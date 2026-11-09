# 001678 · claims · run 39611549349

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cat docs/protocol.md | sed -n '/## Reader/,/^## [A-Z]/p' | head -300; ls claims/001678 claims/001453 paper/ 2>&1
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cat claims/001453/*.yaml | head -150; wc -c paper/*; head -30 paper/10.1162-imag.a.1066.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
head -c 9000 claims/001453/*.yaml | sed -n '28,200p'; echo ----; grep -n "^- id\|^  [a-z_]*:" claims/001453/*.yaml | awk -F: '{print $3}' | sort | uniq -c; wc -c paper/*; head -30 paper/10.1162-imag.a.1066.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
wc -c paper/*; head -40 paper/10.1162-imag.a.1066.txt | cut -c1-400
```

Result: not kept, because it reads the paper's text.

**Agent**

Let me read the whole text.

**Agent calls Bash**

```bash
grep -n "" paper/10.1162-imag.a.1066.txt | awk -F: 'length($0)>0' | cut -c1-120 | grep -v "^\[0-9]*:\[[0-9]*\]" | awk 'NR<400' | grep -nv "^[0-9]*:\[[0-9]" | head -200
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
awk 'NR>=12 && NR<=274 {print NR": "length($0)": "substr($0,1,80)}' paper/10.1162-imag.a.1066.txt | awk -F': ' '$2>0' | head -60; wc -l paper/10.1162-imag.a.1066.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
awk '{print NR": "length($0)}' paper/10.1162-imag.a.1066.txt | sort -t: -k2 -n -r | head; awk 'NR>=130 && NR<=274' paper/10.1162-imag.a.1066.txt | cut -c1-150 | grep -v '^$' | tail -70
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -n 7p paper/10.1162-imag.a.1066.txt | fold -s -w 200 > $TMPDIR/main.txt; wc -l $TMPDIR/main.txt; head -c 30000 $TMPDIR/main.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/main.txt",
 "limit": 160,
 "offset": 10
}
```

```
10	patient responses. Optimization of this treatment requires understanding the dependence of neuronal responses on ACS parameters. We sought to characterize neuronal responses across varying ACS 
11	frequencies and amplitudes and assess the extent to which changes in neuronal activity persist beyond the cessation of the stimulation, thereby informing ACS optimization pathways and evaluating the 
12	potential for sustained neuromodulation. We delivered subcutaneous ACS while recording intracortical electrophysiological activity in adult rats. We applied ACS for 1 or 20 minutes and analyzed 
13	ensuing spiking activity, power spectra, and low-frequency to high-frequency phase–amplitude coupling (LF-HF PAC). Both durations of ACS elicited a modulation of firing patterns (either in rate or 
14	entrainment) in most neurons, in a stimulation frequency- and amplitude-dependent manner. Changes in firing rate were more frequent, albeit modest, whereas changes in entrainment were rarer, but 
15	pronounced. Increasing ACS amplitude or frequency increased the degree of entrainment. Further, entrainment changes persisted beyond the 20-minute ACS, at half their online level. Neuronal power and 
16	LF-HF PAC increased proximal to excited, but decreased near suppressed neurons. Neuronal entrainment was observed alongside decreased power and LF-HF PAC. The prominent entrainment response to 
17	prolonged high-frequency ACS observed here supports the potential of ACS for facilitating signal integration and promoting functional reorganization via spike timing-dependent plasticity. In turn, we 
18	found broader temporal windows of excitation under low ACS frequencies engendered greater variability in spike timing, which may be utilized to reduce hypersynchronous or task-irrelevant activity. 
19	transcranial alternating current stimulation neuromodulation in situ electrophysiology Canadian Institutes of Health Research (CIHR) http://dx.doi.org/10.13039/501100000024 PJT173409 National 
2
[... 149 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/main.txt",
 "offset": 169,
 "limit": 170
}
```

```
169	30–80 Hz), and increasing stimulation amplitudes were investigated (50, 100, 200, 400 μA, or 22.2, 44.4, 88.8, and 177.6 A/m 2 ). The magnitude of electric fields was assessed from sACS artifacts in 
170	electrophysiological recordings, and had medians of 0.77 ± 0.29, 1.42 ± 0.60, 2.86 ± 1.20, and 6.04 ± 1.68 mV/mm for 50, 100, 200, 400 μA sACS amplitudes, respectively ( Fig. 1C ). Finite element 
171	modeling (FEM) using Sim4Life software was used to estimate and visualize electric fields produced across the brain across stimulation amplitudes ( Fig. 2 ). Within the model, the electric field 
172	dropped to ~50% of the intensity measured at the recording electrodes at a further ~70 µm in depth. The cerebral electric field root mean square (RMS) values were fitted with log-normal 
173	distributions, with shape, location, and scale parameters of 1.28, 8.54E-03, 2.17E-01 for 50 µA; 1.28, 1.57E-02, 4.00E-01 for 100 µA; 1.28, 3.17E-02, 8.07E-01 for 200 µA; and 1.28, 6.70E-02, 1.70 for 
174	400 µA. Ellipsoids were fit to thresholded hemispheric volumes experiencing electric field magnitude of at least 1 mV/mm, with primary, secondary, and tertiary axes lengths of 7.37, 2.46, and 1.58 mm 
175	for 50-µA ACS; 7.37, 3.32, and 2.22 for 100-µA ACS; 7.86, 4.73, and 3.28 mm for 200-µA ACS; and 8.80, 6.57, and 4.35 mm for 400-µA ACS. Fig. 2. FEM electric field estimations. (A) Voxels of rat head 
176	used for FEM in Sim4Life software. A Boolean subtraction was used to remove experimentally resected areas of skin, muscle, and connective tissue around the skull. Stimulation electrodes with 
177	dimensions matching experimental conditions (1.5 × 1.5 mm) are displayed as blue squares. (B) RMS estimates of the electric field generated via FEM were normalized such that values in the simulation 
178	matched the experimentally measured values in the 2 × 2 mm grid space of the 4 × 4 MEA approximately 300 µm below the cortical surface. (C) Whole brain and orthogonal slice views of the 
[... 160 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/main.txt",
 "offset": 339,
 "limit": 280
}
```

```
File content (25080 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/main.txt",
 "offset": 339,
 "limit": 140
}
```

```
339	frequency–phase coupling (δ/θ), changes in FR were observed alongside a broader set of LF-HF PAC changes that included the coupling of higher frequency phases (i.e., α and β) to high-frequency 
340	amplitudes. Under propofol anesthesia without the delivery of electric stimulation, modulation indices averaged 1.17E-03 ± 1.11E-03, 3.88E-04 ± 3.86E-04, 3.90E-04 ± 3.48E-04, 2.04E-04 ± 1.87E-04, 
341	7.79E-05 ± 8.31E-05, 1.09E-04 ± 1.12E-04, 1.06E-05 ± 9.64E-06, and 3.78E-05 ± 3.05E-05 for δ to low-γ, δ to high-γ, θ to low-γ, θ to high-γ, α to low-γ, α to high-γ, β to low-γ, and β to high-γ band 
342	couplings, respectively, across 80-minute recordings. 4 Discussion Optimizing the ACS protocol in the clinic is difficult due to the limited sensitivity of non-invasive technologies for recording 
343	neuronal function. Furthermore, in silico simulations of neuronal responses to ACS, which are commonly used to fill the gaps in our understanding of neuromodulatory interventions effects, are 
344	confounded by the lack of ground truth experimental observations. The current study addressed this gap through a finely controlled experimental model study, leveraging intracortical multi-electrode 
345	arrays for high sensitivity recording of neuronal activity with controlled light sedation in co-housed littermates, to limit baseline variability. 4.1 sACS parameter exploration Neuronal responses in 
346	our experiments showed dose dependence, in line with prior work ( Johnson et al., 2020 ; Krause et al., 2022 ), with higher currents inducing more neurons to synchronize their firing to the 
347	stimulating waveform as well as increasing the degree of synchronization in their firing. A progressive suppression of firing rates was induced with increasing sACS frequency and amplitude. 
348	Alterations of FRs, largely within 2 Hz, were split between increases and decreases, in support of maintenance of the excitation/inhibition balance under external perturbations. The greater 
349	re
[... 129 more lines not kept]
```

**Agent**

Main text read. Now the supplement's structure.

**Agent calls Bash**

```bash
cd paper; awk 'NR>=275' 10.1162-imag.a.1066.txt | grep -n "=== page\|^S[0-9]\|Table\|Fig\|^Supplement" | head -120
```

```
3:=== page 1 ===
4:Supplemental  
5:S1 1-min sACS responses across frequency and amplitude 
258:=== page 2 ===
536:=== page 3 ===
546:Table S1.1. Pairwise comparisons of spike timing metrics before and after 1-min sACS.  
555:=== page 4 ===
719:Table S1.2. Linear regressions of the degree of change in spike timing metric across 
737:=== page 5 ===
902:Table S1.3 Linear regressions of the degree of change in spike timing metric across 
920:=== page 6 ===
1055:Table S1.4 Linear regressions of the percentage of neurons affected across frequencies.  
1083:=== page 7 ===
1220:Table S1.5 Linear regressions of the percentage of neurons affected across amplitudes.  
1229:=== page 8 ===
1459:=== page 9 ===
1613:Table S1.6. Anova summary table of linear mixed effects model of power before and after 1-min 
1625:=== page 10 ===
1844:=== page 11 ===
2010:Table S1.7. Anova summary table of linear mixed effects model of phase-amplitude coupling 
[... 30 more lines not kept]
```

**Agent calls Bash**

```bash
cd paper; awk 'NR>=275' 10.1162-imag.a.1066.txt > $TMPDIR/supp.txt; for r in 546,556 719,737 902,920 1055,1083 1220,1229 1613,1625 2010,2105 2437,2447 3037,3100 3197,3210; do sed -n "${r}p" $TMPDIR/supp.txt | tr '\n' ' '; echo; echo ====; done
```

```
Table S1.1. Pairwise comparisons of spike timing metrics before and after 1-min sACS.   For all stimulation frequencies and amplitudes tested, pairwise comparisons of the LMER were used  to report changes in spike timing metrics (changes in √|PPC| or FR); the effect size and 95%  confidence interval as well as the estimated marginal means, standard error of the estimated marginal  means, and p-value.         === page 4 === Spike  
====
Table S1.2. Linear regressions of the degree of change in spike timing metric across  frequencies.   For each stimulation amplitude and spike timing metric, the results from the linear regressions  performed across frequencies assessing changes in spike timing or frequency.                             === page 5 === 
====
Table S1.3 Linear regressions of the degree of change in spike timing metric across  amplitudes.   For each stimulation frequency and spike timing metric, the results from the linear regressions  performed across amplitudes assessing changes in spike timing or frequency.                             === page 6 === 
====
Table S1.4 Linear regressions of the percentage of neurons affected across frequencies.   For each stimulation amplitude and spike timing metric, the results from the linear regressions  performed across frequencies assessing the percentage of neurons affected.                                                   === page 7 === 
====
Table S1.5 Linear regressions of the percentage of neurons affected across amplitudes.   For each stimulation frequency and spike timing metric, the results from the linear regressions  performed across amplitudes assessing the percentage of neurons affected.             === page 8 === 
====
Table S1.6. Anova summary table of linear mixed effects model of power before and after 1-min  sACS conditions.   For local field potentials on electrode channels proximal to neurons which demonstrated significant  modulations in spike timing metrics (increase/decrease firing rate/entrain
[... 9 more lines not kept]
```

**Agent**

Paper and supplement are complete. Now the code the paper links.

**Agent calls Bash**

```bash
cd $TMPDIR && git clone -q https://github.com/m-bellvila/Parametrizing-alternating-current-stimulation-for-neuromodulation.git code 2>&1 | tail -3; cd code && git log -1 --format='%H %cd' && find . -path ./.git -prune -o -type f -print | head -80
```

```
3b89bf2245c21c660427edcac3ecdf8cda5e7845 Fri Dec 5 16:02:46 2025 -0500
./phaseextract.py
./nulldistribution.py
./concatdataforspikesorting.py
./README.md
./MUAartrem.m
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/code && wc -l * && cat README.md && cat nulldistribution.py phaseextract.py
```

```
85 MUAartrem.m
   23 README.md
   92 concatdataforspikesorting.py
  407 nulldistribution.py
  268 phaseextract.py
  875 total
This code was used in the data analysis for:

Monica Bell Vila, Margaret Koletar, Adrienne Dorr, Andrea Trevisiol, Maged Goubran, John G. Sled, Paolo Bazzigaluppi, Bojana Stefanovic; 
Parametrizing alternating current stimulation for neuromodulation. Imaging Neuroscience 2025; doi: https://doi.org/10.1162/IMAG.a.1066


MUA analysis:

First the sACS artefact was removed from MUA data using MUAartrem.m 

Data was concatenated for spike detection using concatdataforspikesorting.py 

After discarding overly channels or stimulation periods with incomplete artefact removal, data was submitted to SpyKING CIRCUS 

[... 679 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/code && cat MUAartrem.m concatdataforspikesorting.py
```

```
function MUAartrem(path)
% Note that this code requires the installation of the TDT MATLAB offline
% analysis tools: https://www.tdt.com/docs/sdk/offline-data-analysis/offline-data-matlab/
% as well as the ARtACS software, DOI: 10.5281/zenodo.596319
% https://github.com/agricolab/ARtACS

format long

%% Set up folder/file selection
selpath = path;

data = TDTbin2mat(selpath);


%% Extract needed data

Fs_MUA = double(data.streams.Wav2.fs); %sampling frequency for MUA channel
Fs_stim = double(data.streams.uS1r.fs); %sampling frequency of stimulation channel

MUAdata = double(data.streams.Wav2.data); %MUA data
[... 139 more lines not kept]
```

**Agent**

Now the dandiset's title and description (metadata only).

**Agent calls Bash**

```bash
curl -s https://api.dandiarchive.org/api/dandisets/001678/ | python -c "import json,sys; d=json.load(sys.stdin); print(json.dumps({k:d.get(k) for k in ['identifier','draft_version','most_recent_published_version']},indent=1))"; curl -s https://api.dandiarchive.org/api/dandisets/001678/versions/draft/info/ | python -c "import json,sys; d=json.load(sys.stdin)['metadata']; print(d.get('name')); print(d.get('description')); print(d.get('relatedResource')); print(d.get('assetsSummary',{}).get('variableMeasured'), d.get('assetsSummary',{}).get('numberOfSubjects'))"
```

Result: the fetched text is not kept.

**Agent**

Now the example file's format in detail.

**Agent calls Read**

```json
{
 "file_path": "claims/001453/10.1016-j.cub.2025.04.027.yaml",
 "limit": 140,
 "offset": 40
}
```

```
40	    every code the analysis uses (0 to 7, 9, 10, 11, 13 and 20) occurs in the dandiset, and the
41	    species' median speeds for the nine whole-field stimuli computed here are within 10% of the
42	    values printed in Fig1-S1.ipynb for at least 14 of the 18 species and stimulus pairs. It is
43	    partially reproduced for 9 to 13 pairs and not reproduced below 9. The fish cannot be
44	    matched one to one, as no identifier links the dandiset's subjects to the code's folders;
45	    the counts per species are compared instead. The sign of the zebrafish turning response
46	    to codes 9 and 11 is reported, as the code and the protocol file disagree on which of them
47	    is lateral right.
48	- id: fig1d-dc-faster-all-codes
49	  statement: Danionella cerebrum (DC) swim at a higher median velocity than zebrafish (ZF)
50	    across the visual stimuli.
51	  source: Results, Larval DC exhibit higher average swimming speeds, paragraph 1; Figure 1D
52	  quote: DC show a significantly higher median velocity across all stimuli than ZF
53	  statistics:
54	  - test: two-way ANOVA, main species effect
55	    p: 0.05
56	    p_relation: "<"
57	  criterion: Tested without stimulus names, over all 21 stimulus codes. For each fish and code
58	    the median over trials of the trial speed in pixels per second; a two-way ANOVA (type II)
59	    of these values on species, code and their interaction. Reproduced when the species effect
[... 120 more lines not kept]
```

**Agent calls Bash**

```bash
grep -oE "^ *-? *[a-z_]+:" claims/001453/*.yaml | sed 's/^ *- */  /' | sort | uniq -c | sort -rn; sed -n 1,80p tools/claims_check.py; ls docs schemas 2>/dev/null
```

```
21   id:
     20   statement:
     20   source:
     19   quote:
     14     p:
     13   statistics:
     12   test:
     12     p_relation:
      9   criterion:
      9     n:
      8   data:
      7   depends_on:
      4   quantity:
      4     value:
      4     unit:
      4     tolerance:
      2   expected:
      2   about:
      2     test:
      1 schema_version:
