"""Signaling and anatomical networks of the C. elegans head, for Dvali et al. (2025).

Dvali, Seguin, Betzel & Leifer (2025), "Diverging Network Architecture of the C. elegans
Connectome and Signaling Network", doi:10.1103/6wgv-b9m6, tested on dandiset 001075 (the
signal propagation atlas of Randi et al. 2023).

What the dandiset holds (segmentation files, read with h5py; pynwb cannot build these files,
see the notebook): per recording the green (GCaMP) and red signals of each segmented ROI,
the NeuroPAL labels, the matching of ROIs to NeuroPAL ROIs, and the stimulation table
(start times and target coordinates). The cited version 0.240920.1434 does not say which ROI
was stimulated; version 0.240930.1859 adds `target_pumpprobe_id`, which is read from it
(`STIM_ID_VERSION`). Files are streamed; nothing is written to disk.

Where the parameters come from:

- The signaling network. The paper keeps pairs with q < 0.05 (Methods, The Networks) and
  does not restate how q is computed (reference 27, Randi et al. 2023). Reading (a) of the
  claims file, recomputing q from the dandiset, needs the control recordings without
  stimulation that Randi et al.'s code uses for its null distribution
  (pumpprobe Funatlas.get_ctrl_distributions, list "No_stim_list.txt"); they are not in the
  dandiset, so reading (b) is used: the wild-type atlas released with Randi et al. 2023,
  `atlas/wild-type.pickle` of https://github.com/leiferlab/worm-functional-connectivity at
  commit 81af01c (`WFC_COMMIT`). Its `scalar_atlas[i, j]` is the response of neuron i to
  stimulation of neuron j, set to NaN where q > 0.05 (pumpprobe
  scripts/fconnectivity/build_wfc_atlas.py, `intensity_map[q>0.05] = np.nan`), on the 188 head
  neurons. An edge runs from stimulated j to responding i (claims file).
- The anatomical network (outside data, as the claims file says). The four EM datasets,
  "three adults and one L4" (Methods, The Networks), are taken as the four sources that
  Randi et al.'s code combines (pumpprobe Funatlas.aconn_sources): White 1986 whole animal
  (adult), White 1986 L4, and Witvliet 2021 datasets 7 and 8 (adults), from
  https://github.com/leiferlab/pumpprobe at commit 1dbc5e0 (`PUMPPROBE_COMMIT`). As in
  pumpprobe `_get_aconnectome_witvliet`, chemical synapses are directed (pre to post) and gap
  junctions count in both directions (the larger of the two directions in each source). An
  edge is any contact in any source (Methods); the controls are an average over the four
  sources of at least 1.25 contacts, and at least three contacts in one source (Methods,
  Network Thresholding Controls).
- Neuron classes and roles: the lists in the paper's code
  (https://github.com/SophieDvali/FunconnNetworkAnalysis at commit 35e87ca, `FNA_COMMIT`;
  richclub.py, SIM.py, broadcaster_integrator.py), which the claims file says match Extended
  Data Figure 5.
- Graph measures follow the paper's code: networkx `average_clustering` on the directed graph
  and the mean shortest path of motifs.py; the rich club coefficient of richclub.py; the
  feed-forward counts of SIM.py and the edge swap of SIM_doubleedge.py; the boundary edge
  ratio of broadcaster_integrator.py.
- Degree-preserving rewiring for the rich club. The paper uses graph-tool
  `random_rewire(g, "configuration")`, which cannot be installed here (graph-tool has no
  PyPI distribution). `rewire_configuration` is a substitute that does what graph-tool's
  default does (one sweep of target swaps over every edge, no self-loops or parallel edges,
  every node's in- and out-degree kept). This is a substitution, recorded as a deviation.
- Rich club thresholds of the control networks (rich-club-controls, reading b). The paper
  reads the thresholds off local maxima of the normalized coefficient "by eye" (richclub.py,
  comment before `neurons_k_gr_3`) and gives no rule. The notebook takes, among the local
  maxima that leave at least 10 neurons, the one with the largest normalized coefficient. This
  is an assumption: it is the simplest rule that gives back the paper's own thresholds on the
  original networks (25 for signaling, 62 for anatomy), which the notebook shows.
"""

