# openneuro-ds000228 · author-revise-2 · run 40740410699

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
date -u; cat transcripts/openneuro-ds000228/verifier-2-report.md; ls entries/openneuro-ds000228-richardson-2018
```

```
Wed Oct 28 18:01:25 UTC 2026
**Round-2 verifier report: Richardson et al. 2018 on ds000228 v1.1.1**

Cell numbers below are the current ones; they have moved since round 1.

**1. Outcomes and assumptions**

The claims file has 42 claims, and the attempt record gives 42 outcomes. I agree with 41 of them.

**I disagree on one: rc-overlap (record says partially_reproduced).** This is a change from round 1, where I agreed and missed it.
- The criterion defines only a reproduced outcome: "one overlapping timepoint is found and p <= .01 under a reading". It does not invoke Rule S and has no partial clause.
- The overlap here is 0 against the paper's 1, with a tolerance of 0 (cell 86).
- For irc-williams, the record reasons that a criterion with no partial clause can only give reproduced or not reproduced. By that same reasoning, rc-overlap is not_reproduced.
- Partial could only be defended by applying Rule S's partial clause, which this criterion does not name. The record should state that reasoning, or change the outcome.

**I agree with the other 41, including the three changed since round 1** (irc-williams, rc-child-adult-timecourse, maturity-across). For maturity-across, within-ToM is also significant under O2b+O3b (p = .049, cell 106). The record does not say so, but it does not change the outcome.