[... 100 more lines not kept]
```

**Agent calls Bash**

```bash
python -c "
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
[... 185 more lines not kept]
```

**Agent calls Bash**

```bash
python -c "
import json;s=json.load(open('schemas/claims.schema.json'));print(json.dumps(s['\$defs'],indent=1))"
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

**Agent**

Let me read supplement tables S1.6, S1.7 and S3.1 (needed for absence claims).

**Agent calls Bash**

```bash
cd $TMPDIR; sed -n '1459,1625p' supp.txt | tr -s ' \n' ' ' | fold -w 200; echo; echo =====; sed -n '1844,2022p' supp.txt | tr -s ' \n' ' ' | fold -w 200; echo; echo ====; sed -n '3098,3300p' supp.txt | tr -s ' \n' ' ' | fold -w 200
```

```
=== page 9 === tp:amp 1.83E-24 1.83E-24 1 2.80E-23 1.00E+00 freqband:amp 2.67E+00 5.34E-01 5 8.16E+00 1.06E-07 tp:freq 3.97E-26 3.97E-26 1 6.07E-25 1.00E+00 freqband:freq 5.87E+00 1.17E+00 5 1.79E+01 
9.10E-18 amp:freq 1.24E+00 1.24E+00 1 1.90E+01 1.33E-05 tp:freqband:amp 1.58E-22 3.17E-23 5 4.84E-22 1.00E+00 tp:freqband:freq 1.82E-22 3.64E-23 5 5.57E-22 1.00E+00 tp:amp:freq 6.54E-25 6.54E-25 1 1.0
0E-23 1.00E+00 freqband:amp:freq 2.11E+00 4.23E-01 5 6.46E+00 5.26E-06 tp:freqband:amp:freq 1.38E-22 2.76E-23 5 4.22E-22 1.00E+00 FR decre ase tp 3.62E-22 3.62E-22 1 8.38E-21 1.00E+00 freqband 8.67E+0
3 1.73E+03 5 4.01E+04 0.00E+00 amp 5.94E+01 5.94E+01 1 1.38E+03 4.16E-300 freq 6.65E-01 6.65E-01 1 1.54E+01 8.80E-05 tp:freqband 4.17E-21 8.35E-22 5 1.93E-20 1.00E+00 tp:amp 3.58E-21 3.58E-21 1 8.29E-
20 1.00E+00 freqband:amp 9.63E+00 1.93E+00 5 4.46E+01 3.68E-46 tp:freq 1.13E-20 1.13E-20 1 2.62E-19 1.00E+00 freqband:freq 3.30E+00 6.61E-01 5 1.53E+01 4.63E-15 amp:freq 2.11E-01 2.11E-01 1 4.89E+00 2
.70E-02 tp:freqband:amp 5.00E-20 1.00E-20 5 2.31E-19 1.00E+00 tp:freqband:freq 2.66E-20 5.31E-21 5 1.23E-19 1.00E+00 tp:amp:freq 3.74E-22 3.74E-22 1 8.66E-21 1.00E+00 freqband:amp:freq 1.44E+00 2.89E-
01 5 6.69E+00 3.08E-06 tp:freqband:amp:freq 4.32E-21 8.64E-22 5 2.00E-20 1.00E+00 Table S1.6. Anova summary table of linear mixed effects model of power before and after 1-min sACS conditions. For loc
al field potentials on electrode channels proximal to neurons which demonstrated significant modulations in spike timing metrics (increase/decrease firing rate/entrainment), the anova summary table re
porting the influence of variables on the log power before and after 1-min of sACS. Variables included in the LMER were timepoint (‘tp’: baseline or post-sACS), frequency band (‘freqband’: θ, α, β, lo
w-γ, or high-γ), sACS amplitude (‘amp’: 50, 100, 200, or 400 μA), and sACS frequency (‘freq’: 5, 10, 20, or 40 Hz). === page 10 === 
=====
=== page 11 === freq 3.30E-01 3.30E-01 1 5.43E-01 4.
[... 17 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR; sed -n '1229,1300p' supp.txt | tr -s ' \n' ' ' | fold -w 200; echo; sed -n '1625,1680p' supp.txt | tr -s ' \n' ' ' | fold -w 200;echo; sed -n '2106,2160p' supp.txt | tr -s ' \n' ' ' | fold -w 200
```

```
=== page 8 === Spike timing metric Variable Sum Sq Mean Sq NumDF F value p √|PPC| increa se tp 8.99E-22 8.99E-22 1 1.70E-20 1.00E+00 freqband 1.61E+03 3.22E+02 5 6.10E+03 0.00E+00 amp 6.13E+00 6.13E+0
0 1 1.16E+02 5.07E-27 freq 2.31E+01 2.31E+01 1 4.38E+02 9.19E-97 tp:freqband 1.61E-21 3.22E-22 5 6.10E-21 1.00E+00 tp:amp 2.64E-21 2.64E-21 1 5.00E-20 1.00E+00 freqband:amp 9.61E+00 1.92E+00 5 3.64E+0
1 2.46E-37 tp:freq 1.25E-21 1.25E-21 1 2.37E-20 1.00E+00 freqband:freq 3.60E+01 7.19E+00 5 1.36E+02 8.24E-144 amp:freq 7.46E+00 7.46E+00 1 1.41E+02 
=== page 10 === Spike timing metric Variable Sum Sq Mean Sq NumDF F value p √|PPC| increa se tp 6.14E-02 6.14E-02 1 9.80E-02 7.54E-01 bandrel 3.73E+02 7.45E+01 5 1.19E+02 1.42E-123 amp 4.35E+00 4.35E+
00 1 6.94E+00 8.44E-03 freq 5.68E+00 5.68E+00 1 9.07E+00 2.60E-03 tp:bandrel 6.79E-02 1.36E-02 5 2.17E-02 1.00E+00 tp:amp 5.97E-02 5.97E-02 1 9.54E-02 7.57E-01 bandrel:amp 1.34E+01 2.67E+00 5 4.27E+00
 7.06E-04 
S2 20-min sACS responses Spike timing metric Frequen cy band Log power pre sACS Log power post sACS eff_size 95% CI emmean SE of emmean p Signif √|PPC| increase δ -14.71 ± 0.39 -15.12 ± 0.50 -5.45E-0 
1 1.04E-01 -1.22E-0 1 1.12E-02 1.07E-24 *** θ -15.44 ± 0.37 -15.94 ± 0.59 -6.77E-0 1 1.04E-01 -1.51E-0 1 1.12E-02 3.27E-37 *** α -15.88 ± 0.36 -15.94 ± 0.52
Shell cwd was reset to
```

**Agent**

Let me check supplementary regression tables S1.2 and S1.4 to see what they report (slope units, n).

**Agent calls Bash**

```bash
cd $TMPDIR; sed -n '555,640p' supp.txt | tr -s ' \n' ' ' | fold -w 200; echo; echo ===; sed -n '920,1060p' supp.txt | tr -s ' \n' ' ' | fold -w 200
```

```
=== page 4 === Spike timing metric Amplitude (μA) Slope (B1) Intercept (B0) R2 p SE Signif √|PPC| increase 50 -6.80E-04 3.10E-01 2.21E-03 7.95E-01 2.60E-03 100 -2.01E-03 3.33E-01 2.74E-02 3.57E-01 2.1
5E-03 200 2.16E-03 3.15E-01 1.68E-02 3.28E-01 2.19E-03 400 5.10E-03 2.88E-01 9.10E-02 2.29E-03 1.63E-03 ** √|PPC| decrease​ 50 -9.61E-04 -1.54E-01 1.68E-02 6.32E-01 1.96E-03 100 -1.60E-03 -1.38E-01 4.4
2E-02 4.71E-01 2.14E-03 200 -1.23E-03 -1.34E-01 6.51E-02 3.59E-01 1.30E-03 400 -1.74E-03 -6.09E-02 4.69E-01 4.17E-02 6.99E-04 FR increase​ 50 1.23E-03 9.14E-01 8.52E-04 8.51E-01 6.50E-03 100 3.65E-02 6
.32E-01 
===
=== page 6 === Spike timing metric Amplitude (μA) Slope (B1) Intercept (B0) R2 p SE Signif √|PPC| increase 50 -3.26E-05 5.91E-02 1.78E-05 9.80E-01 1.32E-03 100 1.27E-03 2.56E-02 5.27E-02 1.85E-01 9.40
E-04 200 2.24E-03 4.65E-02 5.18E-02 1.82E-01 1.64E-03 400 4.58E-03 9.42E-02 7.10E-02 1.62E-01 3.19E-03 √|PPC| decrease​ 50 -1.15E-03 4.77E-02 3.36E-02 2.85E-01 1.06E-03 100 -2.13E-04 2.19E-02 3.96E-03 
7.19E-01 5.87E-04 200 -5.81E-05 1.75E-02 4.54E-04 9.02E-01 4.68E-04 400 -7.37E-04 3.03E-02 6.58E-02 1.79E-01 5.35E-04 FR increase​ 50 -1.36E-03 1.05E-01 2.31E-02 3.76E-01 1.52E-03 100 -8.60E-04 1.28E-0
1 4.49E-03 7.02E-01 2.23E-03 200 -2.30E-03 1.05E-01 1.78E-01 1.05E-02 8.49E-04 * 400 -1.48E-03 1.47E-01 1.76E-02 4.93E-01 2.13E-03 FR decrease 50 1.18E-03 6.08E-01 5.26E-03 6.74E-01 2.77E-03 100 4.31E
-03 5.26E-01 5.90E-02 1.60E-01 2.99E-03 200 5.20E-03 5.14E-01 9.66E-02 6.50E-02 2.73E-03 400 2.91E-03 5.97E-01 4.76E-02 2.56E-01 2.51E-03 Table S1.4 Linear regressions of the percentage of neurons aff
ected across frequencies. For each stimulation amplitude and spike timing metric, the results from the linear regressions performed across frequencies assessing the percentage of neurons affected.
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR; sed -n '1083,1230p' supp.txt | tr -s ' \n' ' ' | fold -w 200; echo; sed -n '737,800p' supp.txt | tr -s ' \n' ' ' | fold -w 200
```