from __future__ import annotations

import ast
import io
import json
import pickle
import urllib.request
import warnings
from concurrent.futures import ThreadPoolExecutor

import h5py
import networkx as nx
import numpy as np
import pandas as pd
import remfile
from dandi.dandiapi import DandiAPIClient

DANDISET_ID = "001075"
DANDISET_VERSION = "0.240920.1434"      # the version the paper cites (Methods, reference 88)
STIM_ID_VERSION = "0.240930.1859"       # the next version, which adds target_pumpprobe_id

WFC_REPO = "leiferlab/worm-functional-connectivity"
WFC_COMMIT = "81af01ce37adc041c53aa877c3f05dbd773afb2c"
PUMPPROBE_REPO = "leiferlab/pumpprobe"
PUMPPROBE_COMMIT = "1dbc5e0a2b609d54bc9b1c90c73d4e3bf183d3c7"
FNA_REPO = "SophieDvali/FunconnNetworkAnalysis"
FNA_COMMIT = "35e87cafc1b95ad1496e64b05e9df0700a6bd46e"

ANATOMY_SOURCES = [  # pumpprobe Funatlas.aconn_sources
    "aconnectome_white_1986_whole.csv",
    "aconnectome_white_1986_L4.csv",
    "aconnectome_witvliet_2020_7.csv",
    "aconnectome_witvliet_2020_8.csv",
]

# Lists from the paper's code (richclub.py, SIM.py, broadcaster_integrator.py at FNA_COMMIT).
SENSORY = ['ADEL', 'ADER', 'ADFL', 'ADFR', 'ADLL', 'ADLR', 'AFDL', 'AFDR',
           'AQR', 'ASEL', 'ASER', 'ASGL', 'ASGR', 'ASHL', 'ASHR', 'ASIL',
           'ASIR', 'ASJL', 'ASJR', 'ASKL', 'ASKR', 'AUAL', 'AUAR', 'AVG',
           'AWAL', 'AWAR', 'AWBL', 'AWBR', 'AWCL', 'AWCR', 'BAGL', 'BAGR',
           'CEPDL', 'CEPDR', 'CEPVL', 'CEPVR', 'FLPL', 'FLPR', 'IL1DL',
           'IL1DR', 'IL1L', 'IL1R', 'IL1VL', 'IL1VR', 'IL2DL', 'IL2DR',
           'IL2L', 'IL2R', 'IL2VL', 'IL2VR', 'NSML', 'NSMR', 'OLLL', 'OLLR',
           'OLQDL', 'OLQDR', 'OLQVL', 'OLQVR', 'URADL', 'URADR', 'URAVL',
           'URAVR', 'URBL', 'URBR', 'URXL', 'URXR', 'URYDL', 'URYDR', 'URYVL',
           'URYVR']
INTER = ['ADAL', 'ADAR', 'AIAL', 'AIAR', 'AIBL', 'AIBR', 'AIML',
         'AIMR', 'AINL', 'AINR', 'AIYL', 'AIYR', 'AIZL', 'AIZR', 'ALA',
         'AVAL', 'AVAR', 'AVBL', 'AVBR', 'AVDL', 'AVDR', 'AVEL', 'AVER',
         'AVFL', 'AVFR', 'AVHL', 'AVHR', 'AVJL', 'AVJR', 'AVKL', 'AVKR',
         'AVL', 'I1L', 'I1R', 'I2L', 'I2R', 'I3', 'I4', 'I5', 'I6', 'RIAL',
         'RIAR', 'RIBL', 'RIBR', 'RICL', 'RICR', 'RIFL', 'RIFR', 'RIGL',
         'RIGR', 'RIH', 'RIPL', 'RIPR', 'RIR', 'RIS', 'RIVL', 'RIVR',
         'SAADL', 'SAADR', 'SAAVL', 'SAAVR', 'SABD', 'SABVL', 'SABVR',
         'SIADL', 'SIADR', 'SIAVL', 'SIAVR', 'SIBDL', 'SIBDR', 'SIBVL',
         'SIBVR']