**Assumed outcomes.** Five outcomes are marked `assumed: true`: irc-tom-behavior-age, irc-fb-across, rc-fb-no-difference, rc-3yo-events and maturity-within. Each is stated in the deviations, with the outcome it would have under the other reading, and each is reasonable:
- **O2a:** the deposited regressors are one indicator per artifact timepoint (cell 8).
- **O3a:** the Methods restrict to TRs 11 to 168 only in paragraphs 9 and 13, not for the inter-region correlations.
[... 52 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n '/## Author/,/## Verifier/p' docs/protocol.md | head -300; grep -n "Rule S" -A15 docs/*.md | head -60
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

[... 281 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n '/### 6. Hand over for verification/,/^## Verifier/p' docs/protocol.md | tail -40; ls attempts | grep ds000228; grep -n "rc-overlap" -A40 attempts/openneuro-ds000228-richardson-2018-01.yaml | head -80
```

```
is never counted as found blind), or not checked. A finding no earlier one
  points at is new. For each claim whose outcome differs from the earlier one,
  it gives the likeliest reason. It changes no outcome or statement of the
  blind attempt.

This keeps two things apart that a repeat attempt used to mix: the dataset's
owners still get the list of what is fixed and what is not, and the attempt's
own outcomes and findings are a second independent reading, so two attempts
on the same version measure how far the registry's results repeat. The
earlier record stays as it was.

A draft can be used when the fixes are not yet published, with its
modification time recorded under `dataset: modified`, since a draft can
change. The author is started with `-f version=draft` (or a version number),
and `docs/agents/author-again.md` is its prompt.

## Local and remote datasets

`encore check` ([encore.md](encore.md)) runs this protocol on someone's own
machine, on a dataset that may be in no archive: a directory of files on that
[... 101 more lines not kept]
```

**Agent calls Bash**

```bash
awk '/### 6. Hand over for verification/{f=1} f&&/An outcome the verifier disagrees/{p=1} p{print; n++} n>45{exit}' docs/protocol.md; grep -n "rule s\|Rule S" -i docs/*.md | head; grep -n "id: rc-overlap" -A25 claims/openneuro-ds000228*.yaml 2>/dev/null || ls claims | grep 228
```

```
own words, and what you changed in reply under `response`. An outcome the verifier disagrees
with is either changed, with the reason, or left with the disagreement
recorded.

After round 1 the revision may change outcomes, and round 2 reviews them.
From round 2 on, an outcome may not differ from the one the latest
verification round of that claim agreed with: `tools/entry.py check` fails
if it does. A verifier's result is recorded as it gave it; never change
`agrees` to get past this check. The final
revision corrects text and adds the outputs the verifier asked for. If it
finds that an outcome should change, it keeps the verified outcome and writes
the change under `proposed` on that outcome, with the analysis behind it in
the notebook. A third round then settles it: `verifier-3` reviews only the
proposed changes, and `author-revise-3` applies those it agreed with and
records the round. A change that needs an analysis not yet run waits for a
new attempt.

## Repeat attempts

When a dataset changes after an attempt, for example after its owners fix
[... 27 more lines not kept]
```

**Agent calls Bash**

```bash
ls claims/openneuro-ds000228; grep -rn "id: rc-overlap" -A25 claims/openneuro-ds000228/; grep -n "Rule S\|rule S" -i claims/openneuro-ds000228/* docs/agents/*.md docs/*.md | head
```

```
10.1038-s41467-018-03399-2.yaml
claims/openneuro-ds000228/10.1038-s41467-018-03399-2.yaml:907:- id: rc-overlap
claims/openneuro-ds000228/10.1038-s41467-018-03399-2.yaml-908-  statement: ToM and pain events overlap at a single timepoint (the last of T05 and first of P05), less
claims/openneuro-ds000228/10.1038-s41467-018-03399-2.yaml-909-    overlap than chance in a permutation test.
claims/openneuro-ds000228/10.1038-s41467-018-03399-2.yaml-910-  source: Results, Reverse correlation analysis, paragraph 2; Methods, fMRI data analysis, paragraph 10
claims/openneuro-ds000228/10.1038-s41467-018-03399-2.yaml-911-  quote: The timepoints that exceeded baseline for ToM and pain networks were almost entirely
claims/openneuro-ds000228/10.1038-s41467-018-03399-2.yaml-912-    non-overlapping, with the exception of a single timepoint (2 s) ... This extent of overlap is
claims/openneuro-ds000228/10.1038-s41467-018-03399-2.yaml-913-    significantly less than that that would occur by chance
claims/openneuro-ds000228/10.1038-s41467-018-03399-2.yaml-914-  statistics:
claims/openneuro-ds000228/10.1038-s41467-018-03399-2.yaml-915-  - test: random timecourse permutations with the same number and duration of events
claims/openneuro-ds000228/10.1038-s41467-018-03399-2.yaml-916-    statistic: 5/1000 permutations with at most one timepoint of overlap
claims/openneuro-ds000228/10.1038-s41467-018-03399-2.yaml-917-    p: 0.005
claims/openneuro-ds000228/10.1038-s41467-018-03399-2.yaml-918-  expected:
claims/openneuro-ds000228/10.1038-s41467-018-03399-2.yaml-919-  - quantity: overlapping timepoints
claims/openneuro-ds000228/10.1038-s41467-018-03399-2.yaml-920-    value: 1
claims/openneuro-ds000228/10.1038-s41467-018-03399-2.yaml-921-    tolerance: 0
claims/openneuro-ds000228/10.1038-s41467-018-03399-2.yaml-922-  - quantity: permutation p
claims/openneuro-ds000228/10.1038-s41467-018-03399-2.yaml-923-    value: 0.005
claims/openneuro-ds000228/10.1038-s41467-018-03399-2.yaml-924-    tolerance: 0.00
[... 18 more lines not kept]
```

**Agent calls Bash**

```bash
cd claims/openneuro-ds000228; sed -n 100,115p 10.1038-s41467-018-03399-2.yaml; sed -n 932,936p 10.1038-s41467-018-03399-2.yaml; cd ../..; grep -n "claim: irc-williams" -A25 attempts/openneuro-ds000228-richardson-2018-01.yaml | head -30
```

```
#    a mean difference of .20) are on a standardized scale: (a) the scores z-scored over the 65
#    children aged 3 to 5; (b) raw scores. The tests are judged on p, and diffs reported for both.
#
# Tolerances. Means given with an s.e. use the s.e. as tolerance (the paper's uncertainty for a
# mean); other reported numbers use 10% of the value. Counts of participants use 0, as they are
# counts of the same people. Rule S, used by many criteria: a claim is reproduced when every
# expected value is within tolerance and every test listed under statistics gives the same sign
# and meets the paper's p bound (for an exact p, the same side of .05, or of the corrected alpha
# the claim gives, as the paper's); partially reproduced when the tests hold but some value is out of
# tolerance; not reproduced when a test fails or its sign is reversed.
#
# Outside data the paper relies on: the independent adult sample (n = 20, scanned by Evelina
# Fedorenko and colleagues) that defined the group ROIs and replicated the events (not deposited;
# only the ROI centers are given); the face and scene group-constrained parcels of Julian et al.
# 2012 (http://web.mit.edu/bcs/nklab/GSS.shtml); the hand-coded "mental", "social" and "pain"
# events of Jacoby et al. 2016 (NeuroImage 126, 39-48); Neurosynth for the M1 and V1 centers
    of 5 in 1000, rounded up. Reproduced when one overlapping timepoint is found and p <= .01 under a
    reading.
- id: rc-child-adult-timecourse
  statement: The mean network timecourse of each child age group correlates with the adult mean
[... 31 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n '/^verifications/,$p' attempts/openneuro-ds000228-richardson-2018-01.yaml | head -60; grep -n "replication-sample" -A12 attempts/openneuro-ds000228-richardson-2018-01.yaml | sed -n '1,60p'
```

```
verifications:
- date: '2026-10-28'
  kind: agent
  by: Independent agent run by CatalystNeuro (verifier-1, same harness, separate context, did not
    write the notebook)
  reviewed: Round 1. The executed notebook with the conclusion cells removed, the helper module and
    the claims file, with the paper. The summary cell was not removed by the handover, as it shared
    a cell with the blocked claims, and the verifier read it after forming most of its outcomes. It
    queried the archive's file list for the blocked claims and tested the helper functions on
    synthetic inputs. Of 42 claims it agreed with 39 outcomes and disagreed on irc-williams,
    rc-child-adult-timecourse and maturity-across.
  results:
  - claim: participants
    agrees: true
    outcome: reproduced
    reason: Every count matches exactly (122, 33, 64, 20, 17/14/34/23/34). Mean child age is 6.71.
    response: No change needed.
  - claim: supp-table1-behavior-by-age
    agrees: true
    outcome: reproduced
[... 67 more lines not kept]
```

**Agent calls Bash**

```bash
ls schemas 2>/dev/null; grep -rn "blocked_by" schemas/*attempt* 2>/dev/null | head; grep -n "verifications" -A60 schemas/attempt*.json 2>/dev/null | grep -n '"' | head -60
```

```
attempt.schema.json
claims.schema.json
entry.schema.json
201:          "blocked_by": {
269:              "blocked_by": {
299:                "blocked_by",
1:334:    "verifications": {
2:335-      "type": "array",
3:336-      "items": {
4:337-        "type": "object",
5:338-        "additionalProperties": false,
6:339-        "required": [
7:340-          "date",
8:341-          "kind",
9:342-          "by",
10:343-          "results"
12:345-        "properties": {
13:346-          "date": {
14:347-            "type": "string",
15:348-            "format": "date"
[... 33 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 390,420p schemas/attempt.schema.json; sed -n 255,310p schemas/attempt.schema.json
```

```
"blocked"
                  ]
                }
              }
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
[... 67 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/openneuro-ds000228-richardson-2018; python -c "
import json;nb=json.load(open('reproduce_richardson_2018.ipynb'))
for i,c in enumerate(nb['cells']):
  s=''.join(c['source'])
  if c['cell_type']=='markdown' and ('Result' in s or i>=120): print('=====',i, c.get('metadata',{}).get('tags')); print(s)
" | sed -n '1,400p' | grep -n "" | awk -F: '{print}' > $TMPDIR/md.txt; wc -l $TMPDIR/md.txt; cat README.md
```

```
156 /tmp/claude-1001/md.txt
# Richardson, Lisandrelli, Riobueno-Naylor & Saxe (2018) from OpenNeuro ds000228

Tests the findings of [Richardson et al. (2018)](https://doi.org/10.1038/s41467-018-03399-2) on
[OpenNeuro ds000228](https://openneuro.org/datasets/ds000228/versions/1.1.1), snapshot 1.1.1,
which holds movie-viewing fMRI of 122 children aged 3 to 12 and 33 adults, with the paper's own
preprocessed images, artifact and CompCor regressors, group ROIs and behavioural scores.

| Claims | Outcome |
|---|---|
| Sample, behaviour and motion (11 claims) | Reproduced |
| Inter-region correlations (15 claims) | 6 partially reproduced, 9 not reproduced |
| Reverse correlation (8 claims) | 1 reproduced, 3 partially reproduced, 4 not reproduced |
| Functional maturity (4 claims) | 3 reproduced, 1 not reproduced |
| Face regions (2 claims) | 1 reproduced, 1 not reproduced |
| Replication sample and hand-coded events (2 claims) | Blocked |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

[... 14 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/md.txt"
}
```

```
1	1:===== 13 None
2	2:**Result: reproduced.** All nine counts match exactly (122 children, 33 adults, 64 and 20 female; 17, 14, 34, 23 and 34 children by age group) and the mean child age is 6.71 years against 6.7. The age-group ranges match Supplementary Table 1. The five children excluded for motion are not in the dataset.
3	3:===== 16 None
4	4:**Result: reproduced.** The five mean ToM scores (.517, .610, .724, .875, .956) are within 10% of .54, .63, .73, .88 and .96, and the nine false-belief group counts by age (4/4/9, 3/7/4, 23/9/2) match exactly.
5	5:===== 19 None
6	6:**Result: reproduced.** ToM score against age: tau-b = .665 (paper .66), p = 5.4e-26. DCCS against age in the 64 children with a DCCS score: tau-b = .198 (paper .20), p = .048 (paper .049, same side of .05).
7	7:===== 22 None
8	8:**Result: reproduced.** Partial Kendall tau of ToM and DCCS given age = .186 (paper .19, tolerance .019), p = .031 (paper .03).
9	9:===== 25 None
10	10:**Result: reproduced.** 30 passers (15 female), 20 inconsistent (13 female), 15 failers (6 female), as deposited in FB_Group; the groups recomputed from FB_Composite with the Methods' cut-offs are the same.
11	11:===== 28 None
12	12:**Result: reproduced.** Under reading (a), the 18 non-false-belief items deposited as ToM Booklet-Matched-NOFB, the means are .546, .572 and .753 (paper .55, .57, .75) and Kruskal-Wallis H = 22.95 (paper 22.96), p = 1e-05. The Tukey tests match: Pass-Fail diff 1.24 on the z scale (paper 1.2), p = 3.8e-05; Pass-Inc 1.08 (paper 1.08), p = 7.8e-05; Inc-Fail .16 (paper .16), p = .85. The z-scaled diffs (O9a) are the ones that match the paper's. Reading (b), the full score, gives means .451, .571, .792, out of tolerance for failers and passers.
13	13:===== 30 None
14	14:**Result: reproduced.** Mean ages 4.08, 4.75 and 5.23 (paper 4.1, 4.8, 5.2). Tukey on the z scale: Pass-Fail diff 1.42 (paper 1.4), p = 4.3e-06; Inc-Fail .83 (paper .83), p = .015 (paper .01); Pass-Inc .59 (paper .59), p = .047 (pap
[... 143 more lines not kept]
```

**Agent calls Bash**

```bash
cd  ls executed/openneuro-ds000228-richardson-2018/ 2>/dev/null; python -c "
import json;nb=json.load(open('executed/openneuro-ds000228-richardson-2018/reproduce_richardson_2018.ipynb'))
for i in (54,102,106,108):
  c=nb['cells'][i]
  print('=====',i); print(''.join(c['source'])[:1500])
  for o in c.get('outputs',[]): print(''.join(o.get('text',''))[:3000])
"
```

```
Exit code 1
Traceback (most recent call last):
  File "<string>", line 2, in <module>
    import json;nb=json.load(open('executed/openneuro-ds000228-richardson-2018/reproduce_richardson_2018.ipynb'))
                             ~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
FileNotFoundError: [Errno 2] No such file or directory: 'executed/openneuro-ds000228-richardson-2018/reproduce_richardson_2018.ipynb'
```

**Agent calls Bash**

```bash
cd  date -u; time python tools/entry.py all entries/openneuro-ds000228-richardson-2018 2>&1 | tail -20; date -u
```

```
Wed Oct 28 18:02:06 UTC 2026
Installed kernelspec registry-openneuro-ds000228-richardson-2018 in executed/openneuro-ds000228-richardson-2018/.venv/share/jupyter/kernels/registry-openneuro-ds000228-richardson-2018
0 error(s)
pass  reproduce_richardson_2018.ipynb  (183 s)

real	3m22.387s
user	3m11.143s
sys	1m17.133s
Wed Oct 28 18:05:29 UTC 2026
```

**Agent calls Bash**

```bash
cd  python -c "
import json;nb=json.load(open('executed/openneuro-ds000228-richardson-2018/reproduce_richardson_2018.ipynb'))
for i in (54,62,68,86,102,106):
  c=nb['cells'][i]
  print('=====',i); 
  for o in c.get('outputs',[]): print(''.join(o.get('text',''))[:2500])
"
```

```
===== 54
                   reading measure  b raw  b z (O4a)     t        p  t motion  p motion
0         O1 all, O2a, O3a    wToM -0.173      -1.16 -6.54 8.66e-10     -1.64     0.103
1         O1 all, O2a, O3a   wPain -0.135       -1.2 -6.72 3.47e-10    -0.512     0.609
2         O1 all, O2a, O3a  across 0.0868       0.83  4.49 1.38e-05      2.87   0.00475
3         O1 all, O2a, O3b    wToM -0.167      -1.11 -6.23 4.38e-09     -1.77    0.0793
4         O1 all, O2a, O3b   wPain -0.132      -1.17 -6.48  1.2e-09    -0.495     0.621
5         O1 all, O2a, O3b  across 0.0836      0.798  4.28 3.28e-05      2.77    0.0064
6         O1 all, O2b, O3a    wToM  -0.18      -1.22 -7.05 5.94e-11     -1.89    0.0608
7         O1 all, O2b, O3a   wPain -0.139      -1.21 -6.72 3.42e-10     0.103     0.918
8         O1 all, O2b, O3a  across 0.0814      0.769  4.17 5.19e-05       3.3   0.00122
9         O1 all, O2b, O3b    wToM -0.174      -1.17 -6.71 3.69e-10     -1.85    0.0665
10        O1 all, O2b, O3b   wPain -0.137      -1.19 -6.56 7.96e-10    0.0573     0.954
11        O1 all, O2b, O3b  across 0.0774      0.728  3.92 0.000135      3.35   0.00102
12  O1 with_data, O2a, O3a    wToM -0.173      -1.16 -6.54 8.66e-10     -1.64     0.103
13  O1 with_data, O2a, O3a   wPain -0.135       -1.2 -6.72 3.47e-10    -0.512     0.609
14  O1 with_data, O2a, O3a  across 0.0868       0.83  4.49 1.38e-05      2.87   0.00475
15  O1 with_data, O2a, O3b    wToM -0.167      -1.11 -6.23 4.38e-09     -1.77    0.0794
16  O1 with_data, O2a, O3b   wPain -0.132      -1.17 -6.48  1.2e-09    -0.495     0.621
17  O1 with_data, O2a, O3b  across 0.0836      0.798  4.28 3.28e-05      2.77    0.0064
[... 98 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/openneuro-ds000228-richardson-2018; cat > $TMPDIR/ed.py <<'EOF'
import json,sys
p='reproduce_richardson_2018.ipynb'
nb=json.load(open(p))
reps={
55:[("so the tests hold with the paper's signs, but all three t values are outside 10% of -5.7, -3.8 and 7.2 under every reading.",
"so the tests hold with the paper's signs, but the t values are out of tolerance (10% of -5.7, -3.8 and 7.2): within-Pain (-6.48 to -6.72) and across (3.92 to 4.49) under every reading, and within-ToM under three of the four O2 and O3 readings (-6.54, -6.71, -7.05; -6.23 under O2a with O3b is inside).")],
87:[("The overlap count differs from the paper's by one timepoint.",
"The overlap count differs from the paper's by one timepoint. The criterion states only when the claim is reproduced. The outcome is partial because the claim's test (less overlap than chance, p <= .01) holds and only its expected count is out of tolerance, which is what the claims file's Rule S and the protocol call a partial result; under irc-williams, by contrast, two of the paper's tests fail.")],
103:[("Under the rc-events reading (O5a) with O6b,",
"No reading reproduced rc-events, so the criterion's \"reading that reproduced rc-events\" is extended to the reading that matched it best (O5a). Under O5a with O6b,")],
107:[("Within-ToM does not predict ToM maturity (t = 1.53, p = .13), as in the paper,",
"Within-ToM does not predict ToM maturity under the main reading (t = 1.53, p = .13), as in the paper, though under O2b with O3b it does (t = 1.99, p = .049),")],
122:[("Every behavioural and demographic number of the paper is\nrecovered exactly from participants.tsv,",
"Every behavioural and demographic number of the paper is\nrecovered from participants.tsv: the counts exactly, the other values within tolerance (for example\nmean ToM scores .517 and .610 against .54 and .63, DCCS p .048 against .049, Inc-Fail p .015\nagainst .01, DCCS b .148 against .16), beh-fb-tom under reading (a) only,"),
("the inter-region correlations are higher within networks and less negative across\nnetworks than the paper reports (adults .604, .398, -.051 against .48, .35, -.17),",
"the adult inter-region correlations are higher within networks and less negative across\nnetworks than the paper reports (.604, .398, -.051 against .48, .35, -.17); in the 3-year-olds\nwithin-ToM is higher (.326 against .21) but within-Pain is lower (.179 against .23, and\nnon-bilateral Pain .146 against .17),")],
}
for i,rs in reps.items():
  s=''.join(nb['cells'][i]['source'])
  for a,b in rs:
    assert s.count(a)==1,(i,a[:40])
    s=s.replace(a,b)
  nb['cells'][i]['source']=s.splitlines(keepends=True)
json.dump(nb,open(p,'w'),indent=1,ensure_ascii=False); open(p,'a').write('\n')
EOF
python $TMPDIR/ed.py && git diff --stat
```

```
.../reproduce_richardson_2018.ipynb                    | 18 +++++++++++-------
 1 file changed, 11 insertions(+), 7 deletions(-)
```

**Agent calls Bash**

```bash
git diff | head -80
```

```
diff --git a/entries/openneuro-ds000228-richardson-2018/reproduce_richardson_2018.ipynb b/entries/openneuro-ds000228-richardson-2018/reproduce_richardson_2018.ipynb
index b083649e8..850dda789 100644
--- a/entries/openneuro-ds000228-richardson-2018/reproduce_richardson_2018.ipynb
+++ b/entries/openneuro-ds000228-richardson-2018/reproduce_richardson_2018.ipynb
@@ -978,7 +978,7 @@
    "id": "6bae4ccf",
    "metadata": {},
    "source": [
-    "**Result: partially reproduced.** Adults have higher within-ToM (t = -6.54 for the child effect, p = 8.7e-10) and within-Pain (t = -6.72, p = 3.5e-10) correlations and a more negative across-network correlation (t = 4.49, p = 1.4e-05) than children, so the tests hold with the paper's signs, but all three t values are outside 10% of -5.7, -3.8 and 7.2 under every reading. z-scaled b values are -1.16, -1.20 and .83 (paper -.97, -.75, 1.26). The motion effects differ from the paper's: on within-ToM t = -1.64 (paper -4.3), on across t = 2.87, p = .005 (paper not significant)."
+    "**Result: partially reproduced.** Adults have higher within-ToM (t = -6.54 for the child effect, p = 8.7e-10) and within-Pain (t = -6.72, p = 3.5e-10) correlations and a more negative across-network correlation (t = 4.49, p = 1.4e-05) than children, so the tests hold with the paper's signs, but the t values are out of tolerance (10% of -5.7, -3.8 and 7.2): within-Pain (-6.48 to -6.72) and across (3.92 to 4.49) under every reading, and within-ToM under three of the four O2 and O3 readings (-6.54, -6.71, -7.05; -6.23 under O2a with O3b is inside). z-scaled b values are -1.16, -1.20 and .83 (paper -.97, -.75, 1.26). The motion effects differ from the paper's: on within-ToM t = -1.64 (paper -4.3), on across t = 2.87, p = .005 (paper not significant)."
    ]
   },
   {
@@ -1522,7 +1522,7 @@
    "id": "bdffea09",
    "metadata": {},
    "source": [
-    "**Result: partially reproduced.** The ToM and pain events found (O5a) do not overlap at all (0 TRs, where th
[... 42 more lines not kept]
```

**Agent calls Bash**

```bash
python - <<'EOF'
import json
p='reproduce_richardson_2018.ipynb'
nb=json.load(open(p))
c=nb['cells'][107]; s=''.join(c['source'])
a="as in the paper, though under O2b with O3b it does (t = 1.99, p = .049), but within-Pain does predict Pain maturity"
assert a in s
s=s.replace(a,"as in the paper; under O2b with O3b it does (t = 1.99, p = .049). Within-Pain does predict Pain maturity")
c['source']=s.splitlines(keepends=True)
json.dump(nb,open(p,'w'),indent=1,ensure_ascii=False); open(p,'a').write('\n')
EOF
git diff --stat; grep -n "irc-adult$\|claim: irc-adult\b" -A20 ../../attempts/openneuro-ds000228-richardson-2018-01.yaml | head -30; grep -n "claim: irc-adult-vs-child" -A14 ../../attempts/openneuro-ds000228-richardson-2018-01.yaml | head -16; grep -n "^findings" -A12 ../../attempts/openneuro-ds000228-richardson-2018-01.yaml
```

```
.../reproduce_richardson_2018.ipynb                    | 18 +++++++++++-------
 1 file changed, 11 insertions(+), 7 deletions(-)
109:- claim: irc-adult
110-  outcome: partially_reproduced
111-  notebook: reproduce_richardson_2018.ipynb
112:  output: claim:irc-adult
113-  measured: [0.604, 0.398, -0.051, 19.1, 21.8]
114-  notes: Main reading (O1 all voxels of the deposited masks, O2a, O3a). Adult means within-ToM
115-    .604, within-Pain .398, across -.051; paired t within-ToM against across 19.1 and within-Pain
116-    against across 21.8, both p < 1e-18. The two t values are in tolerance under three of the
117-    four O2 and O3 readings; the three means are out of tolerance under all. O1 with only voxels
118-    with data gives identical values. Variants outside the paper's method (no high-pass, 50 s
119-    high-pass, no CompCor) give adult means from .556 to .645 within-ToM and -.051 to .059
120-    across, none near the paper's. Further diagnostic variants, adults (within-ToM, within-Pain,
121-    across), are mean r in place of z .519, .354, -.049; the high-pass basis in the nuisance
122-    regression .593, .393, -.086; left and right M1 as two regressors .599, .390, -.037; and the
123-    mean ToM and Pain signal as an added regressor .286, .258, -.382. Only the last, which is not
124-    the paper's method, moves the across value past the paper's, so the offset is in the direction
125-    of a shared signal removed in the paper's processing and not here, which no step of the
126-    Methods accounts for. The ROI masks are in MNI mm (9 mm sphere centroids within 3.7 mm of the
[... 41 more lines not kept]
```

**Agent**

Now the record edits.

**Agent calls Bash**

```bash
cd  python - <<'EOF'
p='attempts/openneuro-ds000228-richardson-2018-01.yaml'
s=open(p).read()
reps=[
("""    the paper's method, moves the across value past the paper's, so the offset is in the direction
    of a shared signal removed in the paper's processing and not here, which no step of the
    Methods accounts for.""",
"""    the paper's method, moves the across value past the paper's, and it also takes both
    within-network values well below the paper's (.286 and .258 against .48 and .35). A shared
    signal removed in the paper's processing would shift the across value in this direction, but
    this variant does not match the paper's pattern, and no step of the Methods accounts for the
    offset."""),
("""    with the paper's signs and below its p values, but all three t values are out of tolerance
    under every reading (-6.23 to -7.05, -6.48 to -6.72, 3.92 to 4.49).""",
"""    with the paper's signs and below its p values, but the t values are out of tolerance:
    within-Pain (-6.48 to -6.72) and across (3.92 to 4.49) under every reading, within-ToM under
    three of the four O2 and O3 readings (-6.54 to -7.05; -6.23 under O2a with O3b is within
    -5.7 +/- .57)."""),
("""    against .48, .35 and -.17; 3yo within-ToM .326 against .21).""",
"""    against .48, .35 and -.17). In the 3-year-olds within-ToM is higher (.326 against .21) but
    within-Pain is lower (.179 against .23; non-bilateral Pain .146 against .17), so the offset
    is not the same in every group."""),
]
for a,b in reps:
    assert s.count(a)==1,a[:50]
    s=s.replace(a,b)
open(p,'w').write(s)
EOF
grep -n "claim: rc-3yo-events" -A22 attempts/openneuro-ds000228-richardson-2018-01.yaml | head -24; grep -n "claim: maturity-across" -A14 attempts/openneuro-ds000228-richardson-2018-01.yaml | head -15
```

```
379:- claim: rc-3yo-events
380-  outcome: partially_reproduced
381-  assumed: true
382-  notebook: reproduce_richardson_2018.ipynb
383-  output: claim:rc-3yo-events
384-  measured: [40, 24, 6, 1]
385-  notes: Reverse correlation on the 17 three-year-olds with the rc-events reading (O5a) and O6b.
386-    3yo pain events 40 s overlapping 6 of 12 adult pain events (22 s) and T04 (6 s); 3yo ToM events
387-    24 s overlapping 1 of 7 adult ToM events (4 s) and P01 (4 s). Both cross-network overlaps hold;
388-    times and the pain count do not. Under O6a, pain 40 s, 6 of 12, T04 6 s; ToM 20 s, 1 of 7, P01
389-    0 s, so the P01 overlap fails. Adult events are those of Supplementary Table 3.
390-  deviations:
391-  - The rc-events reading ties between O6a and O6b. Assumed O6b, z-normalization over all 168 TRs,
392-    because Methods paragraph 9 z-normalizes each ROI timecourse first and leaves out the first 10
393-    timepoints only from the t-tests. Under O6a the claim would not be reproduced.
394-- claim: maturity-across
395-  outcome: not_reproduced
396-  notebook: reproduce_richardson_2018.ipynb
397-  output: claim:maturity-across
398-  measured: [-4.52, -3.55]
[... 19 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python - <<'EOF'
p='attempts/openneuro-ds000228-richardson-2018-01.yaml'
s=open(p).read()
reps=[
("""    timepoints only from the t-tests. Under O6a the claim would not be reproduced.
""",
"""    timepoints only from the t-tests. Under O6a the claim would not be reproduced.
  - The criterion asks for the reading that reproduced rc-events, and no reading did. The reading
    that matched rc-events best (O5a) is used, an extension of the criterion.
"""),
("""    every reading. Within-ToM t = 1.53, p = .13, not significant, as in the paper; within-Pain t =""",
"""    every reading. Within-ToM t = 1.53, p = .13, not significant, as in the paper (under O2b with
    O3b it is significant, t = 1.99, p = .049); within-Pain t ="""),
("""    overlap than chance holds; the
    overlap count does not match.""","""    overlap than chance holds; the
    overlap count does not match. The criterion states only when the claim is reproduced. The
    outcome is partial because the claim's test (p <= .01) holds and only its expected count is
    out of tolerance, the case the claims file's Rule S and the protocol call partial; irc-williams
    is not reproduced because two of the paper's tests fail there. The verifier would give
    not_reproduced; the disagreement is recorded under verifications."""),
]
for a,b in reps:
    assert s.count(a)==1,a[:50]
    s=s.replace(a,b)
open(p,'w').write(s)
EOF
sed -n 300,320p attempts/openneuro-ds000228-richardson-2018-01.yaml
```

```
Traceback (most recent call last):
  File "<stdin>", line 22, in <module>
AssertionError:     overlap than chance holds; the
    overlap cou
    covering all 7 ToM events and 10 of 12 pain events of Supplementary Table 3 (P08 and P10
    missed). Under O5b and O5c, 7 ToM events (56 s, all 7 table events) and 8 pain events (62 s,
    8 of 12). The pain time is in tolerance under O5a, the ToM time under none; the counts never
    both match. At least 5 of 7 and 9 of 12 table events are found under O5a, the partial
    outcome. Peak TRs of the found ToM events (131, 95, 64, 150, 46, 125, 54) are within one TR
    of the table's.
- claim: rc-overlap
  outcome: partially_reproduced
  notebook: reproduce_richardson_2018.ipynb
  output: claim:rc-overlap
  measured: [0, 0.002]
  notes: The found events (O5a) overlap at no timepoint, against 1 in the paper; permutation p =
    .002 under reading (a), 158 TRs, and p < .001 (0 of 1000) under reading (b), 159 TRs (mean
    permuted overlap 11.9 TRs under both). Under O5b and O5c the overlap is also 0, p = .019 to
    .049. With the paper's own events (Supplementary
    Table 3, variant) the overlap is 1 TR, p = .002 and .008. Less overlap than chance holds; the
[... 5 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python - <<'EOF'
p='attempts/openneuro-ds000228-richardson-2018-01.yaml'
s=open(p).read()
reps=[
("""    timepoints only from the t-tests. Under O6a the claim would not be reproduced.
""",
"""    timepoints only from the t-tests. Under O6a the claim would not be reproduced.
  - The criterion asks for the reading that reproduced rc-events, and no reading did. The reading
    that matched rc-events best (O5a) is used, an extension of the criterion.
"""),
("""    every reading. Within-ToM t = 1.53, p = .13, not significant, as in the paper; within-Pain t =""",
"""    every reading. Within-ToM t = 1.53, p = .13, not significant, as in the paper (under O2b with
    O3b it is significant, t = 1.99, p = .049); within-Pain t ="""),
("""    Table 3, variant) the overlap is 1 TR, p = .002 and .008. Less overlap than chance holds; the
    overlap count does not match.
""","""    Table 3, variant) the overlap is 1 TR, p = .002 and .008. Less overlap than chance holds; the
    overlap count does not match. The criterion states only when the claim is reproduced. The
    outcome is partial because the claim's test (p <= .01) holds and only its expected count is
    out of tolerance, the case the claims file's Rule S and the protocol call partial;
    irc-williams is not reproduced because two of the paper's tests fail there. The verifier
    would give not_reproduced in round 2; the disagreement is recorded under verifications.
"""),
]
for a,b in reps:
    assert s.count(a)==1,a[:50]
    s=s.replace(a,b)
open(p,'w').write(s)
EOF
grep -n "^- date\|reviewed:" attempts/openneuro-ds000228-richardson-2018-01.yaml; tail -5 attempts/openneuro-ds000228-richardson-2018-01.yaml
```

```
517:- date: '2026-10-28'
521:  reviewed: Round 1. The executed notebook with the conclusion cells removed, the helper module and
    reason: The Jacoby et al. 2016 coding is not in the snapshot. It exists in an unpinned Saxe-lab
      script (movloc.zip); as the notebook's reason is that it is unpinned, "other" fits better than
      "data_missing". The claim becomes partly testable if an unpinned outside input is accepted.
    response: No change needed; the record already gives blocked_by other for this reason. The
      protocol allows only pinned outside inputs, so the script is not used.
```

**Agent calls Bash**

```bash
cd  python - <<'EOF'
p='attempts/openneuro-ds000228-richardson-2018-01.yaml'
s=open(p).read()
a="""      ROIs, mriqc). The deposited README lists"""
assert s.count(a)==1
s=s.replace(a,"""      ROIs, mriqc), so blocked with data_missing. The deposited README lists""")
open(p,'w').write(s)
import yaml
d=yaml.safe_load(s)
for o in d['outcomes']: print(o['claim'],o['outcome'],o.get('blocked_by',''),o.get('assumed',''))
print(d['verifications'][0].keys())
EOF
```

```
Exit code 1
Traceback (most recent call last):
  File "<stdin>", line 8, in <module>
  File "/opt/hostedtoolcache/Python/3.13.17/x64/lib/python3.13/site-packages/yaml/__init__.py", line 125, in safe_load
    return load(stream, SafeLoader)
  File "/opt/hostedtoolcache/Python/3.13.17/x64/lib/python3.13/site-packages/yaml/__init__.py", line 81, in load
    return loader.get_single_data()
           ~~~~~~~~~~~~~~~~~~~~~~^^
  File "/opt/hostedtoolcache/Python/3.13.17/x64/lib/python3.13/site-packages/yaml/constructor.py", line 49, in get_single_data
    node = self.get_single_node()
  File "/opt/hostedtoolcache/Python/3.13.17/x64/lib/python3.13/site-packages/yaml/composer.py", line 36, in get_single_node
    document = self.compose_document()
  File "/opt/hostedtoolcache/Python/3.13.17/x64/lib/python3.13/site-packages/yaml/composer.py", line 55, in compose_document
    node = self.compose_node(None, None)
  File "/opt/hostedtoolcache/Python/3.13.17/x64/lib/python3.13/site-packages/yaml/composer.py", line 84, in compose_node
    node = self.compose_mapping_node(anchor)
  File "/opt/hostedtoolcache/Python/3.13.17/x64/lib/python3.13/site-packages/yaml/composer.py", line 133, in compose_mapping_node
    item_value = self.compose_node(node, item_key)
  File "/opt/hostedtoolcache/Python/3.13.17/x64/lib/python3.13/site-packages/yaml/composer.py", line 82, in compose_node
    node = self.compose_sequence_node(anchor)
[... 28 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -i 's/but the t values are out of tolerance:$/but the t values are out of tolerance,/' attempts/openneuro-ds000228-richardson-2018-01.yaml; python - <<'EOF'
import yaml
d=yaml.safe_load(open('attempts/openneuro-ds000228-richardson-2018-01.yaml'))
for o in d['outcomes']: print(o['claim'],o['outcome'],o.get('blocked_by',''),o.get('assumed',''))
print(len(d['verifications']))
EOF
```

```
participants reproduced  
supp-table1-behavior-by-age reproduced  
beh-tom-age reproduced  
beh-tom-dccs reproduced  
beh-fb-groups reproduced  
beh-fb-tom reproduced  
beh-fb-age reproduced  
beh-fb-dccs reproduced  
motion-child-adult reproduced  
motion-not-age-tom reproduced  
motion-not-fb reproduced  
irc-adult partially_reproduced  
irc-age-within not_reproduced  
irc-age-across not_reproduced  
irc-adult-vs-child partially_reproduced  
irc-control-networks partially_reproduced  
irc-williams not_reproduced  
irc-3yo-distinct not_reproduced  
irc-3yo-not-anticorrelated partially_reproduced  
irc-3yo-homologous not_reproduced  
[... 23 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat > $TMPDIR/r2.py <<'EOF'
import yaml
p='attempts/openneuro-ds000228-richardson-2018-01.yaml'
d=yaml.safe_load(open(p))
G="Agrees. Every other Result sentence and record note checked matches the printed numbers."
N="No change needed."
spec={
'supp-table1-behavior-by-age':("Agrees. The summary's \"recovered exactly\" is wrong for some numbers, the mean ToM scores .517 and .610 against .54 and .63 are within tolerance but not exact.","The summary now says the counts match exactly and the other values are within tolerance, with these examples."),
'beh-tom-age':("Agrees. The summary's \"recovered exactly\" does not hold for DCCS p .048 against .049.","Summary corrected as for supp-table1-behavior-by-age."),
'beh-fb-tom':("Agrees. beh-fb-tom holds only under reading (a), which the summary's \"recovered exactly\" leaves out.","The summary now says beh-fb-tom holds under reading (a) only."),
'beh-fb-age':("Agrees. The summary's \"recovered exactly\" does not hold for Inc-Fail p .015 against .01.","Summary corrected as for supp-table1-behavior-by-age."),
'motion-child-adult':("Agrees. Per-participant artifact counts against the ART thresholds were not recomputed, as the record says; this does not bear on a conclusion.","No change. Recomputing ART from the raw images is outside this attempt."),
'motion-not-fb':("Agrees. The summary's \"recovered exactly\" does not hold for DCCS b .148 against .16.","Summary corrected as for supp-table1-behavior-by-age."),
'irc-adult':("Agrees. The IRC offset is still unexplained and probably drives most of the inter-region, 3-year-old and maturity failures. The note \"so the offset is in the direction of a shared signal removed in the paper's processing\" is weakly supported, since the shared-signal regressor also pushes both within-network values below the paper's (.286 and .258 against .48 and .35), so it shows only the direction of the across-network shift. Cell 49's hedged wording is acceptable.","The note now says the shared-signal variant shifts the across value in the paper's direction but takes both within-network values below the paper's, so it does not match the paper's pattern. The README's statement of the offset is limited to adults."),
'irc-adult-vs-child':("Agrees, the outcome stays partial. Cell 55 and the record say all three t values are out of tolerance under every reading, but within-ToM t = -6.23 under O2a+O3b is inside the tolerance of -5.7 +/- .57.","Cell 55 and the notes now say within-Pain and across are out of tolerance under every reading and within-ToM under three of the four readings, with -6.23 under O2a with O3b inside."),
'irc-williams':("Agrees with the outcome changed since round 1. The record reasons that a criterion with no partial clause can only give reproduced or not reproduced.",N),
'irc-3yo-distinct':("Agrees. The README's \"higher within networks and less negative across them\" holds for adults, but 3-year-old within-Pain is lower, .179 against .23 (cell 62); the record's first finding cites 3-year-old within-ToM (.326 against .21) and leaves out the lower Pain value.","The README, the summary and the first finding now limit the statement to adults and give the lower 3-year-old Pain values."),
'irc-3yo-nonbilateral':("Agrees. 3-year-old non-bilateral Pain is .146 against .17 (cell 68), lower than the paper's, against the README's statement.","As for irc-3yo-distinct."),
'irc-tom-behavior-age':("Agrees. Assumed outcome, stated in the deviations with the outcome under the other reading; O2a is reasonable, as the deposited regressors are one indicator per artifact timepoint (cell 8), and O3a, since the Methods restrict to TRs 11 to 168 only in paragraphs 9 and 13. As an absence claim it still flips between readings; the rule is now stated, so it is decided, but the outcome rests on the assumed readings.",N),
'irc-fb-across':("Agrees. Assumed outcome, reasonable under O2a and O3a, as for irc-tom-behavior-age. As an absence claim it still flips between readings and its outcome rests on the assumed readings.",N),
'rc-overlap':("Disagrees. The criterion defines only a reproduced outcome (\"one overlapping timepoint is found and p <= .01 under a reading\"), does not invoke Rule S and has no partial clause. The overlap is 0 against 1 with tolerance 0 (cell 86). By the record's reasoning for irc-williams it is not_reproduced. Partial could only be defended by applying Rule S's partial clause, which this criterion does not name; the record should state that reasoning, or change the outcome. In round 1 the verifier agreed and missed this.","Outcome kept and the disagreement recorded. The reasoning is now stated in cell 87 and the notes, the claim's test (less overlap than chance, p <= .01) holds and only its expected count is out of tolerance, which Rule S and the protocol's definition (holds only in part) call partial. irc-williams differs, since there two of the paper's tests fail, which Rule S counts as not reproduced."),
'rc-child-adult-timecourse':("Agrees with the outcome changed since round 1. Problem 4 is resolved, each bin is checked against its own bound (cell 90).",N),
'rc-fb-no-difference':("Agrees. Assumed outcome, reasonable under O7a, since the events and their peaks are defined on the z-normalized timecourse. As an absence claim it still flips between readings and rests on the assumed reading.",N),
'rc-3yo-events':("Agrees. Assumed O6b (Methods paragraph 9 order), only a tie-break, but the claim is still partial under O6b and not reproduced under O6a. The criterion asks for \"the reading that reproduced rc-events\", and no reading did; using the best-matching reading is a sensible extension, and the record should say it is one.","Cell 103 and a deviation now say that the best-matching reading (O5a) is an extension of the criterion."),
'maturity-across':("Agrees with the outcome changed since round 1. Within-ToM is also significant under O2b+O3b (p = .049, cell 106); the record does not say so, but it does not change the outcome.","Added to cell 107 and the notes."),
'maturity-within':("Agrees. Assumed outcome, reasonable under O2a and O3a. As an absence claim it still flips between readings and rests on the assumed readings.",N),
'replication-sample':("Agrees. The record's response explains why other is used (the checker does not allow data_missing on an elsewhere claim), which the verifier accepts. The record did not mention that the verifier gave blocked_by data_missing in round 1.","The round-1 reason now says the verifier gave data_missing."),
}
res=[]
for o in d['outcomes']:
    c=o['claim']
    r,resp=spec.get(c,(G,N))
    e={'claim':c,'agrees':c!='rc-overlap','outcome':'not_reproduced' if c=='rc-overlap' else o['outcome'],'reason':r,'response':resp}
    res.append(e)
block={'date':'2026-10-28','kind':'agent','by':'Independent agent run by CatalystNeuro (verifier-2, same harness, separate context, did not write the notebook)',
'reviewed':'Round 2. The full executed notebook after the round-1 revision, the helper module, the claims file and the attempt record, with the paper. Of 42 claims it agreed with 41 outcomes and disagreed on rc-overlap. It found no misreading in the claims file, so no question was added. The README run time was also questioned and is now given from the run (183 s for the notebook).',
'results':res}
out=yaml.safe_dump([block],sort_keys=False,width=100,allow_unicode=True)
open(p,'a').write(out)
EOF
python $TMPDIR/r2.py; tail -30 attempts/openneuro-ds000228-richardson-2018-01.yaml
```

```
outcome: reproduced
    reason: Agrees. Every other Result sentence and record note checked matches the printed numbers.
    response: No change needed.
  - claim: maturity-fb
    agrees: true
    outcome: reproduced
    reason: Agrees. Every other Result sentence and record note checked matches the printed numbers.
    response: No change needed.
  - claim: face-rc
    agrees: true
    outcome: not_reproduced
    reason: Agrees. Every other Result sentence and record note checked matches the printed numbers.
    response: No change needed.
  - claim: face-overlap
    agrees: true
    outcome: reproduced
    reason: Agrees. Every other Result sentence and record note checked matches the printed numbers.
    response: No change needed.
  - claim: replication-sample
    agrees: true
[... 10 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python - <<'EOF'
p='attempts/openneuro-ds000228-richardson-2018-01.yaml'
s=open(p).read()
a=" The README run time was also questioned and is now given from the run (183 s for the notebook)."
assert s.count(a)==1; s=s.replace(a," It also questioned the README's run time, which is now given from the run's own report.")
open(p,'w').write(s)
p='entries/openneuro-ds000228-richardson-2018/README.md'
s=open(p).read()
for a,b in [("""Methods, the inter-region correlations are higher within
networks and less negative across them than the paper reports, and""","""Methods, the adult inter-region correlations are higher within
networks and less negative across them than the paper reports (in the 3-year-olds within-ToM is
higher but within-Pain lower), and"""),
("""It takes about three minutes, most of it
  streaming the 155 preprocessed images (14 GB).""","""`tools/entry.py all` reported 183 s for it on
  2026-10-28; loading the 155 preprocessed images (14 GB) takes most of that.""")]:
    assert s.count(a)==1,a; s=s.replace(a,b)
open(p,'w').write(s)
EOF
grep -n ": " entries/openneuro-ds000228-richardson-2018/README.md | head -3; python tools/entry.py all entries/openneuro-ds000228-richardson-2018 2>&1 | tail -4
```

```
Traceback (most recent call last):
  File "<stdin>", line 4, in <module>
AssertionError
17:A failure to reproduce here may be a failure of this attempt, not of the paper: see the
28:- `reproduce_richardson_2018.ipynb`: the analysis. It takes about three minutes, most of it
30:- `social_brain.py`: loading from the pinned snapshot, ROI extraction, the timecourse cleaning
Installed kernelspec registry-openneuro-ds000228-richardson-2018 in executed/openneuro-ds000228-richardson-2018/.venv/share/jupyter/kernels/registry-openneuro-ds000228-richardson-2018
0 error(s)
pass  reproduce_richardson_2018.ipynb  (146 s)
```

**Agent calls Bash**

```bash
cd  grep -n "README run time" -A2 attempts/openneuro-ds000228-richardson-2018-01.yaml
```

```
(Bash completed with no output)
```

**Agent calls Bash**

```bash
cd  grep -n "reviewed: Round 2" -A6 attempts/openneuro-ds000228-richardson-2018-01.yaml
```

```
810:  reviewed: Round 2. The full executed notebook after the round-1 revision, the helper module, the claims
811-    file and the attempt record, with the paper. Of 42 claims it agreed with 41 outcomes and disagreed
812-    on rc-overlap. It found no misreading in the claims file, so no question was added. The README run
813-    time was also questioned and is now given from the run (183 s for the notebook).
814-  results:
815-  - claim: participants
816-    agrees: true
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "attempts/openneuro-ds000228-richardson-2018-01.yaml",
 "old_string": "so no question was added. The README run\n    time was also questioned and is now given from the run (183 s for the notebook).",
 "new_string": "so no question was added. It also questioned\n    the README's run time, which now gives the times `tools/entry.py all` reported."
}
```

```
The file attempts/openneuro-ds000228-richardson-2018-01.yaml has been updated successfully.
```

**Agent calls Bash**

```bash
cd  python - <<'EOF'
p='entries/openneuro-ds000228-richardson-2018/README.md'
s=open(p).read()
for a,b in [("""Methods, the inter-region correlations are higher within
networks and less negative across them than the paper reports, and""","""Methods, the adult inter-region correlations are higher within
networks and less negative across them than the paper reports (in the 3-year-olds within-ToM is
higher but within-Pain lower), and"""),
("""It takes about three minutes, most of it
  streaming the 155 preprocessed images (14 GB).""","""`tools/entry.py all` reported 146 and 183 s
  for it in two runs on 2026-10-28; loading the 155 preprocessed images (14 GB) takes most of that.""")]:
    assert s.count(a)==1,a; s=s.replace(a,b)
open(p,'w').write(s)
EOF
```

```
(Bash completed with no output)
```

**Agent calls Bash**

```bash
cd  git diff entries/openneuro-ds000228-richardson-2018/README.md; python tools/entry.py check entries/openneuro-ds000228-richardson-2018 2>&1 | tail -5; grep -n "em dash\|—\|rather" -i attempts/openneuro-ds000228-richardson-2018-01.yaml entries/openneuro-ds000228-richardson-2018/README.md | head; git diff attempts | grep "^+" | grep -n "rather\|—"
```

```
diff --git a/entries/openneuro-ds000228-richardson-2018/README.md b/entries/openneuro-ds000228-richardson-2018/README.md
index 01033bd5c..ccd0a3788 100644
--- a/entries/openneuro-ds000228-richardson-2018/README.md
+++ b/entries/openneuro-ds000228-richardson-2018/README.md
@@ -18,15 +18,16 @@ A failure to reproduce here may be a failure of this attempt, not of the paper:
 reasoning and the differences from the paper's method.
 
 Every behavioural number of the paper is recovered from participants.tsv. With the deposited
-preprocessed data and the pipeline of the Methods, the inter-region correlations are higher within
-networks and less negative across them than the paper reports, and several event-level and
+preprocessed data and the pipeline of the Methods, the adult inter-region correlations are higher within
+networks and less negative across them than the paper reports (in the 3-year-olds within-ToM is
+higher but within-Pain lower), and several event-level and
 false-belief results do not come out as reported. Five outcomes rest on readings of a method the
 paper leaves open. The attempt record, with the reasons and the differences from the paper's
 method, is
 [`attempts/openneuro-ds000228-richardson-2018-01.yaml`](../../attempts/openneuro-ds000228-richardson-2018-01.yaml).
 
-- `reproduce_richardson_2018.ipynb`: the analysis. It takes about three minutes, most of it
-  streaming the 155 preprocessed images (14 GB).
[... 6 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python -c "
import json;nb=json.load(open('executed/openneuro-ds000228-richardson-2018/reproduce_richardson_2018.ipynb'))
print('-6.23 under O2a' in ''.join(nb['cells'][55]['source']))
for i in (86,106): print(''.join(nb['cells'][i]['outputs'][0].get('text',''))[:400])
"; git status --short; date -u
```

```
True
                                   events      reading  observed overlap TRs  perms <= observed      p  mean perm overlap
0                    found (all, a p<.05)  (a) 158 TRs                     0                  2  0.002             11.914
1                    found (all, a p<.05)  (b) 159 TRs                     0                  0  0.000             11.945
2                  found (movie, a
                   reading network  b across raw  b across z  t across  p across  b within z  t within  p within
0         O1 all, O2a, O3a     ToM        -0.679      -0.336     -4.52  1.47e-05       0.112      1.53     0.129
1         O1 all, O2a, O3a    Pain        -0.534      -0.284     -3.55  0.000549       0.204       2.4    0.0178
2         O1 all, O2a, O3b     ToM        -0.655      -0.326 
 M attempts/openneuro-ds000228-richardson-2018-01.yaml
 M entries/openneuro-ds000228-richardson-2018/README.md
 M entries/openneuro-ds000228-richardson-2018/reproduce_richardson_2018.ipynb
?? .bash_profile
?? .bashrc
?? .gitconfig
?? .idea
?? .mcp.json
?? .profile
?? .ripgreprc
?? .vscode
[... 4 more lines not kept]
```

**Agent**

I've handled the round-2 report. No outcome changed, and nothing is under `proposed`. I re-ran the entry twice with `tools/entry.py all`; both runs passed with the same numbers as before, and `tools/entry.py check` reports 0 errors.

**Outcomes**
- **rc-overlap (the one disagreement):** I kept partially reproduced and recorded the verifier's not_reproduced. The claim's test holds (less overlap than chance, p ≤ .01); only the expected count misses (0 overlapping timepoints against the paper's 1). Rule S in the claims file and the protocol both call that partial. The verifier's comparison with irc-williams doesn't carry over: there two of the paper's tests fail. This reasoning is now in the result cell and the claim's notes.
- **The other 41:** the verifier agreed, so they stand as they were.

**Text corrected to match the printed numbers**
- **irc-adult-vs-child** (cell 55 and notes): within-ToM t = -6.23 under one reading (O2a with O3b) is inside tolerance. The other within-ToM values, and all within-Pain and across values, are outside.
- **irc-adult notes:** I weakened the shared-signal claim. That variant moves the across-network value in the paper's direction, but it also pushes both within-network values below the paper's.
- **Summary cell:** it no longer says every behavioural number is recovered "exactly". The counts match exactly and the other values are within tolerance, with examples. beh-fb-tom holds only under reading (a).
- **Summary, README and the first finding:** the "higher within networks" statement now applies to adults only. They add that 3-year-old within-Pain is lower than the paper's (.179 against .23; non-bilateral .146 against .17).
- **README run time:** it now gives the times the tool reported, 146 s and 183 s.

**Added**
- **maturity-across:** within-ToM is significant under O2b with O3b (p = .049).
- **rc-3yo-events:** a deviation and the result cell now say that using the best-matching rc-events reading (O5a) extends the criterion.
- **Round-1 record:** for replication-sample, it now says the verifier gave `data_missing`.
- **Round 2 under `verifications`:** one entry per claim, with the verifier's reasons in its words and my responses.

**Not done**
- No question was added to `questions/openneuro-ds000228.yaml`, because the verifier found no misreading in the claims file.
- The unexplained offset in the inter-region correlations and the per-participant artifact check against the ART thresholds stay open. Both are already recorded, and neither can be settled within this attempt.
- Nothing is committed.

## End of run

31 turns, 9 minutes, result: success.
