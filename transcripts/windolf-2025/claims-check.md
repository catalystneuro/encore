# 001290 · claims-check · run 39693735420

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
ls claims/001290/ paper/; grep -n "Reader" -A60 docs/protocol.md | head -150
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -n 96,220p docs/protocol.md; cat claims/001290/*.yaml; python tools/claims_check.py claims/001290/*.yaml paper/*.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/748fb5b8-ed02-421b-a6eb-9f0c6b1a4d52/tool-results/bxrs5jddr.txt"
}
```

```
1	   - `expected`: each reported number the claim rests on, with a tolerance.
2	     Use the paper's own uncertainty when it gives one (a confidence
3	     interval, or the stated spread); otherwise 10% of the reported value.
4	     For a reported range ("2 to 13%"), the claim holds inside the range
5	     widened by 10% of each bound. Give the reason for any other tolerance.
6	   - `criterion`: how the claim will be judged, for any claim that is not
7	     settled by its expected values alone ("similar", "many", "tended to").
8	     It is written from the paper alone, before anyone analyses the data.
9	   - When a reported number can be read in more than one way (which trials
10	     form the denominator, which subset is meant), list in the criterion the
11	     readings the paper's text plausibly allows, before the analysis. The
12	     claim is reproduced if the result matches under any of them. The
13	     notebook shows every reading, the notes say which ones match, and the
14	     ambiguity is recorded as a deviation.
15	   - Methods come from the paper, never from the author. Every part of a
16	     criterion's method (the selection, the measure, the test, windows,
17	     bins, thresholds, what a measure is compared with) is taken from the
18	     Methods, the figure legends, the supplement, or the code the paper
19	     links, and the criterion says which. Search all of them before
20	     treating a detail as open.
[... 586 more lines not kept]
```

**Agent**

Checker: 0 problems. Now the paper.

**Agent calls Bash**

```bash
cd paper; wc -l *.txt; grep -n -i "Extended Data Fig. 3\|spline\|HDBSCAN\|001290\|Raghavan\|Movshon\|pulsation" *.txt | cut -c1-600
```

```
1462 10.1038-s41592-025-02614-5.txt
7:pmc Nat Methods Nat Methods 319 nihpa 101215604 Nature methods 1548-7091 1548-7105 pmc-is-collection-domain yes pmc-collection-title NIHPA Author Manuscripts PMC13055889 PMC13055889.1 13055889 13055889 NIHMS2068114 40050699 10.1038/s41592-025-02614-5 NIHMS2068114 NIHPA2068114 1 Article DREDge: robust motion correction for high-density extracellular recordings across species http://orcid.org/0000-0002-8360-7726 Windolf Charlie 1 2 ✉ Yu Han 2 3 http://orcid.org/0000-0002-4413-3417 Paulk Angelique C. 4 http://orcid.org/0000-0003-4042-2542 Meszéna Domokos 4 5 http://orcid.org/0000-0002-1354-3472
51:[21] Arganda-Carreras, I. et al. Consistent and elastic registration of histological sections using vector-spline regularization. In Proceedings of the Second ECCV International Conference on Computer Vision Approaches to Medical Image Analysis, CVAMIA ’06, 85–95 https://doi.org/10.1007/11889762_8 (Springer-Verlag, 2006). 10.1007/11889762_8
133:[62] McInnes, L., Healy, J. & Astels, S. hdbscan: hierarchical density based clustering. J. Open Source Softw. 2, 205 (2017). 10.21105/joss.00205
165:[78] Movshon, J. A., Kiorpes, L., Hawken, M. J. & Cavanaugh, J. R. Functional maturation of the macaque’s lateral geniculate nucleus. J. Neurosci. 25, 2712–2722 (2005). 10.1523/JNEUROSCI.2356-04.2005
```

**Agent calls Bash**

```bash
cd paper; awk '{print NR": "length($0)": "substr($0,1,120)}' *.txt | awk -F': ' '$2>300' | head -120
```

```
7: 138933: pmc Nat Methods Nat Methods 319 nihpa 101215604 Nature methods 1548-7091 1548-7105 pmc-is-collection-domain yes pmc-coll
51: 342: [21] Arganda-Carreras, I. et al. Consistent and elastic registration of histological sections using vector-spline regula
55: 382: [23] Feydy, J., Charlier, B., Vialard, F. -X. & Peyré, G. Optimal transport for diffeomorphic registration. In Medical I
85: 387: [38] Boussard, J., Varol, E., Lee, H. D., Dethe, N. & Paninski, L. Three-dimensional spike localization and improved mot
89: 380: [40] Hurwitz, C., Xu, K., Srivastava, A., Buccino, A. & Hennig, M. Scalable spike source localization in extracellular r
119: 325: [55] Choi, J. et al. Optimal adaptive electrode selection to maximize simultaneously recorded neuron yield. In Larochell
169: 319: [80] Paszke, A. et al. Pytorch: an imperative style, high-performance deep learning library. In Wallach, H. et al. (eds.
```

**Agent calls Bash**

```bash
cd paper; sed -n 7p *.txt | fold -w 2000 -s > $TMPDIR/p.txt; wc -l $TMPDIR/p.txt; grep -n -o -i ".\{400\}\(Extended Data Fig. 3\|spline\|HDBSCAN\|DANDI\)[^.]\{0,400\}" $TMPDIR/p.txt
```

```
70 /tmp/claude-1001/p.txt
8:ing 13 . In this dataset, DREDge’s AP-based motion estimation was able to capture the slow trend of the true motion, but not the faster motion due to heartbeats and other sub-second brain motions ( Fig. 2b ). Because well-isolated activity of probable single units was prominent in this recording, it was possible to estimate their trajectories to obtain a faster timescale AP-based estimate using a spline-based method ( Extended Data Fig
29:from all sessions. This combined set of spike positions was then input directly into DREDge. These two approaches should yield similar results, and they were chosen in each case for methodological convenience. Apart from this difference, motion estimation with DREDge and KS were conducted in the same manner as the other analyses of this paper. Tracking fast motion from spikes using clustering and splines In cases where LFP signals are not available or useful for motion tracking but spike data are plentiful, it may be necessary to correct for motion that is too fast to be modeled by DREDge’s or KS’s spike-based motion tracking, whose temporal resolution is on the order of 1 Hz
29:xt, HDBSCAN 62 is applied to cluster high-amplitude spikes based on DREDge-corrected locations and amplitude features. After subtracting their cluster centroids and removing outliers (points more than five standard deviations from the mean in each cluster), spike locations are roughly centered within each cluster, varying around 0 according to the remaining fast drift. Finally, we fit a smoothing spline to all of these centered positions at once to model the sub-second drift, using 2
46:ice of penetrating or non-penetrating guide tube. The interaction of these constraints and a more thorough discussion of insertion approaches is provided on the NP users wiki 34 . Open-source designs for mechanical mounting components for NP1-NHP to drives from Narishige, NAN and other systems are available GitHub via https://github.com/etrautmann
[... 8 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR; grep -o "Tracking fast motion from spikes using clustering.\{0,2500\}" p.txt; echo; grep -o "The recording used in Extended Data Fig. 3.\{0,1500\}" p.txt; echo; grep -o "Extended Data Fig. 3 | Spline.\{0,1200\}" p.txt; echo; grep -o ".\{1500\}well-isolated activity of probable single units.\{0,1500\}" p.txt
```

```
Tracking fast motion from spikes using clustering and splines In cases where LFP signals are not available or useful for motion tracking but spike data are plentiful, it may be necessary to correct for motion that is too fast to be modeled by DREDge’s or KS’s spike-based motion tracking, whose temporal resolution is on the order of 1 Hz. In Fig. 2b and Extended Data Fig. 3 , we introduced a method that estimates fast motion from spike data. First, slower timescale motion is estimated using DREDge. Next, HDBSCAN 62 is applied to cluster high-amplitude spikes based on DREDge-corrected locations and amplitude features. After subtracting their cluster centroids and removing outliers (points more than five standard deviations from the mean in each cluster), spike locations are roughly centered within each cluster, varying around 0 according to the remaining fast drift. Finally, we fit a smoothing spline to all of these centered positions at once to model the sub-second drift, using 2.5 knots per second to match the apparent motion in the example in Extended Data Fig. 3 . Spike registration quality metrics We introduced two simple metrics to directly compare the quality of motion correction without involving 

The recording used in Extended Data Fig. 3 was made in an anesthetized paralyzed preparation, described in detail previously 78 . We induced anesthesia with an intramuscular injection of ketamine HCI (10 mg per kg body weight) and maintained the animal with isoflurane anesthesia during catheterization of saphenous veins and endotracheal intubation. Throughout the experiment, we maintained anesthesia with an infusion of 6 μg per kg body weight per hour and 15 μg per kg body weight per hour sufentanil citrate and neuromuscular blockade with 0.1 mg per kg body weight per hour vecuronium bromide to limit eye movements. We performed a craniotomy and durotomy to insert an NP array 3 or two-shank 128-channel silicon laminar arrays from the NeuroNex Technology Hub 79 . The 
[... 2 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR; tr -d '\n' < p.txt > q.txt; grep -o "DREDge rescues spike sorting and LFP features in human.\{0,9000\}" q.txt | head -c 9000
```

```
DREDge rescues spike sorting and LFP features in human brain activity A major motivation for this work was the substantial motion observed while recording with NP probes in human participants ( Figs. 2 and 3 and Supplementary Video 1 ): brain movements during open craniotomy and deep brain stimulation (DBS) surgeries are substantial, ranging up to millimeters 13 , 14 ( Fig. 2a and Supplementary Video 1 ). Previous studies addressed this with manual motion tracking in the LFP band 13 or semiautomated tracking in the AP band 14 . In a collection of previously shared and newly collected datasets, DREDge’s automated LFP-based tracking revealed motion visible in both bands ( Fig. 2a ). In a subset of participants ( n = 3), DREDge’s estimate was highly correlated with manual LFP-based tracking (Pt01, r = 0.98; Pt02, r = 0.99; Pt03, r = 0.85; Pearson’s r , P < 0.000001 for all three instances; here, we emphasize r statistics rather than P values, because the sample sizes are large enough so that any signals with some correlation to the drift would have significant P values) and featured similar power spectra ( Extended Data Fig. 2 ). Physical motion of the brain surface tracked in video was also similar to the manual and DREDge estimates ( n = 1; Extended Data Fig. 2 ). To further validate that the same motion appeared in the AP and LFP bands, we examined another human recording 13 . In this dataset, DREDge’s AP-based motion estimation was able to capture the slow trend of the true motion, but not the faster motion due to heartbeats and other sub-second brain motions ( Fig. 2b ). Because well-isolated activity of probable single units was prominent in this recording, it was possible to estimate their trajectories to obtain a faster timescale AP-based estimate using a spline-based method ( Extended Data Fig. 3 ). We found that the motion traces estimated using the spline-based AP method and DREDge-LFP overlapped strongly and that the LFP-corrected spike raster visually alig
[... 1 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR; grep -o "(Pt01, r = 0.93, P < 0.00001; Pt03.\{0,14000\}" q.txt | head -c 14000
```

```
Exit code 143
Command timed out after 1h 0m 0s
```

**Agent**

The regex search stalled on the long text line; switching to Python for text slicing.

**Agent calls Bash**

```bash
cd $TMPDIR; timeout 60 python3 -c "
t=open('q.txt').read()
i=t.find('Pt03, r = 0.95, P < 0.00001)')
print(t[i:i+16000])"
```

```
Pt03, r = 0.95, P < 0.00001). Tracking drift during deep probe insertions in nonhuman primates Since DREDge’s decentralized approach does not require neural activity to conform to a single global template, we hypothesized that it would be able to track motion in the presence of turnover in the population of neurons present in a recording. To test this hypothesis, we studied recordings ( n = 2; Fig. 4 and Supplementary Fig. 5 ) made during deep NP1-NHP probe insertions in rhesus macaques 34 . The probe was inserted from the motor cortex toward the basal ganglia ( Fig. 4a ), with a target insertion depth of over 25 mm and a rate of 10 μm s −1 , so that the drift was several times the length of the probe. Tracking such motion would enable users to map the neural population passing by the probe as it advances into the brain, as previously investigated at smaller scale using tetrodes 39 . Indeed, the probe’s motion relative to the neuronal sources was clearly visible in plots of spike positions over time ( Fig. 4a and Supplementary Fig. 5a ). While the KS global template-based drift tracking failed in this case ( Supplementary Fig. 6 ; likely due to the difficulty of modeling several probe lengths of neuronal populations with a single template), DREDge tracked motion across centimeters ( Fig. 4a ). To validate the motion estimate, we first visualized spikes’ locations 38 in the plane of the probe before and after motion correction ( Fig. 4b ). While single-unit clusters were completely obscured before correction, spike positions resolved into well-isolated clusters after registration. Spike waveforms isolated from three clusters in the registered feature space and plotted after averaging in 15-s bins revealed stable waveform shapes corresponding to single units as they traveled the length of the probe ( Fig. 4c ). Although such insertion recordings are not currently part of experimental workflows, the ability to accurately pinpoint the probe’s location within the target 
[... 1 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR; timeout 60 python3 -c "
t=open('q.txt').read()
import re
for key,n in [('Fig. 2 | ',3500),('Fig. 3 | ',3000),('Preprocessing of AP band data',2500),('Setting parameters',4000),('Spike registration quality metrics We',3000),('Extended Data Table 1',1500)]:
  for m in re.finditer(re.escape(key),t):
    print('=====',key,m.start()); print(t[m.start():m.start()+n][:n]); print()
" | head -c 40000
```

```
===== Fig. 2 |  101065
Fig. 2 | Motion tracking comparisons. a , Manual tracking method using tracing in Blender to track voltage changes in the LFP through time. b , Motion traces tracked manually (black lines) versus those used with DREDge (blue) in three data sets; Pearson correlations between manual and DREDge motion traces per participant, p < 10 −6 in all cases. Top row: full traces of the data through time. Bottom row: zoomed-in views from the grey-outlined boxes shown in the top row. c , Power spectra of the motion traces tracked manually (black lines) versus those used with DREDge (blue) in three data sets. Top row: full power spectra of the motion track through time. Bottom row: zoomed-in views from the grey-outlined boxes shown in the top row. d , Motion tracked using video of the brain movements during a Neuropixels recording and an open craniotomy. Left: video of the intraoperative recording and the pumping evident in the CSF surrounding the electrode was tracked through time. Right: video-tracked movements in the same patient (Pt. 03) at two different scales. e , Power spectrum of the motion tracked using video of the brain movements during a Neuropixels recording and an open craniotomy. Top spectrum: zoomed-out view. Bottom power spectrum plot: zoomed-in view of the video motion tracked overlaid on the same spectra of the DREDge and manual motion tracked for the same case (Pt03). Extended Data Fig. 3 | Spline registration. a Spike raster before registration, with AP DREDge displacement estimate overlaid in red. b Spike raster after registration (grey). Colored spikes represent high amplitude spikes that were clustered by HDBSCAN using their registered positions and amplitudes. c Left, centered positions of the clustered spikes (blue) with the spline fit, that captures the sub-second displacement, overlaid in red. Right, zoom of this time-series between times 100 and 110 seconds. d Top, AP registered spike raster. Bottom, AP registered spike raster cor
[... 31 more lines not kept]
```

**Agent**

Checker passes. So far the dandiset claims look broadly faithful. Now I'm checking the parameter sources, the "scrambled" control, and data availability.

**Agent calls Bash**

```bash
cd $TMPDIR; timeout 60 python3 -c "
t=open('q.txt').read()
import re
i=t.find('these basic p',64619); print(t[i:i+3000]); print('=====')
for key,n in [('scrambl',600),('lambda',300),('λ',300),('Data availability',1800),('Extended Data Fig. 1 |',1500),('correlation threshold',400),('Code availability',800)]:
  for m in list(re.finditer(re.escape(key),t))[:6]:
    print('=====',key,m.start()); print(t[max(0,m.start()-300):m.start()+n]); print()
"
```

```
these basic parameters were chosen using simulation experiments (data not shown). Second, the correlation threshold ( θ C above) was set to 0.1 in AP applications and 0.8 in LFP applications. Finally, the chunk size for online LFP registration was set to 10 s (or 2,500 samples at 250 Hz); because this chunk size is small, the time horizon parameter is not relevant in the LFP application. KS’s motion estimation algorithm was discussed in detail elsewhere 6 ; here, we elaborate the discussion of certain parameters that were part of our tuning, based in part on our reading of KS 2.5’s MATLAB code. KS 2.5 exposes one parameter to control the registration, nBlocks, which controls the number of nonrigid blocks (rectangular windows rather than Gaussian profiles); the number of blocks used is 2 × nBlocks – 1 (see line 58 of align_block2.m). When constructing its three-dimensional spike histogram, KS uses a spatial bin size of 5 μm and a temporal bin size controlled by the algorithm’s global batch size (expressed in samples), which leads to approximately 2.18-s temporal bins in data sampled at 30 kHz, although this will vary with the sampling rate; we did not find improvements in some exploratory experiments when tuning the spatial bin size and did not attempt to adjust the temporal bin size. The most important parameters we adjusted in our experiments were KS 2.5’s two search radius parameters (like our max_disp_um above), which are not exposed in a user-facing way except at our fork (Code Availability). Thus, getting KS results of quality in experiments where these parameters were adjusted will require either modifying KS to change these parameters or using our fork. The first of these, which we refer to as nBinsReg1 , sets the maximal search radius (in units of spatial bins) of template cross-correlations during an initial rigid registration pass, before the recording has been divided into spatial blocks; this parameter is set to 15 bins (or 75 μm) by default. The second,
[... 31 more lines not kept]
```

**Agent**

Paper and code details in the opening comment check out (thresholds, lambda, smoothing, ED Table 1). Let me see how other files write `checks` entries.

**Agent calls Bash**

```bash
grep -l "^checks:" claims/*/*.yaml | head -2 | xargs -I{} sh -c 'echo {}; sed -n "/^checks:/,\$p" {} | head -30'
```

```
claims/000005/10.1038-nn.4412.yaml
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
  - fs-suppress-movement-spiking. The paper does not name the groups of its Kruskal-Wallis test; the criterion now says the test is reported and does not enter the outcome.
  - auc-weak-strong. The cri