```
=== page 7 === Spike timing metric Frequency (Hz) Slope (B1) Intercept (B0) R2 p SE Signif √|PPC| increase 5 2.00E-04 8.53E-03 9.38E-02 8.29E-02 1.12E-04 10 1.68E-04 5.67E-02 3.66E-02 2.71E-01 1.50E-0
4 20 5.09E-04 1.67E-02 1.14E-01 5.48E-02 2.55E-04 40 6.04E-04 1.57E-02 2.01E-01 6.86E-03 2.10E-04 * √|PPC| decrease​ 5 7.36E-06 3.07E-02 2.01E-01 9.57E-01 1.36E-04 10 -3.77E-05 2.61E-02 2.01E-01 3.81E-
01 4.25E-05 20 -5.31E-05 2.64E-02 2.01E-01 4.26E-01 6.58E-05 40 1.34E-06 9.05E-03 2.01E-01 9.65E-01 3.02E-05 FR increase​ 5 1.04E-04 8.84E-02 2.53E-02 3.77E-01 1.16E-04 10 1.70E-04 8.46E-02 2.17E-02 3.
98E-01 1.99E-04 20 -1.29E-04 1.05E-01 7.98E-03 6.21E-01 2.58E-04 40 1.06E-04 4.23E-02 2.18E-02 3.97E-01 1.24E-04 FR decrease 5 8.78E-05 5.40E-01 2.38E-03 7.88E-01 3.23E-04 10 -4.69E-05 6.08E-01 9.32E-
04 8.62E-01 2.68E-04 20 1.62E-04 6.25E-01 8.55E-03 6.09E-01 3.13E-04 40 1.25E-04 6.63E-01 6.25E-03 6.52E-01 2.74E-04 Table S1.5 Linear regressions of the percentage of neurons affected across amplitud
es. For each stimulation frequency and spike timing metric, the results from the linear regressions performed across amplitudes assessing the percentage of neurons affected. === page 8 === Spike 
=== page 5 === Spike timing metric Frequency (Hz) Slope (B1) Intercept (B0) R2 p SE Signif √|PPC| increase 5 7.22E-04 1.32E-01 2.36E-01 4.12E-03 2.33E-04 ** 10 -1.06E-04 4.10E-01 4.75E-03 5.82E-01 1.9
2E-04 20 -1.73E-04 3.27E-01 2.21E-02 3.36E-01 1.77E-04 40 7.63E-04 2.10E-01 1.64E-01 1.59E-04 1.93E-04 *** √|PPC| decrease​ 5 2.67E-04 -1.84E-01 3.98E-01 5.01E-03 8.22E-05 * 10 2.36E-04 -1.81E-01 1.82E
-01 6.04E-02 1.18E-04 20 9.91E-06 -1.45E-01
Shell cwd was reset to
```

**Agent**

The README lists `signeurons.py`, but the repository doesn't contain it. The paper also links Science Data Bank (doi:10.57760/sciencedb.32375) for analysis scripts, so I'll check what that holds.

**Agent calls Bash**

```bash
curl -sL -m 30 -o $TMPDIR/sdb.html -w "%{http_code} %{url_effective}\n" https://doi.org/10.57760/sciencedb.32375; grep -oiE "[a-z0-9_ -]+\.(py|m|r|ipynb|zip|tar)" $TMPDIR/sdb.html | sort -u | head; grep -o "<title>[^<]*" $TMPDIR/sdb.html
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
curl -sL -m 30 "https://www.scidb.cn/api/sdb-dataset-service/dataset/details/c8f780ee66fc420e99af26a77d415b0b" | head -c 3000; echo; curl -sL -m 30 "https://www.scidb.cn/api/sdb-query-service/query/file-list?datasetId=c8f780ee66fc420e99af26a77d415b0b&version=V1&path=&page=1&size=50" | head -c 3000
```

Result: the fetched text is not kept.

**Agent**

The Science Data Bank deposit requires a login, so I can't read it. Next, the rest of the checker, to see how it matches p-values.

**Agent calls Bash**

```bash
sed -n 80,200p tools/claims_check.py
```

```
texts = [t for p in paper_paths for t in flattenings(p.read_text(encoding="utf-8", errors="replace"))]
    problems = 0
    for err in schema("claims").iter_errors(_plain(doc)):
        print("SCHEMA", "/".join(str(x) for x in err.path) or "(top level)", err.message)
        problems += 1
    quotes = values = 0
    for c in doc.get("claims", []):
        if c.get("quote"):
            quotes += 1
            if not quote_found(c["quote"], texts):
                print("QUOTE NOT FOUND", c["id"])
                problems += 1
        for s in c.get("statistics", []):
            for v in [s.get("p")] + ([s["ci"]["low"], s["ci"]["high"]] if "ci" in s else []):
                if v is None:
                    continue
                values += 1
                if not any(f in t for f in printed_forms(v) for t in texts):
                    print("VALUE NOT FOUND (confirm by reading)", c["id"], v)
                    problems += 1
[... 13 more lines not kept]
```

**Agent**

I have what I need: the full text, the supplement, and the code. Now writing the claims file.

**Agent calls Write**

