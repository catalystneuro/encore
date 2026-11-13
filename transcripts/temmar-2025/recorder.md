# temmar-2025 · recorder · run 43372718334

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  git log --diff-filter=A --name-only --format= -- docs/pilot-notes | head -n 5; python tools/readme_row.py temmar-2025; ls transcripts/temmar-2025/; cat attempts/temmar-2025-01.yaml; cat claims/temmar-2025.yaml
```

```
<persisted-output>
Output too large (93.4KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/d3530b31-899f-4482-b306-640525ef5f69/tool-results/bk8su2b2o.txt

Preview (first 2KB):
docs/pilot-notes/amjad-2025-01.md
docs/pilot-notes/armstrong-2026-01.md
docs/pilot-notes/ashworth-2025-01.md
docs/pilot-notes/athalye-2023-01.md
docs/pilot-notes/azcorra-2023-01.md
| [001201](https://dandiarchive.org/dandiset/001201) | [Temmar et al. 2025](https://doi.org/10.52202/085713-4642) | 17 | 3 | 3 | 1 | [`temmar-2025`](entries/temmar-2025) |
answer-report.md
answer.md
author-answers-report.md
author-answers.md
author-report.md
author-revise-1-report.md
author-revise-1.md
author-revise-2-report.md
author-revise-2.md
author-revise-3-report.md
[... 55 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/d3530b31-899f-4482-b306-640525ef5f69/tool-results/bk8su2b2o.txt"
}
```

```
1	docs/pilot-notes/amjad-2025-01.md
2	docs/pilot-notes/armstrong-2026-01.md
3	docs/pilot-notes/ashworth-2025-01.md
4	docs/pilot-notes/athalye-2023-01.md
5	docs/pilot-notes/azcorra-2023-01.md
6	| [001201](https://dandiarchive.org/dandiset/001201) | [Temmar et al. 2025](https://doi.org/10.52202/085713-4642) | 17 | 3 | 3 | 1 | [`temmar-2025`](entries/temmar-2025) |
7	answer-report.md
8	answer.md
9	author-answers-report.md
10	author-answers.md
11	author-report.md
12	author-revise-1-report.md
13	author-revise-1.md
14	author-revise-2-report.md
15	author-revise-2.md
16	author-revise-3-report.md
17	author-revise-3.md
18	author.md
19	claims-check-report.md
20	claims-check.md
[... 830 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/d3530b31-899f-4482-b306-640525ef5f69/tool-results/bk8su2b2o.txt",
 "offset": 850,
 "limit": 620
}
```

```
850	    reason: >-
851	      Agreed under the criterion's starting values. The legend-start pass rests only on point estimates:
852	      the 95% intervals of the initial rates include zero in all four legend fits and overlap widely
853	      (training day -2.09 to 0.28 against -0.62 to 0.25; test day -1.53 to 0.33 against -1.91 to 0.84,
854	      multiday [11]). The criterion's starting values have positive rates and look like the 5-session
855	      legend values reordered with their signs dropped; this may be another claims-file misreading, and
856	      is with a reader. It is fit on 12 day-0 sessions only.
857	    response: >-
858	      Outcome kept. The notebook's conclusion and the notes now give the initial-rate intervals and say
859	      the legend-start pass rests on point estimates. The question on the starting values was already in
860	      questions/temmar-2025.yaml; its reasoning now adds the intervals.
861	  - claim: fig5b-finetune
862	    agrees: true
863	    outcome: blocked
864	    reason: >-
865	      Agreed. The run in the notes is not in the entry, so it cannot be checked, and "had not finished
866	      after 52 minutes" has no output in the materials. The cost is understated: the printed fit times are
867	      about 2.8 times round 1's 0.037 s per iteration, which puts the full run at about 18 hours, against
868	      "about twice that". The 30 s arm is now about 2.8 times costlier than estimated in round 1, so the
869	      block is reasonable.
[... 599 more lines not kept]
```

**Agent calls Bash**

```bash
cd  for f in amjad-2025-01 armstrong-2026-01 ashworth-2025-01 athalye-2023-01 azcorra-2023-01; do echo "=== $f"; cat docs/pilot-notes/$f.md; done; echo; head -5 docs/pilot-notes/knierim-2000-02.md; python -c "
import json;d=json.load(open('targets/dandisets.json'))
items=d if isinstance(d,list) else d.get('dandisets',d)
for x in (items if isinstance(items,list) else items.values()):
  if '001201' in json.dumps(x)[:200]: print(json.dumps(x,indent=1))
"; ls -la transcripts/temmar-2025/
```

```
<persisted-output>
Output too large (37.8KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/d3530b31-899f-4482-b306-640525ef5f69/tool-results/beava37cx.txt

Preview (first 2KB):
=== amjad-2025-01
# 002013, Amjad et al. 2025

Seven claims reproduced, one partially and five blocked on the dandiset,
plus one claim linking the dandiset to the paper's Zenodo deposit,
reproduced (trial lists agree for 99.8 to 100% of trials); both rounds
agreed with every outcome. The paper describes microinvasive probes for
recording dopamine and electrical activity in monkeys; the beta burst,
reward and unit isolation claims reproduce, the dopamine reward effect
weakly (p = 0.023, and not in the stored trial-aligned `da`).

The dandiset was converted by CatalystNeuro (catalystneuro/schwerdt-lab-to-nwb,
the same conversion as 002014), and many findings are the same: each event
is stored about five times, once per overlapping trial window; trial
conditions are not in the trials table; the FSCV table columns carry no
units and the raw FSCV current is labelled amperes with values in the
[... 18 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/d3530b31-899f-4482-b306-640525ef5f69/tool-results/beava37cx.txt"
}
```

```
1	=== amjad-2025-01
2	# 002013, Amjad et al. 2025
3	
4	Seven claims reproduced, one partially and five blocked on the dandiset,
5	plus one claim linking the dandiset to the paper's Zenodo deposit,
6	reproduced (trial lists agree for 99.8 to 100% of trials); both rounds
7	agreed with every outcome. The paper describes microinvasive probes for
8	recording dopamine and electrical activity in monkeys; the beta burst,
9	reward and unit isolation claims reproduce, the dopamine reward effect
10	weakly (p = 0.023, and not in the stored trial-aligned `da`).
11	
12	The dandiset was converted by CatalystNeuro (catalystneuro/schwerdt-lab-to-nwb,
13	the same conversion as 002014), and many findings are the same: each event
14	is stored about five times, once per overlapping trial window; trial
15	conditions are not in the trials table; the FSCV table columns carry no
16	units and the raw FSCV current is labelled amperes with values in the
17	thousands; the bipolar LFP is stored in volts with a conversion factor that
18	makes it picovolts; and the raw ephys of one session and the spike times of
19	Monkey P are on different clocks from the rest of the file, by 9831.35 s and
20	6800.666 s, with nothing saying so. In addition, one session's trial-aligned
[... 524 more lines not kept]
```

**Agent**

I've read the record, the claims and five recent notes. Next come the reports and the dataset's target entry.

**Agent calls Bash**

```bash
cd transcripts/temmar-2025; for f in author-report answer-report author-answers-report verifier-1-report author-revise-1-report verifier-2-report author-revise-2-report verifier-3-report author-revise-3-report; do echo "=== $f"; cat $f.md; done; cd ../..; grep -n -B3 -A25 '"001201"' targets/dandisets.json | head -60
```

```
<persisted-output>
Output too large (41.2KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/d3530b31-899f-4482-b306-640525ef5f69/tool-results/blsd6oigu.txt

Preview (first 2KB):
=== author-report
I've done steps 1 to 6 of the Author section. `entry.py all` passed on all three notebooks (10, 33 and 27 min), `check` reports 0 errors, and the handover is built in `executed/temmar-2025/handover/`. The entry is in `entries/temmar-2025/` and the record in `attempts/temmar-2025-01.yaml`. Of the 24 claims, 16 are reproduced, 5 partially reproduced, 2 not reproduced and 1 blocked.

### 1. Outcome per claim

| Claim | Outcome | Measured |
|---|---|---|
| dataset-sessions | reproduced | 312 sessions, 303 days, 1242-day span, 9 two-session days, 375 trials each |
| dataset-contents | partially reproduced | 81 of 312 files have no `imp` column |
| figs2-throughput-improves | reproduced | positive slope under all 3 readings |
| fig2a-sbp-decline | reproduced | −0.0338 µV/month |
| fig2a-irregular-shifts | partially reproduced | the shift rule flags almost every day; LSTM R2 in the window is just above its 90th percentile |
| fig2b-active-channels-decrease | reproduced | −6.5 channels/year |
| fig2c-pr-decline | reproduced | −0.0708 PR/month |
| fig2c-ten-dimensions | reproduced | PR at most 10 on 84.8% of days |
| figs4-bank-slopes | reproduced | all four slopes equal the paper's to the printed digits |
[... 12 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/d3530b31-899f-4482-b306-640525ef5f69/tool-results/blsd6oigu.txt"
}
```

```
1	=== author-report
2	I've done steps 1 to 6 of the Author section. `entry.py all` passed on all three notebooks (10, 33 and 27 min), `check` reports 0 errors, and the handover is built in `executed/temmar-2025/handover/`. The entry is in `entries/temmar-2025/` and the record in `attempts/temmar-2025-01.yaml`. Of the 24 claims, 16 are reproduced, 5 partially reproduced, 2 not reproduced and 1 blocked.
3	
4	### 1. Outcome per claim
5	
6	| Claim | Outcome | Measured |
7	|---|---|---|
8	| dataset-sessions | reproduced | 312 sessions, 303 days, 1242-day span, 9 two-session days, 375 trials each |
9	| dataset-contents | partially reproduced | 81 of 312 files have no `imp` column |
10	| figs2-throughput-improves | reproduced | positive slope under all 3 readings |
11	| fig2a-sbp-decline | reproduced | −0.0338 µV/month |
12	| fig2a-irregular-shifts | partially reproduced | the shift rule flags almost every day; LSTM R2 in the window is just above its 90th percentile |
13	| fig2b-active-channels-decrease | reproduced | −6.5 channels/year |
14	| fig2c-pr-decline | reproduced | −0.0708 PR/month |
15	| fig2c-ten-dimensions | reproduced | PR at most 10 on 84.8% of days |
16	| figs4-bank-slopes | reproduced | all four slopes equal the paper's to the printed digits |
17	| figs5-active-inactive-slopes | partially reproduced | inactive slope −0.54e-3, where the paper prints +0.54e-3 |
18	| fig2d-population-drift | partially reproduced | 3 quarters with an outlying spread, where the rule allows 2 |
19	| fig2e-trajectories-separable | reproduced | 0.21 and 0.22 accuracy against 1/8 chance |
20	| fig3b-two-channels | reproduced | |
[... 319 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 5073,5100p targets/dandisets.json
```

```
"relation": "IsDocumentedBy",
     "resource_type": "JournalArticle",
     "preprint": false
    }
   ],
   "catalystneuro": []
  },
  {
   "dandiset": "001203",
   "name": "Data supporting \"Amygdalostriatal transition zone neurons encode sustained cue responses to guide defensive behaviors\" (Mills, et al, 2026)",
   "published_version": "0.261103.1719",
   "asset_count": 706,
   "size_gb": 1802.07,
   "data_standards": [
    "Neurodata Without Borders (NWB)"
   ],
   "species": [
    "Mus musculus - House mouse"
   ],
   "approaches": [
[... 8 more lines not kept]
```

**Agent**

The target entry has an empty `catalystneuro` field, so the opening sentence about conversion does not apply. Writing both files now.

**Agent calls Write**

```json
{
 "file_path": "docs/pilot-notes/temmar-2025-01.md",
 "content": "# temmar-2025, Temmar et al. 2025\n\n17 claims reproduced, three partially, three not reproduced and one blocked.\nThe first verification round agreed with 23 of the 24 outcomes as they stood,\nthe second with all 24, and a third round was held for the one change proposed\nafter the second, which it accepted. It pins version 0.261026.1912, the latest\npublished; the paper cites none, and all three published versions list the same\nasset ids. The paper, Temmar et al., \"Long-term Intracortical Neural activity\nand Kinematics (LINK)\" in the NeurIPS 2025 Datasets and Benchmarks track,\npresents 312 sessions on 303 days of spiking-band power (SBP) and threshold\ncrossings from 96 channels of two Utah arrays in one rhesus macaque, Monkey N,\ndoing a two finger group task, and describes how the signals, the channels'\ntuning and the decoding accuracy of ridge regression (RR) and an LSTM change\nover the dataset. The claims were written from the version of record with its\nsupplement and from the paper's code (chesteklab/LINK_dataset at 5e1c36a). Every\nclaim was tested except `fig5b-finetune`, blocked as `too_large`: the\ncontinual fine-tuning needs 2,446,600 training iterations, about 18 hours at\nround 2's fit times. The LSTM claims were run on 20 of the 312 sessions (every\n16th), with 12 more for `fig4a-lstm-beats-rr`, and the multi-day training on 12\nof the 283 day-0 sessions, for time. Reproduced are, among others,\n`fig2a-sbp-decline` (-0.0338 per month), `fig2c-pr-decline` (-0.0708 per month),\n`figs4-bank-slopes` (all four slopes equal to the printed digits) and\n`fig4a-lstm-beats-rr` (32 of 32 sessions); `fig4d-cross-day-decay` holds under\none of four reading pairs, by margins of 0.017 and 0.003. Partial are\n`dataset-contents` (81 files without an impedance column),\n`fig2d-population-drift` (three quarters with an outlying spread where the rule\nallows two, 2023Q2 at 25.5% from the median) and `suppc1-shuffle-baseline`\n(LSTM -0.154 inside the tolerance, RR -0.223 outside it). Not reproduced are\n`figs5-active-inactive-slopes` (an inactive slope of -5.36e-04 where the\nsupplement prints 0.54e-3), `fig3e-array-tuning` (medial channels tuned to\nextension of both fingers and lateral ones to flexion, the reverse of Section\n4.2, though the verifier reports that Figures 3C and 3E show the files'\npattern) and `fig5a-long-term-decay`, whose double-exponential fits from the\ncriterion's initial values are degenerate on 12 day-0 sessions, while fits\nstarted from the values printed in the Figure 5A panel meet all three\nconditions on point estimates whose initial-rate intervals include zero. The\nauthor's first run gave 16 reproduced, five partially, two not reproduced and\none blocked, and asked a reader nothing, so the answer and author-answers runs\nchanged nothing. Round 1 disagreed only on figs5, which moved from partially\nreproduced to not reproduced; in reply Figure 5A was also scored with\nnormalisation refit on each test session, fits from the panel's values were\nadded, the LSTM was trained on the 12 sessions with the highest RR R2, channel\n47 was printed from the electrodes table, and five questions went to a reader\nin `questions/temmar-2025.yaml`. Round 2 agreed with all 24 and found the LSTM\nfit times wrong throughout (this run printed 207 to 223 s per fit), corrected\nto 77 to 223 s, and the fine-tuning cost understated; in reply `window.ipynb`\nfitted 24 of the 42 other window sessions, which moved `fig2a-irregular-shifts`\nfrom partially reproduced to reproduced in round 3 (window median 0.641 inside\n0.529 to 0.651), and a sixth question, on the shift rule, went to a reader. In\nthe round-1 revision the full run hit the 2-hour command limit and the\nfine-tuning notebook ran 52 minutes without finishing, so it was removed; runs\nstarted in the background were killed when their call returned, and the later\nrevisions ran the notebooks in two foreground stages. The author's run took\nabout 2 h 50 min; the notebooks ran in 10, 33 and 27 min at first and in 8, 34,\n24 and 29 min at the end.\n\nThe files give the subject's date of birth but not the implant date, so the\npaper's days 349 to 1591 after implant cannot be recovered from the dataset.\nThresholdCrossings is stored with unit volts and conversion 1.0 but holds\ninteger counts per 20 ms bin, while the stored SBP is already in microvolts\n(the code's converter divides it by 0.25 and its analysis multiplies by 0.25).\nIn 81 of 312 files the electrodes table has no imp column at all, which\nAppendix A.2's rule for sessions without a measurement within three weeks may\nexplain, but a column that comes and goes breaks code that reads every file the\nsame way. Velocity at bin t is position at t+1 minus position at t, a forward\ndifference that neither the files nor the paper state. 29 sessions have 72\npauses of 1.05 to 472.9 s that the files do not mark, and 998 trials are no\nlonger than the 750 ms hold. With the files' array labels, which agree with\nFigure S1 (channel 47 medial, row 5, column 5), the lateral bank has the lowest\nSBP and the shallowest slope as Figure S4 says, but the tuning by array is the\nreverse of Section 4.2, so the paper's two statements cannot both hold on these\ndata. The supplement prints the inactive channels' slope as 0.54e-3 while\nSection 4.1 says all categories decreased; the data give -0.536e-3. The code's\ntrain_model passes the LSTM's noise arguments in swapped order, adding a bias\nof SD 0.1 and white noise of SD 0.2, the reverse of Appendix C.1; the paper was\nfollowed. The claims file's \"February 2024\" comes from Appendix B.1's\ncandidate days, while the data end on 2023-06-22. Six questions are put to a\nreader: the sign of the inactive slope, Figure 3E against Section 4.2, the\nimpedance rule, the end date, the criterion's initial values for the\ndouble-exponential fit, and whether the shift rule should be compared with a\nbaseline rate.\n\nThe author's points on the protocol: `tools/entry.py check` requires an\n`about` field on `other` findings that the attempt schema rejects, and the two\nfindings were re-filed as `metadata_insufficient` and `paper_inconsistency`;\nconclusion cells must quote the full run's numbers and editing them changes the\nentry hash, so every notebook ran in full twice; \"develop on a subset\" says to\nblock as `too_large` while the protocol also accepts a subset as a deviation,\nand the LSTM claims were run on pre-chosen subsets with only fig5b blocked;\nchanging `runtime_minutes` in `entry.yaml` after the run invalidates its reuse\nstamp; and with no PDF renderer the supplement's Figure S1 could not be opened.\n"
}
```

```
File created successfully at: docs/pilot-notes/temmar-2025-01.md (file state is current in your context — no need to Read it back)
```

**Agent calls Write**

```json
{
 "file_path": "summaries/temmar-2025-01.md",
 "content": "Most of the paper's main findings held up in this data: signal power, active channel count and dimensionality decline over the years, most channels keep their tuning, same-day decoding stays stable with the LSTM ahead of ridge regression, cross-day accuracy drops sharply then levels off, and multi-day training softens the early drop. The drift of the population state held up only in part. The text's account of tuning by array came out reversed with the files' array labels, though it matches the paper's own figure panels. The fits of long-term decoder decay failed, likely because only 12 of 283 starting sessions could be run, and daily fine-tuning was too costly to test. One supplementary slope came out with the sign opposite to the printed one.\n"
}
```

```
File created successfully at: summaries/temmar-2025-01.md (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd  wc -w summaries/temmar-2025-01.md docs/pilot-notes/temmar-2025-01.md; grep -n -i -E 'rather|—|\*\*' summaries/temmar-2025-01.md docs/pilot-notes/temmar-2025-01.md; git status --short
```

```
125 summaries/temmar-2025-01.md
1070 docs/pilot-notes/temmar-2025-01.md
1195 total
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
?? docs/pilot-notes/temmar-2025-01.md
?? scripts
?? summaries/temmar-2025-01.md
```

**Agent**

The summary is over 120 words; tightening it.

**Agent calls Write**

```json
{
 "file_path": "summaries/temmar-2025-01.md",
 "content": "Most of the paper's main findings held up in this data: signal power, active channel count and dimensionality decline over the years, most channels keep their tuning, same-day decoding stays stable with the LSTM ahead of ridge regression, cross-day accuracy drops sharply then levels off, and multi-day training softens the early drop. Population drift held up only in part. The text's tuning by array came out reversed with the files' array labels, though it matches the paper's own figure panels. The long-term decay fits failed, likely because only 12 of 283 starting sessions could be run, and daily fine-tuning was too costly to test. One supplementary slope came out with the opposite sign.\n"
}
```

```
The file summaries/temmar-2025-01.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd  wc -w summaries/temmar-2025-01.md
```

```
113 summaries/temmar-2025-01.md
```

**Agent**

I've written the notes in `docs/pilot-notes/temmar-2025-01.md` and the summary in `summaries/temmar-2025-01.md`; no other file changed and nothing is committed. The dataset's `catalystneuro` field is empty, so the notes do not open the second paragraph with the CatalystNeuro sentence. The summary is 113 words.

# temmar-2025, Temmar et al. 2025

17 claims reproduced, three partially, three not reproduced and one blocked. The first verification round agreed with 23 of the 24 outcomes as they stood, the second with all 24, and a third round was held for the one change proposed after the second, which it accepted. It pins version 0.261026.1912, the latest published; the paper cites none, and all three published versions list the same asset ids. The paper, Temmar et al., "Long-term Intracortical Neural activity and Kinematics (LINK)" in the NeurIPS 2025 Datasets and Benchmarks track, presents 312 sessions on 303 days of spiking-band power (SBP) and threshold crossings from 96 channels of two Utah arrays in one rhesus macaque, Monkey N, doing a two finger group task, and describes how the signals, the channels' tuning and the decoding accuracy of ridge regression (RR) and an LSTM change over the dataset. The claims were written from the version of record with its supplement and from the paper's code (chesteklab/LINK_dataset at 5e1c36a). Every claim was tested except `fig5b-finetune`, blocked as `too_large`: the continual fine-tuning needs 2,446,600 training iterations, about 18 hours at round 2's fit times. The LSTM claims were run on 20 of the 312 sessions (every 16th), with 12 more for `fig4a-lstm-beats-rr`, and the multi-day training on 12 of the 283 day-0 sessions, for time. Reproduced are, among others, `fig2a-sbp-decline` (-0.0338 per month), `fig2c-pr-decline` (-0.0708 per month), `figs4-bank-slopes` (all four slopes equal to the printed digits) and `fig4a-lstm-beats-rr` (32 of 32 sessions); `fig4d-cross-day-decay` holds under one of four reading pairs, by margins of 0.017 and 0.003. Partial are `dataset-contents` (81 files without an impedance column), `fig2d-population-drift` (three quarters with an outlying spread where the rule allows two, 2023Q2 at 25.5% from the median) and `suppc1-shuffle-baseline` (LSTM -0.154 inside the tolerance, RR -0.223 outside it). Not reproduced are `figs5-active-inactive-slopes` (an inactive slope of -5.36e-04 where the supplement prints 0.54e-3), `fig3e-array-tuning` (medial channels tuned to extension of both fingers and lateral ones to flexion, the reverse of Section 4.2, though the verifier reports that Figures 3C and 3E show the files' pattern) and `fig5a-long-term-decay`, whose double-exponential fits from the criterion's initial values are degenerate on 12 day-0 sessions, while fits started from the values printed in the Figure 5A panel meet all three conditions on point estimates whose initial-rate intervals include zero. The author's first run gave 16 reproduced, five partially, two not reproduced and one blocked, and asked a reader nothing, so the answer and author-answers runs changed nothing. Round 1 disagreed only on figs5, which moved from partially reproduced to not reproduced; in reply Figure 5A was also scored with normalisation refit on each test session, fits from the panel's values were added, the LSTM was trained on the 12 sessions with the highest RR R2, channel 47 was printed from the electrodes table, and five questions went to a reader in `questions/temmar-2025.yaml`. Round 2 agreed with all 24 and found the LSTM fit times wrong throughout (this run printed 207 to 223 s per fit), corrected to 77 to 223 s, and the fine-tuning cost understated; in reply `window.ipynb` fitted 24 of the 42 other window sessions, which moved `fig2a-irregular-shifts` from partially reproduced to reproduced in round 3 (window median 0.641 inside 0.529 to 0.651), and a sixth question, on the shift rule, went to a reader. In the round-1 revision the full run hit the 2-hour command limit and the fine-tuning notebook ran 52 minutes without finishing, so it was removed; runs started in the background were killed when their call returned, and the later revisions ran the notebooks in two foreground stages. The author's run took about 2 h 50 min; the notebooks ran in 10, 33 and 27 min at first and in 8, 34, 24 and 29 min at the end.

The files give the subject's date of birth but not the implant date, so the paper's days 349 to 1591 after implant cannot be recovered from the dataset. ThresholdCrossings is stored with unit volts and conversion 1.0 but holds integer counts per 20 ms bin, while the stored SBP is already in microvolts (the code's converter divides it by 0.25 and its analysis multiplies by 0.25). In 81 of 312 files the electrodes table has no imp column at all, which Appendix A.2's rule for sessions without a measurement within three weeks may explain, but a column that comes and goes breaks code that reads every file the same way. Velocity at bin t is position at t+1 minus position at t, a forward difference that neither the files nor the paper state. 29 sessions have 72 pauses of 1.05 to 472.9 s that the files do not mark, and 998 trials are no longer than the 750 ms hold. With the files' array labels, which agree with Figure S1 (channel 47 medial, row 5, column 5), the lateral bank has the lowest SBP and the shallowest slope as Figure S4 says, but the tuning by array is the reverse of Section 4.2, so the paper's two statements cannot both hold on these data. The supplement prints the inactive channels' slope as 0.54e-3 while Section 4.1 says all categories decreased; the data give -0.536e-3. The code's train_model passes the LSTM's noise arguments in swapped order, adding a bias of SD 0.1 and white noise of SD 0.2, the reverse of Appendix C.1; the paper was followed. The claims file's "February 2024" comes from Appendix B.1's candidate days, while the data end on 2023-06-22. Six questions are put to a reader: the sign of the inactive slope, Figure 3E against Section 4.2, the impedance rule, the end date, the criterion's initial values for the double-exponential fit, and whether the shift rule should be compared with a baseline rate.

The author's points on the protocol: `tools/entry.py check` requires an `about` field on `other` findings that the attempt schema rejects, and the two findings were re-filed as `metadata_insufficient` and `paper_inconsistency`; conclusion cells must quote the full run's numbers and editing them changes the entry hash, so every notebook ran in full twice; "develop on a subset" says to block as `too_large` while the protocol also accepts a subset as a deviation, and the LSTM claims were run on pre-chosen subsets with only fig5b blocked; changing `runtime_minutes` in `entry.yaml` after the run invalidates its reuse stamp; and with no PDF renderer the supplement's Figure S1 could not be opened.

---

Most of the paper's main findings held up in this data: signal power, active channel count and dimensionality decline over the years, most channels keep their tuning, same-day decoding stays stable with the LSTM ahead of ridge regression, cross-day accuracy drops sharply then levels off, and multi-day training softens the early drop. Population drift held up only in part. The text's tuning by array came out reversed with the files' array labels, though it matches the paper's own figure panels. The long-term decay fits failed, likely because only 12 of 283 starting sessions could be run, and daily fine-tuning was too costly to test. One supplementary slope came out with the opposite sign.

## End of run

14 turns, 2 minutes, $1.10 at API prices, result: success.
