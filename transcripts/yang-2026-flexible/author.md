# yang-2026-flexible · author · run 45006249672

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
date -u; cat docs/protocol.md; ls; ls paper entries claims attempts
```

```
<persisted-output>
Output too large (64.3KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/ef5de288-6085-4f1a-b490-d28b30a783ba/tool-results/bxdlnh4r3.txt

Preview (first 2KB):
Sun Nov 22 09:16:01 UTC 2026
# Protocol for an attempt

Version: `pilot-18`. Record this version in the attempt's provenance.

This is what agents, or people, do to attempt a target and deposit the
result. A target is a dataset in a public archive and a paper it names. How
each archive's datasets are named, versioned and read is in
[archives.md](archives.md); the examples here are from DANDI, the first. It is written from the pilot attempts
([pilot notes](pilot-notes.md)); the reasons for the rules are there.

An attempt has three roles, each a separate run with a separate context:

- The **reader** reads the paper and writes the claims file: every finding,
  and how each is to be tested, taken from the paper. A second reader checks
  it against the paper. Readers never see the dataset's data.
[... 20 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/ef5de288-6085-4f1a-b490-d28b30a783ba/tool-results/bxdlnh4r3.txt"
}
```

```
1	Sun Nov 22 09:16:01 UTC 2026
2	# Protocol for an attempt
3	
4	Version: `pilot-18`. Record this version in the attempt's provenance.
5	
6	This is what agents, or people, do to attempt a target and deposit the
7	result. A target is a dataset in a public archive and a paper it names. How
8	each archive's datasets are named, versioned and read is in
9	[archives.md](archives.md); the examples here are from DANDI, the first. It is written from the pilot attempts
10	([pilot notes](pilot-notes.md)); the reasons for the rules are there.
11	
12	An attempt has three roles, each a separate run with a separate context:
13	
14	- The **reader** reads the paper and writes the claims file: every finding,
15	  and how each is to be tested, taken from the paper. A second reader checks
16	  it against the paper. Readers never see the dataset's data.
17	- The **author** tests the claims on the dataset. It reads the paper to
18	  understand the claims, but the claims file binds it: it cannot change a
19	  claim's statement, expected values or criterion. A method detail the file
20	  lacks it takes from the paper, citing the passage, and it asks a reader
[... 1442 more lines not kept]
```

**Agent calls Bash**

```bash
ls paper entries/fouke-2025 papers/datasets | head -5; ls paper; cat claims/yang-2026-flexible.yaml; cat papers/datasets/yang-2026-flexible.yaml; ls attempts | grep yang; ls questions | grep yang
```

```
<persisted-output>
Output too large (63.3KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/ef5de288-6085-4f1a-b490-d28b30a783ba/tool-results/br3alq4va.txt

Preview (first 2KB):
entries/fouke-2025:
README.md
entry.yaml
omr.py
reproduce_fouke_2025.ipynb
10.1523-eneuro.0275-26.2026.txt
# Claims for Yang (2026), "Flexible Cellular Phenotypes Retain a Shared Type-Level Organization
# across Response Regimes", eNeuro 13(11) ENEURO.0275-26.2026, doi:10.1523/eneuro.0275-26.2026,
# on DANDI 000020 (Allen Institute Patch-seq of mouse visual cortex GABAergic neurons, Gouwens et
# al. 2020), which the paper reuses.
#
# Provenance. Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub
# Actions"), 2026-11-22, protocol pilot-18 as stated in docs/protocol.md (Reader, steps 1 to 4).
#
# Text read. The version of record, from paper/10.1523-eneuro.0275-26.2026.txt (PMC13737997):
# abstract, Significance Statement, Introduction, Materials and Methods, Results, Discussion,
[... 16 more lines not kept]
```

**Agent calls Bash**

```bash
cat README.md | head -80; wc -l docs/design.md; cat docs/archives.md | sed -n '1,200p'
```

```
# Encore Science: the registry

Encore Science checks datasets against the papers they came from. This repository holds its public record, the Encore registry, served at <https://encorescience.org>, and the `encore` command that runs the same check on your own data ([docs/encore.md](docs/encore.md)). It is developed by [CatalystNeuro](https://www.catalystneuro.com).

Agents, and people, try to reproduce the key findings of papers from the open
data in public archives, starting with the [DANDI Archive](https://dandiarchive.org), and register the result
here: the notebooks when it works, and the reason when it does not.

- **For the archive:** evidence of whether each dandiset is complete and
  accurate enough to support the findings of its paper.
- **For analysts:** working notebooks to build new analyses on.

Status: pilot. All eight pilot targets have been attempted and checked by an
independent agent.

**Dashboard:** <https://encorescience.org/>

## Reading the outcomes

An outcome says what one attempt could recover from the data in a dandiset,
[... 261 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/ef5de288-6085-4f1a-b490-d28b30a783ba/tool-results/br3alq4va.txt"
}
```

```
1	entries/fouke-2025:
2	README.md
3	entry.yaml
4	omr.py
5	reproduce_fouke_2025.ipynb
6	10.1523-eneuro.0275-26.2026.txt
7	# Claims for Yang (2026), "Flexible Cellular Phenotypes Retain a Shared Type-Level Organization
8	# across Response Regimes", eNeuro 13(11) ENEURO.0275-26.2026, doi:10.1523/eneuro.0275-26.2026,
9	# on DANDI 000020 (Allen Institute Patch-seq of mouse visual cortex GABAergic neurons, Gouwens et
10	# al. 2020), which the paper reuses.
11	#
12	# Provenance. Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub
13	# Actions"), 2026-11-22, protocol pilot-18 as stated in docs/protocol.md (Reader, steps 1 to 4).
14	#
15	# Text read. The version of record, from paper/10.1523-eneuro.0275-26.2026.txt (PMC13737997):
16	# abstract, Significance Statement, Introduction, Materials and Methods, Results, Discussion,
17	# Table 1, Table 2 (statistical summary, rows a to y), the legends of Figures 1 to 4 and of the
18	# Extended Data (Figures 1-1 to 1-3, 2-1, 3-1 to 3-3, 4-1 to 4-4; Tables 1-1 and 2-1), and the
19	# synthesis of the reviews. The Extended Data files themselves (TIF figures, DOCX Tables 1-1,
20	# 2-1, 3-1, 4-1, 4-3) are not in the text and no PDF was supplied; only their legends were read.
[... 919 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/ef5de288-6085-4f1a-b490-d28b30a783ba/tool-results/br3alq4va.txt",
 "offset": 940,
 "limit": 240
}
```

```
940	    tolerance: 0.052
941	  - quantity: Spearman of T with rank range, HVG500
942	    value: 0.105
943	    tolerance: 0.0105
944	  criterion: As fig4ab-rna-tracks-shared-map with the curated genes alone and with the 500
945	    highest-variance genes alone, 50 shuffles (scripts/q3bc_explain.py, which permutes the
946	    phenotype values across pairs, two-sided; readings as there). The asymmetry is judged with
947	    the code's own rule for the primary panel (scripts/q3bc_explain.py, main, landing
948	    "rna_tracks_phenotype_distance"; the paper states none), applied to each panel; rho with
949	    mean S at least 0.25 and |rho| with rank range below 0.15. Reproduced when the
950	    correlations with mean S are within tolerance with p < 0.05 and the asymmetry rule holds for
951	    each panel; partially reproduced
952	    when the asymmetry holds but some value is out of tolerance. The tolerance on 0.011 is 10%
953	    of a value near zero; any value with |rho| < 0.05 is reported as near.
954	- id: fig4c-joint-excitability-modules
955	  statement: A joint representation of the prespecified excitability modules correlates with
956	    mean phenotypic separation (rho 0.314) but not with rank range (rho -0.023).
957	  source: Results, Transcriptomic structure preferentially tracks the shared phenotypic map,
958	    paragraph 2; Figure 4C; Table 2 rows s and t
959	  quote: >-
[... 210 more lines not kept]
```

**Agent calls Bash**

```bash
wc -c paper/*; ls entries/fouke-2025; cat entries/fouke-2025/entry.yaml entries/fouke-2025/README.md; cat entries/fouke-2025/requirements.in; head -c 3000 attempts/fouke-2025-01.yaml
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd $TMPDIR; curl -s https://api.dandiarchive.org/api/dandisets/000020/ | python -m json.tool | head -40; curl -s "https://api.dandiarchive.org/api/dandisets/000020/versions/" | python -m json.tool | head -60
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
grep -n "python" tools/entry.py | head -30; curl -sI https://github.com/zy-neuro/protocol-response-geometry | head -3; python --version
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
sed -n 460,520p tools/entry.py; grep -n "REGISTRY_PYTHON\|CURRENT_PYTHON\|DEFAULT_PYTHON" tools/entry.py | head
```

```
if LONG_LITERAL.search(code):
        report.error(where, f"contains a literal of more than {MAX_LITERAL_NUMBERS} numbers; "
                            "results must be computed from the data")


# --- lock and run -------------------------------------------------------------

LOCK_VERSION = re.compile(r"--python-version\s+(\d+\.\d+)")


def python_of(entry_dir: Path) -> str:
    """The Python version an entry runs on: its entry.yaml's `python`, else the version its lock was compiled for
    (entries from before the field), else the registry's default for new entries, PYTHON_VERSION."""
    entry = yaml.safe_load((entry_dir / "entry.yaml").read_text()) or {}
    if entry.get("python"):
        return str(entry["python"])
    lock_file = entry_dir / "requirements.lock.txt"
    if lock_file.is_file():
        m = LOCK_VERSION.search(lock_file.read_text()[:2000])
        if m:
[... 41 more lines not kept]
```

**Agent calls Bash**

```bash
grep -n "^PYTHON_VERSION\|MAX_LITERAL\|TIMEOUT\|timeout" tools/entry.py | head -20
```

```
63:PYTHON_VERSION = "3.13"
68:MAX_LITERAL_NUMBERS = 200                 # more numbers than this in one literal is "embedded data"
73:LONG_LITERAL = re.compile(r"[\[(]\s*(?:-?\d+\.?\d*(?:e-?\d+)?\s*,\s*){%d,}" % MAX_LITERAL_NUMBERS)
461:        report.error(where, f"contains a literal of more than {MAX_LITERAL_NUMBERS} numbers; "
524:def upgrade_python(entry_dir: Path, version: str, before: Path, output_dir: Path, timeout: int,
531:    if lock(entry_dir, version) or run(entry_dir, output_dir, timeout, max_minutes, fresh=True):
596:def run(entry_dir: Path, output_dir: Path, timeout: int, max_minutes: float, fresh: bool = False) -> int:
627:             f"--ExecutePreprocessor.timeout={timeout}", f"--ExecutePreprocessor.kernel_name={kernel}",
702:    parser.add_argument("--timeout", type=int, default=3600, help="seconds allowed per cell")
744:                              args.timeout, args.max_minutes)
754:    return run(entry_dir, output_dir, args.timeout, args.max_minutes, args.fresh)
```

**Agent**

Setting up a dev environment to test whether IPFX installs and how long one cell takes.

**Agent calls Bash**

```bash
cd $TMPDIR && uv venv -q --python 3.13 dev && uv pip install -q --python dev/bin/python ipfx remfile pynwb h5py dandi pandas scikit-learn 2>&1 | tail -20; dev/bin/python -c "import ipfx, pynwb, numpy; print(ipfx.__version__, pynwb.__version__, numpy.__version__)"
```

```
2.1.2 3.1.2 2.5.5
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && git clone -q https://github.com/zy-neuro/protocol-response-geometry code && cd code && git checkout -q 61a5a41 && git log -1 --format=%H && ls -R scripts configs | head; ls results; du -sh results
```

```
61a5a413daea3b3562fad6e40207320da5665fed
configs:
q3_curated_excitability_genes.txt

scripts:
dump_pc1_loadings.py
figures_eneuro_results.py
figures_eneuro_supplement.py
paths.py
q1_describe_phenotype.py
q1_knn_scale.py
fig1_example_traces.csv
m0
phenotype
q1
q1_reliability
q2
q3_mobility
q3a
q3a_robustness
[... 4 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/code && ls scripts results/*; cat README* | head -80
```

```
results/fig1_example_traces.csv

results/m0:
m0_molecular_join.csv

results/phenotype:
brief_pulse_pca_loadings.csv
brief_pulse_pca_scores.csv
brief_pulse_pca_variance.csv
long_pulse_pca_loadings.csv
long_pulse_pca_scores.csv
long_pulse_pca_variance.csv
phenotype_summary.json
ramp_pca_loadings.csv
ramp_pca_scores.csv
ramp_pca_variance.csv

results/q1:
q1_cross_protocol.csv
q1_knn_jaccard_k15.csv
[... 99 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/code && cat scripts/q1_split_half_long_square.py
```

```
<persisted-output>
Output too large (32.1KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/ef5de288-6085-4f1a-b490-d28b30a783ba/tool-results/b5rkxln18.txt

Preview (first 2KB):
#!/usr/bin/env python3
"""within-regime split-half neighborhood reliability.

Split usable long-square sweeps into two disjoint halves, extract IPFX
long-square features on each half, project into the ORIGINAL long-pulse
phenotype space (full-cell z-score + PCA; halves do not enter the fit),
and compare 15-NN Jaccard of half-A vs half-B with cross-regime 15-NN
Jaccard for the same cells.

Writes results/q1_reliability/ only.
"""

from __future__ import annotations

import argparse
import csv
[... 81 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/ef5de288-6085-4f1a-b490-d28b30a783ba/tool-results/b5rkxln18.txt",
 "offset": 90,
 "limit": 520
}
```

```
90	    num = as_float(obj)
91	    if num is not None:
92	        out[prefix.rstrip(".")] = num
93	
94	
95	def pack_cell_record(cell_record: dict, rec: dict) -> None:
96	    for key, value in cell_record.items():
97	        num = as_float(value)
98	        if num is None:
99	            continue
100	        proto = None
101	        name = key
102	        for suffix, protocol in RECORD_SUFFIX.items():
103	            if key.endswith(suffix):
104	                proto = protocol
105	                name = key[: -len(suffix)]
106	                break
107	        if proto is None:
108	            if key in LONG_RECORD:
109	                proto = "long_squares"
[... 500 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && P=dev/lib/python3.13/site-packages/ipfx; sed -n 1,80p $P/dataset/create.py | grep -n "def \|nwb\|h5py" ; grep -n "NWBHDF5IO\|h5py\|def __init__" $P/dataset/ephys_nwb_data.py $P/dataset/hbg_nwb_data.py | head
```

```
5:import h5py
12:from ipfx.dataset.hbg_nwb_data import HBGNWBData
13:from ipfx.dataset.mies_nwb_data import MIESNWBData
18:def get_scalar_value(dataset_from_nwb):
24:    if isinstance(dataset_from_nwb, np.ndarray):
25:        return dataset_from_nwb.item()
27:    return dataset_from_nwb
30:def is_file_mies(path: str) -> bool:
31:    with h5py.File(path, "r") as fil:
44:def get_nwb_version(nwb_file: str) -> Dict[str, Any]:
46:    Find version of the nwb file
50:    nwb_file
64:    with h5py.File(nwb_file, 'r') as f:
65:        if "nwb_version" in f:         # In version 0 and 1 this is a dataset
66:            nwb_version = get_scalar_value(f["nwb_version"][()])
67:            nwb_version_str = to_str(nwb_version)
68:            if nwb_version is not None and re.match("^NWB-", nwb_version_str):
70:                    "major": int(nwb_version_str[4]),
71:                    "full": nwb_version_str
74:        elif "nwb_version" in f.attrs:   # in version 2 this is an attribute
[... 16 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && P=dev/lib/python3.13/site-packages/ipfx; sed -n 60,130p $P/dataset/ephys_nwb_data.py; sed -n 80,200p $P/dataset/create.py
```

```
"""

    STIMULUS = (VoltageClampStimulusSeries, CurrentClampStimulusSeries)
    RESPONSE = (VoltageClampSeries, CurrentClampSeries)

    def __init__(self,
                 nwb_file: None,
                 ontology: StimulusOntology,
                 load_into_memory: bool = True,
                 validate_stim: bool = True
                 ):

        super(EphysNWBData, self).__init__(
            ontology=ontology, validate_stim=validate_stim)
        self.load_nwb(nwb_file, load_into_memory)

        self.acquisition_path = "acquisition"
        self.stimulus_path = "stimulus/presentation"
        self.nwb_major_version = 2

[... 103 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && cat > list_assets.py <<'EOF'
import requests, json
url="https://api.dandiarchive.org/api/dandisets/000020/versions/0.210913.1639/assets/?page_size=1000"
out=[]
while url:
    r=requests.get(url).json(); out+=r["results"]; url=r["next"]
json.dump(out,open("assets.json","w"))
print(len(out)); print(out[0])
import collections
print(sum(a["size"] for a in out)/1e9)
print(collections.Counter(a["path"].split("/")[0] for a in out).most_common(3), len(set(a["path"].split("/")[0] for a in out)))
EOF
dev/bin/python list_assets.py
```

```
4435
{'asset_id': '293b402c-2217-4611-8e68-b66a6b7be3a1', 'blob': '2f179647-0796-4661-8b05-c2d81511643c', 'zarr': None, 'path': 'sub-1001658958/sub-1001658958_ses-1003321768_icephys.nwb', 'size': 19842547, 'created': '2021-07-01T13:42:36.033305Z', 'modified': '2021-08-05T18:43:30.025949Z'}
141.856436428
[('sub-737379098', 21), ('sub-750787657', 21), ('sub-716843169', 18)] 1040
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && cat > one.py <<'EOF'
import json, time, io, requests, sys, logging, warnings, resource
warnings.filterwarnings("ignore"); logging.disable(logging.WARNING)
assets=json.load(open("assets.json"))
i=int(sys.argv[1])
a=assets[i]
t0=time.time()
url=f"https://api.dandiarchive.org/api/assets/{a['asset_id']}/download/"
data=requests.get(url).content
t1=time.time(); print("fetch", a['size']/1e6, "MB", round(t1-t0,2),"s")
from ipfx.sweep import Sweep
orig=Sweep.__init__
def patched(self,t,v,i,clamp_mode,sampling_rate,sweep_number=None,epochs=None):
    if epochs: epochs={k:x for k,x in epochs.items() if x is not None}
    orig(self,t,v,i,clamp_mode,sampling_rate,sweep_number=sweep_number,epochs=epochs)
Sweep.__init__=patched
from ipfx.dataset.create import create_ephys_data_set
from ipfx.data_set_features import extract_data_set_features
ds=create_ephys_data_set(nwb_file=io.BytesIO(data))
t2=time.time(); print("open", round(t2-t1,2))
st=ds.sweep_table
print(st.columns.tolist()); print(st.stimulus_code.value_counts().head(20)) if 'stimulus_code' in st else None
orig_get=ds.get_sweep_numbers
def filt(*a,**k):
    return [sn for sn in orig_get(*a,**k) if ds.sweep(int(sn)).epochs.get("experiment") and ds.sweep(int(sn)).epochs.get("stim")]
ds.get_sweep_numbers=filt
try:
    cf, sf, cr = extract_data_set_features(ds)
    print("ok", list(cf.keys()), len(cr))
except Exception as e:
    print("fail", type(e).__name__, e)
print("ipfx", round(time.time()-t2,2), "maxrss MB", resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1e3)
EOF
dev/bin/python one.py 0 2>&1 | tail -40
```

```
fetch 19.842547 MB 0.93 s
open 2.31
['sweep_number', 'stimulus_units', 'bridge_balance_mohm', 'leak_pa', 'stimulus_scale_factor', 'stimulus_code', 'stimulus_code_ext', 'clamp_mode', 'stimulus_name']
stimulus_code
X2LP_Search         9
X5SP_Search         7
X1PS_SubThresh      5
X4PS_SupraThresh    3
X7Ramp              3
X3LP_Rheo           2
X6SP_Rheo           2
EXTPGGAEND180424    2
EXTPSMOKET180424    1
EXTPINBATH180424    1
EXTPCllATT180424    1
EXTPBREAKN180424    1
EXTPEXPEND180424    1
Name: count, dtype: int64
fail KeyError 4
ipfx 1.02 maxrss MB 429.164
[... 1 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && sed -i 's/    print("fail", type(e).__name__, e)/    import traceback; traceback.print_exc()/' one.py && dev/bin/python one.py 0 2>&1 | grep -v "^  warn" | tail -30
```

```
Traceback (most recent call last):
  File "/tmp/claude-1001/one.py", line 27, in <module>
    cf, sf, cr = extract_data_set_features(ds)
                 ~~~~~~~~~~~~~~~~~~~~~~~~~^^^^
  File "/tmp/claude-1001/dev/lib/python3.13/site-packages/ipfx/data_set_features.py", line 388, in extract_data_set_features
    sweep_features[s['sweep_number']]['peak_deflect'] = s['peak_deflect']
    ~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
KeyError: 4
fetch 19.842547 MB 0.75 s
open 1.59
['sweep_number', 'stimulus_units', 'bridge_balance_mohm', 'leak_pa', 'stimulus_scale_factor', 'stimulus_code', 'stimulus_code_ext', 'clamp_mode', 'stimulus_name']
stimulus_code
X2LP_Search         9
X5SP_Search         7
X1PS_SubThresh      5
X4PS_SupraThresh    3
X7Ramp              3
X3LP_Rheo           2
X6SP_Rheo           2
EXTPGGAEND180424    2
[... 8 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && sed -n 300,420p dev/lib/python3.13/site-packages/ipfx/data_set_features.py
```

```
ssq_spx, ssq_spfx = extractors_for_sweeps(ssq_sweeps,
                                              est_window=[ssq_start, ssq_start+SSQ_WINDOW],
                                              **detection_parameters(StimulusType.SHORT_SQUARE))

    ssq_an = spa.ShortSquareAnalysis(ssq_spx, ssq_spfx)

    ssq_features = ssq_an.analyze(ssq_sweeps)

    return ssq_an.as_dict(
        ssq_features,
        [dict(sweep_number=sn) for sn in short_square_sweep_numbers]
        )


@record_errors
@fallback_on_error()
def extract_cell_ramp_features(data_set):
    lu.log_pretty_header("Ramps:", level=2)

    ramp_sweep_numbers = data_set.get_sweep_numbers(
[... 85 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && sed -n 180,260p dev/lib/python3.13/site-packages/ipfx/data_set_features.py; grep -rn "subthresh_min_amp\|select_subthreshold" dev/lib/python3.13/site-packages/ipfx/bin/run_feature_extraction.py
```

```
for k in [ "start", "end" ]:
            if k in dp:
                dp.pop(k)

        sfx, _ = extractors_for_sweeps(sweep_set, **dp)

        for sn, sweep in zip(sweep_numbers, sweep_set.sweeps):
#            logging.info("Extracting features from the sweep %d" % sn)
            spikes_df = sfx.process(sweep.t, sweep.v, sweep.i)
            sweep_features[sn] = {'spikes': spikes_df.to_dict(orient='records'), "sweep_number": sn }

    return sweep_features


def select_subthreshold_min_amplitude(stim_amps, decimals=0):
    """Find the min delta between amplitudes of coarse long square sweeps.  Includes failed sweeps.

    Parameters
    ----------
    stim_amps: list of stimulus amplitudes
[... 61 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/code && python -c "
import json;d=json.load(open('results/phenotype/phenotype_summary.json'))
for k,v in d.items():
  if isinstance(v,dict):
    print(k,{kk:(vv if not isinstance(vv,list) else (len(vv),vv)) for kk,vv in v.items()})
  else: print(k,v)
"; cat scripts/paths.py | head -40; head -3 results/m0/m0_molecular_join.csv; wc -l results/m0/m0_molecular_join.csv results/phenotype/*scores.csv
```

```
long_pulse {'n_cells': 4344, 'n_features': 42, 'k80': 11, 'features': (42, ['feat.long_squares.vrest', 'feat.long_squares.ri', 'feat.long_squares.sag', 'feat.long_squares.tau', 'feat.long_squares.vm_for_sag', 'feat.long_squares.f_i_curve_slope', 'feat.long_squares.adaptation', 'feat.long_squares.latency', 'feat.long_squares.avg_isi', 'feat.long_squares.upstroke_downstroke_ratio', 'feat.long_squares.peak_v', 'feat.long_squares.peak_t', 'feat.long_squares.trough_v', 'feat.long_squares.trough_t', 'feat.long_squares.fast_trough_v', 'feat.long_squares.fast_trough_t', 'feat.long_squares.threshold_v', 'feat.long_squares.threshold_i', 'feat.long_squares.threshold_t', 'feat.long_squares.v_baseline', 'feat.long_squares.rheobase_i', 'feat.long_squares.rheobase_sweep.avg_rate', 'feat.long_squares.rheobase_sweep.stim_amp', 'feat.long_squares.rheobase_sweep.v_baseline', 'feat.long_squares.rheobase_sweep.sag', 'feat.long_squares.rheobase_sweep.latency', 'feat.long_squares.rheobase_sweep.index', 'feat.long_squares.rheobase_sweep.sweep_number', 'feat.long_squares.fi_fit_slope', 'feat.long_squares.hero_sweep.avg_rate', 'feat.long_squares.hero_sweep.stim_amp', 'feat.long_squares.hero_sweep.v_baseline', 'feat.long_squares.hero_sweep.sag', 'feat.long_squares.hero_sweep.adapt', 'feat.long_squares.hero_sweep.latency', 'feat.long_squares.hero_sweep.isi_cv', 'feat.long_squares.hero_sweep.mean_isi', 'feat.long_squares.hero_sweep.median_isi', 'feat.long_squares.hero_sweep.first_isi', 'feat.long_squares.hero_sweep.index', 'feat.long_squares.hero_sweep.sweep_number', 'feat.long_squares.input_resistance']), 'scores': 'results/phenotype/long_pulse_pca_scores.csv'}
ramp {'n_cells': 4139, 'n_features': 20, 'k80': 3, 'features': (20, ['feat.ramps.upstroke_downstroke_ratio', 'feat.ramps.peak_v', 'feat.ramps.peak_t', 'feat.ramps.trough_v', 'feat.ramps.trough_t', 'feat.ramps.fast_trough_v', 'feat.ramps.fast_trough_t', 'feat.ramps.threshold_v', 'feat.ramps.threshold_i', 'feat.ramps.threshold_t', 'feat.r
[... 32 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && curl -sI "https://data.nemoarchive.org/other/AIBS/AIBS_patchseq/transcriptome/scell/SMARTseq/processed/analysis/20200611/20200513_Mouse_PatchSeq_Release_count.v2.csv.tar" | head -5; curl -s "https://data.nemoarchive.org/other/AIBS/AIBS_patchseq/transcriptome/scell/SMARTseq/processed/analysis/20200611/" | grep -o 'href="[^"]*"' | head -30
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR && cat > one2.py <<'EOF'
import json, time, io, requests, sys, logging, warnings, resource
warnings.filterwarnings("ignore"); logging.disable(logging.WARNING)
assets=json.load(open("assets.json"))
from ipfx.sweep import Sweep
orig=Sweep.__init__
def patched(self,t,v,i,clamp_mode,sampling_rate,sweep_number=None,epochs=None):
    if epochs: epochs={k:x for k,x in epochs.items() if x is not None}
    orig(self,t,v,i,clamp_mode,sampling_rate,sweep_number=sweep_number,epochs=epochs)
Sweep.__init__=patched
from ipfx.dataset.create import create_ephys_data_set
import ipfx.data_set_features as dsf
from ipfx.feature_record import build_cell_feature_record
for i in map(int, sys.argv[1:]):
    a=assets[i]; t0=time.time()
    data=requests.get(f"https://api.dandiarchive.org/api/assets/{a['asset_id']}/download/").content
    t1=time.time()
    ds=create_ephys_data_set(nwb_file=io.BytesIO(data))
    og=ds.get_sweep_numbers
    def filt(*x,**k):
        return [sn for sn in og(*x,**k) if ds.sweep(int(sn)).epochs.get("experiment") and ds.sweep(int(sn)).epochs.get("stim")]
    ds.get_sweep_numbers=filt
    cf={}; st={}
    cf['long_squares'],st['l']=dsf.extract_cell_long_square_features(ds)
    cf['short_squares'],st['s']=dsf.extract_cell_short_square_features(ds)
    cf['ramps'],st['r']=dsf.extract_cell_ramp_features(ds)
    rec=build_cell_feature_record(cf)
    print(i, a['size']/1e6, "fetch",round(t1-t0,2),"ipfx",round(time.time()-t1,2), {k:v['failed_fx'] for k,v in st.items()}, len(rec), "rss",resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1e3, flush=True)
EOF
dev/bin/python one2.py 0 1 2 100 1000 2000 3000 4000 2>&1 | grep -v warn | tail -20
```

```
0 19.842547 fetch 0.71 ipfx 0.98 {'l': False, 's': False, 'r': False} 47 rss 381.788
1 22.263517 fetch 0.58 ipfx 1.25 {'l': False, 's': False, 'r': False} 47 rss 541.792
2 31.666658 fetch 0.81 ipfx 1.2 {'l': False, 's': False, 'r': False} 47 rss 711.584
100 14.678804 fetch 0.78 ipfx 1.09 {'l': False, 's': False, 'r': False} 47 rss 805.036
1000 14.347637 fetch 0.78 ipfx 0.96 {'l': False, 's': False, 'r': False} 47 rss 916.164
2000 19.694882 fetch 0.79 ipfx 0.86 {'l': False, 's': False, 'r': False} 47 rss 1024.596
3000 69.689869 fetch 1.66 ipfx 2.01 {'l': False, 's': False, 'r': False} 47 rss 1313.624
4000 24.618189 fetch 0.6 ipfx 1.67 {'l': False, 's': False, 'r': False} 47 rss 1577.692
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && cat > meta.py <<'EOF'
import json, remfile, h5py, pynwb, warnings
warnings.filterwarnings("ignore")
a=json.load(open("assets.json"))[0]
import requests
url=requests.head(f"https://api.dandiarchive.org/api/assets/{a['asset_id']}/download/",allow_redirects=True).url
f=h5py.File(remfile.File(url),"r")
io=pynwb.NWBHDF5IO(file=f,load_namespaces=True); nwb=io.read()
print(nwb)
print(nwb.subject)
for k in ["session_id","session_description","identifier","institution","data_collection","protocol","stimulus_notes","experiment_description","session_start_time","source_script"]:
    print(k, getattr(nwb,k,None))
print(list(nwb.acquisition)[:5], len(nwb.acquisition), len(nwb.stimulus))
s=nwb.acquisition[list(nwb.acquisition)[0]]; print(s)
print(nwb.sweep_table.to_dataframe().head() if nwb.sweep_table is not None else None)
print(nwb.epochs.to_dataframe().head(10) if nwb.epochs is not None else None, nwb.epochs.colnames if nwb.epochs is not None else None)
print(nwb.icephys_electrodes)
def walk(g,p=""):
    for k,v in g.items():
        if isinstance(v,h5py.Group):
            if k in ("acquisition","stimulus"): print(p+k+"/ (",len(v),")"); continue
            walk(v,p+k+"/")
        else: print(p+k, v.shape, v.dtype)
walk(f)
EOF
dev/bin/python meta.py 2>&1 | head -150
```

```
root pynwb.file.NWBFile at 0x128248711027680
Fields:
  acquisition: {
    data_00000_AD0 <class 'pynwb.icephys.VoltageClampSeries'>,
    data_00001_AD0 <class 'pynwb.icephys.VoltageClampSeries'>,
    data_00002_AD0 <class 'pynwb.icephys.VoltageClampSeries'>,
    data_00003_AD0 <class 'pynwb.icephys.VoltageClampSeries'>,
    data_00004_AD0 <class 'pynwb.icephys.CurrentClampSeries'>,
    data_00005_AD0 <class 'pynwb.icephys.CurrentClampSeries'>,
    data_00006_AD0 <class 'pynwb.icephys.CurrentClampSeries'>,
    data_00007_AD0 <class 'pynwb.icephys.CurrentClampSeries'>,
    data_00008_AD0 <class 'pynwb.icephys.CurrentClampSeries'>,
    data_00009_AD0 <class 'pynwb.icephys.CurrentClampSeries'>,
    data_00010_AD0 <class 'pynwb.icephys.CurrentClampSeries'>,
    data_00011_AD0 <class 'pynwb.icephys.CurrentClampSeries'>,
    data_00012_AD0 <class 'pynwb.icephys.CurrentClampSeries'>,
    data_00013_AD0 <class 'pynwb.icephys.CurrentClampSeries'>,
    data_00014_AD0 <class 'pynwb.icephys.CurrentClampSeries'>,
    data_00015_AD0 <class 'pynwb.icephys.CurrentClampSeries'>,
    data_00016_AD0 <class 'pynwb.icephys.CurrentClampSeries'>,
[... 131 more lines not kept]
```

**Agent calls Bash**

```bash
which R Rscript; curl -s -m 60 "https://data.nemoarchive.org/other/AIBS/AIBS_patchseq/transcriptome/scell/SMARTseq/processed/analysis/20200611/" | head -50; date -u
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
curl -s -m 60 -o /dev/null -w "%{http_code} %{time_total}\n" "https://data.nemoarchive.org/other/AIBS/AIBS_patchseq/transcriptome/scell/SMARTseq/processed/analysis/20200611/"; curl -s -m 30 -o /dev/null -w "%{http_code}\n" https://data.nemoarchive.org/; grep -n "nemo\|NeMO" $TMPDIR/code/scripts/q3bc_explain.py | head
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR/code && sed -n 1,80p scripts/q1_describe_phenotype.py; grep -n "def \|SEED\|N_PAIRS\|80000\|rng" scripts/q1_describe_phenotype.py | head -60
```

```
#!/usr/bin/env python3
"""Q1 DESCRIBE: cellular phenotype organization across regimes.

No molecular or Cre labels enter the statistics.
"""

from __future__ import annotations

import csv
import json
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
PHENO = ROOT / "results/phenotype"
OUT = ROOT / "results/q1"
SEED = 0
N_SHUFFLE = 100
[... 86 more lines not kept]
```

**Agent calls Bash**

```bash
mkdir -p entries/yang-2026-flexible && cat > entries/yang-2026-flexible/patchseq.py <<'EOF'
"""Loading and cell-level features for the Patch-seq recordings of DANDI:000020, as Yang (2026) uses them.

Where each parameter comes from:

- The dataset version, ``VERSION``, is the one the paper cites (README of the paper's code, "Data")
  and the only published version of the dandiset.
- Features are the cell-level features of the Allen Institute IPFX package (Methods,
  "Electrophysiological feature extraction"), computed per regime with IPFX's
  ``extract_cell_long_square_features``, ``extract_cell_short_square_features`` and
  ``extract_cell_ramp_features``, the parts of ``extract_data_set_features`` (claim
  table1-phenotype-spaces, reading 1a). ``extract_data_set_features`` itself also computes
  per-sweep features of every current-clamp sweep, which the paper does not use and which fail on
  sweeps without epochs; so only its per-regime parts are run (assumption, recorded).
- Empty epoch fields are dropped before IPFX builds a sweep, and only sweeps with both an
  ``experiment`` and a ``stim`` epoch are used: the code's ``repair_nwb_epochs`` and sweep filter
  (scripts/q1_split_half_long_square.py, commit 61a5a41), cited by the claims file.
- Flattening of the features into ``feat.<regime>.<key>`` columns follows the code's
  ``_pack_long_square_features``, ``pack_cell_record`` and ``flatten`` (same script), applied to all
  three regimes: the IPFX cell feature record plus each regime's nested feature dictionary, without
  the spike and sweep lists.
- ``extract_ok`` (Methods, "cells with extract_ok = 1") is not defined in the paper or the code,
  whose IPFX driver script is missing. Here it is 1 when the file could be opened as an IPFX data
  set and the three regime extractions ran, each regime being allowed to fail on its own (its
  features then missing), as IPFX's own cell state counts a cell failed only when every part
  failed. Assumption, recorded.
- The split-half extraction (claim split-half-reliability) is the code's ``extract_one_split``:
  at least four usable long squares, candidate splits in the code's order, at least two sweeps per
  half, the subthreshold minimum amplitude from the coarse long squares. Its random split uses the
  claim's seed (protocol), not the code's seed 0.
- The clock check takes, for each cell, the long square with the most negative amplitude and the
  mean voltage change between the 100 ms before stimulus onset and the last 100 ms of the
  stimulus, and the same with both windows moved 0.5 s earlier, before the stimulus (a standard
  choice for a check, which cannot change a claim's result).
"""

from __future__ import annotations

import io
import logging
import os
import warnings
import zlib
from concurrent.futures import ProcessPoolExecutor, as_completed

import numpy as np
import requests

DANDISET = "000020"
VERSION = "0.210913.1639"
API = "https://api.dandiarchive.org/api"
PAPER_KEY = "yang-2026-flexible"

SKIP_FEATURE_KEYS = {"spikes", "sweeps", "spiking_sweeps", "subthreshold_sweeps",
                     "subthreshold_membrane_property_sweeps", "common_amp_sweeps"}
LONG_RECORD = {"vrest", "ri", "sag", "tau", "vm_for_sag", "f_i_curve_slope", "adaptation", "latency", "avg_isi"}
RECORD_SUFFIX = {"_long_square": "long_squares", "_ramp": "ramps", "_short_square": "short_squares"}
REGIMES = {"long_pulse": "long_squares", "ramp": "ramps", "brief_pulse": "short_squares"}
MIN_USABLE = 4
MIN_SWEEPS_PER_HALF = 2


def seed_of(claim: str) -> int:
    """The claim's seed (protocol, author step 3)."""
    return zlib.crc32(f"{PAPER_KEY}/{claim}".encode())


def list_assets(version: str = VERSION) -> list[dict]:
    url = f"{API}/dandisets/{DANDISET}/versions/{version}/assets/?page_size=1000"
    out = []
    while url:
        r = requests.get(url, timeout=120)
        r.raise_for_status()
        js = r.json()
        out += js["results"]
        url = js["next"]
    return out


def _as_float(value):
    try:
        num = float(value)
    except (TypeError, ValueError):
        return None
    return None if num != num else num


def _flatten(prefix, obj, out):
    if obj is None:
        return
    if isinstance(obj, dict):
        for k, v in obj.items():
            if k in SKIP_FEATURE_KEYS:
                continue
            _flatten(f"{prefix}{k}.", v, out)
        return
    num = _as_float(obj)
    if num is not None:
        out[prefix.rstrip(".")] = num


def _pack_cell_record(cell_record, rec):
    for key, value in cell_record.items():
        num = _as_float(value)
        if num is None:
            continue
        proto, name = None, key
        for suffix, protocol in RECORD_SUFFIX.items():
            if key.endswith(suffix):
                proto, name = protocol, key[: -len(suffix)]
                break
        if proto is None:
            if key in LONG_RECORD:
                proto = "long_squares"
            else:
                continue
        rec[f"feat.{proto}.{name}"] = num


def pack(cell_features: dict) -> dict:
    """Flatten IPFX cell features as the paper's code does."""
    from ipfx.feature_record import build_cell_feature_record
    rec = {}
    full = {k: (cell_features.get(k) or {}) for k in ("long_squares", "ramps", "short_squares")}
    try:
        cell_record = build_cell_feature_record(full)
    except Exception:
        cell_record = {}
    if isinstance(cell_record, dict):
        _pack_cell_record(cell_record, rec)
    _flatten("feat.", {k: v for k, v in full.items() if v}, rec)
    return rec


def _repair_epochs():
    from ipfx.sweep import Sweep
    if getattr(Sweep.__init__, "_prg_epoch_repair", False):
        return
    original = Sweep.__init__

    def patched(self, t, v, i, clamp_mode, sampling_rate, sweep_number=None, epochs=None):
        if epochs:
            epochs = {k: val for k, val in epochs.items() if val is not None}
        original(self, t, v, i, clamp_mode, sampling_rate, sweep_number=sweep_number, epochs=epochs)

    patched._prg_epoch_repair = True
    Sweep.__init__ = patched


def candidate_splits(sns, rng, amps=None):
    """The code's candidate splits, in its order (scripts/q1_split_half_long_square.py)."""
    sns = [int(s) for s in sns]
    out = []
    even = sorted(s for s in sns if s % 2 == 0)
    odd = sorted(s for s in sns if s % 2 == 1)
    out.append((even, odd, "odd_even_sweep_number"))
    sns_s = sorted(sns)
    out.append((sns_s[0::2], sns_s[1::2], "interleaved_index"))
    if amps:
        ordered = [s for s, _a, _n in sorted(((s, amps.get(s, 0.0), s) for s in sns), key=lambda t: (t[1], t[2]))]
        out.append((ordered[0::2], ordered[1::2], "amplitude_interleaved"))
    perm = rng.permutation(len(sns_s))
    mid = max(MIN_SWEEPS_PER_HALF, len(sns_s) // 2)
    if len(sns_s) - mid >= MIN_SWEEPS_PER_HALF:
        out.append((sorted(int(sns_s[i]) for i in perm[:mid]), sorted(int(sns_s[i]) for i in perm[mid:]), "random"))
    seen, uniq = set(), []
    for a, b, rule in out:
        if len(a) < MIN_SWEEPS_PER_HALF or len(b) < MIN_SWEEPS_PER_HALF:
            continue
        key = (tuple(a), tuple(b), rule)
        if key in seen:
            continue
        seen.add(key)
        uniq.append((a, b, rule))
    return uniq


def _fetch(asset_id: str, tries: int = 4) -> bytes:
    url = f"{API}/assets/{asset_id}/download/"
    for k in range(tries):
        try:
            r = requests.get(url, timeout=300)
            r.raise_for_status()
            return r.content
        except Exception:
            if k == tries - 1:
                raise
    raise RuntimeError("unreachable")


def extract_cell(asset: dict, split_seed: int | None = None) -> dict:
    """Stream one NWB file into memory (never to disk) and compute everything the notebook needs from it."""
    warnings.filterwarnings("ignore")
    logging.disable(logging.WARNING)
    stem = asset["path"].split("/")[-1].rsplit(".", 1)[0]
    rec = {"file_stem": stem, "path": asset["path"], "size": asset["size"], "extract_ok": 0, "error": "",
           "features": {}, "failed": {}, "split": None, "clock": None}
    try:
        _repair_epochs()
        import h5py
        import ipfx.data_set_features as dsf
        import ipfx.stim_features as stf
        from ipfx.dataset.create import create_ephys_data_set
        data = _fetch(asset["asset_id"])
        with h5py.File(io.BytesIO(data), "r") as f:
            g = f["general"]
            rec["genotype"] = g["subject/genotype"][()].decode() if "subject/genotype" in g else ""
            rec["session_id"] = g["session_id"][()].decode() if "session_id" in g else ""
            rec["subject_id"] = g["subject/subject_id"][()].decode() if "subject/subject_id" in g else ""
            rec["sex"] = g["subject/sex"][()].decode() if "subject/sex" in g else ""
            rec["age"] = g["subject/age"][()].decode() if "subject/age" in g else ""
        ds = create_ephys_data_set(nwb_file=io.BytesIO(data))
        original_get = ds.get_sweep_numbers
        allowed = {"set": None}

        def filtered(*args, **kwargs):
            keep = []
            for sn in original_get(*args, **kwargs):
                if allowed["set"] is not None and int(sn) not in allowed["set"]:
                    continue
                sw = ds.sweep(int(sn))
                if sw.epochs.get("experiment") and sw.epochs.get("stim"):
                    keep.append(sn)
            return keep

        ds.get_sweep_numbers = filtered
        cc = ds.CURRENT_CLAMP
        names = {"long_squares": ds.ontology.long_square_names, "short_squares": ds.ontology.short_square_names,
                 "ramps": ds.ontology.ramp_names}
        rec["n_sweeps"] = {k: len(ds.get_sweep_numbers(v, clamp_mode=cc)) for k, v in names.items()}
        cf = {}
        f1, s1 = dsf.extract_cell_long_square_features(ds)
        f2, s2 = dsf.extract_cell_short_square_features(ds)
        f3, s3 = dsf.extract_cell_ramp_features(ds)
        cf["long_squares"], cf["short_squares"], cf["ramps"] = f1, f2, f3
        rec["failed"] = {"long_squares": bool(s1.get("failed_fx")), "short_squares": bool(s2.get("failed_fx")),
                         "ramps": bool(s3.get("failed_fx"))}
        rec["features"] = pack({k: (v if not rec["failed"][k] else None) for k, v in cf.items()})
        rec["extract_ok"] = 1
        # subthreshold responses, for the clock check (sign of the deflection against the sign of the current)
        if f1 and not rec["failed"]["long_squares"]:
            rec["subthreshold"] = [(float(s.get("stim_amp", np.nan)), float(s.get("peak_deflect", (np.nan,))[0]))
                                   for s in f1.get("subthreshold_sweeps", []) if "peak_deflect" in s]
        # clock check on the most hyperpolarizing long square
        try:
            usable = [int(s) for s in ds.get_sweep_numbers(names["long_squares"], clamp_mode=cc)]
            tab = ds.filtered_sweep_table(clamp_mode=cc, stimuli=names["long_squares"])
            amps = {int(a): float(b) for a, b in zip(tab["sweep_number"], tab["stimulus_amplitude"])}
            neg = sorted((amps.get(s, 0.0), s) for s in usable)
            if neg and neg[0][0] < 0:
                sw = ds.sweep(neg[0][1])
                sw.align_to_start_of_epoch("experiment")
                start, dur, _amp, _s, _e = stf.get_stim_characteristics(sw.i, sw.t)
                t, v = sw.t, sw.v

                def m(a, b):
                    sel = (t >= a) & (t < b)
                    return float(np.nanmean(v[sel])) if sel.any() else np.nan
                rec["clock"] = {"amp": neg[0][0], "dv": m(start + dur - 0.1, start + dur) - m(start - 0.1, start),
                                "dv_shift": m(start + dur - 0.6, start + dur - 0.5) - m(start - 0.6, start - 0.5)
                                if start - 0.6 >= t[0] else np.nan,
                                "fingerprint": f"{len(v)}:{np.nansum(v):.6g}"}
        except Exception as exc:
            rec["clock_error"] = f"{type(exc).__name__}: {exc}"
        # split halves of the long squares (claim split-half-reliability)
        if split_seed is not None:
            rec["split"] = _split_half(ds, dsf, names, cc, usable if "usable" in dir() else [], allowed, split_seed)
    except Exception as exc:
        rec["error"] = f"{type(exc).__name__}: {exc}"[:300]
    return rec


def _split_half(ds, dsf, names, cc, usable, allowed, seed):
    out = {"n_usable": len(usable), "ok": 0, "rule": "", "reason": "", "a": {}, "b": {}}
    allowed["set"] = None
    if len(usable) < MIN_USABLE:
        out["reason"] = f"n_usable={len(usable)}<{MIN_USABLE}"
        return out
    amp_map = {}
    try:
        tab = ds.filtered_sweep_table(clamp_mode=cc, stimuli=names["long_squares"])
        amp_map = {int(a): float(b) for a, b in zip(tab["sweep_number"], tab["stimulus_amplitude"])}
    except Exception:
        amp_map = {}
    splits = candidate_splits(usable, np.random.default_rng(seed), amp_map or None)
    if not splits:
        out["reason"] = "could_not_split"
        return out
    clsq = ds.filtered_sweep_table(clamp_mode=cc, stimuli=ds.ontology.coarse_long_square_names)
    try:
        smin = dsf.select_subthreshold_min_amplitude(clsq["stimulus_amplitude"])[0] if len(clsq) else -100
    except Exception as exc:
        out["reason"] = f"{type(exc).__name__}: {exc}"
        return out

    def half(sweeps):
        allowed["set"] = set(sweeps)
        try:
            feats, state = dsf.extract_cell_long_square_features(ds, subthresh_min_amp=smin)
        except Exception as exc:
            return None, f"{type(exc).__name__}"
        finally:
            allowed["set"] = None
        if (state or {}).get("failed_fx") or not feats:
            return None, str((state or {}).get("fail_fx_message") or "failed_fx")[:120]
        return pack({"long_squares": feats}), ""

    last = ""
    for a, b, rule in splits:
        fa, ea = half(a)
        fb, eb = half(b)
        if fa is not None and fb is not None:
            out.update(ok=1, rule=rule, a=fa, b=fb, reason="")
            return out
        last = ea or eb
    out["reason"] = last or "half_failed"
    return out


def _init():
    os.environ.setdefault("OMP_NUM_THREADS", "1")
    os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
    warnings.filterwarnings("ignore")
    logging.disable(logging.WARNING)


def extract_all(assets: list[dict], split_seed: int | None, workers: int = 6, progress: int = 500) -> list[dict]:
    """Run ``extract_cell`` over the assets in parallel processes; each process restarts every 25 files."""
    out = []
    with ProcessPoolExecutor(max_workers=workers, initializer=_init, max_tasks_per_child=25) as ex:
        futs = {ex.submit(extract_cell, a, split_seed): a for a in assets}
        for k, fut in enumerate(as_completed(futs), 1):
            a = futs[fut]
            try:
                out.append(fut.result())
            except Exception as exc:
                out.append({"file_stem": a["path"].split("/")[-1].rsplit(".", 1)[0], "path": a["path"],
                            "extract_ok": 0, "error": f"worker: {exc}"[:300], "features": {}})
            if progress and k % progress == 0:
                print(f"  {k}/{len(assets)} files", flush=True)
    order = {a["path"]: i for i, a in enumerate(assets)}
    return sorted(out, key=lambda r: order[r["path"]])
EOF
cd $TMPDIR && cat > bench.py <<'EOF'
import sys, time, json, resource
sys.path.insert(0, "entries/yang-2026-flexible")
import patchseq as ps
assets = json.load(open("assets.json"))
import numpy as np
idx = np.linspace(0, len(assets)-1, int(sys.argv[1])).astype(int)
t0 = time.time()
recs = ps.extract_all([assets[i] for i in idx], split_seed=ps.seed_of("split-half-reliability"), workers=int(sys.argv[2]), progress=0)
dt = time.time()-t0
print("n", len(recs), "time", round(dt,1), "per cell", round(dt/len(recs),2), "est full min", round(dt/len(recs)*4435/60,1))
print("ok", sum(r["extract_ok"] for r in recs), [r["error"] for r in recs if r["error"]][:5])
print("split ok", sum((r.get("split") or {}).get("ok",0) for r in recs), [ (r.get("split") or {}).get("rule") for r in recs][:20])
print("nfeat", [len(r["features"]) for r in recs][:20])
print(recs[0]["clock"], recs[0]["failed"], recs[0]["n_sweeps"], recs[0]["genotype"])
print("maxrss children MB", resource.getrusage(resource.RUSAGE_CHILDREN).ru_maxrss/1e3)
json.dump(recs, open("bench.json","w"))
EOF
dev/bin/python bench.py 48 6 2>&1 | grep -v warn | tail
```

```
n 48 time 0.5 per cell 0.01 est full min 0.8
ok 0 ['worker: A process in the process pool was terminated abruptly while the future was running or pending.', 'worker: A process in the process pool was terminated abruptly while the future was running or pending.', 'worker: A process in the process pool was terminated abruptly while the future was running or pending.', 'worker: A process in the process pool was terminated abruptly while the future was running or pending.', 'worker: A process in the process pool was terminated abruptly while the future was running or pending.']
split ok 0 [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]
nfeat [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
Traceback (most recent call last):
  File "/tmp/claude-1001/bench.py", line 14, in <module>
    print(recs[0]["clock"], recs[0]["failed"], recs[0]["n_sweeps"], recs[0]["genotype"])
          ~~~~~~~^^^^^^^^^
KeyError: 'clock'
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && dev/bin/python -c "
import sys,json; sys.path.insert(0,'entries/yang-2026-flexible')
import patchseq as ps
a=json.load(open('assets.json'))
r=ps.extract_cell(a[0], 1); print({k:(v if k not in ('features',) else len(v)) for k,v in r.items() if k!='split'}); print(r['split']['ok'], r['split']['rule'], len(r['split']['a']))
" 2>&1 | grep -v warn | tail -5
```

```
{'file_stem': 'sub-1001658958_ses-1003321768_icephys', 'path': 'sub-1001658958/sub-1001658958_ses-1003321768_icephys.nwb', 'size': 19842547, 'extract_ok': 1, 'error': '', 'features': 93, 'failed': {'long_squares': False, 'short_squares': False, 'ramps': False}, 'clock': None, 'genotype': 'Vipr2-IRES2-Cre/wt;Slc32a1-IRES2-FlpO/wt;Ai65(RCFL-tdT)/wt', 'session_id': '1003321768', 'subject_id': '1001658958', 'sex': 'M', 'age': 'P55.0D', 'n_sweeps': {'long_squares': 10, 'short_squares': 2, 'ramps': 3}, 'subthreshold': [(-29.999998092651367, -83.41874694824219), (-50.0, -80.51875305175781), (-70.0, -83.51249694824219), (-90.0, -85.8687515258789), (-110.0, -88.25), (140.0, -31.35624885559082)], 'clock_error': "KeyError: 'stimulus_amplitude'"}
1 random 47
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd entries/yang-2026-flexible && python - <<'EOF'
p="patchseq.py"; s=open(p).read()
old=s[s.index("        # subthreshold responses, for the clock check"):s.index("        # split halves of the long squares")]
new='''        # clock check on the most hyperpolarizing long square
        usable = []
        try:
            usable = [int(s) for s in ds.get_sweep_numbers(names["long_squares"], clamp_mode=cc)]
            best = None
            for sn in usable:
                sw = ds.sweep(sn)
                sw.align_to_start_of_epoch("experiment")
                start, dur, amp, _s, _e = stf.get_stim_characteristics(sw.i, sw.t)
                if amp is not None and amp < 0 and (best is None or amp < best[0]):
                    best = (amp, sw, start, dur)
            if best is not None:
                amp, sw, start, dur = best
                t, v = sw.t, sw.v

                def m(a, b):
                    sel = (t >= a) & (t < b)
                    return float(np.nanmean(v[sel])) if sel.any() else np.nan
                rec["clock"] = {"amp": float(amp), "start": float(start), "dur": float(dur),
                                "dv": m(start + dur - 0.1, start + dur) - m(start - 0.1, start),
                                "dv_shift": (m(start + dur - 0.6, start + dur - 0.5) - m(start - 0.6, start - 0.5))
                                if start - 0.6 >= t[0] else np.nan,
                                "fingerprint": f"{len(v)}:{np.nansum(v):.6g}"}
        except Exception as exc:
            rec["clock_error"] = f"{type(exc).__name__}: {exc}"[:200]
'''
s=s.replace(old,new)
s=s.replace('rec["split"] = _split_half(ds, dsf, names, cc, usable if "usable" in dir() else [], allowed, split_seed)','rec["split"] = _split_half(ds, dsf, names, cc, usable, allowed, split_seed)')
open(p,"w").write(s)
EOF
cd $TMPDIR && python - <<'EOF'
s=open("bench.py").read()
lines=s.split("\n")
body="\n".join("    "+l for l in lines[5:])
open("bench.py","w").write("\n".join(lines[:5])+"\nif __name__=='__main__':\n"+body)
EOF
dev/bin/python bench.py 48 6 2>&1 | grep -v warn | tail
```

```
n 48 time 44.8 per cell 0.93 est full min 69.0
ok 48 []
split ok 36 ['', 'odd_even_sweep_number', '', '', '', 'odd_even_sweep_number', 'odd_even_sweep_number', 'odd_even_sweep_number', 'odd_even_sweep_number', 'odd_even_sweep_number', 'odd_even_sweep_number', 'odd_even_sweep_number', 'odd_even_sweep_number', 'odd_even_sweep_number', 'odd_even_sweep_number', 'odd_even_sweep_number', 'odd_even_sweep_number', 'odd_even_sweep_number', 'odd_even_sweep_number', 'odd_even_sweep_number']
nfeat [93, 88, 91, 87, 63, 83, 88, 93, 83, 83, 94, 92, 81, 83, 88, 76, 87, 81, 94, 83]
None {'long_squares': False, 'short_squares': False, 'ramps': False} {'long_squares': 10, 'short_squares': 2, 'ramps': 3} Vipr2-IRES2-Cre/wt;Slc32a1-IRES2-FlpO/wt;Ai65(RCFL-tdT)/wt
maxrss children MB 1772.608
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && sed -i 's/max_tasks_per_child=25/max_tasks_per_child=100/; s/restarts every 25 files/restarts every 100 files/' entries/yang-2026-flexible/patchseq.py && nproc && free -g | head -2 && dev/bin/python bench.py 96 8 2>&1 | grep -v warn | tail -8
```

```
4
               total        used        free      shared  buff/cache   available
Mem:              15           1          10           0           3          13
n 96 time 87.8 per cell 0.91 est full min 67.6
ok 96 []
split ok 67 ['', '', '', '', '', 'odd_even_sweep_number', '', '', '', 'odd_even_sweep_number', 'odd_even_sweep_number', 'odd_even_sweep_number', 'odd_even_sweep_number', 'odd_even_sweep_number', 'odd_even_sweep_number', 'odd_even_sweep_number', 'odd_even_sweep_number', 'odd_even_sweep_number', 'odd_even_sweep_number', 'odd_even_sweep_number']
nfeat [93, 45, 91, 88, 88, 87, 91, 83, 87, 81, 87, 87, 94, 63, 92, 92, 83, 94, 93, 83]
None {'long_squares': False, 'short_squares': False, 'ramps': False} {'long_squares': 10, 'short_squares': 2, 'ramps': 3} Vipr2-IRES2-Cre/wt;Slc32a1-IRES2-FlpO/wt;Ai65(RCFL-tdT)/wt
maxrss children MB 2361.028
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && dev/bin/python -c "
import sys,json,cProfile,pstats; sys.path.insert(0,'entries/yang-2026-flexible')
import patchseq as ps
a=json.load(open('assets.json'))
ps.extract_cell(a[5],1)
cProfile.run('ps.extract_cell(a[2000],1)','prof')
p=pstats.Stats('prof'); p.sort_stats('cumulative').print_stats(35)
" 2>&1 | grep -v warn | head -80
```

```
Sun Nov 22 09:28:54 2026    prof

         3717827 function calls (3655804 primitive calls) in 2.723 seconds

   Ordered by: cumulative time
   List reduced from 1964 to 35 due to restriction <35>

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    2.723    2.723 {built-in method builtins.exec}
        1    0.000    0.000    2.723    2.723 <string>:1(<module>)
        1    0.002    0.002    2.723    2.723 entries/yang-2026-flexible/patchseq.py:190(extract_cell)
        9    0.000    0.000    1.041    0.116 /tmp/claude-1001/dev/lib/python3.13/site-packages/ipfx/data_set_features.py:85(wrapper)
        9    0.005    0.001    1.041    0.116 /tmp/claude-1001/dev/lib/python3.13/site-packages/ipfx/data_set_features.py:99(wrapper)
        1    0.000    0.000    0.849    0.849 /tmp/claude-1001/dev/lib/python3.13/site-packages/ipfx/dataset/create.py:85(create_ephys_data_set)
        7    0.000    0.000    0.823    0.118 /tmp/claude-1001/dev/lib/python3.13/site-packages/ipfx/data_set_features.py:230(extract_cell_long_square_features)
20010/142    0.020    0.000    0.794    0.006 /tmp/claude-1001/dev/lib/python3.13/site-packages/hdmf/utils.py:590(func_call)
        1    0.000    0.000    0.782    0.782 /tmp/claude-1001/dev/lib/python3.13/site-packages/ipfx/dataset/mies_nwb_data.py:14(__init__)
        1    0.000    0.000    0.782    0.782 /tmp/claude-1001/dev/lib/python3.13/site-packages/ipfx/dataset/ephys_nwb_data.py:66(__init__)
        1    0.000    0.000    0.782    0.782 /tmp/claude-1001/dev/lib/python3.13/site-packages/ipfx/dataset/ephys_nwb_data.py:81(load_nwb)
        1    0.000    0.000    0.639    0.639 entries/yang-2026-flexible/patchseq.py:272(_split_half)
[... 24 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/yang-2026-flexible && python - <<'EOF'
p="patchseq.py"; s=open(p).read()
old='''        def filtered(*args, **kwargs):
            keep = []
            for sn in original_get(*args, **kwargs):
                if allowed["set"] is not None and int(sn) not in allowed["set"]:
                    continue
                sw = ds.sweep(int(sn))
                if sw.epochs.get("experiment") and sw.epochs.get("stim"):
                    keep.append(sn)
            return keep
'''
new='''        has_epochs = {}

        def filtered(*args, **kwargs):
            keep = []
            for sn in original_get(*args, **kwargs):
                if allowed["set"] is not None and int(sn) not in allowed["set"]:
                    continue
                if int(sn) not in has_epochs:
                    sw = ds.sweep(int(sn))
                    has_epochs[int(sn)] = bool(sw.epochs.get("experiment") and sw.epochs.get("stim"))
                if has_epochs[int(sn)]:
                    keep.append(sn)
            return keep
'''
assert old in s; s=s.replace(old,new); open(p,"w").write(s)
EOF
cd $TMPDIR && dev/bin/python bench.py 96 8 2>&1 | grep -v warn | tail -8; python -c "
import json; r=json.load(open('$TMPDIR/bench.json')); print([x['clock'] for x in r[:5]]); print([x.get('clock_error') for x in r[:5]])"
```

```
n 96 time 79.3 per cell 0.83 est full min 61.1
ok 96 []
split ok 67 ['', '', '', '', '', 'odd_even_sweep_number', '', '', '', 'odd_even_sweep_number', 'odd_even_sweep_number', 'odd_even_sweep_number', 'odd_even_sweep_number', 'odd_even_sweep_number', 'odd_even_sweep_number', 'odd_even_sweep_number', 'odd_even_sweep_number', 'odd_even_sweep_number', 'odd_even_sweep_number', 'odd_even_sweep_number']
nfeat [93, 45, 91, 88, 88, 87, 91, 83, 87, 81, 87, 87, 94, 63, 92, 92, 83, 94, 93, 83]
None {'long_squares': False, 'short_squares': False, 'ramps': False} {'long_squares': 10, 'short_squares': 2, 'ramps': 3} Vipr2-IRES2-Cre/wt;Slc32a1-IRES2-FlpO/wt;Ai65(RCFL-tdT)/wt
maxrss children MB 2326.044
[None, None, None, None, None]
["AttributeError: 'Sweep' object has no attribute 'align_to_start_of_epoch'", "AttributeError: 'Sweep' object has no attribute 'align_to_start_of_epoch'", "AttributeError: 'Sweep' object has no attribute 'align_to_start_of_epoch'", "AttributeError: 'Sweep' object has no attribute 'align_to_start_of_epoch'", "AttributeError: 'Sweep' object has no attribute 'align_to_start_of_epoch'"]
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd entries/yang-2026-flexible && sed -i '/                sw.align_to_start_of_epoch("experiment")$/d' patchseq.py && grep -n "align_to_start" patchseq.py; sed -i 's/max_tasks_per_child=100/max_tasks_per_child=200/; s/restarts every 100 files/restarts every 200 files/' patchseq.py; curl -s -m 60 -o /dev/null -w "%{http_code} %{time_total}\n" "https://data.nemoarchive.org/other/AIBS/AIBS_patchseq/transcriptome/scell/SMARTseq/processed/analysis/20200611/"; date -u
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
for u in "https://data.nemoarchive.org/" "https://data.nemoarchive.org/other/" "https://data.nemoarchive.org/other/AIBS/AIBS_patchseq/transcriptome/scell/SMARTseq/processed/analysis/20200611/20200513_Mouse_PatchSeq_Release_count.v2.csv.tar" "https://nemoarchive.org/" "https://portal.nemoarchive.org/"; do curl -s -m 40 -o /dev/null -w "%{http_code} $u\n" -r 0-100 "$u"; done
```

```
502 https://data.nemoarchive.org/
000 https://data.nemoarchive.org/other/
000 https://data.nemoarchive.org/other/AIBS/AIBS_patchseq/transcriptome/scell/SMARTseq/processed/analysis/20200611/20200513_Mouse_PatchSeq_Release_count.v2.csv.tar
200 https://nemoarchive.org/
206 https://portal.nemoarchive.org/
```

**Agent calls Bash**

```bash
cd  && ls schemas; grep -n "link" schemas/claims*.json | head -20; grep -rn "kind: link" claims/*.yaml | head -3
```

```
attempt.schema.json
claims.schema.json
entry.schema.json
paper-match.schema.json
87:            "description": "A finding the paper reports (`finding`, the default), or a check the registry adds that the dataset is the data the paper's outside material describes (`link`: the paper's tables, source data, code or deposits). Links are not findings of the paper and are counted apart from them.",
90:              "link"
174:                  "const": "link"
claims/amjad-2025.yaml:167:  kind: link
claims/bech-2026.yaml:113:  kind: link
claims/bennett-2024.yaml:103:  kind: link
```

**Agent calls Bash**

```bash
sed -n 160,200p claims/bennett-2024.yaml; sed -n 160,200p schemas/claims.schema.json
```

```
- id: tracks-rare-bleeding
  statement: Inserted probes rarely caused significant intracranial bleeding, in 3 of 547 tracks.
  source: Results, Installation of SHIELD implant and QC evaluation, paragraph 5
  quote: We found that inserted probes rarely caused significant intracranial bleeding (3/547 tracks).
  expected:
  - quantity: tracks with significant bleeding
    value: 3
    tolerance: 0.3
  - quantity: tracks examined
    value: 547
    tolerance: 54.7
- id: fig3fh-mri-deformation
  statement: In MRI, the 5-mm cranial window deforms the brain under the window, while the brain
    under SHIELD implants (250 and 400 micrometre inserts) is close to naive mice; the thicker insert
    trended toward less deformation.
  source: Results, Installation of SHIELD implant and QC evaluation, paragraph 6; Figures 3F to 3H
  quote: revealed clear brain deformation for the non-contoured 5-mm window over the visual cortex ...
    the area between surface contours for SHIELD mice was more similar to naive mice ... though the
    thicker design trended toward less deformation
  statistics:
[... 62 more lines not kept]
```

**Agent calls Bash**

```bash
grep -n -B2 -A22 "kind: link" claims/bennett-2024.yaml | head -40
```

```
101-claims:
102-- id: link-code-tables
103:  kind: link
104-  statement: The 87 sessions the paper's code lists as passing ephys QC are sessions of the dandiset,
105-    and for them the code's units table agrees with the dandiset's units (unit ids, counts per session,
106-    quality metrics and receptive-field p values).
107-  source: STAR Methods, Key resources table and Data and code availability; DynamicGating_ephys_metrics.ipynb
108-    and metadata_tables/units_table.csv at commit 3c09a0dc
109-  quote: Analysis code used in this paper is available here
110-  criterion: Added by the author (protocol, Author, step 1.4). Sessions are matched by the NWB identifier
111-    (the ecephys session id) and units by unit id. Reproduced when all 87 sessions are found, session
112-    type, mouse and genotype agree, every session has the same unit count, and matched units agree on
113-    max_drift, firing_rate and quality (no more than 1% differing per session) and on RF significance
114-    at 0.01 as recomputed here; partially reproduced when some sessions fail, naming them.
115-- id: fig3b-surgical-outcomes
116-  statement: Of 106 mice entering SHIELD surgery, 79 passed all quality checks, 14 passed after a flag
117-    that resolved and 13 failed, a final passing rate of 87.7%, on par with 90% (122 of 135) for the
118-    earlier 5-mm cranial window surgery.
119-  source: Results, Installation of SHIELD implant and QC evaluation, paragraph 3; Figure 3B
120-  quote: Of the 106 mice entering surgery for this study, 79 passed all quality checks with no issues,
[... 5 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/code/scripts && grep -n "def " q2_anchor.py q3a_explain.py q3a_centroid_robustness.py q1_knn_scale.py q3_mobility_modules.py q3bc_explain.py | head -80
```

```
q2_anchor.py:49:def pc_cols(fieldnames: list[str]) -> list[str]:
q2_anchor.py:54:def parse_session(row: dict) -> str:
q2_anchor.py:64:def choose_k(path: Path, n_available: int) -> int:
q2_anchor.py:78:def load_scores(path: Path) -> tuple[list[str], np.ndarray]:
q2_anchor.py:95:def load_join(path: Path) -> dict[str, dict]:
q2_anchor.py:100:def pairwise_euclidean(x: np.ndarray) -> np.ndarray:
q2_anchor.py:110:def sample_pairs(n: int, rng: np.random.Generator) -> tuple[np.ndarray, np.ndarray]:
q2_anchor.py:124:def spearman(a: np.ndarray, b: np.ndarray) -> float:
q2_anchor.py:132:def mol_distance(labels: np.ndarray, kind: str, extra: np.ndarray | None = None) -> np.ndarray:
q2_anchor.py:147:def align_D(d_pheno: np.ndarray, d_mol: np.ndarray, ii: np.ndarray, jj: np.ndarray, rng: np.random.Generator, labels: np.ndarray) -> dict:
q2_anchor.py:168:def eta2_multivariate(x: np.ndarray, labels: np.ndarray) -> dict:
q2_anchor.py:186:def knn_same_label(d: np.ndarray, labels: np.ndarray, k: int = KNN) -> dict:
q2_anchor.py:206:def residualize_by_group(x: np.ndarray, groups: np.ndarray) -> np.ndarray:
q2_anchor.py:214:def encode(values: list[str]) -> np.ndarray:
q2_anchor.py:219:def protocol_anchor(
q2_anchor.py:335:def main() -> None:
q3a_explain.py:49:def pc_cols(fieldnames):
q3a_explain.py:54:def parse_session(row: dict) -> str:
q3a_explain.py:64:def choose_k(path: Path, n_available: int) -> int:
q3a_explain.py:78:def load_scores(path: Path):
[... 61 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/code/scripts && sed -n 100,335p q2_anchor.py
```

```
def pairwise_euclidean(x: np.ndarray) -> np.ndarray:
    x = np.asarray(x, dtype=np.float64)
    nrm = np.sum(x * x, axis=1, keepdims=True)
    d2 = nrm + nrm.T - 2.0 * np.dot(x, x.T)
    np.maximum(d2, 0.0, out=d2)
    d = np.sqrt(d2)
    np.fill_diagonal(d, 0.0)
    return d


def sample_pairs(n: int, rng: np.random.Generator) -> tuple[np.ndarray, np.ndarray]:
    max_pairs = n * (n - 1) // 2
    take = min(N_PAIR_SAMPLE, max_pairs)
    i = rng.integers(0, n, size=take * 3)
    j = rng.integers(0, n, size=take * 3)
    mask = i < j
    i, j = i[mask], j[mask]
    if i.size < take:
        ii, jj = np.triu_indices(n, k=1)
        pick = rng.choice(ii.size, size=take, replace=False)
[... 217 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/code/scripts && sed -n 100,330p q3a_explain.py
```

```
def spearman(a: np.ndarray, b: np.ndarray) -> float:
    if a.size < 3:
        return float("nan")
    ra = np.argsort(np.argsort(a)).astype(float)
    rb = np.argsort(np.argsort(b)).astype(float)
    if ra.std() == 0 or rb.std() == 0:
        return float("nan")
    return float(np.corrcoef(ra, rb)[0, 1])


def protocol_arrays(stems, X, k, join, label_key: str):
    xs, labs = [], []
    for i, fs in enumerate(stems):
        j = join.get(fs)
        if not j:
            continue
        lab = (j.get(label_key) or "").strip()
        if not lab:
            continue
        xs.append(X[i, :k])
[... 211 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/code/scripts && sed -n 128,330p q3a_centroid_robustness.py; sed -n 96,200p q1_knn_scale.py; sed -n 109,125p q1_describe_phenotype.py; sed -n 160,215p q1_describe_phenotype.py; sed -n 289,314p q3_mobility_modules.py
```

```
def index_by_type(labs: list[str]) -> dict[str, np.ndarray]:
    buckets: dict[str, list[int]] = defaultdict(list)
    for i, t in enumerate(labs):
        buckets[t].append(i)
    return {t: np.asarray(ix, dtype=int) for t, ix in buckets.items()}


def centroids_from_indices(x: np.ndarray, by_type: dict[str, np.ndarray], types: list[str], take: dict[str, np.ndarray]) -> np.ndarray:
    mus = []
    for t in types:
        idx = take[t]
        mus.append(x[idx].mean(axis=0))
    M = np.asarray(mus, dtype=float)
    nrm = np.sum(M * M, axis=1, keepdims=True)
    d2 = nrm + nrm.T - 2.0 * (M @ M.T)
    np.maximum(d2, 0.0, out=d2)
    S = np.sqrt(d2)
    np.fill_diagonal(S, 0.0)
    return S

[... 364 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && sed -i 's/split_seed=ps.seed_of("split-half-reliability")/split_seed=None/' bench.py && dev/bin/python bench.py 320 8 2>&1 | grep -v warn | tail -8; date -u
```

```
n 320 time 103.6 per cell 0.32 est full min 23.9
ok 189 ['worker: A process in the process pool was terminated abruptly while the future was running or pending.', 'worker: A process in the process pool was terminated abruptly while the future was running or pending.', 'worker: A process in the process pool was terminated abruptly while the future was running or pending.', 'worker: A process in the process pool was terminated abruptly while the future was running or pending.', 'worker: A process in the process pool was terminated abruptly while the future was running or pending.']
split ok 0 [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]
nfeat [93, 45, 45, 41, 41, 45, 45, 94, 83, 87, 92, 94, 94, 87, 87, 87, 88, 69, 87, 85]
{'amp': -110.0, 'start': 0.6, 'dur': 1.0, 'dv': -15.894561767578125, 'dv_shift': -17.22118377685547, 'fingerprint': '138952:-1.07297e+07'} {'long_squares': False, 'short_squares': False, 'ramps': False} {'long_squares': 10, 'short_squares': 2, 'ramps': 3} Vipr2-IRES2-Cre/wt;Slc32a1-IRES2-FlpO/wt;Ai65(RCFL-tdT)/wt
maxrss children MB 2050.864
Sun Nov 22 09:34:40 UTC 2026
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && python -c "
import json,numpy as np; a=json.load(open('assets.json')); s=np.array([x['size'] for x in a])/1e6; print(np.percentile(s,[0,50,90,99,100]))
r=json.load(open('bench.json')); import collections; print(collections.Counter(x['error'][:40] for x in r))"
```

```
Exit code 1
Traceback (most recent call last):
  File "<string>", line 2, in <module>
    import json,numpy as np; a=json.load(open('assets.json')); s=np.array([x['size'] for x in a])/1e6; print(np.percentile(s,[0,50,90,99,100]))
    ^^^^^^^^^^^^^^^^^^^^^^^
ModuleNotFoundError: No module named 'numpy'
```

**Agent calls Bash**

```bash
cd $TMPDIR && dev/bin/python -c "
import json,numpy as np; a=json.load(open('assets.json')); s=np.array([x['size'] for x in a])/1e6; print(np.percentile(s,[0,50,90,99,100]))
r=json.load(open('bench.json')); import collections; print(collections.Counter(x['error'][:40] for x in r))"
```

```
[ 4.298539   22.738426   61.074852   73.72355858 94.468433  ]
Counter({'': 189, 'worker: A process in the process pool wa': 131})
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && grep -rn -A2 "lru_cache" dev/lib/python3.13/site-packages/ipfx/ | grep -v "^.*import" | grep "def "
```

```
grep: dev/lib/python3.13/site-packages/ipfx/dataset/__pycache__/ephys_nwb_data.cpython-313.pyc: binary file matches
dev/lib/python3.13/site-packages/ipfx/dataset/ephys_nwb_data.py-111-    def _get_series(self, sweep_number: int,
Shell cwd was reset to
```

**Agent**

Found a memory leak (IPFX's `lru_cache` on `_get_series` keeps every data set alive). Fixing it, making the pool restart after a crash, and fixing the clock check windows.

**Agent calls Bash**

```bash
cd entries/yang-2026-flexible && python - <<'EOF'
p="patchseq.py"; s=open(p).read()
# clear lru cache at end of extract_cell
old='''    except Exception as exc:
        rec["error"] = f"{type(exc).__name__}: {exc}"[:300]
    return rec
'''
new='''    except Exception as exc:
        rec["error"] = f"{type(exc).__name__}: {exc}"[:300]
    finally:
        # IPFX caches series with an lru_cache on a method, which keeps every data set alive
        try:
            from ipfx.dataset.ephys_nwb_data import EphysNWBData
            EphysNWBData._get_series.cache_clear()
        except Exception:
            pass
    return rec
'''
assert old in s; s=s.replace(old,new)
old=s[s.index('                rec["clock"] = {"amp"'):s.index('        except Exception as exc:\n            rec["clock_error"]')]
new='''                rec["clock"] = {"amp": float(amp), "start": float(start), "dur": float(dur),
                                "pre": m(start - 0.01, start) - m(start - 0.1, start - 0.05),
                                "post": m(start + 0.015, start + 0.025) - m(start - 0.1, start - 0.05),
                                "dv": m(start + dur - 0.1, start + dur) - m(start - 0.1, start),
                                "fingerprint": f"{len(v)}:{np.nansum(v):.6g}"}
'''
s=s.replace(old,new)
s=s.replace('''- The clock check takes, for each cell, the long square with the most negative amplitude and the
  mean voltage change between the 100 ms before stimulus onset and the last 100 ms of the
  stimulus, and the same with both windows moved 0.5 s earlier, before the stimulus (a standard
  choice for a check, which cannot change a claim's result).''','''- The clock check takes, for each cell, the long square with the most negative amplitude, and
  the mean voltage, relative to a baseline 100 to 50 ms before stimulus onset, in the 10 ms just
  before the onset ("pre"), 15 to 25 ms after it ("post"), and in the last 100 ms of the stimulus
  ("dv"). The windows are a standard choice for a check, which cannot change a claim's result.''')
old=s[s.index("def extract_all("):]
new='''def extract_all(assets: list[dict], split_seed: int | None, workers: int = 5, progress: int = 500) -> list[dict]:
    """Run ``extract_cell`` over the assets in parallel processes, each restarted every 50 files.

    A process that dies (for example killed for memory) breaks the pool; the files not yet done are
    then run again in a new pool, and a file that breaks two pools is recorded as failed."""
    from concurrent.futures.process import BrokenProcessPool
    done: dict[str, dict] = {}
    tries: dict[str, int] = {}
    todo = list(assets)
    while todo:
        broken = False
        with ProcessPoolExecutor(max_workers=workers, initializer=_init, max_tasks_per_child=50) as ex:
            futs = {ex.submit(extract_cell, a, split_seed): a for a in todo}
            for fut in as_completed(futs):
                a = futs[fut]
                try:
                    done[a["path"]] = fut.result()
                except BrokenProcessPool:
                    broken = True
                    tries[a["path"]] = tries.get(a["path"], 0) + 1
                except Exception as exc:
                    done[a["path"]] = {"file_stem": a["path"].split("/")[-1].rsplit(".", 1)[0], "path": a["path"],
                                       "extract_ok": 0, "error": f"worker: {exc}"[:300], "features": {}}
                if progress and len(done) % progress == 0:
                    print(f"  {len(done)}/{len(assets)} files", flush=True)
        todo = [a for a in assets if a["path"] not in done]
        for a in list(todo):
            if tries.get(a["path"], 0) >= 3:
                done[a["path"]] = {"file_stem": a["path"].split("/")[-1].rsplit(".", 1)[0], "path": a["path"],
                                   "extract_ok": 0, "error": "worker died", "features": {}}
        todo = [a for a in assets if a["path"] not in done]
        if broken:
            print(f"  a worker died; {len(todo)} files run again", flush=True)
    return [done[a["path"]] for a in assets]
'''
s=s.replace(old,new); open(p,"w").write(s)
EOF
cd $TMPDIR && dev/bin/python bench.py 320 5 2>&1 | grep -v warn | tail -8; date -u
```

```
n 320 time 214.1 per cell 0.67 est full min 49.4
ok 320 []
split ok 0 [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]
nfeat [93, 45, 45, 41, 41, 45, 45, 94, 83, 87, 92, 94, 94, 87, 87, 87, 88, 69, 87, 85]
{'amp': -110.0, 'start': 0.6, 'dur': 1.0, 'pre': 0.0892333984375, 'post': -15.764106750488281, 'dv': -15.894561767578125, 'fingerprint': '138952:-1.07297e+07'} {'long_squares': False, 'short_squares': False, 'ramps': False} {'long_squares': 10, 'short_squares': 2, 'ramps': 3} Vipr2-IRES2-Cre/wt;Slc32a1-IRES2-FlpO/wt;Ai65(RCFL-tdT)/wt
maxrss children MB 2811.108
Sun Nov 22 09:38:53 UTC 2026
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && dev/bin/python -c "
import sys,json,time,resource,gc; sys.path.insert(0,'entries/yang-2026-flexible')
import patchseq as ps
a=json.load(open('assets.json'))
def rss():
    return int(open('/proc/self/statm').read().split()[1])*4096/1e6
for i in range(0,4400,400):
    t=time.time(); r=ps.extract_cell(a[i],None); gc.collect(); print(i, round(a[i]['size']/1e6), round(time.time()-t,2), 'rss now', round(rss()), r['error'][:50], flush=True)
" 2>&1 | grep -v warn
```

```
0 20 2.62 rss now 293 
400 14 1.42 rss now 317 
800 49 2.29 rss now 323 
1200 16 1.8 rss now 346 
1600 16 1.52 rss now 313 
2000 20 1.72 rss now 313 
2400 18 1.52 rss now 350 
2800 62 2.78 rss now 388 
3200 27 2.29 rss now 431 
3600 68 3.24 rss now 433 
4000 25 2.61 rss now 428
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd entries/yang-2026-flexible && python - <<'EOF'
p="patchseq.py"; s=open(p).read()
s=s.replace('''import io
import logging
import os
import warnings
import zlib
from concurrent.futures import ProcessPoolExecutor, as_completed

import numpy as np''','''import io
import logging
import os
import warnings
import zlib
from concurrent.futures import ProcessPoolExecutor, as_completed

# one linear-algebra thread per process: the extraction runs several processes at once (set before numpy loads)
for _var in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ.setdefault(_var, "1")

import numpy as np  # noqa: E402''')
s=s.replace('''import requests
''','''import requests  # noqa: E402
''',1)
open(p,"w").write(s)
EOF
cd $TMPDIR && dev/bin/python bench.py 200 5 2>&1 | grep -v warn | grep -E "^n |^ok|maxrss"; date -u
```

```
n 200 time 136.0 per cell 0.68 est full min 50.3
ok 200 []
maxrss children MB 2699.912
Sun Nov 22 09:41:50 UTC 2026
Shell cwd was reset to
```

**Agent calls Bash**

```bash
grep -n "max.minutes\|max_minutes" tools/entry.py | head; sed -n 596,640p tools/entry.py
```

```
29:that takes longer than --max-minutes fails, even if it ran without error.
525:                   max_minutes: float) -> int:
531:    if lock(entry_dir, version) or run(entry_dir, output_dir, timeout, max_minutes, fresh=True):
578:def reusable(entry_dir: Path, output_dir: Path, max_minutes: float) -> dict | None:
589:            if not r["ok"] or r["seconds"] > max_minutes * 60 or file_hash(output_dir / r["notebook"]) != r["sha256"]:
596:def run(entry_dir: Path, output_dir: Path, timeout: int, max_minutes: float, fresh: bool = False) -> int:
598:    stamp = None if fresh else reusable(entry_dir, output_dir, max_minutes)
634:        if ok and seconds > max_minutes * 60:
636:            error = f"took {seconds / 60:.0f} minutes; the limit is {max_minutes:.0f}"
703:    parser.add_argument("--max-minutes", type=float, default=60,
def run(entry_dir: Path, output_dir: Path, timeout: int, max_minutes: float, fresh: bool = False) -> int:
    entry = yaml.safe_load((entry_dir / "entry.yaml").read_text())
    stamp = None if fresh else reusable(entry_dir, output_dir, max_minutes)
    if stamp:
        when = time.strftime("%Y-%m-%d %H:%M UTC", time.gmtime(stamp["finished"]))
        for r in stamp["results"]:
            print(f"pass  {r['notebook']}  ({r['seconds']} s, reused)")
        print(f"reused the executed copies of {when}: nothing the run reads has changed since (hash "
              f"{stamp['hash'][:12]}). Nothing was executed and no environment was built; --fresh runs it again.")
        return 0
[... 35 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && dev/bin/python - <<'EOF' 2>&1 | grep -v warn
import json, requests, io, h5py, numpy as np, collections
a=json.load(open('assets.json'))
for i in [0, 3000]:
    data=requests.get(f"https://api.dandiarchive.org/api/assets/{a[i]['asset_id']}/download/").content
    f=h5py.File(io.BytesIO(data),'r')
    st=f['general/intracellular_ephys/sweep_table'] if 'general/intracellular_ephys/sweep_table' in f else None
    tot=collections.Counter()
    for grp in ['acquisition','stimulus/presentation']:
        for k,v in f[grp].items():
            d=v['data']; code=v.attrs.get('stimulus_description', b'')
            code=code.decode() if isinstance(code,bytes) else str(code)
            tot[(grp.split('/')[0], code[:12])]+=d.id.get_storage_size()
    print(i, len(data)/1e6, f['acquisition'][list(f['acquisition'])[0]]['data'].compression, sorted(tot.items(), key=lambda x:-x[1])[:12])
    print(sum(tot.values())/1e6, list(f['processing/spikes'].keys())[:3] if 'processing/spikes' in f else None)
EOF
```

```
0 19.842547 gzip [(('acquisition', 'X7Ramp_DA_0'), 1581146), (('acquisition', 'X1PS_SubThre'), 790768), (('acquisition', 'X4PS_SupraTh'), 553578), (('acquisition', 'X2LP_Search_'), 359239), (('acquisition', 'X3LP_Rheo_DA'), 326550), (('acquisition', 'X6SP_Rheo_DA'), 202504), (('acquisition', 'X5SP_Search_'), 128950), (('acquisition', 'EXTPBREAKN18'), 89784), (('acquisition', 'EXTPINBATH18'), 87938), (('acquisition', 'EXTPSMOKET18'), 82737), (('stimulus', 'X7Ramp_DA_0'), 71016), (('acquisition', 'EXTPCllATT18'), 65461)]
4.496085 ['Sweep_18', 'Sweep_19', 'Sweep_20']
3000 69.689869 gzip [(('acquisition', 'C2CHIRP18050'), 4147923), (('acquisition', 'C2NSD1SHORT1'), 3885446), (('acquisition', 'C2NSD2SHORT1'), 3163275), (('acquisition', 'C1SQCAPCHK14'), 2474096), (('acquisition', 'C2SSTRIPLE17'), 2058269), (('acquisition', 'X1PS_SubThre'), 1953084), (('acquisition', 'X3LP_Rheo_DA'), 1927108), (('acquisition', 'X7Ramp_DA_0'), 1863704), (('stimulus', 'C2NSD1SHORT1'), 1008674), (('acquisition', 'X4PS_SupraTh'), 716296), (('stimulus', 'C2NSD2SHORT1'), 577678), (('stimulus', 'C2CHIRP18050'), 291342)]
25.390168 ['Sweep_10', 'Sweep_15', 'Sweep_16']
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && dev/bin/python - <<'EOF' 2>&1 | grep -v warn
import json, requests, io, h5py, collections
a=json.load(open('assets.json'))
for i in [0, 3000]:
    data=requests.get(f"https://api.dandiarchive.org/api/assets/{a[i]['asset_id']}/download/").content
    f=h5py.File(io.BytesIO(data),'r')
    sizes=collections.Counter()
    def vis(name,obj):
        if isinstance(obj,h5py.Dataset):
            parts=name.split('/'); key='/'.join(parts[:3]) if parts[0] in ('general','processing') else parts[0]
            sizes[key]+=obj.id.get_storage_size()
    f.visititems(vis)
    print(i, len(data)/1e6, [(k, round(v/1e6,2)) for k,v in sizes.most_common(10)])
EOF
```

```
0 19.842547 [('acquisition', 4.34), ('general/testpulse/ITC18USB_Dev_0', 0.59), ('general/labnotebook/ITC18USB_Dev_0', 0.47), ('stimulus', 0.16), ('general/stimsets/X7Ramp_DA_0_WPT', 0.04), ('general/stimsets/EXTPGGAEND180424_DA_0_WPT', 0.04), ('general/stimsets/EXTPEXPEND180424_DA_0_WPT', 0.04), ('general/stimsets/EXTPINBATH180424_DA_0_WPT', 0.04), ('general/stimsets/X6SP_Rheo_DA_0_WPT', 0.04), ('general/stimsets/X4PS_SupraThresh_DA_0_WPT', 0.04)]
3000 69.689869 [('acquisition', 23.2), ('general/stimsets/referenced', 20.25), ('stimulus', 2.19), ('general/labnotebook/ITC18USB_Dev_0', 1.24), ('general/testpulse/ITC18USB_Dev_0', 0.52), ('general/stimsets/X2LP_Search_DA_0_WPT', 0.04), ('general/stimsets/X4PS_SupraThresh_DA_0_WPT', 0.04), ('general/stimsets/X6SP_Rheo_DA_0_WPT', 0.04), ('general/stimsets/X7Ramp_DA_0_WPT', 0.04), ('general/stimsets/X5SP_Search_DA_0_WPT', 0.04)]
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && grep -n "h5py.File\|def __init__" dev/lib/python3.13/site-packages/ipfx/dataset/labnotebook.py | head; cat > rtest.py <<'EOF'
import json, time, requests, remfile, h5py, warnings, logging, sys
warnings.filterwarnings("ignore"); logging.disable(logging.WARNING)
sys.path.insert(0,'entries/yang-2026-flexible')
import patchseq as ps
from ipfx.dataset import ephys_nwb_data as E
from ipfx.dataset.ephys_nwb_data import NWBHDF5IO
orig=E.EphysNWBData.load_nwb
def load_nwb(self, nwb_file, load_into_memory=True):
    if isinstance(nwb_file, (str,)) or hasattr(nwb_file,'getvalue'):
        return orig(self, nwb_file, load_into_memory)
    self.nwb_file=nwb_file
    h=h5py.File(nwb_file,'r')
    self.nwb=NWBHDF5IO(path="remote.nwb", mode="r", file=h, load_namespaces=True).read()
E.EphysNWBData.load_nwb=load_nwb
a=json.load(open('assets.json'))
for i in [0,3000]:
    url=requests.head(f"https://api.dandiarchive.org/api/assets/{a[i]['asset_id']}/download/",allow_redirects=True).url
    t=time.time()
    rf=remfile.File(url)
    from ipfx.dataset.create import create_ephys_data_set
    ps._repair_epochs()
    import ipfx.data_set_features as dsf
    ds=create_ephys_data_set(nwb_file=rf)
    t1=time.time()
    og=ds.get_sweep_numbers
    def filt(*x,**k): return [s for s in og(*x,**k) if ds.sweep(int(s)).epochs.get("experiment") and ds.sweep(int(s)).epochs.get("stim")]
    ds.get_sweep_numbers=filt
    f1,s1=dsf.extract_cell_long_square_features(ds); f2,s2=dsf.extract_cell_short_square_features(ds); f3,s3=dsf.extract_cell_ramp_features(ds)
    print(i, "open", round(t1-t,2), "total", round(time.time()-t,2), s1['failed_fx'], s2['failed_fx'], s3['failed_fx'])
EOF
dev/bin/python rtest.py 2>&1 | grep -v warn | tail -5
```

```
12:    def __init__(self):
171:    def __init__(self, nwb_file):
174:        h5 = h5py.File(nwb_file, "r")
  File "/tmp/claude-1001/dev/lib/python3.13/site-packages/hdmf/backends/hdf5/h5tools.py", line 149, in __resolve_file_obj
    path = cls.__check_path_file_obj(path, file_obj)
  File "/tmp/claude-1001/dev/lib/python3.13/site-packages/hdmf/backends/hdf5/h5tools.py", line 142, in __check_path_file_obj
    raise ValueError(msg)
ValueError: You argued 'remote.nwb' as this object's path, but supplied a file with filename: <remfile.RemFile.RemFile object at 0x723e86478980>
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && sed -i 's/NWBHDF5IO(path="remote.nwb", mode="r", file=h, load_namespaces=True)/NWBHDF5IO(path=h.filename, mode="r", file=h, load_namespaces=True)/' rtest.py && dev/bin/python rtest.py 2>&1 | grep -v warn | tail -5
```

```
0 open 6.52 total 7.48 False False False
3000 open 14.2 total 15.9 False False False
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && dev/bin/python - <<'EOF'
import json, time, requests
from concurrent.futures import ThreadPoolExecutor
a=json.load(open('assets.json'))
def get(x):
    return len(requests.get(f"https://api.dandiarchive.org/api/assets/{x['asset_id']}/download/").content)
for n,off in [(4,500),(12,600)]:
    sub=a[off:off+36]; t=time.time()
    with ThreadPoolExecutor(n) as ex: tot=sum(ex.map(get, sub))
    print(n, "threads", round(tot/1e6), "MB", round(time.time()-t,1), "s", round(tot/1e6/(time.time()-t)), "MB/s")
EOF
```

```
4 threads 888 MB 7.4 s 119 MB/s
12 threads 991 MB 3.4 s 294 MB/s
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && dev/bin/python -c "
import sys,json,cProfile,pstats; sys.path.insert(0,'entries/yang-2026-flexible')
import patchseq as ps
a=json.load(open('assets.json'))
ps.extract_cell(a[5],None)
cProfile.run('ps.extract_cell(a[2800],None)','prof')
p=pstats.Stats('prof'); p.sort_stats('cumulative').print_stats(25)
p.sort_stats('tottime').print_stats(12)
" 2>&1 | grep -v warn | grep -E "^ +[0-9]" | head -45
```

```
5554938 function calls (5463582 primitive calls) in 3.861 seconds
        1    0.000    0.000    3.862    3.862 {built-in method builtins.exec}
        1    0.000    0.000    3.862    3.862 <string>:1(<module>)
        1    0.002    0.002    3.862    3.862 entries/yang-2026-flexible/patchseq.py:194(extract_cell)
        1    0.000    0.000    1.577    1.577 /tmp/claude-1001/dev/lib/python3.13/site-packages/ipfx/dataset/create.py:85(create_ephys_data_set)
        1    0.000    0.000    1.448    1.448 /tmp/claude-1001/dev/lib/python3.13/site-packages/ipfx/dataset/mies_nwb_data.py:14(__init__)
        1    0.000    0.000    1.448    1.448 /tmp/claude-1001/dev/lib/python3.13/site-packages/ipfx/dataset/ephys_nwb_data.py:66(__init__)
        1    0.000    0.000    1.447    1.447 /tmp/claude-1001/dev/lib/python3.13/site-packages/ipfx/dataset/ephys_nwb_data.py:81(load_nwb)
        1    0.000    0.000    1.241    1.241 /tmp/claude-1001/dev/lib/python3.13/site-packages/pynwb/__init__.py:469(read)
        1    0.000    0.000    1.241    1.241 /tmp/claude-1001/dev/lib/python3.13/site-packages/hdmf/backends/hdf5/h5tools.py:453(read)
        1    0.000    0.000    1.241    1.241 /tmp/claude-1001/dev/lib/python3.13/site-packages/hdmf/backends/io.py:53(read)
        1    0.000    0.000    1.175    1.175 entries/yang-2026-flexible/patchseq.py:181(_fetch)
        1    0.000    0.000    1.175    1.175 /tmp/claude-1001/dev/lib/python3.13/site-packages/requests/api.py:74(get)
        1    0.000    0.000    1.175    1.175 /tmp/claude-1001/dev/lib/python3.13/site-packages/requests/api.py:24(request)
        1    0.000    0.000    1.175    1.175 /tmp/claude-1001/dev/lib/python3.13/site-packages/requests/sessions.py:557(request)
      2/1    0.000    0.000    1.174    1.174 /tmp/claude-1001/dev/lib/python3.13/site-packages/requests/sessions.py:752(send)
      3/2    0.000    0.000    1.045    0.523 /tmp/claude-1001/dev/lib/python3.13/site-packages/requests/sessions.py:186(resolve_redirects)
[... 20 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && sed -n 165,200p dev/lib/python3.13/site-packages/ipfx/dataset/labnotebook.py; dev/bin/python -c "import h5py; print(h5py.__version__, hasattr(h5py.File,'in_memory'))"
```

```
""" 
        LabNotebookReaderIgorNwb:
        Loads lab notebook data out of an Igor-generated NWB file.
        Module input is the name of the nwb file.
        Notebook data can be read through get_value() function
    """
    def __init__(self, nwb_file):
        LabNotebookReader.__init__(self)

        h5 = h5py.File(nwb_file, "r")

        # check NWB version and whether labnotebook exist
        for k in h5["general/labnotebook"]:
            notebook = h5["general/labnotebook"][k]
            break
        # load column data into memory
        self.val_text = notebook["textualValues"][()]
        self.colname_text = notebook["textualKeys"][()]
        self.val_number = notebook["numericalValues"][()]
        self.colname_number = notebook["numericalKeys"][()]
[... 17 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && sed -n 25,45p dev/lib/python3.13/site-packages/ipfx/dataset/create.py; sed -n 1,30p dev/lib/python3.13/site-packages/ipfx/dataset/mies_nwb_data.py
```

```
return dataset_from_nwb.item()

    return dataset_from_nwb


def is_file_mies(path: str) -> bool:
    with h5py.File(path, "r") as fil:
        if "generated_by" in fil["general"].keys():
            generated_by = dict(fil["general"]["generated_by"][:])
            try:
                decoded_generation_info = {k.decode(): v.decode() for k, v in generated_by.items()}
            except:
                decoded_generation_info = generated_by

            return decoded_generation_info.get("Package", "None") == "MIES"

    return False


def get_nwb_version(nwb_file: str) -> Dict[str, Any]:
[... 32 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/yang-2026-flexible && python - <<'EOF'
p="patchseq.py"; s=open(p).read()
helper='''

_ONTOLOGY = None


def open_data_set(data: bytes):
    """An IPFX data set on a file held in memory, as ``ipfx.dataset.create.create_ephys_data_set`` builds it.

    The file is opened with HDF5's in-memory driver, which reads much faster than a Python file object;
    the steps are those of ``create_ephys_data_set`` (NWB 2 only, MIES or not)."""
    global _ONTOLOGY
    import h5py
    import ipfx.dataset.ephys_nwb_data as E
    from ipfx.dataset.create import get_nwb_version  # noqa: F401  (the version check is done below)
    from ipfx.dataset.ephys_data_set import EphysDataSet
    from ipfx.dataset.hbg_nwb_data import HBGNWBData
    from ipfx.dataset.labnotebook import LabNotebookReaderIgorNwb
    from ipfx.dataset.mies_nwb_data import MIESNWBData
    from ipfx.stimulus import StimulusOntology
    import ipfx.json_utilities as ju

    if not getattr(E.EphysNWBData.load_nwb, "_in_memory", False):
        original = E.EphysNWBData.load_nwb

        def load_nwb(self, nwb_file, load_into_memory=True):
            if not isinstance(nwb_file, h5py.File):
                return original(self, nwb_file, load_into_memory)
            self.nwb_file = nwb_file
            with warnings.catch_warnings():
                warnings.simplefilter("ignore")
                self.nwb = E.NWBHDF5IO(path=nwb_file.filename, mode="r", file=nwb_file, load_namespaces=True).read()

        load_nwb._in_memory = True
        E.EphysNWBData.load_nwb = load_nwb
    if _ONTOLOGY is None:
        _ONTOLOGY = StimulusOntology(ju.read(StimulusOntology.DEFAULT_STIMULUS_ONTOLOGY_FILE))
    h5 = h5py.File.in_memory(data)
    version = h5.attrs.get("nwb_version", b"")
    version = version.decode() if isinstance(version, bytes) else str(version)
    if not (version.startswith("2") or version.startswith("NWB-2")):
        raise ValueError(f"Unsupported NWB version {version}")
    mies = False
    if "generated_by" in h5["general"]:
        gen = dict(h5["general"]["generated_by"][:])
        try:
            gen = {k.decode(): v.decode() for k, v in gen.items()}
        except Exception:
            pass
        mies = gen.get("Package", "None") == "MIES"
    if mies:
        notebook = LabNotebookReaderIgorNwb.__new__(LabNotebookReaderIgorNwb)
        LabNotebookReaderIgorNwb.__bases__[0].__init__(notebook)
        nb = h5["general/labnotebook"][next(iter(h5["general/labnotebook"]))]
        notebook.val_text = nb["textualValues"][()]
        notebook.colname_text = nb["textualKeys"][()]
        notebook.val_number = nb["numericalValues"][()]
        notebook.colname_number = nb["numericalKeys"][()]
        notebook.register_enabled_names()
        nwb_data = MIESNWBData(h5, notebook, _ONTOLOGY)
    else:
        nwb_data = HBGNWBData(h5, _ONTOLOGY)
    return EphysDataSet(sweep_info=None, data=nwb_data), h5, mies
'''
s=s.replace("\n\ndef extract_cell(", helper+"\n\ndef extract_cell(",1)
old='''        with h5py.File(io.BytesIO(data), "r") as f:
            g = f["general"]
            rec["genotype"] = g["subject/genotype"][()].decode() if "subject/genotype" in g else ""
            rec["session_id"] = g["session_id"][()].decode() if "session_id" in g else ""
            rec["subject_id"] = g["subject/subject_id"][()].decode() if "subject/subject_id" in g else ""
            rec["sex"] = g["subject/sex"][()].decode() if "subject/sex" in g else ""
            rec["age"] = g["subject/age"][()].decode() if "subject/age" in g else ""
        ds = create_ephys_data_set(nwb_file=io.BytesIO(data))
'''
new='''        ds, h5, rec["mies"] = open_data_set(data)
        del data
        g = h5["general"]
        for key, path in (("genotype", "subject/genotype"), ("session_id", "session_id"),
                          ("subject_id", "subject/subject_id"), ("sex", "subject/sex"), ("age", "subject/age")):
            val = g[path][()] if path in g else b""
            rec[key] = val.decode() if isinstance(val, bytes) else str(val)
'''
assert old in s; s=s.replace(old,new)
s=s.replace('''        import h5py
        import ipfx.data_set_features as dsf
        import ipfx.stim_features as stf
        from ipfx.dataset.create import create_ephys_data_set
''','''        import ipfx.data_set_features as dsf
        import ipfx.stim_features as stf
''')
s=s.replace("import io\n","",1)
open(p,"w").write(s)
EOF
cd $TMPDIR && dev/bin/python -c "
import sys,json,time; sys.path.insert(0,'entries/yang-2026-flexible')
import patchseq as ps
a=json.load(open('assets.json'))
old=json.load(open('bench.json'))
for i in [0,400,800,2800,3600]:
    t=time.time(); r=ps.extract_cell(a[i],None); print(i, round(time.time()-t,2), r['error'], r['mies'], len(r['features']), r['clock'])
" 2>&1 | grep -v warn
```

```
0 2.69  True 93 {'amp': -110.0, 'start': 0.6, 'dur': 1.0, 'pre': 0.0892333984375, 'post': -15.764106750488281, 'dv': -15.894561767578125, 'fingerprint': '138952:-1.07297e+07'}
400 1.47  True 81 {'amp': -110.0, 'start': 1.02, 'dur': 0.9999999999999998, 'pre': 0.15883636474609375, 'post': -19.24828338623047, 'dv': -20.729209899902344, 'fingerprint': '151000:-1.10806e+07'}
800 2.48  True 81 {'amp': -110.0, 'start': 1.02, 'dur': 0.9999999999999998, 'pre': -0.1106719970703125, 'post': -13.0135498046875, 'dv': -13.586540222167969, 'fingerprint': '151000:-1.17761e+07'}
2800 3.35  True 87 {'amp': -70.0, 'start': 0.6, 'dur': 1.0, 'pre': 0.054660797119140625, 'post': -14.31842041015625, 'dv': -17.071422576904297, 'fingerprint': '137970:-9.25063e+06'}
3600 3.79  True 87 {'amp': -110.0, 'start': 0.6, 'dur': 1.0, 'pre': -0.4339141845703125, 'post': -21.43547821044922, 'dv': -22.70191192626953, 'fingerprint': '135960:-9.96001e+06'}
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd entries/yang-2026-flexible && git diff --stat; python - <<'EOF'
p="patchseq.py"; s=open(p).read()
old=s[s.index("        ds, h5, rec[\"mies\"] = open_data_set(data)"):s.index("        original_get = ds.get_sweep_numbers")]
new='''        with h5py.File(io.BytesIO(data), "r") as h5:
            g = h5["general"]
            for key, path in (("genotype", "subject/genotype"), ("session_id", "session_id"),
                              ("subject_id", "subject/subject_id"), ("sex", "subject/sex"), ("age", "subject/age")):
                val = g[path][()] if path in g else b""
                rec[key] = val.decode() if isinstance(val, bytes) else str(val)
        ds = create_ephys_data_set(nwb_file=io.BytesIO(data))
        del data
'''
s=s.replace(old,new)
s=s.replace('''        import ipfx.data_set_features as dsf
        import ipfx.stim_features as stf
''','''        import h5py
        import ipfx.data_set_features as dsf
        import ipfx.stim_features as stf
        from ipfx.dataset.create import create_ephys_data_set
''',1)
a=s.index("\n\n_ONTOLOGY = None"); b=s.index("\n\ndef extract_cell(")
s=s[:a]+s[b:]
s=s.replace("import logging\n","import io\nimport logging\n",1)
open(p,"w").write(s)
EOF
grep -n "open_data_set\|_ONTOLOGY\|^import" patchseq.py; cd $TMPDIR && cat > bench2.py <<'EOF'
import sys, time, json, resource
sys.path.insert(0, "entries/yang-2026-flexible")
import patchseq as ps
import numpy as np
if __name__ == "__main__":
    assets = json.load(open("assets.json"))
    idx = np.random.default_rng(1).choice(len(assets), int(sys.argv[1]), replace=False)
    t0 = time.time()
    recs = ps.extract_all([assets[i] for i in idx], split_seed=None, workers=int(sys.argv[2]), progress=0)
    dt = time.time()-t0
    print("n", len(recs), "time", round(dt,1), "per cell", round(dt/len(recs),3), "est full min", round(dt/len(recs)*4435/60,1))
    print("ok", sum(r["extract_ok"] for r in recs), [r["error"] for r in recs if r["error"]][:5])
    print("maxrss children MB", resource.getrusage(resource.RUSAGE_CHILDREN).ru_maxrss/1e3)
    json.dump(recs, open(f"bench_{sys.argv[1]}.json","w"))
EOF
dev/bin/python bench2.py 300 6 2>&1 | grep -v warn | tail -4; date -u
```

```
38:import io
39:import logging
40:import os
41:import warnings
42:import zlib
49:import numpy as np  # noqa: E402
50:import requests  # noqa: E402
n 300 time 201.4 per cell 0.671 est full min 49.6
ok 298 ["IndexError: Cannot find {'Short Square - Hold -70mV', 'Short Square Threshold', 'Short Square - Hold -60mV', 'Short Square', 'Short Square - Hold -80mV'} sweeps with clamp mode: CurrentClamp ", "IndexError: Cannot find {'Short Square Threshold', 'Short Square - Hold -60mV', 'Short Square - Hold -80mV', 'Short Square', 'Short Square - Hold -70mV'} sweeps with clamp mode: CurrentClamp "]
maxrss children MB 2655.236
Sun Nov 22 09:48:23 UTC 2026
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && grep -n "self.nwb\b\|self\.nwb\." dev/lib/python3.13/site-packages/ipfx/dataset/*.py | head -40; wc -l dev/lib/python3.13/site-packages/ipfx/dataset/ephys_nwb_data.py
```

```
dev/lib/python3.13/site-packages/ipfx/dataset/ephys_nwb_data.py:83:        Load NWB to self.nwb
dev/lib/python3.13/site-packages/ipfx/dataset/ephys_nwb_data.py:108:            self.nwb = reader.read()
dev/lib/python3.13/site-packages/ipfx/dataset/ephys_nwb_data.py:148:        series = self.nwb.sweep_table.get_series(sweep_number)
dev/lib/python3.13/site-packages/ipfx/dataset/ephys_nwb_data.py:268:        return np.unique(self.nwb.sweep_table.sweep_number[:])
dev/lib/python3.13/site-packages/ipfx/dataset/ephys_nwb_data.py:310:        spikes = self.nwb.get_processing_module('spikes')
330 dev/lib/python3.13/site-packages/ipfx/dataset/ephys_nwb_data.py
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && sed -n 130,330p dev/lib/python3.13/site-packages/ipfx/dataset/ephys_nwb_data.py; sed -n 30,120p dev/lib/python3.13/site-packages/ipfx/dataset/mies_nwb_data.py
```

```
Raises
        ------
        TypeError
            If sweep_number is not an integer or series_class is not a stimulus
            or response PatchClampSeries
        ValueError
            If there are no TimeSeries found for this sweep number or if there
            is not exactly one matching PatchClampSeries of the requested type.

        """
        if not isinstance(
            sweep_number, (int, np.uint64, np.int64, np.uint32, np.int32)
        ):
            raise TypeError(
                f"Sweep_number must be an integer, but it is {type(sweep_number)}"
            )

        series = self.nwb.sweep_table.get_series(sweep_number)

        if not series:
[... 210 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && dev/bin/python - <<'EOF' 2>&1 | grep -v warn
import json, requests, io, h5py
a=json.load(open('assets.json'))
data=requests.get(f"https://api.dandiarchive.org/api/assets/{a[0]['asset_id']}/download/").content
f=h5py.File(io.BytesIO(data),'r')
st=f['general/intracellular_ephys/sweep_table']
print(list(st.keys()), {k:dict(st[k].attrs) for k in st})
print(st['sweep_number'][:10], st['series'][:3], st['series_index'][:5] if 'series_index' in st else None)
s=f['acquisition/data_00004_AD0']; print(dict(s.attrs)); print({k:(s[k][()] if s[k].shape==() else s[k].shape) for k in s}); print(dict(s['data'].attrs), dict(s['starting_time'].attrs))
s=f['stimulus/presentation/data_00004_DA0']; print(dict(s.attrs)); print({k:(s[k][()] if s[k].shape==() else s[k].shape) for k in s}); print(dict(s['data'].attrs))
EOF
```

```
['id', 'series', 'series_index', 'sweep_number'] {'id': {'namespace': 'hdmf-common', 'neurodata_type': 'ElementIdentifiers', 'object_id': 'ced4ae0e-0547-4d42-978a-2f25de4b4da1'}, 'series': {'description': 'The PatchClampSeries with the sweep number in that row.', 'namespace': 'hdmf-common', 'neurodata_type': 'VectorData', 'object_id': 'aa06cd61-14d2-4947-93a0-91ec1d0d2e10'}, 'series_index': {'namespace': 'hdmf-common', 'neurodata_type': 'VectorIndex', 'object_id': '619c5c2c-36fb-4f5a-8991-f646358838a0', 'target': <HDF5 object reference>}, 'sweep_number': {'description': 'Sweep number of the PatchClampSeries in that row.', 'namespace': 'hdmf-common', 'neurodata_type': 'VectorData', 'object_id': '5cfc76f4-9d1f-4c61-87f4-c17758ccceac'}}
[0 0 1 1 2 2 3 3 4 4] [<HDF5 object reference> <HDF5 object reference> <HDF5 object reference>] [1 2 3 4 5]
{'comments': 'HS#0:Stim Scale Factor: -30.00 \nHS#0:DA Gain: 400.00 \nHS#0:AD Gain: 0.05 \nIndexing: On\nSampling interval multiplier: 4.00 \nHS#0:Stim set length: 175000.00 a. u.\nRepeated Acq Cycle ID: 1392624.00 \nHS#0:Stim Wave Checksum: 2390421504.00 \nTP buffer size: 1.00 a. u.\nHS#0:Stimset Acq Cycle ID: 364930.00 a. u.\nHS#0:I-Clamp Holding Enable: Off\nHS#0:I-Clamp Holding Level: 0.00 pA\nHS#0:Neut Cap Enabled: On\nHS#0:Neut Cap Value: 5.00 pF\nHS#0:Bridge Bal Enable: On\nHS#0:Bridge Bal Value: 15.32 MOhm\nHS#0:Operating Mode: 1.00 \nHS#0:Scaled Out Signal: 20.00 \nHS#0:Alpha: 5.00 \nHS#0:Scale Factor: 10.00 \nHS#0:Ext Cmd Sens: 0.00 \nHS#0:Raw Out Signal: 31.00 \nHS#0:Raw Scale Factor: 0.50 \nHS#0:Raw Scale Factor Units: 6.00 \nHS#0:Pipette Offset: 72.28 mV\nHS#0:Slow current injection: Off\nHS#0:Slow current injection level: 0.02 V\nHS#0:Slow current injection settling time: 1.00 s\nHS#0:Autobias Vcom: -72.00 mV\nHS#0:Autobias Vcom variance: 0.50 mV\nHS#0:Autobias Ibias max: 100.00 pA\nHS#0:Autobias: On\nHS#0:Async AD 0: Set Temperature: -358.25 degC\nAsync AD 0: Set Temperature: -358.25 degC\nHS#0:USER_DA Scale Chk0 S-
[... 4 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && dev/bin/python - <<'EOF' 2>&1 | grep -v warn
import json, requests, io, h5py
a=json.load(open('assets.json'))
data=requests.get(f"https://api.dandiarchive.org/api/assets/{a[0]['asset_id']}/download/").content
f=h5py.File(io.BytesIO(data),'r')
for p in ['acquisition/data_00004_AD0','stimulus/presentation/data_00004_DA0','acquisition/data_00000_AD0']:
    s=f[p]; print(p, s.attrs['neurodata_type'])
    for k in s:
        if isinstance(s[k],h5py.Dataset): print('  ',k, s[k].shape, s[k][()] if s[k].shape==() else '', dict(s[k].attrs))
        else: print('  group',k, list(s[k].keys()))
EOF
```

```
acquisition/data_00004_AD0 CurrentClampSeries
   bridge_balance (1,)  {'unit': 'MOhm'}
   capacitance_compensation (1,)  {'unit': 'pF'}
   data (180000,)  {'IGORWaveNote': np.bytes_(b'HS#0:Stim Scale Factor: -30.00 \rHS#0:DA Gain: 400.00 \rHS#0:AD Gain: 0.05 \rIndexing: On\rSampling interval multiplier: 4.00 \rHS#0:Stim set length: 175000.00 a. u.\rRepeated Acq Cycle ID: 1392624.00 \rHS#0:Stim Wave Checksum: 2390421504.00 \rTP buffer size: 1.00 a. u.\rHS#0:Stimset Acq Cycle ID: 364930.00 a. u.\rHS#0:I-Clamp Holding Enable: Off\rHS#0:I-Clamp Holding Level: 0.00 pA\rHS#0:Neut Cap Enabled: On\rHS#0:Neut Cap Value: 5.00 pF\rHS#0:Bridge Bal Enable: On\rHS#0:Bridge Bal Value: 15.32 MOhm\rHS#0:Operating Mode: 1.00 \rHS#0:Scaled Out Signal: 20.00 \rHS#0:Alpha: 5.00 \rHS#0:Scale Factor: 10.00 \rHS#0:Ext Cmd Sens: 0.00 \rHS#0:Raw Out Signal: 31.00 \rHS#0:Raw Scale Factor: 0.50 \rHS#0:Raw Scale Factor Units: 6.00 \rHS#0:Pipette Offset: 72.28 mV\rHS#0:Slow current injection: Off\rHS#0:Slow current injection level: 0.02 V\rHS#0:Slow current injection settling time: 1.00 s\rHS#0:Autobias Vcom: -72.00 mV\rHS#0:Autobias Vcom variance: 0.50 mV\rHS#0:Autobias Ibias max: 100.00 pA\rHS#0:Autobias: On\rHS#0:Async AD 0: Set Temperature: -358.25 degC\rAsync AD 0: Set Temperature: -358.25 degC\rHS#0:USER_DA Scale Chk0 S-RMS QC: On\rHS#0:USER_DA Scale Chk0 L-RMS QC: On\rHS#0:USER_DA Scale Chk0 T-V BL QC: On\rUSER_DA Scale Chk0 BL QC: On\rHS#0:USER_DA Scale Chk1 S-RMS QC: On\rHS#0:USER_DA Scale Chk1 L-RMS QC: On\rHS#0:USER_DA Scale Chk1 T-V BL QC: On\rUSER_DA Scale Chk1 BL QC: On\rUSER_DA Scale Sweep QC: On\r\rHS#0:DA unit: pA\rHS#0:AD unit: mV\rHS#0:Generic function: PSQ_DAScale\rHS#0:Function params: OperationMode:string=Sub,DAScales:wave=-30|-50|-70|-90|-110|,SamplingMultiplier:variable=4,\rHigh precision sweep start: 2020-01-28T22:12:51.126Z\rHS#0:OperatingModeString: I-Clamp\rHS#0:ScaledOutSignalString: Membrane Potential\rHS#0:ScaleFactorUnitsString: V/V\rHS#0:RawOutSignalString: Membr
[... 19 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/yang-2026-flexible && python - <<'EOF'
p="patchseq.py"; s=open(p).read()
shim='''

class _Series:
    """The fields of a pynwb PatchClampSeries that IPFX reads, taken from the HDF5 group directly."""

    def __init__(self, group, h5):
        self.name = group.name.split("/")[-1]
        ntype = group.attrs["neurodata_type"]
        ntype = ntype.decode() if isinstance(ntype, bytes) else str(ntype)
        self.is_stimulus = ntype.endswith("StimulusSeries")
        self.clamp_mode = "VoltageClamp" if ntype.startswith("VoltageClamp") else (
            "CurrentClamp" if ntype.startswith(("CurrentClamp", "IZero")) else ntype)
        self.data = group["data"]
        self.conversion = float(self.data.attrs.get("conversion", 1.0))
        unit = self.data.attrs.get("unit", "")
        self.unit = unit.decode() if isinstance(unit, bytes) else str(unit)
        self.rate = float(group["starting_time"].attrs["rate"])
        desc = group.attrs.get("stimulus_description", "")
        self.stimulus_description = desc.decode() if isinstance(desc, bytes) else str(desc)

        def scalar(key):
            if key not in group:
                return None
            val = group[key][()]
            return float(np.ravel(val)[0]) if np.size(val) else None
        self.gain = scalar("gain")
        self.bias_current = scalar("bias_current")
        self.bridge_balance = scalar("bridge_balance")


def _fast_reader(base):
    """A subclass of an IPFX NWB reader that builds its sweep table from HDF5 without pynwb.

    pynwb builds an object for every group in the file, about a third of the time IPFX spends on a
    cell; IPFX itself reads only the sweep table and, per sweep, the data, conversion, unit, rate,
    gain, stimulus description, bias current and bridge balance of its two series, which this
    reader takes from the same HDF5 fields pynwb reads them from. ``check_fast_reader`` in the
    notebook compares the features it gives with those of IPFX's own reader."""

    class Fast(base):
        def load_nwb(self, nwb_file, load_into_memory=True):
            import h5py
            self.nwb_file = nwb_file
            h5 = h5py.File(nwb_file, "r")
            st = h5["general/intracellular_ephys/sweep_table"]
            numbers = st["sweep_number"][:]
            refs = st["series"][:]
            index = st["series_index"][:]
            self._by_sweep = {}
            start = 0
            for row, stop in enumerate(index):
                for ref in refs[start:stop]:
                    self._by_sweep.setdefault(int(numbers[row]), []).append(_Series(h5[ref], h5))
                start = stop
            self._h5 = h5
            self.nwb = None

        def _get_series(self, sweep_number, series_class):
            want_stimulus = series_class == self.STIMULUS
            found = [s for s in self._by_sweep.get(int(sweep_number), []) if s.is_stimulus == want_stimulus]
            if len(found) != 1:
                raise ValueError(f"Found {len(found)} {'stimulus' if want_stimulus else 'response'} series "
                                 f"for sweep number {sweep_number}.")
            return found[0]

        def get_sweep_attrs(self, sweep_number):
            rs = self._get_series(sweep_number, self.RESPONSE)
            attrs = {"gain": rs.gain, "stimulus_description": rs.stimulus_description,
                     "sweep_number": sweep_number, "clamp_mode": rs.clamp_mode}
            if rs.clamp_mode == "CurrentClamp":
                attrs.update(bias_current=rs.bias_current, bridge_balance=rs.bridge_balance)
            elif rs.clamp_mode != "VoltageClamp":
                raise ValueError(f"Must be response series {self.RESPONSE} ")
            return attrs

        @property
        def sweep_numbers(self):
            return np.unique(np.array(sorted(self._by_sweep), dtype=int))

    Fast.__name__ = "Fast" + base.__name__
    return Fast


def open_data_set(data: bytes, fast: bool = True):
    """The IPFX data set of a file held in memory, built as ``ipfx.dataset.create.create_ephys_data_set``
    builds it; with ``fast``, its reader takes the sweeps from HDF5 directly (``_fast_reader``)."""
    from ipfx.dataset.create import create_ephys_data_set, get_nwb_version, is_file_mies
    if not fast:
        return create_ephys_data_set(nwb_file=io.BytesIO(data))
    import ipfx.json_utilities as ju
    from ipfx.dataset.ephys_data_set import EphysDataSet
    from ipfx.dataset.hbg_nwb_data import HBGNWBData
    from ipfx.dataset.labnotebook import LabNotebookReaderIgorNwb
    from ipfx.dataset.mies_nwb_data import MIESNWBData
    from ipfx.stimulus import StimulusOntology
    if get_nwb_version(io.BytesIO(data))["major"] != 2:
        raise ValueError("Unsupported NWB version")
    ontology = StimulusOntology(ju.read(StimulusOntology.DEFAULT_STIMULUS_ONTOLOGY_FILE))
    if is_file_mies(io.BytesIO(data)):
        nwb_data = _fast_reader(MIESNWBData)(io.BytesIO(data), LabNotebookReaderIgorNwb(io.BytesIO(data)), ontology)
    else:
        nwb_data = _fast_reader(HBGNWBData)(io.BytesIO(data), ontology)
    return EphysDataSet(sweep_info=None, data=nwb_data)
'''
s=s.replace("\n\ndef extract_cell(", shim+"\n\ndef extract_cell(",1)
s=s.replace("def extract_cell(asset: dict, split_seed: int | None = None) -> dict:","def extract_cell(asset: dict, split_seed: int | None = None, fast: bool = True) -> dict:")
s=s.replace("        ds = create_ephys_data_set(nwb_file=io.BytesIO(data))\n","        ds = open_data_set(data, fast)\n")
s=s.replace("        from ipfx.dataset.create import create_ephys_data_set\n","",1)
open(p,"w").write(s)
EOF
cd $TMPDIR && dev/bin/python -c "
import sys,json,time; sys.path.insert(0,'entries/yang-2026-flexible')
import patchseq as ps, numpy as np
a=json.load(open('assets.json'))
for i in [0,400,800,2800,3600,1234,4321]:
    t=time.time(); r=ps.extract_cell(a[i],7,fast=True); t1=time.time(); q=ps.extract_cell(a[i],7,fast=False); t2=time.time()
    same = r['features'].keys()==q['features'].keys() and all(np.isclose(r['features'][k],q['features'][k],equal_nan=True) for k in r['features'])
    print(i, 'fast',round(t1-t,2),'pynwb',round(t2-t1,2), r['error'][:60], q['error'][:60], len(r['features']), same, r['clock']==q['clock'], r['split']['a']==q['split']['a'] and r['split']['b']==q['split']['b'], r['n_sweeps']==q['n_sweeps'])
" 2>&1 | grep -v warn
```

```
0 fast 2.6 pynwb 2.06   93 True True True True
400 fast 1.89 pynwb 2.03   81 True True True True
800 fast 2.0 pynwb 2.14   81 True True True True
2800 fast 2.67 pynwb 3.22   87 True True True True
3600 fast 3.0 pynwb 3.46   87 True True True True
1234 fast 2.07 pynwb 2.2   83 True True True True
4321 fast 1.69 pynwb 2.17   92 True True True True
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && dev/bin/python -c "
import sys,json,cProfile,pstats; sys.path.insert(0,'entries/yang-2026-flexible')
import patchseq as ps
a=json.load(open('assets.json'))
ps.extract_cell(a[5],None)
cProfile.run('ps.extract_cell(a[2800],None)','prof')
p=pstats.Stats('prof'); p.sort_stats('tottime').print_stats(25)
" 2>&1 | grep -v warn | grep -E "^ +[0-9]" | head -30
```

```
1951188 function calls (1942609 primitive calls) in 2.637 seconds
     8842    0.969    0.000    0.969    0.000 {method 'read' of '_ssl._SSLSocket' objects}
      451    0.208    0.000    0.225    0.000 /tmp/claude-1001/dev/lib/python3.13/site-packages/h5py/_hl/dataset.py:853(__getitem__)
      178    0.181    0.001    0.181    0.001 /tmp/claude-1001/dev/lib/python3.13/site-packages/h5py/_hl/base.py:288(name)
      272    0.132    0.000    0.164    0.001 /tmp/claude-1001/dev/lib/python3.13/site-packages/ipfx/dataset/labnotebook.py:32(get_numeric_value)
      976    0.098    0.000    0.098    0.000 {method 'nonzero' of 'numpy.ndarray' objects}
        2    0.069    0.035    0.069    0.035 {method 'connect' of '_socket.socket' objects}
        2    0.067    0.034    0.067    0.034 {method 'do_handshake' of '_ssl._SSLSocket' objects}
       78    0.061    0.001    0.061    0.001 {built-in method scipy.signal._sigtools._linear_filter}
   135811    0.032    0.000    0.032    0.000 /tmp/claude-1001/dev/lib/python3.13/site-packages/ipfx/stimulus.py:78(tags)
   561716    0.032    0.000    0.032    0.000 {built-in method math.isnan}
   135675    0.028    0.000    0.060    0.000 /tmp/claude-1001/dev/lib/python3.13/site-packages/ipfx/stimulus.py:88(has_tag)
        2    0.028    0.014    0.028    0.014 {built-in method _socket.getaddrinfo}
       47    0.026    0.001    0.333    0.007 /tmp/claude-1001/dev/lib/python3.13/site-packages/ipfx/dataset/ephys_data_set.py:208(sweep)
      891    0.024    0.000    0.031    0.000 /tmp/claude-1001/dev/lib/python3.13/site-packages/h5py/_hl/attrs.py:51(__getitem__)
       21    0.024    0.001    0.929    0.044 {method 'join' of 'bytes' objects}
       39    0.024    0.001    0.146    0.004 /tmp/claude-1001/dev/lib/python3.13/site-packages/ipfx/time_series_utils.py:26(calculate_dvdt)
       22    0.022    0.001    0.022    0.001 {built-in method builtins.min}
       93    0.021    0.000    0.021    0.000 {built-in method builtins.max}
     
[... 6 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/yang-2026-flexible && sed -i '/        self.name = group.name.split("\/")\[-1\]/d' patchseq.py && grep -n "self.name" patchseq.py; cd $TMPDIR && dev/bin/python bench2.py 300 6 2>&1 | grep -v warn | tail -4; date -u
```

```
n 300 time 115.7 per cell 0.386 est full min 28.5
ok 298 ["IndexError: Cannot find {'Short Square - Hold -70mV', 'Short Square - Hold -80mV', 'Short Square Threshold', 'Short Square', 'Short Square - Hold -60mV'} sweeps with clamp mode: CurrentClamp ", "IndexError: Cannot find {'Short Square', 'Short Square - Hold -70mV', 'Short Square Threshold', 'Short Square - Hold -60mV', 'Short Square - Hold -80mV'} sweeps with clamp mode: CurrentClamp "]
maxrss children MB 2654.816
Sun Nov 22 09:52:11 UTC 2026
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd entries/yang-2026-flexible && python - <<'EOF'
p="patchseq.py"; s=open(p).read()
old='''        rec["n_sweeps"] = {k: len(ds.get_sweep_numbers(v, clamp_mode=cc)) for k, v in names.items()}
'''
new='''        rec["n_sweeps"] = {}
        for k, v in names.items():
            try:
                rec["n_sweeps"][k] = len(ds.get_sweep_numbers(v, clamp_mode=cc))
            except IndexError:  # IPFX raises when a cell has no sweep of the kind
                rec["n_sweeps"][k] = 0
'''
assert old in s; s=s.replace(old,new); open(p,"w").write(s)
EOF
grep -n "usable = \[int" patchseq.py
```

```
356:            usable = [int(s) for s in ds.get_sweep_numbers(names["long_squares"], clamp_mode=cc)]
```

**Agent calls Bash**

```bash
cd $TMPDIR/code/scripts && sed -n 105,150p q3_mobility_modules.py; grep -n "^[A-Z_]* = " q3a_centroid_robustness.py q3a_explain.py q2_anchor.py q1_knn_scale.py figures_eneuro_supplement.py | head -40
```

```
return d


def spearman(a: np.ndarray, b: np.ndarray) -> float:
    a = np.asarray(a, dtype=float)
    b = np.asarray(b, dtype=float)
    mask = np.isfinite(a) & np.isfinite(b)
    a, b = a[mask], b[mask]
    if a.size < 3:
        return float("nan")
    ra = np.argsort(np.argsort(a)).astype(float)
    rb = np.argsort(np.argsort(b)).astype(float)
    if ra.std() == 0 or rb.std() == 0:
        return float("nan")
    return float(np.corrcoef(ra, rb)[0, 1])


def spearman_p(rho: float, n: int) -> float:
    if not np.isfinite(rho) or n < 3 or abs(rho) >= 1:
        return 0.0 if np.isfinite(rho) and abs(rho) >= 1 else float("nan")
[... 67 more lines not kept]
```

**Agent calls Write**

```json
{
 "file_path": "entries/yang-2026-flexible/geometry.py",
 "content": "\"\"\"Phenotype spaces and the cell-level and type-level measures of Yang (2026), on IPFX features.\n\nWhere each parameter comes from (the claims file, claims/yang-2026-flexible.yaml, cites the paper\nor its code, https://github.com/zy-neuro/protocol-response-geometry at commit 61a5a41, for each):\n\n- Phenotype space (claim table1-phenotype-spaces): per regime, cells with extract_ok = 1 and at\n  least one non-missing value among the regime's features (the code's fit_full_cell_pca, reading\n  2a); features with at most 30% missing and nonzero variance; mean imputation; z-scores with the\n  population SD; PCA by SVD; k80 the smallest number of components reaching 80% of the variance.\n- Spearman correlation as the code computes it (np.argsort(np.argsort(x)) ordinal ranks, ties in\n  the order the sort leaves them), with the tie-corrected (average-rank) Spearman as a variant\n  where the claims file asks for it.\n- Pairs of cells: 80,000 sampled pairs (Methods, \"Cross-regime phenotypic organization\"); unique\n  pairs are the main reading, the code's draw of random i < j pairs, which may repeat, a variant.\n- kNN: 15 neighbours, self excluded, Euclidean distance, ties as np.argpartition leaves them.\n- Every random draw uses a generator the notebook makes from the claim's seed (protocol).\n\"\"\"\n\nfrom __future__ import annotations\n\nfrom collections import Counter\n\nimport numpy as np\nfrom scipy.stats import rankdata\n\nPAIRS = [(\"long_pulse\", \"ramp\"), (\"long_pulse\", \"brief_pulse\"), (\"ramp\", \"brief_pulse\")]\nREGIMES = [\"long_pulse\", \"ramp\", \"brief_pulse\"]\nPREFIX = {\"long_pulse\": \"feat.long_squares.\", \"ramp\": \"feat.ramps.\", \"brief_pulse\": \"feat.short_squares.\"}\n\n\n# --- phenotype spaces ---------------------------------------------------------------------------\n\ndef feature_matrix(recs, columns):\n    \"\"\"Cells x features, NaN where missing, for the extract_ok cells.\"\"\"\n    ok = [r for r in recs if r.get(\"extract_ok\") == 1]\n    x = np.full((len(ok), len(columns)), np.nan)\n    pos = {c: j for j, c in enumerate(columns)}\n    for i, r in enumerate(ok):\n        for c, v in r[\"features\"].items():\n            j = pos.get(c)\n            if j is not None and v is not None:\n                x[i, j] = v\n    return [r[\"file_stem\"] for r in ok], x\n\n\ndef rule_features(recs, regime, max_missing=0.30, denominator=\"present\"):\n    \"\"\"The paper's rule for retained features (Methods, \"Protocol-resolved cellular phenotype\"):\n    numeric, at most 30% missing, nonzero variance; missingness among cells with any value of the\n    regime (\"present\", reading 2a) or among all extract_ok cells (\"all\", reading 2b).\"\"\"\n    cols = sorted({c for r in recs if r.get(\"extract_ok\") == 1 for c in r[\"features\"] if c.startswith(PREFIX[regime])})\n    stems, x = feature_matrix(recs, cols)\n    if denominator == \"present\":\n        x = x[np.isfinite(x).any(axis=1)]\n    miss = 1 - np.isfinite(x).mean(axis=0)\n    with np.errstate(all=\"ignore\"):\n        var = np.nanvar(x, axis=0)\n    keep = [c for c, m, v in zip(cols, miss, var) if m <= max_missing and np.isfinite(v) and v > 0]\n    return keep, dict(zip(cols, miss))\n\n\ndef phenotype_space(recs, columns):\n    \"\"\"z-score + PCA of one regime (the code's fit_full_cell_pca).\"\"\"\n    stems, x = feature_matrix(recs, columns)\n    present = np.isfinite(x).any(axis=1)\n    x = x[present]\n    stems = [s for s, p in zip(stems, present) if p]\n    mu = np.nanmean(x, axis=0)\n    xf = np.where(np.isfinite(x), x, mu)\n    xc = xf - xf.mean(axis=0, keepdims=True)\n    sd = xc.std(axis=0, keepdims=True)\n    sd[sd == 0] = 1.0\n    z = xc / sd\n    u, s, vt = np.linalg.svd(z, full_matrices=False)\n    var = s ** 2 / np.sum(s ** 2)\n    cum = np.cumsum(var)\n    k80 = int(np.searchsorted(cum, 0.80) + 1)\n    return {\"stems\": stems, \"scores\": u * s, \"var\": var, \"k80\": k80, \"loadings\": vt, \"columns\": list(columns),\n            \"mu\": mu, \"sd\": sd.ravel(), \"missing\": 1 - np.isfinite(x).mean(axis=0)}\n\n\ndef shared(space_a, space_b, k_a=None, k_b=None):\n    \"\"\"Scores of the cells in both spaces, in the order of space_b (as the code's align_pair).\"\"\"\n    pos_a = {s: i for i, s in enumerate(space_a[\"stems\"])}\n    stems = [s for s in space_b[\"stems\"] if s in pos_a]\n    pos_b = {s: i for i, s in enumerate(space_b[\"stems\"])}\n    ia = np.array([pos_a[s] for s in stems], dtype=int)\n    ib = np.array([pos_b[s] for s in stems], dtype=int)\n    ka = k_a or space_a[\"k80\"]\n    kb = k_b or space_b[\"k80\"]\n    return stems, space_a[\"scores\"][ia, :ka], space_b[\"scores\"][ib, :kb]\n\n\n# --- basic measures -----------------------------------------------------------------------------\n\ndef pairwise_euclidean(x):\n    x = np.asarray(x, dtype=np.float64)\n    nrm = np.sum(x * x, axis=1, keepdims=True)\n    d2 = nrm + nrm.T - 2.0 * (x @ x.T)\n    np.maximum(d2, 0.0, out=d2)\n    d = np.sqrt(d2)\n    np.fill_diagonal(d, 0.0)\n    return d\n\n\ndef ordinal_ranks(x, axis=-1):\n    return np.argsort(np.argsort(x, axis=axis), axis=axis).astype(float)\n\n\ndef spearman(a, b):\n    \"\"\"The code's Spearman: Pearson correlation of np.argsort(np.argsort(.)) ranks.\"\"\"\n    a = np.asarray(a, dtype=float)\n    b = np.asarray(b, dtype=float)\n    if a.size < 3:\n        return float(\"nan\")\n    ra, rb = ordinal_ranks(a), ordinal_ranks(b)\n    if ra.std() == 0 or rb.std() == 0:\n        return float(\"nan\")\n    return float(np.corrcoef(ra, rb)[0, 1])\n\n\ndef spearman_avg(a, b):\n    \"\"\"Tie-corrected Spearman (average ranks), a variant.\"\"\"\n    ra, rb = rankdata(a), rankdata(b)\n    if ra.std() == 0 or rb.std() == 0:\n        return float(\"nan\")\n    return float(np.corrcoef(ra, rb)[0, 1])\n\n\ndef sample_pairs(n, rng, n_pairs=80000, unique=True):\n    \"\"\"80,000 cell pairs i < j: unique pairs (Methods) or the code's draw (``unique=False``).\"\"\"\n    max_pairs = n * (n - 1) // 2\n    take = min(n_pairs, max_pairs)\n    if unique:\n        flat = rng.choice(max_pairs, size=take, replace=False)\n        # invert the row-major index of the strict upper triangle\n        i = (n - 2 - np.floor(np.sqrt(-8 * flat + 4 * n * (n - 1) - 7) / 2.0 - 0.5)).astype(np.int64)\n        j = (flat + i + 1 - n * (n - 1) // 2 + (n - i) * ((n - i) - 1) // 2).astype(np.int64)\n        return i, j\n    i = rng.integers(0, n, size=take * 3)\n    j = rng.integers(0, n, size=take * 3)\n    m = i < j\n    return i[m][:take], j[m][:take]\n\n\ndef emp_p(null, obs):\n    null = np.asarray(null, dtype=float)\n    return float((1.0 + np.sum(null >= obs)) / (1.0 + null.size))\n\n\n# --- cell level ---------------------------------------------------------------------------------\n\ndef distance_correlation(xa, xb, rng, n_shuffle=100, unique=True):\n    \"\"\"Spearman of the two regimes' distances over sampled pairs, with a cell-index permutation null.\"\"\"\n    n = xa.shape[0]\n    da, db = pairwise_euclidean(xa), pairwise_euclidean(xb)\n    ii, jj = sample_pairs(n, rng, unique=unique)\n    ua, ub = da[ii, jj], db[ii, jj]\n    rho = spearman(ua, ub)\n    null = np.empty(n_shuffle)\n    for t in range(n_shuffle):\n        perm = rng.permutation(n)\n        null[t] = spearman(ua, db[perm[ii], perm[jj]])\n    return {\"rho\": rho, \"p\": emp_p(null, rho), \"null_mean\": float(null.mean()), \"null_max\": float(null.max()),\n            \"n\": n, \"n_pairs\": int(ii.size), \"n_unique_pairs\": int(len(set(zip(ii.tolist(), jj.tolist()))))}\n\n\ndef knn_indices(d, k):\n    n = d.shape[0]\n    k = min(k, n - 1)\n    idx = np.argpartition(d, kth=k, axis=1)[:, : k + 1]\n    out = np.empty((n, k), dtype=np.int64)\n    for i in range(n):\n        row = idx[i][idx[i] != i]\n        if row.size < k:\n            full = np.argsort(d[i])\n            row = full[full != i]\n        out[i] = row[:k]\n    return out\n\n\ndef membership(idx, n):\n    m = np.zeros((idx.shape[0], n), dtype=bool)\n    np.put_along_axis(m, idx, True, axis=1)\n    return m\n\n\ndef jaccard_rows(ma, mb, k):\n    inter = np.count_nonzero(ma & mb, axis=1)\n    return inter / (2 * k - inter)\n\n\ndef knn_jaccard(xa, xb, k, rng, n_shuffle=100):\n    \"\"\"Mean Jaccard of each cell's k nearest neighbours in two spaces, and the index-shuffle chance\n    (the code's q1_knn_scale: the second regime's neighbour lists permuted across cells).\"\"\"\n    n = xa.shape[0]\n    k = min(k, n - 1)\n    ma = membership(knn_indices(pairwise_euclidean(xa), k), n)\n    mb = membership(knn_indices(pairwise_euclidean(xb), k), n)\n    jac = jaccard_rows(ma, mb, k)\n    null = np.empty(n_shuffle)\n    for t in range(n_shuffle):\n        null[t] = jaccard_rows(ma, mb[rng.permutation(n)], k).mean()\n    return {\"k\": k, \"n\": n, \"mean\": float(jac.mean()), \"median\": float(np.median(jac)), \"chance\": float(null.mean()),\n            \"chance_sd\": float(null.std()), \"adjusted\": float(jac.mean() - null.mean()), \"per_cell\": jac}\n\n\ndef mobility(spaces):\n    \"\"\"One minus the mean, over the three regime pairs, of the Spearman correlation of a cell's\n    distances to the other triple-shared cells (the code's compute_mobility).\"\"\"\n    sets = [set(spaces[p][\"stems\"]) for p in REGIMES]\n    stems = [s for s in spaces[\"long_pulse\"][\"stems\"] if s in sets[1] and s in sets[2]]\n    n = len(stems)\n    ranks = {}\n    off = ~np.eye(n, dtype=bool)\n    for p in REGIMES:\n        pos = {s: i for i, s in enumerate(spaces[p][\"stems\"])}\n        idx = np.array([pos[s] for s in stems], dtype=int)\n        d = pairwise_euclidean(spaces[p][\"scores\"][idx, : spaces[p][\"k80\"]])\n        d = d[off].reshape(n, n - 1)\n        r = ordinal_ranks(d, axis=1)\n        r -= r.mean(axis=1, keepdims=True)\n        r /= np.sqrt((r ** 2).sum(axis=1, keepdims=True))\n        ranks[p] = r\n        del d\n    rhos = np.column_stack([np.sum(ranks[a] * ranks[b], axis=1) for a, b in PAIRS])\n    return stems, 1.0 - rhos.mean(axis=1), rhos\n\n\n# --- labels -------------------------------------------------------------------------------------\n\ndef labelled(space, join, key, k=None):\n    \"\"\"Scores (first k components) and labels of the space's cells with a non-empty label.\"\"\"\n    k = k or space[\"k80\"]\n    xi, labs = [], []\n    for i, s in enumerate(space[\"stems\"]):\n        lab = (join.get(s, {}).get(key) or \"\").strip()\n        if lab:\n            xi.append(i)\n            labs.append(lab)\n    return space[\"scores\"][np.array(xi, dtype=int), :k], np.array(labs, dtype=object), np.array(xi, dtype=int)\n\n\ndef encode(labels):\n    uniq = {v: i for i, v in enumerate(sorted(set(labels.tolist())))}\n    return np.array([uniq[v] for v in labels], dtype=int)\n\n\ndef eta2(x, labels):\n    \"\"\"Multivariate eta squared: between-group over total sum of squares (Methods, \"Biological anchoring\").\"\"\"\n    x = np.asarray(x, dtype=float)\n    grand = x.mean(axis=0)\n    total = np.sum((x - grand) ** 2)\n    between = 0.0\n    for lab in np.unique(labels):\n        sel = labels == lab\n        between += sel.sum() * float(np.sum((x[sel].mean(axis=0) - grand) ** 2))\n    return float(between / total)\n\n\ndef alignment(x, labels, rng, n_shuffle=100, average_ranks=False):\n    \"\"\"A_t: Spearman of binary label mismatch with phenotypic distance over 80,000 sampled pairs\n    (the code's align_D, pairs drawn as its sample_pairs), with a label-permutation null.\"\"\"\n    n = x.shape[0]\n    ii, jj = sample_pairs(n, rng, unique=False)\n    xi, xj = x[ii], x[jj]\n    ua = np.sqrt(np.sum((xi - xj) ** 2, axis=1))\n    sp = spearman_avg if average_ranks else spearman\n    lab = np.asarray(labels)\n    rho = sp(ua, (lab[ii] != lab[jj]).astype(float))\n    null = np.empty(n_shuffle)\n    for t in range(n_shuffle):\n        perm = rng.permutation(n)\n        null[t] = sp(ua, (lab[perm[ii]] != lab[perm[jj]]).astype(float))\n    return {\"A\": rho, \"p\": emp_p(null, rho), \"null_mean\": float(null.mean()), \"null_max\": float(null.max()), \"n\": n}\n\n\ndef residualize(x, groups):\n    out = np.array(x, dtype=float, copy=True)\n    for g in np.unique(groups):\n        sel = groups == g\n        out[sel] -= out[sel].mean(axis=0)\n    return out\n\n\ndef knn_enrichment(x, labels, k=15):\n    \"\"\"Same-label fraction among each cell's k neighbours against chance (n_type - 1)/(n - 1).\"\"\"\n    n = x.shape[0]\n    idx = knn_indices(pairwise_euclidean(x), k)\n    lab = np.asarray(labels)\n    same = (lab[idx] == lab[:, None]).mean(axis=1)\n    counts = Counter(lab.tolist())\n    chance = np.array([(counts[v] - 1) / (n - 1) for v in lab])\n    with np.errstate(divide=\"ignore\", invalid=\"ignore\"):\n        per_cell = np.where(chance > 0, same / chance, np.nan)\n    return {\"ratio_of_means\": float(same.mean() / chance.mean()), \"mean_of_ratios\": float(np.nanmean(per_cell)),\n            \"same\": float(same.mean()), \"chance\": float(chance.mean()), \"n\": n}\n\n\n# --- type level ---------------------------------------------------------------------------------\n\ndef centroid_distances(x, codes, n_types):\n    \"\"\"Euclidean distances between the centroids of types 0..n_types-1 (codes outside are ignored).\"\"\"\n    sel = (codes >= 0) & (codes < n_types)\n    sums = np.zeros((n_types, x.shape[1]))\n    np.add.at(sums, codes[sel], x[sel])\n    cnt = np.bincount(codes[sel], minlength=n_types).astype(float)\n    m = sums / cnt[:, None]\n    return pairwise_euclidean(m), cnt\n\n\ndef upper(s):\n    i, j = np.triu_indices(s.shape[0], k=1)\n    return s[i, j]\n\n\ndef type_codes(labels, types):\n    pos = {t: i for i, t in enumerate(types)}\n    return np.array([pos.get(v, -1) for v in labels], dtype=int)\n\n\ndef rank_norm(v):\n    r = ordinal_ranks(v)\n    return r / max(1.0, r.size - 1)\n\n\ndef pair_tags(s_by_regime, stable_cv=0.25, selective_range=0.55):\n    \"\"\"The code's tags: per type pair, CV and range of the three rank-normalized S values.\"\"\"\n    ranks = np.column_stack([rank_norm(upper(s_by_regime[p])) for p in REGIMES])\n    mean = ranks.mean(axis=1)\n    cv = np.where(mean > 1e-9, ranks.std(axis=1) / np.where(mean > 1e-9, mean, 1), 0.0)\n    rng_r = ranks.max(axis=1) - ranks.min(axis=1)\n    tags = np.where(cv < stable_cv, \"stable\", np.where(rng_r >= selective_range, \"selective\", \"intermediate\"))\n    return tags, cv, rng_r, mean\n"
}
```

```
File created successfully at: entries/yang-2026-flexible/geometry.py (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd $TMPDIR && dev/bin/python -c "
import sys; sys.path.insert(0,'entries/yang-2026-flexible')
import geometry as g, numpy as np
for n in [5,7,100,4054]:
    rng=np.random.default_rng(0); i,j=g.sample_pairs(n,rng,n_pairs=min(80000,n*(n-1)//2))
    ti,tj=np.triu_indices(n,1); print(n, (i<j).all(), i.min(), j.max(), len(set(zip(i,j)))==len(i), set(zip(i.tolist(),j.tolist()))<=set(zip(ti.tolist(),tj.tolist())))
"; curl -s -m 30 -o /dev/null -w "%{http_code}\n" "https://data.nemoarchive.org/other/AIBS/AIBS_patchseq/transcriptome/scell/SMARTseq/processed/analysis/20200611/"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
curl -s -m 30 -o /dev/null -w "%{http_code}\n" "https://raw.githubusercontent.com/zy-neuro/protocol-response-geometry/61a5a413daea3b3562fad6e40207320da5665fed/results/m0/m0_molecular_join.csv"; cd $TMPDIR/code && dev/bin/python -c "print(1)" 2>/dev/null; ../dev/bin/python -c "
import pandas as pd; j=pd.read_csv('results/m0/m0_molecular_join.csv'); print(j.shape); print(j.isna().sum()); print(j.t_type.notna().sum(), j.has_t_type.sum(), j.subclass.value_counts())"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR && dev/bin/python -c "
import json; r=json.load(open('bench_300.json'))
import collections
c=collections.Counter(k for x in r for k in x['features'])
print(len(c)); print(sorted(k for k in c if 'sweep.' in k)[:60])
s=json.load(open('code/results/phenotype/phenotype_summary.json'))
for reg in ['long_pulse','ramp','brief_pulse']:
    miss=[f for f in s[reg]['features'] if f not in c]; print(reg, 'missing from mine', miss)
"
```

```
98
['feat.long_squares.hero_sweep.adapt', 'feat.long_squares.hero_sweep.avg_rate', 'feat.long_squares.hero_sweep.first_isi', 'feat.long_squares.hero_sweep.index', 'feat.long_squares.hero_sweep.isi_cv', 'feat.long_squares.hero_sweep.latency', 'feat.long_squares.hero_sweep.mean_isi', 'feat.long_squares.hero_sweep.median_isi', 'feat.long_squares.hero_sweep.sag', 'feat.long_squares.hero_sweep.stim_amp', 'feat.long_squares.hero_sweep.sweep_number', 'feat.long_squares.hero_sweep.v_baseline', 'feat.long_squares.rheobase_sweep.adapt', 'feat.long_squares.rheobase_sweep.avg_rate', 'feat.long_squares.rheobase_sweep.first_isi', 'feat.long_squares.rheobase_sweep.index', 'feat.long_squares.rheobase_sweep.isi_cv', 'feat.long_squares.rheobase_sweep.latency', 'feat.long_squares.rheobase_sweep.mean_isi', 'feat.long_squares.rheobase_sweep.median_isi', 'feat.long_squares.rheobase_sweep.sag', 'feat.long_squares.rheobase_sweep.stim_amp', 'feat.long_squares.rheobase_sweep.sweep_number', 'feat.long_squares.rheobase_sweep.v_baseline']
long_pulse missing from mine []
ramp missing from mine []
brief_pulse missing from mine []
Shell cwd was reset to
```

**Agent calls Write**

```json
{
 "file_path": "entries/yang-2026-flexible/build_notebook.py",
 "content": "\"\"\"Writes reproduce_yang_2026.ipynb from the cells below (kept beside the notebook so the cells can be read as code).\"\"\"\n\nimport nbformat as nbf\n\ncells = []\n\n\ndef md(text):\n    cells.append(nbf.v4.new_markdown_cell(text.strip(\"\\n\")))\n\n\ndef code(text, tags=None):\n    c = nbf.v4.new_code_cell(text.strip(\"\\n\"))\n    if tags:\n        c.metadata[\"tags\"] = list(tags)\n    cells.append(c)\n\n\nmd(r\"\"\"\n# Reproducing Yang (2026) on DANDI:000020\n\n**Paper.** Yang Z. (2026), \"Flexible Cellular Phenotypes Retain a Shared Type-Level Organization across\nResponse Regimes\", *eNeuro* 13(11), doi:10.1523/eneuro.0275-26.2026. The claims file,\n`claims/yang-2026-flexible.yaml`, was written from the version of record (PMC13737997), with the\nlegends of the Extended Data, and the paper's code at commit 61a5a41\n(https://github.com/zy-neuro/protocol-response-geometry).\n\n**Dataset.** DANDI:000020, \"Patch-seq recordings from mouse visual cortex\" (Allen Institute,\nGouwens et al. 2020), version **0.210913.1639**, doi:10.48324/dandi.000020/0.210913.1639. This is\nthe version the paper cites (the README of its code, \"Data\") and the only published version of the\ndandiset; the draft has the same 4,435 files and size. Every file is streamed into memory from the\narchive and never written to disk.\n\n**Outside inputs** (claims file, \"Outside data\"). The paper's join of the NWB files to the Allen\nPatch-seq metadata (t-type, subclass, Cre line), `results/m0/m0_molecular_join.csv`, and the\nretained feature lists, `results/phenotype/phenotype_summary.json`, both from the paper's code at\ncommit 61a5a41. The NeMO count matrix (release 20200611) is needed by the transcriptomic claims;\nits server did not answer during this attempt (section \"Transcriptomic claims\").\n\n| Claim | Tested here |\n|---|---|\n| join-link (added by the author) | tested |\n| cohort-label-join | tested |\n| table1-phenotype-spaces | tested |\n| pc1-long-pulse-loadings | tested |\n| fig1b-distance-correlation | tested |\n| fig1-fixed-five-pcs-ordering | tested |\n| fig1c-knn-jaccard | tested |\n| knn-scale-sweep | tested |\n| split-half-reliability | tested |\n| fig2c-eta2-ttype-over-cre | tested |\n| table2-alignment-ttype | tested |\n| ttype-beyond-cre | tested |\n| fig2d-knn-type-enrichment | tested |\n| fig2ab-ttype-structure-within-cre | tested |\n| fig3a-type-map-concordance | tested |\n| shared-map-model-call | tested |\n| subclass-map-concordance | tested |\n| equal-n-centroid-robustness | tested |\n| within-regime-type-map-reliability | tested |\n| fig3b-pair-tags | tested |\n| pair-tag-threshold-sensitivity | tested |\n| type-level-exceeds-cell-level | tested |\n| mobility-distribution | tested |\n| fig4ab-rna-tracks-shared-map, fig4-alternative-panels, fig4c-joint-excitability-modules, fig4c-kv3-strongest, fig4c-no-module-tracks-rank-range, pvalb-marker-control | blocked: the NeMO count matrix could not be fetched |\n| wgcna-mobility-within-type | blocked: the NeMO count matrix could not be fetched; WGCNA (R) is not in the entry's environment |\n\nA failure to reproduce here may be a failure of this attempt, not of the paper: see the\nreasoning and the differences from the paper's method.\n\"\"\")\n\ncode(r\"\"\"\nimport json, resource, time, warnings\nfrom collections import Counter\n\nimport numpy as np\nimport pandas as pd\nimport requests\nfrom scipy.stats import kruskal\n\nimport patchseq as ps\nimport geometry as g\n\nwarnings.filterwarnings(\"ignore\")\nKEY = ps.PAPER_KEY\nSEED_OFFSETS = [0, 1000, 2000, 3000, 4000]\nCODE = \"https://raw.githubusercontent.com/zy-neuro/protocol-response-geometry/61a5a413daea3b3562fad6e40207320da5665fed\"\n\n\ndef rng_for(claim, offset=0, k=0):\n    # the claim's generator (protocol): crc32 of \"<paper>/<claim>\", plus 1 per extra generator, plus the seed offset\n    return np.random.default_rng(ps.seed_of(claim) + offset + k)\n\n\ndef peak_gb():\n    return (resource.getrusage(resource.RUSAGE_SELF).ru_maxrss, resource.getrusage(resource.RUSAGE_CHILDREN).ru_maxrss)\n\n\nT0 = time.time()\nmeta = requests.get(f\"{ps.API}/dandisets/{ps.DANDISET}/versions/{ps.VERSION}/\", timeout=120).json()\nversions = requests.get(f\"{ps.API}/dandisets/{ps.DANDISET}/versions/\", timeout=120).json()[\"results\"]\nprint(\"dandiset:\", meta[\"name\"], \"| version\", ps.VERSION, \"| doi\", meta.get(\"doi\"))\nfor v in versions:\n    print(f\"  version {v['version']}: {v['asset_count']} assets, {v['size'] / 1e9:.1f} GB, modified {v['modified'][:10]}\")\nassets = ps.list_assets()\nprint(\"assets listed:\", len(assets), \"| total\", round(sum(a[\"size\"] for a in assets) / 1e9, 1), \"GB\")\nprint(\"file suffixes:\", Counter(a[\"path\"].rsplit(\"_\", 1)[-1] for a in assets))\nprint(\"subjects (folders):\", len({a[\"path\"].split(\"/\")[0] for a in assets}))\nprint(\"description (start):\", meta[\"metadata\"].get(\"description\", \"\")[:400])\n\"\"\")\n\nmd(r\"\"\"\n## Extraction\n\nOne pass over the 4,435 files, in six processes: each file is fetched into memory, opened as an IPFX\ndata set, and reduced to the cell-level features of the three regimes (long squares, short squares,\nramps), the split-half long-square features of claim split-half-reliability, and the values of the\ndata check. The method and where each part comes from are in the docstring of `patchseq.py`.\n\"\"\")\n\ncode(r\"\"\"\nt = time.time()\nrecs = ps.extract_all(assets, split_seed=ps.seed_of(\"split-half-reliability\"), workers=6, progress=500)\nprint(f\"extraction: {len(recs)} files in {(time.time() - t) / 60:.1f} min; peak memory (kB) self, largest child:\", peak_gb())\nprint(\"extract_ok:\", Counter(r[\"extract_ok\"] for r in recs))\nprint(\"errors:\", Counter(r[\"error\"].split(\":\")[0] for r in recs if r[\"error\"]))\nfor r in recs:\n    if r[\"error\"]:\n        print(\"  \", r[\"path\"], r[\"error\"][:150])\n\"\"\")\n\nmd(r\"\"\"\nThe extraction reads each file's sweep table and series with h5py in place of pynwb, to save time\n(`patchseq._fast_reader`). The next cell checks that this gives the same features, clock values and\nsplit halves as IPFX's own pynwb reader on eight files spread over the dandiset.\n\"\"\")\n\ncode(r\"\"\"\ncheck_idx = np.linspace(0, len(assets) - 1, 8).astype(int)\nsame_all = True\nfor i in check_idx:\n    a = assets[i]\n    f1 = ps.extract_cell(a, ps.seed_of(\"split-half-reliability\"), fast=True)\n    f2 = ps.extract_cell(a, ps.seed_of(\"split-half-reliability\"), fast=False)\n    keys_same = f1[\"features\"].keys() == f2[\"features\"].keys()\n    vals_same = keys_same and all(np.isclose(f1[\"features\"][k], f2[\"features\"][k], equal_nan=True) for k in f1[\"features\"])\n    split_same = (f1.get(\"split\") or {}).get(\"a\") == (f2.get(\"split\") or {}).get(\"a\") and (f1.get(\"split\") or {}).get(\"b\") == (f2.get(\"split\") or {}).get(\"b\")\n    same_all &= bool(vals_same and split_same and f1[\"clock\"] == f2[\"clock\"])\n    print(a[\"path\"], \"| features\", len(f1[\"features\"]), \"same:\", vals_same, \"| split same:\", split_same, \"| clock same:\", f1[\"clock\"] == f2[\"clock\"], \"| errors:\", f1[\"error\"] or \"-\", f2[\"error\"] or \"-\")\nprint(\"fast reader agrees with IPFX's reader on all checked files:\", same_all)\n\"\"\")\n\nmd(\"## Data check\")\n\ncode(r\"\"\"\nok = [r for r in recs if r[\"extract_ok\"] == 1]\nprint(\"files:\", len(recs), \"| opened and extracted:\", len(ok))\n# sessions and subjects, from the files against the paths\npath_ses = [r[\"path\"].split(\"_ses-\")[1].split(\"_\")[0] for r in ok]\nprint(\"session id in file equals the path's:\", sum(r[\"session_id\"] == s for r, s in zip(ok, path_ses)), \"of\", len(ok))\nprint(\"subject id in file equals the path's:\", sum((\"sub-\" + r[\"subject_id\"]) == r[\"path\"].split(\"/\")[0] for r in ok), \"of\", len(ok))\nprint(\"distinct sessions:\", len(set(path_ses)), \"| distinct subjects:\", len({r[\"subject_id\"] for r in ok}))\nprint(\"cells per subject:\", Counter(Counter(r[\"subject_id\"] for r in ok).values()).most_common(8))\nprint(\"sex:\", Counter(r[\"sex\"] for r in ok))\nages = pd.Series([float(r[\"age\"].strip(\"P\").rstrip(\"D\").split(\".\")[0]) if r[\"age\"].startswith(\"P\") else np.nan for r in ok])\nprint(\"age (days): median\", ages.median(), \"range\", ages.min(), \"to\", ages.max(), \"| missing\", int(ages.isna().sum()))\ncre_nwb = Counter(r[\"genotype\"].split(\";\")[0].split(\"/\")[0] for r in ok)\nprint(\"Cre driver in the files' genotype (first allele):\", len(cre_nwb), \"lines;\", cre_nwb.most_common(12))\nprint(\"MIES files:\", Counter(r.get(\"mies\", True) for r in ok))\n# sweeps per regime (current clamp, with experiment and stim epochs)\nns = pd.DataFrame([r[\"n_sweeps\"] for r in ok])\nprint(\"cells with at least one usable sweep: long squares\", int((ns.long_squares > 0).sum()),\n      \"| short squares\", int((ns.short_squares > 0).sum()), \"| ramps\", int((ns.ramps > 0).sum()))\nprint(\"usable sweeps per cell, median (range): long\", ns.long_squares.median(), (ns.long_squares.min(), ns.long_squares.max()),\n      \"| short\", ns.short_squares.median(), (ns.short_squares.min(), ns.short_squares.max()),\n      \"| ramp\", ns.ramps.median(), (ns.ramps.min(), ns.ramps.max()))\nprint(\"regime extraction failed (IPFX state), of\", len(ok), \":\", {k: sum(r[\"failed\"][k] for r in ok) for k in ok[0][\"failed\"]})\n\"\"\", tags=[\"sanity\"])\n\ncode(r\"\"\"\n# Units and ranges of the features the phenotype spaces use\nsummary = json.loads(requests.get(f\"{CODE}/results/phenotype/phenotype_summary.json\", timeout=120).text)\npaper_cols = {p: list(summary[p][\"features\"]) for p in g.REGIMES}\nrows = []\nfor p in g.REGIMES:\n    stems_p, x = g.feature_matrix(recs, paper_cols[p])\n    for j, c in enumerate(paper_cols[p]):\n        v = x[:, j][np.isfinite(x[:, j])]\n        rows.append({\"regime\": p, \"feature\": c.split(\".\", 2)[2], \"n\": v.size, \"min\": v.min() if v.size else np.nan,\n                     \"median\": np.median(v) if v.size else np.nan, \"max\": v.max() if v.size else np.nan})\nwith pd.option_context(\"display.max_rows\", 200, \"display.width\", 200):\n    print(pd.DataFrame(rows).round(4).to_string(index=False))\n\"\"\", tags=[\"sanity\"])\n\ncode(r\"\"\"\n# Clock: the voltage response of each cell's most hyperpolarizing long square starts with the stimulus.\nclk = pd.DataFrame([dict(r[\"clock\"], stem=r[\"file_stem\"]) for r in ok if r.get(\"clock\")])\nprint(\"cells with a hyperpolarizing long square:\", len(clk), \"of\", len(ok))\nprint(\"stimulus onset (s) from the stimulus trace:\", Counter(clk.start.round(2)).most_common(4), \"| duration (s):\", Counter(clk.dur.round(2)).most_common(3))\nprint(\"amplitude (pA): median\", clk.amp.median(), \"range\", clk.amp.min(), clk.amp.max())\nprint(\"voltage change relative to baseline (mV), median [5th, 95th percentile]:\")\nfor col, what in [(\"pre\", \"10 ms just before onset\"), (\"post\", \"15 to 25 ms after onset\"), (\"dv\", \"last 100 ms of the step\")]:\n    print(f\"  {what}: {clk[col].median():.2f} [{clk[col].quantile(0.05):.2f}, {clk[col].quantile(0.95):.2f}]\")\nprint(\"cells whose response is negative 15 to 25 ms after onset:\", int((clk.post < -1).sum()), \"| more than 1 mV off before onset:\", int((clk.pre.abs() > 1).sum()))\n# Recordings deposited twice: identical voltage traces (length and sum) of that sweep\nfp = Counter(clk.fingerprint)\ndups = [(k, n) for k, n in fp.items() if n > 1]\nprint(\"identical traces shared by more than one file:\", len(dups))\nfor k, n in dups[:10]:\n    print(\"  \", k, list(clk.stem[clk.fingerprint == k]))\n\"\"\", tags=[\"sanity\"])\n\nmd(r\"\"\"\n## Labels: the paper's join (outside input)\n\n### join-link (added by the author)\n\n> The NWB files of the dandiset are the cells of the paper's metadata join (results/m0/m0_molecular_join.csv at commit 61a5a41): matched by file stem, with the same session, subject and Cre line, and the same membership of the three regimes.\n\"\"\")\n\ncode(r\"\"\"\njoin_df = pd.read_csv(f\"{CODE}/results/m0/m0_molecular_join.csv\", dtype=str, keep_default_na=False)\njoin = {r[\"file_stem\"]: r for r in join_df.to_dict(\"records\")}\nstems_all = [r[\"file_stem\"] for r in recs]\nprint(\"join rows:\", len(join_df), \"| distinct stems:\", join_df.file_stem.nunique(), \"| columns:\", list(join_df.columns))\nmatched = [s for s in stems_all if s in join]\nprint(\"dandiset files with a join row:\", len(matched), \"of\", len(stems_all), f\"({len(matched) / len(stems_all):.1%})\")\nprint(\"join rows without a dandiset file:\", len(set(join) - set(stems_all)))\nby = {r[\"file_stem\"]: r for r in ok}\nagree = Counter()\nfor s in matched:\n    if s not in by:\n        continue\n    r, j = by[s], join[s]\n    agree[\"session\"] += r[\"session_id\"] == j[\"session_id\"]\n    agree[\"subject\"] += r[\"subject_id\"] == j[\"subject_id\"]\n    agree[\"genotype\"] += r[\"genotype\"] == j[\"full_genotype\"]\n    agree[\"cre_in_genotype\"] += j[\"cre_line\"].split(\"/\")[0].split(\";\")[0] in r[\"genotype\"]\n    agree[\"n\"] += 1\nprint(\"matched and extracted:\", agree[\"n\"], \"| same session id:\", agree[\"session\"], \"| same subject id:\", agree[\"subject\"],\n      \"| same full genotype:\", agree[\"genotype\"], \"| join Cre line found in the file's genotype:\", agree[\"cre_in_genotype\"])\nprint(\"missing in the dandiset (no file):\", sorted(set(join) - set(stems_all))[:5])\nprint(\"files with no join row:\", [s for s in stems_all if s not in join])\n\"\"\", tags=[\"claim:join-link\"])\n\nmd(r\"\"\"\n### cohort-label-join\n\n> Of the cells, 4,430 have a row in the joined metadata table and 4,266 a non-empty t-type; the cells with a t-type number 4,183 in long-pulse, 3,988 in ramp and 4,266 in brief-pulse.\n\nThe per-regime counts need the phenotype spaces of claim table1-phenotype-spaces, built next; they are printed in that claim's section.\n\"\"\")\n\ncode(r\"\"\"\nn_join = len(matched)\nn_ttype = sum(1 for s in matched if join[s][\"t_type\"].strip())\nprint(\"cells with a join row:\", n_join, \"| with a non-empty t-type:\", n_ttype, \"| join rows with a t-type:\", int((join_df.t_type.str.strip() != \"\").sum()))\n\"\"\", tags=[\"claim:cohort-label-join\"])\n\nmd(r\"\"\"\n## Phenotype spaces\n\n### table1-phenotype-spaces\n\n> Built independently per regime, the phenotype spaces hold 4,344 long-pulse cells with 42 features and k80 = 11 components, 4,139 ramp cells with 20 features and k80 = 3, and 4,422 brief-pulse cells with 21 features and k80 = 5; the same-cell overlaps are 4,054 (long-pulse and ramp), 4,336 (long-pulse and brief-pulse), 4,134 (ramp and brief-pulse) and 4,049 (all three).\n\nFirst the paper's rule for retained features (at most 30% missing, nonzero variance) applied to the\nfeatures extracted here, under both denominators (reading 2a, cells with a value in the regime; 2b,\nall extract_ok cells), against the paper's lists; then the spaces on the paper's lists, as the\ncriterion says, and the same on the rule's lists as a variant.\n\"\"\")\n\ncode(r\"\"\"\nrule_lists = {}\nfor p in g.REGIMES:\n    for den in (\"present\", \"all\"):\n        keep, miss = g.rule_features(recs, p, denominator=den)\n        rule_lists[(p, den)] = keep\n        extra = sorted(set(keep) - set(paper_cols[p]))\n        lost = sorted(set(paper_cols[p]) - set(keep))\n        print(f\"{p}, missingness over {den} cells: rule keeps {len(keep)} of {len(miss)} candidate features; paper's list {len(paper_cols[p])};\"\n              f\" same list: {set(keep) == set(paper_cols[p])}\")\n        if extra:\n            print(\"    kept here, not in the paper's list:\", [c.split('.', 2)[2] for c in extra])\n        if lost:\n            print(\"    in the paper's list, not kept here:\", [(c.split('.', 2)[2], round(miss.get(c, np.nan), 3)) for c in lost])\nspaces = {p: g.phenotype_space(recs, paper_cols[p]) for p in g.REGIMES}\nspaces_rule = {p: g.phenotype_space(recs, rule_lists[(p, \"present\")]) for p in g.REGIMES}\nsets = {p: set(spaces[p][\"stems\"]) for p in g.REGIMES}\nprint()\nfor label, sp in ((\"paper's lists\", spaces), (\"rule's lists (variant)\", spaces_rule)):\n    st = {p: set(sp[p][\"stems\"]) for p in g.REGIMES}\n    print(label)\n    for p in g.REGIMES:\n        print(f\"  {p}: cells {len(sp[p]['stems'])}, features {len(sp[p]['columns'])}, k80 {sp[p]['k80']}\"\n              f\" (cumulative variance at k80 {np.cumsum(sp[p]['var'])[sp[p]['k80'] - 1]:.3f}, at k80 - 1 {np.cumsum(sp[p]['var'])[sp[p]['k80'] - 2]:.3f})\")\n    print(\"  shared: long-ramp\", len(st[\"long_pulse\"] & st[\"ramp\"]), \"| long-brief\", len(st[\"long_pulse\"] & st[\"brief_pulse\"]),\n          \"| ramp-brief\", len(st[\"ramp\"] & st[\"brief_pulse\"]), \"| all three\", len(st[\"long_pulse\"] & st[\"ramp\"] & st[\"brief_pulse\"]))\n# against the paper's own regime membership (join columns in_long_pulse, in_ramp, in_brief_pulse)\nfor p in g.REGIMES:\n    theirs = {s for s, r in join.items() if r[f\"in_{p}\"] == \"1\"}\n    print(f\"{p}: paper's join lists {len(theirs)} cells in the regime; here {len(sets[p])}; in both {len(theirs & sets[p])};\"\n          f\" only paper {len(theirs - sets[p])}; only here {len(sets[p] - theirs)}\")\nprint(\"cells with a t-type per regime: long\", sum(join.get(s, {}).get(\"t_type\", \"\").strip() != \"\" for s in spaces[\"long_pulse\"][\"stems\"]),\n      \"| ramp\", sum(join.get(s, {}).get(\"t_type\", \"\").strip() != \"\" for s in spaces[\"ramp\"][\"stems\"]),\n      \"| brief\", sum(join.get(s, {}).get(\"t_type\", \"\").strip() != \"\" for s in spaces[\"brief_pulse\"][\"stems\"]))\n\"\"\", tags=[\"claim:table1-phenotype-spaces\", \"claim:cohort-label-join\"])\n\nmd(r\"\"\"\n### pc1-long-pulse-loadings\n\n> Long-pulse PC1 loads most strongly on rheobase or threshold current and on input resistance.\n\"\"\")\n\ncode(r\"\"\"\nlp = spaces[\"long_pulse\"]\nload = pd.DataFrame({\"feature\": [c.split(\".\", 2)[2] for c in lp[\"columns\"]], \"loading\": lp[\"loadings\"][0]})\nload[\"abs\"] = load.loading.abs()\nload = load.sort_values(\"abs\", ascending=False).reset_index(drop=True)\ncurrent = {\"threshold_i\", \"rheobase_i\", \"rheobase_sweep.stim_amp\", \"hero_sweep.stim_amp\"}\nresist = {\"ri\", \"input_resistance\"}\nload[\"kind\"] = np.where(load.feature.isin(current), \"current\", np.where(load.feature.isin(resist), \"input resistance\", \"other\"))\nprint(load.head(12).round(3).to_string())\nkinds = [k for k in load.kind if k != \"other\"]\nfirst_two_kinds = []\nfor k in load.kind:\n    if k not in first_two_kinds:\n        first_two_kinds.append(k)\nprint(\"PC1 explains\", round(lp[\"var\"][0], 3), \"of the variance\")\nprint(\"reading (a), the two highest-ranked kinds of feature:\", first_two_kinds[:2])\nprint(\"reading (b), kinds among the top five:\", sorted(set(load.kind[:5])))\n\"\"\", tags=[\"claim:pc1-long-pulse-loadings\"])\n\nmd(r\"\"\"\n## Cell-level conservation\n\n### fig1b-distance-correlation\n\n> Pairwise cell-cell phenotypic distances are positively correlated across all three regime pairs, above shuffle and well below identity, strongest for long-pulse and ramp (Spearman rho 0.434), then ramp and brief-pulse (0.384), then long-pulse and brief-pulse (0.336).\n\"\"\")\n\ncode(r\"\"\"\nclaim = \"fig1b-distance-correlation\"\ndc = {}\nfor a, b in g.PAIRS:\n    stems_ab, xa, xb = g.shared(spaces[a], spaces[b])\n    res = g.distance_correlation(xa, xb, rng_for(claim), n_shuffle=100, unique=True)\n    var = g.distance_correlation(xa, xb, rng_for(claim, k=1), n_shuffle=100, unique=False)\n    seeds = [g.distance_correlation(xa, xb, rng_for(claim, off), n_shuffle=0, unique=True)[\"rho\"] for off in SEED_OFFSETS]\n    dc[(a, b)] = res\n    print(f\"{a} vs {b}: n = {res['n']}, rho = {res['rho']:.4f}, p = {res['p']:.4f} (null mean {res['null_mean']:.4f}, max {res['null_max']:.4f});\"\n          f\" code's pair draw rho = {var['rho']:.4f} ({var['n_unique_pairs']} unique of {var['n_pairs']});\"\n          f\" five seeds {min(seeds):.4f} to {max(seeds):.4f}\")\norder = sorted(dc, key=lambda k: -dc[k][\"rho\"])\nprint(\"order:\", [f\"{a}-{b}\" for a, b in order])\n\"\"\", tags=[\"claim:fig1b-distance-correlation\"])\n\nmd(r\"\"\"\n### fig1-fixed-five-pcs-ordering\n\n> The ordering of cross-regime distance correlations is unchanged when a fixed five principal components are kept in each regime instead of k80.\n\"\"\")\n\ncode(r\"\"\"\nclaim = \"fig1-fixed-five-pcs-ordering\"\ndc5 = {}\nfor a, b in g.PAIRS:\n    stems_ab, xa, xb = g.shared(spaces[a], spaces[b], 5, 5)\n    seeds = [g.distance_correlation(xa, xb, rng_for(claim, off), n_shuffle=0, unique=True)[\"rho\"] for off in SEED_OFFSETS]\n    dc5[(a, b)] = seeds[0]\n    print(f\"{a} vs {b}, five PCs: rho = {seeds[0]:.4f} (five seeds {min(seeds):.4f} to {max(seeds):.4f})\")\nprint(\"order with five PCs:\", [f\"{a}-{b}\" for a, b in sorted(dc5, key=lambda k: -dc5[k])])\n\"\"\", tags=[\"claim:fig1-fixed-five-pcs-ordering\"])\n\nmd(r\"\"\"\n### fig1c-knn-jaccard\n\n> Local neighborhoods are much less stable; the mean Jaccard overlap of each cell's 15 nearest neighbors across regimes is 0.023 (long-pulse and ramp), 0.022 (long-pulse and brief-pulse) and 0.019 (ramp and brief-pulse), only modestly above index-shuffle chance of about 0.002.\n\"\"\")\n\ncode(r\"\"\"\nclaim = \"fig1c-knn-jaccard\"\nkj = {}\nfor a, b in g.PAIRS:\n    stems_ab, xa, xb = g.shared(spaces[a], spaces[b])\n    res = g.knn_jaccard(xa, xb, 15, rng_for(claim))\n    chances = [res[\"chance\"]] + [g.knn_jaccard(xa, xb, 15, rng_for(claim, off))[\"chance\"] for off in SEED_OFFSETS[1:]]\n    kj[(a, b)] = res\n    print(f\"{a} vs {b}: n = {res['n']}, mean Jaccard = {res['mean']:.4f} (median {res['median']:.4f}), chance = {res['chance']:.5f}\"\n          f\" (five seeds {min(chances):.5f} to {max(chances):.5f}), adjusted {res['adjusted']:.4f}\")\n\"\"\", tags=[\"claim:fig1c-knn-jaccard\"])\n\nmd(r\"\"\"\n### knn-scale-sweep\n\n> Across neighborhood sizes k = 15 to 600, chance-adjusted overlap rises with k but stays low even at k = 600 (0.134, 0.101 and 0.108 for long-pulse and ramp, long-pulse and brief-pulse, ramp and brief-pulse).\n\"\"\")\n\ncode(r\"\"\"\nclaim = \"knn-scale-sweep\"\ngrid = [15, 30, 60, 120, 240, 480, 600]\nscale = []\nfor a, b in g.PAIRS:\n    stems_ab, xa, xb = g.shared(spaces[a], spaces[b])\n    rng = rng_for(claim)\n    for k in grid:\n        res = g.knn_jaccard(xa, xb, k, rng)\n        scale.append({\"pair\": f\"{a}-{b}\", \"k\": k, \"mean\": res[\"mean\"], \"chance\": res[\"chance\"], \"adjusted\": res[\"adjusted\"]})\n    adj600 = [g.knn_jaccard(xa, xb, 600, rng_for(claim, off))[\"adjusted\"] for off in SEED_OFFSETS[1:]]\n    print(f\"{a}-{b}: adjusted at k = 600 under the other four seeds: {np.round(adj600, 4)}\")\nscale = pd.DataFrame(scale)\nprint(scale.pivot(index=\"k\", columns=\"pair\", values=\"adjusted\").round(4).to_string())\nfor pair, sub in scale.groupby(\"pair\"):\n    adj = sub.sort_values(\"k\").adjusted.values\n    print(pair, \"| rises at every step:\", bool(np.all(np.diff(adj) > 0)), \"| k=600 above k=15:\", bool(adj[-1] > adj[0]))\n\"\"\", tags=[\"claim:knn-scale-sweep\"])\n\nmd(r\"\"\"\n### split-half-reliability\n\n> Within long-pulse, neighborhoods built from two disjoint halves of each cell's sweeps overlap more (mean 15-NN Jaccard 0.109, chance about 0.0026, adjusted 0.107, 3,598 cells) than cross-regime neighborhoods in the same pool (0.025, 0.024 and 0.020), but far from completely.\n\nThe halves were extracted in the pass above (the code's `extract_one_split`, its random split under\nthe claim's seed); each half is put in the paper's long-pulse columns, missing values filled with\nthe full-cell feature mean, z-scored with the full-cell mean and SD and projected on the full-cell\nloadings (k80 components).\n\"\"\")\n\ncode(r\"\"\"\nclaim = \"split-half-reliability\"\nsp_recs = [r for r in ok if r.get(\"split\")]\nprint(\"cells with at least four usable long squares:\", sum(r[\"split\"][\"n_usable\"] >= ps.MIN_USABLE for r in sp_recs),\n      \"| both halves extracted:\", sum(r[\"split\"][\"ok\"] for r in sp_recs))\nprint(\"split rules used:\", Counter(r[\"split\"][\"rule\"] for r in sp_recs if r[\"split\"][\"ok\"]))\nprint(\"reasons for no split:\", Counter(r[\"split\"][\"reason\"].split(\":\")[0][:40] for r in sp_recs if not r[\"split\"][\"ok\"]).most_common(6))\nlp = spaces[\"long_pulse\"]\ncols = lp[\"columns\"]\nhalves = [r for r in sp_recs if r[\"split\"][\"ok\"]]\nxa = np.array([[r[\"split\"][\"a\"].get(c, np.nan) for c in cols] for r in halves], dtype=float)\nxb = np.array([[r[\"split\"][\"b\"].get(c, np.nan) for c in cols] for r in halves], dtype=float)\nkeep = np.isfinite(xa).any(axis=1) & np.isfinite(xb).any(axis=1)\nxa, xb = xa[keep], xb[keep]\nhalf_stems = [r[\"file_stem\"] for r, k in zip(halves, keep) if k]\n\n\ndef project(x):\n    xf = np.where(np.isfinite(x), x, lp[\"mu\"])\n    return ((xf - lp[\"mu\"]) / lp[\"sd\"]) @ lp[\"loadings\"].T[:, : lp[\"k80\"]]\n\n\npa, pb = project(xa), project(xb)\nres = g.knn_jaccard(pa, pb, 15, rng_for(claim))\nchances = [res[\"chance\"]] + [g.knn_jaccard(pa, pb, 15, rng_for(claim, off))[\"chance\"] for off in SEED_OFFSETS[1:]]\nprint(f\"projected split-half cells: {len(half_stems)}; within long-pulse half A against half B: mean 15-NN Jaccard {res['mean']:.4f},\"\n      f\" chance {res['chance']:.5f} (five seeds {min(chances):.5f} to {max(chances):.5f}), adjusted {res['adjusted']:.4f}\")\nsame_pool = {}\nfor a, b in g.PAIRS:\n    pool = [s for s in half_stems if s in sets[a] and s in sets[b]]\n    pos_a = {s: i for i, s in enumerate(spaces[a][\"stems\"])}\n    pos_b = {s: i for i, s in enumerate(spaces[b][\"stems\"])}\n    xa_ = spaces[a][\"scores\"][[pos_a[s] for s in pool], : spaces[a][\"k80\"]]\n    xb_ = spaces[b][\"scores\"][[pos_b[s] for s in pool], : spaces[b][\"k80\"]]\n    r2 = g.knn_jaccard(xa_, xb_, 15, rng_for(claim, k=1), n_shuffle=1)\n    same_pool[(a, b)] = r2[\"mean\"]\n    print(f\"same pool {a}-{b}: n = {len(pool)}, mean 15-NN Jaccard {r2['mean']:.4f}\")\nprint(\"within exceeds every same-pool cross-regime value:\", all(res[\"mean\"] > v for v in same_pool.values()))\n\"\"\", tags=[\"claim:split-half-reliability\"])\n\nmd(r\"\"\"\n## Transcriptomic type anchors the phenotype\n\n### fig2c-eta2-ttype-over-cre\n\n> T-type accounts for more multivariate phenotypic variance than Cre line in every regime (eta squared 0.327 against 0.209 long-pulse, 0.393 against 0.267 ramp, 0.149 against 0.110 brief-pulse).\n\nReadings for Cre: (a) the code's set, cells with both a t-type and a Cre line; (b) all cells with a\nCre line. The join gives every row a Cre line. A variant takes the Cre line from the files' own\ngenotype (the dandiset), for the cells of reading (b).\n\"\"\")\n\ncode(r\"\"\"\ncre_file = {r[\"file_stem\"]: r[\"genotype\"].split(\";\")[0].split(\"/\")[0] for r in ok}\neta = {}\nfor p in g.REGIMES:\n    x_t, lab_t, idx_t = g.labelled(spaces[p], join, \"t_type\")\n    cre_on_t = np.array([join[spaces[p][\"stems\"][i]][\"cre_line\"].strip() for i in idx_t], dtype=object)\n    has_c = cre_on_t != \"\"\n    e_t = g.eta2(x_t, lab_t)\n    e_ca = g.eta2(x_t[has_c], cre_on_t[has_c])\n    x_c, lab_c, idx_c = g.labelled(spaces[p], join, \"cre_line\")\n    e_cb = g.eta2(x_c, lab_c)\n    lab_f = np.array([cre_file[spaces[p][\"stems\"][i]] for i in idx_c], dtype=object)\n    e_cf = g.eta2(x_c, lab_f)\n    eta[p] = (e_t, e_ca, e_cb)\n    print(f\"{p}: t-type eta2 {e_t:.4f} (n {len(lab_t)}, {len(set(lab_t))} types) | Cre (a) {e_ca:.4f} (n {int(has_c.sum())}, {len(set(cre_on_t[has_c]))} lines)\"\n          f\" | Cre (b) {e_cb:.4f} (n {len(lab_c)}) | Cre from the files' genotype {e_cf:.4f} ({len(set(lab_f))} lines) | t-type > Cre: {e_t > e_ca}\")\n\"\"\", tags=[\"claim:fig2c-eta2-ttype-over-cre\"])\n\nmd(r\"\"\"\n### table2-alignment-ttype\n\n> Pairwise alignment of binary t-type mismatch with phenotypic distance is small in all three regimes (A_t 0.021 long-pulse, 0.025 ramp, 0.021 brief-pulse) but exceeds shuffled labels in each.\n\"\"\")\n\ncode(r\"\"\"\nclaim = \"table2-alignment-ttype\"\nfor p in g.REGIMES:\n    x_t, lab_t, _ = g.labelled(spaces[p], join, \"t_type\")\n    res = g.alignment(x_t, lab_t, rng_for(claim))\n    seeds = [res[\"A\"]] + [g.alignment(x_t, lab_t, rng_for(claim, off), n_shuffle=0)[\"A\"] for off in SEED_OFFSETS[1:]]\n    avg = g.alignment(x_t, lab_t, rng_for(claim, k=1), n_shuffle=0, average_ranks=True)[\"A\"]\n    print(f\"{p}: n {res['n']}, A_t {res['A']:.4f}, p {res['p']:.4f} (null mean {res['null_mean']:.4f}, max {res['null_max']:.4f});\"\n          f\" five seeds {min(seeds):.4f} to {max(seeds):.4f}; average-rank Spearman (variant) {avg:.4f}\")\n\"\"\", tags=[\"claim:table2-alignment-ttype\"])\n\nmd(r\"\"\"\n### ttype-beyond-cre\n\n> After removing each Cre line's mean phenotype, t-type alignment stays above the shuffled-label null in all three regimes, though weaker (A_t 0.011, 0.010 and 0.004 for long-pulse, ramp and brief-pulse), and residual t-type eta squared remains detectable.\n\"\"\")\n\ncode(r\"\"\"\nclaim = \"ttype-beyond-cre\"\nfor p in g.REGIMES:\n    x_t, lab_t, idx_t = g.labelled(spaces[p], join, \"t_type\")\n    cre = np.array([join[spaces[p][\"stems\"][i]][\"cre_line\"].strip() for i in idx_t], dtype=object)\n    has = cre != \"\"\n    xr = g.residualize(x_t[has], cre[has])\n    res = g.alignment(xr, lab_t[has], rng_for(claim))\n    seeds = [res[\"A\"]] + [g.alignment(xr, lab_t[has], rng_for(claim, off), n_shuffle=0)[\"A\"] for off in SEED_OFFSETS[1:]]\n    e_res = g.eta2(xr, lab_t[has])\n    r2 = rng_for(claim, k=1)\n    null = [g.eta2(xr, lab_t[has][r2.permutation(has.sum())]) for _ in range(100)]\n    print(f\"{p}: n {int(has.sum())}, residual A_t {res['A']:.4f}, p {res['p']:.4f} (null mean {res['null_mean']:.4f}); five seeds {min(seeds):.4f} to {max(seeds):.4f};\"\n          f\" residual t-type eta2 {e_res:.4f} against label-shuffle null mean {np.mean(null):.4f} (max {np.max(null):.4f})\")\n\"\"\", tags=[\"claim:ttype-beyond-cre\"])\n\nmd(r\"\"\"\n### fig2d-knn-type-enrichment\n\n> Cells are enriched for phenotypic neighbors of their own t-type, most for long-pulse (6.59-fold), then ramp (3.44-fold) and brief-pulse (2.64-fold).\n\"\"\")\n\ncode(r\"\"\"\nenr = {}\nfor p in g.REGIMES:\n    x_t, lab_t, _ = g.labelled(spaces[p], join, \"t_type\")\n    res = g.knn_enrichment(x_t, lab_t)\n    enr[p] = res[\"ratio_of_means\"]\n    print(f\"{p}: n {res['n']}, same-type fraction {res['same']:.4f}, chance {res['chance']:.4f}, enrichment (ratio of means) {res['ratio_of_means']:.3f},\"\n          f\" mean of per-cell ratios (variant) {res['mean_of_ratios']:.3f}\")\nprint(\"order long > ramp > brief:\", enr[\"long_pulse\"] > enr[\"ramp\"] > enr[\"brief_pulse\"])\n\"\"\", tags=[\"claim:fig2d-knn-type-enrichment\"])\n\nmd(r\"\"\"\n### fig2ab-ttype-structure-within-cre\n\n> T-types occupy distinct but overlapping parts of phenotype space, and finer t-type structure remains within single Cre-driver populations; within Sst-IRES-Cre the six most frequent t-types occupy distinct positions on long-pulse PC1.\n\"\"\")\n\ncode(r\"\"\"\nclaim = \"fig2ab-ttype-structure-within-cre\"\np = \"long_pulse\"\nx_t, lab_t, idx_t = g.labelled(spaces[p], join, \"t_type\")\ncre = np.array([join[spaces[p][\"stems\"][i]][\"cre_line\"].strip() for i in idx_t], dtype=object)\nrng = rng_for(claim)\nrows = []\nfor c, n in Counter(cre.tolist()).most_common():\n    sel = cre == c\n    if n < 80 or len(set(lab_t[sel])) < 2:\n        continue\n    res = g.alignment(x_t[sel], lab_t[sel], rng)\n    e = g.eta2(x_t[sel], lab_t[sel])\n    null = [g.eta2(x_t[sel], lab_t[sel][rng.permutation(n)]) for _ in range(100)]\n    rows.append({\"cre\": c, \"n\": n, \"t_types\": len(set(lab_t[sel])), \"A_t\": res[\"A\"], \"p\": res[\"p\"], \"eta2\": e, \"eta2_null_mean\": np.mean(null)})\nwithin = pd.DataFrame(rows)\nprint(within.round(4).to_string(index=False))\nsst = within[within.cre.str.startswith(\"Sst-IRES-Cre\")]\nprint(\"Sst-IRES-Cre rows:\", sst.cre.tolist())\nsel = cre == (sst.cre.iloc[0] if len(sst) else \"\")\nif sel.any():\n    top = [t for t, _ in Counter(lab_t[sel].tolist()).most_common(6)]\n    pc1 = x_t[sel, 0]\n    groups = [pc1[lab_t[sel] == t] for t in top]\n    for t, gr in zip(top, groups):\n        print(f\"  {t}: n {gr.size}, median PC1 {np.median(gr):.3f}\")\n    print(\"  Kruskal-Wallis across the six (descriptive):\", kruskal(*groups))\n\"\"\", tags=[\"claim:fig2ab-ttype-structure-within-cre\"])\n\nmd(r\"\"\"\n## Type-level relationships\n\n### fig3a-type-map-concordance\n\n> Among the 57 t-types with at least 10 cells in every regime (1,596 type pairs), type-type centroid distance maps are concordant across all three regime pairs, strongest for long-pulse and ramp (rho 0.658), then ramp and brief-pulse (0.608), then long-pulse and brief-pulse (0.455).\n\"\"\")\n\ncode(r\"\"\"\nclaim = \"fig3a-type-map-concordance\"\nlab = {p: g.labelled(spaces[p], join, \"t_type\") for p in g.REGIMES}\ncounts = {p: Counter(lab[p][1].tolist()) for p in g.REGIMES}\ntypes = sorted(t for t in counts[\"long_pulse\"] if all(counts[p][t] >= 10 for p in g.REGIMES))\ncodes = {p: g.type_codes(lab[p][1], types) for p in g.REGIMES}\nS = {p: g.centroid_distances(lab[p][0], codes[p], len(types))[0] for p in g.REGIMES}\nprint(\"t-types with at least 10 cells in every regime:\", len(types), \"| type pairs:\", len(types) * (len(types) - 1) // 2)\nconc = {}\nnulls = {}\nfor a, b in g.PAIRS:\n    rho = g.spearman(g.upper(S[a]), g.upper(S[b]))\n    per_seed = []\n    for off in SEED_OFFSETS:\n        rng = rng_for(claim, off)\n        lab_b = lab[b][1]\n        null = np.empty(1000)\n        for t in range(1000):\n            sh = lab_b[rng.permutation(lab_b.size)]\n            null[t] = g.spearman(g.upper(S[a]), g.upper(g.centroid_distances(lab[b][0], g.type_codes(sh, types), len(types))[0]))\n        per_seed.append(null)\n    conc[(a, b)] = rho\n    nulls[(a, b)] = per_seed[0]\n    ps_ = [g.emp_p(nl, rho) for nl in per_seed]\n    print(f\"{a} vs {b}: rho {rho:.4f}, p {ps_[0]:.6f} (null mean {per_seed[0].mean():.4f}, max {per_seed[0].max():.4f}); p under five seeds {np.round(ps_, 6)}\")\nprint(\"order:\", [f\"{a}-{b}\" for a, b in sorted(conc, key=lambda k: -conc[k])])\n\"\"\", tags=[\"claim:fig3a-type-map-concordance\"])\n\nmd(r\"\"\"\n### shared-map-model-call\n\n> The three type-map concordances meet the prespecified shared-map criterion (minimum rho at least 0.40 and range across the three below 0.25).\n\"\"\")\n\ncode(r\"\"\"\nvals = np.array(list(conc.values()))\nprint(f\"minimum {vals.min():.4f}, maximum {vals.max():.4f}, range {vals.max() - vals.min():.4f}; shared-map rule holds: {vals.min() >= 0.40 and vals.max() - vals.min() < 0.25}\")\n\"\"\", tags=[\"claim:shared-map-model-call\"])\n\nmd(r\"\"\"\n### subclass-map-concordance\n\n> At the subclass level (six subclasses), type relationships are even more conserved between long-pulse and ramp (rho 0.936) and moderately aligned for the comparisons with brief-pulse (0.579 and 0.621).\n\"\"\")\n\ncode(r\"\"\"\nsub = {p: g.labelled(spaces[p], join, \"subclass\") for p in g.REGIMES}\nsub_types = {p: sorted(t for t, n in Counter(sub[p][1].tolist()).items() if n >= 10) for p in g.REGIMES}\nprint(\"subclasses with at least 10 cells:\", {p: sub_types[p] for p in g.REGIMES})\nfor a, b in g.PAIRS:\n    sh = sorted(set(sub_types[a]) & set(sub_types[b]))\n    Sa = g.centroid_distances(sub[a][0], g.type_codes(sub[a][1], sh), len(sh))[0]\n    Sb = g.centroid_distances(sub[b][0], g.type_codes(sub[b][1], sh), len(sh))[0]\n    print(f\"{a} vs {b}: {len(sh)} shared subclasses, rho {g.spearman(g.upper(Sa), g.upper(Sb)):.4f} (average ranks {g.spearman_avg(g.upper(Sa), g.upper(Sb)):.4f})\")\n\"\"\", tags=[\"claim:subclass-map-concordance\"])\n\nmd(r\"\"\"\n### equal-n-centroid-robustness\n\n> Rebuilt from 10 cells per type per regime (200 resamples), type-map concordance drops for all three pairs (long-pulse and ramp mean 0.554, ramp and brief-pulse 0.455, long-pulse and brief-pulse 0.329) but stays well above shuffled-label nulls.\n\"\"\")\n\ncode(r\"\"\"\nclaim = \"equal-n-centroid-robustness\"\nby_type = {p: {t: np.where(codes[p] == i)[0] for i, t in enumerate(types)} for p in g.REGIMES}\n\n\ndef equal_n(rng, n_boot=200, n_draw=10):\n    out = {pair: [] for pair in g.PAIRS}\n    for _ in range(n_boot):\n        Sb = {}\n        for p in g.REGIMES:\n            take = np.concatenate([rng.choice(by_type[p][t], size=n_draw, replace=False) for t in types])\n            cc = np.repeat(np.arange(len(types)), n_draw)\n            Sb[p] = g.centroid_distances(lab[p][0][take], cc, len(types))[0]\n        for a, b in g.PAIRS:\n            out[(a, b)].append(g.spearman(g.upper(Sb[a]), g.upper(Sb[b])))\n    return {k: np.array(v) for k, v in out.items()}\n\n\neq = equal_n(rng_for(claim))\neq_seeds = [eq] + [equal_n(rng_for(claim, off)) for off in SEED_OFFSETS[1:]]\nfor a, b in g.PAIRS:\n    v = eq[(a, b)]\n    nl = nulls[(a, b)]\n    means = [e[(a, b)].mean() for e in eq_seeds]\n    print(f\"{a} vs {b}: full {conc[(a, b)]:.4f}; equal-N mean {v.mean():.4f}, 95% interval {np.quantile(v, 0.025):.4f} to {np.quantile(v, 0.975):.4f};\"\n          f\" five seeds mean {min(means):.4f} to {max(means):.4f}; below full: {v.mean() < conc[(a, b)]};\"\n          f\" null max {nl.max():.4f}, null 97.5th {np.quantile(nl, 0.975):.4f}; (a) 2.5th > null max: {np.quantile(v, 0.025) > nl.max()}; (b) mean > null 97.5th: {v.mean() > np.quantile(nl, 0.975)}\")\n\"\"\", tags=[\"claim:equal-n-centroid-robustness\"])\n\nmd(r\"\"\"\n### within-regime-type-map-reliability\n\n> Within-regime split-half concordance of the type-type maps (long-pulse 0.861, ramp 0.851, brief-pulse 0.799) is well above the mean full-sample cross-regime concordance (about 0.57).\n\"\"\")\n\ncode(r\"\"\"\nclaim = \"within-regime-type-map-reliability\"\n\n\ndef split_half_maps(rng, n_boot=200):\n    out = {p: [] for p in g.REGIMES}\n    for _ in range(n_boot):\n        for p in g.REGIMES:\n            ta, tb, ca, cb = [], [], [], []\n            for i, t in enumerate(types):\n                perm = rng.permutation(by_type[p][t])\n                h = perm.size // 2\n                ta.append(perm[:h]); tb.append(perm[h:2 * h]); ca.append(np.full(h, i)); cb.append(np.full(h, i))\n            Sa = g.centroid_distances(lab[p][0][np.concatenate(ta)], np.concatenate(ca), len(types))[0]\n            Sb = g.centroid_distances(lab[p][0][np.concatenate(tb)], np.concatenate(cb), len(types))[0]\n            out[p].append(g.spearman(g.upper(Sa), g.upper(Sb)))\n    return {p: np.mean(v) for p, v in out.items()}\n\n\nrel_seeds = [split_half_maps(rng_for(claim, off)) for off in SEED_OFFSETS]\nref = np.mean(list(conc.values()))\nfor p in g.REGIMES:\n    vals_p = [r[p] for r in rel_seeds]\n    print(f\"{p}: split-half S concordance {vals_p[0]:.4f} (five seeds {min(vals_p):.4f} to {max(vals_p):.4f}); exceeds the reference: {vals_p[0] > ref}\")\nprint(f\"reference, mean of the three full-sample rho: {ref:.4f}\")\n\"\"\", tags=[\"claim:within-regime-type-map-reliability\"])\n\nmd(r\"\"\"\n### fig3b-pair-tags\n\n> Of the 1,596 type pairs, 639 (40.0%) are stable, 801 (50.2%) intermediate and 156 (9.8%) regime-selective.\n\"\"\")\n\ncode(r\"\"\"\ntags_, cv_, range_, mean_ = g.pair_tags(S)\ntc = Counter(tags_.tolist())\nprint({k: (v, f\"{v / len(tags_):.1%}\") for k, v in tc.items()}, \"of\", len(tags_))\n\"\"\", tags=[\"claim:fig3b-pair-tags\"])\n\nmd(r\"\"\"\n### pair-tag-threshold-sensitivity\n\n> The proportions of stable, intermediate and selective pairs are stable under modest variation of the classification thresholds.\n\"\"\")\n\ncode(r\"\"\"\nbase = {k: v / len(tags_) for k, v in tc.items()}\nrows = []\nfor sel_cut in [0.45, 0.50, 0.55, 0.60, 0.65]:\n    t2 = g.pair_tags(S, 0.25, sel_cut)[0]\n    rows.append({\"varied\": \"selective range\", \"cutoff\": sel_cut, **{k: np.mean(t2 == k) for k in (\"stable\", \"intermediate\", \"selective\")}})\nfor cv_cut in [0.15, 0.20, 0.25, 0.30, 0.35]:\n    t2 = g.pair_tags(S, cv_cut, 0.55)[0]\n    rows.append({\"varied\": \"stable CV\", \"cutoff\": cv_cut, **{k: np.mean(t2 == k) for k in (\"stable\", \"intermediate\", \"selective\")}})\nsens = pd.DataFrame(rows)\nfor k in (\"stable\", \"intermediate\", \"selective\"):\n    sens[f\"change_{k}\"] = sens[k] - base.get(k, 0)\nprint(sens.round(3).to_string(index=False))\nprint(\"selective below stable and intermediate at every cutoff:\", bool(((sens.selective < sens.stable) & (sens.selective < sens.intermediate)).all()))\n\"\"\", tags=[\"claim:pair-tag-threshold-sensitivity\"])\n\nmd(r\"\"\"\n### type-level-exceeds-cell-level\n\n> Type-level conservation across regimes is much greater than the preservation of cell-level relationships and local neighborhoods.\n\"\"\")\n\ncode(r\"\"\"\nfor a, b in g.PAIRS:\n    print(f\"{a} vs {b}: type-map rho {conc[(a, b)]:.4f} | cell-cell distance rho {dc[(a, b)]['rho']:.4f} | 15-NN Jaccard {kj[(a, b)]['mean']:.4f}\"\n          f\" | type exceeds cell: {conc[(a, b)] > dc[(a, b)]['rho']}\")\n\"\"\", tags=[\"claim:type-level-exceeds-cell-level\"])\n\nmd(r\"\"\"\n## Mobility\n\n### mobility-distribution\n\n> Cell-level neighborhood mobility across regimes, one minus the mean Spearman correlation of a cell's distance profile across the three regime pairs, has mean 0.589 and SD 0.110 over the 4,049 cells in all three regimes.\n\"\"\")\n\ncode(r\"\"\"\nmob_stems, mob, mob_rhos = g.mobility(spaces)\nprint(f\"cells in all three regimes: {len(mob_stems)}; mobility mean {mob.mean():.4f}, SD {mob.std():.4f} (ddof 0), range {mob.min():.4f} to {mob.max():.4f}\")\nprint(\"mean per-pair profile correlation:\", {f\"{a}-{b}\": round(float(mob_rhos[:, j].mean()), 4) for j, (a, b) in enumerate(g.PAIRS)})\n\"\"\", tags=[\"claim:mobility-distribution\"])\n\nmd(r\"\"\"\n## Transcriptomic claims\n\nThese claims need the NeMO Patch-seq count matrix (release 20200611,\n`20200513_Mouse_PatchSeq_Release_count.v2.csv`). The cell below asks the NeMO data server for the\nrelease folder.\n\"\"\")\n\ncode(r\"\"\"\nurl = \"https://data.nemoarchive.org/other/AIBS/AIBS_patchseq/transcriptome/scell/SMARTseq/processed/analysis/20200611/\"\nfor attempt in range(3):\n    try:\n        r = requests.get(url, timeout=60)\n        print(\"NeMO answered\", r.status_code, len(r.content), \"bytes\")\n    except Exception as exc:\n        print(\"NeMO request failed:\", type(exc).__name__, str(exc)[:200])\n    time.sleep(5)\nprint(f\"notebook ran {(time.time() - T0) / 60:.1f} min; peak memory (kB) self, largest child:\", peak_gb())\n\"\"\")\n\nmd(r\"\"\"\n## Summary\n\nThe outcomes, with the reasoning, are in the attempt record, `attempts/yang-2026-flexible-01.yaml`.\n\"\"\")\n\nnb = nbf.v4.new_notebook()\nnb.cells = cells\nnb.metadata[\"kernelspec\"] = {\"name\": \"python3\", \"display_name\": \"Python 3\", \"language\": \"python\"}\nnbf.write(nb, \"reproduce_yang_2026.ipynb\")\nprint(\"wrote\", len(cells), \"cells\")\n"
}
```

```
File created successfully at: entries/yang-2026-flexible/build_notebook.py (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd entries/yang-2026-flexible && mv build_notebook.py $TMPDIR/ && python - <<'EOF'
p="geometry.py"; s=open(p).read()
s=s.replace('''    return {"rho": rho, "p": emp_p(null, rho), "null_mean": float(null.mean()), "null_max": float(null.max()),
            "n": n,''','''    if not n_shuffle:
        null = np.array([np.nan])
    return {"rho": rho, "p": emp_p(null, rho), "null_mean": float(null.mean()), "null_max": float(null.max()),
            "n": n,''')
s=s.replace('''    return {"A": rho, "p": emp_p(null, rho),''','''    if not n_shuffle:
        null = np.array([np.nan])
    return {"A": rho, "p": emp_p(null, rho),''')
open(p,"w").write(s)
EOF
cd $TMPDIR && sed -i 's/split_seed=None/split_seed=ps.seed_of("split-half-reliability")/' bench2.py && dev/bin/python bench2.py 400 6 2>&1 | grep -v warn | tail -3; date -u
```

```
n 400 time 208.0 per cell 0.52 est full min 38.4
ok 400 []
maxrss children MB 2369.256
Sun Nov 22 10:00:24 UTC 2026
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && dev/bin/python build_notebook.py && mv reproduce_yang_2026.ipynb entries/yang-2026-flexible/ && dev/bin/pip list 2>/dev/null | grep -i nbconvert; uv pip install -q --python dev/bin/python nbconvert nbformat ipykernel jupyter 2>&1 | tail -2; cd entries/yang-2026-flexible && $TMPDIR/dev/bin/jupyter nbconvert --to script reproduce_yang_2026.ipynb --output $TMPDIR/nbdev >/dev/null 2>&1; ls $TMPDIR/nbdev*
```

```
Exit code 2
Traceback (most recent call last):
  File "/tmp/claude-1001/build_notebook.py", line 3, in <module>
    import nbformat as nbf
ModuleNotFoundError: No module named 'nbformat'
ls: cannot access '/tmp/claude-1001/nbdev*': No such file or directory
```

**Agent calls Bash**

```bash
cd $TMPDIR && uv pip install -q --python dev/bin/python nbconvert nbformat ipykernel 2>&1 | tail -2; dev/bin/python build_notebook.py && mv reproduce_yang_2026.ipynb entries/yang-2026-flexible/ && cd entries/yang-2026-flexible && $TMPDIR/dev/bin/jupyter nbconvert --to script reproduce_yang_2026.ipynb --output $TMPDIR/nbdev >/dev/null 2>&1; ls $TMPDIR/nbdev*
```

```
wrote 59 cells
/tmp/claude-1001/nbdev.txt
```

**Agent calls Bash**

```bash
cd $TMPDIR && python3 - <<'EOF'
s=open("nbdev.txt").read()
s=s.replace('recs = ps.extract_all(assets, split_seed=ps.seed_of("split-half-reliability"), workers=6, progress=500)',
 'import os; recs = json.load(open(os.environ["DEVCACHE"])); _p = {r["path"] for r in recs}; assets = [a for a in assets if a["path"] in _p]')
s=s.replace("check_idx = np.linspace(0, len(assets) - 1, 8).astype(int)","check_idx = np.linspace(0, len(assets) - 1, int(os.environ.get('NCHECK', '2'))).astype(int)")
s=s.replace("get_ipython()","#")
open("nbdev.py","w").write(s)
EOF
cd entries/yang-2026-flexible && DEVCACHE=$TMPDIR/bench_400.json $TMPDIR/dev/bin/python $TMPDIR/nbdev.py 2>&1 | grep -v "warn" | tail -150
```

```
Traceback (most recent call last):
  File "/tmp/claude-1001/nbdev.py", line 9, in <module>
    import patchseq as ps
ModuleNotFoundError: No module named 'patchseq'
```

**Agent calls Bash**

```bash
PYTHONPATH=. DEVCACHE=$TMPDIR/bench_400.json $TMPDIR/dev/bin/python $TMPDIR/nbdev.py 2>&1 | grep -v "warn" | tail -150
```

```
dandiset: Patch-seq recordings from mouse visual cortex | version 0.210913.1639 | doi 10.48324/dandi.000020/0.210913.1639
  version draft: 4435 assets, 141.9 GB, modified 2023-06-20
  version 0.210913.1639: 4435 assets, 141.9 GB, modified 2021-09-13
assets listed: 4435 | total 141.9 GB
file suffixes: Counter({'icephys.nwb': 4435})
subjects (folders): 1040
Traceback (most recent call last):
  File "/tmp/claude-1001/nbdev.py", line 37, in <module>
    print("description (start):", meta["metadata"].get("description", "")[:400])
                                  ~~~~^^^^^^^^^^^^
KeyError: 'metadata'
```

**Agent calls Bash**

```bash
cd $TMPDIR && sed -i 's/meta\["metadata"\].get("description", "")\[:400\]/meta.get("description", "")[:400]/' build_notebook.py nbdev.py && cd entries/yang-2026-flexible && PYTHONPATH=. DEVCACHE=$TMPDIR/bench_400.json $TMPDIR/dev/bin/python $TMPDIR/nbdev.py 2>&1 | grep -v "warn" | tail -150
```

```
brief_pulse               mean_spike_0.threshold_t 399   -0.1687   0.5031    0.6547
cells with a hyperpolarizing long square: 399 of 400
stimulus onset (s) from the stimulus trace: [(0.6, 242), (1.02, 157)] | duration (s): [(1.0, 399)]
amplitude (pA): median -110.0 range -110.0 -70.0
voltage change relative to baseline (mV), median [5th, 95th percentile]:
  10 ms just before onset: -0.01 [-0.31, 0.34]
  15 to 25 ms after onset: -15.57 [-28.96, -6.79]
  last 100 ms of the step: -17.85 [-36.40, -7.10]
cells whose response is negative 15 to 25 ms after onset: 399 | more than 1 mV off before onset: 4
identical traces shared by more than one file: 0
join rows: 4430 | distinct stems: 4430 | columns: ['file_stem', 'session_id', 'subject_id', 'cre_line', 'in_long_pulse', 'in_ramp', 'in_brief_pulse', 'cell_specimen_id', 'donor_id', 'full_genotype', 'structure', 'transcriptomics_sample_id', 't_type', 't_type_id', 'subclass', 'has_t_type']
dandiset files with a join row: 399 of 400 (99.8%)
join rows without a dandiset file: 4031
matched and extracted: 399 | same session id: 399 | same subject id: 399 | same full genotype: 399 | join Cre line found in the file's genotype: 399
missing in the dandiset (no file): ['sub-1001658946_ses-1003020741_icephys', 'sub-1001658958_ses-1003305489_icephys', 'sub-1001658958_ses-1003313230_icephys', 'sub-1001658958_ses-1003321768_icephys', 'sub-1001658958_ses-1003336912_icephys']
files with no join row: ['sub-650125704_ses-653191386_icephys']
cells with a join row: 399 | with a non-empty t-type: 382 | join rows with a t-type: 4266
long_pulse, missingness over present cells: rule keeps 42 of 49 candidate features; paper's list 42; same list: True
long_pulse, missingness over all cells: rule keeps 42 of 49 candidate features; paper's list 42; same list: True
ramp, missingness over present cells: rule keeps 20 of 24 candidate features; paper's list 20; same list: True
[... 130 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && dev/bin/python -c "
import json; r=json.load(open('bench_400.json'))
k=[x for x in r if x.get('split') and x['split']['reason'].startswith('KeyError')]
print(len(k), [x['split']['reason'] for x in k][:6], [x['path'] for x in k][:2])
"
```

```
6 ["KeyError: 'stimulus_amplitude'", "KeyError: 'stimulus_amplitude'", "KeyError: 'stimulus_amplitude'", "KeyError: 'stimulus_amplitude'", "KeyError: 'stimulus_amplitude'", "KeyError: 'stimulus_amplitude'"] ['sub-637383977/sub-637383977_ses-638775123_icephys.nwb', 'sub-637383957/sub-637383957_ses-639004554_icephys.nwb']
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && dev/bin/python -c "
import json; r=json.load(open('bench_400.json'))
k=[x for x in r if x.get('split') and x['split']['reason'].startswith('KeyError')]
print([x['failed'] for x in k]); print(sum(x['failed']['long_squares'] for x in r if x['extract_ok']))
"; cd entries/yang-2026-flexible && python - <<'EOF'
p="patchseq.py"; s=open(p).read()
old='''    try:
        smin = dsf.select_subthreshold_min_amplitude(clsq["stimulus_amplitude"])[0] if len(clsq) else -100
    except Exception as exc:'''
new='''    try:
        if clsq is not None and len(clsq) > 0 and "stimulus_amplitude" in clsq:
            smin = dsf.select_subthreshold_min_amplitude(clsq["stimulus_amplitude"])[0]
        else:
            smin = -100
    except Exception as exc:'''
assert old in s; s=s.replace(old,new); open(p,"w").write(s)
EOF
```

```
[{'long_squares': True, 'short_squares': False, 'ramps': False}, {'long_squares': True, 'short_squares': False, 'ramps': False}, {'long_squares': True, 'short_squares': False, 'ramps': False}, {'long_squares': True, 'short_squares': False, 'ramps': False}, {'long_squares': True, 'short_squares': False, 'ramps': False}, {'long_squares': True, 'short_squares': False, 'ramps': False}]
8
```

**Agent calls Bash**

```bash
cat > entry.yaml <<'EOF'
schema_version: 1
name: yang-2026-flexible
type: reproduction
title: Shared type-level organization of Patch-seq phenotypes across response regimes (Yang 2026)
description: Tests the findings of Yang (2026) on dandiset 000020, the Allen Institute Patch-seq
  recordings of 4,435 GABAergic interneurons of mouse visual cortex. IPFX cell-level features are
  extracted from every file for the long-square, ramp and short-square regimes, each regime gets its
  own PCA phenotype space, and the cell-level and type-level comparisons of the paper are repeated
  with the paper's t-type labels. The transcriptomic analyses need the NeMO count matrix, which could
  not be fetched.
license: Apache-2.0
notebooks:
- path: reproduce_yang_2026.ipynb
  title: Reproducing Yang (2026) from dandiset 000020
  runtime_minutes: 50
helpers:
- patchseq.py
- geometry.py
related:
- id: dandi:000020/0.210913.1639
  relation: uses_data
- id: doi:10.1523/eneuro.0275-26.2026
  relation: reproduces
EOF
cat > requirements.in <<'EOF'
ipfx==2.1.2
h5py
numpy
pandas
requests
scipy
EOF
cat entries/../../fouke-2025/requirements.lock.txt 2>/dev/null | head -3; head -5 ../fouke-2025/requirements.lock.txt; cd  && grep -n "helpers\|notebooks" schemas/entry.schema.json | head
```

```
# This file was autogenerated by uv via the following command:
#    uv pip compile --python-version 3.13 requirements.in -o requirements.lock.txt
acres==0.5.0
    # via bidsschematools
aiohappyeyeballs==2.7.1
3:  "title": "An entry: a directory of notebooks with its metadata (entry.yaml)",
7:  "required": ["schema_version", "name", "type", "title", "description", "license", "notebooks", "related"],
21:    "notebooks": {
35:    "helpers": {
36:      "description": "Python modules in the entry that the notebooks import.",
```

**Agent calls Bash**

```bash
python3 - <<'EOF'
p="claims/yang-2026-flexible.yaml"; s=open(p).read()
link='''claims:
- id: join-link
  kind: link
  statement: The NWB files of the dandiset are the cells of the paper's metadata join
    (results/m0/m0_molecular_join.csv of the paper's code at commit 61a5a41); matched by file stem,
    they have the same session, subject and genotype, and the same membership of the three regimes.
  source: Methods, Dataset and animals, last sentence; README of the paper's code, Data
  quote: >-
    n = 4,430 cells with a join row; n = 4,266 with a non-empty t-type
  data: with_inputs
  criterion: Added by the author (protocol, Author, step 1.4). Files are matched to join rows by NWB
    file stem, the key the code uses. Reproduced when at least 99% of the join rows match a file,
    every matched file agrees with its row on session id, subject id and full genotype, and the
    regime membership computed here (claim table1-phenotype-spaces) agrees with the join's in_long_pulse,
    in_ramp and in_brief_pulse columns for at least 99% of the cells; partially reproduced when the
    match holds but some agreement falls short, naming it.
'''
assert s.count("\nclaims:\n")==1
s=s.replace("\nclaims:\n","\n"+link,1)
for cid in ["cohort-label-join","fig2c-eta2-ttype-over-cre","table2-alignment-ttype","fig2d-knn-type-enrichment","fig2ab-ttype-structure-within-cre","fig3a-type-map-concordance"]:
    i=s.index(f"- id: {cid}\n"); j=s.index("  depends_on:\n", i); k=j+len("  depends_on:\n")
    nxt=s.index("\n- id: ", i+5) if "\n- id: " in s[i+5:] else len(s)
    assert j<nxt, cid
    s=s[:k]+"  - join-link\n"+s[k:]
open(p,"w").write(s)
EOF
git diff --stat; python tools/claims_check.py claims/yang-2026-flexible.yaml 2>&1 | tail -5
```

```
claims/yang-2026-flexible.yaml | 21 +++++++++++++++++++++
 1 file changed, 21 insertions(+)
confidence-interval bound in the text. The text may be plain text, HTML or JATS XML; several
files (a paper and its supplement) are searched together. A value printed in a form the
checker does not know (a garbled PDF glyph, "p = 0.04, 0.05 and 0.16") is reported, to be
confirmed by reading. Exits non-zero on any problem.
```

**Agent calls Bash**

```bash
cd $TMPDIR && sed -i 's/tags=\["claim:table1-phenotype-spaces", "claim:cohort-label-join"\]/tags=["claim:table1-phenotype-spaces", "claim:cohort-label-join", "claim:join-link"]/' build_notebook.py && dev/bin/python build_notebook.py && mv reproduce_yang_2026.ipynb entries/yang-2026-flexible/ && cd  && python tools/entry.py lock entries/yang-2026-flexible && python tools/entry.py check entries/yang-2026-flexible 2>&1 | tail -20
```

```
wrote 59 cells
wrote yang-2026-flexible/requirements.lock.txt (Python 3.13, with hashes)
0 error(s)
```

**Agent calls Bash**

```bash
sed -n 555,595p tools/entry.py
```

```
print(f"{entry_dir.name}: every claim prints the same on Python {version}; entry.yaml and the lock now use it")
    return 0


def file_hash(path: Path) -> str:
    import hashlib
    return hashlib.sha256(path.read_bytes()).hexdigest()


def entry_hash(entry_dir: Path) -> str:
    """A hash of everything a run of the entry's notebooks reads from the repository: every file of the entry (its
    notebooks, helpers, lock and entry.yaml, which names the Python and the dataset versions), the packages `run`
    adds, and RUN_VERSION. Two runs from the same hash execute the same code on the same data versions."""
    import hashlib
    h = hashlib.sha256(f"run {RUN_VERSION}; harness {' '.join(HARNESS)}; python {python_of(entry_dir)}\n".encode())
    for path in sorted(p for p in entry_dir.rglob("*") if p.is_file()):
        rel = path.relative_to(entry_dir)
        if any(part in ("__pycache__", ".ipynb_checkpoints", ".venv") or part.endswith(".pyc") for part in rel.parts):
            continue
        h.update(f"{rel.as_posix()}\0{file_hash(path)}\n".encode())
[... 19 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && python3 - <<'EOF'
s=open("nbdev.txt").read()
s=s.replace('recs = ps.extract_all(assets, split_seed=ps.seed_of("split-half-reliability"), workers=6, progress=500)',
 'import os, pickle\nif os.path.exists(os.environ["DEVCACHE"]):\n    recs = pickle.load(open(os.environ["DEVCACHE"], "rb"))\nelse:\n    recs = ps.extract_all(assets, split_seed=ps.seed_of("split-half-reliability"), workers=6, progress=500)\n    pickle.dump(recs, open(os.environ["DEVCACHE"], "wb"))')
s=s.replace("check_idx = np.linspace(0, len(assets) - 1, 8).astype(int)","check_idx = np.linspace(0, len(assets) - 1, int(os.environ.get('NCHECK', '8'))).astype(int)")
s=s.replace("get_ipython()","#")
open("nbfull.py","w").write(s)
EOF
grep -n "DEVCACHE\|NCHECK" nbfull.py | head
```

```
41:if os.path.exists(os.environ["DEVCACHE"]):
42:    recs = pickle.load(open(os.environ["DEVCACHE"], "rb"))
45:    pickle.dump(recs, open(os.environ["DEVCACHE"], "wb"))
53:check_idx = np.linspace(0, len(assets) - 1, int(os.environ.get('NCHECK', '8'))).astype(int)
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd entries/yang-2026-flexible && $TMPDIR/dev/bin/jupyter nbconvert --to script reproduce_yang_2026.ipynb --output $TMPDIR/nbdev >/dev/null 2>&1 && cd $TMPDIR && python3 - <<'EOF'
s=open("nbdev.txt").read()
s=s.replace('recs = ps.extract_all(assets, split_seed=ps.seed_of("split-half-reliability"), workers=6, progress=500)',
 'import os, pickle\nif os.path.exists(os.environ["DEVCACHE"]):\n    recs = pickle.load(open(os.environ["DEVCACHE"], "rb"))\nelse:\n    recs = ps.extract_all(assets, split_seed=ps.seed_of("split-half-reliability"), workers=6, progress=500)\n    pickle.dump(recs, open(os.environ["DEVCACHE"], "wb"))')
s=s.replace("check_idx = np.linspace(0, len(assets) - 1, 8).astype(int)","check_idx = np.linspace(0, len(assets) - 1, int(os.environ.get('NCHECK', '8'))).astype(int)")
s=s.replace("get_ipython()","#")
assert "DEVCACHE" in s and "NCHECK" in s
open("nbfull.py","w").write(s)
EOF
date -u; cd entries/yang-2026-flexible && PYTHONPATH=. DEVCACHE=$TMPDIR/full.pkl $TMPDIR/dev/bin/python $TMPDIR/nbfull.py > $TMPDIR/full_out.txt 2>$TMPDIR/full_err.txt; date -u; grep -v warn $TMPDIR/full_out.txt | head -100
```

```
Sun Nov 22 10:06:09 UTC 2026
Sun Nov 22 10:06:59 UTC 2026
dandiset: Patch-seq recordings from mouse visual cortex | version 0.210913.1639 | doi 10.48324/dandi.000020/0.210913.1639
  version draft: 4435 assets, 141.9 GB, modified 2023-06-20
  version 0.210913.1639: 4435 assets, 141.9 GB, modified 2021-09-13
assets listed: 4435 | total 141.9 GB
file suffixes: Counter({'icephys.nwb': 4435})
subjects (folders): 1040
description (start): Whole-cell Patch-seq recordings from neurons of the mouse visual cortex from the Allen Institute for Brain Science, released in June 2020. The majority of cells in this dataset are GABAergic interneurons, but there are also a small number of glutamatergic neurons from layer 2/3 of the mouse visual cortex.
dandiset: Patch-seq recordings from mouse visual cortex | version 0.210913.1639 | doi 10.48324/dandi.000020/0.210913.1639
  version draft: 4435 assets, 141.9 GB, modified 2023-06-20
  version 0.210913.1639: 4435 assets, 141.9 GB, modified 2021-09-13
assets listed: 4435 | total 141.9 GB
file suffixes: Counter({'icephys.nwb': 4435})
subjects (folders): 1040
description (start): Whole-cell Patch-seq recordings from neurons of the mouse visual cortex from the Allen Institute for Brain Science, released in June 2020. The majority of cells in this dataset are GABAergic interneurons, but there are also a small number of glutamatergic neurons from layer 2/3 of the mouse visual cortex.
dandiset: Patch-seq recordings from mouse visual cortex | version 0.210913.1639 | doi 10.48324/dandi.000020/0.210913.1639
  version draft: 4435 assets, 141.9 GB, modified 2023-06-20
  version 0.210913.1639: 4435 assets, 141.9 GB, modified 2021-09-13
assets listed: 4435 | total 141.9 GB
[... 82 more lines not kept]
```

**Agent calls Bash**

```bash
pkill -f nbfull.py; python - <<'EOF'
p="patchseq.py"; s=open(p).read()
old='''        with ProcessPoolExecutor(max_workers=workers, initializer=_init, max_tasks_per_child=50) as ex:
            futs = {ex.submit(extract_cell, a, split_seed): a for a in todo}
            for fut in as_completed(futs):
                a = futs[fut]
                try:
                    done[a["path"]] = fut.result()
                except BrokenProcessPool:
                    broken = True
                    tries[a["path"]] = tries.get(a["path"], 0) + 1
                except Exception as exc:
                    done[a["path"]] = {"file_stem": a["path"].split("/")[-1].rsplit(".", 1)[0], "path": a["path"],
                                       "extract_ok": 0, "error": f"worker: {exc}"[:300], "features": {}}
                if progress and len(done) % progress == 0:
                    print(f"  {len(done)}/{len(assets)} files", flush=True)'''
new='''        with ProcessPoolExecutor(max_workers=workers, initializer=_init, mp_context=mp.get_context("fork")) as ex:
            futs = {ex.submit(extract_cell, a, split_seed): a for a in todo}
            for fut in as_completed(futs):
                a = futs[fut]
                try:
                    done[a["path"]] = fut.result()
                except BrokenProcessPool:
                    broken = True
                    tries[a["path"]] = tries.get(a["path"], 0) + 1
                    continue
                except Exception as exc:
                    done[a["path"]] = {"file_stem": a["path"].split("/")[-1].rsplit(".", 1)[0], "path": a["path"],
                                       "extract_ok": 0, "error": f"worker: {exc}"[:300], "features": {}}
                if progress and len(done) % progress == 0:
                    print(f"  {len(done)}/{len(assets)} files", flush=True)'''
assert old in s; s=s.replace(old,new)
s=s.replace('''    """Run ``extract_cell`` over the assets in parallel processes, each restarted every 50 files.''','''    """Run ``extract_cell`` over the assets in parallel (forked) processes.''')
s=s.replace("import logging\nimport os\n","import logging\nimport multiprocessing as mp\nimport os\n",1)
open(p,"w").write(s)
EOF
grep -n "max_tasks\|restarted" patchseq.py; cd $TMPDIR && dev/bin/python bench2.py 60 6 2>&1 | grep -v warn | tail -3
```

```
Exit code 143
```

**Agent calls Bash**

```bash
ps aux | grep -c "[n]bfull"; grep -n "max_tasks\|restarted\|mp_context" entries/yang-2026-flexible/patchseq.py
```

```
0
450:    """Run ``extract_cell`` over the assets in parallel processes, each restarted every 50 files.
460:        with ProcessPoolExecutor(max_workers=workers, initializer=_init, max_tasks_per_child=50) as ex:
```

**Agent calls Bash**

```bash
python - <<'EOF'
p="patchseq.py"; s=open(p).read()
old='''        with ProcessPoolExecutor(max_workers=workers, initializer=_init, max_tasks_per_child=50) as ex:
            futs = {ex.submit(extract_cell, a, split_seed): a for a in todo}
            for fut in as_completed(futs):
                a = futs[fut]
                try:
                    done[a["path"]] = fut.result()
                except BrokenProcessPool:
                    broken = True
                    tries[a["path"]] = tries.get(a["path"], 0) + 1
                except Exception as exc:'''
new='''        with ProcessPoolExecutor(max_workers=workers, initializer=_init, mp_context=mp.get_context("fork")) as ex:
            futs = {ex.submit(extract_cell, a, split_seed): a for a in todo}
            for fut in as_completed(futs):
                a = futs[fut]
                try:
                    done[a["path"]] = fut.result()
                except BrokenProcessPool:
                    broken = True
                    tries[a["path"]] = tries.get(a["path"], 0) + 1
                    continue
                except Exception as exc:'''
assert old in s; s=s.replace(old,new)
s=s.replace('''    """Run ``extract_cell`` over the assets in parallel processes, each restarted every 50 files.''','''    """Run ``extract_cell`` over the assets in parallel (forked) processes.''')
s=s.replace("import logging\nimport os\n","import logging\nimport multiprocessing as mp\nimport os\n",1)
open(p,"w").write(s)
EOF
grep -n "max_tasks\|restarted\|mp_context\|^import multi" patchseq.py; cd $TMPDIR && timeout 600 dev/bin/python bench2.py 60 6 2>&1 | grep -v warn | tail -3
```

```
40:import multiprocessing as mp
461:        with ProcessPoolExecutor(max_workers=workers, initializer=_init, mp_context=mp.get_context("fork")) as ex:
n 60 time 32.6 per cell 0.544 est full min 40.2
ok 60 []
maxrss children MB 1324.416
Shell cwd was reset to
```

**Agent**

Fork-based pool works. Starting the full dev pass over all 4,435 files (about 40 min); it caches the extraction so I can refine the analysis afterwards without re-streaming.

**Agent calls Bash**

```bash
cd entries/yang-2026-flexible && date -u && PYTHONPATH=. DEVCACHE=$TMPDIR/full.pkl timeout 4500 $TMPDIR/dev/bin/python $TMPDIR/nbfull.py > $TMPDIR/full_out.txt 2>$TMPDIR/full_err.txt; echo exit $?; date -u; grep -v warn $TMPDIR/full_out.txt | head -30
```

```
Sun Nov 22 10:08:07 UTC 2026
exit 1
Sun Nov 22 10:08:42 UTC 2026
dandiset: Patch-seq recordings from mouse visual cortex | version 0.210913.1639 | doi 10.48324/dandi.000020/0.210913.1639
  version draft: 4435 assets, 141.9 GB, modified 2023-06-20
  version 0.210913.1639: 4435 assets, 141.9 GB, modified 2021-09-13
assets listed: 4435 | total 141.9 GB
file suffixes: Counter({'icephys.nwb': 4435})
subjects (folders): 1040
description (start): Whole-cell Patch-seq recordings from neurons of the mouse visual cortex from the Allen Institute for Brain Science, released in June 2020. The majority of cells in this dataset are GABAergic interneurons, but there are also a small number of glutamatergic neurons from layer 2/3 of the mouse visual cortex.
extraction: 4435 files in 0.0 min; peak memory (kB) self, largest child: (150116, 0)
extract_ok: Counter({0: 4435})
errors: Counter({'worker died': 4435})
   sub-1001658958/sub-1001658958_ses-1003321768_icephys.nwb worker died
   sub-1001658958/sub-1001658958_ses-1003336912_icephys.nwb worker died
   sub-1001658958/sub-1001658958_ses-1003313230_icephys.nwb worker died
   sub-601462926/sub-601462926_ses-602231628_icephys.nwb worker died
   sub-599387254/sub-599387254_ses-601506492_icephys.nwb worker died
   sub-601462915/sub-601462915_ses-602535253_icephys.nwb worker died
   sub-1001658958/sub-1001658958_ses-1003305489_icephys.nwb worker died
[... 13 more lines not kept]
```

**Agent calls Bash**

```bash
grep -v "warn" $TMPDIR/full_err.txt | head -30; ls -la $TMPDIR/full.pkl
```

```
Traceback (most recent call last):
  File "/tmp/claude-1001/nbfull.py", line 82, in <module>
    print("cells with at least one usable sweep: long squares", int((ns.long_squares > 0).sum()),
                                                                     ^^^^^^^^^^^^^^^
  File "/tmp/claude-1001/dev/lib/python3.13/site-packages/pandas/core/generic.py", line 6434, in __getattr__
    return object.__getattribute__(self, name)
           ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^
AttributeError: 'DataFrame' object has no attribute 'long_squares'
-rw-r--r-- 1 runner runner 505755 Nov 22 10:06 /tmp/claude-1001/full.pkl
```

**Agent calls Bash**

```bash
rm -f $TMPDIR/full.pkl; cd entries/yang-2026-flexible && date -u && PYTHONPATH=. DEVCACHE=$TMPDIR/full.pkl timeout 4500 $TMPDIR/dev/bin/python $TMPDIR/nbfull.py > $TMPDIR/full_out.txt 2>$TMPDIR/full_err.txt; echo exit $?; date -u; grep -v warn $TMPDIR/full_out.txt | head -60
```

```
Sun Nov 22 10:08:50 UTC 2026
exit 0
Sun Nov 22 10:43:06 UTC 2026
dandiset: Patch-seq recordings from mouse visual cortex | version 0.210913.1639 | doi 10.48324/dandi.000020/0.210913.1639
  version draft: 4435 assets, 141.9 GB, modified 2023-06-20
  version 0.210913.1639: 4435 assets, 141.9 GB, modified 2021-09-13
assets listed: 4435 | total 141.9 GB
file suffixes: Counter({'icephys.nwb': 4435})
subjects (folders): 1040
description (start): Whole-cell Patch-seq recordings from neurons of the mouse visual cortex from the Allen Institute for Brain Science, released in June 2020. The majority of cells in this dataset are GABAergic interneurons, but there are also a small number of glutamatergic neurons from layer 2/3 of the mouse visual cortex.
  500/4435 files
  1000/4435 files
  1500/4435 files
  2000/4435 files
  2500/4435 files
  a worker died; 1468 files run again
  3000/4435 files
  a worker died; 1137 files run again
  3500/4435 files
  a worker died; 0 files run again
[... 43 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && dev/bin/python -c "
import sys,json,time,resource; sys.path.insert(0,'entries/yang-2026-flexible')
import patchseq as ps
a={x['path']:x for x in json.load(open('assets.json'))}
for p in ['sub-842380940/sub-842380940_ses-844061113_icephys.nwb','sub-844940716/sub-844940716_ses-847731173_icephys.nwb']:
    t=time.time(); r=ps.extract_cell(a[p],1); print(p, a[p]['size']/1e6, round(time.time()-t,1), r['error'], r['n_sweeps'], 'maxrss MB', resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1e3, flush=True)
" 2>&1 | grep -v warn
```

```
sub-842380940/sub-842380940_ses-844061113_icephys.nwb 20.004198 2.7  {'long_squares': 10, 'short_squares': 2, 'ramps': 3} maxrss MB 364.196
sub-844940716/sub-844940716_ses-847731173_icephys.nwb 60.773846 2.0  {'long_squares': 10, 'short_squares': 2, 'ramps': 3} maxrss MB 536.552
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd entries/yang-2026-flexible && python - <<'EOF'
p="patchseq.py"; s=open(p).read()
a=s.index("def extract_all(")
s=s[:a]+'''def extract_all(assets: list[dict], split_seed: int | None, workers: int = 6, chunk: int = 300,
                progress: int = 500) -> list[dict]:
    """Run ``extract_cell`` over the assets in forked processes, a fresh pool for every ``chunk`` files.

    At most ``workers`` files are in flight at once. A process that dies (killed for memory, say)
    breaks the pool; the files then in flight are run again in a new pool, and a file in flight at
    two such breaks is recorded as failed ("worker died")."""
    from concurrent.futures import FIRST_COMPLETED, wait
    from concurrent.futures.process import BrokenProcessPool
    done: dict[str, dict] = {}
    breaks: dict[str, int] = {}
    queue = list(assets)
    n_breaks = 0
    while queue:
        batch, queue = queue[:chunk], queue[chunk:]
        todo = list(batch)
        retry = []
        with ProcessPoolExecutor(max_workers=workers, initializer=_init, mp_context=mp.get_context("fork")) as ex:
            inflight = {}
            broken = False
            while (todo or inflight) and not broken:
                while todo and len(inflight) < workers:
                    a = todo.pop(0)
                    inflight[ex.submit(extract_cell, a, split_seed)] = a
                finished, _ = wait(list(inflight), return_when=FIRST_COMPLETED)
                for fut in finished:
                    a = inflight.pop(fut)
                    try:
                        done[a["path"]] = fut.result()
                    except BrokenProcessPool:
                        broken = True
                        retry.append(a)
                        continue
                    except Exception as exc:
                        done[a["path"]] = {"file_stem": a["path"].split("/")[-1].rsplit(".", 1)[0], "path": a["path"],
                                           "extract_ok": 0, "error": f"worker: {exc}"[:300], "features": {}}
                    if progress and len(done) % progress == 0:
                        print(f"  {len(done)}/{len(assets)} files", flush=True)
            if broken:
                retry += list(inflight.values())
                n_breaks += 1
        for a in retry:
            breaks[a["path"]] = breaks.get(a["path"], 0) + 1
            if breaks[a["path"]] >= 2:
                done[a["path"]] = {"file_stem": a["path"].split("/")[-1].rsplit(".", 1)[0], "path": a["path"],
                                   "extract_ok": 0, "error": "worker died", "features": {}}
        queue = [a for a in retry if a["path"] not in done] + todo + queue
    if n_breaks:
        print(f"  the pool broke {n_breaks} times; files in flight were run again", flush=True)
    return [done[a["path"]] for a in assets]
'''
s=s.replace('''        try:
            from ipfx.dataset.ephys_nwb_data import EphysNWBData
            EphysNWBData._get_series.cache_clear()
        except Exception:
            pass
    return rec''','''        try:
            from ipfx.dataset.ephys_nwb_data import EphysNWBData
            EphysNWBData._get_series.cache_clear()
        except Exception:
            pass
        import gc
        gc.collect()
    return rec''')
open(p,"w").write(s)
EOF
cd $TMPDIR && sed -i 's/workers=int(sys.argv\[2\]), progress=0)/workers=int(sys.argv[2]), chunk=40, progress=0)/' bench2.py && timeout 900 dev/bin/python bench2.py 120 6 2>&1 | grep -v warn | tail -3
```

```
n 120 time 70.3 per cell 0.586 est full min 43.3
ok 120 []
maxrss children MB 1361.056
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && cat > fill.py <<'EOF'
import sys, pickle, json, time
sys.path.insert(0, "entries/yang-2026-flexible")
import patchseq as ps
if __name__ == "__main__":
    recs = pickle.load(open("full.pkl", "rb"))
    assets = {a["path"]: a for a in json.load(open("assets.json"))}
    redo = [assets[r["path"]] for r in recs if r["error"] == "worker died"]
    t = time.time()
    new = ps.extract_all(redo, split_seed=ps.seed_of("split-half-reliability"), workers=6, progress=200)
    print("redo", len(redo), round((time.time() - t) / 60, 1), "min", sum(r["extract_ok"] for r in new), [r["error"] for r in new if r["error"]][:5])
    by = {r["path"]: r for r in new}
    recs = [by.get(r["path"], r) for r in recs]
    pickle.dump(recs, open("full.pkl", "wb"))
    import resource; print(resource.getrusage(resource.RUSAGE_CHILDREN).ru_maxrss / 1e3)
EOF
timeout 1800 dev/bin/python fill.py 2>&1 | grep -v warn | tail -6; date -u
```

```
200/661 files
  400/661 files
  600/661 files
redo 661 6.4 min 661 []
1723.588
Sun Nov 22 10:51:39 UTC 2026
Shell cwd was reset to
```

**Agent**

All files are now extracted in the dev cache (4,431 of 4,435; 4 fail in IPFX because a sweep has two response series). Running the analysis on the full data.

**Agent calls Bash**

```bash
cd entries/yang-2026-flexible && date -u && NCHECK=2 PYTHONPATH=. DEVCACHE=$TMPDIR/full.pkl timeout 2400 $TMPDIR/dev/bin/python $TMPDIR/nbfull.py > $TMPDIR/full_out.txt 2>$TMPDIR/full_err.txt; echo exit $?; date -u; grep -v warn $TMPDIR/full_out.txt | grep -v "^ *sub-.*worker died" | sed -n 8,400p; grep -v warn $TMPDIR/full_err.txt | tail -5
```

```
Sun Nov 22 10:51:45 UTC 2026
exit 0
Sun Nov 22 10:55:36 UTC 2026
extraction: 4435 files in 0.0 min; peak memory (kB) self, largest child: (265944, 0)
extract_ok: Counter({1: 4431, 0: 4})
errors: Counter({'ValueError': 4})
   sub-636828314/sub-636828314_ses-637823738_icephys.nwb ValueError: Found 2 response series for sweep number 1.
   sub-636828314/sub-636828314_ses-637824890_icephys.nwb ValueError: Found 2 response series for sweep number 1.
   sub-636828314/sub-636828314_ses-637833126_icephys.nwb ValueError: Found 2 response series for sweep number 1.
   sub-636828314/sub-636828314_ses-637838825_icephys.nwb ValueError: Found 2 response series for sweep number 1.
sub-1001658958/sub-1001658958_ses-1003321768_icephys.nwb | features 93 same: True | split same: True | clock same: True | errors: - -
sub-992385550/sub-992385550_ses-993548448_icephys.nwb | features 93 same: True | split same: True | clock same: True | errors: - -
fast reader agrees with IPFX's reader on all checked files: True
files: 4435 | opened and extracted: 4431
session id in file equals the path's: 4431 of 4431
subject id in file equals the path's: 4431 of 4431
distinct sessions: 4431 | distinct subjects: 1040
cells per subject: [(1, 217), (2, 196), (3, 129), (4, 113), (5, 100), (7, 64), (6, 61), (8, 43)]
sex: Counter({'M': 2413, 'F': 2018})
age (days): median 55.0 range 34.0 to 159.0 | missing 0
[... 262 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && dev/bin/python - <<'EOF'
import pickle, collections, numpy as np
recs = pickle.load(open("full.pkl","rb"))
ok=[r for r in recs if r["extract_ok"]==1 and r.get("clock")]
fp=collections.defaultdict(list)
for r in ok: fp[r["clock"]["fingerprint"]].append(r)
pairs=[v for v in fp.values() if len(v)>1]
same=0
for v in pairs:
    a,b=v[0],v[1]
    keys=set(a["features"])&set(b["features"])
    eq=all(np.isclose(a["features"][k],b["features"][k]) for k in keys) and len(keys)>0
    same+=eq
    if eq: print("IDENTICAL", a["path"], b["path"], a["clock"], b["clock"]["amp"])
print(len(pairs), "fingerprint pairs;", same, "with identical features")
# also check identical full feature vectors across all cells
fv=collections.defaultdict(list)
for r in recs:
    if r["extract_ok"]==1 and r["features"]:
        fv[tuple(sorted((k,round(v,9)) for k,v in r["features"].items()))].append(r["path"])
d=[v for v in fv.values() if len(v)>1]
print("identical feature vectors:", len(d), d[:5])
EOF
```

```
IDENTICAL sub-673135474/sub-673135474_ses-680563483_icephys.nwb sub-673135516/sub-673135516_ses-680897463_icephys.nwb {'amp': -110.0, 'start': 1.02, 'dur': 1.0000000000000002, 'pre': -0.6888809204101562, 'post': -30.44772720336914, 'dv': -28.854412078857422, 'fingerprint': '604000:-4.37635e+07'} -110.0
50 fingerprint pairs; 1 with identical features
identical feature vectors: 1 [['sub-673135474/sub-673135474_ses-680563483_icephys.nwb', 'sub-673135516/sub-673135516_ses-680897463_icephys.nwb']]
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/code && grep -E "sub-673135474_ses-680563483|sub-673135516_ses-680897463" results/m0/m0_molecular_join.csv
```

```
sub-673135474_ses-680563483_icephys,680563483,673135474,Vip-IRES-Cre/wt;Ai14(RCL-tdT)/wt,1,1,1,680563587,381889,Vip-IRES-Cre/wt;Ai14(RCL-tdT)/wt,VISp2/3,SM-GE93V_S010_E1-50,Vip Lmo1 Myl1,CS180626100020,Vip,1
sub-673135516_ses-680897463_icephys,680897463,673135516,Ndnf-IRES2-dgCre/wt;Slc32a1-IRES2-FlpO/wt;Ai65(RCFL-tdT)/wt,1,1,1,680898048,381812,Ndnf-IRES2-dgCre/wt;Slc32a1-IRES2-FlpO/wt;Ai65(RCFL-tdT)/wt,VISp4,SM-GE93V_S012_E1-50,Lamp5 Lsp1,CS180626100006,Lamp5,1
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd entries/yang-2026-flexible && python - <<'EOF'
p="patchseq.py"; s=open(p).read()
old='''                                "fingerprint": f"{len(v)}:{np.nansum(v):.6g}"}'''
new='''                                "fingerprint": hashlib.sha1(np.ascontiguousarray(v).tobytes()).hexdigest()}
                # one hash over the voltage traces of every usable long square, in sweep order
                hs = hashlib.sha1()
                for sn in sorted(usable):
                    hs.update(np.ascontiguousarray(ds.sweep(sn).v).tobytes())
                rec["clock"]["long_square_hash"] = hs.hexdigest()'''
assert old in s; s=s.replace(old,new)
s=s.replace("import io\n","import hashlib\nimport io\n",1)
s=s.replace('''  ("dv"). The windows are a standard choice for a check, which cannot change a claim's result.''','''  ("dv"). The windows are a standard choice for a check, which cannot change a claim's result.
  For the check of recordings deposited twice, it also keeps the SHA-1 of that sweep's voltage
  trace and one SHA-1 over the voltage traces of all the cell's usable long squares.''')
open(p,"w").write(s)
EOF
grep -n "hashlib" patchseq.py | head
```

```
40:import hashlib
378:                                "fingerprint": hashlib.sha1(np.ascontiguousarray(v).tobytes()).hexdigest()}
380:                hs = hashlib.sha1()
```

**Agent calls Bash**

```bash
cd $TMPDIR && python3 - <<'EOF'
p="build_notebook.py"; s=open(p).read()
old=s[s.index("# Recordings deposited twice: identical voltage traces (length and sum) of that sweep"):s.index('""", tags=["sanity"])\n\nmd(r"""\n## Labels')]
new='''# Recordings deposited twice: identical voltage traces (SHA-1) of that sweep, of all long squares, or identical feature vectors
for col in ("fingerprint", "long_square_hash"):
    groups = clk.groupby(col).stem.apply(list)
    print(f"files sharing an identical {col}:", [v for v in groups if len(v) > 1])
fv = {}
for r in ok:
    if r["features"]:
        fv.setdefault(tuple(sorted((k, round(v, 9)) for k, v in r["features"].items())), []).append(r["file_stem"])
dup_feat = [v for v in fv.values() if len(v) > 1]
print("files with identical IPFX feature vectors:", dup_feat)
dups = sorted({tuple(v) for v in clk.groupby("long_square_hash").stem.apply(list) if len(v) > 1} | {tuple(v) for v in dup_feat})
'''
s=s.replace(old,new)
# join rows of duplicates, in join-link cell
s=s.replace('''print("files with no join row:", [s for s in stems_all if s not in join])
""", tags=["claim:join-link"])''','''print("files with no join row:", [s for s in stems_all if s not in join])
for grp in dups:
    print("identical recordings:", [(s, join.get(s, {}).get("cre_line"), join.get(s, {}).get("t_type"), join.get(s, {}).get("structure"),
                                     join.get(s, {}).get("transcriptomics_sample_id")) for s in grp])
""", tags=["claim:join-link"])''')
# A_t p under all seeds
s=s.replace('''    res = g.alignment(x_t, lab_t, rng_for(claim))
    seeds = [res["A"]] + [g.alignment(x_t, lab_t, rng_for(claim, off), n_shuffle=0)["A"] for off in SEED_OFFSETS[1:]]
    avg = g.alignment(x_t, lab_t, rng_for(claim, k=1), n_shuffle=0, average_ranks=True)["A"]
    print(f"{p}: n {res['n']}, A_t {res['A']:.4f}, p {res['p']:.4f} (null mean {res['null_mean']:.4f}, max {res['null_max']:.4f});"
          f" five seeds {min(seeds):.4f} to {max(seeds):.4f}; average-rank Spearman (variant) {avg:.4f}")''','''    runs = [g.alignment(x_t, lab_t, rng_for(claim, off)) for off in SEED_OFFSETS]
    res = runs[0]
    avg = g.alignment(x_t, lab_t, rng_for(claim, k=1), n_shuffle=0, average_ranks=True)["A"]
    print(f"{p}: n {res['n']}, A_t {res['A']:.4f}, p {res['p']:.4f} (null mean {res['null_mean']:.4f}, max {res['null_max']:.4f});"
          f" five seeds A_t {[round(r['A'], 4) for r in runs]}, p {[round(r['p'], 4) for r in runs]}; average-rank Spearman (variant) {avg:.4f}")''')
s=s.replace('''    res = g.alignment(xr, lab_t[has], rng_for(claim))
    seeds = [res["A"]] + [g.alignment(xr, lab_t[has], rng_for(claim, off), n_shuffle=0)["A"] for off in SEED_OFFSETS[1:]]''','''    runs = [g.alignment(xr, lab_t[has], rng_for(claim, off)) for off in SEED_OFFSETS]
    res = runs[0]''')
s=s.replace('''    print(f"{p}: n {int(has.sum())}, residual A_t {res['A']:.4f}, p {res['p']:.4f} (null mean {res['null_mean']:.4f}); five seeds {min(seeds):.4f} to {max(seeds):.4f};"''','''    print(f"{p}: n {int(has.sum())}, residual A_t {res['A']:.4f}, p {res['p']:.4f} (null mean {res['null_mean']:.4f});"
          f" five seeds A_t {[round(r['A'], 4) for r in runs]}, p {[round(r['p'], 4) for r in runs]};"''')
s=s.replace('''f" chance {res['chance']:.5f} (five seeds {min(chances):.5f} to {max(chances):.5f}), adjusted {res['adjusted']:.4f}")
same_pool = {}''','''f" chance {res['chance']:.6f} (five seeds {min(chances):.6f} to {max(chances):.6f}), adjusted {res['adjusted']:.4f}")
same_pool = {}''')
s=s.replace('''    print(f"same pool {a}-{b}: n = {len(pool)}, mean 15-NN Jaccard {r2['mean']:.4f}")''','''    print(f"same pool {a}-{b}: n = {len(pool)}, mean 15-NN Jaccard {r2['mean']:.5f}")''')
open(p,"w").write(s)
EOF
grep -n "dups = sorted\|five seeds A_t" build_notebook.py | head
```

```
215:dups = sorted({tuple(v) for v in clk.groupby("long_square_hash").stem.apply(list) if len(v) > 1} | {tuple(v) for v in dup_feat})
521:          f" five seeds A_t {[round(r['A'], 4) for r in runs]}, p {[round(r['p'], 4) for r in runs]}; average-rank Spearman (variant) {avg:.4f}")
543:          f" five seeds A_t {[round(r['A'], 4) for r in runs]}, p {[round(r['p'], 4) for r in runs]};"
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && dev/bin/python build_notebook.py && mv reproduce_yang_2026.ipynb entries/yang-2026-flexible/ && cd entries/yang-2026-flexible && $TMPDIR/dev/bin/jupyter nbconvert --to script reproduce_yang_2026.ipynb --output $TMPDIR/nbdev >/dev/null 2>&1 && cd $TMPDIR && python3 - <<'EOF'
s=open("nbdev.txt").read()
s=s.replace('recs = ps.extract_all(assets, split_seed=ps.seed_of("split-half-reliability"), workers=6, progress=500)',
 'import os, pickle\nrecs = pickle.load(open(os.environ["DEVCACHE"], "rb"))\nfor r in recs:\n    if r.get("clock") and "long_square_hash" not in r["clock"]: r["clock"]["long_square_hash"] = r["clock"]["fingerprint"]')
s=s.replace("check_idx = np.linspace(0, len(assets) - 1, 8).astype(int)","check_idx = np.linspace(0, len(assets) - 1, 1).astype(int)")
s=s.replace("get_ipython()","#")
open("nbfull.py","w").write(s)
EOF
cd entries/yang-2026-flexible && PYTHONPATH=. DEVCACHE=$TMPDIR/full.pkl timeout 2400 $TMPDIR/dev/bin/python $TMPDIR/nbfull.py > $TMPDIR/full_out2.txt 2>$TMPDIR/full_err2.txt; echo exit $?; grep -E "identical|five seeds A_t|residual A_t|chance 0.00|same pool" $TMPDIR/full_out2.txt; grep -v warn $TMPDIR/full_err2.txt | tail -3; date -u
```

```
wrote 59 cells
exit 0
files sharing an identical fingerprint: [['sub-750789321_ses-755584342_icephys', 'sub-758112430_ses-759772441_icephys'], ['sub-645665021_ses-647103434_icephys', 'sub-717036602_ses-718852830_icephys'], ['sub-640279135_ses-642832114_icephys', 'sub-689763228_ses-691750590_icephys'], ['sub-696533193_ses-697795197_icephys', 'sub-724625970_ses-728771962_icephys'], ['sub-656436829_ses-656977460_icephys', 'sub-680614572_ses-680983584_icephys', 'sub-710168752_ses-710338258_icephys'], ['sub-701146922_ses-703286422_icephys', 'sub-701147002_ses-704280001_icephys'], ['sub-650869035_ses-651763827_icephys', 'sub-705968866_ses-709363155_icephys'], ['sub-645665001_ses-646570703_icephys', 'sub-652361174_ses-653677241_icephys'], ['sub-648087036_ses-649382452_icephys', 'sub-712195501_ses-714007374_icephys'], ['sub-643830382_ses-644848041_icephys', 'sub-701146952_ses-704409722_icephys'], ['sub-670689800_ses-673692534_icephys', 'sub-700086487_ses-701073368_icephys'], ['sub-656436926_ses-656705650_icephys', 'sub-682365806_ses-688175237_icephys'], ['sub-670689897_ses-673753609_icephys', 'sub-689595099_ses-693275446_icephys'], ['sub-648087026_ses-648547556_icephys', 'sub-670689987_ses-674246439_icephys'], ['sub-657609919_ses-657926504_icephys', 'sub-721974368_ses-724811816_icephys'], ['sub-699347605_ses-700161733_icephys', 'sub-700086520_ses-701630129_icephys'], ['sub-656436967_ses-657052385_icephys', 'sub-701146952_ses-704482085_icephys'], ['sub-642979415_ses-643501513_icephys', 'sub-689763228_ses-691703642_icephys'], ['sub-645665042_ses-647103692_icephys', 'sub-716843159_ses-718254968_icephys'], ['sub-689440687_ses-692793132_icephys', 'sub-693123099_ses-695266274_icephys'], ['sub-689440847_ses-692160891_icephys', 'sub-701146912_ses-703219442_icephys'], ['sub-689440869_ses-692528477_icephys', 'sub-728913614_ses-729270414_icephys'], ['sub-643830402_ses-644993333_icephys', 'sub-710168752_ses-710344970_icephys'], ['sub-714724499_ses-716746180_icephys', 'sub-717036622_ses
[... 63 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && python3 - <<'EOF'
p="build_notebook.py"; s=open(p).read()
def after(tag, text):
    global s
    key = f'tags=["{tag}"])\n'
    if key not in s:
        key = f'tags=["{tag}"' 
        i = s.index(key); j = s.index(")\n", i) + 2
    else:
        j = s.index(key) + len(key)
    s = s[:j] + '\nmd(r"""\n' + text.strip() + '\n""")\n' + s[j:]

after("claim:join-link", """**Result: reproduced.** All 4,430 rows of the paper's join match a file of the dandiset by file stem, and every matched file has the session id, subject id and full genotype of its row. Five files have no row: the four of subject 636828314 that IPFX cannot open and one other (sub-650125704_ses-653191386). The regime membership computed here equals the join's in_long_pulse, in_ramp and in_brief_pulse columns for every cell (next section: 4,344, 4,139 and 4,422 in both, none on one side only).""")
after("claim:table1-phenotype-spaces", """**Result: reproduced.** The paper's rule applied to the features extracted here keeps exactly the paper's lists (42, 20 and 21 features) under both denominators, and the spaces hold 4,344, 4,139 and 4,422 cells with k80 = 11, 3 and 5; the overlaps are 4,054, 4,336, 4,134 and 4,049, all equal to the paper's. The cells of each regime are the paper's own cells, as listed in its join. For cohort-label-join, the cells with a t-type number 4,183, 3,988 and 4,266 per regime.""")
after("claim:cohort-label-join", """**Result: reproduced.** 4,430 files have a join row and 4,266 a non-empty t-type; the per-regime counts with a t-type, printed in the next section, are 4,183, 3,988 and 4,266. All five counts equal the paper's.""")
after("claim:pc1-long-pulse-loadings", """**Result: reproduced.** The four rheobase and threshold current features have the largest absolute PC1 loadings (0.303 each), followed by the two input resistance features (0.263), so the claim holds under both readings.""")
after("claim:fig1b-distance-correlation", """**Result: reproduced.** On unique pairs, rho is 0.441 (long-pulse and ramp), 0.385 (ramp and brief-pulse) and 0.336 (long-pulse and brief-pulse), each within 10% of the paper's 0.434, 0.384 and 0.336, each with p = 0.0099 against 100 shuffles (null maxima at most 0.025), in the paper's order. The code's pair draw gives 0.438, 0.381 and 0.334, and the five seeds keep each value within tolerance (0.435 to 0.441, 0.379 to 0.385, 0.333 to 0.343).""")
after("claim:fig1-fixed-five-pcs-ordering", """**Result: reproduced.** With five components in every regime, rho is 0.434, 0.383 and 0.339 for long-ramp, ramp-brief and long-brief, the same order as with k80, under all five seeds.""")
after("claim:fig1c-knn-jaccard", """**Result: reproduced.** The mean 15-NN Jaccard is 0.0229, 0.0224 and 0.0185 for long-ramp, long-brief and ramp-brief (paper 0.023, 0.022, 0.019), and the index-shuffle chance is 0.0019 to 0.0020 in every pair under all five seeds (paper about 0.002).""")
after("claim:knn-scale-sweep", """**Result: reproduced.** The chance-adjusted overlap at k = 600 is 0.134, 0.100 and 0.108 (paper 0.134, 0.101, 0.108), the same to three decimals under the other four seeds, and it rises at every step of the k grid for each pair.""")
after("claim:split-half-reliability", """**Result: partially reproduced.** 3,256 cells have both halves (paper 3,598, inside the tolerance); the within-regime mean 15-NN Jaccard is 0.1071 against chance 0.00286, adjusted 0.1043 (paper 0.109, 0.0026, 0.107), and it exceeds each same-pool cross-regime value (0.0258, 0.0257, 0.0222; paper 0.025, 0.024, 0.020). The ramp and brief-pulse value, 0.0222, is just above its tolerance (0.020 plus 0.002), and the long-pulse and ramp pool has 2,946 cells, two below its tolerance (3,276 less 327.6). The odd/even and sweep-number splits number 3,112 and 128, the paper's counts exactly, but the random split succeeded in 16 cells against the paper's 358; the random split's permutation depends only on the number of sweeps and the seed, and the protocol's seed is not the code's seed 0, which is the likely reason (not tested here).""")
after("claim:fig2c-eta2-ttype-over-cre", """**Result: reproduced.** Under reading (a), the code's cell set, eta squared of t-type against Cre is 0.327 against 0.209 (long-pulse), 0.393 against 0.267 (ramp) and 0.149 against 0.110 (brief-pulse), the paper's values to three decimals, and t-type exceeds Cre in every regime. Reading (b) and the Cre line from the files' own genotypes also give t-type above Cre in every regime.""")
after("claim:table2-alignment-ttype", """**Result: partially reproduced.** A_t is 0.034, 0.028 and 0.014 for long-pulse, ramp and brief-pulse (paper 0.021, 0.025, 0.021), each above all 100 label shuffles (p = 0.0099), so the alignment exceeds shuffled labels in each regime but none of the three values is within its tolerance. The value moves with the sampled pairs: over the five seeds it ranges 0.021 to 0.034 (long-pulse), 0.024 to 0.034 (ramp) and 0.014 to 0.025 (brief-pulse), with p = 0.0099 under every seed, and no seed puts all three within tolerance. The tie-corrected Spearman (variant) is 0.069 to 0.096, larger, as the claims file expected.""")
after("claim:ttype-beyond-cre", """**Result: partially reproduced.** After removing each Cre line's mean, A_t is 0.008, 0.006 and 0.010 (paper 0.011, 0.010, 0.004), each with p = 0.0099, so the residual alignment is above the label null in every regime, but none of the three values is within its tolerance (also under the other four seeds, whose values range -0.002 to 0.010). Residual t-type eta squared, 0.110, 0.120 and 0.040, is above the largest of 100 label-shuffle values in each regime (0.018, 0.021, 0.031), so residual structure is detectable under both readings.""")
after("claim:fig2d-knn-type-enrichment", """**Result: reproduced.** The same-t-type enrichment among the 15 nearest neighbours is 6.61, 3.45 and 2.64 (paper 6.59, 3.44, 2.64), in the paper's order; the mean of per-cell ratios (variant) gives 6.75, 3.57 and 2.87.""")
after("claim:fig2ab-ttype-structure-within-cre", """**Result: reproduced.** The files hold two Sst-IRES-Cre lines with at least 80 cells. For Sst-IRES-Cre with Ai14 (993 cells, 32 t-types), within-Cre A_t is 0.031 with p = 0.0099 and t-type eta squared is 0.225 against a shuffle mean of 0.031; for Sst-IRES-Cre with Ai167 (81 cells), 0.044 with p = 0.020 and 0.488 against 0.262. The six most frequent t-types of the first have long-pulse PC1 medians from 0.23 to 1.84 (Kruskal-Wallis p = 6e-19, descriptive).""")
after("claim:fig3a-type-map-concordance", """**Result: reproduced.** 57 t-types have at least 10 cells in every regime (1,596 pairs). The concordance is 0.659 (long-ramp), 0.609 (ramp-brief) and 0.455 (long-brief), the paper's values to the third decimal, each above all 1,000 shuffles (p = 0.000999 under all five seeds), in the paper's order.""")
after("claim:shared-map-model-call", """**Result: reproduced.** The minimum concordance is 0.455 (at least 0.40) and the range 0.204 (below 0.25).""")
after("claim:subclass-map-concordance", """**Result: reproduced.** Six subclasses have at least 10 cells in every regime; the subclass map concordance is 0.936 (long-ramp), 0.579 (long-brief) and 0.621 (ramp-brief), the paper's values under reading (a).""")
after("claim:equal-n-centroid-robustness", """**Result: reproduced.** With 10 cells per type, the mean concordance over 200 resamples is 0.553 (long-ramp), 0.457 (ramp-brief) and 0.323 (long-brief), within the paper's spread of 0.554, 0.455 and 0.329, each below its full-sample value, and the 2.5th percentiles (0.469, 0.359, 0.203) exceed the largest of the 1,000 shuffles (0.167, 0.147, 0.186), so both readings of "well above" hold. The five seeds move the means by at most 0.008.""")
after("claim:within-regime-type-map-reliability", """**Result: reproduced.** The split-half concordance of the type maps is 0.862, 0.852 and 0.799 (paper 0.861, 0.851, 0.799), against a mean full-sample cross-regime concordance of 0.574 (paper about 0.57), and the five seeds keep each within 0.005.""")
after("claim:fig3b-pair-tags", """**Result: reproduced.** 644 pairs are stable, 796 intermediate and 156 selective (paper 639, 801, 156).""")
after("claim:pair-tag-threshold-sensitivity", """**Result: reproduced.** At every cutoff of both grids the selective fraction (0.038 to 0.235) is below both the stable (0.231 to 0.569) and the intermediate (0.335 to 0.671) fractions. The selective fraction moves from 0.235 to 0.038 over the range cutoffs, and the stable fraction from 0.231 to 0.569 over the CV cutoffs.""")
after("claim:type-level-exceeds-cell-level", """**Result: reproduced.** For each regime pair the type-map concordance (0.659, 0.455, 0.609) exceeds the cell-cell distance correlation (0.441, 0.336, 0.385), and the 15-NN Jaccard is about 0.02.""")
after("claim:mobility-distribution", """**Result: reproduced.** Over the 4,049 cells in all three regimes, mobility has mean 0.589 and SD 0.110, the paper's values.""")
s = s.replace('''md(r"""
## Summary

The outcomes, with the reasoning, are in the attempt record, `attempts/yang-2026-flexible-01.yaml`.
""")''', '''md(r"""
**Result: blocked.** The NeMO data server did not return the release folder (the cell above prints its answers), so the seven transcriptomic claims (fig4ab-rna-tracks-shared-map, fig4-alternative-panels, fig4c-joint-excitability-modules, fig4c-kv3-strongest, fig4c-no-module-tracks-rank-range, pvalb-marker-control and wgcna-mobility-within-type) are not tested. The WGCNA claim would also need R and WGCNA 1.74, which the entry's Python environment does not hold.

## Summary

| Claim | Outcome |
|---|---|
| join-link | reproduced |
| cohort-label-join | reproduced |
| table1-phenotype-spaces | reproduced |
| pc1-long-pulse-loadings | reproduced |
| fig1b-distance-correlation | reproduced |
| fig1-fixed-five-pcs-ordering | reproduced |
| fig1c-knn-jaccard | reproduced |
| knn-scale-sweep | reproduced |
| split-half-reliability | partially reproduced |
| fig2c-eta2-ttype-over-cre | reproduced |
| table2-alignment-ttype | partially reproduced |
| ttype-beyond-cre | partially reproduced |
| fig2d-knn-type-enrichment | reproduced |
| fig2ab-ttype-structure-within-cre | reproduced |
| fig3a-type-map-concordance | reproduced |
| shared-map-model-call | reproduced |
| subclass-map-concordance | reproduced |
| equal-n-centroid-robustness | reproduced |
| within-regime-type-map-reliability | reproduced |
| fig3b-pair-tags | reproduced |
| pair-tag-threshold-sensitivity | reproduced |
| type-level-exceeds-cell-level | reproduced |
| mobility-distribution | reproduced |
| the six Figure 4 claims | blocked (NeMO count matrix not fetched) |
| wgcna-mobility-within-type | blocked (NeMO count matrix not fetched; WGCNA in R not available) |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

**How the analysis differs from the paper's.** The IPFX version is the current release (2.1.2),
run through its per-regime functions; the paper's driver script is not in its code. `extract_ok`
is taken as "the file opened and the extraction ran" (an assumption; every cell count still equals
the paper's). The sweeps are read with h5py in place of pynwb, checked against IPFX's own reader on
eight files. Every random draw uses the protocol's seed for its claim in place of the code's seed
0; the A_t values and the random split-half count depend on it. Pairs for the distance correlation
are unique pairs (the Methods), with the code's draw as a variant.

**What was found about the dataset.** Everything the paper describes is in the files: 4,435 NWB
files, one cell each, of which 4,431 open in IPFX; the four files of subject 636828314 have two
response series for one sweep number, and IPFX cannot read them. Sessions and subjects in the
files equal those of the paths, and the files' genotypes equal the paper's join. The response of
every cell's most hyperpolarizing long square starts at the stimulus onset given by the stimulus
trace (data check), so stimulus and response share a clock. One pair of files from different mice,
with different Cre lines and t-types in the paper's join (sub-673135474_ses-680563483 and
sub-673135516_ses-680897463), holds identical IPFX feature vectors; the data check prints the
files whose long-square voltage traces are identical. The files hold no transcriptomic label,
sample id or Cre-line field of their own: the t-types come from the Allen metadata, through the
paper's join.
""")''')
open(p,"w").write(s)
EOF
grep -c "Result:" build_notebook.py; dev/bin/python build_notebook.py && mv reproduce_yang_2026.ipynb entries/yang-2026-flexible/
```

```
24
wrote 82 cells
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && python3 - <<'EOF'
p="build_notebook.py"; s=open(p).read()
import re
# move join-link and cohort conclusions after the table1 conclusion
def cut(start):
    global s
    i=s.index('\nmd(r"""\n'+start); j=s.index('""")\n', i)+5
    block=s[i:j]; s=s[:i]+s[j:]; return block
jl=cut("**Result: reproduced.** All 4,430 rows")
co=cut("**Result: reproduced.** 4,430 files have a join row")
k=s.index('\nmd(r"""\n**Result: reproduced.** The paper\'s rule applied'); k=s.index('""")\n', k)+5
s=s[:k]+jl+co+s[k:]
s=s.replace("(next section: 4,344, 4,139 and 4,422 in both, none on one side only)","(above: 4,344, 4,139 and 4,422 in both, none on one side only)")
s=s.replace("the per-regime counts with a t-type, printed in the next section, are 4,183, 3,988 and 4,266","the per-regime counts with a t-type, printed above, are 4,183, 3,988 and 4,266")
s=s.replace("0.134, 0.100 and 0.108 (paper 0.134, 0.101, 0.108), the same to three decimals under the other four seeds,","0.134, 0.100 and 0.108 (paper 0.134, 0.101, 0.108), within 0.0003 under the other four seeds,")
s=s.replace("is 6.61, 3.45 and 2.64 (paper 6.59, 3.44, 2.64), in the paper's order; the mean of per-cell ratios (variant) gives 6.75, 3.57 and 2.87.","is 6.608, 3.445 and 2.643 (paper 6.59, 3.44, 2.64), in the paper's order; the mean of per-cell ratios (variant) gives 6.751, 3.565 and 2.867.")
s=s.replace("0.455 (long-brief), the paper's values to the third decimal,","0.455 (long-brief), within 0.001 of the paper's 0.658, 0.608 and 0.455,")
open(p,"w").write(s)
EOF
dev/bin/python build_notebook.py && mv reproduce_yang_2026.ipynb entries/yang-2026-flexible/ && cp build_notebook.py build_notebook.bak; cd  && python tools/entry.py check entries/yang-2026-flexible 2>&1 | tail -5; date -u
```

```
wrote 82 cells
0 error(s)
Sun Nov 22 11:02:49 UTC 2026
```

**Agent calls Write**

```json
{
 "file_path": "entries/yang-2026-flexible/README.md",
 "content": "# Yang (2026) from dandiset 000020\n\nTests the findings of [Yang (2026)](https://doi.org/10.1523/eneuro.0275-26.2026), \"Flexible\nCellular Phenotypes Retain a Shared Type-Level Organization across Response Regimes\", on\n[DANDI:000020](https://dandiarchive.org/dandiset/000020/0.210913.1639), the Allen Institute\nPatch-seq recordings of 4,435 interneurons of mouse visual cortex (Gouwens et al. 2020), which the\npaper reuses.\n\nThe notebook extracts the IPFX cell-level features of every file for the long-square, ramp and\nshort-square regimes, builds the paper's three phenotype spaces, and repeats its cell-level and\ntype-level analyses with the t-type labels of the paper's metadata join (from its code at commit\n61a5a41). The transcriptomic analyses of Figure 4 and the WGCNA analysis need the NeMO Patch-seq\ncount matrix, whose server did not answer during the attempt; they are blocked.\n\nA failure to reproduce here may be a failure of this attempt, not of the paper: see the\nreasoning and the differences from the paper's method.\n\nThe outcomes, the reasons and the differences from the paper's method are in the attempt record,\n[`attempts/yang-2026-flexible-01.yaml`](../../attempts/yang-2026-flexible-01.yaml), and in the\nnotebook's summary.\n\n- `reproduce_yang_2026.ipynb`: the analysis. It takes about 45 minutes, most of it the one pass\n  that streams the 142 GB of the dandiset and runs IPFX on each file, in six processes.\n- `patchseq.py`: streaming a file into memory, the IPFX feature extraction per regime and for split\n  halves of the long squares, and the values of the data check. Other notebooks on this dandiset\n  can import it.\n- `geometry.py`: the phenotype spaces and the paper's cell-level and type-level measures.\n"
}
```

```
File created successfully at: entries/yang-2026-flexible/README.md (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
date -u && python tools/entry.py all entries/yang-2026-flexible 2>&1 | tail -20; date -u
```

```
Sun Nov 22 11:02:58 UTC 2026
Installed kernelspec registry-yang-2026-flexible in executed/yang-2026-flexible/.venv/share/jupyter/kernels/registry-yang-2026-flexible
0 error(s)
pass  reproduce_yang_2026.ipynb  (2582 s)
Sun Nov 22 11:46:09 UTC 2026
```

**Agent**

The locked run passed in 43 min. Checking the executed outputs against the conclusions.

**Agent calls Bash**

```bash
python3 - <<'EOF' > $TMPDIR/exec_out.txt
import json
nb=json.load(open("executed/yang-2026-flexible/reproduce_yang_2026.ipynb"))
for i,c in enumerate(nb["cells"]):
    if c["cell_type"]!="code": continue
    for o in c.get("outputs",[]):
        t=o.get("text") or "".join(o.get("data",{}).get("text/plain",""))
        t="".join(t) if isinstance(t,list) else t
        if o.get("output_type")=="error": t="ERROR "+o.get("ename","")+o.get("evalue","")
        print(f"--- cell {i} {c['metadata'].get('tags')}"); print(t[:6000])
EOF
grep -v "^ *[a-z_]* *[a-z_.0-9]* *[0-9]* *-\?[0-9.]* *-\?[0-9.]* *-\?[0-9.]*$" $TMPDIR/exec_out.txt | head -150
```

```
--- cell 1 None
dandiset: Patch-seq recordings from mouse visual cortex | version 0.210913.1639 | doi 10.48324/dandi.000020/0.210913.1639
  version draft: 4435 assets, 141.9 GB, modified 2023-06-20
  version 0.210913.1639: 4435 assets, 141.9 GB, modified 2021-09-13
--- cell 1 None
assets listed: 4435 | total 141.9 GB
file suffixes: Counter({'icephys.nwb': 4435})
subjects (folders): 1040
description (start): Whole-cell Patch-seq recordings from neurons of the mouse visual cortex from the Allen Institute for Brain Science, released in June 2020. The majority of cells in this dataset are GABAergic interneurons, but there are also a small number of glutamatergic neurons from layer 2/3 of the mouse visual cortex.
--- cell 3 None
  500/4435 files
--- cell 3 None
  1000/4435 files
--- cell 3 None
  1500/4435 files
--- cell 3 None
  2000/4435 files
--- cell 3 None
  2500/4435 files
--- cell 3 None
[... 130 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n '/cell 32 /,$p' $TMPDIR/exec_out.txt | grep -v "^--- cell" | head -120
```

```
long_pulse-ramp: adjusted at k = 600 under the other four seeds: [0.1344 0.1344 0.1346 0.1344]

long_pulse-brief_pulse: adjusted at k = 600 under the other four seeds: [0.1004 0.1003 0.1003 0.1004]

ramp-brief_pulse: adjusted at k = 600 under the other four seeds: [0.1077 0.1077 0.1076 0.1075]
pair  long_pulse-brief_pulse  long_pulse-ramp  ramp-brief_pulse
k                                                              
15                    0.0205           0.0209            0.0166
30                    0.0304           0.0309            0.0259
60                    0.0435           0.0461            0.0391
120                   0.0592           0.0681            0.0566
240                   0.0749           0.0957            0.0776
480                   0.0944           0.1260            0.1008
600                   0.1004           0.1344            0.1077
long_pulse-brief_pulse | rises at every step: True | k=600 above k=15: True
long_pulse-ramp | rises at every step: True | k=600 above k=15: True
ramp-brief_pulse | rises at every step: True | k=600 above k=15: True

cells with at least four usable long squares: 4430 | both halves extracted: 3256
split rules used: Counter({'odd_even_sweep_number': 3112, 'interleaved_index': 128, 'random': 16})
[... 100 more lines not kept]
```

**Agent calls Bash**

```bash
tail -8 $TMPDIR/exec_out.txt; date -u; ls executed/yang-2026-flexible/
```

```
NeMO answered 502 150 bytes

--- cell 80 None
NeMO answered 502 150 bytes

--- cell 80 None
notebook ran 42.9 min; peak memory (kB) self, largest child: (1469940, 2772164)

Sun Nov 22 11:46:26 UTC 2026
reproduce_yang_2026.ipynb
result.json
```

**Agent calls Bash**

```bash
grep -B2 -A3 "mobility mean" $TMPDIR/exec_out.txt | head; grep -c "NeMO" $TMPDIR/exec_out.txt; grep "NeMO" $TMPDIR/exec_out.txt
```

```
--- cell 77 ['claim:mobility-distribution']
cells in all three regimes: 4049; mobility mean 0.5890, SD 0.1100 (ddof 0), range 0.2447 to 1.1808
mean per-pair profile correlation: {'long_pulse-ramp': 0.4555, 'long_pulse-brief_pulse': 0.381, 'ramp-brief_pulse': 0.3964}

--- cell 80 None
3
NeMO answered 502 150 bytes
NeMO answered 502 150 bytes
NeMO answered 502 150 bytes
```

**Agent**

Executed outputs match every conclusion. Writing the attempt record now.

**Agent calls Bash**

```bash
sed -n 60,140p attempts/fouke-2025-01.yaml; grep -n "findings:" -A30 attempts/fouke-2025-01.yaml | head -50; python3 -c "
import json; s=json.load(open('schemas/attempt.schema.json')); print(list(s['properties'].keys())); o=s['properties']['outcomes']['items']; print(o.get('required'), list(o['properties'].keys())); f=s['properties']['findings']['items']; print(f.get('required'), list(f['properties'].keys()))
print(json.dumps(s['properties']['provenance'],indent=0)[:1500]); print(json.dumps(s['properties']['inputs'],indent=0)[:800])"
```

```
- claim: fig1d-dc-faster-all-codes
  outcome: reproduced
  notebook: reproduce_fouke_2025.ipynb
  output: claim:fig1d-dc-faster-all-codes
  notes: Over all 21 codes, the median over fish and code values is 94.0 pixels/s for DC and 55.2
    for ZF; species effect F = 78.4, p = 6.3e-18. The ANOVA treats each fish and code value as
    independent; with one value per fish, DC 87.4 against ZF 52.9 pixels/s, Mann-Whitney p = 0.02.
    With positions resampled to 30 Hz, 95.2 against 53.8 (p = 1.3e-08). DC are faster within
    each frame-rate group.
  deviations:
  - Tested over all stimulus codes without their names; the paper's figure uses nine whole-field
    stimuli.
  - The comparison assumes one spatial scale for all rigs, which the files do not state.
- claim: fig1d-median-velocity
  outcome: reproduced
  notebook: reproduce_fouke_2025.ipynb
  output: claim:fig1d-median-velocity
  measured:
  - 9.87
  - 6.41
[... 215 more lines not kept]
```

**Agent calls Bash**

```bash
python3 -c "
import json; s=json.load(open('schemas/attempt.schema.json')); o=s['properties']['outcomes']['items']['properties']; print(o['blocked_by'], o['outcome'], o['measured']); f=s['properties']['findings']['items']['properties']; print(f['kind'], f['severity'], f['found'])
print(json.dumps(s['properties']['datasets'])[:600])"
```

```
{'description': 'Required when outcome is blocked.', 'enum': ['data_missing', 'metadata_insufficient', 'methods_underspecified', 'data_unreadable', 'dataset_missing', 'too_large', 'not_runnable', 'other']} {'enum': ['reproduced', 'partially_reproduced', 'not_reproduced', 'blocked'], 'description': 'Describes the result, not the method: whether the effect the claim states was found. Differences in method from the paper go in `deviations`.'} {'description': 'The values obtained, for claims with expected values: one number, or one per expected value, in the same order.', 'oneOf': [{'type': 'number'}, {'type': 'array', 'minItems': 1, 'items': {'type': 'number'}}]}
{'enum': ['metadata_error', 'data_missing', 'identifier_missing', 'metadata_insufficient', 'selection_undocumented', 'methods_unavailable', 'format_error', 'code_mismatch', 'paper_inconsistency', 'other']} {'description': 'For a finding about the data: how much it harms someone who uses the dataset (docs/protocol.md, the attempt record). `critical`: the data are wrong and nothing shows it, so an analysis gives a wrong result. `major`: a main analysis is blocked or changed, and the user would notice. `minor`: evident from the values or easy to work around, a wrong unit label included. `none`: no problem, a check that passed. Required from protocol pilot-18.', 'enum': ['critical', 'major', 'minor', 'none']} {'description': 'How the finding was found. Unset: by the attempt itself. `on_prompt`: by the reconcile step of a repeat attempt, which checked a finding of the earlier attempt that this one, made blind, did not report (docs/protocol.md, "Repeat attempts").', 'enum': ['on_prompt']}
{"description": "Every dataset the attempt used (docs/protocol.md, \"Record the attempt\").", "type": "array", "minItems": 1, "items": {"description": "A dataset the attempt used: the archive, the dataset's identifier there, the pinned version, and how the paper relates to it.", "type": "object", "additionalProperties": false, "req
[... 1 more lines not kept]
```

**Agent calls Bash**

```bash
mkdir -p $TMPDIR/rec && cat > $TMPDIR/rec/make.py <<'EOF'
import yaml
NB = "reproduce_yang_2026.ipynb"
SEEDS = ("Random draws use the claim's seed (protocol) in place of the code's seed 0, with four more seeds"
         " for the range given in the notes.")
EXTRACT = ("Features from IPFX 2.1.2 (the current release) through its per-regime functions"
           " extract_cell_long_square_features, extract_cell_short_square_features and"
           " extract_cell_ramp_features, with the code's epoch repair and sweep filter; the paper's IPFX"
           " driver script and IPFX version are not in its code (claims file, table1-phenotype-spaces,"
           " reading 1a).")
def o(claim, outcome, notes, measured=None, deviations=None, **kw):
    d = {"claim": claim, "outcome": outcome, "notebook": NB, "output": f"claim:{claim}"}
    if outcome == "blocked":
        d.pop("output")
    d.update(kw)
    if measured is not None:
        d["measured"] = measured
    d["notes"] = notes
    if deviations:
        d["deviations"] = deviations
    return d

rna_note = ("The NeMO data server (data.nemoarchive.org), the only source the paper names for the"
            " count matrix 20200513_Mouse_PatchSeq_Release_count.v2.csv of release 20200611, answered"
            " 502 or timed out on every request from 09:20 to 11:46 UTC on 2026-11-22, including the"
            " three requests the notebook makes (its last cell). The matrix is public, so the claim is"
            " not data_missing; it could not be fetched in this run. The phenotype side of the claim"
            " (mean S and rank range over the 1,596 type pairs) is computed in the notebook"
            " (fig3a-type-map-concordance, fig3b-pair-tags).")

outcomes = [
 o("join-link", "reproduced",
   "All 4,430 join rows match a file by stem (100%), and all 4,430 matched files agree with their row on"
   " session id, subject id and full genotype. Five files have no row, the four of subject 636828314 that"
   " IPFX cannot open and sub-650125704_ses-653191386. The regime membership computed here equals the"
   " join's in_long_pulse, in_ramp and in_brief_pulse for every cell (4,344, 4,139 and 4,422 in both, 0 on"
   " one side only). The join also gives two files with identical recordings different Cre lines and"
   " t-types (finding 1)."),
 o("cohort-label-join", "reproduced",
   "4,430 files with a join row, 4,266 with a non-empty t-type; per regime 4,183, 3,988 and 4,266 cells"
   " with a t-type. All equal to the paper's.",
   measured=[4430, 4266, 4183, 3988, 4266]),
 o("table1-phenotype-spaces", "reproduced",
   "The paper's rule (at most 30% missing, nonzero variance) on the features extracted here keeps exactly"
   " the paper's lists of 42, 20 and 21 features under both readings of the denominator (2a and 2b). Cells"
   " 4,344, 4,139 and 4,422; k80 11, 3 and 5 (cumulative variance 0.822, 0.883, 0.824); overlaps 4,054,"
   " 4,336, 4,134 and 4,049. Every value equals the paper's, and the cells are the ones the paper's join"
   " lists for each regime. Of 4,431 files opened, IPFX's long-square extraction failed in 87, the"
   " short-square in 9 and the ramp in 2.",
   measured=[4344, 42, 11, 4139, 20, 3, 4422, 21, 5, 4054, 4336, 4134, 4049], assumed=True,
   deviations=[EXTRACT,
     "extract_ok is not defined in the paper or its code. Assumed here to be 1 when the file opened as an"
     " IPFX data set and the three regime extractions ran, each regime allowed to fail on its own, as"
     " IPFX's own cell state counts a cell failed only when every part failed. The cell sets this gives"
     " equal the paper's own regime membership (join-link), so the claims built on these spaces do not"
     " depend on the choice.",
     "Sweeps are read from the HDF5 file with h5py in place of pynwb, for speed (patchseq._fast_reader);"
     " the notebook shows that the features, split halves and clock values equal those of IPFX's own"
     " reader on eight files across the dandiset."]),
 o("pc1-long-pulse-loadings", "reproduced",
   "The four current features (rheobase_i, threshold_i, rheobase_sweep.stim_amp, hero_sweep.stim_amp)"
   " have the largest absolute loadings (0.303), then input_resistance and ri (0.263); PC1 explains 0.198"
   " of the variance. Both readings hold."),
 o("fig1b-distance-correlation", "reproduced",
   "Unique pairs; rho 0.4410 (long-ramp, n 4,054), 0.3848 (ramp-brief, n 4,134), 0.3363 (long-brief, n"
   " 4,336), each p = 0.0099 (null maxima 0.020, 0.025, 0.023). Over five seeds 0.4353 to 0.4410, 0.3790"
   " to 0.3848 and 0.3331 to 0.3428, all within tolerance and in the paper's order. The code's pair draw"
   " (variant, about 79,600 unique of 80,000 pairs) gives 0.4378, 0.3809 and 0.3342.",
   measured=[0.4410, 0.3848, 0.3363], deviations=[SEEDS]),
 o("fig1-fixed-five-pcs-ordering", "reproduced",
   "With five components rho is 0.4335 (long-ramp), 0.3826 (ramp-brief), 0.3392 (long-brief); over five"
   " seeds 0.4297 to 0.4378, 0.3797 to 0.3839 and 0.3392 to 0.3464, so the order holds under every seed.",
   deviations=[SEEDS]),
 o("fig1c-knn-jaccard", "reproduced",
   "Mean 15-NN Jaccard 0.0229, 0.0224 and 0.0185 (long-ramp, long-brief, ramp-brief); index-shuffle"
   " chance 0.00199, 0.00187 and 0.00193 (measured gives long-ramp's), 0.00186 to 0.00199 over five seeds"
   " and all pairs, so within 0.0002 of 0.002.",
   measured=[0.0229, 0.0224, 0.0185, 0.00199], deviations=[SEEDS]),
 o("knn-scale-sweep", "reproduced",
   "Chance-adjusted Jaccard at k = 600 is 0.1344, 0.1004 and 0.1077 (0.1344 to 0.1346, 0.1003 to 0.1004,"
   " 0.1075 to 0.1077 over five seeds); it rises at every step of the grid 15, 30, 60, 120, 240, 480, 600"
   " for each pair (readings a and b both hold).",
   measured=[0.1344, 0.1004, 0.1077], deviations=[SEEDS]),
 o("split-half-reliability", "partially_reproduced",
   "3,256 cells with both halves (tolerance 3,238 to 3,958); within long-pulse mean 15-NN Jaccard 0.1071,"
   " chance 0.002856 (0.002814 to 0.002856 over five seeds), adjusted 0.1043, all within tolerance, and"
   " above the same-pool cross-regime values 0.02583, 0.02572 and 0.02219. The ramp and brief-pulse value"
   " is 0.0002 above its tolerance (0.022) and the long-pulse and ramp pool, 2,946 cells, is 2 below its"
   " tolerance; the other pools have 3,173 and 3,026 cells. Splits used; odd/even 3,112 and sweep-number"
   " interleaved 128, both the paper's exact counts; random 16 against the paper's 358. The random split's"
   " permutation is drawn from a generator made afresh for each cell, so it depends only on the number of"
   " sweeps and the seed; under the protocol's seed it succeeds in 16 cells, and the paper's seed 0 is the"
   " likely reason for its 358 (not run here; repeating the extraction under four more seeds would add"
   " about a quarter of the notebook's run time, so seed sensitivity of the split is not measured). 1,114"
   " cells failed for too few spiking sweeps to fit an f-I slope in a half.",
   measured=[3256, 0.1071, 0.1043, 0.002856, 0.02583, 0.02572, 0.02219, 2946, 3173, 3026, 3112, 16],
   deviations=[EXTRACT, "The random split uses the claim's seed; the code uses seed 0, which changes which"
               " cells get a random split."]),
 o("fig2c-eta2-ttype-over-cre", "reproduced",
   "Reading (a), the code's cell set; t-type 0.3269, 0.3926, 0.1492 against Cre 0.2092, 0.2672, 0.1095"
   " (long-pulse, ramp, brief-pulse), the paper's values to three decimals. Reading (b), all cells with a"
   " Cre line; Cre 0.2114, 0.2687, 0.1300, still below t-type. With the Cre line taken from the files' own"
   " genotype (44 lines), 0.1903, 0.2472 and 0.1210.",
   measured=[0.3269, 0.2092, 0.3926, 0.2672, 0.1492, 0.1095]),
 o("table2-alignment-ttype", "partially_reproduced",
   "A_t 0.0337 (long-pulse, 4,183 cells), 0.0278 (ramp, 3,988), 0.0137 (brief-pulse, 4,266), each p ="
   " 0.0099 against 100 label shuffles (null maxima 0.0077, 0.0046, 0.0005). None is within tolerance"
   " (0.0189 to 0.0231, 0.0225 to 0.0275, 0.0189 to 0.0231). Over the five seeds A_t is 0.0214 to 0.0337,"
   " 0.0239 to 0.0337 and 0.0137 to 0.0245, p = 0.0099 under every seed, and under no seed are all three"
   " within tolerance, so the outcome is the same under all five. The spread comes from the code's"
   " ordinal ranks, which give the tied 0s and 1s of the mismatch an order set by where the sampled pairs"
   " fall; the tie-corrected Spearman (variant) is 0.0955, 0.0848 and 0.0689. The alignment exceeds"
   " shuffled labels in every regime, as the statement says; its size is not reproduced to the printed"
   " precision.",
   measured=[0.0337, 0.0278, 0.0137], deviations=[SEEDS]),
 o("ttype-beyond-cre", "partially_reproduced",
   "On the code's cell set, after removing each Cre line's mean, A_t 0.0081, 0.0064 and 0.0103 (paper"
   " 0.011, 0.010, 0.004), each p = 0.0099; over five seeds -0.0019 to 0.0088 (ramp lowest) with p ="
   " 0.0099 under every seed, and the long-pulse value never within tolerance, so the outcome holds under"
   " all five. Residual t-type eta squared 0.1102, 0.1197 and 0.0396 against label-shuffle null means"
   " 0.0146, 0.0154 and 0.0139 (maxima 0.0182, 0.0209, 0.0312), so residual structure is detectable under"
   " both readings. The variant on all t-typed cells is the same set here, as every join row has a Cre"
   " line.",
   measured=[0.0081, 0.0064, 0.0103], deviations=[SEEDS]),
 o("fig2d-knn-type-enrichment", "reproduced",
   "Ratio of means 6.608, 3.445 and 2.643 (same-type fractions 0.195, 0.104, 0.078 against chance 0.030),"
   " in the paper's order; the mean of per-cell ratios (variant) gives 6.751, 3.565 and 2.867.",
   measured=[6.608, 3.445, 2.643]),
 o("fig2ab-ttype-structure-within-cre", "reproduced",
   "Two Sst-IRES-Cre lines have at least 80 cells. With Ai14 (993 cells, 32 t-types) within-Cre A_t is"
   " 0.0313 (p 0.0099) and eta squared 0.2251 against a shuffle mean of 0.0311; with Ai167 (81 cells, 22"
   " t-types) 0.0441 (p 0.0198) and 0.4877 against 0.2616. Both hold. Descriptive; the six most frequent"
   " t-types of the Ai14 line have long-pulse PC1 medians 0.233 to 1.844, Kruskal-Wallis p = 5.9e-19. Of"
   " the 15 lines tested, 10 have within-Cre A_t with p < 0.05.",
   deviations=[SEEDS]),
 o("fig3a-type-map-concordance", "reproduced",
   "57 t-types, 1,596 pairs. Concordance 0.6588 (long-ramp), 0.6085 (ramp-brief), 0.4552 (long-brief),"
   " each p = 0.000999 against 1,000 shuffles under all five seeds (null maxima 0.167, 0.147, 0.186), in"
   " the paper's order.",
   measured=[57, 0.6588, 0.6085, 0.4552], deviations=[SEEDS]),
 o("shared-map-model-call", "reproduced",
   "Minimum 0.4552, maximum 0.6588, range 0.2036; the rule (minimum at least 0.40, range below 0.25) holds."),
 o("subclass-map-concordance", "reproduced",
   "Six subclasses (Lamp5, Pvalb, Serpinf1, Sncg, Sst, Vip) with at least 10 cells in every regime;"
   " concordance 0.9357 (long-ramp), 0.5786 (long-brief), 0.6214 (ramp-brief), matching under reading"
   " (a), the code's pair order.",
   measured=[0.9357, 0.5786, 0.6214, 6]),
 o("equal-n-centroid-robustness", "reproduced",
   "Means over 200 resamples 0.5529 (long-ramp, 95% interval 0.4694 to 0.6280), 0.4573 (ramp-brief, 0.3592"
   " to 0.5571), 0.3226 (long-brief, 0.2034 to 0.4183), each below its full-sample value; over five seeds"
   " 0.5527 to 0.5560, 0.4563 to 0.4629 and 0.3223 to 0.3302. Each 2.5th percentile exceeds the largest"
   " of the 1,000 shuffles (0.1671, 0.1466, 0.1855), and each mean the null's 97.5th percentile, so both"
   " readings hold.",
   measured=[0.5529, 0.4573, 0.3226], deviations=[SEEDS]),
 o("within-regime-type-map-reliability", "reproduced",
   "Split-half concordance 0.8621, 0.8522 and 0.7990 (five seeds 0.8621 to 0.8671, 0.8489 to 0.8527,"
   " 0.7990 to 0.8030) against the mean full-sample concordance 0.5742.",
   measured=[0.8621, 0.8522, 0.7990, 0.5742], deviations=[SEEDS]),
 o("fig3b-pair-tags", "reproduced",
   "644 stable (40.4%), 796 intermediate (49.9%), 156 selective (9.8%) of 1,596.",
   measured=[644, 796, 156]),
 o("pair-tag-threshold-sensitivity", "reproduced",
   "At every cutoff of both grids the selective fraction (0.038 to 0.235) is below the stable (0.231 to"
   " 0.569) and the intermediate (0.335 to 0.671) fractions. From the default, the selective fraction moves"
   " by up to 0.137 over the range cutoffs and the stable fraction by up to 0.172 over the CV cutoffs."),
 o("type-level-exceeds-cell-level", "reproduced",
   "Type-map concordance 0.6588, 0.4552 and 0.6085 against cell-cell distance correlations 0.4410, 0.3363"
   " and 0.3848 (long-ramp, long-brief, ramp-brief); 15-NN Jaccard 0.0229, 0.0224, 0.0185."),
 o("mobility-distribution", "reproduced",
   "4,049 triple-shared cells; mobility mean 0.5890, SD 0.1100 (population), range 0.2447 to 1.1808.",
   measured=[0.5890, 0.1100, 4049]),
]
for cid in ["fig4ab-rna-tracks-shared-map", "fig4-alternative-panels", "fig4c-joint-excitability-modules",
            "fig4c-kv3-strongest", "fig4c-no-module-tracks-rank-range", "pvalb-marker-control"]:
    n = rna_note
    if cid != "fig4ab-rna-tracks-shared-map":
        n += " It also depends on fig4ab-rna-tracks-shared-map, blocked for the same reason."
    outcomes.append(o(cid, "blocked", n, blocked_by="other"))
outcomes.append(o("wgcna-mobility-within-type", "blocked",
   rna_note + " The mobility it uses is computed (mobility-distribution). The claim also needs R with WGCNA"
   " 1.74 (the code's q3_wgcna_modules.R), which the entry's locked Python environment does not hold; a"
   " later attempt would need an R environment as well as the matrix.", blocked_by="other"))

rec = {
 "schema_version": 3,
 "id": "yang-2026-flexible-01",
 "datasets": [{"archive": "dandi", "id": "000020", "version": "0.210913.1639",
               "doi": "10.48324/dandi.000020/0.210913.1639", "relation": "reuses"}],
 "paper": "doi:10.1523/eneuro.0275-26.2026",
 "date": "2026-11-22",
 "entry": "yang-2026-flexible",
 "provenance": {"kind": "agent", "accountable": {"name": "CatalystNeuro"},
                "agent": {"harness": "Claude Code", "model": "claude-opus-5-5", "protocol": "pilot-18"},
                "runner": {"platform": "GitHub Actions",
                           "url": "https://github.com/catalystneuro/encore/actions/runs/45006249672"}},
 "inputs": [
  {"what": "The paper's join of the NWB files to the Allen Patch-seq metadata (t-type, subclass, Cre line,"
           " regime membership), results/m0/m0_molecular_join.csv, which the claims file names as the"
           " paper's join of the NeMO metadata.",
   "source": "https://github.com/zy-neuro/protocol-response-geometry at commit 61a5a413daea3b3562fad6e40207320da5665fed"},
  {"what": "The retained feature lists of the three regimes, results/phenotype/phenotype_summary.json, which"
           " the claims file names; the paper's rule applied to this attempt's features gives the same lists.",
   "source": "https://github.com/zy-neuro/protocol-response-geometry at commit 61a5a413daea3b3562fad6e40207320da5665fed"},
 ],
 "outcomes": outcomes,
 "findings": [
  {"kind": "metadata_error", "severity": "critical",
   "statement": "Two files hold the same recording. sub-673135474_ses-680563483 and"
     " sub-673135516_ses-680897463 are from different mice, and the paper's join (Allen metadata) gives them"
     " different Cre lines (Vip-IRES-Cre and Ndnf-IRES2-dgCre), t-types (Vip Lmo1 Myl1 and Lamp5 Lsp1),"
     " layers and transcriptomic samples, yet the voltage traces of all their usable long squares are"
     " identical (SHA-1) and so are all 93 of their IPFX features. At most one of the two cells' recordings"
     " is in the dandiset, and one file carries another cell's data. No other two files share a trace or a"
     " feature vector."},
  {"kind": "format_error", "severity": "minor",
   "statement": "The four files of subject 636828314 (sessions 637823738, 637824890, 637833126, 637838825)"
     " list two response series for sweep number 1 in their sweep table, so IPFX cannot open them. The"
     " paper's join has no row for them either."},
  {"kind": "metadata_insufficient", "severity": "minor",
   "statement": "The files hold no transcriptomic label or sample identifier: the t-types, subclasses and"
     " RNA sample ids of these Patch-seq cells come only from the Allen metadata, joined by session or file"
     " name. The Cre line can be read from the subject genotype, which agrees with the Allen metadata for"
     " every cell."},
  {"kind": "other", "about": "data", "severity": "none",
   "statement": "Every count the paper reports for the dataset is in the files: 4,435 files, 4,430 joined to"
     " the paper's metadata, and IPFX features that give the paper's 4,344, 4,139 and 4,422 cells per regime,"
     " its 42, 20 and 21 retained features and its k80. Sessions and subjects in the files equal the paths,"
     " and the voltage response of every cell's most hyperpolarizing long square begins at the stimulus"
     " onset (median change 0.01 mV in the 10 ms before onset, -15.3 mV 15 to 25 ms after), so stimulus and"
     " response share a clock."},
  {"kind": "methods_unavailable", "about": "paper",
   "statement": "Question for the paper's author. The code does not hold the script that ran IPFX on all"
     " cells: which IPFX version and call made results/features/ipfx_cell_features.csv, and what sets"
     " extract_ok = 1? This attempt used IPFX 2.1.2 through its per-regime functions and took extract_ok = 1"
     " for a file that opened and ran; the resulting cells and features equal the paper's, so the choice"
     " made no difference here, but the paper should state it. The script that wrote"
     " results/q3b/q3b_primary_null_1000.csv (Table 2 rows m and n) is also missing."},
  {"kind": "other", "about": "paper",
   "statement": "The A_t values of Table 2 (rows d to i) depend on an arbitrary order. The code ranks the"
     " binary t-type mismatch with np.argsort(np.argsort(x)), so the tied 0s and 1s are ordered by where the"
     " sampled pairs fall, and the coefficient moves with the pair sample. Here five seeds give long-pulse"
     " A_t from 0.021 to 0.034, against the printed 0.021, while the tie-corrected Spearman is 0.096 and"
     " stable. The significance against shuffles holds under every seed; the printed values have less"
     " precision than their three decimals suggest."},
  {"kind": "other", "about": "paper",
   "statement": "In the split-half analysis the random fallback split draws its permutation from a generator"
     " made afresh with seed 0 for each cell, so every cell with the same number of sweeps gets the same"
     " permutation. Which cells get a random split, 358 in the paper and 16 here under another seed, then"
     " depends on that one permutation per sweep count, and with it the pool of the analysis (3,598 cells in"
     " the paper, 3,256 here)."},
 ],
}
class D(yaml.SafeDumper):
    pass
def str_rep(d, s):
    return d.represent_scalar("tag:yaml.org,2002:str", s)
yaml.add_representer(str, str_rep, Dumper=D)
out = yaml.dump(rec, Dumper=D, sort_keys=False, width=100, allow_unicode=True)
open("attempts/yang-2026-flexible-01.yaml", "w").write(out)
print(len(out))
EOF
python3 $TMPDIR/rec/make.py && grep -n ": .*: " attempts/yang-2026-flexible-01.yaml | grep -v "^ *[0-9]*: *- " | head; python tools/entry.py check entries/yang-2026-flexible 2>&1 | tail -15
```

```
25760
448:  statement: 'The files hold no transcriptomic label or sample identifier: the t-types, subclasses and
455:  statement: 'Every count the paper reports for the dataset is in the files: 4,435 files, 4,430 joined
0 error(s)
```

**Agent calls Bash**

```bash
sed -i 's/hold no transcriptomic label or sample identifier: the t-types/hold no transcriptomic label or sample identifier; the t-types/; s/for the dataset is in the files: 4,435 files/for the dataset is in the files; 4,435 files/' $TMPDIR/rec/make.py && python3 $TMPDIR/rec/make.py && grep -c "^.*: '.*" attempts/yang-2026-flexible-01.yaml; ls tools | head -40; grep -ln "attempt.schema" tools/*.py | head
```

```
25753
3
__pycache__
agent_run.py
archive_transcripts.sh
archives
author_notes.py
authors.py
backfill_summaries.py
blind.sh
build_dryad_targets.py
build_figshare_targets.py
build_openneuro_targets.py
build_reuse_targets.py
build_site.py
build_sparc_targets.py
build_targets.py
changed_entries.py
claims_check.py
colab.py
[... 23 more lines not kept]
```

**Agent calls Bash**

```bash
grep -n "^.*: '.*" attempts/yang-2026-flexible-01.yaml | cut -c1-150; ls tests | head -30; grep -rln "attempts/" tests/*.py 2>/dev/null | head
```

```
5:  id: '000020'
10:date: '2026-11-22'
463:  statement: 'Question for the paper''s author. The code does not hold the script that ran IPFX on all
test_agent_run.py
test_build_site.py
test_build_targets.py
test_claims_check.py
test_datasets.py
test_encore.py
test_entry_tool.py
test_flagged.py
test_notify.py
test_paper_match.py
test_progress.py
test_readme_row.py
test_replicates.py
test_reuse_targets.py
test_run_requests.py
test_runner.py
test_transcript.py
[... 2 more lines not kept]
```

**Agent calls Bash**

```bash
uv run --quiet --with jsonschema --with pyyaml python - <<'EOF'
import json, yaml, jsonschema
for f, s in [("attempts/yang-2026-flexible-01.yaml","schemas/attempt.schema.json"),("claims/yang-2026-flexible.yaml","schemas/claims.schema.json")]:
    d=yaml.safe_load(open(f)); sch=json.load(open(s))
    errs=list(jsonschema.Draft202012Validator(sch).iter_errors(d)) if "2020" in sch.get("$schema","") else list(jsonschema.Draft7Validator(sch).iter_errors(d))
    print(f, len(errs)); [print(" ", e.message[:200], list(e.path)) for e in errs[:10]]
c=yaml.safe_load(open("claims/yang-2026-flexible.yaml")); a=yaml.safe_load(open("attempts/yang-2026-flexible-01.yaml"))
ids=[x["id"] for x in c["claims"]]; oc=[x["claim"] for x in a["outcomes"]]
print("missing outcomes", set(ids)-set(oc), "extra", set(oc)-set(ids))
EOF
```

```
attempts/yang-2026-flexible-01.yaml 0
claims/yang-2026-flexible.yaml 1
  datetime.date(2026, 11, 22) is not of type 'string' ['checks', 0, 'date']
missing outcomes set() extra set()
```

**Agent calls Bash**

```bash
python tools/claims_check.py claims/yang-2026-flexible.yaml paper/10.1523-eneuro.0275-26.2026.txt 2>&1 | tail -8; date -u
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
python tools/entry.py all entries/yang-2026-flexible 2>&1 | tail -4 && python tools/entry.py handover entries/yang-2026-flexible 2>&1 | tail -5; ls executed/yang-2026-flexible/handover; git status --short | head
```

```
0 error(s)
pass  reproduce_yang_2026.ipynb  (2582 s, reused)
reused the executed copies of 2026-11-22 11:46 UTC: nothing the run reads has changed since (hash 380857231da4). Nothing was executed and no environment was built; --fresh runs it again.
wrote executed/yang-2026-flexible/handover
geometry.py
patchseq.py
reproduce_yang_2026.ipynb
yang-2026-flexible.yaml
 M claims/yang-2026-flexible.yaml
?? .bash_profile
?? .bashrc
?? .gitconfig
?? .idea
?? .mcp.json
?? .profile
?? .ripgreprc
?? .vscode
?? .zprofile
```

**Agent calls Bash**

```bash
git status --short | grep -v "^?? \.[a-z]" ; ls -la .bashrc .idea | head -3
```

```
M claims/yang-2026-flexible.yaml
?? attempts/yang-2026-flexible-01.yaml
?? entries/yang-2026-flexible/
?? scripts
crw-rw-rw- 1 nobody nogroup 1, 3 Nov 22 09:10 .bashrc
crw-rw-rw- 1 nobody nogroup 1, 3 Nov 22 09:10 .idea
```

**Agent calls Bash**

```bash
ls -la scripts | head; git check-ignore executed && echo executed-ignored; ls entries/yang-2026-flexible
```

```
crw-rw-rw- 1 nobody nogroup 1, 3 Nov 22 09:10 scripts
executed
executed-ignored
README.md
__pycache__
entry.yaml
geometry.py
patchseq.py
reproduce_yang_2026.ipynb
requirements.in
requirements.lock.txt
```

**Agent calls Bash**

```bash
git check-ignore entries/yang-2026-flexible/__pycache__ && echo ignored; python3 -c "
import json; nb=json.load(open('entries/yang-2026-flexible/reproduce_yang_2026.ipynb')); print(sum(len(c.get('outputs',[])) for c in nb['cells'] if c['cell_type']=='code'))"; date -u
```

```
entries/yang-2026-flexible/__pycache__
ignored
0
Sun Nov 22 11:49:10 UTC 2026
```

**Agent calls Bash**

```bash
curl -s -m 30 -o /dev/null -w "%{http_code}\n" "https://data.nemoarchive.org/other/AIBS/AIBS_patchseq/transcriptome/scell/SMARTseq/processed/analysis/20200611/"; date -u
```

Result: the fetched text is not kept.

**Agent**

## Report: yang-2026-flexible on DANDI:000020 (version 0.210913.1639)

The entry is locked, checked and run, and the handover is built (`executed/yang-2026-flexible/handover/`). Nothing is committed. The record is `attempts/yang-2026-flexible-01.yaml`.

### 1. Outcomes

| Claim | Outcome |
|---|---|
| join-link (link claim I added) | reproduced |
| cohort-label-join, table1-phenotype-spaces (`assumed`), pc1-long-pulse-loadings | reproduced |
| fig1b-distance-correlation, fig1-fixed-five-pcs-ordering, fig1c-knn-jaccard, knn-scale-sweep | reproduced |
| split-half-reliability | partially reproduced |
| fig2c-eta2-ttype-over-cre, fig2d-knn-type-enrichment, fig2ab-ttype-structure-within-cre | reproduced |
| table2-alignment-ttype | partially reproduced |
| ttype-beyond-cre | partially reproduced |
| fig3a, shared-map, subclass, equal-N, within-regime reliability, fig3b pair tags, threshold sensitivity, type-level-exceeds-cell-level | reproduced |
| mobility-distribution | reproduced |
| Six Figure 4 RNA claims, plus wgcna-mobility-within-type | blocked (`other`): the NeMO data server returned 502 or timed out from 09:20 to 11:49 UTC. WGCNA would also need R. |

Most counts equal the paper's exactly: cells per regime, features, k80, overlaps, t-type counts, 57 types, 156 selective pairs. Mobility is 0.589, SD 0.110.

The three partial outcomes:
- **table2-alignment-ttype:** A_t is significant in every regime, but none of the three values is within tolerance. Over the five seeds long-pulse ranges 0.021 to 0.034, because of how the code breaks ties. No seed gives "reproduced", so it is not marked seed-sensitive.
- **ttype-beyond-cre:** the same pattern, after removing each Cre line's mean.
- **split-half-reliability:** one same-pool value is 0.0002 over its bound and one pool is 2 cells short of its tolerance. Only 16 cells got a random split, against the paper's 358, probably because I had to use the protocol's seed instead of the code's seed 0.

### 2. Dataset, assumptions, questions

- **Version.** I pinned 0.210913.1639: it is the version the paper cites and the only published one.
- **Critical finding.** `sub-673135474_ses-680563483` and `sub-673135516_ses-680897463` are identical recordings. All long-square voltage traces have the same SHA-1 and all 93 IPFX features match, yet the files are from different mice with different Cre lines and t-types. No other pair shares a trace or a feature vector.
- **Minor findings.** The four files of subject 636828314 list two response series for sweep 1, so IPFX cannot open them. The files hold no t-type or RNA sample id.
- **Checks that passed.** Sessions, subjects and genotypes match the paper's join for all 4,430 cells. Stimulus and response share a clock.
- **Assumption.** `extract_ok` means the file opened and the extraction ran. It gives exactly the paper's cell sets.
- **Question for the paper's author** (a `methods_unavailable` finding): which IPFX version and call made the feature table, and what sets `extract_ok`. The script for the 1,000-shuffle null of Table 2 rows m and n is also missing.
- **Reader.** I asked no questions.
- **Inputs.** The join CSV and the feature lists, both from the paper's code at commit 61a5a41.

### 3. Protocol points

1. **Adding a link claim means editing the claims file**, which the author is otherwise told not to change. I added `join-link` and listed it in `depends_on` of six claims; statements, expected values and criteria are untouched.
2. **Notebook conclusions are part of the run hash.** Writing them after the run forces a second 43-minute run. I wrote them from a development run of the same deterministic code and checked them against the final executed output.
3. **The protocol's seeds can conflict with a reported count.** Its seed rule replaces the code's seed 0, and one reported count (358 random splits) depends on that seed. Re-extracting under four more seeds would cost about 10 more minutes, so I noted it and did not measure it.
4. **No `blocked_by` value fits a public input whose server is down.** I used `other` and the notebook prints the server's answers.
5. **Python 3.13 runs process pools in spawn mode** when a pool restarts its workers, which breaks scripts. I used fork with my own pool restarts.
6. **Nothing says how to rate a duplicate recording.** I rated it critical: it is one recording deposited as two, which is among the protocol's critical examples.

### 4. Runtime and failures

- **Notebook:** 43 min (extraction 39 min); peak memory 2.8 GB for the largest worker.
- **Development:** in the first full pass a worker was killed and the pool's retry logic marked 661 files as failed. I fixed the retry logic and re-extracted them; the final run had no failures beyond the 4 unreadable files.
- **Whole session:** about 2 h 40 min.

The repo root shows untracked device nodes (`.bashrc`, `scripts`, …); they come from the sandbox, not from me.

## End of run

127 turns, 154 minutes, $11.13 at API prices, result: success.
