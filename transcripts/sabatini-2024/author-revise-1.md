# sabatini-2024 · author-revise-1 · run 44753392099

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
date -u; cat transcripts/sabatini-2024/verifier-1-report.md; ls entries/sabatini-2024 entries/sabatini-2024/*; wc -l docs/protocol.md
```

```
Fri Nov 20 14:31:38 UTC 2026
**A. Outcomes**

The claims file has 34 claims and the notebook tests all of them. My outcomes: 10 reproduced, 13 partially reproduced, 11 not reproduced, none blocked.

| Claim | Outcome | Reason |
|---|---|---|
| data-composition | reproduced | Both monkeys have 72 conditions (36 straight, 36 curved). Trial counts are within tolerance under both readings (J 1595/1381, N 2121/1884), and each array has 96 units, inside 71–130 (cell 13). The units carry no single/multi-unit label, so all units are counted (see B6). |
| jpca-fit-r2 | partially_reproduced | Under reading (a), straight (0.75–0.84) and curved (0.56–0.71) are all inside their ranges. For all conditions together, PMd-N's 0.452 falls outside 0.576–0.803, so 3 of 4 pass. The per-condition signed-rank test is significant only for M1-N, and it does not decide (cell 59). |
| jpca-variance-explained | partially_reproduced | Means are 8.9, 11.6, 11.7 and 5.1%; PMd-N falls below 6.3%. The s.d. is ≤11.6%, consistent with the paper's <13% (cell 61). |
| single-lds-variance | not_reproduced | Means are 0.77–0.82 under reading (a) and 0.79–0.87 under (b). All four are above 0.726 under both readings (cell 32). |
| fig2c-condition-lds-variance | reproduced | Chosen k is 5, 5, 7, 5 (all in 5–9, the same under all five seeds). Mean variance explained is 0.84–0.94, inside 63.9–100% (cell 15). |
| fig3a-eigenvalue-clusters | not_reproduced | Median pair frequencies are within 10% of the targets only for PMd-J (0.54, 1.53). M1-J (0.85, 2.35), M1-N (0.68, 1.74, 3.21) and PMd-N (0.73, 1.67) miss (cell 17). |
| fig3c-eigenvalue-distance-auc | not_reproduced | AUC under the Poisson null: 0.81, 0.71, 0.63, 0.70. Under the half-split null: 0.70, 0.64, 0.66, 0.68. At most one dataset is inside 0.459–0.638 under either null, and the result is stable across seeds (cell 20). |
| suppfig2-eigenvalues-from-kinematics | not_reproduced | Pooled mean R² is 0.275 under both kinematic readings, against 0.1 ± 0.0
[... 68 more lines not kept]
```

**Agent calls Bash**

```bash
date -u; cat docs/protocol.md
```

```
<persisted-output>
Output too large (46.1KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/d5bdbe57-c9bd-4c75-b8dd-bc572c7bb334/tool-results/byj290lko.txt

Preview (first 2KB):
Fri Nov 20 14:31:38 UTC 2026
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
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/d5bdbe57-c9bd-4c75-b8dd-bc572c7bb334/tool-results/byj290lko.txt"
}
```

```
1	Fri Nov 20 14:31:38 UTC 2026
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
[... 755 more lines not kept]
```

**Agent calls Bash**

```bash
ls attempts/ | grep sabatini; ls questions | grep sabatini; ls executed/sabatini-2024 2>/dev/null; cat entries/sabatini-2024/entry.yaml; wc -l attempts/sabatini-2024-01.yaml entries/sabatini-2024/ldr.py claims/sabatini-2024.yaml; ls transcripts/sabatini-2024/
```

```
sabatini-2024-01.yaml
reproduce_sabatini_2024.ipynb
result.json
schema_version: 1
name: sabatini-2024
type: reproduction
title: Reach-dependent reorientation of rotational dynamics in motor cortex (Sabatini & Kaufman 2024)
description: Tests the findings of Sabatini and Kaufman (2024) on dandiset 000070, which holds the two
  maze-task sessions the paper names (monkeys J and N, a PMd and an M1 Utah array each). It rebuilds the
  four datasets from the units, trials and hand position, and tests jPCA, single-condition dynamics, the
  temporal basis factorization, the alignment and dimensionality of rotational planes, the state space
  location, and LDR encoding and decoding.
license: Apache-2.0
python: "3.13"
notebooks:
- path: reproduce_sabatini_2024.ipynb
  title: Reproducing Sabatini & Kaufman (2024) from dandiset 000070
  runtime_minutes: 30
helpers:
- ldr.py
[... 17 more lines not kept]
```

**Agent calls Bash**

```bash
cat attempts/sabatini-2024-01.yaml
```

```
schema_version: 3
id: sabatini-2024-01
datasets:
- archive: dandi
  id: "000070"
  version: 0.260528.0919
  doi: 10.48324/dandi.000070/0.260528.0919
  relation: reuses
paper: doi:10.1038/s41467-024-51308-7
date: 2026-11-20
entry: sabatini-2024
provenance:
  kind: agent
  accountable:
    name: CatalystNeuro
  agent:
    harness: Claude Code
    model: claude-opus-5-5
    protocol: pilot-18
  runner:
[... 470 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/sabatini-2024; python -c "
import json
nb=json.load(open('reproduce_sabatini_2024.ipynb'))
for i,c in enumerate(nb['cells']):
    s=''.join(c['source'])
    print(f'=== cell {i} [{c[\"cell_type\"]}] tags={c.get(\"metadata\",{}).get(\"tags\",[])} lines={s.count(chr(10))+1}')
    print(s[:300])
" | head -700
```

```
<persisted-output>
Output too large (36.4KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/d5bdbe57-c9bd-4c75-b8dd-bc572c7bb334/tool-results/bnegzxo1f.txt

Preview (first 2KB):
=== cell 0 [markdown] tags=[] lines=32
# Reproducing Sabatini & Kaufman (2024) on DANDI:000070

**Paper.** Sabatini, D. A. & Kaufman, M. T. (2024). Reach-dependent reorientation of rotational dynamics
in motor cortex. *Nature Communications* 15, 7007. doi:10.1038/s41467-024-51308-7. The claims file
(`claims/sabatini-2024.yaml`) was writt
=== cell 1 [code] tags=[] lines=25
import os
for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ[_v] = "1"  # many small fits, some in parallel worker processes (protocol)
import time
import zlib
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import ldr
[... 32 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/sabatini-2024; python -c "
import json
nb=json.load(open('reproduce_sabatini_2024.ipynb'))
for i,c in enumerate(nb['cells']):
    s=''.join(c['source'])
    if c['cell_type']=='code':
        print(f'=== cell {i} tags={c.get(\"metadata\",{}).get(\"tags\",[])}')
        print(s)
" > $TMPDIR/code.txt; wc -l $TMPDIR/code.txt; ls -la ../../executed/sabatini-2024/; cat ../../executed/sabatini-2024/result.json | head -50
```

```
1143 /tmp/claude-1001/code.txt
total 596
drwxr-xr-x 3 runner runner   4096 Nov 20 14:11 .
drwxr-xr-x 3 runner runner   4096 Nov 20 14:31 ..
-rw-r--r-- 1 runner runner    321 Nov 20 14:11 .clean-run.json
drwxr-xr-x 5 runner runner   4096 Nov 20 13:48 .venv
-rw-r--r-- 1 runner runner 586681 Nov 20 14:11 reproduce_sabatini_2024.ipynb
-rw-r--r-- 1 runner runner    175 Nov 20 14:11 result.json
{
 "entry": "sabatini-2024",
 "python": "3.13",
 "results": [
  {
   "notebook": "reproduce_sabatini_2024.ipynb",
   "ok": true,
   "seconds": 1325,
   "error": null
  }
 ]
}
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/code.txt"
}
```

```
1	=== cell 1 tags=[]
2	import os
3	for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS"):
4	    os.environ[_v] = "1"  # many small fits, some in parallel worker processes (protocol)
5	import time
6	import zlib
7	import numpy as np
8	import matplotlib.pyplot as plt
9	from scipy import stats
10	import ldr
11	
12	T_START = time.time()
13	DATASETS = [("J", "M1"), ("J", "PMd"), ("N", "M1"), ("N", "PMd")]
14	NAME = {d: f"{d[1]}-{d[0]}" for d in DATASETS}
15	
16	
17	def seed(claim):
18	    """The claim's seed (protocol): crc32 of '<paper key>/<claim id>'."""
19	    return zlib.crc32(f"sabatini-2024/{claim}".encode())
20	
[... 785 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "entries/sabatini-2024/ldr.py"
}
```

```
1	"""Loading and measures for testing Sabatini & Kaufman (2024) on DANDI:000070.
2	
3	Where each parameter comes from is said beside it:
4	- "claims": the claim's criterion in claims/sabatini-2024.yaml (which cites the paper or its code);
5	- "Methods, <section>": a passage of the paper taken by the author (protocol, author step 1.6);
6	- "assumption": a choice the paper leaves open, recorded as a deviation in the attempt;
7	- "standard": a choice that cannot change a result (a padding margin, a plotting detail).
8	
9	The dandiset is read by streaming (remfile + h5py); nothing is written to disk.
10	"""
11	
12	from __future__ import annotations
13	
14	import numpy as np
15	import h5py
16	import remfile
17	import requests
18	from scipy.ndimage import gaussian_filter1d
19	
20	DANDISET = "000070"
[... 663 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/code.txt",
 "offset": 805
}
```

```
805	    vel.append(np.gradient(Hc, axis=1) / 0.01)
806	Bv, Bp_a, Sv = ldr.kin_basis(vel)
807	print("velocity singular values (top 5):", np.round(Sv[:5], 1), "share of the top two", np.round((Sv[:2] ** 2).sum() / (Sv ** 2).sum(), 3))
808	try:
809	    Bv_b, Bp_b = ldr.skewnorm_basis(ldr.GRID_MS.astype(float), Bv)
810	    print("skew-normal fit, correlation with the SVD velocity vectors:",
811	          [round(float(np.corrcoef(Bv[i], Bv_b[i])[0, 1]), 3) for i in range(2)])
812	except Exception as err:
813	    Bp_b = None
814	    print("skew-normal fit failed:", err)
815	KB = {"a": Bp_a, "b": Bp_b} if Bp_b is not None else {"a": Bp_a}
816	for m in ("J", "N"):
817	    for r, Bp in KB.items():
818	        P = ldr.reach_params(KIN[m]["Hc"], Bp)
819	        KIN[m]["P" + r] = P
820	        ve = np.mean([ldr.kin_ve(KIN[m]["Hc"][c], ldr.params_to_pos(P[c:c + 1], Bp)[0]) for c in range(72)])
821	        print(f"monkey {m}, reading ({r}): reach parameters reproduce condition-mean hand position with VE {ve:.3f}")
822	fig, ax = plt.subplots(1, 2, figsize=(8, 3))
823	ax[0].plot(ldr.GRID_MS, Bv.T); ax[0].set_title("velocity basis (a)")
824	ax[1].plot(ldr.GRID_MS, Bp_a.T); ax[1].set_title("position basis (a)")
[... 320 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "claims/sabatini-2024.yaml"
}
```

```
1	# Claims for Sabatini & Kaufman (2024), Nat. Commun. 15:7007, "Reach-dependent reorientation of
2	# rotational dynamics in motor cortex", tested on dandiset 000070 (relation reuses).
3	# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"), 2026-11-20,
4	# protocol pilot-18 as stated in docs/protocol.md. The writer did not look at the dandiset's data
5	# or files.
6	#
7	# Text read: the version of record (open access, CC BY-NC-ND), full text from PubMed Central
8	# (PMC11325044) with Methods, figure legends and Data and Code availability, and its one
9	# supplement, 41467_2024_51308_MOESM1_ESM.pdf (Supplementary Figures 1 to 8 with legends and the
10	# derivation of the basis function representation of a linear dynamical system). The Peer Review
11	# File and Reporting Summary were not read; no result rests on them. The supplement PDF was not
12	# opened beyond its extracted text.
13	#
14	# Code read: github.com/kaufmanlab/LDR-public at commit b65f28d (2024-08-02), the MATLAB code the
15	# Code availability statement links. It holds the analysis functions (TBF, single-condition LDS,
16	# alignment index, subspace excursion angles, rotation and location prediction, LDR encoding and
17	# decoding, jPCA reconciliation). It loads preprocessed .mat files that are not in the repository
18	# (ShenoyMonkeyData, ShenoyMonkeyDataSingleTrial, basisFxnNum, TBFResults and others; the paper
19	# says "Code-compatible data are available upon request"), and lacks kinFuncEval (the kinematic
20	# basis functions), the jPCA codepack, GPFA, and code for the location-from-kinematics regression
[... 755 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/sabatini-2024; date -u; timeout 600 ../../executed/sabatini-2024/.venv/bin/python -c "
import ldr, numpy as np
for m in ('J','N'):
    f,aid=ldr.open_nwb(m)
    u=f['units']
    print(m, list(u.keys()), dict(u.attrs).get('colnames'))
    for k in u.keys():
        if k in ('spike_times',): continue
        ds=u[k]
        try:
            v=ds[:]
            print('  ',k, ds.dtype, ds.shape, v[:5], dict(ds.attrs).get('description'))
        except Exception as e: print('  ',k,e)
    el=u['electrodes'][:]
    print('  electrodes unique', len(np.unique(el)), 'of', len(el))
    print('  electrodes table', list(f['general/extracellular_ephys/electrodes'].keys()))
    print('  description', f['general'].keys() if False else '', [ (k, f['general'][k][()] ) for k in f['general'].keys() if k in ('experiment_description','notes','data_collection')])
    print(f['units'].attrs.get('description'))
"
```

```
Fri Nov 20 14:33:01 UTC 2026
J ['electrode_group', 'electrodes', 'electrodes_index', 'id', 'obs_intervals', 'obs_intervals_index', 'spike_times', 'spike_times_index'] ['spike_times' 'obs_intervals' 'electrodes' 'electrode_group']
   electrode_group object (192,) [<HDF5 object reference> <HDF5 object reference> <HDF5 object reference>
 <HDF5 object reference> <HDF5 object reference>] the electrode group that each spike unit came from
   electrodes int64 (192,) [0 1 2 3 4] the electrodes that each spike unit came from
   electrodes_index uint8 (192,) [1 2 3 4 5] Index for VectorData 'electrodes'
   id int64 (192,) [0 1 2 3 4] None
   obs_intervals float64 (506112, 2) [[ 4.7072      8.56713333]
 [ 9.4072     12.11216667]
 [18.43723333 21.97226667]
 [22.77723333 26.00726667]
 [26.93726667 30.31726667]] the observation intervals for each unit
   obs_intervals_index uint32 (192,) [ 2636  5272  7908 10544 13180] Index for VectorData 'obs_intervals'
   spike_times_index uint32 (192,) [  61030  522584 1064240 1365853 1615759] Index for VectorData 'spike_times'
  electrodes unique 192 of 192
  electrodes table ['filtering', 'gain', 'group', 'group_name', 'id', 'imp', 'location', 'offset', 'x', 'y', 'z']
  description  [('experiment_description', b'')]
Autogenerated by NWBFile
N ['electrode_group', 'electrodes', 'electrodes_index', 'id', 'obs_intervals', 'obs_intervals_index', 'spike_times', 'spike_times_index'] ['spike_times' 'obs_intervals' 'electrodes' 'electrode_group']
   electrode_group object (192,) [<HDF5 object reference> <HDF5 object reference> <HDF5 object reference>
[... 15 more lines not kept]
```

**Agent calls Bash**

```bash
cd  ls paper/; grep -n -i -o ".\{200\}\(1469\|delay period\|successful\|400 ms\|trials were\).\{200\}" paper/*.txt | head -20
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  grep -n -i -o ".\{300\}Subjects, behavior.\{1500\}" paper/*.txt | head -5; grep -c "" paper/*.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  python -c "
import json,datetime
nb=json.load(open('executed/sabatini-2024/reproduce_sabatini_2024.ipynb'))
prev=None
for i,c in enumerate(nb['cells']):
    if c['cell_type']!='code': continue
    ex=c['metadata'].get('execution',{})
    a=ex.get('iopub.execute_input'); b=ex.get('shell.execute_reply')
    if a and b:
        f=lambda s: datetime.datetime.fromisoformat(s.replace('Z','+00:00'))
        print(i, round((f(b)-f(a)).total_seconds()), c.get('metadata',{}).get('tags'))
"
```

```
1 5 None
3 287 None
5 0 ['sanity']
7 0 None
9 4 None
11 192 None
13 0 ['claim:data-composition']
16 195 ['claim:fig2c-condition-lds-variance']
19 0 ['claim:fig3a-eigenvalue-clusters']
22 163 None
23 0 ['claim:fig3c-eigenvalue-distance-auc']
26 0 ['claim:fig3g-basis-frequencies']
29 0 ['claim:tbf-variance-explained']
32 3 None
33 0 ['claim:tbf-shuffle-control']
35 0 ['claim:fig3h-recoverability']
38 1 ['claim:fig3i-duration-warping']
41 0 ['claim:single-lds-variance']
44 63 None
46 0 ['claim:fig4b-plane-alignment']
[... 35 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n "claim:" tools/entry.py | head -30; grep -n "def check" tools/entry.py; ls tools; cat questions/*.yaml 2>/dev/null | head -40; ls questions | head
```

```
505:            if tag.startswith("claim:"):
179:def check(entry_dir: Path) -> Report:
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
[... 72 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 179,330p tools/entry.py; sed -n 480,560p tools/entry.py; cat questions/README.md | head -40; head -5 questions/asari-2009.yaml
```

```
def check(entry_dir: Path) -> Report:
    report = Report()
    rel = entry_dir.relative_to(ROOT)
    entry = validate(report, entry_dir / "entry.yaml", "entry")
    if entry is None:
        return report
    if entry.get("name") != entry_dir.name:
        report.error(rel / "entry.yaml", f"name {entry.get('name')!r} must match the directory name")

    listed = [n["path"] for n in entry.get("notebooks", [])]
    present = sorted(p.name for p in entry_dir.glob("*.ipynb"))
    for name in sorted(set(present) - set(listed)):
        report.error(rel / name, "notebook is not listed in entry.yaml")
    for name in sorted(set(listed) - set(present)):
        report.error(rel / "entry.yaml", f"listed notebook {name!r} does not exist")
    helpers = entry.get("helpers", [])
    for name in helpers:
        if not (entry_dir / name).is_file():
            report.error(rel / "entry.yaml", f"listed helper {name!r} does not exist")

[... 230 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/sabatini-2024; python -c "
import json
nb=json.load(open('reproduce_sabatini_2024.ipynb'))
for i,c in enumerate(nb['cells']):
    s=''.join(c['source'])
    if c['cell_type']=='markdown':
        print(f'=== cell {i}')
        print(s)
" > $TMPDIR/md.txt; wc -c $TMPDIR/md.txt
```

```
33082 /tmp/claude-1001/md.txt
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/md.txt"
}
```

```
1	=== cell 0
2	# Reproducing Sabatini & Kaufman (2024) on DANDI:000070
3	
4	**Paper.** Sabatini, D. A. & Kaufman, M. T. (2024). Reach-dependent reorientation of rotational dynamics
5	in motor cortex. *Nature Communications* 15, 7007. doi:10.1038/s41467-024-51308-7. The claims file
6	(`claims/sabatini-2024.yaml`) was written from the version of record (PMC11325044) with its Methods and
7	its supplement, and from the paper's code (github.com/kaufmanlab/LDR-public at commit b65f28d).
8	
9	**Dataset.** DANDI:000070 ("Neural population dynamics during reaching"), version **0.260528.0919**,
10	streamed. The paper cites the dandiset without a version. Of its three versions (0.251218.1714,
11	0.260528.0919 and the draft), the two published ones list the same ten assets with the same asset ids,
12	sizes and modification times, so they hold the same files; the most recent published one is pinned, as
13	the protocol asks when no version is cited. The two files the paper's Data availability statement
14	names are read: `sub-Jenkins_ses-20090918` (monkey J) and `sub-Nitschke_ses-20100923` (monkey N).
15	
16	**What is tested.** The four datasets of the paper (M1-J, PMd-J, M1-N, PMd-N) are rebuilt from the
17	units, trials and hand position in the two files. The dataset holds no EMG.
18	
19	| Claim | Tested here |
20	|---|---|
[... 388 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -o "Estimating the dimensionality of each rotation.\{2500\}" paper/*.txt; echo; grep -o "Subspace excursion angles [A-Z].\{2500\}" paper/*.txt | head -c 3000
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
mkdir -p $TMPDIR/ed; cat > $TMPDIR/ed/nbedit.py <<'EOF'
import json, sys
P = "entries/sabatini-2024/reproduce_sabatini_2024.ipynb"
def load():
    return json.load(open(P))
def save(nb):
    json.dump(nb, open(P, "w"), indent=1, ensure_ascii=False); open(P, "a").write("\n")
def src(nb, i):
    return "".join(nb["cells"][i]["source"])
def setsrc(nb, i, s):
    lines = s.split("\n")
    nb["cells"][i]["source"] = [l + "\n" for l in lines[:-1]] + [lines[-1]]
def rep(nb, i, old, new, count=1):
    s = src(nb, i)
    assert s.count(old) == count, (i, old[:60], s.count(old))
    setsrc(nb, i, s.replace(old, new))
def find(nb, sub):
    hits = [i for i, c in enumerate(nb["cells"]) if sub in "".join(c["source"])]
    assert len(hits) == 1, (sub, hits)
    return hits[0]
EOF
cd entries/sabatini-2024; head -c 600 reproduce_sabatini_2024.ipynb; python -c "import json;nb=json.load(open('reproduce_sabatini_2024.ipynb'));print(nb['cells'][1].keys(), nb['cells'][1]['metadata'])"
```

```
{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "e7adaf51",
   "metadata": {},
   "source": [
    "# Reproducing Sabatini & Kaufman (2024) on DANDI:000070\n",
    "\n",
    "**Paper.** Sabatini, D. A. & Kaufman, M. T. (2024). Reach-dependent reorientation of rotational dynamics\n",
    "in motor cortex. *Nature Communications* 15, 7007. doi:10.1038/s41467-024-51308-7. The claims file\n",
    "(`claims/sabatini-2024.yaml`) was written from the version of record (PMC11325044) with its Methods and\n",
    "its supplement, and from the paper's code (github.com/kaufmanlab/LDR-public at commidict_keys(['cell_type', 'execution_count', 'id', 'metadata', 'outputs', 'source']) {}
```

**Agent calls Bash**

```bash
cd entries/sabatini-2024; python - <<'EOF'
p='ldr.py'; s=open(p).read()
old='''    loc = f["general/extracellular_ephys/electrodes/location"][:]
    el = u["electrodes"][:]'''
new='''    loc = f["general/extracellular_ephys/electrodes/location"][:]
    el = u["electrodes"][:]
    unit_cols = sorted(u.keys())
    electrode_cols = sorted(f["general/extracellular_ephys/electrodes"].keys())'''
assert s.count(old)==1; s=s.replace(old,new)
old='''                spikes_per_unit=np.diff(np.r_[0, sidx]))'''
new='''                spikes_per_unit=np.diff(np.r_[0, sidx]), unit_columns=unit_cols,
                electrode_columns=electrode_cols, unit_electrode=el, n_electrodes=len(loc))'''
assert s.count(old)==1; s=s.replace(old,new)
old='''            # the trial's 1 ms bins permuted in time, the same permutation for every unit so that
            # spike correlations between units are kept (Methods, Control for data smoothing); over
            # the window read (assumption; claims, tbf-shuffle-control, code scrambleTrials.m)'''
new='''            # the trial's 1 ms bins permuted in time, the same permutation for every unit so that
            # spike correlations between units are kept (Methods, Control for data smoothing). The
            # span permuted is the 1.5 s window read, -500 to +1001 ms around movement onset
            # (assumption: neither the Methods nor the claims give the span; a longer span would
            # move more spikes into the analysis window from farther away and lower the shuffled
            # variance explained, a shorter one raise it)'''
assert s.count(old)==1; s=s.replace(old,new)
old='''    vectors over time; integrated over time to position basis functions. vel_list: arrays
    (conditions, time, 2)."""'''
new='''    vectors over time; integrated over time to position basis functions. vel_list: arrays
    (conditions, time, 2).

    Scale (assumption): the velocity vectors have unit norm and the position functions are their
    cumulative sums over 10 ms bins, with no factor for the bin width. The scale of the position
    functions sets the scale of the reach parameters, and with it what the OU length scale of 10^3
    (fig6e, fig7c, suppfig7a) means; the paper's kinFuncEval, which fixes it, is not published. The
    notebook shows those claims with length scales of 10^2 and 10^4 as well."""'''
assert s.count(old)==1; s=s.replace(old,new)
open(p,'w').write(s)
EOF
```

```
(Bash completed with no output)
```

**Agent calls Bash**

```bash
cd $TMPDIR/ed; python - <<'EOF'
from nbedit import *
nb=load()
rep(nb,1,'''T_START = time.time()''','''# Trial reading of the claims file's shared method that the analyses use: "a", all successful trials
# of the 72 conditions (adopted: the Methods describe the task with a 0-1000 ms delay and name no
# exclusion), or "b", successful trials with a delay above 400 ms. The companion notebook
# reproduce_sabatini_2024_trials_b.ipynb is this notebook with READING = "b" and FULL_SEEDS = False.
READING = "a"
# Run the four extra seeds of each claim (protocol); the companion notebook runs the claim's own seed only.
FULL_SEEDS = True
T_START = time.time()''')
rep(nb,1,'''def seeds5(claim):
    return [seed(claim) + i for i in (0, 1000, 2000, 3000, 4000)]''','''def seeds5(claim):
    return [seed(claim) + i for i in ((0, 1000, 2000, 3000, 4000) if FULL_SEEDS else (0,))]''')
rep(nb,1,'''print("dandiset", ldr.DANDISET, "version", ldr.VERSION)''','''print("dandiset", ldr.DANDISET, "version", ldr.VERSION, "| trial reading", READING, "| five seeds", FULL_SEEDS)''')
# cell 7 MASK
rep(nb,7,'''MASK = {m: ldr.select_trials(SESS[m]["trials"], "b") & np.isfinite(SESS[m]["hand"][:, 0, 0]) for m in ("J", "N")}
print({m: int(MASK[m].sum()) for m in MASK})''','''MASK = {m: ldr.select_trials(SESS[m]["trials"], READING) & np.isfinite(SESS[m]["hand"][:, 0, 0]) for m in ("J", "N")}
print(f"trials analysed (reading ({READING}), with hand position):", {m: int(MASK[m].sum()) for m in MASK})''')
# cell 5 sanity: units table
rep(nb,5,'''    print("  units", len(S["area"]), {a: int((S["area"] == a).sum()) for a in ("M1", "PMd")})''','''    print("  units", len(S["area"]), {a: int((S["area"] == a).sum()) for a in ("M1", "PMd")})
    print("  units table columns:", S["info"]["unit_columns"], "| electrodes table columns:", S["info"]["electrode_columns"])
    print("  electrodes in the file", S["info"]["n_electrodes"], "| units per electrode:",
          np.unique(np.bincount(S["info"]["unit_electrode"], minlength=S["info"]["n_electrodes"]), return_counts=True))''')
# cell 13 units-per-electrode fix
rep(nb,13,'''print("units per electrode (J):", np.unique(np.bincount(np.arange(192))))''','''for m in ("J", "N"):
    el = SESS[m]["info"]["unit_electrode"]
    print(f"monkey {m}: units per electrode (value: number of electrodes)",
          dict(zip(*[a.tolist() for a in np.unique(np.bincount(el, minlength=SESS[m]['info']['n_electrodes']), return_counts=True)])),
          "| units table columns", SESS[m]["info"]["unit_columns"])''')
save(nb)
EOF
```

```
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/ed; python - <<'EOF'
from nbedit import *
nb=load()
rep(nb,26,'''    ax.plot(ldr.GRID_MS[ldr.FIT0:], D[ds]["B"].T)''','''    # the same factorization fitted on other windows (to tell a shift of frequency due to the window
    # from one in the data; verifier's request): 0 to +850 ms and -350 to +850 ms, the dataset's k
    for lab, t0 in (("0..+850 ms", int(np.searchsorted(ldr.GRID_MS, 0))), ("-350..+850 ms", 0)):
        g2, fr2 = ldr.demix(*ldr.tbf(D[ds]["X"][..., t0:], D[ds]["k"]))[3:]
        print(f"   window {lab}: rotation frequencies {np.round([fr2[g2 == r][0] for r in range(g2.max() + 1)], 2)} Hz")
    ax.plot(ldr.GRID_MS[ldr.FIT0:], D[ds]["B"].T)''')
rep(nb,32,'''        SH[ds][sd] = dict(ve=ve, rec=recoverability(Ls, Bs, Xs))''','''        # chance recoverability with the shuffled basis de-mixed, as the real basis is (main), and with
        # the raw SVD basis (variant)
        Bsd, Lsd = ldr.demix(Bs, Ls)[:2]
        SH[ds][sd] = dict(ve=ve, rec=recoverability(Lsd, Bsd, Xs), rec_raw=recoverability(Ls, Bs, Xs))''')
rep(nb,35,'''    print("   chance mean under the five seeds:", [round(SH[ds][sd]["rec"].mean(), 4) for sd in seeds5("tbf-shuffle-control")])''','''    print("   chance mean under the five seeds:", [round(SH[ds][sd]["rec"].mean(), 4) for sd in seeds5("tbf-shuffle-control")],
          f"| variant, chance with the raw shuffled basis: mean {SH[ds][s0]['rec_raw'].mean():.3f}; real with the raw basis: mean "
          f"{recoverability(D[ds]['Lraw'], D[ds]['Braw'], D[ds]['Xw']).mean():.3f}")''')
rep(nb,35,'''chance (shuffled data) mean''','''chance (shuffled data, de-mixed basis) mean''')
save(nb)
EOF
```

```
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/ed; python - <<'EOF'
from nbedit import *
nb=load()
rep(nb,79,'''    ci = [int(np.where(mz == mz[i] + 1)[0][0]) for i in si]''','''    ci = [int(np.where(mz == mz[i] + 1)[0][0]) for i in si]
    tdist = np.hypot(CT[ds[0]]["tx"][si] - CT[ds[0]]["tx"][ci], CT[ds[0]]["ty"][si] - CT[ds[0]]["ty"][ci])
    print(f"   pairing check: {len(si)} straight conditions paired with maze + 1, of which {int((~CT[ds[0]]['straight'][ci]).sum())} "
          f"curved; target distance within pairs median {np.median(tdist):.1f}, max {tdist.max():.1f} (target radius median "
          f"{np.median(np.hypot(CT[ds[0]]['tx'], CT[ds[0]]['ty'])):.1f}, file units)")''')
save(nb)
EOF
```

```
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/ed; python - <<'EOF'
from nbedit import *
nb=load()
rep(nb,62,'''    return same, diff, stats.wilcoxon(same, diff).pvalue, stats.ranksums(same, diff).pvalue''','''    return same, diff, stats.wilcoxon(same, diff).pvalue, stats.ranksums(same, diff).pvalue


def paired_direction(x, y):
    """Median and Hodges-Lehmann estimate (median of Walsh averages) of the paired differences x - y,
    and the one-sided signed-rank p that x is larger."""
    d = np.asarray(x) - np.asarray(y)
    ds = np.random.default_rng(0).choice(d, min(len(d), 3000), replace=False) if len(d) > 3000 else d  # standard subsample for speed
    w = (ds[:, None] + ds[None, :])[np.triu_indices(len(ds))] / 2
    return np.median(d), np.median(w), stats.wilcoxon(x, y, alternative="greater").pvalue''')
rep(nb,63,'''            same, diff, pa, pb = seg_report(ds, n1, n2)
            print(f"{NAME[ds]} {n1} vs onto {n2}: same median {np.median(same):.3f}, different median {np.median(diff):.3f}; "
                  f"mean difference {np.mean(same - diff):+.3f}; same higher on {(same > diff).mean():.3f} of pairs; "
                  f"(a) p {pa:.1e}; (b) p {pb:.1e}")''','''            same, diff, pa, pb = seg_report(ds, n1, n2)
            md, hl, p1 = paired_direction(same, diff)
            print(f"{NAME[ds]} {n1} vs onto {n2}: same median {np.median(same):.3f}, different median {np.median(diff):.3f}; "
                  f"mean difference {np.mean(same - diff):+.3f}, median difference {md:+.3f}, Hodges-Lehmann {hl:+.3f}; same higher on "
                  f"{(same > diff).mean():.3f} of pairs; (a) p {pa:.1e} (one-sided, same higher, {p1:.1e}); (b) p {pb:.1e}")''')
rep(nb,65,'''        same, diff, pa, pb = seg_report(ds, "location", n2)
        print(f"{NAME[ds]} location vs onto {n2}: same median {np.median(same):.3f}, different median {np.median(diff):.3f}; "
              f"(a) p {pa:.1e}; (b) p {pb:.1e}")''','''        same, diff, pa, pb = seg_report(ds, "location", n2)
        md, hl, p1 = paired_direction(same, diff)
        print(f"{NAME[ds]} location vs onto {n2}: same median {np.median(same):.3f}, different median {np.median(diff):.3f}; "
              f"median difference {md:+.3f}; (a) p {pa:.1e} (one-sided {p1:.1e}); (b) p {pb:.1e}")''')
rep(nb,69,'''        print(f"{NAME[ds]} {a} -> {b}: mean {v.mean():.3f} s.d. {v.std():.3f}; null mean {nv.mean():.3f}; signed-rank p {p:.1e} "''','''        md, hl, p1 = paired_direction(v, nv)
        print(f"{NAME[ds]} {a} -> {b}: mean {v.mean():.3f} s.d. {v.std():.3f}; null mean {nv.mean():.3f}; median difference {md:+.3f}; "
              f"signed-rank p {p:.1e} (one-sided, real higher, {p1:.1e}) "''')
rep(nb,118,'''        p = stats.wilcoxon(ca, cb).pvalue
        print(f"reading ({r}) {NAME[ds]}: per-condition VE with potent dims {ca.mean():.3f}, without {cb.mean():.3f} "
              f"(mean drop {np.mean(ca - cb):.3f}); two-sided signed-rank p {p:.3f}")''','''        p = stats.wilcoxon(ca, cb).pvalue
        md, hl, p1 = paired_direction(ca, cb)
        print(f"reading ({r}) {NAME[ds]}: per-condition VE with potent dims {ca.mean():.3f}, without {cb.mean():.3f} "
              f"(mean drop {np.mean(ca - cb):.3f}, median drop {md:.3f}, lower without on {int((cb < ca).sum())}/72); two-sided "
              f"signed-rank p {p:.2e} (one-sided, lower without, {p1:.2e})")''')
save(nb)
EOF
```

```
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/ed; python - <<'EOF'
from nbedit import *
nb=load()
rep(nb,109,'''    for name in ("lin", "pos", "vel"):
        F = feats[name][:, tt - lag]  # (c, T, f)''','''    for name in ("lin", "pos", "vel", "pos_l0.1", "vel_l0.1"):
        fname, _, pen = name.partition("_l")
        F = feats[fname][:, tt - lag]  # (c, T, f)''')
rep(nb,109,'''                f = ldr.kernel_fit(Xtr, Ytr, "ou", 1e12 if name == "pos" else 1e11, 0.1)''','''                # penalty: none (floored at 1e-8, as the LDR encoder's kernel, whose penalty the claims give as
                # none, from the code); 0.1, the Methods' L2 for kernel decoders, is a variant
                f = ldr.kernel_fit(Xtr, Ytr, "ou", 1e12 if fname == "pos" else 1e11, float(pen) if pen else 0.0)''')
rep(nb,110,'''        for name, lab in (("lin", "linear multi-parameter"), ("pos", "kernel on position"), ("vel", "kernel on velocity")):''','''        for name, lab in (("lin", "linear multi-parameter"), ("pos", "kernel on position"), ("vel", "kernel on velocity")):''')
rep(nb,110,'''    print(f"reading ({r}): LDR higher with p < 0.001 in {nwin} of 24 comparisons")''','''        print(f"   variant, kernel penalty 0.1: position {STD[ds]['pos_l0.1'].mean():.3f}, velocity {STD[ds]['vel_l0.1'].mean():.3f}")
    print(f"reading ({r}): LDR higher with p < 0.001 in {nwin} of 24 comparisons")''')
save(nb)
EOF
```

```
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/ed; python - <<'EOF'
from nbedit import *
nb=load()
rep(nb,56,'''            V = np.linalg.svd(Z - Z.mean(0), full_matrices=False)[2]  # PCs of partition 1 (rows)''','''            # PCs of partition 1's loadings, not mean-centred: the bottleneck below is applied to the loadings as
            # they are, so the PCs must span them (Methods, "PCA on the dimensions occupied by these rotations")
            V = np.linalg.svd(Z, full_matrices=False)[2]''')
rep(nb,52,'''SEA_NOISE = {}''','''# Noise SEA (claims: "fraction of noise SEA above the data", code singleFrequencyOverlapControl.m; the
# procedure is not described further, so this is an assumption): SEA run on the 72 half-split estimates
# (36 repeats x 2 halves) of one condition's plane, which differ only by estimation noise, for every
# third condition (24 per rotation), with three seed planes per run (time). A data dimension is above
# chance when fewer than 5% of these noise curves reach its angle.
def sea_noise_job(args):
    ds, name, c = args
    idx = dict(comps(ds))[name]
    planes = [ldr.orth(H[c][:, idx]) for LA, LB in AL[ds]["halves"] for H in (LA, LB)]
    return ldr.sea(planes, 25, seeds=(0, 24, 48))


_nj = [(ds, name, c) for ds in DATASETS for name, _ in comps(ds)[:-1] for c in range(0, 72, 3)]
_nr = ldr.pmap(sea_noise_job, _nj)
SEA_NOISE_CURVES = {}
for (ds, name, c), a in zip(_nj, _nr):
    SEA_NOISE_CURVES.setdefault((ds, name), []).append(a)
SEA_NOISE = {}''')
rep(nb,53,'''        thr = np.percentile(SEA_NOISE[(ds, name)], 95)
        print(f"{NAME[ds]} {name}: angles >45 deg: {int((a > 45).sum())} (with the 2 seed dimensions {int((a > 45).sum()) + 2}); "
              f"above chance ({thr:.1f} deg): {int((a > thr).sum())} of 25; angles {np.round(a[:12], 1)} ...")''','''        thr = np.percentile(SEA_NOISE[(ds, name)], 95)
        nc = np.array(SEA_NOISE_CURVES[(ds, name)])  # (24, 25)
        frac = (nc >= a[None, :]).mean(0)
        n45 = int((a > 45).sum())
        print(f"{NAME[ds]} {name}: angles >45 deg: {n45} (with the 2 seed dimensions {n45 + 2}); above chance (noise SEA, fraction "
              f"< 0.05): {int((frac < 0.05).sum())} of 25, more than the count above 45: {int((frac < 0.05).sum()) > n45}; "
              f"variant, above the 95th percentile of half-split angles ({thr:.1f} deg): {int((a > thr).sum())}")
        print(f"   data angles {np.round(a[:12], 1)} ...; noise SEA median {np.round(np.median(nc, 0)[:12], 1)} ...")''')
save(nb)
EOF
```

```
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/ed; python - <<'EOF'
from nbedit import *
nb=load()
rep(nb,96,'''        elif model == "ou":
            f = ldr.kernel_fit(P[tr], Y[tr], "ou", 1e3, 0.0)''','''        elif model.startswith("ou"):  # "ou": length scale 1e3 (claims); "ou_1e2", "ou_1e4": variants (scale of Bp, assumption)
            f = ldr.kernel_fit(P[tr], Y[tr], "ou", float(model[3:]) if "_" in model else 1e3, 0.0)''')
rep(nb,96,'''        out[model] = (real, null)
    return out''','''        out[model] = (real, null)
    for model in ("ou_1e2", "ou_1e4"):
        out[model] = (cv_offset(P, Y, folds, model), None)
    return out''')
rep(nb,97,'''        print(f"{NAME[ds]} kinematic reading ({r}): " + " | ".join(txt))''','''        print(f"{NAME[ds]} kinematic reading ({r}): " + " | ".join(txt))
        print(f"   variant, OU length scale 1e2: {res['ou_1e2'][0]:.3f}; 1e4: {res['ou_1e4'][0]:.3f}")''')
rep(nb,103,'''        elif model == "ou":
            f = ldr.kernel_fit(Ptr, Y, "ou", 1e3, 0.0)''','''        elif model.startswith("ou"):  # "ou": length scale 1e3 (claims); "ou_1e2", "ou_1e4": variants
            f = ldr.kernel_fit(Ptr, Y, "ou", float(model[3:]) if "_" in model else 1e3, 0.0)''')
rep(nb,103,'''    out["sext_nn"] = encode(ds, P, sfolds, "nn")
    return out''','''    out["sext_nn"] = encode(ds, P, sfolds, "nn")
    if sd == seed("fig7c-ldr-encoding"):
        out.update({m: encode(ds, P, folds, m) for m in ("ou_1e2", "ou_1e4")})
        out.update({"sext_" + m: encode(ds, P, sfolds, m) for m in ("ou_1e2", "ou_1e4")})
    return out''')
rep(nb,104,'''              f"{stats.wilcoxon(e['ou'], e['ou_null']).pvalue:.1e}; other seeds {np.round(o['ou'], 3)})")''','''              f"{stats.wilcoxon(e['ou'], e['ou_null']).pvalue:.1e}; other seeds {np.round(o['ou'], 3)}) | variant, kernel length "
              f"scale 1e2 {e['ou_1e2'].mean():.3f}, 1e4 {e['ou_1e4'].mean():.3f}")''')
rep(nb,106,'''              f"{stats.wilcoxon(e['sext_ou'], e['sext_nn']).pvalue:.1e}")''','''              f"{stats.wilcoxon(e['sext_ou'], e['sext_nn']).pvalue:.1e} (one-sided, kernel higher, "
              f"{stats.wilcoxon(e['sext_ou'], e['sext_nn'], alternative='greater').pvalue:.1e}) | variant, length scale 1e2: mean "
              f"{e['sext_ou_1e2'].mean():.3f}, p {stats.wilcoxon(e['sext_ou_1e2'], e['sext_nn']).pvalue:.1e}; 1e4: mean "
              f"{e['sext_ou_1e4'].mean():.3f}, p {stats.wilcoxon(e['sext_ou_1e4'], e['sext_nn']).pvalue:.1e}")''')
save(nb)
EOF
```

```
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/ed; python - <<'EOF'
from nbedit import *
nb=load()
setsrc(nb,121,'''from scipy.ndimage import gaussian_filter1d


def inst_job(args):
    ds, r, sd = args
    m = ds[0]
    rng = np.random.default_rng(sd)
    folds = ldr.folds_of(72, 2, rng)  # the same draw as decode() under this seed
    rng2 = np.random.default_rng(seed("fig7f-decoder-beats-standard"))
    cond = D[ds]["cond"]
    u = D[ds]["u"]
    lag = 10
    tt = np.arange(lag, len(ldr.GRID_MS))
    feats = {"20 ms": SESS[m]["R"][:, u], "100 ms": gaussian_filter1d(SESS[m]["C10"][:, u], 10, axis=2, mode="reflect")}
    H = KIN[m]["H"]
    out, insample = {}, {}
    configs = [(s, d_, z, 3000) for s in feats for d_ in ("linear, single trials", "kernel, single trials", "kernel, trial averages")
               for z in (False, True)]
    configs.append(("100 ms", "kernel, single trials", False, 6000))  # variant: a larger training subset
    for sname, dname, zs, nsub in configs:
        F = feats[sname]
        ve = np.full(len(cond), np.nan)
        ins = []
        for te in folds:
            tr = np.setdiff1d(np.arange(72), te)
            itr = np.where(MASK[m] & np.isin(cond, tr))[0]
            ite = np.where(MASK[m] & np.isin(cond, te))[0]
            if dname == "kernel, trial averages":
                Fa = ldr.cond_average(F, cond, 72, MASK[m])[tr]
                Ha = KIN[m]["Hc"][tr]
                X = Fa[:, :, tt - lag].transpose(0, 2, 1).reshape(-1, F.shape[1])
                Y = Ha[:, tt].reshape(-1, 2)
            else:
                X = F[itr][:, :, tt - lag].transpose(0, 2, 1).reshape(-1, F.shape[1])
                Y = H[itr][:, tt].reshape(-1, 2)
            # main: rates in spikes/s as they are (the Methods do not standardise); variant: z-scored
            mu, sdv = (X.mean(0), X.std(0) + 1e-9) if zs else (np.zeros(X.shape[1]), np.ones(X.shape[1]))
            X = (X - mu) / sdv
            if dname.startswith("linear"):
                f = ldr.ridge_fit(X, Y, 1.0)
            else:
                if len(X) > nsub:
                    pick = rng2.choice(len(X), nsub, replace=False)
                    X, Y = X[pick], Y[pick]
                f = ldr.kernel_fit(X, Y, "ou", 1e2, 0.1)
            for i in ite:
                Z = (F[i][:, tt - lag].T - mu) / sdv
                ve[i] = ldr.kin_ve(H[i][tt], f(Z))
            # check of the decoder: single trials of the training conditions (the trials it was trained on,
            # except for the trial-average model), 100 per fold
            for i in itr[:: max(1, len(itr) // 100)]:
                Z = (F[i][:, tt - lag].T - mu) / sdv
                ins.append(ldr.kin_ve(H[i][tt], f(Z)))
        key = (sname, dname) if (not zs and nsub == 3000) else (sname, dname + (", z-scored" if zs else f", {nsub} points"))
        out[key] = ve
        insample[key] = float(np.mean(ins))
    return out, insample


_jobs = [(ds, "a", seed("fig7f-ldr-decoding")) for ds in DATASETS]
_r = ldr.pmap(inst_job, _jobs)
INST = {ds: r_[0] for ds, r_ in zip(DATASETS, _r)}
INST_TRAIN = {ds: r_[1] for ds, r_ in zip(DATASETS, _r)}''')
setsrc(nb,122,'''tt = np.arange(10, len(ldr.GRID_MS))  # -250 to +850 ms, the window the instantaneous decoders can score
for kr in KB:
    nwin, ntot, nmain = 0, 0, 0
    for ds in DATASETS:
        m = ds[0]
        ldr_full, dec = DEC[(ds, kr, seed("fig7f-ldr-decoding"), ())]
        ok0 = np.isfinite(dec[:, 0])
        pos = np.full(KIN[m]["H"][:, ::10].shape, np.nan)
        pos[ok0] = ldr.params_to_pos(dec[ok0], KB[kr])
        ldr_ve = np.array([ldr.kin_ve(KIN[m]["H"][i][tt], pos[i][tt]) if ok0[i] else np.nan for i in range(len(ok0))])
        if kr == "a":
            print(f"{NAME[ds]}: LDR decoder over -250..+850 ms mean {np.nanmean(ldr_ve):.3f} (over -350..+850 ms {np.nanmean(ldr_full):.3f})")
        for key, ve in INST[ds].items():
            ok = np.isfinite(ve) & np.isfinite(ldr_ve)
            p = stats.wilcoxon(ldr_ve[ok], ve[ok]).pvalue
            win = (np.mean(ldr_ve[ok] - ve[ok]) > 0) and p < 0.001
            main = not key[1].endswith(("z-scored", "points"))
            nwin += win * main
            nmain += main
            if kr == "a":
                print(f"   {key[1]}, {key[0]} smoothing: mean {np.mean(ve[ok]):.3f} against LDR {np.mean(ldr_ve[ok]):.3f} "
                      f"({int(ok.sum())} trials); two-sided signed-rank p {p:.1e}; median difference {np.median(ldr_ve[ok] - ve[ok]):+.3f}; "
                      f"check on training-condition trials {INST_TRAIN[ds][key]:.3f}")
            elif not win:
                print(f"   kinematic reading (b): {NAME[ds]} {key} not beaten (p {p:.1e})")
    print(f"kinematic reading ({kr}): LDR higher with p < 0.001 in {nwin} of {nmain} comparisons with the main decoders "
          f"(raw rates, 3000 points; GPFA decoders not run)")''')
save(nb)
EOF
```

```
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/ed; python - <<'EOF'
from nbedit import *
nb=load()
rep(nb,122,'''pos = np.full(KIN[m]["H"][:, ::10].shape, np.nan)''','''pos = np.full(KIN[m]["H"].shape, np.nan)''')
save(nb)
EOF
date -u
```

```
Fri Nov 20 14:37:01 UTC 2026
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd entries/sabatini-2024; ls ../../executed/sabatini-2024/.venv/bin | grep -i -E "jupyter|python$" ; date -u
```

```
ipython
jupyter
jupyter-dejavu
jupyter-execute
jupyter-kernel
jupyter-kernelspec
jupyter-migrate
jupyter-nbconvert
jupyter-run
jupyter-troubleshoot
jupyter-trust
python
Fri Nov 20 14:37:11 UTC 2026
```

**Agent calls Bash**

```bash
cd entries/sabatini-2024; time ../../executed/sabatini-2024/.venv/bin/jupyter nbconvert --to notebook --execute --allow-errors --ExecutePreprocessor.timeout=3000 --output-dir $TMPDIR/run1 reproduce_sabatini_2024.ipynb 2>&1 | tail -3; date -u
```

```
[NbConvertApp] Converting notebook reproduce_sabatini_2024.ipynb to notebook
[IPKernelApp] WARNING | Kernel is running over TCP without encryption. All communication (including code and outputs) is sent in plain text and is susceptible to eavesdropping. Use IPC transport or launch with kernel manager-provisioned CurveZMQ keys to enable transport encryption.
[NbConvertApp] Writing 614986 bytes to /tmp/claude-1001/run1/reproduce_sabatini_2024.ipynb

real	21m33.417s
user	58m37.794s
sys	3m2.151s
Fri Nov 20 14:58:47 UTC 2026
```

**Agent calls Bash**

```bash
cd $TMPDIR; cat > $TMPDIR/ed/show.py <<'EOF'
import json, sys
nb=json.load(open(sys.argv[1]))
for i,c in enumerate(nb['cells']):
    if c['cell_type']!='code': continue
    tags=c['metadata'].get('tags',[])
    outs=[]
    for o in c.get('outputs',[]):
        if o.get('output_type')=='error':
            outs.append('ERROR '+o['ename']+': '+o['evalue'])
        t=o.get('text') or (o.get('data') or {}).get('text/plain') or ''
        t=''.join(t) if isinstance(t,list) else t
        if 'image/png' in (o.get('data') or {}): continue
        outs.append(t)
    s=''.join(outs).strip()
    if s: print(f'=== cell {i} {tags}\n{s}')
EOF
python ed/show.py run1/reproduce_sabatini_2024.ipynb
```

```
<persisted-output>
Output too large (70.1KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/d5bdbe57-c9bd-4c75-b8dd-bc572c7bb334/tool-results/bqqlv7q33.txt

Preview (first 2KB):
=== cell 1 []
dandiset 000070 version 0.260528.0919 | trial reading a | five seeds True
=== cell 3 []
J loaded in 132 s; trials kept (successful, 72 conditions): 1595
N loaded in 184 s; trials kept (successful, 72 conditions): 2121
=== cell 5 ['sanity']
== monkey J (asset 033a04c0-9ce7-45c5-8012-c571a7b9bf12)
  trials in file 2636 | successful 2570 | maze_condition values 109 (min 0 max 108 )
  units 192 {'M1': 96, 'PMd': 96}
  units table columns: ['electrode_group', 'electrodes', 'electrodes_index', 'id', 'obs_intervals', 'obs_intervals_index', 'spike_times', 'spike_times_index'] | electrodes table columns: ['filtering', 'gain', 'group', 'group_name', 'id', 'imp', 'location', 'offset', 'x', 'y', 'z']
  electrodes in the file 192 | units per electrode: (array([1]), array([192]))
  spikes per unit: min 61030 median 317716 max 1720529
  recording segments (backward jumps of hand timestamps + 1): 1 | bounds (s): [(np.float64(4.7), np.float64(15668.0))]
  backward jumps in spike times per unit: [191   1]
  trials per segment: [2636]
  trial start times monotonic: True
[... 14 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR; python ed/show.py run1/reproduce_sabatini_2024.ipynb | sed -n '/=== cell 7 /,$p' | grep -v "^   variant, OU\|^$" | head -150
```

```
=== cell 7 []
J reading (a) conditions 72 | reading (b) 1-target conditions 73 | (b) minus maze 0: 72 | same set as (a): True
   maze 0 trials: 203 targets [1 3] barriers [2 7 9] novel_maze [0 1]
   conditions kept: 72 | straight (no barrier): 36 | curved: 36
   trial reading (a): 1595 trials; per condition 17 to 29
   trial reading (b): 1381 trials; per condition 16 to 23
   with correct_reach also required (not a reading): 1345
N reading (a) conditions 72 | reading (b) 1-target conditions 73 | (b) minus maze 0: 72 | same set as (a): True
   maze 0 trials: 419 targets [1 3] barriers [0 1 2 3 4 5 6 7 8 9] novel_maze [0 1]
   conditions kept: 72 | straight (no barrier): 36 | curved: 36
   trial reading (a): 2121 trials; per condition 23 to 42
   trial reading (b): 1884 trials; per condition 19 to 37
   with correct_reach also required (not a reading): 1867
trials analysed (reading (a), with hand position): {'J': 1595, 'N': 2120}
=== cell 9 []
J segment 0: 1595 trials, condition decoded 0.345 (labels of the previous trial 0.013; trained on the other segments nan; chance 0.014)
N segment 0: 533 trials, condition decoded 0.445 (labels of the previous trial 0.013; trained on the other segments 0.424; chance 0.014)
N segment 1: 510 trials, condition decoded 0.455 (labels of the previous trial 0.010; trained on the other segments 0.478; chance 0.014)
N segment 2: 521 trials, condition decoded 0.495 (labels of the previous trial 0.010; trained on the other segments 0.505; chance 0.014)
N segment 3: 532 trials, condition decoded 0.179 (labels of the previous trial 0.024; trained on the other segments 0.491; chance 0.014)
[... 131 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR; python ed/show.py run1/reproduce_sabatini_2024.ipynb | sed -n '/=== cell 49 /,$p' | head -150
```

```
=== cell 49 ['claim:suppfig6a-location-alignment']
M1-J location: AUC 0.901 (P(noise > observed) 0.901); observed median 0.966, noise median 0.992; (a) signed-rank p 1.66e-13 (obs lower on 72/72); (b) rank-sum p 0.00e+00; AUC under four other seeds [0.902 0.903 0.904 0.902]
PMd-J location: AUC 0.784 (P(noise > observed) 0.784); observed median 0.955, noise median 0.982; (a) signed-rank p 1.66e-13 (obs lower on 72/72); (b) rank-sum p 0.00e+00; AUC under four other seeds [0.77  0.769 0.774 0.771]
M1-N location: AUC 0.887 (P(noise > observed) 0.887); observed median 0.935, noise median 0.990; (a) signed-rank p 1.66e-13 (obs lower on 72/72); (b) rank-sum p 0.00e+00; AUC under four other seeds [0.889 0.888 0.885 0.886]
PMd-N location: AUC 0.952 (P(noise > observed) 0.952); observed median 0.969, noise median 0.992; (a) signed-rank p 1.66e-13 (obs lower on 72/72); (b) rank-sum p 0.00e+00; AUC under four other seeds [0.952 0.951 0.952 0.952]
=== cell 53 ['claim:fig4c-subspace-excursion-angles']
M1-J rot0 (0.71 Hz): angles >45 deg: 5 (with the 2 seed dimensions 7); above chance (noise SEA, fraction < 0.05): 25 of 25, more than the count above 45: True; variant, above the 95th percentile of half-split angles (46.4 deg): 4
   data angles [80.6 67.6 55.7 52.6 45.4 42.8 40.4 39.9 37.9 33.3 32.7 30.7] ...; noise SEA median [37.6 22.6 20.9 19.7 19.  18.  17.4 16.8 16.2 15.4 14.6 13.9] ...
M1-J rot1 (1.85 Hz): angles >45 deg: 12 (with the 2 seed dimensions 14); above chance (noise SEA, fraction < 0.05): 25 of 25, more than the count above 45: True; variant, above the 95th percentile of half-split angles (70.7 deg): 4
   data angles [90.  88.5 85.7 80.7 70.5 67.7 61.6 56.  54.6 48.5 46.3 45.3] ...; noise SEA median [53.3 36.5 31.6 29.4 27.1 26.1 24.4 23.7 23.5 22.6 21.8 21. ] ...
M1-J rot2 (3.13 Hz): angles >45 deg: 11 (with the 2 seed dimensions 13); above chance (noise SEA, fraction < 0.05): 25 of 25, more than the count above 45: True; variant, above the 95th percentile of half-
[... 140 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR; python ed/show.py run1/reproduce_sabatini_2024.ipynb | sed -n '/=== cell 91 /,$p' | head -150
```

```
=== cell 91 ['claim:fig4f-plane-alignment-explains-jpca']
M1-J jPCA plane 1: rho (alignment index vs variance in plane) 0.945 p 1.29e-35
M1-J jPCA plane 2: rho (alignment index vs variance in plane) 0.931 p 2.16e-32
PMd-J jPCA plane 1: rho (alignment index vs variance in plane) 0.796 p 6.02e-17
M1-N jPCA plane 1: rho (alignment index vs variance in plane) 0.668 p 1.50e-10
M1-N jPCA plane 2: rho (alignment index vs variance in plane) 0.819 p 1.49e-18
PMd-N jPCA plane 1: rho (alignment index vs variance in plane) 0.805 p 1.53e-17
=== cell 94 []
velocity singular values (top 5): [30440.2 17185.4  5659.4  3565.9  1998. ] share of the top two 0.958
skew-normal fit, correlation with the SVD velocity vectors: [0.998, 0.957]
monkey J, reading (a): reach parameters reproduce condition-mean hand position with VE 0.993
monkey J, reading (b): reach parameters reproduce condition-mean hand position with VE 0.981
monkey N, reading (a): reach parameters reproduce condition-mean hand position with VE 0.996
monkey N, reading (b): reach parameters reproduce condition-mean hand position with VE 0.987
=== cell 97 ['claim:fig6e-kinematics-predict-location']
M1-J kinematic reading (a): linear 0.555 (null max -0.000, p 0.0010; other seeds [0.557 0.547 0.554 0.55 ]) | kernel OU 0.730 (null max -0.186, p 0.0010; other seeds [0.738 0.718 0.723 0.721]) | kernel Gaussian 0.422 (null max 0.040, p 0.0010; other seeds [0.416 0.42  0.415 0.423])
   variant, OU length scale 1e2: 0.728; 1e4: 0.730
M1-J kinematic reading (b): linear 0.554 (null max 0.001, p 0.0010; other seeds [0.557 0.546 0.554 0.548]) | kernel OU 0.741 (null max -0.181, p 0.0010; other seeds [0.749 0.729 0.738 0.736]) | kernel Gaussian 0.435 (null max 0.039, p 0.0010; other seeds [0.432 0.434 0.43  0.437])
   variant, OU length scale 1e2: 0.740; 1e4: 0.741
PMd-J kinematic reading (a): linear 0.555 (null max 0.032, p 0.0010; other seeds [0.558 0.55  0.547 0.549]) | kernel OU 0.685 (null max -0.142, p 0.0010; other seeds [0.691 0.655
[... 131 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR; python ed/show.py run1/reproduce_sabatini_2024.ipynb | sed -n '/=== cell 122 /,$p' | grep -v "z-scored" | sed -n '28,80p'; python ed/show.py run1/reproduce_sabatini_2024.ipynb | grep -n ERROR
```

```
kernel, single trials, 20 ms smoothing: mean 0.070 against LDR 0.697 (2120 trials); two-sided signed-rank p 0.0e+00; median difference +0.712; check on training-condition trials 0.134
   kernel, trial averages, 20 ms smoothing: mean 0.000 against LDR 0.697 (2120 trials); two-sided signed-rank p 0.0e+00; median difference +0.796; check on training-condition trials 0.000
   linear, single trials, 100 ms smoothing: mean 0.159 against LDR 0.697 (2120 trials); two-sided signed-rank p 0.0e+00; median difference +0.597; check on training-condition trials 0.214
   kernel, single trials, 100 ms smoothing: mean 0.455 against LDR 0.697 (2120 trials); two-sided signed-rank p 1.1e-183; median difference +0.243; check on training-condition trials 0.693
   kernel, trial averages, 100 ms smoothing: mean 0.038 against LDR 0.697 (2120 trials); two-sided signed-rank p 0.0e+00; median difference +0.750; check on training-condition trials 0.067
   kernel, single trials, 6000 points, 100 ms smoothing: mean 0.506 against LDR 0.697 (2120 trials); two-sided signed-rank p 2.5e-144; median difference +0.184; check on training-condition trials 0.802
kinematic reading (a): LDR higher with p < 0.001 in 24 of 24 comparisons with the main decoders (raw rates, 3000 points; GPFA decoders not run)
kinematic reading (b): LDR higher with p < 0.001 in 24 of 24 comparisons with the main decoders (raw rates, 3000 points; GPFA decoders not run)
```

**Agent calls Bash**

```bash
cd $TMPDIR/ed; python - <<'EOF'
from nbedit import *
nb=load()
for i in (100,104,106,110,114,116,118):
    s=src(nb,i)
    n=s.count('f"reading ({r})')
    s=s.replace('f"reading ({r})','f"kinematic reading ({r})').replace('f"reading ({r}):','f"kinematic reading ({r}):')
    setsrc(nb,i,s); print(i,n)
s=src(nb,97); print('97 has', s.count('kinematic reading'))
save(nb)
EOF
```

```
100 2
104 1
106 1
110 2
114 1
116 1
118 1
97 has 1
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/ed; python - <<'EOF'
from nbedit import *
nb=load()
setsrc(nb,6,'''### Conditions and trial readings

The claims file gives two readings for the 72 conditions (drop maze conditions that are a multiple of 3;
drop the 3-target versions, whose distractors repeat a curved maze) and two for trials: (a) all
successful trials, (b) successful trials with a delay above 400 ms. Both trial counts are within 10% of
the paper's (1469 and 2014), (a) above them and (b) below. The analyses use the reading set in
`READING` above. This notebook adopts reading (a): the Methods describe the task with "a brief delay
(0–1000 ms)" and name no exclusion of short delays (Methods, Subjects, behavior and data
pre-processing), and the analyses are of peri-movement activity aligned to movement onset. This is an
assumption, recorded. The companion notebook `reproduce_sabatini_2024_trials_b.ipynb` runs every
analysis under reading (b).''')
rep(nb,10,'''condition-averaged rates are formed from trial reading (b)''','''condition-averaged rates are formed from the trials of the reading in `READING`''')
save(nb)
EOF
```

```
Shell cwd was reset to
```

**Agent**

Now the companion-notebook generator, then a dev run of the reading (b) notebook.

**Agent calls Bash**

```bash
cat > $TMPDIR/ed/mkcompanion.py <<'EOF'
import json, copy
from nbedit import P, load, src, setsrc
nb = load()
out = copy.deepcopy(nb)
cells = []
for i, c in enumerate(out["cells"]):
    s = "".join(c["source"])
    if c["cell_type"] == "markdown" and s.startswith("**Result"):
        continue
    if i == 0:
        s = ("# Sabatini & Kaufman (2024) on DANDI:000070: trial reading (b)\n\n"
             "This notebook is `reproduce_sabatini_2024.ipynb` with two parameters changed in its first code cell: "
             "`READING = \"b\"` (successful trials with a delay above 400 ms, reading (b) of the claims file's shared "
             "method) and `FULL_SEEDS = False` (each claim's own seed only). Every analysis and every claim cell is the "
             "same. It shows the results under the trial reading the main notebook does not adopt; the conclusions, "
             "and the outcomes, are in the main notebook, which cites these numbers where the two readings differ.\n\n"
             "Dataset: DANDI:000070, version 0.260528.0919, streamed. Paper: doi:10.1038/s41467-024-51308-7.")
        lines = s.split("\n"); c["source"] = [l + "\n" for l in lines[:-1]] + [lines[-1]]
    if c["cell_type"] == "markdown" and s.startswith("## Summary"):
        s = ("## Summary\n\nThe outcomes are given in the main notebook, `reproduce_sabatini_2024.ipynb`, which adopts "
             "trial reading (a). A failure to reproduce here may be a failure of this attempt, not of the paper: see the "
             "reasoning and the differences from the paper's method.")
        lines = s.split("\n"); c["source"] = [l + "\n" for l in lines[:-1]] + [lines[-1]]
    if c["cell_type"] == "code" and 'READING = "a"' in s:
        assert 'FULL_SEEDS = True' in s
        s = s.replace('READING = "a"', 'READING = "b"').replace("FULL_SEEDS = True", "FULL_SEEDS = False")
        lines = s.split("\n"); c["source"] = [l + "\n" for l in lines[:-1]] + [lines[-1]]
    c["id"] = c["id"][:-1] + "b" if c.get("id") else c.get("id")
    cells.append(c)
out["cells"] = cells
Q = P.replace(".ipynb", "_trials_b.ipynb")
json.dump(out, open(Q, "w"), indent=1, ensure_ascii=False); open(Q, "a").write("\n")
print("wrote", Q, len(cells), "cells")
EOF
cd $TMPDIR/ed && python mkcompanion.py && cd entries/sabatini-2024 && python -c "
import json; [print(c['id']) for c in json.load(open('reproduce_sabatini_2024_trials_b.ipynb'))['cells'][:3]]"; date -u
```

```
wrote entries/sabatini-2024/reproduce_sabatini_2024_trials_b.ipynb 91 cells
e7adaf5b
e27c31bb
a172544b
Fri Nov 20 14:59:55 UTC 2026
```

**Agent calls Bash**

```bash
cd $TMPDIR/ed && sed -i 's/c\["id"\] = c\["id"\]\[:-1\] + "b" if c.get("id") else c.get("id")/c["id"] = c["id"] + "-b"/' mkcompanion.py && python mkcompanion.py && cd entries/sabatini-2024 && python -c "
import json; ids=[c['id'] for c in json.load(open('reproduce_sabatini_2024_trials_b.ipynb'))['cells']]; print(len(ids), len(set(ids)), ids[:2])" && time ../../executed/sabatini-2024/.venv/bin/jupyter nbconvert --to notebook --execute --allow-errors --ExecutePreprocessor.timeout=3000 --output-dir $TMPDIR/run1 reproduce_sabatini_2024_trials_b.ipynb 2>&1 | tail -1; date -u
```

```
wrote entries/sabatini-2024/reproduce_sabatini_2024_trials_b.ipynb 91 cells
91 91 ['e7adaf51-b', 'e27c31b5-b']
[NbConvertApp] Writing 593602 bytes to /tmp/claude-1001/run1/reproduce_sabatini_2024_trials_b.ipynb

real	12m12.969s
user	36m27.944s
sys	1m11.310s
Fri Nov 20 15:12:14 UTC 2026
```

**Agent calls Bash**

```bash
cd $TMPDIR; python ed/show.py run1/reproduce_sabatini_2024_trials_b.ipynb | grep -v "z-scored\|^   variant, OU\|seeds\|pairing check\|data angles\|^M1-J held\|^PMd-J held\|^M1-N held\|^PMd-N held" | sed -n '/=== cell 9 /,$p' | grep -v "kinematic reading (b)" | cut -c1-260 | head -170
```

```
=== cell 9 []
J segment 0: 1381 trials, condition decoded 0.325 (labels of the previous trial 0.013; trained on the other segments nan; chance 0.014)
N segment 0: 467 trials, condition decoded 0.411 (labels of the previous trial 0.006; trained on the other segments 0.437; chance 0.014)
N segment 1: 449 trials, condition decoded 0.416 (labels of the previous trial 0.016; trained on the other segments 0.488; chance 0.014)
N segment 2: 468 trials, condition decoded 0.459 (labels of the previous trial 0.017; trained on the other segments 0.511; chance 0.014)
N segment 3: 477 trials, condition decoded 0.161 (labels of the previous trial 0.027; trained on the other segments 0.478; chance 0.014)
N segment 4: 22 trials, condition decoded 0.000 (labels of the previous trial 0.000; trained on the other segments 0.545; chance 0.014)
=== cell 11 []
=== cell 13 ['claim:data-composition']
monkey J, trial reading (a): 1595 trials (paper 1469, tolerance 146.9; within: True; difference +126)
monkey J, trial reading (b): 1381 trials (paper 1469, tolerance 146.9; within: True; difference -88)
monkey J: conditions 72, straight 36, curved 36
   M1: 96 units; units table columns hold no single/multi-unit label
   PMd: 96 units; units table columns hold no single/multi-unit label
monkey N, trial reading (a): 2121 trials (paper 2014, tolerance 201.4; within: True; difference +107)
monkey N, trial reading (b): 1884 trials (paper 2014, tolerance 201.4; within: True; difference -130)
monkey N: conditions 72, straight 36, curved 36
   M1: 96 units; units table columns hold no single/multi-unit label
   PMd: 96 units; units table columns hold no single/multi-unit label
monkey J: units per electrode (value: number of electrodes) {1: 192} | units table columns ['electrode_group', 'electrodes', 'electrodes_index', 'id', 'obs_intervals', 'obs_intervals_index', 'spike_times', 'spike_times_index']
[... 151 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR; python ed/show.py run1/reproduce_sabatini_2024_trials_b.ipynb | sed -n '/=== cell 34 /,/=== cell 48 /p' | cut -c1-200 | grep -v "data angles\|angles >45"; python ed/show.py run1/reproduce_sabatini_2024_trials_b.ipynb | sed -n '/=== cell 63 /,$p' | grep -v "z-scored\|variant, OU" | grep -v "^   [a-z]" | cut -c1-330
```

```
=== cell 63 ['claim:suppfig3-model-comparison']
M1-J: jPCA 0.089 | single-condition LDS 0.844 | TBF cross-validated (held-out VE at k=7) 0.711 | TBF in sample 0.935; TBF highest (cross-validated): False; (in sample): True
PMd-J: jPCA 0.116 | single-condition LDS 0.902 | TBF cross-validated (held-out VE at k=5) 0.790 | TBF in sample 0.936; TBF highest (cross-validated): False; (in sample): True
M1-N: jPCA 0.117 | single-condition LDS 0.942 | TBF cross-validated (held-out VE at k=7) 0.866 | TBF in sample 0.966; TBF highest (cross-validated): False; (in sample): True
PMd-N: jPCA 0.051 | single-condition LDS 0.906 | TBF cross-validated (held-out VE at k=7) 0.791 | TBF in sample 0.953; TBF highest (cross-validated): False; (in sample): True
=== cell 66 ['claim:fig4d-jpca-variance-correlation']
M1-J jPCA plane 1: rho -0.061 p 6.13e-01 (rotation pairs in the normalised TBF 3)
M1-J jPCA plane 2: rho 0.711 p 2.52e-12 (rotation pairs in the normalised TBF 3)
   M1-J mean rho over retained planes 0.325
PMd-J jPCA plane 1: rho 0.930 p 3.62e-32 (rotation pairs in the normalised TBF 2)
   PMd-J mean rho over retained planes 0.930
M1-N jPCA plane 1: rho 0.663 p 2.23e-10 (rotation pairs in the normalised TBF 3)
M1-N jPCA plane 2: rho 0.627 p 3.71e-09 (rotation pairs in the normalised TBF 3)
   M1-N mean rho over retained planes 0.645
PMd-N jPCA plane 1: rho 0.682 p 4.33e-11 (rotation pairs in the normalised TBF 3)
   PMd-N mean rho over retained planes 0.682
planes with p < 0.05: 5 of 6 (83%)
=== cell 67 ['claim:fig4f-plane-alignment-explains-jpca']
M1-J jPCA plane 1: rho (alignment index vs variance in plane) 0.941 p 1.28e-34
M1-J jPCA plane 2: rho (alignment index vs variance in plane) 0.926 p 2.10e-31
[... 111 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR; python ed/show.py run1/reproduce_sabatini_2024_trials_b.ipynb | sed -n "/claim:fig4b/,/claim:fig4c/p;/claim:rotation-orient/,/claim:fig5a/p;/claim:fig5c/,/claim:fig6c/p" | grep -v "^===" | cut -c1-120
```

```
M1-J rot0 (0.70 Hz): AUC 0.912 (P(noise > observed) 0.912); observed median 0.752, noise median 0.901; (a) signed-rank o
M1-J rot1 (1.82 Hz): AUC 0.886 (P(noise > observed) 0.886); observed median 0.245, noise median 0.572; (a) signed-rank o
M1-J rot2 (3.08 Hz): AUC 0.861 (P(noise > observed) 0.861); observed median 0.243, noise median 0.576; (a) signed-rank o
PMd-J rot0 (0.64 Hz): AUC 0.945 (P(noise > observed) 0.945); observed median 0.720, noise median 0.930; (a) signed-rank 
PMd-J rot1 (1.54 Hz): AUC 0.933 (P(noise > observed) 0.933); observed median 0.212, noise median 0.590; (a) signed-rank 
M1-N rot0 (0.69 Hz): AUC 0.949 (P(noise > observed) 0.949); observed median 0.641, noise median 0.928; (a) signed-rank o
M1-N rot1 (1.79 Hz): AUC 0.952 (P(noise > observed) 0.952); observed median 0.295, noise median 0.814; (a) signed-rank o
M1-N rot2 (3.23 Hz): AUC 0.933 (P(noise > observed) 0.933); observed median 0.176, noise median 0.661; (a) signed-rank o
PMd-N rot0 (0.74 Hz): AUC 0.958 (P(noise > observed) 0.958); observed median 0.367, noise median 0.777; (a) signed-rank 
PMd-N rot1 (1.55 Hz): AUC 0.949 (P(noise > observed) 0.949); observed median 0.135, noise median 0.527; (a) signed-rank 
PMd-N rot2 (2.71 Hz): AUC 0.940 (P(noise > observed) 0.940); observed median 0.053, noise median 0.336; (a) signed-rank 
M1-J location: AUC 0.883 (P(noise > observed) 0.883); observed median 0.965, noise median 0.990; (a) signed-rank p 1.66e
PMd-J location: AUC 0.748 (P(noise > observed) 0.748); observed median 0.955, noise median 0.980; (a) signed-rank p 2.05
M1-N location: AUC 0.870 (P(noise > observed) 0.870); observed median 0.935, noise median 0.989; (a) signed-rank p 1.66e
PMd-N location: AUC 0.945 (P(noise > observed) 0.945); observed median 0.969, noise median 0.991; (a) signed-rank p 1.66
M1-J rot0 (0.70 Hz): (a) PCs to 80% 2, PR 1.8 | (b) PCs 2, PR 1.7 | SNR>1 dims 16 (four other seeds: [])
M1-J rot1 (1.82 Hz): (a) PCs to 80% 8, PR 5.6 | (b) PCs 7, PR 4.4 | SNR>1 dims 8
[... 42 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR; python ed/show.py run1/reproduce_sabatini_2024.ipynb | sed -n '/=== cell 122 /,$p' | grep -v "z-scored" | grep -A7 "^M1-N\|^PMd-N" | cut -c1-250
```

```
M1-N: LDR decoder over -250..+850 ms mean 0.847 (over -350..+850 ms 0.866)
   linear, single trials, 20 ms smoothing: mean 0.144 against LDR 0.847 (2120 trials); two-sided signed-rank p 0.0e+00; median difference +0.740; check on training-condition trials 0.176
   kernel, single trials, 20 ms smoothing: mean 0.290 against LDR 0.847 (2120 trials); two-sided signed-rank p 0.0e+00; median difference +0.570; check on training-condition trials 0.382
   kernel, trial averages, 20 ms smoothing: mean 0.000 against LDR 0.847 (2120 trials); two-sided signed-rank p 0.0e+00; median difference +0.904; check on training-condition trials 0.000
   linear, single trials, 100 ms smoothing: mean 0.543 against LDR 0.847 (2120 trials); two-sided signed-rank p 4.1e-293; median difference +0.293; check on training-condition trials 0.597
   kernel, single trials, 100 ms smoothing: mean 0.747 against LDR 0.847 (2120 trials); two-sided signed-rank p 2.7e-127; median difference +0.082; check on training-condition trials 0.869
   kernel, trial averages, 100 ms smoothing: mean 0.137 against LDR 0.847 (2120 trials); two-sided signed-rank p 0.0e+00; median difference +0.747; check on training-condition trials 0.186
   kernel, single trials, 6000 points, 100 ms smoothing: mean 0.780 against LDR 0.847 (2120 trials); two-sided signed-rank p 4.0e-75; median difference +0.059; check on training-condition trials 0.920
PMd-N: LDR decoder over -250..+850 ms mean 0.697 (over -350..+850 ms 0.730)
   linear, single trials, 20 ms smoothing: mean 0.013 against LDR 0.697 (2120 trials); two-sided signed-rank p 0.0e+00; median difference +0.782; check on training-condition trials 0.021
   kernel, single trials, 20 ms smoothing: mean 0.070 against LDR 0.697 (2120 trials); two-sided signed-rank p 0.0e+00; median difference +0.712; check on training-condition trials 0.134
   kernel, trial averages, 20 ms smoothing: mean 0.000 against LDR 0.697 (2120 trials); two-sided signed-rank p 0.0e+00; median difference +0.796
[... 5 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/ed; python - <<'EOF'
from nbedit import *
nb=load()
R={}
R["data-composition"]='''**Result: reproduced.** Both monkeys have the 72 conditions (36 straight, 36 curved), and the trial counts are within 10% of the paper's under both readings (J 1595 or 1381 against 1469; N 2121 or 1884 against 2014). Each array holds 96 units, inside 71 to 130; the units table has no single-unit, multi-unit or quality column, so all its units are counted. Every one of the 192 electrodes in each file carries exactly one unit, so these are per-electrode units, not shown to be the paper's 79 to 118 sorted single and multi-units (a finding about the dataset).'''
R["fig2c-condition-lds-variance"]='''**Result: reproduced.** The cross-validated dimensionality is 5, 5, 7 and 5 (M1-J, PMd-J, M1-N, PMd-N), the same under all five seeds, and the single-condition LDSs explain on average 85.3, 91.1, 94.6 and 91.2% of the population variance (s.d. 3.4 to 4.8%), all within 63.9 to 100%. The values are at or above the top of the paper's 71 to 93%. The code's 3/4 split chooses 7, 5, 7 and 7.'''
R["fig3a-eigenvalue-clusters"]='''**Result: not reproduced.** Every condition's LDS has the same number of complex pairs (2; 3 in M1-N, where one condition has 2 pairs and 3 real eigenvalues) and at least one real eigenvalue on all 72 conditions, so the eigenvalues form clusters with an offset. The median pair frequencies are 0.86 and 2.38 Hz (M1-J), 0.56 and 1.55 Hz (PMd-J), 0.68, 1.76 and 3.20 Hz (M1-N) and 0.73 and 1.68 Hz (PMd-N); only PMd-J 1.55 Hz is within 10% of its target, and no dataset has all its pairs within 10%. Under trial reading (b) PMd-J has 0.54 and 1.53 Hz, both within 10%, and the other three datasets still miss.'''
R["fig3c-eigenvalue-distance-auc"]='''**Result: not reproduced.** The AUC between distances across conditions and the noise distribution is 0.81, 0.71, 0.64 and 0.70 under the Poisson null (a) and 0.72, 0.67, 0.69 and 0.70 under the half-split null (b), against 0.459 to 0.638; only M1-N under (a) (0.636) is in range. Eigenvalues differ between conditions more than the paper reports, though the distances are small (median 0.011 to 0.016 in the complex plane). The four other seeds give AUCs within 0.02 of these under null (b). Under trial reading (b) the AUCs are 0.63 to 0.81, with the same single dataset in range.'''
R["fig3g-basis-frequencies"]='''**Result: not reproduced.** The cross-validated factorization has 3 rotation pairs and one offset in M1-J, M1-N and PMd-N, and 2 pairs in PMd-J, where the criterion asks for 3 or 4 in every dataset. The rotation frequencies are 0.71, 1.85, 3.13 (M1-J), 0.64, 1.54 (PMd-J), 0.69, 1.81, 3.24 (M1-N) and 0.74, 1.56, 2.71 Hz (PMd-N); 3 of the 11 are within 10% of 0.5, 1.5, 2.5 or 4 Hz, and no dataset has a rotation near 0.5 Hz or 4 Hz. The frequencies depend on the window fitted: over -350 to +850 ms they are 0.55 to 0.71, 1.37 to 1.70 and 2.52 to 2.96 Hz, closer to the paper's, and over 0 to +850 ms 0.61 to 0.67, 1.56 to 1.91 and 2.76 to 3.16 Hz.'''
R["tbf-variance-explained"]='''**Result: reproduced.** The factorization explains on average 94.1, 94.3, 96.9 and 95.8% of the population variance (s.d. 0.7 to 1.4% across conditions) over -150 to +850 ms, and 92.8 to 96.3% over the whole window with the raw basis, all within 81 to 100%.'''
R["tbf-shuffle-control"]='''**Result: partially reproduced.** Shuffling time bins lowers the variance explained to 42.2, 28.7, 41.9 and 42.1%, below the real data on all 72 conditions of every dataset (rank-sum p = 3.9e-25). Three of four lie in 31.5 to 50.6%; PMd-J (28.7%) is below, and stays below under the five seeds (28.7 to 29.1%) and under trial reading (b) (28.7%).'''
R["fig3h-recoverability"]='''**Result: partially reproduced.** Recoverability is 97.4, 98.0, 98.6 and 98.7%, within 81.9 to 100%, and above the shuffled data on every condition (rank-sum p = 3.9e-25). The chance level, now with the shuffled basis de-mixed as the real one is, is 89.5, 86.5, 89.1 and 89.6%, the same to three decimals as with the raw shuffled basis; only PMd-J lies in 56.7 to 88%. The five seeds move chance by less than 0.01.'''
R["fig3i-duration-warping"]='''**Result: not reproduced.** Before warping, M1-N has rho = +0.204 (p = 0.086), opposite in sign to the paper's -0.26; of the other three, PMd-J (0.072) and PMd-N (0.133) lie in -0.198 to 0.231 and M1-J (-0.203) just outside. Warping to 600 ms induces a negative correlation only in M1-J (rho = -0.550, p = 6e-07); PMd-J, M1-N and PMd-N give -0.106, -0.040 and -0.226 (p > 0.05). The 250 ms post-reach variant gives -0.40, -0.23, -0.12 and -0.36. Trial reading (b) gives the same pattern (M1-N unwarped +0.235; warped, only M1-J in range).'''
R["single-lds-variance"]='''**Result: not reproduced.** One LDS fitted to all conditions explains on average 78.1, 82.0, 82.9 and 78.6% of the population variance over -150 to +850 ms (80.6 to 87.2% over the whole window), above the range 41.4 to 72.6% in every dataset; under trial reading (b), 76.6 to 82.1%.'''
R["fig4b-plane-alignment"]='''**Result: reproduced.** For every rotation in every dataset, same-frequency planes on pairs of conditions are less aligned than half-split estimates of the same condition: AUC 0.876 to 0.961, observed alignment lower on 72 of 72 conditions, signed-rank p = 1.7e-13 (reading a) and rank-sum p printed as 0 (reading b). The four other seeds change the AUCs by at most 0.002; trial reading (b) gives 0.861 to 0.958.'''
R["suppfig6a-location-alignment"]='''**Result: partially reproduced.** The state space location is less aligned across conditions than expected from noise in every dataset (signed-rank p = 1.7e-13, observed lower on 72 of 72 conditions), with AUC 0.901, 0.784, 0.887 and 0.952; PMd-J (0.784; 0.769 to 0.774 under the other seeds, 0.748 under trial reading b) is below 0.792.'''
R["fig4c-subspace-excursion-angles"]='''**Result: partially reproduced.** The number of excursion angles above 45 degrees is 5, 12, 11 (M1-J), 7, 11 (PMd-J), 3, 9, 10 (M1-N) and 8, 17, 25 (PMd-N); 8 of 11 lie in 5.4 to 22 (M1-J 0.71 Hz, M1-N 0.69 Hz and PMd-N 2.71 Hz do not). Against the noise SEA (SEA of the half-split estimates of single conditions), all 25 dimensions are above chance for every rotation, more than the count above 45 degrees for 10 of 11 rotations; for PMd-N 2.71 Hz both counts reach the 25 computed. The noise SEA is an assumption about the code's control; the earlier percentile threshold, now a variant, gives 4 to 10 dimensions above chance. Trial reading (b) gives counts of 3 to 25, again 8 of 11 in range.'''
R["rotation-orientation-dimensionality"]='''**Result: not reproduced.** Rotation orientations need 2 to 21 PCs to reach 80% of their variance (reading a; 2 to 20 under b) and have participation ratios of 1.7 to 17.5, against 20.7 to 44 and 15.03 to 40.48; only PMd-N 2.71 Hz is inside either range. With the PCA of the SNR procedure fixed (not mean-centred, so that the bottleneck spans the loadings), the SNR dimensionality is 9 to 21 for all 11 rotations, inside 6.3 to 36.3, and stable across the five seeds. Two of the three measures fail.'''
R["suppfig6b-location-dimensionality"]='''**Result: not reproduced.** SEA finds 1 location dimension with an angle above 15 degrees in each dataset (2 with the seed), the locations need 2 to 5 PCs for 80% of their variance, and their participation ratios are 2.3 to 4.0 (reading a), all far below the stated ranges. The SNR dimensionality, with the procedure fixed, is 7, 2, 3 and 8; two of four lie in 4.5 to 13.2.'''
R["fig5a-frequencies-segregated"]='''**Result: reproduced.** Under reading (a), same-frequency alignment is higher than different-frequency alignment for all 20 rotation comparisons: the one-sided signed-rank test gives p at most 1.4e-12 and the Hodges-Lehmann estimate of the paired difference is positive in every comparison (+0.011 to +0.558). For M1-N 3.24 Hz onto the other two rotations the effect is small: the medians of the two distributions are 0.183 against 0.197 and 0.198, the median paired difference is +0.002 and -0.004, the Hodges-Lehmann estimates +0.025 and +0.024, and same-frequency is higher on 50% and 49% of condition pairs; there the rank-sum test of reading (b) gives p = 0.31 and 0.29. In PMd-J 1.54 Hz onto 0.64 Hz and PMd-N 2.71 Hz onto the others the medians differ by 0.001 to 0.009 and the Hodges-Lehmann estimates are +0.011 to +0.026.'''
R["suppfig6c-location-distinct-from-rotations"]='''**Result: reproduced.** In every dataset, the location on one condition is more aligned with the location on another (median 0.935 to 0.969) than with any rotation plane (median 0.085 to 0.664), with p printed as 0 under both readings and the median paired difference +0.28 to +0.88.'''
R["fig5c-rotations-predict-rotations"]='''**Result: reproduced.** Each rotation predicts on average 44.7 to 95.0% of the variance of another rotation, above the shuffled null (2.9 to 75.2%) for every pair (signed-rank p at most 7.6e-13, median paired difference positive). All 20 pair means lie in 38.7 to 100%, and the four other seeds move them by at most 0.04; trial reading (b) gives 41.4 to 94.6%.'''
R["fig6b-location-predicts-rotations"]='''**Result: reproduced.** The state space location predicts on average 73.3, 74.4, 81.6 and 74.1% of the population variance (6 folds, lambda 0.1), within 60.3 to 88%, against a null of 14.7 to 23.1% (signed-rank p at most 2.4e-13). The four other seeds give 72.0 to 82.9% and the code's variant 75.5 to 86.5%.'''
R["fig6c-location-tracks-direction"]='''**Result: partially reproduced.** With PC 2 flipped, the angle of the location in the PC 1-2 plane correlates with target angle in M1-J (0.696, p = 2e-07), PMd-J (0.709, p = 6e-09) and M1-N (0.245, p = 0.015), but not in PMd-N (0.065, p = 0.55, in either orientation).'''
R["jpca-fit-r2"]='''**Result: partially reproduced.** With the skew-symmetric R2 (reading a), jPCA fits 0.768, 0.632, 0.625 and 0.446 in the first plane; three lie in 0.576 to 0.803 and PMd-N does not. Refitted on straight and curved reaches alone, every dataset fits straight reaches better (0.708 to 0.834) than curved ones (0.565 to 0.689), all within their ranges. The unconstrained R2 (reading b) has two of four in range for all conditions. The per-condition test pairs each straight maze with the next maze, which is curved with the same target in all 36 pairs of every dataset (target distance 0); it gives p = 0.069, 0.009, 1e-05 and 0.63, against the paper's p < 0.001, and does not decide.'''
R["jpca-variance-explained"]='''**Result: partially reproduced.** The retained jPCA planes hold on average 8.8, 10.9, 11.6 and 5.4% of the population variance (s.d. 3.5 to 10.8% across conditions, below the paper's 13%); three lie in 6.3 to 13.2% and PMd-N (5.4%; 5.1% under trial reading b) is below.'''
R["suppfig3-model-comparison"]='''**Result: not reproduced.** Under the main reading, the cross-validated TBF value (73.9, 81.3, 88.0 and 81.4%) is above jPCA (5.4 to 11.6%) but below the in-sample single-condition LDS (85.3 to 94.6%) in every dataset. In sample (the variant), TBF (94.1 to 96.9%) exceeds both in every dataset. The main reading compares a held-out value with in-sample ones; this is asked of a reader (questions/sabatini-2024.yaml).'''
R["fig4d-jpca-variance-correlation"]='''**Result: not reproduced.** Rotational variance correlates with the variance in the jPCA planes more strongly than the paper reports: rho = -0.076 and 0.707 (M1-J), 0.930 (PMd-J), 0.677 and 0.620 (M1-N), 0.719 (PMd-N). Per-dataset means are 0.315, 0.930, 0.648 and 0.719, and the significant planes have rho 0.620 to 0.930; under neither reading do all the values lie in 0.351 to 0.506. Five of six planes (83%) are significant, outside 66 +- 6.6%.'''
R["fig4f-plane-alignment-explains-jpca"]='''**Result: partially reproduced.** The alignment of a condition's rotations with a jPCA plane correlates with its variance in that plane for every plane (p at most 1.5e-10), with rho 0.945, 0.931, 0.796, 0.668, 0.819 and 0.805; five of six lie in 0.738 to 1 (M1-N plane 1 does not).'''
R["fig6e-kinematics-predict-location"]='''**Result: reproduced.** With the SVD kinematic basis (reading a), the four reach parameters linearly predict 55.5, 55.5, 70.5 and 41.5% of the variance of the location (within 33.3 to 78.1%), and OU kernel regression 73.0, 68.5, 88.7 and 77.9% (within 62.1 to 89.1%), both above all 1000 permutations. The four other seeds stay in range (OU 65.5 to 88.7%, linear 38.4 to 70.1%). The skew-normal basis (reading b) gives linear 41.6 to 70.5% and OU 69.3 to 89.1%. OU length scales of 1e2 and 1e4 change the kernel values by at most 0.002. The Gaussian kernel (reading b of the kernel) gives 32 to 55%, below the range.'''
R["suppfig2-eigenvalues-from-kinematics"]='''**Result: not reproduced.** Reach parameters and reach duration predict the eigenvalue components with a mean leave-one-out R2 of 0.285 pooled over datasets (0.135 to 0.493 per dataset) under both kinematic readings, above 0.1 +- 0.05; under trial reading (b), 0.275.'''
R["fig7c-ldr-encoding"]='''**Result: reproduced.** Linear LDR encoding explains on average 77.7, 69.0, 84.9 and 73.6% of the population variance (within 54 to 85.8%) and kernel LDR encoding 85.5, 86.3, 92.7 and 87.8% (within 63.9 to 95.7%), both above the shuffled null (p at most 3.0e-08). The skew-normal basis gives the same within 0.006, the four other seeds stay in range (linear 67.3 to 85.0%, kernel 84.8 to 92.7%), and kernel length scales of 1e2 and 1e4 change the kernel means by at most 0.002.'''
R["suppfig7a-not-memorization"]='''**Result: partially reproduced.** With target sextants held out, kernel regression beats nearest-neighbour regression with p < 0.01 in M1-J, M1-N and PMd-N (p 3e-11 to 1e-09), but not in PMd-J (76.5 against 68.4% in M1-J; PMd-J 68.8 against 60.2%, higher on 37 of 72 conditions, p = 0.024 under the SVD basis and 0.50 under the skew-normal basis). Kernel length scales of 1e2 and 1e4 give the same pattern.'''
R["fig7c-standard-encoding-worse"]='''**Result: reproduced.** Both LDR models exceed each standard encoding model in every dataset with p < 0.001 (24 of 24 comparisons under both kinematic readings; p at most 2.5e-10). The linear multi-parameter model explains 52.1 to 54.4%, the OU kernel model on position 39.8 to 52.2% and on velocity 41.9 to 49.2%, against 69.0 to 84.9% (linear LDR) and 85.5 to 92.7% (kernel LDR). The kernel models now use no penalty, as the LDR encoder's kernel does (assumption); with the penalty of 0.1 used before, a variant, they predict only the mean (0.000).'''
R["fig7f-ldr-decoding"]='''**Result: partially reproduced.** The LDR decoder explains on average 77.0, 74.4, 86.6 and 73.0% of the variance of single-trial hand position (SVD basis; medians 82 to 92%); M1-J and M1-N lie in 75.6 to 100%, PMd-J and PMd-N below. The skew-normal basis gives 72.5 to 86.0% with the same two in range, and trial reading (b) 73.4 to 87.4%, again two. Under the four other seeds PMd-J reaches 76.3% once and PMd-N 75.9% once, so two or three of four lie in range under every seed.'''
R["trial-curvature-decoding"]='''**Result: partially reproduced.** Decoded and actual within-condition curvature correlate with p < 0.001 for all eight parameters, with rho 0.292, 0.169, 0.238, 0.102, 0.446, 0.464, 0.198 and 0.300 (SVD basis); 6 of 8 lie in 0.144 to 0.451 (PMd-J parameter 4 is lower, M1-N parameter 4 higher). The skew-normal basis gives 5 of 8.'''
R["suppfig8-no-output-potent-dependence"]='''**Result: not reproduced.** Removing the dimensions that map to hand position and velocity (the dataset has no EMG) lowers the decoded variance by 3.3 to 7.0 points per condition (lower on 70 to 72 of 72 conditions), and the two-sided signed-rank test finds the drop in every dataset (p < 1e-12, below 0.036).'''
R["fig7f-decoder-beats-standard"]='''**Result: partially reproduced.** The LDR decoder explains more of the single-trial hand position than each of the 24 instantaneous decoders run (ridge regression and OU kernel regression on rates in spikes/s smoothed at 20 or 100 ms, trained on single trials or trial averages), with two-sided signed-rank p at most 3e-127 in every comparison, over the same window (-250 to +850 ms, where LDR explains 73.8, 70.8, 84.7 and 69.7%). The best of them reaches 74.7% (M1-N, kernel on single trials, 100 ms). The instantaneous decoders are weak even on the trials of their training conditions (0.000 to 0.869; the trial-average kernel decoders 0.000 to 0.186), so as configured here they are not strong competitors; z-scored inputs and a 6000-point training set give the same outcome. The GPFA decoders were not run, so the claim holds against all but the GPFA decoders.'''
order=[]
for i,c in enumerate(nb["cells"]):
    s="".join(c["source"])
    if c["cell_type"]=="code":
        tags=[t[6:] for t in c["metadata"].get("tags",[]) if t.startswith("claim:")]
        if tags: last=tags[0]
    if c["cell_type"]=="markdown" and s.startswith("**Result"):
        order.append((i,last))
done=set()
for i,cl in order:
    setsrc(nb,i,R[cl]); done.add(cl)
print(sorted(set(R)-done))
save(nb)
EOF
```

```
[]
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/ed; python - <<'EOF'
from nbedit import *
nb=load()
i=find(nb,"**Result: reproduced.** Linear LDR encoding")
rep(nb,i,"(linear 67.3 to 85.0%, kernel 84.8 to 92.7%)","(linear 67.3 to 84.7%, kernel 84.8 to 92.5%)")
i=find(nb,"**Result: reproduced.** Under reading (a), same-frequency")
rep(nb,i,"the medians differ by 0.001 to 0.009","the medians differ by 0.000 to 0.009")
save(nb)
EOF
```

```
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/ed; python - <<'EOF'
from nbedit import *
nb=load()
rep(nb,21,'''(deviation: the paper simulates at the resolution of its 1 ms pipeline).''','''(deviation: the paper simulates at the resolution of its 1 ms pipeline). The rates simulated from are
already smoothed and the counts are smoothed again, which lowers the noise of null (a); null (b), from
the real trials, does not have this problem.''')
rep(nb,31,'''Shuffled data: the 1 ms bins of each trial permuted in time (one permutation for all units of a trial)
before smoothing and averaging, then TBF with the dataset's k. Recoverability per condition: the
variance of the basis functions explained by pinv(L(c)) X(c) (Methods, Eq. 6).''','''Shuffled data: the 1 ms bins of each trial permuted in time (one permutation for all units of a trial)
before smoothing and averaging, then TBF with the dataset's k. The span permuted is the 1.5 s window
read around movement onset (assumption; the paper does not give it). Recoverability per condition: the
variance of the basis functions explained by pinv(L(c)) X(c) (Methods, Eq. 6), on the de-mixed basis.
Chance is the same measure on the shuffled data, with the shuffled basis de-mixed in the same way; the
raw shuffled basis is shown as a variant.''')
setsrc(nb,51,'''## fig4c-subspace-excursion-angles

> Across conditions, each rotation's planes spanned 6 to 20 distinct dimensions with angles above 45
> degrees to each other, and more that varied above chance.

SEA to 25 dimensions, every condition tried as the seed. Excursion angles are counted after the seed
plane; the count including the seed's dimensions is shown as a variant. Chance (claims: "fraction of
noise SEA above the data", code singleFrequencyOverlapControl.m, not described further): SEA run on
the 72 half-split estimates of a single condition's plane (36 repeats, two halves each), which differ
only by estimation noise, for 24 conditions per rotation and three seed planes per run (time). A data
dimension is above chance when fewer than 5% of these noise SEA curves reach its angle. This reading
of the control is an assumption. The earlier threshold, the 95th percentile of the largest principal
angle between two half-split planes of one condition, is shown as a variant.''')
rep(nb,55,'''dimensionality by the half-split procedure of the Methods, 100 folds: basis from partition 1, loadings
regressed on it for both partitions, PCA of partition 1's loadings; the dimensionality that maximises
the alignment index between the bottlenecked partition-1 loadings and partition 2's (all dimensions
searched).''','''dimensionality by the half-split procedure of the Methods, 100 folds: basis from partition 1, loadings
regressed on it for both partitions, PCA of partition 1's loadings ("PCA on the dimensions occupied by
these rotations", not mean-centred, so that the bottleneck to d PCs spans the loadings themselves);
the dimensionality that maximises the alignment index between the bottlenecked partition-1 loadings
and partition 2's (all dimensions searched).''')
rep(nb,108,'''kernel regression on velocity, length scale 1e11. The kernel penalty is not given; 0.1 is used
(assumption, the Methods' L2 for kernel decoders).''','''kernel regression on velocity, length scale 1e11. The kernel penalty is not given. At these length
scales the kernel matrix differs from a matrix of ones by about 1e-10, so any appreciable penalty
reduces the fit to the training mean; the length scales only make sense with no penalty, as the
claims give for the LDR encoder's kernel (code). No penalty (1e-8, for numerical stability) is used
(assumption); the Methods' L2 of 0.1 for kernel decoders is shown as a variant.''')
setsrc(nb,120,'''## fig7f-decoder-beats-standard

Instantaneous decoders of hand position (Methods, Comparing LDR-based decoding to instantaneous
decoding methods): activity 100 ms before each time point, smoothed with a 20 ms Gaussian (the
single-trial rates used throughout) or a 100 ms Gaussian (10 ms counts smoothed with s.d. 10 bins, a
standard approximation), in spikes/s as they are (the Methods do not standardise them); ridge
regression (lambda 1) trained on single trials; OU kernel regression (length scale 100, L2 0.1)
trained on a random subset of 3000 single-trial time points (the Methods' "subset of single-trial
data"; the size is an assumption) or on trial averages. The same two folds of conditions as the LDR
decoder. Variance explained in position per trial over -250 to +850 ms, the window the 100 ms lag
allows, for both these decoders and the LDR decoder, compared by two-sided signed-rank tests. Variants:
z-scored rates, and a training subset of 6000 points. As a check of each decoder, its variance
explained on single trials of its training conditions is printed. The comparison is run against the
LDR decoder under both kinematic readings. The GPFA decoders are not run: the paper gives neither the
latent dimensionality nor the bin size, and fitting GPFA was not attempted in the time available.''')
save(nb)
EOF
```

```
Shell cwd was reset to
```

**Agent**

Now the header and summary.

**Agent calls Bash**

```bash
cd $TMPDIR/ed; python - <<'EOF'
from nbedit import *
nb=load()
rep(nb,0,'''Where a parameter comes from (the claim, a passage of the paper, an assumption, or a standard choice)
is said in the docstrings of the helper `ldr.py` and beside the code here.''','''Trials: the analyses use trial reading (a) of the claims file, all successful trials of the 72
conditions (an assumption; see "Conditions and trial readings"). The companion notebook
`reproduce_sabatini_2024_trials_b.ipynb` is this notebook run under reading (b), successful trials with
a delay above 400 ms, with each claim's own seed only; every outcome is the same under both readings.

Where a parameter comes from (the claim, a passage of the paper, an assumption, or a standard choice)
is said in the docstrings of the helper `ldr.py` and beside the code here.''')
setsrc(nb,124,'''## Summary

| Claim | Outcome |
|---|---|
| data-composition | reproduced (the units are one per electrode, unlabelled) |
| jpca-fit-r2 | partially reproduced (3 of 4 in range) |
| jpca-variance-explained | partially reproduced (3 of 4 in range) |
| single-lds-variance | not reproduced (78 to 83%, above 41 to 73%) |
| fig2c-condition-lds-variance | reproduced |
| fig3a-eigenvalue-clusters | not reproduced (clusters present; frequencies near 0.7, 1.6 to 2.4 Hz) |
| fig3c-eigenvalue-distance-auc | not reproduced (AUC 0.64 to 0.81) |
| suppfig2-eigenvalues-from-kinematics | not reproduced (mean R2 0.285) |
| fig3g-basis-frequencies | not reproduced (2 pairs in PMd-J; rotations near 0.7, 1.5 to 1.9 and 2.7 to 3.2 Hz) |
| tbf-variance-explained | reproduced |
| tbf-shuffle-control | partially reproduced (3 of 4 in range) |
| fig3h-recoverability | partially reproduced (chance level higher) |
| fig3i-duration-warping | not reproduced |
| suppfig3-model-comparison | not reproduced under the main reading; holds in sample |
| fig4b-plane-alignment | reproduced |
| fig4c-subspace-excursion-angles | partially reproduced (8 of 11 counts in range) |
| rotation-orientation-dimensionality | not reproduced (lower dimensional) |
| fig4d-jpca-variance-correlation | not reproduced (stronger correlations) |
| fig4f-plane-alignment-explains-jpca | partially reproduced (5 of 6 planes) |
| fig5a-frequencies-segregated | reproduced (small effect for M1-N 3.24 Hz) |
| fig5c-rotations-predict-rotations | reproduced |
| suppfig6a-location-alignment | partially reproduced (3 of 4) |
| suppfig6b-location-dimensionality | not reproduced |
| suppfig6c-location-distinct-from-rotations | reproduced |
| fig6b-location-predicts-rotations | reproduced |
| fig6c-location-tracks-direction | partially reproduced (3 of 4) |
| fig6e-kinematics-predict-location | reproduced |
| fig7c-ldr-encoding | reproduced |
| suppfig7a-not-memorization | partially reproduced (3 of 4) |
| fig7c-standard-encoding-worse | reproduced |
| fig7f-ldr-decoding | partially reproduced (2 of 4) |
| fig7f-decoder-beats-standard | partially reproduced (GPFA decoders not run) |
| suppfig8-no-output-potent-dependence | not reproduced (without EMG) |
| trial-curvature-decoding | partially reproduced (6 of 8) |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the reasoning and
the differences from the paper's method.

**How the analysis differs from the paper's.** The dandiset's units are one per electrode (96 per
array) with no single- or multi-unit label, where the paper used 79 to 118 sorted single and stable
multi-units per array; every population measure here rests on these units. Trials are all successful
trials of the 72 conditions (trial reading (a); an assumption, as the paper gives no trial selection);
the companion notebook runs reading (b), delays above 400 ms, and gives the same outcome for every
claim. The eigenvalue nulls use 100 repeats, not 500, and the Poisson null is simulated at 10 ms. The
paper's code is not run (it needs preprocessed files that are not public); the methods follow the
claims file, the Methods, and the code as the claims file reports it. Assumptions where the paper is
silent: the span of the time shuffle, the noise SEA of fig4c, no penalty for the kernel encoders of
fig7c-standard-encoding-worse, the scale of the kinematic basis (length scales 10 times smaller or
larger give the same results), and the size of the kernel decoders' training subset. The dataset has
no EMG, so suppfig8 removes the kinematic dimensions only. The GPFA decoders were not run.

**What was found about the dataset.** The Nitschke file joins five recording segments whose clocks
overlap: trial start times, hand timestamps and every unit's spike times jump backwards four times, so
spike times are not sorted and a trial's spikes cannot be found by time alone. Assigning each trial to
its segment in file order gives condition decoding well above chance in segments 0 to 3 and at chance
with the previous trial's labels, so the alignment within segments is consistent with the trial table;
condition information in segment 3 is lower within the segment (0.18) than in segments 0 to 2 (0.45
to 0.50), while a decoder trained on the other segments still reaches 0.49 there. In the Jenkins file
one unit's spike train restarts at the beginning of the session (two runs concatenated). Hand position
is stored as "meters" with a conversion of NaN, but its values are in millimetres (reaches of about
130). The units table has one unit per electrode on all 192 electrodes of each file and no quality,
sorting or single/multi-unit column.''')
save(nb)
EOF
```

```
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/ed; python - <<'EOF'
from nbedit import *
nb=load()
rep(nb,124,"segments 0 to 2 (0.45\nto 0.50)","segments 0 to 2 (0.44\nto 0.50)")
save(nb)
EOF
cd $TMPDIR/ed && python mkcompanion.py && cd  && cat entries/sabatini-2024/README.md && date -u
```

```
wrote entries/sabatini-2024/reproduce_sabatini_2024_trials_b.ipynb 91 cells
# Sabatini & Kaufman (2024) from dandiset 000070

Tests the findings of [Sabatini & Kaufman (2024)](https://doi.org/10.1038/s41467-024-51308-7) on
[DANDI:000070](https://dandiarchive.org/dandiset/000070/0.260528.0919), version 0.260528.0919, which holds
the two maze-task sessions the paper names (monkey J, 2009-09-18; monkey N, 2010-09-23), each with a PMd
and an M1 Utah array and hand position. The notebook rebuilds the paper's four datasets (M1-J, PMd-J,
M1-N, PMd-N) and tests its claims on jPCA, single-condition dynamics, the temporal basis factorization,
the orientation of rotational planes, the state space location, and LDR encoding and decoding.

| Group | Outcomes |
|---|---|
| Reproduced | 9 claims, among them the factorization's variance explained, the misalignment of rotational planes across conditions, prediction of rotations from each other and from the location, and LDR encoding |
| Partially reproduced | 16 claims, among them the comparison with instantaneous decoders, run without the GPFA decoders |
| Not reproduced | 9 claims, among them the eigenvalue distances, the single-LDS fit, the dimensionality of rotation orientations and location, and the warping control |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the reasoning and
the differences from the paper's method.

The dandiset's units are one per electrode, with no single- or multi-unit label, where the paper used
[... 7 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/sabatini-2024 && python - <<'EOF'
p='README.md'; s=open(p).read()
old=s[s.index('| Reproduced |'):s.index('A failure to reproduce')]
new='''| Reproduced | 11 claims, among them the factorization's variance explained, the misalignment of rotational planes across conditions, the segregation of frequencies, prediction of rotations from each other and from the location, and LDR encoding against standard encoding models |
| Partially reproduced | 12 claims, among them LDR decoding, the time-shuffle control, and the comparison with instantaneous decoders, run without the GPFA decoders |
| Not reproduced | 11 claims, among them the eigenvalue frequencies and distances, the basis frequencies, the single-LDS fit, the dimensionality of rotation orientations and location, and the warping control |

'''
s=s.replace(old,new)
s=s.replace('''sorted units; the Nitschke file joins five recording segments whose clocks overlap.''','''sorted units; the Nitschke file joins five recording segments whose clocks overlap. The main notebook
uses all successful trials; `reproduce_sabatini_2024_trials_b.ipynb` runs the same analyses on trials
with a delay above 400 ms, the claims file's other reading, and every outcome is the same.''')
s=s.replace('''and takes about 30 minutes.''','''and the two notebooks take about 25 and 15 minutes.''')
open(p,'w').write(s)
p='entry.yaml'; s=open(p).read()
s=s.replace('''  runtime_minutes: 30
''','''  runtime_minutes: 25
- path: reproduce_sabatini_2024_trials_b.ipynb
  title: The same analyses on trials with a delay above 400 ms (trial reading b)
  runtime_minutes: 15
''')
open(p,'w').write(s)
EOF
cat entry.yaml | sed -n 10,20p
```

```
license: Apache-2.0
python: "3.13"
notebooks:
- path: reproduce_sabatini_2024.ipynb
  title: Reproducing Sabatini & Kaufman (2024) from dandiset 000070
  runtime_minutes: 25
- path: reproduce_sabatini_2024_trials_b.ipynb
  title: The same analyses on trials with a delay above 400 ms (trial reading b)
  runtime_minutes: 15
helpers:
- ldr.py
```

**Agent calls Bash**

```bash
cd  && date -u && time python tools/entry.py all entries/sabatini-2024 2>&1 | tail -15; date -u
```

```
Fri Nov 20 15:15:26 UTC 2026
Installed kernelspec registry-sabatini-2024 in executed/sabatini-2024/.venv/share/jupyter/kernels/registry-sabatini-2024
0 error(s)
pass  reproduce_sabatini_2024.ipynb  (1276 s)
pass  reproduce_sabatini_2024_trials_b.ipynb  (718 s)

real	33m23.301s
user	93m34.097s
sys	4m8.656s
Fri Nov 20 15:48:49 UTC 2026
```

**Agent**

Both notebooks pass. Checking that the executed copies match the dev run I wrote the conclusions from.

**Agent calls Bash**

```bash
cd $TMPDIR && python - <<'EOF'
import json, re
def outs(p):
    nb=json.load(open(p)); d={}
    for c in nb['cells']:
        if c['cell_type']!='code': continue
        tags=[t for t in c['metadata'].get('tags',[]) if t.startswith('claim:') or t=='sanity']
        txt=''.join(''.join(o.get('text','')) if isinstance(o.get('text',''),list) else o.get('text','') for o in c.get('outputs',[]))
        if tags: d[tags[0]]=txt
    return d
for name in ('reproduce_sabatini_2024.ipynb','reproduce_sabatini_2024_trials_b.ipynb'):
    a=outs('run1/'+name); b=outs('executed/sabatini-2024/'+name)
    diff=[k for k in a if re.sub(r'reading \(','',a[k]).replace('kinematic ','')!=re.sub(r'reading \(','',b.get(k,'')).replace('kinematic ','') and k!='sanity']
    print(name, 'differing claim cells:', diff)
EOF
```

```
reproduce_sabatini_2024.ipynb differing claim cells: []
reproduce_sabatini_2024_trials_b.ipynb differing claim cells: []
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd  (pdftotext paper/*.pdf - 2>/dev/null || python -c "
import sys
from pypdf import PdfReader
r=PdfReader(sys.argv[1]); print('\n'.join(p.extract_text() for p in r.pages))" paper/*.pdf) | grep -n -i -B2 -A12 "Supplementary Figure 3" | head -60
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  ls executed/sabatini-2024/.venv/lib/python3.13/site-packages | grep -i -E "pdf|fitz|mupdf" ; python -c "import fitz" 2>&1; grep -o "Supplementary Fig. 3.\{0,300\}" paper/*.txt | head; grep -o ".\{400\}Supplementary Fig. 3 ).\{100\}" paper/*.txt | head -3
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  timeout 120 uv run --no-project --with pypdf python -c "
import sys,re
from pypdf import PdfReader
r=PdfReader(sys.argv[1]); t='\n'.join(p.extract_text() for p in r.pages)
i=t.find('Supplementary Figure 3'); print(t[i-100:i+1500])" paper/*.pdf 2>&1 | tail -40
```

Result: not kept, because it reads the paper's text.

**Agent**

Now the question for a reader.

**Agent calls Write**

```json
{
 "file_path": "questions/sabatini-2024.yaml",
 "content": "questions:\n- claim: suppfig3-model-comparison\n  question: The criterion's main reading compares a cross-validated value for the factorization (the\n    held-out variance at the chosen k) with in-sample values for jPCA and the single-condition LDS,\n    and makes the all-in-sample comparison a variant. The Supplementary Figure 3 legend says the LDR\n    model \"explains greater neural variance when cross-validated\" than the condition-specific LDS, and\n    gives as reasons the more stable eigenvalues and the objective, which speaks of all three models\n    under the same validation. Should all three models be compared under the same validation, either\n    all cross-validated (held-out variance for jPCA and the LDS as well, if the paper or code fixes how)\n    or all in sample, in place of the mix?\n  passage: 'Supplementary Figure 3 legend, \"Note that while the \"different planes, shared eigenvalues\"\n    (LDR) model is a subset of the \"different planes and eigenvalues\" (condition-specific LDS) model,\n    the \"different planes, shared eigenvalues\" explains greater neural variance when cross-validated.\n    This improvement has two sources. First, as this model assumes that eigenvalues are shared across\n    conditions, it gets to estimate rotational frequencies using every condition, leading to more\n    stable estimates of eigenvalues. Second, LDS models predict the population state''s derivative\n    from the state, which does not directly optimize variance explained.\" Results, Identifying\n    rotations with varying planes, paragraph 4, \"Our method also explained greater variance than jPCA\n    or even single-condition LDSs (due to lower overfitting and differences in objective function;\n    Supplementary Fig. 3 ).\"'\n  why: The outcome turns on the reading. Under the main reading the held-out factorization value (73.9\n    to 88.0%) is below the in-sample single-condition LDS (85.3 to 94.6%) in every dataset, so the\n    claim is not reproduced; with all three in sample the factorization (94.1 to 96.9%) is highest in\n    every dataset and the claim is reproduced. The claims file's check already noted the mix as open.\n    The verifier of round 1 reported it as a reading of the claims file that affects the conclusion.\n"
}
```

```
File created successfully at: questions/sabatini-2024.yaml (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd  python -c "import yaml;print(yaml.safe_load(open('questions/sabatini-2024.yaml'))['questions'][0]['passage'][:200])"; grep -n "verifications" -A40 attempts/*.yaml | grep -v "^--$" | head -80; ls schemas 2>/dev/null; grep -rn "verifications" tools/*.py | head
```

```
Supplementary Figure 3 legend, "Note that while the "different planes, shared eigenvalues" (LDR) model is a subset of the "different planes and eigenvalues" (condition-specific LDS) model, the "differ
attempts/amjad-2025-01.yaml:287:verifications:
attempts/amjad-2025-01.yaml-288-- date: '2026-10-15'
attempts/amjad-2025-01.yaml-289-  kind: agent
attempts/amjad-2025-01.yaml-290-  by: Independent agent run by CatalystNeuro (same harness, separate context, did not write the notebook)
attempts/amjad-2025-01.yaml-291-  reviewed: The first executed notebook with the conclusion cells and the summary removed, the helper
attempts/amjad-2025-01.yaml-292-    module and the claims file, with the paper's full text (PMC12183687). The verifier read the
attempts/amjad-2025-01.yaml-293-    archive's file list and metadata through the DANDI API and tested the helpers on synthetic inputs
attempts/amjad-2025-01.yaml-294-    (beta_power, burst_onsets, window_mean, codes_per_trial, rereference, fscv_window_mean, best_lag,
attempts/amjad-2025-01.yaml-295-    reward_blocks). It had no attempt record and took the claims from the claims file.
attempts/amjad-2025-01.yaml-296-  results:
attempts/amjad-2025-01.yaml-297-  - claim: insertion-yield
attempts/amjad-2025-01.yaml-298-    agrees: true
attempts/amjad-2025-01.yaml-299-    outcome: blocked
attempts/amjad-2025-01.yaml-300-    reason: The archive has 3 assets with sites c8dg, c3bs, c3a and cl3, and nothing about implanted
attempts/amjad-2025-01.yaml-301-      or failed sensors. Figure 3 names 4 functional Monkey T sites against the paper's "3/14", so
attempts/amjad-2025-01.yaml-302-      "sensor" may mean probe. Neither count can be checked; an implant log of sensors per monkey is
attempts/amjad-2025-01.yaml-303-      not in the archive.
attempts/amjad-2025-01.yaml-304-    response: No change.
attempts/amjad-2025-01.yaml-305-  - claim: chronic-duration
[... 75 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python -c "
import json;s=json.load(open('schemas/attempt.schema.json'))
v=s['properties']['verifications']; print(json.dumps(v,indent=1)[:3500])"
```

```
{
 "type": "array",
 "items": {
  "type": "object",
  "additionalProperties": false,
  "required": [
   "date",
   "kind",
   "by",
   "results"
  ],
  "properties": {
   "date": {
    "type": "string",
    "format": "date"
   },
   "kind": {
    "enum": [
     "agent",
     "person",
[... 89 more lines not kept]
```

**Agent calls Bash**

```bash
date -u; cd  sed -n '/^verifications/,$p' attempts/andrews-2024-01.yaml | grep -n "^[a-z]" | head; grep -n "^[a-z_]*:" attempts/andrews-2024-01.yaml | head -30
```

```
Fri Nov 20 15:49:35 UTC 2026
1:verifications:
1:schema_version: 3
2:id: andrews-2024-01
3:datasets:
9:paper: doi:10.1038/s41593-024-01782-5
10:date: 2026-11-10
11:entry: andrews-2024
12:provenance:
23:outcomes:
241:findings:
281:inputs:
285:verifications:
```

**Agent calls Bash**

```bash
mkdir -p $TMPDIR/rec && cat > $TMPDIR/rec/build.py <<'PYEOF'
import yaml, datetime
P = "attempts/sabatini-2024-01.yaml"
rec = yaml.safe_load(open(P))
U = ("Units are the dandiset's 96 per-electrode units per array, with no single or multi-unit label, "
     "where the paper used 79 to 118 sorted single and stable multi-units.")
T = ("Trials are all successful trials of the 72 conditions (trial reading (a) of the claims file), an "
     "assumption. The paper gives no trial selection; the Methods describe the task with \"a brief delay "
     "(0-1000 ms)\" and name no exclusion (Methods, Subjects, behavior and data pre-processing), and the "
     "analyses are of activity around movement onset. Both readings give counts within 10% of the paper's "
     "(1595 and 2121, or 1381 and 1884 with delays above 400 ms, against 1469 and 2014). Every analysis is "
     "also run under reading (b) in reproduce_sabatini_2024_trials_b.ipynb (claim's own seed only), and "
     "the outcome is the same.")
C = ("The paper's MATLAB code was not run; it needs preprocessed files that are available only on "
     "request. Methods follow the claims file and the Methods.")
COMMON = [U, T, C]
NB = "reproduce_sabatini_2024.ipynb"

def o(claim, outcome, notes, extra=(), measured=None, assumed=True):
    d = {"claim": claim, "outcome": outcome, "notebook": NB, "output": f"claim:{claim}"}
    if assumed:
        d["assumed"] = True
    if measured is not None:
        d["measured"] = measured
    d["notes"] = notes
    d["deviations"] = COMMON + list(extra)
    return d

out = [
o("data-composition", "reproduced",
  "Both monkeys have the 72 conditions, 36 straight and 36 curved; the two readings of the conditions give "
  "the same set (maze conditions not a multiple of 3 are exactly the 1-target mazes, once maze 0, a set of "
  "203 and 419 trials outside the 108, is left out). Trials, reading (a) all successful, 1595 (J) and 2121 "
  "(N); reading (b) delay above 400 ms, 1381 and 1884; all four within 10% of 1469 and 2014. Each array "
  "holds 96 units, inside 71 to 130. The units table has no single-unit, multi-unit or quality column "
  "(its columns are electrode_group, electrodes, id, obs_intervals and spike_times), so all units are "
  "counted. Each of the 192 electrodes of each file carries exactly one unit, so these are per-electrode "
  "units and are not shown to be the paper's sorted units (recorded as a finding).",
  measured=[72, 1595, 2121], assumed=False),
o("jpca-fit-r2", "partially_reproduced",
  "Reading (a), the skew-symmetric R2 in the first plane, gives 0.768, 0.632, 0.625 and 0.446 (M1-J, "
  "PMd-J, M1-N, PMd-N); three of four in 0.576 to 0.803. Refitted on straight and curved reaches alone, "
  "straight 0.834, 0.708, 0.768, 0.778 and curved 0.689, 0.575, 0.655, 0.565, all in their ranges and "
  "straight higher in every dataset. Reading (b), unconstrained, gives 0.820, 0.658, 0.684, 0.461 (two of "
  "four in range). The per-condition R2 paired by maze (each straight maze with the next maze, curved with "
  "the same target in all 36 pairs of every dataset) gives p = 0.069, 0.009, 1e-05 and 0.63, against the "
  "paper's p < 0.001; this part does not decide. Trial reading (b) gives 0.776, 0.664, 0.623, 0.452, the "
  "same outcome."),
o("jpca-variance-explained", "partially_reproduced",
  "Retained planes (two for M1, one for PMd) hold on average 8.8, 10.9, 11.6 and 5.4% of the population "
  "variance, s.d. 3.6, 10.8, 5.5 and 3.5% across conditions (the paper gives s.d. below 13%). Three of four "
  "lie in 6.3 to 13.2%; PMd-N is below (5.1% under trial reading b)."),
o("single-lds-variance", "not_reproduced",
  "One full-rank LDS over all conditions, simulated from each condition's state at -150 ms, explains on "
  "average 78.1, 82.0, 82.9 and 78.6% over -150 to +850 ms (reading a) and 80.6, 84.6, 87.2 and 83.4% over "
  "the whole window (reading b), above 41.4 to 72.6% in every dataset; trial reading (b) gives 76.6 to "
  "82.1%. Units pooled per electrode may give smoother, lower-dimensional population activity than sorted "
  "units, which would raise every variance explained here."),
o("fig2c-condition-lds-variance", "reproduced",
  "Cross-validated dimensionality (even split, odd k from 1 to 21, 100 folds) is 5, 5, 7 and 5, the same "
  "under all five seeds; the LDS explains 85.3, 91.1, 94.6 and 91.2% (s.d. 3.4 to 4.8%), within 63.9 to "
  "100%. The code's 3/4 split chooses 7, 5, 7 and 7. Trial reading (b) gives the same k and 84.4 to 94.2%."),
o("fig3a-eigenvalue-clusters", "not_reproduced",
  "Every condition has the same number of complex pairs (2 in the k = 5 datasets; 3 in M1-N except one "
  "condition) and at least one real eigenvalue on all 72 conditions, so the eigenvalues cluster with an "
  "offset. Median pair frequencies are 0.86 and 2.38 Hz (M1-J), 0.56 and 1.55 (PMd-J), 0.68, 1.76 and 3.20 "
  "(M1-N), 0.73 and 1.68 (PMd-N); only PMd-J 1.55 Hz is within 10% of its target. Under trial reading (b) "
  "PMd-J has 0.54 and 1.53 Hz, both within 10%, and the other three still miss. The criterion needs every "
  "dataset, and the frequencies are systematically higher than 0.5 and 1.5 Hz in three datasets."),
o("fig3c-eigenvalue-distance-auc", "not_reproduced",
  "AUC under the Poisson null (a) 0.813, 0.710, 0.636, 0.696 and under the half-split null (b) 0.724, "
  "0.672, 0.688, 0.696; only M1-N under (a) lies in 0.459 to 0.638. The code's norm distance gives AUCs "
  "within 0.02 of these. Under null (b) the five seeds give 0.714 to 0.726 (M1-J), 0.665 to 0.685, 0.688 "
  "to 0.700 and 0.688 to 0.697. Median distance between conditions 0.011 to 0.016, noise 0.006 to 0.013. "
  "Trial reading (b) gives 0.631 to 0.812, the same single dataset in range.",
  extra=["100 repeats per condition for each null, where the Methods give 500 (time); the other four seeds "
         "use 20.",
         "The Poisson null simulates 10 ms counts from the smoothed rates and smooths them again at 10 ms "
         "resolution, which lowers its noise, where the paper's pipeline works at 1 ms. The half-split null "
         "(b) does not have this problem and also fails."]),
o("suppfig2-eigenvalues-from-kinematics", "not_reproduced",
  "Mean leave-one-out R2 over the real and imaginary parts of the frequency-sorted eigenvalues, pooled over "
  "the four datasets, is 0.285 under both kinematic readings (0.135 to 0.493 per dataset), above 0.1 +- "
  "0.05; 0.275 under trial reading (b). Components without variance (the imaginary part of the real "
  "eigenvalue) are left out; they would add zeros and lower the mean.", measured=0.285),
o("fig3g-basis-frequencies", "not_reproduced",
  "Cross-validation chooses k = 6, 5, 7 and 6 under all five seeds; raised to odd, 7, 5, 7, 7. De-mixing "
  "gives 3 rotation pairs and one offset in M1-J, M1-N and PMd-N, 2 pairs in PMd-J, where the criterion "
  "asks for 3 or 4 in every dataset. Frequencies 0.71, 1.85, 3.13 (M1-J), 0.64, 1.54 (PMd-J), 0.69, 1.81, "
  "3.24 (M1-N), 0.74, 1.56, 2.71 Hz (PMd-N); 3 of 11 are within 10% of 0.5, 1.5, 2.5 or 4 Hz and none is "
  "near 0.5 or 4 Hz. The frequencies depend on the window: fitted over -350 to +850 ms they are 0.55 to "
  "0.71, 1.37 to 1.70 and 2.52 to 2.96 Hz, over 0 to +850 ms 0.61 to 0.67, 1.56 to 1.91 and 2.76 to 3.16 "
  "Hz. Trial reading (b) gives the same pattern."),
o("tbf-variance-explained", "reproduced",
  "Reading (a), -150 to +850 ms with the de-mixed basis, 94.1, 94.3, 96.9 and 95.8% (s.d. 0.7 to 1.4%); "
  "reading (b), whole window and raw basis, 92.8, 93.0, 96.3 and 95.0%; all within 81 to 100%. Trial "
  "reading (b) gives 92.1 to 96.6%."),
o("tbf-shuffle-control", "partially_reproduced",
  "Shuffled variance explained 42.2, 28.7, 41.9 and 42.1%, real higher on 72 of 72 conditions, rank-sum p = "
  "3.9e-25 (signed-rank variant 1.7e-13). PMd-J lies below 31.5 to 50.6%. Under the five seeds the "
  "shuffled means vary by at most 0.008 (PMd-J 0.287 to 0.291); trial reading (b) gives PMd-J 0.287.",
  extra=["Time bins are permuted within the 1.5 s window read around movement onset (-500 to +1001 ms), with "
         "one permutation for all units of a trial so that correlations between units are kept (Methods, "
         "Control for data smoothing, \"preserving inter-neuron spike correlations\"); the span shuffled is "
         "not given and is an assumption. A longer span would lower the shuffled value, a shorter one raise "
         "it."]),
o("fig3h-recoverability", "partially_reproduced",
  "Recoverability 97.4, 98.0, 98.6 and 98.7% (within 81.9 to 100%), real higher on all 72 conditions, "
  "rank-sum p = 3.9e-25. Chance, the shuffled data with its basis de-mixed as the real one is, is 89.5, "
  "86.5, 89.1 and 89.6%, the same to three decimals with the raw shuffled basis; only PMd-J lies in 56.7 to "
  "88%. Five seeds move chance by less than 0.01. The main result holds; the chance level is higher than "
  "the paper's. Trial reading (b) gives chance 86.0 to 89.7%, again only PMd-J in range."),
o("fig3i-duration-warping", "not_reproduced",
  "Unwarped rho -0.203 (p = 0.087), 0.072, 0.204 (M1-N, p = 0.086) and 0.133; M1-N has the opposite sign "
  "to -0.26 and M1-J lies just outside -0.198 to 0.231. Warped (600 ms, truncated at 850 ms) rho -0.550 (p "
  "= 6e-07), -0.106, -0.040 and -0.226; only M1-J lies in -0.693 to -0.468 with p < 0.001. The 250 ms "
  "post-reach variant gives -0.396, -0.231, -0.116 and -0.357. Condition mean durations are 234 to 601 ms "
  "(J) and 253 to 570 ms (N). Trial reading (b) gives M1-N unwarped +0.235 (p = 0.047) and, warped, only "
  "M1-J (-0.514) in range.", measured=0.204,
  extra=["Reach end is searched within 850 ms after onset, so durations are capped at 850 ms.",
         "Warping is applied to the 1 ms smoothed rates of each trial before averaging; the basis of the "
         "warped data is de-mixed before recoverability is computed."]),
o("suppfig3-model-comparison", "not_reproduced",
  "Under the main reading the cross-validated TBF value (held-out variance at the dataset's k; 73.9, 81.3, "
  "88.0, 81.4%) exceeds jPCA (5.4 to 11.6%) but not the in-sample single-condition LDS (85.3 to 94.6%) in "
  "any dataset. With all three in sample (the variant), TBF (94.1 to 96.9%) is the highest in every "
  "dataset. The outcome turns on the reading; whether the main reading's mix of a held-out and in-sample "
  "values reads the paper rightly is asked of a reader (questions/sabatini-2024.yaml)."),
o("fig4b-plane-alignment", "reproduced",
  "AUC per rotation 0.923, 0.892, 0.876 (M1-J), 0.950, 0.938 (PMd-J), 0.953, 0.956, 0.937 (M1-N), 0.961, "
  "0.953, 0.943 (PMd-N), observed lower on 72 of 72 conditions; reading (a) signed-rank p = 1.7e-13 for "
  "each; reading (b) rank-sum p printed as 0. Four other seeds change each AUC by at most 0.002; trial "
  "reading (b) gives 0.861 to 0.958. The paper's 4 Hz rotation is not present here; the rotations tested "
  "are those found."),
o("fig4c-subspace-excursion-angles", "partially_reproduced",
  "Excursion angles above 45 degrees per rotation, 5, 12, 11 (M1-J), 7, 11 (PMd-J), 3, 9, 10 (M1-N), 8, "
  "17, 25 (PMd-N); 8 of 11 in 5.4 to 22. Against the noise SEA (SEA of the 72 half-split estimates of one "
  "condition's plane, 24 conditions per rotation), all 25 dimensions are above chance (fewer than 5% of "
  "noise curves reach the data's angle) for every rotation, more than the count above 45 degrees for 10 of "
  "11 rotations; for PMd-N 2.71 Hz both reach the 25 computed. The earlier percentile threshold, now a "
  "variant, gives 4 to 10 dimensions above chance. Trial reading (b) gives counts of 3 to 25, again 8 of "
  "11 in range.",
  extra=["The search over sequences is a greedy search from every seed, keeping the sequence with the largest "
         "summed angles; the Methods say the search was optimised over all sequences.",
         "Chance (claims, \"fraction of noise SEA above the data\", code singleFrequencyOverlapControl.m, not "
         "described further) is taken as SEA run on the 72 half-split estimates (36 repeats, two halves) of "
         "one condition's plane, for every third condition, with three seed planes per run (time); a data "
         "dimension is above chance when fewer than 5% of these noise curves reach its angle (assumption)."]),
o("rotation-orientation-dimensionality", "not_reproduced",
  "PCs to 80% are 2 to 21 (reading a, stacked columns) or 2 to 20 (reading b, activity), and participation "
  "ratios 1.7 to 17.5 or 1.7 to 17.4, against 20.7 to 44 and 15.03 to 40.48; only PMd-N 2.71 Hz is in "
  "range. With the SNR procedure's PCA no longer mean-centred (so that the bottleneck spans the loadings, "
  "Methods, \"PCA on the dimensions occupied by these rotations\"), the SNR dimensionality is 9 to 21 for "
  "all 11 rotations, inside 6.3 to 36.3, and within 1 under the five seeds. Two of the three measures fail; "
  "orientations here are much lower-dimensional than in the paper by PCA."),
o("fig4d-jpca-variance-correlation", "not_reproduced",
  "Rho per plane -0.076 and 0.707 (M1-J), 0.930 (PMd-J), 0.677 and 0.620 (M1-N), 0.719 (PMd-N). Reading "
  "(a), per-dataset means 0.315, 0.930, 0.648, 0.719; reading (b), significant planes 0.620 to 0.930; "
  "under neither do all lie in 0.351 to 0.506. Five of six planes (83%) have p < 0.05, outside 66 +- 6.6%. "
  "The correlations are mostly stronger than the paper's. Trial reading (b) gives the same.", measured=83),
o("fig4f-plane-alignment-explains-jpca", "partially_reproduced",
  "Rho 0.945, 0.931 (M1-J), 0.796 (PMd-J), 0.668, 0.819 (M1-N), 0.805 (PMd-N), all with p at most 1.5e-10; "
  "five of six in 0.738 to 1. Trial reading (b) gives 0.689 to 0.941, again five of six."),
o("fig5a-frequencies-segregated", "reproduced",
  "Under reading (a), for all 20 ordered rotation comparisons the one-sided signed-rank test that "
  "same-frequency alignment is higher gives p at most 1.4e-12, and the Hodges-Lehmann estimate of the "
  "paired difference is positive (+0.011 to +0.558). For M1-N 3.24 Hz onto 0.69 and 1.81 Hz the effect is "
  "small: medians 0.183 against 0.197 and 0.198, median paired difference +0.002 and -0.004, "
  "Hodges-Lehmann +0.025 and +0.024, same higher on 50% and 49% of pairs, and the rank-sum test of reading "
  "(b) gives p = 0.31 and 0.29. Trial reading (b) gives the same, with one-sided p at most 1.9e-08."),
o("fig5c-rotations-predict-rotations", "reproduced",
  "Mean variance explained per ordered pair 44.7 to 95.0% (all 20 in 38.7 to 100%), null 2.9 to 75.2%, "
  "signed-rank p at most 7.6e-13 for every pair, with the median paired difference positive. Four other "
  "seeds move pair means by at most 0.04; trial reading (b) gives 41.4 to 94.6%.",
  extra=["Rotations of each fold's factorization are matched to the full-data rotations by nearest "
         "frequency."]),
o("suppfig6a-location-alignment", "partially_reproduced",
  "AUC 0.901, 0.784, 0.887 and 0.952, observed lower on 72 of 72 conditions in every dataset, signed-rank "
  "p = 1.7e-13; PMd-J is below 0.792. Four other seeds give PMd-J 0.769 to 0.774; trial reading (b) "
  "0.748."),
o("suppfig6b-location-dimensionality", "not_reproduced",
  "SEA location dimensions above 15 degrees 1, 1, 1, 1 (2 with the seed); PCs to 80% 4, 5, 2, 5 (reading "
  "a); participation ratio 4.0, 3.2, 2.3, 3.5; all below their ranges. With the SNR procedure fixed, SNR "
  "dimensionality 7, 2, 3 and 8 (the same under the five seeds), two of four in 4.5 to 13.2. Trial reading "
  "(b) gives 0 to 1 SEA dimensions and 2 to 5 PCs."),
o("suppfig6c-location-distinct-from-rotations", "reproduced",
  "Location-to-location alignment median 0.935 to 0.969 against location onto rotation planes 0.085 to "
  "0.664; median paired difference +0.28 to +0.88; p printed as 0 under both readings in every dataset."),
o("fig6b-location-predicts-rotations", "reproduced",
  "Methods version (6 folds, lambda 0.1) 73.3, 74.4, 81.6 and 74.1%, null 21.0, 14.7, 23.1 and 15.8%, "
  "signed-rank p at most 2.4e-13; the code's variant 75.5 to 86.5%. Four other seeds give 72.0 to 82.9%; "
  "trial reading (b) 70.9 to 80.9%."),
o("fig6c-location-tracks-direction", "partially_reproduced",
  "With PC 2 flipped, circular correlation of target angle with the location's angle in the PC 1-2 plane "
  "is 0.696 (p = 2e-07), 0.709 (6e-09), 0.245 (0.015) and 0.065 (0.55) for M1-J, PMd-J, M1-N and PMd-N; "
  "PMd-N fails in either orientation, also under trial reading (b) (0.053, p = 0.62)."),
o("fig6e-kinematics-predict-location", "reproduced",
  "Kinematic reading (a) (SVD basis), linear 55.5, 55.5, 70.5, 41.5% (in 33.3 to 78.1%); OU kernel 73.0, "
  "68.5, 88.7, 77.9% (in 62.1 to 89.1%); both above all 1000 permutations (p = 0.001). Reading (b) "
  "(skew-normal basis) gives linear 41.6 to 70.5% and OU 69.3 to 89.1%, also all in range. The Gaussian "
  "kernel (kernel reading b) gives 32.1 to 54.6%, below the range. Five seeds give OU 71.8 to 73.8 "
  "(M1-J), 65.5 to 69.1, 86.7 to 88.7 and 74.0 to 77.9%, all in range. OU length scales of 1e2 and 1e4 "
  "change the kernel values by at most 0.002, so the unpublished scale of the kinematic basis does not "
  "matter here.",
  extra=["The position basis functions are cumulative sums of unit-norm velocity vectors over 10 ms bins; "
         "this scale, which sets what the OU length scale of 10^3 means, is an assumption (the paper's "
         "kinFuncEval is not published). Length scales of 1e2 and 1e4 are shown."]),
o("fig7c-ldr-encoding", "reproduced",
  "SVD kinematic basis, linear 77.7, 69.0, 84.9, 73.6% (s.d. 5.8 to 19.1%), kernel 85.5, 86.3, 92.7, 87.8% "
  "(s.d. 2.6 to 7.7%); against the shuffled null, p at most 3.0e-08 (linear) and 2.0e-13 (kernel). "
  "Skew-normal basis within 0.006 of these. Five seeds give linear 67.3 to 70.4% for PMd-J and kernel "
  "84.8 to 92.7% overall, all in range. Kernel length scales of 1e2 and 1e4 change the kernel means by at "
  "most 0.002. Trial reading (b) gives linear 68.1 to 84.3% and kernel 84.0 to 92.1%.",
  extra=["The scale of the kinematic basis is an assumption (see fig6e); length scales of 1e2 and 1e4 are "
         "shown."]),
o("suppfig7a-not-memorization", "partially_reproduced",
  "Sextants held out, kernel against nearest neighbour, SVD basis, 76.5 against 68.4% (p = 1e-09), 68.8 "
  "against 60.2% (p = 0.024, kernel higher on 37 of 72 conditions), 86.5 against 78.3% (p = 3e-11), 78.0 "
  "against 69.5% (p = 5e-11); PMd-J misses p < 0.01, and under the skew-normal basis PMd-J gives p = 0.50. "
  "Kernel length scales of 1e2 and 1e4 give the same pattern; trial reading (b) gives PMd-J p = 0.019 and "
  "0.89.",
  extra=["The scale of the kinematic basis is an assumption (see fig6e); length scales of 1e2 and 1e4 are "
         "shown."]),
o("fig7c-standard-encoding-worse", "reproduced",
  "Both LDR models exceed every standard model with p < 0.001 in all 24 comparisons under both kinematic "
  "readings (p at most 2.5e-10). The linear multi-parameter model explains 52.1 to 54.4%, the OU kernel "
  "model on position (length scale 1e12) 39.8 to 52.2% and on velocity (1e11) 41.9 to 49.2%, against "
  "69.0 to 84.9% (linear LDR) and 85.5 to 92.7% (kernel LDR). With a kernel penalty of 0.1 (variant) the "
  "kernel models predict only the mean (0%). Trial reading (b) gives the same 24 of 24.",
  extra=["Velocity angle enters the linear model as its cosine and sine, and features are z-scored "
         "(assumption).",
         "The kernel models use no penalty (1e-8 for numerical stability), as the claims give for the LDR "
         "encoder's kernel; the Methods give none for these models (assumption). At length scales of 1e11 "
         "and 1e12 the kernel matrix differs from a matrix of ones by about 1e-10, so a penalty of 0.1, "
         "shown as a variant, reduces the fit to the training mean."]),
o("fig7f-ldr-decoding", "partially_reproduced",
  "Mean variance explained in single-trial hand position, SVD basis, 77.0, 74.4, 86.6 and 73.0% (medians "
  "84.8, 82.8, 91.7, 82.3%); M1-J and M1-N in 75.6 to 100%. Skew-normal basis 76.5, 73.7, 86.0 and 72.5%. "
  "Over the five seeds, M1-J 76.5 to 78.3, PMd-J 71.0 to 76.3, M1-N 86.6 to 89.2, PMd-N 71.8 to 75.9%; two "
  "or three datasets in range under each seed, so the outcome holds under all five. Trial reading (b) "
  "gives 77.4, 74.7, 87.4 and 73.4%, again two. The condition-shuffled null gives 2.5 to 4.0% (p below "
  "1e-250)."),
o("fig7f-decoder-beats-standard", "partially_reproduced",
  "Against 24 instantaneous decoders (ridge, lambda 1, on single trials; OU kernel, length scale 100, L2 "
  "0.1, on single trials or trial averages; rates in spikes/s smoothed at 20 or 100 ms, 100 ms lag; six "
  "per dataset), the LDR decoder is higher in every comparison with two-sided signed-rank p at most 3e-127, "
  "scored over the same window (-250 to +850 ms; LDR 73.8, 70.8, 84.7, 69.7%). The instantaneous decoders "
  "explain 0.0 to 74.7% (the best, M1-N kernel on single trials at 100 ms). On trials of their own "
  "training conditions they explain 0.0 to 86.9% (the trial-average kernel decoders 0.0 to 18.6%), so "
  "as configured they are weak decoders. Z-scored rates and a 6000-point training set (variants) give 0.4 "
  "to 78.0% and the same outcome, as does the LDR decoder under kinematic reading (b) and trial reading "
  "(b). The GPFA decoders were not run, so the claim holds against all but them, which the criterion "
  "counts as partial.",
  extra=["GPFA decoders not run; the paper gives neither latent dimensionality nor bin size, and fitting "
         "them was not attempted in the time available.",
         "Kernel decoders on single trials are trained on 3000 random time points of the training trials "
         "(the Methods say \"a subset\"; the size is an assumption; 6000 is shown). Rates enter in spikes/s "
         "as they are; the OU length scale of 100 is in those units, which the paper does not state. The "
         "100 ms smoothing is applied to 10 ms counts (s.d. 10 bins). Only position is decoded."]),
o("suppfig8-no-output-potent-dependence", "not_reproduced",
  "Removing the four-dimensional row space of the least-squares map from activity to hand position and "
  "velocity lowers the per-condition decoded variance from 76.4 to 70.8% (M1-J), 73.5 to 66.5, 87.5 to "
  "84.2 and 74.9 to 70.7% (SVD basis), drops of 3.3 to 7.0 points, lower without them on 70 to 72 of 72 "
  "conditions, and the two-sided signed-rank test gives p < 1e-12 in every dataset, below 0.036. Trial "
  "reading (b) gives drops of 3.9 to 6.3 points, p < 1e-12. The dataset holds no EMG, so the muscle "
  "dimensions could not be removed.",
  extra=["No EMG in the dataset; only kinematic dimensions are removed, as the criterion allows."]),
o("trial-curvature-decoding", "partially_reproduced",
  "Within-condition residuals of decoded and actual curvature parameters, SVD basis, rho 0.292 and 0.169 "
  "(M1-J), 0.238 and 0.102 (PMd-J), 0.446 and 0.464 (M1-N), 0.198 and 0.300 (PMd-N), all p below 0.001; "
  "6 of 8 in 0.144 to 0.451. Skew-normal basis 5 of 8 in range; trial reading (b) 6 of 8."),
]
assert len(out) == 34
rec["outcomes"] = out
F = rec["findings"]
F[0]["statement"] = ("The Nitschke file (sub-Nitschke_ses-20100923) joins five recording segments whose clocks "
  "overlap. Trial start times, hand timestamps and every unit's spike times jump backwards four times "
  "(segments span 5 to 6076 s, 6074 to 12077 s, 6071 to 12494 s, 6120 to 13516 s and 6074 to 6658 s), so "
  "spike times are not sorted and a trial's spikes cannot be selected by time alone; doing so mixes spikes "
  "of up to four segments. Splitting each unit's spikes at the jumps and assigning trials to segments in "
  "file order gives condition decoding of 0.44 to 0.50 in segments 0 to 2 and 0.18 in segment 3 (all "
  "successful trials; chance 0.014; 0.010 to 0.024 with the previous trial's labels).")
F[1]["statement"] = ("The units table holds 96 units per array, exactly one on each of the 192 electrodes, in "
  "both files. Its columns are electrode_group, electrodes, id, obs_intervals and spike_times, with no "
  "column for single or multi-unit, sorting quality or isolation. The paper reports 79 to 118 single and "
  "stable multi-units per array. Whether these units are threshold crossings or sorted units merged per "
  "electrode is not stated.")
F[5]["statement"] = ("In the Nitschke file, condition information in segment 3 is lower within the segment "
  "(decoding 0.179) than in segments 0 to 2 (0.445 to 0.495), while a decoder trained on the other "
  "segments reaches 0.491 on it, and decoding does not peak at another time offset. This is consistent "
  "with a change of the recorded units over the session; segment 4 (24 trials) is too small to check on "
  "its own.")
F[6]["statement"] = ("Questions for the paper's authors. (1) Which trials were analysed? All successful trials "
  "give 1595 (J) and 2121 (N), and successful trials with a delay above 400 ms 1381 and 1884, against 1469 "
  "and 2014 in the Figure 7 legend; the first was used here, and the second gives the same outcomes. (2) "
  "Which units were used, and are they in the dandiset? The files hold one unit per electrode with no "
  "single or multi-unit label. (3) What penalty was used for the OU kernel encoding models with length "
  "scales 1e11 and 1e12? With a penalty of 0.1 they predict only the mean; none was used here. (4) How "
  "were the noise excursion angles of Figure 4c computed? (5) Were the jPCA and single-condition LDS "
  "values of Supplementary Figure 3 cross-validated, and how? (6) Over what span were time bins shuffled "
  "in the control for data smoothing? (7) What scale do the kinematic basis functions (kinFuncEval) "
  "have, and in what units are rates given to the OU kernel decoders with length scale 100, and on how "
  "many points are they trained?")
rec["verifications"] = []  # filled below
yaml.safe_dump(rec, open(P, "w"), sort_keys=False, width=100, allow_unicode=True)
PYEOF
python $TMPDIR/rec/build.py && head -40 attempts/sabatini-2024-01.yaml
```

```
schema_version: 3
id: sabatini-2024-01
datasets:
- archive: dandi
  id: '000070'
  version: 0.260528.0919
  doi: 10.48324/dandi.000070/0.260528.0919
  relation: reuses
paper: doi:10.1038/s41467-024-51308-7
date: 2026-11-20
entry: sabatini-2024
provenance:
  kind: agent
  accountable:
    name: CatalystNeuro
  agent:
    harness: Claude Code
    model: claude-opus-5-5
    protocol: pilot-18
  runner:
[... 20 more lines not kept]
```

**Agent calls Bash**

```bash
cat > $TMPDIR/rec/ver.py <<'PYEOF'
import yaml
P = "attempts/sabatini-2024-01.yaml"
rec = yaml.safe_load(open(P))
for o in rec["outcomes"]:
    if o["claim"] == "data-composition":
        o["deviations"] = [o["deviations"][0], o["deviations"][2]]
R = []
def r(claim, agrees, outcome, reason, response):
    R.append({"claim": claim, "agrees": agrees, "outcome": outcome, "reason": reason, "response": response})
TR = ("Trials are now reading (a), all successful trials, with reading (b) run in a companion notebook "
      "(problem 5).")
r("data-composition", False, "reproduced",
  "Both monkeys have 72 conditions (36 straight, 36 curved). Trial counts are within tolerance under both "
  "readings (J 1595/1381, N 2121/1884), and each array has 96 units, inside 71-130 (cell 13). The units "
  "carry no single/multi-unit label, so all units are counted. Problem 6: the units-per-electrode check, "
  "np.bincount(np.arange(192)), always prints [1] and checks nothing; each array has exactly 96 units, equal "
  "to its electrode count, which suggests channel-level units rather than the paper's 79-118 sorted units; "
  "that is never examined, and it may underlie several mismatches in level.",
  "Outcome changed to reproduced, as the verifier reads the criterion: the dataset marks no unit as single "
  "or multi-unit, so all its units are counted, and 96 lies in 71 to 130. The check is fixed: the data "
  "check and this cell now print the units table's and electrodes table's columns and the number of units "
  "on each electrode (exactly one on each of the 192 in both files). That the units are per electrode is "
  "kept as a finding about the dataset. " + TR)
r("jpca-fit-r2", True, "partially_reproduced",
  "Under reading (a), straight (0.75-0.84) and curved (0.56-0.71) are all inside their ranges. For all "
  "conditions together, PMd-N's 0.452 falls outside 0.576-0.803, so 3 of 4 pass. The per-condition "
  "signed-rank test is significant only for M1-N, and it does not decide (cell 59). Problem 9: the "
  "straight/curved pairing assumes that maze m+1 is the curved version of straight maze m with the same "
  "target; targets are not compared.",
  "The pairing is now checked: in every dataset all 36 straight mazes are followed by a curved maze with "
  "the same target (target distance 0). " + TR + " Under reading (a) 3 of 4 again (PMd-N 0.446); outcome "
  "unchanged.")
r("jpca-variance-explained", True, "partially_reproduced",
  "Means are 8.9, 11.6, 11.7 and 5.1%; PMd-N falls below 6.3%. The s.d. is at most 11.6%, consistent with "
  "the paper's <13% (cell 61). Listed among the borderline claims to rerun under trial reading (a) (problem "
  "5).",
  TR + " Reading (a) gives 8.8, 10.9, 11.6 and 5.4%, PMd-N again below; outcome unchanged.")
r("single-lds-variance", True, "not_reproduced",
  "Means are 0.77-0.82 under reading (a) and 0.79-0.87 under (b). All four are above 0.726 under both "
  "readings (cell 32).",
  TR + " Reading (a) gives 78.1 to 82.9%; outcome unchanged.")
r("fig2c-condition-lds-variance", True, "reproduced",
  "Chosen k is 5, 5, 7, 5 (all in 5-9, the same under all five seeds). Mean variance explained is "
  "0.84-0.94, inside 63.9-100% (cell 15).",
  TR + " Reading (a) gives the same k and 85.3 to 94.6%; outcome unchanged.")
r("fig3a-eigenvalue-clusters", False, "not_reproduced",
  "Median pair frequencies are within 10% of the targets only for PMd-J (0.54, 1.53). M1-J (0.85, 2.35), "
  "M1-N (0.68, 1.74, 3.21) and PMd-N (0.73, 1.67) miss (cell 17). Section C: the fig3g and fig3a frequency "
  "shift (0.7/1.8/3.1 Hz against 0.5/1.5/2.5) comes from the data or the window, not from de-mixing; "
  "frequencies under a different fitting window, or on reading-(a) trials, would separate those causes.",
  "Outcome changed to not reproduced: the criterion needs every dataset, and the partial outcome given "
  "before rested on the clusters, which the criterion does not grade. " + TR + " Under reading (a) no "
  "dataset has all its pairs within 10% (PMd-J 0.56 and 1.55 Hz). The frequencies of the factorization "
  "under other windows are now printed (see fig3g).")
r("fig3c-eigenvalue-distance-auc", True, "not_reproduced",
  "AUC under the Poisson null: 0.81, 0.71, 0.63, 0.70. Under the half-split null: 0.70, 0.64, 0.66, 0.68. "
  "At most one dataset is inside 0.459-0.638 under either null, and the result is stable across seeds "
  "(cell 20). Problem 8: the Poisson null simulates from already-smoothed rates at 10 ms and smooths "
  "again, which lowers the noise, and uses 100 repeats, not 500; the half-split null fails as well, so the "
  "outcome stands.",
  TR + " Reading (a) gives 0.636 to 0.813, with only M1-N under the Poisson null in range. The double "
  "smoothing of the Poisson null is now stated in the notebook and the deviation; the repeats stay at 100 "
  "for time, as the half-split null gives the same outcome. Outcome unchanged.")
r("suppfig2-eigenvalues-from-kinematics", True, "not_reproduced",
  "Pooled mean R2 is 0.275 under both kinematic readings, against 0.1 +- 0.05 (cell 74).",
  TR + " Reading (a) gives 0.285; outcome unchanged.")
r("fig3g-basis-frequencies", False, "not_reproduced",
  "PMd-J has only 2 rotation pairs. The frequencies (0.64-0.74, 1.54-1.82, 2.71-3.23 Hz) sit "
  "systematically above 0.5/1.5/2.5 Hz; the 0.5 Hz rotation misses in all four datasets (cell 22). Section "
  "C: frequencies under a different fitting window, or on reading-(a) trials, would separate whether the "
  "shift comes from the data or the window.",
  "Outcome changed to not reproduced: PMd-J has two pairs where the criterion asks for three or four in "
  "every dataset, and 3 of 11 frequencies are within 10%. The cell now prints the frequencies of the "
  "factorization fitted over -350 to +850 ms (0.55 to 0.71, 1.37 to 1.70, 2.52 to 2.96 Hz) and over 0 to "
  "+850 ms (0.61 to 0.67, 1.56 to 1.91, 2.76 to 3.16 Hz): the window moves them, and the whole window "
  "brings them nearer the paper's. " + TR + " Reading (a) gives the same pattern.")
r("tbf-variance-explained", True, "reproduced",
  "Means are 0.935, 0.936, 0.966, 0.953 under reading (a) and 0.92-0.96 under (b), all inside 81-100% "
  "(cell 24).",
  TR + " Trial reading (a) gives 94.1 to 96.9%; outcome unchanged.")
r("tbf-shuffle-control", True, "partially_reproduced",
  "Shuffled means are 42.2, 28.7, 41.8 and 42.1%; PMd-J falls below 31.5%. The rank-sum test gives p = "
  "3.9e-25 with real data higher on 72/72 conditions in every dataset (cell 27). Problem 12: the time "
  "shuffle permutes bins over -500 to +1001 ms, an assumption that sets the shuffled level; PMd-J's 28.7% is "
  "near the bound.",
  "The span of the shuffle is now stated as an assumption in the helper, the notebook and the deviation, "
  "with the direction in which a longer or shorter span would move the value; another span was not run. "
  + TR + " Reading (a) gives PMd-J 28.7% again; outcome unchanged.")
r("fig3h-recoverability", True, "partially_reproduced",
  "Real recoverability is 0.973-0.986 with rank-sum p < 0.001. The paper states chance as 63-80%. The "
  "notebook's chance is 0.896, 0.860, 0.890, 0.896, so 3 of 4 exceed the widened bound of 88% (cell 28). "
  "Problem 4: real recoverability uses the de-mixed basis and chance the raw SVD basis of the shuffled "
  "data; variance explained in B is not invariant to the non-orthogonal de-mixing, so chance is not "
  "measured the same way as the real value.",
  "Chance now de-mixes the shuffled basis as the real one is, with the raw basis as a variant. The two "
  "agree to three decimals (89.5, 86.5, 89.1, 89.6% under reading a), so the high chance level is not due "
  "to the basis. " + TR + " Outcome unchanged.")
r("fig3i-duration-warping", True, "not_reproduced",
  "Unwarped M1-N is rho +0.235 (paper -0.26). Under the main (truncating) warp, only M1-J (-0.514) lies in "
  "-0.693 to -0.468; under the 250 ms post-reach warp, none do (cell 30).",
  TR + " Reading (a) gives M1-N unwarped +0.204 and, warped, only M1-J (-0.550) in range; outcome "
  "unchanged.")
r("suppfig3-model-comparison", True, "not_reproduced",
  "Under the main reading, cross-validated TBF (0.71-0.87) is below the in-sample single-condition LDS "
  "(0.84-0.94) in every dataset. The all-in-sample variant passes in every dataset (cell 63). Problem 11 "
  "(claims-file reading, reported only): the main reading compares held-out TBF variance against in-sample "
  "LDS and jPCA values, so the outcome flips between readings.",
  "Added as a question for a reader in questions/sabatini-2024.yaml, citing the Supplementary Figure 3 "
  "legend; the claim is tested as the claims file has it. " + TR + " Outcome unchanged.")
r("fig4b-plane-alignment", True, "reproduced",
  "All 11 rotation AUCs are 0.861-0.958 with observed alignment lower. Signed-rank p = 1.7e-13 with "
  "observed lower on 72/72 conditions (cell 36).",
  TR + " Reading (a) gives 0.876 to 0.961; outcome unchanged.")
r("fig4c-subspace-excursion-angles", True, "partially_reproduced",
  "Counts above 45 degrees are 5, 13, 11, 7, 14, 3, 9, 11, 7, 18, 25; 8 of 11 are inside 5.4-22. The "
  "second part (more dimensions above chance than above 45 degrees) fails for most rotations, but it rests "
  "on the notebook's own chance definition. Problem 3: the chance level is the author's own, the 95th "
  "percentile of the largest principal angle between half-split planes of a single condition; that is "
  "neither the claims file's fraction of noise SEA above the data nor a like-for-like comparison with "
  "excursion angles to a growing union.",
  "Chance is now a noise SEA: SEA run on the 72 half-split estimates of a single condition's plane, which "
  "differ only by noise, for 24 conditions per rotation, and a data dimension is above chance when fewer "
  "than 5% of these curves reach its angle. This compares like with like and follows the claims file's "
  "\"fraction of noise SEA above the data\"; it remains an assumption about the code's control. All 25 "
  "dimensions are above chance for every rotation, more than the count above 45 degrees for 10 of 11. The "
  "earlier threshold is a variant. " + TR + " Counts under reading (a) are 3 to 25, 8 of 11 in range; "
  "outcome unchanged.")
r("rotation-orientation-dimensionality", True, "not_reproduced",
  "PCs to 80% are 2-23 and participation ratio is 1.7-18.7, against 20.7-44 and 15-40.5; under both PCA "
  "inputs only one rotation falls inside each range. The SNR dimensions hit the 96 ceiling for two "
  "rotations because of a bug (cell 44). Problem 2: PCA runs on mean-centred loadings, but the bottleneck "
  "is applied to uncentred loadings, so the direction shared across conditions is only restored at full "
  "rank; on synthetic data with 4 true dimensions the procedure returns 72 of 72, with uncentred PCA 4. The "
  "SNR values are unusable.",
  "Fixed: the PCA of the SNR procedure is no longer mean-centred, so the bottleneck spans the loadings "
  "(Methods, \"PCA on the dimensions occupied by these rotations\"). The SNR dimensionality is now 9 to 21 "
  "for all 11 rotations, in range, and stable across seeds. PCs and participation ratio still fail. "
  + TR + " Outcome unchanged.")
r("fig4d-jpca-variance-correlation", True, "not_reproduced",
  "Per-dataset mean rho is 0.33, 0.93, 0.65, 0.68; the significant planes have 0.63-0.93. Neither reading "
  "falls in 0.351-0.506, and 5 of 6 planes (83%) are significant, not 66 +- 6.6% (cell 66).",
  TR + " Reading (a) gives means 0.315, 0.930, 0.648, 0.719 and 5 of 6 significant; outcome unchanged.")
r("fig4f-plane-alignment-explains-jpca", True, "partially_reproduced",
  "rho is 0.94, 0.93, 0.83, 0.69, 0.82, 0.82, all with p < 0.001. M1-N plane 1 (0.689) is below 0.738, so 5 "
  "of 6 pass (cell 67).",
  TR + " Reading (a) gives M1-N plane 1 0.668, again 5 of 6; outcome unchanged.")
r("fig5a-frequencies-segregated", False, "reproduced",
  "Under reading (a), all 20 comparisons have p < 0.001 with mean same-minus-different positive. For M1-N "
  "rot2 the same-frequency median is lower and fewer than half of the pairs favour same, so \"higher\" "
  "rests on the mean (cell 48; B10). Problem 10: signed-rank p values are two-sided with no direction "
  "printed.",
  "Outcome changed to reproduced. The cell now prints the median paired difference, the Hodges-Lehmann "
  "estimate (the location estimate that goes with the signed-rank test) and the one-sided p. For all 20 "
  "comparisons the one-sided test gives p at most 1.4e-12 and the Hodges-Lehmann estimate is positive, so "
  "same-frequency alignment is higher by the paper's test; for M1-N 3.24 Hz the effect is small (estimates "
  "+0.025 and +0.024, median paired difference +0.002 and -0.004), which the notes say. " + TR)
r("fig5c-rotations-predict-rotations", True, "reproduced",
  "Pair means are 0.41-0.95, inside 38.7-100%. Every pair beats its null with signed-rank p at most "
  "2.4e-12, stable across seeds (cell 52). Problem 10: no direction printed.",
  "The median paired difference and the one-sided p are now printed; every pair is positive. " + TR +
  " Reading (a) gives 44.7 to 95.0%; outcome unchanged.")
r("suppfig6a-location-alignment", True, "partially_reproduced",
  "AUCs are 0.883, 0.748, 0.870, 0.945; PMd-J falls below 0.792. p < 1e-12 with observed lower (cell 38).",
  TR + " Reading (a) gives PMd-J 0.784, still below; outcome unchanged.")
r("suppfig6b-location-dimensionality", True, "not_reproduced",
  "SEA dimensions above 15 degrees are 0-1 (1-2 counting the seed), against 3.6-5.5. PCs are 2-5 against "
  "18.9-33, and participation ratio is 1.9-4.3 against 13.6-29. SNR is 72 in all four datasets, the "
  "ceiling, because of the B2 bug (cell 45).",
  "With the SNR fix (see rotation-orientation-dimensionality) the location's SNR dimensionality is 7, 2, 3 "
  "and 8, two of four in range. SEA, PCs and participation ratio still fail. " + TR + " Outcome "
  "unchanged.")
r("suppfig6c-location-distinct-from-rotations", True, "reproduced",
  "Location-to-location median is 0.93-0.97 against 0.08-0.67 onto rotations, p about 0 under both "
  "readings in every dataset (cell 49).",
  "The median paired difference and one-sided p are now printed. " + TR + " Outcome unchanged.")
r("fig6b-location-predicts-rotations", True, "reproduced",
  "Means are 0.709, 0.723, 0.809, 0.716 (inside 60.3-88%), with signed-rank p < 1e-12 against the null. "
  "The code variant also passes (cell 53).",
  TR + " Reading (a) gives 73.3 to 81.6%; outcome unchanged.")
r("fig6c-location-tracks-direction", True, "partially_reproduced",
  "After flipping PC 2, the circular correlation is 0.61, 0.70 and 0.25 (all p < 0.05) for three datasets. "
  "PMd-N has 0.05, p = 0.62 (cell 55).",
  TR + " Reading (a) gives PMd-N 0.065, p = 0.55; outcome unchanged.")
r("fig6e-kinematics-predict-location", True, "reproduced",
  "Under kinematic reading (a), linear is 0.53, 0.55, 0.70, 0.41 (inside 33.3-78.1%) and the OU kernel is "
  "0.70, 0.69, 0.89, 0.77 (inside 62.1-89.1%). Both beat all 1000 permutations. The Gaussian kernel reading "
  "fails (cell 72). Problem 12: in ldr.kin_basis, Bp = cumsum(Bv) fixes the scale of the reach parameters, "
  "and with it the effective OU length scale (10^3) in fig6e, fig7c and suppfig7a; this is not stated as an "
  "assumption.",
  "The scale is now stated as an assumption in the helper and the deviations, and the kernel is also run "
  "with length scales of 1e2 and 1e4; the values change by at most 0.002. " + TR + " Outcome unchanged.")
r("fig7c-ldr-encoding", True, "reproduced",
  "Linear is 0.68-0.84 (inside 54-85.8%) and kernel 0.84-0.92 (inside 63.9-95.7%), with p at most 2.6e-8 "
  "against the nulls, under both kinematic readings (cell 77).",
  "Kernel length scales of 1e2 and 1e4 are now shown (problem 12); the means change by at most 0.002. "
  + TR + " Outcome unchanged.")
r("suppfig7a-not-memorization", True, "partially_reproduced",
  "Kernel beats nearest neighbour at p < 1e-9 in three datasets. PMd-J has p = 0.019 under reading (a) "
  "and 0.89 under (b) (cell 78).",
  "One-sided p and the length-scale variants are now printed. " + TR + " Reading (a) gives PMd-J p = "
  "0.024 (0.50 with the skew-normal basis); outcome unchanged.")
r("fig7c-standard-encoding-worse", False, "partially_reproduced",
  "Both LDR models beat the linear standard model (0.52-0.53) at p < 1e-9. Both kernel standard models "
  "return exactly 0.000 in every dataset, so 16 of the 24 comparisons test nothing (cell 81). Problem 1: "
  "the kernel penalty of 0.1 is the author's assumption; with length scales of 1e12 or 1e11 the kernel "
  "matrix is all ones to within about 1e-10, so the fit returns the training mean; on a synthetic test a "
  "penalty of 0.1 gives R2 = -0.001 and 1e-8 gives 0.86; the 1e12 scale only makes sense with a near-zero "
  "penalty, as for the LDR encoder.",
  "Fixed as the verifier suggests: the kernel models now use no penalty (1e-8), as the LDR encoder's "
  "kernel does, with 0.1 as a variant. They now explain 39.8 to 52.2% (position) and 41.9 to 49.2% "
  "(velocity), and both LDR models beat all three standard models in all 24 comparisons (p at most "
  "2.5e-10), so every comparison is informative. The outcome stays reproduced, now on all 24 "
  "comparisons. " + TR)
r("fig7f-ldr-decoding", True, "partially_reproduced",
  "Mean variance explained is 0.774, 0.747, 0.874, 0.734 under reading (a). PMd-J and PMd-N fall below "
  "0.756, so 2 of 4 pass; reading (b) gives the same pattern (cell 84). Problem 5: only trial reading (b) "
  "is analysed, and fig7f PMd-J 0.747 against 0.756 sits at the range edge.",
  TR + " Trial reading (a) gives 77.0, 74.4, 86.6 and 73.0%, again two of four, and two or three under "
  "each of the five seeds; outcome unchanged.")
r("fig7f-decoder-beats-standard", True, "partially_reproduced",
  "LDR wins with p < 1e-180 in 24/24 comparisons against the non-GPFA decoders. The GPFA decoders were not "
  "run, which the criterion scores as partial (cell 89). Problem 7: rates are z-scored before the OU "
  "decoder (length scale 100), which the paper does not do and which changes the effective length scale; "
  "the 3000-point training subset is an assumption; the instantaneous decoders are scored over -250 to "
  "+850 ms while LDR is scored over -350 to +850 ms; only kinematic reading (a) is run; the very low "
  "baselines are never sanity-checked. Section C: their in-sample variance explained and their variance "
  "explained on trials of training conditions would show whether they are sound; the GPFA decoders could "
  "be run from the spike trains on the archive.",
  "Rates now enter in spikes/s without z-scoring (z-scored is a variant); a 6000-point training set is "
  "shown; LDR is scored over the same -250 to +850 ms window; the comparison is run against LDR under both "
  "kinematic readings; and each decoder's variance explained on trials of its training conditions is "
  "printed. The decoders are weak even there (0.0 to 86.9%; the trial-average kernel decoders 0.0 to "
  "18.6%), which the notes say. LDR still wins all 24 comparisons (p at most 3e-127). The GPFA decoders "
  "were not run in this revision either, so the outcome stays partial. " + TR)
r("suppfig8-no-output-potent-dependence", True, "not_reproduced",
  "Removing the kinematic-potent dimensions drops variance explained by 3.9-6.3 percentage points, with p "
  "< 0.001 in all datasets, against the threshold of p >= 0.036 (cell 86). Archive metadata for both assets "
  "lists Position, Units, ElectricalSeries, with no EMG, so the EMG part cannot be tested. Problem 10: no "
  "direction printed.",
  "The median drop, the count of conditions lower without the dimensions and the one-sided p are now "
  "printed. " + TR + " Reading (a) gives drops of 3.3 to 7.0 points; outcome unchanged.")
r("trial-curvature-decoding", True, "partially_reproduced",
  "Under reading (a), 6 of 8 correlations are inside 0.144-0.451; PMd-J parameter 4 (0.093) and M1-N "
  "parameter 4 (0.548) fall outside. All have p < 0.001. Reading (b) gives 5 of 8 (cell 85).",
  TR + " Trial reading (a) gives 6 of 8 again (PMd-J parameter 4 0.102, M1-N parameter 4 0.464); outcome "
  "unchanged.")
assert len(R) == 34 and [x["claim"] for x in R] == [o["claim"] for o in rec["outcomes"]]
rec["verifications"] = [{
  "date": "2026-11-20", "kind": "agent",
  "by": "Independent agent run by CatalystNeuro (same harness, separate context, did not write the notebook)",
  "reviewed": ("Round 1. The executed notebook with the conclusion cells and the summary removed, the helper "
               "module and the claims file, with the paper under paper/. The verifier read the archive's "
               "asset metadata and tested helpers on synthetic inputs (the kernel fit at length scale 1e12, "
               "the SNR bottleneck, the de-mixing helper). It had no attempt record. The revision answers "
               "each point; problems not tied to one claim: problem 5 (trial reading (a) never run; the "
               "stated reason for reading (b) false for monkey N) is answered by adopting reading (a), for "
               "the reason the Methods give, and running reading (b) in a companion notebook, with the same "
               "outcome for every claim. Section C asks for the jPCA port's R2 on the codepack's example "
               "data; this was not done, as the codepack's data are outside the dataset and not pinned."),
  "results": R}]
yaml.safe_dump(rec, open(P, "w"), sort_keys=False, width=100, allow_unicode=True)
print("ok")
PYEOF
cd  && python $TMPDIR/rec/ver.py && python tools/entry.py check entries/sabatini-2024 2>&1 | tail -20
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
python - <<'EOF'
import yaml
P="attempts/sabatini-2024-01.yaml"
rec=yaml.safe_load(open(P))
v=rec["verifications"][0]
v["reviewed"]=("Round 1. The executed notebook with the conclusion cells and the summary removed, the helper "
  "module and the claims file, with the paper under paper/. The verifier read the archive's asset metadata "
  "and tested helpers on synthetic inputs (the kernel fit at a length scale of 1e12, the SNR bottleneck, the "
  "de-mixing helper). It had no attempt record.")
yaml.safe_dump(rec, open(P,"w"), sort_keys=False, width=100, allow_unicode=True)
EOF
python tools/entry.py check entries/sabatini-2024 2>&1 | tail -3; git status --short; date -u
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
timeout 300 python tools/entry.py run entries/sabatini-2024 2>&1 | tail -4; git diff --stat
```

```
pass  reproduce_sabatini_2024.ipynb  (1276 s, reused)
pass  reproduce_sabatini_2024_trials_b.ipynb  (718 s, reused)
reused the executed copies of 2026-11-20 15:48 UTC: nothing the run reads has changed since (hash fb31ee4dd800). Nothing was executed and no environment was built; --fresh runs it again.
 attempts/sabatini-2024-01.yaml                     | 1236 ++++++++++++++++----
 entries/sabatini-2024/README.md                    |   12 +-
 entries/sabatini-2024/entry.yaml                   |    5 +-
 entries/sabatini-2024/ldr.py                       |   20 +-
 .../sabatini-2024/reproduce_sabatini_2024.ipynb    |  457 +++++---
 5 files changed, 1304 insertions(+), 426 deletions(-)
```

**Agent**

I've revised the entry for every point in the round-1 report. `python tools/entry.py all entries/sabatini-2024` passed, and both notebooks ran: 1276 s for the main one and 718 s for the reading (b) one. `entry.py check` reports 0 errors. Nothing is committed.

**Outcomes:** 11 reproduced, 12 partially reproduced, 11 not reproduced, none blocked. Four changed, all to the verifier's outcome:
- **data-composition**: partially reproduced → reproduced. The dataset labels no unit as single or multi-unit, so all 96 per array count. That they are one per electrode stays a finding.
- **fig3a-eigenvalue-clusters**: partially → not reproduced. The criterion needs every dataset; no dataset has all its eigenvalue pairs within 10% of the paper's frequencies.
- **fig3g-basis-frequencies**: partially → not reproduced. PMd-J has 2 rotation pairs where 3 or 4 are required, and 3 of 11 frequencies are within 10%.
- **fig5a-frequencies-segregated**: partially → reproduced. The one-sided signed-rank tests give p ≤ 1.4e-12 and a positive Hodges-Lehmann estimate (the signed-rank test's estimate of the paired difference) for all 20 comparisons. For M1-N 3.24 Hz the effect is small, and the notes say so.
- **fig7c-standard-encoding-worse** stays reproduced, against the verifier's partial. Its problem is fixed: the kernel encoders now explain 40–52% instead of 0, and the LDR models beat all 24 standard models (p ≤ 2.5e-10).

All five disagreements are recorded under `verifications`.

**Fixes:**
- **Trials (B5):** the analyses now use reading (a), all successful trials. My earlier reason for reading (b) was wrong for monkey N; the new one is that the Methods describe a 0–1000 ms delay and name no exclusion. This is recorded as an assumption. A companion notebook, `reproduce_sabatini_2024_trials_b.ipynb`, runs every analysis under reading (b), and every outcome is the same under both.
- **SNR dimensionality (B2):** the PCA is no longer mean-centred. Rotations now give 9–21 dimensions, all in range; the location gives 7, 2, 3 and 8, two of four in range. Both outcomes stay not reproduced, since PCs and participation ratio still fail.
- **fig4c chance (B3):** it is now a noise SEA run on the half-split estimates of single conditions. This remains an assumption about the paper's code.
- **Recoverability chance (B4):** the shuffled basis is now de-mixed like the real one. The value is unchanged to three decimals.
- **Units (B6):** the check now prints the units table columns and confirms exactly one unit on each of the 192 electrodes in both files.
- **Instantaneous decoders (B7):** rates are no longer z-scored (z-scored is a variant, as is a 6000-point training set). LDR is scored over the same −250 to +850 ms window, and the comparison runs under both kinematic readings. A new check shows the decoders are weak even on trials of their own training conditions (0 to 87%), which the notes now say.
- **Other outputs added:** the jPCA straight/curved pairing check (same target in all 36 pairs), the direction of each signed-rank test, kernel length scales of 1e2 and 1e4 (changes of at most 0.002), and factorization frequencies over other time windows. The whole −350 to +850 ms window brings them closer to the paper's.
- **Stated as assumptions:** the time-shuffle span and the scale of the kinematic basis.
- **Question for a reader:** the suppfig3 comparison of a held-out value against in-sample values is now a question in `questions/sabatini-2024.yaml`, citing the Supplementary Figure 3 legend.
- **Findings:** updated to the new numbers, with three more questions for the paper's authors.

**Not done:**
- **GPFA decoders:** not run, as the paper gives neither the latent dimensionality nor the bin size, so fig7f-decoder-beats-standard stays partial.
- **Eigenvalue null:** still 100 repeats instead of 500, for time. The half-split null gives the same outcome.
- **jPCA check on the codepack's example data:** not done, because that data is outside the dataset and not pinned.
- **Shuffle span:** the alternative spans were not run.

## End of run

66 turns, 81 minutes, $6.84 at API prices, result: success.
