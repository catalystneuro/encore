"""Loading and state space measures for CRCNS vim-4 (Zhang, Gao, Cukur & Gallant 2021).

The data set is streamed from the public CRCNS bucket; nothing is written to disk.

Where each method comes from:

- State space: the paper's Methods ("Voxel-Based State Space Modeling") and its
  code, gallantlab/state-space at commit 6ffb3c3, `extract_state_space_positions`
  (claims file, opening comment): OLS of the responses on the task variables
  with an intercept column (pinv of the normal equations), PCA with 24
  components on the [TR x voxel] responses, denoised weights U U^T B^T, the
  first (variables) columns of Q from the QR of the denoised weights, positions
  = responses x those columns, z-scored per dimension over the TRs fitted.
- Computation in PC space (an exact rewrite, not a change of method): every
  denoised weight vector lies in the span of the 24 components C (24 x voxels,
  orthonormal rows), so with Z = Y C^T the OLS coefficients projected on the
  components are pinv(P^T P) P^T Z, the QR of C^T M equals C^T times the QR of
  M, and the positions are Z Q_M. The PCA itself is computed exactly from the
  TR x TR Gram matrix Y Y^T (the eigenvectors of the centred Gram matrix); the
  code's scikit-learn PCA(24) uses a randomized solver for this shape, which
  approximates the same components. The notebook compares the two on one
  subject.
- JSD: the code's `JSD`, a Monte Carlo estimate from 1000 samples of each
  normal, in log base 2; computed here in the log domain (log-sum-exp), which
  gives the same values without the underflow of the code's ratio of
  densities. CSI: the mean JSD over all pairs of clusters (Methods,
  "Quantification of State Space Results", paragraph 1). Cluster normals use
  the sample mean and covariance (ddof 1), a standard choice.
- The JSD between two normals is unchanged by any invertible affine map applied
  to both, so the CSI does not depend on the signs, order or z-scoring of the
  state dimensions, only on the subspace they span.
- Cross-validation: 10 folds, the state space refitted on the training TRs
  (PCA included), held-out TRs projected and assigned to the nearest training
  cluster (Methods, paragraph 2). Folds, distance and z-scoring of held-out TRs
  are readings named in the claims file.
- Cortical regions (att-weights-cortex, game-weights-two-groups): the paper's
  per-subject ROIs are not public, and the claims file allows an fsaverage atlas
  through the data set's mappers. Regions are unions of visfAtlas and
  HCP-MMP1.0 areas (an assumption, listed in ATT_REGIONS and GAME_REGIONS); a
  region's mean of a voxel map is the mean over its fsaverage vertices that the
  mapper reaches. Weights per region are computed exactly from the
  region-averaged responses (region_weights). The encoding-model thresholds are
  the claims file's readings (ii), with the details stated in semantic_model_r
  and cv_ols_r.
"""
import fsspec
import h5py
import numpy as np
from scipy import linalg

BASE = "https://crcnsarchive.s3-us-west-2.amazonaws.com/vim-4/live/"
DOI = "10.6080/K0668BDF"
VERSION = "unversioned"
ATT_SUBJECTS = ["S1", "S2", "S3", "S5", "S6"]  # S4 not released (data description)
GAME_SUBJECTS = ["S1", "S7"]
CONDITIONS = ["passive", "human", "vehicle"]  # stacking order of the code's Example.ipynb
N_PCS = 24  # Methods, "Voxel-Based State Space Modeling", paragraph 3
TABLE1_ORDER = ["dead", "round start", "safe explore", "unsafe explore", "kill",
                "engage close", "engage far", "flash", "run away"]
PRESENCE_NAMES = ["neither", "humans only", "vehicles only", "both"]


def _open(path, block_size=2**24):
    return fsspec.open(BASE + path, block_size=block_size).open()


def read_hdf(path, keys=None):
    """Read whole datasets of a small HDF5 file into memory."""
    with _open(path) as f, h5py.File(f, "r") as h:
        keys = list(h.keys()) if keys is None else keys
        return {k: h[k][()] for k in keys}


def hdf_layout(path):
    """Names, shapes and dtypes of every dataset in an HDF5 file (no data read)."""
    out = []
    with _open(path, 2**20) as f, h5py.File(f, "r") as h:
        h.visititems(lambda n, o: out.append((n, o.shape, str(o.dtype)))
                     if isinstance(o, h5py.Dataset) else None)
    return out


