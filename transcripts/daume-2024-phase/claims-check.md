# 000673 · claims-check · run 39907737708

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  ls claims/000673/ paper/; grep -n "Reader" -A60 docs/protocol.md | head -150
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  sed -n 96,200p docs/protocol.md
```

```
- `expected`: each reported number the claim rests on, with a tolerance.
     Use the paper's own uncertainty when it gives one (a confidence
     interval, or the stated spread); otherwise 10% of the reported value.
     For a reported range ("2 to 13%"), the claim holds inside the range
     widened by 10% of each bound. Give the reason for any other tolerance.
   - `criterion`: how the claim will be judged, for any claim that is not
     settled by its expected values alone ("similar", "many", "tended to").
     It is written from the paper alone, before anyone analyses the data.
   - When a reported number can be read in more than one way (which trials
     form the denominator, which subset is meant), list in the criterion the
     readings the paper's text plausibly allows, before the analysis. The
     claim is reproduced if the result matches under any of them. The
     notebook shows every reading, the notes say which ones match, and the
     ambiguity is recorded as a deviation.
   - Methods come from the paper, never from the author. Every part of a
     criterion's method (the selection, the measure, the test, windows,
     bins, thresholds, what a measure is compared with) is taken from the
     Methods, the figure legends, the supplement, or the code the paper
     links, and the criterion says which. Search all of them before
     treating a detail as open.
