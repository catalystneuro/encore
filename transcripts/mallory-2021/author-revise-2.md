# mallory-2021 · author-revise-2 · run 42980670983

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
date -u; cat transcripts/mallory-2021/verifier-2-report.md; ls entries/mallory-2021; ls entries/mallory-2021/*
```

```
Wed Nov 11 07:42:36 UTC 2026
# Verifier report, round 2: Mallory, Hardcastle et al. 2021 on DANDI:000053

**Counts.** These come from the claims file and the attempt record, not from any table. The claims file has 47 claims, and the attempt record has 47 outcomes, one per claim. The outcomes are 16 reproduced, 8 partially reproduced, 7 not reproduced and 16 blocked. Eleven outcomes are marked `assumed: true`: the ten Cohort 1 LN claims and supp9-eye.

## 1. Outcomes and assumptions

**Outcomes I agree with, and the assumptions are stated and reasonable:**
- headfixed-session-link, fig1b, fig4f, fig4j, fig4k, fig5a, fig5b, fig5-eye-position-stability, fig5av, fig6-nonlinear-temporal, fig6-eye-velocity-stability, fig7c, fig7e, supp4-eye, supp5-eye, supp7e.
- supp9-eye (assumed: reading (a); stated).
- The blocks of fig8c and fig8e, and of methods-hemispheres. For fig8c and fig8e, the trial tables are now printed (cells 13–14).

**Cohort 1 claims.** These are fig1c ×3, fig1d, fig2-shapes, fig2a, fig2b, fig2-stability, supp4-head and supp5-head. I agree with each outcome against its criterion on the printed numbers (free cells 14–44). The `assumed` statement names only readings (1a, 2a). Two further assumptions are left out:
- **Clock alignment.** The free notebook's clock check came out inconclusive (cell 7). The best lag has a median of −0.20 s for position and −0.40 s for pitch. By mouse it runs from −0.4 to +1.4 s, and only 0.18 and 0.24 of the strongest cells peak within 0.2 s. The notebook summary says the LN results "rest on the deposit's alignment", but the record does not. A misalignment would lower exactly the counts that fail: fig1c-pitch-roll (37 and 43), fig2-shapes and supp4-head.
- **Bin dropping.** Under (2a), 31% of the bins are dropped: the median kept fraction is 0.693 (cell 14). Reading (2b), clipping, would keep all of them, and the not-reproduced counts may depend on it.

**Head-fixed outcomes that depend on the fold reading, none of them marked `a
[... 74 more lines not kept]
```

**Agent calls Bash**

```bash
grep -n "^#" docs/protocol.md | head -80; wc -l docs/protocol.md entries/mallory-2021/*; ls attempts 2>/dev/null | grep mallory; git status --short | head; ls questions | grep mallory
```

```
1:# Protocol for an attempt
43:## Reader
45:### 1. Get the paper
59:### 2. Read the paper's code
69:### 3. Write the claims file
165:### 4. Data from outside the paper's own recordings
173:### 5. Check
186:### 6. Answer questions
199:## Author
215:### 1. Establish what can be tested
345:### 2. Check the data against its description
360:### 3. Write the entry
428:### 4. Lock, check and run
440:### 5. Record the attempt
502:### 6. Hand over for verification
540:## Repeat attempts
582:## Local and remote datasets
605:## Verifier
609:### Round 1: without the author's conclusions
634:### Round 2: with the author's conclusions
[... 24 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 1,42p docs/protocol.md; sed -n 199,654p docs/protocol.md
```

```
# Protocol for an attempt

Version: `pilot-14`. Record this version in the attempt's provenance.

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
[... 478 more lines not kept]
```

**Agent calls Bash**

```bash
cat entries/mallory-2021/entry.yaml entries/mallory-2021/README.md; wc -l attempts/mallory-2021-01.yaml questions/mallory-2021.yaml; ls executed/mallory-2021 2>/dev/null; ls transcripts/mallory-2021
```

```
schema_version: 1
name: mallory-2021
type: reproduction
title: Self-motion signals in mouse entorhinal cortex (Mallory, Hardcastle et al. 2021)
description: Tests the findings of Mallory, Hardcastle, Campbell, Attinger, Low, Raymond and Giocomo
  (2021) on dandiset 000053. The head-fixed Neuropixels recordings with eye tracking are tested with
  the paper's LN model (eye movement distributions, the cells encoding eye position and velocity,
  their tuning shapes, stability, contributions and checks against shuffling and raw tuning curves).
  The freely moving claims rest on head pitch and roll, which the dandiset lacks; they are tested on
  the paper's figshare deposits, where the head posture distributions and the Cohort 1 LN model claims
  are tested and the claims that need the LN model on Cohort 2 are blocked as too large for the time
  limit. The no-landmark track and the hemisphere
  comparison are blocked.
license: Apache-2.0
python: "3.13"
notebooks:
- path: freely_moving_mallory_2021.ipynb
  title: The freely moving claims, on the paper's figshare Datasets 1 and 2
  runtime_minutes: 43
- path: reproduce_mallory_2021.ipynb
[... 104 more lines not kept]
```

**Agent calls Bash**

```bash
grep -n "parallel\|Pool\|concurrent\|def cmd_\|def run\|timeout\|nbclient\|nbconvert" tools/entry.py | head -40
```

```
60:HARNESS = ["ipykernel", "nbconvert"]      # needed to execute, not part of the entry
436:def upgrade_python(entry_dir: Path, version: str, before: Path, output_dir: Path, timeout: int,
443:    if lock(entry_dir, version) or run(entry_dir, output_dir, timeout, max_minutes):
471:def run(entry_dir: Path, output_dir: Path, timeout: int, max_minutes: float) -> int:
477:    # nbconvert cannot pick up some other "python3" kernel (a user's or a conda install's).
492:            [str(python), "-m", "jupyter", "nbconvert", "--to", "notebook", "--execute",
493:             f"--ExecutePreprocessor.timeout={timeout}", f"--ExecutePreprocessor.kernel_name={kernel}",
563:    parser.add_argument("--timeout", type=int, default=3600, help="seconds allowed per cell")
600:                              args.timeout, args.max_minutes)
610:    return run(entry_dir, output_dir, args.timeout, args.max_minutes)
```

**Agent calls Bash**

```bash
sed -n 471,560p tools/entry.py; sed -n 560,615p tools/entry.py | grep -n "notebook\|add_argument"
```

```
def run(entry_dir: Path, output_dir: Path, timeout: int, max_minutes: float) -> int:
    entry = yaml.safe_load((entry_dir / "entry.yaml").read_text())
    output_dir.mkdir(parents=True, exist_ok=True)
    venv = (output_dir / ".venv").resolve()
    python = venv / "bin" / "python"
    # A kernel of the entry's own environment, under a name no other kernel on the machine has, so
    # nbconvert cannot pick up some other "python3" kernel (a user's or a conda install's).
    kernel = f"registry-{entry_dir.name}"
    for cmd in (["uv", "venv", "--quiet", "--clear", "--python", python_of(entry_dir), str(venv)],
                ["uv", "pip", "install", "--quiet", "--python", str(python),
                 "-r", str(entry_dir / "requirements.lock.txt"), *HARNESS],
                [str(python), "-m", "ipykernel", "install", "--prefix", str(venv), "--name", kernel]):
        if subprocess.run(cmd).returncode != 0:
            print(f"error: could not build the environment ({' '.join(cmd[:3])})", file=sys.stderr)
            return 1

    results, failed = [], False
    for notebook in entry["notebooks"]:
        name = notebook["path"]
        started = time.time()
[... 77 more lines not kept]
```

**Agent calls Bash**

```bash
cat transcripts/mallory-2021/author-revise-1-report.md; grep -o '"command": *"[^"]*entry.py[^"]*"' transcripts/mallory-2021/author-revise-1.md | head; grep -n "entry.py all\|entry.py run" transcripts/mallory-2021/author-revise-1.md | head
```

```
Revision done. The entry check passes with 0 errors and the handover is rebuilt. Nothing is committed.

Three notebooks were run with `tools/entry.py run`, and all three pass:
- freely moving: 43 min
- main: 51 min
- random-folds: 42 min

Together they are longer than the 2-hour limit on one command, so I ran them in two parts with `entry.yaml` cut down each time, then restored it and joined `result.json`. The check was run separately on the full entry. I wrote the conclusion cells after the runs, in both the source and executed copies; no code or outputs changed.

**Outcomes that changed** (all were blocked in round 1, and the verifier said they were testable):

| Claim | Now | Key numbers |
|---|---|---|
| fig1c-head-direction-cells | reproduced | 58 of 179 |
| fig1c-pitch-roll-cells | not reproduced | 37 and 43, paper 46 and 53 |
| fig1c-pitch-roll-velocity-rare | reproduced | 3 and 5 |
| fig1d-conjunctive-head | partially reproduced | 87 conjunctive; B alone 0.179, outside tolerance |
| fig2-pitch-roll-shapes | not reproduced | quadratic roll is 16 of 41, not a majority |
| fig2a, fig2b | reproduced | no preference under any reading |
| fig2-pitch-roll-stability | reproduced | Kruskal-Wallis P = 0.116 |
[... 34 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/mallory-2021; python - <<'EOF'
import json
for f in ["reproduce_mallory_2021.ipynb","freely_moving_mallory_2021.ipynb","readings_folds_mallory_2021.ipynb"]:
    nb=json.load(open(f)); print("=====",f,len(nb['cells']))
    for i,c in enumerate(nb['cells']):
        s="".join(c['source']); print(i,c['cell_type'][0],c.get('metadata',{}).get('tags',''),s[:110].replace("\n"," | "))
EOF
```

```
===== reproduce_mallory_2021.ipynb 82
0 m  # Reproducing Mallory, Hardcastle et al. (2021) on dandiset 000053 |  | **Paper.** Mallory CS, Hardcastle K, Campb
1 c  import math | import os | import time | import resource | import warnings | from collections import Counter, defaultdict
2 m  ## Data check
3 c ['sanity'] # Every file's metadata and array shapes (no data read). | with ThreadPoolExecutor(32) as ex: |     summaries = di
4 m  The open field files hold body position, body speed, head direction and azimuthal head velocity only | (head dir
5 c ['sanity'] of = files[files.task == "free exploration."].copy() | of["arena_cm"] = of.arena.str.extract(r"\[([0-9.]+)\]").a
6 m  The 1200 units match the paper's 179 + 1021 cells; 25 subjects against the paper's 26 mice. The six | mice recor
7 c ['sanity'] hf = files[files.task != "free exploration."].copy() | hf["device"] = [summaries[p].get("device", "") for p in h
8 c ['sanity'] # Compare the behaviour of each behaviour-only file with the ecephys file of the same frame count, | # and the s
9 m  Each of the 10 behaviour-only files repeats the behaviour of an ecephys file of the same session; | they are cou
10 m  ### headfixed-session-link |  | Claim (added by the author, `kind: link`): the paper's 11 head-fixed recordings in
11 c ['claim:headfixed-session-link'] with ThreadPoolExecutor(6) as ex: |     fsd = list(ex.map(L.figshare_session, sorted(L.FIGSHARE_FILES))) | ece = h
12 m  **Result: reproduced.** Each of the 11 figshare sessions matches exactly one dandiset file by | subject, unit co
13 c ['sanity'] # The 9 ecephys files that are not the paper's 11 recordings: their trial tables, which would mark | # the landm
14 m  No trial table holds a field for the track, its landmarks or a block: the columns are start and | stop time, vis
15 c ['sanity'] # Load the 11 sessions: behaviour at 50 Hz and spike counts in its 20 ms bins. | t0 = time.time() | DATA = {} | for 
16 m  Behaviour is sampled every 20 ms, as the Methods'
[... 175 more lines not kept]
```

**Agent calls Bash**

```bash
cd  ls claims 2>/dev/null | grep -i mallory; find . -name "*.yaml" -path "*claims*" | grep -i mallory
```

```
mallory-2021.yaml
./claims/mallory-2021.yaml
```

**Agent calls Bash**

```bash
cd  python - <<'EOF'
import yaml
c=yaml.safe_load(open("claims/mallory-2021.yaml"))
print([k for k in c])
for cl in c['claims']:
    if cl['id'] in ('supp12-no-false-eye-detection','fig1c-azimuthal-velocity-cells') or 'supp12' in cl['id'] or 'azimuthal' in cl['id']:
        print(yaml.dump(cl,width=150))
EOF
sed -n 1,40p claims/mallory-2021.yaml
```

```
['schema_version', 'paper', 'claims', 'checks']
criterion: LN pipeline over the Cohort 1 variables, and over B, Bs, Ha and azimuthal head velocity for Cohort 2. Reproduced when both counts are within
  tolerance under one reading of open details (1) and (2); partially reproduced when one is.
data: elsewhere
depends_on:
- fig1c-head-direction-cells
expected:
- quantity: Cohort 1 cells encoding azimuthal head velocity
  tolerance: 1.2
  value: 12
- quantity: Cohort 2 cells encoding azimuthal head velocity
  tolerance: 5.5
  value: 55
id: fig1c-azimuthal-velocity-cells
quote: A small population of neurons encoded azimuthal head velocity ... Tuning of neurons to azimuthal head velocity was verified in an additional dataset
  in which head movements were only measured in the azimuthal plane ( n = 55/1021 cells, 5%; Methods)
source: Results, Entorhinal neurons encode head movements in three dimensions, paragraph 1
statement: A small population of Cohort 1 cells (12 of 179, 7%) encodes azimuthal head velocity, and this is verified in Cohort 2, where 55 of 1021 cells
  (5%) do.
where: figshare, Mallory, Hardcastle et al. Dataset 1, doi:10.6084/m9.figshare.13425392.v1 (Freely_moving_data_with_inertial_sensor.mat, Cohort 1 with pitch
[... 85 more lines not kept]
```

**Agent calls Bash**

```bash
cd  ls paper; grep -n -i "simulated data\|eye-encoded\|Supplementary Fig. 12\|Supplementary Figure 12" paper/*.txt | head -20
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  sed -n 781,790p paper/*.txt | sed 's/\\documentclass.*\\end{document}//g' | cut -c1-3000; sed -n 7015,7040p paper/*.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd entries/mallory-2021; python - <<'EOF'
import json
nb=json.load(open("reproduce_mallory_2021.ipynb"))
for i in (1,22,23,24):
    print("----",i); print("".join(nb['cells'][i]['source']))
EOF
```

```
---- 1
import math
import os
import time
import resource
import warnings
from collections import Counter, defaultdict
from concurrent.futures import ThreadPoolExecutor

import numpy as np
import pandas as pd
from scipy import stats

import mec_ln as L

warnings.filterwarnings("ignore", category=RuntimeWarning)
pd.set_option("display.width", 200)
pd.set_option("display.max_columns", 40)
pd.set_option("display.max_rows", 200)
STARTED = time.time()
[... 56 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/mallory-2021; grep -n "^def \|^    def \|^[A-Z_]* = " mec_ln.py; sed -n 1,60p mec_ln.py
```

```
55:DANDISET_ID = "000053"
56:DANDISET_VERSION = "0.210819.0345"
57:FIGSHARE_HEADFIXED_DOI = "10.6084/m9.figshare.13426103.v1"
59:FIGSHARE_FILES = {1: 25829867, 2: 25829879, 3: 25829885, 4: 25829918, 5: 25830317, 6: 25829999,
62:DT = 0.02
63:VARS = ["B", "Bs", "Eh", "Ev", "Ehd", "Evd"]
64:EYE = ["Eh", "Ev", "Ehd", "Evd"]
65:N_CPTS = {"B": 20, "Eh": 5, "Ev": 5, "Ehd": 5, "Evd": 5}
66:SPEED_STEP = 5.0
67:TENSION = 0.5
68:PCT = (1.0, 99.0)
69:NFOLDS = 10
70:SECTION = 500  # 10 s at 50 Hz
71:ALPHA = 0.05
72:M_BINS = 200
74:PRESET = {"Eh": (-3.0, 3.0), "Ev": (-2.0, 2.0), "Ehd": (-3.0, 3.0), "Evd": (-2.0, 2.0)}
75:EXPLORED_MIN = 0.8  # Methods, "Quantifying tuning curve shape": 80% of the range for eye variables
76:FEE_MIN = 0.9
84:def asset_urls(pattern: str = "") -> dict[str, str]:
93:def _open(url: str) -> h5py.File:
[... 106 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/mallory-2021; sed -n 238,300p mec_ln.py; sed -n 405,475p mec_ln.py; sed -n 545,712p mec_ln.py
```

```
def prepare(sess: dict, range_mode: str = RANGE_DROP, mask: np.ndarray | None = None) -> dict:
    """Bins kept for the model, the variables' inner ranges and the spline blocks."""
    beh = sess["beh"]
    valid = np.ones(len(sess["t"]), bool)
    for v in VARS:
        valid &= np.isfinite(beh[v])
    if mask is not None:
        valid &= mask
    lims = {v: tuple(np.percentile(beh[v][valid], PCT)) for v in VARS}
    if range_mode == RANGE_DROP:
        keep = valid.copy()
        for v in VARS:
            keep &= (beh[v] >= lims[v][0]) & (beh[v] <= lims[v][1])
        vals = {v: beh[v][keep] for v in VARS}
    else:
        keep = valid
        vals = {v: np.clip(beh[v][keep], *lims[v]) for v in VARS}
    cpts = {v: control_points(v, *lims[v]) for v in VARS}
    blocks = {v: spline_1d(vals[v], cpts[v]) for v in VARS}
    return {"keep": keep, "lims": lims, "cpts": cpts, "blocks": blocks, "vals": vals,
[... 282 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 790,800p paper/*.txt | sed 's/\\documentclass.*\\end{document}//g' | cut -c1-1500
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd entries/mallory-2021; python - <<'EOF'
import json
nb=json.load(open("readings_folds_mallory_2021.ipynb"))
for i in (0,1,2,3,4,59,60):
    print("----",i); print("".join(nb['cells'][i]['source']))
print(nb['metadata'])
EOF
```

```
---- 0
# Mallory, Hardcastle et al. (2021): every head-fixed LN claim under reading (1b) random folds, (2a) drop

Companion to `reproduce_mallory_2021.ipynb` (dandiset 000053, version 0.210819.0345; the paper, the
claims file, the choice of version and the data check are there). The claims file leaves two details
of the LN pipeline open and asks for both readings of each: (1) how the 10-s sections are assigned to
the 10 folds, (a) in turn as compute_test_train_ind.m does, or (b) at random; (2) whether bins
outside a variable's inner 98% are (a) dropped or (b) clipped to the range. The main notebook runs
(1a, 2a). This one runs open detail (1) under reading (b), 10-s sections of the kept bins assigned to the 10 folds at random (balanced, a seed per session), and open detail (2) under reading (a), bins outside any variable's inner 98% dropped, on the same 11 recordings (selected as in the main notebook's link
claim), and repeats every downstream analysis of the main notebook on its fits, with the same code,
so that each claim's dependence on the reading can be seen. Each claim is judged in the main
notebook; the results here are variants.
---- 1
import math
import os
import time
import resource
import warnings
from collections import Counter, defaultdict
from concurrent.futures import ThreadPoolExecutor
[... 77 more lines not kept]
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "entries/mallory-2021/mec_ln.py",
 "old_string": "           \"sel_fits\": fs[\"sel_fits\"], \"n_spikes\": int(y.sum())}\n    enc = fs[\"encoded\"]",
 "new_string": "           \"sel_fits\": fs[\"sel_fits\"], \"n_spikes\": int(y.sum())}\n    enc = fs[\"encoded\"]\n    if not with_extras:\n        # the selected model's full-session parameters, from which Supp. Fig. 12 simulates spikes\n        out[\"sel_full\"] = fs[\"sel_full\"]"
}
```

```
The file entries/mallory-2021/mec_ln.py has been updated successfully.
```

**Agent calls Bash**

```bash
cd  date -u; uv venv --quiet --python 3.13 $TMPDIR/venv && uv pip install --quiet --python $TMPDIR/venv/bin/python -r entries/mallory-2021/requirements.lock.txt ipykernel nbconvert 2>&1 | tail -3; date -u
```

```
Wed Nov 11 07:44:34 UTC 2026
Wed Nov 11 07:44:40 UTC 2026
```

**Agent calls Bash**

```bash
cd entries/mallory-2021; cat > $TMPDIR/t.py <<'EOF'
import time, numpy as np, mec_ln as L, resource
urls = L.asset_urls("ecephys")
SESSIONS, fsd = L.paper_sessions(urls)
t=time.time(); p=SESSIONS[0]; s=L.load_session(urls[p]); print("load",time.time()-t, s["counts"].shape)
prep=L.prepare(s,L.RANGE_DROP); folds=L.fold_labels(prep["n_keep"],L.FOLDS_TURN); P=L.by_fold(prep,folds); P["seed"]=1000
Y=s["counts"][:,prep["keep"]][:40]
for ex in (False,True):
    t=time.time(); res=L.analyse_session(P,Y,processes=4,with_extras=ex); print(ex,time.time()-t, sum(bool(r["encoded"]) for r in res))
print(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1e6)
EOF
$TMPDIR/venv/bin/python $TMPDIR/t.py
```

```
Exit code 1
Traceback (most recent call last):
  File "/tmp/claude-1001/t.py", line 1, in <module>
    import time, numpy as np, mec_ln as L, resource
ModuleNotFoundError: No module named 'mec_ln'
```

**Agent calls Bash**

```bash
cd entries/mallory-2021 && PYTHONPATH=. $TMPDIR/venv/bin/python $TMPDIR/t.py
```

```
load 4.112936973571777 (389, 102281)
False 18.597586631774902 22
True 20.731425523757935 22
0.495208
```

**Agent calls Bash**

```bash
cd entries/mallory-2021; python - <<'EOF'
import json
nb=json.load(open("reproduce_mallory_2021.ipynb"))
print("".join(nb['cells'][0]['source'])[:6000])
EOF
grep -n "supp12" ../../attempts/mallory-2021-01.yaml | head
```

```
# Reproducing Mallory, Hardcastle et al. (2021) on dandiset 000053

**Paper.** Mallory CS, Hardcastle K, Campbell MG, Attinger A, Low IIC, Raymond JL, Giocomo LM (2021).
Mouse entorhinal cortex encodes a diverse repertoire of self-motion signals. *Nature Communications*
12, 671. [doi:10.1038/s41467-021-20936-8](https://doi.org/10.1038/s41467-021-20936-8). The claims file
(`claims/mallory-2021.yaml`) was written from the version of record (Europe PMC full text of
PMC7844029) with its Methods, legends and Supplementary Information.

**Dandiset.** [DANDI:000053](https://dandiarchive.org/dandiset/000053/0.210819.0345), version
0.210819.0345 (doi:10.48324/dandi.000053/0.210819.0345). The paper cites no DANDI version (its data
statement points to figshare). This is the only published version; the draft lists the same 359
assets, so the published version is pinned.

**What the dandiset holds.** 329 open field files (25 mice, 1200 units, tetrodes) with body position,
body speed, azimuthal head direction and azimuthal head velocity, and no pitch or roll; 20 head-fixed
Neuropixels files (9 mice, 5120 units) with VR position, speed, eye position and eye velocity, and 10
behaviour-only copies of head-fixed sessions. The paper's head-fixed data are 11 of the 20 files
(link claim below); of the other 9, six hold gain and contrast trials and three only gain 1 and contrast 100% (their trial tables are printed after the link).

**Outside input.** The paper's own deposit, figshare Dataset 3
[... 18 more lines not kept]
```

**Agent calls Bash**

```bash
mkdir -p $TMPDIR/dev; cat > $TMPDIR/dev/mk12.py <<'PYEOF'
import nbformat as nbf
M, C = nbf.v4.new_markdown_cell, nbf.v4.new_code_cell
cells = []
cells.append(M("""# Mallory, Hardcastle et al. (2021): simulated data without eye information (Supp. Fig. 12)

Companion to `reproduce_mallory_2021.ipynb` (dandiset 000053, version 0.210819.0345; the paper, the
claims file, the choice of version, the data check and the link of the 11 recordings are there). This
notebook tests one claim, `supp12-no-false-eye-detection`, which needs the LN pipeline run a second
time, on simulated spike trains, and so does not fit in the main notebook's time limit.

| Claim | Status |
|---|---|
| supp12-no-false-eye-detection | tested here, under readings (1a, 2a) of the LN pipeline, as the main notebook's counts |

**Method, from the paper.** Methods, "Generating simulated data without eye-encoded information": "we
first identified the selected variables of a given cell (i.e. by fitting a series of LN models) and
identified the model parameters corresponding to each variable. We then generated a new spiketrain
using all parameters except those relating to eye movements ... r = exp(A * w) ... By deleting the
relevant entries in A and w that correspond to eye movement information, we generated a new r, and
drew from a Poisson distribution with mean given by each element". The LN pipeline is then rerun on
the simulated spike trains (the claim's criterion). The legend of Supp. Fig. 12e gives the mutual
information of each eye variable with B (four pairs) and of each eye velocity with Bs (two pairs) in
each session, against 100 shuffles.

**Choices not fixed by the paper.** (i) The parameters are those of the selected model fitted to the
whole session (`sel_full`, the parameters the forward search carries between steps), the reading of
"the model parameters" taken here; the code's `param_mean`, the mean over folds, is the other. (ii)
Which cells are simulated. The procedure starts from a cell's selected variables, so cells that
encode nothing have no model to simulate from. The main test simulates every cell that encodes an
eye variable (an assumption: these are the cells whose eye tuning the analysis questions; a cell
without eye terms is simulated from its unchanged model, so an eye detection there would be the
ordinary false positive rate of Supp. Fig. 3). A seeded random sample of 300 of the encoding cells
without eye terms is simulated as well, and the count it would add over all such cells is shown.
(iii) Mutual information: 20 equal-width bins over each variable's inner 98% of the kept bins (a
standard choice), shuffles by random permutation of the eye variable over time (the legend's
"shuffled data"), and, as a stricter variant, by circular shifts of more than 20 s, which keep its
autocorrelation."""))
cells.append(C("""import os
import time
import resource
import warnings

import numpy as np
import pandas as pd
from scipy import stats

import mec_ln as L

warnings.filterwarnings("ignore", category=RuntimeWarning)
pd.set_option("display.width", 200)
pd.set_option("display.max_columns", 40)
STARTED = time.time()
urls = L.asset_urls("ecephys")
print(f"dandiset {L.DANDISET_ID} version {L.DANDISET_VERSION}: {len(urls)} assets")
SESSIONS, fsd = L.paper_sessions(urls)
print("Sessions matched to the figshare deposit:", sum(p is not None for p in SESSIONS), "of", len(SESSIONS))"""))
cells.append(C("""DATA = {p: L.load_session(urls[p]) for p in SESSIONS}
print(pd.DataFrame([{"session": p.split("/")[1][:40], "mouse": s["subject"], "units": s["counts"].shape[0],
                     "frames": len(s["t"])} for p, s in DATA.items()]).to_string(index=False))
print("Units:", sum(s["counts"].shape[0] for s in DATA.values()))""", metadata={"tags": ["sanity"]}))
cells.append(M("""## The LN model on the data, readings (1a, 2a)

The forward search alone (no tuning curves or refits), with the same bins, folds and seeds as the main
notebook, so the selections are the main notebook's."""))
cells.append(C("""SUBSET = int(os.environ.get("MALLORY_SUBSET", "0"))   # 0: every unit (develop on a few)
t0 = time.time()
ORIG, PREP = [], {}
for si, p in enumerate(SESSIONS):
    s = DATA[p]
    prep = L.prepare(s, L.RANGE_DROP)
    folds = L.fold_labels(prep["n_keep"], L.FOLDS_TURN)
    P = L.by_fold(prep, folds)
    P["seed"] = 1000 + si
    Y = s["counts"][:, prep["keep"]]
    if SUBSET:
        Y = Y[:SUBSET]
    res = L.analyse_session(P, Y, processes=4, with_extras=False)
    for i, r in enumerate(res):
        r.update({"session": p, "si": si, "mouse": s["subject"], "unit": i})
    ORIG += res
    PREP[p] = (prep, P)
print(f"LN model on the data: {len(ORIG)} units in {time.time() - t0:.0f} s; peak memory "
      f"{resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1e6:.2f} GB")
orig = pd.DataFrame([{"session": r["session"], "unit": r["unit"], "encoded": ",".join(r["encoded"]),
                      **{v: v in r["encoded"] for v in L.VARS}} for r in ORIG])
orig["eye_any"] = orig[L.EYE].any(axis=1)
orig["any"] = orig.encoded != ""
print("Encoding units:", int(orig["any"].sum()), "of", len(orig), "; eye units:", int(orig.eye_any.sum()))
print("Units per variable:", {v: int(orig[v].sum()) for v in L.VARS})""", metadata={"tags": ["sanity"]}))
cells.append(M("""### supp12-no-false-eye-detection

> Eye variables share information with body position and speed, yet when eye-related contributions
> are deleted from simulated spike trains, the LN model does not falsely detect eye tuning.

Criterion: spike trains are drawn from each cell's fitted model with eye terms removed and the LN
pipeline rerun; mutual information between each eye variable and B or Bs against 100 shuffles.
Reproduced when the data mutual information exceeds all shuffles in most sessions and, for each eye
variable, the cells detected in the simulated data are at most 10% of those in the original.

**Part 1: mutual information of the eye variables with B and Bs**, per session, over the kept bins."""))
cells.append(C("""rng_mi = np.random.default_rng(1200)
PAIRS = [("Eh", "B"), ("Ev", "B"), ("Ehd", "B"), ("Evd", "B"), ("Ehd", "Bs"), ("Evd", "Bs")]
NB, NSH = 20, 100


def codes(x, lo, hi):
    return np.clip(((x - lo) / (hi - lo) * NB).astype(int), 0, NB - 1)


def mi_bits(a, b):
    j = np.bincount(a * NB + b, minlength=NB * NB).reshape(NB, NB) / len(a)
    pa, pb = j.sum(1, keepdims=True), j.sum(0, keepdims=True)
    m = j > 0
    return float((j[m] * np.log2(j[m] / (pa @ pb)[m])).sum())


rows = []
for si, p in enumerate(SESSIONS):
    prep = PREP[p][0]
    cd = {v: codes(prep["vals"][v], *prep["lims"][v]) for v in L.VARS}
    n = len(cd["B"])
    for e, b in PAIRS:
        mi = mi_bits(cd[e], cd[b])
        perm = np.array([mi_bits(rng_mi.permutation(cd[e]), cd[b]) for _ in range(NSH)])
        shifts = rng_mi.integers(int(20 / L.DT), n - int(20 / L.DT), NSH)
        circ = np.array([mi_bits(np.roll(cd[e], k), cd[b]) for k in shifts])
        rows.append({"session": si + 1, "pair": f"{e}-{b}", "MI": mi, "perm_max": perm.max(), "circ_max": circ.max(),
                     "above_perm": mi > perm.max(), "above_circ": mi > circ.max()})
MI = pd.DataFrame(rows)
print(MI.pivot(index="session", columns="pair", values="MI").round(3).to_string())
summ = MI.groupby("pair").agg(sessions=("session", "size"), above_all_permutations=("above_perm", "sum"),
                              above_all_circular_shifts=("above_circ", "sum"), MI_median=("MI", "median"),
                              perm_max_median=("perm_max", "median"), circ_max_median=("circ_max", "median"))
print(summ.round(4).to_string())
print("Range of the data MI (bits):", round(MI.MI.min(), 4), "to", round(MI.MI.max(), 4))"""),
)
cells[-1].metadata["tags"] = ["claim:supp12-no-false-eye-detection"]
cells.append(M("""**Part 2: simulated spike trains without the eye terms.** For each simulated cell the rate is
exp of the intercept plus the B and Bs terms of its selected model (fitted on the whole session),
over the kept bins, and spikes are drawn from a Poisson distribution with that mean (a seed per
session). The forward search is then rerun with the same bins and folds."""))
cells.append(C("""rng_pick = np.random.default_rng(1201)
N_NONEYE = 300
noneye = orig[orig["any"] & ~orig.eye_any].index.to_numpy()
pick = set(rng_pick.choice(noneye, min(N_NONEYE, len(noneye)), replace=False).tolist())
SIM_IDX = sorted(set(orig.index[orig.eye_any]) | pick)
print(f"Simulated: {int(orig.eye_any.sum())} eye cells and {len(pick)} of {len(noneye)} encoding cells without eye terms")

t0 = time.time()
SIM = []
for si, p in enumerate(SESSIONS):
    prep, P = PREP[p]
    idx = [k for k in SIM_IDX if ORIG[k]["si"] == si]
    if not idx:
        continue
    rng_sim = np.random.default_rng(12000 + si)
    Ysim = np.zeros((len(idx), prep["n_keep"]))
    rates = []
    for row, k in enumerate(idx):
        r = ORIG[k]
        lay = L._layout(prep["blocks"], r["encoded"])
        eta = np.full(prep["n_keep"], r["sel_full"][0])
        for v in r["encoded"]:
            if v not in L.EYE:
                eta += prep["blocks"][v] @ r["sel_full"][lay[v]]
        lam = np.exp(eta)
        Ysim[row] = rng_sim.poisson(lam)
        rates.append((lam.mean() / L.DT, r["n_spikes"] / prep["n_keep"] / L.DT))
    res = L.analyse_session(P, Ysim, processes=4, with_extras=False)
    for k, rr, (sim_hz, data_hz) in zip(idx, res, rates):
        SIM.append({"k": k, "session": p, "orig": ORIG[k]["encoded"], "sim": rr["encoded"],
                    "rate_sim_hz": sim_hz, "rate_data_hz": data_hz, "spikes_sim": rr["n_spikes"]})
print(f"LN model on the simulated data: {len(SIM)} units in {time.time() - t0:.0f} s; peak memory "
      f"{resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1e6:.2f} GB")
sim = pd.DataFrame(SIM)
sim["eye_cell"] = sim.orig.apply(lambda e: any(v in L.EYE for v in e))
print("Mean rate, simulated against data (Hz), median over cells: eye cells",
      round(sim[sim.eye_cell].rate_sim_hz.median(), 2), "vs", round(sim[sim.eye_cell].rate_data_hz.median(), 2),
      "; other cells", round(sim[~sim.eye_cell].rate_sim_hz.median(), 2), "vs", round(sim[~sim.eye_cell].rate_data_hz.median(), 2))
print("Simulated units encoding nothing:", int((sim.sim.apply(len) == 0).sum()), "of", len(sim))"""),
)
cells[-1].metadata["tags"] = ["claim:supp12-no-false-eye-detection"]
cells.append(C("""scale = len(noneye) / max(len(pick), 1)
rows = []
for v in L.VARS:
    n_orig = int(orig[v].sum())
    se = sim[sim.eye_cell]
    so = sim[~sim.eye_cell]
    det_eye = int(se.sim.apply(lambda e: v in e).sum())
    det_other = int(so.sim.apply(lambda e: v in e).sum())
    kept = int(se.apply(lambda r: v in r.orig and v in r.sim, axis=1).sum()) if v in L.EYE else None
    rows.append({"variable": v, "original": n_orig, "simulated_eye_cells": det_eye,
                 "of_which_had_it": kept, "simulated_sample_other": det_other,
                 "other_scaled_to_all": round(det_other * scale, 1),
                 "fraction_eye_cells": round(det_eye / n_orig, 3) if n_orig else np.nan,
                 "fraction_with_scaled_other": round((det_eye + det_other * scale) / n_orig, 3) if n_orig else np.nan,
                 "at_most_10pct": (det_eye / n_orig <= 0.10) if (n_orig and v in L.EYE) else None,
                 "at_most_10pct_with_other": ((det_eye + det_other * scale) / n_orig <= 0.10) if (n_orig and v in L.EYE) else None})
T12 = pd.DataFrame(rows)
print(T12.to_string(index=False))
# B and Bs detection among the simulated eye cells that encoded them, as a check that the simulation keeps the body tuning
for v in ("B", "Bs"):
    had = sim[sim.eye_cell & sim.orig.apply(lambda e: v in e)]
    print(f"{v}: kept in {int(had.sim.apply(lambda e: v in e).sum())} of {len(had)} simulated eye cells that encoded it")
by_s = sim[sim.eye_cell].groupby("session").apply(
    lambda d: pd.Series({"eye_cells": len(d), "eye_detected": int(d.sim.apply(lambda e: any(v in L.EYE for v in e)).sum())}))
by_s.index = [SESSIONS.index(p) + 1 for p in by_s.index]
print("Per session, simulated eye cells with any eye variable detected:")
print(by_s.T.to_string())"""))
cells[-1].metadata["tags"] = ["claim:supp12-no-false-eye-detection"]
cells.append(M("**Result: PENDING.**"))
cells.append(M("""## Summary

PENDING"""))
cells.append(C("""print(f"Notebook time: {(time.time() - STARTED) / 60:.1f} min; peak memory "
      f"{resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1e6:.2f} GB")""", metadata={"tags": ["sanity"]}))
nb = nbf.v4.new_notebook(cells=cells, metadata={"kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"}})
nbf.write(nb, "simulated_eye_mallory_2021.ipynb")
PYEOF
cd entries/mallory-2021 && $TMPDIR/venv/bin/python $TMPDIR/dev/mk12.py && ls
```

```
README.md
__pycache__
entry.yaml
freely_moving_mallory_2021.ipynb
mec_free.py
mec_ln.py
readings_folds_mallory_2021.ipynb
reproduce_mallory_2021.ipynb
requirements.in
requirements.lock.txt
simulated_eye_mallory_2021.ipynb
```

**Agent calls Bash**

```bash
date -u && time MALLORY_SUBSET=30 $TMPDIR/venv/bin/python -m jupyter nbconvert --to notebook --execute --output-dir $TMPDIR/dev --output s12.ipynb simulated_eye_mallory_2021.ipynb 2>&1 | tail -3
```

```
Wed Nov 11 07:49:31 UTC 2026
[NbConvertApp] Converting notebook simulated_eye_mallory_2021.ipynb to notebook
[IPKernelApp] WARNING | Kernel is running over TCP without encryption. All communication (including code and outputs) is sent in plain text and is susceptible to eavesdropping. Use IPC transport or launch with kernel manager-provisioned CurveZMQ keys to enable transport encryption.
[NbConvertApp] Writing 24123 bytes to /tmp/claude-1001/dev/s12.ipynb

real	8m38.859s
user	17m40.698s
sys	0m17.909s
```

**Agent calls Bash**

```bash
cd $TMPDIR/dev && python - <<'EOF'
import json
nb=json.load(open("s12.ipynb"))
for i,c in enumerate(nb['cells']):
    if c['cell_type']=='code':
        print("----",i)
        for o in c.get('outputs',[]):
            print(o.get('text','') if 'text' in o else o.get('data',{}).get('text/plain','') if 'data' in o else o)
EOF
```

```
---- 1
['dandiset 000053 version 0.210819.0345: 20 assets\n']
['Sessions matched to the figshare deposit: 11 of 11\n']
---- 2
['                                 session mouse  units  frames\n', 'sub-npJ5_ses-20190505_obj-10plzqh_behavi  npJ5    389  102281\n', 'sub-npI1_ses-20190413_behavior+ecephys.n  npI1     77  127222\n', 'sub-npI1_ses-20190415_behavior+ecephys.n  npI1    173   44061\n', 'sub-npI1_ses-20190416_behavior+ecephys.n  npI1    408   78990\n', 'sub-npI3_ses-20190420_behavior+ecephys.n  npI3    286  451580\n', 'sub-npI4_ses-20190421_obj-1h2xem6_behavi  npI4    254   84626\n', 'sub-npI4_ses-20190423_behavior+ecephys.n  npI4    537   74852\n', 'sub-npJ1_ses-20190523_behavior+ecephys.n  npJ1    303   75904\n', 'sub-npJ2_ses-20190511_behavior+ecephys.n  npJ2    106  117785\n', 'sub-npJ3_ses-20190504_behavior+ecephys.n  npJ3    210  124590\n', 'sub-npJ4_ses-20190511_behavior+ecephys.n  npJ4    118  117863\n', 'Units: 2861\n']
---- 4
['LN model on the data: 330 units in 192 s; peak memory 1.91 GB\n', 'Encoding units: 205 of 330 ; eye units: 52\n', "Units per variable: {'B': 180, 'Bs': 110, 'Eh': 25, 'Ev': 13, 'Ehd': 17, 'Evd': 1}\n"]
---- 6
['pair      Eh-B  Ehd-B  Ehd-Bs   Ev-B  Evd-B  Evd-Bs\n', 'session                                            \n', '1        0.084  0.054   0.046  0.016  0.031   0.015\n', '2        0.136  0.166   0.100  0.086  0.059   0.016\n', '3        0.130  0.115   0.064  0.067  0.103   0.046\n', '4        0.093  0.083   0.049  0.054  0.091   0.026\n', '5        0.293  0.035   0.137  0.182  0.023   0.044\n', '6        0.115  0.070   0.027  0.088  0.058   0.028\n', '7        0.178  0.100   0.057  0.067  0.045   0.022\n', '8        0.168  0.061   0.101  0.118  0.037   0.032\n', '9        0.057  0.100   0.024  0.027  0.054   0.010\n', '10       0.033  0.073   0.150  0.087  0.073   0.089\n', '11       0.071  0.101   0.101  0.056  0.060   0.019\n', '        sessions  above_all_permutations  above_all_circular_shifts  MI_median  perm_max_me
[... 8 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/mallory-2021; python - <<'EOF'
import json
nb=json.load(open("freely_moving_mallory_2021.ipynb"))
for i in (1,3,9,13,14):
    print("----",i); print("".join(nb['cells'][i]['source']))
for i,c in enumerate(nb['cells']):
    s="".join(c['source'])
    for k in ("IDX2","RANGE","raw","SESS2","D2"):
        if k in s: print(i,k)
EOF
grep -n "RANGE\|def " mec_free.py | head -40
```

```
---- 1
import math
import os
import time
import resource
import warnings
from collections import Counter

import numpy as np
import pandas as pd
from scipy import stats

import mec_ln as L
import mec_free as F

warnings.filterwarnings("ignore", category=RuntimeWarning)
pd.set_option("display.width", 200)
pd.set_option("display.max_columns", 40)
pd.set_option("display.max_rows", 200)
STARTED = time.time()
[... 128 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/mallory-2021; sed -i 's/by_s.index = \[SESSIONS.index(p) + 1 for p in by_s.index\]/by_s.index = [SESSIONS.index(p) + 1 for p in by_s.index]\nby_s = by_s.sort_index()/' $TMPDIR/dev/mk12.py && $TMPDIR/venv/bin/python $TMPDIR/dev/mk12.py && grep -c sort_index simulated_eye_mallory_2021.ipynb
python - <<'EOF'
import json
nb=json.load(open("freely_moving_mallory_2021.ipynb"))
for i in (0,5,7,27,45):
    print("----",i); print("".join(nb['cells'][i]['source'])[:2500])
EOF
```

```
1
---- 0
# Mallory, Hardcastle et al. (2021): the freely moving claims, on the paper's figshare deposits

**Paper.** Mallory CS, Hardcastle K, Campbell MG, Attinger A, Low IIC, Raymond JL, Giocomo LM (2021).
Mouse entorhinal cortex encodes a diverse repertoire of self-motion signals. *Nature Communications*
12, 671. [doi:10.1038/s41467-021-20936-8](https://doi.org/10.1038/s41467-021-20936-8). The claims file
(`claims/mallory-2021.yaml`) was written from the version of record with its Methods, legends and
Supplementary Information.

**Data.** Dandiset 000053 holds no head pitch or roll, so a reader marked the freely moving claims
`data: elsewhere` (question of 2026-11-10), on the paper's own deposits: figshare Dataset 1
([doi:10.6084/m9.figshare.13425392.v1](https://doi.org/10.6084/m9.figshare.13425392.v1),
Freely_moving_data_with_inertial_sensor.mat, Cohort 1, 179 cells with pitch and roll) and Dataset 2
([doi:10.6084/m9.figshare.13425017.v1](https://doi.org/10.6084/m9.figshare.13425017.v1),
Freely_moving_data_without_inertial_sensor.mat, Cohort 2). Both are version 1, the only version.
Dataset 1 is one compressed MATLAB 5 variable, so it is streamed whole into memory (1.7 GB) and
reduced as it loads; Dataset 2 (6.4 GB, MATLAB 7.3) is read in place, only its azimuthal head
velocity, for Figure 1b. Nothing is written to disk. Loading is in `mec_free.py`, which also holds the open field LN model
(run here on Cohort 1).
[... 141 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/mallory-2021; sed -n 150,190p mec_free.py; sed -n 76,80p mec_free.py
```

```
return spline_circ(values)
    return L.spline_1d(np.clip(values, cpts[0] + 1e-9, cpts[-1]), cpts)


def prepare(sess: dict, range_mode: str = L.RANGE_DROP, variables=VARS) -> dict:
    """Bins kept for the model, the variables' inner ranges and the spline blocks of one session."""
    beh = sess["beh"]
    dims = [k for k in ("x", "y", "Bs", "Ha", "Hp", "Hr", "Had", "Hpd", "Hrd") if k in beh]
    valid = np.ones(len(sess["t"]), bool)
    for k in dims:
        valid &= np.isfinite(beh[k])
    lims = {k: tuple(np.percentile(beh[k][valid], PCT)) for k in dims if k != "Ha"}
    lims["Ha"] = (0.0, 2 * math.pi)
    if range_mode == L.RANGE_DROP:
        keep = valid.copy()
        for k in dims:
            if k != "Ha":
                keep &= (beh[k] >= lims[k][0]) & (beh[k] <= lims[k][1])
        vals = {k: beh[k][keep] for k in dims}
    else:
[... 26 more lines not kept]
```

**Agent calls Bash**

```bash
nproc; free -g; date -u
```

```
4
               total        used        free      shared  buff/cache   available
Mem:              15           1          10           0           3          14
Swap:              2           0           2
Wed Nov 11 07:58:57 UTC 2026
```

**Agent calls Bash**

```bash
cd entries/mallory-2021; python - <<'EOF'
import json
nb=json.load(open("reproduce_mallory_2021.ipynb"))
for i in (4,64,80):
    print("----",i); print("".join(nb['cells'][i]['source']))
nb=json.load(open("freely_moving_mallory_2021.ipynb"))
for i in (8,):
    print("---- free",i); print("".join(nb['cells'][i]['source']))
EOF
```

```
---- 4
The open field files hold body position, body speed, head direction and azimuthal head velocity only
(head direction in radians, azimuthal head velocity in radians/s, position in cm with a conversion
to metres).
The pitch and roll of Cohort 1 (IMU) are not in the dandiset; the paper deposited them on figshare
(Dataset 1, doi:10.6084/m9.figshare.13425392.v1). Every freely moving claim of the claims file needs
them, or depends on a claim that does, so they are blocked. Below, the open field cohorts are
identified only to describe the data.
---- 64
**Result: reproduced.** Under reading (c), one held-out section, B (median 0.638) and Bs (0.283) each exceed every eye variable and Eh (0.106) and Ev (0.110) each exceed Eh dot (0.053) and Ev dot (0.036), all 12 comparisons at P < 0.0033, and four of six medians are within tolerance. Under reading (a), the fold mean, the same 12 comparisons hold with two medians within tolerance (B 0.625, Eh 0.102); reading (b), the Methods' literal wording, inverts the order (B 0.375, Eh dot 0.940) and matches nothing. With each of the 10 folds as the held-out section, all 12 comparisons hold in 5 folds and four or more medians are within tolerance in 3 (folds 1, 7, 8); both hold together only in fold 1, so the outcome rests on the single-section reading with fold 1.
---- 80
## Summary

| Claim | Outcome |
|---|---|
| headfixed-session-link (link) | reproduced |
| fig4f-eye-movement-distributions | reproduced |
| fig4j-eye-encoding-cells | reproduced |
| fig4k-eye-conjunctive | reproduced |
| fig5a-eh-nasal-temporal-similar | partially reproduced (hemispheres not testable) |
[... 44 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/mallory-2021; cat > $TMPDIR/dev/edit1.py <<'PYEOF'
import json, sys
def edit(fn, i, old, new):
    nb = json.load(open(fn))
    s = "".join(nb["cells"][i]["source"])
    assert old in s, (fn, i, old[:60])
    s = s.replace(old, new)
    nb["cells"][i]["source"] = s.splitlines(keepends=True)
    json.dump(nb, open(fn, "w"), indent=1, ensure_ascii=False); open(fn, "a").write("\n")
M = "reproduce_mallory_2021.ipynb"; FR = "freely_moving_mallory_2021.ipynb"; FO = "readings_folds_mallory_2021.ipynb"
edit(M, 4, """Every freely moving claim of the claims file needs
them, or depends on a claim that does, so they are blocked. Below,""",
"""Every freely moving claim of the claims file needs
them, or depends on a claim that does, so they are tested on the figshare deposits in
`freely_moving_mallory_2021.ipynb` (`data: elsewhere`). Below,""")
edit(M, 22, """The other
reading of detail (1) is run for the counts in `readings_folds_mallory_2021.ipynb`; reading (2b) was not run, for lack of time.""",
"""The other
reading of detail (1) is run, with every downstream analysis, in `readings_folds_mallory_2021.ipynb`; reading (2b) was not run, for lack of time.""")
edit(M, 64, "so the outcome rests on the single-section reading with fold 1.",
"so the outcome rests on the single-section reading with fold 1. Under reading (1b), random folds, it does not hold: reading (c) with fold 1 gives 10 of 12 comparisons and one of six medians, and no fold meets both parts (`readings_folds_mallory_2021.ipynb`). The outcome is therefore marked as resting on reading (1a) of the folds as well.")
edit(M, 80, "| fig7ab-eye-contributions | reproduced (reading c) |", "| fig7ab-eye-contributions | reproduced (reading c, fold 1, folds in turn; assumed, fails under random folds) |")
edit(M, 80, "| fig5bv-ev-low-order-more-stable | partially reproduced |", "| fig5bv-ev-low-order-more-stable | partially reproduced (assumed: folds in turn; reproduced under random folds) |")
edit(M, 80, "| fig6-eye-velocity-linear-nasal | partially reproduced |", "| fig6-eye-velocity-linear-nasal | partially reproduced (assumed: folds in turn) |")
edit(M, 80, "| fig6v-asymmetric-more-stable | partially reproduced |", "| fig6v-asymmetric-more-stable | partially reproduced (assumed: folds in turn) |")
edit(M, 80, "| supp12-no-false-eye-detection | blocked, too large |", "| supp12-no-false-eye-detection | blocked, too large (now run in `simulated_eye_mallory_2021.ipynb`; a change is proposed) |")
edit(M, 80, """Open
details are run under the readings the claims file names, and reading (1b) of the folds is run through
every claim in `readings_folds_mallory_2021.ipynb`;""", """Open
details are run under the readings the claims file names, and reading (1b) of the folds is run through
every claim in `readings_folds_mallory_2021.ipynb`. Four outcomes hold only under reading (1a), folds in
turn, and are marked as resting on it: fig7ab, fig5bv (which would be reproduced under (1b)),
fig6-eye-velocity-linear-nasal and fig6v;""")
edit(FR, 8, """The one claim tested here, fig1b, uses the behaviour alone, so it does not
depend on the clock.""", """fig1b uses the behaviour alone, so it does not depend on the clock. Every
claim on the Cohort 1 LN model (cells 14 to 44) does: a misalignment of spikes and behaviour would
lower the counts of encoding cells and the stability of their tuning. Those outcomes rest on the
deposit's alignment, an assumption stated with each of them.""")
PYEOF
$TMPDIR/venv/bin/python $TMPDIR/dev/edit1.py && git diff --stat .
```

```
.../mallory-2021/freely_moving_mallory_2021.ipynb   |  6 ++++--
 entries/mallory-2021/mec_ln.py                      |  3 +++
 entries/mallory-2021/reproduce_mallory_2021.ipynb   | 21 ++++++++++++---------
 3 files changed, 19 insertions(+), 11 deletions(-)
```

**Agent calls Bash**

```bash
cd entries/mallory-2021; python - <<'EOF'
s=open("entry.yaml").read()
s=s.replace("""  runtime_minutes: 42
helpers:""","""  runtime_minutes: 42
- path: simulated_eye_mallory_2021.ipynb
  title: Simulated spike trains without eye information (Supp. Fig. 12)
  runtime_minutes: 45
helpers:""")
open("entry.yaml","w").write(s)
EOF
cp entry.yaml $TMPDIR/dev/entry_full.yaml
python - <<'EOF'
import yaml
e=yaml.safe_load(open("entry.yaml"))
keep=["reproduce_mallory_2021.ipynb","simulated_eye_mallory_2021.ipynb"]
s=open("entry.yaml").read()
import re
# write a cut version keeping only the two notebooks
lines=s.split("\n"); out=[]; skip=False
for l in lines:
    if l.startswith("- path: "):
        skip = l[8:] not in keep
    elif not l.startswith("  "):
        skip=False
    if not skip: out.append(l)
open("entry.yaml","w").write("\n".join(out))
EOF
sed -n 12,30p entry.yaml; date -u
```

```
limit. The no-landmark track and the hemisphere
  comparison are blocked.
license: Apache-2.0
python: "3.13"
notebooks:
- path: reproduce_mallory_2021.ipynb
  title: Reproducing Mallory, Hardcastle et al. (2021) from dandiset 000053
  runtime_minutes: 51
- path: simulated_eye_mallory_2021.ipynb
  title: Simulated spike trains without eye information (Supp. Fig. 12)
  runtime_minutes: 45
helpers:
- mec_ln.py
- mec_free.py
related:
- id: dandi:000053/0.210819.0345
  relation: uses_data
- id: doi:10.6084/m9.figshare.13425392.v1
  relation: uses_data
Wed Nov 11 07:59:37 UTC 2026
```

**Agent calls Bash**

```bash
cd  date -u; python tools/entry.py run entries/mallory-2021 2>&1 | tail -8; date -u; cp executed/mallory-2021/result.json $TMPDIR/dev/result_A.json
```

```
Wed Nov 11 07:59:41 UTC 2026
Installed kernelspec registry-mallory-2021 in executed/mallory-2021/.venv/share/jupyter/kernels/registry-mallory-2021
pass  reproduce_mallory_2021.ipynb  (2901 s)
pass  simulated_eye_mallory_2021.ipynb  (2478 s)
Wed Nov 11 09:29:25 UTC 2026
```

**Agent calls Bash**

```bash
cd  cp executed/mallory-2021/*.ipynb $TMPDIR/dev/; cd entries/mallory-2021; python - <<'EOF'
keep=["freely_moving_mallory_2021.ipynb","readings_folds_mallory_2021.ipynb"]
s=open("/tmp/claude-1001/dev/entry_full.yaml").read()
lines=s.split("\n"); out=[]; skip=False
for l in lines:
    if l.startswith("- path: "):
        skip = l[8:] not in keep
    elif not l.startswith("  "):
        skip=False
    if not skip: out.append(l)
open("entry.yaml","w").write("\n".join(out))
EOF
grep "path:" entry.yaml; echo $TMPDIR
```

```
- path: freely_moving_mallory_2021.ipynb
- path: readings_folds_mallory_2021.ipynb
/tmp/claude-1001
```

**Agent calls Bash**

```bash
cd  date -u; python tools/entry.py run entries/mallory-2021 2>&1 | tail -8; date -u; cp executed/mallory-2021/result.json $TMPDIR/dev/result_B.json
```

```
Wed Nov 11 09:29:36 UTC 2026
Installed kernelspec registry-mallory-2021 in executed/mallory-2021/.venv/share/jupyter/kernels/registry-mallory-2021
pass  freely_moving_mallory_2021.ipynb  (2631 s)
pass  readings_folds_mallory_2021.ipynb  (2520 s)
Wed Nov 11 10:55:33 UTC 2026
```

**Agent calls Bash**

```bash
cd  cp $TMPDIR/dev/entry_full.yaml entries/mallory-2021/entry.yaml; cp $TMPDIR/dev/reproduce_mallory_2021.ipynb $TMPDIR/dev/simulated_eye_mallory_2021.ipynb executed/mallory-2021/; python - <<'EOF'
import json
a=json.load(open("/tmp/claude-1001/dev/result_A.json")); b=json.load(open("/tmp/claude-1001/dev/result_B.json"))
order=["freely_moving_mallory_2021.ipynb","reproduce_mallory_2021.ipynb","readings_folds_mallory_2021.ipynb","simulated_eye_mallory_2021.ipynb"]
r={x["notebook"]:x for x in a["results"]+b["results"]}
a["results"]=[r[n] for n in order]
open("executed/mallory-2021/result.json","w").write(json.dumps(a,indent=1)+"\n")
print([(x["notebook"],x["ok"],x["seconds"]) for x in a["results"]])
nb=json.load(open("executed/mallory-2021/simulated_eye_mallory_2021.ipynb"))
for i,c in enumerate(nb['cells']):
    if c['cell_type']=='code':
        print("----",i)
        for o in c.get('outputs',[]):
            print("".join(o.get('text','')) if 'text' in o else o)
EOF
```

```
[('freely_moving_mallory_2021.ipynb', True, 2631), ('reproduce_mallory_2021.ipynb', True, 2901), ('readings_folds_mallory_2021.ipynb', True, 2520), ('simulated_eye_mallory_2021.ipynb', True, 2478)]
---- 1
dandiset 000053 version 0.210819.0345: 20 assets

Sessions matched to the figshare deposit: 11 of 11

---- 2
                                 session mouse  units  frames
sub-npJ5_ses-20190505_obj-10plzqh_behavi  npJ5    389  102281
sub-npI1_ses-20190413_behavior+ecephys.n  npI1     77  127222
sub-npI1_ses-20190415_behavior+ecephys.n  npI1    173   44061
sub-npI1_ses-20190416_behavior+ecephys.n  npI1    408   78990
sub-npI3_ses-20190420_behavior+ecephys.n  npI3    286  451580
sub-npI4_ses-20190421_obj-1h2xem6_behavi  npI4    254   84626
sub-npI4_ses-20190423_behavior+ecephys.n  npI4    537   74852
sub-npJ1_ses-20190523_behavior+ecephys.n  npJ1    303   75904
sub-npJ2_ses-20190511_behavior+ecephys.n  npJ2    106  117785
sub-npJ3_ses-20190504_behavior+ecephys.n  npJ3    210  124590
sub-npJ4_ses-20190511_behavior+ecephys.n  npJ4    118  117863
Units: 2861
[... 54 more lines not kept]
```

**Agent calls Bash**

```bash
cd executed/mallory-2021; python - <<'EOF'
import json
def out(fn,i,n=3000):
    nb=json.load(open(fn)); c=nb['cells'][i]
    s="".join("".join(o.get('text','')) for o in c.get('outputs',[]) if 'text' in o)
    print(f"==== {fn[:12]} {i}\n"+s[-n:])
out("reproduce_mallory_2021.ipynb",24,600)
out("reproduce_mallory_2021.ipynb",81,300)
out("freely_moving_mallory_2021.ipynb",14,1500)
out("freely_moving_mallory_2021.ipynb",7,800)
out("freely_moving_mallory_2021.ipynb",46,300)
out("readings_folds_mallory_2021.ipynb",43,2500)
out("readings_folds_mallory_2021.ipynb",60,300)
EOF
```

```
==== reproduce_ma 24
 bins kept (90.3%), 278 s
sub-npJ1_ses-20190523_behavior+ecephys.n: 303 units, 62849 of 69506 valid bins kept (90.4%), 142 s
sub-npJ2_ses-20190511_behavior+ecephys.n: 106 units, 105925 of 117415 valid bins kept (90.2%), 109 s
sub-npJ3_ses-20190504_behavior+ecephys.n: 210 units, 109513 of 120926 valid bins kept (90.6%), 222 s
sub-npJ4_ses-20190511_behavior+ecephys.n: 118 units, 105554 of 115999 valid bins kept (91.0%), 88 s
LN model: 2861 units in 2021 s; peak memory 3.93 GB
Units with no spike in the kept bins (nothing to fit): 3
Units whose selected model failed the final test against 0: 707

==== reproduce_ma 81
Notebook time: 48.2 min; peak memory 3.93 GB

==== freely_movin 14
LN model, Cohort 1: 179 cells in 31.4 min; peak memory 12.06 GB
Kept bins per session (fraction of valid): median 0.693 range 0.674 to 0.751
Cells with no spike in the kept bins: 0 ; selected model failed the final test against 0: 41
Cells encoding any variable: 138 of 179
Counts per variable: {'B': 98, 'Bs': 41, 'Ha': 58, 'Hp': 37, 'Hr': 43, 'Had': 10, 'Hpd': 3, 'Hrd': 5}
Variant, the code's final test on the last model tried: {'B': 99, 'Bs': 40, 'Ha': 59, 'Hp': 37, 'Hr': 45, 'Had': 10, 'Hpd': 3, 'Hrd': 5}
[... 50 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat > $TMPDIR/dev/fill12.py <<'PYEOF'
import json
RES = """**Result: reproduced, under the assumptions stated in the header (proposed change; the verified outcome stays blocked).** The data mutual information exceeds all 100 permutation shuffles in 11 of 11 sessions for each of the six pairs (median 0.026 to 0.115 bits against a median shuffle maximum of 0.004), and all 100 circular shifts in 11 of 11 sessions for five pairs and 10 of 11 for Ev with B. On the simulated spike trains of the 718 eye cells, with the B and Bs terms kept and the eye terms deleted, the rerun LN pipeline detects Eh in 0 cells, Ev in 2, Eh dot in 2 and Ev dot in 0, against 341, 243, 238 and 137 in the data (0.000 to 0.008, all at most 10%). In the sample of 300 encoding cells without eye terms no eye variable is detected, so scaled to all 1422 such cells the count stays 0. B and Bs are kept in 635 of 635 and 456 of 456 simulated eye cells that encoded them. Deleting the eye terms raises the simulated mean rate of the eye cells (median 7.48 Hz against 4.84 Hz in the data), as the Methods' procedure does; a variant that keeps the eye terms' mean was not run."""
SUM = """## Summary

| Claim | Outcome |
|---|---|
| supp12-no-false-eye-detection | blocked, too large (verified outcome); reproduced here, proposed for round 3 |

**How the analysis differs from the paper's.** The LN pipeline is the main notebook's, under readings
(1a, 2a). The simulated cells are the 718 eye cells and a random 300 of the 1422 encoding cells
without eye terms (an assumption; the paper may have simulated every cell). The spikes are drawn from
the selected model fitted on the whole session. Mutual information uses 20 equal-width bins, a
standard choice.

**What was found about the dataset.** Nothing beyond the main notebook."""
for fn in ("entries/mallory-2021/simulated_eye_mallory_2021.ipynb", "executed/mallory-2021/simulated_eye_mallory_2021.ipynb"):
    nb = json.load(open(fn))
    for c in nb["cells"]:
        s = "".join(c["source"])
        if s.startswith("**Result: PENDING"):
            c["source"] = RES
        elif s.startswith("## Summary"):
            c["source"] = SUM
    json.dump(nb, open(fn, "w"), indent=1, ensure_ascii=False)
    open(fn, "a").write("\n")
PYEOF
$TMPDIR/venv/bin/python $TMPDIR/dev/fill12.py; cd entries/mallory-2021; sed -i 's/  runtime_minutes: 43/  runtime_minutes: 44/; s/  runtime_minutes: 51/  runtime_minutes: 48/; s/  runtime_minutes: 45/  runtime_minutes: 41/' entry.yaml; grep runtime entry.yaml
```

```
runtime_minutes: 44
  runtime_minutes: 48
  runtime_minutes: 42
  runtime_minutes: 41
```

**Agent calls Bash**

```bash
cd  cat > $TMPDIR/dev/edit2.py <<'PYEOF'
import json
def edit(name, i, old, new):
    for d in ("entries/mallory-2021/", "executed/mallory-2021/"):
        fn = d + name
        nb = json.load(open(fn))
        s = "".join(nb["cells"][i]["source"])
        assert old in s, (fn, i, old[:60])
        nb["cells"][i]["source"] = s.replace(old, new)
        json.dump(nb, open(fn, "w"), indent=1, ensure_ascii=False); open(fn, "a").write("\n")
FR = "freely_moving_mallory_2021.ipynb"; FO = "readings_folds_mallory_2021.ipynb"
edit(FR, 45, "and the others were not run, for time (32.4 min per reading).",
     "and the others were not run, for time (31.4 min per reading under (2a); reading (2b) keeps every valid bin, about 1.44 times as many, so about 45 min). The Cohort 1 count of azimuthal head velocity cells, needed by the blocked fig1c-azimuthal-velocity-cells, is 10 (paper 12, tolerance 1.2).")
edit(FR, 45, "so the LN results on Cohort 1 rest on the deposit's\nalignment.",
     "so the LN results on Cohort 1 rest on the deposit's\nalignment, an assumption stated with each of those outcomes.")
edit(FO, 59, """The downstream outcomes do not change direction: fig5a and fig5b
still find no preference;""", """Most downstream results keep their direction: fig5a and fig5b
still find no preference;""")
edit(FO, 59, """fig5av and
fig5bv hold their tests, and fig5bv meets two medians here; fig6 linear loses its nasal test; fig6
nonlinear and fig6 stability still fail (Ev dot is more stable than Bs here); fig6v fails in both
parts; fig7ab holds its tests under reading (a);""", """fig5av and
fig5bv hold their tests, and fig5bv meets two of its medians here, which its criterion would count as
reproduced; fig6 linear loses its nasal test; fig6
nonlinear and fig6 stability still fail (Ev dot is more stable than Bs here); fig6v fails in both
parts; fig7ab holds its tests under reading (a), but under reading (c), the one recorded, fold 1
gives 10 of 12 comparisons and one of six medians and no fold meets both parts. Four outcomes of the
main notebook (fig5bv, fig6 linear, fig6v and fig7ab) thus depend on reading (1) and are marked as
resting on reading (1a);""")
PYEOF
$TMPDIR/venv/bin/python $TMPDIR/dev/edit2.py && python - <<'EOF'
import json
nb=json.load(open("executed/mallory-2021/freely_moving_mallory_2021.ipynb"))
print("".join(nb['cells'][13]['source']))
for i in (17,20,26,30,33,35,38,41,44):
    print(i,"".join(nb['cells'][i]['source'])[:600])
EOF
```

```
## The open field LN model on Cohort 1, under readings (1a, 2a)

The claims file's LN pipeline (opening comment) over the eight Cohort 1 variables (B, Bs, Ha, Hp, Hr
and the azimuthal, pitch and roll head velocities), for every cell of figshare Dataset 1, with open
detail (1) under reading (a), 10-s sections assigned to folds in turn (compute_test_train_ind.m),
and open detail (2) under reading (a), bins outside any variable's inner 95% dropped. The criteria ask
for both readings of (1) and (2); only this one was run, because one reading of the 179 cells takes
about 32 minutes on the runner's four cores (printed below) (the cells average 178,000 bins and the 2D position
spline has up to 121 parameters), and the four readings would not fit within the 60-minute notebook
limit or the run's time. The readings not run are named in each claim's notes.
17 **Result: reproduced, under readings (1a, 2a).** 58 of 179 cells (0.324) encode Ha, within the tolerance of 63 and of 0.35. The other readings of open details (1) and (2) were not run, for time.
20 **Result: not reproduced, under readings (1a, 2a).** 37 cells encode pitch (paper 46, tolerance 4.6) and 43 roll (paper 53, tolerance 5.3); both counts are below tolerance. The other readings were not run.
26 **Result: partially reproduced.** 87 cells encode more than one variable (paper 95, within tolerance), but 0.179 encode body position alone (paper 0.15, tolerance 0.015). Each of Bs, Ha, Hp, Hr and azimuthal head velocity alone is at most 5% (0.022, 0.045, 0.011, 0.022, 0.006).
30 **Result: not reproduced.** 33 or 34 pitch and 41 roll curves are classified; linear plus quadratic is the majority of pitch cells (12 and 13 or 14), but quadratic roll cells (16) are not more than half of 41, and none of the six counts is within tolerance.
33 **Result: reproduced.** No reading of preference or explored range finds a pitch preference: 17 to 21 of 33 or 34 cells prefer positive pitch, P from 0.229 to 1.0.
35 **Result: reproduced.*
[... 3 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat > $TMPDIR/dev/edit3.py <<'PYEOF'
import json
exec(open("/tmp/claude-1001/dev/edit2.py").read().split("FR = ")[0])
edit("freely_moving_mallory_2021.ipynb", 13, "about 32 minutes on the runner's four cores (printed below)",
     "about 31 minutes on the runner's four cores (printed below; reading (2b) keeps all valid bins, about 1.44 times as many, so about 45 minutes)")
PYEOF
$TMPDIR/venv/bin/python $TMPDIR/dev/edit3.py && python - <<'EOF'
p="entries/mallory-2021/README.md"; s=open(p).read()
rep=[("| Body variables contribute more than eye variables (Fig. 7a, b) | Reproduced |","| Body variables contribute more than eye variables (Fig. 7a, b) | Reproduced (rests on folds in turn and one held-out fold; fails under random folds) |"),
("| Low-order Ev cells more stable (Fig. 5b v) | Partially reproduced |","| Low-order Ev cells more stable (Fig. 5b v) | Partially reproduced (rests on folds in turn; reproduced under random folds) |"),
("| Linear eye velocity cells and their nasal preference (Fig. 6) | Partially reproduced |","| Linear eye velocity cells and their nasal preference (Fig. 6) | Partially reproduced (rests on folds in turn) |"),
("| Asymmetric eye velocity cells more stable (Fig. 6 v) | Partially reproduced |","| Asymmetric eye velocity cells more stable (Fig. 6 v) | Partially reproduced (rests on folds in turn) |"),
("| No false detection of eye tuning in simulated data (Supp. Fig. 12) | Blocked: too large |","| No false detection of eye tuning in simulated data (Supp. Fig. 12) | Blocked: too large (now run; reproduced, proposed for the next round) |"),
("posture distributions and the Cohort 1 LN model claims (about 43 minutes).","posture distributions and the Cohort 1 LN model claims (about 44 minutes). The Cohort 1 LN outcomes rest on the deposit's clock alignment, which the notebook's check could not establish, and on readings (1a, 2a) only."),
("readings of the LN pipeline (about 51 minutes, most of it the LN fits of 2861 units).","readings of the LN pipeline (about 48 minutes, most of it the LN fits of 2861 units)."),
("folds at random (about 42 minutes). The reading with each variable clipped to its range was not run, for time.","folds at random (about 42 minutes). Under it fig7ab no longer holds and fig5bv would be reproduced, so both, with fig6 linear and fig6v, are marked as resting on folds in turn. The reading with each variable clipped to its range was not run, for time.\n- `simulated_eye_mallory_2021.ipynb`: Supp. Fig. 12, spike trains simulated from each eye cell's model without its eye terms and the LN pipeline rerun (about 41 minutes)."),
]
for a,b in rep:
    assert a in s, a; s=s.replace(a,b)
open(p,"w").write(s)
EOF
date -u
```

```
Wed Nov 11 10:56:24 UTC 2026
```

**Agent calls Bash**

```bash
cd  grep -n "^[a-z_]*:\|^- claim:\|^  - claim:\|^  - round\|^- round\|round:" attempts/mallory-2021-01.yaml | head -150
```

```
1:schema_version: 3
2:id: mallory-2021-01
3:datasets:
9:paper: doi:10.1038/s41467-021-20936-8
10:date: '2026-11-10'
11:entry: mallory-2021
12:provenance:
23:inputs:
40:outcomes:
41:- claim: headfixed-session-link
53:- claim: fig1b-head-posture-distributions
72:- claim: fig1c-head-direction-cells
92:- claim: fig1c-pitch-roll-cells
112:- claim: fig1c-pitch-roll-velocity-rare
132:- claim: fig1c-azimuthal-velocity-cells
145:- claim: fig1d-conjunctive-head
167:- claim: fig2-pitch-roll-shapes
194:- claim: fig2a-pitch-up-down-similar
215:- claim: fig2b-roll-left-right-similar
235:- claim: fig2-pitch-roll-stability
[... 85 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 12,22p attempts/mallory-2021-01.yaml; sed -n 72,145p attempts/mallory-2021-01.yaml; sed -n 258,268p attempts/mallory-2021-01.yaml; sed -n 473,508p attempts/mallory-2021-01.yaml; sed -n 549,596p attempts/mallory-2021-01.yaml; sed -n 654,674p attempts/mallory-2021-01.yaml; sed -n 808,815p attempts/mallory-2021-01.yaml; sed -n 867,890p attempts/mallory-2021-01.yaml; sed -n 1176,1188p attempts/mallory-2021-01.yaml
```

```
provenance:
  kind: agent
  accountable:
    name: CatalystNeuro
  agent:
    harness: Claude Code
    model: claude-opus-5-5
    protocol: pilot-14
  runner:
    platform: GitHub Actions
    url: https://github.com/catalystneuro/encore/actions/runs/42843008382
- claim: fig1c-head-direction-cells
  outcome: reproduced
  assumed: true
  notebook: freely_moving_mallory_2021.ipynb
  output: claim:fig1c-head-direction-cells
  measured:
  - 58
  - 0.324
  notes: Blocked as too_large in round 1; the verifier found it testable and it is now run. 58 of 179 cells encode
[... 226 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python - <<'EOF'
import yaml
d=yaml.safe_load(open("attempts/mallory-2021-01.yaml"))
s=yaml.dump(d,sort_keys=False,width=120,allow_unicode=True)
open("/tmp/claude-1001/dev/rt.yaml","w").write(s)
EOF
diff attempts/mallory-2021-01.yaml $TMPDIR/dev/rt.yaml | head -20; diff attempts/mallory-2021-01.yaml $TMPDIR/dev/rt.yaml | wc -l; grep -n "proposed" tools/entry.py docs/*.md | head; ls schemas 2>/dev/null
```

```
24,26c24,26
< - what: The freely moving cells of Cohort 1 with head pitch and roll (spike times, body position and speed, azimuthal
<     head direction and velocity, pitch, roll), the data of the `elsewhere` Cohort 1 claims; figshare Dataset 1 of
<     the paper, version 1, streamed into memory.
---
> - what: The freely moving cells of Cohort 1 with head pitch and roll (spike times, body position and speed, azimuthal head
>     direction and velocity, pitch, roll), the data of the `elsewhere` Cohort 1 claims; figshare Dataset 1 of the paper, version
>     1, streamed into memory.
28,29c28,29
< - what: The freely moving cells of Cohort 2 (no inertial sensor); figshare Dataset 2 of the paper, version 1, read
<     in place. Only its cell index and the azimuthal head velocity of each session were read, for fig1b.
---
> - what: The freely moving cells of Cohort 2 (no inertial sensor); figshare Dataset 2 of the paper, version 1, read in place.
>     Only its cell index and the azimuthal head velocity of each session were read, for fig1b.
31,33c31,33
< - what: Which dandiset files are the paper's 11 head-fixed recordings (session names, unit and frame counts), and
<     the first unit's spikes and the behaviour of each, used only to match and check the files; figshare Dataset
<     3 of the paper, read in place.
---
> - what: Which dandiset files are the paper's 11 head-fixed recordings (session names, unit and frame counts), and the first
[... 15 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python - <<'EOF'
import yaml,subprocess
d=yaml.safe_load(open("attempts/mallory-2021-01.yaml"))
for w in (110,112,113,114,115,116,118):
    s=yaml.dump(d,sort_keys=False,width=w,allow_unicode=True)
    open("/tmp/claude-1001/dev/rt.yaml","w").write(s)
    n=subprocess.run("diff attempts/mallory-2021-01.yaml /tmp/claude-1001/dev/rt.yaml | wc -l",shell=True,capture_output=True,text=True).stdout
    print(w,n.strip())
EOF
python -c "import json;s=json.load(open('schemas/attempt.schema.json'));import sys;print(json.dumps(s['\$defs'].get('outcome',s)['properties'].get('proposed') if '\$defs' in s else '',indent=1)[:1500])"
```

```
110 0
112 850
113 1033
114 1243
115 1360
116 1394
118 1468
""
```

**Agent calls Bash**

```bash
cd  grep -n "proposed" -A 25 schemas/attempt.schema.json | head -50
```

```
303:          "proposed": {
304-            "description": "A change of outcome found after the last verification round, held until a further round agrees with it.",
305-            "type": "object",
306-            "additionalProperties": false,
307-            "required": [
308-              "outcome",
309-              "reason"
310-            ],
311-            "properties": {
312-              "outcome": {
313-                "enum": [
314-                  "reproduced",
315-                  "partially_reproduced",
316-                  "not_reproduced",
317-                  "blocked"
318-                ]
319-              },
320-              "blocked_by": {
321-                "description": "Required when outcome is blocked.",
322-                "enum": [
[... 6 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 924,972p attempts/mallory-2021-01.yaml; sed -n 1074,1081p attempts/mallory-2021-01.yaml; sed -n 325,360p tools/entry.py
```

```
- claim: fig5av-eh-linear-most-stable
    agrees: true
    outcome: reproduced
    reason: Kruskal-Wallis P = 4.2e-10; linear beats quadratic (P = 0.0015) and higher orders (P = 4.5e-10); all
      three medians are within tolerance.
    response: No change; the (1b) values are in the notes.
  - claim: fig5bv-ev-low-order-more-stable
    agrees: true
    outcome: partially_reproduced
    reason: The tests hold, but only 1 of 3 medians is in tolerance against the two required; the criterion has
      no partial clause, and the verifier calls it partial because the statement holds and only the medians fail.
    response: Outcome kept. Under (1b) two of three medians are within tolerance; the outcome rests on reading (1a),
      as the notes now say.
  - claim: fig6-eye-velocity-linear-nasal
    agrees: true
    outcome: partially_reproduced
    reason: The tests hold (nasal 36 of 56, P = 0.044; vertical P = 0.41), but the linear counts 56 and 36 are outside
      43 +- 4.3 and 29 +- 2.9.
    response: Outcome kept; under (1b) the nasal test also fails (P = 0.070), recorded in the notes.
  - claim: fig6-eye-velocity-nonlinear-temporal
[... 73 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python - <<'EOF'
import yaml
d=yaml.safe_load(open("attempts/mallory-2021-01.yaml"))
for o in d['outcomes']:
    if o['claim'] in ('supp4-eye-ln-conservative','fig5a-eh-nasal-temporal-similar','fig5b-ev-up-down-similar','fig6-eye-velocity-nonlinear-temporal'):
        print(o['claim'], o.get('measured')); print(o['notes']); print()
EOF
python - <<'EOF'
import json
nb=json.load(open("executed/mallory-2021/reproduce_mallory_2021.ipynb"))
for i in (36,37,39,40,54,55,75,76):
    c=nb['cells'][i]
    if c['cell_type']=='code':
        print("==",i,"".join("".join(o.get('text','')) for o in c.get('outputs',[]) if 'text' in o)[:3500])
    else: print("== md",i,"".join(c['source']))
EOF
```

```
fig5a-eh-nasal-temporal-similar None
Over all 341 Eh cells 158 prefer nasal positions (0.463, Z = -1.35, binomial P = 0.194); preference reading (b) and both readings of explored range give P from 0.19 to 0.23. The two hemisphere tests cannot be run, as the dandiset does not record the hemisphere of each recording; the part that can be tested holds. Nasal is taken as positive horizontal eye position (Methods, Comparison between LN and shuffling-based methods; Supplementary Fig. 4 labels). Round 2: preference reading (b) is now the claims file's literal one, the side with the larger absolute slope: 155 of 341 nasal, P = 0.104; the round-1 reading (b), the steeper rise away from 0, is kept as variant (r), 158 of 341, P = 0.194. Round 2, reading (1b) random folds (readings notebook, every downstream analysis): 127 to 132 of 282, P = 0.108 to 0.311. No reading finds a preference.

fig5b-ev-up-down-similar 172
172 of 243 Ev cells are classified (within 17.7 of 177) under both readings of explored range; 84 of 172 prefer upward positions (Z = -0.30, P = 0.819); preference reading (b) gives 81 of 172, P = 0.493. Round 2: literal preference reading (b) gives 82 of 172 upward, P = 0.594. Round 2, reading (1b) random folds (readings notebook, every downstream analysis): 131 classified (outside 177 +- 17.7), 60 to 69 upward, P = 0.38 to 0.60.

fig6-eye-velocity-nonlinear-temporal [39, 143, 20, 78]
182 of 238 Eh dot and 98 to 101 of 134 to 137 Ev dot cells are nonlinear. Slope-sign rule: Eh dot 39 asymmetric and 143 symmetric, 21 of 39 temporal (P = 0.749). Shuffle rule: 78 asymmetric and 104 symmetric, 39 to 41 of 78 temporal (P = 0.73 to 1.0). Ev dot asymmetric cells show no preference (P = 0.08 to 1.0). The horizontal test fails under every combination; at most two of four class counts are within tolerance. Round 2: with the literal preference reading (b) and the shuffle rule, 47 of 78 asymmetric Eh dot cells prefer temporal movement (P = 0.089), still not significant, and t
[... 68 more lines not kept]
```

**Agent calls Bash**

```bash
date -u; cd  python - <<'EOF'
import yaml
d=yaml.safe_load(open("attempts/mallory-2021-01.yaml"))
ids=[o['claim'] for o in d['outcomes']]
print(len(ids)); print({o['claim']:(o['outcome'],o.get('assumed')) for o in d['outcomes']})
print(d['verifications'][-1].keys(), len(d['verifications']), d['verifications'][-1]['reviewed'])
for f in d['findings']: print(f.get('kind'), str(f)[:150])
EOF
```

```
Wed Nov 11 10:57:21 UTC 2026
47
{'headfixed-session-link': ('reproduced', None), 'fig1b-head-posture-distributions': ('reproduced', None), 'fig1c-head-direction-cells': ('reproduced', True), 'fig1c-pitch-roll-cells': ('not_reproduced', True), 'fig1c-pitch-roll-velocity-rare': ('reproduced', True), 'fig1c-azimuthal-velocity-cells': ('blocked', None), 'fig1d-conjunctive-head': ('partially_reproduced', True), 'fig2-pitch-roll-shapes': ('not_reproduced', True), 'fig2a-pitch-up-down-similar': ('reproduced', True), 'fig2b-roll-left-right-similar': ('reproduced', True), 'fig2-pitch-roll-stability': ('reproduced', True), 'fig2c-azimuthal-velocity-shapes': ('blocked', None), 'fig2c-velocity-extrema-near-zero': ('blocked', None), 'fig2c-symmetric-asymmetric-classes': ('blocked', None), 'fig2c-asymmetric-direction-similar': ('blocked', None), 'fig2c-velocity-stability': ('blocked', None), 'fig3ab-head-contributions': ('blocked', None), 'fig3c-freely-moving-model-fit': ('blocked', None), 'fig3e-head-no-clustering': ('blocked', None), 'fig4f-eye-movement-distributions': ('reproduced', None), 'fig4j-eye-encoding-cells': ('reproduced', None), 'fig4k-eye-conjunctive': ('reproduced', None), 'fig5a-eh-nasal-temporal-similar': ('partially_reproduced', None), 'fig5b-ev-up-down-similar': ('reproduced', None), 'fig5-eye-position-stability': ('partially_reproduced', None), 'fig5av-eh-linear-most-stable': ('reproduced', None), 'fig5bv-ev-low-order-more-stable': ('partially_reproduced', None), 'fig6-eye-velocity-linear-nasal': ('partially_reproduced', None), 'fig6-eye-velocity-nonlinear-temporal': ('not_reproduced', None), 'fig6-eye-velocity-stability': ('not_reproduced', None), 'fig6v-asymmetric-more-stable': ('partially_reproduced', None), 'fig7ab-eye-contributions': ('reproduced', None), 'fig7c-head-fixed-model-fit': ('reproduced', None), 'fig7e-eye-no-clustering': ('not_reproduced', None), 'fig8c-eye-tuning-without-landmarks': ('blocked', None), 'fig8e-joint-cells-preserve-eye-tuning': 
[... 12 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat > $TMPDIR/dev/rec.py <<'PYEOF'
import yaml
P = "attempts/mallory-2021-01.yaml"
d = yaml.safe_load(open(P))
O = {o["claim"]: o for o in d["outcomes"]}

def sub(text, old, new):
    assert old in text, old[:70]
    return text.replace(old, new)

COH1 = ["fig1c-head-direction-cells", "fig1c-pitch-roll-cells", "fig1c-pitch-roll-velocity-rare", "fig1d-conjunctive-head",
        "fig2-pitch-roll-shapes", "fig2a-pitch-up-down-similar", "fig2b-roll-left-right-similar", "fig2-pitch-roll-stability",
        "supp4-head-ln-conservative", "supp5-head-model-raw-tuning-agree"]
CLOCK = ("The outcome rests on the deposit's alignment of spikes and behaviour (assumed). The clock check in the freely "
         "moving notebook was inconclusive: the shift of best tuning has a median of -0.20 s for position and -0.40 s for "
         "pitch, by mouse from -0.4 to +1.4 s for position, and only 0.18 and 0.24 of the most strongly tuned quarter of "
         "cells peak within 0.2 s of no shift. A misalignment would lower the counts of encoding cells and the stability "
         "of their tuning.")
DROP = ("Under reading (2a) the bins outside any variable's inner 95% are dropped, a median of 0.307 of the valid bins "
        "(kept fraction 0.693, range 0.674 to 0.751, freely moving notebook); reading (2b), clipping, keeps all of them "
        "and was not run (about 1.44 times the bins, so about 45 min for one reading), so the counts may depend on it.")
for c in COH1:
    o = O[c]
    for k in ("notes",):
        o[k] = o[k].replace("32.4 min", "31.4 min").replace("32.4\n    min", "31.4 min")
    o["deviations"] = [x.replace("takes 32 min", "takes 31 min") for x in o["deviations"]] + [CLOCK, DROP]
    o["notes"] = o["notes"].replace("32.4 min", "31.4 min")
    assert "32.4" not in o["notes"], c

# fig1c-azimuthal: report the Cohort 1 count
o = O["fig1c-azimuthal-velocity-cells"]
o["notes"] = sub(o["notes"], "The Cohort 1 count needs the Cohort 1 LN model, which did not finish within the 60-minute limit of a notebook cell. ",
    "")
o["notes"] = sub(o["notes"], "so one reading needs about an hour on four cores, and reading", "and reading")
o["notes"] = sub(o["notes"], "(one reading, 32.4 min for 179 cells on four cores)", "(one reading, 31.4 min for 179 cells on four cores)")
o["notes"] += (" Round 3: the Cohort 1 count is computed by the Cohort 1 LN model under readings (1a, 2a): 10 cells encode "
               "azimuthal head velocity (freely moving notebook, cell 14), outside 12 +- 1.2. So under this reading the "
               "claim could be at most partially reproduced, and only if the Cohort 2 count were within tolerance; the other "
               "readings of Cohort 1 and the Cohort 2 count were not run, so the claim stays blocked.")
for c in ["fig2c-azimuthal-velocity-shapes", "fig2c-velocity-extrema-near-zero", "fig2c-symmetric-asymmetric-classes",
          "fig2c-asymmetric-direction-similar", "fig2c-velocity-stability", "fig3ab-head-contributions",
          "fig3c-freely-moving-model-fit", "fig3e-head-no-clustering", "supp9-head-correlation-contributions"]:
    o = O[c]
    n = o["notes"]
    n = n.replace("(about an hour per reading on four cores, not run)", "(not run)")
    n = n.replace("about an hour per reading on four cores", "not run")
    n = n.replace("(did not finish within the 60-minute cell limit)", "(now run under one reading, 31.4 min)")
    n = n.replace("32.4 min", "31.4 min")
    assert "an hour" not in n and "32.4" not in n, (c, n)
    o["notes"] = n
for c in ["supp3-head-low-false-positives"]:
    O[c]["notes"] = O[c]["notes"].replace("32.4 min", "31.4 min")
o = O["supp3-eye-low-false-positives"]
o["notes"] = sub(o["notes"], "the main run took 2099 s for the 2861 units (reproduce_mallory_2021.ipynb),\n    so about 3.5 h",
                 "the main run takes about 34 min for the 2861 units (reproduce_mallory_2021.ipynb)")
o["notes"] = o["notes"].replace("the main run took 2099 s for the 2861 units (reproduce_mallory_2021.ipynb), so about 3.5 h",
                                "the main run takes about 34 min for the 2861 units (reproduce_mallory_2021.ipynb)") if "2099" in o["notes"] else o["notes"]
o["notes"] = o["notes"].replace("33 min on four cores (1961\n    s, main notebook)", "34 min on four cores (2021 s, main notebook, round 3 run)").replace(
    "33 min on four cores (1961 s, main notebook)", "34 min on four cores (2021 s, main notebook, round 3 run)")
o["notes"] = o["notes"].replace("about 3.3 h", "about 3.4 h")
assert "1961" not in o["notes"] and "2099" not in o["notes"], o["notes"]

# stale head-fixed notes
o = O["supp4-eye-ln-conservative"]
o["notes"] = sub(o["notes"], "(within-cell 1132, 771, 1062 and 1004 of 2861 units, pooled 885, 410, 925 and 871,",
                 "(within-cell 1132, 771, 1309 and 1178 of 2861 units, pooled 885, 410, 1158 and 1024, the velocity counts with the Methods' symmetric test,")
o["notes"] = sub(o["notes"], "but within-cell shuffling finds only 0.718, 0.609, 0.794 and 0.781 of the LN cells, below the criterion's 90% reading of \"nearly all\" (pooled 0.642, 0.638, 0.752 and 0.774).",
                 "but within-cell shuffling finds only 0.718 and 0.609 of the Eh and Ev LN cells and 0.891 of the Ev dot cells, below the criterion's 90% reading of \"nearly all\" (Eh dot 0.933; pooled 0.642, 0.638, 0.916 and 0.898).")
o = O["fig5a-eh-nasal-temporal-similar"]
o["notes"] = sub(o["notes"], "preference reading (b) and both readings of explored range give P from 0.19 to 0.23.",
                 "preference reading (b), the larger absolute slope, gives 155 of 341 (P = 0.104), variant (r) 158 of 341 (P = 0.194), and on the cells classified under either reading of explored range P is 0.103 to 0.232.")
o = O["fig5b-ev-up-down-similar"]
o["notes"] = sub(o["notes"], "preference reading (b) gives 81 of 172, P = 0.493. Round 2: literal preference reading (b) gives 82 of 172 upward, P = 0.594.",
                 "the literal preference reading (b) gives 82 of 172 upward, P = 0.594, and variant (r) 81 of 172, P = 0.493.")
o = O["fig6-eye-velocity-nonlinear-temporal"]
o["notes"] = sub(o["notes"], "39 to 41 of 78 temporal (P = 0.73 to 1.0). Ev dot asymmetric cells show no preference (P = 0.08 to 1.0).",
                 "39 to 47 of 78 temporal (P = 0.089 to 1.0). The Ev dot test gives P from 0.0026 to 1.0 over the 12 combinations, so it too finds a preference under some of them.")

# fold-reading outcomes: mark assumed
FOLD = ("Assumed: reading (1a), 10-s sections assigned to folds in turn as compute_test_train_ind.m does, the code the "
        "paper links; the Methods say only that the session was divided into 10-s sections for 10-fold cross-validation. "
        "Under reading (1b), random folds, the outcome differs (readings notebook), so it rests on (1a). The eye-cell "
        "counts of fig4j, within tolerance under (1a) (718) and outside it under (1b) (614), support (1a).")
for c, extra in (("fig7ab-eye-contributions", " Under (1b) reading (c) with fold 1 gives 10 of 12 comparisons and 1 of 6 medians within tolerance, and no fold meets both parts, so the reproduction also rests on the single held-out section being fold 1."),
                 ("fig5bv-ev-low-order-more-stable", " Under (1b) every condition of the criterion holds (Kruskal-Wallis P = 6.8e-6, linear and quadratic against higher P = 0.00024 and 1.7e-5, medians 0.855 and 0.838 within tolerance), which would give reproduced; the outcome stays partial on (1a), the reading on which fig7ab is reproduced, so the two are treated alike."),
                 ("fig6-eye-velocity-linear-nasal", " Under (1b) the nasal test fails (33 of 52, P = 0.070)."),
                 ("fig6v-asymmetric-more-stable", " Under (1b) neither part holds.")):
    o = O[c]
    items = list(o.items())
    o.clear()
    for k, v in items:
        o[k] = v
        if k == "outcome":
            o["assumed"] = True
    o["deviations"] = o["deviations"] + [FOLD + extra]
o = O["fig7ab-eye-contributions"]
o["notes"] += (" Round 3: under (1b) reading (c) with fold 1 gives 10 of 12 comparisons and 1 of 6 medians, and no fold "
               "meets both parts (readings notebook); the outcome is now marked as resting on reading (1a) and on fold 1.")
o = O["fig5bv-ev-low-order-more-stable"]
o["notes"] += " Round 3: the outcome is now marked as resting on reading (1a), as for fig7ab."
for c in ("fig6-eye-velocity-linear-nasal", "fig6v-asymmetric-more-stable"):
    O[c]["notes"] += " Round 3: the outcome is now marked as resting on reading (1a)."

# supp12: proposed
o = O["supp12-no-false-eye-detection"]
o["notes"] = sub(o["notes"], "Round 2: one head-fixed LN run takes 33 min on four cores (1961 s); the main notebook, at 51 min, cannot\n    hold another",
                 "Round 2: one head-fixed LN run takes 33 to 34 min on four cores; the main notebook, at about 50 min, cannot hold another") if "1961 s); the main notebook, at 51 min, cannot\n    hold" in o["notes"] else o["notes"].replace("33 min on four cores (1961 s); the main notebook, at 51 min,", "33 to 34 min on four cores; the main notebook, at about 50 min,")
assert "1961" not in o["notes"], o["notes"]
o["notes"] += (" Round 3: now run in its own notebook, simulated_eye_mallory_2021.ipynb (41.3 min), which repeats the forward "
               "search of the main readings (1a, 2a) (718 eye cells, 341, 243, 238 and 137 for Eh, Ev, Eh dot and Ev dot, as "
               "in the main notebook), draws Poisson spike trains from each eye cell's selected model with the eye terms "
               "deleted (Methods, Generating simulated data without eye-encoded information), and reruns the forward search. "
               "Mutual information of each eye variable with B (four pairs) and of each eye velocity with Bs (two pairs) exceeds "
               "all 100 permutation shuffles in 11 of 11 sessions for every pair (circular shifts of more than 20 s: 11 of 11, "
               "and 10 of 11 for Ev with B). In the simulated data Eh is detected in 0 cells, Ev in 2, Eh dot in 2 and Ev dot "
               "in 0 (fractions 0.000 to 0.008 of the original counts, all at most 10%); a random 300 of the 1422 encoding cells "
               "without eye terms, simulated from their unchanged models, give no eye detection. B and Bs are kept in every "
               "simulated eye cell that encoded them (635 of 635, 456 of 456). Simulated mean rates are higher than in the data "
               "for the eye cells (median 7.48 against 4.84 Hz), since deleting the eye terms removes their mean as well.")
o["deviations"] = [
    "The simulated cells are the 718 eye cells and a seeded random 300 of the 1422 encoding cells without eye terms (assumed; the Methods start from a cell's selected variables, so cells encoding nothing have no model, and cells without eye terms are simulated from their unchanged model, where an eye detection would be the ordinary false positive rate of Supp. Fig. 3); the paper may have simulated every encoding cell.",
    "Spikes are drawn from the selected model's parameters fitted on the whole session; the mean of the fold parameters (param_mean) is the other reading of \"the model parameters\" and was not run.",
    "Mutual information uses 20 equal-width bins over each variable's inner 98% of the kept bins, a standard choice; the shuffles permute the eye variable over time, with circular shifts of more than 20 s as a stricter variant.",
    "Only readings (1a, 2a) of the LN pipeline are run for this claim.",
]
o["proposed"] = {"outcome": "reproduced",
                 "reason": ("Now run (simulated_eye_mallory_2021.ipynb): the data mutual information exceeds all 100 shuffles in "
                            "11 of 11 sessions for each of the six pairs, and in the simulated data without eye terms the eye "
                            "variables are detected in 0, 2, 2 and 0 cells against 341, 243, 238 and 137 in the data, at most "
                            "0.008 of the original, within the criterion's 10%. It rests on simulating the eye cells and a sample "
                            "of the other encoding cells, and on readings (1a, 2a).")}
o["notebook"] = "simulated_eye_mallory_2021.ipynb"
o["output"] = "claim:supp12-no-false-eye-detection"
d["_o"] = None
del d["_o"]
yaml.safe_dump  # noqa
open(P, "w").write(yaml.dump(d, sort_keys=False, width=110, allow_unicode=True))
PYEOF
python $TMPDIR/dev/rec.py && git diff --stat attempts/
```

```
Exit code 1
Traceback (most recent call last):
  File "/tmp/claude-1001/dev/rec.py", line 53, in <module>
    o["notes"] = sub(o["notes"], "the main run took 2099 s for the 2861 units (reproduce_mallory_2021.ipynb),\n    so about 3.5 h",
                 ~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
                     "the main run takes about 34 min for the 2861 units (reproduce_mallory_2021.ipynb)")
                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/tmp/claude-1001/dev/rec.py", line 7, in sub
    assert old in text, old[:70]
           ^^^^^^^^^^^
AssertionError: the main run took 2099 s for the 2861 units (reproduce_mallory_2021.ip
```

**Agent calls Bash**

```bash
cd  python - <<'EOF'
p="/tmp/claude-1001/dev/rec.py"; s=open(p).read()
a=s.index('o["notes"] = sub(o["notes"], "the main run took 2099 s'); b=s.index('o["notes"] = o["notes"].replace("the main run took 2099 s')
s=s[:a]+s[b:]
open(p,"w").write(s)
EOF
python $TMPDIR/dev/rec.py && git diff --stat attempts/
```

```
attempts/mallory-2021-01.yaml | 350 +++++++++++++++++++++++++++++-------------
 1 file changed, 243 insertions(+), 107 deletions(-)
```

**Agent calls Bash**

```bash
cd  sed -i 's/ Round 3: / After round 2: /g' attempts/mallory-2021-01.yaml; grep -c "After round 2" attempts/mallory-2021-01.yaml; python - <<'EOF'
import yaml
d=yaml.safe_load(open("attempts/mallory-2021-01.yaml"))
O={o['claim']:o for o in d['outcomes']}
for c in ("supp3-eye-low-false-positives","supp12-no-false-eye-detection","fig1c-azimuthal-velocity-cells","fig2c-azimuthal-velocity-shapes"):
    print(c, O[c]['notes'],"\n")
EOF
```

```
6
supp3-eye-low-false-positives The answer split the earlier claim supp3-low-false-positives (blocked as data_missing, on its dependency on fig1c-head-direction-cells) into a head part, `data: elsewhere` on the figshare deposits, and an eye part on the dandiset, with the rule divided between the parts. This eye part needs six more runs of the whole head-fixed LN pipeline, one per shuffled variable; the main run takes about 34 min for the 2861 units (reproduce_mallory_2021.ipynb), beyond the time limit; not run. Round 2: one head-fixed LN run takes 34 min on four cores (2021 s, main notebook, round 3 run), so the six shuffled reruns need about 3.4 h, over the notebook limit and the time left; not run. 

supp12-no-false-eye-detection Needs spike trains simulated from every cell's fitted model without its eye terms and the whole LN pipeline rerun on them, one more full run of about 35 min, with the mutual-information shuffles; not run within the time limit. Round 2: one head-fixed LN run takes 33 to 34 min on four cores; the main notebook, at about 50 min, cannot hold another, and the run had no time left for a separate notebook; not run. After round 2: now run in its own notebook, simulated_eye_mallory_2021.ipynb (41.3 min), which repeats the forward search of the main readings (1a, 2a) (718 eye cells, 341, 243, 238 and 137 for Eh, Ev, Eh dot and Ev dot, as in the main notebook), draws Poisson spike trains from each eye cell's selected model with the eye terms deleted (Methods, Generating simulated data without eye-encoded information), and reruns the forward search. Mutual information of each eye variable with B (four pairs) and of each eye velocity with Bs (two pairs) exceeds all 100 permutation shuffles in 11 of 11 sessions for every pair (circular shifts of more than 20 s: 11 of 11, and 10 of 11 for Ev with B). In the simulated data Eh is detected in 0 cells, Ev in 2, Eh dot in 2 and Ev dot in 0 (fractions 0.000 to 0.008 of the original counts, all at most 10%); a
[... 4 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -i 's/ (2021 s, main notebook, round 3 run)/ (2021 s, main notebook)/' attempts/mallory-2021-01.yaml; cat > $TMPDIR/dev/ver.py <<'PYEOF'
import yaml
P = "attempts/mallory-2021-01.yaml"
d = yaml.safe_load(open(P))
O = {o["claim"]: o for o in d["outcomes"]}
R = {}
AGREE = ["headfixed-session-link", "fig1b-head-posture-distributions", "fig4f-eye-movement-distributions", "fig4j-eye-encoding-cells",
         "fig4k-eye-conjunctive", "fig5a-eh-nasal-temporal-similar", "fig5b-ev-up-down-similar", "fig5-eye-position-stability",
         "fig5av-eh-linear-most-stable", "fig6-eye-velocity-nonlinear-temporal", "fig6-eye-velocity-stability", "fig7c-head-fixed-model-fit",
         "fig7e-eye-no-clustering", "supp4-eye-ln-conservative", "supp5-eye-model-raw-tuning-agree", "supp7e-eye-velocity-extrema-near-zero"]
STALE = {"supp4-eye-ln-conservative": "The notes' within-cell, pooled and pooled-fraction numbers for the velocity variables were round-1 numbers; main cell 75 prints within-cell 1309 and 1178, pooled 1158 and 1024, and pooled fractions 0.916 and 0.898.",
         "fig5a-eh-nasal-temporal-similar": "The notes' \"preference reading (b) and both readings of explored range give P from 0.19 to 0.23\" is stale; under the reading now called (b), cell 36 gives P = 0.104.",
         "fig5b-ev-up-down-similar": "The notes' \"preference reading (b) gives 81 of 172, P = 0.493\" is stale; cell 39 gives (b) as 82 of 172, P = 0.594, and 81 and 0.493 are variant (r).",
         "fig6-eye-velocity-nonlinear-temporal": "The notes' \"39 to 41 of 78 temporal (P = 0.73 to 1.0)\" and \"Ev dot ... P = 0.08 to 1.0\" are stale; cell 54 gives 39 to 47 of 78, and Ev dot P from 0.0026 to 1.0."}
for c in AGREE:
    reason = "Agrees with the outcome; the assumptions are stated and reasonable."
    resp = "No change of outcome."
    if c in STALE:
        reason += " " + STALE[c]
        resp = "Notes corrected to the printed numbers; no change of outcome."
    if c == "headfixed-session-link" or c == "fig1b-head-posture-distributions":
        pass
    R[c] = (True, O[c]["outcome"], reason, resp)
R["supp9-eye-correlation-contributions"] = (True, "partially_reproduced", "Agrees; assumed on reading (a), which is stated.", "No change.")
for c, extra in (("fig8c-eye-tuning-without-landmarks", " The trial tables are now printed (cells 13 and 14)."),
                 ("fig8e-joint-cells-preserve-eye-tuning", " The trial tables are now printed (cells 13 and 14)."),
                 ("methods-hemispheres-similar", "")):
    R[c] = (True, "blocked", "Agrees with the block." + extra, "No change.")
COH1 = ["fig1c-head-direction-cells", "fig1c-pitch-roll-cells", "fig1c-pitch-roll-velocity-rare", "fig1d-conjunctive-head",
        "fig2-pitch-roll-shapes", "fig2a-pitch-up-down-similar", "fig2b-roll-left-right-similar", "fig2-pitch-roll-stability",
        "supp4-head-ln-conservative", "supp5-head-model-raw-tuning-agree"]
for c in COH1:
    reason = ("Agrees with the outcome against its criterion on the printed numbers. The assumed statement names only "
              "readings (1a, 2a) and leaves out two assumptions: the clock alignment, whose check was inconclusive (best lag "
              "median -0.20 s for position and -0.40 s for pitch, by mouse -0.4 to +1.4 s, only 0.18 and 0.24 of the strongest "
              "cells within 0.2 s), which would lower exactly the counts that fail; and bin dropping, under which 31% of the "
              "bins are dropped, where reading (2b), clipping, would keep all of them and the not-reproduced counts may depend on it.")
    resp = ("Both assumptions are now deviations of this outcome, with the clock check's numbers and the kept fraction "
            "(0.693); the free notebook's clock text no longer says the tested claims do not depend on the clock. Reading "
            "(2b) on Cohort 1 was not run: it keeps about 1.44 times the bins, so about 45 min, which did not fit after the "
            "re-runs this revision needed; reading (1b) on Cohort 1 was not run either, for the same reason. The timing "
            "is corrected to 31.4 min. No change of outcome.")
    R[c] = (True, O[c]["outcome"], reason, resp)
R["fig7ab-eye-contributions"] = (True, "reproduced",
    "Agrees only on the letter of the criterion (\"under one reading\"): the reproduction rests on reading (c) with fold 1; in the per-fold table only fold 1 of 10 meets both parts of the rule, and under (1b) reading (c) with fold 1 gives 10 of 12 tests and 1 of 6 medians and no fold meets both. The outcome should be marked assumed: true and the record should say that it fails under (1b); without that the verifier would record partially reproduced, since the tests hold under (a) in both fold readings, with 2 of 6 medians.",
    "Marked assumed: true, with a deviation that states reading (1a) and that under (1b) the outcome fails (10 of 12 and 1 of 6 with fold 1, no fold meeting both); main cell 64, the main summary, the folds summary and the README now say so. Outcome kept.")
R["fig5bv-ev-low-order-more-stable"] = (True, "partially_reproduced",
    "Under (1b) every condition of the criterion holds (KW P = 6.8e-6, linear vs higher P = 0.00024, quadratic vs higher P = 1.7e-5, medians 0.855 and 0.838 within tolerance), so the criterion's \"under one reading\" gives reproduced. Keeping it partial means committing to (1a), which must be marked as assumed; that same commitment keeps fig7ab reproduced, so the two should be treated alike.",
    "Kept partial and marked assumed: true on reading (1a), as fig7ab now is, with a deviation that gives the (1b) numbers and says they would give reproduced.")
for c, r in (("fig6-eye-velocity-linear-nasal", "Holds only under (1a); under (1b) the nasal test gives P = 0.070. The notes say so, but the assumed flag is missing."),
             ("fig6v-asymmetric-more-stable", "Holds only under (1a); under (1b) fig6v gives neither part. The notes say so, but the assumed flag is missing.")):
    R[c] = (True, "partially_reproduced", r, "Marked assumed: true on reading (1a), with a deviation; outcome kept.")
COH2 = ["fig2c-azimuthal-velocity-shapes", "fig2c-velocity-extrema-near-zero", "fig2c-symmetric-asymmetric-classes",
        "fig2c-asymmetric-direction-similar", "fig2c-velocity-stability", "fig3ab-head-contributions",
        "fig3c-freely-moving-model-fit", "fig3e-head-no-clustering", "supp9-head-correlation-contributions"]
for c in COH2:
    R[c] = (True, "blocked", "Acceptable as too_large on the measured estimate of about 3 h. The notes said \"about an hour per reading on four cores\" and then \"about 3 h\".",
            "The stale \"about an hour\" estimate is removed; the notes keep the measured 3 h estimate. No change.")
R["fig1c-azimuthal-velocity-cells"] = (True, "blocked",
    "Acceptable as too_large on the measured estimate of about 3 h, but the Cohort 1 part is already computed: Had = 10 cells (free cell 14), outside 12 +- 1.2, so the claim can be at most partially reproduced and the record should report the 10. The notes' statement that the Cohort 1 model did not finish is stale, as is \"about an hour per reading\".",
    "The notes now report the Cohort 1 count of 10, outside tolerance, and that the claim could be at most partial; the stale sentences are removed. Kept blocked, since the Cohort 2 count was not run.")
R["supp3-head-low-false-positives"] = (True, "blocked", "Acceptable as too_large on the measured estimate of 3.2 h.", "Timing corrected to 31.4 min per run; no change.")
R["supp3-eye-low-false-positives"] = (True, "blocked", "Acceptable as a run-budget block. The notes' \"2099 s\" and \"33 min ... (1961 s)\" do not match main cell 24, which prints 1989 s.",
    "Timing corrected to the new run's main cell 24 (2021 s, about 34 min; six reruns about 3.4 h). No change.")
R["supp12-no-false-eye-detection"] = (False, "blocked",
    "It needs one more head-fixed run of about 33 min; a separate notebook would fit the 60-minute limit, as the 43-minute readings notebook does, so the block is the run's time, not size.",
    "Now run in a separate notebook, simulated_eye_mallory_2021.ipynb (41.3 min): reproduced under its criterion (mutual information above all 100 shuffles in 11 of 11 sessions for each pair; eye variables detected in 0, 2, 2 and 0 simulated cells against 341, 243, 238 and 137). The verified outcome stays blocked, and the change to reproduced is under proposed, for round 3.")
assert set(R) == set(O), set(O) ^ set(R)
results = []
for c in [o["claim"] for o in d["outcomes"]]:
    a, out, reason, resp = R[c]
    results.append({"claim": c, "agrees": a, "outcome": out, "reason": reason, "response": resp})
d["verifications"].append({"date": "2026-11-11", "kind": "agent", "by": "claude-opus-5-5 (Claude Code), verifier-2",
    "reviewed": "The full executed notebooks of round 2 with their conclusions and summaries, mec_ln.py, mec_free.py, the claims file and the attempt record",
    "results": results})
open(P, "w").write(yaml.dump(d, sort_keys=False, width=110, allow_unicode=True))
PYEOF
python $TMPDIR/dev/ver.py && date -u
```

```
Wed Nov 11 10:58:48 UTC 2026
```

**Agent calls Bash**

```bash
cd  python - <<'EOF'
p="attempts/mallory-2021-01.yaml"; s=open(p).read()
import yaml
d=yaml.safe_load(s)
for r in d['verifications'][-1]['results']:
    r['response']=r['response'].replace("which did not fit after the re-runs this revision needed; reading (1b) on Cohort 1 was not run either, for the same reason.",
      "and the time left in this run after the re-runs and the new Supp. Fig. 12 notebook did not allow it; reading (1b) on Cohort 1 was not run either, for the same reason.")
open(p,"w").write(yaml.dump(d,sort_keys=False,width=110,allow_unicode=True))
EOF
grep -n "—\|rather" attempts/mallory-2021-01.yaml entries/mallory-2021/README.md | head; python tools/entry.py check entries/mallory-2021 2>&1 | tail -20
```

```
0 error(s)
```

**Agent calls Bash**

```bash
cd  grep -c "—\| rather" entries/mallory-2021/simulated_eye_mallory_2021.ipynb executed/mallory-2021/simulated_eye_mallory_2021.ipynb; python - <<'EOF'
import yaml
d=yaml.safe_load(open("attempts/mallory-2021-01.yaml"))
for f in d['findings']:
    if f['kind']=='methods_unavailable': print(f)
EOF
```

```
entries/mallory-2021/simulated_eye_mallory_2021.ipynb:0
executed/mallory-2021/simulated_eye_mallory_2021.ipynb:0
{'kind': 'methods_unavailable', 'statement': "Questions for the paper's authors. (1) How were the 10-s sections assigned to folds? In turn, as compute_test_train_ind.m does, the eye-cell count is 718 (paper 711); at random it is 614. (2) Was the contribution normalized as (full - reduced) / full? The literal wording of the Methods ('subtracted from 1') inverts the paper's order of variables; a single held-out section, as compute_llh_increase.m, matches the medians best. (3) What rule separated symmetric from asymmetric velocity cells? Neither the slope-sign rule nor the shuffle rule gives the paper's 147 asymmetric Eh dot cells (39 and 78 here). (4) Which side is a cell's preference under 'the larger absolute slope' (a question of sign for velocity cells)? The literal reading and the steeper rise away from 0 give different counts (fig6 nonlinear asymmetric Eh dot: 47 and 39 of 78 temporal)."}
```

**Agent calls Bash**

```bash
cd  python - <<'EOF'
p="attempts/mallory-2021-01.yaml"
import yaml
d=yaml.safe_load(open(p))
for f in d['findings']:
    if f['kind']=='methods_unavailable':
        f['statement'] += (" (5) For Supplementary Fig. 12, which cells were simulated (every encoding cell, or the eye cells), "
            "and were the spikes drawn from the full-session fit or the mean of the fold parameters? Here the 718 eye cells and "
            "a sample of 300 other encoding cells are simulated from the full-session fit; no eye variable is detected in more "
            "than 2 simulated cells. (6) Were out-of-range bins dropped or clipped in the open field LN model? Dropping removes "
            "31% of the Cohort 1 bins.")
open(p,"w").write(yaml.dump(d,sort_keys=False,width=110,allow_unicode=True))
EOF
python tools/entry.py check entries/mallory-2021 2>&1 | tail -3; python tools/entry.py handover entries/mallory-2021 2>&1 | tail -2; date -u
```

```
0 error(s)
wrote executed/mallory-2021/handover
Wed Nov 11 10:59:29 UTC 2026
```

**Agent calls Bash**

```bash
cd  rm -rf entries/mallory-2021/__pycache__; cat > $TMPDIR/dev/edit4.py <<'PYEOF'
import json
exec(open("/tmp/claude-1001/dev/edit2.py").read().split("FR = ")[0])
edit("reproduce_mallory_2021.ipynb", 0, "| supp12-no-false-eye-detection | blocked: too large for the time limit |",
     "| supp12-no-false-eye-detection | blocked: too large for this notebook; now run in `simulated_eye_mallory_2021.ipynb`, with a proposed change of outcome |")
PYEOF
$TMPDIR/venv/bin/python $TMPDIR/dev/edit4.py; python - <<'EOF'
p="entries/mallory-2021/entry.yaml"; s=open(p).read()
old="""  limit. The no-landmark track and the hemisphere
  comparison are blocked."""
assert old in s
s=s.replace(old,"""  limit. Supplementary Figure 12, spike trains simulated without eye terms, is run in its own notebook.
  The no-landmark track and the hemisphere comparison are blocked.""")
open(p,"w").write(s)
import json
for f in ["reproduce_mallory_2021.ipynb","freely_moving_mallory_2021.ipynb","readings_folds_mallory_2021.ipynb","simulated_eye_mallory_2021.ipynb"]:
    nb=json.load(open("entries/mallory-2021/"+f)); print(f, sum(len(c.get('outputs',[])) for c in nb['cells'] if c['cell_type']=='code'))
EOF
python tools/entry.py check entries/mallory-2021 2>&1 | tail -2; python tools/entry.py handover entries/mallory-2021 2>&1 | tail -1; git status --short
```

```
reproduce_mallory_2021.ipynb 0
freely_moving_mallory_2021.ipynb 0
readings_folds_mallory_2021.ipynb 0
simulated_eye_mallory_2021.ipynb 0
0 error(s)
wrote executed/mallory-2021/handover
 M attempts/mallory-2021-01.yaml
 M entries/mallory-2021/README.md
 M entries/mallory-2021/entry.yaml
 M entries/mallory-2021/freely_moving_mallory_2021.ipynb
 M entries/mallory-2021/mec_ln.py
 M entries/mallory-2021/readings_folds_mallory_2021.ipynb
 M entries/mallory-2021/reproduce_mallory_2021.ipynb
 M tools/build_reuse_targets.py
 M tools/build_site.py
 M tools/entry.py
 M tools/notify.py
 M tools/papers_manifest.py
 M tools/runner/chain.sh
 M tools/runner/describe.py
[... 14 more lines not kept]
```

**Agent**

The revision is finished. No outcome changed, and the only proposed change is supp12 (blocked → reproduced), which goes to round 3. All four notebooks ran and passed, and `tools/entry.py check` reports 0 errors. Nothing is committed.

**Proposed change (verified outcome kept as blocked)**
- **supp12-no-false-eye-detection:** I ran it in a new notebook, `simulated_eye_mallory_2021.ipynb` (41.3 min). Each eye cell's spikes are simulated from its fitted model with the eye terms removed, and the LN pipeline is rerun.
  - Eye variables and body position or speed share information: the data value is above all 100 shuffles in 11 of 11 sessions for each of the six pairs.
  - In the simulated data the eye variables are found in 0, 2, 2 and 0 cells, against 341, 243, 238 and 137 in the real data. That is at most 0.8%, well inside the criterion's 10%.
  - It rests on two choices the paper leaves open: which cells to simulate (the 718 eye cells plus a random 300 of the other encoding cells) and which fitted parameters to use. Both are recorded as assumptions.

**Marked `assumed: true`, with the reason written into each outcome**
- **fig7ab:** stays reproduced, but only with folds assigned in turn and fold 1 held out. With random folds, fold 1 gives 10 of 12 comparisons and 1 of 6 medians, and no fold meets both parts.
- **fig5bv:** stays partially reproduced on the same fold reading. With random folds it would be reproduced; the record says so, so it is treated the same way as fig7ab.
- **fig6-eye-velocity-linear-nasal and fig6v:** both hold only with folds assigned in turn.
- **The ten Cohort 1 claims:** two assumptions are now stated on each. The check that spikes and behaviour share a clock was inconclusive, and dropping out-of-range bins removes 31% of them.

**Corrected**
- **Stale notes:** supp4-eye, fig5a, fig5b and fig6-nonlinear-temporal now match the printed numbers.
- **fig1c-azimuthal-velocity-cells:** now reports the Cohort 1 count of 10, outside 12 ± 1.2, so it could be at most partially reproduced. It stays blocked because the Cohort 2 count was not run.
- **Timings:** the "about an hour per reading" estimates are gone, and the timings now match this run (31.4 min, 2021 s, and the notebook runtimes).
- **Notebook text:** I fixed the stale passages the verifier quoted in the main notebook (cells 4, 22, 64), the freely moving notebook (cell 8) and the readings notebook's Summary. The summaries and the README now state these fold dependencies.

**Recorded**
- Round 2 is under `verifications` for all 47 claims, using the verifier's reasons and my responses. supp12 is recorded as a disagreement.
- I added two questions for the paper's authors: the supp12 choices, and whether out-of-range bins were dropped or clipped in the freely moving model.
- No question for a reader was added, because the verifier reported no misreading of the claims file this round.

**Not done**
- **Clipping out-of-range bins (2b) and random folds (1b) on Cohort 1, and clipping on the head-fixed data:** none of these were run. Rerunning the four notebooks took about 3 hours, and I gave the remaining time to supp12. The Cohort 1 clipping run would keep about 1.44 times the bins, so about 45 min. The record says these were not run and why.
- **Cohort 2 claims, supp3-head and supp3-eye:** still blocked as too large, about 3 to 3.4 h each.
- **How it was run:** the four notebooks together take longer than the 2-hour limit on one command. So, as in round 1, I ran them in two parts with `entry.yaml` cut down, then restored it and joined `result.json`.

## End of run

57 turns, 198 minutes, $5.12 at API prices, result: success.