def npy_layout(path):
    with _open(path, 2**16) as f:
        np.lib.format.read_magic(f)
        shape, _, dtype = np.lib.format.read_array_header_1_0(f)
    return shape, str(dtype)


def load_attention_states():
    """[TR x 3] states per condition: human presence, vehicle presence, attention."""
    return read_hdf("VisualAttention/Stimuli/states.hdf", CONDITIONS)


def presence_code(states):
    """0 neither, 1 humans only, 2 vehicles only, 3 both (as in Example.ipynb)."""
    return (states[:, 0] + 2 * states[:, 1]).astype(int)


def gram_summary(Y):
    """Gram matrix and per-voxel summaries of a [TR x voxel] array."""
    sd = Y.std(0)
    return {"G": Y @ Y.T, "n_vox": Y.shape[1], "n_zero_vox": int((sd == 0).sum()),
            "vox_mean_range": (float(Y.mean(0).min()), float(Y.mean(0).max())),
            "vox_sd_range": (float(sd[sd > 0].min()), float(sd.max())),
            "n_nan": int(np.isnan(Y).sum())}


def code_positions(X, Y, num_PCs=N_PCS):
    """The paper's code, `extract_state_space_positions` (gallantlab/state-space
    at 6ffb3c3), on the full voxel data, kept as written to check the PC-space
    rewrite."""
    from scipy import stats
    from sklearn.decomposition import PCA
    parameters = np.ones([X.shape[0], X.shape[1] + 1])
    parameters[:, :-1] = X
    covar = parameters.T @ parameters
    coeffs = np.linalg.pinv(covar) @ (parameters.T @ Y)
    pca = PCA(num_PCs, random_state=0)
    pca.fit(Y)
    coeffs_denoised = pca.components_.T @ (pca.components_ @ coeffs.T)
    Q, _ = np.linalg.qr(coeffs_denoised)  # reduced QR: same first columns as 'full'
    return stats.zscore(Y @ Q[:, :X.shape[1]])


def load_attention_gram(subject, X_check=None, keep=None):
    """Stream one subject's deconvolved responses, stacked passive, human, vehicle.

    Returns the 2700 x 2700 Gram matrix and summaries; the voxel data are
    dropped. With X_check, also the positions from the paper's code on the full
    voxel data and the norm of each row of its OLS coefficients (`coeffs`, voxel
    space). With keep, also the responses of those voxels (float32).
    """
    with _open(f"VisualAttention/Data/deconv/{subject}.hdf") as f, h5py.File(f, "r") as h:
        Y = np.vstack([h[c][()] for c in CONDITIONS])
    out = gram_summary(Y)
    if X_check is not None:
        out["code_positions"] = code_positions(X_check, Y)
        P = np.column_stack([X_check, np.ones(len(X_check))])
        out["code_coef_norm"] = np.linalg.norm(np.linalg.pinv(P.T @ P) @ (P.T @ Y), axis=1)
    if keep is not None:
        out["Y_keep"] = Y[:, keep].astype(np.float32)
    del Y
    return out


def load_game(subject, keep=None):
    """Stream one subject's video game BOLD (npy) and its state labels.

    Also the voxel maps of the OLS weights B and denoised weights B_L of every state (data
    set column order, states with no TRs dropped), for the correlation variant of
    game-weights-two-groups, and with keep the responses of those voxels (float32).
    """
    with _open(f"VideoGame/Data/{subject}.npy") as f:
        np.lib.format.read_magic(f)
        shape, fortran, dtype = np.lib.format.read_array_header_1_0(f)
        Y = np.frombuffer(f.read(), dtype=dtype).reshape(shape).astype(np.float64)
    out = gram_summary(Y)
    st = read_hdf(f"VideoGame/Stimuli/{subject}.hdf")
    out["X"] = st["behavioural_state"].astype(float)
    out["labels"] = [s.decode().strip().lower() for s in st["state_labels"]]
    X, names = game_matrix(out["X"], out["labels"], "dataset")
    Z, _, _ = pca_scores(out["G"], np.arange(len(Y)))
    P = np.column_stack([X, np.ones(len(X))])
    pinv = np.linalg.pinv(P.T @ P)
    coef = (pinv @ (P.T @ Z))[:-1]
    out["B_vox"] = (pinv @ (P.T @ Y))[:-1]
    out["BL_vox"] = ((Y - Y.mean(0)).T @ ((Z / (Z ** 2).sum(0)) @ coef.T)).T
    out["map_names"] = names
    if keep is not None:
        out["Y_keep"] = Y[:, keep].astype(np.float32)
    del Y
    return out