MOTOR = ['AS1', 'DA1', 'DB1', 'DB2', 'DD1', 'M1', 'M2L', 'M2R',
         'M3L', 'M3R', 'M4', 'M5', 'MCL', 'MCR', 'MI', 'RID', 'RIML',
         'RIMR', 'RMDDL', 'RMDDR', 'RMDL', 'RMDR', 'RMDVL', 'RMDVR', 'RMED',
         'RMEL', 'RMER', 'RMEV', 'RMFL', 'RMFR', 'RMGL', 'RMGR', 'RMHL',
         'SMBDL', 'SMBDR', 'SMBVL', 'SMBVR', 'SMDDL', 'SMDDR', 'SMDVL',
         'SMDVR', 'VA1', 'VB1', 'VB2', 'VD1', 'VD2']
PHARYNX = ["I1L", "I1R", "I2L", "I2R", "I3", "I4", "I5", "I6", "M1", "M2L", "M2R",
           "M3L", "M3R", "M4", "M5", "MCL", "MCR", "MI", "NSML", "NSMR"]
AMPHID = ["ADFL", "ADLL", "AFDL", "ASEL", "ASGL", "ASHL", "ASIL", "ASJL", "ASKL", "AWAL", "AWBL",
          "AWCL", "ADFR", "ADLR", "AFDR", "ASER", "ASGR", "ASHR", "ASIR", "ASJR", "ASKR", "AWAR",
          "AWBR", "AWCR"]
# richclub.py, the code's signaling rich club (degree > 25), listed in the claims file.
CODE_RICH_CLUB = ["ASHL", "AVDL", "AVEL", "AVER", "AVJL", "AVJR", "AWBL", "AWBR", "M3L", "M3R",
                  "OLLR", "OLQDR", "RMDDL", "RMDDR", "RMDVL", "RMDVR"]

# The 13 connected triad types counted in motifs.py.
TRIAD_TYPES = ["021D", "021U", "021C", "111D", "111U", "030T", "030C", "201", "120D", "120U",
               "120C", "210", "300"]

# Response window for the link check: the 30 s after stimulation onset, against the 10 s
# before (standard choices for a summary check; pumpprobe's intensity map uses 0 to 30 s).
RESP_WINDOW_S = 30.0
BASE_WINDOW_S = 10.0


def _raw(repo: str, commit: str, path: str) -> bytes:
    url = f"https://raw.githubusercontent.com/{repo}/{commit}/{path}"
    with urllib.request.urlopen(url, timeout=120) as r:
        return r.read()


class _Stub:
    def __setstate__(self, state):
        self.__dict__.update(state if isinstance(state, dict) else {"state": state})


class _AtlasUnpickler(pickle.Unpickler):
    """Reads the atlas without the wormfunconn package (its classes hold only arrays)."""

    def find_class(self, module, name):
        if module.startswith("wormfunconn"):
            return type(name, (_Stub,), {})
        return super().find_class(module, name)


def load_atlas(strain: str = "wild-type"):
    """Neuron names (188 head neurons) and the scalar atlas, NaN where q > 0.05."""
    fa = _AtlasUnpickler(io.BytesIO(_raw(WFC_REPO, WFC_COMMIT, f"atlas/{strain}.pickle"))).load()
    return [str(n) for n in fa.neu_ids], np.asarray(fa.scalar_atlas, dtype=float)


def atlas_attributes(strain: str = "wild-type") -> dict:
    """Every attribute the atlas pickle holds, with its type and shape (to show what it lacks)."""
    fa = _AtlasUnpickler(io.BytesIO(_raw(WFC_REPO, WFC_COMMIT, f"atlas/{strain}.pickle"))).load()
    return {k: (type(v).__name__, getattr(v, "shape", None)) for k, v in fa.__dict__.items()}


def repo_files(repo: str, commit: str) -> dict:
    """Path and size of every file of a GitHub repository at a commit (GitHub API)."""
    url = f"https://api.github.com/repos/{repo}/git/trees/{commit}?recursive=1"
    with urllib.request.urlopen(url, timeout=120) as r:
        tree = json.load(r)
    if tree.get("truncated"):
        raise RuntimeError(f"file list of {repo} truncated by the GitHub API")
    return {e["path"]: e["size"] for e in tree["tree"] if e["type"] == "blob"}


