# du-2026 · author-revise-1 · run 44940121047

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
date -u; cat transcripts/du-2026/verifier-1-report.md; ls entries/du-2026 questions paper; wc -l docs/protocol.md
```

```
Sat Nov 21 19:23:57 UTC 2026
**A. Outcomes** (33 claims in the claims file)

| Claim | Outcome | Reason |
|---|---|---|
| synthetic-template-null | reproduced | 01 cell 4: median −0.0000023, median \|gain\| 0.0000092, which is below 0.03. The range −0.0000588 to 0.0000248 matches the paper exactly. |
| synthetic-signal-ordering | reproduced | 01 cell 6: weak 0.22451 and strong 0.37360, strictly increasing from template-only. |
| synthetic-pair-breaking | reproduced | 01 cell 8: 10/10 seeds above both controls. Replacement mean −0.3486, permutation mean −0.3663. |
| link-development-sample | reproduced | 02 cell 10: 9 dates, 6,750 usable trials, all 18 sessions have 375. |
| link-neural-only-r2 | reproduced | 02 cell 12: CO 0.3077, RD 0.3129. |
| link-context-ladder-gain | reproduced | 02 cell 14: gain falls at every step for both tasks, and 10/10 values are within tolerance (all equal the paper to 4 decimals). |
| link-context-only-r2 | reproduced | 02 cell 16: plus history 0.6617/0.6839; phase only 0.0084/0.0055, both below 0.02. |
| link-phase-only-replacement | reproduced | 02 cell 18: RD mean 0.10498, positive. |
| link-task-contrast-by-context | reproduced | 02 cell 20: signs +, −, −, + as stated. Geometry by phase (0.0015) is near zero under both readings: its CI contains 0, and it is smaller in absolute value than the direction (0.0155) and additive (0.0110) contrasts. |
| nested-geometry-gain | reproduced | 02 cell 22: SBP 0.02009 (18/18 positive), TCR 0.01155 (17/18). Date CIs 0.01586–0.02401 and 0.00711–0.01591, close to Table 1. |
| nested-history-gain | reproduced | 02 cell 24: 0.00873 (17/18), 0.00420 (16/18), each below its geometry mean. |
| nested-replacement-negative | reproduced | 02 cell 26: all four negative, 4/4 within tolerance. |
| replacement-source-diagnostics | reproduced | 02 cell 28: minimum eligible sources 5, median maximum reuse 3, maximum 4, self-replacement error 0. |
| permutation-negative | reproduced | 02 cell 30, reading (a): 18/
[... 251 more lines not kept]
```

**Agent calls Bash**

```bash
grep -n "^#" docs/protocol.md | head -80
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
370:### 2. Check the data against its description
385:### 3. Write the entry
470:### 4. Lock, check and run
490:### 5. Record the attempt
599:### 6. Hand over for verification
637:## Repeat attempts
703:## Local and remote datasets
726:## Verifier
730:### Round 1: without the author's conclusions
755:### Round 2: with the author's conclusions
[... 1 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 199,215p docs/protocol.md; sed -n 470,779p docs/protocol.md
```

````
## Author

The workflow puts the paper under `paper/`, as for the reader. Read it to
understand the claims, their data and their figures. The claims file still
decides what is tested: do not change a claim's statement, expected values or
criterion. A method detail the claims file lacks is taken from the paper
(step 6).

**Time.** An author run is stopped five hours after it starts, and whatever
is not recorded by then is lost. The prompt says when the run started and the
time by which to finish. Check the clock (`date -u`) between steps. When that
time comes, stop analysing and finish: record each claim not yet tested as
blocked, `too_large` where the computation is what stopped it, saying how far
it got, then write the attempt record and run the entry's checks. A record
with some claims blocked for time is worth more than a run that is cut off.

### 1. Establish what can be tested
### 4. Lock, check and run

```bash
[... 307 more lines not kept]
````

**Agent calls Bash**

```bash
ls attempts | grep du-; wc -l attempts/du-2026-01.yaml; grep -n "verifications" -A40 attempts/*.yaml | grep -v du-2026 | head -80; cat executed/du-2026/*.stamp 2>/dev/null | head; ls executed/du-2026
```

```
du-2026-01.yaml
481 attempts/du-2026-01.yaml
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
[... 69 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "attempts/du-2026-01.yaml"
}
```

```
1	schema_version: 3
2	id: du-2026-01
3	datasets:
4	- archive: dandi
5	  id: "001201"
6	  version: 0.251023.2336
7	  doi: 10.48324/dandi.001201/0.251023.2336
8	  relation: reuses
9	- archive: dandi
10	  id: "000129"
11	  version: 0.241017.1444
12	  doi: 10.48324/dandi.000129/0.241017.1444
13	  relation: reuses
14	paper: doi:10.64898/2026.08.04.742876
15	date: 2026-11-21
16	entry: du-2026
17	provenance:
18	  kind: agent
19	  accountable:
20	    name: CatalystNeuro
[... 462 more lines not kept]
```

**Agent calls Bash**

```bash
ls claims papers/datasets 2>/dev/null | grep du-; cat papers/datasets/du-2026.yaml; grep -n "maze" -i -A30 claims/du-2026.yaml | head -120; grep -rn "blocked_by" docs/*.md schemas 2>/dev/null | head
```

```
du-2026.yaml
du-2026.yaml
# The datasets this paper is tested on (docs/paper-first.md).
schema_version: 1
paper: doi:10.64898/2026.08.04.742876
title: A Context-Conditional Audit of Trial-Pairing-Dependent Neural Gain in Motor-Cortex Decoding
datasets:
- archive: dandi
  id: '001201'
  relation: reuses
- archive: dandi
  id: 000129
  relation: reuses
18:# holds the loaders (src/neural_evidence/link.py, mc_rtt.py, mc_maze.py), the fully nested and
19-# nonlinear estimators (nested_estimators.py), the synthetic generator (synthetic.py), run
20-# scripts for the synthetic calibration, the primary analyses, the LINK context ladder, the
21-# confirmation and the nonlinear-map seeds, the figure builder, tests, and frozen outputs and
22-# figure source tables. It holds no script for the temporal-offset, quadratic-capacity,
23-# block-penalty or nonlinear-context runs; only their frozen tables. Frozen outputs were not
24-# used to set any expected value; every expected value is the paper's.
[... 119 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 280,330p docs/protocol.md; sed -n 30,50p docs/paper-first.md; sed -n 255,275p schemas/attempt.schema.json; grep -n "data: elsewhere" -B2 -A5 docs/protocol.md docs/*.md | head -40
```

```
other claim. If it cannot be tested here, block it for the reason that
     applies (`too_large`, `not_runnable`, `data_unreadable` and so on),
     never `data_missing`. Data the paper names but that are not public
     anywhere stay `data: dataset`, blocked with `data_missing`.
   - The notes of a `with_inputs` claim say which side a difference comes
     from as far as the outputs show: whether the dataset's measures match
     the paper's per-cell values where those are published, and whether the
     outside labels match the paper's counts.
5. Decide now which claims are blocked, and why; a block that depends on a
   selection (too few units under the claim's own rule) is decided once the
   selection is made. Give the main reason under
   `blocked_by` and any others in the notes:
   - `data_missing`: something the claim needs is not in the dataset and
     not public anywhere else, or for an outside input, not public. When the
     paper deposited it in another public archive, the claim is
     `data: elsewhere` instead (step 4).
   - `metadata_insufficient`: the data are there but cannot be interpreted or
     linked, for lack of a description, label, identifier or mapping.
   - `methods_underspecified`: neither the paper nor its code fixes the
     procedure well enough to repeat it, and no choice has a defensible basis
[... 113 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 165,186p docs/protocol.md; sed -n 215,280p docs/protocol.md
```

```
### 4. Data from outside the paper's own recordings

Say, for each claim, what data the paper's test uses (`data`, above). When the
paper relies on outside data (a model, a reference dataset, measurements of
the same cells made by another method), or deposited part of its data in
another archive, name it and where it is, as the paper gives it. The author
pins it and decides whether it can be used (author, step 4).

### 5. Check

A second reader, in a separate run, checks the claims file against the paper:
that each statement says what the paper says, no more and no less; that each
quote is word for word (the quote checker, `tools/claims_check.py`, does this
mechanically); that each source points at the place; that the statistics are
the paper's and are results, not thresholds; that every part of every
criterion's method is taken from the paper or its code, as cited; and that the
paper's main findings each have a claim. The checker corrects what it can
show is wrong, and records each change, with its reason, under `checks` at
the end of the file. A claims file is ready for an attempt when its last check
says so.
[... 68 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && timeout 120 git clone -q https://github.com/gwkuqgfkqe/neural-decoder-context-audit rel 2>&1 | tail -2; cd rel && git checkout -q b042fbe1cda2ca5a353751c693d7c95f45de0456 && ls src/neural_evidence scripts 2>/dev/null; wc -l src/neural_evidence/mc_maze.py; curl -s https://api.dandiarchive.org/api/dandisets/000139/versions/0.220113.0408/assets/?page_size=10 | head -c 1500
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cat $TMPDIR/rel/src/neural_evidence/mc_maze.py; grep -n "maze\|Maze" -i $TMPDIR/rel/scripts/run_primary_analyses.py $TMPDIR/rel/scripts/run_nonlinear_seed_sensitivity.py | head -60
```

```
"""Loader for the public NLB MC_Maze medium NWB training file."""

from __future__ import annotations

from pathlib import Path

import numpy as np

from .types import DatasetSplit, TrialDataset


def _series(interface: object) -> object:
    spatial_series = getattr(interface, "spatial_series", None)
    if spatial_series is None:
        return interface
    return spatial_series[next(iter(spatial_series))]


def _bin_timestamped_mean(
    data: np.ndarray,
[... 244 more lines not kept]
```

**Agent calls Bash**

```bash
wc -l entries/du-2026/du2026.py; grep -n "^def \|^class " entries/du-2026/du2026.py; cat entries/du-2026/entry.yaml; cat entries/du-2026/requirements.in
```

```
1016 entries/du-2026/du2026.py
72:def _get_json(url: str) -> dict:
77:def list_assets(dandiset: str, version: str) -> list[dict]:
88:def asset_metadata(dandiset: str, version: str, asset_id: str) -> dict:
92:def s3_url(asset_id: str) -> str:
98:def open_h5(asset_id: str) -> h5py.File:
107:def session_date(path: str) -> str:
112:def link_task_from_metadata(metadata: dict) -> str:
121:def interior_ranks(n_items: int, n_select: int = 10) -> list[int]:
130:def _read_trials(h5: h5py.File) -> pd.DataFrame:
147:class LinkSession:
161:def load_link_session(asset_id: str, path: str, signals=("SpikingBandPower", "ThresholdCrossings")) -> LinkSession:
194:def _direction_octant(displacement: np.ndarray) -> int:
200:def phase_basis(n_time: int, n_harmonics: int = 4) -> np.ndarray:
210:class TrialDataset:
220:def build_link_dataset(
318:def _downsample_mean(data: np.ndarray, samples_per_bin: int) -> np.ndarray:
323:def _rtt_octant(target_error: np.ndarray) -> int:
330:class RttRaw:
343:def load_rtt_raw(asset_id: str, bin_ms: int = 20) -> RttRaw:
[... 77 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 1,130p entries/du-2026/du2026.py
```

```
"""Loading and estimators for the attempt on Du, Lai, Hu & Ye (2026).

Paper: "A Context-Conditional Audit of Trial-Pairing-Dependent Neural Gain in
Motor-Cortex Decoding", bioRxiv doi:10.64898/2026.08.04.742876.
Datasets: DANDI:001201 (LINK) and DANDI:000129 (MC_RTT), streamed at the
versions the paper cites (Methods 4.2, Data availability).

Every estimator here is a port of the paper's own code, the release named in
its Code availability section: github.com/gwkuqgfkqe/neural-decoder-context-audit,
tag v1.0-jne-submission, commit b042fbe1cda2ca5a353751c693d7c95f45de0456
(BSD 3-Clause, copyright the paper's authors). The file and function each
port comes from is named in its docstring, so that a verifier can compare
them. Parameters come from the claims file's criteria (which cite the
Methods or that code), from the passage of the paper named where they are
set, or are marked as a standard choice that cannot change a result.
The ports read the NWB files by streaming them (remfile + h5py) and keep
the arithmetic of the original: the same Ridge pipelines, the same
scikit-learn splitters and the same random_state offsets.
"""

[... 111 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 200,230p entries/du-2026/du2026.py; sed -n 318,442p entries/du-2026/du2026.py
```

```
def phase_basis(n_time: int, n_harmonics: int = 4) -> np.ndarray:
    """1, sin(r pi tau), cos(r pi tau), r = 1..4 (Methods 4.4; link.py _phase_basis)."""
    phase = np.linspace(0.0, 1.0, n_time, endpoint=False)
    features = [np.ones_like(phase)]
    for harmonic in range(1, n_harmonics + 1):
        features.extend([np.sin(harmonic * np.pi * phase), np.cos(harmonic * np.pi * phase)])
    return np.stack(features, axis=-1)


@dataclass
class TrialDataset:
    neural: np.ndarray
    context: np.ndarray
    behavior: np.ndarray
    condition: np.ndarray
    train_indices: np.ndarray
    test_indices: np.ndarray
    source_rows: np.ndarray | None = None  # row of the NWB trials table, per usable trial


[... 135 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 486,760p entries/du-2026/du2026.py
```

```
# Estimators (estimators.py, nested_estimators.py, robustness_estimators.py,
# specification_estimators.py)


def _ridge(alpha: float):
    """estimators.py _ridge: StandardScaler then Ridge (Methods 4.5)."""
    return make_pipeline(StandardScaler(), Ridge(alpha=alpha))


def _flat(array: np.ndarray, idx: np.ndarray) -> np.ndarray:
    selected = array[idx]
    return selected.reshape(-1, selected.shape[-1])


def _vw_r2(y, p) -> float:
    return float(r2_score(y, p, multioutput="variance_weighted"))


def _select_alpha(xtr, ytr, xva, yva, grid=ALPHA_GRID) -> float:
    """estimators.py _select_ridge_alpha (first best on ties)."""
[... 255 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 250,330p $TMPDIR/rel/scripts/run_primary_analyses.py; grep -n "id: rff-maze" -A40 claims/du-2026.yaml; grep -n "id: estimator-family-nlb" -A40 claims/du-2026.yaml
```

```
),
    }
    return {"groups": summary, "gates": gates, "all_gates_pass": all(gates.values())}


def _run_nlb(maze: Path, rtt: Path, bootstrap: int) -> dict[str, object]:
    configurations = [
        ("MC_Maze", "template", load_mc_maze(maze, neural_lead_ms=80)),
        (
            "MC_RTT",
            "lag_matched_output_history",
            load_mc_rtt(
                rtt,
                context_mode="causal_history",
                neural_lead_ms=80,
                output_lead_ms=80,
            ),
        ),
    ]
    rows: list[dict[str, object]] = []
[... 143 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/rel/src/neural_evidence; grep -n "def _replacement_sources\|def _ranked_replacement_sources\|def _permutation_sources" -A45 nested_estimators.py robustness_estimators.py | head -150
```

```
nested_estimators.py:363:def _permutation_sources(
nested_estimators.py-364-    *,
nested_estimators.py-365-    test_indices: np.ndarray,
nested_estimators.py-366-    conditions: np.ndarray,
nested_estimators.py-367-    rng: np.random.Generator,
nested_estimators.py-368-) -> np.ndarray:
nested_estimators.py-369-    sources = np.empty_like(test_indices)
nested_estimators.py-370-    test_conditions = conditions[test_indices]
nested_estimators.py-371-    for condition in np.unique(test_conditions):
nested_estimators.py-372-        positions = np.flatnonzero(test_conditions == condition)
nested_estimators.py-373-        if len(positions) < 2:
nested_estimators.py-374-            raise ValueError("Permutation needs two test trials per condition")
nested_estimators.py-375-        shuffled_positions = rng.permutation(positions)
nested_estimators.py-376-        shift = int(rng.integers(1, len(positions)))
nested_estimators.py-377-        sources[shuffled_positions] = test_indices[
nested_estimators.py-378-            np.roll(shuffled_positions, shift)
nested_estimators.py-379-        ]
nested_estimators.py-380-    if np.any(sources == test_indices):
nested_estimators.py-381-        raise AssertionError("Permutation unexpectedly retained a target trial")
nested_estimators.py-382-    return sources
[... 74 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/du-2026; python -c "
import json,sys
nb=json.load(open('06_mc_rtt.ipynb'))
for i,c in enumerate(nb['cells']):
    print('=== cell',i,c['cell_type'],c.get('metadata',{}).get('tags'))
    print(''.join(c['source']))
"
```

```
=== cell 0 markdown None
# Du, Lai, Hu & Ye (2026) on MC_RTT (DANDI:000129)

Paper doi:10.64898/2026.08.04.742876 (claims file written from the bioRxiv full text, without the
supplement). Dataset: DANDI:000129 (MC_RTT, Neural Latents Benchmark), pinned at version
**0.241017.1444**, the version the paper cites (Methods 4.2, Data availability) and the only published
version; file `sub-Indy/sub-Indy_desc-train_behavior+ecephys.nwb`, streamed. See
`02_link_development.ipynb` for the full claims table.

| Claim | Status |
|---|---|
| rtt-data | tested |
| rtt-gain | tested |
| rff-rtt | tested |
| estimator-family-nlb | MC_RTT part tested (reading (a) of the nonlinear context); MC_Maze part not run (DANDI:000139 is not one of this attempt's datasets) |
| maze-gain, rff-maze | blocked (DANDI:000139 not used) |
=== cell 1 code None
import collections, resource, time, zlib
import numpy as np
import pandas as pd
[... 132 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 816,1016p du2026.py
```

```
class _BlockRidge:
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
        self.model = Ridge(alpha=1.0, solver="cholesky")

    def _design(self, c, x, fit):
        if fit:
            c, x = self.cs.fit_transform(c), self.xs.fit_transform(x)
        else:
            c, x = self.cs.transform(c), self.xs.transform(x)
[... 181 more lines not kept]
```

**Agent calls Bash**

```bash
cd  ls -a; ls .venv* envs 2>/dev/null | head; grep -n "venv\|def cmd_run\|def run" tools/entry.py | head -30
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
[... 48 more lines not kept]
```

**Agent calls Bash**

```bash
ls -a executed/du-2026/; sed -n 596,680p tools/entry.py
```

```
.
..
.clean-run.json
.venv
01_synthetic.ipynb
02_link_development.ipynb
03_link_estimators.ipynb
04_link_temporal_capacity.ipynb
05_link_confirmation.ipynb
06_mc_rtt.ipynb
result.json
def run(entry_dir: Path, output_dir: Path, timeout: int, max_minutes: float, fresh: bool = False) -> int:
    entry = yaml.safe_load((entry_dir / "entry.yaml").read_text())
    stamp = None if fresh else reusable(entry_dir, output_dir, max_minutes)
    if stamp:
        when = time.strftime("%Y-%m-%d %H:%M UTC", time.gmtime(stamp["finished"]))
        for r in stamp["results"]:
            print(f"pass  {r['notebook']}  ({r['seconds']} s, reused)")
        print(f"reused the executed copies of {when}: nothing the run reads has changed since (hash "
              f"{stamp['hash'][:12]}). Nothing was executed and no environment was built; --fresh runs it again.")
[... 76 more lines not kept]
```

**Agent**

Existing venv is usable. Inspecting the MC_Maze file layout.

**Agent calls Bash**

```bash
cd entries/du-2026 && PY=../../executed/du-2026/.venv/bin/python; timeout 600 $PY -c "
import du2026 as d, numpy as np
f=d.open_h5('7ef450a8-8684-42e2-8598-cd38ca2b2e50')
def show(name,obj):
    import h5py
    if isinstance(obj,h5py.Dataset): print(name,obj.shape,obj.dtype,dict(obj.attrs).get('unit'),dict(obj.attrs).get('conversion'))
f['processing'].visititems(show)
f['intervals/trials'].visititems(show)
print(list(f['units'].keys()))
print(f['processing/behavior/hand_vel'].attrs.get('description'))
for k in f['processing/behavior']: print(k, dict(f['processing/behavior'][k].attrs).get('description'))
print(f['intervals/trials/split'][:5], f['intervals/trials/target_pos'][:3] if 'target_pos' in f['intervals/trials'] else '')
"
```

```
behavior/cursor_pos/data (757450, 2) float64 meters 0.001
behavior/cursor_pos/reference_frame () object None None
behavior/cursor_pos/timestamps (757450,) float64 seconds None
behavior/eye_pos/data (757450, 2) float64 meters 0.001
behavior/eye_pos/reference_frame () object None None
behavior/eye_pos/timestamps (757450,) float64 seconds None
behavior/hand_pos/data (757450, 2) float64 meters 0.001
behavior/hand_pos/reference_frame () object None None
behavior/hand_pos/timestamps (757450,) float64 seconds None
behavior/hand_vel/data (757450, 2) float64 m/s 0.001
behavior/hand_vel/timestamps (757450,) float64 seconds None
active_target (250,) int64 None None
barrier_pos (1466, 4) int64 None None
barrier_pos_index (250,) uint16 None None
delay (250,) int64 None None
go_cue_time (250,) float64 None None
id (250,) int64 None None
maze_id (250,) int64 None None
move_onset_time (250,) float64 None None
num_barriers (250,) int64 None None
[... 20 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 130,147p du2026.py
```

```
def _read_trials(h5: h5py.File) -> pd.DataFrame:
    group = h5["intervals/trials"]
    columns = {}
    for name in group:
        dataset = group[name]
        if not isinstance(dataset, h5py.Dataset) or name in {"id", "timeseries", "timeseries_index"}:
            continue
        values = dataset[:]
        if values.dtype.kind in "SO":
            values = np.array([v.decode() if isinstance(v, bytes) else str(v) for v in values])
        columns[name] = values
    frame = pd.DataFrame(columns)
    frame.index = group["id"][:]
    return frame


@dataclass
class LinkSession:
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "entries/du-2026/du2026.py",
 "old_string": "# --------------------------------------------------------------------------\n# Synthetic generator (synthetic.py generate_synthetic_dataset; Methods 4.8)",
 "new_string": "# --------------------------------------------------------------------------\n# MC_Maze (data elsewhere: DANDI:000139, the version the claims file names)\n\nMAZE_ID = \"000139\"\nMAZE_VERSION = \"0.220113.0408\"  # claims file, maze-gain \"where\"\nMAZE_TRAIN_PATH = \"sub-Jenkins/sub-Jenkins_ses-medium_desc-train_behavior+ecephys.nwb\"\n\n\ndef _bin_timestamped_mean(data: np.ndarray, timestamps: np.ndarray, bin_edges: np.ndarray) -> np.ndarray:\n    \"\"\"mc_maze.py _bin_timestamped_mean: mean of the samples whose timestamps fall in each bin.\"\"\"\n    n_bins = len(bin_edges) - 1\n    bin_index = np.searchsorted(bin_edges, timestamps, side=\"right\") - 1\n    valid = (bin_index >= 0) & (bin_index < n_bins)\n    sums = np.zeros((n_bins, data.shape[-1]), dtype=float)\n    counts = np.zeros(n_bins, dtype=int)\n    np.add.at(sums, bin_index[valid], data[valid])\n    np.add.at(counts, bin_index[valid], 1)\n    output = np.full_like(sums, np.nan, dtype=float)\n    populated = counts > 0\n    output[populated] = sums[populated] / counts[populated, None]\n    return output\n\n\n@dataclass\nclass MazeRaw:\n    hand_vel: np.ndarray\n    cursor_pos: np.ndarray\n    spike_counts: np.ndarray\n    n_units: int\n    heldout: np.ndarray\n    trials: pd.DataFrame\n    target_pos: list\n    n_bins: int\n    descriptions: dict\n\n\ndef load_maze_raw(asset_id: str, bin_ms: int = 20) -> MazeRaw:\n    \"\"\"Arrays mc_maze.py load_mc_maze reads: hand_vel and cursor_pos (stored\n    values, as pynwb's data[:] returns them), averaged into 20 ms bins on a grid\n    from 0 to the last trial stop_time, every unit's spike times histogrammed on\n    the same grid, and the trials table with its ragged target_pos column.\"\"\"\n    with open_h5(asset_id) as h5:\n        behavior = h5[\"processing/behavior\"]\n        descriptions = {name: {\"unit\": behavior[name][\"data\"].attrs.get(\"unit\"),\n                               \"conversion\": behavior[name][\"data\"].attrs.get(\"conversion\"),\n                               \"description\": behavior[name].attrs.get(\"description\")}\n                        for name in (\"hand_vel\", \"cursor_pos\")}\n        group = h5[\"intervals/trials\"]\n        trials = pd.DataFrame({name: group[name][:] for name in\n                               (\"start_time\", \"stop_time\", \"move_onset_time\", \"trial_type\", \"trial_version\",\n                                \"active_target\", \"split\", \"success\", \"maze_id\")})\n        trials[\"split\"] = [v.decode() if isinstance(v, bytes) else str(v) for v in trials[\"split\"]]\n        target_index = group[\"target_pos_index\"][:]\n        target_data = group[\"target_pos\"][:]\n        target_pos = [target_data[a:b] for a, b in zip(np.concatenate([[0], target_index[:-1]]), target_index)]\n        bin_seconds = bin_ms / 1000.0\n        n_bins = int(np.ceil(float(trials.stop_time.max()) / bin_seconds))\n        edges = np.arange(n_bins + 1, dtype=float) * bin_seconds\n        hand_vel = _bin_timestamped_mean(behavior[\"hand_vel/data\"][:], behavior[\"hand_vel/timestamps\"][:], edges)\n        cursor_pos = _bin_timestamped_mean(behavior[\"cursor_pos/data\"][:], behavior[\"cursor_pos/timestamps\"][:], edges)\n        index = h5[\"units/spike_times_index\"][:]\n        spike_times = h5[\"units/spike_times\"][:]\n        starts = np.concatenate([[0], index[:-1]])\n        counts = np.stack(\n            [np.histogram(spike_times[a:b], bins=edges)[0] for a, b in zip(starts, index)], axis=-1\n        ).astype(np.float32)\n        heldout = h5[\"units/heldout\"][:]\n    return MazeRaw(hand_vel, cursor_pos, counts, counts.shape[1], heldout, trials, target_pos, n_bins, descriptions)\n\n\ndef build_maze_dataset(raw: MazeRaw, *, bin_ms=20, movement_window_ms=800, neural_history_ms=100,\n                       neural_lead_ms=80, output_history_ms=100, output_lead_ms=None) -> TrialDataset:\n    \"\"\"Port of mc_maze.py load_mc_maze with context_mode \"template\", as\n    run_primary_analyses.py _run_nlb calls it (neural_lead_ms=80): 40 bins from\n    the bin nearest move_onset_time, five spike bins ending 80 ms before each\n    behaviour bin, context = condition (trial_type, trial_version) one-hot by\n    phase, phase basis, target, onset cursor position and their difference\n    (Methods 4.3 and 4.4); release split labels \"train\" and \"val\".\"\"\"\n    if output_lead_ms is None:\n        output_lead_ms = neural_lead_ms\n    n_time = movement_window_ms // bin_ms\n    history_bins = neural_history_ms // bin_ms\n    lead_bins = neural_lead_ms // bin_ms\n    out_first = (output_lead_ms + output_history_ms) // bin_ms\n    keys = sorted({(int(a), int(b)) for a, b in zip(raw.trials.trial_type, raw.trials.trial_version)})\n    lookup = {k: i for i, k in enumerate(keys)}\n    basis = phase_basis(n_time)\n    neural_trials, context_trials, behavior_trials, conditions, labels, rows = [], [], [], [], [], []\n    for row_index, row in enumerate(raw.trials.itertuples()):\n        onset = int(round(float(row.move_onset_time) * 1000.0 / bin_ms))\n        samples = np.arange(onset, onset + n_time)\n        if (onset - lead_bins - history_bins < 0 or onset - out_first < 0 or samples[-1] >= raw.n_bins\n                or float(row.stop_time) * 1000.0 < float(row.move_onset_time) * 1000.0 + movement_window_ms\n                or not np.isfinite(raw.hand_vel[samples]).all() or not np.isfinite(raw.cursor_pos[onset]).all()):\n            continue\n        neural_trials.append(np.stack([raw.spike_counts[b - lead_bins - history_bins:b - lead_bins].reshape(-1)\n                                       for b in samples]))\n        c = lookup[(int(row.trial_type), int(row.trial_version))]\n        one_hot = np.zeros(len(keys))\n        one_hot[c] = 1.0\n        condition_phase = (one_hot[None, :, None] * basis[:, None, :]).reshape(n_time, -1)\n        targets = np.asarray(raw.target_pos[row_index]).reshape(-1, 2)\n        target = targets[int(row.active_target)].astype(float)\n        cursor = raw.cursor_pos[onset].astype(float)\n        geometry = np.repeat(np.concatenate([target, cursor, target - cursor])[None, :], n_time, axis=0)\n        context_trials.append(np.concatenate([condition_phase, basis, geometry], axis=-1))\n        behavior_trials.append(raw.hand_vel[samples])\n        conditions.append(np.full(n_time, c, dtype=int))\n        labels.append(str(row.split))\n        rows.append(row_index)\n    labels = np.asarray(labels)\n    return TrialDataset(\n        neural=np.stack(neural_trials),\n        context=np.stack(context_trials),\n        behavior=np.stack(behavior_trials),\n        condition=np.stack(conditions),\n        train_indices=np.flatnonzero(labels == \"train\"),\n        test_indices=np.flatnonzero(labels == \"val\"),\n        source_rows=np.asarray(rows),\n    )\n\n\n# --------------------------------------------------------------------------\n# Synthetic generator (synthetic.py generate_synthetic_dataset; Methods 4.8)"
}
```

```
The file entries/du-2026/du2026.py has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "entries/du-2026/du2026.py",
 "old_string": "        target = targets[int(row.active_target)].astype(float)",
 "new_string": "        if not 0 <= int(row.active_target) < len(targets):\n            raise ValueError(f\"active_target {row.active_target} for {len(targets)} targets\")\n        target = targets[int(row.active_target)].astype(float)"
}
```

```
The file entries/du-2026/du2026.py has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "entries/du-2026/du2026.py",
 "old_string": "def synthetic_job(",
 "new_string": "def maze_jobs(asset_id: str, jobs: list) -> dict:\n    from threadpoolctl import threadpool_limits\n\n    with threadpool_limits(1):\n        raw = load_maze_raw(asset_id)\n        out = {}\n        for name, build_kwargs, estimator, estimator_kwargs, keep in jobs:\n            ds = build_maze_dataset(raw, **build_kwargs)\n            out[name] = _drop_arrays(ESTIMATORS[estimator](ds, **estimator_kwargs), keep)\n    return out\n\n\ndef synthetic_job("
}
```

```
The file entries/du-2026/du2026.py has been updated successfully.
```

**Agent**

Quick test of the MC_Maze port.

**Agent calls Bash**

```bash
PY=../../executed/du-2026/.venv/bin/python; time timeout 1800 $PY -c "
import du2026 as d, numpy as np, time
raw=d.load_maze_raw('7ef450a8-8684-42e2-8598-cd38ca2b2e50')
ds=d.build_maze_dataset(raw)
print(raw.n_units, raw.heldout.sum(), len(raw.trials), ds.neural.shape, ds.context.shape, len(ds.train_indices), len(ds.test_indices), len(np.unique(ds.condition[:,0])))
print(np.bincount(ds.condition[ds.test_indices,0]).min())
t=time.time()
r=d.fully_nested(ds, rff_seeds=d.RFF_SEEDS)
print(time.time()-t)
print({k:r[k] for k in ['context_r2','gain','mse_reduction_percent','context_rmse','exact_rmse','replacement_gain']})
print({s:v['gain'] for s,v in r['rff'].items()})
"
```

```
152 38 250 (250, 40, 760) (250, 40, 258) 188 62 27
2
25.114836931228638
{'context_r2': 0.9053326557587491, 'gain': 0.0005131472939913428, 'mse_reduction_percent': 0.542053120961791, 'context_rmse': 81.7552086995645, 'exact_rmse': 81.53332928477487, 'replacement_gain': -3.706274291700733e-05}
{20260802: 4.4798706280030995e-05, 20260803: 7.722608075344695e-05, 20260804: 0.00013864464054752078}

real	0m29.397s
user	1m41.069s
sys	0m0.575s
```

**Agent calls Bash**

```bash
cd $TMPDIR/rel/src/neural_evidence; grep -n "bootstrap" nested_estimators.py | head -20; grep -n "def _conditional_bootstrap\|def _bootstrap" -A40 nested_estimators.py estimators.py | head -70
```

```
22:    _cluster_bootstrap_delta_r2,
413:    n_bootstrap: int = 1000,
540:    exact_ci_low, exact_ci_high = _cluster_bootstrap_delta_r2(
546:        n_bootstrap=n_bootstrap,
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/rel/src/neural_evidence; sed -n 530,560p nested_estimators.py; grep -n "def _cluster_bootstrap_delta_r2" -A45 estimators.py; grep -n "bootstrap" $TMPDIR/rel/scripts/run_primary_analyses.py | head
```

```
test_shape = dataset.behavior[test_indices].shape
    behavior_trials = behavior_test.reshape(test_shape)
    context_trials = context_prediction.reshape(test_shape)
    exact_trials = exact_prediction.reshape(test_shape)
    replacement_trials = replacement_prediction.reshape(test_shape)
    exact_gain = _normalized_gain(behavior_test, context_prediction, exact_prediction)
    replacement_gain = _normalized_gain(
        behavior_test, context_prediction, replacement_prediction
    )
    exact_ci_low, exact_ci_high = _cluster_bootstrap_delta_r2(
        behavior=behavior_trials,
        context_prediction=context_trials,
        full_prediction=exact_trials,
        conditions=dataset.condition[test_indices, 0],
        rng=np.random.default_rng(seed + 501),
        n_bootstrap=n_bootstrap,
    )

    context_mse = float(mean_squared_error(behavior_test, context_prediction))
    exact_mse = float(mean_squared_error(behavior_test, exact_prediction))
[... 64 more lines not kept]
```

**Agent calls Bash**

```bash
grep -n -i "bootstrap" paper/*.txt | head -20
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -n 1495,1510p paper/*.txt; sed -n 1188,1195p paper/*.txt; grep -n "replicates\|resamples\|500\b\|1,000\|1000" paper/*.txt | head
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd entries/du-2026 && python - <<'EOF'
p='du2026.py'; s=open(p).read()
s=s.replace("""                 permutation_seed_offsets: tuple = ()) -> dict:""","""                 permutation_seed_offsets: tuple = (), n_bootstrap: int = 0) -> dict:""",1)
s=s.replace("""    nonlinear-neural RFF learner of
    evaluate_nonlinear_neural_audit for each map seed in rff_seeds (it shares
    the nuisances and differs only in the residual learner).
    \"\"\"""","""    nonlinear-neural RFF learner of
    evaluate_nonlinear_neural_audit for each map seed in rff_seeds (it shares
    the nuisances and differs only in the residual learner). With n_bootstrap,
    the conditional whole-trial interval of estimators.py
    _cluster_bootstrap_delta_r2 (test trials resampled within condition,
    generator seed+501; run_primary_analyses.py --bootstrap default 500, as the
    paper gives no count).
    \"\"\"""",1)
s=s.replace("""    if n_ranks > 1:
        out["rank_gains\"""","""    if n_bootstrap:
        rng = np.random.default_rng(seed + 501)
        c3 = cpred.reshape(shape)
        e3 = exact.reshape(shape)
        cte_cond = conditions[te]
        boots = np.empty(n_bootstrap)
        for b in range(n_bootstrap):
            sampled = np.concatenate([rng.choice(m, size=len(m), replace=True)
                                      for m in (np.flatnonzero(cte_cond == c) for c in np.unique(cte_cond))])
            yb = y3[sampled].reshape(-1, shape[-1])
            boots[b] = normalized_gain(yb, c3[sampled].reshape(-1, shape[-1]), e3[sampled].reshape(-1, shape[-1]))
        out["conditional_ci"] = tuple(float(q) for q in np.quantile(boots, [0.025, 0.975]))
    if n_ranks > 1:
        out["rank_gains\"""",1)
open(p,'w').write(s)
EOF
grep -n "n_bootstrap" du2026.py
```

```
755:                 permutation_seed_offsets: tuple = (), n_bootstrap: int = 0) -> dict:
829:    if n_bootstrap:
834:        boots = np.empty(n_bootstrap)
835:        for b in range(n_bootstrap):
```

**Agent calls Bash**

```bash
cd $TMPDIR/rel/src/neural_evidence; head -40 nested_estimators.py | grep -n import; grep -n import types.py estimators.py | head; grep -n "class TrialDataset" -A30 types.py | head -40; sed -n 405,425p nested_estimators.py; grep -n "class .*Result\|exact_gain\|replacement_gain\|context_r2" nested_estimators.py | head -20
```

```
9:from __future__ import annotations
11:from dataclasses import asdict, dataclass
13:import numpy as np
14:from sklearn.kernel_approximation import RBFSampler
15:from sklearn.metrics import mean_squared_error, r2_score
16:from sklearn.model_selection import StratifiedKFold, train_test_split
17:from sklearn.pipeline import make_pipeline
18:from sklearn.preprocessing import StandardScaler
19:from sklearn.linear_model import Ridge
21:from .estimators import (
27:from .specification_estimators import _normalized_gain, _resolve_split
28:from .robustness_estimators import _ranked_replacement_sources
29:from .types import TrialDataset
types.py:3:from __future__ import annotations
types.py:5:from dataclasses import dataclass
types.py:7:import numpy as np
estimators.py:3:from __future__ import annotations
estimators.py:5:from dataclasses import asdict, dataclass
estimators.py:7:import numpy as np
estimators.py:8:from sklearn.linear_model import Ridge
[... 60 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/rel/src/neural_evidence; grep -n "^from\|^import" specification_estimators.py robustness_estimators.py __init__.py; grep -n "def evaluate_nonlinear_neural_audit" -A20 nested_estimators.py | head -25
```

```
specification_estimators.py:7:from __future__ import annotations
specification_estimators.py:9:from dataclasses import asdict, dataclass
specification_estimators.py:11:import numpy as np
specification_estimators.py:12:from sklearn.linear_model import Ridge
specification_estimators.py:13:from sklearn.kernel_approximation import RBFSampler
specification_estimators.py:14:from sklearn.metrics import mean_squared_error, r2_score
specification_estimators.py:15:from sklearn.model_selection import StratifiedKFold, train_test_split
specification_estimators.py:16:from sklearn.preprocessing import StandardScaler
specification_estimators.py:18:from .estimators import (
specification_estimators.py:25:from .types import TrialDataset
robustness_estimators.py:7:from __future__ import annotations
robustness_estimators.py:9:from dataclasses import asdict, dataclass
robustness_estimators.py:11:import numpy as np
robustness_estimators.py:12:from sklearn.metrics import r2_score
robustness_estimators.py:14:from .estimators import (
robustness_estimators.py:19:from .specification_estimators import (
robustness_estimators.py:24:from .types import TrialDataset
__init__.py:3:from .estimators import EvaluationResult, evaluate_decoders
__init__.py:4:from .synthetic import generate_synthetic_dataset
__init__.py:5:from .types import DatasetSplit, TrialDataset
[... 22 more lines not kept]
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "entries/du-2026/du2026.py",
 "old_string": "def maze_jobs(",
 "new_string": "RELEASE_MODULES = (\"types\", \"estimators\", \"specification_estimators\", \"robustness_estimators\", \"nested_estimators\")\n\n\ndef release_estimators():\n    \"\"\"The paper's own estimator modules, fetched from the release at PAPER_COMMIT\n    into a temporary package (its __init__ is left empty: the real one imports\n    the synthetic generator only), to run next to the ports here.\"\"\"\n    import importlib\n    import sys\n    import tempfile\n    from pathlib import Path\n\n    root = Path(tempfile.mkdtemp()) / \"neural_evidence\"\n    root.mkdir()\n    (root / \"__init__.py\").write_text(\"\")\n    raw = PAPER_CODE.replace(\"github.com\", \"raw.githubusercontent.com\") + f\"/{PAPER_COMMIT}/src/neural_evidence\"\n    for name in RELEASE_MODULES:\n        with urllib.request.urlopen(f\"{raw}/{name}.py\", timeout=120) as response:\n            (root / f\"{name}.py\").write_bytes(response.read())\n    sys.path.insert(0, str(root.parent))\n    return importlib.import_module(\"neural_evidence.nested_estimators\"), importlib.import_module(\"neural_evidence.types\")\n\n\ndef release_dataset(ds: TrialDataset, types_module):\n    \"\"\"A port TrialDataset as the release's TrialDataset (trial_id and phase are not read by the estimators).\"\"\"\n    n, t = ds.neural.shape[:2]\n    return types_module.TrialDataset(\n        neural=ds.neural, context=ds.context, behavior=ds.behavior,\n        trial_id=np.repeat(np.arange(n)[:, None], t, axis=1), condition=ds.condition,\n        phase=np.repeat(np.linspace(0.0, 1.0, t, endpoint=False)[None, :], n, axis=0))\n\n\ndef maze_jobs("
}
```

```
The file entries/du-2026/du2026.py has been updated successfully.
```

**Agent calls Bash**

```bash
cd entries/du-2026; python -c "
import json
nb=json.load(open('02_link_development.ipynb'))
for i,c in enumerate(nb['cells']):
    if i in (1,2,3,4,37,38,39) or 'versions' in ''.join(c['source']):
        print('=== cell',i,c['cell_type'],c.get('metadata',{}).get('tags'))
        print(''.join(c['source']))
"
```

```
=== cell 0 markdown None
# Du, Lai, Hu & Ye (2026) on LINK: development sessions

Paper: Du Z, Lai ZY, Hu L, Ye T. "A Context-Conditional Audit of Trial-Pairing-Dependent Neural
Gain in Motor-Cortex Decoding". bioRxiv preprint posted 2026-08-10,
doi:10.64898/2026.08.04.742876. The claims file (`claims/du-2026.yaml`) was written from that
preprint's full text (main text, legends, Tables 1 to 3, Methods); the supplement was not available.

Dataset: DANDI:001201 (LINK, Temmar et al.), pinned at version **0.251023.2336**, streamed from the
archive. This is the version the paper cites (Methods 4.2, Data availability; protocol, author step
1.3). Two later versions exist (0.261015.2153 and 0.261026.1912); they list the same 312 asset paths
with the same sizes, so the analysis would read the same files; the pinned version is the cited one.

This notebook tests the claims on the 18 development sessions (nine dates with a CO and an RD
session). Other notebooks of this entry: `01_synthetic.ipynb` (synthetic calibration),
`03_link_estimators.ipynb` (estimator families), `04_link_temporal_capacity.ipynb` (temporal offset
and context capacity), `05_link_confirmation.ipynb` (20 confirmation sessions), `06_mc_rtt.ipynb`
(DANDI:000129). The estimators are ports of the paper's released code (tag v1.0-jne-submission,
commit b042fbe), in `du2026.py`, each function naming its source.

[... 103 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/du-2026; python -c "
import json
for f,keys in [('02_link_development.ipynb',['representative-trial']),('04_link_temporal_capacity.ipynb',['141']),('05_link_confirmation.ipynb',['confirm-replacement','EXTRA','extra'])]:
    nb=json.load(open(f))
    for i,c in enumerate(nb['cells']):
        src=''.join(c['source'])
        if any(k in src or k in str(c.get('metadata',{}).get('tags')) for k in keys):
            print('=====',f,'cell',i,c['cell_type'],c.get('metadata',{}).get('tags'))
            print(src)
"
```

```
/bin/bash: line 1: cd: entries/du-2026: No such file or directory
===== 02_link_development.ipynb cell 0 markdown None
# Du, Lai, Hu & Ye (2026) on LINK: development sessions

Paper: Du Z, Lai ZY, Hu L, Ye T. "A Context-Conditional Audit of Trial-Pairing-Dependent Neural
Gain in Motor-Cortex Decoding". bioRxiv preprint posted 2026-08-10,
doi:10.64898/2026.08.04.742876. The claims file (`claims/du-2026.yaml`) was written from that
preprint's full text (main text, legends, Tables 1 to 3, Methods); the supplement was not available.

Dataset: DANDI:001201 (LINK, Temmar et al.), pinned at version **0.251023.2336**, streamed from the
archive. This is the version the paper cites (Methods 4.2, Data availability; protocol, author step
1.3). Two later versions exist (0.261015.2153 and 0.261026.1912); they list the same 312 asset paths
with the same sizes, so the analysis would read the same files; the pinned version is the cited one.

This notebook tests the claims on the 18 development sessions (nine dates with a CO and an RD
session). Other notebooks of this entry: `01_synthetic.ipynb` (synthetic calibration),
`03_link_estimators.ipynb` (estimator families), `04_link_temporal_capacity.ipynb` (temporal offset
and context capacity), `05_link_confirmation.ipynb` (20 confirmation sessions), `06_mc_rtt.ipynb`
(DANDI:000129). The estimators are ports of the paper's released code (tag v1.0-jne-submission,
commit b042fbe), in `du2026.py`, each function naming its source.
[... 202 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n "id: representative-trial" -A30 claims/du-2026.yaml | grep -n "criterion" -A12; ls questions/du-2026.yaml 2>&1
```

```
Exit code 2
11:621-  criterion: Rule of Methods 4.9; ties to the earlier date and the lower trial index. With 18
12-622-    sessions there is no single median session; the paper's tie rule takes the earlier date, read
13-623-    as the lower of the two middle sessions (the ninth in gain order), or the one of the two
14-624-    middle sessions with the earlier date. With an odd number of test trials (113) the median
15-625-    trial is the middle one. What "trial 123" indexes is not stated; readings (a) the row of the
16-626-    session's NWB trials table, (b) the index among the session's usable trials (the code's
17-627-    trial_id), (c) the position among the session's held-out trials. Reproduced when the rule
18-628-    selects 2022-09-21 RD and the selected trial is 123 under a reading; partially reproduced
19-629-    when only the session matches.
20-630-- id: confirm-geometry-gain
21-631-  statement: In the 20 untouched LINK confirmation sessions, SBP geometry-by-phase gain was
22-632-    positive in all 20 and averaged 0.02158 (CO 0.02104, RD 0.02213).
23-633-  source: Results 2.5, paragraph 2; Table 1; Figure 6a
ls: cannot access 'questions/du-2026.yaml': No such file or directory
```

**Agent calls Bash**

```bash
cd entries/du-2026; PY=../../executed/du-2026/.venv/bin/python; $PY - <<'EOF'
import nbformat
p='02_link_development.ipynb'
nb=nbformat.read(p,4)
c=nb.cells[52]
old="""    print(f"{label}: {row.date} {row.task}; median trial: usable-trial index {usable_index}, "
          f"trials-table row {int(r['source_rows'][usable_index])}, position among {len(order)} held-out trials {position}")"""
new="""    # reading (c): the trial's position among the held-out trials in ascending trial order (test_indices
    # itself is in train_test_split's shuffled order, so an index into it is not a position)
    held_out_position = int(np.searchsorted(np.sort(r["test_indices"]), usable_index))
    print(f"{label}: {row.date} {row.task}; median trial: usable-trial index {usable_index}, "
          f"trials-table row {int(r['source_rows'][usable_index])}, position among the {len(order)} held-out trials "
          f"in trial order {held_out_position} (from 0)")"""
assert old in c.source
c.source=c.source.replace(old,new)
# later versions: support for the header statement
src="""# The header says the two later versions list the same assets: compare paths and sizes with the pinned version
pinned = {a["path"]: a["size"] for a in assets}
for version in ("0.261015.2153", "0.261026.1912"):
    other = {a["path"]: a["size"] for a in d.list_assets(d.LINK_ID, version)}
    print(f"version {version}: {len(other)} assets; same paths as {d.LINK_VERSION}: {set(other) == set(pinned)}; "
          f"same sizes: {other == pinned}")"""
nb.cells.insert(2, nbformat.v4.new_code_cell(src))
nbformat.write(nb,p)
EOF
grep -c "searchsorted" 02_link_development.ipynb
```

```
1
```

**Agent calls Bash**

```bash
cd entries/du-2026; ../../executed/du-2026/.venv/bin/python -c "
import du2026 as d
assets=d.list_assets(d.LINK_ID,d.LINK_VERSION)
pinned = {a['path']: a['size'] for a in assets}
for version in ('0.261015.2153', '0.261026.1912'):
    other = {a['path']: a['size'] for a in d.list_assets(d.LINK_ID, version)}
    print(version, len(other), set(other)==set(pinned), other==pinned)
"; curl -s https://api.dandiarchive.org/api/dandisets/001201/versions/ | python -c "import json,sys; print([v['version'] for v in json.load(sys.stdin)['results']])"
```

Result: the fetched text is not kept.

**Agent**

Now notebook 04 (computed feature counts) and 05 (per-seed count of sessions with gain above replacement).

**Agent calls Bash**

```bash
cd entries/du-2026; grep -n "context_mode ==\|context_mode in\|def build_link_dataset" du2026.py | head; sed -n 230,245p du2026.py
```

```
220:def build_link_dataset(
281:        if context_mode in {"geometry_additive", "geometry_tensor", "geometry_quadratic", "causal_history", "causal_history_quadratic"}:
283:        if context_mode in {"geometry_tensor", "geometry_quadratic", "causal_history", "causal_history_quadratic"}:
285:        if context_mode in {"geometry_quadratic", "causal_history_quadratic"}:
290:        if context_mode in {"causal_history", "causal_history_quadratic"}:
407:        if context_mode == "target_only":
409:        elif context_mode == "task_state":
    sample_offset_ms: int | None = None,
    seed: int = 20260726,
    test_size: float = 0.30,
) -> TrialDataset:
    """Port of link.py load_link, from arrays already streamed.

    Defaults are those every LINK run script passes (run_link_context_ladder.py,
    run_primary_analyses.py, run_link_confirmation.py): SBP, 160 ms history
    ending at the behavior bin (lead 0), 100 ms position history (lead 0),
    25 bins of 20 ms (Methods 4.3), 70/30 split stratified by direction
    octant with random_state=seed (Methods 4.5).
    """
    bin_ms = 20
[... 3 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/du-2026; PY=../../executed/du-2026/.venv/bin/python; $PY - <<'EOF'
import nbformat
s=open('du2026.py').read()
old='''            result["n_usable"] = len(ds.neural)
'''
new='''            result["n_usable"] = len(ds.neural)
            result["n_context"] = ds.context.shape[-1]
'''
assert old in s; s=s.replace(old,new); open('du2026.py','w').write(s)
p='04_link_temporal_capacity.ipynb'
nb=nbformat.read(p,4); c=nb.cells[3]
old='''print("context feature counts are 141, 351, 151 and 361 (Methods 4.4); usable trials at the 280 ms window start:",
      sorted(set(r["offset0_nested"]["n_usable"] for r in results)))'''
new='''print("context feature counts (Methods 4.4: 141, 351, 151, 361):",
      {ctx: sorted(set(r[f"SBP_{ctx}_nested"]["n_context"] for r in results))
       for ctx in ("geometry_tensor", "geometry_quadratic", "causal_history", "causal_history_quadratic")})
print("usable trials at the 280 ms window start:", sorted(set(r["offset0_nested"]["n_usable"] for r in results)))'''
assert old in c.source; c.source=c.source.replace(old,new); nbformat.write(nb,p)
p='05_link_confirmation.ipynb'
nb=nbformat.read(p,4); c=nb.cells[12]
c.source += '''
for k in (0,) + EXTRA:
    g_, r_ = table(results, f"geometry_tensor_{SEED + k}"), table(results, f"geometry_tensor_{SEED + k}", "replacement_gain")
    tm = pd.DataFrame({"task": g_.task, "g": g_.gain, "r": r_.replacement_gain}).groupby("task").mean()
    print(f"seed {SEED + k}: sessions with gain above replacement {int((g_.gain > r_.replacement_gain).sum())}/20; "
          f"task means above replacement in CO and RD: {bool((tm.g > tm.r).all())}")'''
nbformat.write(nb,p)
EOF
date -u
```

```
Sat Nov 21 19:27:43 UTC 2026
```

**Agent calls Bash**

```bash
nproc; free -g | head -2
```

```
4
               total        used        free      shared  buff/cache   available
Mem:              15           1          12           0           2          14
```

**Agent**

Now writing the MC_Maze notebook.

**Agent calls Bash**

```bash
cd entries/du-2026; PY=../../executed/du-2026/.venv/bin/python; $PY - <<'EOF'
import nbformat
from nbformat.v4 import new_markdown_cell as md, new_code_cell as code
def tagged(cell, tag):
    cell.metadata["tags"] = [tag]; return cell
cells = []
cells.append(md("""# Du, Lai, Hu & Ye (2026) on MC_Maze (DANDI:000139, data elsewhere)

Paper doi:10.64898/2026.08.04.742876. MC_Maze-medium is not one of the datasets this paper is listed on
in the registry; the claims file marks its claims `data: elsewhere` and names the file:
DANDI:000139 version **0.220113.0408**, `sub-Jenkins/sub-Jenkins_ses-medium_desc-train_behavior+ecephys.nwb`,
streamed. It is an input of this attempt (protocol, author step 1.4). See `02_link_development.ipynb`
for the full claims table.

The loader is a port of the release's `mc_maze.py` (`load_mc_maze`, template context, called with
`neural_lead_ms=80` by `run_primary_analyses.py _run_nlb`), in `du2026.py` (`load_maze_raw`,
`build_maze_dataset`); the estimators are the same ports used for MC_RTT. The last section runs the
release's own estimator code, fetched at commit b042fbe, next to the ports.

| Claim | Status |
|---|---|
| maze-gain | tested |
| rff-maze | tested |
| estimator-family-nlb | MC_Maze part reported here (the outcome rests on MC_RTT, `06_mc_rtt.ipynb`) |"""))
cells.append(code("""import resource, time
import numpy as np
import pandas as pd
import du2026 as d

T0 = time.time()
EXTRA = (1000, 2000, 3000, 4000)
maze_assets = d.list_assets(d.MAZE_ID, d.MAZE_VERSION)
print([(a["path"], a["size"]) for a in maze_assets])
train_asset = next(a for a in maze_assets if a["path"] == d.MAZE_TRAIN_PATH)
raw = d.load_maze_raw(train_asset["asset_id"])
ds = d.build_maze_dataset(raw)"""))
cells.append(tagged(code("""print("behaviour series:", raw.descriptions)
tr = raw.trials
print(f"units: {raw.n_units} ({int(raw.heldout.sum())} marked heldout, all used, as mc_maze.py does); "
      f"spike counts per 20 ms bin {raw.spike_counts.min():.0f} to {raw.spike_counts.max():.0f}, mean rate {raw.spike_counts.mean() / 0.02:.1f} Hz")
print("trials:", len(tr), "split", tr.split.value_counts().to_dict(), "success", tr.success.value_counts().to_dict())
conds = tr.groupby(["trial_type", "trial_version"]).size()
print(f"conditions (trial_type, trial_version): {len(conds)}; trials per condition {conds.min()} to {conds.max()}")
val_counts = pd.Series(ds.condition[ds.test_indices, 0]).value_counts()
print(f"validation trials per condition: {val_counts.min()} to {val_counts.max()} (replacement needs at least 2)")
after = (tr.stop_time - tr.move_onset_time) * 1000
print(f"ms from movement onset to trial stop: {after.min():.0f} to {after.max():.0f}; trials with fewer than 800 ms: {int((after < 800).sum())}")
print(f"hand velocity range {np.nanmin(raw.hand_vel):.1f} to {np.nanmax(raw.hand_vel):.1f}; cursor {np.nanmin(raw.cursor_pos):.1f} to {np.nanmax(raw.cursor_pos):.1f}")
print(f"20 ms bins with no behaviour sample: {int((~np.isfinite(raw.hand_vel).all(axis=1)).sum())} of {raw.n_bins}")
print("analysis arrays: neural", ds.neural.shape, "context", ds.context.shape, "behaviour", ds.behavior.shape,
      "train/val", len(ds.train_indices), len(ds.test_indices))
# units and alignment: hand velocity (mm/s) against the derivative of cursor position (mm per 20 ms bin)
dcur = np.gradient(raw.cursor_pos, axis=0) / 0.02
for lag in (-2, 0, 2):
    a, b = raw.hand_vel[max(0, lag):len(dcur) + min(0, lag)], dcur[max(0, -lag):len(dcur) - max(0, lag)]
    ok = np.isfinite(a).all(axis=1) & np.isfinite(b).all(axis=1)
    print(f"corr(hand velocity, cursor velocity shifted {lag} bins): x {np.corrcoef(a[ok, 0], b[ok, 0])[0, 1]:.3f}, "
          f"y {np.corrcoef(a[ok, 1], b[ok, 1])[0, 1]:.3f}; SD ratio x {np.std(a[ok, 0]) / np.std(b[ok, 0]):.2f}")
# clock check: decode hand velocity from 100 ms of spikes ending `lag` bins before the behaviour bin, within trials
from sklearn.linear_model import Ridge
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import r2_score
onsets = np.round(tr.move_onset_time.to_numpy() * 50).astype(int)
bins_ = np.concatenate([np.arange(o - 10, o + 40) for o in onsets])
bins_ = bins_[(bins_ > 40) & (bins_ < raw.n_bins - 40)]
bins_ = bins_[np.isfinite(raw.hand_vel[bins_]).all(axis=1)]
half = len(bins_) * 3 // 4
row = {}
for lag in (-10, -4, 0, 2, 4, 6, 10, 25):
    X = np.stack([raw.spike_counts[b - lag - 5:b - lag].reshape(-1) for b in bins_])
    m = make_pipeline(StandardScaler(), Ridge(alpha=1000.0)).fit(X[:half], raw.hand_vel[bins_[:half]])
    row[lag] = round(r2_score(raw.hand_vel[bins_[half:]], m.predict(X[half:]), multioutput="variance_weighted"), 3)
print("held-out R2 (last quarter of the trials) by lag in bins:", row)"""), "sanity"))
cells.append(md("""## maze-gain

> In MC_Maze, a condition-by-phase template with geometry gave context-only R2 of 0.9053, and the fully
> nested neural gain beyond it was 0.00051 (conditional interval 0.00026 to 0.00076), a 0.54% MSE
> reduction (RMSE 81.76 to 81.53), with replacement gain -0.00004.

The criterion gives the data and the method (40 bins after measured movement onset, five spike bins
ending 80 ms before behaviour, 258-feature template context) and no rule; the four expected values are
compared with their tolerances, as for rtt-gain. Estimator seed 20260726 (`run_primary_analyses.py`);
the release split is fixed, and the estimator's folds and inner splits are also run under seeds plus
1000 to 4000. The conditional whole-trial interval is the release's (`_cluster_bootstrap_delta_r2`,
500 resamples, the script's default; the paper gives no count). The same fits give the three
nonlinear-neural maps (rff-maze)."""))
cells.append(tagged(code("""SEED = 20260726
jobs = [(f"nested_{SEED + k}", {}, "nested", dict(seed=SEED + k, rff_seeds=d.RFF_SEEDS, n_bootstrap=500 if k == 0 else 0), False)
        for k in (0,) + EXTRA]
jobs_family = [("block", {}, "block", {"seed": SEED}, False), ("rffctx", {}, "rff_context", {"seed": SEED}, False)]
t = time.time()
out = d.run_parallel(d.maze_jobs, [(train_asset["asset_id"], [j]) for j in jobs + jobs_family])
res = {k: v for o in out for k, v in o.items()}
print(f"fits in {(time.time() - t) / 60:.1f} min")
r = res[f"nested_{SEED}"]
exp = [("context-only R2", r["context_r2"], 0.9053, 0.09053), ("fully nested gain", r["gain"], 0.00051, 0.00025),
       ("% MSE reduction", r["mse_reduction_percent"], 0.54, 0.054), ("replacement gain", r["replacement_gain"], -0.00004, 0.000004)]
for label, v, e, tol in exp:
    print(f"{label}: {v:.7f} (expected {e} +- {tol}; within: {abs(v - e) <= tol})")
print(f"context RMSE {r['context_rmse']:.2f}, context-plus-neural RMSE {r['exact_rmse']:.2f} (paper 81.76 to 81.53)")
print(f"conditional interval {r['conditional_ci'][0]:.5f} to {r['conditional_ci'][1]:.5f} (paper 0.00026 to 0.00076)")
print("context features:", ds.context.shape[-1], "(258 in the criterion)")
for k in (0,) + EXTRA:
    rr = res[f"nested_{SEED + k}"]
    print(f"seed {SEED + k}: context R2 {rr['context_r2']:.4f}, gain {rr['gain']:.6f}, MSE reduction {rr['mse_reduction_percent']:.3f}%, "
          f"replacement {rr['replacement_gain']:.7f}")
print("penalties (context, residualizer, residual learner):", r["context_alpha"], r["residualizer_alpha"], r["innovation_alpha"])"""), "claim:maze-gain"))
cells.append(md("""## rff-maze

> Under the three nonlinear-neural maps, MC_Maze gain stayed practically zero (0.000045 to 0.000139).

Criterion as rff-rtt: D = 512 radial-basis random Fourier features, gamma = 1/p, map seeds 20260802 to
20260804 (`run_nonlinear_seed_sensitivity.py`), fully nested linear nuisances."""))
cells.append(tagged(code("""g = {s: res[f"nested_{SEED}"]["rff"][s]["gain"] for s in d.RFF_SEEDS}
print({s: round(v, 7) for s, v in g.items()}, "penalties", {s: res[f"nested_{SEED}"]["rff"][s]["alpha"] for s in d.RFF_SEEDS})
lo, hi = min(g.values()), max(g.values())
print(f"lowest {lo:.7f} (expected 0.000045 +- 0.0000045; within: {abs(lo - 0.000045) <= 0.0000045}); "
      f"highest {hi:.7f} (expected 0.000139 +- 0.0000139; within: {abs(hi - 0.000139) <= 0.0000139})")
for k in EXTRA:
    gg = [res[f"nested_{SEED + k}"]["rff"][s]["gain"] for s in d.RFF_SEEDS]
    print(f"estimator seed {SEED + k}: map gains {min(gg):.7f} to {max(gg):.7f}")"""), "claim:rff-maze"))
cells.append(md("""## estimator-family-nlb, MC_Maze part

The outcome of estimator-family-nlb rests on MC_RTT (`06_mc_rtt.ipynb`); the criterion reports the
MC_Maze part when the file is used, reading "near zero" as an absolute gain below 0.01
(`run_primary_analyses.py`, `maze_abs_gain_below_0_01`). Estimators as for MC_RTT: block penalties
and nonlinear context under the release's setting."""))
cells.append(code("""print(f"block penalties: gain {res['block']['gain']:.6f} (penalties {res['block']['penalties']}); "
      f"nonlinear context (D 256, g chosen {res['rffctx']['gamma']}): gain {res['rffctx']['gain']:.6f}; fully nested linear {r['gain']:.6f}")
print("absolute MC_Maze gain below 0.01 under both families:", abs(res["block"]["gain"]) < 0.01 and abs(res["rffctx"]["gain"]) < 0.01)"""))
cells.append(md("""## The ports next to the release's own code

The verifier asked for one release function run next to its port. The release's estimator modules
(`types`, `estimators`, `specification_estimators`, `robustness_estimators`, `nested_estimators`) are
fetched at commit b042fbe and run on the same arrays: `evaluate_fully_nested_audit` and
`evaluate_nonlinear_neural_audit` on MC_Maze, and `evaluate_fully_nested_audit` on one LINK session
(2021-10-15 CO, SBP, geometry by phase, split seed 20260726). The loaders are the ports in both columns."""))
cells.append(code("""from threadpoolctl import threadpool_limits
release, release_types = d.release_estimators()
rows = []
with threadpool_limits(1):
    rel = release.evaluate_fully_nested_audit(d.release_dataset(ds, release_types), seed=SEED, train_indices=ds.train_indices,
                                              test_indices=ds.test_indices, n_bootstrap=500)
    rows += [("MC_Maze", "context R2", r["context_r2"], rel.context_r2), ("MC_Maze", "gain", r["gain"], rel.exact_gain),
             ("MC_Maze", "replacement gain", r["replacement_gain"], rel.replacement_gain),
             ("MC_Maze", "interval low", r["conditional_ci"][0], rel.exact_gain_ci_low),
             ("MC_Maze", "interval high", r["conditional_ci"][1], rel.exact_gain_ci_high)]
    for s in d.RFF_SEEDS:
        nl = release.evaluate_nonlinear_neural_audit(d.release_dataset(ds, release_types), seed=SEED, rff_seed=s,
                                                     train_indices=ds.train_indices, test_indices=ds.test_indices)
        rows.append(("MC_Maze", f"RFF gain, map {s}", res[f"nested_{SEED}"]["rff"][s]["gain"], nl.nonlinear_gain))
    link_assets = d.list_assets(d.LINK_ID, d.LINK_VERSION)
    link_asset = next(a for a in link_assets if "20211015" in a["path"] and "CO" in d.load_link_session(a["asset_id"], a["path"], signals=("SpikingBandPower",)).task)
    session = d.load_link_session(link_asset["asset_id"], link_asset["path"], signals=("SpikingBandPower",))
    lds = d.build_link_dataset(session, signal="SpikingBandPower", context_mode="geometry_tensor", seed=SEED)
    port_link = d.fully_nested(lds, seed=SEED)
    rel_link = release.evaluate_fully_nested_audit(d.release_dataset(lds, release_types), seed=SEED, train_indices=lds.train_indices,
                                                   test_indices=lds.test_indices, n_bootstrap=10)
    rows += [(f"LINK {session.date} {session.task}", "context R2", port_link["context_r2"], rel_link.context_r2),
             (f"LINK {session.date} {session.task}", "gain", port_link["gain"], rel_link.exact_gain),
             (f"LINK {session.date} {session.task}", "replacement gain", port_link["replacement_gain"], rel_link.replacement_gain)]
cmp_ = pd.DataFrame(rows, columns=["data", "quantity", "port", "release"])
cmp_["abs difference"] = (cmp_.port - cmp_.release).abs()
pd.set_option("display.float_format", lambda v: f"{v:.9f}")
print(cmp_.to_string())
print(f"largest absolute difference: {cmp_['abs difference'].max():.3g}")
print(f"run time {(time.time() - T0) / 60:.1f} min; peak memory {resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1e6:.2f} GB")"""))
cells.append(md("""## Summary

| Claim | Outcome |
|---|---|
| maze-gain | to be filled |
| rff-maze | to be filled |"""))
nb = nbformat.v4.new_notebook(cells=cells)
nb.metadata = nbformat.read('06_mc_rtt.ipynb', 4).metadata
nbformat.write(nb, '07_mc_maze.ipynb')
EOF
grep -n "nonlinear_gain\|class NonlinearNeuralAuditResult" -A6 $TMPDIR/rel/src/neural_evidence/nested_estimators.py | head -12
```

```
122:class NonlinearNeuralAuditResult:
123-    context_r2: float
124-    nonlinear_exact_r2: float
125:    nonlinear_gain: float
126-    nonlinear_replacement_gain: float
127-    context_mse: float
128-    nonlinear_mse: float
129-    normalized_nonlinear_rmse: float
130-    mse_reduction_percent: float
131-    innovation_alpha: float
--
866:        nonlinear_gain=_normalized_gain(
```

**Agent calls Bash**

```bash
cd entries/du-2026; PY=../../executed/du-2026/.venv/bin/python; $PY - <<'EOF'
import nbformat
p='07_mc_maze.ipynb'; nb=nbformat.read(p,4)
c=nb.cells[10]
old='''    link_asset = next(a for a in link_assets if "20211015" in a["path"] and "CO" in d.load_link_session(a["asset_id"], a["path"], signals=("SpikingBandPower",)).task)'''
new='''    link_asset = next(a for a in link_assets if d.session_date(a["path"]) == "2021-10-15"
                      and d.link_task_from_metadata(d.asset_metadata(d.LINK_ID, d.LINK_VERSION, a["asset_id"])) == "CO")'''
assert old in c.source; c.source=c.source.replace(old,new); nbformat.write(nb,p)
EOF
cd entries/du-2026 && time timeout 3000 ../../executed/du-2026/.venv/bin/jupyter nbconvert --to notebook --execute --ExecutePreprocessor.timeout=3000 --output-dir $TMPDIR/ex --output 07_mc_maze.ipynb 07_mc_maze.ipynb 2>&1 | tail -3
```

```
[NbConvertApp] Converting notebook 07_mc_maze.ipynb to notebook
[IPKernelApp] WARNING | Kernel is running over TCP without encryption. All communication (including code and outputs) is sent in plain text and is susceptible to eavesdropping. Use IPC transport or launch with kernel manager-provisioned CurveZMQ keys to enable transport encryption.
[NbConvertApp] Writing 22728 bytes to /tmp/claude-1001/ex/07_mc_maze.ipynb

real	1m43.391s
user	3m19.596s
sys	0m5.087s
```

**Agent calls Bash**

```bash
cd $TMPDIR/ex; python3 -c "
import json
nb=json.load(open('07_mc_maze.ipynb'))
for i,c in enumerate(nb['cells']):
    if c['cell_type']=='code':
        print('=== cell',i)
        for o in c.get('outputs',[]): print(o.get('text', o.get('data',{}).get('text/plain','')) if isinstance(o.get('text',''),str) else ''.join(o['text']), o.get('ename',''), o.get('evalue',''))
"
```

```
=== cell 1
[('sub-Jenkins/sub-Jenkins_ses-medium_desc-test_ecephys.nwb', 695928), ('sub-Jenkins/sub-Jenkins_ses-medium_desc-train_behavior+ecephys.nwb', 76604764)]
  
=== cell 2
behaviour series: {'hand_vel': {'unit': 'm/s', 'conversion': np.float64(0.001), 'description': 'Monkey hand velocity in mm/s, calculated from monkey hand position. First column x, second column y'}, 'cursor_pos': {'unit': 'meters', 'conversion': np.float64(0.001), 'description': 'Cursor position in mm. First column x, second column y'}}
units: 152 (38 marked heldout, all used, as mc_maze.py does); spike counts per 20 ms bin 0 to 6, mean rate 3.1 Hz
trials: 250 split {'train': 188, 'val': 62} success {True: 250}
conditions (trial_type, trial_version): 27; trials per condition 8 to 10
validation trials per condition: 2 to 3 (replacement needs at least 2)
ms from movement onset to trial stop: 959 to 1742; trials with fewer than 800 ms: 0
hand velocity range -1156.5 to 1003.2; cursor -139.2 to 159.5
20 ms bins with no behaviour sample: 600 of 38644
analysis arrays: neural (250, 40, 760) context (250, 40, 258) behaviour (250, 40, 2) train/val 188 62
corr(hand velocity, cursor velocity shifted -2 bins): x 0.635, y 0.734; SD ratio x 0.69
corr(hand velocity, cursor velocity shifted 0 bins): x 0.787, y 0.873; SD ratio x 0.78
corr(hand velocity, cursor velocity shifted 2 bins): x 0.589, y 0.679; SD ratio x 0.69
  
held-out R2 (last quarter of the trials) by lag in bins: {-10: 0.295, -4: 0.288, 0: 0.354, 2: 0.39, 4: 0.393, 6: 0.373, 10: 0.301, 25: 0.064}
  
=== cell 4
[... 43 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/du-2026; PY=../../executed/du-2026/.venv/bin/python; $PY - <<'EOF'
import nbformat
from nbformat.v4 import new_markdown_cell as md
def tagged(cell, tag):
    cell.metadata["tags"] = [tag]; return cell
p='07_mc_maze.ipynb'; nb=nbformat.read(p,4)
r_maze = tagged(md("""**Result: reproduced (seed sensitive).** Under estimator seed 20260726 the context-only R2 is 0.90533, the fully nested gain 0.000513, the MSE reduction 0.542% (RMSE 81.76 to 81.53) and the replacement gain -0.0000371; all four are within tolerance, and the conditional interval, 0.00026 to 0.00076, equals the paper's. The release's own code gives the same values on the same arrays (last section). The neural gain is small and depends on the estimator's folds: under seeds plus 1000 to 4000 the gain is -0.000138, 0.000479, 0.000528 and 0.000509, and the replacement gain -0.0027212, 0.0000294, -0.0000190 and 0.0000075, so the replacement gain is outside its tolerance under every other seed and the gain under one."""), "claim:maze-gain")
r_rff = tagged(md("""**Result: reproduced (seed sensitive).** The three maps give MC_Maze gains of 0.0000448, 0.0000772 and 0.0001386, so the lowest and highest are within tolerance of the paper's 0.000045 and 0.000139. Under estimator seeds plus 1000 to 4000 the lowest of the three is 0.0000263 to 0.0000624, outside the tolerance under each, while every map gain stays positive and below 0.00014."""), "claim:rff-maze")
r_fam = md("""MC_Maze part: the block-penalty gain is 0.000455 and the nonlinear-context gain -0.000243, both of absolute size below 0.01, so MC_Maze is near zero under both families on the criterion's reading. This part does not enter the outcome of estimator-family-nlb.""")
summary = md("""## Summary

| Claim | Outcome |
|---|---|
| maze-gain | reproduced (seed sensitive) |
| rff-maze | reproduced (seed sensitive) |
| estimator-family-nlb | MC_Maze part holds (outcome in `06_mc_rtt.ipynb`) |

MC_Maze was read from DANDI:000139, which the paper uses but which is not listed as one of its
datasets here; the claims mark it as data elsewhere. Every value equals the paper's under estimator
seed 20260726. The gains are about 0.0005 and smaller, and the replacement gain and the lowest
nonlinear-map gain fall outside their 10% tolerances under the other estimator seeds. The release's
estimator code, run on the same arrays, gives the ported values exactly (largest absolute difference 0),
on MC_Maze and on one LINK session.

What was found about the file: 250 trials, all successful, 27 conditions with 8 to 10 trials each, 152
units (38 marked heldout) and the 188/62 split, as the paper states. Behaviour is stored only around
trials (600 of 38,644 20 ms bins have no sample), and none of the analysis windows reaches a gap. The
behaviour series carry unit m/s or meters with conversion 0.001, so the stored values are mm/s and mm,
as their descriptions say. Velocity decoding from spikes peaks when the spikes end 2 to 4 bins (40 to
80 ms) before the behaviour bin.""")
cells = nb.cells
# insert result cells after code cells 4, 6, 8; replace the summary
new=[]
for i,c in enumerate(cells[:-1]):
    new.append(c)
    if i==4: new.append(r_maze)
    if i==6: new.append(r_rff)
    if i==8: new.append(r_fam)
new.append(summary)
nb.cells=new
nbformat.write(nb,p)

p='06_mc_rtt.ipynb'; nb=nbformat.read(p,4)
c=nb.cells[7]
old='dict(seed=SEED + k, rff_seeds=d.RFF_SEEDS if k == 0 else ())'
assert old in c.source
c.source=c.source.replace(old,'dict(seed=SEED + k, rff_seeds=d.RFF_SEEDS if k == 0 else (), n_bootstrap=500 if k == 0 else 0)')
c.source=c.source.replace('''for k in (0,) + EXTRA:
    rr =''','''print(f"conditional interval {r['conditional_ci'][0]:.5f} to {r['conditional_ci'][1]:.5f} (paper 0.05371 to 0.08478; "
      "estimators.py _cluster_bootstrap_delta_r2, 500 resamples, the run_primary_analyses.py default)")
for k in (0,) + EXTRA:
    rr =''')
assert 'conditional interval' in c.source
h=nb.cells[0]
h.source=h.source.replace("| estimator-family-nlb | MC_RTT part tested (reading (a) of the nonlinear context); MC_Maze part not run (DANDI:000139 is not one of this attempt's datasets) |\n| maze-gain, rff-maze | blocked (DANDI:000139 not used) |",
 "| estimator-family-nlb | tested on MC_RTT (reading (a) of the nonlinear context); the MC_Maze part is reported in `07_mc_maze.ipynb` |\n| maze-gain, rff-maze | tested in `07_mc_maze.ipynb` (DANDI:000139, data elsewhere) |")
assert '07_mc_maze' in h.source
nbformat.write(nb,p)
for i,c in enumerate(nb.cells):
    if c.cell_type=='markdown' and ('Maze' in c.source): print(i, c.source[:3000]); print('---')
EOF
```

```
0 # Du, Lai, Hu & Ye (2026) on MC_RTT (DANDI:000129)

Paper doi:10.64898/2026.08.04.742876 (claims file written from the bioRxiv full text, without the
supplement). Dataset: DANDI:000129 (MC_RTT, Neural Latents Benchmark), pinned at version
**0.241017.1444**, the version the paper cites (Methods 4.2, Data availability) and the only published
version; file `sub-Indy/sub-Indy_desc-train_behavior+ecephys.nwb`, streamed. See
`02_link_development.ipynb` for the full claims table.

| Claim | Status |
|---|---|
| rtt-data | tested |
| rtt-gain | tested |
| rff-rtt | tested |
| estimator-family-nlb | tested on MC_RTT (reading (a) of the nonlinear context); the MC_Maze part is reported in `07_mc_maze.ipynb` |
| maze-gain, rff-maze | tested in `07_mc_maze.ipynb` (DANDI:000139, data elsewhere) |
---
12 ## estimator-family-nlb

> Under the separate-block and nonlinear-context estimators, MC_RTT gain remained positive while
> MC_Maze remained near zero.
[... 21 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/du-2026; PY=../../executed/du-2026/.venv/bin/python; $PY - <<'EOF'
import nbformat
p='06_mc_rtt.ipynb'; nb=nbformat.read(p,4)
c=nb.cells[14]
c.source=c.source.replace("The MC_Maze part of the statement was not tested: DANDI:000139 was not read in this attempt.",
 "The MC_Maze part, which the criterion reports without making the outcome depend on it, holds in `07_mc_maze.ipynb`: block-penalty gain 0.000455 and nonlinear-context gain -0.000243, both of absolute size below 0.01.")
c.source=c.source.replace("**Result: reproduced (MC_RTT part).**","**Result: reproduced.**")
s=nb.cells[15]
s.source=s.source.replace("| estimator-family-nlb | reproduced (MC_RTT part only) |\n| maze-gain, rff-maze | blocked (MC_Maze, DANDI:000139, not read in this attempt) |",
 "| estimator-family-nlb | reproduced (MC_Maze part in `07_mc_maze.ipynb`) |\n| maze-gain, rff-maze | see `07_mc_maze.ipynb` |")
assert '07_mc_maze' in s.source and '07_mc_maze' in c.source
nbformat.write(nb,p)
p='02_link_development.ipynb'; nb=nbformat.read(p,4)
h=nb.cells[0]
h.source=h.source.replace("`05_link_confirmation.ipynb` (20 confirmation sessions), `06_mc_rtt.ipynb`\n(DANDI:000129).","`05_link_confirmation.ipynb` (20 confirmation sessions), `06_mc_rtt.ipynb`\n(DANDI:000129), `07_mc_maze.ipynb` (DANDI:000139, data elsewhere).")
h.source=h.source.replace("| rtt-data, rtt-gain, rff-rtt, estimator-family-nlb | 06 | tested (MC_Maze part of estimator-family-nlb not run) |\n| maze-gain, rff-maze | none | blocked: MC_Maze (DANDI:000139) is not one of this attempt's datasets |",
 "| rtt-data, rtt-gain, rff-rtt, estimator-family-nlb | 06 | tested (MC_Maze part of estimator-family-nlb in 07) |\n| maze-gain, rff-maze | 07 | tested on MC_Maze (DANDI:000139 version 0.220113.0408, data elsewhere) |")
h.source=h.source.replace("Two later versions exist (0.261015.2153 and 0.261026.1912); they list the same 312 asset paths\nwith the same sizes, so","Two later versions exist (0.261015.2153 and 0.261026.1912); they list the same 312 asset paths\nwith the same sizes (next cell), so")
assert '07_mc_maze' in h.source and 'next cell' in h.source, h.source
nbformat.write(nb,p)
EOF
grep -n "Maze\|maze" README.md entry.yaml
```

```
README.md:19:| MC_Maze (2) | none | Blocked: DANDI:000139 not read |
entry.yaml:10:  context-capacity analyses, and the MC_RTT results. The MC_Maze claims (dandiset 000139) are not
```

**Agent calls Bash**

```bash
cd entries/du-2026; cat README.md
```

```
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

[... 5 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/du-2026; python3 - <<'EOF'
p='README.md'; s=open(p).read()
s=s.replace("# Du, Lai, Hu & Ye (2026) on LINK and MC_RTT","# Du, Lai, Hu & Ye (2026) on LINK, MC_RTT and MC_Maze")
s=s.replace("""[DANDI:000129](https://dandiarchive.org/dandiset/000129/0.241017.1444) (MC_RTT), at the versions the
paper cites, and""","""[DANDI:000129](https://dandiarchive.org/dandiset/000129/0.241017.1444) (MC_RTT), at the versions the
paper cites, on [DANDI:000139](https://dandiarchive.org/dandiset/000139/0.220113.0408) (MC_Maze-medium,
data elsewhere, at the version the claims file names), and""")
s=s.replace("| MC_Maze (2) | none | Blocked: DANDI:000139 not read |","| MC_Maze (2) | `07_mc_maze.ipynb` | Reproduced, seed sensitive |")
s=s.replace("""their 10% tolerances. The attempt""","""their 10% tolerances. The MC_Maze gains (about 0.0005 and smaller) likewise match the paper under its
estimator seed and move outside the tolerances under others. `07_mc_maze.ipynb` also runs the
release's own estimator code next to the ports, which give the same values. The attempt""")
open(p,'w').write(s)
p='entry.yaml'; s=open(p).read()
s=s.replace("""  context-capacity analyses, and the MC_RTT results. The MC_Maze claims (dandiset 000139) are not
  tested.""","""  context-capacity analyses, and the MC_RTT results, and the MC_Maze results on dandiset 000139 (data
  elsewhere).""")
s=s.replace("""  title: MC_RTT
  runtime_minutes: 2
""","""  title: MC_RTT
  runtime_minutes: 2
- path: 07_mc_maze.ipynb
  title: MC_Maze, and the ports next to the release's code
  runtime_minutes: 2
""")
s=s.replace("""- id: dandi:000129/0.241017.1444
  relation: uses_data
""","""- id: dandi:000129/0.241017.1444
  relation: uses_data
- id: dandi:000139/0.220113.0408
  relation: uses_data
""")
open(p,'w').write(s)
EOF
sed -n 1,12p entry.yaml; grep -n "uses_data" -r ../../entries/*/entry.yaml | head -3
```

```
schema_version: 1
name: du-2026
type: reproduction
title: Context-conditional neural gain in motor-cortex decoding (Du et al. 2026)
description: Tests the findings of Du, Lai, Hu and Ye (2026) on LINK (dandiset 001201, one macaque,
  18 development and 20 confirmation sessions) and MC_RTT (dandiset 000129), and their matched-seed
  synthetic calibration. It ports the paper's released estimators and recomputes the context ladder,
  the fully nested gains with trial replacement and permutation controls, the practical magnitudes,
  the confirmation sessions, the nonlinear and estimator-family sensitivities, the temporal-offset and
  context-capacity analyses, and the MC_RTT results, and the MC_Maze results on dandiset 000139 (data
  elsewhere).
license: Apache-2.0
../../entries/amjad-2025/entry.yaml:20:  relation: uses_data
../../entries/andrews-2024/entry.yaml:20:  relation: uses_data
../../entries/armstrong-2026/entry.yaml:19:  relation: uses_data
```

**Agent calls Bash**

```bash
cd  sed -i 's/  context-capacity analyses, and the MC_RTT results, and the MC_Maze results on dandiset 000139 (data/  context-capacity analyses, the MC_RTT results and the MC_Maze results on dandiset 000139 (data/' entries/du-2026/entry.yaml; grep -rn "uses_data" docs/*.md | head -5; grep -rln "data: elsewhere" claims | head -5
```

```
claims/dana-2016.yaml
claims/pagan-2025.yaml
claims/mallory-2021.yaml
claims/mills-2026.yaml
claims/gabriel-2025.yaml
```

**Agent calls Bash**

```bash
cd  for p in dana-2016 pagan-2025 mallory-2021 gabriel-2025; do ls entries | grep "^$p" && grep -n "related" -A8 entries/$p*/entry.yaml; grep -n "elsewhere\|inputs" -A3 attempts/$p-01.yaml 2>/dev/null | head -12; done
```

```
dana-2016
19:related:
20-- id: crcns:cai-2/unversioned
21-  relation: uses_data
22-- id: doi:10.7554/elife.12727
23-  relation: reproduces
23:inputs:
24-- what: Supplementary file 1 of the paper (RCaMP1h variant screen), streamed from https://cdn.elifesciences.org/articles/12727/elife-12727-supp1-v2.xlsx,
25-    for screen-single-mutations-improved and culture-jrcamp1-sensitivity.
26-  source: doi:10.7554/eLife.12727.030
--
319:    file, so it was not tried, and whether it should be data elsewhere is asked of a reader (questions/dana-2016.yaml).
320-- claim: culture-jrcamp1-brighter
321-  outcome: blocked
322-  blocked_by: data_missing
--
344:  notes: The V1 grating imaging of Figure 3e is not in cai-2 and not deposited elsewhere. Looked in the paper's data statement
345-    (Materials and methods, Reagent distribution, which names only CRCNS doi:10.6080/K0W37T87 for data) and in the CRCNS
pagan-2025
18:related:
[... 58 more lines not kept]
```

**Agent calls Bash**

```bash
cd  date -u; timeout 600 python tools/entry.py check entries/du-2026 2>&1 | tail -15
```

```
Sat Nov 21 19:31:27 UTC 2026
0 error(s)
```

**Agent calls Bash**

```bash
cd  time timeout 7000 python tools/entry.py all entries/du-2026 2>&1 | tail -20
```

```
Installed kernelspec registry-du-2026 in executed/du-2026/.venv/share/jupyter/kernels/registry-du-2026
0 error(s)
pass  01_synthetic.ipynb  (107 s)
pass  02_link_development.ipynb  (822 s)
pass  03_link_estimators.ipynb  (497 s)
pass  04_link_temporal_capacity.ipynb  (633 s)
pass  05_link_confirmation.ipynb  (350 s)
pass  06_mc_rtt.ipynb  (54 s)
pass  07_mc_maze.ipynb  (103 s)

real	42m55.020s
user	136m14.161s
sys	1m57.102s
```

**Agent**

The full run passed in 43 minutes. Now checking the outputs against every stated conclusion.

**Agent calls Bash**

```bash
cd executed/du-2026; cat > $TMPDIR/show.py <<'EOF'
import json,sys
nb=json.load(open(sys.argv[1]))
want=[int(x) for x in sys.argv[2:]] if len(sys.argv)>2 else None
for i,c in enumerate(nb['cells']):
    if want is not None and i not in want: continue
    if c['cell_type']=='code':
        print('=== cell',i, c.get('metadata',{}).get('tags'))
        for o in c.get('outputs',[]):
            t=o.get('text') or o.get('data',{}).get('text/plain','')
            print(''.join(t) if isinstance(t,list) else t, o.get('ename',''), o.get('evalue',''))
    else:
        print('--- md',i, c['source'][:1500] if isinstance(c['source'],str) else ''.join(c['source'])[:1500])
EOF
python3 $TMPDIR/show.py 07_mc_maze.ipynb | head -120
```

```
--- md 0 # Du, Lai, Hu & Ye (2026) on MC_Maze (DANDI:000139, data elsewhere)

Paper doi:10.64898/2026.08.04.742876. MC_Maze-medium is not one of the datasets this paper is listed on
in the registry; the claims file marks its claims `data: elsewhere` and names the file:
DANDI:000139 version **0.220113.0408**, `sub-Jenkins/sub-Jenkins_ses-medium_desc-train_behavior+ecephys.nwb`,
streamed. It is an input of this attempt (protocol, author step 1.4). See `02_link_development.ipynb`
for the full claims table.

The loader is a port of the release's `mc_maze.py` (`load_mc_maze`, template context, called with
`neural_lead_ms=80` by `run_primary_analyses.py _run_nlb`), in `du2026.py` (`load_maze_raw`,
`build_maze_dataset`); the estimators are the same ports used for MC_RTT. The last section runs the
release's own estimator code, fetched at commit b042fbe, next to the ports.

| Claim | Status |
|---|---|
| maze-gain | tested |
| rff-maze | tested |
| estimator-family-nlb | MC_Maze part reported here (the outcome rests on MC_RTT, `06_mc_rtt.ipynb`) |
=== cell 1 None
[('sub-Jenkins/sub-Jenkins_ses-medium_desc-test_ecephys.nwb', 695928), ('sub-Jenkins/sub-Jenkins_ses-medium_desc-train_behavior+ecephys.nwb', 76604764)]
[... 100 more lines not kept]
```

**Agent calls Bash**

```bash
cd executed/du-2026; python3 $TMPDIR/show.py 02_link_development.ipynb 2 53 54; python3 $TMPDIR/show.py 04_link_temporal_capacity.ipynb 3; python3 $TMPDIR/show.py 05_link_confirmation.ipynb 12 13 17; python3 $TMPDIR/show.py 06_mc_rtt.ipynb 7
```

```
=== cell 2 None
version 0.261015.2153: 312 assets; same paths as 0.251023.2336: True; same sizes: True
  
version 0.261026.1912: 312 assets; same paths as 0.251023.2336: True; same sizes: True
  
=== cell 53 ['claim:representative-trial']
          date task     gain   i
0   2022-02-25   RD  0.00283   2
1   2022-04-29   CO  0.01164   9
2   2022-05-13   RD  0.01262  10
3   2022-05-13   CO  0.01389  11
4   2022-02-25   CO  0.01408   3
5   2022-04-08   CO  0.01409   4
6   2022-04-08   RD  0.01485   5
7   2022-09-21   CO  0.01879  14
8   2022-09-21   RD  0.02067  15
9   2021-10-15   RD  0.02272   1
10  2022-08-10   CO  0.02288  12
11  2021-10-15   CO  0.02304   0
12  2022-11-02   RD  0.02494  16
[... 60 more lines not kept]
```

**Agent calls Bash**

```bash
cd executed/du-2026; for n in 0.22451 0.3736 '0.3077' 0.02009 0.00873 -0.01418 0.10498 0.01733 0.00663 0.00241 0.02158 0.00755 -0.00498 0.06901 0.0690 0.04619 0.00310 4.92 -0.00714 0.00075 '0.00227' 0.0193; do printf "%s: " "$n"; grep -l -- "$n" *.ipynb | tr '\n' ' '; echo; done; git -C  status --short | head -20
```

```
0.22451: 01_synthetic.ipynb 
0.3736: 01_synthetic.ipynb 
0.3077: 02_link_development.ipynb 
0.02009: 02_link_development.ipynb 03_link_estimators.ipynb 
0.00873: 02_link_development.ipynb 03_link_estimators.ipynb 
-0.01418: 02_link_development.ipynb 
0.10498: 02_link_development.ipynb 
0.01733: 03_link_estimators.ipynb 
0.00663: 03_link_estimators.ipynb 
0.00241: 01_synthetic.ipynb 04_link_temporal_capacity.ipynb 
0.02158: 05_link_confirmation.ipynb 
0.00755: 05_link_confirmation.ipynb 
-0.00498: 05_link_confirmation.ipynb 
0.06901: 06_mc_rtt.ipynb 
0.0690: 06_mc_rtt.ipynb 
0.04619: 06_mc_rtt.ipynb 
0.00310: 02_link_development.ipynb 
4.92: 02_link_development.ipynb 
-0.00714: 02_link_development.ipynb 
0.00075: 03_link_estimators.ipynb 05_link_confirmation.ipynb 07_mc_maze.ipynb 
[... 21 more lines not kept]
```

**Agent calls Bash**

```bash
date -u; cd entries/du-2026; PY=../../executed/du-2026/.venv/bin/python; $PY - <<'EOF'
import nbformat
p='02_link_development.ipynb'; nb=nbformat.read(p,4)
c=nb.cells[54]; assert c.source.startswith('**Result:')
old="which coincide because no trial is dropped."
assert old in c.source
c.source=c.source.replace(old, old+" Under reading (c), its position among the 113 held-out trials in trial order is 41 counting from 0 (the 42nd), not 123.")
nbformat.write(nb,p)
p='05_link_confirmation.ipynb'; nb=nbformat.read(p,4)
c=nb.cells[13]; assert c.source.startswith('**Result:')
c.source=c.source.replace("outside the 10% tolerance in each.","outside the 10% tolerance in each; the correct-pair gain exceeds the replacement gain in 20, 19, 20 and 20 of 20 sessions and in both task means under each.")
s=nb.cells[17]
old="""the qualitative pattern (positive geometry gain, smaller history gain, replacement below correct
pairing in every session) does in the printed seed runs."""
assert old in s.source
s.source=s.source.replace(old,"""the qualitative pattern does in the printed seed runs: positive geometry gain, a smaller history gain,
and replacement below correct pairing in both task means and in 19 or 20 of the 20 sessions.""")
nbformat.write(nb,p)
p='06_mc_rtt.ipynb'; nb=nbformat.read(p,4)
c=nb.cells[8]; assert c.source.startswith('**Result:')
c.source=c.source.replace("all eight equal the paper's values at its precision.","all eight equal the paper's values at its precision. The conditional whole-trial interval, 0.05371 to 0.08478, also equals the paper's.")
assert 'conditional whole-trial' in c.source
nbformat.write(nb,p)
EOF
```

```
Sat Nov 21 20:14:53 UTC 2026
```

**Agent calls Bash**

```bash
cd  python3 -c "
import json; s=json.load(open('schemas/attempt.schema.json'))
p=s['properties']
print(json.dumps(p['verifications'],indent=0)[:3000]); print(json.dumps(p['inputs'],indent=0)[:800])
"; curl -s https://api.dandiarchive.org/api/dandisets/000139/versions/0.220113.0408/info/ | python3 -c "import json,sys; d=json.load(sys.stdin); print(d['metadata'].get('doi'), d['metadata'].get('name'))"
```

Result: the fetched text is not kept.

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "attempts/du-2026-01.yaml",
 "old_string": "  source: https://github.com/gwkuqgfkqe/neural-decoder-context-audit at commit b042fbe1cda2ca5a353751c693d7c95f45de0456\noutcomes:",
 "new_string": "  source: https://github.com/gwkuqgfkqe/neural-decoder-context-audit at commit b042fbe1cda2ca5a353751c693d7c95f45de0456\n- what: The release's estimator modules (types, estimators, specification_estimators, robustness_estimators,\n    nested_estimators), fetched unchanged and run next to the ports on the same arrays (07_mc_maze.ipynb).\n  source: https://github.com/gwkuqgfkqe/neural-decoder-context-audit at commit b042fbe1cda2ca5a353751c693d7c95f45de0456\n- what: MC_Maze-medium, sub-Jenkins/sub-Jenkins_ses-medium_desc-train_behavior+ecephys.nwb, streamed; the data\n    of the data-elsewhere claims maze-gain and rff-maze and of the MC_Maze part of estimator-family-nlb.\n  source: 10.48324/dandi.000139/0.220113.0408\noutcomes:"
}
```

```
The file attempts/du-2026-01.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "attempts/du-2026-01.yaml",
 "old_string": "    table row (reading a) and as the usable-trial index (reading b); it is position 39 of the 113\n    held-out trials (reading c). The other",
 "new_string": "    table row (reading a) and as the usable-trial index (reading b); under reading (c) it is at\n    position 41 (from 0) of the 113 held-out trials in trial order. The other"
}
```

```
The file attempts/du-2026-01.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "attempts/du-2026-01.yaml",
 "old_string": "    other seeds the replacement mean is -0.01963, -0.00902, -0.00938 and -0.01515, each outside the\n    tolerance.",
 "new_string": "    other seeds the replacement mean is -0.01963, -0.00902, -0.00938 and -0.01515, each outside the\n    tolerance; the correct-pair gain exceeds replacement in 20, 19, 20 and 20 of 20 sessions and in\n    both task means under each."
}
```

```
The file attempts/du-2026-01.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "attempts/du-2026-01.yaml",
 "old_string": "  notes: All eight values equal the paper's at its precision. Under",
 "new_string": "  notes: All eight values equal the paper's at its precision, and so does the conditional whole-trial\n    interval, 0.05371 to 0.08478 (500 resamples, the release script's default). Under"
}
```

```
The file attempts/du-2026-01.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent**