# ---------------------------------------------------------------- PCA from Gram

def pca_scores(G, train, test=None, k=N_PCS):
    """Scores on the top-k principal components fitted to the training TRs.

    G is Y Y^T over all TRs. Training rows are centred on their own mean, as
    scikit-learn's PCA does; held-out rows are centred with the training mean.
    Returns (Z_train, Z_test or None, fraction of training variance explained).
    """
    train = np.asarray(train)
    Gtt = G[np.ix_(train, train)]
    rs = Gtt.mean(1)
    tot = rs.mean()
    Gc = Gtt - rs[:, None] - rs[None, :] + tot
    n = len(train)
    w, U = linalg.eigh(Gc, subset_by_index=[n - k, n - 1])
    w, U = w[::-1], U[:, ::-1]
    Z_tr = U * np.sqrt(w)
    Z_te = None
    if test is not None:
        test = np.asarray(test)
        Gx = G[np.ix_(test, train)]
        cross = Gx - Gx.mean(1)[:, None] - rs[None, :] + tot
        Z_te = cross @ U / np.sqrt(w)
    return Z_tr, Z_te, float(w.sum() / np.trace(Gc))


# ---------------------------------------------------------------- state space

def state_directions(Z, X):
    """Q_M and R: the QR of the denoised weights in PC coordinates.

    Z [TR x 24] PCA scores, X [TR x d] task variables. The intercept column is
    last, as in the code, so it does not change the first d directions.
    """
    P = np.column_stack([X, np.ones(len(X))])
    coef = np.linalg.pinv(P.T @ P) @ (P.T @ Z)  # (d+1) x 24, = B C^T
    Q, R = np.linalg.qr(coef.T)  # 24 x (d+1)
    d = X.shape[1]
    return Q[:, :d], R[:d, :d]


def positions(Z, X, sign=None):
    """Z-scored state space positions of the fitted TRs.

    sign: None (as the QR returns), "diag" (diagonal of R made positive) or
    "own" (each dimension oriented so its own variable's TRs, X[:, j] > 0, have
    a positive mean position).
    """
    Q, R = state_directions(Z, X)
    if sign == "diag":
        Q = Q * np.sign(np.diag(R))
    pos = Z @ Q
    pos = (pos - pos.mean(0)) / pos.std(0)
    if sign == "own":
        for j in range(X.shape[1]):
            if X[:, j].any() and pos[X[:, j] > 0, j].mean() < 0:
                pos[:, j] *= -1
    return pos


# ---------------------------------------------------------------- JSD and CSI

def _fit_normal(x):
    m = x.mean(0)
    c = np.cov(x, rowvar=False, ddof=1)
    return m, linalg.cholesky(np.atleast_2d(c), lower=True)


def _logpdf(x, m, L):
    sol = linalg.solve_triangular(L, (x - m).T, lower=True)
    d = len(m)
    return -0.5 * (sol ** 2).sum(0) - np.log(np.diag(L)).sum() - 0.5 * d * np.log(2 * np.pi)


def jsd(n1, n2, rng, samples=1000):
    """Monte Carlo JSD (bits) between two fitted normals (m, cholesky)."""
    (m1, L1), (m2, L2) = n1, n2
    d = len(m1)
    s1 = m1 + rng.standard_normal((samples, d)) @ L1.T
    s2 = m2 + rng.standard_normal((samples, d)) @ L2.T
    # log2(p_a / ((p_a + p_b) / 2)) = 1 - log2(1 + p_b / p_a)
    a = 1 - np.logaddexp(0, _logpdf(s1, m2, L2) - _logpdf(s1, m1, L1)) / np.log(2)
    b = 1 - np.logaddexp(0, _logpdf(s2, m1, L1) - _logpdf(s2, m2, L2)) / np.log(2)
    return 0.5 * (a.mean() + b.mean())


