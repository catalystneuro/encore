# kay-2008 · recorder · run 43603588473

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
git log --diff-filter=A --name-only --format= -- docs/pilot-notes | head -n 5; python tools/readme_row.py kay-2008; ls transcripts/kay-2008/; wc -c attempts/kay-2008-01.yaml claims/kay-2008.yaml transcripts/kay-2008/*
```

```
docs/pilot-notes/amjad-2025-01.md
docs/pilot-notes/andrews-2024-01.md
docs/pilot-notes/armstrong-2026-01.md
docs/pilot-notes/asari-2009-01.md
docs/pilot-notes/ashworth-2025-01.md
| [CRCNS:vim-1](http://crcns.org/data-sets/vc/vim-1) | [Kay et al. 2008](https://doi.org/10.1038/nature06713) | 7 | 3 | 3 | 6 (+4) | [`kay-2008`](entries/kay-2008) |
answer-report.md
answer.md
author-answers-report.md
author-answers.md
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
[... 25 more lines not kept]
```

**Agent calls Bash**

```bash
cd docs/pilot-notes; for f in amjad-2025-01.md andrews-2024-01.md armstrong-2026-01.md asari-2009-01.md ashworth-2025-01.md knierim-2000-02.md; do echo "=== $f"; cat $f; done; cd ../..; grep -n "| Dataset\|^| ---\|^|---" README.md | head; ls summaries | head -3; cat summaries/$(ls summaries | head -1)
```

```
<persisted-output>
Output too large (40KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/dc6b010a-3700-4100-b455-226749f75dea/tool-results/b8zm3x8tb.txt

Preview (first 2KB):
=== amjad-2025-01.md
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

**Agent calls Bash**

```bash
cd transcripts/kay-2008; for f in author-report.md author-revise-1-report.md author-revise-2-report.md claims-check-report.md claims-report.md verifier-1-report.md verifier-2-report.md answer-report.md author-answers-report.md; do echo "=== $f"; cat $f; done; cd ../..; python -c "
import json;d=json.load(open('targets/dandisets.json'))
it=d if isinstance(d,list) else d.get('dandisets',d)
for x in (it if isinstance(it,list) else it.values()):
  if 'vim-1' in json.dumps(x): print(json.dumps(x,indent=1))
"
```

```
<persisted-output>
Output too large (39.1KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/dc6b010a-3700-4100-b455-226749f75dea/tool-results/b91p18rs1.txt

Preview (first 2KB):
=== author-report.md
The attempt on Kay et al. (2008) is finished: 12 claims tested, 11 blocked. The entry passes `check` and a clean `run` (39 minutes, peak memory 8.6 GB), and the handover package was built. No verification of my own was done.

**1. Outcome per claim**

| Claim | Outcome |
|---|---|
| fig3-s1-repeated-120 | reproduced: 109/120 (90.8%), paper 110 |
| fig4a-s2-repeated-120 | reproduced: 87/120 (72.5%), paper 86 |
| suppm8-retinotopy-only-120 | reproduced: 53.3% and 43.8% (paper 55 and 42), both below the main model |
| errors-similar-images | reproduced with the local-contrast similarity (p = 0.00031); not with pixel luminance |
| supptable1-voxel-counts | reproduced: all six counts are exact |
| supptable1-predictive-power-by-area | reproduced: 6 of 6 within tolerance, V1 > V2 > V3 |
| methods-v4-poor | reproduced (the S1 margin is 0.7 points) |
| suppfig11-rf-size-eccentricity | reproduced, resting on an assumption |
| fig2-representative-voxel | partially reproduced, resting on an assumption |
[... 11 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/dc6b010a-3700-4100-b455-226749f75dea/tool-results/b8zm3x8tb.txt"
}
```

```
1	=== amjad-2025-01.md
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
[... 558 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/dc6b010a-3700-4100-b455-226749f75dea/tool-results/b91p18rs1.txt"
}
```

```
1	=== author-report.md
2	The attempt on Kay et al. (2008) is finished: 12 claims tested, 11 blocked. The entry passes `check` and a clean `run` (39 minutes, peak memory 8.6 GB), and the handover package was built. No verification of my own was done.
3	
4	**1. Outcome per claim**
5	
6	| Claim | Outcome |
7	|---|---|
8	| fig3-s1-repeated-120 | reproduced: 109/120 (90.8%), paper 110 |
9	| fig4a-s2-repeated-120 | reproduced: 87/120 (72.5%), paper 86 |
10	| suppm8-retinotopy-only-120 | reproduced: 53.3% and 43.8% (paper 55 and 42), both below the main model |
11	| errors-similar-images | reproduced with the local-contrast similarity (p = 0.00031); not with pixel luminance |
12	| supptable1-voxel-counts | reproduced: all six counts are exact |
13	| supptable1-predictive-power-by-area | reproduced: 6 of 6 within tolerance, V1 > V2 > V3 |
14	| methods-v4-poor | reproduced (the S1 margin is 0.7 points) |
15	| suppfig11-rf-size-eccentricity | reproduced, resting on an assumption |
16	| fig2-representative-voxel | partially reproduced, resting on an assumption |
17	| suppfig7-roi-tuning | not reproduced: the V1 spatial-frequency curve rises to the highest frequency in every variant, so it is not band-pass |
18	| suppdisc1-classification-extension | not reproduced: S2's contrast result is never above chance |
19	| suppm7-selected-voxels-v1 | not reproduced: 48% of selected voxels are in V1, not more than half |
20	| fig4a-single-trial, fig4a-noise-ceiling, suppfig4-500-voxels | blocked, `too_large`: refitting every voxel's time series is estimated at about 615 min |
[... 330 more lines not kept]
```

**Agent calls Bash**

```bash
grep -n -B3 "Kay et al" README.md | head; grep -n "^| Dataset\|(+" README.md | head -5; sed -n 1,80p tools/readme_row.py; python -c "
import json;d=json.load(open('targets/dandisets.json'))
print(type(d))
" ; grep -n -B2 -A12 "vim-1" targets/dandisets.json
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
[... 61 more lines not kept]
```

**Agent calls Bash**

```bash
grep -n -i "kay\|vim" targets/dandisets.json | head; python -c "
import json;d=json.load(open('targets/dandisets.json'));print(list(d.keys())[:10]); print(len(d))"
```

```
['schema_version', 'generated', 'source', 'counts', 'targets']
5
```

**Agent calls Read**

```json
{
 "file_path": "attempts/kay-2008-01.yaml"
}
```

```
1	schema_version: 3
2	id: kay-2008-01
3	datasets:
4	- archive: crcns
5	  id: vim-1
6	  version: unversioned
7	  doi: 10.6080/K0QN64NG
8	  relation: primary
9	paper: doi:10.1038/nature06713
10	date: 2026-11-14
11	entry: kay-2008
12	provenance:
13	  kind: agent
14	  accountable:
15	    name: CatalystNeuro
16	  agent:
17	    harness: Claude Code
18	    model: claude-opus-5-5
19	    protocol: pilot-15
20	  runner:
[... 723 more lines not kept]
```

**Agent calls Bash**

```bash
ls questions/ | grep kay; sed -n 1,40p claims/kay-2008.yaml; grep -n "^  - id:\|^- id:\|data: \|statement:\|location:" claims/kay-2008.yaml | head -120
```

```
kay-2008.yaml
# Claims for Kay, Naselaris, Prenger & Gallant (2008), Nature 452:352-355, "Identifying natural
# images from human brain activity", doi:10.1038/nature06713, on CRCNS data set vim-1.
# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"), 2026-11-10,
# protocol as stated in docs/protocol.md (Reader), version pilot-14.
#
# Text read: the version of record with its supplement, as PyMuPDF text under paper/
# (10.1038-nature06713.txt): the Letter, its Methods, and the Supplementary Information
# (Supplementary Figures 1 to 11, Supplementary Table 1, Supplementary Discussion 1 to 3,
# Supplementary Methods 1 to 11). PDF pages were rendered only for Figure 4 and Supplementary
# Figures 4, 5 and 8, whose numbers the text garbles. The data set's description
# (paper/vim-1.data-description.txt) was read only to know what it holds; no claim comes from it.
#
# Code: the paper links no analysis code, so none was read. It names outside code for two steps:
# m-sequence generation by T. Liu (stimulus design only) and Gaussian kernel density estimation by
# A. Ihler (http://ttic.uchicago.edu/~ihler/code/), used for the set-size extrapolation.
#
# Data the paper used. Two subjects, S1 (author T.N., 33) and S2 (author K.N.K., 25). 4 T Varian
# INOVA scanner, 18 coronal slices over occipital cortex, 64 x 64 matrix, TR 1 s, nominal 2 x 2 x
# 2.5 mm. Stimuli are 20 x 20 degree greyscale natural photographs (500 x 500 px, circular mask),
[... 71 more lines not kept]
```

**Agent**

Now I'll write both files.

**Agent calls Write**

```json
{
 "file_path": "docs/pilot-notes/kay-2008-01.md",
 "content": "# kay-2008, Kay et al. 2008\n\nSeven claims reproduced, three partially, three not reproduced and six\nblocked, plus four blocked that also need the paper's 999-image library\n(`with_inputs`); three outcomes, `fig2-representative-voxel`,\n`suppfig11-rf-size-eccentricity` and `supptable1-predictive-power-by-area`,\nrest on an assumption. The first verification round agreed with 21 of the 23\noutcomes as they stood and the second with all 23; nothing was proposed after\nthe second, so there was no third round. CRCNS data sets carry no version, so\nthe record gives `unversioned` with doi:10.6080/K0QN64NG and the notebook\nprints the MD5 sums from the bucket. The paper, Kay, Naselaris, Prenger and\nGallant, \"Identifying natural images from human brain activity\" (Nature\n452:352-355), fits a Gabor wavelet pyramid (GWP) receptive-field model to each\nfMRI voxel of V1 to V3 in two subjects from their responses to 1,750 natural\nimages, and identifies which of 120 new images a subject saw from the\npredicted activity patterns. The claims were written from the version of\nrecord with its supplement; the paper links no analysis code. Reproduced are\nidentification at set size 120 with repeated trials (109 of 120 for S1, paper\n110, and 87 of 120 for S2, paper 86), the retinotopy-only model at set size\n120 (52.1% and 43.3%, below the GWP model), errors falling on images similar\nin local contrast (p = 0.00031; not with pixel luminance), the six voxel\ncounts of Supplementary Table 1 (exact), the fall of predictive power from V1\nto V3, and the poor fit in V4 (the S1 margin is 0.7 points, and V4 stays below\nV3 under two other seeds). The identification results hold only with the\nfinal model's field of view set to the +/-2 SD square of the fitted Gaussian;\nwith the best initial model's field of view they are 75.8% and 46.7%. Partial\nare the example voxel of Figure 2 (left hemifield and high-pass hold; under\nthe adopted reading the envelope peaks 0.24 degrees above the horizontal\nmeridian and the orientation tuning is not broadband), the best voxel count of\nabout 500 (it holds for repeated trials, and the single-trial conditions are\nblocked) and receptive-field size against eccentricity (size rises with\neccentricity, but V1 < V2 < V3 holds in 2 of 5 shared 1 degree bins).\nNot reproduced are the band-pass V1 spatial frequency tuning of Supplementary\nFigure 7 (high-pass in every reading run), the classification-extension\ncontrol (S2's contrast metric gives 1 or 2 of 120, against 7) and most\nselected voxels lying in V1 (48%). Blocked as too large are the single-trial\nidentification, the noise ceilings and the SNR, which need the BRS model\nrefitted to every voxel's time series; blocked for missing data are the\nset-size, extrapolation and constrained-model claims, the two later S1\nsessions and the check against retinotopic mapping. The author's first run\ngave 8 reproduced, 1 partially, 3 not reproduced and 11 blocked. Round 1\nmoved `suppfig4-500-voxels` from blocked to partially reproduced, since its\nrepeated-trial conditions already met the rule, and\n`suppfig11-rf-size-eccentricity` from reproduced to partially reproduced, as\nFigure 2's legend calls the circle the bounds of the stimulus; it also found\nthe too-large estimates overstated, the luminance channel of the\nretinotopy-only model taken relative to the grey background, voxels with NaN\nresponses counted as not significant without saying so, and tuning ratios\nwith the DC offset that depend on an arbitrary grating amplitude. The\nrevision's full run of the entry was killed at the 2-hour command limit with\nno notebook written, so the code went back to the verified version and the\nreplies were made in text; a vectorized BRS fit, tried outside the notebook on\ntwo S1 sessions, was lost with its temporary folder. That revision also put\ntwo questions on the noise ceiling to a reader in `questions/kay-2008.yaml`,\nafter the answer and author-answers runs had found no questions and changed\nnothing. Round 2 asked that the paper's luminance reading be run, the strict\nreceptive-field filter applied, the V4 margin checked under other seeds and a\nGaussian fitted to the Figure 2 envelope, and found the record's time\nestimates (605 and 172 minutes) did not match the notebook (581 and 161); all\nwere run, with no outcome changed, and the paper's luminance reading became\nthe main result. The author's run used about 2 h 40 min; the notebook took 39\nmin with peak memory 8.6 GB at first and 106 min in the last run, after which\nthe conclusions were written into the executed copy without a second run.\nBetween runs at fixed seeds some numbers moved (O1b-O5a gave 110 and 87 where\nit gave 109 and 86), with no outcome changed.\n\nThe data set holds the two subjects' five main sessions only: the two later\nS1 sessions, the session about 14 months later, the 999-image library and the\nmultifocal retinotopic mapping scans are not in it (the readme says the\nlocalizer scans are not included), so seven of the paper's findings cannot be\ntested. It gives the repeated-trial response estimates without standard\nerrors and no single-trial estimates, so the SNR of Supplementary Table 1 and\nthe single-trial results of Figure 4a can be had only by refitting the BRS\nmodel to every voxel's time series; the 70 raw runs are on the archive. 345 V1\nto V3 voxels of S1 and 214 of S2 (and 15 S1 V4 voxels) have NaN responses in\nEstimatedResponses.mat, which the readme does not mention. The readme calls\nthe .mat files MATLAB 7.3 (HDF5) files, but Stimuli.mat and mask.mat are\nMATLAB 5 files, which h5py and PyTables cannot open, and it gives\nStimuli_Trn_FullRes_15.mat as 70 x 120 x 120 where it holds 70 images of 500 x\n500. It does not say whether voxIdx is 0-based or 1-based or how it relates to\nthe paper's voxel numbers (voxIdx holds 42205 for one S1 V1 voxel), and the\nNIfTI headers give a TR of 0. The identification runs hold 13, 14 or 15\npresentations per image, where the claims file says 13 or 14. In the paper,\nthe rule for the final model's field of view, which decides identification\nhere, is not given; nor whether the tuning curves include the DC offset, are\nrestricted to the aperture or combine voxels with different fields of view;\nnor whether the stimulus bounds of Supplementary Figure 11 are the 20 degree\nsquare or the circular aperture. These three are put to the paper's authors.\nThe paper also gives initial fields of view of 10.1 and 5.2 degrees, where its\nresolution list gives 10.0 and 5.12, and an orientation bandwidth of 41\ndegrees, where a 1-octave bandwidth gives about 37.\n\nThe author's points on the protocol: running every combination of readings\nthe claims file asks for roughly doubled the runtime (21 to 39 min), over the\n10-minute aim; a claim that depends on a blocked claim is blocked even when\npart of it can be tested; `too_large` estimates need numbers, which may not\ncome from analyses outside the notebook, so timing cells were put in it; a\nstandard choice, whether tuning curves include the DC offset, decided an\noutcome and was treated as an assumption; archives.md expects zips, but vim-1\nholds plain `.mat` files and gzipped NIfTI, which cannot be range-read and\nwere read whole into memory; and the data check's shared-clock requirement\ndoes not fit per-image estimates, so predictive power with the image order\nshuffled was used as the contrast.\n"
}
```

```
File created successfully at: docs/pilot-notes/kay-2008-01.md (file state is current in your context — no need to Read it back)
```

**Agent calls Write**

```json
{
 "file_path": "summaries/kay-2008-01.md",
 "content": "The paper's central result, that the natural image a person saw can be identified among new images from V1 to V3 fMRI activity with a receptive-field model, holds up in this data for both subjects (90.8% and 72.5% correct), but only under one rule for the model's field of view, which the paper does not describe. Its other main findings could not be tested: identification from single trials needs a refit of every voxel's time series that was too large for the run, and identification among about 1,000 images or months later needs images and sessions that are not in the dataset. The example voxel of Figure 2 reproduces only in part. Among the minor claims, the voxel counts, the fall in predictive power from V1 to V3 and errors on similar images reproduce, while the band-pass V1 tuning, a classification control and the V1 share of selected voxels do not.\n"
}
```

```
File created successfully at: summaries/kay-2008-01.md (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "summaries/kay-2008-01.md",
 "old_string": "identification among about 1,000 images or months later needs images and sessions",
 "new_string": "identification among a far larger image set or months later needs images and sessions"
}
```

```
The file summaries/kay-2008-01.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
wc -w summaries/kay-2008-01.md; grep -c "—\|rather" summaries/kay-2008-01.md docs/pilot-notes/kay-2008-01.md; git status --short
```

```
153 summaries/kay-2008-01.md
summaries/kay-2008-01.md:0
docs/pilot-notes/kay-2008-01.md:0
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
?? docs/pilot-notes/kay-2008-01.md
?? scripts
?? summaries/kay-2008-01.md
```

**Agent**

The summary is 153 words, over the 120 limit, so I'm cutting it down.

**Agent calls Write**

```json
{
 "file_path": "summaries/kay-2008-01.md",
 "content": "The central result, identifying which new natural image a person saw from V1 to V3 fMRI activity with a receptive-field model, holds up for both subjects (90.8% and 72.5% correct), but only under a field-of-view rule the paper does not describe. The other main findings could not be tested: single-trial identification needs a refit of every voxel's time series too large for the run, and the larger image sets and later sessions are not in the dataset. The example voxel of Figure 2 reproduces in part. Among minor claims, voxel counts, the fall in predictive power from V1 to V3 and errors on similar images reproduce; the band-pass V1 tuning, a classification control and the V1 share of selected voxels do not.\n"
}
```

```
The file summaries/kay-2008-01.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
wc -w summaries/kay-2008-01.md
```

```
122 summaries/kay-2008-01.md
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "summaries/kay-2008-01.md",
 "old_string": "The central result, identifying which new natural image a person saw from V1 to V3 fMRI activity with a receptive-field model, holds up",
 "new_string": "The central result, identifying which new natural image a person saw from fMRI activity with a receptive-field model, holds up"
}
```

```
The file summaries/kay-2008-01.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
wc -w summaries/kay-2008-01.md
```

```
119 summaries/kay-2008-01.md
```

**Agent**

I wrote both files and didn't commit anything. `targets/dandisets.json` has no entry for CRCNS vim-1, so there is no `catalystneuro` field and the notes don't mention a conversion. The summary is 119 words. Untracked dotfiles and a `scripts/` folder were already in the working tree when I started; I didn't create them and left them alone.

`docs/pilot-notes/kay-2008-01.md`:

# kay-2008, Kay et al. 2008

Seven claims reproduced, three partially, three not reproduced and six blocked, plus four blocked that also need the paper's 999-image library (`with_inputs`); three outcomes, `fig2-representative-voxel`, `suppfig11-rf-size-eccentricity` and `supptable1-predictive-power-by-area`, rest on an assumption. The first verification round agreed with 21 of the 23 outcomes as they stood and the second with all 23; nothing was proposed after the second, so there was no third round. CRCNS data sets carry no version, so the record gives `unversioned` with doi:10.6080/K0QN64NG and the notebook prints the MD5 sums from the bucket. The paper, Kay, Naselaris, Prenger and Gallant, "Identifying natural images from human brain activity" (Nature 452:352-355), fits a Gabor wavelet pyramid (GWP) receptive-field model to each fMRI voxel of V1 to V3 in two subjects from their responses to 1,750 natural images, and identifies which of 120 new images a subject saw from the predicted activity patterns. The claims were written from the version of record with its supplement; the paper links no analysis code. Reproduced are identification at set size 120 with repeated trials (109 of 120 for S1, paper 110, and 87 of 120 for S2, paper 86), the retinotopy-only model at set size 120 (52.1% and 43.3%, below the GWP model), errors falling on images similar in local contrast (p = 0.00031; not with pixel luminance), the six voxel counts of Supplementary Table 1 (exact), the fall of predictive power from V1 to V3, and the poor fit in V4 (the S1 margin is 0.7 points, and V4 stays below V3 under two other seeds). The identification results hold only with the final model's field of view set to the +/-2 SD square of the fitted Gaussian; with the best initial model's field of view they are 75.8% and 46.7%. Partial are the example voxel of Figure 2 (left hemifield and high-pass hold; under the adopted reading the envelope peaks 0.24 degrees above the horizontal meridian and the orientation tuning is not broadband), the best voxel count of about 500 (it holds for repeated trials, and the single-trial conditions are blocked) and receptive-field size against eccentricity (size rises with eccentricity, but V1 < V2 < V3 holds in 2 of 5 shared 1 degree bins). Not reproduced are the band-pass V1 spatial frequency tuning of Supplementary Figure 7 (high-pass in every reading run), the classification-extension control (S2's contrast metric gives 1 or 2 of 120, against 7) and most selected voxels lying in V1 (48%). Blocked as too large are the single-trial identification, the noise ceilings and the SNR, which need the BRS model refitted to every voxel's time series; blocked for missing data are the set-size, extrapolation and constrained-model claims, the two later S1 sessions and the check against retinotopic mapping. The author's first run gave 8 reproduced, 1 partially, 3 not reproduced and 11 blocked. Round 1 moved `suppfig4-500-voxels` from blocked to partially reproduced, since its repeated-trial conditions already met the rule, and `suppfig11-rf-size-eccentricity` from reproduced to partially reproduced, as Figure 2's legend calls the circle the bounds of the stimulus; it also found the too-large estimates overstated, the luminance channel of the retinotopy-only model taken relative to the grey background, voxels with NaN responses counted as not significant without saying so, and tuning ratios with the DC offset that depend on an arbitrary grating amplitude. The revision's full run of the entry was killed at the 2-hour command limit with no notebook written, so the code went back to the verified version and the replies were made in text; a vectorized BRS fit, tried outside the notebook on two S1 sessions, was lost with its temporary folder. That revision also put two questions on the noise ceiling to a reader in `questions/kay-2008.yaml`, after the answer and author-answers runs had found no questions and changed nothing. Round 2 asked that the paper's luminance reading be run, the strict receptive-field filter applied, the V4 margin checked under other seeds and a Gaussian fitted to the Figure 2 envelope, and found the record's time estimates (605 and 172 minutes) did not match the notebook (581 and 161); all were run, with no outcome changed, and the paper's luminance reading became the main result. The author's run used about 2 h 40 min; the notebook took 39 min with peak memory 8.6 GB at first and 106 min in the last run, after which the conclusions were written into the executed copy without a second run. Between runs at fixed seeds some numbers moved (O1b-O5a gave 110 and 87 where it gave 109 and 86), with no outcome changed.

The data set holds the two subjects' five main sessions only: the two later S1 sessions, the session about 14 months later, the 999-image library and the multifocal retinotopic mapping scans are not in it (the readme says the localizer scans are not included), so seven of the paper's findings cannot be tested. It gives the repeated-trial response estimates without standard errors and no single-trial estimates, so the SNR of Supplementary Table 1 and the single-trial results of Figure 4a can be had only by refitting the BRS model to every voxel's time series; the 70 raw runs are on the archive. 345 V1 to V3 voxels of S1 and 214 of S2 (and 15 S1 V4 voxels) have NaN responses in EstimatedResponses.mat, which the readme does not mention. The readme calls the .mat files MATLAB 7.3 (HDF5) files, but Stimuli.mat and mask.mat are MATLAB 5 files, which h5py and PyTables cannot open, and it gives Stimuli_Trn_FullRes_15.mat as 70 x 120 x 120 where it holds 70 images of 500 x 500. It does not say whether voxIdx is 0-based or 1-based or how it relates to the paper's voxel numbers (voxIdx holds 42205 for one S1 V1 voxel), and the NIfTI headers give a TR of 0. The identification runs hold 13, 14 or 15 presentations per image, where the claims file says 13 or 14. In the paper, the rule for the final model's field of view, which decides identification here, is not given; nor whether the tuning curves include the DC offset, are restricted to the aperture or combine voxels with different fields of view; nor whether the stimulus bounds of Supplementary Figure 11 are the 20 degree square or the circular aperture. These three are put to the paper's authors. The paper also gives initial fields of view of 10.1 and 5.2 degrees, where its resolution list gives 10.0 and 5.12, and an orientation bandwidth of 41 degrees, where a 1-octave bandwidth gives about 37.

The author's points on the protocol: running every combination of readings the claims file asks for roughly doubled the runtime (21 to 39 min), over the 10-minute aim; a claim that depends on a blocked claim is blocked even when part of it can be tested; `too_large` estimates need numbers, which may not come from analyses outside the notebook, so timing cells were put in it; a standard choice, whether tuning curves include the DC offset, decided an outcome and was treated as an assumption; archives.md expects zips, but vim-1 holds plain `.mat` files and gzipped NIfTI, which cannot be range-read and were read whole into memory; and the data check's shared-clock requirement does not fit per-image estimates, so predictive power with the image order shuffled was used as the contrast.

`summaries/kay-2008-01.md`:

The central result, identifying which new natural image a person saw from fMRI activity with a receptive-field model, holds up for both subjects (90.8% and 72.5% correct), but only under a field-of-view rule the paper does not describe. The other main findings could not be tested: single-trial identification needs a refit of every voxel's time series too large for the run, and the larger image sets and later sessions are not in the dataset. The example voxel of Figure 2 reproduces in part. Among minor claims, voxel counts, the fall in predictive power from V1 to V3 and errors on similar images reproduce; the band-pass V1 tuning, a classification control and the V1 share of selected voxels do not.

## End of run

18 turns, 2 minutes, $1.00 at API prices, result: success.
