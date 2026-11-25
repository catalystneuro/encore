# kim-2025 · recorder · run 45027628054

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  git log --diff-filter=A --name-only --format= -- docs/pilot-notes | head -n 5; python tools/readme_row.py kim-2025; ls transcripts/kim-2025/; cat attempts/kim-2025-01.yaml; cat claims/kim-2025.yaml
```

```
<persisted-output>
Output too large (114.9KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/1af6d771-c8b3-41bb-894f-be6feecc7a8e/tool-results/bkd8i9vzk.txt

Preview (first 2KB):
docs/pilot-notes/amjad-2025-01.md
docs/pilot-notes/andrews-2024-01.md
docs/pilot-notes/armstrong-2026-01.md
docs/pilot-notes/asari-2009-01.md
docs/pilot-notes/asari-2009-02.md
| [000248](https://dandiarchive.org/dandiset/000248) | [Kim et al. 2025](https://doi.org/10.1101/2025.06.30.662469) | 3 | 0 | 0 | 0 | [`kim-2025`](entries/kim-2025) |
author-report.md
author-revise-1-report.md
author-revise-1.md
author-revise-2-report.md
author-revise-2.md
author.md
claims-check-report.md
claims-check.md
claims-report.md
claims.md
[... 39 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat attempts/kim-2025-01.yaml; echo ======; wc -c claims/kim-2025.yaml transcripts/kim-2025/*; grep -n -A12 '"000248"' targets/dandisets.json | head -40
```

```
<persisted-output>
Output too large (69.8KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/1af6d771-c8b3-41bb-894f-be6feecc7a8e/tool-results/b2ix42pzc.txt

Preview (first 2KB):
schema_version: 3
id: kim-2025-01
datasets:
- archive: dandi
  id: 000248
  version: 0.240502.2344
  doi: 10.48324/dandi.000248/0.240502.2344
  relation: reuses
paper: doi:10.1101/2025.06.30.662469
date: '2026-11-21'
entry: kim-2025
provenance:
  kind: agent
  accountable:
    name: CatalystNeuro
  agent:
[... 24 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/1af6d771-c8b3-41bb-894f-be6feecc7a8e/tool-results/b2ix42pzc.txt"
}
```

```
1	schema_version: 3
2	id: kim-2025-01
3	datasets:
4	- archive: dandi
5	  id: 000248
6	  version: 0.240502.2344
7	  doi: 10.48324/dandi.000248/0.240502.2344
8	  relation: reuses
9	paper: doi:10.1101/2025.06.30.662469
10	date: '2026-11-21'
11	entry: kim-2025
12	provenance:
13	  kind: agent
14	  accountable:
15	    name: CatalystNeuro
16	  agent:
17	    harness: Claude Code
18	    model: claude-opus-5-5
19	    protocol: pilot-18
20	  runner:
[... 756 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/1af6d771-c8b3-41bb-894f-be6feecc7a8e/tool-results/b2ix42pzc.txt",
 "offset": 777
}
```

```
777	      (problem 5).
778	    response: 'Changed to reproduced. Tested in reproduce_kim_2025_decoding.ipynb: decoding at as-is and slope 0
779	      (p = 5e-05 and 0.035), within-session RSM similarity (16 of 21 slopes and as-is with p < 0.05) and across-session
780	      RSM similarity (all 21 slopes and as-is) all differ between original and shuffled data. The comparison needs
781	      only the decoding at the conditions run, so it is tested although fig2b-decoding-falls-with-slope stays blocked.
782	      The unused shuffle_within_stimulus, which permuted all neurons together (problem 8), now permutes each neuron
783	      separately and is used for the RSMs.'
784	- date: '2026-11-22'
785	  kind: agent
786	  by: Independent agent run by CatalystNeuro (same harness, separate context, did not write the notebooks)
787	  reviewed: Round 2. The full executed notebooks (reproduce_kim_2025.ipynb, reproduce_kim_2025_allen.ipynb and reproduce_kim_2025_decoding.ipynb)
788	    with their conclusions and summaries, the helper module kim2025.py, the claims file, the attempt record and
789	    the paper. The report counts 24 reproduced and 4 blocked outcomes but names three blocked claims; the record
790	    has 25 reproduced (figs4c-shuffling-alters-dependence among them) and 3 blocked. No finding is rated critical,
791	    so none was reviewed for its rating; the report says none of the findings describes a data error that would
792	    qualify, and that the no-defect statements of finding 3 are supported by nb1 cells 3, 5 and 6.
793	  results:
794	  - claim: illusion-data-link
795	    agrees: true
796	    outcome: reproduced
[... 219 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat tools/readme_row.py | head -80; sed -n 1797,1840p targets/dandisets.json; ls entries/kim-2025; cat transcripts/kim-2025/author-report.md
```

```
"""The README's table row for a paper, from its latest attempt.

    python tools/readme_row.py PAPER              # print the row (a paper key, or a dataset listed for one)

Counts are of the paper's findings on the dandiset, including those that name its codes from
elsewhere (`with_labels`); findings that also use outside data (`with_inputs`) are shown in brackets;
findings on data in other archives (`elsewhere`) and the registry's link checks (`kind: link`) are
left out, as the README says. A deprecated attempt's row has no counts.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
[... 164 more lines not kept]
```

**Agent**

Gathered the record and author report. Now reading the example notes, the other reports and the claims file.

**Agent calls Bash**

```bash
cd  grep -n -B2 -A3 'kind: link\|data: ' claims/kim-2025.yaml | head -80; for f in amjad-2025-01 andrews-2024-01 armstrong-2026-01 asari-2009-01 asari-2009-02 knierim-2000-02; do echo "=== $f"; cat docs/pilot-notes/$f.md; done; ls summaries | head;
```

```
<persisted-output>
Output too large (41.2KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/1af6d771-c8b3-41bb-894f-be6feecc7a8e/tool-results/bz78jzav0.txt

Preview (first 2KB):
101-claims:
102-- id: illusion-data-link
103:  kind: link
104-  statement: Dandiset 000248 holds the OpenScope Illusion recordings the paper used for its
105-    Isomap pictures, an ICwcfg1 block in which stimuli are repeated 400 times, with V1 units, in
106-    the example session the paper's code uses.
107-  source: Methods, Visualization of stimulus manifold geometry, paragraph 2; Data and code
108-    availability; visualize_manifold.ipynb cell 8 at commit ac3300b
109:  data: with_labels
110-  criterion: Reproduced when (i) sub_630506 is in the dandiset with an ICwcfg1 presentations block
111-    whose 400-repeat stimuli number 12, as the code expects (num_trial_types 12), (ii) the stimuli
112-    Ic1, Lc1, Tre1 and Tre2 can be identified in it, by the names the dandiset gives or through
--
187-  quote: The number of V1 neurons analyzed in the 30 sessions was 64 ± 25 (mean ± standard
188-    deviation).
189:  data: elsewhere
[... 23 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/1af6d771-c8b3-41bb-894f-be6feecc7a8e/tool-results/bz78jzav0.txt",
 "offset": 80
}
```

```
80	427-  where: Allen Brain Observatory Visual Coding Neuropixels, natural scenes block
81	=== amjad-2025-01
82	# 002013, Amjad et al. 2025
83	
84	Seven claims reproduced, one partially and five blocked on the dandiset,
85	plus one claim linking the dandiset to the paper's Zenodo deposit,
86	reproduced (trial lists agree for 99.8 to 100% of trials); both rounds
87	agreed with every outcome. The paper describes microinvasive probes for
88	recording dopamine and electrical activity in monkeys; the beta burst,
89	reward and unit isolation claims reproduce, the dopamine reward effect
90	weakly (p = 0.023, and not in the stored trial-aligned `da`).
91	
92	The dandiset was converted by CatalystNeuro (catalystneuro/schwerdt-lab-to-nwb,
93	the same conversion as 002014), and many findings are the same: each event
94	is stored about five times, once per overlapping trial window; trial
95	conditions are not in the trials table; the FSCV table columns carry no
96	units and the raw FSCV current is labelled amperes with values in the
97	thousands; the bipolar LFP is stored in volts with a conversion factor that
98	makes it picovolts; and the raw ephys of one session and the spike times of
99	Monkey P are on different clocks from the rest of the file, by 9831.35 s and
[... 531 more lines not kept]
```

**Agent calls Bash**

```bash
cd  for f in verifier-1 author-revise-1 verifier-2 author-revise-2; do echo "=== $f"; cat transcripts/kim-2025/$f-report.md; done; cat summaries/asari-2009-02.md summaries/armstrong-2026-01.md
```

```
=== verifier-1
A. Outcomes for all 28 claims in the claims file

| Claim | My outcome | Reason |
|---|---|---|
| illusion-data-link | reproduced | sub-630506 has an ICwcfg1 block with 12 stimuli at 400 repeats. Codes 3, 4, 10 and 11 (Ic1, Lc1, Tre1, Tre2 by the code's map) are among them, and the session has 75 V1 units (nb1 cells 3 and 8). All 11 of the code's subjects are present; sub-619293 is an extra session. |
| illusion-fig1c-isomap-geometry | reproduced | All three tests hold (slope-0 component of 1, as-is 3, mean overlap 0.00 < 0.22 < 0.32). They also hold in all 8 combinations of N-space or 2D Isomap, Methods or code threshold, and all VISp or quality units (nb1 cell 10). Other sessions are a variant: 9 of 12 pass (cell 13). |
| illusion-fig3a-orthogonal-variance-example | reproduced | Geodesic distance Lc1–Ic1 is 60.0 against 17.6 for Lc1–Tre2. Orthogonal variance is 0.0270 against 0.0161. The same order holds with quality units (cell 15). The 132-pair Spearman variant is weak (ρ 0.15, p 0.086). |
| illusion-geometry-similar-across-datasets | reproduced | Across 12 sessions, dimensionality falls 0.243 → 0.081 → 0.033 and overlap rises 0.142 → 0.398 → 0.603. Both change at every step, with p 0.0005 at slopes 0 and 2 (the exact minimum for n 12). Both unit readings agree (cell 17). |
| data-v1-units | reproduced (depends on the unit reading) | 30 sessions; the excluded ones are the 1st and 7th by session id, which I confirmed on the archive and which matches the code's 0 and 6. With the Methods' three criteria the mean (71.1) and total (2133) are out of tolerance. With AllenSDK's default "good" label added (66.9 ± 25.5, total 2008) every value is in tolerance (nb2 cell 7). |
| fig1b-across-neuron-slope-near-1 | reproduced (depends on the unit reading) | With "good" units: mean 1.0489, SD 0.0665, n 3570, all within tolerance. With the Methods criteria the mean is 1.0552, outside ±0.001 (nb2 cell 10). |
| fig1b-across-stimulus-slope | reproduced | Mean 1.134 
[... 152 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 1,100p claims/kim-2025.yaml; grep -n '^- id:\|^  statement:\|^  source:' claims/kim-2025.yaml | sed -n 1,200p
```

```
# Claims for Kim & Shin (2025), doi:10.1101/2025.06.30.662469, read for dandiset 000248.
# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"), 2026-11-21,
# protocol as stated in docs/protocol.md (Reader).
#
# Text read: paper/10.1101-2025.06.30.662469.txt, the bioRxiv full text of the preprint posted
# July 04, 2025, under the title "Neural variability structure in primary visual cortex is optimal
# for robust representation of visual similarity". The registry lists the paper under a later
# title ("Intrinsic geometry of trial-to-trial variability in primary visual cortex is optimal for
# robust representation of visual similarity"); that later version was not supplied, and every
# claim here is from the July 2025 text. That text holds the Results, Discussion, Methods and the
# legends of Figures 1 to 4 and S1 to S6; the supplementary figures are part of it, and there is
# no separate supplement. The equations of the Methods (slope manipulation, effective
# dimensionality, orthogonal component, number of RSA trial pairs, modulated Poisson model) are
# lost in the extraction, and the legends of Figures 2 and 3 are cut after "(Wilcoxon signed-rank
# test". No PDF was supplied, so figure panels could not be read. Where the equations are needed
# they are taken from the code below.
#
# Code read: GitHub jhk4839/Neural_variability_robustness at commit
# ac3300b007c2348ccda73c0c87fb02f557791089 (2025-07-03), the last commit before the preprint was
# posted; its README names the July 2025 title and maps the notebooks to this text's figure
[... 164 more lines not kept]
```

**Agent**

Now writing the two files.

**Agent calls Write**

```json
{
 "file_path": "docs/pilot-notes/kim-2025-01.md",
 "content": "# kim-2025, Kim et al. 2025\n\nThree claims reproduced on the dandiset, none partially, none not reproduced\nand none blocked, plus the claim linking the dandiset to the paper's example\nsession, reproduced; the 24 claims on the Allen Visual Coding Neuropixels data\n(`data: elsewhere`, read from dandisets 000021 and 000022) are counted apart,\n21 reproduced and 3 blocked. Seventeen outcomes rest on an assumption. The\nfirst verification round agreed with every outcome as it stood, though it\nwould have given `fig2b-decoding-falls-with-slope` the reason other, and the\nsecond agreed with all 28; nothing was proposed after the second, so there was\nno third round. The paper, Kim and Shin, \"Neural variability structure in\nprimary visual cortex is optimal for robust representation of visual\nsimilarity\" (bioRxiv preprint of July 2025), fits the log variance of V1 spike\ncounts against the log mean across neurons, finds a slope near 1, and by\nrescaling the trial residuals to slopes from 0 to 2 reports that\ndimensionality falls and manifold overlap rises with the slope, while\ncontinuity, alignment of manifolds with visual similarity and the consistency\nof representations within and across mice are best near slope 1. Dandiset\n000248, the OpenScope Illusion data, serves only the Isomap pictures of one\nexample session (sub-630506); the claims were written from a text extraction\nof the preprint without figure panels, with the equations taken from the\npaper's code at commit ac3300b. The Illusion claims reproduce in the example\nsession under every reading run (the three stimuli at slope 0 form a component\nof 1, 3 as-is). On the Allen data the unit counts (66.9 +- 25.5, 2008 in all)\nand the across-neuron slope (1.0489) match only with AllenSDK's default units,\nthose labelled good, and this was assumed for every Allen claim; the slope\nmanipulation, overlap, continuity, geodesic, alignment and consistency claims,\nthe behavioural state, higher-area and movie checks and the shuffle comparison\nreproduce. `figs6-higher-areas-consistency` passes only the criterion's first\nreading, which within sessions cannot tell slope 0 from slope 1, and this went\nto a reader in `questions/kim-2025.yaml`. Blocked are the decoding claim of\nFigure 2B as `too_large` (run at as-is and slopes 0 and 1 over 30 sessions and\nat slope 2 in four, with the 22 conditions estimated at about 5.4 hours), and\nthe gain variance fits and the tangent space angle as other, not ported within\nthe time of the runs. The author's first run gave 23 reproduced, 1 partially\nand 4 blocked. Round 1 found that the good units were used for two claims\nonly, that the movie session count was 24 against the paper's 23, and that\nthe decoding and shuffle claims could be tested in part; in reply the good\nunits were used throughout, the paper's code was found to skip\nsub-769319621 for invalid movie presentations, which moved\n`figs5a-movie-slope-near-1` from partial to reproduced, and\n`figs4c-shuffling-alters-dependence` was tested in a third notebook and moved\nfrom blocked to reproduced. The verifier of round 1 saw the Allen notebook's\nconclusion cells, which the handover had not removed, and based its outcomes\non the code outputs. Round 2 asked that the movie outcome be marked assumed,\nthat the shuffled and original decodings share trial order and folds, and\nthat the slope-2 timing be run in the entry, and found sentences the outputs\ndid not support, all corrected. The author's run took about 3 h 32 min (23:36\nto 03:08 UTC); the Allen notebook first ran in 2698 s, took 61 minutes after a\nlater change, and the three notebooks ran in 14, 41 and 49 minutes at the end.\n\nThe ICwcfg1 presentations table lists every 400 ms frame of the block,\nincluding the gray inter-trial frames, under one column; the gray frames show\nthe same image as the Blank stimulus, nothing marks which of them are Blank\ntrials, and the image codes 0 to 21 have no names in the files or the\ndandiset metadata, so the names come only from the paper's code. The trials\ncan be recovered from the sequence (60 leading gray frames, then trial and\ngray frame alternating, 400 Blank trials in every session), and the templates\nagree in kind with the code's names; the code read a post-processed copy\n(v240130) that is not public. The units table describes none of its columns.\nThe spikes share the clock of the ICwcfg1 table: the V1 population rate rises\n75 ms after image onsets and not after Blank onsets, and image identity is\ndecoded from the 400 ms after onset (0.576, chance 0.083) and not from the\n400 ms before (0.089). No session is deposited twice, and all 11 sessions the\ncode lists are present, with a twelfth, sub-619293, that it does not list. In\ndandiset 000021 the pupil area is labelled Pixels ^ 2 but ranges from 0.0002\nto 0.012. Two questions are put to the paper's authors: whether the units\nwere those of AllenSDK's default units table, and which third Functional\nConnectivity session was excluded, since no session in dandiset 000022 has an\nincomplete movie repeat and the paper's code names sub-769319621, whose movie\nblock overlaps an invalid_times interval, which the Methods' word truncated\ndoes not describe.\n\nThe author's points on the protocol: claims on data elsewhere made up most of\nthe paper and the protocol gives no priority between them and the dataset's\nown claims; the rule of five seeds is too costly for the overlap halves and\nthe decoding; no block reason fits a claim not attempted within the time\nlimit; a finding about an input dataset, here the pupil area units, has no\nplace in the record; the protocol does not say whether to apply defaults of\nthe software the paper used to read the data, here AllenSDK's good filter;\nand timings printed in a notebook change from run to run, so a conclusion\nthat quotes them exactly breaks on re-run.\n"
}
```

```
File created successfully at: docs/pilot-notes/kim-2025-01.md (file state is current in your context — no need to Read it back)
```

**Agent calls Write**

```json
{
 "file_path": "summaries/kim-2025-01.md",
 "content": "The paper's main findings held up, tested mostly on the Allen Neuropixels sessions it analysed, since dandiset 000248 (OpenScope Illusion) holds only its example Isomap pictures, which reproduced too. Across V1 neurons, log variance rose with log mean at a slope near 1 (1.0489 against the reported 1.048), and when that slope was rescaled, manifold overlap rose while manifold alignment and the consistency of representations within and across mice peaked near 1. These results assume the paper used AllenSDK's default units labelled good, which the Methods do not state but which the unit counts match. The fall of decoding accuracy with slope was too slow to run in full, and the tangent space angle was not implemented in time, so neither was tested.\n"
}
```

```
File created successfully at: summaries/kim-2025-01.md (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd  grep -c 'assumed: true' attempts/kim-2025-01.yaml; wc -w summaries/kim-2025-01.md; grep -n '—\|rather' docs/pilot-notes/kim-2025-01.md summaries/kim-2025-01.md; git status --short
```

```
19
123 summaries/kim-2025-01.md
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
?? docs/pilot-notes/kim-2025-01.md
?? scripts
?? summaries/kim-2025-01.md
```

**Agent calls Bash**

```bash
cd  sed -n 41,467p attempts/kim-2025-01.yaml | grep -c 'assumed: true'; grep -n 'assumed: true' attempts/kim-2025-01.yaml | tail -3
```

```
18
388:  assumed: true
437:  assumed: true
939:    reason: 'Agrees, but the outcome should be marked assumed: true. The count of 23 sessions (tolerance 0) is reached
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "docs/pilot-notes/kim-2025-01.md",
 "old_string": "21 reproduced and 3 blocked. Seventeen outcomes",
 "new_string": "21 reproduced and 3 blocked. Eighteen outcomes"
}
```

```
The file docs/pilot-notes/kim-2025-01.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "docs/pilot-notes/kim-2025-01.md",
 "old_string": "the Allen notebook first ran in 2698 s, took 61 minutes after a\nlater change, and the three notebooks",
 "new_string": "the Allen notebook first ran in 2698 s and took 61 minutes, over\nthe limit, before the first revision, and the three notebooks"
}
```

```
The file docs/pilot-notes/kim-2025-01.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "summaries/kim-2025-01.md",
 "old_string": "The paper's main findings held up, tested mostly on the Allen Neuropixels sessions it analysed, since dandiset 000248 (OpenScope Illusion) holds only its example Isomap pictures, which reproduced too. Across V1 neurons, log variance rose with log mean at a slope near 1 (1.0489 against the reported 1.048), and when that slope was rescaled, manifold overlap rose while manifold alignment and the consistency of representations within and across mice peaked near 1. These results assume the paper used AllenSDK's default units labelled good, which the Methods do not state but which the unit counts match.",
 "new_string": "The paper's main findings held up, tested mostly on the Allen Neuropixels sessions it analysed, since dandiset 000248 (OpenScope Illusion) holds only its example Isomap pictures, which reproduced too. Across V1 neurons, log variance rose with log mean at a slope near 1 (1.0489 against 1.048), and when that slope was rescaled, manifold overlap rose while alignment and the consistency of representations within and across mice peaked near 1. These results assume the paper used AllenSDK's default units labelled good, which the Methods do not state."
}
```

```
The file summaries/kim-2025-01.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd  wc -w summaries/kim-2025-01.md; cat docs/pilot-notes/kim-2025-01.md summaries/kim-2025-01.md
```

```
114 summaries/kim-2025-01.md
# kim-2025, Kim et al. 2025

Three claims reproduced on the dandiset, none partially, none not reproduced
and none blocked, plus the claim linking the dandiset to the paper's example
session, reproduced; the 24 claims on the Allen Visual Coding Neuropixels data
(`data: elsewhere`, read from dandisets 000021 and 000022) are counted apart,
21 reproduced and 3 blocked. Eighteen outcomes rest on an assumption. The
first verification round agreed with every outcome as it stood, though it
would have given `fig2b-decoding-falls-with-slope` the reason other, and the
second agreed with all 28; nothing was proposed after the second, so there was
no third round. The paper, Kim and Shin, "Neural variability structure in
primary visual cortex is optimal for robust representation of visual
similarity" (bioRxiv preprint of July 2025), fits the log variance of V1 spike
counts against the log mean across neurons, finds a slope near 1, and by
rescaling the trial residuals to slopes from 0 to 2 reports that
dimensionality falls and manifold overlap rises with the slope, while
continuity, alignment of manifolds with visual similarity and the consistency
of representations within and across mice are best near slope 1. Dandiset
000248, the OpenScope Illusion data, serves only the Isomap pictures of one
[... 64 more lines not kept]
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "docs/pilot-notes/kim-2025-01.md",
 "old_string": "to 03:08 UTC); the Allen notebook first ran in 2698 s and took 61 minutes, over\nthe limit, before the first revision, and the three notebooks ran in 14, 41 and 49 minutes at the end.",
 "new_string": "to 03:08 UTC); the Allen notebook first ran in 2698 s and took 61 minutes,\nover the limit, before the first revision, and the three notebooks ran in 14,\n41 and 49 minutes at the end."
}
```

```
The file docs/pilot-notes/kim-2025-01.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent**

I wrote the two new files, `docs/pilot-notes/kim-2025-01.md` and `summaries/kim-2025-01.md`, and changed nothing else. Nothing is committed. `tools/readme_row.py kim-2025` prints 3 | 0 | 0 | 0 because it counts only the three claims tested on dandiset 000248 itself. The link claim and the 24 claims on the Allen data in dandisets 000021 and 000022 are left out, so the notes give those separately.

# kim-2025, Kim et al. 2025

Three claims reproduced on the dandiset, none partially, none not reproduced
and none blocked, plus the claim linking the dandiset to the paper's example
session, reproduced; the 24 claims on the Allen Visual Coding Neuropixels data
(`data: elsewhere`, read from dandisets 000021 and 000022) are counted apart,
21 reproduced and 3 blocked. Eighteen outcomes rest on an assumption. The
first verification round agreed with every outcome as it stood, though it
would have given `fig2b-decoding-falls-with-slope` the reason other, and the
second agreed with all 28; nothing was proposed after the second, so there was
no third round. The paper, Kim and Shin, "Neural variability structure in
primary visual cortex is optimal for robust representation of visual
similarity" (bioRxiv preprint of July 2025), fits the log variance of V1 spike
counts against the log mean across neurons, finds a slope near 1, and by
rescaling the trial residuals to slopes from 0 to 2 reports that
dimensionality falls and manifold overlap rises with the slope, while
continuity, alignment of manifolds with visual similarity and the consistency
of representations within and across mice are best near slope 1. Dandiset
000248, the OpenScope Illusion data, serves only the Isomap pictures of one
example session (sub-630506); the claims were written from a text extraction
of the preprint without figure panels, with the equations taken from the
paper's code at commit ac3300b. The Illusion claims reproduce in the example
session under every reading run (the three stimuli at slope 0 form a component
of 1, 3 as-is). On the Allen data the unit counts (66.9 +- 25.5, 2008 in all)
and the across-neuron slope (1.0489) match only with AllenSDK's default units,
those labelled good, and this was assumed for every Allen claim; the slope
manipulation, overlap, continuity, geodesic, alignment and consistency claims,
the behavioural state, higher-area and movie checks and the shuffle comparison
reproduce. `figs6-higher-areas-consistency` passes only the criterion's first
reading, which within sessions cannot tell slope 0 from slope 1, and this went
to a reader in `questions/kim-2025.yaml`. Blocked are the decoding claim of
Figure 2B as `too_large` (run at as-is and slopes 0 and 1 over 30 sessions and
at slope 2 in four, with the 22 conditions estimated at about 5.4 hours), and
the gain variance fits and the tangent space angle as other, not ported within
the time of the runs. The author's first run gave 23 reproduced, 1 partially
and 4 blocked. Round 1 found that the good units were used for two claims
only, that the movie session count was 24 against the paper's 23, and that
the decoding and shuffle claims could be tested in part; in reply the good
units were used throughout, the paper's code was found to skip
sub-769319621 for invalid movie presentations, which moved
`figs5a-movie-slope-near-1` from partial to reproduced, and
`figs4c-shuffling-alters-dependence` was tested in a third notebook and moved
from blocked to reproduced. The verifier of round 1 saw the Allen notebook's
conclusion cells, which the handover had not removed, and based its outcomes
on the code outputs. Round 2 asked that the movie outcome be marked assumed,
that the shuffled and original decodings share trial order and folds, and
that the slope-2 timing be run in the entry, and found sentences the outputs
did not support, all corrected. The author's run took about 3 h 32 min (23:36
to 03:08 UTC); the Allen notebook first ran in 2698 s and took 61 minutes,
over the limit, before the first revision, and the three notebooks ran in 14,
41 and 49 minutes at the end.

The ICwcfg1 presentations table lists every 400 ms frame of the block,
including the gray inter-trial frames, under one column; the gray frames show
the same image as the Blank stimulus, nothing marks which of them are Blank
trials, and the image codes 0 to 21 have no names in the files or the
dandiset metadata, so the names come only from the paper's code. The trials
can be recovered from the sequence (60 leading gray frames, then trial and
gray frame alternating, 400 Blank trials in every session), and the templates
agree in kind with the code's names; the code read a post-processed copy
(v240130) that is not public. The units table describes none of its columns.
The spikes share the clock of the ICwcfg1 table: the V1 population rate rises
75 ms after image onsets and not after Blank onsets, and image identity is
decoded from the 400 ms after onset (0.576, chance 0.083) and not from the
400 ms before (0.089). No session is deposited twice, and all 11 sessions the
code lists are present, with a twelfth, sub-619293, that it does not list. In
dandiset 000021 the pupil area is labelled Pixels ^ 2 but ranges from 0.0002
to 0.012. Two questions are put to the paper's authors: whether the units
were those of AllenSDK's default units table, and which third Functional
Connectivity session was excluded, since no session in dandiset 000022 has an
incomplete movie repeat and the paper's code names sub-769319621, whose movie
block overlaps an invalid_times interval, which the Methods' word truncated
does not describe.

The author's points on the protocol: claims on data elsewhere made up most of
the paper and the protocol gives no priority between them and the dataset's
own claims; the rule of five seeds is too costly for the overlap halves and
the decoding; no block reason fits a claim not attempted within the time
limit; a finding about an input dataset, here the pupil area units, has no
place in the record; the protocol does not say whether to apply defaults of
the software the paper used to read the data, here AllenSDK's good filter;
and timings printed in a notebook change from run to run, so a conclusion
that quotes them exactly breaks on re-run.

---

The paper's main findings held up, tested mostly on the Allen Neuropixels sessions it analysed, since dandiset 000248 (OpenScope Illusion) holds only its example Isomap pictures, which reproduced too. Across V1 neurons, log variance rose with log mean at a slope near 1 (1.0489 against 1.048), and when that slope was rescaled, manifold overlap rose while alignment and the consistency of representations within and across mice peaked near 1. These results assume the paper used AllenSDK's default units labelled good, which the Methods do not state. The fall of decoding accuracy with slope was too slow to run in full, and the tangent space angle was not implemented in time, so neither was tested.

## End of run

19 turns, 2 minutes, $1.13 at API prices, result: success.