```json
{
 "file_path": "claims/001678/10.1162-imag.a.1066.yaml",
 "content": "# Claims for Bell Vila, Koletar, Dorr, Trevisiol, Goubran, Sled, Bazzigaluppi & Stefanovic,\n# \"Parametrizing alternating current stimulation for neuromodulation\", Imaging Neuroscience\n# (2025/2026), doi:10.1162/imag.a.1066, on dandiset 001678.\n#\n# Written by an agent (model \"claude-opus-5-5\", Claude Code in GitHub Actions), 2026-10-21,\n# protocol as stated in docs/protocol.md. No data of the dandiset were looked at; only its title\n# and description on the archive.\n#\n# Text read: the version of record, open access (CC BY), as served by Europe PMC (PMC12779756),\n# main text with Methods, figure legends and Tables 1 to 4, and the supplementary material\n# (imag.a.1066_supp.pdf: sections S1 1-min sACS, S2 20-min sACS, S3 sham; Tables S1.1 to S1.7,\n# S2.1, S2.2, S3.1; Figures S1.1 to S1.6, S2.1 to S2.4), extracted to text by PyMuPDF.\n#\n# Data the paper used (Methods 2.1 to 2.4). 22 adult Sprague-Dawley rats under propofol, with a\n# 4 x 4 multielectrode array (16 Pt-Ir shanks, 0.5 mm apart) 300 um deep in layer 3 of right\n# sensorimotor cortex, subcutaneous stimulating pads on the skull medial and lateral to the\n# window. TDT PZ5, sampled at 24 kHz (24414.0625 Hz in the code); LFP 0.3 to 300 Hz stored at\n# 12 kHz, MUA 500 to 3000 Hz stored at 24 kHz; the stimulation monitor (two channels, MonA; the\n# code takes their difference as the stimulating waveform).\n#  - 1-min paradigm: 9 rats (4 male, 5 female, 3 months). 20 trials per rat, each 1 min baseline,\n#    1 min sACS, 1 min post; frequencies 5, 10, 20, 40, 140 Hz by amplitudes 50, 100, 200,\n#    400 uA, in randomized order. 140 Hz trials were dropped (incomplete artifact removal), so 16\n#    combinations are analysed.\n#  - 20-min paradigm: 13 rats (7 male, 6 female). 20 min baseline, 20 min of 40 Hz, 100 uA sACS,\n#    and the 10 min after offset (the dandiset description adds further post-stimulation\n#    recordings up to an hour, which the paper does not analyse).\n#  - Sham: one F344 nTg female rat, same preparation, 80 min under propofol without sACS,\n#    split into sixteen 3-min blocks assigned to the 16 parameter combinations. The dandiset\n#    description names only the 9 and 13 rats; whether it holds the sham recording is the\n#    author's to find.\n#  Measured variables: spike times of sorted neurons; firing rate (FR) and entrainment, the\n#  square root of the absolute pairwise phase consistency (sqrt|PPC|) of spike phases relative\n#  to the stimulating waveform; per neuron significance by permutation; LFP log power in six\n#  bands (delta 0.5-4, theta 4-8, alpha 8-12, beta 12-30, low gamma 30-80, high gamma 80-140 Hz)\n#  and the Tort modulation index (MI) for eight band pairs; electric fields from the\n#  stimulation artifact.\n#\n# Code read: github.com/m-bellvila/Parametrizing-alternating-current-stimulation-for-neuromodulation,\n# commit 3b89bf2245c21c660427edcac3ecdf8cda5e7845 (2025-12-05). It holds MUAartrem.m (artifact\n# removal), concatdataforspikesorting.py (concatenation for spike sorting), phaseextract.py\n# (spike phases and neuron inclusion) and nulldistribution.py (permutation null distributions).\n# Its README also names signeurons.py (the comparison of observed changes with the null), which\n# the repository does not hold. No code is given for the linear mixed models, the regressions,\n# the LFP power and PAC analysis, the electric field estimates or the FEM. The paper says data\n# and scripts are also on Science Data Bank (doi:10.57760/sciencedb.32375); its file list could\n# not be read here (the archive asks for a login).\n#\n# Pipeline, as the Methods give it, with the code where the Methods are silent:\n#  - Artifact: during stimulation the MUA band is cleaned with the ARtACS causal comb filter\n#    (Methods 2.5); MUAartrem.m runs artacs.dft.causal over the stimulation frequency +/- 1 Hz\n#    (10 Hz and below) or +/- 4 Hz (above 10 Hz, below 100 Hz), 10 periods, per channel.\n#  - Spike sorting: SpyKING CIRCUS, spatial whitening, detection threshold 6 MAD, templates\n#    merged above 0.95 correlation (Methods 2.6). Other SpyKING CIRCUS settings are not given;\n#    software defaults are the standard choice.\n#  - Phase: Hilbert phase of the stimulating waveform (the difference of the two monitor\n#    channels) over the stimulation period; spikes of the baseline, stimulation and post windows\n#    take the phase at the same offset from the start of their window (phaseextract.py; the\n#    \"temporally extended\" waveform of Fig. 3C). sqrt|PPC| as in Methods 2.6.\n#  - Inclusion of a neuron in a trial: FR of at least 0.25 Hz in more than half of the 10-s\n#    windows of baseline and stimulation (Methods 2.6); phaseextract.py adds at least one such\n#    window in each of the two periods (1-min) or more than 2 spikes in each (20-min).\n#  - Significance: permutation test, 10,000 shuffles, p <= 0.05 (Methods 2.6). FR from 100-ms\n#    bins of both periods pooled, shuffled and split in two; sqrt|PPC| from spike phases pooled\n#    and split. nulldistribution.py first truncates the larger phase group to the size of the\n#    smaller. A neuron's change is an increase or a decrease by the sign of the observed change.\n#    \"Any change\" is a significant FR or sqrt|PPC| change.\n#  - 20-min windows: the full 20 min of stimulation against the 20 min of baseline before it;\n#    the 10 min after offset against the 10 min before onset (Methods 2.6, nulldistribution.py).\n#  - Grubbs' test (alpha 0.05) removes outliers from the Delta values of each\n#    frequency/amplitude group before the mixed models and regressions (Methods 2.6).\n#\n# Details the paper and code leave open, with the readings each criterion runs (labels are\n# used in the criteria):\n#  [S] Sorting unit. Methods 2.6 say sorting was \"performed on per trial MUA recordings\";\n#      concatdataforspikesorting.py concatenates all trials of a rat (and all segments of a\n#      20-min experiment) into one sorting. Readings (S1) one sort per rat over the concatenated\n#      recording, as in the code; (S2) one sort per trial.\n#  [W] Analysis windows. The Methods compare the full 1 min (and the full 20 min) with the\n#      baseline. nulldistribution.py drops the first 5 s of each period (1-min, 5 to 60 s of\n#      baseline and stimulation; 20-min stimulation from 5 s after onset). Main reading (W1)\n#      full periods, per the Methods; variant (W2) the code's 5-s clip. In the 20-min code the\n#      FR null uses only bins from 5 to 60 s of each period (numbins is set from 55 s); that is\n#      run as a further variant of the 20-min stimulation test only.\n#  [P] Sidedness of the sqrt|PPC| test. For FR the Methods test the absolute Delta FR\n#      (two-sided). For sqrt|PPC| they say only \"occurring in <=5% of null distribution samples\",\n#      and the code that compares (signeurons.py) is missing. Readings (P1) two-sided on the\n#      absolute Delta sqrt|PPC| as for FR; (P2) one-sided in the direction of the observed change.\n#  [G] Grubbs' test, per frequency/amplitude group. Readings (G1) per category group (for\n#      example the Delta sqrt|PPC| of neurons with significant increases), iterated until no\n#      outlier remains; (G2) the same, a single pass; (G3) over the Delta values of all\n#      significantly changed neurons of the combination together, iterated.\n#  [R] Points of the linear regressions (scipy.stats; Figs. 6 to 10, Tables S1.2 to S1.5). For\n#      the magnitude of change, (R1) one point per affected neuron and trial, (R2) one point per\n#      rat and combination, the rat's median. The R2 and SE printed in Table S1.2 imply about 100\n#      points for the 400 uA increase in sqrt|PPC| (about 98 residual df), which fits R1; both are\n#      run. For the share of neurons affected, one point per rat and combination (Table S1.5 for\n#      40 Hz implies about 35 points). Table S1.4 and S1.5 slopes and intercepts are in fractions\n#      (intercepts near 0.6 for FR decrease); the main text converts them inconsistently (see the\n#      claims).\n#  [L] LFP channels and model (Methods 2.7). A channel is \"proximal\" to a neuron when the neuron\n#      was detected on it (Results 3.7). Channels with mixed responses are excluded, read as (L1)\n#      a channel with both a significant increase and a significant decrease in the same metric\n#      (FR, or sqrt|PPC|), or (L2) a channel with any increase and any decrease across both\n#      metrics. The model is log power (or order-normalized MI) on band, condition and channel\n#      response with all their interactions (the pairwise pre against post comparisons per band\n#      and response need the three-way interaction), random intercepts for channel within\n#      subject, one row per window. Readings for the family of the Bonferroni correction (B1)\n#      all pre against post comparisons of the model (bands times responses); (B2) none beyond\n#      the single comparison per band and response (the emmeans default within groups). Log\n#      base, (N1) natural, (N2) base 10. FFT window, (F1) rectangular (none named), (F2) Hann.\n#  [M] MI (Methods 2.7). Tensorpac, Tort MI, wavelet decomposition, phase 1 to 29 Hz in 0.5 Hz\n#      steps 2 Hz wide, amplitude 30 to 140 Hz in 1 Hz steps 5 Hz wide, 18 phase bins, 200\n#      surrogates by shuffling the amplitude, 10-s windows over the 2 min before and after.\n#      Open, (M1) MI values not significant against the surrogates set to zero before averaging\n#      within a band pair, or (M2) all values averaged and significance only reported. Order\n#      normalization (Peterson & Cavanaugh, bestNormalize orderNorm) over (O1) all MI values of\n#      the model together, or (O2) each band pair apart.\n#  A claim with several readings is reproduced when it holds under one of them; when the\n#  readings give different outcomes the claim is blocked as methods_underspecified, with all\n#  results shown. Absence claims are judged on the paper's own test as written.\n#\n# Data: every claim uses the recordings the paper describes (data dataset), except the FEM\n# claims, which use the ViZOO Big Male Rat model (IT'IS Foundation) solved in Sim4Life, scaled\n# to the measured fields (with_inputs).\nschema_version: 2\ndataset:\n  archive: dandi\n  id: \"001678\"\npaper: doi:10.1162/imag.a.1066\nclaims:\n- id: efield-1min-medians\n  statement: The electric fields estimated from the stimulation artifact in the 1-minute\n    experiments had medians of 0.77, 1.42, 2.86 and 6.04 mV/mm for 50, 100, 200 and 400 uA.\n  source: Results 3.1, paragraph 1; Figure 1C\n  quote: The magnitude of electric fields was assessed from sACS artifacts in electrophysiological\n    recordings, and had medians of 0.77 ± 0.29, 1.42 ± 0.60, 2.86 ± 1.20, and 6.04 ± 1.68 mV/mm for\n    50, 100, 200, 400 μA sACS amplitudes, respectively\n  data: dataset\n  expected:\n  - quantity: median electric field, 50 uA\n    value: 0.77\n    tolerance: 0.29\n    unit: mV/mm\n  - quantity: median electric field, 100 uA\n    value: 1.42\n    tolerance: 0.6\n    unit: mV/mm\n  - quantity: median electric field, 200 uA\n    value: 2.86\n    tolerance: 1.2\n    unit: mV/mm\n  - quantity: median electric field, 400 uA\n    value: 6.04\n    tolerance: 1.68\n    unit: mV/mm\n  criterion: Method from Methods 2.8. For each rat and amplitude, every channel of every trial\n    of that amplitude is band-pass filtered at the stimulation frequency (5, 10, 20 or 40 Hz);\n    the peak voltage of each stimulation cycle is averaged over the stimulation period per\n    channel; differences between neighbouring electrodes along each array axis are divided by\n    the 0.5 mm spacing (Methods 2.3), the two orthogonal fields combined by vector addition,\n    outliers removed by Grubbs' test (alpha 0.05), and the field averaged over the frequency\n    trials of the amplitude. Tolerances are the paper's stated spread. Open, with readings run\n    (a) the median over rats of each rat's average field, (b) the median over all channel-pair\n    estimates of all rats (Fig. 1C left shows these); \"maximal\" field per axis read as (i) each\n    neighbour pair or (ii) the largest pair per axis and rat. The band-pass filter is not\n    named; a zero-phase Butterworth band of +/- 1 Hz around the stimulation frequency on the\n    LFP stream is the standard choice and is stated as one. Reproduced when all four medians are\n    within tolerance under one reading and rise with amplitude.\n- id: efield-20min-median\n  statement: The median electric field in the 20-minute 100 uA experiments was 1.65 mV/mm.\n  source: Results 3.4, paragraph 1; Figure 1D\n  quote: The median electric field produced for these experiments was 1.65 ± 0.21 mV/mm\n  data: dataset\n  expected:\n    quantity: median electric field, 20-min 40 Hz 100 uA sACS\n    value: 1.65\n    tolerance: 0.21\n    unit: mV/mm\n  criterion: As efield-1min-medians (Methods 2.8, 40 Hz band), over the 13 rats, with the same\n    readings; tolerance the stated spread.\n- id: fem-depth-falloff\n  statement: In the finite element model the electric field falls to about half of its value\n    at the recording electrodes about 70 um deeper.\n  source: Results 3.1, paragraph 2; Figure 2C legend\n  quote: Within the model, the electric field dropped to ~50% of the intensity measured at the\n    recording electrodes at a further ~70 µm in depth\n  data: with_inputs\n  depends_on:\n  - efield-1min-medians\n  expected:\n    quantity: depth below the recording plane at which the field is 50% of its value there\n    value: 70\n    tolerance: 7\n    unit: um\n  criterion: Sim4Life Electro Ohmic Quasi-Static solver on the ViZOO Big Male Rat model with\n    resected tissue removed, 1.5 x 1.5 x 0.1 mm gold electrodes, grid 0.5 mm (0.1 mm between\n    electrodes), scaled so that the RMS field in the 2 x 2 mm array space 300 um deep matches\n    the measured fields (Methods 2.8). The dataset supplies only the measured fields.\n- id: fem-lognormal-fits\n  statement: Cerebral electric field RMS values in the model follow log-normal distributions\n    with shape 1.28 at every amplitude and scale 0.217, 0.400, 0.807 and 1.70 for 50, 100, 200\n    and 400 uA.\n  source: Results 3.1, paragraph 2; Figure 2D\n  quote: The cerebral electric field root mean square (RMS) values were fitted with log-normal\n    distributions, with shape, location, and scale parameters of 1.28, 8.54E-03, 2.17E-01 for 50\n    µA; 1.28, 1.57E-02, 4.00E-01 for 100 µA; 1.28, 3.17E-02, 8.07E-01 for 200 µA; and 1.28,\n    6.70E-02, 1.70 for 400 µA\n  data: with_inputs\n  depends_on:\n  - fem-depth-falloff\n  expected:\n  - quantity: log-normal shape, every amplitude\n    value: 1.28\n    tolerance: 0.128\n  - quantity: log-normal scale, 50 uA\n    value: 0.217\n    tolerance: 0.0217\n  - quantity: log-normal scale, 100 uA\n    value: 0.4\n    tolerance: 0.04\n  - quantity: log-normal scale, 200 uA\n    value: 0.807\n    tolerance: 0.0807\n  - quantity: log-normal scale, 400 uA\n    value: 1.7\n    tolerance: 0.17\n  criterion: scipy.stats lognorm fitted to the cerebral RMS values of the model of\n    fem-depth-falloff (Methods 2.8); units as the paper's (mV/mm, read from the 1 mV/mm\n    threshold). The locations (8.54E-03 to 6.70E-02) are reported alongside.\n- id: fem-ellipsoid-axes\n  statement: Ellipsoids fitted to the hemispheric volumes with fields of at least 1 mV/mm have\n    axes of 7.37, 2.46, 1.58 mm (50 uA), 7.37, 3.32, 2.22 mm (100 uA), 7.86, 4.73, 3.28 mm\n    (200 uA) and 8.80, 6.57, 4.35 mm (400 uA).\n  source: Results 3.1, paragraph 2; Figure 2E\n  quote: Ellipsoids were fit to thresholded hemispheric volumes experiencing electric field\n    magnitude of at least 1 mV/mm, with primary, secondary, and tertiary axes lengths of 7.37,\n    2.46, and 1.58 mm for 50-µA ACS; 7.37, 3.32, and 2.22 for 100-µA ACS; 7.86, 4.73, and 3.28 mm\n    for 200-µA ACS; and 8.80, 6.57, and 4.35 mm for 400-µA ACS\n  data: with_inputs\n  depends_on:\n  - fem-depth-falloff\n  criterion: RMS field of the model thresholded at 1 mV/mm; pyvista.principal_axes on the\n    surface points, standard deviations along each axis times 1.96 as radii (Methods 2.8).\n    Each of the twelve axis lengths within 10% of the paper's value; \"lengths\" read as (a) the\n    radii, (b) twice the radii, both run.\n- id: units-1min\n  statement: In the 1-minute experiments a median of 5 neurons was detected per channel and 66\n    per rat, of which 71% (405 of 586 cumulatively) fired at 0.25 Hz or more in at least half of\n    the 10-second windows and were analysed.\n  source: Results 3.1, paragraph 3; Figure 3A, B\n  quote: Across rats, a median of 5.00 ± 0.17 neurons were detected per recording electrode\n    channel using SpyKING CIRCUS ... This amounted to 66.00 ± 19.60 neurons per rat, of which\n    71.43 ± 10.39% (or, cumulatively, 405/586) had FRs ≥0.25 Hz in at least half of 10-second\n    windows (of baseline and stimulation periods) and were, therefore, included in subsequent\n    analysis\n  data: dataset\n  expected:\n  - quantity: median neurons per channel\n    value: 5.0\n    tolerance: 0.5\n  - quantity: median neurons per rat\n    value: 66\n    tolerance: 19.6\n  - quantity: median percentage of neurons included per rat\n    value: 71.43\n    tolerance: 10.39\n    unit: \"%\"\n  - quantity: neurons included, all rats\n    value: 405\n    tolerance: 40.5\n  - quantity: neurons detected, all rats\n    value: 586\n    tolerance: 58.6\n  criterion: Sorting and inclusion as in the opening comment, under readings S1 and S2. The\n    per-channel tolerance is 10% (the stated 0.17 is narrower than the integer steps of a\n    count); the others are the stated spread, or 10% for the totals. A neuron counts as\n    included when it passes in (a) at least one trial, (b) at least half of its trials; both\n    run. Spike sorting has settings the paper does not give, so counts can differ for reasons\n    other than the data; the result is reported for each reading.\n- id: units-20min\n  statement: In the 20-minute experiments a median of 44 neurons was detected per rat and 4 per\n    channel; 52% (343 of 620) passed the 0.25 Hz criterion and were analysed.\n  source: Results 3.4, paragraph 1\n  quote: A median of 44.00 ± 10.36 neurons were detected per rat, with 4.00 ± 0.60 neurons per\n    electrode channel. Of these neurons, 51.61 ± 10.62% (or, cumulatively, 343 of 620) had FRs\n    ≥0.25 Hz in at least half of all 1-minute windows across baseline and stimulation periods\n  data: dataset\n  expected:\n  - quantity: median neurons per rat\n    value: 44\n    tolerance: 10.36\n  - quantity: median neurons per channel\n    value: 4.0\n    tolerance: 0.6\n  - quantity: median percentage of neurons included per rat\n    value: 51.61\n    tolerance: 10.62\n    unit: \"%\"\n  - quantity: neurons included, all rats\n    value: 343\n    tolerance: 34.3\n  - quantity: neurons detected, all rats\n    value: 620\n    tolerance: 62\n  criterion: As units-1min. The Results say 1-minute windows here while Methods 2.6 and\n    phaseextract.py use 10-second windows; readings (a) 10-s windows over the 20 min baseline\n    and the 20 min stimulation with more than 2 spikes in each (code), (b) 1-min windows,\n    both run, each under S1 and S2.\n- id: baseline-fr\n  statement: Median baseline firing rates were 1.20 Hz in the 1-minute and 1.05 Hz in the\n    20-minute experiments.\n  source: Supplementary Figure S1.1; Results 3.1, paragraph 4 and 3.4, paragraph 1\n  quote: Neurons from 1-min experiments had a median firing rate of 1.20 ± 2.11 Hz, and those\n    from 20-min experiments had a median firing rate of 1.05 ± 4.92 Hz\n  data: dataset\n  depends_on:\n  - units-1min\n  - units-20min\n  expected:\n  - quantity: median baseline FR, 1-min experiments\n    value: 1.2\n    tolerance: 0.12\n    unit: Hz\n  - quantity: median baseline FR, 20-min experiments\n    value: 1.05\n    tolerance: 0.105\n    unit: Hz\n  criterion: Mean baseline FR of each included neuron (Figure S1.1, all neurons of all rats),\n    median over neurons. 10% tolerance, as the stated spreads (2.11 and 4.92 Hz) are wider than\n    the values and do not bound a median. For the 1-min experiments a neuron enters once per\n    included trial (a) or once with its mean over trials (b); both run.\n- id: baseline-ppc\n  statement: Median baseline entrainment (sqrt|PPC|) was 0.12, 0.12, 0.11 and 0.11 to the 5,\n    10, 20 and 40 Hz waveforms in the 1-minute experiments and 0.14 to 40 Hz in the 20-minute\n    experiments.\n  source: Supplementary Figure S1.2; Results 3.1, paragraph 4\n  quote: Neurons from 1-min experiments had median √|PPC| of 0.12 ± 0.05, 0.12 ± 0.07, 0.11 ±\n    0.10, 0.11 ± 0.09 to 5, 10, 20, and 40 Hz endogenous oscillatory frequencies, respectively,\n    and those from 20-min experiments had a median √|PPC| of 0.14 ± 0.06 to 40 Hz frequencies\n  data: dataset\n  depends_on:\n  - units-1min\n  - units-20min\n  expected:\n  - quantity: median baseline sqrt|PPC|, 5 Hz\n    value: 0.12\n    tolerance: 0.05\n  - quantity: median baseline sqrt|PPC|, 10 Hz\n    value: 0.12\n    tolerance: 0.07\n  - quantity: median baseline sqrt|PPC|, 20 Hz\n    value: 0.11\n    tolerance: 0.1\n  - quantity: median baseline sqrt|PPC|, 40 Hz\n    value: 0.11\n    tolerance: 0.09\n  - quantity: median baseline sqrt|PPC|, 20-min experiments\n    value: 0.14\n    tolerance: 0.06\n  criterion: Baseline spike phases taken from the stimulating waveform at the same offset\n    (phaseextract.py), sqrt|PPC| per included neuron and trial, median over neurons by\n    stimulation frequency; tolerances the stated spread.\n- id: table1-any-change\n  statement: Across 1-minute trials about 75% of included neurons per rat were significantly\n    affected (FR or entrainment change), and some neurons were affected under every\n    frequency and amplitude combination.\n  source: Results 3.1, paragraph 3; Table 1\n  quote: Across trials, about 75% of neurons were affected (amplitude/frequency-specific\n    percentages are listed in Table 1 )\n  data: dataset\n  depends_on:\n  - units-1min\n  expected:\n    quantity: median percentage of included neurons per rat with any change, all combinations\n    value: 74.19\n    tolerance: 8.42\n    unit: \"%\"\n  criterion: Table 1 gives, per combination, the median over rats and 95% CI of the percentage\n    of included neurons with a significant change (legend); the overall value is its last\n    cell. Its tolerance is the printed CI half-width. \"Overall\" read as (a) the median of all\n    rat-by-combination percentages, (b) the median of the 16 combination medians; both run,\n    each under W1/W2 and P1/P2. Reproduced when the overall value is within tolerance and the\n    median is above zero in all 16 combinations.\n- id: fr-change-more-common-than-timing\n  statement: In 1-minute trials a change in FR was far more common than a change in spike\n    timing (about 70% against under 10% of neurons).\n  source: Results 3.1, paragraph 3; Table 1\n  quote: A change in FR was more frequent than a change in spike timing (approximately 70% vs.\n    <10%; Table 1 )\n  data: dataset\n  depends_on:\n  - units-1min\n  expected:\n  - quantity: median percentage with FR decrease, all combinations\n    value: 69.23\n    tolerance: 12.64\n    unit: \"%\"\n  - quantity: median percentage with FR increase, all combinations\n    value: 6.7\n    tolerance: 5.38\n    unit: \"%\"\n  - quantity: median percentage with sqrt|PPC| increase, all combinations\n    value: 4.17\n    tolerance: 2.61\n    unit: \"%\"\n  - quantity: median percentage with sqrt|PPC| decrease, all combinations\n    value: 0.0\n    tolerance: 0.44\n    unit: \"%\"\n  criterion: Overall cells of Table 1, readings as table1-any-change. Reproduced when the\n    four values are within tolerance (the CI half-widths) and the share with any FR change is\n    larger than the share with any sqrt|PPC| change, the latter below 10%.\n- id: fr-change-mostly-negative\n  statement: The FR change in 1-minute trials was mostly a decrease, about 60% of neurons\n    inhibited against under 10% excited.\n  source: Results 3.3, paragraph 1; Table 1; Figures 4C, D and 10\n  quote: The majority of neurons responding to sACS decreased their FRs during stimulation (60%\n    of neurons were inhibited by sACS while <10% were excited, Table 1 )\n  data: dataset\n  depends_on:\n  - units-1min\n  criterion: The text gives 60% where Table 1's overall cell is 69.23% (95% CI half-width\n    12.64, so 56.59 to 81.87%). Reproduced when the overall median share with a significant FR\n    decrease lies in 56.59 to 81.87% and the share with an FR increase is below 10%, under the\n    readings of table1-any-change.\n- id: ppc-change-mostly-increase\n  statement: Of the neurons whose spike timing changed in 1-minute trials, nearly all increased\n    their entrainment (about 4%), and very few decreased it (under 0.5%).\n  source: Results 3.1, paragraph 4; Table 1; Figures 6 and 7\n  quote: whereas the vast majority of spike timing affected neurons showed increases in\n    entrainment (4%, Table 1 ... and only a few neurons exhibited negative Δ√|PPC| values (<0.5%;\n    Table 1\n  data: dataset\n  depends_on:\n  - units-1min\n  criterion: Overall cells of Table 1 (4.17 +/- 2.61% increase, 0.00 +/- 0.44% decrease),\n    readings as table1-any-change. Reproduced when the share with a sqrt|PPC| increase is\n    within 4.17 +/- 2.61%, the share with a decrease is below 0.5%, and the increase is larger.\n- id: table2-magnitudes\n  statement: Among affected neurons in 1-minute trials the median changes were +0.32 and -0.13\n    in sqrt|PPC| and +0.85 and -0.91 Hz in FR.\n  source: Table 2\n  inferred: The overall medians are the last cells of Table 2; no sentence states them.\n  data: dataset\n  depends_on:\n  - units-1min\n  expected:\n  - quantity: median Delta sqrt|PPC|, increased neurons\n    value: 0.32\n    tolerance: 0.03\n  - quantity: median Delta sqrt|PPC|, decreased neurons\n    value: -0.13\n    tolerance: 0.02\n  - quantity: median Delta FR, excited neurons\n    value: 0.85\n    tolerance: 0.14\n    unit: Hz\n  - quantity: median Delta FR, suppressed neurons\n    value: -0.91\n    tolerance: 0.04\n    unit: Hz\n  criterion: Per Table 2's legend, the median and 95% CI of the change from baseline to\n    stimulation among neurons significant in that category; tolerance the CI half-width.\n    Readings for the pooling (a) all affected neuron-trials pooled, (b) per-rat medians then\n    the median; each under W, P and G readings (G applies as the values may be cleaned before\n    tabulation).\n- id: fr-change-within-2hz\n  statement: In 1-minute trials FR changes stayed within about 2 Hz of baseline, while\n    entrainment changes were pronounced, Delta sqrt|PPC| reaching 0.55.\n  source: Results 3.1, paragraph 4; Table 2\n  quote: FR remained within ~2 Hz of baseline level ( Table 2 ), 1.20 ± 2.11 Hz ( Supplementary\n    Fig. S1.1 ), whereas entrainment levels achieved were pronounced (Δ√|PPC| of up to 0.55\n  data: dataset\n  depends_on:\n  - units-1min\n  expected:\n    quantity: median Delta sqrt|PPC| of increased neurons at 40 Hz, 400 uA (largest in Table 2)\n    value: 0.55\n    tolerance: 0.07\n  criterion: Table 2 medians as in table2-magnitudes, per combination. Reproduced when every\n    combination's median FR change (excited and suppressed) has absolute value below 2 Hz and\n    the largest median sqrt|PPC| increase is 0.55 +/- 0.07 (Table 2's CI) at 40 Hz, 400 uA.\n- id: fig4-distributions\n  statement: With increasing amplitude and frequency, the distribution of neurons' changes\n    broadens, shifting toward stronger entrainment and slight suppression of firing.\n  source: Figure 4 legend\n  quote: With increasing sACS amplitude (A) and frequency (B), neurons exhibit a broader\n    distribution of responses, with a shift toward stronger entrainment from baseline and a\n    slight suppression of their activity (C, D)\n  data: dataset\n  depends_on:\n  - units-1min\n  criterion: All included neuron-trials (legend, \"all neurons\"), Delta sqrt|PPC| and Delta FR\n    grouped by amplitude (A, C) and by frequency (B, D). The paper fits density functions and\n    names no measure of breadth or shift; readings for breadth (a) standard deviation, (b)\n    interquartile range. Reproduced when, under one reading, the breadth of Delta sqrt|PPC| is\n    larger at 400 than at 50 uA and at 40 than at 5 Hz, the median Delta sqrt|PPC| is higher at\n    400 than 50 uA and at 40 than 5 Hz, and the median Delta FR is below zero at 400 uA and at\n    40 Hz.\n- id: lmer-ppc-increase-interaction\n  statement: Among neurons with increased entrainment, the interaction of amplitude and\n    frequency positively affected the degree of entrainment (LMER), with no significant main\n    effects.\n  source: Results 3.2, paragraph 1; Table 3\n  quote: An LMER revealed that the interaction between amplitude and frequency positively\n    affected the degree of entrainment ( Table 3 , p = 0.02\n  statistics:\n  - about: amplitude by frequency interaction\n    test: linear mixed effects model\n    statistic: estimate 1.47E-05, SE 6.00E-06, t(140.1) = 2.46\n    p: 0.02\n    n: neurons with significant sqrt|PPC| increases in 1-min trials, 9 rats\n  data: dataset\n  depends_on:\n  - units-1min\n  expected:\n    quantity: interaction estimate (Delta sqrt|PPC| per uA per Hz)\n    value: 1.47e-05\n    tolerance: 1.47e-06\n  criterion: Methods 2.6. Delta sqrt|PPC| of neurons with significant increases, on amplitude\n    (uA) and frequency (Hz) as numbers with their interaction (Table 3 gives one coefficient\n    each), random intercepts for neuron within subject, lme4 with Satterthwaite df (Table 3\n    prints df), Grubbs-cleaned (G readings). Reproduced when the interaction is positive with\n    p < 0.05 and the amplitude and frequency main effects have p >= 0.05 (Table 3, 0.683 and\n    0.410), under one reading of W, P and G; partially when the interaction is positive and\n    significant but a main effect is too.\n- id: lmer-ppc-decrease-amplitude\n  statement: Among neurons with decreased entrainment, only amplitude significantly affected\n    the decrease, larger amplitudes giving smaller decreases.\n  source: Results 3.2, paragraph 1; Table 3\n  quote: Only amplitude was found to significantly affect decreases in entrainment ( Table 3 , p\n    = 0.01; Fig. 7 ; Supplementary Tables S1.2–S1.5 ), with increasing amplitude yielding\n    smaller magnitudes of entrainment decrease\n  statistics:\n  - about: amplitude\n    test: linear mixed effects model\n    statistic: estimate 2.73E-04, SE 1.03E-04, t(48.9) = 2.64\n    p: 0.01\n    n: neurons with significant sqrt|PPC| decreases in 1-min trials\n  data: dataset\n  depends_on:\n  - units-1min\n  expected:\n    quantity: amplitude estimate (Delta sqrt|PPC| per uA)\n    value: 2.73e-04\n    tolerance: 2.73e-05\n  criterion: Model as lmer-ppc-increase-interaction, on the Delta sqrt|PPC| (negative) of\n    neurons with significant decreases. Reproduced when the amplitude effect is positive with\n    p < 0.05 and frequency and interaction have p >= 0.05, under one reading.\n- id: lmer-fr-increase-no-dependence\n  statement: The FR change of neurons that increased their FR did not depend on stimulation\n    parameters.\n  source: Results 3.3, paragraph 1; Table 3\n  quote: Neurons that increased their FR during sACS did not show a dependence of their induced\n    FR change on the sACS parameters ( Table 3 )\n  data: dataset\n  depends_on:\n  - units-1min\n  criterion: A claim of absence, judged on the paper's test, the LMER of Methods 2.6 (as\n    lmer-ppc-increase-interaction) on Delta FR of neurons with significant FR increases, at\n    p <= 0.05. Reproduced when amplitude, frequency and their interaction all have p > 0.05\n    (Table 3, 0.434, 0.408, 0.463); not reproduced when any is significant. Estimates are\n    reported either way, under W1 and G1 (the readings that do not touch the test as written\n    are shown as variants).\n- id: lmer-fr-decrease\n  statement: For suppressed neurons, amplitude and frequency had independent and interactive\n    effects on the decrease in FR (larger amplitude and frequency, deeper suppression).\n  source: Results 3.3, paragraph 1; Table 3 and legend\n  quote: an LMER revealed that amplitude and frequency had independent and interactive effects\n    on the decrease in FR ( Table 3 , independent effect of amplitude\n  statistics:\n  - about: amplitude\n    test: linear mixed effects model\n    statistic: estimate -4.84E-04, SE 1.67E-04, t(1766.5) = -2.90\n    p: 0.004\n  - about: frequency\n    test: linear mixed effects model\n    statistic: estimate -1.01E-02, SE 1.61E-03, t(1764.1) = -6.26\n    p: 0.0001\n    p_relation: \"<\"\n  - about: amplitude by frequency interaction\n    test: linear mixed effects model\n    statistic: estimate 1.67E-05, SE 6.72E-06, t(1761.9) = 2.48\n    p: 0.01\n  data: dataset\n  depends_on:\n  - units-1min\n  expected:\n  - quantity: amplitude estimate (Hz per uA)\n    value: -4.84e-04\n    tolerance: 4.84e-05\n  - quantity: frequency estimate (Hz per Hz)\n    value: -1.01e-02\n    tolerance: 1.01e-03\n  criterion: Model as lmer-ppc-increase-interaction on Delta FR of neurons with significant\n    FR decreases. The Results print p = 0.001 for the interaction where Table 3 gives 1.31E-02\n    and its legend p = 0.01; the table is used. Reproduced when amplitude and frequency are\n    negative and the interaction positive, each with p < 0.05, under one reading.\n- id: fig6a-ppc-frequency-400ua\n  statement: At 400 uA the increase in entrainment grew with stimulation frequency, 5.10e-3\n    Delta sqrt|PPC| per Hz.\n  source: Figure 6A; Results 3.2, paragraph 2; Table S1.2\n  quote: The 400 µA linear regressions showed significant increases in Δ√|PPC| with increasing\n    frequency at 5.10 × 10 −3 Δ√|PPC| per Hz, p = 0.002)\n  statistics:\n  - test: linear regression (scipy.stats)\n    p: 0.002\n  data: dataset\n  depends_on:\n  - units-1min\n  expected:\n    quantity: slope, Delta sqrt|PPC| of increased neurons against frequency, 400 uA\n    value: 5.1e-03\n    tolerance: 5.1e-04\n    unit: per Hz\n  criterion: Least-squares regression (scipy.stats.linregress) of Delta sqrt|PPC| of neurons\n    with significant increases at 400 uA on frequency (5, 10, 20, 40 Hz), readings R1/R2, W, P\n    and G. Reproduced when the slope is positive with p <= 0.05 and within tolerance under one\n    reading; partially when positive and significant but outside tolerance. Of the other\n    amplitudes Table S1.2 reports none significant.\n- id: fig6b-ppc-amplitude-5-40hz\n  statement: At 5 and 40 Hz the increase in entrainment grew with amplitude, by 7.22e-4 and\n    7.63e-4 Delta sqrt|PPC| per uA.\n  source: Figure 6B; Results 3.2, paragraph 2; Table S1.3\n  quote: with increasing sACS amplitudes, the degree of entrainment increased across 5 and 40 Hz\n    stimulation frequencies (p = 0.004 and 0.0002, respectively); growing at a rate of 7.22 × 10\n    −4 and 7.63 × 10 −4 Δ√|PPC| per μA\n  statistics:\n  - about: 5 Hz\n    test: linear regression (scipy.stats)\n    p: 0.004\n  - about: 40 Hz\n    test: linear regression (scipy.stats)\n    p: 0.0002\n  data: dataset\n  depends_on:\n  - units-1min\n  expected:\n  - quantity: slope against amplitude, 5 Hz\n    value: 7.22e-04\n    tolerance: 7.22e-05\n    unit: per uA\n  - quantity: slope against amplitude, 40 Hz\n    value: 7.63e-04\n    tolerance: 7.63e-05\n    unit: per uA\n  criterion: As fig6a-ppc-frequency-400ua, regressing on amplitude (50 to 400 uA) at each\n    frequency. Reproduced when both slopes are positive with p <= 0.05 and within tolerance\n    under one reading; partially when one holds.\n- id: fig6d-entrained-share-40hz\n  statement: At 40 Hz the share of neurons entrained rose with amplitude, by 6.04e-2 % per uA.\n  source: Figure 6D; Results 3.2, paragraph 2; Table S1.5\n  quote: 40 Hz also showed an increase in the number of neurons entrained with increasing\n    stimulation amplitude (6.04 × 10 −2 % per μA, p = 0.007)\n  statistics:\n  - test: linear regression (scipy.stats)\n    p: 0.007\n  data: dataset\n  depends_on:\n  - units-1min\n  expected:\n    quantity: slope of the share of included neurons with significant sqrt|PPC| increase against amplitude, 40 Hz\n    value: 6.04e-02\n    tolerance: 6.04e-03\n    unit: percentage points per uA\n  criterion: One point per rat and amplitude (the share of its included neurons in that trial,\n    as Table 1), regressed on amplitude with scipy.stats.linregress; Table S1.5 gives 6.04E-04\n    in fractions, the same slope. Readings W and P. Reproduced when the slope is positive with\n    p <= 0.05 and within tolerance under one reading.\n- id: fig7-ppc-decrease-regressions\n  statement: For neurons with decreased entrainment, only the 400 uA regression across\n    frequency (-1.74e-3 per Hz) and the 5 Hz regression across amplitude (2.67e-4 per uA) were\n    significant.\n  source: Figure 7A, B legend; Table S1.2, S1.3\n  quote: Only the 400-µA regression (A) across frequencies and the 5-Hz regression across\n    amplitudes (B) showed significance, with -1.74 × 10 −3 Δ√|PPC| per Hz and 2.67 × 10 −4 Δ√|PPC|\n    per µA (p = 0.04 and 0.005, respectively)\n  statistics:\n  - about: 400 uA, against frequency\n    test: linear regression (scipy.stats)\n    p: 0.04\n  - about: 5 Hz, against amplitude\n    test: linear regression (scipy.stats)\n    p: 0.005\n  data: dataset\n  depends_on:\n  - units-1min\n  expected:\n  - quantity: slope against frequency, 400 uA\n    value: -1.74e-03\n    tolerance: 1.74e-04\n    unit: per Hz\n  - quantity: slope against amplitude, 5 Hz\n    value: 2.67e-04\n    tolerance: 2.67e-05\n    unit: per uA\n  criterion: As fig6a-ppc-frequency-400ua, on the Delta sqrt|PPC| of neurons with significant\n    decreases. Reproduced when both named slopes have the paper's sign, p <= 0.05 and are\n    within tolerance under one reading, and no other of the eight regressions is significant;\n    partially when the two named slopes hold but another regression is also significant.\n- id: fig8a-excited-fr-frequency-100ua\n  statement: At 100 uA the FR increase of excited neurons grew with frequency, 3.65e-2 Hz per\n    Hz.\n  source: Figure 8A; Results 3.3, paragraph 1; Table S1.2\n  quote: Linear regressions of 100 μA sACS response data versus sACS frequency showed increases\n    in the magnitude of FR increase in excited neurons with increasing frequency (3.65 × 10 −2\n    ΔHz per Hz, p = 0.0003)\n  statistics:\n  - test: linear regression (scipy.stats)\n    p: 0.0003\n  data: dataset\n  depends_on:\n  - units-1min\n  expected:\n    quantity: slope of Delta FR of excited neurons against frequency, 100 uA\n    value: 3.65e-02\n    tolerance: 3.65e-03\n    unit: Hz per Hz\n  criterion: As fig6a-ppc-frequency-400ua, on Delta FR of neurons with significant FR\n    increases at 100 uA.\n- id: fig8b-excited-fr-amplitude-5hz\n  statement: At 5 Hz the FR increase of excited neurons grew with amplitude, 2.22e-3 Hz per uA.\n  source: Figure 8B; Results 3.3, paragraph 1; Table S1.3\n  quote: The 5 Hz response regression across amplitudes ( Fig. 8B ; Supplementary Table S1.3 )\n    showed an increase in the magnitude of FR increase of excited neurons with increasing\n    amplitude (2.22 × 10 −3 ΔHz per μA, p = 0.002)\n  statistics:\n  - test: linear regression (scipy.stats)\n    p: 0.002\n  data: dataset\n  depends_on:\n  - units-1min\n  expected:\n    quantity: slope of Delta FR of excited neurons against amplitude, 5 Hz\n    value: 2.22e-03\n    tolerance: 2.22e-04\n    unit: Hz per uA\n  criterion: As fig6b-ppc-amplitude-5-40hz, on Delta FR of neurons with significant FR\n    increases at 5 Hz.\n- id: fig8c-excited-share-frequency-200ua\n  statement: At 200 uA the share of excited neurons fell with frequency.\n  source: Figure 8C; Results 3.3, paragraph 1; Table S1.4\n  quote: The 200 µA response regression showed a significant decrease in the percentage of\n    excited neurons with increasing frequency ( Fig. 8C ; Supplementary Table S1.4 ) (-2.30 ×\n    10 −3 % per Hz, p = 0.01)\n  statistics:\n  - test: linear regression (scipy.stats)\n    p: 0.01\n  data: dataset\n  depends_on:\n  - units-1min\n  expected:\n    quantity: slope of the fraction of included neurons with significant FR increase against frequency, 200 uA\n    value: -2.30e-03\n    tolerance: 2.30e-04\n    unit: fraction per Hz\n  criterion: One point per rat and frequency at 200 uA, regressed on frequency. Table S1.4\n    gives -2.30E-03 in fractions (intercept 0.105, about 10%), so the slope is -0.23 percentage\n    points per Hz; the text's \"% per Hz\" is read as the table's fraction, and the other\n    reading (-2.30e-3 percentage points per Hz) is reported alongside. Reproduced when the\n    slope is negative with p <= 0.05 and within tolerance under one reading of W and P.\n- id: fig9a-suppressed-fr-frequency\n  statement: For suppressed neurons at 50 and 100 uA, FR decreased further with frequency, by\n    -8.33e-3 and -1.19e-2 Hz per Hz.\n  source: Figure 9A legend; Results 3.3, paragraph 2; Table S1.2\n  quote: The 50 and 100 µA regressions across frequencies (A) showed greater degrees of\n    suppression in FRs with increasing frequency (-8.33 × 10 −3 and -1.19 × 10 −2 ΔHz per Hz, p =\n    0.0004 and <0.0001, respectively)\n  statistics:\n  - about: 50 uA\n    test: linear regression (scipy.stats)\n    p: 0.0004\n  - about: 100 uA\n    test: linear regression (scipy.stats)\n    p: 0.0001\n    p_relation: \"<\"\n  data: dataset\n  depends_on:\n  - units-1min\n  expected:\n  - quantity: slope of Delta FR of suppressed neurons against frequency, 50 uA\n    value: -8.33e-03\n    tolerance: 8.33e-04\n    unit: Hz per Hz\n  - quantity: slope of Delta FR of suppressed neurons against frequency, 100 uA\n    value: -1.19e-02\n    tolerance: 1.19e-03\n    unit: Hz per Hz\n  criterion: As fig6a-ppc-frequency-400ua on Delta FR of neurons with significant FR\n    decreases. The Results print \"50 and 10 μA\"; the legend's 100 uA is used (10 uA was not\n    tested). Reproduced when both slopes are negative, p <= 0.05 and within tolerance under one\n    reading; partially when one holds.\n- id: fig9b-suppressed-fr-amplitude-5hz\n  statement: Only at 5 Hz did suppressed neurons' FR decrease further with amplitude,\n    -1.36e-3 Hz per uA.\n  source: Figure 9B legend; Results 3.3, paragraph 2; Table S1.3\n  quote: Only the 5-Hz regression (B) showed increased suppression with increasing amplitude\n    (-1.36 × 10 −3 ΔHz per µA, p = 0.0008)\n  statistics:\n  - test: linear regression (scipy.stats)\n    p: 0.0008\n  data: dataset\n  depends_on:\n  - units-1min\n  expected:\n    quantity: slope of Delta FR of suppressed neurons against amplitude, 5 Hz\n    value: -1.36e-03\n    tolerance: 1.36e-04\n    unit: Hz per uA\n  criterion: As fig6b-ppc-amplitude-5-40hz. Reproduced when the 5 Hz slope is negative,\n    p <= 0.05 and within tolerance, and the 10, 20 and 40 Hz regressions are not significant,\n    under one reading; partially when the 5 Hz slope holds and another is also significant.\n- id: fig9cd-suppressed-share-unchanged\n  statement: The share of suppressed neurons showed no linear dependence on frequency and was\n    maintained across amplitudes.\n  source: Results 3.3, paragraph 2; Figure 9C, D; Tables S1.4, S1.5\n  quote: with no (linear) stimulation frequency dependence of the fraction of neurons affected (\n    Fig. 9C ; Supplementary Table S1.4 ) ... However, the fraction of neurons affected was\n    maintained across sACS amplitudes\n  data: dataset\n  depends_on:\n  - units-1min\n  criterion: A claim of absence, judged on the paper's test, scipy.stats linear regressions of\n    the per-rat share of included neurons with a significant FR decrease against frequency\n    (one per amplitude) and against amplitude (one per frequency), at p <= 0.05, under W1 and\n    P1. Reproduced when none of the eight is significant; not reproduced when any is. Slopes\n    are reported either way.\n- id: fig10a-all-fr-frequency\n  statement: Taking all FR-changed neurons together, suppression deepened with frequency at\n    50, 100 and 200 uA (-1.02e-2, -1.33e-2, -1.47e-2 Hz per Hz), while it was largely\n    maintained across amplitudes.\n  source: Figure 10 legend; Results 3.3, paragraph 2; Tables S1.2, S1.3\n  quote: When considering grouped FR changes, most amplitudes of stimulation elicited further\n    suppression with increasing stimulation frequency (at rates of -1.02 × 10 −2 , -1.33 × 10 −2\n    , and -1.47 × 10 −2 ΔHz per Hz for 50, 100, and 200 µA trials; p = 0.0003, <0.0001, and\n    0.0001, respectively\n  statistics:\n  - about: 50 uA\n    test: linear regression (scipy.stats)\n    p: 0.0003\n  - about: 100 uA\n    test: linear regression (scipy.stats)\n    p: 0.0001\n    p_relation: \"<\"\n  - about: 200 uA\n    test: linear regression (scipy.stats)\n    p: 0.0001\n  data: dataset\n  depends_on:\n  - units-1min\n  expected:\n  - quantity: slope of Delta FR of all FR-changed neurons against frequency, 50 uA\n    value: -1.02e-02\n    tolerance: 1.02e-03\n    unit: Hz per Hz\n  - quantity: slope, 100 uA\n    value: -1.33e-02\n    tolerance: 1.33e-03\n    unit: Hz per Hz\n  - quantity: slope, 200 uA\n    value: -1.47e-02\n    tolerance: 1.47e-03\n    unit: Hz per Hz\n  criterion: As fig6a-ppc-frequency-400ua on Delta FR of all neurons with a significant FR\n    change (increase or decrease). Reproduced when the three slopes are negative, p <= 0.05\n    and within tolerance under one reading; partially when two hold. The amplitude\n    regressions (Fig. 10B) are reported; \"largely maintained\" sets no test.\n- id: lfp-1min-no-change\n  statement: One minute of sACS produced no significant change in LFP power or LF-HF PAC from\n    before to after stimulation.\n  source: Results 3.1, paragraph 4; Tables S1.6, S1.7\n  quote: LFP analysis did not show significant changes in power or LF-HF PAC before and after\n    1-min sACS ( Supplementary Tables S1.6–S1.7 )\n  data: dataset\n  depends_on:\n  - units-1min\n  criterion: A claim of absence, judged on the paper's test, the ANOVA tables of LMERs (Tables\n    S1.6, S1.7), one per response category (increase or decrease in FR or sqrt|PPC|), of log\n    power (or order-normalized MI) on timepoint, band (or band pair), amplitude and frequency\n    with all interactions, on channels proximal to affected neurons. Reproduced when the\n    timepoint term and every interaction containing it have p >= 0.05 in all eight models; not\n    reproduced when any is below. Methods 2.5 say LFP was analysed only around the 20-min\n    trials, so the windows are open; read as the 1 min before onset and the 1 min after offset\n    in 2-s (power) and 10-s (MI) windows, with the L and M readings. Effects reported either\n    way.\n- id: sham-no-fr-change\n  statement: Under sham stimulation no neuron changed its FR in any of the 16 paradigms, and\n    one or two neurons were spuriously detected as changing entrainment in some, without the\n    trends seen under true sACS.\n  source: Results 3.1, paragraph 5; Table S3.1\n  quote: Under sham sACS, no neurons showed significant changes in firing rate across any of the\n    1-minute baseline to sham stimulation paradigms ( Supplementary Table S3.1 ). One or two\n    neurons were spuriously detected as having significantly changed entrainment levels\n  data: dataset\n  criterion: Methods 2.7, the 80-min sham recording cut into sixteen 3-min blocks, each assigned\n    one amplitude and frequency, its first minute as baseline and its second as sham\n    stimulation, through the 1-min pipeline; phases taken from a sinusoid at the assigned\n    frequency, as no stimulating waveform exists (the phase offset does not change PPC).\n    Block assignment is random in the paper; it changes only the phase-reference frequency,\n    and the 16 blocks are run in order (a standard choice). The FR part is a claim of absence\n    judged on the paper's test, the FR permutation test at p <= 0.05: reproduced when no\n    neuron in any block is significant, not reproduced otherwise, with counts reported. The\n    sqrt|PPC| part holds when each block has at most two significant neurons (Table S3.1 shows\n    0 to 2 per category).\n- id: sham-lfp-baseline\n  statement: Without stimulation, LFP band power and modulation indices stayed stable over 80\n    minutes under propofol, for example delta power 1.71e-6 and delta to low-gamma MI 1.17e-3.\n  source: Results 3.7, paragraph 2 and 3.8, paragraph 2\n  quote: In 80-minute LFP recordings under propofol anesthesia without sACS perturbation, power\n    was maintained at 1.71E-06 ± 6.94E-07 mV/Hz, 9.70E-07 ± 3.89E-07 mV/Hz, 6.66E-07 ± 2.72E-07\n    mV/Hz, 3.03E-07 ± 9.35E-08, 8.40E-08 ± 1.74E-08 mV/Hz, and 3.61E-08 ± 3.50E-09 mV/Hz for δ, θ,\n    α, β, low-γ, and high-γ band activity\n  data: dataset\n  expected:\n  - quantity: sham delta power\n    value: 1.71e-06\n    tolerance: 6.94e-07\n    unit: mV/Hz as printed\n  - quantity: sham theta power\n    value: 9.7e-07\n    tolerance: 3.89e-07\n  - quantity: sham alpha power\n    value: 6.66e-07\n    tolerance: 2.72e-07\n  - quantity: sham beta power\n    value: 3.03e-07\n    tolerance: 9.35e-08\n  - quantity: sham low-gamma power\n    value: 8.4e-08\n    tolerance: 1.74e-08\n  - quantity: sham high-gamma power\n    value: 3.61e-08\n    tolerance: 3.5e-09\n  - quantity: sham MI, delta to low gamma\n    value: 1.17e-03\n    tolerance: 1.11e-03\n  - quantity: sham MI, delta to high gamma\n    value: 3.88e-04\n    tolerance: 3.86e-04\n  - quantity: sham MI, theta to low gamma\n    value: 3.90e-04\n    tolerance: 3.48e-04\n  - quantity: sham MI, theta to high gamma\n    value: 2.04e-04\n    tolerance: 1.87e-04\n  - quantity: sham MI, alpha to low gamma\n    value: 7.79e-05\n    tolerance: 8.31e-05\n  - quantity: sham MI, alpha to high gamma\n    value: 1.09e-04\n    tolerance: 1.12e-04\n  - quantity: sham MI, beta to low gamma\n    value: 1.06e-05\n    tolerance: 9.64e-06\n  - quantity: sham MI, beta to high gamma\n    value: 3.78e-05\n    tolerance: 3.05e-05\n  criterion: Methods 2.7, the average and standard deviation of band power and of the raw MI\n    in 1-min windows every 10 min of the sham recording; tolerances the stated SD. Open\n    details, run as readings, power windows (a) 3 s, as the sham paragraph says, (b) 2 s, as\n    for the 20-min analysis it claims to copy; units (the text prints mV/Hz) read as power\n    spectral density in (i) mV^2/Hz, (ii) V^2/Hz; channels, all 16 averaged (none are\n    singled out). The MI readings M1/M2 apply. Reproduced when, under one reading, all six\n    power values and at least six of the eight MI values are within tolerance.\n- id: 20min-during-percentages\n  statement: Over the 20 minutes of sACS, 4% of neurons were entrained and 2% decreased their\n    entrainment, while 54% increased and 34% decreased their FRs; on the whole neurons were\n    excited.\n  source: Results 3.5, paragraph 1; Table 4; Supplementary Figures S2.1, S2.2\n  quote: 4% of all neurons were entrained, while in 2% of all neurons √|PPC| decreased ( Table 4\n    ; Supplementary Fig. S2.1 ). When considering the FRs of neurons, 54% showed increased FRs,\n    while 34% decreased their FRs\n  data: dataset\n  depends_on:\n  - units-20min\n  expected:\n  - quantity: neurons with sqrt|PPC| increase, of 343 (Fig. S2.1, n = 13)\n    value: 3.79\n    tolerance: 0.379\n    unit: \"%\"\n  - quantity: neurons with sqrt|PPC| decrease (n = 7)\n    value: 2.04\n    tolerance: 0.204\n    unit: \"%\"\n  - quantity: neurons with FR increase (Fig. S2.2, n = 186)\n    value: 54.23\n    tolerance: 5.42\n    unit: \"%\"\n  - quantity: neurons with FR decrease (n = 115)\n    value: 33.53\n    tolerance: 3.35\n    unit: \"%\"\n  - quantity: neurons with any change\n    value: 88.63\n    tolerance: 8.86\n    unit: \"%\"\n  criterion: The 20 min of stimulation against the 20 min of baseline (Methods 2.6), the\n    pooled percentages of Table 4 over all included neurons of the 13 rats. Readings S, W\n    (including the code's 55-s FR null) and P. Reproduced when, under one reading, all five are\n    within tolerance (10%, as Table 4 gives no spread for pooled values) and more neurons\n    increase than decrease FR. The per-rat medians of Table 4 (91.89, 0.00, 0.00, 63.41, 24.39%)\n    are reported alongside.\n- id: 20min-post-percentages\n  statement: In the 10 minutes after the 20-minute sACS, 2% of neurons kept increased\n    entrainment and 4% had decreased entrainment; 51% had decreased and 39% increased FRs, so\n    excitation during sACS turned to suppression after it.\n  source: Results 3.6, paragraph 1; Table 4; Supplementary Figures S2.3, S2.4\n  quote: 2% of all neurons maintained imposed spiking patterns (i.e., showed increases in\n    entrainment from baseline after stimulus offset) ... Finally, half of all neurons (51%) had\n    decreased firing post-stimulation ... while 39% showed increased FRs post-sACS ... excitation\n    during sACS thus turned to suppression post-sACS\n  data: dataset\n  depends_on:\n  - units-20min\n  expected:\n  - quantity: neurons with sqrt|PPC| increase after offset (Fig. S2.3, n = 7)\n    value: 2.04\n    tolerance: 0.204\n    unit: \"%\"\n  - quantity: neurons with sqrt|PPC| decrease after offset (n = 15)\n    value: 4.37\n    tolerance: 0.437\n    unit: \"%\"\n  - quantity: neurons with FR increase after offset (Fig. S2.4, n = 134)\n    value: 39.07\n    tolerance: 3.91\n    unit: \"%\"\n  - quantity: neurons with FR decrease after offset (n = 174)\n    value: 50.73\n    tolerance: 5.07\n    unit: \"%\"\n  - quantity: neurons with any change after offset\n    value: 90.38\n    tolerance: 9.04\n    unit: \"%\"\n  criterion: The first 10 min after offset against the last 10 min before onset (Methods 2.6;\n    nulldistribution.py), pooled over the 343 included neurons. Readings S and P. Reproduced\n    when all five are within tolerance (10%) and more neurons decrease than increase FR after\n    offset, while 20min-during-percentages shows the reverse during stimulation.\n- id: 20min-magnitudes\n  statement: Affected neurons changed sqrt|PPC| by +0.04 and -0.07 during 20-minute sACS and by\n    +0.07 and -0.04 after it, with FR changes of +0.91 and -0.30 Hz during and +1.53 and -0.43\n    Hz after.\n  source: Table 4\n  inferred: Values from the columns of Table 4 for changes across all affected neurons; no\n    sentence states them. The Discussion (4.2) says the FR changes remained within 2 Hz.\n  data: dataset\n  depends_on:\n  - 20min-during-percentages\n  - 20min-post-percentages\n  expected:\n  - quantity: median Delta sqrt|PPC| of increased neurons, during\n    value: 0.04\n    tolerance: 0.01\n  - quantity: median Delta sqrt|PPC| of decreased neurons, during\n    value: -0.07\n    tolerance: 0.03\n  - quantity: median Delta FR of excited neurons, during\n    value: 0.91\n    tolerance: 0.42\n    unit: Hz\n  - quantity: median Delta FR of suppressed neurons, during\n    value: -0.3\n    tolerance: 0.37\n    unit: Hz\n  - quantity: median Delta sqrt|PPC| of increased neurons, after\n    value: 0.07\n    tolerance: 0.08\n  - quantity: median Delta sqrt|PPC| of decreased neurons, after\n    value: -0.04\n    tolerance: 0.03\n  - quantity: median Delta FR of excited neurons, after\n    value: 1.53\n    tolerance: 1.41\n    unit: Hz\n  - quantity: median Delta FR of suppressed neurons, after\n    value: -0.43\n    tolerance: 0.44\n    unit: Hz\n  criterion: Medians over the affected neurons of each category, pooled across rats (Table 4,\n    with its 95% CI as tolerance); the same readings as the two percentage claims. The per-rat\n    medians of Table 4 are reported alongside.\n- id: power-entrained-channels\n  statement: On the 12 channels near entrained neurons, log power fell from before to after\n    20-minute sACS in the delta, theta, alpha, beta and low-gamma bands.\n  source: Results 3.7, paragraph 1; Figure 11B legend; Table S2.1\n  quote: For channels near entrained neurons, significant decreases in log power observed across\n    δ, θ, α, β, and low-γ frequency bands (emmean = -0.12, -0.15, -0,13, -0.06, and -0.04\n  statistics:\n  - about: delta, theta, alpha, beta (each)\n    test: LMER pairwise comparison of estimated marginal means, pre against post\n    p: 0.0001\n    p_relation: \"<\"\n    corrected: Bonferroni\n    n: 12 channels\n  - about: low gamma\n    test: LMER pairwise comparison of estimated marginal means, pre against post\n    p: 0.0002\n    corrected: Bonferroni\n    n: 12 channels\n  data: dataset\n  depends_on:\n  - 20min-during-percentages\n  expected:\n  - quantity: channels proximal to neurons with increased sqrt|PPC|\n    value: 12\n    tolerance: 1.2\n  - quantity: post minus pre log power, delta\n    value: -0.12\n    tolerance: 0.012\n  - quantity: theta\n    value: -0.15\n    tolerance: 0.015\n  - quantity: alpha\n    value: -0.13\n    tolerance: 0.013\n  - quantity: beta\n    value: -0.06\n    tolerance: 0.006\n  - quantity: low gamma\n    value: -0.04\n    tolerance: 0.004\n  criterion: Methods 2.7 with readings L1/L2, B1/B2, N1/N2, F1/F2. Channels chosen from the\n    neurons significant over the full 20 min of stimulation; LFP decimated to 1.2 kHz; FFT of\n    non-overlapping 2-s windows over the 2 min before onset and after offset, mean power per\n    band, log-transformed. Reproduced when, under one reading, the five bands decrease with\n    p < 0.05 after correction and high gamma does not, and the contrasts are within tolerance\n    (10%); partially when the signs and significance hold but the contrasts fall outside.\n- id: power-reduced-entrainment-channels\n  statement: On the 6 channels near neurons with decreased entrainment, log power rose in the\n    alpha, beta, low-gamma and high-gamma bands.\n  source: Results 3.7, paragraph 1; Figure 11B legend; Table S2.1\n  quote: whereas near decreases in √|PPC|, channels showed increases in the log power of α, β,\n    low-γ, and high-γ frequency bands (emmean = 0.05, 0.09, 0.09, and 0.09\n  statistics:\n  - about: alpha\n    test: LMER pairwise comparison of estimated marginal means, pre against post\n    p: 0.001\n    corrected: Bonferroni\n    n: 6 channels\n  - about: beta, low gamma (each)\n    test: LMER pairwise comparison of estimated marginal means, pre against post\n    p: 0.0001\n    p_relation: \"<\"\n    corrected: Bonferroni\n  - about: high gamma\n    test: LMER pairwise comparison of estimated marginal means, pre against post\n    p: 0.0007\n    corrected: Bonferroni\n  data: dataset\n  depends_on:\n  - 20min-during-percentages\n  expected:\n  - quantity: channels proximal to neurons with decreased sqrt|PPC|\n    value: 6\n    tolerance: 0.6\n  - quantity: post minus pre log power, alpha\n    value: 0.05\n    tolerance: 0.005\n  - quantity: beta\n    value: 0.09\n    tolerance: 0.009\n  - quantity: low gamma\n    value: 0.09\n    tolerance: 0.009\n  - quantity: high gamma\n    value: 0.09\n    tolerance: 0.009\n  criterion: As power-entrained-channels. Reproduced when the four bands increase with\n    p < 0.05 after correction and delta and theta do not change significantly, under one\n    reading, with contrasts within tolerance; partially when signs and significance hold only.\n- id: power-excited-channels\n  statement: On the 78 channels near neurons whose FR rose, log power increased in all bands.\n  source: Results 3.7, paragraph 2; Figure 11B legend; Table S2.1\n  quote: Channels near excited neurons had increases in log power across all frequency bands\n    (emmean = 0.04, 0.08, 0.10, 0.10, 0.09, and 0.05\n  statistics:\n  - about: each of the six bands\n    test: LMER pairwise comparison of estimated marginal means, pre against post\n    p: 0.0001\n    p_relation: \"<\"\n    corrected: Bonferroni\n    n: 78 channels\n  data: dataset\n  depends_on:\n  - 20min-during-percentages\n  expected:\n  - quantity: channels proximal to neurons with increased FR\n    value: 78\n    tolerance: 7.8\n  - quantity: post minus pre log power, delta\n    value: 0.04\n    tolerance: 0.004\n  - quantity: theta\n    value: 0.08\n    tolerance: 0.008\n  - quantity: alpha\n    value: 0.1\n    tolerance: 0.01\n  - quantity: beta\n    value: 0.1\n    tolerance: 0.01\n  - quantity: low gamma\n    value: 0.09\n    tolerance: 0.009\n  - quantity: high gamma\n    value: 0.05\n    tolerance: 0.005\n  criterion: As power-entrained-channels. Reproduced when all six bands increase with p < 0.05\n    after correction under one reading and the contrasts are within tolerance; partially\n    when signs and significance hold only.\n- id: power-suppressed-channels\n  statement: On the 47 channels near neurons whose FR fell, log power decreased in all bands.\n  source: Results 3.7, paragraph 2; Figure 11B legend; Table S2.1\n  quote: and near suppressed neurons, decreases across all bands (emmean = -0.14, -0.19, -0.18,\n    -0.16, -0.13, and 0.09\n  statistics:\n  - about: each of the six bands\n    test: LMER pairwise comparison of estimated marginal means, pre against post\n    p: 0.0001\n    p_relation: \"<\"\n    corrected: Bonferroni\n    n: 47 channels\n  data: dataset\n  depends_on:\n  - 20min-during-percentages\n  expected:\n  - quantity: channels proximal to neurons with decreased FR\n    value: 47\n    tolerance: 4.7\n  - quantity: post minus pre log power, delta\n    value: -0.14\n    tolerance: 0.014\n  - quantity: theta\n    value: -0.19\n    tolerance: 0.019\n  - quantity: alpha\n    value: -0.18\n    tolerance: 0.018\n  - quantity: beta\n    value: -0.16\n    tolerance: 0.016\n  - quantity: low gamma\n    value: -0.13\n    tolerance: 0.013\n  - quantity: high gamma, sign read as negative\n    value: -0.09\n    tolerance: 0.009\n  criterion: As power-entrained-channels. The legend prints +0.09 for high gamma in a list of\n    decreases \"across all bands\"; it is read as -0.09. Reproduced when all six bands decrease\n    with p < 0.05 after correction under one reading and the contrasts are within tolerance;\n    partially when signs and significance hold only.\n- id: pac-entrained-channels\n  statement: On channels near entrained neurons, order-normalized MI fell after 20-minute sACS\n    for delta and theta to low gamma and to high gamma.\n  source: Results 3.8, paragraph 1; Figure 12B legend; Table S2.2\n  quote: For channels near entrained neurons, there was a significant decrease in the order\n    normalized MI observed in δ to low-γ, θ to low-γ, δ to high-γ, and θ to high-γ (emmean =\n    -0.39, -0.21, -0.15, and -0.15\n  statistics:\n  - about: delta to low gamma, delta to high gamma\n    test: LMER pairwise comparison of estimated marginal means, pre against post\n    p: 0.0001\n    p_relation: \"<\"\n    corrected: Bonferroni\n    n: 12 channels\n  - about: theta to low gamma\n    test: LMER pairwise comparison of estimated marginal means, pre against post\n    p: 0.002\n    corrected: Bonferroni\n  - about: theta to high gamma\n    test: LMER pairwise comparison of estimated marginal means, pre against post\n    p: 0.03\n    corrected: Bonferroni\n  data: dataset\n  depends_on:\n  - 20min-during-percentages\n  expected:\n  - quantity: post minus pre order-normalized MI, delta to low gamma\n    value: -0.39\n    tolerance: 0.039\n  - quantity: theta to low gamma\n    value: -0.21\n    tolerance: 0.021\n  - quantity: delta to high gamma\n    value: -0.15\n    tolerance: 0.015\n  - quantity: theta to high gamma\n    value: -0.15\n    tolerance: 0.015\n  criterion: Methods 2.7, MI as in reading block M of the opening comment (M1/M2, O1/O2), with\n    the L and B readings, 10-s windows over the 2 min before onset and after offset, eight\n    band pairs. Reproduced when, under one reading, the four pairs decrease with p < 0.05\n    after correction and the alpha and beta pairs do not change significantly, with contrasts\n    within tolerance (10%); partially when signs and significance hold only.\n- id: pac-reduced-entrainment-channels\n  statement: On channels near neurons with decreased entrainment, alpha to high-gamma\n    order-normalized MI increased.\n  source: Results 3.8, paragraph 1; Figure 12B legend; Table S2.2\n  quote: whereas channels near decreases in √|PPC| showed a significant increase in α to high-γ\n    coupling (emmean = 0.22, SE = 0.10, p = *0.02)\n  statistics:\n  - test: LMER pairwise comparison of estimated marginal means, pre against post\n    p: 0.02\n    corrected: Bonferroni\n    n: 6 channels\n  data: dataset\n  depends_on:\n  - 20min-during-percentages\n  expected:\n    quantity: post minus pre order-normalized MI, alpha to high gamma\n    value: 0.22\n    tolerance: 0.1\n  criterion: As pac-entrained-channels; tolerance the printed SE. Reproduced when alpha to\n    high gamma increases with p < 0.05 after correction and no other pair changes\n    significantly, under one reading.\n- id: pac-excited-channels\n  statement: On channels near excited neurons, order-normalized MI rose for alpha and beta to\n    low gamma and delta, alpha and beta to high gamma.\n  source: Results 3.8, paragraph 2; Figure 12B legend; Table S2.2\n  quote: Channels near excited neurons showed increases in the order normalized MI between α to\n    low-γ, β to low-γ, δ to high-γ, α to high-γ, and β to high-γ band pairs (emmean = 0.10, 0.10,\n    0.15, 0.12, and 0.09\n  statistics:\n  - about: alpha to low gamma\n    test: LMER pairwise comparison of estimated marginal means, pre against post\n    p: 0.0007\n    corrected: Bonferroni\n    n: 78 channels\n  - about: beta to low gamma\n    test: LMER pairwise comparison of estimated marginal means, pre against post\n    p: 0.0005\n    corrected: Bonferroni\n  - about: delta to high gamma, alpha to high gamma (each)\n    test: LMER pairwise comparison of estimated marginal means, pre against post\n    p: 0.0001\n    p_relation: \"<\"\n    corrected: Bonferroni\n  - about: beta to high gamma\n    test: LMER pairwise comparison of estimated marginal means, pre against post\n    p: 0.002\n    corrected: Bonferroni\n  data: dataset\n  depends_on:\n  - 20min-during-percentages\n  expected:\n  - quantity: post minus pre order-normalized MI, alpha to low gamma\n    value: 0.1\n    tolerance: 0.01\n  - quantity: beta to low gamma\n    value: 0.1\n    tolerance: 0.01\n  - quantity: delta to high gamma\n    value: 0.15\n    tolerance: 0.015\n  - quantity: alpha to high gamma\n    value: 0.12\n    tolerance: 0.012\n  - quantity: beta to high gamma\n    value: 0.09\n    tolerance: 0.009\n  criterion: As pac-entrained-channels. Reproduced when the five pairs increase with p < 0.05\n    after correction under one reading, with contrasts within tolerance; partially when signs\n    and significance hold only.\n- id: pac-suppressed-channels\n  statement: On channels near suppressed neurons, order-normalized MI fell for seven of the\n    eight band pairs (all but beta to low gamma).\n  source: Results 3.8, paragraph 2; Figure 12B legend; Table S2.2\n  quote: and near suppressed neurons, decreases in δ to low-γ, θ to low-γ, α to low-γ, δ to\n    high-γ, θ to high-γ, α to high-γ, and β to high-γ band pairs (emmean = -0.60, -0.37, -0.21,\n    -0.54, -0.36, -0.29, and -0.06\n  statistics:\n  - about: the first six pairs (each)\n    test: LMER pairwise comparison of estimated marginal means, pre against post\n    p: 0.0001\n    p_relation: \"<\"\n    corrected: Bonferroni\n    n: 47 channels\n  - about: beta to high gamma\n    test: LMER pairwise comparison of estimated marginal means, pre against post\n    p: 0.01\n    corrected: Bonferroni\n  data: dataset\n  depends_on:\n  - 20min-during-percentages\n  expected:\n  - quantity: post minus pre order-normalized MI, delta to low gamma\n    value: -0.6\n    tolerance: 0.06\n  - quantity: theta to low gamma\n    value: -0.37\n    tolerance: 0.037\n  - quantity: alpha to low gamma\n    value: -0.21\n    tolerance: 0.021\n  - quantity: delta to high gamma\n    value: -0.54\n    tolerance: 0.054\n  - quantity: theta to high gamma\n    value: -0.36\n    tolerance: 0.036\n  - quantity: alpha to high gamma\n    value: -0.29\n    tolerance: 0.029\n  - quantity: beta to high gamma\n    value: -0.06\n    tolerance: 0.006\n  criterion: As pac-entrained-channels. Reproduced when the seven pairs decrease with p < 0.05\n    after correction under one reading, with contrasts within tolerance; partially when signs\n    and significance hold only.\n"
}
```

