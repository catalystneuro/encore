# 001687 · claims-check · run 39639772730

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
ls claims/001687/ paper/; grep -n "Reader" -A60 docs/protocol.md | head -150
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -n 96,200p docs/protocol.md; python tools/claims_check.py claims/001687/10.1016-j.neuron.2026.05.027.yaml paper/10.1016-j.neuron.2026.05.027.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
wc -l claims/001687/*.yaml paper/*.txt; git log --oneline -5 -- claims/001687
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "claims/001687/10.1016-j.neuron.2026.05.027.yaml"
}
```

```
1	# Claims for Xiao, Severson et al. (2026), "Peri-head distance coding in the mouse brainstem",
2	# Neuron, doi:10.1016/j.neuron.2026.05.027, on dandiset 001687.
3	#
4	# Written by an agent (model "claude-opus-5-5", Claude Code in GitHub Actions), 2026-10-21,
5	# protocol pilot-10 as stated in docs/protocol.md.
6	#
7	# Text read: the accepted author manuscript in PubMed Central (NIHMS2191201, PMC13336321), as
8	# fetched 2026-10-20 into paper/10.1016-j.neuron.2026.05.027.txt: main text, STAR Methods, the
9	# legends of Figures 1 to 6, and the supplement file NIHMS2191201-supplement-1.pdf (legends of
10	# Figures S1 to S6 and Tables S2 to S5). The version of record was not read. Tables S1 (mouse
11	# sex, age and figure assignments) and S6 (test statistics, degrees of freedom and p-values of
12	# all analyses) are named in the text but are not in the supplement file read; every number
13	# used below is in the main text, the legends or Tables S2 to S5. Figures were not opened.
14	#
15	# Code read: github.com/wanglab-neuro/2026_Xiao-Severson_Peri-head-distance at commit b1a9f3c
16	# (2026-08-21; archived as doi:10.5281/zenodo.20330279). It holds the original MATLAB scripts
17	# for Figures 1E, 2, 3, 4B-C, 5C-E, 6D, 6G-I, S1, S4I and S5A ("Manuscript figures/Original
18	# Matlab code"), Python helpers that read the deposited NWB files, the Python circuit model
19	# (PrV_simulation/simulate_prv.py), and a submodule (Processing, the spike-sorting pipeline;
20	# not read). The helper generate_deposition_tables.py reads, per NWB unit, the columns
[... 999 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "paper/10.1016-j.neuron.2026.05.027.txt"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "claims/001687/10.1016-j.neuron.2026.05.027.yaml",
 "offset": 1019
}
```

```
1019	  - quantity: proximity units becoming map
1020	    value: 2
1021	    tolerance: 0.2
1022	  criterion: >-
1023	    As fig4c-map-units-after-cut. Gain is not defined in the paper. Readings for lower or higher
1024	    gain: (a) the unit's peak mean wall rate in the single-whisker condition below or above that
1025	    in the full-array condition; (b) its mean wall rate over distances below or above. Reproduced
1026	    when all five counts are within tolerance under one reading.
1027	- id: figs5fg-cut-decoding
1028	  statement: >-
1029	    Whisker cutting lowers population decoding accuracy in both map (31.0 to 21.5%) and proximity
1030	    (24.1 to 20.2%) populations of 21 units, with the largest decreases at intermediate and far
1031	    distances in the map population and less effect at the closest distances.
1032	  source: Results, PrV map tuning can persist, paragraph 5; Figure S5F-G
1033	  quote: >-
1034	    Whisker cutting reduced overall decoding accuracy in both populations (map: 31.0 ± 0.10% vs.
1035	    21.5 ± 0.08%; proximity: 24.1 ± 0.82% vs. 20.2 ± 1.22%; mean ± 95% CI for full-array vs.
1036	    single-whisker conditions), with the largest decreases occurring at intermediate and far
1037	    distances in the map population
1038	  depends_on:
[... 450 more lines not kept]
```

**Agent**

The checker passes (41 claims, 0 problems). Now reading the Methods and legends to check each claim.

**Agent calls Bash**

```bash
python3 -c "
t=open('paper/10.1016-j.neuron.2026.05.027.txt').read()
print(t[50000:95000])"
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
python3 -c "
t=open('paper/10.1016-j.neuron.2026.05.027.txt').read()
import textwrap
s=t[51500:162401]
print('\n'.join(textwrap.wrap(s,200)))" > $TMPDIR/p.txt; wc -l $TMPDIR/p.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/p.txt"
}
```

```
1	zontal position (in 2-mm steps, relative to the closest position) of the stepper motor controlling the wall’s mediolateral position. High-Speed Videography High-speed whisker videos (688 × 688 pixels
2	at 500 Hz) were acquired with a machine-vision camera (Basler acA1300–200um) controlled by custom Python software (CamPy 50 ). Illumination was provided by a 940 nm LED (Roithner Lasertechnik)
3	collimated with a condenser lens and diffused to form an even backlight. The whiskers appeared in silhouette against this background and were imaged via a front-surface mirror into a 0.25× telecentric
4	lens (Edmund Optics). Frame timing was triggered by a Teensy microcontroller, and TTL pulses were recorded alongside electrophysiology to synchronize spikes and video. Awake and Anesthetized Wall-
5	Passing Recordings In a subset of mice (N = 4), high-speed video was continuously acquired during the wall-passing paradigm under both awake and anesthetized conditions. Mice were head-fixed
6	throughout, keeping their position constant relative to the moving wall stimulus. To enable whisker tracking, all whiskers except a single row (C1–C4 and γ or β) were trimmed. While awake, each mouse
7	experienced wall passes with randomized wall distances (7–23 mm in 2mm increments), repeated for 20 passes per distance. Following the awake session, the same animals were anesthetized via
8	intraperitoneal injection of a fentanyl-based cocktail (0.05 mg/kg fentanyl, 5 mg/kg midazolam, 0.5 mg/kg dexmedetomidine). After a 10-minute induction period, the same wall-passing protocol was
9	repeated under anesthesia. Comparisons between awake and anesthetized conditions were performed within-subject across matched wall distances. Electrophysiology Recording: Silicon Probe Following
10	habituation to the wall-passing paradigm, mice were head-fixed and allowed to run on the treadmill. The craniotomy was exposed and covered with artificial cerebrospinal fluid (aCSF). For wild-type and
11	TeLC experimen
[... 229 more lines not kept]
```

**Agent calls Grep**

```json
{
 "pattern": "Figure 1\\.|Supplemental|Table S2|Figure S",
 "path": "/tmp/claude-1001/p.txt",
 "output_mode": "count"
}
```

```
/tmp/claude-1001/p.txt:16

Found 16 total occurrences across 1 file.
```

**Agent calls Bash**

```bash
grep -n -m3 "Figure 1\. \|FIGURE\|Figure Legends\|Figure S1\." $TMPDIR/p.txt | head
```

```
281:. 57. Watkins PV , and Barbour DL ( 2011 ). Rate-level responses in awake marmoset auditory cortex . Hear. Res 275 , 30 – 42 . doi: 10.1016/j.heares.2010.11.011 . 21145961 PMC3095711 Figure 1. Acute
401:Anesthetized 15 0 10 5 -.0015 -.001 -.0005 0 Δĸ (mm-1) Δĸ (mm-1) Δĸ (mm-1) -.0015 -.001 -.0005 -.001 -.0005 Figure S1. Wall-passing stimulus induced minimal active whisker retraction, Related to
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/p.txt",
 "offset": 281,
 "limit": 285
}
```

```
File content (27890 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/p.txt",
 "offset": 281,
 "limit": 140
}
```

```
281	. 57. Watkins PV , and Barbour DL ( 2011 ). Rate-level responses in awake marmoset auditory cortex . Hear. Res 275 , 30 – 42 . doi: 10.1016/j.heares.2010.11.011 . 21145961 PMC3095711 Figure 1. Acute
282	PrV recordings in a wall-passing paradigm (A) Conceptual illustration showing how whiskers map peri-head space in head-centered coordinates. (B) Left, schematic of a hypothetical brainstem circuit to
283	compute non-monotonic distance code. Two TG neurons (A and B, red) with different distance sensitivities project to the brainstem: neuron A provides excitatory input to a PrV output neuron (C, black),
284	whereas neuron B synapses onto an inhibitory neuron (blue) in the trigeminal brainstem complex. Middle, tuning curves for neurons A and B; the shaded region indicates the difference between their
285	distance-tuning profiles. Right, linear summation yields a non-monotonic tuning curve in neuron C, with a peak at an intermediate peri-head distance. (C) Left, Schematic of the experimental setup.
286	Head-fixed mouse on a treadmill with a wall moving from anterior to posterior past the mouse’s face. Wall distance from the face was randomly varied between 7–23 mm in 2-mm increments on each pass.
287	Each recording contains 15–20 repetitions per distance. Right, Example video frame showing multiple whiskers contacting the wall (moving left to right). Red arrow indicates measured distance between
288	face and wall. (D) Example coronal brain section (4.8 mm posterior to Bregma) showing two silicon probe tracks through PrV labeled with DiI (red); cell bodies stained with Nissl (blue). (E) Example
289	extracellular voltage trace from one recording session. Colored bars indicate wall-passing periods. Figure 2. PrV contains multiple neural codes for peri-head distance (A) Example spike rasters of six
290	PrV single units during repeated wall passes. Each row is one wall pass, and each dot indicates a 50 ms bin containing at least one spike, colored by wall distance. Wall p
[... 130 more lines not kept]
```

**Agent**

Reading the supplement legends and tables next.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/p.txt",
 "offset": 421,
 "limit": 145
}
```

```
421	touch 5 sec 0.5 mV F Population Tuning Heatmap 6 12 18 Wall distance (mm) 9 15 39 0 0 10 20 30 40 0 2 4 6 8 10 12 Time (s) 0 20 40 60 80 Firing rate (sp/s) 8 10 12 14 18 Wall distance (mm) Firing rate
422	(z-score) 0 20 40 60 20 40 60 1 1 Units (far    close) Normalized firing rate 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 Wall distance (mm) E Firing rate (sp/s) Firing rate (z-score) 0 2 4 6 8 10 12 Time
423	(s) 5 8 11 14 17 Wall distance (mm) 8 9 10 11 12 13 14 15 16 17 18 19 Wall distance (mm) 16 Wall distance Wall-Passing Paradigm 4 20 mm 1 mm PrV Example PrV Responses N = 14 mice  === page 4 ===
424	Figure S3. Spike sorting quality metrics, Related to STAR Methods (A) Inter-spike-interval (ISI) histograms for the example units in Figure 2A-C. The grey shaded region indicates ±  0.8 ms refractory
425	period. Insets show the corresponding mean spike waveforms; shaded areas represent ± STD.  Scale bars: 0.5 ms (horizontal), 0.25 mV (vertical).  (B) Scatter plot of waveform signal-to-noise ratio
426	(SNR) versus ISI false alarm (FA) rate for wild-type dataset  collected with silicon probes (WT-Si Probe; n = 1358 total units). The area within the grey square contains accept- able units with SNR >
427	5 and false alarm rate < 2% (n = 1301 units from 36 mice).  (C) Z-scored waveforms of a subset of acceptable units from the WT-Si Probe dataset (n = 100 waveforms  shown).  (D) Histogram of spike
428	widths of all acceptable units from the WT-Si Probe dataset.  (E) Scatter plot of spike widths, in ms, versus mean firing rate, in spikes per second, for baseline periods (prior to  wall pass) of
429	acceptable units.  (F-I) Same as (B-E), but for tetanus toxin (TeLC) dataset (n = 665 total units from 11 mice; n = 631 acceptable  units in green shaded area).  (J-M) Same as (B-E), but for tungsten
430	dataset (n = 46 total units from 14 mice; n = 46 acceptable units in grey  shaded area; n = 46 waveforms shown in K). 0 6000 A B C D <10 -4 10 -2 1 FA rate (%) 0 15 SNR Wavefor
[... 134 more lines not kept]
```

**Agent calls Bash**

```bash
git show c7a5b6b3 --stat | head; git show c7a5b6b3 -- claims/ | grep -A40 "^+checks" | head -60; git diff c7a5b6b3 d9fa3acc --stat
```

```
commit c7a5b6b387ce09bdb6cf9cbcaee1bb877a34ca9d
Author: github-actions[bot] <github-actions[bot]@users.noreply.github.com>
Date:   Wed Oct 21 09:19:52 2026 +0000

    Agent run on 001687: claims-check (success)
    
    Run: https://github.com/catalystneuro/reproduction-registry/actions/runs/39575826299
    
    Account: unverified

 claims/001687/10.1016-j.neuron.2026.05.027.yaml | 1487 +++++++++++++++++++++++
 transcripts/001687/claims-report.md             |   49 +-
 transcripts/001687/claims.md                    |  831 ++++++++++---
 3 files changed, 2187 insertions(+), 180 deletions(-)
```

**Agent calls Bash**

```bash
timeout 30 git ls-remote https://github.com/wanglab-neuro/2026_Xiao-Severson_Peri-head-distance 2>&1 | head -5
```

```
b1a9f3cfacf6b0b9673df82b92f58a93290eb997	HEAD
b1a9f3cfacf6b0b9673df82b92f58a93290eb997	refs/heads/main
909a8f0d1f51b2f6982efcd851f3e6311fc84ef0	refs/tags/2026-paper-v1
```

**Agent**

The code repository is reachable, so I'll clone it to verify the code details the claims cite.

**Agent calls Bash**

```bash
cd $TMPDIR && timeout 120 git clone -q https://github.com/wanglab-neuro/2026_Xiao-Severson_Peri-head-distance code && cd code && git log --oneline -3 && find . -name "*.m" -o -name "*.py" | grep -v Processing | head -60
```

```
b1a9f3c Fix formatting in README.md
0468a9d Add link to published paper in README
6c4b217 Update DOI link in README.md
./materials/__init__.py
./PrV_simulation/simulate_prv.py
./PrV_simulation/plot_figures.py
./PrV_simulation/analysis.py
./PrV_simulation/__init__.py
./Manuscript figures/plot_figure2_from_nwb.py
./Manuscript figures/generate_deposition_tables.py
./Manuscript figures/Original Matlab code/figS5A.m
./Manuscript figures/Original Matlab code/FigS4I_probemap.m
./Manuscript figures/Original Matlab code/FigS1_Stats.m
./Manuscript figures/Original Matlab code/FigS1_Code.m
./Manuscript figures/Original Matlab code/Fig6GHI_right_model_TC_shape_analysis.m
./Manuscript figures/Original Matlab code/Fig6GHI_left_TC_shape_analysis.m
./Manuscript figures/Original Matlab code/Fig6D_Model_Heatmap.m
./Manuscript figures/Original Matlab code/Fig5D_TeLC_Pref_Dist_CDF.m
./Manuscript figures/Original Matlab code/Fig5CE_TeLC_heatmap_stacked_bar.m
./Manuscript figures/Original Matlab code/Fig4BC_WhiskerCutting_pairwise_FR_PrefDist.m
[... 7 more lines not kept]
```

**Agent calls Bash**

```bash
cd "$TMPDIR/code/Manuscript figures/Original Matlab code" && wc -l *.m && grep -n -i "fdr\|signrank\|low_fir\|lowfir\|< *1\b\|alpha\|tail" Fig2DEF_Pop_Heatmap_Hist_Pie.m | head -80
```

```
28 Fig1E_plot_raw_trace.m
   203 Fig2A_Example_Rasters.m
   189 Fig2B_Example_SDF_PSTHs.m
  1059 Fig2C_Example_Tuning_Curves.m
   843 Fig2DEF_Pop_Heatmap_Hist_Pie.m
   883 Fig3ABC_Decoder_Accuracy_Time_Confusion_Avg.m
   636 Fig4BC_WhiskerCutting_pairwise_FR_PrefDist.m
   963 Fig5CE_TeLC_heatmap_stacked_bar.m
   164 Fig5D_TeLC_Pref_Dist_CDF.m
    67 Fig6D_Model_Heatmap.m
   598 Fig6GHI_left_TC_shape_analysis.m
   572 Fig6GHI_right_model_TC_shape_analysis.m
  1061 FigS1_Code.m
   393 FigS1_Stats.m
   162 FigS4I_probemap.m
    69 figS5A.m
  7890 total
36:dataTable.low_firing = cellfun(@(b,w) max(b) < threshold_stats & mean(w) < threshold_stats, ...
39:included_units = sst.acceptable & ~dataTable.low_firing;
50:alpha = 0.05;
[... 39 more lines not kept]
```

**Agent calls Bash**

```bash
cd "$TMPDIR/code/Manuscript figures/Original Matlab code" && sed -n 20,60p Fig2DEF_Pop_Heatmap_Hist_Pie.m && sed -n 100,340p Fig2DEF_Pop_Heatmap_Hist_Pie.m
```

```
dataTable = matfile(fullfile(settings.data_folder, 'tuningTable_PrV.mat')).dataTable;
dataTable_cut = matfile(fullfile('E:\PrV_Wall_Recordings\Analysis\IntermediateData\Whisker_Cutting_naive\tuningTable_PrV.mat')).dataTable;
dataTable_one = matfile(fullfile('E:\PrV_Wall_Recordings\Analysis\IntermediateData\One_Whisker_naive\tuningTable_PrV.mat')).dataTable;
dataTable = cat(1, dataTable, dataTable_cut(:,1:size(dataTable,2)), dataTable_one(:,1:size(dataTable,2))); % only take columns without condition labels
clear dataTable_cut dataTable_one

% Load spike stats table (1358 units)
sst = matfile(fullfile(settings.wv_stats, 'PrV_spike_stats_table_naive.mat')).sst;

%% Prerequisite in Figure 2: Run stats for naive full array condition

rng('Default')
rng(42)

% Define units to be included
threshold_stats = 1; % 1.0; % mean baseline or wall fr, in Hz
dataTable.low_firing = cellfun(@(b,w) max(b) < threshold_stats & mean(w) < threshold_stats, ...
    dataTable.fr_mean, dataTable.fr_base_mean, 'Uni',1);

included_units = sst.acceptable & ~dataTable.low_firing;
[... 263 more lines not kept]
```

**Agent**

Several code details need checking against the repo (decoder CV, whisker-cutting rates, Fig 5D masks, model defaults).

**Agent calls Bash**

```bash
cd "$TMPDIR/code/Manuscript figures/Original Matlab code" && grep -n -i "num_cv\|cv_splits\|zscore\|normaliz\|num_resample\|summary_period\|ranksum\|mafdr\|shuffle\|118\|36\b\|82\b\|err_by" Fig3ABC_Decoder_Accuracy_Time_Confusion_Avg.m | head -60
```

```
115:shuffled_pop = proximity_pop | map_pop;
122:disp(['Shuffled: ' num2str(sum(shuffled_pop))])
124:% 592 untuned, 263 proximity, 139 map, 102 suppressed, 402 shuffled
127:population_names = {'untuned', 'proximity', 'map', 'mixed', 'suppressed', 'shuffled'};
139:    find(shuffled_pop), ...
156:mixed_map_size = 36;
157:mixed_prox_size = 82;
165:% population_names = {'untuned', 'proximity', 'map', 'mixed', 'suppressed', 'shuffled'};
192:            % If shuffled control, shuffle the trial data with respect to stimulus ID
193:            if strcmp(population_names{p}, 'shuffled')
231:% p = 'untuned'; % 'mixed'; % 'suppressed'; % 'map'; % 'proximity'; % 'shuffled'; % 
245:population_names = {'untuned', 'proximity', 'map', 'mixed', 'suppressed', 'shuffled'};
277:        num_cv_splits = 15; % 15*9 = 135
284:        ds = basic_DS(binned_format_file_name, specific_label_name_to_use, num_cv_splits);
286:        % Create feature preprocessor to z-score normalize each neuron
289:        the_feature_preprocessors{1} = zscore_normalize_FP;
300:        the_cross_validator.num_resample_runs = 5;
321:population_names = {'Untuned', 'Proximity', 'Map', 'Mixed', 'Suppressed', 'Shuffled'}; % (mixed = map + ambiguous?)
324:n = '118'; % number of units in smallest population to subsample
333:    ['DECODING_RESULTS_' rundate '_Binned_Wenxi_PrV_9dist_raster_data_150ms_bins_50ms_sampled_shuffled_' n 'units']};
[... 27 more lines not kept]
```

**Agent calls Bash**

```bash
cd "$TMPDIR/code/Manuscript figures/Original Matlab code" && sed -n 95,125p Fig3ABC_Decoder_Accuracy_Time_Confusion_Avg.m; sed -n 185,200p Fig3ABC_Decoder_Accuracy_Time_Confusion_Avg.m; grep -n "fr_wall\|fr_base\b\|fr_base =\|signrank\|mafdr\|alpha\|median\|activated_tuned_mask\|silenc" Fig4BC_WhiskerCutting_pairwise_FR_PrefDist.m | head -50
```

```
filename = 'naive_proximity_map_population_mixed.mat';
datetoday = '20251207';

% Load tables for indexing units
sst = matfile('E:\PrV_Wall_Recordings\WaveformStats_naive\PrV_spike_stats_table_naive.mat').sst;
t = matfile('E:\PrV_Wall_Recordings\Analysis\IntermediateData\tuningTable_PrV_anova.mat').dataTable;
t_mask = t(t.wallResp & sst.acceptable & ~t.low_firing,:); % 1141 with acceptable spike stats

activated = shiftdim(t_mask.activated & t_mask.wallTuned); % 383/1140 tuned and activated
suppressed = shiftdim(t_mask.suppressed & t_mask.wallTuned);
proximity = strcmp(t_mask.map, 'proximity');
map = strcmp(t_mask.map, 'map');
ambiguous = strcmp(t_mask.map, 'ambiguous');
untuned = strcmp(t_mask.map, 'untuned');

untuned_pop = untuned;
proximity_pop = activated & proximity;
ambiguous_pop = activated & ambiguous;
map_pop = activated & map & ~ambiguous;
shuffled_pop = proximity_pop | map_pop;
[... 77 more lines not kept]
```

**Agent calls Bash**

```bash
cd "$TMPDIR/code/Manuscript figures/Original Matlab code" && grep -n "mask1\|mask2\|kstest2\|pref" Fig5D_TeLC_Pref_Dist_CDF.m | head -20; grep -n "def \|default\|add_argument" "$TMPDIR/code/PrV_simulation/simulate_prv.py" | head -50
```

```
64:%% Panel D: Plot CDF comparing distribution of preferred wall distances Control vs. TeLC
68:[pref_distance, pref_distance_binned] = deal(cell(2,1));
70:% Get preferred wall distances for Control wall tuned and activated
73:mask1 = sst1.acceptable & ~dt1.low_firing & ~dt1.stats_err & dt1.activated; % sst1.mean_fr>1
74:[pref_distance{1}, pref_distance_binned{1}] = get_preferred_distance(mask1, dt1, dist_edges, dist_centers);
76:% Get preferred wall distances for TeLC wall tuned and activated
79:mask2 = sst2.acceptable & ~dt2.low_firing & ~dt2.stats_err & dt2.activated;
80:[pref_distance{2}, pref_distance_binned{2}] = get_preferred_distance(mask2, dt2, dist_edges, dist_centers);
86:data1 = pref_distance_binned{1}; % pref_distance{1}; % 
87:data2 = pref_distance_binned{2}; % pref_distance{2}; % 
119:[~,p,~] = kstest2(data1, data2, 'Tail','smaller');
136:function [pref_distance, pref_distance_binned] = get_preferred_distance(mask, dataTable, dist_edges, dist_centers)
140:    [pref_distance, pref_distance_binned] = deal(NaN(num_units,1));
160:        pref_distance(u) = actual_dist_centers(pd);
161:        pref_distance_binned(u) = dist_centers(pd);
17:def sigmoid(x, beta, theta):
25:def exponential_sampling(a, b, N, rate=5.0):
35:def PrV(x1, x, M1, M2, w1, beta1, beta2, theta1, theta2,
46:    def relu(x_):
67:def sample_discrete_exp_numpy(M, lambd):
[... 26 more lines not kept]
```

**Agent calls Bash**

```bash
cd "$TMPDIR/code/Manuscript figures/Original Matlab code" && grep -n -i "ttest\|mean_diff\|meandiff\|effect\|bonf\|0.0167\|sgolay\|segment\|arclength\|4 *mm\|mm_seg" FigS1_Stats.m FigS1_Code.m | head -30; grep -n -i "poly2\|poly3\|probe" FigS4I_probemap.m | head
```

```
FigS1_Stats.m:45:    'VariableNames', {'whiskerID','whiskerLabel','n_mice','meanDiff_awake_minus_anesth','t','df','p_two_sided','sig_Bonf'});
FigS1_Stats.m:59:        [~, p2, ci, stats] = ttest(Wi.awake, Wi.anesthetized);  % TWO-SIDED
FigS1_Stats.m:73:% Holm–Bonferroni across the 3 whiskers (two-sided p-values)
FigS1_Stats.m:74:% results.p_corrected = holm_bonferroni(p_all);
FigS1_Stats.m:78:results.sig_Bonf = results.p_two_sided < alpha;
FigS1_Stats.m:79:disp(results(:, {'whiskerLabel','p_two_sided','sig_Bonf'}))
FigS1_Stats.m:101:                      'meanDiff_awake_minus_anesth','t','df','p_two_sided','sig_Bonf'});
FigS1_Stats.m:123:        [~, p2, ~, stats] = ttest(Wi.awake, Wi.anesthetized);  % TWO-SIDED
FigS1_Stats.m:138:% Bonferroni across whiskers
FigS1_Stats.m:140:results.sig_Bonf = results.p_two_sided < alpha;
FigS1_Stats.m:143:disp(results(:, {'whiskerLabel','mean_awake','sem_awake','mean_anesth','sem_anesth','meanDiff_awake_minus_anesth','p_two_sided','sig_Bonf'}))
FigS1_Stats.m:231:% (Your Bonferroni flag remains valid for two-sided tests)
FigS1_Stats.m:233:results.sig_Bonf = results.p_two_sided < alpha;
FigS1_Stats.m:292:                      'meanDiff_awake_minus_anesth','t','df','p_two_sided','sig_Bonf'});
FigS1_Stats.m:314:        [~, p2, ~, stats] = ttest(Wi.awake, Wi.anesthetized);  % TWO-SIDED
FigS1_Stats.m:331:% Bonferroni across the 3 whiskers
FigS1_Stats.m:333:results.sig_Bonf = results.p_two_sided < alpha;
FigS1_Stats.m:336:                 'meanDiff_awake_minus_anesth','p_two_sided','sig_Bonf'}))
FigS1_Code.m:97:var = smoothdata(var, 1, 'sgolay',51, 'degree',3);
FigS1_Code.m:100:% var = smoothdata(var, 1, 'sgolay',51, 'degree',3);
[... 16 more lines not kept]
```

**Agent calls Bash**

```bash
cd "$TMPDIR/code/Manuscript figures/Original Matlab code" && sed -n 795,845p FigS1_Code.m
```

```
vars.theta_raw = session.whiskerData.theta(:,1:3);
    for w = size(vars.theta_raw, 2):-1:1
        % Interpolate NaN in theta
        nans = find(isnan(vars.theta_raw(:,w)));
        vars.theta_raw(nans,w) = interp1(1:numel(vars.theta_raw(:,w)), vars.theta_raw(:,w), nans, 'linear', NaN);
    end

    % Smooth theta a couple times to smooth over tracking errors, noise
    vars.theta_med = smoothdata(vars.theta_raw, 1, 'movmedian',5);
    vars.theta_smooth = smoothdata(vars.theta_med, 1, 'sgolay',21, 'degree',3);
    vars.theta_smooth = smoothdata(vars.theta_smooth, 1, 'sgolay',21, 'degree',3);

    vars.midpoint = smoothdata(vars.theta_smooth, 1, 'sgolay',101, 'degree',3);
    
%     % Re-calculate midpoint, amplitude, setpoint
%     for w = size(vars.theta_raw, 2):-1:1
%         % Get lower envelope
%         [pks, locs] = findpeaks(vars.theta_smooth(:,w));
%         vars.upper_envelope(:,w) = interp1(locs, pks, 1:numel(vars.theta_smooth(:,w)), 'linear', NaN);
%         [vals, locs] = findpeaks(-vars.theta_smooth(:,w));
[... 31 more lines not kept]
```

**Agent calls Bash**

```bash
python3 -c "
from scipy.stats import norm
import math
sd=math.sqrt(10*10*21/12); z=(50-0.5)/sd; print(2*norm.sf(z), norm.sf(z))"
```

```
Exit code 1
Traceback (most recent call last):
  File "<string>", line 2, in <module>
    from scipy.stats import norm
ModuleNotFoundError: No module named 'scipy'
```

**Agent calls Bash**

```bash
python3 -c "
import math
sd=math.sqrt(10*10*21/12); z=(50-0.5)/sd; print(math.erfc(z/math.sqrt(2)), math.erfc(z/math.sqrt(2))/2)"
```

```
0.00018267179110955043 9.133589555477521e-05
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001687/10.1016-j.neuron.2026.05.027.yaml",
 "old_string": "#   the pass's wall rate against its own baseline rate (Methods); the code corrects the nine\n#   p-values of each direction with Benjamini-Hochberg (BH-FDR) and uses q < 0.05. The Methods\n#   print only \"p < 0.05\"; uncorrected p < 0.05 is the variant reading. Wall-responsive means\n#   activated or suppressed.",
 "new_string": "#   the pass's wall rate against its own baseline rate, p < 0.05 (Methods, no correction named,\n#   while the same paragraph names BH-FDR for the tuning test). The code corrects the nine\n#   p-values of each direction with Benjamini-Hochberg (BH-FDR) and uses q < 0.05. Methods and\n#   code disagree, so the Methods' uncorrected p < 0.05 is the main reading, on which claims are\n#   judged, and the code's BH-FDR is the variant, shown. Wall-responsive means activated or\n#   suppressed."
}
```

```
The file claims/001687/10.1016-j.neuron.2026.05.027.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001687/10.1016-j.neuron.2026.05.027.yaml",
 "old_string": "    code leaves the number of distances to each session). Responsiveness is judged with the\n    code's BH-FDR across distances; uncorrected p < 0.05 per distance is the variant reading.\n    Reproduced when all four counts are within tolerance under one reading.",
 "new_string": "    code leaves the number of distances to each session). Responsiveness is judged with the\n    Methods' uncorrected p < 0.05 per distance; the code's BH-FDR across distances is the\n    variant, shown. Reproduced when all four counts are within tolerance under the Methods'\n    test."
}
```

```
The file claims/001687/10.1016-j.neuron.2026.05.027.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001687/10.1016-j.neuron.2026.05.027.yaml",
 "old_string": "    Classification as in the opening comment (code's BH-FDR across the nine distances; variant,\n    uncorrected p < 0.05). Reproduced when all four counts are within tolerance under one\n    reading.",
 "new_string": "    Classification as in the opening comment (Methods, uncorrected p < 0.05 per distance; variant,\n    the code's BH-FDR across the nine distances, shown). Reproduced when all four counts are\n    within tolerance under the Methods' test."
}
```

```
The file claims/001687/10.1016-j.neuron.2026.05.027.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001687/10.1016-j.neuron.2026.05.027.yaml",
 "old_string": "    Distance tuning as in the opening comment. Reproduced when all four counts are within\n    tolerance under one of the responsiveness readings. The 472",
 "new_string": "    Distance tuning as in the opening comment. Reproduced when all four counts are within\n    tolerance under the Methods' responsiveness test (the code's BH-FDR variant shown). The 472"
}
```

```
The file claims/001687/10.1016-j.neuron.2026.05.027.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001687/10.1016-j.neuron.2026.05.027.yaml",
 "old_string": "    Fig5CE_TeLC_heatmap_stacked_bar.m). Reproduced when all four values are within tolerance\n    under one responsiveness reading.",
 "new_string": "    Fig5CE_TeLC_heatmap_stacked_bar.m). Reproduced when all four values are within tolerance\n    under the Methods' responsiveness test (the code's BH-FDR variant shown)."
}
```

```
The file claims/001687/10.1016-j.neuron.2026.05.027.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001687/10.1016-j.neuron.2026.05.027.yaml",
 "old_string": "    printed; (b) the counts implied by fig2-distance-tuned-counts (184 and 112, same 10%\n    tolerance).",
 "new_string": "    printed; (b) the counts implied by fig2-distance-tuned-counts (184 and 112, same 10%\n    tolerance; the Methods also count 112 silicon-probe units as wall-responsive but not\n    distance-tuned, Characterizing Wall Distance Tuning)."
}
```

```
The file claims/001687/10.1016-j.neuron.2026.05.027.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001687/10.1016-j.neuron.2026.05.027.yaml",
 "old_string": "    the readings are the mean over the three whiskers and each whisker alone.",
 "new_string": "    the readings are the mean over the three whiskers and each whisker alone. The code\n    (FigS1_Code.m) takes the midpoint as a 101-frame Savitzky-Golay smoothing of the twice\n    21-frame-smoothed angle, with the envelope method commented out; this is the variant, shown,\n    and the Methods' envelope midpoint is the main."
}
```

```
The file claims/001687/10.1016-j.neuron.2026.05.027.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001687/10.1016-j.neuron.2026.05.027.yaml",
 "old_string": "    two summaries are the readings of \"larger ... at closer wall distances\"; the outcome is the\n    one both give.",
 "new_string": "    two summaries are the readings of \"larger ... at closer wall distances\"; the outcome is the\n    one both give. The cited panels (S1D and S1H, right) show one example C1 whisker in one\n    mouse; the across-mouse curves per whisker are in S1F and S1J, which this criterion uses."
}
```

```
The file claims/001687/10.1016-j.neuron.2026.05.027.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001687/10.1016-j.neuron.2026.05.027.yaml",
 "old_string": "    untuned groups, and a one-sided Wilcoxon rank-sum test on the 10 subsample values has p <\n    0.05 for each such pair, under",
 "new_string": "    untuned groups, and a two-sided Wilcoxon rank-sum test (MATLAB ranksum default, as in the\n    code; the Table S2 value 1.83e-4 is the two-sided normal-approximation p for complete\n    separation of 10 against 10) on the 10 subsample values has p < 0.05 for each such pair, under"
}
```

```
The file claims/001687/10.1016-j.neuron.2026.05.027.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001687/10.1016-j.neuron.2026.05.027.yaml",
 "old_string": "    n: 266 proximity and 118 map units\n  - about: proximity against map at 13, 15 and 17 mm",
 "new_string": "    n: 266 proximity and 118 map units\n  - about: proximity against map at 11 mm\n    test: Wilcoxon rank-sum test\n    p: 0.02\n    corrected: BH-FDR\n    n: 266 proximity and 118 map units\n  - about: proximity against map at 13, 15 and 17 mm"
}
```

```
The file claims/001687/10.1016-j.neuron.2026.05.027.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001687/10.1016-j.neuron.2026.05.027.yaml",
 "old_string": "    populations, the map population's drop summed over 11 to 23 mm exceeds its drop summed over 7\n    and 9 mm, and the four values",
 "new_string": "    populations, the map population's largest per-distance drop is at 11 mm or farther and its\n    mean drop per distance over 11 to 23 mm exceeds its mean drop over 7 and 9 mm, and the four\n    values"
}
```

```
The file claims/001687/10.1016-j.neuron.2026.05.027.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001687/10.1016-j.neuron.2026.05.027.yaml",
 "old_string": "    passes within each laser condition, (b) passes within each condition and distance. Tuning is\n    classified on laser-off passes at the five distances (7 to 23 mm in 4-mm steps). Reproduced\n    when the five counts are within tolerance under one reading and at least 12 of the\n    disinhibited tuned units have the same preferred distance with laser on as off; the paper\n    says all retained it but gives no number, so the share is reported.",
 "new_string": "    passes within each laser condition, (b) passes within each condition and distance. Tuning is\n    classified at the five distances (7 to 23 mm in 4-mm steps); the paper does not say on which\n    passes, so the readings are (i) laser-off passes and (ii) all passes. Reproduced when the\n    five counts are within tolerance under one reading and the disinhibited tuned units keep\n    their preferred distance with laser on as off; the paper says they retained it but gives no\n    number, so the readings are all of them and more than half of them, and the share is\n    reported."
}
```

```
The file claims/001687/10.1016-j.neuron.2026.05.027.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001687/10.1016-j.neuron.2026.05.027.yaml",
 "old_string": "    value: 4.74\n    tolerance: 2.68",
 "new_string": "    value: 4.74\n    tolerance: 2.71"
}
```

```
The file claims/001687/10.1016-j.neuron.2026.05.027.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001687/10.1016-j.neuron.2026.05.027.yaml",
 "old_string": "    per-unit mean baseline rates (-4.5 to 0 s, over all passes) between full-array and",
 "new_string": "    per-unit mean baseline rates (-4.5 to 0 s; the code averages the per-distance means) between full-array and"
}
```

```
The file claims/001687/10.1016-j.neuron.2026.05.027.yaml has been updated successfully.
```

**Agent**

Now the `checks` entry. Checking the format another file uses:

**Agent calls Bash**

```bash
grep -l "^checks:" claims/*/*.yaml | head -1 | xargs -I{} sh -c 'sed -n "/^checks:/,\$p" {} | head -20'
```

```
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
  - auc-weak-strong. The criterion compared groups on the Fig. 
