# 001273 · recorder · run 41354537082

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  git log --diff-filter=A --name-only --format= -- docs/pilot-notes | head -n 5; echo; python tools/readme_row.py 001273; ls claims/001273 transcripts/001273; cat attempts/001273-semenov-2025-01.yaml; python -c "
import json;d=json.load(open('targets/dandisets.json'));
items=d if isinstance(d,list) else d.get('dandisets',d)
for x in (items if isinstance(items,list) else items.values()):
  if '001273' in json.dumps(x)[:200]: print(json.dumps(x,indent=1))
"
```

```
<persisted-output>
Output too large (43.3KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/b5cce524-9971-4b6e-8a0b-e51393032de8/tool-results/b0frq102c.txt

Preview (first 2KB):
docs/pilot-notes/001272-semenov-2025-01.md
docs/pilot-notes/001271-semenov-2025-01.md
docs/pilot-notes/001274-semenov-2025-01.md
docs/pilot-notes/001256-cody-2024-01.md
docs/pilot-notes/001261-luo-2024-01.md

| [001273](https://dandiarchive.org/dandiset/001273) | [Semenov et al. 2025](https://doi.org/10.1016/j.xcrp.2025.102660) | 2 | 0 | 1 | 3 | [`001273-semenov-2025`](entries/001273-semenov-2025) |
claims/001273:
10.1016-j.xcrp.2025.102660.yaml

transcripts/001273:
answer-report.md
answer.md
author-answers-report.md
author-answers.md
author-report.md
[... 47 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat attempts/001273-semenov-2025-01.yaml; for f in docs/pilot-notes/001272-semenov-2025-01.md docs/pilot-notes/001271-semenov-2025-01.md docs/pilot-notes/001274-semenov-2025-01.md docs/pilot-notes/001256-cody-2024-01.md docs/pilot-notes/001261-luo-2024-01.md; do echo "=== $f"; cat $f; done
```

```
<persisted-output>
Output too large (87.7KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/b5cce524-9971-4b6e-8a0b-e51393032de8/tool-results/bbpwns2ja.txt

Preview (first 2KB):
schema_version: 2
id: 001273-semenov-2025-01
dataset:
  archive: dandi
  id: "001273"
  version: 0.250805.1356
  doi: 10.48324/dandi.001273/0.250805.1356
paper: doi:10.1016/j.xcrp.2025.102660
date: 2026-11-01
entry: 001273-semenov-2025
provenance:
  kind: agent
  accountable:
    name: CatalystNeuro
  agent:
    harness: Claude Code
[... 28 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n '"001273"' -A25 targets/dandisets.json | head -40; cat claims/001273/*.yaml
```

```
<persisted-output>
Output too large (35.6KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/b5cce524-9971-4b6e-8a0b-e51393032de8/tool-results/b809frk66.txt

Preview (first 2KB):
5389:   "dandiset": "001273",
5390-   "name": "Kinetics of Membrane Charging and Its Dependence on Neuron Shape and Alignment with the Electric Field",
5391-   "published_version": "0.250805.1356",
5392-   "asset_count": 181,
5393-   "size_gb": 10.63,
5394-   "data_standards": [
5395-    "Neurodata Without Borders (NWB)"
5396-   ],
5397-   "species": [
5398-    "Rattus norvegicus - Norway rat"
5399-   ],
5400-   "approaches": [],
5401-   "papers": [
5402-    {
5403-     "doi": "10.1016/j.xcrp.2025.102660",
5404-     "title": "Excitation and polarization of isolated neurons by high-frequency sine waves for temporal interference stimulation",
[... 26 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/b5cce524-9971-4b6e-8a0b-e51393032de8/tool-results/bbpwns2ja.txt",
 "limit": 200
}
```

```
1	schema_version: 2
2	id: 001273-semenov-2025-01
3	dataset:
4	  archive: dandi
5	  id: "001273"
6	  version: 0.250805.1356
7	  doi: 10.48324/dandi.001273/0.250805.1356
8	paper: doi:10.1016/j.xcrp.2025.102660
9	date: 2026-11-01
10	entry: 001273-semenov-2025
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
[... 180 more lines not kept]
```

**Agent calls Bash**

```bash
cd  wc -l attempts/001273-semenov-2025-01.yaml; sed -n 200,400p attempts/001273-semenov-2025-01.yaml
```

```
679 attempts/001273-semenov-2025-01.yaml
  - F is the mean over the whole 16 x 16 frame. At this resolution the soma the Methods name
    ("emission intensity over the entire cell soma") cannot be outlined.
  - The bleaching trace is the only session without APs during the stimulus under both
    readings (c7 at 1.0 V), used for every cell (Methods, "corrected for bleaching by
    subtracting a trace without APs"). Uncorrected results are shown too.
  - The first 20 frames (6.4 ms) of each file are dropped, a standard choice. The first frame is
    2.6 to 7.6 times brighter than the rest, and the next ones recover from it.
  - The criterion does not say how cells are combined. Each cell's field series is judged on its
    own, as Figure 3C shows one cell ("Sustained firing and depolarization in a neuron", Figure 3
    legend). Assumed that the claim is reproduced when the criterion holds in most cells,
    partially reproduced when it holds in at least one cell or its firing parts hold in most,
    and not reproduced otherwise. The Results present the neuron of Figure 3C as what was
    observed ("we observed sustained firing for the entire duration of the sine wave"), so a
    typical cell should show it, which a single cell does not establish. The outcome rests on
    this rule. Judged on any one cell the claim would be reproduced (c7); judged on most cells it
    would not.
  - AP detection runs on a 1-ms running mean of the trace; a reading (a) peak must stand 5% dF
    above its surroundings, and peaks of both readings must be at least 5 ms apart. These are
    standard choices (APs last about 10 ms, Methods). The first run used no smoothing and a
[... 182 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 400,679p attempts/001273-semenov-2025-01.yaml
```

```
labels or notes.
  - claim: fig4-no-pole-difference
    agrees: true
    outcome: reproduced
    reason: Reproduced (weak). No p < 0.05 for |dFmax|, charging tau or discharging tau under any
      of the 16 unscaled readings, in either experiment set, and the frame-scaled variant gives
      the same. Only 7 to 15 pairs survive the fits (not 19), and the 95% intervals are wide, so
      the test has little power. |dFmax| enters the paired test only when the charging fit
      succeeded at both poles, and the hyperpolarized pole loses more fits. The fits also use only
      the nominal onset, frame 20, where estimated onsets range from 18 to 21.
    response: No change of outcome, as the criterion's quantity shows no difference under any of
      its readings. Added variants with each experiment's estimated onset, with fits whose tau
      exceeds its window dropped, with ROI (a) clipped to the soma, and with |dF| over the last
      0.5 us of the pulse, which needs no fit and keeps all 22 experiments. The time constants
      differ under none. The amplitude does in set A, in two variants (|dF| larger at the anodic
      pole, p = 0.014 and 0.011; |dFmax| at p = 0.046 in 2 of 8 readings of the window variant),
      not in the 40 V set; the notes and the conclusion now say so.
  - claim: fig4-discharging-slower
    agrees: true
    outcome: blocked
[... 260 more lines not kept]
```

**Agent**

Read the attempt record. Next, the recent notes, the README column headers and the author's report.

**Agent calls Bash**

```bash
cd  grep -n -B3 '| Dandiset\|^| ---' README.md | head -20; for f in docs/pilot-notes/001272-semenov-2025-01.md docs/pilot-notes/001271-semenov-2025-01.md docs/pilot-notes/001274-semenov-2025-01.md docs/pilot-notes/001256-cody-2024-01.md docs/pilot-notes/001261-luo-2024-01.md; do echo "=== $f"; cat $f; done
```

```
<persisted-output>
Output too large (45.2KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/b5cce524-9971-4b6e-8a0b-e51393032de8/tool-results/bjr6lgks3.txt

Preview (first 2KB):
=== docs/pilot-notes/001272-semenov-2025-01.md
# 001272, Semenov et al. 2025

Two claims reproduced on the dataset, three not reproduced and none blocked,
and of the two claims that also need the FluoVolt dandisets, one partially
reproduced and one not reproduced. Of the 12 claims on data elsewhere, other
dandisets of the same paper, two reproduced (one on an assumption), two
partially reproduced, four not reproduced and four blocked. The first
verification round agreed with 12 of the 19 outcomes as they stood and the
second with 18, and a third round, held on the one change of outcome proposed
after the second, agreed with it. It pins version 0.250805.1358, the latest
published version; the paper cites none, and 0.250701.1622 has the same blobs.
The paper, Semenov, Kim, Silkuniene and Pakhomov, "Excitation and polarization
of isolated neurons by high-frequency sine waves for temporal interference
stimulation" in Cell Reports Physical Science, records optical APs by fast
imaging in cultured rat hippocampal neurons stimulated with sine waves, and
[... 14 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/b5cce524-9971-4b6e-8a0b-e51393032de8/tool-results/bjr6lgks3.txt"
}
```

```
1	=== docs/pilot-notes/001272-semenov-2025-01.md
2	# 001272, Semenov et al. 2025
3	
4	Two claims reproduced on the dataset, three not reproduced and none blocked,
5	and of the two claims that also need the FluoVolt dandisets, one partially
6	reproduced and one not reproduced. Of the 12 claims on data elsewhere, other
7	dandisets of the same paper, two reproduced (one on an assumption), two
8	partially reproduced, four not reproduced and four blocked. The first
9	verification round agreed with 12 of the 19 outcomes as they stood and the
10	second with 18, and a third round, held on the one change of outcome proposed
11	after the second, agreed with it. It pins version 0.250805.1358, the latest
12	published version; the paper cites none, and 0.250701.1622 has the same blobs.
13	The paper, Semenov, Kim, Silkuniene and Pakhomov, "Excitation and polarization
14	of isolated neurons by high-frequency sine waves for temporal interference
15	stimulation" in Cell Reports Physical Science, records optical APs by fast
16	imaging in cultured rat hippocampal neurons stimulated with sine waves, and
17	001272 holds the control experiment of Figure S1, neurons stained with
18	Di-8-ANEPPS in place of FluoVolt and stimulated with 250-ms unmodulated 2-kHz
19	sine waves. The claims were written from the NIH author manuscript
20	(PMC12320893) with its supplement, Figure S1 read from its legend only; the
[... 617 more lines not kept]
```

**Agent**

Now the README columns, the readme_row logic, the author's and later reports.

**Agent calls Bash**

```bash
cd  grep -n 'Reproduced\|Partial' README.md | head; sed -n 1,80p tools/readme_row.py; grep -n '001272\|001274' README.md
```

```
"""The README's table row for a dataset, from its latest attempt.

    python tools/readme_row.py DATASET            # print the row

Counts are of the paper's findings on the dandiset, including those that name its codes from
elsewhere (`with_labels`); findings that also use outside data (`with_inputs`) are shown in brackets;
findings on data in other archives (`elsewhere`) and the registry's link checks (`kind: link`) are
left out, as the README says. A deprecated attempt's row has no counts.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
[... 58 more lines not kept]
```

**Agent calls Bash**

```bash
cd  f=claims/001273/*.yaml; sed -n 1,60p $f; grep -n '^- id:\|^  data:\|^  - id:\|    data:' $f; ls -la transcripts/001273; git log --format='%h %ad %s' --date=iso -- transcripts/001273 attempts/001273-semenov-2025-01.yaml | head -20
```

```
# Claims for Semenov, Kim, Silkuniene & Pakhomov (2025), Cell Reports Physical Science 6, 102660,
# on dandiset 001273.
# Written by an agent (model "claude-opus-5-5", Claude Code in GitHub Actions), 2026-10-22, under
# docs/protocol.md version pilot-10, as the reader.
#
# Text read. The NIH author manuscript (NIHMS2098259, PMC12320893) as served by Europe PMC, with its
# main text, figure legends and STAR Methods, and the supplement (NIHMS2098259-supplement-1.pdf,
# Figures S1 to S4 and Table S1, the Key Resource Table), all in
# paper/10.1016-j.xcrp.2025.102660.txt. The version of record was not read. No main-text PDF was
# available, so Figures 1 to 6 could not be looked at; values shown only in figures (the group
# means of Figures 4D and 4E, the n per group of Figure 2D) are not used.
#
# Code. The paper states that it does not report original code. Exponential fits and the standard
# errors of fitted constants were made with Origin 8.0; ROI intensities with MetaMorph; linear
# regression with Grapher 16 (STAR Methods, Quantification and statistical analysis).
#
# Data the paper used. E18 Sprague-Dawley rat hippocampal neurons (BrainBits), cultured about one
# week on coverslips, stained with FluoVolt (Di-8-ANEPPS in Figure S1). Two kinds of recording:
# (1) Fast imaging of the optical membrane potential (64 x 64 pixels, 3,130 or 3,086.4 frames/s,
# 1,200 images per session: 50 ms before, 250 ms during and about 90 ms after the stimulus) with
[... 97 more lines not kept]
```

**Agent calls Bash**

```bash
cd transcripts/001273; for f in author-report.md answer-report.md author-answers-report.md verifier-1-report.md author-revise-1-report.md verifier-2-report.md author-revise-2-report.md; do echo "=== $f"; cat $f; done
```

```
<persisted-output>
Output too large (31.3KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/b5cce524-9971-4b6e-8a0b-e51393032de8/tool-results/bvxn9gqun.txt

Preview (first 2KB):
=== author-report.md
I've finished steps 1 to 5 and run the handover (step 6) for DANDI:001273 at version 0.250805.1356. Of the 17 claims, 2 were reproduced, 1 partially reproduced, 2 not reproduced and 12 blocked. `tools/entry.py check` reports 0 errors and all three notebooks pass from a clean environment. Nothing is committed and no reader was asked a question.

**Version.** The paper cites no version. The two published versions have identical files (same 181 blobs) and differ only in an added grant, so I pinned the most recent and said why in the notebook header.

## 1. Outcomes

| Claim | Outcome | Notes |
|---|---|---|
| fig4-polarized-poles-face-electrodes | reproduced (assumed) | 13 of the 14 experiments that state an electrode axis pass; 1 of 14 passes with the axes swapped |
| fig4-no-pole-difference | reproduced | none of the 16 readings is significant at p < 0.05; wide intervals, so little power |
| fig4-pooled-time-constants | not reproduced | no reading puts all four within the paper's SEMs; cathodic discharging is 1.37 to 4.20 us against 0.91 |
| fig4-orientation-time-constants | blocked: metadata_insufficient | no shape or orientation labels in the dataset |
| fig4-discharging-slower | blocked: metadata_insufficient | the same labels are missing; the pooled test is shown |
| fig4-full-charge-within-3us | blocked: metadata_insufficient | its reading (b) fails, so it cannot stand in for (a) |
| fig3c-sustained-firing-2s (DANDI:001030) | partially reproduced | firing rises with field in all 4 cells; no cell meets the block test (c7 is closest, with 1 AP) |
[... 4 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/b5cce524-9971-4b6e-8a0b-e51393032de8/tool-results/bvxn9gqun.txt"
}
```

```
1	=== author-report.md
2	I've finished steps 1 to 5 and run the handover (step 6) for DANDI:001273 at version 0.250805.1356. Of the 17 claims, 2 were reproduced, 1 partially reproduced, 2 not reproduced and 12 blocked. `tools/entry.py check` reports 0 errors and all three notebooks pass from a clean environment. Nothing is committed and no reader was asked a question.
3	
4	**Version.** The paper cites no version. The two published versions have identical files (same 181 blobs) and differ only in an added grant, so I pinned the most recent and said why in the notebook header.
5	
6	## 1. Outcomes
7	
8	| Claim | Outcome | Notes |
9	|---|---|---|
10	| fig4-polarized-poles-face-electrodes | reproduced (assumed) | 13 of the 14 experiments that state an electrode axis pass; 1 of 14 passes with the axes swapped |
11	| fig4-no-pole-difference | reproduced | none of the 16 readings is significant at p < 0.05; wide intervals, so little power |
12	| fig4-pooled-time-constants | not reproduced | no reading puts all four within the paper's SEMs; cathodic discharging is 1.37 to 4.20 us against 0.91 |
13	| fig4-orientation-time-constants | blocked: metadata_insufficient | no shape or orientation labels in the dataset |
14	| fig4-discharging-slower | blocked: metadata_insufficient | the same labels are missing; the pooled test is shown |
15	| fig4-full-charge-within-3us | blocked: metadata_insufficient | its reading (b) fails, so it cannot stand in for (a) |
16	| fig3c-sustained-firing-2s (DANDI:001030) | partially reproduced | firing rises with field in all 4 cells; no cell meets the block test (c7 is closest, with 1 AP) |
17	| figs1-di8-anepps-control (DANDI:001272) | not reproduced | no session reaches the 5% depolarization (largest 3.2%); 3 neurons where the paper has 8 |
18	| fig1, fig2, fig2c, fig2d, fig3b, figs2 | blocked: other | not tested for lack of time; fig3b's sodium gluconate sessions do not appear to be deposited |
19	| fig5, fig6, threshold-depolarization-estimate |
[... 245 more lines not kept]
```

**Agent**

I have everything I need. The final counts match the author's first run, round 1 disagreed only on fig3c, round 2 agreed with all 17, and there was no third round. Writing the note now.

**Agent calls Write**

```json
{
 "file_path": "docs/pilot-notes/001273-semenov-2025-01.md",
 "content": "# 001273, Semenov et al. 2025\n\nTwo claims reproduced on the dataset (one on an assumption), none partially,\none not reproduced and three blocked. Of the 11 claims on data elsewhere,\nother dandisets of the same paper, one partially reproduced on an assumption,\none not reproduced and nine blocked. The first verification round agreed with\n16 of the 17 outcomes as they stood and the second with all 17, and nothing was\nproposed after the second, so there was no third round. It pins version\n0.250805.1356; the paper cites none, and the two published versions have the\nsame 181 blobs and differ only in an added grant. The paper, Semenov, Kim,\nSilkuniene and Pakhomov, \"Excitation and polarization of isolated neurons by\nhigh-frequency sine waves for temporal interference stimulation\" in Cell\nReports Physical Science, stimulates cultured rat hippocampal neurons stained\nwith FluoVolt with sine waves and records optical APs by fast imaging, and\nimages membrane charging under 2-us pulses at 140 V/cm by pulsed laser strobe\nimaging at 50-ns steps (Figure 4), the experiment of 001273. The claims were\nwritten from the NIH author manuscript (PMC12320893) with its supplement; the\npaper reports no original code. On the dataset,\n`fig4-polarized-poles-face-electrodes` reproduces on reading \"Up and Bottom\"\nin the session description as the image's vertical axis: in 13 of the 14\nexperiments that name the electrode axis the extreme pixels lie on opposite\nsides of the soma centroid within 45 degrees of the field axis (median 13.8\ndegrees), and 1 of 14 with the axes swapped. `fig4-no-pole-difference`\nreproduces, none of the 16 unscaled readings finding a difference at p < 0.05,\nbut weakly: 7 to 10 of 22 experiments per reading lose a pair to a failed fit,\nand the |dF| over the last 0.5 us of the pulse, which needs no fit, is larger\nat the anodic pole in set A (p = 0.014, ROI a). `fig4-pooled-time-constants`\nis not reproduced, no reading putting all four means within the paper's SEMs\n(cathodic discharging 1.37 to 4.20 us against 0.91 plus or minus 0.08).\n`fig4-orientation-time-constants`, `fig4-discharging-slower` and\n`fig4-full-charge-within-3us` are blocked as `metadata_insufficient`, the shape\nand orientation groups not being in the dataset. Elsewhere,\n`fig3c-sustained-firing-2s` is partially reproduced on DANDI:001030, the\ncriterion holding in 1 of 4 cells (c7) and its firing part in all 4, an\noutcome that rests on judging each cell on its own, and\n`figs1-di8-anepps-control` is not reproduced on DANDI:001272, no session\nreaching the 5% depolarization level (largest 3.2%). The other nine claims are\nblocked as other, not tested for lack of time. The author's first run gave the\nsame counts, with three of the blocked claims given as `too_large`. The author\nasked a reader nothing, so the answer and author-answers runs changed nothing;\na reader question on whether the FluoVolt 5% level suits Di-8-ANEPPS was added\nin the round-1 revision, after those runs. Round 1 disagreed only with fig3c,\ngiving not reproduced by the letter of the criterion, and found that its AP\ndetector counted noise on a depolarized plateau as APs (197 at c7 2.3 V), that\nfits accepted tau up to 50 us from a 2-us window, that the fits used only the\nnominal onset though a docstring said otherwise, and that the ROI square was\nnot clipped to the soma; in reply the detector was revised, after which c7\nmeets the whole criterion, fig3c was kept as partial with the disagreement\nrecorded, and variants with the estimated onset, with long-tau fits dropped,\nwith ROI a clipped to the soma, with the soma mask opened (12 of 14 pass) and\nwith the fit-free |dF| were added, none changing an outcome. Round 2 asked that\nfig3c be marked assumed with its rule stated and that the three `too_large`\nreasons be other, both done, and found sentences the outputs did not support\n(a streaming time of 1,115 s, the survey of the other dandisets, the README's\nfile count, the figs1 AP readings and the no-pole wording), which were\ncorrected, the survey moving into a new notebook,\nsurvey_other_dandisets.ipynb. The author's run took about 3 h 10 min (15:04\nto about 18:16 UTC); the first full run exposed a wrong check of\n`starting_time` and a wrong count of single files, both fixed. The notebooks\nran in 1349 s, 40 s and 81 s at first, the main one in 1,495 s after round 1,\nand the survey notebook in about 9 minutes. `tools/build_site.py` was found\nmodified before the revisions and left untouched.\n\nThe dataset holds only the raw strobe images: the ROIs over the de- and\nhyperpolarized poles, the debris ROI used to scale out laser-flash\nfluctuations and the shape and orientation group of each experiment are not in\nit, so the group comparisons of Figures 4D and 4E cannot be made and the time\nconstants cannot be recomputed as the paper did. The January 17 files say\n\"Electrode position not specified\", and no file says which electrode was the\ncathode or how the camera image is oriented relative to the named directions.\nThe files form 22 runs of 7 or 8 replicates plus six single files at 100 V,\nwhere the paper reports 19 experiments, with nothing saying which runs were\nused; the nominal amplitudes are 40, 60, 80, 100 and 130 V where the paper\ngives one field, 140 V/cm, and no file gives the field. Files recorded \"in a\nbackward manner\" are stored in acquisition order, so their frames run back in\ntime, which the files do not say beyond the stepping direction. The time base\n(50 ns per frame) is given only in prose, the ImageSeries rate is the camera's\n6 Hz, and starting_time holds a Unix time where NWB expects seconds after the\nsession start. The 13 subjects are cells, with age P18D for neurons dissected\nat E18 and cultured about one week. The Results give 180 images per replicate\nand the Methods 160; the files hold 160. The first image of 156 of 175 files is\nabout half as bright as the rest, and 204 frames in all were dropped as dim.\nAcross the paper's deposits, DANDI:001034 holds the same 178 image arrays as\nDANDI:001032 under other subject ids, every session description of 001032 to\n001035 names the NaCl solution so the sodium gluconate thresholds of Figure 3B\ndo not appear to be deposited, DANDI:001272 holds three Di-8-ANEPPS neurons\nwhere the paper reports eight, and DANDI:001030 gives the species as Mus\nmusculus, with two of its 17 sessions ending at 1.91 s, before the 2-s stimulus\ndoes. The 2-us, 257 V/cm pulse recordings of the nine cells of Figures 5 and 6\nare not in 001273, whose files date from January and March 2024. A question is\nput to the paper's authors: the size and placement of the pole ROIs, how the\nfits were weighted, whether the discharge amplitude was free, and whether the\nROIs, the debris ROI and the list of the 19 experiments with their groups could\nbe deposited.\n\nThe author's points on the protocol: a claim marked elsewhere whose data are\nnot there cannot be `data_missing`, and `other` was used; `too_large` covers\nonly a computation that stopped, not a claim never started for lack of time;\nno rule covers experiments that cannot be matched to the paper's (22 runs\nagainst 19), and both all 22 and the 15 at 40 V were run; the protocol does not\nsay whether the author may read another dataset's claims file that a criterion\npoints to; it does not say whether findings may rest on surveys run outside the\nnotebooks; the main notebook's 22.5 minutes, nearly all streaming, is over the\n10-minute aim; and without the debris ROI the paper's flash correction cannot\nbe repeated, so unscaled traces were used with whole-frame scaling as a\nvariant.\n"
}
```

```
File created successfully at: docs/pilot-notes/001273-semenov-2025-01.md (file state is current in your context — no need to Read it back)
```

**Agent**

I wrote `docs/pilot-notes/001273-semenov-2025-01.md` and changed no other file. Nothing is committed. Some details of how the run went:

- **Counts:** the README row reads 2 reproduced, 0 partially, 1 not reproduced and 3 blocked, all on the dataset. These match the author's first run.
- **Verification rounds:** round 1 disagreed only on fig3c, and round 2 agreed with all 17 outcomes. Nothing was proposed after round 2, so there was no third round.
- **Late reader question:** the question on whether the 5% level suits Di-8-ANEPPS was added after the answer runs, so it was never answered. The note says this.
- **Unrelated change:** `tools/build_site.py` had been modified before the revision runs. The author left it untouched, and the round-2 report says the workflow will commit it unless someone removes it.

Here is the subsection:

# 001273, Semenov et al. 2025

Two claims reproduced on the dataset (one on an assumption), none partially, one not reproduced and three blocked. Of the 11 claims on data elsewhere, other dandisets of the same paper, one partially reproduced on an assumption, one not reproduced and nine blocked. The first verification round agreed with 16 of the 17 outcomes as they stood and the second with all 17, and nothing was proposed after the second, so there was no third round. It pins version 0.250805.1356; the paper cites none, and the two published versions have the same 181 blobs and differ only in an added grant. The paper, Semenov, Kim, Silkuniene and Pakhomov, "Excitation and polarization of isolated neurons by high-frequency sine waves for temporal interference stimulation" in Cell Reports Physical Science, stimulates cultured rat hippocampal neurons stained with FluoVolt with sine waves and records optical APs by fast imaging, and images membrane charging under 2-us pulses at 140 V/cm by pulsed laser strobe imaging at 50-ns steps (Figure 4), the experiment of 001273. The claims were written from the NIH author manuscript (PMC12320893) with its supplement; the paper reports no original code. On the dataset, `fig4-polarized-poles-face-electrodes` reproduces on reading "Up and Bottom" in the session description as the image's vertical axis: in 13 of the 14 experiments that name the electrode axis the extreme pixels lie on opposite sides of the soma centroid within 45 degrees of the field axis (median 13.8 degrees), and 1 of 14 with the axes swapped. `fig4-no-pole-difference` reproduces, none of the 16 unscaled readings finding a difference at p < 0.05, but weakly: 7 to 10 of 22 experiments per reading lose a pair to a failed fit, and the |dF| over the last 0.5 us of the pulse, which needs no fit, is larger at the anodic pole in set A (p = 0.014, ROI a). `fig4-pooled-time-constants` is not reproduced, no reading putting all four means within the paper's SEMs (cathodic discharging 1.37 to 4.20 us against 0.91 plus or minus 0.08). `fig4-orientation-time-constants`, `fig4-discharging-slower` and `fig4-full-charge-within-3us` are blocked as `metadata_insufficient`, the shape and orientation groups not being in the dataset. Elsewhere, `fig3c-sustained-firing-2s` is partially reproduced on DANDI:001030, the criterion holding in 1 of 4 cells (c7) and its firing part in all 4, an outcome that rests on judging each cell on its own, and `figs1-di8-anepps-control` is not reproduced on DANDI:001272, no session reaching the 5% depolarization level (largest 3.2%). The other nine claims are blocked as other, not tested for lack of time. The author's first run gave the same counts, with three of the blocked claims given as `too_large`. The author asked a reader nothing, so the answer and author-answers runs changed nothing; a reader question on whether the FluoVolt 5% level suits Di-8-ANEPPS was added in the round-1 revision, after those runs. Round 1 disagreed only with fig3c, giving not reproduced by the letter of the criterion, and found that its AP detector counted noise on a depolarized plateau as APs (197 at c7 2.3 V), that fits accepted tau up to 50 us from a 2-us window, that the fits used only the nominal onset though a docstring said otherwise, and that the ROI square was not clipped to the soma; in reply the detector was revised, after which c7 meets the whole criterion, fig3c was kept as partial with the disagreement recorded, and variants with the estimated onset, with long-tau fits dropped, with ROI a clipped to the soma, with the soma mask opened (12 of 14 pass) and with the fit-free |dF| were added, none changing an outcome. Round 2 asked that fig3c be marked assumed with its rule stated and that the three `too_large` reasons be other, both done, and found sentences the outputs did not support (a streaming time of 1,115 s, the survey of the other dandisets, the README's file count, the figs1 AP readings and the no-pole wording), which were corrected, the survey moving into a new notebook, survey_other_dandisets.ipynb. The author's run took about 3 h 10 min (15:04 to about 18:16 UTC); the first full run exposed a wrong check of `starting_time` and a wrong count of single files, both fixed. The notebooks ran in 1349 s, 40 s and 81 s at first, the main one in 1,495 s after round 1, and the survey notebook in about 9 minutes. `tools/build_site.py` was found modified before the revisions and left untouched.

The dataset holds only the raw strobe images: the ROIs over the de- and hyperpolarized poles, the debris ROI used to scale out laser-flash fluctuations and the shape and orientation group of each experiment are not in it, so the group comparisons of Figures 4D and 4E cannot be made and the time constants cannot be recomputed as the paper did. The January 17 files say "Electrode position not specified", and no file says which electrode was the cathode or how the camera image is oriented relative to the named directions. The files form 22 runs of 7 or 8 replicates plus six single files at 100 V, where the paper reports 19 experiments, with nothing saying which runs were used; the nominal amplitudes are 40, 60, 80, 100 and 130 V where the paper gives one field, 140 V/cm, and no file gives the field. Files recorded "in a backward manner" are stored in acquisition order, so their frames run back in time, which the files do not say beyond the stepping direction. The time base (50 ns per frame) is given only in prose, the ImageSeries rate is the camera's 6 Hz, and starting_time holds a Unix time where NWB expects seconds after the session start. The 13 subjects are cells, with age P18D for neurons dissected at E18 and cultured about one week. The Results give 180 images per replicate and the Methods 160; the files hold 160. The first image of 156 of 175 files is about half as bright as the rest, and 204 frames in all were dropped as dim. Across the paper's deposits, DANDI:001034 holds the same 178 image arrays as DANDI:001032 under other subject ids, every session description of 001032 to 001035 names the NaCl solution so the sodium gluconate thresholds of Figure 3B do not appear to be deposited, DANDI:001272 holds three Di-8-ANEPPS neurons where the paper reports eight, and DANDI:001030 gives the species as Mus musculus, with two of its 17 sessions ending at 1.91 s, before the 2-s stimulus does. The 2-us, 257 V/cm pulse recordings of the nine cells of Figures 5 and 6 are not in 001273, whose files date from January and March 2024. A question is put to the paper's authors: the size and placement of the pole ROIs, how the fits were weighted, whether the discharge amplitude was free, and whether the ROIs, the debris ROI and the list of the 19 experiments with their groups could be deposited.

The author's points on the protocol: a claim marked elsewhere whose data are not there cannot be `data_missing`, and `other` was used; `too_large` covers only a computation that stopped, not a claim never started for lack of time; no rule covers experiments that cannot be matched to the paper's (22 runs against 19), and both all 22 and the 15 at 40 V were run; the protocol does not say whether the author may read another dataset's claims file that a criterion points to; it does not say whether findings may rest on surveys run outside the notebooks; the main notebook's 22.5 minutes, nearly all streaming, is over the 10-minute aim; and without the debris ROI the paper's flash correction cannot be repeated, so unscaled traces were used with whole-frame scaling as a variant.

## End of run

14 turns, 1 minutes, result: success.
