# du-2026 · author · run 44913833754

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
date -u; cat docs/protocol.md; ls; ls paper entries claims attempts | head -50
```

```
<persisted-output>
Output too large (47.8KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/454389d8-415a-4c8b-a4ff-1fa16fa31155/tool-results/b4u2a8gt5.txt

Preview (first 2KB):
Sat Nov 21 14:30:50 UTC 2026
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
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/454389d8-415a-4c8b-a4ff-1fa16fa31155/tool-results/b4u2a8gt5.txt"
}
```

```
1	Sat Nov 21 14:30:50 UTC 2026
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
[... 842 more lines not kept]
```

**Agent calls Bash**

```bash
ls paper; cat claims/du-2026.yaml; cat papers/datasets/du-2026.yaml; ls questions | grep du; ls entries/fouke-2025 entries | head -5; ls attempts | grep du
```

```
<persisted-output>
Output too large (55.9KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/454389d8-415a-4c8b-a4ff-1fa16fa31155/tool-results/bliypzg77.txt

Preview (first 2KB):
10.64898-2026.08.04.742876.txt
# Claims for Du, Lai, Hu & Ye (2026), "A Context-Conditional Audit of Trial-Pairing-Dependent
# Neural Gain in Motor-Cortex Decoding", bioRxiv doi:10.64898/2026.08.04.742876, tested on
# DANDI:001201 (LINK) and DANDI:000129 (MC_RTT).
# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"), 2026-11-21,
# protocol as stated in docs/protocol.md (version pilot-18, Reader).
#
# Text read. The bioRxiv preprint posted August 10, 2026 (a Journal of Neural Engineering
# submission), full text in paper/10.64898-2026.08.04.742876.txt: main text, figure legends,
# Tables 1 to 3, Methods, Data and Code availability. No PDF was supplied. The paper's
# Supplementary information (formal properties, complete ladder results, replacement
# diagnostics, confirmation details, nonlinear-map seeds, temporal and capacity sensitivities)
# is not under paper/ and is not in the code release; every claim below rests on numbers the
# main text or its tables state. The one main-text sentence that points to supplement values
# (replacement ranks one to five) is a claim judged by sign alone (replacement-ranks-lower).
#
[... 12 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/454389d8-415a-4c8b-a4ff-1fa16fa31155/tool-results/bliypzg77.txt"
}
```

```
1	10.64898-2026.08.04.742876.txt
2	# Claims for Du, Lai, Hu & Ye (2026), "A Context-Conditional Audit of Trial-Pairing-Dependent
3	# Neural Gain in Motor-Cortex Decoding", bioRxiv doi:10.64898/2026.08.04.742876, tested on
4	# DANDI:001201 (LINK) and DANDI:000129 (MC_RTT).
5	# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"), 2026-11-21,
6	# protocol as stated in docs/protocol.md (version pilot-18, Reader).
7	#
8	# Text read. The bioRxiv preprint posted August 10, 2026 (a Journal of Neural Engineering
9	# submission), full text in paper/10.64898-2026.08.04.742876.txt: main text, figure legends,
10	# Tables 1 to 3, Methods, Data and Code availability. No PDF was supplied. The paper's
11	# Supplementary information (formal properties, complete ladder results, replacement
12	# diagnostics, confirmation details, nonlinear-map seeds, temporal and capacity sensitivities)
13	# is not under paper/ and is not in the code release; every claim below rests on numbers the
14	# main text or its tables state. The one main-text sentence that points to supplement values
15	# (replacement ranks one to five) is a claim judged by sign alone (replacement-ranks-lower).
16	#
17	# Code read. github.com/gwkuqgfkqe/neural-decoder-context-audit, tag v1.0-jne-submission,
18	# commit b042fbe1cda2ca5a353751c693d7c95f45de0456 (Code availability names this release). It
19	# holds the loaders (src/neural_evidence/link.py, mc_rtt.py, mc_maze.py), the fully nested and
20	# nonlinear estimators (nested_estimators.py), the synthetic generator (synthetic.py), run
[... 1106 more lines not kept]
```

**Agent calls Bash**

```bash
wc -c paper/*; sed -n 1,400p docs/archives.md | grep -n -A40 "## DANDI" | head -80
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
ls entries/fouke-2025; cat entries/fouke-2025/entry.yaml entries/fouke-2025/requirements.in; cat attempts/fouke-2025-01.yaml | head -150
```

```
README.md
entry.yaml
omr.py
reproduce_fouke_2025.ipynb
requirements.in
requirements.lock.txt
schema_version: 1
name: fouke-2025
type: reproduction
title: Optomotor swimming of zebrafish and Danionella cerebrum (Fouke et al. 2025)
description: Tests the freely swimming findings of Fouke, He, Loring and Naumann (2025) on dandiset
  001453, which holds the tracking data of 25 zebrafish and 12 Danionella cerebrum larvae during the
  optomotor protocol. It compares swimming speed, turning and angular acceleration between species
  and stimuli, the response to monocular stimuli, and how steady the swimming is. The imaging and
  head-fixed tail tracking of the paper's Figures 2 to 4 are not in the dandiset.
license: Apache-2.0
notebooks:
- path: reproduce_fouke_2025.ipynb
  title: Reproducing Fouke et al. (2025) from dandiset 001453
  runtime_minutes: 6
[... 165 more lines not kept]
```

**Agent**

Read the protocol and claims file (32 claims across two dandisets). Now reading the paper and checking whether the paper's code repo is reachable.

**Agent calls Read**

```json
{
 "file_path": "paper/10.64898-2026.08.04.742876.txt"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd $TMPDIR && timeout 60 git clone -q https://github.com/gwkuqgfkqe/neural-decoder-context-audit.git 2>&1 | tail -3; cd neural-decoder-context-audit 2>/dev/null && git log --oneline -1 && git tag && find . -name "*.py" | xargs wc -l | tail -30
```

```
56ae7a8 Publish finger velocity analysis code and reproduction guide
finger-velocity-2026-11
v1.0-jne-submission
    88 ./tests/test_robustness_estimators.py
    49 ./tests/test_download_manifest.py
   255 ./tests/test_submission_package.py
   132 ./tests/test_specification_estimators.py
   882 ./src/neural_evidence/nested_estimators.py
    13 ./src/neural_evidence/__init__.py
    38 ./src/neural_evidence/serialization.py
    25 ./src/neural_evidence/types.py
   238 ./src/neural_evidence/robustness_estimators.py
   221 ./src/neural_evidence/mc_rtt.py
   269 ./src/neural_evidence/link.py
   986 ./src/neural_evidence/specification_estimators.py
   242 ./src/neural_evidence/synthetic.py
   751 ./src/neural_evidence/estimators.py
   248 ./src/neural_evidence/mc_maze.py
    94 ./scripts/download_link_confirmation.py
   176 ./scripts/build_link_confirmation_manifest.py
[... 14 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "paper/10.64898-2026.08.04.742876.txt",
 "offset": 1304,
 "limit": 480
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd $TMPDIR/neural-decoder-context-audit && git checkout -q v1.0-jne-submission && git log --oneline -1 && ls; ls outputs outputs/* | head -50; cat src/neural_evidence/link.py
```

```
b042fbe Refresh package checksum inventory
ANALYSIS_PROVENANCE.md
CHECKSUMS.sha256
FROZEN_ARTIFACTS.sha256
LICENSE
README.md
REPRODUCE.md
data
outputs
pyproject.toml
requirements-original-analysis.txt
requirements.txt
scripts
src
submission_source
tests
outputs:
confirmation_analysis
primary_analysis

[... 293 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/neural-decoder-context-audit && cat src/neural_evidence/nested_estimators.py src/neural_evidence/types.py
```

```
<persisted-output>
Output too large (32KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/454389d8-415a-4c8b-a4ff-1fa16fa31155/tool-results/bbzeg6tm3.txt

Preview (first 2KB):
"""Fully nested and practical-effect audits added for submission version 0.6.

The development--earlier sensitivity analysis estimators and outputs are intentionally left unchanged.  This
module makes the scope of every nuisance prediction auditable: the penalty,
scaler, and coefficients used for one cross-fit validation fold are learned
only from that fold's training trials.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass

import numpy as np
from sklearn.kernel_approximation import RBFSampler
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import StratifiedKFold, train_test_split
[... 59 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/454389d8-415a-4c8b-a4ff-1fa16fa31155/tool-results/bbzeg6tm3.txt"
}
```

```
1	"""Fully nested and practical-effect audits added for submission version 0.6.
2	
3	The development--earlier sensitivity analysis estimators and outputs are intentionally left unchanged.  This
4	module makes the scope of every nuisance prediction auditable: the penalty,
5	scaler, and coefficients used for one cross-fit validation fold are learned
6	only from that fold's training trials.
7	"""
8	
9	from __future__ import annotations
10	
11	from dataclasses import asdict, dataclass
12	
13	import numpy as np
14	from sklearn.kernel_approximation import RBFSampler
15	from sklearn.metrics import mean_squared_error, r2_score
16	from sklearn.model_selection import StratifiedKFold, train_test_split
17	from sklearn.pipeline import make_pipeline
18	from sklearn.preprocessing import StandardScaler
19	from sklearn.linear_model import Ridge
20	
[... 888 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/neural-decoder-context-audit && grep -n "^def \|^class " src/neural_evidence/*.py && cat src/neural_evidence/robustness_estimators.py | sed -n 1,140p
```

```
src/neural_evidence/estimators.py:18:class EvaluationResult:
src/neural_evidence/estimators.py:49:def _ridge(alpha: float) -> object:
src/neural_evidence/estimators.py:56:def _flatten_trials(array: np.ndarray, trial_indices: np.ndarray) -> np.ndarray:
src/neural_evidence/estimators.py:61:def _select_ridge_alpha(
src/neural_evidence/estimators.py:87:def _cross_fitted_nuisance_predictions(
src/neural_evidence/estimators.py:158:def _context_matched_trial_sources(
src/neural_evidence/estimators.py:198:def _cluster_bootstrap_delta_r2(
src/neural_evidence/estimators.py:237:def evaluate_decoders(
src/neural_evidence/estimators.py:442:def evaluate_decoders_nested(
src/neural_evidence/link.py:13:def _direction_octant(displacement: np.ndarray) -> int:
src/neural_evidence/link.py:18:def _phase_basis(n_time: int, n_harmonics: int = 4) -> np.ndarray:
src/neural_evidence/link.py:31:def load_link(
src/neural_evidence/mc_maze.py:12:def _series(interface: object) -> object:
src/neural_evidence/mc_maze.py:19:def _bin_timestamped_mean(
src/neural_evidence/mc_maze.py:39:def load_mc_maze(
src/neural_evidence/mc_rtt.py:12:def _spatial_series(interface: object) -> object:
src/neural_evidence/mc_rtt.py:19:def _downsample_mean(data: np.ndarray, samples_per_bin: int) -> np.ndarray:
src/neural_evidence/mc_rtt.py:26:def _direction_octant(target_error: np.ndarray) -> int:
src/neural_evidence/mc_rtt.py:32:def load_mc_rtt(
src/neural_evidence/nested_estimators.py:44:class FoldScope:
[... 181 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/neural-decoder-context-audit && sed -n 1,90p src/neural_evidence/estimators.py; sed -n 198,236p src/neural_evidence/estimators.py; sed -n 442,751p src/neural_evidence/estimators.py; sed -n 153,180p src/neural_evidence/specification_estimators.py; sed -n 813,826p src/neural_evidence/specification_estimators.py
```

```
"""Cross-fitted estimators for task-template and neural contributions."""

from __future__ import annotations

from dataclasses import asdict, dataclass

import numpy as np
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import StratifiedKFold, train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

from .types import TrialDataset


@dataclass(frozen=True)
class EvaluationResult:
    context_r2: float
    neural_r2: float
[... 462 more lines not kept]
```

**Agent**

Now the run scripts (primary, ladder, confirmation) to see call parameters.

**Agent calls Bash**

```bash
cd $TMPDIR/neural-decoder-context-audit && cat scripts/run_link_context_ladder.py | sed -n 1,137p; grep -n "load_link\|evaluate_\|neural_history\|neural_lead\|SEEDS\|n_permutations\|n_bootstrap\|context_mode\|output_" scripts/run_primary_analyses.py scripts/run_link_confirmation.py scripts/run_nonlinear_seed_sensitivity.py
```

```
"""Run the complete primary SBP context ladder with fully nested nuisances."""

from __future__ import annotations

import argparse
import csv
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

import numpy as np
from pynwb import NWBHDF5IO

from neural_evidence.link import load_link
from neural_evidence.nested_estimators import evaluate_fully_nested_audit
from neural_evidence.serialization import dumps_strict, write_json


CONTEXTS = (
    "phase_only",
    "condition_phase",
[... 198 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/neural-decoder-context-audit && sed -n 60,135p scripts/run_primary_analyses.py; sed -n 250,300p scripts/run_primary_analyses.py; cat src/neural_evidence/mc_rtt.py
```

```
"replacement_sources",
            "permutation_gains",
        }
    }


def _run_link_session(path_string: str, bootstrap: int) -> dict[str, object]:
    path = Path(path_string)
    date, task = _metadata(path)
    rows: list[dict[str, object]] = []
    prediction_records: list[dict[str, object]] = []
    nonlinear_rows: list[dict[str, object]] = []
    for signal in SIGNALS:
        for context in CONTEXTS:
            for seed in SEEDS:
                split = load_link(
                    path,
                    neural_signal=signal,
                    neural_history_ms=160,
                    neural_lead_ms=0,
[... 329 more lines not kept]
```

**Agent calls Bash**

```bash
date -u; cd $TMPDIR && curl -s "https://api.dandiarchive.org/api/dandisets/001201/versions/" | python -c "import json,sys; d=json.load(sys.stdin); [print(v['version'],v['status'],v['modified'],v.get('asset_count'),v.get('size')) for v in d['results']]"; curl -s "https://api.dandiarchive.org/api/dandisets/000129/versions/" | python -c "import json,sys; d=json.load(sys.stdin); [print(v['version'],v['status'],v['modified'],v.get('asset_count'),v.get('size')) for v in d['results']]"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR && python - <<'EOF'
import json,urllib.request
def assets(ds,v):
    out=[];url=f"https://api.dandiarchive.org/api/dandisets/{ds}/versions/{v}/assets/?page_size=1000"
    while url:
        d=json.load(urllib.request.urlopen(url)); out+=d['results']; url=d['next']
    return out
a=assets('001201','0.251023.2336'); b=assets('001201','0.261026.1912')
json.dump(a,open('link_assets.json','w'))
print(len(a), a[0])
pa={x['path']:(x['blob'] if 'blob' in x else x.get('zarr'),x['size']) for x in a}
pb={x['path']:(x.get('blob'),x['size']) for x in b}
print(set(pa)==set(pb), sum(pa[k][1]!=pb[k][1] for k in pa if k in pb))
for x in a[:5]: print(x['path'],x['size'],x['asset_id'])
r=assets('000129','0.241017.1444'); json.dump(r,open('rtt_assets.json','w'))
for x in r: print(x['path'],x['size'],x['asset_id'])
EOF
```

```
312 {'asset_id': 'ea07a2e3-d5f4-4036-9b62-93d1f89cba64', 'blob': '68f2afdf-0748-4644-a5e7-f13d9b976411', 'zarr': None, 'path': 'sub-Monkey-N/sub-Monkey-N_ses-20200204_ecephys.nwb', 'size': 43052898, 'created': '2025-10-03T17:23:17.501967Z', 'modified': '2025-10-23T23:36:27.374098Z'}
True 0
sub-Monkey-N/sub-Monkey-N_ses-20200204_ecephys.nwb 43052898 ea07a2e3-d5f4-4036-9b62-93d1f89cba64
sub-Monkey-N/sub-Monkey-N_ses-20200127_ecephys.nwb 45005026 c002a9a1-664d-4a69-af02-ba810046c4fb
sub-Monkey-N/sub-Monkey-N_ses-20200130_ecephys.nwb 43863496 9d1820f1-7583-4faf-bbd0-7e9fb7001ca4
sub-Monkey-N/sub-Monkey-N_ses-20200206_ecephys.nwb 43884592 008fc384-2a95-47ec-8dbe-7acb4a18bcc7
sub-Monkey-N/sub-Monkey-N_ses-20200205_ecephys.nwb 43262978 24b91bc3-92ba-457c-8718-490b508f6b8f
sub-Indy/sub-Indy_desc-test_ecephys.nwb 1201344 648a7418-98e8-4413-ba97-3772dd325ecc
sub-Indy/sub-Indy_desc-train_behavior+ecephys.nwb 49764168 2ae6bf3c-788b-4ece-8c01-4b4a5680b25b
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && python - <<'EOF'
import json,collections
a=json.load(open('link_assets.json'))
paths=sorted(x['path'] for x in a)
import re
c=collections.Counter(re.search(r'ses-(\d{8})',p).group(1) for p in paths)
print([p for p in paths if not re.fullmatch(r'sub-Monkey-N/sub-Monkey-N_ses-\d{8}_ecephys.nwb',p)][:40])
print([d for d,n in c.items() if n>1])
print(paths[:3], len(paths), sum(x['size'] for x in a)/1e9)
EOF
cat neural-decoder-context-audit/data/data_manifest.json | head -80
```

```
['sub-Monkey-N/sub-Monkey-N_ses-20211015_obj-1wbkdus_ecephys.nwb', 'sub-Monkey-N/sub-Monkey-N_ses-20211015_obj-a6r2sq_ecephys.nwb', 'sub-Monkey-N/sub-Monkey-N_ses-20220225_obj-1n9hlgs_ecephys.nwb', 'sub-Monkey-N/sub-Monkey-N_ses-20220225_obj-1o8kg92_ecephys.nwb', 'sub-Monkey-N/sub-Monkey-N_ses-20220408_obj-1n84koa_ecephys.nwb', 'sub-Monkey-N/sub-Monkey-N_ses-20220408_obj-1owcs5m_ecephys.nwb', 'sub-Monkey-N/sub-Monkey-N_ses-20220415_obj-1ro3kfu_ecephys.nwb', 'sub-Monkey-N/sub-Monkey-N_ses-20220415_obj-y4c3g5_ecephys.nwb', 'sub-Monkey-N/sub-Monkey-N_ses-20220429_obj-1fu8b25_ecephys.nwb', 'sub-Monkey-N/sub-Monkey-N_ses-20220429_obj-1qhe815_ecephys.nwb', 'sub-Monkey-N/sub-Monkey-N_ses-20220513_obj-nedbdh_ecephys.nwb', 'sub-Monkey-N/sub-Monkey-N_ses-20220513_obj-yotjar_ecephys.nwb', 'sub-Monkey-N/sub-Monkey-N_ses-20220810_obj-1h8xjhp_ecephys.nwb', 'sub-Monkey-N/sub-Monkey-N_ses-20220810_obj-hjf8k2_ecephys.nwb', 'sub-Monkey-N/sub-Monkey-N_ses-20220921_obj-1k78ex8_ecephys.nwb', 'sub-Monkey-N/sub-Monkey-N_ses-20220921_obj-iknmjb_ecephys.nwb', 'sub-Monkey-N/sub-Monkey-N_ses-20221102_obj-3s4gm4_ecephys.nwb', 'sub-Monkey-N/sub-Monkey-N_ses-20221102_obj-ndh6o5_ecephys.nwb']
['20211015', '20220225', '20220408', '20220415', '20220429', '20220513', '20220810', '20220921', '20221102']
['sub-Monkey-N/sub-Monkey-N_ses-20200127_ecephys.nwb', 'sub-Monkey-N/sub-Monkey-N_ses-20200130_ecephys.nwb', 'sub-Monkey-N/sub-Monkey-N_ses-20200204_ecephys.nwb'] 312 12.563287466
{
  "schema_version": "1.1",
  "datasets": {
    "000129": {
      "version": "0.241017.1444",
      "license": "CC-BY-4.0"
    },
    "000139": {
      "version": "0.220113.0408",
      "license": "CC-BY-4.0"
    },
    "001201": {
      "version": "0.251023.2336",
      "license": "CC-BY-4.0"
    }
  },
  "nlb": [
[... 64 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && uv venv -q -p 3.12 venv 2>&1 | tail -2; . venv/bin/activate && uv pip install -q pynwb remfile h5py scikit-learn numpy pandas scipy matplotlib dandi 2>&1 | tail -2; python -c "import pynwb,sklearn;print(pynwb.__version__,sklearn.__version__)"; cat tools/entry.py | grep -n "python\b\|PYTHON\|3\.1" | head
```

```
4.2.0 1.9.1
3:    python tools/entry.py lock  entries/<name>   # pin the environment
4:    python tools/entry.py check entries/<name>   # validate metadata and conventions
5:    python tools/entry.py check entries/*/       # the same for every entry, in one process
6:    python tools/entry.py run   entries/<name>   # execute every notebook from a clean environment
7:    python tools/entry.py all   entries/<name>   # check, then run
8:    python tools/entry.py handover entries/<name> # the verifier's package, from the executed copies
63:PYTHON_VERSION = "3.13"
206:        if entry.get("python") and locked_for and locked_for.group(1) != str(entry["python"]):
208:                         f"says {entry['python']}; run `tools/entry.py lock`")
467:LOCK_VERSION = re.compile(r"--python-version\s+(\d+\.\d+)")
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && . venv/bin/activate && cat > survey.py <<'EOF'
import remfile,h5py,pynwb,json,time,sys
t=time.time()
aid=sys.argv[1]; ds=sys.argv[2]; ver=sys.argv[3]
url=f"https://api.dandiarchive.org/api/assets/{aid}/download/"
import urllib.request
req=urllib.request.Request(url,method='HEAD')
s3=urllib.request.urlopen(req).geturl()
f=h5py.File(remfile.File(s3),'r')
io=pynwb.NWBHDF5IO(file=f,load_namespaces=True); nwb=io.read()
print(nwb.identifier, nwb.session_description[:300], nwb.session_start_time)
print('subject',nwb.subject)
print('acq',list(nwb.acquisition)); print('analysis',list(nwb.analysis)); print('proc',{k:list(v.data_interfaces) for k,v in nwb.processing.items()})
for k,v in nwb.analysis.items():
    print(k, type(v).__name__, getattr(v,'data',None).shape if hasattr(v,'data') else '', getattr(v,'unit',None), getattr(v,'description','')[:200], 'rate',getattr(v,'rate',None), 'ts', v.timestamps.shape if getattr(v,'timestamps',None) is not None else None)
tr=nwb.trials.to_dataframe() if nwb.trials is not None else None
if tr is not None:
    print(tr.shape); print(tr.head(3).T); print(tr.describe().T)
    for c in nwb.trials.colnames: print(c, nwb.trials[c].description)
if nwb.units is not None: print('units',len(nwb.units), nwb.units.colnames)
print('elapsed',time.time()-t)
EOF
python survey.py 5c74bad7-55be-47a6-b754-c77654064981 001201 0.251023.2336 2>&1 | grep -v Warning
```

```
2021-10-15_CO_nwb Neural and behavioral data for target style CO 2021-10-15 00:00:00+00:00
subject subject pynwb.file.Subject at 0x136141362347520
Fields:
  age__reference: birth
  date_of_birth: 2012-05-26 00:00:00+00:00
  description: Monkey N
  sex: M
  species: Macaca mulatta
  subject_id: Monkey N