[... 39 more lines not kept]
```

**Agent**

Now the edits. Opening comment, pipeline step 1: the spike detection and localization choice could change outcomes, so it becomes two readings and stops being a "standard choice".

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001290/10.1038-s41592-025-02614-5.yaml",
 "old_string": "#     DARTsort (ref. 37, 38) (Methods, Mouse brain activity in vivo data). This is used as the\n#     standard choice; a variant uses SpikeInterface detect_peaks (locally_exclusive, threshold\n#     6, both signs) and localize_peaks (monopolar_triangulation, radius 75 um), as in the dredge\n#     repository's notebook/ap_registration.ipynb.",
 "new_string": "#     DARTsort (ref. 37, 38) (Methods, Mouse brain activity in vivo data). Since detection and\n#     localization can change the spike positions every later step uses, two readings are run:\n#     (i) that pipeline; (ii) SpikeInterface detect_peaks (locally_exclusive, threshold 6, both\n#     signs) and localize_peaks (monopolar_triangulation, radius 75 um), as in the dredge\n#     repository's notebook/ap_registration.ipynb. Every \"combination of readings\" in the\n#     criteria below includes readings (i) and (ii) of this step."
}
```

```
The file claims/001290/10.1038-s41592-025-02614-5.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001290/10.1038-s41592-025-02614-5.yaml",
 "old_string": "    raster of mean spike amplitudes, bins outside the probe after correction masked. Reproduced\n    when, under readings (a) and (b) of step 2, the mean template correlation",
 "new_string": "    raster of mean spike amplitudes, bins outside the probe after correction masked. Reproduced\n    when, under readings (a) and (b) of step 2 and (i) and (ii) of step 1, the mean template correlation"
}
```