Now the MC_Maze outcomes and estimator-family-nlb.

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "attempts/du-2026-01.yaml",
 "old_string": "  notes: MC_RTT gain 0.0690 under block penalties and 0.04619 under nonlinear context (g chosen 0.25),\n    both positive, which is what the criterion tests. The MC_Maze part of the statement (near zero) was\n    not tested, as DANDI:000139 was not read.\n  deviations:\n  - MC_Maze part not tested; block Ridge solved exactly in place of lsqr (as in estimator-family-link);\n    nonlinear context under the release's setting only.\n- claim: maze-gain\n  outcome: blocked\n  blocked_by: other\n  notes: The claim's data are MC_Maze-medium, DANDI:000139 version 0.220113.0408 (data elsewhere,\n    public). This attempt did not read it; the paper's loader (mc_maze.py) is in the release, and the\n    port and runs did not fit in this run after the 32 other claims. A later attempt can test it.\n- claim: rff-maze\n  outcome: blocked\n  blocked_by: other\n  notes: As maze-gain, DANDI:000139 was not read in this attempt.",
 "new_string": "  notes: MC_RTT gain 0.0690 under block penalties and 0.04619 under nonlinear context (g chosen 0.25),\n    both positive, which is what the criterion tests. The MC_Maze part, which the criterion reports\n    without making the outcome depend on it, holds on DANDI:000139 (07_mc_maze.ipynb) with block-penalty\n    gain 0.000455 and nonlinear-context gain -0.000243, both of absolute size below 0.01.\n  deviations:\n  - Block Ridge solved exactly in place of lsqr (as in estimator-family-link); nonlinear context under the\n    release's setting only.\n- claim: maze-gain\n  outcome: reproduced\n  notebook: 07_mc_maze.ipynb\n  output: claim:maze-gain\n  measured:\n  - 0.90533\n  - 0.000513\n  - 0.542\n  - -0.0000371\n  seed_sensitive: true\n  notes: On DANDI:000139 version 0.220113.0408 (data elsewhere; 250 trials, 27 conditions, 152 units,\n    188/62 release split, 258 context features), estimator seed 20260726 gives context-only R2 0.90533,\n    fully nested gain 0.000513, MSE reduction 0.542% (RMSE 81.76 to 81.53) and replacement gain\n    -0.0000371, all four within tolerance; the conditional interval is 0.00026 to 0.00076, as in the paper.\n    The release's own estimator code gives the same values on the same arrays. Under estimator seeds plus\n    1000 to 4000 the gain is -0.000138, 0.000479, 0.000528 and 0.000509 and the replacement gain\n    -0.0027212, 0.0000294, -0.0000190 and 0.0000075; the replacement gain is outside its tolerance under\n    each of these seeds and the gain under the first.\n  deviations:\n  - Tested in the revision after verification round 1; the first version of the attempt had blocked it\n    without reading the file. The loader is a port of the release's mc_maze.py (template context,\n    neural_lead_ms 80, as run_primary_analyses.py _run_nlb calls it).\n  - The conditional interval uses 500 bootstrap resamples, the default of run_primary_analyses.py; the\n    paper gives no count.\n- claim: rff-maze\n  outcome: reproduced\n  notebook: 07_mc_maze.ipynb\n  output: claim:rff-maze\n  measured:\n  - 0.0000448\n  - 0.0001386\n  seed_sensitive: true\n  notes: Map seeds 20260802, 20260803 and 20260804 give MC_Maze gains 0.0000448, 0.0000772 and\n    0.0001386 (the release's code gives the same), so the lowest and highest are within tolerance. Under\n    estimator seeds plus 1000 to 4000 the lowest of the three is 0.0000263, 0.0000360, 0.0000624 and\n    0.0000384, outside its tolerance under each, and the highest 0.0001194 to 0.0001387; every map gain\n    stays positive.\n  deviations:\n  - Tested in the revision after verification round 1, as maze-gain."
}
```

```
The file attempts/du-2026-01.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "attempts/du-2026-01.yaml",
 "old_string": "    legend). In MC_RTT the series carry unit m/s or meters with conversion 0.001, so the stored values\n    are mm/s and mm, as the descriptions say; the fields agree once the conversion is applied.",
 "new_string": "    legend). In MC_RTT and in MC_Maze (hand_vel, cursor_pos) the series carry unit m/s or meters with\n    conversion 0.001, so the stored values are mm/s and mm, as the descriptions say; the fields agree\n    once the conversion is applied."
}
```

```
The file attempts/du-2026-01.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "attempts/du-2026-01.yaml",
 "old_string": "    precision for every claim tested. The confirmation-set values are those of one outer split (seed\n    20260726); under four other split seeds the combined geometry-by-phase mean is 0.0148 to 0.0207 and\n    the history mean 0.0034 to 0.0082, so the exact values reported rest on that split, while the\n    qualitative pattern holds in each.",
 "new_string": "    precision for every claim tested; run next to the ports on MC_Maze and on one LINK session, the\n    release's estimator functions give identical values. The confirmation-set values are those of one\n    outer split (seed 20260726); under four other split seeds the combined geometry-by-phase mean is\n    0.0148 to 0.0207 and the history mean 0.0034 to 0.0082, so the exact values reported rest on that\n    split, while the qualitative pattern holds in each. The MC_Maze gain (0.00051) and replacement gain\n    (-0.00004) likewise rest on the estimator seed: under four others the gain is -0.00014 to 0.00053\n    and the replacement gain -0.0027 to 0.00003."
}
```

```
The file attempts/du-2026-01.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd  cat >> attempts/du-2026-01.yaml <<'EOF'
verifications:
- date: '2026-11-21'
  kind: agent
  by: Independent agent run by CatalystNeuro (same harness, separate context, did not write the notebook)
  reviewed: The first executed notebooks (01 to 06) with the conclusion cells and the summaries removed, the
    helper module and the claims file, with the paper's full text under paper/. The verifier read the DANDI
    API for 000129, 001201 and 000139 and tested the helpers on synthetic inputs (interior ranks, octants,
    window and drop rule, neural, position and behaviour alignment, tie rule, permutations, gain, Spearman,
    date bootstrap, build_link_dataset feature counts). It found no leakage.
  results:
  - claim: synthetic-template-null
    agrees: true
    outcome: reproduced
    reason: 01 cell 4 gives median -0.0000023 and median absolute gain 0.0000092, below 0.03. The range
      -0.0000588 to 0.0000248 matches the paper exactly.
    response: No change.
  - claim: synthetic-signal-ordering
    agrees: true
    outcome: reproduced
    reason: 01 cell 6 gives weak 0.22451 and strong 0.37360, strictly increasing from template-only.
    response: No change.
  - claim: synthetic-pair-breaking
    agrees: true
    outcome: reproduced
    reason: 01 cell 8 gives 10/10 seeds above both controls, replacement mean -0.3486 and permutation mean
      -0.3663.
    response: No change.
  - claim: link-development-sample
    agrees: true
    outcome: reproduced
    reason: 02 cell 10 gives 9 dates and 6,750 usable trials; all 18 sessions have 375.
    response: The notebook's statement that the two later versions of 001201 list the same assets had no
      supporting output (report, part C); a new cell in 02 lists both later versions and shows the same
      312 paths with the same sizes. Outcome unchanged.
  - claim: link-neural-only-r2
    agrees: true
    outcome: reproduced
    reason: 02 cell 12 gives CO 0.3077 and RD 0.3129.
    response: No change.
  - claim: link-context-ladder-gain
    agrees: true
    outcome: reproduced
    reason: 02 cell 14 shows the gain falling at every step for both tasks, and 10/10 values within
      tolerance (all equal the paper to 4 decimals).
    response: No change.
  - claim: link-context-only-r2
    agrees: true
    outcome: reproduced
    reason: 02 cell 16 gives plus history 0.6617/0.6839 and phase only 0.0084/0.0055, both below 0.02.
    response: No change.
  - claim: link-phase-only-replacement
    agrees: true
    outcome: reproduced
    reason: 02 cell 18 gives an RD mean of 0.10498, positive.
    response: No change.
  - claim: link-task-contrast-by-context
    agrees: true
    outcome: reproduced
    reason: 02 cell 20 gives signs +, -, -, + as stated. Geometry by phase (0.0015) is near zero under both
      readings; its interval contains 0, and it is smaller in absolute value than the direction (0.0155)
      and additive (0.0110) contrasts.
    response: No change.
  - claim: nested-geometry-gain
    agrees: true
    outcome: reproduced
    reason: 02 cell 22 gives SBP 0.02009 (18/18 positive) and TCR 0.01155 (17/18); date intervals 0.01586
      to 0.02401 and 0.00711 to 0.01591, close to Table 1.
    response: No change.
  - claim: nested-history-gain
    agrees: true
    outcome: reproduced
    reason: 02 cell 24 gives 0.00873 (17/18) and 0.00420 (16/18), each below its geometry mean.
    response: No change.
  - claim: nested-replacement-negative
    agrees: true
    outcome: reproduced
    reason: 02 cell 26 gives all four negative, 4/4 within tolerance.
    response: No change.
  - claim: replacement-source-diagnostics
    agrees: true
    outcome: reproduced
    reason: 02 cell 28 gives minimum eligible sources 5, median maximum reuse 3, maximum 4 and
      self-replacement error 0.
    response: No change.
  - claim: permutation-negative
    agrees: true
    outcome: reproduced
    reason: 02 cell 30, reading (a), gives 18/18 negative, mean -0.01418. Reading (b) also passes (36/36,
      -0.01387).
    response: No change.
  - claim: replacement-penalty-distance
    agrees: true
    outcome: reproduced
    reason: 02 cell 32 gives 8 positive and 10 negative correlations, and the date interval -0.0204 to
      0.0301 contains 0. Both readings hold.
    response: No change.
  - claim: replacement-ranks-lower
    agrees: true
    outcome: reproduced
    reason: 02 cell 34 shows ranks 1 to 5 and all five random draws below the correct-pair mean, for SBP
      and TCR.
    response: No change.
  - claim: practical-mse-reduction
    agrees: true
    outcome: reproduced
    reason: 02 cell 36 gives 6/6 within tolerance (4.92%, 0.01407, 0.01372, 2.72%, 2.83%, 1.31%).
    response: No change.
  - claim: representative-trial
    agrees: true
    outcome: reproduced
    reason: 02 cell 38 gives 2022-09-21 RD as the ninth session in gain order, and its median trial is 123
      under readings (a) and (b); the other session reading gives 2021-10-15 RD. The "position among 113
      held-out trials" (39 and 75) is an index into test_indices in train_test_split's shuffled order, so
      it is not a meaningful position for reading (c) (problem 1). Sorting by (gain, date, task) and taking
      index (n-1)//2 matches the claims file's first reading (problem 6).
    response: Reading (c) is now computed as the position among the held-out trials in ascending trial
      order, 41 from 0 (77 for the other session reading); notes and notebook text corrected. Outcome
      unchanged, as readings (a) and (b) give 123.
  - claim: confirm-geometry-gain
    agrees: true
    outcome: reproduced
    reason: 05 cell 6 gives 20/20 positive and 0.02158 (CO 0.02104, RD 0.02213). The re-run selection rule
      gives the same 20 assets as the frozen manifest, and the paper's gate passes. The confirmation
      results depend strongly on the split seed; under seeds +1000 to +4000 the combined geometry mean is
      0.0148 to 0.0207 and several values fall outside the 10% tolerances, but the criterion fixes seed
      20260726 (problem 4).
    response: No change; the outcome was already marked seed_sensitive with the values under each seed.
  - claim: confirm-history-contraction
    agrees: true
    outcome: reproduced
    reason: 05 cell 8 gives 0.00755 (CO 0.00670, RD 0.00840), 19/20 positive, below the geometry mean.
    response: No change (seed_sensitive, as for confirm-geometry-gain).
  - claim: confirm-replacement
    agrees: true
    outcome: reproduced
    reason: 05 cell 10 gives -0.00771, with correct-pair gain above replacement in 20/20 sessions and in
      both task means. Under seeds +1000 to +4000 the notebook prints only how many replacement gains are
      positive, not how many sessions have correct-pair gain above replacement.
    response: The cell now prints, for each of the five seeds, the sessions with gain above replacement
      (20, 20, 19, 20 and 20 of 20) and whether both task means are above (yes under each). The summary
      sentence that said every session was corrected to 19 or 20 of 20. Outcome unchanged.
  - claim: confirm-table1-values
    agrees: true
    outcome: reproduced
    reason: 05 cell 12 gives -0.00498, 4.761% and 2.047%.
    response: No change.
  - claim: rtt-data
    agrees: true
    outcome: reproduced
    reason: 06 cell 4 gives 1080 blocks, 130 units, an 810/270 split and 21 bins per block.
    response: No change.
  - claim: rtt-gain
    agrees: true
    outcome: reproduced
    reason: 06 cell 6 gives gain 0.06846 (positive) and replacement -0.02297 (negative); all 7 other values
      within tolerance.
    response: The conditional whole-trial interval of the release is now computed as well (0.05371 to
      0.08478, as in the paper). Outcome unchanged.
  - claim: rff-rtt
    agrees: true
    outcome: reproduced
    reason: 06 cell 8 gives 0.01685, 0.01501 and 0.01491, all positive and inside the widened range.
    response: No change.
  - claim: rff-link
    agrees: true
    outcome: reproduced
    reason: 02 cell 42 shows CO and RD positive under every map. Reading (a) 0.00310 to 0.00404 is inside
      the range, and history 0.00111 to 0.00142 is inside. Reading (b) fails (0.00269 is outside), but one
      reading suffices.
    response: No change.
  - claim: estimator-family-link
    agrees: true
    outcome: reproduced
    reason: 03 cell 4 shows that under the code's setting (nonlinear-context reading (a)) every CO, RD and
      18-session mean is positive for both families. Reading (b), all 27 nonlinear-context settings, was
      not run; the criterion needs only one reading. _BlockRidge solves with cholesky where the release
      uses lsqr; this is stated, one session differs by 5e-7, and a different solver cannot plausibly flip
      the positive means (problem 3).
    response: No change. Reading (b) of the nonlinear context was not run in the revision either (estimated
      about 9 h).
  - claim: estimator-family-nlb
    agrees: true
    outcome: reproduced
    reason: 06 cell 10 gives block 0.06901 and nonlinear context 0.04619, both positive. The criterion makes
      the outcome depend only on MC_RTT; the MC_Maze half of the statement is untested.
    response: The MC_Maze part is now run on DANDI:000139 (07_mc_maze.ipynb) and holds (block-penalty gain
      0.000455, nonlinear-context gain -0.000243, both of absolute size below 0.01). Outcome unchanged.
  - claim: temporal-offset
    agrees: true
    outcome: reproduced
    reason: 04 cell 5 shows the gain at 120 ms below the gain at 0 ms for CO and RD under both estimators.
      Under the fully nested reading only RD-change reading (b) holds (RD-CO goes from +0.00241 to -0.00024
      and -0.00061); under the evaluate_decoders_nested reading both (a) and (b) hold.
    response: No change.
  - claim: split-seed-stability
    agrees: true
    outcome: reproduced
    reason: 02 cell 40 gives 6/6 positive and within tolerance.
    response: No change.
  - claim: context-capacity-contrast
    agrees: true
    outcome: reproduced
    reason: 04 cell 7 shows the quadratic-plus-history contrast positive for SBP and TCR under both
      estimators. Only TCR shows a changed contrast; SBP does not change. The context feature counts
      141/351/151/361 in 04 cell 3 are a hard-coded string, not computed (problem 2); the verifier's own
      check of build_link_dataset gives 9/81/87/141/151/351/361.
    response: 04 cell 3 now prints the context feature counts from the datasets the fits used (141, 351,
      151 and 361 in every session). Outcome unchanged.
  - claim: maze-gain
    agrees: true
    outcome: blocked
    reason: Blocked (data_missing). DANDI:000139 is not one of this attempt's datasets. The API shows 000129
      holds only sub-Indy files (2 assets) and 001201 only sub-Monkey-N (312); the MC_Maze file exists only
      in 000139 0.220113.0408. No part can be tested.
    response: Outcome changed to reproduced. The claim is data elsewhere, and the protocol (author step 1.4)
      says to test such a claim on the archive that holds its data and never to block it as data_missing.
      The file is public, so the revision ports the release's mc_maze.py and tests it in a new notebook,
      07_mc_maze.ipynb. Under estimator seed 20260726 all four values are within tolerance and the
      interval equals the paper's. Under other estimator seeds the replacement gain falls outside its
      tolerance, so the outcome is marked seed_sensitive.
  - claim: rff-maze
    agrees: true
    outcome: blocked
    reason: Blocked (data_missing), same as maze-gain.
    response: Outcome changed to reproduced, on DANDI:000139 as for maze-gain. The three map gains are
      0.0000448, 0.0000772 and 0.0001386, and the lowest and highest are within tolerance. Under other
      estimator seeds the lowest falls outside, so the outcome is marked seed_sensitive.