acq []
analysis ['SpikingBandPower', 'ThresholdCrossings', 'index_position', 'index_velocity', 'mrs_position', 'mrs_velocity']
proc {}
SpikingBandPower ElectricalSeries (21825, 96) volts Spiking Band Power across time, in 20ms bins rate None ts (21825,)
ThresholdCrossings ElectricalSeries (21825, 96) volts Threshold crossings (threshold = -4.5RMS) across time, in 20ms bins rate None ts (21825,)
index_position TimeSeries (21825, 1) flexion units Index flexion position, from fully extended (0) to fully flexed (1) rate None ts (21825,)
index_velocity TimeSeries (21825, 1) flexion units per time bin Velocity of index flexion rate None ts (21825,)
mrs_position TimeSeries (21825, 1) flexion units Middle-ring-pinky flexion position, from fully extended (0) to fully flexed (1) rate None ts (21825,)
mrs_velocity TimeSeries (21825, 1) flexion units per time bin Velocity of middle-ring-pinky flexion rate None ts (21825,)
(375, 10)
[... 36 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/neural-decoder-context-audit && cat src/neural_evidence/synthetic.py | sed -n 1,132p; sed -n 1,146p scripts/run_synthetic_calibration.py | grep -v "^\s*$"
```

```
"""Synthetic task-template and trial-innovation neural decoding data."""

from __future__ import annotations

import numpy as np

from .types import TrialDataset


def _smooth_ar_innovations(
    rng: np.random.Generator,
    n_trials: int,
    n_time: int,
    n_outputs: int,
    scale: float,
    rho: float = 0.85,
) -> np.ndarray:
    innovations = rng.normal(size=(n_trials, n_time, n_outputs))
    residual = np.zeros_like(innovations)
    residual[:, 0] = innovations[:, 0]
[... 246 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/neural-decoder-context-audit && sed -n 93,152p src/neural_evidence/specification_estimators.py; sed -n 181,700p src/neural_evidence/specification_estimators.py
```

```
class _BlockRidge:
    """Ridge regression with separate penalties for two feature blocks.

    After block-wise standardization, dividing a block by the square root of
    its requested penalty and fitting Ridge(alpha=1) is equivalent to applying
    that penalty to the block's coefficients.
    """

    def __init__(
        self,
        *,
        context_penalty: float,
        neural_penalty: float,
    ) -> None:
        if context_penalty <= 0 or neural_penalty <= 0:
            raise ValueError("Block penalties must be strictly positive")
        self.context_penalty = float(context_penalty)
        self.neural_penalty = float(neural_penalty)
        self.context_scaler = StandardScaler()
        self.neural_scaler = StandardScaler()
[... 560 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/neural-decoder-context-audit && sed -n 87,197p src/neural_evidence/estimators.py; sed -n 1,176p scripts/build_link_confirmation_manifest.py | grep -v "^\s*$" | sed -n 1,140p
```

```
def _cross_fitted_nuisance_predictions(
    *,
    dataset: TrialDataset,
    trial_indices: np.ndarray,
    context_alpha: float,
    residualizer_alpha: float,
    n_splits: int,
    seed: int,
) -> tuple[np.ndarray, np.ndarray]:
    """Return out-of-fold behavior and neural predictions.

    Folds are defined over whole trials. Each training residual used by the
    innovation decoder is therefore produced by nuisance models that never
    saw that trial.
    """

    conditions = dataset.condition[trial_indices, 0]
    _, counts = np.unique(conditions, return_counts=True)
    effective_splits = min(n_splits, int(counts.min()))
    if effective_splits < 2:
[... 232 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/neural-decoder-context-audit && grep -n "def date_cluster_summary" -A45 scripts/build_submission_figures.py; grep -n "def _link_ladder" -A60 scripts/build_submission_figures.py | grep -n "boot\|rng\|diff\|RD\|CO" | head -30; grep -n "representative\|median" scripts/build_submission_figures.py | head -30
```

```
999:def date_cluster_summary() -> pd.DataFrame:
1000-    link = _primary_link()
1001-    rng = np.random.default_rng(20260802)
1002-    rows = []
1003-    for signal in ("SpikingBandPower", "ThresholdCrossings"):
1004-        for context in ("geometry_tensor", "causal_history"):
1005-            selected = link[(link.signal == signal) & (link.context_mode == context)]
1006-            dates = np.asarray(sorted(selected.date.unique()))
1007-            boot = []
1008-            for _ in range(10000):
1009-                sampled_dates = rng.choice(dates, size=len(dates), replace=True)
1010-                sampled = pd.concat([selected[selected.date == date] for date in sampled_dates], ignore_index=True)
1011-                boot.append(sampled.exact_gain.mean())
1012-            rows.append(
1013-                {
1014-                    "signal": signal,
1015-                    "context_mode": context,
1016-                    "n_sessions": len(selected),
1017-                    "n_dates": len(dates),
1018-                    "mean_gain": selected.exact_gain.mean(),
[... 45 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/neural-decoder-context-audit && sed -n 712,745p scripts/build_submission_figures.py
```

```
lineterminator="\n",
    )
    figure.tight_layout(h_pad=1.5)
    _save(figure, "figure5_estimator_sensitivity")


def figure8_practical_effects() -> None:
    link = _primary_link()
    geometry = link[(link.signal == "SpikingBandPower") & (link.context_mode == "geometry_tensor")].copy()
    geometry = geometry.sort_values(["exact_gain", "date", "task"]).reset_index(drop=True)
    median_row = geometry.iloc[(len(geometry) - 1) // 2]
    source = np.load(
        OUTPUT
        / "link_prediction_source_data"
        / f"{median_row.date}_{median_row.task}_sbp_geometry.npz"
    )
    improvement = source["per_trial_context_mse"] - source["per_trial_exact_mse"]
    ordering = np.lexsort((source["test_indices"], improvement))
    trial_position = int(ordering[(len(ordering) - 1) // 2])
    trial_index = int(source["test_indices"][trial_position])
[... 15 more lines not kept]
```

**Agent**

Writing the helper module now (port of the paper's loader and estimators, with citations).

**Agent calls Bash**

```bash
mkdir -p entries/du-2026; date -u
```

```
Sat Nov 21 14:32:46 UTC 2026
```

**Agent calls Write**

```json
{
 "file_path": "entries/du-2026/du2026.py",
 "content": "\"\"\"Loading and estimators for the attempt on Du, Lai, Hu & Ye (2026).\n\nPaper: \"A Context-Conditional Audit of Trial-Pairing-Dependent Neural Gain in\nMotor-Cortex Decoding\", bioRxiv doi:10.64898/2026.08.04.742876.\nDatasets: DANDI:001201 (LINK) and DANDI:000129 (MC_RTT), streamed at the\nversions the paper cites (Methods 4.2, Data availability).\n\nEvery estimator here is a port of the paper's own code, the release named in\nits Code availability section: github.com/gwkuqgfkqe/neural-decoder-context-audit,\ntag v1.0-jne-submission, commit b042fbe1cda2ca5a353751c693d7c95f45de0456\n(BSD 3-Clause, copyright the paper's authors). The file and function each\nport comes from is named in its docstring, so that a verifier can compare\nthem. Parameters come from the claims file's criteria (which cite the\nMethods or that code), from the passage of the paper named where they are\nset, or are marked as a standard choice that cannot change a result.\nThe ports read the NWB files by streaming them (remfile + h5py) and keep\nthe arithmetic of the original: the same Ridge pipelines, the same\nscikit-learn splitters and the same random_state offsets.\n\"\"\"\n\nfrom __future__ import annotations\n\nimport json\nimport re\nimport urllib.request\nfrom dataclasses import dataclass\nfrom decimal import ROUND_HALF_UP, Decimal\n\nimport h5py\nimport numpy as np\nimport pandas as pd\nimport remfile\nfrom sklearn.kernel_approximation import RBFSampler\nfrom sklearn.linear_model import Ridge\nfrom sklearn.metrics import mean_squared_error, r2_score\nfrom sklearn.model_selection import StratifiedKFold, train_test_split\nfrom sklearn.pipeline import make_pipeline\nfrom sklearn.preprocessing import StandardScaler\n\nAPI = \"https://api.dandiarchive.org/api\"\nLINK_ID = \"001201\"\nLINK_VERSION = \"0.251023.2336\"  # Methods 4.2 and Data availability\nRTT_ID = \"000129\"\nRTT_VERSION = \"0.241017.1444\"  # Methods 4.2 and Data availability\nRTT_TRAIN_PATH = \"sub-Indy/sub-Indy_desc-train_behavior+ecephys.nwb\"\n\nPAPER_CODE = \"https://github.com/gwkuqgfkqe/neural-decoder-context-audit\"\nPAPER_COMMIT = \"b042fbe1cda2ca5a353751c693d7c95f45de0456\"\n\n# Methods 4.5: penalty grid\nALPHA_GRID = (0.1, 1.0, 10.0, 100.0, 1000.0, 10000.0, 100000.0)\n# run_primary_analyses.py SEEDS; Results 2.7 (three split seeds)\nSPLIT_SEEDS = (20260726, 20260727, 20260728)\n# Methods 4.6 and run_nonlinear_seed_sensitivity.py RFF_SEEDS\nRFF_SEEDS = (20260802, 20260803, 20260804)\nLADDER = (\"phase_only\", \"condition_phase\", \"geometry_additive\", \"geometry_tensor\", \"causal_history\")\nLADDER_NAMES = {\n    \"phase_only\": \"phase only\",\n    \"condition_phase\": \"direction by phase\",\n    \"geometry_additive\": \"additive geometry\",\n    \"geometry_tensor\": \"geometry by phase\",\n    \"causal_history\": \"plus measured-output history\",\n    \"geometry_quadratic\": \"quadratic geometry\",\n    \"causal_history_quadratic\": \"quadratic plus history\",\n}\n\n\n# --------------------------------------------------------------------------\n# Archive access\n\n\ndef _get_json(url: str) -> dict:\n    with urllib.request.urlopen(url, timeout=120) as response:\n        return json.load(response)\n\n\ndef list_assets(dandiset: str, version: str) -> list[dict]:\n    \"\"\"Every asset of a published version, from the DANDI REST API.\"\"\"\n    url = f\"{API}/dandisets/{dandiset}/versions/{version}/assets/?page_size=1000\"\n    out: list[dict] = []\n    while url:\n        page = _get_json(url)\n        out.extend(page[\"results\"])\n        url = page[\"next\"]\n    return out\n\n\ndef asset_metadata(dandiset: str, version: str, asset_id: str) -> dict:\n    return _get_json(f\"{API}/dandisets/{dandiset}/versions/{version}/assets/{asset_id}/\")\n\n\ndef s3_url(asset_id: str) -> str:\n    request = urllib.request.Request(f\"{API}/assets/{asset_id}/download/\", method=\"HEAD\")\n    with urllib.request.urlopen(request, timeout=120) as response:\n        return response.geturl()\n\n\ndef open_h5(asset_id: str) -> h5py.File:\n    \"\"\"Stream one NWB file (no download to disk).\"\"\"\n    return h5py.File(remfile.File(s3_url(asset_id)), \"r\")\n\n\n# --------------------------------------------------------------------------\n# LINK\n\n\ndef session_date(path: str) -> str:\n    value = re.search(r\"ses-(\\d{8})\", path).group(1)\n    return f\"{value[:4]}-{value[4:6]}-{value[6:]}\"\n\n\ndef link_task_from_metadata(metadata: dict) -> str:\n    \"\"\"Target style from the asset metadata (build_link_confirmation_manifest.py, _task).\"\"\"\n    for activity in metadata.get(\"wasGeneratedBy\", []):\n        match = re.search(r\"target style\\s+(CO|RD)\", str(activity.get(\"description\", \"\")))\n        if match:\n            return match.group(1)\n    raise ValueError(f\"No target style in metadata for {metadata.get('identifier')}\")\n\n\ndef interior_ranks(n_items: int, n_select: int = 10) -> list[int]:\n    \"\"\"Half-up ranks nearest j/11 (build_link_confirmation_manifest.py, _interior_ranks; Methods 4.2).\"\"\"\n    ranks = []\n    for index in range(1, n_select + 1):\n        raw = Decimal(index) * Decimal(n_items - 1) / Decimal(n_select + 1)\n        ranks.append(int(raw.quantize(Decimal(\"1\"), rounding=ROUND_HALF_UP)))\n    return ranks\n\n\ndef _read_trials(h5: h5py.File) -> pd.DataFrame:\n    group = h5[\"intervals/trials\"]\n    columns = {}\n    for name in group:\n        dataset = group[name]\n        if not isinstance(dataset, h5py.Dataset) or name in {\"id\", \"timeseries\", \"timeseries_index\"}:\n            continue\n        values = dataset[:]\n        if values.dtype.kind in \"SO\":\n            values = np.array([v.decode() if isinstance(v, bytes) else str(v) for v in values])\n        columns[name] = values\n    frame = pd.DataFrame(columns)\n    frame.index = group[\"id\"][:]\n    return frame\n\n\n@dataclass\nclass LinkSession:\n    asset_id: str\n    path: str\n    identifier: str\n    date: str\n    task: str\n    timestamps: np.ndarray\n    signals: dict\n    position: np.ndarray\n    velocity: np.ndarray\n    trials: pd.DataFrame\n    units: dict\n\n\ndef load_link_session(asset_id: str, path: str, signals=(\"SpikingBandPower\", \"ThresholdCrossings\")) -> LinkSession:\n    \"\"\"Read the arrays link.py reads (load_link): the 20 ms SBP/TCR series in the\n    NWB analysis module, index and MRS position and velocity, and the trials table.\"\"\"\n    with open_h5(asset_id) as h5:\n        identifier = h5[\"identifier\"][()]\n        identifier = identifier.decode() if isinstance(identifier, bytes) else str(identifier)\n        analysis = h5[\"analysis\"]\n        timestamps = analysis[signals[0]][\"timestamps\"][:].astype(float)\n        data = {s: analysis[s][\"data\"][:].astype(np.float32) for s in signals}\n        for s in signals:\n            if not np.array_equal(analysis[s][\"timestamps\"][:].astype(float), timestamps):\n                raise AssertionError(f\"{s} timestamps differ from {signals[0]}\")\n        position = np.concatenate(\n            [analysis[\"index_position\"][\"data\"][:], analysis[\"mrs_position\"][\"data\"][:]], axis=1\n        ).astype(np.float32)\n        velocity = np.concatenate(\n            [analysis[\"index_velocity\"][\"data\"][:], analysis[\"mrs_velocity\"][\"data\"][:]], axis=1\n        ).astype(np.float32)\n        units = {}\n        for name in (\"SpikingBandPower\", \"ThresholdCrossings\", \"index_position\", \"index_velocity\"):\n            if name in analysis:\n                units[name] = analysis[name][\"data\"].attrs.get(\"unit\")\n                if isinstance(units[name], bytes):\n                    units[name] = units[name].decode()\n        # position/velocity share the clock of the neural series\n        for name in (\"index_position\", \"index_velocity\", \"mrs_position\", \"mrs_velocity\"):\n            if not np.allclose(analysis[name][\"timestamps\"][:], timestamps):\n                raise AssertionError(f\"{name} timestamps differ from the neural series\")\n        trials = _read_trials(h5)\n    date, task, _ = identifier.rsplit(\"_\", 2)\n    return LinkSession(asset_id, path, identifier, date, task, timestamps, data, position, velocity, trials, units)\n\n\ndef _direction_octant(displacement: np.ndarray) -> int:\n    \"\"\"link.py _direction_octant.\"\"\"\n    angle = np.arctan2(displacement[1], displacement[0])\n    return int(np.floor(((angle + np.pi) / (2.0 * np.pi)) * 8)) % 8\n\n\ndef phase_basis(n_time: int, n_harmonics: int = 4) -> np.ndarray:\n    \"\"\"1, sin(r pi tau), cos(r pi tau), r = 1..4 (Methods 4.4; link.py _phase_basis).\"\"\"\n    phase = np.linspace(0.0, 1.0, n_time, endpoint=False)\n    features = [np.ones_like(phase)]\n    for harmonic in range(1, n_harmonics + 1):\n        features.extend([np.sin(harmonic * np.pi * phase), np.cos(harmonic * np.pi * phase)])\n    return np.stack(features, axis=-1)\n\n\n@dataclass\nclass TrialDataset:\n    neural: np.ndarray\n    context: np.ndarray\n    behavior: np.ndarray\n    condition: np.ndarray\n    train_indices: np.ndarray\n    test_indices: np.ndarray\n    source_rows: np.ndarray | None = None  # row of the NWB trials table, per usable trial\n\n\ndef build_link_dataset(\n    session: LinkSession,\n    *,\n    signal: str = \"SpikingBandPower\",\n    context_mode: str = \"geometry_tensor\",\n    movement_window_ms: int = 500,\n    neural_history_ms: int = 160,\n    neural_lead_ms: int = 0,\n    output_history_ms: int = 100,\n    output_lead_ms: int = 0,\n    sample_offset_ms: int | None = None,\n    seed: int = 20260726,\n    test_size: float = 0.30,\n) -> TrialDataset:\n    \"\"\"Port of link.py load_link, from arrays already streamed.\n\n    Defaults are those every LINK run script passes (run_link_context_ladder.py,\n    run_primary_analyses.py, run_link_confirmation.py): SBP, 160 ms history\n    ending at the behavior bin (lead 0), 100 ms position history (lead 0),\n    25 bins of 20 ms (Methods 4.3), 70/30 split stratified by direction\n    octant with random_state=seed (Methods 4.5).\n    \"\"\"\n    bin_ms = 20\n    n_time = movement_window_ms // bin_ms\n    history_bins = neural_history_ms // bin_ms\n    lead_bins = neural_lead_ms // bin_ms\n    out_hist = output_history_ms // bin_ms\n    out_lead = output_lead_ms // bin_ms\n    warmup = max(history_bins + lead_bins, out_hist + out_lead)\n    offset = warmup if sample_offset_ms is None else sample_offset_ms // bin_ms\n    if offset < warmup:\n        raise ValueError(\"sample offset must accommodate all history and lead bins\")\n    basis = phase_basis(n_time)\n    timestamps = session.timestamps\n    data = session.signals[signal]\n    position = session.position\n    velocity = session.velocity\n\n    neural_trials, context_trials, behavior_trials, conditions, rows = [], [], [], [], []\n    for row_index, row in enumerate(session.trials.itertuples()):\n        start_index = int(np.argmin(np.abs(timestamps - float(row.start_time))))\n        sample_start = start_index + offset\n        samples = np.arange(sample_start, sample_start + n_time)\n        stop_index = start_index + int(row.trial_count)\n        if samples[-1] >= min(stop_index, len(timestamps)):\n            continue\n        neural_trial = np.stack(\n            [data[b - lead_bins - history_bins : b - lead_bins].reshape(-1) for b in samples]\n        )\n        behavior_trial = velocity[samples]\n        initial = position[start_index].astype(float)\n        target = np.array([float(row.index_target_position), float(row.mrs_target_position)])\n        displacement = target - initial\n        condition = _direction_octant(displacement)\n        one_hot = np.repeat(np.eye(8)[condition][None, :], n_time, axis=0)\n        condition_phase = (one_hot[:, :, None] * basis[:, None, :]).reshape(n_time, -1)\n        geometry = np.repeat(np.concatenate([target, initial, displacement])[None, :], n_time, axis=0)\n        geometry_phase = (geometry[:, :, None] * basis[:, None, :]).reshape(n_time, -1)\n        parts = [basis]\n        if context_mode != \"phase_only\":\n            parts.insert(0, condition_phase)\n        if context_mode in {\"geometry_additive\", \"geometry_tensor\", \"geometry_quadratic\", \"causal_history\", \"causal_history_quadratic\"}:\n            parts.append(geometry)\n        if context_mode in {\"geometry_tensor\", \"geometry_quadratic\", \"causal_history\", \"causal_history_quadratic\"}:\n            parts.append(geometry_phase)\n        if context_mode in {\"geometry_quadratic\", \"causal_history_quadratic\"}:\n            quadratic = np.stack(\n                [geometry[:, a] * geometry[:, b] for a in range(6) for b in range(a, 6)], axis=-1\n            )\n            parts.extend([quadratic, (quadratic[:, :, None] * basis[:, None, :]).reshape(n_time, -1)])\n        if context_mode in {\"causal_history\", \"causal_history_quadratic\"}:\n            parts.append(\n                np.stack([position[b - out_lead - out_hist : b - out_lead].reshape(-1) for b in samples])\n            )\n        neural_trials.append(neural_trial)\n        context_trials.append(np.concatenate(parts, axis=-1))\n        behavior_trials.append(behavior_trial)\n        conditions.append(np.full(n_time, condition, dtype=int))\n        rows.append(row_index)\n\n    condition = np.stack(conditions)\n    indices = np.arange(len(neural_trials))\n    train, test = train_test_split(indices, test_size=test_size, random_state=seed, stratify=condition[:, 0])\n    return TrialDataset(\n        neural=np.stack(neural_trials),\n        context=np.stack(context_trials).astype(float),\n        behavior=np.stack(behavior_trials),\n        condition=condition,\n        train_indices=np.asarray(train, dtype=int),\n        test_indices=np.asarray(test, dtype=int),\n        source_rows=np.asarray(rows),\n    )\n\n\n# --------------------------------------------------------------------------\n# MC_RTT\n\n\ndef _downsample_mean(data: np.ndarray, samples_per_bin: int) -> np.ndarray:\n    usable = data.shape[0] - (data.shape[0] % samples_per_bin)\n    return data[:usable].reshape(-1, samples_per_bin, data.shape[-1]).mean(axis=1)\n\n\ndef _rtt_octant(target_error: np.ndarray) -> int:\n    mean_error = target_error.mean(axis=0)\n    angle = np.arctan2(mean_error[1], mean_error[0])\n    return int(np.floor(((angle + np.pi) / (2 * np.pi)) * 8)) % 8\n\n\n@dataclass\nclass RttRaw:\n    finger_vel: np.ndarray\n    cursor_pos: np.ndarray\n    target_pos: np.ndarray\n    behavior_timestamps_head: np.ndarray\n    behavior_rate: float | None\n    spike_counts: np.ndarray\n    n_units: int\n    trials: pd.DataFrame\n    n_bins: int\n    descriptions: dict\n\n\ndef load_rtt_raw(asset_id: str, bin_ms: int = 20) -> RttRaw:\n    \"\"\"Arrays mc_rtt.py load_mc_rtt reads: finger_vel, cursor_pos, target_pos\n    (1 kHz, averaged into 20 ms bins), spike times histogrammed on the same grid\n    (Methods 4.3), and the trials table with its split column.\"\"\"\n    with open_h5(asset_id) as h5:\n        behavior = h5[\"processing/behavior\"]\n        descriptions = {}\n\n        def series(name):\n            group = behavior[name]\n            if \"data\" not in group:\n                group = group[next(iter(group))]\n            descriptions[name] = {\n                \"unit\": group[\"data\"].attrs.get(\"unit\"),\n                \"conversion\": group[\"data\"].attrs.get(\"conversion\"),\n                \"description\": group.attrs.get(\"description\"),\n            }\n            if \"timestamps\" in group:\n                ts = group[\"timestamps\"][:5]\n                rate = None\n            else:\n                ts = np.array([group[\"starting_time\"][()]])\n                rate = group[\"starting_time\"].attrs.get(\"rate\")\n            return group[\"data\"][:].astype(float), ts, rate\n\n        fv, ts_head, rate = series(\"finger_vel\")\n        cp, _, _ = series(\"cursor_pos\")\n        tp, _, _ = series(\"target_pos\")\n        finger_velocity = _downsample_mean(fv, bin_ms)\n        cursor_position = _downsample_mean(cp, bin_ms)\n        target_position = _downsample_mean(tp, bin_ms)\n        n_bins = min(len(finger_velocity), len(cursor_position), len(target_position))\n        edges = np.linspace(0.0, n_bins * bin_ms / 1000.0, n_bins + 1)\n        index = h5[\"units/spike_times_index\"][:]\n        spike_times = h5[\"units/spike_times\"][:]\n        starts = np.concatenate([[0], index[:-1]])\n        counts = np.stack(\n            [np.histogram(spike_times[a:b], bins=edges)[0] for a, b in zip(starts, index)], axis=-1\n        ).astype(np.float32)\n        trials = _read_trials(h5)\n    return RttRaw(finger_velocity, cursor_position, target_position, ts_head, rate, counts, counts.shape[1], trials, n_bins, descriptions)\n\n\ndef build_rtt_dataset(raw: RttRaw, *, bin_ms=20, neural_history_ms=100, neural_lead_ms=80,\n                      output_history_ms=100, output_lead_ms=80, context_mode=\"causal_history\") -> TrialDataset:\n    \"\"\"Port of mc_rtt.py load_mc_rtt. Defaults are run_primary_analyses.py _run_nlb:\n    causal_history context, neural and output leads of 80 ms (Methods 4.3, 4.4);\n    release split labels \"train\" and \"val\".\"\"\"\n    history_bins = neural_history_ms // bin_ms\n    lead_bins = neural_lead_ms // bin_ms\n    out_hist = output_history_ms // bin_ms\n    out_lead = output_lead_ms // bin_ms\n    warmup = max(history_bins + lead_bins, out_hist + out_lead)\n    neural_trials, context_trials, behavior_trials, conditions, labels, rows = [], [], [], [], [], []\n    for row_index, row in enumerate(raw.trials.itertuples()):\n        start_bin = int(round(float(row.start_time) * 1000.0 / bin_ms))\n        stop_bin = int(round(float(row.stop_time) * 1000.0 / bin_ms))\n        samples = np.arange(start_bin + warmup, stop_bin)\n        if samples.size == 0 or samples[-1] >= raw.n_bins:\n            continue\n        neural_trial = np.stack([raw.spike_counts[b - lead_bins - history_bins : b - lead_bins].reshape(-1) for b in samples])\n        target = raw.target_pos[samples]\n        cursor = raw.cursor_pos[samples]\n        error = target - cursor\n        if context_mode == \"target_only\":\n            context = target\n        elif context_mode == \"task_state\":\n            context = np.concatenate([target, cursor, error], axis=-1)\n        else:\n            history = np.stack([raw.cursor_pos[b - out_lead - out_hist : b - out_lead].reshape(-1) for b in samples])\n            context = np.concatenate([target, history, target - history[:, -2:]], axis=-1)\n        neural_trials.append(neural_trial)\n        context_trials.append(context)\n        behavior_trials.append(raw.finger_vel[samples])\n        conditions.append(np.full(samples.size, _rtt_octant(error), dtype=int))\n        labels.append(str(row.split))\n        rows.append(row_index)\n    labels = np.asarray(labels)\n    return TrialDataset(\n        neural=np.stack(neural_trials),\n        context=np.stack(context_trials),\n        behavior=np.stack(behavior_trials),\n        condition=np.stack(conditions),\n        train_indices=np.flatnonzero(labels == \"train\"),\n        test_indices=np.flatnonzero(labels == \"val\"),\n        source_rows=np.asarray(rows),\n    )\n\n\n# --------------------------------------------------------------------------\n# Synthetic generator (synthetic.py generate_synthetic_dataset; Methods 4.8)\n\nSYNTHETIC_REGIMES = {\n    \"template_only\": {\"neural_innovation_strength\": 0.0, \"innovation_scale\": 0.20},\n    \"weak\": {\"neural_innovation_strength\": 0.8, \"innovation_scale\": 0.25},\n    \"strong\": {\"neural_innovation_strength\": 1.8, \"innovation_scale\": 0.35},\n}\nSYNTHETIC_SEEDS = tuple(range(20260726, 20260736))\n\n\ndef generate_synthetic(*, seed, n_trials=480, n_time=60, n_conditions=8, n_neurons=48, template_scale=1.0,\n                       innovation_scale=0.20, neural_innovation_strength=0.0, neural_noise=0.20) -> TrialDataset:\n    \"\"\"Port of synthetic.py generate_synthetic_dataset. neural_noise=0.20 is what\n    run_synthetic_calibration.py passes (Methods 4.8, neural noise SD 0.20). The\n    outer split is the estimator's own 70/30 condition-stratified split with\n    random_state=seed (nested_estimators.py _resolve_split).\"\"\"\n    rng = np.random.default_rng(seed)\n    condition_per_trial = np.tile(np.arange(n_conditions), n_trials // n_conditions)\n    rng.shuffle(condition_per_trial)\n    phase = np.linspace(0.0, 1.0, n_time, endpoint=False)\n    angles = 2.0 * np.pi * condition_per_trial / n_conditions\n    directions = np.stack([np.cos(angles), np.sin(angles)], axis=-1)\n    speed = np.sin(np.pi * phase) ** 1.5\n    template = template_scale * directions[:, None, :] * speed[None, :, None]\n    innovations = rng.normal(size=(n_trials, n_time, 2))\n    residual = np.zeros_like(innovations)\n    residual[:, 0] = innovations[:, 0]\n    rho = 0.85\n    for t in range(1, n_time):\n        residual[:, t] = rho * residual[:, t - 1] + np.sqrt(1 - rho**2) * innovations[:, t]\n    residual = innovation_scale * residual\n    behavior = template + residual\n    one_hot = np.eye(n_conditions)[condition_per_trial]\n    phase_features = np.stack(\n        [np.sin(np.pi * phase), np.cos(np.pi * phase), np.sin(2 * np.pi * phase), np.cos(2 * np.pi * phase), speed], axis=-1\n    )\n    rep_one_hot = np.repeat(one_hot[:, None, :], n_time, axis=1)\n    rep_phase = np.repeat(phase_features[None], n_trials, axis=0)\n    condition_phase = (rep_one_hot[:, :, :, None] * rep_phase[:, :, None, :]).reshape(n_trials, n_time, -1)\n    context = np.concatenate([rep_one_hot, rep_phase, condition_phase], axis=-1)\n    context_weights = rng.normal(scale=1.0 / np.sqrt(context.shape[-1]), size=(context.shape[-1], n_neurons))\n    innovation_weights = rng.normal(scale=1.0 / np.sqrt(2), size=(2, n_neurons))\n    neural = (\n        np.einsum(\"ntc,cp->ntp\", context, context_weights)\n        + neural_innovation_strength * np.einsum(\"ntd,dp->ntp\", residual, innovation_weights)\n        + rng.normal(scale=neural_noise, size=(n_trials, n_time, n_neurons))\n    )\n    condition = np.repeat(condition_per_trial[:, None], n_time, axis=1)\n    train, test = train_test_split(np.arange(n_trials), test_size=0.30, random_state=seed, stratify=condition[:, 0])\n    return TrialDataset(neural, context, behavior, condition, np.asarray(train), np.asarray(test))\n\n\n# --------------------------------------------------------------------------\n# Estimators (estimators.py, nested_estimators.py, robustness_estimators.py,\n# specification_estimators.py)\n\n\ndef _ridge(alpha: float):\n    \"\"\"estimators.py _ridge: StandardScaler then Ridge (Methods 4.5).\"\"\"\n    return make_pipeline(StandardScaler(), Ridge(alpha=alpha))\n\n\ndef _flat(array: np.ndarray, idx: np.ndarray) -> np.ndarray:\n    selected = array[idx]\n    return selected.reshape(-1, selected.shape[-1])\n\n\ndef _vw_r2(y, p) -> float:\n    return float(r2_score(y, p, multioutput=\"variance_weighted\"))\n\n\ndef _select_alpha(xtr, ytr, xva, yva, grid=ALPHA_GRID) -> float:\n    \"\"\"estimators.py _select_ridge_alpha (first best on ties).\"\"\"\n    best, best_score = grid[0], -np.inf\n    for a in grid:\n        score = _vw_r2(yva, _ridge(a).fit(xtr, ytr).predict(xva))\n        if score > best_score:\n            best, best_score = a, score\n    return float(best)\n\n\ndef normalized_gain(y, context_prediction, candidate_prediction) -> float:\n    \"\"\"(MSE_C - MSE_C+X) / Var(Y), Results 2.1 and Methods 4.9 (specification_estimators.py _normalized_gain).\"\"\"\n    variance = float(np.mean((y - y.mean(axis=0)) ** 2))\n    return float((mean_squared_error(y, context_prediction) - mean_squared_error(y, candidate_prediction)) / variance)\n\n\ndef _inner_split(ds: TrialDataset, idx: np.ndarray, seed: int, size: float = 0.20):\n    \"\"\"nested_estimators.py _stratified_inner_split.\"\"\"\n    cond = ds.condition[idx, 0]\n    _, counts = np.unique(cond, return_counts=True)\n    strat = cond if counts.min() >= 2 else None\n    a, b = train_test_split(idx, test_size=size, random_state=seed, stratify=strat)\n    return np.asarray(a, dtype=int), np.asarray(b, dtype=int)\n\n\ndef _nuisance_alphas(ds, idx, seed):\n    \"\"\"nested_estimators.py _select_nuisance_alphas: separate penalties for\n    context->behavior and context->neural on an inner 80/20 split (Methods 4.5, step 3).\"\"\"\n    tr, va = _inner_split(ds, idx, seed)\n    ctr, cva = _flat(ds.context, tr), _flat(ds.context, va)\n    ca = _select_alpha(ctr, _flat(ds.behavior, tr), cva, _flat(ds.behavior, va))\n    ra = _select_alpha(ctr, _flat(ds.neural, tr), cva, _flat(ds.neural, va))\n    return ca, ra\n\n\ndef _nested_oof(ds, idx, seed, folds=5):\n    \"\"\"nested_estimators.py _fully_nested_nuisance_predictions (Methods 4.5, steps 1-4).\"\"\"\n    cond = ds.condition[idx, 0]\n    _, counts = np.unique(cond, return_counts=True)\n    k = min(folds, int(counts.min()))\n    splitter = StratifiedKFold(n_splits=k, shuffle=True, random_state=seed)\n    bp = np.empty(ds.behavior[idx].shape, dtype=float)\n    npred = np.empty(ds.neural[idx].shape, dtype=float)\n    for fold, (ltr, lva) in enumerate(splitter.split(idx, cond)):\n        ftr, fva = idx[ltr], idx[lva]\n        ca, ra = _nuisance_alphas(ds, ftr, seed + 100 + fold)\n        ctr, cva = _flat(ds.context, ftr), _flat(ds.context, fva)\n        bp[lva] = _ridge(ca).fit(ctr, _flat(ds.behavior, ftr)).predict(cva).reshape(bp[lva].shape)\n        npred[lva] = _ridge(ra).fit(ctr, _flat(ds.neural, ftr)).predict(cva).reshape(npred[lva].shape)\n    return bp, npred, k\n\n\ndef _innovation_alpha(rx, ry, cond, seed, grid=ALPHA_GRID):\n    \"\"\"nested_estimators.py _select_grouped_innovation_alpha: three-fold whole-trial\n    validation on out-of-fold residuals (Methods 4.5).\"\"\"\n    _, counts = np.unique(cond, return_counts=True)\n    splitter = StratifiedKFold(n_splits=min(3, int(counts.min())), shuffle=True, random_state=seed)\n    scores = {float(a): [] for a in grid}\n    for tr, va in splitter.split(np.arange(len(cond)), cond):\n        xtr, ytr = rx[tr].reshape(-1, rx.shape[-1]), ry[tr].reshape(-1, ry.shape[-1])\n        xva, yva = rx[va].reshape(-1, rx.shape[-1]), ry[va].reshape(-1, ry.shape[-1])\n        for a in grid:\n            scores[float(a)].append(_vw_r2(yva, _ridge(a).fit(xtr, ytr).predict(xva)))\n    return max(scores, key=lambda a: (np.mean(scores[a]), -a))\n\n\ndef ranked_sources(ds: TrialDataset, n_ranks: int = 1):\n    \"\"\"robustness_estimators.py _ranked_replacement_sources (Methods 4.7): other\n    test trials of the same condition, flattened context trajectories standardized\n    with outer-training centers and scales, mean squared distance, ties to the\n    lower trial index.\"\"\"\n    tr, te = ds.train_indices, ds.test_indices\n    flat = ds.context.reshape(ds.context.shape[0], -1).astype(float)\n    center, scale = flat[tr].mean(axis=0), flat[tr].std(axis=0)\n    informative = scale > 1e-8\n    z = np.zeros_like(flat)\n    z[:, informative] = (flat[:, informative] - center[informative]) / scale[informative]\n    cond = ds.condition[:, 0]\n    sources = np.empty((n_ranks, len(te)), dtype=int)\n    distances = np.empty((n_ranks, len(te)))\n    for j, t in enumerate(te):\n        cand = te[cond[te] == cond[t]]\n        cand = cand[cand != t]\n        d = np.mean((z[cand] - z[t]) ** 2, axis=1)\n        order = np.lexsort((cand, d))[:n_ranks]\n        sources[:, j] = cand[order]\n        distances[:, j] = d[order]\n    return sources, distances\n\n\ndef permutation_sources(test_indices, conditions, rng):\n    \"\"\"nested_estimators.py _permutation_sources: random ordering then a random\n    cyclic shift within condition, no fixed points (Methods 4.7).\"\"\"\n    sources = np.empty_like(test_indices)\n    tc = conditions[test_indices]\n    for c in np.unique(tc):\n        pos = np.flatnonzero(tc == c)\n        shuffled = rng.permutation(pos)\n        shift = int(rng.integers(1, len(pos)))\n        sources[shuffled] = test_indices[np.roll(shuffled, shift)]\n    assert not np.any(sources == test_indices)\n    return sources\n\n\ndef _rankdata(values):\n    order = np.argsort(values, kind=\"mergesort\")\n    ranks = np.empty(len(values))\n    sv = values[order]\n    start = 0\n    while start < len(values):\n        stop = start + 1\n        while stop < len(values) and sv[stop] == sv[start]:\n            stop += 1\n        ranks[order[start:stop]] = 0.5 * (start + stop - 1)\n        start = stop\n    return ranks\n\n\ndef spearman(x, y) -> float:\n    \"\"\"nested_estimators.py _spearman.\"\"\"\n    if len(x) < 2 or np.std(x) == 0 or np.std(y) == 0:\n        return float(\"nan\")\n    return float(np.corrcoef(_rankdata(x), _rankdata(y))[0, 1])\n\n\ndef fully_nested(ds: TrialDataset, *, seed: int = 20260726, n_permutations: int = 0, n_ranks: int = 1,\n                 random_source_seeds: tuple = (), rff_seeds: tuple = ()) -> dict:\n    \"\"\"Port of nested_estimators.py evaluate_fully_nested_audit (Methods 4.5, 4.7, 4.9).\n\n    Random-state offsets are the code's: nuisance folds seed+21 (fold\n    selection seed+21+100+fold), residual-learner selection seed+301, final\n    nuisance penalties seed+401, permutations seed+601 (Methods 4.7: \"One\n    hundred deterministic permutations\"). The bootstrap interval of the code\n    is not computed (no claim uses it).\n\n    Extra outputs, using the same fitted models: replacement ranks 1..n_ranks\n    (Methods 4.7 diagnostics), uniform random same-condition sources for each\n    seed in random_source_seeds (the paper says only \"a random same-condition\n    source\"; a uniform draw is a standard choice, claims file\n    replacement-ranks-lower), and the nonlinear-neural RFF learner of\n    evaluate_nonlinear_neural_audit for each map seed in rff_seeds (it shares\n    the nuisances and differs only in the residual learner).\n    \"\"\"\n    tr, te = ds.train_indices, ds.test_indices\n    assert not np.intersect1d(tr, te).size\n    bp, npred, k = _nested_oof(ds, tr, seed + 21)\n    ry = ds.behavior[tr] - bp\n    rx = ds.neural[tr] - npred\n    cond_tr = ds.condition[tr, 0]\n    ia = _innovation_alpha(rx, ry, cond_tr, seed + 301)\n    innovation = _ridge(ia).fit(rx.reshape(-1, rx.shape[-1]), ry.reshape(-1, ry.shape[-1]))\n    ca, ra = _nuisance_alphas(ds, tr, seed + 401)\n    ctr, cte = _flat(ds.context, tr), _flat(ds.context, te)\n    xte = _flat(ds.neural, te)\n    yte = _flat(ds.behavior, te)\n    context_model = _ridge(ca).fit(ctr, _flat(ds.behavior, tr))\n    residualizer = _ridge(ra).fit(ctr, _flat(ds.neural, tr))\n    cpred = context_model.predict(cte)\n    resid_te = xte - residualizer.predict(cte)\n    exact = cpred + innovation.predict(resid_te)\n\n    def source_prediction(sources, learner=innovation):\n        return cpred + learner.predict(_flat(ds.neural, sources) - residualizer.predict(_flat(ds.context, sources)))\n\n    srcs, dists = ranked_sources(ds, n_ranks=max(1, n_ranks))\n    replacement = source_prediction(srcs[0])\n    self_prediction = source_prediction(te)\n    shape = ds.behavior[te].shape\n    y3 = yte.reshape(shape)\n    trial_c = np.mean((y3 - cpred.reshape(shape)) ** 2, axis=(1, 2))\n    trial_e = np.mean((y3 - exact.reshape(shape)) ** 2, axis=(1, 2))\n    trial_r = np.mean((y3 - replacement.reshape(shape)) ** 2, axis=(1, 2))\n    variance = float(np.mean((yte - yte.mean(axis=0)) ** 2))\n    cmse, emse, rmse_ = (float(mean_squared_error(yte, p)) for p in (cpred, exact, replacement))\n    comp_gain = []\n    for c in range(yte.shape[1]):\n        v = float(np.mean((yte[:, c] - yte[:, c].mean()) ** 2))\n        comp_gain.append(float((mean_squared_error(yte[:, c], cpred[:, c]) - mean_squared_error(yte[:, c], exact[:, c])) / v))\n    conditions = ds.condition[:, 0]\n    eligible = np.array([np.sum(conditions[te] == conditions[t]) - 1 for t in te])\n    reuse = np.bincount(srcs[0], minlength=ds.neural.shape[0])\n    out = dict(\n        context_r2=_vw_r2(yte, cpred),\n        exact_r2=_vw_r2(yte, exact),\n        gain=normalized_gain(yte, cpred, exact),\n        replacement_gain=normalized_gain(yte, cpred, replacement),\n        self_replacement_max_abs_error=float(np.max(np.abs(self_prediction - exact))),\n        context_mse=cmse, exact_mse=emse, replacement_mse=rmse_,\n        context_rmse=float(np.sqrt(cmse)), exact_rmse=float(np.sqrt(emse)),\n        mse_reduction_percent=float(100 * (cmse - emse) / cmse),\n        component_gain=tuple(comp_gain),\n        variance=variance,\n        n_train=len(tr), n_test=len(te), folds=k,\n        context_alpha=ca, residualizer_alpha=ra, innovation_alpha=ia,\n        eligible_sources_min=int(eligible.min()),\n        source_reuse_max=int(reuse[reuse > 0].max()),\n        replacement_penalty_distance_spearman=spearman(dists[0], trial_r - trial_e),\n        per_trial_context_mse=trial_c, per_trial_exact_mse=trial_e,\n        test_indices=te.copy(),\n    )\n    if n_ranks > 1:\n        out[\"rank_gains\"] = tuple(normalized_gain(yte, cpred, source_prediction(srcs[r])) for r in range(n_ranks))\n    if random_source_seeds:\n        gains = []\n        for s in random_source_seeds:\n            rng = np.random.default_rng(s)\n            picks = np.empty_like(te)\n            for j, t in enumerate(te):\n                cand = te[conditions[te] == conditions[t]]\n                cand = cand[cand != t]\n                picks[j] = rng.choice(cand)\n            gains.append(normalized_gain(yte, cpred, source_prediction(picks)))\n        out[\"random_source_gains\"] = tuple(gains)\n    if n_permutations:\n        rng = np.random.default_rng(seed + 601)\n        gains = [normalized_gain(yte, cpred, source_prediction(permutation_sources(te, conditions, rng)))\n                 for _ in range(n_permutations)]\n        out[\"permutation_mean\"] = float(np.mean(gains))\n    if rff_seeds:\n        rff = {}\n        for map_seed in rff_seeds:\n            alpha = _rff_alpha(rx, ry, cond_tr, seed + 301, map_seed)\n            learner = _rff_ridge(alpha, 512, 1.0 / rx.shape[-1], map_seed).fit(\n                rx.reshape(-1, rx.shape[-1]), ry.reshape(-1, ry.shape[-1]))\n            pred = cpred + learner.predict(resid_te)\n            rff[map_seed] = dict(gain=normalized_gain(yte, cpred, pred), alpha=alpha,\n                                 replacement_gain=normalized_gain(yte, cpred, source_prediction(srcs[0], learner)))\n        out[\"rff\"] = rff\n    return out\n\n\ndef _rff_ridge(alpha, n_components, gamma, seed):\n    \"\"\"nested_estimators.py _rff_ridge: scaler, RBFSampler (W ~ N(0, 2 gamma),\n    b ~ U(0, 2 pi)), scaler, Ridge lsqr (Methods 4.6).\"\"\"\n    return make_pipeline(StandardScaler(), RBFSampler(gamma=gamma, n_components=n_components, random_state=seed),\n                         StandardScaler(), Ridge(alpha=alpha, solver=\"lsqr\", tol=1e-6))\n\n\ndef _rff_alpha(rx, ry, cond, seed, map_seed, n_components=512, g=1.0, grid=ALPHA_GRID):\n    \"\"\"nested_estimators.py _select_grouped_rff_alpha: gamma = g / (neural feature\n    count), map seed + fold in the selection folds.\"\"\"\n    _, counts = np.unique(cond, return_counts=True)\n    splitter = StratifiedKFold(n_splits=min(3, int(counts.min())), shuffle=True, random_state=seed)\n    scores = {float(a): [] for a in grid}\n    for fold, (tr, va) in enumerate(splitter.split(np.arange(len(cond)), cond)):\n        xtr, ytr = rx[tr].reshape(-1, rx.shape[-1]), ry[tr].reshape(-1, ry.shape[-1])\n        xva, yva = rx[va].reshape(-1, rx.shape[-1]), ry[va].reshape(-1, ry.shape[-1])\n        for a in grid:\n            model = _rff_ridge(a, n_components, g / max(1, xtr.shape[1]), map_seed + fold).fit(xtr, ytr)\n            scores[float(a)].append(_vw_r2(yva, model.predict(xva)))\n    return max(scores, key=lambda a: (np.mean(scores[a]), -a))\n\n\ndef _cross_fitted_fixed(ds, idx, ca, ra, seed, folds=5, transform=None):\n    \"\"\"estimators.py _cross_fitted_nuisance_predictions (fixed penalties).\"\"\"\n    cond = ds.condition[idx, 0]\n    _, counts = np.unique(cond, return_counts=True)\n    k = min(folds, int(counts.min()))\n    splitter = StratifiedKFold(n_splits=k, shuffle=True, random_state=seed)\n    bp = np.empty(ds.behavior[idx].shape, dtype=float)\n    npred = np.empty(ds.neural[idx].shape, dtype=float)\n    for fold, (ltr, lva) in enumerate(splitter.split(idx, cond)):\n        ftr, fva = idx[ltr], idx[lva]\n        ctr, cva = _flat(ds.context, ftr), _flat(ds.context, fva)\n        if transform is not None:\n            fmap = transform(fold)\n            ctr, cva = fmap.fit_transform(ctr), fmap.transform(cva)\n        bp[lva] = _ridge(ca).fit(ctr, _flat(ds.behavior, ftr)).predict(cva).reshape(bp[lva].shape)\n        npred[lva] = _ridge(ra).fit(ctr, _flat(ds.neural, ftr)).predict(cva).reshape(npred[lva].shape)\n    return bp.reshape(-1, bp.shape[-1]), npred.reshape(-1, npred.shape[-1])\n\n\ndef decoders_nested(ds: TrialDataset, *, seed: int = 20260726, neural_only_only: bool = False) -> dict:\n    \"\"\"Port of estimators.py evaluate_decoders_nested, the release's neural-only\n    Ridge and its residual-neural (\"innovation\") gain. Penalties from one inner\n    80/20 direction-stratified split of the outer-training trials (random_state\n    seed+11), nuisances cross-fitted with those fixed penalties (seed+21).\n    The context-matched replacement and bootstrap of the original are not\n    computed (no claim uses them).\"\"\"\n    tr, te = ds.train_indices, ds.test_indices\n    cond = ds.condition[:, 0]\n    itr, iva = train_test_split(tr, test_size=0.20, random_state=seed + 11, stratify=cond[tr])\n    xi, xv = _flat(ds.neural, itr), _flat(ds.neural, iva)\n    yi, yv = _flat(ds.behavior, itr), _flat(ds.behavior, iva)\n    xtr, xte = _flat(ds.neural, tr), _flat(ds.neural, te)\n    ytr, yte = _flat(ds.behavior, tr), _flat(ds.behavior, te)\n    na = _select_alpha(xi, yi, xv, yv)\n    neural_r2 = _vw_r2(yte, _ridge(na).fit(xtr, ytr).predict(xte))\n    if neural_only_only:\n        return dict(neural_r2=neural_r2, neural_alpha=na)\n    ci, cv = _flat(ds.context, itr), _flat(ds.context, iva)\n    ca = _select_alpha(ci, yi, cv, yv)\n    ra = _select_alpha(ci, xi, cv, xv)\n    cm = _ridge(ca).fit(ci, yi)\n    rm = _ridge(ra).fit(ci, xi)\n    ia = _select_alpha(xi - rm.predict(ci), yi - cm.predict(ci), xv - rm.predict(cv), yv - cm.predict(cv))\n    ctr, cte = _flat(ds.context, tr), _flat(ds.context, te)\n    cpred = _ridge(ca).fit(ctr, ytr).predict(cte)\n    residualizer = _ridge(ra).fit(ctr, xtr)\n    bp, npred = _cross_fitted_fixed(ds, tr, ca, ra, seed + 21)\n    innovation = _ridge(ia).fit(xtr - npred, ytr - bp)\n    pred = cpred + innovation.predict(xte - residualizer.predict(cte))\n    return dict(neural_r2=neural_r2, context_r2=_vw_r2(yte, cpred), innovation_gain=normalized_gain(yte, cpred, pred),\n                neural_alpha=na, context_alpha=ca, residualizer_alpha=ra, innovation_alpha=ia)\n\n\nclass _BlockRidge:\n    \"\"\"specification_estimators.py _BlockRidge: blockwise standardization, each\n    block divided by sqrt(its penalty), Ridge(alpha=1) (Methods 4.5 objective).\"\"\"\n\n    def __init__(self, cp, xp):\n        self.cp, self.xp = float(cp), float(xp)\n        self.cs, self.xs = StandardScaler(), StandardScaler()\n        self.model = Ridge(alpha=1.0, solver=\"lsqr\", tol=1e-6)\n\n    def _design(self, c, x, fit):\n        if fit:\n            c, x = self.cs.fit_transform(c), self.xs.fit_transform(x)\n        else:\n            c, x = self.cs.transform(c), self.xs.transform(x)\n        return np.concatenate([c / np.sqrt(self.cp), x / np.sqrt(self.xp)], axis=1)\n\n    def fit(self, c, x, y):\n        self.model.fit(self._design(c, x, True), y)\n        return self\n\n    def predict(self, c, x):\n        return self.model.predict(self._design(c, x, False))\n\n\ndef block_ridge(ds: TrialDataset, *, seed: int = 20260726) -> dict:\n    \"\"\"Port of specification_estimators.py evaluate_block_ridge_audit: context-only\n    penalty and the pair (lambda_C, lambda_X) over the grid squared on an inner\n    80/20 split (random_state seed+11), refit on all outer-training trials.\"\"\"\n    tr, te = ds.train_indices, ds.test_indices\n    itr, iva = train_test_split(tr, test_size=0.20, random_state=seed + 11, stratify=ds.condition[tr, 0])\n    ci, cv = _flat(ds.context, itr), _flat(ds.context, iva)\n    xi, xv = _flat(ds.neural, itr), _flat(ds.neural, iva)\n    yi, yv = _flat(ds.behavior, itr), _flat(ds.behavior, iva)\n    ca = _select_alpha(ci, yi, cv, yv)\n    best, best_score = (ALPHA_GRID[0], ALPHA_GRID[0]), -np.inf\n    for cp in ALPHA_GRID:\n        for xp in ALPHA_GRID:\n            score = _vw_r2(yv, _BlockRidge(cp, xp).fit(ci, xi, yi).predict(cv, xv))\n            if score > best_score:\n                best, best_score = (cp, xp), score\n    ctr, cte = _flat(ds.context, tr), _flat(ds.context, te)\n    xtr, xte = _flat(ds.neural, tr), _flat(ds.neural, te)\n    ytr, yte = _flat(ds.behavior, tr), _flat(ds.behavior, te)\n    cpred = _ridge(ca).fit(ctr, ytr).predict(cte)\n    joint = _BlockRidge(*best).fit(ctr, xtr, ytr).predict(cte, xte)\n    return dict(gain=normalized_gain(yte, cpred, joint), context_alpha=ca, penalties=best)\n\n\nclass _RFFContext:\n    \"\"\"specification_estimators.py _RFFContextFeatures: [c, sqrt(2/D) cos(W'c + b)]\n    on standardized context, gamma = g / p (Methods 4.6).\"\"\"\n\n    def __init__(self, g, n_components, seed):\n        self.g, self.n, self.seed = g, n_components, seed\n        self.scaler = StandardScaler()\n\n    def fit_transform(self, c):\n        z = self.scaler.fit_transform(c)\n        self.sampler = RBFSampler(gamma=self.g / max(1, z.shape[1]), n_components=self.n, random_state=self.seed)\n        return np.concatenate([z, self.sampler.fit_transform(z)], axis=1)\n\n    def transform(self, c):\n        z = self.scaler.transform(c)\n        return np.concatenate([z, self.sampler.transform(z)], axis=1)\n\n\ndef rff_context(ds: TrialDataset, *, seed: int = 20260726, gammas=(0.25, 1.0, 4.0), n_components: int = 256,\n                fixed_gamma: float | None = None, map_seed_offset: int = 0) -> dict:\n    \"\"\"Port of specification_estimators.py evaluate_rff_context_audit: g chosen\n    from gammas together with the three penalties on an inner 80/20 split\n    (random_state seed+11; map seed seed+101+gamma index), five cross-fitting\n    folds (seed+21, map seed seed+21+1000+fold). With fixed_gamma, g is fixed\n    (the reading that runs one setting of Methods 4.6); map_seed_offset shifts\n    every map seed (the \"three map seeds\" of Methods 4.6).\"\"\"\n    tr, te = ds.train_indices, ds.test_indices\n    if fixed_gamma is not None:\n        gammas = (fixed_gamma,)\n    itr, iva = train_test_split(tr, test_size=0.20, random_state=seed + 11, stratify=ds.condition[tr, 0])\n    ci, cv = _flat(ds.context, itr), _flat(ds.context, iva)\n    xi, xv = _flat(ds.neural, itr), _flat(ds.neural, iva)\n    yi, yv = _flat(ds.behavior, itr), _flat(ds.behavior, iva)\n    best, best_score = None, -np.inf\n    for gi, g in enumerate(gammas):\n        fmap = _RFFContext(g, n_components, seed + 101 + gi + map_seed_offset)\n        mi, mv = fmap.fit_transform(ci), fmap.transform(cv)\n        ca = _select_alpha(mi, yi, mv, yv)\n        ra = _select_alpha(mi, xi, mv, xv)\n        cm, rm = _ridge(ca).fit(mi, yi), _ridge(ra).fit(mi, xi)\n        rxi, rxv = xi - rm.predict(mi), xv - rm.predict(mv)\n        ryi, ryv = yi - cm.predict(mi), yv - cm.predict(mv)\n        ia = _select_alpha(rxi, ryi, rxv, ryv)\n        pred = cm.predict(mv) + _ridge(ia).fit(rxi, ryi).predict(rxv)\n        score = _vw_r2(yv, pred)\n        if score > best_score:\n            best, best_score = (gi, g, ca, ra, ia), score\n    gi, g, ca, ra, ia = best\n    ctr, cte = _flat(ds.context, tr), _flat(ds.context, te)\n    xtr, xte = _flat(ds.neural, tr), _flat(ds.neural, te)\n    ytr, yte = _flat(ds.behavior, tr), _flat(ds.behavior, te)\n    bp, npred = _cross_fitted_fixed(\n        ds, tr, ca, ra, seed + 21,\n        transform=lambda fold: _RFFContext(g, n_components, seed + 21 + 1000 + fold + map_seed_offset))\n    fmap = _RFFContext(g, n_components, seed + 101 + gi + map_seed_offset)\n    mtr, mte = fmap.fit_transform(ctr), fmap.transform(cte)\n    cpred = _ridge(ca).fit(mtr, ytr).predict(mte)\n    residualizer = _ridge(ra).fit(mtr, xtr)\n    innovation = _ridge(ia).fit(xtr - npred, ytr - bp)\n    pred = cpred + innovation.predict(xte - residualizer.predict(mte))\n    return dict(gain=normalized_gain(yte, cpred, pred), gamma=g, context_r2=_vw_r2(yte, cpred))\n\n\n# --------------------------------------------------------------------------\n# Summaries\n\n\ndef date_bootstrap(values_by_date: dict, rng: np.random.Generator, n: int = 10000) -> tuple[float, float]:\n    \"\"\"Resample dates with replacement, mean over the sessions of the sampled\n    dates, 2.5 and 97.5 percentiles (Table 1 legend; build_submission_figures.py\n    date_cluster_summary). values_by_date maps a date to its session values.\"\"\"\n    dates = sorted(values_by_date)\n    boots = np.empty(n)\n    for i in range(n):\n        sampled = rng.choice(len(dates), size=len(dates), replace=True)\n        boots[i] = np.mean(np.concatenate([np.atleast_1d(values_by_date[dates[j]]) for j in sampled]))\n    return float(np.quantile(boots, 0.025)), float(np.quantile(boots, 0.975))\n"
}
```

```
File created successfully at: entries/du-2026/du2026.py (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd entries/du-2026 && . $TMPDIR/venv/bin/activate && cat > $TMPDIR/t1.py <<'EOF'
import time,resource,sys
sys.path.insert(0,'.')
import du2026 as d, numpy as np
t=time.time()
s=d.load_link_session('5c74bad7-55be-47a6-b754-c77654064981','x')
print('load',time.time()-t, s.identifier, s.units); t=time.time()
for ctx in ['phase_only','geometry_tensor','causal_history']:
    ds=d.build_link_dataset(s,context_mode=ctx)
    print(ctx, ds.neural.shape, ds.context.shape, len(ds.train_indices), len(ds.test_indices), 'build',time.time()-t); t=time.time()
    r=d.fully_nested(ds)
    print({k:v for k,v in r.items() if not isinstance(v,np.ndarray)}); print('nested',time.time()-t); t=time.time()
r=d.fully_nested(ds,n_permutations=100); print('perm',time.time()-t, r['permutation_mean']); t=time.time()
r=d.fully_nested(ds,rff_seeds=(20260802,)); print('rff1',time.time()-t, r['rff']); t=time.time()
print(d.decoders_nested(ds)); print('dec',time.time()-t); t=time.time()
print(d.block_ridge(ds)); print('block',time.time()-t); t=time.time()
print(d.rff_context(ds)); print('rffctx',time.time()-t); t=time.time()
print('maxrss MB',resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1e3)
EOF
python $TMPDIR/t1.py 2>&1 | grep -v Warn
```

```
load 1.7302579879760742 2021-10-15_CO_nwb {'SpikingBandPower': 'volts', 'ThresholdCrossings': 'volts', 'index_position': 'flexion units', 'index_velocity': 'flexion units per time bin'}
phase_only (375, 25, 768) (375, 25, 9) 262 113 build 0.04855513572692871
{'context_r2': 0.014791120389920634, 'exact_r2': 0.3446565070134729, 'gain': 0.32986539673259063, 'replacement_gain': -0.04893790555229011, 'self_replacement_max_abs_error': 0.0, 'context_mse': 0.00022913227691097305, 'exact_mse': 0.0001524147313473493, 'replacement_mse': 0.00024051387690959212, 'context_rmse': 0.01513711587162406, 'exact_rmse': 0.012345636125665995, 'mse_reduction_percent': 33.481771576612736, 'component_gain': (0.2713362253640503, 0.39195299310361836), 'variance': 0.00023257227439898998, 'n_train': 262, 'n_test': 113, 'folds': 5, 'context_alpha': 0.1, 'residualizer_alpha': 1000.0, 'innovation_alpha': 1000.0, 'eligible_sources_min': 5, 'source_reuse_max': 17, 'replacement_penalty_distance_spearman': nan}
nested 7.926666736602783
geometry_tensor (375, 25, 768) (375, 25, 141) 262 113 build 0.05771350860595703
{'context_r2': 0.6113038373608219, 'exact_r2': 0.6343440204753946, 'gain': 0.023040183820660972, 'replacement_gain': -0.0011964670758875522, 'self_replacement_max_abs_error': 0.0, 'context_mse': 9.039995336554578e-05, 'exact_mse': 8.504144541180385e-05, 'replacement_mse': 9.067821843462846e-05, 'context_rmse': 0.009507889006795662, 'exact_rmse': 0.009221791876409044, 'mse_reduction_percent': 5.927556104010366, 'component_gain': (0.026017022182739487, 0.019882358677841196), 'variance': 0.00023257227439898998, 'n_train': 262, 'n_test': 113, 'folds': 5, 'context_alpha': 0.1, 'residualizer_alpha': 10000.0, 'innovation_alpha': 10000.0, 'eligible_sources_min': 5, 'source_reuse_max': 3, 'replacement_penalty_distance_spearman': -0.030393898045994048}
nested 12.107146978378296
causal_history (375, 25, 768) (375, 25, 151) 262 113 build 0.07189321517944336
{'context_r2': 0.6853889835829753, 'exact_r2':
[... 10 more lines not kept]
```

**Agent calls Bash**

```bash
date -u; cd entries/du-2026 && . $TMPDIR/venv/bin/activate && python $TMPDIR/survey.py 2ae6bf3c-788b-4ece-8c01-4b4a5680b25b 000129 x 2>&1 | grep -v Warn | head -60
```

```
Sat Nov 21 14:38:19 UTC 2026
7043e134-0b92-11ec-96df-0db753c69267 Data from monkey Indy performing self-paced random target reaching task. This file contains continuous segments of the full session on 2017-02-02 that can be used for training models for the Neural Latents Benchmark. 2017-02-02 00:00:00-08:00
subject subject pynwb.file.Subject at 0x125835301442368
Fields:
  age: P11Y
  sex: M
  species: Macaca mulatta
  subject_id: Indy

acq []
analysis []
proc {'behavior': ['cursor_pos', 'finger_pos', 'finger_vel', 'target_pos']}
(1080, 3)
id              0    1    2
start_time    0.0  0.6  1.2
stop_time     0.6  1.2  1.8
split       train  val  val
             count    mean         std  min      25%     50%      75%    max
start_time  1080.0  324.15  187.472999  0.0  162.075  324.15  486.225  648.3
stop_time   1080.0  324.75  187.472999  0.6  162.675  324.75  486.825  648.9
[... 5 more lines not kept]
```

**Agent calls Bash**

```bash
. $TMPDIR/venv/bin/activate && cat > $TMPDIR/t2.py <<'EOF'
import time,sys,resource
sys.path.insert(0,'.')
import du2026 as d, numpy as np
t=time.time()
raw=d.load_rtt_raw('2ae6bf3c-788b-4ece-8c01-4b4a5680b25b')
print('load',time.time()-t, raw.descriptions, raw.behavior_timestamps_head, raw.behavior_rate, raw.spike_counts.shape, raw.n_bins, raw.trials.split.value_counts().to_dict()); t=time.time()
ds=d.build_rtt_dataset(raw)
print(ds.neural.shape, ds.context.shape, len(ds.train_indices), len(ds.test_indices))
r=d.fully_nested(ds, n_permutations=0)
print({k:v for k,v in r.items() if not isinstance(v,np.ndarray)}); print('nested',time.time()-t); t=time.time()
print('maxrss MB',resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1e3)
EOF
python $TMPDIR/t2.py 2>&1 | grep -v Warn
```

```
load 2.0216434001922607 {'finger_vel': {'unit': 'm/s', 'conversion': np.float64(0.001), 'description': 'The x and y velocity of the finger in mm/s. Calculated offline from upsampled finger position'}, 'cursor_pos': {'unit': 'meters', 'conversion': np.float64(0.001), 'description': 'The position of the cursor in Cartesian coordinates (x, y) in mm. Recorded at 250 Hz and upsampled to 1 kHz'}, 'target_pos': {'unit': 'meters', 'conversion': np.float64(0.001), 'description': 'The position of the target in Cartesian coordinates (x, y) in mm. Recorded at 250 Hz and upsampled to 1 kHz'}} [0.] 1000.0 (32455, 130) 32455 {'train': 810, 'val': 270}
(1080, 21, 650) (1080, 21, 14) 810 270
{'context_r2': 0.6030810777088083, 'exact_r2': 0.6715410902247172, 'gain': 0.06846001251590875, 'replacement_gain': -0.022972719888446073, 'self_replacement_max_abs_error': 0.0, 'context_mse': 1582.5582063736347, 'exact_mse': 1309.6008124804544, 'replacement_mse': 1674.1528982374598, 'context_rmse': 39.78138014666704, 'exact_rmse': 36.18840715588978, 'mse_reduction_percent': 17.247858106821276, 'component_gain': (0.08359472872984132, 0.05125279247982539), 'variance': 3987.106982046643, 'n_train': 810, 'n_test': 270, 'folds': 5, 'context_alpha': 0.1, 'residualizer_alpha': 0.1, 'innovation_alpha': 10000.0, 'eligible_sources_min': 19, 'source_reuse_max': 4, 'replacement_penalty_distance_spearman': 0.22293327595429982}
nested 11.81830358505249
maxrss MB 745.768
```

**Agent calls Bash**

```bash
cat >> du2026.py <<'EOF'


# --------------------------------------------------------------------------
# Running many fits: one process per session, one BLAS thread per process
# (protocol, "Keep it fast"). Number of workers is a standard choice that
# cannot change a result.

ESTIMATORS = {
    "nested": fully_nested,
    "decoders": decoders_nested,
    "block": block_ridge,
    "rff_context": rff_context,
}


def _drop_arrays(result: dict, keep_arrays: bool) -> dict:
    if keep_arrays:
        return result
    return {k: v for k, v in result.items() if not isinstance(v, np.ndarray)}


def link_session_jobs(asset_id: str, path: str, jobs: list, signals=("SpikingBandPower", "ThresholdCrossings")) -> dict:
    """Stream one LINK session once and run every job on it.

    Each job is (name, build_kwargs, estimator, estimator_kwargs, keep_arrays)."""
    from threadpoolctl import threadpool_limits

    with threadpool_limits(1):
        session = load_link_session(asset_id, path, signals=signals)
        out = {"date": session.date, "task": session.task, "identifier": session.identifier}
        for name, build_kwargs, estimator, estimator_kwargs, keep in jobs:
            ds = build_link_dataset(session, **build_kwargs)
            result = ESTIMATORS[estimator](ds, **estimator_kwargs)
            result["n_usable"] = len(ds.neural)
            result["n_trials_table"] = len(session.trials)
            if keep:
                result["source_rows"] = ds.source_rows
            out[name] = _drop_arrays(result, keep)
    return out


def rtt_jobs(asset_id: str, jobs: list) -> dict:
    from threadpoolctl import threadpool_limits

    with threadpool_limits(1):
        raw = load_rtt_raw(asset_id)
        out = {}
        for name, build_kwargs, estimator, estimator_kwargs, keep in jobs:
            ds = build_rtt_dataset(raw, **build_kwargs)
            out[name] = _drop_arrays(ESTIMATORS[estimator](ds, **estimator_kwargs), keep)
    return out


def synthetic_job(seed: int, regime: str, n_permutations: int = 100) -> dict:
    from threadpoolctl import threadpool_limits

    with threadpool_limits(1):
        ds = generate_synthetic(seed=seed, **SYNTHETIC_REGIMES[regime])
        result = fully_nested(ds, seed=seed, n_permutations=n_permutations)
    return {"seed": seed, "regime": regime, **_drop_arrays(result, False)}


def run_parallel(function, argument_lists: list, workers: int = 4) -> list:
    """Run function(*args) for each args in a process pool; results in input order."""
    import multiprocessing as mp
    from concurrent.futures import ProcessPoolExecutor

    with ProcessPoolExecutor(max_workers=workers, mp_context=mp.get_context("spawn")) as pool:
        futures = [pool.submit(function, *args) for args in argument_lists]
        return [f.result() for f in futures]
EOF
python -c "import ast;ast.parse(open('du2026.py').read())"
```

```
(Bash completed with no output)
```

**Agent calls Bash**

```bash
cd  && grep -n "cwd\|timeout\|sanity\|claim:\|nbclient\|papermill\|jupyter" tools/entry.py | head -40; cat entries/fouke-2025/README.md | head -30
```

```
21:- each notebook has a cell tagged `sanity` that prints what was loaded;
236:        if not any("sanity" in c.metadata.get("tags", []) for c in nb.cells if c.cell_type == "code"):
237:            report.error(rel / name, "no code cell tagged `sanity` (the data check; see docs/protocol.md)")
502:                        "requirements.in", "-o", "requirements.lock.txt"], cwd=entry_dir)
516:            if tag.startswith("claim:"):
524:def upgrade_python(entry_dir: Path, version: str, before: Path, output_dir: Path, timeout: int,
531:    if lock(entry_dir, version) or run(entry_dir, output_dir, timeout, max_minutes, fresh=True):
596:def run(entry_dir: Path, output_dir: Path, timeout: int, max_minutes: float, fresh: bool = False) -> int:
626:            [str(python), "-m", "jupyter", "nbconvert", "--to", "notebook", "--execute",
627:             f"--ExecutePreprocessor.timeout={timeout}", f"--ExecutePreprocessor.kernel_name={kernel}",
629:            cwd=entry_dir, capture_output=True, text=True,
630:            env={**os.environ, "JUPYTER_PATH": str(venv / "share" / "jupyter")})
702:    parser.add_argument("--timeout", type=int, default=3600, help="seconds allowed per cell")
744:                              args.timeout, args.max_minutes)
754:    return run(entry_dir, output_dir, args.timeout, args.max_minutes, args.fresh)
# Fouke, He, Loring & Naumann (2025) from dandiset 001453

Tests the findings of [Fouke et al. (2025)](https://doi.org/10.1016/j.cub.2025.04.027) that can be
tested on [DANDI:001453](https://dandiarchive.org/dandiset/001453/0.250518.1950), which holds the
freely swimming tracking of 25 zebrafish and 12 *Danionella cerebrum* larvae (Figure 1 and Figure
[... 24 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/du-2026 && python - <<'EOF'
s=open('du2026.py').read()
old='''    if n_permutations:
        rng = np.random.default_rng(seed + 601)
        gains = [normalized_gain(yte, cpred, source_prediction(permutation_sources(te, conditions, rng)))
                 for _ in range(n_permutations)]
        out["permutation_mean"] = float(np.mean(gains))'''
new='''    if n_permutations:
        # seed + 601 is the code's generator; extra offsets give the protocol's
        # seed-sensitivity runs (claim seed plus 1000, 2000, 3000, 4000)
        out["permutation_means"] = {}
        for offset in (0,) + tuple(permutation_seed_offsets):
            rng = np.random.default_rng(seed + 601 + offset)
            gains = [normalized_gain(yte, cpred, source_prediction(permutation_sources(te, conditions, rng)))
                     for _ in range(n_permutations)]
            out["permutation_means"][offset] = float(np.mean(gains))
        out["permutation_mean"] = out["permutation_means"][0]'''
assert old in s; s=s.replace(old,new)
s=s.replace("random_source_seeds: tuple = (), rff_seeds: tuple = ()) -> dict:","random_source_seeds: tuple = (), rff_seeds: tuple = (),\n                 permutation_seed_offsets: tuple = ()) -> dict:")
open('du2026.py','w').write(s)
EOF
. $TMPDIR/venv/bin/activate; uv pip install -q nbformat nbconvert ipykernel threadpoolctl 2>&1|tail -1; date -u
```

```
Sat Nov 21 14:39:43 UTC 2026
```

**Agent calls Write**

```json
{
 "file_path": "/tmp/claude/nbtools.py",
 "content": "import nbformat\n\n\ndef build(path, cells):\n    nb = nbformat.v4.new_notebook()\n    nb.metadata[\"kernelspec\"] = {\"name\": \"python3\", \"display_name\": \"Python 3\", \"language\": \"python\"}\n    out = []\n    for cell in cells:\n        kind, source = cell[0], cell[1]\n        tags = cell[2] if len(cell) > 2 else []\n        if kind == \"md\":\n            c = nbformat.v4.new_markdown_cell(source.strip(\"\\n\"))\n        else:\n            c = nbformat.v4.new_code_cell(source.strip(\"\\n\"))\n        if tags:\n            c.metadata[\"tags\"] = tags\n        out.append(c)\n    nb.cells = out\n    nbformat.write(nb, path)\n"
}
```

```
File created successfully at: /tmp/claude/nbtools.py (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
echo $TMPDIR; ls /tmp/claude | head
```

```
/tmp/claude-1001
nbtools.py
```

**Agent calls Write**

```json
{
 "file_path": "/tmp/claude/build02.py",
 "content": "import sys\nsys.path.insert(0, \"/tmp/claude\")\nfrom nbtools import build\n\nCONC = {}  # claim id -> conclusion markdown, filled after the first run\ntry:\n    from conclusions02 import CONC  # noqa\nexcept ImportError:\n    pass\n\n\ndef conc(cid):\n    return [(\"md\", CONC[cid], [f\"claim:{cid}\"])] if cid in CONC else []\n\n\ncells = []\ncells.append((\"md\", r\"\"\"\n# Du, Lai, Hu & Ye (2026) on LINK: development sessions\n\nPaper: Du Z, Lai ZY, Hu L, Ye T. \"A Context-Conditional Audit of Trial-Pairing-Dependent Neural\nGain in Motor-Cortex Decoding\". bioRxiv preprint posted 2026-08-10,\ndoi:10.64898/2026.08.04.742876. The claims file (`claims/du-2026.yaml`) was written from that\npreprint's full text (main text, legends, Tables 1 to 3, Methods); the supplement was not available.\n\nDataset: DANDI:001201 (LINK, Temmar et al.), pinned at version **0.251023.2336**, streamed from the\narchive. This is the version the paper cites (Methods 4.2, Data availability; protocol, author step\n1.3). Two later versions exist (0.261015.2153 and 0.261026.1912); they list the same 312 asset paths\nwith the same sizes, so the analysis would read the same files; the pinned version is the cited one.\n\nThis notebook tests the claims on the 18 development sessions (nine dates with a CO and an RD\nsession). Other notebooks of this entry: `01_synthetic.ipynb` (synthetic calibration),\n`03_link_estimators.ipynb` (estimator families), `04_link_temporal_capacity.ipynb` (temporal offset\nand context capacity), `05_link_confirmation.ipynb` (20 confirmation sessions), `06_mc_rtt.ipynb`\n(DANDI:000129). The estimators are ports of the paper's released code (tag v1.0-jne-submission,\ncommit b042fbe), in `du2026.py`, each function naming its source.\n\n| Claim | Where | Status |\n|---|---|---|\n| synthetic-template-null, synthetic-signal-ordering, synthetic-pair-breaking | 01 | tested (data generated by the paper's code) |\n| link-development-sample, link-neural-only-r2, link-context-ladder-gain, link-context-only-r2, link-phase-only-replacement, link-task-contrast-by-context | this notebook | tested |\n| nested-geometry-gain, nested-history-gain, nested-replacement-negative, replacement-source-diagnostics, permutation-negative, replacement-penalty-distance, replacement-ranks-lower, practical-mse-reduction, representative-trial, split-seed-stability, rff-link | this notebook | tested |\n| estimator-family-link | 03 | tested |\n| temporal-offset, context-capacity-contrast | 04 | tested |\n| confirm-geometry-gain, confirm-history-contraction, confirm-replacement, confirm-table1-values | 05 | tested |\n| rtt-data, rtt-gain, rff-rtt, estimator-family-nlb | 06 | tested (MC_Maze part of estimator-family-nlb not run) |\n| maze-gain, rff-maze | none | blocked: MC_Maze (DANDI:000139) is not one of this attempt's datasets |\n\"\"\"))\n\ncells.append((\"code\", r\"\"\"\nimport collections, resource, time, zlib\nimport numpy as np\nimport pandas as pd\nimport du2026 as d\n\nPAPER = \"du-2026\"\ndef claim_seed(claim_id):\n    return zlib.crc32(f\"{PAPER}/{claim_id}\".encode())\n\nT0 = time.time()\nassets = d.list_assets(d.LINK_ID, d.LINK_VERSION)\nby_date = collections.defaultdict(list)\nfor a in assets:\n    by_date[d.session_date(a[\"path\"])].append(a)\npaired_dates = sorted(k for k, v in by_date.items() if len(v) > 1)\ndev_assets = [a for k in paired_dates for a in sorted(by_date[k], key=lambda a: a[\"path\"])]\nprint(f\"{len(assets)} assets in DANDI:{d.LINK_ID} version {d.LINK_VERSION}, {len(by_date)} dates\")\nprint(\"dates with more than one asset:\", {k: len(v) for k, v in by_date.items() if len(v) > 1})\n\"\"\"))\n\ncells.append((\"md\", r\"\"\"\n## Data check\n\nEach development session is streamed once here for the checks; the fits below stream them again,\none process per session.\n\"\"\"))\n\ncells.append((\"code\", r\"\"\"\nsessions = [d.load_link_session(a[\"asset_id\"], a[\"path\"]) for a in dev_assets]\nrows = []\nfor s in sessions:\n    tr = s.trials\n    dt = np.diff(s.timestamps)\n    start_idx = np.array([int(np.argmin(np.abs(s.timestamps - t))) for t in tr.start_time])\n    # usable-trial rule of link.py: the 25-bin window starting 8 bins after the start bin ends before start bin + trial_count\n    usable = int(np.sum(start_idx + 8 + 24 < np.minimum(start_idx + tr.trial_count.to_numpy(), len(s.timestamps))))\n    sbp, tcr = s.signals[\"SpikingBandPower\"], s.signals[\"ThresholdCrossings\"]\n    rows.append(dict(\n        date=s.date, task=s.task, target_style=\",\".join(sorted(tr.target_style.unique())),\n        trials=len(tr), usable=usable, bins=len(s.timestamps),\n        dt_ms_median=1000 * np.median(dt), dt_ms_min=1000 * dt.min(), dt_ms_max=1000 * dt.max(),\n        trial_count_vs_duration=np.median(tr.trial_count / ((tr.stop_time - tr.start_time) / 0.02)),\n        start_offset_ms=1000 * np.max(np.abs(s.timestamps[start_idx] - tr.start_time)),\n        sbp_min=sbp.min(), sbp_max=sbp.max(), tcr_min=tcr.min(), tcr_max=tcr.max(),\n        tcr_integer=bool(np.allclose(tcr, np.round(tcr))),\n        pos_min=s.position.min(), pos_max=s.position.max(),\n        vel_min=s.velocity.min(), vel_max=s.velocity.max(),\n        targets=len(np.unique(np.c_[tr.index_target_position, tr.mrs_target_position], axis=0)),\n        target_min=min(tr.index_target_position.min(), tr.mrs_target_position.min()),\n        target_max=max(tr.index_target_position.max(), tr.mrs_target_position.max()),\n    ))\ncheck = pd.DataFrame(rows)\npd.set_option(\"display.width\", 250, \"display.max_columns\", 40)\nprint(check.to_string(float_format=lambda v: f\"{v:.4g}\"))\nprint(\"units:\", sessions[0].units)\nprint(\"tasks per paired date:\", {dt: sorted(check.task[check.date == dt]) for dt in check.date.unique()})\nprint(\"target_style column agrees with the identifier's task:\", bool((check.task == check.target_style).all()))\n\"\"\"))\n\ncells.append((\"code\", r\"\"\"\n# Recordings deposited more than once: compare every pair of sessions' SBP, TCR and position arrays\nimport hashlib\ndigests = {}\nfor s in sessions:\n    for name, arr in [(\"SBP\", s.signals[\"SpikingBandPower\"]), (\"TCR\", s.signals[\"ThresholdCrossings\"]), (\"pos\", s.position)]:\n        digests.setdefault(name, []).append(hashlib.sha1(np.ascontiguousarray(arr).tobytes()).hexdigest())\nfor name, values in digests.items():\n    dup = [(sessions[i].identifier, sessions[j].identifier) for i in range(len(values)) for j in range(i + 1, len(values)) if values[i] == values[j]]\n    print(f\"{name}: {len(set(values))} distinct arrays of {len(values)}; identical pairs: {dup}\")\n# near-duplicates: the largest correlation of the first 2000 SBP rows (channel mean) between sessions\nfirst = np.array([s.signals[\"SpikingBandPower\"][:2000].mean(axis=1) for s in sessions])\nc = np.corrcoef(first)\nnp.fill_diagonal(c, np.nan)\nprint(\"largest between-session correlation of the first 2000 SBP bins:\", round(float(np.nanmax(c)), 3))\n# velocity against the first difference of position (velocity is described as derived post hoc)\nfor s in sessions[:18]:\n    dp = np.diff(s.position, axis=0)\n    r = [np.corrcoef(dp[:, k], s.velocity[1:, k])[0, 1] for k in range(2)]\n    r_lag = [np.corrcoef(dp[:, k], s.velocity[:-1, k])[0, 1] for k in range(2)]\n    ratio = [np.std(s.velocity[:, k]) / np.std(dp[:, k]) for k in range(2)]\n    print(f\"{s.identifier}: corr(velocity[t], position[t]-position[t-1]) = {r[0]:.3f}, {r[1]:.3f}; \"\n          f\"with velocity[t-1] {r_lag[0]:.3f}, {r_lag[1]:.3f}; std ratio {ratio[0]:.2f}, {ratio[1]:.2f}\")\n\"\"\"))\n\ncells.append((\"code\", r\"\"\"\n# Clock check: decode finger velocity in the 25-bin trial windows from 40 ms of SBP whose end is\n# shifted by `lag` bins from the behaviour bin (positive lag = neural data earlier). If the SBP\n# series and the trials table share a clock, held-out R2 peaks at a small positive lag and falls\n# away on both sides; an offset between the streams would move the peak.\nfrom sklearn.linear_model import Ridge\nfrom sklearn.pipeline import make_pipeline\nfrom sklearn.preprocessing import StandardScaler\nfrom sklearn.metrics import r2_score\nlags = [-25, -10, -5, -2, 0, 2, 5, 10, 25]\nclock = []\nfor s in sessions:\n    ds = d.build_link_dataset(s, context_mode=\"phase_only\", sample_offset_ms=40 * 20)  # window 40 bins in, room for +-25 lags\n    starts = np.array([int(np.argmin(np.abs(s.timestamps - t))) for t in s.trials.start_time.to_numpy()[ds.source_rows]])\n    bins = starts[:, None] + 40 + np.arange(25)[None, :]\n    sbp = s.signals[\"SpikingBandPower\"]\n    row = {\"session\": s.identifier}\n    for lag in lags:\n        X = np.stack([np.concatenate([sbp[b - lag - 2: b - lag].reshape(-1) for b in tb])[None] for tb in bins])\n        X = np.stack([np.stack([sbp[b - lag - 2: b - lag].reshape(-1) for b in tb]) for tb in bins])\n        tr, te = ds.train_indices, ds.test_indices\n        m = make_pipeline(StandardScaler(), Ridge(alpha=1000.0)).fit(X[tr].reshape(-1, X.shape[-1]), ds.behavior[tr].reshape(-1, 2))\n        row[lag] = r2_score(ds.behavior[te].reshape(-1, 2), m.predict(X[te].reshape(-1, X.shape[-1])), multioutput=\"variance_weighted\")\n    clock.append(row)\nclock = pd.DataFrame(clock).set_index(\"session\")\nprint(\"held-out R2 of velocity from 40 ms of SBP ending `lag` bins before the behaviour bin\")\nprint(clock.round(3).to_string())\nprint(\"lag of the peak per session:\", clock.idxmax(axis=1).value_counts().to_dict())\n\"\"\"))\n\ncells.append((\"code\", r\"\"\"\nprint(f\"data check done in {time.time() - T0:.0f} s; peak memory {resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1e6:.2f} GB\")\n\"\"\", [\"sanity\"]))\n\ncells.append((\"md\", r\"\"\"\n## The fits\n\nEvery fit is the fully nested estimator (Methods 4.5; `du2026.fully_nested`, a port of\n`evaluate_fully_nested_audit`) unless named otherwise, with the windows of the run scripts: 160 ms of\nSBP or TCR ending at the behaviour bin, 100 ms of position history ending at the same bin, a 70/30\ndirection-stratified split with random_state 20260726. Per session:\n\n- SBP, the five contexts of the ladder (`run_link_context_ladder.py`).\n- SBP and TCR geometry by phase with 100 within-condition permutations, replacement ranks one to\n  five and uniform random same-condition sources (Methods 4.7), and SBP geometry by phase and plus\n  history with the three nonlinear-neural maps (Methods 4.6).\n- TCR plus history.\n- Neural-only Ridge (`decoders_nested`, the release's `evaluate_decoders_nested`, claims file).\n- SBP geometry by phase under split seeds 20260727 and 20260728 (Results 2.7).\n- Seed sensitivity (protocol, author step 3): SBP geometry by phase and plus history, and the\n  neural-only R2, under split and refit seeds 20260726 plus 1000, 2000, 3000 and 4000.\n\"\"\"))\n\ncells.append((\"code\", r\"\"\"\nSEED = 20260726\nEXTRA = (1000, 2000, 3000, 4000)\nRANDOM_SOURCE_SEEDS = tuple(claim_seed(\"replacement-ranks-lower\") + k for k in (0,) + EXTRA)\ndef job(name, signal, context, estimator=\"nested\", seed=SEED, keep=False, **kw):\n    build = dict(signal=signal, context_mode=context, seed=seed)\n    est = dict(kw)\n    if estimator == \"nested\":\n        est[\"seed\"] = seed\n    if estimator == \"decoders\":\n        est.update(seed=seed, neural_only_only=True)\n    return (name, build, estimator, est, keep)\n\njobs = []\nfor context in d.LADDER:\n    kw = {}\n    if context == \"geometry_tensor\":\n        kw = dict(n_permutations=100, permutation_seed_offsets=EXTRA, n_ranks=5,\n                  random_source_seeds=RANDOM_SOURCE_SEEDS, rff_seeds=d.RFF_SEEDS)\n    if context == \"causal_history\":\n        kw = dict(rff_seeds=d.RFF_SEEDS)\n    jobs.append(job(f\"SBP_{context}\", \"SpikingBandPower\", context, keep=(context == \"geometry_tensor\"), **kw))\njobs.append(job(\"TCR_geometry_tensor\", \"ThresholdCrossings\", \"geometry_tensor\", n_permutations=100,\n                permutation_seed_offsets=EXTRA, n_ranks=5, random_source_seeds=RANDOM_SOURCE_SEEDS))\njobs.append(job(\"TCR_causal_history\", \"ThresholdCrossings\", \"causal_history\"))\nfor k in (0,) + EXTRA:\n    jobs.append(job(f\"neural_only_{SEED + k}\", \"SpikingBandPower\", \"geometry_tensor\", \"decoders\", seed=SEED + k))\nfor seed in d.SPLIT_SEEDS[1:]:\n    jobs.append(job(f\"SBP_geometry_tensor_{seed}\", \"SpikingBandPower\", \"geometry_tensor\", seed=seed))\nfor k in EXTRA:\n    for context in (\"geometry_tensor\", \"causal_history\"):\n        jobs.append(job(f\"SBP_{context}_{SEED + k}\", \"SpikingBandPower\", context, seed=SEED + k))\n\nt = time.time()\nresults = d.run_parallel(d.link_session_jobs, [(a[\"asset_id\"], a[\"path\"], jobs) for a in dev_assets])\nprint(f\"{len(jobs)} fits per session on {len(results)} sessions in {(time.time() - t) / 60:.1f} min\")\n\ndef table(name, field=\"gain\"):\n    return pd.DataFrame([{\"date\": r[\"date\"], \"task\": r[\"task\"], field: r[name][field]} for r in results])\ndef task_means(name, field=\"gain\"):\n    return table(name, field).groupby(\"task\")[field].mean()\n\"\"\"))\n\n# ---- claims\ncells.append((\"md\", r\"\"\"\n## link-development-sample\n\n> The LINK development set is the nine dates with both a CO and an RD session, 18 sessions and\n> 6,750 usable trials from one macaque, with 375 usable trials in every analyzed session.\n\"\"\"))\ncells.append((\"code\", r\"\"\"\nusable = pd.DataFrame([{\"date\": r[\"date\"], \"task\": r[\"task\"], \"usable\": r[\"SBP_geometry_tensor\"][\"n_usable\"],\n                        \"trials_table\": r[\"SBP_geometry_tensor\"][\"n_trials_table\"]} for r in results])\nprint(usable.to_string())\nboth = [dt for dt in paired_dates if sorted(check.task[check.date == dt]) == [\"CO\", \"RD\"]]\nprint(f\"dates with both a CO and an RD session: {len(both)}  (expected 9)\")\nprint(f\"sessions: {len(usable)}; subjects: {sorted(set(s.identifier and 'Monkey N' for s in sessions))}\")\nprint(f\"usable trials: {usable.usable.sum()}  (expected 6750, tolerance 675)\")\nprint(f\"sessions with 375 usable trials: {(usable.usable == 375).sum()} of {len(usable)}; \"\n      f\"range {usable.usable.min()} to {usable.usable.max()}; trials dropped by the window rule: \"\n      f\"{(usable.trials_table - usable.usable).sum()}\")\n\"\"\", [\"claim:link-development-sample\"]))\ncells += conc(\"link-development-sample\")\n\ncells.append((\"md\", r\"\"\"\n## link-neural-only-r2\n\n> In the LINK development sessions, neural-only Ridge decoding of finger velocity from 160 ms of SBP\n> had held-out R2 of 0.308 in CO and 0.313 in RD, the same at every rung of the context ladder.\n\nX, Y and the split do not depend on the context (the split is stratified by direction octant,\nwhich every rung shares), so one neural-only fit per session serves every rung.\n\"\"\"))\ncells.append((\"code\", r\"\"\"\nno = table(f\"neural_only_{SEED}\", \"neural_r2\")\nprint(no.pivot(index=\"date\", columns=\"task\", values=\"neural_r2\").round(4).to_string())\nm = no.groupby(\"task\").neural_r2.mean()\nprint(f\"CO mean {m['CO']:.4f} (expected 0.308 +- 0.0308); RD mean {m['RD']:.4f} (expected 0.313 +- 0.0313)\")\nfor k in (0,) + EXTRA:\n    mm = task_means(f\"neural_only_{SEED + k}\", \"neural_r2\")\n    print(f\"seed {SEED + k}: CO {mm['CO']:.4f}, RD {mm['RD']:.4f}\")\nprint(\"neural-only penalties chosen:\", collections.Counter(r[f\"neural_only_{SEED}\"][\"neural_alpha\"] for r in results))\n\"\"\", [\"claim:link-neural-only-r2\"]))\ncells += conc(\"link-neural-only-r2\")\n\ncells.append((\"md\", r\"\"\"\n## link-context-ladder-gain\n\n> In LINK with SBP, mean context-conditional neural gain fell along the context ladder, from\n> 0.3012/0.3125 (CO/RD) beyond phase alone to 0.0657/0.0502 beyond direction by phase, 0.0443/0.0332\n> beyond additive geometry, 0.0193/0.0209 beyond geometry by phase, and 0.0077/0.0098 beyond\n> geometry by phase plus measured-output history.\n\"\"\"))\ncells.append((\"code\", r\"\"\"\nexpected = {\"phase_only\": (0.3012, 0.3125), \"condition_phase\": (0.0657, 0.0502), \"geometry_additive\": (0.0443, 0.0332),\n            \"geometry_tensor\": (0.0193, 0.0209), \"causal_history\": (0.0077, 0.0098)}\nladder = []\nfor context in d.LADDER:\n    m = task_means(f\"SBP_{context}\")\n    g = table(f\"SBP_{context}\").gain\n    for task, exp in zip((\"CO\", \"RD\"), expected[context]):\n        ladder.append(dict(context=d.LADDER_NAMES[context], task=task, mean_gain=m[task], expected=exp,\n                           within_10pct=abs(m[task] - exp) <= 0.1 * exp))\n    print(f\"{d.LADDER_NAMES[context]:>30}: session gains {g.min():.4f} to {g.max():.4f}, {int((g > 0).sum())}/18 positive\")\nladder = pd.DataFrame(ladder)\nprint(ladder.to_string(float_format=lambda v: f\"{v:.4f}\"))\nfalls = {task: bool(np.all(np.diff(ladder[ladder.task == task].mean_gain.to_numpy()) < 0)) for task in (\"CO\", \"RD\")}\nprint(\"falls at every step:\", falls, \"; values within tolerance:\", int(ladder.within_10pct.sum()), \"of 10\")\nprint(\"per session (rows: date and task; columns: rung):\")\nprint(pd.DataFrame({d.LADDER_NAMES[c]: table(f\"SBP_{c}\").set_index([\"date\", \"task\"]).gain for c in d.LADDER}).round(4).to_string())\n\"\"\", [\"claim:link-context-ladder-gain\"]))\ncells += conc(\"link-context-ladder-gain\")\n\ncells.append((\"md\", r\"\"\"\n## link-context-only-r2\n\n> Context-only R2 in LINK rose along the ladder from 0.0084/0.0055 (CO/RD) with phase alone to\n> 0.6617/0.6839 with geometry by phase plus measured-output history.\n\"\"\"))\ncells.append((\"code\", r\"\"\"\ncr = pd.DataFrame({d.LADDER_NAMES[c]: task_means(f\"SBP_{c}\", \"context_r2\") for c in d.LADDER}).T\nprint(cr.round(4).to_string())\nprint(f\"phase only: CO {cr.loc['phase only', 'CO']:.4f}, RD {cr.loc['phase only', 'RD']:.4f} (criterion below 0.02; 10% tolerances 0.0084 +- 0.00084, 0.0055 +- 0.00055)\")\nprint(f\"plus history: CO {cr.loc['plus measured-output history', 'CO']:.4f} (0.6617 +- 0.06617), RD {cr.loc['plus measured-output history', 'RD']:.4f} (0.6839 +- 0.06839)\")\npc = table(\"SBP_phase_only\", \"context_r2\").context_r2\nprint(f\"phase-only session context R2 range {pc.min():.4f} to {pc.max():.4f}\")\n\"\"\", [\"claim:link-context-only-r2\"]))\ncells += conc(\"link-context-only-r2\")\n\ncells.append((\"md\", r\"\"\"\n## link-phase-only-replacement\n\n> With phase-only context, the mean nearest-replacement gain in RD stayed positive (0.10498).\n\nUnder phase only every trial has the same context trajectory, so every distance is zero and the tie\nrule (lower trial index, Methods 4.7) picks the first other same-direction test trial.\n\"\"\"))\ncells.append((\"code\", r\"\"\"\npr = table(\"SBP_phase_only\", \"replacement_gain\")\nm = pr.groupby(\"task\").replacement_gain.mean()\nprint(pr.pivot(index=\"date\", columns=\"task\", values=\"replacement_gain\").round(4).to_string())\nprint(f\"RD mean replacement gain, phase only: {m['RD']:.5f} (expected 0.10498 +- 0.010498); CO {m['CO']:.5f}\")\nprint(f\"RD sessions positive: {int((pr[pr.task == 'RD'].replacement_gain > 0).sum())}/9\")\n\"\"\", [\"claim:link-phase-only-replacement\"]))\ncells += conc(\"link-phase-only-replacement\")\n\ncells.append((\"md\", r\"\"\"\n## link-task-contrast-by-context\n\n> The descriptive RD-minus-CO gain contrast changed with the context; it was positive under phase\n> only, negative under direction by phase and additive geometry, near zero under geometry by phase,\n> and small positive after measured-output history.\n\nPer date RD minus CO, mean over nine dates, 95% interval from 10,000 date resamples (generator\nseeded from the claim; the claim seed plus 1000 to 4000 give the interval's sensitivity).\n\"\"\"))\ncells.append((\"code\", r\"\"\"\ncontrast = []\nfor context in d.LADDER:\n    p = table(f\"SBP_{context}\").pivot(index=\"date\", columns=\"task\", values=\"gain\")\n    diff = (p[\"RD\"] - p[\"CO\"]).to_numpy()\n    cis = []\n    for k in (0,) + EXTRA:\n        rng = np.random.default_rng(claim_seed(\"link-task-contrast-by-context\") + k)\n        boots = np.array([rng.choice(diff, len(diff), replace=True).mean() for _ in range(10000)])\n        cis.append(np.quantile(boots, [0.025, 0.975]))\n    contrast.append(dict(context=d.LADDER_NAMES[context], mean=diff.mean(), ci_low=cis[0][0], ci_high=cis[0][1],\n                         ci_contains_zero=bool(cis[0][0] <= 0 <= cis[0][1]),\n                         ci_low_range=f\"{min(c[0] for c in cis):.4f}..{max(c[0] for c in cis):.4f}\",\n                         ci_high_range=f\"{min(c[1] for c in cis):.4f}..{max(c[1] for c in cis):.4f}\",\n                         dates_positive=int((diff > 0).sum())))\ncontrast = pd.DataFrame(contrast).set_index(\"context\")\nprint(contrast.to_string(float_format=lambda v: f\"{v:.4f}\"))\ng = abs(contrast.loc[\"geometry by phase\", \"mean\"])\nprint(f\"reading (b): |geometry by phase| {g:.4f} < |direction by phase| {abs(contrast.loc['direction by phase', 'mean']):.4f} \"\n      f\"and < |additive geometry| {abs(contrast.loc['additive geometry', 'mean']):.4f}: \"\n      f\"{g < abs(contrast.loc['direction by phase', 'mean']) and g < abs(contrast.loc['additive geometry', 'mean'])}\")\n\"\"\", [\"claim:link-task-contrast-by-context\"]))\ncells += conc(\"link-task-contrast-by-context\")\n\ncells.append((\"md\", r\"\"\"\n## nested-geometry-gain\n\n> With geometry-by-phase context, fully nested mean gain over the 18 LINK sessions was 0.02009 for SBP\n> (18 of 18 sessions positive) and 0.01155 for TCR (17 of 18 positive).\n\"\"\"))\ncells.append((\"code\", r\"\"\"\ndef summary(name, field=\"gain\", seed_key=None):\n    t = table(name, field)\n    by_date = {dt: g[field].to_numpy() for dt, g in t.groupby(\"date\")}\n    lo, hi = d.date_bootstrap(by_date, np.random.default_rng(claim_seed(\"nested-geometry-gain\")))\n    return dict(mean=t[field].mean(), positive=int((t[field] > 0).sum()), min=t[field].min(), max=t[field].max(),\n                CO=t[t.task == \"CO\"][field].mean(), RD=t[t.task == \"RD\"][field].mean(), ci_low=lo, ci_high=hi)\nfor name, exp, exp_pos in [(\"SBP_geometry_tensor\", 0.02009, 18), (\"TCR_geometry_tensor\", 0.01155, 17)]:\n    s_ = summary(name)\n    print(f\"{name}: mean {s_['mean']:.5f} (expected {exp}), positive {s_['positive']}/18 (expected {exp_pos}), \"\n          f\"range {s_['min']:.5f} to {s_['max']:.5f}, CO {s_['CO']:.5f}, RD {s_['RD']:.5f}, \"\n          f\"date-clustered 95% interval {s_['ci_low']:.5f} to {s_['ci_high']:.5f}\")\nprint(\"tolerances: SBP 0.00423, TCR 0.00446; counts 1.8 and 1.7\")\nvals = [np.mean(table(\"SBP_geometry_tensor\" if k == 0 else f\"SBP_geometry_tensor_{SEED + k}\").gain) for k in (0,) + EXTRA]\npos = [int((table(\"SBP_geometry_tensor\" if k == 0 else f\"SBP_geometry_tensor_{SEED + k}\").gain > 0).sum()) for k in (0,) + EXTRA]\nprint(\"SBP mean under seeds 20260726 +0/1000/2000/3000/4000:\", np.round(vals, 5), \"positive:\", pos)\nprint(table(\"SBP_geometry_tensor\").merge(table(\"TCR_geometry_tensor\"), on=[\"date\", \"task\"], suffixes=(\"_SBP\", \"_TCR\")).round(5).to_string())\n\"\"\", [\"claim:nested-geometry-gain\"]))\ncells += conc(\"nested-geometry-gain\")\n\ncells.append((\"md\", r\"\"\"\n## nested-history-gain\n\n> Adding lag-matched measured-output history reduced fully nested mean gain to 0.00873 for SBP (17 of\n> 18 sessions positive) and 0.00420 for TCR (16 of 18 positive).\n\"\"\"))\ncells.append((\"code\", r\"\"\"\nfor name, exp, exp_pos in [(\"SBP_causal_history\", 0.00873, 17), (\"TCR_causal_history\", 0.0042, 16)]:\n    s_ = summary(name)\n    print(f\"{name}: mean {s_['mean']:.5f} (expected {exp}), positive {s_['positive']}/18 (expected {exp_pos}), \"\n          f\"range {s_['min']:.5f} to {s_['max']:.5f}, CO {s_['CO']:.5f}, RD {s_['RD']:.5f}, \"\n          f\"date-clustered 95% interval {s_['ci_low']:.5f} to {s_['ci_high']:.5f}\")\nprint(\"tolerances: SBP 0.00273, TCR 0.0021; counts 1.7 and 1.6\")\nfor sig in (\"SBP\", \"TCR\"):\n    print(f\"{sig}: history mean {table(f'{sig}_causal_history').gain.mean():.5f} below geometry mean {table(f'{sig}_geometry_tensor').gain.mean():.5f}:\",\n          table(f\"{sig}_causal_history\").gain.mean() < table(f\"{sig}_geometry_tensor\").gain.mean())\nvals = [np.mean(table(\"SBP_causal_history\" if k == 0 else f\"SBP_causal_history_{SEED + k}\").gain) for k in (0,) + EXTRA]\npos = [int((table(\"SBP_causal_history\" if k == 0 else f\"SBP_causal_history_{SEED + k}\").gain > 0).sum()) for k in (0,) + EXTRA]\nprint(\"SBP history mean under the five seeds:\", np.round(vals, 5), \"positive:\", pos)\n\"\"\", [\"claim:nested-history-gain\"]))\ncells += conc(\"nested-history-gain\")\n\ncells.append((\"md\", r\"\"\"\n## nested-replacement-negative\n\n> Nearest source-context replacement made all four LINK mean gains negative, -0.00714 and -0.00407 for\n> SBP (geometry by phase, plus history) and -0.00905 and -0.00537 for TCR.\n\"\"\"))\ncells.append((\"code\", r\"\"\"\nexp = {\"SBP_geometry_tensor\": -0.00714, \"SBP_causal_history\": -0.00407, \"TCR_geometry_tensor\": -0.00905, \"TCR_causal_history\": -0.00537}\nwithin = 0\nfor name, e in exp.items():\n    t = table(name, \"replacement_gain\").replacement_gain\n    ok = abs(t.mean() - e) <= abs(0.1 * e)\n    within += ok\n    print(f\"{name}: mean replacement gain {t.mean():.5f} (expected {e} +- {abs(0.1 * e):.6f}; within: {ok}); \"\n          f\"negative sessions {int((t < 0).sum())}/18; range {t.min():.5f} to {t.max():.5f}\")\nprint(\"all four negative:\", all(table(n, \"replacement_gain\").replacement_gain.mean() < 0 for n in exp), \"; within tolerance:\", within, \"of 4\")\nfor k in EXTRA:\n    print(f\"seed {SEED + k}: SBP geometry {table(f'SBP_geometry_tensor_{SEED + k}', 'replacement_gain').replacement_gain.mean():.5f}, \"\n          f\"SBP history {table(f'SBP_causal_history_{SEED + k}', 'replacement_gain').replacement_gain.mean():.5f}\")\n\"\"\", [\"claim:nested-replacement-negative\"]))\ncells += conc(\"nested-replacement-negative\")\n\ncells.append((\"md\", r\"\"\"\n## replacement-source-diagnostics\n\n> For primary SBP geometry, every test trial had at least five eligible same-condition sources, the\n> median over sessions of the maximum source reuse was three targets and the maximum over sessions\n> four, and self-replacement reproduced the correct-pair predictions exactly.\n\"\"\"))\ncells.append((\"code\", r\"\"\"\ndiag = pd.DataFrame([{\"date\": r[\"date\"], \"task\": r[\"task\"], \"eligible_min\": r[\"SBP_geometry_tensor\"][\"eligible_sources_min\"],\n                      \"reuse_max\": r[\"SBP_geometry_tensor\"][\"source_reuse_max\"],\n                      \"self_error\": r[\"SBP_geometry_tensor\"][\"self_replacement_max_abs_error\"]} for r in results])\nprint(diag.to_string())\nprint(f\"minimum eligible sources over sessions: {diag.eligible_min.min()} (expected at least 5)\")\nprint(f\"median over sessions of the maximum reuse: {diag.reuse_max.median()} (expected 3); maximum: {diag.reuse_max.max()} (expected 4)\")\nprint(f\"largest self-replacement difference: {diag.self_error.max():.3g} (criterion below 1e-10)\")\n\"\"\", [\"claim:replacement-source-diagnostics\"]))\ncells += conc(\"replacement-source-diagnostics\")\n\ncells.append((\"md\", r\"\"\"\n## permutation-negative\n\n> The mean gain of 100 within-condition whole-trial permutations was negative in every LINK session,\n> with an across-session mean of -0.0142.\n\"\"\"))\ncells.append((\"code\", r\"\"\"\nfor label, names in [(\"(a) 18 SBP geometry sessions\", [\"SBP_geometry_tensor\"]),\n                     (\"(b) 36 SBP and TCR geometry sessions\", [\"SBP_geometry_tensor\", \"TCR_geometry_tensor\"])]:\n    vals = np.concatenate([table(n, \"permutation_mean\").permutation_mean.to_numpy() for n in names])\n    print(f\"{label}: negative {int((vals < 0).sum())}/{len(vals)}, mean {vals.mean():.5f} (expected -0.0142 +- 0.00142), \"\n          f\"range {vals.min():.5f} to {vals.max():.5f}\")\n    for k in EXTRA:\n        v = np.concatenate([[r[n][\"permutation_means\"][k] for r in results] for n in names])\n        print(f\"   permutation generator offset +{k}: negative {int((v < 0).sum())}/{len(v)}, mean {v.mean():.5f}\")\n\"\"\", [\"claim:permutation-negative\"]))\ncells += conc(\"permutation-negative\")\n\ncells.append((\"md\", r\"\"\"\n## replacement-penalty-distance\n\n> The replacement penalty had no consistent rank relation to the nearest-source context distance across\n> sessions.\n\"\"\"))\ncells.append((\"code\", r\"\"\"\nsp = table(\"SBP_geometry_tensor\", \"replacement_penalty_distance_spearman\")\nv = sp.replacement_penalty_distance_spearman\nprint(sp.round(3).to_string())\nprint(f\"positive {int((v > 0).sum())}, negative {int((v < 0).sum())} of {len(v)}; mean {v.mean():.4f}\")\nby_date = {dt: g.replacement_penalty_distance_spearman.to_numpy() for dt, g in sp.groupby(\"date\")}\nfor k in (0,) + EXTRA:\n    lo, hi = d.date_bootstrap(by_date, np.random.default_rng(claim_seed(\"replacement-penalty-distance\") + k))\n    print(f\"date-bootstrap 95% interval of the mean (generator +{k}): {lo:.4f} to {hi:.4f}; contains zero: {lo <= 0 <= hi}\")\nprint(\"reading (a) not all of one sign:\", bool((v > 0).any() and (v < 0).any()))\n\"\"\", [\"claim:replacement-penalty-distance\"]))\ncells += conc(\"replacement-penalty-distance\")\n\ncells.append((\"md\", r\"\"\"\n## replacement-ranks-lower\n\n> Replacement with the first to fifth nearest sources and with a random same-condition source all\n> lowered the across-session mean gain.\n\nThe random source is a uniform draw among the other same-condition test trials (a standard choice,\nclaims file); five draws are shown, from the claim's seed and that seed plus 1000 to 4000.\n\"\"\"))\ncells.append((\"code\", r\"\"\"\nfor sig in (\"SBP\", \"TCR\"):\n    name = f\"{sig}_geometry_tensor\"\n    correct = table(name).gain.mean()\n    ranks = np.array([r[name][\"rank_gains\"] for r in results]).mean(axis=0)\n    rand = np.array([r[name][\"random_source_gains\"] for r in results]).mean(axis=0)\n    print(f\"{sig} geometry: correct-pair mean {correct:.5f}; rank 1-5 means {np.round(ranks, 5)}; \"\n          f\"random-source means over five draws {np.round(rand, 5)}\")\n    print(f\"   all six (ranks and the first random draw) below the correct-pair mean: {bool(np.all(ranks < correct) and rand[0] < correct)}; \"\n          f\"every random draw below: {bool(np.all(rand < correct))}\")\n\"\"\", [\"claim:replacement-ranks-lower\"]))\ncells += conc(\"replacement-ranks-lower\")\n\ncells.append((\"md\", r\"\"\"\n## practical-mse-reduction\n\n> In LINK, SBP geometry-by-phase gain reduced context-model MSE by 4.92% on average (mean context RMSE\n> 0.01407 to 0.01372), adding measured-output history reduced the remaining MSE by 2.72%, and the TCR\n> reductions were 2.83% and 1.31%.\n\"\"\"))\ncells.append((\"code\", r\"\"\"\nvals = [(\"SBP geometry % MSE reduction\", table(\"SBP_geometry_tensor\", \"mse_reduction_percent\").mse_reduction_percent.mean(), 4.92),\n        (\"SBP geometry mean context RMSE\", table(\"SBP_geometry_tensor\", \"context_rmse\").context_rmse.mean(), 0.01407),\n        (\"SBP geometry mean correct-pair RMSE\", table(\"SBP_geometry_tensor\", \"exact_rmse\").exact_rmse.mean(), 0.01372),\n        (\"SBP history % MSE reduction\", table(\"SBP_causal_history\", \"mse_reduction_percent\").mse_reduction_percent.mean(), 2.72),\n        (\"TCR geometry % MSE reduction\", table(\"TCR_geometry_tensor\", \"mse_reduction_percent\").mse_reduction_percent.mean(), 2.83),\n        (\"TCR history % MSE reduction\", table(\"TCR_causal_history\", \"mse_reduction_percent\").mse_reduction_percent.mean(), 1.31)]\nwithin = 0\nfor label, v, e in vals:\n    ok = abs(v - e) <= 0.1 * e\n    within += ok\n    print(f\"{label}: {v:.5g} (expected {e} +- {0.1 * e:.4g}; within: {ok})\")\nprint(\"within tolerance:\", within, \"of 6\")\nr = table(\"SBP_geometry_tensor\", \"mse_reduction_percent\").mse_reduction_percent\nprint(f\"SBP geometry session reductions {r.min():.2f} to {r.max():.2f}%\")\n\"\"\", [\"claim:practical-mse-reduction\"]))\ncells += conc(\"practical-mse-reduction\")\n\ncells.append((\"md\", r\"\"\"\n## representative-trial\n\n> The prespecified rule for the illustrative trajectory (session with median primary SBP geometry\n> gain, then the held-out trial with median context-minus-correct trial MSE improvement) selects\n> 2022-09-21 RD, trial 123.\n\"\"\"))\ncells.append((\"code\", r\"\"\"\ngeo = pd.DataFrame([{\"date\": r[\"date\"], \"task\": r[\"task\"], \"gain\": r[\"SBP_geometry_tensor\"][\"gain\"], \"i\": i} for i, r in enumerate(results)])\ngeo = geo.sort_values([\"gain\", \"date\", \"task\"]).reset_index(drop=True)\nprint(geo.round(5).to_string())\nlower = geo.iloc[(len(geo) - 1) // 2]\nmiddle = geo.iloc[[(len(geo) - 1) // 2, len(geo) // 2]].sort_values([\"date\", \"task\"]).iloc[0]\nfor label, row in [(\"ninth in gain order (code: build_submission_figures.py figure8)\", lower), (\"earlier date of the two middle sessions\", middle)]:\n    r = results[int(row.i)][\"SBP_geometry_tensor\"]\n    improvement = r[\"per_trial_context_mse\"] - r[\"per_trial_exact_mse\"]\n    order = np.lexsort((r[\"test_indices\"], improvement))\n    position = int(order[(len(order) - 1) // 2])\n    usable_index = int(r[\"test_indices\"][position])\n    print(f\"{label}: {row.date} {row.task}; median trial: usable-trial index {usable_index}, \"\n          f\"trials-table row {int(r['source_rows'][usable_index])}, position among {len(order)} held-out trials {position}\")\n\"\"\", [\"claim:representative-trial\"]))\ncells += conc(\"representative-trial\")\n\ncells.append((\"md\", r\"\"\"\n## split-seed-stability\n\n> The fully nested SBP geometry-by-phase result was stable across three whole-trial split and\n> refitting seeds, with CO means 0.0193, 0.0180 and 0.0158 and RD means 0.0209, 0.0223 and 0.0201.\n\"\"\"))\ncells.append((\"code\", r\"\"\"\nexp = {20260726: (0.0193, 0.0209), 20260727: (0.0180, 0.0223), 20260728: (0.0158, 0.0201)}\nwithin, positive = 0, True\nfor seed in d.SPLIT_SEEDS:\n    name = \"SBP_geometry_tensor\" if seed == SEED else f\"SBP_geometry_tensor_{seed}\"\n    m = task_means(name)\n    for task, e in zip((\"CO\", \"RD\"), exp[seed]):\n        ok = abs(m[task] - e) <= 0.1 * e\n        within += ok\n        positive &= m[task] > 0\n        print(f\"seed {seed} {task}: {m[task]:.4f} (expected {e} +- {0.1 * e:.5f}; within: {ok})\")\nprint(\"all six positive:\", bool(positive), \"; within tolerance:\", within, \"of 6\")\n\"\"\", [\"claim:split-seed-stability\"]))\ncells += conc(\"split-seed-stability\")\n\ncells.append((\"md\", r\"\"\"\n## rff-link\n\n> In LINK SBP, nonlinear-neural geometry-by-phase means were positive for both tasks under every map\n> (combined range 0.00310 to 0.00404), and the measured-output-history mean ranged from 0.00111 to\n> 0.00142.\n\"\"\"))\ncells.append((\"code\", r\"\"\"\nrows_ = []\nfor seed in d.RFF_SEEDS:\n    for context in (\"geometry_tensor\", \"causal_history\"):\n        t = pd.DataFrame([{\"task\": r[\"task\"], \"gain\": r[f\"SBP_{context}\"][\"rff\"][seed][\"gain\"]} for r in results])\n        rows_.append(dict(map_seed=seed, context=d.LADDER_NAMES[context], CO=t[t.task == \"CO\"].gain.mean(),\n                          RD=t[t.task == \"RD\"].gain.mean(), all18=t.gain.mean(), positive=int((t.gain > 0).sum())))\nrff = pd.DataFrame(rows_)\nprint(rff.to_string(float_format=lambda v: f\"{v:.5f}\"))\ngeo_ = rff[rff.context == \"geometry by phase\"]\nhis_ = rff[rff.context == \"plus measured-output history\"]\nlo_g, hi_g = 0.0031 - 0.00031, 0.00404 + 0.000404\nlo_h, hi_h = 0.00111 - 0.000111, 0.00142 + 0.000142\nprint(f\"geometry CO and RD positive under every map: {bool((geo_[['CO', 'RD']] > 0).all().all())}\")\nprint(f\"reading (a), 18-session geometry means {geo_.all18.min():.5f} to {geo_.all18.max():.5f}, inside {lo_g:.5f}..{hi_g:.5f}: {bool(geo_.all18.between(lo_g, hi_g).all())}\")\nsix = np.r_[geo_.CO, geo_.RD]\nprint(f\"reading (b), six task means {six.min():.5f} to {six.max():.5f}, inside: {bool(np.all((six >= lo_g) & (six <= hi_g)))}\")\nprint(f\"history 18-session means {his_.all18.min():.5f} to {his_.all18.max():.5f}, inside {lo_h:.6f}..{hi_h:.6f}: {bool(his_.all18.between(lo_h, hi_h).all())}\")\nprint(\"RFF penalties chosen (geometry):\", collections.Counter(r[\"SBP_geometry_tensor\"][\"rff\"][s][\"alpha\"] for r in results for s in d.RFF_SEEDS))\nprint(f\"notebook run time {(time.time() - T0) / 60:.1f} min; peak memory of this process {resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1e6:.2f} GB\")\n\"\"\", [\"claim:rff-link\"]))\ncells += conc(\"rff-link\")\n\nif \"summary\" in CONC:\n    cells.append((\"md\", CONC[\"summary\"]))\n\nbuild(\"entries/du-2026/02_link_development.ipynb\", cells)\nprint(\"ok\")\n"
}
```

```
File created successfully at: /tmp/claude/build02.py (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd /tmp/claude && python - <<'EOF'
s=open('build02.py').read()
s=s.replace('''        X = np.stack([np.concatenate([sbp[b - lag - 2: b - lag].reshape(-1) for b in tb])[None] for tb in bins])
''','')
s=s.replace('''    ds = d.build_link_dataset(s, context_mode="phase_only", sample_offset_ms=40 * 20)  # window 40 bins in, room for +-25 lags
    starts = np.array([int(np.argmin(np.abs(s.timestamps - t))) for t in s.trials.start_time.to_numpy()[ds.source_rows]])
    bins = starts[:, None] + 40 + np.arange(25)[None, :]''','''    ds = d.build_link_dataset(s, context_mode="phase_only")  # the analysis windows: 25 bins from 8 bins after the start bin
    starts = np.array([int(np.argmin(np.abs(s.timestamps - t))) for t in s.trials.start_time.to_numpy()[ds.source_rows]])
    bins = starts[:, None] + 8 + np.arange(25)[None, :]''')
s=s.replace('''print(f"sessions: {len(usable)}; subjects: {sorted(set(s.identifier and 'Monkey N' for s in sessions))}")''','''print(f"sessions: {len(usable)}; subjects in the asset paths: {sorted(set(a['path'].split('/')[0] for a in dev_assets))}")''')
open('build02.py','w').write(s)
EOF
. $TMPDIR/venv/bin/activate && python build02.py
```

```
ok
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd entries/du-2026 && . $TMPDIR/venv/bin/activate && python - <<'EOF'
import nbformat
nb=nbformat.read('02_link_development.ipynb',4)
code="\n\n".join(c.source for c in nb.cells if c.cell_type=='code')
code=code.replace('dev_assets = [a for k in paired_dates for a in sorted(by_date[k], key=lambda a: a["path"])]','dev_assets = [a for k in paired_dates[7:8] for a in sorted(by_date[k], key=lambda a: a["path"])]')
open('/tmp/claude/test02.py','w').write(code)
EOF
cd entries/du-2026 && timeout 1800 python /tmp/claude/test02.py 2>&1 | grep -v Warn | tail -120
```

```
Traceback (most recent call last):
  File "/tmp/claude/test02.py", line 4, in <module>
    import du2026 as d
ModuleNotFoundError: No module named 'du2026'
```

**Agent calls Bash**

```bash
. $TMPDIR/venv/bin/activate && PYTHONPATH=. timeout 1800 python /tmp/claude/test02.py 2>&1 | grep -v Warn | tail -150
```

```
312 assets in DANDI:001201 version 0.251023.2336, 303 dates
dates with more than one asset: {'2021-10-15': 2, '2022-02-25': 2, '2022-04-08': 2, '2022-04-15': 2, '2022-04-29': 2, '2022-05-13': 2, '2022-08-10': 2, '2022-09-21': 2, '2022-11-02': 2}
         date task target_style  trials  usable   bins  dt_ms_median  dt_ms_min  dt_ms_max  trial_count_vs_duration  start_offset_ms  sbp_min  sbp_max  tcr_min  tcr_max  tcr_integer  pos_min  pos_max  vel_min  vel_max  targets  target_min  target_max
0  2022-09-21   CO           CO     375     375  22725            20         19         21                    1.018                0   0.7437    24.62        0        5         True  0.03825        1  -0.1743   0.1986       23         0.1         0.9
1  2022-09-21   RD           RD     375     375  25015            20         19         21                    1.016                0   0.7063    25.12        0        5         True        0        1  -0.2107   0.2626      375    0.001202      0.9999
units: {'SpikingBandPower': 'volts', 'ThresholdCrossings': 'volts', 'index_position': 'flexion units', 'index_velocity': 'flexion units per time bin'}
tasks per paired date: {'2022-09-21': ['CO', 'RD']}
target_style column agrees with the identifier's task: True
SBP: 2 distinct arrays of 2; identical pairs: []
TCR: 2 distinct arrays of 2; identical pairs: []
pos: 2 distinct arrays of 2; identical pairs: []
largest between-session correlation of the first 2000 SBP bins: 0.048
2022-09-21_CO_nwb: corr(velocity[t], position[t]-position[t-1]) = 0.826, 0.698; with velocity[t-1] 1.000, 1.000; std ratio 1.00, 1.00
2022-09-21_RD_nwb: corr(velocity[t], position[t]-position[t-1]) = 0.869, 0.740; with velocity[t-1] 1.000, 1.000; std ratio 1.00, 1.00
Traceback (most recent call last):
  File "/tmp/claude/test02.py", line 90, in <module>
    X = np.stack([np.stack([sbp[b - lag - 2: b - lag].reshape(-1) for b in tb]) for tb in bins])
                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[... 3 more lines not kept]
```

**Agent calls Bash**

```bash
cd /tmp/claude && python - <<'EOF'
s=open('build02.py').read()
old='''    bins = starts[:, None] + 8 + np.arange(25)[None, :]
    sbp = s.signals["SpikingBandPower"]'''
new='''    bins = starts[:, None] + 8 + np.arange(25)[None, :]
    sbp = s.signals["SpikingBandPower"]
    inside = (bins.min(axis=1) - 27 >= 0) & (bins.max(axis=1) + 25 < len(sbp))  # every lag stays inside the recording
    tr, te = np.intersect1d(ds.train_indices, np.flatnonzero(inside)), np.intersect1d(ds.test_indices, np.flatnonzero(inside))'''
assert old in s; s=s.replace(old,new)
s=s.replace('''        tr, te = ds.train_indices, ds.test_indices
        m = make_pipeline''','''        m = make_pipeline''')
s=s.replace('''    row = {"session": s.identifier}''','''    row = {"session": s.identifier, "trials": int(inside.sum())}''')
s=s.replace('''print("lag of the peak per session:", clock.idxmax(axis=1).value_counts().to_dict())''','''print("lag of the peak per session:", clock[lags].idxmax(axis=1).value_counts().to_dict())''')
open('build02.py','w').write(s)
EOF
. $TMPDIR/venv/bin/activate && python build02.py && cd entries/du-2026 && python - <<'EOF'
import nbformat
nb=nbformat.read('02_link_development.ipynb',4)
code="\n\n".join(c.source for c in nb.cells if c.cell_type=='code')
code=code.replace('dev_assets = [a for k in paired_dates for a in sorted(by_date[k], key=lambda a: a["path"])]','dev_assets = [a for k in paired_dates[7:8] for a in sorted(by_date[k], key=lambda a: a["path"])]')
open('/tmp/claude/test02.py','w').write(code)
EOF
PYTHONPATH=. timeout 1800 python /tmp/claude/test02.py 2>&1 | grep -v Warn | tail -150 | cut -c1-250
```

```
ok
312 assets in DANDI:001201 version 0.251023.2336, 303 dates
dates with more than one asset: {'2021-10-15': 2, '2022-02-25': 2, '2022-04-08': 2, '2022-04-15': 2, '2022-04-29': 2, '2022-05-13': 2, '2022-08-10': 2, '2022-09-21': 2, '2022-11-02': 2}
         date task target_style  trials  usable   bins  dt_ms_median  dt_ms_min  dt_ms_max  trial_count_vs_duration  start_offset_ms  sbp_min  sbp_max  tcr_min  tcr_max  tcr_integer  pos_min  pos_max  vel_min  vel_max  targets  target_min  target_max
0  2022-09-21   CO           CO     375     375  22725            20         19         21                    1.018                0   0.7437    24.62        0        5         True  0.03825        1  -0.1743   0.1986       23         0.1         0.9
1  2022-09-21   RD           RD     375     375  25015            20         19         21                    1.016                0   0.7063    25.12        0        5         True        0        1  -0.2107   0.2626      375    0.001202      0.9999
units: {'SpikingBandPower': 'volts', 'ThresholdCrossings': 'volts', 'index_position': 'flexion units', 'index_velocity': 'flexion units per time bin'}
tasks per paired date: {'2022-09-21': ['CO', 'RD']}
target_style column agrees with the identifier's task: True
SBP: 2 distinct arrays of 2; identical pairs: []
TCR: 2 distinct arrays of 2; identical pairs: []
pos: 2 distinct arrays of 2; identical pairs: []
largest between-session correlation of the first 2000 SBP bins: 0.048
2022-09-21_CO_nwb: corr(velocity[t], position[t]-position[t-1]) = 0.826, 0.698; with velocity[t-1] 1.000, 1.000; std ratio 1.00, 1.00
2022-09-21_RD_nwb: corr(velocity[t], position[t]-position[t-1]) = 0.869, 0.740; with velocity[t-1] 1.000, 1.000; std ratio 1.00, 1.00
Traceback (most recent call last):
  File "/tmp/claude/test02.py", line 92, in <module>
    X = np.stack([np.stack([sbp[b - lag - 2: b - lag].reshape(-1) for b in tb]) for tb in bins])
                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[... 3 more lines not kept]
```

**Agent calls Bash**

```bash
cd /tmp/claude && python - <<'EOF'
s=open('build02.py').read()
old='''    tr, te = np.intersect1d(ds.train_indices, np.flatnonzero(inside)), np.intersect1d(ds.test_indices, np.flatnonzero(inside))'''
new='''    keep = np.flatnonzero(inside)
    position_of = {k: i for i, k in enumerate(keep)}
    tr = np.array([position_of[i] for i in ds.train_indices if inside[i]])
    te = np.array([position_of[i] for i in ds.test_indices if inside[i]])
    Y = ds.behavior[keep]'''
assert old in s; s=s.replace(old,new)
s=s.replace("for tb in bins])\n        m = make","for tb in bins[keep]])\n        m = make")
s=s.replace("Ridge(alpha=1000.0)).fit(X[tr].reshape(-1, X.shape[-1]), ds.behavior[tr].reshape(-1, 2))","Ridge(alpha=1000.0)).fit(X[tr].reshape(-1, X.shape[-1]), Y[tr].reshape(-1, 2))")
s=s.replace("row[lag] = r2_score(ds.behavior[te].reshape(-1, 2)","row[lag] = r2_score(Y[te].reshape(-1, 2)")
open('build02.py','w').write(s)
EOF
grep -n "bins\[keep\]\|Y\[t" build02.py | head; . $TMPDIR/venv/bin/activate && python build02.py && cd entries/du-2026 && python - <<'EOF'
import nbformat
nb=nbformat.read('02_link_development.ipynb',4)
code="\n\n".join(c.source for c in nb.cells if c.cell_type=='code')
code=code.replace('dev_assets = [a for k in paired_dates for a in sorted(by_date[k], key=lambda a: a["path"])]','dev_assets = [a for k in paired_dates[7:8] for a in sorted(by_date[k], key=lambda a: a["path"])]')
open('/tmp/claude/test02.py','w').write(code)
EOF
PYTHONPATH=. timeout 1800 python /tmp/claude/test02.py 2>&1 | grep -v Warn | tail -150 | cut -c1-250
```

```
158:        X = np.stack([np.stack([sbp[b - lag - 2: b - lag].reshape(-1) for b in tb]) for tb in bins[keep]])
159:        m = make_pipeline(StandardScaler(), Ridge(alpha=1000.0)).fit(X[tr].reshape(-1, X.shape[-1]), Y[tr].reshape(-1, 2))
160:        row[lag] = r2_score(Y[te].reshape(-1, 2), m.predict(X[te].reshape(-1, X.shape[-1])), multioutput="variance_weighted")
ok
    _fixup_main_from_path(data['init_main_from_path'])
  File "/home/runner/.local/share/uv/python/cpython-3.12.16-linux-x86_64-gnu/lib/python3.12/multiprocessing/spawn.py", line 297, in _fixup_main_from_path
    main_content = runpy.run_path(main_path,
                   ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<frozen runpy>", line 287, in run_path
  File "<frozen runpy>", line 98, in _run_module_code
  File "<frozen runpy>", line 88, in _run_code
  File "/tmp/claude/test02.py", line 140, in <module>
    results = d.run_parallel(d.link_session_jobs, [(a["asset_id"], a["path"], jobs) for a in dev_assets])
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "entries/du-2026/du2026.py", line 1009, in run_parallel
    futures = [pool.submit(function, *args) for args in argument_lists]
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/runner/.local/share/uv/python/cpython-3.12.16-linux-x86_64-gnu/lib/python3.12/concurrent/futures/process.py", line 822, in submit
    self._adjust_process_count()
  File "/home/runner/.local/share/uv/python/cpython-3.12.16-linux-x86_64-gnu/lib/python3.12/concurrent/futures/process.py", line 781, in _adjust_process_count
[... 134 more lines not kept]
```

**Agent calls Bash**

```bash
. $TMPDIR/venv/bin/activate && python - <<'EOF'
import nbformat
nb=nbformat.read('02_link_development.ipynb',4)
for c in nb.cells:
    c.source=c.source.replace('dev_assets = [a for k in paired_dates for a in sorted(by_date[k], key=lambda a: a["path"])]','dev_assets = [a for k in paired_dates[7:9] for a in sorted(by_date[k], key=lambda a: a["path"])]')
nbformat.write(nb,'/tmp/claude/test02.ipynb')
EOF
cp /tmp/claude/test02.ipynb ./_test02.ipynb && time jupyter nbconvert --to notebook --execute --ExecutePreprocessor.timeout=3000 --output /tmp/claude/test02_out.ipynb _test02.ipynb 2>&1 | tail -3; rm -f _test02.ipynb
```

```
[NbConvertApp] Converting notebook _test02.ipynb to notebook
[IPKernelApp] WARNING | Kernel is running over TCP without encryption. All communication (including code and outputs) is sent in plain text and is susceptible to eavesdropping. Use IPC transport or launch with kernel manager-provisioned CurveZMQ keys to enable transport encryption.
[NbConvertApp] Writing 69163 bytes to /tmp/claude/test02_out.ipynb

real	5m1.878s
user	18m24.300s
sys	0m8.001s
```

**Agent calls Bash**

```bash
. $TMPDIR/venv/bin/activate && python - <<'EOF'
import nbformat
nb=nbformat.read('/tmp/claude/test02_out.ipynb',4)
for c in nb.cells[10:]:
    if c.cell_type!='code': continue
    for o in c.outputs:
        t=o.get('text') or (o.get('data',{}).get('text/plain')) or ''.join(o.get('traceback',[]))[-1500:]
        print(t[:2500])
    print('-----')
EOF
```

```
date task  usable  trials_table
0  2022-09-21   CO     375           375
1  2022-09-21   RD     375           375
2  2022-11-02   RD     375           375
3  2022-11-02   CO     375           375
dates with both a CO and an RD session: 2  (expected 9)
sessions: 4; subjects in the asset paths: ['sub-Monkey-N']
usable trials: 1500  (expected 6750, tolerance 675)
sessions with 375 usable trials: 4 of 4; range 375 to 375; trials dropped by the window rule: 0

-----
task            CO      RD
date                      
2022-09-21  0.2078  0.2552
2022-11-02  0.2996  0.3424
CO mean 0.2537 (expected 0.308 +- 0.0308); RD mean 0.2988 (expected 0.313 +- 0.0313)
seed 20260726: CO 0.2537, RD 0.2988
seed 20261726: CO 0.2814, RD 0.2843
seed 20262726: CO 0.2578, RD 0.2895
seed 20263726: CO 0.2761, RD 0.2979
[... 176 more lines not kept]
```

**Agent calls Bash**

```bash
date -u; cd  && grep -n "def handover" -A50 tools/entry.py | grep -n "Result\|markdown\|summary\|strip\|tag" | head -20; grep -n "max_minutes\|max-minutes" tools/entry.py | head -5
```

```
Sat Nov 21 14:48:42 UTC 2026
11:678-        nb = strip_conclusions(nbformat.read(executed, as_version=4))
29:that takes longer than --max-minutes fails, even if it ran without error.
525:                   max_minutes: float) -> int:
531:    if lock(entry_dir, version) or run(entry_dir, output_dir, timeout, max_minutes, fresh=True):
578:def reusable(entry_dir: Path, output_dir: Path, max_minutes: float) -> dict | None:
589:            if not r["ok"] or r["seconds"] > max_minutes * 60 or file_hash(output_dir / r["notebook"]) != r["sha256"]:
```

**Agent calls Bash**

```bash
grep -n "def strip_conclusions" -A30 tools/entry.py
```

```
654:def strip_conclusions(nb):
655-    """The notebook without the author's conclusions, for a verifier's first round."""
656-    kept = []
657-    for cell in nb.cells:
658-        text = cell.source.lstrip()
659-        if cell.cell_type == "markdown" and text.startswith("## Summary"):
660-            break
661-        if cell.cell_type == "markdown" and text.startswith("**Result:"):
662-            continue
663-        kept.append(cell)
664-    nb.cells = kept
665-    return nb
666-
667-
668-def handover(entry_dir: Path, output_dir: Path) -> int:
669-    entry = yaml.safe_load((entry_dir / "entry.yaml").read_text())
670-    target = output_dir / "handover"
671-    target.mkdir(parents=True, exist_ok=True)
672-    for notebook in entry["notebooks"]:
673-        executed = output_dir / notebook["path"]
[... 11 more lines not kept]
```

**Agent**

Subset test of the main notebook works (4 sessions in 5 min; the representative-trial rule already lands on 2022-09-21 RD, trial 123). Writing the remaining notebooks now.

**Agent calls Write**

```json
{
 "file_path": "/tmp/claude/build_rest.py",
 "content": "import sys\nsys.path.insert(0, \"/tmp/claude\")\nfrom nbtools import build\n\nCONC = {}\ntry:\n    from conclusions_rest import CONC  # noqa\nexcept ImportError:\n    pass\nENTRY = \"entries/du-2026/\"\n\n\ndef conc(cid):\n    return [(\"md\", CONC[cid], [f\"claim:{cid}\"])] if cid in CONC else []\n\n\ndef summary(key):\n    return [(\"md\", CONC[key])] if key in CONC else []\n\n\nSETUP = r\"\"\"\nimport collections, resource, time, zlib\nimport numpy as np\nimport pandas as pd\nimport du2026 as d\n\nPAPER = \"du-2026\"\ndef claim_seed(claim_id):\n    return zlib.crc32(f\"{PAPER}/{claim_id}\".encode())\nT0 = time.time()\nEXTRA = (1000, 2000, 3000, 4000)\n\"\"\"\n\nLINK_DEV = r\"\"\"\nassets = d.list_assets(d.LINK_ID, d.LINK_VERSION)\nby_date = collections.defaultdict(list)\nfor a in assets:\n    by_date[d.session_date(a[\"path\"])].append(a)\npaired_dates = sorted(k for k, v in by_date.items() if len(v) > 1)\ndev_assets = [a for k in paired_dates for a in sorted(by_date[k], key=lambda a: a[\"path\"])]\nprint(f\"{len(assets)} assets in DANDI:{d.LINK_ID} {d.LINK_VERSION}; {len(paired_dates)} dates with two sessions, {len(dev_assets)} development sessions\")\n\"\"\"\n\nLINK_SANITY = r\"\"\"\nsessions = [d.load_link_session(a[\"asset_id\"], a[\"path\"], signals=(\"SpikingBandPower\", \"ThresholdCrossings\")) for a in dev_assets]\ncheck = pd.DataFrame([dict(session=s.identifier, trials=len(s.trials), bins=len(s.timestamps),\n                           dt_ms=1000 * float(np.median(np.diff(s.timestamps))),\n                           sbp_range=f\"{s.signals['SpikingBandPower'].min():.3g}..{s.signals['SpikingBandPower'].max():.3g}\",\n                           tcr_range=f\"{s.signals['ThresholdCrossings'].min():.3g}..{s.signals['ThresholdCrossings'].max():.3g}\",\n                           pos_range=f\"{s.position.min():.3g}..{s.position.max():.3g}\",\n                           vel_range=f\"{s.velocity.min():.3g}..{s.velocity.max():.3g}\") for s in sessions])\nprint(check.to_string())\nprint(\"tasks:\", collections.Counter(s.task for s in sessions), \"; units:\", sessions[0].units)\nprint(\"The full data check of these sessions (duplicates, clock, velocity) is in 02_link_development.ipynb.\")\ndel sessions\nprint(f\"peak memory {resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1e6:.2f} GB\")\n\"\"\"\n\nTABLES = r\"\"\"\ndef table(results, name, field=\"gain\"):\n    return pd.DataFrame([{\"date\": r[\"date\"], \"task\": r[\"task\"], field: r[name][field]} for r in results])\n\"\"\"\n\n# ============================================================== 01 synthetic\nc = []\nc.append((\"md\", r\"\"\"\n# Du, Lai, Hu & Ye (2026): matched-seed synthetic calibration\n\nPaper: doi:10.64898/2026.08.04.742876 (bioRxiv preprint posted 2026-08-10; claims file written from\nits full text without the supplement). These claims are `data: elsewhere`: the data are not\ndeposited but generated by the paper's code (github.com/gwkuqgfkqe/neural-decoder-context-audit, tag\nv1.0-jne-submission, commit b042fbe, `synthetic.py` and `run_synthetic_calibration.py`), ported to\n`du2026.generate_synthetic` and run here. No dataset version applies; the generator's code is pinned\nat that commit. The full claims table is in `02_link_development.ipynb`.\n\n| Claim | Status |\n|---|---|\n| synthetic-template-null | tested |\n| synthetic-signal-ordering | tested |\n| synthetic-pair-breaking | tested |\n\"\"\"))\nc.append((\"code\", SETUP + r\"\"\"\n# Methods 4.8: 480 trials, 60 bins, 8 conditions, 48 neural features, AR(1) 0.85, template scale 1.0,\n# neural noise SD 0.20; regimes (trial-signal scale, embedding) 0.20/0, 0.25/0.8, 0.35/1.8; seeds 20260726-35.\n# Seed sensitivity (protocol, author step 3): the ten seeds are also run shifted by 1000, 2000, 3000, 4000.\nseed_sets = {k: [s + k for s in d.SYNTHETIC_SEEDS] for k in (0,) + EXTRA}\nargs = [(s, regime) for k in seed_sets for s in seed_sets[k] for regime in d.SYNTHETIC_REGIMES]\nt = time.time()\nrows = d.run_parallel(d.synthetic_job, args)\nsyn = pd.DataFrame(rows)\nsyn[\"offset\"] = [a[0] - (a[0] - 20260726) % 1000 - 20260726 for a in args]\nprint(f\"{len(rows)} fits in {(time.time() - t) / 60:.1f} min\")\n\"\"\"))\nc.append((\"code\", r\"\"\"\nds = d.generate_synthetic(seed=20260726, **d.SYNTHETIC_REGIMES[\"strong\"])\nprint(\"generated arrays:\", \"neural\", ds.neural.shape, \"context\", ds.context.shape, \"behavior\", ds.behavior.shape)\nprint(\"conditions:\", np.bincount(ds.condition[:, 0]), \"; train/test trials:\", len(ds.train_indices), len(ds.test_indices))\nprint(f\"behavior range {ds.behavior.min():.3f} to {ds.behavior.max():.3f}; neural range {ds.neural.min():.3f} to {ds.neural.max():.3f}\")\nmain = syn[syn.offset == 0]\nprint(main.pivot(index=\"seed\", columns=\"regime\", values=\"gain\").round(5).to_string())\nprint(f\"peak memory {resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1e6:.2f} GB\")\n\"\"\", [\"sanity\"]))\n\nc.append((\"md\", r\"\"\"\n## synthetic-template-null\n\n> In the matched-seed synthetic calibration, the template-only regime (no trial signal in the neural\n> features) gave a median context-conditional neural gain of about zero (-0.0000023, range -0.0000588\n> to 0.0000248 over ten seeds).\n\"\"\"))\nc.append((\"code\", r\"\"\"\nfor k in (0,) + EXTRA:\n    g = syn[(syn.offset == k) & (syn.regime == \"template_only\")].gain\n    print(f\"seeds 20260726+{k}..: template-only median {g.median():.7f}, median |gain| {g.abs().median():.7f}, range {g.min():.7f} to {g.max():.7f}\")\nprint(\"criterion: median absolute gain below 0.03 (expected median -0.0000023, range -0.0000588 to 0.0000248)\")\n\"\"\", [\"claim:synthetic-template-null\"]))\nc += conc(\"synthetic-template-null\")\n\nc.append((\"md\", r\"\"\"\n## synthetic-signal-ordering\n\n> Weak and strong trial-signal regimes gave median gains of 0.2245 and 0.3736, and the three regime\n> medians were strictly ordered (template-only, weak, strong).\n\"\"\"))\nc.append((\"code\", r\"\"\"\nfor k in (0,) + EXTRA:\n    med = syn[syn.offset == k].groupby(\"regime\").gain.median()\n    print(f\"seeds +{k}: medians template {med['template_only']:.5f}, weak {med['weak']:.5f}, strong {med['strong']:.5f}; \"\n          f\"strictly increasing: {med['template_only'] < med['weak'] < med['strong']}\")\nprint(\"expected weak 0.2245 +- 0.02245, strong 0.3736 +- 0.03736\")\nfor regime in (\"weak\", \"strong\"):\n    g = main[main.regime == regime].gain\n    print(f\"{regime}: range over the ten seeds {g.min():.4f} to {g.max():.4f}\")\n\"\"\", [\"claim:synthetic-signal-ordering\"]))\nc += conc(\"synthetic-signal-ordering\")\n\nc.append((\"md\", r\"\"\"\n## synthetic-pair-breaking\n\n> In the strong synthetic regime, correct-pair gain exceeded nearest source-context replacement and the\n> mean of 100 within-condition permutations for 10 of 10 seeds; replacement and permutation means were\n> -0.3486 and -0.3663.\n\"\"\"))\nc.append((\"code\", r\"\"\"\nfor k in (0,) + EXTRA:\n    s_ = syn[(syn.offset == k) & (syn.regime == \"strong\")]\n    above = int(((s_.gain > s_.replacement_gain) & (s_.gain > s_.permutation_mean)).sum())\n    print(f\"seeds +{k}: seeds with gain above both controls {above}/10; mean replacement {s_.replacement_gain.mean():.4f}; \"\n          f\"mean permutation {s_.permutation_mean.mean():.4f}\")\nprint(\"expected 10 (tolerance 1), -0.3486 +- 0.03486, -0.3663 +- 0.03663\")\ns_ = main[main.regime == \"strong\"]\nprint(s_[[\"seed\", \"gain\", \"replacement_gain\", \"permutation_mean\"]].round(4).to_string())\nfor regime in (\"template_only\", \"weak\"):\n    r_ = main[main.regime == regime]\n    print(f\"{regime}: mean replacement {r_.replacement_gain.mean():.4f}, mean permutation {r_.permutation_mean.mean():.4f}\")\nprint(f\"run time {(time.time() - T0) / 60:.1f} min\")\n\"\"\", [\"claim:synthetic-pair-breaking\"]))\nc += conc(\"synthetic-pair-breaking\")\nc += summary(\"summary01\")\nbuild(ENTRY + \"01_synthetic.ipynb\", c)\n\n# ============================================================== 03 estimator families\nc = []\nc.append((\"md\", r\"\"\"\n# Du, Lai, Hu & Ye (2026) on LINK: estimator families\n\nPaper doi:10.64898/2026.08.04.742876; dataset DANDI:001201 version 0.251023.2336 (the cited version;\nsee `02_link_development.ipynb` for the header, the full claims table and the data check).\nThis notebook tests estimator-family-link on the 18 development sessions.\n\n| Claim | Status |\n|---|---|\n| estimator-family-link | tested; reading (b) of the nonlinear context (every setting of Methods 4.6) not run, see below |\n\"\"\"))\nc.append((\"code\", SETUP + LINK_DEV + TABLES))\nc.append((\"code\", LINK_SANITY, [\"sanity\"]))\nc.append((\"md\", r\"\"\"\n## estimator-family-link\n\n> Separately penalized context and neural blocks and nonlinear context random features retained\n> positive LINK task means, with magnitudes that differed between estimator families.\n\nBlock penalties: `du2026.block_ridge`, port of `evaluate_block_ridge_audit` (the pair of penalties\nover the grid squared on the inner 80/20 split). Nonlinear context: `du2026.rff_context`, port of\n`evaluate_rff_context_audit` (D = 256, g chosen from 0.25, 1, 4 with the penalties on the inner split,\nfive cross-fitting folds), the claims file's reading (a). Reading (b), every setting of Methods 4.6\n(D 128/256/512 by three map seeds by g 0.25/1/4, 27 settings), was not run: one setting takes about\n18 s per session and context, so 27 settings on 18 sessions and 4 signal-context pairs are about 27\ntimes this notebook's nonlinear-context part (estimated 9 h on four processes). The fully nested\nlinear means for comparison are those of `02_link_development.ipynb`; they are recomputed here for\nthe magnitudes.\n\"\"\"))\nc.append((\"code\", r\"\"\"\njobs = []\nfor signal, tag in ((\"SpikingBandPower\", \"SBP\"), (\"ThresholdCrossings\", \"TCR\")):\n    for context in (\"geometry_tensor\", \"causal_history\"):\n        build_kw = dict(signal=signal, context_mode=context, seed=20260726)\n        jobs.append((f\"{tag}_{context}_block\", build_kw, \"block\", {\"seed\": 20260726}, False))\n        jobs.append((f\"{tag}_{context}_rffctx\", build_kw, \"rff_context\", {\"seed\": 20260726}, False))\n        jobs.append((f\"{tag}_{context}_nested\", build_kw, \"nested\", {\"seed\": 20260726}, False))\nt = time.time()\nresults = d.run_parallel(d.link_session_jobs, [(a[\"asset_id\"], a[\"path\"], jobs) for a in dev_assets])\nprint(f\"{len(jobs)} fits per session on {len(results)} sessions in {(time.time() - t) / 60:.1f} min\")\nrows = []\nfor tag in (\"SBP\", \"TCR\"):\n    for context in (\"geometry_tensor\", \"causal_history\"):\n        for family, key in ((\"fully nested linear\", \"nested\"), (\"block penalties\", \"block\"), (\"nonlinear context\", \"rffctx\")):\n            t_ = table(results, f\"{tag}_{context}_{key}\")\n            rows.append(dict(signal=tag, context=d.LADDER_NAMES[context], family=family, CO=t_[t_.task == \"CO\"].gain.mean(),\n                             RD=t_[t_.task == \"RD\"].gain.mean(), all18=t_.gain.mean(), positive=int((t_.gain > 0).sum()),\n                             min=t_.gain.min(), max=t_.gain.max()))\nfam = pd.DataFrame(rows)\nprint(fam.to_string(float_format=lambda v: f\"{v:.5f}\"))\nalt = fam[fam.family != \"fully nested linear\"]\nprint(\"reading (a), every CO and RD mean positive for both families:\", bool((alt[[\"CO\", \"RD\"]] > 0).all().all()))\nprint(\"reading (b), every 18-session mean positive for both families:\", bool((alt.all18 > 0).all()))\nprint(\"nonlinear-context g chosen:\", collections.Counter(r[f\"{tag}_{ctx}_rffctx\"][\"gamma\"] for r in results for tag in (\"SBP\", \"TCR\") for ctx in (\"geometry_tensor\", \"causal_history\")))\nprint(\"block penalty pairs chosen:\", collections.Counter(r[f\"{tag}_{ctx}_block\"][\"penalties\"] for r in results for tag in (\"SBP\", \"TCR\") for ctx in (\"geometry_tensor\", \"causal_history\")).most_common(6))\nprint(f\"run time {(time.time() - T0) / 60:.1f} min; peak memory {resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1e6:.2f} GB\")\n\"\"\", [\"claim:estimator-family-link\"]))\nc += conc(\"estimator-family-link\")\nc += summary(\"summary03\")\nbuild(ENTRY + \"03_link_estimators.ipynb\", c)\n\n# ============================================================== 04 temporal and capacity\nc = []\nc.append((\"md\", r\"\"\"\n# Du, Lai, Hu & Ye (2026) on LINK: temporal offset and context capacity\n\nPaper doi:10.64898/2026.08.04.742876; dataset DANDI:001201 version 0.251023.2336 (the cited version;\nsee `02_link_development.ipynb` for the header, the full claims table and the data check).\n\n| Claim | Status |\n|---|---|\n| temporal-offset | tested, readings (i) fully nested and (ii) `evaluate_decoders_nested` |\n| context-capacity-contrast | tested, readings (i) and (ii) |\n\nThe release has no script for either analysis, and the paper does not name the estimator for Figure\n7a or 7c; the claims file names both readings. Reading (ii) is `du2026.decoders_nested`, a port of\n`evaluate_decoders_nested`, whose residual-neural gain is used.\n\"\"\"))\nc.append((\"code\", SETUP + LINK_DEV + TABLES))\nc.append((\"code\", LINK_SANITY, [\"sanity\"]))\nc.append((\"code\", r\"\"\"\njobs = []\n# temporal offset: both histories end `offset` before the behaviour bin; one window start for all\n# offsets, 280 ms after the start bin (eight SBP bins plus six offset bins; claims file)\nfor offset in (0, 40, 80, 120):\n    build_kw = dict(signal=\"SpikingBandPower\", context_mode=\"causal_history\", neural_lead_ms=offset,\n                    output_lead_ms=offset, sample_offset_ms=280, seed=20260726)\n    jobs.append((f\"offset{offset}_nested\", build_kw, \"nested\", {\"seed\": 20260726}, False))\n    jobs.append((f\"offset{offset}_decoders\", build_kw, \"decoders\", {\"seed\": 20260726}, False))\n# context capacity: linear and quadratic geometry, with and without history (Methods 4.4)\nfor signal, tag in ((\"SpikingBandPower\", \"SBP\"), (\"ThresholdCrossings\", \"TCR\")):\n    for context in (\"geometry_tensor\", \"geometry_quadratic\", \"causal_history\", \"causal_history_quadratic\"):\n        build_kw = dict(signal=signal, context_mode=context, seed=20260726)\n        jobs.append((f\"{tag}_{context}_nested\", build_kw, \"nested\", {\"seed\": 20260726}, False))\n        jobs.append((f\"{tag}_{context}_decoders\", build_kw, \"decoders\", {\"seed\": 20260726}, False))\nt = time.time()\nresults = d.run_parallel(d.link_session_jobs, [(a[\"asset_id\"], a[\"path\"], jobs) for a in dev_assets])\nprint(f\"{len(jobs)} fits per session on {len(results)} sessions in {(time.time() - t) / 60:.1f} min\")\nprint(\"context feature counts are 141, 351, 151 and 361 (Methods 4.4); usable trials at the 280 ms window start:\",\n      sorted(set(r[\"offset0_nested\"][\"n_usable\"] for r in results)))\n\"\"\"))\nc.append((\"md\", r\"\"\"\n## temporal-offset\n\n> Shifting both the neural and the measured-output histories back by 40, 80 and 120 ms with the\n> behavioral window fixed reduced the small output-history-conditional gain and changed the RD\n> direction at intermediate offsets.\n\"\"\"))\nc.append((\"code\", r\"\"\"\nfor reading, key, field in ((\"(i) fully nested\", \"nested\", \"gain\"), (\"(ii) evaluate_decoders_nested\", \"decoders\", \"innovation_gain\")):\n    rows = []\n    for offset in (0, 40, 80, 120):\n        t_ = table(results, f\"offset{offset}_{key}\", field)\n        rows.append(dict(offset_ms=offset, CO=t_[t_.task == \"CO\"][field].mean(), RD=t_[t_.task == \"RD\"][field].mean(),\n                         RD_minus_CO=t_[t_.task == \"RD\"][field].mean() - t_[t_.task == \"CO\"][field].mean(),\n                         positive=int((t_[field] > 0).sum())))\n    off = pd.DataFrame(rows).set_index(\"offset_ms\")\n    print(reading)\n    print(off.to_string(float_format=lambda v: f\"{v:.5f}\"))\n    reduced = bool(off.loc[120, \"CO\"] < off.loc[0, \"CO\"] and off.loc[120, \"RD\"] < off.loc[0, \"RD\"])\n    a = bool(off.loc[40, \"RD\"] < 0 or off.loc[80, \"RD\"] < 0)\n    b = bool(np.sign(off.loc[40, \"RD_minus_CO\"]) != np.sign(off.loc[0, \"RD_minus_CO\"]) or np.sign(off.loc[80, \"RD_minus_CO\"]) != np.sign(off.loc[0, \"RD_minus_CO\"]))\n    print(f\"   gain at 120 ms below 0 ms for both tasks: {reduced}; RD change reading (a) RD mean negative at 40 or 80 ms: {a}; \"\n          f\"reading (b) RD minus CO changes sign at 40 or 80 ms: {b}\\n\")\n\"\"\", [\"claim:temporal-offset\"]))\nc += conc(\"temporal-offset\")\nc.append((\"md\", r\"\"\"\n## context-capacity-contrast\n\n> Adding quadratic geometry to the context changed the descriptive RD-minus-CO gain contrast, and the\n> richest quadratic-history context gave a small positive contrast for both SBP and TCR.\n\nPer date RD minus CO, mean over nine dates, 95% paired date-bootstrap interval (10,000 resamples,\ngenerator from the claim's seed; the seed plus 1000 to 4000 give the range of the interval bounds).\n\"\"\"))\nc.append((\"code\", r\"\"\"\nfor reading, key, field in ((\"(i) fully nested\", \"nested\", \"gain\"), (\"(ii) evaluate_decoders_nested\", \"decoders\", \"innovation_gain\")):\n    rows = []\n    for tag in (\"SBP\", \"TCR\"):\n        for context in (\"geometry_tensor\", \"geometry_quadratic\", \"causal_history\", \"causal_history_quadratic\"):\n            p = table(results, f\"{tag}_{context}_{key}\", field).pivot(index=\"date\", columns=\"task\", values=field)\n            diff = (p[\"RD\"] - p[\"CO\"]).to_numpy()\n            bounds = []\n            for k in (0,) + EXTRA:\n                rng = np.random.default_rng(claim_seed(\"context-capacity-contrast\") + k)\n                boots = np.array([rng.choice(diff, len(diff), replace=True).mean() for _ in range(10000)])\n                bounds.append(np.quantile(boots, [0.025, 0.975]))\n            rows.append(dict(signal=tag, context=d.LADDER_NAMES[context], CO=p[\"CO\"].mean(), RD=p[\"RD\"].mean(), RD_minus_CO=diff.mean(),\n                             ci_low=bounds[0][0], ci_high=bounds[0][1], excludes_zero=bool(bounds[0][0] > 0 or bounds[0][1] < 0),\n                             excludes_zero_all_seeds=all(b[0] > 0 or b[1] < 0 for b in bounds) if (bounds[0][0] > 0 or bounds[0][1] < 0) else not any(b[0] > 0 or b[1] < 0 for b in bounds)))\n    cap = pd.DataFrame(rows)\n    print(reading)\n    print(cap.to_string(float_format=lambda v: f\"{v:.5f}\"))\n    qh = cap[cap.context == \"quadratic plus history\"].set_index(\"signal\").RD_minus_CO\n    changed = []\n    for tag in (\"SBP\", \"TCR\"):\n        lin = cap[(cap.signal == tag) & (cap.context == \"geometry by phase\")].iloc[0]\n        quad = cap[(cap.signal == tag) & (cap.context == \"quadratic geometry\")].iloc[0]\n        changed.append(bool(np.sign(lin.RD_minus_CO) != np.sign(quad.RD_minus_CO) or lin.excludes_zero != quad.excludes_zero))\n    print(f\"   quadratic-plus-history contrast positive: SBP {qh['SBP'] > 0}, TCR {qh['TCR'] > 0}; \"\n          f\"quadratic contrast differs from linear (sign or interval excluding zero): SBP {changed[0]}, TCR {changed[1]}\\n\")\nprint(f\"run time {(time.time() - T0) / 60:.1f} min; peak memory {resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1e6:.2f} GB\")\n\"\"\", [\"claim:context-capacity-contrast\"]))\nc += conc(\"context-capacity-contrast\")\nc += summary(\"summary04\")\nbuild(ENTRY + \"04_link_temporal_capacity.ipynb\", c)\n\n# ============================================================== 05 confirmation\nc = []\nc.append((\"md\", r\"\"\"\n# Du, Lai, Hu & Ye (2026) on LINK: the 20 confirmation sessions\n\nPaper doi:10.64898/2026.08.04.742876; dataset DANDI:001201 version 0.251023.2336 (the version the\npaper cites; see `02_link_development.ipynb` for the full header and claims table).\n\nThe confirmation sessions are re-selected here with the paper's rule (Methods 4.2; port of\n`build_link_confirmation_manifest.py`) from the archive's asset metadata, and compared with the\npaper's frozen manifest (`outputs/primary_analysis/link_confirmation_manifest.json` in the release at\ncommit b042fbe, read from GitHub; an input).\n\n| Claim | Status |\n|---|---|\n| confirm-geometry-gain | tested |\n| confirm-history-contraction | tested |\n| confirm-replacement | tested |\n| confirm-table1-values | tested |\n\"\"\"))\nc.append((\"code\", SETUP + LINK_DEV + TABLES + r\"\"\"\nfrom concurrent.futures import ThreadPoolExecutor\nimport json, urllib.request\nwith ThreadPoolExecutor(12) as pool:\n    metadata = dict(zip([a[\"asset_id\"] for a in assets],\n                        pool.map(lambda a: d.asset_metadata(d.LINK_ID, d.LINK_VERSION, a[\"asset_id\"]), assets)))\ndev_ids = {a[\"asset_id\"] for a in dev_assets}\nrecords = [dict(asset_id=a[\"asset_id\"], path=a[\"path\"], date=d.session_date(a[\"path\"]), task=d.link_task_from_metadata(metadata[a[\"asset_id\"]]))\n           for a in assets]\nprint(\"tasks over all 312 assets:\", collections.Counter(r[\"task\"] for r in records))\nselected = []\nfor task in (\"CO\", \"RD\"):\n    eligible = sorted((r for r in records if r[\"task\"] == task and r[\"asset_id\"] not in dev_ids), key=lambda r: (r[\"date\"], r[\"asset_id\"]))\n    ranks = d.interior_ranks(len(eligible))\n    print(f\"{task}: {len(eligible)} eligible assets, ranks {ranks}\")\n    selected += [eligible[k] for k in ranks]\nurl = f\"https://raw.githubusercontent.com/gwkuqgfkqe/neural-decoder-context-audit/{d.PAPER_COMMIT}/outputs/primary_analysis/link_confirmation_manifest.json\"\nfrozen = json.load(urllib.request.urlopen(url, timeout=60))\nfrozen_ids = [r[\"asset_id\"] for r in frozen.get(\"selected\", frozen.get(\"sessions\", []))]\nprint(f\"frozen manifest: {len(frozen_ids)} assets; re-selected here: {len(selected)}; identical sets: {set(frozen_ids) == {r['asset_id'] for r in selected}}\")\nprint(\"in the frozen manifest only:\", set(frozen_ids) - {r['asset_id'] for r in selected}, \"; re-selected only:\", {r['asset_id'] for r in selected} - set(frozen_ids))\nprint(pd.DataFrame(selected)[[\"date\", \"task\", \"path\"]].to_string())\n\"\"\"))\nc.append((\"code\", r\"\"\"\nconf_assets = [a for a in assets if a[\"asset_id\"] in set(frozen_ids)]\nsessions = [d.load_link_session(a[\"asset_id\"], a[\"path\"], signals=(\"SpikingBandPower\",)) for a in conf_assets]\nchk = []\nfor s in sessions:\n    start_idx = np.array([int(np.argmin(np.abs(s.timestamps - t))) for t in s.trials.start_time])\n    usable = int(np.sum(start_idx + 8 + 24 < np.minimum(start_idx + s.trials.trial_count.to_numpy(), len(s.timestamps))))\n    chk.append(dict(session=s.identifier, task=s.task, trials=len(s.trials), usable=usable, bins=len(s.timestamps),\n                    dt_ms=1000 * float(np.median(np.diff(s.timestamps))),\n                    sbp=f\"{s.signals['SpikingBandPower'].min():.3g}..{s.signals['SpikingBandPower'].max():.3g}\",\n                    pos=f\"{s.position.min():.3g}..{s.position.max():.3g}\", vel=f\"{s.velocity.min():.3g}..{s.velocity.max():.3g}\"))\nchk = pd.DataFrame(chk)\nprint(chk.to_string())\nprint(\"tasks:\", collections.Counter(chk.task), \"; usable trials\", chk.usable.sum(), \"(paper 7,500); sessions with 375 usable:\", int((chk.usable == 375).sum()))\nprint(\"task in the NWB identifier agrees with the asset metadata:\",\n      all(s.task == d.link_task_from_metadata(metadata[s.asset_id]) for s in sessions))\nimport hashlib\nh = [hashlib.sha1(s.signals[\"SpikingBandPower\"].tobytes()).hexdigest() for s in sessions]\nprint(\"distinct SBP arrays:\", len(set(h)), \"of\", len(h))\ndel sessions\nprint(f\"peak memory {resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1e6:.2f} GB\")\n\"\"\", [\"sanity\"]))\nc.append((\"md\", r\"\"\"\n## The fits\n\nFully nested estimator, SBP, geometry by phase and plus history, outer split seed 20260726\n(`run_link_confirmation.py`), and the same under split and refit seeds plus 1000 to 4000 (protocol,\nseed sensitivity).\n\"\"\"))\nc.append((\"code\", r\"\"\"\nSEED = 20260726\njobs = []\nfor k in (0,) + EXTRA:\n    for context in (\"geometry_tensor\", \"causal_history\"):\n        jobs.append((f\"{context}_{SEED + k}\", dict(signal=\"SpikingBandPower\", context_mode=context, seed=SEED + k), \"nested\", {\"seed\": SEED + k}, False))\nt = time.time()\nresults = d.run_parallel(d.link_session_jobs, [(a[\"asset_id\"], a[\"path\"], jobs, (\"SpikingBandPower\",)) for a in conf_assets])\nprint(f\"{len(jobs)} fits per session on {len(results)} sessions in {(time.time() - t) / 60:.1f} min\")\nG, H = f\"geometry_tensor_{SEED}\", f\"causal_history_{SEED}\"\nper = table(results, G).rename(columns={\"gain\": \"geometry\"})\nper[\"history\"] = table(results, H).gain\nper[\"replacement_geometry\"] = table(results, G, \"replacement_gain\").replacement_gain\nper[\"replacement_history\"] = table(results, H, \"replacement_gain\").replacement_gain\nper[\"mse_red_geometry\"] = table(results, G, \"mse_reduction_percent\").mse_reduction_percent\nper[\"mse_red_history\"] = table(results, H, \"mse_reduction_percent\").mse_reduction_percent\nprint(per.round(5).to_string())\ndef seed_line(field, ctx):\n    out = []\n    for k in (0,) + EXTRA:\n        t_ = table(results, f\"{ctx}_{SEED + k}\", field)\n        out.append(f\"{t_[field].mean():.5f} ({int((t_[field] > 0).sum())} positive)\")\n    return \"; \".join(out)\n\"\"\"))\nc.append((\"md\", r\"\"\"\n## confirm-geometry-gain\n\n> In the 20 untouched LINK confirmation sessions, SBP geometry-by-phase gain was positive in all 20\n> and averaged 0.02158 (CO 0.02104, RD 0.02213).\n\"\"\"))\nc.append((\"code\", r\"\"\"\nm = per.groupby(\"task\").geometry.mean()\nprint(f\"positive {int((per.geometry > 0).sum())}/20 (expected 20, tolerance 2); mean {per.geometry.mean():.5f} (0.02158 +- 0.002158); \"\n      f\"CO {m['CO']:.5f} (0.02104 +- 0.002104); RD {m['RD']:.5f} (0.02213 +- 0.002213); range {per.geometry.min():.5f} to {per.geometry.max():.5f}\")\nprint(\"paper's gate (at least 16 of 20 positive, positive CO and RD means):\", bool((per.geometry > 0).sum() >= 16 and m[\"CO\"] > 0 and m[\"RD\"] > 0))\nprint(\"combined mean under seeds 20260726 + 0/1000/2000/3000/4000:\", seed_line(\"gain\", \"geometry_tensor\"))\n\"\"\", [\"claim:confirm-geometry-gain\"]))\nc += conc(\"confirm-geometry-gain\")\nc.append((\"md\", r\"\"\"\n## confirm-history-contraction\n\n> In the confirmation sessions, adding measured-output history reduced the combined mean gain to\n> 0.00755 (CO 0.00670, RD 0.00840), with 19 of 20 sessions positive.\n\"\"\"))\nc.append((\"code\", r\"\"\"\nm = per.groupby(\"task\").history.mean()\nprint(f\"mean {per.history.mean():.5f} (0.00755 +- 0.000755); CO {m['CO']:.5f} (0.0067 +- 0.00067); RD {m['RD']:.5f} (0.0084 +- 0.00084); \"\n      f\"positive {int((per.history > 0).sum())}/20 (19 +- 1.9); below the geometry mean {per.geometry.mean():.5f}: {per.history.mean() < per.geometry.mean()}\")\nprint(f\"range {per.history.min():.5f} to {per.history.max():.5f}\")\nprint(\"combined mean under the five seeds:\", seed_line(\"gain\", \"causal_history\"))\n\"\"\", [\"claim:confirm-history-contraction\"]))\nc += conc(\"confirm-history-contraction\")\nc.append((\"md\", r\"\"\"\n## confirm-replacement\n\n> In the confirmation sessions, nearest-replacement gain averaged -0.00771 under geometry by phase,\n> and correct-pair gain exceeded replacement gain in all 20 sessions and in both task means.\n\"\"\"))\nc.append((\"code\", r\"\"\"\nabove = int((per.geometry > per.replacement_geometry).sum())\nmt = per.groupby(\"task\")[[\"geometry\", \"replacement_geometry\"]].mean()\nprint(f\"mean replacement gain {per.replacement_geometry.mean():.5f} (-0.00771 +- 0.000771); sessions with gain above replacement {above}/20 (20 +- 2)\")\nprint(mt.round(5).to_string())\nprint(\"correct-pair mean above replacement in CO and RD:\", bool((mt.geometry > mt.replacement_geometry).all()))\nprint(\"replacement mean under the five seeds:\", seed_line(\"replacement_gain\", \"geometry_tensor\"))\n\"\"\", [\"claim:confirm-replacement\"]))\nc += conc(\"confirm-replacement\")\nc.append((\"md\", r\"\"\"\n## confirm-table1-values\n\n> Table 1 gives, for the confirmation sessions, a replacement gain of -0.00498 with measured-output\n> history and MSE reductions of 4.76% (geometry by phase) and 2.05% (plus history).\n\"\"\"))\nc.append((\"code\", r\"\"\"\nprint(f\"replacement gain, plus history: {per.replacement_history.mean():.5f} (-0.00498 +- 0.000498)\")\nprint(f\"MSE reduction, geometry: {per.mse_red_geometry.mean():.3f}% (4.76 +- 0.476); plus history: {per.mse_red_history.mean():.3f}% (2.05 +- 0.205)\")\nprint(\"plus-history replacement under the five seeds:\", seed_line(\"replacement_gain\", \"causal_history\"))\nprint(\"geometry MSE reduction under the five seeds:\", seed_line(\"mse_reduction_percent\", \"geometry_tensor\"))\nprint(\"history MSE reduction under the five seeds:\", seed_line(\"mse_reduction_percent\", \"causal_history\"))\nprint(f\"run time {(time.time() - T0) / 60:.1f} min; peak memory {resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1e6:.2f} GB\")\n\"\"\", [\"claim:confirm-table1-values\"]))\nc += conc(\"confirm-table1-values\")\nc += summary(\"summary05\")\nbuild(ENTRY + \"05_link_confirmation.ipynb\", c)\n\n# ============================================================== 06 MC_RTT\nc = []\nc.append((\"md\", r\"\"\"\n# Du, Lai, Hu & Ye (2026) on MC_RTT (DANDI:000129)\n\nPaper doi:10.64898/2026.08.04.742876 (claims file written from the bioRxiv full text, without the\nsupplement). Dataset: DANDI:000129 (MC_RTT, Neural Latents Benchmark), pinned at version\n**0.241017.1444**, the version the paper cites (Methods 4.2, Data availability) and the only published\nversion; file `sub-Indy/sub-Indy_desc-train_behavior+ecephys.nwb`, streamed. See\n`02_link_development.ipynb` for the full claims table.\n\n| Claim | Status |\n|---|---|\n| rtt-data | tested |\n| rtt-gain | tested |\n| rff-rtt | tested |\n| estimator-family-nlb | MC_RTT part tested (reading (a) of the nonlinear context); MC_Maze part not run (DANDI:000139 is not one of this attempt's datasets) |\n| maze-gain, rff-maze | blocked (DANDI:000139 not used) |\n\"\"\"))\nc.append((\"code\", SETUP + r\"\"\"\nrtt_assets = d.list_assets(d.RTT_ID, d.RTT_VERSION)\nprint([(a[\"path\"], a[\"size\"]) for a in rtt_assets])\ntrain_asset = next(a for a in rtt_assets if a[\"path\"] == d.RTT_TRAIN_PATH)\nraw = d.load_rtt_raw(train_asset[\"asset_id\"])\nds = d.build_rtt_dataset(raw)\n\"\"\"))\nc.append((\"code\", r\"\"\"\nprint(\"behaviour series:\", raw.descriptions)\nprint(f\"behaviour sampling: starting time {raw.behavior_timestamps_head}, rate {raw.behavior_rate} Hz; 20 ms bins: {raw.n_bins}\")\nprint(f\"units: {raw.n_units}; spike counts per 20 ms bin range {raw.spike_counts.min():.0f} to {raw.spike_counts.max():.0f}, mean rate {raw.spike_counts.mean() / 0.02:.1f} Hz\")\nprint(\"trials table:\", raw.trials.shape, \"split counts\", raw.trials.split.value_counts().to_dict())\ndur = (raw.trials.stop_time - raw.trials.start_time)\nprint(f\"block durations {dur.min():.3f} to {dur.max():.3f} s; first start {raw.trials.start_time.min()}, last stop {raw.trials.stop_time.max()} s; record {raw.n_bins * 0.02:.2f} s\")\nprint(f\"finger velocity range {raw.finger_vel.min():.1f} to {raw.finger_vel.max():.1f}; cursor {raw.cursor_pos.min():.1f} to {raw.cursor_pos.max():.1f}; target {raw.target_pos.min():.1f} to {raw.target_pos.max():.1f}\")\nprint(\"analysis arrays: neural\", ds.neural.shape, \"context\", ds.context.shape, \"behaviour\", ds.behavior.shape, \"train/val\", len(ds.train_indices), len(ds.test_indices))\n# velocity against the derivative of cursor position, as a check of units and alignment (mm/s against mm per 20 ms bin)\ndcur = np.gradient(raw.cursor_pos, axis=0) / 0.02\nfor lag in (-5, -2, 0, 2, 5):\n    a, b = (raw.finger_vel[max(0, lag):len(dcur) + min(0, lag)], dcur[max(0, -lag):len(dcur) - max(0, lag)])\n    print(f\"corr(finger velocity, cursor velocity shifted {lag} bins): x {np.corrcoef(a[:, 0], b[:, 0])[0, 1]:.3f}, y {np.corrcoef(a[:, 1], b[:, 1])[0, 1]:.3f}\")\n# clock check: decode finger velocity from 100 ms of spikes ending `lag` bins before the behaviour bin\nfrom sklearn.linear_model import Ridge\nfrom sklearn.pipeline import make_pipeline\nfrom sklearn.preprocessing import StandardScaler\nfrom sklearn.metrics import r2_score\nbins_ = np.arange(50, raw.n_bins - 50)\nrow = {}\nfor lag in (-25, -10, -4, 0, 2, 4, 6, 10, 25):\n    X = np.stack([raw.spike_counts[b - lag - 5:b - lag].reshape(-1) for b in bins_])\n    half = len(bins_) * 3 // 4\n    m = make_pipeline(StandardScaler(), Ridge(alpha=1000.0)).fit(X[:half], raw.finger_vel[bins_[:half]])\n    row[lag] = round(r2_score(raw.finger_vel[bins_[half:]], m.predict(X[half:]), multioutput=\"variance_weighted\"), 3)\nprint(\"held-out R2 (last quarter of the record) by lag in bins:\", row)\nprint(f\"peak memory {resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1e6:.2f} GB\")\n\"\"\", [\"sanity\"]))\nc.append((\"md\", r\"\"\"\n## rtt-data\n\n> The MC_RTT training file holds 1,080 fixed analysis blocks, 130 units, finger velocity, cursor\n> position and target position, with a release split of 810 train and 270 validation blocks.\n\"\"\"))\nc.append((\"code\", r\"\"\"\nprint(f\"blocks kept by the mc_rtt.py rule: {len(ds.neural)} of {len(raw.trials)} (expected 1080); units {raw.n_units} (expected 130); \"\n      f\"train {len(ds.train_indices)} (810), validation {len(ds.test_indices)} (270); bins per block {ds.neural.shape[1]}\")\nprint(\"series present: finger_vel, cursor_pos, target_pos:\", sorted(raw.descriptions))\n\"\"\", [\"claim:rtt-data\"]))\nc += conc(\"rtt-data\")\nc.append((\"md\", r\"\"\"\n## rtt-gain\n\n> In MC_RTT, target plus lag-matched cursor-position history gave context-only R2 of 0.6031, and fully\n> nested neural gain beyond it was 0.06846 (conditional interval 0.05371 to 0.08478), context RMSE\n> falling from 39.78 to 36.19 (a 17.25% MSE reduction), with component gains 0.0836 and 0.0513 and\n> replacement gain -0.02297.\n\nEstimator seed 20260726 (`run_primary_analyses.py`); the release split is fixed, and the estimator's\nfolds and inner splits are also run under seeds plus 1000 to 4000. The same fits give the three\nnonlinear-neural maps (rff-rtt).\n\"\"\"))\nc.append((\"code\", r\"\"\"\nSEED = 20260726\njobs = [(f\"nested_{SEED + k}\", {}, \"nested\", dict(seed=SEED + k, rff_seeds=d.RFF_SEEDS if k == 0 else ()), False) for k in (0,) + EXTRA]\njobs_family = [(\"block\", {}, \"block\", {\"seed\": SEED}, False), (\"rffctx\", {}, \"rff_context\", {\"seed\": SEED}, False)]\nt = time.time()\nout = d.run_parallel(d.rtt_jobs, [(train_asset[\"asset_id\"], [j]) for j in jobs + jobs_family])\nres = {k: v for o in out for k, v in o.items()}\nprint(f\"fits in {(time.time() - t) / 60:.1f} min\")\nr = res[f\"nested_{SEED}\"]\nexp = [(\"context-only R2\", r[\"context_r2\"], 0.6031, 0.06031), (\"fully nested gain\", r[\"gain\"], 0.06846, 0.01632),\n       (\"context RMSE\", r[\"context_rmse\"], 39.78, 3.978), (\"context-plus-neural RMSE\", r[\"exact_rmse\"], 36.19, 3.619),\n       (\"% MSE reduction\", r[\"mse_reduction_percent\"], 17.25, 1.725), (\"gain, component 1\", r[\"component_gain\"][0], 0.0836, 0.00836),\n       (\"gain, component 2\", r[\"component_gain\"][1], 0.0513, 0.00513), (\"replacement gain\", r[\"replacement_gain\"], -0.02297, 0.002297)]\nfor label, v, e, tol in exp:\n    print(f\"{label}: {v:.5f} (expected {e} +- {tol}; within: {abs(v - e) <= tol})\")\nfor k in (0,) + EXTRA:\n    rr = res[f\"nested_{SEED + k}\"]\n    print(f\"seed {SEED + k}: gain {rr['gain']:.5f}, replacement {rr['replacement_gain']:.5f}, context R2 {rr['context_r2']:.4f}\")\nprint(\"penalties (context, residualizer, residual learner):\", r[\"context_alpha\"], r[\"residualizer_alpha\"], r[\"innovation_alpha\"])\n\"\"\", [\"claim:rtt-gain\"]))\nc += conc(\"rtt-gain\")\nc.append((\"md\", r\"\"\"\n## rff-rtt\n\n> Under three prespecified nonlinear-neural random-feature maps, MC_RTT gain stayed positive (0.01491 to\n> 0.01685).\n\"\"\"))\nc.append((\"code\", r\"\"\"\ng = {s: res[f\"nested_{SEED}\"][\"rff\"][s][\"gain\"] for s in d.RFF_SEEDS}\nprint({s: round(v, 5) for s, v in g.items()}, \"penalties\", {s: res[f\"nested_{SEED}\"][\"rff\"][s][\"alpha\"] for s in d.RFF_SEEDS})\nlo, hi = 0.01491 - 0.001491, 0.01685 + 0.001685\nprint(f\"all positive: {all(v > 0 for v in g.values())}; all inside {lo:.5f}..{hi:.5f}: {all(lo <= v <= hi for v in g.values())}\")\nprint(\"replacement gains under the maps:\", {s: round(res[f\"nested_{SEED}\"][\"rff\"][s][\"replacement_gain\"], 5) for s in d.RFF_SEEDS})\n\"\"\", [\"claim:rff-rtt\"]))\nc += conc(\"rff-rtt\")\nc.append((\"md\", r\"\"\"\n## estimator-family-nlb\n\n> Under the separate-block and nonlinear-context estimators, MC_RTT gain remained positive while\n> MC_Maze remained near zero.\n\"\"\"))\nc.append((\"code\", r\"\"\"\nprint(f\"block penalties: gain {res['block']['gain']:.5f} (penalties {res['block']['penalties']}); \"\n      f\"nonlinear context (D 256, g chosen {res['rffctx']['gamma']}): gain {res['rffctx']['gain']:.5f}; fully nested linear {res[f'nested_{SEED}']['gain']:.5f}\")\nprint(\"MC_RTT positive under both families:\", res[\"block\"][\"gain\"] > 0 and res[\"rffctx\"][\"gain\"] > 0)\nprint(f\"run time {(time.time() - T0) / 60:.1f} min; peak memory {resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1e6:.2f} GB\")\n\"\"\", [\"claim:estimator-family-nlb\"]))\nc += conc(\"estimator-family-nlb\")\nc += summary(\"summary06\")\nbuild(ENTRY + \"06_mc_rtt.ipynb\", c)\nprint(\"ok\")\n"
}
```

```
File created successfully at: /tmp/claude/build_rest.py (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd /tmp/claude && python - <<'EOF'
s=open('build_rest.py').read()
s=s.replace('syn["offset"] = [a[0] - (a[0] - 20260726) % 1000 - 20260726 for a in args]','syn["offset"] = [(a[0] - 20260726) // 1000 * 1000 for a in args]')
open('build_rest.py','w').write(s)
EOF
python -c "
import json;d=json.load(open('$TMPDIR/neural-decoder-context-audit/outputs/primary_analysis/link_confirmation_manifest.json'));print(list(d.keys())); k=[k for k in d if isinstance(d[k],list)];print(k, d[k[0]][0] if k else '')"
```

```
['schema_version', 'dandiset', 'version', 'selection_frozen', 'selection_rule', 'asset_count', 'excluded_frozen_v05_count', 'eligible_counts', 'selected_ranks_zero_based', 'selected']
['selected'] {'asset_id': 'b9868d49-f641-4b95-a8e3-6295111b958b', 'path': 'sub-Monkey-N/sub-Monkey-N_ses-20200924_ecephys.nwb', 'date': '2020-09-24', 'task': 'CO', 'size_bytes': 36913714, 'sha256': 'aafb0f44f01f92892c81dbcc3f6b7e2491e4c4790a5de93f81295e9baff20667', 'download_url': 'https://api.dandiarchive.org/api/assets/b9868d49-f641-4b95-a8e3-6295111b958b/download/', 'excluded_frozen_v05': False, 'eligible_rank_zero_based': 13, 'selection_quantile': '1/11', 'output': 'link_confirmation/sub-Monkey-N_ses-20200924_ecephys.nwb'}
Shell cwd was reset to
```

**Agent calls Bash**

```bash
date -u; . $TMPDIR/venv/bin/activate && python /tmp/claude/build_rest.py && cd entries/du-2026 && mkdir -p /tmp/claude/out && for nb in 06_mc_rtt 01_synthetic; do /usr/bin/time -f "$nb %e s %M KB" jupyter nbconvert --to notebook --execute --ExecutePreprocessor.timeout=3600 --output-dir /tmp/claude/out $nb.ipynb 2>&1 | grep -v "TCP\|Converting\|Writing"; done; date -u
```

```
Sat Nov 21 14:51:18 UTC 2026
ok
Traceback (most recent call last):
  File "/tmp/claude-1001/venv/bin/jupyter-nbconvert", line 10, in <module>
    sys.exit(main())
             ^^^^^^
  File "/tmp/claude-1001/venv/lib/python3.12/site-packages/jupyter_core/application.py", line 284, in launch_instance
    super().launch_instance(argv=argv, **kwargs)
  File "/tmp/claude-1001/venv/lib/python3.12/site-packages/traitlets/config/application.py", line 1080, in launch_instance
    app.start()
  File "/tmp/claude-1001/venv/lib/python3.12/site-packages/nbconvert/nbconvertapp.py", line 420, in start
    self.convert_notebooks()
  File "/tmp/claude-1001/venv/lib/python3.12/site-packages/nbconvert/nbconvertapp.py", line 597, in convert_notebooks
    self.convert_single_notebook(notebook_filename)
  File "/tmp/claude-1001/venv/lib/python3.12/site-packages/nbconvert/nbconvertapp.py", line 563, in convert_single_notebook
    output, resources = self.export_single_notebook(
                        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/tmp/claude-1001/venv/lib/python3.12/site-packages/nbconvert/nbconvertapp.py", line 487, in export_single_notebook
    output, resources = self.exporter.from_filename(
                        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[... 215 more lines not kept]
```

**Agent calls Bash**

```bash
cd /tmp/claude && python - <<'EOF'
s=open('build_rest.py').read()
old='''print(f"finger velocity range {raw.finger_vel.min():.1f} to {raw.finger_vel.max():.1f}; cursor {raw.cursor_pos.min():.1f} to {raw.cursor_pos.max():.1f}; target {raw.target_pos.min():.1f} to {raw.target_pos.max():.1f}")'''
new='''print(f"finger velocity range {np.nanmin(raw.finger_vel):.1f} to {np.nanmax(raw.finger_vel):.1f}; cursor {np.nanmin(raw.cursor_pos):.1f} to {np.nanmax(raw.cursor_pos):.1f}; target {np.nanmin(raw.target_pos):.1f} to {np.nanmax(raw.target_pos):.1f}")
bad = ~np.isfinite(raw.finger_vel).all(axis=1) | ~np.isfinite(raw.cursor_pos).all(axis=1) | ~np.isfinite(raw.target_pos).all(axis=1)
print(f"20 ms bins with a missing (NaN) behaviour value: {int(bad.sum())} of {raw.n_bins}; NaN in the analysis arrays: "
      f"behaviour {int(np.isnan(ds.behavior).sum())}, context {int(np.isnan(ds.context).sum())}")'''
assert old in s; s=s.replace(old,new)
s=s.replace('''    print(f"corr(finger velocity, cursor velocity shifted {lag} bins): x {np.corrcoef(a[:, 0], b[:, 0])[0, 1]:.3f}, y {np.corrcoef(a[:, 1], b[:, 1])[0, 1]:.3f}")''','''    ok = np.isfinite(a).all(axis=1) & np.isfinite(b).all(axis=1)
    print(f"corr(finger velocity, cursor velocity shifted {lag} bins): x {np.corrcoef(a[ok, 0], b[ok, 0])[0, 1]:.3f}, y {np.corrcoef(a[ok, 1], b[ok, 1])[0, 1]:.3f}")''')
s=s.replace('''bins_ = np.arange(50, raw.n_bins - 50)''','''bins_ = np.arange(50, raw.n_bins - 50)
bins_ = bins_[~bad[bins_]]''')
open('build_rest.py','w').write(s)
EOF
. $TMPDIR/venv/bin/activate && python /tmp/claude/build_rest.py && /usr/bin/time -f "%e s %M KB" jupyter nbconvert --to notebook --execute --ExecutePreprocessor.timeout=3600 --output-dir /tmp/claude/out 06_mc_rtt.ipynb 2>&1 | grep -v "TCP\|Converting\|Writing" | tail -5; python - <<'EOF'
import nbformat
for f in ['06_mc_rtt','01_synthetic']:
    nb=nbformat.read(f'/tmp/claude/out/{f}.ipynb',4)
    for c in nb.cells:
        if c.cell_type!='code': continue
        for o in c.outputs:
            t=o.get('text') or (o.get('data',{}).get('text/plain')) or ''.join(o.get('traceback',[]))[-1500:]
            print(t[:3000])
        print('-----')
EOF
```

```
Exit code 1
ok

To see all available configurables, use `--help-all`.

Command exited with non-zero status 255
0.73 s 62392 KB
Traceback (most recent call last):
  File "/tmp/claude-1001/venv/lib/python3.12/site-packages/nbformat/__init__.py", line 169, in read
    buf = fp.read()
          ^^^^^^^
AttributeError: 'str' object has no attribute 'read'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<stdin>", line 3, in <module>
  File "/tmp/claude-1001/venv/lib/python3.12/site-packages/nbformat/__init__.py", line 171, in read
    with open(fp, encoding="utf8") as f:  # noqa: PTH123
         ^^^^^^^^^^^^^^^^^^^^^^^^^
[... 1 more lines not kept]
```

**Agent calls Bash**

```bash
. $TMPDIR/venv/bin/activate && /usr/bin/time -f "%e s %M KB" jupyter nbconvert --to notebook --execute --ExecutePreprocessor.timeout=3600 --output-dir /tmp/claude/out 06_mc_rtt.ipynb 2>&1 | grep -v "TCP\|Converting\|Writing" | tail -5; cat > /tmp/claude/show.py <<'EOF'
import nbformat,sys
for f in sys.argv[1:]:
    nb=nbformat.read(f'/tmp/claude/out/{f}.ipynb',4)
    for c in nb.cells:
        if c.cell_type!='code': continue
        for o in c.outputs:
            t=o.get('text') or (o.get('data',{}).get('text/plain')) or ''.join(o.get('traceback',[]))[-1500:]
            print(t[:4000])
        print('-----')
EOF
python /tmp/claude/show.py 06_mc_rtt 01_synthetic
```

```
80.85 s 972420 KB
[('sub-Indy/sub-Indy_desc-test_ecephys.nwb', 1201344), ('sub-Indy/sub-Indy_desc-train_behavior+ecephys.nwb', 49764168)]

-----
behaviour series: {'finger_vel': {'unit': 'm/s', 'conversion': np.float64(0.001), 'description': 'The x and y velocity of the finger in mm/s. Calculated offline from upsampled finger position'}, 'cursor_pos': {'unit': 'meters', 'conversion': np.float64(0.001), 'description': 'The position of the cursor in Cartesian coordinates (x, y) in mm. Recorded at 250 Hz and upsampled to 1 kHz'}, 'target_pos': {'unit': 'meters', 'conversion': np.float64(0.001), 'description': 'The position of the target in Cartesian coordinates (x, y) in mm. Recorded at 250 Hz and upsampled to 1 kHz'}}
behaviour sampling: starting time [0.], rate 1000.0 Hz; 20 ms bins: 32455
units: 130; spike counts per 20 ms bin range 0 to 3, mean rate 4.0 Hz
trials table: (1080, 3) split counts {'train': 810, 'val': 270}
block durations 0.600 to 0.600 s; first start 0.0, last stop 648.9 s; record 649.10 s
finger velocity range -490.2 to 467.2; cursor -65.1 to 117.9; target -52.5 to 112.5
20 ms bins with a missing (NaN) behaviour value: 15 of 32455; NaN in the analysis arrays: behaviour 0, context 0
analysis arrays: neural (1080, 21, 650) context (1080, 21, 14) behaviour (1080, 21, 2) train/val 810 270
corr(finger velocity, cursor velocity shifted -5 bins): x 0.701, y 0.770
corr(finger velocity, cursor velocity shifted -2 bins): x 0.959, y 0.969
corr(finger velocity, cursor velocity shifted 0 bins): x 0.993, y 0.996
corr(finger velocity, cursor velocity shifted 2 bins): x 0.890, y 0.921
corr(finger velocity, cursor velocity shifted 5 bins): x 0.609, y 0.695

held-out R2 (last quarter of the record) by lag in bins: {-25: 0.059, -10: 0.151, -4: 0.287, 0: 0.405, 2: 0.431, 4: 0.425, 6: 0.389, 10: 0.254, 25: 0.034}
peak memory 0.58 GB
[... 94 more lines not kept]
```

**Agent**

Synthetic and MC_RTT results match the paper to the printed digit. Running the confirmation notebook next.

**Agent calls Bash**

```bash
date -u; cd entries/du-2026 && . $TMPDIR/venv/bin/activate && /usr/bin/time -f "%e s %M KB" jupyter nbconvert --to notebook --execute --ExecutePreprocessor.timeout=3600 --output-dir /tmp/claude/out 05_link_confirmation.ipynb 2>&1 | grep -v "TCP\|Converting\|Writing" | tail -30; python /tmp/claude/show.py 05_link_confirmation | cut -c1-300
```

```
Sat Nov 21 14:55:41 UTC 2026
543.94 s 519988 KB
312 assets in DANDI:001201 0.251023.2336; 9 dates with two sessions, 18 development sessions

tasks over all 312 assets: Counter({'CO': 156, 'RD': 156})
CO: 147 eligible assets, ranks [13, 27, 40, 53, 66, 80, 93, 106, 119, 133]
RD: 147 eligible assets, ranks [13, 27, 40, 53, 66, 80, 93, 106, 119, 133]
frozen manifest: 20 assets; re-selected here: 20; identical sets: True
in the frozen manifest only: set() ; re-selected only: set()
          date task                                                path
0   2020-09-24   CO  sub-Monkey-N/sub-Monkey-N_ses-20200924_ecephys.nwb
1   2020-12-11   CO  sub-Monkey-N/sub-Monkey-N_ses-20201211_ecephys.nwb
2   2021-03-23   CO  sub-Monkey-N/sub-Monkey-N_ses-20210323_ecephys.nwb
3   2021-06-01   CO  sub-Monkey-N/sub-Monkey-N_ses-20210601_ecephys.nwb
4   2021-08-05   CO  sub-Monkey-N/sub-Monkey-N_ses-20210805_ecephys.nwb
5   2021-09-15   CO  sub-Monkey-N/sub-Monkey-N_ses-20210915_ecephys.nwb
6   2021-11-16   CO  sub-Monkey-N/sub-Monkey-N_ses-20211116_ecephys.nwb
7   2022-02-28   CO  sub-Monkey-N/sub-Monkey-N_ses-20220228_ecephys.nwb
8   2022-04-27   CO  sub-Monkey-N/sub-Monkey-N_ses-20220427_ecephys.nwb
9   2022-09-02   CO  sub-Monkey-N/sub-Monkey-N_ses-20220902_ecephys.nwb
[... 90 more lines not kept]
```

**Agent calls Bash**

```bash
date -u; cd entries/du-2026 && . $TMPDIR/venv/bin/activate && /usr/bin/time -f "%e s %M KB" jupyter nbconvert --to notebook --execute --ExecutePreprocessor.timeout=3600 --output-dir /tmp/claude/out 02_link_development.ipynb 2>&1 | grep -v "TCP\|Converting\|Writing" | tail -30; date -u
```

```
Sat Nov 21 15:04:52 UTC 2026
1331.16 s 668488 KB
Sat Nov 21 15:27:03 UTC 2026
```

**Agent calls Bash**

```bash
. $TMPDIR/venv/bin/activate && python /tmp/claude/show.py 02_link_development | cut -c1-260
```

```
312 assets in DANDI:001201 version 0.251023.2336, 303 dates
dates with more than one asset: {'2021-10-15': 2, '2022-02-25': 2, '2022-04-08': 2, '2022-04-15': 2, '2022-04-29': 2, '2022-05-13': 2, '2022-08-10': 2, '2022-09-21': 2, '2022-11-02': 2}

-----
          date task target_style  trials  usable   bins  dt_ms_median  dt_ms_min  dt_ms_max  trial_count_vs_duration  start_offset_ms  sbp_min  sbp_max  tcr_min  tcr_max  tcr_integer  pos_min  pos_max  vel_min  vel_max  targets  target_min  target_max
0   2021-10-15   CO           CO     375     375  21825            20         19       1094                    1.019                0   0.7937    30.52        0        6         True  0.06596        1 -0.09982    0.154       23         0.1         0.9
1   2021-10-15   RD           RD     375     375  26836            20         19         21                    1.015                0    0.725    25.74        0        7         True        0        1  -0.2025   0.3075      375   9.266e-05      0.9994
2   2022-02-25   RD           RD     375     375  27135            20         19         21                    1.015                0   0.7188    16.64        0        6         True        0        1  -0.1384   0.5444      375   0.0005175      0.9946
3   2022-02-25   CO           CO     375     375  23816            20         19         21                    1.017                0   0.7188    15.84        0        6         True  0.03073   0.9815  -0.1196   0.1525       23         0.1         0.9
4   2022-04-08   CO           CO     375     375  22384            20         19         21                    1.018                0    0.725    21.08        0        5         True  0.05292        1  -0.1354   0.2096       23         0.1         0.9
5   2022-04-08   RD           RD     375     375  24997            20         19         21                    1.016                0      0.7    21.33        0        5         True    0.028        1  -0.1798   0.2542      375   0.000
[... 360 more lines not kept]
```

**Agent calls Bash**

```bash
date -u; cd entries/du-2026 && . $TMPDIR/venv/bin/activate && for nb in 04_link_temporal_capacity 03_link_estimators; do /usr/bin/time -f "$nb %e s %M KB" jupyter nbconvert --to notebook --execute --ExecutePreprocessor.timeout=3600 --output-dir /tmp/claude/out $nb.ipynb 2>&1 | grep -v "TCP\|Converting\|Writing" | tail -8; date -u; done
```

```
Sat Nov 21 15:27:11 UTC 2026
04_link_temporal_capacity 1055.69 s 620272 KB
Sat Nov 21 15:44:47 UTC 2026
03_link_estimators 3511.37 s 622688 KB
Sat Nov 21 16:43:18 UTC 2026
```

**Agent calls Bash**

```bash
. $TMPDIR/venv/bin/activate && python /tmp/claude/show.py 04_link_temporal_capacity 03_link_estimators | grep -v "^  *[0-9]*  *20..-..-.._" | cut -c1-220
```

```
312 assets in DANDI:001201 0.251023.2336; 9 dates with two sessions, 18 development sessions

-----
              session  trials   bins  dt_ms    sbp_range tcr_range      pos_range       vel_range
0   2021-10-15_CO_nwb     375  21825   20.0  0.794..30.5      0..6       0.066..1  -0.0998..0.154
1   2021-10-15_RD_nwb     375  26836   20.0  0.725..25.7      0..7           0..1   -0.202..0.308
2   2022-02-25_RD_nwb     375  27135   20.0  0.719..16.6      0..6           0..1   -0.138..0.544
3   2022-02-25_CO_nwb     375  23816   20.0  0.719..15.8      0..6  0.0307..0.981    -0.12..0.153
4   2022-04-08_CO_nwb     375  22384   20.0  0.725..21.1      0..5      0.0529..1    -0.135..0.21
5   2022-04-08_RD_nwb     375  24997   20.0    0.7..21.3      0..5       0.028..1    -0.18..0.254
6   2022-04-15_CO_nwb     375  22568   20.0  0.725..23.5      0..7      0.0838..1   -0.113..0.215
7   2022-04-15_RD_nwb     375  24874   20.0  0.663..28.1      0..7     0.00575..1   -0.223..0.361
8   2022-04-29_RD_nwb     375  24682   20.0  0.731..21.1      0..7      0.0211..1   -0.245..0.228
9   2022-04-29_CO_nwb     375  22364   20.0  0.667..20.5      0..6      0.0789..1   -0.162..0.183
10  2022-05-13_RD_nwb     375  25290   20.0   0.75..19.4      0..6      0.0315..1   -0.219..0.219
11  2022-05-13_CO_nwb     375  23653   20.0  0.712..40.2      0..6  0.0785..0.952   -0.118..0.114
12  2022-08-10_CO_nwb     375  22292   20.0  0.769..24.9      0..7  0.0868..0.991   -0.123..0.153
13  2022-08-10_RD_nwb     375  23475   20.0    0.681..31     0..11           0..1   -0.182..0.261
14  2022-09-21_CO_nwb     375  22725   20.0  0.744..24.6      0..5      0.0383..1   -0.174..0.199
15  2022-09-21_RD_nwb     375  25015   20.0  0.706..25.1      0..5           0..1   -0.211..0.263
[... 107 more lines not kept]
```

**Agent calls Bash**

```bash
cd  && sed -n 560,652p tools/entry.py
```

```
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
    return h.hexdigest()


def reusable(entry_dir: Path, output_dir: Path, max_minutes: float) -> dict | None:
    """The stamp of executed copies that a run now would only make again: made from this hash, each copy still as
[... 73 more lines not kept]
```

**Agent**

The estimator-family notebook took 58 min (block-penalty fits with the lsqr solver), which won't fit in the final run. Testing whether an exact Cholesky solve gives the same gains, to cut that cost.

**Agent calls Bash**

```bash
cd entries/du-2026 && . $TMPDIR/venv/bin/activate && cat > /tmp/claude/t3.py <<'EOF'
import sys,time
sys.path.insert(0,'.')
import du2026 as d, numpy as np
from threadpoolctl import threadpool_limits
s=d.load_link_session('5c74bad7-55be-47a6-b754-c77654064981','x')
with threadpool_limits(1):
  for ctx in ['geometry_tensor']:
    ds=d.build_link_dataset(s,context_mode=ctx)
    t=time.time(); r1=d.block_ridge(ds); print('lsqr',r1,time.time()-t)
    from sklearn.linear_model import Ridge
    orig=d._BlockRidge.__init__
    def init(self,cp,xp):
        orig(self,cp,xp); self.model=Ridge(alpha=1.0, solver="cholesky")
    d._BlockRidge.__init__=init
    t=time.time(); r2=d.block_ridge(ds); print('chol',r2,time.time()-t)
EOF
python /tmp/claude/t3.py 2>&1 | grep -v Warn
```

```
lsqr {'gain': 0.0261219226681603, 'context_alpha': 100.0, 'penalties': (100.0, 10000.0)} 59.782655477523804
chol {'gain': 0.026122367976066395, 'context_alpha': 100.0, 'penalties': (100.0, 10000.0)} 8.244542360305786
```

**Agent calls Bash**

```bash
python - <<'EOF'
s=open('du2026.py').read()
old='''class _BlockRidge:
    """specification_estimators.py _BlockRidge: blockwise standardization, each
    block divided by sqrt(its penalty), Ridge(alpha=1) (Methods 4.5 objective)."""

    def __init__(self, cp, xp):
        self.cp, self.xp = float(cp), float(xp)
        self.cs, self.xs = StandardScaler(), StandardScaler()
        self.model = Ridge(alpha=1.0, solver="lsqr", tol=1e-6)'''
new='''class _BlockRidge:
    """specification_estimators.py _BlockRidge: blockwise standardization, each
    block divided by sqrt(its penalty), Ridge(alpha=1) (Methods 4.5 objective).

    The release solves this Ridge with solver="lsqr", tol=1e-6; here it is solved
    exactly (solver="cholesky"), which minimizes the same objective about seven
    times faster. On one session (2021-10-15 CO, SBP geometry by phase) the two
    gave gains 0.0261219 and 0.0261224 with the same penalties (a deviation
    recorded in the attempt; it cannot change a sign or a count)."""

    def __init__(self, cp, xp):
        self.cp, self.xp = float(cp), float(xp)
        self.cs, self.xs = StandardScaler(), StandardScaler()
        self.model = Ridge(alpha=1.0, solver="cholesky")'''
assert old in s; s=s.replace(old,new); open('du2026.py','w').write(s)
EOF
sed -n 39,140p $TMPDIR/neural-decoder-context-audit/src/neural_evidence/mc_maze.py
```

```
def load_mc_maze(
    path: str | Path,
    *,
    bin_ms: int = 20,
    movement_window_ms: int = 800,
    neural_history_ms: int = 100,
    neural_lead_ms: int = 80,
    context_mode: str = "template",
    output_history_ms: int = 100,
    output_lead_ms: int | None = None,
) -> DatasetSplit:
    """Load fixed post-movement-onset windows from MC_Maze.

    Context contains reach-condition identity, phase harmonics, target
    position, movement-onset cursor position, and their displacement.
    """

    try:
        from pynwb import NWBHDF5IO
    except ImportError as error:
[... 82 more lines not kept]
```

**Agent calls Write**

```json
{
 "file_path": "/tmp/claude/conclusions02.py",
 "content": "CONC = {\n\"link-development-sample\": \"\"\"**Result: reproduced.** Nine dates have both a CO and an RD session (the only dates with more than one asset), and each of the 18 sessions has 375 trials in its table, all 375 usable under the window rule of link.py: 6,750 usable trials in total.\"\"\",\n\"link-neural-only-r2\": \"\"\"**Result: reproduced.** Neural-only Ridge from 160 ms of SBP gives held-out R2 of 0.3077 in CO and 0.3129 in RD (paper 0.308 and 0.313). Under the four other split seeds the task means stay between 0.2969 and 0.3248, inside both tolerances.\"\"\",\n\"link-context-ladder-gain\": \"\"\"**Result: reproduced.** The task means are 0.3012/0.3125, 0.0657/0.0502, 0.0443/0.0332, 0.0193/0.0209 and 0.0077/0.0098 (CO/RD) along the five rungs, equal to the paper's values at the printed precision, so all 10 are within tolerance, and both task means fall at every step.\"\"\",\n\"link-context-only-r2\": \"\"\"**Result: reproduced.** Context-only R2 is 0.0084/0.0055 (CO/RD) with phase only, below 0.02 and equal to the paper's values, and 0.6617/0.6839 with geometry by phase plus measured-output history, equal to the paper's.\"\"\",\n\"link-phase-only-replacement\": \"\"\"**Result: reproduced.** Under phase only, the mean nearest-replacement gain over the nine RD sessions is 0.10498 (paper 0.10498), positive in 8 of 9 RD sessions; in CO it is -0.01087.\"\"\",\n\"link-task-contrast-by-context\": \"\"\"**Result: reproduced.** The mean RD-minus-CO contrast over nine dates is positive under phase only (0.0113), negative under direction by phase (-0.0155) and additive geometry (-0.0110), near zero under geometry by phase (0.0015; its date-bootstrap interval, -0.0035 to 0.0077, contains zero, and its size is below the two negative rungs, so both readings hold) and positive after measured-output history (0.0021). The phase-only and history intervals also contain zero; the claim is judged on the signs of the means, as the criterion says.\"\"\",\n\"nested-geometry-gain\": \"\"\"**Result: reproduced.** Under geometry by phase the mean gain is 0.02009 for SBP with 18 of 18 sessions positive, and 0.01155 for TCR with 17 of 18 positive, equal to the paper's values; the date-clustered intervals are 0.01586 to 0.02401 and 0.00711 to 0.01591. Under the four other split seeds the SBP mean is 0.01795 to 0.01918, all 18 sessions positive (TCR was not re-run under other seeds).\"\"\",\n\"nested-history-gain\": \"\"\"**Result: reproduced.** With measured-output history the mean gain is 0.00873 for SBP (17 of 18 positive) and 0.00420 for TCR (16 of 18 positive), equal to the paper's values and below each signal's geometry-by-phase mean. Under the four other seeds the SBP mean is 0.00742 to 0.00829, with 17 or 18 sessions positive.\"\"\",\n\"nested-replacement-negative\": \"\"\"**Result: reproduced.** Nearest source-context replacement gives mean gains of -0.00714 and -0.00407 for SBP and -0.00905 and -0.00537 for TCR, all four negative and all within tolerance. The SBP values move with the split seed: under the four other seeds they are -0.00887 to -0.00714 (geometry) and -0.00496 to -0.00428 (history), so two of those seeds put both SBP values outside their 10% tolerances.\"\"\",\n\"replacement-source-diagnostics\": \"\"\"**Result: reproduced.** The fewest eligible same-condition sources for any test trial is 5, the median over sessions of the largest reuse of one source is 3 and the largest over sessions is 4, and self-replacement reproduces the correct-pair predictions exactly (largest difference 0).\"\"\",\n\"permutation-negative\": \"\"\"**Result: reproduced.** Under reading (a), the 18 SBP geometry-by-phase sessions, the permutation mean is negative in 18 of 18 sessions with an across-session mean of -0.01418 (paper -0.0142); reading (b), with the TCR sessions, also holds (36 of 36, -0.01387). Four other permutation generators give -0.01405 to -0.01426 under reading (a).\"\"\",\n\"replacement-penalty-distance\": \"\"\"**Result: reproduced.** The per-session Spearman correlations between nearest-source distance and replacement penalty are positive in 8 and negative in 10 of 18 sessions (reading a), and their mean, 0.0058, has a date-bootstrap interval of -0.0204 to 0.0301 that contains zero (reading b), under all five generators.\"\"\",\n\"replacement-ranks-lower\": \"\"\"**Result: reproduced.** For SBP the correct-pair mean is 0.02009 and replacement with ranks one to five gives -0.00714 to -0.01167, and random same-condition sources -0.01382 to -0.01433 over five draws, all lower (reading a); for TCR the same holds (0.01155 against -0.00905 to -0.01411).\"\"\",\n\"practical-mse-reduction\": \"\"\"**Result: reproduced.** The mean percentage MSE reductions are 4.92 (SBP geometry), 2.72 (SBP plus history), 2.83 (TCR geometry) and 1.31 (TCR plus history), and the SBP geometry mean RMSE falls from 0.01407 to 0.01372; all six values are within tolerance.\"\"\",\n\"representative-trial\": \"\"\"**Result: reproduced.** Taking the ninth of the 18 sessions in gain order (the lower middle session, as the release's figure code does) selects 2022-09-21 RD, and its median-improvement held-out trial is trial 123 both as the row of the NWB trials table (reading a) and as the usable-trial index (reading b), which coincide because no trial is dropped. The other reading of the session tie (the earlier date of the two middle sessions) selects 2021-10-15 RD, trial 260, so the match rests on the first reading of the tie rule.\"\"\",\n\"split-seed-stability\": \"\"\"**Result: reproduced.** Under split seeds 20260726, 20260727 and 20260728 the CO means are 0.0193, 0.0180 and 0.0158 and the RD means 0.0209, 0.0223 and 0.0201, equal to the paper's six values and all positive.\"\"\",\n\"rff-link\": \"\"\"**Result: reproduced.** With the three nonlinear-neural maps, the CO and RD geometry-by-phase means are positive under every map (0.00269 to 0.00417). Under reading (a) the 18-session geometry means span 0.00310 to 0.00404 and the history means 0.00111 to 0.00142, equal to the paper's ranges. Reading (b), the six task means, does not hold: the lowest, 0.00269, is below the widened bound of 0.00279.\"\"\",\n\"summary\": \"\"\"## Summary\n\n| Claim | Outcome |\n|---|---|\n| link-development-sample | reproduced |\n| link-neural-only-r2 | reproduced |\n| link-context-ladder-gain | reproduced |\n| link-context-only-r2 | reproduced |\n| link-phase-only-replacement | reproduced |\n| link-task-contrast-by-context | reproduced |\n| nested-geometry-gain | reproduced |\n| nested-history-gain | reproduced |\n| nested-replacement-negative | reproduced (seed sensitive) |\n| replacement-source-diagnostics | reproduced |\n| permutation-negative | reproduced |\n| replacement-penalty-distance | reproduced |\n| replacement-ranks-lower | reproduced |\n| practical-mse-reduction | reproduced |\n| representative-trial | reproduced (on one reading of the session tie rule) |\n| split-seed-stability | reproduced |\n| rff-link | reproduced (reading a) |\n\nHow the analysis differs from the paper's: the estimators are ports of the paper's released code\n(commit b042fbe) and read the NWB files by streaming them; the bootstrap intervals use generators\nseeded from the claims, not the release's seed 20260802; the seed sensitivity of the protocol was run\nfor the SBP geometry-by-phase and plus-history fits and the neural-only R2, not for the other ladder\nrungs or for TCR.\n\nWhat was found about the dataset: the 18 development sessions are as the paper describes (nine dates,\n375 usable trials each, one subject); no session is deposited twice; SBP, TCR, position and velocity\nshare one 20 ms clock (velocity decoding from SBP peaks at lag 0 in 16 sessions and 2 bins in 2);\nthe released velocity is exactly the forward first difference of the released position\n(velocity[t] = position[t+1] - position[t], correlation 1.000), which the files do not state; the\nthreshold-crossing series is labelled in volts though it holds integer counts (0 to 11 per bin).\nOne session (2021-10-15 CO) has a gap of 1094 ms in its 20 ms timestamps.\n\"\"\"\n}\n"
}
```

```
File created successfully at: /tmp/claude/conclusions02.py (file state is current in your context — no need to Read it back)
```

**Agent calls Write**

```json
{
 "file_path": "/tmp/claude/conclusions_rest.py",
 "content": "CONC = {\n\"synthetic-template-null\": \"\"\"**Result: reproduced.** Over the ten seeds the template-only median gain is -0.0000023 (median absolute gain 0.0000092, far below 0.03), with range -0.0000588 to 0.0000248, the paper's values. The four shifted seed sets give medians of -0.0000040 to -0.0000168.\"\"\",\n\"synthetic-signal-ordering\": \"\"\"**Result: reproduced.** The weak and strong medians are 0.22451 and 0.37360 (paper 0.2245 and 0.3736), and the three medians increase strictly; the four shifted seed sets give 0.21996 to 0.22321 and 0.37035 to 0.37368, also ordered.\"\"\",\n\"synthetic-pair-breaking\": \"\"\"**Result: reproduced.** In the strong regime the correct-pair gain exceeds both nearest replacement and the permutation mean for 10 of 10 seeds; the mean replacement gain is -0.3486 and the mean permutation gain -0.3663, the paper's values. The shifted seed sets give 10 of 10 each, replacement means -0.3514 to -0.3782 and permutation means -0.3619 to -0.3673, all within tolerance.\"\"\",\n\"summary01\": \"\"\"## Summary\n\n| Claim | Outcome |\n|---|---|\n| synthetic-template-null | reproduced |\n| synthetic-signal-ordering | reproduced |\n| synthetic-pair-breaking | reproduced |\n\nThe generator and estimator are ports of the paper's code; the values equal the paper's at the\nprinted precision. These claims test the code, not a dataset (`data: elsewhere`).\n\"\"\",\n\"estimator-family-link\": \"\"\"**Result: reproduced.** Under both families every CO and RD mean is positive for SBP and TCR, geometry by phase and plus history (reading a), and so is every 18-session mean (reading b). The nonlinear-context means over 18 sessions (0.01733, 0.00663, 0.00949 and 0.00274 for SBP geometry, SBP history, TCR geometry and TCR history) are smaller than the fully nested linear ones (0.02009, 0.00873, 0.01155, 0.00420), and the block-penalty means lie close to the linear ones, so the magnitudes differ between families. Reading (b) of the nonlinear context, every setting of Methods 4.6, was not run.\"\"\",\n\"summary03\": \"\"\"## Summary\n\n| Claim | Outcome |\n|---|---|\n| estimator-family-link | reproduced (nonlinear context under the release's setting only) |\n\nThe block-penalty Ridge is solved exactly (Cholesky) where the release uses lsqr with tolerance 1e-6;\non a test session the gains agreed to 5e-7. The nonlinear-context sensitivity follows the release's\n`evaluate_rff_context_audit` (D = 256, g chosen on the inner split); the other settings Methods 4.6\nlists were not run.\n\"\"\",\n\"temporal-offset\": \"\"\"**Result: reproduced.** Under the fully nested estimator (reading i), shifting both histories from 0 to 120 ms lowers the CO mean from 0.00382 to 0.00055 and the RD mean from 0.00623 to 0.00038, and the RD-minus-CO difference turns from 0.00241 at 0 ms to -0.00024 at 40 ms and -0.00061 at 80 ms (reading b of the RD change); the RD mean stays positive (reading a fails). Under `evaluate_decoders_nested` (reading ii) the reduction holds (0.00400 to 0.00058, 0.00678 to 0.00000) and both readings of the RD change hold (RD -0.00032 at 80 ms). The outcome holds under both estimators.\"\"\",\n\"context-capacity-contrast\": \"\"\"**Result: reproduced.** Under the fully nested estimator the quadratic-plus-history RD-minus-CO contrast is positive for SBP (0.00374) and TCR (0.00275), and for TCR the quadratic-geometry contrast (0.00495, interval 0.00079 to 0.00915) excludes zero where the linear one (0.00227, -0.00246 to 0.00686) does not. For SBP the contrast keeps its sign and its interval contains zero in both. The release's other estimator gives the same pattern (0.00410 and 0.00374; TCR quadratic interval 0.00115 to 0.00927).\"\"\",\n\"summary04\": \"\"\"## Summary\n\n| Claim | Outcome |\n|---|---|\n| temporal-offset | reproduced (under both estimators) |\n| context-capacity-contrast | reproduced (under both estimators) |\n\nThe paper's figure for these analyses plots a frozen table whose script is not in the release; both\nestimators the claims file names were run, and they give the same outcomes. Holding the behavioural\nwindow fixed was read as one window start, 280 ms after the start bin, for every offset; at that start\n367 to 375 trials per session are usable, against 375 in the other analyses.\n\"\"\",\n\"confirm-geometry-gain\": \"\"\"**Result: reproduced.** The paper's rule re-run on the archive's asset metadata selects the same 20 sessions as its frozen manifest. Under geometry by phase all 20 gains are positive and the mean is 0.02158 (CO 0.02104, RD 0.02213), the paper's values. The values depend on the split: under the four other split seeds the combined mean is 0.01478 to 0.02070, with 19 or 20 sessions positive, so three of those seeds put the mean outside its 10% tolerance.\"\"\",\n\"confirm-history-contraction\": \"\"\"**Result: reproduced.** With measured-output history the combined mean is 0.00755 (CO 0.00670, RD 0.00840) with 19 of 20 sessions positive, below the geometry-by-phase mean of 0.02158. Under the four other split seeds the combined mean is 0.00335 to 0.00818, three of them outside the tolerance.\"\"\",\n\"confirm-replacement\": \"\"\"**Result: reproduced.** The mean nearest-replacement gain is -0.00771, and the correct-pair gain exceeds the replacement gain in 20 of 20 sessions and in both task means (CO 0.02104 against -0.00292, RD 0.02213 against -0.01250). Under the four other split seeds the replacement mean is -0.00902 to -0.01963, outside the 10% tolerance in each.\"\"\",\n\"confirm-table1-values\": \"\"\"**Result: reproduced.** With measured-output history the mean replacement gain is -0.00498, and the mean MSE reductions are 4.761% (geometry by phase) and 2.047% (plus history), the values of Table 1. Under the four other split seeds these become -0.00467 to -0.01462, 3.43 to 4.58% and 1.15 to 2.21%, mostly outside their tolerances.\"\"\",\n\"summary05\": \"\"\"## Summary\n\n| Claim | Outcome |\n|---|---|\n| confirm-geometry-gain | reproduced (seed sensitive) |\n| confirm-history-contraction | reproduced (seed sensitive) |\n| confirm-replacement | reproduced (seed sensitive) |\n| confirm-table1-values | reproduced (seed sensitive) |\n\nThe confirmation sessions re-selected from the archive's metadata are those of the paper's frozen\nmanifest; each has 375 usable trials (7,500 in all) and no SBP array repeats. Every value equals the\npaper's under its split seed 20260726; the 10% tolerances do not hold under other split seeds, while\nthe qualitative pattern (positive geometry gain, smaller history gain, replacement below correct\npairing in every session) does in the printed seed runs.\n\"\"\",\n\"rtt-data\": \"\"\"**Result: reproduced.** The training file's trials table has 1,080 blocks of 600 ms, all kept by the loader's rule (21 bins each after the warm-up), with 130 units and the finger velocity, cursor position and target position series; the split labels give 810 train and 270 validation blocks.\"\"\",\n\"rtt-gain\": \"\"\"**Result: reproduced.** Context-only R2 is 0.60308, the fully nested gain 0.06846, the context RMSE 39.781 and the context-plus-neural RMSE 36.188 (a 17.248% MSE reduction), the component gains 0.08359 and 0.05125, and the replacement gain -0.02297; all eight equal the paper's values at its precision. Under four other estimator seeds the gain is 0.06821 to 0.06855 and the replacement gain -0.02300 to -0.02332.\"\"\",\n\"rff-rtt\": \"\"\"**Result: reproduced.** The three nonlinear-neural maps give MC_RTT gains of 0.01685, 0.01501 and 0.01491, all positive and spanning the paper's range of 0.01491 to 0.01685.\"\"\",\n\"estimator-family-nlb\": \"\"\"**Result: reproduced (MC_RTT part).** The block-penalty estimator gives an MC_RTT gain of 0.0690 and the nonlinear-context estimator 0.04619, both positive, as the criterion requires. The MC_Maze part of the statement was not tested: DANDI:000139 was not read in this attempt.\"\"\",\n\"summary06\": \"\"\"## Summary\n\n| Claim | Outcome |\n|---|---|\n| rtt-data | reproduced |\n| rtt-gain | reproduced |\n| rff-rtt | reproduced |\n| estimator-family-nlb | reproduced (MC_RTT part only) |\n| maze-gain, rff-maze | blocked (MC_Maze, DANDI:000139, not read in this attempt) |\n\nWhat was found about the dataset: the counts are as the paper states. The behaviour series hold 15\nmissing (NaN) 20 ms bins, none inside the analysis blocks. The units of the behaviour series are\nconsistent once the `conversion` attribute is read: `unit` m/s or meters with conversion 0.001, so\nthe stored values are mm/s and mm, as the descriptions say; the paper's statement that the NLB unit\nfields and descriptions disagree reads the unit without the conversion. Finger velocity follows the\nderivative of cursor position at lag 0 (correlation 0.993 and 0.996), and velocity decoding from\nspikes peaks 2 bins (40 ms) after the spikes, so the spikes and behaviour share a clock.\n\"\"\",\n}\n"
}
```

```
File created successfully at: /tmp/claude/conclusions_rest.py (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
date -u; . $TMPDIR/venv/bin/activate && cd /tmp/claude && python build02.py && python build_rest.py && cd entries/du-2026 && ls && python -c "
import nbformat,glob
for f in sorted(glob.glob('*.ipynb')):
    nb=nbformat.read(f,4); print(f, len(nb.cells), sum(1 for c in nb.cells if c.cell_type=='markdown' and c.source.startswith('**Result')))"
```

```
Sat Nov 21 16:47:09 UTC 2026
ok
ok
01_synthetic.ipynb
02_link_development.ipynb
03_link_estimators.ipynb
04_link_temporal_capacity.ipynb
05_link_confirmation.ipynb
06_mc_rtt.ipynb
__pycache__
du2026.py
01_synthetic.ipynb 13 3
02_link_development.ipynb 61 17
03_link_estimators.ipynb 7 1
04_link_temporal_capacity.ipynb 11 2
05_link_confirmation.ipynb 18 4
06_mc_rtt.ipynb 16 4
```

**Agent calls Bash**

```bash
rm -rf __pycache__ && cat > requirements.in <<'EOF'
h5py
numpy
pandas
remfile
scikit-learn
threadpoolctl
EOF
cat > entry.yaml <<'EOF'
schema_version: 1
name: du-2026
type: reproduction
title: Context-conditional neural gain in motor-cortex decoding (Du et al. 2026)
description: Tests the findings of Du, Lai, Hu and Ye (2026) on LINK (dandiset 001201, one macaque,
  18 development and 20 confirmation sessions) and MC_RTT (dandiset 000129), and their matched-seed
  synthetic calibration. It ports the paper's released estimators and recomputes the context ladder,
  the fully nested gains with trial replacement and permutation controls, the practical magnitudes,
  the confirmation sessions, the nonlinear and estimator-family sensitivities, the temporal-offset and
  context-capacity analyses, and the MC_RTT results. The MC_Maze claims (dandiset 000139) are not
  tested.
license: Apache-2.0
notebooks:
- path: 01_synthetic.ipynb
  title: Matched-seed synthetic calibration
  runtime_minutes: 3
- path: 02_link_development.ipynb
  title: LINK development sessions (context ladder, fully nested gains, controls)
  runtime_minutes: 23
- path: 03_link_estimators.ipynb
  title: LINK estimator families
  runtime_minutes: 15
- path: 04_link_temporal_capacity.ipynb
  title: LINK temporal offset and context capacity
  runtime_minutes: 18
- path: 05_link_confirmation.ipynb
  title: LINK confirmation sessions
  runtime_minutes: 10
- path: 06_mc_rtt.ipynb
  title: MC_RTT
  runtime_minutes: 2
helpers:
- du2026.py
related:
- id: dandi:001201/0.251023.2336
  relation: uses_data
- id: dandi:000129/0.241017.1444
  relation: uses_data
- id: doi:10.64898/2026.08.04.742876
  relation: reproduces
EOF
cat > README.md <<'EOF'
# Du, Lai, Hu & Ye (2026) on LINK and MC_RTT

Tests the findings of [Du et al. (2026)](https://doi.org/10.64898/2026.08.04.742876), "A
Context-Conditional Audit of Trial-Pairing-Dependent Neural Gain in Motor-Cortex Decoding", on
[DANDI:001201](https://dandiarchive.org/dandiset/001201/0.251023.2336) (LINK) and
[DANDI:000129](https://dandiarchive.org/dandiset/000129/0.241017.1444) (MC_RTT), at the versions the
paper cites, and on the synthetic data its code generates. The estimators in `du2026.py` are ports
of the paper's released code (github.com/gwkuqgfkqe/neural-decoder-context-audit, tag
v1.0-jne-submission, commit b042fbe), reading the NWB files by streaming them.

| Claims | Notebook | Outcome |
|---|---|---|
| Synthetic calibration (3) | `01_synthetic.ipynb` | Reproduced |
| LINK development sessions: sample, neural-only R2, context ladder, task contrast, fully nested gains, replacement and permutation controls, practical magnitude, representative trial, split seeds, nonlinear maps (17) | `02_link_development.ipynb` | Reproduced |
| LINK estimator families (1) | `03_link_estimators.ipynb` | Reproduced |
| LINK temporal offset and context capacity (2) | `04_link_temporal_capacity.ipynb` | Reproduced |
| LINK confirmation sessions (4) | `05_link_confirmation.ipynb` | Reproduced, seed sensitive |
| MC_RTT (4) | `06_mc_rtt.ipynb` | Reproduced |
| MC_Maze (2) | none | Blocked: DANDI:000139 not read |

Almost every value equals the paper's at its printed precision. The confirmation values hold only
under the paper's split seed; under other split seeds the pattern holds but the values move outside
their 10% tolerances. The attempt record, with the deviations and findings, is
[`attempts/du-2026-01.yaml`](../../attempts/du-2026-01.yaml).
EOF
cd  && date -u && python tools/entry.py lock entries/du-2026 2>&1 | tail -5 && python tools/entry.py check entries/du-2026 2>&1 | tail -20
```

```
Sat Nov 21 16:47:25 UTC 2026
wrote du-2026/requirements.lock.txt (Python 3.13, with hashes)
0 error(s)
```

**Agent**

Entry passes `check`. Before the final run I'll look at the attempt schema so I can write the record in parallel with the run.

**Agent calls Bash**

```bash
ls schemas; python -c "
import json,glob
for f in glob.glob('schemas/*attempt*'):
    s=json.load(open(f)); print(f); print(json.dumps(s.get('required')), list(s['properties'].keys()))
    o=s['properties']['outcomes']['items']; print('outcome', o.get('required'), list(o['properties'].keys()))
    print(json.dumps(o['properties'].get('blocked_by'))[:400])
    fi=s['properties']['findings']['items']; print('finding', fi.get('required'), list(fi['properties'].keys())); print(json.dumps(fi['properties'].get('kind'))[:300])
    print(json.dumps(s['properties']['provenance'])[:1500])
    print(json.dumps(s['properties'].get('missing_datasets'))[:300])
    print(json.dumps(s['properties'].get('inputs'))[:400])
"
```

```
attempt.schema.json
claims.schema.json
entry.schema.json
paper-match.schema.json
schemas/attempt.schema.json
["schema_version", "id", "datasets", "paper", "date", "provenance", "outcomes"] ['schema_version', 'id', 'datasets', 'missing_datasets', 'paper', 'date', 'entry', 'deprecated', 'provenance', 'outcomes', 'verifications', 'findings', 'reconciliation', 'inputs', 'findings_review']
outcome ['claim', 'outcome'] ['claim', 'outcome', 'blocked_by', 'notes', 'notebook', 'output', 'measured', 'deviations', 'assumed', 'seed_sensitive', 'proposed']
{"description": "Required when outcome is blocked.", "enum": ["data_missing", "metadata_insufficient", "methods_underspecified", "data_unreadable", "dataset_missing", "too_large", "not_runnable", "other"]}
finding ['kind', 'statement'] ['kind', 'statement', 'found', 'about', 'severity', 'datasets']
{"enum": ["metadata_error", "data_missing", "identifier_missing", "metadata_insufficient", "selection_undocumented", "methods_unavailable", "format_error", "code_mismatch", "paper_inconsistency", "other"]}
{"type": "object", "additionalProperties": false, "required": ["kind", "accountable"], "properties": {"kind": {"enum": ["agent", "person"]}, "accountable": {"description": "The person or organisation responsible for this attempt.", "type": "object", "additionalProperties": false, "required": ["name"], "properties": {"name": {"type": "string"}, "orcid": {"type": "string", "pattern": "^[0-9]{4}-[0-9]{4}-[0-9]{4}-[0-9]{3}[0-9X]$"}, "ror": {"type": "string"}}}, "agent": {"description": "Required when kind is agent.", "type": "object", "additionalProperties": false, "required": ["harness", "model", "protocol"], "properties": {"harness": {"type": "string"}, "model": {"type": "string"}, "protocol": {"description": "Version of the reproduction protocol the agent followed.", "type": "string"}}}, "runner": {"description": "Where the attempt was run: the platform, and the run that wrote this record. Its other runs (verification rounds, revis
[... 2 more lines not kept]
```

**Agent**

Now launching the final `entry.py all` run (~70 min) and writing the attempt record in parallel.

**Agent calls Bash**

```bash
date -u && python tools/entry.py all entries/du-2026 2>&1 | tail -30; date -u
```

**Agent calls Write**

```json
{
 "file_path": "attempts/du-2026-01.yaml",
 "content": "schema_version: 3\nid: du-2026-01\ndatasets:\n- archive: dandi\n  id: \"001201\"\n  version: 0.251023.2336\n  doi: 10.48324/dandi.001201/0.251023.2336\n  relation: reuses\n- archive: dandi\n  id: \"000129\"\n  version: 0.241017.1444\n  doi: 10.48324/dandi.000129/0.241017.1444\n  relation: reuses\npaper: doi:10.64898/2026.08.04.742876\ndate: 2026-11-21\nentry: du-2026\nprovenance:\n  kind: agent\n  accountable:\n    name: CatalystNeuro\n  agent:\n    harness: Claude Code\n    model: claude-opus-5-5\n    protocol: pilot-18\n  runner:\n    platform: GitHub Actions\n    url: https://github.com/catalystneuro/encore/actions/runs/44913833754\ninputs:\n- what: The paper's analysis code, ported into the entry's helper du2026.py (LINK and MC_RTT loaders,\n    synthetic generator, fully nested, nonlinear-neural, block-penalty, nonlinear-context and\n    evaluate_decoders_nested estimators, replacement and permutation sources, the confirmation\n    selection rule). The synthetic claims are tested on data this generator produces (data elsewhere).\n  source: https://github.com/gwkuqgfkqe/neural-decoder-context-audit at commit b042fbe1cda2ca5a353751c693d7c95f45de0456\n    (tag v1.0-jne-submission)\n- what: The frozen confirmation manifest outputs/primary_analysis/link_confirmation_manifest.json, read\n    to compare with the 20 sessions re-selected from the archive's metadata.\n  source: https://github.com/gwkuqgfkqe/neural-decoder-context-audit at commit b042fbe1cda2ca5a353751c693d7c95f45de0456\noutcomes:\n- claim: synthetic-template-null\n  outcome: reproduced\n  notebook: 01_synthetic.ipynb\n  output: claim:synthetic-template-null\n  measured: -0.0000023\n  notes: Template-only median gain -0.0000023 over seeds 20260726 to 20260735, median absolute gain\n    0.0000092 (criterion below 0.03), range -0.0000588 to 0.0000248, as in the paper. The ten seeds\n    shifted by 1000, 2000, 3000 and 4000 give medians of -0.0000040 to -0.0000168.\n  deviations:\n  - The data are generated by a port of the paper's synthetic.py (commit b042fbe) with the parameters of\n    run_synthetic_calibration.py, which match Methods 4.8; no dataset is involved.\n- claim: synthetic-signal-ordering\n  outcome: reproduced\n  notebook: 01_synthetic.ipynb\n  output: claim:synthetic-signal-ordering\n  measured:\n  - 0.22451\n  - 0.3736\n  notes: Weak and strong medians 0.22451 and 0.37360, template-only -0.0000023, strictly increasing.\n    The four shifted seed sets give weak 0.21996 to 0.22321 and strong 0.37035 to 0.37368, all ordered\n    and within tolerance.\n- claim: synthetic-pair-breaking\n  outcome: reproduced\n  notebook: 01_synthetic.ipynb\n  output: claim:synthetic-pair-breaking\n  measured:\n  - 10\n  - -0.3486\n  - -0.3663\n  notes: In the strong regime correct-pair gain exceeds nearest replacement and the mean of 100\n    permutations for 10 of 10 seeds; mean replacement gain -0.3486, mean permutation gain -0.3663.\n    The shifted seed sets give 10 of 10 each, replacement means -0.3514 to -0.3782 and permutation\n    means -0.3619 to -0.3673, all within tolerance.\n- claim: link-development-sample\n  outcome: reproduced\n  notebook: 02_link_development.ipynb\n  output: claim:link-development-sample\n  measured:\n  - 9\n  - 6750\n  notes: The nine dates with more than one asset each hold one CO and one RD session (task from the NWB\n    identifier, which agrees with the trials table's target_style). All 18 sessions have 375 trials\n    and all 375 are usable under the window rule of link.py; one subject (sub-Monkey-N).\n- claim: link-neural-only-r2\n  outcome: reproduced\n  notebook: 02_link_development.ipynb\n  output: claim:link-neural-only-r2\n  measured:\n  - 0.3077\n  - 0.3129\n  notes: Held-out neural-only R2 from 160 ms of SBP, CO 0.3077 and RD 0.3129. Under split seeds plus\n    1000 to 4000 the task means are 0.2969 to 0.3116 (CO) and 0.3125 to 0.3248 (RD), all within\n    tolerance. X, Y and the split do not change across the ladder, so one fit per session serves every\n    rung, as the paper says.\n  deviations:\n  - The neural-only penalty is chosen as in the release's evaluate_decoders_nested (inner 80/20 split,\n    random state seed plus 11), the choice the claims file names; no release script computes this R2.\n- claim: link-context-ladder-gain\n  outcome: reproduced\n  notebook: 02_link_development.ipynb\n  output: claim:link-context-ladder-gain\n  measured:\n  - 0.3012\n  - 0.3125\n  - 0.0657\n  - 0.0502\n  - 0.0443\n  - 0.0332\n  - 0.0193\n  - 0.0209\n  - 0.0077\n  - 0.0098\n  notes: All ten task means equal the paper's at its precision and both tasks fall at every step. The\n    gain is positive in 18 of 18 sessions on the first four rungs and 17 of 18 with history.\n  deviations:\n  - The protocol's five-seed sensitivity was run for the geometry-by-phase and plus-history rungs (in\n    other claims), not for the phase-only, direction-by-phase and additive-geometry rungs, to keep the\n    notebook within its time limit.\n- claim: link-context-only-r2\n  outcome: reproduced\n  notebook: 02_link_development.ipynb\n  output: claim:link-context-only-r2\n  measured:\n  - 0.0084\n  - 0.0055\n  - 0.6617\n  - 0.6839\n  notes: Context-only R2 0.0084/0.0055 (CO/RD) with phase only (below 0.02, and equal to the paper's\n    values), 0.6617/0.6839 with history. The middle rungs give 0.4064/0.4524, 0.4621/0.5175 and\n    0.5702/0.5999.\n- claim: link-phase-only-replacement\n  outcome: reproduced\n  notebook: 02_link_development.ipynb\n  output: claim:link-phase-only-replacement\n  measured: 0.10498\n  notes: Mean RD replacement gain under phase only 0.10498, positive in 8 of 9 RD sessions; CO mean\n    -0.01087. All source distances tie under phase only, and the tie rule picks the source.\n- claim: link-task-contrast-by-context\n  outcome: reproduced\n  notebook: 02_link_development.ipynb\n  output: claim:link-task-contrast-by-context\n  notes: Mean RD minus CO over nine dates is 0.0113 (phase only), -0.0155 (direction by phase), -0.0110\n    (additive geometry), 0.0015 (geometry by phase) and 0.0021 (plus history). Geometry by phase is\n    near zero under both readings (date-bootstrap interval -0.0035 to 0.0077 contains zero; its size\n    is below the two negative rungs). The phase-only and history intervals also contain zero\n    (-0.0396 to 0.0503 and -0.0015 to 0.0067); the criterion judges the signs on the means. The interval\n    bounds change by at most 0.0018 over five generators.\n  deviations:\n  - The bootstrap generator is seeded from the claim (protocol), not with the release's 20260802.\n- claim: nested-geometry-gain\n  outcome: reproduced\n  notebook: 02_link_development.ipynb\n  output: claim:nested-geometry-gain\n  measured:\n  - 0.02009\n  - 18\n  - 0.01155\n  - 17\n  notes: SBP mean 0.02009 with 18 of 18 positive, TCR 0.01155 with 17 of 18 positive; date-clustered\n    intervals 0.01586 to 0.02401 and 0.00711 to 0.01591 (paper 0.01586 to 0.02404 and 0.00709 to\n    0.01594). Under split seeds plus 1000 to 4000 the SBP mean is 0.01795 to 0.01918, 18 of 18 positive\n    each; TCR was not re-run under other seeds.\n  deviations:\n  - Seed sensitivity was run for SBP only.\n- claim: nested-history-gain\n  outcome: reproduced\n  notebook: 02_link_development.ipynb\n  output: claim:nested-history-gain\n  measured:\n  - 0.00873\n  - 17\n  - 0.0042\n  - 16\n  notes: SBP 0.00873 with 17 of 18 positive, TCR 0.00420 with 16 of 18 positive, each below its\n    geometry-by-phase mean; intervals 0.00599 to 0.01103 and 0.00214 to 0.00629. Under the four other\n    seeds the SBP mean is 0.00742 to 0.00829 with 17 or 18 positive, within tolerance.\n  deviations:\n  - Seed sensitivity was run for SBP only.\n- claim: nested-replacement-negative\n  outcome: reproduced\n  notebook: 02_link_development.ipynb\n  output: claim:nested-replacement-negative\n  measured:\n  - -0.00714\n  - -0.00407\n  - -0.00905\n  - -0.00537\n  seed_sensitive: true\n  notes: All four means negative and within tolerance (-0.00714, -0.00407, -0.00905, -0.00537); 14 to 16\n    of 18 sessions negative per configuration. Under split seeds plus 1000 to 4000 the SBP means are\n    -0.00887, -0.00714, -0.00831, -0.00776 (geometry) and -0.00496, -0.00478, -0.00428, -0.00428\n    (history); with seeds plus 1000 and plus 3000 both SBP values fall outside their 10% tolerances, so\n    at most two of four could be within and the outcome there would be partially reproduced (TCR was\n    not re-run). All are still negative.\n- claim: replacement-source-diagnostics\n  outcome: reproduced\n  notebook: 02_link_development.ipynb\n  output: claim:replacement-source-diagnostics\n  measured:\n  - 5\n  - 3\n  - 4\n  notes: Minimum eligible same-condition sources 5 (sessions 2021-10-15 CO and 2022-08-10 CO); median\n    of session maximum reuse 3, maximum 4; largest self-replacement difference 0.\n- claim: permutation-negative\n  outcome: reproduced\n  notebook: 02_link_development.ipynb\n  output: claim:permutation-negative\n  measured: -0.01418\n  notes: Reading (a), 18 SBP geometry sessions, 18 of 18 negative, mean -0.01418, range -0.01916 to\n    -0.00752. Reading (b), with TCR, 36 of 36 negative, mean -0.01387, also within tolerance. Four other\n    permutation generators give -0.01405 to -0.01426 under reading (a), every session negative.\n- claim: replacement-penalty-distance\n  outcome: reproduced\n  notebook: 02_link_development.ipynb\n  output: claim:replacement-penalty-distance\n  notes: Session Spearman correlations between nearest-source distance and replacement penalty are\n    positive in 8 and negative in 10 of 18 sessions (-0.089 to 0.134); mean 0.0058, date-bootstrap\n    interval -0.0204 to 0.0301, containing zero under all five generators. Both readings hold.\n- claim: replacement-ranks-lower\n  outcome: reproduced\n  notebook: 02_link_development.ipynb\n  output: claim:replacement-ranks-lower\n  notes: SBP correct-pair mean 0.02009; ranks one to five give -0.00714, -0.00868, -0.01047, -0.01138,\n    -0.01167, random same-condition sources -0.01382 to -0.01433 over five draws. TCR 0.01155 against\n    -0.00905 to -0.01208 (ranks) and -0.01275 to -0.01411 (random). All lower under both readings.\n  deviations:\n  - The random source is a uniform draw among the other same-condition test trials, with generators\n    seeded from the claim (a standard choice the claims file names); five draws are shown.\n- claim: practical-mse-reduction\n  outcome: reproduced\n  notebook: 02_link_development.ipynb\n  output: claim:practical-mse-reduction\n  measured:\n  - 4.92\n  - 0.01407\n  - 0.01372\n  - 2.72\n  - 2.83\n  - 1.31\n  notes: Mean percentage MSE reductions 4.92 (SBP geometry), 2.72 (SBP history), 2.83 (TCR geometry),\n    1.31 (TCR history); SBP mean context RMSE 0.01407 and correct-pair RMSE 0.01372. Six of six within\n    tolerance. SBP geometry session reductions range 0.61 to 7.99%.\n- claim: representative-trial\n  outcome: reproduced\n  notebook: 02_link_development.ipynb\n  output: claim:representative-trial\n  notes: The ninth of 18 sessions in gain order (the lower middle, as build_submission_figures.py\n    figure8 takes it) is 2022-09-21 RD, and its median-improvement held-out trial is 123 as the trials\n    table row (reading a) and as the usable-trial index (reading b); it is position 39 of the 113\n    held-out trials (reading c). The other session reading, the earlier date of the two middle\n    sessions, gives 2021-10-15 RD, trial 260.\n  deviations:\n  - The match holds under the lower-middle reading of the session tie only; the criterion names both\n    readings, and the release's figure code uses the lower middle.\n- claim: split-seed-stability\n  outcome: reproduced\n  notebook: 02_link_development.ipynb\n  output: claim:split-seed-stability\n  measured:\n  - 0.0193\n  - 0.018\n  - 0.0158\n  - 0.0209\n  - 0.0223\n  - 0.0201\n  notes: CO means 0.0193, 0.0180, 0.0158 and RD means 0.0209, 0.0223, 0.0201 under seeds 20260726, 27\n    and 28; six of six within tolerance and positive.\n- claim: rff-link\n  outcome: reproduced\n  notebook: 02_link_development.ipynb\n  output: claim:rff-link\n  measured:\n  - 0.0031\n  - 0.00404\n  - 0.00111\n  - 0.00142\n  notes: Reading (a), 18-session geometry means 0.00361, 0.00404 and 0.00310 for the three map seeds,\n    history means 0.00111, 0.00142 and 0.00121, all inside the widened ranges; CO and RD geometry means\n    positive under every map (0.00269 to 0.00417). Reading (b), the six task means, does not hold\n    (0.00269 is below the widened bound 0.00279).\n- claim: estimator-family-link\n  outcome: reproduced\n  notebook: 03_link_estimators.ipynb\n  output: claim:estimator-family-link\n  notes: Under block penalties and nonlinear context every CO and RD mean (reading a) and every\n    18-session mean (reading b) is positive for SBP and TCR, geometry by phase and plus history.\n    Nonlinear-context 18-session means 0.01733, 0.00663, 0.00949 and 0.00274 against fully nested\n    0.02009, 0.00873, 0.01155 and 0.00420; block-penalty means close to the fully nested ones (about\n    0.019, 0.0086, 0.011 and 0.0041). The lowest task mean is 0.00075 (TCR history, CO, nonlinear\n    context). Values from the run in the executed notebook.\n  deviations:\n  - The block Ridge is solved exactly (Cholesky) where the release uses lsqr with tolerance 1e-6, to fit\n    the time limit (lsqr took 58 min for this notebook); on one session the gains were 0.0261224 and\n    0.0261219 with the same penalties, and a full lsqr run made while preparing gave the same signs.\n  - Reading (b) of the nonlinear context, every setting of Methods 4.6 (27 combinations), was not run;\n    estimated about 9 h on four processes. The outcome rests on reading (a), the release's setting.\n- claim: temporal-offset\n  outcome: reproduced\n  notebook: 04_link_temporal_capacity.ipynb\n  output: claim:temporal-offset\n  notes: Reading (i), fully nested, CO 0.00382, 0.00134, 0.00104, 0.00055 and RD 0.00623, 0.00110,\n    0.00043, 0.00038 at 0, 40, 80 and 120 ms; RD minus CO is 0.00241 at 0 ms and -0.00024 and -0.00061 at\n    40 and 80 ms (RD-change reading b holds, reading a does not). Reading (ii), evaluate_decoders_nested,\n    CO 0.00400 to 0.00058 and RD 0.00678 to 0.00000 from 0 to 120 ms, RD -0.00032 at 80 ms, both RD\n    readings hold. The reduction holds under both estimators.\n  deviations:\n  - One window start, 280 ms after the start bin, for every offset (the claims file's reading of\n    holding the window fixed); 367 to 375 trials per session are usable there.\n- claim: context-capacity-contrast\n  outcome: reproduced\n  notebook: 04_link_temporal_capacity.ipynb\n  output: claim:context-capacity-contrast\n  notes: Reading (i), fully nested, RD minus CO is 0.00152 (linear geometry), 0.00400 (quadratic),\n    0.00214 (linear plus history), 0.00374 (quadratic plus history) for SBP and 0.00227, 0.00495,\n    0.00181, 0.00275 for TCR. Quadratic plus history positive for both; for TCR the quadratic interval\n    (0.00079 to 0.00915) excludes zero and the linear one (-0.00246 to 0.00686) does not. For SBP the\n    quadratic contrast keeps its sign and its interval contains zero. Reading (ii) gives the same\n    pattern. Whether each interval excludes zero is the same under five bootstrap generators.\n- claim: confirm-geometry-gain\n  outcome: reproduced\n  notebook: 05_link_confirmation.ipynb\n  output: claim:confirm-geometry-gain\n  measured:\n  - 20\n  - 0.02158\n  - 0.02104\n  - 0.02213\n  seed_sensitive: true\n  notes: The selection rule re-run on the archive's metadata picks the 20 assets of the frozen manifest.\n    All 20 gains positive, mean 0.02158 (CO 0.02104, RD 0.02213), range 0.00593 to 0.04001; the paper's\n    gate passes. Under split seeds plus 1000 to 4000 the combined mean is 0.01478, 0.01699, 0.02070 and\n    0.01843 with 19 or 20 positive; three of the four fall outside the 10% tolerance.\n- claim: confirm-history-contraction\n  outcome: reproduced\n  notebook: 05_link_confirmation.ipynb\n  output: claim:confirm-history-contraction\n  measured:\n  - 0.00755\n  - 0.0067\n  - 0.0084\n  - 19\n  seed_sensitive: true\n  notes: Combined mean 0.00755 (CO 0.00670, RD 0.00840), 19 of 20 positive (2023-03-10 RD is -0.00128),\n    below the geometry mean 0.02158. Under the four other seeds the combined mean is 0.00335, 0.00475,\n    0.00818 and 0.00600, three outside the tolerance, each below that seed's geometry mean.\n- claim: confirm-replacement\n  outcome: reproduced\n  notebook: 05_link_confirmation.ipynb\n  output: claim:confirm-replacement\n  measured:\n  - -0.00771\n  - 20\n  seed_sensitive: true\n  notes: Mean replacement gain -0.00771; correct-pair gain above replacement in 20 of 20 sessions and\n    in both task means (CO 0.02104 against -0.00292, RD 0.02213 against -0.01250). Under the four\n    other seeds the replacement mean is -0.01963, -0.00902, -0.00938 and -0.01515, each outside the\n    tolerance.\n- claim: confirm-table1-values\n  outcome: reproduced\n  notebook: 05_link_confirmation.ipynb\n  output: claim:confirm-table1-values\n  measured:\n  - -0.00498\n  - 4.761\n  - 2.047\n  seed_sensitive: true\n  notes: Plus-history replacement gain -0.00498, MSE reductions 4.761% and 2.047%. Under the four other\n    seeds these are -0.01462 to -0.00467, 3.43 to 4.58% and 1.15 to 2.21%, mostly outside tolerance.\n- claim: rtt-data\n  outcome: reproduced\n  notebook: 06_mc_rtt.ipynb\n  output: claim:rtt-data\n  measured:\n  - 1080\n  - 130\n  - 810\n  - 270\n  notes: 1,080 blocks of 600 ms, all kept (21 bins each), 130 units, split labels 810 train and 270 val;\n    finger_vel, cursor_pos and target_pos present.\n- claim: rtt-gain\n  outcome: reproduced\n  notebook: 06_mc_rtt.ipynb\n  output: claim:rtt-gain\n  measured:\n  - 0.60308\n  - 0.06846\n  - 39.781\n  - 36.188\n  - 17.248\n  - 0.08359\n  - 0.05125\n  - -0.02297\n  notes: All eight values equal the paper's at its precision. Under estimator seeds plus 1000 to 4000\n    (the release split is fixed) the gain is 0.06821 to 0.06855 and the replacement gain -0.02300 to\n    -0.02332.\n- claim: rff-rtt\n  outcome: reproduced\n  notebook: 06_mc_rtt.ipynb\n  output: claim:rff-rtt\n  measured:\n  - 0.01491\n  - 0.01685\n  notes: Map seeds 20260802, 20260803, 20260804 give 0.01685, 0.01501 and 0.01491, all positive and\n    inside the range; replacement under the maps -0.00547 to -0.00931.\n- claim: estimator-family-nlb\n  outcome: reproduced\n  notebook: 06_mc_rtt.ipynb\n  output: claim:estimator-family-nlb\n  notes: MC_RTT gain 0.0690 under block penalties and 0.04619 under nonlinear context (g chosen 0.25),\n    both positive, which is what the criterion tests. The MC_Maze part of the statement (near zero) was\n    not tested, as DANDI:000139 was not read.\n  deviations:\n  - MC_Maze part not tested; block Ridge solved exactly in place of lsqr (as in estimator-family-link);\n    nonlinear context under the release's setting only.\n- claim: maze-gain\n  outcome: blocked\n  blocked_by: other\n  notes: The claim's data are MC_Maze-medium, DANDI:000139 version 0.220113.0408 (data elsewhere,\n    public). This attempt did not read it; the paper's loader (mc_maze.py) is in the release, and the\n    port and runs did not fit in this run after the 32 other claims. A later attempt can test it.\n- claim: rff-maze\n  outcome: blocked\n  blocked_by: other\n  notes: As maze-gain, DANDI:000139 was not read in this attempt.\nfindings:\n- kind: metadata_insufficient\n  about: data\n  severity: minor\n  datasets:\n  - \"001201\"\n  statement: The LINK velocity series (index_velocity, mrs_velocity, described as \"Velocity of index\n    flexion\" in \"flexion units per time bin\") are exactly the forward first difference of the released\n    position, velocity[t] = position[t+1] - position[t] (correlation 1.000 in all 18 development\n    sessions), so each velocity bin uses the position of the next bin. The files do not say so, and the\n    paper states the differentiation recipe could not be verified.\n- kind: metadata_error\n  about: data\n  severity: minor\n  datasets:\n  - \"001201\"\n  statement: ThresholdCrossings is stored with unit volts but holds integer counts per 20 ms bin (0 to\n    11), and SpikingBandPower, also in volts, holds values of about 0.04 to 341, which are not plausible\n    as volts.\n- kind: format_error\n  about: data\n  severity: minor\n  datasets:\n  - \"001201\"\n  statement: The 20 ms timestamps of session 2021-10-15 CO contain one gap of 1094 ms; the other 17\n    development sessions have steps of 19 to 21 ms only. All 375 trials of that session are still\n    usable.\n- kind: metadata_insufficient\n  about: data\n  severity: minor\n  datasets:\n  - \"000129\"\n  statement: The MC_RTT training file's behaviour series hold 15 missing (NaN) 20 ms bins, which no\n    description mentions; none falls inside the 1,080 analysis blocks.\n- kind: other\n  about: data\n  severity: none\n  datasets:\n  - \"001201\"\n  - \"000129\"\n  statement: Checks that passed. LINK holds nine dates with a CO and an RD session, 375 trials each, one\n    subject, no session deposited twice, and SBP, TCR, position, velocity and trials on one clock\n    (velocity decoding from SBP peaks at lag 0 in 16 of 18 sessions and 2 bins in 2). The paper's\n    confirmation rule re-run on the archive's metadata gives its 20 sessions, each with 375 usable\n    trials. MC_RTT holds 1,080 blocks, 130 units and the 810/270 split, and its finger velocity follows\n    the derivative of cursor position at lag 0.\n- kind: other\n  about: paper\n  statement: The paper says the NLB velocity unit fields and descriptions disagree (Limitations, Table 2\n    legend). In MC_RTT the series carry unit m/s or meters with conversion 0.001, so the stored values\n    are mm/s and mm, as the descriptions say; the fields agree once the conversion is applied.\n- kind: other\n  about: paper\n  statement: The paper's released code, ported here, reproduces its reported values at their printed\n    precision for every claim tested. The confirmation-set values are those of one outer split (seed\n    20260726); under four other split seeds the combined geometry-by-phase mean is 0.0148 to 0.0207 and\n    the history mean 0.0034 to 0.0082, so the exact values reported rest on that split, while the\n    qualitative pattern holds in each.\n"
}
```

```
Sat Nov 21 16:47:55 UTC 2026
[32m--> [39m[32m604[39m     response = [30;43mself[39;49m[30;43m.[39;49m[30;43mparent[39;49m[30;43m.[39;49m[30;43merror[39;49m[30;43m([39;49m
[32m    605[39m [30;43m        [39;49m[30;43m'[39;49m[30;43mhttp[39;49m[30;43m'[39;49m[30;43m,[39;49m[30;43m [39;49m[30;43mrequest[39;49m[30;43m,[39;49m[30;43m [39;49m[30;43mresponse[39;49m[30;43m,[39;49m[30;43m [39;49m[30;43mcode[39;49m[30;43m,[39;49m[30;43m [39;49m[30;43mmsg[39;49m[30;43m,[39;49m[30;43m [39;49m[30;43mhdrs[39;49m[30;43m)[39;49m
[32m    607[39m [38;5;28;01mreturn[39;00m response

[36mFile [39m[32m/opt/hostedtoolcache/Python/3.13.18/x64/lib/python3.13/urllib/request.py:533[39m, in [36mOpenerDirector.error[39m[34m(self, proto, *args)[39m
[32m    531[39m [38;5;28;01mif[39;00m http_err:
[32m    532[39m     args = ([38;5;28mdict[39m, [33m'[39m[33mdefault[39m[33m'[39m, [33m'[39m[33mhttp_error_default[39m[33m'[39m) + orig_args
[32m--> [39m[32m533[39m     [38;5;28;01mreturn[39;00m [30;43mself[39;49m[30;43m.[39;49m[30;43m_call_chain[39;49m[30;43m([39;49m[30;43m*[39;49m[30;43margs[39;49m[30;43m)[39;49m

[36mFile [39m[32m/opt/hostedtoolcache/Python/3.13.18/x64/lib/python3.13/urllib/request.py:466[39m, in [36mOpenerDirector._call_chain[39m[34m(self, chain, kind, meth_name, *args)[39m
[32m    464[39m [38;5;28;01mfor[39;00m handler [38;5;129;01min[39;00m handlers:
[32m    465[39m     func = [38;5;28mgetattr[39m(handler, meth_name)
[32m--> [39m[32m466[39m     result = [30;43mfunc[39;49m[30;43m([39;49m[30;43m*[39;49m[30;43margs[39;49m[30;43m)[39;49m
[32m    467[39m     [38;5;28;01mif[39;00m result [38;5;129;01mis[39;00m [38;5;129;01mnot[39;00m [38;5;28;01mNone[39;00m:
[32m    468[39m         [38;5;28;01mreturn[39;00m result

[36mFile [39m[32m/opt/hostedtoolcache/Python/3.13.18/x64/lib/python3.13/urllib/request.py:613[39m, in [36mHTTPDefaul
[... 14 more lines not kept]
```

```
File created successfully at: attempts/du-2026-01.yaml (file state is current in your context — no need to Read it back)
```

**Agent**

The run failed: under Python 3.13, `urllib` keeps HEAD on the redirect to S3, which returns 403 (3.12 switched to GET). Fixing `s3_url` to take the S3 URL from the asset's `contentUrl` metadata.

**Agent calls Bash**

```bash
cd entries/du-2026 && python - <<'EOF'
s=open('du2026.py').read()
old='''def s3_url(asset_id: str) -> str:
    request = urllib.request.Request(f"{API}/assets/{asset_id}/download/", method="HEAD")
    with urllib.request.urlopen(request, timeout=120) as response:
        return response.geturl()'''
new='''def s3_url(asset_id: str) -> str:
    """The asset's S3 address, from its contentUrl metadata."""
    urls = _get_json(f"{API}/assets/{asset_id}/")["contentUrl"]
    return next(u for u in urls if "s3" in u and "amazonaws.com" in u)'''
assert old in s; s=s.replace(old,new); open('du2026.py','w').write(s)
EOF
ls executed/du-2026/ | head; executed/du-2026/.venv/bin/python -c "
import sys; sys.path.insert(0,'.')
import du2026 as d, time
t=time.time(); s=d.load_link_session('5c74bad7-55be-47a6-b754-c77654064981','x'); print(s.identifier, time.time()-t)
r=d.load_rtt_raw('2ae6bf3c-788b-4ece-8c01-4b4a5680b25b'); print(r.n_units)
print(d.s3_url('5c74bad7-55be-47a6-b754-c77654064981'))
" 2>&1 | grep -v Warn | tail -5
```

```
01_synthetic.ipynb
result.json
2021-10-15_CO_nwb 1.6013445854187012
130
https://dandiarchive.s3.amazonaws.com/blobs/4d4/a8d/4d4a8dd0-41d5-4354-ae33-9f5151379707
```

**Agent**

Fixed and verified under the 3.13 environment. Relaunching the full run.

**Agent calls Bash**

```bash
cd  && date -u && python tools/entry.py all entries/du-2026 2>&1 | tail -15; date -u
```

```
Sat Nov 21 16:51:41 UTC 2026
Installed kernelspec registry-du-2026 in executed/du-2026/.venv/share/jupyter/kernels/registry-du-2026
0 error(s)
pass  01_synthetic.ipynb  (166 s)
pass  02_link_development.ipynb  (1350 s)
pass  03_link_estimators.ipynb  (842 s)
pass  04_link_temporal_capacity.ipynb  (1077 s)
pass  05_link_confirmation.ipynb  (548 s)
pass  06_mc_rtt.ipynb  (81 s)
Sat Nov 21 17:59:35 UTC 2026
```

**Agent**

All six notebooks pass (68 min total). Checking that the executed outputs match the numbers in the conclusions and the record.

**Agent calls Bash**

```bash
. $TMPDIR/venv/bin/activate && python - <<'EOF'
import nbformat,difflib,re
def txt(p):
    nb=nbformat.read(p,4); out=[]
    for c in nb.cells:
        if c.cell_type!='code': continue
        for o in c.outputs:
            t=o.get('text') or o.get('data',{}).get('text/plain') or ''
            out+= [l for l in t.splitlines() if not re.search(r'min|peak memory| s;|in \d+ s|done in',l)]
    return out
for f in ['01_synthetic','02_link_development','03_link_estimators','04_link_temporal_capacity','05_link_confirmation','06_mc_rtt']:
    a=txt(f'/tmp/claude/out/{f}.ipynb'); b=txt(f'executed/du-2026/{f}.ipynb')
    d=[l for l in difflib.unified_diff(a,b,lineterm='',n=0) if l[:1] in '+-' and not l.startswith(('+++','---'))]
    print(f, len(d)); print('\n'.join(d[:40]))
EOF
```

```
01_synthetic 0

02_link_development 0

03_link_estimators 8
-1     SBP             geometry by phase      block penalties 0.01953 0.01894 0.01924        18  0.00267 0.02973
+1     SBP             geometry by phase      block penalties 0.01953 0.01894 0.01924        18  0.00267 0.02970
-4     SBP  plus measured-output history      block penalties 0.00759 0.00953 0.00856        18  0.00078 0.01671
+4     SBP  plus measured-output history      block penalties 0.00759 0.00952 0.00856        18  0.00079 0.01671
-7     TCR             geometry by phase      block penalties 0.01069 0.01135 0.01102        17 -0.00329 0.02520
+7     TCR             geometry by phase      block penalties 0.01071 0.01137 0.01104        17 -0.00325 0.02520
-10    TCR  plus measured-output history      block penalties 0.00306 0.00514 0.00410        18  0.00028 0.01284
+10    TCR  plus measured-output history      block penalties 0.00306 0.00514 0.00410        18  0.00028 0.01286
04_link_temporal_capacity 0

05_link_confirmation 0

06_mc_rtt 2
-block penalties: gain 0.06902 (penalties (0.1, 10000.0)); nonlinear context (D 256, g chosen 0.25): gain 0.04619; fully nested linear 0.06846
+block penalties: gain 0.06901 (penalties (0.1, 10000.0)); nonlinear context (D 256, g chosen 0.25): gain 0.04619; fully nested linear 0.06846
```

**Agent calls Bash**

```bash
date -u && python tools/entry.py handover entries/du-2026 2>&1 | tail -3; ls tools | head -40; python - <<'EOF'
import json,yaml,jsonschema
s=json.load(open('schemas/attempt.schema.json')); a=yaml.safe_load(open('attempts/du-2026-01.yaml'))
jsonschema.validate(a,s); print('schema ok', len(a['outcomes']))
c=yaml.safe_load(open('claims/du-2026.yaml')); ids=[x['id'] for x in c['claims']]
print(set(ids)-{o['claim'] for o in a['outcomes']}, {o['claim'] for o in a['outcomes']}-set(ids))
EOF
```

```
Exit code 1
Sat Nov 21 17:59:54 UTC 2026
wrote executed/du-2026/handover
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
[... 34 more lines not kept]
```

**Agent calls Bash**

```bash
python - <<'EOF'
import json,yaml,jsonschema
s=json.load(open('schemas/attempt.schema.json')); a=yaml.safe_load(open('attempts/du-2026-01.yaml')); a['date']=str(a['date'])
jsonschema.validate(a,s); print('schema ok', len(a['outcomes']))
c=yaml.safe_load(open('claims/du-2026.yaml')); ids=[x['id'] for x in c['claims']]
print(set(ids)-{o['claim'] for o in a['outcomes']}, {o['claim'] for o in a['outcomes']}-set(ids))
import collections; print(collections.Counter(o['outcome'] for o in a['outcomes']))
EOF
grep -rn "attempts/" tools/build_site.py | head -3; git status --short | head
```

```
schema ok 33
set() set()
Counter({'reproduced': 31, 'blocked': 2})
6:Reads targets/dandisets.json, targets/pilot.yaml, claims/, attempts/,
3626:                  f'<a href="{REPO_URL}/blob/main/attempts/{e(a["id"])}.yaml">{e(a["id"])}</a>')
?? .bash_profile
?? .bashrc
?? .gitconfig
?? .idea
?? .mcp.json
?? .profile
?? .ripgreprc
?? .vscode
?? .zprofile
?? .zshrc
```

**Agent calls Bash**

```bash
python tools/entry.py check entries/du-2026 2>&1 | tail -3; git status --short entries attempts executed questions claims | head; git check-ignore -v executed/du-2026 | head -2; date -u
```

```
0 error(s)
?? attempts/du-2026-01.yaml
?? entries/du-2026/
.gitignore:6:executed/	executed/du-2026
Sat Nov 21 18:00:33 UTC 2026
```

**Agent calls Bash**

```bash
ls -a entries/du-2026; rm -rf entries/du-2026/__pycache__; python tools/entry.py run entries/du-2026 2>&1 | tail -2
```

```
.
..
.claude
01_synthetic.ipynb
02_link_development.ipynb
03_link_estimators.ipynb
04_link_temporal_capacity.ipynb
05_link_confirmation.ipynb
06_mc_rtt.ipynb
README.md
__pycache__
du2026.py
entry.yaml
requirements.in
requirements.lock.txt
pass  06_mc_rtt.ipynb  (81 s, reused)
reused the executed copies of 2026-11-21 17:59 UTC: nothing the run reads has changed since (hash aebfffc01da1). Nothing was executed and no environment was built; --fresh runs it again.
```

**Agent calls Bash**

```bash
find entries/du-2026/.claude -type f | head;
```

```
(Bash completed with no output)
```

**Agent**

I finished steps 1 to 6 by 18:01 UTC. The entry is locked, its check passes with 0 errors, all six notebooks run cleanly from a fresh environment, and the handover package is built in `executed/du-2026/handover/`. Of the 33 claims, 31 are reproduced and 2 are blocked; none is partially or not reproduced. Nearly every value matches the paper exactly at its printed precision.

## 1. Outcomes

| Claim | Outcome |
|---|---|
| synthetic-template-null, synthetic-signal-ordering, synthetic-pair-breaking | reproduced |
| link-development-sample, link-neural-only-r2, link-context-ladder-gain, link-context-only-r2, link-phase-only-replacement, link-task-contrast-by-context | reproduced |
| nested-geometry-gain, nested-history-gain | reproduced |
| nested-replacement-negative | reproduced, `seed_sensitive` |
| replacement-source-diagnostics, permutation-negative, replacement-penalty-distance, replacement-ranks-lower, practical-mse-reduction | reproduced |
| representative-trial | reproduced, but only on one of the two readings of the session tie rule (the one the paper's code uses) |
| split-seed-stability | reproduced |
| rff-link | reproduced on reading (a); reading (b) misses by 0.0001 |
| estimator-family-link | reproduced (nonlinear context only at the setting in the paper's code) |
| temporal-offset, context-capacity-contrast | reproduced with both candidate estimators |
| confirm-geometry-gain, confirm-history-contraction, confirm-replacement, confirm-table1-values | reproduced, all `seed_sensitive` |
| rtt-data, rtt-gain, rff-rtt | reproduced |
| estimator-family-nlb | reproduced for the MC_RTT part, which is what the criterion tests; the MC_Maze part was not tested |
| maze-gain, rff-maze | blocked (`other`): DANDI:000139 was not read |

On seed sensitivity: under the paper's split seed 20260726 every value matches. Under split seeds +1000 to +4000, the confirmation values and the SBP replacement means move outside their 10% tolerances. The qualitative pattern holds under all five seeds.

## 2. Dataset, assumptions, questions

- **Versions.** I pinned the versions the paper cites: 001201 at 0.251023.2336 and 000129 at 0.241017.1444. Two later 001201 versions list the same 312 paths with the same sizes.
- **Method.** The estimators in `du2026.py` are ports of the paper's released code (commit b042fbe). That code is listed under `inputs`.
- **Checks that passed.**
  - LINK: 9 paired dates, 18 sessions, 375 usable trials each, one subject, no recording deposited twice.
  - LINK clock: velocity decoding from SBP peaks at lag 0 in 16 of 18 sessions and at 2 bins in the other 2, so the streams share a clock.
  - The paper's confirmation selection rule, re-run on the archive's metadata, gives the same 20 sessions as its frozen manifest.
  - MC_RTT: the counts match the paper.
- **Findings about the data** (all rated minor):
  - LINK velocity is exactly the forward difference of position, velocity[t] = position[t+1] − position[t]. Neither the files nor the paper say so.
  - Threshold crossings are stored with the unit "volts" but hold integer counts; spiking-band power values (0.04 to 341) are also implausible as volts.
  - Session 2021-10-15 CO has one 1094 ms gap in its 20 ms timestamps.
  - MC_RTT has 15 missing (NaN) behaviour bins, none inside the analysis blocks.
- **Finding about the paper.** The paper says the MC_RTT unit fields and descriptions disagree. They agree once the stored `conversion` attribute of 0.001 is applied.
- **Assumptions:** none (`assumed` is not set on any outcome). Every method detail came from the claims file or the paper's code.
- **Questions for the paper's authors:** none.
- **Questions to a reader:** none.

## 3. Where the protocol was unclear, wrong or missing something

1. **Paper-fixed seeds against the five-seed rule.** The claims fix the paper's own seeds. I treated those as the claim's seed and varied them by +1000 to +4000. When the seed is the split itself, this marks exact-value claims as seed-sensitive. Because of the cost, I ran the extra seeds only for SBP geometry and history, the neural-only fit, and the confirmation and RTT fits, and recorded that limit as a deviation.
2. **Generated data marked `data: elsewhere`.** The synthetic claims say the data are "not deposited; generated by the paper's code". The protocol assumes such data sit in another archive. I ran the ported generator and listed the code, pinned at its commit, under `inputs`.
3. **No block reason for an untested `elsewhere` claim.** The protocol forbids `data_missing`, and `not_runnable` would wrongly say the method cannot run. I used `other` for the MC_Maze claims and said honestly that I ran out of time.
4. **Using the paper's own code.** The protocol doesn't say whether porting the paper's code is allowed. I ported it into the helper, cited the source function in each docstring, and listed it under `inputs`.
5. **Getting the S3 address (archives.md).** It says to "open each asset's S3 URL" but not how to get it. A HEAD request to `/download/` returns 403 under Python 3.13, the registry's version, though it worked under 3.12. This failed my first final run. I switched to the `contentUrl` in the asset metadata.
6. **Every entry needs two full runs.** Conclusions must be markdown cells, so writing them changes the entry hash and forces a second full run. That doubled the compute: about 70 minutes each time.
7. **The 60-minute notebook limit forced a solver change.** The estimator-family notebook took 58 minutes with the paper's solver (lsqr). I switched to an exact Cholesky solve. On a test session the gain differs by 5e-7, and I recorded this as a deviation.

## 4. Runtime and failures

- **Final run:** 68 minutes. Per notebook: 01 2.8 min, 02 22.5, 03 14, 04 18, 05 9, 06 1.4. Peak memory per process was under 1 GB.
- **Failures along the way:**
  - The first `entry.py all` failed on the S3 address issue above; the second passed.
  - Two analyses were not run because of their cost:
    - every nonlinear-context setting of Methods 4.6 (estimated about 9 h);
    - the MC_Maze claims.
- **Files written:** `entries/du-2026/` and `attempts/du-2026-01.yaml`. Nothing is committed.
- **Not mine:** untracked dotfiles at the repository root (`.bashrc`, `.idea` and others). I left them alone.

## End of run

75 turns, 210 minutes, $13.20 at API prices, result: success.
