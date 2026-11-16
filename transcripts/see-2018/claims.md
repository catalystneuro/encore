# see-2018 · claims · run 42945138568

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  grep -n "^#" docs/protocol.md | head -50; ls paper/ claims/ | head; ls paper | grep -i see
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  sed -n 1,198p docs/protocol.md; ls paper | head; ls paper/see* 2>/dev/null; find paper -iname "*see*"
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  cat claims/fouke-2025.yaml | head -150; wc -l paper/*; cat papers/datasets/see-2018.yaml; cat paper/ac-3.data-description.txt | head -60
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.7554-elife.35587.txt"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.7554-elife.35587.txt",
 "offset": 144,
 "limit": 160
}
```

Result: not kept, because it reads the paper's text.

**Agent**

I've read the Results; reading the Methods now.

**Agent calls Read**

```json
{
 "file_path": "paper/10.7554-elife.35587.txt",
 "offset": 304,
 "limit": 170
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  sed -n 150,400p claims/fouke-2025.yaml | grep -nE "^\s*(- id|kind|data|inferred|code|outside|elsewhere|depends|deviation|open)" | head -40; ls docs; grep -rl "schema" docs tools | head; sed -n 1,60p tools/claims_check.py
```

```
1:  data: with_labels
2:  depends_on:
9:- id: fig1h-zf-higher-angular-acceleration
20:  data: with_labels
21:  depends_on:
33:- id: figs1e-dc-respond-less-monocular
39:  data: with_labels
40:  depends_on:
49:- id: fig1c-continuous-vs-bouts
63:- id: fig1cef-representative-values
74:- id: fig2d-shared-architecture
81:- id: fig2g-dsi-similar
91:- id: fig2h-fewer-motion-responsive
101:- id: fig2k-more-monocular
111:- id: fig2l-bi-ratio
121:- id: fig3e-longer-swims
131:- id: fig3cd-zf-turn-more
148:- id: fig4f-longer-on-duration
160:- id: fig4hi-vspn-lateralized
agents
[... 81 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python -c "
import json;s=json.load(open('schemas/claims.schema.json'));print(json.dumps(s,indent=1)[:6000])"; head -c 300 paper/*.xlsx | od -c | head -3
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  python -c "
import json;s=json.load(open('schemas/claims.schema.json'));print(json.dumps(s['\$defs'],indent=1)[:5000]); print(list(s['properties']))"; ls claims | wc -l; grep -l "crcns" claims/*.yaml | head -3
```

```
{
 "expected": {
  "type": "object",
  "additionalProperties": false,
  "required": [
   "quantity",
   "value"
  ],
  "properties": {
   "quantity": {
    "type": "string"
   },
   "value": {
    "type": "number"
   },
   "tolerance": {
    "type": "number",
    "minimum": 0
   },
   "unit": {
[... 87 more lines not kept]
```

**Agent calls Bash**

```bash
cd  head -30 claims/asari-2009.yaml; timeout 60 git ls-remote https://github.com/mackelab/CorBinian HEAD 2>&1 | head
```

```
# Claims for Asari & Zador (2009), J Neurophysiol 102:2638-2656, on CRCNS ac-1.
# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"), 2026-11-10,
# protocol pilot-14 as stated in docs/protocol.md. The writer did not look at the dataset's data or
# files; only its description on crcns.org (paper/ac-1.data-description.txt) was read.
#
# Text read: the version of record, as a text extraction of the publisher's PDF (PyMuPDF), with
# the PDF. The extraction garbles some symbols (Greek letters, "<", ">", "~", "=" and "+/-" print
# as a replacement glyph); they were read from context, and quotes are cut around them. The PDF
# pages could not be rendered in this run, so figure axes were not read; every value used here is
# printed in the text or a legend. The online supplement (Supplemental Figures S1 to S10) was not
# supplied and was not read. The main findings rest on the main-text Figures 2 to 9 and their
# legends; the supplement holds example traces (S2 to S10) and the "silence probe" analysis (S1),
# whose one claim (figs1-silence-probe) is quoted from the Methods only.
#
# Code read: none. The paper links no code; it says all analysis was done in MATLAB.
#
# Data the paper used. Long-Evans rats, 20 to 28 days old, anesthetized with ketamine and
# medetomidine; in vivo blind patch recordings sampled at 10 kHz.
# - A1 current clamp (whole cell): 194 cells in 139 animals, of which 123 met the analysis
#   criterion (at least 4 repeats of a probe tested with at least 2 conditioning stimuli). By
[... 11 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && timeout 120 git clone -q --depth 1 https://github.com/mackelab/CorBinian && cd CorBinian && git log -1 --format="%H %ad" && ls && ls */ | head -50 && grep -ril "dichgauss\|DichGauss" --include=*.m . | head
```

```
8ebb12dec79e55ea7efc877e5b95bf95e8680a50 Mon Jul 26 14:37:04 2021 +0200
CONTRIBUTING.md
LICENSE.md
README.md
base_dir.m
demo
dich_gauss
maxent
startup.m
third_party
util
demo/:
base_dir.m
demo_MPF.m
demo_all.m
demo_bwVK.m
demo_dich_gauss_01.m
demo_dich_gauss_bivar_bayes.m
demo_dich_gauss_counts.m
demo_dich_gauss_temporal_correlations.m
[... 47 more lines not kept]
```

**Agent**

The paper links only CorBinian (the dichotomized Gaussian implementation); no analysis code. Checking its two DG functions, then writing the file.

**Agent calls Bash**

```bash
cd $TMPDIR/CorBinian/dich_gauss; head -30 findLatentGaussian01.m; head -25 sampleDichGauss01.m
```

```
function [gamma,Lambda] = findLatentGaussian(mu,Sigma,acc)

% function [gamma,Lambda] = findLatentGaussian(mu,Sigma,acc)
% 	Compute mean gamma and covariance Lambda for the hidden Gaussian random vector Z generating the
% 	binary Bernoulli vector X with mean mu and covariances Sigma according to
%     X = 0 <==> Z < 0
%     X = 1 <==> Z > 0
%
% Usage: [gamma,Lambda] = findLatentGaussian([0.5 0.5],[0.25 0.1; 0.1 0.25])
%
% Code from the paper: 'Generating spike-trains with specified
% correlations', Macke et al., Neural Computation
%
%note: does NOT ensure that the matrix Lambda is positive definite, if oyu
%want to do this, need to use the higham-correction.


% parameter check
if any(mu < 0 | mu >= 1)
    error('mean has to be in (0,1)')