```
The file claims/001290/10.1038-s41592-025-02614-5.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001290/10.1038-s41592-025-02614-5.yaml",
 "old_string": "    correction exceeds that of the unregistered raster; not reproduced when it is lower under\n    both; methods_underspecified",
 "new_string": "    correction exceeds that of the unregistered raster; not reproduced when it is lower under\n    all; methods_underspecified"
}
```

```
The file claims/001290/10.1038-s41592-025-02614-5.yaml has been updated successfully.
```

**Agent**

Next, edf3c: the permutation bins, count and 5th-percentile cut are the file's own choices, not the paper's. I'm relabelling them as such.

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001290/10.1038-s41592-025-02614-5.yaml",
 "old_string": "    number. The control is the paper's own, the \"randomly permuted or 'scrambled'\" motion\n    estimate of Fig. 2e (legend). For each combination, the pooled within-cluster s.d. of\n    corrected depth of the clustered spikes is computed after correction by the spline and\n    after correction by the same spline trace with its time bins (0.4 s, the knot spacing)\n    randomly permuted, 100 permutations with a fixed seed (a standard choice). Reproduced when,\n    in every combination, the spline-corrected s.d. is below the 5th percentile of the scrambled\n    s.d. values; not reproduced when in none; methods_underspecified otherwise.",
 "new_string": "    number and no test for this panel. The control is borrowed from another panel of the paper,\n    the \"randomly permuted or 'scrambled'\" motion estimate of Fig. 2e (legend), which the paper\n    uses for ISI violations, not for this figure, and whose permutation unit it does not give.\n    For each combination, the pooled within-cluster s.d. of corrected depth of the clustered\n    spikes is computed after correction by the spline and after correction by the same spline\n    trace with its time bins randomly permuted. The permutation bin (0.4 s, the knot spacing),\n    the 100 permutations with a fixed seed and the one-sided 5% level are choices of this file,\n    not of the paper. Reproduced when, in every combination, the spline-corrected s.d. is below\n    the 5th percentile of the scrambled s.d. values; not reproduced when in none;\n    methods_underspecified otherwise."
}
```

```
The file claims/001290/10.1038-s41592-025-02614-5.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001290/10.1038-s41592-025-02614-5.yaml",
 "old_string": "    spline correction (the spline displacement subtracted from each spike's registered depth at\n    its time). Panel e, the pooled within-cluster s.d. of corrected depth over the HDBSCAN\n    clusters, before and after spline correction.",
 "new_string": "    spline correction (the spline displacement subtracted from each spike's registered depth at\n    its time). Panel e, the pooled within-cluster s.d. of corrected depth over the HDBSCAN\n    clusters, before and after spline correction; the paper names no measure for panel e, so\n    this one is the file's choice, and since the spline is fit to minimize these residuals it\n    is reported with that circularity noted. The 1 s bins of the template correlation are the\n    Methods' and cannot show motion faster than 1 s, so the panel d measure is also reported\n    at 0.1 s bins as a variant that does not enter the outcome."
}
```

```
The file claims/001290/10.1038-s41592-025-02614-5.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001290/10.1038-s41592-025-02614-5.yaml",
 "old_string": "  where: Human recordings of ref. 13, Dryad doi:10.5061/dryad.d2547d840 and DANDI:000397.\n- id: fig3b-evoked-potentials",
 "new_string": "  criterion: The count before correction is a bound (\"more than 500\"); it holds when the\n    unregistered sort gives more than 500 units, and the corrected count is within the\n    expected value's tolerance.\n  where: One of the N > 20 human cortical recordings of Fig. 2d to h; the paper does not say\n    which recording or which deposit holds it (human data from MGH, ref. 13, at Dryad\n    doi:10.5061/dryad.d2547d840 and DANDI:000397; from UCSF, ref. 14, at Dryad\n    doi:10.7272/Q6ST7N3B).\n- id: fig3b-evoked-potentials"
}
```

```
The file claims/001290/10.1038-s41592-025-02614-5.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001290/10.1038-s41592-025-02614-5.yaml",
 "old_string": "  criterion: The reported range 0.5 to 22.2 holds when every per-dataset difference lies within\n    it widened by 10% of each bound (0.45 to 24.42).",
 "new_string": "  criterion: The paper does not say over what unit the differences in mean jumps per minute\n    are taken; the readings are (a) per dataset, the mean over its sessions (ten values), and\n    (b) per session. The reported range 0.5 to 22.2 holds when every difference lies within it\n    widened by 10% of each bound (0.45 to 24.42)."
}
```

```
The file claims/001290/10.1038-s41592-025-02614-5.yaml has been updated successfully.
```

**Agent**

Now I'm adding claims for the main findings that had none (all data elsewhere), plus the checks entry.

**Agent calls Bash**

```bash
cat >> claims/001290/10.1038-s41592-025-02614-5.yaml <<'EOF'
- id: fig2c-lfp-tracking-clusters
  statement: In a human NP1-S recording with millimeters of drift, LFP-based DREDge tracks
    features of both the LFP and the spike raster, and offsetting spike positions by the tracked
    motion reveals isolated clusters with well-stereotyped waveforms.
  source: Results, DREDge rescues spike sorting and LFP features in human brain activity,
    paragraph 2; Fig. 2c
  quote: Offsetting spike positions to compensate for the tracked motion revealed isolated
    clusters of spike activity ( Fig. 2c(ii , iii )).
  data: elsewhere
  where: Human NP1-S recording of ref. 14 (UCSF), Dryad doi:10.7272/Q6ST7N3B.
