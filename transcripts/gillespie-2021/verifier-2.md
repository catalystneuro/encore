# 000115 · verifier-2 · run 39965757224

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
ls -la; cat round-1-report.md; ls docs paper 2>/dev/null
```

```
Exit code 2
total 480
drwxr-xr-x 6 runner runner    4096 Oct 23 14:07 .
drwxr-xr-x 7 runner runner    4096 Oct 23 14:07 ..
crw-rw-rw- 1 nobody nogroup   1, 3 Oct 23 13:58 .bash_profile
crw-rw-rw- 1 nobody nogroup   1, 3 Oct 23 13:58 .bashrc
drwxr-xr-x 5 runner runner    4096 Oct 23 14:07 .claude
-rw-r--r-- 1 runner runner       0 Oct 23 14:07 .env
-rw-r--r-- 1 runner runner       0 Oct 23 14:07 .env.development
-rw-r--r-- 1 runner runner       0 Oct 23 14:07 .env.development.local
-rw-r--r-- 1 runner runner       0 Oct 23 14:07 .env.local
-rw-r--r-- 1 runner runner       0 Oct 23 14:07 .env.production
-rw-r--r-- 1 runner runner       0 Oct 23 14:07 .env.production.local
-rw-r--r-- 1 runner runner       0 Oct 23 14:07 .env.test
-rw-r--r-- 1 runner runner       0 Oct 23 14:07 .env.test.local
drwx------ 2 runner runner      40 Oct 23 14:07 .git
crw-rw-rw- 1 nobody nogroup   1, 3 Oct 23 13:58 .gitconfig
crw-rw-rw- 1 nobody nogroup   1, 3 Oct 23 13:58 .github
-rw-r--r-- 1 runner runner       0 Oct 23 14:07 .gitmodules
crw-rw-rw- 1 nobody nogroup   1, 3 Oct 23 13:58 .idea
[... 69 more lines not kept]
```

**Agent calls Bash**

```bash
cat 000115-gillespie-2021-01.yaml
```

```
<persisted-output>
Output too large (47.1KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work--temp-work/5bd99b26-4d77-4c13-b25b-f69422ba5d28/tool-results/bhflo1ao7.txt

Preview (first 2KB):
schema_version: 2
id: 000115-gillespie-2021-01
dataset:
  archive: dandi
  id: '000115'
  version: 0.210914.1732
  doi: 10.48324/dandi.000115/0.210914.1732
paper: doi:10.1016/j.neuron.2021.07.029
date: '2026-10-22'
entry: 000115-gillespie-2021
provenance:
  kind: agent
  accountable:
    name: CatalystNeuro
  agent:
    harness: Claude Code (GitHub Actions)
[... 33 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "000115-gillespie-2021-01.yaml"
}
```

```
1	schema_version: 2
2	id: 000115-gillespie-2021-01
3	dataset:
4	  archive: dandi
5	  id: '000115'
6	  version: 0.210914.1732
7	  doi: 10.48324/dandi.000115/0.210914.1732
8	paper: doi:10.1016/j.neuron.2021.07.029
9	date: '2026-10-22'
10	entry: 000115-gillespie-2021
11	provenance:
12	  kind: agent
13	  accountable:
14	    name: CatalystNeuro
15	  agent:
16	    harness: Claude Code (GitHub Actions)
17	    model: claude-opus-5-5
18	    protocol: pilot-10
19	  runner:
20	    platform: GitHub Actions
[... 791 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "10.1016-j.neuron.2021.07.029.yaml"
}
```

```
1	# Claims for Gillespie, Astudillo Maya, Denovellis, Liu, Kastner, Coulter, Roumis, Eden & Frank
2	# (2021), Neuron 109, 3149-3163, on dandiset 000115.
3	# Written by an agent (model "claude-opus-5-5", Claude Code in GitHub Actions), 2026-10-22,
4	# protocol pilot-10 as stated in docs/protocol.md.
5	#
6	# Text read: the accepted author manuscript in PubMed Central (PMC8497431, NIHMS1731801), in
7	# paper/10.1016-j.neuron.2021.07.029.txt: Summary, Introduction, Results, Discussion, STAR
8	# Methods, all figure legends, and the Supplemental Information PDF (Supplementary Figures 1
9	# to 8 with legends), extracted into the same file. The version of record was not read; the
10	# bioRxiv preprint (version 2, paper/10.1101-2021.03.09.434621.txt) was not used for claims.
11	# The PDF was not needed: every claim rests on a sentence or a legend.
12	#
13	# Code read: the analysis code the paper links (doi:10.5281/zenodo.5140706), which is the
14	# GitHub repository LorenFrankLab/Gillespie_Neuron_2021, tag v1.0, commit
15	# 1be6a6a7dbd806154a544d6f509452617e52d8c3 (the later head 48108d8 changes only the README).
16	# MATLAB scripts in the Frank lab filter framework. dfs_ripcontent.m, parts 1 to 16, makes
17	# Figures 1D to 8 and Supplementary Figures 1, 3G-H, 5 to 8 (its README maps parts to
18	# panels); dfa_ripcontent.m labels trials and assigns each SWR to a trial phase;
19	# utilities/label_trial_interval.m codes each trial's task phase; dfa_makeFFripdecodes.m
20	# summarises the decoder posterior over each SWR; dfs_decodequant_movement.m makes
[... 863 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python3 -c "
import json
nb=json.load(open('reproduce_gillespie_2021.ipynb'))
for i,c in enumerate(nb['cells']):
    src=''.join(c['source'])
    print(f'=== cell {i} [{c[\"cell_type\"]}] len={len(src)}')
    print(src[:300].replace('\n',' | '))
"; find / -iname 'README*' -path '*000115*' 2>/dev/null | head
```

```
=== cell 0 [markdown] len=3780
# Reproducing Gillespie et al. (2021) from dandiset 000115 |  | Paper. Gillespie AK, Astudillo Maya DA, Denovellis EL, Liu DF, Kastner DB, Coulter ME, | Roumis DK, Eden UT, Frank LM (2021). *Neuron* 109, 3149-3163. | [doi:10.1016/j.neuron.2021.07.029](https://doi.org/10.1016/j.neuron.2021.07.029). The claim
=== cell 1 [code] len=537
import time | import warnings |  | import matplotlib.pyplot as plt | import numpy as np | import pandas as pd | from scipy import stats |  | import replaytask as rt |  | pd.set_option("display.width", 220) | pd.set_option("display.max_columns", 40) | pd.set_option("display.max_rows", 200) | warnings.filterwarnings("ignore", 
=== cell 2 [markdown] len=88
## Data check |  | Each check of the metadata against the values is stated under its output.
=== cell 3 [code] len=1166
files = pd.DataFrame([{"subject": d["subject"], "day": d["day"], "session_id": d["session_id"], |                        "date": d["session_start"][:10], "epochs": " ".join(d["tags"]), |                        "run_epochs": len(d["runs"]), "GB": round(d["bytes"] / 1e9, 1), |                        "channe
=== cell 4 [markdown] len=465
The paper used 24, 32, 23 and 33 run sessions after excluding two of subject 1 (26, 32, 23 and | 33 before). The files hold 27, 32, 24 and 33 run epochs, all with the task | "Eight arm flexible spatial task / goal_delay"; jaq and despereaux have one more than the paper | reports. The electrode table gives
=== cell 5 [code] len=1686
runs = [] | for d in days: |     for r in d["runs"]: |         tr = r["trials"] |         v = tr[~tr.lockout] |         clk = rt.statescript_to_nwb_clock(r) |         runs.append({"subject": d["subject"], "day": d["day"], "epoch": r["epoch_index"], "tag": r["epoch_tag"], |                      "minutes": round(r[
=== cell 6 [code] len=1929
print("Run epochs per subject:", runs.groupby("subject").size().loc[rt.SUBJECTS].to_dict()) | print("Epoch length (min): median", runs.minutes.me
[... 48 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python3 -c "
import json
nb=json.load(open('reproduce_gillespie_2021.ipynb'))
for i,c in enumerate(nb['cells']):
    src=''.join(c['source'])
    print(f'=== cell {i} [{c[\"cell_type\"]}]')
    print(src)
    for o in c.get('outputs',[]):
        if 'text' in o: print('--OUT--'); print(''.join(o['text']))
        elif 'data' in o:
            d=o['data']
            if 'text/plain' in d: print('--OUT(data)--'); print(''.join(d['text/plain'])[:3000])
            else: print('--OUT--', list(d.keys()))
" > $TMPDIR/nb.txt; wc -l $TMPDIR/nb.txt
```

```
1441 /tmp/claude-1001/nb.txt
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/nb.txt"
}
```

```
1	=== cell 0 [markdown]
2	# Reproducing Gillespie et al. (2021) from dandiset 000115
3	
4	Paper. Gillespie AK, Astudillo Maya DA, Denovellis EL, Liu DF, Kastner DB, Coulter ME,
5	Roumis DK, Eden UT, Frank LM (2021). *Neuron* 109, 3149-3163.
6	[doi:10.1016/j.neuron.2021.07.029](https://doi.org/10.1016/j.neuron.2021.07.029). The claims file
7	was written from the accepted author manuscript in PubMed Central (PMC8497431) with its
8	Supplemental Information, and from the paper's code (LorenFrankLab/Gillespie_Neuron_2021, commit
9	1be6a6a).
10	
11	Dandiset. [DANDI:000115](https://dandiarchive.org/dandiset/000115/0.210914.1732), version
12	0.210914.1732 (doi:10.48324/dandi.000115/0.210914.1732). The paper cites no version, and its
13	code's README links the draft. 0.210914.1732 is the only published version, and it is pinned.
14	The draft (modified 2024-02-22) has the same 57 paths, but 55 of its files were rewritten in
15	January 2022 (NWB 2.4.0). The data check below compares one of them: the DIO timestamps agree to
16	within a microsecond, but the draft's position timestamps are no longer on the DIO clock, while
17	the published version's are. The published version therefore fits the analysis better as well as
18	being fixed.
19	
20	What the dandiset holds. One NWB file per recording day for each of four rats (jaq,
[... 518 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/nb.txt",
 "offset": 539,
 "limit": 450
}
```

```
539	      f"one 90-min run epoch ({90 * 60 * 30000 * 128 * 2 / 1e9:.0f} GB) {90 * 60 * 30000 * 128 * 2 / rate / 60:.0f} min")
540	--OUT--
541	 session  day  epoch  arms_visited  valid  rewards_log
542	       1    6      2             8    107           46
543	       2    6      4             7     66           30
544	       3    6      5             8    110           65
545	       4    7      2             8     74            6
546	       5    7      4             8    107           49
547	       6    8      2             8    101           45
548	jaq sessions with fewer than eight arms visited: [{'day': 6, 'epoch': 4, 'arms_visited': 7}]
549	Reading (b): second session (6, 4) ; 26 candidates for the first
550	
551	--OUT--
552	
553	Read 77 MB of raw broadband (300000 samples x 128 channels) in 8.1 s, 9.5 MB/s
554	At that rate the dandiset's 9.1 TB would take 267 h; one 90-min run epoch (41 GB) 73 min
555	
556	=== cell 13 [markdown]
557	The raw broadband is stored one channel per chunk of 212,978 to 329,259 samples (7 to 11 s),
558	so any time window must fetch every channel's chunk. The rate measured above puts streaming the
[... 430 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/nb.txt",
 "offset": 988,
 "limit": 460
}
```

```
988	
989	Criterion: per subject over the blocks with at least four rewards, the final unrewarded trial
990	dropped; a trial scores 1 when rewarded; binomial S.E.M.; trials 1 to 15. Reproduced when, in all
991	four subjects, the band on trial 1 of Figure 1E reaches 0.125 or lies below it, the rate rises
992	over trials 1 to 15, and every point of Figure 1F has its band above 0.125. "Rises" is shown two
993	ways: trial 15 against trial 1 (non-overlapping bands), and the Spearman correlation of the
994	rate with trial number. Blocks are those of fig1d-sessions-blocks, closed by the first trial after
995	each goal change (`replaytask.FINAL_TRIAL`); that closing trial is the one dropped. Sessions
996	follow readings (a) and (b), and for (b) every candidate first session of jaq is run. The
997	old-goal-visit rule is shown only to say what the answer changed.
998	=== cell 23 [code]
999	def curves(reading=None, final=rt.FINAL_TRIAL, exclude=None, subjects=rt.SUBJECTS):
1000	    ss = session_set(reading, exclude)
1001	    out = {}
1002	    for s in subjects:
1003	        S, R = [], []
1004	        for r in ss[ss.subject == s].run:
1005	            a, b = rt.reward_curves(rt.label_task_phase(r["trials"], final))
1006	            S.append(a); R.append(b)
1007	        out[s] = (np.vstack(S), np.vstack(R))
[... 435 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n "def \|adjacen\|neighbour\|VISIT_WINDOW\|FINAL_TRIAL" replaytask.py | head -60; grep -c "^- claim:" 000115-gillespie-2021-01.yaml; grep -c "^- id:" 10.1016-j.neuron.2021.07.029.yaml; ls | grep -i readme
```

```
33:  is `FINAL_TRIAL` = "first_after_switch". The other value of `FINAL_TRIAL_READINGS`,
40:  count as next to the goal, and arms 1 and 8 are not treated as neighbours.
71:FINAL_TRIAL_READINGS = ("first_after_switch", "old_goal_visit")
72:FINAL_TRIAL = "first_after_switch"   # claims file, opening comment
80:def list_assets():
93:def open_nwb(url):
97:def _s(x):
103:def parse_statescript(content):
115:def header_parameters(content):
124:def trials_from_events(events):
153:def label_task_phase(trials, final=FINAL_TRIAL):
211:def full_blocks(labelled):
217:def reward_curves(labelled):
240:VISIT_WINDOW = 40   # fig6b-visits-decay, as fig6a-pg-replay-persists: 40 trials either side
244:def visit_traces(labelled, completed_only=False):
257:    offs = np.arange(-VISIT_WINDOW, VISIT_WINDOW + 1)
274:def binomial_curve(mat):
284:def _events_on(group, start, stop):
290:def load_day(asset):
376:def load_all(assets, workers=12):
[... 6 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "replaytask.py",
 "offset": 25,
 "limit": 250
}
```

```
25	  the paper's code (LorenFrankLab/Gillespie_Neuron_2021 at 1be6a6a): 0 or -0.2 for search trials
26	  before the goal is found (-0.2 when the arm was already visited in this search), an integer n
27	  for the n-th reward of the block, n + 0.5 for an error at an arm next to the goal (arm number
28	  differs by 1), n + 0.3 for an error at the previous goal, n + 0.8 for other errors, and
29	  n + 0.9 for the final unrewarded visit to the old goal after the goal changes.
30	- The trial that closes a block: the claims file's opening comment (after a reader's answer)
31	  gives the first valid trial after each goal change to the old block, whatever arm it visits,
32	  as label_trial_interval.m (goalbounds) and dfa_ripcontent.m ("[1 ctemp(1:end-1)]") do. This
33	  is `FINAL_TRIAL` = "first_after_switch". The other value of `FINAL_TRIAL_READINGS`,
34	  "old_goal_visit" (only a visit to the old goal closes the block), was the second reading run
35	  before the answer; it is kept to show what the answer changed and decides nothing.
36	- A block counts for Figure 1D to 1F when it has a trial of task phase >= 4 (claims file,
37	  fig1d-sessions-blocks, from dfs_ripcontent.m part 2, `any(ctphase>=4)`).
38	- The error subtypes n + 0.3, 0.5 and 0.8 are not used by any test here (only integer phases,
39	  phase <= 1 against > 1 and the reward flags are); the claims file does not say which arms
40	  count as next to the goal, and arms 1 and 8 are not treated as neighbours.
41	- A log shows forage assist when a `CURRENTGOAL IS [...]` line lists more than one arm: with
42	  forageNum above 1 the observer's goalWell holds several arms until one is found (the
43	  observer code in the log headers); `n_multi_goal_lines` counts such lines.
44	- The visit traces of fig6b-visits-decay follow its criterion (as fig6a-pg-replay-persists, for
[... 230 more lines not kept]
```

**Agent calls Bash**

```bash
cd paper; grep -n -i "sessions 1 and 3\|not all arms\|75%\|returning to baseline\|Figure 6B\|(B) \|rank-sum\|ranksum" 10.1016-j.neuron.2021.07.029.txt | head -40
```

```
70:(B) Schematic illustrates the arm choices of the rat across the two trial types, search and repeat, that make up each block of trials.
100:(B) Decoded position for the movement period as the animal runs from a center port to the end of arm 5. Representative CA1 LFP trace is shown above.
126:(B) Left, boxplots of the fraction of remote replay events in the box area that represent the past, future, previous goal, or other arms during a subset of search phase trials in which past, future, and previous goal arms are distinct. Boxplot range reflects the variability in remote event fractions across sessions; only sessions with at least 5 trials that met the distinct arm criteria were included. N = 22, 23, 16, and 26 sessions per subject, respectively. Significance was calculated relative to a random distribution which was matched for remote event numbers per session for each subject using Wilcoxon rank-sum test. * indicates p<0.05; ** indicates p<0.01; *** indicates p<0.001. Right, total fraction of remote events corresponding to arms in the “other” category.
128:(C) As in (B) but using a subset of repeat trials when the past, future, and goal arms are the same and the previous goal arm is distinct. N = 23, 30, 22, and 31 sessions per subject, respectively.
154:(B) Same as (A) for trials when the subject has earned five or more rewards at the current goal location. N = 801, 895, 600, and 967 trials per subject; 8 entries per trial.
168:(A) Future replay per trial tends to occur less than once per trial, and more often during search trials than repeat trials for three of the four subjects. N = 534, 617, 570, and 879 search trials and 924, 1019, 894, 1302 repeat trials per subject, respectively. Search vs repeat rate p = 0.001, 5.002e-11, 0.264, and 4.111e-5 for each subject, respectively, using Wilcoxon rank-sum test.
170:(B) Rate of future arm replay during the repeat phase on correct (solid) compared to error (shaded) trials.
174:For (B) and (C), n = 923, 1007, 847, a
[... 19 more lines not kept]
```

**Agent**

**Verifier report, round 2: Gillespie et al. 2021 on DANDI:000115 (0.210914.1732)**

The claims file lists 33 claims. The attempt record has 33 outcomes: 2 reproduced (fig1d-sessions-blocks, fig1ef-reward-rate) and 31 blocked as too_large. There is no separate entry README among my materials, so I checked notebook cell 0, which acts as the entry text.

### 1. Outcomes

| claim | agree? | note |
|---|---|---|
| fig1d-sessions-blocks: reproduced | yes | Cell 20 matches round 1: 25/32/24/33 sessions and 88/85/109/166 blocks under reading (a); 26 of 26 candidates pass under (b) (jaq 88–93 blocks). The new variant leaves out one more jaq or despereaux epoch: 25/25 and 24/24 choices pass (jaq 82–87, despereaux 100–108 blocks). |
| fig1ef-reward-rate: reproduced | yes | Cell 23. The per-trial table is now printed and agrees with the summary columns. The plain reading of "rises" holds in all subjects. |
| fig6b-visits-decay: blocked, too_large | yes | The replay half is still not testable. The behavioural half (cell 27) holds in jaq, despereaux and montague (last significant trial +2 or +3) and fails in roquefort at +29 with the tie-corrected test. Without tie correction all four end at +2. |
| the other 30 claims: blocked, too_large | yes | Unchanged from round 1. |

The claims file reads the paper correctly on the points that bear on these results. I checked the Methods text on excluding "sessions 1 and 3 of subject 1", the trial-wise visit curves, and the eight-block limit.

### 2. Statements the printed outputs do not support

- **All 31 blocked notes in the attempt record:** "5 to 8.4 MB/s … (8.4 MB/s in the latest run)". Cell 12 of this run prints **9.5 MB/s** (77 MB in 8.1 s; 267 h for the dandiset; 73 min for one epoch). "Over an hour" and "hundreds of hours" still hold, so the reason stands, but the stated rate is wrong.
- **Cell 7 and the attempt record's finding:** "one more reward pump (arm 8) **226 s after the last logged reward**". No output prints this. Cell 15 prints the last logged trial at 2592 s and the extra pump at 2632 s, which is 40 s after the last trial. The 226 s may be right if measured from the last reward, but nothing printed shows it.
- **Cell 0:** "55 of its files were rewritten in January 2022". Only one file is compared (cell 10, montague day 4). Nothing printed shows 55.
- **Finding (metadata_error):** "110 of 116 run epochs **end with** 1 to 4 NaN position timestamps". Cell 10 prints the count of epochs with NaN timestamps, not where in the epoch they fall.
- **Cell 28 and the fig6b note:** "trial +1 (the closing trial)". `visit_traces` also takes the open last block of each session (any block with at least one reward). There, +1 is simply the next trial in the same block. The 0.84–0.90 figure covers both kinds of block.
- **fig1ef note:** "The closing-trial rule moves trial 15 for roquefort … and montague's Spearman rho …". This is true but incomplete. The rule also moves despereaux's rho (0.996 → 0.979) and its lowest 1F bound (0.420 → 0.429). It also moves jaq's trial 15 under reading (b) (0.696 → 0.681). No condition changes.

I checked every other sentence of the "**Result:" cells (21, 25, 28), cell 29, the Summary (cell 30), cells 4/7/9/11/13/16/18 and the record's notes against the outputs, and all of them hold. That includes 383/35/5 closing trials, 26/26 candidates, ratios within 5%/8%/4% and errors 11–24% over, 94/95/112/169 goal traces, 9 of 39 against 8 of 170 at p = 1.6e-4 / 0.074, and 0 of 116 logs with a multi-arm CURRENTGOAL line.

**My round-1 reasons in the attempt record:** they are faithful to my report and mostly close to my wording. "I confirmed" becomes "the verifier confirmed", and problems 1–4 and 6 are folded into the fig1d and fig1ef reasons accurately. No reason is misstated.

### 3. Round-1 points

**Resolved:**
- **1 (9- and 3-reward blocks):** explained in cells 15–16. Both follow a closing trial that was a rewarded visit to the new goal, and the outerreps printed are 10 and 4. The text was corrected.
- **2 (five logs without a header):** none has a multi-arm CURRENTGOAL line (cell 15).
- **3 (arms in jaq day 6 epoch 4):** the DIO beam breaks show arm 6 was never entered, including after the last logged trial. It is the only jaq session with fewer than eight arms.
- **5 (arms 1 and 8 not adjacent):** documented in the helper module's docstring. Only the error subtypes use it, and no test here does.
- **6 (E_rises stricter than the criterion):** acknowledged, and the plain reading was added and holds.
- **7 (behavioural half of fig6b):** computed in cell 27.
- **Section C requests:** all supplied (trial counts against the legends, per-session table, DIO arms, per-trial 1E/1F values, fig6b curves).

**Partly resolved:**
- **4 (the extra jaq and despereaux epochs):** these are still not identified. The leave-one-out variant shows the fig1d outcome does not depend on which one it is, so the conclusion is unaffected. The record notes that the paper's repository holds a saved filter output with per-animal epoch lists that might identify them; it was not used.

**Remaining points that bear on a conclusion:**
- **fig6b behavioural half:** the roquefort result depends on whether the rank-sum test corrects for ties, and that question is still open. To my knowledge, MATLAB's `ranksum` (the paper's code is MATLAB) corrects for ties in its normal approximation. If so, the tie-corrected form is the code's, and the behavioural half fails in roquefort under both bounds. The notebook did not look at why trial +29 is significant. The outcome stays blocked either way.
- **Error-trial labelling:** error trials are 11–24% above the Figure 5B counts (cell 17). No tested claim uses them, but any later analysis of correct against error trials would.
- **Corrections needed in the text, none changing an outcome:**
  - the streaming rate stated in all 31 blocked notes (9.5 MB/s, not 8.4);
  - the unprinted "226 s", "55 files" and "end with" statements;
  - the "+1 (the closing trial)" wording for fig6b.

## End of run

13 turns, 5 minutes, result: success.
