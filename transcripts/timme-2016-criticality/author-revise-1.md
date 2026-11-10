# timme-2016-criticality · author-revise-1 · run 42716863239

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
date -u; ls entries/timme-2016-criticality transcripts/timme-2016-criticality; cat transcripts/timme-2016-criticality/verifier-1-report.md
```

```
Mon Nov  9 23:08:28 UTC 2026
entries/timme-2016-criticality:
README.md
complexity_culture.ipynb
culture_criticality.ipynb
entry.yaml
hc8.py
models.ipynb
models.py
requirements.in
requirements.lock.txt

transcripts/timme-2016-criticality:
answer-report.md
answer.md
author-answers-report.md
author-answers.md
author-report.md
author-revise-1.md
author.md
[... 74 more lines not kept]
```

**Agent calls Bash**

```bash
wc -l docs/protocol.md; grep -n "^#" docs/protocol.md
```

```
647 docs/protocol.md
1:# Protocol for an attempt
43:## Reader
45:### 1. Get the paper
59:### 2. Read the paper's code
69:### 3. Write the claims file
159:### 4. Data from outside the paper's own recordings
167:### 5. Check
180:### 6. Answer questions
193:## Author
209:### 1. Establish what can be tested
339:### 2. Check the data against its description
354:### 3. Write the entry
422:### 4. Lock, check and run
433:### 5. Record the attempt
495:### 6. Hand over for verification
533:## Repeat attempts
575:## Local and remote datasets
598:## Verifier
602:### Round 1: without the author's conclusions
[... 2 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 1,42p docs/protocol.md; sed -n 193,340p docs/protocol.md
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
[... 169 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 340,647p docs/protocol.md
```

```
Descriptive metadata is often wrong. For every quantity the analysis uses,
check the description against the values: units and ranges, sampling rates,
counts of subjects, sessions, trials and cells, the size of an arena, which
conditions exist. Show that every data stream shares the clock of the trial
tables, using a contrast between conditions where an overall check cannot
tell a response from an offset (with spikes and a trial table only, decoding
a task variable in windows around the trial start does this; for continuous
sessions, decoding the annotations with the labels shifted in time), and name any
session where this could not be established. A description that a check
supports but does not prove is reported as consistent with the data, not as
shown. Where they disagree, trust the data, say so in the notebook,
and record it as a finding.

### 3. Write the entry

An entry is a directory `entries/<paper>/` holding
`entry.yaml`, `requirements.in`, one or more notebooks, and usually a helper
module.

- **Stream the data** from the archive, at a pinned version of the dataset
[... 287 more lines not kept]
```

**Agent calls Bash**

```bash
ls attempts | grep timme; cat entries/timme-2016-criticality/entry.yaml; cat entries/timme-2016-criticality/README.md; wc -l entries/timme-2016-criticality/*.py; ls executed/timme-2016-criticality 2>/dev/null; tail -50 transcripts/timme-2016-criticality/author-report.md
```

```
timme-2016-criticality-01.yaml
schema_version: 1
name: timme-2016-criticality
type: reproduction
title: Criticality and complexity in rat hippocampal cultures (Timme et al. 2016)
description: Tests the findings of Timme, Marshall, Bennett, Ripp, Lautzenhiser and Beggs (2016) on
  CRCNS data set hc-8, the spike-sorted spontaneous activity of 435 recordings from 28 dissociated
  hippocampal cultures. It recomputes the avalanche statistics, critical exponents with and without
  sub-sampling, branching ratios, susceptibility, shape collapse curvature and neural complexity, and
  their changes under five kinds of randomization, with a Python port of the NCC toolbox the paper
  used. A third notebook runs the paper's chain, Bethe lattice and cortical branching models.
license: Apache-2.0
notebooks:
- path: culture_criticality.ipynb
  title: Avalanches, exponents, branching ratio and randomizations in the culture recordings
  runtime_minutes: 46
- path: complexity_culture.ipynb
  title: Complexity of the culture recordings and of their randomizations
  runtime_minutes: 32
- path: models.ipynb
[... 93 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/timme-2016-criticality; grep -n "^def \|^N_\|^[A-Z_]* =" hc8.py models.py; grep -n "def complexity" -A120 hc8.py | head -200
```

```
hc8.py:51:BUCKET = "https://crcnsarchive.s3-us-west-2.amazonaws.com/hc-8/live"
hc8.py:52:ZIP_URL = f"{BUCKET}/Data.zip"
hc8.py:53:DATASET_ID = "hc-8"
hc8.py:54:DATASET_VERSION = "unversioned"  # CRCNS data sets carry no versions (docs/archives.md); the MD5 pins the zip
hc8.py:56:BIN_MS = 0.05            # data description: spike times in 0.05 ms bins
hc8.py:57:ANALYSIS_MIN = 59.0      # Methods 2.2: first 59 min of each recording
hc8.py:58:ANALYSIS_BINS = int(round(ANALYSIS_MIN * 60e3 / BIN_MS))
hc8.py:60:MIN_VALUE = 4            # Methods 2.7: sizes or durations less than 4 removed
hc8.py:61:MIN_COUNT = 20           # Methods 2.7: values seen fewer than 20 times removed
hc8.py:62:N_SURROGATES = 500       # Methods 2.7
hc8.py:63:P_CRIT = 0.2             # Methods 2.7
hc8.py:64:BR_DELAYS = np.arange(1, 9)      # Methods 2.11: 1 <= k <= 8
hc8.py:65:BR_ACT_MAX_CULTURE = 10          # Methods 2.11: 0 <= A(t) <= 10 for the culture data
hc8.py:66:BR_ACT_MAX_MODEL = 5             # Methods 2.11: 0 <= A(t) <= 5 for the cortical branching model
hc8.py:73:def _zip():
hc8.py:78:def recording_names() -> list[str]:
hc8.py:84:def culture_div(name: str) -> tuple[int, int]:
hc8.py:89:def load(name: str, zf: zipfile.ZipFile | None = None) -> dict:
hc8.py:101:def open_zip() -> zipfile.ZipFile:
hc8.py:109:def first_window(spikes: list[np.ndarray], nbins: int = ANALYSIS_BINS) -> list[np.ndarray]:
[... 231 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/timme-2016-criticality; sed -n 355,421p hc8.py
```

```
S = np.exp((1 - best) * logT)[:, None] * interp
    coeffs = np.polyfit(grid, S.mean(axis=0), 2)
    return float(best), float(2 * coeffs[0])


# ----------------------------------------------------------------------------------------------
# Complexity (complexity.m)

def _states(raster_bins: list[np.ndarray], bins: np.ndarray):
    """Unique network states over the given bins: a sparse (n_unique x n_neurons) matrix and the
    count of each state."""
    n = len(raster_bins)
    pos = {}
    index = np.full(bins.max() + 2 if bins.size else 1, -1, dtype=np.int64)
    index[bins] = np.arange(bins.size)
    rows, cols = [], []
    for j, s in enumerate(raster_bins):
        r = index[s[s < index.size]]
        r = r[r >= 0]
        rows.append(r)
[... 45 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/timme-2016-criticality; python - <<'EOF'
import json
for nb in ["complexity_culture.ipynb","models.ipynb"]:
    d=json.load(open(nb))
    print("=====",nb)
    for i,c in enumerate(d["cells"]):
        print(f"--- cell {i} [{c['cell_type']}] tags={c['metadata'].get('tags')}")
        print("".join(c["source"])[:3000])
EOF
```

```
<persisted-output>
Output too large (33.6KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/f9353a9b-0706-49f2-a067-8a2e9e56a7e8/tool-results/b1oy8dwhp.txt

Preview (first 2KB):
===== complexity_culture.ipynb
--- cell 0 [markdown] tags=None
# Timme et al. (2016) on CRCNS hc-8: complexity of the culture recordings

Paper: Timme et al. (2016), Front. Physiol. 7:425, doi:10.3389/fphys.2016.00425; claims file
`claims/crcns-hc-8/10.3389-fphys.2016.00425.yaml` (version of record, PMC5037237, with the
supplement). Dataset: CRCNS hc-8, doi:10.6080/K0PC308P, `hc-8/live/Data.zip` (MD5
`bd4e2a8685df3e55e1a3c04fbe09d9ce` in the data set's `checksums.md5`), version `unversioned`: CRCNS
data sets carry no versions and this is the only published copy (see `culture_criticality.ipynb`).

Complexity (Methods 2.9, `complexity.m` of the NCC toolbox): on the avalanche bins of the rebinned
first 59 min, with the sub-sampling correction (the integration curve of data whose neurons are
each permuted in time is subtracted, and the curve is cut at the first peak of I(k)/(k-1)). It uses
100 random subsets per subset size, as Methods 2.9 give, and runs on 40 of the 435 recordings drawn
with a fixed seed, to fit the time limit of a notebook. A first version used 10 subsets on 180
recordings; the verifier found the cut unstable at 10 subsets, and the spread of the estimate over
[... 25 more lines not kept]
```

**Agent calls Bash**

```bash
cd  git log --oneline -8 -- entries/timme-2016-criticality attempts/timme-2016-criticality-01.yaml transcripts/timme-2016-criticality; git status --short entries attempts questions; tail -40 transcripts/timme-2016-criticality/author-revise-1.md; ls -la transcripts/timme-2016-criticality
```

````
d49c320d0f Paper-first names (the cutover, docs/paper-first.md)
```
/opt/hostedtoolcache/Python/3.13.18/x64/lib/python3.13/site-packages/nbformat/validator.py:434: DuplicateCellId: Non-unique cell id 'cebc6b1c' detected. Corrected to 'b01e93d0'.
  _validate(nbdict, ref, version, version_minor, relax_add_props)
/opt/hostedtoolcache/Python/3.13.18/x64/lib/python3.13/site-packages/nbformat/validator.py:434: DuplicateCellId: Non-unique cell id '345e3060' detected. Corrected to 'd94f8be3'.
  _validate(nbdict, ref, version, version_minor, relax_add_props)
0 error(s)
Mon Nov  9 13:33:37 UTC 2026
```

**Agent**

Duplicate cell ids from copying cells; I'll give the new cells fresh ids, then start the full run.

**Agent calls Bash**

```bash
cd entries/crcns-hc-8-timme-2016; $TMPDIR/dev/bin/python - <<'EOF'
import json, uuid
for f in ("models.ipynb","complexity_culture.ipynb","culture_criticality.ipynb"):
[... 37 more lines not kept]
````

**Agent calls Bash**

```bash
cd  grep -n -A6 "^\*\*Agent\*\*" transcripts/timme-2016-criticality/author-revise-1.md | grep -v "^--$" | cut -c1-600 | head -300
```

````
305:**Agent**
306-
307-The dev environment is ready. Next I profile the complexity estimator on one recording to see what 100 subsets per size would cost.
308-
309-**Agent calls Bash**
310-
311-```bash
476:**Agent**
477-
478-Values match the old code exactly. A first finding: on this recording, 100 subsets still keep only 12 of 90 sizes after the cut, so more subsets may not move the cut much. Now I'll profile the speed.
479-
480-**Agent calls Bash**
481-
482-```bash
618:**Agent**
619-
620-The Bethe raster is cheap: 3 s per call at 100 subsets. Across seeds the cut complexity is 0.0016 to 0.0030 and keeps 14 to 24 of 245 sizes. Next I read the claims for the affected items.
621-
622-**Agent calls Bash**
623-
[... 57 more lines not kept]
````

**Agent calls Read**

```json
{
 "file_path": "transcripts/timme-2016-criticality/author-revise-1.md",
 "offset": 300,
 "limit": 580
}
```

````
300	                [str(python), "-m", "ipykernel", "install", "--prefix", str(venv), "--name", kernel]):
301	        if subprocess.run(cmd).returncode != 0:
302	[... 22 more lines not kept]
303	```
304	
305	**Agent**
306	
307	The dev environment is ready. Next I profile the complexity estimator on one recording to see what 100 subsets per size would cost.
308	
309	**Agent calls Bash**
310	
311	```bash
312	cd entries/crcns-hc-8-timme-2016; $TMPDIR/dev/bin/python - <<'EOF'
313	import json
314	for nb in ["complexity_culture.ipynb","models.ipynb"]:
315	    d=json.load(open(nb))
316	    print("=====",nb, len(d["cells"]))
317	    for i,c in enumerate(d["cells"]):
318	        print(f"--- cell {i} [{c['cell_type']}] tags={c.get('metadata',{}).get('tags')}")
319	        print("".join(c["source"])[:2500])
[... 560 more lines not kept]
````

**Agent calls Read**

```json
{
 "file_path": "transcripts/timme-2016-criticality/author-revise-1.md",
 "offset": 878,
 "limit": 560
}
```

```
878	cd entries/crcns-hc-8-timme-2016; $TMPDIR/dev/bin/python - <<'EOF'
879	import json, copy
880	f="complexity_culture.ipynb"
881	d=json.load(open(f))
882	C=d["cells"]
883	def setsrc(c, s): c["source"]=s.splitlines(keepends=True)
884	s="".join(C[0]["source"])
885	s=s.replace("""The
886	paper uses up to 100 random subsets per subset size; this notebook uses 10, to fit the time limit
887	of 8 conditions), and runs on 180 of the 435 recordings drawn with a fixed seed.""","""It uses
888	100 random subsets per subset size, as Methods 2.9 give, and runs on 40 of the 435 recordings drawn
889	with a fixed seed, to fit the time limit of a notebook. A first version used 10 subsets on 180
890	recordings; the verifier found the cut unstable at 10 subsets, and the spread of the estimate over
891	repeated draws is shown below at 10 and 100 subsets.""")
892	setsrc(C[0], s)
893	s="".join(C[1]["source"])
894	s=s.replace('N_SUBSETS = 10        # Methods 2.9 give up to 100; 10 to fit the time limit (a deviation)',
895	            'N_SUBSETS = 100       # Methods 2.9: "the lesser of either all possible permutations of neurons or 100"')
896	s=s.replace("""# 180 of the 435 recordings, drawn with a fixed seed: all 435 would take about 68 min with 4
897	# processes (37 s per recording in development), over the 60 min limit of a notebook
[... 540 more lines not kept]
```

**Agent calls Bash**

```bash
cd  git diff HEAD --stat -- entries attempts questions; wc -l attempts/timme-2016-criticality-01.yaml; grep -n "verifications\|^  - id:\|outcome:\|^[a-z_]*:" attempts/timme-2016-criticality-01.yaml | head -80; ls questions | grep timme; grep -n "N_SUBSETS\|N_RECORDINGS\|N_DRAWS\|GRID" entries/timme-2016-criticality/*.ipynb | head
```

```
341 attempts/timme-2016-criticality-01.yaml
1:schema_version: 3
2:id: timme-2016-criticality-01
3:datasets:
9:paper: doi:10.3389/fphys.2016.00425
10:date: 2026-11-09
11:entry: timme-2016-criticality
12:provenance:
23:inputs:
30:outcomes:
32:  outcome: reproduced
46:  outcome: reproduced
57:  outcome: not_reproduced
66:  outcome: reproduced
85:  outcome: blocked
93:  outcome: reproduced
102:  outcome: reproduced
111:  outcome: reproduced
119:  outcome: reproduced
128:  outcome: reproduced
[... 29 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n "argv\|argparse\|add_argument\|def cmd_run\|def run\b\|parallel\|Pool\|executed/" tools/entry.py | head -30; nproc; free -g | head -2
```

```
28:go to --output-dir (default: executed/<name>/, which git ignores). A notebook
35:executed/<name>/handover/. Run the entry first.
43:import argparse
463:def run(entry_dir: Path, output_dir: Path, timeout: int, max_minutes: float) -> int:
549:    parser = argparse.ArgumentParser(description=__doc__,
550:                                     formatter_class=argparse.RawDescriptionHelpFormatter)
551:    parser.add_argument("command", choices=["lock", "check", "run", "all", "handover", "upgrade-python"])
552:    parser.add_argument("entry", type=Path, nargs="+",
554:    parser.add_argument("--output-dir", type=Path, help="where executed notebooks go")
555:    parser.add_argument("--timeout", type=int, default=3600, help="seconds allowed per cell")
556:    parser.add_argument("--max-minutes", type=float, default=60,
558:    parser.add_argument("--python", help="lock: the Python version to lock for (default: the entry's); "
560:    parser.add_argument("--before", type=Path, help="upgrade-python: the executed notebooks to compare with "
561:                                                    "(default: executed/<entry>)")
4
               total        used        free      shared  buff/cache   available
Mem:              15           1          12           0           2          14
```

**Agent calls Bash**

```bash
cd  sed -n 463,548p tools/entry.py
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
[... 66 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -c "import pandas as pd" entries/timme-2016-criticality/culture_criticality.ipynb; python tools/entry.py check entries/timme-2016-criticality 2>&1 | tail -3; date -u
```

```
1
0 error(s)
Mon Nov  9 23:09:45 UTC 2026
```

**Agent calls Bash**

```bash
cd  date -u; python tools/entry.py all entries/timme-2016-criticality 2>&1 | tail -15; date -u
```

```
Mon Nov  9 23:09:50 UTC 2026
Installed kernelspec registry-timme-2016-criticality in executed/timme-2016-criticality/.venv/share/jupyter/kernels/registry-timme-2016-criticality
0 error(s)
pass  culture_criticality.ipynb  (2512 s)
pass  complexity_culture.ipynb  (2258 s)
pass  models.ipynb  (682 s)
Tue Nov 10 00:40:52 UTC 2026
```

**Agent**

All three notebooks passed (42, 38 and 11 min). Now reading the new outputs.

**Agent calls Bash**

```bash
cd  python - <<'EOF'
import json
for nb in ["complexity_culture.ipynb","models.ipynb"]:
    d=json.load(open(f"executed/timme-2016-criticality/{nb}"))
    print("=====",nb)
    for i,c in enumerate(d["cells"]):
        if c["cell_type"]=="markdown":
            print(f"--- md {i}:", "".join(c["source"])[:200].replace("\n"," ")); continue
        print(f"--- code {i} tags={c['metadata'].get('tags')}")
        for o in c["outputs"]:
            if o.get("output_type")=="stream": print("".join(o["text"])[-6000:])
            elif o.get("output_type")=="error": print("ERR", o["evalue"])
EOF
```

```
===== complexity_culture.ipynb
--- md 0: # Timme et al. (2016) on CRCNS hc-8: complexity of the culture recordings  Paper: Timme et al. (2016), Front. Physiol. 7:425, doi:10.3389/fphys.2016.00425; claims file `claims/crcns-hc-8/10.3389-fphys
--- code 1 tags=None
40 recordings in 34.2 min; peak memory of this process 0.21 GB

--- code 2 tags=['sanity']
recordings: 40 | cultures: 21 | neurons analysed: 3610
avalanche bins per recording (real): 43097 to 812127
real       complexity (bits/neuron) median 0.00223, range 0.00011 to 0.07550; subset sizes kept by the cut: median 10 of 90; NaN 0
jitter1    complexity (bits/neuron) median 0.00164, range 0.00006 to 0.06823; subset sizes kept by the cut: median 10 of 90; NaN 0
jitter10   complexity (bits/neuron) median 0.00084, range 0.00002 to 0.07706; subset sizes kept by the cut: median 10 of 90; NaN 0
jitter100  complexity (bits/neuron) median 0.00036, range 0.00000 to 0.10385; subset sizes kept by the cut: median 10 of 90; NaN 0
wrap       complexity (bits/neuron) median 0.00037, range 0.00002 to 0.00250; subset sizes kept by the cut: median 10 of 90; NaN 0
poisson    complexity (bits/neuron) median 0.00031, range 0.00002 to 0.00419; subset sizes kept by the cut: median 10 of 90; NaN 0
swap       complexity (bits/neuron) median 0.00265, range 0.00001 to 0.16197; subset sizes kept by the cut: median 13 of 90; NaN 0
shuffle    complexity (bits/neuron) median 0.17576, range 0.00540 to 0.30930; subset sizes kept by the cut: median 74 of 90; NaN 0
neurons left without a spike by shuffling (dropped): 0 recordings
recordings kept under exclusion reading (a): 40 of 40

--- md 3: ## Spread of the estimate over repeated draws  The verifier of the first version asked how much the toolbox's complexity (correction and cut) varies with the random draws (the subsets and the time per
[... 281 more lines not kept]
```

**Agent calls Bash**

```bash
cd  ls claims | grep -i timme; f=$(ls claims/timme-2016*.yaml 2>/dev/null || ls claims/*/*fphys*); echo $f; python - "$f" <<'EOF'
import yaml,sys
d=yaml.safe_load(open(sys.argv[1]))
for c in d["claims"]:
    if c["id"] in ("fig10a-complexity-randomization","figs8-complexity-susceptibility-correlation","figs9-complexity-fit-range-correlation","fig12a-swap-preserves-complexity","fig12b-shuffle-lowers-complexity","fig5f-network-state-poisson-keeps-complexity","fig7ab-cb-complexity-susceptibility-peak","fig7d-cb-branching-ratio-near-1","fig2e-avalanche-count"):
        print(c["id"], "| depends:", c.get("depends_on"), "| expected:", c.get("expected"))
        print("  CRIT:", c["criterion"]); print()
EOF
```

```
Exit code 1
timme-2016-criticality.yaml
timme-2016.yaml
claims/timme-2016-criticality.yaml claims/timme-2016.yaml
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
FileNotFoundError: [Errno 2] No such file or directory: 'claims/timme-2016-criticality.yaml\nclaims/timme-2016.yaml'
```

**Agent calls Bash**

```bash
cd  head -5 claims/timme-2016.yaml; python - claims/timme-2016-criticality.yaml <<'EOF'
import yaml,sys
d=yaml.safe_load(open(sys.argv[1]))
for c in d["claims"]:
    if c["id"] in ("fig10a-complexity-randomization","figs8-complexity-susceptibility-correlation","figs9-complexity-fit-range-correlation","fig12a-swap-preserves-complexity","fig12b-shuffle-lowers-complexity","fig5f-network-state-poisson-keeps-complexity","fig7ab-cb-complexity-susceptibility-peak","fig7d-cb-branching-ratio-near-1","fig2e-avalanche-count","fig5d-bethe-small-avalanches","fig5e-shuffle-removes-complexity"):
        print(c["id"], "| depends:", c.get("depends_on"), "| expected:", c.get("expected"))
        print("  CRIT:", c["criterion"]); print()
EOF
```

```
# Claims for Timme, Ito, Myroshnychenko, Nigam, Shimono, Yeh, Hottowy, Litke & Beggs (2016),
# "High-Degree Neurons Feed Cortical Computations", PLoS Comput Biol 12(5), e1004858, on CRCNS ssc-3.
# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"), 2026-11-06,
# protocol as stated in docs/protocol.md (version pilot-13), Reader steps 1 to 4.
#
fig5d-bethe-small-avalanches | depends: None | expected: None
  CRIT: A simulation, not a test on recorded data. Bethe lattice of Methods 2.4 (two outgoing connections per neuron, p_trans = 0.5, activity stopped at layer 10^4, one neuron active in the first layer per run), as in the toolbox's bethelattice.m. The number of runs is not stated; a standard choice of 10^4 runs is used and cannot change the direction of the result. Small avalanches are those that stop on or before layer 8; each run is one time series of network states over the neurons of layers 1 to 8. Reproduced when the size distribution of the small avalanches is accepted as a truncated power law by plparams (p at least 0.2) and their complexity (toolbox complexity, sub-sampling correction on) is above zero.

fig5e-shuffle-removes-complexity | depends: ['fig5d-bethe-small-avalanches'] | expected: None
  CRIT: A simulation, not a test on recorded data. Neuron shuffling as in Methods 2.5 (at each time bin the active count kept and the identities drawn uniformly over all neurons). Reproduced when the shuffled size distribution equals the original and the complexity falls to below 10% of the original value ("removed" read as near zero; 10% is a choice the paper does not make).

fig5f-network-state-poisson-keeps-complexity | depends: ['fig5d-bethe-small-avalanches'] | expected: None
  CRIT: A simulation, not a test on recorded data. Whole network states (one per time bin) placed at random times, as Methods 2.5, paragraph 4, last sentence. Complexity depends only on the distribution of states (Methods 2.9), so it is preserved exactly whe
[... 24 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python - <<'EOF'
import json
d=json.load(open("executed/timme-2016-criticality/culture_criticality.ipynb"))
for i,c in enumerate(d["cells"]):
    if "claim:fig2e-avalanche-count" in (c["metadata"].get("tags") or []):
        for o in c["outputs"]:
            if o.get("output_type")=="stream": print("".join(o["text"]))
for nb in ["complexity_culture.ipynb","models.ipynb","culture_criticality.ipynb"]:
    d=json.load(open(f"entries/timme-2016-criticality/{nb}"))
    for i,c in enumerate(d["cells"]):
        s="".join(c["source"])
        if c["cell_type"]=="markdown" and (s.startswith("**Result") or s.startswith("## Summary")) and (nb!="culture_criticality.ipynb" or "fig2e" in s or "Summary" in s or "avalanches per recording" in s):
            print(f"==== {nb} cell {i}\n{s}\n")
EOF
```

```
avalanches per recording (first 59 min, rebinned to the network ISI): (a) median 83289; (b) Terrell-Scott mode 81707 (10 bins); expected 10000 +/- 1000
range 2250 to 531966; 5th to 95th percentile 22187 to 192127
recordings with 9000 to 11000 avalanches: 2
by culture (median): {1: 53259, 2: 168892, 3: 76779, 4: 81115, 5: 59985, 6: 50268, 7: 87077, 8: 58274, 9: 63236, 10: 121442, 11: 66787, 12: 74549, 13: 64995, 14: 59490, 15: 90804, 16: 98738, 17: 94171, 18: 78209, 19: 102420, 20: 94425, 21: 194086, 22: 93222, 23: 52133, 24: 81925, 25: 61474, 26: 66837, 27: 104243, 28: 56187}
log10 avalanches per recording, histogram (bins of 0.25 decades):
3.00-3.25      0
3.25-3.50      1
3.50-3.75      2
3.75-4.00      2
4.00-4.25      9
4.25-4.50     30
4.50-4.75     79
4.75-5.00    148
5.00-5.25    135
5.25-5.50     26
5.50-5.75      3
5.75-6.00      0
recordings with 10^3.5 to 10^4.5 avalanches (within half a decade of 10,000): 43; median log10 4.92

==== complexity_culture.ipynb cell 7
[... 112 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python - claims/timme-2016-criticality.yaml <<'EOF'
import yaml,sys
d=yaml.safe_load(open(sys.argv[1]))
for c in d["claims"]:
    if c["id"] in ("figs2-recording-length","fig7a-complexity-boundary-rise"):
        print(c["id"], c.get("depends_on"), c.get("expected")); print("  CRIT:", c["criterion"]); print()
EOF
sed -n 1,60p attempts/timme-2016-criticality-01.yaml
```

```
fig7a-complexity-boundary-rise ['fig7ab-cb-complexity-susceptibility-peak'] None
  CRIT: A simulation, not a test on recorded data. With the analysis of fig7ab-cb-complexity-susceptibility-peak, reproduced when the mean complexity at the largest p_trans tested is above that at the next lower p_trans and above the minimum between the main peak and 0.3.

figs2-recording-length None [{'quantity': 'p_trans at the primary complexity peak, all time bins', 'value': 0.28, 'tolerance': 0.028}]
  CRIT: A simulation, not a test on recorded data. 30 models per p_trans run for 3 x 10^4, 10^5 and 3 x 10^5 steps; complexity on all time bins (Figure S2 legend). The p_trans grid as the readings of fig7ab-cb-complexity-susceptibility-peak. Open whether the sub-sampling extrapolation was applied (the supplement says the analysis was identical to the main text apart from the time bins); readings (a) extrapolated, (b) whole 100-neuron system. Reproduced when the mean complexity at the primary peak increases with recording length, the primary peak lies within tolerance of 0.28, and the ratio of the value at p_trans 0.3 to the primary peak value decreases with recording length.

schema_version: 3
id: timme-2016-criticality-01
datasets:
- archive: crcns
  id: hc-8
  version: unversioned
  doi: 10.6080/K0PC308P
  relation: primary
paper: doi:10.3389/fphys.2016.00425
date: 2026-11-09
entry: timme-2016-criticality
provenance:
  kind: agent
  accountable:
[... 46 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 60,341p attempts/timme-2016-criticality-01.yaml
```

```
measured: 83289
  notes: After rebinning the first 59 min to the mean network ISI, the median number of avalanches
    per recording is 83289 (reading a) and the histogram mode 81707 (reading b), against 10000 +/-
    1000; the range is 2250 to 531966 and only 2 of 435 recordings have 9000 to 11000. How the paper
    counted avalanches for Figure 2E is asked of the authors (findings).
- claim: fig8-subsampling-exponents
  outcome: reproduced
  notebook: culture_criticality.ipynb
  output: claim:fig8-subsampling-exponents
  notes: Over 435 recordings, the full-system search gives tau 2.491 +/- 0.623 and alpha 2.928 +/-
    0.648; sub-sampling with each sub-sample rebinned to its own ISI gives tau 2.106 +/- 0.407 and
    alpha 2.730 +/- 0.579, lower means and lower SDs. 1/sigma nu z changes by 3.6% (size given
    duration, 1.411 to 1.360) and 1.6% (shape collapse, 1.467 to 1.490). Keeping the full system's
    bin for the sub-samples gives tau 1.745 +/- 0.465, alpha 2.356 +/- 0.504 and changes of 1.9% and
    3.4%, the same conclusion. On one recording run with layout (b), the extrapolated values differ
    from layout (a) by at most 0.044. One recording has no accepted duration fit.
  deviations:
  - Methods 2.10 do not say whether a sub-sample is rebinned to its own network ISI; the main
    reading rebins it ("These analyses were identical to those performed in the whole recorded
    system", Methods 2.10), and keeping the full system's bin is shown. Both give the same outcome.
[... 262 more lines not kept]
```

**Agent calls Bash**

```bash
cd  ls schemas 2>/dev/null; grep -l "verifications:" attempts/*.yaml | head -3; f=$(grep -l "verifications:" attempts/*.yaml | head -1); sed -n "$(grep -n '^verifications:' $f | cut -d: -f1),+45p" $f
```

```
attempt.schema.json
claims.schema.json
entry.schema.json
paper-match.schema.json
attempts/amjad-2025-01.yaml
attempts/armstrong-2026-01.yaml
attempts/ashworth-2025-01.yaml
verifications:
- date: '2026-10-15'
  kind: agent
  by: Independent agent run by CatalystNeuro (same harness, separate context, did not write the notebook)
  reviewed: The first executed notebook with the conclusion cells and the summary removed, the helper
    module and the claims file, with the paper's full text (PMC12183687). The verifier read the
    archive's file list and metadata through the DANDI API and tested the helpers on synthetic inputs
    (beta_power, burst_onsets, window_mean, codes_per_trial, rereference, fscv_window_mean, best_lag,
    reward_blocks). It had no attempt record and took the claims from the claims file.
  results:
  - claim: insertion-yield
    agrees: true
    outcome: blocked
[... 33 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python -c "
import json;s=json.load(open('schemas/attempt.schema.json'))
import pprint
def find(o,k):
    if isinstance(o,dict):
        for kk,v in o.items():
            if kk==k: pprint.pprint(v, width=150); return True
            if find(v,k): return True
    if isinstance(o,list):
        for v in o:
            if find(v,k): return True
find(s,'verifications')
" | head -60
```

```
{'items': {'additionalProperties': False,
           'properties': {'by': {'type': 'string'},
                          'date': {'format': 'date', 'type': 'string'},
                          'kind': {'enum': ['agent', 'person', 'paper_author']},
                          'results': {'items': {'additionalProperties': False,
                                                'properties': {'agrees': {'type': 'boolean'},
                                                               'claim': {'type': 'string'},
                                                               'outcome': {'description': 'The outcome the verifier would give.',
                                                                           'enum': ['reproduced',
                                                                                    'partially_reproduced',
                                                                                    'not_reproduced',
                                                                                    'blocked']},
                                                               'reason': {'description': "The verifier's reason, in its own words.",
                                                                          'type': 'string'},
                                                               'response': {'description': 'What the author changed or replied, kept apart from the '
                                                                                           "verifier's reason.",
                                                                            'type': 'string'}},
                                                'required': ['claim', 'agrees'],
                                                'type': 'object'},
                                      'type': 'array'},
[... 4 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat > $TMPDIR/concl.py <<'EOF'
import json
E = "entries/timme-2016-criticality/"
X = "executed/timme-2016-criticality/"
cells = {
"complexity_culture.ipynb": {
7: "**Result: not reproduced.** Over 40 recordings with 100 subsets per size, the toolbox's complexity (correction and cut) has median 0.00223 bits/neuron in the real data. 10-bin and 100-bin jitter, wrap and Poisson lower it with Benjamini-Hochberg corrected p from 0.0372 to 1.16e-06, and Poisson and 100-bin jitter give the two largest decreases. 1-bin jitter lowers the median to 0.00164 without significance (corrected p 0.836), and shuffling raises it to 0.176 (corrected p 2.85e-13), against the claim; under Benjamini-Yekutieli three of the six are significant. The cut keeps a median of 10 of 90 subset sizes for the real data and 74 for shuffled data. Without the cut shuffling lowers complexity too, but 1-bin and 10-bin jitter are not significant (corrected p 0.43 and 0.303); without the correction shuffling raises it.",
10: "**Result: not reproduced.** Over 40 recordings, the Pearson correlation of the toolbox's complexity with the susceptibility is 0.902 with Eq. 14 and 0.905 with N var(A/N) (Spearman 0.724 and 0.745): positive, as stated, but far outside 0.23 +/- 0.023. Without the cut it is -0.605 and -0.592, and without the correction 0.267 and 0.446.",
13: "**Result: not reproduced.** Over 40 recordings, the Pearson correlations of the toolbox's complexity with the size and duration fit ranges are 0.060 (p 0.72) and -0.107 (p 0.51), against 0.296 and 0.197. Without the cut they are 0.052 and 0.276, and without the correction 0.369 and 0.038; no variant matches both.",
16: "**Result: reproduced.** By the paper's rank sum test, spike swapping does not change the toolbox's complexity significantly (median 0.00223 against 0.00265, corrected p 0.836), and real and swapped complexity correlate with Pearson r 0.775, above the 0.7 reading of strong (Spearman 0.533, below it). The median per-recording relative change is -0.089. Both variants agree: without the cut p 0.927 and r 0.989, without the correction p 0.958 and r 0.998. The test uses 40 recordings, and the cut complexity of one recording has a median coefficient of variation of 0.78 over repeated draws at 100 subsets (spread section above), so r passes the 0.7 reading by 0.075.",
19: "**Result: not reproduced.** With the toolbox's complexity, real complexity exceeds shuffled complexity in none of the 40 recordings (median change +0.174, corrected p 2.85e-13) and Pearson r is 0.431. Without the cut the claim holds: real exceeds shuffled in all 40 recordings, corrected p 2.97e-07, r 0.902. Without the correction real is never greater.",
20: """## Summary

| claim | outcome |
|---|---|
| fig10a-complexity-randomization | not reproduced |
| figs8-complexity-susceptibility-correlation | not reproduced |
| figs9-complexity-fit-range-correlation | not reproduced |
| fig12a-swap-preserves-complexity | reproduced |
| fig12b-shuffle-lowers-complexity | not reproduced |

Differences from the paper's method: 40 of the 435 recordings, drawn with a fixed seed. The 100
subsets per size of Methods 2.9 took 34.2 min for 40 recordings with 4 processes, so all 435 would
exceed the 60 min limit of a notebook. The first version used 10 subsets on 180 recordings.

With 100 subsets the toolbox's cut at the first peak of I(k)/(k-1) still falls early: it keeps a
median of 10 of 90 subset sizes in the real data and 74 in shuffled data. Over three draws on 10
recordings the cut complexity has a median coefficient of variation of 0.78 at 100 subsets and 0.86
at 10, and the cut keeps a median of 8 and 7 sizes. Shuffling then raises complexity, against
Figures 10A and 12B, and without the cut it lowers it in every recording. Spike swapping leaves
complexity unchanged under every variant, as the paper says.

A failure to reproduce here may be a failure of this attempt, not of the paper: see the reasoning and the differences from the paper's method.""",
},
"models.ipynb": {
8: "**Result: reproduced.** 7018 of 10000 runs end by layer 8. Their sizes after the cuts are accepted as a truncated power law (tau 1.593, sizes 4 to 12, p 0.338). Their complexity with 100 subsets per size is 0.00300 bits/neuron (24 of 245 sizes kept by the cut); 5 repeated draws give 0.00073 to 0.00335, above zero in all 5 and above the 0.00000 of the shuffled data (fig5e). The full model's sizes are also accepted (tau 1.402, p 0.368).",
11: "**Result: reproduced.** Shuffling leaves A(t), and so the size distribution, unchanged, and lowers the complexity from 0.00300 to 0.00000, a ratio of 0.000; over repeated draws the largest shuffled value is 0.003 of the smallest original one. Without the cut the complexity falls from 0.26451 to -0.05185; without the correction it rises from 0.37416 to 0.41433.",
14: "**Result: not reproduced.** Permuting the network states changes the size distribution (tau 2.222 against 1.593 +/- 0.058), but the toolbox's complexity changes from 0.00300 to 0.00345, a relative difference of 0.151, and 0.105 between the means of 5 repeated draws, against the criterion of 5%. The original's own draws differ from their mean by up to 0.675, so with the cut the estimator's spread is larger than the 5% the criterion allows for it. Without the cut the difference is 0.013 (0.004 between the means) and without the correction 0.001, both within 5%.",
23: "**Result: not reproduced.** The extrapolated susceptibility, averaged over 30 models per p_trans on the 0.01 grid, rises at every step from 0.2 to 0.3 under both readings of Eq. 14 and has no interior maximum, so it does not peak within 0.0265 of 0.265; the whole 100-neuron system has no interior maximum either. The complexity half was not computed (too large, see above) and cannot change the outcome.",
26: "**Result: not reproduced.** The mean B_new is closest to 1 at p_trans 0.28 (1.0052), but the susceptibility of fig7ab has no interior maximum to compare it with, so the criterion fails. 0.28 is within 0.0265 of the paper's 0.265. For reference, the one-step ratio is 0.9373 at p_trans 0.25, where 4 p_trans is 1, and the mean avalanche size rises from 16.1 at 0.25 to 110.9 at 0.28 and 2276.6 at 0.30.",
27: """## Summary

| claim | outcome |
|---|---|
| fig3-chain-model-complexity | reproduced |
| fig5d-bethe-small-avalanches | reproduced |
| fig5e-shuffle-removes-complexity | reproduced |
| fig5f-network-state-poisson-keeps-complexity | not reproduced |
| fig6-cb-distribution-curvature | partially reproduced |
| fig7c-cb-curvature-no-peak | not reproduced |
| fig7ab-cb-complexity-susceptibility-peak | not reproduced (susceptibility half) |
| fig7a-complexity-boundary-rise | blocked, too_large |
| figs2-recording-length | blocked, too_large |
| fig7d-cb-branching-ratio-near-1 | not reproduced |

Differences from the paper's method: the p_trans grid of 0.01 only (reading b), as 0.005 would
double the simulation time; curvature of the distributions as a quadratic term, a measure the paper
does not define; the complexity of the sub-sampled cortical branching models not computed. In this
port of the cortical branching model the mean B_new is closest to 1 at p_trans 0.28, the one-step
ratio is 0.9373 at 0.25, and the susceptibility rises to the end of the grid. These are simulations,
so they say nothing about the dataset.

A failure to reproduce here may be a failure of this attempt, not of the paper: see the reasoning and the differences from the paper's method.""",
},
"culture_criticality.ipynb": {
13: "**Result: not reproduced.** After rebinning the first 59 min to the network ISI, the median number of avalanches per recording is 83289 and the histogram mode 81707, about eight times the stated 10,000; only 2 of 435 recordings have 9000 to 11000 avalanches. On a log scale the median is 10^4.92, and 43 of 435 recordings lie within half a decade of 10^4, so the count does not hold as an order of magnitude either.",
},
}
for nb, edits in cells.items():
    for base in (E, X):
        d = json.load(open(base + nb))
        for i, text in edits.items():
            c = d["cells"][i]
            old = "".join(c["source"])
            assert c["cell_type"] == "markdown" and (old.startswith("**Result") or old.startswith("## Summary")), (nb, i, old[:50])
            c["source"] = text.splitlines(keepends=True)
        json.dump(d, open(base + nb, "w"), indent=1, ensure_ascii=False)
        open(base + nb, "a").write("\n")
print("ok")
EOF
python $TMPDIR/concl.py; git diff --stat entries/
```

```
ok
 .../complexity_culture.ipynb                       | 29 +++++++++++++---------
 .../culture_criticality.ipynb                      |  2 +-
 entries/timme-2016-criticality/models.ipynb        | 26 ++++++++++---------
 3 files changed, 32 insertions(+), 25 deletions(-)
```

**Agent calls Bash**

```bash
cd entries/timme-2016-criticality; python - <<'EOF'
s=open("entry.yaml").read()
s=s.replace("runtime_minutes: 46","runtime_minutes: 42").replace("runtime_minutes: 32","runtime_minutes: 38").replace("runtime_minutes: 12","runtime_minutes: 11")
open("entry.yaml","w").write(s)
r=open("README.md").read()
r=r.replace("(all 435 recordings, about 46 min with 4 processes)","(all 435 recordings, about 42 min with 4 processes)")
r=r.replace("neural complexity of the real and randomized data (180 recordings,\n  about 32 min)","neural complexity of the real and randomized data (40 recordings,\n  100 subsets per size, about 38 min)")
r=r.replace("the cortical branching model (about 12 min)","the cortical branching model (about 11 min)")
old=r[r.index("The counts of recordings"):r.index("A failure to reproduce")]
new="""The counts of recordings and neurons match the paper exactly, and the exponents, branching ratios,
susceptibility, curvature and fit ranges behave as the paper reports, with some exceptions under
the weakest randomization. The number of avalanches per recording is about eight times the stated
10,000. The complexity results depend on the toolbox's cut of the integration curve, which keeps
about a tenth of the subset sizes in the real data even with the paper's 100 subsets per size:
with it, shuffling raises complexity, against the paper, while spike swapping leaves it unchanged,
as the paper says. In the cortical branching model the susceptibility rises to the end of the
p_trans range with no peak. Two model claims are blocked for time.

"""
r=r.replace(old,new)
open("README.md","w").write(r)
EOF
grep -n "40 recordings\|42 min\|11 min\|Two model" README.md; grep runtime entry.yaml
```

```
12:  they change under randomization (all 435 recordings, about 42 min with 4 processes).
13:- `complexity_culture.ipynb`: neural complexity of the real and randomized data (40 recordings,
15:- `models.ipynb`: the chain model, the Bethe lattice and the cortical branching model (about 11 min).
27:p_trans range with no peak. Two model claims are blocked for time.
  runtime_minutes: 42
  runtime_minutes: 38
  runtime_minutes: 11
```

**Agent calls Bash**

```bash
date -u
```

```
Tue Nov 10 00:43:30 UTC 2026
```

**Agent calls Bash**

```bash
cd  cat > $TMPDIR/rec.py <<'PYEOF'
p = "attempts/timme-2016-criticality-01.yaml"
s = open(p).read()

def swap(start, end, new):
    global s
    i = s.index(start); j = s.index(end, i)
    s = s[:i] + new + s[j:]

swap("- claim: fig10a-complexity-randomization", "- claim: fig3-chain-model-complexity", """- claim: fig10a-complexity-randomization
  outcome: not_reproduced
  notebook: complexity_culture.ipynb
  output: claim:fig10a-complexity-randomization
  notes: Over 40 recordings with 100 subsets per size, the toolbox's complexity (correction and cut)
    has median 0.00223 bits/neuron in the real data. 10-bin and 100-bin jitter, wrap and Poisson
    lower it with Benjamini-Hochberg corrected p from 0.0372 to 1.16e-06, and Poisson and 100-bin
    jitter give the two largest decreases. 1-bin jitter lowers the median to 0.00164 without
    significance (corrected p 0.836), and shuffling raises it to 0.176 (corrected p 2.85e-13),
    against the claim; under Benjamini-Yekutieli three of the six are significant. The cut keeps a
    median of 10 of 90 subset sizes for the real data and 74 for shuffled data. Without the cut
    shuffling lowers complexity too, but 1-bin and 10-bin jitter are not significant (corrected p
    0.43 and 0.303); without the correction shuffling raises it. The first version, with 10 subsets
    on 180 recordings, gave the same pattern (five of six lower, shuffling raises it 74-fold) and
    was recorded as partially reproduced; a 78-fold rise under shuffling contradicts the claim, so
    the outcome is now not reproduced, as the verifier gave it.
  deviations:
  - 40 of the 435 recordings, drawn with a fixed seed. With the 100 subsets per size of Methods 2.9
    the 40 recordings took 34.2 min with 4 processes, so all 435 would exceed the 60 min limit of a
    notebook. The first version used 10 subsets on 180 recordings.
- claim: figs8-complexity-susceptibility-correlation
  outcome: not_reproduced
  notebook: complexity_culture.ipynb
  output: claim:figs8-complexity-susceptibility-correlation
  measured: 0.902
  notes: Pearson r between the toolbox's complexity and the susceptibility over 40 recordings is
    0.902 with Eq. 14 as printed and 0.905 with N var(A/N) (Spearman 0.724 and 0.745), against 0.23
    +/- 0.023; the correlation is positive, as stated, but much larger. Without the cut it is -0.605
    and -0.592, without the correction 0.267 and 0.446.
  deviations:
  - As for fig10a-complexity-randomization, 40 recordings.
- claim: figs9-complexity-fit-range-correlation
  outcome: not_reproduced
  notebook: complexity_culture.ipynb
  output: claim:figs9-complexity-fit-range-correlation
  measured:
  - 0.06
  - -0.107
  notes: Over 40 recordings, Pearson r of the toolbox's complexity with the size fit range is 0.060
    (p 0.72) and with the duration fit range -0.107 (p 0.51), against 0.296 and 0.197. Without the
    cut they are 0.052 and 0.276, without the correction 0.369 and 0.038; no variant matches both.
  deviations:
  - As for fig10a-complexity-randomization, 40 recordings.
- claim: fig12a-swap-preserves-complexity
  outcome: reproduced
  notebook: complexity_culture.ipynb
  output: claim:fig12a-swap-preserves-complexity
  notes: By the paper's rank sum test, spike swapping does not change the toolbox's complexity
    significantly over 40 recordings (median 0.00223 against 0.00265, relative +0.189; corrected p
    0.836 BH, 1 BY), and real and swapped complexity correlate with Pearson r 0.775, above the 0.7
    reading of strong (Spearman 0.533, below it). The median per-recording relative change is
    -0.089 and the signed-rank p 0.858. Both variants agree; without the cut p 0.927 and r 0.989,
    without the correction p 0.958 and r 0.998. With 10 subsets on 180 recordings the first version
    found a 65% decrease (corrected p 3.2e-08) and r 0.502; with 100 subsets the cut complexity of
    one recording still has a median coefficient of variation of 0.78 over repeated draws, so r
    passes the 0.7 reading by a small margin, and the rank sum test on 40 recordings has less power
    than on 180.
  deviations:
  - As for fig10a-complexity-randomization, 40 recordings.
- claim: fig12b-shuffle-lowers-complexity
  outcome: not_reproduced
  notebook: complexity_culture.ipynb
  output: claim:fig12b-shuffle-lowers-complexity
  notes: With the toolbox's complexity, real complexity exceeds shuffled complexity in none of 40
    recordings, the median rises by 0.174 (corrected p 2.85e-13) and Pearson r is 0.431. Without the
    cut the claim holds (real greater in all 40 recordings, corrected p 2.97e-07, r 0.902); without
    the correction real is never greater. Shuffling as Methods 2.5 describe is the toolbox's swap2,
    so the claims file's variant is the same procedure.
  deviations:
  - As for fig10a-complexity-randomization, 40 recordings.
""")

swap("- claim: fig5d-bethe-small-avalanches", "- claim: fig6-cb-distribution-curvature", """- claim: fig5d-bethe-small-avalanches
  outcome: reproduced
  notebook: models.ipynb
  output: claim:fig5d-bethe-small-avalanches
  notes: Of 10000 runs, 7018 end by layer 8. Their sizes after the cuts of Methods 2.7 are accepted
    as a truncated power law (tau 1.593, sizes 4 to 12, p 0.338) and their complexity, with the
    correction and 100 subsets per size, is 0.00300 bits/neuron with 24 of 245 subset sizes kept by
    the cut (no cut 0.265, no correction 0.374). Five repeated draws give 0.00073 to 0.00335, above
    zero in all five and above the shuffled data's 0.00000 (fig5e). The full model's sizes are
    accepted too (tau 1.402, 4 to 43, p 0.368) and its shape collapse gives 1/sigma nu z 1.598.
  deviations:
  - The number of runs (10^4) is the claims file's standard choice; small avalanches are those whose
    last active layer is 8 or less ("stopped on or before the 8th layer", Results 3.1).
- claim: fig5e-shuffle-removes-complexity
  outcome: reproduced
  notebook: models.ipynb
  output: claim:fig5e-shuffle-removes-complexity
  notes: Shuffling leaves A(t) and the size distribution unchanged and lowers the complexity from
    0.00300 to 0.00000 bits/neuron (ratio 0.000); over five repeated draws the largest shuffled value
    is 0.003 of the smallest original one. Without the cut it falls from 0.265 to -0.052; without
    the correction it rises from 0.374 to 0.414.
- claim: fig5f-network-state-poisson-keeps-complexity
  outcome: not_reproduced
  notebook: models.ipynb
  output: claim:fig5f-network-state-poisson-keeps-complexity
  notes: Permuting the order of all time bins changes the size distribution (tau 2.222 against the
    original 1.593 +/- 0.058, sizes of 1 from 0.361 to 0.209 of avalanches), but the toolbox's
    complexity changes from 0.00300 to 0.00345, a relative difference of 0.151, and 0.105 between
    the means of five repeated draws, against the criterion of 5%. The same states are kept, so the
    difference is the estimator's own spread; the original's draws differ from their mean by up to
    0.675, more than the 5% the criterion allows for the random subset draws. Without the cut the
    relative difference is 0.013 (0.004 between the means) and without the correction 0.001, both
    within 5%.
""")

swap("- claim: fig7ab-cb-complexity-susceptibility-peak", "findings:", """- claim: fig7ab-cb-complexity-susceptibility-peak
  outcome: not_reproduced
  notebook: models.ipynb
  output: claim:fig7ab-cb-complexity-susceptibility-peak
  measured:
  - null
  - 0.3
  notes: The extrapolated susceptibility, averaged over 30 models per p_trans on the 0.01 grid,
    rises at every step from 0.2 to 0.3 under both readings of Eq. 14 (N var(A/N) from 0.00105 to
    1.53) and has no interior maximum; its largest value is at 0.3, the end of the range. The whole
    100-neuron system has no interior maximum either. The criterion needs both halves, so the claim
    fails whatever the complexity shows. The complexity half was not computed; with 100 subsets per
    size one whole-system complexity of a model at p_trans 0.3 took 134 s in development, and the
    claim needs 9,900 sub-sample computations on the 0.01 grid and 18,900 on the 0.005 grid.
  deviations:
  - Only the p_trans grid of 0.01 (reading b) was run; the susceptibility rises at every step of it,
    so a grid of 0.005 cannot add an interior maximum unless the curve turns between two of its
    points.
- claim: fig7a-complexity-boundary-rise
  outcome: blocked
  blocked_by: too_large
  notes: Needs the extrapolated complexity of the sub-sampled cortical branching models of
    fig7ab-cb-complexity-susceptibility-peak, which was not computed (9,900 sub-sample computations
    on the 0.01 grid, at up to 134 s each with 100 subsets per size).
- claim: figs2-recording-length
  outcome: blocked
  blocked_by: too_large
  notes: Needs the complexity of 30 models per p_trans at three recording lengths, on all time bins.
    With extrapolation (reading a) it is three times the computation of fig7ab. Without it (reading
    b), it is 990 whole-system computations on the 0.01 grid; at 100 subsets per size one
    computation on a model of 3 x 10^5 steps at p_trans 0.3 took 134 s in development, so the
    longest recordings alone come to several hours on 4 processes, beyond the 60 min limit of a
    notebook and the time left in the run.
- claim: fig7d-cb-branching-ratio-near-1
  outcome: not_reproduced
  notebook: models.ipynb
  output: claim:fig7d-cb-branching-ratio-near-1
  notes: The mean B_new over 30 models is closest to 1 at p_trans 0.28 (1.0052). Its criterion
    compares that value with the peaks found in fig7ab-cb-complexity-susceptibility-peak, and the
    susceptibility has none, so the claim fails. 0.28 is within 0.0265 of the paper's 0.265. For
    reference, the one-step ratio sum A(t+1) / sum A(t) is 0.9373 at p_trans 0.25, where 4 p_trans
    is 1, B_basic is 0.9676 there, and the mean avalanche size rises from 16.1 at 0.25 to 110.9 at
    0.28 and 2276.6 at 0.30.
""")

s = s.replace("""    1000; the range is 2250 to 531966 and only 2 of 435 recordings have 9000 to 11000. How the paper
    counted avalanches for Figure 2E is asked of the authors (findings).""", """    1000; the range is 2250 to 531966 and only 2 of 435 recordings have 9000 to 11000. On a log scale
    the median is 10^4.92 and 43 of 435 recordings lie within half a decade of 10^4, so the count
    does not hold as an order of magnitude either. How the paper counted avalanches for Figure 2E is
    asked of the authors (findings).""")

s = s.replace("""  - Only the p_trans grid of 0.01 (reading b) was run; the 0.005 grid (reading a) would double the
    simulation time.""", """  - Only the p_trans grid of 0.01 (reading b) was run; the 0.005 grid (reading a) would double the
    simulation time. The interior maximum at 0.25 has lower values on both sides (4.619 at 0.24 and
    4.440 at 0.26), points the 0.005 grid also holds.""")

old = s[s.index("  statement: Question for the authors. With the complexity function"):s.index("- kind: methods_unavailable\n  statement: Question for the authors. Methods 2.4")]
s = s.replace(old, """  statement: Question for the authors. With the complexity function of the NCC toolbox (sub-sampling
    correction and cut at the first peak of I(k)/(k-1)) and 100 subsets per size, as Methods 2.9
    give, the cut keeps a median of 10 of 90 subset sizes in the real culture data and 74 in
    shuffled data, the cut complexity of one recording varies with a median coefficient of variation
    of 0.78 over repeated draws, and shuffling raises complexity, unlike Figures 10A and 12B. Without
    the cut the results agree with the paper. How often did the cut apply in the paper's culture
    analysis, and was it applied to the randomized data in the same way?
""")
open(p, "w").write(s)
PYEOF
python $TMPDIR/rec.py && cd  && python tools/entry.py check entries/timme-2016-criticality 2>&1 | tail -3
```

```
error: attempts/timme-2016-criticality-01.yaml: outcomes/24/measured: [None, 0.3] is not valid under any of the given schemas
1 error(s)
```

**Agent calls Bash**

```bash
cd  python - <<'EOF'
p="attempts/timme-2016-criticality-01.yaml"; s=open(p).read()
s=s.replace("""  output: claim:fig7ab-cb-complexity-susceptibility-peak
  measured:
  - null
  - 0.3
""","""  output: claim:fig7ab-cb-complexity-susceptibility-peak
""")
open(p,"w").write(s)
EOF
python tools/entry.py check entries/timme-2016-criticality 2>&1 | tail -2
```

```
0 error(s)
```

**Agent calls Bash**

```bash
cd  cat > $TMPDIR/ver.py <<'PYEOF'
import yaml
C40 = "the complexity is now computed with 100 subsets per size, as Methods 2.9 give, on 40 recordings (all 435 would exceed the notebook limit)"
R = []
def r(claim, agrees, outcome, reason, response):
    R.append(dict(claim=claim, agrees=agrees, outcome=outcome, reason=reason, response=response))

r("fig3-chain-model-complexity", True, "reproduced",
  "Complexity is 0 at c = 0 and c = 1 and 0.431 bits at c = 0.8. Integration is 0, 5.84 and 11 bits for c = 0, 0.8, 1.",
  "No change.")
r("fig5d-bethe-small-avalanches", True, "reproduced",
  "The size fit is accepted (p 0.338), but only over sizes 4 to 12. Corrected complexity is 0.00637 > 0. The same network states gave 0.00001 in another cell, so above zero is within the estimator's noise (B1); reproduced (fragile).",
  "The complexity now uses 100 subsets per size (B1) and five repeated draws are shown. It is 0.00300 bits/neuron, 0.00073 to 0.00335 over the draws, above zero in all five and above the shuffled data's 0.00000. Outcome unchanged.")
r("fig5e-shuffle-removes-complexity", True, "reproduced",
  "Size distribution identical; shuffled/original complexity ratio is 0.003. The original value is itself at noise level (B1). With the no-cut variant the complexity is also removed (-0.050 vs 0.271); reproduced (unreliable).",
  "Redone with 100 subsets per size and repeated draws. The ratio is 0.000, and the largest shuffled value over the draws is 0.003 of the smallest original one. Outcome unchanged.")
r("fig5f-network-state-poisson-keeps-complexity", True, "not_reproduced",
  "Relative change in complexity is 0.998 against a criterion of < 0.05; the size distribution did change. The network states are the same before and after, so the miss comes from the estimator's noise (B1). The no-cut (0.049) and raw (0.020) variants pass; not reproduced (unreliable).",
  "Redone with 100 subsets per size and five repeated draws. The relative difference is 0.151 (0.105 between the means of the draws), still above 5%; the original's own draws differ from their mean by up to 0.675, so the cut complexity's spread exceeds the criterion's 5% at the paper's number of subsets. No cut 0.013, no correction 0.001. Outcome unchanged, with this stated in the notes.")
r("fig6-cb-distribution-curvature", True, "partially_reproduced",
  "Durations pass all three parts (-1.23 at 0.2, +1.39 at 0.3, smallest at 0.25). Sizes fail, +0.087 +/- 0.51 at 0.2, and the smallest magnitude is at 0.2/0.21.",
  "No change. On B4, the failure is at grid points (0.2, 0.21) that the 0.005 grid also holds, as the verifier says; the 0.005 grid was not run.")
r("fig7ab-cb-complexity-susceptibility-peak", False, "not_reproduced",
  "The susceptibility half was computed by the criterion's method. It rises monotonically to the edge of the range (0.3) under both readings and has no interior peak, so the claim fails whatever the complexity shows. The complexity half is untested (B2).",
  "Agreed; changed from blocked (too_large) to not reproduced. The notebook now has a fig7ab section that prints the extrapolated susceptibility under both readings (rises at every step, no interior maximum) and says the complexity half was not computed.")
r("fig7a-complexity-boundary-rise", True, "blocked",
  "Needs the sub-sampled complexity of the cortical branching model, which was not computed.",
  "No change.")
r("figs2-recording-length", True, "blocked",
  "Not run. Reading (b) (whole 100-neuron system, no extrapolation) needs only about 1,000 complexity calls and could have been run.",
  "Not run. With the paper's 100 subsets per size, which B1 asked for, one whole-system computation on a model of 3 x 10^5 steps at p_trans 0.3 took 134 s in development, so the 990 calls of reading (b) come to several hours on 4 processes, over the 60 min notebook limit and the time left. The estimate is in the notes; outcome unchanged.")
r("fig7c-cb-curvature-no-peak", True, "not_reproduced",
  "The extrapolated absolute curvature has its only interior maximum at 0.25 (4.667); the full-system curvature also peaks at 0.25. The 0.2 > 0.3 part holds.",
  "No change. The deviation now notes that the values on both sides of the maximum (0.24 and 0.26) are points the 0.005 grid also holds (B4).")
r("fig7d-cb-branching-ratio-near-1", True, "blocked",
  "It depends on fig7ab's peak, and there is none for susceptibility; blocked, other. For reference, B_new is closest to 1 at 0.28, which is within 0.0265 of the paper's 0.265.",
  "Changed from blocked to not reproduced, judged against fig7ab as B2 asks: the susceptibility has no interior maximum, so B_new's closest approach to 1 (0.28) cannot lie within 0.0265 of it. As asked under C, the notebook now prints the mean avalanche size, B_basic and the one-step ratio against 4 p_trans; the one-step ratio is 0.9373 at 0.25, where 4 p_trans is 1.")
r("culture-counts", True, "reproduced",
  "435 recordings and 39,529 neurons, both exact. Median 91 and mode 93.3 neurons per recording, within 90 to 110. Firing-rate 5th/95th percentiles are 0.04548 and 7.70 Hz, inside 0.045 to 22 Hz; the lower one only just passes.",
  "No change.")
r("fig2d-network-isi", True, "reproduced",
  "Median mean network ISI is 6.67 ms, within 7 +/- 0.7.", "No change.")
r("fig2e-avalanche-count", True, "not_reproduced",
  "Median 83,289 avalanches and mode 81,707, against 10,000 +/- 1,000. Only 2 recordings fall in 9k to 11k. No error found in the rebinning or avalanche code. Whether the axis of Figure 2E is logarithmic could not be told; a histogram of log10 avalanche count would show whether around 10,000 is meant as an order of magnitude.",
  "Added the histogram of log10 avalanche count. The median is 10^4.92 and 43 of 435 recordings lie within half a decade of 10^4, so the count does not hold as an order of magnitude either. Outcome unchanged.")
r("fig8-subsampling-exponents", True, "reproduced",
  "Sub-sampled tau (2.106 +/- 0.407) and alpha (2.730 +/- 0.579) are lower and less spread than full-system tau (2.491 +/- 0.623) and alpha (2.928 +/- 0.648). 1/sigma nu z changes 3.6% and 1.6%. Both rebinning readings pass.",
  "No change. On B5, layout (b) stays on one recording, where it agrees with layout (a) to within 0.044, as the deviation says. On B6, the MLE over the full range after the cuts follows plmle.m as the claims file reads it; it raises tau on synthetic data (1.692 against 1.621), which the verifier found does not change the direction, and no change was made. On B7, the exclusion question is already a finding for the authors.")
r("fig8-exponents-match-literature", True, "blocked",
  "REFS is empty. The reference values come from the three cited papers, and the archive does not hold them.",
  "No change.")
r("fig8-sigmanuz-methods-agree", True, "reproduced",
  "Differences of 0.056 / 0.130 / 0.133 are each below the larger SD (0.204 / 0.337 / 0.297).", "No change.")
r("eq4-exponent-relation", True, "reproduced",
  "1.293 +/- 0.694 and 1.565 +/- 0.778 each lie within one SD of both 1/sigma nu z estimates. The test is lax; per recording only 21% agree within 0.1.",
  "No change; the per-recording agreement was already in the notes.")
r("eq4-relation-randomized", True, "reproduced",
  "For wrap and Poisson the relation holds, and tau and alpha both differ from the real data by more than one SD.", "No change.")
r("fig9-branching-ratio", True, "reproduced",
  "Band 0.05, 73.6% of recordings have B_new in [0.95, 1), and 94.7% have B_basic below 0.95. SD of B_basic is 0.088 against 0.064 for B_new.", "No change.")
r("fig10a-complexity-randomization", False, "not_reproduced",
  "Five of six non-swap randomizations lower complexity, but shuffling raises it 74-fold (0.0019 to 0.145). This pattern is what the 10-subset estimator produces (B1). The no-cut variant passes all six with Poisson among the two largest drops; not reproduced (unreliable).",
  "Redone with 100 subsets per size on 40 recordings (B1, B3). Shuffling still raises complexity, 78-fold (corrected p 2.85e-13), the cut keeps a median of 10 of 90 sizes in real data and 74 in shuffled data, and 1-bin jitter is not significant; without the cut 1-bin and 10-bin jitter are not significant on 40 recordings. Changed from partially reproduced to not reproduced, as the verifier gave it, since a 78-fold rise contradicts the claim.")
r("fig10b-susceptibility-randomization", True, "reproduced",
  "Reading (b) N var(A/N) with BH, all five randomizations lower with p_BH < 0.05, Poisson the largest drop. It fails under reading (a) or BY, where jitter1 is not significant.",
  "No change; the readings that fail were already in the notes.")
r("fig10c-curvature-randomization", True, "partially_reproduced",
  "jitter10, jitter100, wrap and Poisson lower with p < 1e-37. jitter1 is +0.139 with p_BH 0.39.", "No change.")
r("figs8-complexity-susceptibility-correlation", True, "not_reproduced",
  "Pearson r is 0.542 (a) or 0.625 (b), against 0.23 +/- 0.023. Only the no-correction variant with reading (a) lands inside (0.221); not reproduced (unreliable).",
  "Redone with 100 subsets per size on 40 recordings: r is 0.902 (a) and 0.905 (b); no variant lands inside (no correction 0.267 and 0.446, no cut -0.605 and -0.592). Outcome unchanged.")
r("fig11ac-fit-range-randomization", True, "reproduced",
  "Poisson lowers the size and duration ranges (p_BH ~1e-141). jitter10 raises them (+0.047 / +0.070 decades, significant). jitter100 and wrap lower them; jitter1 is not significant.",
  "No change.")
r("figs9-complexity-fit-range-correlation", True, "not_reproduced",
  "r = 0.143 for the size range (expected 0.296) and -0.049 for the duration range (expected 0.197); not reproduced (unreliable).",
  "Redone with 100 subsets per size on 40 recordings: r is 0.060 and -0.107; no variant matches both. Outcome unchanged.")
r("fig11bd-exponents-randomization", True, "partially_reproduced",
  "tau rises significantly for 4 of 5 randomizations; jitter1 lowers it significantly (p_BH 0.011). alpha rises for 3 of 5; jitter1 and jitter10 are not significant.",
  "No change.")
r("fig12a-swap-preserves-complexity", True, "not_reproduced",
  "Swapping lowers complexity by 65% (rank-sum p_BH 3e-8) and Pearson r is 0.502. The no-cut (p 0.42, r 0.968) and raw (p 0.81, r 0.996) variants both meet the criterion; not reproduced (unreliable).",
  "Redone with 100 subsets per size on 40 recordings, as B1 asks. The rank sum test now gives corrected p 0.836 (median 0.00223 against 0.00265) and Pearson r 0.775, which meets the criterion, so the outcome is changed to reproduced. The notes say that r passes the 0.7 reading by a small margin, that the cut complexity varies across draws (median coefficient of variation 0.78), and that 40 recordings give the test less power than 180.")
r("fig12b-shuffle-lowers-complexity", True, "not_reproduced",
  "Real complexity exceeds shuffled in only 10% of recordings, and r is 0.234. The no-cut variant meets the criterion (99.4%, p 1e-25, r 0.856); not reproduced (unreliable).",
  "Redone with 100 subsets per size on 40 recordings: real exceeds shuffled in none of 40 and r is 0.431; without the cut in all 40 (r 0.902). Outcome unchanged.")

v = [dict(date="2026-11-09", kind="agent",
          by="Independent agent run by CatalystNeuro (same harness, separate context, did not write the notebooks)",
          reviewed=("Round 1. The three executed notebooks with the conclusion cells and the summaries removed, the helper "
                    "modules hc8.py and models.py and the claims file, with the paper's full text. The verifier tested the "
                    "helpers on synthetic inputs (complexity with 10 and 100 subsets, fdr, branching_new, wls_intercept, "
                    "shape_collapse, plmle_full) and checked the archive's file list and the Data.zip MD5. It could not reach "
                    "the toolbox's site. It reported seven problems; B1 (10 subsets per size make the cut complexity noisy) "
                    "and B2 (fig7ab blocked although its susceptibility half fails) affect conclusions."),
          results=R)]
txt = yaml.safe_dump({"verifications": v}, sort_keys=False, width=100, allow_unicode=True)
p = "attempts/timme-2016-criticality-01.yaml"
s = open(p).read()
assert "verifications:" not in s
open(p, "a").write(txt)
PYEOF
python $TMPDIR/ver.py && python tools/entry.py check entries/timme-2016-criticality 2>&1 | tail -2; grep -n "—\|rather" attempts/timme-2016-criticality-01.yaml entries/timme-2016-criticality/README.md | head
```

```
0 error(s)
```

**Agent calls Bash**

```bash
cd  grep -nE "^\s+[^:]*: .*: " attempts/timme-2016-criticality-01.yaml | head; grep -nE "^\s{4,}[^-][^:]*: " attempts/timme-2016-criticality-01.yaml | grep -v "^\S*\s*[a-z_]*: " | head
```

```
457:    response: 'Changed from blocked to not reproduced, judged against fig7ab as B2 asks: the susceptibility
550:    response: 'Redone with 100 subsets per size on 40 recordings: r is 0.902 (a) and 0.905 (b); no variant
563:    response: 'Redone with 100 subsets per size on 40 recordings: r is 0.060 and -0.107; no variant matches
586:    response: 'Redone with 100 subsets per size on 40 recordings: real exceeds shuffled in none of 40
```

**Agent calls Bash**

```bash
cd  grep -n "180 rec\|0\.00637\|10 subsets per size\|N_SUBSETS = 10 \|blocked, too_large (depends" entries/timme-2016-criticality/*.ipynb entries/timme-2016-criticality/README.md attempts/timme-2016-criticality-01.yaml | cut -c1-220
```

```
entries/timme-2016-criticality/complexity_culture.ipynb:389:    "exceed the 60 min limit of a notebook. The first version used 10 subsets on 180 recordings.\n",
attempts/timme-2016-criticality-01.yaml:179:    on 180 recordings, gave the same pattern (five of six lower, shuffling raises it 74-fold) and
attempts/timme-2016-criticality-01.yaml:185:    notebook. The first version used 10 subsets on 180 recordings.
attempts/timme-2016-criticality-01.yaml:218:    without the correction p 0.958 and r 0.998. With 10 subsets on 180 recordings the first version
attempts/timme-2016-criticality-01.yaml:379:    reach the toolbox's site. It reported seven problems; B1 (10 subsets per size make the cut complexity
attempts/timme-2016-criticality-01.yaml:391:    reason: The size fit is accepted (p 0.338), but only over sizes 4 to 12. Corrected complexity is 0.00637
```

**Agent calls Bash**

```bash
cd  python tools/entry.py check entries/timme-2016-criticality 2>&1 | tail -1; git status --short | grep -v "^ M tools\|^?? tools"; date -u
```

```
0 error(s)
 M attempts/timme-2016-criticality-01.yaml
 M entries/timme-2016-criticality/README.md
 M entries/timme-2016-criticality/complexity_culture.ipynb
 M entries/timme-2016-criticality/culture_criticality.ipynb
 M entries/timme-2016-criticality/entry.yaml
 M entries/timme-2016-criticality/models.ipynb
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
Tue Nov 10 00:45:28 UTC 2026
```

**Agent**

I ran the whole entry again with `python tools/entry.py all`. All three notebooks pass: 42 min for the culture notebook, 38 min for complexity and 11 min for the models. `entry.py check` reports 0 errors. The code changes from the earlier revision run, which was cut off before its full run finished, were already in the source; this run executed them, wrote the conclusions and updated the record. Nothing is committed.

**Changes in outcome**
- **fig7ab** (complexity and susceptibility peak in the model): blocked → not reproduced, as the verifier said (B2). The susceptibility rises at every step up to p_trans 0.3, under both readings, and never peaks. The complexity half was not computed.
- **fig7d** (branching ratio near 1): blocked → not reproduced. There is no susceptibility peak to compare against. B_new is closest to 1 at p_trans 0.28, which is within 0.0265 of the paper's 0.265.
- **fig10a** (complexity falls under randomization): partially reproduced → not reproduced, as the verifier gave it. Even with 100 subsets, shuffling raises complexity 78-fold, and the 1-bin jitter is not significant.
- **fig12a** (swapping preserves complexity): not reproduced → reproduced. With 100 subsets, swapping makes no significant difference (corrected p 0.836) and Pearson r is 0.775, which passes the 0.7 threshold. The record notes that it passes only narrowly and that the estimate is noisy (median coefficient of variation 0.78 across repeated draws).
- Every other outcome stays the same. The complexity claims fig5d, fig5e, fig5f, figs8, figs9 and fig12b were redone with the new settings. figs8 is now r 0.90 against the expected 0.23, and fig5f's relative difference is 0.151 against the 5% criterion. fig5f fails because the estimate's own spread across draws (up to 0.675) is larger than 5%.

**What I added or corrected**
- Complexity now uses 100 subsets per size, as Methods 2.9 give (B1). Even at 100, the toolbox's cut keeps a median of 10 of 90 subset sizes in the real data and 74 in shuffled data, so the instability the verifier found is not only due to 10 subsets.
- Outputs the verifier asked for:
  - repeated draws at 10 and 100 subsets on 10 recordings, with the number of subset sizes the cut keeps;
  - five draws on the Bethe raster;
  - for the model, mean avalanche size, B_basic and the one-step ratio against 4·p_trans (the one-step ratio is 0.937 at p_trans 0.25);
  - a log10 histogram of avalanche counts for fig2e. Its median is 10^4.92, so "around 10,000" fails as an order of magnitude too.
- I rewrote the conclusion cells, the summaries, the README, the notebook runtimes in `entry.yaml`, and the record's notes and deviations. I also updated the finding that asks the authors about the cut. Round 1 is recorded under `verifications`, with the verifier's reasons and my responses.

**What I did not do**
- **Fewer recordings for complexity.** It now runs on 40 of 435 recordings, down from 180. At 100 subsets, 40 recordings took 34 min, so more would break the 60-minute limit per notebook. This is recorded as a deviation.
- **figs2 reading (b)** is still blocked as too large. At 100 subsets, the 990 calls come to several hours of computing.
- **p_trans grid.** The 0.005 grid was not run. The fig6 and fig7c results sit at points the 0.005 grid also contains.
- **Smaller verifier points.** B5 (layout b on one recording), B6 (how the power-law fit handles gaps after the cuts) and B7 (exclusion) are answered in the record with no code change.
- **Reader questions.** The verifier reported no misreading of the claims file, so I added none.

## End of run

35 turns, 97 minutes, $3.15 at API prices, result: success.