def csi(pos, members, rng, samples=1000):
    """Cluster separation index: mean pairwise JSD of the clusters' normals.

    members: list of boolean or index arrays, one per cluster.
    """
    normals = [_fit_normal(pos[m]) for m in members]
    vals = [jsd(normals[i], normals[j], rng, samples)
            for i in range(len(normals)) for j in range(i + 1, len(normals))]
    return float(np.mean(vals))


# ---------------------------------------------------------------- classification

def nearest_cluster(train_pos, train_lab, test_pos, classes, rule):
    """Assign each test point to the nearest training cluster.

    rule "euclid": Euclidean distance to the cluster mean; "density": highest
    density under the cluster's fitted normal.
    """
    if rule == "euclid":
        means = np.array([train_pos[train_lab == c].mean(0) for c in classes])
        d2 = ((test_pos[:, None, :] - means[None]) ** 2).sum(-1)
        return np.asarray(classes)[d2.argmin(1)]
    ll = np.column_stack([_logpdf(test_pos, *_fit_normal(train_pos[train_lab == c]))
                          for c in classes])
    return np.asarray(classes)[ll.argmax(1)]


def folds(n, scheme, rng, k=10):
    """Test indices of k folds: "contig" (contiguous tenths) or "random"."""
    idx = np.arange(n) if scheme == "contig" else rng.permutation(n)
    return np.array_split(idx, k)


def fold_scores(G, test_sets):
    """PCA scores per fold: list of (train, test, Z_train, Z_test)."""
    n = G.shape[0]
    out = []
    for te in test_sets:
        tr = np.setdiff1d(np.arange(n), te)
        Ztr, Zte, _ = pca_scores(G, tr, te)
        out.append((tr, te, Ztr, Zte))
    return out


def project_fold(Ztr, Zte, Xtr):
    """Training and held-out positions; held-out z-scored with training statistics."""
    Q, _ = state_directions(Ztr, Xtr)
    ptr, pte = Ztr @ Q, Zte @ Q
    m, s = ptr.mean(0), ptr.std(0)
    return (ptr - m) / s, (pte - m) / s


# ---------------------------------------------------------------- attention task

def att_positions(Z, X, third, rng=None):
    """Positions in the attention state space under a reading of its third axis.

    In the deposited deconvolved data each attentive condition is z-scored per
    voxel, so the attention variable (-1, 0, +1) has an OLS weight of zero up to
    rounding and the third QR direction is set by rounding noise.
    third: "qr" (as the QR returns it), "2d" (human and vehicle axes only) or
    "random" (a random unit direction in the PC space, orthogonal to the
    first two, drawn from rng).
    """
    Q, _ = state_directions(Z, X)
    if third == "2d":
        Q = Q[:, :2]
    elif third == "random":
        v = rng.standard_normal(Q.shape[0])
        v -= Q[:, :2] @ (Q[:, :2].T @ v)
        Q = np.column_stack([Q[:, :2], v / np.linalg.norm(v)])
    pos = Z @ Q
    return (pos - pos.mean(0)) / pos.std(0)


def cond_slices(n_per=900):
    return [slice(i * n_per, (i + 1) * n_per) for i in range(len(CONDITIONS))]


def att_csis(pos, pcode, rng, members=None):
    """CSI of the four presence clusters within each condition (passive, human, vehicle).

    members: optional list of three index arrays giving each condition's TRs.
    """
    members = cond_slices() if members is None else members
    out = []
    for m in members:
        p, c = pos[m], pcode[m]
        out.append(csi(p, [c == k for k in range(4)], rng))
    return np.array(out)


def shuffle_presence(X, reading, rng):
    """Permuted presence labels: "a" rows of (human, vehicle) shuffled over all
    TRs; "b" circularly shifted by a random lag within each condition."""
    Xp = X.copy()
    if reading == "a":
        Xp[:, :2] = X[rng.permutation(len(X)), :2]
    else:
        for s in cond_slices():
            Xp[s, :2] = np.roll(X[s, :2], rng.integers(1, s.stop - s.start), axis=0)
    return Xp