```
File created successfully at: claims/001678/10.1162-imag.a.1066.yaml (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
python tools/claims_check.py claims/001678/10.1162-imag.a.1066.yaml paper/10.1162-imag.a.1066.txt; grep -nP "—|rather" claims/001678/*.yaml
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd claims/001678 && grep -nE "^[^#]*[^ ]: .*" 10.1162-imag.a.1066.yaml | grep -vE "^[0-9]+: *(- )?[a-z_]+: " | head; grep -nE "^ {2,}[^-#][^:]*[a-zA-Z0-9)]: " 10.1162-imag.a.1066.yaml | grep -vE "^[0-9]+: +(- )?[a-z_]+: " | head
```

```
901:    judged on the paper's test, the FR permutation test at p <= 0.05: reproduced when no
901:    judged on the paper's test, the FR permutation test at p <= 0.05: reproduced when no
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001678/10.1162-imag.a.1066.yaml",
 "old_string": "test at p <= 0.05: reproduced when no",
 "new_string": "test at p <= 0.05; reproduced when no"
}
```

```
The file claims/001678/10.1162-imag.a.1066.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd  && python tools/claims_check.py claims/001678/10.1162-imag.a.1066.yaml paper/10.1162-imag.a.1066.txt; python - <<'EOF'
import yaml
d=yaml.safe_load(open('claims/001678/10.1162-imag.a.1066.yaml'))
def walk(x):
    if isinstance(x,dict):
        for v in x.values(): yield from walk(v)
    elif isinstance(x,list):
        for v in x: yield from walk(v)
    elif isinstance(x,str): yield x
print([s[:60] for s in walk(d) if ': ' in s])
EOF
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
python -c "
import yaml;d=yaml.safe_load(open('claims/001678/10.1162-imag.a.1066.yaml'))['claims']
print(len(d), sum('quote' in c for c in d), sum('inferred' in c for c in d), sum('statistics' in c for c in d), sum(len(c.get('statistics',[])) for c in d), sum('criterion' in c for c in d), sum('expected' in c for c in d), [c['id'] for c in d if c.get('data')!='dataset'])"; git status --short
```

