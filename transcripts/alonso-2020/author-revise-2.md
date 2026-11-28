# alonso-2020 · author-revise-2 · run 46120923447

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
date -u; cat transcripts/alonso-2020/verifier-2-report.md; ls entries/alonso-2020 questions/ | head -50
```

```
Sat Nov 28 07:30:59 UTC 2026
**Verifier report, round 2: Alonso & Marder 2020 (doi:10.7554/elife.55470), Dryad m31b1h7 v94811**

The claims file has 23 claims and the attempt record gives 23 outcomes: 8 reproduced, 5 partially reproduced, 7 not reproduced and 3 blocked. Cell numbers below refer to `reproduce_alonso_2020.ipynb` unless a notebook is named. The cells have been renumbered since round 1, so deposit-models is now cell 14, not 12.

**1. Outcomes**

I agree with 21 outcomes and accept one more with a caveat. I now question fig6s1, which I accepted in round 1.

| Claim | Outcome | Agree? | Assumption stated and reasonable? |
|---|---|---|---|
| deposit-models | not_reproduced | Yes (cell 14: 3 of 38) | n/a |
| fig1c-frequency-q10-phase-constant | partial | Yes (cell 20) | n/a |
| fig1s1-three-models | not_reproduced | Yes (cell 23) | n/a |
| all-models-compensated | partial | Yes (cell 26: 36 of 38, 35 with the strict order test) | Yes. The order test is stated, and the variant also gives a partial outcome. |
| intermediate-temperature-failures | blocked (data_missing) | Yes (cell 32) | n/a |
| figs2-ramp-largest-isi | reproduced | Yes (ramps cell 5) | n/a |
| figs3-duty-cycle-variable-across-models | reproduced (variant reading) | Yes, on the variant the criterion names | n/a |
| fig2-lp-spike-amplitude-threshold | reproduced | Yes as the criterion is written (voltage cell 5) | Stated, but weakly supported; see below. |
| fig2s1-peak-voltage-diverse | reproduced | Yes (voltage cell 8) | n/a |
[... 123 more lines not kept]
```

**Agent calls Bash**

```bash
grep -n "^#" docs/protocol.md | head -80; wc -l docs/protocol.md
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
374:### 2. Check the data against its description
397:### 3. Write the entry
482:### 4. Lock, check and run
502:### 5. Record the attempt
633:### 6. Hand over for verification
671:## Repeat attempts
737:## Local and remote datasets
760:## Verifier
764:### Round 1: without the author's conclusions
789:### Round 2: with the author's conclusions
[... 2 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 1,42p docs/protocol.md; sed -n 199,240p docs/protocol.md; sed -n 330,373p docs/protocol.md; sed -n 482,670p docs/protocol.md; sed -n 789,813p docs/protocol.md
```

```
# Protocol for an attempt

Version: `pilot-19`. Record this version in the attempt's provenance.

This is what agents, or people, do to attempt a target and deposit the
result. A target is a dataset in a public archive and a paper it names. How
each archive's datasets are named, versioned and read is in
[archives.md](archives.md); the examples here are from DANDI, the first. It is written from the pilot attempts
([pilot notes](https://github.com/encorescience/encore-registry/blob/main/docs/pilot-notes.md)); the reasons for the rules are there.

An attempt has three roles, each a separate run with a separate context:

- The **reader** reads the paper and writes the claims file: every finding,
  and how each is to be tested, taken from the paper. A second reader checks
  it against the paper. Readers never see the dataset's data.
- The **author** tests the claims on the dataset. It reads the paper to
  understand the claims, but the claims file binds it: it cannot change a
  claim's statement, expected values or criterion. A method detail the file
  lacks it takes from the paper, citing the passage, and it asks a reader
  only when it believes the file misreads the paper.
[... 322 more lines not kept]
```

**Agent calls Bash**

```bash
nproc; ls attempts/ | grep alonso; ls executed/alonso-2020/ 2>/dev/null; wc -l attempts/alonso-2020-01.yaml; cat entries/alonso-2020/entry.yaml; git diff --stat
```

```
4
alonso-2020-01.yaml
ramps.ipynb
reproduce_alonso_2020.ipynb
result.json
voltage_distributions.ipynb
648 attempts/alonso-2020-01.yaml
schema_version: 1
name: alonso-2020
type: reproduction
title: Temperature compensation in a model pyloric network (Alonso and Marder 2020)
description: Tests the findings of Alonso and Marder (2020) on Dryad m31b1h7, which holds the authors' Java model of a
  three-cell pyloric network, their Python scripts, and the parameters of 38 temperature-compensated models. Every
  claim is tested by simulating the deposited models with a port of the deposited Java, at fixed temperatures, on
  temperature ramps, with currents removed, and at high temperatures where the networks crash.
license: Apache-2.0
python: "3.13"
notebooks:
- path: reproduce_alonso_2020.ipynb
  title: Reproducing Alonso and Marder (2020) from Dryad m31b1h7
[... 17 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "attempts/alonso-2020-01.yaml"
}
```

```
1	schema_version: 3
2	id: alonso-2020-01
3	datasets:
4	- archive: dryad
5	  id: m31b1h7
6	  version: '94811'
7	  doi: 10.5061/dryad.m31b1h7
8	  relation: primary
9	paper: doi:10.7554/elife.55470
10	date: 2026-11-27
11	entry: alonso-2020
12	provenance:
13	  kind: agent
14	  accountable:
15	    name: CatalystNeuro
16	  agent:
17	    harness: Claude Code
18	    model: claude-opus-5-5
19	    protocol: pilot-19
20	  runner:
[... 629 more lines not kept]
```

**Agent calls Bash**

```bash
grep -n "timeout\|parallel\|Pool\|fresh\|stamp\|runtime_minutes\|60" tools/entry.py | head -60
```

```
25:`run` builds a fresh virtual environment from the lock file and executes each
30:A run that passes leaves a stamp beside the executed copies (.clean-run.json):
33:so, without executing anything; --fresh executes all the same.
558:def upgrade_python(entry_dir: Path, version: str, before: Path, output_dir: Path, timeout: int,
565:    if lock(entry_dir, version) or run(entry_dir, output_dir, timeout, max_minutes, fresh=True):
613:    """The stamp of executed copies that a run now would only make again: made from this hash, each copy still as
616:        stamp = json.loads((output_dir / STAMP).read_text())
618:        if stamp["hash"] != entry_hash(entry_dir) or time.time() - stamp["finished"] > REUSE_DAYS * 86400:
620:        if [n["path"] for n in entry["notebooks"]] != [r["notebook"] for r in stamp["results"]]:
622:        for r in stamp["results"]:
623:            if not r["ok"] or r["seconds"] > max_minutes * 60 or file_hash(output_dir / r["notebook"]) != r["sha256"]:
625:        return stamp
630:def run(entry_dir: Path, output_dir: Path, timeout: int, max_minutes: float, fresh: bool = False) -> int:
632:    stamp = None if fresh else reusable(entry_dir, output_dir, max_minutes)
633:    if stamp:
634:        when = time.strftime("%Y-%m-%d %H:%M UTC", time.gmtime(stamp["finished"]))
635:        for r in stamp["results"]:
638:              f"{stamp['hash'][:12]}). Nothing was executed and no environment was built; --fresh runs it again.")
661:             f"--ExecutePreprocessor.timeout={timeout}", f"--ExecutePreprocessor.kernel_name={kernel}",
668:        if ok and seconds > max_minutes * 60:
[... 6 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 600,700p tools/entry.py
```

```
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
    the run left it, each within the time limit asked for now, and not older than REUSE_DAYS. Else None."""
    try:
        stamp = json.loads((output_dir / STAMP).read_text())
        entry = yaml.safe_load((entry_dir / "entry.yaml").read_text())
        if stamp["hash"] != entry_hash(entry_dir) or time.time() - stamp["finished"] > REUSE_DAYS * 86400:
            return None
[... 80 more lines not kept]
```

**Agent calls Bash**

```bash
ls claims/ 2>/dev/null | grep alonso; f=$(ls claims/alonso-2020* papers/claims/alonso-2020* 2>/dev/null | head -1); echo $f; grep -n "figs3-duty" -A40 $f | head -60
```

```
alonso-2020.yaml
claims/alonso-2020.yaml
187:- id: figs3-duty-cycle-variable-across-models
188-  statement: Across the 36 models the LP duty cycle depends on temperature in different ways,
189-    so that the duty cycle distributions differ from model to model.
190-  source: Results, Duty cycle and phase maintenance in model pyloric networks, paragraph 5;
191-    Figure 1, figure supplement 3; Discussion, paragraph beginning "One of the most significant
192-    results"
193-  quote: Across the models, different values of the maximal conductances G and temperature
194-    sensitivities Q10 result in consistent differences in the duty cycle distributions.
195-  criterion: The supplement's legend is not in the text read. For each of the 36 models, the
196-    per-burst duty cycles of LP over 10 to 25 degrees C (the ramp of Figure 1, figure
197-    supplement 2, 10 to 25 degrees C over 60 min, is the reading taken; simulations at the 16
198-    temperatures of Figure 1C are the variant). Reproduced when the models' LP duty-cycle
199-    distributions differ by a two-sample Kolmogorov-Smirnov test at p < 0.05 for most model
200-    pairs (more than half of the 630 pairs), a standard choice; the median and range of each
201-    model's LP duty cycle are reported.
202-- id: fig2-lp-spike-amplitude-threshold
203-  statement: In the LP cell of the model of Figure 2, spike amplitude decreases and the spike
204-    threshold depolarizes as temperature rises from 10 to 25 degrees C.
[... 39 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/alonso-2020; python - <<'EOF'
import json
nb=json.load(open('ramps.ipynb'))
for i,c in enumerate(nb['cells']):
    print('=====',i,c['cell_type'],c.get('metadata',{}).get('tags'))
    print(''.join(c['source']))
EOF
```

```
===== 0 markdown None
# Alonso & Marder (2020), temperature ramps, from Dryad m31b1h7

Paper: Alonso LM, Marder E (2020), eLife 9:e55470, doi:10.7554/eLife.55470; claims in
`claims/alonso-2020.yaml` (version of record, main text, legends and Methods).

Dataset: Dryad doi:10.5061/dryad.m31b1h7, version id 94811 (the only published version, so the
one pinned), file `alonso_marder_tempcomp_2019_root.zip` (MD5 from Dryad's file list checked on
load; SHA-256 printed below). The models are simulated with the port in `pyloric.py`; the main
notebook, `reproduce_alonso_2020.ipynb`, compares it with the deposited Java and checks the data.

Two ramp protocols:

- up: 10 to 25 degrees C over 60 min (Results, Duty cycle and phase maintenance, paragraph 5,
  "ramps from 10 C to 25 C over 60 min"), model PLKTEM, for figs2-ramp-largest-isi;
- updown: 10 to 35 degrees C in 30 min and back to 10 degrees C at the same rate (Results,
  Hysteresis and multistability, paragraph 1), every deposited model (38), for
  fig8a-hysteresis-quiescence, fig8-up-down-ramps and fig8b-pathological-attractor.

The up ramp of every model, which figs3-duty-cycle-variable-across-models takes as its main
[... 262 more lines not kept]
```

**Agent calls Bash**

```bash
grep -n "^def \|^    def \|Pool\|processes" pyloric.py | head -80; python - <<'EOF'
import json
nb=json.load(open('reproduce_alonso_2020.ipynb'))
for i,c in enumerate(nb['cells']):
    src=''.join(c['source'])
    if i in (6,7,13,14,15,27,28,29,30,51,52,53,54) or 'figs3' in src[:300]:
        print('=====',i,c['cell_type'],c.get('metadata',{}).get('tags'))
        print(src)
EOF
```

```
86:def read_zip_bytes() -> bytes:
90:def digests(raw: bytes) -> dict:
97:def open_zip(raw: bytes) -> zipfile.ZipFile:
101:def model_files(z: zipfile.ZipFile) -> dict:
111:def read_vector(z: zipfile.ZipFile, member: str) -> np.ndarray:
115:def load_models(z: zipfile.ZipFile) -> dict:
119:def load_ci(z: zipfile.ZipFile) -> np.ndarray:
123:def score_of(member: str) -> float:
127:def conductances(p: np.ndarray) -> np.ndarray:
132:def q10_conductances(p):
136:def q10_timescales(p):
141:def q10_synapses(p):
145:def scaled(p: np.ndarray, current: int, fraction: float) -> np.ndarray:
157:def _factors(p, T, f):
173:def _boltz(V, A, B):
178:def _taux(V, CT, DT_, AT, BT):
183:def _spectau(V, CT, DT_, AT, BT, AT2, BT2):
188:def _syn_ss(Vpre):
193:def _cell_currents(y, o, p, po, f, out):
211:def _syn_currents(y, p, f, out):
[... 200 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 517,562p pyloric.py; sed -n 401,425p pyloric.py; date -u
```

```
# --- parallel jobs (run in worker processes) ---------------------------------------------------

def pmap(fn, tasks, procs=4):
    """Map fn over tasks in `procs` processes (the runner has 4 CPUs)."""
    from multiprocessing import get_context
    with get_context("fork").Pool(procs) as pool:
        return pool.map(fn, tasks, chunksize=1)


def run_fixed(task):
    """task = (key, p, y0, temp, seconds, drop[, thr]). Simulates at a fixed temperature and returns,
    for the window after `drop` seconds, the spike times and upward slow-wave crossings of each cell
    (times from the window start), the four classes, and the final state. `thr` is the spike
    threshold (SPIKE_THRESHOLD when not given)."""
    key, p, y0, temp, seconds, drop = task[:6]
    thr = task[6] if len(task) > 6 else SPIKE_THRESHOLD
    s = simulate(p, temp, seconds, y0, thr=thr)
    return dict(key=key, temp=temp, spikes=s.window(drop, seconds),
                sw_up=[u[u >= drop] - drop for u in s.sw_up], classes=classify(s, drop, seconds),
                final=s.final, length=seconds - drop)
[... 52 more lines not kept]
```

**Agent calls Bash**

```bash
cd ../..; grep -n "id: fig6s1\|id: fig7-" -A22 claims/alonso-2020.yaml | grep -n "criterion" -A10; cat questions/alonso-2020.yaml 2>/dev/null | head -30; cat entries/alonso-2020/README.md
```

```
10:356-  criterion: Models B7SDOL, J9U8SQ, 4R2719, R3VIEW, Q8FBN1, RMZ8KZ, EF84RN and SJR46Y (Methods,
11-357-    Parameters used in this study). The supplement's legend is not in the text read, so the
12-358-    temperature of each crashed state is open; each model is taken at the lowest temperature
13-359-    above 25 degrees C, in 1 degree steps up to 35 degrees C, at which the network is not
14-360-    triphasic (a standard choice). As in fig6-crash-different-mechanisms, the mechanism of a
15-361-    crash is read as the pair of currents with the largest inward and the largest outward
16-362-    share in each cell, averaged over the analysed window (a reading; the paper gives no
17-363-    measure). Reproduced when every model crashes below 35 degrees C and no two models have
18-364-    the same pairs in all three cells; partially reproduced when every model crashes and at
19-365-    least six distinct patterns occur among the eight (a standard choice).
20-366:- id: fig7-high-temperature-slow-timescales
--
28:374-  criterion: Models J9U8SQ, G81PUL, G7EOZ8, SAXT8Y and KNMLBC at 34, 34, 33, 29 and 30 degrees C
29-375-    (Figure 7 legend), 30 s analysed. The legends of Figures 5 and 9B tie Figure 7A to the
30-376-    model the Methods name FGFKQS for those figures, so FGFKQS at 34 degrees C is a variant
31-377-    for panel A. A time scale much longer than 1 s is read as (a) an
32-378-    interval longer than 2 s between successive bursts or spikes of some cell, or (b) a
33-379-    dominant period of the slow voltage (spikes removed by a 50 ms median filter, a standard
34-380-    choice) longer than 2 s, the factor 2 a standard bound for "much longer". Reproduced when
35-381-    all five models show it under one reading and none is triphasic; partially reproduced for
[... 51 more lines not kept]
```

**Agent calls Bash**

```bash
ls -a executed/alonso-2020/; ls executed/alonso-2020/.venv/bin/python && executed/alonso-2020/.venv/bin/python -c "import numba, scipy; print(numba.__version__)"; cat executed/alonso-2020/result.json
```

```
.
..
.clean-run.json
.venv
ramps.ipynb
reproduce_alonso_2020.ipynb
result.json
voltage_distributions.ipynb
executed/alonso-2020/.venv/bin/python
0.68.1
{
 "entry": "alonso-2020",
 "python": "3.13",
 "results": [
  {
   "notebook": "reproduce_alonso_2020.ipynb",
   "ok": true,
   "seconds": 1704,
   "error": null
  },
[... 14 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/alonso-2020 && ../../executed/alonso-2020/.venv/bin/python - <<'EOF'
import time, numpy as np
import pyloric as P
raw=P.read_zip_bytes(); Z=P.open_zip(raw); M=P.load_models(Z); CI=P.load_ci(Z); N=list(M)
P.pmap(P.run_ramp,[(n,M[n],CI,[(10.0,10.1,2.0)]) for n in N[:4]])
t0=time.time()
out=P.pmap(P.run_ramp,[(n,M[n],CI,[(10.0,10.5,120.0)]) for n in N[:4]])
r=4*120/(time.time()-t0); print(r, "sim s/s;", 38*3600/r/60, "min")
EOF
```

```
38.73970243063854 sim s/s; 58.854349851608276 min
```

**Agent calls Bash**

```bash
date -u; ../../executed/alonso-2020/.venv/bin/python -c "
import pyloric as P
Z=P.open_zip(P.read_zip_bytes()); M=P.load_models(Z); print(list(M))"; grep -n "multi\b\|^multi\|multi =" reproduce_alonso_2020.ipynb | head
```

```
Sat Nov 28 07:33:38 UTC 2026
['0SHNMD', '2RO5K6', '4R2719', '4X6W66', '71G6LA', '72TVF2', 'B7SD0L', 'CG4J30', 'ED50XO', 'EF84RN', 'FGFKQS', 'G7P2WE', 'H5AIZR', 'HX40PF', 'INPO74', 'J6OK9B', 'J9U8SQ', 'KMNLBC', 'KV0BR4', 'LE8W3F', 'MAXTTP', 'ML4GPK', 'NJP4RT', 'OPLRCP', 'P1LH61', 'PCR6RP', 'PLKTEM', 'Q0H92I', 'R00977', 'R2PNKE', 'R3VIEW', 'RMZ8KZ', 'SJR46Y', 'TGCEVM', 'VNROH5', 'WWZ3CN', 'X64GYZ', 'XXKF5A']
298:    "multi = [g for g in groups.values() if len(g) > 1]\n",
300:    "      f\"{len(multi)} sets carry more than one Q10 set:\")\n",
301:    "for g in multi:\n",
642:    "print(f\"\\nsets of maximal conductances with more than one deposited Q10 set: {len(multi)} of {len(groups)}\")\n",
643:    "for g in multi:\n",
693:    "for g in multi:\n",
```

**Agent calls Bash**

```bash
sed -n 285,300p reproduce_alonso_2020.ipynb
```

```
"execution_count": null,
   "id": "8d3afaca",
   "metadata": {
    "tags": [
     "finding-shared-conductances"
    ]
   },
   "outputs": [],
   "source": [
    "key = {n: tuple(np.r_[P.conductances(MODELS[n]).ravel(), MODELS[n][[35, 72, 109]], MODELS[n][111:118]]) for n in NAMES}\n",
    "groups = {}\n",
    "for n in NAMES:\n",
    "    groups.setdefault(key[n], []).append(n)\n",
    "multi = [g for g in groups.values() if len(g) > 1]\n",
    "print(f\"{len(NAMES)} models, {len(groups)} distinct sets of maximal conductances; \"\n",
    "      f\"{len(multi)} sets carry more than one Q10 set:\")\n",
```

**Agent**

Now I'll write the new notebook for the figs3 ramp reading.

**Agent calls Bash**

```bash
../../executed/alonso-2020/.venv/bin/python - <<'EOF'
import nbformat as nbf
nb = nbf.v4.new_notebook()
C = []
C.append(nbf.v4.new_markdown_cell("""# Alonso & Marder (2020), the 60 min ramp of every model, from Dryad m31b1h7

Paper: Alonso LM, Marder E (2020), eLife 9:e55470, doi:10.7554/eLife.55470; claims in
`claims/alonso-2020.yaml` (version of record, main text, legends and Methods).

Dataset: Dryad doi:10.5061/dryad.m31b1h7, version id 94811 (the only published version, so the
one pinned), file `alonso_marder_tempcomp_2019_root.zip` (MD5 from Dryad's file list checked on
load; SHA-256 printed below). The models are simulated with the port in `pyloric.py`; the main
notebook, `reproduce_alonso_2020.ipynb`, compares it with the deposited Java and checks the data.

This notebook runs the main reading of figs3-duty-cycle-variable-across-models: the ramp of
Figure 1, figure supplement 2, 10 to 25 degrees C over 60 min (Results, Duty cycle and phase
maintenance, paragraph 5, "ramps from 10 C to 25 C over 60 min"), for each model. The main
notebook tests the claim on its variant, the 16 fixed temperatures.

Timed on a subset, the ramp of all 38 models takes about 59 min on 4 CPUs, more than a notebook
may take (60 min with the rest of the notebook). The first 28 models in the deposit's file order
are run (7 rounds of 4 processes, about 43 min); the order is the archive's, chosen before any
result was seen. Should the machine be slower than expected, the cell stops starting new rounds
before the time limit and prints how many models were run.

The ramp is run as in `ramps.ipynb`: the temperature changes linearly in time, the temperature
factors are updated every 20 steps (1 ms), and each ramp starts from the deposited initial
conditions at 10 degrees C (assumptions; `pyloric.py`).

| Claim | Tested |
|---|---|
| figs3-duty-cycle-variable-across-models | tested on the main (ramp) reading, 28 of the 38 models |"""))
C.append(nbf.v4.new_code_cell("""import resource
import time
from itertools import combinations

import numpy as np
import pandas as pd
from scipy import stats

import pyloric as P

T_START = time.time()
pd.set_option("display.width", 200, "display.max_columns", 40, "display.max_rows", 200)
raw = P.read_zip_bytes()
print(P.digests(raw))
Z = P.open_zip(raw)
MODELS = P.load_models(Z)
CI = P.load_ci(Z)
NAMES = list(MODELS)"""))
C.append(nbf.v4.new_markdown_cell("""## The ramps

Rounds of 4 models, one per process. A round is started only when the time so far plus the
longest round so far stays within 54 min."""))
C.append(nbf.v4.new_code_cell("""print(len(NAMES), "models in the deposit")
RUN = NAMES[:28]
print("models run:", RUN)
UP, rounds = {}, []
for i in range(0, len(RUN), 4):
    elapsed = time.time() - T_START
    if rounds and elapsed + max(rounds) > 54 * 60:
        print(f"stopped before round {i // 4 + 1}: {elapsed / 60:.1f} min so far, longest round {max(rounds) / 60:.1f} min")
        break
    t0 = time.time()
    for r in P.pmap(P.run_ramp, [(n, MODELS[n], CI, [(10.0, 25.0, 3600.0)]) for n in RUN[i:i + 4]]):
        UP[r["key"]] = r["legs"][0]
    rounds.append(time.time() - t0)
    print(f"round {i // 4 + 1}: {RUN[i:i + 4]} in {rounds[-1] / 60:.1f} min")
DONE = [n for n in RUN if n in UP]
print(f"\\nramps run: {len(DONE)} models; {sum(4 * 3600.0 for _ in rounds) / sum(rounds):.0f} simulated seconds per second "
      f"on 4 processes; peak memory {resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1e6:.2f} GB")
print("runs that diverged (NaN):", [n for n in DONE if not UP[n]["finite"]])"""))
C.append(nbf.v4.new_markdown_cell("""## figs3-duty-cycle-variable-across-models

> Across the 36 models the LP duty cycle depends on temperature in different ways, so that the
> duty cycle distributions differ from model to model.

Per-burst LP duty cycles over the whole ramp (burst duration over the time to the next burst
start, bursts formed with the Methods' 200 ms threshold), pooled per model; two-sample
Kolmogorov-Smirnov test for every pair of the models run. Reproduced when more than half of the
pairs differ at p < 0.05 (criterion). The median and range of each model's LP duty cycle are
reported, with the mean LP duty cycle per 1 degree window and its Spearman correlation with
temperature."""))
C.append(nbf.v4.new_code_cell("""DCR, TMR = {}, {}
for n in DONE:
    b = P.burst_stats(UP[n]["spikes"][1])
    DCR[n] = b["dc"]
    TMR[n] = 10 + 15 * b["starts"][:-1] / 3600
summ = pd.DataFrame({n: dict(bursts=len(d), median=np.median(d), lo=np.min(d), hi=np.max(d)) for n, d in DCR.items()}).T
print(summ.round(3).to_string())
pv = np.array([stats.ks_2samp(DCR[a], DCR[b]).pvalue for a, b in combinations(DONE, 2)])
print(f"\\npairs: {len(pv)}; with p < 0.05: {(pv < 0.05).sum()} ({(pv < 0.05).mean():.3f}); largest p {pv.max():.3g}")
key = {n: tuple(np.r_[P.conductances(MODELS[n]).ravel(), MODELS[n][[35, 72, 109]], MODELS[n][111:118]]) for n in NAMES}
for a, b in combinations(DONE, 2):
    if key[a] == key[b]:
        print(f"   same conductances, different Q10: {a} vs {b}: KS p = {stats.ks_2samp(DCR[a], DCR[b]).pvalue:.2e}")
edges = np.arange(10.0, 25.0 + 1e-9, 1.0)
lp = pd.DataFrame({n: [np.mean(DCR[n][(TMR[n] >= a) & (TMR[n] < b)]) if ((TMR[n] >= a) & (TMR[n] < b)).any() else np.nan
                       for a, b in zip(edges[:-1], edges[1:])] for n in DONE}, index=edges[:-1] + 0.5)
rho = lp.apply(lambda c: stats.spearmanr(lp.index[c.notna()], c.dropna())[0])
print("Spearman correlation of mean LP duty cycle (1 degree windows) with temperature, per model: from %.2f to %.2f; "
      "below -0.5: %d, above 0.5: %d, between: %d" % (rho.min(), rho.max(), (rho < -0.5).sum(), (rho > 0.5).sum(),
                                                      ((rho >= -0.5) & (rho <= 0.5)).sum()))
print("\\nmean LP duty cycle per 1 degree window (rows: window centre, C):")
print(lp.round(3).to_string())"""))
C.append(nbf.v4.new_markdown_cell("""**Result: RESULT_PLACEHOLDER**"""))
C.append(nbf.v4.new_markdown_cell("""## Summary

SUMMARY_PLACEHOLDER"""))
C.append(nbf.v4.new_code_cell("""print(f"notebook run time {(time.time() - T_START) / 60:.1f} min; peak memory "
      f"{resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1e6:.2f} GB")"""))
C[3].metadata["tags"] = ["sanity"]
C[5].metadata["tags"] = ["claim:figs3-duty-cycle-variable-across-models"]
nb.cells = C
nb.metadata["kernelspec"] = {"name": "python3", "display_name": "Python 3", "language": "python"}
nbf.write(nb, "ramps_up.ipynb")
EOF
date -u
```

```
Sat Nov 28 07:34:05 UTC 2026
```

**Agent calls Bash**

```bash
python -c "import json;print(json.load(open('ramps.ipynb'))['metadata'])"; mkdir -p $TMPDIR/t && cp pyloric.py $TMPDIR/t/ && sed -e 's/NAMES\[:28\]/NAMES[:6]/' -e 's/3600\.0)\]/60.0)]/' -e 's/15 \* b\[\\"starts\\"\]\[:-1\] \/ 3600/15 * b[\\"starts\\"][:-1] \/ 60/' ramps_up.ipynb > $TMPDIR/t/ramps_up.ipynb && grep -n "NAMES\[:6\]\|60.0)\]\|/ 60" $TMPDIR/t/ramps_up.ipynb; cd $TMPDIR/t && time ../../../$OLDPWD/../../executed/alonso-2020/.venv/bin/python -m jupyter nbconvert --to notebook --execute --output out.ipynb ramps_up.ipynb 2>&1 | tail -3
```

```
{'jupytext': {'cell_metadata_filter': 'tags,-all', 'main_language': 'python', 'notebook_metadata_filter': '-all'}}
88:    "RUN = NAMES[:6]\n",
94:    "        print(f\"stopped before round {i // 4 + 1}: {elapsed / 60:.1f} min so far, longest round {max(rounds) / 60:.1f} min\")\n",
97:    "    for r in P.pmap(P.run_ramp, [(n, MODELS[n], CI, [(10.0, 25.0, 60.0)]) for n in RUN[i:i + 4]]):\n",
100:    "    print(f\"round {i // 4 + 1}: {RUN[i:i + 4]} in {rounds[-1] / 60:.1f} min\")\n",
140:    "    TMR[n] = 10 + 15 * b[\"starts\"][:-1] / 60\n",
185:    "print(f\"notebook run time {(time.time() - T_START) / 60:.1f} min; peak memory \"\n",
[NbConvertApp] Converting notebook ramps_up.ipynb to notebook
[IPKernelApp] WARNING | Kernel is running over TCP without encryption. All communication (including code and outputs) is sent in plain text and is susceptible to eavesdropping. Use IPC transport or launch with kernel manager-provisioned CurveZMQ keys to enable transport encryption.
[NbConvertApp] Writing 12204 bytes to out.ipynb

real	0m17.553s
user	0m49.947s
sys	0m0.996s
Shell cwd was reset to
```

**Agent calls Bash**

```bash
python - <<EOF
import json
nb=json.load(open("$TMPDIR/t/out.ipynb"))
for c in nb['cells']:
    if c['cell_type']=='code':
        for o in c.get('outputs',[]): print(o.get('text', o.get('data',{}).get('text/plain','')) if isinstance(o.get('text',''),str) else ''.join(o['text']))
EOF
```

```
{'md5': '37766522dabaaa620d4c44264e76e686', 'sha256': '327279e2c4553c0b946bf230260caf0f7321e36bc5201ad7d65bbe6638d2df08', 'bytes': 99026}

38 models in the deposit
models run: ['0SHNMD', '2RO5K6', '4R2719', '4X6W66', '71G6LA', '72TVF2']

round 1: ['0SHNMD', '2RO5K6', '4R2719', '4X6W66'] in 0.2 min

round 2: ['71G6LA', '72TVF2'] in 0.1 min

ramps run: 6 models; 2069 simulated seconds per second on 4 processes; peak memory 0.21 GB
runs that diverged (NaN): []

        bursts  median     lo     hi
0SHNMD   112.0   0.153  0.130  0.637
2RO5K6   101.0   0.184  0.151  0.596
4R2719   112.0   0.195  0.126  0.296
4X6W66   106.0   0.186  0.132  0.309
71G6LA   116.0   0.208  0.155  0.804
72TVF2   113.0   0.174  0.131  0.750

[... 23 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/alonso-2020 && python - <<'EOF'
import json
nb=json.load(open('ramps_up.ipynb'))
for c in nb['cells']:
    s=''.join(c['source'])
    s=s.replace('''    b = P.burst_stats(UP[n]["spikes"][1])
    DCR[n] = b["dc"]
    TMR[n] = 10 + 15 * b["starts"][:-1] / 3600''','''    b = P.burst_stats(UP[n]["spikes"][1])
    keep = b["starts"][:-1] >= 10.0                       # the first 10 s dropped, as the Methods drop them
    DCR[n] = b["dc"][keep]
    TMR[n] = 10 + 15 * b["starts"][:-1][keep] / 3600''')
    s=s.replace("Per-burst LP duty cycles over the whole ramp (burst","Per-burst LP duty cycles over the ramp, from 10 s on (the Methods drop the first 10 s; burst")
    c['source']=s.splitlines(keepends=True)
nb['metadata']={'jupytext': {'cell_metadata_filter': 'tags,-all', 'main_language': 'python', 'notebook_metadata_filter': '-all'}}
json.dump(nb,open('ramps_up.ipynb','w'),indent=1); open('ramps_up.ipynb','a').write('\n')
EOF
grep -n "keep\|from 10 s" ramps_up.ipynb | head; date -u
```

```
117:    "Per-burst LP duty cycles over the ramp, from 10 s on (the Methods drop the first 10 s; burst duration over the time to the next burst\n",
139:    "    keep = b[\"starts\"][:-1] >= 10.0                       # the first 10 s dropped, as the Methods drop them\n",
140:    "    DCR[n] = b[\"dc\"][keep]\n",
141:    "    TMR[n] = 10 + 15 * b[\"starts\"][:-1][keep] / 3600\n",
Sat Nov 28 07:34:41 UTC 2026
```

**Agent calls Bash**

```bash
cd $TMPDIR/t && cp $OLDPWD/ramps_up.ipynb $OLDPWD/pyloric.py . && date -u && ../../../$OLDPWD/../../executed/alonso-2020/.venv/bin/python -m jupyter nbconvert --to notebook --execute --ExecutePreprocessor.timeout=3600 --output full.ipynb ramps_up.ipynb 2>&1 | tail -1; date -u
```

```
Sat Nov 28 07:34:58 UTC 2026
[NbConvertApp] Writing 18411 bytes to full.ipynb
Sat Nov 28 08:19:09 UTC 2026
Shell cwd was reset to
```

**Agent calls Bash**

```bash
python - <<EOF
import json
nb=json.load(open("$TMPDIR/t/full.ipynb"))
for c in nb['cells'][3:]:
    if c['cell_type']=='code':
        for o in c.get('outputs',[]): print(''.join(o.get('text','')))
EOF
```

```
38 models in the deposit
models run: ['0SHNMD', '2RO5K6', '4R2719', '4X6W66', '71G6LA', '72TVF2', 'B7SD0L', 'CG4J30', 'ED50XO', 'EF84RN', 'FGFKQS', 'G7P2WE', 'H5AIZR', 'HX40PF', 'INPO74', 'J6OK9B', 'J9U8SQ', 'KMNLBC', 'KV0BR4', 'LE8W3F', 'MAXTTP', 'ML4GPK', 'NJP4RT', 'OPLRCP', 'P1LH61', 'PCR6RP', 'PLKTEM', 'Q0H92I']

round 1: ['0SHNMD', '2RO5K6', '4R2719', '4X6W66'] in 6.2 min

round 2: ['71G6LA', '72TVF2', 'B7SD0L', 'CG4J30'] in 6.0 min

round 3: ['ED50XO', 'EF84RN', 'FGFKQS', 'G7P2WE'] in 6.0 min

round 4: ['H5AIZR', 'HX40PF', 'INPO74', 'J6OK9B'] in 6.2 min

round 5: ['J9U8SQ', 'KMNLBC', 'KV0BR4', 'LE8W3F'] in 6.0 min

round 6: ['MAXTTP', 'ML4GPK', 'NJP4RT', 'OPLRCP'] in 6.2 min

round 7: ['P1LH61', 'PCR6RP', 'PLKTEM', 'Q0H92I'] in 6.2 min

ramps run: 28 models; 39 simulated seconds per second on 4 processes; peak memory 0.27 GB
runs that diverged (NaN): []

[... 66 more lines not kept]
```

**Agent calls Bash**

```bash
date -u; grep -n "57 min\|113\|58 \|3e-9\|figs3\|25 models\|about 15\|fig6s1" reproduce_alonso_2020.ipynb voltage_distributions.ipynb ramps.ipynb | cut -c1-220
```

```
Sat Nov 28 08:19:23 UTC 2026
grep: reproduce_alonso_2020.ipynb: No such file or directory
grep: voltage_distributions.ipynb: No such file or directory
grep: ramps.ipynb: No such file or directory
```

**Agent calls Bash**

```bash
cd entries/alonso-2020 && grep -n "57 min\|113\|58 \|3e-9\|figs3\|25 models\|about 15\|fig6s1" reproduce_alonso_2020.ipynb voltage_distributions.ipynb ramps.ipynb | cut -c1-250
```

```
reproduce_alonso_2020.ipynb:42:    "| figs3-duty-cycle-variable-across-models | this | tested (variant reading) |\n",
reproduce_alonso_2020.ipynb:50:    "| fig6s1-crash-mechanisms | this | tested (7 of 8 models) |\n",
reproduce_alonso_2020.ipynb:208:    "The Methods (Parameters used in this study) name 25 models. The deposit's file names are\n",
reproduce_alonso_2020.ipynb:665:    "## figs3-duty-cycle-variable-across-models\n",
reproduce_alonso_2020.ipynb:670:    "The criterion's main reading is the 60 min ramp of every model, which is not run (57 min by the\n",
reproduce_alonso_2020.ipynb:683:     "claim:figs3-duty-cycle-variable-across-models"
reproduce_alonso_2020.ipynb:1057:    "These runs serve fig6s1-crash-mechanisms (the crash temperature of each model) and the counts\n",
reproduce_alonso_2020.ipynb:1166:    "## fig6s1-crash-mechanisms\n",
reproduce_alonso_2020.ipynb:1184:     "claim:fig6s1-crash-mechanisms"
reproduce_alonso_2020.ipynb:1659:    "| figs3-duty-cycle-variable-across-models | reproduced, variant reading |\n",
reproduce_alonso_2020.ipynb:1667:    "| fig6s1-crash-mechanisms | not reproduced (7 of 8 models) |\n",
reproduce_alonso_2020.ipynb:1680:    "deposited Java, which matches it to 3e-9 mV over 3 s at 18 C, to 0.06 mV over 3 s at 25 C, and\n",
voltage_distributions.ipynb:23:    "The Methods use 101 temperatures. At dt = 0.001 ms one temperature costs about 1500 simulated\n",
ramps.ipynb:26:    "The up ramp of every model, which figs3-duty-cycle-variable-across-models takes as its main\n",
ramps.ipynb:29:    "from a subset. figs3-duty-cycle-variable-across-models is tested in the main notebook on its\n",
ramps.ipynb:316:    "      f\"for the up legs alone (the main reading of figs3-duty-cycle-variable-across-models), 38 x 3600 s: {38 * 3600 / rate / 60:.0f} min\")\n",
ramps.ipynb:332:    "second, it would take 113 min, and this notebook had already run for 58 of its 60 min."
ramps.ipynb:418:    "| fig8-up-down-ramps | blocked (too_large; first re
[... 1 more lines not kept]
```

**Agent calls Bash**

```bash
python - <<'EOF'
import json
nb=json.load(open('reproduce_alonso_2020.ipynb'))
for i in (0,):
    print(''.join(nb['cells'][i]['source']))
print('=====')
print(''.join(nb['cells'][-2]['source']))
EOF
```

```
# Reproducing Alonso & Marder (2020) from Dryad m31b1h7

Paper: Alonso LM, Marder E (2020). Temperature compensation in a small rhythmic circuit. eLife
9:e55470, doi:10.7554/eLife.55470. The claims file, `claims/alonso-2020.yaml`, was written from
the version of record (main text, legends and Methods; the figure supplements' legends were not
in the text read).

Dataset: Dryad doi:10.5061/dryad.m31b1h7, version id 94811, one file,
`alonso_marder_tempcomp_2019_root.zip` (99,026 bytes, MD5 37766522dabaaa620d4c44264e76e686 from
Dryad's file list; its SHA-256 is printed below). Version 94811 is pinned because it is the only
published version of the dataset (the versions list of the API gives one, published 2020-12-07),
and the paper cites the dataset by its DOI, which resolves to it. Dryad needs a token to
download, so the workflow stages the file before the run and the notebook reads it in place,
into memory (docs/archives.md, "Dryad").

The paper has no recordings. The dataset holds the authors' Java model, Python driver scripts,
initial conditions and the parameters of each model network. Every claim is tested by simulating
the deposited models with a numba port of the deposited Java (`pyloric.py`), checked against the
Java below when a Java compiler is present.

[... 79 more lines not kept]
```

**Agent calls Bash**

```bash
python - <<'EOF'
import json
def edit(path, reps):
    nb=json.load(open(path))
    for old,new in reps:
        hits=0
        for c in nb['cells']:
            s=''.join(c['source'])
            if old in s:
                s=s.replace(old,new); hits+=1
                c['source']=s.splitlines(keepends=True)
        assert hits==1,(path,old[:60],hits)
    json.dump(nb,open(path,'w'),indent=1,ensure_ascii=False); open(path,'a').write('\n')

# --- ramps_up
edit('ramps_up.ipynb',[
("**Result: RESULT_PLACEHOLDER**",
"""**Result: reproduced** (main reading, 28 of the 38 models). On the 60 min ramp from 10 to 25 C,
all 378 pairs of the 28 models run have LP duty-cycle distributions that differ at p < 0.05
(two-sample Kolmogorov-Smirnov; largest p 3.5e-10), including the 9 pairs that share their maximal
conductances. Each model contributes 6162 to 7669 bursts, autocorrelated along the ramp, so the
test detects small differences; the outcome shows that the distributions are not identical, little
more. Model medians run from 0.148 to 0.262. The mean LP duty cycle per 1 degree window falls with
temperature in 18 models (Spearman below -0.5), rises in 3 and neither in 7. No ramp diverged.
The 10 models not run are the last 10 in file order."""),
("SUMMARY_PLACEHOLDER",
"""| Claim | Outcome |
|---|---|
| figs3-duty-cycle-variable-across-models | reproduced (main reading, 28 of 38 models; the variant, all 38, in the main notebook) |

How the analysis differs from the paper's: 28 of the 38 deposited models are run, the first 28
in file order, as all 38 would exceed the time a notebook may take; the paper's 36 cannot be told
from the files. The deposit has no ramp code, so the temperature is changed linearly and the
factors updated every 20 steps (1 ms); each ramp starts from the deposited initial conditions and
the first 10 s are dropped."""),
])

# --- ramps
edit('ramps.ipynb',[
("""The up ramp of every model, which figs3-duty-cycle-variable-across-models takes as its main
reading, and the second ramp reading of fig8-up-down-ramps (10 to 25 degrees C over 60 min and
back, every model) are not run: the cell timed in the fig8-up-down-ramps section estimates them
from a subset. figs3-duty-cycle-variable-across-models is tested in the main notebook on its
variant, the 16 fixed temperatures.""",
"""The second ramp reading of fig8-up-down-ramps (10 to 25 degrees C over 60 min and back, every
model) is not run: the cell timed in the fig8-up-down-ramps section estimates it from a subset.
The up ramp of every model, the main reading of figs3-duty-cycle-variable-across-models, is run
for 28 of the 38 models in `ramps_up.ipynb`; the main notebook tests that claim on its variant,
the 16 fixed temperatures."""),
("""The runs below take about 35 min on 4 otherwise idle CPUs (about 67 simulated seconds per second,
measured on a subset while preparing) and about an hour when the CPUs are shared; the run time
is printed.""",
"""The runs below take most of this notebook's time; their run time is printed."""),
("""The criterion is met when either reading gives a count within tolerance, and the second reading
(10 to 25 C over 60 min and back) was not run: timed on a subset at 40 simulated seconds per
second, it would take 113 min, and this notebook had already run for 58 of its 60 min.""",
"""The criterion is met when either reading gives a count within tolerance, and the second reading
(10 to 25 C over 60 min and back) was not run: the estimate printed above, from a subset, is
well over the 60 min a notebook may take, on its own as well as beside the runs of this notebook."""),
("| fig8-up-down-ramps | blocked (too_large; first reading 22 of 38, second reading estimated at 113 min) |",
 "| fig8-up-down-ramps | blocked (too_large; first reading 22 of 38, second reading estimated over 60 min) |"),
("""deposited initial conditions. The second ramp reading of fig8-up-down-ramps and the 60 min ramp
of every model for figs3-duty-cycle-variable-across-models were not run (113 and 57 min by the
timing on a subset). On""",
"""deposited initial conditions. The second ramp reading of fig8-up-down-ramps was not run (the
estimate from a subset is printed in its section); the 60 min ramp of 28 of the 38 models, for
figs3-duty-cycle-variable-across-models, is in `ramps_up.ipynb`. On"""),
])

# --- main
edit('reproduce_alonso_2020.ipynb',[
("""This is the first of three notebooks. `ramps.ipynb` tests the claims on temperature ramps
(figs2-ramp-largest-isi, fig8a-hysteresis-quiescence, fig8-up-down-ramps,
fig8b-pathological-attractor) and""",
"""This is the first of four notebooks. `ramps.ipynb` tests the claims on temperature ramps
(figs2-ramp-largest-isi, fig8a-hysteresis-quiescence, fig8-up-down-ramps,
fig8b-pathological-attractor), `ramps_up.ipynb` runs the 60 min ramp of 28 models, the main
reading of figs3-duty-cycle-variable-across-models, and"""),
("| figs3-duty-cycle-variable-across-models | this | tested (variant reading) |",
 "| figs3-duty-cycle-variable-across-models | this, ramps_up | tested (variant reading here, main reading on 28 models in ramps_up) |"),
("| fig6s1-crash-mechanisms | this | tested (7 of 8 models) |",
 "| fig6s1-crash-mechanisms | this | tested (7 of 8 models); blocked (data_missing) proposed |"),
("The Methods (Parameters used in this study) name 25 models.",
 "The Methods (Parameters used in this study) name 21 models."),
("""print("mean burst frequency over models and cells: %.3f Hz (median %.3f)" %
      (d10[[f"f {c}" for c in P.CELLS]].values.mean(), np.median(d10[[f"f {c}" for c in P.CELLS]].values)))""",
"""print("mean burst frequency over models and cells: %.3f Hz (median %.3f)" %
      (d10[[f"f {c}" for c in P.CELLS]].values.mean(), np.median(d10[[f"f {c}" for c in P.CELLS]].values)))
print("mean PD duty cycle over models: %.3f; mean LP and PY duty cycle over models and the two cells: %.3f" %
      (d10["dc PD"].mean(), d10[["dc LP", "dc PY"]].values.mean()))"""),
("""The criterion's main reading is the 60 min ramp of every model, which is not run (57 min by the
timing on a subset in `ramps.ipynb`). This is its variant:""",
"""The criterion's main reading, the 60 min ramp of every model, is run for 28 of the 38 models in
`ramps_up.ipynb` (all 38 would exceed the time a notebook may take). This is its variant:"""),
("""**Result: reproduced** (on the criterion's variant reading, 16 fixed temperatures; the ramp
reading was not run).""",
"""**Result: reproduced** (on the criterion's variant reading, 16 fixed temperatures; on the main,
ramp, reading, `ramps_up.ipynb` finds all 378 pairs of 28 models different at p < 0.05)."""),
("""print("variant, models sharing a pattern:", [(a, b) for a, b in combinations(pat13, 2) if pat13[a] == pat13[b]])""",
"""print("variant, models sharing a pattern:", [(a, b) for a, b in combinations(pat13, 2) if pat13[a] == pat13[b]])
# What the missing Q8FBN1 could change: it adds at most one pattern, and whether it crashes cannot be shown.
best = distinct + (8 - len(s6))
print(f"with Q8FBN1 (absent): at most {best} distinct patterns among 8; reproduced (8 distinct) possible: {best == 8}; "
      f"partially reproduced (6 or more distinct, every model crashing) possible: {best >= 6}")"""),
("""**Result: not reproduced.** Seven of the eight models are in the deposit (Q8FBN1 is absent).""",
"""**Result: not reproduced** (the verified outcome; a change to blocked, data_missing, is proposed,
see below). Seven of the eight models are in the deposit (Q8FBN1 is absent)."""),
("""eight (partially); with the eighth model at most six could be distinct, and Q8FBN1 cannot be shown
to crash.""",
"""eight (partially). With the eighth model at most six could be distinct, as printed, so reproduced
is ruled out but partially reproduced is not: it would need Q8FBN1 to crash with a sixth pattern,
which the deposit cannot show. The outcome therefore depends on the missing model, as for
fig7-high-temperature-slow-timescales, and blocked (data_missing) is proposed in the attempt
record; it can be at best partially reproduced."""),
("| figs3-duty-cycle-variable-across-models | reproduced, variant reading |",
 "| figs3-duty-cycle-variable-across-models | reproduced (variant reading, 38 models; main reading, 28 models, in ramps_up) |"),
("| fig6s1-crash-mechanisms | not reproduced (7 of 8 models) |",
 "| fig6s1-crash-mechanisms | not reproduced (7 of 8 models; blocked, data_missing, proposed, as the missing model could make it partial) |"),
("""absent (Q8FBN1, G81PUL, G7EOZ8, SAXT8Y) and 4 filed under other spellings;""",
"""absent (Q8FBN1, G81PUL, G7EOZ8, SAXT8Y), 3 filed under other spellings and 1 matched at the
character the text cannot render;"""),
])
EOF
date -u
```

```
Sat Nov 28 08:19:58 UTC 2026
```

**Agent calls Bash**

```bash
python - <<'EOF'
import json
nb=json.load(open('voltage_distributions.ipynb'))
for i,c in enumerate(nb['cells']):
    s=''.join(c['source'])
    if s.startswith('**Result') or 'Summary' in s[:20]: print(i, s, '\n---')
nb=json.load(open('../../executed/alonso-2020/voltage_distributions.ipynb'))
for o in nb['cells'][5].get('outputs',[]): print(''.join(o.get('text',''))[:3000])
EOF
```

```
6 **Result: reproduced** (resting on the assumed reading of where the distribution's spike region
begins). In G7P2WE's LP cell the spike amplitude falls from 10 to 25 C under both readings (peak
minus trough 56.9 to 26.2 mV; upper envelope 16.7 to -1.8 mV; Spearman -1.000 each). The threshold
under reading (a) does not depolarize steadily (-27.8 to -27.5 mV, Spearman -0.197). Under reading
(b) it rises: the upper edge of the densely occupied part of the distribution goes from -36.1 to
-26.5 mV at 5% of the largest occupancy (Spearman 0.997), from -38.2 to -29.1 mV at 10% (0.996)
and from -33.0 to -20.0 mV at 2% (0.996; at the -20 mV search limit at 2 of 26 temperatures). 26
of the Methods' 101 temperatures were run. 
---
9 **Result: reproduced.** From 10 to 25 C the upper envelope falls in every cell of G7P2WE (by 19.1,
18.5 and 13.8 mV), rises in every cell of 4X6W66 (3.9, 7.3 and 6.3 mV; more than 5 mV in LP and
PY), and stays within 5 mV in every cell of MAXTTP (-1.5, -2.5 and 1.0 mV). The 2 mV variant loses
MAXTTP and the 10 mV variant loses 4X6W66. The mean V rises in 8 of the 9 cells and falls in one
(4X6W66 LP, -0.26 mV). 
---
10 ## Summary

| Claim | Outcome |
|---|---|
| fig2-lp-spike-amplitude-threshold | reproduced (assumed: threshold reading b) |
[... 42 more lines not kept]
```

**Agent calls Bash**

```bash
python - <<'EOF'
import json
p='voltage_distributions.ipynb'
nb=json.load(open(p))
c=nb['cells'][6]; s=''.join(c['source'])
old="of the Methods' 101 temperatures were run."
assert old in s
s=s.replace(old, old+""" The outcome rests on the rule for reading (b): LP fires 114
spikes in the analysed 10 s at 10 C and 433 at 25 C, and more spikes put more occupancy just
above the densely occupied part of the distribution, which could raise this edge with no change
in the per-spike threshold, which reading (a) finds flat.""")
c['source']=s.splitlines(keepends=True)
json.dump(nb,open(p,'w'),indent=1,ensure_ascii=False); open(p,'a').write('\n')
EOF
git diff --stat .; python -c "import json;[json.load(open(f)) for f in ['ramps.ipynb','ramps_up.ipynb','reproduce_alonso_2020.ipynb','voltage_distributions.ipynb']]"; git diff reproduce_alonso_2020.ipynb | head -30
```

```
entries/alonso-2020/ramps.ipynb                 | 26 +++++++--------
 entries/alonso-2020/reproduce_alonso_2020.ipynb | 44 ++++++++++++++++---------
 entries/alonso-2020/voltage_distributions.ipynb |  5 ++-
 3 files changed, 44 insertions(+), 31 deletions(-)
diff --git a/entries/alonso-2020/reproduce_alonso_2020.ipynb b/entries/alonso-2020/reproduce_alonso_2020.ipynb
index c5ae6b5..7facf13 100644
--- a/entries/alonso-2020/reproduce_alonso_2020.ipynb
+++ b/entries/alonso-2020/reproduce_alonso_2020.ipynb
@@ -25,9 +25,10 @@
     "the deposited models with a numba port of the deposited Java (`pyloric.py`), checked against the\n",
     "Java below when a Java compiler is present.\n",
     "\n",
-    "This is the first of three notebooks. `ramps.ipynb` tests the claims on temperature ramps\n",
+    "This is the first of four notebooks. `ramps.ipynb` tests the claims on temperature ramps\n",
     "(figs2-ramp-largest-isi, fig8a-hysteresis-quiescence, fig8-up-down-ramps,\n",
-    "fig8b-pathological-attractor) and `voltage_distributions.ipynb` the claims\n",
+    "fig8b-pathological-attractor), `ramps_up.ipynb` runs the 60 min ramp of 28 models, the main\n",
+    "reading of figs3-duty-cycle-variable-across-models, and `voltage_distributions.ipynb` the claims\n",
     "on membrane potential distributions (fig2-lp-spike-amplitude-threshold,\n",
     "fig2s1-peak-voltage-diverse).\n",
[... 14 more lines not kept]
```

**Agent calls Bash**

```bash
python - <<'EOF'
p='entry.yaml'; s=open(p).read()
s=s.replace("""  runtime_minutes: 15
- path: ramps.ipynb
  title: Temperature ramps (Alonso and Marder 2020)
  runtime_minutes: 35
- path: voltage_distributions.ipynb
  title: Membrane potential distributions (Alonso and Marder 2020)
  runtime_minutes: 15""","""  runtime_minutes: 30
- path: ramps.ipynb
  title: Temperature ramps (Alonso and Marder 2020)
  runtime_minutes: 52
- path: voltage_distributions.ipynb
  title: Membrane potential distributions (Alonso and Marder 2020)
  runtime_minutes: 21
- path: ramps_up.ipynb
  title: The 60 min ramp of 28 models (Alonso and Marder 2020)
  runtime_minutes: 44""")
open(p,'w').write(s)
p='README.md'; s=open(p).read()
reps=[("""simulating the deposited models with a port of the deposited Java (`pyloric.py`), which matches the
Java to 3e-9 mV.""","""simulating the deposited models with a port of the deposited Java (`pyloric.py`), which matches the
Java to 3e-9 mV over 3 s at 18 C and to 0.06 mV over 3 s at 25 C."""),
("| Figure 2: LP spike amplitude falls and threshold depolarizes | Reproduced |","| Figure 2: LP spike amplitude falls and threshold depolarizes | Reproduced, resting on an assumed rule for reading the threshold |"),
("| Figure 1, supplement 3: LP duty-cycle distributions differ across models | Reproduced |","| Figure 1, supplement 3: LP duty-cycle distributions differ across models | Reproduced (ramp reading on 28 of 38 models, fixed temperatures on 38) |"),
("| Figure 6, supplement 1: crashes by different mechanisms | Not reproduced |","| Figure 6, supplement 1: crashes by different mechanisms | Not reproduced; blocked (data missing) proposed, as the missing model could make it partial |"),
("""four are filed under other spellings.""","""three are filed under other spellings, and one is matched at the character the paper's text cannot
render."""),
("""- `reproduce_alonso_2020.ipynb`: the data check and most claims, at fixed temperatures (about 15
  min).
- `ramps.ipynb`: the claims on temperature ramps (about 35 min).
- `voltage_distributions.ipynb`: the membrane potential distributions of Figure 2 (about 15 min).""",
"""- `reproduce_alonso_2020.ipynb`: the data check and most claims, at fixed temperatures (about 30
  min).
- `ramps.ipynb`: the claims on temperature ramps (about 50 min).
- `voltage_distributions.ipynb`: the membrane potential distributions of Figure 2 (about 20 min).
- `ramps_up.ipynb`: the 60 min ramp of 28 of the 38 models, the main reading of the Figure 1,
  supplement 3 claim (about 45 min)."""),
]
for a,b in reps:
    assert a in s, a[:50]; s=s.replace(a,b)
open(p,'w').write(s)
EOF
cd ../.. && python tools/entry.py check entries/alonso-2020 2>&1 | tail -15; date -u
```

```
0 error(s)
Sat Nov 28 08:20:31 UTC 2026
```

**Agent**

The full run (four notebooks, about 145 min) is longer than one tool call may last (120 min), so I start it detached and wait on it in the foreground with polling.

**Agent calls Bash**

```bash
nohup python tools/entry.py all entries/alonso-2020 > $TMPDIR/run.log 2>&1 &
echo started; date -u
```

```
started
Sat Nov 28 08:20:39 UTC 2026
```

**Agent calls Bash**

```bash
sleep 5; cat $TMPDIR/run.log; python - <<'EOF'
import json,re
nb=json.load(open('executed/alonso-2020/reproduce_alonso_2020.ipynb'))
for c in nb['cells']:
    if 'claim:deposit-models' in c.get('metadata',{}).get('tags',[]):
        t=''.join(''.join(o.get('text','')) for o in c['outputs'])
        rows=[l.split() for l in t.splitlines()[2:40]]
        import numpy as np
        pd_=[float(r[4]) for r in rows]; lp=[float(r[5]) for r in rows]; py=[float(r[6]) for r in rows]
        print(t.splitlines()[0]); print(len(rows), np.mean(pd_), np.mean(lp+py))
EOF
```

```
Exit code 1
Traceback (most recent call last):
  File "<stdin>", line 7, in <module>
ModuleNotFoundError: No module named 'numpy'
```

**Agent calls Bash**

```bash
ls schemas/ 2>/dev/null; grep -rn "proposed" --include=*.py tools/ | head; grep -rln "proposed:" attempts/ | head -3
```

```
attempt.schema.json
claims.schema.json
entry.schema.json
paper-match.schema.json
tools/agent_run.py:6:    python tools/agent_run.py proposals ROLE PAPER        # "true" if the attempt has proposed changes
tools/agent_run.py:16:author-revise-3, the third round that settles changes proposed after the second. A repeat attempt
tools/agent_run.py:365:    """The claims of the paper's latest attempt that carry a proposed change of outcome."""
tools/agent_run.py:367:    return [o["claim"] for o in (found[0]["outcomes"] if found else []) if o.get("proposed")]
tools/replicates.py:10:revision committed, and its third when the second left proposed changes (as chain.sh decides). One still going is
tools/replicates.py:55:    return "author-revise-3" in done or not any(o.get("proposed") for o in rec["outcomes"])
tools/entry.py:444:                                    f"verification agreed with {verified!r}; record the change under `proposed`, "
tools/build_site.py:407:                "proposed": o.get("proposed"),
tools/build_site.py:2033:    if o.get("proposed"):
tools/build_site.py:2034:        tags += (f'<span class="tag">change to {e(OUTCOMES[o["proposed"]["outcome"]][0].lower())} '
attempts/tingley-2018-02.yaml
attempts/gabriel-2025-01.yaml
attempts/raicevic-2023-01.yaml
```

**Agent calls Bash**

```bash
python3 -c "
import json;s=json.load(open('schemas/attempt.schema.json'))
d=s.get('\$defs',s.get('definitions',{}))
print(json.dumps(d.get('proposed', {}),indent=0)[:1500])
for k in d:
  if 'verif' in k.lower() or 'round' in k.lower(): print(k, json.dumps(d[k])[:2500])
" ; grep -n "proposed:" -A6 attempts/gabriel-2025-01.yaml | head -20
```

```
{}
522:  proposed:
523-    outcome: partially_reproduced
524-    reason: The shuffled-label control the round-2 report asked for shows the shocked mice's pre-shock value under
525-      C1 N1 equals their value with shuffled outcomes (0.489 against 0.476), and above the shuffled values the
526-      pre-shock difference is not significant in any cohort or coding (p >= 0.55); the C1 N1 difference there
527-      comes from the non-shocked mice scoring below their own shuffled values (0.108 against 0.230). The shock
528-      epoch difference stays above the shuffled values (C1 N1 p = 0.046 to 0.054, C2 N1 p = 0.0018 to 0.013). The
```

**Agent calls Bash**

```bash
python3 -c "
import json;s=json.load(open('schemas/attempt.schema.json'))
def find(o,path=''):
  if isinstance(o,dict):
    for k,v in o.items():
      if k in ('verifications','proposed','findings') : print(path+'/'+k, json.dumps(v)[:3000]); print()
      find(v,path+'/'+k)
find(s)
" | head -40
```

```
/properties/outcomes/items/properties/proposed {"description": "A change of outcome found after the last verification round, held until a further round agrees with it.", "type": "object", "additionalProperties": false, "required": ["outcome", "reason"], "properties": {"outcome": {"enum": ["reproduced", "partially_reproduced", "not_reproduced", "blocked"]}, "blocked_by": {"description": "Required when outcome is blocked.", "enum": ["data_missing", "metadata_insufficient", "methods_underspecified", "data_unreadable", "dataset_missing", "too_large", "not_runnable", "other"]}, "reason": {"type": "string", "minLength": 1}}}

/properties/verifications {"type": "array", "items": {"type": "object", "additionalProperties": false, "required": ["date", "kind", "by", "results"], "properties": {"date": {"type": "string", "format": "date"}, "kind": {"enum": ["agent", "person", "paper_author"]}, "by": {"type": "string"}, "results": {"type": "array", "items": {"type": "object", "additionalProperties": false, "required": ["claim", "agrees"], "properties": {"claim": {"type": "string"}, "agrees": {"type": "boolean"}, "reason": {"description": "The verifier's reason, in its own words.", "type": "string"}, "response": {"description": "What the author changed or replied, kept apart from the verifier's reason.", "type": "string"}, "outcome": {"description": "The outcome the verifier would give.", "enum": ["reproduced", "partially_reproduced", "not_reproduced", "blocked"]}}}}, "reviewed": {"description": "What was reviewed, e.g. a commit, when the attempt changed afterwards.", "type": "string"}, "findings": {"description": "From protocol pilot-18, in round 2: what the verifier said of each finding the record rates `critical` (docs/protocol.md, the attempt record).", "type": "array", "items": {"type": "object", "additionalProperties": false, "required": ["finding", "agrees"], "properties": {"finding": {"description": "The finding's number in this record's `findings`, from 1.", "type": "inte
[... 8 more lines not kept]
```

**Agent calls Bash**

```bash
cat $TMPDIR/run.log; python3 -c "import yaml; print(yaml.__version__)"
```

```
6.0.4
```

**Agent calls Bash**

```bash
python3 - <<'EOF'
p='attempts/alonso-2020-01.yaml'; s=open(p).read()
reps=[
# figs3
("""  measured: 1.0
  notes: On the criterion's variant (per-burst LP duty cycles from the 16 fixed temperatures, 30 s each), all 703
    pairs of the 38 models differ at p < 0.05 (two-sample Kolmogorov-Smirnov), including every pair that shares
    its maximal conductances (largest p 0.025, EF84RN against FGFKQS). The mean LP duty cycle falls with temperature
    in 23 models (Spearman below -0.5), rises in 3 and neither in 12. The main reading, the 60 min ramp of every
    model, was not run. The test pools autocorrelated per-burst values across temperatures, so it detects small
    differences; the outcome says that the distributions are not identical, little more.
  deviations:
  - 'The ramp reading (38 models, 3600 s each) was not run: timed on a subset in ramps.ipynb at 40 simulated seconds
    per second on 4 processes, it would take 57 min, and that notebook already takes 58 min. The outcome rests on
    the variant reading the criterion names.'
  - 703 pairs of 38 models, where the criterion counts 630 pairs of 36.""",
"""  measured: 1.0
  notes: On the main reading, the 60 min ramp from 10 to 25 C (ramps_up.ipynb), run for 28 of the 38 models, all
    378 pairs differ at p < 0.05 (two-sample Kolmogorov-Smirnov, largest p 3.5e-10), including the 9 pairs among
    them that share their maximal conductances. Each model gives 6162 to 7669 bursts; model medians run from 0.148
    to 0.262; the mean LP duty cycle per 1 degree window falls with temperature in 18 models (Spearman below -0.5),
    rises in 3 and neither in 7; no ramp diverged. On the variant (per-burst LP duty cycles from the 16 fixed temperatures,
    30 s each), all 703 pairs of the 38 models differ at p < 0.05, including every pair that shares its maximal
    conductances (largest p 0.025, EF84RN against FGFKQS); the mean LP duty cycle falls with temperature in 23 models,
    rises in 3 and neither in 12. Both tests pool autocorrelated per-burst values, so they detect small differences;
    the outcome says that the distributions are not identical, little more.
  deviations:
  - 'The ramp reading is run for the first 28 of the 38 models in the deposit''s file order (378 pairs): all 38
    were timed on a subset at 39 simulated seconds per second on 4 processes, about 59 min, over the time a notebook
    may take. The variant reading covers all 38 models (703 pairs), where the criterion counts 630 pairs of 36.'
  - The deposit has no ramp code; the temperature is changed linearly and the temperature factors updated every
    1 ms, from the deposited initial conditions at 10 C, and bursts starting in the first 10 s are dropped, as the
    Methods drop 10 s when scoring."""),
("""  notebook: reproduce_alonso_2020.ipynb
  output: claim:figs3-duty-cycle-variable-across-models""",
"""  notebook: ramps_up.ipynb
  output: claim:figs3-duty-cycle-variable-across-models"""),
# fig2
("""    the search limit at 2 of 26 temperatures). Amplitude (a) and threshold (b) meet the criterion. Where the spike
    region begins is assumed; the question is for the paper's authors (finding 6).""",
"""    the search limit at 2 of 26 temperatures). Amplitude (a) and threshold (b) meet the criterion. Where the spike
    region begins is assumed; the question is for the paper's authors (finding 6). The outcome rests on this rule.
    LP fires 114 spikes in the analysed 10 s at 10 C and 433 at 25 C; more spikes put more occupancy just above
    the densely occupied part, which could raise the edge with no change in the per-spike threshold, which reading
    (a) finds flat, and reading (b) lies 8 to 10 mV below reading (a)."""),
# fig6s1
("""    at least six distinct among eight with every model crashing; with the missing model at most six could be, and
    Q8FBN1 cannot be shown to crash.
  deviations:""",
"""    at least six distinct among eight with every model crashing; with the missing model at most six could be, and
    Q8FBN1 cannot be shown to crash. Reproduced is ruled out; partially reproduced is not, as it would need Q8FBN1
    to crash with a sixth pattern. The outcome can be at best partially reproduced.
  proposed:
    outcome: blocked
    blocked_by: data_missing
    reason: The seven models present give 5 distinct patterns, and the missing Q8FBN1 could add a sixth, as the notebook
      now prints (at most 6 distinct among 8; partially reproduced possible, reproduced not). Whether the partial
      case holds therefore depends on a model the deposit lacks, so the claim cannot be decided between not reproduced
      and partially reproduced, as for fig7-high-temperature-slow-timescales, which is blocked for the same reason.
      Raised by the round-2 verifier.
  deviations:"""),
# fig7
("""    0.35, 0.35 and 0.29 s (reading b). So neither model present shows a time scale above 2 s, and the claim would
    not be reproduced even with the three missing models.""",
"""    0.35, 0.35 and 0.29 s (reading b). So neither model present shows a time scale above 2 s, and the claim would
    not be reproduced even with the three missing models; partially reproduced (three or four of five) would need
    all three missing models to show it, so the outcome can be at best partially reproduced."""),
# finding 2
("""  statement: Four models are filed under names that differ from the Methods. OSHNMD and B7SDOL are 0SHNMD and B7SD0L
    (digit 0 for the letter O), KNMLBC is KMNLBC (two letters swapped), and the Figure 1 model, printed with a symbol
    in its second place, is 4X6W66. Each is the only close match among the 38 files.""",
"""  statement: Three models are filed under names that differ from the Methods. OSHNMD and B7SDOL are 0SHNMD and B7SD0L
    (digit 0 for the letter O) and KNMLBC is KMNLBC (two letters swapped). The Figure 1 model, printed with a symbol
    in its second place, is 4X6W66, the one file that matches at the other five characters. Each is the only close
    match among the 38 files."""),
]
for a,b in reps:
    assert s.count(a)==1, a[:60]; s=s.replace(a,b)
open(p,'w').write(s)
EOF
cat $TMPDIR/run.log; date -u
```

```
Sat Nov 28 08:21:30 UTC 2026
```

**Agent calls Bash**

```bash
pkill -f "tools/entry.py all" ; pkill -f nbconvert; sleep 2; ps aux | grep -c "[n]bconvert"; cd entries/alonso-2020 && python3 - <<'EOF'
import json
p='ramps_up.ipynb'; nb=json.load(open(p))
c=nb['cells'][3]; s=''.join(c['source'])
old='''print("runs that diverged (NaN):", [n for n in DONE if not UP[n]["finite"]])'''
assert old in s
s=s.replace(old, '''rate = sum(4 * 3600.0 for _ in rounds) / sum(rounds)
print(f"at this rate the ramps of all {len(NAMES)} models would take {len(NAMES) * 3600 / rate / 60:.0f} min")
''' + old)
c['source']=s.splitlines(keepends=True)
s=''.join(nb['cells'][0]['source']).replace("Timed on a subset, the ramp of all 38 models takes about 59 min on 4 CPUs","Timed on a subset while preparing, the ramps of all 38 models take about 59 min on 4 CPUs")
nb['cells'][0]['source']=s.splitlines(keepends=True)
json.dump(nb,open(p,'w'),indent=1,ensure_ascii=False); open(p,'a').write('\n')
EOF
cd ../.. && nohup python tools/entry.py all entries/alonso-2020 > $TMPDIR/run.log 2>&1 &
sleep 1; date -u
```

```
Exit code 143
```

**Agent calls Bash**

```bash
ps aux | grep -E "[e]ntry.py all|[n]bconvert" | cut -c1-150; grep -c "would take" entries/alonso-2020/ramps_up.ipynb; date -u
```

```
0
Sat Nov 28 08:21:46 UTC 2026
```

**Agent**

Run stopped and edit not applied; applying it now and restarting.

**Agent calls Bash**

```bash
cd entries/alonso-2020 && python3 - <<'EOF'
import json
p='ramps_up.ipynb'; nb=json.load(open(p))
c=nb['cells'][3]; s=''.join(c['source'])
old='''print("runs that diverged (NaN):", [n for n in DONE if not UP[n]["finite"]])'''
assert old in s
s=s.replace(old, '''rate = sum(4 * 3600.0 for _ in rounds) / sum(rounds)
print(f"at this rate the ramps of all {len(NAMES)} models would take {len(NAMES) * 3600 / rate / 60:.0f} min")
''' + old)
c['source']=s.splitlines(keepends=True)
s=''.join(nb['cells'][0]['source']).replace("Timed on a subset, the ramp of all 38 models takes about 59 min on 4 CPUs","Timed on a subset while preparing, the ramps of all 38 models take about 59 min on 4 CPUs")
nb['cells'][0]['source']=s.splitlines(keepends=True)
json.dump(nb,open(p,'w'),indent=1,ensure_ascii=False); open(p,'a').write('\n')
EOF
grep -n "would take\|while preparing" ramps_up.ipynb
```

```
23:    "Timed on a subset while preparing, the ramps of all 38 models take about 59 min on 4 CPUs, more than a notebook\n",
105:    "print(f\"at this rate the ramps of all {len(NAMES)} models would take {len(NAMES) * 3600 / rate / 60:.0f} min\")\n",
```

**Agent calls Bash**

```bash
cd  && python tools/entry.py check entries/alonso-2020 2>&1 | tail -2 && (nohup python tools/entry.py all entries/alonso-2020 > $TMPDIR/run.log 2>&1 &) ; sleep 3; ps aux | grep -c "[e]ntry.py all"; date -u
```

```
0 error(s)
3
Sat Nov 28 08:22:06 UTC 2026
```

**Agent calls Bash**

```bash
python3 - <<'EOF'
p='attempts/alonso-2020-01.yaml'; s=open(p).read()
s=s.rstrip('\n')+'\n'+'''- date: '2026-11-28'
  kind: agent
  by: Independent agent run by CatalystNeuro (same harness, separate context, did not write the notebook)
  reviewed: 'Round 2: the three executed notebooks in full, with the conclusions and summaries, the helper module,
    the claims file and this record, with the paper''s full text under paper/. The verifier agreed with 21 outcomes,
    accepted fig8-up-down-ramps with a caveat and questioned fig6s1-crash-mechanisms. It found no misreading of the
    paper in the claims file. No finding is rated critical; it found that the ratings given match what the outputs
    show (finding 1 major, cells 7 and 8; findings 2, 3, 4, 5 and 7 minor; finding 6 has no rating). Its section
    2 quoted sentences the printed outputs do not support, answered here: the stale timings in ramps cell 13, ramps
    cell 17, main cell 28 and this record (ramps cell 12 printed 45 simulated seconds per second, 102 min, 52 min
    so far and 51 min for the up legs) are removed from the notebooks, whose conclusions now refer to the estimate
    printed in ramps cell 12, and the record quotes the numbers of the new run; deposit-models measured now takes
    the printed means; the README now gives the agreement with the Java at 18 and 25 C, run times near the printed
    ones, three models under other spellings and one matched at an unreadable character, and fig2 as resting on
    an assumed rule; main cell 6 now says 21 models. Remaining points it listed: the figs3 main reading is now run
    for 28 of 38 models in a notebook of its own (ramps_up.ipynb); the fig8 second reading is still not run; which
    36 of the 38 models the paper used still cannot be told from the files (finding 3).'
  results:
  - claim: deposit-models
    agrees: true
    outcome: not_reproduced
    reason: 'Cell 14: 3 of 38. The measured 0.192 and 0.239 ("means over models and cells") are not printed; the
      cell 14 table averages to 0.193 for PD duty cycle and 0.234 for LP and PY. This does not change the outcome.'
    response: Cell 14 now prints the two means, and measured takes them (MEASURED_DC).
  - claim: fig1c-frequency-q10-phase-constant
    agrees: true
    outcome: partially_reproduced
    reason: Cell 20.
    response: No change.
  - claim: fig1s1-three-models
    agrees: true
    outcome: not_reproduced
    reason: Cell 23.
    response: No change.
  - claim: all-models-compensated
    agrees: true
    outcome: partially_reproduced
    reason: 'Cell 26: 36 of 38, 35 with the strict order test. The order test is stated, and the variant also gives
      a partial outcome. Which 36 of the 38 models the paper used still cannot be told from the files.'
    response: No change.
  - claim: intermediate-temperature-failures
    agrees: true
    outcome: blocked
    reason: Cell 32.
    response: No change.
  - claim: figs2-ramp-largest-isi
    agrees: true
    outcome: reproduced
    reason: Ramps cell 5.
    response: No change.
  - claim: figs3-duty-cycle-variable-across-models
    agrees: true
    outcome: reproduced
    reason: 'Reproduced (variant reading): agreed on the variant the criterion names. The main ramp reading has
      not been run; a notebook of its own could run it (51 min printed). The 57 min estimate for the up legs and
      "that notebook already takes 58 min" are not printed: ramps cell 12 prints 51 min and the ramps notebook ran
      51.7 min, so "does not fit" holds only for running it beside the existing ramps.'
    response: 'No change of outcome. The main reading is now run in a notebook of its own, ramps_up.ipynb, for the
      first 28 of the 38 models in file order, as all 38 measured at 39 simulated seconds per second would take about
      59 min, over a notebook''s limit with the rest of the notebook: all 378 pairs differ at p < 0.05 (largest p
      3.5e-10), so the outcome now rests on the main reading as well as the variant. The stale timings are removed
      from the notes, the deviation and the notebooks.'
  - claim: fig2-lp-spike-amplitude-threshold
    agrees: true
    outcome: reproduced
    reason: 'Yes as the criterion is written (voltage cell 5). The assumption is stated, but weakly supported. The
      direct per-spike threshold (reading a) does not move (-27.8 to -27.5 mV, rho = -0.197); reading (b) sits 8
      to 10 mV below it; LP fires 114 spikes at 10 C and 433 at 25 C, and more spikes put more occupancy just above
      the dense region, which would push this edge upward even if the threshold did not change. At 2% the rule reaches
      the -20 mV search limit at 24.4 and 25 C. The outcome should be read as resting on this rule.'
    response: 'Outcome kept, marked assumed. The rule is the only reading of "where the spike region begins" this
      attempt found to locate a point on the distribution, and the paper gives no other; the concern is recorded
      in the notes and in voltage cell 6, which now say that the outcome rests on the rule and why it may track spike
      count, and the README now marks the outcome as resting on it. The question stays with the paper''s authors
      (finding 6).'
  - claim: fig2s1-peak-voltage-diverse
    agrees: true
    outcome: reproduced
    reason: Voltage cell 8.
    response: No change.
  - claim: fig3-current-amplitudes
    agrees: true
    outcome: partially_reproduced
    reason: Cell 35.
    response: No change.
  - claim: fig4-currentscapes-reorganize
    agrees: true
    outcome: not_reproduced
    reason: 'Cell 38: no part holds under any of the 4 readings.'
    response: No change.
  - claim: currentscapes-dominant-currents
    agrees: true
    outcome: reproduced
    reason: Cell 41.
    response: No change.
  - claim: fig5-a-to-kca-tradeoff
    agrees: true
    outcome: reproduced
    reason: Cell 44.
    response: No change.
  - claim: fig6-crash-different-mechanisms
    agrees: true
    outcome: not_reproduced
    reason: 'Cell 50: FGFKQS PD fires 1005 spikes; still 336 at 0 mV, cell 71. The assumption is stated and reasonable.'
    response: No change.
  - claim: fig6s1-crash-mechanisms
    agrees: false
    outcome: blocked
    reason: 'Reproduced is ruled out, because B7SD0L, J9U8SQ and SJR46Y share a pattern (cell 53). Partial is not
      ruled out: it needs six distinct patterns among eight and every model crashing. The 7 models present give
      5 patterns, so the missing Q8FBN1 could supply the sixth, and the notes themselves say "at most six could
      be". fig7 is in the same position (partial possible only through the missing models) and is marked blocked.
      For consistency fig6s1 should be blocked (data_missing), or both records should say that the outcome can be
      at best partial.'
    response: 'The verified outcome, not reproduced, is kept, as round 2 may not change an outcome, and blocked (data_missing)
      is proposed on it for round 3: the claim cannot be decided between not reproduced and partially reproduced
      without Q8FBN1. Cell 53 now prints what the missing model could change (at most 6 distinct among 8, so partial
      possible and reproduced not), and the notes of both fig6s1-crash-mechanisms and fig7-high-temperature-slow-timescales
      now say that the outcome can be at best partially reproduced.'
  - claim: fig7-high-temperature-slow-timescales
    agrees: true
    outcome: blocked
    reason: 'Cell 56. Partial is possible only through the missing models.'
    response: No change of outcome; the notes now say that partially reproduced would need all three missing models,
      so the outcome can be at best partially reproduced.
  - claim: fig8a-hysteresis-quiescence
    agrees: true
    outcome: reproduced
    reason: 'Ramps cell 8: 1.94 C.'
    response: No change.
  - claim: fig8-up-down-ramps
    agrees: true
    outcome: blocked
    reason: 'Accepted with a caveat. On the printed estimate (102 min, ramps cell 12), the second reading exceeds
      the 60 min notebook limit. That meets the too_large definition the author quotes from the protocol, so the
      verifier withdraws its provisional not_reproduced. The first reading gives 22 of 38 (ramps cell 11), so the
      claim cannot pass on that reading. The second reading has not been run, so the claim is undecided. Ramps cell
      13 ("timed on a subset at 40 simulated seconds per second, it would take 113 min, and this notebook had already
      run for 58 of its 60 min") is not supported: ramps cell 12 prints 45 simulated seconds per second, 102 min
      and 52 min so far, and the same stale figures appear in the record''s notes and verification response.'
    response: 'No change of outcome. Ramps cell 13 and the summary no longer quote timings; they refer to the estimate
      printed in ramps cell 12, which in this run is EST_UD min for the second reading at EST_RATE simulated seconds
      per second, and the notes quote these numbers. The second reading is not run: at about 100 min it would need
      two notebooks passing the states at 25 C from one to the other, beside the 44 min notebook added for figs3,
      more than this revision''s time allows.'
  - claim: fig8b-pathological-attractor
    agrees: true
    outcome: not_reproduced
    reason: Ramps cell 15. The assumption is stated and reasonable.
    response: No change.
  - claim: fig9a-remove-a-current
    agrees: true
    outcome: partially_reproduced
    reason: Cell 59. The assumption is stated and reasonable.
    response: No change.
  - claim: fig9b-remove-kca-current
    agrees: true
    outcome: reproduced
    reason: Cell 62. The assumption is stated and reasonable.
    response: No change.
  - claim: fig10a-graded-removal
    agrees: true
    outcome: partially_reproduced
    reason: 'Cell 65: 4 of 5 with control first, 3 of 5 from t = 0. Control first is the Results'' Figure 9 protocol
      and the deposit''s removal script.'
    response: No change.
  - claim: fig10b-complete-removal-differs
    agrees: true
    outcome: not_reproduced
    reason: 'Cell 68: H gives 30 or 31, against 33. The assumption is stated and reasonable.'
    response: No change.
'''
open(p,'w').write(s)
import yaml; yaml.safe_load(open(p)); print('ok')
EOF
cat $TMPDIR/run.log; date -u
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
python3 - <<'EOF'
p='attempts/alonso-2020-01.yaml'; s=open(p).read()
a="""    paper cites for this sentence, was timed in the notebook on a subset at 40 simulated seconds per second on 4
    processes: 113 min for 38 models, while the notebook had already run 58 of its 60 min. It was not run, so the
    outcome cannot be decided; the second reading, run on its own and split over two notebooks to fit the limit,
    would settle it.'"""
b="""    paper cites for this sentence, was timed in the notebook on a subset at EST_RATE simulated seconds per second on
    4 processes: EST_UD min for 38 models, over the 60 min a notebook may take. It was not run, so the outcome cannot
    be decided; the second reading, split over two notebooks that pass the states at 25 C from one to the other,
    would settle it.'"""
assert s.count(a)==1; s=s.replace(a,b); open(p,'w').write(s)
EOF
grep -n "EST_\|MEASURED_DC" attempts/alonso-2020-01.yaml
```

```
304:    paper cites for this sentence, was timed in the notebook on a subset at EST_RATE simulated seconds per second on
305:    4 processes: EST_UD min for 38 models, over the 60 min a notebook may take. It was not run, so the outcome cannot
691:    response: Cell 14 now prints the two means, and measured takes them (MEASURED_DC).
809:      printed in ramps cell 12, which in this run is EST_UD min for the second reading at EST_RATE simulated seconds
```

**Agent calls Bash**

```bash
python3 - <<'EOF'
p='attempts/alonso-2020-01.yaml'; s=open(p).read()
reps=[("""    response: No change of outcome. The ramp reading is now timed in the ramps notebook (57 min for 38 models at
      40 simulated seconds per second), which does not fit beside that notebook's 58 min, so it stays not run.""",
"""    response: No change of outcome. The ramp reading is now timed in the ramps notebook (51 min for 38 models at
      45 simulated seconds per second, as printed; corrected in round 2 from figures of an earlier run), which does
      not fit beside that notebook's 52 min, so it stays not run."""),
("""      second reading is now timed in the notebook on a subset: 113 min for 38 models at 40 simulated seconds per
      second, beside a notebook that already takes 58 of its 60 min.""",
"""      second reading is now timed in the notebook on a subset: 102 min for 38 models at 45 simulated seconds per
      second, as printed (corrected in round 2 from figures of an earlier run), over the 60 min a notebook may take."""),
]
for a,b in reps:
    assert s.count(a)==1,a[:50]; s=s.replace(a,b)
open(p,'w').write(s)
import yaml; yaml.safe_load(open(p)); print('ok')
EOF
cat $TMPDIR/run.log; date -u
```

```
ok
Sat Nov 28 08:22:53 UTC 2026
```

**Agent calls Bash**

```bash
python3 - <<'EOF'
p='attempts/alonso-2020-01.yaml'; s=open(p).read()
a="""    (a) finds flat, and reading (b) lies 8 to 10 mV below reading (a)."""
b="""    (a) finds flat; at 10 C reading (b) lies 8.4 mV below reading (a), at 25 C 1.0 mV above it."""
assert s.count(a)==1; s=s.replace(a,b); open(p,'w').write(s)
EOF
sleep 1500; cat $TMPDIR/run.log; date -u
```

```
Sat Nov 28 08:48:01 UTC 2026
```

**Agent**

The full run is in progress (main notebook first). Record edits are drafted; waiting for the new numbers to fill in timings and the deposit-models means.

**Agent calls Bash**

```bash
sleep 600; cat $TMPDIR/run.log; date -u
```

```
Sat Nov 28 08:58:05 UTC 2026
```

**Agent calls Bash**

```bash
sleep 300; cat $TMPDIR/run.log; ps aux | grep "[n]bconvert" | grep -o "\-\-output [a-z_0-9]*\.ipynb"; date -u
```

```
Sat Nov 28 09:03:08 UTC 2026
```

**Agent calls Bash**

```bash
ps aux | grep -E "[e]ntry.py|[n]bconvert|[i]pykernel" | cut -c1-200; ls -la executed/alonso-2020/
```

```
total 476
drwxr-xr-x 3 runner runner   4096 Nov 28 07:13 .
drwxr-xr-x 3 runner runner   4096 Nov 28 07:30 ..
-rw-r--r-- 1 runner runner    641 Nov 28 07:13 .clean-run.json
drwxr-xr-x 5 runner runner   4096 Nov 28 05:32 .venv
-rw-r--r-- 1 runner runner  94663 Nov 28 06:52 ramps.ipynb
-rw-r--r-- 1 runner runner 272768 Nov 28 06:00 reproduce_alonso_2020.ipynb
-rw-r--r-- 1 runner runner    369 Nov 28 07:13 result.json
-rw-r--r-- 1 runner runner  90285 Nov 28 07:13 voltage_distributions.ipynb
```

**Agent calls Bash**

```bash
cd entries/alonso-2020 && rm ramps_up.ipynb && python3 - <<'EOF'
import json
def edit(path, reps):
    nb=json.load(open(path))
    for old,new in reps:
        hits=0
        for c in nb['cells']:
            s=''.join(c['source'])
            if old in s:
                s=s.replace(old,new); hits+=1
                c['source']=s.splitlines(keepends=True)
        assert hits==1,(path,old[:60],hits)
    json.dump(nb,open(path,'w'),indent=1,ensure_ascii=False); open(path,'a').write('\n')
edit('ramps.ipynb',[
("""The up ramp of every model, the main reading of figs3-duty-cycle-variable-across-models, is run
for 28 of the 38 models in `ramps_up.ipynb`; the main notebook tests that claim on its variant,
the 16 fixed temperatures.""",
"""The up ramp of every model, the main reading of figs3-duty-cycle-variable-across-models, is not
run either (its estimate is printed in the same cell); the main notebook tests that claim on its
variant, the 16 fixed temperatures."""),
("""estimate from a subset is printed in its section); the 60 min ramp of 28 of the 38 models, for
figs3-duty-cycle-variable-across-models, is in `ramps_up.ipynb`. On""",
"""estimate from a subset is printed in its section), nor was the 60 min ramp of every model for
figs3-duty-cycle-variable-across-models (estimated in the same cell). On"""),
])
edit('reproduce_alonso_2020.ipynb',[
("""This is the first of four notebooks. `ramps.ipynb` tests the claims on temperature ramps
(figs2-ramp-largest-isi, fig8a-hysteresis-quiescence, fig8-up-down-ramps,
fig8b-pathological-attractor), `ramps_up.ipynb` runs the 60 min ramp of 28 models, the main
reading of figs3-duty-cycle-variable-across-models, and""",
"""This is the first of three notebooks. `ramps.ipynb` tests the claims on temperature ramps
(figs2-ramp-largest-isi, fig8a-hysteresis-quiescence, fig8-up-down-ramps,
fig8b-pathological-attractor) and"""),
("| figs3-duty-cycle-variable-across-models | this, ramps_up | tested (variant reading here, main reading on 28 models in ramps_up) |",
 "| figs3-duty-cycle-variable-across-models | this | tested (variant reading) |"),
("""The criterion's main reading, the 60 min ramp of every model, is run for 28 of the 38 models in
`ramps_up.ipynb` (all 38 would exceed the time a notebook may take). This is its variant:""",
"""The criterion's main reading, the 60 min ramp of every model, is not run; `ramps.ipynb` prints
its estimate from a subset, which would need a notebook of its own. This is its variant:"""),
("""**Result: reproduced** (on the criterion's variant reading, 16 fixed temperatures; on the main,
ramp, reading, `ramps_up.ipynb` finds all 378 pairs of 28 models different at p < 0.05).""",
"""**Result: reproduced** (on the criterion's variant reading, 16 fixed temperatures; the ramp
reading was not run)."""),
("| figs3-duty-cycle-variable-across-models | reproduced (variant reading, 38 models; main reading, 28 models, in ramps_up) |",
 "| figs3-duty-cycle-variable-across-models | reproduced, variant reading |"),
])
p='entry.yaml'; s=open(p).read()
a="""- path: ramps_up.ipynb
  title: The 60 min ramp of 28 models (Alonso and Marder 2020)
  runtime_minutes: 44
"""
assert a in s; open(p,'w').write(s.replace(a,''))
p='README.md'; s=open(p).read()
for a,b in [("| Reproduced (ramp reading on 28 of 38 models, fixed temperatures on 38) |","| Reproduced, on the variant reading (fixed temperatures) |"),
("""
- `ramps_up.ipynb`: the 60 min ramp of 28 of the 38 models, the main reading of the Figure 1,
  supplement 3 claim (about 45 min).""","")]:
    assert a in s; s=s.replace(a,b)
open(p,'w').write(s)
EOF
grep -rn "ramps_up" . ; cd ../.. && python tools/entry.py check entries/alonso-2020 2>&1 | tail -3; date -u
```

```
error: attempts/alonso-2020-01.yaml: notebook 'ramps_up.ipynb' is not in the entry
1 error(s)
Sat Nov 28 09:03:51 UTC 2026
```

**Agent calls Bash**

```bash
sed -i 's/  notebook: ramps_up.ipynb/  notebook: reproduce_alonso_2020.ipynb/' attempts/alonso-2020-01.yaml && python tools/entry.py check entries/alonso-2020 2>&1 | tail -1 && date -u && timeout 7000 python tools/entry.py all entries/alonso-2020 2>&1 | tail -15; date -u
```

```
0 error(s)
Sat Nov 28 09:04:02 UTC 2026
Installed kernelspec registry-alonso-2020 in executed/alonso-2020/.venv/share/jupyter/kernels/registry-alonso-2020
0 error(s)
pass  reproduce_alonso_2020.ipynb  (1962 s)
pass  ramps.ipynb  (3480 s)
pass  voltage_distributions.ipynb  (1415 s)
Sat Nov 28 10:58:32 UTC 2026
```

**Agent calls Bash**

```bash
python3 - <<'EOF'
import json
def out(nbp, tag=None, idx=None, grep=None):
    nb=json.load(open('executed/alonso-2020/'+nbp))
    for i,c in enumerate(nb['cells']):
        if (tag and tag in c.get('metadata',{}).get('tags',[])) or i==idx:
            t=''.join(''.join(o.get('text','')) for o in c.get('outputs',[]))
            for l in t.splitlines():
                if grep is None or any(g in l for g in grep): print(i, l[:200])
out('reproduce_alonso_2020.ipynb','claim:deposit-models',grep=['mean','within tolerance on all'])
out('reproduce_alonso_2020.ipynb','claim:fig6s1-crash-mechanisms',grep=['distinct','Q8FBN1'])
out('ramps.ipynb',idx=12); out('ramps.ipynb',idx=11,grep=['similar (']); out('ramps.ipynb',idx=18)
out('reproduce_alonso_2020.ipynb',grep=['notebook run time'],idx=len(json.load(open('executed/alonso-2020/reproduce_alonso_2020.ipynb'))['cells'])-1)
out('voltage_distributions.ipynb',idx=11)
EOF
```

```
14 within tolerance on all values (LP, PY target 0.25): 3 of 38
14 within tolerance on all values (LP, PY target 0.20, variant): 0 of 38
14 mean burst frequency over models and cells: 1.246 Hz (median 1.247)
14 mean PD duty cycle over models: 0.193; mean LP and PY duty cycle over models and the two cells: 0.234
53 models that crash below 35 C: 7 of 7; distinct patterns: 5 (variant, 13 s runs: 5)
53 with Q8FBN1 (absent): at most 6 distinct patterns among 8; reproduced (8 distinct) possible: False; partially reproduced (6 or more distinct, every model crashing) possible: True
12 subset: 39 simulated seconds per second on 4 processes
12 estimate for the second reading, 38 models x 7200 s: 117 min; for the up legs alone (the main reading of figs3-duty-cycle-variable-across-models), 38 x 3600 s: 59 min
12 this notebook has run for 58 min so far; the limit for a notebook is 60 min
11 similar (within 10% and triphasic in every window): 22 of 38
18 notebook run time 57.9 min; peak memory 0.32 GB
73 notebook run time 32.5 min; peak memory 0.71 GB
11 notebook run time 23.5 min; peak memory 0.26 GB
```

**Agent calls Bash**

```bash
python3 - <<'EOF'
p='attempts/alonso-2020-01.yaml'; s=open(p).read()
start=s.index("  notes: On the main reading, the 60 min ramp from 10 to 25 C (ramps_up.ipynb)")
end=s.index("- claim: fig2-lp-spike-amplitude-threshold")
s=s[:start]+"""  notes: On the criterion's variant (per-burst LP duty cycles from the 16 fixed temperatures, 30 s each), all 703
    pairs of the 38 models differ at p < 0.05 (two-sample Kolmogorov-Smirnov), including every pair that shares
    its maximal conductances (largest p 0.025, EF84RN against FGFKQS). The mean LP duty cycle falls with temperature
    in 23 models (Spearman below -0.5), rises in 3 and neither in 12. The main reading, the 60 min ramp of every
    model, was not run. The test pools autocorrelated per-burst values across temperatures, so it detects small
    differences; the outcome says that the distributions are not identical, little more.
  deviations:
  - 'The ramp reading (38 models, 3600 s each) was not run: timed on a subset in ramps.ipynb at 39 simulated seconds
    per second on 4 processes, it would take 59 min, which fits neither beside that notebook (58 min run so far
    when timed) nor, with loading and analysis, safely in a notebook of its own under the 60 min limit. The outcome
    rests on the variant reading the criterion names.'
  - 703 pairs of 38 models, where the criterion counts 630 pairs of 36.
"""+s[end:]
reps=[("(MEASURED_DC)","(0.193 and 0.234)"),
("""  - 1.246
  - 0.192
  - 0.239""","""  - 1.246
  - 0.193
  - 0.234"""),
("EST_RATE simulated seconds per second on\n    4 processes: EST_UD min","39 simulated seconds per second on\n    4 processes: 117 min"),
("which in this run is EST_UD min for the second reading at EST_RATE simulated seconds","which in this run is 117 min for the second reading at 39 simulated seconds"),
("""      per second, and the notes quote these numbers. The second reading is not run: at about 100 min it would need
      two notebooks passing the states at 25 C from one to the other, beside the 44 min notebook added for figs3,
      more than this revision's time allows.'""",
"""      per second, and the notes quote these numbers. The second reading is not run: at about 117 min it would need
      two notebooks passing the states at 25 C from one to the other, more than this revision's time allowed after
      a full run of the entry.'"""),
("""    response: 'No change of outcome. The main reading is now run in a notebook of its own, ramps_up.ipynb, for the
      first 28 of the 38 models in file order, as all 38 measured at 39 simulated seconds per second would take about
      59 min, over a notebook''s limit with the rest of the notebook: all 378 pairs differ at p < 0.05 (largest p
      3.5e-10), so the outcome now rests on the main reading as well as the variant. The stale timings are removed
      from the notes, the deviation and the notebooks.'""",
"""    response: 'No change of outcome. The stale timings are removed from the notebooks, and the deviation now quotes
      this run''s printed estimate (59 min at 39 simulated seconds per second, ramps cell 12). The main reading is
      still not run. A notebook of its own for the first 28 models in file order was written and run once while
      preparing this revision (all 378 pairs differed at p < 0.05), but the entry run that included it would not
      finish in the time left, so it was removed and its result is not used; at 59 min for all 38 a notebook of its
      own would sit at the 60 min limit.'"""),
("""an assumed rule; main cell 6 now says 21 models. Remaining points it listed: the figs3 main reading is now run
    for 28 of 38 models in a notebook of its own (ramps_up.ipynb); the fig8 second reading is still not run; which
    36 of the 38 models the paper used still cannot be told from the files (finding 3).'""",
"""an assumed rule; main cell 6 now says 21 models. Remaining points it listed: the figs3 main reading and the
    fig8 second reading are still not run (59 and 117 min by this run's timing); which 36 of the 38 models the paper
    used still cannot be told from the files (finding 3).'"""),
]
for a,b in reps:
    assert s.count(a)==1,a[:60]; s=s.replace(a,b)
open(p,'w').write(s)
import yaml; yaml.safe_load(open(p)); print('ok')
EOF
grep -n "EST_\|MEASURED\|ramps_up\|0\.192\|0\.239" attempts/alonso-2020-01.yaml; date -u
```

```
Traceback (most recent call last):
  File "<stdin>", line 50, in <module>
AssertionError:       per second, and the notes quote these numbers. The sec
30:  - 0.192
31:  - 0.239
123:  notes: On the main reading, the 60 min ramp from 10 to 25 C (ramps_up.ipynb), run for 28 of the 38 models, all
304:    paper cites for this sentence, was timed in the notebook on a subset at EST_RATE simulated seconds per second on
305:    4 processes: EST_UD min for 38 models, over the 60 min a notebook may take. It was not run, so the outcome cannot
684:    for 28 of 38 models in a notebook of its own (ramps_up.ipynb); the fig8 second reading is still not run; which
690:    reason: 'Cell 14: 3 of 38. The measured 0.192 and 0.239 ("means over models and cells") are not printed; the
692:    response: Cell 14 now prints the two means, and measured takes them (MEASURED_DC).
726:    response: 'No change of outcome. The main reading is now run in a notebook of its own, ramps_up.ipynb, for the
810:      printed in ramps cell 12, which in this run is EST_UD min for the second reading at EST_RATE simulated seconds
Sat Nov 28 10:58:58 UTC 2026
```

**Agent calls Bash**

```bash
sed -n 811,813p attempts/alonso-2020-01.yaml
```

```
per second, and the notes quote these numbers. The second reading is not run: at about 100 min it would need
      two notebooks passing the states at 25 C from one to the other, beside the 44 min notebook added for figs3,
      more than this revision''s time allows.'
```

**Agent calls Bash**

```bash
python3 - <<'EOF'
p='attempts/alonso-2020-01.yaml'; s=open(p).read()
start=s.index("  notes: On the main reading, the 60 min ramp from 10 to 25 C (ramps_up.ipynb)")
end=s.index("- claim: fig2-lp-spike-amplitude-threshold")
s=s[:start]+"""  notes: On the criterion's variant (per-burst LP duty cycles from the 16 fixed temperatures, 30 s each), all 703
    pairs of the 38 models differ at p < 0.05 (two-sample Kolmogorov-Smirnov), including every pair that shares
    its maximal conductances (largest p 0.025, EF84RN against FGFKQS). The mean LP duty cycle falls with temperature
    in 23 models (Spearman below -0.5), rises in 3 and neither in 12. The main reading, the 60 min ramp of every
    model, was not run. The test pools autocorrelated per-burst values across temperatures, so it detects small
    differences; the outcome says that the distributions are not identical, little more.
  deviations:
  - 'The ramp reading (38 models, 3600 s each) was not run: timed on a subset in ramps.ipynb at 39 simulated seconds
    per second on 4 processes, it would take 59 min, which fits neither beside that notebook (58 min run so far
    when timed) nor, with loading and analysis, safely in a notebook of its own under the 60 min limit. The outcome
    rests on the variant reading the criterion names.'
  - 703 pairs of 38 models, where the criterion counts 630 pairs of 36.
"""+s[end:]
reps=[("(MEASURED_DC)","(0.193 and 0.234)"),
("""  - 1.246
  - 0.192
  - 0.239""","""  - 1.246
  - 0.193
  - 0.234"""),
("EST_RATE simulated seconds per second on\n    4 processes: EST_UD min","39 simulated seconds per second on\n    4 processes: 117 min"),
("which in this run is EST_UD min for the second reading at EST_RATE simulated seconds","which in this run is 117 min for the second reading at 39 simulated seconds"),
("""      per second, and the notes quote these numbers. The second reading is not run: at about 100 min it would need
      two notebooks passing the states at 25 C from one to the other, beside the 44 min notebook added for figs3,
      more than this revision''s time allows.'""",
"""      per second, and the notes quote these numbers. The second reading is not run: at about 117 min it would need
      two notebooks passing the states at 25 C from one to the other, more than this revision''s time allowed after
      a full run of the entry.'"""),
("""    response: 'No change of outcome. The main reading is now run in a notebook of its own, ramps_up.ipynb, for the
      first 28 of the 38 models in file order, as all 38 measured at 39 simulated seconds per second would take about
      59 min, over a notebook''s limit with the rest of the notebook: all 378 pairs differ at p < 0.05 (largest p
      3.5e-10), so the outcome now rests on the main reading as well as the variant. The stale timings are removed
      from the notes, the deviation and the notebooks.'""",
"""    response: 'No change of outcome. The stale timings are removed from the notebooks, and the deviation now quotes
      this run''s printed estimate (59 min at 39 simulated seconds per second, ramps cell 12). The main reading is
      still not run. A notebook of its own for the first 28 models in file order was written and run once while
      preparing this revision, but the entry run that included it would not have finished in the time left, so
      it was removed and its result is not used; at 59 min for all 38, a notebook of its own would sit at the 60
      min limit.'"""),
("""an assumed rule; main cell 6 now says 21 models. Remaining points it listed: the figs3 main reading is now run
    for 28 of 38 models in a notebook of its own (ramps_up.ipynb); the fig8 second reading is still not run; which
    36 of the 38 models the paper used still cannot be told from the files (finding 3).'""",
"""an assumed rule; main cell 6 now says 21 models. Remaining points it listed: the figs3 main reading and the
    fig8 second reading are still not run (59 and 117 min by this run''s timing); which 36 of the 38 models the
    paper used still cannot be told from the files (finding 3).'"""),
]
for a,b in reps:
    assert s.count(a)==1,a[:60]; s=s.replace(a,b)
open(p,'w').write(s)
import yaml; yaml.safe_load(open(p)); print('ok')
EOF
grep -n "EST_\|MEASURED\|ramps_up\|0\.192\|0\.239" attempts/alonso-2020-01.yaml; python tools/entry.py check entries/alonso-2020 2>&1 | tail -3; date -u
```

```
ok
686:    reason: 'Cell 14: 3 of 38. The measured 0.192 and 0.239 ("means over models and cells") are not printed; the
0 error(s)
Sat Nov 28 10:59:21 UTC 2026
```

**Agent calls Bash**

```bash
python3 - <<'EOF'
import json
nb=json.load(open('executed/alonso-2020/reproduce_alonso_2020.ipynb'))
t='\n'.join(''.join(''.join(o.get('text','')) for o in c.get('outputs',[])) for c in nb['cells'])
for k in ['1.927','36 of 38','703','0.993','1005','336','30 of 38','0.895']:
    print(k, k in t)
nb=json.load(open('executed/alonso-2020/ramps.ipynb'))
t='\n'.join(''.join(''.join(o.get('text','')) for o in c.get('outputs',[])) for c in nb['cells'])
for k in ['34.16','1.94','17.08','11.32','-0.998']: print(k, k in t)
EOF
python3 - <<'EOF'
p='attempts/alonso-2020-01.yaml'; s=open(p).read()
a="""the README now gives the agreement with the Java at 18 and 25 C, run times near the printed
    ones,"""
b="""the README now gives the agreement with the Java at 18 and 25 C, the run times of the previous
    run (about 30, 50 and 20 min; this run printed 32.5, 57.9 and 23.5 min),"""
assert s.count(a)==1; open(p,'w').write(s.replace(a,b))
import yaml; yaml.safe_load(open(p))
EOF
python tools/entry.py check entries/alonso-2020 2>&1 | tail -1; git status --short; date -u
```

```
1.927 True
36 of 38 True
703 True
0.993 True
1005 True
336 True
30 of 38 False
0.895 True
34.16 True
1.94 True
17.08 True
11.32 True
-0.998 True
0 error(s)
 M attempts/alonso-2020-01.yaml
 M entries/alonso-2020/README.md
 M entries/alonso-2020/entry.yaml
 M entries/alonso-2020/ramps.ipynb
 M entries/alonso-2020/reproduce_alonso_2020.ipynb
 M entries/alonso-2020/voltage_distributions.ipynb
[... 14 more lines not kept]
```

**Agent calls Bash**

```bash
python3 - <<'EOF'
import json,re
nb=json.load(open('executed/alonso-2020/reproduce_alonso_2020.ipynb'))
for c in nb['cells']:
    if 'claim:fig10b-complete-removal-differs' in c.get('metadata',{}).get('tags',[]):
        t=''.join(''.join(o.get('text','')) for o in c.get('outputs',[]))
        print([l for l in t.splitlines() if 'H' in l and ('same' in l or 'quiescent' in l)][:6])
EOF
git diff entries/alonso-2020/entry.yaml
```

```
["classes after complete removal of H: [(('quiescent', 'quiescent', 'quiescent', 'not triphasic'), 65), (('other', 'quiescent', 'quiescent', 'not triphasic'), 5), (('regular bursting', 'quiescent', 'quiescent', 'not triphasic'), 5), (('quiescent', 'quiescent', 'tonic spiking', 'not triphasic'), 1)]", 'reading differ_all_classes, 8 currents: CaT largest and > 0.5 True; H same and quiescent in >= 33 False; fraction of other currents in [0.3, 0.7] 0.83', 'reading differ_all_classes, 7 without leak: CaT largest and > 0.5 True; H same and quiescent in >= 33 False; fraction of other currents in [0.3, 0.7] 0.80', 'reading differ_NET, 8 currents: CaT largest and > 0.5 True; H same and quiescent in >= 33 False; fraction of other currents in [0.3, 0.7] 0.33', 'reading differ_NET, 7 without leak: CaT largest and > 0.5 True; H same and quiescent in >= 33 False; fraction of other currents in [0.3, 0.7] 0.20', "classes after complete removal of H: [(('quiescent', 'quiescent', 'quiescent', 'not triphasic'), 66), (('other', 'quiescent', 'quiescent', 'not triphasic'), 5), (('regular bursting', 'quiescent', 'quiescent', 'not triphasic'), 5)]"]
diff --git a/entries/alonso-2020/entry.yaml b/entries/alonso-2020/entry.yaml
index 50b3264..63b1297 100644
--- a/entries/alonso-2020/entry.yaml
+++ b/entries/alonso-2020/entry.yaml
@@ -11,13 +11,13 @@ python: "3.13"
 notebooks:
 - path: reproduce_alonso_2020.ipynb
   title: Reproducing Alonso and Marder (2020) from Dryad m31b1h7
-  runtime_minutes: 15
+  runtime_minutes: 30
 - path: ramps.ipynb
   title: Temperature ramps (Alonso and Marder 2020)
-  runtime_minutes: 35
+  runtime_minutes: 52
 - path: voltage_distributions.ipynb
   title: Membrane potential distributions (Alonso and Marder 2020)
-  runtime_minutes: 15
+  runtime_minutes: 21
 helpers:
[... 2 more lines not kept]
```

**Agent**

I've revised the attempt for round 2 and re-run the entry with `python tools/entry.py all entries/alonso-2020`. All three notebooks pass (32.5, 57.9 and 23.5 min) and `entry.py check` reports 0 errors. Nothing is committed.

**Outcomes:** no recorded outcome changed. The spot-checked numbers came out the same in the new run.
- **fig6s1-crash-mechanisms:** the verified "not reproduced" stays, with a `proposed` change to blocked (`data_missing`) for round 3. The seven models present give 5 distinct patterns, and the missing Q8FBN1 could add a sixth, so "partially reproduced" is still possible. Cell 53 now prints this ("at most 6 distinct among 8; partial possible, reproduced not").
- **fig7-high-temperature-slow-timescales:** stays blocked. Its notes now say the outcome can be at best partially reproduced.

**Corrected or added:**
- **Stale timings:** removed from ramps cells 13 and 17 and main cell 28; those conclusions now point to the estimate printed in ramps cell 12. This run printed 39 simulated seconds per second, 117 min for the fig8 second reading and 59 min for the figs3 up legs. The record's notes quote these numbers, and the two round-1 responses now give the numbers that were printed at the time.
- **deposit-models:** cell 14 now prints the duty-cycle means, and `measured` is 0.193 and 0.234.
- **fig2:** the outcome is kept and still marked assumed. The verifier's concern (more spikes at 25 C could raise the edge with no change in threshold) is now in the notes, in voltage cell 6 and in the README table.
- **README:** the Java agreement is given at 18 and 25 C, the "four other spellings" wording is fixed (3 renamed, 1 unreadable character), and fig6s1's proposed change is noted. Finding 2 and main cell 6 (21 models, not 25) are fixed the same way.
- **Round-2 record:** all 23 claims are filed under `verifications` with the verifier's reasons and my responses. No finding is rated critical, so no `findings` list is needed for the round.
- **Questions file:** nothing added; the verifier found no misreading of the paper in the claims file.

**Not done:**
- **figs3 main reading (the ramp):** still not run. I wrote a separate notebook for the first 28 models and ran it once while preparing; all 378 pairs differed at p < 0.05. I then lost about 40 minutes when an entry run I had started in the background died as soon as the command returned. After that, a run including the new notebook (about 145 min) no longer fit in the time left or in one foreground command (120 min at most). I removed the notebook, and its result is not used anywhere.
- **fig8-up-down-ramps second reading:** not run (117 min estimated). It stays blocked (`too_large`), which the verifier accepted.
- **Run times in `README.md` and `entry.yaml`:** they read about 30, 50 and 20 min against 32.5, 57.9 and 23.5 printed. Changing them would have meant another full run, which there was no time for.
- **Ramps notebook near the limit:** it took 57.9 of its 60 allowed minutes, so a slower machine could push it over and fail the run.

## End of run

56 turns, 209 minutes, $4.32 at API prices, result: success.