def shuffle_conditions(n_per, scheme, rng):
    """Permuted condition membership for the passive-against-attentive test.

    Returns three index arrays (passive, human, vehicle). "matched": at each
    movie time point the three TRs showing the same frame are given the three
    conditions in random order, so every condition keeps the same presence
    labels; "global": TRs shuffled across all conditions. A standard choice for
    a detail the claims file does not fix; both are run.
    """
    n = n_per * 3
    if scheme == "global":
        p = rng.permutation(n)
        return [np.sort(p[i * n_per:(i + 1) * n_per]) for i in range(3)]
    order = np.argsort(rng.random((n_per, 3)), axis=1)  # condition of each copy
    t = np.arange(n_per)
    return [np.sort(np.concatenate([c * n_per + t[order[:, c] == k] for c in range(3)]))
            for k in range(3)]


def members_to_X(X, members):
    """State matrix with the attention column set by the permuted membership."""
    Xp = X.copy()
    for value, m in zip([0.0, -1.0, 1.0], members):
        Xp[m, 2] = value
    return Xp


# ---------------------------------------------------------------- video game

def game_matrix(X, labels, order):
    """State matrix with columns in dataset order or Table 1 order; states with
    no TRs are dropped (flash in S7), as Supplementary Figure 4 has no flash
    weights for that subject."""
    names = labels if order == "dataset" else [s for s in TABLE1_ORDER if s in labels]
    cols = [labels.index(s) for s in names]
    keep = [i for i, c in enumerate(cols) if X[:, c].any()]
    return X[:, [cols[i] for i in keep]], [names[i] for i in keep]


def game_members(X, names, reading):
    """Clusters for the video game CSI.

    "a" one per state, a TR in the cluster of every state it has; "b" one per
    state from TRs with exactly one state; "c" safe explore, engage close and
    all other TRs (Figure 3A). Clusters with no more TRs than dimensions are
    left out (no covariance can be fitted).
    """
    d = X.shape[1]
    if reading == "c":
        se, ec = X[:, names.index("safe explore")] > 0, X[:, names.index("engage close")] > 0
        mem, nm = [se, ec, ~se & ~ec], ["safe explore", "engage close", "other"]
    else:
        ok = np.ones(len(X), bool) if reading == "a" else X.sum(1) == 1
        mem = [(X[:, j] > 0) & ok for j in range(d)]
        nm = list(names)
    keep = [i for i, m in enumerate(mem) if m.sum() > d]
    dropped = [(nm[i], int(mem[i].sum())) for i in range(len(mem)) if i not in keep]
    return [mem[i] for i in keep], [nm[i] for i in keep], dropped


def projection_matrix(pos, X):
    """M[i, j]: mean position on dimension j of the TRs that have state i."""
    return np.array([pos[X[:, i] > 0].mean(0) for i in range(X.shape[1])])


def balanced_accuracy(H, pred, classes):
    """Balanced accuracy (Brodersen et al. 2010, cited by the paper): the mean
    recall over the classes present. H [TR x classes] is True where a TR has
    the class (a TR may have several); the recall of class c is the fraction
    of the TRs that have c that are predicted as c."""
    rec = [(pred[H[:, k]] == c).mean() for k, c in enumerate(classes) if H[:, k].any()]
    return float(np.mean(rec))


# ---------------------------------------------------------------- cortical regions

VISF_URL = "https://download.brainvoyager.com/data/visfAtlas.zip"
VISF_SHA256 = "2eae192d3aeab8f9812991c8a9bc2822d10c4d0a621172aaa43df1900660799d"
HCP_URL = {"lh": "https://ndownloader.figshare.com/files/5528816",
           "rh": "https://ndownloader.figshare.com/files/5528819"}
HCP_MD5 = {"lh": "46a102b59b2fb1bb4bd62d51bf02e975", "rh": "75e96b331940227bbcb07c1c791c2463"}

