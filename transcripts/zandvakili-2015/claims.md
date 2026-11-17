# zandvakili-2015 · claims · run 42867807049

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cat docs/protocol.md; ls paper/ | grep -i zandv; ls claims | head
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
grep -n "^#" docs/protocol.md; ls paper/ | grep -i zand; ls paper | head -3
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "docs/protocol.md",
 "offset": 43,
 "limit": 156
}
```

```
43	## Reader
44	
45	### 1. Get the paper
46	
47	The workflow puts the paper's full text, and its PDF where there is one, under
48	`paper/`: the main text, the Methods, and the supplement. Read the text; open
49	the PDF only to read a figure or a table the text garbles. If the full text is
50	not there, or lacks the Methods or a supplement the results rest on, stop:
51	write no claims, and end with a report that names what is missing, so that it
52	can be supplied. Never write claims from the abstract. Do not copy figures.
53	Do not look at the dataset's data: its title and description on the archive
54	are enough to know which paper and which experiments it is meant to hold. A
55	data descriptor under `paper/` (`<id>.data-description.txt`, the dataset's own
56	documentation) is a longer description, to be read for that alone; it is not
57	the paper, and no claim comes from it.
58	
59	### 2. Read the paper's code
60	
61	Read the code the paper links to before writing criteria. Say what it holds,
62	and record the repository and commit read. Where the Methods leave a choice
[... 136 more lines not kept]
```

**Agent calls Bash**

```bash
cat claims/fouke-2025.yaml; cat paper/v1v2-1.data-description.txt; wc -l paper/*.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1016-j.neuron.2015.07.026.txt",
 "limit": 700
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1016-j.neuron.2015.07.026.txt",
 "offset": 700,
 "limit": 1320
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1016-j.neuron.2015.07.026.txt",
 "offset": 700,
 "limit": 650
}
```

Result: not kept, because it reads the paper's text.

**Agent**

Main text and supplement are both present. Reading the supplement now.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1016-j.neuron.2015.07.026.txt",
 "offset": 1349,
 "limit": 670
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cat papers/datasets/zandvakili-2015.yaml 2>/dev/null; ls claims | grep -i -E "semedo|crcns|v1v2"; grep -rl "crcns" claims | head -3; sed -n 1,60p tools/claims_check.py
```

```
# The datasets this paper is tested on (docs/paper-first.md).
schema_version: 1
paper: doi:10.1016/j.neuron.2015.07.026
title: Coordinated Neuronal Activity Enhances Corticocortical Communication
datasets:
- archive: crcns
  id: v1v2-1
  relation: primary
claims/li-2016/crcns-alm-3.yaml
claims/li-2016/000011.yaml
claims/moaddab-2021.yaml
"""Check a claims file against the full text of its paper.

    python tools/claims_check.py claims/<dandiset>/<doi>.yaml paper/<text>.txt [more texts ...]

Validates the file against schemas/claims.schema.json, checks every quote word for word
(fragments split on "...", found in order) and looks for every recorded p-value and
confidence-interval bound in the text. The text may be plain text, HTML or JATS XML; several
files (a paper and its supplement) are searched together. A value printed in a form the
checker does not know (a garbled PDF glyph, "p = 0.04, 0.05 and 0.16") is reported, to be
[... 51 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 1,40p claims/moaddab-2021.yaml; python -c "import json;s=json.load(open('schemas/claims.schema.json'));print(json.dumps(s,indent=1)[:5000])"
```

```
# Claims for Moaddab & McDannald (2021), Curr Biol 31:2099-2110, "Retrorubral field is a hub for
# diverse threat and aversive outcome signals", on CRCNS data set rrf-1 (doi:10.6080/K04B2ZJ5).
# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"), 2026-11-06,
# protocol as stated in docs/protocol.md (Reader), version pilot-13.
#
# Text read: the version of record with its supplemental information, as supplied under paper/
# (PyMuPDF text of the journal PDF): Results, Discussion, figure legends, Table 1, STAR Methods,
# and the supplement (Figures S1 to S6, Tables S1 to S4). The text garbles powers of ten ("2.80 3
# 10�11" is 2.80 x 10^-11, "5.93E�38" is 5.93E-38); p-values below are read from them, and the
# quote checker cannot find these, so they were confirmed by reading (also Table S3's "1.50E-02",
# "1.16E-04", "2.39E-04", and the Figure S4 bound printed "1-.62"). The column layout of Tables
# S1 to S4 and the Figure 6 panels were read from the PDF pages rendered as images: Table S1 rows
# are danger vs. uncertainty then uncertainty vs. safety; Table S2 columns are peak threat
# probability, fear output, then their difference; Table S3 rows are the regressor x bin
# interaction then the main effect of regressor; Table S4 rows are danger, uncertainty shock,
# uncertainty omission, safety. The gray boxes of Figure 6 (the analysed outcome interval) span 0
# to 8 s after shock offset for k1, k3, k5 and k6, and the whole 17.5 s for k2, k4, k7 and k8.
#
# Code. The paper says its "MATLAB code will be uploaded to http://crcns.org/", which puts it inside
# the data set, which the reader may not open; the lab page it names for behavior programs
[... 168 more lines not kept]
```

**Agent calls Bash**

```bash
python -c "import json;s=json.load(open('schemas/claims.schema.json'));print(json.dumps(s['\$defs'],indent=1))"
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
[... 82 more lines not kept]
```

**Agent calls Bash**

```bash
python -c "
import json;s=json.load(open('schemas/claims.schema.json'))
p=s['properties']['claims']['items']['properties']
for k,v in p.items(): print(k, '|', v.get('description','')[:300])
print(list(s['properties']))"
```

```
id | Stable within the file, e.g. fig2b.
statement | The finding in one or two sentences, in words. Not a copy of the figure.
source | Where the paper shows it, precise enough to find without searching: a figure panel, e.g. 'Figure 2B', or a section and paragraph, e.g. 'Results, Place fields, paragraph 3'.
kind | A finding the paper reports (`finding`, the default), or a check the registry adds that the dataset is the data the paper's outside material describes (`link`: the paper's tables, source data, code or deposits). Links are not findings of the paper and are counted apart from them.
quote | The sentence of the paper that states the finding, word for word, from the place `source` names, so a reader can check the statement against the paper. Cut with '...' where it runs long. From the full text.
inferred | For a finding with no quote: why the statement is the author's reading and not a sentence of the paper, e.g. 'Numbers from Supplementary Table 1; no sentence states them.'
expected | The reported numbers the claim rests on, each with a tolerance: one, or a list.
statistics | The statistical support the paper reports for the finding: one entry per test or interval, as the paper gives it. A record of the paper, not a target with a tolerance (that is `expected`).
criterion | For a claim without a number, how it will be judged. Written before the analysis is run.
depends_on | Ids of claims in this file whose result this one uses.
data | What the claim's test uses: the dataset alone (`dataset`, the default); the dataset with names for its own codes taken from elsewhere (`with_labels`), which counts as the dataset; the dataset with other data from elsewhere (`with_inputs`), which is counted apart; or data the paper deposited in anoth
where | For a claim with data `elsewhere`: the archive and the pinned identifier of the data, e.g. 'PRIDE PXD012345' or 'Zenodo doi:10.5281/zenodo.123'.
datasets | Only when the paper is tested on more than one dataset: the folder names
[... 1 more lines not kept]
```

**Agent calls Bash**

```bash
grep -n -i -B2 -A8 "simulat\|model fit" claims/*.yaml | grep -i -E "data:|criterion|simulat" | head -20
```

```
claims/andrews-2024.yaml:31:# (Theta_Wave_Videos) and the NEST simulation (Simulation). The R code for the t-tests, the
claims/andrews-2024.yaml:166:- id: simulation-dampening
claims/andrews-2024.yaml:171:    3; Methods, Simulation Prototype
claims/andrews-2024.yaml-174-  data: elsewhere
claims/andrews-2024.yaml:176:    Simulation directory (model code, rerun)
claims/andrews-2024.yaml:177:  criterion: Run Simulation/simulation.py as published (NEST 3.4, NESTML, 1000 granule and 12
claims/andrews-2024.yaml:179:    Simulation Prototype) with the opsin fraction 0, 0.10, 0.25 and 0.50. The measure of
claims/armstrong-2026.yaml-622-    4B ) produces best fit (Bayesian information criterion, BIC of −664, Fig. 4C ) for nondecision
claims/athalye-2023.yaml:11:# S2 (simulation statistics, Figure 6). The columns of Tables S1 and S2 were read from the
claims/athalye-2023.yaml:21:# the OFC simulations (LQR/behavior_co_obs.py, LQR/analyze_lqr.py and the notebooks
claims/athalye-2023.yaml:42:# simulations built from the dynamics fitted to these data and the sessions' decoders.
claims/athalye-2023.yaml:997:  quote: "These simulations revealed that the population required significantly less input in the
claims/athalye-2023.yaml:1013:  criterion: Simulation as in Methods, Optimal feedback control model and simulation. Per session,
claims/athalye-2023.yaml:1019:    noiseless No Dynamics simulation; No Dynamics Model A = 0 with b kept. Input magnitude per
claims/athalye-2023.yaml:1050:  statement: In the OFC simulations, activity issuing the same command differs between conditions
claims/athalye-2023.yaml:1095:  criterion: On the simulations of fig6c and fig6d, commands discretized and tuples of 15 or more
claims/athalye-2023.yaml:1098:    shuffle (Methods, Simulated activity issuing a given command) and do not give the number of
claims/athalye-2023.yaml:1099:    shuffles for the simulations; the code draws condition-sized subsamples of the matched pool
claims/athalye-2023.yaml:1100: 
[... 1 more lines not kept]
```

**Agent calls Bash**

```bash
python -c "
import json;s=json.load(open('schemas/claims.schema.json'))
it=s['properties']['claims']['items'];print({k:v for k,v in it.items() if k!='properties'})"; grep -n -i "simulat\|no data\|model only" docs/protocol.md | head
```

```
{'type': 'object', 'additionalProperties': False, 'required': ['id', 'statement', 'source'], 'allOf': [{'not': {'required': ['quote', 'inferred']}}, {'if': {'properties': {'kind': {'const': 'link'}}, 'required': ['kind']}, 'then': {'not': {'required': ['inferred']}}}, {'if': {'properties': {'data': {'const': 'elsewhere'}}, 'required': ['data']}, 'then': {'required': ['where']}}]}
```

**Agent calls Bash**

```bash
cd $TMPDIR && python -c "
import fitz
d=fitz.open('paper/10.1016-j.neuron.2015.07.026.pdf')
print(len(d))
for i in (7,23):
    d[i].get_pixmap(dpi=110).save(f'p{i+1}.png')
" && ls $TMPDIR
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1016-j.neuron.2015.07.026.pdf",
 "pages": "24"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1016-j.neuron.2015.07.026.pdf",
 "pages": "8"
}
```

Result: not kept, because it reads the paper's text.

**Agent**

Full text with Methods and the supplement is present. The paper links no code. Writing the claims file now.

**Agent calls Write**

```json
{
 "file_path": "claims/zandvakili-2015.yaml",
 "content": "# Claims for Zandvakili & Kohn (2015), Neuron 87, 827-839, \"Coordinated Neuronal Activity Enhances\n# Corticocortical Communication\" (doi:10.1016/j.neuron.2015.07.026), on CRCNS data set v1v2-1.\n# Written by an agent (model \"claude-opus-5-5\", Claude Code, runner \"GitHub Actions\"), 2026-11-10,\n# protocol as stated in docs/protocol.md (Reader), version pilot-14.\n#\n# Text read. The version of record as supplied under paper/ (PyMuPDF text of the journal PDF, with\n# the Supplemental Information appended): Results, Discussion, figure legends, Experimental\n# Procedures, and the supplement (Figures S1 to S6 with their texts, Supplemental Experimental\n# Procedures). The PDF pages could not be rendered in this run, so no figure was read from the\n# image; every value below is from the text. The extracted text prints the degree sign as a\n# replacement glyph and a few dashes oddly; one such case is named in figS5-middle-layer-relay.\n#\n# Code. The paper links no analysis code and names no repository. No code was read; every\n# method below is from the Experimental Procedures, the Results, the figure legends or the\n# supplement, and details none of them fixes are named as open.\n#\n# Data the paper used. Nine hemispheres of seven anesthetized (sufentanil), paralyzed adult male\n# Macaca fascicularis. V1 recorded with a 10 x 10 Utah array (1 mm electrodes, 400 um spacing,\n# layers 2/3 and 4B), RFs 2 to 4 deg from the fovea; 10 array implants, V1 populations of 61 to 160\n# units (average 98). V2 recorded with seven moveable electrodes and tetrodes (300 um spacing) in\n# translaminar penetrations through V1 and the white matter; 16 penetrations and 55 V2 recording\n# sites (the CCG analysis counts 223 V2 sites, one per electrode and site), 896 V2 cells in all.\n# Units are single units and small clusters with waveform SNR of 2 or more and a mean rate of at\n# least 0.5 sp/s across stimuli. V2 depth is given relative to the layer 6/white matter border.\n# Stimuli are full-contrast drifting gratings (1 cycle/deg, 3 to 6.5 Hz, typically 2 to 3.5 deg) of 8\n# orientations at 22.5 deg steps, 1.28 s each with 1.5 s blanks, 300 to 400 presentations each;\n# RFs were mapped with 0.6 deg gratings and fit with a 2D Gaussian (diameter as +/-2 SD). Measured\n# variables are spike times of V1 and V2 units per trial, stimulus orientation, RF fits, V2 site\n# depth and unit SNR. The CRCNS data set, by its title and description, holds 5 of these recording\n# sessions in 3 animals (V1 array and V2 tetrodes, spike times, stimulus identity per trial and\n# RF fits per channel), so the paper's totals (896 V2 cells, 223 sites, 83,441 pairs, the epoch\n# counts) describe a larger sample than the data set; proportions and medians are the values the\n# attempt compares, and counts are reported beside them.\n#\n# Shared CCG method (Experimental Procedures, Pairwise V1-V2 Analysis). Spike trains as binary\n# series at 0.1 ms; CCG of Equation 1 (normalized by trial count, the triangular overlap function\n# Q and the V1 rate), computed per stimulus, shuffle-corrected for stimulus-locked correlation,\n# then combined over stimuli. Jitter-corrected CCG is the CCG minus the expected CCG of jittered\n# data (Smith and Kohn 2008), smoothed with a Gaussian of SD 1.5 ms. A pair, or a V2 site from its\n# site-average CCG over all V1-V2 pairs at that V2 electrode and site, is significant when the\n# jitter-corrected peak within 10 ms of zero lag exceeds 5 SD of the noise in the flanks (75 to 125\n# ms on both sides). Open, and named where it matters: (j-a) the CCG jitter window, given only as\n# 10 ms for Figure 4C (used here for all narrow-peak tests) or (j-b) another window; the analysis\n# window within the trial (the whole 1.28 s, or from 50 ms after onset as in the divergence\n# analysis), a standard choice that is not expected to change the outcome; whether the peak is\n# the maximum of the smoothed CCG (used here) or of the raw one.\n#\n# Shared divergence method (Experimental Procedures, Divergence Analysis; Results, V2 Spiking Is\n# Preceded by Stronger V1 Coordination). The V1 network state is the proportion of V1 units active\n# in a 1 ms window. For each spike of each V2 neuron in a group, the states in the epoch 1.5 to 3.5\n# ms before (or, for other offsets, around) the spike are pooled into one distribution over all\n# spikes and neurons of the group. Responses are used from 50 ms after stimulus onset to the end\n# of the stimulus. The surrogate distribution comes from the same epochs in jittered V1 data:\n# jitter windows tile the trial from 50 ms after stimulus onset, and each V1 spike is replaced by\n# one drawn with replacement from the spikes that neuron fired in the same window on other trials,\n# so each neuron's count per window and trial is kept. Windows are 5, 10, 20, 40, 80 and 1280 ms\n# (Figure 6; Figure 7 uses 5 to 80). Divergence is Jensen-Shannon (Equations 2 and 3), in bits\n# (log base 2, as the figures label bits). Control epochs take, for each V2 spike, an epoch from\n# another trial at the same time after stimulus onset, as many control epochs as spike epochs.\n# Confidence intervals by bootstrap over V2 neurons resampled with replacement, 5000 draws (Figure\n# 6 legend), 95% intervals (Figure 7 legend). Open, and named where they matter: (e-a) the 2 ms\n# epoch contributes its two 1 ms bins (1.5 to 2.5 and 2.5 to 3.5 ms before the spike) or (e-b) the\n# one 1 ms bin centred 2.5 ms before; (s-a) the jittered spikes and the control trials are taken\n# from trials of the same grating orientation (the CCGs are computed per stimulus) or (s-b) from\n# all trials; (r-a) one jitter realization per divergence or (r-b) the mean distribution of\n# several; (p-a) the bootstrap p-value as the fraction of draws, neurons resampled once and used\n# for both spike and control epochs, in which the control divergence is at least the spike\n# divergence, or (p-b) the two bootstrap distributions compared as independent (fraction of\n# draw pairs where control is at least spike). A comparison is significant at p < 0.05 two-sided\n# under the reading in use. The outcome is the one all readings give; where they differ, every\n# result is shown and the readings that match are named.\n#\n# Layer groups (Results; Experimental Procedures). Middle-layer V2 sites are those whose\n# site-average V1-V2 CCG has a significant narrow peak, chosen per electrode. Non-middle sites are\n# those superficial to or deeper than such sites in the same penetration. Offset-RF neurons are V2\n# neurons 500 to 1000 um from the layer 6/WM border whose RF centre is at least 3 deg from the centre\n# of the V1 population (the mean of the V1 RF centres, a standard reading of \"the center of the V1\n# population\").\nschema_version: 2\npaper: doi:10.1016/j.neuron.2015.07.026\nclaims:\n- id: fig4c-broad-ccg-peaks\n  statement: V1-V2 CCGs frequently have broad peaks, tens to hundreds of milliseconds wide, evident\n    in site-average CCGs at all laminar locations.\n  source: Results, V1-V2 Recordings, paragraph 3; Figure 4C, left\n  quote: We frequently observed broad peaks in V1-V2 CCGs, tens to hundreds of milliseconds wide.\n    These were evident in the average V1-V2 CCGs at all laminar locations\n  criterion: Site-average shuffle-corrected CCGs (shared CCG method, not jitter-corrected). The\n    paper gives no test for a broad peak, so one is fixed here and is open. Readings, (a) the mean\n    CCG over lags -50 to +50 ms is above the mean over the 75 to 125 ms flanks; (b) the mean over\n    lags -50 to +50 ms is above zero. Reproduced when, under one reading, a majority of V2 sites\n    have such a peak and sites both with and without a significant narrow peak have it. The\n    fraction of sites and the width at half height of the across-site average are reported.\n- id: fig4c-narrow-peak-sites\n  statement: A significant narrow peak in the site-average V1-V2 CCG occurs at a minority of V2\n    sites (46 of 223).\n  source: Results, V1-V2 Recordings, paragraph 4\n  quote: Average V1-V2 CCGs contained a significant narrow peak at 46 of 223 V2 sites\n  expected:\n  - quantity: fraction of V2 sites with a significant site-average narrow peak\n    value: 0.206\n    tolerance: 0.021\n  criterion: Shared CCG method, site-average jitter-corrected CCG per V2 electrode and site, 5 SD\n    rule. The paper's sample targeted middle-layer sites in some penetrations (Experimental\n    Procedures, Physiology), so the fraction depends on sampling; the count of sites and of\n    significant sites is reported beside the fraction.\n- id: fig4-narrow-peak-depth\n  statement: V2 sites with a narrow V1-V2 CCG peak lie on average 694 um superficial to the layer\n    6/white matter border, the expected depth of layer 4 and deep layer 3.\n  source: Results, V1-V2 Recordings, paragraph 4\n  quote: whose mean depth was 694 ± 49 (SEM) microns superficial to the layer 6/white matter border\n  expected:\n  - quantity: mean depth of narrow-peak V2 sites above the layer 6/WM border\n    value: 694\n    tolerance: 49\n    unit: um\n  criterion: Tolerance is the paper's SEM. Depth as the paper gives it, relative to the layer\n    6/WM border; needs a site depth on that reference.\n- id: fig5a-rf-alignment\n  statement: The probability that a V1-V2 pair has a significant narrow CCG peak is highest for RF\n    offsets below 0.5 deg, about 1%, and falls quickly with greater offset.\n  source: Results, V1-V2 Recordings, paragraph 5; Figure 5A\n  quote: The probability was highest for pairs with offsets of <0.5�, and decayed quickly with\n    greater offsets (Figure 5A). Even for pairs with well-aligned RFs, the probability was only\n    �1%\n  expected:\n  - quantity: probability of a significant narrow peak, pairs with RF offset below 0.5 deg\n    value: 0.01\n    tolerance: 0.001\n  criterion: Pairs judged by the 5 SD rule (shared CCG method); RF centre-to-centre distance from\n    the 2D Gaussian fits (Visual Stimuli). Bins of 0.5 deg from 0 to 4 deg, a standard choice\n    matching the abscissa of Figure 5A. Reproduced when the 0 to 0.5 deg bin has the highest\n    probability, the probability in the 1 to 1.5 deg bin is below half of it, and the 0 to 0.5\n    deg value is within tolerance; partially reproduced when the ordering holds and the value\n    does not. Open, the conversion of RF positions to degrees, which the paper does not give (it\n    gives 1024 x 768 pixels at 110 cm but no screen size); the attempt states the scale it uses\n    and where it comes from.\n- id: fig5-narrow-pairs-rare\n  statement: Only about 0.3% of all V1-V2 pairs have a significant narrow CCG peak (296 of 83,441).\n  source: Results, V1-V2 Recordings, paragraph 5\n  quote: In total, 0.3% of V1-V2 pairs had a significant narrow peak (n = 296 out of 83,441 pairs)\n  expected:\n  - quantity: fraction of V1-V2 pairs with a significant narrow peak, as printed\n    value: 0.003\n    tolerance: 0.0003\n  - quantity: fraction of V1-V2 pairs with a significant narrow peak, from the counts\n    value: 0.00355\n    tolerance: 0.000355\n  criterion: All V1-V2 pairs, 5 SD rule (shared CCG method). The printed 0.3% and the counts\n    (0.355%) disagree; reproduced when the fraction is within tolerance of either.\n- id: fig5b-v1v2-latency\n  statement: Narrow V1-V2 CCG peaks are offset from zero lag by a median of 2.8 ms, significantly\n    different from zero, with a mean peak width of 3.71 ms, consistent with direct V1 to V2 input.\n  source: Results, V1-V2 Recordings, paragraph 6; Figure 5B, gray\n  quote: Narrow peaks were offset from zero time lag by a median of 2.8 ms (Figure 5B, gray; p <\n    0.001 for difference with 0), with an average peak width of 3.71 ± 0.05 ms (SEM)\n  statistics:\n  - about: median peak offset against zero\n    p: 0.001\n    p_relation: \"<\"\n    n: 296 V1-V2 pairs with a significant narrow peak\n  expected:\n  - quantity: median peak offset of significant V1-V2 narrow peaks\n    value: 2.8\n    tolerance: 0.28\n    unit: ms\n  - quantity: mean peak width of significant V1-V2 narrow peaks\n    value: 3.71\n    tolerance: 0.1\n    unit: ms\n  depends_on:\n  - fig5-narrow-pairs-rare\n  criterion: Significant pairs as in fig5-narrow-pairs-rare; offset is the lag of the maximum of\n    the smoothed jitter-corrected CCG within 10 ms of zero, positive for V2 after V1. The width\n    tolerance is twice the paper's SEM, about its 95% interval. Open, the test against zero,\n    which the paper does not name; readings (a) Wilcoxon signed-rank, (b) sign test, both\n    two-sided. Open, the width measure, which the paper does not define; readings (a) full width\n    at half the peak height of the smoothed jitter-corrected CCG, (b) the same on the unsmoothed\n    CCG. Reproduced when the test gives p < 0.001 and the median offset is within tolerance;\n    the width is judged under either reading.\n- id: fig5b-intra-areal-zero-lag\n  statement: Significant narrow peaks of V1-V1 and V2-V2 jitter-corrected CCGs have a median offset\n    of 0.0 ms, not different from zero.\n  source: Results, V1-V2 Recordings, paragraph 6; Figure 5B, blue and red\n  quote: significant peaks in V1-V1 (Figure 5B; blue, n = 2845) and V2-V2 (red, n = 368)\n    jitter-corrected CCGs had a median offset of 0.0 ms (p = 0.45 and 0.42, respectively, for\n    difference from zero)\n  statistics:\n  - about: V1-V1 median offset against zero\n    p: 0.45\n    n: 2845 V1-V1 pairs\n  - about: V2-V2 median offset against zero\n    p: 0.42\n    n: 368 V2-V2 pairs\n  criterion: A claim of absence. Pairs within each area with a significant narrow peak (shared CCG\n    method, 5 SD rule). The lag sign is arbitrary within an area; the pair order is the order of\n    the unit lists, a standard choice. The paper does not name its test; readings (a) Wilcoxon\n    signed-rank, (b) sign test, two-sided at p < 0.05. Reproduced when the test finds no\n    difference from zero in both areas; the medians are reported either way.\n- id: figs3-efficacy\n  statement: For significant V1-V2 pairs with peak offsets above 1 ms, the median efficacy (CCG\n    integral within 2.5 ms of the peak) is 0.39%, mean 0.69%.\n  source: Figure S3A; Supplemental Figure 3 text, Amplitude\n  quote: In the analyzed pairs, the median efficacy was 0.39% (Figure S3A, mean 0.69 ± 0.06%)\n  expected:\n  - quantity: median efficacy, significant V1-V2 pairs with offset above 1 ms\n    value: 0.39\n    tolerance: 0.039\n    unit: percent\n  - quantity: mean efficacy, same pairs\n    value: 0.69\n    tolerance: 0.12\n    unit: percent\n  depends_on:\n  - fig5b-v1v2-latency\n  criterion: Efficacy is the integral of the V1-rate-normalized CCG within 2.5 ms of the peak\n    (Supplemental Figure 3, Amplitude), in pairs with peak offset above 1 ms (255 in the paper).\n    The mean tolerance is twice the paper's SEM. Open, whether the integral is over the\n    jitter-corrected CCG (reading a, the one whose peak defines significance) or the raw CCG\n    (reading b).\n- id: fig6a-coordination-before-v2\n  statement: In epochs 1.5 to 3.5 ms before spikes of middle-layer V2 neurons, V1 divergence is\n    significantly higher than in control epochs at every jitter window from 5 to 1280 ms.\n  source: Results, V2 Spiking Is Preceded by Stronger V1 Coordination, paragraphs 2 and 3; Figure 6A\n  quote: The divergence values in control epochs (blue) were significantly smaller than in epochs\n    preceding V2 spiking (red; p = 0.011 for jitter window of 5 ms; p < 0.001 for all other jitter\n    windows)\n  statistics:\n  - about: jitter window 5 ms\n    test: bootstrap over V2 neurons\n    p: 0.011\n    n: 226 middle-layer V2 neurons, 3,846,629 epochs\n  - about: jitter windows 10 to 1280 ms\n    test: bootstrap over V2 neurons\n    p: 0.001\n    p_relation: \"<\"\n    n: 226 middle-layer V2 neurons, 3,846,629 epochs\n  depends_on:\n  - fig4c-narrow-peak-sites\n  criterion: Shared divergence method, V2 neurons at middle-layer sites, epochs 1.5 to 3.5 ms\n    before each spike, against control epochs. Reproduced when the spike divergence exceeds the\n    control divergence with p < 0.05 at all six windows; partially reproduced at four or five;\n    not reproduced otherwise. Every reading of the shared method is run.\n- id: fig7a-threefold\n  statement: For jitter windows of 5 to 80 ms, divergence before middle-layer V2 spikes is roughly\n    3-fold that of control epochs.\n  source: Results, V2 Spiking Is Preceded by Stronger V1 Coordination, paragraph 4; Figure 7A\n  quote: Divergence values for epochs associated with V2 spiking were roughly 3-fold greater than\n    in control epochs\n  expected:\n  - quantity: ratio of spike-epoch to control-epoch divergence, jitter windows 5 to 80 ms\n    value: 3\n    tolerance: 1\n  depends_on:\n  - fig6a-coordination-before-v2\n  criterion: Ratio of the divergence values of fig6a-coordination-before-v2 at 5, 10, 20, 40 and 80\n    ms. The tolerance is wider than 10% because the paper says \"roughly\" and reads it off a log\n    axis. Open, how the ratio is summarized across windows; readings (a) the geometric mean of\n    the five ratios, (b) the median of the five, (c) each window separately, reproduced when at\n    least four of five are within tolerance.\n- id: fig7a-above-shuffle\n  statement: Divergence both before middle-layer V2 spikes and in control epochs is significantly\n    larger than divergence of shuffled data, so V1 activity is coordinated also in control epochs.\n  source: Results, V2 Spiking Is Preceded by Stronger V1 Coordination, paragraph 4; Figure 7A, black\n  quote: Note that both for epochs preceding V2 spiking and for control epochs, the divergence\n    values were significantly larger than those obtained from shuffled data (Figure 7A, black)\n  depends_on:\n  - fig6a-coordination-before-v2\n  criterion: Shuffled data remove correlations (Results, same paragraph); the paper does not say\n    how. Readings (a) each V1 neuron's trials permuted independently among trials of the same\n    orientation, (b) among all trials. Divergence of shuffled data against their own jitter\n    surrogate, in the spike-triggered epochs. Reproduced when, for jitter windows 5 to 80 ms, the\n    lower 95% bootstrap bound of both spike and control divergence is above the shuffled value\n    at a majority of windows.\n- id: fig6b-not-after-v2\n  statement: In epochs 1.5 to 3.5 ms after middle-layer V2 spikes, V1 divergence does not differ\n    from control epochs for jitter windows of 5 to 80 ms.\n  source: Results, V2 Spiking Is Preceded by Stronger V1 Coordination, paragraph 3; Figure 6B\n  quote: In epochs 1.5–3.5 ms after the occurrence of a V2 spike, there was no difference in\n    divergence with control epochs, for jitter windows between 5 and 80 ms (Figure 6B; p > 0.18 for\n    all comparisons)\n  statistics:\n  - test: bootstrap over V2 neurons\n    p: 0.18\n    p_relation: \">\"\n    n: 226 middle-layer V2 neurons\n  depends_on:\n  - fig6a-coordination-before-v2\n  criterion: A claim of absence, judged on the paper's bootstrap comparison (shared divergence\n    method, readings p-a and p-b) at 5, 10, 20, 40 and 80 ms, at p < 0.05. Reproduced when no\n    window shows a significant difference; not reproduced when any does. Differences and p-values\n    are reported for every window.\n- id: fig6-slow-both-sides\n  statement: At a jitter window of 1280 ms, V1 divergence is elevated both before and after\n    middle-layer V2 spikes.\n  source: Results, V2 Spiking Is Preceded by Stronger V1 Coordination, paragraph 3; Figure 6A and\n    6B, bottom rows\n  quote: For larger jitter windows, there was enhanced divergence both before and after V2 spiking,\n    as illustrated for a jitter window of 1280 ms (red compared to blue; bottom row of Figures 6A\n    and 6B; p < 0.001 for both cases)\n  statistics:\n  - test: bootstrap over V2 neurons\n    p: 0.001\n    p_relation: \"<\"\n    n: 226 middle-layer V2 neurons\n  depends_on:\n  - fig6a-coordination-before-v2\n  criterion: Shared divergence method, 1280 ms window, epochs 1.5 to 3.5 ms before and after each\n    spike, each against control epochs. Reproduced when both are higher than control at p < 0.05;\n    partially reproduced when one is.\n- id: fig7d-time-course\n  statement: Enhanced V1 coordination is evident several milliseconds before middle-layer V2\n    spikes, but not in more distant epochs or after V2 spikes.\n  source: Results, V2 Spiking Is Preceded by Stronger V1 Coordination, paragraph 5; Figure 7D\n  quote: Enhanced V1 coordination was evident several milliseconds before V2 spiking, but not in\n    more temporally distant epochs or in epochs following V2 activity\n  depends_on:\n  - fig6a-coordination-before-v2\n  criterion: Difference in divergence (spike minus control) for jitter windows 5 to 80 ms over\n    temporal offsets within 15 ms of the V2 spike (Figure 7D axis; Divergence Analysis, \"±15 ms\").\n    Open, the offset steps, which the paper does not give; readings (a) 2 ms epochs stepped by 1\n    ms, (b) 1 ms bins. Reproduced when, for at least four of the five windows, the largest\n    difference is at an offset between 1 and 6 ms before the V2 spike, and no epoch after the\n    spike nor any epoch more than 8 ms before it has a difference above control at p < 0.05\n    (bootstrap, shared method). Partially reproduced when the peak is before the spike in at\n    least four windows but some after or distant epochs are significant.\n- id: fig7b-nonmiddle-no-coordination\n  statement: Before spikes of V2 neurons in layers superficial or deep to the middle layers, V1\n    divergence does not differ from control epochs, apart from the 80 ms jitter window.\n  source: Results, V2 Spiking Is Preceded by Stronger V1 Coordination, paragraph 6; Figure 7B\n  quote: In epochs 1.5–3.5 ms before V2 spikes in these layers, divergence was not significantly\n    different from that measured in control epochs (Figure 7B; p = 0.008 for jitter window of 80\n    ms; p > 0.15 for other windows)\n  statistics:\n  - about: jitter window 80 ms\n    test: bootstrap over V2 neurons\n    p: 0.008\n    n: 236 non-middle-layer V2 neurons, 2,398,161 epochs\n  - about: jitter windows 5 to 40 ms\n    test: bootstrap over V2 neurons\n    p: 0.15\n    p_relation: \">\"\n    n: 236 non-middle-layer V2 neurons, 2,398,161 epochs\n  depends_on:\n  - fig4c-narrow-peak-sites\n  criterion: A claim of absence, on the paper's bootstrap comparison (shared method) at 5, 10, 20\n    and 40 ms, p < 0.05, for V2 neurons at sites superficial to or deeper than the middle-layer\n    sites of their penetration. Reproduced when none of the four windows differs; not reproduced\n    when any does. The 80 ms result is reported, and the size of every difference. Needs the\n    depth order of sites within a penetration.\n- id: fig7e-nonmiddle-time-course\n  statement: Across temporal offsets around non-middle-layer V2 spikes, the difference in V1\n    divergence from control is minimal.\n  source: Results, V2 Spiking Is Preceded by Stronger V1 Coordination, paragraph 6; Figure 7E\n  quote: We explored a range of temporal offsets relative to the V2 spikes, but the difference in\n    divergence between epochs around the time of V2 spikes and control epochs was minimal (Figure\n    7E)\n  depends_on:\n  - fig7b-nonmiddle-no-coordination\n  - fig7d-time-course\n  criterion: As fig7d-time-course, for non-middle-layer neurons. Reproduced when, at jitter windows\n    5 to 40 ms, the largest difference over offsets is below half the largest difference of the\n    middle-layer neurons at the same window, for at least three of the four windows.\n- id: fig7c-offset-rf-no-coordination\n  statement: Before spikes of V2 neurons at middle-layer depths whose RFs are offset by at least 3\n    deg from the V1 population, V1 divergence does not differ from control.\n  source: Results, V2 Spiking Is Preceded by Stronger V1 Coordination, paragraph 7; Figure 7C and 7F\n  quote: We found no difference in divergence in epochs associated with spiking of these V2\n    neurons, compared to control epochs (Figures 7C and 7F; p > 0.2 for all comparisons)\n  statistics:\n  - test: bootstrap over V2 neurons\n    p: 0.2\n    p_relation: \">\"\n    n: 80 V2 neurons, 1,382,605 epochs\n  criterion: A claim of absence, on the paper's bootstrap comparison (shared method) at 5 to 80 ms,\n    p < 0.05, for offset-RF neurons as the header defines them. Reproduced when no window differs;\n    not reproduced when any does. Needs depth on the layer 6/WM reference and RF positions in\n    degrees (see fig5a-rf-alignment); if the data set has no such neurons the claim cannot be\n    tested.\n- id: figs2a-v2-single-units\n  statement: Using only well-isolated V2 single units (SNR of 3 or more) in the middle layers,\n    divergence is still elevated before V2 spikes for most jitter windows.\n  source: Figure S2A; Supplemental Figure 2 text, paragraph 2\n  quote: divergence was significantly elevated in epochs preceding V2 spiking, relative to control\n    epochs, for most jitter windows (p=0.3 for 5 ms jitter window; p=0.08 for 10 ms; p<0.01 for all\n    other comparisons)\n  statistics:\n  - about: jitter window 5 ms\n    p: 0.3\n    n: 43 middle-layer V2 single units\n  - about: jitter window 10 ms\n    p: 0.08\n    n: 43 middle-layer V2 single units\n  - about: jitter windows 20 to 80 ms\n    p: 0.01\n    p_relation: \"<\"\n    n: 43 middle-layer V2 single units\n  depends_on:\n  - fig6a-coordination-before-v2\n  criterion: As fig6a-coordination-before-v2, with V2 neurons restricted to SNR of 3 or more\n    (waveform amplitude over SD of waveform noise). Reproduced when 20, 40 and 80 ms are\n    significant at p < 0.05. Needs unit SNR or waveforms.\n- id: figs2b-v1-single-units\n  statement: Using only V1 single units (SNR of 3 or more), V1 divergence is elevated before\n    middle-layer V2 spikes at every jitter window, and not before non-middle-layer or offset-RF\n    V2 spikes.\n  source: Figure S2B; Supplemental Figure 2 text, paragraph 3\n  quote: Divergence is elevated in a population of V1 single units before spiking in the middle\n    layers of V2 (p<0.001 for all jitter windows). V1 divergence is not elevated before spiking in\n    the superficial or deep layers of V2, or before spiking at offset V2 sites\n  statistics:\n  - about: middle-layer V2, all jitter windows\n    p: 0.001\n    p_relation: \"<\"\n    n: V1 populations of 19.7 ± 1.1 single units\n  depends_on:\n  - fig6a-coordination-before-v2\n  - fig7b-nonmiddle-no-coordination\n  criterion: As fig6a-coordination-before-v2 and fig7b-nonmiddle-no-coordination, with V1 units\n    restricted to SNR of 3 or more. Reproduced when the middle-layer comparison is significant at\n    p < 0.05 at all of 5 to 80 ms and the non-middle comparison at none of them; partially\n    reproduced when only the first holds. Needs unit SNR or waveforms.\n- id: figs4-partner-not-needed\n  statement: V1 coordination is elevated before spikes of middle-layer V2 neurons both with and\n    without a significant CCG peak with a recorded V1 neuron, slightly more for those with one.\n  source: Figure S4; Supplemental Figure 4 text, paragraph 3; Results, Dissociation of Divergence\n    Analysis, paragraph 3\n  quote: Figure S4 shows that coordination in V1 was elevated in epochs preceding either subset of\n    V2 cells, evident as higher divergence values associated with V2 spiking than in the\n    corresponding control epochs. The increase in divergence was slightly stronger, when based on\n    V2 neurons with a V1 partner\n  depends_on:\n  - fig6a-coordination-before-v2\n  - fig5-narrow-pairs-rare\n  criterion: Middle-layer V2 neurons split by whether any pair with a recorded V1 neuron passes the\n    5 SD rule (73 with and 153 without in the paper). Shared divergence method at 5 to 80 ms.\n    Reproduced when, in each subset, spike divergence exceeds control at p < 0.05 at a majority\n    of windows; the ratio of spike to control divergence of the two subsets is reported.\n- id: figs5-middle-layer-relay\n  statement: V2 middle-layer divergence is higher before spikes in superficial and deep V2 layers\n    than in control epochs for jitter windows above 10 ms, and also higher after them.\n  source: Figure S5A and S5B; Supplemental Figure 5 text, paragraph 2\n  quote: The elevation in divergence was significant for all jitter windows greater than 10 ms\n    (p=0.02 for jitter window of 20 ms; p=0.009 for 40 ms; p<0.001 for 80 ms)\n  statistics:\n  - about: before superficial or deep spikes, 20 ms window\n    p: 0.02\n  - about: before, 40 ms window\n    p: 0.009\n  - about: before, 80 ms window\n    p: 0.001\n    p_relation: \"<\"\n  - about: after, 5 ms window\n    p: 0.03\n  - about: after, 10 ms window\n    p: 0.007\n  - about: after, 20 to 80 ms windows\n    p: 0.001\n    p_relation: \"<\"\n  depends_on:\n  - fig4c-narrow-peak-sites\n  criterion: Shared divergence method with the middle-layer V2 units (11.5 ± 0.6 cells per\n    population in the paper) as the population and spikes of superficial and deep V2 units, pooled,\n    as triggers. The epoch is printed \"0.5±1 ms\" before the spike, which the text leaves unclear;\n    readings (a) 0.5 to 1 ms before, (b) a 2 ms epoch from 1.5 ms before to 0.5 ms after, (c) 1.5\n    to 3.5 ms before as in the main analysis. Reproduced when divergence before is above control at\n    p < 0.05 at 20, 40 and 80 ms and divergence after is above control at a majority of 5 to 80 ms.\n- id: fig1-ffn-propagation\n  statement: In a ten-layer feedforward network of integrate-and-fire neurons, spike packets\n    propagate to the deepest layer with high convergence but not with low convergence, where\n    downstream spiking beyond layers 2 or 3 is not associated with heightened layer 1 divergence.\n  source: Results, paragraphs 2 and 6; Figure 1A and 1B\n  quote: Thus, beyond layers 2 or 3, downstream spiking is not associated with heightened\n    coordination in layer 1, indicating a failure of spike packets to propagate\n  criterion: A simulation, not a test on the recordings, and no code is published. Rerun from\n    Simulations and the Supplemental Experimental Procedures (100 cells per layer, 20,000 Poisson\n    inputs, convergence 40, 70 and 100, packets of SD 2.5 ms at 2 Hz). Reproduced when the layer 1\n    divergence before layer 10 spikes is above the all-epoch value at convergence 100 and within\n    the all-epoch value's range at convergence 40.\n- id: fig3-divergence-correlation\n  statement: In synthetic populations of 100 neurons, divergence rises about 3-fold when pairwise\n    correlation goes from 0.1 to 0.2 and falls 3-fold from 0.1 to 0.05, and is insensitive to firing\n    rate.\n  source: Results, paragraphs 7 and 8; Figure 3A and 3B\n  quote: Increasing correlations from 0.1 (Figure 3A, green) to 0.2 (red) caused a roughly 3-fold\n    increase in divergence; reducing correlations from 0.1 to 0.05 (blue) caused a 3-fold decrease\n    in divergence\n  criterion: A simulation, not a test on the recordings, and no code is published (Figure S6\n    describes the generator). Rerun as described; reproduced when both ratios are between 2 and 4\n    at a majority of jitter windows from 5 to 1280 ms and divergence at 1.25 and 80 sp/s differs by\n    less than 2-fold at a correlation of 0.1.\n- id: figs1-higher-order\n  statement: With pairwise correlations fixed, divergence rises monotonically with the order of\n    the coordinated patterns.\n  source: Figure S1C; Supplemental Figure 1 text, paragraph 3\n  quote: Divergence values rose monotonically with pattern complexity (Figure S1C)\n  criterion: A simulation, not a test on the recordings, and no code is published. Rerun as the\n    Figure S1 text describes (100 Poisson cells at 20 Hz, added patterns of 2 to 10 cells, CCG peak\n    0.002 coinc/spk, 10 ms jitter window); reproduced when divergence increases with each step of\n    pattern complexity.\n- id: fig8-architecture\n  statement: In a model V2 neuron, V1 coordination is elevated before V2 spikes with excitatory\n    correlated input, not when the correlated input mixes excitation and inhibition (though a CCG\n    peak remains), and is elevated when the sampled V1 neurons do not project to the V2 cell (with\n    no CCG peak).\n  source: Results, Dissociation of Divergence Analysis, paragraphs 2 to 4; Figure 8\n  quote: Together these three simulations illustrate that the presence of significant pairwise\n    timing correlations (i.e., a significant interareal CCG peak) is neither necessary nor\n    sufficient for determining whether downstream spiking is related to the strength of\n    coordination in the input population\n  criterion: A simulation, not a test on the recordings, and no code is published. Rerun from the\n    Supplemental Experimental Procedures, Figure 8 (1,500 excitatory and 1,140 inhibitory inputs at\n    20 sp/s, a pool of 500 correlated V1 cells at correlation 0.1, 400 trials of 1280 ms, 100 V2\n    cells per scenario). Reproduced when the three scenarios give the pattern of the statement,\n    judged by non-overlapping 95% bootstrap intervals at a majority of jitter windows 5 to 80 ms.\n- id: rf-sizes\n  statement: Mean RF diameter is 1.21 deg in V1 and 2.27 deg in V2.\n  source: Results, V1-V2 Recordings, paragraph 2\n  quote: mean diameter of 1.21�± 0.01�(SEM) for V1 and 2.27�± 0.05�for V2\n  expected:\n  - quantity: mean V1 RF diameter\n    value: 1.21\n    tolerance: 0.121\n    unit: deg\n  - quantity: mean V2 RF diameter\n    value: 2.27\n    tolerance: 0.227\n    unit: deg\n  criterion: Diameter as plus and minus 2 SD of the 2D Gaussian fit (Visual Stimuli). The SEMs\n    (0.01 and 0.05 deg) describe the paper's sample; the tolerance is 10%, since the data set is a\n    subset of sessions with its own stimulus sizes. Open, how the two SDs of an elliptical fit make\n    one diameter; readings (a) 4 times the square root of the mean of the two variances, (b) 4\n    times the geometric mean of the two SDs. The pixel-to-degree scale is open as in\n    fig5a-rf-alignment.\n"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
python tools/claims_check.py claims/zandvakili-2015.yaml paper/10.1016-j.neuron.2015.07.026.txt; grep -n -i "rather\|—" claims/zandvakili-2015.yaml; python - <<'E'
import yaml
d=yaml.safe_load(open('claims/zandvakili-2015.yaml'))
def walk(x,path=''):
    if isinstance(x,dict):
        for k,v in x.items(): walk(v,path+'/'+str(k))
    elif isinstance(x,list):
        for i,v in enumerate(x): walk(v,path+f'[{i}]')
    elif isinstance(x,str) and ': ' in x: print(path)
walk(d); print(len(d['claims']))
E
grep -n '": \|^  [a-z_]*: "' claims/zandvakili-2015.yaml | head
```

Result: not kept, because it reads the paper's text.

**Agent**

I wrote `claims/zandvakili-2015.yaml`. The quote checker passes it: 26 claims, 26 quotes, 20 statistical values, 0 problems. It contains no em dashes, no "rather", and no ": " inside plain scalars. Nothing was committed.

**Text read:** the version of record (PyMuPDF text of the journal PDF) with its full Supplemental Information appended: Figures S1 to S6 and the Supplemental Experimental Procedures. The full text, Methods and supplement were all there. The paper links no analysis code, so none was read. I could not render PDF pages here (`pdftoppm` and `fitz` are not installed), so every value comes from the text and no figure was read from its image.

**Claims:** 26, all with quotes and none `inferred`; all 26 have a criterion.
- 10 claims carry statistics: the narrow V1-V2 peak delay, the V1-V1 and V2-V2 zero offsets, the four Figure 6 and 7 divergence comparisons, and Figures S2A, S2B and S5.
- 8 claims carry expected values: the fraction of sites with a narrow peak, their depth, the RF-alignment probability, the fraction of pairs, delay and width, efficacy, the 3-fold ratio, and RF sizes.
- 4 claims are simulations (Figures 1, 3, 8 and S1). No code is published for them, so they would have to be re-simulated from the Methods; they are not tests on the recordings.

**Details the paper leaves open, with the readings named:**
- **CCG jitter window:** 10 ms, the only value given (for Fig. 4C), or another window.
- **Divergence epoch:** two 1-ms bins between 1.5 and 3.5 ms before the spike, or one bin centred 2.5 ms before it.
- **Jitter and control trials:** drawn from trials of the same orientation, or from all trials.
- **Jitter surrogate:** one jitter realization, or the mean of several.
- **Bootstrap p-value:** paired resampling, or two independent bootstrap distributions.
- **Shuffle for Fig. 7A:** within orientation, or across all trials.
- **Test of peak offset against zero (Fig. 5B, both claims):** Wilcoxon signed-rank or sign test.
- **Peak width:** full width at half height on the smoothed or the raw CCG.
- **Efficacy integral (Fig. S3):** on the jitter-corrected or the raw CCG.
- **Summary of the "roughly 3-fold" ratio:** geometric mean, median, or each window separately. Its tolerance is widened to ±1, with the reason given.
- **Time-course offset steps (Fig. 7D):** 2-ms epochs stepped by 1 ms, or 1-ms bins.
- **Broad-peak test (Fig. 4C):** none is given; one is fixed in the criterion, with two readings named.
- **Fig. S5 epoch:** printed "0.5±1 ms"; read as 0.5 to 1 ms before, a 2-ms epoch around the spike, or 1.5 to 3.5 ms before.
- **RF diameter of an elliptical fit:** two readings.
- **Printed 0.3% against counts of 296/83,441 (0.355%):** the claim holds if the result is within tolerance of either.

**Missing from the paper that some claims need:**
- **Pixels per degree:** the paper gives 1024 × 768 at 110 cm but no screen size. This affects the RF-offset bins, the 3° offset group and the RF sizes.
- **Depth and laminar order:** the depth claim, the non-middle-layer claims and the offset-RF claims need site depth relative to the layer 6/white matter border and the order of sites within a penetration.
- **Unit SNR:** the Fig. S2 single-unit claims need it.

The paper does not report any of these. Whether the dataset holds the depth and SNR data is for the author to find.

The paper's counts (896 V2 cells, 223 sites, 83,441 pairs, the epoch totals) come from 7 monkeys. The dataset holds 5 sessions in 3 animals, so the criteria compare proportions and medians and report the counts beside them.

## End of run

20 turns, 4 minutes, $1.49 at API prices, result: success.
