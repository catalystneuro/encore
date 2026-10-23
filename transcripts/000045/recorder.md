# 000045 · recorder · run 39876409392

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  git log --diff-filter=A --name-only --format= -- docs/pilot-notes | head -n 5; ls attempts/000045* claims/000045/ transcripts/000045/; python tools/readme_row.py 000045; python -c "
import json;d=json.load(open('targets/dandisets.json'))
items=d if isinstance(d,list) else d.get('dandisets',d)
import sys
for x in (items if isinstance(items,list) else items.values()):
  if '000045' in json.dumps(x)[:200]: print(json.dumps(x,indent=1))
"
```

```
docs/pilot-notes/001828-mantas-2024-01.md
docs/pilot-notes/000037-gillon-2023-01.md
docs/pilot-notes/000036-mayner-2022-01.md
docs/pilot-notes/000003-senzai-2017-01.md
docs/pilot-notes/000004-chandravadia-2020-01.md
attempts/000045-ibl-2021-01.yaml

claims/000045/:
10.7554-elife.63711.yaml

transcripts/000045/:
answer-report.md
answer.md
author-answers-report.md
author-answers.md
author-report.md
author-revise-1-report.md
author-revise-1.md
author-revise-2-report.md
author-revise-2.md
[... 10 more lines not kept]
```

**Agent calls Bash**

```bash
cd  for f in docs/pilot-notes/001828-mantas-2024-01.md docs/pilot-notes/000037-gillon-2023-01.md docs/pilot-notes/000036-mayner-2022-01.md docs/pilot-notes/000003-senzai-2017-01.md docs/pilot-notes/000004-chandravadia-2020-01.md docs/pilot-notes/001754-knierim-2000-02.md; do echo "=== $f"; cat $f; done; grep -n -B2 -A12 '"000045"' targets/dandisets.json | head -40; grep -n "Claims\|^|" README.md | head -5
```

```
<persisted-output>
Output too large (31.9KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/6fe147b6-3455-4bd7-9998-0fd65cba2af6/tool-results/bi7ezk2eg.txt

Preview (first 2KB):
=== docs/pilot-notes/001828-mantas-2024-01.md
# 001828, Mantas et al. 2024

Four claims reproduced, two partially, four not reproduced and 27 blocked on
the dandiset, with one more, on the RNA-seq counts at GEO, also blocked. It
pins version 0.261020.1002, the only published version; the paper cites none.
The paper, the bioRxiv preprint "Anxa1+ dopamine neuron vulnerability defines
prodromal Parkinson's disease bradykinesia and procedural motor learning
impairment", reports that Anxa1+ dopamine neurons of the ventral SNc are lost
early in mouse Parkinson's disease models, that their axons in dorsal CP
carry speed-related signals, and that silencing them with TeTx slows
locomotion and impairs procedural motor learning in an arrow maze and a
forelimb reaching task. The claims were written from the preprint's text
without its figures or supplement, and the paper's code, listed in a Zenodo
record whose DOI returned 404, was not read. The evoked release in dCP and
cCP, the water drop photometry of Figure 3, the speed correlations of Figure
[... 14 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/6fe147b6-3455-4bd7-9998-0fd65cba2af6/tool-results/bi7ezk2eg.txt"
}
```

```
1	=== docs/pilot-notes/001828-mantas-2024-01.md
2	# 001828, Mantas et al. 2024
3	
4	Four claims reproduced, two partially, four not reproduced and 27 blocked on
5	the dandiset, with one more, on the RNA-seq counts at GEO, also blocked. It
6	pins version 0.261020.1002, the only published version; the paper cites none.
7	The paper, the bioRxiv preprint "Anxa1+ dopamine neuron vulnerability defines
8	prodromal Parkinson's disease bradykinesia and procedural motor learning
9	impairment", reports that Anxa1+ dopamine neurons of the ventral SNc are lost
10	early in mouse Parkinson's disease models, that their axons in dorsal CP
11	carry speed-related signals, and that silencing them with TeTx slows
12	locomotion and impairs procedural motor learning in an arrow maze and a
13	forelimb reaching task. The claims were written from the preprint's text
14	without its figures or supplement, and the paper's code, listed in a Zenodo
15	record whose DOI returned 404, was not read. The evoked release in dCP and
16	cCP, the water drop photometry of Figure 3, the speed correlations of Figure
17	4B, the open field locomotion of the TeTx and early model mice, the arrow
18	maze speed and reaching accuracy were tested. Twelve histology and qPCR
19	claims and three nosepoke claims are blocked as `data_missing`, as the
20	dandiset holds behaviour and fiber photometry only, as are the two Figure 6D
[... 464 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 676,700p targets/dandisets.json; head -3 README.md; grep -n "^| Dandiset\|^| ---" README.md | head; cat attempts/000045-ibl-2021-01.yaml
```

```
<persisted-output>
Output too large (63KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/6fe147b6-3455-4bd7-9998-0fd65cba2af6/tool-results/bvkxzd9uw.txt

Preview (first 2KB):
    "behavioral approach",
    "electrophysiological approach"
   ],
   "papers": [
    {
     "doi": "10.7554/elife.63711",
     "title": null,
     "relation": "IsDescribedBy",
     "resource_type": null,
     "preprint": false
    }
   ],
   "catalystneuro": []
  },
  {
   "dandiset": "000053",
[... 45 more lines not kept]
```

**Agent calls Bash**

```bash
cd  wc -c attempts/000045-ibl-2021-01.yaml claims/000045/*.yaml transcripts/000045/*-report.md; grep -n "^| Dandiset" README.md
```

```
63531 attempts/000045-ibl-2021-01.yaml
 66553 claims/000045/10.7554-elife.63711.yaml
  2655 transcripts/000045/answer-report.md
  6149 transcripts/000045/author-answers-report.md
  6260 transcripts/000045/author-report.md
  3592 transcripts/000045/author-revise-1-report.md
  2350 transcripts/000045/author-revise-2-report.md
  3115 transcripts/000045/claims-check-report.md
  3988 transcripts/000045/claims-report.md
 11631 transcripts/000045/verifier-1-report.md
  6281 transcripts/000045/verifier-2-report.md
176105 total
```

**Agent calls Read**

```json
{
 "file_path": "attempts/000045-ibl-2021-01.yaml"
}
```

```
1	schema_version: 2
2	id: 000045-ibl-2021-01
3	dataset:
4	  archive: dandi
5	  id: "000045"
6	  version: 0.211209.1413
7	  doi: 10.48324/dandi.000045/0.211209.1413
8	paper: doi:10.7554/elife.63711
9	date: 2026-10-22
10	entry: 000045-ibl-2021
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
[... 859 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "attempts/000045-ibl-2021-01.yaml",
 "offset": 879
}
```

```
879	  - claim: fig2-abs-bias-threshold-during-training
880	    agrees: true
881	    outcome: reproduced
882	    reason: "Agrees; the outcome matches round 1 and the re-executed outputs support it."
883	    response: "No change of outcome."
884	  - claim: fig2s2-variability-decreases
885	    agrees: true
886	    outcome: partially_reproduced
887	    reason: "Agrees. Cell 34 and the record say the two means are within tolerance under most readings; cell
888	      33 shows both means within tolerance under every reading, all 20 rows, so the sentence understates the
889	      result."
890	    response: "No change of outcome. The conclusion and the record now say the means are within tolerance
891	      under every reading (cell 33, all 20 rows)."
892	  - claim: early-sessions-predict-slow-learners
893	    agrees: true
894	    outcome: blocked
895	    reason: "Agrees; the outcome matches round 1 and the re-executed outputs support it."
896	    response: "No change of outcome."
897	  - claim: fig3c-easy-errors-basic
898	    agrees: true
[... 176 more lines not kept]
```

**Agent calls Bash**

```bash
cd transcripts/000045; for f in author-report.md verifier-1-report.md author-revise-1-report.md verifier-2-report.md author-revise-2-report.md claims-report.md claims-check-report.md answer-report.md author-answers-report.md; do echo "=== $f"; cat $f; done; ls -la --time-style=full-iso
```

```
<persisted-output>
Output too large (46.9KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/6fe147b6-3455-4bd7-9998-0fd65cba2af6/tool-results/bwi1166lb.txt

Preview (first 2KB):
=== author-report.md
I finished steps 1 to 5 of the Author section and built the handover (step 6). The entry passes `tools/entry.py all` and runs in 18.3 minutes. Nothing is committed. I did not verify my own work.

I pinned version 0.211209.1413. The paper cites no version of the dandiset, and the two published versions (.1412 and .1413, made a minute apart) hold the same files.

**1. Outcome per claim** (38 findings, plus one link claim I added)

| Claim | Outcome |
|---|---|
| cohort-counts | not reproduced |
| fig2g-days-to-proficiency | partially reproduced |
| fig2g-days-differ-across-labs | not reproduced |
| fig2s1-trials-to-proficiency | partially reproduced |
| fig2h-proportion-learned-40-days | blocked: methods_underspecified |
| fig2bc-threshold-bias-iqr | partially reproduced |
| fig2-abs-bias-threshold-during-training | reproduced |
[... 21 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/6fe147b6-3455-4bd7-9998-0fd65cba2af6/tool-results/bwi1166lb.txt"
}
```

```
1	=== author-report.md
2	I finished steps 1 to 5 of the Author section and built the handover (step 6). The entry passes `tools/entry.py all` and runs in 18.3 minutes. Nothing is committed. I did not verify my own work.
3	
4	I pinned version 0.211209.1413. The paper cites no version of the dandiset, and the two published versions (.1412 and .1413, made a minute apart) hold the same files.
5	
6	**1. Outcome per claim** (38 findings, plus one link claim I added)
7	
8	| Claim | Outcome |
9	|---|---|
10	| cohort-counts | not reproduced |
11	| fig2g-days-to-proficiency | partially reproduced |
12	| fig2g-days-differ-across-labs | not reproduced |
13	| fig2s1-trials-to-proficiency | partially reproduced |
14	| fig2h-proportion-learned-40-days | blocked: methods_underspecified |
15	| fig2bc-threshold-bias-iqr | partially reproduced |
16	| fig2-abs-bias-threshold-during-training | reproduced |
17	| fig2s2-variability-decreases | partially reproduced |
18	| early-sessions-predict-slow-learners | blocked: methods_underspecified |
19	| fig3c-easy-errors-basic | reproduced |
20	| fig3de-threshold-bias-basic | reproduced |
[... 386 more lines not kept]
```

**Agent calls Bash**

```bash
cd  head -60 claims/000045/10.7554-elife.63711.yaml; grep -n "^  - id:\|^- id:" claims/000045/10.7554-elife.63711.yaml | head -50
```

```
# Claims for The International Brain Laboratory (2021), "Standardized and reproducible measurement
# of decision-making in mice", eLife 10:e63711, on dandiset 000045 ("IBL behavioral data").
# Written by an agent (model "claude-opus-5-5", Claude Code in GitHub Actions), 2026-10-22, under
# docs/protocol.md version pilot-10.
#
# Text read: the version of record (eLife, PMC8137147, as served by Europe PMC), full text with
# Results, figure legends and figure supplement legends, Materials and methods, Appendix 1 (table 1,
# standardization and proficiency criteria), the decision letter and author response. The only
# supplementary file is eLife's transparent reporting form; it holds no results. The Methods refer
# the psychometric fitting procedure and the full training criteria to "Protocol 2" (IBL Protocol
# for Mice Training, figshare doi:10.6084/m9.figshare.11634729.v3), which is not in paper/ and was
# not read; the code below settles the fitting procedure.
#
# Code read: github.com/int-brain-lab/paper-behavior at commit
# edc453189104a1f76f4b2ab230cd86f2140e3f63 (the commit the paper archives at Software Heritage).
# One script per figure panel; each queries the IBL DataJoint pipeline (or CSV extracts of it) and
# uses paper_behavior_functions.py for the shared selection, trial coding and psychometric fit. The
# psychometric fit itself is brainbox.behavior.pyschofit (ibllib), which the repository imports.
# The code for the Random Forest prediction of slow learners (Results, Training succeeded,
# paragraph 4) and for Figure 5, figure supplement 1c statistics is not in the repository.
[... 79 more lines not kept]
```

**Agent calls Write**

```json
{
 "file_path": "docs/pilot-notes/000045-ibl-2021-01.md",
 "content": "# 000045, International Brain Laboratory et al. 2021\n\nNineteen claims reproduced, thirteen partially, five not reproduced and one\nblocked, all on the dandiset, with the link claim `lab-link`, which the\nauthor added, also reproduced. It pins version 0.211209.1413; the paper cites\nno version, and the two published versions, made a minute apart, hold the\nsame files. The paper, \"Standardized and reproducible measurement of\ndecision-making in mice\" in eLife, trains mice in seven laboratories on a\nbasic and a full visual decision task and reports that learning rates differ\nacross laboratories but that performance, psychometric parameters and the use\nof block priors at proficiency do not, so that a classifier cannot tell the\nlaboratories apart. The cohort counts, days and trials to proficiency, the\nFigure 2 psychometric ranges, the lab tests and classifiers of Figures 3 and\n4, the GLM weights and accuracy of Figure 5, win-stay/lose-switch, updating\nby contrast and the session end criteria were tested. Only\n`early-sessions-predict-slow-learners` is blocked, as\n`methods_underspecified`: the paper gives no code or method for its Random\nForest, and the criterion's readings disagree, 3 of 20 accuracy values within\n0.53 +- 0.053 and the others from 0.143 to 0.667. The author put seven\nquestions to a reader; the answers, mostly from the paper's code and the\nIBL-pipeline code it imports, changed how basic proficiency (P1) is computed\n(each session and the two before it, all trials counted, 1a or 1b at any\ndate) and let the classifiers run with 5 mice per lab, the lowest lab count,\nagainst the code's 8, which moved `fig2h-proportion-learned-40-days`,\n`fig3cde-no-lab-difference-medians`, `fig3f-classifier-chance-basic`,\n`fig3f-positive-control` and `fig4j-classifier-chance-full` from blocked to\nreproduced and `fig3c-easy-errors-basic` from reproduced to partially\nreproduced. Round 1 gave its own outcome for each claim without the\nconclusions and summary and agreed with 33 of 39; the author took its\noutcomes for `fig2g-days-differ-across-labs`, `fig3s2a-trial-duration` and\n`fig3s4-looser-criterion` (from not reproduced to partially reproduced) and\nfor `fig5s2-glm-accuracy` (from blocked to reproduced, dropping the\nnotebook's own rule that readings of an open detail must agree), moved\n`fig3s3-other-classifiers` from blocked as `not_runnable` to reproduced, where\nround 1 gave partially reproduced, by running the Random Forest in 4\nprocesses on the first 50 of the criterion's 2000 subsamples (2.5th\npercentile 0.035, bootstrap 95% interval 0.029 to 0.057, against a shuffled\nmean of 0.100), and kept `fig5dg-history-weights-higher-full` as reproduced\nwhere round 1 gave partially reproduced. Round 2 agreed with all 39, so there\nwas no third round; it found statements the outputs did not support, among\nthem a run of 100 Random Forest subsamples that no output printed, wheel\ntimestamps called not monotonic and a loading time of about six minutes\nagainst 3.4 printed, and these were corrected. Some outcomes rest on weak\nground: `fig3s2a-trial-duration` has a median of 420.45 ms, just outside 468\n+- 46.8; `fig4i-bias-shifts-with-block` is partial because the paper's p <\n1e-16 cannot be reached by a Wilcoxon test with 60 mice (smallest p\n1.6e-11); and `fig5dg-history-weights-higher-full` holds on the code's\nsessions while its unrewarded difference is not significant on the sessions\nof reading (b) (p = 0.10 to 0.39). Streaming the 6,615 files with h5py in\nthreads took 108 minutes, and processes brought it to about 5 minutes; the\nentry ran in 18.3 minutes at first and 1607 s in the last run, beyond the\nprotocol's aim of ten.\n\nThe dandiset holds only part of the paper's data: 178 mice and 6,615\nsessions from 2019-06-11 to 2020-03-23, while the paper's mice began training\nin January 2019 (206 mice, 10,903 sessions), so 41 mice of the project begin\nmid-training in the dandiset, only 136 have their whole training in it, and\n83 reach basic and 60 full task proficiency against 140 and 98. The training\nstatus of each session, on which every analysis of the paper selects\nsessions, is not in the files and had to be recomputed from the trials, which\nleaves open details of the criteria, and the metadata do not say which of the\n178 mice are the paper's; one mouse (SWC_029) belongs to another project by\nits subject record. probabilityLeft is described as the probability of a left\nstimulus for the current block, but in every basic-task session it varies\nfrom trial to trial between 0 and 1 (24% of basic-task trials are not 0.5),\nwith the stimulus side following it. session_start_time is stated in UTC\n(+00:00) but holds local clock times, as all seven labs, from London to\nBerkeley, have median start hours between 11.0 and 14.4 h, so the start times\ncannot confirm the time zones `fig3f-positive-control` takes from the code.\nOther findings: in 807 files the wheel position data and its timestamps\ndiffer in length (for example 181,623 samples against 340,799 timestamps), 16\nfiles have no wheel series, and in one session checked (ibl_witten_07) the\nwheel moves the opposite way to the choice on every trial; 257,021 trials\n(6%) have no stimulus onset time, 185 sessions have none, and 1,541 trials in\n220 sessions have a response time before the stimulus onset (down to -5,638\ns), though no proficiency window fails for the missing onsets alone; one\nrecording is deposited twice, under two mice (CSHL_013 and CSHL_015,\n2019-07-15); one session (ZM_1367, 2019-06-11) uses contrasts of 4% and 8%,\nwhich the paper does not describe; and the Methods give the 1a/1b\nperformance criterion on easy trials and the lapse criterion as a maximum of\n0.2 for the sum of the lapses, while Appendix 1, table 1d gives performance on\n100% contrast and a bound on each lapse rate, which with performance on 100%\ncontrast only gives 84 mice at P1 against 83.\n\nThe author's points on the protocol: it does not say what to do when the\nclaims file's own readings disagree on a claim of absence; it has no rule for\npartial outcomes when only some expected values match; `other` was used for\ntoo few units under the claim's own rule; the clock check had no streams to\ncheck, as the claims use only the trial table, so the wheel was checked\nagainst it; a criterion that cannot be met, p < 1e-16 with 60 mice, was\napplied as written; the schema forbids `inferred` on a link claim, so the\nnote went into its criterion; and the aim of under ten minutes was not met.\n"
}
```

```
File created successfully at: docs/pilot-notes/000045-ibl-2021-01.md (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd  git status --short; grep -nE "—|rather|\*\*" docs/pilot-notes/000045-ibl-2021-01.md
```

```
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
?? docs/pilot-notes/000045-ibl-2021-01.md
?? scripts
```

**Agent**

I've written `docs/pilot-notes/000045-ibl-2021-01.md` and changed no other file. Nothing is committed. `git status` also lists dotfiles and a `scripts` entry at the repository root as untracked. I didn't create them, and the author's reports say the same of theirs, so I left them alone.

For the heading I used "International Brain Laboratory et al. 2021". The paper's first author is the consortium, as the claims file names it. `tools/readme_row.py` prints the shorter "Ibl et al. 2021", so change the heading if you'd rather match that. The counts below don't include the `lab-link` claim, because `readme_row.py` doesn't count it.

# 000045, International Brain Laboratory et al. 2021

Nineteen claims reproduced, thirteen partially, five not reproduced and one
blocked, all on the dandiset, with the link claim `lab-link`, which the
author added, also reproduced. It pins version 0.211209.1413; the paper cites
no version, and the two published versions, made a minute apart, hold the
same files. The paper, "Standardized and reproducible measurement of
decision-making in mice" in eLife, trains mice in seven laboratories on a
basic and a full visual decision task and reports that learning rates differ
across laboratories but that performance, psychometric parameters and the use
of block priors at proficiency do not, so that a classifier cannot tell the
laboratories apart. The cohort counts, days and trials to proficiency, the
Figure 2 psychometric ranges, the lab tests and classifiers of Figures 3 and
4, the GLM weights and accuracy of Figure 5, win-stay/lose-switch, updating
by contrast and the session end criteria were tested. Only
`early-sessions-predict-slow-learners` is blocked, as
`methods_underspecified`: the paper gives no code or method for its Random
Forest, and the criterion's readings disagree, 3 of 20 accuracy values within
0.53 +- 0.053 and the others from 0.143 to 0.667. The author put seven
questions to a reader; the answers, mostly from the paper's code and the
IBL-pipeline code it imports, changed how basic proficiency (P1) is computed
(each session and the two before it, all trials counted, 1a or 1b at any
date) and let the classifiers run with 5 mice per lab, the lowest lab count,
against the code's 8, which moved `fig2h-proportion-learned-40-days`,
`fig3cde-no-lab-difference-medians`, `fig3f-classifier-chance-basic`,
`fig3f-positive-control` and `fig4j-classifier-chance-full` from blocked to
reproduced and `fig3c-easy-errors-basic` from reproduced to partially
reproduced. Round 1 gave its own outcome for each claim without the
conclusions and summary and agreed with 33 of 39; the author took its
outcomes for `fig2g-days-differ-across-labs`, `fig3s2a-trial-duration` and
`fig3s4-looser-criterion` (from not reproduced to partially reproduced) and
for `fig5s2-glm-accuracy` (from blocked to reproduced, dropping the
notebook's own rule that readings of an open detail must agree), moved
`fig3s3-other-classifiers` from blocked as `not_runnable` to reproduced, where
round 1 gave partially reproduced, by running the Random Forest in 4
processes on the first 50 of the criterion's 2000 subsamples (2.5th
percentile 0.035, bootstrap 95% interval 0.029 to 0.057, against a shuffled
mean of 0.100), and kept `fig5dg-history-weights-higher-full` as reproduced
where round 1 gave partially reproduced. Round 2 agreed with all 39, so there
was no third round; it found statements the outputs did not support, among
them a run of 100 Random Forest subsamples that no output printed, wheel
timestamps called not monotonic and a loading time of about six minutes
against 3.4 printed, and these were corrected. Some outcomes rest on weak
ground: `fig3s2a-trial-duration` has a median of 420.45 ms, just outside 468
+- 46.8; `fig4i-bias-shifts-with-block` is partial because the paper's p <
1e-16 cannot be reached by a Wilcoxon test with 60 mice (smallest p
1.6e-11); and `fig5dg-history-weights-higher-full` holds on the code's
sessions while its unrewarded difference is not significant on the sessions
of reading (b) (p = 0.10 to 0.39). Streaming the 6,615 files with h5py in
threads took 108 minutes, and processes brought it to about 5 minutes; the
entry ran in 18.3 minutes at first and 1607 s in the last run, beyond the
protocol's aim of ten.

The dandiset holds only part of the paper's data: 178 mice and 6,615
sessions from 2019-06-11 to 2020-03-23, while the paper's mice began training
in January 2019 (206 mice, 10,903 sessions), so 41 mice of the project begin
mid-training in the dandiset, only 136 have their whole training in it, and
83 reach basic and 60 full task proficiency against 140 and 98. The training
status of each session, on which every analysis of the paper selects
sessions, is not in the files and had to be recomputed from the trials, which
leaves open details of the criteria, and the metadata do not say which of the
178 mice are the paper's; one mouse (SWC_029) belongs to another project by
its subject record. probabilityLeft is described as the probability of a left
stimulus for the current block, but in every basic-task session it varies
from trial to trial between 0 and 1 (24% of basic-task trials are not 0.5),
with the stimulus side following it. session_start_time is stated in UTC
(+00:00) but holds local clock times, as all seven labs, from London to
Berkeley, have median start hours between 11.0 and 14.4 h, so the start times
cannot confirm the time zones `fig3f-positive-control` takes from the code.
Other findings: in 807 files the wheel position data and its timestamps
differ in length (for example 181,623 samples against 340,799 timestamps), 16
files have no wheel series, and in one session checked (ibl_witten_07) the
wheel moves the opposite way to the choice on every trial; 257,021 trials
(6%) have no stimulus onset time, 185 sessions have none, and 1,541 trials in
220 sessions have a response time before the stimulus onset (down to -5,638
s), though no proficiency window fails for the missing onsets alone; one
recording is deposited twice, under two mice (CSHL_013 and CSHL_015,
2019-07-15); one session (ZM_1367, 2019-06-11) uses contrasts of 4% and 8%,
which the paper does not describe; and the Methods give the 1a/1b
performance criterion on easy trials and the lapse criterion as a maximum of
0.2 for the sum of the lapses, while Appendix 1, table 1d gives performance on
100% contrast and a bound on each lapse rate, which with performance on 100%
contrast only gives 84 mice at P1 against 83.

The author's points on the protocol: it does not say what to do when the
claims file's own readings disagree on a claim of absence; it has no rule for
partial outcomes when only some expected values match; `other` was used for
too few units under the claim's own rule; the clock check had no streams to
check, as the claims use only the trial table, so the wheel was checked
against it; a criterion that cannot be met, p < 1e-16 with 60 mice, was
applied as written; the schema forbids `inferred` on a link claim, so the
note went into its criterion; and the aim of under ten minutes was not met.

## End of run

13 turns, 2 minutes, result: success.