# Regions of the claims, as unions of atlas areas on fsaverage (an assumption: the paper's
# ROIs were drawn per subject from localizers, which are not public).
# visfAtlas (Rosenke et al. 2021, doi:10.1093/cercor/bhaa246): the face areas on the
# fusiform (mFus, pFus) form the FFA, IOG-faces is the OFA, the lateral body areas (LOS, ITG,
# MTG) form the EBA, CoS-places is the PPA and TOS-places (right hemisphere only) the OPA.
# HCP-MMP1.0 (Glasser et al. 2016, on fsaverage: doi:10.6084/m9.figshare.3498446.v2) for the
# regions visfAtlas lacks, with the area names of Glasser et al. (2016), Supplementary
# Neuroanatomical Results.
ATT_REGIONS = {
    "FFA": ("visf", ["mFus-faces", "pFus-faces"]),
    "OFA": ("visf", ["IOG-faces"]),
    "EBA": ("visf", ["LOS-bodies", "ITG-bodies", "MTG-bodies"]),
    "MT+": ("visf", ["hMT"]),
    "PPA": ("visf", ["CoS-places"]),
    "OPA": ("visf", ["TOS-places"]),
    "RSC": ("hcp", ["RSC"]),
    "LO": ("hcp", ["LO1", "LO2", "LO3"]),
    "FO": ("hcp", ["FOP1", "FOP2", "FOP3", "FOP4", "FOP5"]),
    "IFS": ("hcp", ["IFSa", "IFSp"]),
    "IPS": ("hcp", ["IPS1", "IP0", "IP1", "IP2", "LIPv", "LIPd", "VIP", "MIP", "AIP"]),
    "FEF": ("hcp", ["FEF"]),
    "SEF": ("hcp", ["SCEF"]),
    # variants of the body, face and place areas, not used by the criterion
    "LOS-bodies": ("visf", ["LOS-bodies"]),
    "ITG-bodies": ("visf", ["ITG-bodies"]),
    "MTG-bodies": ("visf", ["MTG-bodies"]),
    "OTS-bodies": ("visf", ["OTS-bodies"]),
    "FFC (HCP)": ("hcp", ["FFC"]),
    "PHA1-3 (HCP)": ("hcp", ["PHA1", "PHA2", "PHA3"]),
    "POS1 (HCP)": ("hcp", ["POS1"]),
}
_PFC = ["8C", "8Av", "i6-8", "s6-8", "SFL", "8BL", "9p", "9a", "8Ad", "p9-46v", "a9-46v", "46", "9-46d",
        "44", "45", "47l", "a47r", "p47r", "IFJa", "IFJp", "IFSa", "IFSp",
        "10d", "10pp", "a10p", "p10p", "11l", "13l", "OFC", "47m", "47s", "pOFC",
        "10r", "10v", "9m", "8BM", "p32", "d32", "s32", "a24", "25"]
GAME_REGIONS = {
    "TPJ": ("hcp", ["TPOJ1", "TPOJ2", "TPOJ3", "PGi", "PGs"]),
    "precuneus": ("hcp", ["7m", "PCV", "POS2", "31pd", "31pv"]),
    "prefrontal": ("hcp", _PFC),
    "motor": ("hcp", ["4"]),
    "premotor": ("hcp", ["6a", "6d", "6v", "6r", "55b", "PEF"]),
    "SMA": ("hcp", ["6ma", "6mp"]),
    "IPS": ATT_REGIONS["IPS"],
    "FEF": ("hcp", ["FEF"]),
    "SEF": ("hcp", ["SCEF"]),
}


def parse_annot(buf):
    """Vertex labels and names of a FreeSurfer .annot file (bytes), new colour table format."""
    import io
    f = io.BytesIO(buf)
    i4 = lambda n=1: np.frombuffer(f.read(4 * n), ">i4")
    vnum = int(i4()[0])
    vd = i4(2 * vnum).reshape(-1, 2)
    values = np.zeros(vnum, np.int64)
    values[vd[:, 0]] = vd[:, 1]
    assert int(i4()[0]) == 1  # colour table present
    assert int(i4()[0]) == -2  # version 2
    i4()  # max structure id
    f.read(int(i4()[0]))  # name of the original table
    names, codes = [], []
    for _ in range(int(i4()[0])):
        i4()  # structure id
        names.append(f.read(int(i4()[0])).rstrip(b"\x00").decode())
        r, g, b, _t = i4(4)
        codes.append(int(r) + int(g) * 256 + int(b) * 65536)
    lookup = dict(zip(codes, names))
    return np.array([lookup.get(int(v), "") for v in values])