[... 4 more lines not kept]
```

**Agent calls Bash**

```bash
cat >> claims/001687/10.1016-j.neuron.2026.05.027.yaml <<'EOF'
checks:
- date: 2026-10-21
  kind: agent
  model: claude-opus-5-5
  ready: true
  changes:
  - Opening comment. The Methods give the responsiveness test as one-tailed signed-rank at p < 0.05 with no correction, while the code applies BH-FDR across distances. The file made the code the main reading; protocol step 2 puts the Methods first, so the uncorrected test is now the main reading on which claims are judged and the code's BH-FDR is the variant, shown.
  - figs2-tungsten-responsiveness, fig2-wall-responsive-counts, fig2-distance-tuned-counts, telc-unit-yield. Judged under the Methods' responsiveness test, with the code's BH-FDR shown as a variant, following the change above. Claims that classify "as in the opening comment" follow it too.
  - fig2f-tuning-categories. Added that the Methods count 112 silicon-probe units as wall-responsive but not tuned, which supports reading (b).
  - figs1f-angle-awake-vs-anesthetized. Named the code's midpoint (FigS1_Code.m, 101-frame Savitzky-Golay smoothing, envelope method commented out) as a variant of the Methods' envelope midpoint.
  - figs1d-bending-larger-closer. Noted that the cited panels S1D and S1H show one example C1 whisker in one mouse and that the criterion uses the across-mouse curves of S1F and S1J.
  - fig3a-decoding-above-controls. The criterion used a one-sided rank-sum test. The code calls ranksum with its two-sided default, and the Table S2 value 1.83e-4 is the two-sided normal-approximation p for complete separation of 10 against 10. Changed to two-sided.
  - figs5c-single-neuron-decoders. Added the Table S4 test at 11 mm (p = 0.02), which the criterion requires but the statistics did not record.
  - figs5fg-cut-decoding. The criterion compared the map drop summed over seven distances (11 to 23 mm) with the drop summed over two (7 and 9 mm), which favours the far range by construction. It now compares mean drops per distance and requires the largest drop at 11 mm or farther ("largest decreases").
  - figs6-opto-local-inhibition-gain. Removed the threshold of 12 of 16 disinhibited units keeping their preferred distance, which is not in the paper. The readings are now all of them and more than half. Named as open whether tuning is classified on laser-off or on all passes, which the paper does not say.
  - figs6l-telc-increase-at-close-distances. The 7 mm tolerance was 2.68, the mean half-width of the CI. By the criterion's own rule (larger half of the CI [2.09, 7.45] around 4.74) it is 2.71. Corrected.
  - fig4-cut-baseline-unchanged. Noted that the code's per-unit baseline is the mean of per-distance means.
  - Checked the code details the file cites against the repository at b1a9f3c (classification and low-firing rule in Fig2DEF, decoder settings in Fig3ABC, cutting tests in Fig4BC, masks and kstest2 tail in Fig5D, model defaults in simulate_prv.py, Poly2 mask in FigS4I). They match the file.
  - Not settled. Figure 2F (119 suppressed-only, 177 untuned) cannot be reconciled with 472 + 213 - 29 = 656 tuned. Both readings stay in fig2f-tuning-categories, and the downstream claims use the paper's printed populations.
  - Not settled. Minor findings without a claim: the Figure S4M shifts of preferred distance across windows, the SVM error values of Table S3, and the receptive-field split of tungsten units (18 single-whisker, 28 multi-whisker). These are descriptive and judged not main findings.
  - Not settled. Tables S1 and S6 are named in the paper but absent from the supplement read; S6 may hold test details (tails, degrees of freedom) that the criteria now treat as open.