def pypi_files(package: str) -> int:
    """Number of distribution files of a package on PyPI, over all its releases."""
    with urllib.request.urlopen(f"https://pypi.org/pypi/{package}/json", timeout=120) as r:
        d = json.load(r)
    return sum(len(v) for v in d["releases"].values())


def code_lists() -> dict:
    """The neuron lists as written in the paper's code (FNA_COMMIT), parsed from the source, to
    compare with the lists of this module: {(file, variable): list}."""
    out = {}
    for fname, variables in (("SIM.py", ("sensory", "inter", "motor")),
                             ("SIM_doubleedge.py", ("sensory", "inter", "motor")),
                             ("richclub.py", ("sensory", "inter", "motor", "pharynx")),
                             ("broadcaster_integrator.py", ("Amphid", "pharynx"))):
        with warnings.catch_warnings():  # the scripts hold LaTeX labels with backslashes in plain strings
            warnings.simplefilter("ignore", SyntaxWarning)
            tree = ast.parse(_raw(FNA_REPO, FNA_COMMIT, fname).decode())
        for node in tree.body:
            if (isinstance(node, ast.Assign) and len(node.targets) == 1
                    and isinstance(node.targets[0], ast.Name) and node.targets[0].id in variables
                    and isinstance(node.value, ast.List)):
                out[(fname, node.targets[0].id)] = ast.literal_eval(node.value)
    return out


def code_function_source(fname: str, name: str) -> str:
    """Source text of a function in the paper's code (FNA_COMMIT)."""
    text = _raw(FNA_REPO, FNA_COMMIT, fname).decode()
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", SyntaxWarning)
        body = ast.parse(text).body
    for node in body:
        if isinstance(node, ast.FunctionDef) and node.name == name:
            return ast.get_source_segment(text, node)
    raise KeyError(name)


def signaling_adjacency(scalar_atlas: np.ndarray) -> np.ndarray:
    """A[j, i] = 1 for an edge from stimulated j to responding i (q < 0.05), no self-edges."""
    resp_by_stim = np.isfinite(scalar_atlas)
    np.fill_diagonal(resp_by_stim, False)
    return resp_by_stim.T.astype(int)


def load_anatomy(names: list[str], sources: list[str] = ANATOMY_SOURCES, symmetrize_gaps: bool = True):
    """Per source, chemical and gap junction counts as [pre, post] arrays on `names`.

    Gap junctions are symmetrized within each source by the larger direction, as in pumpprobe
    `_get_aconnectome_witvliet` (`symmetrize_gaps=False`, a variant, keeps the listed direction
    only). Contacts with neurons outside `names` are dropped.
    """
    idx = {n: i for i, n in enumerate(names)}
    n = len(names)
    out = {}
    for fname in sources:
        d = pd.read_csv(io.BytesIO(_raw(PUMPPROBE_REPO, PUMPPROBE_COMMIT, f"pumpprobe/{fname}")),
                        sep="\t")
        chem = np.zeros((n, n))
        gap = np.zeros((n, n))
        for r in d.itertuples():
            if r.pre not in idx or r.post not in idx or r.synapses == 0:
                continue
            if r.type == "chemical":
                chem[idx[r.pre], idx[r.post]] += r.synapses
            elif r.type == "electrical":
                gap[idx[r.pre], idx[r.post]] += r.synapses
        out[fname] = (chem, np.maximum(gap, gap.T) if symmetrize_gaps else gap)
    return out