def load_atlases():
    """Vertex names per hemisphere for both atlases: {"visf"|"hcp": {"lh": names, "rh": names}}.

    Each file is read into memory and checked against its published checksum."""
    import hashlib, io, zipfile
    import requests
    z = requests.get(VISF_URL, timeout=600).content
    assert hashlib.sha256(z).hexdigest() == VISF_SHA256
    out = {"visf": {}, "hcp": {}}
    with zipfile.ZipFile(io.BytesIO(z)) as zf:
        for h in ("lh", "rh"):
            out["visf"][h] = parse_annot(zf.read(f"visfAtlas/FreeSurfer/{h}.visfAtlas.annot"))
    for h in ("lh", "rh"):
        b = requests.get(HCP_URL[h], timeout=600).content
        assert hashlib.md5(b).hexdigest() == HCP_MD5[h]
        out["hcp"][h] = np.array([n[2:-4] if n.endswith("_ROI") else "" for n in parse_annot(b)])
    return out


def load_mapper(subject):
    """The data set's voxel-to-fsaverage mappers, {"lh"|"rh": CSR [vertices x voxels]}."""
    from scipy import sparse
    d = read_hdf(f"Mappers/{subject}.hdf")
    side = {"lh": "left", "rh": "right"}
    return {h: sparse.csr_matrix((d[f"vox_to_fsavg_{s}_data"], d[f"vox_to_fsavg_{s}_indices"],
                                  d[f"vox_to_fsavg_{s}_indptr"]), shape=tuple(d[f"vox_to_fsavg_{s}_shape"]))
            for h, s in side.items()}


def region_matrix(mapper, atlases, regions, voxel_mask=None):
    """[voxel x region] matrix whose product with a voxel map gives the region's mean on fsaverage.

    A region's mean is taken over its vertices (both hemispheres) that the mapper reaches,
    each vertex the mapper's weighted mean of its voxels. voxel_mask keeps only some voxels
    (a vertex counts when it reaches a kept voxel). Returns the matrix and the vertices used.
    """
    from scipy import sparse
    cols, nvert = [], []
    for atlas, areas in regions.values():
        col, n = 0, 0
        for h, Mh in mapper.items():
            if voxel_mask is not None:
                Mh = Mh @ sparse.diags(voxel_mask.astype(float))
            rows = np.isin(atlases[atlas][h], areas) & (np.diff(Mh.indptr) > 0)
            col = col + np.asarray(Mh[rows].sum(0)).ravel()
            n += int(rows.sum())
        cols.append(col / max(n, 1))
        nvert.append(n)
    return np.column_stack(cols), nvert


def region_weights(Z, X, S, sign_X=None):
    """Mean weight per region of each state dimension, under the three readings of the claims file.

    Z [TR x 24] PCA scores of the TRs fitted, X [TR x d] variables, S [TR x region] the
    responses averaged per region (Y R_mat). The components are C = diag(1/sqrt(w)) U^T Yc,
    with Z = U sqrt(w), so for a vector z in PC space the voxel map C^T z has region means
    Sc^T (Z / w) z. Readings: "B" the OLS weights (the code's coeffs, from S itself), "B_L"
    the denoised weights, "Q_S" the state directions. Each dimension is oriented so that its
    own state's TRs (X[:, j] > 0) have a positive mean position: along Q_S for Q_S, along the
    denoised weights for B and B_L. Returns {reading: [region x d]}.
    """
    d = X.shape[1]
    P = np.column_stack([X, np.ones(len(X))])
    pinv = np.linalg.pinv(P.T @ P)
    B = (pinv @ (P.T @ S))[:d].T  # region x d
    coef = (pinv @ (P.T @ Z))[:d]  # d x 24
    w = (Z ** 2).sum(0)
    Sc = S - S.mean(0)
    to_reg = Sc.T @ (Z / w)  # region x 24
    Q, _ = state_directions(Z, X)
    out = {"B": B, "B_L": to_reg @ coef.T, "Q_S": to_reg @ Q}
    sx = X if sign_X is None else sign_X
    for key, dirs in [("B_L", coef.T), ("Q_S", Q)]:
        p = Z @ dirs
        sg = np.array([np.sign(p[sx[:, j] > 0, j].mean() - p[:, j].mean()) if sx[:, j].any() else 1.0
                       for j in range(d)])
        if key == "B_L":
            out["B"] = out["B"] * sg
        out[key] = out[key] * sg
    return out