EOF
python tools/claims_check.py claims/001687/10.1016-j.neuron.2026.05.027.yaml paper/10.1016-j.neuron.2026.05.027.txt; grep -n ": .*: " claims/001687/*.yaml | grep -v "^\S*:[0-9]*:\s*#" | grep -v "quote\|>-" | head
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -i 's/^  - Not settled. Minor findings without a claim: the Figure/  - Not settled. Minor findings without a claim, the Figure/' claims/001687/10.1016-j.neuron.2026.05.027.yaml && python tools/claims_check.py claims/001687/10.1016-j.neuron.2026.05.027.yaml paper/10.1016-j.neuron.2026.05.027.txt && grep -c "—\|rather" claims/001687/*.yaml; git status --short
```

Result: not kept, because it reads the paper's text.

**Agent**

## Check of DANDI:001687 claims (doi:10.1016/j.neuron.2026.05.027)

**Checker result:** `41 claims, 41 quotes, 40 statistical values, 0 problems`. Before my edits it also had 0 problems, with 39 statistical values.

I read the main text, the Methods, the legends and the supplement. I also cloned the paper's code at commit b1a9f3c to check the details the file cites. The classification, decoder settings, whisker-cutting tests, Fig. 5D masks and test direction, model defaults and the Poly2 probe filter all match what the file says. Nothing is committed, and only `claims/001687/` was changed.

**Changes, by claim**
- **Opening comment, figs2-tungsten-responsiveness, fig2-wall-responsive-counts, fig2-distance-tuned-counts, telc-unit-yield:** The Methods test responsiveness at uncorrected p < 0.05, while the code applies a BH-FDR correction across distances. The file had made the code the main reading. The protocol puts the Methods first, so claims are now judged on the uncorrected test, and the code's result is shown as a variant. Every claim that classifies units by the opening comment follows this.
- **fig2f-tuning-categories:** Added that the Methods count 112 units as wall-responsive but not tuned. This supports reading (b).
- **figs1f-angle-awake-vs-anesthetized:** The code computes the midpoint angle by heavy smoothing (its envelope method is commented out). That is now named as a variant of the Methods' envelope midpoint.
- **figs1d-bending-larger-closer:** Noted that the cited panels show one example whisker in one mouse, and that the criterion uses the across-mouse panels S1F and S1J.
- **fig3a-decoding-above-controls:** Changed the rank-sum test from one-sided to two-sided. The code uses MATLAB's two-sided default, and Table S2's p = 1.83e-4 is exactly the two-sided value when 10 subsamples are fully separated from 10.
- **figs5c-single-neuron-decoders:** Added the 11 mm test (p = 0.02). The criterion requires it, but it was not recorded.
- **figs5fg-cut-decoding:** The criterion compared a drop summed over seven distances with one summed over two, which favours the far range by construction. It now compares mean drops per distance and requires the largest drop to be at 11 mm or farther.
- **figs6-opto-local-inhibition-gain:** Removed an invented threshold (12 of 16 units keeping their preferred distance). The readings are now "all of them" and "more than half". The paper does not say which passes the tuning is classified on (laser-off or all), so that is now named as open.
- **figs6l-telc-increase-at-close-distances:** The 7 mm tolerance was 2.68. By the criterion's own rule (the larger half of the confidence interval) it is 2.71.
- **fig4-cut-baseline-unchanged:** Noted that the code's per-unit baseline is the mean of the per-distance means.

**What remains open**
- Figure 2F's counts (119 suppressed-only, 177 untuned) cannot be reconciled with the 656 tuned units given in the text. Both readings stay in the claim.
- A few minor descriptive findings have no claim: the Figure S4M shifts in preferred distance across time windows, the SVM error values in Table S3, and the receptive-field split of the tungsten units. I judged none of them a main finding.
- Tables S1 and S6 are named in the paper but are not in the supplement that was read. Test details that may be in S6 stay open.

**Ready:** yes. The `checks` entry records `ready: true`.

## End of run

44 turns, 4 minutes, result: success.
