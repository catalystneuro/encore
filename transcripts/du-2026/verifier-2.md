# du-2026 · verifier-2 · run 44949312683

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  ls -la; ls paper docs 2>/dev/null; cat round-1-report.md
```

```
total 424
drwxr-xr-x 6 runner runner   4096 Nov 21 22:21 .
drwxr-xr-x 8 runner runner   4096 Nov 21 22:21 ..
crw-rw-rw- 1 nobody nogroup  1, 3 Nov 21 21:01 .bash_profile
crw-rw-rw- 1 nobody nogroup  1, 3 Nov 21 21:01 .bashrc
drwxr-xr-x 5 runner runner   4096 Nov 21 22:21 .claude
-rw-r--r-- 1 runner runner      0 Nov 21 22:21 .env
-rw-r--r-- 1 runner runner      0 Nov 21 22:21 .env.development
-rw-r--r-- 1 runner runner      0 Nov 21 22:21 .env.development.local
-rw-r--r-- 1 runner runner      0 Nov 21 22:21 .env.local
-rw-r--r-- 1 runner runner      0 Nov 21 22:21 .env.production
-rw-r--r-- 1 runner runner      0 Nov 21 22:21 .env.production.local
-rw-r--r-- 1 runner runner      0 Nov 21 22:21 .env.test
-rw-r--r-- 1 runner runner      0 Nov 21 22:21 .env.test.local
drwx------ 2 runner runner   4096 Nov 21 22:21 .git
crw-rw-rw- 1 nobody nogroup  1, 3 Nov 21 21:01 .gitconfig
crw-rw-rw- 1 nobody nogroup  1, 3 Nov 21 21:01 .github
-rw-r--r-- 1 runner runner      0 Nov 21 22:21 .gitmodules
crw-rw-rw- 1 nobody nogroup  1, 3 Nov 21 21:01 .idea
crw-rw-rw- 1 nobody nogroup  1, 3 Nov 21 21:01 .mcp.json
[... 99 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat README.md; head -60 du-2026.yaml; echo ----; head -60 du-2026-01.yaml; wc -l paper/*
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  sed -n 60,2000p du-2026-01.yaml
```

```
<persisted-output>
Output too large (33.1KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work--temp-work/4007710a-2704-431a-9262-3e923a1c5224/tool-results/b8b0wfnjv.txt

Preview (first 2KB):
  measured:
  - 0.22451
  - 0.3736
  notes: Weak and strong medians 0.22451 and 0.37360, template-only -0.0000023, strictly increasing.
    The four shifted seed sets give weak 0.21996 to 0.22321 and strong 0.37035 to 0.37368, all ordered
    and within tolerance.
- claim: synthetic-pair-breaking
  outcome: reproduced
  notebook: 01_synthetic.ipynb
  output: claim:synthetic-pair-breaking
  measured:
  - 10
  - -0.3486
  - -0.3663
  notes: In the strong regime correct-pair gain exceeds nearest replacement and the mean of 100
    permutations for 10 of 10 seeds; mean replacement gain -0.3486, mean permutation gain -0.3663.
[... 30 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 60,1000p du-2026.yaml
```

```
<persisted-output>
Output too large (44.8KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work--temp-work/4007710a-2704-431a-9262-3e923a1c5224/tool-results/b1tsc4txl.txt

Preview (first 2KB):
# - LINK contexts (Methods 4.4; link.py). Phase basis 1, sin(r pi tau), cos(r pi tau), r = 1 to 4,
#   tau the within-window phase in [0, 1). Direction is the octant of target minus initial
#   position (code floor(((atan2(dy, dx) + pi) / 2 pi) 8) mod 8). Ladder: phase only (9 features);
#   direction by phase plus phase (81); plus additive target, initial position and displacement
#   (87); plus geometry by phase (141, "geometry by phase", the primary context); plus five past
#   bins of two-dimensional measured finger position ending at the same bin as the neural
#   history (151, "measured-output history"). Quadratic sensitivities add the 21 second-order
#   products of the six geometry variables and their phase interactions (351 and 361 features).
# - MC_RTT (Methods 4.3 and 4.4; mc_rtt.py). Behavior averaged from 1 kHz samples into 20 ms bins,
#   spikes histogrammed on the same grid; five 20 ms spike-count bins over 130 units (650
#   predictors) ending 80 ms before each behavior bin. Headline context is target plus five
#   cursor-position history bins ending at the same 80 ms boundary plus target minus the last
#   history cursor position. Direction octant of the block's mean target error is used for
#   stratification and replacement matching. Blocks use all bins after the warm-up (code; 21
#   bins per block in Table 2).
# - Fully nested estimator (Methods 4.5; nested_estimators.py, evaluate_fully_nested_audit).
[... 7 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work--temp-work/4007710a-2704-431a-9262-3e923a1c5224/tool-results/b8b0wfnjv.txt"
}
```

```
1	  measured:
2	  - 0.22451
3	  - 0.3736
4	  notes: Weak and strong medians 0.22451 and 0.37360, template-only -0.0000023, strictly increasing.
5	    The four shifted seed sets give weak 0.21996 to 0.22321 and strong 0.37035 to 0.37368, all ordered
6	    and within tolerance.
7	- claim: synthetic-pair-breaking
8	  outcome: reproduced
9	  notebook: 01_synthetic.ipynb
10	  output: claim:synthetic-pair-breaking
11	  measured:
12	  - 10
13	  - -0.3486
14	  - -0.3663
15	  notes: In the strong regime correct-pair gain exceeds nearest replacement and the mean of 100
16	    permutations for 10 of 10 seeds; mean replacement gain -0.3486, mean permutation gain -0.3663.
17	    The shifted seed sets give 10 of 10 each, replacement means -0.3514 to -0.3782 and permutation
18	    means -0.3619 to -0.3673, all within tolerance.
19	- claim: link-development-sample
20	  outcome: reproduced
[... 672 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n "^- id:\|^  id:\|id: " du-2026.yaml | head -50; grep -n "maze" -i du-2026.yaml | head -60
```

```
105:- id: synthetic-template-null
128:- id: synthetic-signal-ordering
149:- id: synthetic-pair-breaking
181:- id: link-development-sample
205:- id: link-neural-only-r2
231:- id: link-context-ladder-gain
290:- id: link-context-only-r2
318:- id: link-phase-only-replacement
337:- id: link-task-contrast-by-context
357:- id: nested-geometry-gain
403:- id: nested-history-gain
448:- id: nested-replacement-negative
479:- id: replacement-source-diagnostics
511:- id: permutation-negative
531:- id: replacement-penalty-distance
549:- id: replacement-ranks-lower
567:- id: practical-mse-reduction
611:- id: representative-trial
630:- id: confirm-geometry-gain
661:- id: confirm-history-contraction
[... 31 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 60,104p du-2026.yaml; sed -n 765,982p du-2026.yaml
```

```
# - LINK contexts (Methods 4.4; link.py). Phase basis 1, sin(r pi tau), cos(r pi tau), r = 1 to 4,
#   tau the within-window phase in [0, 1). Direction is the octant of target minus initial
#   position (code floor(((atan2(dy, dx) + pi) / 2 pi) 8) mod 8). Ladder: phase only (9 features);
#   direction by phase plus phase (81); plus additive target, initial position and displacement
#   (87); plus geometry by phase (141, "geometry by phase", the primary context); plus five past
#   bins of two-dimensional measured finger position ending at the same bin as the neural
#   history (151, "measured-output history"). Quadratic sensitivities add the 21 second-order
#   products of the six geometry variables and their phase interactions (351 and 361 features).
# - MC_RTT (Methods 4.3 and 4.4; mc_rtt.py). Behavior averaged from 1 kHz samples into 20 ms bins,
#   spikes histogrammed on the same grid; five 20 ms spike-count bins over 130 units (650
#   predictors) ending 80 ms before each behavior bin. Headline context is target plus five
#   cursor-position history bins ending at the same 80 ms boundary plus target minus the last
#   history cursor position. Direction octant of the block's mean target error is used for
#   stratification and replacement matching. Blocks use all bins after the warm-up (code; 21
#   bins per block in Table 2).
# - Fully nested estimator (Methods 4.5; nested_estimators.py, evaluate_fully_nested_audit).
#   Ridge with predictors standardized on each training scope, penalty grid 0.1, 1, 10, 100, 1e3,
#   1e4, 1e5. LINK outer split 70/30 whole trials stratified by direction (code random_state
#   20260726 for the primary results); NLB uses the release labels. Five condition-stratified
#   nuisance folds; in each, separate context-to-behavior and context-to-neural penalties from an
[... 243 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n "assumed" du-2026-01.yaml; cat > $TMPDIR/dump.py <<'EOF'
import json,sys
nb=json.load(open(sys.argv[1]))
for i,c in enumerate(nb['cells']):
    src=''.join(c['source'])
    print(f"=== cell {i} [{c['cell_type']}]")
    if c['cell_type']=='markdown': print(src)
    else:
        print(src if len(sys.argv)>2 else src[:300])
        for o in c.get('outputs',[]):
            if 'text' in o: print('>>', ''.join(o['text']))
            elif 'data' in o and 'text/plain' in o['data']: print('>>', ''.join(o['data']['text/plain']))
            elif o.get('output_type')=='error': print('ERR', o.get('ename'), o.get('evalue'))
EOF
for f in 0*.ipynb; do python3 $TMPDIR/dump.py $f > $TMPDIR/${f%.ipynb}.txt; wc -l $TMPDIR/${f%.ipynb}.txt; done
```

```
139 /tmp/claude-1001/01_synthetic.txt
732 /tmp/claude-1001/02_link_development.txt
107 /tmp/claude-1001/03_link_estimators.txt
155 /tmp/claude-1001/04_link_temporal_capacity.txt
217 /tmp/claude-1001/05_link_confirmation.txt
149 /tmp/claude-1001/06_mc_rtt.txt
178 /tmp/claude-1001/07_mc_maze.txt
```

**Agent calls Bash**

```bash
cat $TMPDIR/07_mc_maze.txt
```

```
=== cell 0 [markdown]
# Du, Lai, Hu & Ye (2026) on MC_Maze (DANDI:000139, data elsewhere)

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
=== cell 1 [code]
[... 158 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 1,400p $TMPDIR/02_link_development.txt
```

```
<persisted-output>
Output too large (29.7KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work--temp-work/4007710a-2704-431a-9262-3e923a1c5224/tool-results/bl6w1vz1u.txt

Preview (first 2KB):
=== cell 0 [markdown]
# Du, Lai, Hu & Ye (2026) on LINK: development sessions

Paper: Du Z, Lai ZY, Hu L, Ye T. "A Context-Conditional Audit of Trial-Pairing-Dependent Neural
Gain in Motor-Cortex Decoding". bioRxiv preprint posted 2026-08-10,
doi:10.64898/2026.08.04.742876. The claims file (`claims/du-2026.yaml`) was written from that
preprint's full text (main text, legends, Tables 1 to 3, Methods); the supplement was not available.

Dataset: DANDI:001201 (LINK, Temmar et al.), pinned at version **0.251023.2336**, streamed from the
archive. This is the version the paper cites (Methods 4.2, Data availability; protocol, author step
1.3). Two later versions exist (0.261015.2153 and 0.261026.1912); they list the same 312 asset paths
with the same sizes (next cell), so the analysis would read the same files; the pinned version is the cited one.

This notebook tests the claims on the 18 development sessions (nine dates with a CO and an RD
session). Other notebooks of this entry: `01_synthetic.ipynb` (synthetic calibration),
`03_link_estimators.ipynb` (estimator families), `04_link_temporal_capacity.ipynb` (temporal offset
[... 10 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work--temp-work/4007710a-2704-431a-9262-3e923a1c5224/tool-results/bl6w1vz1u.txt",
 "offset": 20
}
```

```
20	
21	| Claim | Where | Status |
22	|---|---|---|
23	| synthetic-template-null, synthetic-signal-ordering, synthetic-pair-breaking | 01 | tested (data generated by the paper's code) |
24	| link-development-sample, link-neural-only-r2, link-context-ladder-gain, link-context-only-r2, link-phase-only-replacement, link-task-contrast-by-context | this notebook | tested |
25	| nested-geometry-gain, nested-history-gain, nested-replacement-negative, replacement-source-diagnostics, permutation-negative, replacement-penalty-distance, replacement-ranks-lower, practical-mse-reduction, representative-trial, split-seed-stability, rff-link | this notebook | tested |
26	| estimator-family-link | 03 | tested |
27	| temporal-offset, context-capacity-contrast | 04 | tested |
28	| confirm-geometry-gain, confirm-history-contraction, confirm-replacement, confirm-table1-values | 05 | tested |
29	| rtt-data, rtt-gain, rff-rtt, estimator-family-nlb | 06 | tested (MC_Maze part of estimator-family-nlb in 07) |
30	| maze-gain, rff-maze | 07 | tested on MC_Maze (DANDI:000139 version 0.220113.0408, data elsewhere) |
31	=== cell 1 [code]
32	import collections, resource, time, zlib
33	import numpy as np
34	import pandas as pd
35	import du2026 as d
36	
37	PAPER = "du-2026"
38	def claim_seed(claim_id):
39	    return zlib.crc32(f"{PAPER}/{claim_id}".encode())
[... 362 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work--temp-work/4007710a-2704-431a-9262-3e923a1c5224/tool-results/bl6w1vz1u.txt",
 "offset": 400
}
```

```
400	SBP mean under seeds 20260726 +0/1000/2000/3000/4000: [0.02009 0.01882 0.01907 0.01918 0.01795] positive: [18, 18, 18, 18, 18]
401
```

**Agent calls Bash**

```bash
sed -n 401,732p $TMPDIR/02_link_development.txt
```

```
date task  gain_SBP  gain_TCR
0   2021-10-15   CO   0.02304   0.00804
1   2021-10-15   RD   0.02272   0.01252
2   2022-02-25   RD   0.00283   0.00262
3   2022-02-25   CO   0.01408   0.00824
4   2022-04-08   CO   0.01409  -0.00382
5   2022-04-08   RD   0.01485   0.00271
6   2022-04-15   CO   0.02688   0.01901
7   2022-04-15   RD   0.02529   0.01339
8   2022-04-29   RD   0.03347   0.01769
9   2022-04-29   CO   0.01164   0.00496
10  2022-05-13   RD   0.01262   0.00563
11  2022-05-13   CO   0.01389   0.00623
12  2022-08-10   CO   0.02288   0.01917
13  2022-08-10   RD   0.03031   0.02571
14  2022-09-21   CO   0.01879   0.00992
15  2022-09-21   RD   0.02067   0.02047
16  2022-11-02   RD   0.02494   0.01344
17  2022-11-02   CO   0.02870   0.02202

[... 313 more lines not kept]
```

**Agent calls Bash**

```bash
cat $TMPDIR/05_link_confirmation.txt
```

```
=== cell 0 [markdown]
# Du, Lai, Hu & Ye (2026) on LINK: the 20 confirmation sessions

Paper doi:10.64898/2026.08.04.742876; dataset DANDI:001201 version 0.251023.2336 (the version the
paper cites; see `02_link_development.ipynb` for the full header and claims table).

The confirmation sessions are re-selected here with the paper's rule (Methods 4.2; port of
`build_link_confirmation_manifest.py`) from the archive's asset metadata, and compared with the
paper's frozen manifest (`outputs/primary_analysis/link_confirmation_manifest.json` in the release at
commit b042fbe, read from GitHub; an input).

| Claim | Status |
|---|---|
| confirm-geometry-gain | tested |
| confirm-history-contraction | tested |
| confirm-replacement | tested |
| confirm-table1-values | tested |
=== cell 1 [code]
import collections, resource, time, zlib
import numpy as np
[... 197 more lines not kept]
```

**Agent calls Bash**

```bash
cat $TMPDIR/04_link_temporal_capacity.txt; cat $TMPDIR/03_link_estimators.txt
```

```
=== cell 0 [markdown]
# Du, Lai, Hu & Ye (2026) on LINK: temporal offset and context capacity

Paper doi:10.64898/2026.08.04.742876; dataset DANDI:001201 version 0.251023.2336 (the cited version;
see `02_link_development.ipynb` for the header, the full claims table and the data check).

| Claim | Status |
|---|---|
| temporal-offset | tested, readings (i) fully nested and (ii) `evaluate_decoders_nested` |
| context-capacity-contrast | tested, readings (i) and (ii) |

The release has no script for either analysis, and the paper does not name the estimator for Figure
7a or 7c; the claims file names both readings. Reading (ii) is `du2026.decoders_nested`, a port of
`evaluate_decoders_nested`, whose residual-neural gain is used.
=== cell 1 [code]
import collections, resource, time, zlib
import numpy as np
import pandas as pd
import du2026 as d

[... 243 more lines not kept]
```

**Agent calls Bash**

```bash
cat $TMPDIR/06_mc_rtt.txt; grep -n -A3 "Result\|Summary" $TMPDIR/01_synthetic.txt; grep -n ">>" -A4 $TMPDIR/01_synthetic.txt | head -80
```

```
=== cell 0 [markdown]
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
| estimator-family-nlb | tested on MC_RTT (reading (a) of the nonlinear context); the MC_Maze part is reported in `07_mc_maze.ipynb` |
| maze-gain, rff-maze | tested in `07_mc_maze.ipynb` (DANDI:000139, data elsewhere) |
=== cell 1 [code]
import collections, resource, time, zlib
import numpy as np
import pandas as pd
[... 174 more lines not kept]
```

**Agent calls Bash**

```bash
cd paper; grep -n -i "0.00004\b\|-0.00004\|0\.000045\|near zero\|gain range" *.txt | head -20; grep -n -i "unit field\|conversion\|differentiat" *.txt | head
```

```
438:orange bars show medians. The template-only null is near zero and embedded trial signal is recovered monotonically.
472:positive under phase only, negative under direction and additive geometry, near zero
554:Low-gain range
572:Absolute endpoint values accompany the contraction; no ratio near zero carries the claim alone. (c) Paired
630:-0.00004
756:conditional interval excludes zero, but the practical magnitude remains near zero
766:remained practically zero (gain range, 0.000045–0.000139), whereas MC_RTT
775:positive LINK task means; MC_Maze remained near zero, and MC_RTT remained
782:upstream differentiation or filtering recipe. We therefore relabel the previous
1190:code. NLB velocity unit fields and text descriptions disagree, so we report their
1191:released numerical units without conversion. Replacement is approximate and does
1238:as released because the NLB unit fields and text descriptions disagree.
1352:differentiation/filter
```

**Agent calls Bash**

```bash
cd paper; sed -n 615,640p *.txt; sed -n 750,790p *.txt
```

```
0.00420 (0.00217, 0.00630)
-0.00537
1.31%
LINK confirm SBP Geometry × phase
0.02158 (20/20)
-0.00771
4.76%
LINK confirm SBP + measured-output
history
0.00755 (19/20)
-0.00498
2.05%
MC_Maze
Task template
0.00051 (0.00026, 0.00076)
-0.00004
0.54%
MC_RTT
Lag-matched
measured-output
[... 47 more lines not kept]
```

**Agent**

**Verifier report, round 2: du-2026-01 (doi:10.64898/2026.08.04.742876)**

The claims file has 33 claims and the attempt record has 33 outcomes, all `reproduced`. No outcome is marked `assumed: true`. Cell indices below are those of the re-executed notebooks; in 02 they have shifted by about two from round 1.

**1. Outcomes**

I agree with all 31 outcomes I agreed with in round 1. The numbers in the re-executed notebooks are unchanged.

- **maze-gain and rff-maze (blocked → reproduced):** I agree, provided the protocol's author step 1.4 says what the response says. I cannot see docs/protocol.md.
  - maze-gain: 07 cell 4 gives 0.90533, 0.000513, 0.542% and −0.0000371, all within tolerance, and the interval 0.00026 to 0.00076. 07 cell 13 shows the release's own code gives identical values.
  - rff-maze: 07 cell 7 gives 0.0000448 and 0.0001386, both inside the widened range, with all three map gains positive.
- **maze-gain needs an `assumed` flag.** Its criterion states no reproduction rule ("Not on this attempt's datasets"). The rule used, all four values within tolerance as for rtt-gain, is the author's (07 cell 3). It is reasonable, but the outcome rests on it, so it should be marked `assumed: true`.
- **maze-gain's replacement tolerance is too tight (claims-file problem, reported, not corrected).** The tolerance (±0.000004) is narrower than the rounding of the paper's printed −0.00004 (±0.000005). Under the other four estimator seeds the replacement gain is −0.0027212, +0.0000294, −0.0000190 and +0.0000075, so it changes sign. The `seed_sensitive` marking is warranted.
- **estimator-family-nlb:** I agree. The MC_Maze part is now reported (07 cell 10: 0.000455 and −0.000243) and correctly kept out of the outcome.

**2. Sentences the printed outputs do not support**

- **02 cell 36** says "so two of those seeds put both SBP values outside their 10% tolerances". The attempt record (nested-replacement-negative) says "with seeds plus 1000 and plus 3000 both SBP values fall outside". Per 02 cell 35, only +1000 has both outside (−0.00887 and −0.00496). At +3000 the history value, −0.00428, is inside [−0.00448, −0.00366]. The outcome at the fixed seed is unaffected.
- **Finding 1, 02 Summary (cell 61) and the finding about the paper's data checks** say velocity is "exactly" the forward difference, with "correlation 1.000 in all 18 development sessions". 02 cell 5 shows 2021-10-15 CO second component at 0.987 (SD ratio 0.99). This is probably the session with the 1094 ms gap. Minor.
- **README** says "The MC_Maze gains … move outside the tolerances under others". Per 07 cell 4, the gain stays within tolerance under 3 of the 4 other seeds; it is the replacement gain (07 cell 4) and the lowest map gain (07 cell 7) that move outside under every one.
- **README** ("under other split seeds … the values move outside their 10% tolerances") and **05 Summary (cell 17)** ("the 10% tolerances do not hold under other split seeds") overgeneralize. Per 05 cells 6 and 9, at seed +3000 the geometry mean 0.02070 and the history mean 0.00818 are within tolerance.
- **Finding about the paper** says the code "reproduces its reported values at their printed precision for every claim tested". Not all:
  - 02 cell 29: date intervals 0.02401 against the paper's 0.02404, and 0.00711–0.01591 against 0.00709–0.01594.
  - 02 cell 59: rff-link reading (b) fails.
  - 02 cell 53: representative-trial matches under one tie reading only.
  - 04 cell 5: temporal-offset reading (a) fails under the fully nested estimator.
- **Attempt record, estimator-family-link deviations:** "0.0261224 and 0.0261219", "lsqr took 58 min" and "a full lsqr run … gave the same signs" have no printed output. 03 cell 6 also states the 5e-7 agreement without output.
- **07 cell 14:** "none of the analysis windows reaches a gap" is only indirectly supported. 07 cell 2 shows every trial runs at least 959 ms past movement onset, longer than the 800 ms window. Unlike 06, it prints no NaN count for the analysis arrays.

Every other conclusion and Summary sentence, and the rest of the README and the attempt record's notes, match the printed outputs. That includes:
- the counts in 05 cell 13 (20, 19, 20, 20);
- "three outside" in 05 cells 7 and 10;
- "mostly outside" in 05 cell 16 (7 of 12);
- the MC_Maze values;
- finding 2: SBP 0.0437 to 341 (05 cell 2) and TCR 0 to 11 (02 cell 4);
- finding 3: the 1094 ms gap (02 cell 4);
- finding 4: 15 NaN bins, none in the analysis arrays (06 cell 2).

The README claim counts (3+17+1+2+4+4+2 = 33) agree with the claims file.

The attempt record states my round-1 reasons faithfully and in my words, lightly edited ("CI" became "interval", problem numbers folded in).

**3. Round-1 points**

Resolved:
- Problem 1: reading (c) is now the position in trial order, 41 (02 cell 53).
- Problem 2: feature counts are now computed (04 cell 3).
- Problem 4: confirmation outcomes are marked `seed_sensitive`.
- Problem 5: now reported as finding 1.
- Part C, ports against release code: 07 cell 13 shows identical values for `evaluate_fully_nested_audit` and `evaluate_nonlinear_neural_audit`. The block, nonlinear-context and `decoders_nested` ports were not compared.
- Part C, confirm-replacement under other seeds: now printed (05 cell 12).
- Part C, later 001201 versions: now listed (02 cell 2).
- Part C, MC_Maze: now tested.

Unchanged, and not bearing on any conclusion:
- Problem 3, cholesky in place of lsqr; the supporting numbers are still not printed.
- Problems 6 and 1 needed no change.
- Reading (b) of the nonlinear context in estimator-family-link is still not run.

Still open and bearing on a conclusion:
- maze-gain's reproduction rule is the author's and should be flagged `assumed: true`.
- maze-gain's replacement tolerance is tighter than the paper's rounding, and the value changes sign across seeds.
- Both MC_Maze outcomes depend on protocol step 1.4 allowing data-elsewhere claims to be tested, which I could not check.

**4. Critical findings**

No finding in the attempt record is rated `critical`. The four rated `minor` are correctly rated. The data checks (no duplicates, one clock, the 9/18/375 structure, labels agreeing) show nothing that would be critical.

## End of run

19 turns, 2 minutes, $1.26 at API prices, result: success.