def anatomy_adjacency(sources, mode: str = "any") -> np.ndarray:
    """Binarized anatomical network, A[pre, post].

    mode "any": a contact in any source (Methods, The Networks);
    "avg125": average over the four sources of chemical plus gap contacts >= 1.25;
    "three_total": chemical plus gap contacts >= 3 in at least one source;
    "three_type": chemical >= 3 or gap >= 3 in at least one source (pumpprobe thresholds
    each type separately). The last two are the two readings of "at least three synaptic
    contacts between them in at least one of the connectomes".
    """
    mats = list(sources.values())
    n = mats[0][0].shape[0]
    if mode == "any":
        a = sum(c + g for c, g in mats) > 0
    elif mode == "avg125":
        a = sum(c + g for c, g in mats) / len(mats) >= 1.25
    elif mode == "three_total":
        a = np.zeros((n, n), bool)
        for c, g in mats:
            a |= (c + g) >= 3
    elif mode == "three_type":
        a = np.zeros((n, n), bool)
        for c, g in mats:
            a |= (c >= 3) | (g >= 3)
    else:
        raise ValueError(mode)
    a = a.copy()
    np.fill_diagonal(a, False)
    return a.astype(int)


def density(a: np.ndarray) -> float:
    n = a.shape[0]
    return a.sum() / (n * (n - 1))


def mean_shortest_path(g: nx.DiGraph) -> float:
    """motifs.py: mean over sources of the mean path length to the nodes they reach (self at 0)."""
    return float(np.mean([np.mean(list(d.values())) for _, d in nx.shortest_path_length(g)]))


def small_world(a: np.ndarray, p: float, rng: np.random.Generator, n_er: int = 100):
    """Clustering, path length and sigma against `n_er` directed Erdos-Renyi graphs (motifs.py)."""
    g = nx.DiGraph(a)
    c = nx.average_clustering(g)
    l_ = mean_shortest_path(g)
    cs, ls = [], []
    for _ in range(n_er):
        ger = nx.erdos_renyi_graph(a.shape[0], p, directed=True, seed=int(rng.integers(2**31)))
        cs.append(nx.average_clustering(ger))
        ls.append(mean_shortest_path(ger))
    sigma = (c / np.mean(cs)) / (l_ / np.mean(ls))
    return dict(C=c, L=l_, C_ER=float(np.mean(cs)), L_ER=float(np.mean(ls)), sigma=float(sigma))


def triad_counts(a: np.ndarray) -> dict:
    """Counts of the 13 connected triad types. networkx `triadic_census` gives the same counts
    as `triads_by_type` (used in motifs.py) and is faster."""
    census = nx.triadic_census(nx.DiGraph(a))
    return {t: census[t] for t in TRIAD_TYPES}


def total_degree(a: np.ndarray) -> np.ndarray:
    return a.sum(0) + a.sum(1)


def rich_club_phi(a: np.ndarray, kmax: int | None = None) -> np.ndarray:
    """richclub.py: phi(k) = E_k / (N_k (N_k - 1)) over nodes of total degree > k."""
    deg = total_degree(a)
    kmax = int(deg.max()) if kmax is None else kmax
    phi = np.full(kmax, np.nan)
    for k in range(kmax):
        sel = deg > k
        nk = sel.sum()
        if nk > 1:
            phi[k] = a[np.ix_(sel, sel)].sum() / (nk * (nk - 1))
    return phi


def rewire_configuration(a: np.ndarray, rng: np.random.Generator) -> np.ndarray:
    """Degree-preserving rewiring standing in for graph-tool random_rewire(g, "configuration").

    One sweep: each edge in random order is paired with a random other edge and their targets
    are swapped, unless that creates a self-loop or a parallel edge (graph-tool's defaults,
    n_iter=1, edge_sweep=True, no self-loops or parallel edges). In- and out-degrees are kept.
    """
    src, dst = np.nonzero(a)
    m = len(src)
    eset = set(zip(src.tolist(), dst.tolist()))
    src = src.tolist()
    dst = dst.tolist()
    order = rng.permutation(m)
    partners = rng.integers(0, m, size=m)
    for e, f in zip(order, partners):
        if e == f:
            continue
        u, v, x, y = src[e], dst[e], src[f], dst[f]
        if u == y or x == v or v == y:
            continue
        if (u, y) in eset or (x, v) in eset:
            continue
        eset.discard((u, v))
        eset.discard((x, y))
        eset.add((u, y))
        eset.add((x, v))
        dst[e], dst[f] = y, v
    out = np.zeros_like(a)
    out[src, dst] = 1
    return out


