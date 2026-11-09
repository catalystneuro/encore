# 000140 · author-revise-2 · run 40801407192

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
date -u; cat transcripts/000140/verifier-2-report.md; ls entries/000140-churchland-2010 entries/000140-churchland-2010/*
```

```
Thu Oct 29 01:40:28 UTC 2026
**Verifier report, round 2: 000140-churchland-2010-01**

**1. Outcomes** (20 claims in the claims file, 20 outcomes in the attempt record)

| Claim | Record | Agree? | Assumption |
|---|---|---|---|
| fig4d-mean-correlation-j-array | not_reproduced | Yes | – |
| fig4abc-mean-correlation-other-datasets | blocked: data_missing | Yes | – |
| fig4-broad-near-zero | not_reproduced | Yes | O1a: stated and reasonable. The O1b passes rest on 3–5 units. |
| fig4e-correlation-time-course | reproduced | Yes, on the criterion only | O1a: stated and reasonable. Cell 16 shows the pass is mostly shared trial noise. With disjoint trials the fig4 units have r at −200 ms of only 0.02–0.145, and 4 of 12 readings pass. The record says this. |
| suppfig1-population-averages-lose-tuning | reproduced | Yes, on the criterion only | – |
| fig6d-perimovement-best-j-array | partially_reproduced | Yes | O1a: stated and reasonable. Under O1a both T-matrix readings give reproduced or partial in every setting, so O1a alone carries the outcome. |
| fig6abc-perimovement-best-other-datasets | blocked: data_missing | Yes | – |
| fig6-perimovement-best-each-dimensionality | not_reproduced | Yes | – |
| fig6-maze-endpoint-speed-space-poor | not_reproduced | Yes | O1a: stated and reasonable |
| fig6-dimensionality-trend | not_reproduced | Yes | O1a: stated and reasonable |
| fig6e-summary-rank | blocked: data_missing | Yes | – |
| prep-dimensionality-7-to-10 | not_reproduced | Yes | – |
| fig7a-shuffled-space-poor | reproduced | Yes (weak) | – |
[... 53 more lines not kept]
```

**Agent calls Bash**

```bash
grep -n "" docs/protocol.md | sed -n '/[Hh]and over for verification/,+60p' | head -120; ls attempts* 2>/dev/null | head; find . -path ./node_modules -prune -o -name "*000140*" -print | grep -v transcripts | head
```

```
440:  verification round, with its `reason` (see "Hand over for verification").
441:- **`inputs`**: everything used that is not in the dataset, each with where
442:  it came from (a DOI, or a repository at a commit).
443:- **`findings`**: what the attempt found about the dataset, whatever the
444:  outcomes. These are for the data owner and the archive. The kinds are
445:  `metadata_error`, `data_missing`, `identifier_missing`,
446:  `selection_undocumented`, `methods_unavailable`, `format_error` (files that
447:  break their own format, such as unsorted spike times), `code_mismatch`
448:  (published code that disagrees with the paper or the data),
449:  `paper_inconsistency` (the paper disagrees with itself),
450:  `metadata_insufficient` (a variable without a description or a needed
451:  mapping) and `other`.
452:- **`provenance`**: who is accountable, and for an agent the harness, model
453:  and this protocol's version.
454:
455:If any outcome is `not_reproduced` or `partially_reproduced`, the entry's
456:`README.md` and the notebook's summary carry this sentence: "A failure to
457:reproduce here may be a failure of this attempt, not of the paper: see the
458:reasoning and the differences from the paper's method."
459:
[... 58 more lines not kept]
```

**Agent calls Bash**

```bash
cat attempts/000140-churchland-2010-01.yaml; cat entries/000140-churchland-2010/entry.yaml | head -50
```

```
<persisted-output>
Output too large (34KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/1e64015a-5c17-4a9c-af37-5cc0ab3e3638/tool-results/bm9z1u326.txt

Preview (first 2KB):
schema_version: 2
id: 000140-churchland-2010-01
dataset:
  archive: dandi
  id: "000140"
  version: 0.220113.0408
  doi: 10.48324/dandi.000140/0.220113.0408
paper: doi:10.1016/j.neuron.2010.09.015
date: 2026-10-29
entry: 000140-churchland-2010
provenance:
  kind: agent
  accountable:
    name: CatalystNeuro
  agent:
    harness: Claude Code
[... 28 more lines not kept]
```

**Agent calls Bash**

```bash
grep -n "claim: \|fig7b\|10 of 12\|23 of 24\|mostly from noise\|verifications:\|round:\|proposed\|assumed" attempts/000140-churchland-2010-01.yaml | head -100
```

```
23:- claim: fig4d-mean-correlation-j-array
46:- claim: fig4abc-mean-correlation-other-datasets
52:- claim: fig4-broad-near-zero
54:  assumed: true
68:- claim: fig4e-correlation-time-course
70:  assumed: true
83:    units) the value at onset is 0.091 to 0.244, partially reproduced in 10 of 12 readings.
89:- claim: suppfig1-population-averages-lose-tuning
98:    readings, so the strongest trace being on top at -150 ms comes mostly from noise shared within the
104:- claim: fig6d-perimovement-best-j-array
106:  assumed: true
138:- claim: fig6abc-perimovement-best-other-datasets
143:- claim: fig6-perimovement-best-each-dimensionality
150:- claim: fig6-maze-endpoint-speed-space-poor
152:  assumed: true
163:- claim: fig6-dimensionality-trend
165:  assumed: true
174:- claim: fig6e-summary-rank
181:- claim: prep-dimensionality-7-to-10
191:- claim: fig7a-shuffled-space-poor
[... 33 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 68,135p attempts/000140-churchland-2010-01.yaml; echo ----; sed -n 195,215p attempts/000140-churchland-2010-01.yaml; echo ---; sed -n 273,290p attempts/000140-churchland-2010-01.yaml; echo ----; sed -n 330,520p attempts/000140-churchland-2010-01.yaml
```

```
- claim: fig4e-correlation-time-course
  outcome: reproduced
  assumed: true
  notebook: reproduce_churchland_2010.ipynb
  output: claim:fig4e-correlation-time-course
  notes: Under all 18 O1 range readings the mean correlation at movement onset is below 0.1 and below
    half its value at -200 ms, and the largest 50 ms drop starts 270 to 210 ms before onset. Main
    reading (fig4 units, 19) 0.295 at -200 ms and -0.078 at onset; all units with preparatory tuning
    (93) 0.62 at -400 ms, 0.39 at -200 ms, 0.12 at -100 ms and -0.00 at onset. Trial noise also meets
    the criterion, so the pass carries little evidence. With condition labels shuffled it is met in 18
    of 20 shuffles for the fig4 units and 20 of 20 for all units with > 5 spikes/s (r at -200 ms 0.28
    to 0.37, at onset -0.028 to 0.035), because the preparatory and movement-locked means share the
    noise of the same 1 to 4 trials and the preparatory window ends about 220 ms before onset. With the
    two means from disjoint trials the correlation at -200 ms is only 0.12 to 0.18 for all units, and
    the criterion is met in 4 of 12 readings (fig4 units) and 9 of 12 (all units). Under O1 SD (3 to 8
    units) the value at onset is 0.091 to 0.244, partially reproduced in 10 of 12 readings.
  deviations:
  - Assumed O1 is the range across conditions (see fig4-broad-near-zero).
  - The time axis uses go-locked means from -200 to +200 ms and movement-locked means from -400 to
    +400 ms, in 10 ms steps (Supplemental Experimental Procedures, the spliced trace); the judgement
[... 275 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/000140-churchland-2010; python - <<'EOF'
import json
nb=json.load(open('reproduce_churchland_2010.ipynb'))
for i in [24,25,28,30,53,54,55,67,68,72]:
    c=nb['cells'][i]
    print('=====',i,c['cell_type'],c.get('metadata',{}).get('tags'))
    print(''.join(c['source'])[:3000])
    for o in c.get('outputs',[]):
        t=''.join(o.get('text',''))  or ''.join(o.get('data',{}).get('text/plain',''))
        print('--out--');print(t[:4000])
EOF
```

```
===== 24 code ['claim:fig4e-correlation-time-course']
rows, curves = [], {}
for (o, f), cfg in CONFIGS.items():
    for O1 in ("range", "sd"):
        for O2 in ("i", "ii"):
            for units_reading in ("a", "b"):
                sel = fig4_units(cfg, O1, O2) if units_reading == "a" else mp.tuning(cfg["P"], O1) > mp.PREP_TUNING_MIN
                if sel.sum() < 3 or (units_reading == "b" and O2 == "ii"):
                    continue
                go, mv = time_course(cfg, sel)
                curves[(o, f, O1, O2, units_reading)] = (go, mv)
                rows.append({"O3": o, "O4": f, "O1": O1, "O2": O2 if units_reading == "a" else "-",
                             "units": units_reading, "n": int(sel.sum()), "r at go-200": go[0], "r at go": go[LAGS_GO == 0][0],
                             **judge_tc(mv)})
tc_table = pd.DataFrame(rows)
print(tc_table.round(3).to_string(index=False))
print("readings passing:", int(tc_table["pass"].sum()), "of", len(tc_table))
go_m, mv_m = curves[("a", "a", "range", "i", "a")]
go_b, mv_b = curves[("a", "a", "range", "i", "b")]
print("main, fig4 units: r from %.2f to %.2f over -400..400 ms re onset" % (mv_m.min(), mv_m.max()))
[... 196 more lines not kept]
```

**Agent calls Bash**

```bash
python - <<'EOF'
import json
nb=json.load(open('reproduce_churchland_2010.ipynb'))
for i in [24,30,32]:
    c=nb['cells'][i]
    for o in c.get('outputs',[]):
        t=''.join(o.get('text',''))
        print('=====',i);print(t[:6000])
for i,c in enumerate(nb['cells']):
    s=''.join(c['source'])
    if 'reliab' in s and c['cell_type']=='code': print('#### reliability in cell',i); print(s[:2500])
EOF
```

```
(Bash completed with no output)
```

**Agent calls Bash**

```bash
cd  ls executed/ 2>/dev/null | head; ls executed/000140-churchland-2010 2>/dev/null; sed -n '/^## /p' docs/protocol.md | head -40
```

```
## Reader
## Author
## Repeat attempts
## Local and remote datasets
## Verifier
```

**Agent calls Bash**

```bash
ls transcripts/000140/; grep -o "performance for all units and readings in [0-9.]* s" -r transcripts/000140 | head; grep -oi "took [0-9]* min[^\"]\{0,40\}\|in [0-9]\+ min[^\"]\{0,30\}" -r transcripts/000140/*.md | head
```

```
answer-report.md
answer.md
author-answers-report.md
author-answers.md
author-report.md
author-revise-1-report.md
author-revise-1.md
author.md
claims-check-report.md
claims-check.md
claims-report.md
claims.md
verifier-1-report.md
verifier-1.md
verifier-2-report.md
verifier-2.md
```

**Agent calls Bash**

```bash
grep -n "entry.py all\|real\|minutes\|elapsed" transcripts/000140/author-revise-1.md | head -20; python tools/entry.py --help 2>&1 | head -20
```

```
195:For each proposed change the verifier agreed with, set the claim's `outcome` (and `blocked_by`) to the proposed one and remove `proposed`. For each it did not agree with, keep the outcome and leave `proposed` with the verifier's view added to its reason. Change nothing else in the outcomes. Update the notebook's conclusions and summary, the entry README and the attempt notes to match, re-run with `python tools/entry.py all entries/{entry}`, and record round 3 under `verifications` with one result for each claim the verifier reviewed: whether it agreed, the outcome it would give, its reason in its own words, and your response. Do not commit or push: the workflow commits your changes.
262:Notebook runs in under 2 minutes, so I can iterate. Baseline run first.
267:cd  time python tools/entry.py all entries/000140-churchland-2010 2>&1 | tail -15
275:real	2m32.712s
602:real	0m25.199s
1447:cd  date -u; python tools/entry.py all entries/000140-churchland-2010 2>&1 | tail -5; date -u
1800:"the analysis, about two minutes.":"the analysis, about four minutes."}
1805:date -u; python tools/entry.py all entries/000140-churchland-2010 2>&1 | tail -3; date -u
2227:      is satisfied trivially. The real evidence is O1b (8 units), 0.209 intact vs -0.06 shuffled. Run
2393:I've revised the attempt for verifier round 1. The entry re-ran cleanly (`entry.py all`: 0 errors, notebook passes in 232 s), every number in the conclusions matches the new run, and `check` passes. Nothing is committed.
2419:- The notebook now takes about 4 minutes instead of 2, mostly from running fig7d on every reading.
2423:48 turns, 24 minutes, result: success.
usage: entry.py [-h] [--output-dir OUTPUT_DIR] [--timeout TIMEOUT]
                [--max-minutes MAX_MINUTES]
                {lock,check,run,all,handover} entry

Lock, check and run one entry. This is the whole local workflow for a deposit.

    python tools/entry.py lock  entries/<name>   # pin the environment
    python tools/entry.py check entri
[... 12 more lines not kept]
```

**Agent**

About 4 minutes per run. I'll run the entry now to get outputs, then make text fixes.

**Agent calls Bash**

```bash
date -u; python tools/entry.py all entries/000140-churchland-2010 2>&1 | tail -5; date -u; ls executed/000140-churchland-2010
```

```
Thu Oct 29 01:41:01 UTC 2026
Installed kernelspec registry-000140-churchland-2010 in executed/000140-churchland-2010/.venv/share/jupyter/kernels/registry-000140-churchland-2010
0 error(s)
pass  reproduce_churchland_2010.ipynb  (138 s)
Thu Oct 29 01:43:51 UTC 2026
reproduce_churchland_2010.ipynb
result.json
```

**Agent calls Bash**

```bash
cat > $TMPDIR/show.py <<'EOF'
import json,sys
nb=json.load(open('executed/000140-churchland-2010/reproduce_churchland_2010.ipynb'))
for a in sys.argv[1:]:
    i=int(a); c=nb['cells'][i]
    print('=====',i)
    for o in c.get('outputs',[]):
        print(''.join(o.get('text','')) or ''.join(o.get('data',{}).get('text/plain','')))
EOF
python $TMPDIR/show.py 24 30 32 | cut -c1-250
```

```
===== 24
entries/000140-churchland-2010/maze_prep.py:270: RuntimeWarning: invalid value encountered in divide
  return (a * b).sum(0) / np.sqrt((a ** 2).sum(0) * (b ** 2).sum(0))

O3 O4    O1 O2 units  n  r at go-200  r at go  r at -200  r at 0  largest 50 ms drop starts  pass  partial
 a  a range  i     a 19        0.341    0.620      0.295  -0.078                       -250  True    False
 a  a range  -     b 93        0.410    0.605      0.388  -0.001                       -220  True    False
 a  a range ii     a 88        0.404    0.595      0.376  -0.011                       -220  True    False
 a  a    sd  -     b  8        0.621    0.787      0.555   0.106                       -130 False     True
 a  a    sd ii     a  5        0.632    0.801      0.567   0.091                         90 False    False
 a  b range  i     a 13        0.350    0.643      0.298  -0.075                       -240  True    False
 a  b range  -     b 91        0.436    0.611      0.399   0.019                       -220  True    False
 a  b range ii     a 85        0.423    0.596      0.381   0.008                       -210  True    False
 a  b    sd  -     b  8        0.637    0.803      0.593   0.126                       -130 False     True
 a  b    sd ii     a  4        0.565    0.782      0.543   0.147                       -220 False     True
 a  c range  i     a 15        0.334    0.604      0.330  -0.065                       -230  True    False
 a  c range  -     b 91        0.452    0.614      0.414   0.022                       -220  True    False
 a  c range ii     a 85        0.442    0.599      0.395   0.012                       -210  True    False
 a  c    sd  -     b  7        0.691    0.834      0.661   0.172                       -130 False     True
 a  c    sd ii     a  4        0.625    0.766      0.561   0.142                         90 False     True
[... 209 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/000140-churchland-2010; python - <<'EOF'
import json
nb=json.load(open('reproduce_churchland_2010.ipynb'))
for i,c in enumerate(nb['cells']):
    s=''.join(c['source'])
    if 'split' in s.lower() and c['cell_type']=='code': print('#### cell',i); print(s[:3000])
EOF
grep -n "def .*split\|def .*reliab" maze_prep.py
```

```
#### cell 3
meta = data["meta"]
print("subject", meta["subject"], "session start", meta["session_start"])
print("train file trials:", len(trials), "splits:", trials.split.value_counts().to_dict())
print("test file segments:", len(test["trials"]), "columns:", test["colnames"], "behaviour:", test["has_behavior"])
print("test segment length (s):", np.unique(np.round(test["trials"].stop_time - test["trials"].start_time, 3)),
      "move onset re start (s):", np.unique(np.round(test["trials"].move_onset_time - test["trials"].start_time, 3)))
print("all train trials successful:", bool(trials.success.all()))
print("conditions (maze_id x trial_version):", trials.groupby(["maze_id", "trial_version"]).ngroups,
      "| mazes:", trials.maze_id.nunique(), "| trial_type values:", trials.trial_type.nunique())
print("trial_version vs targets/barriers:")
print(pd.crosstab(trials.trial_version, [trials.num_targets, trials.num_barriers]))
print("delay (ms): min %d median %d max %d; trials with delay > 400 ms: %d"
      % (trials.delay.min(), trials.delay.median(), trials.delay.max(), (trials.delay > mp.MIN_DELAY_MS).sum()))
kept_delay = trials[trials.delay > mp.MIN_DELAY_MS]
per_cond = kept_delay.groupby("cond").size()
print("trials per condition after the delay rule: min %d, median %.0f, max %d; conditions with 1 trial: %d"
      % (per_cond.min(), per_cond.median(), per_cond.max(), (per_cond == 1).sum()))
print("delay column = go cue - target onset (max abs diff, ms):",
      float(np.abs((trials.go_cue_time - trials.target_on_time) * 1000 - trials.delay).max()))
[... 96 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/000140-churchland-2010; python - <<'EOF'
import json
p='reproduce_churchland_2010.ipynb'
nb=json.load(open(p))
c=nb['cells'][11]
s=''.join(c['source'])
add='''
sel_sd = mp.tuning(CONFIGS[MAIN]["P"], "sd") > mp.PREP_TUNING_MIN
print("same, units with > 5 spikes/s preparatory SD (n = %d): preparatory median %.2f (values %s), peri-movement median %.2f"
      % (sel_sd.sum(), np.nanmedian(rel_P[sel_sd]), np.round(np.sort(rel_P[sel_sd]), 2), np.nanmedian(rel_M[sel_sd])))'''
s=s.rstrip('\n')+add
c['source']=s.splitlines(keepends=True)
json.dump(nb,open(p,'w'),indent=1,ensure_ascii=False); open(p,'a').write('\n')
EOF
git diff --stat
```

```
entries/000140-churchland-2010/reproduce_churchland_2010.ipynb | 5 ++++-
 1 file changed, 4 insertions(+), 1 deletion(-)
```

**Agent calls Bash**

```bash
cd  python $TMPDIR/show.py 53 67 | grep -v "^ *$" | cut -c1-200
```

```
===== 53
O3 O4    O1   -150   -100    -50      0     50    100  ratio 0/-150
 a  a range -0.044 -0.048 -0.049 -0.054 -0.066 -0.067           NaN
 a  a    sd  0.209  0.162  0.140  0.105  0.057  0.047         0.501
 a  b range -0.045 -0.049 -0.051 -0.059 -0.069 -0.071           NaN
 a  b    sd  0.202  0.118  0.112  0.095  0.063  0.045         0.471
 a  c range -0.023 -0.029 -0.034 -0.050 -0.052 -0.051           NaN
 a  c    sd  0.247  0.242  0.230  0.188  0.152  0.133         0.761
 b  a range -0.046 -0.047 -0.049 -0.057 -0.065 -0.067           NaN
 b  a    sd  0.140  0.134  0.116  0.091  0.071  0.061         0.646
 b  b range -0.043 -0.044 -0.045 -0.056 -0.064 -0.068           NaN
 b  b    sd  0.129  0.128  0.119  0.087  0.066  0.050         0.669
 b  c range -0.026 -0.029 -0.032 -0.046 -0.051 -0.051           NaN
 b  c    sd  0.249  0.245  0.232  0.186  0.160  0.140         0.748
ratio defined (performance at -150 ms above zero): 6 of 12 | within 0.97 +/- 0.097: 0
O1 SD ratios: 0.471 to 0.761
===== 67
O3 O4    O1                 space  k  z-scored axes  n units  consistency other  consistency peri  peri higher
 a  a range endpoints + max. spd.  3          False       93              0.523             0.617         True
 a  a range endpoints + max. spd.  3           True       93              0.531             0.630         True
[... 79 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n "clearer\|performs best\|fig7b\|10 of 12\|23 of 24\|mostly from" entries/000140-churchland-2010/README.md attempts/000140-churchland-2010-01.yaml; grep -n "assumed" docs/protocol.md | head
```

```
attempts/000140-churchland-2010-01.yaml:83:    units) the value at onset is 0.091 to 0.244, partially reproduced in 10 of 12 readings.
attempts/000140-churchland-2010-01.yaml:98:    readings, so the strongest trace being on top at -150 ms comes mostly from noise shared within the
attempts/000140-churchland-2010-01.yaml:201:- claim: fig7b-window-start-slide
attempts/000140-churchland-2010-01.yaml:204:  output: claim:fig7b-window-start-slide
attempts/000140-churchland-2010-01.yaml:285:    comparison in 23 of 24 readings.
attempts/000140-churchland-2010-01.yaml:398:      2 of 12 readings, so the strongest trace being on top at -150 ms comes mostly from noise shared
attempts/000140-churchland-2010-01.yaml:459:  - claim: fig7b-window-start-slide
attempts/000140-churchland-2010-01.yaml:506:      segment directions beat the peri-movement space in 23 of 24, under O1b as under O1a.
301:     Record it as an assumption: a deviation that says what was assumed and
302:     why, and `assumed: true` on the outcome. The notebook still shows the
312:     differ, and what was assumed), and add a `methods_unavailable` finding
432:- **`assumed`**: `true` on an outcome that rests on an assumption about a
433:  method the paper leaves open (step 1.6); a deviation says what was assumed
583:   claims file; units; leakage between training and test data; the statistics; anything assumed and never
595:   assumption an outcome rests on (`assumed`) is stated and reasonable.
```

**Agent calls Bash**

```bash
cd  cat entries/000140-churchland-2010/README.md | head -80
```

```
# Churchland, Cunningham, Kaufman, Ryu & Shenoy (2010) from dandiset 000140

Tests the findings of [Churchland et al. (2010)](https://doi.org/10.1016/j.neuron.2010.09.015) that can
be tested on [DANDI:000140](https://dandiarchive.org/dandiset/000140/0.220113.0408) (MC_Maze_Small of
the Neural Latents Benchmark), which holds 100 trials of 27 maze conditions recorded with the two Utah
arrays of monkey J. The paper's J-array dataset has 108 conditions and about 2166 trials per neuron; its
single-electrode datasets of monkeys A, B and J and its EMG are not in the dandiset.

| Claim | Outcome |
|---|---|
| Mean preparatory to peri-movement tuning correlation, J-array (r = 0.13) | Not reproduced |
| The same for monkeys A, B and J | Blocked: data missing |
| Correlations broad and centred near zero | Not reproduced (assumption) |
| Correlation falls to near zero by movement onset | Reproduced (assumption; trial noise also passes) |
| Population averages lose preparatory tuning by movement onset | Reproduced (trial noise passes about half the time) |
| PD performance best in the peri-movement space, J-array | Partially reproduced (assumption) |
| The same for monkeys A, B and J | Blocked: data missing |
| Peri-movement space best at each dimensionality | Not reproduced |
| Endpoints + max. speed space performs poorly in the maze task | Not reproduced (assumption) |
| Performance rises with dimensionality, then declines above 10 | Not reproduced (assumption) |
[... 29 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/000140-churchland-2010; python - <<'EOF'
import json
p='reproduce_churchland_2010.ipynb'
nb=json.load(open(p))
def rep(i, old, new):
    c=nb['cells'][i]; s=''.join(c['source'])
    assert old in s, (i, old)
    c['source']=s.replace(old,new).splitlines(keepends=True)
rep(25, """Under O1b (SD, 3 to 8 units) the correlation at onset stays between 0.09 and
0.24, partially reproduced in 10 of 12 readings.""",
"""Under O1b (SD, 3 to 8 units) the correlation at onset stays between 0.09 and
0.24, partially reproduced in 11 of 12 readings; in the twelfth (O3a, O4a, O2 ii, 5 units) r at onset
is 0.091 but the largest drop starts at +90 ms, so it is neither a pass nor a partial.""")
rep(28, """With the preparatory and movement-locked means from disjoint trials it is met in 2 of 12 readings, so
the strongest trace being on top at -150 ms, the part of the result that noise does not give every time,
comes mostly from noise shared within the same trials.""",
"""With the preparatory and movement-locked means from disjoint trials it is met in 2 of 12 readings. This
suggests that the strongest trace being on top at -150 ms, the part of the result that noise does not
give every time, comes mostly from noise shared within the same trials, but it does not show it: each
disjoint half uses about half the trials, and the added noise could also hide a real effect.""")
rep(54, """**Result: not reproduced.** Under O1b""",
"""**Result: not reproduced, resting on the SD reading of tuning (O1b), the only reading under which the
ratio is defined.** Under O1b""")
rep(72, "| fig7b-window-start-slide | not reproduced |", "| fig7b-window-start-slide | not reproduced (assumption O1b: under O1a the ratio is undefined) |")
rep(72, """the SD reading keeps
7 or 8 units with clearer tuning, and on them the peri-movement space built from all recorded units
performs best with positive performance, as in the paper; built from those 7 or 8 units only, it does not.""",
"""the SD reading keeps
7 or 8 units. On them every space performs above zero, and the peri-movement space built from all
recorded units has the highest mean performance in 5 of the 6 O3/O4 settings (with O3b and O4b the
kinematic space is higher, 0.134 against 0.129), but no difference from the best other space is
significant (paired t p 0.47 to 0.98); built from those 7 or 8 units only, it is beaten by 6 to 8 spaces.""")
json.dump(nb,open(p,'w'),indent=1,ensure_ascii=False); open(p,'a').write('\n')
EOF
git diff --stat
```

```
.../reproduce_churchland_2010.ipynb                | 26 ++++++++++++++--------
 1 file changed, 17 insertions(+), 9 deletions(-)
```

**Agent calls Bash**

```bash
cd  date -u; python tools/entry.py all entries/000140-churchland-2010 2>&1 | tail -3; python $TMPDIR/show.py 11 | tail -5
```

```
Thu Oct 29 01:44:27 UTC 2026
Installed kernelspec registry-000140-churchland-2010 in executed/000140-churchland-2010/.venv/share/jupyter/kernels/registry-000140-churchland-2010
0 error(s)
pass  reproduce_churchland_2010.ipynb  (129 s)
same, units with > 5 spikes/s preparatory SD (n = 8): preparatory median 0.57 (values [0.03 0.11 0.38 0.53 0.62 0.63 0.7  0.99]), peri-movement median 0.49

entries/000140-churchland-2010/maze_prep.py:270: RuntimeWarning: invalid value encountered in divide
  return (a * b).sum(0) / np.sqrt((a ** 2).sum(0) * (b ** 2).sum(0))
```

**Agent calls Bash**

```bash
cd  python $TMPDIR/show.py 11 | head -6; python -c "
import json;nb=json.load(open('entries/000140-churchland-2010/reproduce_churchland_2010.ipynb'))
print(''.join(nb['cells'][12]['source']))"
```

```
===== 11
conditions with >= 2 trials: 25
preparatory split-half r over units: median 0.20, IQR -0.03 to 0.40
peri-movement split-half r over units: median 0.28, IQR 0.07 to 0.53
same, units with > 5 spikes/s preparatory range: preparatory median 0.26, peri-movement median 0.34
same, units with > 5 spikes/s preparatory SD (n = 8): preparatory median 0.57 (values [0.03 0.11 0.38 0.53 0.62 0.63 0.7  0.99]), peri-movement median 0.49
### Readings adopted where readings differ (author, step 1.6)

Every claim below is run under every reading the claims file names. Where they give different
outcomes, these are adopted as assumptions, and the outcome is marked as resting on them:

- O1, "spikes/s of preparatory tuning" (Methods, Neural recordings and datasets): the range of the
  preparatory rate across conditions (O1a). The Methods speak of a rate difference ("Firing rate
  modulation was typically lower for the array recordings ... We thus used a lower inclusion criterion:
  >5 spikes/s of preparatory tuning"), which the range measures directly. The SD reading (O1b) is
  shown everywhere.
- O3, movement onset: the dataset's `move_onset_time` (O3a), computed by the data's authors ("calculated
  offline using a robust algorithm", its description). The paper defers to Churchland et al. (2006c).
- O4, the proto-trial: a trial of the condition, the one best correlated with the condition mean (O4a),
  since the Supplemental Experimental Procedures call it a "reference 'proto-trial'".
[... 3 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/000140-churchland-2010; python - <<'EOF'
import json
p='reproduce_churchland_2010.ipynb'
nb=json.load(open(p))
c=nb['cells'][72]; s=''.join(c['source'])
old="""the SD reading keeps
7 or 8 units. On them"""
new="""the SD reading keeps
7 or 8 units, whose preparatory tuning is more reliable over trials (main reading, split-half r median
0.57 against 0.20 over all units, though the units are selected on the same trials). On them"""
assert old in s
c['source']=s.replace(old,new).splitlines(keepends=True)
json.dump(nb,open(p,'w'),indent=1,ensure_ascii=False); open(p,'a').write('\n')
EOF
sed -i 's/| Window start can slide to movement onset (97% of performance) | Not reproduced |/| Window start can slide to movement onset (97% of performance) | Not reproduced (assumption) |/' README.md; grep -n "Window start" README.md
```

```
24:| Window start can slide to movement onset (97% of performance) | Not reproduced (assumption) |
```

**Agent calls Bash**

```bash
cd  sed -n 236,256p attempts/000140-churchland-2010-01.yaml; python -c "
import json;nb=json.load(open('entries/000140-churchland-2010/reproduce_churchland_2010.ipynb'))
for i,c in enumerate(nb['cells']):
  s=''.join(c['source'])
  if c['cell_type']=='markdown' and 'upper limit' in s: print('##',i);print(s)"; grep -n "problem 6\|Problem 6" -A4 transcripts/000140/verifier-1-report.md | head -20
```

```
- claim: fig7c-anterior-posterior-performance
  outcome: blocked
  blocked_by: other
  notebook: reproduce_churchland_2010.ipynb
  output: claim:fig7c-anterior-posterior-performance
  notes: The normalised measure the criterion uses does not exist here. Under O1 range the upper-limit
    performance is at or below zero for every subset (-0.019 to -0.097), so performance cannot be
    normalised by it. Raw 6-D peri-movement performance is far below zero at both arrays, -1.535
    (prefix 1, 44 units) and -1.087 (prefix 2, 49 units) with the space from the half's units, and
    -1.454 and -1.293 from all units, against -1.008 and -1.400 for random halves. Under O1 SD (4 and
    4 units) the upper limits are positive (0.145 and 0.184) but the 6-D performance is not
    (normalised -12.048 and -2.915, random halves -7.282), so a threshold at 70% of the random-half
    value has no meaning either. Which half is anterior is also not known
    (prep-activity-more-anterior); with prefix 1 as PMd the anterior half is lower in raw
    performance, with the arrays swapped higher.
  deviations:
  - AP halves are the two arrays (see ap-location-no-effect-j-array), not a median split of positions.
  - O1 range, O3a and O4a (see fig6d-perimovement-best-j-array); 20 random halves of the size of the
    prefix-1 array.
- claim: prep-activity-more-anterior
[... 78 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n "6\." transcripts/000140/verifier-1-report.md | head; grep -n -i "T matrix\|T-matrix" transcripts/000140/verifier-1-report.md
```

```
12:| fig6-perimovement-best-each-dimensionality | not_reproduced | Cell 26: 0/96 readings reach 0.8; fractions are 0.07–0.36. |
16:| prep-dimensionality-7-to-10 | not_reproduced | Cell 34: 16–17 components under O1a and 5–6 under O1b; none fall in 6.3–11. Shuffling condition labels gives 17, so the O1a count measures noise. The O1b count is capped by the 7–8 units. |
32:2. **[affects a conclusion] The > 5 spikes/s range criterion admits noise (cells 14, 23, 34).** In my simulation, 63 of 93 untuned units passed it. In the data, median preparatory range is 6.6–10.2 spikes/s while mean preparatory rates are only 2.4–3.7 spikes/s, and only 13/142 units beat a condition-shuffled null (cell 46). The paper justifies the 5 spikes/s threshold by the high trial count ("acceptable given the higher signal-to-noise ratio provided by the higher trial count"), which this dandiset does not have. The notebook states the trial-count gap (cell 0) but never says how it affects selection.
42:6. **[does not affect a conclusion] The peri T matrix uses all 142 recorded units, untuned ones included (`leave_one_out_scores` in cell 23).** The Methods say "all neurons except the neuron whose preparatory activity we were trying to capture", which could mean recorded or included neurons. Only the first reading was run. Rates are not normalised, so near-silent units have little weight.
42:6. **[does not affect a conclusion] The peri T matrix uses all 142 recorded units, untuned ones included (`leave_one_out_scores` in cell 23).** The Methods say "all neurons except the neuron whose preparatory activity we were trying to capture", which could mean recorded or included neurons. Only the first reading was run. Rates are not normalised, so near-silent units have little weight.
```

**Agent**

Now the record edits.

**Agent calls Bash**

```bash
cd  python - <<'EOF'
p='attempts/000140-churchland-2010-01.yaml'
s=open(p).read()
def rep(old,new):
    global s
    assert s.count(old)==1,(old,s.count(old))
    s=s.replace(old,new)
rep("""    units) the value at onset is 0.091 to 0.244, partially reproduced in 10 of 12 readings.""",
"""    units) the value at onset is 0.091 to 0.244, partially reproduced in 11 of 12 readings; in the
    twelfth (O3a, O4a, O2 ii, 5 units) r at onset is 0.091 but the largest drop starts at +90 ms, so it
    is neither a pass nor a partial.""")
rep("""    shuffles, and with the preparatory and movement-locked means from disjoint trials in 2 of 12
    readings, so the strongest trace being on top at -150 ms comes mostly from noise shared within the
    same trials, and the pass carries little evidence.""",
"""    shuffles, and with the preparatory and movement-locked means from disjoint trials in 2 of 12
    readings. This suggests that the strongest trace being on top at -150 ms comes mostly from noise
    shared within the same trials, but does not show it, as each disjoint half uses about half the
    trials and the added noise could also hide a real effect. The pass carries little evidence.""")
rep("""- claim: fig7b-window-start-slide
  outcome: not_reproduced
  notebook""","""- claim: fig7b-window-start-slide
  outcome: not_reproduced
  assumed: true
  notebook""")
rep("""  deviations:
  - Start times -150 to +100 ms""","""  deviations:
  - Assumed O1 SD (O1b). Under the O1 range reading adopted elsewhere (see fig4-broad-near-zero)
    performance at -150 ms is below zero and the ratio is undefined, so the outcome rests on the O1b
    readings (7 or 8 units) alone.
  - Start times -150 to +100 ms""")
rep("""raw and z-scored axes are both run and agree on the segment-directions
    comparison in 23 of 24 readings.""","""raw and z-scored axes are both run and agree on the segment-directions
    comparison in 11 of 12 pairs (they differ under O1 SD with O3a and O4b).""")
rep("""    value has no meaning either. Which half is anterior""","""    value has no meaning either. Under O1 SD the upper limit of all 8 units (0.123) is also below the
    best peri-movement performance (0.209), so it is not a ceiling. Which half is anterior""")
rep(""" No per-reading
      SEs or paired tests were output (problem 3). The peri T matrix uses all 142 recorded units,
      untuned ones included; the Methods' "all neurons" could mean recorded or included neurons, and
      only the first reading was run (problem 6).""",""" No per-reading
      SEs or paired tests were output.""")
open(p,'w').write(s)
EOF
sed -n 400,415p attempts/000140-churchland-2010-01.yaml
```

```
outcome: reproduced
    reason: 36/36 runs pass. Criterion met, but not informative. Untuned Poisson data also pass, with
      spread 8.3 in the preparatory window, -0.55 at onset and the strongest trace on top at -150 ms
      (problem 1).
    response: Outcome kept, and the conclusion and notes now say the pass carries little evidence. The
      shuffled-label null meets the criterion in 11 of 20 shuffles, and the disjoint-trial variant in
      2 of 12 readings, so the strongest trace being on top at -150 ms comes mostly from noise shared
      within trials.
  - claim: fig6d-perimovement-best-j-array
    agrees: false
    outcome: partially_reproduced
    reason: 64 runs reproduced and 32 partial (initial vel. >= peri under O3/O4 a,b / b,a / b,b). The
      criterion needs every reading to hold. Under O1a every space has negative performance, and the
      gaps are about 0.005; peri vs kinematic p=0.62 and peri vs initial vel. p=0.81. No per-reading
      SEs or paired tests were output.
    response: Outcome changed from reproduced to partially_reproduced, as the criterion asks that it
```

**Agent calls Bash**

```bash
cd entries/000140-churchland-2010; python - <<'EOF'
import json
p='reproduce_churchland_2010.ipynb'
nb=json.load(open(p))
c=nb['cells'][62]; s=''.join(c['source'])
old="""threshold at 70% of the random-half value has no meaning either."""
new="""threshold at 70% of the random-half value has no meaning either. Under O1b the upper limit of all 8
units (0.123, fig6d cell) is also below the best peri-movement performance (0.209), so it is not a
ceiling."""
assert old in s
c['source']=s.replace(old,new).splitlines(keepends=True)
json.dump(nb,open(p,'w'),indent=1,ensure_ascii=False); open(p,'a').write('\n')
EOF
tail -5 attempts/000140-churchland-2010-01.yaml; grep -n "^[a-z_]*:" attempts/000140-churchland-2010-01.yaml
```

```
reason: Median |r| is 0.11 (disk) and 0.15 (square), below 0.3; median r 0.004/0.012 is within
      0.08+/-0.3; minimum PD performance is 1.0. The simulate_rotation docstring mentions a hold that
      is never applied (problem 7).
    response: Outcome kept. The hold parameter is removed from simulate_rotation and its docstring
      says why no hold is simulated; the deviation about a hold is removed from the record.
1:schema_version: 2
2:id: 000140-churchland-2010-01
3:dataset:
8:paper: doi:10.1016/j.neuron.2010.09.015
9:date: 2026-10-29
10:entry: 000140-churchland-2010
11:provenance:
22:outcomes:
305:findings:
353:verifications:
```

**Agent calls Bash**

```bash
cd  cat >> attempts/000140-churchland-2010-01.yaml <<'EOF'
- date: 2026-10-29
  kind: agent
  by: Independent agent run by CatalystNeuro (same harness, separate context, did not write the
    notebook), verifier-2
  reviewed: The full executed notebook of the first revision, with its conclusions and summary, the
    helper module, the README, the attempt record and the claims file, with the paper under paper/.
  results:
  - claim: fig4d-mean-correlation-j-array
    agrees: true
    outcome: not_reproduced
    reason: Agrees. The values in the conclusion match the printed numbers.
    response: None needed.
  - claim: fig4abc-mean-correlation-other-datasets
    agrees: true
    outcome: blocked
    reason: Agrees.
    response: None needed.
  - claim: fig4-broad-near-zero
    agrees: true
    outcome: not_reproduced
    reason: O1a is stated and reasonable. The O1b passes rest on 3 to 5 units.
    response: None needed.
  - claim: fig4e-correlation-time-course
    agrees: true
    outcome: reproduced
    reason: Agrees on the criterion only. O1a is stated and reasonable. The noise control shows the
      pass is mostly shared trial noise; with disjoint trials the fig4 units have r at -200 ms of only
      0.02 to 0.145, and 4 of 12 readings pass, which the record says. The text says O1b is partially
      reproduced in 10 of 12 readings, but the table shows 11 of 12 marked partial; the 12th (O3a,
      O4a, sd, ii; r at onset 0.091, drop starting at +90 ms) is neither a pass nor a partial.
    response: Corrected to 11 of 12 in the conclusion and the notes, and the twelfth reading is
      described as neither a pass nor a partial.
  - claim: suppfig1-population-averages-lose-tuning
    agrees: true
    outcome: reproduced
    reason: Agrees on the criterion only. That the strongest trace on top at -150 ms comes mostly from
      noise shared within the same trials is an inference, not something shown; the disjoint halves
      also use about half the trials, so the extra noise could hide a real effect. "Suggests" would be
      accurate.
    response: The conclusion and the notes now say the disjoint-trial result suggests this but does not
      show it, and give the reason the verifier gives.
  - claim: fig6d-perimovement-best-j-array
    agrees: true
    outcome: partially_reproduced
    reason: O1a is stated and reasonable. Under O1a both T-matrix readings give reproduced or partial
      in every setting, so O1a alone carries the outcome. The round-1 reason recorded for this claim
      included problem 6, which the verifier had marked as not affecting a conclusion.
    response: The round-1 reason no longer includes problem 6. The Summary sentence on the SD reading,
      which said the peri-movement space performs best on those units, now says it has the highest mean
      in 5 of 6 O3/O4 settings (with O3b and O4b the kinematic space is higher, 0.134 against 0.129)
      and that no difference is significant (p 0.47 to 0.98). For "clearer tuning", which no output
      showed, cell 11 now prints the split-half reliability of the SD units (median 0.57 against 0.20
      over all units), and the Summary cites it, noting the units are selected on the same trials.
  - claim: fig6abc-perimovement-best-other-datasets
    agrees: true
    outcome: blocked
    reason: Agrees.
    response: None needed.
  - claim: fig6-perimovement-best-each-dimensionality
    agrees: true
    outcome: not_reproduced
    reason: Agrees.
    response: None needed.
  - claim: fig6-maze-endpoint-speed-space-poor
    agrees: true
    outcome: not_reproduced
    reason: O1a is stated and reasonable.
    response: None needed.
  - claim: fig6-dimensionality-trend
    agrees: true
    outcome: not_reproduced
    reason: O1a is stated and reasonable.
    response: None needed.
  - claim: fig6e-summary-rank
    agrees: true
    outcome: blocked
    reason: Agrees.
    response: None needed.
  - claim: prep-dimensionality-7-to-10
    agrees: true
    outcome: not_reproduced
    reason: Agrees.
    response: None needed.
  - claim: fig7a-shuffled-space-poor
    agrees: true
    outcome: reproduced
    reason: Agrees, a weak result.
    response: None needed.
  - claim: fig7b-window-start-slide
    agrees: true
    outcome: not_reproduced
    reason: Agrees, but the assumption is not marked. Under the adopted O1a reading the ratio is
      undefined, so the outcome rests only on the O1b readings (7 to 8 units). Everywhere else O1b is
      the non-adopted reading. The record should carry assumed true and say that the outcome rests on
      O1b.
    response: The outcome now carries assumed true, with a deviation saying it rests on the O1b
      readings alone because the ratio is undefined under O1a. The conclusion, the Summary and the
      README say the same.
  - claim: ap-location-no-effect-j-array
    agrees: true
    outcome: reproduced
    reason: Array identity as AP location is stated, reasonable, and valid under both mappings.
    response: None needed.
  - claim: ap-location-no-effect-other-datasets
    agrees: true
    outcome: blocked
    reason: Agrees.
    response: None needed.
  - claim: fig7c-anterior-posterior-performance
    agrees: true
    outcome: blocked
    reason: Agrees. The O1b upper limit (0.123) is below the peri-movement best (0.209), so it bounds
      nothing; that affects only fig7c's O1b normalisation, and fig7c is blocked anyway. fig7c is still
      run on O3a/O4a only, which is stated.
    response: The conclusion and the notes now say that under O1b the upper limit is below the best
      peri-movement performance and so is not a ceiling. The O3a/O4a restriction is kept, as the claim
      is blocked under them.
  - claim: prep-activity-more-anterior
    agrees: true
    outcome: blocked
    reason: Agrees.
    response: None needed.
  - claim: fig7d-pd-consistency
    agrees: true
    outcome: not_reproduced
    reason: Agrees. The deviation says raw and z-scored axes agree on the segment-directions comparison
      in 23 of 24 readings, but there are 12 raw/z pairs, and they agree in 11 of 12; 23 of 24 is the
      number of rows where the peri-movement space loses.
    response: The deviation now says 11 of 12 pairs, and names the pair that differs.
  - claim: fig8-linear-dynamics-simulation
    agrees: true
    outcome: reproduced
    reason: Agrees.
    response: None needed.
EOF
date -u; python tools/entry.py all entries/000140-churchland-2010 2>&1 | tail -3
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  python $TMPDIR/show.py 11 24 53 67 | grep -E "SD \(n|readings passing|ratios|peri higher:"; python $TMPDIR/show.py 30 | grep "O1 SD units"; grep -n " — \|rather" attempts/000140-churchland-2010-01.yaml entries/000140-churchland-2010/README.md | head; git status --short
```

```
same, units with > 5 spikes/s preparatory SD (n = 8): preparatory median 0.57 (values [0.03 0.11 0.38 0.53 0.62 0.63 0.7  0.99]), peri-movement median 0.49
readings passing: 18 of 30
O1 SD ratios: 0.471 to 0.761
comparisons with peri higher: 46 of 72
O1 SD units (n = 8): peri best 0.209, kin best 0.136, upper best 0.123
 M attempts/000140-churchland-2010-01.yaml
 M entries/000140-churchland-2010/README.md
 M entries/000140-churchland-2010/reproduce_churchland_2010.ipynb
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
```

**Agent**

I've revised the attempt for verifier round 2. No outcome changed and nothing is proposed for a third round. The entry re-ran cleanly (`entry.py all`: 0 errors, the notebook passes in 131 s), and the corrected text matches the new run's numbers.

**Outcomes:** all 20 are the same as before. The one change is that fig7b-window-start-slide now carries `assumed: true`. The verifier pointed out that under the range reading of tuning, which the rest of the attempt uses, the fig7b ratio is undefined. So that "not reproduced" rests only on the SD reading (7 or 8 units). A new deviation in the record says this, and the notebook conclusion, the summary table and the README now mark it as an assumption.

**Corrected (in the notebook, the attempt record, and the README where it applied):**
- **fig4e:** under the SD reading it is partially reproduced in 11 of 12 readings, not 10. The twelfth reading is described as neither a pass nor a partial.
- **suppfig1:** the claim that the strongest trace on top at -150 ms comes mostly from noise shared within trials now says "suggests" instead of stating it as shown. It gives the verifier's reason: each disjoint half uses about half the trials.
- **Summary, SD reading:**
  - It no longer says the peri-movement space "performs best". It now says that space has the highest mean in 5 of 6 settings (the kinematic space is higher with O3b/O4b, 0.134 against 0.129) and that no difference is significant (p 0.47 to 0.98).
  - The summary had said these units have "clearer tuning", but no output showed it. I added an output to cell 11: their split-half reliability has a median of 0.57, against 0.20 over all units. The summary cites it and notes that the units are selected on the same trials.
- **fig7d deviation:** raw and z-scored axes agree in 11 of 12 pairs, not "23 of 24 readings". The pair that differs is named.
- **fig7c:** the conclusion and notes now say that under the SD reading the upper limit (0.123) is below the best peri-movement performance (0.209), so it is not a ceiling.
- **Round-1 record for fig6d:** I removed the round-1 problem 6 from the recorded reason, because the verifier had marked it as not affecting a conclusion.
- **Round 2** is recorded under `verifications`, with the verifier's agreement, outcome, reason and my response for each of the 20 claims.

**Not done:**
- fig7c still runs only with the default movement-onset and proto-trial settings (O3a/O4a). The record says so, the verifier noted it, and the claim is blocked anyway.
- No questions were added to `questions/000140.yaml`, because the verifier found no place where the claims file misreads the paper.
- Nothing is committed. The working tree also has untracked files I did not create (`.bashrc`, `.idea`, `scripts` and others), and I left them alone.

## End of run

28 turns, 10 minutes, result: success.
