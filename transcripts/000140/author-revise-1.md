# 000140 · author-revise-1 · run 40797123409

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
date -u; cat transcripts/000140/verifier-1-report.md; ls entries/000140-churchland-2010 entries/000140-churchland-2010/*
```

```
Thu Oct 29 00:57:16 UTC 2026
**A. Outcomes** (20 claims in the claims file)

| Claim | Outcome | Reason |
|---|---|---|
| fig4d-mean-correlation-j-array | not_reproduced | Cell 14: none of the 18 runnable readings has a positive mean at p<0.05. Mean r runs from −0.148 to 0.095, and the main reading gives −0.079 (n=19). Low power (split-half reliability 0.20/0.28, cell 11) means this is a failure to detect, not evidence against. |
| fig4abc-mean-correlation-other-datasets | blocked: data_missing | The archive API shows 1 subject (Jenkins), 2 files and no EMG. None of the A, B or single-electrode J data is there. |
| fig4-broad-near-zero | not_reproduced | Cell 17: every range (O1a) reading fails the IQR ≥ 0.3 test (IQR 0.17–0.29). The only passes are the SD readings, with n = 3–5 units. An IQR near 0.26 is what pure noise gives with 27 conditions. |
| fig4e-correlation-time-course | reproduced (criterion met, but not informative) | Cell 19: 18/30 readings pass, including every O1a reading (r falls from 0.30–0.41 at −200 ms to about 0 at onset). My noise-only simulation passes the same test (problem 1), so the data cannot separate this from shared trial noise. |
| suppfig1-population-averages-lose-tuning | reproduced (criterion met, but not informative) | Cell 21: 36/36 runs pass. Untuned Poisson data also pass: spread 8.3 in the preparatory window, −0.55 at onset, strongest trace on top at −150 ms (problem 1). |
| fig6d-perimovement-best-j-array | partially_reproduced | Cell 23: 64 runs reproduced and 32 partial (initial vel. ≥ peri under O3/O4 a,b / b,a / b,b). The criterion needs every reading to hold. Under O1a every space has negative performance, and the gaps are about 0.005; cell 32 gives peri vs kinematic p=0.62 and peri vs initial vel. p=0.81. |
| fig6abc-perimovement-best-other-datasets | blocked: data_missing | Confirmed on the archive: no single-electrode data, no EMG. |
| fig6-perimovement-best-each-dimensionality | not_reproduced | Cell 26: 0/96 readings
[... 55 more lines not kept]
```

**Agent calls Bash**

```bash
cat docs/protocol.md | sed -n '/^## Author/,$p' | head -400; ls attempts* 2>/dev/null; ls; find . -path ./paper -prune -o -name "*000140*" -print | grep -v transcripts | head
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

[... 511 more lines not kept]
```

**Agent calls Bash**

```bash
cat attempts/000140-churchland-2010-01.yaml; ls questions | grep 140; cat questions/000140.yaml 2>/dev/null | head -50
```

```
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
    model: claude-opus-5-5
    protocol: pilot-12
  runner:
    platform: GitHub Actions
[... 297 more lines not kept]
```

**Agent calls Bash**

```bash
grep -n "verifications" -A40 schemas/*.json | grep -v "^--$" | head -120; grep -l "verifications:" attempts/*.yaml | head -3
```

```
schemas/attempt.schema.json:334:    "verifications": {
schemas/attempt.schema.json-335-      "type": "array",
schemas/attempt.schema.json-336-      "items": {
schemas/attempt.schema.json-337-        "type": "object",
schemas/attempt.schema.json-338-        "additionalProperties": false,
schemas/attempt.schema.json-339-        "required": [
schemas/attempt.schema.json-340-          "date",
schemas/attempt.schema.json-341-          "kind",
schemas/attempt.schema.json-342-          "by",
schemas/attempt.schema.json-343-          "results"
schemas/attempt.schema.json-344-        ],
schemas/attempt.schema.json-345-        "properties": {
schemas/attempt.schema.json-346-          "date": {
schemas/attempt.schema.json-347-            "type": "string",
schemas/attempt.schema.json-348-            "format": "date"
schemas/attempt.schema.json-349-          },
schemas/attempt.schema.json-350-          "kind": {
schemas/attempt.schema.json-351-            "enum": [
schemas/attempt.schema.json-352-              "agent",
schemas/attempt.schema.json-353-              "person",
[... 24 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 374,420p schemas/attempt.schema.json; grep -n "^verifications:" -A30 attempts/000139-churchland-2010-01.yaml | head -50
```

```
"type": "boolean"
                },
                "reason": {
                  "description": "The verifier's reason, in its own words.",
                  "type": "string"
                },
                "response": {
                  "description": "What the author changed or replied, kept apart from the verifier's reason.",
                  "type": "string"
                },
                "outcome": {
                  "description": "The outcome the verifier would give.",
                  "enum": [
                    "reproduced",
                    "partially_reproduced",
                    "not_reproduced",
                    "blocked"
                  ]
                }
              }
[... 58 more lines not kept]
```

**Agent**

Now the notebook structure.

**Agent calls Bash**

```bash
cd entries/000140-churchland-2010; wc -l *.py *.ipynb; python -c "
import json;nb=json.load(open('reproduce_churchland_2010.ipynb'))
for i,c in enumerate(nb['cells']):
    s=''.join(c['source']); print(i,c['cell_type'],c['metadata'].get('tags'),len(s),repr(s[:90]))
"; ls ../../executed/000140-churchland-2010 2>/dev/null
```

```
Exit code 2
   451 maze_prep.py
  1685 reproduce_churchland_2010.ipynb
  2136 total
0 markdown None 2683 '# Churchland et al. (2010) on dandiset 000140 (MC_Maze_Small)\n\nPaper. Churchland MM, Cunni'
1 code None 650 'import os\nos.environ.setdefault("OMP_NUM_THREADS", "1")\nos.environ.setdefault("OPENBLAS_NU'
2 markdown None 85 '## Data check\n\nWhat was loaded, and each check of the description against the values.'
3 code ['sanity'] 4932 'meta = data["meta"]\nprint("subject", meta["subject"], "session start", meta["session_start'
4 markdown None 966 'The positions are stored as numbers in mm with `unit` meters and `conversion` 0.001, which'
5 code None 1912 'rng_clock = np.random.default_rng(0)\n\ndef window_counts(t_ref, w0, w1):\n    X = np.zeros(('
6 markdown None 348 '### Duplicated recordings\n\nThe test file holds 0.7 s segments with movement onset at 250 m'
7 code None 1132 'held = units.index[~units.heldout].values\nassert np.array_equal(units.id.values[held], tes'
8 markdown None 494 '### Shared computations\n\nCondition means under each reading of the open details the claims'
9 code None 2482 't0 = time.time()\nkeep = np.flatnonzero(trials.delay.values > mp.MIN_DELAY_MS)\nconds = tria'
10 markdown None 423 "### Reliability of condition means\n\nThe paper's J-array dataset averaged about 20 trials p"
11 code None 1024 'Rg, Rm = RATES["a"]\nPt = mp.epoch_mean(Rg, GO_L, mp.PREP_WIN)       # trials x units\nMt = '
12 markdown None 1062 '### Readings adopted where readings differ (author, step 1.6)\n\nEvery claim below is run un'
13 markdown None 608 '## fig4d-mean-correlation-j-array\n\n> For the J-array dataset, the correlation across condi'
14 code ['claim:fig4d-mean-correlation-j-array'] 2815 'def fig4_units(cfg, O1, O2):\n    pt = mp.tuning(cfg["P"], O1)\n    qt = mp.peri_tuning(cfg['
15 markdown None 568 '**Result: not reproduced.** Under none of the 18 readings with units is the mean correlati'
[... 53 more lines not kept]
```

**Agent calls Bash**

```bash
ls executed/ 2>/dev/null | head; ls executed 2>/dev/null; cat docs/agents/*revise* 2>/dev/null | head -80; ls docs/agents/
```

```
You are the author of the reproduction attempt `{attempt}` (entry `entries/{entry}`) in the reproduction registry, checked out in the current directory. The verifier has reviewed the changes you proposed after round 2; its round-3 report is `{report}`. Follow docs/protocol.md, step 6.

For each proposed change the verifier agreed with, set the claim's `outcome` (and `blocked_by`) to the proposed one and remove `proposed`. For each it did not agree with, keep the outcome and leave `proposed` with the verifier's view added to its reason. Change nothing else in the outcomes. Update the notebook's conclusions and summary, the entry README and the attempt notes to match, re-run with `python tools/entry.py all entries/{entry}`, and record round 3 under `verifications` with one result for each claim the verifier reviewed: whether it agreed, the outcome it would give, its reason in its own words, and your response. Do not commit or push: the workflow commits your changes.

Write prose plainly: no em dashes, never the word "rather". YAML plain scalars must not contain ": ".

Your final message is a short report of which outcomes changed and which proposals stand.

Run every command in the foreground and wait for it to finish: the run ends when you stop, and anything still running is lost. Before a command that may take long, time it on a subset and estimate the whole (docs/protocol.md, "Develop on a subset").
You are the author of the reproduction attempt `{attempt}` (entry `entries/{entry}`) in the reproduction registry, checked out in the current directory. An independent verifier has reviewed it; its round-{round} report is `{report}`. Follow docs/protocol.md, step 6 ("Hand over for verification") and the rules it refers to.

For each point in the report: fix what it found, or say why not. Add any output it asked for. Where it disagrees with an outcome, either change the outcome and say why, or keep it and record the disagreement. In round 2, no outcome may change: if you
[... 20 more lines not kept]
```

**Agent calls Bash**

```bash
cd  ls transcripts/000140/; grep -o "notebook ran in [0-9.]* min" -r transcripts/000140 | tail -3; grep -o "ran in [0-9.]* s" -r transcripts/000140 | tail -5
```

```
answer-report.md
answer.md
author-answers-report.md
author-answers.md
author-report.md
author.md
claims-check-report.md
claims-check.md
claims-report.md
claims.md
verifier-1-report.md
verifier-1.md
transcripts/000140/author.md:notebook ran in 1.7 min
```

**Agent calls Bash**

```bash
cd  cat transcripts/000140/author-answers-report.md transcripts/000140/answer-report.md; git log --stat -5 | head -60
```

```
There were no questions to act on, so I changed nothing in the notebook, the conclusions, the attempt record or any claim's notes.

**Why there are no questions**
- `questions/000140.yaml` does not exist, and git history shows it never has. The answer run's report (`transcripts/000140/answer-report.md`) says the same and that it made no changes.
- My earlier author run asked readers nothing. Its three open points are method details the paper leaves out: the >5 spikes/s inclusion rule, how the proto-trial was chosen along with how movement onset was detected, and the details of the task spaces. Those are questions for the paper's authors. They are recorded as `methods_unavailable` findings in the attempt, and the protocol sends that kind of question to the authors, not a reader.
- Nothing in `claims/`, `questions/`, `attempts/` or the entry has changed since the author run's commit (72bb5edc7), so no claim needed re-running.

**Outcomes** are unchanged from the earlier run:

| Claim | Earlier outcome | Now |
|---|---|---|
| fig4d-mean-correlation-j-array | not reproduced | unchanged |
| fig4abc-mean-correlation-other-datasets | blocked: data_missing | unchanged |
| fig4-broad-near-zero | partially reproduced (assumed) | unchanged |
| fig4e-correlation-time-course | reproduced (assumed) | unchanged |
| suppfig1-population-averages-lose-tuning | reproduced | unchanged |
| fig6d-perimovement-best-j-array | reproduced (assumed) | unchanged |
| fig6abc-perimovement-best-other-datasets | blocked: data_missing | unchanged |
| fig6-perimovement-best-each-dimensionality | not reproduced | unchanged |
| fig6-maze-endpoint-speed-space-poor | not reproduced (assumed) | unchanged |
[... 87 more lines not kept]
```

**Agent**

Notebook runs in under 2 minutes, so I can iterate. Baseline run first.

**Agent calls Bash**

```bash
cd  time python tools/entry.py all entries/000140-churchland-2010 2>&1 | tail -15
```

```
Installed kernelspec registry-000140-churchland-2010 in executed/000140-churchland-2010/.venv/share/jupyter/kernels/registry-000140-churchland-2010
0 error(s)
pass  reproduce_churchland_2010.ipynb  (115 s)

real	2m32.712s
user	2m22.326s
sys	0m5.491s
```

**Agent**

Now read the helper and the notebook code.

**Agent calls Read**

```json
{
 "file_path": "entries/000140-churchland-2010/maze_prep.py"
}
```

```
1	"""Loading and measures for the maze-task array data of dandiset 000140 (MC_Maze_Small).
2	
3	Churchland, Cunningham, Kaufman, Ryu & Shenoy (2010), Neuron 68:387-400,
4	doi:10.1016/j.neuron.2010.09.015. Claims: claims/000140/10.1016-j.neuron.2010.09.015.yaml.
5	
6	The train file holds 100 trials of monkey J (Jenkins) on 2009-09-28, 27 maze conditions
7	(`maze_id` x `trial_version`), 142 units from two 96-electrode arrays, and hand position and
8	velocity at 1 kHz. The test file holds 100 segments of 0.7 s with no condition, go cue or
9	behaviour, so only the train file is used. Files are streamed; nothing is written to disk.
10	
11	Where the parameters come from (C = the claim's criterion or the claims file header, which
12	cite the paper; P = a passage of the paper taken by the author, step 1.6; A = an assumption;
13	S = a standard choice for a detail that cannot change a result):
14	
15	- Delay > 400 ms (C; Methods, Task design and behavior).
16	- Spike trains smoothed with a 20 ms Gaussian before averaging (C; Supplemental Experimental
17	  Procedures, Computing the mean firing rate versus time). The width is taken as the SD (S).
18	- Preparatory epoch -200 to +100 ms around the go cue; peri-movement epoch -100 to +350 ms
19	  around movement onset (C; Methods, Correlations).
20	- Inclusion > 5 spikes/s of preparatory tuning; peri-movement tuning >= 1.5 times it (C;
[... 432 more lines not kept]
```

**Agent calls Bash**

```bash
cd executed/000140-churchland-2010; ls; python - <<'EOF'
import json
nb=json.load(open('reproduce_churchland_2010.ipynb'))
for i,c in enumerate(nb['cells']):
    if i>12: break
    print(f"===== [{i}] {c['cell_type']} {c['metadata'].get('tags')}")
    print(''.join(c['source']))
    for o in c.get('outputs',[]):
        if 'text' in o: print('--OUT--');print(''.join(o['text'])[:4000])
        elif 'data' in o and 'text/plain' in o['data']: print('--OUT--');print(''.join(o['data']['text/plain'])[:3000])
EOF
```

```
reproduce_churchland_2010.ipynb
result.json
===== [0] markdown None
# Churchland et al. (2010) on dandiset 000140 (MC_Maze_Small)

Paper. Churchland MM, Cunningham JP, Kaufman MT, Ryu SI, Shenoy KV (2010). Cortical preparatory
activity: representation of movement or first cog in a dynamical machine? Neuron 68:387-400,
doi:10.1016/j.neuron.2010.09.015.

Claims. `claims/000140/10.1016-j.neuron.2010.09.015.yaml`, written from the NIH author manuscript
in PubMed Central (PMC2991102) and its supplement (NIHMS240235-supplement-01.pdf), and checked by a
second reader. The claims file decides what is tested; method details it lacks are taken from the
paper and cited where they are used, here and in `maze_prep.py`.

Dataset. DANDI:000140, version 0.220113.0408 (doi:10.48324/dandi.000140/0.220113.0408), streamed.
The paper cites no version of the dandiset. 0.220113.0408 is the only published version; the draft
(modified 2023-06-20) has the same two assets and size. A published version is fixed, so it is pinned.

The dandiset is the Neural Latents Benchmark's MC_Maze_Small: one session of monkey J (Jenkins,
2009-09-28) with two 96-electrode arrays, 100 train/val trials over 27 maze conditions, and 100 test
[... 380 more lines not kept]
```

**Agent calls Bash**

```bash
cd executed/000140-churchland-2010; python - <<'EOF'
import json
nb=json.load(open('reproduce_churchland_2010.ipynb'))
for i,c in enumerate(nb['cells']):
    if i<13 or i>40: continue
    print(f"===== [{i}] {c['cell_type']} {c['metadata'].get('tags')}")
    print(''.join(c['source']))
    for o in c.get('outputs',[]):
        if 'text' in o: print('--OUT--');print(''.join(o['text'])[:5000])
        elif 'data' in o and 'text/plain' in o['data']: print('--OUT--');print(''.join(o['data']['text/plain'])[:3000])
EOF
```

```
<persisted-output>
Output too large (55.4KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/32801633-a32d-4195-a070-6715bbacdcae/tool-results/b9aovm7oc.txt

Preview (first 2KB):
===== [13] markdown None
## fig4d-mean-correlation-j-array

> For the J-array dataset, the correlation across conditions between a unit's preparatory and
> peri-movement firing rates is positive on average but small (mean Pearson r = 0.13, p = 0.03; mean
> Spearman r = 0.11).

Criterion: units with > 5 spikes/s of preparatory tuning and peri-movement tuning at least 1.5 times as
strong, under O1 (range, SD) and O2 (i epoch means, ii largest tuning at any time); O3 and O4 as
above; the mean against zero by (a) one-sample t-test, (b) t-test on Fisher z, (c) Wilcoxon. Expected
mean Pearson 0.13 ± 0.013 and Spearman 0.11 ± 0.011.
===== [14] code ['claim:fig4d-mean-correlation-j-array']
def fig4_units(cfg, O1, O2):
    pt = mp.tuning(cfg["P"], O1)
    qt = mp.peri_tuning(cfg["CMm"], MV_L, cfg["M"], O1, O2)
    return (pt > mp.PREP_TUNING_MIN) & (qt >= mp.PERI_RATIO_MIN * pt)
[... 23 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/32801633-a32d-4195-a070-6715bbacdcae/tool-results/b9aovm7oc.txt"
}
```

```
1	===== [13] markdown None
2	## fig4d-mean-correlation-j-array
3	
4	> For the J-array dataset, the correlation across conditions between a unit's preparatory and
5	> peri-movement firing rates is positive on average but small (mean Pearson r = 0.13, p = 0.03; mean
6	> Spearman r = 0.11).
7	
8	Criterion: units with > 5 spikes/s of preparatory tuning and peri-movement tuning at least 1.5 times as
9	strong, under O1 (range, SD) and O2 (i epoch means, ii largest tuning at any time); O3 and O4 as
10	above; the mean against zero by (a) one-sample t-test, (b) t-test on Fisher z, (c) Wilcoxon. Expected
11	mean Pearson 0.13 ± 0.013 and Spearman 0.11 ± 0.011.
12	===== [14] code ['claim:fig4d-mean-correlation-j-array']
13	def fig4_units(cfg, O1, O2):
14	    pt = mp.tuning(cfg["P"], O1)
15	    qt = mp.peri_tuning(cfg["CMm"], MV_L, cfg["M"], O1, O2)
16	    return (pt > mp.PREP_TUNING_MIN) & (qt >= mp.PERI_RATIO_MIN * pt)
17	
18	def fig4_corrs(cfg, sel):
19	    r = mp.rowwise_corr(cfg["P"][:, sel], cfg["M"][:, sel])
20	    rs = np.array([stats.spearmanr(cfg["P"][:, j], cfg["M"][:, j])[0] for j in np.flatnonzero(sel)])
[... 794 more lines not kept]
```

**Agent calls Bash**

```bash
cd executed/000140-churchland-2010; python - <<'EOF'
import json
nb=json.load(open('reproduce_churchland_2010.ipynb'))
for i,c in enumerate(nb['cells']):
    if i<41: continue
    print(f"===== [{i}] {c['cell_type']} {c['metadata'].get('tags')}")
    print(''.join(c['source']))
    for o in c.get('outputs',[]):
        if 'text' in o: print('--OUT--');print(''.join(o['text'])[:3500])
        elif 'data' in o and 'text/plain' in o['data']: print('--OUT--');print(''.join(o['data']['text/plain'])[:2000])
EOF
```

```
<persisted-output>
Output too large (30.4KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/32801633-a32d-4195-a070-6715bbacdcae/tool-results/bjcbkr0tj.txt

Preview (first 2KB):
===== [41] markdown None
## prep-dimensionality-7-to-10

> Preparatory activity is moderately high dimensional; depending on the dataset 7 to 10 dimensions
> capture 90% of its variance.

Criterion: PCA of the c x n matrix of condition-mean preparatory rates of the fig6d units; the number
of components reaching 90% of the variance; expected 8.65 ± 2.35 (6.3 to 11). Unnormalised main,
z-scored variant; bounded by c - 1 = 26.
===== [42] code ['claim:prep-dimensionality-7-to-10']
rows = []
for key, cfg in CONFIGS.items():
    for O1 in ("range", "sd"):
        sel = mp.tuning(cfg["P"], O1) > mp.PREP_TUNING_MIN
        Psel = cfg["P"][:, sel]
        n90, ev = mp.n_components_for(Psel)
[... 24 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/32801633-a32d-4195-a070-6715bbacdcae/tool-results/bjcbkr0tj.txt",
 "offset": 30
}
```

```
30	    null_n.append(mp.n_components_for(mp.condition_means(Pt_k, perm, C)[:, sel])[0])
31	print("same count with condition labels shuffled across trials (50 shuffles): median %d, range %d to %d"
32	      % (np.median(null_n), min(null_n), max(null_n)))
33	--OUT--
34	O3 O4    O1  n units  PCs for 90%  z-scored  PC1 share  within 6.3-11
35	 a  a range       93           16        18      0.195          False
36	 a  a    sd        8            6         6      0.349          False
37	 a  b range       91           16        18      0.209          False
38	 a  b    sd        8            5         6      0.363          False
39	 a  c range       91           16        18      0.222          False
40	 a  c    sd        7            5         5      0.405          False
41	 b  a range       93           17        18      0.194          False
42	 b  a    sd        8            6         6      0.347          False
43	 b  b range       91           16        18      0.214          False
44	 b  b    sd        8            5         6      0.367          False
45	 b  c range       91           16        18      0.222          False
46	 b  c    sd        7            5         5      0.405          False
47	same count with condition labels shuffled across trials (50 shuffles): median 17, range 16 to 17
48	
49	===== [43] markdown None
[... 445 more lines not kept]
```

**Agent**

Now the claims file for the disputed claims.

**Agent calls Bash**

```bash
cd  ls claims/000140; f=$(ls claims/000140/*.yaml | head -1); sed -n 1,80p $f; grep -n "id: \(fig4e\|suppfig1\|fig6d\|fig7c\|prep-activity\|fig7d\|fig4-broad\|fig7b\)" -A40 $f | grep -n "criterion\|reproduced\|partial\|id:" | head -60
```

```
10.1016-j.neuron.2010.09.015.yaml
# Claims for Churchland, Cunningham, Kaufman, Ryu & Shenoy (2010), Neuron 68, 387-400, on dandiset 000140.
# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"), 2026-10-28,
# protocol as stated in docs/protocol.md.
#
# Text read: the NIH author manuscript in PubMed Central (PMC2991102), not the version of record,
# as extracted to paper/10.1016-j.neuron.2010.09.015.txt: Summary, Results, Discussion, Methods,
# figure legends, and its one supplement (NIHMS240235-supplement-01.pdf: Supplemental Figures 1
# to 5 with legends, Supplemental Text, Supplemental Experimental Procedures). The figures are not
# in the text; values shown only in Figures 4, 6 and 7 are not stated and no expected value is
# taken from them. The paper links no code, so every method below comes from the Methods, the
# legends or the supplement. The archive also lists doi:10.1038/nature11129 for this dandiset;
# these claims are for the 2010 paper only.
#
# Data the paper used (Results, Behavior and recordings; Methods; Supplemental Experimental
# Procedures). Three adult male rhesus monkeys (A, B, J, about 10 kg) made delayed reaches on a
# fronto-parallel screen from a central touch spot to a target. Events per trial: target onset
# (the target jitters), go cue (jitter stops, touch spot disappears), movement onset. Delays about
# 0 to 1000 ms; only trials with delays above 400 ms analysed. Hand tracked at 60 Hz, eye at
# 240 Hz. Four datasets:
[... 93 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 142,230p claims/000140/*.yaml; sed -n 395,440p claims/000140/*.yaml
```

```
- id: fig4-broad-near-zero
  statement: Correlations between preparatory and peri-movement tuning span a broad range centred
    near zero, with no separate populations of concordant (r near 1) and opposing (r near -1)
    tuning; most neurons have weakly correlated tuning.
  source: Results, Correlations between preparatory and peri-movement tuning, paragraphs 3 and 4;
    Figure 4A to 4D
  quote: different neurons show markedly different relationships between preparatory and
    peri-movement activity, with a broad range of correlations centered near zero ... Instead, most
    neurons have weakly correlated tuning
  depends_on:
  - fig4d-mean-correlation-j-array
  criterion: The paper gives no test; the judgement rule is fixed here. On the J-array units and
    correlations of fig4d-mean-correlation-j-array, reproduced when the median r lies between
    -0.3 and 0.3, the interquartile range spans at least 0.3, more than half of units have |r|
    below 0.5 (most weakly correlated), and fewer than 15% of units have r above 0.8 and fewer
    than 15% below -0.8 (no cluster at either end). The histogram is shown in
    bins of 0.1, a standard choice.
- id: fig4e-correlation-time-course
  statement: When peri-movement activity is taken at single time points, its correlation with
    preparatory tuning starts to fall about 200 ms before movement onset and is near zero by
[... 115 more lines not kept]
```

**Agent calls Bash**

```bash
date -u; cd  ls executed/000140-churchland-2010/.venv/bin/python; python - <<'EOF'
import json
nb=json.load(open('entries/000140-churchland-2010/reproduce_churchland_2010.ipynb'))
src=[]
for i in [1,3,5,7,9,11,14,18,21,24,27]:
    s=''.join(nb['cells'][i]['source']).replace('plt.show()','plt.close("all")')
    src.append(f"# ---- cell {i}\n"+s)
open('/tmp/claude/prefix.py','w').write('\n'.join(src)) if False else None
import os
d=os.environ.get('TMPDIR','/tmp/claude'); os.makedirs(d,exist_ok=True)
open(os.path.join(d,'prefix.py'),'w').write("import matplotlib; matplotlib.use('Agg')\nimport sys; sys.path.insert(0,'entries/000140-churchland-2010')\n"+'\n'.join(src))
print(d)
EOF
```

```
Thu Oct 29 01:01:32 UTC 2026
executed/000140-churchland-2010/.venv/bin/python
/tmp/claude-1001
```

**Agent calls Bash**

```bash
cd  cat >> $TMPDIR/prefix.py <<'EOF'

import pickle
state = {k: globals()[k] for k in ["data","test","trials","units","beh","keep","conds","C","GO_L","MV_L","onsets","RATES","KINS","TSEL","CONFIGS","MAIN","Pt","Mt","PERF","dims","KMAX"]}
pickle.dump(state, open(os.environ["TMPDIR"] + "/state.pkl", "wb"))
EOF
time executed/000140-churchland-2010/.venv/bin/python $TMPDIR/prefix.py > $TMPDIR/prefix.out 2>&1; tail -3 $TMPDIR/prefix.out; ls -la $TMPDIR/state.pkl
```

```
real	0m25.199s
user	0m22.695s
sys	0m0.611s
units with peri performance > 0 at their best k <= 14: 47 of 93
O1 SD units (n = 8): peri best 0.209, kin best 0.136, upper best 0.123
points below the axis (< -1.5): 26 of 68; plotted values range -44.32 to -0.04
-rw-r--r-- 1 runner runner 363017169 Oct 29 01:02 /tmp/claude-1001/state.pkl
```

**Agent calls Bash**

```bash
cd  cat > $TMPDIR/noise.py <<'EOF'
import os, sys, pickle, time
sys.path.insert(0,'entries/000140-churchland-2010')
import numpy as np, pandas as pd
from scipy import stats
import maze_prep as mp
globals().update(pickle.load(open(os.environ["TMPDIR"]+"/state.pkl","rb")))
pd.set_option("display.width", 250); pd.set_option("display.max_columns", 40)
exec(open(os.environ["TMPDIR"]+"/funcs.py").read())
t0=time.time()
EOF
cat > $TMPDIR/funcs.py <<'EOF'
def fig4_units(cfg, O1, O2):
    pt = mp.tuning(cfg["P"], O1)
    qt = mp.peri_tuning(cfg["CMm"], MV_L, cfg["M"], O1, O2)
    return (pt > mp.PREP_TUNING_MIN) & (qt >= mp.PERI_RATIO_MIN * pt)
def fig4_corrs(cfg, sel):
    r = mp.rowwise_corr(cfg["P"][:, sel], cfg["M"][:, sel])
    rs = np.array([stats.spearmanr(cfg["P"][:, j], cfg["M"][:, j])[0] for j in np.flatnonzero(sel)])
    return r, rs
LAGS_MV = np.arange(-400, 401, 10)
LAGS_GO = np.arange(-200, 201, 10)
def time_course(cfg, sel):
    P = cfg["P"][:, sel]
    mv = np.array([np.nanmean(mp.rowwise_corr(P, cfg["CMm"][:, sel, np.flatnonzero(MV_L == t)[0]])) for t in LAGS_MV])
    go = np.array([np.nanmean(mp.rowwise_corr(P, cfg["CMg"][:, sel, np.flatnonzero(GO_L == t)[0]])) for t in LAGS_GO])
    return go, mv
def judge_tc(mv):
    at0 = mv[LAGS_MV == 0][0]; at200 = mv[LAGS_MV == -200][0]
    drops = mv[:-5] - mv[5:]
    start = LAGS_MV[:-5][np.argmax(drops)]
    return {"r at -200": at200, "r at 0": at0, "largest 50 ms drop starts": start,
            "pass": at0 < 0.1 and at0 < 0.5 * at200 and -300 <= start <= 0,
            "partial": at0 >= 0.1 and at0 < at200}
def pop_avg(cfg, sel, normalise=True):
    P = cfg["P"][:, sel]
    order = np.argsort(P, axis=0)
    ranks = [order[-1], order[int(round((C - 1) * 2 / 3))], order[int(round((C - 1) / 3))], order[0]]
    idx = np.flatnonzero(sel)
    go_tr, mv_tr = [], []
    for rk in ranks:
        g = np.stack([cfg["CMg"][c, u] for c, u in zip(rk, idx)])
        m = np.stack([cfg["CMm"][c, u] for c, u in zip(rk, idx)])
        if normalise:
            mx = np.maximum(cfg["CMg"][:, idx].max((0, 2)), cfg["CMm"][:, idx].max((0, 2)))
            g, m = g / mx[:, None], m / mx[:, None]
        go_tr.append(g.mean(0)); mv_tr.append(m.mean(0))
    return np.array(go_tr), np.array(mv_tr)
def judge_pop(go_tr, mv_tr):
    prep = (GO_L >= mp.PREP_WIN[0]) & (GO_L <= mp.PREP_WIN[1])
    spread_prep = (go_tr[0] - go_tr[3])[prep].mean()
    spread_0 = (mv_tr[0] - mv_tr[3])[MV_L == 0][0]
    top150 = mv_tr[:, MV_L == -150][:, 0]
    return {"spread prep": spread_prep, "spread at onset": spread_0, "ratio": spread_0 / spread_prep,
            "strongest on top at -150": bool(np.argmax(top150) == 0),
            "pass": spread_0 < 0.5 * spread_prep and np.argmax(top150) == 0}
EOF
cat >> $TMPDIR/noise.py <<'EOF'
# ---------- new code
def means_from(o, idx_prep, lab_prep, idx_peri, lab_peri):
    """Condition means with the preparatory (go-locked) and movement-locked means taken from
    given trials (positions in `keep`) and condition labels."""
    Rg, Rm = RATES[o]
    cfg = {"CMg": mp.condition_means(Rg[idx_prep], lab_prep, C), "CMm": mp.condition_means(Rm[idx_peri], lab_peri, C)}
    cfg["P"] = mp.epoch_mean(cfg["CMg"], GO_L, mp.PREP_WIN)
    cfg["M"] = mp.epoch_mean(cfg["CMm"], MV_L, mp.PERI_WIN)
    return cfg

def noise_row(cfg, sel_fixed=None):
    sel = fig4_units(cfg, "range", "i") if sel_fixed is None else sel_fixed
    selb = mp.tuning(cfg["P"], "range") > mp.PREP_TUNING_MIN
    r, _ = fig4_corrs(cfg, sel)
    _, mv = time_course(cfg, sel); _, mvb = time_course(cfg, selb)
    ja, jb = judge_tc(mv), judge_tc(mvb)
    pa = judge_pop(*pop_avg(cfg, sel, True))
    return {"n prep>5": int(selb.sum()), "n fig4": int(sel.sum()), "mean r": np.nanmean(r),
            "tc(a) r-200": ja["r at -200"], "tc(a) r0": ja["r at 0"], "tc(a) drop": ja["largest 50 ms drop starts"], "tc(a) pass": ja["pass"],
            "tc(b) r-200": jb["r at -200"], "tc(b) r0": jb["r at 0"], "tc(b) pass": jb["pass"],
            "pop ratio": pa["ratio"], "pop top": pa["strongest on top at -150"], "pop pass": pa["pass"]}

rng_null = np.random.default_rng(7)
rows = []
for key in [MAIN]:
    kp = np.flatnonzero(CONFIGS[key]["kept"]); lab = conds[kp]
    rows.append({"set": "data", **noise_row(CONFIGS[key])})
    for s in range(20):
        perm = rng_null.permutation(lab)
        rows.append({"set": f"shuffle {s}", **noise_row(means_from(key[0], kp, perm, kp, perm))})
null_tab = pd.DataFrame(rows)
print(null_tab.round(3).to_string(index=False))
print(time.time()-t0)
EOF
executed/000140-churchland-2010/.venv/bin/python $TMPDIR/noise.py 2>&1 | grep -v Warn | grep -v "return (a"
```

```
set  n prep>5  n fig4  mean r  tc(a) r-200  tc(a) r0  tc(a) drop  tc(a) pass  tc(b) r-200  tc(b) r0  tc(b) pass  pop ratio  pop top  pop pass
      data        93      19  -0.079        0.295    -0.078        -250        True        0.388    -0.001        True      0.186     True      True
 shuffle 0        92      10   0.026        0.188    -0.062        -250        True        0.334    -0.028        True      0.393    False     False
 shuffle 1        95      13  -0.002        0.319    -0.123         120       False        0.280     0.001        True     -0.355     True      True
 shuffle 2        82       9  -0.081        0.214    -0.009        -130        True        0.314    -0.001        True      0.193     True      True
 shuffle 3        89      13   0.038        0.208    -0.003        -280        True        0.301    -0.023        True      0.323    False     False
 shuffle 4        92      13   0.013        0.308    -0.021        -190        True        0.328     0.015        True      0.264     True      True
 shuffle 5        87      15  -0.060        0.196    -0.008        -230        True        0.340     0.000        True     -0.396    False     False
 shuffle 6        90      15  -0.024        0.273     0.053        -280        True        0.332     0.009        True      0.146     True      True
 shuffle 7        87      13   0.019        0.206    -0.062        -250        True        0.292     0.004        True      0.207    False     False
 shuffle 8        96      11   0.000        0.201    -0.102        -240        True        0.308    -0.015        True     -0.753     True      True
 shuffle 9        90      13   0.012        0.317     0.012        -230        True        0.369    -0.003        True      0.014     True      True
shuffle 10        86      19  -0.005        0.258    -0.001        -240        True        0.367     0.006        True      0.048    False     False
shuffle 11        88      13   0.008        0.228    -0.015        -26
[... 9 more lines not kept]
```

**Agent**

Striking: with condition labels shuffled, ~90 units still pass the O1a selection (93 in the data), and fig4e passes in 18–20 of 20 shuffles. Now the disjoint-trial variant.

**Agent calls Bash**

```bash
cd  cat > $TMPDIR/disj.py <<'EOF'
exec(open(os.environ["TMPDIR"]+"/noise_head.py").read()) if False else None
EOF
head -9 $TMPDIR/noise.py > $TMPDIR/head.py
sed -n '/^def means_from/,/^rng_null/p' $TMPDIR/noise.py | head -n -1 >> $TMPDIR/head.py
cat $TMPDIR/head.py > $TMPDIR/disj.py
cat >> $TMPDIR/disj.py <<'EOF'
def split_halves(kp):
    """Positions (in keep) of two disjoint trial sets: within each condition with >= 2 trials,
    alternate trials go to A and B; single-trial conditions are dropped."""
    A, B = [], []
    for c in range(C):
        idx = kp[conds[kp] == c]
        if len(idx) < 2: continue
        A += list(idx[0::2]); B += list(idx[1::2])
    return np.array(A), np.array(B)
rows=[]
for key in CONFIGS:
    kp = np.flatnonzero(CONFIGS[key]["kept"])
    A, B = split_halves(kp)
    for nm, (X, Y) in {"prep A, peri B": (A, B), "prep B, peri A": (B, A)}.items():
        cfg = means_from(key[0], X, conds[X], Y, conds[Y])
        # conditions present in both halves
        present = np.isfinite(cfg["P"][:, 0]) & np.isfinite(cfg["M"][:, 0])
        cfg = {k: v[present] for k, v in cfg.items()}
        sel_full = fig4_units(CONFIGS[key], "range", "i")
        Cn = present.sum()
        globals()["C"] = Cn
        row = noise_row(cfg, sel_fixed=sel_full)
        globals()["C"] = 27
        rows.append({"O3":key[0],"O4":key[1],"split":nm,"conditions":int(Cn),"trials":(len(X),len(Y)), **row})
print(pd.DataFrame(rows).round(3).to_string(index=False))
EOF
executed/000140-churchland-2010/.venv/bin/python $TMPDIR/disj.py 2>&1 | grep -v Warn | grep -v "return (a"
```

```
return np.stack([X[conds == c].mean(0) for c in range(n_cond)])
  ret = um.true_divide(
O3 O4          split  conditions   trials  n prep>5  n fig4  mean r  tc(a) r-200  tc(a) r0  tc(a) drop  tc(a) pass  tc(b) r-200  tc(b) r0  tc(b) pass  pop ratio  pop top  pop pass
 a  a prep A, peri B          23 (35, 27)       102      19  -0.090        0.134    -0.003         180       False        0.171     0.030        True      0.282    False     False
 a  a prep B, peri A          23 (27, 35)       100      19  -0.048        0.090    -0.077        -360       False        0.137    -0.021       False     -0.176    False     False
 a  b prep A, peri B          24 (38, 30)       100      13  -0.100        0.100    -0.032         200       False        0.177     0.024        True      0.208    False     False
 a  b prep B, peri A          24 (30, 38)       102      13  -0.118        0.106    -0.049         -60        True        0.146    -0.008        True     -0.434    False     False
 a  c prep A, peri B          25 (44, 32)        99      15   0.025        0.115     0.045         250       False        0.184     0.024        True      0.017    False     False
 a  c prep B, peri A          25 (32, 44)       104      15  -0.153        0.140    -0.104        -200        True        0.161     0.009       False     -0.610    False     False
 b  a prep A, peri B          23 (34, 28)       100      18  -0.049        0.043     0.029         210       False        0.126     0.017        True      0.325    False     False
 b  a prep B, peri A          23 (28, 34)        98      18  -0.062        0.134    -0.095          90       False        0.122    -0.019       False     -0.306     True      True
 b  b prep A, peri B          24 (40, 30)        99      15   0.036        0.022     0.052         210       False        0.128     0.013        True      0.327     True      True
 b  b prep B, peri A          24 (30, 40)       104      15  -0.128        0.145    -0.090        -200        Tr
[... 2 more lines not kept]
```

**Agent**

Disjoint trials weaken the fig4e and suppfig1 signals a lot. Next: fig6d with per-unit paired tests, the included-units T-matrix variant, and a shuffled-label null.

**Agent calls Bash**

```bash
cd  cp $TMPDIR/head.py $TMPDIR/f6.py; cat >> $TMPDIR/f6.py <<'EOF'
def perf_matrix(P, spaces_per_unit, idx, kmax=KMAX):
    return np.array([mp.loo_performance_curve(P[:, j], spaces_per_unit[j], kmax) for j in idx])
t0=time.time()
# per-reading paired tests: per unit, peri at the population-best k against the best other space at its best k
rows=[]
for key in CONFIGS:
    res=PERF[key]; cfg=CONFIGS[key]
    for O1 in ("range","sd"):
        sel = mp.tuning(cfg["P"], O1) > mp.PREP_TUNING_MIN
        for kmax in (14,20):
          for end in (600,800):
            for seg in ("length","time"):
                peri = res["peri"][sel,:kmax]; kb=np.argmax(np.nanmean(peri,0)); pu=peri[:,kb]
                others={"kinematic": res[f"kin{end}"][sel,:kmax][:, np.argmax(np.nanmean(res[f"kin{end}"][sel,:kmax],0))]}
                for name in mp.TASK_SPACES: others[name]=res[f"{seg}:{name}"][sel]
                bo=max(others,key=lambda k: np.nanmean(others[k])); ou=others[bo]
                d=pu-ou
                rows.append({"O3":key[0],"O4":key[1],"O1":O1,"kmax":kmax,"end":end,"seg":seg,"peri":np.nanmean(pu),"SE":np.nanstd(pu)/np.sqrt(len(pu)),
                             "best other":bo,"other":np.nanmean(ou),"diff":np.nanmean(d),"SE diff":np.nanstd(d)/np.sqrt(len(d)),"p paired t":stats.ttest_rel(pu,ou,nan_policy="omit").pvalue})
t=pd.DataFrame(rows)
print(t.drop_duplicates(subset=["O3","O4","O1","best other","peri","other"]).round(3).to_string(index=False))
print("p<0.05 with peri higher:", int(((t["p paired t"]<0.05)&(t["diff"]>0)).sum()), "of", len(t))
# included-units T matrix
rows=[]
for key in CONFIGS:
    cfg=CONFIGS[key]
    for O1 in ("range","sd"):
        sel = mp.tuning(cfg["P"], O1) > mp.PREP_TUNING_MIN
        sc = mp.leave_one_out_scores(cfg["CMm"][:, :, TSEL], KMAX, members=sel)
        pm = np.nanmean(perf_matrix(cfg["P"], sc, np.flatnonzero(sel)),0)
        allu = np.nanmean(PERF[key]["peri"][sel],0)
        kin = np.nanmean(PERF[key]["kin800"][sel],0).max()
        tasks = max(np.nanmean(PERF[key][f"length:{n}"][sel]) for n in mp.TASK_SPACES)
        rows.append({"O3":key[0],"O4":key[1],"O1":O1,"n":int(sel.sum()),"peri best, all units":allu.max(),"peri best, included units":pm.max(),"k":int(np.argmax(pm)+1),"kin best":kin,"task best":tasks})
print(pd.DataFrame(rows).round(3).to_string(index=False))
print(time.time()-t0)
# null
rng_null=np.random.default_rng(8)
key=MAIN; kp=np.flatnonzero(CONFIGS[key]["kept"]); lab=conds[kp]
ks = mp.pca_scores(mp.kinematic_matrix(CONFIGS[key]["KIN"], 800), KMAX)
rows=[]
for s in range(10):
    perm=rng_null.permutation(lab)
    cfg=means_from(key[0],kp,perm,kp,perm)
    sel = mp.tuning(cfg["P"], "range") > mp.PREP_TUNING_MIN
    sc=mp.leave_one_out_scores(cfg["CMm"][:, :, TSEL], 14)
    pm=np.nanmean(perf_matrix(cfg["P"], sc, np.flatnonzero(sel),14),0)
    km=np.nanmean(perf_matrix(cfg["P"], [ks]*142, np.flatnonzero(sel),14),0)
    iv=np.nanmean([mp.loo_performance(cfg["P"][:,j], CONFIGS[key]["TS_length"]["initial vel."]) for j in np.flatnonzero(sel)])
    rows.append({"n":int(sel.sum()),"peri best":pm.max(),"k":int(np.argmax(pm)+1),"kin best":km.max(),"init vel":iv})
print(pd.DataFrame(rows).round(3).to_string(index=False))
print(time.time()-t0)
EOF
executed/000140-churchland-2010/.venv/bin/python $TMPDIR/f6.py 2>&1 | grep -v Warn | grep -v "return (a\|return 1.0\|np.stack"
```

```
O3 O4    O1  kmax  end    seg   peri    SE   best other  other   diff  SE diff  p paired t
 a  a range    14  600 length -0.044 0.021 initial vel. -0.048  0.004    0.018       0.813
 a  a    sd    14  600 length  0.209 0.097    kinematic  0.138  0.072    0.125       0.608
 a  a    sd    14  800 length  0.209 0.097    kinematic  0.136  0.073    0.124       0.596
 a  b range    14  600 length -0.045 0.022 initial vel. -0.041 -0.004    0.018       0.815
 a  b    sd    14  600 length  0.202 0.091    kinematic  0.135  0.068    0.147       0.680
 a  b    sd    14  800 length  0.202 0.091    kinematic  0.133  0.070    0.146       0.669
 a  c range    14  600 length -0.023 0.022 initial vel. -0.036  0.013    0.018       0.492
 a  c    sd    14  600 length  0.247 0.053 kitchen sink  0.228  0.018    0.079       0.836
 a  c    sd    14  600   time  0.247 0.053 kitchen sink  0.186  0.060    0.110       0.628
 b  a range    14  600 length -0.046 0.021 initial vel. -0.042 -0.004    0.018       0.820
 b  a    sd    14  600 length  0.140 0.132    kinematic  0.135  0.005    0.123       0.968
 b  a    sd    14  800 length  0.140 0.132    kinematic  0.133  0.007    0.123       0.958
 b  b range    14  600 length -0.043 0.023 initial vel. -0.033 -0.010    0.018       0.572
 b  b    sd    14  600 length  0.129 0.125    kinematic  0.134 -0.005    0.104       0.965
 b  b    sd    14  800 length  0.129 0.125    kinematic  0.132 -0.003    0.103       0.982
 b  c range    14  600 length -0.026 0.022 initial vel. -0.029  0.003    0.018       0.885
 b  c    sd    14  600 length  0.249 0.058 kitchen sink  0.217  0.032    0.078       0.720
 b  c    sd    14  600   time  0.249 0.058    kinematic  0.187  0.062    0.081       0.504
 b  c    sd    14  800   time  0.249 0.058    kinematic  0.183  0.066    0.079       0.470
[... 27 more lines not kept]
```

**Agent**

Under O1b, building the peri space only from included units removes the peri-space advantage. I need to check which reading the paper supports.

**Agent calls Bash**

```bash
cd  ls paper; grep -n -i "inclusion criterion\|5 spikes/s\|all neurons except\|isolations\|robust peri-movement" paper/*.txt | head -20
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  grep -o -i ".\{400\}5 spikes/s.\{300\}" paper/10.1016-j.neuron.2010.09.015.txt | head -3; echo ====; grep -o -i ".\{300\}all neurons except.\{200\}" paper/10.1016-j.neuron.2010.09.015.txt | head -3
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  grep -o -i ".\{1500\}We thus used a lower inclusion criterion" paper/10.1016-j.neuron.2010.09.015.txt | head -c 1600; echo; grep -o -i "146.\{300\}" paper/10.1016-j.neuron.2010.09.015.txt | head -3
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  cp $TMPDIR/head.py $TMPDIR/f7d.py; cat >> $TMPDIR/f7d.py <<'EOF'
rng_pd = np.random.default_rng(5)
t0=time.time()
rows = []
for key in CONFIGS:
    cfg = CONFIGS[key]; P = cfg["P"]
    ks_kin = mp.pca_scores(mp.kinematic_matrix(cfg["KIN"], 800), KMAX)
    for O1 in ("range","sd"):
        sel = np.flatnonzero(mp.tuning(P, O1) > mp.PREP_TUNING_MIN)
        kin_k = int(np.argmax(np.nanmean(PERF[key]["kin800"][sel, :14], 0)) + 1)
        comps = {"endpoints + max. spd.": cfg["TS_length"]["endpoints + max. spd."],
                 "segment dirs.": cfg["TS_length"]["segment dirs."], "kinematic": ks_kin[:, :kin_k]}
        for name, S in comps.items():
            k = S.shape[1]
            for zs in (False, True):
                c_other = np.nanmean([mp.pd_consistency(P[:, j], S, rng_pd, standardize=zs) for j in sel])
                c_peri = np.nanmean([mp.pd_consistency(P[:, j], PERF[key]["peri_scores"][j][:, :k], rng_pd, standardize=zs) for j in sel])
                rows.append({"O3": key[0], "O4": key[1], "O1":O1, "space": name, "k": k, "z": zs, "n": len(sel),
                             "other": c_other, "peri": c_peri, "peri higher": c_peri > c_other})
    print(key, time.time()-t0, flush=True)
t=pd.DataFrame(rows); print(t.round(3).to_string(index=False))
print(t.groupby(["O1","space"])["peri higher"].agg(["sum","count"]))
EOF
executed/000140-churchland-2010/.venv/bin/python $TMPDIR/f7d.py 2>&1 | grep -v Warn | grep -v "return (a\|return 1.0\|np.stack"
```

```
('a', 'a') 18.33882212638855
('a', 'b') 36.24901556968689
('a', 'c') 54.0543315410614
('b', 'a') 72.34670305252075
('b', 'b') 90.26545596122742
('b', 'c') 107.9965968132019
O3 O4    O1                 space  k     z  n  other  peri  peri higher
 a  a range endpoints + max. spd.  3 False 93  0.523 0.617         True
 a  a range endpoints + max. spd.  3  True 93  0.531 0.630         True
 a  a range         segment dirs.  6 False 93  0.525 0.416        False
 a  a range         segment dirs.  6  True 93  0.527 0.449        False
 a  a range             kinematic  1 False 93  0.563 0.587         True
 a  a range             kinematic  1  True 93  0.548 0.591         True
 a  a    sd endpoints + max. spd.  3 False  8  0.576 0.780         True
 a  a    sd endpoints + max. spd.  3  True  8  0.631 0.776         True
 a  a    sd         segment dirs.  6 False  8  0.615 0.545        False
 a  a    sd         segment dirs.  6  True  8  0.629 0.607        False
 a  a    sd             kinematic  3 False  8  0.672 0.765         True
 a  a    sd             kinematic  3  True  8  0.740 0.784         True
 a  b range endpoints + max. spd.  3 False 91  0.525 0.617         True
[... 67 more lines not kept]
```

**Agent**

fig7d over all 6 settings and both O1 readings takes 108 s and leaves the outcome unchanged. Now I'll write the notebook edits.

**Agent calls Bash**

```bash
cd  python - <<'EOF'
import json
nb=json.load(open('entries/000140-churchland-2010/reproduce_churchland_2010.ipynb'))
for i in [0,12,21,24,50,52,56,59,64,65,67]:
    print(f"===== [{i}]"); print(''.join(nb['cells'][i]['source']))
print(nb['cells'][14]['metadata'], nb['cells'][14].keys())
EOF
```

```
===== [0]
# Churchland et al. (2010) on dandiset 000140 (MC_Maze_Small)

Paper. Churchland MM, Cunningham JP, Kaufman MT, Ryu SI, Shenoy KV (2010). Cortical preparatory
activity: representation of movement or first cog in a dynamical machine? Neuron 68:387-400,
doi:10.1016/j.neuron.2010.09.015.

Claims. `claims/000140/10.1016-j.neuron.2010.09.015.yaml`, written from the NIH author manuscript
in PubMed Central (PMC2991102) and its supplement (NIHMS240235-supplement-01.pdf), and checked by a
second reader. The claims file decides what is tested; method details it lacks are taken from the
paper and cited where they are used, here and in `maze_prep.py`.

Dataset. DANDI:000140, version 0.220113.0408 (doi:10.48324/dandi.000140/0.220113.0408), streamed.
The paper cites no version of the dandiset. 0.220113.0408 is the only published version; the draft
(modified 2023-06-20) has the same two assets and size. A published version is fixed, so it is pinned.

The dandiset is the Neural Latents Benchmark's MC_Maze_Small: one session of monkey J (Jenkins,
2009-09-28) with two 96-electrode arrays, 100 train/val trials over 27 maze conditions, and 100 test
segments without conditions. The paper's J-array dataset has 108 conditions and 2166 trials per
neuron; the dandiset holds 27 of its conditions (or of a session like it) with 1 to 4 analysable
[... 301 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat > $TMPDIR/cells.py <<'PYEOF'
NOISE_MD = """### Noise reference for fig4d, fig4-broad-near-zero, fig4e and suppfig1

With 1 to 4 trials per condition, the preparatory and peri-movement means of a condition share the
noise of the same few trials, and the preparatory window ends 100 ms after the go cue, about 220 ms
before movement onset (median reaction time 321 ms). Two references are computed on the main reading
(O3a, O4a, O1a):

- **condition-shuffled null**: the condition labels of the kept trials are permuted (counts kept), and
  the whole pipeline (selection, correlations, time course, population averages) is run on the
  shuffled means, 20 times. There is no tuning in these data, only trial noise.
- **disjoint trials**: within each condition with at least two kept trials, alternate trials go to two
  sets; the preparatory means come from one set and the movement-locked means from the other, both
  ways. Single-trial conditions are dropped. Units are those of fig4d on all trials. Shared trial noise
  cannot correlate the two means here.

The time-course and population-average functions used by fig4e and suppfig1 are defined here."""

NOISE_CODE = '''LAGS_MV = np.arange(-400, 401, 10)
LAGS_GO = np.arange(-200, 201, 10)

def time_course(cfg, sel):
    P = cfg["P"][:, sel]
    mv = np.array([np.nanmean(mp.rowwise_corr(P, cfg["CMm"][:, sel, np.flatnonzero(MV_L == t)[0]])) for t in LAGS_MV])
    go = np.array([np.nanmean(mp.rowwise_corr(P, cfg["CMg"][:, sel, np.flatnonzero(GO_L == t)[0]])) for t in LAGS_GO])
    return go, mv

def judge_tc(mv):
    at0 = mv[LAGS_MV == 0][0]; at200 = mv[LAGS_MV == -200][0]
    drops = mv[:-5] - mv[5:]            # drop over 50 ms starting at each lag
    start = LAGS_MV[:-5][np.argmax(drops)]
    return {"r at -200": at200, "r at 0": at0, "largest 50 ms drop starts": start,
            "pass": at0 < 0.1 and at0 < 0.5 * at200 and -300 <= start <= 0,
            "partial": at0 >= 0.1 and at0 < at200}

def pop_avg(cfg, sel, normalise=True):
    P = cfg["P"][:, sel]
    n_c = P.shape[0]
    order = np.argsort(P, axis=0)
    ranks = [order[-1], order[int(round((n_c - 1) * 2 / 3))], order[int(round((n_c - 1) / 3))], order[0]]
    idx = np.flatnonzero(sel)
    go_tr, mv_tr = [], []
    for rk in ranks:
        g = np.stack([cfg["CMg"][c, u] for c, u in zip(rk, idx)])
        m = np.stack([cfg["CMm"][c, u] for c, u in zip(rk, idx)])
        if normalise:
            mx = np.maximum(cfg["CMg"][:, idx].max((0, 2)), cfg["CMm"][:, idx].max((0, 2)))
            g, m = g / mx[:, None], m / mx[:, None]
        go_tr.append(g.mean(0)); mv_tr.append(m.mean(0))
    return np.array(go_tr), np.array(mv_tr)

def judge_pop(go_tr, mv_tr):
    prep = (GO_L >= mp.PREP_WIN[0]) & (GO_L <= mp.PREP_WIN[1])
    spread_prep = (go_tr[0] - go_tr[3])[prep].mean()
    spread_0 = (mv_tr[0] - mv_tr[3])[MV_L == 0][0]
    top150 = mv_tr[:, MV_L == -150][:, 0]
    return {"spread prep": spread_prep, "spread at onset": spread_0, "ratio": spread_0 / spread_prep,
            "strongest on top at -150": bool(np.argmax(top150) == 0),
            "pass": spread_0 < 0.5 * spread_prep and np.argmax(top150) == 0}

def means_from(o, idx_prep, idx_peri, labels, cond_list):
    """Condition means over `cond_list`, go-locked from trials idx_prep and movement-locked from
    idx_peri (positions in `keep`), with the given condition label of every kept trial."""
    Rg, Rm = RATES[o]
    cm = lambda R, idx: np.stack([R[idx[labels[idx] == c]].mean(0) for c in cond_list])
    cfg = {"CMg": cm(Rg, idx_prep), "CMm": cm(Rm, idx_peri)}
    cfg["P"] = mp.epoch_mean(cfg["CMg"], GO_L, mp.PREP_WIN)
    cfg["M"] = mp.epoch_mean(cfg["CMm"], MV_L, mp.PERI_WIN)
    return cfg

def noise_row(cfg, sel=None):
    sel_b = mp.tuning(cfg["P"], "range") > mp.PREP_TUNING_MIN
    sel = fig4_units(cfg, "range", "i") if sel is None else sel
    r, _ = fig4_corrs(cfg, sel)
    q1, q3 = np.nanpercentile(r, [25, 75])
    ja, jb = judge_tc(time_course(cfg, sel)[1]), judge_tc(time_course(cfg, sel_b)[1])
    pa = judge_pop(*pop_avg(cfg, sel, True))
    return {"n > 5 spikes/s": int(sel_b.sum()), "n fig4": int(sel.sum()), "mean r": np.nanmean(r), "IQR r": q3 - q1,
            "fig4e(a) r -200": ja["r at -200"], "r 0": ja["r at 0"], "drop": ja["largest 50 ms drop starts"], "pass (a)": ja["pass"],
            "fig4e(b) r -200": jb["r at -200"], "r 0 (b)": jb["r at 0"], "pass (b)": jb["pass"],
            "suppfig1 ratio": pa["ratio"], "top at -150": pa["strongest on top at -150"], "suppfig1 pass": pa["pass"]}

rng_null = np.random.default_rng(7)
kp_main = np.flatnonzero(CONFIGS[MAIN]["kept"])
lab_all = conds.copy()
rows = [{"set": "data (main reading)", **noise_row(CONFIGS[MAIN])}]
for s in range(20):
    lab = conds.copy(); lab[kp_main] = rng_null.permutation(conds[kp_main])
    rows.append({"set": f"shuffle {s + 1}", **noise_row(means_from("a", kp_main, kp_main, lab, range(C)))})
null_table = pd.DataFrame(rows)
print("condition-shuffled null, main reading")
print(null_table.round(3).to_string(index=False))
nt = null_table.iloc[1:]
print("over 20 shuffles: units passing > 5 spikes/s range %d to %d (data %d of %d); fig4e passes (a) %d, (b) %d; suppfig1 passes %d;"
      % (nt["n > 5 spikes/s"].min(), nt["n > 5 spikes/s"].max(), null_table["n > 5 spikes/s"].iloc[0], len(units),
         nt["pass (a)"].sum(), nt["pass (b)"].sum(), nt["suppfig1 pass"].sum()))
print("  mean r %.3f to %.3f; IQR of r %.3f to %.3f; fig4e(b) r at -200 %.2f to %.2f and at onset %.3f to %.3f"
      % (nt["mean r"].min(), nt["mean r"].max(), nt["IQR r"].min(), nt["IQR r"].max(),
         nt["fig4e(b) r -200"].min(), nt["fig4e(b) r -200"].max(), nt["r 0 (b)"].min(), nt["r 0 (b)"].max()))

rows = []
for key, cfg in CONFIGS.items():
    kp = np.flatnonzero(cfg["kept"])
    A, B, both = [], [], []
    for c in range(C):
        idx = kp[conds[kp] == c]
        if len(idx) >= 2:
            A += list(idx[0::2]); B += list(idx[1::2]); both.append(c)
    A, B = np.array(A), np.array(B)
    sel = fig4_units(cfg, "range", "i")[None]
    for name, (X, Y) in (("prep A, move B", (A, B)), ("prep B, move A", (B, A))):
        d = means_from(key[0], X, Y, conds, both)
        rows.append({"O3": key[0], "O4": key[1], "split": name, "conditions": len(both), "trials": f"{len(X)}/{len(Y)}",
                     **noise_row(d, sel[0])})
disj_table = pd.DataFrame(rows).drop(columns=["n > 5 spikes/s"])
print()
print("disjoint trials for the preparatory and movement-locked means (units of fig4d, O1 range, O2 i)")
print(disj_table.round(3).to_string(index=False))
print("disjoint readings: fig4e passes (a) %d, (b) %d of %d; suppfig1 passes %d; fig4e(b) r at -200 %.2f to %.2f"
      % (disj_table["pass (a)"].sum(), disj_table["pass (b)"].sum(), len(disj_table), disj_table["suppfig1 pass"].sum(),
         disj_table["fig4e(b) r -200"].min(), disj_table["fig4e(b) r -200"].max()))'''

TC_CODE_HEAD_OLD = None
PYEOF
echo ok
```

```
ok
```

**Agent calls Bash**

```bash
cd  sed -i 's/^lab_all = conds.copy()\n//' $TMPDIR/cells.py; python - <<'EOF'
import os
p=os.environ['TMPDIR']+'/cells.py'; s=open(p).read(); s=s.replace("lab_all = conds.copy()\n",""); open(p,'w').write(s)
EOF
cat >> $TMPDIR/cells.py <<'PYEOF'

F6_MD = """Spread of the fig6d comparisons, a second reading of the T matrix, and a noise reference.

- Per reading, the peri-movement performance per unit (at the k best on average) is compared with
  the best other space per unit by a paired t-test, with SEs across units.
- The Methods say each row of the T matrix "contained data from all neurons except the neuron whose
  preparatory activity we were trying to capture", and that "Analysis of preparatory responses was
  restricted to neurons with at least 10 spikes/s of preparatory tuning" (5 for the arrays). "All
  neurons" may be all recorded units (main, 142) or the included units only; both are run.
- Condition-shuffled null (main reading, 10 shuffles): the neural condition labels are permuted, the
  kinematic and task spaces are left intact, and the same comparison is made."""

F6_CODE = '''rows = []
for key in CONFIGS:
    res = PERF[key]
    for O1 in ("range", "sd"):
        sel = mp.tuning(CONFIGS[key]["P"], O1) > mp.PREP_TUNING_MIN
        for kmax in (14, 20):
            for end in (600, 800):
                for seg in ("length", "time"):
                    peri = res["peri"][sel, :kmax]
                    pu = peri[:, np.argmax(np.nanmean(peri, 0))]
                    kin = res[f"kin{end}"][sel, :kmax]
                    others = {"kinematic": kin[:, np.argmax(np.nanmean(kin, 0))],
                              **{name: res[f"{seg}:{name}"][sel] for name in mp.TASK_SPACES}}
                    best_o = max(others, key=lambda k: np.nanmean(others[k]))
                    d = pu - others[best_o]
                    rows.append({"O3": key[0], "O4": key[1], "O1": O1, "kmax": kmax, "kin end": end, "segments": seg,
                                 "peri": np.nanmean(pu), "SE peri": np.nanstd(pu) / np.sqrt(len(pu)), "best other": best_o,
                                 "other": np.nanmean(others[best_o]), "peri - other": np.nanmean(d),
                                 "SE diff": np.nanstd(d) / np.sqrt(len(d)), "p paired t": stats.ttest_rel(pu, others[best_o], nan_policy="omit").pvalue})
f6_tests = pd.DataFrame(rows)
print(f6_tests.drop_duplicates(subset=["O3", "O4", "O1", "best other", "peri", "other"]).round(3).to_string(index=False))
print("(rows identical in all values but kmax, kin end and segments are shown once)")
print("readings where the peri-movement space is better than the best other space at p < 0.05: %d of %d; p range %.2f to %.2f"
      % (((f6_tests["p paired t"] < 0.05) & (f6_tests["peri - other"] > 0)).sum(), len(f6_tests), f6_tests["p paired t"].min(), f6_tests["p paired t"].max()))

rows = []
for key, cfg in CONFIGS.items():
    for O1 in ("range", "sd"):
        sel = mp.tuning(cfg["P"], O1) > mp.PREP_TUNING_MIN
        sc = mp.leave_one_out_scores(cfg["CMm"][:, :, TSEL], KMAX, members=sel)
        pm = np.nanmean(perf_matrix(cfg["P"], sc, np.flatnonzero(sel)), 0)
        kin = np.nanmean(PERF[key]["kin800"][sel], 0).max()
        tasks = {n: np.nanmean(PERF[key][f"length:{n}"][sel]) for n in mp.TASK_SPACES}
        best_t = max(tasks, key=tasks.get)
        n_beat = int(kin >= pm.max()) + sum(v >= pm.max() for v in tasks.values())
        rows.append({"O3": key[0], "O4": key[1], "O1": O1, "n": int(sel.sum()),
                     "peri best, T of all units": np.nanmean(PERF[key]["peri"][sel], 0).max(),
                     "peri best, T of included units": pm.max(), "k": int(np.argmax(pm) + 1), "kin best": kin,
                     "best task": tasks[best_t], "spaces >= peri (included)": n_beat,
                     "outcome (included)": "reproduced" if n_beat == 0 else ("partial" if n_beat == 1 else "no")})
memb_table = pd.DataFrame(rows)
print()
print("peri-movement T matrix from all recorded units or from the included units only (kmax 20, kin end 800, segments by length)")
print(memb_table.round(3).to_string(index=False))

rng_f6 = np.random.default_rng(8)
ks_main = mp.pca_scores(mp.kinematic_matrix(CONFIGS[MAIN]["KIN"], 800), KMAX)
rows = []
for s in range(10):
    lab = conds.copy(); lab[kp_main] = rng_f6.permutation(conds[kp_main])
    d = means_from("a", kp_main, kp_main, lab, range(C))
    sel = mp.tuning(d["P"], "range") > mp.PREP_TUNING_MIN
    sc = mp.leave_one_out_scores(d["CMm"][:, :, TSEL], 14)
    pm = np.nanmean(perf_matrix(d["P"], sc, np.flatnonzero(sel), 14), 0)
    km = np.nanmean(perf_matrix(d["P"], [ks_main] * len(units), np.flatnonzero(sel), 14), 0)
    iv = np.nanmean([mp.loo_performance(d["P"][:, j], CONFIGS[MAIN]["TS_length"]["initial vel."]) for j in np.flatnonzero(sel)])
    rows.append({"shuffle": s + 1, "n": int(sel.sum()), "peri best": pm.max(), "k": int(np.argmax(pm) + 1), "kin best": km.max(), "initial vel.": iv})
f6_null = pd.DataFrame(rows)
print()
print("condition-shuffled null, main reading (data: peri -0.044, kinematic -0.053, initial vel. -0.048)")
print(f6_null.round(3).to_string(index=False))
print("null peri best %.3f to %.3f, kinematic best %.3f to %.3f" % (f6_null["peri best"].min(), f6_null["peri best"].max(),
                                                                   f6_null["kin best"].min(), f6_null["kin best"].max()))'''
PYEOF
echo ok
```

```
ok
```

**Agent calls Bash**

```bash
cd  python - <<'EOF'
import os
p=os.environ['TMPDIR']+'/cells.py'; s=open(p).read()
s=s.replace('''print("condition-shuffled null, main reading (data: peri -0.044, kinematic -0.053, initial vel. -0.048)")''',
'''print("condition-shuffled null, main reading (data: peri %.3f, kinematic %.3f, initial vel. %.3f)" % (peri6.max(), kin6.max(), tasks6["initial vel."]))''')
open(p,'w').write(s)
EOF
cat >> $TMPDIR/cells.py <<'PYEOF'

MAZE_CODE = '''rows = []
for key in CONFIGS:
    for O1 in ("range", "sd"):
        for kmax in (14, 20):
            sel, peri, kin, tasks = fig6_summary(key, O1, kmax, 800, "length")
            e = tasks["endpoints + max. spd."]
            d = PERF[key]["peri"][sel, 2] - PERF[key]["length:endpoints + max. spd."][sel]
            rows.append({"O3": key[0], "O4": key[1], "O1": O1, "kmax": kmax, "endpoints+max spd": e, "peri k=3": peri[2],
                         "diff": peri[2] - e, "SE diff": np.nanstd(d) / np.sqrt(len(d)), "p paired t": stats.ttest_rel(PERF[key]["peri"][sel, 2], PERF[key]["length:endpoints + max. spd."][sel], nan_policy="omit").pvalue,
                         "best peri": peri.max(), "below peri3 by >= 0.1": e <= peri[2] - 0.1, "below half best": e < 0.5 * peri.max(),
                         "pass": (e <= peri[2] - 0.1) and (e < 0.5 * peri.max())})
ems_table = pd.DataFrame(rows)
print(ems_table.round(3).to_string(index=False))
print("readings passing:", int(ems_table["pass"].sum()), "of", len(ems_table))
# O1 SD with the peri-movement T matrix of the included units only (see fig6d)
rows = []
for key, cfg in CONFIGS.items():
    sel = mp.tuning(cfg["P"], "sd") > mp.PREP_TUNING_MIN
    sc = mp.leave_one_out_scores(cfg["CMm"][:, :, TSEL], 14, members=sel)
    pm = np.nanmean(perf_matrix(cfg["P"], sc, np.flatnonzero(sel), 14), 0)
    e = np.nanmean(PERF[key]["length:endpoints + max. spd."][sel])
    rows.append({"O3": key[0], "O4": key[1], "n": int(sel.sum()), "endpoints+max spd": e, "peri k=3 (included)": pm[2],
                 "best peri (included)": pm.max(), "pass": (e <= pm[2] - 0.1) and (e < 0.5 * pm.max())})
print("O1 SD, T matrix of the included units:")
print(pd.DataFrame(rows).round(3).to_string(index=False))'''
PYEOF
echo ok
```

```
ok
```

**Agent**

Now apply the code changes to the notebook.

**Agent calls Bash**

```bash
cd  cat > $TMPDIR/apply1.py <<'PYEOF'
import json, os, re
exec(open(os.environ['TMPDIR']+'/cells.py').read())
path='entries/000140-churchland-2010/reproduce_churchland_2010.ipynb'
nb=json.load(open(path))
cells=nb['cells']
def src(i): return ''.join(cells[i]['source'])
def setsrc(i, s): cells[i]['source']=s.splitlines(keepends=True)
def md(s): return {"cell_type":"markdown","metadata":{},"source":s.splitlines(keepends=True)}
def code(s, tags=None):
    c={"cell_type":"code","execution_count":None,"metadata":{},"outputs":[],"source":s.splitlines(keepends=True)}
    if tags: c["metadata"]["tags"]=tags
    return c
# cell 21: drop function defs (moved to noise cell)
s=src(21); s=s[s.index("rows, curves = [], {}"):]; setsrc(21,s)
# cell 24: drop pop_avg/judge_pop defs
s=src(24); s=s[s.index("rows = []"):]; setsrc(24,s)
# cell 34 maze
setsrc(34, MAZE_CODE)
# cell 45 fig7a: all configs
s=src(45); s=s.replace('for key in [MAIN, ("a", "c"), ("b", "a")]:','for key in CONFIGS:'); setsrc(45,s)
# cell 48 fig7b
s=src(48); s=s.replace('for key in [MAIN, ("a", "c"), ("b", "a")]:','for key in CONFIGS:')
s=s.replace('        row["ratio 0/-150"] = row[0] / row[-150]\n',
            '        row["ratio 0/-150"] = row[0] / row[-150] if row[-150] > 0 else np.nan   # a ratio of negative performances is undefined\n')
s=s.replace('print("ratio within 0.97 +/- 0.097:", int(((slide_table["ratio 0/-150"] - 0.97).abs() <= 0.097).sum()), "of", len(slide_table))',
 'print("ratio defined (performance at -150 ms above zero):", int(slide_table["ratio 0/-150"].notna().sum()), "of", len(slide_table),\n      "| within 0.97 +/- 0.097:", int(((slide_table["ratio 0/-150"] - 0.97).abs() <= 0.097).sum()))\nprint("O1 SD ratios: %.3f to %.3f" % (slide_table["ratio 0/-150"].min(), slide_table["ratio 0/-150"].max()))')
setsrc(48,s)
# cell 52 ap: swapped
s=src(52)
s=s.replace('''print("readings with p >= 0.05:", int((ap_table.p >= 0.05).sum()), "of", len(ap_table),
      "| swapping the arrays changes the sign of r only")''',
'''ap_table["regression r, arrays swapped"] = -ap_table["regression r"]   # the 0/1 location is reversed; p is unchanged
print(ap_table.round(3).to_string(index=False))
print("readings with p >= 0.05:", int((ap_table.p >= 0.05).sum()), "of", len(ap_table), "under either mapping of the arrays")''')
s=s.replace('ap_table = pd.DataFrame(rows)\nprint(ap_table.round(3).to_string(index=False))\n','ap_table = pd.DataFrame(rows)\n')
setsrc(52,s)
# cell 56 fig7c: swapped and O1 SD random halves
s=src(56)
s=s.replace('''sd_sel = mp.tuning(P, "sd") > mp.PREP_TUNING_MIN
for lab, mem in (("PMd (anterior), O1 SD units", pmd), ("M1 (posterior), O1 SD units", ~pmd)):
    p6, up, n = half_perf(mem, "all", sd_sel)
    rows.append({"space from": "all", "subset": lab, "n tuned": n, "perf k=6": p6, "upper limit": up,
                 "normalised": p6 / up if up > 0 else np.nan})''',
'''sd_sel = mp.tuning(P, "sd") > mp.PREP_TUNING_MIN
for lab, mem in (("all units, O1 SD units", np.ones(len(units), bool)), ("PMd (anterior), O1 SD units", pmd), ("M1 (posterior), O1 SD units", ~pmd)):
    p6, up, n = half_perf(mem, "all", sd_sel)
    rows.append({"space from": "all", "subset": lab, "n tuned": n, "perf k=6": p6, "upper limit": up,
                 "normalised": p6 / up if up > 0 else np.nan})
rand = []
for _ in range(20):
    mem = np.zeros(len(units), bool); mem[rng_ap.choice(len(units), pmd.sum(), replace=False)] = True
    if (mem & sd_sel).sum():
        p6, up, n = half_perf(mem, "all", sd_sel)
        rand.append((p6, up, p6 / up if up > 0 else np.nan))
rand = np.array(rand)
rows.append({"space from": "all", "subset": f"random halves ({len(rand)}), O1 SD units", "n tuned": np.nan, "perf k=6": rand[:, 0].mean(),
             "upper limit": rand[:, 1].mean(), "normalised": np.nanmean(rand[:, 2])})''')
s=s.replace('''print("upper limits <= 0 make the normalisation undefined:", int((ap7_table["upper limit"] <= 0).sum()), "of", len(ap7_table))''',
'''print("upper limits <= 0 make the normalisation undefined:", int((ap7_table["upper limit"] <= 0).sum()), "of", len(ap7_table))
for a_lab, b_lab, name in (("PMd (anterior)", "M1 (posterior)", "prefix 1 = PMd"), ("M1 (posterior)", "PMd (anterior)", "arrays swapped (prefix 2 = PMd)")):
    t_ = ap7_table[ap7_table["space from"] == "half"].set_index("subset")["perf k=6"]
    print(f"{name}: raw 6-D performance, anterior {t_[a_lab]:.3f}, posterior {t_[b_lab]:.3f} (space from the half's units)")''')
setsrc(56,s)
# cell 59 prevalence: swapped
s=src(59)
s=s.replace('''        rows.append({"O3": o, "O4": f, "O1": O1, "PMd passing": f"{a_}/{pmd.sum()}", "M1 passing": f"{b_}/{(~pmd).sum()}",
                     "frac PMd": a_ / pmd.sum(), "frac M1": b_ / (~pmd).sum(), "Fisher p": p})''',
'''        fa, fb = a_ / pmd.sum(), b_ / (~pmd).sum()
        judge = lambda ant, post: "reproduced" if ant > post and p < 0.05 else ("partial" if ant > post else "not reproduced")
        rows.append({"O3": o, "O4": f, "O1": O1, "prefix 1 passing": f"{a_}/{pmd.sum()}", "prefix 2 passing": f"{b_}/{(~pmd).sum()}",
                     "frac prefix 1": fa, "frac prefix 2": fb, "Fisher p": p,
                     "outcome if prefix 1 = PMd": judge(fa, fb), "outcome if prefix 2 = PMd": judge(fb, fa)})''')
s=s.replace('print(prev_table.round(4).to_string(index=False))\n','print(prev_table.round(4).to_string(index=False))\nprint(prev_table.groupby("O1")[["outcome if prefix 1 = PMd", "outcome if prefix 2 = PMd"]].agg(lambda x: x.value_counts().to_dict()))\n')
setsrc(59,s)
# cell 62 fig7d all configs and O1
setsrc(62, '''rng_pd = np.random.default_rng(5)
rows = []
for key, cfg in CONFIGS.items():
    P = cfg["P"]
    ks_kin = mp.pca_scores(mp.kinematic_matrix(cfg["KIN"], 800), KMAX)
    for O1 in ("range", "sd"):
        sel = np.flatnonzero(mp.tuning(P, O1) > mp.PREP_TUNING_MIN)
        kin_k = int(np.argmax(np.nanmean(PERF[key]["kin800"][sel, :14], 0)) + 1)
        comps = {"endpoints + max. spd.": cfg["TS_length"]["endpoints + max. spd."],
                 "segment dirs.": cfg["TS_length"]["segment dirs."], "kinematic (best k)": ks_kin[:, :kin_k]}
        for name, S in comps.items():
            k = S.shape[1]
            for zs in (False, True):
                c_other = np.nanmean([mp.pd_consistency(P[:, j], S, rng_pd, standardize=zs) for j in sel])
                c_peri = np.nanmean([mp.pd_consistency(P[:, j], PERF[key]["peri_scores"][j][:, :k], rng_pd, standardize=zs) for j in sel])
                rows.append({"O3": key[0], "O4": key[1], "O1": O1, "space": name, "k": k, "z-scored axes": zs, "n units": len(sel),
                             "consistency other": c_other, "consistency peri": c_peri, "peri higher": c_peri > c_other})
pd_table = pd.DataFrame(rows)
print(pd_table.round(3).to_string(index=False))
print("comparisons with peri higher:", int(pd_table["peri higher"].sum()), "of", len(pd_table))
print(pd_table.groupby(["O1", "space"])["peri higher"].agg(["sum", "count"]))''')
# insert new cells: after 27 (fig6d) and after 14 (fig4d) -- do higher index first
cells.insert(28, code(F6_CODE, ["claim:fig6d-perimovement-best-j-array"]))
cells.insert(28, md(F6_MD))
cells.insert(15, code(NOISE_CODE, ["claim:fig4d-mean-correlation-j-array","claim:fig4-broad-near-zero","claim:fig4e-correlation-time-course","claim:suppfig1-population-averages-lose-tuning"]))
cells.insert(15, md(NOISE_MD))
json.dump(nb, open(path,'w'), indent=1, ensure_ascii=False); open(path,'a').write("\n")
print(len(cells))
PYEOF
python $TMPDIR/apply1.py; git diff --stat
```

```
73
 .../reproduce_churchland_2010.ipynb                | 354 +++++++++++++++++----
 1 file changed, 288 insertions(+), 66 deletions(-)
```

**Agent calls Bash**

```bash
cd  git diff entries/ | head -30; python - <<'EOF'
p='entries/000140-churchland-2010/maze_prep.py'
s=open(p).read()
s=s.replace('''def simulate_rotation(rng, n_cond=25, hold=100, n_steps=360, init="disk"):
    """x(t+1) = W x(t), W = [[1, -2pi/360], [2pi/360, 1]] (Figure 8 legend), after holding the
    initial state for `hold` steps. Returns initial states (c x 2) and released trajectories
    (c x n_steps x 2)."""''','''def simulate_rotation(rng, n_cond=25, n_steps=360, init="disk"):
    """x(t+1) = W x(t), W = [[1, -2pi/360], [2pi/360, 1]] (Figure 8 legend), released from the
    initial state. Holding the initial state before release (the figure's preparatory period) would
    not change either measure, so no hold is simulated. Returns initial states (c x 2) and released
    trajectories (c x n_steps x 2)."""''')
s=s.replace('''- Upper limit of PD performance: PCA space of the c x n preparatory matrix (C; Supplemental
  Experimental Procedures, Estimating the upper limit), here without the fitted unit, as for the
  peri-movement space (A).''','''- Upper limit of PD performance: PCA space of the c x n preparatory matrix (C; Supplemental
  Experimental Procedures, Estimating the upper limit), here without the fitted unit, as for the
  peri-movement space (A).
- Units in the peri-movement T matrix: "all neurons except the neuron whose preparatory activity
  we were trying to capture" (Methods, PCA-based spaces), read as all recorded units (main) or the
  units passing the inclusion rule ("Analysis of preparatory responses was restricted to neurons
  with at least 10 spikes/s of preparatory tuning", Methods); `leave_one_out_scores(members=...)`
  gives the second reading.''')
open(p,'w').write(s)
EOF
grep -n "hold" entries/000140-churchland-2010/maze_prep.py
```

```
diff --git a/entries/000140-churchland-2010/reproduce_churchland_2010.ipynb b/entries/000140-churchland-2010/reproduce_churchland_2010.ipynb
index 671598744..5a3366780 100644
--- a/entries/000140-churchland-2010/reproduce_churchland_2010.ipynb
+++ b/entries/000140-churchland-2010/reproduce_churchland_2010.ipynb
@@ -473,6 +473,145 @@
     "print(\"O2 ii (main otherwise): n = %d, mean r = %.3f (t-test p = %.3f), mean Spearman %.3f\" % (sel_ii.sum(), r_ii.mean(), stats.ttest_1samp(r_ii, 0).pvalue, rs_ii.mean()))"
    ]
   },
+  {
+   "cell_type": "markdown",
+   "metadata": {},
+   "source": [
+    "### Noise reference for fig4d, fig4-broad-near-zero, fig4e and suppfig1\n",
+    "\n",
+    "With 1 to 4 trials per condition, the preparatory and peri-movement means of a condition share the\n",
+    "noise of the same few trials, and the preparatory window ends 100 ms after the go cue, about 220 ms\n",
+    "before movement onset (median reaction time 321 ms). Two references are computed on the main reading\n",
+    "(O3a, O4a, O1a):\n",
+    "\n",
+    "- **condition-shuffled null**: the condition labels of the kept trials are permuted (counts kept), and\n",
[... 13 more lines not kept]
```

**Agent**

Run the full entry now.

**Agent calls Bash**

```bash
cd  date -u; python tools/entry.py all entries/000140-churchland-2010 2>&1 | tail -5; date -u
```

```
Thu Oct 29 01:07:59 UTC 2026
/opt/hostedtoolcache/Python/3.13.17/x64/lib/python3.13/site-packages/nbformat/validator.py:434: MissingIDFieldWarning: Cell is missing an id field, this will become a hard error in future nbformat versions. You may want to use `normalize()` on your notebooks before validations (available since nbformat 5.1.4). Previous versions of nbformat are fixing this issue transparently, and will stop doing so in the future.
  _validate(nbdict, ref, version, version_minor, relax_add_props)
Installed kernelspec registry-000140-churchland-2010 in executed/000140-churchland-2010/.venv/share/jupyter/kernels/registry-000140-churchland-2010
0 error(s)
pass  reproduce_churchland_2010.ipynb  (227 s)
Thu Oct 29 01:12:22 UTC 2026
```

**Agent calls Bash**

```bash
cd executed/000140-churchland-2010; python - <<'EOF'
import json
nb=json.load(open('reproduce_churchland_2010.ipynb'))
for i,c in enumerate(nb['cells']):
    if c['cell_type']!='code' or i not in (16,23,26,30,37,49,52,56,60,62,64,66): continue
    print(f"===== [{i}] {c['metadata'].get('tags')}")
    for o in c.get('outputs',[]):
        if 'text' in o and o.get('name')=='stdout': print(''.join(o['text'])[:6000])
EOF
```

```
===== [16] ['claim:fig4d-mean-correlation-j-array', 'claim:fig4-broad-near-zero', 'claim:fig4e-correlation-time-course', 'claim:suppfig1-population-averages-lose-tuning']
condition-shuffled null, main reading
                set  n > 5 spikes/s  n fig4  mean r  IQR r  fig4e(a) r -200    r 0  drop  pass (a)  fig4e(b) r -200  r 0 (b)  pass (b)  suppfig1 ratio  top at -150  suppfig1 pass
data (main reading)              93      19  -0.079  0.201            0.295 -0.078  -250      True            0.388   -0.001      True           0.186         True           True
          shuffle 1              92      10   0.026  0.239            0.188 -0.062  -250      True            0.334   -0.028      True           0.393        False          False
          shuffle 2              95      13  -0.002  0.101            0.319 -0.123   120     False            0.280    0.001      True          -0.355         True           True
          shuffle 3              82       9  -0.081  0.169            0.214 -0.009  -130      True            0.314   -0.001      True           0.193         True           True
          shuffle 4              89      13   0.038  0.330            0.208 -0.003  -280      True            0.301   -0.023      True           0.323        False          False
          shuffle 5              92      13   0.013  0.069            0.308 -0.021  -190      True            0.328    0.015      True           0.264         True           True
          shuffle 6              87      15  -0.060  0.291            0.196 -0.008  -230      True            0.340    0.000      True          -0.396        False          False
          shuffle 7              90      15  -0.024  0.226            0.273  0.053  -280      True            0.332    0.009      True           0.146         True           True
          shuffle 8              87      13   0.019  0.184            0.206 -0.062  -250      True            0.292    0.004      True           0.207        False          False
 
[... 249 more lines not kept]
```

**Agent calls Bash**

```bash
cd executed/000140-churchland-2010; python - <<'EOF'
import json
nb=json.load(open('reproduce_churchland_2010.ipynb'))
for i,c in enumerate(nb['cells']):
    tags=c['metadata'].get('tags') or []
    if c['cell_type']!='code': continue
    if not any(t in ('claim:fig6d-perimovement-best-j-array','claim:fig6-maze-endpoint-speed-space-poor','claim:prep-activity-more-anterior','claim:fig7d-pd-consistency','claim:fig8-linear-dynamics-simulation') for t in tags): continue
    if i==29: continue
    print(f"===== [{i}] {tags}")
    out=''.join(''.join(o['text']) for o in c.get('outputs',[]) if o.get('name')=='stdout')
    print(out[-5000:] if 'fig7d' in tags[0] else out)
EOF
```

```
===== [31] ['claim:fig6d-perimovement-best-j-array']
O3 O4    O1  kmax  kin end segments   peri  SE peri   best other  other  peri - other  SE diff  p paired t
 a  a range    14      600   length -0.044    0.021 initial vel. -0.048         0.004    0.018       0.813
 a  a    sd    14      600   length  0.209    0.097    kinematic  0.138         0.072    0.125       0.608
 a  a    sd    14      800   length  0.209    0.097    kinematic  0.136         0.073    0.124       0.596
 a  b range    14      600   length -0.045    0.022 initial vel. -0.041        -0.004    0.018       0.815
 a  b    sd    14      600   length  0.202    0.091    kinematic  0.135         0.068    0.147       0.680
 a  b    sd    14      800   length  0.202    0.091    kinematic  0.133         0.070    0.146       0.669
 a  c range    14      600   length -0.023    0.022 initial vel. -0.036         0.013    0.018       0.492
 a  c    sd    14      600   length  0.247    0.053 kitchen sink  0.228         0.018    0.079       0.836
 a  c    sd    14      600     time  0.247    0.053 kitchen sink  0.186         0.060    0.110       0.628
 b  a range    14      600   length -0.046    0.021 initial vel. -0.042        -0.004    0.018       0.820
 b  a    sd    14      600   length  0.140    0.132    kinematic  0.135         0.005    0.123       0.968
 b  a    sd    14      800   length  0.140    0.132    kinematic  0.133         0.007    0.123       0.958
 b  b range    14      600   length -0.043    0.023 initial vel. -0.033        -0.010    0.018       0.572
 b  b    sd    14      600   length  0.129    0.125    kinematic  0.134        -0.005    0.104       0.965
 b  b    sd    14      800   length  0.129    0.125    kinematic  0.132        -0.003    0.103       0.982
 b  c range    14      600   length -0.026    0.022 initial vel. -0.029         0.003    0.018       0.885
 b  c    sd    14      600   length  0.249    0.058 kitchen sink  0.217         0.032    0.078       0.720
 b  c    sd    14    
[... 147 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat > $TMPDIR/apply2.py <<'PYEOF'
import json
path='entries/000140-churchland-2010/reproduce_churchland_2010.ipynb'
nb=json.load(open(path)); cells=nb['cells']
def find(prefix):
    hits=[i for i,c in enumerate(cells) if ''.join(c['source']).startswith(prefix)]
    assert len(hits)==1,(prefix,hits); return hits[0]
def setmd(prefix, text):
    cells[find(prefix)]['source']=text.strip('\n').splitlines(keepends=True)
def md(s): return {"cell_type":"markdown","metadata":{},"source":s.strip('\n').splitlines(keepends=True)}

# header table rows
i=find("# Churchland et al. (2010)")
s=''.join(cells[i]['source'])
s=s.replace("| fig7c-anterior-posterior-performance | tested on array identity (assumption) |",
            "| fig7c-anterior-posterior-performance | run on array identity; blocked: other (the normalisation is undefined) |")
s=s.replace("| prep-activity-more-anterior | tested on array identity (assumption) |",
            "| prep-activity-more-anterior | run on array identity; blocked: metadata_insufficient (which array is anterior) |")
cells[i]['source']=s.splitlines(keepends=True)

i=find("### Readings adopted")
s=''.join(cells[i]['source']).rstrip('\n')+"""
- Units in the peri-movement T matrix ("all neurons except the neuron whose preparatory activity we
  were trying to capture", Methods): all recorded units (main) and, as a second reading, the units
  passing the inclusion rule; both are run in fig6d. Under O1a they give the same outcome."""
cells[i]['source']=s.splitlines(keepends=True)

# after noise code cell insert summary
j=find("### Noise reference for fig4d")+2
cells.insert(j, md("""
**Noise reference.** With condition labels shuffled, 82 to 96 units pass the > 5 spikes/s range rule,
against 93 with the true labels: under O1a the selection admits units whose range comes from trial
noise. The paper justified the 5 spikes/s threshold by its trial count ("acceptable given the higher
signal-to-noise ratio provided by the higher trial count", Methods), which this dandiset does not have.
The conclusions of fig4d, fig4-broad-near-zero, fig4e and suppfig1 below refer to both references.
"""))

setmd("**Result: not reproduced.** Under none of the 18 readings", """
**Result: not reproduced.** Under none of the 18 readings with units is the mean correlation within
0.13 ± 0.013 or positive at p < 0.05: mean r ranges from -0.148 to 0.095 and mean Spearman r from -0.061
to 0.061 (main reading -0.079 and -0.020, 19 units, 27 conditions); the one reading at p < 0.05 has a
negative mean. With condition labels shuffled the mean r is -0.106 to 0.074, so the main value is within
what trial noise gives. The condition means here rest on 1 to 4 trials, and their split-half
reliability (above) is low, so a weak true correlation such as 0.13 could not be resolved; the outcome
is a property of these 100 trials, not a test of the paper's J-array data.
""")
setmd("**Result: partially reproduced, resting on the assumption that tuning", """
**Result: not reproduced, resting on the assumption that tuning is the range across conditions
(O1a).** Under O1a (12 readings) the median correlation is near zero (-0.098 to 0.016), 92% to 100% of
units have |r| < 0.5, at most 1.2% lie above 0.8 and none below -0.8, but the interquartile range
(0.173 to 0.286) is below the 0.3 the criterion asks for a broad range in every O1a reading. The
criterion has no partial rule, and the condition that fails is the one that tests the breadth the claim
states. The conditions that hold are also met by noise: with condition labels shuffled the IQR is 0.069
to 0.422 and the mean r -0.106 to 0.074. Under O1b (SD; 3 to 5 units) all 6 readings pass.
""")
setmd("**Result: reproduced, resting on the assumption that tuning is the range across conditions", """
**Result: reproduced, resting on the assumption that tuning is the range across conditions (O1a); trial
noise also meets the criterion, so the pass carries little evidence.** Under every reading with O1a (18
of 18) the mean correlation at movement onset is below 0.1 and below half its value at 200 ms before
onset, and the largest 50 ms drop starts between 270 and 210 ms before onset; in the main reading it
falls from 0.295 at -200 ms to -0.078 at onset, and for all units with preparatory tuning from 0.39 to
-0.00. With condition labels shuffled the criterion is met in 18 of 20 shuffles for the fig4 units and
in 20 of 20 for all units with > 5 spikes/s (r at -200 ms 0.28 to 0.37, at onset -0.028 to 0.035): the
preparatory and movement-locked means share the noise of the same 1 to 4 trials, and the preparatory
window ends about 220 ms before onset. With the two means taken from disjoint trials, the correlation
at -200 ms is only 0.12 to 0.18 for all units, and the criterion is met in 4 of 12 readings (fig4 units)
and 9 of 12 (all units). Under O1b (SD, 3 to 8 units) the correlation at onset stays between 0.09 and
0.24, partially reproduced in 10 of 12 readings.
""")
setmd("**Result: reproduced.** In all 36 readings", """
**Result: reproduced; trial noise also meets the criterion in about half the shuffles, so the pass
carries little evidence.** In all 36 readings (normalised and not) the spread between the strongest and
weakest preparatory conditions at movement onset is less than half the preparatory spread (ratio 0.186
in the main normalised reading, -0.175 to 0.295 over readings), with the strongest-preparatory trace on
top at 150 ms before onset. With condition labels shuffled the criterion is met in 11 of 20 shuffles.
With the preparatory and movement-locked means from disjoint trials it is met in 2 of 12 readings, so
the strongest trace being on top at -150 ms, the part of the result that noise does not give every time,
comes mostly from noise shared within the same trials.
""")
setmd("**Result: reproduced, resting on assumptions (O1a range", """
**Result: partially reproduced, resting on the assumption O1a.** In the main reading the best
peri-movement performance (-0.044 at k = 2) is above the best kinematic (-0.053) and every task space
(best, initial velocity, -0.048). Over the 96 readings 64 meet the criterion and 32 are partial: under
O1a with the condition mean as proto-trial (O4b), or with the speed-based onset (O3b) and a filter, and
under O1b with O3b and O4b, the initial-velocity or kinematic space matches or beats it. The criterion
asks that it hold under each reading, so the outcome is partial. The differences are small against
their spread: in no reading is the peri-movement space better than the best other space at p < 0.05
(paired t p 0.47 to 0.98; main reading difference 0.004, SE 0.018). With the T matrix built from the
included units only, O1a gives the same (reproduced or partial in each of 6 settings), while under O1b
the peri-movement space falls to -0.022 to 0.101 and 6 to 8 spaces match or beat it. Under O1a every
space performs below zero, worse than predicting the mean rate, but above the condition-shuffled null
(peri-movement -0.214 to -0.092, kinematic -0.138 to -0.108), so the data carry some tuning these spaces
capture.
""")
setmd("**Result: not reproduced, resting on the assumption O1a.** Under O1a (12 readings) the end", """
**Result: not reproduced, resting on the assumption O1a.** Under O1a (12 readings) the endpoints +
max. speed space (-0.126 to -0.147) is below the 3-D peri-movement space by 0.011 to 0.065, less than
the 0.1 required (main: -0.143 against -0.104, SE of the difference 0.025). Under O1b (12 readings) it
passes with the T matrix of all recorded units: -0.040 to 0.018 against 0.101 to 0.209. With the T
matrix of the 7 or 8 included units, the 3-D peri-movement space gives -0.088 to 0.045 and no O1b reading
passes.
""")
setmd("**Result: reproduced.** In all 12 readings the shuffled", """
**Result: reproduced, weakly.** In all 24 readings (six O3/O4 settings, O1a and O1b, the coin per unit
or per condition) the shuffled space's best performance (mean of 20 shuffles) is below half the intact
best and below the best kinematic performance: main reading -0.097 against -0.044 intact and -0.053
kinematic. Under O1a the intact space is itself below zero, so "below half the intact best" is met
trivially; the evidence is the O1b readings (7 or 8 units), where the shuffled mean is -0.065 to 0.041
against an intact 0.129 to 0.249.
""")
setmd("**Result: not reproduced.** The ratio of performance with the window", """
**Result: not reproduced.** Under O1b the ratio of performance with the window starting at movement
onset to that at -150 ms is 0.471 to 0.761 in the 6 readings, outside 0.97 ± 0.097. Under O1a (6
readings) performance at -150 ms is below zero (-0.046 to -0.023), so the ratio is undefined; from there
it falls to -0.059 to -0.046 at onset. The monkeys A and B value cannot be computed from this dandiset.
""")
setmd("## Anterior and posterior sites", """
## Anterior and posterior sites

The electrodes table has no positions, and every unit's `electrodes` entry points to the PMd group.
The three claims below use array identity as the only anterior-posterior information: PMd anterior,
M1 posterior (Supplemental Figure 3 legend: "the first in caudal PMd ... the second in surface M1").
Which array is which is not in the file: the electrode index of both prefixes points into the PMd
group. Prefix 1 is read as PMd only because the PMd group comes first in the electrodes table. Each
claim's result is shown under both mappings: the regression r with the arrays swapped
(ap-location-no-effect-j-array), the raw performance of each half under each mapping (fig7c), and the
outcome under each mapping (prep-activity-more-anterior).
""")
setmd("**Result: reproduced, resting on the assumption that array identity gives AP location.** In all 17", """
**Result: reproduced, resting on the assumption that array identity gives AP location.** In all 17
readings with units in both arrays the tuning correlation does not differ between the two arrays
(p 0.538 to 1.000; main reading r = 0.105, p = 0.668, 10 and 9 units), under either mapping of the
arrays: swapping them changes only the sign of r. With 19 units and two locations the test has little
power.
""")
setmd("**Result: not reproduced, resting on the assumption that array identity gives AP location.** The", """
**Result: blocked (other): the normalised measure the criterion uses does not exist here.** Under O1a
the upper-limit performance is at or below zero for every subset (-0.019 to -0.097), so performance
cannot be normalised by it. The raw 6-D performance is far below zero at both arrays: -1.535 (prefix 1)
and -1.087 (prefix 2) with the space from the half's units, -1.454 and -1.293 from all units, against
-1.008 and -1.400 for random halves. Under O1b (4 and 4 units) the upper limits are positive (0.145 and
0.184) but the 6-D performance is not (normalised -12.048 and -2.915, random halves -7.282), so a
threshold at 70% of the random-half value has no meaning either. Which half is anterior is also not
known: with prefix 1 as PMd the anterior half is lower in raw performance (-1.535 against -1.087), with
the arrays swapped it is higher.
""")
setmd("**Result: not reproduced, resting on the assumptions O1a and the array mapping.**", """
**Result: blocked (metadata_insufficient): the outcome depends on which array is anterior, which the
file does not say.** Under O1a 44 of 72 prefix-1 units (0.611) and 49 of 70 prefix-2 units (0.700) pass
the > 5 spikes/s rule (Fisher p = 0.293). With prefix 1 as PMd the anterior fraction is lower, not
reproduced in all 12 readings; with prefix 2 as PMd it is higher without significance, partially
reproduced in all 12 (Fisher p 0.293 to 1.000). Under O1b 4 of 72 and 4 of 70 pass. Units whose range is
above the 95th percentile of its condition-shuffled null are 7 of 72 and 6 of 70, and with condition
labels shuffled 82 to 96 units pass the O1a rule (noise reference), so under O1a these counts mostly
measure noise.
""")
setmd("**Result: not reproduced.** The peri-movement space is more consistent", """
**Result: not reproduced.** Over the six O3/O4 settings, both O1 readings and raw or z-scored axes (72
comparisons) the peri-movement space is more consistent in 46: than endpoints + max. speed in 24 of 24,
than the kinematic space at its best k in 21 of 24, but than segment directions in only 1 of 24 (main
reading 0.416 against 0.525; O1b with O3a and O4a 0.545 against 0.615).
""")
# summary
i=find("## Summary")
s=''.join(cells[i]['source'])
rep={"| fig4-broad-near-zero | partially reproduced (assumption O1a) |":"| fig4-broad-near-zero | not reproduced (assumption O1a) |",
"| fig4e-correlation-time-course | reproduced (assumption O1a) |":"| fig4e-correlation-time-course | reproduced (assumption O1a; noise also passes) |",
"| suppfig1-population-averages-lose-tuning | reproduced |":"| suppfig1-population-averages-lose-tuning | reproduced (noise passes in 11 of 20 shuffles) |",
"| fig6d-perimovement-best-j-array | reproduced (assumptions O1a, O3a, O4a) |":"| fig6d-perimovement-best-j-array | partially reproduced (assumption O1a) |",
"| fig7a-shuffled-space-poor | reproduced |":"| fig7a-shuffled-space-poor | reproduced (weak: under O1a the intact space is below zero) |",
"| fig7c-anterior-posterior-performance | not reproduced (assumption: array identity as AP location) |":"| fig7c-anterior-posterior-performance | blocked: other (upper limit at or below zero; normalisation undefined) |",
"| prep-activity-more-anterior | not reproduced (assumptions O1a and the array mapping) |":"| prep-activity-more-anterior | blocked: metadata insufficient (which array is anterior) |",
"""Condition means are therefore noisy (median split-half reliability of
preparatory tuning 0.20), and under the range reading of tuning every PD space performs below zero.""":
"""Condition means are therefore noisy (median split-half reliability of
preparatory tuning 0.20): with condition labels shuffled, about as many units pass the > 5 spikes/s range
rule as with the true labels, and the fig4e and suppfig1 criteria are met by trial noise. Under the range
reading of tuning every PD space performs below zero, though above a shuffled-label null.""",
"""7 or 8 units with clearer tuning, and on them the peri-movement space performs best with positive
performance, as in the paper.""":"""7 or 8 units with clearer tuning, and on them the peri-movement space built from all recorded units
performs best with positive performance, as in the paper; built from those 7 or 8 units only, it does not.""",
"""The anterior-posterior claims use array identity, as the electrodes have
no positions.""":"""The anterior-posterior claims use array identity, as the electrodes have
no positions, and the file does not say which array is PMd.""",
"""  prefixes (72 units with 1, 70 with 2) and the dataset describes recordings from M1 and PMd; no unit
  points to an M1 electrode.""":"""  prefixes (72 units with 1, 70 with 2) and the dataset describes recordings from M1 and PMd; no unit
  points to an M1 electrode, and nothing in the file says which prefix is PMd."""}
for a,b in rep.items():
    assert a in s,a; s=s.replace(a,b)
cells[i]['source']=s.splitlines(keepends=True)
json.dump(nb, open(path,'w'), indent=1, ensure_ascii=False); open(path,'a').write("\n")
PYEOF
python $TMPDIR/apply2.py && python - <<'EOF'
import nbformat
p='entries/000140-churchland-2010/reproduce_churchland_2010.ipynb'
nb=nbformat.read(p,as_version=4)
nbformat.validator.normalize(nb) if hasattr(nbformat.validator,'normalize') else None
import uuid
for c in nb.cells:
    if 'id' not in c: c['id']=uuid.uuid4().hex[:8]
nbformat.write(nb,p)
EOF
git diff --stat; grep -c '"id"' entries/000140-churchland-2010/reproduce_churchland_2010.ipynb
```

```
/opt/hostedtoolcache/Python/3.13.17/x64/lib/python3.13/site-packages/nbformat/validator.py:434: MissingIDFieldWarning: Cell is missing an id field, this will become a hard error in future nbformat versions. You may want to use `normalize()` on your notebooks before validations (available since nbformat 5.1.4). Previous versions of nbformat are fixing this issue transparently, and will stop doing so in the future.
  _validate(nbdict, ref, version, version_minor, relax_add_props)
 entries/000140-churchland-2010/maze_prep.py        |  14 +-
 .../reproduce_churchland_2010.ipynb                | 546 +++++++++++++++------
 2 files changed, 418 insertions(+), 142 deletions(-)
74
```

**Agent calls Bash**

```bash
cd  git diff entries/ | grep "^[-+]" | grep -n "—\|rather" ; cat entries/000140-churchland-2010/README.md; date -u
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
| Correlations broad and centred near zero | Partially reproduced (assumption) |
| Correlation falls to near zero by movement onset | Reproduced (assumption) |
| Population averages lose preparatory tuning by movement onset | Reproduced |
| PD performance best in the peri-movement space, J-array | Reproduced (assumptions) |
| The same for monkeys A, B and J | Blocked: data missing |
| Peri-movement space best at each dimensionality | Not reproduced |
| Endpoints + max. speed space performs poorly in the maze task | Not reproduced (assumption) |
| Performance rises with dimensionality, then declines above 10 | Not reproduced (assumption) |
[... 27 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python - <<'EOF'
p='entries/000140-churchland-2010/README.md'
s=open(p).read()
rep={"| Correlations broad and centred near zero | Partially reproduced (assumption) |":"| Correlations broad and centred near zero | Not reproduced (assumption) |",
"| Correlation falls to near zero by movement onset | Reproduced (assumption) |":"| Correlation falls to near zero by movement onset | Reproduced (assumption; trial noise also passes) |",
"| Population averages lose preparatory tuning by movement onset | Reproduced |":"| Population averages lose preparatory tuning by movement onset | Reproduced (trial noise passes about half the time) |",
"| PD performance best in the peri-movement space, J-array | Reproduced (assumptions) |":"| PD performance best in the peri-movement space, J-array | Partially reproduced (assumption) |",
"| Shuffled peri-movement space performs poorly | Reproduced |":"| Shuffled peri-movement space performs poorly | Reproduced (weak) |",
"| Peri-movement space works at anterior and posterior sites | Not reproduced (assumption) |":"| Peri-movement space works at anterior and posterior sites | Blocked: other (normalisation undefined) |",
"| Preparatory activity more prevalent at anterior sites | Not reproduced (assumption) |":"| Preparatory activity more prevalent at anterior sites | Blocked: metadata insufficient (which array is anterior) |",
"""preparatory tuning 0.20), and when tuning is read as the range across conditions every preferred
direction space performs below zero.""":"""preparatory tuning 0.20). With condition labels shuffled about as many units pass the 5 spikes/s range
rule as with the true labels, and the two time-course criteria (Figure 4E, Supplemental Figure 1) are
met by trial noise. When tuning is read as the range across conditions every preferred direction space
performs below zero.""",
"""electrodes have no positions, so the anterior-posterior claims use the array read from the unit ids.""":
"""electrodes have no positions, so the anterior-posterior claims use the array read from the unit ids;
the file does not say which array is PMd.""",
"the analysis, about two minutes.":"the analysis, about four minutes."}
for a,b in rep.items():
    assert a in s,a; s=s.replace(a,b)
open(p,'w').write(s)
EOF
date -u; python tools/entry.py all entries/000140-churchland-2010 2>&1 | tail -3; date -u
```

```
Thu Oct 29 01:14:13 UTC 2026
Installed kernelspec registry-000140-churchland-2010 in executed/000140-churchland-2010/.venv/share/jupyter/kernels/registry-000140-churchland-2010
0 error(s)
pass  reproduce_churchland_2010.ipynb  (232 s)
Thu Oct 29 01:18:40 UTC 2026
```

**Agent**

The notebook passes in 232 s. Quick check that the numbers cited in the conclusions match this run:

**Agent calls Bash**

```bash
cd executed/000140-churchland-2010; python - <<'EOF'
import json
nb=json.load(open('reproduce_churchland_2010.ipynb'))
txt='\n'.join(''.join(''.join(o.get('text','')) for o in c.get('outputs',[])) for c in nb['cells'] if c['cell_type']=='code')
for k in ["units passing > 5 spikes/s range 82 to 96","fig4e passes (a) 18, (b) 20; suppfig1 passes 11","IQR of r 0.069 to 0.422","fig4e passes (a) 4, (b) 9 of 12; suppfig1 passes 2","p range 0.47 to 0.98","null peri best -0.214 to -0.092, kinematic best -0.138 to -0.108","comparisons with peri higher: 46 of 72","O1 SD ratios: 0.471 to 0.761","normalised readings passing: 18 of 18"]:
    print(k in txt, k)
EOF
```

```
True units passing > 5 spikes/s range 82 to 96
True fig4e passes (a) 18, (b) 20; suppfig1 passes 11
True IQR of r 0.069 to 0.422
True fig4e passes (a) 4, (b) 9 of 12; suppfig1 passes 2
True p range 0.47 to 0.98
True null peri best -0.214 to -0.092, kinematic best -0.138 to -0.108
True comparisons with peri higher: 46 of 72
True O1 SD ratios: 0.471 to 0.761
True normalised readings passing: 18 of 18
```

**Agent**

Numbers match. Now the attempt record: I'm replacing the changed outcome blocks and adding the verification round.

**Agent calls Bash**

```bash
cd  cat > $TMPDIR/rec.py <<'PYEOF'
import re
p='attempts/000140-churchland-2010-01.yaml'
s=open(p).read()
head, rest = s.split("outcomes:\n",1)
outs, tail = rest.split("findings:\n",1)
blocks = re.split(r'(?m)^(?=- claim: )', outs)
blocks = [b for b in blocks if b.strip()]
byid = {re.match(r'- claim: (\S+)', b).group(1): b for b in blocks}
order = [re.match(r'- claim: (\S+)', b).group(1) for b in blocks]
NEW = {}
NEW["fig4d-mean-correlation-j-array"] = byid["fig4d-mean-correlation-j-array"].replace(
"""    r 0.011 (p = 0.662). Under O1 SD""","""    r 0.011 (p = 0.662). With condition labels shuffled across trials (20 shuffles, no tuning) the
    mean r is -0.106 to 0.074, so the main value is within what trial noise gives. Under O1 SD""")
NEW["fig4-broad-near-zero"] = """- claim: fig4-broad-near-zero
  outcome: not_reproduced
  assumed: true
  notebook: reproduce_churchland_2010.ipynb
  output: claim:fig4-broad-near-zero
  notes: Under O1 range (12 readings) the median r is near zero (-0.098 to 0.016), 92% to 100% of
    units have |r| < 0.5, at most 1.2% are above 0.8 and none below -0.8, but the interquartile range
    is 0.173 to 0.286, below the 0.3 the criterion requires, in every O1 range reading. The criterion
    has no partial rule, and the condition that fails is the one that tests the breadth the claim
    states. The conditions that hold are also met by noise. With condition labels shuffled (20
    shuffles) the IQR is 0.069 to 0.422 and the mean r -0.106 to 0.074. Under O1 SD (3 to 5 units)
    all 6 readings pass.
  deviations:
  - Assumed O1 is the range of the preparatory rate across conditions, as the Methods describe the
    inclusion rule as a rate difference ("Firing rate modulation was typically lower ... >5 spikes/s
    of preparatory tuning"); under the SD reading the claim is reproduced, on 3 to 5 units.
"""
NEW["fig4e-correlation-time-course"] = """- claim: fig4e-correlation-time-course
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
    uses the movement-locked part.
"""
NEW["suppfig1-population-averages-lose-tuning"] = """- claim: suppfig1-population-averages-lose-tuning
  outcome: reproduced
  notebook: reproduce_churchland_2010.ipynb
  output: claim:suppfig1-population-averages-lose-tuning
  notes: In all 36 readings, normalised and not, the spread between the strongest and weakest
    preparatory conditions at movement onset is below half the preparatory spread (ratio 0.186 in the
    main normalised reading; -0.175 to 0.295 over readings), with the strongest trace on top at -150
    ms. Trial noise also meets the criterion. With condition labels shuffled it is met in 11 of 20
    shuffles, and with the preparatory and movement-locked means from disjoint trials in 2 of 12
    readings, so the strongest trace being on top at -150 ms comes mostly from noise shared within the
    same trials, and the pass carries little evidence.
  deviations:
  - Each unit is normalised by its maximum condition-mean rate over the go-locked and movement-locked
    spans stored (-300 to +200 ms and -400 to +900 ms); the legend says "normalizing each neuron's
    activity by its maximum rate".
"""
NEW["fig6d-perimovement-best-j-array"] = """- claim: fig6d-perimovement-best-j-array
  outcome: partially_reproduced
  assumed: true
  notebook: reproduce_churchland_2010.ipynb
  output: claim:fig6d-perimovement-best-j-array
  notes: Main reading (O1 range, O3a, O4a; 93 units) best peri-movement performance -0.044 at k = 2,
    best kinematic -0.053, best task space (initial velocity) -0.048. Of 96 readings 64 meet the
    criterion and 32 are partial (initial velocity or kinematic at or above the peri-movement space),
    the partial ones under O1 range with O3a and O4b, O3b and O4a, or O3b and O4b, and under O1 SD
    with O3b and O4b. The criterion asks that it hold under each reading, so the outcome is partial.
    The differences are small against their spread. In no reading is the peri-movement space better
    than the best other space at p < 0.05 (paired t p 0.47 to 0.98; main difference 0.004, SE
    0.018). With the T matrix built from the included units only, O1 range gives the same (reproduced
    or partial in each of 6 settings), while under O1 SD the peri-movement space falls to -0.022 to
    0.101 and 6 to 8 spaces match or beat it. Under O1 range all spaces perform below zero, worse than
    predicting the mean rate, but above a condition-shuffled null (peri-movement -0.214 to -0.092,
    kinematic -0.138 to -0.108). Under O1 SD (8 units, T of all units) the peri-movement space is
    best with positive performance, 0.209 against 0.136 kinematic and 0.133 task. Repeating the
    kinematic variables (reading a) leaves performance unchanged (largest difference 8e-15).
  deviations:
  - Assumed O1 range (see fig4-broad-near-zero). Under O1 SD with the T matrix of the included units
    the claim is not reproduced; under O1 range every reading gives reproduced or partial.
  - The units of the peri-movement T matrix are read two ways, all recorded units (main) and the units
    passing the inclusion rule. The Methods say each row "contained data from all neurons except the
    neuron whose preparatory activity we were trying to capture" and that "Analysis of preparatory
    responses was restricted to neurons with at least 10 spikes/s of preparatory tuning".
  - The upper limit uses the preparatory matrix of all units except the fitted one, as the
    peri-movement space does (Methods, PCA-based spaces); the supplement says "all neurons".
  - Task spaces follow the Methods' list (Task spaces). Details they leave open, set here and stated
    in maze_prep.py, are the end of the reach (last time within 800 ms of onset with speed at least
    10% of peak), the peak velocity components (the signed value of largest magnitude), and the
    segments (equal path length, with equal duration as a variant, which gives the same outcome).
  - Acceleration for the kinematic space is the derivative of the dataset's hand velocity after a
    20 ms Gaussian, a standard choice.
"""
NEW["fig6-maze-endpoint-speed-space-poor"] = """- claim: fig6-maze-endpoint-speed-space-poor
  outcome: not_reproduced
  assumed: true
  notebook: reproduce_churchland_2010.ipynb
  output: claim:fig6-maze-endpoint-speed-space-poor
  notes: Under O1 range (12 readings) the endpoints + max. speed space (-0.126 to -0.147) is below the
    3-D peri-movement space by 0.011 to 0.065, less than the 0.1 required (main reading -0.143 against
    -0.104, SE of the per-unit difference 0.025). Under O1 SD all 12 readings pass with the T matrix of
    all recorded units (-0.040 to 0.018 against 0.101 to 0.209); with the T matrix of the 7 or 8
    included units the 3-D peri-movement space gives -0.088 to 0.045 and none of the 6 settings passes.
  deviations:
  - Assumed O1 is the range across conditions (see fig4-broad-near-zero); under the SD reading with
    the T matrix of all recorded units the claim is reproduced.
"""
NEW["fig7a-shuffled-space-poor"] = """- claim: fig7a-shuffled-space-poor
  outcome: reproduced
  notebook: reproduce_churchland_2010.ipynb
  output: claim:fig7a-shuffled-space-poor
  notes: In all 24 readings (six O3/O4 settings, O1 range and SD, the coin per unit and condition or
    per condition) the mean best performance over 20 shuffles is below half the intact best and below
    the best kinematic performance. Main reading -0.097 against -0.044 intact and -0.053 kinematic.
    Under O1 range the intact space is itself below zero, so below half the intact best is met
    trivially. The evidence is the O1 SD readings (7 or 8 units), where the shuffled mean is -0.065 to
    0.041 against an intact 0.129 to 0.249.
"""
NEW["fig7b-window-start-slide"] = """- claim: fig7b-window-start-slide
  outcome: not_reproduced
  notebook: reproduce_churchland_2010.ipynb
  output: claim:fig7b-window-start-slide
  measured: 0.501
  notes: Under O1 SD the ratio of performance with the window starting at movement onset to that at
    -150 ms is 0.471 to 0.761 in the 6 O3/O4 settings, outside 0.97 +/- 0.097 (main settings 0.209 to
    0.105, ratio 0.501). Under O1 range performance at -150 ms is below zero (-0.046 to -0.023), so the
    ratio is undefined; it falls from there to -0.059 to -0.046 at onset. Only the monkey J value under
    reading (a) can be computed; the monkeys A and B value (0.94) is not in the dandiset.
  deviations:
  - Start times -150 to +100 ms in 50 ms steps, end fixed at +800 ms, best k up to 14 for each start
    (Figure 7B legend, "the best dimensionality for that dataset/start-time").
"""
NEW["ap-location-no-effect-j-array"] = byid["ap-location-no-effect-j-array"].replace(
"""(p 0.538 to
    1.000). Main reading r = 0.105, p = 0.668, 10 PMd and 9 M1 units (mean r -0.060 and
    -0.099).""","""(p 0.538 to
    1.000). Main reading r = 0.105, p = 0.668, 10 PMd and 9 M1 units (mean r -0.060 and
    -0.099). The outcome holds under either mapping of the arrays; swapping them changes only the
    sign of r.""")
assert NEW["ap-location-no-effect-j-array"]!=byid["ap-location-no-effect-j-array"]
NEW["fig7c-anterior-posterior-performance"] = """- claim: fig7c-anterior-posterior-performance
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
"""
NEW["prep-activity-more-anterior"] = """- claim: prep-activity-more-anterior
  outcome: blocked
  blocked_by: metadata_insufficient
  notebook: reproduce_churchland_2010.ipynb
  output: claim:prep-activity-more-anterior
  notes: The outcome depends on which array is anterior, and neither the file nor the archive's
    metadata says which unit-id prefix is PMd (every unit's electrodes entry points to the PMd group
    for both prefixes). Under O1 range 44 of 72 prefix-1 units (0.611) and 49 of 70 prefix-2 units
    (0.700) pass the > 5 spikes/s rule (Fisher p = 0.293). With prefix 1 as PMd the anterior fraction
    is lower, not reproduced in all 12 readings; with prefix 2 as PMd it is higher without
    significance, partially reproduced in all 12 (Fisher p 0.293 to 1.000). Under O1 SD 4 of 72 and 4
    of 70. Units whose range exceeds the 95th percentile of a condition-shuffled null are 7 of 72 and
    6 of 70, and with condition labels shuffled 82 to 96 units pass the O1 range rule, so under O1
    range these counts mostly measure noise. Median preparatory range is 6.58 spikes/s on the prefix-1
    array and 10.19 on the prefix-2 array, and the mean preparatory rate 2.40 and 3.73 spikes/s.
  deviations:
  - AP location is the array, PMd anterior and M1 posterior (Supplemental Figure 3 legend); both
    mappings of the unit-id prefixes to the arrays are run.
"""
NEW["fig7d-pd-consistency"] = """- claim: fig7d-pd-consistency
  outcome: not_reproduced
  notebook: reproduce_churchland_2010.ipynb
  output: claim:fig7d-pd-consistency
  notes: Over the six O3/O4 settings, both O1 readings and raw or z-scored axes (72 comparisons) the
    peri-movement space is more consistent in 46. It is more consistent than endpoints + max. speed in
    24 of 24 (main reading 0.617 against 0.523) and than the kinematic space at its best k in 21 of 24
    (main, k = 1, 0.587 against 0.563), but than segment directions at k = 6 in only 1 of 24 (main
    0.416 against 0.525; O1 SD with O3a and O4a 0.545 against 0.615).
  deviations:
  - The paper does not give the scale of task-space axes, which sets a PD's direction when units are
    mixed (mm and mm/s); raw and z-scored axes are both run and agree on the segment-directions
    comparison in 23 of 24 readings.
  - Draws in which the unit's rate is the same in all drawn conditions (a zero PD) are dropped; 100
    repeats per unit, the claim's standard choice.
"""
b=byid["fig8-linear-dynamics-simulation"]
b=b[:b.index("  deviations:")]
NEW["fig8-linear-dynamics-simulation"]=b
out = "".join(NEW.get(k, byid[k]) for k in order)
# findings
tail = tail.replace("""Four claims cannot be tested, and the claims that were tested rest on condition means
    whose split-half reliability has a median of 0.20.""","""Four claims cannot be tested, and the claims that were tested rest on condition means
    whose split-half reliability has a median of 0.20. With condition labels shuffled across trials,
    82 to 96 of the 142 units pass the paper's > 5 spikes/s inclusion rule (read as the range), against
    93 with the true labels; the paper justified that threshold by its high trial count.""")
tail = tail.replace("""Figure 7D? Did the upper-limit space of the supplement include the fitted neuron?""",
"""Figure 7D? Did the upper-limit space of the supplement include the fitted neuron, and did the
    peri-movement T matrix use all recorded neurons or only those passing the inclusion rule? Under
    the SD reading of tuning the fig6d result here depends on it.""")
assert "82 to 96" in tail and "T matrix use all" in tail
open(p,'w').write(head+"outcomes:\n"+out+"findings:\n"+tail)
PYEOF
python $TMPDIR/rec.py && git diff --stat attempts/
```

```
Exit code 1
Traceback (most recent call last):
  File "/tmp/claude-1001/rec.py", line 150, in <module>
    assert NEW["ap-location-no-effect-j-array"]!=byid["ap-location-no-effect-j-array"]
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError
```

**Agent calls Bash**

```bash
cd  python - <<'EOF'
import os
p=os.environ['TMPDIR']+'/rec.py'; s=open(p).read()
s=s.replace('''"""(p 0.538 to
    1.000). Main reading r = 0.105, p = 0.668, 10 PMd and 9 M1 units (mean r -0.060 and
    -0.099).""","""(p 0.538 to
    1.000). Main reading r = 0.105, p = 0.668, 10 PMd and 9 M1 units (mean r -0.060 and
    -0.099). The outcome''','''"""(mean r -0.060 and
    -0.099).""","""(mean r -0.060 and
    -0.099). The outcome''')
open(p,'w').write(s)
EOF
python $TMPDIR/rec.py && git diff --stat attempts/
```

```
attempts/000140-churchland-2010-01.yaml | 165 +++++++++++++++++++-------------
 1 file changed, 96 insertions(+), 69 deletions(-)
```

**Agent**

Now the verifications block.

**Agent calls Bash**

```bash
cd  tail -5 attempts/000140-churchland-2010-01.yaml; cat >> attempts/000140-churchland-2010-01.yaml <<'EOF'
verifications:
- date: 2026-10-29
  kind: agent
  by: Independent agent run by CatalystNeuro (same harness, separate context, did not write the
    notebook), verifier-1
  reviewed: The handover of the first run, the executed notebook with the conclusions and summary
    removed, the helper module and the claims file, with the paper under paper/ and the archive's
    API.
  results:
  - claim: fig4d-mean-correlation-j-array
    agrees: true
    outcome: not_reproduced
    reason: None of the 18 runnable readings has a positive mean at p<0.05. Mean r runs from -0.148 to
      0.095, and the main reading gives -0.079 (n=19). Low power (split-half reliability 0.20/0.28)
      means this is a failure to detect, not evidence against.
    response: Outcome kept. A condition-shuffled null (20 shuffles) is added; its mean r is -0.106 to
      0.074, and the notes say the main value is within what trial noise gives.
  - claim: fig4abc-mean-correlation-other-datasets
    agrees: true
    outcome: blocked
    reason: The archive API shows 1 subject (Jenkins), 2 files and no EMG. None of the A, B or
      single-electrode J data is there.
    response: None needed.
  - claim: fig4-broad-near-zero
    agrees: false
    outcome: not_reproduced
    reason: Every range (O1a) reading fails the IQR >= 0.3 test (IQR 0.17-0.29). The only passes are
      the SD readings, with n = 3-5 units. An IQR near 0.26 is what pure noise gives with 27
      conditions.
    response: Outcome changed from partially_reproduced to not_reproduced. The criterion has no partial
      rule, and the condition that fails is the one that tests breadth. The notebook now shows the
      condition-shuffled null, whose IQR is 0.069 to 0.422, so the conditions that hold are also met
      by noise.
  - claim: fig4e-correlation-time-course
    agrees: true
    outcome: reproduced
    reason: 18/30 readings pass, including every O1a reading (r falls from 0.30-0.41 at -200 ms to
      about 0 at onset). Criterion met, but not informative. A noise-only simulation passes the same
      test, so the data cannot separate this from shared trial noise. The go+100 ms end of the
      preparatory window sits about 200 ms before movement onset (problem 1).
    response: Outcome kept, and the conclusion and notes now say the pass carries little evidence. The
      notebook adds the noise baseline asked for, on the data. With condition labels shuffled the
      criterion is met in 18 of 20 shuffles (fig4 units) and 20 of 20 (all units). With the
      preparatory and movement-locked means from disjoint trials, r at -200 ms is 0.12 to 0.18 and the
      criterion is met in 4 of 12 and 9 of 12 readings.
  - claim: suppfig1-population-averages-lose-tuning
    agrees: true
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
      SEs or paired tests were output (problem 3). The peri T matrix uses all 142 recorded units,
      untuned ones included; the Methods' "all neurons" could mean recorded or included neurons, and
      only the first reading was run (problem 6).
    response: Outcome changed from reproduced to partially_reproduced, as the criterion asks that it
      hold under each reading. Added per-reading SEs and paired t-tests (no reading has the
      peri-movement space better at p < 0.05, p 0.47 to 0.98), the T matrix of the included units as
      a second reading (same outcome under O1a; under O1b the peri-movement space loses to 6 to 8
      spaces, so the outcome still rests on O1a), and a condition-shuffled null (data above it).
  - claim: fig6abc-perimovement-best-other-datasets
    agrees: true
    outcome: blocked
    reason: Confirmed on the archive, no single-electrode data, no EMG.
    response: None needed.
  - claim: fig6-perimovement-best-each-dimensionality
    agrees: true
    outcome: not_reproduced
    reason: 0/96 readings reach 0.8; fractions are 0.07-0.36.
    response: None needed. The outcome does not rest on small differences (0.36 at most against the
      0.8 required).
  - claim: fig6-maze-endpoint-speed-space-poor
    agrees: true
    outcome: not_reproduced
    reason: Under O1a the gap to the 3-D peri space is only 0.01-0.07, short of the 0.1 required. All
      12 O1b readings pass, so the outcome depends on the stated O1a assumption. Decided by mean
      differences with no SE or test per reading (problem 3).
    response: Outcome kept. The notebook adds the SE and a paired test of each difference, and the O1b
      readings with the T matrix of the included units, under which none passes.
  - claim: fig6-dimensionality-trend
    agrees: true
    outcome: not_reproduced
    reason: Under O1a the best k is 2, so there is no rise. The decline holds everywhere (-44 at
      k=20), but that alone is not the partial outcome. 3 of the 6 O1b readings pass.
    response: None needed.
  - claim: fig6e-summary-rank
    agrees: true
    outcome: blocked
    reason: There is no EMG and no A/B/J data. The J-array variant ranks peri top but not significantly
      above kinematic or initial vel., and all means are negative.
    response: None needed.
  - claim: prep-dimensionality-7-to-10
    agrees: true
    outcome: not_reproduced
    reason: 16-17 components under O1a and 5-6 under O1b; none fall in 6.3-11. Shuffling condition
      labels gives 17, so the O1a count measures noise. The O1b count is capped by the 7-8 units.
    response: None needed.
  - claim: fig7a-shuffled-space-poor
    agrees: true
    outcome: reproduced
    reason: 12/12 pass, a weak result. Under O1a the intact best is negative, so below half of intact
      is satisfied trivially. The real evidence is O1b (8 units), 0.209 intact vs -0.06 shuffled. Run
      on 3 of the six O3/O4 configurations only (problem 5).
    response: Outcome kept. The cell now runs all six O3/O4 settings (24 of 24 pass), and the
      conclusion says the O1a comparison is trivial and the evidence is the O1b readings.
  - claim: fig7b-window-start-slide
    agrees: true
    outcome: not_reproduced
    reason: 0/6 ratios within 0.97+/-0.097. The O1b ratios are 0.50-0.76; the O1a ratios divide
      negative numbers and mean nothing. The A/B part (0.94) cannot be tested on this dandiset. Run on
      3 of the six O3/O4 configurations only (problem 5).
    response: Outcome kept. The cell now runs all six settings and leaves the ratio undefined when
      performance at -150 ms is not above zero. The O1b ratios are 0.471 to 0.761, and the measured
      value is now the O1b main ratio (0.501), not the undefined O1a one.
  - claim: ap-location-no-effect-j-array
    agrees: true
    outcome: reproduced
    reason: p >= 0.05 in 17/17 readings, and swapping the arrays only flips the sign. Low power and a
      proxy, AP location is reduced to array identity, and n is 19 under the main reading.
    response: Outcome kept. The swapped regression r is now printed in the table.
  - claim: ap-location-no-effect-other-datasets
    agrees: true
    outcome: blocked
    reason: Confirmed on the archive.
    response: None needed.
  - claim: fig7c-anterior-posterior-performance
    agrees: false
    outcome: blocked
    reason: The upper limit is <= 0 in 8/10 rows, so the normalised measure the criterion uses does not
      exist. Raw 6-D performance is about -1.1 to -1.5 at both sites. Which array is anterior is also
      unverified, and the swap promised in the notebook is missing from this cell (problem 4).
    response: Outcome changed from not_reproduced to blocked (other), because the criterion's
      normalised measure is undefined. The cell now prints the raw performance of each half under both
      mappings, and O1b random halves (normalised -7.282, with both arrays' units negative too).
  - claim: prep-activity-more-anterior
    agrees: false
    outcome: blocked
    reason: With prefix 1 taken as PMd, PMd 0.61 vs M1 0.70 (p=0.29) is not_reproduced; with the arrays
      swapped it would be partially_reproduced. Neither the file nor the API metadata says which array
      is which, and every unit's electrode index points to the PMd group for both prefixes, so the
      prefix 1 = PMd reading has no support in the file (problem 4).
    response: Outcome changed from not_reproduced to blocked (metadata_insufficient). The cell now
      prints the outcome under both mappings (not reproduced in 12 of 12 readings with prefix 1 as
      PMd, partial in 12 of 12 with prefix 2), and the section text no longer claims support for the
      mapping beyond the order of the electrode groups.
  - claim: fig7d-pd-consistency
    agrees: true
    outcome: not_reproduced
    reason: Peri wins only 7 of 12 comparisons and loses to segment dirs. in all 4. The cell used 2 of
      the six O3/O4 configurations and O1a only; O1b changed other outcomes and fig7d under O1b was not
      run (problem 5).
    response: Outcome kept. The cell now runs all six settings under both O1 readings (72 comparisons);
      segment directions beat the peri-movement space in 23 of 24, under O1b as under O1a.
  - claim: fig8-linear-dynamics-simulation
    agrees: true
    outcome: reproduced
    reason: Median |r| is 0.11 (disk) and 0.15 (square), below 0.3; median r 0.004/0.012 is within
      0.08+/-0.3; minimum PD performance is 1.0. The simulate_rotation docstring mentions a hold that
      is never applied (problem 7).
    response: Outcome kept. The hold parameter is removed from simulate_rotation and its docstring
      says why no hold is simulated; the deviation about a hold is removed from the record.
EOF
python tools/entry.py check entries/000140-churchland-2010 2>&1 | tail -5
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  ls tools; python -c "
import yaml;d=yaml.safe_load(open('attempts/000140-churchland-2010-01.yaml'));print(len(d['outcomes']),len(d['verifications'][0]['results']))"; grep -n "—\|rather" attempts/000140-churchland-2010-01.yaml entries/000140-churchland-2010/README.md entries/000140-churchland-2010/maze_prep.py; awk '/^verifications:/{f=1} f' attempts/000140-churchland-2010-01.yaml | grep -n "^      .*: " | head
```

```
__pycache__
agent_run.py
archive_transcripts.sh
archives
blind.sh
build_dryad_targets.py
build_figshare_targets.py
build_openneuro_targets.py
build_site.py
build_targets.py
claims_check.py
conversion_issue.py
datasets.py
entry.py
flagged.py
get_papers.sh
notify.py
paper_match.py
papers_manifest.py
progress.py
[... 8 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n "attempt.schema\|verifications\|def check" tools/entry.py | head; grep -rn "rather\|—" entries/000140-churchland-2010/reproduce_churchland_2010.ipynb | head -3
```

```
121:def check(entry_dir: Path) -> Report:
257:        for rnd in (attempt.get("verifications") or [])[1:]:
```

**Agent calls Bash**

```bash
cd  sed -n 121,140p tools/entry.py; grep -n "schema" tools/entry.py | head
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

[... 8 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python tools/entry.py handover entries/000140-churchland-2010 2>&1 | tail -2; git status --short; date -u
```

```
wrote executed/000140-churchland-2010/handover
 M attempts/000140-churchland-2010-01.yaml
 M entries/000140-churchland-2010/README.md
 M entries/000140-churchland-2010/maze_prep.py
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
Thu Oct 29 01:21:16 UTC 2026
```

**Agent**

I've revised the attempt for verifier round 1. The entry re-ran cleanly (`entry.py all`: 0 errors, notebook passes in 232 s), every number in the conclusions matches the new run, and `check` passes. Nothing is committed.

**Outcome changes (four, all as the verifier gave them)**
- **fig4-broad-near-zero**: partially_reproduced → not_reproduced. The criterion has no partial rule, and the condition that fails (interquartile range of r at least 0.3) is the one that tests breadth. The conditions that pass are also met when condition labels are shuffled.
- **fig6d-perimovement-best-j-array**: reproduced → partially_reproduced (still resting on the range reading of "tuning", O1a). The criterion must hold under every reading, and 32 of 96 readings are partial. No reading shows the peri-movement space ahead at p < 0.05 (p 0.47 to 0.98).
- **fig7c-anterior-posterior-performance**: not_reproduced → blocked (`other`). The upper limit used for normalising is at or below zero, so the normalised measure the criterion needs does not exist.
- **prep-activity-more-anterior**: not_reproduced → blocked (`metadata_insufficient`). The result flips with which array is PMd: not reproduced if prefix 1 is PMd, partial if prefix 2 is, in all 12 readings each way. Nothing in the file says which.

All other outcomes are unchanged and the verifier agreed with them.

**What I added or corrected**
- **Noise checks on the data** (problems 1 and 2):
  - With condition labels shuffled, 82 to 96 units pass the > 5 spikes/s range rule, against 93 with the true labels.
  - Shuffled labels meet the fig4e criterion in 18 to 20 of 20 shuffles and the suppfig1 criterion in 11 of 20.
  - With preparatory and peri-movement means taken from separate trials, fig4e is met in 4 to 9 of 12 readings (correlation at -200 ms only 0.12 to 0.18), and suppfig1 in 2 of 12.
  - fig4e and suppfig1 stay reproduced, but their conclusions and notes now say the pass carries little evidence. The selection-noise result is added to the `data_missing` finding.
- **Spread of the comparisons** (problem 3): fig6d and fig6-maze now print SEs and paired tests. Against a shuffled-label null, the fig6d performances are above noise even though below zero. fig7b leaves the ratio undefined when performance is not positive; its recorded value is now the SD-reading ratio, 0.501.
- **Second reading of the peri-movement space** (problem 6): the Methods restrict preparatory analyses to included units, so I also built the space from the included units only. Under the range reading this changes nothing. Under the SD reading the peri-movement space loses its lead in fig6d and fig6-maze. That reading is now a deviation, and the question is added to the `methods_unavailable` finding.
- **Array mapping** (problem 4): the anterior-posterior cells print results under both mappings, and the text no longer claims support for prefix 1 = PMd beyond the order of the electrode groups.
- **Partial runs** (problem 5): fig7a, fig7b and fig7d now cover all six onset/proto-trial settings, and fig7d covers both O1 readings. None changes an outcome: fig7a passes 24 of 24, and in fig7d segment directions beat the peri-movement space in 23 of 24.
- **Docstring** (problem 7): removed the unused `hold` from `simulate_rotation`, and its deviation from the record.
- Updated the notebook header and summary, the README, the attempt notes, and round 1 under `verifications`.

**Not done**
- I added no reader questions: the verifier reported no place where the claims file misreads the paper.
- The verifier's other unchecked items (whether this session is the paper's J-array session, and the figures) need provenance or visual inspection this run can't provide.
- The notebook now takes about 4 minutes instead of 2, mostly from running fig7d on every reading.

## End of run

48 turns, 24 minutes, result: success.
