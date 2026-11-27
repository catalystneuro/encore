# wirth-2017 · recorder · run 43495124283

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  git log --diff-filter=A --name-only --format= -- docs/pilot-notes | head -n 5; ls transcripts/wirth-2017/; python tools/readme_row.py wirth-2017; ls summaries | head
```

```
docs/pilot-notes/amjad-2025-01.md
docs/pilot-notes/armstrong-2026-01.md
docs/pilot-notes/ashworth-2025-01.md
docs/pilot-notes/athalye-2023-01.md
docs/pilot-notes/azcorra-2023-01.md
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
author-revise-3.md
author.md
claims-check-report.md
claims-check.md
claims-report.md
[... 18 more lines not kept]
```

**Agent calls Bash**

```bash
cd  for f in docs/pilot-notes/{amjad-2025-01,armstrong-2026-01,ashworth-2025-01,athalye-2023-01,azcorra-2023-01}.md; do echo "=== $f"; cat $f; done; head -30 docs/pilot-notes/knierim-2000-02.md; cat summaries/amjad-2025-01.md summaries/README.md; grep -n "| Dataset\|^| ---" README.md | head
```

```
<persisted-output>
Output too large (38.9KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/95ce7b85-9203-4046-ba5e-7129f11ecbda/tool-results/b5xawrxsq.txt

Preview (first 2KB):
=== docs/pilot-notes/amjad-2025-01.md
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
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/95ce7b85-9203-4046-ba5e-7129f11ecbda/tool-results/b5xawrxsq.txt"
}
```

```
1	=== docs/pilot-notes/amjad-2025-01.md
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
[... 527 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat attempts/wirth-2017-01.yaml; cat claims/wirth-2017.yaml; python -c "
import json;d=json.load(open('targets/dandisets.json'))
import sys
items = d if isinstance(d,list) else d.get('dandisets', d)
for x in (items if isinstance(items,list) else items.values()):
    if 'wirth' in json.dumps(x).lower() or 'hc-21' in json.dumps(x).lower(): print(json.dumps(x,indent=1))
"
```

```
<persisted-output>
Output too large (104.7KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/95ce7b85-9203-4046-ba5e-7129f11ecbda/tool-results/bwpr4ael3.txt

Preview (first 2KB):
schema_version: 3
id: wirth-2017-01
datasets:
- archive: crcns
  id: hc-21
  version: unversioned
  doi: 10.6080/K0GX48R9
  relation: primary
- archive: crcns
  id: hc-12
  version: unversioned
  doi: 10.6080/K0R49NQV
  relation: primary
paper: doi:10.1371/journal.pbio.2001045
date: 2026-11-13
entry: wirth-2017
[... 30 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/95ce7b85-9203-4046-ba5e-7129f11ecbda/tool-results/bwpr4ael3.txt"
}
```

```
1	schema_version: 3
2	id: wirth-2017-01
3	datasets:
4	- archive: crcns
5	  id: hc-21
6	  version: unversioned
7	  doi: 10.6080/K0GX48R9
8	  relation: primary
9	- archive: crcns
10	  id: hc-12
11	  version: unversioned
12	  doi: 10.6080/K0R49NQV
13	  relation: primary
14	paper: doi:10.1371/journal.pbio.2001045
15	date: 2026-11-13
16	entry: wirth-2017
17	provenance:
18	  kind: agent
19	  accountable:
20	    name: CatalystNeuro
[... 909 more lines not kept]
```

**Agent**

Read the attempt record; now the claims file and dataset entry.

**Agent calls Bash**

```bash
cd  grep -nE "^- id:|^  id:|figure|location|  source:|^#" claims/wirth-2017.yaml | head -150; grep -n -B3 -A12 '"hc-21"\|hc-12' targets/dandisets.json | head -60
```

```
1:# Claims for Wirth, Baraduc, Plante, Pinede & Duhamel (2017), PLoS Biology 15(2), e2001045,
2:# tested on CRCNS hc-12 and hc-21.
3:# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"), 2026-11-10,
4:# protocol pilot-14 as stated in docs/protocol.md.
5:#
6:# Text read: the version of record (PMC5328243, open access), full text from Europe PMC JATS
7:# XML as stored under paper/: Results, Discussion, Materials and Methods, the figure legends of
8:# Figs 1 to 7 and the legends of S1 to S7 Figs. The supplementary text files S1 Appendix
9:# (sections A1 to A5: point-of-gaze density maps, gaze before joystick actions, recording
10:# methods and cell selection, population averages, the control for space dimensionality) and
11:# S2 Appendix (description of the CRCNS files and scripts) are DOCX files that are not under
12:# paper/ and were not read. The claims that rest on them say so (gaze-anticipates-action,
13:# gaze-anticipates-landmarks, dimensionality-control, fields-per-cell). No PDF was read; the
14:# reference list is absent from the stored text, so reference 60 (the learning curve method)
15:# is not named.
16:#
17:# Code: the paper links no repository. It says some Matlab scripts are hosted with the data on
18:# CRCNS (Supporting data; S2 Appendix); the hc-12 descriptor lists them (a scripts folder that
19:# plots position, direction and state-space maps, rasters and learning curves). These are files
20:# of the dataset and were not read. No criterion below takes a method from code; the author may
[... 130 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n -i -B2 -A12 'wirth\|hc-21\|hc-12' targets/dandisets.json | head -60; head -c 600 targets/dandisets.json; sed -n 400,470p claims/wirth-2017.yaml; sed -n 495,545p claims/wirth-2017.yaml
```

```
{
 "schema_version": 1,
 "generated": "2026-11-11T14:22:56+00:00",
 "source": "https://api.dandiarchive.org/api",
 "counts": {
  "public_dandisets": 675,
  "with_a_paper": 295,
  "with_a_published_version": 254,
  "papers": 312,
  "converted_by_catalystneuro": 51
 },
 "targets": [
  {
   "dandiset": "000003",
   "name": "Physiological Properties and Behavioral Correlates of Hippocampal Granule Cells and Mossy Cells",
   "published_version": "0.260218.2052",
   "asset_count": 101,
   "size_gb": 1922.23,
   "data_standards": [
    "Neurodata Without Borders (NWB)"
[... 124 more lines not kept]
```

**Agent calls Bash**

```bash
cd transcripts/wirth-2017; wc -w *-report.md; cat author-report.md
```

```
104 answer-report.md
  240 author-answers-report.md
  813 author-report.md
  670 author-revise-1-report.md
  617 author-revise-2-report.md
  289 author-revise-3-report.md
  468 claims-check-report.md
  455 claims-report.md
 1778 verifier-1-report.md
 1443 verifier-2-report.md
  606 verifier-3-report.md
 7483 total
The author run is complete: 28 claims recorded, the entry's checks pass with 0 errors, and the handover is built. The notebook ran from a clean environment in 1,178 s (about 20 minutes), with peak memory around 1 GB.

## 1. Outcomes

| Claim | Outcome |
|---|---|
| gaze-anticipates-action | reproduced (rests on an assumption about the eye signal's sign) |
| gaze-anticipates-landmarks | reproduced (same assumption) |
[... 52 more lines not kept]
```

**Agent calls Bash**

```bash
cd transcripts/wirth-2017; for f in answer-report.md author-answers-report.md author-revise-1-report.md author-revise-2-report.md verifier-3-report.md author-revise-3-report.md; do echo "=== $f"; cat $f; done
```

```
=== answer-report.md
I found no questions to answer, so I changed nothing.

- **No questions file:** `questions/wirth-2017.yaml` doesn't exist on this branch, and git history has never had it on any branch.
- **No questions asked:** the author's report (`transcripts/wirth-2017/author-report.md:48`) says "Questions to a reader: none." The author's open method questions went to the paper's authors as `methods_unavailable` findings in the attempt record, not to a reader.
- **No verifier questions yet:** only the author run has happened (latest commit afe6442), so no verifier has raised any.

I left `claims/wirth-2017.yaml` unchanged and did not create a questions file, so there was nothing to run `tools/claims_check.py` on.
=== author-answers-report.md
No reader answered any questions, so no claims changed, and I left the notebook, conclusions, attempt record and claim notes as they were.

**Questions:** none. `questions/wirth-2017.yaml` does not exist, and git history has no version of it on any branch. My first author run asked a reader nothing. I sent its open method questions to the paper's authors as `methods_unavailable` findings in `attempts/wirth-2017-01.yaml`: how the surrogate chunks were shifted and whether returns were included, which method reference 60 is, how a positional field is defined and how the dimensionality control was done, and which rotational moves and laps were used. The reader's answer run (`transcripts/wirth-2017/answer-report.md`) found the same and left `claims/wirth-2017.yaml` unchanged. It is still identical to the claims file in the handover.

**Outcomes:** no claim was affected, so every outcome stays as it was:
- **Reproduced:** gaze-anticipates-action, gaze-anticipates-landmarks, learning-trials, learning-to-90, sparsity-state-vs-direction.
- **Partially reproduced:** cells-recorded, direction-tuning-not-maintained.
- **Not reproduced:** probe-transfer, state-space-most-responsive, direction-center-vs-periphery, sparsity-state-vs-po
[... 85 more lines not kept]
```

**Agent calls Bash**

```bash
cd  head -c 3500 transcripts/wirth-2017/verifier-1-report.md; echo; echo ====; head -c 2500 transcripts/wirth-2017/verifier-2-report.md; echo; grep -n "Wirth\|wirth" README.md | head -3; sed -n 1,40p README.md | grep -n "^|" | head -3
```

```
A. Outcomes for the 28 claims in the claims file

| Claim | Outcome | Reason |
|---|---|---|
| gaze-anticipates-action | reproduced | Cell 23: before right turns the eye signal differs from before left turns in each monkey, in both windows and for every eye choice (500 ms, both eyes: K −0.77 SD, p = 4e-148; S −1.00 SD, p = 4e-146; 39/40 and 20/20 sessions). The direction depends on an assumed sign of the eye signal (cell 24, problem 1). |
| gaze-anticipates-landmarks | partially_reproduced | Cell 26: the eye signal differs between right and left returns in each monkey, p ≤ 1.5e-10 under every reading. The side relative to the turn is not tested independently, because the sign was chosen on the assumption that the eyes deviate toward the side the view rotates to, and that is what this test measures (problem 1). |
| learning-trials | reproduced | Cell 17: S 12.26 (12.3 ± 2), K 16.53 under reading (a) and 15.82 under (b) (14.8 ± 2.4). The curves are the files' own; their column order was checked against `learningtrial` in 66 of 66 sessions (cell 8). |
| learning-to-90 | reproduced | Cell 18: 0.898 of sessions that reach both criteria, 0.803 of all sessions; both fall within 0.89 ± 0.089. |
| probe-transfer | not_reproduced | Cell 20: monkey K, 12 sessions: 28.3% in the first 5 trials (44 ± 4.4) and 58.3% after the new entries (73 ± 7.3); Wilcoxon p = 0.072. Monkey S has no probe session in hc-12 and none in hc-21 (data_missing for that part). |
| probe-faster-criterion | blocked (methods_underspecified) | The criterion needs learning curves recomputed from the introduction with the unnamed method of reference 60. Monkey S also has no probe sessions (data_missing). |
| cells-recorded | partially_reproduced | Cell 14: 186 cells with more than 100 spikes (189 ± 18.9). The archive holds only the 189 deposited cells, so the 270 recorded cells (128 S, 142 K) cannot be checked. |
| responsive-cells | blocked (metadata_insufficient) | The point-of-gaze space needs a calibrated
[... 27 more lines not kept]
```

**Agent**

The datasets are on CRCNS, so `targets/dandisets.json` has no entry for them and the notes leave out the CatalystNeuro sentence. Next I'm writing the two files.

**Agent calls Write**

```json
{
 "file_path": "docs/pilot-notes/wirth-2017-01.md",
 "content": "# wirth-2017, Wirth et al. 2017\n\nFive claims reproduced, two partially, five not reproduced and 16 blocked, 13\nas `metadata_insufficient` and three as `methods_underspecified`. The paper,\nWirth, Baraduc, Plante, Pinede and Duhamel in PLoS Biology, records 189\nhippocampal cells of two rhesus macaques, S and K, that navigate a virtual\nfive-arm star maze with a joystick, with a new landmark layout each day, and\ncompares how the cells code position, direction, point of gaze and a state\nspace of the task. The claims were written from the version of record\n(PMC5328243) without S1 and S2 Appendix, which are DOCX files that were not\nread, and every claim lists hc-12, the deposit the paper names; hc-21 was used\nonly to check its overlap with hc-12 and to look for the missing probe\nsessions. Reproduced are the two claims that gaze anticipates turns and\nlandmarks (both on an assumed sign of the eye signal), the two learning claims\n(12.26 and 16.53 trials to criterion; 0.898 of sessions reach 0.9 within 10\ntrials) and `sparsity-state-vs-direction` (p = 0.0022, only with the passive\nreturns in the trial window). Partial are `cells-recorded` (186 cells with more\nthan 100 spikes, but the 270 recorded are not deposited) and\n`state-space-ic-higher` (state space above position and direction, p < 0.01\nunder all six readings; the gaze comparison cannot be made). Not reproduced are\n`probe-transfer` (monkey K 28.3% and 58.3% against 44% and 73%, and no probe\nsession of S), `state-space-most-responsive` (57 of 186 cells under the main\nreading, 37 to 57 under all, against 75.6 to 92.4),\n`sparsity-state-vs-position` (state space is significantly sparser overall,\np = 0.00013 to 0.00043, where the paper finds no difference),\n`state-space-selectivity` (on permuted chunks; open under shifted chunks) and\n`landmark-identity-distance` (at most 31 cells with a distance effect, 33 with\ntype III sums of squares, against 64 +- 6.4). Every claim that needs the\npoint-of-gaze space, the responsive set or foveation is blocked, as are the\nprobe criterion count, the field count and the dimensionality control, whose\nmethods are in the unread appendix or in the unnamed reference 60. Round 1\nagreed with 24 of the 28 outcomes; it found that the shifted-chunk surrogates\noverlapped and made a train without coding significant, which was fixed and\nevery analysis re-run, and in reply `state-space-ic-higher` moved from blocked\nto partially reproduced, `direction-center-vs-periphery` from not reproduced to\npartially reproduced and `direction-tuning-not-maintained` from partially\nreproduced to not reproduced, while the author kept `gaze-anticipates-landmarks`\nreproduced after setting the eye sign from the slow-phase velocity during turns\n(40 of 40 sessions of K, 20 of 20 of S). Round 2 agreed with all 28, asked for a\ncaveat that the view already rotates toward the turn before the turn code, and\nfound that the text on the abscissa did not match the printed values, both\ncorrected; the author then proposed moving the two direction claims to blocked,\nas the paper's responsive set lies between bounds that both meet and fail\ntheir criteria, and a third round agreed with both changes. The third revision\nrun found that an earlier run of the same step (commit d9b90dd) had already\nmade these edits and changed nothing. The author's run took about 1 h 50 min\n(11:51 to 13:42 UTC), the notebook ran in 1,231 s and 1,178 s at first and\n1724 s after round 2, and the loader failed twice during development on files\nin other layouts, fixed before the final runs. Uncommitted changes to\n`tools/build_site.py` and two `tools/site_assets` files, which the runs did not\nmake, were left alone.\n\nThe horizontal and vertical eye signals have no units, calibration or sign\nconvention, on a +-5000 scale in 36 hc-12 sessions and a +-5 scale in 26, with\nsaturated samples at the bound (up to 22% of a session), so the paper's\npoint-of-gaze maps, foveation and landmark eccentricity cannot be computed;\nevery claim blocked as `metadata_insufficient` rests on this, and the sign used\nhere is inferred from the slow phases during turns. hc-12 holds 12 probe\nsessions of monkey K and none of monkey S, where the paper reports 15 and 9,\nand the 8 probe-like sessions of hc-21 are all among K's 12; in 3 of the 12 the\nfirst entries lie on both sides of the rewarded arm, and in the other 9 on one\nside, clockwise in 2 and counterclockwise in 7, where the paper describes\nnortheastern and southeastern entries. 87 of the 101 hc-21 files hold the same\nspike trains as hc-12 files under other file names, and neither descriptor says\nthat the two data sets overlap. Two hc-12 files (sn20121015_HPC_e2_c1a and c1c)\nhave no new-maze data, so 187 of the 189 cells can be analysed. The descriptor\nputs the probability of a correct response in the middle column of\n`learning_curves`, while in all 187 files the columns are probability, lower\nbound and upper bound, and the field `learningtrial`, not described, is the\nfirst trial whose lower bound exceeds 1/4. The descriptor gives the eye\npositions at 250 Hz, where `eye_times` are 5 ms apart (200 Hz) in every file,\nand says code 53 is the rewarded chosen arm, which holds in 32 of 66 sessions.\nThe files come in seven layouts (spike times under `file.elec` in 175 files and\nonly under `newallo.elec` in 12, camera data at the top level or under\n`newallo`, camera orientation from 0 to 360 or from -180 to 180), where the\ndescriptor gives one. Questions are put to the paper's authors: how the 5 s\nchunks were shifted for the surrogates and whether the maps include the passive\nreturns, which change the significant counts (state space 57 or 47 of 186 cells\nwith returns, 42 or 37 without); which learning-curve method is reference 60\nand how trials to criterion were counted after the new entries; how a\npositional field is defined and how the dimensionality control was done; and\nwhich three rotational moves enter the selectivity index and which laps the\ntwo-way ANOVA used, as its residual df of 756 fits all 193 laps of session\nsn20110624.\n\nThe author's points on the protocol: the archives are tar.gz files that cannot\nbe opened in place, and each was streamed and reduced member by member; the\nprotocol does not say how to judge a count over a selection that cannot be\nformed, and bounds were used, with a claim blocked only when they include the\nexpected value; it does not say what to do when part of a criterion cannot be\ntested, and `probe-transfer` was judged on monkey K's values, which already\nfail; it does not address development caches of reduced arrays; and it defines\n`partially_reproduced` only loosely.\n"
}
```

```
File created successfully at: docs/pilot-notes/wirth-2017-01.md (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "docs/pilot-notes/wirth-2017-01.md",
 "old_string": "as the paper's responsive set lies between bounds that both meet and fail\ntheir criteria, and a third round",
 "new_string": "as the paper's responsive set cannot be formed and the sets it could be give\ndifferent outcomes, and a third round"
}
```

```
The file docs/pilot-notes/wirth-2017-01.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Write**

```json
{
 "file_path": "summaries/wirth-2017-01.md",
 "content": "Some of the paper's central findings on hippocampal cells of monkeys navigating a virtual maze held up in this data, several did not, and those involving gaze could not be tested. Maps in the task's state space carried more information than position and direction maps and were sparser than direction maps. Fewer cells were significant in state space (57 against the paper's 84), fewer coded distance to landmarks, and selectivity for the current rotation at the maze centre failed under an assumed surrogate method the paper leaves open. Gaze maps, foveation-aligned responses and the direction tuning comparisons need a calibrated eye signal, which the files lack. Among minor claims, gaze anticipation and learning speed reproduced, while transfer in probe sessions did not.\n"
}
```

```
File created successfully at: summaries/wirth-2017-01.md (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd  wc -w summaries/wirth-2017-01.md docs/pilot-notes/wirth-2017-01.md; grep -c "—\|rather" summaries/wirth-2017-01.md docs/pilot-notes/wirth-2017-01.md; git status --short
```

```
122 summaries/wirth-2017-01.md
1106 docs/pilot-notes/wirth-2017-01.md
1228 total
summaries/wirth-2017-01.md:0
docs/pilot-notes/wirth-2017-01.md:0
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
?? docs/pilot-notes/wirth-2017-01.md
?? scripts
?? summaries/wirth-2017-01.md
```

**Agent calls Write**

```json
{
 "file_path": "summaries/wirth-2017-01.md",
 "content": "Some of the paper's central findings on hippocampal cells of monkeys navigating a virtual maze held up in this data, several did not, and those involving gaze could not be tested. Maps in the task's state space carried more information than position and direction maps and were sparser than direction maps. Fewer cells were significant in state space (57 against the paper's 84), fewer coded distance to landmarks, and selectivity for the rotation at the maze centre failed under an assumed surrogate method the paper leaves open. Gaze maps, foveation-aligned responses and the direction tuning comparisons need a calibrated eye signal, which the files lack. Of the minor claims, gaze anticipation and learning speed reproduced and probe-session transfer did not.\n"
}
```

```
The file summaries/wirth-2017-01.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd  wc -w summaries/wirth-2017-01.md; cat docs/pilot-notes/wirth-2017-01.md
```

```
120 summaries/wirth-2017-01.md
# wirth-2017, Wirth et al. 2017

Five claims reproduced, two partially, five not reproduced and 16 blocked, 13
as `metadata_insufficient` and three as `methods_underspecified`. The paper,
Wirth, Baraduc, Plante, Pinede and Duhamel in PLoS Biology, records 189
hippocampal cells of two rhesus macaques, S and K, that navigate a virtual
five-arm star maze with a joystick, with a new landmark layout each day, and
compares how the cells code position, direction, point of gaze and a state
space of the task. The claims were written from the version of record
(PMC5328243) without S1 and S2 Appendix, which are DOCX files that were not
read, and every claim lists hc-12, the deposit the paper names; hc-21 was used
only to check its overlap with hc-12 and to look for the missing probe
sessions. Reproduced are the two claims that gaze anticipates turns and
landmarks (both on an assumed sign of the eye signal), the two learning claims
(12.26 and 16.53 trials to criterion; 0.898 of sessions reach 0.9 within 10
trials) and `sparsity-state-vs-direction` (p = 0.0022, only with the passive
returns in the trial window). Partial are `cells-recorded` (186 cells with more
than 100 spikes, but the 270 recorded are not deposited) and
`state-space-ic-higher` (state space above position and direction, p < 0.01
[... 74 more lines not kept]
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "docs/pilot-notes/wirth-2017-01.md",
 "old_string": "Every claim that needs the\npoint-of-gaze space, the responsive set or foveation is blocked, as are the\nprobe criterion count,",
 "new_string": "Blocked are the claims that\nneed the point-of-gaze space or foveation, or a count over the paper's\nresponsive set that the bounds of the attempt cannot decide, and the probe\ncriterion count,"
}
```

```
The file docs/pilot-notes/wirth-2017-01.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "docs/pilot-notes/wirth-2017-01.md",
 "old_string": "1724 s after round 2",
 "new_string": "1,724 s after round 2"
}
```

```
The file docs/pilot-notes/wirth-2017-01.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "summaries/wirth-2017-01.md",
 "old_string": "Some of the paper's central findings",
 "new_string": "Some central findings"
}
```

```
The file summaries/wirth-2017-01.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd  wc -w summaries/wirth-2017-01.md; sed -n 30,36p docs/pilot-notes/wirth-2017-01.md
```

```
117 summaries/wirth-2017-01.md
responsive set that the bounds of the attempt cannot decide, and the probe
criterion count, the field count and the dimensionality control, whose
methods are in the unread appendix or in the unnamed reference 60. Round 1
agreed with 24 of the 28 outcomes; it found that the shifted-chunk surrogates
overlapped and made a train without coding significant, which was fixed and
every analysis re-run, and in reply `state-space-ic-higher` moved from blocked
to partially reproduced, `direction-center-vs-periphery` from not reproduced to
```

**Agent**

I wrote `docs/pilot-notes/wirth-2017-01.md` and `summaries/wirth-2017-01.md`. Nothing is committed. The two datasets are on CRCNS and have no entry in `targets/dandisets.json`, so the notes have no CatalystNeuro sentence. The summary is 117 words.

# wirth-2017, Wirth et al. 2017

Five claims reproduced, two partially, five not reproduced and 16 blocked, 13 as `metadata_insufficient` and three as `methods_underspecified`. The paper, Wirth, Baraduc, Plante, Pinede and Duhamel in PLoS Biology, records 189 hippocampal cells of two rhesus macaques, S and K, that navigate a virtual five-arm star maze with a joystick, with a new landmark layout each day, and compares how the cells code position, direction, point of gaze and a state space of the task. The claims were written from the version of record (PMC5328243) without S1 and S2 Appendix, which are DOCX files that were not read, and every claim lists hc-12, the deposit the paper names; hc-21 was used only to check its overlap with hc-12 and to look for the missing probe sessions. Reproduced are the two claims that gaze anticipates turns and landmarks (both on an assumed sign of the eye signal), the two learning claims (12.26 and 16.53 trials to criterion; 0.898 of sessions reach 0.9 within 10 trials) and `sparsity-state-vs-direction` (p = 0.0022, only with the passive returns in the trial window). Partial are `cells-recorded` (186 cells with more than 100 spikes, but the 270 recorded are not deposited) and `state-space-ic-higher` (state space above position and direction, p < 0.01 under all six readings; the gaze comparison cannot be made). Not reproduced are `probe-transfer` (monkey K 28.3% and 58.3% against 44% and 73%, and no probe session of S), `state-space-most-responsive` (57 of 186 cells under the main reading, 37 to 57 under all, against 75.6 to 92.4), `sparsity-state-vs-position` (state space is significantly sparser overall, p = 0.00013 to 0.00043, where the paper finds no difference), `state-space-selectivity` (on permuted chunks; open under shifted chunks) and `landmark-identity-distance` (at most 31 cells with a distance effect, 33 with type III sums of squares, against 64 +- 6.4). Blocked are the claims that need the point-of-gaze space or foveation, or a count over the paper's responsive set that the bounds of the attempt cannot decide, and the probe criterion count, the field count and the dimensionality control, whose methods are in the unread appendix or in the unnamed reference 60. Round 1 agreed with 24 of the 28 outcomes; it found that the shifted-chunk surrogates overlapped and made a train without coding significant, which was fixed and every analysis re-run, and in reply `state-space-ic-higher` moved from blocked to partially reproduced, `direction-center-vs-periphery` from not reproduced to partially reproduced and `direction-tuning-not-maintained` from partially reproduced to not reproduced, while the author kept `gaze-anticipates-landmarks` reproduced after setting the eye sign from the slow-phase velocity during turns (40 of 40 sessions of K, 20 of 20 of S). Round 2 agreed with all 28, asked for a caveat that the view already rotates toward the turn before the turn code, and found that the text on the abscissa did not match the printed values, both corrected; the author then proposed moving the two direction claims to blocked, as the paper's responsive set cannot be formed and the sets it could be give different outcomes, and a third round agreed with both changes. The third revision run found that an earlier run of the same step (commit d9b90dd) had already made these edits and changed nothing. The author's run took about 1 h 50 min (11:51 to 13:42 UTC), the notebook ran in 1,231 s and 1,178 s at first and 1,724 s after round 2, and the loader failed twice during development on files in other layouts, fixed before the final runs. Uncommitted changes to `tools/build_site.py` and two `tools/site_assets` files, which the runs did not make, were left alone.

The horizontal and vertical eye signals have no units, calibration or sign convention, on a +-5000 scale in 36 hc-12 sessions and a +-5 scale in 26, with saturated samples at the bound (up to 22% of a session), so the paper's point-of-gaze maps, foveation and landmark eccentricity cannot be computed; every claim blocked as `metadata_insufficient` rests on this, and the sign used here is inferred from the slow phases during turns. hc-12 holds 12 probe sessions of monkey K and none of monkey S, where the paper reports 15 and 9, and the 8 probe-like sessions of hc-21 are all among K's 12; in 3 of the 12 the first entries lie on both sides of the rewarded arm, and in the other 9 on one side, clockwise in 2 and counterclockwise in 7, where the paper describes northeastern and southeastern entries. 87 of the 101 hc-21 files hold the same spike trains as hc-12 files under other file names, and neither descriptor says that the two data sets overlap. Two hc-12 files (sn20121015_HPC_e2_c1a and c1c) have no new-maze data, so 187 of the 189 cells can be analysed. The descriptor puts the probability of a correct response in the middle column of `learning_curves`, while in all 187 files the columns are probability, lower bound and upper bound, and the field `learningtrial`, not described, is the first trial whose lower bound exceeds 1/4. The descriptor gives the eye positions at 250 Hz, where `eye_times` are 5 ms apart (200 Hz) in every file, and says code 53 is the rewarded chosen arm, which holds in 32 of 66 sessions. The files come in seven layouts (spike times under `file.elec` in 175 files and only under `newallo.elec` in 12, camera data at the top level or under `newallo`, camera orientation from 0 to 360 or from -180 to 180), where the descriptor gives one. Questions are put to the paper's authors: how the 5 s chunks were shifted for the surrogates and whether the maps include the passive returns, which change the significant counts (state space 57 or 47 of 186 cells with returns, 42 or 37 without); which learning-curve method is reference 60 and how trials to criterion were counted after the new entries; how a positional field is defined and how the dimensionality control was done; and which three rotational moves enter the selectivity index and which laps the two-way ANOVA used, as its residual df of 756 fits all 193 laps of session sn20110624.

The author's points on the protocol: the archives are tar.gz files that cannot be opened in place, and each was streamed and reduced member by member; the protocol does not say how to judge a count over a selection that cannot be formed, and bounds were used, with a claim blocked only when they include the expected value; it does not say what to do when part of a criterion cannot be tested, and `probe-transfer` was judged on monkey K's values, which already fail; it does not address development caches of reduced arrays; and it defines `partially_reproduced` only loosely.

---

Summary (`summaries/wirth-2017-01.md`):

Some central findings on hippocampal cells of monkeys navigating a virtual maze held up in this data, several did not, and those involving gaze could not be tested. Maps in the task's state space carried more information than position and direction maps and were sparser than direction maps. Fewer cells were significant in state space (57 against the paper's 84), fewer coded distance to landmarks, and selectivity for the rotation at the maze centre failed under an assumed surrogate method the paper leaves open. Gaze maps, foveation-aligned responses and the direction tuning comparisons need a calibrated eye signal, which the files lack. Of the minor claims, gaze anticipation and learning speed reproduced and probe-session transfer did not.

## End of run

21 turns, 2 minutes, $1.13 at API prices, result: success.
