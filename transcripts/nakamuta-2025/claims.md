# 002020 · claims · run 39533162544

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cat docs/protocol.md; ls claims/001453/ claims/002020/ paper/ 2>&1; ls tools
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cat claims/001453/*.yaml | head -150; wc -l paper/*.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cat paper/10.1101-2025.01.14.630383.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1101-2025.01.14.630383.txt"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
grep -n -i -E "github|code|zenodo|dandi|availab" paper/*.txt | head; ls paper -la; grep -rn "002020" --include=*.yaml --include=*.json --include=*.md . 2>/dev/null | grep -v transcripts | head
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -n 6550,6600p targets/dandisets.json; sed -n 1945,1965p papers/manifest.yaml
```

```
"resource_type": null,
     "preprint": false
    }
   ],
   "catalystneuro": [
    "conversion code at https://github.com/catalystneuro/schwerdt-lab-to-nwb",
    "contributor Weigl, Szonja of CatalystNeuro"
   ]
  },
  {
   "dandiset": "002020",
   "name": "High-density MEA recordings of spontaneous activity in developing rat cortical cultures",
   "published_version": "0.261004.1410",
   "asset_count": 129,
   "size_gb": 1.18,
   "data_standards": [
    "Neurodata Without Borders (NWB)"
   ],
   "species": [
    "Rattus norvegicus - Norway rat"
[... 38 more lines not kept]
```

**Agent calls Bash**

```bash
curl -s https://api.dandiarchive.org/api/dandisets/002020/versions/0.261004.1410/info/ | python -c "import json,sys;d=json.load(sys.stdin);m=d['metadata'];print(m.get('name'));print(m.get('description'));print(m.get('relatedResource'))"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
grep -rn -i -B2 -A8 "model simulation\|simulat" claims/*/*.yaml | grep -i -E "data:|criterion|simul" | head -20; ls claims | head -50; cat tools/claims_check.py | head -60
```

```
claims/000009/10.1038-nature22324.yaml:649:  criterion: A simulation, not a test on recorded data; its parameters are in the Supplementary
claims/000070/10.1038-nature11129.yaml:275:  statement: A simulated population of units tuned to hand velocity and speed, with
claims/000070/10.1038-nature11129.yaml:285:  criterion: One simulated dataset per array dataset from that session's condition-mean hand
claims/000070/10.1038-nature11129.yaml:286:    kinematics (`simulate_population`, fixed seed), analysed as the data. Reproduced when, in
claims/000070/10.1038-nature11129.yaml:291:  statement: A simulated population tuned to hand position, velocity, acceleration and jerk
claims/000070/10.1038-nature11129.yaml-298-  criterion: As for fig6-velocity-model, with the complex kinematic model.
claims/000070/10.1038-nature11129.yaml:331:    correlations of 0.97 to 0.99, and its simulated units resemble real neurons.
claims/000070/10.1038-nature11129.yaml:335:    fit/EMG correlation ranged from 0.97–0.99 across datasets ... Simulated units displayed
claims/000947/10.1371-journal.pbio.3000829.yaml:499:- id: fig6-simulation
claims/000947/10.1371-journal.pbio.3000829.yaml:502:  source: Results, Simulations suggest GPi-VLa communication scales with GPi synchrony and
claims/000947/10.1371-journal.pbio.3000829.yaml-507-  data: elsewhere
claims/000947/10.1371-journal.pbio.3000829.yaml:508:  where: Dryad doi:10.5061/dryad.0cfxpnvxm (Data_Fig6.mat, simulation output), mirrored on Zenodo
000003
000004
000005
000006
000008
000009
000035
000041
[... 102 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 640,660p claims/000009/10.1038-nature22324.yaml; python -c "import json;d=json.load(open('schemas/claims.schema.json'));print(json.dumps(d,indent=1))" | head -200
```

```
source: Results, Thalamus drives ALM preparatory activity, paragraph 3; Extended Data Figure 6d;
    Supplementary information
  quote: Even when 100% of the input neurons were inhibited, we expect to observe latency of 1.8 ± 0.7
    ms
  expected:
    quantity: model latency, all inputs inhibited
    value: 1.8
    tolerance: 0.7
    unit: ms
  criterion: A simulation, not a test on recorded data; its parameters are in the Supplementary
    information, which is not in the text read. Cannot be specified from the text; recorded so the
    finding is covered.
- id: fig5-weak-photoinhibition-rates
  statement: Weak thalamus photoinhibition (20-fold weaker, 0.5 mW) significantly changed the spike rate
    of 83 of 160 ALM neurons, with a mean reduction of 1.2 spikes per s; 39% of the changed neurons
    (32/83) increased their rate.
  source: Results, Thalamus contributes to selectivity in ALM, paragraph 1; Figure 5b
  quote: 83 /160 of ALM neurons showed statistically significant changes in mean spike rate during
    photoinhibition ( t -test; average reduction of spike rate, 1.2 ± 0.2 spikes per s, mean ± SEM, n =
    160; Fig. 5a, b ). A substantial fraction of these neurons (39%, 32/83) showed increases in spike
[... 201 more lines not kept]
```

**Agent calls Write**

```json
{
 "file_path": "claims/002020/10.1101-2025.01.14.630383.yaml",
 "content": "# Claims for \"Self-organization of high-dimensional geometry of neural activity in culture\"\n# (doi:10.1101/2025.01.14.630383) on dandiset 002020.\n# Written by an agent (model \"claude-opus-5-5\", Claude Code in GitHub Actions), 2026-10-21,\n# protocol pilot-10 as stated in docs/protocol.md.\n#\n# Text read: the bioRxiv preprint, version 1, full text flattened from the bioRxiv JATS XML\n# (paper/10.1101-2025.01.14.630383.txt): Introduction, Results, figure legends, Discussion and\n# Methods. No PDF was supplied. The supplement (Figures S1 and S2) is not in the text; only the\n# Results sentences that cite them were read. The dandiset's related resource points at\n# version 2 of the preprint, which was not read. The equations of the Methods (local Moran's I,\n# the fitted function, the model's update rule and connection distributions) are lost in the\n# flattened text; only their surrounding words survive. The paper links no analysis code and\n# has no code or data availability statement, so no repository was read.\n#\n# Data the paper used, as it reports them. Dissociated cortical neurons from E18 rat embryos,\n# about 380,000 cells per dish, cultured on MaxOne high-density multi-electrode arrays (26,400\n# electrodes over 3.85 mm by 2.10 mm). Each day, 30 s of activity was recorded on all\n# electrodes, up to 1,024 electrodes with the largest mean spike amplitudes were selected, and\n# 30 minutes of spontaneous activity were recorded on them. Activity became detectable at about\n# 2 to 3 DIV; recordings shown run to at least 19 DIV. Analysed were dishes with spontaneous\n# activity observed continuously for more than 10 days, seven dishes in all, and activity with\n# frequency above 0.03 Hz. The measured variable is spike times per electrode; the analyses\n# also need each electrode's position (for Moran's I) and each recording's DIV and dish. There\n# are no stimuli or conditions; the only manipulation is a temporal shuffle done in analysis\n# (an independent circular shift of each electrode's time series). The dandiset's description\n# (seven cultures, daily 30-minute recordings of up to 1,024 of 26,400 electrodes) matches.\n#\n# Shared method, from the Methods unless said otherwise.\n# - Selection. Dishes with activity observed for more than 10 days; \"spontaneous activity data\n#   with frequencies greater than 0.03 Hz\". Open, with readings (S1) electrodes whose mean rate\n#   over the 30 minutes exceeds 0.03 Hz are kept, (S2) recordings whose mean rate over\n#   electrodes exceeds 0.03 Hz are kept.\n# - PCA. Spike counts in 100 ms bins (18,000 bins in 30 minutes) for each electrode; the\n#   eigenvalues of the electrode by electrode covariance matrix, ranked in descending order,\n#   are the variance spectrum. The covariance is used as written, without z-scoring. Converting\n#   counts to rates scales all eigenvalues alike and cannot change b or c below.\n# - Fit (Methods, Parameter fitting). The text says each graph is fitted to \"a product of\n#   power-law decay and exponential decay\" with parameters a, b, c, by least squares, with\n#   b >= 0, behaving as a power law for small x; the formula itself is lost. It is read as\n#   f(x) = a x^(-c) exp(-b x), where x is the PC rank (or cascade size), b the exponential\n#   decay rate and c the power exponent. Open, with readings (F1) the squared error on log\n#   values (the graphs are plotted on log-log axes), (F2) the squared error on the raw values.\n#   The ranks fitted for the variance spectrum are not given; the reading is all ranks with a\n#   positive eigenvalue. For avalanches the fit is over cascade sizes 1 to 128 (Methods).\n# - Shuffle (Figure 1D legend). Each electrode's binned series is circularly shifted by an\n#   independent random amount; the seed is a standard choice.\n# - Spatial structure (Methods, Spatial structure of PCs). For PC k, local Moran's I at\n#   electrode i from the PC weights, with w_ij = 1 for electrodes within 200 um and 0\n#   otherwise, row-normalized; the locality of PC k is the number of electrodes with local\n#   Moran's I above 0.0001; the locality spectrum is locality against PC index; the locality\n#   slope is the slope of a linear fit to the locality spectrum on a semi-logarithmic scale.\n#   The formula is lost. Open, with readings (M1) Anselin's local Moran's I,\n#   n (x_i - mean) sum_j w_ij (x_j - mean) / sum_k (x_k - mean)^2, (M2) the same without the\n#   normalization by the variance, (x_i - mean) sum_j w_ij (x_j - mean). Whether w_ii counts\n#   (distance 0 is within 200 um) is open; the reading is the usual one, w_ii = 0, with\n#   w_ii = 1 as a variant. Which axis is logarithmic is open, with readings (L1) locality\n#   against log PC index, (L2) log locality against PC index. The moving average of 10 PCs\n#   in Figure 2C is for display only.\n# - Avalanches (Methods, Neuronal avalanches). A cascade is a run of spikes whose\n#   inter-spike intervals are shorter than the mean inter-spike interval (mISI), following\n#   ref. 22. The reading is that spikes of all electrodes are pooled into one train and the\n#   mISI is that train's mean interval. The size S is open, with readings (A1) the number of\n#   spikes in the cascade, (A2) the number of distinct electrodes in it. P(S) is the fraction\n#   of cascades of size S.\n# - Groups (Results, Co-occurrence, paragraph 3). \"Power law\" group, PCA exponential decay\n#   rate b below 0.1; \"Exponential\" group, all others.\n# Where the readings above give different outcomes for a claim, the claim is blocked as\n# methods_underspecified, with every result shown.\nschema_version: 2\ndataset:\n  archive: dandi\n  id: \"002020\"\npaper: doi:10.1101/2025.01.14.630383\nclaims:\n- id: dishes-analysed\n  statement: Seven dishes met the paper's inclusion rule (spontaneous activity observed\n    continuously for more than 10 days) and were summarized.\n  source: Results, Self-organization of power law in PCA, paragraph 3; Methods, Data processing\n    and principal component analysis, paragraph 1\n  quote: Averaging data across seven dishes revealed that power law in PCA was consistently\n    established around 15 DIV\n  expected:\n    quantity: dishes with activity observed for more than 10 days\n    value: 7\n    tolerance: 0\n    unit: dishes\n  criterion: Count the dishes whose recordings with activity above 0.03 Hz (reading S1 or S2)\n    span more than 10 days. A count of dishes is exact; tolerance 0 for that reason.\n- id: activity-onset\n  statement: Spontaneous activity became detectable at about 2 to 3 DIV.\n  source: Results, Self-organization of power law in PCA, paragraph 1\n  quote: Spontaneous activity became detectable approximately 2 – 3 days in vitro (DIV)\n  expected:\n    quantity: earliest DIV with detectable spontaneous activity, median over dishes\n    value: 2.5\n    tolerance: 0.8\n    unit: DIV\n  criterion: For each dish, the earliest DIV with a recording whose activity exceeds 0.03 Hz\n    (readings S1, at least one electrode above 0.03 Hz, or S2). Reproduced when the median over\n    dishes lies within the reported range 2 to 3 widened by 10% of each bound (1.8 to 3.3).\n    The paper gives no detection rule beyond the 0.03 Hz selection, which is used for that\n    reason. If the dataset starts each dish later than this, the claim cannot be tested.\n- id: fig1b-async-to-bursts\n  statement: As the cultures matured, spiking changed from asynchronous firing to synchronous\n    bursting.\n  source: Figure 1B; Results, Self-organization of power law in PCA, paragraphs 1 and 4\n  quote: During this transition from exponential to power-law decay, spiking activity evolved\n    from asynchronous firing to synchronous bursting\n  criterion: The paper shows this in raster plots only and defines no burst or synchrony\n    measure. Readings, each over all recordings of all dishes against DIV, (a) the mean\n    pairwise Pearson correlation of the 100 ms spike counts (the bins of the Methods), (b) the\n    largest fraction of electrodes active within one 100 ms bin, as a share of electrodes.\n    Reproduced when under each reading the Spearman correlation with DIV is positive with\n    p < 0.05, and the dish median at 15 DIV and later exceeds that at 3 to 5 DIV. The test and\n    threshold are a reading of \"evolved\" chosen here, as the paper gives none.\n- id: fig1d-power-law-emerges\n  statement: In early cultures the variance spectrum decays faster than a power function; as\n    the culture matures it follows a power function, linear on log-log axes.\n  source: Figure 1D; Results, Self-organization of power law in PCA, paragraph 2\n  quote: Initially, the variance spectrum decayed more rapidly than a power function. However,\n    as the culture matured, the spectrum began to follow a power function, appearing linear on a\n    bilogarithmic scale\n  criterion: Fit b per recording (fit readings F1 and F2). Reproduced when in a majority of the\n    seven dishes the recordings of the first three recorded DIV have b at or above 0.1 and the\n    recordings from 15 DIV on have b below 0.1. The 0.1 boundary is the paper's own threshold\n    between its Exponential and Power-law groups (Results, Co-occurrence, paragraph 3).\n- id: fig1e-example-dish\n  statement: In the example dish the variance spectrum shifted from exponential to power-law\n    decay around 10 DIV and stayed so to at least 19 DIV, with a power-law fit of exponent\n    1.30.\n  source: Figure 1E and legend; Results, Self-organization of power law in PCA, paragraph 2\n  quote: in this dish, the variance spectrum shifted from exponential decay to power-law decay\n    around 10 DIV and remained stable at least until 19 DIV\n  expected:\n  - quantity: DIV of the shift to power-law decay in the example dish\n    value: 10\n    tolerance: 1\n    unit: DIV\n  - quantity: power exponent of the fit in Figure 1E\n    value: 1.30\n    tolerance: 0.13\n  criterion: The example dish is not identified, and the paper does not say which spectra the\n    red line of Figure 1E fits. The shift is the first DIV from which b stays below 0.1 (the\n    paper's group threshold). The exponent is read as (a) the median of c over that dish's\n    recordings from the shift to 19 DIV, (b) c fitted to the 19 DIV spectrum, (c) a pure power\n    law fitted to all the dish's spectra from the shift on, pooled. Reproduced when at least one\n    of the seven dishes has a shift within tolerance, b below 0.1 at every recording from the\n    shift to 19 DIV, and an exponent within tolerance under one reading, with fit reading F1 or\n    F2.\n- id: fig1f-transition-15div\n  statement: Across seven dishes the exponential decay rate of the variance spectrum is large\n    early in development and falls as the culture matures, so that the power law in PCA is\n    established around 15 DIV.\n  source: Figure 1F (left); Results, Self-organization of power law in PCA, paragraph 3\n  quote: The exponential decay rate, which quantifies the degree of exponential decay, was large\n    in the early stages of development, indicating a dominance of exponential decay. As the\n    culture matured, the decay rate decreased, reflecting a shift toward power-law decay\n  expected:\n    quantity: DIV at which the power law in PCA is established, over seven dishes\n    value: 15\n    tolerance: 1.5\n    unit: DIV\n  criterion: Fit b per recording (F1 and F2). The decrease holds when the Spearman correlation\n    of b with DIV over all recordings is negative. \"Established\" is read as the first DIV from\n    which b stays below 0.1 (the paper's group threshold), taken as (a) on the 3-day moving\n    average over DIV of b pooled over dishes (the thick line of Figure 1F), (b) per dish, the\n    median over dishes. Reproduced when b decreases with DIV and the DIV is within tolerance\n    under one reading.\n- id: fig1f-exponent-1p2\n  statement: Once established, the power-law exponent of the variance spectrum stabilized at\n    about 1.2.\n  source: Figure 1F (right); Results, Self-organization of power law in PCA, paragraph 3\n  quote: The powerlaw exponent stabilized at approximately 1.2\n  depends_on:\n  - fig1f-transition-15div\n  expected:\n    quantity: power exponent c of the variance spectrum after the transition\n    value: 1.2\n    tolerance: 0.12\n  criterion: The exponent c of the fit, over recordings after the transition DIV found in\n    fig1f-transition-15div. Readings (a) the median of c over those recordings, (b) the 3-day\n    moving average of c at the last DIV. Reproduced when the value is within tolerance under\n    one reading, with fit reading F1 or F2.\n- id: fig1d-shuffle\n  statement: Temporal shuffling leaves the variance spectrum unchanged early in development but,\n    once the power law has emerged, disrupts it and returns it to exponential decay.\n  source: Figure 1D, dashed lines and legend; Results, Self-organization of power law in PCA,\n    paragraph 4\n  quote: During the initial development period, shuffling did not alter the variance spectra.\n    However, after the emergence of the power law in PCA, shuffling significantly disrupted the\n    power law, reverting them to exponential decay\n  criterion: Shuffle each recording as in the Figure 1D legend and fit b to the original and the\n    shuffled spectra (F1 and F2). The paper reports no test. Early recordings are those in the\n    Exponential group (b at or above 0.1); late ones those in the Power-law group. Reproduced\n    when (i) in early recordings the median ratio of shuffled to original b lies within 0.9 to\n    1.1 (the registry's default 10%), and (ii) in late recordings the shuffled b is at or above\n    0.1 in a majority and exceeds the original b, with a one-sided Wilcoxon signed-rank test\n    over recordings at p < 0.05. The test and the 10% band are readings of \"did not alter\" and\n    \"significantly\" chosen here, as the paper gives none; the effect sizes are reported.\n- id: fig2b-spatial-structure\n  statement: Early in development (3 DIV) all PCs correspond to a few scattered electrodes; in\n    mature cultures (15 DIV) dominant PCs correspond to localized clusters of electrodes, while\n    minor PCs remain on globally distributed, sporadic electrodes.\n  source: Figure 2B; Results, Self-organization of spatial structure of PCs, paragraph 2\n  quote: In the early stages of development(3 DIV), all PCs corresponded to a small number of\n    scattered electrodes. However, as the culture matured (15 DIV), dominant PCs began to\n    correspond to localized clusters of electrodes, while minor PCs remained associated with\n    globally distributed, sporadic electrodes\n  depends_on:\n  - fig2c-locality-spectrum\n  criterion: Shown as maps of PC weights; judged with the paper's own measure. Reproduced when\n    fig2c-locality-spectrum is reproduced and, in a majority of dishes at 15 DIV (or the nearest\n    recorded DIV), the mean locality of the first 10 PCs exceeds that of the last 10, while at\n    3 DIV it does not exceed it by more than 10%. The 10-PC groups follow the window of the\n    Figure 2C moving average.\n- id: fig2c-locality-spectrum\n  statement: The locality spectrum (the number of electrodes with local Moran's I above\n    threshold, against PC index) is flat early in development and becomes steeper as the\n    culture matures.\n  source: Figure 2C; Results, Self-organization of spatial structure of PCs, paragraph 3\n  quote: Initially, the locality spectrum was flat, but as culture matured, it became steeper\n  criterion: Locality spectra and slopes as in the opening comment (readings M1 and M2, L1 and\n    L2). Steeper means a more negative slope (dominant PCs more local). Reproduced when the\n    Spearman correlation of the locality slope with DIV, over all recordings, is negative with\n    p < 0.05, and the median slope at 3 to 5 DIV is closer to zero than that at 15 DIV and\n    later. The test is a reading of \"became steeper\", which the paper does not test.\n- id: fig2d-locality-slope\n  statement: The slope of the locality spectrum confirms that spatial structure emerges\n    progressively and is absent in the initial stages of development.\n  source: Figure 2D; Results, Self-organization of spatial structure of PCs, paragraph 3\n  quote: analysis of the slope of the locality spectrum confirmed the progressive emergence of\n    spatial structure, which was absent during the initial stages of development\n  depends_on:\n  - fig2c-locality-spectrum\n  criterion: As fig2c-locality-spectrum, on the 3-day moving average of the slope over DIV\n    (Figure 2D, blue line). Reproduced when the moving average is near zero at the first\n    recorded DIVs (its magnitude below 10% of its most negative value) and falls over DIV,\n    without returning to zero once below half of its most negative value.\n- id: fig2d-shuffle-locality\n  statement: Temporal shuffling, which removes inter-electrode correlations, disrupts the\n    spatial structure of PCs; the locality spectrum becomes nearly independent of PC index.\n  source: Figure 2D, dashed line; Results, Self-organization of spatial structure of PCs,\n    paragraph 4\n  quote: applying a circular shift to data with an established spatial structure, which removed\n    inter-electrode correlations, disrupted the structure ... the locality spectrum became nearly\n    independent of the PC indices\n  depends_on:\n  - fig2c-locality-spectrum\n  criterion: Shuffle as in the Figure 1D legend. Data with established structure are read as\n    (a) recordings from 15 DIV on, (b) recordings in the PCA Power-law group. Reproduced when,\n    under each of M1 and M2 and L1 and L2, the median shuffled slope has a magnitude below 10%\n    of the median original slope and the shuffled slopes are less negative than the original\n    ones by a one-sided Wilcoxon signed-rank test at p < 0.05. \"Nearly independent\" and the test\n    are readings chosen here, as the paper gives no number or test.\n- id: fig3c-avalanches-emerge\n  statement: Across seven dishes the cascade size distribution shifted from exponential to\n    power-law decay at about 15 DIV, with a power exponent of about 1.5.\n  source: Figure 3C; Results, Co-occurrence of power law in PCA and neuronal avalanches,\n    paragraph 2\n  quote: Data summarized from seven dishes show that the distribution shifted from an\n    exponential decay to a power-law decay at approximately 15 DIV, with an exponent around 1.5\n  expected:\n  - quantity: DIV of the shift to power-law cascade size distributions\n    value: 15\n    tolerance: 1.5\n    unit: DIV\n  - quantity: power exponent of the cascade size distribution after the shift\n    value: 1.5\n    tolerance: 0.15\n  criterion: Cascades and sizes as in the opening comment (readings A1 and A2), fit over sizes 1\n    to 128 (F1 and F2), per recording. The shift DIV is read as in fig1f-transition-15div, on\n    the avalanche b with the same 0.1 boundary, (a) on the pooled 3-day moving average, (b) per\n    dish, the median. The exponent is the median c over recordings after the shift. Reproduced\n    when both values are within tolerance under one reading. The 0.1 boundary for avalanches is\n    carried over from the PCA groups; the paper gives none for avalanches.\n- id: fig3d-decay-rates-correlated\n  statement: The exponential decay rates of the variance spectrum and of the cascade size\n    distribution are positively correlated across recordings, so the two power laws are\n    established concurrently.\n  source: Figure 3D; Results, Co-occurrence of power law in PCA and neuronal avalanches,\n    paragraph 3\n  quote: A clear positive correlation between the two exponential decay rates indicates that\n    two power laws are established concurrently in the dissociated culture\n  criterion: One point per recording (all dishes and DIVs), PCA b against avalanche b, under\n    the fit, size and Moran-independent readings F1, F2, A1, A2. The paper reports no\n    correlation coefficient or test. \"Clear\" is read as a Spearman correlation and a Pearson\n    correlation both positive with two-sided p < 0.05, a reading chosen here; the coefficients\n    and their per-dish values are reported.\n- id: fig3ef-groups-cooccur\n  statement: Recordings classified by the PCA decay rate alone (Power-law group, b below 0.1)\n    show both power laws, while the Exponential group shows neither.\n  source: Figure 3E and 3F; Results, Co-occurrence of power law in PCA and neuronal avalanches,\n    paragraph 3\n  quote: Interestingly, although these groups were categorized based solely on the power law in\n    PCA, regardless of the power law in the neuronal avalanches, it was clearly observed that\n    both phenomena appeared in the Power-law group ( Fig. 3E ). In contrast, neither power law\n    was observed in the Exponential group\n  expected:\n    quantity: threshold on the PCA exponential decay rate b separating the groups\n    value: 0.1\n    tolerance: 0\n  criterion: Groups by PCA b with the paper's threshold 0.1 (tolerance 0, a method value used\n    as given). The panels show representative recordings. Readings, (a) per recording, the\n    avalanche b is lower in the Power-law group than in the Exponential group (one-sided\n    Mann-Whitney U, p < 0.05, a test chosen here) and the median avalanche b is below 0.1 in the\n    Power-law group and at or above 0.1 in the Exponential group; (b) the cascade size\n    distribution pooled over all recordings of each group, fitted, has b below 0.1 for the\n    Power-law group and at or above 0.1 for the Exponential group. Reproduced when one reading\n    holds under the fit and size readings.\n- id: figs1-classified-by-avalanches\n  statement: A similar co-occurrence is seen when recordings are classified by their neuronal\n    avalanches.\n  source: Figure S1, cited in Results, Co-occurrence of power law in PCA and neuronal avalanches,\n    paragraph 3\n  quote: A similar co-occurrence was also observed when data were classified based on the\n    neuronal avalanches (Fig. S1)\n  criterion: Figure S1 and its legend are not in the text read, so the threshold on the\n    avalanche b is not known. The reading is the same threshold as the PCA groups, 0.1, on the\n    avalanche b, with readings (a) and (b) of fig3ef-groups-cooccur applied with the roles of\n    the two decay rates swapped. A different threshold in the supplement could change the\n    outcome; the claim is open on that point until the supplement is read.\n- id: figs2-shuffle-breaks-cooccurrence\n  statement: The co-occurrence of the two power laws is easily disrupted by temporal shuffling,\n    reflecting that the two phenomena are not inherently associated.\n  source: Figure S2, cited in Results, Co-occurrence of power law in PCA and neuronal avalanches,\n    paragraph 3; Discussion, paragraph 2\n  quote: This co-occurrence is notable because it is easily disrupted by temporal shuffling,\n    reflecting that these phenomena are inherently unassociated (Fig. S2)\n  criterion: Figure S2 and its legend are not in the text read, so neither the shuffle applied\n    to the avalanche analysis nor the measure of disruption is known. Readings, on recordings\n    of the Power-law group shuffled as in the Figure 1D legend, (a) the shuffled data keep\n    avalanche b below 0.1 while their PCA b is at or above 0.1 (the Discussion says sequences\n    with avalanches but no power law in PCA are easy to construct), in a majority of recordings;\n    (b) over all recordings, the correlation of fig3d-decay-rates-correlated computed on\n    shuffled data is not positive with p < 0.05. The claim is open on this point until the\n    supplement is read; where the readings disagree it is blocked as methods_underspecified.\n- id: no-temporal-structure\n  statement: The cultures did not show the in vivo temporal structure of PCs, in which dominant\n    PCs have longer time scales than minor PCs.\n  source: Discussion, paragraph 4\n  quote: This temporal structure is characterized by dominant PCs exhibiting longer time scales,\n    while minor PCs exhibit shorter time scales. However, our study using the dissociated\n    neuronal culture was unable to replicate such a temporal structure\n  criterion: A claim of absence, but the paper names no measure or test. Readings, on\n    recordings from 15 DIV on, (a) the time scale of each PC's projection as the lag at which\n    its autocorrelation (100 ms bins) first falls below 1/e, (b) the integral of the positive\n    part of that autocorrelation; the claim holds when the Spearman correlation of time scale\n    with PC rank is not negative with p < 0.05 in a majority of recordings. As the paper names\n    no test, the outcome is reported under both readings, and the claim is blocked as\n    methods_underspecified where they disagree.\n- id: fig4d-cauchy-model-power-law\n  statement: In the binary threshold network with heavy-tailed (Cauchy) connections, the\n    variance spectrum decays exponentially for weak connections and becomes a power law at the\n    critical point, with exponent 1.56, where neuronal avalanches also occur.\n  source: Figure 4C and 4D; Results, Heavy-tailed connectivity is important for the\n    co-occurrence, paragraph 4\n  quote: The variance spectrum exhibited an exponential decay when the typical connection\n    strength was sufficiently smaller than the critical point. However, as the connection\n    strength increased, the spectrum transitioned to a power-law decay at the critical point.\n    ... The power-law exponent at the critical state was 1.56\n  expected:\n    quantity: power exponent of the model's variance spectrum at the critical point\n    value: 1.56\n    tolerance: 0.156\n  criterion: A simulation, not a test on the recorded data. The Methods give the threshold\n    theta 1, connection probability 0.01, the critical point at g 1, and Gaussian or Cauchy\n    weights of strength g, but the network size N, the scaling of the distributions with g (the\n    formulas are lost from the text), the run length, the initial state and inputs, and how\n    model activity is binned for PCA are not given. Cannot be specified from the text read;\n    recorded so the finding is covered.\n- id: fig4d-gaussian-model-no-power-law\n  statement: Networks with Gaussian connections, which lack neuronal avalanches, show no power\n    law in PCA at any connection strength.\n  source: Figure 4C and 4D; Results, Heavy-tailed connectivity is important for the\n    co-occurrence, paragraph 4\n  quote: In contrast, Gaussian networks, which fails to reproduce neuronal avalanches, were also\n    unable to reproduce a power law in PCA at any connection strength\n  criterion: A simulation, not a test on the recorded data; unspecified as for\n    fig4d-cauchy-model-power-law. Recorded so the finding is covered.\n"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -i 's/under\n    the fit, size and Moran-independent readings/X/' claims/002020/*.yaml; python - <<'E'
p='claims/002020/10.1101-2025.01.14.630383.yaml'
s=open(p).read()
s=s.replace("under\n    the fit, size and Moran-independent readings F1, F2, A1, A2.","under\n    the fit and size readings F1, F2, A1, A2.")
open(p,'w').write(s)
E
grep -n "Moran-independent\|—\|rather" claims/002020/*.yaml; python tools/claims_check.py claims/002020/10.1101-2025.01.14.630383.yaml paper/10.1101-2025.01.14.630383.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
grep -v '^#' claims/002020/*.yaml | grep -nE '^\s+[^#]*\S: ' | grep -vE '^\s*[0-9]+:\s*-? ?[a-z_]+: ' | head
```

```
(Bash completed with no output)
```

**Agent**

I've written the claims file, `claims/002020/10.1101-2025.01.14.630383.yaml`. The quote checker reports 20 claims, 20 quotes and 0 problems.

**Text read.** The bioRxiv preprint, version 1, flattened from its JATS XML. It has the main text, figure legends, Discussion and Methods. There is no PDF and no supplement. The dandiset's metadata points at version 2 of the preprint, which I did not read. The paper links no code and has no code or data availability statement, so I read no repository.

**Claims.** 20, all with quotes and none inferred.
- **Statistics:** none. The paper reports no tests, p-values or intervals for any finding.
- **Expected values:** 8 claims have them: 7 dishes; activity onset at 2 to 3 DIV; the example dish's shift at about 10 DIV with exponent 1.30; transition at about 15 DIV; exponent about 1.2; avalanche shift at about 15 DIV with exponent about 1.5; the paper's group threshold b = 0.1; the model's exponent 1.56.
- **Criteria:** all 20 claims have one.
- **Model claims:** 2 are simulation claims, recorded so the findings are covered. They cannot be specified from the text: the network size, how the weight distributions scale with g, the run length, the initial state and how model activity is binned for PCA are all missing.

**Details the paper leaves open, with the readings named**
- **The 0.03 Hz rule:** applied per electrode, or per recording.
- **The fitted function:** its formula is lost from the text. I read it as a·x^(−c)·exp(−b·x). The squared error is taken either on log values or on raw values. The ranks fitted for the variance spectrum aren't stated, so the reading is all ranks with a positive eigenvalue.
- **Local Moran's I:** its formula is also lost. Readings are Anselin's normalised form, or the form without the variance normalisation. Whether an electrode counts as its own neighbour is open; the usual reading (it does not) is the default, the other a variant.
- **Locality slope:** "semi-logarithmic" could mean locality against log PC index, or log locality against PC index.
- **Avalanches:** spikes from all electrodes pooled into one train for the mean inter-spike interval. Cascade size is either the number of spikes or the number of distinct electrodes.
- **When the transition happens:** the DIV at which b stays below 0.1, taken either on the 3-day moving average pooled over dishes or per dish then the median.
- **Figure 1E:** which dish is the example, and which spectra the exponent-1.30 line fits (three readings).
- **No measure given:** the shift from asynchronous firing to bursting (two synchrony measures named) and the absent temporal structure of PCs (two timescale measures named).
- **No test given:** for "did not alter", "significantly disrupted", "clear positive correlation", "became steeper" and "nearly independent", the criteria use Spearman/Pearson, Wilcoxon or Mann-Whitney tests at p < 0.05, or 10% bands. These are readings I chose because the paper gives no test, and each criterion says so.
- **Avalanche threshold:** the 0.1 boundary on b is carried over from the PCA groups, because the paper gives none for avalanches.

**Missing from the paper**
- **Supplementary Figures S1 and S2:** their legends are not in the text. So for classifying recordings by avalanches (S1) the threshold is unknown, and for shuffling breaking the co-occurrence (S2) the shuffle and the measure are unknown. Both claims rest only on the Results sentence that cites the figure, and stay open until the supplement is supplied.
- **The Methods equations:** these are garbled in the flattened text, as listed above.
- **The model's parameters:** too incomplete to simulate, as noted under the claims.

## End of run

13 turns, 3 minutes, result: success.