- id: edf4a-nonrigid-human
  statement: In human recordings, nonrigid LFP-based correction gives more stable spiking activity
    than rigid correction, visibly and in a metric of spike activity stability.
  source: Results, DREDge rescues spike sorting and LFP features in human brain activity,
    paragraph 2; Extended Data Fig. 4a and 4c
  quote: it led to visible improvements in the stability of spiking activity over rigid
    correction, as well as improvements in a metric of spike activity stability
  data: elsewhere
  where: Human recordings of ref. 14 (Dryad doi:10.7272/Q6ST7N3B) and the three human recordings
    of Extended Data Fig. 4c, whose deposit the paper does not name.
- id: supp2-rat-spike-tracking
  statement: In ketamine-xylazine-anesthetized rats, LFP-based tracking gives an artifactually
    oscillatory motion estimate, while spike-based tracking is stable.
  source: Results, DREDge rescues spike sorting and LFP features in human brain activity,
    paragraph 3; Supplementary Fig. 2
  quote: were dominated by global slow-wave activity, leading to an artifactually oscillatory
    motion estimate; however, spike-based tracking was stable in this case.
  data: elsewhere
  where: Neuroseeker rat recordings on G-node (gin.g-node.org/UlbertLab/High_Resolution_Cortical_Spikes).
