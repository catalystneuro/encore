# 000971 · verifier-2 · run 39114785673

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  ls -la; ls paper docs 2>/dev/null; cat round-1-report.md
```

```
total 600
drwxr-xr-x 5 runner runner    4096 Oct 18 09:42 .
drwxr-xr-x 7 runner runner    4096 Oct 18 09:42 ..
crw-rw-rw- 1 nobody nogroup   1, 3 Oct 18 09:16 .bash_profile
crw-rw-rw- 1 nobody nogroup   1, 3 Oct 18 09:16 .bashrc
drwxr-xr-x 5 runner runner    4096 Oct 18 09:42 .claude
-rw-r--r-- 1 runner runner       0 Oct 18 09:42 .env
-rw-r--r-- 1 runner runner       0 Oct 18 09:42 .env.development
-rw-r--r-- 1 runner runner       0 Oct 18 09:42 .env.development.local
-rw-r--r-- 1 runner runner       0 Oct 18 09:42 .env.local
-rw-r--r-- 1 runner runner       0 Oct 18 09:42 .env.production
-rw-r--r-- 1 runner runner       0 Oct 18 09:42 .env.production.local
-rw-r--r-- 1 runner runner       0 Oct 18 09:42 .env.test
-rw-r--r-- 1 runner runner       0 Oct 18 09:42 .env.test.local
drwx------ 2 runner runner    4096 Oct 18 09:42 .git
crw-rw-rw- 1 nobody nogroup   1, 3 Oct 18 09:16 .gitconfig
crw-rw-rw- 1 nobody nogroup   1, 3 Oct 18 09:16 .github
-rw-r--r-- 1 runner runner       0 Oct 18 09:42 .gitmodules
crw-rw-rw- 1 nobody nogroup   1, 3 Oct 18 09:16 .idea
crw-rw-rw- 1 nobody nogroup   1, 3 Oct 18 09:16 .mcp.json
[... 96 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat README.md; echo ======; cat 000971-seiler-2022-01.yaml
```

```
<persisted-output>
Output too large (44.1KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work--temp-work/857e38bb-8b43-44ba-b749-c4a1944f6233/tool-results/br9kh7h5k.txt

Preview (first 2KB):
# Seiler et al. (2022) from dandiset 000971

Tests the findings of [Seiler et al. (2022)](https://doi.org/10.1016/j.cub.2022.01.055) that can be
tested on [DANDI:000971](https://dandiarchive.org/dandiset/000971/0.261013.1707), which holds the operant
behavior of a fiber photometry cohort (RI60 and RR20 mice) and of three optogenetic cohorts, DMS and DLS
dopamine axon photometry during RI60 and RR20 training, and western blot images. Photometry during RI30
and the shock probes, fear conditioning, open field and histology are not in it.

| Claim | Outcome |
|---|---|
| RI60 mice accept more shocks than RR20 mice | Not reproduced |
| RI60 mice take longer on the omission probe than RR20 mice | Partially reproduced |
| Late shocks and omission time are not correlated | Reproduced |
| The phenotype rule gives 9 PR, 9 DPR and 18 PS mice | Partially reproduced |
| Only DPR mice accept more shocks on the late probe | Reproduced |
| PR and DPR mice nosepoke faster than PS mice | Reproduced |
[... 17 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "README.md"
}
```

```
1	# Seiler et al. (2022) from dandiset 000971
2	
3	Tests the findings of [Seiler et al. (2022)](https://doi.org/10.1016/j.cub.2022.01.055) that can be
4	tested on [DANDI:000971](https://dandiarchive.org/dandiset/000971/0.261013.1707), which holds the operant
5	behavior of a fiber photometry cohort (RI60 and RR20 mice) and of three optogenetic cohorts, DMS and DLS
6	dopamine axon photometry during RI60 and RR20 training, and western blot images. Photometry during RI30
7	and the shock probes, fear conditioning, open field and histology are not in it.
8	
9	| Claim | Outcome |
10	|---|---|
11	| RI60 mice accept more shocks than RR20 mice | Not reproduced |
12	| RI60 mice take longer on the omission probe than RR20 mice | Partially reproduced |
13	| Late shocks and omission time are not correlated | Reproduced |
14	| The phenotype rule gives 9 PR, 9 DPR and 18 PS mice | Partially reproduced |
15	| Only DPR mice accept more shocks on the late probe | Reproduced |
16	| PR and DPR mice nosepoke faster than PS mice | Reproduced |
17	| PR mice take longer on the omission probe than PS mice | Reproduced |
18	| PS mice wait longer after a reward | Partially reproduced |
19	| PS mice make fewer extra nosepokes than PR mice | Partially reproduced |
20	| PS mice have longer inter-reward intervals | Reproduced |
[... 40 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "000971-seiler-2022-01.yaml"
}
```

```
1	schema_version: 1
2	id: 000971-seiler-2022-01
3	dandiset: "000971"
4	dandiset_version: 0.261013.1707
5	paper: doi:10.1016/j.cub.2022.01.055
6	date: 2026-10-18
7	entry: 000971-seiler-2022
8	provenance:
9	  kind: agent
10	  accountable:
11	    name: CatalystNeuro
12	  agent:
13	    harness: Claude Code (GitHub Actions)
14	    model: claude-opus-5-5
15	    protocol: pilot-7
16	inputs:
17	- what: The authors' photometry analysis code (IndividualPhotometryAnalysis.m and helpers), read for the
18	    smoothing, the control fit, dF/F, the z-score, the removal of the first second, the 2 s burst rule
19	    for unrewarded nosepokes and the PSTH alignment, which the analysis follows.
20	  source: https://github.com/jillianseiler/Seiler-et-al.-2022-MATLAB-code at commit
[... 719 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python3 -c "
import yaml;d=yaml.safe_load(open('10.1016-j.cub.2022.01.055.yaml'));print(d.keys())
cl=d.get('claims')
print(len(cl))
" ; head -c 3000 10.1016-j.cub.2022.01.055.yaml
```

```
dict_keys(['schema_version', 'dandiset', 'paper', 'claims'])
38
# Claims for Seiler, Cosme, Sherathiya, Schaid, Bianco, Bridgemohan & Lerner (2022) on dandiset 000971.
# Source: the accepted author manuscript in PubMed Central (PMC8930615), full text: Results, figure
# legends and STAR Methods. The supplementary figures (NIHMS1775870-supplement-3.pdf) could not be
# downloaded (the server returned a browser check), so claims on Figures S1 to S7 rest on the main
# text only.
#
# When these criteria were written, the author had seen the data check only: the file list and
# session descriptions of every file, the event series each file holds, the punishment group label
# stored in each fiber photometry subject's notes, the number of shocks in each shock probe file
# (and so the early and late probe values of each mouse), which sessions carry photometry, and, for
# one photometry session, the rewarded nosepoke response in each of the four photometry columns
# (to check which column is the calcium signal). No claim's statistics had been run. The authors'
# MATLAB code (GitHub jillianseiler/Seiler-et-al.-2022-MATLAB-code at commit 56f1529) and the
# conversion code and notes (GitHub catalystneuro/lerner-lab-to-nwb at commit d301f7e) had been read.
#
# Method choices fixed here, from the Methods, then the authors' code, where the Methods are silent:
# - Shock probe value: the number of entries in a probe file's footshock_times. When a mouse has more
#   than one probe file on one day, the last file of the day that holds footshock_times is used; the
[... 16 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python3 - <<'EOF' > $TMPDIR/nb.txt
import json
nb=json.load(open('reproduce_seiler_2022.ipynb'))
for i,c in enumerate(nb['cells']):
    print(f"\n######## CELL {i} [{c['cell_type']}]")
    print(''.join(c['source']))
    for o in c.get('outputs',[]):
        if 'text' in o: print('--OUT--\n'+''.join(o['text']))
        elif 'data' in o:
            d=o['data']
            if 'text/plain' in d: print('--OUT--\n'+''.join(d['text/plain']))
        elif o.get('output_type')=='error': print('--ERR--',o['ename'],o['evalue'])
EOF
wc -l $TMPDIR/nb.txt; grep -c "######## CELL" $TMPDIR/nb.txt
```

```
2565 /tmp/claude-1001/nb.txt
134
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/nb.txt",
 "limit": 700
}
```

```
1	
2	######## CELL 0 [markdown]
3	# Reproducing Seiler et al. (2022) from dandiset 000971
4	
5	Paper. Seiler JL, Cosme CV, Sherathiya VN, Schaid MD, Bianco JM, Bridgemohan AS, Lerner TN (2022).
6	Dopamine signaling in the dorsomedial striatum promotes compulsive behavior. *Current Biology* 32,
7	1175-1188. [doi:10.1016/j.cub.2022.01.055](https://doi.org/10.1016/j.cub.2022.01.055). This attempt
8	used the full text of the accepted author manuscript in PubMed Central (PMC8930615). The supplementary
9	figures could not be downloaded, so claims on Figures S1 to S7 rest on the main text.
10	
11	Dandiset. [DANDI:000971](https://dandiarchive.org/dandiset/000971/0.261013.1707), version
12	0.261013.1707. The paper predates the dandiset and cites no version. This is the most recent published
13	version. All three published versions (0.240802.2004, 0.260213.1851, 0.261013.1707) and the draft hold
14	the same 4139 assets with the same blobs; they differ only in dandiset metadata (contributors, ORCIDs,
15	study targets), none of which the analysis uses.
16	
17	Code read. The authors' photometry code (GitHub `jillianseiler/Seiler-et-al.-2022-MATLAB-code`,
18	commit 56f1529) and the conversion code with its notes (GitHub `catalystneuro/lerner-lab-to-nwb`,
19	commit d301f7e). The photometry processing here follows the authors' code where the Methods are silent.
20	
[... 680 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/nb.txt",
 "offset": 700,
 "limit": 700
}
```

```
700	print("Training sessions used (up to the late probe):", len(tr), "; per mouse", per_mouse.sessions.min(), "to", per_mouse.sessions.max())
701	print("Sessions without port entries (no wait or extra nosepokes):", int((~tr.has_ports).sum()))
702	print("Ranges: rate", tr.rate.min().round(2), "to", tr.rate.max().round(1), "per min; rewards", tr.n_rewards.min(), "to", tr.n_rewards.max())
703	print(per_mouse.groupby("pheno").size().to_string())
704	--OUT--
705	Training sessions used (up to the late probe): 551 ; per mouse 7 to 19
706	Sessions without port entries (no wait or extra nosepokes): 0
707	Ranges: rate 0.02 to 39.7 per min; rewards 1 to 50
708	pheno
709	DPR      9
710	PR       9
711	PS      18
712	RR20     6
713	
714	
715	######## CELL 20 [code]
716	print(f"Training files with 0 rewards: {(tr_all.n_rewards == 0).sum()}; with 0 active nosepokes: {(tr_all.n_active == 0).sum()}; "
717	      f"both, left out: {len(empty)} of {len(tr_all)}")
718	print(empty[["subject", "pheno", "stage", "date", "size_mb", "series_names", "n_events", "last_event_s"]]
719	      .round(2).sort_values(["pheno", "subject", "date"]).to_string(index=False))
[... 680 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/nb.txt",
 "offset": 1400,
 "limit": 600
}
```

```
1400	Unpaired t-test: t = 5.96, p = 5.4e-07
1401	Variant with the empty files kept: {'RI60': 41.89, 'RR20': 15.38} ; t-test p = 1.4e-11
1402	Active nosepokes per minute by schedule (Fig S1G, similar rates): {'RI60': {'mean': 9.39, 'std': 5.81}, 'RR20': {'mean': 7.92, 'std': 3.97}}
1403	
1404	
1405	######## CELL 60 [markdown]
1406	**Result: reproduced.** RI60 mice earn 41.97 rewards per training session and RR20 mice 22.63
1407	(t-test p = 5.4e-07, not below the paper's 0.0001). With the 20 RR20 files that hold port entries only
1408	counted as sessions of 0 rewards, the RR20 mean is 15.38 and p = 1.4e-11. Only 6 RR20 mice are in the
1409	dandiset.
1410	
1411	
1412	######## CELL 61 [markdown]
1413	### figs2b-males-more-shocks
1414	
1415	> Male mice accept more shocks than female mice in the shock probes (main effect of sex, F1,35 = 26.19,
1416	> p < 0.0001).
1417	
1418	######## CELL 62 [code]
1419	aov3, w3 = mixed_anova(ri_long, "sex")
[... 580 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/nb.txt",
 "offset": 2000,
 "limit": 600
}
```

```
2000	pheno          DPR  PR  PS
2001	subject_arm               
2002	ChR2             0  12   1
2003	ChR2Scrambled    3   6   3
2004	EYFP             0   5   2
2005	Fraction PR: {'ChR2': 0.923, 'ChR2Scrambled': 0.5, 'EYFP': 0.714}
2006	Fisher exact, PR vs not, ChR2 vs both controls: odds ratio 8.73, p = 0.0497
2007	Fiber photometry RI60 mice, for reference: {'PS': 0.531, 'DPR': 0.281, 'PR': 0.188}
2008	
2009	
2010	######## CELL 97 [markdown]
2011	**Result: reproduced.** 12 of 13 ChR2 mice are PR (92%), against 5 of 7 EYFP (71%) and 6 of 12
2012	ChR2 Scrambled (50%); Fisher's test of ChR2 against both controls gives p = 0.0497. The control
2013	proportions are higher than in the fiber photometry cohort (19% PR).
2014	
2015	######## CELL 98 [markdown]
2016	### figs5f-chr2-pr-by-sex
2017	
2018	> Under DMS ChR2 stimulation 100% of male mice and about 71% of female mice are PR.
2019	
[... 547 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 30,80p 10.1016-j.cub.2022.01.055.yaml; grep -n "fig2n" -A30 10.1016-j.cub.2022.01.055.yaml | head -50; python3 -c "
import yaml,collections
a=yaml.safe_load(open('000971-seiler-2022-01.yaml'));c=yaml.safe_load(open('10.1016-j.cub.2022.01.055.yaml'))
print(len(a['outcomes']),collections.Counter(o['outcome'] for o in a['outcomes']))
print(set(x['id'] for x in c['claims'])==set(o['claim'] for o in a['outcomes']))
v=a['verifications'][0]['results'];print(len(v),collections.Counter(r['agrees'] for r in v))
print([ (r['claim'],r['outcome'],o['outcome']) for r,o in zip(v,a['outcomes']) if r['outcome']!=o['outcome']])
"
```

```
# - Photometry (authors' code): 100-sample moving average applied forward and backward to both
#   channels; least-squares fit of the 405 nm channel to the 465 nm channel; dF/F = (465 - fit) / fit;
#   z-score over the session; first second of the session dropped. Unrewarded nosepokes are active
#   nosepokes that are not rewarded, less those within 2 s of the previous unrewarded nosepoke. Score
#   = maximum of the mean rewarded nosepoke PSTH in 0 to 1.5 s minus the minimum of the mean
#   unrewarded nosepoke PSTH in 0 to 1.5 s (Methods). Early RI60 sessions are photometry sessions held
#   before the mouse's first shock probe (or within its first 3 RI60 days when it has no early probe);
#   late sessions are those after it.
# - Where the paper states a mixed-effects analysis, a linear mixed model with a random intercept per
#   mouse is used, and effects are tested by likelihood ratio. Tukey tests use statsmodels.
schema_version: 1
dandiset: "000971"
paper: doi:10.1016/j.cub.2022.01.055
claims:
- id: fig1d-ri60-vs-rr20-shocks
  statement: Mice trained on RI60 accept more shocks in the shock probes than mice trained on RR20
    (main effect of schedule, F1,43 = 6.37, p < 0.05; schedule by time interaction, F1,43 = 4.54,
    p < 0.05), and RI60 mice accept more shocks on the late probe than on the early one (p < 0.01).
  source: Results, first section; Figure 1D
  criterion: Mice of the fiber photometry experiment with both probes. A two-way mixed ANOVA
[... 66 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n -A14 "id: fig5f\|id: fig7f\|id: fig6-nphr\|id: fig3g\|id: fig4g" 10.1016-j.cub.2022.01.055.yaml | grep -v "^\-\-$" | head -90
```

```
232:- id: fig3g-dms-score-shock-correlation
233-  statement: The DMS rewarded-unrewarded peak score correlates with the shocks a mouse receives in
234-    the shock probes (r = 0.53, p < 0.0001).
235-  source: Results, third section; Figure 3G
236-  expected:
237-    quantity: Pearson r between DMS peak score and shocks received
238-    value: 0.53
239-    tolerance: 0.053
240-  criterion: Readings, before the analysis. (a) Pooled pairs of the early RI60 score with the early
241-    probe count and the late RI60 score with the late probe count; (b) late pairs only; (c) early
242-    pairs only. Reproduced when under one reading r is within tolerance and p < 0.05. Partially
243-    reproduced when r > 0 with p < 0.05 but no reading is within tolerance. Not reproduced otherwise.
244-- id: fig3h-dms-score-omission-no-correlation
245-  statement: The DMS rewarded-unrewarded peak score does not correlate with omission completion time
246-    (r = 0.1, ns).
256:- id: fig4g-dls-score-shock-no-correlation
257-  statement: The DLS rewarded-unrewarded peak score does not correlate with shocks received (r =
258-    -0.01, ns).
259-  source: Results, fourth section; Figure 4G
260-  criterion: Absence claim. Pearson correlation on the pooled pairs of reading (a) of
[... 52 more lines not kept]
```

**Agent calls Grep**

```json
{
 "pattern": "def dropout_mask|median|def zscored_dff",
 "path": "seiler.py",
 "output_mode": "content",
 "-A": 3
}
```

```
29:  channel median, and 1 s around them, are left out (a choice here; the Methods say only that
30-  recordings with excessive artifacts were excluded). The code's processing without this step is
31-  available with mask_dropouts=False.
32-- Rewarded port entry, extra nosepokes and the wait after reward (Figure 2K and 2L) are defined
--
64:DROPOUT_FRACTION = 0.5       # a choice here: raw samples below half the channel median are dropouts
65-DROPOUT_PAD_S = 1.0          # a choice here: and 1 s on each side of them is left out
66-
67-STAGES = [("Footshock Probe", "shock"), ("Omission Probe", "omission"), ("RI60 Training", "RI60"),
--
258:def dropout_mask(signal: np.ndarray, control: np.ndarray, fs: float) -> np.ndarray:
259:    """Samples near a dropout: either channel below DROPOUT_FRACTION of its median, widened by
260-    DROPOUT_PAD_S on each side. A choice here; the authors' code has no such step."""
261:    bad = (signal < DROPOUT_FRACTION * np.median(signal)) | (control < DROPOUT_FRACTION * np.median(control))
262-    if not bad.any():
263-        return bad
264-    pad = int(round(DROPOUT_PAD_S * fs))
--
268:def zscored_dff(signal: np.ndarray, control: np.ndarray, fs: float, mask_dropouts: bool = True) -> np.ndarray:
269-    """As IndividualPhotometryAnalysis.m: smooth, fit control to signal, dF/F, z-score.
[... 2 more lines not kept]
```

**Agent**

## Round 2 verifier report: Seiler et al. (2022), dandiset 000971 v0.261013.1707

Counts are taken from the claims file (38 claims) and from the attempt record's outcomes: 18 reproduced, 9 partially reproduced, 6 not reproduced, 5 blocked. Since round 1, two outcomes have changed: fig6-nphr-learning-dropout is now blocked, as I recommended, and fig2n-rewards-per-session went from reproduced to partially reproduced. I did not re-download the paper. The checks below use the claims file, the notebook outputs and my round-1 reading.

### 1. Outcomes

I agree with all 38 stated outcomes. Three need a note:

- **fig2n-rewards-per-session (partially_reproduced).** I accept this outcome, but it sits on the threshold, and which result you get depends on a rule chosen after round 1.
  - The claims file defines sessions as the files described as RI60 training. Under that definition the 170 s file of 140.306 is included and Tukey PS vs DPR gives p = 0.048 (cell 53), which would be reproduced.
  - Leaving out that one file gives p = 0.059. Keeping one file per mouse-day gives p = 0.044.
  - The stated reason for leaving it out is "a false start followed by a full session the same day". That reason applies just as well to files the analysis keeps: 271.396 (2 rewards, 720 s), 88.239 (1 reward on two days), 92.246 (4 rewards), 348.393 and 115.273 (3 rewards). Removing all of those is what the one-file-per-mouse-day variant does, and it gives 0.044.
  - Partially reproduced is the conservative choice and every variant is reported, so I accept it. The claim should still be read as borderline.
- **fig6-nphr-learning-dropout (blocked).** I agree. Cell 105 shows the shortfall against Figure 6F is 3, 2 and 0 mice, the "Did Not Learn" flag also marks an EYFP mouse, and no file says which group a mouse was in.
- **fig5f and fig7f (not_reproduced).** I agree, because the criterion fixed the pooled least-squares fit before the analysis. In both, a mixed model with a per-mouse slope reverses the result (cells 90 and 117).

### 2. Sentences the numbers do not support

**Result conclusions, Summary, README and notes**

- **Cell 73:** "The dropout step leaves out more than 1% of samples in only one DMS session of the 51 behind these pairs (1.61%)."
  - The count is correct, but the sentence suggests the step has little effect. Cell 72's table shows it changes DMS scores a lot in sessions where it leaves out 1.61% or less: 88.239 goes from 0.09 to 1.92, 048.392 from 0.02 to 1.81, 346.394 from 0.00 to 1.10, and 92.246 from 0.04 to 0.30.
  - The fig3g response in the attempt record ("one DMS session above 1%") carries the same implication.
- **Summary (cell 133) and the fig2c and fig2n deviations:** "Training files with no nosepoke and no reward are left out."
  - The 140.306 file holds `left_nose_poke_times` (30 events in the file, cell 20). It has no active nosepoke, which is what cell 21 says correctly.
- **Cell 60, and the figs1i notes:** "With the 20 RR20 files that hold port entries only counted as sessions of 0 rewards…"
  - That variant also keeps the RI60 false start (RI60 mean 41.89 instead of 41.97, cell 59). This is minor and does not change the result.
- **Cell 91, and the fig5f notes:** "A mixed model … agrees with the per-mouse slopes."
  - The fit converged only after a retry with lbfgs and warns that "the MLE may be on the boundary" (cell 90).
- **Cell 118, and the fig7f notes:** the mixed-model p values (0.43 to 0.96) are reported with no caveat.
  - Cell 117 prints repeated "Random effects covariance is singular" warnings, so those p values are weak evidence that the result rests on the pooled fit.

Every other "**Result:" sentence, the Summary, the README and the outcome notes match the printed outputs. That includes the counts (33/39, 42/47, 6/9 mice), the p values, the means, the 2336/2337 and 10892/10916 event counts, and the runtime of about 25 minutes (1407 s).

**My round-1 reasons in the attempt record**

These are stated accurately and in my wording, each with its B point. Two small things:

- The fig6 reason leaves out my note that applying the criterion literally would have given not_reproduced. That point no longer matters now that the claim is blocked.
- The fig2n entry correctly records my round-1 outcome as reproduced.

### 3. Round-1 points

**Resolved (fixed in the notebook, or disclosed in the conclusion and notes):**

- B1: dropout step dependence stated, with variants.
- B2: Bonferroni p = 0.13 and the no-dropout-step readings added.
- B3: mixed-model variant added.
- B4: fig6 changed to blocked.
- B5: variance ratio of 251 reported.
- B6: table of the empty files and variants added.
- B7: per-stage mouse counts against Figure 3E given.
- B8: per-mouse wait table added.
- B9: counts said to match by construction.
- B10: events kept now printed.
- B11: 95% intervals of r added.
- B12: RI60 part of fig3e shown.
- C: Zenodo blocks printed, fig3g without the dropout step shown, per-session dropout fractions shown.

**Still open, and bearing on a conclusion:**

- **fig4g (and fig3f, fig3g).** The outcome still depends on the dropout step, which was chosen after seeing the data and is in neither the Methods nor the authors' code. This is now disclosed. In the sessions with large dropouts the authors' processing gives scores near 0 (cell 72), which supports the step but cannot prove it is right.
- **fig2n.** The outcome changes with the session-exclusion rule (p = 0.048, 0.059 or 0.044). The rule used is the only one of the three above 0.05 and is narrower than the false-start reason given for it.
- **fig5f and fig7f.** Both outcomes rest on a pooled fit with no mouse term. The mixed models that reverse them have convergence or singularity warnings that the conclusions do not mention.
- **Not resolved: Figure S1 to S7 legends.** figs1i, figs2b, figs5f and figs3ab are still judged on the main text alone.

## End of run

14 turns, 2 minutes, result: success.