def swapping_edges(a: np.ndarray, rng: np.random.Generator, nswap: int = 2000,
                   max_tries: int = 4000) -> np.ndarray:
    """Port of `swapping_edges` in SIM_doubleedge.py: x->y and a->b become x->b and a->y.

    Sources are drawn with probability proportional to total degree, targets uniformly among
    each source's successors; a swap that would create a parallel edge is skipped. As in the
    code, self-loops are not prevented, and at most `max_tries` attempts are made for `nswap`
    swaps.
    """
    succ = [np.nonzero(a[i])[0].tolist() for i in range(a.shape[0])]
    succ_set = [set(x) for x in succ]
    deg = total_degree(a).astype(float)
    pairs = rng.choice(len(deg), size=(max_tries + 1, 2), p=deg / deg.sum())
    picks = rng.random((max_tries + 1, 2))
    swaps = 0
    for tries in range(max_tries + 1):
        if swaps >= nswap:
            break
        ui, xi = pairs[tries]
        if ui == xi or not succ[ui] or not succ[xi]:
            continue
        vi = int(picks[tries, 0] * len(succ[ui]))
        yi = int(picks[tries, 1] * len(succ[xi]))
        v, y = succ[ui][vi], succ[xi][yi]
        if v == y or y in succ_set[ui] or v in succ_set[xi]:
            continue
        succ[ui][vi], succ[xi][yi] = y, v
        succ_set[ui].discard(v)
        succ_set[ui].add(y)
        succ_set[xi].discard(y)
        succ_set[xi].add(v)
        swaps += 1
    out = np.zeros_like(a)
    for i, t in enumerate(succ):
        out[i, t] = 1
    return out


def class_flow(a: np.ndarray, labels: np.ndarray) -> dict:
    """Edge counts between classes S, I, M (SIM.py): keys like 'SI' for sensory to inter."""
    out = {}
    for s in "SIM":
        for t in "SIM":
            out[s + t] = int(a[np.ix_(labels == s, labels == t)].sum())
    return out


def feedforward_measures(flow: dict) -> dict:
    """log(N forward / N backward) per leg, and the code's log ratio of out-edge fractions."""
    res = {}
    tot = {s: sum(flow[s + t] for t in "SIM") for s in "SIM"}
    for f, b in (("SI", "IS"), ("IM", "MI"), ("SM", "MS")):
        with np.errstate(divide="ignore", invalid="ignore"):
            res["count_" + f] = np.log(flow[f] / flow[b]) if flow[b] and flow[f] else np.nan
            pf = flow[f] / tot[f[0]] if tot[f[0]] else np.nan
            pb = flow[b] / tot[b[0]] if tot[b[0]] else np.nan
            res["frac_" + f] = np.log(pf / pb) if pf and pb else np.nan
    return res


def boundary_ratio(a: np.ndarray, members: np.ndarray) -> tuple[int, int]:
    """Edges into a group from outside, and out of it to outside (broadcaster_integrator.py)."""
    into = int(a[np.ix_(~members, members)].sum())
    out = int(a[np.ix_(members, ~members)].sum())
    return into, out


# ----------------------------------------------------------------------------------------------
# Dandiset


def _s(x) -> str:
    return x.decode() if isinstance(x, bytes) else str(x)


def list_segmentation_assets(version: str = DANDISET_VERSION):
    ds = DandiAPIClient().get_dandiset(DANDISET_ID, version)
    return ds, sorted((a for a in ds.get_assets() if "desc-segmentation" in a.path),
                      key=lambda a: a.path)


def _open(asset):
    url = asset.get_content_url(follow_redirects=1, strip_query=True)
    return h5py.File(remfile.File(url), "r")


