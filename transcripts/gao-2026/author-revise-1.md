# 001683 · author-revise-1 · run 41630260889

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
date -u; cat transcripts/001683/verifier-1-report.md; ls entries/001683-gao-2026 entries/001683-gao-2026/*;
```

```
Tue Nov  3 11:50:59 UTC 2026
**A. Outcomes**

The claims file has 22 claims. The notebooks test 19 and treat 3 as blocked.

| Claim | My outcome | Reason |
|---|---|---|
| fig2c-sham-duration-stable | not_reproduced | The block main effect is significant under every reading: per rat, ordinary p=0.00145 and repeated p=3.9e-05; per seizure, p≤5e-24 with 12–13 significant post hoc tests (seizure_metrics cell 12). |
| fig2d-seizures-under-two-minutes | reproduced | 99.4% of ipsilateral and 99.2% of contralateral seizures last under 120 s (cell 15). |
| fig2e-sham-count-stable | reproduced | No main effect or post hoc test is significant under any reading (smallest p_family = 1), and the same holds for the BH635 variant. The mean count falls slightly, from 18.11 to 16.50 (cell 17). |
| fig2f-sham-percent-time-post3 | reproduced (fragile) | Under repeated measures, contralateral baseline against post 3 gives p_family 0.0209 (reading b of "sham"). Ordinary ANOVA gives nothing, and the label-following BH635 variant gives 0.083 (cell 19). |
| fig3a-count-reduction | reproduced | Under M4(b) all six decreases are within tolerance (8.7/36.4/41.9 and 10.5/41.4/42.4). Under repeated measures, baseline against post 1 and post 2 is significant in both hemispheres (p_family 0.0024–0.0085) (cell 23). |
| fig3a-count-sham-vs-tfus | partially_reproduced | Sham against tFUS at post 1 is significant in both hemispheres under ordinary ANOVA (0.035, 0.025), and sham is steady. Post 2 reaches p<0.05 only in the repeated reading (ipsilateral 0.0458), and that rests on a z reference (problem 1); the ordinary reading has the same statistic and gives p=0.057 (cells 23, 25). |
| fig3b-percent-time-reduction | reproduced | The decreases are within tolerance under both M4 readings. Under repeated measures all six comparisons against baseline are significant (p_family ≤0.0007) (cell 27). |
| fig3b-sham-percent-time-no-change | not_reproduced | Under repeated measures, sham baseline against post 2 
[... 55 more lines not kept]
```

**Agent calls Bash**

```bash
wc -l docs/protocol.md; grep -n "^#" docs/protocol.md
```

```
612 docs/protocol.md
1:# Protocol for an attempt
40:## Reader
42:### 1. Get the paper
53:### 2. Read the paper's code
63:### 3. Write the claims file
148:### 4. Data from outside the paper's own recordings
156:### 5. Check
169:### 6. Answer questions
182:## Author
198:### 1. Establish what can be tested
325:### 2. Check the data against its description
340:### 3. Write the entry
398:### 4. Lock, check and run
409:### 5. Record the attempt
460:### 6. Hand over for verification
498:## Repeat attempts
540:## Local and remote datasets
563:## Verifier
567:### Round 1: without the author's conclusions
[... 2 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 1,40p docs/protocol.md; sed -n 182,612p docs/protocol.md
```

```
# Protocol for an attempt

Version: `pilot-13`. Record this version in the attempt's provenance.

This is what agents, or people, do to attempt a target and deposit the
result. A target is a dataset in a public archive and a paper it names. How
each archive's datasets are named, versioned and read is in
[archives.md](archives.md); the examples here are from DANDI, the first. It is written from the pilot attempts
([pilot notes](pilot-notes.md)); the reasons for the rules are there.

An attempt has three roles, each a separate run with a separate context:

- The **reader** reads the paper and writes the claims file: every finding,
  and how each is to be tested, taken from the paper. A second reader checks
  it against the paper. Readers never see the dataset's data.
- The **author** tests the claims on the dataset. It reads the paper to
  understand the claims, but the claims file binds it: it cannot change a
  claim's statement, expected values or criterion. A method detail the file
  lacks it takes from the paper, citing the passage, and it asks a reader
  only when it believes the file misreads the paper.
[... 451 more lines not kept]
```

**Agent calls Bash**

```bash
ls attempts | grep 001683; cat attempts/001683-gao-2026-01.yaml; ls questions | grep 001683; ls claims 2>/dev/null | grep 001683
```

```
001683-gao-2026-01.yaml
schema_version: 2
id: 001683-gao-2026-01
dataset:
  archive: dandi
  id: "001683"
  version: 0.260109.2104
  doi: 10.48324/dandi.001683/0.260109.2104
paper: doi:10.1109/tnsre.2025.3644273
date: 2026-11-03
entry: 001683-gao-2026
provenance:
  kind: agent
  accountable:
    name: CatalystNeuro
  agent:
    harness: Claude Code
    model: claude-opus-5-5
    protocol: pilot-13
  runner:
[... 369 more lines not kept]
```

**Agent calls Bash**

```bash
ls claims/ | head; find . -path ./node_modules -prune -o -name "*001683*" -print | grep -v executed | head -30; wc -l entries/001683-gao-2026/tfus.py; cat questions/001683.yaml | head -80
```

```
000003
000004
000005
000006
000008
000009
000010
000011
000013
000015
./attempts/001683-gao-2026-01.yaml
./entries/001683-gao-2026
./claims/001683
./papers/match/001683.yaml
./.git/logs/refs/heads/attempt/001683
./.git/logs/refs/remotes/origin/attempt/001683
./.git/refs/heads/attempt/001683
./.git/refs/remotes/origin/attempt/001683
./transcripts/001683
535 entries/001683-gao-2026/tfus.py
[... 1 more lines not kept]
```

**Agent calls Bash**

```bash
ls claims/001683 transcripts/001683 questions | head -40; wc -c claims/001683/*
```

```
claims/001683:
10.1109-tnsre.2025.3644273.yaml

questions:
000005.yaml
000006.yaml
000008.yaml
000009.yaml
000010.yaml
000011.yaml
000013.yaml
000015.yaml
000019.yaml
000023.yaml
000036.yaml
000037.yaml
000045.yaml
000061.yaml
000115.yaml
000128.yaml
[... 21 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "claims/001683/10.1109-tnsre.2025.3644273.yaml"
}
```

```
1	# Claims for Gao, Frake, Durand and He (2026), "Transcranial Focused Ultrasound Stimulation
2	# Targeting White Matter Inhibits Seizures in a Rat Model of Epilepsy", IEEE Trans Neural Syst
3	# Rehabil Eng 34, doi:10.1109/tnsre.2025.3644273, on dandiset 001683 (same title on the archive;
4	# its description says the dataset is described in this paper).
5	# Written by an agent (model "claude-opus-5-5", Claude Code in GitHub Actions), 2026-10-21,
6	# protocol as stated in docs/protocol.md (version pilot-10).
7	#
8	# Text read: the NIH author manuscript (PMC12848950) as served by Europe PMC, stored under paper/:
9	# abstract, Introduction, Methods, Results, Discussion, Data Availability and the legends of Figs. 1
10	# to 6; and the supplement (supp1-3644273.pdf, 8 pages: ex-vivo scanning, target confirmation, Figs.
11	# S1 to S7). There is no PDF of the main paper, so values and significance marks drawn only inside
12	# Figs. 2 to 6 were not read; Figs. S4, S5 and S7 were viewed in the supplement PDF. The paper links
13	# no code; the only repository it names is the dandiset. No code was read.
14	#
15	# Data the paper used, as it reports them (Methods A to E, supplement):
16	#  - Rats. 16 adult male Sprague-Dawley rats in the epilepsy study, 10 tFUS (experimental) and 6
17	#    sham; 7 more in a mechanism study, 23 in all. The wild-type analysis (Fig. 5) uses all 23
18	#    (Fig. 5B, N = 23 per group). Isoflurane anesthesia throughout.
19	#  - Recordings. A 32-channel skull EEG probe (NeuroNexus HC32), aligned with bregma, and a
20	#    64-channel intracranial array in left S1 (AP -2, ML -2.5, DV -1.5 mm). Tucker-Davis system at
[... 565 more lines not kept]
```

**Agent calls Bash**

```bash
grep -n -i "absence" docs/protocol.md docs/*.md | head -20
```

```
docs/protocol.md:131:   - For a claim of absence ("no difference", "did not change"), the
docs/protocol.md:135:     several readings does not apply: absence is judged on the paper's test
docs/pilot-notes.md:38:- **Claims of absence** are judged by the paper's own test (000147 point 5).
docs/pilot-notes.md:70:- **Claims of absence are judged on the paper's test alone**, outside the
docs/pilot-notes.md:134:  after it; absence claims judged on the paper's test as written; the first
docs/protocol.md:131:   - For a claim of absence ("no difference", "did not change"), the
docs/protocol.md:135:     several readings does not apply: absence is judged on the paper's test
```

**Agent calls Bash**

```bash
sed -n 100,147p docs/protocol.md
```

```
- `expected`: each reported number the claim rests on, with a tolerance.
     Use the paper's own uncertainty when it gives one (a confidence
     interval, or the stated spread); otherwise 10% of the reported value.
     For a reported range ("2 to 13%"), the claim holds inside the range
     widened by 10% of each bound. Give the reason for any other tolerance.
   - `criterion`: how the claim will be judged, for any claim that is not
     settled by its expected values alone ("similar", "many", "tended to").
     It is written from the paper alone, before anyone analyses the data.
   - When a reported number can be read in more than one way (which trials
     form the denominator, which subset is meant), list in the criterion the
     readings the paper's text plausibly allows, before the analysis. The
     claim is reproduced if the result matches under any of them. The
     notebook shows every reading, the notes say which ones match, and the
     ambiguity is recorded as a deviation.
   - Methods come from the paper, never from the author. Every part of a
     criterion's method (the selection, the measure, the test, windows,
     bins, thresholds, what a measure is compared with) is taken from the
     Methods, the figure legends, the supplement, or the code the paper
     links, and the criterion says which. Search all of them before
     treating a detail as open.
[... 27 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/001683-gao-2026; cat tfus.py; cat entry.yaml README.md; ls ../../executed/001683-gao-2026/ 2>/dev/null
```

```
Exit code 2
"""Loading and measures for dandiset 001683 (Gao, Frake, Durand and He 2026, IEEE TNSRE,
doi:10.1109/tnsre.2025.3644273): EEG and seizure labels of 16 rats with 4-AP seizures, and the
evoked-potential (LFP) and EEG recordings of the wild-type phase of 23 rats.

The files are streamed from the archive at the pinned version; nothing is written to disk. Every
ElectricalSeries in this dandiset is stored contiguous (not chunked) as float64, time by channel,
so reading any channel means reading whole rows. `read_rows` therefore fetches the byte range of
a block of rows with parallel HTTP range requests, which is several times faster than h5py over
remfile; `check_read` compares it with h5py on a slice.

Where the parameters come from:

- RATE, the sampling rate, is the files' own (3051.7578125 Hz; Methods C, "3051.8 Hz").
- Seizure labels are the files' `intervals` table, one row per seizure and hemisphere, tagged
  ipsilateral or contralateral (claims file, M1: the paper's labels are used when the dandiset
  holds them). Their times are in minutes, not the seconds NWB prescribes: the stops reach
  about 62.5 in blocks of 3752 s, and the notebook checks this against the EEG. `MINUTES` converts.
- Seizure metrics follow M2 of the claims file (Methods C): duration leaves out seizures that
  start at the first sample or end at the last; percent time is summed durations over the block
[... 158 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "entries/001683-gao-2026/tfus.py",
 "offset": 90,
 "limit": 420
}
```

```
90	        page = _session.get(url).json()
91	        rows += [{"path": a["path"], "asset_id": a["asset_id"], "size": a["size"]} for a in page["results"]]
92	        url = page.get("next")
93	    return pd.DataFrame(rows)
94	
95	
96	def version_info() -> dict:
97	    return _session.get(f"{API}/dandisets/{DANDISET_ID}/versions/{DANDISET_VERSION}/info/").json()
98	
99	
100	def s3_url(asset_id: str) -> str:
101	    return _session.head(f"{API}/assets/{asset_id}/download/", allow_redirects=True).url
102	
103	
104	def _text(x):
105	    if isinstance(x, np.ndarray):
106	        x = x[0] if x.shape else x[()]
107	    return x.decode() if isinstance(x, bytes) else str(x)
108	
109	
[... 400 more lines not kept]
```

**Agent calls Bash**

```bash
ls executed/ 2>/dev/null | head; cd entries/001683-gao-2026; python - <<'EOF'
import json
for nb in ["seizure_metrics.ipynb","eeg_blocks.ipynb","wild_type.ipynb"]:
    d=json.load(open(nb))
    print("=====",nb,len(d["cells"]))
    for i,c in enumerate(d["cells"]):
        src="".join(c["source"])
        print(f"--- [{i}] {c['cell_type']} tags={c.get('metadata',{}).get('tags')} len={len(src)}")
        print(src[:300])
EOF
```

```
<persisted-output>
Output too large (34.2KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/00380fd7-6c6d-47a7-8b37-9f3cd67d736a/tool-results/bvvd2ikkj.txt

Preview (first 2KB):
===== seizure_metrics.ipynb 53
--- [0] markdown tags=None len=1851
# Gao et al. (2026) on dandiset 001683: seizure metrics from the labels

Paper. Gao H, Frake A, Durand DM, He B (2026). Transcranial focused ultrasound stimulation
targeting white matter inhibits seizures in a rat model of epilepsy. *IEEE Trans Neural Syst Rehabil
Eng* 34, 251-259. [doi:10.1109/tnsr
--- [1] code tags=None len=931
import hashlib
import time
import warnings

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy import stats
[... 32 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/00380fd7-6c6d-47a7-8b37-9f3cd67d736a/tool-results/bvvd2ikkj.txt"
}
```

```
1	===== seizure_metrics.ipynb 53
2	--- [0] markdown tags=None len=1851
3	# Gao et al. (2026) on dandiset 001683: seizure metrics from the labels
4	
5	Paper. Gao H, Frake A, Durand DM, He B (2026). Transcranial focused ultrasound stimulation
6	targeting white matter inhibits seizures in a rat model of epilepsy. *IEEE Trans Neural Syst Rehabil
7	Eng* 34, 251-259. [doi:10.1109/tnsr
8	--- [1] code tags=None len=931
9	import hashlib
10	import time
11	import warnings
12	
13	import matplotlib.pyplot as plt
14	import numpy as np
15	import pandas as pd
16	from scipy import stats
17	
18	import tfus
19	
20	warnings.filterwarnings("ignore")
[... 686 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/001683-gao-2026; sed -n 60,90p tfus.py; cat requirements.in; python -c "import statsmodels, scipy; print(statsmodels.__version__, scipy.__version__)"
```

```
Exit code 1
/bin/bash: line 1: cd: entries/001683-gao-2026: No such file or directory
import remfile
import requests
from scipy import signal

DANDISET_ID = "001683"
DANDISET_VERSION = "0.260109.2104"
API = "https://api.dandiarchive.org/api"

RATE = 3051.7578125
N_EEG = 32
IPSI_CH, CONTRA_CH = 8, 25                 # 1-based channel numbers (Fig. S1 drawing)
S1_IPSI, S1_CONTRA = (7, 8, 10, 12), (21, 23, 25, 26)
NONS1_IPSI = tuple(c for c in range(1, 17) if c not in S1_IPSI)
NONS1_CONTRA = tuple(c for c in range(17, 33) if c not in S1_CONTRA)
BANDS = {"theta": (5.0, 8.0), "alpha": (8.0, 12.0), "beta": (12.0, 30.0), "gamma": (30.0, 80.0)}
BLOCKS = ["baseline", "condition", "post1", "post2", "post3"]
MINUTES = 60.0                             # the label table's unit, in seconds
WELCH_S = 2.0
[... 27 more lines not kept]
```

**Agent calls Bash**

```bash
cd  ls -a; grep -n "venv\|def cmd_\|uv " tools/entry.py | head -40
```

```
.
..
.bash_profile
.bashrc
.claude
.env
.env.development
.env.development.local
.env.local
.env.production
.env.production.local
.env.test
.env.test.local
.git
.gitconfig
.github
.gitignore
.gitmodules
.idea
.mcp.json
[... 39 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 330,380p tools/entry.py; grep -n "PYTHON_VERSION =" tools/entry.py
```

```
# --- lock and run -------------------------------------------------------------

def lock(entry_dir: Path) -> int:
    r = subprocess.run(["uv", "pip", "compile", "--quiet", "--python-version", PYTHON_VERSION,
                        "requirements.in", "-o", "requirements.lock.txt"], cwd=entry_dir)
    if r.returncode == 0:
        print(f"wrote {(entry_dir / 'requirements.lock.txt').relative_to(ROOT)}")
    return r.returncode


def run(entry_dir: Path, output_dir: Path, timeout: int, max_minutes: float) -> int:
    entry = yaml.safe_load((entry_dir / "entry.yaml").read_text())
    output_dir.mkdir(parents=True, exist_ok=True)
    venv = (output_dir / ".venv").resolve()
    python = venv / "bin" / "python"
    # A kernel of the entry's own environment, under a name no other kernel on the machine has, so
    # nbconvert cannot pick up some other "python3" kernel (a user's or a conda install's).
    kernel = f"registry-{entry_dir.name}"
    for cmd in (["uv", "venv", "--quiet", "--clear", "--python", PYTHON_VERSION, str(venv)],
                ["uv", "pip", "install", "--quiet", "--python", str(python),
[... 30 more lines not kept]
```

**Agent**

Build a dev environment from the lock file for developing on subsets.

**Agent calls Bash**

```bash
cd  uv venv --quiet --python 3.13 $TMPDIR/venv && uv pip install --quiet --python $TMPDIR/venv/bin/python -r entries/001683-gao-2026/requirements.lock.txt && $TMPDIR/venv/bin/python -c "import statsmodels; print(statsmodels.__version__)"
```

```
0.15.0
```

**Agent**

Now the Satterthwaite rewrite of the repeated-measures reading in `twoway`.

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "entries/001683-gao-2026/tfus.py",
 "old_string": "    else:\n        with warnings.catch_warnings():\n            warnings.simplefilter(\"ignore\")              # boundary fits (zero rat variance) are expected\n            res = smf.mixedlm(formula, d, groups=d[subject]).fit(reml=True)\n        names = list(res.fe_params.index)\n        beta = res.fe_params.to_numpy()\n        V = res.cov_params().loc[names, names].to_numpy()\n        rows = []\n        for term in (f\"C({a}, Sum)\", f\"C({b}, Sum)\", f\"C({a}, Sum):C({b}, Sum)\"):\n            if \":\" in term:\n                idx = [i for i, n in enumerate(names) if \":\" in n]\n            else:\n                idx = [i for i, n in enumerate(names) if n.startswith(term + \"[\") and \":\" not in n]\n            if not idx:\n                continue\n            bb, VV = beta[idx], V[np.ix_(idx, idx)]\n            chi = float(bb @ np.linalg.pinv(VV) @ bb)\n            rows.append({\"term\": term, \"F\": chi / len(idx), \"p\": stats.chi2.sf(chi, len(idx))})\n        table = pd.DataFrame(rows).set_index(\"term\")\n        dof = None\n    out = []\n    for name, c1, c2, fam in comparisons:\n        x1 = _contrast_rows(di, pd.DataFrame([c1]))[0][: len(beta)]\n        x2 = _contrast_rows(di, pd.DataFrame([c2]))[0][: len(beta)]\n        c = x1 - x2\n        est, se = float(c @ beta), float(np.sqrt(c @ V @ c))\n        stat = est / se if se > 0 else np.nan\n        p = 2 * (stats.t.sf(abs(stat), dof) if dof is not None else stats.norm.sf(abs(stat)))\n        n1 = int(((d[a] == c1[a]) & (d[b] == c1[b])).sum())\n        n2 = int(((d[a] == c2[a]) & (d[b] == c2[b])).sum())\n        out.append({\"comparison\": name, \"family\": fam, \"diff\": est, \"stat\": stat, \"p_raw\": p, \"n1\": n1, \"n2\": n2})",
 "new_string": "    else:\n        with warnings.catch_warnings():\n            warnings.simplefilter(\"ignore\")              # boundary fits (zero rat variance) are expected\n            res = smf.mixedlm(formula, d, groups=d[subject]).fit(reml=True)\n        names = list(res.fe_params.index)\n        sat = _Satterthwaite(np.asarray(res.model.exog), d[subject].to_numpy(),\n                             float(res.scale), float(np.asarray(res.cov_re)[0, 0]))\n        beta = res.fe_params.to_numpy()\n        V = sat.V\n        rows = []\n        for term in (f\"C({a}, Sum)\", f\"C({b}, Sum)\", f\"C({a}, Sum):C({b}, Sum)\"):\n            if \":\" in term:\n                idx = [i for i, n in enumerate(names) if \":\" in n]\n            else:\n                idx = [i for i, n in enumerate(names) if n.startswith(term + \"[\") and \":\" not in n]\n            if not idx:\n                continue\n            L = np.eye(len(beta))[idx]\n            Fv, ddf = sat.ftest(L, beta)\n            rows.append({\"term\": term, \"F\": Fv, \"df_den\": ddf, \"p\": stats.f.sf(Fv, len(idx), ddf)})\n        table = pd.DataFrame(rows).set_index(\"term\")\n    out = []\n    for name, c1, c2, fam in comparisons:\n        x1 = _contrast_rows(di, pd.DataFrame([c1]))[0][: len(beta)]\n        x2 = _contrast_rows(di, pd.DataFrame([c2]))[0][: len(beta)]\n        c = x1 - x2\n        est, se = float(c @ beta), float(np.sqrt(c @ V @ c))\n        stat = est / se if se > 0 else np.nan\n        df_c = sat.df(c) if rm else dof\n        p = 2 * stats.t.sf(abs(stat), df_c)\n        n1 = int(((d[a] == c1[a]) & (d[b] == c1[b])).sum())\n        n2 = int(((d[a] == c2[a]) & (d[b] == c2[b])).sum())\n        out.append({\"comparison\": name, \"family\": fam, \"diff\": est, \"stat\": stat, \"df\": df_c, \"p_raw\": p,\n                    \"n1\": n1, \"n2\": n2})"
}
```

```
The file entries/001683-gao-2026/tfus.py has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "entries/001683-gao-2026/tfus.py",
 "old_string": "def twoway(df: pd.DataFrame,",
 "new_string": "class _Satterthwaite:\n    \"\"\"Satterthwaite degrees of freedom for contrasts of a random-intercept mixed model (the method of\n    SAS PROC MIXED and of lmerTest; Prism's repeated-measures and mixed-effects analyses report t and F\n    on finite df, not z). Variance parameters theta = (residual, subject intercept); their asymptotic\n    covariance is the inverse of the REML information, 0.5 tr(P S_i P S_j).\"\"\"\n\n    def __init__(self, X: np.ndarray, groups: np.ndarray, s2e: float, s2s: float):\n        Z = (groups[:, None] == np.unique(groups)[None, :]).astype(float)\n        self.S = [np.eye(len(X)), Z @ Z.T]\n        Si = np.linalg.inv(s2e * self.S[0] + s2s * self.S[1])\n        self.V = np.linalg.inv(X.T @ Si @ X)\n        P = Si - Si @ X @ self.V @ X.T @ Si\n        PS = [P @ s for s in self.S]\n        info = 0.5 * np.array([[np.trace(PS[i] @ PS[j]) for j in range(2)] for i in range(2)])\n        self.A = np.linalg.pinv(info)\n        Q = X.T @ Si\n        self.dV = [-self.V @ Q @ s @ Q.T @ self.V for s in self.S]\n        self.df_max = len(X) - np.linalg.matrix_rank(X)\n\n    def df(self, c: np.ndarray) -> float:\n        var = float(c @ self.V @ c)\n        g = np.array([float(c @ dv @ c) for dv in self.dV])\n        den = float(g @ self.A @ g)\n        return float(np.clip(2 * var ** 2 / den, 1.0, self.df_max)) if den > 0 else float(self.df_max)\n\n    def ftest(self, L: np.ndarray, beta: np.ndarray) -> tuple[float, float]:\n        \"\"\"F statistic and denominator df of H0: L beta = 0 (lmerTest's eigen-decomposition method).\"\"\"\n        VL = L @ self.V @ L.T\n        Lb = L @ beta\n        k = len(L)\n        F = float(Lb @ np.linalg.pinv(VL) @ Lb) / k\n        w, U = np.linalg.eigh(VL)\n        nus = [self.df(U[:, m] @ L) for m in range(k)]\n        E = sum(nu / (nu - 2) for nu in nus if nu > 2)\n        ddf = 2 * E / (E - k) if E > k else min(nus)\n        return F, float(ddf)\n\n\ndef twoway(df: pd.DataFrame,"
}
```

```
The file entries/001683-gao-2026/tfus.py has been updated successfully.
```

**Agent calls Bash**

```bash
cd entries/001683-gao-2026; $TMPDIR/venv/bin/python - <<'EOF'
import numpy as np, pandas as pd, tfus
rng=np.random.default_rng(1)
rows=[]
for s in range(16):
    g="sham" if s<6 else "tFUS"; u=rng.normal(0,2)
    for b in ["baseline","condition","post1","post2"]:
        rows.append(dict(subject=f"r{s}",group=g,block=b,y=10+u+rng.normal(0,1)+(b=="post1")*(g=="tFUS")*1.5))
d=pd.DataFrame(rows)
for rm in (False,True):
    t,p=tfus.group_block_tests(d,"y")["repeated" if rm else "ordinary"]
    print(t); print(p[["comparison","stat","df","p_raw"]].round(4).to_string())
# classical split-plot
import statsmodels.formula.api as smf
EOF
```

```
F         p
C(group, Sum)                2.798283  0.099944
C(block, Sum)                0.666890  0.575915
C(group, Sum):C(block, Sum)  0.618925  0.605665
                comparison    stat    df   p_raw
0  sham baseline-condition -0.0436  56.0  0.9654
1      sham baseline-post1  0.1415  56.0  0.8880
2      sham baseline-post2  0.3205  56.0  0.7498
3  tFUS baseline-condition  0.2120  56.0  0.8329
4      tFUS baseline-post1 -1.5484  56.0  0.1272
5      tFUS baseline-post2 -0.4742  56.0  0.6372
6       sham-tFUS baseline -0.3274  56.0  0.7446
7      sham-tFUS condition -0.0951  56.0  0.9246
8          sham-tFUS post1 -1.8266  56.0  0.0731
9          sham-tFUS post2 -1.0964  56.0  0.2776
                                    F  df_den         p
term                                                   
C(group, Sum)                0.798107    14.0  0.386760
C(block, Sum)                2.262857    42.0  0.095101
C(group, Sum):C(block, Sum)  3.760850    42.0  0.017663
[... 11 more lines not kept]
```

**Agent**

Exact split-plot dfs (42 within, 14 group, Satterthwaite 18.1 between at a block) come out as expected. Updating the docstrings, then `timepoint_tests` and `wild_pli`.

**Agent calls Bash**

```bash
cd entries/001683-gao-2026; $TMPDIR/venv/bin/python - <<'EOF'
import re
s=open("tfus.py").read()
old="""    t on the pooled residual error and its df. rm=True: mixed model with a random intercept per subject;
    main effects and interaction by Wald tests, post hoc by Wald z of the contrast.
    \"\"\""""
new="""    t on the pooled residual error and its df. rm=True: mixed model with a random intercept per subject
    (REML); main effects and interaction by F tests and post hoc by t tests of the contrasts, each on
    Satterthwaite degrees of freedom (`_Satterthwaite`). On balanced data these are the df of the
    classical split-plot ANOVA: (rats - groups)(blocks - 1) within rats, and for groups compared at one
    block the Satterthwaite pooling of the rat and residual mean squares, as Prism does.
    \"\"\""""
assert old in s; s=s.replace(old,new)
old2="""  Prism does) and the repeated-measures reading (a linear mixed model with a random intercept per
  rat, Prism's mixed-effects analysis, with Wald tests of contrasts)."""
new2="""  Prism does) and the repeated-measures reading (a linear mixed model with a random intercept per
  rat, Prism's mixed-effects analysis, with t and F tests of contrasts on Satterthwaite df; an
  earlier version used normal and chi-squared references, which understate p with 6 to 16 rats)."""
assert old2 in s; s=s.replace(old2,new2)
open("tfus.py","w").write(s)
EOF
```

```
(Bash completed with no output)
```

**Agent calls Bash**

```bash
cd entries/001683-gao-2026; $TMPDIR/venv/bin/python - <<'EOF'
s=open("tfus.py").read()
i=s.index("def timepoint_tests"); j=s.index("def wild_pli")
new='''def timepoint_tests(a: np.ndarray, b: np.ndarray) -> pd.DataFrame:
    """tFUS against sham at each time point, a and b of shape (rats, time), the same rats in both.

    Both readings are the group by time point two-way ANOVA of Methods F, with Bonferroni-corrected post
    hoc t tests of tFUS against sham at each time point. Ordinary reading: the post hoc t uses the pooled
    residual mean square of the full model and its df. Repeated reading: the same rats give both groups,
    so the model adds a random intercept per rat (Prism's repeated-measures analysis with pooled error,
    as in `twoway`); with balanced data the rat effect leaves the contrasts' estimate unchanged and
    removes the rat variance from the error, df 2nT - 2T - (n - 1). (An earlier version used a paired t
    per time point, which the claims-file check had replaced with this ANOVA.)"""
    from scipy import stats
    n, T = a.shape
    resid = np.concatenate([a - a.mean(0), b - b.mean(0)])
    df_res = 2 * n * T - 2 * T
    mse = (resid ** 2).sum() / df_res
    diff = a.mean(0) - b.mean(0)
    t_ord = diff / np.sqrt(mse * 2 / n)
    p_ord = 2 * stats.t.sf(np.abs(t_ord), df_res)
    rat = np.concatenate([a, b], axis=1).mean(1)                  # each rat's mean over both groups
    resid_rm = resid - np.concatenate([rat - rat.mean()] * 2)[:, None]
    df_rm = df_res - (n - 1)
    mse_rm = (resid_rm ** 2).sum() / df_rm
    t_rm = diff / np.sqrt(mse_rm * 2 / n)
    p_rm = 2 * stats.t.sf(np.abs(t_rm), df_rm)
    return pd.DataFrame({"diff": diff, "p_ordinary": np.minimum(1, p_ord * T), "p_repeated": np.minimum(1, p_rm * T)})


'''
s=s[:i]+new+s[j:]
open("tfus.py","w").write(s)
EOF
$TMPDIR/venv/bin/python - <<'EOF'
import numpy as np, tfus
rng=np.random.default_rng(0); n,T=23,50
u=rng.normal(0,3,(n,1))
a=u+rng.normal(0,1,(n,T)); b=u+rng.normal(0,1,(n,T)); a[:,10]+=1.5
r=tfus.timepoint_tests(a,b); print(r.iloc[8:12])
EOF
```

```
diff  p_ordinary    p_repeated
8  -0.267438    1.000000  1.000000e+00
9  -0.313693    1.000000  1.000000e+00
10  2.109562    0.603079  7.023309e-11
11 -0.696611    1.000000  9.357452e-01
```

**Agent calls Bash**

```bash
cd entries/001683-gao-2026; grep -n "def wild_pli" -A 40 tfus.py | tail -12
```

```
577-    windows = {"pre": (-n0, 0), "tfus": (0, w20), "post": (w20, n1)}
578-    out = {"n_trials": len(idx)}
579-    for band in BANDS:
580-        ph = np.angle(signal.hilbert(signal.sosfiltfilt(band_sos(band, RATE), x, axis=0), axis=0))
581-        res = {}
582-        for name, (a, b) in windows.items():
583-            seg = np.stack([ph[i + a:i + b] for i in idx])            # trials, samples, channels
584-            d = np.sin(seg[:, :, ii][:, :, :, None] - seg[:, :, cc][:, :, None, :])
585-            s = np.sign(d)
586-            res[name] = {"per_trial": np.abs(s.mean(axis=1)).mean(axis=0), "concat": np.abs(s.mean(axis=(0, 1)))}
587-        out[band] = res
588-    return out
```

**Agent calls Bash**

```bash
cd entries/001683-gao-2026; $TMPDIR/venv/bin/python - <<'EOF'
s=open("tfus.py").read()
old='''    windows = {"pre": (-n0, 0), "tfus": (0, w20), "post": (w20, n1)}
    out = {"n_trials": len(idx)}
    for band in BANDS:
        ph = np.angle(signal.hilbert(signal.sosfiltfilt(band_sos(band, RATE), x, axis=0), axis=0))
        res = {}
        for name, (a, b) in windows.items():
            seg = np.stack([ph[i + a:i + b] for i in idx])            # trials, samples, channels
            d = np.sin(seg[:, :, ii][:, :, :, None] - seg[:, :, cc][:, :, None, :])
            s = np.sign(d)
            res[name] = {"per_trial": np.abs(s.mean(axis=1)).mean(axis=0), "concat": np.abs(s.mean(axis=(0, 1)))}
        out[band] = res
    return out'''
new='''    windows = {"pre": [(-n0, 0)], "tfus": [(0, w20)], "post_full": [(w20, n1)],
               "post": [(w20 + k * w20, w20 + (k + 1) * w20) for k in range((n1 - w20) // w20)]}
    out = {"n_trials": len(idx)}

    def one(seg_i, seg_c):
        s = np.sign(np.sin(seg_i[:, :, :, None] - seg_c[:, :, None, :]))
        return np.abs(s.mean(axis=1)).mean(axis=0), np.abs(s.mean(axis=(0, 1)))

    for band in BANDS:
        ph = np.angle(signal.hilbert(signal.sosfiltfilt(band_sos(band, RATE), x, axis=0), axis=0))
        res = {}
        for name, spans in windows.items():
            acc = {"per_trial": [], "concat": [], "per_trial_shuffled": [], "concat_shuffled": []}
            for a, b in spans:
                seg = np.stack([ph[i + a:i + b] for i in idx])        # trials, samples, channels
                pt, ct = one(seg[:, :, ii], seg[:, :, cc])
                ps, cs = one(seg[:, :, ii], np.roll(seg[:, :, cc], 1, axis=0))
                for k, v in zip(acc, (pt, ct, ps, cs)):
                    acc[k].append(v)
            res[name] = {k: np.mean(v, axis=0) for k, v in acc.items()}
        out[band] = res
    return out'''
assert old in s; s=s.replace(old,new)
old='''    interval table: per trial and averaged (reading a) and over the concatenated trial samples (reading b).'''
new='''    interval table: per trial and averaged (reading a) and over the concatenated trial samples (reading b).

    The PLI of a short window is biased upwards, more the fewer samples it has (on independent noise the
    61-sample windows give about 0.6 to 0.95 per trial, the 549-sample post window 0.2 to 0.8), so a
    change between windows of different length is mostly that bias. `post` is therefore the mean of the
    PLI of the nine 20 ms sub-windows of 20 to 200 ms, each as long as the pre and tFUS windows;
    `post_full` is the whole 20 to 200 ms window, kept for comparison. Each window also gets a noise
    floor (`*_shuffled`): the same PLI with the contralateral channels taken from the next trial, which
    keeps every channel's own phase and its locking to the pulse and breaks the same-trial pairing.'''
assert old in s; s=s.replace(old,new)
open("tfus.py","w").write(s)
EOF
```

```
(Bash completed with no output)
```

**Agent calls Bash**

```bash
cd entries/001683-gao-2026; $TMPDIR/venv/bin/python - <<'EOF'
import json
d=json.load(open("wild_type.ipynb"))
for i,c in enumerate(d["cells"]):
    print(f"#### [{i}] {c['cell_type']} {c.get('metadata',{}).get('tags')}")
    print("".join(c["source"]))
EOF
```

```
#### [0] markdown None
# Gao et al. (2026) on dandiset 001683: evoked potentials and PLI in wild-type rats

Paper. Gao H, Frake A, Durand DM, He B (2026). Transcranial focused ultrasound stimulation
targeting white matter inhibits seizures in a rat model of epilepsy. *IEEE Trans Neural Syst Rehabil
Eng* 34, 251-259. [doi:10.1109/tnsre.2025.3644273](https://doi.org/10.1109/tnsre.2025.3644273). The
claims file was written from the NIH author manuscript (PMC12848950) and the supplement.

Dandiset. [DANDI:001683](https://dandiarchive.org/dandiset/001683/0.260109.2104), version
0.260109.2104, the only published version (the paper cites none; see `seizure_metrics.ipynb`).

The wild-type phase, before any 4-AP: the target-confirmation recordings (`EP data`: a resting
`BASELINE` recording and one recording per transducer position, each with about 200 bursts, from
the 64-channel intracranial array in left S1), and one EEG recording per rat labelled
`EEG data for PLV analysis` (32 skull channels, `*_1Hz_20ms_CC`).

| Claim | Tested here |
|---|---|
| fig5b-tfus-evoked-potentials | yes |
| fig5cdj-wild-type-gamma-pli-decrease | blocked (data_missing): no EEG of the resting baseline (the sham); the tFUS part is run |
[... 314 more lines not kept]
```

**Agent**

Now the wild_type notebook edits: alignment check, split-half position reading, equal-length PLI windows with noise floors.

**Agent calls Bash**

```bash
mkdir -p $TMPDIR/nb; cat > $TMPDIR/nb/nbedit.py <<'EOF'
import json, sys
def load(p): return json.load(open(p))
def save(d,p):
    json.dump(d,open(p,"w"),indent=1,ensure_ascii=False); open(p,"a").write("\n")
def src(d,i): return "".join(d["cells"][i]["source"])
def setsrc(d,i,s):
    lines=s.split("\n"); d["cells"][i]["source"]=[l+"\n" for l in lines[:-1]]+[lines[-1]]
def new(kind,s,tags=None):
    c={"cell_type":kind,"metadata":({"tags":tags} if tags else {}),"source":[]}
    if kind=="code": c["outputs"]=[]; c["execution_count"]=None
    lines=s.split("\n"); c["source"]=[l+"\n" for l in lines[:-1]]+[lines[-1]]
    return c
EOF
cd entries/001683-gao-2026; head -c 600 wild_type.ipynb; tail -c 400 wild_type.ipynb
```

```
{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "a0bd1d6b",
   "metadata": {},
   "source": [
    "# Gao et al. (2026) on dandiset 001683: evoked potentials and PLI in wild-type rats\n",
    "\n",
    "Paper. Gao H, Frake A, Durand DM, He B (2026). Transcranial focused ultrasound stimulation\n",
    "targeting white matter inhibits seizures in a rat model of epilepsy. *IEEE Trans Neural Syst Rehabil\n",
    "Eng* 34, 251-259. [doi:10.1109/tnsre.2025.3644273](https://doi.org/10.1109/tnsre.2025.3644273). The\n",
    "claims file was written from the NIH author manuscript (PMC12848950) andis not recorded."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2d21a054",
   "metadata": {},
[... 16 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/nb; $TMPDIR/venv/bin/python - <<'EOF'
s=open("nbedit.py").read()
s=s.replace('c={"cell_type":kind,','import uuid\n    c={"id":uuid.uuid4().hex[:8],"cell_type":kind,')
s=s.replace('json.dump(d,open(p,"w"),indent=1,ensure_ascii=False); open(p,"a").write("\\n")','open(p,"w").write(json.dumps(d,indent=1,ensure_ascii=False)+"\\n")')
open("nbedit.py","w").write(s)
EOF
cat nbedit.py
```

```
import json, sys
def load(p): return json.load(open(p))
def save(d,p):
    open(p,"w").write(json.dumps(d,indent=1,ensure_ascii=False)+"\n")
def src(d,i): return "".join(d["cells"][i]["source"])
def setsrc(d,i,s):
    lines=s.split("\n"); d["cells"][i]["source"]=[l+"\n" for l in lines[:-1]]+[lines[-1]]
def new(kind,s,tags=None):
    import uuid
    c={"id":uuid.uuid4().hex[:8],"cell_type":kind,"metadata":({"tags":tags} if tags else {}),"source":[]}
    if kind=="code": c["outputs"]=[]; c["execution_count"]=None
    lines=s.split("\n"); c["source"]=[l+"\n" for l in lines[:-1]]+[lines[-1]]
    return c
Shell cwd was reset to
```

**Agent**

Prototype the EP alignment check on two rats first.

**Agent calls Bash**

```bash
cd entries/001683-gao-2026; cat > $TMPDIR/align.py <<'EOF'
import time, numpy as np, pandas as pd, tfus, sys
t0=time.time()
assets=tfus.list_assets(); small=assets[assets["size"]<2e9]
metas=tfus.read_all_meta(small.asset_id.tolist())
ep=[m for m in metas if m["kind"]=="EP data"]; plv=[m for m in metas if m["kind"].startswith("EEG data for PLV")]
print("meta", time.time()-t0, len(ep), len(plv))
import pickle; pickle.dump((ep,plv,[m for m in metas]),open(sys.argv[1],"wb"))
EOF
$TMPDIR/venv/bin/python $TMPDIR/align.py $TMPDIR/metas.pkl; date -u
```

```
Traceback (most recent call last):
  File "/tmp/claude-1001/align.py", line 1, in <module>
    import time, numpy as np, pandas as pd, tfus, sys
ModuleNotFoundError: No module named 'tfus'
Tue Nov  3 11:55:15 UTC 2026
```

**Agent calls Bash**

```bash
cd entries/001683-gao-2026; PYTHONPATH=. $TMPDIR/venv/bin/python $TMPDIR/align.py $TMPDIR/metas.pkl
```

```
meta 144.45791864395142 228 20
```

**Agent calls Bash**

```bash
cd entries/001683-gao-2026; cat > $TMPDIR/align2.py <<'EOF'
import time, pickle, numpy as np, pandas as pd, tfus
ep,plv,metas=pickle.load(open("/tmp/claude-1001/metas.pkl","rb"))
def position(m):
    lab = m["label"].split("_", 1)[1]
    if lab == "BASELINE": return "BASELINE"
    lab = lab.replace("_", "")
    for key in ("CENTER2", "CENTER", "SHALLOW1mm", "DEEP1mm", "FRONT05mm", "FRONT1mm", "BACK05mm", "BACK1mm", "LSIDE05mm", "RSIDE05mm"):
        if "S1" in lab: return "S1:" + lab
        if key in lab: return key
    return "?" + lab
for kind, files in (("EP", ep), ("PLV", plv)):
    L = np.concatenate([(m["intervals"].stop - m["intervals"].start).to_numpy() for m in files])
    print(kind, "interval stop - start (s): min %.4f median %.4f max %.4f" % (L.min(), np.median(L), L.max()))
t0=time.time()
def long_mean(m, n=30, pre=1.0, post=2.2, binms=10):
    on = np.sort(m["intervals"].start.to_numpy())[1:n+1]
    i0 = int((on[0]-pre)*tfus.RATE); i1 = int((on[-1]+post)*tfus.RATE)+1
    x = tfus.read_rows(m, i0, i1).mean(axis=1)    # channel mean
    n0, n1 = int(pre*tfus.RATE), int(post*tfus.RATE)
    ep_ = np.stack([x[int(t*tfus.RATE)-i0-n0: int(t*tfus.RATE)-i0+n1] for t in on])
    ep_ = ep_ - ep_[:, n0-int(0.02*tfus.RATE):n0].mean(1, keepdims=True)
    mu = ep_.mean(0)*1e6
    b = int(binms/1000*tfus.RATE); nb = len(mu)//b
    return mu[:nb*b].reshape(nb, b).mean(1)
cen=[m for m in ep if position(m)=="CENTER"][:2]
for m in cen:
    r=long_mean(m); t=np.arange(len(r))*10-1000
    print(m["subject"], "max |mean| bins:", [(int(t[i]), round(r[i],2)) for i in np.argsort(-np.abs(r))[:6]])
print(time.time()-t0)
EOF
PYTHONPATH=. $TMPDIR/venv/bin/python $TMPDIR/align2.py
```

```
EP interval stop - start (s): min 2.2000 median 2.2000 max 2.2000
PLV interval stop - start (s): min 2.2000 median 2.2000 max 2.2000
BH624 max |mean| bins: [(720, np.float64(21.04)), (750, np.float64(20.54)), (920, np.float64(-19.74)), (760, np.float64(18.07)), (240, np.float64(17.69)), (930, np.float64(-17.46))]
BH626 max |mean| bins: [(870, np.float64(-25.43)), (1140, np.float64(-25.25)), (1180, np.float64(-24.56)), (1130, np.float64(-24.4)), (1500, np.float64(-24.39)), (1270, np.float64(23.44))]
1.7005724906921387
```

**Agent calls Bash**

```bash
cd entries/001683-gao-2026; cat > $TMPDIR/align3.py <<'EOF'
import time, pickle, numpy as np, pandas as pd, tfus
from scipy import signal
ep,plv,metas=pickle.load(open("/tmp/claude-1001/metas.pkl","rb"))
exec(open("/tmp/claude-1001/pos.py").read())
sos=signal.butter(4,[3,300],btype="bandpass",fs=tfus.RATE,output="sos")
def folded(m, n=100, binms=5):
    on = np.sort(m["intervals"].start.to_numpy())[1:n+1]
    i0 = int((on[0]-0.1)*tfus.RATE); i1 = int((on[-1]+2.0)*tfus.RATE)
    x = tfus.read_rows(m, i0, i1)
    x = signal.sosfiltfilt(sos, x, axis=0)
    L = int(2.0*tfus.RATE)
    e = np.stack([x[int(t*tfus.RATE)-i0 - int(0.1*tfus.RATE): int(t*tfus.RATE)-i0 - int(0.1*tfus.RATE)+L] for t in on])  # -100 ms .. 1900 ms
    mu = e.mean(0)                      # time, channels
    rms = np.sqrt((mu**2).mean(1))*1e6  # RMS over channels of trial mean
    b=int(binms/1000*tfus.RATE); nb=len(rms)//b
    return rms[:nb*b].reshape(nb,b).mean(1)
t0=time.time()
for kind in ("CENTER","BASELINE"):
    for m in [m for m in ep if position(m)==kind][:4]:
        r=folded(m); t=np.arange(len(r))*5-100
        top=np.argsort(-r)[:5]
        print(kind, m["subject"], "median %.2f" % np.median(r), "top bins (ms, uV):", [(int(t[i]), round(r[i],2)) for i in top])
print(time.time()-t0)
EOF
$TMPDIR/venv/bin/python - <<'EOF'
import json
d=json.load(open("wild_type.ipynb")); s="".join(d["cells"][3]["source"]); open("/tmp/claude-1001/pos.py","w").write(s.split("\nE = ")[0])
EOF
PYTHONPATH=. $TMPDIR/venv/bin/python $TMPDIR/align3.py
```

```
CENTER BH624 median 3.17 top bins (ms, uV): [(195, np.float64(13.41)), (160, np.float64(12.33)), (200, np.float64(12.32)), (535, np.float64(11.89)), (540, np.float64(11.84))]
CENTER BH626 median 3.98 top bins (ms, uV): [(1260, np.float64(17.6)), (1255, np.float64(15.33)), (1265, np.float64(14.88)), (875, np.float64(14.22)), (1280, np.float64(13.57))]
CENTER BH634 median 3.42 top bins (ms, uV): [(500, np.float64(15.89)), (495, np.float64(15.02)), (240, np.float64(14.27)), (505, np.float64(13.99)), (245, np.float64(13.82))]
CENTER BH635 median 2.66 top bins (ms, uV): [(1320, np.float64(8.97)), (70, np.float64(8.92)), (1330, np.float64(8.52)), (1325, np.float64(8.47)), (260, np.float64(8.36))]
BASELINE BH624 median 2.74 top bins (ms, uV): [(1645, np.float64(9.11)), (315, np.float64(9.05)), (320, np.float64(8.65)), (310, np.float64(8.45)), (1440, np.float64(8.14))]
BASELINE BH626 median 5.61 top bins (ms, uV): [(1655, np.float64(17.22)), (50, np.float64(16.46)), (45, np.float64(16.24)), (55, np.float64(16.06)), (930, np.float64(15.47))]
BASELINE BH634 median 2.68 top bins (ms, uV): [(120, np.float64(10.4)), (115, np.float64(10.23)), (1495, np.float64(9.76)), (1500, np.float64(9.06)), (125, np.float64(8.64))]
BASELINE BH635 median 2.89 top bins (ms, uV): [(1020, np.float64(10.43)), (1755, np.float64(9.7)), (1195, np.float64(9.52)), (930, np.float64(9.38)), (1025, np.float64(9.16))]
23.333654165267944
```

**Agent**

No stimulus-locked response appears anywhere in the 2 s cycle in CENTER files (same RMS as BASELINE). Checking for a 1.5 kHz PRF artifact to pin the burst timing independently.

**Agent calls Bash**

```bash
cd entries/001683-gao-2026; cat > $TMPDIR/align4.py <<'EOF'
import time, pickle, numpy as np, pandas as pd, tfus
from scipy import signal
ep,plv,metas=pickle.load(open("/tmp/claude-1001/metas.pkl","rb"))
exec(open("/tmp/claude-1001/pos.py").read())
m=[m for m in ep if position(m)=="CENTER"][0]
on = np.sort(m["intervals"].start.to_numpy())
x = tfus.read_rows(m, int((on[1]-0.1)*tfus.RATE), int((on[21])*tfus.RATE)).mean(1)
f,p=signal.welch(x,tfus.RATE,nperseg=4096)
print("peaks of channel-mean PSD above 200 Hz:", [(round(f[i]),f"{p[i]:.2e}") for i in np.argsort(-p*(f>200))[:8]])
for lo,hi in ((1400,1520),(700,760),(200,400)):
    sos=signal.butter(4,[lo,hi],btype="bandpass",fs=tfus.RATE,output="sos")
    for mm,name in ((m,"CENTER"),([q for q in ep if position(q)=="BASELINE" and q["subject"]==m["subject"]][0],"BASELINE")):
        on = np.sort(mm["intervals"].start.to_numpy())[1:61]
        i0=int((on[0]-0.1)*tfus.RATE); i1=int((on[-1]+2.0)*tfus.RATE)
        y=signal.sosfiltfilt(sos, tfus.read_rows(mm,i0,i1), axis=0)**2
        y=y.mean(1); L=int(2*tfus.RATE)
        e=np.stack([y[int(t*tfus.RATE)-i0-int(0.1*tfus.RATE):][:L] for t in on]).mean(0)
        b=int(0.01*tfus.RATE); nb=len(e)//b; r=e[:nb*b].reshape(nb,b).mean(1); t=np.arange(nb)*10-100
        print(lo,hi,name,"ratio max/median %.2f"%(r.max()/np.median(r)),"at",[int(t[i]) for i in np.argsort(-r)[:5]])
EOF
PYTHONPATH=. $TMPDIR/venv/bin/python $TMPDIR/align4.py
```

```
peaks of channel-mean PSD above 200 Hz: [(212, '4.99e-15'), (212, '4.71e-15'), (204, '4.65e-15'), (203, '4.33e-15'), (215, '4.08e-15'), (215, '3.97e-15'), (211, '3.93e-15'), (205, '3.79e-15')]
1400 1520 CENTER ratio max/median 1.65 at [30, 20, 40, 60, 50]
1400 1520 BASELINE ratio max/median 1.24 at [1130, 1430, 810, 120, 1510]
700 760 CENTER ratio max/median 1.95 at [1610, 650, 1620, 670, 680]
700 760 BASELINE ratio max/median 1.71 at [1430, 1420, 1130, 1500, 1510]
200 400 CENTER ratio max/median 2.69 at [1610, 1620, 680, 720, 760]
200 400 BASELINE ratio max/median 1.67 at [1430, 1140, 110, 1420, 1130]
```

**Agent**

The 1.4–1.5 kHz band (the 1.5 kHz PRF) rises 20–60 ms after the interval start in CENTER only, which fits burst onset at the interval start. I'll make that a notebook check over all rats.

**Agent calls Bash**

```bash
cd entries/001683-gao-2026; $TMPDIR/venv/bin/python - <<'EOF'
import sys; sys.path.insert(0,"/tmp/claude-1001/nb"); from nbedit import *
p="wild_type.ipynb"; d=load(p)
assert src(d,5).startswith("# Alignment of the intervals")
cell = new("code", '''# Alignment of the EP intervals with the bursts (verifier, round 1). The intervals last 2.2 s and start
# 2 s apart; a burst at another lag would still show at a fixed lag of the 2 s cycle. Two checks on the
# first 40 cycles of every CENTER and BASELINE file: (1) the RMS over the 64 channels of the
# trial-mean LFP (3-300 Hz) over the whole cycle, -100 to 1900 ms from the interval start, in 10 ms
# bins; (2) the power at 1400-1520 Hz, the band of the bursts' 1.5 kHz pulse repetition frequency (just
# under the 1526 Hz Nyquist frequency), where an ultrasound artifact would mark the 67 ms burst.
from scipy import signal as sg
for kind, files in (("EP", ep), ("PLV", plv)):
    L = np.concatenate([(m["intervals"].stop - m["intervals"].start).to_numpy() for m in files])
    print(f"{kind} files, interval stop - start: {L.min():.4f} to {L.max():.4f} s; start spacing:",
          sorted({round(float(np.median(np.diff(np.sort(m['intervals'].start)))), 3) for m in files}))
SOS_LFP = sg.butter(4, [3, 300], btype="bandpass", fs=tfus.RATE, output="sos")
SOS_PRF = sg.butter(4, [1400, 1520], btype="bandpass", fs=tfus.RATE, output="sos")

def cycle_profile(m, n=40):
    on = np.sort(m["intervals"].start.to_numpy())[1:n + 1]
    pre, L, b = int(0.1 * tfus.RATE), int(2.0 * tfus.RATE), int(0.01 * tfus.RATE)
    i0, i1 = int(on[0] * tfus.RATE) - pre, int(on[-1] * tfus.RATE) - pre + L
    x = tfus.read_rows(m, i0, i1, threads=8)
    idx = [int(t * tfus.RATE) - pre - i0 for t in on]
    lfp = sg.sosfiltfilt(SOS_LFP, x, axis=0)
    mu = np.mean([lfp[i:i + L] for i in idx], axis=0)
    rms = np.sqrt((mu ** 2).mean(1)) * 1e6
    hf = (sg.sosfiltfilt(SOS_PRF, x, axis=0) ** 2).mean(1)
    pw = np.mean([hf[i:i + L] for i in idx], axis=0)
    nb = L // b
    return rms[:nb * b].reshape(nb, b).mean(1), pw[:nb * b].reshape(nb, b).mean(1)

t_cyc = np.arange(int(2.0 * tfus.RATE) // int(0.01 * tfus.RATE)) * 10 - 100
prof = {}
with ThreadPoolExecutor(4) as ex:
    jobs = [m for m in ep if position(m) in ("CENTER", "BASELINE")]
    for m, r in zip(jobs, ex.map(cycle_profile, jobs)):
        prof[(m["subject"], position(m))] = r
burst = (t_cyc >= 0) & (t_cyc < 70)
rows = []
for (s, pos), (rms, pw) in prof.items():
    rows.append({"subject": s, "position": pos, "LFP RMS 0-70 ms / rest (uV)": f"{rms[burst].mean():.2f} / {rms[~burst & (t_cyc >= 0)].mean():.2f}",
                 "LFP RMS peak lag (ms)": int(t_cyc[np.argmax(rms)]),
                 "1.4-1.5 kHz power 0-70 ms / rest": pw[burst].mean() / pw[~burst & (t_cyc >= 0)].mean(),
                 "1.4-1.5 kHz peak lag (ms)": int(t_cyc[np.argmax(pw)])})
AL = pd.DataFrame(rows).sort_values(["position", "subject"])
print(AL.round(3).to_string(index=False))
for pos in ("CENTER", "BASELINE"):
    a = AL[AL.position == pos]
    print(f"{pos}: 1.4-1.5 kHz power ratio 0-70 ms over the rest of the cycle, median {a['1.4-1.5 kHz power 0-70 ms / rest'].median():.3f}, "
          f"above 1.1 in {(a['1.4-1.5 kHz power 0-70 ms / rest'] > 1.1).sum()} of {len(a)} rats; "
          f"high-frequency peak within 0-70 ms in {((a['1.4-1.5 kHz peak lag (ms)'] >= 0) & (a['1.4-1.5 kHz peak lag (ms)'] < 70)).sum()}; "
          f"LFP RMS peak within 0-200 ms in {((a['LFP RMS peak lag (ms)'] >= 0) & (a['LFP RMS peak lag (ms)'] < 200)).sum()}")
mean_rms = {pos: np.mean([v[0] for k, v in prof.items() if k[1] == pos], axis=0) for pos in ("CENTER", "BASELINE")}
for pos, r in mean_rms.items():
    print(f"{pos}, mean over rats of the cycle RMS profile: 0-200 ms {r[(t_cyc >= 0) & (t_cyc < 200)].mean():.2f} uV, "
          f"200-1900 ms {r[t_cyc >= 200].mean():.2f} uV, max {r.max():.2f} uV at {int(t_cyc[np.argmax(r)])} ms")''', ["sanity"])
d["cells"].insert(6, cell)
save(d,p)
EOF
```

```
(Bash completed with no output)
```

**Agent calls Bash**

```bash
cd entries/001683-gao-2026; cat > $TMPDIR/runcells.py <<'EOF'
import sys, json, pickle, time
sys.path.insert(0,"."); 
nb, cells = sys.argv[1], [int(c) for c in sys.argv[2].split(",")]
d=json.load(open(nb)); g={}
exec("import pickle\nep,plv,metas=pickle.load(open('/tmp/claude-1001/metas.pkl','rb'))", g)
for i in cells:
    t=time.time(); s="".join(d["cells"][i]["source"])
    s="\n".join(l for l in s.split("\n") if not l.startswith("plt.") and "plt.show" not in l)
    exec(s, g); print(f"[cell {i}: {time.time()-t:.0f} s]")
EOF
sed -i 's#^exec("import pickle#import matplotlib; matplotlib.use("Agg")\nexec("import time, re, numpy as np, pandas as pd, tfus, matplotlib.pyplot as plt\\nfrom concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor\\nimport multiprocessing as mp\\nimport pickle#' $TMPDIR/runcells.py
PYTHONPATH=. $TMPDIR/venv/bin/python $TMPDIR/runcells.py wild_type.ipynb 3,6 2>&1 | tail -70
```

```
BH649    BH649_1Hz_20ms_CC 2025-02-16T20:52:12.000000-05:00       200 1.999995 400.556032        32
  BH650    BH650_1Hz_20ms_CC 2025-02-18T17:58:00.000000-05:00       200 1.999995 401.478779        32
  BH651    BH651_1Hz_20ms_CC 2025-02-04T19:26:29.000000-05:00       200 1.999995 401.311007        32
  BH652    BH652_1Hz_20ms_CC 2025-02-07T20:01:16.000000-05:00       200 1.999995 400.388260        32
  BH653    BH653_1Hz_20ms_CC 2025-02-11T18:05:58.000000-05:00       200 1.999995 400.388260        32
  BH659    BH659_1Hz_20ms_CC 2025-02-28T19:35:14.000000-05:00       200 1.999995 401.227121        32
  BH660    BH660_1Hz_20ms_CC 2025-03-04T18:08:40.000000-05:00       200 1.999995 400.723804        32
  BH661    BH661_1Hz_20ms_CC 2025-03-06T18:17:22.000000-05:00       200 1.999995 400.556032        32
  BH662    BH662_1Hz_20ms_CC 2025-03-11T16:18:14.000000-04:00       200 1.999995 401.143235        32
  BH663    BH663_1Hz_20ms_CC 2025-03-13T18:20:01.000000-04:00       206 1.999995 413.810033        32
  BH665    BH665_1Hz_20ms_CC 2025-03-18T17:14:39.000000-04:00       201 1.999995 403.492045        32
  BH666    BH666_1Hz_20ms_CC 2025-02-25T17:40:30.000000-05:00       206 1.999995 413.810033        32
Rats with EP files but no PLV file: ['BH638', 'BH642', 'BH644']
PLV electrode tables all the same: True
Other kinds among the small files: []
[cell 3: 0 s]
EP files, interval stop - start: 2.2000 to 2.2000 s; start spacing: [2.0, 2.5]
PLV files, interval stop - start: 2.2000 to 2.2000 s; start spacing: [1.0, 2.0]
subject position LFP RMS 0-70 ms / rest (uV)  LFP RMS peak lag (ms)  1.4-1.5 kHz power 0-70 ms / rest  1.4-1.5 kHz peak lag (ms)
  BH624 BASELINE                 3.57 / 5.30                   1440                             0.981                       1130
[... 50 more lines not kept]
```

**Agent**

Alignment confirmed: in 13 of 23 CENTER rats the PRF-band power peaks 10–60 ms after the interval start, in 0 of 23 BASELINE. Now updating the fig5b and PLI cells.

**Agent calls Bash**

```bash
cd entries/001683-gao-2026; $TMPDIR/venv/bin/python - <<'EOF'
import sys; sys.path.insert(0,"/tmp/claude-1001/nb"); from nbedit import *
p="wild_type.ipynb"; d=load(p)
s=src(d,7)
old="""In the PLV EEG the mean response after the interval start is many times the pre-onset level, so
the interval starts are the pulse onsets, in seconds (these files' tables are in seconds, unlike
the seizure labels). In the intracranial EP files the contrast is weaker; it is tested below."""
new="""In the PLV EEG the mean response after the interval start is many times the pre-onset level, so
the interval starts are the pulse onsets, in seconds (these files' tables are in seconds, unlike
the seizure labels). In the intracranial EP files the LFP shows no clear response at any lag of the
2 s cycle, in CENTER as in BASELINE (second table). The bursts can still be located: power at 1.4 to
1.5 kHz, the band of their 1.5 kHz pulse repetition frequency, peaks 10 to 60 ms after the interval
start in most CENTER recordings and in none of the resting ones (counts printed above), so the
interval starts are the burst onsets. An EP absent from the LFP is therefore not a misalignment of
the intervals."""
assert old in s; setsrc(d,7,s.replace(old,new))
s=src(d,7)
s=s.replace("""or repeated measures (`tfus.timepoint_tests`), Bonferroni over the time points from 0 to 200 ms.""","""or repeated measures (`tfus.timepoint_tests`; the repeated reading adds a random intercept per rat to
the same two-way ANOVA), Bonferroni over the time points from 0 to 200 ms.""")
s=s.replace("""recording, the first estimate, and (b) the position whose channel-mean EP has the largest peak
from 0 to 200 ms.""","""recording, the first estimate, and (b) the position whose channel-mean EP has the largest peak
from 0 to 200 ms. Reading (b) picks the position on the data it then tests, so it is also run with
the position picked on the odd trials and the test made on the even trials (`largest, split`).""")
setsrc(d,7,s)
s=src(d,8)
old="""def ep_job(m):
    on = np.sort(m["intervals"].start.to_numpy())[:tfus.N_TRIALS]
    return (m["subject"], position(m)), tfus.evoked(tfus.read_epochs(m, on, threads=16))

t0 = time.time()
stim_files = [m for m in ep if position(m) not in ("BASELINE",) and not position(m).startswith("S1:")]
with ThreadPoolExecutor(4) as ex:
    for k, v in ex.map(ep_job, stim_files):
        evo[k] = v"""
new="""evo_half = {}     # (subject, position) -> (evoked of the odd trials, evoked of the even trials)

def ep_job(m):
    on = np.sort(m["intervals"].start.to_numpy())[:tfus.N_TRIALS]
    x = tfus.read_epochs(m, on, threads=16)
    return (m["subject"], position(m)), tfus.evoked(x), (tfus.evoked(x[0::2]), tfus.evoked(x[1::2]))

t0 = time.time()
stim_files = [m for m in ep if position(m) not in ("BASELINE",) and not position(m).startswith("S1:")]
with ThreadPoolExecutor(4) as ex:
    for k, v, h in ex.map(ep_job, stim_files):
        evo[k], evo_half[k] = v, h"""
assert old in s; setsrc(d,8,s.replace(old,new))
s=src(d,9)
old="""chosen_b = {s: max([k for k in evo if k[0] == s], key=lambda k: peak[k])[1] for s in rats}
print("Position with the largest channel-mean EP peak (reading b):", pd.Series(chosen_b).value_counts().to_dict())
rows, results = [], {}
for pos_reading in ("CENTER", "largest"):
    keys = [(s, "CENTER" if pos_reading == "CENTER" else chosen_b[s]) for s in rats]
    A = np.stack([evo[k] for k in keys])                       # rats, time, channels"""
new="""chosen_b = {s: max([k for k in evo if k[0] == s], key=lambda k: peak[k])[1] for s in rats}
peak_odd = {k: np.abs(v[0].mean(axis=1)[post]).max() for k, v in evo_half.items()}
chosen_split = {s: max([k for k in evo if k[0] == s], key=lambda k: peak_odd[k])[1] for s in rats}
print("Position with the largest channel-mean EP peak (reading b):", pd.Series(chosen_b).value_counts().to_dict())
print("Same, picked on the odd trials:", pd.Series(chosen_split).value_counts().to_dict(),
      f"; same position as reading (b) in {sum(chosen_b[s] == chosen_split[s] for s in rats)} of {len(rats)} rats")
rows, results = [], {}
for pos_reading in ("CENTER", "largest", "largest, split"):
    if pos_reading == "largest, split":
        A = np.stack([evo_half[(s, chosen_split[s])][1] for s in rats])    # even trials only
    else:
        keys = [(s, "CENTER" if pos_reading == "CENTER" else chosen_b[s]) for s in rats]
        A = np.stack([evo[k] for k in keys])                   # rats, time, channels"""
assert old in s; setsrc(d,9,s.replace(old,new))
save(d,p)
EOF
```

```
(Bash completed with no output)
```

**Agent calls Bash**

```bash
cd entries/001683-gao-2026; $TMPDIR/venv/bin/python - <<'EOF'
import sys; sys.path.insert(0,"/tmp/claude-1001/nb"); from nbedit import *
p="wild_type.ipynb"; d=load(p)
s=src(d,13)
old="""            for win in ("tfus", "post"):"""
new="""            for win in ("tfus", "post", "post_full"):"""
assert old in s; s=s.replace(old,new)
old="""WM = WP.groupby(["band", "reading", "norm", "window"])[["S1", "nonS1", "pairs decreasing"]].mean()
print(WM.round(4).unstack("window").to_string())"""
new="""WM = WP.groupby(["band", "reading", "norm", "window"])[["S1", "nonS1", "pairs decreasing"]].mean()
print(WM.round(4).unstack("window").to_string())
# Noise floor (verifier, round 1): the PLI of each window with the contralateral channels taken from the
# next trial, against the same-trial PLI. "post" is the mean over the nine 20 ms sub-windows of 20-200 ms,
# as long as the pre and tFUS windows; "post_full" is the whole 549-sample window.
rows = []
for s, r in W.items():
    for band in tfus.BANDS:
        for reading in ("per_trial", "concat"):
            for win in ("pre", "tfus", "post", "post_full"):
                x, f = r[band][win][reading], r[band][win][reading + "_shuffled"]
                rows.append({"subject": s, "band": band, "reading": reading, "window": win,
                             "S1": x[:k, :k].mean(), "S1 floor": f[:k, :k].mean(),
                             "nonS1": x[k:, k:].mean(), "nonS1 floor": f[k:, k:].mean()})
FL = pd.DataFrame(rows)
FLm = FL.groupby(["band", "reading", "window"])[["S1", "S1 floor", "nonS1", "nonS1 floor"]].mean()
print("\\nPLI and its trial-shuffled noise floor, mean over rats:")
print(FLm.round(4).unstack("window").to_string())"""
assert old in s; s=s.replace(old,new)
setsrc(d,13,s)
s=src(d,12)
old="""per trial and averaged (reading a) or over the concatenated samples of all trials (reading b)."""
new="""per trial and averaged (reading a) or over the concatenated samples of all trials (reading b).
The PLI of a short window is biased upwards, the more so the fewer samples it holds, so the 549
samples of 20 to 200 ms cannot be compared with the 61 of the pre window (the first version of this
attempt did, and its post-window decreases were that bias). The post window is therefore the mean
PLI of its nine 20 ms sub-windows, each as long as the pre window; the whole window is shown as
`post_full`. Each window's PLI is also given with a noise floor, the same PLI with the contralateral
channels taken from the next trial."""
assert old in s; setsrc(d,12,s.replace(old,new))
s=src(d,15)
s=s.replace("""print(g.round(4).unstack("window").to_string())""","""print(g.round(4).unstack("window").to_string())
print("\\nGamma PLI against its trial-shuffled floor (means over rats):")
print(FLm.loc["gamma"].round(4).unstack("window").to_string())""")
s=s.replace("""columns=["reading", "window"], values=["S1", "nonS1"])""","""columns=["reading", "window"], values=["S1", "nonS1"])
per_rat = per_rat.loc[:, per_rat.columns.get_level_values("window") != "post_full\"""")
setsrc(d,15,s)
save(d,p)
print(src(d,15))
EOF
```

```
g = WM.loc["gamma"]
print(g.round(4).unstack("window").to_string())
print("\nGamma PLI against its trial-shuffled floor (means over rats):")
print(FLm.loc["gamma"].round(4).unstack("window").to_string())
per_rat = WP[(WP.band == "gamma") & (WP.norm == "diff")].pivot_table(index="subject", columns=["reading", "window"], values=["S1", "nonS1"])
per_rat = per_rat.loc[:, per_rat.columns.get_level_values("window") != "post_full"
print("\nPer rat, gamma PLI difference from pre:")
print(per_rat.round(4).to_string())
```

**Agent**

Fix the bracket typo.

**Agent calls Bash**

```bash
cd entries/001683-gao-2026; $TMPDIR/venv/bin/python - <<'EOF'
import sys; sys.path.insert(0,"/tmp/claude-1001/nb"); from nbedit import *
p="wild_type.ipynb"; d=load(p)
s=src(d,15).replace('!= "post_full"\n','!= "post_full"]\n'); setsrc(d,15,s); save(d,p)
s=src(d,18)
s=s.replace('''print("\\nMeans over rats, theta, alpha, beta:")''','''print("\\nThe same with the whole 20-200 ms window (post_full), biased by its length (shown for comparison):")
rows = []
for reading in ("per_trial", "concat"):
    for norm in ("diff", "ratio"):
        ref = 0.0 if norm == "diff" else 1.0
        bands_ok = [band for band in ("theta", "alpha", "beta")
                    if all(WM.loc[(band, reading, norm, w)].S1 < ref and WM.loc[(band, reading, norm, w)].nonS1 >= ref for w in ("tfus", "post_full"))]
        rows.append({"reading": reading, "norm": norm, "bands with S1 below and non-S1 not below": ", ".join(bands_ok) or "none"})
print(pd.DataFrame(rows).to_string(index=False))
print("\\nMeans over rats, theta, alpha, beta:")''')
setsrc(d,18,s); save(d,p)
print(s[-600:])
EOF
```

```
for norm in ("diff", "ratio"):
        ref = 0.0 if norm == "diff" else 1.0
        bands_ok = [band for band in ("theta", "alpha", "beta")
                    if all(WM.loc[(band, reading, norm, w)].S1 < ref and WM.loc[(band, reading, norm, w)].nonS1 >= ref for w in ("tfus", "post_full"))]
        rows.append({"reading": reading, "norm": norm, "bands with S1 below and non-S1 not below": ", ".join(bands_ok) or "none"})
print(pd.DataFrame(rows).to_string(index=False))
print("\nMeans over rats, theta, alpha, beta:")
print(WM.loc[["theta", "alpha", "beta"]].round(4).unstack("window").to_string())
```

**Agent calls Bash**

```bash
cd entries/001683-gao-2026; PYTHONPATH=. $TMPDIR/venv/bin/python - <<'EOF'
import pickle,time,tfus,numpy as np
ep,plv,metas=pickle.load(open("/tmp/claude-1001/metas.pkl","rb"))
t=time.time(); r=tfus.wild_pli(plv[0]); print(time.time()-t)
k=4
for b in tfus.BANDS:
    print(b, {w:(round(r[b][w]["per_trial"][:k,:k].mean(),3), round(r[b][w]["per_trial_shuffled"][:k,:k].mean(),3), round(r[b][w]["concat"][:k,:k].mean(),3), round(r[b][w]["concat_shuffled"][:k,:k].mean(),3)) for w in r[b] if w!="n_trials"})
EOF
```

```
42.11320233345032
theta {'pre': (np.float64(0.979), np.float64(0.977), np.float64(0.102), np.float64(0.089)), 'tfus': (np.float64(0.978), np.float64(0.979), np.float64(0.109), np.float64(0.094)), 'post_full': (np.float64(0.797), np.float64(0.79), np.float64(0.102), np.float64(0.084)), 'post': (np.float64(0.977), np.float64(0.977), np.float64(0.105), np.float64(0.088))}
alpha {'pre': (np.float64(0.971), np.float64(0.967), np.float64(0.103), np.float64(0.107)), 'tfus': (np.float64(0.972), np.float64(0.973), np.float64(0.11), np.float64(0.114)), 'post_full': (np.float64(0.722), np.float64(0.735), np.float64(0.082), np.float64(0.064)), 'post': (np.float64(0.967), np.float64(0.968), np.float64(0.098), np.float64(0.069))}
beta {'pre': (np.float64(0.846), np.float64(0.844), np.float64(0.183), np.float64(0.154)), 'tfus': (np.float64(0.895), np.float64(0.892), np.float64(0.335), np.float64(0.267)), 'post_full': (np.float64(0.374), np.float64(0.364), np.float64(0.072), np.float64(0.048)), 'post': (np.float64(0.852), np.float64(0.852), np.float64(0.103), np.float64(0.076))}
gamma {'pre': (np.float64(0.628), np.float64(0.634), np.float64(0.067), np.float64(0.038)), 'tfus': (np.float64(0.606), np.float64(0.609), np.float64(0.063), np.float64(0.052)), 'post_full': (np.float64(0.242), np.float64(0.24), np.float64(0.029), np.float64(0.016)), 'post': (np.float64(0.635), np.float64(0.64), np.float64(0.049), np.float64(0.044))}
```

**Agent**

Per-trial PLI sits at its shuffled floor in every window; concatenated PLI is slightly above it. Now the eeg_blocks notebook.

**Agent calls Bash**

```bash
cd entries/001683-gao-2026; $TMPDIR/venv/bin/python - <<'EOF'
import json
d=json.load(open("eeg_blocks.ipynb"))
for i,c in enumerate(d["cells"]):
    print(f"#### [{i}] {c['cell_type']} {c.get('metadata',{}).get('tags')}")
    print("".join(c["source"]))
EOF
```

```
#### [0] markdown None
# Gao et al. (2026) on dandiset 001683: band power, asymmetry index and seizure PLI

Paper. Gao H, Frake A, Durand DM, He B (2026). Transcranial focused ultrasound stimulation
targeting white matter inhibits seizures in a rat model of epilepsy. *IEEE Trans Neural Syst Rehabil
Eng* 34, 251-259. [doi:10.1109/tnsre.2025.3644273](https://doi.org/10.1109/tnsre.2025.3644273). The
claims file was written from the NIH author manuscript (PMC12848950) and the supplement.

Dandiset. [DANDI:001683](https://dandiarchive.org/dandiset/001683/0.260109.2104), version
0.260109.2104, the only published version (the paper cites none; see `seizure_metrics.ipynb`).

This notebook streams all 70 labelled EEG blocks (2.9 GB each, about 205 GB) once and reduces each
as it loads (`tfus.process_block`): the Welch PSD of the two labelling channels (8 and 25, Fig. S1)
after a common average reference and a 60 Hz notch, over the whole block and over the seizure
periods; 30 to 80 Hz power in 1 s bins for the clock check of the labels; and the phase lag index
over the seizure periods for every pair of one ipsilateral and one contralateral channel. It takes
about 13 minutes with four processes.

| Claim | Tested here |
|---|---|
[... 422 more lines not kept]
```

**Agent**

Now the pre-4-AP check (verifier point 4). First the timing of the PLV recordings against each rat's first labelled block.

**Agent calls Bash**

```bash
cd entries/001683-gao-2026; PYTHONPATH=. $TMPDIR/venv/bin/python - <<'EOF'
import pickle, tfus, pandas as pd, numpy as np, time
t=time.time()
assets=tfus.list_assets(); big=assets[assets["size"]>2e9]
lab=[m for m in tfus.read_all_meta(big.asset_id.tolist()) if m["kind"]=="Labeled_data"]
pickle.dump(lab,open("/tmp/claude-1001/lab.pkl","wb")); print(time.time()-t)
ep,plv,metas=pickle.load(open("/tmp/claude-1001/metas.pkl","rb"))
blocks=tfus.assign_blocks(lab)
first=blocks[blocks.order==0].set_index("subject")
for m in plv:
    s=m["subject"]
    if s not in first.index: print(s,"no blocks"); continue
    t0=pd.Timestamp(m["start"]); t1=t0+pd.Timedelta(seconds=m["n_samples"]/m["rate"])
    b=pd.Timestamp(first.loc[s,"start"])
    # all recordings of this rat in time order
    allr=sorted([(pd.Timestamp(x["start"]),x["kind"],x["label"]) for x in metas+lab if x["subject"]==s])
    idx=[i for i,r in enumerate(allr) if r[2]==m["label"]][0]
    print(s, first.loc[s,"group"], "PLV end -> baseline start: %.1f min"%((b-t1).total_seconds()/60), "next rec:", allr[idx+1][1:], "prev:", allr[idx-1][1:] if idx else None)
EOF
```

```
43.400803327560425
BH624 tFUS PLV end -> baseline start: 127.8 min next rec: ('Labeled_data', 'BH624_BASELINE') prev: ('EP data', 'BH624_DEEP1mm_1500_15')
BH626 tFUS PLV end -> baseline start: 107.5 min next rec: ('Labeled_data', 'BH626_BASELINE') prev: ('EP data', 'BH626_LSIDE05mm_1500_15')
BH634 tFUS PLV end -> baseline start: 65.1 min next rec: ('Labeled_data', 'BH634_BASELINE') prev: ('EP data', 'BH634_1500_RSIDE05mm')
BH635 sham PLV end -> baseline start: 172.5 min next rec: ('Labeled_data', 'BH635_BASELINE') prev: ('EP data', 'BH635_1500_RSIDE05mm')
BH645 no blocks
BH646 tFUS PLV end -> baseline start: 86.3 min next rec: ('Labeled_data', 'BH646_BASELINE') prev: ('EP data', 'BH646_1500_200_67_S1')
BH647 no blocks
BH648 no blocks
BH649 sham PLV end -> baseline start: 87.9 min next rec: ('Labeled_data', 'BH649_BASELINE') prev: ('EP data', 'BH649_1500_RSIDE05mm')
BH650 tFUS PLV end -> baseline start: 89.8 min next rec: ('Labeled_data', 'BH650_BASELINE') prev: ('EP data', 'BH650_1500_RSIDE05mm')
BH651 no blocks
BH652 no blocks
BH653 tFUS PLV end -> baseline start: 72.2 min next rec: ('Labeled_data', 'BH653_BASELINE') prev: ('EP data', 'BH653_1500_RSIDE05mm')
BH659 sham PLV end -> baseline start: 143.9 min next rec: ('Labeled_data', 'BH659_BASELINE') prev: ('EP data', 'BH659_1500_RSIDE05mm')
BH660 tFUS PLV end -> baseline start: 70.3 min next rec: ('Labeled_data', 'BH660_BASELINE') prev: ('EP data', 'BH660_1500_RSIDE05mm')
BH661 no blocks
BH662 sham PLV end -> baseline start: 71.0 min next rec: ('Labeled_data', 'BH662_BASELINE') prev: ('EP data', 'BH662_1500_200_67_RSIDE05mm')
BH663 sham PLV end -> baseline start: 175.6 min next rec: ('Labeled_data', 'BH663_BASELINE') prev: ('EP data', 'BH663_1500_RSIDE05mm')
BH665 sham PLV end -> baseline start: 64.0 min next rec: ('Labeled_data', 'BH665_BASELINE') prev: ('EP data', 'BH665_1500_RSIDE05mm')
[... 1 more lines not kept]
```

**Agent**

The PLV recording ends 64 to 176 min before each of the 13 rats' baseline block, so it precedes the monitoring block and the first injection. Adding a helper to analyse it between pulses.

**Agent calls Bash**

```bash
cd entries/001683-gao-2026; cat >> tfus.py <<'EOF'


# ---------------------------------------------------------------- pre-4-AP state (Figs. S5 and S7)

PRE_SKIP, PRE_GUARD = 0.25, 0.02      # s after each pulse onset left out, and before the next onset


def pre_state(meta: dict) -> dict:
    """Band power of channels 8 and 25 and the PLI of every ipsilateral-contralateral pair in a PLV EEG
    recording, the last recording before the first 4-AP injection (it ends 64 to 176 min before the
    baseline block, so before the monitoring block that the first injection opens, Fig. 1E). The
    recording carries a 20 ms pulse every 2 s (every 1 s in one file); the pre-4-AP state is read from
    the gaps between pulses, from PRE_SKIP after one onset to PRE_GUARD before the next (an assumption:
    the paper's own pre-4-AP baseline is not in the dandiset), and, as a variant, from the whole
    recording.

    Same preprocessing as `process_block`: common average reference, 60 Hz notch; PSD of the gaps by a
    Hann periodogram of each gap (all cut to the shortest gap) averaged, PSD of the whole recording by
    Welch with 2 s windows; PLI on the signal decimated by 3, notched and filtered 3-300 Hz, band
    filtered and Hilbert transformed over the whole recording, then over the concatenated gap samples
    (`concat`) and per gap averaged (`per_gap`)."""
    n = meta["n_samples"]
    x = read_rows(meta, 0, n)
    x = x - x.mean(axis=1, keepdims=True)
    on = np.sort(meta["intervals"].start.to_numpy())
    spacing = float(np.median(np.diff(on)))
    nxt = np.append(on[1:], on[-1] + spacing)
    gaps = [(int((a + PRE_SKIP) * RATE), int((b - PRE_GUARD) * RATE)) for a, b in zip(on, nxt)]
    gaps = [(i, j) for i, j in gaps if 0 <= i < j <= n]
    L = min(j - i for i, j in gaps)
    car2 = _notch(x[:, [IPSI_CH - 1, CONTRA_CH - 1]], RATE)
    f, pg = signal.periodogram(np.stack([car2[i:i + L] for i, _ in gaps]), RATE, window="hann", axis=1)
    out = {"asset_id": meta["asset_id"], "subject": meta["subject"], "n_gaps": len(gaps), "gap_s": L / RATE,
           "spacing_s": spacing, "psd_gaps": (f, pg.mean(axis=0)), "psd_whole": welch_segments(car2, RATE)}
    fs_d = RATE / DECIMATE
    xd = signal.resample_poly(x, 1, DECIMATE, axis=0)
    del x
    bn, an = signal.iirnotch(60.0, 30.0, fs_d)
    xd = signal.sosfiltfilt(signal.butter(4, [3, 300], btype="bandpass", fs=fs_d, output="sos"),
                            signal.filtfilt(bn, an, xd, axis=0), axis=0)
    ii = [c - 1 for c in S1_IPSI + NONS1_IPSI]
    cc = [c - 1 for c in S1_CONTRA + NONS1_CONTRA]
    gd = [(int(i / DECIMATE), int(j / DECIMATE)) for i, j in gaps]
    res = {}
    for band in BANDS:
        ph = np.angle(signal.hilbert(signal.sosfiltfilt(band_sos(band, fs_d), xd, axis=0), axis=0))
        cat = np.concatenate([ph[i:j] for i, j in gd])
        res[band] = {"concat": pli(cat[:, ii], cat[:, cc]),
                     "per_gap": np.mean([pli(ph[i:j][:, ii], ph[i:j][:, cc]) for i, j in gd], axis=0),
                     "whole": pli(ph[:, ii], ph[:, cc]), "seconds": len(cat) / fs_d}
    out["pli"] = res
    return out


def pre_states(metas: list[dict], workers: int = 4) -> dict:
    from concurrent.futures import ProcessPoolExecutor
    import multiprocessing as mp
    with ProcessPoolExecutor(workers, mp_context=mp.get_context("spawn")) as ex:
        return {r["subject"]: r for r in ex.map(pre_state, metas)}
EOF
PYTHONPATH=. $TMPDIR/venv/bin/python - <<'EOF'
import pickle,time,tfus,numpy as np
ep,plv,metas=pickle.load(open("/tmp/claude-1001/metas.pkl","rb"))
t=time.time(); r=tfus.pre_state(plv[0]); print(time.time()-t, r["n_gaps"], r["gap_s"], r["spacing_s"])
f,p=r["psd_gaps"]; pw=tfus.band_powers(f,p); print({b:((pw[b][0]-pw[b][1])/(pw[b][0]+pw[b][1])).round(3) for b in tfus.BANDS})
f,p=r["psd_whole"]; pw=tfus.band_powers(f,p); print({b:((pw[b][0]-pw[b][1])/(pw[b][0]+pw[b][1])).round(3) for b in tfus.BANDS})
for b in tfus.BANDS: print(b, {k: tfus.pair_means(r["pli"][b][k]) for k in ("concat","per_gap","whole")})
EOF
```

```
28.88017964363098 250 1.72982272 1.9999948800000027
{'theta': np.float64(0.273), 'alpha': np.float64(0.203), 'beta': np.float64(0.103), 'gamma': np.float64(-0.007)}
{'theta': np.float64(0.262), 'alpha': np.float64(0.234), 'beta': np.float64(0.074), 'gamma': np.float64(-0.016)}
theta {'concat': {'S1': 0.0718625, 'nonS1': 0.09004226641414141}, 'per_gap': {'S1': 0.2984028409090909, 'nonS1': 0.29923273358585856}, 'whole': {'S1': 0.0685398214509264, 'nonS1': 0.08683429875716352}}
alpha {'concat': {'S1': 0.07934147727272728, 'nonS1': 0.10441281565656566}, 'per_gap': {'S1': 0.2712227272727273, 'nonS1': 0.27723421717171715}, 'whole': {'S1': 0.07637750571169254, 'nonS1': 0.10581839556209313}}
beta {'concat': {'S1': 0.03928835227272727, 'nonS1': 0.07577711489898992}, 'per_gap': {'S1': 0.130121875, 'nonS1': 0.14473380681818182}, 'whole': {'S1': 0.04039482074674512, 'nonS1': 0.07722523998671618}}
gamma {'concat': {'S1': 0.026237784090909093, 'nonS1': 0.05073207070707071}, 'per_gap': {'S1': 0.08518494318181818, 'nonS1': 0.09340726010101011}, 'whole': {'S1': 0.026416088977215823, 'nonS1': 0.05015419722465643}}
```

**Agent calls Bash**

```bash
date -u
```

```
Tue Nov  3 12:04:10 UTC 2026
```

**Agent calls Bash**

```bash
cd entries/001683-gao-2026; $TMPDIR/venv/bin/python - <<'EOF'
import sys; sys.path.insert(0,"/tmp/claude-1001/nb"); from nbedit import *
p="eeg_blocks.ipynb"; d=load(p)
assert src(d,23).startswith("## figs5")
setsrc(d,23,"""## figs5-seizures-lower-ai

> During seizures (baseline block, after 4-AP) the asymmetry index is negative and differs from
> zero in every band, more than in the pre-4-AP baseline state; seizures disrupt the normal
> interhemispheric balance.

The claims file reads the pre-4-AP state as (a) the resting baseline recording of the target
confirmation or (b) the first recording before the first injection, where the dataset holds one.
Reading (a) cannot be run: the resting recordings (`EP data`, `BASELINE`) hold only the 64
intracranial channels of left S1, not the EEG. Reading (b) can, for 13 of the 16 rats (all 6 sham
and 7 of the 10 tFUS rats; BH638, BH642 and BH644 have none): each rat's EEG file labelled
`EEG data for PLV analysis` is its last recording before the first labelled block, and it ends 64
to 176 min before that block starts (table below), so before the monitoring block of about
62.5 min that the first injection opens (Fig. 1E, Methods D). The first version of this attempt
missed this and blocked the claim; the verifier found it. That recording carries a 20 ms tFUS
pulse every 2 s, so the pre-4-AP state is taken from the gaps between pulses, 250 ms after one
onset to 20 ms before the next (`tfus.pre_state`), with the whole recording as a variant. This is
an assumption: the paper's pre-4-AP baseline may have been a recording without pulses.

AI (Eq. 1, not normalized) on the band power of channels 8 and 25, and, as a second reading, on
the band over 3-300 Hz ratios (the paper calls that ratio "absolute power"; Eq. 1 says "PSD").
Seizure AI is that of the merged seizure periods of the baseline block. Rats: (a) all 16 (13 with
a pre-4-AP recording), (b) the 10 tFUS rats (7). Tests: one-sample t against 0 per band (Fig. S5
legend); seizure against pre-4-AP by paired t and by a two-way ANOVA (state by band, ordinary and
repeated measures) with Bonferroni post hoc tests per band.""")
c1 = new("code", '''# The pre-4-AP recordings: timing against each rat's first labelled block, then band power and PLI.
first = blocks[blocks.order == 0].set_index("subject")
rows = []
for m in plv:
    if m["subject"] not in first.index:
        continue
    t0 = pd.Timestamp(m["start"]); t1 = t0 + pd.Timedelta(seconds=m["n_samples"] / m["rate"])
    later = [pd.Timestamp(x["start"]) for x in lab if x["subject"] == m["subject"]]
    rows.append({"subject": m["subject"], "group": first.loc[m["subject"], "group"], "PLV start": str(t0)[:19],
                 "PLV minutes": round((t1 - t0).total_seconds() / 60, 1),
                 "min from PLV end to first block": round((pd.Timestamp(first.loc[m["subject"], "start"]) - t1).total_seconds() / 60, 1),
                 "first block is earliest labelled": pd.Timestamp(first.loc[m["subject"], "start"]) == min(later)})
PT = pd.DataFrame(rows).sort_values(["group", "subject"])
print(PT.to_string(index=False))
print("Epilepsy rats without a PLV recording:", sorted(set(blocks.subject) - set(PT.subject)))
t0 = time.time()
PRE = tfus.pre_states([m for m in plv if m["subject"] in set(PT.subject)], workers=4)
print(f"pre-4-AP state of {len(PRE)} rats in {time.time() - t0:.0f} s; gaps per recording "
      f"{min(r['n_gaps'] for r in PRE.values())} to {max(r['n_gaps'] for r in PRE.values())}, gap length "
      f"{min(r['gap_s'] for r in PRE.values()):.2f} to {max(r['gap_s'] for r in PRE.values()):.2f} s")
rows = []
for s, r in PRE.items():
    for reading in ("gaps", "whole"):
        f, p = r["psd_" + reading]
        pw = tfus.band_powers(f, p)
        for band in tfus.BANDS:
            ip, co = pw[band]
            ri, rc = ip / pw["total_3_300"][0], co / pw["total_3_300"][1]
            rows.append({"subject": s, "group": first.loc[s, "group"], "pre": reading, "band": band,
                         "ai": (ip - co) / (ip + co), "ai_ratio": (ri - rc) / (ri + rc)})
PA = pd.DataFrame(rows)
print("\\nPre-4-AP AI, mean (min to max) over the 13 rats:")
print(PA.groupby(["pre", "band"])[["ai", "ai_ratio"]].agg(["mean", "min", "max"]).round(3).to_string())''', ["claim:figs5-seizures-lower-ai"])
c2 = new("code", '''sa = ai[(ai.segment == "seizure") & (ai.block == "baseline")]
rows = []
for value in ("ai", "ai_ratio"):
    for rats, dd in (("16 rats", sa), ("10 tFUS rats", sa[sa.group == "tFUS"]),
                     ("13 rats with pre", sa[sa.subject.isin(PRE)]), ("7 tFUS rats with pre", sa[sa.subject.isin(PRE) & (sa.group == "tFUS")])):
        for band in tfus.BANDS:
            x = dd[dd.band == band][value]
            t = stats.ttest_1samp(x, 0)
            rows.append({"AI on": value, "rats": rats, "band": band, "n": len(x), "seizure AI": x.mean(), "sem": x.sem(), "t": t.statistic, "p": t.pvalue})
print("Seizure AI of the baseline block against 0 (one-sample t):")
print(pd.DataFrame(rows).round(4).to_string(index=False))
rows, verdict = [], []
for value in ("ai", "ai_ratio"):
    for pre in ("gaps", "whole"):
        for rats in ("13 rats", "7 tFUS rats"):
            pp = PA[(PA.pre == pre) & ((PA.group == "tFUS") if rats.startswith("7") else True)]
            m = pp[["subject", "band", value]].rename(columns={value: "pre"}).merge(
                sa[["subject", "band", value]].rename(columns={value: "seizure"}), on=["subject", "band"])
            long = pd.concat([m.assign(state="pre", y=m.pre), m.assign(state="seizure", y=m.seizure)])[["subject", "band", "state", "y"]]
            comps = [(band, {"state": "seizure", "band": band}, {"state": "pre", "band": band}, "bands") for band in tfus.BANDS]
            anova = {k: tfus.twoway(long, "y", "state", "band", "subject", comps, rm=(k == "repeated"))[1].set_index("comparison")
                     for k in ("ordinary", "repeated")}
            sig0, lower = {}, {}
            for band in tfus.BANDS:
                x = m[m.band == band]
                t0 = stats.ttest_1samp(x.seizure, 0); tp = stats.ttest_1samp(x.pre, 0); tr = stats.ttest_rel(x.seizure, x.pre)
                rows.append({"AI on": value, "pre": pre, "rats": rats, "band": band, "n": len(x),
                             "seizure": x.seizure.mean(), "p seizure vs 0": t0.pvalue, "pre-4-AP": x.pre.mean(), "p pre vs 0": tp.pvalue,
                             "seizure - pre": (x.seizure - x.pre).mean(), "p paired": tr.pvalue,
                             "p ANOVA ordinary": anova["ordinary"].loc[band, "p_family"], "p ANOVA repeated": anova["repeated"].loc[band, "p_family"]})
                sig0[band] = (t0.pvalue < 0.05) and x.seizure.mean() < 0
                lower[band] = {k: (p < 0.05) and (x.seizure - x.pre).mean() < 0 for k, p in
                               (("paired", tr.pvalue), ("ordinary", anova["ordinary"].loc[band, "p_family"]), ("repeated", anova["repeated"].loc[band, "p_family"]))}
            for test in ("paired", "ordinary", "repeated"):
                verdict.append({"AI on": value, "pre": pre, "rats": rats, "test": test, "seizure below 0 in all bands": all(sig0.values()),
                                "seizure below pre in": ", ".join(b for b in tfus.BANDS if lower[b][test]) or "none",
                                "reproduced": all(sig0.values()) and lower["alpha"][test] and lower["beta"][test]})
S5 = pd.DataFrame(rows)
print("\\nSeizure against pre-4-AP AI, per band (p of the ANOVA post hoc tests Bonferroni over the four bands):")
print(S5.round(4).to_string(index=False))
print("\\nCriterion per combination of readings:")
print(pd.DataFrame(verdict).to_string(index=False))''', ["claim:figs5-seizures-lower-ai"])
assert src(d,24).startswith("sa = ai[")
d["cells"][24] = c2
d["cells"].insert(24, c1)
save(d,p)
for i,c in enumerate(d["cells"]): print(i, c["cell_type"], "".join(c["source"])[:50].replace("\n"," "))
EOF
```

```
0 markdown # Gao et al. (2026) on dandiset 001683: band power
1 code import time import warnings  import matplotlib.pyp
2 code t0 = time.time() R = tfus.process_blocks(lab, work
3 markdown ## Data check  Each check of the metadata against 
4 code print("Rats per group:", blocks.groupby("group").s
5 markdown The electrode table puts channels 1 to 16 on the r
6 code rows = [] for a, r in R.items():     g = r["gamma_
7 markdown With the labels read as minutes, 30 to 80 Hz power
8 code # Per rat, hemisphere, block: band power ratios (M
9 markdown ## fig4-no-theta-alpha-gamma-power-change  > There
10 code def band_tests(df, value="ratio", bands=tfus.BANDS
11 code print("Group mean band ratios (seizure segment, 3-
12 markdown **Result: not reproduced, resting on an assumption
13 markdown ## fig4c-beta-decrease  > The beta power ratio of 
14 code wb = T4[(T4.band == "beta") & T4.comparison.isin([
15 markdown **Result: partially reproduced.** Over the whole b
16 markdown ## figs4-sham-power-no-change  > In the sham group
17 code rows = [] for (seg, tot), d in bp[bp.group == "sha
18 markdown **Result: not reproduced, resting on an assumption
19 markdown ## fig4ef-ai-increase  > The normalized asymmetry 
[... 14 more lines not kept]
```

**Agent**

Now the figs7 cells.

**Agent calls Bash**

```bash
cd entries/001683-gao-2026; $TMPDIR/venv/bin/python - <<'EOF'
import sys; sys.path.insert(0,"/tmp/claude-1001/nb"); from nbedit import *
p="eeg_blocks.ipynb"; d=load(p)
assert src(d,31).startswith("## figs7")
setsrc(d,31,"""## figs7-seizure-pli-s1-vs-non-s1

> Comparing seizures (baseline block) with the pre-4-AP baseline state, the PLI change of S1 pairs
> differs significantly from that of non-S1 pairs in every band.

The pre-4-AP state is the gaps between pulses of each rat's PLV recording, as for
figs5-seizures-lower-ai (13 of the 16 rats; reading (a) of the state cannot be run). Per rat, band
and region, the change is the seizure PLI of the baseline block minus (reading a) or over
(reading b) the pre-4-AP PLI; the seizure PLI per seizure averaged or over the concatenated seizure
samples (M6), the pre-4-AP PLI over the concatenated gap samples. The pre-4-AP PLI per gap,
averaged, is shown as well; its gaps of 1.7 s are far shorter than the seizures, so it is biased
upwards against them (see the PLI bias in `wild_type.ipynb`) and it is not used for the change.
Two-way ANOVA (region by band, ordinary and repeated measures) of the change with Bonferroni post
hoc tests of S1 against non-S1 per band; rats (a) all 13, (b) the 7 tFUS rats. Reproduced when, under
one combination, S1 is significantly higher than non-S1 in all four bands.""")
c = new("code", '''pre_pli = []
for s, r in PRE.items():
    for band in tfus.BANDS:
        for reading in ("concat", "per_gap", "whole"):
            pm = tfus.pair_means(r["pli"][band][reading])
            for region in ("S1", "nonS1"):
                pre_pli.append({"subject": s, "band": band, "pre reading": reading, "region": region, "pre": pm[region]})
pre_pli = pd.DataFrame(pre_pli)
print("Pre-4-AP PLI, mean over the 13 rats (concatenated gaps, per gap, whole recording):")
print(pre_pli.pivot_table(index=["band", "region"], columns="pre reading", values="pre").round(4).to_string())
sz = P[(P.block == "baseline")][["subject", "group", "band", "reading", "region", "pli"]]
C = sz.merge(pre_pli[pre_pli["pre reading"] == "concat"][["subject", "band", "region", "pre"]], on=["subject", "band", "region"])
C["diff"] = C.pli - C.pre
C["ratio"] = C.pli / C.pre
print("\\nSeizure PLI of the baseline block, pre-4-AP PLI and the change, mean over the 13 rats:")
print(C.groupby(["reading", "band", "region"])[["pli", "pre", "diff", "ratio"]].mean().round(4).unstack("region").to_string())
rows, verdict = [], []
for reading in ("per_seizure", "concat"):
    for norm in ("diff", "ratio"):
        for rats in ("13 rats", "7 tFUS rats"):
            dd = C[(C.reading == reading) & ((C.group == "tFUS") if rats.startswith("7") else True)]
            comps = [(band, {"region": "S1", "band": band}, {"region": "nonS1", "band": band}, "bands") for band in tfus.BANDS]
            for k in ("ordinary", "repeated"):
                post = tfus.twoway(dd, norm, "region", "band", "subject", comps, rm=(k == "repeated"))[1].set_index("comparison")
                ok = [b for b in tfus.BANDS if post.loc[b, "p_family"] < 0.05 and post.loc[b, "diff"] > 0]
                for b in tfus.BANDS:
                    rows.append({"seizure reading": reading, "change": norm, "rats": rats, "anova": k, "band": b,
                                 "S1 - nonS1": post.loc[b, "diff"], "p": post.loc[b, "p_family"]})
                verdict.append({"seizure reading": reading, "change": norm, "rats": rats, "anova": k,
                                "bands with S1 significantly higher": ", ".join(ok) or "none", "n": len(ok)})
print("\\nS1 against non-S1 change per band (Bonferroni over the four bands):")
print(pd.DataFrame(rows).round(4).to_string(index=False))
print("\\nCriterion per combination of readings:")
print(pd.DataFrame(verdict).to_string(index=False))''', ["claim:figs7-seizure-pli-s1-vs-non-s1"])
d["cells"].insert(32, c)
save(d,p)
EOF
```

```
(Bash completed with no output)
```

**Agent**

Now `ai_ratio` tests and the sign fix for fig4ef.

**Agent calls Bash**

```bash
cd entries/001683-gao-2026; $TMPDIR/venv/bin/python - <<'EOF'
import sys; sys.path.insert(0,"/tmp/claude-1001/nb"); from nbedit import *
p="eeg_blocks.ipynb"; d=load(p)
setsrc(d,20,'''# AI on the band power (`ai`) and, as a second reading (verifier, round 1), on the band over 3-300 Hz
# ratios (`ai_ratio`): the paper calls the ratio "absolute power" and Eq. 1 says "PSD".
d = ai[ai.block != "post3"].copy()
rows, bases = [], []
for value in ("ai", "ai_ratio"):
    base = d[d.block == "baseline"].groupby(["segment", "band", "group"])[value].mean().rename("base")
    dv = d.join(base, on=["segment", "band", "group"])
    dv["norm_div"] = dv[value] / dv.base
    dv["norm_sub"] = dv[value] - dv.base
    bases.append(base.rename(value))
    for seg in ("block", "seizure"):
        for norm in ("norm_div", "norm_sub"):
            for band in tfus.BANDS:
                dd = dv[(dv.segment == seg) & (dv.band == band)]
                for k, (table, post) in tfus.group_block_tests(dd, norm).items():
                    for r in post.itertuples():
                        rows.append({"value": value, "segment": seg, "norm": norm, "band": band, "anova": k, "comparison": r.comparison,
                                     "family": r.family, "diff": r.diff, "p_family": r.p_family, "p_all": r.p_all,
                                     "tFUS base": base.loc[(seg, band, "tFUS")]})
    if value == "ai":
        print("Group means of normalized AI (AI on band power):")
        print(dv.groupby(["segment", "band", "group", "block"])[["norm_div", "norm_sub"]].mean().unstack().round(3).to_string())
TA = pd.DataFrame(rows)
print("\\nGroup mean baseline AI, on band power and on band ratios (its sign decides what an increase means under division):")
print(pd.concat(bases, axis=1).unstack().round(4).to_string())''')
setsrc(d,21,'''def ai_verdict(t):
    # "increase", two readings: the normalized value rises above its baseline (baseline minus block < 0),
    # or the AI itself rises; they agree under subtraction and are opposite under division when the
    # group's baseline AI is negative (then a rising AI gives a falling ratio).
    up_norm, up_ai = {}, {}
    for band in ("theta", "alpha"):
        x = t[(t.band == band) & t.comparison.str.startswith("tFUS baseline") & (t.p_family < 0.05)]
        up_norm[band] = bool((x["diff"] < 0).any())
        flip = (t.name[2] == "norm_div") & (x["tFUS base"] < 0)
        up_ai[band] = bool((np.where(flip, x["diff"] > 0, x["diff"] < 0)).any())
    between = {band: bool((t[(t.band == band) & (t.family == "between")].p_family < 0.05).any()) for band in tfus.BANDS}
    return pd.Series({**{f"norm up {k}": v for k, v in up_norm.items()}, **{f"AI up {k}": v for k, v in up_ai.items()},
                      **{f"between {k}": v for k, v in between.items()}})

V = TA.groupby(["value", "segment", "norm", "anova"]).apply(ai_verdict)
print(V.to_string())
print("\\nSignificant comparisons (own family):")
print(TA[TA.p_family < 0.05].round(4).to_string(index=False))''')
save(d,p)
EOF
```

```
(Bash completed with no output)
```

**Agent**

Now seizure_metrics: the end-of-block check (point 8) and the BH635 ordinary variant.

**Agent calls Bash**

```bash
cd entries/001683-gao-2026; $TMPDIR/venv/bin/python - <<'EOF'
import json
d=json.load(open("seizure_metrics.ipynb"))
for i in [0,1,3,4,5,9,10,12,25,38,43,51]:
    c=d["cells"][i]; print(f"#### [{i}] {c['cell_type']} {c.get('metadata',{}).get('tags')}"); print("".join(c["source"]))
EOF
```

```
#### [0] markdown None
# Gao et al. (2026) on dandiset 001683: seizure metrics from the labels

Paper. Gao H, Frake A, Durand DM, He B (2026). Transcranial focused ultrasound stimulation
targeting white matter inhibits seizures in a rat model of epilepsy. *IEEE Trans Neural Syst Rehabil
Eng* 34, 251-259. [doi:10.1109/tnsre.2025.3644273](https://doi.org/10.1109/tnsre.2025.3644273). The
claims file was written from the NIH author manuscript (PMC12848950) and the supplement.

Dandiset. [DANDI:001683](https://dandiarchive.org/dandiset/001683/0.260109.2104), version
0.260109.2104. The paper cites no version (its Data Availability statement gives the dandiset's
address only). This is the only published version and so the most recent; the draft lists the same
318 assets and size.

This is the first of three notebooks. It tests the claims on seizure count, percent time in
seizure, seizure duration and inter-seizure interval (Figs. 2 and 3), which use only the seizure
labels the dandiset holds. `eeg_blocks.ipynb` tests the band power, asymmetry index and seizure PLI
claims (Figs. 4, 6, S4, S5, S7); `wild_type.ipynb` the evoked potentials and wild-type PLI (Fig. 5).

| Claim | Notebook | Tested here |
|---|---|---|
[... 267 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/001683-gao-2026; PYTHONPATH=. $TMPDIR/venv/bin/python - <<'EOF'
import pickle, tfus, numpy as np, pandas as pd
lab=pickle.load(open("/tmp/claude-1001/lab.pkl","rb"))
v=np.concatenate([m["intervals"][["start","stop"]].to_numpy().ravel() for m in lab])
print(v[:20])
for k in (1,2,3,4,6):
    print(k, np.mean(np.isclose(v*60*10**0, np.round(v*60,k-1)) ), np.mean(np.isclose(v, np.round(v,k))))
rows=[]
for m in lab:
    T=m["n_samples"]/tfus.RATE
    for h in ("ipsilateral","contralateral"):
        s=tfus.seizures(m,h)
        if len(s): rows.append((m["subject"],h,T-s.stop.max(), s.start.min()))
r=pd.DataFrame(rows,columns=["s","h","end_gap","first_start"]); print(r.end_gap.describe()); print(np.sort(r.end_gap)[:10]); print(np.sort(r.first_start)[:10])
EOF
```

```
[ 3.73706479  5.41314253  3.73874142  5.47820339 11.18628523 11.36406801
 11.18664021 11.36384956 19.61009152 21.22871057 19.61083972 21.2257123
 26.39550327 26.5731386  26.39638255 26.5712599  27.72130202 29.25331524
 27.72227959 29.25383953]
1 0.0354738477472812 0.005955463490419472
2 0.34464008285862247 0.05774210253754531
3 0.9544277576385293 0.5846711548420508
4 0.9955981356809943 0.9746245468669084
6 0.9984464008285863 0.9981874676333506
count     136.000000
mean      393.443482
std       407.888543
min         0.969933
25%        54.613279
50%       240.925082
75%       586.765599
max      1641.943859
Name: end_gap, dtype: float64
[ 0.9699328   0.9699328   1.21110528  1.21110528  1.27926272  1.3893632
  3.36986112  6.64764416  6.68106752 12.49968128]
[... 3 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/001683-gao-2026; $TMPDIR/venv/bin/python - <<'EOF'
s=open("tfus.py").read()
old='''def seizures(meta: dict, hemi: str) -> pd.DataFrame:
    """Seizures of one hemisphere, in seconds from the block start."""
    iv = meta["intervals"]
    s = iv[iv.tag == hemi][["start", "stop"]].sort_values("start") * MINUTES
    s["duration"] = s.stop - s.start
    T = meta["n_samples"] / RATE
    s["truncated"] = (s.start <= 1.5 / RATE) | (s.stop >= T - 1.5 / RATE)
    return s.reset_index(drop=True)'''
new='''def seizures(meta: dict, hemi: str, edge: float = 1.5 / RATE) -> pd.DataFrame:
    """Seizures of one hemisphere, in seconds from the block start. `truncated` marks a seizure that
    starts within `edge` seconds of the block start or ends within `edge` of its end (Methods C leaves
    out seizures that "started before or continued after the recording"). The labels are given to
    about 1e-6 min, finer than a sample, and the seizures cut at the start begin at exactly one sample,
    so the default is 1.5 samples; `edge=2.0` is a variant for the few last seizures that end 1 to
    1.4 s before the block end."""
    iv = meta["intervals"]
    s = iv[iv.tag == hemi][["start", "stop"]].sort_values("start") * MINUTES
    s["duration"] = s.stop - s.start
    T = meta["n_samples"] / RATE
    s["truncated"] = (s.start <= edge) | (s.stop >= T - edge)
    return s.reset_index(drop=True)'''
assert old in s; s=s.replace(old,new)
old='''def block_metrics(meta: dict, hemi: str) -> dict:
    """Seizure Count, Percent Time in Seizure, Seizure Duration and Inter-Seizure Interval (M2)."""
    s = seizures(meta, hemi)'''
new='''def block_metrics(meta: dict, hemi: str, edge: float = 1.5 / RATE) -> dict:
    """Seizure Count, Percent Time in Seizure, Seizure Duration and Inter-Seizure Interval (M2)."""
    s = seizures(meta, hemi, edge)'''
assert old in s; s=s.replace(old,new)
open("tfus.py","w").write(s)
EOF
$TMPDIR/venv/bin/python - <<'EOF'
import sys; sys.path.insert(0,"/tmp/claude-1001/nb"); from nbedit import *
p="entries/001683-gao-2026/seizure_metrics.ipynb"; d=load(p)
s=src(d,5)
s+='''
# Resolution of the labels and the distance of each hemisphere's last seizure from the block end
# (verifier, round 1: a seizure cut by the block end may not end at the last sample).
vals = real[["start", "stop"]].to_numpy().ravel()
print(f"\\nLabel values given to 4 decimals of a minute or finer: {np.mean(~np.isclose(vals, np.round(vals, 3))):.1%}; "
      f"first starts at one sample (1/{tfus.RATE:.0f} s): {int(np.isclose(real.start * 60, 1 / tfus.RATE, atol=1e-6).sum())}")
end_gap = (real.n_samples / tfus.RATE - real.stop * 60).groupby([real.asset_id, real.tag]).min()
print(f"Seconds from each block-hemisphere's last seizure end to the block end: smallest {np.sort(end_gap.to_numpy())[:8].round(2).tolist()}; "
      f"within 2 s: {int((end_gap < 2).sum())} of {len(end_gap)}; within 10 s: {int((end_gap < 10).sum())}")'''
setsrc(d,5,s)
save(d,p)
EOF
```

```
(Bash completed with no output)
```

**Agent calls Bash**

```bash
cd entries/001683-gao-2026; $TMPDIR/venv/bin/python - <<'EOF'
import sys; sys.path.insert(0,"/tmp/claude-1001/nb"); from nbedit import *
p="seizure_metrics.ipynb"; d=load(p)
s=src(d,9)
old='''def metrics_table(blocks):
    rows = []
    for _, r in blocks.iterrows():
        for h in ("ipsilateral", "contralateral"):
            rows.append({"subject": r.subject, "group": r.group, "block": r.block, "hemi": h,
                         **tfus.block_metrics(M[r.asset_id], h)})
    return pd.DataFrame(rows)'''
new='''def metrics_table(blocks, edge=1.5 / tfus.RATE):
    rows = []
    for _, r in blocks.iterrows():
        for h in ("ipsilateral", "contralateral"):
            rows.append({"subject": r.subject, "group": r.group, "block": r.block, "hemi": h,
                         **tfus.block_metrics(M[r.asset_id], h, edge)})
    return pd.DataFrame(rows)'''
assert old in s; s=s.replace(old,new)
s+='''

# Variant for the durations: seizures within 2 s of either end of the block counted as cut off.
met_edge = metrics_table(blocks, edge=2.0)
print("\\nSeizures left out of the duration with a 2 s edge:", int(met_edge.n_truncated.sum()))'''
setsrc(d,9,s)
s=src(d,12)
s+='''
print("\\nVariant, seizures within 2 s of a block end left out (per-rat means):")
for k, (table, post) in sham_tests(met_edge[met_edge.group == "sham"], "duration").items():
    print(f"  [{k}] main effects:", {i: f"F={r.F:.2f}, p={r.p:.3g}" for i, r in table.iterrows()},
          "; post hoc significant (own family):", int((post.p_family < 0.05).sum()))'''
setsrc(d,12,s)
s=src(d,49)
s+='''
print("\\nVariant, seizures within 2 s of a block end left out:")
for h in ("ipsilateral", "contralateral"):
    for k, (table, post) in group_tests(met_edge, "duration", h).items():
        p = post[post.family == "within"]
        print(h, k, {r.comparison: round(r.p_family, 4) for r in p.itertuples()})'''
setsrc(d,49,s)
setsrc(d,38,'''# Variant: BH635's blocks by their labels (seizure_metrics data check). Sham comparisons and sham against
# tFUS, both ANOVA readings.
for k in ("ordinary", "repeated"):
    for value in ("count", "percent_time", "isi_gap", "duration"):
        for h in ("ipsilateral", "contralateral"):
            table, post = group_tests(met_alt, value, h)[k]
            p = post[post.comparison.str.startswith("sham baseline") | (post.family == "between")]
            print(k, value, h, {r.comparison: round(r.p_family, 4) for r in p.itertuples()})''')
save(d,p)
for i in (22,): print(src(d,i))
EOF
```

```
print("Mean percent time (rats) per hemisphere and block:")
print(s.groupby(["hemi", "block"])["percent_time"].agg(["mean", "sem"]).round(2).unstack(0).to_string())
keep = ["contra condition-post3", "contra baseline-post3", "ipsila condition-post3", "ipsila baseline-post3"]
for name, df in (("blocks in time order", s), ("variant, BH635 by labels (no post 3 for BH635)", s_alt)):
    print(f"\n{name}:")
    show(sham_tests(df, "percent_time"), keep)
```

**Agent**

Run seizure_metrics in the dev environment to see the new p values.

**Agent calls Bash**

```bash
cd entries/001683-gao-2026; uv pip install --quiet --python $TMPDIR/venv/bin/python nbconvert ipykernel nbclient 2>&1 | tail -2; mkdir -p $TMPDIR/out; time $TMPDIR/venv/bin/python -m jupyter nbconvert --to notebook --execute --ExecutePreprocessor.timeout=3000 --output-dir $TMPDIR/out seizure_metrics.ipynb 2>&1 | tail -3
```

```
[NbConvertApp] Converting notebook seizure_metrics.ipynb to notebook
[IPKernelApp] WARNING | Kernel is running over TCP without encryption. All communication (including code and outputs) is sent in plain text and is susceptible to eavesdropping. Use IPC transport or launch with kernel manager-provisioned CurveZMQ keys to enable transport encryption.
[NbConvertApp] Writing 185527 bytes to /tmp/claude-1001/out/seizure_metrics.ipynb

real	1m2.756s
user	0m14.414s
sys	0m0.771s
```

**Agent calls Bash**

```bash
cat > $TMPDIR/show.py <<'EOF'
import json, sys
d=json.load(open(sys.argv[1])); cells=[int(x) for x in sys.argv[2].split(",")] if len(sys.argv)>2 else range(len(d["cells"]))
for i in cells:
    c=d["cells"][i]
    if c["cell_type"]!="code": continue
    print(f"######## [{i}]")
    for o in c.get("outputs",[]):
        if o.get("output_type")=="stream": print("".join(o["text"]))
        elif "data" in o and "text/plain" in o["data"]: print("".join(o["data"]["text/plain"])[:3000])
        elif o.get("output_type")=="error": print("ERROR", o["ename"], o["evalue"])
EOF
$TMPDIR/venv/bin/python $TMPDIR/show.py $TMPDIR/out/seizure_metrics.ipynb 5,9,12
```

```
######## [5]
Label tags: {'ipsilateral': 970, 'contralateral': 959, 'no_seizure': 2}
Blocks with a 'no_seizure' row (start, stop): [{'subject': 'BH634', 'block': 'post2', 'start': 0.0, 'stop': 0.0}, {'subject': 'BH638', 'block': 'post2', 'start': 0.0, 'stop': 0.0}]

Largest stop time in each file, against the block length: stop/length in minutes {'count': 68.0, 'mean': 0.898, 'std': 0.11, 'min': 0.563, '25%': 0.844, '50%': 0.938, '75%': 0.986, 'max': 1.0}
Largest stop over all files: 62.71; shortest block: 62.51 min = 3750 s
So the label times are minutes: in seconds every seizure would fall in the first 63 s of a 3750 s block.
Label durations, read as minutes: 10.0 to 464.8 s, median 45.4 s; 0 under the 10 s minimum of Methods C
Rows with stop before start: 0
Seizures starting at the first sample (start below 2 samples): 6; ending at the last sample: 0
Files whose ipsilateral and contralateral counts differ: 19 of 68

Label values given to 4 decimals of a minute or finer: 41.6%; first starts at one sample (1/3052 s): 6
Seconds from each block-hemisphere's last seizure end to the block end: smallest [0.97, 0.97, 1.21, 1.21, 1.28, 1.39, 3.37, 6.65]; within 2 s: 6 of 136; within 10 s: 9

######## [9]
Rat-blocks without seizures: [{'subject': 'BH634', 'group': 'tFUS', 'block': 'post2', 'hemi': 'ipsilateral'}, {'subject': 'BH634', 'group': 'tFUS', 'block': 'post2', 'hemi': 'contralateral'}, {'subject': 'BH638', 'group': 'tFUS', 'block': 'post2', 'hemi': 'ipsilateral'}, {'subject': 'BH638', 'group': 'tFUS', 'block': 'post2', 'hemi': 'contralateral'}]
Rats left out of the inter-seizure interval: ['BH634', 'BH638'] (Methods C: two rats; Fig. 3C: N = 8 tFUS)
Truncated seizures left out of the duration: 6

[... 86 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/001683-gao-2026; $TMPDIR/venv/bin/python - <<'EOF'
import sys; sys.path.insert(0,"/tmp/claude-1001/nb"); from nbedit import *
p="seizure_metrics.ipynb"; d=load(p)
s=src(d,5)
old='''print(f"\\nLabel values given to 4 decimals of a minute or finer: {np.mean(~np.isclose(vals, np.round(vals, 3))):.1%}; "'''
new='''print(f"\\nLabel values (minutes) equal to their rounding to 3, 4 and 6 decimals: "
      f"{', '.join(f'{np.mean(np.isclose(vals, np.round(vals, k), rtol=0, atol=1e-9)):.1%}' for k in (3, 4, 6))}; "'''
assert old in s; setsrc(d,5,s.replace(old,new)); save(d,p)
t=open("tfus.py").read()
old='''out seizures that "started before or continued after the recording"). The labels are given to
    about 1e-6 min, finer than a sample, and the seizures cut at the start begin at exactly one sample,
    so the default is 1.5 samples;'''
new='''out seizures that "started before or continued after the recording"). The seizures cut at the
    start begin at exactly one sample, so the default is 1.5 samples;'''
assert old in t; open("tfus.py","w").write(t.replace(old,new))
EOF
$TMPDIR/venv/bin/python $TMPDIR/show.py $TMPDIR/out/seizure_metrics.ipynb 19,22,27,30,33,36,38,40,43,46,49
```

```
<persisted-output>
Output too large (41.9KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/00380fd7-6c6d-47a7-8b37-9f3cd67d736a/tool-results/bausg9prl.txt

Preview (first 2KB):
######## [19]
Mean count (rats) per hemisphere and block:
                   mean                       sem            
hemi      contralateral ipsilateral contralateral ipsilateral
block                                                        
baseline          18.17       18.17          3.18        3.18
condition         17.83       18.33          3.33        3.88
post1             18.17       18.00          4.06        3.92
post2             16.33       16.83          3.24        3.48
post3             16.33       16.50          3.01        3.69

Per rat (ipsilateral):
block    baseline  condition  post1  post2  post3
subject                                          
BH635          14         34     34     30     33
BH649          22         14     13     10     11
[... 21 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR; grep -v "^\s*$" /home/runner/.claude/projects/-home-runner-work-encore-encore/00380fd7-6c6d-47a7-8b37-9f3cd67d736a/tool-results/bausg9prl.txt | sed -n 30,400p | grep -v "^ *\(sham\|tFUS\) baseline-\(condition\|post\)" | head -300
```

```
condition         24.23       24.89          6.25        6.96
post1             22.24       20.60          5.73        4.28
post2             17.56       16.43          3.50        2.96
post3             15.54       15.32          3.25        3.67
blocks in time order:
  [ordinary] main effects: {'C(hemi, Sum)': 'F=0.07, p=0.786', 'C(block, Sum)': 'F=1.75, p=0.153', 'C(hemi, Sum):C(block, Sum)': 'F=0.02, p=0.999'}
            comparison family    diff   stat  p_raw  p_family  p_all
 ipsila baseline-post3 blocks  8.6809 1.3373 0.1872       1.0    1.0
ipsila condition-post3 blocks  9.5664 1.4737 0.1468       1.0    1.0
 contra baseline-post3 blocks 10.1091 1.5573 0.1257       1.0    1.0
contra condition-post3 blocks  8.6947 1.3394 0.1865       1.0    1.0
  [repeated] main effects: {'C(hemi, Sum)': 'F=0.33, p=0.568', 'C(block, Sum)': 'F=7.77, p=7.53e-05', 'C(hemi, Sum):C(block, Sum)': 'F=0.11, p=0.98'}
            comparison family    diff   stat  p_raw  p_family  p_all
 ipsila baseline-post3 blocks  8.6809 2.8146 0.0072    0.1444 0.1805
ipsila condition-post3 blocks  9.5664 3.1017 0.0033    0.0664 0.0829
 contra baseline-post3 blocks 10.1091 3.2777 0.0020    0.0404 0.0505
contra condition-post3 blocks  8.6947 2.8191 0.0071    0.1427 0.1784
variant, BH635 by labels (no post 3 for BH635):
  [ordinary] main effects: {'C(hemi, Sum)': 'F=0.03, p=0.869', 'C(block, Sum)': 'F=2.83, p=0.0346', 'C(hemi, Sum):C(block, Sum)': 'F=0.02, p=0.999'}
            comparison family    diff   stat  p_raw  p_family  p_all
[... 274 more lines not kept]
```

**Agent calls Bash**

```bash
F=/home/runner/.claude/projects/-home-runner-work-encore-encore/00380fd7-6c6d-47a7-8b37-9f3cd67d736a/tool-results/bausg9prl.txt; grep -n "^######\|^ipsilateral:\|^contralateral:\|\[repeated\]\|\[ordinary\]\|tFUS baseline-\|^==== \|^ipsilateral \|^contralateral \|Variant\|Bonferroni" $F | grep -v "sham baseline" | sed -n 1,400p | grep -v "^[0-9]*:\(ipsilateral\|contralateral\) \(ordinary\|repeated\) {'sham" | head -150
```

```
1:######## [19]
22:[ordinary] main effects: {'C(hemi, Sum)': 'F=0.01, p=0.929', 'C(block, Sum)': 'F=0.13, p=0.972', 'C(hemi, Sum):C(block, Sum)': 'F=0.00, p=1'} ; significant post hoc: 0 of 25; smallest p (own family) 1
23:[repeated] main effects: {'C(hemi, Sum)': 'F=0.02, p=0.877', 'C(block, Sum)': 'F=0.38, p=0.821', 'C(hemi, Sum):C(block, Sum)': 'F=0.01, p=1'} ; significant post hoc: 0 of 25; smallest p (own family) 1
27:Variant, BH635 blocks by their labels: {'ordinary': 'block p=0.656, smallest post hoc p 1', 'repeated': 'block p=0.612, smallest post hoc p 1'}
29:######## [22]
42:  [ordinary] main effects: {'C(hemi, Sum)': 'F=0.07, p=0.786', 'C(block, Sum)': 'F=1.75, p=0.153', 'C(hemi, Sum):C(block, Sum)': 'F=0.02, p=0.999'}
48:  [repeated] main effects: {'C(hemi, Sum)': 'F=0.33, p=0.568', 'C(block, Sum)': 'F=7.77, p=7.53e-05', 'C(hemi, Sum):C(block, Sum)': 'F=0.11, p=0.98'}
57:  [ordinary] main effects: {'C(hemi, Sum)': 'F=0.03, p=0.869', 'C(block, Sum)': 'F=2.83, p=0.0346', 'C(hemi, Sum):C(block, Sum)': 'F=0.02, p=0.999'}
63:  [repeated] main effects: {'C(hemi, Sum)': 'F=0.10, p=0.751', 'C(block, Sum)': 'F=6.69, p=0.00028', 'C(hemi, Sum):C(block, Sum)': 'F=0.08, p=0.988'}
70:######## [27]
74:contralateral      -27.0  -47.2  -50.3
75:ipsilateral        -24.1  -46.2  -49.4
79:contralateral      -10.5  -41.4  -42.4
80:ipsilateral         -8.7  -36.4  -41.9
85:contralateral baseline   18.17  15.9  3.18  2.24     6   10
89:ipsilateral   baseline   18.17  15.8  3.18  2.11     6   10
94:ipsilateral:
96:  [ordinary] main effects: {'C(group, Sum)': 'F=14.97, p=0.000287', 'C(block, Sum)': 'F=2.07, p=0.115', 'C(group, Sum):C(block, Sum)': 'F=0.85, p=0.47'}
101:tFUS baseline-condition  within  3.8000  1.2560 0.2143    1.0000 1.0000
102:    tFUS baseline-post1  within  7.3000  2.4128 0.0191    0.1148 0.1913
[... 130 more lines not kept]
```

**Agent calls Bash**

```bash
F=/home/runner/.claude/projects/-home-runner-work-encore-encore/00380fd7-6c6d-47a7-8b37-9f3cd67d736a/tool-results/bausg9prl.txt; sed -n '/######## \[46\]/,$p' $F | grep -v "^\s*$" | grep -v "sham-tFUS"
```

```
Permission for this tool use was denied. It requires approval, and this session has no approval surface — nobody can answer a permission prompt here — so it was denied automatically. The action was NOT performed; do not claim it succeeded, and do not retry it: this action, and anything else that requires approval, will be denied the same way for the rest of this session. Tell the user what was blocked and why you needed it, then continue with the parts of the task that do not require approval. What required approval: This Bash command contains multiple operations. The following parts require approval: F=/home/runner/.claude/projects/-home-runner-work-encore-encore/00380fd7-6c6d-47a7-8b37-9f3cd67d736a/tool-results/bausg9prl.txt; sed -n '/######## \[46\]/,$p' $F, grep -v "^\s*$"
```

**Agent calls Bash**

```bash
$TMPDIR/venv/bin/python $TMPDIR/show.py $TMPDIR/out/seizure_metrics.ipynb 46,49 | grep -v "sham-tFUS" | grep -v "^\s*$" | tail -60
```

```
group                     sham   tFUS  sham  tFUS  sham tFUS
hemi          block                                         
contralateral baseline   56.85  61.00  9.37  5.79     6   10
              condition  48.88  49.15  4.03  4.53     6   10
              post1      43.29  49.59  2.78  3.15     6   10
              post2      40.60  49.88  1.74  4.79     6    8
ipsilateral   baseline   53.00  59.84  8.91  6.02     6   10
              condition  48.55  48.52  3.49  4.78     6   10
              post1      43.85  48.00  3.52  3.24     6   10
              post2      37.78  48.73  2.07  4.71     6    8
ipsilateral:
  [ordinary] main effects: {'C(group, Sum)': 'F=2.11, p=0.152', 'C(block, Sum)': 'F=2.52, p=0.0679', 'C(group, Sum):C(block, Sum)': 'F=0.38, p=0.765'}
             comparison  family     diff    stat  p_raw  p_family  p_all
sham baseline-condition  within   4.4504  0.5463 0.5871    1.0000 1.0000
    sham baseline-post1  within   9.1566  1.1239 0.2660    1.0000 1.0000
    sham baseline-post2  within  15.2199  1.8681 0.0672    0.4030 0.6717
tFUS baseline-condition  within  11.3168  1.7933 0.0785    0.4712 0.7853
    tFUS baseline-post1  within  11.8388  1.8760 0.0661    0.3964 0.6607
    tFUS baseline-post2  within  11.1085  1.6596 0.1028    0.6168 1.0000
  [repeated] main effects: {'C(group, Sum)': 'F=1.45, p=0.248', 'C(block, Sum)': 'F=2.88, p=0.0479', 'C(group, Sum):C(block, Sum)': 'F=0.43, p=0.736'}
[... 40 more lines not kept]
```

**Agent calls Bash**

```bash
$TMPDIR/venv/bin/python $TMPDIR/show.py $TMPDIR/out/seizure_metrics.ipynb 46
```

```
######## [46]
isi_gap ipsilateral ordinary {'sham baseline-condition': (-19.1, 1.0, 1.0), 'sham baseline-post1': (-21.1, 1.0, 1.0), 'sham baseline-post2': (-24.9, 1.0, 1.0), 'sham-tFUS post1': (-121.9, 0.0508, 0.127)}
isi_gap ipsilateral repeated {'sham baseline-condition': (-19.1, 1.0, 1.0), 'sham baseline-post1': (-21.1, 1.0, 1.0), 'sham baseline-post2': (-24.9, 1.0, 1.0), 'sham-tFUS post1': (-121.9, 0.061, 0.1524)}
isi_gap contralateral ordinary {'sham baseline-condition': (-22.1, 1.0, 1.0), 'sham baseline-post1': (-22.7, 1.0, 1.0), 'sham baseline-post2': (-30.5, 1.0, 1.0), 'sham-tFUS post1': (-140.1, 0.0268, 0.067)}
isi_gap contralateral repeated {'sham baseline-condition': (-22.1, 1.0, 1.0), 'sham baseline-post1': (-22.7, 1.0, 1.0), 'sham baseline-post2': (-30.5, 1.0, 1.0), 'sham-tFUS post1': (-140.1, 0.0368, 0.092)}
isi_onset ipsilateral ordinary {'sham baseline-condition': (-14.5, 1.0, 1.0), 'sham baseline-post1': (-11.4, 1.0, 1.0), 'sham baseline-post2': (-9.7, 1.0, 1.0), 'sham-tFUS post1': (-124.0, 0.0575, 0.1437)}
isi_onset ipsilateral repeated {'sham baseline-condition': (-14.5, 1.0, 1.0), 'sham baseline-post1': (-11.4, 1.0, 1.0), 'sham baseline-post2': (-9.7, 1.0, 1.0), 'sham-tFUS post1': (-124.0, 0.0655, 0.1639)}
isi_onset contralateral ordinary {'sham baseline-condition': (-14.1, 1.0, 1.0), 'sham baseline-post1': (-11.0, 1.0, 1.0), 'sham baseline-post2': (-14.7, 1.0, 1.0), 'sham-tFUS post1': (-142.8, 0.0292, 0.073)}
isi_onset contralateral repeated {'sham baseline-condition': (-14.1, 1.0, 1.0), 'sham baseline-post1': (-11.0, 1.0, 1.0), 'sham baseline-post2': (-14.7, 1.0, 1.0), 'sham-tFUS post1': (-142.8, 0.0383, 0.0958)}
```

**Agent**

seizure_metrics numbers are in. Now running the two long notebooks in the dev env; checking resources first.

**Agent calls Bash**

```bash
nproc; free -g | head -2; date -u
```

```
4
               total        used        free      shared  buff/cache   available
Mem:              15           1          11           0           3          14
Tue Nov  3 12:07:55 UTC 2026
```

**Agent calls Bash**

```bash
cd entries/001683-gao-2026; time $TMPDIR/venv/bin/python -m jupyter nbconvert --to notebook --execute --ExecutePreprocessor.timeout=3600 --output-dir $TMPDIR/out wild_type.ipynb 2>&1 | grep -v WARNING | tail -3
```

```
[NbConvertApp] Converting notebook wild_type.ipynb to notebook
[NbConvertApp] Writing 136982 bytes to /tmp/claude-1001/out/wild_type.ipynb

real	12m0.852s
user	17m24.533s
sys	3m21.180s
```

**Agent**

Start eeg_blocks in the dev env while I read the wild_type outputs.

**Agent calls Bash**

```bash
cd entries/001683-gao-2026; (nohup $TMPDIR/venv/bin/python -m jupyter nbconvert --to notebook --execute --ExecutePreprocessor.timeout=5400 --output-dir $TMPDIR/out eeg_blocks.ipynb > $TMPDIR/eeg.log 2>&1 &); $TMPDIR/venv/bin/python $TMPDIR/show.py $TMPDIR/out/wild_type.ipynb 8,9,10,13,15
```

```
######## [8]
evoked potentials of 201 stimulated recordings and 23 resting recordings in 240 s
Sham onsets per rat (every 2 s): {'BH624': 122, 'BH626': 150, 'BH634': 150, 'BH635': 150, 'BH638': 150, 'BH642': 150, 'BH644': 150, 'BH645': 150, 'BH646': 150, 'BH647': 150, 'BH648': 150, 'BH649': 150, 'BH650': 150, 'BH651': 151, 'BH653': 150, 'BH659': 150, 'BH660': 150, 'BH662': 150, 'BH663': 150, 'BH665': 150, 'BH652': 175, 'BH661': 150, 'BH666': 150}

######## [9]
Position with the largest channel-mean EP peak (reading b): {'BACK1mm': 5, 'FRONT1mm': 4, 'RSIDE05mm': 3, 'LSIDE05mm': 3, 'SHALLOW1mm': 3, 'CENTER': 2, 'FRONT05mm': 1, 'DEEP1mm': 1, 'BACK05mm': 1}
Same, picked on the odd trials: {'DEEP1mm': 4, 'SHALLOW1mm': 4, 'FRONT1mm': 4, 'BACK1mm': 3, 'BACK05mm': 3, 'CENTER': 2, 'RSIDE05mm': 1, 'LSIDE05mm': 1, 'FRONT05mm': 1} ; same position as reading (b) in 12 of 23 rats

      position    sham onsets    anova  mean of 64: significant time points  of  first (ms)  smallest p  channels with any significant point
        CENTER      every 2 s ordinary                                    0 610         NaN     1.00000                                    1
        CENTER      every 2 s repeated                                    0 610         NaN     1.00000                                   12
        CENTER         random ordinary                                   13 610        66.5     0.01311                                   39
        CENTER         random repeated                                   26 610        64.2     0.00067                                   55
        CENTER file intervals ordinary                                    0 610         NaN     1.00000                                    3
        CENTER file intervals repeated                                    0 610         NaN     0.43929                                   22
       largest      every 2 s ordinary                                    0 610         NaN     1.00000                              
[... 109 more lines not kept]
```

**Agent calls Bash**

```bash
$TMPDIR/venv/bin/python $TMPDIR/show.py $TMPDIR/out/wild_type.ipynb 6,18 | head -120
```

```
######## [6]
EP files, interval stop - start: 2.2000 to 2.2000 s; start spacing: [2.0, 2.5]
PLV files, interval stop - start: 2.2000 to 2.2000 s; start spacing: [1.0, 2.0]

subject position LFP RMS 0-70 ms / rest (uV)  LFP RMS peak lag (ms)  1.4-1.5 kHz power 0-70 ms / rest  1.4-1.5 kHz peak lag (ms)
  BH624 BASELINE                 3.57 / 5.30                   1440                             0.981                       1130
  BH626 BASELINE                8.42 / 10.49                    130                             1.009                        120
  BH634 BASELINE                 4.61 / 4.28                   1310                             1.008                        640
  BH635 BASELINE                 3.46 / 5.07                    910                             0.992                       1470
  BH638 BASELINE                 4.21 / 6.03                    330                             1.064                       1910
  BH642 BASELINE                 7.89 / 9.99                   1560                             0.990                        530
  BH644 BASELINE                 2.35 / 3.42                   1640                             0.994                        700
  BH645 BASELINE                 3.90 / 3.66                   1450                             0.996                       1800
  BH646 BASELINE                 4.38 / 4.39                    -80                             1.015                       1630
  BH647 BASELINE                 4.49 / 2.98                   1600                             0.997                       1680
  BH648 BASELINE                 4.45 / 5.80                   1520                             1.001                       1760
  BH649 BASELINE                 6.64 / 5.04                    640                             0.978                        740
  BH650 BASELINE                 6.00 / 5.93                   1770                             0.869                        820
  BH651 BASELINE     
[... 82 more lines not kept]
```

**Agent**

While eeg_blocks runs, I'll rewrite the wild_type conclusions to match the new numbers.

**Agent calls Bash**

```bash
cd entries/001683-gao-2026; $TMPDIR/venv/bin/python - <<'EOF'
import sys; sys.path.insert(0,"/tmp/claude-1001/nb"); from nbedit import *
p="wild_type.ipynb"; d=load(p)
assert src(d,11).startswith("**Result: blocked")
setsrc(d,11,"""**Result: blocked (methods_underspecified).** The readings the criterion names disagree. With the
mean over the 64 channels, two of the eighteen combinations of position, sham onsets and ANOVA find
significant time points, both with the CENTER position and random sham onsets (ordinary: 13 of 610
points from 66.5 ms, smallest Bonferroni p = 0.013; repeated measures: 26 points from 64.2 ms,
p = 0.00067); the other sixteen find none (smallest p = 0.054 to 1), including the largest-EP
position chosen on the odd trials and tested on the even ones. With each channel tested, 1 to 55
of the 64 channels have a significant point, depending on the combination. The mean channel-mean EP
at the CENTER position reaches 3.1 uV, the sham 1.7 uV. The intervals mark the burst onsets (the
1.4-1.5 kHz power peaks 10 to 60 ms after the interval start in 13 of 23 CENTER recordings and in
none of the resting ones), so the missing EP is not a misalignment. The criterion blocks the claim
when the readings disagree; which channels, which position and which sham onsets the paper used
are questions for its authors.""")
assert src(d,16).startswith("**Result: blocked")
setsrc(d,16,"""**Result: blocked (data_missing).** Without the resting-state EEG the sham part cannot be tested.
The tFUS part does not hold either once the windows are of equal length. Per trial, the PLI equals
its trial-shuffled floor in every window (gamma S1 0.625 pre, 0.613 tFUS, 0.630 post, floors 0.628,
0.615, 0.629), so it measures the window length and not coupling. Over concatenated samples the
gamma PLI changes little: S1 +0.002 in the tFUS window and -0.008 after it, non-S1 +0.005 and
-0.002, with 47% of the 256 pairs decreasing in each window. The decreases the first version of
this attempt reported in the 20 to 200 ms window (S1 -0.029, non-S1 -0.016 concatenated, 100% of
pairs per trial) were the bias of comparing 549 samples with 61: they appear again with the whole
window (`post_full`) and vanish with its 20 ms sub-windows.""")
assert src(d,19).startswith("**Result: not reproduced")
setsrc(d,19,"""**Result: not reproduced.** In no band and under no combination of readings does the S1 PLI fall
while the non-S1 PLI does not, with equal-length windows or with the whole 20 to 200 ms window. In
the 0 to 20 ms window the S1 PLI is not below pre in theta, alpha or beta under any reading
(differences +0.0002 to +0.070). After it, with 20 ms sub-windows over concatenated samples, both
regions fall slightly in alpha (S1 -0.010, non-S1 -0.014) and beta (-0.016, -0.026). The per-trial
PLI is at its trial-shuffled floor (theta 0.976 against 0.976 pre), so the per-trial reading
cannot show a change, and the concatenated PLI (0.10 to 0.18) is only 0.01 to 0.03 above its floor.""")
setsrc(d,20, src(d,20).replace("""these files. For the repeated-measures reading of the EP test the tFUS-sham comparison at each time
point is a paired t-test.""","""these files. The repeated-measures reading of the EP test adds a random intercept per rat to the
group by time point ANOVA. Short windows bias the PLI upwards, so the 20 to 200 ms window is
compared with the pre window through its nine 20 ms sub-windows, and each PLI is given with a
trial-shuffled noise floor.""").replace("""with interval tables in seconds whose starts are the burst
onsets.""","""with interval tables in seconds whose starts are the burst
onsets (1.4-1.5 kHz power, the pulse repetition frequency, peaks just after them in most CENTER
recordings). The LFP shows no clear evoked response at any lag of the 2 s cycle."""))
save(d,p)
print(src(d,20))
EOF
```

```
## Summary

A failure to reproduce here may be a failure of this attempt, not of the paper: see the reasoning
and the differences from the paper's method.

| Claim | Outcome |
|---|---|
| fig5b-tfus-evoked-potentials | blocked: methods underspecified |
| fig5cdj-wild-type-gamma-pli-decrease | blocked: data missing |
| fig5ghi-low-band-pli-s1-only | not reproduced |

The outcomes of the other nineteen claims are in `seizure_metrics.ipynb` and `eeg_blocks.ipynb`.

How the analysis differs from the paper's. The position whose bursts form the tFUS EPs is not
recorded; the CENTER recording and the position with the largest EP are both run. The wild-type
PLI uses the dandiset's PLV EEG files, recordings with 20 ms pulses, since the EEG of the
target-confirmation bursts is not in the dandiset; the Methods' "tFUS (20 ms of stimulation)" fits
these files. The repeated-measures reading of the EP test adds a random intercept per rat to the
group by time point ANOVA. Short windows bias the PLI upwards, so the 20 to 200 ms window is
compared with the pre window through its nine 20 ms sub-windows, and each PLI is given with a
[... 7 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/001683-gao-2026; $TMPDIR/venv/bin/python - <<'EOF'
import sys; sys.path.insert(0,"/tmp/claude-1001/nb"); from nbedit import *
p="wild_type.ipynb"; d=load(p)
s=src(d,19).replace("""PLI is at its trial-shuffled floor (theta 0.976 against 0.976 pre), so the per-trial reading
cannot show a change, and the concatenated PLI (0.10 to 0.18) is only 0.01 to 0.03 above its floor.""","""PLI is at its trial-shuffled floor (theta S1 pre 0.976, floor 0.976), so the per-trial reading
cannot show a change, and the concatenated PLI (0.10 to 0.20) is about 0.02 above its floor.""")
setsrc(d,19,s)
s=src(d,20).replace("cycle. The resting recordings hold no EEG, so the sham of Figs. 5E-F cannot be computed. The PLV\nEEG","cycle. The resting recordings hold no EEG, so the sham of Figs. 5E-F cannot be computed.\nThe PLV EEG")
setsrc(d,20,s); save(d,p)
EOF
tail -3 $TMPDIR/eeg.log; date -u
```

```
Tue Nov  3 12:20:38 UTC 2026
```

**Agent**

Now the seizure_metrics conclusions.

**Agent calls Bash**

```bash
cd entries/001683-gao-2026; $TMPDIR/venv/bin/python - <<'EOF'
import json
d=json.load(open("seizure_metrics.ipynb"))
for i in [14,20,23,24,28,31,34,37,41,44,47,50]:
    print(f"#### [{i}]"); print("".join(d["cells"][i]["source"]))
EOF
```

```
#### [14]
**Result: not reproduced.** The effect of block on sham seizure duration is significant under
every reading: per seizure, F = 30.45, p = 5.5e-24 (ordinary) and p = 2.4e-31 (repeated), with 12
and 13 of 25 post hoc comparisons significant; per rat, p = 0.00145 (ordinary, no post hoc
comparison significant) and p = 3.9e-05 (repeated, contralateral baseline against post 3
significant). The hemisphere effect is not significant under any reading (p = 0.16 to 0.63). Mean
durations fall from 49.6 to 53.0 s at baseline to 34.8 to 35.7 s at post 3.
#### [20]
**Result: reproduced.** No main effect is significant (block p = 0.97 ordinary and 0.82 repeated;
hemisphere p = 0.93 and 0.88) and no post hoc comparison is (smallest Bonferroni p = 1). The mean
count is 18.11 over baseline to post 1 and 16.50 over post 2 and post 3, the slight decrease the
paper describes. With BH635's blocks taken by their labels the block effect stays non-significant
(p = 0.66 and 0.61).
#### [23]
**Result: reproduced, resting on assumptions.** Under the repeated-measures reading the
contralateral comparison of baseline (reading b of "sham") with post 3 is significant (Bonferroni
p = 0.021 in its family, 0.026 over all), a decrease from 25.6% to 15.5%; condition against post 3
is not (p = 0.096). Under the ordinary reading no comparison is significant (p = 1). The result
rests on the repeated-measures reading and on taking BH635's files in time order: with BH635 by
its labels the comparison is not significant (p = 0.083).
[... 67 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/001683-gao-2026; $TMPDIR/venv/bin/python - <<'EOF'
import sys; sys.path.insert(0,"/tmp/claude-1001/nb"); from nbedit import *
p="seizure_metrics.ipynb"; d=load(p)
T={}
T[14]="""**Result: not reproduced.** The effect of block on sham seizure duration is significant under
every reading: per seizure, F = 30.45, p = 5.5e-24 (ordinary) and F = 37.48, p = 2.7e-29
(repeated), with 12 and 13 of 25 post hoc comparisons significant; per rat, p = 0.00145 (ordinary,
no post hoc comparison significant) and p = 0.00037 (repeated, contralateral baseline against
post 3 significant, p = 0.026). The hemisphere effect is not significant under any reading
(p = 0.16 to 0.63). Mean durations fall from 49.6 to 53.0 s at baseline to 34.8 to 35.7 s at
post 3. Counting the seizures that end within 2 s of a block end as cut off changes nothing (per
rat, block p = 0.0017 ordinary and 0.00043 repeated)."""
T[20]="""**Result: reproduced.** No main effect is significant (block p = 0.97 ordinary and 0.82 repeated;
hemisphere p = 0.93 and 0.88) and no post hoc comparison is (smallest Bonferroni p = 1). The mean
count is 18.11 over baseline to post 1 and 16.50 over post 2 and post 3, the slight decrease the
paper describes. With BH635's blocks taken by their labels the block effect stays non-significant
(p = 0.66 and 0.61)."""
T[23]="""**Result: reproduced, resting on assumptions.** Under the repeated-measures reading the
contralateral comparison of baseline (reading b of "sham") with post 3 is significant in its
family (Bonferroni p = 0.040), a decrease from 25.6% to 15.5%; over all 25 comparisons it is not
(p = 0.051), and condition against post 3 is not (p = 0.14). Under the ordinary reading no
comparison is significant (p = 1). The result rests on the repeated-measures reading, the family
reading and on taking BH635's files in time order: with BH635 by its labels the comparison is not
significant (p = 0.13 repeated, 0.94 ordinary)."""
T[28]="""**Result: reproduced.** Under reading (b) of M4, each rat's change from its own baseline, the six
decreases are 8.7%, 36.4% and 41.9% (ipsilateral) and 10.5%, 41.4% and 42.4% (contralateral), all
within tolerance of 9, 36, 42, 10, 41 and 42; reading (a) gives 24 to 50%, outside. Under the
repeated-measures reading baseline against post 1 and against post 2 are significant in both
hemispheres (Bonferroni p = 0.016 and 0.0087 ipsilateral, 0.011 and 0.0059 contralateral, in the
`within` family; 0.027, 0.014, 0.019 and 0.0098 over all ten). Under the ordinary reading none of
the four is significant (p = 0.057 to 0.115)."""
T[31]="""**Result: partially reproduced.** Sham against tFUS is significant at post 1 in both hemispheres
under both ANOVA readings with the `between` family (ordinary p = 0.035 ipsilateral and 0.025
contralateral; repeated 0.040 and 0.029), and at post 2 in neither (ordinary 0.057 and 0.069;
repeated 0.064 and 0.076). No sham block differs from sham baseline (p = 1 under both readings), so
the sham count is steady. Only one of post 1 and post 2 is significant, the criterion's partial
outcome. With BH635's blocks by their labels the pattern turns over (post 2 significant, 0.038 to
0.048; post 1 not, 0.055 to 0.062), still one of the two. The first version of this attempt
reported ipsilateral post 2 as significant (p = 0.046) under the repeated reading; that p came from
a normal reference in place of the t distribution (see the summary)."""
T[34]="""**Result: reproduced.** The decreases under reading (b) of M4 are 32.5% and 34.8% (stimulation),
55.5% and 55.3% (post 1), 54.9% and 55.2% (post 2), ipsilateral and contralateral, all within
tolerance; reading (a) gives 35.8% to 57.3%, also within. Under the repeated-measures reading all
six comparisons with baseline are significant (Bonferroni p from 0.0025 down to below 0.0001), so
reading (a) of "significantly" holds; under the ordinary reading post 1 and post 2 are (p = 0.008
to 0.012) and stimulation is not (p = 0.22 and 0.17)."""
T[37]="""**Result: not reproduced, resting on an assumption.** The two ANOVA readings disagree, and so do the
two family readings. Under the ordinary reading no sham block differs from baseline (smallest
Bonferroni p = 0.79). Under the repeated-measures reading, adopted here as the paper's test with
the `within` family (see the summary), contralateral post 2 differs from baseline (p = 0.034;
ipsilateral post 2 p = 0.062); over all ten comparisons it does not (p = 0.057). The sham percent
time falls from 24.0% to 16.4% (ipsilateral) and from 25.6% to 17.6% (contralateral). With BH635's
blocks by their labels, contralateral post 2 is significant under the repeated reading (p = 0.024)
and not under the ordinary one (p = 0.53)."""
T[41]="""**Result: not reproduced.** tFUS is lower than sham in all three named comparisons (by 11.4,
9.8 and 10.0 percentage points), but none is significant under either reading: contralateral
post 1 p = 0.075 (ordinary) and 0.097 (repeated), ipsilateral stimulation 0.14 and 0.16,
ipsilateral post 1 0.13 and 0.15, in the `between` family."""
T[44]="""**Result: reproduced, resting on an assumption.** With the interval read as the gap between one
seizure's end and the next one's start, and reading (b) of M4, the increases are 27.4%, 49.1% and
27.8% (ipsilateral) and 30.1%, 51.9% and 30.9% (contralateral), all within tolerance. Under the
repeated-measures reading contralateral post 1 is the only significant comparison with baseline
under both family readings (p = 0.0086 in the `within` family, 0.014 over all ten); ipsilateral
post 1 is not (0.056 and 0.093), and the other four have p = 0.70 or more. The ordinary reading
finds none (contralateral post 1 p = 0.18). The onset-to-onset reading gives increases of 12.6% to
30.6%, outside tolerance, so the outcome rests on the gap reading, which the paper's "time between
neighboring seizures" favours."""
T[47]="""**Result: partially reproduced.** Sham against tFUS at post 1 is significant in the contralateral
S1 with tFUS higher (by 140 s; ordinary p = 0.027, repeated 0.037, `between` family) and not in
the ipsilateral S1 (by 122 s; ordinary 0.051, repeated 0.061); the onset-to-onset interval gives
the same (contralateral 0.029 and 0.038, ipsilateral 0.058 and 0.066). No sham block differs from
sham baseline (p = 1), so the sham interval is steady. The claim holds in one hemisphere, the
criterion's partial outcome. The first version of this attempt reported the ipsilateral comparison
as significant (p = 0.039) under the repeated reading; that p came from a normal reference in place
of the t distribution."""
T[50]="""**Result: not reproduced.** The group means decline from baseline to post 2 in both groups
(tFUS 59.8 to 48.7 s ipsilateral and 61.0 to 49.9 s contralateral; sham 53.0 to 37.8 s and 56.8 to
40.6 s), but tFUS baseline against post 2 is not significant in either hemisphere (Bonferroni
p = 0.42 and 0.33 repeated, 0.62 and 0.59 ordinary), nor is any other within-group comparison
against baseline (smallest p = 0.16). Counting the seizures that end within 2 s of a block end as
cut off gives the same (tFUS post 2 p = 0.42 and 0.33 repeated)."""
for i,t in T.items():
    assert src(d,i).startswith("**Result"), i
    setsrc(d,i,t)
save(d,p)
EOF
tail -2 $TMPDIR/eeg.log
```

```
(Bash completed with no output)
```

**Agent calls Bash**

```bash
sleep 240; cat $TMPDIR/eeg.log | grep -v WARNING; ps aux | grep -c "[n]bconvert"; date -u
```

```
0
Tue Nov  3 12:25:32 UTC 2026
```

**Agent**

The background run did not survive; running eeg_blocks in the foreground instead.

**Agent calls Bash**

```bash
cd entries/001683-gao-2026; time $TMPDIR/venv/bin/python -m jupyter nbconvert --to notebook --execute --ExecutePreprocessor.timeout=5400 --output-dir $TMPDIR/out eeg_blocks.ipynb 2>&1 | grep -v WARNING | tail -5
```

```
[NbConvertApp] Converting notebook eeg_blocks.ipynb to notebook
[NbConvertApp] Writing 109585 bytes to /tmp/claude-1001/out/eeg_blocks.ipynb

real	24m55.174s
user	75m3.764s
sys	14m32.610s
```

**Agent calls Bash**

```bash
$TMPDIR/venv/bin/python $TMPDIR/show.py $TMPDIR/out/eeg_blocks.ipynb 2,10,14,17 | cut -c1-250
```

```
######## [2]
processed 70 blocks in 21.7 min

######## [10]
Number of significant within-group comparisons against baseline (of 12: 2 groups x 3 blocks x 2 hemispheres):
                             sig_i            sig_ii         
anova                     ordinary repeated ordinary repeated
band  segment total                                          
alpha block   total_3_300        0        0        0        0
              total_all          0        0        0        0
      seizure total_3_300        0        0        0        0
              total_all          0        0        0        0
beta  block   total_3_300        1        9        0        8
              total_all          1        9        0        9
      seizure total_3_300        0        4        0        2
              total_all          0        5        0        2
gamma block   total_3_300        0        0        0        0
              total_all          0        0        0        0
      seizure total_3_300        0        0        0        0
              total_all          0        0        0        0
[... 95 more lines not kept]
```

**Agent calls Bash**

```bash
$TMPDIR/venv/bin/python $TMPDIR/show.py $TMPDIR/out/eeg_blocks.ipynb 21,22 | cut -c1-250
```

```
######## [21]
                                    norm up theta  norm up alpha  AI up theta  AI up alpha  between theta  between alpha  between beta  between gamma
value    segment norm     anova                                                                                                                      
ai       block   norm_div ordinary          False          False        False        False          False          False         False          False
                          repeated          False          False         True         True          False          False         False          False
                 norm_sub ordinary          False          False        False        False          False          False         False          False
                          repeated           True           True         True         True          False          False         False          False
         seizure norm_div ordinary          False          False        False        False          False          False         False          False
                          repeated          False          False        False        False          False          False         False          False
                 norm_sub ordinary          False          False        False        False          False          False         False          False
                          repeated          False          False        False        False          False          False         False          False
ai_ratio block   norm_div ordinary          False          False        False        False          False          False         False          False
                          repeated          False          False        False        False          False          False         False          False
                 norm_sub ordinary          False          False        False        False          False          False         False          False
                          repeated  
[... 20 more lines not kept]
```

**Agent calls Bash**

```bash
$TMPDIR/venv/bin/python $TMPDIR/show.py $TMPDIR/out/eeg_blocks.ipynb 20 | grep -A12 "Group mean baseline AI, on"; $TMPDIR/venv/bin/python $TMPDIR/show.py $TMPDIR/out/eeg_blocks.ipynb 25,26 | cut -c1-260
```

```
Group mean baseline AI, on band power and on band ratios (its sign decides what an increase means under division):
                   ai         ai_ratio        
group            sham    tFUS     sham    tFUS
segment band                                  
block   alpha -0.6064 -0.2576  -0.0050 -0.0158
        beta  -0.6072 -0.2543  -0.0348 -0.0108
        gamma -0.6093 -0.2882  -0.0885 -0.0467
        theta -0.5845 -0.2441   0.0400 -0.0014
seizure alpha -0.6509 -0.2838  -0.0011 -0.0131
        beta  -0.6332 -0.2723  -0.0027  0.0016
        gamma -0.6313 -0.3027  -0.0583 -0.0319
        theta -0.6457 -0.2673   0.0201  0.0047

######## [25]
Seizure AI of the baseline block against 0 (one-sample t):
   AI on                 rats  band  n  seizure AI    sem       t      p
      ai              16 rats theta 16     -0.4092 0.0634 -6.4586 0.0000
      ai              16 rats alpha 16     -0.4215 0.0614 -6.8695 0.0000
      ai              16 rats  beta 16     -0.4077 0.0605 -6.7434 0.0000
      ai              16 rats gamma 16     -0.4260 0.0597 -7.1366 0.0000
[... 91 more lines not kept]
```

**Agent**

figs5 depends on what the AI is computed on: raw band power reproduces it under several readings, the band/total ratio under none. Checking the paper's AI definition.

**Agent calls Bash**

```bash
ls paper/; grep -il "asymmetry" paper/* | head
```

Result: not kept, because it reads the paper's text.

**Agent calls Grep**

```json
{
 "pattern": "asymmetry|absolute power|PSD|power ratio|AI ",
 "path": "paper/10.1109-tnsre.2025.3644273.txt",
 "output_mode": "content",
 "-i": true
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd paper; $TMPDIR/venv/bin/python - <<'EOF'
import re
t=open("10.1109-tnsre.2025.3644273.txt").read()
for k in ["absolute power","Asymmetry Index","AI =","PSD","power ratio","normalized AI","Fig. S5"]:
    for m in re.finditer(re.escape(k),t):
        print("==",k,":",t[max(0,m.start()-300):m.end()+300].replace("\n"," "))
        print()
EOF
```

```
== absolute power : x (PLI) were calculated to analyze brain activity changes induced by tFUS. CC tFUS can significantly reduce percent time in seizure, seizure duration, and seizure count, as well as increase inter-seizure interval. These effects extended up to 2 hours post-stimulation. We also observed a decrease in absolute power of the beta band and changes in the brain network, as evidenced by a decrease in synchronization and an improvement in interhemispheric balance. Our study is the first to show that white matter tFUS can significantly suppress seizures with a lasting post stimulation effect, potentially providing a 

== absolute power : on, the EEG power spectral density (PSD) was calculated within the theta (5–8 Hz), alpha (8–12 Hz), beta (12–30 Hz), and gamma (30–80 Hz) bands using the Fourier transform. The PSD values were determined using the EEG electrode closest to the burr hole within each hemisphere. We then calculated the absolute power of each frequency band by dividing the frequency-specific PSD values by the total PSD of entire spectrum. Furthermore, the asymmetry index (AI), which represents the imbalance between hemispheres, was calculated using Eq. 1 for each of the aforementioned frequency bands by taking the relative diffe

== absolute power : ses dependent on the stimulation parameters used [ 3 ], [ 12 ]. Some studies showed that increased PSD within the beta band might be related to cortical hyperexcitability [ 41 ], which is a predisposition of seizures [ 42 ] and could be used as a biomarker [ 43 ]. Our work showed a reduction in the absolute power of the beta band during and after CC tFUS, which may indicate a disruption in this pathological synchrony ( Fig. 4 ). A few studies have investigated network level changes and found that tFUS could reduce the strength of the brain network [ 6 ], [ 44 ] and modulate the nonlinear dynamics of the rec

== absolute power : at white matter tFUS can significantly inhibit acute seizures, exhibitin
[... 34 more lines not kept]
```

**Agent calls Bash**

```bash
$TMPDIR/venv/bin/python $TMPDIR/show.py $TMPDIR/out/eeg_blocks.ipynb 29,30,33 | cut -c1-220
```

```
######## [29]
    reading  norm  tFUS S1 cells below baseline (of 12)  tFUS non-S1 cells not below baseline (of 12) S1 sham-tFUS significant
per_seizure  diff                                     8                                             4                     none
per_seizure ratio                                     8                                             4                     none
     concat  diff                                     6                                             4                     none
     concat ratio                                     6                                             4                     none

Per rat, tFUS S1 PLI difference from the group baseline, per_seizure reading:
block   baseline                      condition                       post1                       post2                     
band       alpha   beta  gamma  theta     alpha   beta  gamma  theta  alpha   beta  gamma  theta  alpha   beta  gamma  theta
subject                                                                                                                     
BH624     -0.051 -0.010 -0.010 -0.064    -0.032 -0.035 -0.017 -0.069  0.064  0.023  0.027 -0.012  0.009  0.010  0.008  0.048
BH626      0.010 -0.022 -0.016  0.092    -0.052 -0.011 -0.003 -0.065 -0.013 -0.043  0.012 -0.086 -0.041 -0.037  0.012 -0.118
BH634      0.018 -0.010 -0.034 -0.037     0.040 -0.002 -0.032 -0.120 -0.049  0.092  0.032 -0.038    NaN    NaN    NaN    NaN
BH638      0.066 -0.017 -0.024  0.016     0.039 -0.016 -0.008  0.068  0.054 -0.010 -0.023 -0.013    NaN    NaN    NaN    NaN
BH642      0.095 -0.022  0.071  0.132     0.050 -0.013  0.070  0.060 -0.041  0.005 -0.019 -0.045 -0.067  0.023  0.023 -0.034
BH644     -0.068 -0.004 -0.042  0.088    -0.106 -0.001 -0.046  0.131 -0.071 -0.013 -0.045  0.044 -0.057 -0.034 -0.046 -0.040
BH646     -0.036 -0.074 -0.053 -0.041    -0.054 -0.063 -0.033 -0.079 -0.070 -0.053 -0.058 -0.091 -0.093 -0.052 -0.052 -0.084
BH650      0.025  0.04
[... 2 more lines not kept]
```

**Agent calls Bash**

```bash
$TMPDIR/venv/bin/python - <<'EOF'
import json
d=json.load(open("/tmp/claude-1001/out/eeg_blocks.ipynb"))
for i,c in enumerate(d["cells"]):
    print(i,c["cell_type"],c.get("metadata",{}).get("tags"),"".join(c["source"])[:40].replace("\n"," "))
EOF
```

```
0 markdown None # Gao et al. (2026) on dandiset 001683: 
1 code None import time import warnings  import matp
2 code None t0 = time.time() R = tfus.process_blocks
3 markdown None ## Data check  Each check of the metadat
4 code ['sanity'] print("Rats per group:", blocks.groupby(
5 markdown None The electrode table puts channels 1 to 1
6 code ['sanity'] rows = [] for a, r in R.items():     g =
7 markdown None With the labels read as minutes, 30 to 8
8 code None # Per rat, hemisphere, block: band power
9 markdown None ## fig4-no-theta-alpha-gamma-power-chang
10 code ['claim:fig4-no-theta-alpha-gamma-power-change'] def band_tests(df, value="ratio", bands=
11 code ['claim:fig4-no-theta-alpha-gamma-power-change'] print("Group mean band ratios (seizure s
12 markdown None **Result: not reproduced, resting on an 
13 markdown None ## fig4c-beta-decrease  > The beta power
14 code ['claim:fig4c-beta-decrease'] wb = T4[(T4.band == "beta") & T4.compari
15 markdown None **Result: partially reproduced.** Over t
16 markdown None ## figs4-sham-power-no-change  > In the 
17 code ['claim:figs4-sham-power-no-change'] rows = [] for (seg, tot), d in bp[bp.gro
18 markdown None **Result: not reproduced, resting on an 
19 markdown None ## fig4ef-ai-increase  > The normalized 
[... 15 more lines not kept]
```

**Agent calls Bash**

```bash
$TMPDIR/venv/bin/python $TMPDIR/show.py $TMPDIR/out/eeg_blocks.ipynb 24,32,34 | cut -c1-220
```

```
######## [24]
subject group           PLV start  PLV minutes  min from PLV end to first block  first block is earliest labelled
  BH635  sham 2024-12-13 18:58:05          7.3                            172.5                              True
  BH649  sham 2025-02-16 20:52:12          6.7                             87.9                              True
  BH659  sham 2025-02-28 19:35:14          6.7                            143.9                              True
  BH662  sham 2025-03-11 16:18:14          6.7                             71.0                              True
  BH663  sham 2025-03-13 18:20:01          6.9                            175.6                              True
  BH665  sham 2025-03-18 17:14:39          6.7                             64.0                              True
  BH624  tFUS 2024-12-03 17:20:27          8.4                            127.8                              True
  BH626  tFUS 2024-11-29 19:35:44          5.0                            107.5                              True
  BH634  tFUS 2024-12-11 19:31:27          7.4                             65.1                              True
  BH646  tFUS 2025-02-22 18:58:25          6.7                             86.3                              True
  BH650  tFUS 2025-02-18 17:58:00          6.7                             89.8                              True
  BH653  tFUS 2025-02-11 18:05:58          6.7                             72.2                              True
  BH660  tFUS 2025-03-04 18:08:40          6.7                             70.3                              True
Epilepsy rats without a PLV recording: ['BH638', 'BH642', 'BH644']

pre-4-AP state of 13 rats in 123 s; gaps per recording 199 to 300, gap length 0.73 to 1.73 s

Pre-4-AP AI, mean (min to max) over the 13 rats:
[... 127 more lines not kept]
```

**Agent**

figs7 comes out partial: S1 change exceeds non-S1 only in theta (and gamma under one reading). Getting the remaining Fig. 4 numbers for the conclusions.

**Agent calls Bash**

```bash
$TMPDIR/venv/bin/python $TMPDIR/show.py $TMPDIR/out/eeg_blocks.ipynb 11 | grep -E "theta|block|Between|none|sham|tFUS" | head -60 | cut -c1-200
```

```
block                      baseline  condition   post1   post2
alpha contralateral sham     0.1473     0.1551  0.1535  0.1575
                    tFUS     0.1416     0.1420  0.1402  0.1216
      ipsilateral   sham     0.1458     0.1557  0.1497  0.1487
                    tFUS     0.1390     0.1363  0.1356  0.1180
beta  contralateral sham     0.4955     0.4634  0.4556  0.4524
                    tFUS     0.4908     0.4833  0.4972  0.5221
      ipsilateral   sham     0.4960     0.4445  0.4290  0.4175
                    tFUS     0.4930     0.4871  0.5001  0.5181
gamma contralateral sham     0.2343     0.2311  0.2255  0.2203
                    tFUS     0.2224     0.2235  0.2238  0.2324
      ipsilateral   sham     0.2126     0.2005  0.1964  0.1916
                    tFUS     0.2091     0.2144  0.2145  0.2207
theta contralateral sham     0.0777     0.1021  0.1106  0.1166
                    tFUS     0.0945     0.0975  0.0769  0.0781
      ipsilateral   sham     0.0784     0.1169  0.1243  0.1312
                    tFUS     0.0962     0.0961  0.0776  0.0781
Group mean band ratios (whole block, 3-300 Hz total):
block                      baseline  condition   post1   post2
alpha contralateral sham     0.1502     0.1592  0.1568  0.1573
[... 17 more lines not kept]
```

**Agent**

Writing the eeg_blocks conclusions.

**Agent calls Bash**

```bash
cd entries/001683-gao-2026; $TMPDIR/venv/bin/python - <<'EOF'
import sys; sys.path.insert(0,"/tmp/claude-1001/nb"); from nbedit import *
p="eeg_blocks.ipynb"; d=load(p)
T={}
T[12]="""**Result: not reproduced, resting on an assumption.** The ANOVA readings disagree, and the M5
readings agree within each. Under the ordinary reading no within-group comparison against baseline
is significant for theta, alpha or gamma under any of the four M5 readings. Under the
repeated-measures reading, adopted as the paper's test (see the summary), the sham theta ratio
rises above baseline in 4 or 5 of the 12 comparisons under every M5 reading (ipsilateral post 2:
Bonferroni p = 0.017 over the whole block, where the 3-300 Hz ratio goes from 0.098 to 0.136, and
p = 0.0018 over the seizure periods, from 0.078 to 0.131). Alpha and gamma have none. No
between-group comparison is significant."""
T[15]="""**Result: partially reproduced.** Over the whole block under the repeated-measures reading the
tFUS beta ratio at post 1 is significantly below baseline in both hemispheres (3-300 Hz total:
p = 0.0067 ipsilateral, 0.040 contralateral; 0 Hz to Nyquist: 0.0019 and 0.018), but the condition
block is not (p = 0.19 to 0.64), although its mean is lower (ipsilateral 0.445 at baseline, 0.417
at the condition block). Over the seizure periods the beta ratio does not fall (ipsilateral 0.493,
0.487 and 0.500) and no comparison is significant. Under the ordinary reading none is."""
T[18]="""**Result: not reproduced, resting on an assumption.** Beta varies with block and hemisphere: over
the whole block the block and hemisphere effects are significant under both readings (ordinary
block p = 0.0004 and 0.0002 for the two totals, hemisphere p below 0.0001, with 4 and 5 post hoc
comparisons significant), and over the seizure periods under the repeated-measures reading (block
p = 0.0030 and 0.0025, 1 and 2 post hoc comparisons). Gamma has a hemisphere effect over the whole
block (ordinary p = 0.0037 and 0.0004) and, under the repeated reading, over the seizure periods
too (p = 0.028 and 0.013); the repeated reading also finds a theta block effect (p = 0.011 to
0.040). Under the ordinary reading over the seizure periods nothing is significant in any band
(smallest p = 0.09), so the M5 readings disagree under that ANOVA reading; under the
repeated-measures reading, the one adopted, they agree."""
T[22]="""**Result: partially reproduced.** With AI on the band power (Eq. 1), the mean baseline AI is
negative in both groups (whole block: sham -0.58 to -0.61, tFUS -0.24 to -0.29), so the two
normalizations read an increase in opposite directions. Over the whole block under the
repeated-measures reading the tFUS AI rises above baseline, toward balance, in theta and alpha
under both normalizations once the sign is read this way (subtraction: theta post 1 p = 0.050,
post 2 p = 0.010, alpha post 2 p = 0.012; division, where a rising AI is a falling ratio: theta
post 2 p = 0.0020, alpha post 2 p = 0.0005). Read literally, as the normalized value rising, only
subtraction gives it. Over the seizure periods nothing is significant. Sham against tFUS is not
significant in any band, block or combination of readings. With AI on the band ratios (the
verifier's second reading) the baseline AI is near 0 (-0.09 to +0.04), no tFUS block differs from
baseline in theta or alpha, and no group difference is significant. So only the first part of the
claim holds, under one combination of readings."""
T[26]="""**Result: reproduced, resting on assumptions.** With AI on the band power, the seizure AI of the
baseline block is negative and below 0 in every band: -0.41 to -0.43 over the 16 rats (p < 0.0001
in each band), -0.27 to -0.30 over the 10 tFUS rats (p = 0.0001 to 0.0012), and the same over the
13 and 7 rats that have a pre-4-AP recording (p < 0.0001; p = 0.004 to 0.014). It is lower than the
pre-4-AP AI of the gaps between pulses in every band, for all 13 rats (seizure - pre -0.19 to
-0.28; paired t p = 0.0006 or less; repeated-measures ANOVA p < 0.0001) and for the 7 tFUS rats
(paired p = 0.0003 to 0.022; repeated p = 0.0009 to 0.018); the whole recording gives the same.
The ordinary two-way ANOVA finds it in theta and alpha only for the 13 rats (p = 0.028 and 0.039;
beta 0.095) and in no band for the 7. The pre-4-AP AI is itself negative (-0.17 to -0.26, below 0
in every band for the 13 rats, p = 0.0007 to 0.045; for the 7 tFUS rats only in gamma, p = 0.022,
the band Fig. S5 marks). The outcome rests on two choices. (1) The pre-4-AP state is the gaps
between the 20 ms pulses of the last recording before the first injection, the only pre-4-AP EEG
in the dandiset. (2) AI is computed on the band power, as Methods E says ("the relative difference
in PSD") and the Fig. 4 legend ("calculated using PSD values"). On the band over 3-300 Hz ratios
the seizure AI is near 0 (-0.04 to +0.01) and not below 0 in any band (p = 0.08 to 0.99), and the
claim fails under every combination."""
T[30]="""**Result: not reproduced.** Per seizure and averaged (reading a of M6), the tFUS S1 PLI is below
the group's baseline in 8 of the 12 band and block cells: in theta and alpha at all three blocks,
in beta only at the condition block and in gamma only at post 1; over the concatenated seizure
samples, 6 of 12. The non-S1 PLI falls as well: it is not below baseline in only 4 of 12 cells
under every reading, where the claim needs most of the 12. No sham against tFUS comparison of S1
PLI is significant in any band or block under either ANOVA reading. So the S1 decrease holds in two
bands only, the S1 specificity fails and the group difference fails. The first version of this
attempt called this partial, as the criterion's partial clause names the first and last of these
failures; the verifier judged it not reproduced, since the non-S1 part, which the partial clause
does not cover, fails too, and this revision agrees."""
for i,t in T.items():
    assert src(d,i).startswith("**Result"), i
    setsrc(d,i,t)
c=new("markdown","""**Result: partially reproduced, resting on an assumption.** With the pre-4-AP state taken from the
gaps between pulses of the PLV recording (13 rats), the seizure PLI of the baseline block is 2 to 5
times the pre-4-AP PLI in both regions (concatenated reading: S1 0.10 to 0.24 against 0.03 to
0.08). The S1 change is larger than the non-S1 change in every band (difference reading, S1 minus
non-S1 0.006 to 0.087), but significantly so only in theta under every ANOVA and rat reading over
concatenated samples (13 rats p = 0.0067 ordinary, 0.0004 repeated; 7 tFUS rats 0.024 and 0.026),
and in theta and gamma per seizure under the repeated reading (p = 0.0017 and 0.044). Alpha and
beta never reach significance, and the ratio reading finds nothing. One or two of four bands is
the criterion's partial outcome. Unlike Fig. S7B, where seizure non-S1 is below zero, both changes
here are positive. The per-gap pre-4-AP PLI (0.09 to 0.31) is three to four times the concatenated
one, the short-window bias, so it is not used.""")
d["cells"].insert(33,c)
save(d,p)
EOF
```

```
(Bash completed with no output)
```

**Agent calls Bash**

```bash
cd entries/001683-gao-2026; $TMPDIR/venv/bin/python - <<'EOF'
import sys; sys.path.insert(0,"/tmp/claude-1001/nb"); from nbedit import *
p="eeg_blocks.ipynb"; d=load(p)
for i,c in enumerate(d["cells"]):
    s=src(d,i)
    s2=s.replace("theta post 1 p = 0.050,\npost 2","theta post 1 p = 0.0495,\npost 2").replace("(paired p = 0.0003 to 0.022; repeated p = 0.0009 to 0.018)","(paired p = 0.0003 to 0.022; repeated p = 0.018 or less)").replace("is three to four times the concatenated\none","is 1.7 to 4 times the concatenated\none")
    if s2!=s: setsrc(d,i,s2); print("fixed",i)
save(d,p)
EOF
```

```
fixed 22
fixed 26
fixed 33
```

**Agent**

Now the headers and summary cells.

**Agent calls Bash**

```bash
cd entries/001683-gao-2026; $TMPDIR/venv/bin/python - <<'EOF'
import sys; sys.path.insert(0,"/tmp/claude-1001/nb"); from nbedit import *
p="eeg_blocks.ipynb"; d=load(p)
s=src(d,0)
s=s.replace("about 13 minutes with four processes.","about 22 minutes with four processes. It also reads the 13 EEG recordings made before the first\n4-AP injection (`EEG data for PLV analysis`) for Figs. S5 and S7.")
s=s.replace("| figs5-seizures-lower-ai | blocked (data_missing): no pre-4-AP EEG in the dandiset; the tests of seizure AI against 0 are run |","| figs5-seizures-lower-ai | yes, the pre-4-AP state from the PLV recordings (13 of 16 rats) |")
s=s.replace("| figs7-seizure-pli-s1-vs-non-s1 | blocked (data_missing): no pre-4-AP EEG in the dandiset |","| figs7-seizure-pli-s1-vs-non-s1 | yes, as figs5-seizures-lower-ai |")
setsrc(d,0,s)
i=[k for k in range(len(d["cells"])) if src(d,k).startswith("## Summary")][0]
setsrc(d,i,"""## Summary

A failure to reproduce here may be a failure of this attempt, not of the paper: see the reasoning
and the differences from the paper's method.

| Claim | Outcome |
|---|---|
| fig4-no-theta-alpha-gamma-power-change | not reproduced (assumed) |
| fig4c-beta-decrease | partially reproduced |
| figs4-sham-power-no-change | not reproduced (assumed) |
| fig4ef-ai-increase | partially reproduced |
| figs5-seizures-lower-ai | reproduced (assumed) |
| fig6-epileptic-pli-s1-decrease | not reproduced |
| figs7-seizure-pli-s1-vs-non-s1 | partially reproduced (assumed) |

The outcomes of the other fifteen claims are in `seizure_metrics.ipynb` and `wild_type.ipynb`.

How the analysis differs from the paper's. No ICA is applied: which components the authors
removed is not recorded. The EEG is re-referenced to the common average and notched at 60 Hz, as
in Methods C. The labelling channels 8 and 25 are read from the drawing of Fig. S1 and the S1
channels from the notes of the dandiset's PLV files; the paper's text lists neither. The segment
analysed, the total of the band ratio and the normalization of AI and PLI are not fixed by the
paper and are run under each reading. AI is computed on the band power, as Methods E and the
Fig. 4 legend say, with AI on the band ratios shown as a second reading; the two disagree for
figs5-seizures-lower-ai. The repeated-measures ANOVA reading, a mixed model with t and F tests on
Satterthwaite degrees of freedom, is adopted where the ANOVA readings disagree on a claim of
absence, as in `seizure_metrics.ipynb`. The pre-4-AP state of Figs. S5 and S7 is taken from the
gaps between the 20 ms pulses of each rat's last recording before the first injection, which 13 of
the 16 rats have; the paper's own pre-4-AP baseline may have been a recording without pulses.
During the condition block of the tFUS rats the EEG carries the pulse responses at 1 Hz; the paper
does not say whether they were removed, and they are not.

What was found about the dataset. The seizure labels share the EEG's clock and are in minutes:
30 to 80 Hz power inside them is 2.5 to 50 times that outside, and the contrast is gone when they
are shifted by a minute or read as seconds. The EEG before the first 4-AP injection is there for 13
of the 16 rats, as the PLV recordings, which end 64 to 176 min before the baseline block; they are
not described as pre-4-AP recordings and carry tFUS pulses. The baseline AI on the band power is
strongly negative in both groups (mean contralateral band power about 1.7 (tFUS) to 4 (sham) times
the ipsilateral), and negative before 4-AP too (-0.17 to -0.26), while the AI on band ratios is near
0, so the asymmetry is in the total power of the two channels; the paper reports only AI normalized
to the baseline.""")
save(d,p)
EOF
```

```
(Bash completed with no output)
```

**Agent calls Bash**

```bash
cd entries/001683-gao-2026; $TMPDIR/venv/bin/python - <<'EOF'
import sys; sys.path.insert(0,"/tmp/claude-1001/nb"); from nbedit import *
p="seizure_metrics.ipynb"; d=load(p)
s=src(d,51)
for a,b in [("| fig3a-count-sham-vs-tfus | seizure_metrics | reproduced |","| fig3a-count-sham-vs-tfus | seizure_metrics | partially reproduced |"),
            ("| fig3c-interval-sham-vs-tfus | seizure_metrics | reproduced |","| fig3c-interval-sham-vs-tfus | seizure_metrics | partially reproduced |"),
            ("| figs5-seizures-lower-ai | eeg_blocks | blocked: data missing |","| figs5-seizures-lower-ai | eeg_blocks | reproduced (assumed) |"),
            ("| fig6-epileptic-pli-s1-decrease | eeg_blocks | partially reproduced |","| fig6-epileptic-pli-s1-decrease | eeg_blocks | not reproduced |"),
            ("| figs7-seizure-pli-s1-vs-non-s1 | eeg_blocks | blocked: data missing |","| figs7-seizure-pli-s1-vs-non-s1 | eeg_blocks | partially reproduced (assumed) |"),
            ("""repeated-measures reading, implemented here as a mixed model with a random intercept per rat, so
that reading is adopted as an assumption where the readings disagree on a claim of absence. The
Bonferroni family is not specified either; both readings are shown and no single one gives every
significance claim the paper makes.""","""repeated-measures reading, implemented here as a mixed model with a random intercept per rat, so
that reading is adopted as an assumption where the readings disagree on a claim of absence. Its
post hoc tests are t tests and its main effects F tests, on Satterthwaite degrees of freedom (on
balanced data, the df of the classical repeated-measures ANOVA, as Prism uses); the first version
of this attempt used normal and chi-squared references, which made two sham against tFUS
comparisons look significant. The Bonferroni family is not specified either; both readings are
shown. Each set of comparisons as its own family (reading i) is adopted where they disagree, as
Prism corrects each set of multiple comparisons it is asked for on its own; this decides
fig2f-sham-percent-time-post3 and fig3b-sham-percent-time-no-change. The durations leave out
seizures that start or end at a block edge; counting the six that end 1 to 1.4 s before a block
end as cut off as well changes no result.""")]:
    assert a in s, a[:40]; s=s.replace(a,b)
setsrc(d,51,s); save(d,p)
EOF
```

```
(Bash completed with no output)
```

**Agent**

Updating entry.yaml runtimes and the README, then the full run.

**Agent calls Bash**

```bash
cd entries/001683-gao-2026; sed -i 's/  runtime_minutes: 14/  runtime_minutes: 25/; s/  runtime_minutes: 8/  runtime_minutes: 12/' entry.yaml; grep runtime entry.yaml; sed -n '/| Claim | Outcome |/,$p' README.md
```

```
runtime_minutes: 1
  runtime_minutes: 25
  runtime_minutes: 12
| Claim | Outcome |
|---|---|
| Sham seizure duration does not change across blocks (Fig. 2C) | Not reproduced |
| Most sham seizures last under 2 minutes (Fig. 2D) | Reproduced |
| Sham seizure count does not change (Fig. 2E) | Reproduced |
| Sham percent time in seizure differs at post 3 (Fig. 2F) | Reproduced, on assumptions |
| tFUS reduces seizure count by 9 to 42% (Fig. 3A) | Reproduced |
| Seizure count differs between sham and tFUS at post 1 and 2 (Fig. 3A) | Reproduced |
| tFUS reduces percent time in seizure by 33 to 55% (Fig. 3B) | Reproduced |
| Sham percent time does not change (Fig. 3B) | Not reproduced, on an assumption |
| Percent time differs between sham and tFUS (Fig. 3B) | Not reproduced |
| tFUS lengthens the inter-seizure interval by 27 to 52% (Fig. 3C) | Reproduced, on an assumption |
| Interval differs between sham and tFUS at post 1 (Fig. 3C) | Reproduced |
| Seizure duration falls significantly only at tFUS post 2 (Fig. 3D) | Not reproduced |
| No change in theta, alpha, gamma power (Fig. 4) | Not reproduced, on an assumption |
| Beta power falls during and after tFUS (Fig. 4C) | Partially reproduced |
| Sham band power does not change (Fig. S4) | Not reproduced, on an assumption |
[... 27 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/001683-gao-2026; $TMPDIR/venv/bin/python - <<'EOF'
s=open("README.md").read()
for a,b in [("| Seizure count differs between sham and tFUS at post 1 and 2 (Fig. 3A) | Reproduced |","| Seizure count differs between sham and tFUS at post 1 and 2 (Fig. 3A) | Partially reproduced |"),
 ("| Interval differs between sham and tFUS at post 1 (Fig. 3C) | Reproduced |","| Interval differs between sham and tFUS at post 1 (Fig. 3C) | Partially reproduced |"),
 ("| Seizures lower the AI (Fig. S5) | Blocked: data missing |","| Seizures lower the AI (Fig. S5) | Reproduced, on assumptions |"),
 ("| Seizure PLI of S1 falls with tFUS (Fig. 6) | Partially reproduced |","| Seizure PLI of S1 falls with tFUS (Fig. 6) | Not reproduced |"),
 ("| Seizure PLI change, S1 against non-S1 (Fig. S7) | Blocked: data missing |","| Seizure PLI change, S1 against non-S1 (Fig. S7) | Partially reproduced, on an assumption |"),
 ("""assumption. The pre-4-AP EEG and the resting EEG of the wild-type phase are not in the dandiset.""","""assumption. The EEG before the first 4-AP injection is there for 13 of the 16 rats, as recordings
with tFUS pulses (the PLV files), and is read between the pulses. The resting EEG of the wild-type
phase is not in the dandiset."""),
 ("(205 GB) once, in about 14 minutes with four processes.","(205 GB) once, in about 25 minutes with four processes."),
 ("EEG (about 8 minutes).","EEG (about 12 minutes).")]:
    assert a in s, a[:50]; s=s.replace(a,b)
open("README.md","w").write(s)
EOF
date -u
```

```
Tue Nov  3 12:53:01 UTC 2026
```

**Agent**

Now the full run with the entry tool (about 40 minutes).

**Agent calls Bash**

```bash
cd  time python tools/entry.py all entries/001683-gao-2026 2>&1 | tail -30
```

```
[36mFile [39m[32m/opt/hostedtoolcache/Python/3.13.17/x64/lib/python3.13/concurrent/futures/_base.py:318[39m, in [36m_result_or_cancel[39m[34m(***failed resolving arguments***)[39m
[32m    316[39m [38;5;28;01mtry[39;00m:
[32m    317[39m     [38;5;28;01mtry[39;00m:
[32m--> [39m[32m318[39m         [38;5;28;01mreturn[39;00m [30;43mfut[39;49m[30;43m.[39;49m[30;43mresult[39;49m[30;43m([39;49m[30;43mtimeout[39;49m[30;43m)[39;49m
[32m    319[39m     [38;5;28;01mfinally[39;00m:
[32m    320[39m         fut.cancel()

[36mFile [39m[32m/opt/hostedtoolcache/Python/3.13.17/x64/lib/python3.13/concurrent/futures/_base.py:453[39m, in [36mFuture.result[39m[34m(self, timeout)[39m
[32m    451[39m     [38;5;28;01mraise[39;00m CancelledError()
[32m    452[39m [38;5;28;01melif[39;00m [38;5;28mself[39m._state == FINISHED:
[32m--> [39m[32m453[39m     [38;5;28;01mreturn[39;00m [30;43mself[39;49m[30;43m.[39;49m[30;43m__get_result[39;49m[30;43m([39;49m[30;43m)[39;49m
[32m    455[39m [38;5;28mself[39m._condition.wait(timeout)
[32m    457[39m [38;5;28;01mif[39;00m [38;5;28mself[39m._state [38;5;129;01min[39;00m [CANCELLED, CANCELLED_AND_NOTIFIED]:

[36mFile [39m[32m/opt/hostedtoolcache/Python/3.13.17/x64/lib/python3.13/concurrent/futures/_base.py:402[39m, in [36mFuture.__get_result[39m[34m(self)[39m
[32m    400[39m [38;5;28;01mif[39;00m [38;5;28mself[39m._exception [38;5;129;01mis[39;00m [38;5;129;01mnot[39;00m [38;5;28;01mNone[39;00m:
[32m    401[39m     [38;5;28;01mtry[39;00m:
[32m--> [39m[32m402[39m         [38;5;28;01mraise[39;00m [38;5;28mself[39m._exception
[32m    403[39m     [38;5;28;01mfinally[39;00m:
[32m    404[39m         [38;5;66;03m# Break a reference cycle with the exception in self._exception[39;00m
[... 13 more lines not kept]
```

**Agent calls Bash**

```bash
cd  $TMPDIR/venv/bin/python - <<'EOF'
p="entries/001683-gao-2026/tfus.py"; s=open(p).read()
old='''    def get(i):
        for _ in range(5):
            r = _session.get(meta["url"], headers={"Range": f"bytes={edges[i]}-{edges[i + 1] - 1}"}, timeout=120)
            if r.status_code == 206 and len(r.content) == edges[i + 1] - edges[i]:
                return r.content
        raise OSError(f"range read failed for {meta['asset_id']}")'''
new='''    def get(i):
        for attempt in range(8):
            try:
                r = _session.get(meta["url"], headers={"Range": f"bytes={edges[i]}-{edges[i + 1] - 1}"}, timeout=120)
                if r.status_code == 206 and len(r.content) == edges[i + 1] - edges[i]:
                    return r.content
            except requests.RequestException:          # a dropped connection is retried
                pass
            time.sleep(min(30, 2 ** attempt))
        raise OSError(f"range read failed for {meta['asset_id']}")'''
assert old in s; s=s.replace(old,new)
s=s.replace("import json\nimport warnings\n","import json\nimport time\nimport warnings\n")
open(p,"w").write(s)
EOF
grep -n "^import" entries/001683-gao-2026/tfus.py; grep -n "add_argument\|def main\|sub.add_parser\|subparsers" tools/entry.py | head -30; ls executed/001683-gao-2026/
```

```
54:import json
55:import time
56:import warnings
59:import h5py
60:import numpy as np
61:import pandas as pd
62:import remfile
63:import requests
425:def main() -> int:
428:    parser.add_argument("command", choices=["lock", "check", "run", "all", "handover"])
429:    parser.add_argument("entry", type=Path, nargs="+",
431:    parser.add_argument("--output-dir", type=Path, help="where executed notebooks go")
432:    parser.add_argument("--timeout", type=int, default=3600, help="seconds allowed per cell")
433:    parser.add_argument("--max-minutes", type=float, default=60,
eeg_blocks.ipynb
result.json
seizure_metrics.ipynb
```

**Agent**

Helper fixed. Before re-running everything, I'll write the attempt record. Checking the schema for `verifications`.

**Agent calls Bash**

```bash
cd  ls schemas; grep -n "verifications" -A60 schemas/attempt*.json | head -120; date -u
```

```
attempt.schema.json
claims.schema.json
entry.schema.json
paper-match.schema.json
334:    "verifications": {
335-      "type": "array",
336-      "items": {
337-        "type": "object",
338-        "additionalProperties": false,
339-        "required": [
340-          "date",
341-          "kind",
342-          "by",
343-          "results"
344-        ],
345-        "properties": {
346-          "date": {
347-            "type": "string",
348-            "format": "date"
349-          },
[... 46 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 394,420p schemas/attempt.schema.json; grep -l "verifications:" attempts/*.yaml | head -3; f=$(grep -l "verifications:" attempts/*.yaml | head -1); sed -n '/^verifications:/,/^[a-z]/p' $f | head -30
```

```
}
          },
          "reviewed": {
            "description": "What was reviewed, e.g. a commit, when the attempt changed afterwards.",
            "type": "string"
          }
        }
      }
    },
    "findings": {
      "description": "What the attempt found about the dataset itself, whatever the outcomes. These roll up into the per-dataset report.",
      "type": "array",
      "items": {
        "type": "object",
        "additionalProperties": false,
        "required": [
          "kind",
          "statement"
        ],
        "properties": {
[... 40 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n "agrees\|verification" tools/entry.py | head -30
```

```
279:        for rnd in (attempt.get("verifications") or [])[1:]:
281:                agreed[r["claim"]] = r.get("outcome") if r.get("agrees") else None
298:                                    f"verification agreed with {verified!r}; record the change under `proposed`, "
```

**Agent calls Bash**

```bash
cd  grep -rn "agrees" tools/*.py scripts/* 2>/dev/null | head -20
```

```
tools/build_site.py:26:verification decides, and it counts only if it agrees with every outcome.
tools/build_site.py:118:    "code_mismatch": "Published code disagrees",
tools/build_site.py:141:    agreed = {r["claim"] for r in latest.get("results", []) if r.get("agrees")}
tools/build_site.py:210:        disagreed = {r["claim"] for v in verifications for r in v["results"] if not r.get("agrees")}
tools/build_site.py:255:                "agreed": sum(1 for r in v["results"] if r.get("agrees")),
tools/build_site.py:259:                                  for r in v["results"] if not r.get("agrees")],
tools/build_site.py:1156:     "it agrees with each outcome. The author revises once more. Any change of outcome proposed after this goes to a "
tools/entry.py:281:                agreed[r["claim"]] = r.get("outcome") if r.get("agrees") else None
```

**Agent**

Writing the attempt record (outcomes, deviations, findings and the round-1 verification block).

**Agent calls Bash**

```bash
cd  cat > $TMPDIR/rec.py <<'PYEOF'
import yaml, copy
p="attempts/001683-gao-2026-01.yaml"
R=yaml.safe_load(open(p))
O={o["claim"]:o for o in R["outcomes"]}
SAT=("The repeated-measures reading of M3 is a linear mixed model with a random intercept per rat (REML), "
     "a standard stand-in for Prism's repeated-measures and mixed-effects analysis; its post hoc tests are t tests "
     "and its main effects F tests on Satterthwaite degrees of freedom, which on balanced data are those of the "
     "classical repeated-measures ANOVA.")
FAM=("Assumed that each set of post hoc comparisons is its own Bonferroni family (reading i of M3), as Prism corrects "
     "each set of multiple comparisons it is asked for on its own; the paper names no family. Reading (ii) is shown.")
def setn(c, notes, **kw):
    O[c]["notes"]=notes
    for k,v in kw.items():
        if v is None: O[c].pop(k,None)
        else: O[c][k]=v
setn("fig2c-sham-duration-stable",
 "The block effect on sham seizure duration is significant under every reading. Per seizure (1046 seizures) "
 "F = 30.45, p = 5.5e-24 ordinary and F = 37.48, p = 2.7e-29 repeated, with 12 and 13 of 25 Bonferroni post hoc "
 "comparisons significant; per rat p = 0.00145 ordinary (no post hoc comparison significant) and p = 0.00037 "
 "repeated (contralateral baseline against post 3, p = 0.026). The hemisphere effect is not significant "
 "(p = 0.16 to 0.63). Mean durations fall from 49.6 to 53.0 s at baseline to 34.8 to 35.7 s at post 3. Counting "
 "the seizures that end within 2 s of a block end as cut off gives block p = 0.0017 and 0.00043 per rat. The "
 "readings agree, so the outcome rests on none of them.")
O["fig2c-sham-duration-stable"]["deviations"][3]=SAT
setn("fig2f-sham-percent-time-post3",
 "Under the repeated-measures reading, contralateral baseline (reading b of \"sham\") against post 3 is "
 "significant in its family, Bonferroni p = 0.040, a decrease from 25.6% to 15.5%; over all 25 comparisons it is "
 "not (p = 0.051). Condition against post 3 is not (p = 0.14). Under the ordinary reading no comparison is "
 "significant (p = 1). With BH635's files taken by their labels the comparison is not significant (p = 0.13 "
 "repeated, 0.94 ordinary).")
O["fig2f-sham-percent-time-post3"]["deviations"].append(FAM+" Under reading (ii) the comparison is not significant.")
setn("fig3a-count-reduction",
 "Under reading (b) of M4 all six decreases are within tolerance. Reading (a) gives 24.1, 46.2, 49.4, 27.0, 47.2 "
 "and 50.3%, outside. Under the repeated-measures reading baseline against post 1 and post 2 are significant in "
 "both hemispheres (Bonferroni p = 0.016 and 0.0087 ipsilateral, 0.011 and 0.0059 contralateral, within family; "
 "0.027, 0.014, 0.019 and 0.0098 over all ten). Under the ordinary reading none of the four is (p = 0.057 to "
 "0.115).")
setn("fig3a-count-sham-vs-tfus",
 "Sham against tFUS is significant at post 1 in both hemispheres under both readings, between family (ordinary "
 "p = 0.035 ipsilateral and 0.025 contralateral; repeated 0.040 and 0.029), and at post 2 in neither (ordinary "
 "0.057 and 0.069; repeated 0.064 and 0.076). No sham block differs from sham baseline (p = 1). Only one of the "
 "two blocks is significant. With BH635 by its labels post 2 is significant (0.038 to 0.048) and post 1 is not "
 "(0.055 to 0.062), still one of the two.", outcome="partially_reproduced")
setn("fig3b-percent-time-reduction",
 "Reading (b) of M4 gives 32.5 and 34.8% at stimulation, 55.5 and 55.3% at post 1, 54.9 and 55.2% at post 2 "
 "(ipsilateral and contralateral; the measured values for the \"each hemisphere\" expectations are the "
 "ipsilateral ones), all within tolerance; reading (a) gives 35.8 to 57.3%, also within. Under the "
 "repeated-measures reading all six comparisons with baseline are significant (Bonferroni p from 0.0025 to below "
 "0.0001); under the ordinary reading post 1 and post 2 are (0.008 to 0.012) and stimulation is not (0.22, "
 "0.17).")
setn("fig3b-sham-percent-time-no-change",
 "The ANOVA readings disagree, and so do the family readings. Ordinary, no sham block differs from baseline "
 "(smallest Bonferroni p = 0.79). Repeated, contralateral post 2 differs in its family (p = 0.034; ipsilateral "
 "post 2 p = 0.062) and not over all ten comparisons (p = 0.057). Sham percent time falls from 24.0 to 16.4% "
 "(ipsilateral) and from 25.6 to 17.6% (contralateral). With BH635 by its labels contralateral post 2 is "
 "significant under the repeated reading (p = 0.024) and not under the ordinary one (p = 0.53).")
O["fig3b-sham-percent-time-no-change"]["deviations"]=[
 O["fig3b-sham-percent-time-no-change"]["deviations"][0].replace(
  "Under the ordinary reading the claim would be reproduced.",
  "Under the ordinary reading the claim would be reproduced."),
 FAM+" Under reading (ii) the claim would be reproduced."]
setn("fig3b-percent-time-sham-vs-tfus",
 "tFUS is lower than sham in all three named comparisons (by 11.4, 9.8 and 10.0 percentage points), but none is "
 "significant. Contralateral post 1 p = 0.075 (ordinary) and 0.097 (repeated), ipsilateral stimulation 0.14 and "
 "0.16, ipsilateral post 1 0.13 and 0.15, between family; larger over all ten comparisons.")
setn("fig3c-interval-increase",
 "Gap reading of the interval and reading (b) of M4, all six increases within tolerance. The two rats left out "
 "are BH634 and BH638 (no seizures at post 2). Under the repeated-measures reading contralateral post 1 is the "
 "only significant comparison with baseline under both family readings (p = 0.0086 within family, 0.014 over all "
 "ten; ipsilateral post 1 0.056 and 0.093, the others 0.70 or more). The ordinary reading finds none "
 "(contralateral post 1 p = 0.18). Onset-to-onset intervals give increases of 12.6 to 30.6%, outside tolerance.")
setn("fig3c-interval-sham-vs-tfus",
 "Sham against tFUS at post 1 is significant in the contralateral S1 with tFUS higher (by 140 s; ordinary "
 "p = 0.027, repeated 0.037, between family) and not in the ipsilateral S1 (by 122 s; 0.051 and 0.061); the "
 "onset-to-onset interval gives the same (contralateral 0.029 and 0.038, ipsilateral 0.058 and 0.066). No sham "
 "block differs from sham baseline (p = 1). The claim holds in one hemisphere.", outcome="partially_reproduced")
setn("fig3d-duration-decline",
 "Means decline in both groups (tFUS 59.8 to 48.7 s ipsilateral, 61.0 to 49.9 s contralateral; sham 53.0 to "
 "37.8 and 56.8 to 40.6 s), but tFUS baseline against post 2 is not significant (Bonferroni p = 0.42 and 0.33 "
 "repeated, 0.62 and 0.59 ordinary), nor is any other within-group comparison (smallest p = 0.16). Counting the "
 "seizures that end within 2 s of a block end as cut off gives the same (0.42 and 0.33).")
setn("fig4-no-theta-alpha-gamma-power-change",
 "The M5 readings agree within each ANOVA reading; the ANOVA readings disagree. Ordinary, no within-group "
 "comparison against baseline is significant for theta, alpha or gamma. Repeated, the sham theta ratio rises "
 "above baseline in 4 or 5 of 12 comparisons under every M5 reading (ipsilateral post 2 p = 0.017 over the whole "
 "block, ratio 0.098 to 0.136; p = 0.0018 over the seizure periods, 0.078 to 0.131). Alpha and gamma have none. "
 "No between-group comparison is significant.")
setn("fig4c-beta-decrease",
 "Whole block, repeated-measures reading, the tFUS beta ratio at post 1 is significantly below baseline in both "
 "hemispheres (3-300 Hz total p = 0.0067 ipsilateral and 0.040 contralateral; 0 Hz to Nyquist 0.0019 and "
 "0.018), but the condition block is not (p = 0.19 to 0.64) although its mean is lower (ipsilateral 0.445 to "
 "0.417). Over the seizure periods the beta ratio does not fall (ipsilateral 0.493, 0.487, 0.500) and nothing is "
 "significant. Under the ordinary reading nothing is significant.")
setn("figs4-sham-power-no-change",
 "Over the whole block beta has significant block and hemisphere effects under both readings (ordinary block "
 "p = 0.0004 and 0.0002 for the two totals, hemisphere p below 0.0001, 4 and 5 post hoc comparisons significant) "
 "and gamma a hemisphere effect (0.0037 and 0.0004). Over the seizure periods the repeated-measures reading finds "
 "a beta block effect (0.0030, 0.0025, 1 and 2 post hoc comparisons) and a gamma hemisphere effect (0.028, 0.013); "
 "the ordinary reading finds nothing in any band (smallest p = 0.09).")
setn("fig4ef-ai-increase",
 "With AI on the band power (Eq. 1), mean baseline AI is negative in both groups (whole block, sham -0.58 to "
 "-0.61, tFUS -0.24 to -0.29). Whole block, repeated-measures reading, the tFUS AI rises above baseline, toward "
 "balance, in theta and alpha under both normalizations when a rising AI is read as a falling ratio under "
 "division (subtraction theta post 1 p = 0.0495, post 2 p = 0.010, alpha post 2 p = 0.012; division theta post 2 "
 "p = 0.0020, alpha post 2 p = 0.0005); read as the normalized value rising, only subtraction gives it. Sham "
 "against tFUS is not significant in any band, block or combination of readings. Over the seizure periods "
 "nothing is significant. With AI on band ratios the baseline AI is -0.09 to +0.04 and neither part holds.")
O["fig4ef-ai-increase"]["deviations"]=[
 "AI is computed on the band power (sum of PSD in the band) of channels 8 and 25, as Methods E says (\"the "
 "relative difference in PSD between the ipsilateral and contralateral S1\") and the Fig. 4 legend (\"calculated "
 "using PSD values\"); AI on the band over 3-300 Hz ratios is shown as a second reading. The seizure segment is "
 "the union of both hemispheres' labels.",
 "\"Increase\" is shown in two readings, the normalized value rising and the AI rising; they differ under "
 "division when the baseline AI is negative. The outcome is the same under both.",
 "As for fig4-no-theta-alpha-gamma-power-change (no ICA)."]
f5=O["figs5-seizures-lower-ai"]
f5.update({"outcome":"reproduced","assumed":True})
f5.pop("blocked_by",None)
f5["notes"]=("With AI on the band power, seizure AI of the baseline block is negative and below 0 in every band: "
 "-0.41 to -0.43 over the 16 rats (p < 0.0001), -0.27 to -0.30 over the 10 tFUS rats (p = 0.0001 to 0.0012), and "
 "the same over the 13 and 7 rats with a pre-4-AP recording (p < 0.0001; 0.004 to 0.014). It is lower than the "
 "pre-4-AP AI of the gaps between pulses in every band, for the 13 rats (difference -0.19 to -0.28; paired t "
 "p = 0.0006 or less; repeated-measures ANOVA p < 0.0001) and the 7 tFUS rats (paired 0.0003 to 0.022; repeated "
 "0.018 or less); the whole recording gives the same. The ordinary ANOVA finds it in theta and alpha only for the "
 "13 rats (0.028, 0.039; beta 0.095) and in no band for the 7. The pre-4-AP AI is itself negative (-0.17 to "
 "-0.26; below 0 in every band for the 13 rats, p = 0.0007 to 0.045; for the 7 tFUS rats only in gamma, "
 "p = 0.022). With AI on band ratios the seizure AI is -0.04 to +0.01, not below 0 in any band (p = 0.08 to "
 "0.99), and the claim fails under every combination.")
f5["deviations"]=[
 "The pre-4-AP state is reading (b) of the claims file, the recording before the first injection. For 13 of the "
 "16 rats (6 sham, 7 tFUS; not BH638, BH642, BH644) the EEG labelled \"EEG data for PLV analysis\" is the last "
 "recording before the first labelled block and ends 64 to 176 min before it, so before the monitoring block "
 "that the first injection opens (Fig. 1E). It carries a 20 ms tFUS pulse every 2 s (1 s in one file); assumed "
 "that the gaps between pulses, 250 ms after one onset to 20 ms before the next, stand for the pre-4-AP "
 "baseline, which the paper may have recorded without pulses. The whole recording is shown as a variant. "
 "Reading (a), the resting recording of the target confirmation, holds no EEG.",
 "Assumed that AI is computed on the band power, as Methods E (\"the relative difference in PSD\") and the "
 "Fig. 4 legend (\"calculated using PSD values\") say; on the band over 3-300 Hz ratios the claim fails. Both "
 "are shown.",
 "PSD of the gaps by a Hann periodogram of each gap, all cut to the shortest gap (1.73 s; 0.73 s in the 1 s "
 "file), averaged; a standard choice."]
f6=O["fig6-epileptic-pli-s1-decrease"]
f6["outcome"]="not_reproduced"
f6["notes"]=("Per seizure and averaged, the tFUS S1 PLI is below the group's baseline in 8 of 12 band and block "
 "cells (theta and alpha at all three blocks; beta only at the condition block; gamma only at post 1); over "
 "concatenated samples 6 of 12. The non-S1 PLI falls too (not below baseline in only 4 of 12 cells under every "
 "reading), so that part fails. No sham against tFUS comparison of S1 PLI is significant under either ANOVA "
 "reading. The S1 decrease holds in two bands, the S1 specificity fails and the group difference fails; the "
 "criterion's partial clause names only the first and last of these, so the outcome is not reproduced (changed "
 "from partially reproduced after round 1).")
f7=O["figs7-seizure-pli-s1-vs-non-s1"]
f7.update({"outcome":"partially_reproduced","assumed":True,"output":"claim:figs7-seizure-pli-s1-vs-non-s1"})
f7.pop("blocked_by",None)
f7["notes"]=("With the pre-4-AP state from the gaps between pulses of the PLV recording (13 rats), the seizure PLI "
 "of the baseline block is 2 to 5 times the pre-4-AP PLI in both regions (concatenated, S1 0.10 to 0.24 against "
 "0.03 to 0.08). The S1 change exceeds the non-S1 change in every band (difference reading, by 0.006 to 0.087), "
 "significantly only in theta over concatenated samples under every ANOVA and rat reading (13 rats p = 0.0067 "
 "ordinary, 0.0004 repeated; 7 tFUS rats 0.024, 0.026) and in theta and gamma per seizure under the repeated "
 "reading for the 13 rats (0.0017, 0.044). Alpha and beta are never significant and the ratio reading finds "
 "nothing. Unlike Fig. S7B, where seizure non-S1 is below zero, both changes are positive.")
f7["deviations"]=[
 "The pre-4-AP state is the gaps between pulses of the PLV recording, as for figs5-seizures-lower-ai (13 of 16 "
 "rats; an assumption). Its PLI is taken over the concatenated gap samples; the per-gap PLI (gaps of 1.7 s) is 1.7 "
 "to 4 times higher, the short-window bias, and is shown only.",
 "S1 channels and seizure periods as for fig6-epileptic-pli-s1-decrease."]
O["fig5b-tfus-evoked-potentials"]["notes"]=(
 "The readings disagree. With the mean over the 64 channels, 2 of 18 combinations of position (CENTER, largest "
 "EP, largest EP chosen on odd trials and tested on even trials), sham onsets (every 2 s, random, the file's own "
 "intervals) and ANOVA (ordinary, repeated) find significant time points, both CENTER with random onsets "
 "(ordinary 13 of 610 points from 66.5 ms, smallest Bonferroni p = 0.013; repeated 26 points from 64.2 ms, "
 "p = 0.00067); the other 16 find none (smallest p = 0.054 to 1). With each channel, 1 to 55 of 64 channels have "
 "a significant point depending on the combination. The CENTER channel-mean EP reaches 3.1 uV, the sham 1.7 uV. "
 "The interval starts are the burst onsets: 1.4-1.5 kHz power, the band of the 1.5 kHz pulse repetition "
 "frequency, peaks 10 to 60 ms after them in 13 of 23 CENTER recordings and in none of the 23 resting ones, and "
 "the LFP shows no clear response at any lag of the 2 s cycle. The criterion blocks the claim when the readings "
 "disagree. Question for the authors (findings) which channels, which position and which sham onsets were used.")
O["fig5b-tfus-evoked-potentials"]["deviations"]=[
 "The repeated-measures reading of the time-point test adds a random intercept per rat to the group by time "
 "point two-way ANOVA (pooled error); the first version used a paired t-test per time point, which the claims-file "
 "check had replaced with this ANOVA.",
 "The largest-EP position reading picks the position on the data it tests; a split-half variant picks it on the "
 "odd trials and tests the even trials."]
O["fig5cdj-wild-type-gamma-pli-decrease"]["notes"]=(
 "The sham, the EEG of the resting baseline recording of the target confirmation, is not in the dandiset; its "
 "resting recordings hold only the intracranial LFP. The tFUS part, from the PLV EEG files of 20 rats, does not "
 "hold once the windows have equal length. Per trial, the PLI equals its trial-shuffled floor in every window "
 "(gamma S1 0.625 pre, 0.613 tFUS, 0.630 post; floors 0.628, 0.615, 0.629). Over concatenated samples the gamma "
 "PLI changes by S1 +0.002 and non-S1 +0.005 in the 0 to 20 ms window and -0.008 and -0.002 after it, with 47% of "
 "pairs decreasing in each. The decreases of the first version (20 to 200 ms window, 100% of pairs per trial) were "
 "the bias of comparing 549 samples with 61.")
O["fig5cdj-wild-type-gamma-pli-decrease"]["deviations"]=[
 "The 20 to 200 ms window is compared with the 20 ms pre window through the mean PLI of its nine 20 ms "
 "sub-windows, since a PLI over fewer samples is biased upwards; the whole window is shown. Each PLI is given with "
 "a noise floor, the contralateral channels taken from the next trial."]
O["fig5ghi-low-band-pli-s1-only"]["notes"]=(
 "In no band and under no combination of readings does the S1 PLI fall while the non-S1 PLI does not, with "
 "equal-length windows or with the whole 20 to 200 ms window. In the 0 to 20 ms window S1 PLI is not below pre in "
 "theta, alpha or beta under any reading (differences +0.0002 to +0.070). After it, over concatenated 20 ms "
 "sub-windows, both regions fall slightly in alpha (S1 -0.010, non-S1 -0.014) and beta (-0.016, -0.026). The "
 "per-trial PLI is at its trial-shuffled floor (theta S1 0.976 pre, floor 0.976), and the concatenated PLI (0.10 "
 "to 0.20) is about 0.02 above its floor.")
O["fig5ghi-low-band-pli-s1-only"]["deviations"].append(
 "Equal-length windows (nine 20 ms sub-windows of 20 to 200 ms) and trial-shuffled noise floors, as for "
 "fig5cdj-wild-type-gamma-pli-decrease.")
# findings
F=R["findings"]
for f in F:
    if f["kind"]=="data_missing":
        f["statement"]=("The EEG of the resting baseline of the target confirmation (the sham of Figs. 5E-F) is not in "
          "the dandiset; the resting recordings hold only the intracranial LFP, and the first monitoring block after "
          "the first injection was not deposited. The EEG before the first 4-AP injection (Figs. S5 and S7) is there "
          "only as the PLV recordings, which carry tFUS pulses and are not described as pre-4-AP recordings; 13 of the "
          "16 epileptic rats have one. PLV EEG files exist for 20 of the 23 wild-type rats (not BH638, BH642, BH644), "
          "while Fig. 5 gives N = 23.")
    if f["kind"]=="other" and "baseline AI" in f["statement"]:
        f["statement"]=("The baseline AI of the labelling channels on band power is strongly negative in both groups "
          "(whole block, sham -0.58 to -0.61, tFUS -0.24 to -0.29), and negative before 4-AP too (-0.17 to -0.26), so "
          "the contralateral channel carries 1.7 to 4 times the ipsilateral power; on band over total ratios the AI is "
          "near 0. The asymmetry is in the total power of channels 8 and 25. The paper reports only AI normalized to "
          "the baseline.")
F.append({"kind":"other","statement":("In the target-confirmation LFP the trial-mean response shows no clear "
  "evoked potential at any lag of the 2 s cycle, at the CENTER position as in the resting recording (mean RMS "
  "over channels 5.2 uV from 0 to 200 ms against 6.8 uV later in the cycle), although 1.4-1.5 kHz power, the "
  "pulse repetition frequency, marks the bursts at the interval starts in 13 of 23 CENTER recordings.")})
F.append({"kind":"metadata_insufficient","statement":("The PLV EEG recordings of the 16 epileptic rats are the "
  "last recordings before the first 4-AP injection (they end 64 to 176 min before the baseline block), but nothing "
  "in the files says so, and the timeline of Fig. 1E does not list them.")})
R["verifications"]=[]
PYEOF
echo ok
```

```
ok
```

**Agent**

Now the verification block (part 2 of the script).

**Agent calls Bash**

```bash
cd  cat >> $TMPDIR/rec.py <<'PYEOF'
for f in F:
    if f["kind"]=="methods_unavailable" and "two-way ANOVA" in f["statement"]:
        f["statement"]=("Question for the authors. Was the two-way ANOVA of Figs. 2 to 4 and 6 ordinary or repeated "
          "measures (or Prism's mixed-effects model), and which comparisons formed each Bonferroni family? The "
          "paper's within-group significance in Fig. 3 appears here only under a repeated-measures reading; this "
          "attempt assumed repeated measures, and each set of comparisons as its own family, for the claims where "
          "the readings disagree.")
V=[
("fig2c-sham-duration-stable",True,"not_reproduced","The block main effect is significant under every reading: per rat, ordinary p=0.00145 and repeated p=3.9e-05; per seizure, p≤5e-24 with 12–13 significant post hoc tests (seizure_metrics cell 12).",
 "No change of outcome. With t and F references on Satterthwaite df (point 1) the repeated per-rat block p is 0.00037; added the variant with seizures ending within 2 s of a block end counted as cut off (point 8), which gives the same."),
("fig2d-seizures-under-two-minutes",True,"reproduced","99.4% of ipsilateral and 99.2% of contralateral seizures last under 120 s (cell 15).","No change needed."),
("fig2e-sham-count-stable",True,"reproduced","No main effect or post hoc test is significant under any reading (smallest p_family = 1), and the same holds for the BH635 variant. The mean count falls slightly, from 18.11 to 16.50 (cell 17).","No change needed; the numbers are unchanged under the corrected repeated reading."),
("fig2f-sham-percent-time-post3",True,"reproduced","Reproduced (fragile). Under repeated measures, contralateral baseline against post 3 gives p_family 0.0209 (reading b of \"sham\"). Ordinary ANOVA gives nothing, and the label-following BH635 variant gives 0.083 (cell 19).",
 "Outcome kept. With the Satterthwaite t reference (point 1) the comparison gives p_family 0.040 and 0.051 over all 25, so it now also rests on the family reading, recorded as an assumption; the label-following BH635 variant under the ordinary ANOVA is shown (p = 0.94; point 9)."),
("fig3a-count-reduction",True,"reproduced","Under M4(b) all six decreases are within tolerance (8.7/36.4/41.9 and 10.5/41.4/42.4). Under repeated measures, baseline against post 1 and post 2 is significant in both hemispheres (p_family 0.0024–0.0085) (cell 23).",
 "No change of outcome; with the Satterthwaite t reference the four p values are 0.0059 to 0.016."),
("fig3a-count-sham-vs-tfus",False,"partially_reproduced","Sham against tFUS at post 1 is significant in both hemispheres under ordinary ANOVA (0.035, 0.025), and sham is steady. Post 2 reaches p<0.05 only in the repeated reading (ipsilateral 0.0458), and that rests on a z reference (problem 1); the ordinary reading has the same statistic and gives p=0.057 (cells 23, 25).",
 "Agreed and changed to partially reproduced. The repeated reading now uses t on Satterthwaite df; post 2 gives 0.064 and 0.076, post 1 0.040 and 0.029."),
("fig3b-percent-time-reduction",True,"reproduced","The decreases are within tolerance under both M4 readings. Under repeated measures all six comparisons against baseline are significant (p_family ≤0.0007) (cell 27).","No change of outcome; the six p values are now 0.0025 or less."),
("fig3b-sham-percent-time-no-change",True,"not_reproduced","Under repeated measures, sham baseline against post 2 is significant: contralateral 0.0214, ipsilateral 0.0434. This is the reading under which the paper's own within-group effects appear. Ordinary ANOVA gives none (cell 29).",
 "Outcome kept. With the t reference only contralateral post 2 stays significant (p_family 0.034; 0.057 over all ten), so the outcome now also rests on the family reading, stated as an assumption."),
("fig3b-percent-time-sham-vs-tfus",True,"not_reproduced","None of the three named comparisons is significant under any reading (p_family 0.06–0.14) (cell 32).","No change needed."),
("fig3c-interval-increase",True,"reproduced","Using gaps between seizures under M4(b), the increases are 27.4/49.1/27.8 and 30.1/51.9/30.9. Under repeated measures with family (ii), only contralateral post 1 is significant (0.0056; ipsilateral post 1 is 0.0595) (cell 34).",
 "No change of outcome. With the t reference contralateral post 1 is the only significant comparison under both families (0.0086 and 0.014)."),
("fig3c-interval-sham-vs-tfus",False,"partially_reproduced","Contralateral post 1 is significant under both ANOVAs (0.027 ordinary), with tFUS higher. Ipsilateral reaches 0.0385 only through the z reference (ordinary 0.0508, same statistic). No sham block differs from baseline (cell 36).",
 "Agreed and changed to partially reproduced; with the t reference ipsilateral post 1 gives 0.061."),
("fig3d-duration-decline",True,"not_reproduced","tFUS baseline against post 2 is not significant in either hemisphere under any reading (p_family ≥0.29) (cell 38).","No change needed; added the block-end variant (point 8), which gives the same."),
("fig4-no-theta-alpha-gamma-power-change",True,"not_reproduced","Under repeated measures, sham theta changes from baseline are significant under all four M5 readings (p_family down to 0.0004). Ordinary ANOVA gives none (eeg_blocks cell 10). The outcome depends on the protocol's absence rule.",
 "Outcome kept, resting on the assumption that the repeated reading is the paper's test. With the t reference the sham theta comparisons stay significant (p_family down to 0.0018); the tFUS gamma comparison no longer is."),
("fig4c-beta-decrease",True,"partially_reproduced","Post 1 is significantly lower than baseline (whole block, repeated measures, both hemispheres: 0.0028 and 0.026). The condition block never is (≥0.16). No combination of readings has both significant (cell 13).","No change of outcome; post 1 gives 0.0067 and 0.040 with the t reference."),
("figs4-sham-power-no-change",True,"not_reproduced","Beta block and hemisphere effects are significant under three of four segment × ANOVA combinations, and the gamma hemisphere effect is significant on whole blocks. Only seizure periods with ordinary ANOVA is clean (cell 15). Under the ordinary ANOVA alone, the M5 readings disagree, which by the criterion's rule would make this blocked.",
 "Outcome kept, resting on the repeated reading as for fig4; under that reading the M5 readings agree. The disagreement under the ordinary reading is stated in the notebook."),
("fig4ef-ai-increase",True,"partially_reproduced","tFUS theta and alpha rise above baseline only under whole block / subtraction / repeated measures. No sham against tFUS comparison is significant in any band under any reading (cells 17–18).",
 "No change of outcome. Added the tests of AI on band ratios (point 5) and the sign-corrected reading of an increase under division (point 6); with it, division gives the rise too, and no group difference is significant under any reading."),
("figs5-seizures-lower-ai",True,"blocked","Blocked (data_missing), but partly testable. Seizure AI is negative and below 0 in all bands: 16 rats p<0.001; 10 tFUS rats, theta p=0.0012 (cell 20). Pre-4-AP EEG does exist for 13 of 16 rats (point 4).",
 "Changed to reproduced, resting on assumptions. Following point 4, the PLV EEG of 13 rats is shown to end 64 to 176 min before the baseline block and is analysed between pulses; seizure AI is below the pre-4-AP AI in every band (paired t and repeated ANOVA). The outcome rests on that pre-4-AP state and on AI computed on band power; on band ratios (point 5) it fails, which is shown."),
("fig5b-tfus-evoked-potentials",True,"blocked","Blocked (methods_underspecified). The readings disagree. CENTER with random sham onsets and ordinary ANOVA gives 13 significant time points. Every other channel-mean combination gives 0. Per channel, 0–39 channels show significance (wild_type cell 8). The alignment is unverified (problem 3).",
 "Outcome kept. Added the alignment check (point 3): interval stop minus start is 2.2 s in every file, and 1.4-1.5 kHz power peaks 10 to 60 ms after the interval start in 13 of 23 CENTER recordings and none of the resting ones, so the starts are the burst onsets. Replaced the paired t of the repeated reading with the repeated-measures two-way ANOVA and added a split-half position reading (point 7); 2 of 18 combinations now find significant points."),
("fig5cdj-wild-type-gamma-pli-decrease",True,"blocked","Blocked (data_missing). The dandiset has no EEG of the resting sham. The tFUS-part \"post\" decrease is a window-length artifact (problem 2).",
 "Outcome kept. Fixed point 2: the post window is now the mean of nine 20 ms sub-windows and every PLI has a trial-shuffled floor; the tFUS-part decrease is gone and the notes say so."),
("fig5ghi-low-band-pli-s1-only",True,"not_reproduced","In the 0–20 ms window, S1 PLI is below pre in 0 of 3 bands under every reading. No band shows \"S1 below, non-S1 not below\" (cell 15). This is on the PLV files, a disclosed deviation, at roughly the noise-floor PLI level.",
 "No change of outcome; rerun with equal-length windows and noise floors (point 2), with the same result."),
("fig6-epileptic-pli-s1-decrease",False,"not_reproduced","tFUS S1 is below baseline in only 8 (or 6) of 12 cells. Non-S1 is also below in 8 of 12. Sham S1 falls as much or more. No S1 sham against tFUS comparison is significant (cells 22–23).",
 "Agreed and changed to not reproduced: the non-S1 part fails as well, which the criterion's partial clause does not cover."),
("figs7-seizure-pli-s1-vs-non-s1",True,"blocked","Blocked (data_missing), but partly testable. Same as figs5 (point 4).",
 "Changed to partially reproduced, resting on an assumption: with the pre-4-AP PLI from the gaps between pulses of the PLV recordings (13 rats), the S1 change exceeds the non-S1 change significantly in theta (and gamma under one reading), not in all four bands."),
]
R["verifications"]=[{"date":"2026-11-03","kind":"agent",
  "by":"Independent agent run by CatalystNeuro (same harness, separate context, did not write the notebook)",
  "reviewed":("Round 1. The first executed notebooks with the conclusion cells and the summary removed, the helper "
   "module and the claims file, with the paper. The verifier tested helper functions on synthetic inputs and queried "
   "the archive's asset metadata. Its report had no attempt record and gave its own outcome for each claim; 19 of 22 "
   "agree with the record as it then was."),
  "results":[{"claim":c,"agrees":a,"outcome":o,"reason":r,"response":s} for c,a,o,r,s in V]}]
assert len(V)==22 and {v[0] for v in V}==set(O)
# order of outcome keys
order=["claim","outcome","blocked_by","assumed","notebook","output","measured","notes","deviations"]
R["outcomes"]=[{k:o[k] for k in order if k in o} | {k:v for k,v in o.items() if k not in order} for o in R["outcomes"]]
class D(yaml.SafeDumper): pass
def strrep(d, s):
    return d.represent_scalar("tag:yaml.org,2002:str", s)
yaml.dump(R, open(p,"w"), Dumper=D, sort_keys=False, width=100, allow_unicode=True)
PYEOF
$TMPDIR/venv/bin/python $TMPDIR/rec.py && python tools/entry.py check entries/001683-gao-2026 2>&1 | tail -15
```

```
Exit code 1
Traceback (most recent call last):
  File "/tmp/claude-1001/rec.py", line 1, in <module>
    import yaml, copy
ModuleNotFoundError: No module named 'yaml'
```

**Agent calls Bash**

```bash
cd  python $TMPDIR/rec.py && python tools/entry.py check entries/001683-gao-2026 2>&1 | tail -15
```

```
0 error(s)
```

**Agent calls Bash**

```bash
cd  git diff --stat; git diff attempts/ | head -60
```

```
attempts/001683-gao-2026-01.yaml              | 696 +++++++++++++++++---------
 entries/001683-gao-2026/README.md             |  18 +-
 entries/001683-gao-2026/eeg_blocks.ipynb      | 370 +++++++++++---
 entries/001683-gao-2026/entry.yaml            |   4 +-
 entries/001683-gao-2026/seizure_metrics.ipynb | 166 +++---
 entries/001683-gao-2026/tfus.py               | 199 ++++++--
 entries/001683-gao-2026/wild_type.ipynb       | 192 +++++--
 7 files changed, 1203 insertions(+), 442 deletions(-)
diff --git a/attempts/001683-gao-2026-01.yaml b/attempts/001683-gao-2026-01.yaml
index 3d5fc75825..a7fca3bd1d 100644
--- a/attempts/001683-gao-2026-01.yaml
+++ b/attempts/001683-gao-2026-01.yaml
@@ -2,7 +2,7 @@ schema_version: 2
 id: 001683-gao-2026-01
 dataset:
   archive: dandi
-  id: "001683"
+  id: 001683
   version: 0.260109.2104
   doi: 10.48324/dandi.001683/0.260109.2104
[... 48 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -i 's/^  id: 001683$/  id: "001683"/' attempts/001683-gao-2026-01.yaml; git diff attempts/ | head -12 | tail -5; grep -n "—\|rather" attempts/001683-gao-2026-01.yaml entries/001683-gao-2026/*.ipynb entries/001683-gao-2026/tfus.py entries/001683-gao-2026/README.md | head
```

```
output: claim:fig2c-sham-duration-stable
-  notes: The block effect on sham seizure duration is significant under every reading. Per seizure
-    (1046 seizures) F = 30.45, p = 5.5e-24 ordinary and p = 2.4e-31 repeated, with 12 and 13 of 25
-    Bonferroni post hoc comparisons significant; per rat p = 0.00145 ordinary (no post hoc
-    comparison significant) and p = 3.9e-05 repeated (contralateral baseline against post 3,
```

**Agent**

Record written and the check passes. Now the full re-run with the retry fix.

**Agent calls Bash**

```bash
cd  date -u; python tools/entry.py all entries/001683-gao-2026 2>&1 | tail -6; date -u
```

```
Tue Nov  3 13:34:08 UTC 2026
Installed kernelspec registry-001683-gao-2026 in executed/001683-gao-2026/.venv/share/jupyter/kernels/registry-001683-gao-2026
0 error(s)
pass  seizure_metrics.ipynb  (61 s)
pass  eeg_blocks.ipynb  (1531 s)
pass  wild_type.ipynb  (724 s)
Tue Nov  3 14:12:53 UTC 2026
```

**Agent**

All three pass. Checking that the executed outputs match the dev-run numbers the conclusions were written from.

**Agent calls Bash**

```bash
cd  for nb in seizure_metrics eeg_blocks wild_type; do $TMPDIR/venv/bin/python $TMPDIR/show.py $TMPDIR/out/$nb.ipynb > $TMPDIR/a.txt; $TMPDIR/venv/bin/python $TMPDIR/show.py executed/001683-gao-2026/$nb.ipynb > $TMPDIR/b.txt; echo "== $nb"; diff $TMPDIR/a.txt $TMPDIR/b.txt | grep -v " in [0-9]* s\|ran in\|min$" | head -20; done
```

```
== seizure_metrics
4c4
---
50c50
< Label values given to 4 decimals of a minute or finer: 41.6%; first starts at one sample (1/3052 s): 6
---
> Label values (minutes) equal to their rounding to 3, 4 and 6 decimals: 0.0%, 0.0%, 0.2%; first starts at one sample (1/3052 s): 6
337a338
> 
413,414c414
<   [ordinary] main effects:
<  {'C(group, Sum)': 'F=8.66, p=0.00474', 'C(block, Sum)': 'F=5.15, p=0.00326', 'C(group, Sum):C(block, Sum)': 'F=0.95, p=0.422'}
---
>   [ordinary] main effects: {'C(group, Sum)': 'F=8.66, p=0.00474', 'C(block, Sum)': 'F=5.15, p=0.00326', 'C(group, Sum):C(block, Sum)': 'F=0.95, p=0.422'}
440d439
< 
591d589
< 
592a591
> 
[... 19 more lines not kept]
```

**Agent**

Outputs are identical apart from the reworded label-resolution line. Final check of the tree.

**Agent calls Bash**

```bash
cd  git status --short; python tools/entry.py check entries/001683-gao-2026 2>&1 | tail -2; grep -c "A failure to reproduce here may be a failure of this attempt" entries/001683-gao-2026/README.md entries/001683-gao-2026/*.ipynb; date -u
```

```
M attempts/001683-gao-2026-01.yaml
 M entries/001683-gao-2026/README.md
 M entries/001683-gao-2026/eeg_blocks.ipynb
 M entries/001683-gao-2026/entry.yaml
 M entries/001683-gao-2026/seizure_metrics.ipynb
 M entries/001683-gao-2026/tfus.py
 M entries/001683-gao-2026/wild_type.ipynb
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
?? scripts
0 error(s)
entries/001683-gao-2026/README.md:1
[... 4 more lines not kept]
```

**Agent**

I've revised the attempt for every point in the round-1 report. `python tools/entry.py all` passes all three notebooks (seizure_metrics 61 s, eeg_blocks 26 min, wild_type 12 min), and the check reports 0 errors. Every conclusion matches the new outputs. Nothing is committed.

**Outcome changes (5 of 22)**
- **fig3a-count-sham-vs-tfus**: reproduced → partially reproduced, as the verifier gave it. With the corrected repeated-measures test, post 2 is not significant (p = 0.064 and 0.076); post 1 is, in both hemispheres.
- **fig3c-interval-sham-vs-tfus**: reproduced → partially reproduced, as the verifier gave it. Only the contralateral side is significant at post 1 (ipsilateral p = 0.061).
- **fig6-epileptic-pli-s1-decrease**: partially → not reproduced, as the verifier gave it. The non-S1 part fails too, and the criterion's partial clause does not cover that.
- **figs5-seizures-lower-ai**: blocked → reproduced, resting on assumptions. As the verifier said, 13 of 16 rats have EEG from before the first 4-AP injection; it ends 64 to 176 min before the baseline block. Read between its tFUS pulses, the seizure AI is below that pre-4-AP AI in every band. This holds only with AI on band power, which the paper's wording supports ("relative difference in PSD"). With AI on band-to-total ratios the claim fails, and the notebook shows that.
- **figs7-seizure-pli-s1-vs-non-s1**: blocked → partially reproduced, resting on an assumption. The S1 change is significantly larger than the non-S1 change in theta only (and gamma under one reading), not in all four bands.

**Fixes for each point**
1. **Repeated-measures test**: it now uses t and F with Satterthwaite degrees of freedom, not the normal reference. I checked it against the classical split-plot ANOVA on synthetic data. The first two outcome changes come from this. fig2f and fig3b-sham-percent-time-no-change now also depend on which Bonferroni family is used. I adopted one family per set of comparisons and recorded it as an assumption.
2. **PLI window-length bias**: the 20–200 ms window is now averaged over nine 20 ms sub-windows, so it matches the pre window, and every PLI gets a trial-shuffled noise floor. The earlier tFUS-part decrease for fig5cdj is gone; the notes say so.
3. **EP alignment**: the intervals do start at the burst onsets. Power at 1.4–1.5 kHz (the burst pulse rate) peaks 10–60 ms after the interval start in 13 of 23 CENTER recordings and in none of the 23 resting ones. The LFP shows no clear response at any point in the 2 s cycle, so the missing EP is not a misalignment.
4. **Pre-4-AP EEG**: added a timing table and the figs5/figs7 analyses (see above).
5. **AI on ratios**: tests added. The ratio AI is near 0 at baseline, which means the strongly negative raw AI reflects a difference in total power between the two channels.
6. **Sign under division**: an increase is now shown both ways (the normalized value rising and the AI rising). fig4ef stays partial.
7. **fig5b test**: the paired t is replaced by the repeated-measures two-way ANOVA, and a split-half position reading is added. Now 2 of 18 combinations find significant time points. The outcome stays blocked.
8. **Block-end cut-offs**: six seizures end 1–1.4 s before a block end. Treating them as cut off changes neither fig2c nor fig3d.
9. **BH635**: the label-following variant is now also shown under the ordinary ANOVA.

I also made the helper's range reads retry dropped connections, after a transient network error failed the first full run. In the record, I updated the findings, added two (no clear EP in the LFP; the pre-4-AP recordings are not described as such), and recorded round 1 under `verifications` with the verifier's reasons and my responses.

**Not done**: I added nothing to `questions/001683.yaml`, because the report names no place where the claims file misreads the paper. Two of the verifier's unanswerable items stay open: Satterthwaite is not Prism's exact method, and the borderline cases (fig2f p = 0.040, fig3b-sham-percent-time-no-change p = 0.034) remain sensitive to it.

## End of run

98 turns, 143 minutes, $7.97 at API prices, result: success.