```
45 43 2 21 37 45 37 ['fem-depth-falloff', 'fem-lognormal-fits', 'fem-ellipsoid-axes']
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
?? claims/001678/
?? scripts
```

**Agent**

I've written `claims/001678/10.1162-imag.a.1066.yaml`. The quote checker reports 45 claims, 43 quotes, 37 statistical values and 0 problems. Nothing is committed.

**Text read.** I read the version of record, open access, from Europe PMC (PMC12779756): the main text with Methods, figure legends and Tables 1 to 4, plus the full supplement (sections S1 to S3, Tables S1.1 to S3.1, Figures S1.1 to S2.4). Nothing the claims need is missing from the text.

**Code read.** I read github.com/m-bellvila/Parametrizing-alternating-current-stimulation-for-neuromodulation at commit 3b89bf2. It holds four scripts:
- `MUAartrem.m` removes the stimulation artifact with a comb filter.
- `concatdataforspikesorting.py` joins each rat's trials for spike sorting.
- `phaseextract.py` computes spike phases and decides which neurons are included.
- `nulldistribution.py` builds the permutation null distributions.

Several pieces are not in the repository:
- `signeurons.py`, which compares observed changes with the null. The README names it.
- The R mixed-model code, the regressions, the LFP power and phase-amplitude coupling code, and the electric-field and finite-element-model code.