- id: fig2fg-unit-spatial-spread
  statement: After 250 Hz LFP-based motion-corrected interpolation, the spatial distribution of
    voltage in each sorted human unit is more concentrated, with higher amplitudes.
  source: Results, DREDge rescues spike sorting and LFP features in human brain activity,
    paragraph 4; Fig. 2f and 2g; Extended Data Fig. 5b
  quote: the spatial distribution of voltages in each unit was more concentrated with higher
    amplitudes with this correction
  statistics:
  - test: two-sided two sample t-test at each distance from center
    p: 0.05
    p_relation: "<"
    corrected: Bonferroni
    n: sorted units of one human recording, per distance from center
  data: elsewhere
  where: Same recording as fig2-sorted-units; the paper does not say which deposit holds it.
- id: edf6-128-channel
  statement: In three human awake intraoperative recordings with a 128-channel probe of 30 um
    vertical spacing, DREDge's tracking stabilizes the spike rasters.
  source: Results, DREDge rescues spike sorting and LFP features in human brain activity,
    paragraph 5; Extended Data Fig. 6
  quote: In three such recordings, DREDge’s tracking yielded stabilized spike rasters after motion
    correction of spike locations
  data: elsewhere
  where: Human recordings with a 128-channel probe; the paper does not say whether they are
    among the deposited human data.
