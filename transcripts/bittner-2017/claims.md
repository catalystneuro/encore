# bittner-2017 · claims · run 42927045957

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cat docs/protocol.md | sed -n '/## Reader/,/^## [A-Z]/p'; ls paper/; head -50 claims/fouke-2025.yaml; wc -l claims/fouke-2025.yaml
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -n 50,321p claims/fouke-2025.yaml; cat paper/pvc-11.data-description.txt; wc -c paper/*.txt; ls papers/datasets/ | grep bittner; cat papers/datasets/bittner-2017.yaml
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1371-journal.pone.0181773.txt"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1371-journal.pone.0181773.txt",
 "offset": 178
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd $TMPDIR && git clone -q https://github.com/sbittner12/litwin-kumar_doiron_cluster_2012 && git clone -q https://github.com/adam-neuro/waveformClassification; for d in litwin-kumar_doiron_cluster_2012 waveformClassification; do echo "== $d"; git -C $d log -1 --format='%H %ad'; find $d -type f -not -path '*/.git/*' | head -50; done
```

```
== litwin-kumar_doiron_cluster_2012
438289358d0367047cc578dcd519ad0f7948808e Fri Jul 21 09:58:40 2017 -0400
litwin-kumar_doiron_cluster_2012/runsim.jl
litwin-kumar_doiron_cluster_2012/COPYING
litwin-kumar_doiron_cluster_2012/README.md
litwin-kumar_doiron_cluster_2012/README
litwin-kumar_doiron_cluster_2012/sim.jl
== waveformClassification
062762678299198f61e5d8b2042bdccba695d72f Fri Jul 21 10:02:43 2017 -0400
waveformClassification/data/class_exampleData2.mat
waveformClassification/data/class_exampleData1.mat
waveformClassification/data/model.mat
waveformClassification/src/averageWaveform.m
waveformClassification/src/nevscan.m
waveformClassification/src/classifyNeuronTypes.m
waveformClassification/src/nevWaveforms.m
waveformClassification/src/readWaveforms.m
waveformClassification/src/fitWaveformParameters.m
waveformClassification/src/getSNR.m
waveformClassification/src/justSNR.m
[... 5 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/waveformClassification && cat README.md example.m src/classifyNeuronTypes.m src/fitWaveformParameters.m src/averageWaveform.m src/getSNR.m src/justSNR.m; cd ../litwin-kumar_doiron_cluster_2012 && cat README.md runsim.jl; head -80 sim.jl
```

```
# waveformClassification
MATLAB implementation of a Gaussian mixture model to classify neurons by waveform shape.

Snyder, Adam C., Michael J. Morais, and Matthew A. Smith. "Dynamics of excitatory and inhibitory networks are differentially altered by selective attention." Journal of neurophysiology 116.4 (2016): 1807-1820.
function [] = example(datapath, MoG)
% example(datapath, MoG)
%
% Example of how to classify neurons using mixture of gaussians (MoG)
% model, as described in the following publication:
%
% Snyder AC, Morais MJ, Smith MA (2016). Dynamics of excitatory and
% inhibitory networks are differentially altered by selective attention.
% Journal of Neurophysiology, V(I): pp-pp. doi:11.1152/jn.00343.2016.
%
% http://jn.physiology.org/content/early/2016/07/22/jn.00343.2016.abstract
%
% INPUTS:
%
% datapath - path to .nev files. Set to current working dir when not
%            provided. Each NEV file should contain all the data from a
[... 558 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/litwin-kumar_doiron_cluster_2012 && sed -n 80,400p sim.jl; git log --oneline | head
```

```
weights = zeros(Ncells,Ncells)

	#random connections
	weights[1:Ne,1:Ne] = jeeout*(rand(Ne,Ne) .< peeout)
	weights[1:Ne,(1+Ne):Ncells] = jei*(rand(Ne,Ni) .< pei)
	weights[(1+Ne):Ncells,1:Ne] = jie*(rand(Ni,Ne) .< pie)
	weights[(1+Ne):Ncells,(1+Ne):Ncells] = jii*(rand(Ni,Ni) .< pii)

	#connections within cluster
	for pii = 1:Npop
		ipopstart = 1 + Nepop*(pii-1)
		ipopend = pii*Nepop

		weights[ipopstart:ipopend,ipopstart:ipopend] = jeein*(rand(Nepop,Nepop) .< peein)
	end

	for ci = 1:Ncells
		weights[ci,ci] = 0
	end

[... 79 more lines not kept]
```

**Agent calls Bash**

```bash
grep -rh "^  data:\|^    data:\|kind:" claims/*.yaml | sort | uniq -c; sed -n 1,60p tools/claims_check.py; grep -l "data: elsewhere" claims/*.yaml | head -3
```

```
214   data: dataset
    483   data: elsewhere
    306   data: with_inputs
    344   data: with_labels
    220   kind: agent
     63   kind: link
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

[... 50 more lines not kept]
```

**Agent calls Bash**

```bash
python -c "import json;s=json.load(open('schemas/claims.schema.json'));print(json.dumps(s,indent=1)[:6000])"; grep -B3 -A12 "data: elsewhere" claims/andrews-2024.yaml | head -40
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
[... 197 more lines not kept]
```

**Agent calls Bash**

```bash
python -c "import json;s=json.load(open('schemas/claims.schema.json'));print(json.dumps(s,indent=1)[6000:])"
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
[... 133 more lines not kept]
```

**Agent**

The paper reports no statistical tests, so no claim gets a `statistics` entry. Both linked repositories are cloned and read. Writing the claims file now.

**Agent calls Write**

```json
{
 "file_path": "claims/bittner-2017.yaml",
 "content": "# Claims for Bittner, Williamson, Snyder, Litwin-Kumar, Doiron, Chase, Smith & Yu (2017),\n# \"Population activity structure of excitatory and inhibitory neurons\", PLoS ONE 12(8),\n# e0181773, tested on CRCNS pvc-11.\n# Written by an agent (model \"claude-opus-5-5\", Claude Code, runner \"GitHub Actions\"),\n# 2026-11-10, protocol as stated in docs/protocol.md.\n#\n# Text read: the version of record, PMC5560553 (open access), from the Europe PMC full-text\n# XML: main text, Materials and methods, figure legends, and the legends of the supplement\n# (S1 to S6 Fig, figures only; the supplement holds no text or tables beyond its legends).\n# No PDF was available, so no figure was read; the claims rest on the text and legends.\n# The Fig 7 legend in the text names panels A to D while the Results cite Fig 7A to 7F; the\n# Results' lettering is used here (A, D for V1; B, E for the clustered network; C, F for the\n# non-clustered network). The Methods (\"Fig 6A\") and the Discussion (\"cf. Fig 6\") cite Fig 6\n# for the V1 analysis; Fig 7 is meant.\n#\n# Code read. (1) github.com/sbittner12/litwin-kumar_doiron_cluster_2012 at commit\n# 438289358d0367047cc578dcd519ad0f7948808e: sim.jl and runsim.jl (Julia), the clustered\n# balanced network of Litwin-Kumar & Doiron (2012): 4,000 E and 1,000 I leaky\n# integrate-and-fire neurons, 50 clusters of 80, dt 0.1 ms, biases uniform in 1.1 to 1.2 (E)\n# and 1 to 1.05 (I), T = 2,000 ms, and a stimulus to neurons 1 to 399 in the last 500 ms.\n# Its weights agree with the Methods except the same-cluster E-E weight (code 1.9 x\n# 10/(15 sqrt(800)) = 0.0448; Methods 0.0456). The code holds no non-clustered network, no\n# spike counting and no factor analysis. (2) github.com/adam-neuro/waveformClassification at\n# commit 062762678299198f61e5d8b2042bdccba695d72f (MATLAB): average waveforms from NEV files,\n# a two-Gaussian fit of each average waveform and of its derivative (first 1 ms), and a\n# two-component Gaussian mixture (10 replicates, random starts) on three fitted parameters\n# (coefVals 5, 6 and 7+10, documented as time of the after-hyperpolarization, its width, and\n# rise plus fall rate), trained on units above the 25th percentile of SNR in each file and\n# with mean waveform correlation to the other units above 0.5; the component with the smaller\n# mean of the first parameter is the narrow (fast) class. Its SNR is the waveform's\n# peak-to-trough amplitude over twice the standard deviation of the residuals. The factor\n# analysis code is not linked.\n#\n# Data the paper used. Models: two balanced networks (clustered and non-clustered), spontaneous\n# activity (zero input), spike counts in one-second windows (\"trials\"), up to 20,000 trials\n# per sampling, with five non-overlapping sets of trials. These simulations are not deposited;\n# the model claims are data elsewhere, to be rerun from the network code. V1: spontaneous\n# activity (gray screen, 20 to 30 min) from Utah arrays in four V1 hemispheres of three\n# anesthetized macaques (sufentanil 6 to 18 ug/kg/hr, vecuronium), sorted off line, kept when\n# the firing rate exceeds 1 spike/s and the SNR exceeds 1.33 (median SNR per array 2.96, 2.75,\n# 2.50 and 2.31), cut into one-second trials (at least 1,200 per array), classified by\n# waveform as broad-spiking (putative E) or narrow-spiking (putative I) at 85% posterior\n# probability, giving 24/39, 41/72, 23/60 and 47/25 broad/narrow neurons per array; 23 of each\n# type, chosen at random, enter the analysis of each array. The recordings are those of Smith &\n# Kohn (2008) and Kelly et al. (2010). CRCNS pvc-11 describes six spontaneous arrays from four\n# monkeys, so the four arrays used are to be identified (claim v1-array-link). The data\n# description lists spike times, channels, the array map and an SNR per unit, and no\n# waveforms; the waveform classification needs average waveforms, which is for the author to\n# check.\n#\n# Method details fixed by the paper, used in every factor analysis (FA) criterion below\n# (Materials and methods, Factor analysis): FA fit by EM; the number of latent dimensions m\n# chosen by maximum cross-validated data likelihood with four folds; FA then refit with that m\n# on all the sampled trials (stated for Fig 4, read as the rule throughout); d_shared is the\n# number of eigenvalues of LL^T needed to explain 95% of shared variance; percent shared\n# variance of neuron k is L_k L_k^T / (L_k L_k^T + Psi_k), averaged over the neurons of a type.\n# Open details, used in every FA criterion: the grid of candidate m (reading used, every m from\n# 0 to n-1, which holds any narrower grid's peak), the EM convergence rule and initialisation\n# (standard choices, cannot change the outcome beyond run-to-run noise), and the assignment of\n# trials to the four folds (contiguous blocks or random; both run).\n#\n# Model simulation details, used in every model claim: the network of sim.jl, without its\n# stimulus (the Discussion says the model activity is spontaneous, zero input), with the\n# Methods' weights (same-cluster J 0.0456; the code's 0.0448 as a variant); the non-clustered\n# network as the Methods give it (p_EE 0.2, J_EE 0.024, the rest unchanged), which the code\n# allows by setting ratiopee and ratioejee to 1. Open: the simulated duration (at least five\n# non-overlapping sets of 20,000 one-second trials for Fig 5C, if its sets do not overlap; one\n# reading uses five sets of 10,000 for Fig 3 and 5B and the same 50,000 trials, overlapping,\n# for 20,000-trial sets), the initial transient discarded (a standard choice of 1 s), the\n# network seed (one network per type, as the paper analysed one representative network).\nschema_version: 2\npaper: doi:10.1371/journal.pone.0181773\nclaims:\n- id: v1-array-link\n  kind: link\n  statement: The four V1 arrays the paper analysed can be identified among the spontaneous\n    recordings of CRCNS pvc-11, from four hemispheres of three monkeys, by their kept neurons'\n    median SNRs of 2.96, 2.75, 2.50 and 2.31.\n  source: Materials and methods, Neural recordings, paragraph 2; Data Availability\n  quote: For our analysis, we only used neurons which had average firing rate greater than one\n    spike per second, and signal-to-noise ratio (SNR), computed as the average waveform amplitude\n    divided by the standard deviation across waveforms, greater than 1.33. Median SNR values were\n    2.96, 2.75, 2.50, and 2.31 for each of the four arrays.\n  expected:\n  - quantity: median SNR of kept neurons, first array\n    value: 2.96\n    tolerance: 0.296\n  - quantity: median SNR of kept neurons, second array\n    value: 2.75\n    tolerance: 0.275\n  - quantity: median SNR of kept neurons, third array\n    value: 2.50\n    tolerance: 0.25\n  - quantity: median SNR of kept neurons, fourth array\n    value: 2.31\n    tolerance: 0.231\n  criterion: For each spontaneous array, keep units with mean firing rate over the whole\n    recording above 1 spike/s and SNR above 1.33, and take the median SNR of those kept. The\n    SNR is open between (a) the dataset's SNR field, which its description defines as the\n    Methods do, and (b) the waveform code's getSNR (amplitude over twice the residual standard\n    deviation), when waveforms are available. Reproduced when four arrays, from four\n    hemispheres of three monkeys, match the four medians within tolerance one to one under\n    one reading, and no other set of four does as well; the matched arrays are the ones the V1\n    claims use. When no set matches, the four arrays from three monkeys whose broad/narrow\n    counts (claim v1-classification-counts) come closest are used, as a recorded assumption.\n- id: fig1ab-inhibitory-higher-rates\n  statement: In both model networks the mean firing rate of inhibitory neurons exceeds that of\n    excitatory neurons (clustered 4.1 against 3.2 Hz, non-clustered 2.9 against 2.0 Hz).\n  source: Results, first section, paragraph 2; Figure 1A and 1B legend\n  quote: The average firing rate of inhibitory neurons was greater than that of excitatory neurons\n    in both model networks\n  data: elsewhere\n  where: GitHub sbittner12/litwin-kumar_doiron_cluster_2012 at commit 438289358d0367047cc578dcd519ad0f7948808e\n    (network code, rerun)\n  expected:\n  - quantity: clustered network, excitatory mean rate\n    value: 3.2\n    tolerance: 0.32\n    unit: Hz\n  - quantity: clustered network, inhibitory mean rate\n    value: 4.1\n    tolerance: 0.41\n    unit: Hz\n  - quantity: non-clustered network, excitatory mean rate\n    value: 2.0\n    tolerance: 0.2\n    unit: Hz\n  - quantity: non-clustered network, inhibitory mean rate\n    value: 2.9\n    tolerance: 0.29\n    unit: Hz\n  criterion: Mean over neurons of each neuron's rate over the simulated spontaneous activity,\n    per type and network (Fig 1A and 1B legend). The tolerance is 10% of each mean, as the\n    paper's plus or minus is the spread over neurons, not an uncertainty of the mean.\n    Reproduced when the inhibitory mean exceeds the excitatory mean in both networks and the\n    four means are within tolerance; partially reproduced when the order holds and some means\n    fall outside.\n- id: fig1cd-spike-count-correlations\n  statement: In the clustered network same-cluster excitatory pairs have strongly positive\n    spike count correlations (0.72 on average) while other pair types are near zero, and in the\n    non-clustered network all pair types are near zero, with a wider spread for\n    inhibitory-inhibitory than excitatory-excitatory pairs.\n  source: Figure 1C and 1D legend; Results, first section, paragraph 2\n  quote: Same-cluster excitatory neurons in the clustered network recurrently excite each other,\n    acting similarly to a bistable unit with high and low activity states ( Fig 1E ) resulting in\n    positive noise correlations which have been observed among nearby neurons [ 40 ]. The\n    non-clustered network does not have this property\n  data: elsewhere\n  where: GitHub sbittner12/litwin-kumar_doiron_cluster_2012 at commit 438289358d0367047cc578dcd519ad0f7948808e\n    (network code, rerun)\n  expected:\n  - quantity: clustered, same-cluster EE correlation, mean\n    value: 0.72\n    tolerance: 0.072\n  - quantity: clustered, same-cluster EE correlation, standard deviation\n    value: 0.27\n    tolerance: 0.027\n  - quantity: clustered, out-of-cluster EE correlation, standard deviation\n    value: 0.11\n    tolerance: 0.011\n  - quantity: clustered, EI correlation, standard deviation\n    value: 0.14\n    tolerance: 0.014\n  - quantity: clustered, II correlation, standard deviation\n    value: 0.15\n    tolerance: 0.015\n  - quantity: non-clustered, EE correlation, standard deviation\n    value: 0.11\n    tolerance: 0.011\n  - quantity: non-clustered, EI correlation, standard deviation\n    value: 0.018\n    tolerance: 0.0018\n  - quantity: non-clustered, II correlation, standard deviation\n    value: 0.025\n    tolerance: 0.0025\n  criterion: Pearson correlation of one-second spike counts for every pair of each type (Fig 1C\n    and 1D legend), mean and standard deviation per type. The paper does not say how many\n    trials or which neurons; all neurons and all simulated trials are used. The means printed\n    near zero (-0.0085, 9.0e-4, 4.5e-4, 1.9e-5, 2.1e-4, -7.3e-4) are judged as near zero,\n    absolute value below 0.01, since 10% of such a value is below what a rerun can resolve;\n    this tolerance is set here. The non-clustered EE spread printed as 0.11 conflicts with\n    the 0.011 that the S2 Fig legend gives for the same distribution; both are named as\n    readings, and the claim holds for that entry under either. Reproduced when all values are\n    within tolerance under a reading and the II spread exceeds the EE spread in the\n    non-clustered network; partially reproduced when the same-cluster mean and the near-zero\n    means hold and some spreads do not.\n- id: fig3ab-dim-scaling-neurons\n  statement: With 10,000 trials, the shared dimensionality of the excitatory population\n    saturates with neuron count in the clustered network but not in the non-clustered network,\n    while that of the inhibitory population keeps increasing in both.\n  source: Results, Excitatory and inhibitory populations of balanced networks have different\n    activity structure, paragraph 3; Figure 3A and 3B, top\n  quote: The shared dimensionality of the excitatory population saturated with increasing neuron\n    count in the clustered network ( Fig 3A , top, red), but not in the non-clustered network ( Fig\n    3B , top, red) [ 39 ]. In contrast, the shared dimensionality of the inhibitory population\n    continued to increase with neuron count regardless of whether the excitatory population was\n    clustered or not\n  data: elsewhere\n  where: GitHub sbittner12/litwin-kumar_doiron_cluster_2012 at commit 438289358d0367047cc578dcd519ad0f7948808e\n    (network code, rerun)\n  criterion: Sampling as in the Methods (Varying neuron and trial count) and the Fig 3 legend,\n    neurons added 10 at a time from 10 to 150, nested within each of five non-overlapping\n    neuron sets, crossed with five non-overlapping sets of 10,000 trials (25 fits per count),\n    plus 750-neuron samplings that join the five sets. Saturation is not defined. Readings,\n    (a) the mean d_shared increases by less than 10% from 100 to 150 neurons, (b) the mean\n    d_shared at 750 neurons is less than twice that at 150 neurons; continuing increase is\n    the negation of each. Reproduced when, under one reading, clustered E saturates and\n    non-clustered E and both I populations do not.\n- id: fig3ab-750-neuron-values\n  statement: For 750-neuron samplings with 10,000 trials, the clustered network's excitatory\n    population has a shared dimensionality of 23.95 and 91.43% shared variance and its\n    inhibitory population 246.7 and 79.56%; the non-clustered network's excitatory population\n    has 139.4 and 20.70% and its inhibitory population 347.2 and 59.74%.\n  source: Figure 3 legend\n  quote: For 750-neuron samplings of the clustered network (10,000 trials), the excitatory\n    population had a shared dimensionality of 23.95 ± 0.05 and percent shared variance of 91.43% ±\n    0.06%, while the inhibitory population had a shared dimensionality of 246.7 ± 2.5 and a\n    percent shared variance of 79.56% ± 0.22%. For 750-neuron samplings of the non-clustered\n    network (10,000 trials), the excitatory population had a shared dimensionality of 139.4 ± 3.8\n    and percent shared variance of 20.70% ± 0.43%, while the inhibitory population had a shared\n    dimensionality of 347.2 ± 4.2 and a percent shared variance of 59.74% ± 0.47%\n  data: elsewhere\n  where: GitHub sbittner12/litwin-kumar_doiron_cluster_2012 at commit 438289358d0367047cc578dcd519ad0f7948808e\n    (network code, rerun)\n  depends_on:\n  - fig3ab-dim-scaling-neurons\n  expected:\n  - quantity: clustered E, d_shared, 750 neurons\n    value: 23.95\n    tolerance: 0.05\n  - quantity: clustered E, percent shared variance, 750 neurons\n    value: 91.43\n    tolerance: 0.06\n    unit: '%'\n  - quantity: clustered I, d_shared, 750 neurons\n    value: 246.7\n    tolerance: 2.5\n  - quantity: clustered I, percent shared variance, 750 neurons\n    value: 79.56\n    tolerance: 0.22\n    unit: '%'\n  - quantity: non-clustered E, d_shared, 750 neurons\n    value: 139.4\n    tolerance: 3.8\n  - quantity: non-clustered E, percent shared variance, 750 neurons\n    value: 20.70\n    tolerance: 0.43\n    unit: '%'\n  - quantity: non-clustered I, d_shared, 750 neurons\n    value: 347.2\n    tolerance: 4.2\n  - quantity: non-clustered I, percent shared variance, 750 neurons\n    value: 59.74\n    tolerance: 0.47\n    unit: '%'\n  criterion: The five 150-neuron sets of each type joined into one 750-neuron sampling, fit on\n    each of the five 10,000-trial sets (Fig 3 legend). The tolerances are the paper's\n    plus-or-minus, read as the standard error over the five trial sets (the legend's error\n    bars are standard errors); they describe one simulated network, so a rerun with another\n    network seed is reported against both these tolerances and 10% of each value. Reproduced\n    when all eight values are within the paper's tolerances; partially reproduced when they\n    are within 10% and the orderings (clustered E below I in d_shared and above in percent\n    shared variance; non-clustered E below I in both) hold.\n- id: fig3ab-psv-type-order\n  statement: The excitatory population has greater percent shared variance than the inhibitory\n    population in the clustered network, and the reverse holds in the non-clustered network.\n  source: Results, Excitatory and inhibitory populations of balanced networks have different\n    activity structure, paragraph 4; Figure 3A and 3B, bottom\n  quote: We found that the excitatory population had greater percent shared variance than the\n    inhibitory population in the clustered network ( Fig 3A , bottom) ... Conversely, in the\n    non-clustered network, the inhibitory population had greater percent shared variance than the\n    excitatory population\n  data: elsewhere\n  where: GitHub sbittner12/litwin-kumar_doiron_cluster_2012 at commit 438289358d0367047cc578dcd519ad0f7948808e\n    (network code, rerun)\n  depends_on:\n  - fig3ab-dim-scaling-neurons\n  criterion: From the samplings of fig3ab-dim-scaling-neurons. Reproduced when the mean percent\n    shared variance of E exceeds that of I at every neuron count from 20 to 150 in the\n    clustered network, and I exceeds E at every such count in the non-clustered network;\n    partially reproduced when the order holds at 100 and 150 neurons only.\n- id: fig3ab-inh-psv-grows\n  statement: The percent shared variance of inhibitory neurons increases with neuron count in\n    both networks, while that of excitatory neurons saturates.\n  source: Results, Excitatory and inhibitory populations of balanced networks have different\n    activity structure, paragraph 4; Figure 3A and 3B, bottom\n  quote: we observed that the percent shared variance of the inhibitory neurons increased with\n    neuron count for both networks ( Fig 3A and 3B , bottom, blue), in contrast to that of\n    excitatory neurons which saturated with increasing neuron count\n  data: elsewhere\n  where: GitHub sbittner12/litwin-kumar_doiron_cluster_2012 at commit 438289358d0367047cc578dcd519ad0f7948808e\n    (network code, rerun)\n  depends_on:\n  - fig3ab-dim-scaling-neurons\n  criterion: From the samplings of fig3ab-dim-scaling-neurons. Readings for saturation as in\n    that claim, applied to percent shared variance, (a) an increase of less than 10% (relative)\n    from 100 to 150 neurons, (b) the 750-neuron value within 10% (relative) of the 150-neuron\n    value. Reproduced when, under one reading, both I populations increase and both E\n    populations saturate.\n- id: fig3cd-trial-saturation\n  statement: With 100 neurons, shared dimensionality and percent shared variance saturate with\n    trial count for both types in both networks; in the clustered network the excitatory\n    population saturates at fewer trials than the inhibitory one, and in the non-clustered\n    network the reverse.\n  source: Results, Excitatory and inhibitory populations of balanced networks have different\n    activity structure, paragraph 5; Figure 3C and 3D\n  quote: In the clustered network, the shared dimensionality and percent shared variance of the\n    excitatory population ( Fig 3C , red) saturated at fewer trials than the inhibitory population\n    ( Fig 3C , blue) ... In the non-clustered network, we saw the opposite trend\n  data: elsewhere\n  where: GitHub sbittner12/litwin-kumar_doiron_cluster_2012 at commit 438289358d0367047cc578dcd519ad0f7948808e\n    (network code, rerun)\n  criterion: 100 neurons per type, trials increased in nested steps within five\n    non-overlapping trial sets, crossed with five non-overlapping neuron sets (Methods, Varying\n    neuron and trial count). The trial grid is not given and no figure was read; the grid\n    used is 100, 200, 500, 1,000, 2,000, 5,000 and 10,000 trials (and 20,000 when the\n    simulation allows), a standard choice. The point of saturation is not defined; readings,\n    the smallest trial count at which the mean reaches (a) 90% or (b) 95% of its value at the\n    largest trial count. Reproduced when, under one reading, for both d_shared and percent\n    shared variance, clustered E saturates at fewer trials than clustered I and non-clustered\n    I at fewer than non-clustered E; partially reproduced when this holds for one of the two\n    measures.\n- id: fig3cd-clustering-raises-psv\n  statement: Both excitatory and inhibitory neurons have greater percent shared variance in the\n    clustered than in the non-clustered network, although connections involving inhibitory\n    neurons are the same in the two.\n  source: Results, Excitatory and inhibitory populations of balanced networks have different\n    activity structure, paragraph 6; Figure 3C and 3D, bottom\n  quote: we expected excitatory neurons to have greater percent shared variance in the clustered\n    than in the non-clustered network (compare red curves in Fig 3C and 3D , bottom).\n    Interestingly, we found that this was also true for the inhibitory neurons\n  data: elsewhere\n  where: GitHub sbittner12/litwin-kumar_doiron_cluster_2012 at commit 438289358d0367047cc578dcd519ad0f7948808e\n    (network code, rerun)\n  depends_on:\n  - fig3cd-trial-saturation\n  criterion: From the samplings of fig3cd-trial-saturation. Reproduced when, at 10,000 trials\n    and 100 neurons, the mean percent shared variance of each type is higher in the clustered\n    network than in the non-clustered one.\n- id: s3-100ms-window\n  statement: All the trends of Fig 3 hold with 100 ms spike count windows.\n  source: Results, Excitatory and inhibitory populations of balanced networks have different\n    activity structure, paragraph 6; S3 Fig legend\n  quote: All the trends observed in Fig 3 with one second spike count windows remained true with\n    100 ms spike count windows\n  data: elsewhere\n  where: GitHub sbittner12/litwin-kumar_doiron_cluster_2012 at commit 438289358d0367047cc578dcd519ad0f7948808e\n    (network code, rerun)\n  depends_on:\n  - fig3ab-dim-scaling-neurons\n  - fig3ab-psv-type-order\n  - fig3ab-inh-psv-grows\n  - fig3cd-trial-saturation\n  - fig3cd-clustering-raises-psv\n  criterion: Spike counts in the first 100 ms of each one-second trial, the same neurons and\n    trials (S3 Fig legend), and the criteria of the five claims listed under depends_on, each\n    under the reading that it was judged on there. Reproduced when all five hold; partially\n    reproduced when three or four do.\n- id: s2-psv-vs-correlation-width\n  statement: In simulated spike counts with zero-mean correlation distributions, percent shared\n    variance increases with the width (standard deviation) of the correlation distribution.\n  source: Results, Excitatory and inhibitory populations of balanced networks have different\n    activity structure, paragraph 4; S2 Fig legend\n  quote: We found that percent shared variance indeed increases with the variance of the spike\n    count correlation distribution\n  data: elsewhere\n  where: GitHub sbittner12/litwin-kumar_doiron_cluster_2012 at commit 438289358d0367047cc578dcd519ad0f7948808e\n    (network code, rerun; the means and variances come from the non-clustered network)\n  criterion: As the S2 Fig legend describes, correlations drawn from a normal distribution with\n    mean 0 and a chosen standard deviation, placed at random in a symmetric matrix, means and\n    variances matched to 100 randomly sampled inhibitory neurons of the non-clustered network,\n    100,000 counts for 100 neurons by the method of the paper's ref 44 (Macke et al. 2009,\n    which the attempt has to name and pin), five sets of 20,000 trials. The widths tested are\n    not given; the grid used is 0.005 to 0.04 in steps of 0.005, including 0.011 and 0.025.\n    Reproduced when the mean percent shared variance rises monotonically over the grid, or\n    with at most one step down smaller than its standard error; it is reported at 0.011 and\n    0.025.\n- id: fig4a-mode-structure\n  statement: In the clustered network the dominant modes of the excitatory population give\n    same-cluster neurons similar values, describing co-variation between clusters, while the\n    modes of the non-clustered excitatory population and of both inhibitory populations show no\n    obvious structure.\n  source: Results, Excitatory clustering affects modes of shared activity in both the excitatory\n    and inhibitory populations, paragraph 1; Figure 4A\n  quote: Same-cluster neurons had similar values within each mode for the excitatory population of\n    the clustered network, indicating that the dominant modes describe co-varying activity between\n    clusters. In contrast, the excitatory population of the non-clustered network ( Fig 4A ,\n    top-right) and both inhibitory populations ( Fig 4A , bottom) did not exhibit any obvious\n    structure\n  data: elsewhere\n  where: GitHub sbittner12/litwin-kumar_doiron_cluster_2012 at commit 438289358d0367047cc578dcd519ad0f7948808e\n    (network code, rerun)\n  criterion: 100-neuron samplings of each type, FA with the cross-validated m on all 10,000\n    trials (Methods, Factor analysis), the ten leading eigenvectors of LL^T. The paper judges\n    by eye; the measure set here is the fraction of the variance of each eigenvector's entries\n    explained by cluster membership (a one-way ANOVA R squared over clusters with at least two\n    sampled neurons), averaged over the ten modes. Reproduced when this fraction for clustered\n    E exceeds that of a shuffle of cluster labels (1,000 shuffles) at p < 0.05. For the other\n    populations, which have no clusters, the claim of no structure is not tested; their\n    heatmaps are shown.\n- id: fig4b-top-five-modes\n  statement: The five most dominant modes explain more shared variance in the clustered than the\n    non-clustered network, for excitatory (64.5% against 31.2%) and for inhibitory populations\n    (54.3% against 20.1%).\n  source: Results, Excitatory clustering affects modes of shared activity in both the excitatory\n    and inhibitory populations, paragraph 2; Figure 4B\n  quote: The five most dominant modes of shared activity explained 64.5% ± 1.5% of shared variance\n    in the clustered network and 31.2% ± 0.8% of shared variance in the non-clustered network ...\n    For inhibitory populations, the five most dominant modes of shared activity explained 54.3% ±\n    0.4% of shared variance in the clustered network and only 20.1% ± 0.2% of shared variance in\n    the non-clustered network\n  data: elsewhere\n  where: GitHub sbittner12/litwin-kumar_doiron_cluster_2012 at commit 438289358d0367047cc578dcd519ad0f7948808e\n    (network code, rerun)\n  expected:\n  - quantity: clustered E, shared variance in top five modes\n    value: 64.5\n    tolerance: 1.5\n    unit: '%'\n  - quantity: non-clustered E, shared variance in top five modes\n    value: 31.2\n    tolerance: 0.8\n    unit: '%'\n  - quantity: clustered I, shared variance in top five modes\n    value: 54.3\n    tolerance: 0.4\n    unit: '%'\n  - quantity: non-clustered I, shared variance in top five modes\n    value: 20.1\n    tolerance: 0.2\n    unit: '%'\n  criterion: 100-neuron samplings, five non-overlapping neuron sets by five non-overlapping sets\n    of 10,000 trials (Fig 4B legend), FA with the cross-validated m on each, the sum of the five\n    largest eigenvalues of LL^T over their total. Tolerances are the paper's standard errors.\n    Reproduced when the four values are within them; partially reproduced when they are within\n    10% and the clustered value exceeds the non-clustered one for each type.\n- id: fig5b-dim-rises-with-inhibitory-fraction\n  statement: In 100-neuron samplings with 10,000 trials, shared dimensionality increases as\n    excitatory neurons are replaced by inhibitory ones, in both networks.\n  source: Results, Ratio of excitatory to inhibitory neurons affects population activity\n    structure of mixed-type samplings, paragraph 2; Figure 5B, top\n  quote: As we replaced excitatory neurons with inhibitory neurons ( Fig 5 , moving left to right\n    along the horizontal axis), shared dimensionality increased from the only-excitatory neuron\n    sampling to the only-inhibitory neuron sampling for the clustered and non-clustered networks\n    with 10,000 trials\n  data: elsewhere\n  where: GitHub sbittner12/litwin-kumar_doiron_cluster_2012 at commit 438289358d0367047cc578dcd519ad0f7948808e\n    (network code, rerun)\n  criterion: Ratios 0:100 to 100:0 in steps of 10, excitatory neurons replacing inhibitory ones\n    10 at a time and kept as added, 25 repeats over five non-overlapping sets of 100 E and 100\n    I neurons and five non-overlapping trial sets (Methods, Mixed neuron type sampling).\n    Reproduced when, in each network, the mean d_shared at 0:100 (all inhibitory) exceeds that\n    at 100:0 and the Spearman correlation of the eleven means with the inhibitory fraction is\n    positive.\n- id: fig5b-psv-by-ratio\n  statement: As inhibitory neurons replace excitatory ones, the percent shared variance of\n    excitatory neurons decreases in the clustered network and increases in the non-clustered\n    network, while that of inhibitory neurons stays mostly unchanged in both.\n  source: Results, Ratio of excitatory to inhibitory neurons affects population activity\n    structure of mixed-type samplings, paragraph 3; Figure 5B, bottom\n  quote: In the clustered network, we found that as we replaced excitatory neurons with inhibitory\n    neurons, the percent shared variance for excitatory neurons decreased ( Fig 5B , bottom, dashed\n    red) ... In contrast, the percent shared variance of excitatory neurons in the non-clustered\n    network ( Fig 5B , bottom, solid red) increased as more inhibitory neurons were sampled ... The\n    percent shared variance of inhibitory neurons in both networks was mostly independent of\n    neuron type sampling ratio\n  data: elsewhere\n  where: GitHub sbittner12/litwin-kumar_doiron_cluster_2012 at commit 438289358d0367047cc578dcd519ad0f7948808e\n    (network code, rerun)\n  depends_on:\n  - fig5b-dim-rises-with-inhibitory-fraction\n  criterion: From the samplings of fig5b-dim-rises-with-inhibitory-fraction, percent shared\n    variance averaged over the E neurons (ratios 100:0 to 10:90) and over the I neurons\n    (ratios 90:10 to 0:100). Reproduced when the E value at 10:90 is below that at 100:0 in\n    the clustered network and above it in the non-clustered network, with Spearman\n    correlations of the matching sign over the ratios, and the I value varies by less than 10%\n    (relative) of its mean across ratios in both networks. \"Mostly independent\" has no\n    threshold in the paper; 10% is set here, and the range is reported.\n- id: fig5ac-trial-dependence\n  statement: With 1,200 trials the non-clustered network shows small shared dimensionality and\n    percent shared variance at all ratios; with 20,000 trials its dimensionality curve is\n    flatter than with 10,000; the clustered network's trends do not change from 10,000 to\n    20,000 trials, and with 1,200 trials its dimensionality for inhibitory-dominated ratios\n    drops.\n  source: Results, Ratio of excitatory to inhibitory neurons affects population activity\n    structure of mixed-type samplings, paragraphs 4 and 5; Figure 5A and 5C\n  quote: With 1,200 trials, the non-clustered network shared dimensionality ( Fig 5A , top, solid),\n    as well as the percent shared variance of excitatory ( Fig 5A , bottom, solid red) and\n    inhibitory ( Fig 5A , bottom, solid blue) neurons, were small for all ratios. With 20,000\n    trials, the non-clustered dimensionality was flatter than with 10,000 trials ... However, with\n    only 1,200 trials instead of 10,000 trials, the shared dimensionality for inhibitory neuron\n    dominated ratios dropped\n  data: elsewhere\n  where: GitHub sbittner12/litwin-kumar_doiron_cluster_2012 at commit 438289358d0367047cc578dcd519ad0f7948808e\n    (network code, rerun)\n  depends_on:\n  - fig5b-dim-rises-with-inhibitory-fraction\n  - fig5b-psv-by-ratio\n  criterion: The sampling of fig5b-dim-rises-with-inhibitory-fraction with 1,200 and 20,000\n    trials. Whether the five 20,000-trial sets overlap is open (see the opening comment).\n    \"Small\" is read as below 20% of the clustered network's value at the same ratio and trial\n    count; \"flatter\" as a smaller range (maximum minus minimum) of the mean d_shared over\n    ratios; \"did not change\" as the signs of the fig5b trends being the same at 20,000\n    trials; \"dropped\" as lower mean d_shared at 1,200 than at 10,000 trials for the ratios\n    30:70 to 0:100. Each of these readings is set here, as the paper gives none. Reproduced\n    when the four parts hold; partially reproduced when two or three do.\n- id: fig6-blind-sampling\n  statement: For 100-neuron, 10,000-trial samplings blind to neuron type, the clustered network\n    has a shared dimensionality of 20.3 and percent shared variance of 85.8%, and the\n    non-clustered network 43.1 and 23.7%.\n  source: Results, Neuron-type information reduces uncertainty of population activity metrics,\n    paragraph 2; Figure 6B and 6C\n  quote: The clustered network exhibited shared dimensionality of 20.3 ± 1.8 ( Fig 6B , dashed,\n    black, mean ± standard deviation) and percent shared variance of 85.8% ± 1.4% ( Fig 6C ,\n    dashed, black). The non-clustered network exhibited shared dimensionality of 43.1 ± 8.2 ( Fig\n    6B , solid, black) and percent shared variance of 23.7% ± 5.3%\n  data: elsewhere\n  where: GitHub sbittner12/litwin-kumar_doiron_cluster_2012 at commit 438289358d0367047cc578dcd519ad0f7948808e\n    (network code, rerun)\n  expected:\n  - quantity: clustered, blind sampling, mean d_shared\n    value: 20.3\n    tolerance: 2.03\n  - quantity: clustered, blind sampling, mean percent shared variance\n    value: 85.8\n    tolerance: 8.58\n    unit: '%'\n  - quantity: non-clustered, blind sampling, mean d_shared\n    value: 43.1\n    tolerance: 4.31\n  - quantity: non-clustered, blind sampling, mean percent shared variance\n    value: 23.7\n    tolerance: 2.37\n    unit: '%'\n  criterion: 100 neurons drawn at random from all 5,000 without regard to type, 10,000 trials;\n    percent shared variance averaged over all sampled neurons. The number of random samplings\n    and the trial sets are not given; readings, (a) 100 samplings each on one of the five\n    10,000-trial sets in turn, (b) 25 samplings, five per trial set. Tolerances are 10% of\n    each mean, as the plus-or-minus is the spread over samplings. Reproduced when the four\n    means are within tolerance under one reading.\n- id: fig6-type-control-reduces-spread\n  statement: Controlling neuron type composition (80 E, 20 I) lowers the standard deviation of\n    shared dimensionality in the non-clustered network from 8.2 to 6.8 and of percent shared\n    variance from 2.3 to 1.0 (clustered) and 5.2 to 4.5 (non-clustered), while the clustered\n    network's dimensionality spread stays at 2.0.\n  source: Results, Neuron-type information reduces uncertainty of population activity metrics,\n    paragraph 3; Figure 6B and 6C\n  quote: If neurons are randomly sampled from the network, the standard deviation is 8.2 ( Fig 6B ,\n    solid, black). However, if the neuron type composition is known and controlled for (in this\n    case, 80 E and 20 I), the standard deviation decreases to 6.8 ( Fig 6B , solid, green).\n    Similarly, the percent shared variance of the clustered and non-clustered networks decreases\n    when neuron type composition is controlled from 2.3 to 1.0 ( Fig 6C , dashed) and from 5.2 to\n    4.5 ( Fig 6C , solid), respectively. When sampling neurons randomly from the clustered network,\n    the standard deviation of shared dimensionality is 2.0 ( Fig 6B , dashed, black), which is the\n    same as when neuron type ratio is controlled\n  data: elsewhere\n  where: GitHub sbittner12/litwin-kumar_doiron_cluster_2012 at commit 438289358d0367047cc578dcd519ad0f7948808e\n    (network code, rerun)\n  depends_on:\n  - fig6-blind-sampling\n  expected:\n  - quantity: non-clustered, d_shared standard deviation, blind\n    value: 8.2\n    tolerance: 0.82\n  - quantity: non-clustered, d_shared standard deviation, 80 E and 20 I\n    value: 6.8\n    tolerance: 0.68\n  - quantity: clustered, percent shared variance standard deviation, blind\n    value: 2.3\n    tolerance: 0.23\n  - quantity: clustered, percent shared variance standard deviation, 80 E and 20 I\n    value: 1.0\n    tolerance: 0.1\n  - quantity: non-clustered, percent shared variance standard deviation, blind\n    value: 5.2\n    tolerance: 0.52\n  - quantity: non-clustered, percent shared variance standard deviation, 80 E and 20 I\n    value: 4.5\n    tolerance: 0.45\n  - quantity: clustered, d_shared standard deviation, blind and 80 E and 20 I\n    value: 2.0\n    tolerance: 0.2\n  criterion: The blind samplings of fig6-blind-sampling against samplings of exactly 80 E and 20\n    I, under the same readings. The paper's blind spreads differ between its two paragraphs\n    (clustered d_shared 1.8 and 2.0, clustered percent shared variance 1.4 and 2.3,\n    non-clustered percent shared variance 5.3 and 5.2); both printed values are readings of\n    the blind spread, and a value holds when it is within 10% of either. Reproduced when every\n    controlled spread is below its blind spread except clustered d_shared, which is within 10%\n    of it; partially reproduced when the reductions hold and some values are out of tolerance.\n- id: v1-classification-counts\n  statement: Waveform classification at 85% posterior probability gives 24 broad- and 39\n    narrow-spiking neurons, 41 and 72, 23 and 60, and 47 and 25 on the four arrays.\n  source: Materials and methods, Neuron type classification; Results, V1 recordings show similar\n    population activity structure as the clustered network, paragraph 1\n  quote: This resulted in the following distributions of classified neuron types for the four\n    arrays: 24 broad-spiking and 39 narrow-spiking, 41 broad-spiking and 72 narrow-spiking, 23\n    broad-spiking and 60 narrow-spiking, and 47 broad-spiking and 25 narrow-spiking neurons\n  depends_on:\n  - v1-array-link\n  expected:\n  - quantity: array 1, broad-spiking count\n    value: 24\n    tolerance: 2.4\n  - quantity: array 1, narrow-spiking count\n    value: 39\n    tolerance: 3.9\n  - quantity: array 2, broad-spiking count\n    value: 41\n    tolerance: 4.1\n  - quantity: array 2, narrow-spiking count\n    value: 72\n    tolerance: 7.2\n  - quantity: array 3, broad-spiking count\n    value: 23\n    tolerance: 2.3\n  - quantity: array 3, narrow-spiking count\n    value: 60\n    tolerance: 6.0\n  - quantity: array 4, broad-spiking count\n    value: 47\n    tolerance: 4.7\n  - quantity: array 4, narrow-spiking count\n    value: 25\n    tolerance: 2.5\n  criterion: Following the waveformClassification code, which settles what the Methods leave\n    open, average waveforms, two-Gaussian fits of the waveform and its derivative, a\n    two-component Gaussian mixture on fitted parameters 5, 6 and 7+10 (read as the Methods'\n    time of peak, duration of hyperpolarization and rate of repolarization), 10 replicates;\n    narrow is the component with the smaller mean of the first parameter; kept at posterior\n    above 0.85. Units first pass rate above 1 spike/s and SNR above 1.33 (Neural recordings).\n    Open, with readings, (a) training on the top 75% by SNR within each array (the code) or\n    pooled over the four arrays (the Methods' \"across all recording sessions\"); (b) the code's\n    shape-correlation exclusion at 0.5, or the Methods' exclusion of the four waveforms with a\n    pre-depolarization rise found by inspection, read as the units with a positive deflection\n    above 0.2 of the normalized amplitude before the trough; (c) the SNR readings of\n    v1-array-link. The mixture's random starts are a seed, a standard choice. The arrays are\n    matched by v1-array-link. Reproduced when all eight counts are within tolerance under one\n    reading; partially reproduced when every array has at least 23 neurons of each type and\n    the narrow-spiking majority on three arrays and broad on one hold. Needs average waveforms;\n    if the dataset holds none, the claim is blocked as data missing.\n- id: v1-fig7a-dim-with-neurons\n  statement: In V1 the shared dimensionality of both broad- and narrow-spiking populations\n    increases with neuron count (up to 23 neurons, 1,200 trials), as in the clustered network.\n  source: Results, V1 recordings show similar population activity structure as the clustered\n    network, paragraph 2; Figure 7A, top\n  quote: The shared dimensionality of the broad-spiking population (red) and narrow-spiking\n    population (blue) increased with increasing neuron count ( Fig 7A , top)\n  depends_on:\n  - v1-classification-counts\n  criterion: Per array, 23 neurons of each type chosen at random from the classified neurons;\n    for each neuron count, as many non-overlapping samples of the 23 as possible, FA on each\n    with 1,200 trials, averaged, then mean and standard error over the four arrays (Methods,\n    Varying neuron and trial count; Fig 7 legend). Open, with readings, the neuron-count grid\n    (no figure read; used, 2 to 23 in steps of 1, and a coarser 5, 10, 15, 20, 23) and which\n    1,200 trials (the first 1,200 one-second epochs, or 1,200 drawn at random). Reproduced\n    when, for both types, the four-array mean d_shared at 23 neurons exceeds that at the\n    smallest count and the Spearman correlation of the means with neuron count is positive.\n- id: v1-fig7a-psv-plateau\n  statement: In V1 the percent shared variance of both broad- and narrow-spiking populations\n    first increases with neuron count and then plateaus.\n  source: Results, V1 recordings show similar population activity structure as the clustered\n    network, paragraph 2; Figure 7A, bottom\n  quote: The percent shared variance of the broad-spiking and narrow-spiking populations initially\n    increased with neuron count, then plateaued\n  depends_on:\n  - v1-fig7a-dim-with-neurons\n  criterion: From the samplings of v1-fig7a-dim-with-neurons. Plateau is not defined;\n    readings, the four-array mean at the largest count is within (a) 10% or (b) one standard\n    error over arrays of its value at the midpoint count (11 or 12, or 10 on the coarse grid),\n    while the value at the midpoint exceeds that at the smallest count. Reproduced when this\n    holds for both types under one reading; partially reproduced for one type.\n- id: v1-fig7d-trial-plateau\n  statement: In V1, with 23 neurons, the shared dimensionality of both populations increases and\n    plateaus with trial count, and their percent shared variance plateaus.\n  source: Results, V1 recordings show similar population activity structure as the clustered\n    network, paragraph 3; Figure 7D\n  quote: The shared dimensionality of both neuron types in the V1 recordings ( Fig 7D , top), as\n    well as the clustered network ( Fig 7E , top), increased and eventually plateaued with\n    increasing trial count. Similarly the percent shared variance of both populations plateaued\n    with increasing trial count in both the V1 recordings\n  depends_on:\n  - v1-classification-counts\n  criterion: Per array, the 23 neurons of each type; trials increased up to 1,200, with as many\n    non-overlapping trial samples as possible at each count (Methods, Varying neuron and trial\n    count). The trial grid is open (used, 100, 200, 300, 400, 600 and 1,200, and in steps of\n    100). Readings for plateau as in v1-fig7a-psv-plateau, comparing 1,200 with 600 trials.\n    Reproduced when d_shared rises from 100 to 600 trials and plateaus, and percent shared\n    variance plateaus, for both types under one reading; partially reproduced when this holds\n    for three of the four curves.\n- id: v1-no-excitatory-psv-advantage\n  statement: Unlike the clustered network, where excitatory neurons have higher percent shared\n    variance than inhibitory ones, V1 broad-spiking neurons do not show higher percent shared\n    variance than narrow-spiking neurons.\n  source: Results, V1 recordings show similar population activity structure as the clustered\n    network, paragraph 4; Figure 7A, 7B, 7D and 7E, bottom\n  quote: whereas the excitatory neurons showed higher percent shared variance than inhibitory\n    neurons in the clustered network ( Fig 7B and 7E , bottom), this was not seen in the V1\n    recordings\n  depends_on:\n  - v1-fig7a-dim-with-neurons\n  - v1-fig7d-trial-plateau\n  criterion: A claim of absence for which the paper reports no test; it compares the curves by\n    eye with standard error bars over four arrays. The rule set here, as the paper's figure\n    implies, is that the broad-spiking four-array mean is not above the narrow-spiking mean by\n    more than the larger of the two standard errors, at 23 neurons and 1,200 trials and at each\n    count of the neuron and trial sweeps. Reproduced when that holds at 23 neurons and 1,200\n    trials and at most counts; not reproduced when broad exceeds narrow by more than that at 23\n    neurons and 1,200 trials. The difference and its sign per array are given either way.\n- id: v1-resembles-clustered-network\n  statement: With 23 neurons of each type and 1,200 trials, V1 population activity structure\n    resembles that of the clustered network, while the non-clustered network shows nearly zero\n    shared dimensionality and percent shared variance for both types.\n  source: Results, V1 recordings show similar population activity structure as the clustered\n    network, paragraphs 2 to 4; Figure 7B, 7C, 7E and 7F; Discussion, paragraph 1\n  quote: The V1 recordings had similar population activity structure to the corresponding\n    populations in the clustered network when compared with 23 neurons of each type and 1,200\n    trials sampled ... In contrast, the non-clustered network was different from both the V1\n    recordings and clustered network in that it showed nearly zero shared dimensionality and\n    percent shared variance for both neuron types\n  data: with_inputs\n  depends_on:\n  - v1-fig7a-dim-with-neurons\n  - v1-fig7a-psv-plateau\n  - v1-fig7d-trial-plateau\n  criterion: The networks sampled with the V1 numbers, 23 neurons per type and up to 1,200\n    trials, four non-overlapping samplings (Fig 7 legend), the same grids as the V1 claims.\n    Reproduced when (a) the clustered network's d_shared rises with neuron count for both types\n    (the rule of v1-fig7a-dim-with-neurons), (b) its d_shared and percent shared variance rise\n    and plateau with trial count (v1-fig7d-trial-plateau), and (c) the non-clustered network's\n    mean d_shared is below 1 and its percent shared variance below 5% at 23 neurons and 1,200\n    trials for both types. \"Nearly zero\" has no threshold in the paper; the thresholds in (c)\n    are set here and the values are reported. Partially reproduced when (c) holds and one of\n    (a) and (b) fails.\n- id: s6-v1-dominant-mode-same-sign\n  statement: In V1 the dominant mode of shared activity of both broad- and narrow-spiking\n    populations describes the population rising and falling together, nearly all entries having\n    the same sign, unlike the dominant modes of the clustered network.\n  source: Results, V1 recordings show similar population activity structure as the clustered\n    network, paragraph 4; S6 Fig\n  quote: the mode that explained the largest amount of shared variance (referred to as the\n    \"dominant mode\") in the V1 recordings described the population increasing and decreasing its\n    activity together ( S6 Fig , left column of heatmaps have nearly all elements of the same sign)\n  depends_on:\n  - v1-classification-counts\n  criterion: Per array and type, FA on the 23 neurons with all 1,200 trials and the\n    cross-validated m, the eigenvector of LL^T with the largest eigenvalue. The S6 Fig legend\n    does not say which arrays it shows; all four are used. \"Nearly all\" is open; readings,\n    (a) at least 20 of 23 entries and (b) at least 18 of 23 share the sign of the majority.\n    Reproduced when, under one reading, this holds for both types on at least three of the\n    four arrays. The clustered network's dominant modes (fig4a-mode-structure) are reported\n    by the same count, without a criterion, as the paper does not quantify them.\n- id: s1-autocorrelation-to-one-second\n  statement: Neurons in both model networks and in V1 show non-zero autocorrelation at lags\n    from zero to one second.\n  source: Results, Excitatory and inhibitory populations of balanced networks have different\n    activity structure, paragraph 2; S1 Fig\n  quote: we found that neurons in both model networks and the in vivo recordings exhibited\n    non-zero autocorrelation at lags throughout the range of zero to one second\n  depends_on:\n  - v1-classification-counts\n  data: with_inputs\n  criterion: Spike counts in 10 ms bins, autocorrelation per neuron normalized to one at zero\n    lag, averaged over neurons of each type (S1 Fig legend). For V1 the neurons are open,\n    readings (a) the 23 analysed per type and array, (b) all classified neurons; the\n    networks use all neurons of each type. Non-zero is read as the mean autocorrelation above\n    zero at every lag from 10 ms to 1 s, the reading set here. Reproduced when this holds for\n    both V1 types and for both types of both networks under one reading; partially reproduced\n    when it holds for V1 only.\n"
}
```

```
File created successfully at: claims/bittner-2017.yaml (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
python tools/claims_check.py claims/bittner-2017.yaml paper/10.1371-journal.pone.0181773.txt; grep -n ": " claims/bittner-2017.yaml | grep -v "^[0-9]*: *[-a-z_]*: \|^[0-9]*:  *- [a-z_]*: " | grep -v "^[0-9]*:#" | head
```

Result: not kept, because it reads the paper's text.

**Agent**

Cut the quote at the colon.

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/bittner-2017.yaml",
 "old_string": "  quote: This resulted in the following distributions of classified neuron types for the four\n    arrays: 24 broad-spiking and 39 narrow-spiking, 41",
 "new_string": "  quote: This resulted in the following distributions of classified neuron types for the four\n    arrays ... 24 broad-spiking and 39 narrow-spiking, 41"
}
```

```
The file claims/bittner-2017.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
python tools/claims_check.py claims/bittner-2017.yaml paper/10.1371-journal.pone.0181773.txt; python - <<'E'
import yaml,re
d=yaml.safe_load(open('claims/bittner-2017.yaml'))
c=d['claims'];print(len(c),sum('quote' in x for x in c),sum('criterion' in x for x in c),sum('statistics' in x for x in c))
t=open('claims/bittner-2017.yaml').read();print('—' in t, 'rather' in t.lower())
E
```

Result: not kept, because it reads the paper's text.

**Agent**

I wrote `claims/bittner-2017.yaml`. The quote checker reports 26 claims, 26 quotes and 0 problems. Nothing is committed.

**Text read:** the version of record, PMC5560553 (open access, Europe PMC full-text XML). That covers the main text, Methods and figure legends, plus the legends of S1 to S6 Fig. The supplement has nothing beyond those legends. There was no PDF, so I read no figure.

**Code read:**
- **Network code:** `sbittner12/litwin-kumar_doiron_cluster_2012` at commit `4382893`. It holds the clustered network only. It adds a stimulus in the last 500 ms, and its same-cluster E-E weight is 0.0448 where the Methods give 0.0456.
- **Classification code:** `adam-neuro/waveformClassification` at commit `062762678`. It fixes the three waveform features, the training on the top 75% of neurons by SNR within each file, a waveform-shape exclusion and its SNR formula.
- **Factor analysis code:** the paper links none.

**Claims:**
- **Totals:** 26 claims (1 is a link check that identifies the arrays), all with quotes, 26 with criteria, 0 with `statistics`. The paper reports no statistical tests.
- **Data:** 17 claims are on the model networks (`data: elsewhere`, rerun from the network code). 7 are on V1 recordings in the dataset. 2 compare the dataset with the models (`with_inputs`).
- **Tolerances:** 9 claims carry expected values. Where the ± is a standard error I used it as the tolerance; where it is a spread over neurons or samplings, I used 10%. Correlations printed near zero are judged as an absolute value below 0.01; I set that threshold, with the reason given.

**Details the paper leaves open, and the readings named:**
- **Which arrays:** the dataset holds 6 spontaneous arrays; the paper used 4, from 3 monkeys. They are identified by the paper's median SNRs.
- **SNR definition:** (a) the dataset's SNR field, or (b) the code's amplitude over twice the standard deviation.
- **Classifier training:** (a) top 75% by SNR within each array (the code), or (b) pooled across arrays (the Methods). The excluded waveforms are either (a) the code's shape-correlation rule or (b) the Methods' four neurons excluded by inspection.
- **Which 1,200 trials:** the first 1,200, or 1,200 drawn at random.
- **Sampling grids:** neuron-count and trial-count grids for Fig 3 and Fig 7 are not given. I used standard grids.
- **Factor analysis:** the grid of candidate dimensions (I used every value from 0 to n−1) and how trials are assigned to the four folds (contiguous or random; both run).
- **Simulations:** duration, whether the 20,000-trial sets overlap, the transient discarded, and the network seed.
- **Fig 6:** how many blind samplings were drawn, and on which trial sets.
- **Undefined words:** "saturate", "plateau", "nearly zero", "mostly independent" and "nearly all same sign" have no thresholds in the paper. I set explicit ones and say so in each criterion.
- **Conflicting numbers in the paper:**
  - The blind-sampling spreads differ between two paragraphs (1.8 and 2.0, 1.4 and 2.3, 5.3 and 5.2).
  - The non-clustered E-E correlation spread is printed as 0.11 in the Fig 1D legend and 0.011 in the S2 Fig legend.

  In each case both values are named as readings.
- **Mislabels in the paper:** the Fig 7 legend letters A to D while the Results cite 7A to 7F. The Methods and Discussion cite Fig 6 where Fig 7 is meant.

**Missing, which claims need:**
- **Waveforms:** the dataset's description lists no average waveforms. Without them the classification, and every V1 claim that depends on it, cannot be redone. The author should check; if there are none, `v1-classification-counts` is blocked as data missing.
- **Simulations and factor analysis code:** the simulations are not deposited, the factor analysis code is not linked, and the non-clustered network must be built from the Methods.
- **Fig 7 readings:** with no PDF, the values in the Fig 7 panels could not be read.

## End of run

15 turns, 5 minutes, $1.56 at API prices, result: success.