The Science Data Bank deposit the paper points to (doi:10.57760/sciencedb.32375) asks for a login, so I could not read its files.

**Claims.** There are 45. 43 have quotes; 2 are marked `inferred`, because their numbers appear only in Tables 2 and 4. 21 claims record statistics (37 tests in all), 45 have criteria and 37 have expected values. Three finite-element-model claims use outside inputs (the ViZOO rat model in Sim4Life); every other claim uses the dataset.

**Details the paper leaves open, with the readings named.** These are listed in the opening comment, labelled [S] to [M], and the criteria refer to the labels.
- **[S] Spike sorting:** the Methods say "per trial" recordings, but the code sorts each rat's trials concatenated. Both readings are named.
- **[W] Analysis windows:** the Methods use the full periods; the code drops the first 5 s. In the 20-min code, the firing-rate null also uses only 5 to 60 s of each period.
- **[P] Entrainment test sidedness:** two-sided on the absolute change, as for firing rate, or one-sided. The missing `signeurons.py` would settle this.
- **[G] Grubbs outlier removal:** per response group or over all affected neurons together; iterated or a single pass.
- **[R] Regression points:** one point per neuron and trial, or per-rat medians. Table S1.2 implies about 100 points, which fits per neuron. The share slopes in Tables S1.4 and S1.5 are in fractions.
- **[L] LFP analysis:**
  - Which channels count as "mixed response" and are excluded.
  - What family the Bonferroni correction covers.
  - Natural log or base 10.
  - A rectangular or Hann FFT window.