EOF
date -u
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  timeout 600 python tools/entry.py check entries/du-2026 2>&1 | tail -15; ls tools | head -40
```

```
error: attempts/du-2026-01.yaml: not valid YAML: mapping values are not allowed in this context
  in "<unicode string>", line 522, column 51
1 error(s)
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
[... 23 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 518,524p attempts/du-2026-01.yaml; grep -n ": " attempts/du-2026-01.yaml | awk -F: 'NR>0' | grep -vE "^[0-9]+:\s*(-\s)?[a-z_]+: " | head
```

```
release's estimator functions give identical values. The confirmation-set values are those of one
    outer split (seed 20260726); under four other split seeds the combined geometry-by-phase mean is
    0.0148 to 0.0207 and the history mean 0.0034 to 0.0082, so the exact values reported rest on that
    split, while the qualitative pattern holds in each. The MC_Maze gain (0.00051) and replacement gain
    (-0.00004) likewise rest on the estimator seed: under four others the gain is -0.00014 to 0.00053
    and the replacement gain -0.0027 to 0.00003.
verifications:
522:    (-0.00004) likewise rest on the estimator seed: under four others the gain is -0.00014 to 0.00053
```

**Agent calls Bash**

```bash
cd  sed -i '522s/rest on the estimator seed: under four others/rest on the estimator seed, and under four others/' attempts/du-2026-01.yaml; python3 -c "
import yaml
d=yaml.safe_load(open('attempts/du-2026-01.yaml'))
def walk(x,path=''):
    if isinstance(x,dict):
        for k,v in x.items(): walk(v,path+'/'+str(k))
    elif isinstance(x,list):
        for i,v in enumerate(x): walk(v,path+f'[{i}]')
    elif isinstance(x,str) and ': ' in x: print(path, x[:80])
walk(d)
"; grep -n "—\|rather" attempts/du-2026-01.yaml entries/du-2026/README.md entries/du-2026/*.ipynb | head; timeout 600 python tools/entry.py check entries/du-2026 2>&1 | tail -5
```

```
0 error(s)
```

**Agent**

Record validates. Starting the final full re-run so the executed copies match the edited notebooks.

**Agent calls Bash**

```bash
cd  date -u; timeout 7000 python tools/entry.py all entries/du-2026 2>&1 | tail -10; date -u
```

```
Sat Nov 21 20:16:34 UTC 2026
Installed kernelspec registry-du-2026 in executed/du-2026/.venv/share/jupyter/kernels/registry-du-2026
0 error(s)
pass  01_synthetic.ipynb  (106 s)
pass  02_link_development.ipynb  (817 s)
pass  03_link_estimators.ipynb  (497 s)
pass  04_link_temporal_capacity.ipynb  (639 s)
pass  05_link_confirmation.ipynb  (349 s)
pass  06_mc_rtt.ipynb  (53 s)
pass  07_mc_maze.ipynb  (104 s)
Sat Nov 21 20:59:27 UTC 2026
```

**Agent calls Bash**

```bash
cd executed/du-2026; python3 $TMPDIR/show.py 07_mc_maze.ipynb 4 7 10 13 | grep -v "^ *$" | head -50; python3 $TMPDIR/show.py 02_link_development.ipynb 2 53 | tail -4; python3 $TMPDIR/show.py 05_link_confirmation.ipynb 12 | tail -6; python3 $TMPDIR/show.py 06_mc_rtt.ipynb 7 | grep interval; python3 $TMPDIR/show.py 04_link_temporal_capacity.ipynb 3
```

```
=== cell 4 ['claim:maze-gain']
fits in 0.9 min
context-only R2: 0.9053327 (expected 0.9053 +- 0.09053; within: True)
fully nested gain: 0.0005131 (expected 0.00051 +- 0.00025; within: True)
% MSE reduction: 0.5420531 (expected 0.54 +- 0.054; within: True)
replacement gain: -0.0000371 (expected -4e-05 +- 4e-06; within: True)
context RMSE 81.76, context-plus-neural RMSE 81.53 (paper 81.76 to 81.53)
conditional interval 0.00026 to 0.00076 (paper 0.00026 to 0.00076)
context features: 258 (258 in the criterion)
seed 20260726: context R2 0.9053, gain 0.000513, MSE reduction 0.542%, replacement -0.0000371
seed 20261726: context R2 0.9053, gain -0.000138, MSE reduction -0.146%, replacement -0.0027212
seed 20262726: context R2 0.9053, gain 0.000479, MSE reduction 0.506%, replacement 0.0000294
seed 20263726: context R2 0.9053, gain 0.000528, MSE reduction 0.557%, replacement -0.0000190
seed 20264726: context R2 0.9053, gain 0.000509, MSE reduction 0.537%, replacement 0.0000075
penalties (context, residualizer, residual learner): 0.1 10000.0 100000.0
=== cell 7 ['claim:rff-maze']
{20260802: 4.48e-05, 20260803: 7.72e-05, 20260804: 0.0001386} penalties {20260802: 100000.0, 20260803: 100000.0, 20260804: 100000.0}
lowest 0.0000448 (expected 0.000045 +- 0.0000045; within: True); highest 0.0001386 (expected 0.000139 +- 0.0000139; within: True)
estimator seed 20261726: map gains 0.0000263 to 0.0001194
estimator seed 20262726: map gains 0.0000360 to 0.0001238
[... 35 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/du-2026; for f in *.ipynb; do python3 -c "
import json,sys; nb=json.load(open('$f')); print('$f', sum(len(c.get('outputs',[])) for c in nb['cells'] if c['cell_type']=='code'))"; done; cd ../..; python tools/entry.py check entries/du-2026 | tail -2; git status --short entries attempts
```

```
01_synthetic.ipynb 0
02_link_development.ipynb 0
03_link_estimators.ipynb 0
04_link_temporal_capacity.ipynb 0
05_link_confirmation.ipynb 0
06_mc_rtt.ipynb 0
07_mc_maze.ipynb 0
0 error(s)
 M attempts/du-2026-01.yaml
 M entries/du-2026/02_link_development.ipynb
 M entries/du-2026/04_link_temporal_capacity.ipynb
 M entries/du-2026/05_link_confirmation.ipynb
 M entries/du-2026/06_mc_rtt.ipynb
 M entries/du-2026/README.md
 M entries/du-2026/du2026.py
 M entries/du-2026/entry.yaml
?? entries/du-2026/07_mc_maze.ipynb
```

**Agent**

I've answered the round-1 report. Two outcomes changed: maze-gain and rff-maze went from blocked to reproduced, marked seed sensitive. All 31 other outcomes are unchanged, and the verifier agreed with them. The final run passed for all seven notebooks, `check` reports 0 errors, and every conclusion matches the new numbers. Nothing is committed.

**Outcome changes**
- The verifier agreed with blocking maze-gain and rff-maze, but gave the reason as data missing. The protocol (author step 1.4) says a claim whose data are elsewhere must be tested on the archive that holds them, never blocked as data missing. DANDI:000139 is public, so I ported the release's `mc_maze.py` into a new notebook, `07_mc_maze.ipynb`.
- **maze-gain:** with estimator seed 20260726, all four values are within tolerance: context R2 0.90533, gain 0.000513, MSE reduction 0.542%, replacement gain -0.0000371. The interval (0.00026 to 0.00076) and the RMSE (81.76 to 81.53) equal the paper's. With seeds +1000 to +4000, the replacement gain falls outside its tolerance under all four, and the gain under one of them (-0.000138).
- **rff-maze:** the three map gains are 0.0000448, 0.0000772 and 0.0001386, so the lowest and highest are within tolerance. With the other estimator seeds, the lowest falls outside its tolerance under each.

**Added or corrected, per the report**
- **Port against the release code:** `07_mc_maze.ipynb` fetches the release's estimator modules at commit b042fbe and runs them on the same arrays as the ports, on MC_Maze and on one LINK session (2021-10-15 CO). Every value is identical.
- **MC_Maze half of estimator-family-nlb:** now reported. Block-penalty gain is 0.000455 and nonlinear-context gain -0.000243, both below 0.01 in absolute size. The outcome still rests on MC_RTT, as the criterion says.
- **rtt-gain:** the release's conditional interval is now computed (500 resamples, the script's default) and equals the paper's, 0.05371 to 0.08478.
- **Problem 1 (representative-trial):** reading (c) is now the position in trial order among the held-out trials, 41 counting from 0. The old value was an index into the shuffled split order. Readings (a) and (b) still give 123.
- **Problem 2:** the context feature counts in notebook 04 are now computed from the data: 141, 351, 151 and 361.
- **confirm-replacement:** the notebook now prints, for each of the five seeds, how many sessions have gain above replacement: 20, 20, 19, 20 and 20. The summary had said "every session" under all seeds; I corrected that to "19 or 20 of 20".
- **Later 001201 versions:** a new cell shows both later versions list the same 312 paths with the same sizes as the pinned one.
- **Attempt record:** I added the round-1 `verifications` block, the two new inputs (DANDI:000139 and the release modules), and updated findings for MC_Maze units and seed dependence.

**Not changed, and why**
- **Problem 3 (solver):** kept, since it was already stated as a deviation.
- **Problem 4 (seed dependence):** already recorded with `seed_sensitive`.
- **Problems 5 and 6:** no change needed.
- **Nonlinear-context reading (b) of estimator-family-link:** still not run. I estimated about 9 hours, and the criterion needs only one reading.
- **Questions file:** the verifier reported no misreading of the paper by the claims file, so I added nothing to `questions/du-2026.yaml`.

**Registry listing:** DANDI:000139 holds data this paper analysed, but the registry does not list the paper on it. That is how the claims file has it, so I kept it as data elsewhere and did not add it to the record's `datasets` (it is under `inputs`). It is a dataset this paper reuses, not one the authors deposited, so whether to list it is the registry's call.

## End of run

73 turns, 96 minutes, $3.80 at API prices, result: success.