- id: fig3gh-iids
  statement: Epileptiform interictal discharges are detectable in the median signal over
    channels both before and after correction, and are not obscured by the preprocessing.
  source: Results, DREDge rescues spike sorting and LFP features in human brain activity,
    paragraph 7; Fig. 3g and 3h; Supplementary Fig. 4
  quote: was large enough to be detected in the median signal over channels before and after
    correction ( Fig. 3h ) and was not obscured by this preprocessing
  data: elsewhere
  where: Human recording of participant Pt03 (ref. 13), Dryad doi:10.5061/dryad.d2547d840 and
    DANDI:000397.
- id: fig4f-insertion-anatomy
  statement: During the deep macaque insertion, averages of waveform features as a function of
    motion-corrected spike depth vary in a way that roughly aligns with the expected anatomical
    boundaries along the trajectory.
  source: Results, Tracking drift during deep probe insertions in nonhuman primates, paragraph 3;
    Fig. 4d to 4f
  quote: Visualizing averages of these features as a function of motion-corrected spike depth
    revealed variations that roughly aligned with expected anatomical boundaries along the
    insertion trajectory
  data: elsewhere
  where: DANDI:001282 (NP1-NHP insertion datasets).
- id: fig5a-imposed-zigzag
  statement: In NP1 and NP2 recordings with imposed zigzag motion of about 50 um, DREDge
    recapitulates the performance of Kilosort.
  source: Results, Estimating motion in acute mouse recordings, paragraph 1; Fig. 5a(i, ii)
  quote: In these recordings, DREDge recapitulated the performance of KS
  data: elsewhere
  where: Figshare doi:10.6084/m9.figshare.14024495.v1 (dataset 1 of ref. 6).
- id: edf4d-nonrigid-ibl
  statement: In nine further IBL recordings across brain regions, DREDge's nonrigid correction
    gives higher template correlation scores than its rigid correction.
  source: Results, Estimating motion in acute mouse recordings, paragraph 4; Extended Data Fig. 4b
    and 4d
  quote: it led to visual improvements ( Extended Data Fig. 4b ) and higher correlation scores
    when compared to rigid correction
  data: elsewhere
  where: IBL data, AWS Open Data registry ibl-reproducible-ephys; the paper does not name the
    nine recordings.