[... 85 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python tools/claims_check.py claims/000673/10.1038-s41586-024-07309-z.yaml paper/10.1038-s41586-024-07309-z.txt; cat claims/000673/10.1038-s41586-024-07309-z.yaml
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  wc -l claims/000673/*.yaml paper/*.txt; ls code 2>/dev/null | head
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1038-s41586-024-07309-z.txt",
 "limit": 700
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "claims/000673/10.1038-s41586-024-07309-z.yaml",
 "limit": 400
}
```

```
1	# Claims for Daume, Kaminski, Schjetnan, Salimpour, Khan, Kyzar, Reed, Anderson, Valiante,
2	# Mamelak & Rutishauser (2024), "Control of working memory by phase-amplitude coupling of human
3	# hippocampal neurons", Nature 629, 393-401, on dandiset 000673.
4	#
5	# Written by an agent (model "claude-opus-5-5", Claude Code in GitHub Actions), 2026-10-23,
6	# protocol pilot-10 as stated in docs/protocol.md.
7	#
8	# Text read: the version of record (open access, CC BY) as served by Europe PMC (PMC11078732),
9	# full text with Results, Methods, figure legends and Extended Data Fig. 1 to 9 legends, and the
10	# Supplementary Information PDF (41586_2024_7309_MOESM1_ESM: Supplementary Tables S1 to S5 and the
11	# Supplementary Discussion). The Peer Review File (MOESM3) is in the text too; the Reporting
12	# Summary (MOESM2) came through empty and nothing here rests on it. The text of Supplementary
13	# Table S4 is garbled (its model formula is lost); its rows (Intercept, SC, Load1, SC:Load1 for
14	# hippocampus and amygdala) were read from the text that survives.
15	#
16	# Code read: github.com/rutishauserlab/SBCAT-release-NWB at commit a25e8cc3 (2025-01-21), the
17	# repository the paper links (also Zenodo 10.5281/zenodo.10494533). It holds sample code only:
18	# loading the NWB files, behaviour metrics (NWB_QA_graphs.m), category cell selection
19	# (NWB_calcSelective_SB.m), the LFP PAC comodulogram with Tort's modulation index
20	# (cfc_tort_comodulogram.m, NWB_samplePAC_LFP.m), the PAC neuron GLMs for one example neuron
[... 380 more lines not kept]
```

**Agent**

Checker result: 56 claims, 0 problems. Now reading the paper text and the rest of the claims.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1038-s41586-024-07309-z.txt",
 "limit": 300
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  awk '{print NR": "length($0)}' paper/*.txt | sort -t: -k2 -n -r | head -20; grep -n "^#\|^[A-Z][a-z]* *$" paper/*.txt | head -80
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  f=paper/10.1038-s41586-024-07309-z.txt; for i in 1 2 3 4 5 6 8 9 10 30 31 32 33 35 36; do echo "$i: $(sed -n ${i}p $f | cut -c1-200)"; done; sed -n 7p $f | fold -s -w 4000 > $TMPDIR/l7.txt; sed -n 34p $f | fold -s -w 4000 > $TMPDIR/l34.txt; wc -l $TMPDIR/l7.txt $TMPDIR/l34.txt; head -c 600 $TMPDIR/l34.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  fold -s -w 1500 paper/10.1038-s41586-024-07309-z.txt > $TMPDIR/p.txt; wc -l $TMPDIR/p.txt; grep -n "Hippocampal PAC is modulated\|^Methods\|Methods \|Patients\b" $TMPDIR/p.txt | head
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/p.txt",
 "offset": 8,
 "limit": 5
}
```

```
8	grid.17063.33 0000 0001 2157 2938 Krembil Research Institute and Division of Neurosurgery, University Health Network (UHN), University of Toronto, Toronto, Ontario Canada 6 grid.21107.35 0000 0001 2171 9311 Department of Neurosurgery, Johns Hopkins School of Medicine, Baltimore, MD USA 7 https://ror.org/05dxps055 grid.20861.3d 0000 0001 0706 8890 Division of Biology and Biological Engineering, California Institute of Technology, Pasadena, CA USA 17 4 2024 2024 629 8011 461995 393 401 3 5 2023 13 3 2024 17 04 2024 10 05 2024 16 05 2024 © The Author(s) 2024 https://creativecommons.org/licenses/by/4.0/ Open Access This article is licensed under a Creative Commons Attribution 4.0 International License, which permits use, sharing, adaptation, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons licence, and indicate if changes were made. The images or other third party material in this article are included in the article’s Creative Commons licence, unless indicated otherwise in a credit line to the material. If material is not included in the article’s Creative Commons licence and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this licence, visit http://creativecommons.org/licenses/by/4.0/ . Control of working memory maintenance by 
9	theta-gamma phase amplitude coupling of human hippocampal neurons 7 4 2023 2023.04.05.535772 bioRxiv 10.1101/2023.04.05.535772 PMC10104113 37066145 Retaining information in working memory is a demanding process that relies on cognitive control to protect memoranda-specific persistent activity from interference 1 , 2 . However, how cognitive control regulates working memory storage is unclear. Here we show that interactions of frontal control and hippocampal persistent activity are coordinat
[... 3 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/p.txt",
 "offset": 14,
 "limit": 2
}
```

```
14	two different gamma-frequency bands—a lower (30–55 Hz) and a higher gamma range (70–140 Hz). For each channel, we then separately averaged the normalized modulation indices in the theta to low-gamma and the theta to high-gamma combinations and assessed which of the channels exhibited significant PAC across both load conditions in the given frequency combination (averaged z score > 1.64; P < 0.05; right sided). For theta to high-gamma PAC, 137 out of 586 hippocampal channels showed significant PAC across all correct trials from both load conditions (Fig. 2b ). For these 137 channels, we then compared the PAC estimates between the two load conditions. This comparison revealed significantly weaker theta–high-gamma PAC in load 3 compared with load 1 trials ( t 136 = −4.26, P < 0.001; Fig. 2c (left); false-discovery rate (FDR) corrected for the five brain regions of interest 33 ; Fig. 2d shows PAC for a single example channel in the hippocampus; Fig. 2e shows the average PAC across all significant PAC channels in the hippocampus). Fig. 2 TG-PAC. a , Average normalized modulation indices for all phase–amplitude pairs. n = 1,917 channels. b , The proportion of channels with significant theta–high-gamma PAC in each area, determined by comparisons to trial-shuffled surrogates (both loads). The horizontal lines indicate the 99th percentile of the surrogate null distribution per area ( P = 0.005 for hippocampus (hippo.), amygdala (amy.) and vmPFC; right-sided permutation test, no 
15	adjustment for multiple comparisons). c , log-normalized modulation indices were averaged within the theta–high-gamma band in each load and compared between the loads in each significant PAC channel in each region. Only in the hippocampus, theta–high-gamma PAC differed as a function of load, with PAC higher in load 1 versus load 3 trials (left: n = 137 channels, P = 0.0005; amygdala (middle): n = 130, P = 0.38; vmPFC (right): n = 40, P = 0.87; two-sided permutation-based t -tests; FDR corrected
[... 1 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/p.txt",
 "offset": 18,
 "limit": 2
}
```

```
18	hippocampus and amygdala combined for simplicity; statistics per area are shown in Extended Data Fig. 4b ). Furthermore, the FRs of category cells were significantly higher in trials in which a stimulus of the preferred category of a cell was held in WM relative to when patients held stimuli in mind that belonged to the non-preferred categories of a cell in the MTL, but not the vmPFC ( t 269 = 2.93, P = 0.001; Fig. 3b ; see Extended Data Fig. 4b for vmPFC). Category neurons in the MTL but not the frontal lobe therefore exhibited stimulus-specific persistent activity (statistics per area are shown in Extended Data Fig. 4b ). For this reason, we focus on MTL category neurons for the remainder of the paper. Fig. 3 FRs and SFC of category neurons in MTL. a , Example hippocampal category neuron. The preferred category of this neuron was ‘animals’. Pic., picture. b , Category neurons ( n = 270) remained active (preferred (pref.) versus baseline (bsl), P = 0.0001; non-preferred (non-pref.), P = 0.0001) and retained their selectivity during the maintenance period, with FRs higher for preferred compared with non-preferred categories ( P = 0.001). FRs are shown as the percentage change compared with the baseline (−0.9 to −0.3 s before picture 1 onset). c , FRs of category neurons were higher in load 1 compared with load 3 trials with their preferred category held in WM ( n = 270, P = 0.004) during the maintenance period. d , Category neurons fired more in correct compared with 
19	incorrect trials ( n = 246, P = 0.02). e , SFC between spikes and LFPs from the same area. The slice ( https://osf.io/r2hvk/ ) was obtained under a Creative Commons licence CC BY 4.0 . f , Paired with PAC channels, hippocampal category neurons were more strongly phase-locked to local gamma LFPs with the preferred category held in WM ( n = 151 combinations; P = 0.004). Differences were not significant in the amygdala ( n = 423) or non-PAC channels (Extended Data Fig. 5e ). Statistical analysis was
[... 1 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/p.txt",
 "offset": 23,
 "limit": 1
}
```

```
23	gamma amplitude (amp.), median split into low and high, were used to predict the spike counts of each neuron from the MTL during the delay. The spike count was higher during high-gamma amplitudes (gamma main effect) and differed in their theta phase distribution between high and low gamma amplitudes (interaction effect), resulting in selecting this neuron as a PAC neuron. b , The proportions of neurons qualifying as PAC neurons. Cat., category. c , d , FRs of PAC neurons were positively correlated with single-trial estimates of TG-PAC in the hippocampus ( c ; n = 79, P = 0.028, mixed-effects GLM), but not in the amygdala ( d ; n = 163, P = 0.98; GLM results are shown in Supplementary Table 4 ). e , f , FRs of PAC neurons during the maintenance period differed between correct and incorrect trials in the hippocampus ( e ; n = 63; correct versus baseline, P = 0.01; incorrect, P = 0.33; correct − incorrect, P = 0.0001; 16 neurons were excluded due to insufficient data in the incorrect condition), but not in the amygdala ( f ; n = 156; correct, P = 0.0001; incorrect, P = 0.0001; correct − incorrect, P = 0.45; 7 were neurons excluded due to insufficient data in the incorrect condition). FRs are shown as the percentage change compared with the baseline (−0.9 to −0.3 s). g , h , FRs did not differ between loads (hippocampus ( g ): n = 79; load 1, P = 0.03; load 3, P = 0.01; load 3 − load 1, P = 0.20; amygdala ( h ): n = 163; load 1, P = 0.0001; load 3, P = 0.0001; load 3 − load 1, P
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/p.txt",
 "offset": 26,
 "limit": 2
}
```

```
26	(Fig. 4d and Supplementary Table 4 ). PAC neurons in the amygdala also showed higher FRs during the maintenance period compared with the baseline ( t 162 = 6.40, P < 0.001), but there were no significant differences between correct and incorrect WM trials ( t 156 = −0.77, P = 0.45; Fig. 4f ), loads (load 3 − load 1, t 162 = 0.26, P = 0.80; Fig. 4h ; SFC and phase shift results in the amygdala are shown in Extended Data Fig. 7c,d ) or fast and slow RT trials ( t 162 = 1.87, P = 0.07). Thus, hippocampal PAC neurons, despite not being tuned to WM content, were engaged in WM maintenance because their FRs were elevated during WM maintenance and differed as a function of behavioural accuracy. PAC neurons phase lock to the frontal cortex Given the properties of PAC neurons shown above, we hypothesized that PAC neurons might be involved in cognitive control of WM. We therefore next examined whether the activity of PAC neurons is related to frontal activity 34 . To do so, we computed cross-regional SFC between spiking activity of PAC neurons in the MTL and the LFPs recorded in the pre-SMA, dACC and vmPFC (Fig. 5a ). If PAC neuron activity is related to frontal cognitive control, we expected cross-regional SFC in the theta range to be stronger in load 3 than in load 1 trials. The data support this hypothesis—SFC was significantly stronger in load 3 compared with load 1 between spiking activity of PAC neurons in the hippocampus and theta-band LFPs recorded in the vmPFC (Fig. 5b and 
27	Methods ; cluster P < 0.001). We did not observe significant differences for other frequency bands, nor for the other two frontal brain areas (see Extended Data Fig. 8a–h for narrow versus broad-spiking neurons, patient-level statistics, load comparisons for within-vmPFC and cross-regional SFC between vmPFC LFPs and hippocampal spiking, as well as comparisons of non-specific global changes). Repeating the same analysis for category neurons did not reveal significant differences in SFC strengt
[... 1 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/p.txt",
 "offset": 30,
 "limit": 30
}
```

```
30	category neurons and PAC neurons that were not also category neurons (Extended Data Fig. 9e,f ). Fig. 6 Noise correlations of PAC neurons in the hippocampus. a , The mean correlation for all category–PAC neuron pairs was positive ( n = 162, P = 0.0001) (left). Right, the mean correlation was larger than the null distribution of mean correlations without noise correlations ( P = 0.001, right-sided permutation test). b , The decoding accuracy for category from FR in the maintenance period with intact or removed noise correlations for an example session. The white dots signify accuracy, and the coloured dots indicate the identity for each neuron. Indiv., individual. c , Adding single PAC neurons to the ensemble with intact noise correlations increased the decoding accuracy ( n = 21; intact, P = 0.0007; removed, P = 0.91; intact − removed, P = 0.003). d , Removing PAC neurons reduced decodability with intact noise correlations only ( n = 22 sessions; intact, P = 0.004; removed, P = 0.20). Removing non-PAC neurons decreased decoding for intact ( P = 0.010) and removed ( P = 0.0001) correlations. e , The decoding difference with and without noise correlations was lower only when PAC neurons were removed ( n = 22 sessions; PAC, P = 0.0007; non-PAC, P = 0.10). f , The signal–noise axis for simulated tuned (neuron 1) and untuned (neuron 2) neurons. The signal–noise axis angle is reduced without noise correlations. g , The signal–noise angle in the data was reduced after removing 
31	noise correlations ( n = 32 sessions, P = 0.009). h , The variance along the signal axis was reduced when noise correlations were intact only when PAC neurons were present ( n = 19 sessions, P = 0.014; main effect ensemble: P = 0.0013; permutation-based F -test). i , Correlations of PAC–category pairs ( n = 162) were stronger in fast ( P = 0.0001) compared with slow ( P = 0.06; median split; fast − slow, P = 0.028; preferred category trials only) RT trials. This effect was significant in load 
[... 28 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/p.txt",
 "offset": 28,
 "limit": 1
}
```

```
28	the MTL to frontal theta LFPs. a , Long-range SFC between MTL spiking activity and LFPs recorded from all three frontal regions. The slices ( https://osf.io/r2hvk/ ) were obtained under a Creative Commons licence CC BY 4.0 . b , Spikes of hippocampal PAC neurons were more strongly synchronized with theta-band LFPs recorded in the vmPFC during the maintenance period during load 3 compared with load 1 trials ( n = 175 connections; cluster P = 0.0001). This was not the case for the pre-SMA and dACC (Extended Data Fig. 8 ). c , d , Category neurons from the hippocampus ( c ; n = 215) or PAC neurons from the amygdala ( d ; n = 767) did not show significant SFC differences between loads relative to the vmPFC LFP. For b – d , statistical analysis was performed using two-sided cluster-based permutation t -tests with a Bonferroni-corrected alpha-level for two MTL areas, three frontal areas and two cell populations. e , Hippocampal PAC cells ( n = 175, cyan line) yielded the strongest long-range theta SFC difference between load 3 and load 1 trials among 10,000 random selections of hippocampus–vmPFC connections ( P = 0.0001, right-sided permutation test). t values correspond to comparisons between load 3 and load 1 trials for an average of SFC values in the significant theta range (2.5–4.3 Hz). For b – d , data are mean (centre line) ± s.e.m. (coloured areas). f , The remote theta-band SFC between spiking activity of PAC neurons and LFPs recorded in the vmPFC was significantly
```

**Agent calls Bash**

```bash
cd /tmp/claude-1001; grep -n "Model 3: SC" p.txt | head -3; awk 'NR>=60 && NR<=120 {print NR": "substr($0,1,120)}' p.txt
```

```
82:				\begin{document}$${\rm{Model\; 3:}}\,{\rm{SC}} \sim 1+{{\rm{Theta}}}_{\cos }+{{\rm{Theta}}}_{\sin }+\left({{\rm{Theta}}}_{\cos }+{{\rm{Theta}}}_{\sin }\right)\times {\rm{Gamma}}$$\end{document} Model 3: SC ~ 1 + Theta cos + Theta sin + Theta cos + Theta sin × Gamma We next compared pairs of models using a likelihood-ratio test between model 1 and the two other models (using compare.m). A neuron qualified as a PAC neuron if model 1 explained variance in spike counts significantly better than both of the other two models ( P < 0.01, FDR corrected for all possible channel combinations). The rationale behind each model comparison was as follows. First, we were specifically interested in neurons that followed the interaction of theta phase and gamma amplitude, that is, PAC, and not just theta phase or gamma amplitude alone. Selecting neurons for which model 1, including the interaction term, explained spike count variance of a given neuron significantly better than model 2, lacking the interaction term, ensured extracting those neurons. Second, we also compared model 1 to model 3, lacking the gamma term, for the following reason. Assume that a given neuron–channel combination has an LFP with strong PAC at the field potential level, that is, strong interactions between theta phase and gamma amplitude, and a neuron of which the FR is not related to neither theta phase nor gamma amplitude. Nevertheless, this situation would result in a significant 
60: 				\usepackage{amsbsy}
61: 				\usepackage{mathrsfs}
62: 				\usepackage{upgreek}
63: 				\setlength{\oddsidemargin}{-69pt}
64: 				\begin{document}$$\text{Model 1:}\,{\rm{SC}} \sim 1+{{\rm{Theta}}}_{\cos }+{{\rm{Theta}}}_{\sin }+{\rm{Gamma}}+\left
65: 				\usepackage{amsmath}
66: 				\usepackage{wasysym} 
67: 				\usepackage{amsfonts} 
68: 				\usepackage{amssymb} 
69: 				\usepackage{amsbsy}
70: 				\usepackage{mathrsfs}
71: 				\usepackage{upgreek}
72: 				\setlength{\oddsidemargin}{-69pt}
73: 				\begin{document}$
[... 48 more lines not kept]
```

**Agent**

Read the Results and first half of Methods; now the remaining Methods and Extended Data legends.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/p.txt",
 "offset": 83,
 "limit": 27
}
```

```
83	interaction term in model 1 because the spikes that fall into the low and high gamma amplitude groups will have different theta phases (due to PAC). This is only the case if the underlying PAC in the LFP is very strong (an illustration and further discussion is provided in Extended Data Fig. 6 ). However, in this scenario, the gamma amplitude term (or the theta phase term) would not be significant. Comparing model 1 to model 2 and model 3 therefore ensures that cells were selected only at PAC neurons in which the interaction term explained variance above and beyond the main effects and interactions alone. As we did not observe strong PAC nor persistently active category neurons in frontal regions, we restricted this analysis to channels from the MTL regions and performed it separately in each load condition. If spike count variance was significantly better explained by model 1 than the two other models in either of the load conditions for at least one neuron-to-channel combination, we included this neuron as a PAC neuron. If a neuron was selected in more than one neuron-to-channel combination, we selected the combination with the highest R 2 in the full model (model 1). This combined channel was later used for within-region SFC as well as FR correlation analyses. Lastly, to determine whether the number of selected PAC neurons per area was significantly higher than chance, we repeated the entire selection process 200 times after pairing spikes and LFPs from different, 
84	randomly selected trials, therefore destroying their relationship with theta phase and gamma amplitude. The P values indicate the proportion of repetitions that resulted in a higher number of selected neurons using the shuffled data than the original number of PAC neurons determined using the unshuffled data. Properties of PAC neurons We used mixed-effects GLMs with load as a confounder and modelling a random intercept for each PAC neuron-to-channel combination nested into patientID (using only c
[... 25 more lines not kept]
```

**Agent**

Now the supplement tables.

**Agent calls Bash**

```bash
cd  sed -n 236,480p paper/10.1038-s41586-024-07309-z.txt | tr '\n' '|' | fold -s -w 3000
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  sed -n 480,1180p paper/10.1038-s41586-024-07309-z.txt | tr '\n' '|' | fold -s -w 3000 | grep -v "^$" | awk '{print substr($0,1,3000)}' | grep -n "" | sed -n '1,3p;'; sed -n 670,720p paper/10.1038-s41586-024-07309-z.txt | tr '\n' '|'; echo; sed -n 720,1180p paper/10.1038-s41586-024-07309-z.txt | tr '\n' ' ' | grep -o "Supplementary Discussion.\{0,200\}\|Related work on role of theta.\{0,3000\}" | head -5
```

Result: not kept, because it reads the paper's text.

**Agent**

I have the paper. Now the rest of the claims file.

**Agent calls Read**

```json
{
 "file_path": "claims/000673/10.1038-s41586-024-07309-z.yaml",
 "offset": 400,
 "limit": 400
}
```

```
400	    of O3, averaged); the load difference of preferred phase tested against zero with a circular
401	    one-sample test (V test against 0); the peak frequency from a comodulogram with 0.5 Hz phase
402	    steps. Reproduced when none of the tests gives p < 0.05; partially reproduced when one does;
403	    not reproduced when more do. The asymmetries are also tested against 0.5.
404	- id: edf3a-kappa-load
405	  statement: The distribution of gamma amplitude over theta phase was wider (lower kappa) in load
406	    3 than in load 1 across hippocampal PAC channels.
407	  source: Extended Data Fig. 3a legend
408	  quote: Across all PAC channels, kappa was significantly lower in load 3 compared to load 1 (n =
409	    137 channels, t(136) = −3.7453, p = 0.0001) trials
410	  statistics:
411	  - test: two-sided permutation-based t-test
412	    statistic: t(136) = -3.7453
413	    p: 0.0001
414	    n: 137 channels
415	  depends_on:
416	  - fig2b-pac-channel-proportions
417	  criterion: Kappa is the von Mises concentration estimated (circ_kappa) from the 18-bin
418	    distribution of high-gamma amplitude over theta phase, bins weighted by their normalized
419	    amplitude; the estimator is not named, and circ_kappa of the CircStat toolbox is the
[... 380 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "claims/000673/10.1038-s41586-024-07309-z.yaml",
 "offset": 800,
 "limit": 380
}
```

```
800	- id: pac-neuron-counts
801	  statement: 79 of 212 hippocampal neurons (37.29%) and 163 of 358 amygdala neurons (45.53%)
802	    qualified as PAC neurons, more than expected by chance.
803	  source: Results, Category neurons are not PAC neurons, paragraph 1; Figure 4a, b
804	  quote: In the hippocampus, 79 (37.29%) out of 212 available neurons ( P < 0.005; 200 permutations
805	    ( Methods ); pre-processing steps removed broadband LFPs for some of the neurons and those
806	    were therefore not part of this analysis) qualified as PAC neurons. In the amygdala, 163
807	    (45.53%) out of 358 neurons ( P < 0.005) qualified as PAC neurons
808	  statistics:
809	  - about: hippocampus
810	    test: permutation test, 200 trial re-pairings of spikes and LFP
811	    p: 0.005
812	    p_relation: <
813	    n: 212 neurons
814	  - about: amygdala
815	    test: permutation test, 200 trial re-pairings of spikes and LFP
816	    p: 0.005
817	    p_relation: <
818	    n: 358 neurons
819	  expected:
[... 360 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "claims/000673/10.1038-s41586-024-07309-z.yaml",
 "offset": 1179,
 "limit": 370
}
```

```
1179	    LFPs was significantly stronger for PAC than for category neurons ... t(376.07) = 3.3942, p =
1180	    0.0001; unpaired two-sided permutation t -test)
1181	  statistics:
1182	  - test: unpaired two-sided permutation t-test
1183	    statistic: t(376.07) = 3.3942
1184	    p: 0.0001
1185	    n: 175 PAC and 215 category neuron connections
1186	  depends_on:
1187	  - fig5b-hippocampus-vmpfc-theta-sfc-load
1188	  criterion: Per connection the load 3 minus load 1 SFC averaged over 2.5 to 4.3 Hz.
1189	- id: edf8de-narrow-spiking
1190	  statement: The load and RT effects on hippocampus-vmPFC theta SFC held for narrow-spiking PAC
1191	    neurons only, not broad-spiking ones.
1192	  source: Extended Data Fig. 8d, e legends
1193	  quote: we observed a significant difference in theta SFC between load 3 and load 1 only for the
1194	    narrow-spiking PAC neurons (trough-to-peak time <0.5 ms; n = 91 connections; cluster-p =
1195	    0.0001, left). No effect was found for broad-spiking PAC neurons (n = 84)
1196	  statistics:
1197	  - about: load, narrow-spiking
1198	    test: two-sided cluster-based permutation t-test
[... 350 more lines not kept]
```

**Agent**

I've read the whole file. Let me look at how `checks` entries are formatted in another file, then make the edits.

**Agent calls Bash**

```bash
cd  grep -l "^checks:" claims/*/*.yaml | head -2; f=$(grep -l "^checks:" claims/*/*.yaml | head -1); sed -n '/^checks:/,$p' $f | head -30; grep -n "checks" tools/claims_check.py | head
```

```
claims/000005/10.1038-nn.4412.yaml
claims/000006/10.1038-s41586-018-0642-9.yaml
checks:
- date: 2026-10-20
  kind: agent
  model: claude-opus-5-5
  ready: true
  changes:
  - behavior-touches. The criterion stated that the touch and trial counts come from the 111 cortical cells and from principal-whisker touches; the paper says neither. Named both as open, with readings for the recordings and for the whiskers counted.
  - vpm-whisking. Added that the 13.5 spikes/s "after onset of whisker movement" is read as the whisking-epoch rate of Fig. 5d, since the paper defines no spike window after whisking onset.
  - exc-vm-touch-whisking. The criterion gave the Supplementary Fig. 4 windows as the measure of the 1.2 mV whisking change; the paper does not say how it is measured. Named it open, with readings (a) those windows and (b) whisking-epoch minus nonwhisking mean Vm.
  - ion-cut-exc-whisking. Uses both readings of the whisking change, as exc-vm-touch-whisking now does.
  - exc-inhibition-timing. Removed the requirement that the delay be positive in most neurons, which the paper does not state (its Discussion gives a range of -0.8 to 1.6 ms); the range is now reported against that.
  - exc-thalamus-photoinhibition. Removed latency reading (b), a 3 s.d. threshold on Vm that appears nowhere in the paper. The Methods' touch-latency rule is applied to laser onset, and the criterion says this is an assumption.
  - pv-enphr-suppression. Same change for its latencies; the Methods' dPSTH/dt rule is applied to the laser-onset PSTH, as an assumption.
  - ion-cut-exc-no-touch. The post-touch Vm (Vm at the peak of the average PSP) is undefined without a PSP and biased upward on a flat average. The test now uses the paper's touch epoch (4 to 50 ms) against the 0 to 5 ms pre-touch mean, with the peak-based amplitude as a variant.
  - fs-suppress-movement-spiking. The paper does not name the groups of its Kruskal-Wallis test; the criterion now says the test is reported and does not en
[... 10 more lines not kept]
```

**Agent**

Making the edits.

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/000673/10.1038-s41586-024-07309-z.yaml",
 "old_string": "    as condenseAreas.m does. Reproduced when every total and every per-area count matches exactly;",
 "new_string": "    as condenseAreas.m does. Tolerance is 0 because these are counts of the recordings the dataset\n    is said to hold, not estimates. Reproduced when every total and every per-area count matches exactly;"
}
```

```
The file claims/000673/10.1038-s41586-024-07309-z.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/000673/10.1038-s41586-024-07309-z.yaml",
 "old_string": "    statistic: t4 = -0.16\n    p: 0.87\n    n: 5 channels\n  - about: dACC\n    test: two-sided permutation-based t-test\n    statistic: t13 = -0.82\n    p: 0.73\n    n: 14 channels",
 "new_string": "    statistic: t4 = -0.16\n    p: 0.87\n    corrected: FDR over five brain areas\n    n: 5 channels\n  - about: dACC\n    test: two-sided permutation-based t-test\n    statistic: t13 = -0.82\n    p: 0.73\n    corrected: FDR over five brain areas\n    n: 14 channels"
}
```

```
The file claims/000673/10.1038-s41586-024-07309-z.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/000673/10.1038-s41586-024-07309-z.yaml",
 "old_string": "combination, as the differing n of Table S1 show. Reproduced when, under one reading, of the\n    20 area and band tests only the two hippocampal high-gamma tests give p < 0.05, both with\n    load 1 higher.",
 "new_string": "combination, as the differing n of Table S1 show. Reproduced when, under one reading, of the\n    area and band tests (19 in Table S1, since pre-SMA had no significant fast theta to high\n    gamma channel) only the two hippocampal high-gamma tests give p < 0.05, both with load 1\n    higher."
}
```

```
The file claims/000673/10.1038-s41586-024-07309-z.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/000673/10.1038-s41586-024-07309-z.yaml",
 "old_string": "t-test between loads (Extended Data Fig. 3 legend). Theta (3-7 Hz) and gamma (70-140 Hz)\n    power on the PAC trials; peak-to-trough",
 "new_string": "t-test between loads (Extended Data Fig. 3 legend, panels b, c, d, h). Theta (3-7 Hz) and\n    gamma (70-140 Hz) power on the PAC trials, the paper's bands; the power estimate is not\n    stated, and readings are (a) the mean squared Hilbert amplitude from the PAC filters of O3,\n    (b) the Welch spectrum of the 0 to 2.5 s window averaged over each band; peak-to-trough"
}
```

```
The file claims/000673/10.1038-s41586-024-07309-z.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/000673/10.1038-s41586-024-07309-z.yaml",
 "old_string": "    of O3, averaged); the load difference of preferred phase tested against zero with a circular\n    one-sample test (V test against 0); the peak frequency",
 "new_string": "    of O3, averaged); the load difference of preferred phase tested against zero, by a test the\n    paper does not name (the legend's t-tests cover panels a-f and h, not g), with readings (a)\n    a V test of the per-channel differences against 0, (b) a two-sided permutation t-test of the\n    differences wrapped to -180 to 180 degrees against 0; the peak frequency"
}
```

```
The file claims/000673/10.1038-s41586-024-07309-z.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/000673/10.1038-s41586-024-07309-z.yaml",
 "old_string": "  statistics:\n  - about: hippocampus, preferred against non-preferred\n    test: two-sided permutation-based t-test\n    p: 0.025\n    n: 89 neurons\n  - about: amygdala, preferred against non-preferred",
 "new_string": "  statistics:\n  - about: hippocampus, preferred against baseline\n    test: two-sided permutation-based t-test\n    p: 0.0001\n    n: 89 neurons\n  - about: hippocampus, non-preferred against baseline\n    test: two-sided permutation-based t-test\n    p: 0.0001\n    n: 89 neurons\n  - about: amygdala, preferred against baseline\n    test: two-sided permutation-based t-test\n    p: 0.0001\n    n: 181 neurons\n  - about: amygdala, non-preferred against baseline\n    test: two-sided permutation-based t-test\n    p: 0.0001\n    n: 181 neurons\n  - about: hippocampus, preferred against non-preferred\n    test: two-sided permutation-based t-test\n    p: 0.025\n    n: 89 neurons\n  - about: amygdala, preferred against non-preferred"
}
```

```
The file claims/000673/10.1038-s41586-024-07309-z.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/000673/10.1038-s41586-024-07309-z.yaml",
 "old_string": "  criterion: Pseudo-populations across sessions (legend), linear SVM as in O11 on rates 0.2 to 1.0\n    s after each encoding picture (the selection window), trials per category subsampled to the\n    smallest count across neurons, 1,000 repetitions, accuracy the mean; null from 1,000 label\n    shuffles. Which encoding presentations enter is not stated; readings are (a) all encoding\n    pictures of both loads; (b) encoding 1 of load 1 trials.",
 "new_string": "  criterion: Pseudo-populations across sessions (legend), linear SVM as in O11, trials per category\n    subsampled to the smallest count across neurons, 1,000 repetitions, accuracy the mean; null\n    from 1,000 label shuffles (Methods). The rate window is not stated beyond \"during picture\n    presentation\"; readings are (w1) 0.2 to 1.0 s after picture onset, the selection window;\n    (w2) 0 to 2 s, the whole presentation. Which encoding presentations enter is not stated;\n    readings are (a) all encoding pictures of both loads; (b) encoding 1 of load 1 trials."
}
```

```
The file claims/000673/10.1038-s41586-024-07309-z.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/000673/10.1038-s41586-024-07309-z.yaml",
 "old_string": "    Reproduced when vmPFC has a cluster with load 3 higher within 2 to 8 Hz and no other\n    cluster,",
 "new_string": "    Reproduced when vmPFC has a cluster with load 3 higher that overlaps the paper's theta band\n    (3 to 7 Hz; the paper's cluster spans 2.5 to 4.3 Hz, Fig. 5e legend) and no other cluster,"
}
```

```
The file claims/000673/10.1038-s41586-024-07309-z.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/000673/10.1038-s41586-024-07309-z.yaml",
 "old_string": "  statement: Hippocampal category neurons and amygdala PAC neurons showed no load difference in SFC\n    to vmPFC LFP.",
 "new_string": "  statement: Hippocampal category neurons showed no load difference in SFC to vmPFC LFP, and\n    amygdala PAC neurons showed none to the LFP of any frontal area."
}
```

```
The file claims/000673/10.1038-s41586-024-07309-z.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/000673/10.1038-s41586-024-07309-z.yaml",
 "old_string": "    averaged over 500 draws; paired permutation t-tests, FDR (Benjamini-Hochberg) over the four.",
 "new_string": "    averaged over 500 draws; paired permutation t-tests, FDR (Benjamini-Hochberg) over \"all\n    comparisons\", which the paper does not list; readings are (a) the four tests of Fig. 6d;\n    (b) those four and the two of Fig. 6e."
}
```

```
The file claims/000673/10.1038-s41586-024-07309-z.yaml has been updated successfully.
```

**Agent**

Now adding the missing Extended Data Fig. 8f-h claim and the checks entry.

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/000673/10.1038-s41586-024-07309-z.yaml",
 "old_string": "    when the narrow-spiking load cluster and RT test give p < 0.05 and the broad-spiking tests do\n    not.\n",
 "new_string": "    when the narrow-spiking load cluster and RT test give p < 0.05 and the broad-spiking tests do\n    not.\n- id: edf8fgh-frontal-controls\n  statement: Across all vmPFC neurons, neither within-region SFC nor SFC to hippocampal LFPs\n    differed between loads, and maintenance firing rates of all neurons in the pre-SMA, dACC and\n    vmPFC did not differ between correct and incorrect trials.\n  source: Extended Data Fig. 8f, g, h legends; Results, PAC neurons phase lock to the frontal\n    cortex, paragraph 1\n  quote: We did not find significant differences between the load conditions for ( f ) within-region\n    SFC or ( g ) cross-regional SFC to hippocampal LFPs across all neurons from the vmPFC ... FRs\n    for all neurons recorded in the three frontal areas were not significantly different between\n    correct and incorrect trials during the delay period (pre-SMA: n = 201; dACC: n = 180; vmPFC:\n    n = 201)\n  expected:\n  - quantity: pre-SMA neurons in the correct against incorrect test\n    value: 201\n    tolerance: 20.1\n  - quantity: dACC neurons in the correct against incorrect test\n    value: 180\n    tolerance: 18\n  - quantity: vmPFC neurons in the correct against incorrect test\n    value: 201\n    tolerance: 20.1\n  criterion: A claim of absence. Panels f and g, SFC as in fig5b-hippocampus-vmpfc-theta-sfc-load\n    (per load, at least 50 spikes per condition) for every vmPFC neuron with every vmPFC channel of\n    its bundle (f) and with every hippocampal channel of the same hemisphere (g), two-sided cluster\n    tests over the 40 frequencies (legend); the legend names no Bonferroni correction, so alpha is\n    0.025 per one-sided cluster (Methods, Statistics), with the 0.025/12 of fig5b shown as a\n    variant. Panel h, per neuron the mean maintenance rate over correct and over incorrect trials\n    of both loads, both readings of O6, neurons without enough incorrect trials left out (O7);\n    two-sided paired permutation t-test per area (legend). Reproduced when no cluster and no area\n    test gives p < 0.05; not reproduced when any does. The n of each area is reported.\n"
}
```

```
The file claims/000673/10.1038-s41586-024-07309-z.yaml has been updated successfully.
```

**Agent calls Bash**

```bash
cd  cat >> claims/000673/10.1038-s41586-024-07309-z.yaml <<'EOF'
checks:
- date: 2026-10-23
  kind: agent
  model: claude-opus-5-5
  ready: true
  changes:
  - cohort-counts. Gave the reason for the zero tolerance (counts of the recordings the dataset should hold), as the protocol asks for any tolerance other than 10%.
  - fig2c-no-load-effect-other-areas. Marked the pre-SMA and dACC tests as FDR corrected over five areas; the Fig. 2c legend says the correction covers all five brain areas.
  - tables1-slow-fast-theta. The criterion counted 20 area and band tests; Table S1 has 19, since pre-SMA had no significant fast theta to high gamma channel.
  - edf3-hippocampus-pac-controls. The power estimate was not stated by the paper and was used without saying so; named it open with two readings. The test for the preferred-phase difference (panel g) was given as a V test, which the paper does not name (the legend's t-tests cover a-f and h); named it open with two readings.
  - edf4b-persistent-activity-by-area. Added the preferred and non-preferred against baseline tests for the hippocampus and amygdala (all p = 0.0001, legend), which the criterion uses but the statistics left out.
  - edf7a-pac-neurons-no-category-decoding. The rate window 0.2 to 1.0 s was presented as fixed; the paper says only "during picture presentation". Named it open with two readings.
  - fig5b-hippocampus-vmpfc-theta-sfc-load. The cluster window "within 2 to 8 Hz" is not in the paper; the criterion now asks for a cluster overlapping the paper's theta band (3 to 7 Hz) and cites the reported 2.5 to 4.3 Hz.
  - fig5cd-no-effect-category-amygdala. The statement now includes the Results' "or regions" for amygdala PAC neurons, which the criterion already tested.
  - fig6d-removing-pac-neurons. The paper corrects "for all comparisons" without listing them; the criterion took the four tests of Fig. 6d as fixed. Named it open, with the four of 6d or those and the two of 6e.
  - Added claim edf8fgh-frontal-controls (Extended Data Fig. 8f-h, cited in the Results as controls for non-specific global changes), which had no claim.
  - Open, not settled. fig4-amygdala-pac-neurons. The paper gives n = 156 neurons for the amygdala correct against incorrect test (163 minus 7 excluded) but t156, which implies 157; the file keeps the legend's 156.
  - Open, not settled. The code (SBCAT-release-NWB) was not available in this run, so the details the file attributes to it (median RT per session, the two-sided p < 0.1 post hoc test of category selection, the bin edges of the PAC neuron GLMs, the -1.5 to 4 s epochs, subspace() for the angle) were not checked against it.
  - Open, not settled. G2 uses FieldTrip's default cluster-forming threshold (clusteralpha 0.05) and maxsum statistic, which the paper does not state; a different threshold could change cluster results.
EOF
python tools/claims_check.py claims/000673/10.1038-s41586-024-07309-z.yaml paper/10.1038-s41586-024-07309-z.txt 2>&1 | head -20
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  python -c "import yaml;yaml.safe_load(open('claims/000673/10.1038-s41586-024-07309-z.yaml'))" 2>&1 | tail -6
```

```
File "/opt/hostedtoolcache/Python/3.13.16/x64/lib/python3.13/site-packages/yaml/scanner.py", line 577, in fetch_value
    raise ScannerError(None, None,
            "mapping values are not allowed here",
            self.get_mark())
yaml.scanner.ScannerError: mapping values are not allowed here
  in "claims/000673/10.1038-s41586-024-07309-z.yaml", line 1251, column 66
```

**Agent calls Read**

```json
{
 "file_path": "claims/000673/10.1038-s41586-024-07309-z.yaml",
 "offset": 1248,
 "limit": 5
}
```

```
1248	  quote: We did not find significant differences between the load conditions for ( f ) within-region
1249	    SFC or ( g ) cross-regional SFC to hippocampal LFPs across all neurons from the vmPFC ... FRs
1250	    for all neurons recorded in the three frontal areas were not significantly different between
1251	    correct and incorrect trials during the delay period (pre-SMA: n = 201; dACC: n = 180; vmPFC:
1252	    n = 201)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/000673/10.1038-s41586-024-07309-z.yaml",
 "old_string": "    correct and incorrect trials during the delay period (pre-SMA: n = 201; dACC: n = 180; vmPFC:\n    n = 201)\n  expected:",
 "new_string": "    correct and incorrect trials during the delay period\n  inferred: The n per area (pre-SMA 201, dACC 180, vmPFC 201) are from the same sentence of the\n    Extended Data Fig. 8h legend, left out of the quote.\n  expected:"
}
```

```
The file claims/000673/10.1038-s41586-024-07309-z.yaml has been updated successfully.
```

**Agent calls Bash**

```bash
cd  grep -n "inferred" claims/*/*.yaml | head -3; python tools/claims_check.py claims/000673/10.1038-s41586-024-07309-z.yaml paper/10.1038-s41586-024-07309-z.txt 2>&1 | tail -5
```

Result: not kept, because it reads the paper's text.

**Agent**

Quote and `inferred` cannot coexist; I'll move the n note into the criterion.

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/000673/10.1038-s41586-024-07309-z.yaml",
 "old_string": "  inferred: The n per area (pre-SMA 201, dACC 180, vmPFC 201) are from the same sentence of the\n    Extended Data Fig. 8h legend, left out of the quote.\n  expected:",
 "new_string": "  expected:"
}
```

```
The file claims/000673/10.1038-s41586-024-07309-z.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/000673/10.1038-s41586-024-07309-z.yaml",
 "old_string": "    test gives p < 0.05; not reproduced when any does. The n of each area is reported.",
 "new_string": "    test gives p < 0.05; not reproduced when any does. The n of each area is reported against\n    the legend's n, which closes the quoted sentence (pre-SMA 201, dACC 180, vmPFC 201)."
}
```

```
The file claims/000673/10.1038-s41586-024-07309-z.yaml has been updated successfully.
```

**Agent calls Bash**

```bash
cd  python tools/claims_check.py claims/000673/10.1038-s41586-024-07309-z.yaml paper/10.1038-s41586-024-07309-z.txt 2>&1 | tail -3; grep -n "—\|rather" claims/000673/*.yaml | grep -v "quote" | head; git status --short
```

Result: not kept, because it reads the paper's text.

**Agent**

The checks entry marks the file `ready: true`. Final checker result: `57 claims, 57 quotes, 117 statistical values, 0 problems`. The first run, before my edits, had 56 claims and 0 problems.

**Changes, by claim**
- **cohort-counts**: added the reason for the zero tolerance: these are counts of recordings the dataset should hold, not estimates.
- **fig2c-no-load-effect-other-areas**: the pre-SMA and dACC tests are now marked FDR corrected over five areas, as the Fig. 2c legend says.
- **tables1-slow-fast-theta**: the criterion counted 20 area and band tests. Table S1 has 19, because pre-SMA had no channel for fast theta to high gamma.
- **edf3-hippocampus-pac-controls**:
  - The paper does not say how power was estimated. This is now named as open, with two readings (Hilbert amplitude and Welch spectrum).
  - The preferred-phase test (panel g) had been given as a V test, which the paper does not name. It is now open, with two readings.
- **edf4b-persistent-activity-by-area**: added the four tests against baseline for hippocampus and amygdala (p = 0.0001). The criterion used them but the statistics list left them out.
- **edf7a-pac-neurons-no-category-decoding**: the 0.2 to 1.0 s rate window had been stated as fixed, but the paper only says "during picture presentation". It is now open: 0.2 to 1.0 s, or 0 to 2 s.
- **fig5b-hippocampus-vmpfc-theta-sfc-load**: the cluster window "2 to 8 Hz" was invented. The criterion now asks for a cluster overlapping the paper's theta band (3 to 7 Hz) and cites the reported 2.5 to 4.3 Hz.
- **fig5cd-no-effect-category-amygdala**: the statement now also covers the Results' "or regions" for amygdala PAC neurons, which the criterion already tested.
- **fig6d-removing-pac-neurons**: the paper corrects "for all comparisons" without listing them. That is now open, with two readings: the four tests of 6d, or those plus the two of 6e.
- **edf8fgh-frontal-controls**: new claim for Extended Data Fig. 8f-h, the frontal control analyses the Results cite. It is a claim of absence.

**Open, recorded in `checks`**
- **fig4-amygdala-pac-neurons**: the paper is inconsistent. It gives n = 156 neurons but t156, which implies 157. The file keeps 156.
- The paper's code repository was not available in this run. The details the file attributes to it could not be checked (median RT per session, the post hoc threshold in category selection, the GLM phase-bin edges, the epoch length, the angle function).
- The cluster tests use FieldTrip's default cluster-forming threshold and cluster statistic, which the paper does not state.

The rest of the file matched the paper: statements, sources, statistics (results, not selection thresholds), tolerances, and the general rules G1 to G4 and open details O1 to O11. Every claim comes from this paper. Nothing was committed or pushed.

## End of run

45 turns, 7 minutes, result: success.