- **[M] Phase-amplitude coupling:** whether values not significant against the surrogates are zeroed; whether order normalization pools all values or each band pair apart.

Some open details apply to single claims:
- **Electric field:** how values are combined (per-rat median or all channel pairs pooled), and the band-pass filter, which is not named.
- **Ellipsoids:** whether the axis lengths are radii or diameters.
- **Inclusion windows for the 20-min paradigm:** the Results say 1-minute windows, the Methods and code use 10-second windows.
- **1-min LFP:** the windows, since the Methods say LFP was analysed only around the 20-min trials.
- **Sham:** power windows of 3 s or 2 s, and the power units (printed as "mV/Hz").

**Inconsistencies in the paper, and how I resolved them:**
- The Results give p = 0.001 for the amplitude-by-frequency interaction on firing-rate decrease; Table 3 gives 0.0131. I used the table.
- "50 and 10 μA" in the Results is read as 50 and 100 μA, as in the legend (10 μA was not tested).
- One of the "decreases across all bands" is printed as +0.09; I read it as -0.09.
- The text says 60% of neurons were inhibited; Table 1 gives 69.23%. The criterion accepts any value within Table 1's confidence interval.
- The text gives -2.30e-3 "% per Hz" for the 200 μA share of excited neurons; Table S1.4 gives the same number as a fraction per Hz. I followed the table and report both.

**Missing from the paper.** Nothing in the text is missing. The one gap is in the code: the comparison script, `signeurons.py`, which leaves the entrainment test's sidedness open. Also, the dandiset description names only the 9 and 13 rats, not the single sham rat; whether the dataset holds that recording is for the author to find.

## End of run

36 turns, 9 minutes, result: success.
