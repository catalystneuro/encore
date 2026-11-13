# nishimoto-2011-reconstructing · claims · run 42867466578

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  grep -n "^#" docs/protocol.md | head -50; ls paper/; ls claims | head; wc -l paper/*
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "docs/protocol.md",
 "limit": 200
}
```

```
1	# Protocol for an attempt
2	
3	Version: `pilot-14`. Record this version in the attempt's provenance.
4	
5	This is what agents, or people, do to attempt a target and deposit the
6	result. A target is a dataset in a public archive and a paper it names. How
7	each archive's datasets are named, versioned and read is in
8	[archives.md](archives.md); the examples here are from DANDI, the first. It is written from the pilot attempts
9	([pilot notes](pilot-notes.md)); the reasons for the rules are there.
10	
11	An attempt has three roles, each a separate run with a separate context:
12	
13	- The **reader** reads the paper and writes the claims file: every finding,
14	  and how each is to be tested, taken from the paper. A second reader checks
15	  it against the paper. Readers never see the dataset's data.
16	- The **author** tests the claims on the dataset. It reads the paper to
17	  understand the claims, but the claims file binds it: it cannot change a
18	  claim's statement, expected values or criterion. A method detail the file
19	  lacks it takes from the paper, citing the passage, and it asks a reader
20	  only when it believes the file misreads the paper.
[... 180 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "claims/fouke-2025.yaml"
}
```

```
1	# Claims for Fouke, He, Loring & Naumann (2025) on dandiset 001453.
2	# Source: the accepted author manuscript in PubMed Central (PMC12218792), full text, read
3	# from its Results, figure legends and STAR Methods. The version of record is not open access.
4	#
5	# When these criteria were written, the author had seen the data check only: the file list,
6	# subject metadata, frame rates, units, trial structure and stimulus codes of every file, and
7	# the extent of positions. No claim's analysis had been run. The author had also read the
8	# outputs printed in the paper's own analysis notebook (Fig1-S1.ipynb, GitLab commit 33a5c29),
9	# which include per-stimulus median speeds and angular velocities and its statistics.
10	#
11	# The dandiset holds only the freely swimming tracking data of Figure 1 and Figure S1. Its
12	# stimulus codes 0 to 20 carry no names. The names come from the paper's code and from the
13	# stimulus software's protocol file (see stimulus-code-link), so the claims that need them
14	# use outside data and depend on that claim.
15	#
16	# Method choices fixed here, from the paper's Fig1-S1.ipynb where the Methods are silent: a
17	# trial is one stim_index; tracked frames only; positions smoothed with a Savitzky-Golay filter
18	# (21 frames, order 2); trials rejected when the absolute cumulative heading change exceeds
19	# 1000 degrees in the first 10 s or 2000 degrees in the first 35 s, or the mean speed exceeds
20	# 100 mm/s; measures taken from 3 s to 35 s after the first frame (the 3 s stationary phase is
[... 302 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "paper/10.1016-j.cub.2011.08.031.txt"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/vim-2.data-description.txt"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  cat papers/datasets/nishimoto-2011-reconstructing.yaml; git show --stat HEAD~1 | head; ls claims | grep -i crcns; grep -l "crcns" claims/*.yaml | head -3; sed -n 1,40p claims/drieu-2018.yaml
```

```
# The datasets this paper is tested on (docs/paper-first.md).
schema_version: 1
paper: doi:10.1016/j.cub.2011.08.031
title: Reconstructing Visual Experiences from Brain Activity Evoked by Natural Movies
datasets:
- archive: crcns
  id: vim-2
  relation: primary
commit 6e0c5baff11296ec269bf5a6b973420248658771
Author: github-actions[bot] <github-actions[bot]@users.noreply.github.com>
Date:   Tue Nov 10 12:37:12 2026 -0500

    Claims for drieu-2018, checked
    
    From attempt/drieu-2018, after its claims check said the file is ready (docs/pipeline.md).

 claims/drieu-2018.yaml | 1195 ++++++++++++++++++++++++++++++++++++++++++++++++
 1 file changed, 1195 insertions(+)
claims/asari-2009.yaml
claims/bruno-2017.yaml
[... 41 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 40,140p claims/drieu-2018.yaml; tail -30 claims/drieu-2018.yaml; python tools/claims_check.py --help 2>&1 | head -20
```

```
# - Firing curves on the linearized track, kernel method, 2.4 cm bins, Gaussian kernel
#   4.5 cm. A field is the set of contiguous bins holding the peak (peak at least 1 Hz in
#   Active, 0.7 Hz in Passive) with rate above 30% of the peak; a place cell is a pyramidal
#   cell with at least one field (Firing fields). Open: a minimum field size. Readings: (a)
#   none, as the Methods give none; (b) FiringCurve's default of 10 bins.
# - Theta cycles: start at peaks of the theta-band (6-10 Hz) filtered LFP; cycles shorter
#   than 80 ms or longer than 200 ms dropped; only runs of at least three contiguous cycles
#   kept (Theta power, frequency and cycles). Peaks and troughs for asymmetry and phase
#   precession from the LFP filtered at 1-40 Hz (Theta asymmetry and phase precession).
#   Open: the LFP channel. Readings: (a) one CA1 pyramidal-layer channel per rat with the
#   largest theta power; (b) the mean of the pyramidal-layer channels, as for ripples.
#   Open: how spike phase is assigned. Readings: (a) linear interpolation between the
#   1-40 Hz peaks (0) and troughs (pi); (b) Hilbert phase of the theta-band filtered LFP.
# - Bayesian decoding (Bayesian trajectory decoding): occupancy prior, Poisson likelihood,
#   trained on each travel session and applied to that session (theta sequences, windows
#   of pi/3, six per cycle) and to the following sleep (replay, 20 ms windows). Baseline
#   sleep is decoded with the model of the travel session whose post-sleep it is compared
#   with. Only events with at least three units, and candidate events lasting > 60 ms.
#   Position bins 2.4 cm, as for firing curves; ReconstructPosition's default of 200 bins
#   is a variant.
[... 121 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python -c "
import json;s=json.load(open('schemas/claims.schema.json'));print(json.dumps(s,indent=1)[:6000])"
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
  "paper",
  "claims"
 ],
 "properties": {
  "schema_version": {
   "const": 2
  },
  "dataset": {
   "description": "Before the cutover to paper-first records, the dataset a per-dataset claims file was read for. A paper's own claims file (claims/<paper>.yaml) leaves it out.",
   "type": "object",
   "additionalProperties": false,
   "required": [
[... 181 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python -c "
import json;s=json.load(open('schemas/claims.schema.json'));print(json.dumps(s,indent=1)[6000:12000])"; grep -rn "with_inputs" claims/*.yaml | head -5; grep -rn "data: elsewhere" -A2 claims/*.yaml | head -10
```

```
required": [
        "where"
       ]
      }
     }
    ]
   }
  },
  "checks": {
   "description": "Checks of the claims file against the paper by a second reader (docs/protocol.md, Reader, step 5), oldest first. The file is ready for an attempt when the last says so.",
   "type": "array",
   "items": {
    "type": "object",
    "additionalProperties": false,
    "required": [
     "date",
     "kind",
     "ready"
    ],
    "properties": {
[... 148 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && python -c "
import fitz;d=fitz.open('paper/10.1016-j.cub.2011.08.031.pdf');p=d[3];pix=p.get_pixmap(dpi=130);pix.save('p4.png')
d=fitz.open('paper/10.1016-j.cub.2011.08.031.supp.pdf');print(len(d));d[1].get_pixmap(dpi=110).save('s2.png');d[2].get_pixmap(dpi=110).save('s3.png')" && ls
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1016-j.cub.2011.08.031.pdf",
 "pages": "4"
}
```

Result: not kept, because it reads the paper's text.

**Agent**

I can't render the PDF pages here, so the figures stay unread and I'll work from the text alone. Writing the claims file now.

**Agent calls Write**

```json
{
 "file_path": "claims/nishimoto-2011-reconstructing.yaml",
 "content": "# Claims for Nishimoto, Vu, Naselaris, Benjamini, Yu & Gallant (2011), Current Biology 21,\n# 1641-1646, tested on CRCNS vim-2.\n# Written by an agent (model \"claude-opus-5-5\", Claude Code, runner \"GitHub Actions\"),\n# 2026-11-10, protocol pilot-14 as stated in docs/protocol.md.\n#\n# Text read: the version of record (main text, figure legends, Experimental Procedures) and\n# its Supplemental Information (Figures S1 and S2 with legends, Supplemental Experimental\n# Procedures). The PDF pages could not be rendered in this run, so no value was read off a\n# figure; every number below is printed in the text.\n#\n# Code read: none. The paper links no code, and none is named in the Experimental\n# Procedures or the supplement.\n#\n# Data the paper used (Results paragraph 4; Experimental Procedures; Supplemental Data\n# Preprocessing, Model Fitting, Voxel Selection): three subjects, S1, S2 and S3 (authors,\n# ages 30, 34 and 23), 4 T Varian scanner, TR 1 s, 2.0 x 2.0 x 2.5 mm voxels, 18 coronal\n# slices over posterior occipital cortex, collected over several sessions per subject.\n# Stimuli are color natural movies shown at 20 x 20 degrees and 15 Hz with a fixation spot.\n# Training set, 12 blocks of 10 min (7,200 s), each movie shown once; after discarding the\n# first 6 s of each block, 7,128 samples. Test set, 9 min of different movies repeated ten\n# times, cut in 1 min chunks; after discarding the first 6 s of each chunk, 486 samples.\n# About 15,000 occipital voxels, of which about 4,500 lie in the stimulated portions of V1,\n# V2, V3, V3A and V3B, assigned from retinotopic mapping done in separate sessions.\n# Measured variable: the BOLD signal per voxel, detrended per run with a third-degree\n# polynomial and z-scored. The data set's description (CRCNS vim-2) says it holds, per\n# subject, training responses (7,200 timepoints) and validation responses (540 timepoints,\n# averaged and per repeat) for the 64 x 64 x 18 volume, ROI masks, and the training and\n# validation stimuli at 128 x 128 pixels, RGB, 15 Hz. It holds neither the sampled natural\n# movie prior (about 18,000,000 s of YouTube clips), nor the 1,000,000-clip identification\n# set, nor the multifocal retinotopic mapping data; the paper gives no location for any of\n# them, so the claims that need them use outside data (data with_inputs) that may not exist\n# in public.\n#\n# Common methods, from the Supplemental Experimental Procedures unless stated; the criteria\n# refer to them by name.\n# - Motion-energy features (Motion-Energy Encoding Model; Gabor Wavelet Basis Set): frames\n#   downsampled to 96 x 96 pixels, converted to CIE L*A*B*, luminance kept; 6,555\n#   spatiotemporal Gabor filters at spatial frequencies 0, 2, 4, 8, 16 and 32 cycles/image,\n#   temporal frequencies 0, 2 and 4 Hz, eight directions (four orientations at 0 Hz, one\n#   filter at 0 cycles/image), on square grids with neighbours 3.5 s.d. of the spatial\n#   envelope apart, in quadrature pairs squared and summed; log-compressed; downsampled from\n#   15 Hz to 1 Hz; z-scored over time and clipped at 3 s.d. Open, and able to change the\n#   outcome: the size of the spatial and temporal Gaussian envelopes and the filter's\n#   temporal length. Reading: spatial s.d. proportional to the wavelength (a constant\n#   bandwidth in octaves) and a temporal window of about 10 frames, a standard choice;\n#   envelopes half and double that size are shown as variants. Open, and unlikely to\n#   change the outcome: the offset of the log (log(x) or log(1 + x)), how the 15 frames of a\n#   second are reduced to one sample (mean, or one frame), and whether the z-score uses the\n#   training and test features together or separately. Standard choices are log(1 + x),\n#   the mean, and training statistics applied to the test set.\n# - Static and nondirectional models (Gabor Wavelet Basis Set): the nondirectional model sums\n#   the outputs of opposite-direction filters at each position, orientation and temporal\n#   frequency; the static model keeps only the 0 Hz filters.\n# - Encoding model fit (Model Fitting): per voxel, the features at delays of 3, 4, 5 and\n#   6 s (4 samples), L1-regularized least squares (refs. 15 and 16, coordinate descent).\n#   Open, and able to change the outcome: how the L1 penalty, or the stopping point of the\n#   coordinate descent, is chosen. Readings: (a) chosen per voxel by prediction of a held-out\n#   10% of the training data in 50 s blocks, the split the paper uses for voxel selection;\n#   (b) chosen by cross-validation over the training data with several such splits.\n# - Prediction accuracy (Results paragraph 4): the correlation between predicted and\n#   observed BOLD signals on the test data. Open: whether the observed signal is the mean\n#   of the ten repeats or each repeat. Readings: (a) the repeat-averaged signal; (b) the mean\n#   over repeats of the single-repeat correlation.\n# - Voxel selection (Voxel Selection): for identification and reconstruction, per subject\n#   the 2,000 voxels of V1, V2, V3, V3A and V3B whose model, fit on 90% of the training data,\n#   best predicted the held-out 10% (50 s blocks chosen at random until 10% are held out).\n# - Likelihood (Likelihood Estimation): multivariate Gaussian on the selected voxels, with\n#   the noise covariance of the training residuals and its inverse estimated by Tikhonov\n#   regularization. Open: the size of the Tikhonov penalty. Reading: chosen by\n#   identification accuracy on the held-out 10% of the training data, with the result shown\n#   for a range of penalties. For reconstruction the model is refit with the single delay of\n#   4 s (Motion-Energy Encoding Model, last paragraph).\nschema_version: 2\npaper: doi:10.1016/j.cub.2011.08.031\nclaims:\n- id: fig2de-prediction-accuracy\n  statement: Averaged over subjects and voxels in V1, V2, V3, V3A and V3B, the prediction\n    accuracy on the test data is 0.24 for the static model, 0.39 for the nondirectional\n    motion-energy model and 0.40 for the directional motion-energy model, and the\n    differences are significant (Wilcoxon signed-rank test, p < 0.0001).\n  source: Results, paragraph 6; Figures 2D and 2E with legend\n  quote: The averaged accuracy across subjects and voxels in early visual areas (V1, V2, V3,\n    V3A, and V3B) was 0.24, 0.39, and 0.40 for the static, nondirectional, and directional\n    encoding models, respectively ... This difference in prediction accuracy was significant\n    (p < 0.0001, Wilcoxon signed-rank test)\n  statistics:\n  - about: directional against nondirectional and static models, voxel-wise\n    test: Wilcoxon signed-rank test\n    p: 0.0001\n    p_relation: \"<\"\n    n: voxels of V1, V2, V3, V3A and V3B in three subjects\n  expected:\n  - quantity: mean prediction accuracy, static model\n    value: 0.24\n    tolerance: 0.024\n  - quantity: mean prediction accuracy, nondirectional motion model\n    value: 0.39\n    tolerance: 0.039\n  - quantity: mean prediction accuracy, directional motion model\n    value: 0.40\n    tolerance: 0.04\n  criterion: The three models are built and fit as in Common methods (Motion-energy\n    features, Static and nondirectional models, Encoding model fit) and scored as in\n    Prediction accuracy. Open, and able to change the outcome, which voxels are averaged.\n    Readings, (a) every voxel of the V1, V2, V3, V3A and V3B masks; (b) the 2,000 voxels per\n    subject of Voxel selection; and how subjects are combined, (i) all voxels pooled, (ii)\n    the mean of the three subject means. The Wilcoxon signed-rank test is paired over\n    voxels; the paper does not say which pairs \"this difference\" covers, so the two\n    comparisons the Figure 2 legend names (directional against static, directional against\n    nondirectional) are both run. Reproduced when, under one reading, the three means are\n    within tolerance, their order is static < nondirectional < directional, and both tests\n    give p < 0.0001. Partially reproduced when the order and tests hold but a mean falls\n    outside its tolerance.\n- id: fig2e-directional-gain-small\n  statement: The directional model predicts better than the nondirectional model, but the\n    difference is small, so BOLD signals carry spatially localized but mostly nondirectional\n    motion information.\n  source: Results, paragraph 6; Figure 2E with legend; Figure S1A\n  quote: Note that the difference in prediction accuracy between the directional and\n    nondirectional motion models, though significant, was small\n  depends_on:\n  - fig2de-prediction-accuracy\n  criterion: From the fits of fig2de-prediction-accuracy, under the same readings.\n    Reproduced when the directional model's mean accuracy exceeds the nondirectional\n    model's, the paired Wilcoxon signed-rank test gives p < 0.0001, and the difference is\n    less than a tenth of the gain of the nondirectional model over the static model (the\n    paper's values give 0.01 against 0.15; the bound of a tenth is set here, as the paper\n    gives no number for small).\n- id: figs1a-motion-better-every-area\n  statement: In each of the five visual areas and each of the three subjects, both motion\n    models predict better than the static model, and the best predictions are in V1 for all\n    three subjects (Wilcoxon rank-sum test, p < 0.0001).\n  source: Figure S1A legend\n  quote: The directional and non-directional motion models perform better than the static\n    model in every case. The best overall predictions for all three subjects (p < 0.0001,\n    Wilcoxon rank-sum test) are obtained in area V1.\n  statistics:\n  - about: V1 against the other areas\n    test: Wilcoxon rank-sum test\n    p: 0.0001\n    p_relation: \"<\"\n    n: voxels per area, each of three subjects\n  depends_on:\n  - fig2de-prediction-accuracy\n  criterion: From the fits of fig2de-prediction-accuracy, mean accuracy per model, area and\n    subject (15 area and subject cells). Open, what V1 is compared with in the rank-sum\n    test. Readings, (a) V1 voxels against the voxels of each other area in turn; (b) V1\n    voxels against the voxels of the other four areas pooled; the directional model's\n    accuracy is used, as the model the main text calls best. Reproduced when both motion\n    models beat the static model in all 15 cells and, under one reading, V1 has the highest\n    mean with p < 0.0001 in all three subjects. Partially reproduced when the motion models\n    beat the static model in at least 12 of 15 cells or V1 is best in two subjects.\n- id: fig2fgh-retinotopic-receptive-fields\n  statement: Voxel receptive fields estimated from the motion-energy model are spatially\n    localized and retinotopically organized, and their angle and eccentricity maps are\n    similar to those from conventional multifocal mapping, except in the far periphery.\n  source: Results, paragraph 7; Figures 2F to 2I with legends\n  quote: The spatial receptive fields of individual voxels were spatially localized (Figures\n    2F and 2G, left) and were organized retinotopically (Figures 2H and 2I)\n  data: with_inputs\n  depends_on:\n  - fig2de-prediction-accuracy\n  criterion: Receptive fields from the directional model as in Selectivity Estimation\n    (Supplemental Experimental Procedures) - dynamic Gaussian white noise in each cell of a\n    17 x 17 grid, predicted response minus the response to uniform gray, and a 2D Gaussian\n    fit whose center gives angle and eccentricity; voxels with prediction accuracy p > 0.01\n    left out. The paper compares the maps with multifocal mapping data that the data set does\n    not hold and the paper does not deposit. Open, the p-value of prediction accuracy.\n    Readings, (a) the test of a correlation on the 486 test samples; (b) the same on the\n    held-out 10% of the training data. Without the mapping data the claim is judged on the\n    retinotopy the dataset's ROI masks imply. Reproduced when, in each subject, more than\n    half of the retained voxels have a Gaussian fit inside the 20 degree display, the\n    centers of left-hemisphere V1 voxels lie mostly (over 75%) in the right visual field\n    and the reverse for the right hemisphere, and eccentricity rises along V1 from the\n    occipital pole forward (positive correlation, p < 0.05). The thresholds are set here,\n    since the paper reports the maps visually. With the multifocal maps, a circular\n    correlation of angle and a correlation of eccentricity are reported as well.\n- id: fig2j-speed-eccentricity\n  statement: Optimal speed (peak temporal frequency over peak spatial frequency) correlates\n    positively with eccentricity, so peripheral voxels prefer higher speeds, in V1, V2 and V3\n    of all three subjects (t test for correlation coefficient, p < 0.0001).\n  source: Results, paragraph 8; Figure 2J; Figure S1B legend\n  quote: Projecting the optimal speed of the voxels onto a flattened map of the cortical\n    surface (Figure 2J) revealed a significant positive correlation between eccentricity and\n    optimal speed ... This pattern was observed in areas V1, V2, and V3 and for all three\n    subjects (p < 0.0001, t test for correlation coefficient\n  statistics:\n  - test: t test for correlation coefficient\n    p: 0.0001\n    p_relation: \"<\"\n    n: voxels of each of V1, V2 and V3 in each of three subjects\n  depends_on:\n  - fig2fgh-retinotopic-receptive-fields\n  criterion: Eccentricity from the receptive field fit of fig2fgh-retinotopic-receptive-fields.\n    Spatial and temporal frequency tuning from the directional model's predicted responses\n    to full-field drifting gratings at the basis set's directions, spatial and temporal\n    frequencies, averaged over directions, minus the response to uniform gray (Selectivity\n    Estimation). Spatial frequency in cycles per degree (cycles per image over 20 degrees).\n    Voxels with prediction accuracy p > 0.01, or with optimal spatial frequency 0, left out\n    (Figure S1B legend); the p-value readings are those of fig2fgh-retinotopic-receptive-fields.\n    Open, how the peaks are taken. Readings, (a) the spatial and temporal frequency of the\n    maximum of the joint tuning map; (b) the maximum of each marginal tuning curve. The\n    Pearson correlation of eccentricity with optimal speed is taken over voxels per area and\n    subject (the 2 degree bins of Figure S1B are for display). Reproduced when, under one\n    reading, all nine area and subject correlations are positive with p < 0.0001. Partially\n    reproduced when all nine are positive and at least six reach p < 0.0001.\n- id: fig3ab-identification-s1\n  statement: For subject S1 the motion-energy model identifies the test second that evoked an\n    observed BOLD pattern within one volume (1 s) 95% of the time (464 of 486 volumes), far\n    above chance (under 1%, 3 of 486).\n  source: Results, paragraph 9; Figures 3A and 3B with legends\n  quote: Our motion-energy encoding model could identify the specific movie stimulus that\n    evoked an observed BOLD signal 95% of the time (464 of 486 volumes) within 6 one volume\n    (1 s; subject S1; Figures 3A and 3B)\n  expected:\n  - quantity: S1 test volumes identified within one volume\n    value: 464\n    tolerance: 46.4\n    unit: volumes of 486\n  criterion: Voxel selection and the Likelihood of Common methods; for each observed test\n    volume, the log-likelihood under the predicted signal of each of the 486 test seconds,\n    and the second of maximum likelihood is chosen (Figure 3A legend); correct when it lies\n    within one volume of the true second. Open, which encoding model gives the predictions.\n    Readings, (a) the directional model with four delays; (b) the single 4 s delay refit\n    used for reconstruction. Also open, which 486 samples are used, as the paper discards the\n    first 6 s of each 1 min test chunk; the author takes the dataset's test samples that\n    match this. Reproduced when, under one reading, S1's count is within tolerance (at least\n    418 of 486); the chance level of 3 of 486 is reported.\n- id: fig3c-identification-large-set\n  statement: Identification accuracy within one volume stays above 75% for all three\n    subjects even when the candidate set holds 1,000,000 clips drawn at random from the\n    internet.\n  source: Results, paragraph 9; Figure 3C with legend\n  quote: Identification accuracy (within 6 one volume) was >75% for all three subjects even\n    when the set of possible natural movie clips included 1,000,000 separate clips chosen at\n    random from the internet\n  data: with_inputs\n  depends_on:\n  - fig3ab-identification-s1\n  criterion: As fig3ab-identification-s1, for each subject, with the candidate set enlarged\n    by 1 s clips from a natural movie database not used in the experiment. The paper gives\n    neither the database nor where it is; the author decides whether any public collection\n    of natural movies can stand in, as an assumption. Reproduced when, at a set of 1,000,000\n    clips, each subject is above 75% correct within one volume.\n- id: fig4-reconstructions\n  statement: Bayesian decoding with a sampled prior of about 18,000,000 s of internet movies\n    reconstructs the viewed movies; the maximum a posteriori (MAP) clip is good when the prior\n    holds similar clips and poor otherwise, and the average of the 100 highest posterior\n    clips (AHP) captures the spatiotemporal structure even of unique clips.\n  source: Results, paragraphs 10 and 11; Figure 4A to 4C with legend; Figure S2\n  quote: When the sampled natural movie prior contained clips similar to the viewed clip, the\n    MAP reconstructions were good ... However, when the prior contained no clips similar to\n    the viewed clip, the reconstructions are poor ... The AHP reconstruction captures the\n    spatiotemporal structure within a viewed clip even when it is completely unique\n  data: with_inputs\n  depends_on:\n  - fig3ab-identification-s1\n  criterion: The paper shows this with example frames only, and judges it by the measure of\n    fig4d-reconstruction-accuracy, on which this claim is judged. It needs the sampled prior,\n    which the data set does not hold and the paper does not deposit.\n- id: fig4d-reconstruction-accuracy\n  statement: For all three subjects both MAP and AHP reconstructions correlate with the viewed\n    movies in motion-energy space above chance (Wilcoxon rank-sum test, p < 0.0001), and AHP\n    reconstructions are better than MAP (Wilcoxon signed-rank test, p < 0.0001), though\n    still crude (motion-energy correlation about 0.3).\n  source: Results, paragraph 12; Figure 4D with legend; Supplemental Experimental Procedures,\n    Evaluating the Accuracy of Reconstructions\n  quote: In both cases, reconstruction accuracy was significantly higher than chance (p <\n    0.0001, Wilcoxon rank-sum test; see Supplemental Experimental Procedures). Furthermore,\n    AHP reconstructions were significantly better than MAP reconstructions (p < 0.0001,\n    Wilcoxon signed-rank test).\n  statistics:\n  - about: MAP and AHP reconstructions against random prior clips\n    test: Wilcoxon rank-sum test\n    p: 0.0001\n    p_relation: \"<\"\n    n: 1 s test clips, each of three subjects\n  - about: AHP against MAP reconstructions\n    test: Wilcoxon signed-rank test\n    p: 0.0001\n    p_relation: \"<\"\n    n: 1 s test clips, each of three subjects\n  expected:\n  - quantity: motion-energy correlation of the reconstructions\n    value: 0.3\n    tolerance: 0.03\n  data: with_inputs\n  depends_on:\n  - fig3ab-identification-s1\n  criterion: Posterior over the sampled prior from the Likelihood of Common methods with the\n    single 4 s delay model, using BOLD 4 s after each 1 s clip; the MAP is the clip of\n    highest posterior; the AHP is the average of the 100 highest, each clip's pixels scaled\n    to unit s.d. before averaging and the average rescaled to the mean and s.d. of the top\n    100 (Figure S2D legend), with the five seconds after a chosen clip of the same movie\n    excluded from selection (Additional Notes on Reconstruction). Accuracy per 1 s clip is\n    the correlation of motion-energy vectors (filter bank up to downsampling, no\n    hemodynamics) of the viewed and reconstructed clip. Chance is the correlation with clips\n    drawn at random from the prior; the dashed line is its 99th percentile. Open, which\n    value \"about 0.3\" describes. Readings, (a) the AHP mean per subject; (b) the larger of\n    the MAP and AHP means per subject. Reproduced when, in each subject, both tests give\n    p < 0.0001 with AHP above MAP, and under one reading the values are within tolerance.\n    The prior is not in the data set and has no given location; the author decides whether\n    a stand-in prior is defensible, as an assumption, or blocks the claim.\n- id: discussion-color-no-gain\n  statement: In preliminary work, encoding models with explicit color information did not\n    predict or identify better than models using luminance alone.\n  source: Discussion, paragraph 4\n  quote: However, we found that color information did not improve the accuracy of predictions\n    or identification beyond what could be achieved with models that include only luminance\n    information.\n  depends_on:\n  - fig2de-prediction-accuracy\n  criterion: The paper shows no data and does not describe its color models. Reading, the\n    directional model of fig2de-prediction-accuracy with the same filter bank applied as\n    well to the A* and B* channels of CIE L*A*B*, fit and scored the same way. A claim of\n    absence, for which the paper names no test; the test is set here, the paired Wilcoxon\n    signed-rank test over voxels of fig2de-prediction-accuracy at p < 0.0001. Reproduced\n    when the color model's mean accuracy is not higher by that test; the difference is\n    reported either way, and the outcome rests on the reading of the color model.\n"
}
```

```
File created successfully at: claims/nishimoto-2011-reconstructing.yaml (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd  python tools/claims_check.py claims/nishimoto-2011-reconstructing.yaml paper/10.1016-j.cub.2011.08.031.txt; grep -n ": .*: " claims/nishimoto-2011-reconstructing.yaml | grep -v "^[0-9]*:#" ; grep -c "—" claims/nishimoto-2011-reconstructing.yaml; grep -ci rather claims/nishimoto-2011-reconstructing.yaml
```

Result: not kept, because it reads the paper's text.

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/nishimoto-2011-reconstructing.yaml",
 "old_string": "    encoding models, respectively ... This difference in prediction accuracy was significant",
 "new_string": "    encoding models, respectively ... difference in prediction accuracy was significant"
}
```

```
The file claims/nishimoto-2011-reconstructing.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd  python tools/claims_check.py claims/nishimoto-2011-reconstructing.yaml paper/10.1016-j.cub.2011.08.031.txt; git status --short
```

Result: not kept, because it reads the paper's text.

**Agent**

I wrote `claims/nishimoto-2011-reconstructing.yaml`. The quote checker passes: 10 claims, 10 quotes, 5 statistical values, 0 problems. Nothing is committed.

**Text read:** the version of record (main text, figure legends, Experimental Procedures) and its Supplemental Information (Figures S1 and S2 with legends, Supplemental Experimental Procedures). Rendering the PDF pages failed, so I read no values off figures; every number comes from the text. The paper links no code and names none, so I read no code.

**Claims:** 10 claims, all with quotes. Five carry statistics entries (Wilcoxon signed-rank, Wilcoxon rank-sum, and the t test for a correlation coefficient, all p < 0.0001). Three have expected values:
- prediction accuracy of 0.24, 0.39 and 0.40 for the static, nondirectional and directional models;
- identification of 464 of 486 volumes for subject S1;
- reconstruction correlation of about 0.3.

Every claim has a criterion. Six can be tested on the dataset:
- prediction accuracy;
- the small gain of the directional model over the nondirectional one;
- motion models beat the static model in every area, with V1 best;
- optimal speed rises with eccentricity;
- identification for S1;
- color adds nothing (from the Discussion, with no data shown).

Four claims need outside data (`with_inputs`):
- the retinotopic maps, which the paper compares with multifocal mapping data;
- identification with 1,000,000 clips;
- the reconstructions;
- reconstruction accuracy.

**Details left open, and the readings named:**
- **Gabor envelope sizes and filter length:** a standard constant-bandwidth choice with about 10 frames, plus variants at half and double size. Smaller items (the log offset, how 15 frames become one sample, the z-score data) get standard choices.
- **How the L1 penalty or stopping point is chosen:** (a) a held-out 10% of training data in 50 s blocks; (b) cross-validation over the training data.
- **Observed test signal:** (a) the mean of the ten repeats; (b) correlation with each repeat, averaged.
- **Voxels averaged for accuracy:** (a) all ROI voxels; (b) the 2,000 selected voxels. Subjects are either (i) pooled or (ii) averaged as subject means.
- **Which pairs the signed-rank test covers:** both comparisons in the Fig. 2 legend are run.
- **What V1 is compared with in the rank-sum test:** (a) each other area in turn; (b) the other four areas pooled.
- **The p-value for "accuracy p > 0.01":** (a) on the test data; (b) on the held-out training data.
- **How peak frequencies are taken:** (a) the maximum of the joint map; (b) the maximum of each marginal curve.
- **Model used for identification:** (a) four delays; (b) the single 4 s delay.
- **Tikhonov penalty:** chosen on held-out training data, with a range shown.
- **What "about 0.3" refers to:** (a) the AHP mean per subject; (b) the larger of the MAP and AHP means.
- **The color model:** read as the same filter bank applied to the A* and B* channels as well. The paper names no test, so I set one.

Two thresholds are set by me, not the paper, and each criterion says so: "small" for the directional gain is taken as less than a tenth of the nondirectional gain, and the retinotopy thresholds are mine because the paper only shows the maps.

**Missing from the paper:**
- **Outside data:** the sampled movie prior (about 18,000,000 s of YouTube clips), the 1,000,000-clip identification set and the multifocal mapping data are neither deposited nor located. The four claims that need them may have to be blocked.
- **Data mismatch:** the paper gives sample counts of 7,128 and 486, while the data description lists 7,200 and 540 timepoints. Matching the two is left to the author.

## End of run

16 turns, 3 minutes, $1.05 at API prices, result: success.
