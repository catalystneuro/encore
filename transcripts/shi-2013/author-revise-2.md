# shi-2013 · author-revise-2 · run 42703026687

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
date -u; cat transcripts/shi-2013/verifier-2-report.md; ls entries/shi-2013 transcripts/shi-2013
```

```
Mon Nov  9 21:36:06 UTC 2026
**Verifier report, round 2: Shi, Apker & Buneo 2013 on CRCNS ppc-1**

The claims file has 28 claims, and the attempt record gives an outcome for each of them. The record has 7 reproduced, 5 partially reproduced, 13 not reproduced and 3 blocked. Twelve outcomes are marked `assumed: true`. Cell indices below refer to the re-executed notebook. They have shifted since round 1.

### 1. Outcomes

I agree with all 28 outcomes in the record. Three of them differ from what I gave in round 1:

- **fig4-indx1-means: partially_reproduced.** I now agree. The criterion requires two things. The Position Only part holds in full: −12.0% is within −13 ± 1.3, and it is the least negative group. The Position/Vision part fails: −24.2% is outside −31 ± 3.1, and it is not the most negative group (cell 67). Calling that partial is defensible.
- **rate-variance-nv-higher: partially_reproduced.** I now agree, but only just. The criterion is purely numerical, and both means are outside tolerance: 46.4 against a bound of 50.4, and 23.1 against 27 (cell 78). The "tended to be higher" part of the statement does hold: NV is higher in 67% of cells, at about twice the V value. That direction rests on the code mapping, and the record flags this.
- **longer-hold-no-difference: blocked (data_missing).** I now agree. The per-trial table (cell 15) removes my round-1 objection. No completed trial has a code 10 to code 12 interval shorter than its own field 11 plus 28 ms. This supports reading field 11 as the minimum hold. No completed trial has field 11 ≥ 1,200.

**Assumptions.** Each flagged assumption is stated in the deviations and is reasonable:

- movement onset read as code 8
- the first sorted unit in each session (hold-vision-main-effect, hold-subepochs, fig4-indx1-negative, decoding-subepochs; the all-units variant changes each of these, as the notebook shows)
- correlation reading (a)
- FF outlier reading (a)
- CV2 reading (a)
[... 64 more lines not kept]
```

**Agent calls Bash**

```bash
grep -n "^#" docs/protocol.md | head -60; grep -n -i "verifications" docs/protocol.md | head -30
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
[... 2 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 433,532p docs/protocol.md
```

```
### 5. Record the attempt

Write `attempts/<paper>-<nn>.yaml`, numbered after the paper's earlier attempts.

- **`datasets`**: every dataset the attempt used, each with `archive`, `id`,
  the pinned `version`, its `doi` where the archive gives one, and
  `relation` as `papers/datasets/<paper>.yaml` gives it (`primary` or
  `reuses`). Use as many of the paper's datasets as can be loaded.
- **`missing_datasets`**: each dataset the paper's claims rest on that this
  attempt could not use, with `archive` and `id` where it has them, and
  `why` (not in any open archive, not yet converted, unreadable). A missing
  dataset does not stop the attempt: test what the others allow, and block
  each claim that needs a missing one with `dataset_missing`. The site flags
  the attempt, so that a later one can add the dataset.

- **One outcome per claim**, including blocked ones. The outcome describes the
  result, not the method:
  - `reproduced`: the result matches the claim.
  - `partially_reproduced`: the effect is present but weaker, or holds only in
    part.
[... 79 more lines not kept]
```

**Agent calls Bash**

```bash
ls attempts 2>/dev/null | grep shi; find . -path ./node_modules -prune -o -name "*shi-2013*" -print | grep -v "^./transcripts" | head
```

```
ishii-2025-01.yaml
shi-2013-01.yaml
shin-2025-01.yaml
./attempts/shi-2013-01.yaml
./.git/refs/remotes/origin/attempt/shi-2013
./.git/refs/heads/attempt/shi-2013
./.git/logs/refs/remotes/origin/attempt/shi-2013
./.git/logs/refs/heads/attempt/shi-2013
./papers/datasets/shi-2013.yaml
./claims/shi-2013.yaml
./entries/shi-2013
./questions/shi-2013.yaml
```

**Agent calls Bash**

```bash
wc -l attempts/shi-2013-01.yaml; grep -n "^[a-z_]*:" attempts/shi-2013-01.yaml; grep -n "verifications" -A60 attempts/shi-2013-01.yaml | head -120
```

```
745 attempts/shi-2013-01.yaml
1:schema_version: 3
2:id: shi-2013-01
3:datasets:
9:paper: doi:10.1152/jn.00223.2012
10:date: 2026-11-09
11:entry: shi-2013
12:provenance:
23:outcomes:
467:findings:
516:verifications:
516:verifications:
517-- date: '2026-11-09'
518-  kind: agent
519-  by: Independent agent run by CatalystNeuro (same harness, separate context, did not write the notebook)
520-  reviewed: The first executed notebook with the conclusion cells and the summary removed, the helper
521-    module (ppc.py) and the claims file, with the paper's full text under paper/. The verifier checked
522-    anova2 and hotelling2 against statsmodels and decode on synthetic data, and took the claims from
523-    the claims file.
524-  results:
[... 52 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 576,745p attempts/shi-2013-01.yaml
```

```
(142). The analysis window was not shown to lie inside the hold (B3).'
    response: 'Added a per-trial table of code 10 to code 12 against the trial''s own field 11: on
      all 30,789 completed trials the interval is at least field 11 plus 28 ms, so the 800 ms window
      lies in the hold as the task timed it (the 0.832 s intervals are on trials with field 11 = 800).
      In 11.6% of trials the window starts less than 250 ms after code 10. Outcome unchanged.'
  - claim: hold-vision-main-effect
    agrees: true
    outcome: reproduced
    reason: 49/359 (13.6%, 47 scaled to 343), against 44 +/- 4.4, and fewer than position. The all-units
      variant (49 scaled) falls just outside.
    response: 'Outcome kept, now marked as resting on the assumption of the first sorted unit per
      session, as all units fall just outside. Population (B1, B5): added a data check of recording
      dates, geometry by month and same-day tuning; all 359 sessions predate submission, have monkey
      X''s layout and are distinct neurons, so the extra sessions over the paper''s 219 remain unexplained
      (selection_undocumented finding).'
  - claim: hold-interaction
    agrees: true
    outcome: reproduced
    reason: 27/359 (7.5%, 26 scaled to 343), against 27 +/- 2.7 (reading a).
    response: No change.
[... 150 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/shi-2013; cat entry.yaml | head -40; ls ../../executed/shi-2013 2>/dev/null; python - <<'EOF'
import json
nb=json.load(open('reproduce_shi_2013.ipynb'))
for i,c in enumerate(nb['cells']):
    s=''.join(c['source'])
    for k in ["follows its field 11","by 320 ms","0.22 to 0.58","0.54 to 0.96","only the test over bootstraps","give the same","position percentages are close","the closest, outliers","0.03 to 0.38"]:
        if k in s: print(i,c['cell_type'],repr(k))
EOF
```

```
schema_version: 1
name: shi-2013
type: reproduction
title: Limb position, vision and area 5 activity (Shi, Apker and Buneo 2013)
description: Tests the findings of Shi, Apker and Buneo (2013) on CRCNS ppc-1, which holds the
  sorted spikes and trial events of area 5 recordings while monkeys held the arm at eight targets
  with or without vision of a cursor. It compares hand positions, ANOVA effect counts, suppression
  indexes, variability and decoding between the Vision and No Vision conditions. The data set holds
  monkey X's sessions only, and which condition code is Vision is inferred from the data.
license: Apache-2.0
notebooks:
- path: reproduce_shi_2013.ipynb
  title: Reproducing Shi et al. (2013) from CRCNS ppc-1
  runtime_minutes: 5
helpers:
- ppc.py
related:
- id: crcns:ppc-1/unversioned
  relation: uses_data
- id: doi:10.1152/jn.00223.2012
[... 13 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python - <<'EOF'
import json
nb=json.load(open('entries/shi-2013/reproduce_shi_2013.ipynb'))
for i in [9,10,15,56,59,67,68,75,76,90,93,98,111,112]:
    c=nb['cells'][i]
    print('=====',i,c['cell_type'])
    print(''.join(c['source'])[:3000])
    if c['cell_type']=='code':
        for o in c.get('outputs',[]):
            print('--out--'); print(''.join(o.get('text',''))[:2500])
EOF
```

```
===== 9 code
allt = pd.concat([s["trials"].assign(session=k) for k, s in D["sessions"].items()], ignore_index=True)
print("trials:", len(allt), " completed (code 12):", int(allt.completed.sum()), " aborted (code 14):",
      int(allt.aborted.sum()))
print("record length (fields) per trial:")
print(allt.nrec.value_counts().to_string())
c = allt[allt.completed & allt.target.notna()]
print("completed trials by target code and field 14:")
print(pd.crosstab(c.target, c.cond).to_string())
iv = pd.DataFrame({
    "3 - t0 (start held, target on?)": c.t3 - c.t0,
    "8 - 3 (reaction time?)": c.t8 - c.t3,
    "target code - 8 (movement time?)": c.t_target - c.t8,
    "10 - target code": c.t10 - c.t_target,
    "12 - 10": c.t12 - c.t10,
    "13 - 12": c.t13 - c.t12,
})
print("intervals between events on completed trials (s):")
print(iv.describe(percentiles=[0.05, 0.5, 0.95]).T.round(3).to_string())
===== 10 markdown
[... 171 more lines not kept]
```

**Agent calls Bash**

```bash
python tools/entry.py --help 2>&1 | head -30; ls executed/ 2>/dev/null | head
```

```
usage: entry.py [-h] [--output-dir OUTPUT_DIR] [--timeout TIMEOUT]
                [--max-minutes MAX_MINUTES] [--python PYTHON]
                [--before BEFORE]
                {lock,check,run,all,handover,upgrade-python} entry [entry ...]

Lock, check and run one entry. This is the whole local workflow for a deposit.

    python tools/entry.py lock  entries/<name>   # pin the environment
    python tools/entry.py check entries/<name>   # validate metadata and conventions
    python tools/entry.py check entries/*/       # the same for every entry, in one process
    python tools/entry.py run   entries/<name>   # execute every notebook from a clean environment
    python tools/entry.py all   entries/<name>   # check, then run
    python tools/entry.py handover entries/<name> # the verifier's package, from the executed copies

`lock` compiles the entry's requirements.in (direct dependencies only) into
requirements.lock.txt with every version pinned.

`check` validates entry.yaml, and the claims and attempt files that mention
the entry, against the schemas, and applies the conventions that keep a result
tied to the data:
[... 10 more lines not kept]
```

**Agent calls Bash**

```bash
find / -name "reproduce_shi_2013*.ipynb" -not -path "*/proc/*" 2>/dev/null
```

```
entries/shi-2013/reproduce_shi_2013.ipynb
```

**Agent**

I'll run the entry now to get the current outputs (about 5 minutes per the entry metadata), then fix the text.

**Agent calls Bash**

```bash
time python tools/entry.py all entries/shi-2013 2>&1 | tail -15; ls executed/shi-2013
```

```
Installed kernelspec registry-shi-2013 in executed/shi-2013/.venv/share/jupyter/kernels/registry-shi-2013
0 error(s)
pass  reproduce_shi_2013.ipynb  (329 s)

real	5m39.229s
user	1m53.691s
sys	0m12.958s
reproduce_shi_2013.ipynb
result.json
```

**Agent calls Bash**

```bash
python - <<'EOF'
import json
nb=json.load(open('executed/shi-2013/reproduce_shi_2013.ipynb'))
for i in [9,15,56,67,75,90,111]:
    c=nb['cells'][i]
    print('=====',i)
    for o in c.get('outputs',[]):
        print(''.join(o.get('text',''))[:6000])
EOF
```

```
===== 9
trials: 54116  completed (code 12): 31330  aborted (code 14): 22756
record length (fields) per trial:
nrec
24    33438
22    19509
19     1132
0        37
completed trials by target code and field 14:
cond    2.0   4.0   7.0
target                 
44.0      0  1948  1930
45.0      0  1934  1915
46.0      0  1933  1916
54.0      0  1932  1910
56.0      0  1929  1910
64.0      1  1933  1914
65.0      0  1932  1911
66.0      0  1932  1909
intervals between events on completed trials (s):
[... 116 more lines not kept]
```

**Agent calls Bash**

```bash
python - <<'EOF'
import json
nb=json.load(open('entries/shi-2013/reproduce_shi_2013.ipynb'))
for i in [65,70,103,105,106]:
    c=nb['cells'][i]
    print('=====',i,c['cell_type']); print(''.join(c['source'])[:2500])
EOF
grep -n "near the paper\|0.22 to 0.58\|0.03 to 0.38\|fig6-decoding-vv\|assumed: true\|22 and 23\|Levene\|follows its field\|320 ms\|bootstraps finds\|give the same" attempts/shi-2013-01.yaml entries/shi-2013/README.md
```

```
===== 65 markdown
**Result: reproduced (resting on an assumption).** With each cell's V and NV mean rates at a
target as the pair (reading (a)), r is 0.9237 where endpoints differed (463 pairs) and 0.9154 where
they did not (2,409), both within 0.093 of the paper's, and the permutation test finds no difference
(P = 0.469). With single trials as pairs (reading (b)), r is 0.794 and 0.767, outside tolerance, and
the difference is significant (P = 0.025). Reading (a) is adopted, as its r values are of the
paper's size; all units give the same pattern (P = 0.267 and 0.001).
===== 70 markdown
**Result: partially reproduced.** Mean INDX1 is -12.0% for Position Only cells (paper -13 +/-
1.3, within) and -24.2% for Position/Vision cells (paper -31 +/- 3.1, not within), and the most
negative of the four populations is all cells (-24.9%), not Position/Vision. Position Only is the
least negative, as in the paper. Outlier readings (b) and (c) and all units give the same pattern.
===== 103 code
E = pd.concat([t.assign(session=k) for k, t in kept.items() if "f22" in t and t.f22.notna().all()])
print("sessions with the two fields:", E.session.nunique(), "; trials:", len(E))
print("field 22 range", E.f22.min(), "to", E.f22.max(), "; field 23 range", E.f23.min(), "to", E.f23.max())
print("within-session SD (median over sessions): field 22", round(E.groupby("session").f22.std().median(), 3),
      "; field 23", round(E.groupby("session").f23.std().median(), 3))
rows = []
for tg in ppc.TARGETS:
[... 64 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 95,180p attempts/shi-2013-01.yaml; sed -n 335,465p attempts/shi-2013-01.yaml
```

```
- Monkey X only.
- claim: movement-epoch-tuning
  outcome: not_reproduced
  assumed: true
  notebook: reproduce_shi_2013.ipynb
  output: claim:movement-epoch-tuning
  measured: 179
  notes: With movement onset at event code 8, 187 of 359 units (52.1%, 179 scaled to 343) have a target
    main effect or interaction in the 500 ms centred on it, against 139 +/- 13.9 (41%). All 483 units
    give 49.9% (171 scaled). A window centred on the target-code event (the cursor entering the target
    window) gives 65.5%, and one on code 3 (target onset) 6.1%. Question for the paper's authors,
    how movement onset was defined (methods_unavailable finding).
  deviations:
  - Movement onset is taken as event code 8 (reading (a) of the criterion, an event code). The data
    set does not document the codes; code 8 comes 0.22 to 0.58 s after code 3 (read as target onset)
    and 0.03 to 0.38 s before the target code event, which fits the cursor leaving the start window,
    the definition of reading (b). No continuous arm position is in the data set to run reading (b)
    directly. This reading of the code is an assumption.
  - Monkey X only, 359 units; counts compared as percentages, scaled to 343.
- claim: hold-position-main-effect
[... 197 more lines not kept]
```

**Agent**

Now the text fixes. Cell 10 first:

**Agent calls Bash**

```bash
python - <<'EOF'
import json
p='entries/shi-2013/reproduce_shi_2013.ipynb'
nb=json.load(open(p))
def rep(i,old,new):
    s=''.join(nb['cells'][i]['source'])
    assert old in s,(i,old)
    s=s.replace(old,new)
    nb['cells'][i]['source']=s.splitlines(keepends=True)
rep(10,"""Code 3 comes 0.54 to 0.96 s after the trial starts (the start position is shown, then
held for 500 ms): it fits target onset, the go signal. Code 8 follows 0.22 to 0.58 s later (a
reaction time), and the target code 0.03 to 0.38 s after 8 (median 0.13 s): 8 fits the cursor
leaving the start window and the target code the cursor entering the target window. Code 10
follows the target code by 320 ms on every trial, the 300 ms after which the target is
extinguished (on a 32 ms strobe clock).""","""Ranges below are the 5th to 95th percentiles of the
table above, with the minimum and maximum in brackets. Code 3 comes 0.54 to 0.96 s (0.54 to 1.92
s) after the trial starts (the start position is shown, then held for 500 ms): it fits target
onset, the go signal. Code 8 follows 0.22 to 0.58 s (0.08 to 1.12 s) later (a reaction time), and
the target code 0.03 to 0.38 s (0.02 to 1.25 s) after 8 (median 0.13 s): 8 fits the cursor leaving
the start window and the target code the cursor entering the target window. Code 10 follows the
target code by a median of 320 ms (5th to 95th percentile 0.30 to 0.32 s, range 0.22 to 0.42 s),
the 300 ms after which the target is extinguished (on a 32 ms strobe clock).""")
rep(59,"""The position percentages are close; the
vision and interaction ones are higher than the paper's.""","""The last 400 ms position percentage is within
tolerance and the first 400 ms one (35.7%) is above it; the vision and interaction percentages are
higher than the paper's.""")
rep(68,"Readings (b) and (c) give the same.","""Reading (c) gives the same values; reading (b)
gives 78.4, 70.0, 75.0 and 75.0%, again only the first within tolerance.""")
rep(76,"""the closest, outliers on
INDX2 by reading (c), gives -1.7, -10.5 and -9.5%.""","""the closest are outliers on
INDX2 by reading (c), which gives -1.7, -10.5 and -9.5% for the 359 units, and -2.0, -14.1 and
-9.9% for all 483 units, where only Vision Only (-14.1%) is within tolerance.""")
rep(93,"""With all 483
units only the test over bootstraps finds it (paired over targets P = 0.29, unpaired P = 0.40).""","""With all 483
units and resampling n cells, only the test over bootstraps finds it (paired over targets P = 0.29,
unpaired P = 0.40); with populations of 200 cells the paired test over targets also finds it (P =
0.036, unpaired P = 0.14). The test over bootstraps treats the 200 resamples as independent
samples, so its P value shrinks as more resamples are drawn; the tests over targets do not have
this problem.""")
rep(112,"""and each session's shortest interval
follows its field 11 (800 to 1,100 ms against 0.83 to 1.15 s), so field 11 is read as the minimum
hold.""","""so field 11 is read as the minimum hold.
Grouped by the field 11 of its first completed trial, a session's shortest interval is below that
value in sessions grouped at 900 (0.832 s) and 1,000 ms (0.960 s); these are sessions whose field
11 changes within the session, and their shortest interval falls on a trial with a lower field 11
(data check above).""")
json.dump(nb,open(p,'w'),indent=1,ensure_ascii=False); open(p,'a').write('\n')
EOF
git diff --stat entries/shi-2013/reproduce_shi_2013.ipynb
```

```
entries/shi-2013/reproduce_shi_2013.ipynb | 43 +++++++++++++++++++------------
 1 file changed, 27 insertions(+), 16 deletions(-)
```

**Agent**

Now make cell 111 print the evidence the corrected sentence relies on:

**Agent calls Bash**

```bash
python - <<'EOF'
import json
p='entries/shi-2013/reproduce_shi_2013.ipynb'
nb=json.load(open(p))
i=111
s=''.join(nb['cells'][i]['source'])
old='''    rows.append(dict(session=k, field11=f11.iloc[0], field11_values=len(set(f11)), n=len(c), min_10_to_12=(c.t12 - c.t10).min()))'''
new='''    d = c.t12 - c.t10
    rows.append(dict(session=k, field11=f11.iloc[0], field11_values=len(set(f11)), n=len(c), min_10_to_12=d.min(),
                     field11_at_min=f11.loc[d.idxmin()], field11_set=sorted(set(f11))))'''
assert old in s; s=s.replace(old,new)
old2='''print("sessions whose field 11 changes within the session:", int((HP.field11_values > 1).sum()))'''
new2=old2+'''
below = HP[HP.min_10_to_12 < HP.field11 / 1000]
print("sessions whose shortest interval is below the field 11 of their first completed trial:")
print(below[["session", "field11", "field11_set", "min_10_to_12", "field11_at_min"]].to_string(index=False))'''
assert old2 in s; s=s.replace(old2,new2)
nb['cells'][i]['source']=s.splitlines(keepends=True)
json.dump(nb,open(p,'w'),indent=1,ensure_ascii=False); open(p,'a').write('\n')
EOF
git diff entries/shi-2013/reproduce_shi_2013.ipynb | tail -5
```

```
"nbformat": 4,
  "nbformat_minor": 5
-}
\ No newline at end of file
+}
```

**Agent calls Bash**

```bash
python - <<'EOF'
p='entries/shi-2013/reproduce_shi_2013.ipynb'
s=open(p).read().rstrip('\n'); open(p,'w').write(s)
EOF
git diff entries/shi-2013/reproduce_shi_2013.ipynb | tail -3; date -u
```

```
"sessions with the extended hold."
    ]
   },
Mon Nov  9 21:43:58 UTC 2026
```

**Agent calls Bash**

```bash
python - <<'EOF'
import json
nb=json.load(open('executed/shi-2013/reproduce_shi_2013.ipynb'))
for o in nb['cells'][103]['outputs']: print(''.join(o.get('text','')))
print(''.join(nb['cells'][104]['source'])[:300])
EOF
grep -n "eye-position" -A25 claims/shi-2013.yaml | grep -n "criterion" -A8
```

```
sessions with the two fields: 224 ; trials: 17920
field 22 range -1.58 to 1.43 ; field 23 range -3.19 to 0.73
within-session SD (median over sessions): field 22 0.053 ; field 23 0.073
(a) per target, trials pooled over sessions:
 target  n_V  n_NV           mean_V          mean_NV  p_manova  p_levene_h  p_levene_v  p_levene_h_median  p_levene_v_median
      0 1120  1120  [0.076, -1.766]   [0.07, -1.762]  0.907371    0.710010    0.844366           0.825764           0.599448
     45 1120  1120    [0.1, -1.778]   [0.09, -1.763]  0.383185    0.742611    0.827356           0.738219           0.709786
     90 1120  1120   [0.032, -1.66]  [0.013, -1.663]  0.504437    0.800415    0.011956           0.856390           0.282153
    135 1120  1120 [-0.012, -1.766] [-0.035, -1.753]  0.219999    0.128504    0.659528           0.255449           0.469519
    180 1120  1120 [-0.003, -1.814] [-0.023, -1.813]  0.460659    0.369630    0.609239           0.657098           0.535611
    225 1120  1120 [-0.007, -1.834] [-0.022, -1.829]  0.626561    0.129553    0.963056           0.293188           0.920017
    270 1120  1120  [0.056, -1.868]  [0.045, -1.854]  0.368546    0.694729    0.814492           0.750011           0.770764
    315 1120  1120  [0.065, -1.795]   [0.05, -1.785]  0.554510    0.611468    0.715120           0.588751           0.557759
targets with any P < 0.05: 1

(b) per session and target, % significant: MANOVA 8.7 ; Levene horizontal 8.7 ; vertical 9.3 ; undefined 0

# The analog files of three sessions (ppc.read_anaad; layout read from the files, not documented).
for st, A in D["ana"].items():
    k = st + ".mat"
[... 15 more lines not kept]
```

**Agent calls Bash**

```bash
python - <<'EOF'
import json
p='entries/shi-2013/reproduce_shi_2013.ipynb'
nb=json.load(open(p))
i=106
s=''.join(nb['cells'][i]['source'])
old="record fields 22 and 23 are\nunnamed."
assert old in s
s=s.replace(old, old+""" The block also rests on a reading of the analog file layout that is
at least partly wrong (channel 6). If fields 22 and 23 were the mean eye position, reading (a)
would not reproduce the claim: Levene's test centred on the mean finds a V against NV difference at
90 degrees, vertical (P = 0.012, data check above).""")
nb['cells'][i]['source']=s.splitlines(keepends=True)
open(p,'w').write(json.dumps(nb,indent=1,ensure_ascii=False))
EOF
git diff --stat
```

```
entries/shi-2013/reproduce_shi_2013.ipynb |  53 +++++--
 tools/build_site.py                       | 248 +++++++++++++++++++++++++++++-
 tools/entry.py                            | 112 +++++++++++++-
 tools/notify.py                           |   5 +-
 tools/runner/chain.sh                     |   5 +-
 tools/site_assets/app.css                 |  31 ++++
 tools/site_assets/list.js                 |  33 +++-
 7 files changed, 450 insertions(+), 37 deletions(-)
```

**Agent**

Now the attempt record.

**Agent calls Bash**

```bash
sed -n 240,300p attempts/shi-2013-01.yaml; sed -n 460,470p attempts/shi-2013-01.yaml
```

```
- Monkey X only, one unit per session; the population of all units, a variant, reproduces it.
  - One unit per session, as the paper has one neuron per session (Table 1 legend, means over 219
    sessions for monkey X; Results, Behavior, N = 343 sessions for 343 neurons). Which unit of a session
    the paper used is not stated; the first sorted unit (a) is assumed, a standard choice. With all
    483 sorted units (a variant) the outcome would differ, so it rests on this assumption. Question
    for the paper's authors (methods_unavailable finding).
- claim: fig4-indx1-means
  outcome: partially_reproduced
  notebook: reproduce_shi_2013.ipynb
  output: claim:fig4-indx1-means
  measured:
  - -12.0
  - -24.2
  notes: Mean INDX1 is -12.0% for Position Only cells, within -13 +/- 1.3, and -24.2% for Position/Vision
    cells, outside -31 +/- 3.1. Position Only is the least negative of the four populations, as in
    the paper, but the most negative is all cells (-24.9%), not Position/Vision. Readings (b) and
    (c), all units (-13.7 and -26.2%) and the other code mapping (-14.2 and -27.1%) give the same
    pattern.
  deviations:
  - As for fig4-indx1-negative.
[... 52 more lines not kept]
```

**Agent calls Bash**

```bash
python - <<'EOF'
p='attempts/shi-2013-01.yaml'
s=open(p).read()
def rep(old,new):
    global s
    assert s.count(old)==1,old
    s=s.replace(old,new)
rep("""    set does not document the codes; code 8 comes 0.22 to 0.58 s after code 3 (read as target onset)
    and 0.03 to 0.38 s before the target code event,""","""    set does not document the codes; code 8 comes 0.22 to 0.58 s after code 3 (read as target onset)
    and 0.03 to 0.38 s before the target code event (5th to 95th percentiles; the full ranges are
    0.08 to 1.12 s and 0.02 to 1.25 s),""")
rep("""The position percentages
    are near the paper's; the vision and interaction percentages are higher.""","""The last 400 ms position
    percentage is within tolerance and the first 400 ms one is above it; the vision and interaction
    percentages are higher.""")
rep("""- claim: fig6-decoding-vv
  outcome: not_reproduced
  assumed: true
""","""- claim: fig6-decoding-vv
  outcome: not_reproduced
""")
rep("""  - Which code is V is assumed; under the other mapping V/V accuracy is 63.7%, also not within.""",
"""  - Which code is V is assumed; under the other mapping V/V accuracy is 63.7%, also not within, and
    all units give 68.4%, so the outcome does not rest on the mapping or the choice of unit.""")
rep("""With all
    483 units, 68.4 against 63.0%, paired P = 0.29 and over bootstraps P = 4e-15. With all units the
    unpaired test over targets gives P = 0.40.""","""With all
    483 units, 68.4 against 63.0%, paired P = 0.29 and over bootstraps P = 4e-15. With all units the
    unpaired test over targets gives P = 0.40. With all units and populations of 200 cells, 62.9 against
    55.3%, the paired test over targets also finds the difference (P = 0.036; unpaired P = 0.14). The
    test over bootstraps (reading (b)) treats the 200 resamples as independent, so its P value depends
    on how many are drawn; the tests over targets do not.""")
rep("""the
    closest, outliers on INDX2 with reading (c), gives -1.7, -10.5 and -9.5%.""","""the
    closest are outliers on INDX2 with reading (c), which gives -1.7, -10.5 and -9.5% for the 359 units
    and -2.0, -14.1 and -9.9% for all 483 units, where only Vision Only is within tolerance.""")
rep("""    mean, 0.28 on the median); 8.7% of session and target pairs differ by MANOVA.""","""    mean, 0.28 on the median); 8.7% of session and target pairs differ by MANOVA. If these fields
    were the mean eye position, reading (a) would therefore not reproduce the claim. The block also
    rests on a reading of the analog file layout known to be at least partly wrong.""")
open(p,'w').write(s)
EOF
```

```
(Bash completed with no output)
```

**Agent calls Bash**

```bash
grep -n -i "bootstraps\|near the paper\|close\|320\|field 11" entries/shi-2013/README.md; python - <<'EOF'
import json
nb=json.load(open('entries/shi-2013/reproduce_shi_2013.ipynb'))
for i,c in enumerate(nb['cells']):
    s=''.join(c['source'])
    if c['cell_type']=='markdown' and any(k in s for k in ['only the test over','are close','320 ms','fields 22 and 23 were']):
        print(i, s[:200])
EOF
```

```
10 Reading of the codes, from the timing and the paper's paradigm (Methods, Experimental
paradigm). Ranges below are the 5th to 95th percentiles of the
table above, with the minimum and maximum in bracke
93 **Result: reproduced (resting on an assumption).** V accuracy exceeds NV accuracy (77.4 against
63.7%) and every t-test reading finds it (paired over targets P = 0.0087, over bootstraps P <
1e-60, unp
98 **Result: not reproduced (resting on an assumption).** The 400 ms windows decode less well than
the 800 ms window (V 61.2 and 66.0 against 78.3%; NV 59.8 and 42.8 against 64.6%), as the paper
says. In
106 **Result: blocked (metadata_insufficient).** The data set holds no documented eye position. No
analog channel of the three sessions summarised differs between targets in the hold or follows the
hand,
```

**Agent calls Bash**

```bash
python - <<'EOF'
import json
nb=json.load(open('executed/shi-2013/reproduce_shi_2013.ipynb'))
for i in [95,96,97]:
    c=nb['cells'][i]
    if c['cell_type']=='code':
        print('==',i,''.join(c['source'])[:400])
        for o in c['outputs']: print(''.join(o.get('text','')))
EOF
```

```
== 96 for lab, M in (("main", M1), ("all units", MA)):
    res = {}
    for w in ("hold_count", "first400_count", "last400_count"):
        res[w] = boot(counts_of(M, w), schemes=((0, 0), (1, 1)), seed=5)
    for ci, cn in ((0, "V"), (1, "NV")):
        s = (ci, ci)
        h, f_, l_ = (res[w][s] for w in ("hold_count", "first400_count", "last400_count"))
        print(f"{lab}, {cn}: 800 ms {h.mean():.1
main, V: 800 ms 78.3, first 400 61.2, last 400 66.0; first vs last: (a) paired t over targets P 0.382, (b) two-sample t over bootstraps P 6.62e-11, (c) two-sample t over targets P 0.313; difference -4.8 points
main, NV: 800 ms 64.6, first 400 59.8, last 400 42.8; first vs last: (a) paired t over targets P 0.00733, (b) two-sample t over bootstraps P 3.54e-78, (c) two-sample t over targets P 0.0168; difference 17.0 points

all units, V: 800 ms 68.3, first 400 54.1, last 400 57.2; first vs last: (a) paired t over targets P 0.6, (b) two-sample t over bootstraps P 1.49e-05, (c) two-sample t over targets P 0.554; difference -3.1 points
all units, NV: 800 ms 62.2, first 400 56.3, last 400 41.7; first vs last: (a) paired t over targets P 0.0721, (b) two-sample t over bootstraps P 7.35e-74, (c) two-sample t over targets P 0.074; difference 14.6 points

== 97 # Variant: the same with the windows starting no earlier than 250 ms after code 10. The decoder is
# given counts scaled to 400 ms (rate x 0.4 s) so that the two parts are compared on one scale.
for lab in ("main", "all units"):
    res = {key: boot(np.stack(LATE[lab][key]) * 0.4, schemes=((0, 0), (1, 1)), seed=5) for key in ("first", "last")}
    for ci, cn in ((0, "V"), (1, "NV")):
        s = (
[... 5 more lines not kept]
```

**Agent calls Bash**

```bash
head -c 2500 transcripts/shi-2013/verifier-2.md; sed -n 627,640p docs/protocol.md
```

````
# shi-2013 · verifier-2 · run 42700257966

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  ls -la; ls paper docs 2>/dev/null; cat round-1-report.md
```

```
total 376
drwxr-xr-x 6 runner runner    4096 Nov  9 21:24 .
drwxr-xr-x 7 runner runner    4096 Nov  9 21:24 ..
crw-rw-rw- 1 nobody nogroup   1, 3 Nov  9 21:12 .bash_profile
crw-rw-rw- 1 nobody nogroup   1, 3 Nov  9 21:12 .bashrc
drwxr-xr-x 5 runner runner    4096 Nov  9 21:24 .claude
-rw-r--r-- 1 runner runner       0 Nov  9 21:24 .env
-rw-r--r-- 1 runner runner       0 Nov  9 21:24 .env.development
-rw-r--r-- 1 runner runner       0 Nov  9 21:24 .env.development.local
[... 44 more lines not kept]
````

**Agent calls Bash**

```bash
sed -n 1,40p entries/shi-2013/README.md
```

```
# Shi, Apker & Buneo (2013) from CRCNS ppc-1

Tests the findings of [Shi et al. (2013)](https://doi.org/10.1152/jn.00223.2012) on
[CRCNS ppc-1](https://doi.org/10.6080/K0CZ353K), which holds the sorted spikes and trial events of
area 5 recordings while monkeys held the arm at eight targets with or without vision of the arm
cursor. The notebook streams the data set's single `data.tar.gz` from the public CRCNS bucket.

| Claim | Outcome |
|---|---|
| Neurons with a position, vision or interaction effect in the hold (39%, 13%, 9%) | Reproduced (vision count rests on an assumption) |
| V and NV responses correlate alike whether endpoints differed or not | Reproduced (assumption) |
| CV2 larger in NV; decoding better in V; cross-condition decoding lower | Reproduced (two rest on an assumption) |
| Table 1 endpoint means; overall effect percentages; INDX1 mostly negative and its group means; rate variance higher in NV | Partially reproduced |
| Behavioural MANOVA and Levene percentages; Table 1 SDs; example neuron; movement epoch tuning; 400 ms subepochs; tuning shift; INDX2; Fano factor; decoding accuracies and subepochs; cells without effects | Not reproduced |
| Eye position; aborted trials; longer hold | Blocked |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The data set holds monkey X's sessions only (every session has monkey X's target layout), and
[... 6 more lines not kept]
```

**Agent calls Bash**

```bash
python - <<'EOF'
import json
nb=json.load(open('entries/shi-2013/reproduce_shi_2013.ipynb'))
for i,c in enumerate(nb['cells']):
    s=''.join(c['source'])
    if 'Summary' in s[:200] or 'decoding-vv' in s or ('fig6' in s and c['cell_type']=='markdown'):
        print(i, c['metadata'].get('tags'), s[:1500])
for i in [86,87]:
    print(i,''.join(nb['cells'][i]['source'])[:800])
EOF
```

```
0 None # Reproducing Shi, Apker and Buneo (2013) on CRCNS ppc-1

**Paper.** Shi Y, Apker G, Buneo CA (2013). Multimodal representation of limb endpoint position in
the posterior parietal cortex. *J Neurophysiol* 109: 2097-2107.
[doi:10.1152/jn.00223.2012](https://doi.org/10.1152/jn.00223.2012)

**Dataset.** CRCNS ppc-1, Buneo, Shi, Apker and VanGilder (2016),
[doi:10.6080/K0CZ353K](https://doi.org/10.6080/K0CZ353K), identified here as
`crcns:ppc-1/unversioned`. It is read from the public bucket
(`https://crcnsarchive.s3-us-west-2.amazonaws.com/ppc-1/live/data.tar.gz`, streamed, not
downloaded).

**Version.** CRCNS data sets are not versioned, and ppc-1 has one published copy, under `live/`
(no `old/` copy exists in the bucket), so that copy is the one pinned. The paper cites no version.
To detect a later change: `data.tar.gz` has MD5 `bbb341b8947a6314b2618f0caa0b64f8` in the data
set's `checksums.md5` (printed below as read), size 4,394,813,551 bytes; data descriptor version 0.8
(Dec 7, 2016).

**Claims.** `claims/shi-2013.yaml`, written from the version of record (Methods, Results,
Discussion, Table 1, legends of Figures 1 to 6; the paper has no supplement and links no code), and
[... 72 more lines not kept]
```

**Agent**

Find the fig6-decoding-vv result cell, to drop "resting on an assumption" if it says so:

**Agent calls Bash**

```bash
python - <<'EOF'
import json
nb=json.load(open('entries/shi-2013/reproduce_shi_2013.ipynb'))
for i in range(88,96):
    c=nb['cells'][i]
    if c['cell_type']=='markdown': print(i,''.join(c['source']))
EOF
```

```
91 **Result: not reproduced.** Trained and tested on V, the decoder's accuracy over 200 bootstrap
resamples of the 359 cells is 77.4 +/- 6.5% (reading (a)) and 73.3% with populations of 200 cells
(reading (b)), below 91.6 +/- 9%. The full population without resampling gives 87.5%. With
shuffled target labels the decoder gives 16.1% (V) and 11.2% (NV) on average over 20 shuffles,
near the nominal chance of 12.5%, so the accuracies are far above chance.
92 **Result: not reproduced.** Trained and tested on NV, accuracy is 63.7 +/- 7.0% (reading (a)) and
57.2% (reading (b)), just below the 63.9% lower bound of 81.9 +/- 18.0%. The full population gives
77.5%.
93 **Result: reproduced (resting on an assumption).** V accuracy exceeds NV accuracy (77.4 against
63.7%) and every t-test reading finds it (paired over targets P = 0.0087, over bootstraps P <
1e-60, unpaired over targets P = 0.0081), as do populations of 200 cells. Which condition is V
rests on the code mapping: under the other one NV decodes better (77.4 against 63.7%). With all 483
units and resampling n cells, only the test over bootstraps finds it (paired over targets P = 0.29,
unpaired P = 0.40); with populations of 200 cells the paired test over targets also finds it (P =
0.036, unpaired P = 0.14). The test over bootstraps treats the 200 resamples as independent
samples, so its P value shrinks as more resamples are drawn; the tests over targets do not have
this problem.
94 **Result: reproduced.** Trained on NV and tested on V, accuracy is 58.9% (paper 60.7 +/- 22);
trained on V and tested on NV, 52.7% (69.1 +/- 17); both are within tolerance and below the V/V
accuracy (77.4%). Training on all five trials (reading (b)) gives 62.1 and 56.8%. Swapping the code
[... 4 more lines not kept]
```

**Agent calls Bash**

```bash
python - <<'EOF'
import json
p='entries/shi-2013/reproduce_shi_2013.ipynb'
nb=json.load(open(p))
s=''.join(nb['cells'][91]['source'])
old="so the accuracies are far above chance."
assert old in s
s=s.replace(old, old+""" The other code mapping (63.7%) and all 483 units (68.4%)
are also below tolerance, so the outcome rests on neither choice.""")
nb['cells'][91]['source']=s.splitlines(keepends=True)
open(p,'w').write(json.dumps(nb,indent=1,ensure_ascii=False))
EOF
```

```
(Bash completed with no output)
```

**Agent**

Now the round-2 verification block. Claims and outcomes in order:

**Agent calls Bash**

```bash
python - <<'EOF'
import yaml
d=yaml.safe_load(open('attempts/shi-2013-01.yaml'))
for o in d['outcomes']: print(o['claim'],o['outcome'],o.get('blocked_by',''),o.get('assumed',''))
print(d['verifications'][0].keys())
EOF
```

```
behavior-mean-position-sessions not_reproduced  
behavior-variability-sessions not_reproduced  
table1-endpoint-means partially_reproduced  
table1-endpoint-sd not_reproduced  
fig3-example-neuron not_reproduced  
movement-epoch-tuning not_reproduced  True
hold-position-main-effect reproduced  
hold-vision-main-effect reproduced  True
hold-interaction reproduced  
hold-subepochs not_reproduced  True
hold-overall-effects partially_reproduced  
correlation-endpoint-datasets reproduced  True
fig4-indx1-negative partially_reproduced  True
fig4-indx1-means partially_reproduced  
indx1-tuning-shift not_reproduced  
indx2-means not_reproduced  
rate-variance-nv-higher partially_reproduced  True
fig5-fano-factor not_reproduced  True
cv2-larger-nv reproduced  True
fig6-decoding-vv not_reproduced  
[... 9 more lines not kept]
```

**Agent calls Bash**

```bash
cat > $TMPDIR/v2.py <<'EOF'
import yaml
A="I agree with all 28 outcomes in the record."
R=[
("behavior-mean-position-sessions","not_reproduced",A+" Remaining (B2): whether fields 19 to 21 are the mean over the hold or a single sample remains undecidable; the behavioural and Table 1 outcomes rest on them. This is stated. The MANOVA is calibrated on these data (5.7% significant with shuffled labels), the two conditions are interleaved within sessions, and within-session SDs are printed.",
 "No change; the question stays stated in the deviation and asked of the paper's authors."),
("behavior-variability-sessions","not_reproduced",A+" Fields 19 to 21 (B2) remain undecidable, as for behavior-mean-position-sessions.","No change."),
("table1-endpoint-means","partially_reproduced",A+" Fields 19 to 21 (B2) remain undecidable, as for behavior-mean-position-sessions.","No change."),
("table1-endpoint-sd","not_reproduced",A+" Fields 19 to 21 (B2) remain undecidable, as for behavior-mean-position-sessions.","No change."),
("fig3-example-neuron","not_reproduced",A,"No change."),
("movement-epoch-tuning","not_reproduced",A+" Movement onset read as code 8 is stated and reasonable. Cell 10 gives 0.22 to 0.58 s (code 8) and 0.54 to 0.96 s (code 3) as ranges, but they are the 5th to 95th percentiles, not the minimum to maximum (0.08 to 1.12 s and 0.54 to 1.92 s); the record's deviation repeats the 0.22 to 0.58 and 0.03 to 0.38 s ranges without saying they are percentiles.",
 "Cell 10 and the deviation now say the ranges are 5th to 95th percentiles and give the full ranges as well. Outcome unchanged."),
("hold-position-main-effect","reproduced",A+" B3 (window placement) is resolved by the per-trial table of the interval against field 11. Remaining (clock alignment) is checked per session, but in 206 of 359 sessions no unit is tuned in the hold, so the shared spike and event clock is not confirmed there; a misaligned session would dilute the counts and the decoding.",
 "No change; the clock check and its limit are shown in the notebook. Cell 10 now says code 10 follows the target code by a median of 320 ms (range 0.22 to 0.42 s), not by 320 ms on every trial."),
("hold-vision-main-effect","reproduced",A+" The first sorted unit per session is stated and reasonable. Remaining (B1): the record has 359 monkey X sessions against the paper's 219; the new checks rule out monkey B and repeated recordings of one neuron but do not say which sessions the paper used. Every count, index and decoding claim rests on this. It is stated as a finding and cannot be settled from the data.",
 "No change; kept as the selection_undocumented finding."),
("hold-interaction","reproduced",A,"No change."),
("hold-subepochs","not_reproduced",A+" The first sorted unit per session is stated and reasonable, and the late-start variant leaves the outcome unchanged (B3 resolved). Cell 59 says the position percentages are close, but the first-400 ms one, 35.7%, is outside 31 +/- 3.1; the record's near the paper's has the same problem.",
 "Cell 59 and the notes now say the last 400 ms position percentage is within tolerance and the first 400 ms one is above it. Outcome unchanged."),
("hold-overall-effects","partially_reproduced",A,"No change."),
("correlation-endpoint-datasets","reproduced",A+" Correlation reading (a) is stated and reasonable. Data set 1 rests on fields 19 to 21 (B2), which remain undecidable.","No change."),
("fig4-indx1-negative","partially_reproduced",A+" The first sorted unit per session is stated and reasonable. Cell 68 says readings (b) and (c) give the same, but reading (b) gives 78.4% and 70.0% for all cells and Position Only, not reading (a)'s 77.8% and 68.4%. The outcome is the same, and the record's notes state these values correctly.",
 "Cell 68 now gives reading (b)'s values (78.4, 70.0, 75.0, 75.0%, only the first within tolerance). Outcome unchanged."),
("fig4-indx1-means","partially_reproduced","I now agree. The Position Only part holds in full (-12.0%, within -13 +/- 1.3, the least negative group). The Position/Vision part fails (-24.2% outside -31 +/- 3.1, and not the most negative group). Calling that partial is defensible.",
 "No change."),
("indx1-tuning-shift","not_reproduced",A,"No change."),
("indx2-means","not_reproduced",A+" Cell 76 calls outliers on INDX2 by reading (c) the closest (-1.7, -10.5, -9.5%), but all units with the same reading give -2.0, -14.1 and -9.9, and -14.1 is within -13 +/- 1.3, so it is arguably closer. The outcome is unaffected.",
 "Cell 76 and the notes now give both, and say that with all units only Vision Only is within tolerance. Outcome unchanged."),
("rate-variance-nv-higher","partially_reproduced","I now agree, but only just. Both means are outside tolerance (46.4 against a bound of 50.4, 23.1 against 27), but NV is higher in 67% of cells, at about twice the V value. That direction rests on the code mapping (V = 4, B4), which is unchanged, reasonable and flagged.",
 "No change."),
("fig5-fano-factor","not_reproduced",A+" FF outlier reading (a) and V = 4 are stated and reasonable. The possible misreading in the claims file (B6) is now asked of a reader; it does not change the outcome, as no reading reproduces the claim, including the 0 to 80 range variant.",
 "No change; the question stays in questions/shi-2013.yaml."),
("cv2-larger-nv","reproduced",A+" CV2 reading (a) and V = 4 are stated and reasonable; the direction depends on the mapping (B4).","No change."),
("fig6-decoding-vv","not_reproduced",A+" The assumed flag is not needed: the claim is not reproduced under both code mappings (63.7%) and with all units (68.4%), so its outcome rests on no assumption. The decoder's chance level on these data (B7) and the unused branch of ppc.decode (B9) are resolved.",
 "Removed assumed from this outcome; the deviation and cell 91 now say the outcome rests on neither the mapping nor the choice of unit."),
("fig6-decoding-nvnv","not_reproduced",A+" V = 4 is stated and reasonable; the outcome depends on it (B4).","No change."),
("decoding-v-better-than-nv","reproduced",A+" V = 4 is stated and reasonable; the direction depends on it (B4). Cell 93 says that with all 483 units only the test over bootstraps finds it, but cell 90 shows that with all units and populations of 200 cells the paired test over targets also finds it (P = 0.0364). The outcome is unaffected. B8 (the t-test over bootstrap accuracies is pseudo-replicated) was not addressed; it decides no outcome.",
 "Cell 93 and the notes now give the all-units populations of 200 cells (paired P = 0.036, unpaired P = 0.14). On B8, the test over bootstraps is reading (b) of the claims file's criterion and is kept as a reading; cell 93 and the notes now say it treats the resamples as independent, so its P value depends on how many are drawn, while the tests over targets do not. Outcome unchanged."),
("fig6-decoding-cross","reproduced",A,"No change."),
("decoding-subepochs","not_reproduced",A+" The first sorted unit per session is stated and reasonable, and the late-start variant leaves the outcome unchanged (B3 resolved).","No change."),
("decoding-nonsignificant-cells","not_reproduced",A,"No change."),
("eye-position-no-difference","blocked",A+" It is confirmed as metadata_insufficient; the analog channels are now shown and the note on fields 22 and 23 is corrected. Remaining: the block depends on the layout read for the analog files, seven channels out of 16 described, with channel 6 spanning 16 bits, so it rests partly on a layout reading known to be at least partly wrong. If fields 22 and 23 were eye position, reading (a) would fail the claim (Levene's test P = 0.012 at 90 degrees, vertical).",
 "Block kept. Cell 106 and the notes now say that the block rests on a layout reading known to be partly wrong, and that if fields 22 and 23 were the mean eye position reading (a) would not reproduce the claim."),
("aborted-trials-nv","blocked",A,"No change."),
("longer-hold-no-difference","blocked","I now agree. The per-trial table removes my round-1 objection and supports reading field 11 as the minimum hold; no completed trial has field 11 >= 1,200. Cell 112 says each session's shortest interval follows its field 11, which cell 111 contradicts (sessions grouped at 900 have a shortest interval of 0.832 s, at 1,000 of 0.960 s); most likely the three sessions whose field 11 changes within the session explain it, but the sentence does not say so.",
 "Cell 112 now drops the per-session sentence and says the sessions whose shortest interval is below their first field 11 are those whose field 11 changes within the session; cell 111 now lists those sessions with their field 11 values and the field 11 of the trial with the shortest interval. Block unchanged."),
]
res=[]
for c,o,r,resp in R:
    d=dict(claim=c,agrees=True,outcome=o,reason=r,response=resp)
    res.append(d)
v=dict(date='2026-11-09',kind='agent',by='Independent agent run by CatalystNeuro (same harness, separate context, did not write the notebook)',
 reviewed="Round 2. The full re-executed notebook with the conclusions and the summary, the helper module (ppc.py), the claims file, the README and the attempt record, with the paper's full text under paper/. The verifier checked the outcomes and the flagged assumptions, every conclusion sentence against the outputs, and which of its round-1 points are resolved.",
 results=res)
txt=yaml.dump([v],sort_keys=False,width=100,allow_unicode=True,default_flow_style=False)
txt='\n'.join(l for l in txt.splitlines())+'\n'
p='attempts/shi-2013-01.yaml'
s=open(p).read()
if not s.endswith('\n'): s+='\n'
open(p,'w').write(s+txt)
EOF
python $TMPDIR/v2.py && tail -30 attempts/shi-2013-01.yaml
```

Result: not kept, because it reads the paper's text.

**Agent**

Re-running the entry with the edits:

**Agent calls Bash**

```bash
date -u; python tools/entry.py all entries/shi-2013 2>&1 | tail -6
```

```
Mon Nov  9 21:45:19 UTC 2026
Installed kernelspec registry-shi-2013 in executed/shi-2013/.venv/share/jupyter/kernels/registry-shi-2013
0 error(s)
pass  reproduce_shi_2013.ipynb  (330 s)
```

**Agent calls Bash**

```bash
python - <<'EOF'
import json
nb=json.load(open('executed/shi-2013/reproduce_shi_2013.ipynb'))
for o in nb['cells'][111]['outputs']: print(''.join(o.get('text','')))
EOF
```

```
completed trials' record field 11 against the shortest code 10 to code 12 interval of each session (s):

         sessions  shortest_min  shortest_median  shortest_max
field11                                                       
800.0           4         0.832            0.832         0.832
900.0         352         0.832            0.960         1.216
1000.0         46         0.960            1.056         1.056
1100.0          4         1.152            1.152         1.152
sessions whose field 11 changes within the session: 3
sessions whose shortest interval is below the field 11 of their first completed trial:
                 session  field11     field11_set  min_10_to_12  field11_at_min
data/012109/012109_5.mat    900.0  [800.0, 900.0]      0.832000           800.0
data/032509/032509_3.mat   1000.0 [900.0, 1000.0]      0.960025           900.0
data/033009/033009_6.mat   1000.0 [900.0, 1000.0]      0.960000           900.0
trials with field 11 >= 1200, any outcome: 4 ; completed: 0
```

**Agent**

Confirmed: the three sessions are exactly those whose field 11 changes. Final checks on wording:

**Agent calls Bash**

```bash
git diff attempts/ entries/ | grep "^+" | grep -n -i "—\|rather" ; python tools/entry.py check entries/shi-2013 2>&1 | tail -2; git status --short
```

```
0 error(s)
 M attempts/shi-2013-01.yaml
 M entries/shi-2013/reproduce_shi_2013.ipynb
 M tools/build_site.py
 M tools/entry.py
 M tools/notify.py
 M tools/runner/chain.sh
 M tools/site_assets/app.css
 M tools/site_assets/list.js
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
[... 2 more lines not kept]
```

**Agent calls Bash**

```bash
ls -la .bashrc .idea scripts .mcp.json 2>&1 | head
```

```
crw-rw-rw- 1 nobody nogroup 1, 3 Nov  9 21:28 .bashrc
crw-rw-rw- 1 nobody nogroup 1, 3 Nov  9 21:28 .idea
crw-rw-rw- 1 nobody nogroup 1, 3 Nov  9 21:28 .mcp.json
crw-rw-rw- 1 nobody nogroup 1, 3 Nov  9 21:28 scripts
```

**Agent**

Round 2 is done. No outcome changed, and none needs a `proposed` change. The verifier agreed with all 28 outcomes (7 reproduced, 5 partially reproduced, 13 not reproduced, 3 blocked). The entry re-ran cleanly with `python tools/entry.py all entries/shi-2013` (0 check errors, notebook passes in 330 s), and the numbers are the same as before.

**Wording the outputs did not support, now corrected in the notebook and the attempt record:**
- **Cell 10 and the movement-epoch-tuning deviation:** the event-timing ranges are now labelled as 5th to 95th percentiles, with the full minimum to maximum given beside them. "Code 10 follows by 320 ms on every trial" now says a median of 320 ms, range 0.22 to 0.42 s.
- **Cell 112 (longer hold):** I removed the per-session sentence. Cell 111 now lists the sessions whose shortest interval is below their first field 11 value. The re-run shows they are exactly the 3 sessions whose field 11 changes within the session, and their shortest interval falls on a trial with a lower field 11.
- **Cell 93 and notes (decoding V better than NV):** with all units and populations of 200 cells, the paired test over targets also finds the difference (P = 0.036).
- **Cell 68:** now gives reading (b)'s own values (78.4, 70.0, 75.0, 75.0%) in place of "gives the same".
- **Cell 59 and notes (400 ms subepochs):** now say the first-400 ms position percentage, 35.7%, is outside tolerance. The last-400 ms one is within.
- **Cell 76 and notes (INDX2):** now also give the all-units reading (c) result (−2.0, −14.1, −9.9%), where only Vision Only is within tolerance.

**Other changes:**
- **fig6-decoding-vv:** I removed `assumed: true`, as the verifier said. The outcome holds under both code mappings and with all units. The deviation and cell 91 now say so.
- **Eye position (cell 106 and notes):** they now say the block partly rests on a reading of the analog-file layout that is known to be partly wrong. They also say that if fields 22 and 23 were eye position, reading (a) would fail the claim (Levene's test P = 0.012 at 90°, vertical).
- **Point B8 (t-test over bootstrap accuracies):** I kept this test, because it is reading (b) of the claims file's criterion. Cell 93 and the notes now say it treats the resamples as independent, so its P value depends on how many are drawn. It decides no outcome.
- **Round-2 record:** added under `verifications` for all 28 claims, with the verifier's reasons from its report and my changes under `response`.

**Not done, and why:** the remaining points the verifier listed cannot be settled from the data set. These are the 359 sessions against the paper's 219, what fields 19 to 21 mean, the V = code 4 mapping, the clock check in sessions with no tuned unit, and the analog-file layout. They stay as stated findings and flagged assumptions. The possible misreading of the claims file (point B6) was already in `questions/shi-2013.yaml`, so I added no new question. I did not commit, as instructed.

The tool files that were already modified, and the untracked placeholder files at the repository root (such as `.bashrc` and `scripts`, created at 21:28 before this run started), are not mine and I left them alone.

## End of run

35 turns, 15 minutes, $1.19 at API prices, result: success.
