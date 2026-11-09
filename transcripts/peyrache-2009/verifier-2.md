# crcns-pfc-6 · verifier-2 · run 41965401156

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  ls -la; ls paper docs 2>/dev/null; cat round-1-report.md
```

```
total 464
drwxr-xr-x 6 runner runner    4096 Nov  5 04:10 .
drwxr-xr-x 7 runner runner    4096 Nov  5 04:10 ..
crw-rw-rw- 1 nobody nogroup   1, 3 Nov  5 04:03 .bash_profile
crw-rw-rw- 1 nobody nogroup   1, 3 Nov  5 04:03 .bashrc
drwxr-xr-x 5 runner runner    4096 Nov  5 04:10 .claude
-rw-r--r-- 1 runner runner       0 Nov  5 04:10 .env
-rw-r--r-- 1 runner runner       0 Nov  5 04:10 .env.development
-rw-r--r-- 1 runner runner       0 Nov  5 04:10 .env.development.local
-rw-r--r-- 1 runner runner       0 Nov  5 04:10 .env.local
-rw-r--r-- 1 runner runner       0 Nov  5 04:10 .env.production
-rw-r--r-- 1 runner runner       0 Nov  5 04:10 .env.production.local
-rw-r--r-- 1 runner runner       0 Nov  5 04:10 .env.test
-rw-r--r-- 1 runner runner       0 Nov  5 04:10 .env.test.local
drwx------ 2 runner runner    4096 Nov  5 04:10 .git
crw-rw-rw- 1 nobody nogroup   1, 3 Nov  5 04:03 .gitconfig
crw-rw-rw- 1 nobody nogroup   1, 3 Nov  5 04:03 .github
-rw-r--r-- 1 runner runner       0 Nov  5 04:10 .gitmodules
crw-rw-rw- 1 nobody nogroup   1, 3 Nov  5 04:03 .idea
crw-rw-rw- 1 nobody nogroup   1, 3 Nov  5 04:03 .mcp.json
[... 76 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat README.md; cat crcns-pfc-6-peyrache-2009-01.yaml
```

```
<persisted-output>
Output too large (36.6KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work--temp-work/4757c909-cf7f-4839-aa71-6c80ee01c9e3/tool-results/bisqiy1kc.txt

Preview (first 2KB):
# Peyrache, Khamassi, Benchenane, Wiener & Battaglia (2009) from CRCNS pfc-6

Tests the findings of [Peyrache et al. (2009)](https://doi.org/10.1038/nn.2337) that can be tested on
[CRCNS pfc-6](https://doi.org/10.6080/K0KH0KH5), which holds the prefrontal spike trains, cell types,
behaviour, position, and awake and SWS intervals of 86 sessions from four rats. It holds no LFP, no
sharp-wave ripple, delta-wave or spindle times, and no tetrode of each cell, so the analyses of
Figures 5 to 7 and the same-tetrode control cannot be repeated.

| Claim | Outcome |
|---|---|
| 1,692 cells in 63 sessions | Not reproduced (56 sessions, 1499 cells under the inclusion rule) |
| Rules learned by each rat | Not reproduced |
| Ten learning sessions by the paper's definition | Not reproduced |
| 323 signal and 811 nonsignal components | Partially reproduced |
| Reactivation higher in post than pre SWS, all signal groups | Reproduced |
| Replay concentrated in SWS (Supplementary Fig. 5) | Partially reproduced (post exceeds pre outside SWS too) |
[... 17 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat README.md | tail -n +25; echo ======; cat crcns-pfc-6-peyrache-2009-01.yaml
```

```
<persisted-output>
Output too large (35KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work--temp-work/4757c909-cf7f-4839-aa71-6c80ee01c9e3/tool-results/bbym1fa9v.txt

Preview (first 2KB):
| Behaviour unchanged by learning | Reproduced |
| SPWR, delta, spindle and same-tetrode analyses (14 claims) | Blocked: data missing |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The attempt record, with the reasons and the differences from the paper's method, is
[`attempts/crcns-pfc-6-peyrache-2009-01.yaml`](../../attempts/crcns-pfc-6-peyrache-2009-01.yaml).

- `reproduce_peyrache_2009.ipynb`: the analysis. It takes about two minutes, most of it streaming
  the 295 MB archive.
- `pfc6.py`: streaming and parsing the archive, the awake templates and reactivation strengths of
  the Online Methods, the closed-form shuffle mean, and the behavioural criteria. Other notebooks on
  this data set can import it.
======
schema_version: 2
[... 35 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "crcns-pfc-6-peyrache-2009-01.yaml"
}
```

```
1	schema_version: 2
2	id: crcns-pfc-6-peyrache-2009-01
3	dataset:
4	  archive: crcns
5	  id: pfc-6
6	  version: unversioned
7	  doi: 10.6080/K0KH0KH5
8	paper: doi:10.1038/nn.2337
9	date: 2026-11-05
10	entry: crcns-pfc-6-peyrache-2009
11	provenance:
12	  kind: agent
13	  accountable:
14	    name: CatalystNeuro
15	  agent:
16	    harness: Claude Code
17	    model: claude-opus-5-5
18	    protocol: pilot-13
19	  runner:
20	    platform: GitHub Actions
[... 581 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat 10.1038-nn.2337.yaml
```

```
<persisted-output>
Output too large (47.1KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work--temp-work/4757c909-cf7f-4839-aa71-6c80ee01c9e3/tool-results/b9fvzcc78.txt

Preview (first 2KB):
# Claims for Peyrache, Khamassi, Benchenane, Wiener & Battaglia (2009), Nat Neurosci 12:919-926,
# on CRCNS data set pfc-6 (doi:10.6080/K0KH0KH5).
# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"), 2026-11-05,
# protocol as stated in docs/protocol.md (Reader), version pilot-13.
#
# Text read: the version of record, as supplied under paper/ (PyMuPDF text of the journal PDF),
# with its Results, Discussion, figure legends and Online Methods, and the supplement
# (41593_2009_BFnn2337_MOESM12_ESM.pdf), from which the Supplementary Discussion, the legends of
# Supplementary Figures 2 to 13 and Supplementary Table 1 were read. The legend of
# Supplementary Figure 1 (histology) is not in the extracted text; no claim rests on it. The PDF
# pages could not be rendered here, so no figure was read from the image. The extracted text
# prints some signs as other glyphs. "P o" is P <, "P 4" is P >, "n 1⁄4" is n =, "B" before a
# number is "about", and "10�30" is 10 to the power -30. Quotes keep these glyphs as printed,
# and the p-values below are read from them; the quote checker cannot find p-values printed as
# powers of ten, which were confirmed by reading. The paper links no analysis code, so none was
# read; every method below is from the Online Methods, the figure legends or the supplement.
[... 9 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "10.1038-nn.2337.yaml"
}
```

```
1	# Claims for Peyrache, Khamassi, Benchenane, Wiener & Battaglia (2009), Nat Neurosci 12:919-926,
2	# on CRCNS data set pfc-6 (doi:10.6080/K0KH0KH5).
3	# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"), 2026-11-05,
4	# protocol as stated in docs/protocol.md (Reader), version pilot-13.
5	#
6	# Text read: the version of record, as supplied under paper/ (PyMuPDF text of the journal PDF),
7	# with its Results, Discussion, figure legends and Online Methods, and the supplement
8	# (41593_2009_BFnn2337_MOESM12_ESM.pdf), from which the Supplementary Discussion, the legends of
9	# Supplementary Figures 2 to 13 and Supplementary Table 1 were read. The legend of
10	# Supplementary Figure 1 (histology) is not in the extracted text; no claim rests on it. The PDF
11	# pages could not be rendered here, so no figure was read from the image. The extracted text
12	# prints some signs as other glyphs. "P o" is P <, "P 4" is P >, "n 1⁄4" is n =, "B" before a
13	# number is "about", and "10�30" is 10 to the power -30. Quotes keep these glyphs as printed,
14	# and the p-values below are read from them; the quote checker cannot find p-values printed as
15	# powers of ten, which were confirmed by reading. The paper links no analysis code, so none was
16	# read; every method below is from the Online Methods, the figure legends or the supplement.
17	#
18	# Data the paper used. Four male Long-Evans rats (rats 15, 18, 19 and 20), a drive of six
19	# recording tetrodes in the right prelimbic cortex (mPFC) and three tetrodes for LFP in ventral
20	# CA1. 63 sessions (rat 15, 16; rat 18, 11; rat 19, 12; rat 20, 24), 1,692 mPFC cells. Only
[... 737 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -c '^- id:' 10.1038-nn.2337.yaml; grep -c '^- claim:' crcns-pfc-6-peyrache-2009-01.yaml; grep -A1 '^- claim:' crcns-pfc-6-peyrache-2009-01.yaml | grep outcome | sort | uniq -c
python3 - <<'EOF'
import json
nb=json.load(open('reproduce_peyrache_2009.ipynb'))
out=[]
for i,c in enumerate(nb['cells']):
    src=''.join(c['source'])
    out.append(f"\n######## CELL {i} [{c['cell_type']}]\n{src}")
    if c['cell_type']=='code':
        for o in c.get('outputs',[]):
            if o['output_type']=='stream': out.append('--- OUT:\n'+''.join(o['text']))
            elif 'data' in o:
                d=o['data']
                if 'text/plain' in d and 'image/png' not in d: out.append('--- OUT:\n'+''.join(d['text/plain']))
                elif 'image/png' in d: out.append('--- [image]')
            elif o['output_type']=='error': out.append('--- ERR '+o['ename']+o['evalue'])
open('/tmp/claude/nb.txt','w').write('\n'.join(out)) if False else None
import os
open(os.environ.get('TMPDIR','/tmp')+'/nb.txt','w').write('\n'.join(out))
print(len(nb['cells']))
EOF
wc -c $TMPDIR/nb.txt; echo $TMPDIR
```

```
29
29
     14   outcome: blocked
      5   outcome: not_reproduced
      6   outcome: partially_reproduced
      4   outcome: reproduced
58
108685 /tmp/claude-1001/nb.txt
/tmp/claude-1001
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/nb.txt"
}
```

```
1	
2	######## CELL 0 [markdown]
3	# Reproducing Peyrache et al. (2009) from CRCNS pfc-6
4	
5	**Paper.** Peyrache A, Khamassi M, Benchenane K, Wiener SI, Battaglia FP (2009). Replay of
6	rule-learning related neural patterns in the prefrontal cortex during sleep. *Nature
7	Neuroscience* 12(7):919-926. [doi:10.1038/nn.2337](https://doi.org/10.1038/nn.2337)
8	
9	**Dataset.** CRCNS pfc-6, "Activity of neurons in rat medial prefrontal cortex during learning
10	and sleep" ([doi:10.6080/K0KH0KH5](https://doi.org/10.6080/K0KH0KH5)), read anonymously from the
11	public bucket at `https://crcnsarchive.s3-us-west-2.amazonaws.com/pfc-6/live/`. The data set holds
12	one archive, `mPFC_Data.tar.gz`, with seven text files per session (spikes, cell types, behaviour,
13	position, awake and SWS intervals), described by `docs/crcns_pfc-6_data_description.pdf`
14	(version 0.7, March 12, 2018).
15	
16	**Version.** CRCNS data sets are not versioned (docs/archives.md), so the version is recorded as
17	`unversioned`, and the file read is pinned by its MD5 from the data set's `checksums.md5`:
18	`mPFC_Data.tar.gz` 2c255b44209ece01326dd09efaabd92a, checked below against the bucket's ETag.
19	The data set's description is checksummed too (pdf 3464d68562a83bb15d843999ec3227c8, docx
20	c536d32bb1a791ac00a9a7d1056f57a6); the learning sessions are read from the docx. This is the
[... 684 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/nb.txt",
 "offset": 705,
 "limit": 480
}
```

```
705	    if drop_silent:
706	        cw = cw[cw.sum(1) > 0]
707	    lam, _, lmin, lmax = pfc6.template(pfc6.zscore(cw))
708	    phi = lam[lam > lmax] / lmax
709	    return int(np.sum(lam > lmax)), int(np.sum((lam > lmin) & (lam <= lmax))), [int(np.sum(phi > 1.8)), int(np.sum((phi > 1.4) & (phi <= 1.8))), int(np.sum(phi <= 1.4))]
710	for thr in (4.0, 3.5):
711	    ks = info.session[(info.cells >= 10) & (info.sws_pre_min >= thr) & (info.sws_post_min >= thr)]
712	    for drop in (False, True):
713	        res = [awake_classes(S[k], drop) for k in ks]
714	        nsig = [r[0] for r in res]
715	        print(f"variant, SWS threshold {thr} min ({len(ks)} sessions), cells silent in the awake epoch {'left out' if drop else 'kept'}: "
716	              f"signal {sum(nsig)} (291 to 355: {291 <= sum(nsig) <= 355}), nonsignal {sum(r[1] for r in res)} (730 to 892: {730 <= sum(r[1] for r in res) <= 892}), "
717	              f"sessions with 1 to 6 signal {sum(1 <= x <= 6 for x in nsig)}, group sizes >1.8, 1.4-1.8, 1-1.4: {np.sum([r[2] for r in res], axis=0).tolist()} (expected 10, 40, 273)")
718	print("per session: signal %.2f, nonsignal %.2f here; paper 323/63 = %.2f, 811/63 = %.2f" % (n_sig / len(per), n_non / len(per), 323 / 63, 811 / 63))
719	--- OUT:
720	included sessions (56): signal 285 (expected 323, 291 to 355: False), nonsignal 730 (expected 811, 730 to 892: True), below lambda_min 484
721	signal components per session: {2: 1, 3: 12, 4: 14, 5: 12, 6: 6, 7: 4, 9: 4, 10: 2, 11: 1}
722	sessions with 1 to 6 signal components: 45 of 56
723	by rat:
724	 cls  signal  nonsignal  below_lmin
[... 460 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/nb.txt",
 "offset": 1184,
 "limit": 470
}
```

```
1184	epochz (a): signal groups in 36 to 55%: 1 of 3
1185	epochz (b): signal groups in 36 to 55%: 0 of 3
1186	swsz (a): signal groups in 36 to 55%: 2 of 3
1187	swsz (b): signal groups in 36 to 55%: 2 of 3
1188	
1189	
1190	######## CELL 42 [markdown]
1191	**Result: partially reproduced.** Pooling bins by group (reading a), the share of the net post
1192	minus pre reactivation from bins above the post 99th percentile is 52.2%, 56.1% and 16.1% (Phi above 1.8, 1.4 to 1.8, 1 to
1193	1.4) with z over the epoch, and 51.0%, 60.6% and 36.6% with z over SWS: one and two of three groups in 36 to 55%. Averaging
1194	per component (reading b) gives two of three in range with z over SWS (46.3%, 45.8%) and none with z over the epoch, as
1195	components whose net is near zero give extreme ratios (99 of 241 components in the lowest group have a negative net). Those means (for example 5459%, with one component's
1196	ratio above 10^6 %) are not well defined; the count of groups in range rests on readings (a) and on the two highest
1197	groups of (b) with z over SWS, whose per-component ratios stay within 149%.
1198	
1199	######## CELL 43 [markdown]
1200	## supp10-no-coactivation
1201	
1202	> During sleep, reactivation strengths of different simultaneously recorded signal components
1203	> tend not to peak together, with a trough at zero lag in their cross-correlograms, while in the
[... 447 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 1,40p pfc6.py; grep -n "def learning_point" -A 25 pfc6.py; grep -n "def rest_epochs" -A 12 pfc6.py; python3 -c "
import re
t=open('/tmp/claude-1001/nb.txt').read()
" ; awk 'NR>=109 && NR<=194 {s+=$13} END {print s}' $TMPDIR/nb.txt
```

```
"""Loading and reactivation measures for CRCNS pfc-6 (Peyrache et al. 2009, Nat Neurosci 12:919).

The data set is one tar.gz on the public CRCNS bucket. It is streamed once, in order, and each
session's text files are parsed in memory; nothing is written to disk.

Where parameters come from:

- 100 ms bins, z-transform per cell within an epoch, C = QQ'/B, projectors p p', and
  R_l(t) = sum over i != j of Q_it P_ij Q_jt: Online Methods, "Computational methods", and
  Supplementary Figure 3 (cited in the claims file's opening comment).
- lambda_max/min = (1 +- sqrt(1/q))^2, q = B/n, Phi = lambda/lambda_max: Online Methods,
  "Signal and nonsignal components".
- Inclusion rule (at least ten cells, at least 4 min of SWS in each rest epoch): Results,
  paragraph 2, as the claims file quotes it.
- A bin counts as SWS when it lies wholly inside an SWS interval: standard choice named in the
  claims file's opening comment.
- Rest epochs: the data set gives SWS intervals and the awake epoch only. The pre epoch is taken
  as the time from 0 to the start of the awake epoch and the post epoch as the time from its end to
  the end of the position record, or of the last post SWS interval if later (an assumption; the
  claims file's supp5 criterion says the rest epochs are taken from the data set's epoch times).
[... 54 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python3 - <<'EOF'
import json,base64,os
nb=json.load(open('reproduce_peyrache_2009.ipynb'))
d=os.environ['TMPDIR']
for i,c in enumerate(nb['cells']):
    for j,o in enumerate(c.get('outputs',[])):
        if 'data' in o and 'image/png' in o['data']:
            p=f"{d}/fig_{i}_{j}.png"; open(p,'wb').write(base64.b64decode(o['data']['image/png'])); print(p)
EOF
```

```
/tmp/claude-1001/fig_23_1.png
/tmp/claude-1001/fig_32_1.png
/tmp/claude-1001/fig_44_1.png
/tmp/claude-1001/fig_50_3.png
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/fig_50_3.png"
}
```

Result: no output.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/fig_44_1.png"
}
```

Result: no output.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/fig_23_1.png"
}
```

Result: no output.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/fig_32_1.png"
}
```

Result: no output.

**Agent**

**Round 2 verification: Peyrache et al. 2009 (nn.2337) on CRCNS pfc-6**

The claims file and the attempt record both have 29 claims. The record gives 4 reproduced, 6 partially reproduced, 5 not reproduced and 14 blocked (data_missing). The notebook tests 15 of them.

**1. Outcomes and assumptions**

| Claim | Outcome in record | Agree? | Note |
|---|---|---|---|
| sessions-and-cells | not_reproduced | yes | |
| rules-learned | not_reproduced | yes | |
| learning-sessions | not_reproduced | yes | The fixed reading (b) gives 22 and 14 sessions; neither is in 9 to 11 (cell 15). |
| fig1b-signal-components | partially_reproduced | yes | |
| fig2b-post-greater-than-pre | reproduced | yes | |
| supp5-sws-only | partially_reproduced (assumed) | yes, I now agree | See below. |
| supp6-pre-post-sws-alike | reproduced | yes, I withdraw my round-1 disagreement | See below. |
| fig2b-encoding-correlation | not_reproduced | yes | |
| fig2b-pre-weaker | partially_reproduced | yes | |
| fig2e-skewness | not_reproduced | yes | |
| fig2f-tail-contribution | partially_reproduced | yes | |
| supp10-no-coactivation | reproduced | yes | |
| supp11-shuffle-control | partially_reproduced | yes | |
| fig6b-down-up | partially_reproduced (assumed) | yes on the outcome | The stated assumption does not support it. See below. |
| supp12-behavior-unchanged | reproduced | yes | |
| supp8, the five fig5 claims, replay-in-delta-spindle-periods, fig6a, fig6c, fig6d, the four fig7 claims (14 in all) | blocked, data_missing | yes | |

- **supp5:** The repeated-measures ANOVA gives state p = 0.0019 and epoch p = 4.9e-08, with SWS above non-SWS and post above pre (cell 26). Outside SWS, post still exceeds pre under both readings (t p = 0.042, Wilcoxon p = 0.018). Two of the three parts hold, so partially_reproduced fits.
  - The assumption about the rest-epoch bounds is stated, follows the criterion, and the 30-min variant gives the same result.
  - The repeated-measures ANOVA is a fair reading of the legend's "two-way ANOVA" for per-component means.
- **supp6:** The criterion includes the SPWR, delta and LFP measures only "where the data hold them" and judges each measure on its own. Every measure the data set holds shows no difference by paired t-test (cell 29), so reproduced is consistent with the criterion as written.
- **fig6b:** The deviation says the outcome rests on comparing pre and post over −0.5 to −0.3 s. Under that comparison pre is lower (0.063 against 0.107, cell 50), so the criterion as written would give reproduced, not partial.
  - The partial outcome actually rests on two other facts: the two ways of comparing disagree (pre's peak, 0.145, is above post's, 0.132), and the per-component difference is not significant (p = 0.15).
  - The record's `assumed` deviation and the summary's "resting on an assumption" should say this. I agree with partially_reproduced, as in round 1.

**2. Text against the printed outputs**

Almost every sentence checks out against the outputs, including the 2834 trials of the data check. The README's 86 sessions, 14 blocked claims and its outcome table agree with the record. The exceptions:

- **Cell 57 (Summary), wrong:** "not reproduced by the definition (16 to 34 sessions)". Cell 15 prints 34, 16, 22 and 14, so the range is 14 to 34. This was left over from before reading (b) was fixed.
- **Cell 51 and the fig6b notes, incomplete:** "three bins at p < 0.001". Cell 50 prints "significant bins 4", of which three are positive before the transition. The fourth bin, from the profile and the figure probably the dip at 0 s, is not mentioned.
- **supp11 notes, imprecise:** "5.3% to 5.9% of the actual". That is the epoch-z range only; with z over SWS bins it is 5.1% (cell 47). The conclusion does not change.
- **supp5 deviation and notebook cell 0, incomplete:** they bound post at "the end of the position record". `rest_epochs` also extends it to the last post SWS interval if that is later. No included session appears to be affected.

The attempt record states my round-1 reasons faithfully and in my own words for all 29 claims. Problems 2 to 9 and the section C requests are folded into the matching claims: problem 4 under supp5, problems 7 and 8 under fig1b and sessions-and-cells, problems 3 and 9 under supp12.

**3. Round-1 points**

All resolved:
1. `learning_point` under reading (b): fixed, with an assert on the synthetic input in cell 15.
2. DOWN-state reading (b) identical to (a): the notebook now explains it (0.21 to 2.22 spikes per 10 ms bin).
3. supp12 sessions taken from the description: the reading (a) learning-point variant is added (p = 0.19).
4. Rest-epoch docstring: corrected.
5. supp5 ANOVA: now repeated-measures.
6. Ill-defined ratio readings in fig2f and supp10: no longer used for conclusions, and the notebook says why.
7. Silent cells: variant run (287 and 727).
8. 3.5-min SWS variant: run (315 and 820; group sizes 11, 39, 265) and the two failing learning sessions noted.
9. Speed bins: Bonferroni added (bin 0 p = 0.34).

All section C requests were met. The longest-run table shows rat 18 is one trial short of the criterion on the right-arm rule. I also viewed the four figures this time, and they match the printed values.

What remains that bears on a conclusion:
- The fig6b justification: the outcome is right, but its stated assumption would give reproduced.
- The Summary's "16 to 34 sessions" for learning-sessions.

## End of run

17 turns, 2 minutes, $1.38 at API prices, result: success.