[... 36 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 60,113p paper/ac-3.data-description.txt
```

Result: not kept, because it reads the paper's text.

**Agent**

I have what I need. Writing the claims file now.

**Agent calls Write**

```json
{
 "file_path": "claims/see-2018.yaml",
 "content": "# Claims for See, Atencio, Sohal & Schreiner (2018), eLife 7, e35587, on CRCNS ac-3.\n# Written by an agent (model \"claude-opus-5-5\", Claude Code, runner \"GitHub Actions\"), 2026-11-11,\n# protocol pilot-14 as stated in docs/protocol.md. The writer did not look at the dataset's data or\n# files; only its description on crcns.org (paper/ac-3.data-description.txt) was read, for what\n# the dataset is meant to hold.\n#\n# Text read: the version of record (PMC6017807, Europe PMC full-text XML, flattened), with its\n# figure legends, figure supplement legends and Materials and methods; and Supplementary file 1\n# (elife-35587-supp1-v2.xlsx, the table of statistical tests with test, N and exact p for each\n# panel), which the text file reproduces at its end. No PDF was supplied; every value used here is\n# printed in the text, a legend or Supplementary file 1. Figure axes were not read.\n#\n# Code read: the paper links one repository, the dichotomized Gaussian (DG) implementation of\n# Macke et al., https://github.com/mackelab/CorBinian, read at commit 8ebb12d (2021-07-26; the\n# paper cites the 2017 state, which is not pinned). It holds the DG fit (findLatentGaussian01.m)\n# and sampler (sampleDichGauss01.m) for binary vectors with given means and covariances. The\n# paper's own analysis code (MATLAB) is not linked; the PCA/ICA code was supplied privately by\n# Lopes-dos-Santos (Acknowledgements). The dataset's sample STRF code is the dataset's, not the\n# paper's, and was not read.\n#\n# Data the paper used. Female Sprague-Dawley rats, 2 to 3 months, ketamine/xylazine anesthesia.\n# Right primary auditory cortex (AI), penetrations perpendicular to the surface.\n# - 16 columnar penetrations with a 32-channel probe (NeuroNexus a1x32-poly3, to about 800 um),\n#   20 kHz, Bayesian spike sorting; 655 single units in total. Stimulus a 10-min continuous\n#   dynamic moving ripple (DMR) or ripple noise (RN, the sum of 16 DMRs), 500 Hz to 40 kHz. Each\n#   penetration used one of the two stimuli. These give Figures 1 to 7, 9, 10 and 11C to F.\n# - 5-s frozen segments of DMR or RN, repeated 50 times with 0.5 s silence (Figures 9 and its\n#   supplements; 330 cNE and neuron pairs in Figure 9C).\n# - 15 repetitions of the 10-min RN stimulus, from which 24 units with stable rates were kept\n#   (Figure 11A, B; also the 'repeat' CR of Figure 11E, F).\n# - 8 recordings with a 64-channel probe (Cambridge NeuroTech H3, to about 1400 um), MountainSort,\n#   with contiguous epochs of spontaneous activity and DMR-evoked activity (Figure 8).\n# Measured variables are spike times per unit, the channel position and depth of each unit, the\n# stimulus envelopes and the triggers. The dataset descriptor (version 0.6, March 2018) lists unit\n# spike times with channel, depth and position, triggers, and the rn1 and rn16 stimulus matrices;\n# which of the experiments above it holds is the author's to find.\n#\n# The cNE detection used throughout (\"cNE detection\" in the criteria), from Materials and methods,\n# Detection of coordinated neuronal ensembles, and Results, Identification of cNEs. Spikes binned\n# at 10 ms, each unit's binned train z-scored; PCA of the correlation matrix; eigenvalues above\n# the upper Marcenko-Pastur bound are significant and their number is the number of cNEs; fastICA\n# (negentropy) on the significant eigenvectors gives one IC per cNE; cNE activity is the\n# projection of the IC onto the z-scored spike matrix. Membership is an IC weight beyond 1.5 SD\n# above or below the mean of the distribution of IC weights from 100 independently circularly\n# shuffled spike matrices (ICA run on the N largest eigenvectors of each, N the number found in\n# the real data). A cNE is active where its activity exceeds the 99.9th percentile of the\n# activity of the real ICs projected onto the shuffled matrices.\n# Details of the detection the paper does not fix, with the readings it allows.\n# - The Marcenko-Pastur upper bound is taken as (1 + sqrt(n/T))^2 for n units and T bins, the\n#   standard bound of Lopes-dos-Santos et al. (2013) for z-scored data; the paper names only the\n#   distribution.\n# - IC scale and sign are open. Readings (a) each IC scaled to unit length and its sign set so the\n#   largest absolute weight is positive, as in Lopes-dos-Santos et al. (2013); (b) ICs as fastICA\n#   returns them, unit length, sign unchanged. The sign matters for the negative-weight count.\n# - The activity projection is open. Readings (a) the quadratic form z(t)' P z(t) with P the outer\n#   product of the IC and its diagonal set to zero, as in Lopes-dos-Santos et al. (2013); (b) the\n#   linear projection w . z(t).\n# - fastICA settings (nonlinearity, initial values, iterations) and the shuffle seeds are standard\n#   choices; the paper names only fastICA based on negentropy.\n# - What a cNE event is, once activity crosses threshold, is open. Readings (a) every 10-ms bin\n#   above threshold; (b) one event per contiguous run of bins above threshold, at its peak.\nschema_version: 2\npaper: doi:10.7554/elife.35587\nclaims:\n- id: fig2bd-pwc-measures-covary\n  statement: Across all penetrations, the sharpness and peak delay of pairwise correlation (PWC)\n    functions covaried with the pairs' spike train correlation coefficients, accounting for about\n    50% of the variance.\n  source: Results, Heterogeneous functional connectivity between columnar AI neurons, paragraph 2;\n    Figure 2B to D\n  quote: Across all penetrations, PWCs were fairly heterogeneous but sharpness and delay covaried\n    with correlation coefficients, accounting for ~50% of the variance\n  expected:\n  - quantity: R2 of PWC sharpness against spike train correlation coefficient\n    value: 0.5\n    tolerance: 0.05\n  - quantity: R2 of PWC peak delay against spike train correlation coefficient\n    value: 0.5\n    tolerance: 0.05\n  criterion: All pairs of simultaneously recorded units in the 16 penetrations. The correlation\n    coefficient is Pearson's correlation of the spike trains binned at 10 ms (Results, same\n    paragraph). Peak delay is the absolute lag of the PWC maximum; sharpness is the half-count\n    width of the PWC folded around its peak (Results, Synchrony between cNE members, paragraph\n    2; Figure 6G to I legend). R2 is that of a least-squares line. Open, as the paper does not\n    fix them, are the PWC lag bin and lag range, and the axes of the fit. Readings (a) 1-ms lag\n    bins over plus or minus 50 ms; (b) 1-ms bins over plus or minus 100 ms; each with the fit on\n    linear axes and on log axes. Reproduced when, under one reading, both R2 values are within\n    tolerance; partially reproduced when one is.\n- id: fig2eg-distance-weak\n  statement: The correlation between the pairwise synchrony measures (sharpness, peak delay,\n    correlation coefficient) and the distance between the pair's channels explained only about\n    10 to 30% of the variance.\n  source: Results, Heterogeneous functional connectivity between columnar AI neurons, paragraph\n    3; Figure 2E to G\n  quote: We observed similar trends in columnar recordings, although the correlation between these\n    synchrony aspects and pairwise distance only explained ~10–30% of the total variance\n  depends_on:\n  - fig2bd-pwc-measures-covary\n  expected:\n    quantity: R2 of each synchrony measure against pairwise distance (range)\n    value: 0.2\n    tolerance: 0.13\n  criterion: The three measures of fig2bd-pwc-measures-covary, each regressed on the pairwise\n    distance across all pairs of the 16 penetrations. The claim is a range, so it holds when each\n    R2 lies within 0.09 to 0.33 (10 to 30%, each bound widened by 10%); the expected entry above\n    records the centre and half-width of that interval. Pairwise distance is open. Readings (a)\n    the difference in depth ('position') between the two units' channels; (b) the Euclidean\n    distance between the channels on the three-column probe layout. Under each PWC reading of\n    fig2bd-pwc-measures-covary. Reproduced when all three R2 lie in the interval under one\n    reading; partially reproduced when one or two do.\n- id: fig4-example-nine-cnes\n  statement: In an example columnar recording with 38 isolated neurons, the cNE detection found\n    nine cNEs, with 2 to 6 member neurons each.\n  source: Results, Identification of coordinated neuronal ensembles (cNEs), paragraph 2; Figure 4B\n  quote: Applying this cNE detection algorithm to an actual AI columnar recording with 38 isolated\n    neurons ( Figure 4D ), we identified nine separate cNEs ( Figure 4B ) with significantly\n    contributing members ranging from 2 to 6 neurons\n  expected:\n  - quantity: number of cNEs in the 38-neuron penetration\n    value: 9\n    tolerance: 1\n  - quantity: smallest cNE size\n    value: 2\n    tolerance: 0\n  - quantity: largest cNE size\n    value: 6\n    tolerance: 1\n  criterion: The penetration with 38 units, with cNE detection as in the opening comment. The\n    tolerance on counts is one, 10% of a small integer rounded up; the smallest size of 2 is the\n    least a cNE can have. If more than one penetration has 38 units, each is reported and the\n    claim holds when one matches. Under each reading of IC scale and sign.\n- id: fig4s2-interleaved-halves-stable\n  statement: cNEs detected independently in two interleaved halves of a recording were the same,\n    with about 96% of the ICs of one half having a significant match in the other.\n  source: Results, Identification of coordinated neuronal ensembles (cNEs), paragraph 4; Figure\n    4—figure supplement 2\n  quote: Approximately 96% of independent components had significant matches ( Figure 4—figure\n    supplement 2D and E ), indicating that the two interleaved parts of the recording contained\n    the same independent components\n  expected:\n    quantity: percentage of ICs (of both halves) with a significant match\n    value: 96\n    tolerance: 9.6\n    unit: '%'\n  criterion: Each of the 16 recordings split into 10 equal parts, the odd parts forming half A and\n    the even parts half B; cNE detection on each. IC A against IC B by the absolute correlation of\n    their weights. The null distribution comes from spike trains circularly shuffled and run\n    through the detection, its ICs correlated; the threshold is its 99th percentile, per\n    penetration (Results, same paragraph; legend). Open, the paper does not fix them, are the\n    number of shuffles, which ICs the shuffled ones are correlated with, and what counts as a\n    match. Readings (a) 100 shuffles, as for membership, shuffled ICs of one half correlated with\n    shuffled ICs of the other; (b) 100 shuffles, real ICs of one half correlated with shuffled\n    ICs of the other; with a match being, for each IC, its largest absolute correlation with any\n    IC of the other half above the threshold. The percentage pools IC As and IC Bs over all\n    penetrations (legend E). Reproduced when one reading is within tolerance.\n- id: fig4s3-train-test-83pct\n  statement: cNEs detected in the first half of a recording predicted cNE activity in the second\n    half; of 102 training cNEs, about 83% had significant matches to test cNE activity.\n  source: Results, Identification of coordinated neuronal ensembles (cNEs), paragraph 5; Figure\n    4—figure supplement 3E\n  quote: Across all penetrations, approximately 83% of training cNE activity had significant\n    matches to test cNE activity\n  expected:\n  - quantity: number of training cNEs, all penetrations\n    value: 102\n    tolerance: 10.2\n  - quantity: percentage of training cNEs with a significant match\n    value: 83\n    tolerance: 8.3\n    unit: '%'\n  criterion: Each recording split into a first half (training) and second half (test); cNE\n    detection on each; both sets of ICs projected onto the test half to give training and test\n    activities, which are correlated pairwise. For each training cNE the largest correlation is\n    its matched correlation; all other correlations of all penetrations pooled form the null, and\n    its 95th percentile is the threshold (Results, same paragraph; legend C). Under each reading\n    of the activity projection. Reproduced when both values are within tolerance under one\n    reading; partially reproduced when the percentage is and the count is not.\n- id: fig5a-mi-peaks-10-15ms\n  statement: The mutual information between cNE STRFs and the stimulus peaked at bin sizes of\n    about 10 to 15 ms.\n  source: Results, cNE identity is dependent on time bin size, paragraph 2; Figure 5A\n  quote: Receptive field information peaked at bin sizes of approximately 10–15 ms ( Figure 5A )\n  criterion: Method from Materials and methods, STRF mutual information. cNE detection at bin\n    sizes 2, 5, 8, 10, 15, 20, 35 and 50 ms; activity interpolated to 1 ms; per cNE a threshold\n    giving 5000 events; STRF by event-triggered average; MI between STRF projections and events,\n    from P(x|event) and P(x) of the projections z-scored, extrapolated to infinite data by a line\n    through the means of 20 subsamples at 90, 95, 97.5, 99 and 100% of events against the\n    inverse fraction. Open are the STRF time window, the number of projection bins, and how MI\n    is summarised over cNEs at a bin size. Readings for the summary (a) mean over all cNEs; (b)\n    median over all cNEs; the window and bins are taken as standard choices and stated.\n    Reproduced when, under one summary reading, the largest value falls at 10 or 15 ms.\n- id: fig5b-number-decreases-with-bin\n  statement: The number of detected cNEs decreased as the bin size increased.\n  source: Results, cNE identity is dependent on time bin size, paragraph 3; Figure 5B\n  quote: we found that as the spike train temporal bin size increased, the number of recovered\n    cNEs decreased ( Figure 5B )\n  criterion: cNE detection on the 16 penetrations at the bin sizes of fig5a-mi-peaks-10-15ms. The\n    paper reports no test. Read as a trend, the number of cNEs (mean over penetrations) has a\n    negative Spearman correlation with bin size over the eight sizes and is lower at 50 ms than\n    at 2 ms; this test is a reading of \"decreased\", not the paper's.\n- id: fig5c-size-increases-with-bin\n  statement: The mean number of member neurons per cNE increased as the bin size increased.\n  source: Results, cNE identity is dependent on time bin size, paragraph 3; Figure 5C\n  quote: the number of member neurons in each cNE increased ( Figure 5C )\n  criterion: As fig5b-number-decreases-with-bin, for the mean cNE size (mean over penetrations of\n    the mean size per penetration), with the signs reversed. The test is a reading of\n    \"increased\", not the paper's.\n- id: fig6c-spike-pwc-narrower-than-strf-pwc\n  statement: For pairs of neurons in the same cNE, spike train PWCs were much narrower than the\n    PWCs of their STRFs' temporal profiles, while for pairs not in the same cNE the spike train\n    PWCs were often as wide as the STRF PWCs.\n  source: Results, Synchrony between cNE members cannot be fully explained by receptive field\n    overlap, paragraph 1; Figure 6A to F\n  quote: Comparing STRF PWCs to spike train PWCs ( Figure 6A–6F ) revealed that the spike train\n    PWCs ( Figure 6C , histogram) were much narrower than the STRF PWCs ( Figure 6C , solid line)\n    for neuronal pairs within the same cNE. In contrast, for non-cNE pairs, the spike train PWCs\n    were often as wide as the STRF PWCs\n  depends_on:\n  - fig6j-sharpness-cne-pairs\n  criterion: The paper shows one example of each kind and reports no population test. The STRF\n    temporal profile is the STRF averaged over frequency at each delay (Figure 6B, E legend); the\n    STRF PWC is the cross-correlation of the two profiles; its sharpness is measured as for spike\n    PWCs. Read over all pairs of the 16 penetrations, the claim holds when the spike PWC is\n    sharper than the STRF PWC for more than half of cNE pairs, and the ratio of spike to STRF PWC\n    sharpness is lower for cNE pairs than for non-cNE pairs (Mann-Whitney U, p < 0.05, the test\n    of Figure 6J). \"Most\" and the ratio comparison are readings of \"much narrower\" and \"often as\n    wide\", not the paper's.\n- id: fig6j-sharpness-cne-pairs\n  statement: In every penetration, spike train PWCs were significantly sharper (narrower) for\n    pairs of neurons in the same cNE than for pairs not in the same cNE.\n  source: Results, Synchrony between cNE members cannot be fully explained by receptive field\n    overlap, paragraph 2; Figure 6J; Figure 6—figure supplement 1; Supplementary file 1\n  quote: The PWCs were significantly narrower for cNE pairs than for non-cNE pairs (p < 0.001,\n    Mann-Whitney U test; Figure 6J ; see Figure 6—figure supplement 1 for each of the other\n    penetrations)\n  statistics:\n  - about: example penetration, Figure 6J\n    test: Mann-Whitney U test\n    p: 1.69e-23\n    n: 73 cNE pairs and 331 non-cNE pairs\n  - about: each of the other 15 penetrations, Figure 6—figure supplement 1\n    test: Mann-Whitney U test\n    p: 0.001\n    p_relation: <\n    n: 15 penetrations, from 10 and 104 to 365 and 295 pairs (Supplementary file 1)\n  criterion: Sharpness as in fig2bd-pwc-measures-covary (half-count width of the PWC folded at its\n    peak), under each of its lag readings. A cNE pair is two members of the same cNE; a non-cNE\n    pair is two units of the penetration that share no cNE. Per penetration, a two-sided\n    Mann-Whitney U test. Reproduced when cNE pairs are sharper with p < 0.001 in all 16\n    penetrations under one reading; partially reproduced when in at least 12.\n- id: fig6-member-pwc-sharpness-delay\n  statement: PWCs between members of the same cNE are sharp, with a median sharpness of about 2 ms,\n    a mean sharpness of 3.39 +/- 1.21 ms and a mean absolute peak delay of 0.76 +/- 1.74 ms.\n  source: Results, Synchrony between cNE members cannot be fully explained by receptive field\n    overlap, paragraph 2; Results, cNE events are not fully accounted for by stimulus\n    synchronization, paragraph 5\n  quote: The median PWC sharpness for member neurons was ~2 ms ... since PWCs between pairs of\n    neurons in the same cNE are sharp, with mean sharpness values of 3.39 ± 1.21 ms ( Figure\n    6G–6J , Figure 6—figure supplement 1 ), and mean absolute peak delays of 0.76 ± 1.74 ms\n  depends_on:\n  - fig6j-sharpness-cne-pairs\n  expected:\n  - quantity: median sharpness of cNE pair PWCs\n    value: 2\n    tolerance: 0.2\n    unit: ms\n  - quantity: mean sharpness of cNE pair PWCs\n    value: 3.39\n    tolerance: 1.21\n    unit: ms\n  - quantity: mean absolute peak delay of cNE pair PWCs\n    value: 0.76\n    tolerance: 1.74\n    unit: ms\n  criterion: The tolerances of the means are the paper's stated spread. Whether the values pool\n    all cNE pairs or average per penetration is open. Readings (a) over all cNE pairs pooled; (b)\n    mean over penetrations of the per-penetration mean (or median). Under each lag reading of\n    fig2bd-pwc-measures-covary. Reproduced when all three are within tolerance under one reading;\n    partially reproduced when two are.\n- id: fig7-totals\n  statement: Across 16 penetrations, 104 cNEs were identified from 655 isolated neurons, an average\n    of 6.5 +/- 2.0 cNEs per penetration.\n  source: Results, cNEs are not depth-biased and reflect local circuitry, paragraph 1\n  quote: Across 16 penetrations, we identified a total of 104 cNEs ... The average number of cNEs\n    per penetration was 6.5 ± 2.0\n  expected:\n  - quantity: penetrations\n    value: 16\n    tolerance: 0\n  - quantity: isolated neurons\n    value: 655\n    tolerance: 0\n  - quantity: cNEs in total\n    value: 104\n    tolerance: 10.4\n  - quantity: cNEs per penetration, mean\n    value: 6.5\n    tolerance: 2.0\n  criterion: Penetration and neuron counts are a check that the 16 recordings are the ones the\n    paper used (tolerance zero). If a penetration was recorded with both DMR and RN, which file\n    the paper used is open; readings are each file, choosing the set whose unit counts sum to\n    655. cNE detection as in the opening comment. The tolerance of the mean is the paper's SD.\n- id: fig7a-number-vs-neurons\n  statement: The number of cNEs per penetration increased with the number of isolated neurons\n    (R2 = 0.74), and was about 15% of the number of recorded neurons.\n  source: Results, cNEs are not depth-biased and reflect local circuitry, paragraph 1; Figure 7A;\n    Supplementary file 1\n  quote: For each penetration, the number of cNEs was ~15% of the recorded number of neurons ...\n    the covariance between the number of identified cNEs and the number of isolated neurons (\n    Figure 7A ; R 2 = 0.74)\n  depends_on:\n  - fig7-totals\n  statistics:\n  - test: F-test\n    p: 1.68e-5\n    n: 16 penetrations\n  expected:\n  - quantity: R2 of number of cNEs on number of neurons\n    value: 0.74\n    tolerance: 0.074\n  - quantity: number of cNEs as a fraction of neurons\n    value: 15\n    tolerance: 1.5\n    unit: '%'\n  criterion: Least-squares line of number of cNEs on number of units over the 16 penetrations,\n    F-test of the fit. The fraction is open; readings (a) the mean over penetrations of\n    cNEs/neurons; (b) the slope of the line; (c) total cNEs over total neurons. Reproduced when R2\n    is within tolerance, p < 0.05 with positive slope, and the fraction is within tolerance under\n    one reading; partially reproduced when the fit holds and the fraction does not.\n- id: fig7b-size-vs-neurons\n  statement: The mean cNE size was 7.4 +/- 2.5 neurons, about 17% of the recorded neurons, and\n    increased with the number of isolated neurons, more weakly than the number of cNEs (R2 =\n    0.33).\n  source: Results, cNEs are not depth-biased and reflect local circuitry, paragraph 1; Figure 7B;\n    Supplementary file 1\n  quote: The mean number of neurons in cNEs was 7.4 ± 2.5 neurons. This again depended on the\n    number of isolated neurons ( Figure 7B ), with mean cNE size ~17% of the total number of\n    recorded neurons in the column. However, the covariance between mean cNE size and the number\n    of isolated neurons ( Figure 7B ; R 2 = 0.33) was not as strong\n  depends_on:\n  - fig7-totals\n  statistics:\n  - test: F-test\n    p: 0.02\n    n: 16 penetrations\n  expected:\n  - quantity: mean cNE size\n    value: 7.4\n    tolerance: 2.5\n    unit: neurons\n  - quantity: R2 of mean cNE size on number of neurons\n    value: 0.33\n    tolerance: 0.033\n  - quantity: mean cNE size as a fraction of neurons\n    value: 17\n    tolerance: 1.7\n    unit: '%'\n  criterion: Mean cNE size per penetration regressed on number of units, F-test of the fit. The\n    tolerance of the mean size is the paper's SD. Open is the averaging; readings (a) over all\n    cNEs pooled; (b) over penetrations of the per-penetration mean; the same two for the\n    fraction. Reproduced when R2 is within tolerance, p < 0.05 with positive slope and the mean\n    size within tolerance under one reading; partially reproduced when two of the three hold.\n- id: fig7-negative-weights\n  statement: The IC weights of almost all cNE members were positive; 9 cNEs (8.3%) had at least\n    one member with a negative weight.\n  source: Results, cNEs are not depth-biased and reflect local circuitry, paragraph 1\n  quote: The IC weight of the vast majority of cNE member neurons was positive ... However, 9 cNEs\n    (8.3%) also contained at least one neuron with a negative weight\n  depends_on:\n  - fig7-totals\n  expected:\n    quantity: cNEs with a negative-weight member\n    value: 9\n    tolerance: 1\n  criterion: A negative-weight member is one whose weight is below the lower membership threshold.\n    The count tolerance is one, 10% of 9 rounded up. The 8.3% does not equal 9 of 104 (8.7%); the\n    count is judged and the percentage reported. Rests on the IC sign reading (a) of the opening\n    comment, under which a sign is defined; reading (b) is shown as a variant. Reproduced when\n    the count is within tolerance and more than 90% of member weights are positive.\n- id: fig7c-membership\n  statement: Of the 655 isolated neurons, about 68% belonged to a single cNE, about 9% to none and\n    about 23% to more than one.\n  source: Results, cNEs are not depth-biased and reflect local circuitry, paragraph 1; Figure 7C\n  quote: Of the 655 neurons that were isolated, a majority (~68%) belonged to a single cNE, ~9% did\n    not belong to any cNE, and ~23% belonged to multiple cNEs\n  depends_on:\n  - fig7-totals\n  expected:\n  - quantity: neurons in exactly one cNE\n    value: 68\n    tolerance: 6.8\n    unit: '%'\n  - quantity: neurons in no cNE\n    value: 9\n    tolerance: 0.9\n    unit: '%'\n  - quantity: neurons in more than one cNE\n    value: 23\n    tolerance: 2.3\n    unit: '%'\n  criterion: Under each reading of IC scale and sign. Reproduced when all three are within\n    tolerance under one reading; partially reproduced when two are.\n- id: fig7d-pairs-within-200um\n  statement: About 82% of pairs of neurons in the same cNE were recorded on channels less than 200\n    um apart, so cNEs are mostly spatially confined.\n  source: Results, cNEs are not depth-biased and reflect local circuitry, paragraph 1; Figure 7D\n  quote: A majority of pairs of neurons within the same cNE (~82%) tended to be recorded from\n    channels separated by <200 µm ( Figure 7D ), indicating that cNEs are mostly spatially\n    confined\n  depends_on:\n  - fig7-totals\n  expected:\n    quantity: cNE pairs less than 200 um apart\n    value: 82\n    tolerance: 8.2\n    unit: '%'\n  criterion: All pairs of members of each cNE, pooled over cNEs and penetrations. Distance has the\n    two readings of fig2eg-distance-weak (depth difference; Euclidean distance on the probe).\n    Whether a pair in two cNEs counts once or once per cNE is open; both are shown. Reproduced\n    when one reading is within tolerance.\n- id: fig7e-no-depth-bias\n  statement: cNEs and their member neurons were found across the whole explored depth with no bias\n    to any depth; the depths of cNE members and of all recorded neurons were similarly\n    distributed.\n  source: Results, cNEs are not depth-biased and reflect local circuitry, paragraph 1; Figure 7E\n    legend\n  quote: There was no depth bias for cNE neurons, that is the distributions of the depth of cNE\n    members and that of all recorded neurons were similar\n  depends_on:\n  - fig7-totals\n  criterion: A claim of absence for which the paper names no test. Depth of a unit is its channel\n    'position' depth; the depth of a cNE is the median depth of its members (legend E). Readings\n    (a) two-sample Kolmogorov-Smirnov test, members (units in at least one cNE) against all\n    units; (b) Mann-Whitney U on the same; at alpha 0.05. Neither test is the paper's, so the\n    outcome rests on an assumption. Not reproduced when a test finds a difference; the\n    difference in median depth is given either way.\n- id: fig7f-span-200um\n  statement: Most cNEs (about 70%) spanned 200 um of cortical depth or less, though a few spanned\n    most of the recorded column.\n  source: Results, cNEs are not depth-biased and reflect local circuitry, paragraph 1; Figure 7F\n  quote: Most isolated cNEs (~70%) spanned a depth range of 200 µm or less of the cortical column\n  depends_on:\n  - fig7-totals\n  expected:\n    quantity: cNEs with a span of 200 um or less\n    value: 70\n    tolerance: 7\n    unit: '%'\n  criterion: Span is the maximum minus the minimum depth of a cNE's members (legend F), over the\n    104 cNEs.\n- id: fig8-spont-evoked-72pct\n  statement: cNEs detected separately in contiguous epochs of spontaneous and DMR-evoked activity\n    were largely the same; across eight recordings about 72% of spontaneous and evoked cNEs had\n    significant matches.\n  source: Results, cNEs persist across epochs of spontaneous and evoked activity; Figure 8E\n  quote: Across all eight recordings comprising contiguous epochs of spontaneous and evoked\n    activity we found significant matches for ~72% of spontaneous and evoked cNEs\n  expected:\n    quantity: spontaneous and evoked cNEs with a significant match\n    value: 72\n    tolerance: 7.2\n    unit: '%'\n  criterion: The eight 64-channel recordings. cNE detection on the spontaneous epoch and on the\n    evoked epoch separately; absolute correlation of IC weights; the null and the 99th-percentile\n    threshold per recording as in fig4s2-interleaved-halves-stable, under its readings. The\n    percentage pools spontaneous and evoked cNEs (legend E). Reproduced when one reading is\n    within tolerance.\n- id: fig9c-cne-events-more-mi\n  statement: Over 50 repeats of a 5-s stimulus, cNE events carried about 10% more mutual\n    information than the spikes of each member neuron; the median cNE/neuron MI ratio was 1.11\n    +/- 0.13 (median absolute deviation), significantly above 1.\n  source: Results, cNEs show enhanced information processing, paragraph 1; Figure 9C, D;\n    Supplementary file 1\n  quote: the MI conveyed by cNE events was, accordingly, ~10% higher than the MI of each member\n    neuron (p < 0.001, Wilcoxon signed-rank test; Figure 9C ). Correspondingly, the ratio of the\n    MIs (cNE/neuron) was significantly larger than 1 (median ± median absolute deviation = 1.11 ±\n    0.13; p < 0.001, Wilcoxon signed-rank test\n  statistics:\n  - about: cNE MI against member neuron MI, and the MI ratio against 1\n    test: Wilcoxon signed-rank test\n    p: 1.84e-26\n    n: 330 cNE and member neuron pairs\n  expected:\n  - quantity: median MI ratio, cNE over neuron\n    value: 1.11\n    tolerance: 0.13\n  - quantity: cNE and member neuron pairs\n    value: 330\n    tolerance: 33\n  criterion: Method from Materials and methods, MI analysis on 5-s repeats. Trials by 10-ms bins;\n    MI from the PSTH r(t) and its mean (Brenner et al., 2000), extrapolated to infinite data from\n    20 subsamples at 90 to 100% of the bins; the larger of cNE events and neuron spikes randomly\n    subsampled to equal counts. Open is how cNE events on the repeats are obtained; readings (a)\n    ICs and activity threshold from the 10-min recording of the penetration, the ICs projected\n    onto the repeat spike trains; (b) cNE detection on the repeat data; each with both event\n    readings of the opening comment. The tolerance of the ratio is the paper's MAD. Reproduced\n    when, under one reading, the median ratio is within tolerance and the signed-rank test gives\n    p < 0.001 with cNE MI higher.\n- id: fig9s1-cne-mi-above-random-groups\n  statement: The MI of the summed spikes of cNE members exceeded that of random groups of neurons\n    of the same size, and the uniqueness index distribution was skewed towards 0, unlike the\n    uniform distribution expected for random membership.\n  source: Results, cNEs show enhanced information processing, paragraph 2; Figure 9—figure\n    supplement 1D; Supplementary file 1\n  quote: We found that the MI of spikes from cNE members was significantly higher than the MI of\n    spikes from random groups of neurons (p < 0.001, Wilcoxon signed-rank test ... The\n    distribution of UI values was significantly skewed towards 0 and was significantly different\n    from an expected uniform distribution\n  statistics:\n  - about: cNE MI against median random group MI\n    test: Wilcoxon signed-rank test\n    p: 2.03e-8\n    n: 96 cNEs\n  - about: UI distribution against uniform\n    test: Kolmogorov–Smirnov test\n    p: 0.001\n    p_relation: <\n  depends_on:\n  - fig9c-cne-events-more-mi\n  criterion: Random groups as in Materials and methods, MI comparisons between cNE and random\n    groups (one member of the cNE plus non-members, at most one member of any other cNE, raised\n    stepwise until 500 unique groups exist); spikes summed; all subsampled to the fewest spikes;\n    sets under 200 spikes excluded; MI as in fig9c-cne-events-more-mi. UI is the share of the 501\n    values at or above the cNE value. Reproduced when the signed-rank test gives p < 0.001 with\n    cNE MI higher and the one-sample KS test against uniform on [0, 1] gives p < 0.001 with UI\n    below the uniform median.\n- id: fig9s2-noise-correlations\n  statement: Pairs of neurons in the same cNE had higher noise correlations than pairs not in the\n    same cNE, in each of the 16 recordings and across them.\n  source: Results, cNEs show enhanced information processing, paragraph 3; Figure 9—figure\n    supplement 2; Supplementary file 1\n  quote: Over the 16 columnar recordings, pairs of neurons that were members of the same cNE had\n    significantly higher noise correlations than pairs of neurons not within the same cNE\n  statistics:\n  - about: per-recording medians, cNE pairs against non-cNE pairs, 16 recordings\n    test: paired t-test\n    p: 1.73e-5\n    n: 16 recordings\n  - about: example recordings (Figure 9—figure supplement 2B), each\n    test: Mann-Whitney U-test\n    p: 0.001\n    p_relation: <\n    n: 3 recordings\n  criterion: Noise correlation is Pearson's R between two neurons' spike rates over the 50 trials\n    of the 5-s repeat (legend A). Open is the rate; readings (a) spike count over the whole 5-s\n    trial; (b) the rate in each 10-ms bin minus its PSTH, correlated over trials and bins.\n    Reproduced when, under one reading, the paired t-test over recordings gives p < 0.001 with\n    cNE pairs higher; partially reproduced when p < 0.05.\n- id: fig10b-ptd-higher\n  statement: cNE STRFs had stronger excitatory and inhibitory subfields than those of their member\n    neurons, with a higher peak-trough difference.\n  source: Results, cNEs show enhanced information processing, paragraph 4; Figure 10B;\n    Supplementary file 1\n  quote: Compared to neuronal STRFs, cNE STRFs had higher peak-trough differences (PTD; p < 0.001,\n    Wilcoxon signed-rank test; Figure 10B )\n  statistics:\n  - test: Wilcoxon signed-rank test\n    p: 1.62e-37\n    n: 703 cNE and member neuron pairs\n  criterion: STRFs by event- or spike-triggered average of the 10-min stimulus, after subsampling\n    the larger train to equal counts; PTD is the highest minus the lowest STRF value divided by\n    the number of spikes or events (legend B). The STRF window and the subsampling seed are\n    standard choices, stated. Under both event readings. Reproduced when p < 0.001 with cNE PTD\n    higher under one reading; the number of pairs is reported against 703.\n- id: fig10c-strf-mi-higher\n  statement: cNEs had higher mutual information between their STRFs and single events than member\n    neurons had between their STRFs and single spikes.\n  source: Results, cNEs show enhanced information processing, paragraph 4; Figure 10C;\n    Supplementary file 1\n  quote: and MI (p < 0.001, Wilcoxon signed-rank test; Figure 10C )\n  statistics:\n  - test: Wilcoxon signed-rank test\n    p: 1.60e-59\n    n: 703 cNE and member neuron pairs\n  depends_on:\n  - fig10b-ptd-higher\n  criterion: STRF MI as in fig5a-mi-peaks-10-15ms (projection distributions, extrapolation over\n    90 to 100% of events, 20 iterations), on the equal-count trains of fig10b-ptd-higher.\n    Reproduced when p < 0.001 with cNE MI higher under one event reading.\n- id: fig10s1-random-group-strfs\n  statement: Multi-unit STRFs of cNE members had higher PTD and higher STRF MI than those of random\n    groups of neurons of the same size, with uniqueness indices skewed towards 0.\n  source: Results, cNEs show enhanced information processing, paragraph 5; Figure 10—figure\n    supplement 1C, E; Supplementary file 1\n  quote: Across the entire population, the STRF PTD for cNE members was significantly higher than\n    that of the STRF PTD for random groups of neurons (p < 0.001, Wilcoxon signed-rank test ...\n    The STRF MI of cNE member neurons was also significantly higher than that of random groups\n    of neurons (p < 0.001, Wilcoxon signed-rank test\n  statistics:\n  - about: PTD, cNE against median random group\n    test: Wilcoxon signed-rank test\n    p: 1.39e-6\n    n: 103 cNEs\n  - about: STRF MI, cNE against median random group\n    test: Wilcoxon signed-rank test\n    p: 8.70e-12\n    n: 103 cNEs\n  - about: UI distributions against uniform, PTD and MI\n    test: Kolmogorov–Smirnov test\n    p: 0.001\n    p_relation: <\n  criterion: Random groups, summed spikes and equal-count subsampling as in\n    fig9s1-cne-mi-above-random-groups; PTD and MI as in fig10b-ptd-higher and\n    fig10c-strf-mi-higher. Reproduced when both signed-rank tests give p < 0.001 with cNEs higher\n    and both KS tests give p < 0.001; partially reproduced when the PTD or the MI part holds alone.\n- id: fig11ab-real-vs-surrogate\n  statement: Spike matrices built from simultaneous spike trains ('real') gave more cNEs, and\n    larger ones, than matrices built from different presentations of the same stimulus\n    ('surrogate'), so stimulus-driven synchronization is not the main source of cNE synchrony.\n  source: Results, cNE events are not fully accounted for by stimulus synchronization, paragraph 1;\n    Figure 11A, B; Supplementary file 1\n  quote: We found, however, that the ‘surrogate’ spike train matrices had fewer cNEs ( Figure 11A )\n    and that the detected cNEs had fewer member neurons ( Figure 11B )\n  statistics:\n  - about: number of cNEs, real against surrogate\n    test: paired t-test\n    p: 6.15e-38\n    n: 100 combinations of 15 neurons\n  - about: mean cNE size, real against surrogate\n    test: paired t-test\n    p: 2.79e-57\n    n: 100 combinations of 15 neurons\n  criterion: Method from Materials and methods, Constructing repeat ('surrogate') spike matrices.\n    Units responding to all 15 presentations of the 10-min RN with rates varying by less than 30%\n    between adjacent presentations (24 in the paper); 100 unique random 15-unit combinations; per\n    combination 15 real and 15 surrogate matrices (the shuffled order shifted circularly by one\n    each time); cNE detection on each, averaged over the 15. How the 30% is computed is open;\n    readings (a) the absolute rate difference over the mean of the two; (b) over the earlier\n    presentation. Reproduced when both paired t-tests give p < 0.001 with real higher; the number\n    of units passing is reported against 24.\n- id: fig11c-models-number\n  statement: Surrogate spike trains from the 'shuffled' and 'preserved receptive field' (PR)\n    models gave fewer cNEs than the real data, while the dichotomized Gaussian (DG) model gave\n    more.\n  source: Results, cNE events are not fully accounted for by stimulus synchronization, paragraph 6;\n    Figure 11C; Supplementary file 1\n  quote: Surrogate spike trains from the ‘shuffled’ and ‘PR’ models had significantly fewer cNEs (\n    Figure 11C ) than the real data. On the other hand, the ‘DG’ model overestimates the number of\n    detected cNEs\n  statistics:\n  - about: shuffled against real\n    test: paired t-test with Bonferroni correction\n    p: 4.87e-9\n    corrected: Bonferroni\n    n: 16 penetrations\n  - about: PR against real\n    test: paired t-test with Bonferroni correction\n    p: 4.62e-8\n    corrected: Bonferroni\n    n: 16 penetrations\n  - about: DG against real\n    test: paired t-test with Bonferroni correction\n    p: 7.98e-6\n    corrected: Bonferroni\n    n: 16 penetrations\n  criterion: Models from Materials and methods, Simulated spike trains. Shuffled, each unit's\n    binned train shifted circularly by a random number of bins. PR, the full range of each unit's\n    STRF projection values split into 15 equal bins, and spikes moved at random to time bins of\n    the same projection bin. DG, binary 5-ms trains fitted for means and covariances and sampled\n    with CorBinian (findLatentGaussian01, sampleDichGauss01), then rebinned to 10 ms. 200\n    iterations per model and penetration, mean number of cNEs per penetration. Open are the bin\n    width of the PR shuffle and the STRF used for it; readings (a) 10-ms bins; (b) 5-ms bins;\n    with the STRF of the same recording. Bonferroni over the three model comparisons. Reproduced\n    when, under one reading, all three corrected p < 0.05 with shuffled and PR fewer and DG more;\n    partially reproduced when two of the three hold.\n- id: fig11d-models-size\n  statement: All three models, including the DG model, gave cNEs with fewer member neurons than\n    the real data.\n  source: Results, cNE events are not fully accounted for by stimulus synchronization, paragraph 6;\n    Figure 11D; Supplementary file 1\n  quote: all three models, including the ‘DG’ model, resulted in cNEs that were smaller in size\n    (i.e., fewer member neurons, Figure 11D ) than the real data (n = 16 penetrations\n  depends_on:\n  - fig11c-models-number\n  statistics:\n  - about: shuffled against real\n    test: paired t-test with Bonferroni correction\n    p: 1.23e-7\n    corrected: Bonferroni\n    n: 16 penetrations\n  - about: PR against real\n    test: paired t-test with Bonferroni correction\n    p: 0.04\n    corrected: Bonferroni\n    n: 16 penetrations\n  - about: DG against real\n    test: paired t-test with Bonferroni correction\n    p: 7.2e-3\n    corrected: Bonferroni\n    n: 16 penetrations\n  criterion: The model runs of fig11c-models-number, mean cNE size per penetration. A model run\n    that yields no cNE has no size; whether such runs are left out or count as zero is open, and\n    both are shown. Reproduced when all three corrected p < 0.05 with the models smaller;\n    partially reproduced when two hold.\n- id: fig11ef-coincidence-ratios\n  statement: Normalized to the real data, the coincidence ratios of groups of 2 and 3 cNE members\n    were significantly below one for the 'repeat' data and the shuffled, PR and DG models.\n  source: Results, cNE events are not fully accounted for by stimulus synchronization, paragraph 7;\n    Figure 11E, F; Supplementary file 1\n  quote: The normalized CR for the repeated stimulus data (‘repeat’), ‘shuffled’, ‘PR’ and ‘DG’\n    models were significantly less than one for all groups ( Figure 11E and F )\n  depends_on:\n  - fig11c-models-number\n  statistics:\n  - about: each of shuffled, PR, repeat and DG against real, pairs (Figure 11E)\n    test: paired t-test with Bonferroni correction\n    p: 1.0e-100\n    p_relation: <\n    corrected: Bonferroni\n    n: 400 groups\n  - about: each of shuffled, PR, repeat and DG against real, triplets (Figure 11F)\n    test: paired t-test with Bonferroni correction\n    p: 1.0e-100\n    p_relation: <\n    corrected: Bonferroni\n    n: 400 groups\n  criterion: Method from Materials and methods, Calculation of coincidence ratios. CR is the\n    number of bins in which all units of the group spike over the number in which its\n    lowest-rate unit spikes; 400 unique groups of 2 and of 3 members of the same cNE; one real\n    CR, one repeat CR (trains from different presentations), and the median of 1000 iterations\n    of each model; all divided by the real CR. Bins of 10 ms, the detection bin, as the paper\n    names no other. The repeat CR needs the repeated 10-min RN data; without it the claim is\n    judged on the three models. Reproduced when every comparison gives corrected p < 0.001 with\n    the normalized CR below one; partially reproduced when the models hold and repeat cannot be\n    run.\n- id: fig11s3b-pr-strf-similarity\n  statement: The PR model preserved the neurons' STRFs (median STRF similarity with the real\n    spike trains about 0.74), while the shuffled and DG models gave STRF similarities close to\n    zero.\n  source: Results, cNE events are not fully accounted for by stimulus synchronization, paragraph\n    5; Figure 11—figure supplement 3B\n  quote: the ‘PR’ model had a high median correlation value (~0.74) while the ‘shuffled’ and ‘DG’\n    models had values close to zero\n  depends_on:\n  - fig11c-models-number\n  expected:\n    quantity: median STRF similarity, PR model against real\n    value: 0.74\n    tolerance: 0.074\n  criterion: STRF similarity is the correlation of a unit's model STRF with its real STRF, by\n    spike-triggered average; median over all units and iterations. \"Close to zero\" is read as an\n    absolute median below 0.1, a reading not fixed by the paper. Reproduced when the PR median is\n    within tolerance and both other medians are below 0.1 in absolute value.\n"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  python tools/claims_check.py claims/see-2018.yaml paper/10.7554-elife.35587.txt; grep -nE "^\s+[a-z_]+: [^'\"|>].*: " claims/see-2018.yaml; grep -nE "^\s{4,}[^-#].*: " claims/see-2018.yaml | head; grep -n "—\|rather" claims/see-2018.yaml | grep -v "figure supplement" | head
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  sed -i 's/—/-/g' claims/see-2018.yaml; grep -c "—" claims/see-2018.yaml; python tools/claims_check.py claims/see-2018.yaml paper/10.7554-elife.35587.txt; python -c "
import yaml;d=yaml.safe_load(open('claims/see-2018.yaml'));c=d['claims'];print(len(c),sum('statistics' in x for x in c),sum('criterion' in x for x in c),sum('expected' in x for x in c))"; git status --short
```

Result: not kept, because it reads the paper's text.

**Agent**

I wrote `claims/see-2018.yaml`: 31 claims from the full text, Methods and supplement. The quote checker passes every quote. It flags one value it can't match, which I checked by hand (below).

**Text read**
- **Paper:** the version of record (PMC6017807, Europe PMC full-text XML), with all figure and figure-supplement legends and the Materials and methods.
- **Supplement:** Supplementary file 1 (`elife-35587-supp1-v2.xlsx`), the table of statistical tests giving the test, N and exact p for each panel. It is also printed at the end of the text file.
- **Figures:** no PDF was supplied, so figure axes were not read. Every value used is printed in the text, a legend or the supplement.
- **Code:** the only repository the paper links is CorBinian (Macke lab), the implementation of its dichotomized Gaussian (DG) model, used as a surrogate data model. I read it at commit 8ebb12d (2021); the paper cites the 2017 state, which can't be pinned. The paper's own MATLAB analysis code is not linked.

**Counts**
- 31 claims, all with quotes, none inferred.
- 13 claims record statistics (24 p-values in all, most of them exact values from Supplementary file 1).
- 31 have criteria and 16 have expected values.
- The checker flags p = 8.70e-12 (Figure 10, figure supplement 1E) as not found. I read it in Supplementary file 1 (text line 457) and it is correct. The checker misses it only because the paper prints a trailing zero. I left the checker and the value as they are.

**Details the paper leaves open, with the readings named**
- **cNE detection** (used in most claims):
  - Marčenko–Pastur bound: the standard (1+√(n/T))², as in Lopes-dos-Santos et al. (2013).
  - Independent component (IC) scale and sign: (a) unit length, largest weight made positive; (b) as fastICA returns them.
  - Activity: (a) the quadratic form with the diagonal set to zero; (b) a linear projection.
  - What counts as an event: (a) every bin above threshold; (b) one per run of bins above threshold.
  - fastICA settings and random seeds: standard choices, stated as such.
- **Pairwise correlation functions** (Figures 2 and 6): the lag bin and range, either 1-ms bins over ±50 ms or ±100 ms, with the fit on linear or log axes.
- **Pairwise distance:** depth difference, or Euclidean distance on the probe.
- **Stability matching** (Figure 4, supplement 2, and Figure 8): the number of shuffles and what the shuffled ICs are correlated with (shuffled against shuffled, or real against shuffled).
- **Averaging:** pooled over all cNEs, or per penetration first, for the Figure 6 sharpness means and the Figure 7 sizes and fractions.
- **Penetrations recorded with both stimuli:** which file the paper used; the reading is the set whose unit counts sum to 655.
- **Figure 9 events on the 5-s repeats:** the ICs from the 10-min recording projected onto the repeats, or detection run on the repeats themselves.
- **Noise correlation:** the spike count per trial, or rates per bin.
- **Figure 11A/B:** how the 30% rate-stability rule is computed.
- **PR surrogate model** (spikes reshuffled while each neuron's receptive field is kept): the shuffle bin, 5 ms or 10 ms.
- **Figure 11D:** whether model runs that yield no cNE are dropped or counted as zero.
- **Figure 5A:** how mutual information is summarised over cNEs (mean or median). The STRF window and the number of projection bins are standard choices.

**Thresholds I had to supply** (the paper reports no test, so each is marked in its criterion as a reading, not the paper's method):
- the depth-bias test (KS test or Mann–Whitney);
- the bin-size trends (Spearman correlation);
- "much narrower" versus "often as wide" in Figure 6C;
- "close to zero" in Figure 11, supplement 3B (absolute value below 0.1).

**Inconsistency in the paper:** "9 cNEs (8.3%)" doesn't match 104 cNEs (9/104 is 8.7%). The criterion judges the count of 9 and reports the percentage.

**Nothing a claim needed is missing from the paper.** Several claims need experiments that may not be in the dataset: the 5-s repeats (Figure 9), the 15 repeats of the 10-min stimulus (Figure 11A/B and the "repeat" coincidence ratio in Figure 11E/F), and the eight 64-channel spontaneous and evoked recordings (Figure 8). The descriptor lists only the long-stimulus files; whether the dataset holds the rest is the author's to find. Nothing is committed.

## End of run

17 turns, 5 minutes, $1.62 at API prices, result: success.