- id: supp10-11-simulated-drift
  statement: In MEArec simulations mimicking the IBL recordings, DREDge and Kilosort both track
    the simulated motion accurately, with DREDge better under discontinuous bump drift.
  source: Results, Estimating motion in acute mouse recordings, paragraph 4; Supplementary Figs. 10
    and 11
  quote: DREDge and KS accurately tracked simulated motion ( Supplementary Figs. 10 and 11 ), with
    DREDge showing improvements
  data: elsewhere
  where: MEArec simulations generated with github.com/cwindolf/mearec_drift_simulations.
- id: supp12-subsetted-channels
  statement: When the NP1 and NP2 recordings of Fig. 5a are subsetted to the 282 um span of the
    Ultra probe, DREDge improves over Kilosort as in the NP Ultra data.
  source: Results, Estimating motion in acute mouse recordings, paragraph 4; Supplementary Fig. 12
  quote: we spatially subsetted the channels of the NP1 and NP2 recordings of Fig. 5a to fit inside
    the 282-μm span of the Ultra probe and found similar improvements of DREDge over KS
  data: elsewhere
  where: Figshare doi:10.6084/m9.figshare.14024495.v1.
- id: fig6cd-chronic-clusters
  statement: In a chronic NP2 recording (AL032, shank 1), clusters isolated on DREDge-corrected
    positions have well-stereotyped waveforms across sessions, while the Kilosort estimate gives
    them drifting, jumpy trajectories, evidence that DREDge tracks the probe more accurately.
  source: Results, Estimating motion in chronic mouse recordings, paragraph 2; Fig. 6c and 6d;
    Supplementary Fig. 16
  quote: This provided evidence that DREDge was tracking the probe trajectory more accurately
    than KS.
  data: elsewhere
  where: Chronic NP2.4 recording AL032 of ref. 6; the Data availability gives no deposit for it.
checks:
- date: 2026-10-21
  kind: agent
  model: claude-opus-5-5
  ready: true
  changes:
  - Opening comment, pipeline step 1. Spike detection and localization were a standard choice with a variant, but the Methods leave them open per data source and they set every spike position used later; made them readings (i) and (ii), included in every combination of readings.
  - edf3a-ap-dredge-slow-trend. Criterion now requires agreement across the step 1 readings as well as the step 2 readings, and "not reproduced" now reads "under all".
  - edf3c-spline-subsecond. The criterion presented the scrambled control as the paper's own; the paper uses it for ISI violations in Fig. 2e, not for this panel, and gives no permutation unit. Said so, and named the 0.4 s permutation bin, 100 permutations and 5% level as choices of the file.
  - edf3de-spline-improves-registration. The panel e measure (within-cluster s.d.) is not in the paper; said so and noted that the spline is fit to minimize it. Noted that the 1 s template correlation bins cannot resolve sub-second motion and added a 0.1 s variant that does not enter the outcome.
  - fig2-sorted-units. The where named ref. 13 only; the paper places the result in one of the N > 20 human cortical recordings without naming it, so all human deposits are named. Added a criterion for the bound "more than 500".
  - fig6e-chronic-jumps. The paper does not say whether the 0.5 to 22.2 range is over datasets or sessions; named both readings.
  - Added claims fig2c-lfp-tracking-clusters, edf4a-nonrigid-human, supp2-rat-spike-tracking, fig2fg-unit-spatial-spread, edf6-128-channel, fig3gh-iids, fig4f-insertion-anatomy, fig5a-imposed-zigzag, edf4d-nonrigid-ibl, supp10-11-simulated-drift, supp12-subsetted-channels and fig6cd-chronic-clusters, findings of the Results with no claim. All use data elsewhere.
  - Open, not settled. The Results and the Fig. 2b legend place the spline method in a human recording, while the Methods and Data availability place Extended Data Fig. 3 in the macaque recording of this dandiset. The file follows the Methods and Data availability for the Extended Data Fig. 3 claims.
  - Open, not settled. The Extended Data Fig. 3 claims rest on panels with no number or test; their criteria use the paper's template correlation where it applies, but the spline measures and thresholds (edf3b at least two clusters, edf3c scrambled control, edf3de panel e) are the file's readings, and edf3c and edf3de panel e are close to circular.
  - Open, not settled. Fig. 3e gives the Kruskal-Wallis P as < 0.0000001 in the legend and < 0.000001 in the Results; the Results value is recorded.
  - Open, not settled. The Extended Data figure images and the supplement PDF were not read; panel-level details (cluster count in Extended Data Fig. 3b, snippet length) could not be checked.
