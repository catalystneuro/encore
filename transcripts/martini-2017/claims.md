# martini-2017 · claims · run 42663063373

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
grep -n "^#" docs/protocol.md | head -50; ls paper/ claims/ | head -50
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "docs/protocol.md",
 "limit": 195
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
[... 175 more lines not kept]
```

**Agent calls Bash**

```bash
ls -la paper/; cat claims/fouke-2025.yaml; ls claims/martini* 2>&1
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cat paper/10.1093-cercor-bhx019.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/c907c2f1-450b-46e3-a349-cca56c9cfce5/tool-results/bplcrfm78.txt"
}
```

```
1	DOI: 10.1093/cercor/bhx019
2	Version: version of record
3	Source: supplied by a person
4	Stored: 2026-11-08
5	Extracted: PyMuPDF, dehyphenated, NFKC
6	------------------------------------------------------------------------
7	
8	=== page 1 ===
9	Cerebral Cortex, July 2017;27: 3782–3789
10	doi: 10.1093/cercor/bhx019
11	Advance Access Publication Date: 25 February 2017
12	Original Article
13	O R I G I N A L A R T I C L E
14	Interspersed Distribution of Selectivity to Kinematic
15	Stimulus Features in Supragranular Layers of Mouse
16	Barrel Cortex
17	Francisco J. Martini1, Manuel Molano-Mazón1,2 and Miguel Maravall1,3
18	1Instituto de Neurociencias de Alicante UMH-CSIC, Avda. Ramón y Cajal s/n, Campus de San Juan, 03550 Sant
19	Joan d’Alacant, Spain, 2Laboratory of Neural Computation, Center for Neuroscience and Cognitive
20	Systems @UniTn, Istituto Italiano di Tecnologia, 38068 Rovereto, Italy and 3Sussex Neuroscience, School of Life
[... 750 more lines not kept]
```

**Agent calls Bash**

```bash
cat paper/ssc-6.data-description.txt; echo ----; cat papers/datasets/martini-2017.yaml; grep -l "archive: crcns" claims/*.yaml | head -3; sed -n 1,200p tools/claims_check.py | head -80
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -n 1,40p claims/bruno-2017.yaml; python -c "import json;d=json.load(open('schemas/claims.schema.json'));print(json.dumps(d,indent=1)[:6000])"
```

```
# Claims for Bruno, Frost & Humphries (2017), eLife 6:e27342, "A spiral attractor network drives
# rhythmic locomotion", doi:10.7554/elife.27342, on CRCNS data set apl-1 (doi:10.6080/K0SN074B).
# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"), 2026-11-08,
# protocol as stated in docs/protocol.md (Reader), version pilot-13.
#
# Text read: the version of record (PMC5546814, open access), as JATS XML flattened to text under
# paper/: main text, Materials and methods, and the legends of Figures 1 to 8 and of all twelve
# figure supplements. The paper has no other supplementary file. No PDF of the paper was supplied,
# and none was needed: no claim rests on a number shown only in a figure. The extraction garbles
# some formulas: the Gaussian width reads "σ = {median ISI in population}/12" (a square root may be
# lost) and the rotation period reads "ω = 2πbΔt"; the code settles the second (see below).
# The data set's description (paper/apl-1.data-description.txt) was read only to know what it
# holds; no claim comes from it.
#
# Code read: https://github.com/mdhumphries/AplysiaAttractorAnalysis, commit e5f28e98 (2018-07-11),
# MATLAB, linked from the paper's Data and code availability. Analysis/DataSet_Properties.m builds
# the spike-density functions and the PCA; Analysis/Classify_attractors/ holds the recurrence
# analysis (Analyse_by_Recurrence_Points.m, LocalLinearDynamics.m, recurrence_point_results_Viz.m),
# manifold comparisons (Are_sequential_attractors_the_same.m and _CommonAxes.m,
# Initial_Conditions.m), perturbations (Are_jumps_perturbations_or_transitions2.m), period change
[... 221 more lines not kept]
```

**Agent calls Bash**

```bash
python -c "import json;d=json.load(open('schemas/claims.schema.json'));print(json.dumps(d['\$defs'],indent=1))"; sed -n 40,120p claims/bruno-2017.yaml
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
[... 163 more lines not kept]
```

**Agent**

The paper and Methods are complete, and no analysis code is linked. I have what I need and will write the claims file now.

**Agent calls Write**

```json
{
 "file_path": "claims/martini-2017.yaml",
 "content": "# Claims for Martini, Molano-Mazon & Maravall (2017), Cerebral Cortex 27:3782-3789, \"Interspersed\n# Distribution of Selectivity to Kinematic Stimulus Features in Supragranular Layers of Mouse Barrel\n# Cortex\", doi:10.1093/cercor/bhx019, on CRCNS data set ssc-6 (doi:10.6080/K02F7KCP).\n# Written by an agent (model \"claude-opus-5-5\", Claude Code, runner \"GitHub Actions\"), 2026-11-09,\n# protocol as stated in docs/protocol.md (Reader), version pilot-14.\n#\n# Text read: the version of record (open access, CC BY), extracted from the PDF to\n# paper/10.1093-cercor-bhx019.txt: main text, Materials and Methods, legends of Figures 1 to 4, and\n# the supplement (text_suppmat.docx), which holds only the legends of Supplementary Figures 1 to 3.\n# These repeat the data of Figures 2C, 2F and 4B split into red, green and blue channels; no result\n# rests on the supplement alone. The PDF was not opened: no claim needed a value shown only in a\n# figure. The data set's description (paper/ssc-6.data-description.txt) was read only to know what\n# it holds; no claim comes from it.\n#\n# Code: the paper links none. It names the software used: a modified StackReg ImageJ plugin\n# (registration), Caltracer 2.5 (Yuste lab, ROI detection and traces), and the Matlab function\n# fdr_bh by David Groppe (false discovery rate); stimuli were made in Matlab. \"All data supporting\n# this study are available at http://crcns.org.\" No analysis script was available to read, so every\n# detail the Methods leave open is named below as open.\n#\n# Data the paper used. Female CD1 mice at about postnatal day 30, under ketamine-xylazine\n# anesthesia (n = 10 mice). Layer 2/3 of barrel cortex bulk-loaded with OGB1-AM, imaged with a\n# 2-photon microscope at 100 to 350 um depth, 512 x 128 pixel frames at 1.48 pixel/um and 8.8 Hz.\n# 10 to 15 contralateral whiskers in a capillary on a piezoelectric bender moved rostro-caudally.\n# Nine stimuli, idealized position, velocity and acceleration filters, each at three amplitudes in\n# the ratio 1:3:5, randomly interleaved, 1 s apart; each stimulus 10 times per recording and 4\n# recordings per field of view (40 presentations per stimulus and field). 49 fields of view and\n# 1054 neurons after discarding experiments with excessive motion. In 3 mice, tangential\n# cytochrome-oxidase sections placed the imaged neurons on the barrel map (167, 102 and 117 neurons).\n# Measured variables: per-neuron calcium response amplitude to each presentation (mean dF/F0 of the\n# 5 frames after the stimulus minus the mean of the 3 frames before), regression tuning\n# coefficients for position, velocity and acceleration, pairwise Spearman correlations of the whole\n# fluorescence time series, pairwise distances, a tuning similarity index (SI), and distance to the\n# nearest barrel border. The data set's description says it holds, for each of ten mice, the raw\n# movies of every field (four repetitions each), the stimulus command and frame-trigger signals for\n# each movie, and, for experiments 8 to 10, histology reconstructions (PDF). It holds no ROIs,\n# traces or tuning labels: the author must segment the movies again, so neuron counts and\n# identities will not match the paper's one to one. All claims use the data set (data: dataset).\n#\n# Method fixed by the Methods (2-Photon Image Analysis; Measurements of Response Properties), used\n# by every claim: rigid registration of each movie to its first frame; ROIs outlined on the mean\n# image of all frames; mean raw fluorescence per ROI with background from unstained blood vessels\n# subtracted; a perisomatic halo scaled by 0.7 and subtracted; dF/F0 with F0 the 8th percentile of\n# corrected fluorescence in a symmetric 6 s sliding window; response amplitude as above; tuning by\n# linear regression of all single-presentation response amplitudes on the amplitude of the\n# corresponding waveform, one regression per waveform type, scored with the Benjamini-Hochberg-\n# Yekutieli false discovery rate procedure at P < 0.05 (fdr_bh) over the neurons of a field;\n# non-significant coefficients set to zero; mixed selectivity when significant for several features.\n#\n# Details the paper leaves open, named again in the claims they touch:\n# (1) the halo width, the blood-vessel background ROI, and how ROIs are carried across the four\n#     movies of a field (one ROI set on the mean of all four registered movies is the reading used;\n#     a standard choice). The motion threshold for discarding fields is not given.\n# (2) which frames count as \"after\" and \"before\" a stimulus: the first frame starting at or after\n#     the command onset is the first frame after (standard choice).\n# (3) amplitude units in the regression: normalized 1, 3, 5 (Figure 2B legend, \"normalized to the\n#     smallest value\") or the peak command voltage. Significance does not depend on the units when\n#     each waveform type is regressed separately; coefficient magnitudes do. dF/F0 as a fraction or\n#     as percent scales coefficients by 100.\n# (4) the test of each regression: the t test of the slope, two-sided, is the standard reading;\n#     whether a significant negative slope counts as tuning is not stated (readings: either sign;\n#     positive only).\n# (5) the false discovery rate family and variant: fdr_bh with 'pdep' (Benjamini-Hochberg) or\n#     'dep' (Benjamini-Yekutieli), the text names both authors; family of all 3 x N p-values of a\n#     field, or N p-values per feature.\n# (6) what \"responded to whisker stimulation\" means (50.2%): not defined.\n# (7) the correlation signal: neuropil-corrected fluorescence before dF/F0 (the Methods' \"corrected\n#     fluorescence\") or dF/F0; the shuffle unit (one stimulus presentation, from its onset to the\n#     next onset) and the number of shuffles for correlations (not given; 100, as for SI, is used).\n# (8) distance between neurons: between ROI centroids in the imaging plane (standard choice);\n#     whether pairs beyond 300 um are fitted.\n# (9) which 26 of the 49 fields enter the SI analysis, and the SI scale (raw dot product as the\n#     Methods write it, or of unit-length tuning vectors).\n# (10) for Figure 4D, the group of a neuron tuned to several features, and whether the distance to\n#     the border is signed.\n# (11) the example neuron (Figure 2A-C) and the example field (Figure 3A, B, D, F) are not\n#     identified by mouse or field. The paper also gives the example field two sizes: n = 31\n#     neurons (Figure 3B) and n = 29 neurons with n = 465 pairs (Figure 3F, \"the field of view in\n#     A\"); 465 is the number of pairs of 31 neurons.\nschema_version: 2\npaper: doi:10.1093/cercor/bhx019\nclaims:\n- id: dataset-size\n  statement: Layer 2/3 neurons were imaged in 10 anesthetized mice, 49 fields of view and 1054\n    neurons in all; each stimulus was presented 10 times per recording, in 4 recordings per field.\n  source: Materials and Methods, Whisker Stimulation, paragraph 3; Results, paragraphs 1 and 3\n  quote: In a recording, each stimulus was presented 10 times; 4 recordings were done for each field\n    of view, for a total of 40 repetitions per field ... anesthetized mice (n = 10) ... n = 10 mice,\n    49 fields of view, 1054 neurons\n  expected:\n  - quantity: mice\n    value: 10\n    tolerance: 0\n  - quantity: fields of view\n    value: 49\n    tolerance: 0\n  - quantity: recordings per field of view\n    value: 4\n    tolerance: 0\n  - quantity: presentations of each stimulus per recording\n    value: 10\n    tolerance: 0\n  - quantity: neurons over all fields\n    value: 1054\n    tolerance: 105\n  criterion: Mice, fields and recordings are counted from the deposited movies and stimulus files,\n    presentations from the command signal of each stimulus file, with zero tolerance. The paper\n    discarded fields with excessive motion by a threshold it does not give (open detail 1); if the\n    data set holds more than 49 fields, the excluded ones cannot be identified from the paper, and\n    the count is reported as it is. Neurons must be segmented again from the raw movies (Caltracer\n    or an equivalent, ROIs on the mean image, as the Methods), so the count takes the 10% tolerance.\n- id: stimulus-set\n  statement: The stimulus set holds idealized position, velocity and acceleration waveforms, each at\n    three amplitudes in the ratio 1:3:5, randomly interleaved and separated by 1 s.\n  source: Materials and Methods, Stimulus Design and Whisker Stimulation, paragraph 3; Results,\n    paragraph 1\n  quote: The set included idealized \"position,\" \"velocity,\" and \"acceleration\" filters ... Each\n    waveform type was presented with 3 possible amplitudes, in the ratio 1:3:5 ... Consecutive\n    deflections were separated by 1 s ... Different deflection waveforms and amplitudes were\n    randomly interleaved in time\n  expected:\n  - quantity: distinct waveform shapes\n    value: 3\n    tolerance: 0\n  - quantity: amplitudes per shape\n    value: 3\n    tolerance: 0\n  - quantity: ratio of largest to smallest amplitude within a shape\n    value: 5\n    tolerance: 0.5\n  - quantity: ratio of middle to smallest amplitude within a shape\n    value: 3\n    tolerance: 0.3\n  - quantity: interval between consecutive deflection onsets\n    value: 1\n    tolerance: 0.1\n    unit: s\n  criterion: Read from the command signal (column 2) of the stimulus files. Each deflection is\n    classed by its shape (the three filter shapes of Figure 1B) and its peak amplitude. Reproduced\n    when the nine classes fall into three shapes with three amplitudes each in the ratios above, onsets\n    are 1 s apart, and the order of the nine classes differs between recordings (randomly\n    interleaved).\n- id: fig2ab-example-neuron\n  statement: In an example neuron, calcium responses grew most with the amplitude of the velocity\n    waveform; its regression coefficients were 0.0069 for position, 0.0169 for velocity and 0.0106\n    for acceleration.\n  source: Results, paragraph 2; Figure 2A and 2B\n  quote: the value of the regression coefficient between stimulus amplitude and neuronal response\n    was greatest for velocity [rp = 0.0069 for position (5–95% CI 0.0032–0.011); rv = 0.0169 for\n    velocity (CI 0.0132–0.021); ra = 0.0106 for acceleration (CI 0.0073–0.0151); Fig. 2B]\n  statistics:\n  - about: position coefficient\n    ci:\n      level: 0.9\n      low: 0.0032\n      high: 0.011\n  - about: velocity coefficient\n    ci:\n      level: 0.9\n      low: 0.0132\n      high: 0.021\n  - about: acceleration coefficient\n    ci:\n      level: 0.9\n      low: 0.0073\n      high: 0.0151\n  expected:\n  - quantity: position regression coefficient (tolerance to the paper's 5-95% interval, 0.0032 to\n      0.011)\n    value: 0.0069\n    tolerance: 0.0041\n  - quantity: velocity regression coefficient (interval 0.0132 to 0.021)\n    value: 0.0169\n    tolerance: 0.0041\n  - quantity: acceleration regression coefficient (interval 0.0073 to 0.0151)\n    value: 0.0106\n    tolerance: 0.0045\n  criterion: The paper does not say which mouse, field or ROI holds this neuron (open detail 11). The\n    author identifies it by matching the field and ROI mask of Figure 2C (black arrow) to the mean\n    images of the fields; if no field matches, the claim cannot be tested. Coefficients are the\n    slopes of three separate regressions of all single-presentation responses (Methods, Measurements\n    of Response Properties) on amplitude. Amplitude in normalized units 1, 3, 5 and dF/F0 as a\n    fraction is the main reading (Figure 2B legend; open detail 3), the command voltage as a variant.\n    Reproduced when the velocity coefficient is the largest of the three and each coefficient lies\n    in its interval (the tolerances span the paper's interval, taking the wider side); partially\n    reproduced when only the order holds. The tolerance on each coefficient is the larger\n    distance from the value to a bound of the paper's interval.\n- id: responsive-fraction\n  statement: About half (50.2%) of all neurons in the data set responded to whisker stimulation.\n  source: Results, paragraph 3; Discussion, paragraph 3\n  quote: Overall, 50.2% of neurons in the data set responded to whisker stimulation\n  expected:\n    quantity: percentage of neurons responding to whisker stimulation\n    value: 50.2\n    tolerance: 5.0\n    unit: percent\n  criterion: The paper does not define a responsive neuron (open detail 6). Readings the text\n    allows, each run on all segmented neurons, pooled across fields: (a) the mean response amplitude\n    over all 360 presentations is greater than zero, one-sided signed-rank test p < 0.05; (b) at\n    least one of the nine stimuli evokes a response greater than zero (signed-rank test over its 40\n    presentations, p < 0.05), with the Benjamini-Hochberg-Yekutieli correction over the neurons and\n    stimuli of a field as the paper uses for tuning. Reproduced when a reading gives 50.2% within the\n    tolerance; the outcome rests on that reading as an assumption.\n- id: fig2de-tuned-fraction\n  statement: Most neurons were not tuned to any kinematic feature; 71.8% of all neurons were\n    non-tuned, so about 30% were tuned.\n  source: Results, paragraph 3; Figure 2D and 2E; Discussion, paragraph 3\n  quote: The analysis evidenced both tuned and non-tuned neurons, with an overall majority of\n    non-tuned cells (71.8% of all neurons were non-tuned; n = 10 mice, 49 fields of view, 1054\n    neurons; Fig. 2D,E)\n  expected:\n    quantity: percentage of neurons with no significant tuning\n    value: 71.8\n    tolerance: 7.2\n    unit: percent\n  depends_on:\n  - dataset-size\n  criterion: Tuning as the Methods (Measurements of Response Properties) give it, a neuron being\n    tuned when at least one of its three regression coefficients is significant after the false\n    discovery rate correction at P < 0.05. Readings run (open details 4 and 5) are BH ('pdep') and BY\n    ('dep'), with the family of all 3 x N p-values of a field or of the N p-values per feature, and\n    slopes of either sign or positive only. The percentage is computed pooled over neurons and, as\n    Figure 2E plots, as the mean over fields. Reproduced when a reading gives 71.8% within the\n    tolerance and non-tuned neurons are the majority.\n- id: fig2e-all-categories\n  statement: Among tuned neurons all categories of selectivity are represented, neurons tuned to\n    position only, velocity only, acceleration only, and neurons with mixed selectivity.\n  source: Results, paragraph 3; Figure 2E\n  quote: Within tuned neurons, all categories of selectivity were represented (Fig. 2E)\n  depends_on:\n  - fig2de-tuned-fraction\n  criterion: With the tuning of fig2de-tuned-fraction, neurons are classed as tuned to position\n    only, velocity only, acceleration only, or mixed (significant for two or more features; Methods).\n    Reproduced when each of the four classes holds at least one neuron over the data set, under the\n    reading that reproduces fig2de-tuned-fraction (each reading shown).\n- id: tuning-consistency\n  statement: Tuning was consistent across halves of the data; 95% of neurons had identical tuning to\n    at least one feature in the first and last pairs of recordings, and 81% to all three features.\n  source: Materials and Methods, Measurements of Response Properties, paragraph 2\n  quote: data were split into 2 subsets consisting of the first and last pairs of recordings. 95% of\n    neurons displayed identical tuning to at least one feature over the 2 subsets, and 81% displayed\n    identical tuning to all 3 features\n  expected:\n  - quantity: percentage of neurons with identical tuning to at least one feature in both halves\n    value: 95\n    tolerance: 9.5\n    unit: percent\n  - quantity: percentage of neurons with identical tuning to all three features in both halves\n    value: 81\n    tolerance: 8.1\n    unit: percent\n  depends_on:\n  - fig2de-tuned-fraction\n  criterion: The tuning procedure is run separately on recordings 1 and 2 and on recordings 3 and 4\n    of each field, with the reading of fig2de-tuned-fraction. Identical tuning to a feature means\n    the coefficient is significant in both halves or in neither. The denominator is not stated;\n    readings are all neurons, neurons tuned in the full data, and neurons tuned in at least one half.\n    Reproduced when both percentages fall within their tolerances under one reading.\n- id: shuffle-significance\n  statement: Scoring tuning by shuffling responses against stimulus amplitude (1000 repeats) in\n    place of the regression test gives no qualitative change in the results.\n  source: Materials and Methods, Measurements of Response Properties, paragraph 2\n  quote: We also assessed tuning significance via direct shuffling of responses with respect to\n    stimulus magnitude for each neuron (1000 repeats), with no qualitative change in results\n  depends_on:\n  - fig2de-tuned-fraction\n  - fig2e-all-categories\n  - fig3g-si-no-spatial-organization\n  criterion: For each neuron and feature the responses are shuffled across the amplitudes of that\n    waveform type 1000 times and the p-value is the fraction of shuffled slopes at least as extreme\n    as the observed one. Whether the false discovery rate correction is then applied is not stated;\n    both readings are run. Reproduced when, with this tuning, non-tuned neurons remain the majority,\n    all four tuned classes are represented, and the SI test of fig3g-si-no-spatial-organization still\n    finds no difference from shuffled data (P >= 0.05).\n- id: fig3b-example-correlation\n  statement: In an example field the mean pairwise correlation was 0.14, against 0.0022 when\n    responses were shuffled across stimulus presentations.\n  source: Results, paragraph 4; Figure 3A and 3B\n  quote: mean correlation coefficient was 0.14 ± 0.0062 compared with 0.0022 ± 0.0013 obtained by\n    shuffling responses of different neurons across stimulus presentations (n = 31 neurons\n  expected:\n  - quantity: mean pairwise correlation, example field (tolerance the paper's stated spread)\n    value: 0.14\n    tolerance: 0.0062\n  - quantity: mean pairwise correlation, shuffled, example field (tolerance the stated spread)\n    value: 0.0022\n    tolerance: 0.0013\n  depends_on:\n  - fig3c-correlation-above-shuffle\n  criterion: Method as fig3c-correlation-above-shuffle, on the example field. The field is not\n    identified (open detail 11); the author identifies it by matching the raster and field of Figure\n    3A to the data, and the claim cannot be tested if none matches. Reproduced when both means fall\n    within their tolerances; partially reproduced when the true mean exceeds the shuffled mean but a\n    value falls outside.\n- id: fig3c-correlation-above-shuffle\n  statement: Across the data set, pairwise correlations of neurons in a field were higher than for\n    shuffled data (0.1004 against 0.011, mean over 49 fields).\n  source: Results, paragraph 4; Figure 3C\n  quote: Taking all experiments into account, the correlation coefficient for the data set was\n    0.1004 ± 0.008 (mean ± SEM across fields of view), compared with 0.011 ± 0.0024 for shuffled\n    data (n = 49 fields of view including n = 1054 neurons; P = 1.11 × 10−9; Wilcoxon signed-rank\n    test; Fig. 3C)\n  statistics:\n  - test: Wilcoxon signed-rank test\n    p: 1.11e-9\n    n: 49 fields of view, 1054 neurons\n  expected:\n  - quantity: mean over fields of the mean pairwise correlation (tolerance the paper's SEM)\n    value: 0.1004\n    tolerance: 0.008\n  - quantity: mean over fields of the mean pairwise correlation, shuffled (tolerance the SEM)\n    value: 0.011\n    tolerance: 0.0024\n  depends_on:\n  - dataset-size\n  criterion: As the Methods (Measurements of Response Properties, paragraph 3) - for every pair of\n    neurons in a field, the Spearman correlation of their whole corrected fluorescence time series\n    over the four concatenated recordings; the field's value is the mean over pairs. Shuffled data\n    permute, for each neuron independently, the temporal order of its responses to the stimulus\n    presentations. Open (detail 7) - the signal is neuropil-corrected fluorescence before dF/F0 (main\n    reading, the Methods' \"corrected fluorescence\") or dF/F0; a presentation's segment runs from its\n    onset to the next onset, permuted over the whole concatenated series or within each recording;\n    the shuffled value is the mean over 100 permutations (a standard choice, the count the paper uses\n    for SI), one permutation shown as a variant. Reproduced when the Wilcoxon signed-rank test over\n    fields of true against shuffled means gives P < 0.05 with true above shuffled, and both means\n    fall within their tolerances; partially reproduced when the test holds and a mean falls outside.\n- id: neuropil-correlation\n  statement: Neuropil ROIs were more correlated with each other than neurons were (0.1792 against\n    0.1004 mean correlation; 10 neuropil ROIs per field).\n  source: Results, paragraph 4\n  quote: Neuropil responses were more correlated with each other than neuronal responses (for\n    neuropil, mean ± SEM coefficient was 0.1792 ± 0.0097; n = 49 fields including n = 490 ROIs; vs.\n    neurons, P = 2.13 × 10−7; Wilcoxon signed-rank test)\n  statistics:\n  - test: Wilcoxon signed-rank test\n    p: 2.13e-7\n    n: 49 fields, 490 neuropil ROIs\n  expected:\n    quantity: mean over fields of the mean pairwise neuropil correlation (tolerance the paper's SEM)\n    value: 0.1792\n    tolerance: 0.0097\n  depends_on:\n  - fig3c-correlation-above-shuffle\n  criterion: Ten ROIs per field chosen within the neuropil, their traces taken and correlated as for\n    neurons (fig3c-correlation-above-shuffle), the field's value the mean over the 45 pairs. The\n    size and placement of the neuropil ROIs are not given; the reading used is ROIs of the median\n    somatic ROI size placed at random in areas free of somata and vessels, with two independent\n    placements reported. Reproduced when the Wilcoxon signed-rank test over fields of neuropil\n    against neuronal means gives P < 0.05 with neuropil higher, and the neuropil mean falls within\n    the tolerance; partially reproduced when only the test holds.\n- id: fig3d-example-correlation-distance\n  statement: In the example field correlations decreased with distance, with a slope of -0.15 per mm\n    (0.0025 per mm for shuffled data), most of the fall-off within the first 100 um.\n  source: Results, paragraph 5; Figure 3D\n  quote: correlations decreased with distance, with a mean spatial gradient of −0.15 mm−1 (0.0025\n    mm−1 for shuffled data; Fig. 3D). Most of the fall-off in correlation occurred within the first\n    100 μm of distance between neurons\n  expected:\n  - quantity: slope of correlation against distance, example field\n    value: -0.15\n    tolerance: 0.015\n    unit: 1/mm\n  - quantity: slope of correlation against distance, shuffled, example field\n    value: 0.0025\n    tolerance: 0.00025\n    unit: 1/mm\n  depends_on:\n  - fig3b-example-correlation\n  criterion: The example field of fig3b-example-correlation. The slope is that of the least-squares\n    line of pair correlation on distance between ROI centroids, in mm (open detail 8). The\n    shuffled slope is near zero, so 10% of it is a strict bound; it is reproduced when it lies\n    within 0.01 per mm of zero, reported against the paper's value. Most of the fall-off within 100\n    um is judged with 100 um bands taken from the sentence - reproduced when the drop in mean\n    correlation from 0-100 um to 100-200 um exceeds the drop from 100-200 um to 200-300 um.\n- id: fig3e-correlation-falls-with-distance\n  statement: Over the data set, correlations fell with distance between neurons, with a median\n    slope of -0.29 per mm against -0.0062 per mm for shuffled data.\n  source: Results, paragraph 5; Figure 3E\n  quote: For the complete data set, the spatial gradient was −0.29 ± 0.062 mm−1 (median ± standard\n    error of median [SEM]), significantly different than for shuffled data, −0.0062 ± 0.014 mm−1 (n\n    = 49 fields of view; P = 1.31 × 10−8; Wilcoxon signed-rank test; Fig. 3E)\n  statistics:\n  - test: Wilcoxon signed-rank test\n    p: 1.31e-8\n    n: 49 fields of view\n  expected:\n  - quantity: median over fields of the slope of correlation on distance (tolerance the paper's SEM)\n    value: -0.29\n    tolerance: 0.062\n    unit: 1/mm\n  - quantity: median over fields of the shuffled slope (tolerance the paper's SEM)\n    value: -0.0062\n    tolerance: 0.014\n    unit: 1/mm\n  depends_on:\n  - fig3c-correlation-above-shuffle\n  criterion: For each field, the slope of the least-squares line of pair correlation (as in\n    fig3c-correlation-above-shuffle) on centroid distance in mm, and the same for shuffled data.\n    The Results examine distances \"up to 300 um\"; readings are all pairs and pairs up to 300 um\n    (open detail 8). Reproduced when the Wilcoxon signed-rank test over fields of true against\n    shuffled slopes gives P < 0.05 with true slopes more negative, and both medians fall within their\n    tolerances; partially reproduced when only the test holds.\n- id: correlation-gradient-beyond-200um\n  statement: For pairs of neurons more than 200 um apart the correlation-distance slope did not\n    differ from shuffled data (-0.13 against -0.109 per mm, P = 0.106), so correlations fall off over\n    about 200 um, the diameter of a barrel column.\n  source: Results, paragraph 5\n  quote: Yet for experiments with pairs of neurons separated by over 200 μm, the spatial gradient\n    decreased to −0.13 ± 0.17 mm−1, compared with −0.109 ± 0.085 mm−1 for shuffled data (median, SEM;\n    n = 30 fields of view with >4 pairs extending >200 μm; P = 0.106; Wilcoxon signed-rank test)\n  statistics:\n  - test: Wilcoxon signed-rank test\n    p: 0.106\n    n: 30 fields of view with more than 4 pairs over 200 um apart\n  expected:\n  - quantity: median slope, pairs over 200 um (tolerance the paper's SEM)\n    value: -0.13\n    tolerance: 0.17\n    unit: 1/mm\n  - quantity: median shuffled slope, pairs over 200 um (tolerance the paper's SEM)\n    value: -0.109\n    tolerance: 0.085\n    unit: 1/mm\n  - quantity: fields with more than 4 pairs over 200 um apart\n    value: 30\n    tolerance: 3\n  depends_on:\n  - fig3e-correlation-falls-with-distance\n  criterion: A claim of absence, judged on the paper's test - Wilcoxon signed-rank over fields of\n    true against shuffled slopes; reproduced when P >= 0.05, not reproduced when P < 0.05, with the\n    median difference given either way. Fields are those with more than 4 pairs over 200 um apart.\n    The text reads most directly as slopes fitted to the pairs over 200 um apart, which is the main\n    reading; slopes over all pairs of those fields are shown as a variant.\n- id: fig3f-example-si-distance\n  statement: In the example field the tuning similarity index fell with distance (slope -1.29 per mm\n    against 0.133 per mm shuffled).\n  source: Results, paragraph 6; Figure 3F\n  quote: for the example in Fig. 3F, spatial gradient = −1.29 mm−1; compared with shuffled, 0.133\n    mm−1; n = 29 neurons, n = 465 pairs\n  expected:\n  - quantity: slope of SI on distance, example field\n    value: -1.29\n    tolerance: 0.129\n    unit: 1/mm\n  - quantity: mean shuffled slope of SI on distance, example field\n    value: 0.133\n    tolerance: 0.0133\n    unit: 1/mm\n  - quantity: neuron pairs in the example field\n    value: 465\n    tolerance: 47\n  depends_on:\n  - fig3b-example-correlation\n  - fig3g-si-no-spatial-organization\n  criterion: The example field of fig3b-example-correlation (Figure 3F legend, \"the field of view\n    in A\"), with SI and shuffles as in fig3g-si-no-spatial-organization. The paper gives 29 neurons\n    and 465 pairs, and 31 neurons for the same field in Figure 3B (open detail 11); 465 pairs is the\n    count of 31 neurons, all pairs. The slope values depend on the SI scale (open detail 9) and\n    are compared under each reading. Reproduced when the true slope is negative, the shuffled slope\n    is above it, and both fall within their tolerances under one reading; partially reproduced when\n    only the signs and order hold.\n- id: fig3g-si-no-spatial-organization\n  statement: Pooled across fields, tuning similarity showed no consistent spatial organization; the\n    slope of SI on distance did not differ from shuffled data (median -0.467 against -0.0169 per mm,\n    26 fields, P = 0.114), so neurons tuned to different features are interspersed.\n  source: Results, paragraph 6; Figure 3G; Discussion, paragraph 1\n  quote: However, pooling across experiments indicated no consistent spatial organization of SI\n    (median slope −0.467 ± 0.000675 mm−1; for shuffled data, −0.0169 ± 0.119 mm−1; n = 26 fields of\n    view; P = 0.114; Wilcoxon signed-rank test; Fig. 3G). These results confirm a visual intuition\n    from Fig. 2F\n  statistics:\n  - test: Wilcoxon signed-rank test\n    p: 0.114\n    n: 26 fields of view\n  expected:\n  - quantity: median over fields of the slope of SI on distance\n    value: -0.467\n    tolerance: 0.047\n    unit: 1/mm\n  - quantity: median over fields of the mean shuffled slope (tolerance the paper's SEM)\n    value: -0.0169\n    tolerance: 0.119\n    unit: 1/mm\n  - quantity: fields in the analysis\n    value: 26\n    tolerance: 3\n  depends_on:\n  - fig2de-tuned-fraction\n  criterion: As the Methods (Measurements of Response Properties, paragraph 3) - each neuron's\n    tuning vector is its three coefficients with non-significant ones set to zero; SI of a pair is\n    the dot product of the two vectors; the slope of the least-squares line of SI on centroid\n    distance in mm is compared with shuffled data, made by reassigning tuning vectors at random\n    across the neurons of the field, 100 times, the field's shuffled value being the mean slope. A\n    claim of absence, judged on the Wilcoxon signed-rank test over fields of true against shuffled\n    slopes - reproduced when P >= 0.05, not reproduced when P < 0.05, with the median difference\n    given either way. The paper does not say which 26 fields enter (open detail 9); the main\n    reading takes all pairs of all neurons (465 pairs of 31 neurons in the example) in fields with\n    at least two tuned neurons, since SI is zero for every pair otherwise. SI of unit-length tuning\n    vectors is shown as a variant, as the paper's slope magnitudes may imply a normalized scale.\n    The paper's SEM for the true median (0.000675) is about 0.1% of the value and is not used as\n    the tolerance; 10% is used.\n- id: fig4c-barrel-septum-tuned\n  statement: In 3 mice with reconstructed barrel maps, tuned neurons were evenly distributed between\n    barrel- and septum-related areas (38.8% and 35.8% tuned, P = 0.58).\n  source: Results, paragraph 7; Figure 4B and 4C\n  quote: n = 3 mice; respectively, n = 167, 102, and 117 imaged neurons, of which n = 59, 39, and 47\n    were tuned ... Tuned neurons were evenly distributed between barrel- and septum-related areas\n    (38.8% and 35.8%, respectively were tuned; P = 0.58; Fisher exact test; Fig. 4C)\n  statistics:\n  - test: Fisher exact test\n    p: 0.58\n    n: 386 neurons from 3 mice\n  expected:\n  - quantity: imaged neurons, mouse 1 of the reconstructed three\n    value: 167\n    tolerance: 17\n  - quantity: imaged neurons, mouse 2\n    value: 102\n    tolerance: 10\n  - quantity: imaged neurons, mouse 3\n    value: 117\n    tolerance: 12\n  - quantity: tuned neurons, mouse 1\n    value: 59\n    tolerance: 6\n  - quantity: tuned neurons, mouse 2\n    value: 39\n    tolerance: 4\n  - quantity: tuned neurons, mouse 3\n    value: 47\n    tolerance: 5\n  - quantity: percentage of barrel-related neurons tuned\n    value: 38.8\n    tolerance: 3.9\n    unit: percent\n  - quantity: percentage of septum-related neurons tuned\n    value: 35.8\n    tolerance: 3.6\n    unit: percent\n  depends_on:\n  - fig2de-tuned-fraction\n  criterion: The three mice are those with histology (experiments 8 to 10 in the data set's\n    description). Each neuron is placed on the barrel map by aligning the imaged field to the\n    reconstruction (Methods, Histology and Barrel Field Reconstruction) and assigned to barrel or\n    septum by its soma centre. A claim of absence, judged on the Fisher exact test of tuned against\n    non-tuned by barrel against septum over the pooled neurons - reproduced when P >= 0.05, not\n    reproduced when P < 0.05, with the two percentages given either way. If the histology PDFs do not\n    allow the registration, the claim cannot be tested.\n- id: fig4d-border-distance-by-feature\n  statement: Neurons tuned to position, velocity and acceleration did not differ in their distance\n    to the nearest barrel border (P = 0.77, 0.70 and 0.68), so feature tuning is not organized\n    relative to the barrel map.\n  source: Results, paragraph 7; Figure 4D\n  quote: Neurons tuned to different features were not located differently relative to barrel\n    borders, that is, relative to the columnar structure of barrel cortex (position vs. velocity: P =\n    0.77; position vs. acceleration: P = 0.70; velocity vs. acceleration: P = 0.68; Kolmogorov–Smirnov\n    2-sample test; Fig. 4D)\n  statistics:\n  - about: position against velocity\n    test: Kolmogorov-Smirnov 2-sample test\n    p: 0.77\n  - about: position against acceleration\n    test: Kolmogorov-Smirnov 2-sample test\n    p: 0.7\n  - about: velocity against acceleration\n    test: Kolmogorov-Smirnov 2-sample test\n    p: 0.68\n  depends_on:\n  - fig4c-barrel-septum-tuned\n  criterion: For each significantly tuned neuron of the three mice, the horizontal distance from\n    its soma to the nearest barrel border on the registered map. A claim of absence, judged on the\n    three Kolmogorov-Smirnov 2-sample tests - reproduced when all give P >= 0.05, not reproduced when\n    any gives P < 0.05, with the medians given. The paper does not say where a neuron tuned to several\n    features goes or whether the distance is signed (open detail 10); the main reading puts a neuron\n    in every group it is significantly tuned to (the Methods allow mixed selectivity) and uses the\n    unsigned distance, as the text says \"distance ... to the nearest barrel border\". Single-feature\n    neurons only, and the signed distance (inside barrels positive), are shown as variants.\n"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
python tools/claims_check.py claims/martini-2017.yaml paper/10.1093-cercor-bhx019.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
grep -n ": [^ ]" claims/martini-2017.yaml | grep -v "^[0-9]*:#" | grep -vE "^[0-9]+: *(- )?[a-z_]+: "
```

```
198:    allows, each run on all segmented neurons, pooled across fields: (a) the mean response amplitude
555:    borders, that is, relative to the columnar structure of barrel cortex (position vs. velocity: P =
556:    0.77; position vs. acceleration: P = 0.70; velocity vs. acceleration: P = 0.68; Kolmogorov–Smirnov
```

**Agent calls Bash**

```bash
python - <<'EOF'
p='claims/martini-2017.yaml'
s=open(p).read()
s=s.replace("pooled across fields: (a) the mean","pooled across fields, are (a) the mean")
old="""    borders, that is, relative to the columnar structure of barrel cortex (position vs. velocity: P =
    0.77; position vs. acceleration: P = 0.70; velocity vs. acceleration: P = 0.68; Kolmogorov–Smirnov
    2-sample test; Fig. 4D)"""
new="""    borders, that is, relative to the columnar structure of barrel cortex ... Kolmogorov–Smirnov
    2-sample test; Fig. 4D)"""
assert old in s
s=s.replace(old,new)
open(p,'w').write(s)
EOF
python tools/claims_check.py claims/martini-2017.yaml paper/10.1093-cercor-bhx019.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
grep -n -e "—" -e "rather" claims/martini-2017.yaml; python -c "
import yaml;d=yaml.safe_load(open('claims/martini-2017.yaml'));c=d['claims'];print(len(c),sum('statistics' in x for x in c),sum('criterion' in x for x in c),sum('expected' in x for x in c))"
```

```
18 8 18 15
```

**Agent**

I wrote `claims/martini-2017.yaml`. The quote checker reports 18 claims, 18 quotes, 15 statistical values and 0 problems. Nothing is committed.

**Text read:** the version of record (open access), extracted from the PDF, with the main text, Methods and figure legends. The supplement (`text_suppmat.docx`) only holds the legends of Supplementary Figs 1 to 3, which repeat Figs 2C, 2F and 4B split by colour channel. I did not need to open the PDF. The paper links no analysis code. It only names the tools it used: StackReg, Caltracer 2.5 and Groppe's `fdr_bh`.

**Claims:** 18, all with quotes and none marked `inferred`.
- 8 claims carry statistics: six Wilcoxon signed-rank tests, one Fisher exact test and three Kolmogorov–Smirnov tests, plus the 5–95% confidence intervals for the example neuron.
- 15 claims have expected values and all 18 have a criterion.
- 4 claims say an effect is absent: the correlation slope beyond 200 µm (P = 0.106), the similarity-index slope (Fig 3G, P = 0.114), barrel against septum (Fig 4C, P = 0.58) and distance to the barrel border (Fig 4D).
- Where the paper gives a SEM, I used it as the tolerance. The exception is the median similarity-index slope: its SEM of 0.000675 is about 0.1% of the value, so I used 10% and said why in the file.

**Details the paper leaves open, and the readings named:**
1. **Segmentation and field exclusion:** the halo width, the blood-vessel background, and how one set of ROIs covers the 4 movies of a field are not given. I used one ROI set on the mean of the registered movies. The motion threshold for discarding fields is not given either.
2. **Response window:** the frame boundaries around stimulus onset are not given. I took the first frame at or after onset as the first frame "after", a standard choice.
3. **Amplitude units in the regression:** normalized 1, 3, 5 (the Fig 2B legend) or command voltage, and ΔF/F0 as a fraction or a percent. This changes coefficient sizes but not significance.
4. **Slope test sign:** a significant slope of either sign counts as tuned, or positive only.
5. **False discovery rate:** `fdr_bh` with 'pdep' (Benjamini–Hochberg) or 'dep' (Benjamini–Yekutieli). The family is either all 3×N p-values of a field or N per feature.
6. **"Responded" (50.2%):** never defined. Readings: (a) a test over all presentations; (b) any one of the nine stimuli significant, with FDR correction.
7. **Correlations:**
   - Signal: neuropil-corrected fluorescence, or ΔF/F0.
   - Shuffle segments: permuted across the whole concatenated series, or within each recording.
   - Shuffle count: not given, so I used 100, with a single shuffle as a variant.
8. **Distance:** between ROI centroids, using all pairs or only pairs up to 300 µm.
9. **Similarity index:**
   - The paper does not say which 26 of the 49 fields entered. The main reading is fields with at least two tuned neurons.
   - Scale: the raw dot product the Methods give, or unit-length vectors.
10. **Fig 4D:** a neuron tuned to several features is counted in every group it is tuned to, or only single-feature neurons are used. The distance is either unsigned or signed.
11. **Beyond 200 µm:** the slope is fitted to pairs over 200 µm apart (main reading) or to all pairs of those 30 fields.
12. **Tuning consistency (95% and 81%):** the denominator is all neurons, tuned neurons, or neurons tuned in either half.
13. **Tuning by shuffle:** whether the FDR correction is applied after the 1000-repeat shuffle is not stated, so both are run.

**Missing from the paper:**
- **Unidentified examples:** the paper does not say which mouse, field or ROI the example neuron (Fig 2A–C) and the example field (Fig 3A/B/D/F) come from. The author has to match them from the figures, or those claims cannot be tested.
- **Inconsistent example size:** the example field has two sizes in the paper: 31 neurons (Fig 3B), and 29 neurons with 465 pairs (Fig 3F). 465 is the number of pairs among 31 neurons.
- **Raw data only:** the dataset description says it holds raw movies, stimulus signals and histology PDFs, but no ROIs or tuning labels. Neurons must be segmented again, so the counts carry a 10% tolerance.

## End of run

14 turns, 5 minutes, $1.40 at API prices, result: success.
