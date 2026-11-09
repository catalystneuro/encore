# 000785 · claims · run 39890294913

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cat docs/protocol.md; ls claims/001453/ paper/ claims/000785 2>&1;
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
awk '/^## Reader/,/^## Author/' docs/protocol.md; ls claims/001453/ paper/ claims/000785 2>&1
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cat claims/001453/10.1016-j.cub.2025.04.027.yaml; wc paper/*.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.64898-2025.12.12.694045.txt"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.64898-2025.12.12.694045.txt",
 "offset": 119,
 "limit": 200
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.64898-2025.12.12.694045.txt",
 "offset": 318,
 "limit": 240
}
```

Result: not kept, because it reads the paper's text.

**Agent**

The text has main text, Methods and supplementary figure legends; the contents of Tables 2 to 8 are missing (headings only). Next I'll look at the linked GitLab repository.

**Agent calls Bash**

```bash
cd $TMPDIR && timeout 120 git clone --depth 50 https://gitlab.com/fleischmann-lab/calcium-imaging/projection-difference.git pd 2>&1 | tail -3; cd pd 2>/dev/null && git log -1 --format='%H %ci' && find . -type f -not -path './.git/*' | head -100
```

```
Cloning into 'pd'...
f478b34c79606c3109f259d24add0256fb0b3b67 2025-06-25 14:56:01 -0400
./src/nwb_processor.py
./requirements.txt
./notebooks/process-passive-dataset.ipynb
./notebooks/process-GNG-dataset.ipynb
./notebooks/demo-classify-projection.ipynb
./notebooks/construct-metadata-database.ipynb
./media/orc-criteria.svg
./media/orc-criteria.png
./media/muse-orc-pipeline.svg
./media/muse-orc-pipeline.png
./data/proc/.gitkeep
./data/dandi/.gitkeep
./data/README.md
./data/.gitignore
./config/preprocess.yml
./config/mpl.sty
./config/graphics.yml
./_toc.yml
[... 7 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/pd && cat README.md config/preprocess.yml data/README.md; wc -l src/nwb_processor.py; grep -n "def \|percentile\|median\|window\|zscore\|std" src/nwb_processor.py | head -80
```

```
<persisted-output>
Output too large (31.7KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/fd8571a8-7b94-4f75-9765-13dc25499037/tool-results/brot4woed.txt

Preview (first 2KB):
# Piriform Projection Differences

[[_TOC_]]

## Quick links

- Repository: <https://gitlab.com/fleischmann-lab/calcium-imaging/projection-difference>
- Static site (for better viewing of notebooks): <https://fleischmann-lab.gitlab.io/calcium-imaging/projection-difference>
- DANDI Archive (embargoed): <https://dandiarchive.org/dandiset/000785>


## Description

This repository is part of an ongoing research project in the Fleischmann lab at Brown University, led by Dr. Simon Daste.
The goal of the project is to analyze neural activity of different projection pyramidal neurons in the piriform cortex (PCx), specifically:

[... 35 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/pd && sed -n 40,400p README.md | cut -c1-300; echo ----; cat config/preprocess.yml
```

```
## Data & Access

The data are currently on [DANDI Archive](https://dandiarchive.org/) (embargoed) and will need an API key to download. 

If you have not been granted access, please create an account on DANDI Archive with your GitHub account and contact us with your email or GitHub username.

If this is your first time using `dandi` with an API key, it will likely prompt you to set up a keyring to store your API key.

For more information on access credentials, please see [DANDI Archive handbook](https://docs.dandiarchive.org/13_upload/#storing-access-credentials).


## Collaboration

### Color schemes

For consistency of visualization, please refer to `config/graphics.yml` file for the main colors.

#### Projection / population

This file defines the color schemes for the different **projection targets** / populations, specifically, colors related to:
[... 331 more lines not kept]
```

**Agent**

The repository holds data access and preprocessing only; the analysis code is "made available upon publication". Let me check the notebooks for the bad-trial rule and the normalization choice.

**Agent calls Bash**

```bash
cd $TMPDIR/pd && python3 - <<'EOF'
import json
for nb in ['notebooks/process-passive-dataset.ipynb','notebooks/process-GNG-dataset.ipynb','notebooks/demo-classify-projection.ipynb']:
    d=json.load(open(nb))
    print('=====',nb)
    for c in d['cells']:
        s=''.join(c['source'])
        if c['cell_type']=='markdown' or any(k in s for k in ['bad','percdFF','dff_type','compute_dFF0','method','min_3']):
            print('['+c['cell_type']+']',s[:1500]);print('--')
EOF
```

```
<persisted-output>
Output too large (51.1KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/fd8571a8-7b94-4f75-9765-13dc25499037/tool-results/ba5f2g0ne.txt

Preview (first 2KB):
===== notebooks/process-passive-dataset.ipynb
[markdown] # PASSIVE: Load and compute normalized fluorescence data for passive experiments 
--
[markdown] **Purpose**: This notebook demonstrates how to select for an experiment, loads the NWB files, computes the `dFF0` with different methods.

At the end, this also saves the data, or at least suggests how to save them.

**Prerequisite**: Before running this notebook, please follow the instructions in `README.md` to set up, download data, and run the `construct-metadata-database.ipynb` first.

This notebook assumes you have the downloaded dandiset in `data/dandi/000785` and a metadata CSV `data/database.csv`.

**Scope**: In this notebook please only use the **passive** datasets:

- `identity_dataset`
- `concentration_dataset`
- `fast_hz_sniff_trig_dataset` (hold off on this for now)
[... 24 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/pd && grep -n "bad_trial\|is_bad\|outlier\|percdFF\|dff_method\|norm_method\|DFF_METHOD\|min_3\|ORC_CRIT" -r notebooks src | cut -c1-260 | head -60
```

```
notebooks/process-passive-dataset.ipynb:189:    "- `percdFF0`: use a running percentile of fluorescence to estimate `F0` then do `(F - F0) / F0`\n",
notebooks/process-passive-dataset.ipynb:190:    "- `percdFF` (notice no `0` at the end): also use running percentile for `F0` but then do `dF = F - F0` to remove baseline shifts, then divide by the standard deviation of `dF`. So basically: `(F - F0) / std(F - 
notebooks/process-passive-dataset.ipynb:192:    "We recommend using either `zscore` or `percdFF` based on our experience."
notebooks/process-passive-dataset.ipynb:220:      "    percdFF0:\n",
notebooks/process-passive-dataset.ipynb:228:      "            tau_m: 1 # (unit = second) median filter to remove outliers first, keep `None` to avoid cropping off high calcium transients\n",
notebooks/process-passive-dataset.ipynb:231:      "    percdFF:\n",
notebooks/process-passive-dataset.ipynb:239:      "            tau_m: 1 # (unit = second) median filter to remove outliers first, keep `None` to avoid cropping off high calcium transients\n",
notebooks/process-passive-dataset.ipynb:287:    "2. Please change `norm_method_key` for different normalization methods (we recommend `percdFF`, `zscore`)\n",
notebooks/process-passive-dataset.ipynb:308:    "norm_method_key = \"percdFF\" # \"percdFF\", \"zscore\", \"percdFF0\""
notebooks/process-passive-dataset.ipynb:413:    "        **norm_sets[norm_method_key],\n",
notebooks/process-passive-dataset.ipynb:474:       "      <th>is_bad_trial</th>\n",
notebooks/process-passive-dataset.ipynb:781:       "        is_bad_trial stim_type projection             exp_id  \\\n",
notebooks/process-passive-dataset.ipynb:852:       "       'trial_id', 'is_bad_trial', 'stim_type', 'projection', 'exp_id', 't',\n",
notebooks/process-passive-dataset.ipynb:886:    "| `is_bad_trial` | bool | indicates whether the trial has very extreme outliers | all datasets | \n",
notebooks/process-passive-dataset.ipynb:938:    "1. Remove bad trials (indicated by `is
[... 46 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/pd && grep -n "bad\|def \|is_red\|iscell" src/nwb_processor.py | head -50; grep -n "GNG_2023b\|day_num.*4\|day 4\|<= 3\|isin(\[1" notebooks/process-GNG-dataset.ipynb | cut -c1-200 | head
```

```
20:def construct_muse_metadata(df):
37:        'cell_id', 'is_redcell', 'projection',
63:def __check_muse_persistence__(df):
94:def __codify_multi_session_list__(cdf):
103:        .astype({'day_num': 'int', 'is_redcell': 'int'})
105:        [['day_num', 'is_redcell']]
109:            'is_redcell': 'is_redcell_muse'
115:    # format e.g.: "0:<is_redcell_day_0>|1:<is_redcell_day_1>"
120:                x['is_redcell_muse']
141:def __determine_omni_criteria__(cdf):
153:    cdf['is_redcell__min_1_session'] = cdf['is_redcell_muse'].apply(sum) >= 1
154:    cdf['is_redcell__min_3_sessions'] = cdf['is_redcell_muse'].apply(sum) >= 3
157:    cdf['is_redcell__first_4_sessions'] = cdf['is_redcell_muse'].apply(lambda x: sum(x[:4]) == 4)
158:    cdf['is_redcell__all_sessions'] = cdf['is_redcell_muse'].apply(sum) == cdf['max_sessions']
161:    for rc_col in cdf.filter(regex='is_redcell__').columns:
179:def summarize_task_outcome(nwb):
230:def gather_metadata(file_path):
260:        total_iscells = nwb.processing['ophys']['ImageSegmentation']['PlaneSegmentation']['iscell'].data[:,0].sum().astype(int)
263:        num_bad_trials = sum(nwb.trials.is_bad_trial.data[:])
285:            total_is_cells = total_iscells,
[... 41 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/pd && python3 -c "
import json
d=json.load(open('notebooks/demo-classify-projection.ipynb'))
for c in d['cells']:
    s=''.join(c['source'])
    print('['+c['cell_type']+']',s[:700]);print('--')
" | head -120; sed -n 988,1046p src/nwb_processor.py
```

```
[markdown] # Demonstration of projection prediction using SVM on averaged odor activity
--
[markdown] **Purpose**: This notebook demonstrates how to decode projection target based on averaged fluorescence activity per odor.

This can serve as a baseline to compare with more complicated models, such as a neural network or transformer models (e.g. GAFormer) 
that can take into account all trials and time points at the same time, or even further about stimulus or trial metadata.

**Prerequisite**: This notebook assumes the following notebooks are already run:
- [`process-passive-dataset.ipynb`](process-passive-dataset.ipynb)
- [`process-GNG-dataset.ipynb`](process-GNG-dataset.ipynb)

And it assumes the processed data files have already been time-aligned and saved.

The notebook assumes the proc
--
[markdown] ## 1. Import package & define paths
--
[markdown] ### 1.1. Import packages
--
[code] import os
[... 158 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 1,80p tools/claims_check.py; ls tools schema* docs 2>/dev/null | head -40
```

```
"""Check a claims file against the full text of its paper.

    python tools/claims_check.py claims/<dandiset>/<doi>.yaml paper/<text>.txt [more texts ...]

Validates the file against schemas/claims.schema.json, checks every quote word for word
(fragments split on "...", found in order) and looks for every recorded p-value and
confidence-interval bound in the text. The text may be plain text, HTML or JATS XML; several
files (a paper and its supplement) are searched together. A value printed in a form the
checker does not know (a garbled PDF glyph, "p = 0.04, 0.05 and 0.16") is reported, to be
confirmed by reading. Exits non-zero on any problem.
"""

from __future__ import annotations

import html
import re
import sys
import unicodedata
from pathlib import Path

[... 100 more lines not kept]
```

**Agent calls Bash**

```bash
python3 -c "
import json;d=json.load(open('schemas/claims.schema.json'));print(json.dumps(d,indent=1)[:9000])"
```

```
{
 "$schema": "https://json-schema.org/draft/2020-12/schema",
 "title": "Claims proposed for one target (a dataset and one of its papers)",
 "description": "Draft. To be revised after the pilot.",
 "type": "object",
 "additionalProperties": false,
 "required": [
  "schema_version",
  "dataset",
  "paper",
  "claims"
 ],
 "properties": {
  "schema_version": {
   "const": 2
  },
  "dataset": {
   "description": "The dataset the claims are tested on: the archive and the dataset's identifier there.",
   "type": "object",
   "additionalProperties": false,
[... 326 more lines not kept]
```

**Agent**

Code read. The repository (commit f478b34) holds NWB loading and preprocessing plus a demo SVM notebook, but no figure analyses. Let me check which SVM class the demo uses.

**Agent calls Bash**

```bash
cd $TMPDIR/pd && grep -n "svm\.\|StandardScaler\|cross_val\|KFold\|n_splits\|cv=" notebooks/demo-classify-projection.ipynb | cut -c1-200 | head -20
```

```
1103:    "model_selection.cross_val_score(\n",
1104:    "    estimator = svm.SVC(kernel='linear'), \n",
1106:    "    cv = model_selection.RepeatedStratifiedKFold()\n",
1136:    "model_selection.cross_val_score(\n",
1139:    "    cv = model_selection.RepeatedStratifiedKFold()\n",
1247:    "    estimator = svm.SVC(kernel='linear'),\n",
1269:       "sklearn.model_selection._split.StratifiedGroupKFold"
1283:    "model_selection.StratifiedGroupKFold"
1302:    "This can be improved with better stratification / class imbalance checks in `classify_with_groups` function or `sklearn.StratifiedGroupKFold` (though this does not seem to generate all satis
1889:    "    'SVM | no-group-split': model_selection.cross_val_score(estimator = svm.SVC(kernel='linear'), X = X, y = y, cv = model_selection.RepeatedStratifiedKFold()).mean(),\n",
1890:    "    'dummy | no-group-split': model_selection.cross_val_score(estimator = dummy.DummyClassifier(), X = X, y = y, cv = model_selection.RepeatedStratifiedKFold()).mean(),\n",
1891:    "    'SVM | group-split': classify_with_groups(estimator = svm.SVC(kernel='linear'), X = X, y = y, g = g).mean(),\n",
1982:    "            scores = model_selection.cross_val_score(\n",
2339:    "    'SVM': svm.SVC(kernel='linear'),\n",
2344:    "cv = model_selection.RepeatedStratifiedKFold(\n",
2345:    "    n_splits=4, n_repeats=10, \n",
Shell cwd was reset to
```

**Agent**

I'm writing the claims file now. It has about 33 claims, and shared method details go in the opening comment.

**Agent calls Write**

```json
{
 "file_path": "claims/000785/10.64898-2025.12.12.694045.yaml",
 "content": "# Claims for Daste, Pierré et al., \"Projection-specific Routing of Odor Information in the\n# Olfactory Cortex\" (bioRxiv preprint doi:10.64898/2025.12.12.694045) on dandiset 000785.\n# Written by an agent (model \"claude-opus-5-5\", Claude Code in GitHub Actions), 2026-10-23,\n# protocol pilot-10 as stated in docs/protocol.md.\n#\n# Text read. The bioRxiv preprint, version 1, flattened from its JATS XML (paper/\n# 10.64898-2025.12.12.694045.txt). It holds the main text, the Methods and the legends of the\n# supplementary figures S1 to S13. No PDF was supplied. The contents of Tables 2 to 8 are\n# missing from the text (only their titles remain): the odorants and concentrations of each\n# dataset (Tables 2, 3, 4), the transformer hyperparameters (Table 5), the animal pairs held\n# out for across-animal evaluation (Table 6) and the MLP search space and final\n# hyperparameters (Tables 7, 8). The equations for normalized fluorescence, lifetime\n# sparseness, population sparseness and mutual information are also lost in the flattening\n# (the text keeps the words around them).\n#\n# Code read. The paper links https://gitlab.com/fleischmann-lab/calcium-imaging/projection-difference\n# (commit f478b34c79606c3109f259d24add0256fb0b3b67, 2025-06-25). It holds the loading and\n# preprocessing of the dandiset's NWB files (src/nwb_processor.py, notebooks process-passive-\n# dataset, process-GNG-dataset, construct-metadata-database) and a demo notebook that decodes\n# projection target with an SVM. The figure analyses are not in it; the paper says the\n# analysis code \"will be made available ... upon publication\". Choices the code settles, and\n# that are used below, are (1) normalized fluorescence is the code's \"percdFF\", F median-\n# filtered over 1 s, F0 the running 10th percentile of that over 30 s, and (F - F0) divided by\n# the standard deviation of (F - F0) over the session, per cell, no neuropil correction\n# (k_neu 0), suite2p iscell cells only; (2) bad trials are those flagged in the NWB trials\n# column is_bad_trial, and are removed with control trials (mineral oil, air) before\n# pseudo-populations are built; (3) for tracked Go/NoGo neurons a cell is OB-p or mPFC-p when\n# it is tracked across all four sessions (day 0 passive and task days 1 to 3) and red in at\n# least 3 of them (code criterion min_3_sessions, matching the Methods' \"at least 3 out of 4\n# days\"); (4) the linear SVM is sklearn.svm.SVC(kernel='linear') with default parameters, as\n# in the demo notebook (the Methods say \"a linear SVM with all default parameters as given by\n# sklearn\"; sklearn.svm.LinearSVC is shown as a variant). In the GNG_2023b dataset the code\n# ignores task day 4, to match the 3 task days of GNG_2021.\n#\n# Data the paper used. Ai14 mice with jGCaMP7f in anterior piriform cortex (aPCx) and\n# retrograde AAV-Cre in the olfactory bulb (OB-p mice) or infralimbic/prelimbic mPFC (mPFC-p\n# mice), two-photon imaging through a GRIN lens. tdTomato-positive cells are OB-p or mPFC-p\n# by the mouse's injection; GCaMP-only cells are untagged. Four experiments, which the code\n# names identity_dataset, concentration_dataset, fast_hz_sniff_trig_dataset and the Go/NoGo\n# datasets GNG_2021_dataset and GNG_2023b_dataset.\n#   - Identity (passive): 10 mice, 8 monomolecular odorants at one concentration plus 2\n#     controls, 8 to 10 presentations each, 22 s trials (5 s baseline, 2 s odor, 15 s after),\n#     3 planes at 4.53 Hz per plane; 81 OB-p, 84 mPFC-p and 1978 untagged neurons.\n#   - Concentration (passive): 10 mice, 3 odorants (acetophenone, butyl acetate, ethyl\n#     hexanoate) at 3 concentrations plus a control; 87 OB-p, 102 mPFC-p, 2232 untagged.\n#   - Fast (passive, 30 Hz, one plane, odor aligned to the first sniff): 5 mice, 24 OB-p, 27\n#     mPFC-p, 424 untagged. The code's README marks this dataset \"may need revisiting, don't\n#     use for now\".\n#   - Go/NoGo: 7 mice (4 OB-p, 3 mPFC-p), a passive day 0 then task days 1 to 3, 4 odors (CS+1,\n#     CS+2 rewarded, CS-1, CS-2 not), trials of 5 s baseline, 2 s odor, 3 s delay, then the\n#     reward window; licks, reward times and trial outcomes (hit, miss, false alarm, correct\n#     rejection). Per session 95 +/- 2 OB-p, 87 +/- 8 mPFC-p and 1690 +/- 35 untagged neurons.\n#     Tracked across days with ROICaT and manual refinement (the NWB field\n#     subject_global_roi_muse, renamed muse_cell_id in the code); 46 OB-p and 41 mPFC-p\n#     tracked projection neurons.\n# The Methods count 18 mice (9 OB-p, 8 mPFC-p, which sum to 17) and 16 in passive sessions,\n# while Figure S2B has N = 9 OB-p and 10 mPFC-p mice; the counts are not consistent.\n#\n# Methods shared by many claims, from the Methods unless said otherwise.\n#   - Active (binarized) response on a trial. Null distribution of 1000 values sampled from\n#     the normalized trace in the 4 s before odor onset, across all trials. A forward sliding\n#     one-sided Mann-Whitney U test (window 0.7 s) of the response window against it; active if\n#     p < 0.01 for at least 8 consecutive forward frames and (for windows starting at odor\n#     onset) not backward-active (p < 0.01 for any of 4 consecutive backward frames). Response\n#     window 0 to 5 s after odor onset for the passive datasets, each task phase for Go/NoGo.\n#     Open details, which could change the outcome. Whether the 0.7 s window is anchored at\n#     its start or centred on each frame, and whether the backward test slides into the\n#     baseline from odor onset; the readings are (a) windows starting at each frame and\n#     extending 0.7 s forward (backward windows ending at each of the 4 frames before onset)\n#     and (b) windows centred on each frame. The 1000-point sample is random (a seed; a\n#     standard choice).\n#   - Lifetime sparseness, population sparseness and mutual information. The formulas are\n#     lost from the text. Readings: lifetime sparseness as in Vinje and Gallant (2000),\n#     S = (1 - (sum r / k)^2 / (sum r^2 / k)) / (1 - 1/k) over the k stimuli of a cell's trial-\n#     averaged binarized activity r; population sparseness the same over the N cells of a\n#     group for one stimulus or one trial; mutual information I(X; S) = H(X) - H(X | S)\n#     between a cell's binary activity and the stimulus, in bits, from empirical frequencies.\n#   - Pseudo-populations. Cells pooled across mice within a group; trials matched across mice\n#     by stimulus and by the order of presentation of that stimulus. Trials per stimulus are\n#     truncated to the smallest count across mice (implied by the matching; the 64 trials of\n#     Figure 2D are 8 odors by 8 trials). Size-matched subsamples drawn without replacement\n#     (75 cells for the passive data, 85 for Go/NoGo) and repeated (100 or 200 times). The\n#     response of a cell in a window is \"either the average or maximum\" of normalized\n#     fluorescence; the Methods name the mean for the identity and concentration decoders,\n#     and give no aggregate for Go/NoGo, so Go/NoGo decoding is run with the mean (a) and the\n#     maximum (b). Folds are 5-fold cross-validation for the passive datasets; no fold scheme\n#     is given for Go/NoGo, read as 5-fold stratified cross-validation as for the passive data,\n#     with train and test never on the same trial (Methods, Decoding analysis).\n#   - Go/NoGo task phases, relative to odor onset. Odor 0 to 2 s, delay 2 to 5 s, act-early 5\n#     to 10 s, act-late 10 to 15 s. Go trials count as hits only if the reward came within 10 s\n#     after the delay. Decoding is done per task day; expert means day 3.\n#   - Statistics. Bonferroni correction for most analyses, Benjamini-Hochberg for single-cell\n#     properties of tracked neurons; the significance level is 0.05.\nschema_version: 2\ndataset:\n  archive: dandi\n  id: \"000785\"\npaper: doi:10.64898/2025.12.12.694045\nclaims:\n- id: dataset-neuron-counts\n  statement: The passive identity dataset holds 81 OB-p, 84 mPFC-p and 1978 untagged neurons\n    from 10 mice; the concentration dataset 87 OB-p, 102 mPFC-p and 2232 untagged neurons from\n    10 mice; the Go/NoGo dataset 7 mice (4 OB-p, 3 mPFC-p tagged) with, per session, 95 +/- 2\n    OB-p, 87 +/- 8 mPFC-p and 1690 +/- 35 untagged neurons.\n  source: Results, Calcium imaging of piriform neurons with distinct projection targets,\n    paragraph 2\n  quote: head-fixed mice were either exposed to 8 monomolecular odorants at a single\n    concentration (10 mice, totaling 81 OB-p, 84 mPFC-p, and 1978 untagged aPCx neurons ... or to\n    three odorants at three concentrations each (10 mice, totaling 87 OB-p, 102 mPFC-p, and 2232\n    untagged cells ... Per session (mean ± SD), we recorded 95 ± 2 OB-p, 87 ± 8 mPFC-p, and 1690\n    ± 35 untagged neurons\n  expected:\n  - quantity: identity dataset OB-p neurons\n    value: 81\n    tolerance: 8.1\n  - quantity: identity dataset mPFC-p neurons\n    value: 84\n    tolerance: 8.4\n  - quantity: identity dataset untagged neurons\n    value: 1978\n    tolerance: 197.8\n  - quantity: concentration dataset OB-p neurons\n    value: 87\n    tolerance: 8.7\n  - quantity: concentration dataset mPFC-p neurons\n    value: 102\n    tolerance: 10.2\n  - quantity: concentration dataset untagged neurons\n    value: 2232\n    tolerance: 223.2\n  - quantity: Go/NoGo OB-p neurons per session, mean\n    value: 95\n    tolerance: 2\n  - quantity: Go/NoGo mPFC-p neurons per session, mean\n    value: 87\n    tolerance: 8\n  - quantity: Go/NoGo untagged neurons per session, mean\n    value: 1690\n    tolerance: 35\n  criterion: Counts of suite2p cells (iscell) by tag, per experiment, as the code's\n    load_experiment builds them. The Go/NoGo tolerances are the paper's SD. \"Per session\" is\n    read as (a) the total over all mice of one task day, averaged over task days 1 to 3, or (b)\n    the same over days 0 to 3; for OB-p and mPFC-p, only the mice tagged for that target count.\n    Reproduced when all values are within tolerance under one reading; partially reproduced\n    when the identity and concentration counts are and the Go/NoGo counts are not.\n- id: fast-dataset-counts\n  statement: The 30 Hz subset holds 24 OB-p, 27 mPFC-p and 424 untagged neurons from 5 mice.\n  source: Results, OB-p and mPFC-p neurons exhibit broadly similar odor response properties,\n    but differ in dynamics, paragraph 3\n  quote: in a subset of experiments (5 mice, totaling 24 OB-p, 27 mPFC-p, and 424 untagged\n    cells), we examined the temporal structure of odor responses by performing high-speed (30\n    Hz) imaging\n  expected:\n  - quantity: OB-p neurons\n    value: 24\n    tolerance: 2.4\n  - quantity: mPFC-p neurons\n    value: 27\n    tolerance: 2.7\n  - quantity: untagged neurons\n    value: 424\n    tolerance: 42.4\n  - quantity: mice\n    value: 5\n    tolerance: 0\n- id: figs2b-labeling-similar\n  statement: OB-p and mPFC-p mice do not differ in the number of jGCaMP7f neurons or of co-\n    labeled jGCaMP7f/tdTomato neurons.\n  source: Figure S2B legend\n  quote: Quantification of jGCaMP7f and co-labeled jGCaMP7f/tdTomato-expressing neurons in\n    OB-p and mPFC-p mice. (OB-p, N = 9; mPFC-p, N = 10. Unpaired two-tailed t-test\n  statistics:\n  - about: jGCaMP7f neurons per mouse\n    test: unpaired two-tailed t-test\n    p: 0.555\n    n: 9 OB-p and 10 mPFC-p mice\n  - about: co-labeled neurons per mouse\n    test: unpaired two-tailed t-test\n    p: 0.455\n    n: 9 OB-p and 10 mPFC-p mice\n  criterion: A claim of absence, judged on the paper's test. Per mouse, the number of suite2p\n    cells and of red (tdTomato-tagged) cells, with an unpaired two-tailed Student t-test of\n    OB-p against mPFC-p mice for each count. The legend does not say which session gives a\n    mouse's count when a mouse was imaged more than once; readings are (a) each mouse's first\n    imaging session and (b) its mean over sessions. Reproduced when neither test has p < 0.05\n    under the readings; not reproduced when either has p < 0.05 under all readings. The mouse\n    counts per group are reported against 9 and 10.\n- id: mlp-projection-f1\n  statement: An MLP trained on normalized fluorescence traces pooled across the identity and\n    Go/NoGo datasets classifies OB-p against mPFC-p neurons with F1 scores of 0.688 (OB-p) and\n    0.557 (mPFC-p).\n  source: Results, Temporal structure of activity predicts OB-p vs mPFC-p identity, paragraph 1\n  quote: The MLP achieved F1 scores of 0.688 (OB-p) and 0.557 (mPFC-p)\n  expected:\n  - quantity: F1, OB-p\n    value: 0.688\n    tolerance: 0.0688\n  - quantity: F1, mPFC-p\n    value: 0.557\n    tolerance: 0.0557\n  criterion: Inputs as for the transformer (Methods, Preprocessing), trials from 1 s before to\n    15 s after odor onset (70 frames), L = 5 subsamples of M = 20 trials per neuron, the\n    identity passive and Go/NoGo datasets, within-animal split 0.8/0.1/0.1 of neurons, averaged\n    over the seeds 0, 1, 2, 3, 4, 42, 43, 44, 45, 46. The MLP's architecture and training\n    hyperparameters are in Table 8, which is missing from the text; until it is supplied the\n    claim is blocked as methods_underspecified. Whether untagged neurons are a third class in\n    training (Figure 1F colors them) is open; readings are (a) two classes, OB-p and mPFC-p\n    only, and (b) three classes, with F1 reported for OB-p and mPFC-p.\n- id: transformer-projection-f1\n  statement: A transformer classifier on single-neuron calcium traces decodes projection\n    target with F1 0.759 (OB-p) and 0.744 (mPFC-p) when neurons from all animals are split,\n    and 0.754 (OB-p) and 0.623 (mPFC-p) when one OB-p and one mPFC-p animal are held out.\n  source: Results, Temporal structure of activity predicts OB-p vs mPFC-p identity, paragraph\n    1; Figure S3B\n  quote: which improved test performance to 0.759 (OB-p) and 0.744 (mPFC-p) ( Figure S3B ) ...\n    Performance remained high (F1 0.754 OB-p; 0.623 mPFC-p)\n  expected:\n  - quantity: F1 within-animal, OB-p\n    value: 0.759\n    tolerance: 0.0759\n  - quantity: F1 within-animal, mPFC-p\n    value: 0.744\n    tolerance: 0.0744\n  - quantity: F1 across-animal, OB-p\n    value: 0.754\n    tolerance: 0.0754\n  - quantity: F1 across-animal, mPFC-p\n    value: 0.623\n    tolerance: 0.0623\n  criterion: As in the Methods (Projection decoding analysis with a transformer model).\n    Identity passive and Go/NoGo datasets; trials from 1 s before to 15 s after odor onset (70\n    frames); L = 5 subsamples of M = 20 trials per neuron; patches of 2 frames embedded in 128\n    dimensions; a ViT encoder with a class token; trial latents average-pooled; majority vote\n    over subsamples; Adam with cosine decay. Within-animal split 0.8/0.1/0.1 over seeds 0, 1,\n    2, 3, 4, 42, 43, 44, 45, 46; across-animal over 6 held-out OB-p/mPFC-p pairs (Table 6) with\n    seeds 42, 43, 44. The depth, heads, learning rate, epochs and batch size (Table 5) and the\n    held-out pairs (Table 6) are missing from the text; until they are supplied the claim is\n    blocked as methods_underspecified. Classes as in mlp-projection-f1 (readings a and b).\n- id: fig1g-attention-timing\n  statement: Attention rollout on correctly classified neurons puts the informative epochs\n    early after odor onset (about 0 to 3 s) for OB-p neurons and later in the trial for mPFC-p\n    neurons.\n  source: Results, Temporal structure of activity predicts OB-p vs mPFC-p identity, paragraph\n    2; Figure 1G and Figure S3D\n  quote: informative epochs cluster early after odor onset (around 0-3 s) for OB-p neurons, but\n    later in the trial for mPFC-p neurons\n  depends_on:\n  - transformer-projection-f1\n  criterion: From the transformer of transformer-projection-f1, attention rollout (Abnar and\n    Zuidema 2020) of the class token over patches, averaged over trials per correctly\n    classified subsample, averaged over 10 seeds, OB-p minus mPFC-p (Figure 1G legend), on the\n    identity dataset. Reproduced when the difference is positive over most of 0 to 3 s after\n    odor onset and negative over most of the time after 3 s. Blocked with the transformer\n    while Table 5 is missing.\n- id: fig1f-latent-separation\n  statement: The transformer's penultimate-layer embeddings separate OB-p from mPFC-p neurons,\n    with little clustering by animal or dataset.\n  source: Results, Temporal structure of activity predicts OB-p vs mPFC-p identity, paragraph\n    2; Figure 1F and Figure S3E to S3G\n  quote: which separated OB-p and mPFC-p well with minimal clustering by animal or dataset\n  depends_on:\n  - transformer-projection-f1\n  criterion: The paper shows PCA plots and gives no measure of separation, so the claim can be\n    judged only by inspecting the same plots (PCA of neuron embeddings, seed 42, colored by\n    label, animal and dataset). It is blocked with the transformer while Table 5 is missing;\n    if run, it is reported as plots without an outcome beyond what they show.\n- id: fig2b-lifetime-sparseness-similar\n  statement: Lifetime sparseness does not differ significantly between OB-p, mPFC-p and\n    untagged neurons in the identity dataset.\n  source: Results, OB-p and mPFC-p neurons exhibit broadly similar odor response properties,\n    but differ in dynamics, paragraph 3; Figure 2B\n  quote: Odor responses in PCx were generally sparse on the single cell level, with no\n    significant differences in lifetime sparseness between groups\n  criterion: A claim of absence. Per neuron, lifetime sparseness over the 8 odors of its trial-\n    averaged binarized activity (0 to 5 s window), 81 OB-p, 84 mPFC-p and 1978 untagged\n    neurons. The text names no test here; the test the paper uses for the other single-cell\n    comparisons of Figure 2 is the two-sided Mann-Whitney U test with Bonferroni correction,\n    taken here over the 3 pairs. Reproduced when no pair has corrected p < 0.05; not\n    reproduced when any does. Medians are reported.\n- id: fig2c-mutual-information\n  statement: Mutual information between binarized activity and odor identity does not differ\n    between OB-p and mPFC-p neurons, but is lower for OB-p than untagged neurons (p = 0.012).\n  source: Results, OB-p and mPFC-p neurons exhibit broadly similar odor response properties,\n    but differ in dynamics, paragraph 3; Figure 2C\n  quote: Mutual information did not differ significantly between projection sub-populations,\n    but was lower for OB-p neurons than for untagged neurons (p = 0.012)\n  statistics:\n  - about: OB-p against untagged\n    test: not named; two-sided Mann-Whitney U with Bonferroni correction is the test of the\n      other Figure 2 comparisons\n    p: 0.012\n    corrected: Bonferroni (presumed)\n    n: 81 OB-p and 1978 untagged neurons\n  criterion: Per neuron, mutual information between its binary activity per trial (0 to 5 s\n    window) and the odor (8 odors). Two-sided Mann-Whitney U tests with Bonferroni correction\n    over the 3 pairs. Reproduced when OB-p against mPFC-p has corrected p >= 0.05 and OB-p is\n    lower than untagged with corrected p < 0.05.\n- id: fig2d-population-sparseness\n  statement: Population sparseness per trial differs only between OB-p and untagged\n    populations (p = 1.26 x 10^-5).\n  source: Results, OB-p and mPFC-p neurons exhibit broadly similar odor response properties,\n    but differ in dynamics, paragraph 3; Figure 2D\n  quote: At the ensemble level, population sparseness differed only between OB-p ensembles and\n    the untagged populations\n  statistics:\n  - about: OB-p against untagged\n    test: not named; two-sided Mann-Whitney U with Bonferroni correction presumed\n    p: 1.26e-05\n    n: 64 trials per group\n  criterion: Population sparseness per pseudo-population trial (8 odors by 8 trials, 64 per\n    group) over all cells of the group, from their binary activity on that trial (0 to 5 s).\n    Two-sided Mann-Whitney U tests over the 3 pairs, Bonferroni corrected. Reproduced when only\n    OB-p against untagged has corrected p < 0.05. The direction is reported (the paper does\n    not state it).\n- id: fig2-proportion-responding\n  statement: A higher proportion of OB-p than mPFC-p neurons responds to odorants.\n  source: Results, OB-p and mPFC-p neurons exhibit broadly similar odor response properties,\n    but differ in dynamics, paragraph 3\n  quote: with OB-p neurons responding in a significantly higher proportion than mPFC-p neurons\n    (two-sided Mann–Whitney U test with Bonferroni corrected p-values, p = 5.79 × 10⁻ 7 )\n  statistics:\n  - test: two-sided Mann-Whitney U test\n    p: 5.79e-07\n    corrected: Bonferroni\n  criterion: The proportion of active cells (Methods, Metrics derived from response\n    binarization) per trial, 0 to 5 s window. Readings of the sample are (a) per pseudo-\n    population trial over all cells of the group (64 values per group) and (b) per neuron, the\n    proportion of trials it is active (mean binarized activity). Two-sided Mann-Whitney U test,\n    Bonferroni corrected over the 3 pairs. Reproduced when OB-p exceeds mPFC-p with corrected p\n    < 0.05 under one reading.\n- id: fig2e-reliability\n  statement: OB-p populations contain higher fractions of both unreliable and reliable\n    responsive cells per trial (10.97% and 1.54%) than mPFC-p populations (8.71% and 0.25%).\n  source: Results, OB-p and mPFC-p neurons exhibit broadly similar odor response properties,\n    but differ in dynamics, paragraph 3; Figure 2E\n  quote: OB-p populations contained higher fractions of both unreliable and reliable cells\n    (10.97% and 1.54%, respectively) than mPFC-p populations ( Figure 2E , 8.71% and 0.25%\n  statistics:\n  - about: unreliable cells\n    test: two-sided Mann-Whitney U test\n    p: 0.00039\n    corrected: Bonferroni\n  - about: reliable cells\n    test: two-sided Mann-Whitney U test\n    p: 8.2e-14\n    corrected: Bonferroni\n  expected:\n  - quantity: OB-p unreliable responsive cells per trial\n    value: 10.97\n    tolerance: 1.097\n    unit: percent\n  - quantity: OB-p reliable responsive cells per trial\n    value: 1.54\n    tolerance: 0.154\n    unit: percent\n  - quantity: mPFC-p unreliable responsive cells per trial\n    value: 8.71\n    tolerance: 0.871\n    unit: percent\n  - quantity: mPFC-p reliable responsive cells per trial\n    value: 0.25\n    tolerance: 0.025\n    unit: percent\n  criterion: Methods, Reliability analysis. A cell responds on a trial when its mean\n    normalized fluorescence 0 to 5 s after onset exceeds its baseline mean plus 2.33 baseline\n    SDs; a cell is reliable if it responds on more than half of its odor trials, unreliable\n    otherwise; per trial, the percentage of the group's cells that respond and are reliable,\n    and that respond and are unreliable. Open details are the baseline window, read as (a) the\n    4 s before onset (the Methods' baseline for active responses) or (b) the whole 5 s pre-odor\n    baseline; whether the baseline mean and SD are per trial or pooled over the cell's trials,\n    read as (c) per trial or (d) pooled; and whether \"more than half\" counts over all odor\n    trials or per odor, read as (e) all odor trials or (f) any odor. Trials are pseudo-\n    population trials (64). Two-sided Mann-Whitney U tests of OB-p against mPFC-p, Bonferroni\n    corrected. Reproduced when, under one combination of readings, the four percentages are\n    within tolerance and both tests have corrected p < 0.05 with OB-p higher; partially\n    reproduced when both directions and tests hold but the values do not.\n- id: fig2f-latency\n  statement: In the 30 Hz data OB-p neurons reach their first calcium peak after odor onset\n    sooner than mPFC-p neurons; OB-p and untagged neurons do not differ.\n  source: Results, OB-p and mPFC-p neurons exhibit broadly similar odor response properties,\n    but differ in dynamics, paragraph 4; Figure 2F\n  quote: OB-p neurons exhibited shorter latencies to reach the first peak of calcium activity\n    following odor onset compared to mPFC-p neurons\n  statistics:\n  - about: OB-p against mPFC-p\n    test: two-sided Mann-Whitney U test\n    p: 1.18e-17\n    corrected: Bonferroni\n  - about: OB-p against untagged\n    test: two-sided Mann-Whitney U test\n    p: 1\n    corrected: Bonferroni\n  - about: mPFC-p against untagged\n    test: two-sided Mann-Whitney U test\n    p: 5.05e-25\n    corrected: Bonferroni\n  data: dataset\n  criterion: Fast (30 Hz) dataset. Peaks found on normalized fluorescence per trial with the\n    Methods' minimum criteria (width 100 ms, distance 1 s, height 0.5, prominence 0.25), read as\n    scipy.signal.find_peaks arguments, ignoring the first and last second of each trial;\n    latency is the time of the first peak after odor onset. Whether a latency is per trial\n    (all trials with a peak) or per neuron (median over trials) is open; the sizes of the p-\n    values suggest per trial, and both are run, (a) per trial and (b) per neuron. Two-sided\n    Mann-Whitney U tests, Bonferroni corrected over the 3 pairs. Reproduced when OB-p is\n    shorter than mPFC-p with corrected p < 0.05 under one reading. The OB-p against untagged\n    result is reported; the \"= 1\" is not required.\n- id: fig2g-early-peaks\n  statement: OB-p neurons have more calcium peaks at early time points after odor onset than\n    mPFC-p neurons.\n  source: Results, OB-p and mPFC-p neurons exhibit broadly similar odor response properties,\n    but differ in dynamics, paragraph 4; Figure 2G and Figure S4A to S4C\n  quote: OB-p neurons also had more peaks during earlier time points than mPFC-p neurons\n  depends_on:\n  - fig2f-latency\n  criterion: Peaks as in fig2f-latency, counted per trial in time bins aligned to odor onset\n    and averaged per neuron. The paper gives no bin width, no window for \"earlier\" and no test.\n    Readings of \"earlier\" are (a) 0 to 2 s (the odor pulse) and (b) 0 to 3 s (the early epoch\n    of Figure 1G). Reproduced when the mean number of peaks per trial in that window is higher\n    for OB-p than mPFC-p under both readings; the counts are reported. The OASIS deconvolved-\n    event version (Figure S4) is shown as a variant.\n- id: fig2h-identity-decoding-5s\n  statement: Odor identity decoded from 5 s windows reaches similar accuracy in size-matched OB-\n    p and mPFC-p pseudo-populations, above chance and slightly below untagged.\n  source: Results, OB-p and mPFC-p neurons exhibit broadly similar odor response properties,\n    but differ in dynamics, paragraph 5; Figure 2H\n  quote: both OB-p and mPFC-p pseudo-populations reached similar accuracy levels, significantly\n    above chance but slightly lower than the untagged population ( Figure 2H ; two-sided\n    Mann-Whitney U test, p = 0.398)\n  statistics:\n  - about: OB-p against mPFC-p, 75 cells\n    test: two-sided Mann-Whitney U test\n    p: 0.398\n  criterion: A claim of absence for OB-p against mPFC-p, on the paper's test. Linear SVM, 8\n    odors, mean normalized fluorescence per cell in the window, 5-fold cross-validation, 75-\n    cell pseudo-populations, 200 train/test repeats (Figure 2H legend, right). The window is\n    0 to 5 s in the legend and 1 to 5 s in the Methods; both are run, (a) 0 to 5 s and (b) 1 to\n    5 s. Reproduced when the two-sided Mann-Whitney U test of the 200 OB-p against the 200\n    mPFC-p accuracies has p >= 0.05; not reproduced when p < 0.05. The mean accuracies are\n    reported against chance (12.5%) and against untagged. If the two windows disagree the\n    claim is methods_underspecified.\n- id: fig2i-identity-decoding-early\n  statement: In an early window (0 to 2 s) OB-p pseudo-populations decode odor identity better\n    than mPFC-p pseudo-populations.\n  source: Results, OB-p and mPFC-p neurons exhibit broadly similar odor response properties,\n    but differ in dynamics, paragraph 6; Figure 2I\n  quote: we found that OB-p pseudo-populations outperformed mPFC-p pseudo-populations ( Figure\n    2I , two-sided Mann-Whitney U test with p = 2.15 × 10⁻ 30 )\n  statistics:\n  - test: two-sided Mann-Whitney U test\n    p: 2.15e-30\n    n: 200 train/test repeats per group, 75 cells\n  criterion: As fig2h-identity-decoding-5s with a 0 to 2 s window. Reproduced when OB-p\n    accuracy exceeds mPFC-p with two-sided Mann-Whitney U p < 0.05 over the 200 repeats.\n- id: fig2j-identity-decoding-peaks-earlier\n  statement: With a sliding window, odor identity decoding accuracy peaks earlier for OB-p\n    than for mPFC-p pseudo-populations.\n  source: Results, OB-p and mPFC-p neurons exhibit broadly similar odor response properties,\n    but differ in dynamics, paragraph 6; Figure 2J\n  quote: SVM classification using a sliding window for odor responses revealed that decoding\n    accuracy for OB-p neurons peaked earlier than for mPFC-p neurons\n  criterion: Linear SVM on mean normalized fluorescence in consecutive windows across the\n    trial, trained and tested on the same window, 75-cell pseudo-populations, 100 repeats. The\n    window is 250 ms in the Figure 2J legend and 500 ms in the Methods; at 4.53 Hz a 250 ms\n    window holds one or two frames. Both are run, (a) 250 ms and (b) 500 ms. No test is\n    given. Reproduced when the time of the peak of the mean accuracy curve is earlier for OB-p\n    than for mPFC-p under both readings; the times and the 95% intervals of the peak time over\n    repeats are reported.\n- id: fig2k-mpfc-late-identity\n  statement: Late in the trial, mPFC-p pseudo-populations keep low but above-chance identity\n    decoding that exceeds OB-p decoding.\n  source: Results, OB-p and mPFC-p neurons exhibit broadly similar odor response properties,\n    but differ in dynamics, paragraph 6; Figure 2K\n  quote: mPFC-p pseudo-populations maintained low but above-chance identity decoding that\n    exceeded OB-p decoding later in the trial\n  criterion: From the same-window accuracies of fig2j-identity-decoding-peaks-earlier (the\n    diagonal of Figure 2K). \"Later in the trial\" is not bounded; it is read as after odor\n    offset, (a) 2 to 15 s and (b) 5 to 15 s after onset. Reproduced when, under both readings,\n    the mPFC-p mean accuracy over the window exceeds 12.5% and exceeds the OB-p mean, with\n    repeats as samples (one-sample one-sided t-test against 12.5% and two-sided Mann-Whitney U,\n    p < 0.05, the tests the paper uses for decoding elsewhere).\n- id: fig3bc-concentration-tuning\n  statement: Similar fractions of OB-p and mPFC-p neurons are tuned to odor identity, but OB-p\n    neurons more often show significant effects of concentration and identity by\n    concentration interactions, which are rare in mPFC-p neurons.\n  source: Results, Odor concentration is robustly encoded in OB-p but not mPFC-p neurons,\n    paragraph 2; Figure 3B and 3C\n  quote: Across time, similar fractions of OB-p and mPFC-p neurons were significantly tuned to\n    odor identity ( Figure 3B ) ... By contrast, OB-p neurons were more likely to show\n    significant main effects of concentration, as well as identity × concentration interactions\n  criterion: Concentration dataset. Per neuron, a two-way ANOVA (identity, 3 odors, by\n    concentration, 3 levels, with interaction) on mean normalized fluorescence in the first 5 s\n    of odor presentation over trials (Figure 3B legend), p < 0.05 per term; the fraction of\n    neurons significant per term per group. The time-resolved version (Figure 3C) uses\n    sliding windows of unstated width, read as (a) 500 ms and (b) 1 s steps of the same width.\n    The paper gives no test of the fractions. Reproduced when, in the 0 to 5 s analysis, the\n    OB-p fractions for concentration and for interaction both exceed the mPFC-p fractions, and\n    the OB-p minus mPFC-p difference for identity is smaller in absolute size than that for\n    concentration; the time courses are reported.\n- id: fig3de-concentration-decoding\n  statement: OB-p pseudo-populations decode odor concentration more accurately and earlier\n    than mPFC-p and untagged pseudo-populations, while mPFC-p decoding stays close to chance.\n  source: Results, Odor concentration is robustly encoded in OB-p but not mPFC-p neurons,\n    paragraph 3; Figure 3D and 3E\n  quote: OB-p pseudo-populations reached higher concentration classification accuracy and did\n    so earlier in the trial than both mPFC-p and untagged pseudo-populations, whereas mPFC-p\n    ensembles supported only weak concentration decoding that remained close to chance\n  criterion: Per odor, a linear SVM decoding the 3 concentrations from mean normalized\n    fluorescence in sliding windows (250 ms in the Figure 3D legend, 500 ms in Figure 3E and\n    the Methods; both run), 75-cell pseudo-populations, 100 repeats, accuracies averaged over\n    the 3 odors; chance 33.3%. No test is given. Reproduced when the peak mean accuracy of OB-p\n    exceeds those of mPFC-p and untagged, the OB-p peak time is earlier than both, and the\n    mPFC-p peak mean accuracy is below the midpoint between chance and the OB-p peak, under\n    both window readings.\n- id: figs5g-pairwise-concentration\n  statement: Pairwise concentration decoding (low against medium, medium against high, low\n    against high) is strongest and most sustained in OB-p ensembles, intermediate in untagged\n    neurons and weakest in mPFC-p neurons.\n  source: Results, Odor concentration is robustly encoded in OB-p but not mPFC-p neurons,\n    paragraph 3; Figure S5G\n  quote: concentration decoding was again strongest and most sustained in OB-p ensembles,\n    intermediate in untagged neurons, and weakest in mPFC-p neurons\n  criterion: As fig3de-concentration-decoding, with binary SVMs for each pair of\n    concentrations per odor (chance 50%), averaged over odors, same-window accuracies. Read\n    as the mean same-window accuracy over 0 to 15 s after onset per group. Reproduced when the\n    order OB-p > untagged > mPFC-p holds for all three pairs under both window readings.\n- id: figs5-sparseness-concentration\n  statement: Across the three concentrations, response sparseness and the fraction of active\n    cells change only modestly in all three populations.\n  source: Results, Odor concentration is robustly encoded in OB-p but not mPFC-p neurons,\n    paragraph 2; Figure S5A to S5D\n  quote: overall response sparseness and the fraction of active cells changed only modestly in\n    all three populations ( Figure S5 )\n  criterion: Per concentration (0.1%, 1%, 10% in the Figure S5 legend), the percentage of\n    active cells (binarized, 0 to 5 s) and lifetime sparseness per neuron over the 3 odors,\n    population sparseness per subject (Figure S5D). The paper gives no test and no bound for\n    \"modestly\"; the values per population and concentration are reported and the claim is\n    judged only on whether no population shows a monotonic change of more than half its value\n    at 0.1% across the range, a reading of \"only modestly\" recorded as such.\n- id: fig4c-behavior-learning\n  statement: Go/NoGo performance improves across training days, with no difference between OB-\n    p and mPFC-p labelled mice, reaching 73.7% correct trials on day 3.\n  source: Results, Differential encoding of odor valence in OB-p and mPFC-p neurons, paragraph\n    2; Figure 4C\n  quote: Behavioral performance improved as training progressed, with no significant\n    difference between OB-p and mPFC-p labelled mice ... with, on average, 73.7% correct trials\n    (hit and correct rejection) on day 3\n  statistics:\n  - about: days, repeated-measures ANOVA\n    test: repeated-measures ANOVA within days\n    statistic: F = 4.375\n    p: 0.0374\n    n: 7 mice\n  - about: days, mixed ANOVA\n    test: mixed ANOVA, within days\n    p: 0.0441\n  - about: projection, mixed ANOVA\n    test: mixed ANOVA, between projections\n    p: 0.767\n  - about: days by projection interaction\n    test: mixed ANOVA, interaction\n    p: 0.421\n  expected:\n  - quantity: repeated-measures ANOVA F for days\n    value: 4.375\n    tolerance: 0.4375\n  - quantity: mean percent correct trials on day 3\n    value: 73.7\n    tolerance: 7.37\n    unit: percent\n  criterion: Per mouse and task day (1 to 3), percent correct = (hits + correct rejections) /\n    scored CS trials, with hits as relabeled in the Methods (reward within 10 s after the\n    delay), excluding bad trials. A one-way repeated-measures ANOVA on days, and a mixed ANOVA\n    (days within, projection between). Reproduced when F and the day 3 mean are within\n    tolerance, the day effect has p < 0.05 in both ANOVAs and projection and interaction have\n    p >= 0.05. Whether the NWB outcome labels already apply the 10 s relabeling is the\n    author's to check; both the stored outcome and the relabeled outcome are run.\n- id: fig4c-anticipatory-licking\n  statement: Anticipatory licking in response to the rewarded odorants increases across\n    training.\n  source: Results, Differential encoding of odor valence in OB-p and mPFC-p neurons, paragraph\n    2; Figure 4C right and Figure S6\n  quote: an increase in anticipatory licking in response to the rewarded odorants\n  criterion: Lick rate on CS+ trials before the reward window opens. \"Anticipatory\" is read\n    as (a) the delay, 2 to 5 s after odor onset, and (b) odor and delay, 0 to 5 s. The paper\n    gives no test. Reproduced when the mean over mice of the CS+ lick rate is higher on day 3\n    than on day 1 under both readings; per-mouse values are reported.\n- id: fig4def-identity-decoding-gng\n  statement: In expert mice (day 3), OB-p pseudo-populations decode odor identity above chance\n    in all four task phases, peaking early (delay) and declining later, whereas mPFC-p\n    pseudo-populations are near chance early and improve later in the trial.\n  source: Results, Differential encoding of odor valence in OB-p and mPFC-p neurons, paragraph\n    3; Figure 4D, 4E and 4F\n  quote: odor identity decoding in OB-p pseudo-populations was greater than chance across all 4\n    task phases ... Decoding accuracy peaked during early trial phases (delay phase after odor\n    exposure), but declined later in the trial (action) ... In contrast, mPFC-p\n    pseudo-populations performed near chance during early trial phases, but decoding accuracy\n    increased later in the trial\n  statistics:\n  - about: OB-p, odor phase, against 25%\n    test: one-sample one-sided t-test\n    p: 2.34e-56\n    corrected: Bonferroni\n  - about: OB-p, delay\n    test: one-sample one-sided t-test\n    p: 7.27e-78\n    corrected: Bonferroni\n  - about: OB-p, act-early\n    test: one-sample one-sided t-test\n    p: 1.66e-73\n    corrected: Bonferroni\n  - about: OB-p, act-late\n    test: one-sample one-sided t-test\n    p: 1.2e-63\n    corrected: Bonferroni\n  - about: mPFC-p, odor\n    test: one-sample one-sided t-test\n    p: 0.0301\n    corrected: Bonferroni\n  - about: mPFC-p, delay\n    test: one-sample one-sided t-test\n    p: 1.42e-32\n    corrected: Bonferroni\n  - about: mPFC-p, act-early\n    test: one-sample one-sided t-test\n    p: 4.44e-70\n    corrected: Bonferroni\n  - about: mPFC-p, act-late\n    test: one-sample one-sided t-test\n    p: 4.95e-87\n    corrected: Bonferroni\n  criterion: Day 3, 4 odors (chance 25%), linear SVM per task phase (trained and tested on the\n    same phase), 85-cell pseudo-populations from 4 OB-p and 3 mPFC-p mice, 100 repeats;\n    aggregate readings (a) mean and (b) maximum over the phase. One-sample one-sided t-tests\n    against 25% over the 100 accuracies, Bonferroni over 4 phases. Reproduced when, under one\n    aggregate reading, OB-p is above chance in all 4 phases with its highest mean accuracy in\n    the odor or delay phase and lower in act-late than in delay, and mPFC-p has its two lowest\n    mean accuracies in odor and delay and its highest in act-early or act-late. The Figure 4F\n    legend's OB-p against mPFC-p differences in every phase are reported with two-sided\n    Mann-Whitney U tests (the paper's test for such comparisons in Figure 4H).\n- id: fig4g-valence-any\n  statement: Generalized odor valence can be decoded above chance from a general PCx (any-p)\n    pseudo-population in all task phases in expert mice.\n  source: Results, Differential encoding of odor valence in OB-p and mPFC-p neurons, paragraph\n    4; Figure 4G and Figure S8H\n  quote: We found that odor valence could be decoded with high accuracy from a general PCx\n    pseudo-population across all phases\n  statistics:\n  - about: odor phase\n    test: one-sample one-sided t-test against 50%\n    p: 0.00222\n    corrected: Bonferroni\n  - about: delay\n    test: one-sample one-sided t-test against 50%\n    p: 5.31e-31\n    corrected: Bonferroni\n  - about: act-early\n    test: one-sample one-sided t-test against 50%\n    p: 1.55e-28\n    corrected: Bonferroni\n  - about: act-late\n    test: one-sample one-sided t-test against 50%\n    p: 1.7e-16\n    corrected: Bonferroni\n  criterion: Day 3. Generalized valence (Methods) trains on one CS+/CS- pair and tests on the\n    other, all 4 permutations, accuracy averaged over them; any-p pseudo-populations of 85\n    cells sampled from tagged and untagged cells of all 7 mice, 100 repeats, per task phase;\n    aggregate readings (a) mean and (b) maximum. One-sample one-sided t-tests against 50%,\n    Bonferroni over 4 phases. Reproduced when all 4 phases have corrected p < 0.05 under one\n    reading.\n- id: fig4h-valence-timing\n  statement: In expert mice OB-p pseudo-populations encode generalized valence in the odor and\n    delay phases but fall to chance in the action phases, while mPFC-p pseudo-populations\n    encode valence in the later but not the earliest phase; the two differ in all four phases.\n  source: Results, Differential encoding of odor valence in OB-p and mPFC-p neurons, paragraph\n    5; Figure 4H\n  quote: OB-p pseudo-populations accurately encoded odor valence during early phases of the\n    trial (odor exposure, delay), but that decoding accuracy decreased to chance level later in\n    the trial (action) ... In contrast, mPFC-p pseudo-populations encoded odor valence during\n    later but not early phases of the trial\n  statistics:\n  - about: OB-p, odor, against 50%\n    test: one-sample one-sided t-test\n    p: 1.37e-40\n    corrected: Bonferroni\n  - about: OB-p, delay\n    test: one-sample one-sided t-test\n    p: 1.78e-44\n    corrected: Bonferroni\n  - about: OB-p, act-early\n    test: one-sample one-sided t-test\n    p: 0.00141\n    corrected: Bonferroni\n  - about: OB-p, act-late\n    test: one-sample one-sided t-test\n    p: 1\n    corrected: Bonferroni\n  - about: mPFC-p, odor\n    test: one-sample one-sided t-test\n    p: 1\n    corrected: Bonferroni\n  - about: mPFC-p, delay\n    test: one-sample one-sided t-test\n    p: 2.62e-15\n    corrected: Bonferroni\n  - about: mPFC-p, act-early\n    test: one-sample one-sided t-test\n    p: 1.07e-42\n    corrected: Bonferroni\n  - about: mPFC-p, act-late\n    test: one-sample one-sided t-test\n    p: 2.42e-68\n    corrected: Bonferroni\n  - about: OB-p against mPFC-p, odor\n    test: two-sided Mann-Whitney U test\n    p: 1.29e-33\n    corrected: Bonferroni\n  - about: OB-p against mPFC-p, delay\n    test: two-sided Mann-Whitney U test\n    p: 3.05e-13\n    corrected: Bonferroni\n  - about: OB-p against mPFC-p, act-early\n    test: two-sided Mann-Whitney U test\n    p: 1.14e-23\n    corrected: Bonferroni\n  - about: OB-p against mPFC-p, act-late\n    test: two-sided Mann-Whitney U test\n    p: 1.0e-33\n    corrected: Bonferroni\n  criterion: As fig4g-valence-any with OB-p and mPFC-p pseudo-populations. Reproduced when,\n    under one aggregate reading, OB-p is above 50% (corrected p < 0.05) in odor and delay and\n    not in act-late; mPFC-p is not above 50% in odor and is above in delay, act-early and act-\n    late; and the two-sided Mann-Whitney U test of OB-p against mPFC-p accuracies has corrected\n    p < 0.05 in all four phases. Partially reproduced when the pattern of above-chance phases\n    holds and the between-group tests hold in two or three phases. The text's act-early OB-p\n    result (p = 0.00141, above chance) is reported alongside.\n- id: fig4ij-valence-correct-trials\n  statement: Restricted to correct trials, OB-p pseudo-populations encode valence well early\n    and much less later, mPFC-p pseudo-populations encode it more accurately late than early,\n    and the two differ in all four phases.\n  source: Results, Differential encoding of odor valence in OB-p and mPFC-p neurons,\n    paragraphs 6 and 7; Figure 4I and 4J\n  quote: OB-p pseudo-populations accurately encoded odor valence during early phases of the\n    trial but much less so later ... mPFC-p pseudo-populations encoded odor valence late in\n    correct trials more accurately than early ... For all four task phases, these projection\n    pseudo-populations performed differently from one another at decoding valence for correct\n    trials\n  statistics:\n  - about: OB-p, odor, against 50%\n    test: one-sample one-sided t-test\n    p: 5.04e-69\n    corrected: Bonferroni\n  - about: OB-p, delay\n    test: one-sample one-sided t-test\n    p: 4.35e-72\n    corrected: Bonferroni\n  - about: OB-p, act-early\n    test: one-sample one-sided t-test\n    p: 4.29e-18\n    corrected: Bonferroni\n  - about: OB-p, act-late\n    test: one-sample one-sided t-test\n    p: 3.04e-12\n    corrected: Bonferroni\n  - about: mPFC-p, odor\n    test: one-sample one-sided t-test\n    p: 1\n    corrected: Bonferroni\n  - about: mPFC-p, delay\n    test: one-sample one-sided t-test\n    p: 1.97e-19\n    corrected: Bonferroni\n  - about: mPFC-p, act-early\n    test: one-sample one-sided t-test\n    p: 3.89e-63\n    corrected: Bonferroni\n  - about: mPFC-p, act-late\n    test: one-sample one-sided t-test\n    p: 1.16e-88\n    corrected: Bonferroni\n  - about: OB-p against mPFC-p, odor\n    test: two-sided Mann-Whitney U test\n    p: 1.09e-33\n    corrected: Bonferroni\n  - about: OB-p against mPFC-p, delay\n    test: two-sided Mann-Whitney U test\n    p: 1.46e-33\n    corrected: Bonferroni\n  - about: OB-p against mPFC-p, act-early\n    test: two-sided Mann-Whitney U test\n    p: 5.06e-22\n    corrected: Bonferroni\n  - about: OB-p against mPFC-p, act-late\n    test: two-sided Mann-Whitney U test\n    p: 1.12e-33\n    corrected: Bonferroni\n  criterion: Day 3, correct trials only (hits and correct rejections). Which valence scheme\n    Figure 4I and 4J use is open, since the legend says generalized valence in correct trials\n    is in Figure S8E and S8G; the reading is valence (unconstrained) for correct trials\n    (Methods, the fifth classifier), with the generalized scheme as the subject of\n    figs8-generalized-valence-correct. 85 cells, 100 repeats, aggregate readings (a) mean and\n    (b) maximum. Reproduced when, under one reading, OB-p mean accuracy is higher in odor and\n    delay than in act-early and act-late, mPFC-p is higher in act-early and act-late than in\n    odor and delay with odor not above 50% (corrected p >= 0.05), and OB-p against mPFC-p\n    differs (two-sided Mann-Whitney U, Bonferroni, p < 0.05) in all four phases.\n- id: figs8-generalized-valence-correct\n  statement: Generalized valence decoding in correct trials differs between OB-p and mPFC-p\n    pseudo-populations in the odor and act-early phases but not in the delay and act-late\n    phases.\n  source: Results, Differential encoding of odor valence in OB-p and mPFC-p neurons, paragraph\n    7; Figure S8E, S8G and S8K\n  quote: We also observed significant differences with generalized valence decoding performance\n    in correct trials between projection pseudo-populations during odor and act-early phases\n  statistics:\n  - about: odor\n    test: two-sided Mann-Whitney U test\n    p: 4.54e-31\n    corrected: Bonferroni\n  - about: delay\n    test: two-sided Mann-Whitney U test\n    p: 0.86\n    corrected: Bonferroni\n  - about: act-early\n    test: two-sided Mann-Whitney U test\n    p: 2.11e-27\n    corrected: Bonferroni\n  - about: act-late\n    test: two-sided Mann-Whitney U test\n    p: 1\n    corrected: Bonferroni\n  criterion: Day 3, correct trials, generalized valence (4 permutations), 85 cells, 100\n    repeats, aggregate readings (a) mean and (b) maximum. Reproduced when, under one reading,\n    the two-sided Mann-Whitney U test of OB-p against mPFC-p has corrected p < 0.05 in odor and\n    act-early and corrected p >= 0.05 in delay and act-late; the direction in each phase is\n    reported.\n- id: tracked-neuron-counts\n  statement: Longitudinal tracking across the three Go/NoGo sessions follows 46 OB-p and 41\n    mPFC-p neurons in 4 OB-p and 3 mPFC-p tagged mice.\n  source: Results, Longitudinal tracking reveals greater stability of valence encoding in\n    feedforward projection neurons, paragraph 1; Methods, Longitudinal tracking\n  quote: we longitudinally tracked identified neurons across three Go/NoGo sessions and followed\n    46 OB-p and 41 mPFC-p neurons in 4 OB-p–tagged and 3 mPFC-p–tagged mice\n  expected:\n  - quantity: tracked OB-p neurons\n    value: 46\n    tolerance: 4.6\n  - quantity: tracked mPFC-p neurons\n    value: 41\n    tolerance: 4.1\n  criterion: Cells with one tracking identifier present in all four sessions (day 0 to 3) and\n    red in at least 3 of them (code criterion min_3_sessions), counted per projection.\n    Reproduced when both counts are within tolerance; the counts under the code's other\n    criteria (min_1_session, first_4_sessions, all_sessions) are reported.\n- id: figs10d-slope-no-difference\n  statement: Tracked OB-p and mPFC-p neurons do not differ in the average slope of their\n    session-averaged normalized fluorescence across the three Go/NoGo days.\n  source: Results, Longitudinal tracking reveals greater stability of valence encoding in\n    feedforward projection neurons, paragraph 2; Figure S10D\n  quote: there was no significant difference in the average slope between OB-p and mPFC-p\n    neurons\n  statistics:\n  - about: combination of valence and task phase\n    test: mixed ANOVA on slopes\n    p: 0.11\n  - about: projection target\n    test: mixed ANOVA on slopes\n    p: 0.36\n  - about: interaction\n    test: mixed ANOVA on slopes\n    p: 0.0031\n  depends_on:\n  - tracked-neuron-counts\n  criterion: A claim of absence, on the paper's test. For each tracked neuron and each\n    combination of odor valence (CS+, CS-) and task phase (4), the mean normalized\n    fluorescence over the phase and over that valence's trials on each of days 1 to 3, and\n    the least-squares slope over days; a mixed ANOVA with the combination (8 levels) within\n    neurons and projection between. Reproduced when the projection effect has p >= 0.05; not\n    reproduced when p < 0.05. The interaction is reported against p = 0.0031.\n- id: figs10e-sparseness-slope-no-difference\n  statement: Changes in lifetime sparseness across sessions show no clear effect of projection\n    target.\n  source: Results, Longitudinal tracking reveals greater stability of valence encoding in\n    feedforward projection neurons, paragraph 2; Figure S10E\n  quote: We similarly quantified changes in lifetime sparseness across sessions and did not\n    observe a clear effect of projection target\n  statistics:\n  - about: task phase\n    test: mixed ANOVA on sparseness slopes\n    p: 0.0491\n  - about: projection target\n    test: mixed ANOVA on sparseness slopes\n    p: 0.364\n  - about: interaction\n    test: mixed ANOVA on sparseness slopes\n    p: 0.765\n  depends_on:\n  - tracked-neuron-counts\n  criterion: A claim of absence. Per tracked neuron, task phase and day, lifetime sparseness\n    over the 4 odors of binarized activity in that phase; slope over days 1 to 3; a mixed ANOVA\n    with phase within and projection between. Reproduced when the projection effect has p >=\n    0.05; not reproduced when p < 0.05.\n- id: fig5c-cv-higher-obp\n  statement: Tracked OB-p neurons show a higher coefficient of variation of session-averaged\n    fluorescence across days than mPFC-p neurons.\n  source: Results, Longitudinal tracking reveals greater stability of valence encoding in\n    feedforward projection neurons, paragraph 3; Figure 5C\n  quote: OB-p neurons typically showed higher fluorescence CV across days than mPFC-p neurons (\n    Figure 5C, D ). A mixed ANOVA on CV within combinations of odors and task phases revealed a\n    significant effect of projection target (p = 0.0127)\n  statistics:\n  - about: projection target\n    test: mixed ANOVA on CV\n    p: 0.0127\n  - about: odor and phase combination\n    test: mixed ANOVA on CV\n    p: 0.0372\n  - about: interaction\n    test: mixed ANOVA on CV\n    p: 0.43\n  depends_on:\n  - tracked-neuron-counts\n  criterion: Per tracked neuron and combination, the coefficient of variation (SD over mean)\n    of the session-averaged normalized fluorescence over days 1 to 3; a mixed ANOVA with the\n    combination within neurons and projection between. Open details are the combination,\n    read as (a) valence (CS+, CS-, as plotted in Figure 5C) by phase, 8 levels, and (b) odor (4)\n    by phase, 16 levels; and the treatment of means near zero or negative (normalized\n    fluorescence is centred near zero), read as (c) SD over the absolute mean and (d) SD over\n    the mean. Reproduced when, under every combination of readings, the projection effect has\n    p < 0.05 with OB-p higher (by median CV); when readings disagree, methods_underspecified.\n    The per-condition Mann-Whitney U tests with Benjamini-Hochberg correction (Figure S10F)\n    are reported.\n- id: fig5e-transferability\n  statement: Identity decoding transfers across sessions comparably in tracked OB-p and mPFC-p\n    ensembles, whereas generalized valence decoding transfers better in mPFC-p ensembles,\n    especially across distal sessions.\n  source: Results, Longitudinal tracking reveals greater stability of valence encoding in\n    feedforward projection neurons, paragraph 4; Figure 5E and Figure S11\n  quote: When decoding odor identity, transferability across dissimilar sessions was\n    comparable between OB-p and mPFC-p ensembles ... whereas mPFC-p ensembles maintained higher\n    valence decoding accuracy, particularly for generalized valence across distal sessions\n  statistics:\n  - about: identity, within session\n    test: two-sided Mann-Whitney U test\n    p: 4.59e-05\n    corrected: Bonferroni\n  - about: identity, proximal sessions\n    test: two-sided Mann-Whitney U test\n    p: 0.194\n    corrected: Bonferroni\n  - about: identity, distal sessions\n    test: two-sided Mann-Whitney U test\n    p: 0.686\n    corrected: Bonferroni\n  - about: generalized valence, within session\n    test: two-sided Mann-Whitney U test\n    p: 0.774\n    corrected: Bonferroni\n  - about: generalized valence, proximal sessions\n    test: two-sided Mann-Whitney U test\n    p: 0.0356\n    corrected: Bonferroni\n  - about: generalized valence, distal sessions\n    test: two-sided Mann-Whitney U test\n    p: 5.41e-06\n    corrected: Bonferroni\n  depends_on:\n  - tracked-neuron-counts\n  criterion: Per mouse, a linear SVM on its tracked projection neurons, trained on one (day,\n    phase) and tested on another, for days 1 to 3 and the 4 phases (Figure 5D); same-phase and\n    adjacent-phase pairs only; transfers grouped as within session, proximal (consecutive\n    days) and distal (day 1 and day 3). Open details, which could change the outcome. The\n    samples of the Mann-Whitney test, read as (a) every qualifying accuracy entry of every\n    mouse and (b) per mouse means; the folds for train and test within one session, read as 5-\n    fold stratified cross-validation; aggregate readings mean and maximum. Two-sided Mann-\n    Whitney U tests of OB-p against mPFC-p entries per group, Bonferroni over the 3 groups.\n    Reproduced when, under one reading, identity has corrected p >= 0.05 for proximal and\n    distal, and generalized valence has mPFC-p higher with corrected p < 0.05 for distal.\n- id: fig5f-stability\n  statement: The temporal structure of valence coding across sessions is more stable in\n    tracked mPFC-p than OB-p ensembles, while odor identity coding is not.\n  source: Results, Longitudinal tracking reveals greater stability of valence encoding in\n    feedforward projection neurons, paragraph 5; Figure 5F and Figure S12B\n  quote: These analyses revealed that the temporal structure of valence coding was\n    consistently more stable in mPFC-p than in OB-p ensembles\n  statistics:\n  - about: odor identity\n    test: two-sided Mann-Whitney U test\n    p: 0.755\n    corrected: Bonferroni\n  - about: valence\n    test: two-sided Mann-Whitney U test\n    p: 6.24e-06\n    corrected: Bonferroni\n  - about: generalized valence\n    test: two-sided Mann-Whitney U test\n    p: 2.89e-11\n    corrected: Bonferroni\n  - about: valence for correct trials\n    test: two-sided Mann-Whitney U test\n    p: 2.5e-06\n    corrected: Bonferroni\n  depends_on:\n  - fig5e-transferability\n  criterion: From the per-mouse transfer matrices of fig5e-transferability, each 4 by 4\n    transfer block (train day, test day) flattened, and Pearson correlations between pairs of\n    blocks (Methods, Decoding with tracked neurons). Open details are which blocks are paired,\n    read as (a) all pairs of the 9 blocks and (b) pairs sharing the training day; and the\n    samples, read as (c) every correlation of every mouse and (d) per mouse means. Two-sided\n    Mann-Whitney U tests of OB-p against mPFC-p correlations, Bonferroni over the 4 schemes.\n    Reproduced when, under one combination of readings, valence, generalized valence and\n    correct-trial valence each have mPFC-p higher with corrected p < 0.05 and odor identity has\n    corrected p >= 0.05.\n- id: discussion-differences-grow\n  statement: The differences in timing of identity and valence encoding between OB-p and mPFC-\n    p ensembles increase over the course of learning.\n  source: Discussion, Functional specializations of projection neurons align with those of\n    their target areas, paragraph 1; Figure S7A and Figure S9\n  quote: Notably, these differences increased over the course of learning\n  criterion: As in the Figure S7A and S9 legends. Per projection and task phase, accuracies\n    of 50 size-matched pseudo-populations per day are sampled and the slope of accuracy over\n    days 1 to 3 is fitted, 1000 times; a null from day-shuffled data; two-sided Mann-Whitney\n    U tests with Bonferroni correction of observed against null slopes, for identity and\n    generalized valence. The paper gives no test of the difference itself; the claim is read\n    as reproduced when the slopes are significantly positive (corrected p < 0.05, above the\n    null) for OB-p in the odor or delay phase and for mPFC-p in an action phase, for identity\n    or generalized valence. Aggregate readings mean and maximum.\n"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/000785/10.64898-2025.12.12.694045.yaml",
 "old_string": "    Performance remained high (F1 0.754 OB-p; 0.623 mPFC-p)",
 "new_string": "    Performance remained high ... 0.754 OB-p; 0.623 mPFC-p"
}
```

```
The file claims/000785/10.64898-2025.12.12.694045.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
python tools/claims_check.py claims/000785/10.64898-2025.12.12.694045.yaml paper/10.64898-2025.12.12.694045.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
grep -n "—\|rather" claims/000785/*.yaml; python3 -c "
import yaml,re
src=open('claims/000785/10.64898-2025.12.12.694045.yaml').read()
for i,l in enumerate(src.splitlines(),1):
    s=l.split('#')[0] if l.lstrip().startswith('#') else l
    body=re.sub(r'^\s*(- )?[a-z_]+: ','',l)
    if not l.lstrip().startswith('#') and ': ' in body: print(i,l)
"
```

```
(Bash completed with no output)
```

**Agent calls Bash**

```bash
python3 -c "
import yaml;d=yaml.safe_load(open('claims/000785/10.64898-2025.12.12.694045.yaml'))['claims']
print(len(d),sum('quote' in c for c in d),sum('statistics' in c for c in d),sum(len(c.get('statistics',[])) for c in d),sum('criterion' in c for c in d),sum('expected' in c for c in d))"
```

```
36 36 19 75 35 7
```

**Agent**

I wrote `claims/000785/10.64898-2025.12.12.694045.yaml`. The quote checker passes every quote but exits non-zero on two p-values it can't find. I read both in the text: the paper prints them with trailing zeros ("3.90 × 10⁻ 4" in fig2e-reliability and "2.50 × 10 -6" in fig5f-stability), which the checker doesn't recognise. The recorded values are correct, and I changed neither the values nor the checker.

**Text read.** The bioRxiv preprint, version 1, flattened from its JATS XML. It has the main text, the Methods and the legends of supplementary figures S1 to S13; there is no PDF. The paper's linked code is gitlab.com/fleischmann-lab/calcium-imaging/projection-difference at commit f478b34. It only loads and preprocesses the NWB files, plus one demo SVM notebook. The figure analyses are "to be released upon publication". The code settles four things:
- **Normalization:** "percdFF" (1 s median filter, running 10th percentile over 30 s, then divided by the SD).
- **Trial removal:** the NWB `is_bad_trial` column.
- **Tracked-cell labels:** red in at least 3 of 4 sessions (`min_3_sessions`).
- **Classifier:** `SVC(kernel='linear')`, with `LinearSVC` shown as a variant.

**Claims.** There are 36 claims, all with quotes. 19 have statistics (75 entries), 35 have criteria and 7 have expected values. They cover the neuron counts, the labeling check, the transformer and MLP classifiers, the Figure 2 response properties and identity decoding, concentration tuning and decoding, behavior and licking, identity and valence decoding in the Go/NoGo task, and the tracked-neuron slopes, CV, transferability and stability. The last claim, that the differences grow with learning, comes from the Discussion.

**Details the paper leaves open, with the readings named:**
- **Active-response sliding window:** anchored at the start of each frame, or centred on it.
- **Sparseness and mutual information formulas:** lost in the flattening. The reading is Vinje and Gallant sparseness and empirical mutual information.
- **Go/NoGo window aggregate:** mean or maximum. The folds are taken as 5-fold stratified, as for the passive datasets.
- **Figure 2H window:** 0–5 s (legend) or 1–5 s (Methods).
- **Sliding-window width:** 250 ms (legends) or 500 ms (Methods), in Figures 2J and 3D/E.
- **Reliability analysis:** the baseline window (the 4 s or the 5 s before odor onset), per-trial or pooled baseline statistics, and "more than half" counted over all odor trials or per odor.
- **Latency and proportion responding:** the sample is per trial or per neuron.
- **Count reporting:** per session over days 1–3 or days 0–3 (Go/NoGo counts); first session or session mean per mouse (Figure S2B).
- **Classes for the classifiers:** two classes, or three including untagged neurons.
- **Figure 4I/J valence scheme:** read as unconstrained valence on correct trials.
- **CV of tracked neurons:** combinations of valence × phase or odor × phase, and SD over the absolute mean or the signed mean.
- **Transfer and stability tests:** the Mann-Whitney samples are matrix entries or per-mouse means; the block pairs are all pairs or pairs sharing the training day.
- **Undefined windows:** "earlier", "later", "anticipatory" and the Figure 3C window width.
- **Claims with no test given:** judged on direction only, and the file says so.
- **The paper's own tests:** several are unnamed. Two-sided Mann-Whitney U with Bonferroni correction is presumed and labelled as presumed.

**Missing from the paper:**
- **Tables 2 to 8** survive as titles only. Without Table 5 (transformer hyperparameters), Table 6 (held-out animal pairs) and Tables 7 and 8 (MLP search space and settings), the transformer and MLP claims are blocked as `methods_underspecified` until those tables are supplied. That covers the F1 scores, attention timing and latent separation. Tables 2 to 4 (odorants and concentrations) are not needed to test the claims.
- **The equations** for the measures above are lost in the flattening.
- **The mouse counts don't agree.** The Methods say 18 mice but list 9 OB-p and 8 mPFC-p (17), while Figure S2B has N = 9 OB-p and 10 mPFC-p.
- **The 30 Hz dataset** is marked "don't use for now" in the code's README.

Nothing was committed.

## End of run

22 turns, 6 minutes, result: success.
