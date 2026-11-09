# 000013 · author-answers · run 39619556396

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  sed -n '/## Author/,/^## [^A]/p' docs/protocol.md | head -300; ls entries/000013-hires-2015 entries/000013-hires-2015/*; cat questions/000013.yaml
```

```
## Author

The workflow puts the paper under `paper/`, as for the reader. Read it to
understand the claims, their data and their figures. The claims file still
decides what is tested and how: do not change a claim's statement, expected
values or criterion, and do not apply a method detail the claims file lacks,
even one the paper gives. Ask for it (step 6).

### 1. Establish what can be tested

Do this before any analysis.

1. List the dataset's files and read its metadata from the archive. Open a
   file and list everything it holds, including every column of every table.
2. Work out which of the subjects, sessions, conditions and measured
   variables that the claims file describes are in the dataset. A dataset
   that names a paper may hold only part of its data. Check for recordings
   deposited more than once (identical traces, frame counts or annotations),
   report each pair, and count each recording once. Where the analysis treats
   a unit as the same across sessions, show that it is, or state it as an
[... 390 more lines not kept]
```

**Agent calls Bash**

```bash
cd  ls attempts | grep 000013; wc -l attempts/000013* claims/000013/* entries/000013-hires-2015/*; git log --oneline -3 -- claims/000013 questions/000013.yaml; git diff b6ee3df4 HEAD --stat
```

```
000013-hires-2015-01.yaml
   471 attempts/000013-hires-2015-01.yaml
  1264 claims/000013/10.7554-elife.06619.yaml
    36 entries/000013-hires-2015/README.md
    22 entries/000013-hires-2015/entry.yaml
  1044 entries/000013-hires-2015/hires.py
  3243 entries/000013-hires-2015/reproduce_hires_2015.ipynb
     8 entries/000013-hires-2015/requirements.in
    68 entries/000013-hires-2015/requirements.lock.txt
  6156 total
4ddfc755 Agent run on 000013: answer (success)
b6ee3df4 Agent run on 000013: author (success)
2273b46b Agent run on 000013: claims-check (success)
 claims/000013/10.7554-elife.06619.yaml |  68 +++-
 questions/000013.yaml                  |  46 +++
 transcripts/000013/answer-report.md    |   9 +
 transcripts/000013/answer.md           | 656 +++++++++++++++++++++++++++++++++
 4 files changed, 760 insertions(+), 19 deletions(-)
```

**Agent calls Bash**

```bash
cd  git diff b6ee3df4 HEAD -- claims/
```

```
diff --git a/claims/000013/10.7554-elife.06619.yaml b/claims/000013/10.7554-elife.06619.yaml
index 24d860bc..9a96183e 100644
--- a/claims/000013/10.7554-elife.06619.yaml
+++ b/claims/000013/10.7554-elife.06619.yaml
@@ -52,8 +52,8 @@
 #   - Exploration time is whisking epochs including touch epochs, excluding touches >100 ms.
 #   - The touch spike window of a cell runs from its onset latency to its touch response cutoff
 #     t_on. Latency is where the 1 ms PCTH rises above the pre-touch mean (-50 to 0 ms) by two
-#     standard deviations. t_on is the first window size at which the increase of the cumulative
-#     count of spikes indexed to the closest touch onset falls below the 95th percentile of the
+#     standard deviations. t_on is the first window size, after the curve's rise, at which the
+#     increase of the cumulative count of spikes indexed to the closest touch onset falls below the 95th percentile of the
 #     slopes of 1000 spike-time shuffles, the curves smoothed by a degree-11 polynomial.
 #   - Phase tuning is a 12-bin histogram fitted by A[1 + cos(theta - phi_pref)] + B, A, B > 0;
 #     modulation depth A / (A + B).
@@ -737,7 +737,10 @@ claims:
     p: 0.019
     n: 11 cells
   criterion: As whisking-rate-l4-no-change, for the 11 L5 cells. Reproduced when p < 0.05 with the
-    median whisking rate higher, under both readings of whisking periods.
[... 123 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat attempts/000013-hires-2015-01.yaml
```

```
schema_version: 2
id: 000013-hires-2015-01
dataset:
  archive: dandi
  id: "000013"
  version: 0.220126.2143
  doi: 10.48324/dandi.000013/0.220126.2143
paper: doi:10.7554/elife.06619
date: 2026-10-21
entry: 000013-hires-2015
provenance:
  kind: agent
  accountable:
    name: CatalystNeuro
  agent:
    harness: Claude Code (GitHub Actions)
    model: claude-opus-5-5
    protocol: pilot-10
  runner:
    platform: GitHub Actions
[... 451 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/000013-hires-2015; cat entry.yaml README.md requirements.in; python -c "
import json
nb=json.load(open('reproduce_hires_2015.ipynb'))
for i,c in enumerate(nb['cells']):
    src=''.join(c['source'])
    print(i,c['cell_type'],c.get('metadata',{}).get('tags',[]),len(src.splitlines()),'|',src.splitlines()[0][:110] if src else '')
"
```

```
schema_version: 1
name: 000013-hires-2015
type: reproduction
title: Low-noise encoding of active touch by layer 4 (Hires et al. 2015)
description: Tests the findings of Hires, Gutnisky, Yu, O'Connor and Svoboda (2015) on dandiset
  000013, which holds the 52 loose-seal recordings of the paper (31 L4 cells in C2, 10 L4 cells
  outside C2, 11 L5 cells) with millisecond whisker tracking during pole localization. It covers
  the behaviour, the example cell, Table 1, the touch and phase coupled spikes of Figure 3, the
  population decoders of Figure 4, the modulation indices of Figure 5 and the Fano factors of
  Figure 6.
license: Apache-2.0
notebooks:
- path: reproduce_hires_2015.ipynb
  title: Reproducing Hires et al. (2015) from dandiset 000013
  runtime_minutes: 10
helpers:
- hires.py
related:
- id: dandi:000013/0.220126.2143
  relation: uses_data
[... 199 more lines not kept]
```

**Agent calls Bash**

```bash
cd  ls executed/ 2>/dev/null | head; ls executed/000013-hires-2015 2>/dev/null; git status --short | head
```

```
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

**Agent**

No executed copy is around, so I'll read the notebook source and the helper module before running anything.

**Agent calls Bash**

```bash
cd entries/000013-hires-2015; python -c "
import json
nb=json.load(open('reproduce_hires_2015.ipynb'))
for i,c in enumerate(nb['cells']):
    if i in list(range(0,3))+list(range(12,20))+list(range(56,64))+list(range(78,101)):
        print('#### CELL',i,c['cell_type'],c.get('metadata',{}).get('tags',[]))
        print(''.join(c['source']))
"
```

```
<persisted-output>
Output too large (32.3KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/0c4b01be-3c6b-45c5-bd46-6187c2251e9c/tool-results/bsbq9484c.txt

Preview (first 2KB):
#### CELL 0 markdown []
# Hires et al. (2015) from dandiset 000013

**Paper.** Hires, Gutnisky, Yu, O'Connor & Svoboda (2015), "Low-noise encoding of active touch by
layer 4 in the somatosensory cortex", eLife 4, e06619, [doi:10.7554/eLife.06619](https://doi.org/10.7554/eLife.06619).

**Dataset.** [DANDI:000013](https://dandiarchive.org/dandiset/000013/0.220126.2143), version
`0.220126.2143` ([doi:10.48324/dandi.000013/0.220126.2143](https://doi.org/10.48324/dandi.000013/0.220126.2143)).
The paper (2015) cites no version of the dandiset, which was created in 2020. This is its only
published version, and so the most recent one; the draft holds the same 52 files (the same
blobs, checked through the API when the attempt was prepared), so no other version could match
the claims file better.

**Claims.** `claims/000013/10.7554-elife.06619.yaml`, written by a reader from the version of
record (PMC4525079, as served by Europe PMC), its figure legends and figure supplements, and
checked by a second reader. The claims file decides what is tested and how; where it leaves a
[... 16 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/0c4b01be-3c6b-45c5-bd46-6187c2251e9c/tool-results/bsbq9484c.txt"
}
```

```
1	#### CELL 0 markdown []
2	# Hires et al. (2015) from dandiset 000013
3	
4	**Paper.** Hires, Gutnisky, Yu, O'Connor & Svoboda (2015), "Low-noise encoding of active touch by
5	layer 4 in the somatosensory cortex", eLife 4, e06619, [doi:10.7554/eLife.06619](https://doi.org/10.7554/eLife.06619).
6	
7	**Dataset.** [DANDI:000013](https://dandiarchive.org/dandiset/000013/0.220126.2143), version
8	`0.220126.2143` ([doi:10.48324/dandi.000013/0.220126.2143](https://doi.org/10.48324/dandi.000013/0.220126.2143)).
9	The paper (2015) cites no version of the dandiset, which was created in 2020. This is its only
10	published version, and so the most recent one; the draft holds the same 52 files (the same
11	blobs, checked through the API when the attempt was prepared), so no other version could match
12	the claims file better.
13	
14	**Claims.** `claims/000013/10.7554-elife.06619.yaml`, written by a reader from the version of
15	record (PMC4525079, as served by Europe PMC), its figure legends and figure supplements, and
16	checked by a second reader. The claims file decides what is tested and how; where it leaves a
17	method detail open, every reading it lists is run, and where it lists none for a detail that
18	can change a result, the question is asked in `questions/000013.yaml` and the readings this
19	notebook can see are all shown.
20	
[... 511 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/000013-hires-2015; python -c "
import json
nb=json.load(open('reproduce_hires_2015.ipynb'))
for i,c in enumerate(nb['cells']):
    if i in list(range(101,122))+list(range(133,137))+[151]:
        print('#### CELL',i,c['cell_type'],c.get('metadata',{}).get('tags',[]))
        print(''.join(c['source']))
" > $TMPDIR/cells2.txt; wc -l $TMPDIR/cells2.txt
```

```
470 /tmp/claude-1001/cells2.txt
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/cells2.txt"
}
```

```
1	#### CELL 101 markdown []
2	## Figure 4A: fig4a-touch-detection-c2 and fig4a-touch-detection-outside
3	
4	> Pooling the activity of only 15 L4 C2 neurons, integrated over 10 ms, is enough to detect
5	> 95% of touches.
6	
7	> Touch detection by neurons from surrounding barrels, outside C2, is poor.
8	
9	Touch-aligned responses from -30 to +50 ms, leaving out touches with another onset within 50
10	ms; N neurons drawn with replacement, 1000 responses each with replacement, 10 ms causal
11	integration, pooled; one threshold per post-touch time point, chosen on half the samples to
12	maximise percent correct, tested on the other half. Open details from the claims file: (1)
13	the non-touch epochs, (a) the 30 ms before touch in the same responses, or (b) 10 ms windows of
14	exploration time away from touch; (2) the measure at the best post-touch time point, (a)
15	fraction of touches detected or (b) percent correct. Within (1a) the claims file does not say
16	which 10 ms of the 30 ms before touch; both ends are run, the window ending at onset
17	(`pre_end`, -10 to 0 ms) and the earliest (`pre_start`, -30 to -20 ms). Reading (1b) uses
18	windows with no touch onset from 60 ms before to 100 ms after them (a standard choice).
19	20 repetitions per population size give the mean and the 95% bounds.
20	#### CELL 102 code []
[... 451 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/000013-hires-2015; grep -n "^def \|^[A-Z_]* = " hires.py
```

```
51:DANDISET_ID = "000013"
52:DANDISET_VERSION = "0.220126.2143"
53:API = "https://api.dandiarchive.org/api"
55:TRIAL_STRIDE_MS = 100_000      # spacing of trials on the virtual axis; trials last 4.5 s
56:CLOCKS = ("spike", "voltage")   # SpikeTrain timestamps, or those of the voltage
58:WHISK_AMP = 2.5          # deg, whisking (Methods)
59:NONWHISK_AMP = 1.25      # deg, non-whisking (Methods)
60:NONWHISK_MIN_MS = 100    # ms, non-whisking periods (Methods)
61:LONG_TOUCH_MS = 100      # ms, prolonged touches left out of exploration (Methods)
62:AFTER_TOUCH_MS = 70      # ms, whisk cycles excluded after touch (Methods)
63:PRE_MS = 50              # ms, pre-touch baseline for latency (Methods)
64:LAT_SEARCH_MS = 50       # ms, latency searched 0 to 50 ms (claim latency-determinable)
65:N_SURROGATES = 1000      # Methods
66:POLY_DEGREE = 11         # Methods
67:TMAX_READINGS = (100, 200)  # ms, longest touch window searched: open, two readings
68:N_PHASE_BINS = 12        # Figure 3, figure supplement 1C
69:N_SPOT_CHECK = 40        # spikes per file whose stored timestamp is read back
71:GROUPS = {"L4C2": "L4 inside C2", "L4out": "L4 outside C2", "L5": "L5 near C2"}
76:def list_assets() -> pd.DataFrame:
86:def _text(x):
[... 52 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "entries/000013-hires-2015/hires.py",
 "offset": 1,
 "limit": 50
}
```

```
1	"""Loading and measures for dandiset 000013, Hires, Gutnisky, Yu, O'Connor & Svoboda (2015), eLife
2	4, e06619, "Low-noise encoding of active touch by layer 4 in the somatosensory cortex".
3	
4	Each NWB file holds one loose-seal recording (one cell, one session): a 10 kHz spike train
5	(`SpikeTrain`, 0 or 1 per sample) with the voltage it was detected from, 1 kHz whisker tracking
6	(azimuthal angle `theta_at_base`, the 6 to 60 Hz Hilbert `amplitude` and `phase`, curvature change
7	`delta_kappa`, touch onset and offset, lick onsets `beam_break_times`, `pole_available`), and a
8	trials table. Trials are 4.5 s windows, stored one after another with gaps between them. Files are
9	streamed from the archive at the pinned version; nothing is written to disk.
10	
11	Times. Every per-trial quantity is kept in "virtual milliseconds": trial k, sample j of its
12	behaviour segment is at ``k * TRIAL_STRIDE_MS + j``, so that a search for the nearest event never
13	crosses into another trial. Spikes are placed on the same axis from their own timestamps. In 36
14	files the `SpikeTrain` timestamps are 10 ms earlier than those of the voltage the spikes were
15	detected from (the samples themselves line up); ``CLOCKS`` names the two readings, and the notebook shows which
16	one agrees with the touch response.
17	
18	Where the parameters come from (the claims file, claims/000013/10.7554-elife.06619.yaml, cites the
19	paper for each):
20	
[... 30 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "entries/000013-hires-2015/hires.py",
 "offset": 330,
 "limit": 300
}
```

```
330	def cycles(cell: Cell) -> np.ndarray:
331	    """Whisk cycles: from one wrap of the phase (pi to -pi) to the next, inside one trial.
332	    Returns start, stop (exclusive) sample indices."""
333	    ph = cell.phase.astype(float)
334	    wrap = np.flatnonzero(np.diff(ph) < -np.pi) + 1
335	    st, en = wrap[:-1], wrap[1:]
336	    same = cell.trial_of[st] == cell.trial_of[en - 1]
337	    return np.c_[st[same], en[same]]
338	
339	
340	def cycle_table(cell: Cell, T: Touches) -> pd.DataFrame:
341	    """Each cycle with the properties the exclusions use."""
342	    cyc = cycles(cell)
343	    ph = cell.phase.astype(float)
344	    touch = touch_mask(cell, T)
345	    # samples within 70 ms after the end of a touch (or in it)
346	    after = touch.copy()
347	    for b in T.off:
348	        k = cell.trial_of[min(b, len(after) - 1)]
349	        e = min(b + AFTER_TOUCH_MS, len(after))
[... 280 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "entries/000013-hires-2015/hires.py",
 "offset": 740,
 "limit": 280
}
```

```
740	
741	# ----------------------------------------------------------------------------- touch responses
742	
743	def touch_responses(cell: Cell, svt: np.ndarray, T: Touches, pre: int = 30, post: int = 50,
744	                    exclude_next: int = 50) -> np.ndarray:
745	    """Spike counts in 1 ms bins from -pre to +post ms around each touch onset, leaving out
746	    touches followed by another onset within exclude_next ms, and touches whose window leaves
747	    the trial (Methods, Population decoding). Shape (n_touches, pre + post)."""
748	    s = np.sort(svt)
749	    on_vt = cell.vt[T.on].astype(float)
750	    nxt = np.r_[on_vt[1:] - on_vt[:-1], np.inf]
751	    same_next = np.r_[T.trial[1:] == T.trial[:-1], False]
752	    k = (on_vt // TRIAL_STRIDE_MS).astype(int)
753	    pos = on_vt - k * TRIAL_STRIDE_MS
754	    nseg = np.diff(np.r_[cell.seg_start, len(cell.vt)])
755	    keep = ~(same_next & (nxt <= exclude_next)) & (pos - pre >= 0) & (pos + post <= nseg[k])
756	    edges = np.arange(-pre, post + 1)
757	    out = []
758	    for o in on_vt[keep]:
759	        a, b = np.searchsorted(s, [o - pre, o + post])
[... 260 more lines not kept]
```

**Agent**

Questions and answers are clear. Next I'll read the current criteria of every claim that uses the touch window or one of the answered details.

**Agent calls Bash**

```bash
cd  python - <<'EOF'
import yaml
d=yaml.safe_load(open('claims/000013/10.7554-elife.06619.yaml'))
want=['example-cell-touch-window','text-spikes-per-touch','table1-l4-c2','table1-l4-outside','table1-l5','l4-outside-weaker-touch','fig3c-touch-spikes-outside','fig3c-touch-spikes-l5','fig3d-touch-phase-outside','fig3d-touch-phase-l5','fig3d-phase-only','fig4a-touch-detection-c2','fig4a-touch-detection-outside','fig5c-modulation-index','fig5-modulation-correlations','fig6d-not-refractory','fig4c-phase-decoding','fig4b-touch-time-precision']
for c in d['claims']:
    if c['id'] in want:
        print('=====',c['id'],'depends',c.get('depends_on'))
        print('EXP',c.get('expected'))
        print(c['criterion'])
EOF
```

```
===== example-cell-touch-window depends ['example-cell-rates']
EXP [{'quantity': 'fraction of exploration-time spikes in the touch window', 'value': 74.4, 'tolerance': 7.44, 'unit': '%'}, {'quantity': 'touch window start (onset latency)', 'value': 8, 'tolerance': 0.8, 'unit': 'ms'}, {'quantity': 'touch window end', 'value': 40, 'tolerance': 4, 'unit': 'ms'}, {'quantity': 'fraction of exploration time inside touch windows', 'value': 15.3, 'tolerance': 1.53, 'unit': '%'}]
As fig3c-touch-spikes-l4c2, for the cell identified in example-cell-rates. Since a window end is a whole number of ms, the tolerance on 8 and 40 ms is read as at least 1 ms.
===== text-spikes-per-touch depends ['example-cell-rates']
EXP [{'quantity': 'spikes per first touch', 'value': 1.51, 'tolerance': 0.151}, {'quantity': 'spikes per later touch', 'value': 0.31, 'tolerance': 0.031}, {'quantity': 'onset latency', 'value': 8, 'tolerance': 0.8, 'unit': 'ms'}]
The sentence cites Table 1, whose L4 C2 values (mean 1.36 and 0.74, median 0.87 and 0.33, median latency 8 ms) do not match 1.51 and 0.31, and it sits in the paragraph on the example cell. Readings, (a) the example cell identified in example-cell-rates; (b) the L4 C2 population mean; (c) the L4 C2 population median. Spikes per touch is the mean spike count in the cell's touch spike window (Methods, Spike analysis), first touches of trials apart from later ones. Reproduced when all three values are within tolerance under one reading (latency tolerance at least 1 ms).
===== table1-l4-c2 depends None
EXP [{'quantity': 'spikes per first touch, mean', 'value': 1.36, 'tolerance': 1.32}, {'quantity': 'spikes per first touch, median', 'value': 0.87, 'tolerance': 0.087}, {'quantity': 'spikes per later touch, mean', 'value': 0.74, 'tolerance': 0.87}, {'quantity': 'spikes per later touch, median', 'value': 0.33, 'tolerance': 0.033}, {'quantity': 'spikes evoked by touch, mean', 'value': 70.6, 'tolerance': 20.9, 'unit': '%'}, {'quantity': 'spikes evoked by to
[... 46 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n "add_parser\|def cmd_\|subparsers\|choices" tools/entry.py | head -30; python -c "import nbclient, jupyter_core; print('ok')"; which python; ls ~/.cache 2>/dev/null | head
```

```
380:    parser.add_argument("command", choices=["lock", "check", "run", "all", "handover"])
Traceback (most recent call last):
  File "<string>", line 1, in <module>
    import nbclient, jupyter_core; print('ok')
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
ModuleNotFoundError: No module named 'nbclient'
/opt/hostedtoolcache/Python/3.13.16/x64/bin/python
```

**Agent calls Bash**

```bash
cd  sed -n 1,60p tools/entry.py; grep -n "def run\|venv\|nbconvert\|papermill\|timeout" tools/entry.py | head -30
```

```
"""Lock, check and run one entry. This is the whole local workflow for a deposit.

    python tools/entry.py lock  entries/<name>   # pin the environment
    python tools/entry.py check entries/<name>   # validate metadata and conventions
    python tools/entry.py run   entries/<name>   # execute every notebook from a clean environment
    python tools/entry.py all   entries/<name>   # check, then run
    python tools/entry.py handover entries/<name> # the verifier's package, from the executed copies

`lock` compiles the entry's requirements.in (direct dependencies only) into
requirements.lock.txt with every version pinned.

`check` validates entry.yaml, and the claims and attempt files that mention
the entry, against the schemas, and applies the conventions that keep a result
tied to the data:

- every notebook in the directory is listed in entry.yaml, and exists;
- notebooks are committed without outputs;
- the lock file is present and newer requirements are not left unlocked;
- each notebook, or a helper it imports, names the dataset the entry uses (its identifier and version);
- each notebook has a cell tagged `sanity` that prints what was loaded;
[... 52 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/000013-hires-2015; python -c "
import json
nb=json.load(open('reproduce_hires_2015.ipynb'))
for i,c in enumerate(nb['cells']):
    if i in [44,45,46,47,48,49,67,68,69]:
        print('#### CELL',i,c['cell_type'],c.get('metadata',{}).get('tags',[]))
        print(''.join(c['source']))
"
```

```
#### CELL 44 markdown []
## example-cell-touch-window

> For the example neuron, 74.4% of spikes fell in a window 8 to 40 ms after touch onset, which
> covers 15.3% of exploration time.

As fig3c-touch-spikes-l4c2 (below), for the cell of example-cell-rates, under every reading of
the touch window. The window runs from the latency to latency + t_on.
#### CELL 45 code ['claim:example-cell-touch-window']
ew = W[(W.cell == EXC) & (W.lat_reading == "a")].copy()
ew["end_ms"] = ew.latency + ew.t_on
ew["ok_frac"] = [within(100 * v, 74.4, 7.44) for v in ew.frac_spikes]
ew["ok_start"] = [within(v, 8, 1) for v in ew.latency]
ew["ok_end"] = [within(v, 40, 4) for v in ew.end_ms]
ew["ok_time"] = [within(100 * v, 15.3, 1.53) for v in ew.frac_time]
ew["all_ok"] = ew[["ok_frac", "ok_start", "ok_end", "ok_time"]].all(axis=1)
print(ew[WKEY[1:] + ["latency", "t_on", "end_ms", "frac_spikes", "frac_time", "all_ok"]].round(3).to_string(index=False))
print("readings with all four within tolerance: %d of %d" % (ew.all_ok.sum(), len(ew)))
#### CELL 46 markdown []
**Result: partially reproduced.** For cell 23 the window starts at
[... 76 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/000013-hires-2015; cat > $TMPDIR/edit1.py <<'EOF'
import json
P = 'reproduce_hires_2015.ipynb'
nb = json.load(open(P))
C = nb['cells']
def src(i): return ''.join(C[i]['source'])
def setsrc(i, s):
    C[i]['source'] = s.splitlines(keepends=True)
def rep(i, old, new):
    s = src(i)
    assert old in s, (i, old[:60])
    setsrc(i, s.replace(old, new))

# example-cell-touch-window
rep(45, 'print("readings with all four within tolerance: %d of %d" % (ew.all_ok.sum(), len(ew)))',
'''print("readings with all four within tolerance: %d of %d" % (ew.all_ok.sum(), len(ew)))
for st, g in ew.groupby("start"):
    print(f"start = {st}{' (the criterion)' if st == 'cross' else ' (variant)'}: spikes {100 * g.frac_spikes.min():.1f} to {100 * g.frac_spikes.max():.1f} %, "
          f"window {g.latency.min():.0f} to {g.end_ms.min():.0f}-{g.end_ms.max():.0f} ms, time {100 * g.frac_time.min():.1f} to {100 * g.frac_time.max():.1f} %, "
          f"all four within tolerance in {g.all_ok.sum()} of {len(g)}")''')
# text-spikes-per-touch
rep(48, 'print(TS.groupby(["reading", "latency_from"])', 'print(TS.groupby(["start", "reading", "latency_from"])')
# table 1
for i, name in ((58, "L4 C2"), (60, "L4 outside C2"), (62, "L5")):
    s = src(i)
    s += '''
print("verdicts by start of the cutoff search (cross is the criterion's, first a variant) and whisking reading:")
print(t.groupby(["start", "whisk_with_touch", "latency_from"]).n_ok.agg(["min", "max"]).to_string())
print(t.groupby("start").verdict.value_counts().unstack(fill_value=0).to_string())'''
    setsrc(i, s)
# weaker touch
rep(68, 'print(LW.groupby("start")[["p_first", "p_later"]]', 'print(LW.groupby("start").both.agg(["sum", "size"]).to_string())\nprint(LW.groupby("start")[["p_first", "p_later"]]')
# fig3c
rep(85, 'print("readings within both tolerances: %d of %d" % (t.ok.sum(), len(t)))',
'''print("readings within both tolerances: %d of %d" % (t.ok.sum(), len(t)))
print("by start and longest window (cross is the criterion's start, first a variant):")
print(t.groupby(["start", "tmax"]).agg(ok=("ok", "sum"), n=("ok", "size"), touch_min=("touch_mean", "min"), touch_max=("touch_mean", "max"),
                                       time_min=("time_mean", "min"), time_max=("time_mean", "max")).round(2).to_string())''')
for i in (87, 89):
    s = src(i) + '''
print(t.groupby(["start", "lat_reading", "tmax"]).agg(ok=("ok", "sum"), n=("ok", "size"), touch_min=("touch_mean", "min"), touch_max=("touch_mean", "max"),
                                                      time_min=("time_mean", "min"), time_max=("time_mean", "max"), p_max=("p_vs_c2", "max")).round(3).to_string())'''
    setsrc(i, s)
# fig3d
for i in (93, 95, 97):
    s = src(i) + '''
print(t.groupby(["start", "lat_reading", "tmax", "width"]).agg(ok=("ok", "sum"), n=("ok", "size"), tp_min=("tp_mean", "min"), tp_max=("tp_mean", "max"),
                                                               time_min=("time_mean", "min"), time_max=("time_mean", "max")).round(2).to_string())'''
    setsrc(i, s)
rep(99, 'print("readings meeting the criterion: latency reading (a) %d, (b) %d, of %d" % (po.ok.sum(), po.ok_latb.sum(), len(po)))',
'''print("readings meeting the criterion: latency reading (a) %d, (b) %d, of %d" % (po.ok.sum(), po.ok_latb.sum(), len(po)))
print(po.groupby("start")[["ok", "ok_latb"]].agg(["sum", "size"]).to_string())''')
# fig5c
rep(117, 'print(mis.groupby(["prop", "reading", "start"]).ok.agg(["sum", "size"]).to_string())',
'''print(mis.groupby(["prop", "reading", "start"]).ok.agg(["sum", "size"]).to_string())
print("range of the means by start of the cutoff search:")
print(mis.groupby(["prop", "start"])["mean"].agg(["min", "max"]).round(3).to_string())''')
# whisking-rate-l5
setsrc(81, '''print(WR[WR.group == "L5"].to_string(index=False, float_format="{:.3g}".format))
for r in WR[WR.group == "L5"].itertuples():
    print(f"whisking with touch epochs {r.whisking_with_touch}: p < 0.05 {r.p < 0.05}, median of the per-cell differences positive {r.median_difference > 0}")''')
json.dump(nb, open(P, 'w'), indent=1, ensure_ascii=False)
open(P, 'a').write('\n')
EOF
python $TMPDIR/edit1.py && git diff --stat
```

```
.../000013-hires-2015/reproduce_hires_2015.ipynb   | 56 +++++++++++++++++-----
 1 file changed, 44 insertions(+), 12 deletions(-)
```

**Agent**

Now the helper: the phase decoder gets the two smoothing readings from the answer.

**Agent calls Bash**

```bash
cd entries/000013-hires-2015; python - <<'EOF'
P='hires.py'
s=open(P).read()
old='''def phase_discrimination(C_list, pref, rng, N=1000, reps=100, model="cycles", shifts="random",
                         deltas=np.arange(2, 61, 2), M=50, pseudo=1.0):'''
new='''def phase_discrimination(C_list, pref, rng, N=1000, reps=100, model="cycles", shifts="random",
                         deltas=np.arange(2, 61, 2), M=50, smooth="add_one"):'''
assert old in s; s=s.replace(old,new)
old='''    does) and the percent-correct curves."""'''
new='''    does) and the percent-correct curves.

    Bins with no spikes (claim fig4c-phase-decoding, open detail 3, which the paper does not
    treat): 'add_one' adds one spike to every bin's count over the training cycles (Laplace);
    'floor' raises each bin's rate to at least one spike over all of the cell's training cycles
    and bins, 1 / (120 n), a value of our choosing as the paper gives none; 'spread' adds one
    spike spread over the 120 bins (the earlier run's choice, kept as a variant)."""'''
assert old in s; s=s.replace(old,new)
old='''    zero). Returns per repetition'''
assert old in s
s=s.replace('''rates learned on the other half (one split per recorded cell and repetition, shared by the
    neurons drawn from it); 'poisson': responses drawn as Poisson counts with the cycle-averaged
    rates. Rates get `pseudo` spikes spread over the bins (a standard choice so that no rate is
    zero). Returns per repetition''','''rates learned on the other half (one split per recorded cell and repetition, shared by the
    neurons drawn from it); 'poisson': responses drawn as Poisson counts with the cycle-averaged
    rates. Returns per repetition''')
old='''            lam_cell.append((tr.sum(0) + pseudo / nbins) / max(len(tr), 1))'''
new='''            n = max(len(tr), 1)
            if smooth == "add_one":
                lam_cell.append((tr.sum(0) + 1.0) / n)
            elif smooth == "floor":
                lam_cell.append(np.maximum(tr.sum(0) / n, 1.0 / (nbins * n)))
            else:
                lam_cell.append((tr.sum(0) + 1.0 / nbins) / n)'''
assert old in s; s=s.replace(old,new)
open(P,'w').write(s)
EOF
grep -n "pseudo" hires.py
```

```
(Bash completed with no output)
```

**Agent calls Bash**

```bash
cd entries/000013-hires-2015; python - <<'EOF'
P='hires.py'
s=open(P).read()
pairs=[('''  polynomial, 1 ms steps: claim fig3c-touch-spikes-l4c2. The longest window searched
  (``TMAX_READINGS``) is not given anywhere; both values are readings, asked about in
  questions/000013.yaml.''','''  polynomial, 1 ms steps: claim fig3c-touch-spikes-l4c2. The cutoff is the first increment
  below chance after the increment has been above it (the criterion, after the answer in
  questions/000013.yaml); the literal search from 1 ms is a variant. The longest window searched
  (``TMAX_READINGS``) is not given in the paper; the criterion's open detail (4) lists both
  values as readings.'''),
('''TMAX_READINGS = (100, 200)  # ms, longest touch window searched: open, two readings''','''TMAX_READINGS = (100, 200)  # ms, longest touch window searched: readings (r100), (r200) of the claims file'''),
('''    """Index into t = 1..tmax of the cutoff. 'first': the first increment below chance, read
    literally from t = 1. 'cross': the first increment below chance after the increment has
    been above chance (the transition where the curve levels off, Results, paragraph on Figure
    3); when it is never above chance, the literal cutoff is used and the second value is False."""''',
'''    """Index into t = 1..tmax of the cutoff. 'cross', the criterion's: the first increment below
    chance after the increment has been above chance (the transition where the curve levels off,
    Results, paragraph on Figure 3; claim fig3c-touch-spikes-l4c2); when it is never above
    chance, the literal cutoff is used and the second value is False. 'first', a variant only:
    the first increment below chance, read literally from t = 1."""''')]
for a,b in pairs:
    assert a in s, a[:50]; s=s.replace(a,b)
open(P,'w').write(s)
EOF
```

```
(Bash completed with no output)
```

**Agent**

Now the Figure 4 and refractory-model code cells.

**Agent calls Bash**

```bash
cd entries/000013-hires-2015; cat > $TMPDIR/edit2.py <<'EOF'
import json
P = 'reproduce_hires_2015.ipynb'
nb = json.load(open(P))
C = nb['cells']
def src(i): return ''.join(C[i]['source'])
def setsrc(i, s): C[i]['source'] = s.splitlines(keepends=True)
def rep(i, old, new):
    s = src(i); assert old in s, (i, old[:60]); setsrc(i, s.replace(old, new))

# fig4a: reading (a3), all pre-touch windows
rep(102, 'Q_list.append({"pre_end": Ii[:, 29], "pre_start": Ii[:, 9], "explore":',
         'Q_list.append({"pre_end": Ii[:, 29], "pre_start": Ii[:, 9], "pre_all": Ii[:, 9:30].ravel(), "explore":')
rep(103, '[["pre_end", "pre_start", "explore"]', '[["pre_end", "pre_start", "pre_all", "explore"]')

# fig4b: smoothing variant
rep(108, '''for si, split in enumerate(("half", "independent")):
    for ci, t0b in enumerate((9, 30)):
        rng4b = np.random.default_rng([4200, si, ci])
        dec, tru, rep = hires.time_decoding(I_c2, rng4b, N=200, reps=100, split=split, t0_bin=t0b)''',
'''for si, split in enumerate(("half", "independent")):
    for ci, t0b in enumerate((9, 30)):
      for ai, alpha in enumerate((1.0, 0.01)):
        rng4b = np.random.default_rng([4200, si, ci] + ([ai] if ai else []))
        dec, tru, rep = hires.time_decoding(I_c2, rng4b, N=200, reps=100, split=split, t0_bin=t0b, alpha=alpha)''')
rep(108, "tb_rows.append(dict(split=split, classes_from=t0b - 30, t=t,", "tb_rows.append(dict(split=split, classes_from=t0b - 30, alpha=alpha, t=t,")
s = src(108)
# re-indent the inner body of the alpha loop by two spaces
lines = s.splitlines(keepends=True)
out, inside = [], False
for ln in lines:
    if ln.startswith("      for ai, alpha"):
        inside = True; out.append(ln); continue
    if inside and ln.startswith("        "):
        out.append("  " + ln); continue
    if inside and not ln.startswith("        "):
        inside = False
    out.append(ln)
s = "".join(out).replace("      for ai, alpha", "        for ai, alpha")
setsrc(108, s)
s = src(109)
s = s.replace('print(TB[TB.t.isin([6, 8, 9, 10, 11, 12, 14])].round(3).to_string(index=False))',
              'print(TB[TB.t.isin([6, 8, 9, 10, 11, 12, 14]) & (TB.alpha == 1.0)].round(3).to_string(index=False))')
s = s.replace('mins = near.groupby(["split", "classes_from"])', 'mins = near.groupby(["alpha", "split", "classes_from"])')
s = s.replace('for (sp, cf), g in TB.groupby(["split", "classes_from"]):\n    print(sp, cf,', 'for (al, sp, cf), g in TB.groupby(["alpha", "split", "classes_from"]):\n    print(al, sp, cf,')
setsrc(109, s)

# fig4c: the phase-tuning cycles, smoothing readings
setsrc(112, '''t0 = time.time()
CB, CB_all = {}, {}
for g in ("L4C2", "L4out"):
    Cl, Ca, pref = [], [], []
    for no in G[g]:
        cyc = D[no]["cyc"]
        cp = cyc[cyc.phase_ok & cyc.in_sample]                  # the cycles of phase tuning (criterion)
        Cl.append(hires.cycle_bin_counts(by_no[no], D[no]["s"], cp))
        ca = cyc[cyc.amp_max > hires.WHISK_AMP]                 # every cycle peaking above 2.5 deg (earlier run, variant)
        Ca.append(hires.cycle_bin_counts(by_no[no], D[no]["s"], ca))
        phi = base.loc[no, "phi_pref"]
        pref.append(0.0 if pd.isna(phi) else phi)
    CB[g] = (Cl, np.array(pref))
    CB_all[g] = (Ca, np.array(pref))
    for name, L in (("phase-tuning cycles", Cl), ("all cycles > 2.5 deg (variant)", Ca)):
        print(g, name, "| cycles per cell: median %d, range %d to %d; spikes per cycle, mean over cells %.3f; cells with no spike %d of %d" % (
            np.median([len(x) for x in L]), min(len(x) for x in L), max(len(x) for x in L),
            np.mean([x.sum() / max(len(x), 1) for x in L]), sum(x.sum() == 0 for x in L), len(L)))
READ4C = [("cycles", "add_one"), ("poisson", "add_one"), ("poisson", "floor")]
pd_rows = []
for g in ("L4C2", "L4out"):
    for mi, (model, smooth) in enumerate(READ4C):
        for shi, shifts in enumerate(("random", "even")):
            rng4c = np.random.default_rng([4300, mi, shi, GROUP_ORDER.index(g), 1])
            res, cur = hires.phase_discrimination(CB[g][0], CB[g][1], rng4c, N=1000, reps=100, model=model, shifts=shifts, smooth=smooth)
            pd_rows.append(dict(cycles="phase tuning", group=g, model=model, smooth=smooth, shifts=shifts,
                                median_deg=np.nanmedian(res) if np.isfinite(res).any() else np.nan,
                                runs_reaching=int(np.isfinite(res).sum()), lo=np.nanpercentile(res, 2.5) if np.isfinite(res).any() else np.nan,
                                hi=np.nanpercentile(res, 97.5) if np.isfinite(res).any() else np.nan, pc_at_180=cur[:, -1].mean()))
    # variant: the earlier run's cycles and smoothing, Poisson rates, random shifts
    rng4c = np.random.default_rng([4300, 9, 0, GROUP_ORDER.index(g)])
    res, cur = hires.phase_discrimination(CB_all[g][0], CB_all[g][1], rng4c, N=1000, reps=100, model="poisson", shifts="random", smooth="spread")
    pd_rows.append(dict(cycles="all > 2.5 deg (variant)", group=g, model="poisson", smooth="spread", shifts="random",
                        median_deg=np.nanmedian(res) if np.isfinite(res).any() else np.nan, runs_reaching=int(np.isfinite(res).sum()),
                        lo=np.nanpercentile(res, 2.5) if np.isfinite(res).any() else np.nan,
                        hi=np.nanpercentile(res, 97.5) if np.isfinite(res).any() else np.nan, pc_at_180=cur[:, -1].mean()))
PDC = pd.DataFrame(pd_rows)
print(f"{time.time() - t0:.0f} s")
''')
setsrc(113, '''print(PDC.round(3).to_string(index=False))
for (cy, model, smooth, shifts), g in PDC.groupby(["cycles", "model", "smooth", "shifts"]):
    a_, b_ = g.set_index("group").loc["L4C2"], g.set_index("group").loc["L4out"]
    print(f"{cy} | {model}/{smooth}/{shifts}: C2 {a_.median_deg:.1f} deg (24 +- 2.4: {within(a_.median_deg, 24, 2.4)}), "
          f"outside {b_.median_deg:.1f} deg (33 +- 3.3: {within(b_.median_deg, 33, 3.3)}), C2 better: {a_.median_deg < b_.median_deg}")''')

# fig6d: rate compensated for the refractory period (Berry and Meister 1998)
s = src(134)
s = s.replace('''def simulate_refractory(rate_ms, n_trains, rng, dead=2.3, dt=0.1):
    """Spike times (ms) of n_trains inhomogeneous Poisson trains with an absolute dead time."""
    p = np.repeat(rate_ms, int(round(1 / dt))) * dt
''', '''def free_rate(rate_ms, dead=2.3, dt=0.1, cap=0.95):
    """Berry and Meister (1998): the rate of the process before the dead time, lambda(t) = r(t) /
    (1 - integral of r over [t - dead, t)), so that the output rate is r. r is given per 1 ms bin
    and spread over steps of dt; the integral is capped at `cap` where it would reach 1."""
    r = np.repeat(rate_ms, int(round(1 / dt)))
    k = int(round(dead / dt))
    c = np.r_[0, np.cumsum(r * dt)]
    i = np.arange(len(r))
    integ = c[i] - c[np.maximum(i - k, 0)]
    return r / (1 - np.minimum(integ, cap)), int((integ > cap).sum())


def simulate_refractory(rate_fine, n_trains, rng, dead=2.3, dt=0.1):
    """Spike times (ms) of n_trains inhomogeneous Poisson trains with an absolute dead time;
    rate_fine is in spikes/ms per step of dt."""
    p = rate_fine * dt
''')
s = s.replace('''                X = hires.window_counts(c, s, on, np.arange(0, 31), 1)       # 1 ms PSTH, 0 to 30 ms
                rate = X.mean(0)
                rngr = np.random.default_rng([6400, oi, 0 if touches == "pooled" else (1 if minpts == "5" else 2), no, gi])
                sim = simulate_refractory(rate, len(on), rngr)
                ff_model = ff_windows(sim, starts20)
                Xd = hires.window_counts(c, s, on, starts20, 10)
                with np.errstate(invalid="ignore", divide="ignore"):
                    ff_data = Xd.var(0, ddof=1) / Xd.mean(0)
                ref_rows.append(dict(ici_from=ici_from, touches=touches, minpts=minpts, cell=no, group=gi + 1, ff_data=ff_data, ff_model=ff_model))''',
'''                X = hires.window_counts(c, s, on, np.arange(-PRE6D, 31), 1)   # 1 ms PSTH, -10 to 30 ms
                rate = X.mean(0)
                Xd = hires.window_counts(c, s, on, starts20, 10)
                with np.errstate(invalid="ignore", divide="ignore"):
                    ff_data = Xd.var(0, ddof=1) / Xd.mean(0)
                lam, n_cap = free_rate(rate)
                for mi, (model, rf) in enumerate((("compensated", lam), ("uncompensated", np.repeat(rate, 10)))):
                    rngr = np.random.default_rng([6400, oi, 0 if touches == "pooled" else (1 if minpts == "5" else 2), no, gi, mi])
                    sim = [list(np.asarray(tr) - PRE6D) for tr in simulate_refractory(rf, len(on), rngr)]
                    Xm = np.array([[np.sum((np.asarray(tr) >= a) & (np.asarray(tr) < a + 10)) for a in starts20] for tr in sim])
                    ref_rows.append(dict(ici_from=ici_from, touches=touches, minpts=minpts, cell=no, group=gi + 1, model=model, ff_data=ff_data,
                                         ff_model=ff_windows(sim, starts20), mean_data=Xd.mean(0), mean_model=Xm.mean(0), n_capped=n_cap))''')
s = s.replace('t0 = time.time()\nref_rows = []', 'PRE6D = 10   # ms of PSTH before onset, so that the integral of the free rate starts before the first window\nt0 = time.time()\nref_rows = []')
setsrc(134, s)
s = src(135)
s = s.replace('for (ici_from, touches, minpts), g in REF.groupby(["ici_from", "touches", "minpts"]):',
              'for (model, ici_from, touches, minpts), g in REF.groupby(["model", "ici_from", "touches", "minpts"]):')
s = s.replace('rows.append(dict(ici_from=ici_from,', 'rows.append(dict(model=model, ici_from=ici_from,')
s = s.replace('''F6D = pd.DataFrame(rows)
print(F6D.round(4).to_string(index=False))''', '''F6D = pd.DataFrame(rows)
print(F6D.round(4).to_string(index=False))
# does the model's mean count match the data's? ratio of the population mean counts in the 10 ms windows
for model, g in REF.groupby("model"):
    md = np.vstack(g.mean_data.to_numpy()).mean(0)
    mm = np.vstack(g.mean_model.to_numpy()).mean(0)
    print(f"{model}: model / data mean count over the 21 windows, {np.min(mm / md):.3f} to {np.max(mm / md):.3f} (at the 0 to 10 ms window {mm[0] / md[0]:.3f});"
          f" steps where the free-rate integral was capped: {int(g.n_capped.sum())}")''')
setsrc(135, s)
json.dump(nb, open(P, 'w'), indent=1, ensure_ascii=False)
open(P, 'a').write('\n')
EOF
python $TMPDIR/edit2.py && python -c "
import json
nb=json.load(open('reproduce_hires_2015.ipynb'))
for i in (108,109,134,135):
    print('####',i); print(''.join(nb['cells'][i]['source']))
"
```

```
#### 108
t0 = time.time()
I_c2 = DEC["L4C2"][0]
tb_rows = []
for si, split in enumerate(("half", "independent")):
    for ci, t0b in enumerate((9, 30)):
        for ai, alpha in enumerate((1.0, 0.01)):
          rng4b = np.random.default_rng([4200, si, ci] + ([ai] if ai else []))
          dec, tru, rep = hires.time_decoding(I_c2, rng4b, N=200, reps=100, split=split, t0_bin=t0b, alpha=alpha)
          for t in range(0, 21):
              sel = tru == t
              err = dec[sel] - t
              rms = np.sqrt(np.mean(err ** 2))
              lo, hi = np.percentile(dec[sel], [2.5, 97.5])
              tb_rows.append(dict(split=split, classes_from=t0b - 30, alpha=alpha, t=t, rms=rms, half95=(hi - lo) / 2, rms196=1.96 * rms,
                                  exact=np.mean(err == 0)))
TB = pd.DataFrame(tb_rows)
print(f"{time.time() - t0:.0f} s")
#### 109
print(TB[TB.t.isin([6, 8, 9, 10, 11, 12, 14]) & (TB.alpha == 1.0)].round(3).to_string(index=False))
[... 105 more lines not kept]
```

**Agent**

Cell 108's indentation came out uneven, so I'll rewrite it cleanly.

**Agent calls Bash**

```bash
cd entries/000013-hires-2015; python - <<'EOF'
import json
P='reproduce_hires_2015.ipynb'
nb=json.load(open(P))
nb['cells'][108]['source']='''t0 = time.time()
I_c2 = DEC["L4C2"][0]
tb_rows = []
for si, split in enumerate(("half", "independent")):
    for ci, t0b in enumerate((9, 30)):
        for ai, alpha in enumerate((1.0, 0.01)):     # add-one smoothing (criterion), a smaller pseudocount (variant)
            rng4b = np.random.default_rng([4200, si, ci] + ([ai] if ai else []))
            dec, tru, rep = hires.time_decoding(I_c2, rng4b, N=200, reps=100, split=split, t0_bin=t0b, alpha=alpha)
            for t in range(0, 21):
                sel = tru == t
                err = dec[sel] - t
                rms = np.sqrt(np.mean(err ** 2))
                lo, hi = np.percentile(dec[sel], [2.5, 97.5])
                tb_rows.append(dict(split=split, classes_from=t0b - 30, alpha=alpha, t=t, rms=rms, half95=(hi - lo) / 2,
                                    rms196=1.96 * rms, exact=np.mean(err == 0)))
TB = pd.DataFrame(tb_rows)
print(f"{time.time() - t0:.0f} s")
'''.splitlines(keepends=True)
json.dump(nb, open(P,'w'), indent=1, ensure_ascii=False); open(P,'a').write('\n')
EOF
cd ..; cd ..; python tools/entry.py check entries/000013-hires-2015 2>&1 | tail -5
```

```
0 error(s)
```

**Agent**

The check passes. Running the notebook now; it takes around ten minutes or more.

**Agent calls Bash**

```bash
cd  time python tools/entry.py run entries/000013-hires-2015 2>&1 | tail -20
```

```
Installed kernelspec registry-000013-hires-2015 in executed/000013-hires-2015/.venv/share/jupyter/kernels/registry-000013-hires-2015
pass  reproduce_hires_2015.ipynb  (540 s)

real	9m8.996s
user	7m5.385s
sys	0m48.252s
```

**Agent calls Bash**

```bash
cd  cat > $TMPDIR/out.py <<'EOF'
import json,sys
nb=json.load(open('executed/000013-hires-2015/reproduce_hires_2015.ipynb'))
for i in map(int, sys.argv[1:]):
    c=nb['cells'][i]
    print('#### CELL',i)
    for o in c.get('outputs',[]):
        if 'text' in o: print(''.join(o['text']))
        elif 'data' in o and 'text/plain' in o['data'] and 'image/png' not in o['data']: print(''.join(o['data']['text/plain']))
EOF
python $TMPDIR/out.py 15 45 48 58 60 62 68 81
```

```
#### CELL 15
touch windows: 1664 rows in 34 s
cells whose increment never rose above chance under `cross` (the literal cutoff is used):
group  shuffle   nearest  tmax
L4out  circular  before   100                                 [32]
                          200                             [32, 32]
                 either   100                                 [32]
                          200                                 [32]
       uniform   before   100                         [32, 38, 38]
                          200                             [32, 32]
                 either   100                         [32, 39, 39]
                          200                             [39, 39]
L5     circular  before   100                     [43, 43, 51, 51]
                          200                     [43, 43, 49, 49]
                 either   100                     [43, 43, 51, 51]
                          200                     [43, 43, 47, 47]
       uniform   before   100                     [43, 43, 51, 51]
                          200                     [43, 43, 50, 50]
                 either   100             [43, 43, 50, 50, 51, 51]
                          200     [43, 43, 47, 47, 50, 50, 51, 51]
[... 165 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 1,80p claims/000013/10.7554-elife.06619.yaml; grep -n "whisking periods\|touch epochs" claims/000013/10.7554-elife.06619.yaml | head -30
```

```
# Claims for Hires, Gutnisky, Yu, O'Connor & Svoboda (2015), eLife 4, e06619, "Low-noise encoding
# of active touch by layer 4 in the somatosensory cortex", on dandiset 000013.
# Written by an agent (model "claude-opus-5-5", Claude Code in GitHub Actions), 2026-10-21, protocol
# pilot-10 as stated in docs/protocol.md (Reader).
#
# Text read: the version of record (PMC4525079) as served by Europe PMC
# (paper/10.7554-elife.06619.txt): Introduction, Results, Discussion, Materials and methods, Table 1,
# the legends of Figures 1 to 6 and of their figure supplements (Figure 1, supplements 1 and 2;
# Figure 2, supplement 1; Figure 3, supplements 1 and 2; Figure 4, supplement 1; Figure 6,
# supplement 1), the decision letter and the author response. eLife has no supplement beyond
# these figure supplements, whose legends are in the text. No PDF was supplied, so the figure
# images were not read. Table 1 came through as one run of text; its columns were read in order
# (9 measures, rows of mean +- s.d., median and range for each of three populations). One cell of
# it is garbled, the L5 "Spikes evoked (touch)" mean printed "24.0-18.6%", read as 24.0 +- 18.6%
# from Results, paragraph on Figure 3C.
#
# Code read: the paper links the Janelia Whisker Tracker (openwiki.janelia.org, not code for the
# analyses) and https://github.com/hireslab/HLab_Whiskers for the detection of contact periods.
# Read at HEAD, commit cdbc9148da6c505ba940b971fbe419b11cb80049 (2020-12-11); the last commit
# before publication is 0eb360a (2014-11-19). It holds MATLAB classes for behaviour trials (+Solo),
[... 72 more lines not kept]
```

**Agent**

Table 1 for L4 C2 now turns only on whether whisking periods include touch epochs: 15 of 18 without them, 14 with. Next, the outputs for Figures 3, 4, 5 and 6D.

**Agent calls Bash**

```bash
cd  python $TMPDIR/out.py 85 87 89 93 95 97 99 2>&1 | grep -v "^ *uniform\|^ *circular" | head -150
```

```
#### CELL 85
 shuffle nearest  tmax start  touch_mean  touch_sd  touch_median  time_mean  ok_values    ok
readings within both tolerances: 5 of 16
by start and longest window (cross is the criterion's start, first a variant):
            ok  n  touch_min  touch_max  time_min  time_max
start tmax                                                 
cross 100    4  4      66.88      73.81     14.60     16.27
      200    1  4      68.86      75.80     16.01     17.58
first 100    0  4      38.62      42.84      8.53      9.60
      200    0  4      59.24      64.47     11.89     13.36

plotted ranges: time 0.9 to 49.0 %, spikes 0.0 to 94.3 %

#### CELL 87
lat_reading  shuffle nearest  tmax start  touch_mean  touch_sd  touch_median  time_mean p_vs_c2  lower_than_c2  ok_values  variant_zero_mean    ok
          a circular  before   100 cross      28.186    22.421        29.245     21.209       0           True      False             27.014 False
          a circular  before   100 first       1.526     1.261         1.148      1.250   0.069           True      False              1.382 False
          a circular  before   200 cross      28.827    26.705        25.921     21.673       0           True      False             22.300 False
          a circular  before   200 first       1.758     1.275         1.764      1.564   0.001           True      False              1.613 False
          a circular  either   100 cross      20.540    16.630        17.785     19.713       0           True      False             19.521 False
[... 130 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python $TMPDIR/out.py 97 99 103 105 109 112 113 117 120 2>&1 | grep -v "^ *uniform\|^ *circular" | head -230
```

```
#### CELL 97
                        tp_mean      time_mean       p_vs_c2         
                            min  max       min  max      min      max
start lat_reading width                                              
cross a           pm       40.3 52.7      29.8 39.9 9.88e-06 0.000458
                  total    36.4 48.6      26.3   41 6.62e-06 9.43e-05
      b           pm       40.3 52.7      29.8 39.9 9.88e-06 0.000458
                  total    36.4 48.6      26.3   41 6.62e-06 9.43e-05
first a           pm       16.9 24.7      12.1 16.3 0.000699    0.165
                  total    6.14 23.2      3.79 15.5 0.000509    0.112
      b           pm       16.9 24.7      12.1 16.3 0.000699    0.165
                  total    6.14 23.2      3.79 15.5 0.000509    0.112
readings meeting the criterion: 8 of 64
                              ok  n  tp_min  tp_max  time_min  time_max
start lat_reading tmax width                                           
cross a           100  pm      0  4   40.34   45.30     29.83     35.31
                       total   4  4   36.40   37.50     26.31     28.11
                  200  pm      0  4   45.44   52.68     34.34     39.91
                       total   0  4   40.33   48.65     30.56     40.98
      b           100  pm      0  4   40.34   45.30     29.83     35.31
[... 202 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python $TMPDIR/out.py 134 135 152
```

```
#### CELL 134
12 s

#### CELL 135
        model ici_from touches minpts  units  start_of_min  data_ff  model_ff  sem_sum  a_ok  cells_below   n  sign_p  b_ok
  compensated   offset   group      5     94             3   0.7466    0.7445   0.0601 False           61  89  0.0003  True
  compensated   offset   group      N     94             4   0.7530    0.7133   0.0588 False           52  91  0.1041 False
  compensated   offset  pooled      -     31             3   0.7912    0.7633   0.0855 False           17  31  0.3601 False
  compensated    onset   group      5    103             3   0.7657    0.7775   0.0625 False           61 100  0.0176  True
  compensated    onset   group      N    103             3   0.7755    0.7155   0.0546 False           59  99  0.0350  True
  compensated    onset  pooled      -     31             3   0.8190    0.7862   0.0870 False           22  31  0.0147  True
uncompensated   offset   group      5     94             3   0.7466    0.7600   0.0547 False           66  86  0.0000  True
uncompensated   offset   group      N     94             4   0.7530    0.7782   0.0521 False           67  89  0.0000  True
uncompensated   offset  pooled      -     31             3   0.7912    0.7766   0.0777 False           22  31  0.0147  True
uncompensated    onset   group      5    103             3   0.7657    0.7687   0.0528 False           77  97  0.0000  True
uncompensated    onset   group      N    103             3   0.7755    0.8135   0.0467 False           80 102  0.0000  True
uncompensated    onset  pooled      -     31             3   0.8190    0.8031   0.0751 False           21  31  0.0354  True
compensated: model / data mean count over the 21 windows, 1.001 to 1.034 (at the 0 to 10 ms window 1.001); steps where the free-rate integral was capped: 0
uncompensated: model / data mean count over the 21 windows, 0.796 to 0.891 (at the 0 to 10 ms window 0.807); steps where the free-rate integral was capped: 0

[... 3 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python - <<'EOF'
import yaml
d=yaml.safe_load(open('claims/000013/10.7554-elife.06619.yaml'))
for c in d['claims']:
    if c['id'] in ('whisking-rate-l5-increase','whisking-rate-l4-no-change'):
        print(c['id'], c.get('expected'), c.get('statement'))
EOF
python $TMPDIR/out.py 57 | head -80
```

```
whisking-rate-l4-no-change None Across L4 neurons, inside and outside C2, spike rate does not change between whisking and non-whisking periods.
whisking-rate-l5-increase None L5 neurons fire modestly but significantly more during whisking than during non-whisking periods.
#### CELL 57

L4C2: 256 reading combinations; values within tolerance: min 9, max 15 (of 18 numeric values)
verdict
partially         160
reproduced         64
not reproduced     32
       min  max
start          
cross   14   15
first    9   14
fraction of combinations in which each value is within tolerance:
ok_spt_first_mean       1.0
ok_spt_first_median     0.0
ok_spt_later_mean       1.0
ok_spt_later_median     0.5
ok_touch_pct_mean      0.75
ok_touch_pct_median    0.75
[... 62 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/000013-hires-2015; cat > $TMPDIR/edit3.py <<'EOF'
import json
P = 'reproduce_hires_2015.ipynb'
nb = json.load(open(P))
C = nb['cells']
def src(i): return ''.join(C[i]['source'])
def setsrc(i, s): C[i]['source'] = s.splitlines(keepends=True)
def rep(i, old, new):
    s = src(i); assert old in s, (i, old[:60]); setsrc(i, s.replace(old, new))

# Table 1: the first reading each open detail lists, and the criterion's readings
rep(57, 'T1 = pd.DataFrame(t1_rows)\n', '''T1 = pd.DataFrame(t1_rows)
# the criterion's readings: the transition cutoff (answer in questions/000013.yaml) and whisking periods outside touch
# epochs (the claims file's definitions, "For other epochs ... whisking epochs have amplitude >2.5 deg")
T1["criterion"] = (T1.start == "cross") & ~T1.whisk_with_touch
FIRST = dict(lat_reading="a", shuffle="uniform", nearest="before", tmax=100, start="cross", width="pm", whisk_with_touch=False, latency_from="lat_first")


def first_reading(t):
    """The values under the first reading of every open detail, in the claims file's order."""
    r = t[np.logical_and.reduce([t[k] == v for k, v in FIRST.items()])].iloc[0]
    return [(f"{m}_{stat}", round(float(r[f"{m}_{stat}"]), 3), e, tol, bool(r[f"ok_{m}_{stat}"])) for m, stat, e, tol in EXPECT[r.group]]
''')
for i in (58, 60, 62):
    s = src(i) + '''
c = t[t.criterion]
print("under the criterion's readings (cross, whisking outside touch epochs): values within tolerance %d to %d over %d combinations;" % (c.n_ok.min(), c.n_ok.max(), len(c)),
      "verdicts", c.verdict.value_counts().to_dict())
print(c.groupby(["tmax", "width"]).n_ok.agg(["min", "max"]).to_string())
print("values under the first reading of each open detail (measured, expected, tolerance, within):")
for row in first_reading(t):
    print("  ", row)'''
    setsrc(i, s)
# fig5c: measured values under the first reading listed
rep(117, 'print("cells with an undefined index', '''sel = (mis.shuffle == "uniform") & (mis.nearest == "before") & (mis.tmax == 100) & (mis.start == "cross")
print("first reading of each open detail (uniform, before, 100 ms, transition cutoff; ranks, onset, whole touch):",
      {p: round(float(mis[sel & (mis.prop == p) & (mis.reading == r)]["mean"].iloc[0]), 3) for p, r in (("order", "ranks"), ("velocity", "onset"), ("curvature", "touch"))})
print("cells with an undefined index''')
json.dump(nb, open(P, 'w'), indent=1, ensure_ascii=False)
open(P, 'a').write('\n')
EOF
python $TMPDIR/edit3.py && echo ok
```

```
ok
```

**Agent calls Bash**

```bash
cd entries/000013-hires-2015; sed -i 's/for m, stat, e, tol in EXPECT\[r.group\]\]/for m, stat, e, tol in EXPECT[r[\\"group\\"]]]/' reproduce_hires_2015.ipynb; grep -n 'EXPECT\[r' reproduce_hires_2015.ipynb; cd ../..; python tools/entry.py run entries/000013-hires-2015 2>&1 | tail -2; python $TMPDIR/out.py 58 60 62 117 | grep -v "^ *uniform\|^ *circular"
```

```
1328:    "    return [(f\"{m}_{stat}\", round(float(r[f\"{m}_{stat}\"]), 3), e, tol, bool(r[f\"ok_{m}_{stat}\"])) for m, stat, e, tol in EXPECT[r[\"group\"]]]\n",
Installed kernelspec registry-000013-hires-2015 in executed/000013-hires-2015/.venv/share/jupyter/kernels/registry-000013-hires-2015
pass  reproduce_hires_2015.ipynb  (538 s)
#### CELL 58
L4 C2: verdicts over the reading combinations: {'partially': 160, 'reproduced': 64, 'not reproduced': 32}
medians within tolerance, per combination: min 3, max 6 of 9
            min  max
start tmax          
cross 100    14   15
      200    14   15
first 100     9   10
      200    13   14
verdicts by start of the cutoff search (cross is the criterion's, first a variant) and whisking reading:
                                     min  max
start whisk_with_touch latency_from          
cross False            lat_all        15   15
                       lat_first      15   15
      True             lat_all        14   14
                       lat_first      14   14
first False            lat_all        10   14
[... 165 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python $TMPDIR/out.py 103 113 135 | grep -E "^pre|^explore|phase tuning \||variant\) \||compensated" | head -30
```

```
pre_end    detected            4
pre_start  detected            1
pre_all    detected            1
explore    detected           11
all > 2.5 deg (variant) | poisson/spread/random: C2 64.5 deg (24 +- 2.4: False), outside 123.0 deg (33 +- 3.3: False), C2 better: True
phase tuning | cycles/add_one/even: C2 nan deg (24 +- 2.4: False), outside nan deg (33 +- 3.3: False), C2 better: False
phase tuning | cycles/add_one/random: C2 nan deg (24 +- 2.4: False), outside nan deg (33 +- 3.3: False), C2 better: False
phase tuning | poisson/add_one/even: C2 60.0 deg (24 +- 2.4: False), outside 40.7 deg (33 +- 3.3: False), C2 better: False
phase tuning | poisson/add_one/random: C2 84.0 deg (24 +- 2.4: False), outside 35.7 deg (33 +- 3.3: True), C2 better: False
phase tuning | poisson/floor/even: C2 12.0 deg (24 +- 2.4: False), outside 6.0 deg (33 +- 3.3: False), C2 better: False
phase tuning | poisson/floor/random: C2 14.8 deg (24 +- 2.4: False), outside 6.0 deg (33 +- 3.3: False), C2 better: False
  compensated   offset   group      5     94             3   0.7466    0.7445   0.0601 False           61  89  0.0003  True
  compensated   offset   group      N     94             4   0.7530    0.7133   0.0588 False           52  91  0.1041 False
  compensated   offset  pooled      -     31             3   0.7912    0.7633   0.0855 False           17  31  0.3601 False
  compensated    onset   group      5    103             3   0.7657    0.7775   0.0625 False           61 100  0.0176  True
  compensated    onset   group      N    103             3   0.7755    0.7155   0.0546 False           59  99  0.0350  True
  compensated    onset  pooled      -     31             3   0.8190    0.7862   0.0870 False           22  31  0.0147  True
uncompensated   offset   group      5     94             3   0.7466    0.7600   0.0547 False           66  86  0.0000  True
uncompensated   offset   group      N     94             4   0.7530    0.7782   0.0521 False           67  89  0.0000  True
uncompensa
[... 5 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python $TMPDIR/out.py 85 93 99 | grep -E "cross|start|L4C2" | head -40; python $TMPDIR/out.py 120 | head -3; python - <<'EOF'
import json
nb=json.load(open('executed/000013-hires-2015/reproduce_hires_2015.ipynb'))
# fig5 corr ok combos under cross reading a
EOF
```

```
shuffle nearest  tmax start  touch_mean  touch_sd  touch_median  time_mean  ok_values    ok
circular  before   100 cross       70.86     17.36         77.48      14.60       True  True
circular  before   200 cross       73.89     12.99         78.09      16.01       True  True
circular  either   100 cross       66.88     15.46         68.00      14.92       True  True
circular  either   200 cross       68.86     14.16         71.85      16.50      False False
 uniform  before   100 cross       73.81     14.89         79.98      16.27       True  True
 uniform  before   200 cross       75.80     13.20         80.34      17.48      False False
 uniform  either   100 cross       68.56     15.64         71.31      16.00       True  True
 uniform  either   200 cross       70.28     14.30         71.85      17.58      False False
by start and longest window (cross is the criterion's start, first a variant):
start tmax                                                 
cross 100    4  4      66.88      73.81     14.60     16.27
 shuffle nearest  tmax start width  tp_mean  tp_sd  time_mean  phase_only_mean  phase_only_sd  ok_values    ok
circular  before   100 cross    pm    77.85  14.20      24.86             6.99           8.97      False False
circular  before   100 cross total    77.29  14.01      24.04             6.43           8.34       True  True
circular  before   200 cross    pm    79.58  13.01      26.41             5.70           6.63      False False
circular  before   200 cross total    80.25  11.55      27.15             6.37           6.68      False False
circular  either   100 cross    pm    76.18  12.51      25.59             9.30          11.01      False False
circular  either   100 cross total    74.56  12.57      24.19             7.68           9.54       True  True
circular  either   200 cross    pm    77.80  12.97      27.22             8.95           9.97      False False
[... 23 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python $TMPDIR/out.py 99 | grep cross; python $TMPDIR/out.py 87 89 | grep -c cross
```

```
circular  before   100 cross    pm  6.99  27.03 19.43       26.92    19.43  True     True
circular  before   100 cross total  6.43  20.29 10.74       19.98    10.74  True     True
circular  before   200 cross    pm  5.70  22.52 25.16       21.11    25.16 False    False
circular  before   200 cross total  6.37  27.31 14.72       27.11    14.72  True     True
circular  either   100 cross    pm  9.30  29.99 23.29       29.79    23.29 False    False
circular  either   100 cross total  7.68  21.66 15.98       21.46    15.98  True     True
circular  either   200 cross    pm  8.95  21.79 25.36       22.91    25.36 False    False
circular  either   200 cross total  8.24  28.01 24.37       28.79    24.37 False    False
 uniform  before   100 cross    pm  7.04  22.14 18.09       22.15    18.09  True     True
 uniform  before   100 cross total  5.14  20.42 10.30       20.34    10.30  True     True
 uniform  before   200 cross    pm  5.93  28.48 16.97       23.31    16.97  True     True
 uniform  before   200 cross total  5.30  26.23 12.52       26.38    12.52  True     True
 uniform  either   100 cross    pm  8.29  26.36 18.98       26.39    18.98  True     True
 uniform  either   100 cross total  7.84  22.29 15.83       22.33    15.83  True     True
 uniform  either   200 cross    pm  9.04  32.13 23.71       32.77    23.71 False    False
 uniform  either   200 cross total  7.39  28.45 18.59       29.19    18.59  True     True
cross  11   16      11   16
34
```

**Agent**

All the numbers are in. I'll now rewrite the conclusion cells, the section introductions, the header and the summary.

**Agent calls Bash**

```bash
cd entries/000013-hires-2015; python -c "
import json
nb=json.load(open('reproduce_hires_2015.ipynb'))
for i in (8,10,56,78,83,91,115,119,122,126,129,137):
    print('####',i); print(''.join(nb['cells'][i]['source']))
" | head -150
```

```
#### 8
**Clocks.** The trials table, the behaviour series and the spike train each carry timestamps.
Behaviour segments start within 5 ms of each trial's `start_time`. In 36 files the
`SpikeTrain` timestamps start 10 ms before the voltage (`CurrentClampSeries`) timestamps, though
the spike samples line up with the voltage samples one for one; in 16 files the two agree. The
cell below asks which clock puts the spikes on the behaviour's time: the touch response is the
contrast. If the `SpikeTrain` timestamps are right, the touch-response peak should fall at the
same latency in both kinds of file; if the voltage timestamps are right, the peaks in the 36
files should sit 10 ms earlier than the others under the `SpikeTrain` clock.
#### 10
**Recordings deposited twice.** Pairs of files from the same subject are compared trial by
trial on the whisker angle and the spike train.
#### 56
## Table 1: table1-l4-c2, table1-l4-outside, table1-l5

> For the 31 L4 C2 cells Table 1 gives, as mean +- s.d. (median), spikes per first touch 1.36 +-
> 1.32 (0.87), per later touch 0.74 +- 0.87 (0.33), touch-evoked spikes 70.6 +- 20.9% (74.7%),
> touch and whisking spikes 75.2 +- 19.0% (80.3%), phase modulation depth 0.67 +- 0.32 (0.70),
> non-whisking rate 1.31 +- 2.88 (0.32) spikes/s, whisking rate 1.39 +- 2.33 (0.33) spikes/s,
> onset latency 7.8 +- 3.0 (8) ms and minimum ISI 2.9 +- 1.9 (2.3) ms.
[... 119 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/000013-hires-2015; cat > $TMPDIR/edit4.py <<'PYEOF'
import json, re
P = 'reproduce_hires_2015.ipynb'
nb = json.load(open(P))
C = nb['cells']
def src(i): return ''.join(C[i]['source'])
def setsrc(i, s): C[i]['source'] = s.rstrip('\n').splitlines(keepends=True)
def rep(i, old, new):
    s = src(i); assert old in s, (i, old[:60]); setsrc(i, s.replace(old, new))

# header
rep(0, '''Every claim's data are in the dandiset, so none is blocked before the analysis; the outcomes,
some of them `blocked` as `methods_underspecified` where the readings disagree, are in the
summary at the end.''', '''Every claim's data are in the dandiset, so none is blocked before the analysis; the outcomes,
some of them `blocked` as `methods_underspecified` where the readings disagree, are in the
summary at the end.

Answers. A first run asked seven questions (`questions/000013.yaml`). A reader answered them
from the paper, and the claims file now carries the answers. This run follows the updated
criteria: the touch-window cutoff is the transition where the curve levels off, the literal
search from 1 ms being a variant only (fig3c-touch-spikes-l4c2, fig3d-touch-phase-l4c2, and the
claims that use the touch window); the longest window of the cutoff curve is an open detail
with readings of 100 and 200 ms; touch detection adds the reading with every pre-touch window
(fig4a-touch-detection-c2); the time decoder's classes and smoothing are readings
(fig4b-touch-time-precision); the phase decoder uses the cycles of phase tuning, with two
readings for empty bins (fig4c-phase-decoding); the refractory model's rate is raised so that
its output matches the cell's touch response (fig6d-not-refractory); and the L5 whisking
increase is the median of the per-cell differences (whisking-rate-l5-increase).''')
# strip bold labels other than the Result openers
for i, c in enumerate(C):
    if c['cell_type'] != 'markdown':
        continue
    s = src(i)
    s2 = re.sub(r'\*\*(?!Result:)([^*]+?)\*\*', r'\1', s)
    if s2 != s:
        setsrc(i, s2)

setsrc(14, '''### Touch spike windows

The claims file (fig3c-touch-spikes-l4c2) leaves four details open and lists their readings:
the shuffle (`uniform` over exploration time, or `circular` shifts within each trial), the
closest touch onset (`before` the spike, or on `either` side), the 1 ms step, and the longest
window over which the curve is built and the degree-11 polynomial fitted, 100 or 200 ms
(`tmax`, readings r100 and r200). Where the search for the cutoff starts (`start`) was asked,
and the answer is now in the criterion: `cross`, the first increment below chance after the
increment has been above it, the transition where "the curve levels off" (Results, paragraph on
Figure 3). The literal search from t = 1 ms (`first`) is computed as well and shown only as a
variant; the fitted polynomial dips at the start of a steep curve, so it often stops at 1 ms.
Outcomes rest on `cross`.

Cells without a first-touch latency take reading (a), latency 0 ms, or (b), the all-touch
latency where there is one and else 0 ms (claim fig3c-touch-spikes-outside). Cells with a
first-touch latency use it under both. Each cell and reading has its own random generator.''')

setsrc(46, '''**Result: partially reproduced.** For cell 23 the transition cutoff and the literal one
give the same window under every reading: it starts at the 8 ms latency and ends at 36 to 38
ms (paper 8 to 40 ms, within tolerance). The fraction of exploration spikes in it is 78.4 to
79.1% when the closest onset is read on either side (within 74.4 +- 7.44%) and 83.6 to 84.6%
when it is read as the onset before the spike (outside). The window covers 19.0 to 20.2% of
exploration time under every reading, against 15.3 +- 1.53%. No reading puts all four values in
tolerance.''')

setsrc(49, '''**Result: reproduced.** Under reading (a), the example cell, there are
1.474 to 1.505 spikes per first touch and 0.302 to 0.307 per later touch with an 8 ms latency
(9 ms from all touches), within tolerance under all 8 window readings of the transition cutoff
(and the 8 of the literal variant, which give the same window for this cell). The L4 C2 mean
(1.16 to 1.28 and 0.62 to 0.69 under the transition cutoff) and median (0.70 to 0.73 and 0.31
to 0.33), readings (b) and (c), do not match, which agrees with the claims file's note that the
sentence is about the example cell.''')

rep(56, '''(and the same measures for the 10 L4 cells outside C2 and the 11 L5 cells). Each value is
computed under every combination of readings: the touch window (16, and the two latency
readings for cells without a first-touch latency), the phase window width, whisking with or
without touch epochs, and the latency from first touches or from all touches. The criterion
counts the values within tolerance (15 of 18 for L4 C2 and L5, 13 of 17 for L4 outside C2).''',
'''(and the same measures for the 10 L4 cells outside C2 and the 11 L5 cells). Each value is
computed under every combination of readings: the touch window (8 with the transition cutoff,
the criterion's, and 8 more with the literal cutoff as a variant, and the two latency readings
for cells without a first-touch latency), the phase window width, whisking with or without
touch epochs, and the latency from first touches or from all touches. The criterion counts the
values within tolerance (15 of 18 for L4 C2 and L5, 13 of 17 for L4 outside C2).

Whisking periods are read here as the claims file defines them, outside touch epochs ("Touch
epochs are periods of contact. For other epochs theta is band-passed ... whisking epochs have
amplitude >2.5 deg"; the answer about fig4c-phase-decoding quotes the Methods to the same
effect). Whisking with touch epochs, which the whisking-rate claims list as a reading of their
own, is shown here as a variant.''')

setsrc(59, '''**Result: reproduced.** Under the criterion's readings, the transition
cutoff with whisking periods outside touch epochs, 15 of the 18 values are within tolerance in
all 64 combinations of the other readings (the 100 and 200 ms curves, the shuffle, the closest
onset, the phase window width and the latency PCTH), at the threshold for reproduced. The three
outside tolerance are medians: spikes per first touch (0.704 under the first reading of each
detail, against 0.87 +- 0.087), modulation depth (1.0 against 0.70) and whisking rate (0.86
against 0.33). Spikes evoked by touch are 73.8% (median 80.0%) and by touch or phase 80.9%
(82.7%) under the first reading. With touch epochs in the whisking rate (a variant) the mean
whisking rate also falls outside and the count is 14 (partially); with the literal cutoff (a
variant) it is 9 to 14. Fourteen of the 25 cells with a phase fit have a depth of 1; the median
L4 C2 cell has 4 spikes in the phase-analysis cycles.''')

setsrc(61, '''**Result: blocked (methods_underspecified).** Under the criterion's
readings the count of values within tolerance is 7 to 9 of 17, which falls on both sides of the
threshold for partially reproduced (9): 52 combinations give not reproduced and 12 partially,
the difference coming from the touch-window readings. The medians of spikes per touch are not 0
under any reading; the means of spikes per touch (0.31 and 0.15 under the first reading,
against 0.08 and 0.02), the touch-evoked fraction (26.2%, median 23.8%, against 9.2% and 3.6%)
and the latency mean (8.1 ms over the cells with a latency, against 18.5) are outside
tolerance. Rates, mean depth and the minimum ISI are within it. The literal cutoff, a variant,
gives 10 to 11.''')

setsrc(63, '''**Result: partially reproduced.** Under the criterion's readings 11 to
13 of the 18 values are within tolerance in every combination, partially reproduced throughout.
Rates, mean depth and median depth (0.226 and 0.131), the means of spikes per touch and the
touch-evoked fraction (27.2%, median 22.1% under the first reading) are within tolerance. The
medians of spikes per first and later touch (0.227 and 0.188 against 0.98 and 0.42), the median
whisking rate (11.0 against 13.5), the median latency (4 against 8 ms) and the median minimum
ISI (1.5 against 2.7 ms) are not. The literal cutoff, a variant, gives 9 to 11.''')

setsrc(69, '''**Result: reproduced.** Under reading (a) both rank-sum tests give p
< 0.05 with the C2 median higher in all 16 window readings of the transition cutoff (first
touches p = 1.0e-4 to 0.0043, later touches 2.0e-4 to 0.015; the paper gives 1.4e-5 and
6.32e-6), and in the 16 of the literal variant. Under reading (b) the peak touch rate is 148.1
against 25.0 spikes/s for first touches (p = 1.63e-5) and 51.3 against 5.6 for later touches (p
= 1.07e-5).''')

setsrc(82, '''**Result: reproduced.** The signed-rank test is
significant under both readings of whisking periods (p = 0.024 without touch epochs and 0.014
with them, paper 0.019), and the median of the per-cell differences, the measure the answered
criterion names, is positive under both (+1.88 and +1.79 spikes/s), with 9 and 10 of the 11
cells firing more when whisking. The group medians, shown only for comparison, run the other
way (11.0 and 11.3 spikes/s when whisking against 12.9 outside whisking; Table 1 gives 13.5 and
12.8).''')

setsrc(86, '''**Result: blocked (methods_underspecified).** Under the transition
cutoff, the criterion's, 66.9 to 75.8% of exploration spikes fall in touch windows covering 14.6
to 17.6% of exploration time. All 4 readings with the 100 ms curve put both values in tolerance
(70.6 +- 20.9% and 14.9 +- 1.49%), but only 1 of the 4 with the 200 ms curve does: the other
three cover 16.5 to 17.6% of exploration time. The readings of the curve's range, which the
paper does not give, disagree. The literal cutoff, a variant, gives 38.6 to 64.5% in 8.5 to
13.4% of time.''')

setsrc(88, '''**Result: blocked (methods_underspecified).** The claim depends
on fig3c-touch-spikes-l4c2, which is blocked. Under every one of its 16 readings with the
transition cutoff the time fraction is outside tolerance: 18.8 to 31.7% of spikes in 17.5 to
26.3% of exploration time (paper 8.4 +- 13.3% in 3.5%), with the rank-sum test against L4 C2 at
p < 0.001. The literal cutoff, a variant, gives 1.5 to 7.4% in 1.2 to 2.6%.''')

setsrc(90, '''**Result: blocked (methods_underspecified).** The claim depends on
fig3c-touch-spikes-l4c2, which is blocked. Under the transition cutoff 4 of the 8 window
readings meet the criterion under both latency readings (20.8 to 30.6% of spikes in 15.4 to
22.5% of time across the 8, paper 24.0 +- 18.6% in 19.0%; p against L4 C2 below 0.001), 2 with
the 100 ms curve and 2 with the 200 ms curve. The literal cutoff, a variant, gives 5.1 to 14.1%
in 3.2 to 8.2% of time.''')

setsrc(94, '''**Result: blocked (methods_underspecified).** The claim depends on
fig3c-touch-spikes-l4c2. Under the transition cutoff 74.6 to 81.7% of spikes are touch or phase
coupled in 22.3 to 28.1% of exploration time, and 4 of the 16 readings put both values in
tolerance (75.2 +- 19.0% in 22.0 +- 2.2%), all with the 100 ms curve and the phase window t_w
wide in total; the others cover 24.0 to 28.1% of time. The literal cutoff, a variant, gives
44.3 to 68.1% in 11.7 to 18.4%.''')

setsrc(96, '''**Result: blocked (methods_underspecified).** The claim depends on
fig3d-touch-phase-l4c2. None of the 32 readings with the transition cutoff meets the criterion:
the touch or phase fraction is 40.6 to 60.2% (within 33.0 +- 30.2%), but the time fraction is 27.0
to 42.0% against 16.9 +- 1.69%. One reading of the literal variant meets it (34.3% in 16.0%).''')

setsrc(98, '''**Result: blocked (methods_underspecified).** The claim depends on
fig3d-touch-phase-l4c2. Under the transition cutoff 8 of 32 readings meet the criterion, all
with the 100 ms curve and the phase window t_w wide in total (36.4 to 37.5% in 26.3 to 28.1% of
time, paper 31.5 +- 16.4% in 26.1 +- 2.61%); over all 32 the fraction is 36.4 to 52.7% in 26.3
to 41.0% of time. None of the literal variant does (6.1 to 24.7%).''')

setsrc(100, '''**Result: blocked (methods_underspecified).** The claim depends on
fig3d-touch-phase-l4c2. Under the transition cutoff the phase-only fractions meet the criterion
in 11 of 16 readings (L4 C2 5.1 to 9.3%, L4 outside 20.3 to 32.1%, L5 10.3 to 25.4%); in the 5
that fail the L5 mean is 23.3 to 25.4%, above its tolerance (7.6 +- 14.9%). All 16 of the
literal variant meet it.''')

rep(101, '''fraction of touches detected or (b) percent correct. Within (1a) the claims file does not say
which 10 ms of the 30 ms before touch; both ends are run, the window ending at onset
(`pre_end`, -10 to 0 ms) and the earliest (`pre_start`, -30 to -20 ms). Reading (1b) uses
windows with no touch onset from 60 ms before to 100 ms after them (a standard choice).''',
'''fraction of touches detected or (b) percent correct, both with the threshold that maximises
percent correct on the training half. Within (1a), after the answer to the question, the
criterion lists three samples: (a1) the window ending at onset (`pre_end`, -10 to 0 ms), (a2)
the earliest (`pre_start`, -30 to -20 ms) and (a3) every pre-touch window pooled (`pre_all`, the
21 windows from -30 to -20 ms through -10 to 0 ms). Reading (1b) uses windows with no touch
onset from 60 ms before to 100 ms after them (a standard choice).''')

setsrc(104, '''**Result: blocked (methods_underspecified).** The smallest
population whose mean performance reaches 95% depends on the readings: 11 (fraction detected)
or 13 (percent correct) neurons with non-touch windows from exploration time; 17, 30 and 25 with
percent correct and the pre-touch windows (a1), (a2) and (a3); and 4, 1 and 1 with the fraction
of touches detected and the same windows (the threshold that maximises percent correct detects
nearly every touch). None is within 15 +- 1.5. The added reading (a3) changes the random draws
of the others, which moved the exploration and percent-correct value from 11 to 13, the (a1)
value from 18 to 17 and the (a1) fraction-detected value from 1 to 4; 20 repetitions per size
leave the mean near 95% uncertain by a few neurons.''')

setsrc(106, '''**Result: blocked (methods_underspecified).** The claim depends
on fig4a-touch-detection-c2. With percent correct, 15 outside neurons perform at 0.53 to 0.55
(upper bound 0.56 to 0.60) against 0.90 to 0.97 in C2, and no outside population up to 200
reaches C2's level, so detection is poor. With the fraction of touches detected, 15 outside
neurons detect 0.91 to 0.94 of touches with an upper bound of 1.000, so the bound does not
exclude 95%. The readings disagree.''')

setsrc(107, '''## fig4b-touch-time-precision

> A naive Bayes decoder reading 200 L4 C2 neurons integrated over 10 ms decodes the time elapsed
> since touch with high precision, a minimum uncertainty of 0.55 ms (95% confidence) at 10 ms
> after touch onset.

Multinomial naive Bayes over the 10 ms integrated responses of 200 neurons, 100 bootstrap runs.
Open details from the claims file: (1) the uncertainty, (a) RMS error, (b) half width of the
95% bound of decoded time, (c) 1.96 x RMS; (2) training and test sets, (a) halves of 1000 draws
or (b) independent sets of 1000 draws; (3) the times the decoder chooses among, added after the
answer to the question, (c-all) every 1 ms where a full 10 ms window fits, from -21 ms, or
(c-post) every 1 ms from onset on; (4) the smoothing of zero counts, add-one (alpha = 1), with a
smaller pseudocount (alpha = 0.01) as a variant.''')

setsrc(110, '''**Result: not reproduced.** With add-one smoothing the smallest
uncertainty 5 to 15 ms after onset, at 8 ms after onset, is an RMS error of 1.09 to 1.40 ms, a
half width of the 95% bound of 2.0 ms, or 2.14 to 2.74 ms as 1.96 x RMS, under both splits and
both sets of time classes; none is within 0.55 +- 0.055 ms. The smaller pseudocount, a variant,
gives 1.18 to 1.48 ms RMS and the same 2.0 ms half width. The error falls with population size
(19.9 ms at 10 neurons to 1.55 ms at 200, at 10 ms after onset), as the Figure 4B inset shows.''')

setsrc(111, '''## fig4c-phase-decoding

> Even 1000 L4 neurons give only a rough estimate of whisking phase, a resolution of 24 deg in
> C2 and 33 deg outside C2 at d' = 1 (76% correct discrimination).

Per cell, spike counts in 120 phase bins for every whisk cycle used for phase tuning, as the
answered criterion says: complete cycles with amplitude above 2.5 deg throughout, monotonic
phase, no lick, not within 70 ms after a touch and with the pole in reach. 1000 neurons drawn
with replacement and circularly shifted to uniformly distributed preferred phases (from the
cosine fit; 0 for the cells without phase spikes); a Poisson naive Bayes decision between two
phases, 50 test samples per phase and phase difference, phase differences of 6 to 180 deg in 6
deg steps, 100 runs, median. Open details from the claims file: (1) responses, (a) counts of
held-out cycles or (b) Poisson counts with the cycle-averaged rates; (2) shifts, (a) random or
(b) even; (3) empty bins, add-one smoothing of the counts, or under (1b) a floor rate, here one
spike over all of the cell's cycles and bins (the paper gives no value). The earlier run's
cycles (every cycle peaking above 2.5 deg) and smoothing (one spike spread over the 120 bins)
are shown as a variant.''')

setsrc(114, '''**Result: blocked (methods_underspecified).** No reading gives the
paper's values, and the readings of the empty bins, which the paper does not treat, move the C2
resolution to both sides of 24 deg. With held-out cycle counts and add-one smoothing, neither
group reaches 76% correct in any run. With Poisson rates and add-one smoothing, C2 reaches it
at 84.0 deg (random shifts) or 60.0 deg (even shifts) and outside C2 at 35.7 or 40.7 deg, so C2
is worse than outside. With a floor rate, C2 reaches it at 14.8 or 12.0 deg and outside C2 at
6.0 deg, again better outside. The earlier run's cycles and smoothing, a variant, give 64.5 deg
in C2 and 123.0 deg outside. The phase-tuning cycles are few (median 137 per C2 cell, 0.100
spikes per cycle, 6 of 31 C2 cells with no spike in them), so the decoder depends heavily on how
empty bins are filled.''')

setsrc(118, '''**Result: reproduced.** Under the transition cutoff every reading of
the window, velocity, curvature and touch order gives mean modulation indices within tolerance:
touch order 0.666 to 0.692, velocity 0.703 to 0.735 and curvature 0.664 to 0.698 (paper 0.71 +-
0.25, 0.71 +- 0.27, 0.72 +- 0.23); under the first reading of each detail 0.677, 0.713 and
0.672. The literal cutoff, a variant, gives 0.744 to 0.894, also within tolerance.''')

setsrc(121, '''**Result: blocked (methods_underspecified).** Under reading (a),
correlations of the indices across cells, with the transition cutoff r is 0.618 to 0.788 for
velocity and curvature, 0.706 to 0.788 for order and velocity, and 0.588 to 0.641 for order and
curvature, and the criterion holds in 16 of 64 combinations of the fig5c readings; where it
fails, the velocity and curvature r is below 0.72 or not the largest of the three. Under reading
(b), pooled curves, r is 0.27 to 0.51 for velocity and curvature and the criterion never holds.
The fig5c readings give different outcomes. The literal cutoff, a variant, holds in 8 of 64
under (a).''')

setsrc(133, '''## fig6d-not-refractory

> The low Fano factor after touch cannot be explained by a Poisson process with a 2.3 ms
> refractory period and rates matched to each neuron.

Per cell, spike trains simulated at 0.1 ms resolution as a Poisson process with an absolute
refractory period of 2.3 ms, one train per real touch; the FF in the same 10 ms windows. After
the answer to the question, the model's average touch response is matched to the data: its
rate is the free rate of Berry and Meister (1998), lambda(t) = r(t) / (1 - integral of r over
[t - 2.3 ms, t)), with r the cell's touch PSTH in 1 ms bins from the same touches, starting 10
ms before onset so that the integral is defined in the first window. The PSTH used directly as
the rate, the earlier run's model, is shown as a variant. Open details from the claims file: (1)
touches pooled (> 250 ms touches) or per group; (2) the comparison, (a) the population mean
data FF below the model's at the window of the data minimum by more than the sum of the two
s.e.m., or (b) the per-cell data FF below the model's in more than half the cells, sign test
p < 0.05.''')

setsrc(136, '''**Result: blocked (methods_underspecified).** The compensated model
matches the data's mean count (model over data 1.001 to 1.034 across the windows; 0.80 to 0.89
without compensation) and its FF at the data minimum is 0.71 to 0.79. Under reading (2a) the
population mean data FF (0.75 to 0.82) is not below the model's by more than the sum of the two
s.e.m. in any of the 6 touch readings. Under reading (2b) the per-cell data FF is below the
model's in 4 of the 6 (61 of 89 units, 61 of 100, 59 of 99, and 22 of 31 pooled cells counted
from onsets, sign test p = 0.0003 to 0.035), but not with groups of N points counted from
offsets (52 of 91, p = 0.10) or pooled touches counted from offsets (17 of 31, p = 0.36). The
readings disagree. The uncompensated variant, whose FF is higher, gives (2b) in all 6.''')
json.dump(nb, open(P, 'w'), indent=1, ensure_ascii=False)
open(P, 'a').write('\n')
PYEOF
python $TMPDIR/edit4.py && echo ok
```

```
ok
```

**Agent calls Bash**

```bash
cd entries/000013-hires-2015; python - <<'EOF'
import json
P='reproduce_hires_2015.ipynb'
nb=json.load(open(P)); C=nb['cells']
def rep(i,a,b):
    s=''.join(C[i]['source']); assert a in s,(i,a); C[i]['source']=s.replace(a,b).splitlines(keepends=True)
rep(104,"value from 18 to 17 and the (a1) fraction-detected value from 1 to 4; 20","value from 18 to 17 and the (a1) fraction-detected value to 4 (1 or 2 before); 20")
rep(121,"""fails, the velocity and curvature r is below 0.72 or not the largest of the three. Under reading""","""fails, at least one r is outside its tolerance or velocity and curvature is not the largest. Under reading""")
rep(94,"the others cover 24.0 to 28.1% of time","the others cover 24.9 to 28.1% of time")
json.dump(nb,open(P,'w'),indent=1,ensure_ascii=False); open(P,'a').write('\n')
EOF
python -c "
import json
nb=json.load(open('reproduce_hires_2015.ipynb'))
print(''.join(nb['cells'][151]['source']))" | sed -n 1,10p
```

```
## Summary

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

| Claim | Outcome |
|---|---|
| recordings-counts | reproduced |
| recordings-mice | not reproduced |
| behavior-performance | reproduced |
```

**Agent**

Now the summary cell.

**Agent calls Bash**

```bash
cd entries/000013-hires-2015; python - <<'EOF'
import json
P='reproduce_hires_2015.ipynb'
nb=json.load(open(P)); C=nb['cells']
s=''.join(C[151]['source'])
pairs=[
("| table1-l4-c2, table1-l4-outside, table1-l5 | blocked: methods underspecified |",
 "| table1-l4-c2 | reproduced |\n| table1-l4-outside | blocked: methods underspecified |\n| table1-l5 | partially reproduced |"),
("| whisking-rate-l5-increase | partially reproduced |","| whisking-rate-l5-increase | reproduced |"),
("| fig4c-phase-decoding | not reproduced |","| fig4c-phase-decoding | blocked: methods underspecified |"),
("""Of the 45 claims, 20 are reproduced, 5 partially reproduced, 5 not reproduced and 15 blocked as
methods underspecified, most of them on one question: where the search for the touch-window
cutoff starts.""",
"""Of the 45 claims, 22 are reproduced, 5 partially reproduced, 4 not reproduced and 14 blocked as
methods underspecified. The answers to the seven questions of the first run changed four
outcomes: table1-l4-c2 (blocked to reproduced) and table1-l5 (blocked to partially reproduced)
once the touch-window cutoff is the transition, whisking-rate-l5-increase (partially to
reproduced) once the increase is the median of the paired differences, and fig4c-phase-decoding
(not reproduced to blocked) once the empty-bin readings move its C2 resolution to both sides of
the paper's. The Figure 3 claims stay blocked, now on the range of the cutoff curve (100 or 200
ms), which the paper does not give."""),
("""- Details the claims file leaves open without readings were run under each reading this
  notebook could see, and asked about in `questions/000013.yaml`: where the cutoff search
  starts, the longest window of the cutoff curve, the pre-touch window of the touch detector,
  the decoder's time classes, the phase decoder's response and smoothing, and the rate of the
  refractory model. Standard choices that are not expected to change a result: the
  polynomial's conditioning, the guard around touches for non-touch windows, the random seeds.""",
"""- The details asked about in `questions/000013.yaml` (where the cutoff search starts, the
  longest window of the cutoff curve, the pre-touch window of the touch detector, the decoder's
  time classes and smoothing, the phase decoder's cycles and empty bins, the rate of the
  refractory model, the measure of the L5 whisking increase) are now set or listed as readings
  by the claims file and run as it says. The values chosen here where the answers list a
  reading without a number: the floor rate of the phase decoder (one spike over all of a cell's
  cycles and bins) and the smaller pseudocount of the time decoder (0.01). Whisking periods for
  Table 1 are read as the claims file defines them, outside touch epochs. Standard choices that
  are not expected to change a result: the polynomial's conditioning, the guard around touches
  for non-touch windows, the random seeds."""),
]
for a,b in pairs:
    assert a in s, a[:50]; s=s.replace(a,b)
C[151]['source']=s.rstrip('\n').splitlines(keepends=True)
json.dump(nb,open(P,'w'),indent=1,ensure_ascii=False); open(P,'a').write('\n')
EOF
python -c "
import json
nb=json.load(open('reproduce_hires_2015.ipynb'))
print(''.join(nb['cells'][151]['source']))" | sed -n 40,100p; grep -c "—\|rather" reproduce_hires_2015.ipynb hires.py
```

```
| fig6d-not-refractory | blocked: methods underspecified |
| fig6e-sample-epoch-ff, fig6e-random-38ms-ff, fig6e-touch-38ms-ff, fig6e-touch-10ms-ff, fig6e-similar-touch-ff | reproduced |
| whisk-cycle-spikes | reproduced |

Of the 45 claims, 22 are reproduced, 5 partially reproduced, 4 not reproduced and 14 blocked as
methods underspecified. The answers to the seven questions of the first run changed four
outcomes: table1-l4-c2 (blocked to reproduced) and table1-l5 (blocked to partially reproduced)
once the touch-window cutoff is the transition, whisking-rate-l5-increase (partially to
reproduced) once the increase is the median of the paired differences, and fig4c-phase-decoding
(not reproduced to blocked) once the empty-bin readings move its C2 resolution to both sides of
the paper's. The Figure 3 claims stay blocked, now on the range of the cutoff curve (100 or 200
ms), which the paper does not give.

How the analysis differs from the paper's.

- The paper's analysis code is not public (the claims file records that the repository it
  links holds only the contact detection). Every procedure is rebuilt from the claims file.
- Touch onsets and offsets, the Hilbert amplitude and phase, and the lick and pole series are
  the dandiset's own. The stored amplitude and phase match a 6 to 60 Hz fourth-order
  Butterworth band-pass and Hilbert transform of `theta_at_base`.
[... 38 more lines not kept]
```

**Agent**

Now the README.

**Agent calls Bash**

```bash
cd entries/000013-hires-2015; python - <<'EOF'
P='README.md'
s=open(P).read()
pairs=[
("""| Touch responses weaker outside C2; L5 rates higher; phase modulation L4 vs L5 and inside vs outside | Reproduced |""",
"""| Table 1 for L4 C2; the L5 rate increase with whisking | Reproduced |
| Touch responses weaker outside C2; L5 rates higher; phase modulation L4 vs L5 and inside vs outside | Reproduced |"""),
("""| Whisking bouts; touches and reaction time; example cell's touch window; rate change with whisking (L4, L5) | Partially reproduced |
| Mice and lines; whisking rates in the text; how many cells have a latency; time and phase decoding (Figure 4B, 4C) | Not reproduced |
| Table 1; touch and phase coupled spikes (Figure 3C, 3D); touch detection (Figure 4A); Figure 5 correlations; refractory model (Figure 6D); Figure 6B example | Blocked: methods underspecified |""",
"""| Whisking bouts; touches and reaction time; example cell's touch window; rate change with whisking in L4; Table 1 for L5 | Partially reproduced |
| Mice and lines; whisking rates in the text; how many cells have a latency; time decoding (Figure 4B) | Not reproduced |
| Table 1 for L4 outside C2; touch and phase coupled spikes (Figure 3C, 3D); touch detection (Figure 4A); phase decoding (Figure 4C); Figure 5 correlations; refractory model (Figure 6D); Figure 6B example | Blocked: methods underspecified |"""),
("""Most of the blocked claims turn on one question asked in
[`questions/000013.yaml`](../../questions/000013.yaml): where the search for the touch-window
cutoff starts. The files""",
"""The first run asked seven questions in
[`questions/000013.yaml`](../../questions/000013.yaml), and a reader answered them from the
paper. With the touch-window cutoff set to the transition where the curve levels off, Table 1
for L4 C2 is reproduced and for L5 partially; the Figure 3 claims stay blocked on the range of
the cutoff curve (100 or 200 ms), which the paper does not give. The files"""),
]
for a,b in pairs:
    assert a in s, a[:50]; s=s.replace(a,b)
open(P,'w').write(s)
EOF
cat README.md | sed -n 8,30p
```

```
| Claims | Outcome |
|---|---|
| Recording counts, behavioural performance, sample epoch | Reproduced |
| The Figure 1 example cell: rates, sample-epoch Fano factor, spikes per touch, phase modulation | Reproduced (cell 23) |
| Table 1 for L4 C2; the L5 rate increase with whisking | Reproduced |
| Touch responses weaker outside C2; L5 rates higher; phase modulation L4 vs L5 and inside vs outside | Reproduced |
| Modulation indices of Figure 5C; touch clusters; Fano factor near the binomial limit | Reproduced |
| Fano factors of Figure 6E (five conditions); spikes per whisk cycle | Reproduced |
| Whisking bouts; touches and reaction time; example cell's touch window; rate change with whisking in L4; Table 1 for L5 | Partially reproduced |
| Mice and lines; whisking rates in the text; how many cells have a latency; time decoding (Figure 4B) | Not reproduced |
| Table 1 for L4 outside C2; touch and phase coupled spikes (Figure 3C, 3D); touch detection (Figure 4A); phase decoding (Figure 4C); Figure 5 correlations; refractory model (Figure 6D); Figure 6B example | Blocked: methods underspecified |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The first run asked seven questions in
[`questions/000013.yaml`](../../questions/000013.yaml), and a reader answered them from the
paper. With the touch-window cutoff set to the transition where the curve levels off, Table 1
for L4 C2 is reproduced and for L5 partially; the Figure 3 claims stay blocked on the range of
the cutoff curve (100 or 200 ms), which the paper does not give. The files fall in batches that were converted differently: in 36 of them the
[... 2 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/000013-hires-2015; python - <<'EOF'
P='README.md'
s=open(P).read()
s=s.replace("which the paper does not give. The files fall in batches that were converted differently: in 36 of them the\nspike train's","which the paper does not give.\n\nThe files fall in batches that were converted differently: in 36 of them the spike train's")
open(P,'w').write(s)
EOF
sed -n 22,35p README.md; grep -n "schema\|outcome:\|proposed\|verifications" ../../schemas/*attempt* 2>/dev/null | head; ls ../../schemas
```

```
reasoning and the differences from the paper's method.

The first run asked seven questions in
[`questions/000013.yaml`](../../questions/000013.yaml), and a reader answered them from the
paper. With the touch-window cutoff set to the transition where the curve levels off, Table 1
for L4 C2 is reproduced and for L5 partially; the Figure 3 claims stay blocked on the range of
the cutoff curve (100 or 200 ms), which the paper does not give.

The files fall in batches that were converted differently: in 36 of them the spike train's timestamps run 10 ms ahead of the voltage they were detected from, and in 38 the
stored `theta_filt` is not the band-passed angle and the voltage's unit conversion is off by
1000.
The attempt record, with the reasons and the differences from the paper's method, is
[`attempts/000013-hires-2015-01.yaml`](../../attempts/000013-hires-2015-01.yaml).

2:  "$schema": "https://json-schema.org/draft/2020-12/schema",
8:    "schema_version",
17:    "schema_version": {
248:          "proposed": {
303:    "verifications": {
attempt.schema.json
[... 2 more lines not kept]
```

**Agent**

Next, the attempt record. I'll check the schema's outcome fields first.

**Agent calls Bash**

```bash
cd  python -c "
import json
s=json.load(open('schemas/attempt.schema.json'))
o=s['properties']['outcomes']['items']
print(list(o['properties'].keys()))
print(json.dumps(o['properties'].get('measured'),indent=0)[:600])
"
```

```
['claim', 'outcome', 'blocked_by', 'notes', 'notebook', 'output', 'measured', 'deviations', 'proposed']
{
"description": "The values obtained, for claims with expected values: one number, or one per expected value, in the same order.",
"oneOf": [
{
"type": "number"
},
{
"type": "array",
"minItems": 1,
"items": {
"type": "number"
}
}
]
}
```

**Agent calls Bash**

```bash
cd  cat > $TMPDIR/att.py <<'PYEOF'
import re
P = 'attempts/000013-hires-2015-01.yaml'
s = open(P).read()
NEW = {}
NEW['example-cell-touch-window'] = '''- claim: example-cell-touch-window
  outcome: partially_reproduced
  notebook: reproduce_hires_2015.ipynb
  output: claim:example-cell-touch-window
  measured:
  - 84.6
  - 8
  - 37
  - 19.6
  notes: Measured values are for the uniform shuffle, the onset before, 100 ms and the transition
    cutoff. For cell 23 the window runs from 8 ms to 36 to 38 ms under all 8 readings of the
    transition cutoff. The spike fraction is 78.4 to 79.1% with the closest onset on either side
    and 83.6 to 84.6% with the onset before; the time fraction is 19.0 to 20.2% under every
    reading, against 15.3 +- 1.53%. The answer on where the cutoff search starts changed nothing
    here, as the transition and the literal cutoff give this cell the same window under every
    reading; the 100 and 200 ms curves, now listed by the criterion, were both run before and
    give the same outcome.
'''
NEW['text-spikes-per-touch'] = '''- claim: text-spikes-per-touch
  outcome: reproduced
  notebook: reproduce_hires_2015.ipynb
  output: claim:text-spikes-per-touch
  measured:
  - 1.505
  - 0.305
  - 8
  notes: Under reading (a), the example cell, 1.474 to 1.505 spikes per first touch, 0.302 to
    0.307 per later touch and an 8 ms latency under all 8 window readings of the transition
    cutoff (9 ms from the all-touch PCTH, also within tolerance). Readings (b) and (c) do not
    match (means 1.16 to 1.28 and 0.62 to 0.69, medians 0.70 to 0.73 and 0.31 to 0.33). The answer
    on the cutoff leaves the outcome as it was, since the example cell's window is the same under
    both starts; it moves the population values of (b) and (c), which were 0.53 to 1.28 and 0.28
    to 0.68 over both starts.
'''
NEW['table1-l4-c2'] = '''- claim: table1-l4-c2
  outcome: reproduced
  notebook: reproduce_hires_2015.ipynb
  output: claim:table1-l4-c2
  measured:
  - 1.24
  - 0.704
  - 0.66
  - 0.314
  - 73.8
  - 80.0
  - 80.9
  - 82.7
  - 0.727
  - 1.0
  - 1.303
  - 0.315
  - 2.402
  - 0.86
  - 7.29
  - 7.0
  - 2.768
  - 2.3
  notes: Measured values are for the first reading of each open detail (uniform shuffle, onset
    before, 100 ms, transition cutoff, phase window +-t_w, latency from first touches, whisking
    outside touch epochs). Under the transition cutoff, the criterion's after the answer, 15 of
    18 values are within tolerance in all 64 combinations of the other readings, at the threshold
    for reproduced. The three outside are medians, spikes per first touch (0.70 to 0.73 against
    0.87), modulation depth (1.0 against 0.70) and whisking rate (0.86 against 0.33); 14 of the 25
    cells with a phase fit have depth 1. Whisking periods are read as the claims file defines
    them, outside touch epochs ("For other epochs ... whisking epochs have amplitude >2.5 deg",
    and the answer about fig4c-phase-decoding quotes the Methods to the same effect); with touch
    epochs in, a variant, the mean whisking rate (3.98) also falls outside and the count is 14.
    What the answer changed, the earlier run was blocked because the literal cutoff gave 9 to 14
    values and the transition one 14 or 15; the literal cutoff is now a variant only. The 100 and
    200 ms curves give 15 alike.
'''
NEW['table1-l4-outside'] = '''- claim: table1-l4-outside
  outcome: blocked
  blocked_by: methods_underspecified
  notebook: reproduce_hires_2015.ipynb
  output: claim:table1-l4-outside
  notes: Under the transition cutoff, the criterion's after the answer, 7 to 9 of 17 values are
    within tolerance, 52 of the 64 combinations of readings below the threshold of 9 (not
    reproduced) and 12 at it (partially); the readings of the touch window decide which. The
    medians of spikes per touch are never 0; the means of spikes per touch (0.31 and 0.15 under
    the first reading, against 0.08 and 0.02), the touch-evoked fraction (26.2%, median 23.8%,
    against 9.2% and 3.6%) and the latency mean (8.1 ms against 18.5) are outside tolerance.
    Rates, mean depth and minimum ISI match. What the answer changed, the literal cutoff, which
    gave 10 to 11 (partially), is now a variant only; the outcome stays blocked because the
    transition cutoff's own readings straddle the threshold.
'''
NEW['table1-l5'] = '''- claim: table1-l5
  outcome: partially_reproduced
  notebook: reproduce_hires_2015.ipynb
  output: claim:table1-l5
  measured:
  - 2.046
  - 0.227
  - 1.313
  - 0.188
  - 27.2
  - 22.1
  - 45.3
  - 40.0
  - 0.226
  - 0.131
  - 12.04
  - 12.9
  - 18.49
  - 10.96
  - 4.9
  - 4.0
  - 2.627
  - 1.5
  notes: Measured values are for the first reading of each open detail, as for table1-l4-c2.
    Under the transition cutoff 11 to 13 of 18 values are within tolerance in every combination of
    readings, partially reproduced throughout. Rates, depth (mean 0.226, median 0.131), the means
    of spikes per touch and the touch-evoked fraction match; the medians of spikes per first and
    later touch (0.23 and 0.19 against 0.98 and 0.42), the median whisking rate (11.0 against
    13.5), the median latency (4 against 8 ms) and the median minimum ISI (1.5 against 2.7 ms) do
    not. What the answer changed, the earlier run was blocked because the literal cutoff gave 9 to
    11, 8 combinations not reproduced; with the literal cutoff a variant only, the outcome is
    partially reproduced.
'''
NEW['l4-outside-weaker-touch'] = '''- claim: l4-outside-weaker-touch
  outcome: reproduced
  notebook: reproduce_hires_2015.ipynb
  output: claim:l4-outside-weaker-touch
  notes: Reading (a), spikes per touch, gives p < 0.05 for first and later touches with the C2
    median higher in all 16 window readings of the transition cutoff (p = 1.0e-4 to 0.0043 and
    2.0e-4 to 0.015), and in the 16 of the literal variant. Reading (b), the peak touch rate, gives
    148.1 against 25.0 spikes/s (p = 1.63e-5) and 51.3 against 5.6 (p = 1.07e-5). The answer on
    the cutoff leaves the outcome as it was, as both starts gave it.
'''
NEW['whisking-rate-l5-increase'] = '''- claim: whisking-rate-l5-increase
  outcome: reproduced
  notebook: reproduce_hires_2015.ipynb
  output: claim:whisking-rate-l5-increase
  notes: Signed-rank p = 0.024 without touch epochs and 0.014 with them, 9 and 10 of 11 cells
    higher when whisking, median of the per-cell differences +1.88 and +1.79 spikes/s, positive
    under both readings. What the answer changed, the criterion now names the median of the
    per-cell differences as the measure of the increase; the earlier run read "the median
    whisking rate higher" as the group medians, which run the other way (11.0 and 11.3 against
    12.9 spikes/s), and recorded partially reproduced.
'''
NEW['fig3c-touch-spikes-l4c2'] = '''- claim: fig3c-touch-spikes-l4c2
  outcome: blocked
  blocked_by: methods_underspecified
  notebook: reproduce_hires_2015.ipynb
  output: claim:fig3c-touch-spikes-l4c2
  notes: Under the transition cutoff, the criterion's after the answer, 66.9 to 75.8% of spikes
    in 14.6 to 17.6% of exploration time. All 4 readings with the 100 ms curve put both values in
    tolerance, but only 1 of 4 with the 200 ms curve (the other three cover 16.5 to 17.6% of
    time), so the readings of the curve's range disagree. What the answers changed, the start of
    the search is now fixed, and the literal cutoff (38.6 to 64.5% in 8.5 to 13.4%, none within
    tolerance) is a variant only; the range of the curve, which the paper does not give, is now
    the criterion's open detail (4), and it alone keeps the claim blocked.
'''
NEW['fig3c-touch-spikes-outside'] = '''- claim: fig3c-touch-spikes-outside
  outcome: blocked
  blocked_by: methods_underspecified
  notebook: reproduce_hires_2015.ipynb
  output: claim:fig3c-touch-spikes-outside
  notes: Blocked as it depends on fig3c-touch-spikes-l4c2. Every one of its 16 readings with the
    transition cutoff is outside tolerance on the time fraction (18.8 to 31.7% of spikes in 17.5 to
    26.3% of time, against 8.4 +- 13.3% in 3.5%), with the rank-sum test against L4 C2 at p < 0.001.
    With the answer the literal cutoff (1.5 to 7.4% in 1.2 to 2.6%) is a variant only; the values
    that decide are the transition ones, all outside tolerance.
'''
NEW['fig3c-touch-spikes-l5'] = '''- claim: fig3c-touch-spikes-l5
  outcome: blocked
  blocked_by: methods_underspecified
  notebook: reproduce_hires_2015.ipynb
  output: claim:fig3c-touch-spikes-l5
  notes: Depends on fig3c-touch-spikes-l4c2. Under the transition cutoff 4 of the 8 window
    readings meet the criterion under both latency readings (2 with the 100 ms curve, 2 with the
    200 ms one; 20.8 to 30.6% in 15.4 to 22.5% of time over the 8). With the answer the literal
    cutoff (5.1 to 14.1% in 3.2 to 8.2%, none) is a variant only; the transition cutoff's readings
    still disagree.
'''
NEW['fig3d-touch-phase-l4c2'] = '''- claim: fig3d-touch-phase-l4c2
  outcome: blocked
  blocked_by: methods_underspecified
  notebook: reproduce_hires_2015.ipynb
  output: claim:fig3d-touch-phase-l4c2
  notes: Depends on fig3c-touch-spikes-l4c2. Under the transition cutoff, which the answer makes
    the rule for t_w too, 74.6 to 81.7% in 22.3 to 28.1% of time, and 4 of 16 readings meet both
    tolerances, all with the 100 ms curve and the window t_w wide in total. The literal cutoff
    (44.3 to 68.1% in 11.7 to 18.4%, none) is a variant only.
'''
NEW['fig3d-touch-phase-outside'] = '''- claim: fig3d-touch-phase-outside
  outcome: blocked
  blocked_by: methods_underspecified
  notebook: reproduce_hires_2015.ipynb
  output: claim:fig3d-touch-phase-outside
  notes: Depends on fig3d-touch-phase-l4c2. None of the 32 readings with the transition cutoff
    meets the criterion; the fraction is 40.6 to 60.2% (within tolerance) but the time fraction 27.0
    to 42.0% against 16.9 +- 1.69%. The one reading that met it in the earlier run used the literal
    cutoff, a variant only after the answer.
'''
NEW['fig3d-touch-phase-l5'] = '''- claim: fig3d-touch-phase-l5
  outcome: blocked
  blocked_by: methods_underspecified
  notebook: reproduce_hires_2015.ipynb
  output: claim:fig3d-touch-phase-l5
  notes: Depends on fig3d-touch-phase-l4c2. 8 of the 32 readings with the transition cutoff meet
    the criterion, all with the 100 ms curve and the total-width phase window (36.4 to 37.5% in
    26.3 to 28.1% of time); over the 32 the time fraction is 26.3 to 41.0%. The answer drops the
    literal cutoff to a variant (none of its readings met it), which does not change the outcome.
'''
NEW['fig3d-phase-only'] = '''- claim: fig3d-phase-only
  outcome: blocked
  blocked_by: methods_underspecified
  notebook: reproduce_hires_2015.ipynb
  output: claim:fig3d-phase-only
  notes: Depends on fig3d-touch-phase-l4c2. Under the transition cutoff 11 of 16 readings meet the
    criterion (L4 C2 5.1 to 9.3%, outside 20.3 to 32.1%, L5 10.3 to 25.4%); the 5 that fail have an
    L5 mean of 23.3 to 25.4%. All 16 of the literal variant meet it; with the answer they no longer
    count.
'''
NEW['fig4a-touch-detection-c2'] = '''- claim: fig4a-touch-detection-c2
  outcome: blocked
  blocked_by: methods_underspecified
  notebook: reproduce_hires_2015.ipynb
  output: claim:fig4a-touch-detection-c2
  notes: The population reaching 95% is 11 (fraction detected) or 13 (percent correct) neurons
    with exploration non-touch windows; 17, 30 and 25 with percent correct and the pre-touch
    windows (a1), (a2) and (a3); 4, 1 and 1 with the fraction detected and the same windows. None
    is within 15 +- 1.5. What the answer changed, it adds reading (a3), all pre-touch windows,
    and keeps the threshold that maximises percent correct; the readings still disagree and none
    matches. Adding (a3) changed the random draws of the other readings (20 repetitions per
    population size), moving three of the earlier values by 1 to 3 neurons.
  deviations:
  - Reading (1b) leaves out windows within 60 ms before or 100 ms after a touch onset, a standard
    choice.
'''
NEW['fig4a-touch-detection-outside'] = '''- claim: fig4a-touch-detection-outside
  outcome: blocked
  blocked_by: methods_underspecified
  notebook: reproduce_hires_2015.ipynb
  output: claim:fig4a-touch-detection-outside
  notes: Depends on fig4a-touch-detection-c2. With percent correct 15 outside neurons reach 0.53 to
    0.55 (upper bound 0.56 to 0.60) against 0.90 to 0.97 in C2, poor; with the fraction of touches
    detected they reach 0.91 to 0.94 with an upper bound of 1.000, so the bound does not exclude
    95%. The added reading (a3) agrees with the other pre-touch readings, and the outcome is as
    before.
'''
NEW['fig4b-touch-time-precision'] = '''- claim: fig4b-touch-time-precision
  outcome: not_reproduced
  notebook: reproduce_hires_2015.ipynb
  output: claim:fig4b-touch-time-precision
  measured: 1.396
  notes: With add-one smoothing the smallest uncertainty 5 to 15 ms after onset, at 8 ms, is an
    RMS error of 1.09 to 1.40 ms, a 95% half width of 2.0 ms or 1.96 x RMS of 2.14 to 2.74 ms,
    under both splits and both sets of time classes (c-all, from -21 ms, and c-post, from 0 ms);
    none is within 0.55 +- 0.055 ms. The smaller pseudocount (0.01), a variant, gives 1.18 to 1.48
    ms RMS. The error falls with population size (19.9 ms at 10 neurons, 1.55 ms at 200). What the
    answer changed, the time classes and the smoothing are now readings of the criterion; both
    sets of classes were run before, and the outcome is as before.
  deviations:
  - The smaller pseudocount of the variant, 0.01, is a value of our choosing; the criterion gives
    none.
'''
NEW['fig4c-phase-decoding'] = '''- claim: fig4c-phase-decoding
  outcome: blocked
  blocked_by: methods_underspecified
  notebook: reproduce_hires_2015.ipynb
  output: claim:fig4c-phase-decoding
  notes: On the phase-tuning cycles (median 137 per C2 cell, 0.100 spikes per cycle, 6 of 31 C2
    cells with none), held-out cycle counts with add-one smoothing never reach 76% correct in
    either group. Poisson rates with add-one smoothing reach it at 84.0 or 60.0 deg in C2 (random
    or even shifts) and 35.7 or 40.7 deg outside; with a floor rate at 14.8 or 12.0 deg in C2 and
    6.0 deg outside. The C2 value is never within 24 +- 2.4 deg and C2 is never better than
    outside, but the empty-bin readings put C2 on both sides of the paper's value, so the
    criterion's fallback applies. What the answer changed, the decoder now uses the cycles of
    phase tuning in place of every cycle peaking above 2.5 deg, and empty bins follow the two
    listed readings; the earlier cycles and smoothing (64.5 deg in C2, 123.0 outside, a variant
    here) gave values far above the paper's under every reading, and the earlier run recorded not
    reproduced.
  deviations:
  - The floor rate, one spike over all of a cell's training cycles and bins, is a value of our
    choosing, as the paper gives none. Cells without a phase fit take preferred phase 0. Tests
    use 50 samples per phase and phase differences in 6 deg steps.
'''
NEW['fig5c-modulation-index'] = '''- claim: fig5c-modulation-index
  outcome: reproduced
  notebook: reproduce_hires_2015.ipynb
  output: claim:fig5c-modulation-index
  measured:
  - 0.677
  - 0.713
  - 0.672
  notes: Measured values are for the uniform shuffle, onset before, 100 ms, transition cutoff,
    order by ranks, velocity at onset and curvature over the touch. Under every reading with the
    transition cutoff the means are within tolerance, order 0.666 to 0.692, velocity 0.703 to
    0.735 and curvature 0.664 to 0.698. The answer on the cutoff leaves the outcome as it was; the
    earlier measured values (0.853, 0.857, 0.827) came from the literal cutoff, now a variant
    (0.744 to 0.894, also within tolerance).
'''
NEW['fig5-modulation-correlations'] = '''- claim: fig5-modulation-correlations
  outcome: blocked
  blocked_by: methods_underspecified
  notebook: reproduce_hires_2015.ipynb
  output: claim:fig5-modulation-correlations
  notes: Under reading (a), with the transition cutoff, r is 0.618 to 0.788 (velocity,
    curvature), 0.706 to 0.788 (order, velocity) and 0.588 to 0.641 (order, curvature), and the
    criterion holds in 16 of 64 combinations of the fig5c readings; under reading (b) it never
    holds (r 0.27 to 0.51 for velocity and curvature). With the answer the literal cutoff (8 of 64
    under (a)) is a variant only; the fig5c readings still give different outcomes.
'''
NEW['fig6d-not-refractory'] = '''- claim: fig6d-not-refractory
  outcome: blocked
  blocked_by: methods_underspecified
  notebook: reproduce_hires_2015.ipynb
  output: claim:fig6d-not-refractory
  notes: With the rate compensated as the answer says (the free rate of Berry and Meister), the
    model's mean count is 1.001 to 1.034 of the data's, and its FF at the data minimum 0.71 to
    0.79. Under reading (2a) the data FF (0.75 to 0.82) is never below the model's by more than the
    sum of the s.e.m.; under (2b) it is below in 4 of 6 touch readings (61 of 89, 61 of 100, 59 of
    99 units and 22 of 31 pooled cells counted from onsets, p = 0.0003 to 0.035) but not with
    groups of N points from offsets (52 of 91, p = 0.10) or pooled touches from offsets (17 of 31,
    p = 0.36). What the answer changed, the uncompensated model, now a variant, has a mean count
    0.80 to 0.89 of the data's and a higher FF, and gives (2b) in all 6 readings; compensation
    lowers the model's FF and removes two of them. The outcome is blocked as before.
  deviations:
  - The PSTH used for the free rate starts 10 ms before onset so that the integral over the
    preceding 2.3 ms is defined at the first window.
'''
blocks = re.split(r'(?m)^(?=- claim: )', s)
out = []
seen = set()
for b in blocks:
    m = re.match(r'- claim: (\S+)\n', b)
    if m and m.group(1) in NEW:
        cid = m.group(1)
        # keep a trailing "findings:" section if the block ends the outcomes list
        tail = ''
        k = b.find('\nfindings:')
        if k >= 0:
            tail = b[k + 1:]
        out.append(NEW[cid] + tail)
        seen.add(cid)
    else:
        out.append(b)
assert seen == set(NEW), set(NEW) - seen
open(P, 'w').write(''.join(out))
PYEOF
python $TMPDIR/att.py && git diff --stat attempts/ && python -c "import yaml;d=yaml.safe_load(open('attempts/000013-hires-2015-01.yaml'));print(len(d['outcomes']), len(d['findings']))"
```

```
attempts/000013-hires-2015-01.yaml | 283 +++++++++++++++++++++++++------------
 1 file changed, 192 insertions(+), 91 deletions(-)
45 9
```

**Agent**

The record parses. Next I'll check it for ": " inside plain scalars, em dashes and the word "rather".

**Agent calls Bash**

```bash
cd  grep -nE "^\s{4,}.*: |^  (notes|statement): .*: " attempts/000013-hires-2015-01.yaml | head; grep -nE "—|rather" attempts/000013-hires-2015-01.yaml entries/000013-hires-2015/README.md | head
```

```
14:    name: CatalystNeuro
16:    harness: Claude Code (GitHub Actions)
17:    model: claude-opus-5-5
18:    protocol: pilot-10
20:    platform: GitHub Actions
21:    url: https://github.com/catalystneuro/reproduction-registry/actions/runs/39600960457
```

**Agent**

Clean. Now lock, check and run the entry.

**Agent calls Bash**

```bash
cd  python tools/entry.py lock entries/000013-hires-2015 2>&1 | tail -3; git diff --stat entries/000013-hires-2015/requirements.lock.txt; python tools/entry.py all entries/000013-hires-2015 2>&1 | tail -4
```

```
wrote entries/000013-hires-2015/requirements.lock.txt
Installed kernelspec registry-000013-hires-2015 in executed/000013-hires-2015/.venv/share/jupyter/kernels/registry-000013-hires-2015
0 error(s)
pass  reproduce_hires_2015.ipynb  (531 s)
```

**Agent**

The run passes. Now I'll confirm the executed numbers still match the conclusions.

**Agent calls Bash**

```bash
cd  python $TMPDIR/out.py 58 62 81 103 110 113 117 135 2>/dev/null | grep -E "criterion's readings|first reading|positive|^pre|^explore|phase tuning \||compensated:|  compensated" ; python $TMPDIR/out.py 152
```

```
under the criterion's readings (cross, whisking outside touch epochs): values within tolerance 15 to 15 over 64 combinations; verdicts {'reproduced': 64}
values under the first reading of each open detail (measured, expected, tolerance, within):
under the criterion's readings (cross, whisking outside touch epochs): values within tolerance 11 to 13 over 64 combinations; verdicts {'partially': 64}
values under the first reading of each open detail (measured, expected, tolerance, within):
whisking with touch epochs False: p < 0.05 True, median of the per-cell differences positive True
whisking with touch epochs True: p < 0.05 True, median of the per-cell differences positive True
pre_end    detected            4
pre_start  detected            1
pre_all    detected            1
explore    detected           11
phase tuning | cycles/add_one/even: C2 nan deg (24 +- 2.4: False), outside nan deg (33 +- 3.3: False), C2 better: False
phase tuning | cycles/add_one/random: C2 nan deg (24 +- 2.4: False), outside nan deg (33 +- 3.3: False), C2 better: False
phase tuning | poisson/add_one/even: C2 60.0 deg (24 +- 2.4: False), outside 40.7 deg (33 +- 3.3: False), C2 better: False
phase tuning | poisson/add_one/random: C2 84.0 deg (24 +- 2.4: False), outside 35.7 deg (33 +- 3.3: True), C2 better: False
phase tuning | poisson/floor/even: C2 12.0 deg (24 +- 2.4: False), outside 6.0 deg (33 +- 3.3: False), C2 better: False
phase tuning | poisson/floor/random: C2 14.8 deg (24 +- 2.4: False), outside 6.0 deg (33 +- 3.3: False), C2 better: False
first reading of each open detail (uniform, before, 100 ms, transition cutoff; ranks, onset, whole touch): {'order': 0.677, 'velocity': 0.713, 'curvature': 0.672}
  compensated   offset   group      5     94             3   0.7466    0.7445   0.0601 False           61  89  0.0003  True
  compensated   offset   group      N     94             4   0.7530    0.7133   0.0588 False           52  91  0.1041 False
  compensated   offset  pooled      -   
[... 7 more lines not kept]
```

**Agent**

Identical to the earlier run. Building the handover.

**Agent calls Bash**

```bash
cd  python tools/entry.py handover entries/000013-hires-2015 2>&1 | tail -5; ls executed/000013-hires-2015/handover; git status --short | grep -v "^??"
```

```
wrote executed/000013-hires-2015/handover
10.7554-elife.06619.yaml
hires.py
reproduce_hires_2015.ipynb
 M attempts/000013-hires-2015-01.yaml
 M entries/000013-hires-2015/README.md
 M entries/000013-hires-2015/hires.py
 M entries/000013-hires-2015/reproduce_hires_2015.ipynb
```

**Agent**

I re-ran the claims each answer bears on, then updated the notebook, helper, README and attempt record. The entry passes `lock` and `all` (0 errors, the notebook runs in 8.7 min), and the handover is in `executed/000013-hires-2015/handover/`. Nothing is committed and nothing was verified.

Four outcomes changed. The record now has 22 reproduced, 5 partially reproduced, 4 not reproduced and 14 blocked, against 20, 5, 5 and 15 before.

**Q1: where the cutoff search starts.** The answer is the transition where the curve levels off; the literal search from 1 ms is now a variant only.

| Claim | Before | Now |
|---|---|---|
| table1-l4-c2 | blocked | reproduced: 15 of 18 values in all 64 reading combinations |
| table1-l5 | blocked | partially reproduced: 11 to 13 of 18 in every combination |
| table1-l4-outside | blocked | blocked: 7 to 9 of 17, which straddles its threshold of 9 |
| fig3c-touch-spikes-l4c2 | blocked | blocked, now only on the curve's range (Q2) |
| fig3c-touch-spikes-outside, fig3c-touch-spikes-l5, the four fig3d claims | blocked | blocked: they depend on a blocked claim, and their own readings disagree or fail |
| fig5c-modulation-index | reproduced | reproduced: means 0.677, 0.713, 0.672 (before 0.853, 0.857, 0.827, from the literal cutoff) |
| fig5-modulation-correlations | blocked | blocked: holds in 16 of 64 combinations |
| example-cell-touch-window | partially | partially: cell 23 gets the same window under either start |
| text-spikes-per-touch | reproduced | reproduced |
| l4-outside-weaker-touch | reproduced | reproduced |

For table1-l4-c2, the 15 rests on reading whisking periods as outside touch epochs. The Table 1 criterion doesn't name this reading. I took it from the claims file's own definitions, which the Q5 answer also quotes. With touch epochs counted in, the count is 14, which is partially reproduced. A verifier may question this choice.

**Q2: the range of the cutoff curve.** The paper doesn't give it, so 100 and 200 ms are both readings, as already run. For fig3c-touch-spikes-l4c2, all 4 readings with 100 ms pass but only 1 of 4 with 200 ms does. It stays blocked, now only on this detail.

**Q3: the pre-touch window for touch detection.** The answer adds a third reading, all pre-touch windows. fig4a-touch-detection-c2 stays blocked: the population sizes reaching 95% run from 1 to 30 neurons and none is within 15 ± 1.5. Adding the reading changed the random draws, so three earlier values moved by 1 to 3 neurons. fig4a-touch-detection-outside stays blocked, because the two performance measures still disagree.

**Q4: the time decoder's classes and smoothing.** Both class sets were already run; I added a smaller pseudocount (0.01) as a variant. fig4b-touch-time-precision stays not reproduced: the minimum RMS error is 1.09 to 1.40 ms, or 1.18 to 1.48 ms with the variant, against 0.55 ms.

**Q5: the phase decoder's cycles and empty bins.** The decoder now uses the phase-tuning cycles, and empty bins are filled by add-one smoothing or a floor rate. fig4c-phase-decoding goes from not reproduced to blocked:
- With held-out cycle counts and add-one smoothing, it never reaches 76% correct.
- With Poisson rates and add-one smoothing, C2 reaches it at 60 to 84 deg.
- With the floor rate, C2 reaches it at 12 to 15 deg.

So C2 falls on both sides of the paper's 24 deg, which is the criterion's fallback. The floor value is my own choice, as the paper gives none.

**Q6: the refractory model's rate.** The rate is now raised to make up for the refractory period (Berry and Meister's free rate), and the model's mean count matches the data's (ratio 1.00 to 1.03). fig6d-not-refractory stays blocked. Under one comparison the data FF is never below the model's by more than the error bars. Under the other it is below in only 4 of the 6 touch readings; without the compensation it was below in all 6.

**Q7: the L5 whisking increase.** The measure is now the median of the per-cell differences, which is +1.88 and +1.79 spikes/s, with p = 0.024 and 0.014. whisking-rate-l5-increase goes from partially reproduced to reproduced.

Each affected claim's notes in the attempt record say what the answer changed.

## End of run

48 turns, 37 minutes, result: success.
