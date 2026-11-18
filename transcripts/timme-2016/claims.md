# crcns-ssc-3 · claims · run 42203731016

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  grep -n "^#" docs/protocol.md | head -50; ls claims/001453 claims/crcns-ssc-3 paper/ 2>&1; ls claims | head
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  sed -n 1,185p docs/protocol.md; cat claims/001453/*.yaml
```

```
# Protocol for an attempt

Version: `pilot-13`. Record this version in the attempt's provenance.

This is what agents, or people, do to attempt a target and deposit the
result. A target is a dataset in a public archive and a paper it names. How
each archive's datasets are named, versioned and read is in
[archives.md](archives.md); the examples here are from DANDI, the first. It is written from the pilot attempts
([pilot notes](pilot-notes.md)); the reasons for the rules are there.

An attempt has three roles, each a separate run with a separate context:

- The **reader** reads the paper and writes the claims file: every finding,
  and how each is to be tested, taken from the paper. A second reader checks
  it against the paper. Readers never see the dataset's data.
- The **author** tests the claims on the dataset. It reads the paper to
  understand the claims, but the claims file binds it: it cannot change a
  claim's statement, expected values or criterion. A method detail the file
  lacks it takes from the paper, citing the passage, and it asks a reader
  only when it believes the file misreads the paper.
[... 486 more lines not kept]
```

**Agent calls Bash**

```bash
cd  wc -l paper/*.txt; head -c 3000 paper/ssc-3.data-description.txt; echo; ls claims | grep crcns | head; sed -n 1,140p tools/claims_check.py | head -60
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1371-journal.pcbi.1004858.txt"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  sed -n 60,152p paper/ssc-3.data-description.txt; ls claims/crcns-hc-24; head -40 claims/crcns-hc-24/*.yaml
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1371-journal.pcbi.1004858.txt",
 "offset": 542
}
```

Result: not kept, because it reads the paper's text.

**Agent**

The full text is here (version of record, PMC4861348, Methods and the S1 Fig legend). It has no displayed equations, and there is no PDF. Next I'll check the schema, then write the claims.

**Agent calls Bash**

```bash
cd  cat schemas/claims.schema.json | head -200; grep -rl "simulation\|model only\|data: elsewhere" claims | head
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
[... 190 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 200,320p schemas/claims.schema.json; grep -n -B2 -A12 "simulat\|model" claims/000011/10.1038-nature17643.yaml | head -60; grep -h "archive:" claims/crcns-*/*.yaml | sort | uniq -c; grep -h -A3 "^dataset:" claims/crcns-hc-24/*.yaml
```

```
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
          "date": {
            "type": "string",
            "format": "date"
          },
          "kind": {
            "enum": [
[... 166 more lines not kept]
```

**Agent**

The text is complete except for its displayed equations (Eqs 1 to 24 are images and were lost in the XML), and the paper links no code. Writing the claims file now.

**Agent calls Write**

```json
{
 "file_path": "claims/crcns-ssc-3/10.1371-journal.pcbi.1004858.yaml",
 "content": "# Claims for Timme, Ito, Myroshnychenko, Nigam, Shimono, Yeh, Hottowy, Litke & Beggs (2016),\n# \"High-Degree Neurons Feed Cortical Computations\", PLoS Comput Biol 12(5), e1004858, on CRCNS ssc-3.\n# Written by an agent (model \"claude-opus-5-5\", Claude Code, runner \"GitHub Actions\"), 2026-11-06,\n# protocol as stated in docs/protocol.md (version pilot-13), Reader steps 1 to 4.\n#\n# Text read: the version of record, PMC4861348 (Europe PMC full-text XML, flattened), with its\n# Materials and Methods, Results, Discussion, the legends of Figures 1 to 7, Table 1 and the legend\n# of S1 Fig (the only supplement; it is a figure, so only its legend is text). No PDF was supplied,\n# so no figure could be read. The flattened text has lost every displayed equation (Eqs 1 to 24).\n# The information measures (Eqs 1 to 12) are described in words well enough to be rebuilt, and\n# each criterion says how it reads them. The feedforward model is not: the binary-signal currents\n# (Eqs 16 to 19), the form of the rewiring score (Eq 20) and the fitted score equations (Eqs 22 to\n# 24) are given only as equations. The model claims below need these equations read from the\n# version of record before they can be tested. Values shown only in figures (the binomial skew\n# probabilities of Fig 5A and 5B, the fitted exponents and their 95% ranges in Fig 6, the means in\n# Fig 7C and 7D) could not be read and are not claimed as numbers.\n#\n# Code read: none. The paper links no analysis or model code. Its Data Availability names the\n# deposit \"http://dx.doi.org/10.6080/K07D2S2F\" at CRCNS, which is ssc-3. The data descriptor\n# (ssc-3 data description, version 0.8) was read only to know what the dataset holds; no claim\n# comes from it.\n#\n# The data the paper used, as it reports them (Materials and Methods, Experimental System).\n# Cortico-hippocampal organotypic slice cultures from postnatal day 6 C57BL/6 mouse pups, recorded\n# after 2 to 4 weeks in vitro, spontaneous activity, no stimulation. A 512-electrode array (5 um\n# flat electrodes, 60 um spacing, about 0.9 by 1.9 mm). Only cortical recordings were used: 25\n# recordings of somatosensory cortex, about 60 min each. Spikes sorted by PCA over seven adjacent\n# electrodes; duplicates and neurons with many refractory violations removed; neurons with fewer\n# than 100 spikes in the 60 min removed. 7735 neurons in total, 309.4 per recording on average,\n# mean rate 2.10 Hz, spike times at 50 us resolution. The measured variable is spike times only.\n# The descriptor lists 25 recordings with spike times in ms (20 kHz), neuron positions and a\n# recording ID; it matches the paper's description.\n#\n# Methods the analysis rests on, with what is open. Criteria below refer to these by label.\n# M-TE. Transfer entropy from J to I, TE = MI(I_F; J_P | I_P), with spike trains binarized (each\n#   bin spiking or not) and probabilities counted over the whole recording (Methods, Effective\n#   Connectivity Detection, paragraphs 2 and 3). Normalized TE is TE divided by the entropy of the\n#   receiver's future state, H(I_F) (same section, paragraph 3, and Multivariate Transfer Entropy\n#   and Computation, paragraph 4). The paper used the TE networks of its reference [44] (Timme et\n#   al. 2014, PLoS One 9, e115764) at two time scales, \"1.6 to 6.4 ms and 3.5 to 14 ms\" (paragraph\n#   4), and says the complete TE procedure is in [44]. Open in this paper, with readings: the bin\n#   and delays of each time scale, (a) bins of 1.6 ms and 3.5 ms with delays of 1 to 4 bins, the\n#   reading the stated ranges imply, or (b) the bin sizes and delays [44] gives; how TE over the\n#   delays of one time scale is combined, (c) the maximum over delays, (d) the sum over delays, or\n#   the rule [44] gives. Past states are one bin, as the four-variable PID (past of three neurons,\n#   future of one) implies.\n# M-SIG. A connection is significant when fewer than 5 of 5000 jittered surrogates give a TE larger\n#   than the real one (p < 0.001) (Effective Connectivity Detection, paragraph 5). Open, the jitter\n#   width; readings, the width [44] gives, or, failing that, two widths an order of magnitude apart\n#   around the time scale's longest delay, both reported.\n# M-SUB. For each recording, 500 sub-networks of 50 neurons with average total degree 3 (so 75\n#   connections) drawn from the full network (same paragraph, citing [44, 83]). Open, how they are\n#   drawn; readings, (a) 50 neurons at random, then the 75 strongest significant connections among\n#   them, (b) 50 neurons at random, then 75 of their significant connections at random; draws with\n#   fewer than 75 significant connections among the 50 neurons are redrawn. Also open, whether the\n#   degree and synergy analyses use these sub-networks or the full networks; readings, (s) the\n#   sub-networks, degrees counted within each and the 500 pooled per recording, which the paper's\n#   stated purpose (to reduce bias from degree and network size) supports, (f) the full network of\n#   significant connections.\n# M-PID. For every triple in which two neurons J and K both send significant connections to I, the\n#   synergy of the multivariate TE {J,K} to I, by the Williams and Beer decomposition: redundancy is\n#   I_min of J_P and K_P about I_F, conditioned on I_P, the unique terms are each bivariate TE minus\n#   the redundancy, and synergy is TE({J,K} to I) minus the redundancy and both unique terms (Eqs 5\n#   to 10, described in Multivariate Transfer Entropy and Computation, paragraphs 3 to 4), with the\n#   same bins and delays as the TE, normalized by H(I_F). The conditioning of I_min on I_P is stated\n#   in words; the form taken is the specific information of each source about each state of I_F\n#   within each state of I_P, the minimum over sources, weighted by p(i_F, i_P).\n# M-CORR. Per recording and time scale, the correlation between the synergy of each triple and\n#   either the receiver's in-degree, or the out-degree of one transmitter, each of the two\n#   transmitters of a triple being a separate data point (Results, Degree and Computation,\n#   paragraph 1). Open, the correlation coefficient; readings, (p) Pearson, (r) Spearman. The\n#   Fig 5 legend gives N data = 40 correlations per panel; with 25 recordings and two time scales\n#   the paper does not say which 40. The count is reported, not tested.\nschema_version: 2\ndataset:\n  archive: crcns\n  id: ssc-3\n  doi: 10.6080/K07D2S2F\npaper: doi:10.1371/journal.pcbi.1004858\nclaims:\n- id: data-recordings\n  statement: The analysis used 25 recordings of somatosensory cortex cultures, with 7735 neurons in\n    total after removing neurons with fewer than 100 spikes in the 60 min recording, an average of\n    309.4 neurons per recording and an average firing rate of 2.10 Hz.\n  source: Materials and Methods, Experimental System, paragraph 1\n  quote: only recordings from cortex were used in this analysis (number of recordings - 25 ... neurons\n    with less than 100 spikes in the 60 minute recording (firing rate < 0.028 Hz) were removed from\n    the analysis. Spike sorting yielded spike times for each neuron (7735 total neurons) with a\n    resolution of 50 μs. The average firing rate for each neuron was 2.10 Hz and each recording had\n    an average of 309.4 neurons\n  expected:\n  - quantity: number of recordings\n    value: 25\n    tolerance: 2.5\n  - quantity: neurons in total\n    value: 7735\n    tolerance: 773.5\n  - quantity: neurons per recording, mean\n    value: 309.4\n    tolerance: 30.9\n  - quantity: firing rate per neuron, mean over neurons\n    value: 2.10\n    tolerance: 0.21\n    unit: Hz\n  criterion: Counted from the dataset's spike times. The paper says the 100-spike threshold was\n    applied; whether the deposited neurons already passed it is for the author to find, and the\n    counts are reported both as deposited and after applying it. Open, how the rate is taken;\n    readings (a) spikes over the recording length of each recording, (b) spikes over 60 min.\n    Reproduced when all four values are within tolerance under one reading.\n- id: fig4ac-te-lognormal\n  statement: The significant TE connection weights, raw and normalized, are roughly log-normally\n    distributed at both time scales and vary over several orders of magnitude.\n  source: Results, Connection Weight and Degree Distributions, paragraphs 2 and 3; Figure 4A and 4C\n  quote: Similar to these studies, we found a roughly log-normal distribution of significant TE\n    weights ... both TE and normalized TE values varied broadly over several orders of magnitude\n  criterion: TE and significance as in M-TE and M-SIG, on the full network of significant\n    connections of each recording. Per time scale, raw and normalized TE binned into 100\n    logarithmically spaced bins (Results, paragraph 3) and fit with a log-normal probability mass\n    function with an extra normalization factor (Eq 21, not in the text read; the reading is a\n    Gaussian in log TE times a factor alpha), by nonlinear least squares, per recording and on the\n    average over recordings. The paper gives no goodness-of-fit threshold. Reading fixed here,\n    reproduced when, for both time scales and both raw and normalized TE, the fit on the average\n    distribution has R2 of at least 0.9 and the 1st and 99th percentiles of the significant TE\n    values differ by at least a factor of 100 (two orders of magnitude); R2 and the spread are\n    reported for every recording.\n  depends_on:\n  - data-recordings\n- id: fig4bd-heavy-tailed-degree\n  statement: The total degree distributions are heavy-tailed, with many more high-degree neurons\n    than in random networks with the same numbers of neurons and connections.\n  source: Results, Connection Weight and Degree Distributions, paragraph 4; Figure 4B and 4D\n  quote: the degree distributions indicate that the real data contained many more high-degree neurons\n    than would be expected in a random network\n  criterion: Networks as in M-TE, M-SIG and M-SUB. Random networks made by placing binary\n    connections with uniform probability among the same number of neurons with the same number of\n    connections (paragraph 4), with the same sampling as the real data (Fig 4 legend), so under\n    reading (s) one random network per sub-network. Distributions of total degree averaged over\n    recordings, per time scale. The paper gives no measure of the tail. Reading fixed here,\n    reproduced when, at both time scales, the fraction of neurons whose total degree exceeds the\n    99.9th percentile of the random networks' total degree is at least 10 times 0.001 (and the\n    largest real degree exceeds the largest random one). The fraction is reported for every\n    reading of M-TE and M-SUB.\n  depends_on:\n  - data-recordings\n- id: fig4bd-out-tail-longer\n  statement: The in-degree distribution has a shorter tail than the out-degree distribution, so\n    there are more high out-degree neurons than high in-degree neurons.\n  source: Figure 4B and 4D legend\n  quote: note that the in-degree distribution had a shorter tail than the out-degree distribution,\n    indicating that there were more high out-degree neurons than there were high in-degree neurons\n  criterion: Networks as in fig4bd-heavy-tailed-degree. The paper gives no measure of the tail.\n    Reading fixed here, reproduced when, at both time scales, the 99th percentile of out-degree is\n    larger than that of in-degree and the largest out-degree is larger than the largest in-degree,\n    pooled over recordings; a one-sided Wilcoxon signed-rank test over recordings of the 99th\n    percentiles is reported as well.\n  depends_on:\n  - fig4bd-heavy-tailed-degree\n- id: fig5a-in-degree-uncorrelated\n  statement: The correlation between a receiver's in-degree and the synergy (computation) it\n    performs is centered near zero across recordings, with a slight negative skew; computation is\n    independent of in-degree.\n  source: Results, Degree and Computation, paragraph 1; Figure 5A\n  quote: though significant positive and negative correlations between receiver in-degree and\n    computation were found, the distribution of these correlation values for each recording was\n    centered near zero with a slight negative skew\n  criterion: Synergy as in M-PID on the networks of M-TE, M-SIG and M-SUB; correlations as in\n    M-CORR, one per recording and time scale. A claim of absence, judged on the paper's test, the\n    count of positive against negative correlations under a binomial with p = 0.5, as the\n    probability of a skew of that size or larger (Fig 5A legend). The paper names no alpha; 0.05\n    is the reading. Reproduced when that test is not significant; partially reproduced when the\n    skew is significantly negative (the paper's slight negative skew, but not independence); not\n    reproduced when it is significantly positive. The median correlation and the counts are\n    reported under every reading.\n  depends_on:\n  - data-recordings\n- id: fig5b-out-degree-positive\n  statement: Most recordings show a positive correlation between a transmitter's out-degree and the\n    synergy computed by its receivers.\n  source: Results, Degree and Computation, paragraph 1; Figure 5B\n  quote: the majority of recordings exhibited positive correlations between transmitter out-degree\n    and computation\n  criterion: As fig5a-in-degree-uncorrelated, with the transmitter's out-degree. Reproduced when\n    more than half of the correlations are positive and the binomial probability of that many\n    positives or more under p = 0.5 is below 0.05 (alpha a reading; the paper names none), at\n    each time scale separately and over both pooled. Partially reproduced when a majority is\n    positive but not significant.\n  depends_on:\n  - data-recordings\n- id: fig5ab-correlations-beyond-null\n  statement: Nearly all the per-recording degree and synergy correlations lie beyond a null of\n    randomized degree and computation pairings, whose correlations sit near zero.\n  source: Figure 5A and 5B legend\n  quote: Nearly all correlations were likely to be significant given the proximity of the null model\n    correlations (no correlation) to zero (null model consisted of randomized degree/computation\n    pairings) (N null = 400)\n  criterion: For each correlation of fig5a-in-degree-uncorrelated and fig5b-out-degree-positive,\n    null correlations from random permutations of degree against synergy within the same\n    recording and time scale. N null = 400 against N data = 40 gives 10 permutations per\n    correlation, the reading taken. The paper gives no rule for significance. Reading fixed here,\n    a correlation is beyond the null when its absolute value exceeds the 99th percentile of the\n    absolute null correlations pooled over all 400; reproduced when at least 90% of correlations\n    in each panel are beyond the null.\n  depends_on:\n  - fig5a-in-degree-uncorrelated\n  - fig5b-out-degree-positive\n- id: fig5cd-pooled-trends\n  statement: Pooled over all neuron groups and recordings, synergy shows no trend with receiver\n    in-degree and rises with transmitter out-degree, at both time scales.\n  source: Results, Degree and Computation, paragraph 1; Figure 5C and 5D\n  quote: These trends were also observed in distributions of all neuron groups combined across all\n    recordings for the two time scales of interest\n  criterion: Synergy values of all triples pooled over recordings, grouped by degree, with only\n    degrees having 20 or more neuron groups kept (Fig 5 legend), the median per degree. The\n    paper gives no test. Reading fixed here, Spearman correlation of the per-degree medians with\n    degree; reproduced when, at both time scales, it is positive with p < 0.05 for out-degree and\n    is not significantly positive for in-degree.\n  depends_on:\n  - fig5a-in-degree-uncorrelated\n  - fig5b-out-degree-positive\n- id: fig6-information-gain-not-rising\n  statement: The information gained by adding inputs to a neuron, a bound on its highest-order\n    synergy, stays constant or decreases with the number of inputs at both time scales; exponential\n    fits to the medians give small negative exponents, one with a 95% range overlapping zero.\n  source: Results, Degree and Computation, paragraph 2; Figure 6\n  quote: we found that the information gain remained constant or decreased with added number of\n    inputs ... Both fits produced small negative exponent values, one of which had an error\n    overlapping zero\n  criterion: Information gain (Eq 12, not in the text read) read from Methods, Multivariate Transfer\n    Entropy and Computation, last two paragraphs, as the TE from all n inputs jointly to I minus\n    the TE from n - 1 of them, averaged over the n choices of the input left out, normalized by\n    H(I_F) as the other terms are. For each receiver and n, all combinations of n of its inputs or\n    100 sampled combinations, whichever is smaller, averaged per neuron; n up to 6. Open, the\n    first n; readings (a) n from 2 to 6, (b) n from 1 to 6. Network readings as in M-TE, M-SIG and\n    M-SUB. Medians over neurons, pooled over recordings, fit with A exp(k n) by nonlinear least\n    squares with a 95% confidence interval for k (Fig 6 legend). Reproduced when, at both time\n    scales, the interval for k does not lie wholly above zero and k is negative at at least one;\n    not reproduced when either time scale has an interval wholly above zero.\n  depends_on:\n  - data-recordings\n- id: table1-pid-examples\n  statement: On the example distributions of Table 1, the PID multivariate TE finds synergy only in\n    the synergistic and the synergistic and redundant examples; mutual information misses the\n    hidden self interaction, and interaction information misses simultaneous synergy and\n    redundancy and unique information.\n  source: Materials and Methods, Multivariate Transfer Entropy and Computation, paragraphs 5 and 6;\n    Figure 2 and Table 1\n  quote: Synergy is only found in the Synergistic Interaction example and the Synergistic and\n    Redundant Interaction example\n  criterion: A computation on the joint distributions printed in Table 1, using no recorded data.\n    PID terms as in M-PID, MI as Eq 1 and interaction information II(J_P; K_P; I_F) as the\n    standard difference of conditional and unconditional mutual informations (Eq 11, not in the\n    text read). Reproduced when synergy is above 1e-6 bits in exactly those two examples, MI(J_P;\n    I_F) is zero for the hidden self interaction, and II is zero for the synergistic and redundant\n    and for the single and redundant examples while their synergy, respectively unique\n    information, is not.\n- id: fig7c-degree-modified-rule-matches\n  statement: In a two-layer feedforward model, degree-modified and firing-rate-modified Hebbian\n    rewiring rules qualitatively reproduce the degree and synergy correlations of the real data,\n    the degree-modified rule more closely, while a pure Hebbian rule and random wiring do not.\n  source: Results, Feedforward Network Model, paragraph 3; Figure 7C\n  quote: Both the degree-modified and firing rate modified Hebbian rules qualitatively matched the\n    degree vs. computation correlation results seen in the real data ... The degree-modified rule\n    was closer than the firing rate modified rule ... the purely Hebbian rule and the random network\n    produced correlation results that were qualitatively very different from the real data\n  criterion: A simulation with the parameters of Materials and Methods, Feedforward Network Model\n    (20 binary neurons per layer; firing probability a sigmoid of input current with alpha about\n    0.023 and beta about 4.6, read as p = 1 / (1 + exp(beta - alpha I)), which gives rare firing\n    at I = 0 and p = 0.5 at I = I_con N_Neurons = 200; I_con = 10; 80 connections; rewiring by\n    500 runs of statistics then one swap, repeated 80 times; 100 models per type). The currents\n    from the binary signal (Eqs 16 to 19), the form of the score (Eq 20) and the fitted scores\n    (Eqs 22 and 23) are not in the text read and must be taken from the version of record's\n    equations before analysis. Degree and synergy correlations of the models computed as in\n    M-PID and M-CORR on the model's states. Fig 7C shows means and standard deviations; reading\n    fixed here, a model type matches when its mean in-degree and mean out-degree correlations\n    both lie within the real data's mean plus or minus one standard deviation. Reproduced when the\n    degree-modified and firing-rate-modified types match, the degree-modified mean is nearer the\n    real means (Euclidean distance over the two correlations), and the Hebbian and random types\n    do not match.\n  depends_on:\n  - fig5a-in-degree-uncorrelated\n  - fig5b-out-degree-positive\n- id: fig7b-connectivity-patterns\n  statement: The pure Hebbian rule pools connections among the input neurons most correlated with\n    the network-wide signal, the firing-rate-modified rule spreads them to less correlated input\n    neurons, and the degree-modified rule spreads them almost uniformly across the input layer.\n  source: Results, Feedforward Network Model, paragraph 2; Figure 7B\n  quote: As expected, the purely Hebbian rule pooled connections between the most strongly correlated\n    neurons ... The firing rate modified rule spread connections more broadly to input layer neurons\n    less well correlated with the binary network-wide signal. Finally, the degree-modified rule ...\n    spread connectivity almost uniformly across the input layer\n  criterion: The models of fig7c-degree-modified-rule-matches, connection probabilities averaged\n    over 100 models. The paper gives no measure. Reading fixed here, the fraction of connections\n    leaving the upper half of input-layer indices (the neurons more correlated with the binary\n    signal); reproduced when it is ordered Hebbian above firing-rate-modified above\n    degree-modified, and the degree-modified fraction is within 0.5 plus or minus 0.1.\n  depends_on:\n  - fig7c-degree-modified-rule-matches\n- id: fig7d-degree-rule-highest-conditioned-mi\n  statement: The pure Hebbian rule gives the highest mutual information between connected neurons,\n    but conditioned on the network-wide binary signal the degree-modified rule gives the highest;\n    it alone raises neuron-to-neuron communication while also reinforcing network-wide\n    correlation.\n  source: Results, Feedforward Network Model, paragraph 4; Figure 7D and 7E\n  quote: Unsurprisingly, we found the largest mutual information in the purely Hebbian rule ...\n    when we conditioned the mutual information on the binary network-wide correlation signal, we\n    found that the degree-modified Hebbian rule produced the highest mutual information\n  statistics:\n  - test: Mann-Whitney rank-sum test\n    p: 0.001\n    p_relation: \"<\"\n    corrected: False Discovery Rate\n    n: 100 models per rule\n  criterion: The models of fig7c-degree-modified-rule-matches. Per model, the mean over connections\n    of MI between the input and output neuron's states (Eq 1) and of MI conditioned on b(t). Open,\n    the number of runs MI is estimated from; reading, a fresh set of runs at least as large as\n    the 500 used for rewiring, with the count reported. Pairs of rules compared by two-sided\n    Mann-Whitney tests across the 100 models with Benjamini-Hochberg FDR control (Fig 7D legend).\n    Reproduced when the Hebbian rule has the highest unconditioned MI and the degree-modified rule\n    the highest conditioned MI, each significant against every other rule at corrected p < 0.001,\n    and the degree-modified rule's conditioned MI is above the random model's while the Hebbian\n    and firing-rate-modified rules are not significantly above it.\n  depends_on:\n  - fig7c-degree-modified-rule-matches\n- id: figs1-larger-model\n  statement: With 40 neurons per layer the model gives the same qualitative results, the\n    degree-modified rule again raising neuron-to-neuron communication, though the Hebbian and\n    firing-rate-modified rules give larger conditioned mutual information than in the small model.\n  source: Results, Feedforward Network Model, paragraph 6; S1 Fig\n  quote: As with the smaller model, the larger model produced computation correlation results\n    similar to the results seem in the data for the degree-modified and firing-rate modified Hebbian\n    rewiring rules, but not the pure Hebbian rewiring rule ... As in the smaller model, the\n    degree-modified Hebbian rewiring rule reinforced network-wide activity and increased\n    neuron-to-neuron communication\n  criterion: As fig7c-degree-modified-rule-matches, fig7b-connectivity-patterns and\n    fig7d-degree-rule-highest-conditioned-mi with N_Neurons = 40 (so 320 connections and 320\n    rewirings) and the larger model's score equations (Eq 23 and Eq 24, not in the text read).\n    Reproduced when the correlation match of fig7c holds for the degree-modified and\n    firing-rate-modified rules and not for the Hebbian rule, and the degree-modified rule's\n    conditioned MI is above the random model's (Mann-Whitney, FDR, p < 0.001).\n  depends_on:\n  - fig7c-degree-modified-rule-matches\n"
}
```

```
File created successfully at: claims/crcns-ssc-3/10.1371-journal.pcbi.1004858.yaml (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/crcns-ssc-3/10.1371-journal.pcbi.1004858.yaml",
 "old_string": "  quote: only recordings from cortex were used in this analysis (number of recordings - 25 ... neurons\n    with less than 100 spikes in the 60 minute recording (firing rate < 0.028 Hz) were removed from\n    the analysis. Spike sorting yielded spike times for each neuron (7735 total neurons) with a\n    resolution of 50 μs. The average firing rate for each neuron was 2.10 Hz and each recording had\n    an average of 309.4 neurons",
 "new_string": "  quote: \"only recordings from cortex were used in this analysis (number of recordings: 25 ... neurons\n    with less than 100 spikes in the 60 minute recording (firing rate < 0.028 Hz) were removed from\n    the analysis. Spike sorting yielded spike times for each neuron (7735 total neurons) with a\n    resolution of 50 μs. The average firing rate for each neuron was 2.10 Hz and each recording had\n    an average of 309.4 neurons\""
}
```

```
The file claims/crcns-ssc-3/10.1371-journal.pcbi.1004858.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd  python tools/claims_check.py claims/crcns-ssc-3/10.1371-journal.pcbi.1004858.yaml paper/10.1371-journal.pcbi.1004858.txt; echo exit $?; grep -nP '(?<!")\b\w+: [^"]' claims/crcns-ssc-3/*.yaml | grep -v '^\S*:[0-9]*:\s*-\? \?[a-z_]*: ' | head
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  grep -n -i "rather\|—" claims/crcns-ssc-3/*.yaml; git status --short
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
?? claims/crcns-ssc-3/
?? scripts
```

**Agent**

I wrote the claims file at `claims/crcns-ssc-3/10.1371-journal.pcbi.1004858.yaml`. The quote checker passes it: 14 claims, 14 quotes, 1 statistical value, 0 problems.

**Text read.** The version of record (PMC4861348, from Europe PMC's full-text XML). That includes the Methods, Results, Discussion, the figure legends, Table 1 and the legend of S1 Fig, which is the only supplement and is a figure. No PDF was supplied. The paper links no code. The data descriptor was read only to see what the dataset holds.

**Claims.**
- All 14 have quotes; none rests on an inferred note.
- Only one has statistics: Fig 7D, Mann-Whitney with FDR correction, p < 0.001. The Fig 5 binomial probabilities and the Fig 6 fit intervals appear only in the figures.
- One claim has expected values: the dataset counts (25 recordings, 7735 neurons, 309.4 per recording, 2.10 Hz), all at 10% tolerance.
- All 14 have criteria. They cover the TE weight distribution (4A/C), heavy-tailed degree (4B/D), out-degree tail longer than in-degree, in-degree uncorrelated with synergy (5A, a claim of absence judged on the paper's binomial skew test), out-degree positively correlated (5B), correlations beyond the null, pooled trends (5C/D), information gain (Fig 6), the Table 1 PID examples, and four model claims (7B, 7C, 7D/E, S1).

**Details the paper leaves open, and the readings named:**
- **TE time scales.** Either bins of 1.6 and 3.5 ms with delays of 1 to 4 bins, or whatever reference [44] (Timme et al. 2014) gives. Combining across delays: maximum or sum.
- **Jitter width for the surrogates.** The width [44] gives, or two widths an order of magnitude apart.
- **Building the sub-networks.** 50 random neurons plus either their 75 strongest connections or 75 random ones. A second choice is whether the analysis runs on the sub-networks or on the full networks.
- **Correlation type.** Pearson or Spearman.
- **Information gain.** n runs from 2 to 6, or from 1 to 6.
- **Firing rate.** Spikes over each recording's length, or over 60 min.
- **Model MI.** How many runs the mutual information is estimated from.
- **"N data = 40".** The paper has 25 recordings and two time scales, which makes 50; it does not say which 40. The count is reported, not tested.
- **No thresholds given.** The paper sets none for "roughly log-normal", "heavy-tailed", "nearly all significant", "qualitatively matched" or "almost uniformly". Each criterion fixes a threshold of its own and says so.

**Missing from the text.**
- The flattened text has lost every displayed equation (Eqs 1 to 24). The information measures can be rebuilt from the prose, and each criterion says how it reads them.
- The feedforward model cannot be rebuilt. The binary-signal currents (Eqs 16 to 19), the form of the rewiring score (Eq 20) and the fitted score equations (Eqs 22 to 24) are given only as equations. So the four model claims need those equations from the version of record, or its PDF, before anyone can test them.
- Values shown only in figures could not be read, so they are not claimed: the binomial skew probabilities in Fig 5, the exponents and their 95% ranges in Fig 6, and the means in Fig 7.

## End of run

13 turns, 4 minutes, $1.21 at API prices, result: success.