def read_session(asset, with_signal: bool = True) -> dict:
    """One recording: labels, ROI matching, stimulation table and, optionally, the green signal."""
    f = _open(asset)
    sub = f["general/subject"]
    npal = f["processing/ophys/NeuroPALSegmentations/NeuroPALPlaneSegmentation"]
    pp_ = f["processing/ophys/PumpProbeGreenSegmentations/PumpProbeGreenPlaneSegmentation"]
    st = f["intervals/OptogeneticStimulusTable"]
    gs = f["processing/ophys/GreenSignals/GreenSignal"]
    np_labels = [_s(x).strip() for x in npal["labels"][:]]
    np_ids = npal["id"][:].tolist()
    np_label_of = dict(zip(np_ids, np_labels))
    pp_np = [_s(x).strip() for x in pp_["neuropal_ids"][:]]
    # Non-numeric entries ("merge") are ROIs not matched to a single NeuroPAL ROI.
    roi_label = [np_label_of.get(int(x), "") if x.isdigit() else "" for x in pp_np]
    region = gs["table_region"][:]
    r = dict(
        path=asset.path,
        strain=_s(sub["strain"][()]), genotype=_s(sub["genotype"][()]),
        stage=_s(sub["growth_stage"][()]), start=_s(f["session_start_time"][()]),
        np_labels=np_labels, roi_label=roi_label, signal_rois=region,
        stim_start=st["start_time"][:], stim_stop=st["stop_time"][:],
        timestamps=gs["timestamps"][:], signal_shape=gs["data"].shape,
        red_shape=f["processing/ophys/RedSignals/RedSignal/data"].shape,
        red_same_clock=bool(np.array_equal(f["processing/ophys/RedSignals/RedSignal/timestamps"][:],
                                           gs["timestamps"][:])),
    )
    if with_signal:
        r["green"] = gs["data"][:]
    f.close()
    return r


def read_stim_ids(asset) -> dict:
    """From STIM_ID_VERSION: `target_pumpprobe_id` of each stimulation (NaN where not assigned),
    the stimulation start times, and the green signal with its missing frames left as NaN
    (`BaseGreenSignal`), to compare with the cited version's `GreenSignal`."""
    f = _open(asset)
    ids = f["intervals/OptogeneticStimulusTable/target_pumpprobe_id"][:]
    start = f["intervals/OptogeneticStimulusTable/start_time"][:]
    base = f["processing/ophys/GreenSignals/BaseGreenSignal/data"][:]
    f.close()
    return dict(ids=ids, start=start, base=base)


def load_sessions(with_signal: bool = True, workers: int = 8, limit: int | None = None):
    """All segmentation files of the pinned version, with stimulated-ROI ids from the next one."""
    _, assets = list_segmentation_assets(DANDISET_VERSION)
    _, later = list_segmentation_assets(STIM_ID_VERSION)
    later = {a.path: a for a in later}
    if limit is not None:
        assets = assets[:limit]
    with ThreadPoolExecutor(workers) as ex:
        sessions = list(ex.map(lambda a: read_session(a, with_signal), assets))
        stims = list(ex.map(lambda a: read_stim_ids(later[a.path]), assets))
    for s, t in zip(sessions, stims):
        s["later"] = t
    return sessions


def stimulated_labels(session: dict) -> list[str]:
    """Label of the stimulated ROI for each stimulation ('' where unassigned or unlabeled)."""
    out = []
    for x in session["later"]["ids"]:
        if not np.isfinite(x) or int(x) < 0 or int(x) >= len(session["roi_label"]):
            out.append("")
        else:
            out.append(session["roi_label"][int(x)])
    return out


def responses(session: dict, shift_s: float = 0.0):
    """Mean dF/F of every ROI in the RESP_WINDOW_S after each stimulation, over the
    BASE_WINDOW_S before it; returns an array (n_stim, n_roi), NaN where a window is empty."""
    t = session["timestamps"]
    y = session["green"]
    out = np.full((len(session["stim_start"]), y.shape[1]), np.nan)
    for k, t0 in enumerate(session["stim_start"] + shift_s):
        pre = (t >= t0 - BASE_WINDOW_S) & (t < t0)
        post = (t >= t0) & (t < t0 + RESP_WINDOW_S)
        if pre.sum() < 3 or post.sum() < 3:
            continue
        with np.errstate(invalid="ignore", divide="ignore"):
            b = np.nanmean(y[pre], axis=0)
            out[k] = np.nanmean(y[post], axis=0) / b - 1
    return out