EOF
python tools/claims_check.py claims/001290/10.1038-s41592-025-02614-5.yaml paper/10.1038-s41592-025-02614-5.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
f=claims/001290/10.1038-s41592-025-02614-5.yaml; timeout 60 python3 - "$f" <<'EOF'
import re,sys
f=sys.argv[1]; t=open(f).read()
i=t.index('- id: fig2c-lfp-tracking-clusters'); j=t.index('\nchecks:')
a=t[i:j]
a=re.sub(r',\n?\s*paragraph \d+;', ';', a)
a=a.replace("""  where: Human recording of participant Pt03 (ref. 13), Dryad doi:10.5061/dryad.d2547d840 and
    DANDI:000397.""","""  where: Human recording of participant Pt03; the paper does not say which deposit holds it
    (human data at Dryad doi:10.5061/dryad.d2547d840, DANDI:000397 and Dryad
    doi:10.7272/Q6ST7N3B).""")
t=t[:i]+a+t[j:]
open(f,'w').write(t)
EOF
grep -n "paragraph\|Pt03;" $f | tail -20; python tools/claims_check.py $f paper/10.1038-s41592-025-02614-5.txt; git status --short
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -n '/id: fig2c-lfp/,/^checks:/p' claims/001290/*.yaml | grep -A2 "source:"
```

```
source: Results, DREDge rescues spike sorting and LFP features in human brain activity; Fig. 2c
  quote: Offsetting spike positions to compensate for the tracked motion revealed isolated
    clusters of spike activity ( Fig. 2c(ii , iii )).
--
  source: Results, DREDge rescues spike sorting and LFP features in human brain activity; Extended Data Fig. 4a and 4c
  quote: it led to visible improvements in the stability of spiking activity over rigid
    correction, as well as improvements in a metric of spike activity stability
--
  source: Results, DREDge rescues spike sorting and LFP features in human brain activity; Supplementary Fig. 2
  quote: were dominated by global slow-wave activity, leading to an artifactually oscillatory
    motion estimate; however, spike-based tracking was stable in this case.
--
  source: Results, DREDge rescues spike sorting and LFP features in human brain activity; Fig. 2f and 2g; Extended Data Fig. 5b
  quote: the spatial distribution of voltages in each unit was more concentrated with higher
    amplitudes with this correction
--
  source: Results, DREDge rescues spike sorting and LFP features in human brain activity; Extended Data Fig. 6
  quote: In three such recordings, DREDge’s tracking yielded stabilized spike rasters after motion
    correction of spike locations
--
[... 27 more lines not kept]
```

**Agent**

The claims file for DANDI:001290 is ready for an attempt. It is at `claims/001290/10.1038-s41592-025-02614-5.yaml`, and nothing was committed.

**Checker result:** `34 claims, 34 quotes, 14 statistical values, 0 problems`. Before my changes it read 22 claims and 13 values, also with 0 problems.

**Changes, by claim:**
- **Opening comment, pipeline step 1:** spike detection and localization were listed as a "standard choice" with a variant. The Methods leave this open for each data source, and it sets every spike position used later, so these are now readings (i) and (ii), and every combination of readings includes both.
- **edf3a-ap-dredge-slow-trend:** the criterion now requires the result to hold under the step 1 readings as well as the step 2 ones.
- **edf3c-spline-subsecond:** the criterion called its scrambled-trace control "the paper's own". The paper uses that control only for ISI violations in Fig. 2e. The 0.4 s permutation bin, 100 permutations and 5% level are now stated as the file's own choices.
- **edf3de-spline-improves-registration:** the panel e measure (spread of corrected depth within each cluster) is not in the paper. I said so and noted that the spline is fit to minimize it. The paper's 1 s raster bins cannot show sub-second motion, so I added a 0.1 s variant that only gets reported and does not decide the outcome.
- **fig2-sorted-units:** the data location named only ref. 13. The paper puts this result in an unnamed one of its N > 20 human recordings, so all human deposits are now named. I also added a criterion for the bound "more than 500".
- **fig6e-chronic-jumps:** the paper does not say whether the 0.5 to 22.2 range is over datasets or sessions, so both readings are named.
- **12 claims added** for findings in the Results that had none. All of them use data held elsewhere: fig2c-lfp-tracking-clusters, edf4a-nonrigid-human, supp2-rat-spike-tracking, fig2fg-unit-spatial-spread, edf6-128-channel, fig3gh-iids, fig4f-insertion-anatomy, fig5a-imposed-zigzag, edf4d-nonrigid-ibl, supp10-11-simulated-drift, supp12-subsetted-channels, fig6cd-chronic-clusters.

The pipeline parameters in the opening comment, the quotes, the statistics and the expected values of the other claims match the paper.

**Still open (recorded in `checks`):**
- **Which recording:** the Results and the Fig. 2b legend place the spline method in a human recording. The Methods and Data availability place Extended Data Fig. 3 in the macaque recording held in this dandiset. The file follows the Methods and Data availability.
- **Extended Data Fig. 3 claims:** the paper gives no number or test for these panels. The thresholds for the spline steps are the file's own readings, and two of the measures are close to circular, so they will tend to pass by construction.
- **Fig. 3e p-value:** the legend and the Results disagree (< 1e-7 against < 1e-6). The Results value is recorded.
- **Not read:** the Extended Data figure images and the supplement PDF, so panel details such as the cluster count in Fig. 3b and the snippet length could not be checked.

The `checks` entry is set to `ready: true`.

## End of run

24 turns, 109 minutes, result: success.