def fir(F, delays=(1, 2, 3, 4)):
    """Features delayed by 1 to 4 TRs, concatenated (Methods, "Deconvolution of the
    Hemodynamic Response in the Attention Task")."""
    out = []
    for k in delays:
        D = np.zeros_like(F)
        D[k:] = F[:-k]
        out.append(D)
    return np.hstack(out)


def semantic_model_r(subject, sem, voxels, alphas=(1e1, 1e2, 1e3, 1e4, 1e5), k=10):
    """Cross-validated prediction of the raw attention BOLD by the WordNet FIR model.

    Reading (ii) of att-weights-cortex, for the voxels given (those the regions reach). The
    paper's deconvolution model (Methods, "Deconvolution of the Hemodynamic Response in the
    Attention Task"): WordNet labels (semantics.hdf: "attentive" for the human and vehicle
    runs, "passive" for the passive runs), delayed 1 to 4 TRs within each condition, ridge
    regression with 10-fold cross-validation. Folds are contiguous tenths of each condition.
    One ridge parameter per subject, the one with the highest mean prediction correlation
    over these voxels (the paper does not say how it was chosen; an assumption). Returns the
    per-voxel correlation of the held-out predictions (all folds pooled) with the responses,
    the ridge parameter, the number of TRs and the mean correlation per ridge parameter.
    """
    with _open(f"VisualAttention/Data/{subject}.hdf") as f, h5py.File(f, "r") as h:
        Y = np.vstack([h[c][()][:, voxels].astype(np.float32) for c in CONDITIONS])
        sizes = [h[c].shape[0] for c in CONDITIONS]
    feats = {"passive": sem["passive"], "human": sem["attentive"], "vehicle": sem["attentive"]}
    X = np.vstack([fir(feats[c]) for c in CONDITIONS]).astype(np.float32)
    fold_of = np.concatenate([np.repeat(np.arange(k), [len(a) for a in np.array_split(np.arange(n), k)])
                              for n in sizes])
    pred = np.zeros((len(alphas),) + Y.shape, np.float32)
    for j in range(k):
        te, tr = fold_of == j, fold_of != j
        Xtr = X[tr].astype(np.float64)
        s2, V = np.linalg.eigh(Xtr.T @ Xtr)  # ridge in the eigenbasis of X^T X
        VtXtY = (V.T @ (Xtr.T @ Y[tr])).astype(np.float32)
        Xte_V = (X[te] @ V).astype(np.float32)
        for a, alpha in enumerate(alphas):
            pred[a, te] = (Xte_V / (np.clip(s2, 0, None) + alpha).astype(np.float32)) @ VtXtY
    Yc = Y - Y.mean(0)
    r = np.array([((P - P.mean(0)) * Yc).sum(0) /
                  np.sqrt(((P - P.mean(0)) ** 2).sum(0) * (Yc ** 2).sum(0) + 1e-30) for P in pred])
    best = int(np.argmax(r.mean(1)))
    return r[best], alphas[best], len(Y), r.mean(1)


def cv_ols_r(Y, X, k=10):
    """Per-voxel correlation of cross-validated OLS predictions (with intercept) with the
    responses, 10 contiguous folds pooled: reading (ii) of game-weights-two-groups, the
    nine-state model as the encoding model (claims file)."""
    P = np.column_stack([X, np.ones(len(X))])
    pred = np.zeros(Y.shape, np.float64)
    for te in np.array_split(np.arange(len(Y)), k):
        tr = np.setdiff1d(np.arange(len(Y)), te)
        W = np.linalg.pinv(P[tr].T @ P[tr]) @ (P[tr].T @ Y[tr])
        pred[te] = P[te] @ W
    Pc, Yc = pred - pred.mean(0), Y - Y.mean(0)
    return (Pc * Yc).sum(0) / np.sqrt((Pc ** 2).sum(0) * (Yc ** 2).sum(0) + 1e-30)


def r_pvalue(r, n):
    """One-sided p of a correlation above zero, from the t distribution with n - 2 df."""
    from scipy import stats
    r = np.clip(r, -0.999999, 0.999999)
    return stats.t.sf(r * np.sqrt((n - 2) / (1 - r ** 2)), n - 2)
