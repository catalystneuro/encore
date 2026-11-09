# crcns-apl-1 · verifier-2 · run 42506524293

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  ls -la; ls paper docs 2>/dev/null; cat round-1-report.md
```

```
total 664
drwxr-xr-x 6 runner runner    4096 Nov  8 18:23 .
drwxr-xr-x 7 runner runner    4096 Nov  8 18:23 ..
crw-rw-rw- 1 nobody nogroup   1, 3 Nov  8 17:44 .bash_profile
crw-rw-rw- 1 nobody nogroup   1, 3 Nov  8 17:44 .bashrc
drwxr-xr-x 5 runner runner    4096 Nov  8 18:23 .claude
-rw-r--r-- 1 runner runner       0 Nov  8 18:23 .env
-rw-r--r-- 1 runner runner       0 Nov  8 18:23 .env.development
-rw-r--r-- 1 runner runner       0 Nov  8 18:23 .env.development.local
-rw-r--r-- 1 runner runner       0 Nov  8 18:23 .env.local
-rw-r--r-- 1 runner runner       0 Nov  8 18:23 .env.production
-rw-r--r-- 1 runner runner       0 Nov  8 18:23 .env.production.local
-rw-r--r-- 1 runner runner       0 Nov  8 18:23 .env.test
-rw-r--r-- 1 runner runner       0 Nov  8 18:23 .env.test.local
drwx------ 2 runner runner    4096 Nov  8 18:23 .git
crw-rw-rw- 1 nobody nogroup   1, 3 Nov  8 17:44 .gitconfig
crw-rw-rw- 1 nobody nogroup   1, 3 Nov  8 17:44 .github
-rw-r--r-- 1 runner runner       0 Nov  8 18:23 .gitmodules
crw-rw-rw- 1 nobody nogroup   1, 3 Nov  8 17:44 .idea
crw-rw-rw- 1 nobody nogroup   1, 3 Nov  8 17:44 .mcp.json
[... 89 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat README.md; cat crcns-apl-1-bruno-2017-01.yaml
```

```
<persisted-output>
Output too large (47.3KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work--temp-work/860acd3d-9566-47c3-ae9d-a6310beabc9d/tool-results/bm7xfoz7z.txt

Preview (first 2KB):
# Bruno, Frost & Humphries (2017) from CRCNS apl-1

Tests the findings of [Bruno, Frost & Humphries (2017)](https://doi.org/10.7554/elife.27342),
"A spiral attractor network drives rhythmic locomotion", on CRCNS data set
[apl-1](https://doi.org/10.6080/K0SN074B): spike times of 30 voltage-sensitive dye recordings of the
Aplysia pedal ganglion (three evoked bouts in each of 10 preparations), P10 nerve spikes for nine of
them, and neuron positions on the photodiode array.

| Claim | Outcome |
|---|---|
| Counts of preparations, recordings and neurons; 120 to 180 neurons per recording | Partially reproduced |
| Slow (at most 0.1 Hz) oscillation in the spectra | Reproduced |
| Decaying population rate | Reproduced |
| 4 to 8 dimensions for 80% of the variance | Reproduced (under the code's count rule) |
| Periodic recurrence at 10 to 15 s in many responses | Reproduced |
| A single dominant orbit | Reproduced |
[... 19 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python3 - <<'EOF'
import json
nb=json.load(open('reproduce_bruno_2017.ipynb'))
for i,c in enumerate(nb['cells']):
    src=''.join(c['source'])
    print(f"=== [{i}] {c['cell_type']} ===")
    print(src if c['cell_type']=='markdown' else src[:1500])
    if c['cell_type']=='code':
        for o in c.get('outputs',[]):
            if 'text' in o: print('--OUT--\n'+''.join(o['text'])[:6000])
            elif 'data' in o and 'text/plain' in o['data']: print('--OUT--\n'+''.join(o['data']['text/plain'])[:3000])
EOF
```

```
<persisted-output>
Output too large (179.6KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work--temp-work/860acd3d-9566-47c3-ae9d-a6310beabc9d/tool-results/bjkybhajx.txt

Preview (first 2KB):
=== [0] markdown ===
# Reproducing Bruno, Frost & Humphries (2017) from CRCNS data set apl-1

**Paper.** Bruno AM, Frost WN, Humphries MD (2017). A spiral attractor network drives rhythmic
locomotion. *eLife* 6:e27342. [doi:10.7554/elife.27342](https://doi.org/10.7554/elife.27342). The
claims file was written from the version of record (PMC5546814): main text, Materials and methods
and all figure legends and supplement legends.

**Data set.** CRCNS apl-1, [doi:10.6080/K0SN074B](https://doi.org/10.6080/K0SN074B), streamed from
the public bucket `crcnsarchive` under `apl-1/live/`. Version: `unversioned`. CRCNS data sets carry
no versions (docs/archives.md), and the bucket holds one copy of the processed files (`live/`; the
`orig/` folder holds only one raw optical file). That copy is pinned by the MD5 sums printed in the
data check, which match the data set's `checksums.md5`. The paper cites the data set's DOI and no
version. Files read: FileTable.mat, SpikeData.mat, ExtracellularData.mat, Coordinates.mat and
diode_template.mat; the 6.9 GB raw optical archive is not needed.

[... 12 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work--temp-work/860acd3d-9566-47c3-ae9d-a6310beabc9d/tool-results/bm7xfoz7z.txt"
}
```

```
1	# Bruno, Frost & Humphries (2017) from CRCNS apl-1
2	
3	Tests the findings of [Bruno, Frost & Humphries (2017)](https://doi.org/10.7554/elife.27342),
4	"A spiral attractor network drives rhythmic locomotion", on CRCNS data set
5	[apl-1](https://doi.org/10.6080/K0SN074B): spike times of 30 voltage-sensitive dye recordings of the
6	Aplysia pedal ganglion (three evoked bouts in each of 10 preparations), P10 nerve spikes for nine of
7	them, and neuron positions on the photodiode array.
8	
9	| Claim | Outcome |
10	|---|---|
11	| Counts of preparations, recordings and neurons; 120 to 180 neurons per recording | Partially reproduced |
12	| Slow (at most 0.1 Hz) oscillation in the spectra | Reproduced |
13	| Decaying population rate | Reproduced |
14	| 4 to 8 dimensions for 80% of the variance | Reproduced (under the code's count rule) |
15	| Periodic recurrence at 10 to 15 s in many responses | Reproduced |
16	| A single dominant orbit | Reproduced |
17	| Periods robust to the recurrence threshold | Reproduced |
18	| Coalescence within one period of stimulation | Not reproduced |
19	| Same manifold across bouts (two axis choices) | Reproduced (2 claims) |
20	| Different initial conditions | Reproduced |
[... 752 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work--temp-work/860acd3d-9566-47c3-ae9d-a6310beabc9d/tool-results/bjkybhajx.txt"
}
```

```
1	=== [0] markdown ===
2	# Reproducing Bruno, Frost & Humphries (2017) from CRCNS data set apl-1
3	
4	**Paper.** Bruno AM, Frost WN, Humphries MD (2017). A spiral attractor network drives rhythmic
5	locomotion. *eLife* 6:e27342. [doi:10.7554/elife.27342](https://doi.org/10.7554/elife.27342). The
6	claims file was written from the version of record (PMC5546814): main text, Materials and methods
7	and all figure legends and supplement legends.
8	
9	**Data set.** CRCNS apl-1, [doi:10.6080/K0SN074B](https://doi.org/10.6080/K0SN074B), streamed from
10	the public bucket `crcnsarchive` under `apl-1/live/`. Version: `unversioned`. CRCNS data sets carry
11	no versions (docs/archives.md), and the bucket holds one copy of the processed files (`live/`; the
12	`orig/` folder holds only one raw optical file). That copy is pinned by the MD5 sums printed in the
13	data check, which match the data set's `checksums.md5`. The paper cites the data set's DOI and no
14	version. Files read: FileTable.mat, SpikeData.mat, ExtracellularData.mat, Coordinates.mat and
15	diode_template.mat; the 6.9 GB raw optical archive is not needed.
16	
17	**Method.** The claims file decides what is tested. Where it leaves a detail open, the detail is
18	taken from the paper's Methods or from its code (github.com/mdhumphries/AplysiaAttractorAnalysis at
19	commit e5f28e98), cited in `apl.py`. Two details recur in almost every claim: the width of the
20	Gaussian kernel and the rule for the number of PCs. Each is run under every reading the criteria
[... 770 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work--temp-work/860acd3d-9566-47c3-ae9d-a6310beabc9d/tool-results/bjkybhajx.txt",
 "offset": 791,
 "limit": 700
}
```

```
791	    4     2        1   6259          0.994         0.980
792	    4     3        1   4512          0.989         0.917
793	    5     1        2   6271          0.957         0.885
794	    5     2        1   6146          0.984         0.917
795	    5     3        2   6405          0.971         0.892
796	    6     1        1   7326          1.000         0.970
797	    6     2        1   6561          0.998         0.929
798	    6     3        1   7024          0.970         0.952
799	    7     1        2   2530          0.787         0.532
800	    7     2        2   1821          0.583         0.331
801	    7     3        2   2009          0.838         0.319
802	    8     1        1   4739          0.966         0.742
803	    8     2        1   2660          0.968         0.552
804	    8     3        3   5186          0.897         0.801
805	    9     1        2   4967          0.902         0.867
806	    9     2        4   3852          0.852         0.718
807	    9     3        3   5576          0.953         0.899
808	   10     1        1   5497          1.000         0.944
809	   10     2        3   2276          0.443         0.415
810	   10     3        3   3651          0.731         0.710
[... 680 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work--temp-work/860acd3d-9566-47c3-ae9d-a6310beabc9d/tool-results/bjkybhajx.txt",
 "offset": 1491,
 "limit": 650
}
```

```
1491	    8     1    108.5     0.298     False      True
1492	    8     2     68.5     0.000      True     False
1493	    8     2    109.5     0.034     False      True
1494	    8     3     45.5     0.468      True     False
1495	    8     3    101.5     0.026      True      True
1496	    9     1     96.5     0.488      True     False
1497	    9     1    106.5     0.000     False      True
1498	    9     2     83.5     0.230      True     False
1499	    9     2    104.5     0.266     False      True
1500	    9     3     96.5     0.042      True      True
1501	   10     1     79.5     0.000      True     False
1502	   10     2     48.5     0.000      True     False
1503	   10     2    109.5     0.100     False      True
1504	   10     3     66.5     0.000      True     False
1505	   10     3    104.5     0.000     False      True
1506	
1507	=== [53] markdown ===
1508	**Result: partially reproduced, resting on the adopted reading.** Under the adopted reading
1509	with the Methods' period (mean of the dominant peak), 34 divergent periods are found and 16 remain
1510	after removing those within two periods of the end; 15 of 16 (0.938) returned above 90%. The fraction
[... 630 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work--temp-work/860acd3d-9566-47c3-ae9d-a6310beabc9d/tool-results/bjkybhajx.txt",
 "offset": 2141,
 "limit": 610
}
```

```
2141	   own  le80          [3, 4, 4, 4, 3, 4, 4, 4, 5]     [7, 10, 9, 10, 9, 10, 11, 11, 16]               True             True
2142	pooled min80          [5, 6, 5, 5, 4, 5, 4, 5, 5]    [9, 13, 11, 10, 11, 12, 9, 10, 12]              False            False
2143	pooled  le80          [4, 5, 4, 4, 3, 4, 3, 4, 4]      [8, 12, 10, 9, 10, 11, 8, 9, 11]               True             True
2144	
2145	own/min80, full history grid for both:
2146	 prep  bout  dims80  dims90  hist80_ms  hist90_ms  MAE80        MAE90  R2_80  R2_90
2147	    2     1       4       8         60         70  8.396        7.472  0.395  0.380
2148	    2     2       5      11        120         60 27.802       43.759  0.313  0.238
2149	    2     3       5      10         80         70 15.346       16.450  0.680  0.619
2150	    4     1       5      11         50         50 19.504 66042549.094  0.048  0.055
2151	    4     2       4      10         90         50 20.235       21.361  0.800  0.742
2152	    4     3       5      11        180         60 29.486       30.203  0.465  0.552
2153	    5     1       5      12         50         60  4.364        4.207  0.768  0.761
2154	    5     2       5      12        160         50  6.640        9.778  0.700  0.578
2155	    5     3       6      17         50         50 11.836       13.616  0.795  0.602
2156	
2157	own/le80, full history grid for both:
2158	 prep  bout  dims80  dims90  hist80_ms  hist90_ms  MAE80        MAE90  R2_80  R2_90
2159	    2     1       3       7         60         60 10.994 7.462000e+00  0.348  0.385
2160	    2     2       4      10         70         60 26.812 3.876100e+01  0.319  0.279
[... 589 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -c "^- id:\|^  - id:" 10.7554-elife.27342.yaml; grep -n "id:" 10.7554-elife.27342.yaml | head -50; head -60 10.7554-elife.27342.yaml
```

```
30
77:  id: apl-1
81:- id: dataset-size
104:- id: fig1d-slow-oscillation
124:- id: fig1e-decaying-rate
138:- id: fig2b-dimensions
162:- id: fig2ef-periodic-recurrence
187:- id: fig2e-single-dominant-orbit
201:- id: fig2s2-threshold-robust
214:- id: fig3a-coalescence
231:- id: fig3c-same-manifold
257:- id: fig3s1a-common-axes
269:- id: fig3d-initial-conditions
287:- id: fig3f-pairwise-similarity
306:- id: fig3h-perturbations-return
330:- id: fig3i-same-manifold-after
347:- id: fig4bc-stable-spiral
368:- id: fig4c-orbital-period
387:- id: fig4s1a-contracting-dimensions
402:- id: fig4s1b-rotation-dominant
[... 72 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "10.7554-elife.27342.yaml",
 "offset": 60,
 "limit": 600
}
```

```
60	# responses, "programs"), each evoked by 8 V, 5 ms pulses at 20 Hz for 2.5 s to pedal nerve 9 at
61	# 30 s into a recording of about 125 s (30 s spontaneous, about 95 s evoked); stimulation
62	# intervals of 15 and 60 min. The same neurons were tracked across the three bouts of a
63	# preparation; the paper gives 120 to 180 neurons per recording and 1131 neurons in all
64	# (Figure 7B). Extracellular P10 nerve recordings for all three bouts in 3 preparations (nine
65	# responses). Neuron (x, y) positions on the array, reconstructed for 8 preparations (4 left,
66	# 4 right ganglia). The data set's description says it holds spike times of the 30 recordings,
67	# the P10 channel where recorded, and neuron location maps; so all claims use the data set.
68	# The data set's description gives 75 to 160 neurons per preparation, against the paper's 120 to
69	# 180 (claim dataset-size).
70	#
71	# Not made into claims: the three-neuron model of Figure 1, figure supplement 1 (a simulation, no
72	# data), and Figure 2, figure supplement 1, which describes the range of dynamics without a finding
73	# beyond the claims below.
74	schema_version: 2
75	dataset:
76	  archive: crcns
77	  id: apl-1
78	  doi: 10.6080/K0SN074B
79	paper: doi:10.7554/elife.27342
[... 580 more lines not kept]
```

**Agent calls Bash**

```bash
cd paper; grep -n -i "divergent\|two oscillation\|two cycles" 10.7554-elife.27342.txt | head -30; grep -n -i "consistent with the directly\|all nine\|173" 10.7554-elife.27342.txt | head
```

```
95:Low dimensional population dynamics meet the conditions for a periodic attractor. ( A ) Distribution of the time the population dynamics took to coalesce onto the attractor from the stimulation onset, and the subsequent stability of the attractor (measured by the proportion of recurrent points). Colours indicate evoked responses from the same preparation. The coalescence time is the mid-point of the first 5 s sliding window in which at least 90% of the points on the population trajectory recurred in the future. ( B ) Projection of three sequential population responses from one preparation onto the same embedding dimensions. Dots are time of stimulus offset. ( C ) Sequential population responses fall onto the same manifold. Dots indicate distances between pairs of population responses in the same preparation; color indicates preparation. Control distances are from random projections of each population response onto the same embedding dimensions - using the same time-series, but shuffling the assignment of time series to neurons. This shows how much of the manifold agreement is due to the choice of embedding dimensions alone. The two pairs below the diagonal are for response pairs (1,2) and (1,3) in preparation 4; this correctly identified the unique presence of apparent chaos in response 1 (see Figure 3—figure supplement 1 ). ( D ) Distances between pairs of population responses from the same preparation in three states: the end of spontaneous activity (at stimulus onset); between stimulation onset and coalescence (the maximum distance between the pair); and after both had coalesced (both reaching the putative attractor manifold; data from panel C). ( E ) Example neuron activity similarity matrices for consecutively evoked population responses. Neurons are ordered according to their total similarity in stimulation 2. ( F ) Correlation between pairs of neuron similarity matrices (Data) compared to the expected correlation between pairs of matrices with the same tot
[... 10 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python3 -c "
import json
nb=json.load(open('reproduce_bruno_2017.ipynb'))
for i,c in enumerate(nb['cells']):
    m=c.get('metadata',{})
    if m.get('tags') or any(k not in ('execution','collapsed','scrolled') for k in m): print(i,m)
" | head -50
```

```
3 {'execution': {'iopub.execute_input': '2026-11-08T17:46:43.085575Z', 'iopub.status.busy': '2026-11-08T17:46:43.085315Z', 'iopub.status.idle': '2026-11-08T17:46:43.130534Z', 'shell.execute_reply': '2026-11-08T17:46:43.129965Z'}, 'tags': ['sanity']}
5 {'execution': {'iopub.execute_input': '2026-11-08T17:46:43.132126Z', 'iopub.status.busy': '2026-11-08T17:46:43.131996Z', 'iopub.status.idle': '2026-11-08T17:46:43.216653Z', 'shell.execute_reply': '2026-11-08T17:46:43.215970Z'}, 'tags': ['sanity']}
6 {'execution': {'iopub.execute_input': '2026-11-08T17:46:43.218076Z', 'iopub.status.busy': '2026-11-08T17:46:43.217936Z', 'iopub.status.idle': '2026-11-08T17:46:44.753164Z', 'shell.execute_reply': '2026-11-08T17:46:44.752455Z'}, 'tags': ['sanity']}
7 {'execution': {'iopub.execute_input': '2026-11-08T17:46:44.754543Z', 'iopub.status.busy': '2026-11-08T17:46:44.754388Z', 'iopub.status.idle': '2026-11-08T17:46:44.760831Z', 'shell.execute_reply': '2026-11-08T17:46:44.760160Z'}, 'tags': ['sanity']}
10 {'execution': {'iopub.execute_input': '2026-11-08T17:46:44.762143Z', 'iopub.status.busy': '2026-11-08T17:46:44.762024Z', 'iopub.status.idle': '2026-11-08T17:46:44.796663Z', 'shell.execute_reply': '2026-11-08T17:46:44.795955Z'}, 'tags': ['claim:dataset-size']}
13 {'execution': {'iopub.execute_input': '2026-11-08T17:46:44.798054Z', 'iopub.status.busy': '2026-11-08T17:46:44.797924Z', 'iopub.status.idle': '2026-11-08T17:46:50.869816Z', 'shell.execute_reply': '2026-11-08T17:46:50.869245Z'}, 'tags': ['claim:fig1d-slow-oscillation']}
14 {'execution': {'iopub.execute_input': '2026-11-08T17:46:50.871407Z', 'iopub.status.busy': '2026-11-08T17:46:50.871244Z', 'iopub.status.idle': '2026-11-08T17:46:50.955287Z', 'shell.execute_reply': '2026-11-08T17:46:50.954602Z'}, 'tags': ['claim:fig1d-slow-oscillation']}
17 {'execution': {'iopub.execute_input': '2026-11-08T17:46:50.956715Z', 'iopub.status.busy': '2026-11-08T17:46:50.956580Z', 'iopub.status.idle': '2026-11-08T17:46:50.993380Z', 'shell.execute_
[... 28 more lines not kept]
```

**Agent**

# Verifier report, round 2: Bruno, Frost & Humphries 2017 (eLife 27342) on CRCNS apl-1

The claims file has 30 claims, and the attempt record has 30 outcomes: 22 reproduced, 5 partially reproduced, 2 not reproduced and 1 blocked. Three outcomes are marked `assumed: true`: fig3h, fig4c and fig7gh. I found no place where the claims file misreads the paper.

## 1. Outcomes

I agree with 29 of the 30 outcomes. I disagree with one.

**Disagreement: fig6d-decode-p10.** The record says partially reproduced; I say not reproduced.
- The criterion requires mean forecast R − 2 s.e.m. > 0 "in each of the nine responses", and it has no partial rule. The paper's statement is specifically "in all nine".
- Cell 79 shows preparation 4, bout 1 failing under all four readings, with histories up to 100 ms, and with the code's windowing (mean R −0.060 to −0.127).
- The failure therefore does not depend on the reading. Eight of nine is a failure of exactly what the claim says, not a partial match.

**Outcomes where my round-1 view has changed**
- **fig4c (reproduced, assumed): I now agree.** The criterion judges only the mean, 10 ± 1 s, and says consistency is "reported", not judged. Under the adopted reading the mean is 10.45 s (cell 61). In round 1 I judged consistency, which the criterion does not ask for.
- **fig3h (partially reproduced, assumed): I accept it.** The criterion holds under own/le80 (18 kept and 16 returned; 19 and 17) and fails under the adopted reading (16 and 15), and the record says so. Two caveats:
  - The criterion's text gives no partial outcome. Strictly, under the adopted reading it gives not reproduced.
  - An unreported fact bears on this; see point 2 below.
- **fig7gh (partially reproduced, assumed): I agree, as I did in round 1.** The result is split by reading: one slope of two is significant under own/min80 and under own/le80 with recurrent points, and none under either pooled reading (cell 100). The same strictness caveat as fig3h applies.
- **fig7s2 (reproduced): I agree.** Cell 103 gives 0 or 1 of 10 preparations with a core, across both widths, both seeds and both participation readings. The caveat is that the ported toolbox was not checked against MATLAB, as the record says.
- **fig6s2 (reproduced): I agree.** Under own/le80 the counts are 3 to 5 and the 90% counts at least double them. The 90% models are not better: MAE p = 0.91, R² p = 0.50, with the full history grid for both (cell 83).

**Assumptions**
- All three are stated and are reasonable: the adopted reading (own/min80) follows the Methods' count rule first.
- The record openly says that fig2b fails under that same reading (by one response) and that no single reading makes the whole chain hold.
- One correction for fig7gh: the deviation says "under the pooled readings the claim is reproduced". That is true with the legend's exclusion, the main reading. With the code's exclusion, pooled/min80 has a significant total-change slope with recurrent points (p = 0.028 and 0.029, cell 100), and this is not mentioned.

## 2. Sentences the numbers do not support

- **Cell 62 and the record's fig4c notes:** "consistency holds only for the means (10.45 s against a median recurrence period of 12.73 s)". The two values differ by 2.3 s, more than twice the claim's tolerance of 1 s, so cell 61/25 does not show consistency of the means either.
- **Cell 21:** "The Methods' printed width (median ISI / 12, or / sqrt(12)) gives 22 to 76 dimensions". Cell 20 gives 21 (sqrt12/le80) to 76; the record's "21 to 76" is correct.
- **Cell 22:** "the two narrow widths give 22 to 75 dimensions". Cell 20 gives 21 to 76.
- **Cell 108, Summary:** "The Methods' kernel width as printed (median ISI / 12) gives 22 to 76 dimensions". Under /12, cell 20 gives 33 to 76; 21 to 76 is the range over both printed readings.
- **Cell 53 and the record's fig3h notes:** "The code's rule … keeps 17 to 21" is true but leaves out something that bears on the outcome. Under the adopted reading the code's rule keeps 19 periods and 18 return (0.947, cell 52). That meets both tolerances and matches the paper's 19.
- **Cell 79/83 (not discussed anywhere):** for preparation 4, bout 1 the mean MAE reaches 7.6e6 (code windowing), 6.6e7 (90%, own/min80) and 3.1e9 (90%, own/le80), which points to exploding forecasts in some windows. It does not change any outcome, since the 90% models only look worse.
- **README:** "about 36 minutes". Cell 109 prints 33.8 min, so this is trivial.
- **Record, fig7s2 entry:** it has no `notebook:` or `output:` fields, although cell 103 is tagged `claim:fig7s2-no-invariant-core`.

All other "**Result:**" sentences, the Summary's per-reading table and the README outcome table match the printed outputs.

**My round-1 reasons in the record.** They are stated faithfully in my own words. One misattribution: in fig4c, the record attaches my B.11 toy-orbit note as a reason. I had marked B.11 as not affecting a conclusion; my reasons for fig4c were the le80 failure and the missing correlation.

## 3. Round-1 points

**Resolved**
- **B.1:** disclosed in cells 21 and 22 and in the Summary table.
- **B.2:** fig7gh now runs under all four readings.
- **B.3:** fig6d now runs under all four readings and fails under every one.
- **B.4:** the "weak evidence" wording is now in fig3h and fig3i.
- **B.5 and B.6:** full history grid; own/le80 90% models; comparison on four histories.
- **B.7:** windows now count at ≥ 90%.
- **B.8:** fig7s2 is now tested.
- **B.9:** quadrant shares and true quintiles added.
- **B.10:** detrended spectrum added.
- **All items in section C:** neighbour counts, coalescence densities, the fig6d plot, the fig7gh readings, the fig6s2 equal-grid comparison and the fig7s2 outputs.

**Remaining, bearing on a conclusion**
1. **fig6d:** the outcome should be not reproduced (see section 1).
2. **fig3h:** the code's removal rule under the adopted reading meets the criterion (19 kept, 18 returned). This is unreported, and "partial" is not an outcome the criterion's text allows.
3. **fig4c:** the "consistent with" sentence is unsupported (section 2).
4. **No consistent reading:** no single reading of width and count makes fig2b, fig3h, fig4c, fig6s2 and fig7gh all hold, and fig2b fails under the adopted reading. This is now disclosed, but every assumed outcome rests on it.
5. **fig7s2:** the outcome rests on an unvalidated port of random clustering. It is stable across seeds and widths.
6. **fig7gh:** the record's statement that the pooled readings reproduce the claim depends on the exclusion rule.

## End of run

13 turns, 3 minutes, $1.83 at API prices, result: success.
