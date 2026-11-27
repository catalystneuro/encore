# kaku-2025 · author-revise-1 · run 44077639707

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
date -u; cat transcripts/kaku-2025/verifier-1-report.md; ls entries/kaku-2025 entries/kaku-2025/*; grep -n "" docs/protocol.md | sed -n '1,40p' | cut -c1-200
```

**Agent calls Bash**

```bash
grep -n "^#" docs/protocol.md
```

```
Tue Nov 17 11:57:00 UTC 2026
**Verification report, round 1: Kaku, Liu et al. 2025 (doi:10.1101/2025.01.27.635041) on DANDI:001619 v0.251027.1953**

The claims file has 48 claims. I checked the archive through the API. It holds 335 files, all `*_behavior+core.nwb`, and the draft version is the same. All 31 subjects are VGAT-ChR2-EYFP mice, and no other species or genotype appears. Notebook cell 5 shows the files have no cue or photostimulation times and no videos.

### A. Outcomes

| Claim | Outcome | Reason |
|---|---|---|
| code-dataset-link | reproduced | Every input exists. 20,109 units pass get_good_units, 0.9% below 20,300 (cell 13). |
| fig1d-lick-breath-frequencies | not_reproduced | Mean lick frequency is 26.96 Hz under (a) and 8.06 Hz under (b), against 6.23 ± 0.62. Breathing is within tolerance under (a). The value under (b) is distorted by the defect in B2. |
| fig1f-inspiration-between-licks | not_reproduced | Pooled, 30.4% of in-bout inspirations fall inside a protrusion; no session has none (cell 20). Unchecked alignment, B6. |
| fig1g-lick-delayed-before-slow-breath | partially_reproduced | Over sessions: +22.0 ms, p = 4.5e-4, n = 71. Only 16 of 20 mice are positive, and over mice p = 0.18 (cell 21). |
| fig1f-licking-mode-switch | not_reproduced | The inter-breath interval rises with lick count in 116 of 117 sessions. The latency from last lick to next inspiration differs by 62.5% across groups (133, 92, 82 ms); the limit is 20% (cell 22). |
| fig1i-breath-delayed-before-slow-lick | reproduced | Over sessions: +10.5 ms, p = 1.5e-9, n = 86 (cell 23). |
| ed1-unidirectional-models-fail | reproduced (weak) | Breathing model: Fig 1i difference is 0.0 in all 162 sessions. Licking model: the Fig 1g measure exists in only 2 of 169 sessions, so "not significant" holds only by default (cell 24, B8). |
| ed2-rats-similar | blocked: data_missing | The archive has mouse data only. |
| ed1bc-licks-pause-at-swallows | not_reproduced | Lick probability is lower af
[... 127 more lines not kept]
```

```
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
627:### Round 2: with the author's conclusions
[... 1 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 193,640p docs/protocol.md
```

```
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

Do this before any analysis.

[... 428 more lines not kept]
```

**Agent calls Bash**

```bash
ls attempts/ | grep kaku; ls questions | grep kaku; wc -l entries/kaku-2025/* attempts/kaku-2025-01.yaml; cat entries/kaku-2025/entry.yaml; ls executed/kaku-2025 2>/dev/null; ls claims* papers 2>/dev/null | head; git log --oneline | head -5; ls transcripts/kaku-2025
```

```
kaku-2025-01.yaml
    56 entries/kaku-2025/README.md
    23 entries/kaku-2025/entry.yaml
   975 entries/kaku-2025/kaku.py
  1600 entries/kaku-2025/reproduce_kaku_2025.ipynb
     5 entries/kaku-2025/requirements.in
    33 entries/kaku-2025/requirements.lock.txt
   505 attempts/kaku-2025-01.yaml
  3197 total
schema_version: 1
name: kaku-2025
type: reproduction
title: A brainstem map of orofacial rhythms (Kaku, Liu et al. 2025)
description: Tests the findings of Kaku, Liu et al. (2025) on dandiset 001619, which holds the
  brainstem Neuropixels recordings of 31 mice in the multi-directional licking task, with DeepLabCut
  tracking of jaw and tongue, the airflow trace and CCF positions of the units. It ports the paper's
  analysis code to streamed NWB files and tests the lick-breath timing, swallow detection, unit
  counts, phase tuning to licking and breathing, swallow modulation and their maps. The cued licking
  task with photostimulation, the rat recordings, the raw videos and the premotor tracing are not in
  the dandiset.
[... 37 more lines not kept]
```

**Agent calls Bash**

```bash
cat transcripts/kaku-2025/author-answers-report.md; cat attempts/kaku-2025-01.yaml
```

```
<persisted-output>
Output too large (33.1KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/66737f11-a542-4ee7-a3f2-e26c0cc8667e/tool-results/b0jv5ong9.txt

Preview (first 2KB):
There were no questions to act on, so no claim was re-run and no outcome changed.

**Questions:** `questions/001619.yaml` does not exist, and it never existed on any branch. The first author run asked a reader nothing: its report says "Questions to a reader: none." The reader's answer run found nothing to answer (`transcripts/001619/answer-report.md`) and changed neither the claims file nor `questions/`. The claims file under `claims/001619/` is still the one from the checked commit `b99964abb2`. The three open method questions from the first run are for the paper's authors: the significance test for the licking and breathing MI, how the swallow MI is normalised, and how the units in Fig 4d were selected. They stay in the record as `methods_unavailable` findings, which a reader does not answer.

**Effect on claims:** None. All 48 outcomes stand as before:

| Outcome | Claims |
|---|---|
| Reproduced | 16 |
| Partially reproduced | 7 |
| Not reproduced | 8 |
| Blocked, data missing | 15 |
| Blocked, other | 4 |
| Blocked, metadata insufficient | 1 |
| Blocked, too large | 1 |

[... 17 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "attempts/kaku-2025-01.yaml"
}
```

```
1	schema_version: 3
2	id: kaku-2025-01
3	datasets:
4	- archive: dandi
5	  id: 001619
6	  version: 0.251027.1953
7	  doi: 10.48324/dandi.001619/0.251027.1953
8	  relation: primary
9	paper: doi:10.1101/2025.01.27.635041
10	date: '2026-11-05'
11	entry: kaku-2025
12	provenance:
13	  kind: agent
14	  accountable:
15	    name: CatalystNeuro
16	  agent:
17	    harness: Claude Code
18	    model: claude-opus-5-5
19	    protocol: pilot-13
20	  runner:
[... 486 more lines not kept]
```

**Agent calls Bash**

```bash
ls claims/ | grep -i kaku; ls questions | head; ls paper/; python -c "
import json;nb=json.load(open('entries/kaku-2025/reproduce_kaku_2025.ipynb'))
for i,c in enumerate(nb['cells']):
  s=''.join(c['source']); print(i,c['cell_type'],c['metadata'].get('tags'),len(s),repr(s[:90]))
"
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd entries/kaku-2025; python -c "
import json;nb=json.load(open('reproduce_kaku_2025.ipynb'))
for i in [0,1,2,3]:
  print('----',i); print(''.join(nb['cells'][i]['source']))
"; grep -n "^def \|^class \|^[A-Z_]* = " kaku.py
```

```
---- 0
# Reproducing Kaku, Liu et al. (2025) from dandiset 001619

Paper. Kaku H, Liu LD, Gao R, West S, Liao S-M, Finkelstein A, Kleinfeld D, Thomas A, Tipparaju SL,
Svoboda K, Li N (2025). A brainstem map of orofacial rhythms. bioRxiv,
[doi:10.1101/2025.01.27.635041](https://doi.org/10.1101/2025.01.27.635041). The claims file was written
from the preprint, version 1 (January 27, 2025), its Methods and the Extended Data legends, and from the
paper's analysis code (github.com/NuoLiLabBCM/KakuEtAl2025 at commit fbc0abe).

Dandiset. [DANDI:001619](https://dandiarchive.org/dandiset/001619/0.251027.1953), version
0.251027.1953. The paper cites no version (its data statement says the data will be deposited upon
publication; the dandiset was created later). This is the only published version, and it is the
most recent; the draft has the same 335 assets and size. It holds the brainstem Neuropixels recordings
of the multi-directional licking task: one NWB file per probe insertion, with units, quality metrics,
CCF positions, DeepLabCut tracking and the airflow (breathing) trace, per trial.

What is not in it. The cued licking task with ALM, latSC and brainstem photostimulation, the rat
recordings, the raw videos, and the premotor tracing data are not in the dandiset.

Outside input. Region names in the files are Allen CCF names; their acronyms and parent regions
[... 117 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "entries/kaku-2025/kaku.py",
 "offset": 1,
 "limit": 70
}
```

```
1	"""Loading and measures for dandiset 001619, Kaku, Liu et al. (2025), "A brainstem map of
2	orofacial rhythms", bioRxiv doi:10.1101/2025.01.27.635041.
3	
4	Each NWB file holds one Neuropixels insertion (probe p1 or p2) of one session: the units with
5	their quality metrics and CCF positions (`units/histology`), the side and bottom DeepLabCut
6	tracking per trial (1471 frames at 3.4 ms), the 3D tracking, and the 25 kHz airflow per trial.
7	Trials are stored separately; every per-trial time starts at 0 at the trial start. The two
8	probes of a session carry the same behaviour (checked in the notebook), so behaviour is read
9	once per session. Files are streamed from the archive at the pinned version; nothing is written
10	to disk.
11	
12	Spike times: `units/spike_times_index` holds the start offset of each unit, not its end, so the
13	standard NWB reading gives each unit the spikes of the unit before it. Spikes are read here by
14	the per-unit, per-trial spike counts of `units/unit and trial pairs`, which agree with the index
15	read as starts (checked in the notebook).
16	
17	Where the parameters come from. "Code" is the paper's analysis code, process_mat.py and
18	generate_figures.py in https://github.com/NuoLiLabBCM/KakuEtAl2025 at commit fbc0abe, which
19	the claims file names and whose choices it adopts in its header.
20	
[... 50 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "entries/kaku-2025/kaku.py",
 "offset": 340,
 "limit": 640
}
```

```
340	    return sess
341	
342	
343	# ----------------------------------------------------------------------------- behaviour
344	
345	def _ma_downsample(x, w):
346	    """np.convolve(x, ones(w)/w, 'same')[w::w], computed only at the kept samples."""
347	    c = np.r_[0.0, np.cumsum(x)]
348	    n = len(x)
349	    j = np.arange(w, n, w)
350	    lo = np.clip(j - (w - 1) // 2 - (1 if w % 2 == 0 else 0), 0, n)
351	    hi = np.clip(j + w // 2 + 1 - (1 if w % 2 == 0 else 0), 0, n)
352	    # numpy 'same' for odd w centres the kernel; for even w it is shifted by one
353	    return (c[hi] - c[lo]) / w
354	
355	
356	def movement_timing(sess):
357	    """Code get_movement_timing: tongue onsets and offsets, lick bouts and inspiration onsets
358	    on the concatenated timeline (s)."""
359	    bw = FRAME_S
[... 617 more lines not kept]
```

**Agent calls Bash**

```bash
cd  wc -l claims/kaku-2025.yaml; grep -n "^  - id:\|^- id:\|^[a-z_]*:" claims/kaku-2025.yaml | head -80
```

```
1065 claims/kaku-2025.yaml
171:schema_version: 2
172:dataset:
175:paper: doi:10.1101/2025.01.27.635041
176:claims:
177:- id: code-dataset-link
190:- id: fig1d-lick-breath-frequencies
227:- id: fig1f-inspiration-between-licks
240:- id: fig1g-lick-delayed-before-slow-breath
257:- id: fig1f-licking-mode-switch
272:- id: fig1i-breath-delayed-before-slow-lick
287:- id: ed1-unidirectional-models-fail
309:- id: ed2-rats-similar
322:- id: ed1bc-licks-pause-at-swallows
337:- id: fig1k-rhythms-follow-swallow-at-fixed-latency
350:- id: fig1l-lick-interval-preserved
365:- id: fig1l-lick-cycle-prolonged
386:- id: fig1n-breath-interval-preserved
398:- id: fig1n-breath-cycle-prolonged
415:- id: units-count
[... 34 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "claims/kaku-2025.yaml",
 "limit": 475
}
```

```
1	# Claims for Kaku, Liu et al. (2025), "A brainstem map of orofacial rhythms", bioRxiv
2	# doi:10.1101/2025.01.27.635041, on dandiset 001619.
3	# Written by an agent (model "claude-opus-5-5", Claude Code in GitHub Actions), 2026-10-21,
4	# protocol pilot-10 as stated in docs/protocol.md.
5	#
6	# Text read: the bioRxiv preprint, version 1 (posted January 27, 2025), as served on its web
7	# page, stored in paper/10.1101-2025.01.27.635041.txt: main text, legends of Figures 1 to 5,
8	# Methods and references, and the supplement "Extended Data Figures" (the legends of Extended
9	# Data Figures 1 to 12, from the supplement PDF, extracted to text). The display equations of
10	# the Methods (the circular Gaussian tuning curve and the VAF) are missing from the text; the
11	# words around them name every term. The Figure 5 legend stops at panel f, although the
12	# Results cite a Figure 5g. No later version was read. Data the dandiset description names: its
13	# title and description only (no data or file was looked at).
14	#
15	# Code read: github.com/NuoLiLabBCM/KakuEtAl2025 at commit fbc0abe (2026-06-18). The preprint
16	# says "Code used for analyses will be deposited upon publication"; this repository is the one
17	# the dandiset description names as "the corresponding analysis code", and its README points
18	# at the preprint v1 and at dandiset 001619. It holds process_mat.py (unit quality filter,
19	# trial filter, tongue and inspiration onsets, lick bouts, licking and breathing phase tuning
20	# and modulation index, the lick-to-breath and breath-to-lick timing analyses of Figs 1f-i and
[... 455 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "claims/kaku-2025.yaml",
 "offset": 475,
 "limit": 460
}
```

```
475	  statement: Units showed significant phase tuning to licking (3551 of 20,300) or breathing
476	    (1015 of 20,300), but rarely to both (182 of 20,300).
477	  source: Results, Brainstem activity maps of orofacial rhythms, paragraph 3
478	  quote: Individual units exhibited significant phase tuning to either licking (3551/20300), or
479	    breathing (1015/20300), but rarely to both (182/20300)
480	  depends_on:
481	  - units-count
482	  expected:
483	  - quantity: licking-tuned units
484	    value: 3551
485	    tolerance: 355
486	  - quantity: breathing-tuned units
487	    value: 1015
488	    tolerance: 102
489	  - quantity: units tuned to both
490	    value: 182
491	    tolerance: 18
492	  criterion: Phase tuning and MI as in the header, tuned at P < 0.001 and MI > 0.6, readings V2
493	    (a) and (b) and V3 (a) and (b). The text does not say whether the licking and breathing
494	    counts include the 182 units tuned to both; readings (i) they include them; (ii) they
[... 440 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR; timeout 30 git clone -q https://github.com/NuoLiLabBCM/KakuEtAl2025 kcode 2>&1 | tail -2; cd kcode 2>/dev/null && git checkout -q fbc0abe && ls; curl -sI -m 20 https://download.alleninstitute.org/informatics-archive/current-release/mouse_ccf/annotation/ccf_2017/annotation_25.nrrd | head -5
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR/kcode; grep -n "def get_peak_diff_lick_unit" -A75 process_mat.py | grep -n "n_trial\|sort\|i1\|i2\|median\|fast\|slow" | head -40
```

```
3:897-    n_trial=40
5:899-    min_trial=40
65:959-    sorted_indexes=np.argsort(ibi)
66:960-    sorted_indexes=sorted_indexes[::-1]
68:962-    licks = [licks[i] for i in sorted_indexes]
69:963-    n_licks=n_licks[sorted_indexes]
70:964-    lick_bef_time=lick_bef_time[sorted_indexes]
71:965-    ibi=ibi[sorted_indexes]
73:967-    d_bound=np.median(ibi[n_licks==2])
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/kcode; sed -n 960,1040p process_mat.py
```

```
sorted_indexes=sorted_indexes[::-1]

    licks = [licks[i] for i in sorted_indexes]
    n_licks=n_licks[sorted_indexes]
    lick_bef_time=lick_bef_time[sorted_indexes]
    ibi=ibi[sorted_indexes]

    d_bound=np.median(ibi[n_licks==2])

    psth_1_i= np.where((ibi<d_bound) & (n_licks==2))[0]
    psth_2_i= np.where((ibi>d_bound) & (n_licks==2))[0]
    if len(psth_1_i)>n_trial:
        psth_1_i=psth_1_i[:n_trial]
    if len(psth_2_i)>n_trial:
        psth_2_i=psth_2_i[-n_trial:]

    if (len(psth_1_i)<min_trial) | (len(psth_2_i)<min_trial):
        print(f'Less than {min_trial} trials')
        return np.array([]), np.array([]),np.array([]),np.array([]),np.array([]),np.array([]),np.array([]) 

[... 63 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/kcode; grep -n "def plot_licking_swallow_summary" -A80 generate_figures.py | head -110
```

```
344:def plot_licking_swallow_summary(licks, num_after=2, num_before=4, max_ili=1/3, min_ili=1/15, split=3):
345-    """ """
346-    ili = []
347-    filtered_licks = []
348-    for lick in licks:
349-        lick = np.atleast_1d(lick)
350-        if (lick[lick>=0].size >= num_after) & (lick[lick<0].size >= num_before): 
351-            before_4, before_3, before_2, before_1 = lick[lick<0][-num_before:]
352-            after_1, after_2 = lick[lick>=0][:num_after]
353-            _ili = after_1 - before_1 
354-            if (_ili < max_ili) & (_ili > min_ili): 
355-                ili.append(_ili) 
356-                filtered_licks.append(lick)
357-    ili = np.array(ili)
358-    sorted_ix = np.argsort(ili) 
359-    sorted_ix = sorted_ix[::-1] 
360-    licks_sorted = [filtered_licks[i] for i in sorted_ix]
361-    licks = licks_sorted.copy()
362-    
363-    ili_0, ili_1, ili_neg1,  = [], [], []
[... 62 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/kcode; grep -n "get_licks_around_event\|get_breaths_around_event" -A3 process_mat.py generate_figures.py | head -40; grep -n "def get_licks_around_event" -A25 process_mat.py
```

```
process_mat.py:1211:def get_licks_around_event(mat):
process_mat.py-1212-    """ """
process_mat.py-1213-    events = mat[foi]['swallow_times']
process_mat.py-1214-    result, indices = [], []
--
process_mat.py:1229:def get_breaths_around_event(mat):
process_mat.py-1230-    """ """
process_mat.py-1231-    events = mat[foi]['swallow_times']
process_mat.py-1232-    result, indices = [], []
--
process_mat.py:1554:        mat[foi]['swallow_aligned_licks'] = get_licks_around_event(mat)
process_mat.py:1555:        mat[foi]['swallow_aligned_breaths'] = get_breaths_around_event(mat)
process_mat.py-1556-        
process_mat.py-1557-        # swallow aligned psth and raster
process_mat.py-1558-        print("\nFetching swallow psth & raster...")
1211:def get_licks_around_event(mat):
1212-    """ """
1213-    events = mat[foi]['swallow_times']
1214-    result, indices = [], []
1215-    fs = 1000/3.4
[... 22 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/kaku-2025; python -c "
import json;nb=json.load(open('reproduce_kaku_2025.ipynb'))
for i in [10,11,22,23,26,28,32]:
  print('----',i); print(''.join(nb['cells'][i]['source']))
"
```

```
---- 10
# Clock check. Spikes, tracking and airflow are stored per trial on separate arrays. If they share the
# trial clock, phase tuning to jaw and breathing should fall when each trial's spikes are paired with the
# next trial's phases.
for mod, col in (("jaw", "jaw_mi_grid_4"), ("breathing", "br_mi_grid_4")):
    shift = "jaw_mi_shift" if mod == "jaw" else "br_mi_shift"
    top = T[T[col] > 0.6]
    print(f"{mod}: units with grid MI > 0.6, true pairing {len(top)}; their median MI {top[col].median():.3f} true, "
          f"{top[shift].median():.3f} with the next trial's phases; units above 0.6 after the shift: {(T[shift] > 0.6).sum()}")
by = T.groupby("subject").apply(lambda g: pd.Series({"n_true": (g.jaw_mi_grid_4 > 0.6).sum(), "n_shift": (g.jaw_mi_shift > 0.6).sum(),
                                                     "br_true": (g.br_mi_grid_4 > 0.6).sum(), "br_shift": (g.br_mi_shift > 0.6).sum()}))
print("\nPer subject, units with MI > 0.6, true and shifted pairing:")
print(by.T.to_string())
# Behaviour: inspirations and tongue onsets lie on the same per-trial clock; the lick-breath relation is tested in fig1f.
---- 11
Jaw phase tuning is present with the true pairing (3,476 units above MI 0.6, median 0.80) and falls
when spikes are paired with the next trial's tracking (median 0.13, 308 units above 0.6), in every
subject. Breathing tuning falls likewise overall (950 units, median 0.74, against 0.16 and 313 units),
but in four subjects (DL004, DL005, DL010, DL020) the shifted pairing gives as many units above 0.6 as
the true one (5 against 7, 7 against 9, 14 against 14, 3 against 6), so for their airflow the shared
[... 159 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/kaku-2025; python -c "
import json;nb=json.load(open('reproduce_kaku_2025.ipynb'))
for i in [34,36,38,48,52,62,63,64]:
  print('----',i); print(''.join(nb['cells'][i]['source']))
"
```

```
/bin/bash: line 1: cd: entries/kaku-2025: No such file or directory
---- 34
# Extended Data Fig 1b-c: lick probability around swallows and around expirations inside bouts
bins = np.arange(-0.3, 0.3 + 1e-9, kaku.FRAME_S)
rows = []
for r, (_, s) in zip(res, sess.iterrows()):
    sw = r["swallow_times"]
    if len(sw) < 20:
        continue
    mt = r["mt"]
    ton = mt["tongue_onset_all"]
    ex = r["expir_onset"]
    ex = ex[in_bouts(ex, mt)]
    def prob(ev):
        h = np.zeros(len(bins) - 1)
        for e in ev:
            h += np.histogram(ton - e, bins)[0]
        return h / max(len(ev), 1)
    ps, pe = prob(sw), prob(ex)
    c = bins[:-1]
[... 177 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n -i "43 recordings\|simultaneous\|12c\|Extended Data Figure 12" paper/10.1101-2025.01.27.635041.txt | cut -c1-400 | head -20
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  sed -n 888,915p paper/10.1101-2025.01.27.635041.txt; grep -n -i "two probes\|2 Neuropixels\|dual\|cued licking task" paper/10.1101-2025.01.27.635041.txt | cut -c1-300 | head
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
date -u; cd entries/kaku-2025; sed -n 86,340p kaku.py
```

```
Tue Nov 17 11:59:47 UTC 2026
BEH = "processing/processing module/breathing_behavior/breathing"


# ----------------------------------------------------------------------------- archive

def list_assets():
    """Assets of the pinned version: path, asset id, size, subject, session, probe, url."""
    import json
    import urllib.request
    url = f"{API}/dandisets/{DANDISET_ID}/versions/{DANDISET_VERSION}/assets/?page_size=1000"
    rows = []
    while url:
        page = json.load(urllib.request.urlopen(url))
        rows += page["results"]
        url = page["next"]
    out = []
    for a in rows:
        m = re.match(r"(sub-[^/]+)/\1_ses-(.+)-(p\d)_behavior\+core\.nwb$", a["path"])
        out.append({"path": a["path"], "asset_id": a["asset_id"], "size": a["size"],
[... 236 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/kaku-2025; cat > $TMPDIR/dev_survey.py <<'EOF'
import time, pickle, sys
sys.path.insert(0, ".")
import kaku
t=time.time()
assets = kaku.list_assets()
files, units = kaku.survey(assets)
onto = kaku.ontology()
regions = kaku.region_table(units.region.dropna().unique(), onto)
print("survey", time.time()-t)
pickle.dump((assets, files, units, onto, regions), open(sys.argv[1], "wb"))
EOF
/usr/bin/time -v python $TMPDIR/dev_survey.py $TMPDIR/survey.pkl 2>&1 | grep -E "survey|Maximum resident|Elapsed"
```

```
/bin/bash: line 1: cd: entries/kaku-2025: No such file or directory
  File "/tmp/claude-1001/dev_survey.py", line 3, in <module>
	Command being timed: "python /tmp/claude-1001/dev_survey.py /tmp/claude-1001/survey.pkl"
	Elapsed (wall clock) time (h:mm:ss or m:ss): 0:00.25
	Maximum resident set size (kbytes): 22768
```

**Agent calls Bash**

```bash
pwd; python -c "import h5py, remfile, scipy, pandas; print('ok')"; ls ../../.venv* 2>/dev/null | head -2; cat requirements.in
```

```
entries/kaku-2025
Traceback (most recent call last):
  File "<string>", line 1, in <module>
    import h5py, remfile, scipy, pandas; print('ok')
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
ModuleNotFoundError: No module named 'h5py'
h5py
numpy
pandas
remfile
scipy
```

**Agent calls Bash**

```bash
cd  grep -n "venv\|def cmd_run\|def run\b\|uv " tools/entry.py | head -30; ls .entry-envs 2>/dev/null; ls -a | head -30
```

```
521:        if any(part in ("__pycache__", ".ipynb_checkpoints", ".venv") or part.endswith(".pyc") for part in rel.parts):
545:def run(entry_dir: Path, output_dir: Path, timeout: int, max_minutes: float, fresh: bool = False) -> int:
557:    venv = (output_dir / ".venv").resolve()
558:    python = venv / "bin" / "python"
562:    for cmd in (["uv", "venv", "--quiet", "--clear", "--python", python_of(entry_dir), str(venv)],
565:                [str(python), "-m", "ipykernel", "install", "--prefix", str(venv), "--name", kernel]):
579:            env={**os.environ, "JUPYTER_PATH": str(venv / "share" / "jupyter")})
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
[... 17 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && uv venv -q dev && uv pip install -q --python dev/bin/python -r entries/kaku-2025/requirements.lock.txt && dev/bin/python -c "import h5py, remfile; print('ok')"
```

```
ok
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd entries/kaku-2025 && /usr/bin/time -v $TMPDIR/dev/bin/python $TMPDIR/dev_survey.py $TMPDIR/survey.pkl 2>&1 | grep -E "survey|Maximum resident|Elapsed|Error"
```

```
survey 224.61400485038757
	Command being timed: "/tmp/claude-1001/dev/bin/python /tmp/claude-1001/dev_survey.py /tmp/claude-1001/survey.pkl"
	Elapsed (wall clock) time (h:mm:ss or m:ss): 3:47.58
	Maximum resident set size (kbytes): 608296
```

**Agent calls Bash**

```bash
python - <<'EOF'
p='kaku.py'; s=open(p).read()
old_l = s[s.index("def peak_diff_lick_behv"):s.index("def peak_diff_breath_behv")]
new_l = '''def _lick_peak_diff(licks, i1, i2):
    """Second-lick peak difference (slow minus fast) of the code's get_peak_diff_lick_behv for the
    cycles i1 (fast) and i2 (slow): lick PSTHs from -0.4 to 1 s in 20 ms bins, first peak in
    0.12-0.32 s (fast) and 0.16-0.36 s (slow)."""
    bins = np.arange(-0.4, 1, 0.02)
    centres = bins[1:] - 0.01
    p1 = np.mean([np.histogram(licks[i], bins)[0] for i in i1], 0) / 0.02
    p2 = np.mean([np.histogram(licks[i], bins)[0] for i in i2], 0) / 0.02
    pk1 = _peaks(p1, centres, 5, 0.14, (0.12, 0.32))
    pk2 = _peaks(p2, centres, 5, 0.14, (0.16, 0.36))
    return pk1, pk2, (pk2[0] - pk1[0]) if len(pk1) and len(pk2) else np.nan


def random_split(i1, i2, rng):
    """Null for the fast/slow split (verifier, round 1): the cycles of both groups pooled and
    split at random into groups of the same sizes."""
    pool = rng.permutation(np.r_[i1, i2])
    return np.sort(pool[:len(i1)]), np.sort(pool[len(i1):])


def peak_diff_lick_behv(mt, spikes=None, n_trial=None, unit=False, rng=None, n_null=20):
    """Code get_peak_diff_lick_behv (unit=False) and the event selection of
    get_peak_diff_lick_unit. Returns the selection and the behavioural peaks. With rng, also
    the same difference for n_null random splits of the two-lick cycles (diff_null)."""
    insp, ton = mt["inspir_onset"], mt["tongue_onset"]
    on, off = mt["bout_on"], mt["bout_off"]
    insp_l = np.hstack([insp[(insp > on[i] + 0.2) & (insp < off[i] - 0.2)] for i in range(len(on))]) if len(on) else np.array([])
    max_ibi = np.max(np.diff(insp))
    rows = []
    for i in range(2, len(insp_l) - 2):
        lick = ton[(ton > insp_l[i - 2]) & (ton < insp_l[i + 2])]
        lick_in = lick[(lick > insp_l[i]) & (lick < insp_l[i + 1])]
        if lick_in.size:
            bef = lick[lick < insp_l[i]]
            if len(bef):
                rows.append((insp_l[i], lick - insp_l[i], lick_in[-1] - insp_l[i], bef[-1] - insp_l[i],
                             lick_in.size, insp_l[i + 1] - insp_l[i]))
    if not rows:
        return None
    t0 = np.array([r[0] for r in rows])
    licks = [r[1] for r in rows]
    lick2 = np.array([r[2] for r in rows])
    lbef = np.array([r[3] for r in rows])
    nl = np.array([r[4] for r in rows])
    ibi = np.array([r[5] for r in rows])
    k = ibi < max_ibi
    t0, licks, lick2, lbef, nl, ibi = t0[k], [l for l, kk in zip(licks, k) if kk], lick2[k], lbef[k], nl[k], ibi[k]
    rem1 = np.where((nl == 1) & (lbef > -0.05) & (lbef < 0))[0]
    rem2 = np.where((nl == 2) & (lick2 > ibi - 0.05) & (lick2 < ibi))[0]
    keep = np.setdiff1d(np.arange(len(ibi)), np.r_[rem1, rem2])
    t0, licks, lbef, nl, ibi, lick2 = t0[keep], [licks[i] for i in keep], lbef[keep], nl[keep], ibi[keep], lick2[keep]
    order = np.argsort(ibi)[::-1]
    t0, licks, lbef, nl, ibi, lick2 = t0[order], [licks[i] for i in order], lbef[order], nl[order], ibi[order], lick2[order]
    out = {"t0": t0, "licks": licks, "lick_bef": lbef, "n_licks": nl, "ibi": ibi, "max_ibi": max_ibi,
           "last_lick_to_next_insp": ibi - lick2}
    if not (nl == 2).any():
        return out
    d = np.median(ibi[nl == 2])
    i1 = np.where((ibi < d) & (nl == 2))[0]
    i2 = np.where((ibi > d) & (nl == 2))[0]
    out.update(i_fast=i1, i_slow=i2)
    if len(i1) >= 40 and len(i2) >= 40:
        pk1, pk2, diff = _lick_peak_diff(licks, i1, i2)
        out.update(peaks_fast=pk1, peaks_slow=pk2, diff=diff)
        if rng is not None:
            out["diff_null"] = np.array([_lick_peak_diff(licks, *random_split(i1, i2, rng))[2] for _ in range(n_null)])
    else:
        out["diff"] = np.nan
    # Unit version. Cycles are sorted longest first, so the 40 fastest are the last 40 of i1 and
    # the 40 slowest the first 40 of i2, as the claims file's header says. The code
    # (get_peak_diff_lick_unit) takes psth_1_i[:n_trial] and psth_2_i[-n_trial:], the 40 cycles
    # nearest the median on each side; it is kept as a variant.
    out["unit_fast"] = i1[-40:]
    out["unit_slow"] = i2[:40]
    out["unit_fast_code"] = i1[:40]
    out["unit_slow_code"] = i2[-40:]
    return out


'''
s = s.replace(old_l, new_l)
old_b = '''    bins = np.arange(-0.1, 0.6, 0.02)
    centres = bins[1:] - 0.01
    if len(i1) >= 100 and len(i2) >= 100:
        p1 = np.mean([np.histogram(breaths[i], bins)[0] for i in i1], 0) / 0.02
        p2 = np.mean([np.histogram(breaths[i], bins)[0] for i in i2], 0) / 0.02
        pk1 = _peaks(p1, centres, 7, 0.24, (0, 0.22))
        pk2 = _peaks(p2, centres, 7, 0.24, (0, 0.24))
        out.update(peaks_fast=pk1, peaks_slow=pk2,
                   diff=(pk2[0] - pk1[0]) if len(pk1) and len(pk2) else np.nan)
    else:
        out["diff"] = np.nan
    return out
'''
new_b = '''    if len(i1) >= 100 and len(i2) >= 100:
        pk1, pk2, diff = _breath_peak_diff(breaths, i1, i2)
        out.update(peaks_fast=pk1, peaks_slow=pk2, diff=diff)
        if rng is not None:
            out["diff_null"] = np.array([_breath_peak_diff(breaths, *random_split(i1, i2, rng))[2] for _ in range(n_null)])
    else:
        out["diff"] = np.nan
    return out


def _breath_peak_diff(breaths, i1, i2):
    """Inspiration peak difference of the code's get_peak_diff_breath_behv: PSTHs -0.1 to 0.6 s,
    20 ms bins, first peak in 0-0.22 s (fast) and 0-0.24 s (slow)."""
    bins = np.arange(-0.1, 0.6, 0.02)
    centres = bins[1:] - 0.01
    p1 = np.mean([np.histogram(breaths[i], bins)[0] for i in i1], 0) / 0.02
    p2 = np.mean([np.histogram(breaths[i], bins)[0] for i in i2], 0) / 0.02
    pk1 = _peaks(p1, centres, 7, 0.24, (0, 0.22))
    pk2 = _peaks(p2, centres, 7, 0.24, (0, 0.24))
    return pk1, pk2, (pk2[0] - pk1[0]) if len(pk1) and len(pk2) else np.nan
'''
assert old_b in s
s = s.replace(old_b, new_b)
s = s.replace('''def peak_diff_breath_behv(mt):
    """Code get_peak_diff_breath_behv (and the event selection of get_peak_diff_breath_unit)."""''',
'''def peak_diff_breath_behv(mt, rng=None, n_null=20):
    """Code get_peak_diff_breath_behv (and the event selection of get_peak_diff_breath_unit).
    With rng, also the difference for n_null random splits (diff_null)."""''')
open(p,'w').write(s)
EOF
grep -n "def peak_diff_breath_behv" kaku.py
```

```
571:def peak_diff_breath_behv(mt, rng=None, n_null=20):
```

**Agent calls Bash**

```bash
cat > $TMPDIR/peek.py <<'EOF'
import sys; sys.path.insert(0,'.')
import pickle, numpy as np, kaku
assets, files, units, onto, regions = pickle.load(open(sys.argv[1],'rb'))
url = assets.url.iloc[0]
with kaku.open_nwb(url) as f:
    t3 = f["processing/3D_tracking/tongue_bottom"][:]
    side = f["processing/DLC_tracking/side-facing_camera/tongue"][:]
    print(t3.dtype, t3.shape, side.dtype)
    print("idx range", t3["idx"].min(), t3["idx"].max(), "trial range", side["trial"].min(), side["trial"].max())
    print("nan frac", np.isnan(t3["x"]).mean())
    for o in (-1, 0, 1):
        cs=[]
        for t in range(2, 40):
            a = side["likelihood"][side["trial"]==t][:1471] > 0.95
            b = t3[t3["idx"]==t+o]
            if len(b)==0: continue
            z = np.linalg.norm(np.stack([b["x"],b["y"],b["z"]],1),axis=1)[:1471]
            n=min(len(a),len(z)); ok=~np.isnan(z[:n])
            cs.append(np.corrcoef(a[:n][ok], z[:n][ok])[0,1] if ok.sum()>10 else np.nan)
        print(o, np.nanmean(cs))
EOF
$TMPDIR/dev/bin/python $TMPDIR/peek.py $TMPDIR/survey.pkl
```

```
[('idx', '<i8'), ('x', '<f8'), ('y', '<f8'), ('z', '<f8')] (467778,) [('trial', '<i8'), ('x', '<f8'), ('y', '<f8'), ('likelihood', '<f8')]
idx range 1 318 trial range 1 319
nan frac 0.0
-1 0.004879747687451701
0 -0.05251845382910329
1 -0.004761987060536298
```

**Agent calls Bash**

```bash
cat > $TMPDIR/peek.py <<'EOF'
import sys; sys.path.insert(0,'.')
import pickle, numpy as np, kaku
assets, files, units, onto, regions = pickle.load(open(sys.argv[1],'rb'))
for url in assets.url.iloc[[0, 50, 200]]:
  with kaku.open_nwb(url) as f:
    t3 = f["processing/3D_tracking/tongue_bottom"][:]
    bot = f["processing/DLC_tracking/bottom-facing_camera/tongue"][:]
    for o in (-1, 0, 1):
        cs=[]
        for t in range(2, 60):
            a = bot[bot["trial"]==t][:1471]
            b = t3[t3["idx"]==t+o][:1471]
            n=min(len(a),len(b))
            if n<100: continue
            vis = a["likelihood"][:n]>0.95
            if vis.sum()<20: continue
            M = np.corrcoef(np.stack([a["x"][:n][vis],a["y"][:n][vis],b["x"][:n][vis],b["y"][:n][vis],b["z"][:n][vis]]))
            cs.append(np.nanmax(np.abs(M[:2,2:])))
        print(url[-50:-10], o, round(np.nanmean(cs),3), len(cs))
EOF
$TMPDIR/dev/bin/python $TMPDIR/peek.py $TMPDIR/survey.pkl
```

```
ets/fdb7e0d9-6861-4e3e-aea3-9b63b707cfc5 -1 0.256 57
ets/fdb7e0d9-6861-4e3e-aea3-9b63b707cfc5 0 0.853 57
ets/fdb7e0d9-6861-4e3e-aea3-9b63b707cfc5 1 0.255 57
ets/85763a02-5ef7-4570-8770-a67598d7cfc1 -1 0.341 57
ets/85763a02-5ef7-4570-8770-a67598d7cfc1 0 0.992 57
ets/85763a02-5ef7-4570-8770-a67598d7cfc1 1 0.348 57
ets/da10fa03-f303-48fc-b74d-706f782abeca -1 0.357 58
ets/da10fa03-f303-48fc-b74d-706f782abeca 0 0.985 58
ets/da10fa03-f303-48fc-b74d-706f782abeca 1 0.37 58
```

**Agent calls Bash**

```bash
python - <<'EOF'
p='kaku.py'; s=open(p).read()
# 3D idx check in read_session
old = '''    sess["tongue3d"] = t3d
    sess["jaw3d"] = j3d
'''
new = '''    sess["tongue3d"] = t3d
    sess["jaw3d"] = j3d
    # Whether the 3D `idx` field counts trials as the DLC `trial` field does (verifier, round 1):
    # per good trial, the largest |correlation| between the bottom-camera DLC tongue x, y and the
    # 3D tongue x, y, z over frames with the tongue visible, with 3D idx = trial + offset.
    bt = bottom["tongue"]
    chk = {o: [] for o in (-1, 0, 1)}
    for t in trials[:60]:
        a = bt[bt["trial"] == t][:N_FRAMES]
        for o in chk:
            b = t3[t3["idx"] == t + o][:N_FRAMES]
            n = min(len(a), len(b))
            vis = a["likelihood"][:n] > 0.95
            if vis.sum() < 20:
                continue
            m = np.corrcoef(np.stack([a["x"][:n][vis], a["y"][:n][vis], b["x"][:n][vis], b["y"][:n][vis], b["z"][:n][vis]]))
            chk[o].append(np.nanmax(np.abs(m[:2, 2:])))
    sess["idx3d_corr"] = {o: float(np.mean(v)) if v else np.nan for o, v in chk.items()}
'''
assert old in s; s = s.replace(old, new)

old = '''    pdl = peak_diff_lick_behv(mt)
    pdb = peak_diff_breath_behv(mt)
'''
new = '''    rng_null = np.random.default_rng(seed + 100_000)  # random-split nulls (Figs 1g, 1i, 4e, 4f)
    pdl = peak_diff_lick_behv(mt, rng=rng_null)
    pdb = peak_diff_breath_behv(mt, rng=rng_null)
'''
assert old in s; s = s.replace(old, new)

old = '''    out["pd_breath"] = None if pdb is None else {k: v for k, v in pdb.items() if k != "breaths"}
'''
new = '''    out["pd_breath"] = None if pdb is None else {k: v for k, v in pdb.items() if k != "breaths"}
    out["idx3d_corr"] = sess["idx3d_corr"]
    # Airflow against tongue and jaw (verifier, round 1): cross-correlation of the z-scored 3.4 ms
    # airflow with the tongue-visible indicator and with jaw_y over the concatenated good trials,
    # lags -0.5 to 0.5 s (positive lag: airflow later).
    gb = mt["breath_ds"]
    vis = ((sess["side_tongue_l"] > 0.95) & (sess["bottom_tongue_l"] > 0.95)).astype(float).reshape(-1)[1:]
    jy = sess["jaw_y"].reshape(-1)[1:]
    jy = np.where(np.isnan(jy), np.nanmean(jy), jy)
    nmin = min(len(gb), len(vis))
    lag = 147
    xc = {}
    for name, x in (("tongue", vis[:nmin]), ("jaw", jy[:nmin])):
        a = (gb[:nmin] - gb[:nmin].mean()) / gb[:nmin].std()
        b = (x - x.mean()) / (x.std() or 1)
        c = signal.correlate(a, b, mode="full", method="fft") / nmin
        mid = nmin - 1
        xc[name] = c[mid - lag:mid + lag + 1]
    out["xcorr"] = xc
'''
assert old in s; s = s.replace(old, new)

old = '''            if pdl is not None and len(pdl.get("unit_fast", [])) >= 40 and len(pdl.get("unit_slow", [])) >= 40:
                row["pd_lick_unit"] = unit_peak_diffs(train, pdl["t0"], pdl["unit_fast"], pdl["unit_slow"],
                                                      -0.4, 1, ((0.1, 0.3), (0.16, 0.36)), 0.14)
            else:
                row["pd_lick_unit"] = np.nan
            if pdb is not None and len(pdb["i_fast"]) >= 100 and len(pdb["i_slow"]) >= 100:
                row["pd_breath_unit"] = unit_peak_diffs(train, pdb["t0"], pdb["i_fast"], pdb["i_slow"],
                                                        -0.1, 0.6, ((0, 0.24), (0.02, 0.26)), 0.24)
            else:
                row["pd_breath_unit"] = np.nan
'''
new = '''            # Each unit also gets one random split (verifier, round 1): for licking units 40 and 40
            # two-lick cycles drawn at random from both halves; for breathing units both halves
            # pooled and split at random into groups of the same sizes.
            if pdl is not None and len(pdl.get("unit_fast", [])) >= 40 and len(pdl.get("unit_slow", [])) >= 40:
                lw = (-0.4, 1, ((0.1, 0.3), (0.16, 0.36)), 0.14)
                row["pd_lick_unit"] = unit_peak_diffs(train, pdl["t0"], pdl["unit_fast"], pdl["unit_slow"], *lw)
                row["pd_lick_unit_code"] = unit_peak_diffs(train, pdl["t0"], pdl["unit_fast_code"], pdl["unit_slow_code"], *lw)
                pool = rng_null.permutation(np.r_[pdl["i_fast"], pdl["i_slow"]])
                row["pd_lick_unit_null"] = unit_peak_diffs(train, pdl["t0"], np.sort(pool[:40]), np.sort(pool[40:80]), *lw)
            else:
                row["pd_lick_unit"] = row["pd_lick_unit_code"] = row["pd_lick_unit_null"] = np.nan
            if pdb is not None and len(pdb["i_fast"]) >= 100 and len(pdb["i_slow"]) >= 100:
                bw_ = (-0.1, 0.6, ((0, 0.24), (0.02, 0.26)), 0.24)
                row["pd_breath_unit"] = unit_peak_diffs(train, pdb["t0"], pdb["i_fast"], pdb["i_slow"], *bw_)
                row["pd_breath_unit_null"] = unit_peak_diffs(train, pdb["t0"], *random_split(pdb["i_fast"], pdb["i_slow"], rng_null), *bw_)
            else:
                row["pd_breath_unit"] = row["pd_breath_unit_null"] = np.nan
'''
assert old in s; s = s.replace(old, new)
open(p,'w').write(s)
EOF
grep -n "rng_null" kaku.py | head
```

```
908:    rng_null = np.random.default_rng(seed + 100_000)  # random-split nulls (Figs 1g, 1i, 4e, 4f)
909:    pdl = peak_diff_lick_behv(mt, rng=rng_null)
910:    pdb = peak_diff_breath_behv(mt, rng=rng_null)
1007:                pool = rng_null.permutation(np.r_[pdl["i_fast"], pdl["i_slow"]])
1014:                row["pd_breath_unit_null"] = unit_peak_diffs(train, pdb["t0"], *random_split(pdb["i_fast"], pdb["i_slow"], rng_null), *bw_)
```

**Agent calls Bash**

```bash
python - <<'EOF'
p='kaku.py'; s=open(p).read()
old = '''# ----------------------------------------------------------------------------- reading
'''
new = '''CCF_ANNOTATION_URL = ("https://download.alleninstitute.org/informatics-archive/current-release/"
                      "mouse_ccf/annotation/ccf_2017/annotation_25.nrrd")


def ccf_annotation():
    """Allen CCFv3 (2017) annotation volume at 25 um, axes (AP, DV, ML) in voxels, read from the
    NRRD file into memory (header, then gzip-compressed data with the first axis fastest)."""
    import gzip
    import urllib.request
    raw = urllib.request.urlopen(CCF_ANNOTATION_URL).read()
    head, data = raw.split(b"\\n\\n", 1)
    h = dict(line.split(": ", 1) for line in head.decode().splitlines()[1:] if ": " in line and not line.startswith("#"))
    sizes = tuple(int(x) for x in h["sizes"].split())
    dtype = {"unsigned int": "<u4", "uint32": "<u4", "uint": "<u4"}.get(h["type"], h["type"])
    vol = np.frombuffer(gzip.decompress(data) if h.get("encoding") == "gzip" else data, dtype=dtype)
    return vol.reshape(sizes, order="F")


def region_voxels(vol, ids, res=25.0, midline=5700.0):
    """Positions (um) of the voxels of the given structure ids: AP, DV and distance from the
    midline (|ML - midline|), both hemispheres pooled."""
    ix = np.argwhere(np.isin(vol, list(ids)))
    return pd.DataFrame({"ap": ix[:, 0] * res, "dv": ix[:, 1] * res, "ml": np.abs(ix[:, 2] * res - midline)})


# ----------------------------------------------------------------------------- reading
'''
assert old in s; s = s.replace(old, new, 1)
open(p,'w').write(s)
EOF
cat > $TMPDIR/peek2.py <<'EOF'
import sys; sys.path.insert(0,'.')
import pickle, numpy as np, kaku, time
assets, files, units, onto, regions = pickle.load(open(sys.argv[1],'rb'))
t=time.time(); vol = kaku.ccf_annotation(); print(vol.shape, vol.dtype, time.time()-t)
ids = onto[onto.acronym.isin(["AMB","AMBd","AMBv"])].id.tolist(); print(ids)
amb = kaku.region_voxels(vol, ids); print(amb.describe().round(0))
u = units.dropna(subset=["ccf_x"]); a = u[u.region.str.contains("ambiguus", case=False, na=False)]
print(len(a), a[["ccf_x","ccf_y","ccf_z"]].describe().round(0))
# check labels agree: annotation at unit positions
ix = np.clip((u[["ccf_z","ccf_y","ccf_x"]].to_numpy()/25).round().astype(int), 0, np.array(vol.shape)-1)
lab = vol[ix[:,0], ix[:,1], ix[:,2]]
idn = dict(zip(onto.id, onto.name))
names = [idn.get(int(l), "?") for l in lab]
norm = lambda n: " ".join(str(n).replace(",", " ").lower().split())
agree = np.mean([norm(a)==norm(b) for a,b in zip(names, u.region)])
print("annotation label equals file label:", agree)
EOF
$TMPDIR/dev/bin/python $TMPDIR/peek2.py $TMPDIR/survey.pkl
```

```
(528, 320, 456) uint32 1.4618773460388184
[135, 939, 143]
            ap      dv      ml
count   2763.0  2763.0  2763.0
mean   11882.0  6618.0  1369.0
std      311.0    78.0    65.0
min    11350.0  6450.0  1225.0
25%    11625.0  6550.0  1325.0
50%    11825.0  6625.0  1375.0
75%    12150.0  6675.0  1425.0
max    12575.0  6750.0  1525.0
87         ccf_x   ccf_y    ccf_z
count    87.0    87.0     87.0
mean   4797.0  6600.0  11829.0
std    1039.0    91.0    355.0
min    4200.0  6480.0  11460.0
25%    4320.0  6520.0  11500.0
50%    4340.0  6600.0  11540.0
75%    4360.0  6670.0  12140.0
max    7060.0  6760.0  12420.0
[... 1 more lines not kept]
```

**Agent calls Bash**

```bash
date -u; cat > $TMPDIR/dev_proc.py <<'EOF'
import sys; sys.path.insert(0,'.')
import pickle, time, resource, kaku
assets, files, units, onto, regions = pickle.load(open(sys.argv[1],'rb'))
n = int(sys.argv[3])
jobs = []
for i, ((sub, ses), g) in enumerate(assets.groupby(["subject", "session"], sort=True)):
    jobs.append(((sub, ses), g.url.iloc[0], dict(zip(g.probe, g.url)), 1000 + i))
step = len(jobs) // n
jobs = jobs[::step][:n]
t = time.time()
res = kaku.run_sessions(jobs, workers=min(n, 5))
print(len(res), "sessions", time.time() - t, "s; maxrss MB", resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1e3)
pickle.dump(res, open(sys.argv[2], "wb"))
EOF
$TMPDIR/dev/bin/python $TMPDIR/dev_proc.py $TMPDIR/survey.pkl $TMPDIR/res2.pkl 2 2>&1 | tail -5
```

```
Tue Nov 17 12:05:45 UTC 2026
2 sessions 40.322470903396606 s; maxrss MB 341.904
```

**Agent calls Bash**

```bash
$TMPDIR/dev/bin/python $TMPDIR/dev_proc.py $TMPDIR/survey.pkl $TMPDIR/res15.pkl 15 2>&1 | tail -3; date -u
```

```
15 sessions 229.02467513084412 s; maxrss MB 366.008
Tue Nov 17 12:10:19 UTC 2026
```

**Agent calls Bash**

```bash
cat > $TMPDIR/runnb.py <<'EOF'
import sys, json, pickle, time, traceback
sys.path.insert(0, '.')
nb = json.load(open('reproduce_kaku_2025.ipynb'))
ns = {}
exec("""import time, warnings
import numpy as np, pandas as pd
from scipy import stats
import kaku
warnings.filterwarnings('ignore')
pd.set_option('display.width', 220); pd.set_option('display.max_columns', 40); pd.set_option('display.max_rows', 200)
t_start = time.time()""", ns)
assets, files, units, onto, regions = pickle.load(open(sys.argv[1], 'rb'))
res = pickle.load(open(sys.argv[2], 'rb'))
ns.update(assets=assets, files=files, units=units, onto=onto, regions=regions, res=res)
only = set(sys.argv[3].split(',')) if len(sys.argv) > 3 else None
for i, c in enumerate(nb['cells']):
    if c['cell_type'] != 'code' or i < 3:
        continue
    src = ''.join(c['source'])
    if 'res = kaku.run_sessions' in src:
        continue
    print(f'==== cell {i} {c["metadata"].get("tags")}')
    t = time.time()
    try:
        exec(src, ns)
    except Exception:
        traceback.print_exc()
    print(f'---- {time.time()-t:.1f}s')
EOF
cd entries/kaku-2025 && timeout 900 $TMPDIR/dev/bin/python $TMPDIR/runnb.py $TMPDIR/survey.pkl $TMPDIR/res15.pkl > $TMPDIR/out0.txt 2>&1; grep -n "Traceback\|Error\|==== cell\|----" $TMPDIR/out0.txt | head -80
```

```
1:==== cell 3 None
3:---- 0.1s
4:==== cell 5 ['sanity']
49:---- 0.0s
50:==== cell 6 ['sanity']
88:---- 0.0s
89:==== cell 8 ['sanity']
106:---- 0.0s
107:==== cell 10 ['sanity']
117:---- 0.0s
118:==== cell 13 ['claim:code-dataset-link']
123:side and bottom DLC jaw and tongue with likelihoods     <- DLC_tracking side- and bottom-facing camera jaw, tongue, lickportTraceback (most recent call last):
128:NameError: name 'jobs' is not defined
133:---- 0.0s
134:==== cell 16 ['claim:units-count']
194:---- 0.1s
195:==== cell 19 ['claim:region-spike-rates']
210:---- 0.0s
211:==== cell 22 ['claim:fig1d-lick-breath-frequencies']
219:---- 0.0s
[... 44 more lines not kept]
```

**Agent calls Bash**

```bash
cat > $TMPDIR/peek3.py <<'EOF'
import pickle, numpy as np
res = pickle.load(open('/tmp/claude-1001/res15.pkl','rb'))
for r in res[:4]:
    lt = r["lick_tips"]
    if not len(lt): continue
    d = lt[:, 2:5] - lt[:, 5:8]
    print(r["key"], len(lt), "tip-jaw pctl per axis:")
    for k in range(3):
        print("  axis", k, np.nanpercentile(d[:, k], [5, 25, 50, 75, 95]).round(1), " tip", np.nanpercentile(lt[:, 2+k], [5,50,95]).round(1))
    # per-trial median tip: if a trial has one target, trial medians cluster
    tr = lt[:,0].astype(int)
    med = np.array([np.nanmedian(lt[tr==t, 2:5], 0) for t in np.unique(tr)])
    for k in range(3):
        h,_ = np.histogram(med[:,k][~np.isnan(med[:,k])], 15); print("  trial-median hist axis",k, h)
    print("  idx3d", r["idx3d_corr"])
EOF
$TMPDIR/dev/bin/python $TMPDIR/peek3.py
```

```
('DL004', '20210308-20210308-180033-s1') 3750 tip-jaw pctl per axis:
  axis 0 [-9.4 -8.4 -7.7 -7.2 -6.1]  tip [-6.4 -4.9 -3.7]
  axis 1 [-16.3 -14.7 -13.6 -12.8 -11.8]  tip [-12.7 -11.6  -9.5]
  axis 2 [36.1 38.  39.7 40.8 41.7]  tip [174.5 178.  179.6]
  trial-median hist axis 0 [  1   0   0   1   6   4  27 101  52  47   3   1   0   3   5]
  trial-median hist axis 1 [ 1  0  0  0  0  0 15 36 41 28 39 42 27 15  7]
  trial-median hist axis 2 [ 1  0  0  1  2  0  9  9 14 22 54 48 45 40  6]
  idx3d {-1: 0.2594730084914349, 0: 0.8530123439615154, 1: 0.2628106913297849}
('DL006', '20210404-20210404-190316-s4') 4976 tip-jaw pctl per axis:
  axis 0 [-7.6 -4.9 -3.9 -2.8 -0.7]  tip [-6.1 -2.7  0.2]
  axis 1 [-18.3 -17.2 -16.2 -15.5 -14.6]  tip [-14.2 -13.  -11.8]
  axis 2 [35.  37.7 39.6 40.6 41.7]  tip [172.7 177.4 178.7]
  trial-median hist axis 0 [ 3  9 14 10 11 22 19 83 29 16  7  5 11  2  1]
  trial-median hist axis 1 [ 4  9 20 30 45 39 33 18 22 14  5  2  0  0  1]
  trial-median hist axis 2 [ 8  4 12 13 13 18  7  7 15 11 44 35 20 17 18]
  idx3d {-1: 0.9620827116612328, 0: 0.37018654930691663, 1: 0.2862640499727756}
('DL010', '20210423-20210423-181024-s8') 1294 tip-jaw pctl per axis:
  axis 0 [-8.  -6.2 -5.5 -4.3 -3.1]  tip [-5.7 -3.5 -1.4]
  axis 1 [-16.9 -15.1 -14.4 -14.  -13.5]  tip [-14.  -12.4 -11.6]
  axis 2 [35.8 37.9 39.1 40.5 41.9]  tip [174.1 176.8 179.4]
[... 12 more lines not kept]
```

**Agent calls Bash**

```bash
python - <<'EOF'
p='kaku.py'; s=open(p).read()
old_start = s.index("    # 3D tongue (bottom) and jaw (side) per good trial, for protrusion and lick angle")
old_end = s.index('    sess["idx3d_corr"] = {o: float(np.mean(v)) if v else np.nan for o, v in chk.items()}\n') + len('    sess["idx3d_corr"] = {o: float(np.mean(v)) if v else np.nan for o, v in chk.items()}\n')
new = '''    # Whether the 3D `idx` field counts trials as the DLC `trial` field does (verifier, round 1):
    # per good trial (the first 60), the largest |correlation| between the bottom-camera DLC
    # tongue x, y and the 3D tongue x, y, z over frames with the tongue visible, with 3D idx =
    # trial + offset. The files differ (notebook), so each session's 3D tracks are read at the
    # offset with the highest correlation.
    bt = bottom["tongue"]
    chk = {o: [] for o in (-1, 0, 1)}
    for t in trials[:60]:
        a = bt[bt["trial"] == t][:N_FRAMES]
        for o in chk:
            b = t3[t3["idx"] == t + o][:N_FRAMES]
            n = min(len(a), len(b))
            vis = a["likelihood"][:n] > 0.95
            if vis.sum() < 20:
                continue
            m = np.corrcoef(np.stack([a["x"][:n][vis], a["y"][:n][vis], b["x"][:n][vis], b["y"][:n][vis], b["z"][:n][vis]]))
            chk[o].append(np.nanmax(np.abs(m[:2, 2:])))
    sess["idx3d_corr"] = {o: float(np.mean(v)) if v else np.nan for o, v in chk.items()}
    off3d = max(chk, key=lambda o: np.nan_to_num(sess["idx3d_corr"][o], nan=-1))
    sess["idx3d_offset"] = off3d
    # 3D tongue (bottom) and jaw (side) per good trial, for protrusion and lick angle
    t3d = np.full((len(trials), N_FRAMES, 3), np.nan)
    j3d = np.full((len(trials), N_FRAMES, 3), np.nan)
    for i, t in enumerate(trials):
        for rec, out in ((t3, t3d), (j3, j3d)):
            sel = rec["idx"] == t + off3d
            if sel.any():
                v = np.stack([rec["x"][sel], rec["y"][sel], rec["z"][sel]], 1)[:N_FRAMES]
                out[i, :len(v)] = v
    sess["tongue3d"] = t3d
    sess["jaw3d"] = j3d
'''
s = s[:old_start] + new + s[old_end:]
s = s.replace('''    out["idx3d_corr"] = sess["idx3d_corr"]
''','''    out["idx3d_corr"] = sess["idx3d_corr"]
    out["idx3d_offset"] = sess["idx3d_offset"]
''')
open(p,'w').write(s)
EOF
grep -n "idx3d" kaku.py
```

```
341:    sess["idx3d_corr"] = {o: float(np.mean(v)) if v else np.nan for o, v in chk.items()}
342:    off3d = max(chk, key=lambda o: np.nan_to_num(sess["idx3d_corr"][o], nan=-1))
343:    sess["idx3d_offset"] = off3d
945:    out["idx3d_corr"] = sess["idx3d_corr"]
946:    out["idx3d_offset"] = sess["idx3d_offset"]
```

**Agent calls Bash**

```bash
python - <<'EOF'
p='kaku.py'; s=open(p).read()
old = '''# ----------------------------------------------------------------------------- per session
'''
new = '''# ----------------------------------------------------------------------------- GLM (ed7, timing only)

GLM_BIN_FRAMES = 5  # Methods: 17 ms bins, five 3.4 ms frames


def glm_design(sess, lag=0):
    """Design of the Methods' GLM for one session and one lag (in 17 ms bins): 3D jaw and tongue
    x, y, z (tongue set to 0 when its likelihood is below 0.05 in both views) and the airflow,
    each z-scored, in 17 ms bins over the first 1470 frames of each good trial; every 5th trial
    is held out. Returns X_train, X_test, train and test trial masks per bin."""
    n_tr = len(sess["trials"])
    nb = N_FRAMES // GLM_BIN_FRAMES
    nf = nb * GLM_BIN_FRAMES

    def binned(a):  # (trials, frames) -> (trials, bins)
        return np.nanmean(a[:, :nf].reshape(n_tr, nb, GLM_BIN_FRAMES), 2)

    lost = (sess["side_tongue_l"] < 0.05) & (sess["bottom_tongue_l"] < 0.05)
    feats = []
    for k in range(3):
        feats.append(binned(sess["jaw3d"][:, :, k]))
        feats.append(binned(np.where(lost, 0.0, sess["tongue3d"][:, :, k])))
    br = sess["breath_move"]
    w = br.shape[1] // nb
    feats.append(br[:, :nb * w].reshape(n_tr, nb, w).mean(2))
    F = np.stack([np.nan_to_num(f) for f in feats], 2)          # trials x bins x 7
    F = (F - F.reshape(-1, 7).mean(0)) / (F.reshape(-1, 7).std(0) + 1e-12)
    F = np.roll(F, lag, axis=1)
    test = (np.arange(n_tr) % 5) == 4
    X = np.concatenate([np.ones((n_tr, nb, 1)), F], 2)
    return X[~test].reshape(-1, 8), X[test].reshape(-1, 8), ~test, test


def glm_counts(spikes, trials_mask):
    """Spike counts of each unit in the GLM's 17 ms bins: bins x units."""
    nb = N_FRAMES // GLM_BIN_FRAMES
    edges = np.arange(nb + 1) * GLM_BIN_FRAMES * FRAME_S
    cols = []
    for sp in spikes:
        cols.append(np.concatenate([np.histogram(s, edges)[0] for s, m in zip(sp, trials_mask) if m]))
    return np.stack(cols, 1).astype(float)


def fit_poisson_batch(X, Y, n_iter=15):
    """Unpenalised Poisson GLM (log link), O8 (a), fitted by Newton's method for all units of a
    session at once: X bins x p, Y bins x units. Returns the weights p x units."""
    p = X.shape[1]
    B = np.zeros((p, Y.shape[1]))
    B[0] = np.log(Y.mean(0) + 1e-6)
    for _ in range(n_iter):
        mu = np.exp(np.clip(X @ B, -20, 20))
        g = X.T @ (Y - mu)
        H = np.einsum("np,nq,nu->upq", X, X, mu) + 1e-6 * np.eye(p)[None]
        B = B + np.linalg.solve(H, g.T[:, :, None])[:, :, 0].T
    return B


# ----------------------------------------------------------------------------- per session
'''
assert old in s; s = s.replace(old, new, 1)
open(p,'w').write(s)
EOF
cat > $TMPDIR/peek4.py <<'EOF'
import sys; sys.path.insert(0,'.')
import pickle, numpy as np, kaku, time
assets, files, units, onto, regions = pickle.load(open(sys.argv[1],'rb'))
g = assets[assets.session==assets.session.iloc[10]]
t=time.time(); sess = kaku.read_session(g.url.iloc[0], dict(zip(g.probe, g.url))); print("read", time.time()-t, sess["idx3d_offset"])
t=time.time(); Xtr, Xte, tr, te = kaku.glm_design(sess, 0); 
sp = [u for pr in sess["probes"].values() for u in pr["spikes"]]
Y = kaku.glm_counts(sp, tr); print(Xtr.shape, Y.shape, time.time()-t)
t=time.time(); B = kaku.fit_poisson_batch(Xtr, Y); print("fit one lag", time.time()-t, np.isfinite(B).all())
EOF
$TMPDIR/dev/bin/python $TMPDIR/peek4.py $TMPDIR/survey.pkl
```

```
entries/kaku-2025/kaku.py:932: RuntimeWarning: Mean of empty slice
  return np.nanmean(a[:, :nf].reshape(n_tr, nb, GLM_BIN_FRAMES), 2)
read 20.376880645751953 0
(80262, 8) (80262, 114) 0.4054229259490967
fit one lag 13.395940065383911 True
```

**Agent calls Bash**

```bash
sed -n 1,200p $TMPDIR/out0.txt | sed -n 107,117p; sed -n 211,300p $TMPDIR/out0.txt
```

```
==== cell 10 ['sanity']
jaw: units with grid MI > 0.6, true pairing 342; their median MI 0.813 true, 0.130 with the next trial's phases; units above 0.6 after the shift: 32
breathing: units with grid MI > 0.6, true pairing 79; their median MI 0.759 true, 0.143 with the next trial's phases; units above 0.6 after the shift: 36

Per subject, units with MI > 0.6, true and shifted pairing:
subject   DL004  DL006  DL010  DL014  DL016  DL018  DL021  DL023  DL024  DL025  DL027  DL029  DL030  DL032  DL033
n_true        3     95     29     20     28     47     43      4     17     15     20      7      1      5      8
n_shift       0      1      5      2      5      2      6      1      5      1      3      1      0      0      0
br_true       2     11      3     10     10      1      4      1      3     20      3      8      1      2      0
br_shift      0      4      7      4      3      3      3      0      3      0      3      0      4      1      1
---- 0.0s
==== cell 22 ['claim:fig1d-lick-breath-frequencies']
              reading  lick mean  lick sd  lick 2.5%  lick 97.5%  breath mean  breath sd  breath 2.5%  breath 97.5%  n licks  n breaths
    (a) within trials      25.82    37.50       1.22      147.06         3.87       1.08         2.28          6.54    76634      76314
(b) within lick bouts       7.99    14.62       3.50       12.25         4.19       0.98         2.63          6.26    32995      16377
(a) within trials {'lick mean': False, 'breath mean': True, 'lick 2.5%': False, 'lick 97.5%': False, 'breath 2.5%': True, 'breath 97.5%': True}
(b) within lick bouts {'lick mean': False, 'breath mean': True, 'lick 2.5%': True, 'lick 97.5%': False, 'breath 2.5%': False, 'breath 97.5%': False}

Per session median frequencies, reading (b): licking [5.43 6.13 6.44] breathing [2.88 3.72 4.79] (5th, 50th, 95th percentiles over sessions)
---- 0.0s
[... 81 more lines not kept]
```

**Agent calls Bash**

```bash
mkdir -p $TMPDIR/cells; cd $TMPDIR/cells
cat > c10b.py <<'EOF'
# Airflow against tongue and jaw (verifier, round 1). Per session, the cross-correlation of the z-scored
# airflow with the tongue-visible indicator and with jaw_y, lags -0.5 to 0.5 s (positive lag: airflow
# later); per subject the mean curve, its largest |r| and the lag of it, and the spread of the session lags.
lags = np.arange(-147, 148) * kaku.FRAME_S
XC = pd.DataFrame([{"subject": r["key"][0], "signal": name, "c": r["xcorr"][name]} for r in res for name in ("tongue", "jaw")])
out = []
for (sub, name), g in XC.groupby(["subject", "signal"]):
    m = np.mean(np.vstack(g.c), 0)
    k = np.argmax(np.abs(m))
    sl = np.array([lags[np.argmax(np.abs(c))] for c in g.c]) * 1000
    out.append({"subject": sub, "signal": name, "sessions": len(g), "r at extreme": m[k], "lag of extreme (ms)": lags[k] * 1000,
                "session lags 25% (ms)": np.percentile(sl, 25), "session lags 75% (ms)": np.percentile(sl, 75)})
XCS = pd.DataFrame(out)
print(XCS.round(3).to_string(index=False))
for name in ("tongue", "jaw"):
    d = XCS[XCS.signal == name]
    print(f"{name}: lag of the subject-mean extreme, median {d['lag of extreme (ms)'].median():.1f} ms, range {d['lag of extreme (ms)'].min():.1f} "
          f"to {d['lag of extreme (ms)'].max():.1f} ms; r at the extreme from {d['r at extreme'].min():.3f} to {d['r at extreme'].max():.3f}, "
          f"positive in {int((d['r at extreme'] > 0).sum())} of {len(d)} subjects")
print("Lag range of the plotted curves: -500 to 500 ms; all points shown.")

# 3D tracking `idx` against the DLC `trial` field (verifier, round 1)
IDX = pd.DataFrame([{"subject": r["key"][0], "session": r["key"][1], **{f"r, offset {o}": v for o, v in r["idx3d_corr"].items()},
                     "offset used": r["idx3d_offset"]} for r in res])
print("\n3D idx = DLC trial + offset; sessions by the offset with the highest correlation:", IDX["offset used"].value_counts().to_dict())
print(IDX[[c for c in IDX.columns if c.startswith("r,")]].describe().round(3).to_string())
print("Subjects by offset used:", IDX.groupby("offset used").subject.apply(lambda s: sorted(set(s))).to_dict())
best = IDX[[c for c in IDX.columns if c.startswith("r,")]].max(1)
print(f"Correlation at the offset used: median {best.median():.3f}, minimum {best.min():.3f}")
EOF
cat > c22.py <<'EOF'
sess = pd.DataFrame([{"subject": r["key"][0], "session": r["key"][1]} for r in res])
def trial_of(t):
    return np.floor(t / kaku.TRIAL_S).astype(int)
def bout_of(t, mt):
    """Index of the code's lick bout holding each time, -1 outside bouts."""
    on, off = mt["bout_on"], mt["bout_off"]
    i = np.searchsorted(on, t, side="right") - 1
    ok = i >= 0
    ok[ok] = t[ok] <= off[i[ok]]
    return np.where(ok, i, -1)
def in_bouts(t, mt):
    return bout_of(np.asarray(t), mt) >= 0
def within_trial_freq(times, bout=None):
    """Inverse intervals between consecutive onsets in the same trial; with bout, both onsets in the
    same lick bout (round 1 corrected this: pairs in two adjacent bouts were counted)."""
    t = np.asarray(times)
    d = np.diff(t)
    same = trial_of(t[:-1]) == trial_of(t[1:])
    if bout is not None:
        same &= (bout[:-1] >= 0) & (bout[:-1] == bout[1:])
    return 1 / d[same & (d > 0)]
lf_a, bf_a, lf_b, bf_b, lf_x = [], [], [], [], []
n_cross = 0
for r in res:
    mt = r["mt"]
    ton, ins = mt["tongue_onset_all"], mt["inspir_onset"]
    bt, bi = bout_of(ton, mt), bout_of(ins, mt)
    lf_a.append(within_trial_freq(ton)); bf_a.append(within_trial_freq(ins))
    lf_b.append(within_trial_freq(ton, bt)); bf_b.append(within_trial_freq(ins, bi))
    # the round-1 version: both onsets in some bout, not necessarily the same one
    inb = bt >= 0
    same = (trial_of(ton[:-1]) == trial_of(ton[1:])) & inb[:-1] & inb[1:]
    lf_x.append(1 / np.diff(ton)[same & (np.diff(ton) > 0)])
    n_cross += int((same & (bt[:-1] != bt[1:])).sum())
rows = []
for name, lf, bf in (("(a) within trials", lf_a, bf_a), ("(b) within lick bouts", lf_b, bf_b)):
    L, B = np.hstack(lf), np.hstack(bf)
    rows.append({"reading": name, "lick mean": L.mean(), "lick sd": L.std(), "lick 2.5%": np.percentile(L, 2.5), "lick 97.5%": np.percentile(L, 97.5),
                 "breath mean": B.mean(), "breath sd": B.std(), "breath 2.5%": np.percentile(B, 2.5), "breath 97.5%": np.percentile(B, 97.5),
                 "n licks": len(L), "n breaths": len(B)})
fq = pd.DataFrame(rows)
print(fq.round(2).to_string(index=False))
exp = {"lick mean": (6.23, .62), "breath mean": (4.02, .4), "lick 2.5%": (3.59, .36), "lick 97.5%": (8.91, .89), "breath 2.5%": (2.12, .21), "breath 97.5%": (7.17, .72)}
for _, r in fq.iterrows():
    print(r.reading, {k: bool(abs(r[k] - v) <= t) for k, (v, t) in exp.items()})
print("\nPer session median frequencies, reading (b): licking", np.round(np.percentile([np.median(x) for x in lf_b if len(x)], [5, 50, 95]), 2),
      "breathing", np.round(np.percentile([np.median(x) for x in bf_b if len(x)], [5, 50, 95]), 2), "(5th, 50th, 95th percentiles over sessions)")
# Diagnostics asked for by the verifier (round 1); they do not decide the outcome.
LX, LA = np.hstack(lf_x), np.hstack(lf_a)
two_frames = 1 / (2 * kaku.FRAME_S)
print(f"\nRound-1 version of (b) (onset pairs in two adjacent bouts counted): {len(LX)} intervals, {n_cross} of them between two bouts; "
      f"lick mean {LX.mean():.2f} Hz, 97.5% {np.percentile(LX, 97.5):.2f} Hz")
print(f"Lick intervals shorter than 2 frames (6.8 ms, > {two_frames:.0f} Hz): {(LA > two_frames).sum()} of {len(LA)} under (a), "
      f"{(np.hstack(lf_b) > two_frames).sum()} of {len(np.hstack(lf_b))} under (b)")
LA2 = LA[LA <= two_frames]
print(f"(a) without intervals under 2 frames: lick mean {LA2.mean():.2f} Hz, 2.5% {np.percentile(LA2, 2.5):.2f}, 97.5% {np.percentile(LA2, 97.5):.2f} Hz (n = {len(LA2)})")
EOF
echo ok
```

```
ok
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/cells
cat > c26.py <<'EOF'
pdl = pd.DataFrame([{"subject": s.subject, "session": s.session, "diff": (r["pd_lick"] or {}).get("diff", np.nan),
                     "n_fast": len((r["pd_lick"] or {}).get("i_fast", [])), "n_slow": len((r["pd_lick"] or {}).get("i_slow", []))}
                    for r, (_, s) in zip(res, sess.iterrows())])
v = pdl.dropna(subset=["diff"])
print(f"Sessions with at least 40 two-lick cycles in each half and a peak in each window: {len(v)} of {len(pdl)} "
      f"({((pdl.n_fast >= 40) & (pdl.n_slow >= 40)).sum()} with enough cycles)")
print("Session peak differences, slow minus fast (s):", v["diff"].describe().round(4).to_dict())
t_a = stats.ttest_1samp(v["diff"], 0)
m = v.groupby("subject")["diff"].mean()
t_b = stats.ttest_1samp(m, 0)
print(f"(a) sessions: mean {v['diff'].mean() * 1000:.1f} ms, t = {t_a.statistic:.2f}, p = {t_a.pvalue:.2e}, n = {len(v)}")
print(f"(b) mice: mean {m.mean() * 1000:.1f} ms, t = {t_b.statistic:.2f}, p = {t_b.pvalue:.2e}, n = {len(m)}")
print("Mice with a positive mean:", int((m > 0).sum()), "of", len(m), "; zero:", int((m == 0).sum()), "; negative:", int((m < 0).sum()))
print("Per mouse mean (ms) and sessions:")
print(pd.DataFrame({"mean_ms": (m * 1000).round(1), "sessions": v.groupby("subject").size()}).T.to_string())
print("Sessions with difference > 0:", int((v['diff'] > 0).sum()), "; = 0:", int((v['diff'] == 0).sum()), "; < 0:", int((v['diff'] < 0).sum()))

def null_report(key, data):
    """Random-split null (verifier, round 1). The fast and slow windows differ, so a peak between their
    starts gives a positive difference with no effect. Per session, the difference for 20 random splits of
    the same cycles into groups of the halves' sizes (kaku.random_split); the session's null value is
    their mean. Data against null, paired over the sessions that have both."""
    rows = []
    for r, (_, s) in zip(res, sess.iterrows()):
        p = r[key] or {}
        nul = np.asarray(p.get("diff_null", []), float)
        rows.append({"subject": s.subject, "session": s.session, "diff": p.get("diff", np.nan),
                     "null": np.nanmean(nul) if np.isfinite(nul).any() else np.nan,
                     "null_first": nul[np.isfinite(nul)][0] if np.isfinite(nul).any() else np.nan,
                     "null_pos": np.mean(nul[np.isfinite(nul)] > 0) if np.isfinite(nul).any() else np.nan})
    N = pd.DataFrame(rows)
    both = N.dropna(subset=["diff", "null"])
    t0 = stats.ttest_1samp(N.null_first.dropna(), 0)
    tp = stats.ttest_rel(both["diff"], both["null"])
    print(f"Null, one random split per session: {N.null_first.notna().sum()} sessions, mean {N.null_first.mean() * 1000:.1f} ms, p = {t0.pvalue:.2e} (t-test against 0)")
    print(f"Null, mean of 20 splits per session: mean {N.null.mean() * 1000:.1f} ms; share of splits above 0, median over sessions {N.null_pos.median():.2f}")
    print(f"Data minus null over {len(both)} sessions: mean {(both['diff'] - both['null']).mean() * 1000:.1f} ms, paired t-test p = {tp.pvalue:.2e}; "
          f"data above null in {int((both['diff'] > both['null']).sum())}")
    mm = both.groupby("subject")[["diff", "null"]].mean()
    tm = stats.ttest_rel(mm["diff"], mm["null"]) if len(mm) > 2 else None
    print(f"Mice: data above null in {int((mm['diff'] > mm['null']).sum())} of {len(mm)}; paired t-test p = {tm.pvalue if tm else np.nan:.2e}")
    return N
NL1g = null_report("pd_lick", v)
EOF
cat > c30add.py <<'EOF'
NL1i = null_report("pd_breath", None)
EOF
echo
```

```
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd entries/kaku-2025; python -c "
import json;nb=json.load(open('reproduce_kaku_2025.ipynb'))
for i in [24,30,56,58]:
  print('----',i); print(''.join(nb['cells'][i]['source']))
"
```

```
---- 24
rows = []
lat_by_n = []
for r, (_, s) in zip(res, sess.iterrows()):
    mt = r["mt"]
    ton = mt["tongue_onset_all"]
    # protrusion intervals: each tongue onset to the first offset after it (code onsets and offsets)
    off = np.sort(mt["tongue_offset"])
    j = np.searchsorted(off, ton, side="right")
    ok = j < len(off)
    on_i, off_i = ton[ok], off[j[ok]]
    ins = mt["inspir_onset"]
    ins_b = ins[in_bouts(ins, mt)]
    k = np.searchsorted(on_i, ins_b, side="right") - 1
    inside = (k >= 0) & (ins_b <= off_i[np.clip(k, 0, None)]) & (ins_b >= on_i[np.clip(k, 0, None)])
    rows.append({"subject": s.subject, "session": s.session, "inspirations in bouts": len(ins_b), "within protrusion": int(inside.sum())})
pr = pd.DataFrame(rows)
pr["fraction"] = pr["within protrusion"] / pr["inspirations in bouts"]
print("Per session fraction of in-bout inspiration onsets that fall inside a tongue protrusion:")
print(pr.fraction.describe().round(4).to_string())
[... 65 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/cells
cat > c32.py <<'EOF'
# Extended Data Fig 1d-i: unidirectional models, simulated as the Methods describe.
# Inter-breath intervals come from fig1d reading (a) and inter-lick intervals from reading (b): for each
# rhythm the reading whose values are closest to the paper's Fig 1d (fig1d above).
rng = np.random.default_rng(11)
ibi_emp = 1 / np.hstack(bf_a)          # inter-breath intervals within trials (fig1d reading (a))
ili_emp = 1 / np.hstack(lf_b)          # inter-lick intervals within one lick bout (fig1d reading (b))
ili_range = np.percentile(ili_emp, [2.5, 97.5])
ibi_range = np.percentile(ibi_emp, [2.5, 97.5])
lat_ll = lat.lat.median() if lat.lat.notna().any() else np.nan       # last lick -> next inspiration
# last inspiration -> next lick, from the breath-to-lick cycles of the data
lat_il = []
for r in res:
    mt = r["mt"]
    ton, ins = mt["tongue_onset"], mt["inspir_onset"]
    tb = ton[in_bouts(ton, mt)]
    k = np.searchsorted(ins, tb) - 1
    ok = k >= 0
    lat_il.append(tb[ok] - ins[k[ok]])
lat_il = np.median(np.hstack(lat_il))
print(f"Empirical ranges: inter-lick {ili_range.round(3)} s, inter-breath {ibi_range.round(3)} s; latencies: last lick -> inspiration {lat_ll:.3f} s, inspiration -> next lick {lat_il:.3f} s")

def sim_breath_driven(n_breaths):
    ins = np.cumsum(rng.choice(ibi_emp, n_breaths))
    licks = np.sort(ins - lat_ll)
    out = [licks[0]]
    for a, b in zip(licks[:-1], licks[1:]):
        gap = b - a
        k = int(np.ceil(gap / ili_range[1])) - 1 if gap > ili_range[1] else 0
        out += list(a + gap * np.arange(1, k + 1) / (k + 1)) + [b]
    licks = np.sort(np.array(out) + rng.normal(0, 0.01, len(out)))
    return licks, ins

def sim_lick_driven(n_licks):
    licks = np.cumsum(rng.choice(ili_emp, n_licks))
    cand = licks - lat_il
    ins = [cand[0]]
    for c in cand[1:]:
        if ibi_range[0] <= c - ins[-1]:
            ins.append(c)
    ins = np.array(ins) + rng.normal(0, 0.01, len(ins))
    return licks, np.sort(ins)

def measures(licks, ins):
    mt = {"tongue_onset": licks, "inspir_onset": ins, "bout_on": np.array([licks[0]]), "bout_off": np.array([licks[-1]])}
    a = kaku.peak_diff_lick_behv(mt) or {}
    b = kaku.peak_diff_breath_behv(mt) or {}
    return {"fig1g": a.get("diff", np.nan), "fig1i": b.get("diff", np.nan),
            "two-lick fast": len(a.get("i_fast", [])), "two-lick slow": len(a.get("i_slow", [])),
            "fast peak": len(a.get("peaks_fast", [])) > 0, "slow peak": len(a.get("peaks_slow", [])) > 0}

sim, diag = [], []
for r in res:
    mt = r["mt"]
    nb = int(in_bouts(mt["inspir_onset"], mt).sum()); nl = int(in_bouts(mt["tongue_onset"], mt).sum())
    if nb < 50:
        continue
    mb = measures(*sim_breath_driven(nb))
    ml = measures(*sim_lick_driven(nl))
    sim.append({"breath_model_fig1g": mb["fig1g"], "breath_model_fig1i": mb["fig1i"], "lick_model_fig1g": ml["fig1g"], "lick_model_fig1i": ml["fig1i"]})
    diag.append({**{f"breath model {k}": v for k, v in mb.items() if k not in ("fig1g", "fig1i")},
                 **{f"lick model {k}": v for k, v in ml.items() if k not in ("fig1g", "fig1i")}})
sim = pd.DataFrame(sim); diag = pd.DataFrame(diag)
for col in sim.columns:
    v_ = sim[col].dropna()
    tt = stats.ttest_1samp(v_, 0) if len(v_) > 2 and v_.std() > 0 else None
    print(f"{col}: sessions with a value {len(v_)} of {len(sim)}, mean {v_.mean() * 1000 if len(v_) else np.nan:.1f} ms, "
          f"SD {v_.std() * 1000 if len(v_) > 1 else np.nan:.1f} ms, p = {tt.pvalue if tt else np.nan:.3g}")
print(f"Data: Fig 1g mean {v['diff'].mean() * 1000:.1f} ms (p = {t_a.pvalue:.2e}); Fig 1i mean {v2['diff'].mean() * 1000:.1f} ms (p = {t_a2.pvalue:.2e})")
# Why the Fig 1g measure is mostly missing in the licking-driven model (verifier, round 1)
for mdl in ("lick model", "breath model"):
    nf, ns = diag[f"{mdl} two-lick fast"], diag[f"{mdl} two-lick slow"]
    enough = (nf >= 40) & (ns >= 40)
    print(f"{mdl}: two-lick cycles per half, median {nf.median():.0f} (fast) and {ns.median():.0f} (slow); sessions with >= 40 in both "
          f"{int(enough.sum())} of {len(diag)}; of those, a peak in the fast window {int(diag.loc[enough, f'{mdl} fast peak'].sum())}, "
          f"in the slow window {int(diag.loc[enough, f'{mdl} slow peak'].sum())}")
EOF
cat > c34.py <<'EOF'
# Extended Data Fig 1b-c: lick probability around swallows and around expirations inside bouts
bins = np.arange(-0.3, 0.3 + 1e-9, kaku.FRAME_S)
rows, tr_sw, tr_ex = [], [], []
for r, (_, s) in zip(res, sess.iterrows()):
    sw = r["swallow_times"]
    if len(sw) < 20:
        continue
    mt = r["mt"]
    ton = mt["tongue_onset_all"]
    ex = r["expir_onset"]
    ex = ex[in_bouts(ex, mt)]
    def prob(ev):
        h = np.zeros(len(bins) - 1)
        for e in ev:
            h += np.histogram(ton - e, bins)[0]
        return h / max(len(ev), 1)
    ps, pe = prob(sw), prob(ex)
    tr_sw.append(ps); tr_ex.append(pe)
    c = bins[:-1]
    w = (c >= 0) & (c < 0.1)
    rows.append({"subject": s.subject, "session": s.session, "swallows": len(sw), "expirations": len(ex),
                 "p_swallow": ps[w].mean(), "p_expiration": pe[w].mean()})
lp = pd.DataFrame(rows)
wt = stats.wilcoxon(lp.p_swallow, lp.p_expiration)
print(f"Sessions with >= 20 swallows: {len(lp)}; lick probability per 3.4 ms bin, 0 to 100 ms after onset:")
print(lp[["p_swallow", "p_expiration"]].describe().round(4).to_string())
print(f"Lower around swallows in {int((lp.p_swallow < lp.p_expiration).sum())} of {len(lp)} sessions; Wilcoxon signed-rank p = {wt.pvalue:.2e}")
print("Median ratio swallow / expiration:", round(float((lp.p_swallow / lp.p_expiration).median()), 3))
# The whole trace from -300 to 300 ms (verifier, round 1): mean over sessions, in 30 ms steps (each the
# mean of the 3.4 ms bins whose start falls in it)
c = bins[:-1]
steps = np.arange(-0.3, 0.3, 0.03)
TS, TE = np.mean(tr_sw, 0), np.mean(tr_ex, 0)
trace = pd.DataFrame({"from (ms)": (steps * 1000).round(0).astype(int),
                      "swallow": [TS[(c >= a) & (c < a + 0.03)].mean() for a in steps],
                      "expiration": [TE[(c >= a) & (c < a + 0.03)].mean() for a in steps]})
print("\nLick probability per 3.4 ms bin, mean over sessions:")
print(trace.round(4).T.to_string(header=False))
print(f"Minimum of the swallow trace: {TS.min():.4f} at {c[np.argmin(TS)] * 1000:.0f} ms; of the expiration trace: {TE.min():.4f} at {c[np.argmin(TE)] * 1000:.0f} ms")
EOF
cat > c38.py <<'EOF'
def delta_tests(df, label):
    rows = []
    for name, d in readings(df).items():
        for q, col in (("Delta(1,-1)", "d1"), ("Delta(0,-1)", "d0")):
            x = (d.c1 - d.cm1) if col == "d1" else (d.c0 - d.cm1)
            t = stats.ttest_1samp(x, 0)
            rows.append({"events": label, "reading": name, "quantity": q, "n": len(x), "mean_ms": x.mean() * 1000, "p": t.pvalue})
    d = readings(df)["(a) code: longest third of cycle 0"]
    for q in ("Delta(1,-1)", "Delta(0,-1)"):
        x = (d.c1 - d.cm1) if q == "Delta(1,-1)" else (d.c0 - d.cm1)
        sm = x.groupby(d.session.to_numpy()).mean()
        t = stats.ttest_1samp(sm, 0)
        rows.append({"events": label, "reading": "(d) (a) with session means", "quantity": q, "n": len(sm), "mean_ms": sm.mean() * 1000, "p": t.pvalue})
    return pd.DataFrame(rows)
DL = delta_tests(SWL, "licks")
print(DL.round(4).to_string(index=False))

def cycle_report(df, max_c0, label):
    """Distributions of cycles -1, 0 and 1 under O5 (a) (verifier, round 1). The code limits cycle 0 to
    max_c0 and sets no limit on cycle 1, so a pause after the swallow enters Delta(1,-1)."""
    d = readings(df)["(a) code: longest third of cycle 0"]
    q = pd.DataFrame({k: (d[c] * 1000).quantile([0.05, 0.25, 0.5, 0.75, 0.95]) for k, c in (("cycle -1", "cm1"), ("cycle 0", "c0"), ("cycle 1", "c1"))})
    print(f"\n{label}, O5 (a), cycle quantiles (ms):")
    print(q.round(1).T.to_string())
    long1 = d.c1 > max_c0
    print(f"Cycle 1 longer than {max_c0 * 1000:.0f} ms (the cycle-0 limit): {int(long1.sum())} of {len(d)} ({long1.mean():.1%}); "
          f"cycle -1 longer: {int((d.cm1 > max_c0).sum())}")
    x = (d.c1 - d.cm1)[~long1]
    t = stats.ttest_1samp(x, 0)
    print(f"Diagnostic, not a reading: Delta(1,-1) without those events {x.mean() * 1000:.1f} ms (n = {len(x)}, p = {t.pvalue:.2e}); "
          f"median Delta(1,-1) over all events {(d.c1 - d.cm1).median() * 1000:.1f} ms")
cycle_report(SWL, 1 / 3, "Licks")
EOF
cat > c40.py <<'EOF'
DB = delta_tests(SWB, "breaths")
print(DB.round(4).to_string(index=False))
cycle_report(SWB, 1 / 2, "Breaths")
EOF
echo
```

```
Shell cwd was reset to
```

**Agent**

Now the region cell (CCF annotation), fig4e/f, fig4d, ed8i and ed7 cells.

**Agent calls Bash**

```bash
cd $TMPDIR/cells
cat > c48.py <<'EOF'
# Regions the CCF does not label (claims file O3), built from the Allen CCFv3 annotation volume (2017, 25 um;
# kaku.CCF_ANNOTATION_URL), as the verifier asked in round 1. Round 1 built them from the positions of the
# units the files label; both are printed.
vol = kaku.ccf_annotation()
def ids_under(acr):
    i = int(onto.loc[onto.acronym == acr, "id"].iloc[0])
    return onto[onto.structure_id_path.astype(str).str.contains(f"/{i}/")].id.astype(int).tolist()
# check: the annotation at each good unit's CCF position (nearest voxel) against the file's region name
norm = lambda n: " ".join(str(n).replace(",", " ").lower().split())
name_of = dict(zip(onto.id.astype(int), onto.name))
g_ = T.dropna(subset=["ccf_x"])
ix = np.clip((g_[["ccf_z", "ccf_y", "ccf_x"]].to_numpy() / 25).round().astype(int), 0, np.array(vol.shape) - 1)
lab = vol[ix[:, 0], ix[:, 1], ix[:, 2]]
agree = np.mean([norm(name_of.get(int(l), "")) == norm(r) for l, r in zip(lab, g_.region)])
print(f"Annotation volume {vol.shape} (AP, DV, ML); its label at the unit's position equals the file's region name for {agree:.1%} of {len(g_)} good units")
amb = kaku.region_voxels(vol, ids_under("AMB"))
nts = kaku.region_voxels(vol, ids_under("NTS"))
irn = kaku.region_voxels(vol, ids_under("IRN"))
T["ml"] = (T.ccf_x - 5700).abs()
T["apb"] = (T.ccf_z // 100).astype("Int64")
amb_bin = amb.assign(apb=amb.ap // 100).groupby("apb").agg(ml_lo=("ml", "min"), ml_hi=("ml", "max"), dv_lo=("dv", "min"), dv_hi=("dv", "max"))
nts_edge = nts.assign(apb=nts.ap // 100).groupby("apb").ml.max()
print(f"AMB in the annotation: AP {amb.ap.min():.0f} to {amb.ap.max():.0f}, |ML| {amb.ml.min():.0f} to {amb.ml.max():.0f}, DV {amb.dv.min():.0f} to {amb.dv.max():.0f} um "
      f"({len(amb)} voxels, both sides)")
allu = units.dropna(subset=["ccf_x"])
amb_u = allu[allu.acronym.isin(["AMB", "AMBd", "AMBv"])]
print(f"Round 1, from the {len(amb_u)} AMB-labelled units: AP {amb_u.ccf_z.min():.0f} to {amb_u.ccf_z.max():.0f}, |ML| {(amb_u.ccf_x - 5700).abs().min():.0f} to "
      f"{(amb_u.ccf_x - 5700).abs().max():.0f}, DV {amb_u.ccf_y.min():.0f} to {amb_u.ccf_y.max():.0f} um")
irn_ap_mid = (irn.ap.min() + irn.ap.max()) / 2; irn_dv_mid = (irn.dv.min() + irn.dv.max()) / 2
print(f"IRN in the annotation: AP {irn.ap.min():.0f} to {irn.ap.max():.0f} (midpoint {irn_ap_mid:.0f}), DV {irn.dv.min():.0f} to {irn.dv.max():.0f} (midpoint {irn_dv_mid:.0f}) um")
ab = T.apb.map(lambda b: amb_bin.loc[b] if b in amb_bin.index else None)
A = pd.DataFrame([x if x is not None else pd.Series({"ml_lo": np.nan, "ml_hi": np.nan, "dv_lo": np.nan, "dv_hi": np.nan}) for x in ab], index=T.index)
in_amb_col = A.ml_lo.notna() & (T.ml >= A.ml_lo) & (T.ml <= A.ml_hi)
def prebotc(d):
    """Within d um ventral of AMB's ventral edge, inside AMB's ML extent, in the same 100 um AP step."""
    return (in_amb_col & (T.ccf_y > A.dv_hi) & (T.ccf_y <= A.dv_hi + d)).to_numpy()
def above_amb(d):
    return (in_amb_col & (T.ccf_y < A.dv_lo) & (T.ccf_y >= A.dv_lo - d)).to_numpy()
pv_irn = (T.in_IRN & (T.ccf_z > irn_ap_mid) & (T.ccf_y > irn_dv_mid)).to_numpy()
pd_irn_parn = ((T.in_IRN | T.in_PARN) & (T.ccf_z > irn_ap_mid) & (T.ccf_y < irn_dv_mid)).to_numpy()
def lateral_nts(d):
    """Beyond NTS's lateral edge in the same 100 um AP step, within d um."""
    e = T.apb.map(nts_edge).astype(float)
    return (e.notna() & (T.ml > e) & (T.ml <= e + d) & ~T.in_NTS).to_numpy()
PM = (T.in_P | T.in_MY).to_numpy()
for d in (300, 500):
    print(f"d = {d} um: good units near preBotC {prebotc(d).sum()}, above AMB {above_amb(d).sum()}, lateral of NTS {lateral_nts(d).sum()}")
print("posterior-ventral IRN:", pv_irn.sum(), "; posterior-dorsal IRN/PARN:", pd_irn_parn.sum(), "; pons and medulla:", PM.sum())

def enrich(sel, flag, base):
    a = int((sel & flag).sum()); b = int((sel & ~flag).sum())
    c = int((base & flag).sum()); d_ = int((base & ~flag).sum())
    p = stats.fisher_exact([[a, b], [c, d_]], alternative="greater")[1] if a + b > 0 else np.nan
    return {"n": a + b, "tuned": a, "fraction": a / (a + b) if a + b else np.nan, "base fraction": c / (c + d_), "p": p}

rows = []
for order, sig in ((4, "a"), (4, "b"), (2, "a"), (2, "b"), (5, "code")):
    B = tuned("br", order, sig)
    for d in (300, 500):
        rows.append({"tuning": f"order {order}, {sig}", "region": f"preBotC ({d} um)", **enrich(prebotc(d), B, PM)})
    rows.append({"tuning": f"order {order}, {sig}", "region": "posterior ventral IRN", **enrich(pv_irn, B, PM)})
BL = pd.DataFrame(rows)
print(BL.round(4).to_string(index=False))
EOF
cat > c62.py <<'EOF'
# Figure 4e-f: unit peak differences; O1 unit readings, O2 recording readings, V2 orders 4 and 2.
# Each unit also has the difference for one random split of its cycles (null, verifier round 1), and licking
# units the difference for the code's 40 cycles nearest the median on each side ("code selection").
two_probe = files.groupby(["subject", "session"]).probe.nunique()
two_probe = set(two_probe[two_probe == 2].index.get_level_values(1))
def sim_sessions(Lm, Bm, d):
    """Sessions with two probes, one holding licking units in posterior-dorsal IRN/PARN and the other
    breathing units near the preBotC (O2 (b), O3)."""
    pre = prebotc(d)
    out = {}
    for ses in two_probe:
        s = (T.session == ses).to_numpy()
        lick_p = set(T.loc[s & Lm & pd_irn_parn, "probe"]); br_p = set(T.loc[s & Bm & pre, "probe"])
        pairs = [(a, b) for a in lick_p for b in br_p if a != b]
        if pairs:
            out[ses] = pairs
    return out
O1 = {"(a) MI > 0.6, P < 0.001": dict(mi_thr=0.6), "(b) MI > 0.9, P < 0.001": dict(mi_thr=0.9), "(c) MI > 0.9 alone": dict(mi_thr=0.9, sig=None)}
rows = []
for order in (4, 2):
    for oname, kw in O1.items():
        sig = kw.get("sig", "a")
        for sname in (["a", "b"] if sig is not None else [None]):
            L = tuned("jaw", order, sname, mi_thr=kw["mi_thr"]); B = tuned("br", order, sname, mi_thr=kw["mi_thr"])
            for which, Um, col in (("fig4e licking units", L, "pd_lick_unit"), ("fig4f breathing units", B, "pd_breath_unit")):
                for o2 in ("(a) all sessions", "(b) simultaneous, 300 um", "(b) simultaneous, 500 um"):
                    m = Um.copy()
                    if o2.startswith("(b)"):
                        ss = sim_sessions(L, B, 300 if "300" in o2 else 500)
                        region = pd_irn_parn if which.startswith("fig4e") else prebotc(300 if "300" in o2 else 500)
                        m = m & T.session.isin(ss.keys()).to_numpy() & region
                    x = T.loc[m, col].dropna()
                    nl_ = T.loc[m, col + "_null"]
                    both = T.loc[m, [col, col + "_null"]].dropna()
                    tt = stats.ttest_1samp(x, 0) if len(x) > 2 else None
                    tn = stats.ttest_1samp(nl_.dropna(), 0) if nl_.notna().sum() > 2 else None
                    tp = stats.ttest_rel(both[col], both[col + "_null"]) if len(both) > 2 else None
                    row = {"claim": which, "order": order, "O1": oname, "V3": sname, "O2": o2, "units": len(x),
                           "mean_ms": x.mean() * 1000 if len(x) else np.nan, "p": tt.pvalue if tt else np.nan,
                           "positive": int((x > 0).sum()), "negative": int((x < 0).sum()),
                           "null_mean_ms": nl_.mean() * 1000, "null_p": tn.pvalue if tn else np.nan,
                           "data-null_ms": (both[col] - both[col + "_null"]).mean() * 1000 if len(both) else np.nan,
                           "paired_p": tp.pvalue if tp else np.nan}
                    if col == "pd_lick_unit":
                        xc = T.loc[m, "pd_lick_unit_code"].dropna()
                        row["code_sel_mean_ms"] = xc.mean() * 1000 if len(xc) else np.nan
                        row["code_sel_p"] = stats.ttest_1samp(xc, 0).pvalue if len(xc) > 2 else np.nan
                    rows.append(row)
PDU = pd.DataFrame(rows)
print(PDU.round(4).to_string(index=False))
EOF
cat > c64.py <<'EOF'
rows = []
for order in (4, 2):
    for oname, kw in O1.items():
        for sname in (["a", "b"] if kw.get("sig", "a") is not None else [None]):
            L = tuned("jaw", order, sname, mi_thr=kw["mi_thr"]); B = tuned("br", order, sname, mi_thr=kw["mi_thr"])
            for d in (300, 500):
                ss = sim_sessions(L, B, d)
                nl, nb = [], []
                for ses, pairs in ss.items():
                    s = (T.session == ses).to_numpy()
                    a, b = pairs[0]
                    nl.append(int((s & L & pd_irn_parn & (T.probe == a).to_numpy()).sum()))
                    nb.append(int((s & B & prebotc(d) & (T.probe == b).to_numpy()).sum()))
                mice = {T.loc[T.session == ses, "subject"].iloc[0] for ses in ss}
                rows.append({"order": order, "O1": oname, "V3": sname, "O3": f"{d} um", "recordings": len(ss), "mice": len(mice),
                             "licking units per recording": f"{min(nl) if nl else 0}-{max(nl) if nl else 0}",
                             "breathing units per recording": f"{min(nb) if nb else 0}-{max(nb) if nb else 0}"})
print(pd.DataFrame(rows).to_string(index=False))
print("Paper: 43 recordings (+-4) in 21 mice (+-2); 1-28 licking and 1-12 breathing units per recording")
print("Two-probe sessions in the dandiset:", len(two_probe), "in", files[files.session.isin(two_probe)].subject.nunique(), "mice")
# Regardless of tuning (verifier, round 1): two-probe sessions with any good unit near the preBotC on one probe
# and any good unit in the posterior-dorsal IRN/PARN on the other
allm = np.ones(len(T), bool)
for d in (300, 500):
    ss = sim_sessions(allm, allm, d)
    mice = {T.loc[T.session == ses, "subject"].iloc[0] for ses in ss}
    print(f"O3 {d} um, any good units: {len(ss)} two-probe sessions in {len(mice)} mice")
EOF
cat > c_ed8i.py <<'EOF'
# Extended Data Fig 8i, the part that can be run (verifier, round 1). The 3D tracking states no axes or
# sign, so which licks are ipsilateral cannot be fixed (blocked, metadata_insufficient). Without the sign,
# one can still ask whether the lick-side preference differs between the hemispheres (two-sided). Since the
# lateral axis is not named either, both horizontal-looking axes of the 3D tongue track (x, y) are tried.
# Licks are split at the session median of the coordinate, a stand-in for the midline (O9 (b)), or of the
# tip minus the jaw's position before the lick (O9 (a)); per licking unit (O1 (a), order 4, V3 (a)) the rate
# from -50 to 100 ms around lick onset on one side minus the other (kaku.process_session, lick_counts).
lc = {}
for r in res:
    for probe, us in r["units"].items():
        for u in us:
            if "lick_counts" in u:
                lc[(r["key"][1], probe, u["unit_index"])] = u["lick_counts"]
tips = {r["key"][1]: r["lick_tips"] for r in res}
Lu = T[tuned("jaw", 4, "a")]
rows = []
for axis, an in ((0, "x"), (1, "y")):
    for o9 in ("(a) tip minus jaw", "(b) tip"):
        dif, hem = [], []
        for u in Lu.itertuples():
            c = lc.get((u.session, u.probe, u.pos)); lt = tips.get(u.session)
            if c is None or lt is None or not len(lt):
                continue
            x = lt[:, 2 + axis] - (lt[:, 5 + axis] if o9.startswith("(a)") else 0)
            mid = np.nanmedian(x)
            hi, lo = x > mid, x < mid
            if hi.sum() < 10 or lo.sum() < 10:
                continue
            dif.append((c[hi].mean() - c[lo].mean()) / 0.15); hem.append(u.hemi)
        dif, hem = np.array(dif), np.array(hem)
        l_, r_ = dif[hem == "left"], dif[hem == "right"]
        mw = stats.mannwhitneyu(l_, r_, alternative="two-sided") if len(l_) and len(r_) else None
        rows.append({"axis": an, "O9": o9, "units left": len(l_), "units right": len(r_),
                     "median left (spikes/s)": np.median(l_) if len(l_) else np.nan, "median right": np.median(r_) if len(r_) else np.nan,
                     "Mann-Whitney p, two-sided": mw.pvalue if mw else np.nan})
print(pd.DataFrame(rows).round(4).to_string(index=False))
print("Hemisphere from ccf_x against the 5,700 um midline; the files' left/right text is opposite in 99.3% of units (data check).")
EOF
cat > c_ed7.py <<'EOF'
# ed7: cost of the Methods' GLM, measured on one session (verifier, round 1). Reading O8 (a), log link, one
# lag: all good units of the session fitted at once by Newton's method (kaku.fit_poisson_batch).
keys_ = sorted(assets.groupby(["subject", "session"]).groups.keys())
sub_, ses_ = keys_[10]
g_ = assets[(assets.subject == sub_) & (assets.session == ses_)]
t0_ = time.time()
S_ = kaku.read_session(g_.url.iloc[0], dict(zip(g_.probe, g_.url)))
t_read = time.time() - t0_
Xtr, Xte, trm, tem = kaku.glm_design(S_, 0)
Y_ = kaku.glm_counts([u for pr in S_["probes"].values() for u in pr["spikes"]], trm)
t0_ = time.time()
W_ = kaku.fit_poisson_batch(Xtr, Y_)
t_fit = time.time() - t0_
per = t_fit / Y_.shape[1]
n_all = int(units.good.sum())
est_a = per * n_all * 11
print(f"Session {sub_} {ses_}: {Y_.shape[1]} units, {Xtr.shape[0]} training bins of 17 ms, {Xtr.shape[1]} regressors; read in {t_read:.0f} s, "
      f"one lag fitted in {t_fit:.1f} s ({per:.3f} s per unit); weights finite: {bool(np.isfinite(W_).all())}")
print(f"O8 (a), log link, 11 lags, {n_all} units: about {est_a / 3600:.1f} CPU hours; with the logit link as well {2 * est_a / 3600:.1f}; "
      f"O8 (b) adds 5 penalty values per unit and link, each at least one such fit: at least {12 * est_a / 3600:.1f} CPU hours in all, "
      f"against a 60-minute limit for the notebook on 4 CPUs")
del S_, Xtr, Xte, Y_
EOF
echo
```

```
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/cells && python - <<'EOF'
s=open('c48.py').read()
old = '''ab = T.apb.map(lambda b: amb_bin.loc[b] if b in amb_bin.index else None)
A = pd.DataFrame([x if x is not None else pd.Series({"ml_lo": np.nan, "ml_hi": np.nan, "dv_lo": np.nan, "dv_hi": np.nan}) for x in ab], index=T.index)
'''
new = '''A = amb_bin.reindex(T.apb.astype(float).to_numpy()).set_index(T.index)
'''
assert old in s; s=s.replace(old,new)
s=s.replace('e = T.apb.map(nts_edge).astype(float)', 'e = pd.Series(nts_edge.reindex(T.apb.astype(float).to_numpy()).to_numpy(), index=T.index)')
open('c48.py','w').write(s)
EOF
cat > $TMPDIR/apply.py <<'EOF'
import json, sys
P = 'entries/kaku-2025/reproduce_kaku_2025.ipynb'
C = '/tmp/claude-1001/cells/'
nb = json.load(open(P))
def src(i): return ''.join(nb['cells'][i]['source'])
def find(prefix):
    hits = [i for i, c in enumerate(nb['cells']) if ''.join(c['source']).startswith(prefix)]
    assert len(hits) == 1, (prefix, hits); return hits[0]
def lines(t): 
    l = t.rstrip('\n').split('\n'); return [x + '\n' for x in l[:-1]] + [l[-1]]
def setc(i, text): nb['cells'][i]['source'] = lines(text)
def code(text, tags=None):
    return {"cell_type": "code", "execution_count": None, "metadata": {"tags": tags} if tags else {}, "outputs": [], "source": lines(text)}
def md(text): return {"cell_type": "markdown", "metadata": {}, "source": lines(text)}
r = lambda f: open(C + f).read()
# replacements
setc(find('sess = pd.DataFrame([{"subject": r["key"][0], "session": r["key"][1]} for r in res])'), r('c22.py'))
setc(find('pdl = pd.DataFrame('), r('c26.py'))
i = find('pdb = pd.DataFrame('); setc(i, src(i).rstrip('\n') + '\n' + r('c30add.py'))
setc(find('# Extended Data Fig 1d-i'), r('c32.py'))
setc(find('# Extended Data Fig 1b-c'), r('c34.py'))
setc(find('def delta_tests'), r('c38.py'))
setc(find('DB = delta_tests'), r('c40.py'))
setc(find('# Regions the CCF does not label'), r('c48.py'))
setc(find('# Figure 4e-f'), r('c62.py'))
i = find('rows = []\nfor oname, kw in O1.items():'); setc(i, r('c64.py'))
# insertions (from the end so indices hold)
i = find('# Clock check.')
nb['cells'].insert(i + 1, code(r('c10b.py'), ['sanity']))
i = find('rows = []\nfor v4, col in (("V4(a)", "sw_mod_a")')  # ed6e
j = i + 1  # its conclusion
nb['cells'].insert(j + 1, md('## ed7-glm-separate-clusters\n\n> A GLM on the tracked features found separate clusters of units predicted by licking or by breathing movements.\n\nBlocked, too_large. The cell below measures the cost of the GLM on one session.'))
nb['cells'].insert(j + 2, code(r('c_ed7.py'), ['claim:ed7-glm-separate-clusters']))
i = find('def circ_median')  # ed8e
nb['cells'].insert(i + 2, md('## ed8i-ipsilateral-lick-selectivity\n\n> Licking-related neurons showed selectivity for ipsilateral licking, while individual units within each hemisphere had diverse direction preferences, including the center direction.\n\nBlocked, metadata_insufficient; the cell below runs the part that needs no left-right sign.'))
nb['cells'].insert(i + 3, code(r('c_ed8i.py'), ['claim:ed8i-ipsilateral-lick-selectivity']))
json.dump(nb, open(P, 'w'), indent=1, ensure_ascii=False)
open(P, 'a').write('\n')
print('ok', len(nb['cells']))
EOF
cd  && git diff --stat entries/kaku-2025/reproduce_kaku_2025.ipynb; head -c 300 entries/kaku-2025/reproduce_kaku_2025.ipynb; tail -c 200 entries/kaku-2025/reproduce_kaku_2025.ipynb
```

```
{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "452f3297",
   "metadata": {},
   "source": [
    "# Reproducing Kaku, Liu et al. (2025) from dandiset 001619\n",
    "\n",
    "Paper. Kaku H, Liu LD, Gao R, West S, Liao S-M, Finkelstein A, Kleinfeld D, Thomas A, Tipparaju SL,\n",
    "Svobodawhere the paper reports 339."
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  }
[... 4 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && cp entries/kaku-2025/reproduce_kaku_2025.ipynb nb_backup.ipynb && python - <<'EOF'
s=open('/tmp/claude-1001/apply.py').read()
s=s.replace('''def code(text, tags=None):
    return {"cell_type": "code", "execution_count": None, "metadata": {"tags": tags} if tags else {}, "outputs": [], "source": lines(text)}
def md(text): return {"cell_type": "markdown", "metadata": {}, "source": lines(text)}''','''import uuid
def code(text, tags=None):
    return {"cell_type": "code", "execution_count": None, "id": uuid.uuid4().hex[:8], "metadata": {"tags": tags} if tags else {}, "outputs": [], "source": lines(text)}
def md(text): return {"cell_type": "markdown", "id": uuid.uuid4().hex[:8], "metadata": {}, "source": lines(text)}''')
s=s.replace("json.dump(nb, open(P, 'w'), indent=1, ensure_ascii=False)\nopen(P, 'a').write('\\n')","json.dump(nb, open(P, 'w'), indent=1, ensure_ascii=False)\nopen(P, 'a').write('\\n')")
open('/tmp/claude-1001/apply.py','w').write(s)
EOF
tail -c 3 nb_backup.ipynb | od -c | head -2; python apply.py && cd  && git diff --stat entries/kaku-2025/
```

```
0000000  \n   }  \n
0000003
ok 73
 entries/kaku-2025/kaku.py                   | 224 ++++++++++++--
 entries/kaku-2025/reproduce_kaku_2025.ipynb | 460 ++++++++++++++++++++++------
 2 files changed, 562 insertions(+), 122 deletions(-)
```

**Agent calls Bash**

```bash
cd entries/kaku-2025 && $TMPDIR/dev/bin/python $TMPDIR/dev_proc.py $TMPDIR/survey.pkl $TMPDIR/res15.pkl 15 2>&1 | tail -2; sed -i 's/ns.update(assets=assets, files=files, units=units, onto=onto, regions=regions, res=res)/ns.update(assets=assets, files=files, units=units, onto=onto, regions=regions, res=res, jobs=[None]*len(res))/' $TMPDIR/runnb.py; timeout 1200 $TMPDIR/dev/bin/python $TMPDIR/runnb.py $TMPDIR/survey.pkl $TMPDIR/res15.pkl > $TMPDIR/out1.txt 2>&1; grep -n "Traceback\|Error" $TMPDIR/out1.txt | head; date -u
```

```
15 sessions 244.3440089225769 s; maxrss MB 366.144
Tue Nov 17 12:21:19 UTC 2026
```

**Agent calls Bash**

```bash
awk '/==== cell 11 /,/==== cell 14 /' $TMPDIR/out1.txt | head -60
```

```
==== cell 11 ['sanity']
subject signal  sessions  r at extreme  lag of extreme (ms)  session lags 25% (ms)  session lags 75% (ms)
  DL004    jaw         1         0.081                 64.6                   64.6                   64.6
  DL004 tongue         1         0.063                 71.4                   71.4                   71.4
  DL006    jaw         1         0.044                 95.2                   95.2                   95.2
  DL006 tongue         1         0.060                 98.6                   98.6                   98.6
  DL010    jaw         1         0.032                261.8                  261.8                  261.8
  DL010 tongue         1         0.041               -217.6                 -217.6                 -217.6
  DL014    jaw         1         0.069                 61.2                   61.2                   61.2
  DL014 tongue         1         0.113                 61.2                   61.2                   61.2
  DL016    jaw         1        -0.047                180.2                  180.2                  180.2
  DL016 tongue         1         0.077                 88.4                   88.4                   88.4
  DL018    jaw         1         0.054                 95.2                   95.2                   95.2
  DL018 tongue         1         0.061                 91.8                   91.8                   91.8
  DL021    jaw         1         0.071                 91.8                   91.8                   91.8
  DL021 tongue         1         0.084                 91.8                   91.8                   91.8
  DL023    jaw         1         0.036                 74.8                   74.8                   74.8
  DL023 tongue         1         0.040                 64.6                   64.6                   64.6
  DL024    jaw         1         0.043                 91.8                   91.8                   91.8
  DL024 tongue         1         0.051                 91.8         
[... 30 more lines not kept]
```

**Agent calls Bash**

```bash
awk '/==== cell 23 /,/==== cell 25 /' $TMPDIR/out1.txt; awk '/==== cell 27 /,/==== cell 29 /' $TMPDIR/out1.txt | tail -8; awk '/==== cell 31 /,/==== cell 39 /' $TMPDIR/out1.txt | grep -v "^ *DL0"
```

```
==== cell 23 ['claim:fig1d-lick-breath-frequencies']
              reading  lick mean  lick sd  lick 2.5%  lick 97.5%  breath mean  breath sd  breath 2.5%  breath 97.5%  n licks  n breaths
    (a) within trials      25.82    37.50       1.22      147.06         3.87       1.08         2.28          6.54    76634      76314
(b) within lick bouts       6.10     1.02       3.92        8.40         4.22       0.98         2.65          6.39    31693      15120
(a) within trials {'lick mean': False, 'breath mean': True, 'lick 2.5%': False, 'lick 97.5%': False, 'breath 2.5%': True, 'breath 97.5%': True}
(b) within lick bouts {'lick mean': True, 'breath mean': True, 'lick 2.5%': True, 'lick 97.5%': True, 'breath 2.5%': False, 'breath 97.5%': False}

Per session median frequencies, reading (b): licking [5.43 6.13 6.44] breathing [2.91 3.77 4.79] (5th, 50th, 95th percentiles over sessions)

Round-1 version of (b) (onset pairs in two adjacent bouts counted): 32995 intervals, 1302 of them between two bouts; lick mean 7.99 Hz, 97.5% 12.25 Hz
Lick intervals shorter than 2 frames (6.8 ms, > 147 Hz): 3255 of 76634 under (a), 0 of 31693 under (b)
(a) without intervals under 2 frames: lick mean 20.45 Hz, 2.5% 1.17, 97.5% 98.04 Hz (n = 73379)
---- 0.0s
==== cell 25 ['claim:fig1f-inspiration-between-licks']
sessions    1.0    1.0    1.0    1.0
Sessions with difference > 0: 4 ; = 0: 0 ; < 0: 0
Null, one random split per session: 6 sessions, mean 3.3 ms, p = 6.11e-01 (t-test against 0)
Null, mean of 20 splits per session: mean 8.6 ms; share of splits above 0, median over sessions 0.42
Data minus null over 4 sessions: mean 30.0 ms, paired t-test p = 1.21e-02; data above null in 4
Mice: data above null in 4 of 4; paired t-test p = 1.21e-02
[... 52 more lines not kept]
```

**Agent calls Bash**

```bash
awk '/==== cell 39 /,/==== cell 45 /' $TMPDIR/out1.txt | grep -v "^ *DL0" | head -60; awk '/==== cell 49 /,/==== cell 52 /' $TMPDIR/out1.txt | head -40
```

```
==== cell 39 ['claim:fig1l-lick-interval-preserved', 'claim:fig1l-lick-cycle-prolonged']
events                            reading    quantity   n  mean_ms      p
 licks (a) code: longest third of cycle 0 Delta(1,-1) 158 139.9810 0.0007
 licks (a) code: longest third of cycle 0 Delta(0,-1) 158  27.9316 0.0000
 licks      (b) longest third of cycle -1 Delta(1,-1) 158  66.3861 0.0326
 licks      (b) longest third of cycle -1 Delta(0,-1) 158   1.9152 0.4687
 licks                     (c) all events Delta(1,-1) 474  54.5937 0.0002
 licks                     (c) all events Delta(0,-1) 474  10.3578 0.0000
 licks         (d) (a) with session means Delta(1,-1)  13  56.9289 0.0967
 licks         (d) (a) with session means Delta(0,-1)  13  42.6800 0.0008

Licks, O5 (a), cycle quantiles (ms):
           0.05   0.25   0.50   0.75    0.95
cycle -1  148.1  170.0  176.8  193.8   231.7
cycle 0   183.6  187.0  200.6  217.6   280.8
cycle 1    26.7  156.4  176.8  213.4  1638.8
Cycle 1 longer than 333 ms (the cycle-0 limit): 19 of 158 (12.0%); cycle -1 longer: 0
Diagnostic, not a reading: Delta(1,-1) without those events -12.2 ms (n = 139, p = 2.24e-02); median Delta(1,-1) over all events 3.4 ms
---- 0.0s
==== cell 41 ['claim:fig1n-breath-interval-preserved', 'claim:fig1n-breath-cycle-prolonged']
[... 65 more lines not kept]
```

**Agent calls Bash**

```bash
awk '/==== cell 57 /,/==== cell 58 /' $TMPDIR/out1.txt; awk '/==== cell 63 /,/==== cell 999 /' $TMPDIR/out1.txt | cut -c1-260 | head -100
```

```
(Bash completed with no output)
```

**Agent calls Bash**

```bash
grep -n "==== cell" $TMPDIR/out1.txt | tail -14
```

```
427:==== cell 45 ['claim:fig2-licking-breathing-tuned-counts']
448:==== cell 47 ['claim:fig2-swallow-modulated-counts']
494:==== cell 49 ['claim:fig2f-breathing-units-location']
519:==== cell 51 ['claim:fig2g-licking-units-location']
542:==== cell 53 ['claim:fig2h-swallow-units-location']
572:==== cell 55 ['claim:ed6e-swallow-latencies']
585:==== cell 58 ['claim:ed7-glm-separate-clusters']
589:==== cell 59 ['claim:ed8bc-prebotc-inspiration-phase']
603:==== cell 61 ['claim:ed8e-licking-units-protrusion']
613:==== cell 64 ['claim:ed8i-ipsilateral-lick-selectivity']
621:==== cell 65 ['claim:ed4c-licking-map-insensitive-to-sorting']
628:==== cell 67 ['claim:fig4e-licking-units-anticipate-breath', 'claim:fig4f-breathing-units-anticipate-lick']
691:==== cell 69 ['claim:fig4d-simultaneous-recordings']
718:==== cell 71 None
```

**Agent calls Bash**

```bash
sed -n 585,720p $TMPDIR/out1.txt | cut -c1-280
```

```
==== cell 58 ['claim:ed7-glm-separate-clusters']
Session DL006 20210331-20210331-165022-s3: 176 units, 79968 training bins of 17 ms, 8 regressors; read in 19 s, one lag fitted in 20.1 s (0.114 s per unit); weights finite: True
O8 (a), log link, 11 lags, 20109 units: about 7.0 CPU hours; with the logit link as well 14.0; O8 (b) adds 5 penalty values per unit and link, each at least one such fit: at least 84.2 CPU hours in all, against a 60-minute limit for the notebook on 4 CPUs
---- 40.0s
==== cell 59 ['claim:ed8bc-prebotc-inspiration-phase']
       tuning   d  units  inspiration half  fraction  Rayleigh p
   order 4, a 300      0                 0       NaN         NaN
   order 4, a 500      0                 0       NaN         NaN
   order 4, b 300      0                 0       NaN         NaN
   order 4, b 500      0                 0       NaN         NaN
   order 2, a 300      0                 0       NaN         NaN
   order 2, a 500      0                 0       NaN         NaN
   order 2, b 300      0                 0       NaN         NaN
   order 2, b 500      0                 0       NaN         NaN
order 5, code 300      0                 0       NaN         NaN
order 5, code 500      0                 0       NaN         NaN
All breathing units (MI > 0.9, order 4, V3(a)): 28, in the inspiration half 0.464
---- 0.0s
==== cell 61 ['claim:ed8e-licking-units-protrusion']
       tuning  units  within pi/2 of protrusion  fraction
[... 116 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n "def \|argparse\|add_parser" tools/entry.py | head -60
```

```
47:import argparse
77:    def __init__(self):
80:    def error(self, where, message: str) -> None:
85:def dataset_id(record: dict) -> str | None:
94:def dataset_ids(record: dict) -> list[str]:
99:def claims_paths() -> list[Path]:
105:def claims_target(data: dict) -> tuple:
110:def lookup(index: dict, attempt: dict):
119:def schema(name: str) -> Draft202012Validator:
130:def _parsed(text: str):
138:def _schema_errors(text: str, schema_name: str) -> tuple[str, ...]:
144:def load(report: Report, path: Path):
152:def validate(report: Report, path: Path, schema_name: str) -> dict | None:
161:def _plain(value):
172:def code_of(notebook_path: Path) -> str:
179:def check(entry_dir: Path) -> Report:
395:def _local_data(code: str, start: int) -> bool:
402:def _derivation_checks(report: Report, where, code: str) -> None:
419:def python_of(entry_dir: Path) -> str:
433:def set_python(entry_dir: Path, version: str) -> None:
[... 12 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 508,545p tools/entry.py; sed -n 644,720p tools/entry.py | grep -n "all\|run\|reus" | head -20
```

```
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
    return h.hexdigest()


def reusable(entry_dir: Path, output_dir: Path, max_minutes: float) -> dict | None:
[... 23 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/kaku-2025 && sed -i 's/^step = len(jobs) \/\/ n$/step = max(len(jobs) \/\/ n, 1) if n else 1/; s/^jobs = jobs\[::step\]\[:n\]$/jobs = jobs[::step][:n] if n else jobs/; s/workers=min(n, 5)/workers=5/' $TMPDIR/dev_proc.py && grep -n "step\|jobs =" $TMPDIR/dev_proc.py && date -u && /usr/bin/time -v $TMPDIR/dev/bin/python $TMPDIR/dev_proc.py $TMPDIR/survey.pkl $TMPDIR/res_all.pkl 0 2>&1 | grep -E "sessions|Maximum resident|Elapsed|Error"; date -u
```

```
5:jobs = []
8:step = max(len(jobs) // n, 1) if n else 1
9:jobs = jobs[::step][:n] if n else jobs
Tue Nov 17 12:21:55 UTC 2026
173 sessions 2362.304786682129 s; maxrss MB 885.6
	Elapsed (wall clock) time (h:mm:ss or m:ss): 39:26.02
	Maximum resident set size (kbytes): 2715484
Tue Nov 17 13:01:21 UTC 2026
```

**Agent calls Bash**

```bash
timeout 1500 $TMPDIR/dev/bin/python $TMPDIR/runnb.py $TMPDIR/survey.pkl $TMPDIR/res_all.pkl > $TMPDIR/outA.txt 2>&1; grep -n "Traceback\|Error" $TMPDIR/outA.txt | head; grep -n "==== cell" $TMPDIR/outA.txt | head -50; date -u
```

```
1:==== cell 3 None
4:==== cell 5 ['sanity']
50:==== cell 6 ['sanity']
89:==== cell 8 ['sanity']
107:==== cell 10 ['sanity']
118:==== cell 11 ['sanity']
199:==== cell 14 ['claim:code-dataset-link']
210:==== cell 17 ['claim:units-count']
271:==== cell 20 ['claim:region-spike-rates']
287:==== cell 23 ['claim:fig1d-lick-breath-frequencies']
300:==== cell 25 ['claim:fig1f-inspiration-between-licks']
357:==== cell 27 ['claim:fig1g-lick-delayed-before-slow-breath']
373:==== cell 29 ['claim:fig1f-licking-mode-switch']
382:==== cell 31 ['claim:fig1i-breath-delayed-before-slow-lick']
394:==== cell 33 ['claim:ed1-unidirectional-models-fail']
404:==== cell 35 ['claim:ed1bc-licks-pause-at-swallows']
424:==== cell 37 ['claim:fig1k-rhythms-follow-swallow-at-fixed-latency']
431:==== cell 39 ['claim:fig1l-lick-interval-preserved', 'claim:fig1l-lick-cycle-prolonged']
450:==== cell 41 ['claim:fig1n-breath-interval-preserved', 'claim:fig1n-breath-cycle-prolonged']
469:==== cell 44 ['sanity']
[... 15 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 107,200p $TMPDIR/outA.txt | grep -v "^  DL0.. *\(jaw\|tongue\)" ; sed -n 199,300p $TMPDIR/outA.txt
```

```
==== cell 10 ['sanity']
jaw: units with grid MI > 0.6, true pairing 3476; their median MI 0.798 true, 0.130 with the next trial's phases; units above 0.6 after the shift: 308
breathing: units with grid MI > 0.6, true pairing 950; their median MI 0.743 true, 0.161 with the next trial's phases; units above 0.6 after the shift: 313

Per subject, units with MI > 0.6, true and shifted pairing:
subject   DL004  DL005  DL006  DL007  DL008  DL009  DL010  DL011  DL012  DL014  DL015  DL016  DL017  DL018  DL019  DL020  DL021  DL022  DL023  DL024  DL025  DL026  DL027  DL028  DL029  DL030  DL031  DL032  DL033  DL034  DL035
n_true       20     63    189     84     34     48     90     88     58     72    117    102    117    126     60     48    251     59     60    214    130    132    133    131    132     89    131    236    182     87    193
n_shift       4      9      7     10      1      6     15     13      8      7      6      8      5      8      9      6     13      7     18     23     12     13      6      9     13     10     12     15     17      5     13
br_true       5      7     35     24     17     29     14     26     23     19     24     15     27     30      8      3     39     30     18     52     55     25     12     54     54     36     36     57     71     40     65
br_shift      7      9      7      8      1      4     14     10      7      9     11      9     11      9      4      6      5     10     14     24     15     15     11     10      7     10     17     11     17      9     12
---- 0.0s
==== cell 11 ['sanity']
subject signal  sessions  r at extreme  lag of extreme (ms)  session lags 25% (ms)  session lags 75% (ms)
tongue: lag of the subject-mean extreme, median 85.0 ms, range 54.4 to 261.8 ms; r at the extreme from 0.035 to 0.106, positive in 31 of 31 subjects
jaw: lag of the subject-mean extreme, median 91.8 ms, range 61.2 to 261.8 ms; r at the extreme from -0.032 to 0.071, positive in 30 of 31 subjects
Lag range of the plotted curves: -500 to 5
[... 118 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 300,470p $TMPDIR/outA.txt | grep -v "^DL0..  *0\.\|^  *DL0"
```

```
==== cell 25 ['claim:fig1f-inspiration-between-licks']
Per session fraction of in-bout inspiration onsets that fall inside a tongue protrusion:
count    173.0000
mean       0.2651
std        0.1059
min        0.0325
25%        0.1793
50%        0.3002
75%        0.3463
max        0.4611

Pooled: 70298 of 231563 = 0.3036; reading (b) holds (< 5%): False
Reading (a), no such inspiration in any session: False ; sessions with none: 0 of 173
By subject (pooled fraction):
subject

Latency from the last lick in a breath cycle to the next inspiration (s), pooled:
           count    25%    50%    75%
n_licks                              
1        33791.0  0.109  0.133  0.153
[... 120 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 470,680p $TMPDIR/outA.txt
```

```
br: 300 random units, |grid MI - code MI| median 0.0015, 90th pct 0.050; same side of 0.6 in 0.990
jaw: 300 random units, |grid MI - code MI| median 0.0013, 90th pct 0.018; same side of 0.6 in 0.990

Code scheme on 24 units with MI > 0.6 (31 s): significant at 0.001 by curve_fit 24, by grid 24, same decision 24
---- 30.9s
==== cell 45 ['claim:fig2-licking-breathing-tuned-counts']
       filter significance  lick (i)  breath (i)  both  lick (ii)  breath (ii)  both/lick  both/breath  match (i)  match (ii)  partial
V2(a) order 4        V3(a)      3517        1021   177       3340          844      0.050        0.173       True       False     True
V2(a) order 4        V3(b)      2757         602    69       2688          533      0.025        0.115      False       False     True
V2(a) order 4     code 100      3515        1020   177       3338          843      0.050        0.174       True       False     True
V2(b) order 2        V3(a)      3584        1030   193       3391          837      0.054        0.187       True       False     True
V2(b) order 2        V3(b)      2806         604    70       2736          534      0.025        0.116      False       False     True
V2(b) order 2     code 100      3583        1030   193       3390          837      0.054        0.187       True       False     True
 code order 5        V3(a)      3500        1026   177       3323          849      0.051        0.173       True       False     True
 code order 5        V3(b)      2735         607    71       2664          536      0.026        0.117      False       False     True
 code order 5     code 100      3498        1025   177       3321          848      0.051        0.173       True       False     True

Paper: licking 3551 (+-355), breathing 1015 (+-102), both 182 (+-18) of 20,300; ratios both/lick 5%, both/breath 18%
Units without a breathing fit (no kept trials or empty bins): 0 ; jaw: 0

[... 192 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 680,770p $TMPDIR/outA.txt | cut -c1-250 | grep -v "simultaneous" ; sed -n 680,740p $TMPDIR/outA.txt | grep "simultaneous" | awk '{print $1,$2,$3,$7,$8,$9,$10,$11,$12,$13,$14,$15,$16}' | sort | uniq -c | head -30
```

```
fig4f breathing units      4 (a) MI > 0.6, P < 0.001   a         (a) all sessions     88  33.4091 0.0000        61         1        3.4343  0.5218       30.1266    0.0005               NaN         NaN
  fig4e licking units      4 (a) MI > 0.6, P < 0.001   b         (a) all sessions    692  61.8497 0.0000       590        94       51.3824  0.0000        6.9787    0.1279           60.6683      0.0000
fig4f breathing units      4 (a) MI > 0.6, P < 0.001   b         (a) all sessions     73  33.4247 0.0000        52         1        4.6341  0.4258       28.2353    0.0010               NaN         NaN
  fig4e licking units      4 (b) MI > 0.9, P < 0.001   a         (a) all sessions    271  68.2657 0.0000       240        27       44.0876  0.0000       21.8947    0.0013           54.5122      0.0000
fig4f breathing units      4 (b) MI > 0.9, P < 0.001   a         (a) all sessions     54  32.9630 0.0000        40         1        5.0794  0.4437       25.4902    0.0129               NaN         NaN
  fig4e licking units      4 (b) MI > 0.9, P < 0.001   b         (a) all sessions    271  68.2657 0.0000       240        27       44.0876  0.0000       21.8947    0.0013           54.5122      0.0000
fig4f breathing units      4 (b) MI > 0.9, P < 0.001   b         (a) all sessions     54  32.9630 0.0000        40         1        5.0794  0.4437       25.4902    0.0129               NaN         NaN
  fig4e licking units      4      (c) MI > 0.9 alone NaN         (a) all sessions    271  68.2657 0.0000       240        27       44.0876  0.0000       21.8947    0.0013           54.5122      0.0000
fig4f breathing units      4      (c) MI > 0.9 alone NaN         (a) all sessions     54  32.9630 0.0000        40         1        5.0794  0.4437       25.4902    0.0129               NaN         NaN
  fig4e licking units      2 (a) MI > 0.6, P < 0.001   a         (a) all sessions    825  62.4000 0.0000       702       110       52.9877  0.0000        6.1210    0.1471           61.2672   
[... 60 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 676,740p $TMPDIR/outA.txt | grep "simultaneous" | cut -c1-200 | grep -v " 0      NaN"; grep -n "depends_on" -A2 claims/kaku-2025.yaml | sed -n '/929/,$p' | head; sed -n 929,960p claims/kaku-2025.yaml
```

```
fig4e licking units      4 (a) MI > 0.6, P < 0.001   a (b) simultaneous, 300 um      5  72.0000 0.1485         3         0       68.5714  0.0493       46.6667    0.4987           51.4286      0.1462
  fig4e licking units      4 (a) MI > 0.6, P < 0.001   a (b) simultaneous, 500 um      5  72.0000 0.1485         3         0       68.5714  0.0493       46.6667    0.4987           51.4286      0.1462
==== cell 69 ['claim:fig4d-simultaneous-recordings']
- id: fig4h-fewer-correlations-outside-oscillator
  statement: Units outside the licking oscillator were less often cross-correlated with breathing
    units (54 of 110 pairs), a significantly lower proportion than licking-breathing oscillator
    pairs (Chi-square test, p < 0.0001).
  source: Results, Coupled brainstem oscillators autonomously coordinate licking and breathing,
    paragraph 4; Figure 4h
  quote: units outside of the licking oscillator exhibited less cross correlation with the
    breathing units (Figure 4h; 54/110 pairs with significant cross correlation; a significantly
    lower proportion compared to licking-breathing oscillator unit pairs, p<0.0001, Chi-square
    test)
  statistics:
  - test: Chi-square test
    p: 0.0001
    p_relation: "<"
    n: 110 and 119 pairs
  depends_on:
  - fig4g-licking-breathing-pairs-correlated
[... 15 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/cells && python - <<'EOF'
s=open('c48.py').read()
old='''A = amb_bin.reindex(T.apb.astype(float).to_numpy()).set_index(T.index)
in_amb_col = A.ml_lo.notna() & (T.ml >= A.ml_lo) & (T.ml <= A.ml_hi)
def prebotc(d):
    """Within d um ventral of AMB's ventral edge, inside AMB's ML extent, in the same 100 um AP step."""
    return (in_amb_col & (T.ccf_y > A.dv_hi) & (T.ccf_y <= A.dv_hi + d)).to_numpy()
def above_amb(d):
    return (in_amb_col & (T.ccf_y < A.dv_lo) & (T.ccf_y >= A.dv_lo - d)).to_numpy()
'''
new='''A = amb_bin.reindex(T.apb.astype(float).to_numpy()).set_index(T.index)
in_amb_col = A.ml_lo.notna() & (T.ml >= A.ml_lo) & (T.ml <= A.ml_hi)
in_amb_box = T.ccf_z.between(amb.ap.min(), amb.ap.max()) & T.ml.between(amb.ml.min(), amb.ml.max())
def prebotc(d, step=False):
    """O3 as the claims file words it: within d um ventral of AMB, inside AMB's AP and ML extent (the
    whole nucleus), below its ventral edge. step=True, a variant: AMB's ML extent and ventral edge in the
    unit's own 100 um AP step."""
    if step:
        return (in_amb_col & (T.ccf_y > A.dv_hi) & (T.ccf_y <= A.dv_hi + d)).to_numpy()
    return (in_amb_box & (T.ccf_y > amb.dv.max()) & (T.ccf_y <= amb.dv.max() + d)).to_numpy()
def above_amb(d, step=False):
    if step:
        return (in_amb_col & (T.ccf_y < A.dv_lo) & (T.ccf_y >= A.dv_lo - d)).to_numpy()
    return (in_amb_box & (T.ccf_y < amb.dv.min()) & (T.ccf_y >= amb.dv.min() - d)).to_numpy()
'''
assert old in s; s=s.replace(old,new)
old='''for d in (300, 500):
    print(f"d = {d} um: good units near preBotC {prebotc(d).sum()}, above AMB {above_amb(d).sum()}, lateral of NTS {lateral_nts(d).sum()}")
'''
new='''for d in (300, 500):
    print(f"d = {d} um: good units near preBotC {prebotc(d).sum()} (AMB's extent in each AP step: {prebotc(d, True).sum()}), "
          f"above AMB {above_amb(d).sum()} ({above_amb(d, True).sum()}), lateral of NTS {lateral_nts(d).sum()}")
'''
assert old in s; s=s.replace(old,new)
old='''    for d in (300, 500):
        rows.append({"tuning": f"order {order}, {sig}", "region": f"preBotC ({d} um)", **enrich(prebotc(d), B, PM)})
'''
new='''    for d in (300, 500):
        rows.append({"tuning": f"order {order}, {sig}", "region": f"preBotC ({d} um)", **enrich(prebotc(d), B, PM)})
    for d in (300, 500):
        rows.append({"tuning": f"order {order}, {sig}", "region": f"variant: preBotC by AP step ({d} um)", **enrich(prebotc(d, True), B, PM)})
'''
assert old in s; s=s.replace(old,new)
open('c48.py','w').write(s)
EOF
python - <<'EOF'
import json
P='entries/kaku-2025/reproduce_kaku_2025.ipynb'
nb=json.load(open(P))
def lines(t):
    l=t.rstrip('\n').split('\n'); return [x+'\n' for x in l[:-1]]+[l[-1]]
for c in nb['cells']:
    s=''.join(c['source'])
    if s.startswith('# Regions the CCF does not label'):
        c['source']=lines(open('/tmp/claude-1001/cells/c48.py').read())
    if s.startswith('def rayleigh'):
        s=s.replace('''    for d in (300, 500):
        sel = B & prebotc(d)''','''    for d, step in ((300, False), (500, False), (300, True), (500, True)):
        sel = B & prebotc(d, step)''').replace('''rows.append({"tuning": f"order {order}, {sig}", "d": d, "units"''','''rows.append({"tuning": f"order {order}, {sig}", "d": d, "AMB extent": "by AP step (variant)" if step else "whole nucleus", "units"''')
        c['source']=lines(s)
    if s.startswith('rows = []\nfor order in (4, 2):\n    for oname, kw in O1.items():\n        for sname'):
        s=s.replace('''# Regardless of tuning (verifier, round 1): two-probe sessions with any good unit near the preBotC on one probe
# and any good unit in the posterior-dorsal IRN/PARN on the other
allm = np.ones(len(T), bool)
for d in (300, 500):
    ss = sim_sessions(allm, allm, d)
    mice = {T.loc[T.session == ses, "subject"].iloc[0] for ses in ss}
    print(f"O3 {d} um, any good units: {len(ss)} two-probe sessions in {len(mice)} mice")''','''# Regardless of tuning (verifier, round 1): two-probe sessions with any good unit near the preBotC on one probe
# and any good unit in the posterior-dorsal IRN/PARN on the other; and with AMB's extent taken per AP step
allm = np.ones(len(T), bool)
for d in (300, 500):
    ss = sim_sessions(allm, allm, d)
    mice = {T.loc[T.session == ses, "subject"].iloc[0] for ses in ss}
    print(f"O3 {d} um, any good units: {len(ss)} two-probe sessions in {len(mice)} mice")
_pb = prebotc
for d in (300, 500):
    prebotc = lambda d_, step=False: _pb(d_, True)
    L = tuned("jaw", 4, "a"); B = tuned("br", 4, "a")
    n_t = len(sim_sessions(L, B, d)); n_any = len(sim_sessions(allm, allm, d))
    prebotc = _pb
    print(f"Variant, AMB's extent per AP step, {d} um: {n_t} recordings with O1 (a), order 4, V3 (a); {n_any} with any good units")''')
        c['source']=lines(s)
json.dump(nb, open(P,'w'), indent=1, ensure_ascii=False); open(P,'a').write('\n')
EOF
cd entries/kaku-2025 && timeout 1500 $TMPDIR/dev/bin/python $TMPDIR/runnb.py $TMPDIR/survey.pkl $TMPDIR/res_all.pkl > $TMPDIR/outB.txt 2>&1; grep -n "Traceback\|Error" $TMPDIR/outB.txt | head; date -u
```

```
Tue Nov 17 13:06:58 UTC 2026
```

**Agent calls Bash**

```bash
awk '/==== cell 49 /,/==== cell 51 /' $TMPDIR/outB.txt; awk '/==== cell 53 /,/==== cell 55 /' $TMPDIR/outB.txt | tail -8; awk '/==== cell 59 /,/==== cell 61 /' $TMPDIR/outB.txt; awk '/==== cell 67 /,/==== cell 71 /' $TMPDIR/outB.txt | grep -v " 0      NaN\|0-0" | cut -c1-230
```

```
==== cell 49 ['claim:fig2f-breathing-units-location']
Annotation volume (528, 320, 456) (AP, DV, ML); its label at the unit's position equals the file's region name for 96.3% of 20109 good units
AMB in the annotation: AP 11350 to 12575, |ML| 1225 to 1525, DV 6450 to 6750 um (2763 voxels, both sides)
Round 1, from the 87 AMB-labelled units: AP 11460 to 12420, |ML| 1320 to 1500, DV 6480 to 6760 um
IRN in the annotation: AP 10325 to 13150 (midpoint 11738), DV 5325 to 6975 (midpoint 6150) um
d = 300 um: good units near preBotC 36 (AMB's extent in each AP step: 12), above AMB 127 (29), lateral of NTS 1956
d = 500 um: good units near preBotC 41 (AMB's extent in each AP step: 15), above AMB 221 (69), lateral of NTS 2815
posterior-ventral IRN: 517 ; posterior-dorsal IRN/PARN: 770 ; pons and medulla: 12013
       tuning                               region   n  tuned  fraction  base fraction      p
   order 4, a                     preBotC (300 um)  36     21    0.5833         0.0663 0.0000
   order 4, a                     preBotC (500 um)  41     21    0.5122         0.0663 0.0000
   order 4, a variant: preBotC by AP step (300 um)  12      3    0.2500         0.0663 0.0409
   order 4, a variant: preBotC by AP step (500 um)  15      3    0.2000         0.0663 0.0730
   order 4, a                posterior ventral IRN 517    106    0.2050         0.0663 0.0000
   order 4, b                     preBotC (300 um)  36     20    0.5556         0.0444 0.0000
   order 4, b                     preBotC (500 um)  41     20    0.4878         0.0444 0.0000
   order 4, b variant: preBotC by AP step (300 um)  12      2    0.1667         0.0444 0.0971
   order 4, b variant: preBotC by AP step (500 um)  15      2    0.1333         0.0444 0.1417
   order 4, b                posterior ventral IRN 517     88    0.1702         0.0444 0.0000
   order 2, a                     preBotC (300 um)  36     20    0.5556         0.0669 0.0000
[... 142 more lines not kept]
```

**Agent calls ToolSearch**

```json
{
 "query": "select:WebSearch",
 "max_results": 1
}
```

Result: no output.

**Agent calls WebSearch**

```json
{
 "query": "Takatoh 2021 eLife orofacial premotor atlas Allen CCF data availability premotor neuron coordinates"
}
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR && curl -sL -m 60 -o f5.zip https://cdn.elifesciences.org/articles/67291/elife-67291-fig5-data1-v2.zip && unzip -l f5.zip | head -20; date -u
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR && unzip -o -q f5.zip -d f5 && head -3 f5/g1.csv f5/m1.csv && wc -l f5/*.csv | tail -1 && python3 -c "
import pandas as pd
for f in ['g1','m1']:
    d=pd.read_csv('f5/'+f+'.csv',header=None); print(f, d.shape); print(d.describe().round(1))
"
```

```
Exit code 1
==> f5/g1.csv <==
,name,acronym,AP_location,DV_location,ML_location,avIndex
0,Midbrain reticular nucleus,MRN,-2.85,4.83,-1.28,827
1,Midbrain,MB,-2.86,4.67,-1.81,807

==> f5/m1.csv <==
,name,acronym,AP_location,DV_location,ML_location,avIndex
0,Periaqueductal gray,PAG,-4.1,2.78,0.62,839
1,Koelliker-Fuse subnucleus,KF,-4.68,4.87,2.15,892
  37825 total
Traceback (most recent call last):
  File "<string>", line 2, in <module>
    import pandas as pd
ModuleNotFoundError: No module named 'pandas'
```

**Agent calls Bash**

```bash
cd entries/kaku-2025; python -c "
import json;nb=json.load(open('reproduce_kaku_2025.ipynb'))
for i,c in enumerate(nb['cells']):
  s=''.join(c['source'])
  if c['cell_type']=='markdown' and (s.startswith('**Result') or s.startswith('## Summary') or i in (9,12)): print('----',i); print(s)
"
```

```
---- 9
`ccf_x` is medial-lateral, `ccf_y` dorsal-ventral (cerebellum above medulla) and `ccf_z`
anterior-posterior (pons anterior of medulla), in um, as the paper's code plots them; the files do not
name the axes. The midline of the CCF is at 5700 um, but the `unit_location` text ("left Medulla",
"right Medulla") puts almost every unit on the side opposite to the one that reading of `ccf_x` gives
if it increases to the right. Which side is left is therefore not settled by the files; no claim tested
here depends on it.
---- 12
Jaw phase tuning is present with the true pairing (3,476 units above MI 0.6, median 0.80) and falls
when spikes are paired with the next trial's tracking (median 0.13, 308 units above 0.6), in every
subject. Breathing tuning falls likewise overall (950 units, median 0.74, against 0.16 and 313 units),
but in four subjects (DL004, DL005, DL010, DL020) the shifted pairing gives as many units above 0.6 as
the true one (5 against 7, 7 against 9, 14 against 14, 3 against 6), so for their airflow the shared
clock is not established. Elsewhere spikes, tracking and airflow are consistent with one trial clock.
This concerns alignment within trials; the trials cannot be placed on one session clock, since every
trial starts at 0.
---- 15
**Result: reproduced.** Every input of process_mat.py can be built from the NWB files (listed above), and
the code's unit filter keeps 20,109 units, 0.9% below 20,300. With the Methods' drift metric added it
keeps 16,957 (16.5% below). The spike index needs the reading described in the data check.
[... 188 more lines not kept]
```

**Agent calls Bash**

```bash
awk '/==== cell 53 /,/==== cell 55 /' $TMPDIR/outB.txt | head -25; awk '/==== cell 25 /,/Latency/' $TMPDIR/outB.txt | grep "^DL0" | tr '\n' ' '; echo; grep -n "DL0.. *tongue" $TMPDIR/outB.txt | awk '{print $2,$5,$6}' | tr '\n' ';'
```

```
==== cell 53 ['claim:fig2h-swallow-units-location']
   V4   d         region    n  tuned  fraction  base fraction      p  enriched
V4(a) 300              V  234     13    0.0556         0.0284 0.0183      True
V4(a) 300             IC  313     34    0.1086         0.0284 0.0000      True
V4(a) 300            NLL  189     19    0.1005         0.0284 0.0000      True
V4(a) 300 lateral of NTS 1690     33    0.0195         0.0284 0.9895     False
V4(a) 300      above AMB   92      8    0.0870         0.0284 0.0050      True
V4(a) 500              V  234     13    0.0556         0.0284 0.0183      True
V4(a) 500             IC  313     34    0.1086         0.0284 0.0000      True
V4(a) 500            NLL  189     19    0.1005         0.0284 0.0000      True
V4(a) 500 lateral of NTS 2461     47    0.0191         0.0284 0.9979     False
V4(a) 500      above AMB  157     12    0.0764         0.0284 0.0020      True
V4(b) 300              V  234      8    0.0342         0.0196 0.0948     False
V4(b) 300             IC  313     29    0.0927         0.0196 0.0000      True
V4(b) 300            NLL  189     16    0.0847         0.0196 0.0000      True
V4(b) 300 lateral of NTS 1690     21    0.0124         0.0196 0.9887     False
V4(b) 300      above AMB   92      4    0.0435         0.0196 0.1090     False
V4(b) 500              V  234      8    0.0342         0.0196 0.0948     False
V4(b) 500             IC  313     29    0.0927         0.0196 0.0000      True
V4(b) 500            NLL  189     16    0.0847         0.0196 0.0000      True
[... 7 more lines not kept]
```

**Agent calls Bash**

```bash
cat > $TMPDIR/md.py <<'PYEOF'
import json, uuid
P='entries/kaku-2025/reproduce_kaku_2025.ipynb'
nb=json.load(open(P))
def lines(t):
    l=t.strip('\n').split('\n'); return [x+'\n' for x in l[:-1]]+[l[-1]]
def md(t): return {"cell_type":"markdown","id":uuid.uuid4().hex[:8],"metadata":{},"source":lines(t)}
def find(prefix):
    h=[i for i,c in enumerate(nb['cells']) if ''.join(c['source']).startswith(prefix)]
    assert len(h)==1,(prefix,h); return h[0]
def set_(prefix, t): nb['cells'][find(prefix)]['source']=lines(t)
R={}
R['Jaw phase tuning is present']='''
Jaw phase tuning is present with the true pairing (3,476 units above MI 0.6, median 0.80) and falls
when spikes are paired with the next trial's tracking (median 0.13, 308 units above 0.6), in every
subject. Breathing tuning falls likewise overall (950 units, median 0.74, against 0.16 and 313 units),
but in four subjects (DL004, DL005, DL010, DL020) the shifted pairing gives as many units above 0.6 as
the true one (5 against 7, 7 against 9, 14 against 14, 3 against 6), so for their airflow the shared
clock is not established by this check. This concerns alignment within trials; the trials cannot be
placed on one session clock, since every trial starts at 0.

Airflow against tongue and jaw (added in round 1 of verification). The cross-correlation of the airflow
with the tongue-visible indicator peaks at a positive lag in every subject: median 85 ms over subjects,
54 to 112 ms in 28 of 31, and about 250 ms (the next breath cycle) in DL007, DL010 and DL027. The
correlations are weak (r 0.035 to 0.106), so this check is consistent with one clock within trials but
cannot exclude offsets of a few tens of milliseconds. Subjects DL029 to DL034, where fewer inspirations
fall inside a protrusion (fig1f), have lags of 88 to 112 ms, within the range of the others.

The 3D tracking. In 154 of 173 sessions the 3D `idx` field matches the DLC `trial` field (median
correlation 0.98 between the 2D and 3D tongue tracks at offset 0); in 19 sessions, in 15 subjects, it
matches trial - 1. Each session's 3D tracks are read at its best offset (`kaku.read_session`); round 1
read every file at offset 0. This bears on ed8e and on the lick tips of ed8i.
'''
R['**Result: partially reproduced.** Cerebellum and medulla match']='''
**Result: not reproduced.** Cerebellum and medulla match: 21.3 spikes/s in the cerebellum and
10.9 in the medulla without the vestibular nuclei (reading (a); 21.4 and 11.3 under (b)), against 22 and
11. The vestibular nuclei fire at 27.2 spikes/s under both rate readings, outside 38 +- 3.8, though
still faster than the medulla. With the vestibular nuclei counted in the medulla (i), the medulla mean
is 13.2 to 13.6, outside tolerance. The criterion asks for all three means under one reading and
defines no partial outcome.
'''
R['**Result: not reproduced.** Breathing matches under reading (a)']='''
**Result: partially reproduced.** Under reading (b), within lick bouts, licking is 6.07 Hz (95% range
3.77 to 8.40 Hz) against 6.23 (3.59 to 8.91), and breathing 4.19 Hz against 4.02: both means and both
licking bounds are within tolerance, but the breathing bounds (2.41 and 6.39 Hz against 2.12 and 7.17)
are not. Under reading (a), within trials, breathing matches on all three values (3.89 Hz, 2.10 to 6.68)
but licking does not (26.96 Hz), because the code's tongue onsets include onsets a few milliseconds
apart (39,027 intervals under 2 frames). Round 1 counted, under (b), onset pairs that lie in two
adjacent bouts (13,498 such pairs), which gave 8.06 Hz; reading (b) now takes only pairs inside one bout.
'''
R['**Result: not reproduced.** 30.4% of in-bout']='''
**Result: not reproduced.** 30.4% of in-bout inspiration onsets (70,298 of 231,563) fall between a
tongue onset and the following tongue offset, above the 5% of reading (b); every session has some
(3.3% to 46.1% per session; by subject 8.5% to 42.5%). Both readings fail. The latency from the last
lick of a cycle to the next inspiration has a median of 133 ms after one lick and 92 ms after two
(pooled). The airflow-tongue cross-correlation (data check) peaks at similar lags in the subjects with
low and high fractions, so the fraction is not explained by a clock offset that this check can see.
'''
R['**Result: partially reproduced.** Over the 71 sessions']='''
**Result: partially reproduced.** Over the 71 sessions with enough two-lick cycles and a peak in
each window, the second lick is later before a slow breath by 22.0 ms on average (t = 3.68, p =
4.5e-4, reading (a)); over the 20 mice the mean is 13.6 ms (p = 0.18, reading (b)). 16 of the 20 mice
have a positive mean, one zero and three negative, so not every mouse is positive. 102 of 173 sessions
give no value (fewer than 40 cycles in a half, or no peak). The random-split null, run in round 1 of
verification, gives a positive difference too: 18.3 ms over 83 sessions with one random split each
(p = 0.0012), and the data exceed the mean of 20 random splits by 9.1 ms (paired p = 0.17; above the
null in 50 of 71 sessions and in 10 of 20 mice). The slow window of the header starts 40 ms after the
fast one, so a positive difference arises without an effect, and on these data the measured difference
cannot be told from it. The outcome follows the claims file's criterion, which compares with 0.
'''
R['**Result: partially reproduced.** The median inter-breath interval']='''
**Result: not reproduced.** The median inter-breath interval rises from 1 to 2 to 3 licks per cycle
in 116 of 117 sessions (medians over sessions 0.228, 0.296 and 0.418 s), so licks are added as
breathing slows. The latency from the last lick to the next inspiration is not fixed by the criterion's
20% rule: pooled medians are 133, 92 and 82 ms for 1, 2 and 3 licks (62.5% apart), and only 1 of 117
sessions keeps them within 20%. The criterion asks for both parts and defines no partial outcome.
'''
R['**Result: reproduced.** Over 86 sessions']='''
**Result: reproduced.** Over 86 sessions the inspiration after a lick is later before a slow lick by
10.5 ms on average (t = 6.79, p = 1.5e-9, reading (a)); over 23 mice 9.6 ms (p = 0.0012, reading (b)).
44 sessions are positive, 37 zero and 5 negative. The random-split null gives 3.1 ms (one split per
session, p = 0.092), and the data exceed the mean of 20 random splits by 10.2 ms (paired p = 1.4e-9;
19 of 23 mice above the null), so the effect is not an artefact of the two windows.
'''
R['**Result: reproduced.** With the data']='''
**Result: reproduced.** With the data's interval distributions (inter-breath intervals from fig1d
reading (a), inter-lick intervals from reading (b)) and latencies (112 ms last lick to inspiration,
119 ms inspiration to next lick), the breathing-driven model gives a Fig 1i difference of 0.0 ms in all
162 simulated sessions with a value (no effect). The licking-driven model gives a Fig 1g value in only
1 of 172 sessions: 145 sessions have at least 40 two-lick cycles per half, but the lick PSTH has a peak
above threshold in the fast window in 18 of them and in the slow window in 12, since simulated licks do
not lock to inspiration. So neither model produces the relation it lacks, while the data give both
differences positive (22.0 and 10.5 ms, p < 0.001). The licking-driven result holds because the measure
is missing, not because a test found no effect. Each model does produce the other relation
(breathing-driven Fig 1g 59.3 ms; licking-driven Fig 1i 35.9 ms).
'''
R['**Result: not reproduced.** In 90 sessions']='''
**Result: not reproduced.** In 90 sessions with at least 20 swallows, the probability of a tongue
onset per 3.4 ms bin in the 100 ms after swallow onset is higher than after in-bout expiration onsets
(mean 0.0308 against 0.0211; lower around swallows in 4 of 90 sessions; Wilcoxon p = 4.0e-16). The full
trace shows a pause before the onset: from -90 to 0 ms the swallow trace is 0.0036 to 0.0068 per bin
(minimum 0.0026 at -48 ms) against about 0.021 around expirations, and licking resumes from 0 to 60 ms
(0.030 and 0.050). The code's detector requires a lick within 0.25 s after the detected peak and takes
the onset at the start of the airflow pause, so the criterion's window after onset falls where licking
resumes. This is put to a reader as a question on the criterion's window.
'''
R['**Result: fig1l-lick-cycle-prolonged reproduced']='''
**Result: fig1l-lick-cycle-prolonged reproduced; fig1l-lick-interval-preserved not reproduced.** On
the code's selection (reading (a), 1,932 events), the lick cycle spanning the swallow is longer than
the cycle before by 33.36 ms (p < 0.0001), against 33.3 ms. The cycle after the swallow is also longer
than the one before, by 117.9 ms (p < 0.0001), so the paper's test finds the effect the claim says is
absent; readings (b) to (d) give 86.6, 50.3 and 86.3 ms, all p < 0.001. The mean is driven by long
pauses after the swallow: cycle 1 exceeds 333 ms in 267 of 1,932 events (95th percentile 1,242 ms) and
the median Delta(1,-1) is 0.0 ms. Without those events (a diagnostic, not a reading) the mean is
-16.2 ms, p = 3e-24, which still differs from 0. The port computes cycle 1 as the paper's code does
(generate_figures.plot_licking_swallow_summary, after_2 - after_1, with no limit on cycle 1).
'''
R['**Result: reproduced.** Breathing-tuned units are enriched']='''
**Result: reproduced (resting on the construction of the region).** With the preBotzinger complex built
from the CCF annotation as O3 words it (within 300 or 500 um below AMB, inside the whole nucleus's AP
and ML extent), 36 and 41 good units lie there, of which 20 or 21 are breathing-tuned (49% to 58%,
against 4.4% to 6.7% of pons and medulla units, p < 0.0001), and posterior ventral IRN holds 88 to 109
of 517 (17% to 21%, p < 0.0001), under every reading of tuning and distance. Taking AMB's ML extent and
ventral edge in each 100 um AP step (a variant) leaves 12 or 15 units with 2 or 3 tuned (p 0.04 to
0.27), which would not reproduce; the outcome rests on the whole-nucleus box.
'''
R['**Result: reproduced.** Licking-tuned units are enriched']='''
**Result: reproduced.** Licking-tuned units are enriched in XII (36% to 45% of 166 units), V (43%
to 55% of 269) and IRN (34% to 40% of 1,804), against 20% to 26% of pons and medulla units (p < 0.00001
in each, every reading), and make up 15% to 20% of pons units, above 1%.
'''
R['**Result: partially reproduced.** Under V4(a), the code']='''
**Result: blocked, methods_underspecified.** The two readings of V4 give different outcomes. Under
V4(a), the code's normalisation, swallow-modulated units are enriched in V (5.6%, p = 0.018), IC
(10.9%), NLL (10.1%) and above AMB (8.7% and 7.6%, p = 0.005 and 0.002) against 2.8% in the same
sessions, but not lateral of NTS (1.9% to 2.0%): four of five under both distances, partially
reproduced. Under V4(b), V is not enriched (3.4%, p = 0.095), and above AMB only at 500 um (4.5%, p =
0.037; 4.3%, p = 0.11 at 300 um): two of five at 300 um and three at 500 um, not reproduced. The claims
file's rule blocks a claim whose readings disagree.
'''
R['**Result: not reproduced.** Only 4 or 5 breathing units']='''
**Result: reproduced (resting on the construction of the region, as fig2f).** With the whole-nucleus
box, 18 or 19 breathing units with MI > 0.9 lie near the preBotzinger complex under every reading, of
which 14 prefer the inspiration half (74% to 78%), Rayleigh p < 0.0001. With AMB's extent per AP step
(variant) only 2 units remain (both in the inspiration half), too few for the Rayleigh test, which
cannot reach p < 0.05 with 2 units. Over all 265 breathing units with MI > 0.9, 40.8% prefer the
inspiration half, so the preference is specific to the region.
'''
R['**Result: reproduced.** 70.4% to 70.5%']='''
**Result: reproduced.** 71.4% to 71.5% of licking units with MI > 0.9 (643 to 660 of 899 to 925)
prefer a jaw phase within pi/2 of their session's median phase at full tongue protrusion, under every
reading. The 3D tracks are now read at each session's own trial offset (data check).
'''
R['**Result: both reproduced, resting on reading O2(a)']='''
**Result: both reproduced; fig4f rests on reading O2(a).** Over all sessions (O2(a)), licking units
fire later before a slow breath (mean 61.8 to 68.3 ms; 240 to 702 positive against 27 to 110 negative;
p < 0.001) and breathing units later before a slow lick (33.0 to 33.6 ms; 40 to 61 positive against 1
negative; p < 0.001), under every reading of O1, V2 and V3. Under O2(b), the simultaneous recordings,
3 to 10 licking units give 53.3 to 72.0 ms (p 0.003 to 0.015, every reading), and 2 breathing units
remain, too few for a test. The random-split null (round 1 of verification) separates the two claims.
For breathing units the null is 3.4 to 5.1 ms (p > 0.4) and the data exceed it by 25.5 to 30.1 ms
(paired p 0.0005 to 0.013). For licking units the null is itself large, 44.1 to 53.0 ms (p < 0.0001):
units with MI > 0.6 exceed it by only 6.1 to 8.0 ms (paired p 0.076 to 0.15), units with MI > 0.9 by
20.7 to 21.9 ms (paired p 0.0013 to 0.0019), and under O2(b) not at all. So for licking units most of
the measured difference comes from the slow window starting 60 ms after the fast one. With the 40
cycles nearest the median, as the code selects them, the means are 54.5 to 61.3 ms. The outcomes
follow the claims file's criterion, which compares with 0.
'''
R['**Result: not reproduced.** With the claims file']='''
**Result: blocked, data_missing.** With the claims file's definitions (O1 and O3, the preBotzinger
complex from the CCF annotation), 2 or 3 two-probe sessions have licking units in posterior-dorsal
IRN/PARN on one probe and breathing units near the preBotzinger complex on the other, in 2 or 3 mice,
against 43 recordings in 21 mice. Regardless of tuning, only 4 two-probe sessions, in 4 mice, have any
good unit in each of the two regions (1 with AMB's extent per AP step), of 162 two-probe sessions in 31
mice. Extended Data Fig 12c analyses the same unit pairs in the baseline of the cued licking task, and
the claims file's header places these recordings in that task, which is not in the dandiset. The
recordings are taken as not deposited; were they among these files, the count would not reproduce.

fig4g-licking-breathing-pairs-correlated, fig4g-symmetric-lags and fig4h-fewer-correlations-outside-oscillator
are blocked for the same reason: their unit pairs are those of these recordings (fig4g, fig4g-symmetric-lags
and fig4h depend on fig4d through fig4g in the claims file), and their cross-correlations were not computed.
'''
for k,v in R.items(): set_(k,v)
# new conclusions after ed7 and ed8i cells
i=find('# ed7: cost of the Methods')
nb['cells'].insert(i+1, md('''
**Result: blocked, too_large.** One lag of the unpenalised GLM (O8 (a), log link) takes 20.2 s for the
176 units of one session (0.115 s per unit). For the 20,109 units and 11 lags that is about 7.0 CPU
hours, 14.1 with the logit link, and at least 84.5 with the five penalty values of O8 (b), against a
60-minute limit for the notebook. The claim needs every reading of O8, so no part of it was run.
'''))
i=find('# Extended Data Fig 8i, the part')
nb['cells'].insert(i+1, md('''
**Result: blocked, metadata_insufficient.** Which licks are ipsilateral needs the left-right axis of the
3D tracking and its sign, which the files do not state. The part that needs no sign was run: along the
3D x axis, the lick-side preference of licking units differs between the hemispheres (medians 0.15
against -0.31 spikes/s with the tip against the jaw, 0.22 against -0.26 with the tip alone; 1,714 and
1,803 units; Mann-Whitney p < 0.0001, two-sided), and along the y axis it does not (p 0.30 and 0.81).
So licking units prefer opposite sides in the two hemispheres along x, consistent with a lateral
preference; whether it is ipsilateral cannot be told from the files.
'''))
json.dump(nb, open(P,'w'), indent=1, ensure_ascii=False); open(P,'a').write('\n')
print('ok')
PYEOF
python $TMPDIR/md.py
```

```
ok
```

**Agent calls Bash**

```bash
cat > $TMPDIR/md2.py <<'PYEOF'
import json
P='entries/kaku-2025/reproduce_kaku_2025.ipynb'
nb=json.load(open(P))
def lines(t):
    l=t.strip('\n').split('\n'); return [x+'\n' for x in l[:-1]]+[l[-1]]
c0=''.join(nb['cells'][0]['source'])
old=c0[c0.index('Outside input.'):]
new='''Outside input. Region names in the files are Allen CCF names; their acronyms and parent regions
come from the Allen structure tree, read from the iblatlas repository at a pinned commit
(`kaku.ONTOLOGY_URL`). It maps names only. The regions the CCF does not label (preBotzinger complex,
parts of IRN, the areas next to AMB and NTS) are built from the Allen CCFv3 2017 annotation volume at 25
um (`kaku.CCF_ANNOTATION_URL`).

Revision after round 1 of verification. Lick frequencies within bouts take only pairs inside one bout;
the regions above are built from the annotation volume, not from labelled units; the 3D tracks are read
at each session's trial offset; the peak-difference claims carry a random-split null; Fig 4e units use
the 40 fastest and 40 slowest cycles as the claims file says, with the code's selection beside them;
and ed1, ed1bc, fig1l, fig4d, ed7 and ed8i show the outputs the verifier asked for.

| Claim | Tested here |
|---|---|
| code-dataset-link, units-count, region-spike-rates | yes |
| fig1d, fig1f (two), fig1g, fig1i, ed1, ed1bc, fig1k, fig1l (two), fig1n (two) | yes |
| fig2 tuned counts, swallow counts, fig2f, fig2g, fig2h, ed6e, ed8bc, ed8e, ed4c | yes (fig2h blocked, methods_underspecified) |
| fig4e, fig4f | yes |
| fig4d, fig4g, fig4g lags, fig4h | run in part; blocked, data_missing (recordings not deposited) |
| ed8i (lick direction) | part without the sign run; blocked, metadata_insufficient |
| ed7 (GLM) | cost measured; blocked, too_large |
| ed7g, ed7h (CAE) | blocked, data_missing (raw videos) |
| fig3a, fig3b (premotor atlas) | blocked, other (public source found, not analysed in this run) |
| ed12c, ed2 (rats), fig3ce, fig3dfh, ed10, fig4b, fig4c, ed11b, fig5b, fig5c, fig5e, fig5f | blocked, data_missing |

The notebook streams every file once (about 40 minutes, most of it reading the 25 kHz airflow and
fitting tuning curves) and computes each claim from what it reads.
'''
nb['cells'][0]['source']=lines(c0.replace(old,new))
for c in nb['cells']:
    s=''.join(c['source'])
    if s.startswith('## Summary'):
        c['source']=lines('''
## Summary

| Claim | Outcome |
|---|---|
| code-dataset-link | reproduced |
| units-count | partially reproduced |
| region-spike-rates | not reproduced |
| fig1d-lick-breath-frequencies | partially reproduced |
| fig1f-inspiration-between-licks | not reproduced |
| fig1g-lick-delayed-before-slow-breath | partially reproduced |
| fig1f-licking-mode-switch | not reproduced |
| fig1i-breath-delayed-before-slow-lick | reproduced |
| ed1-unidirectional-models-fail | reproduced |
| ed1bc-licks-pause-at-swallows | not reproduced |
| fig1k-rhythms-follow-swallow-at-fixed-latency | reproduced |
| fig1l-lick-interval-preserved | not reproduced |
| fig1l-lick-cycle-prolonged | reproduced |
| fig1n-breath-interval-preserved | reproduced |
| fig1n-breath-cycle-prolonged | reproduced |
| fig2-licking-breathing-tuned-counts | partially reproduced |
| fig2-swallow-modulated-counts | not reproduced |
| fig2f-breathing-units-location | reproduced (assumed) |
| fig2g-licking-units-location | reproduced |
| fig2h-swallow-units-location | blocked: methods underspecified |
| ed6e-swallow-latencies | reproduced |
| ed8bc-prebotc-inspiration-phase | reproduced (assumed) |
| ed8e-licking-units-protrusion | reproduced |
| ed4c-licking-map-insensitive-to-sorting | reproduced |
| fig4e-licking-units-anticipate-breath | reproduced |
| fig4f-breathing-units-anticipate-lick | reproduced (assumed) |
| fig4d-simultaneous-recordings, fig4g (two), fig4h | blocked: data missing |
| ed8i-ipsilateral-lick-selectivity | blocked: metadata insufficient |
| ed7-glm-separate-clusters | blocked: too large |
| fig3a, fig3b | blocked: other (public source found, not analysed) |
| ed7g, ed7h, ed12c, ed2, fig3ce, fig3dfh, ed10, fig4b, fig4c, ed11b, fig5b, fig5c, fig5e, fig5f | blocked: data missing |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

How the analysis differs from the paper's. The paper's code (process_mat.py) is ported to the
streamed NWB files and its choices are kept. The tuning curves of the 1000 resamples per unit are fitted
by a grid search where the code uses curve_fit (the measured MI uses curve_fit; on 300 random units the
two agree to a median of 0.0015 in MI, and on 24 tuned units the code's own significance scheme gives
the same decision with either fit). Regions the CCF does not label are built from the CCF annotation
volume as the claims file's O3 words them; fig2f and ed8bc reproduce with AMB's whole extent and would
not with AMB's extent taken per AP step. For Fig 4e the licking units' 40 fastest and 40 slowest cycles
are used, as the claims file says; the code takes the 40 nearest the median. The peak-difference
measures of Figs 1g and 4e give a positive difference under a random split of the cycles (18.3 ms and
44.1 to 53.0 ms), because the slow window starts later than the fast one; Figs 1i and 4f do not (3.1 ms
and 3.4 to 5.1 ms). Where the claims file names several readings, all are shown above.

What was found about the dataset. The spike index of every file holds start offsets, not end
offsets, so standard NWB readers misassign spikes; 19 files have more histology rows than units; the
behaviour of both probes of a session is the same recording deposited twice; trials carry no session
times; the age field (P2xxW) and the `photostim` stimulus field do not fit the data; the `left`/`right`
location text disagrees with the side `ccf_x` gives; the 3D tracking has no stated axes, and in 19
sessions its trial index is one below the DLC trial number. The cued licking task, the photostimulation
experiments, the rat recordings and the raw videos are not in the dandiset, and it holds 335 insertions
where the paper reports 339.
''')
json.dump(nb, open(P,'w'), indent=1, ensure_ascii=False); open(P,'a').write('\n')
PYEOF
python $TMPDIR/md2.py && cd  && cat entries/kaku-2025/README.md
```

```
# Kaku, Liu et al. (2025) from dandiset 001619

Tests the findings of [Kaku, Liu et al. (2025)](https://doi.org/10.1101/2025.01.27.635041), "A
brainstem map of orofacial rhythms", that can be tested on
[DANDI:001619](https://dandiarchive.org/dandiset/001619/0.251027.1953). The dandiset holds the brainstem
Neuropixels recordings of 31 mice in the multi-directional licking task (335 probe insertions in 173
sessions), with DeepLabCut tracking of jaw and tongue, the 25 kHz airflow trace and CCF positions of the
units. The cued licking task with photostimulation, the rat recordings, the raw videos and the premotor
tracing data are not in it.

| Claim | Outcome |
|---|---|
| The dandiset holds the inputs of the paper's code (20,109 units pass its filter) | Reproduced |
| 20,300 units, 5,700 cerebellum, 3,700 pons, 10,900 medulla, 339 insertions | Partially reproduced |
| Spike rates of cerebellum, vestibular nuclei and medulla | Partially reproduced |
| Lick and breath frequencies (Fig 1d) | Not reproduced |
| Inspiration never coincides with licking (Fig 1f) | Not reproduced |
| Second lick delayed before a slow breath (Fig 1g) | Partially reproduced |
| Licks added as breathing slows, fixed latency (Fig 1f) | Partially reproduced |
| Inspiration delayed before a slow lick (Fig 1i) | Reproduced |
[... 36 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/kaku-2025 && python - <<'EOF'
p='README.md'; s=open(p).read()
rep=[
("| Spike rates of cerebellum, vestibular nuclei and medulla | Partially reproduced |","| Spike rates of cerebellum, vestibular nuclei and medulla | Not reproduced |"),
("| Lick and breath frequencies (Fig 1d) | Not reproduced |","| Lick and breath frequencies (Fig 1d) | Partially reproduced |"),
("| Licks added as breathing slows, fixed latency (Fig 1f) | Partially reproduced |","| Licks added as breathing slows, fixed latency (Fig 1f) | Not reproduced |"),
("| Breathing units near preBotzinger and posterior ventral IRN (Fig 2f) | Reproduced |","| Breathing units near preBotzinger and posterior ventral IRN (Fig 2f) | Reproduced, on an assumption |"),
("| Swallow units in V, IC, NLL, beside NTS and above AMB (Fig 2h) | Partially reproduced, on an assumption |","| Swallow units in V, IC, NLL, beside NTS and above AMB (Fig 2h) | Blocked: methods underspecified |"),
("| preBotzinger units fire at inspiration (Extended Data Fig 8b-c) | Not reproduced |","| preBotzinger units fire at inspiration (Extended Data Fig 8b-c) | Reproduced, on an assumption |"),
("| Licking and breathing units anticipate the other rhythm (Fig 4e, f) | Reproduced (both), on an assumption |","| Licking units anticipate the next breath (Fig 4e) | Reproduced |\n| Breathing units anticipate the next lick (Fig 4f) | Reproduced, on an assumption |"),
("| 43 simultaneous licking and breathing oscillator recordings (Fig 4d) | Not reproduced |","| 43 simultaneous licking and breathing oscillator recordings (Fig 4d) | Blocked: data missing |"),
("| Cross-correlation of oscillator pairs (Fig 4g, h; three claims) | Blocked: other |","| Cross-correlation of oscillator pairs (Fig 4g, h; three claims) | Blocked: data missing |"),
("| Premotor regions (Fig 3a) | Blocked: other |","| Premotor regions and licking units inside them (Fig 3a, b) | Blocked: other (public source found, not analysed) |"),
("| Autoencoder, rats, photostimulation, cued task, premotor overlap (15 claims) | Blocked: data missing |","| Autoencoder, rats, photostimulation, cued task (14 claims) | Blocked: data missing |"),
("record, with the reasons","record, with the reasons, the verifier's first report and the replies to it,"),
]
for a,b in rep:
    assert a in s, a; s=s.replace(a,b)
s=s.replace("""standard NWB reader misassigns spikes; the helper reads them by the per-trial spike counts.""","""standard NWB reader misassigns spikes; the helper reads them by the per-trial spike counts. Regions
the CCF does not label are built from the Allen CCFv3 annotation volume. The peak-difference measures
of Figs 1g and 4e give a positive difference under a random split of the cycles, so their positive
results carry little weight (see the notebook).""")
open(p,'w').write(s)
EOF
date -u; cd  && timeout 300 python tools/entry.py check entries/kaku-2025 2>&1 | tail -15
```

```
Tue Nov 17 13:09:39 UTC 2026
0 error(s)
```

**Agent calls Bash**

```bash
date -u && timeout 6600 python tools/entry.py all entries/kaku-2025 2>&1 | tail -15; date -u
```

```
Tue Nov 17 13:09:46 UTC 2026
Installed kernelspec registry-kaku-2025 in executed/kaku-2025/.venv/share/jupyter/kernels/registry-kaku-2025
0 error(s)
pass  reproduce_kaku_2025.ipynb  (2630 s)
Tue Nov 17 13:53:44 UTC 2026
```

**Agent calls Bash**

```bash
python - <<'EOF'
import json
nb=json.load(open('executed/kaku-2025/reproduce_kaku_2025.ipynb'))
txt=''
for c in nb['cells']:
    for o in c.get('outputs',[]):
        txt+=''.join(o.get('text',''))+''.join(o.get('data',{}).get('text/plain',''))
for k in ['6.07','18.3 ms','9.1 ms','44.0876','52.6841','20.2 s','0.115 s','71.4','0.7152','36 (AMB','14    0.7368','648','4 two-probe sessions','154','-16.2 ms','0.1526','10.2 ms','59.3 ms','1 of 172','3517']:
    print(k, k in txt)
EOF
```

```
6.07 True
18.3 ms True
9.1 ms True
44.0876 True
52.6841 True
20.2 s False
0.115 s False
71.4 True
0.7152 True
36 (AMB True
14    0.7368 True
648 True
4 two-probe sessions True
154 True
-16.2 ms True
0.1526 True
10.2 ms True
59.3 ms True
1 of 172 True
3517 True
```

**Agent calls Bash**

```bash
python - <<'EOF'
import json
nb=json.load(open('executed/kaku-2025/reproduce_kaku_2025.ipynb'))
for c in nb['cells']:
    if ''.join(c['source']).startswith('# ed7'):
        for o in c['outputs']: print(''.join(o.get('text','')))
EOF
```

```
Session DL006 20210331-20210331-165022-s3: 176 units, 79968 training bins of 17 ms, 8 regressors; read in 18 s, one lag fitted in 19.8 s (0.113 s per unit); weights finite: True
O8 (a), log link, 11 lags, 20109 units: about 6.9 CPU hours; with the logit link as well 13.8; O8 (b) adds 5 penalty values per unit and link, each at least one such fit: at least 83.0 CPU hours in all, against a 60-minute limit for the notebook on 4 CPUs
```

**Agent calls Bash**

```bash
cd entries/kaku-2025 && python - <<'EOF'
import json
P='reproduce_kaku_2025.ipynb'; nb=json.load(open(P))
for c in nb['cells']:
    s=''.join(c['source'])
    if s.startswith('**Result: blocked, too_large.**'):
        s='''**Result: blocked, too_large.** One lag of the unpenalised GLM (O8 (a), log link) takes about 20 s for
the 176 units of one session (about 0.11 s per unit; the printed timing varies a little between runs).
For the 20,109 units and 11 lags that is about 7 CPU hours, about 14 with the logit link, and over 80
with the five penalty values of O8 (b), against a 60-minute limit for the notebook. The claim needs
every reading of O8, so no part of it was run.'''
        l=s.split('\n'); c['source']=[x+'\n' for x in l[:-1]]+[l[-1]]
json.dump(nb, open(P,'w'), indent=1, ensure_ascii=False); open(P,'a').write('\n')
EOF
cat questions/README.md | head -60; ls questions | head -3; cat questions/$(ls questions | sed -n 2p) | head -30
```

```
# Questions

`<dandiset>.yaml` holds an attempt's questions to a reader: places where the author or a verifier
believes the claims file misreads the paper (docs/protocol.md, "Author", step 1.6, and "Hand over for
verification"), and the reader's answers ("Reader", step 6), which say whether the claims file was
amended and why. Each question has `claim`, `question`, `passage`, `why` (how the misreading could
change the outcome), and, once answered, `answer` and `answered` (a date). Method details the claims
file lacks are not asked here: the author takes them from the paper, and a detail the paper does not
settle is a question for the paper's authors, recorded in the claim's notes and as a
`methods_unavailable` finding in the attempt. Files from before protocol `pilot-11` also hold
questions about method details, asked under the earlier rule.
README.md
ashworth-2025.yaml
athalye-2023.yaml
dandiset: "001708"
paper: doi:10.64898/2025.12.15.693905
questions:
- claim: figs3-neutral-unmodulated
  asked: 2026-11-05
  question: >-
[... 24 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n "Extended Data Figure 1\. \|Licking was paused\|swallowing was detected\|Swallow detection" paper/10.1101-2025.01.27.635041.txt | cut -c1-600 | head
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  sed -n 610,620p paper/10.1101-2025.01.27.635041.txt; grep -n "swallow" paper/10.1101-2025.01.27.635041.txt | grep -i "method\|pause\|onset\|detect" | cut -c1-400 | head -8
```

Result: not kept, because it reads the paper's text.

**Agent**

Now the questions file.

**Agent calls Write**

```json
{
 "file_path": "questions/kaku-2025.yaml",
 "content": "paper: doi:10.1101/2025.01.27.635041\ndandiset: \"001619\"\nquestions:\n- claim: units-count\n  asked: 2026-11-17\n  question: >-\n    The criterion counts cerebellum, pons and medulla as CB, P and MY \"with their subregions\" of\n    the Allen structure tree. The paper's three counts (5,700, 3,700 and 10,900) sum to exactly its\n    total of 20,300, so the paper seems to have assigned every unit to one of the three. Under the\n    criterion 2,711 good units fall in none, among them 1,222 in the arbor vitae and others in the\n    cerebellar peduncles and the spinal tract of the trigeminal nerve, which are fibre tracts, not\n    subregions of CB, P or MY in the tree. Should the criterion assign fibre-tract units to the\n    division they lie in (for example the arbor vitae to the cerebellum)?\n  passage: >-\n    \"we obtained 20,300 clear single units, including 5,700 units in the cerebellum, 3,700 units\n    in the pons, and 10,900 units in the medulla\" (Results, Brainstem activity maps of orofacial\n    rhythms, paragraph 2).\n  why: >-\n    With the arbor vitae counted in the cerebellum, the cerebellum count is 5,385, within\n    tolerance of 5,700, where it is 4,157 under the criterion. The pons (3,021) and medulla (8,992)\n    counts would also change if the peduncles and tracts were assigned. Raised by the verifier\n    (round 1, point B11).\n- claim: ed1bc-licks-pause-at-swallows\n  asked: 2026-11-17\n  question: >-\n    The criterion compares lick probability from 0 to 100 ms after swallow onset with that after\n    expirations. The swallow detector it adopts (code detect_swallows) keeps a swallow only if a\n    lick follows the detected peak within 0.25 s, and takes the onset at the start of the airflow\n    pause, so the window after onset partly selects for licks. On these data the lick probability\n    is lowest from about -90 to 0 ms (minimum at -48 ms) and rises from 0 to 60 ms. Does the\n    paper's \"Licking was paused during swallowing\" refer to the pause around the detected event, so\n    that the window should cover the swallow itself (for example the 100 ms before onset, or a\n    window centred on it)?\n  passage: >-\n    \"Example session. Top, lick timing aligned to the detected swallow events ... Licking was\n    paused during swallowing. Bottom, lick timing aligned to all expirations as a control. Lick\n    was not paused during expiration.\" (Extended Data Figure 1b legend); \"c. Lick probably aligned\n    to swallowing across all sessions.\" (Extended Data Figure 1c legend).\n  why: >-\n    In the criterion's window the lick probability is higher around swallows than around\n    expirations in 86 of 90 sessions (0.0308 against 0.0211 per 3.4 ms bin), so the claim is not\n    reproduced; from -90 to 0 ms it is 0.0036 to 0.0068 against about 0.021, which would reproduce\n    it. Raised by the verifier (round 1, point B5).\n- claim: fig4e-licking-units-anticipate-breath\n  asked: 2026-11-17\n  question: >-\n    The header (Unit versions, Fig 4e-f) says the code uses \"the 40 fastest and 40 slowest\n    two-lick cycles\". get_peak_diff_lick_unit sorts the cycles longest first and takes\n    psth_1_i[:n_trial] and psth_2_i[-n_trial:], which are the 40 cycles on each side nearest the\n    median, not the fastest and slowest. Which selection should the criterion use?\n  passage: >-\n    process_mat.py at commit fbc0abe, get_peak_diff_lick_unit: \"sorted_indexes=np.argsort(ibi);\n    sorted_indexes=sorted_indexes[::-1]; ... psth_1_i= np.where((ibi<d_bound) & (n_licks==2))[0];\n    psth_2_i= np.where((ibi>d_bound) & (n_licks==2))[0]; if len(psth_1_i)>n_trial:\n    psth_1_i=psth_1_i[:n_trial]; if len(psth_2_i)>n_trial: psth_2_i=psth_2_i[-n_trial:]\".\n  why: >-\n    The attempt uses the header's 40 fastest and 40 slowest (mean 61.8 to 68.3 ms over all\n    sessions) and shows the code's selection beside it (54.5 to 61.3 ms); both are positive with p\n    < 0.001, so the outcome does not change here, but the numbers do. Raised by the verifier\n    (round 1, point B7).\n"
}
```

```
File created successfully at: questions/kaku-2025.yaml (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd  grep -l "^verifications:" attempts/*.yaml | head -3; f=$(grep -l "^verifications:" attempts/*.yaml | head -1); awk '/^verifications:/,0' $f | head -40; ls schemas 2>/dev/null | head; grep -rn "verifications" schemas/*attempt* 2>/dev/null | head -3
```

```
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
    reason: The archive has 3 assets with sites c8dg, c3bs, c3a and cl3, and nothing about implanted
      or failed sensors. Figure 3 names 4 functional Monkey T sites against the paper's "3/14", so
      "sensor" may mean probe. Neither count can be checked; an implant log of sensors per monkey is
      not in the archive.
[... 28 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python -c "
import json;s=json.load(open('schemas/attempt.schema.json'))
import pprint
d=s['properties']['verifications']; print(json.dumps(d,indent=0)[:2500])
print(json.dumps(s['properties']['outcomes']['items'].get('properties',{}).get('proposed',{}),indent=0)[:600])
print(s['properties']['provenance'] if 'provenance' in s['properties'] else '')
" | head -120; grep -n "blocked_by" -A12 schemas/attempt.schema.json | head -20
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
[... 106 more lines not kept]
```

**Agent calls Bash**

```bash
cat > $TMPDIR/rec.py <<'PYEOF'
import yaml
P='attempts/kaku-2025-01.yaml'
r=yaml.safe_load(open(P))
r['provenance']['agent']['protocol']='pilot-14'
r['inputs'].append({'what': 'Allen CCFv3 annotation volume (2017 release, 25 um), to build the regions the CCF does not label (preBotzinger complex, parts of IRN, the areas next to AMB and NTS) as the claims file words them.',
  'source': 'https://download.alleninstitute.org/informatics-archive/current-release/mouse_ccf/annotation/ccf_2017/annotation_25.nrrd (CCFv3 2017)'})
O={o['claim']:o for o in r['outcomes']}
def upd(c, **kw):
    o=O[c]
    for k,v in kw.items():
        if v is None: o.pop(k,None)
        else: o[k]=v
upd('units-count', notes='Code filter 20,109 units (tolerance 18,270 to 22,330), 60.0 per probe (SD 32.9 against 22), 31 mice; 335 insertions, not 339. Cerebellum 4,157 (5,385 with the arbor vitae, within tolerance), pons 3,021 and medulla 8,992, both below tolerance; 2,711 good units lie outside these regions, 1,222 of them in the arbor vitae and others in the cerebellar peduncles and the spinal tract of the trigeminal nerve. The criterion defines no partial outcome; partially reproduced because the total, the mean per probe and the mice match and the division counts do not. Whether fibre-tract units belong to a division is asked of a reader (questions/kaku-2025.yaml). With the drift metric 16,957 units (CB 3,292, P 2,698, MY 7,626).')
upd('region-spike-rates', outcome='not_reproduced', notes='Reading (a), avg_firing_rate: cerebellum 21.3 +- 28.8 (n 4,157), vestibular nuclei 27.2 +- 28.8 (n 1,276), medulla without VNC 10.9 +- 14.5 (n 7,716), with VNC 13.2. Reading (b), spikes in the first 5 s of good trials: 21.4, 27.2, 11.3 and 13.6. Cerebellum and medulla (ii) are within tolerance; the vestibular nuclei are not (38 +- 3.8) under any reading, though they still fire faster than the medulla. The criterion asks for all three means under one reading and defines no partial outcome, so the outcome is not reproduced (changed from partially reproduced after round 1).')
upd('fig1d-lick-breath-frequencies', outcome='partially_reproduced', measured=[6.07,4.19,3.77,8.4,2.41,6.39],
  notes='Reading (b), within one lick bout: licking 6.07 +- 1.08 Hz (95% range 3.77 to 8.40), breathing 4.19 +- 1.01 Hz (2.41 to 6.39); both means and both licking bounds are within tolerance, the breathing bounds are not (2.12 +- 0.21, 7.17 +- 0.72). Reading (a), within trials: licking 26.96 Hz (1.11 to 147.06), breathing 3.89 Hz (2.10 to 6.68), all three breathing values within tolerance. Round 1 counted under (b) onset pairs lying in two adjacent bouts (13,498 pairs), which gave 8.06 Hz; reading (b) now takes only pairs inside one bout, which changes the outcome from not reproduced. Under (a) 39,027 lick intervals are shorter than 2 frames (tongue detection flickering between frames).',
  deviations=['measured gives reading (b), the reading under which both means are within tolerance.'])
upd('fig1f-inspiration-between-licks', notes='70,298 of 231,563 in-bout inspiration onsets (30.4%) fall between a tongue onset and the next tongue offset; per session 3.3% to 46.1% (median 30.0%), per subject 8.5% to 42.5%; no session has none, so readings (a) and (b) both fail. The median latency from the last lick in a cycle to the next inspiration is 133 ms (1 lick), 92 ms (2), 82 ms (3) and 109 ms (4). The airflow-tongue cross-correlation peaks at 54 to 112 ms in 28 of 31 subjects (about 250 ms, the next cycle, in the other 3), with weak correlations (r 0.035 to 0.106), at similar lags in the subjects with low and high fractions; it is consistent with one clock but cannot exclude offsets of a few tens of milliseconds.')
upd('fig1g-lick-delayed-before-slow-breath', notes='71 of 173 sessions give a value (83 have at least 40 two-lick cycles per half; the others lack a peak in a window). Reading (a), sessions: mean 22.0 ms, t = 3.68, p = 4.5e-4. Reading (b), mice: mean 13.6 ms, p = 0.18 (n = 20). 16 of 20 mice have a positive mean, 1 zero and 3 negative (DL008 -120 ms from one session, DL011 -50, DL027 -33). 60 sessions are positive, 6 zero, 5 negative. A random split of the same cycles also gives a positive difference, because the slow window starts 40 ms after the fast one: 18.3 ms over 83 sessions with one split each (p = 0.0012); the data exceed the mean of 20 splits by 9.1 ms (paired p = 0.17; 50 of 71 sessions and 10 of 20 mice above the null). So the measured difference cannot be told from this artefact. The outcome follows the criterion, which compares with 0.')
upd('fig1f-licking-mode-switch', outcome='not_reproduced', notes='The median inter-breath interval rises from 1 to 2 to 3 licks per cycle in 116 of 117 sessions that have all three (median session medians 0.228, 0.296, 0.418 s; 4 licks 0.558 s), so licks are added as breathing slows. The latency from the last lick to the next inspiration differs by 62.5% between the groups (pooled medians 133, 92 and 82 ms), and only 1 of 117 sessions keeps it within 20%, so the fixed-latency part fails. The criterion asks for both parts and defines no partial outcome (changed from partially reproduced after round 1).')
upd('fig1i-breath-delayed-before-slow-lick', notes='86 sessions give a value. Reading (a): mean 10.5 ms, t = 6.79, p = 1.5e-9; reading (b), 23 mice: 9.6 ms, p = 0.0012. 44 sessions positive, 37 zero (the PSTH bins are 20 ms), 5 negative; 18 of 23 mice positive. Random-split null 3.1 ms (one split per session, p = 0.092); the data exceed the mean of 20 splits by 10.2 ms (paired p = 1.4e-9; 19 of 23 mice above it), so the effect is not an artefact of the two windows.')
upd('ed1-unidirectional-models-fail', notes='Inter-breath intervals from fig1d reading (a), inter-lick intervals from reading (b) (within one bout), the readings closest to the paper for each rhythm; ranges 0.150 to 0.476 s and 0.119 to 0.265 s (2.5th to 97.5th percentiles); latencies 112 ms (last lick to inspiration) and 119 ms (inspiration to next lick). Breathing-driven model: Fig 1i difference 0.0 ms in all 162 of 172 simulated sessions with a value (no variance, so no test). Licking-driven model: a Fig 1g value in 1 of 172 sessions; 145 have at least 40 two-lick cycles per half, but the lick PSTH has a peak above threshold in the fast window in 18 and in the slow window in 12, since simulated licks do not lock to inspiration. So the licking-driven result holds because the measure is missing, not because a test found no effect. Data: 22.0 and 10.5 ms, both p < 0.001. The breathing-driven model gives a Fig 1g effect (59.3 ms, 141 sessions) and the licking-driven model a Fig 1i effect (35.9 ms, 169 sessions).')
upd('ed1bc-licks-pause-at-swallows', notes='90 sessions with at least 20 swallows. Tongue-onset probability per 3.4 ms bin, 0 to 100 ms after onset: 0.0308 around swallows against 0.0211 around in-bout expiration onsets (median ratio 1.50); lower around swallows in 4 of 90 sessions; Wilcoxon p = 4.0e-16 in the opposite direction. The full trace shows the pause before the onset: from -90 to 0 ms 0.0036 to 0.0068 per bin (minimum 0.0026 at -48 ms) against about 0.021 around expirations; licking resumes from 0 to 60 ms (0.030 and 0.050). The detector keeps swallows with a lick within 0.25 s after the detected peak and takes the onset at the start of the airflow pause, so the window after onset favours licks. Whether the criterion\'s window misreads the paper is asked of a reader (questions/kaku-2025.yaml).')
upd('fig1l-lick-interval-preserved', notes='Code selection (O5 a, 1,932 events): Delta(1,-1) = 117.9 ms, one-sample t-test p < 0.0001, so the paper\'s test finds a change. Variants: (b) 86.6 ms, (c) 50.3 ms (5,797 events), (d) 86.3 ms over 140 sessions, all p < 0.0001. The mean is driven by pauses after the swallow: cycle 1 exceeds 333 ms in 267 of 1,932 events (95th percentile 1,242 ms; cycle -1 never does), and the median Delta(1,-1) is 0.0 ms. Without those events (a diagnostic) the mean is -16.2 ms, p = 3e-24. The port computes cycle 1 as the paper\'s code does (generate_figures.plot_licking_swallow_summary, after_2 - after_1, no limit on cycle 1), checked against the code at fbc0abe.')
upd('fig2f-breathing-units-location', assumed=True, notes='The preBotzinger complex is built from the CCF annotation as O3 words it: within 300 or 500 um below AMB, inside the whole nucleus\'s AP and ML extent (AP 11,350 to 12,575, |ML| 1,225 to 1,525, ventral edge DV 6,750 um). It holds 36 and 41 good units, 20 or 21 breathing-tuned (49% to 58%), against 4.4% to 6.7% of pons and medulla units, Fisher p < 0.0001; posterior ventral IRN 88 to 109 of 517 (17% to 21%), p < 0.0001, under every reading of tuning and distance. With AMB\'s ML extent and ventral edge taken in each 100 um AP step (a variant), 12 or 15 units, 2 or 3 tuned, p 0.04 to 0.27, which would not reproduce. Round 1 built the box from 87 AMB-labelled units (16 units, p 0.0004 to 0.0032).',
  deviations=['Assumed: AMB\'s "anterior-posterior and medial-lateral extent" in O3 is the extent of the whole nucleus in the CCF annotation, as the claims file words it; the per-AP-step reading gives a different outcome and is shown. Regions come from the Allen CCFv3 2017 annotation at 25 um (inputs), whose label at the unit\'s position equals the file\'s region name for 96.3% of good units.'])
upd('fig2g-licking-units-location', notes='Licking-tuned fractions: XII 36% to 45% (166 units), V 43% to 55% (269), IRN 34% to 40% (1,804), against 20% to 26% of pons and medulla units, Fisher p < 0.00001 in each under every reading; pons 15% to 20% of 3,021 units, above 1%.')
upd('fig2h-swallow-units-location', outcome='blocked', blocked_by='methods_underspecified', assumed=None,
  notes='The two readings of V4 give different outcomes, which the claims file\'s header blocks. V4(a): enriched in V (13 of 234, 5.6%, p = 0.018), IC (10.9%), NLL (10.1%) and above AMB (8.7% and 7.6%, p = 0.005 and 0.002) against 2.8% in the same sessions, not lateral of NTS (1.9% to 2.0%): four of five under both distances, partially reproduced. V4(b): V 3.4% (p = 0.095), IC and NLL enriched, above AMB 4.3% (p = 0.11) at 300 um and 4.5% (p = 0.037) at 500 um: two and three of five, not reproduced. Regions from the CCF annotation (see fig2f). Round 1 adopted V4(a) as an assumption; the verifier pointed to the header\'s rule, and the outcome was changed from partially reproduced. The question of the normalisation is put to the authors (findings).',
  deviations=['"Lateral of NTS" is units beyond the lateral edge of NTS in the CCF annotation in the same 100 um AP step, within the distance; "above AMB" is units within the distance above AMB\'s dorsal edge inside its AP and ML extent.'])
upd('ed6e-swallow-latencies', notes='Median PSTH peak time (within +-0.15 s) of swallow-modulated units: V and IRN -1 ms (111 units, V4 a) and -4 ms (68, V4 b); IC and NLL +16 ms (53 and 45 units); Mann-Whitney p < 0.0001 under both. By region (V4 a): V -11 ms (13), IRN -1 ms (98), IC +13 ms (34), NLL +20 ms (19). The lead of IRN is small, within one video frame.')
upd('ed7-glm-separate-clusters', notes='Not run. The notebook times the unpenalised GLM (O8 a, log link) on one session: one lag for its 176 units takes about 20 s (about 0.11 s per unit). For 20,109 units and 11 lags that is about 7 CPU hours, about 14 with the logit link, and over 80 with the five penalty values of O8 (b), against a 60-minute limit for the notebook. The claim needs every reading of O8, so a subset or one reading cannot give its outcome, and none was run.')
upd('ed8bc-prebotc-inspiration-phase', outcome='reproduced', assumed=True,
  notes='With the preBotzinger complex of fig2f (CCF annotation, AMB\'s whole extent), 18 or 19 breathing units with MI > 0.9 lie near it under every reading of tuning and distance, and 14 prefer the inspiration half (74% to 78%), Rayleigh p < 0.0001. With AMB\'s extent per AP step (variant) 2 units remain, both in the inspiration half, too few for the Rayleigh test (it cannot reach p < 0.05 with 2). Over all 265 breathing units with MI > 0.9 (order 4, V3 a) 40.8% prefer the inspiration half. Round 1, with the box built from AMB-labelled units, had 4 or 5 units and gave not reproduced; the change follows the region built from the annotation.',
  deviations=['Inspiration onset is phase pi in the tuning phase (Hilbert angle plus pi, as the code), so the inspiration half is preferred phase minus pi in [0, pi).', 'Assumed: the region construction of fig2f.'])
upd('ed8e-licking-units-protrusion', notes='Licking units with MI > 0.9: 643 to 660 of 899 to 925 (71.4% to 71.5%) prefer a jaw phase within pi/2 of the session\'s circular median phase at full protrusion, under every reading. Session protrusion phases have quartiles 3.25, 3.37 and 3.56 rad. The 3D tracks are read at each session\'s trial offset (19 of 173 sessions have 3D idx = DLC trial - 1); round 1 read all at offset 0 and gave 70.4% to 70.5%.')
upd('ed8i-ipsilateral-lick-selectivity', notes='The lick angle needs the left-right axis of the 3D tracking and its sign, which the files do not state, and the files\' left/right hemisphere text is opposite to the side ccf_x gives in 99.3% of units, so ipsilateral cannot be fixed. The part that needs no sign was run (licking units by O1 a; licks split at the session median of the tip, or tip minus jaw; rate from -50 to 100 ms): along the 3D x axis the side preference differs between the hemispheres (medians 0.15 against -0.31 spikes/s, tip minus jaw; 0.22 against -0.26, tip; 1,714 and 1,803 units; two-sided Mann-Whitney p < 0.0001); along y it does not (p 0.30 and 0.81). This is consistent with a lateral preference whose side cannot be named.')
upd('fig3a-premotor-regions', blocked_by='other', notes='The premotor neuron coordinates of reference 43 are public, as eLife 10:e67291 Figure 5 source data 1 (elife-67291-fig5-data1-v2.zip: 12 CSV files, genioglossus, masseter and vibrissa animals, with region, acronym and AP, DV, ML positions in mm from bregma). Round 1 did not look for them. They were found in the revision after round 1 but not analysed in this run: the test needs a conversion from bregma coordinates to CCF and the density contours of Extended Data Fig 9a. A later attempt can test the claim on them.')
upd('fig3b-licking-units-in-premotor-regions', blocked_by='other', notes='Needs the premotor regions of fig3a, built from the premotor neuron coordinates of reference 43, which are public as eLife 10:e67291 Figure 5 source data 1 (found after round 1, not analysed in this run; see fig3a).')
upd('fig4e-licking-units-anticipate-breath', assumed=None,
  notes='Reading O2(a), all sessions: licking units under every reading of O1, V2 (orders 4 and 2) and V3: 271 to 825 units, mean 61.8 to 68.3 ms, 240 to 702 positive against 27 to 110 negative, p < 0.001. Reading O2(b), the simultaneous recordings: 3 to 10 units, 53.3 to 72.0 ms, p 0.003 to 0.015. So every reading gives a positive significant mean. The random-split null is large for this measure, 44.1 to 53.0 ms (p < 0.0001), since the slow window starts 60 ms after the fast one: units with MI > 0.6 exceed it by 6.1 to 8.0 ms (paired p 0.076 to 0.15), units with MI > 0.9 by 20.7 to 21.9 ms (paired p 0.0013 to 0.0019), and under O2(b) not at all. Most of the measured difference is this artefact. The outcome follows the criterion, which compares with 0. Units use the 40 fastest and 40 slowest cycles as the claims file says; the code\'s 40 nearest the median give 54.5 to 61.3 ms (asked of a reader).',
  deviations=['The 40 fastest and 40 slowest two-lick cycles, as the claims file\'s header says; the code takes the 40 on each side nearest the median (shown as a variant; questions/kaku-2025.yaml).'])
upd('fig4f-breathing-units-anticipate-lick',
  notes='Reading O2(a): breathing units under every reading of O1, V2 and V3: 54 to 89 units, mean 33.0 to 33.6 ms, 40 to 61 positive and 1 negative, p < 0.001. Random-split null 3.4 to 5.1 ms (p > 0.4); the data exceed it by 25.5 to 30.1 ms (paired p 0.0005 to 0.013). Reading O2(b): 2 units (30 ms) under every reading, too few for a test. The outcome adopts O2(a), as O2(b) cannot be tested.',
  deviations=['Assumed: reading O2(a) decides where O2(b) cannot be tested (2 units).'])
upd('fig4d-simultaneous-recordings', outcome='blocked', blocked_by='data_missing', measured=None,
  notes='With O1 and O3 as the claims file defines them (preBotzinger complex from the CCF annotation), 2 or 3 two-probe sessions in 2 or 3 mice qualify under every reading, against 43 in 21; regardless of tuning only 4 two-probe sessions (4 mice) have any good unit in both regions, of 162 two-probe sessions in 31 mice. Extended Data Fig 12c analyses these unit pairs in the baseline of the cued licking task, and the claims file\'s header places the recordings in that task, which is not in the dandiset. The recordings are taken as not deposited (the verifier\'s reading after round 1; round 1 gave not reproduced). Were they among these files, the count would not reproduce.')
for c in ('fig4g-licking-breathing-pairs-correlated','fig4g-symmetric-lags','fig4h-fewer-correlations-outside-oscillator'):
    upd(c, blocked_by='data_missing', notes='Depends on fig4d-simultaneous-recordings: the unit pairs are those of the simultaneous recordings, which are taken as not deposited (Extended Data Fig 12c places them in the cued licking task, not in the dandiset). The cross-correlations were not computed. Round 1 gave blocked, other.')
# findings
F=r['findings']
F.insert(4, {'kind':'metadata_error','statement':'The 3D tracking\'s idx field matches the DLC trial number in 154 of 173 sessions and the trial number minus one in 19 sessions (15 subjects), judged by the correlation of the 2D and 3D tongue tracks (median 0.98 at the matching offset); the files do not say how idx counts trials.'})
F.append({'kind':'methods_unavailable','statement':'Question for the authors (fig1g, fig4e): the peak windows of get_peak_diff_lick_behv and get_peak_diff_lick_unit start 40 and 60 ms later for the slow half than for the fast half. On these data a random split of the same cycles gives a positive slow-minus-fast difference (18.3 ms for Fig 1g, 44 to 53 ms for Fig 4e), close to the measured one. Was the difference compared with a split at random, or with equal windows?'})
for f in F:
    if f['statement'].startswith("Question for the authors (fig2f, ed8bc"):
        f['statement']="Question for the authors (fig2f, ed8bc, fig4d, fig4e, fig4f): how were units 'near the preBotzinger complex' and in 'posterior-dorsal IRN/PARN' selected, since the CCF does not label them, and which 43 recordings form Fig 4d? With a region below AMB inside the nucleus's whole extent (CCF annotation) 36 to 41 units qualify and 2 or 3 recordings; with AMB's extent per AP step, 12 to 15 units and the enrichment of fig2f and ed8bc is lost."
    if f['statement'].startswith('The 3D tracking (jaw_side'):
        f['statement']='The 3D tracking (jaw_side, tongue_bottom, lickport_bottom) has no stated axes, origin or units, and the trial tables have no target position, so the lick direction of Extended Data Fig 8 cannot be computed; along the 3D x axis licking units prefer opposite sides in the two hemispheres, but which side is ipsilateral cannot be named.'
r['findings']=F
yaml.safe_dump(r, open(P,'w'), sort_keys=False, width=110, allow_unicode=True)
print('ok')
PYEOF
cd  && python $TMPDIR/rec.py && git diff --stat attempts/
```

```
ok
 attempts/kaku-2025-01.yaml | 283 +++++++++++++++++++++++++++------------------
 1 file changed, 172 insertions(+), 111 deletions(-)
```

**Agent calls Bash**

```bash
cat > $TMPDIR/ver.py <<'PYEOF'
import yaml
P='attempts/kaku-2025-01.yaml'
r=yaml.safe_load(open(P))
V=[
('code-dataset-link',True,'reproduced','Every input exists. 20,109 units pass get_good_units, 0.9% below 20,300 (cell 13).','No change.'),
('fig1d-lick-breath-frequencies',True,'not_reproduced','Mean lick frequency is 26.96 Hz under (a) and 8.06 Hz under (b), against 6.23 +- 0.62. Breathing is within tolerance under (a). The value under (b) is distorted by the defect in B2: two consecutive onsets in adjacent bouts are counted as one interval, and adjacent bouts are often split by a 1 to 2 frame likelihood flicker; dropping between-bout pairs could bring the mean within tolerance.','Fixed B2: reading (b) now takes only onset pairs inside one bout (13,498 between-bout pairs had been counted). Licking is 6.07 Hz (3.77 to 8.40) and breathing 4.19 Hz under (b), both means and the licking bounds within tolerance, the breathing bounds not; outcome changed to partially reproduced. The notebook prints the count of between-bout pairs and of intervals under 2 frames (39,027 under (a), 0 under (b)) and reading (a) without them.'),
('fig1f-inspiration-between-licks',True,'not_reproduced','Pooled, 30.4% of in-bout inspirations fall inside a protrusion; no session has none (cell 20). Unchecked alignment, B6: the share ranges from 8.5% to 42% by subject, about 10% in DL029 to DL034, and no lag check was done.','Added the per-subject cross-correlation of the airflow with the tongue indicator and with jaw_y (data check): peak lags 54 to 112 ms in 28 of 31 subjects, similar in DL029 to DL034, with weak correlations; stated as consistent with one clock but unable to exclude offsets of tens of milliseconds. Outcome unchanged.'),
('fig1g-lick-delayed-before-slow-breath',True,'partially_reproduced','Over sessions +22.0 ms, p = 4.5e-4, n = 71. Only 16 of 20 mice are positive, and over mice p = 0.18. B1: the slow-group window starts later than the fast-group window, so any peak in the gap gives a positive difference with no real effect; on synthetic units with identical firing it gave about +170 ms in 200 of 200 runs. The notebook ran no random-split control. This is a weakness in the claims file\'s method.','Added a random-split null: 18.3 ms with one split per session (p = 0.0012); the data exceed the mean of 20 splits by 9.1 ms (paired p = 0.17). Stated in the notes that the measured difference cannot be told from the artefact. Outcome kept, as the criterion compares with 0; a question on the windows is put to the authors (findings).'),
('fig1f-licking-mode-switch',False,'not_reproduced','The inter-breath interval rises with lick count in 116 of 117 sessions. The latency from last lick to next inspiration differs by 62.5% across groups (133, 92, 82 ms); the limit is 20% (cell 22).','Agreed: the criterion asks for both parts and defines no partial outcome. Outcome changed from partially reproduced to not reproduced.'),
('fig1i-breath-delayed-before-slow-lick',True,'reproduced','Over sessions +10.5 ms, p = 1.5e-9, n = 86 (cell 23).','Added the random-split null (B1): 3.1 ms (p = 0.092); the data exceed it by 10.2 ms (paired p = 1.4e-9). Outcome unchanged.'),
('ed1-unidirectional-models-fail',True,'reproduced','Weak. Breathing model: Fig 1i difference is 0.0 in all 162 sessions. Licking model: the Fig 1g measure exists in only 2 of 169 sessions, so "not significant" holds only by default (B8: the reason is not shown, the keep line is dead code, and the mix of fig1d readings for the two interval sets is not stated).','Removed the dead keep line; the mix of readings is stated in the cell and the notes; inter-lick intervals now come from the corrected reading (b). Added per-model counts of two-lick cycles per half and of sessions with a peak in each window: the licking model has 145 sessions with enough cycles but a fast-window peak in 18 and a slow-window peak in 12, so the measure exists in 1 of 172 sessions. Notes say the result holds because the measure is missing. Outcome unchanged.'),
('ed2-rats-similar',True,'blocked','The archive has mouse data only.','No change.'),
('ed1bc-licks-pause-at-swallows',True,'not_reproduced','Lick probability is lower after swallows in only 4 of 90 sessions; it is higher (0.031 vs 0.021 per bin, Wilcoxon p = 4e-16) (cell 25). B5: detect_swallows keeps a swallow only if a lick follows the swallow peak within 0.25 s, so the criterion\'s window (0 to 100 ms after onset) partly selects for licks; the notebook shows only the window mean, not the full trace.','Added the full trace from -300 to 300 ms: licking is lowest from -90 to 0 ms (minimum at -48 ms) and resumes after onset. The criterion\'s window is put to a reader as a question (questions/kaku-2025.yaml); the claim is tested as the file has it. Outcome unchanged.'),
('fig1k-rhythms-follow-swallow-at-fixed-latency',True,'reproduced','The latency difference is smaller than the cycle -1 difference for licks and breaths under O5 (a) and (b) (cell 26).','No change.'),
('fig1l-lick-interval-preserved',True,'not_reproduced','Under O5 (a), Delta(1,-1) = +117.9 ms, p near 0. Every variant also gives p near 0 (cell 27). B4: this points to a different cycle-1 definition or to unfiltered pauses after the swallow; it was not investigated.','Checked the port against the paper\'s code at fbc0abe (plot_licking_swallow_summary): cycle 1 is after_2 - after_1 with no limit, as ported. Added the cycle -1, 0 and 1 distributions: cycle 1 exceeds 333 ms in 13.8% of events (95th percentile 1,242 ms), the median Delta(1,-1) is 0.0 ms, and without those events the mean is -16.2 ms (p = 3e-24). Outcome unchanged.'),
('fig1l-lick-cycle-prolonged',True,'reproduced','Under O5 (a), Delta(0,-1) = 33.36 ms, p near 0 (paper 33.3 +- 3.3). Under (b) it is 4.0 ms and under (c) 11.0 ms.','No change.'),
('fig1n-breath-interval-preserved',True,'reproduced','Under O5 (a), Delta(1,-1) = -1.8 ms, p = 0.26 (cell 28).','Added the cycle distributions for breaths beside those for licks. Outcome unchanged.'),
('fig1n-breath-cycle-prolonged',True,'reproduced','Under O5 (a), Delta(0,-1) = 48.13 ms, p near 0 (paper 48.0).','No change.'),
('units-count',True,'partially_reproduced','Total (20,109), units per probe (60.0) and mice (31) match. Insertions are 335, not 339. CB 4,157, P 3,021 and MY 8,992 are all outside tolerance. The criterion defines no partial outcome; this is my judgement. B11: 1,222 units in the arbor vitae, plus the cerebellar peduncles and sptV, are counted in no division; the paper\'s three counts sum to exactly 20,300, so the criterion\'s "with their subregions" may misread the paper.','Added B11 to questions/kaku-2025.yaml for a reader; the claim is tested as the file has it, with the arbor-vitae count shown. Outcome unchanged.'),
('region-spike-rates',False,'not_reproduced','CB is 21.3 and MY without VNC is 10.9, both within tolerance. VNC is 27.2 against 38 +- 3.8 under every reading (cell 17).','Agreed: the criterion asks for all three means and defines no partial outcome. Outcome changed from partially reproduced to not reproduced.'),
('fig2-licking-breathing-tuned-counts',True,'partially_reproduced','V3(a) matches under (i) for every V2 reading (for example 3517/1021/177). V3(b) gives 2757/602/69. The both-tuned ratios hold under every reading (cell 31). The header\'s disagreement rule would instead call this methods_underspecified; I followed the claim\'s own two-level criterion.','No change.'),
('fig2-swallow-modulated-counts',True,'not_reproduced','No combination matches. The denominator under (a), 18,494, fits; the swallow-only count is 187 to 355 against 427 +- 43 (cell 32).','No change.'),
('fig2f-breathing-units-location',True,'reproduced','PreBotC: Fisher p <= 0.0032 under all readings, but n = 16 (B3: the AMB box is built from the positions of 87 labelled units, a medial-lateral extent of only 180 um, not from the CCF annotation, and this is not stated as an assumption). Posterior-ventral IRN: p near 0 (cell 33).','Fixed B3: the regions are built from the Allen CCFv3 annotation volume (inputs). With AMB\'s whole extent, as O3 words it, 36 and 41 units, 49% to 58% breathing-tuned, p < 0.0001; with AMB\'s extent per AP step (variant), 12 or 15 units, p 0.04 to 0.27. Outcome kept and marked as resting on the construction (assumed).'),
('fig2g-licking-units-location',True,'reproduced','XII, V and IRN are each enriched (p near 0). The pons fraction is 15 to 20%, above the 1% threshold (cell 34).','No change.'),
('fig2h-swallow-units-location',False,'blocked','V4(a) gives 3 of 5 regions (partial) and V4(b) gives 2 of 5. Lateral of NTS and above AMB are not enriched under either reading (cell 35).','Agreed with the header\'s rule. With the regions from the CCF annotation V4(a) gives four of five (above AMB now enriched) and V4(b) two or three; the readings still disagree. Outcome changed from partially reproduced to blocked, methods_underspecified.'),
('ed6e-swallow-latencies',True,'reproduced','Median peak for V+IRN is -1 ms (V4(a)) and -4 ms (V4(b)); for IC+NLL it is +16 ms; Mann-Whitney p near 0. IRN alone is only -1 to -3 ms, within one video frame (cell 36).','Added the within-one-frame remark to the notes. Outcome unchanged.'),
('ed7-glm-separate-clusters',False,'blocked','Contested. The inputs are all in the files. B12: ed7 is blocked as too_large with no estimate of the cost; the O8(a) unpenalised GLM, or a subset of units, was feasible and was not tried.','Added a cell that fits O8 (a) for one session and times it: about 0.11 s per unit and lag, about 7 CPU hours for all units and lags with the log link alone, over 80 with every reading. The claim needs every reading of O8, so a subset or one reading cannot decide it. Outcome unchanged.'),
('ed7g-cae-better-than-features',True,'blocked','The files hold no raw videos.','No change.'),
('ed7h-prebotc-exception',True,'blocked','Same reason as ed7g.','No change.'),
('ed8bc-prebotc-inspiration-phase',True,'not_reproduced','Only 4 to 5 units qualify; 2 prefer the inspiration half; Rayleigh p = 0.13 to 0.22 (cell 37). The selection is very small (B3).','With the region built from the CCF annotation (B3), 18 or 19 units qualify, 74% to 78% in the inspiration half, Rayleigh p < 0.0001 under every reading; with AMB\'s extent per AP step 2 units remain. Outcome changed to reproduced, marked as resting on the region construction (assumed).'),
('ed8e-licking-units-protrusion',True,'reproduced','70.5% of units (639 of 906) prefer a phase within pi/2 of protrusion. Chance is 50%, which the threshold equals (cell 38). Section C asks whether the 3D idx field counts from 0 or 1 relative to the DLC trial field.','Checked the 3D idx against the DLC trial per session: offset 0 in 154 sessions, -1 in 19; each session is now read at its own offset (finding added). The fraction is 71.4% to 71.5%. Outcome unchanged.'),
('ed8i-ipsilateral-lick-selectivity',True,'blocked','Partly testable. The hemisphere label is consistent (opposite to ccf_x in 99.3% of units), so hemispheres can be separated; only the sign of the lick direction is unknown. A two-sided between-hemisphere test was possible (B13).','Ran it: along the 3D x axis the side preference differs between hemispheres (p < 0.0001, two-sided), along y it does not. Reported in the notes; the claim stays blocked, as ipsilateral cannot be named.'),
('ed4c-licking-map-insensitive-to-sorting',True,'reproduced','2,366 units above 500 uV (paper 2,223 +- 222). Spearman rho = 0.94, p near 0 (cell 39).','No change.'),
('fig3a-premotor-regions',False,'blocked','data_missing. The premotor data are from reference 43 and are not in the dandiset.','Looked for them: the coordinates are public as eLife 10:e67291 Figure 5 source data 1, so the claim is not data_missing (the claims file marks it data elsewhere). Not analysed in this run; kept blocked, other, with the source in the notes.'),
('fig3b-licking-units-in-premotor-regions',True,'blocked','data_missing. Needs the premotor contours from reference 43.','The source is public (see fig3a); blocked_by changed to other, since the data are not missing; not analysed in this run.'),
('fig3ce-descending-stimulation-rhythmic-licking',True,'blocked','No ALM or latSC mice; the cued task is absent.','No change.'),
('fig3dfh-projections-and-rhythm-site',True,'blocked','No Phox2b mice and no fibre-site data.','No change.'),
('ed10-site-classes',True,'blocked','Same reason as fig3dfh.','No change.'),
('fig4b-artificial-licking-keeps-lick-timing',True,'blocked','The cued task with ALM photostimulation is absent.','No change.'),
('fig4c-artificial-licking-breath-timing',True,'blocked','Same reason as fig4b.','No change.'),
('ed11b-alm-breathing-rate',True,'blocked','Same reason as fig4b.','No change.'),
('fig4e-licking-units-anticipate-breath',True,'reproduced','Under the header\'s rule that one O2 reading suffices. Under O2(a) all O1 and V3 readings give +54.5 to +60.7 ms with p near 0. Under O2(b) only 2 to 9 units qualify. The measure is biased by construction (B1). B7: unit_fast and unit_slow select the 40 cycles nearest the median, where the header asks for the 40 fastest and 40 slowest. B9: only filter order 4 was run.','Fixed B7 (40 fastest and slowest, the code\'s selection shown; asked of a reader, since the header misdescribes the code), B9 (order 2 added) and added the null (B1): 44.1 to 53.0 ms; units with MI > 0.6 exceed it by 6.1 to 8.0 ms (p 0.076 to 0.15), MI > 0.9 by about 21 ms (p < 0.002). With the CCF-annotation region O2(b) has 3 to 10 units, all positive and significant, so assumed is removed. Outcome kept, as the criterion compares with 0; the notes say most of the difference is the artefact.'),
('fig4f-breathing-units-anticipate-lick',True,'reproduced','As fig4e: +33 ms, p near 0 under O2(a); 1 unit under O2(b) (cell 40). Same bias (B1).','Added the null: 3.4 to 5.1 ms (p > 0.4); the data exceed it by 25.5 to 30.1 ms (paired p 0.0005 to 0.013), so the effect is not the window artefact. Order 2 added. O2(b) has 2 units. Outcome unchanged.'),
('fig4d-simultaneous-recordings',False,'blocked','data_missing (my reading). The notebook finds only 1 to 2 recordings in 1 to 2 mice, against 43 in 21. ED Fig 12c and the claims header place these recordings in the cued task, which is not deposited. Under the notebook\'s O3 box it would be not_reproduced.','Agreed. With the region from the CCF annotation 2 or 3 recordings qualify, and only 4 two-probe sessions have any unit in both regions. Outcome changed from not reproduced to blocked, data_missing.'),
('fig4g-licking-breathing-pairs-correlated',False,'blocked','data_missing. Depends on the fig4d pairs. The notebook gives no reason in the record available to me (B14).','blocked_by changed from other to data_missing, following fig4d; the notebook now gives the reason after fig4d.'),
('fig4g-symmetric-lags',False,'blocked','data_missing. Same reason as fig4g.','As fig4g.'),
('ed12c-correlation-without-licking',True,'blocked','Needs the cued-task baseline period.','No change.'),
('fig4h-fewer-correlations-outside-oscillator',False,'blocked','data_missing. Same reason as fig4g.','As fig4g.'),
('fig5b-voluntary-lick-latency',True,'blocked','The cued task is absent.','No change.'),
('fig5c-preemptive-breath-adjustment',True,'blocked','Same reason as fig5b.','No change.'),
('fig5e-photostim-lick-latency-longer',True,'blocked','Same reason as fig5b.','No change.'),
('fig5f-artificial-licking-late-breath-adjustment',True,'blocked','Same reason as fig5b.','No change.'),
]
claims={o['claim'] for o in r['outcomes']}
assert {v[0] for v in V}==claims, claims ^ {v[0] for v in V}
r['verifications']=[{'date':'2026-11-17','kind':'agent','by':'Independent agent run by CatalystNeuro (same harness, separate context, did not write the notebook)',
 'reviewed':'Round 1: the executed notebook with the conclusion cells and the summary removed, the helper module kaku.py and the claims file, with the paper under paper/; the verifier read the archive through the DANDI API (335 assets, 31 VGAT-ChR2-EYFP subjects) and tested the peak-difference windows on synthetic units. Report: transcripts/kaku-2025/verifier-1-report.md. Points B10 (histology rows matched by position) and C (fidelity of the port) are answered in the responses; B10 is already a finding and was not changed, since the files give no unit identifier in the histology table.',
 'results':[{'claim':c,'agrees':a,'outcome':o,'reason':rs,'response':rp} for c,a,o,rs,rp in V]}]
yaml.safe_dump(r, open(P,'w'), sort_keys=False, width=110, allow_unicode=True)
PYEOF
cd  && python $TMPDIR/ver.py && timeout 300 python tools/entry.py check entries/kaku-2025 2>&1 | tail -15; date -u
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
grep -n -i "rather\|—" attempts/kaku-2025-01.yaml questions/kaku-2025.yaml entries/kaku-2025/README.md entries/kaku-2025/reproduce_kaku_2025.ipynb entries/kaku-2025/kaku.py | head; grep -n "verification\|transcript" tools/entry.py | head -5; ls tools/ | grep -i check
```

```
350:        for rnd in (attempt.get("verifications") or [])[1:]:
372:                                    f"verification agreed with {verified!r}; record the change under `proposed`, "
claims_check.py
```

**Agent calls Bash**

```bash
date -u && timeout 6600 python tools/entry.py all entries/kaku-2025 2>&1 | tail -5; date -u
```

```
Tue Nov 17 13:56:47 UTC 2026
Installed kernelspec registry-kaku-2025 in executed/kaku-2025/.venv/share/jupyter/kernels/registry-kaku-2025
0 error(s)
pass  reproduce_kaku_2025.ipynb  (2662 s)
Tue Nov 17 14:41:15 UTC 2026
```

**Agent calls Bash**

```bash
python - <<'EOF'
import json
nb=json.load(open('executed/kaku-2025/reproduce_kaku_2025.ipynb'))
txt=''
for c in nb['cells']:
    for o in c.get('outputs',[]):
        txt+=''.join(o.get('text',''))
for k in ['6.07','18.3 ms','9.1 ms','44.0876','36 (AMB','648','154','-16.2 ms','0.1526','10.2 ms','1 of 172','3517','per unit']:
    print(k, k in txt)
import re; print(re.findall(r'one lag fitted in [\d.]+ s \([\d.]+ s per unit\)', txt), re.findall(r'about [\d.]+ CPU hours', txt))
EOF
git status --short | head -20
```

```
6.07 True
18.3 ms True
9.1 ms True
44.0876 True
36 (AMB True
648 True
154 True
-16.2 ms True
0.1526 True
10.2 ms True
1 of 172 True
3517 True
per unit True
['one lag fitted in 19.3 s (0.110 s per unit)'] ['about 6.7 CPU hours']
 M attempts/kaku-2025-01.yaml
 M entries/kaku-2025/README.md
 M entries/kaku-2025/kaku.py
 M entries/kaku-2025/reproduce_kaku_2025.ipynb
 M tools/agent_run.py
 M tools/backfill_summaries.py
[... 14 more lines not kept]
```

**Agent calls Bash**

```bash
git status --short | grep -v "^ M tools\|?? tools"; python tools/entry.py check entries/kaku-2025 2>&1 | tail -2; python -c "import yaml;yaml.safe_load(open('questions/kaku-2025.yaml'));print('q ok')"; date -u
```

```
M attempts/kaku-2025-01.yaml
 M entries/kaku-2025/README.md
 M entries/kaku-2025/kaku.py
 M entries/kaku-2025/reproduce_kaku_2025.ipynb
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
?? questions/kaku-2025.yaml
?? scripts
0 error(s)
q ok
Tue Nov 17 14:41:27 UTC 2026
```

**Agent**

I've revised the attempt for round 1: I fixed or answered every point in the report, re-ran the entry, and nine outcomes changed. The final `python tools/entry.py all entries/kaku-2025` passed with 0 check errors (notebook 2,662 s), and the conclusions match the executed numbers. Nothing is committed.

**Outcome changes**

| Claim | Before | Now | Why |
|---|---|---|---|
| fig1d-lick-breath-frequencies | not reproduced | partially reproduced | Fixed B2: reading (b) had counted 13,498 onset pairs spanning two bouts. Licking is now 6.07 Hz (3.77 to 8.40), within tolerance. Breathing is 4.19 Hz, but its bounds (2.41 and 6.39 Hz) are outside. |
| fig1f-licking-mode-switch | partially reproduced | not reproduced | The criterion defines no partial outcome (verifier's point). |
| region-spike-rates | partially reproduced | not reproduced | Same reason. |
| fig2h-swallow-units-location | partially reproduced | blocked, methods_underspecified | The two V4 readings still disagree (4 of 5 regions against 2 or 3). |
| ed8bc-prebotc-inspiration-phase | not reproduced | reproduced, assumed | With the region built from the CCF annotation, 18 or 19 units qualify, 74 to 78% in the inspiration half, Rayleigh p < 0.0001. |
| fig4d-simultaneous-recordings | not reproduced | blocked, data_missing | The verifier's reading: only 4 two-probe sessions have any unit in both regions. Extended Data Fig 12c places these recordings in the cued task, which is not deposited. |
| fig4g (two claims), fig4h | blocked, other | blocked, data_missing | They follow fig4d; the notebook now gives the reason. |

fig3a and fig3b stay blocked, but for a different reason. The premotor coordinates are public as eLife 10:e67291 Figure 5 source data 1, so the data are not missing. I found them but did not analyse them in this run, so both are recorded as `other`. fig2f stays reproduced but is now marked as resting on how the region is built. fig4e loses its assumption flag, because the simultaneous-recording reading now has 3 to 10 units and agrees.

**Added or corrected**
- **Regions (B3):** the preBötzinger complex and the other unlabelled regions are now built from the Allen CCFv3 2017 annotation volume, recorded as an input. Taking AMB's whole extent, as the claims file words it, gives 36 to 41 units. Taking its extent per 100 µm AP step, shown as a variant, gives 12 to 15 units and loses the fig2f and ed8bc results.
- **Random-split null (B1):** the asymmetric windows produce most of the fig1g and fig4e effects:
  - fig1g: the null is 18.3 ms, and the data exceed it by 9.1 ms (p = 0.17).
  - fig4e: the null is 44 to 53 ms.
  - fig1i and fig4f survive the null.

  I kept the criterion's outcomes, which compare with 0, recorded this in the notes, and added a question for the paper's authors.
- **New finding:** in 19 of 173 sessions the 3D `idx` field is one below the DLC trial number. Each session is now read at its own offset, which moves ed8e to 71.4 to 71.5%.
- **Outputs the verifier asked for:**
  - airflow-to-tongue/jaw cross-correlation per subject
  - full lick trace around swallows (licking pauses from -90 to 0 ms)
  - fig1l cycle distributions, after confirming the port matches the paper's code
  - ed1 diagnostics, with the dead line removed
  - filter order 2 for fig4d, fig4e and fig4f
  - the 40 fastest and 40 slowest cycles for fig4e, with the code's selection beside it
  - the sign-free hemisphere test for ed8i: it differs between hemispheres along the 3D x axis (p < 0.0001); the claim stays blocked
  - a measured GLM cost for ed7: about 7 CPU hours for one reading, over 80 for all
- **Questions for a reader**, in `questions/kaku-2025.yaml`:
  - units-count: arbor vitae and other fibre tracts (B11)
  - ed1bc: the window after swallow onset (B5)
  - the header calls the code's selection the "40 fastest and slowest"; the code actually takes the 40 nearest the median (B7)
- **Record:** the round is under `verifications` for all 48 claims, and the protocol version is now pilot-14. The README, the notebook header and the summary are updated.

**Not done**
- fig3a and fig3b were not analysed. They need a bregma-to-CCF conversion and the density contours, which did not fit in this run.
- B10 (histology rows matched to units by position) is unchanged. It is already a finding, and the files give no identifier to match on.

## End of run

90 turns, 165 minutes, $8.16 at API prices, result: success.
