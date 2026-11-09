# 001687 · claims · run 39638075902

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cat docs/protocol.md; ls claims/001453/ claims/001687/ paper/ 2>&1; git log --stat -3 | head -40
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cat transcripts/001687/claims-report.md transcripts/001687/claims-check-report.md; head -60 paper/*.txt; wc paper/*.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd paper; head -30 *.txt; wc *.txt; pdfinfo *.pdf | head -20; pdftotext -layout *.supp.pdf $TMPDIR/supp.txt && wc $TMPDIR/supp.txt
```

```
Exit code 127
DOI: 10.1016/j.neuron.2026.05.027
Version: as served by ncbi_pmc
Source: ncbi_pmc+crossref (paper-text-fetcher)
Stored: 2026-10-20
Extracted: as fetched; with 1 supplement file(s) from PubMed Central, downloaded in a browser (PMC13336321), PDFs extracted with PyMuPDF (dehyphenated, NFKC), Word files with textutil
------------------------------------------------------------------------
pmc Neuron Neuron 319 nihpa 8809320 Neuron 0896-6273 1097-4199 pmc-is-collection-domain yes pmc-collection-title NIHPA Author Manuscripts PMC13336321 PMC13336321.1 13336321 13336321 NIHMS2191201 42349407 10.1016/j.neuron.2026.05.027 NIHMS2191201 NIHPA2191201 1 Article Peri-Head Distance Coding in the Mouse Brainstem Xiao Wenxi 1 2 5 Severson Kyle S. 1 2 5 Zheng Hao 1 2 3 Chen Ke 1 2 Thompson P. M. 1 2 Levy Manuel S. 1 2 Choi Seonmi 1 2 Zhao Shengli 4 Takatoh Jun 1 2 Prevosto Vincent 1 2 6 Wang Fan 1 2 3 6 7 1. McGovern Institute for Brain Research, MIT, Cambridge, MA 02139, USA 2. Department of Brain and Cognitive Sciences, MIT, Cambridge, MA 02139, USA 3. Yang Tan Collective, MIT, Cambridge, MA 02139, USA 4. Department of Neurobiology, Duke University, Durham, NC 27710, USA 5. Equal contribution 6. Address correspondence to [removed: an e-mail address] and [removed: an e-mail address] 7. Lead Contact AUTHOR CONTRIBUTIONS F.W. conceived the study. F.W., K.S.S, V.P., and W.X. designed the experiments. W.X. and K.S.S. performed all experiments. P.M.T. and V.P. trained W.X. in brainstem recordings. K.S.S. and V.P. developed analysis code. H.Z. implemented the brainstem circuitry simulation. K.C. and M.L. advised on data analysis. J.T. advised on viral constructs and injections. K.S.S., W.X., and V.P. analyzed the data. S.Z. generated GtACR and TeLC viruses. S.C. bred all animals. W.X., K.S.S, and F.W. wrote the manuscript with input from all authors. 25 6 2026 517084 S0896-6273(26)00419-8 27 06 2026 06 07 2026 07 07 2026 25 09 2026 This file is available for text mining. It may also be used consist
[... 4 more lines not kept]
```

**Agent calls Bash**

```bash
cd paper; wc *.txt; grep -n -o "Supplement[^ ]* [^ ]* [^ ]*" *.txt | head -30; awk '{print NR, length($0)}' *.txt | sort -k2 -n -r | head
```

```
2340  25759 164077 10.1016-j.neuron.2026.05.027.txt
7:Supplemental Figure S1
7:Supplemental Figure S1D
7:Supplemental Figure S1H
7:Supplemental Figure S1F
7:Supplemental Figure S2
7:Supplemental Figure S3J
7:Supplemental Figure S2D
7:Supplemental Figure S2E
7:Supplemental Figure S2F
7:Supplemental Figure S3A
7:Supplemental Figure S4I
7:Supplemental Figure S4A
7:Supplemental Figure S4B
7:Supplemental Figure S4B
7:Supplemental Figure S4C
7:Supplemental Figure S4D
7:Supplemental Figure S4G
7:Supplemental Figure S4E
7:Supplemental Figure S4F
[... 21 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 7p paper/*.txt | fold -s -w 4000 > $TMPDIR/main.txt; wc -l $TMPDIR/main.txt; sed -n '8,40p' paper/*.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  grep -n -v "^\[[0-9]*\]" paper/*.txt | grep -v "^[0-9]*:$" | sed -n '1,400p' | cut -c1-300 | head -150
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  grep -n "=== page\|^#####" paper/*.txt; awk 'length($0)>80{print NR": "$0}' paper/*.txt | sed -n '1,500p' | grep -v "^[0-9]*: \[[0-9]*\]" | cut -c1-200 | head -80
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/main.txt"
}
```

```
1	pmc Neuron Neuron 319 nihpa 8809320 Neuron 0896-6273 1097-4199 pmc-is-collection-domain yes pmc-collection-title NIHPA Author Manuscripts PMC13336321 PMC13336321.1 13336321 13336321 NIHMS2191201 42349407 10.1016/j.neuron.2026.05.027 NIHMS2191201 NIHPA2191201 1 Article Peri-Head Distance Coding in the Mouse Brainstem Xiao Wenxi 1 2 5 Severson Kyle S. 1 2 5 Zheng Hao 1 2 3 Chen Ke 1 2 Thompson P. M. 1 2 Levy Manuel S. 1 2 Choi Seonmi 1 2 Zhao Shengli 4 Takatoh Jun 1 2 Prevosto Vincent 1 2 6 Wang Fan 1 2 3 6 7 1. McGovern Institute for Brain Research, MIT, Cambridge, MA 02139, USA 2. Department of Brain and Cognitive Sciences, MIT, Cambridge, MA 02139, USA 3. Yang Tan Collective, MIT, Cambridge, MA 02139, USA 4. Department of Neurobiology, Duke University, Durham, NC 27710, USA 5. Equal contribution 6. Address correspondence to [removed: an e-mail address] and [removed: an e-mail address] 7. Lead Contact AUTHOR CONTRIBUTIONS F.W. conceived the study. F.W., K.S.S, V.P., and W.X. designed the experiments. W.X. and K.S.S. performed all experiments. P.M.T. and V.P. trained W.X. in brainstem recordings. K.S.S. and V.P. developed analysis code. H.Z. implemented the brainstem circuitry simulation. K.C. and M.L. advised on data analysis. J.T. advised on viral constructs and injections. K.S.S., W.X., and V.P. analyzed the data. S.Z. generated GtACR and TeLC viruses. S.C. bred all animals. W.X., K.S.S, and F.W. wrote the manuscript with input from all authors. 25 6 2026 517084 S0896-6273(26)00419-8 27 06 2026 06 07 2026 07 07 2026 25 09 2026 This file is available for text mining. It may also be used consistent with the principles of fair use under the copyright law. Peri-Head Distance Coding in the Mouse Brainstem 10 12 2025 2025.11.30.691334 bioRxiv 10.64898/2025.11.30.691334 PMC12822691 41573919 SUMMARY Perceiving the location of nearby objects relative to the body is essential for guiding movement and avoiding danger. Many organisms use touch to estimate object distance, yet how somatosensory cir
[... 13 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/main.txt",
 "offset": 15,
 "limit": 18
}
```

```
File content (25949 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/main.txt",
 "offset": 15,
 "limit": 9
}
```

```
15	sites were confirmed by post hoc histological analysis. Isolation of Single Unit Activity For silicon probe data, initial single-unit isolation (spike sorting) was performed using Kilosort2.5 51 , followed by manual curation in Phy 52 ( github.com/cortex-lab/phy ). Spike times and waveforms for isolated clusters were exported from Phy. Most units exhibited narrow spike widths, defined by a trough-to-peak latency of less than 0.4 ms. Duplicate units, identified as those with high Pearson’s correlation coefficients (> 0.1) in spike counts binned at 1 ms resolution, were excluded from further analysis. For tungsten electrode data, spike waveforms were extracted by thresholding high-pass filtered traces (500 Hz) and clustered using MClust-4.4 (A.D. Redish, http://redishlab.neuroscience.umn.edu/MClust/MClust.html ). Isolation quality was assessed using the following metrics: signal-to-noise ratio (SNR), defined as the mean waveform amplitude divided by the standard deviation (SD) of waveform noise; and false alarm (FA) rate, defined as the percentage of spikes with inter-spike intervals (ISI) shorter than 0.8 ms. Units with an SNR less than 5 SDs or an FA rate greater than 2% did not meet single-unit isolation quality criteria and were excluded from subsequent analyses. For silicon probe data, in wild-type mice, 1141 of 1358 units (36 mice), in TeLC experiments, 587 of 665 units (11 mice), and for Tungsten recordings (46 of 46 units (14 mice), passed isolation quality and minimum firing rate (>1 Hz) criteria and were subsequently entered into population analyses. For acute whisker-cutting experiments, only units demonstrating stable waveform properties both before and after cutting were included in analyses. Acute Whisker-Cutting Manipulation During sessions involving acute whisker cutting, neural responses were first recorded with the full whisker array intact. Each session included 15 to 20 repetitions of the same wall distance over approximately one hour. The whisk
[... 8 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/main.txt",
 "offset": 24,
 "limit": 9
}
```

```
24	preferring close distance, positive values indicating preferring far distance, and values near 0 indicating either symmetric edge responses or centrally peaked tuning. Supplementary Material 1 2 3 ACKNOWLEDGMENTS We thank Drs. Jennifer Groh, David Kleinfeld, Lindsey Glickfeld, John Pearson, and members of the Wang Lab for insightful discussions. We are grateful to Julia Dziubek, Ina Bando, He Jiang, Kai Ding, Nathalie Verlinde, Priyadarshini Dutta, and Gabrielle Sevrain for technical assistance and mouse colony maintenance. This work was supported by NS077986, DP1 NS137188, and a subcontract of U19NS137920 to F.W. K.S.S. was supported by F32MH122995. H.Z. is supported by K. Lisa Yang Integrative Computational Neuroscience Center fellowship. This is a PDF file of an unedited manuscript that has been accepted for publication. As a service to our customers we are providing this early version of the manuscript. The manuscript will undergo copyediting, typesetting, and review of the resulting proof before it is published in its final form. Please note that during the production process errors may be discovered which could affect the content, and all legal disclaimers that apply to the journal pertain. DECLARATION OF INTERESTS The authors declare no competing interests. SUPPLEMENTAL TABLE TITLES Table S1. Mouse Metadata and Figure Appearances, Related to STAR Methods Table S6. Statistics, Related to STAR Methods REFERENCES 1. Andersen RA , Snyder LH , Bradley DC , and Xing J ( 1997 ). Multimodal representation of space in the posterior parietal cortex and its use in planning movements . Annu. Rev. Neurosci 20 , 303 – 330 . 9056716 10.1146/annurev.neuro.20.1.303 2. Colby CL , and Goldberg ME ( 1999 ). Space and attention in parietal cortex . Annu. Rev. Neurosci 22 , 319 – 349 . doi: 10.1146/annurev.neuro.20.1.303 . 10202542 3. Avillac M , Denève S , Olivier E , Pouget A , and Duhamel JR ( 2005 ). Reference frames for representing visual and tactile locations in parietal
[... 8 more lines not kept]
```

**Agent**

Main text and Methods read. Now the supplement legends and tables.

**Agent calls Bash**

```bash
cd  awk 'NR>=125 && (length($0)>45 || /^Table|^=== page/){print NR": "$0}' paper/*.txt
```

Result: not kept, because it reads the paper's text.

**Agent**

Supplement PDF has Figures S1–S6 legends and Tables S2–S5; Tables S1 (mouse metadata) and S6 (statistics) are not in it. Let me look at the tables.

**Agent calls Bash**

```bash
cd  sed -n '1566,1830p' paper/*.txt | paste -sd'|' | fold -w 3000
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  sed -n '1826,2340p' paper/*.txt | paste -sd'|' | fold -w 3000
```

Result: not kept, because it reads the paper's text.

**Agent**

Tables read. Now the paper's code repository.

**Agent calls Bash**

```bash
cd $TMPDIR && git clone -q https://github.com/wanglab-neuro/2026_Xiao-Severson_Peri-head-distance code 2>&1 | tail -3; cd code && git log -1 --format='%H %cd' && find . -type f -not -path './.git/*' | head -100 && find . -type f -not -path './.git/*' | wc -l
```

```
b1a9f3cfacf6b0b9673df82b92f58a93290eb997 Fri Aug 21 16:34:02 2026 -0400
./materials/__init__.py
./materials/WX_KS_headcap_side_PrV.svg
./README.md
./PrV_simulation/simulate_prv.py
./PrV_simulation/plot_figures.py
./PrV_simulation/analysis.py
./PrV_simulation/__init__.py
./PrV_simulation/Readme.md
./Manuscript figures/unit_tuning_summary.csv
./Manuscript figures/readme.md
./Manuscript figures/plot_figure2_from_nwb.py
./Manuscript figures/generate_deposition_tables.py
./Manuscript figures/figure_unit_manifest.csv
./Manuscript figures/Original Matlab code/figS5A.m
./Manuscript figures/Original Matlab code/FigS4I_probemap.m
./Manuscript figures/Original Matlab code/FigS1_Stats.m
./Manuscript figures/Original Matlab code/FigS1_Code.m
./Manuscript figures/Original Matlab code/Fig6GHI_right_model_TC_shape_analysis.m
./Manuscript figures/Original Matlab code/Fig6GHI_left_TC_shape_analysis.m
[... 14 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/code; cat .gitmodules README.md "Manuscript figures/readme.md" PrV_simulation/Readme.md; wc -l "Manuscript figures"/*.py "Manuscript figures/Original Matlab code"/* PrV_simulation/*.py; head -5 "Manuscript figures"/*.csv
```

```
[submodule "Processing"]
	path = Processing
	url = https://github.com/wanglab-neuro/HighChannelCount-Ephys-Pipeline.git
	branch = Wenxi_PHD
# Xiao, Severson, et al. Peri-head distance coding in the mouse brainstem - Code Repository

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.20330279.svg)](https://doi.org/10.5281/zenodo.20330279)  

Original code for [Xiao & Severson et al., 2026: **"Peri-head distance coding in the mouse brainstem"**](https://doi.org/10.1016/j.neuron.2026.05.027).

This repository contains the analysis, processing, figure-generation, and simulation code used for the Peri-head Distance project. The code is organized around three main workflows:

- MATLAB scripts for generating manuscript figure panels.
- A MATLAB electrophysiology processing pipeline for high-channel-count silicon probe recordings.
- A Python simulation of PrV circuit mechanisms receiving excitatory and inhibitory trigeminal inputs.

The repository is intended as a code release for transparency and reuse. Some analysis and figure scripts reference local data paths from the original analysis environment and may require path updates, project-specific data files, or external toolboxes before they can be run on another machine.

## Repository Layout

[... 350 more lines not kept]
```

**Agent calls Bash**

```bash
cd "$TMPDIR/code/Manuscript figures/Original Matlab code"; grep -v "^\s*$" Fig2DEF_Pop_Heatmap_Hist_Pie.m | cut -c1-220 | head -400
```

```
% Run stats to test significance of wall tuning
% Also compute tuning modulation index (wall - baseline) / (wall + baseline)
% and assign 'activated' vs. 'suppressed' label
clear; clc
settings.region = 'PrV';
settings.output_path = 'E:\PrV_Wall_Recordings\Analysis\IntermediateData';
settings.fig_dir = 'E:\PrV_Wall_Recordings\Figures';
%% Naive -- 1 way stats - wall distance for naive experiment (naive + before cut)
settings.dataset = 'naive';
settings.data_dir = 'E:\PrV_Wall_Recordings';
settings.wv_stats = 'E:\PrV_Wall_Recordings\WaveformStats_naive';
% Also computes "Activation" and "Suppression"
clearvars -except settings
% Load tuning curve data combined from naive and whisker cutting
% experiments (1358 total units)
settings.data_folder = 'E:\PrV_Wall_Recordings\Analysis\IntermediateData';
dataTable = matfile(fullfile(settings.data_folder, 'tuningTable_PrV.mat')).dataTable;
dataTable_cut = matfile(fullfile('E:\PrV_Wall_Recordings\Analysis\IntermediateData\Whisker_Cutting_naive\tuningTable_PrV.mat')).dataTable;
dataTable_one = matfile(fullfile('E:\PrV_Wall_Recordings\Analysis\IntermediateData\One_Whisker_naive\tuningTable_PrV.mat')).dataTable;
dataTable = cat(1, dataTable, dataTable_cut(:,1:size(dataTable,2)), dataTable_one(:,1:size(dataTable,2))); % only take columns without condition labels
[... 381 more lines not kept]
```

**Agent calls Bash**

```bash
cd "$TMPDIR/code/Manuscript figures/Original Matlab code"; grep -v "^\s*$" Fig3ABC_Decoder_Accuracy_Time_Confusion_Avg.m | grep -v "^\s*%" | cut -c1-200 | head -330
```

```
clear; clc
cd('E:\Code\Analysis\NeuralDecoder')
toolbox_basedir_name = 'ndt.1.0.4/';
addpath(toolbox_basedir_name);
add_ndt_paths_and_init_rand_generator
save_dir = 'E:\Code\Analysis\NeuralDecoder\ndt.1.0.4\Wenxi_PrV_9dist_raster_data';
sst = matfile('E:\PrV_Wall_Recordings\WaveformStats_naive\PrV_spike_stats_table_naive.mat').sst;
dataTable = matfile('E:\PrV_Wall_Recordings\Analysis\IntermediateData\tuningTable_PrV_anova.mat').dataTable;
psth = matfile('E:\PrV_Wall_Recordings\Analysis\IntermediateData\PSTH_naive.mat').psth;
psth.dataTable.wall_tuned = dataTable.wallTuned;
psth.dataTable.acceptable = sst.acceptable;
psth.dataTable.low_firing = dataTable.low_firing;
included_units = ~dataTable.low_firing & sst.acceptable == 1;
psth.dataTable = psth.dataTable(included_units, :);
start = 0; % ms
stop = 14000; % ms
binsize = 1; % ms
num_units = size(psth.dataTable,1);
for unit = 1:num_units
    unit_name = psth.dataTable.Properties.RowNames{unit};
[... 311 more lines not kept]
```

**Agent calls Bash**

```bash
cd "$TMPDIR/code/Manuscript figures/Original Matlab code"; grep -v "^\s*$" Fig3ABC_Decoder_Accuracy_Time_Confusion_Avg.m | grep -v "^\s*%" | cut -c1-200 | sed -n '330,600p' | grep -n -i "ranksum\|mafdr\|summary\|mean(\|bootci\|sem\|std\|p_\|signrank\|ttest"
```

```
10:filename = fullfile(fig_dir, 'decoding_accuracy_proximity_map_vs_time');
13:summary_period = [3000 11000]; % 3-11 second wall-pass period
14:summary_bins = x >= summary_period(1) & x <= summary_period(2);
17:y = cell2mat(cellfun(@(x) mean(x(:,summary_bins,:),2,'omitnan'), accuracy_by_distance, 'Uni',0));
31:err = std(y,[],3) / sqrt(size(y,3));
32:y = mean(y,3);
88:filename = fullfile(fig_dir, 'decoding_accuracy_proximity_map_bar');
91:y = cell2mat(cellfun(@(x) mean(x(:,summary_bins,:),2,'omitnan'), error_by_distance, 'Uni',0));
97:err = std(y,[],3) / sqrt(size(y,3));
98:y = mean(y,3);
154:filename = fullfile(fig_dir, 'decoding_error_proximity_map_bar');
158:mean_accuracy = cellfun(@(x) squeeze(mean(x(:,summary_bins,:),2)), accuracy_by_distance, 'Uni',0);
160:mean_error = cellfun(@(x) squeeze(mean(x(:,summary_bins,:),2)), error_by_distance, 'Uni',0);
212:        [pvalues(d), ~] = ranksum(y(dd & prox), y(dd & map));
214:    pvalues_adj = mafdr(pvalues, 'BHFDR',true);
224:        [pvalues(d), ~] = ranksum(y(dd & prox), y(dd & map));
226:    pvalues_adj = mafdr(pvalues, 'BHFDR',true);
236:        [pvalues(d), ~] = ranksum(y(dd & prox), y(dd & map));
238:    pvalues_adj = mafdr(pvalues, 'BHFDR',true);
248:        [pvalues(d), ~] = ranksum(y(dd & prox), y(dd & map));
[... 5 more lines not kept]
```

**Agent calls Bash**

```bash
cd "$TMPDIR/code/Manuscript figures/Original Matlab code"; for f in Fig4BC_WhiskerCutting_pairwise_FR_PrefDist.m Fig5CE_TeLC_heatmap_stacked_bar.m Fig5D_TeLC_Pref_Dist_CDF.m; do echo "=== $f"; grep -n -i "ranksum\|mafdr\|signrank\|kstest\|ztest\|normcdf\|alpha\|Tail\|summary_period\|wall_period\|base_period\|bonf\|pref_dist\b\|dataTable_cut\|load\|matfile" $f | cut -c1-220 | head -60; done
```

```
=== Fig4BC_WhiskerCutting_pairwise_FR_PrefDist.m
2:% *** Requires MATLAB 2024 (?) to run mafdr (multiple comparisons correction)
10:settings.dist_centers = matfile('E:\Code\Analysis\NeuralDecoder\dist_centers.mat').dist_centers;
16:% Load spike stats
18:sst = matfile(fullfile(settings.wv_stats, 'PrV_spike_stats_table_onewhisker.mat')).sst;
20:% Load psth data
22:dataTable = matfile(fullfile(data_folder,'tuningTable_PrV_stats.mat')).dataTable;
23:dataTable_cond = matfile(fullfile(data_folder,'tuningTable_PrV_stats_condition.mat')).dataTable;
25:%% Load baseline firing rate between control (1=full array) and condition (2=one whisker)
34:    disp(['Loading data from ' conditions{c}])
196:    pvals(uu) = signrank(x, y, 'method','exact');  % exact p-values
199:adj_p = mafdr(pvals, 'BHFDR', true);
200:alpha = 0.05;
204:    if adj_p(u) < alpha
253:p_base = signrank(base1, base2);
260:p_wall = signrank(wall1, wall2);
264:alpha = 0.05;
267:alpha_corrected = alpha / (num_units * 2); % correct for multiple comparison (neurons * 2) left and right tail
279:    pb(neuron,1) = signrank(b1, b2);
291:    pw(neuron,1) = signrank(w1, w2, 'Tail','both');
[... 103 more lines not kept]
```

**Agent calls Bash**

```bash
cd "$TMPDIR/code/Manuscript figures/Original Matlab code"; sed -n 25,60p Fig4BC_WhiskerCutting_pairwise_FR_PrefDist.m; sed -n 180,300p Fig4BC_WhiskerCutting_pairwise_FR_PrefDist.m; sed -n 60,164p Fig5D_TeLC_Pref_Dist_CDF.m; sed -n 860,910p Fig5CE_TeLC_heatmap_stacked_bar.m
```

```
%% Load baseline firing rate between control (1=full array) and condition (2=one whisker)

% Set unit inclusion criteria
incl = sst.acceptable & ~dataTable.low_firing;
included_units = find(incl);

% Get mean firing rate and repetitions for baseline and each wall distance
clear fr_base fr_base_distance fr_base_all fr_wall fr_wall_distance fr_wall_all
for c = numel(conditions):-1:1
    disp(['Loading data from ' conditions{c}])
    if strcmp(conditions{c},'Cut') || strcmp(conditions{c},'Laser')
        cond = '_cond';
        dt = dataTable_cond;
    else
        cond = '';
        dt = dataTable;
    end

    % Get median wall firing rate
    fr_wall(:,c) = cellfun(@(x) median(x), dt.(['fr_mean' cond]), 'Uni',1);
[... 294 more lines not kept]
```

**Agent calls Bash**

```bash
cd "$TMPDIR/code/Manuscript figures"; grep -n "units\[\|colnames\|\.trials\|get(\|\[\"\|\['" generate_deposition_tables.py | head -50; grep -n "def \|window\|3\.0\|11\.0\|-4.5\|zscore\|baseline" plot_figure2_from_nwb.py | head -60
```

```
137:    module = nwb.processing["wall_tuning"]
140:    distances = module["distance_axis"].to_dataframe()["distance_mm"].to_numpy(float)
145:    flags = [bool(value) for value in as_list(unit.get("trial_include", []))]
181:                "spike_count": len(as_list(unit["spike_times"])) if "spike_times" in units.columns else 0,
202:                label = str(unit.get("unit_label", "")).strip()
211:                        "tuning_type": str(unit.get("tuning_type", "")),
221:        label = entry["matlab_row_label"]
64:def parse_args() -> argparse.Namespace:
122:        "--window",
127:        help="Time window in seconds relative to wall-pass onset.",
171:def load_plot_data(nwb_path: Path) -> PlotData:
196:def normalize_unit_label(value: object) -> str:
200:def unit_indices_from_labels(units: pd.DataFrame, requested_labels: list[str]) -> list[int]:
228:def choose_units(
263:def iter_nwb_files(nwb_dir: Path) -> list[Path]:
270:def index_nwb_directory(nwb_dir: Path) -> tuple[list[tuple[int, str, Path, int]], dict[str, tuple[Path, int]]]:
286:def selections_from_nwb_directory(
340:def selections_from_nwb_file(
370:def distance_values(data: PlotData, order: str, include_all_trial_distances: bool) -> np.ndarray:
380:def make_distance_colors(distances: np.ndarray) -> dict[float, tuple[float, float, float, float]]:
[... 26 more lines not kept]
```

**Agent calls Bash**

```bash
cd "$TMPDIR/code/Manuscript figures"; sed -n 125,215p generate_deposition_tables.py
```

```
if isinstance(value, (np.floating, float)):
        return "" if np.isnan(float(value)) else round(float(value), digits)
    return str(value)


def format_float_list(values: Iterable[float], digits: int) -> str:
    return ";".join("" if np.isnan(float(value)) else str(round(float(value), digits)) for value in values)


def session_distance_axis(nwb, digits: int) -> str:
    if "wall_tuning" not in nwb.processing:
        return ""
    module = nwb.processing["wall_tuning"]
    if "distance_axis" not in module.data_interfaces:
        return ""
    distances = module["distance_axis"].to_dataframe()["distance_mm"].to_numpy(float)
    return format_float_list(distances, digits)


def trial_include_counts(unit: pd.Series) -> tuple[int, int]:
[... 70 more lines not kept]
```

**Agent calls Bash**

```bash
curl -s https://api.dandiarchive.org/api/dandisets/001687/ | python -c "import json,sys; d=json.load(sys.stdin); print(json.dumps({k:d.get(k) for k in ['identifier','draft_version','most_recent_published_version']},indent=1))"; curl -s https://api.dandiarchive.org/api/dandisets/001687/versions/draft/info/ | python -c "import json,sys; d=json.load(sys.stdin)['metadata']; print(d.get('name')); print(d.get('description')); print(d.get('assetsSummary'))"
```

Result: the fetched text is not kept.

**Agent**

Now the format example.

**Agent calls Bash**

```bash
cd  head -150 claims/001453/*.yaml; grep -n "^  [a-z_]*:" claims/001453/*.yaml | awk '{print $2}' | sort | uniq -c; ls tools; sed -n 1,60p tools/claims_check.py
```

```
# Claims for Fouke, He, Loring & Naumann (2025) on dandiset 001453.
# Source: the accepted author manuscript in PubMed Central (PMC12218792), full text, read
# from its Results, figure legends and STAR Methods. The version of record is not open access.
#
# When these criteria were written, the author had seen the data check only: the file list,
# subject metadata, frame rates, units, trial structure and stimulus codes of every file, and
# the extent of positions. No claim's analysis had been run. The author had also read the
# outputs printed in the paper's own analysis notebook (Fig1-S1.ipynb, GitLab commit 33a5c29),
# which include per-stimulus median speeds and angular velocities and its statistics.
#
# The dandiset holds only the freely swimming tracking data of Figure 1 and Figure S1. Its
# stimulus codes 0 to 20 carry no names. The names come from the paper's code and from the
# stimulus software's protocol file (see stimulus-code-link), so the claims that need them
# use outside data and depend on that claim.
#
# Method choices fixed here, from the paper's Fig1-S1.ipynb where the Methods are silent: a
# trial is one stim_index; tracked frames only; positions smoothed with a Savitzky-Golay filter
# (21 frames, order 2); trials rejected when the absolute cumulative heading change exceeds
# 1000 degrees in the first 10 s or 2000 degrees in the first 35 s, or the mean speed exceeds
# 100 mm/s; measures taken from 3 s to 35 s after the first frame (the 3 s stationary phase is
[... 220 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python -c "
import json;s=json.load(open('schemas/claims.schema.json'));print(json.dumps(s,indent=1))" | head -250; sed -n 150,400p claims/001453/*.yaml | grep -n -A12 "expected:\|checks:\|inputs\|where:" | head -80
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
[... 230 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python -c "
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

**Agent calls Bash**

```bash
cd "$TMPDIR/code/Manuscript figures/Original Matlab code"; grep -n -i "kstest\|ranksum\|mask\s*=\|baseline\s*=\|fr_base\|monoton.*=" Fig6GHI_left_TC_shape_analysis.m | head -30; grep -n -i "ttest\|alpha\|mean(" FigS1_Stats.m | head -20; cat figS5A.m | head -5; grep -n "def \|seed\|n_neurons\|N =\|1225\|telc" "$TMPDIR/code/PrV_simulation/simulate_prv.py" | head -40
```

```
87:    p.addParameter('BaselineVar', 'fr_base_mean', @(x)ischar(x) || isstring(x));
445:function mask = get_wall_tuned_mask(tbl, sst, x)
449:    mask = tbl.wallTuned ...
59:        [~, p2, ci, stats] = ttest(Wi.awake, Wi.anesthetized);  % TWO-SIDED
60:        mDiff = mean(diffs);
77:alpha = 0.05/3
78:results.sig_Bonf = results.p_two_sided < alpha;
116:        mAw = mean(Wi.awake, 'omitnan');
118:        mAn = mean(Wi.anesthetized, 'omitnan');
123:        [~, p2, ~, stats] = ttest(Wi.awake, Wi.anesthetized);  % TWO-SIDED
124:        mDiff = mean(diffs, 'omitnan');
139:alpha = 0.05/3;
140:results.sig_Bonf = results.p_two_sided < alpha;
232:alpha = 0.05/3;
233:results.sig_Bonf = results.p_two_sided < alpha;
307:        mAw = mean(Wi.awake, 'omitnan');
309:        mAn = mean(Wi.anesthetized, 'omitnan');
314:        [~, p2, ~, stats] = ttest(Wi.awake, Wi.anesthetized);  % TWO-SIDED
315:        mDiff = mean(diffs, 'omitnan');
332:alpha = 0.05/3;
[... 47 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -rn -B3 -A8 "simulat" claims/*/*.yaml | grep -n "data:\|criterion\|statement" | head -20
```

```
4:claims/000009/10.1038-nature22324.yaml:649:  criterion: A simulation, not a test on recorded data; its parameters are in the Supplementary
8:claims/000009/10.1038-nature22324.yaml-653-  statement: Weak thalamus photoinhibition (20-fold weaker, 0.5 mW) significantly changed the spike rate
17:claims/000070/10.1038-nature11129.yaml:275:  statement: A simulated population of units tuned to hand velocity and speed, with
27:claims/000070/10.1038-nature11129.yaml:285:  criterion: One simulated dataset per array dataset from that session's condition-mean hand
33:claims/000070/10.1038-nature11129.yaml:291:  statement: A simulated population tuned to hand position, velocity, acceleration and jerk
40:claims/000070/10.1038-nature11129.yaml-298-  criterion: As for fig6-velocity-model, with the complex kinematic model.
45:claims/000070/10.1038-nature11129.yaml-330-  statement: A generator model of two rotations of fixed frequency fits deltoid EMG with
53:claims/000070/10.1038-nature11129.yaml-338-  statement: Rotations have similar angular velocity for instructed fast and slow reaches; the
60:claims/000947/10.1371-journal.pbio.3000829.yaml-500-  statement: In a model thalamocortical cell with N converging GPi inputs, post-spike inhibition
67:claims/000947/10.1371-journal.pbio.3000829.yaml-507-  data: elsewhere
74:claims/001710/10.1101-2023.11.20.567978.yaml:538:  criterion: A simulation, not a test on recorded data. The Methods give M=N=1000, input
82:claims/001710/10.1101-2023.11.20.567978.yaml-546-  statement: Place fields are wider in the Plasticity model than in the No-Plasticity model.
86:claims/001710/10.1101-2023.11.20.567978.yaml:550:  criterion: A simulation, as fig3bc-model-stable-place-cells. The paper does not say how a
90:claims/001710/10.1101-2023.11.20.567978.yaml-554-  statement: Units in the No-Plasticity model have more place fields per cell than units in the
96:claims/001710/10.1101-2023.11.20.567978.yaml:560:  criterion: A simulation, as fig3bc-model-stable-
[... 5 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 530,560p claims/001710/*.yaml; sed -n 515,535p claims/001750/*.yaml
```

```
- id: fig3bc-model-stable-place-cells
  statement: In the CA3-CA1 K-Winners-Take-All model, both the Plasticity and the No-Plasticity
    versions produce place-selective CA1 units with a spatially stable code from the first
    trial.
  source: Figures 3B-C; Results, Spatial coding in Cre animals may be passively inherited from
    upstream activity, paragraph 1
  quote: In both models, individual units were clearly place-selective, and the population
    maintained spatially stable place coding from the first trial (Fig. 3B-C)
  criterion: A simulation, not a test on recorded data. The Methods give M=N=1000, input
    variance 0.5 on x in [0,10], K=50, output noise 0.5N(0,1), stimulus noise 0.05N(0,1), eta
    1e-4 and alpha 9e-4 (Plasticity) or 0 and 0 (No-Plasticity), weight noise 0.001N(0,1),
    wmax 10, lognormal initial weights (mean 0, sd 0.5). The text read omits the weight update
    equation and the input tuning function, and gives no number of trials, no position
    sampling and no measure of stability or place selectivity. Not specified by the paper;
    recorded so the finding is covered.
- id: fig3d-model-wider-fields-with-plasticity
  statement: Place fields are wider in the Plasticity model than in the No-Plasticity model.
  source: Figure 3D; Results, Spatial coding in Cre animals may be passively inherited from
    upstream activity, paragraph 2
  quote: place fields were wider in the Plasticity model than the No-Plasticity model (Fig. 3D)
[... 32 more lines not kept]
```

**Agent**

I have what I need from the code (repo at commit b1a9f3c). Checking a few legend lines before writing.

**Agent calls Bash**

```bash
cd  sed -n '930,966p;1297,1302p;1537,1543p;1560,1567p;341,345p;462,470p' paper/*.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Write**

```json
{
 "file_path": "claims/001687/10.1016-j.neuron.2026.05.027.yaml",
 "content": "# Claims for Xiao, Severson et al. (2026), \"Peri-head distance coding in the mouse brainstem\",\n# Neuron, doi:10.1016/j.neuron.2026.05.027, on dandiset 001687.\n#\n# Written by an agent (model \"claude-opus-5-5\", Claude Code in GitHub Actions), 2026-10-21,\n# protocol pilot-10 as stated in docs/protocol.md.\n#\n# Text read: the accepted author manuscript in PubMed Central (NIHMS2191201, PMC13336321), as\n# fetched 2026-10-20 into paper/10.1016-j.neuron.2026.05.027.txt: main text, STAR Methods, the\n# legends of Figures 1 to 6, and the supplement file NIHMS2191201-supplement-1.pdf (legends of\n# Figures S1 to S6 and Tables S2 to S5). The version of record was not read. Tables S1 (mouse\n# sex, age and figure assignments) and S6 (test statistics, degrees of freedom and p-values of\n# all analyses) are named in the text but are not in the supplement file read; every number\n# used below is in the main text, the legends or Tables S2 to S5. Figures were not opened.\n#\n# Code read: github.com/wanglab-neuro/2026_Xiao-Severson_Peri-head-distance at commit b1a9f3c\n# (2026-08-21; archived as doi:10.5281/zenodo.20330279). It holds the original MATLAB scripts\n# for Figures 1E, 2, 3, 4B-C, 5C-E, 6D, 6G-I, S1, S4I and S5A (\"Manuscript figures/Original\n# Matlab code\"), Python helpers that read the deposited NWB files, the Python circuit model\n# (PrV_simulation/simulate_prv.py), and a submodule (Processing, the spike-sorting pipeline;\n# not read). The helper generate_deposition_tables.py reads, per NWB unit, the columns\n# unit_label, wall_responsive, wall_tuned, activated, suppressed, tuning_type, pref_dist_index,\n# pref_dist_mm, low_firing and trial_include, and a wall_tuning processing module with a\n# distance_axis; so the deposit is meant to carry the paper's own unit labels. The repository's\n# unit_tuning_summary.csv is derived from the deposit and was not read for these claims.\n#\n# Data the paper used (Methods, Results, Table and figure legends):\n# - Wall-passing paradigm. Awake head-fixed mice on a linear treadmill, in the dark; a wall\n#   moves anterior to posterior past the face at 10 mm/s; each pass about 14 s, onset at t = 0,\n#   whisker contact typically 3 to 11 s. Wall distance is measured from the C2 follicle. Silicon\n#   probe sessions: 7 to 23 mm in 2-mm steps (nine distances), 15 to 20 passes per distance,\n#   randomly ordered. Analysis windows: baseline -4.5 to 0 s, wall pass 3 to 11 s; onset 2.5 to\n#   4.5 s, sustained 4.5 to 9.5 s, offset 9.5 to 11.5 s. Distances are binned into nine 2-mm bins\n#   centred on 7, 9, ..., 23 mm; sessions with fewer than nine distances are left out of\n#   population analyses.\n# - Wild-type silicon probe recordings (C57BL/6J): 1,358 units from 36 mice, 1,141 passing the\n#   unit criteria (SNR of at least 5, ISI false-alarm rate at most 2% at 0.8 ms, firing above 1\n#   Hz). This set includes the full-array part of the whisker-cutting sessions (the code merges\n#   \"naive\" and pre-cut tables).\n# - Whisker-cutting sessions (subset of the above): 195 units from 18 mice recorded with the full\n#   array and then after cutting all but one whisker, in one continuous recording.\n# - SpVi-TeLC (vGat-Cre, AAV-FLEX-TeLC in caudal SpVi, recorded 10 to 15 days later): 665 units\n#   from 11 mice, 587 passing the criteria.\n# - PrV GtACR optogenetics (vGat-Cre, N = 2): 112 units; distances 7 to 23 mm in 4-mm steps,\n#   laser on and off passes interleaved, light during the whole pass.\n# - Tungsten single-electrode recordings: 46 units from 14 mice, C-row whiskers only, distances\n#   4 to 20 mm in 1-mm steps, 10 to 20 passes per distance.\n# - High-speed video (500 Hz): 4 mice with a single whisker row, awake then anesthetized (20\n#   passes per distance, 7 to 23 mm); and whisker-array midpoint angle in 15 wild-type sessions\n#   (6 mice) and 15 SpVi-TeLC sessions (6 mice).\n# - Measured variables: spike times of sorted units, wall pass start and end times (from the\n#   stepper-motor signal), wall distance per pass, laser condition, cutting condition, whisker\n#   angle and curvature from video.\n# The dandiset's description names baseline recordings and the multi-whisker, local-inhibition\n# and long-range-inhibition perturbations, processed and raw NWB files; whether the tungsten and\n# video data are there is for the author to find.\n#\n# Method choices fixed here (each claim cites them), from the Methods and, where the Methods\n# are silent, from Fig2DEF_Pop_Heatmap_Hist_Pie.m (same procedure in Fig5CE_TeLC_heatmap_stacked_bar.m):\n# - Per pass, the wall firing rate is the mean rate from 3 to 11 s and the baseline rate the\n#   mean rate from -4.5 to 0 s after wall-movement onset (Methods, Wall Distance Tuning Curve\n#   Calculation).\n# - Unit inclusion: SNR and false-alarm criteria (Methods); the code drops a unit as low-firing\n#   when both its largest per-distance mean wall rate and its mean baseline rate are below 1 Hz.\n# - Wall-activated or wall-suppressed: at each distance, one-tailed Wilcoxon signed-rank test of\n#   the pass's wall rate against its own baseline rate (Methods); the code corrects the nine\n#   p-values of each direction with Benjamini-Hochberg (BH-FDR) and uses q < 0.05. The Methods\n#   print only \"p < 0.05\"; uncorrected p < 0.05 is the variant reading. Wall-responsive means\n#   activated or suppressed.\n# - Distance-tuned: two-tailed Wilcoxon signed-rank tests between all 36 pairs of distances,\n#   BH-FDR corrected, any q < 0.05 (Methods). The code pairs the k-th pass at one distance with\n#   the k-th pass at the other.\n# - Preferred distance: the distance of the maximum of the unit's mean tuning curve (code: the\n#   z-scored curve, which has the same maximum).\n# - Proximity unit: activated, tuned, preferred distance 7 mm. Map unit: activated, tuned,\n#   preferred distance at least 9 mm, and at least one of the eight one-tailed signed-rank tests\n#   (distance d above 7 mm) significant after BH-FDR across the eight (Methods; Figure S4H\n#   legend; code). Ambiguous: activated, tuned, preferred at least 9 mm, no significant test.\n#   Suppressed-only: tuned, suppressed, never activated. Untuned: wall-responsive and not\n#   distance-tuned (Methods; code).\n# - Population decoding (Methods; Fig3ABC_Decoder_Accuracy_Time_Confusion_Avg.m): maximum\n#   correlation coefficient classifier of the Neural Decoding Toolbox on a pseudo-population;\n#   spike counts in 150-ms windows stepped by 50 ms from 0 to 14 s; 15 passes per distance,\n#   resampled 5 times; z-score feature normalisation (code; Methods silent); subpopulations of\n#   118 units drawn 10 times without replacement (the combined group 36 map and 82 proximity\n#   units); a shuffled group from map and proximity units with the passes' distance labels\n#   scrambled; accuracy per distance is the true-positive rate, averaged over the time bins\n#   starting within 3 to 11 s; overall accuracy is the mean over the nine distances (Table S2,\n#   \"Average\"). Cross-validation is 10-fold in the Methods and 15 splits (one pass per distance\n#   held out) in the code: the Methods' 10-fold is the main reading, the code's the variant.\n#   Group comparisons per distance are Wilcoxon rank-sum tests on the 10 subsample values,\n#   BH-FDR across the nine distances (Methods; Figure 3C legend; code).\n#\n# Inconsistencies in the paper, noted where they bear on a claim: 472 activated + 213 suppressed\n# - 29 both = 656 tuned implies 184 suppressed-only and 112 untuned, but Figure 2F gives 119 and\n# 177 (fig2f-tuning-categories); the Figure 4B legend gives 11.58 +/- 2.986 sp/s where the text\n# gives +/- 1.338; the Figure S6J legend prints p = 3.98 x 10^-3 for the TeLC untuned baseline\n# where the text prints 3.98 x 10^-5; the Methods describe the +/- of firing-rate comparisons as a\n# bootstrap 95% CI half-width while the Figure S4 legends call it SEM; Figure 3C plots mean +/-\n# SEM while Tables S2 and S3 give mean +/- 95% CI; the Methods correct per-unit whisker-cutting\n# tests with Bonferroni in one place and BH-FDR in another, and the Results print p < 0.05.\nschema_version: 2\ndataset:\n  archive: dandi\n  id: \"001687\"\npaper: doi:10.1016/j.neuron.2026.05.027\nclaims:\n- id: figs1f-angle-awake-vs-anesthetized\n  statement: >-\n    Wall-induced change in whisker midpoint angle does not differ significantly between awake and\n    anesthetized mice for the C1, C2 and Greek whiskers (paired t-tests across 4 mice, Bonferroni\n    alpha 0.017); the mean awake minus anesthetized difference is 2.28 degrees.\n  source: Results, A wall-passing paradigm, paragraph 2; Figure S1F legend\n  quote: >-\n    Awake mice showed similar bending angle (mean difference: 2.28°) and curvature (mean\n    difference: 1.66 × 10 −5 mm −1 ) changes, with no significant differences from the\n    anesthetized condition across whiskers\n  statistics:\n  - about: C1 whisker, awake against anesthetized\n    test: two-tailed paired t-test across mice\n    p: 0.03\n    corrected: Bonferroni, alpha 0.017\n    n: 4 mice\n  - about: C2 whisker\n    test: two-tailed paired t-test across mice\n    p: 0.04\n    corrected: Bonferroni, alpha 0.017\n    n: 4 mice\n  - about: Greek whisker\n    test: two-tailed paired t-test across mice\n    p: 0.0199\n    corrected: Bonferroni, alpha 0.017\n    n: 4 mice\n  expected:\n  - quantity: mean awake minus anesthetized change in midpoint angle\n    value: 2.28\n    tolerance: 0.228\n    unit: degrees\n  criterion: >-\n    A claim of absence, judged on the paper's test (Methods, Data Analysis: Wall-Induced Whisker\n    Retraction; FigS1_Stats.m). Per pass, the midpoint angle (Savitzky-Golay 21 frames, order 3,\n    mean of the upper and lower envelopes) is averaged over 3 to 11 s minus its mean over -4.5 to\n    0 s; per mouse, whisker and condition, averaged over distances and passes; for each whisker a\n    two-tailed paired t-test across the 4 mice, significant at 0.05/3. Reproduced when no whisker\n    reaches p < 0.0167; not reproduced when any does. The mean difference is reported for each\n    whisker; the paper does not say whether 2.28 degrees is pooled over whiskers or for one, so\n    the readings are the mean over the three whiskers and each whisker alone.\n- id: figs1j-curvature-awake-vs-anesthetized\n  statement: >-\n    Wall-induced change in whisker curvature does not differ significantly between awake and\n    anesthetized mice for any of the three whiskers.\n  source: Results, A wall-passing paradigm, paragraph 2; Figure S1H-J legend\n  quote: >-\n    (H-J) Same as D-F, but for curvature. Significance reflects mouse-level paired comparisons\n    (awake vs. anesthe- tized) with Bonferroni correction (α = 0.017): C1, p = 0.56 (n.s.); C2, p\n    = 0.053 (n.s.), Greek: p = 0.43 (n.s.)\n  statistics:\n  - about: C1 whisker\n    test: two-tailed paired t-test across mice\n    p: 0.56\n    corrected: Bonferroni, alpha 0.017\n    n: 4 mice\n  - about: C2 whisker\n    test: two-tailed paired t-test across mice\n    p: 0.053\n    corrected: Bonferroni, alpha 0.017\n    n: 4 mice\n  - about: Greek whisker\n    test: two-tailed paired t-test across mice\n    p: 0.43\n    corrected: Bonferroni, alpha 0.017\n    n: 4 mice\n  expected:\n  - quantity: mean awake minus anesthetized change in curvature\n    value: 1.66e-5\n    tolerance: 1.66e-6\n    unit: 1/mm\n  criterion: >-\n    A claim of absence, as figs1f-angle-awake-vs-anesthetized, for curvature (signed planar\n    curvature from a local second-order fit to a 4-mm arclength segment, minus its baseline mean\n    over -4.5 to 0 s, averaged over 3 to 11 s; Methods). Reproduced when no whisker reaches p <\n    0.0167. The Methods do not say where along the whisker the 4-mm segment lies; this is open,\n    and the author reports the segment used.\n- id: figs1d-bending-larger-closer\n  statement: >-\n    Under anesthesia the passing wall bends whiskers in the retraction direction, with larger\n    angle changes and larger curvature changes at closer wall distances, so wall-induced bending\n    grows roughly monotonically as the wall approaches.\n  source: Results, A wall-passing paradigm, paragraph 2; Figure S1D, H\n  quote: >-\n    Under anesthesia, the moving wall pushed whiskers in the retraction direction, producing\n    larger absolute bending angles ( Supplemental Figure S1D , right) and greater change in\n    whisker curvature ( Supplemental Figure S1H , right) at closer wall distances\n  criterion: >-\n    The paper reports no test. Per distance, the across-mouse mean of the absolute change in\n    midpoint angle and of the absolute change in curvature in the anesthetized condition\n    (measures as in figs1f-angle-awake-vs-anesthetized). Reproduced when, for each of the two\n    measures and each of the three whiskers, the value at 7 mm exceeds the value at 23 mm and the\n    Spearman correlation between distance and value over the nine distances is negative. These\n    two summaries are the readings of \"larger ... at closer wall distances\"; the outcome is the\n    one both give.\n- id: figs2-tungsten-responsiveness\n  statement: >-\n    Of 46 tungsten-recorded PrV units from 14 mice, 41 (89.1%) were wall-activated, 3 (6.5%)\n    wall-suppressed, and 43 (93.5%) wall-responsive in all, one unit being both.\n  source: Results, PrV contains both proximity and map codes, paragraphs 1-2\n  quote: >-\n    Of the 46 units, 41/46 (89.1%) were wall-activated and 3/46 (6.5%) were wall-suppressed; one\n    unit showed both activation and suppression at different distances, yielding a total of\n    43/46 (93.5%) wall-responsive\n  expected:\n  - quantity: tungsten units passing criteria\n    value: 46\n    tolerance: 4.6\n  - quantity: wall-activated tungsten units\n    value: 41\n    tolerance: 4.1\n  - quantity: wall-suppressed tungsten units\n    value: 3\n    tolerance: 0.3\n  - quantity: wall-responsive tungsten units\n    value: 43\n    tolerance: 4.3\n  criterion: >-\n    Classification as in the opening comment, applied to the tungsten sessions with their own\n    distances (4 to 20 mm in 1-mm steps, so the binning into nine 2-mm bins does not apply; the\n    code leaves the number of distances to each session). Responsiveness is judged with the\n    code's BH-FDR across distances; uncorrected p < 0.05 per distance is the variant reading.\n    Reproduced when all four counts are within tolerance under one reading.\n- id: figs2-tungsten-tuning\n  statement: >-\n    Of the 43 wall-responsive tungsten units, 39 (90.7%) were distance-tuned; 24 (55.8%) were\n    broadly monotonic, firing more at closer distances, and 6 (14.0%) peaked at intermediate or\n    far distances.\n  source: Results, PrV contains both proximity and map codes, paragraph 2; Figure S2D-F\n  quote: >-\n    Wall-responsive units with significant differences in mean firing rates for at least one\n    distance pair were classified as \"distance-tuned\" (i.e., distance-selective; 90.7%, 39/43)\n    ... The majority of wall-responsive units (55.8%, 24/43) showed a broadly monotonic,\n    inversely proportional relationship with wall distance ... a distinct subset (14.0%, 6/43)\n    showed peak responses at intermediate or far wall distances\n  depends_on:\n  - figs2-tungsten-responsiveness\n  expected:\n  - quantity: distance-tuned tungsten units\n    value: 39\n    tolerance: 3.9\n  - quantity: monotonic (proximity-like) tungsten units\n    value: 24\n    tolerance: 2.4\n  - quantity: tungsten units peaking at intermediate or far distances\n    value: 6\n    tolerance: 0.6\n  criterion: >-\n    Distance tuning as in the opening comment (36 pairs become all pairs of the session's\n    distances). The paper does not say how the 24 monotonic and 6 peaked units were defined for\n    the tungsten data. Readings: (a) the silicon-probe rule, proximity (preferred at the closest\n    distance) and map (preferred farther, with a significant BH-FDR one-tailed test against the\n    closest distance), with activated or suppressed units both eligible as in the code's\n    tungsten branch; (b) preferred distance at the closest distance against elsewhere, without\n    the map test. Reproduced when all three counts are within tolerance under one reading.\n- id: si-unit-yield\n  statement: >-\n    Silicon probe recordings in wild-type mice yielded 1,141 single units from 36 mice passing\n    isolation and firing criteria, out of 1,358 sorted units.\n  source: Results, PrV contains both proximity and map codes, paragraph 3; Methods, Isolation of Single Unit Activity\n  quote: >-\n    For silicon probe data, in wild-type mice, 1141 of 1358 units (36 mice), in TeLC experiments,\n    587 of 665 units (11 mice)\n  expected:\n  - quantity: wild-type silicon probe units passing criteria\n    value: 1141\n    tolerance: 114.1\n  - quantity: wild-type silicon probe mice\n    value: 36\n    tolerance: 0\n  criterion: >-\n    Units with SNR of at least 5 and ISI false-alarm rate at most 2% (0.8 ms), not low-firing as\n    defined in the opening comment, in wild-type full-array sessions (including the pre-cut part\n    of whisker-cutting sessions). The number of mice is a count and must match exactly. If the\n    deposit carries only curated units, the count of deposited units is compared and the\n    difference reported.\n- id: fig2-wall-responsive-counts\n  statement: >-\n    Of the 1,141 units, 768 (67.3%) were wall-responsive; of these 532 (69.3%) were activated at\n    one or more distances, 333 (43.4%) suppressed, and 97 both.\n  source: Results, PrV contains both proximity and map codes, paragraph 3\n  quote: >-\n    Of the 1,141 units, 67.3% (768/1141) were significantly modulated by the passing-wall\n    stimulus and classified as \"wall-responsive\". Among these wall-responsive units, 532/768\n    (69.3%) showed significant activation at one or more distances, 333/768 (43.4%) showed\n    significant suppression, and 97 units met both criteria\n  depends_on:\n  - si-unit-yield\n  expected:\n  - quantity: wall-responsive units\n    value: 768\n    tolerance: 76.8\n  - quantity: wall-activated units\n    value: 532\n    tolerance: 53.2\n  - quantity: wall-suppressed units\n    value: 333\n    tolerance: 33.3\n  - quantity: units both activated and suppressed\n    value: 97\n    tolerance: 9.7\n  criterion: >-\n    Classification as in the opening comment (code's BH-FDR across the nine distances; variant,\n    uncorrected p < 0.05). Reproduced when all four counts are within tolerance under one\n    reading.\n- id: fig2-distance-tuned-counts\n  statement: >-\n    Over the full wall-contact period, 656 of 768 wall-responsive units (85.4%) were distance\n    tuned; of these, 472 (72.0%) were activated at one or more distances (the activated\n    population), 213 (32.5%) suppressed (the suppressed population), and 29 both.\n  source: Results, PrV contains both proximity and map codes, paragraph 4\n  quote: >-\n    Across the full wall-contact period (8 s), we identified 656 out of the 768 (85.4%)\n    wall-responsive units that were significantly tuned to wall distance. Within this\n    distance-tuned population, 472/656 (72.0%) showed significant activation relative to\n    baseline at one or more distances ... whereas 213/656 (32.5%) showed significant suppression\n    at one or more distances ... A small subset of units (29/656; 4.4%) exhibited both\n  depends_on:\n  - fig2-wall-responsive-counts\n  expected:\n  - quantity: distance-tuned units\n    value: 656\n    tolerance: 65.6\n  - quantity: activated population (activated and tuned)\n    value: 472\n    tolerance: 47.2\n  - quantity: suppressed population (suppressed and tuned)\n    value: 213\n    tolerance: 21.3\n  - quantity: tuned units both activated and suppressed\n    value: 29\n    tolerance: 2.9\n  criterion: >-\n    Distance tuning as in the opening comment. Reproduced when all four counts are within\n    tolerance under one of the responsiveness readings. The 472 activated units are the\n    population of Figures 2D-E, 5D, 6G-I and S4.\n- id: fig2f-tuning-categories\n  statement: >-\n    Among the 768 wall-responsive units, 266 (34.6%) were proximity units, 118 (15.4%) map\n    units, 88 (11.5%) ambiguous, and 119 (15.5%) suppressed-only; the remainder (177, 23.0%) were\n    untuned, giving a proximity to map ratio of 2.3 to 1.\n  source: Results, PrV contains both proximity and map codes, paragraph 7; Figure 2F; Figure 5E legend\n  quote: >-\n    We identified 266 proximity units (34.6%) and 118 map units (15.4%) out of the 768\n    wall-responsive units ( Figure 2F ) ... An additional 88 units (11.5%) were\n    distance-selective but did not meet criteria for either map or proximity and were labeled\n    \"ambiguous\" ... Suppressed-only units ... accounted for 119 out of 768 wall-responsive units\n    (15.5%; Figure 2F )\n  depends_on:\n  - fig2-distance-tuned-counts\n  expected:\n  - quantity: proximity units\n    value: 266\n    tolerance: 26.6\n  - quantity: map units\n    value: 118\n    tolerance: 11.8\n  - quantity: ambiguous units\n    value: 88\n    tolerance: 8.8\n  - quantity: suppressed-only units\n    value: 119\n    tolerance: 11.9\n  - quantity: untuned units\n    value: 177\n    tolerance: 17.7\n  criterion: >-\n    Categories as in the opening comment. The paper's counts are not consistent with each other\n    (472 + 213 - 29 = 656 tuned implies 184 suppressed-only and 112 untuned; the five Figure 2F\n    counts sum to 768 with 119 and 177). Readings for the last two: (a) the Figure 2F counts as\n    printed; (b) the counts implied by fig2-distance-tuned-counts (184 and 112, same 10%\n    tolerance). Reproduced when the proximity, map and ambiguous counts are within tolerance and\n    the suppressed-only and untuned counts are within tolerance under one reading; partially\n    reproduced when only the proximity, map and ambiguous counts are.\n- id: figs4a-baseline-activated-lower\n  statement: >-\n    Before wall movement, units of the activated population fire less than untuned units (5.46\n    against 6.93 sp/s).\n  source: Results, PrV contains both proximity and map codes, paragraph 4; Figure S4A\n  quote: >-\n    At baseline prior to wall movement onset, units in the activated population showed lower\n    firing rates than untuned units (5.46 ± 0.670 vs. 6.93 ± 0.947 sp/s; two-tailed\n    Kolmogorov-Smirnov (K-S) test: p = 2.47 × 10 − 7 )\n  statistics:\n  - test: two-tailed two-sample Kolmogorov-Smirnov test\n    p: 2.47e-7\n    n: 472 activated and 177 untuned units\n  depends_on:\n  - fig2f-tuning-categories\n  expected:\n  - quantity: mean baseline rate, activated population\n    value: 5.46\n    tolerance: 0.67\n    unit: sp/s\n  - quantity: mean baseline rate, untuned units\n    value: 6.93\n    tolerance: 0.947\n    unit: sp/s\n  criterion: >-\n    Per unit, the mean baseline rate (-4.5 to 0 s) over all passes; two-sample K-S test\n    (two-tailed, kstest2) between the activated population and untuned units (Methods). The\n    tolerances are the paper's printed spread (bootstrap CI half-width in the Methods, SEM in the\n    legend). Reproduced when p < 0.05 with the activated mean lower and both means within\n    tolerance; partially reproduced when the test holds but a mean is out of tolerance.\n- id: figs4a-baseline-suppressed-similar\n  statement: >-\n    Units of the suppressed population have baseline firing comparable to untuned units (7.31\n    against 6.93 sp/s, not significant).\n  source: Results, PrV contains both proximity and map codes, paragraph 4; Figure S4A\n  quote: >-\n    whereas units in the suppressed population had baseline firing rates comparable to untuned\n    units (7.31 ± 1.124 vs. 6.93 ± 0.947 sp/s; two-tailed K-S test: p = 0.63\n  statistics:\n  - test: two-tailed two-sample Kolmogorov-Smirnov test\n    p: 0.63\n    n: 213 suppressed and 177 untuned units\n  depends_on:\n  - fig2f-tuning-categories\n  expected:\n  - quantity: mean baseline rate, suppressed population\n    value: 7.31\n    tolerance: 1.124\n    unit: sp/s\n  criterion: >-\n    A claim of absence, judged on the paper's test, a two-tailed two-sample K-S test of per-unit\n    mean baseline rates, suppressed population (213) against untuned units, at p < 0.05.\n    Reproduced when p >= 0.05; not reproduced when p < 0.05. The difference of means is reported\n    either way.\n- id: figs4b-activated-increase-suppressed-decrease\n  statement: >-\n    During wall passes the activated population fires more than at baseline (16.44 against 6.36\n    sp/s at the preferred distance) and the suppressed population fires less (4.47 against 6.19\n    sp/s).\n  source: Results, PrV contains both proximity and map codes, paragraph 5; Figure S4B\n  quote: >-\n    During wall-passing period, the activated population increased firing relative to baseline\n    (16.44 ± 1.640 vs. 6.36 ± 0.704 sp/s; one-tailed K-S test: p = 9.26 × 10 −28 ; Supplemental\n    Figure S4B , left), while the suppressed population exhibited a significant decrease in\n    firing (4.47 ± 1.000 vs. 6.19 ± 1.076 sp/s; one-tailed K-S test: p = 3.06 × 10 −4\n  statistics:\n  - about: activated population, wall at preferred distance against baseline\n    test: one-tailed two-sample Kolmogorov-Smirnov test\n    p: 9.26e-28\n    n: 472 units\n  - about: suppressed population, wall at least-preferred distance against baseline\n    test: one-tailed two-sample Kolmogorov-Smirnov test\n    p: 3.06e-4\n    n: 213 units\n  depends_on:\n  - fig2-distance-tuned-counts\n  expected:\n  - quantity: activated population, mean wall rate at preferred distance\n    value: 16.44\n    tolerance: 1.64\n    unit: sp/s\n  - quantity: activated population, mean baseline rate\n    value: 6.36\n    tolerance: 0.704\n    unit: sp/s\n  - quantity: suppressed population, mean wall rate at its minimum\n    value: 4.47\n    tolerance: 1.0\n    unit: sp/s\n  - quantity: suppressed population, mean baseline rate\n    value: 6.19\n    tolerance: 1.076\n    unit: sp/s\n  criterion: >-\n    Per unit, the mean wall rate (3 to 11 s) at the preferred distance (activated) or at the\n    distance of minimum rate (suppressed; Figure S4B legend), against the unit's baseline rate;\n    one-tailed two-sample K-S tests in the stated direction (Methods). The baseline paired with\n    it is not specified, and the paper's 6.36 sp/s differs from the 5.46 sp/s of the same\n    population's all-pass baseline (figs4a-baseline-activated-lower). Readings: (a) baseline of\n    the passes at that same distance; (b) baseline over all passes. Reproduced when both tests\n    give p < 0.05 in the stated direction and the four means are within tolerance under one\n    reading; partially reproduced when both tests hold but no reading puts the means within\n    tolerance.\n- id: figs4c-untuned-no-change\n  statement: >-\n    Untuned units do not change their firing between baseline and wall passes (6.93 against 6.32\n    sp/s).\n  source: Results, PrV contains both proximity and map codes, paragraph 5; Figure S4C\n  quote: >-\n    Untuned units showed no significant change between baseline and wall-passing periods (6.93 ±\n    0.947 vs. 6.32 ± 0.953 sp/s; two-tailed K-S test: p = 0.53\n  statistics:\n  - test: two-tailed two-sample Kolmogorov-Smirnov test\n    p: 0.53\n    n: 177 units\n  depends_on:\n  - fig2f-tuning-categories\n  expected:\n  - quantity: untuned units, mean wall rate averaged over distances\n    value: 6.32\n    tolerance: 0.953\n    unit: sp/s\n  criterion: >-\n    A claim of absence, judged on the paper's test, a two-tailed two-sample K-S test between\n    per-unit mean baseline rates and per-unit wall rates averaged across distances (Figure S4C\n    legend) for untuned units, at p < 0.05. Reproduced when p >= 0.05; not reproduced when p <\n    0.05. The difference of means is reported either way.\n- id: fig2de-preferred-distances-span\n  statement: >-\n    In both the activated and the suppressed populations a large proportion of units prefer the\n    closest wall position (7 mm), while others are best tuned to intermediate or far distances.\n  source: Results, PrV contains both proximity and map codes, paragraph 6; Figure 2D-E; Figure S4D, G\n  quote: >-\n    In both populations, while a large proportion of units preferred the closest wall position (7\n    mm), others were best tuned to intermediate or far distances ( Figure 2E , Supplemental\n    Figure S4G ), revealing coexistence of proximity and map-like coding schemes in PrV\n  depends_on:\n  - fig2-distance-tuned-counts\n  criterion: >-\n    Preferred distance is the maximum of the mean tuning curve (activated population, 472) and\n    the minimum (trough, suppressed population, 213; Figure S4G legend and the code's\n    pref_dist_sup). Reproduced when, in each population, 7 mm is the most frequent preferred\n    distance and at least one unit prefers each of the eight distances from 9 to 23 mm. The\n    paper reports no test; the most frequent bin and coverage of the range are the reading of\n    \"a large proportion ... others\".\n- id: figs4ef-crossvalidated-stability\n  statement: >-\n    Preferred distances of the activated population are stable across two random halves of the\n    wall passes, whereas the suppressed population is only partly reproducible, with only\n    proximity-preferring responses stable.\n  source: Results, PrV contains both proximity and map codes, paragraph 6; Figure S4E-F\n  quote: >-\n    The resulting distance-tuning heatmaps of the activated population revealed little changes in\n    the preferred distance between cross-validated partitions ( Supplemental Figure S4E ). In\n    contrast, the suppressed population showed partial reproducibility, where only\n    proximity-preferring responses were stable, while map-like profiles lacked consistent\n    structure\n  depends_on:\n  - fig2-distance-tuned-counts\n  criterion: >-\n    Per unit, passes at each distance are split at random into two halves (the code draws\n    floor(reps/2) repetition indices without replacement, the same split for all distances of a\n    unit); preferred distance (maximum for activated, minimum for suppressed units) is taken in\n    each half. The paper gives no measure of stability. Readings: (a) the fraction of units whose\n    preferred distance is the same in both halves; (b) the Spearman correlation of preferred\n    distance across halves. Reproduced when, under both readings, the activated population is\n    more stable than the suppressed population, and, within the suppressed population, units\n    whose first-half trough is at 7 mm keep it more often than units with a trough at 9 mm or\n    more. A fixed seed is a standard choice; the split is repeated 100 times and the median\n    reported.\n- id: figs4j-ventral-location\n  statement: >-\n    Wall-responsive units, and proximity and map units among them, lie preferentially in ventral\n    PrV, toward the probe tip.\n  source: Results, PrV contains both proximity and map codes, paragraphs 3 and 7; Figure S4I-J\n  quote: >-\n    We identified 266 proximity units (34.6%) and 118 map units (15.4%) out of the 768\n    wall-responsive units ( Figure 2F ), which were preferentially located in ventral PrV (\n    Supplemental Figure S4J )\n  depends_on:\n  - fig2f-tuning-categories\n  criterion: >-\n    Depth is the shank coordinate of the unit's peak channel (largest peak-to-trough amplitude of\n    the mean waveform) from the probe tip, Poly2 probes only, in 100-um bins (Methods, Unit Depth\n    Along Silicon Probe; FigS4I_probemap.m), n = 1050 well-isolated and 703 wall-responsive units\n    (Figure S4I-J legends). The paper reports no test. Readings: (a) the median depth of\n    wall-responsive units is smaller than that of unresponsive units, and the median depth of\n    proximity and of map units is smaller than that of unresponsive units; (b) the fraction of\n    units that are responsive is higher in the 0 to 400 um half of the shank than in the 400 to\n    800 um half, and so is the fraction that are proximity or map units. Reproduced when both\n    readings agree.\n- id: figs4l-temporal-windows-map\n  statement: >-\n    Applied to temporal windows, the classification finds map units most often in the sustained\n    period (122 of 768, 15.9%), less in the onset period (83, 10.8%) and fewest in the offset\n    period (34, 4.4%).\n  source: Results, PrV contains both proximity and map codes, paragraph 8; Figure S4L\n  quote: >-\n    Map units were most prevalent during the sustained period among wall-responsive units (15.9%,\n    122/768), but were also present during the onset epoch (10.8%, 83/768). In contrast, offset\n    responses yielded fewer map units (4.4%, 34/768)\n  depends_on:\n  - fig2-wall-responsive-counts\n  expected:\n  - quantity: map units, sustained window\n    value: 122\n    tolerance: 12.2\n  - quantity: map units, onset window\n    value: 83\n    tolerance: 8.3\n  - quantity: map units, offset window\n    value: 34\n    tolerance: 3.4\n  criterion: >-\n    The classification of the opening comment with the wall rate taken in the onset (2.5 to 4.5\n    s), sustained (4.5 to 9.5 s) or offset (9.5 to 11.5 s) window. The paper does not say whether\n    the 768 wall-responsive units are reclassified for responsiveness in each window or kept from\n    the full-period classification. Readings: (a) responsiveness kept from the full period, tuning\n    and map tests rerun in each window; (b) all tests rerun in each window. Reproduced when the\n    three counts are within tolerance, and ordered sustained > onset > offset, under one reading;\n    partially reproduced when the order holds but a count is out of tolerance.\n- id: fig3a-decoding-above-controls\n  statement: >-\n    Population decoders trained on map, proximity, suppressed-only and combined map plus\n    proximity units decode wall distance during the contact period better than shuffled and\n    untuned controls.\n  source: Results, The map code in PrV allows more accurate readout, paragraph 1; Figure 3A\n  quote: >-\n    As expected, decoding accuracy during the wall-contact period was higher in the map,\n    proximity, suppressed-only, and combined \"map + proximity\" groups compared to shuffled and\n    untuned controls ( Figure 3A )\n  statistics:\n  - about: suppressed-only against shuffled, each of nine distances\n    test: Wilcoxon rank-sum test\n    p: 1.83e-4\n    corrected: BH-FDR\n    n: 10 subsamples per group\n  depends_on:\n  - fig2f-tuning-categories\n  criterion: >-\n    Decoding as in the opening comment. Reproduced when the overall accuracy (mean over the nine\n    distances, 3 to 11 s) of each of the four groups exceeds that of both the shuffled and the\n    untuned groups, and a one-sided Wilcoxon rank-sum test on the 10 subsample values has p <\n    0.05 for each such pair, under the Methods' 10-fold cross-validation and under the code's 15\n    splits.\n- id: fig3-overall-decoding-accuracy\n  statement: >-\n    Averaged across the nine distances, the map group decodes best (71.5%), ahead of the combined\n    map plus proximity group (58.6%) and the proximity group (48.9%); the suppressed-only group\n    reaches 32.6% and untuned units 15.7%, against a chance level of 11.1%.\n  source: Results, The map code in PrV allows more accurate readout, paragraph 1; Table S2\n  quote: >-\n    the map group achieved the highest overall decoding accuracy averaged across all nine\n    distances (71.5%), outperforming the proximity (48.9%) and combined \"map + proximity\" (58.6%)\n    groups. The suppressed-only group had an average overall decoding accuracy of 32.6%. Untuned\n    units performed slightly above chance (15.7%)\n  depends_on:\n  - fig2f-tuning-categories\n  expected:\n  - quantity: overall accuracy, map\n    value: 71.53\n    tolerance: 7.15\n    unit: percent\n  - quantity: overall accuracy, combined map plus proximity\n    value: 58.55\n    tolerance: 5.86\n    unit: percent\n  - quantity: overall accuracy, proximity\n    value: 48.86\n    tolerance: 4.89\n    unit: percent\n  - quantity: overall accuracy, suppressed-only\n    value: 32.56\n    tolerance: 3.26\n    unit: percent\n  - quantity: overall accuracy, untuned\n    value: 15.73\n    tolerance: 1.57\n    unit: percent\n  - quantity: overall accuracy, shuffled\n    value: 10.9\n    tolerance: 1.09\n    unit: percent\n  criterion: >-\n    Decoding as in the opening comment; values from the Table S2 \"Average\" row. The text says\n    \"During the sustained wall-passing period\" while the Methods, the code (summary_period 3000\n    to 11000 ms) and the Table give the 3 to 11 s contact period. Readings: window (i) 3 to 11 s\n    (main), (ii) 4.5 to 9.5 s; cross-validation (x) 10-fold (Methods), (y) 15 splits (code).\n    Reproduced when the order map > combined > proximity > suppressed-only > untuned > shuffled\n    holds and all six values are within tolerance under one reading; partially reproduced when\n    the order holds with the map group first but values are out of tolerance.\n- id: fig3c-decoding-by-distance\n  statement: >-\n    At the two closest distances (7 and 9 mm) the combined map plus proximity and proximity\n    groups decode most accurately, whereas the map group is most accurate at 11 to 23 mm.\n  source: Results, The map code in PrV allows more accurate readout, paragraph 2; Figure 3B-C; Table S2\n  quote: >-\n    At the closest distances (7 and 9 mm), the combined \"map + proximity\" and proximity\n    populations achieved the highest accuracy. In contrast, the map population was most accurate\n    at decoding more distal wall positions (11–23 mm)\n  statistics:\n  - about: proximity against map at 7 mm, MCC accuracy\n    test: Wilcoxon rank-sum test\n    p: 2.06e-4\n    corrected: BH-FDR\n    n: 10 subsamples per group\n  - about: proximity against map plus proximity at 7 mm, MCC accuracy\n    test: Wilcoxon rank-sum test\n    p: 0.18\n    corrected: BH-FDR\n    n: 10 subsamples per group\n  - about: map against map plus proximity at each distance, MCC accuracy\n    test: Wilcoxon rank-sum test\n    p: 1.83e-4\n    corrected: BH-FDR\n    n: 10 subsamples per group\n  depends_on:\n  - fig3-overall-decoding-accuracy\n  expected:\n  - quantity: MCC accuracy at 7 mm, combined\n    value: 88.48\n    tolerance: 8.85\n    unit: percent\n  - quantity: MCC accuracy at 7 mm, proximity\n    value: 87.84\n    tolerance: 8.78\n    unit: percent\n  - quantity: MCC accuracy at 7 mm, map\n    value: 81.14\n    tolerance: 8.11\n    unit: percent\n  - quantity: MCC accuracy at 15 mm, map\n    value: 82.5\n    tolerance: 8.25\n    unit: percent\n  - quantity: MCC accuracy at 15 mm, proximity\n    value: 36.29\n    tolerance: 3.63\n    unit: percent\n  criterion: >-\n    Per-distance accuracy as in the opening comment, with the readings of\n    fig3-overall-decoding-accuracy. Tolerances are 10% of the Table S2 values; the Table's 95%\n    CIs over 10 subsamples (0.1 to 3 points) are left aside because a rerun draws new subsamples.\n    Reproduced when, under one reading, (a) at 7 and at 9 mm the combined and proximity groups\n    both exceed the map group, (b) at each of 11 to 23 mm the map group exceeds every other\n    group, with the per-distance rank-sum tests (BH-FDR over nine distances) of map against\n    proximity and map against combined giving q < 0.05 at 11 to 23 mm, and (c) the five values\n    are within tolerance. Partially reproduced when (a) and (b) hold at all but one distance.\n- id: fig3c-decoding-error\n  statement: >-\n    Decoding error grows with distance; proximity, map and combined groups reach submillimetre\n    error at 7 and 9 mm, and only the map group is submillimetre at 13 and 15 mm.\n  source: Results, The map code in PrV allows more accurate readout, paragraph 2; Figure 3C right; Table S3\n  quote: >-\n    While classification error generally increased with distance, proximity, map, and the\n    combined \"map + proximity\" groups showed submillimeter precision when decoding the two\n    closest distances (7 and 9 mm; Figure 3C , right; Table S3 ). Only the map population\n    achieved submillimeter error at the intermediate distances of 13 and 15 mm\n  depends_on:\n  - fig3-overall-decoding-accuracy\n  expected:\n  - quantity: MCC error at 13 mm, map\n    value: 0.7\n    tolerance: 0.07\n    unit: mm\n  - quantity: MCC error at 15 mm, map\n    value: 0.78\n    tolerance: 0.078\n    unit: mm\n  - quantity: mean MCC error over distances, map\n    value: 0.86\n    tolerance: 0.086\n    unit: mm\n  - quantity: mean MCC error over distances, proximity\n    value: 1.78\n    tolerance: 0.178\n    unit: mm\n  criterion: >-\n    Error per true distance is the confusion-matrix-weighted mean of the absolute difference\n    between predicted and true distance, averaged over time bins in the contact period (Methods;\n    code err_by_distance). Readings as in fig3-overall-decoding-accuracy. Reproduced when, under\n    one reading, proximity, map and combined errors are below 1 mm at 7 and 9 mm, the map error\n    is below 1 mm at 13 and 15 mm while proximity and combined errors are not, and the four values\n    are within tolerance.\n- id: figs5c-single-neuron-decoders\n  statement: >-\n    Single-neuron decoders show the same pattern with lower accuracy than population decoders,\n    proximity units being more accurate than map units at 7 mm and map units more accurate at 11\n    to 17 mm.\n  source: Results, The map code in PrV allows more accurate readout, paragraph 2; Figure S5B-C; Table S4\n  quote: >-\n    These results are consistent with the performance of single-neuron decoders, although their\n    overall decoding accuracy is lower than that of population decoders\n  statistics:\n  - about: proximity against map at 7 mm\n    test: Wilcoxon rank-sum test\n    p: 0.01\n    corrected: BH-FDR\n    n: 266 proximity and 118 map units\n  - about: proximity against map at 13, 15 and 17 mm\n    test: Wilcoxon rank-sum test\n    p: 0.001\n    p_relation: \"<\"\n    corrected: BH-FDR\n    n: 266 proximity and 118 map units\n  depends_on:\n  - fig2f-tuning-categories\n  expected:\n  - quantity: single-neuron accuracy at 7 mm, proximity\n    value: 65.84\n    tolerance: 2.582\n    unit: percent\n  - quantity: single-neuron accuracy at 7 mm, map\n    value: 59.08\n    tolerance: 3.702\n    unit: percent\n  - quantity: single-neuron accuracy at 15 mm, map\n    value: 34.72\n    tolerance: 4.463\n    unit: percent\n  - quantity: single-neuron accuracy at 15 mm, proximity\n    value: 18.84\n    tolerance: 2.154\n    unit: percent\n  criterion: >-\n    Per unit, spike counts in 200-ms bins over 3 to 11 s; a template (mean over training passes)\n    per distance; nearest template in Euclidean distance; leave-two-out cross-validation (two\n    passes per distance held out, exhaustively); accuracy the fraction of correct test passes\n    (Methods). Tolerances are the Table S4 95% CIs across units. Per-distance proximity against\n    map with Wilcoxon rank-sum tests, BH-FDR over nine distances. Reproduced when proximity\n    exceeds map at 7 mm and map exceeds proximity at 11, 13, 15 and 17 mm, each with q < 0.05,\n    every single-neuron group's mean accuracy is below the corresponding population value of\n    fig3-overall-decoding-accuracy, and the four values are within tolerance; partially\n    reproduced when the directions hold but some tests or values do not.\n- id: figs5de-svm-robust\n  statement: >-\n    The ranking of subpopulations is robust to the decoder; with a linear SVM the map group\n    still has the highest average accuracy (72.1%) and proximity and combined groups are best at\n    the closest distance.\n  source: Results, The map code in PrV allows more accurate readout, paragraph 2; Figure S5D-E; Tables S2-S3\n  quote: >-\n    Importantly, these findings were robust to the choice of decoder (see STAR Methods ,\n    Supplemental Figure S5D , E , and Tables S2 , S3 for SVM classifier)\n  depends_on:\n  - fig3-overall-decoding-accuracy\n  expected:\n  - quantity: SVM overall accuracy, map\n    value: 72.14\n    tolerance: 7.21\n    unit: percent\n  - quantity: SVM overall accuracy, combined\n    value: 54.43\n    tolerance: 5.44\n    unit: percent\n  - quantity: SVM overall accuracy, proximity\n    value: 52.79\n    tolerance: 5.28\n    unit: percent\n  - quantity: SVM overall accuracy, suppressed-only\n    value: 35.01\n    tolerance: 3.5\n    unit: percent\n  criterion: >-\n    As fig3-overall-decoding-accuracy and fig3c-decoding-by-distance with the Neural Decoding\n    Toolbox libsvm_CL, linear kernel, C = 1, one-versus-one (Methods). Reproduced when, under one\n    reading, the map group has the highest overall accuracy, the proximity and combined groups\n    both exceed the map group at 7 mm, the map group is highest at 13 to 23 mm, and the four\n    values are within tolerance.\n- id: fig4-cut-baseline-unchanged\n  statement: >-\n    Cutting all whiskers but one does not change baseline firing across the recorded population\n    (7.09 against 7.10 sp/s; 195 units from 18 mice).\n  source: Results, PrV map tuning can persist, paragraph 2\n  quote: >-\n    Across the recorded population (n = 195 units from 18 mice), acute whisker cutting did not\n    significantly alter baseline firing rates, measured before wall-movement onset for each wall\n    pass (full array: 7.09 ± 1.034 vs. single whisker: 7.10 ± 1.038 sp/s; Wilcoxon signed-rank\n    test: p = 0.70)\n  statistics:\n  - test: two-sided Wilcoxon signed-rank test\n    p: 0.7\n    n: 195 units from 18 mice\n  expected:\n  - quantity: whisker-cutting units\n    value: 195\n    tolerance: 19.5\n  - quantity: mean baseline rate, full array\n    value: 7.09\n    tolerance: 1.034\n    unit: sp/s\n  - quantity: mean baseline rate, single whisker\n    value: 7.1\n    tolerance: 1.038\n    unit: sp/s\n  criterion: >-\n    A claim of absence, judged on the paper's test, a two-sided Wilcoxon signed-rank test of\n    per-unit mean baseline rates (-4.5 to 0 s, over all passes) between full-array and\n    single-whisker conditions, at p < 0.05 (Methods; Fig4BC_WhiskerCutting_pairwise_FR_PrefDist.m,\n    signrank on fr_base). Units are those passing the unit criteria with stable waveforms in both\n    conditions (Methods). Reproduced when p >= 0.05; not reproduced when p < 0.05. The difference\n    of means is reported either way.\n- id: fig4b-cut-wall-firing-reduced\n  statement: >-\n    In the 86 wall-activated, distance-tuned units, firing during wall passes falls after cutting\n    to a single whisker (11.58 against 8.18 sp/s), in many cases to below 1 sp/s.\n  source: Results, PrV map tuning can persist, paragraph 2; Figure 4B\n  quote: >-\n    firing rates of wall-activated, distance-tuned units (activated population; n = 86) during\n    wall-passing periods were significantly reduced following cutting down to a single whisker\n    (full array: 11.58 ± 1.338 vs. single whisker: 8.18 ± 2.602 sp/s, p = 4.43 × 10 −8 ; Figure\n    4B )\n  statistics:\n  - test: two-sided Wilcoxon signed-rank test\n    p: 4.43e-8\n    n: 86 units from 18 mice\n  depends_on:\n  - fig4-cut-baseline-unchanged\n  expected:\n  - quantity: activated tuned units in cutting sessions\n    value: 86\n    tolerance: 8.6\n  - quantity: mean wall rate, full array\n    value: 11.58\n    tolerance: 1.338\n    unit: sp/s\n  - quantity: mean wall rate, single whisker\n    value: 8.18\n    tolerance: 2.602\n    unit: sp/s\n  criterion: >-\n    Units activated and distance-tuned in the full-array condition (classification of the\n    opening comment). The per-unit wall rate in the code is the median over distances of the\n    per-distance mean rate (fr_wall = median of fr_mean); the Methods say mean firing rate during\n    wall passes. Readings: (a) median over distances (code); (b) mean over all passes (Methods).\n    Two-sided Wilcoxon signed-rank test. The full-array spread is printed as 1.338 in the text\n    and 2.986 in the Figure 4B legend; the larger is used as the tolerance. Reproduced when p <\n    0.05 with lower single-whisker rates and the three values within tolerance under one reading;\n    partially reproduced when the test holds but a value does not.\n- id: fig4b-cut-per-unit-changes\n  statement: >-\n    Of the 86 activated units, 66 change firing significantly after cutting, 52 decreasing and 14\n    increasing.\n  source: Results, PrV map tuning can persist, paragraph 2; Figure 4B\n  quote: >-\n    Among the 86 activated units, 66 showed significant changes in firing rates during\n    wall-passing periods between cutting conditions (two-sided Wilcoxon signed-rank test, p <\n    0.05). Of these 66 units, 52 exhibited a significant decrease in firing rates ... whereas 14\n    units displayed increased firing rates\n  depends_on:\n  - fig4b-cut-wall-firing-reduced\n  expected:\n  - quantity: units with a significant change\n    value: 66\n    tolerance: 6.6\n  - quantity: units with a significant decrease\n    value: 52\n    tolerance: 5.2\n  - quantity: units with a significant increase\n    value: 14\n    tolerance: 1.4\n  criterion: >-\n    Per unit, two-sided Wilcoxon signed-rank test of per-pass wall rates (3 to 11 s) between\n    conditions, passes paired in order and truncated to the shorter condition (code), direction\n    from the sign of the median difference (code). The paper gives three corrections. Readings:\n    (a) uncorrected p < 0.05 (Results); (b) BH-FDR across the 86 units (Methods, Data Analysis:\n    Acute Whisker-Cutting Manipulation; code mafdr); (c) Bonferroni across units (Methods,\n    Characterizing Wall Distance Tuning; code alpha / (2n)). The code also differs on the pass\n    set: (i) all passes pooled over distances; (ii) the code's exact-test block over repetitions.\n    Reproduced when the three counts are within tolerance under one reading.\n- id: fig4c-map-units-after-cut\n  statement: >-\n    Of 21 map units in the full-array condition, 10 remain distance-tuned after cutting to a\n    single whisker; of these, 2 shift their preferred distance to the closest distance (becoming\n    proximity units), 6 shift their preferred distance while keeping map tuning, and 2 keep their\n    preferred distance with a change in gain.\n  source: Results, PrV map tuning can persist, paragraph 3; Figure 4C-I\n  quote: >-\n    Of the 21 units categorized as map cells in the full-array condition, 10 remained\n    significantly tuned to wall distance after cutting down to a single whisker ... Two units\n    shifted their preferred distance to the closest distance ( Figure 4D , E ), effectively\n    converting from map cells to proximity cells. In contrast, six units shifted their preferred\n    distance while retaining map tuning (e.g., Figure 4F , G ), and two additional units\n    preserved their preferred distance but changed in response gain\n  depends_on:\n  - fig4b-cut-wall-firing-reduced\n  expected:\n  - quantity: map units in full-array condition\n    value: 21\n    tolerance: 2.1\n  - quantity: map units still tuned after cutting\n    value: 10\n    tolerance: 1.0\n  - quantity: map units converted to proximity\n    value: 2\n    tolerance: 0.2\n  - quantity: map units shifting preference but staying map\n    value: 6\n    tolerance: 0.6\n  - quantity: map units keeping preferred distance\n    value: 2\n    tolerance: 0.2\n  - quantity: activated units still tuned after cutting (Figure 4C)\n    value: 33\n    tolerance: 3.3\n  criterion: >-\n    Classification of the opening comment run separately on full-array and single-whisker\n    passes. \"Remained tuned\" is read as in the code, activated and distance-tuned in the\n    single-whisker condition and not silenced (activated_tuned_mask); the variant drops the\n    activation requirement. Map after cutting means the map category in the single-whisker\n    condition (with the map test); a variant counts any preferred distance above 7 mm. Reproduced\n    when all six counts are within tolerance under one reading; partially reproduced when the\n    first two are and the split of the 10 is off by at most one unit per class. Gain change is\n    reported, not judged, as the paper gives no measure.\n- id: fig4jk-proximity-units-after-cut\n  statement: >-\n    Of 45 proximity units in the full-array condition only 15 remain distance-selective after\n    cutting; 9 stay proximity units with lower gain, 4 stay proximity units with higher gain, and\n    2 become map units.\n  source: Results, PrV map tuning can persist, paragraph 4; Figure 4J-K\n  quote: >-\n    Of the 45 units categorized as proximity cells before whisker cutting, only 15 remained\n    distance-selective after cutting down to a single whisker. Of these 15 units, nine remained\n    proximity cells with reduced response gain ... four remained proximity cells with increased\n    response gain ... and two shifted to exhibit map tuning\n  depends_on:\n  - fig4b-cut-wall-firing-reduced\n  expected:\n  - quantity: proximity units in full-array condition\n    value: 45\n    tolerance: 4.5\n  - quantity: proximity units still tuned after cutting\n    value: 15\n    tolerance: 1.5\n  - quantity: proximity units staying proximity with lower gain\n    value: 9\n    tolerance: 0.9\n  - quantity: proximity units staying proximity with higher gain\n    value: 4\n    tolerance: 0.4\n  - quantity: proximity units becoming map\n    value: 2\n    tolerance: 0.2\n  criterion: >-\n    As fig4c-map-units-after-cut. Gain is not defined in the paper. Readings for lower or higher\n    gain: (a) the unit's peak mean wall rate in the single-whisker condition below or above that\n    in the full-array condition; (b) its mean wall rate over distances below or above. Reproduced\n    when all five counts are within tolerance under one reading.\n- id: figs5fg-cut-decoding\n  statement: >-\n    Whisker cutting lowers population decoding accuracy in both map (31.0 to 21.5%) and proximity\n    (24.1 to 20.2%) populations of 21 units, with the largest decreases at intermediate and far\n    distances in the map population and less effect at the closest distances.\n  source: Results, PrV map tuning can persist, paragraph 5; Figure S5F-G\n  quote: >-\n    Whisker cutting reduced overall decoding accuracy in both populations (map: 31.0 ± 0.10% vs.\n    21.5 ± 0.08%; proximity: 24.1 ± 0.82% vs. 20.2 ± 1.22%; mean ± 95% CI for full-array vs.\n    single-whisker conditions), with the largest decreases occurring at intermediate and far\n    distances in the map population\n  statistics:\n  - about: map population, full array\n    ci:\n      level: 0.95\n      low: 30.9\n      high: 31.1\n      unit: percent\n  - about: map population, single whisker\n    ci:\n      level: 0.95\n      low: 21.42\n      high: 21.58\n      unit: percent\n  - about: proximity population, full array\n    ci:\n      level: 0.95\n      low: 23.28\n      high: 24.92\n      unit: percent\n  - about: proximity population, single whisker\n    ci:\n      level: 0.95\n      low: 18.98\n      high: 21.42\n      unit: percent\n  depends_on:\n  - fig4c-map-units-after-cut\n  - fig4jk-proximity-units-after-cut\n  expected:\n  - quantity: overall accuracy, map, full array\n    value: 31.0\n    tolerance: 3.1\n    unit: percent\n  - quantity: overall accuracy, map, single whisker\n    value: 21.5\n    tolerance: 2.15\n    unit: percent\n  - quantity: overall accuracy, proximity, full array\n    value: 24.1\n    tolerance: 2.41\n    unit: percent\n  - quantity: overall accuracy, proximity, single whisker\n    value: 20.2\n    tolerance: 2.02\n    unit: percent\n  criterion: >-\n    MCC decoders as in the opening comment, trained and tested within each condition on units\n    recorded in both, grouped by full-array category; map n = 21, proximity 21 of 45 drawn 10\n    times (Methods). Tolerances are 10%: the printed CIs (0.08 to 1.2 points) describe the spread\n    over subsamples, not a rerun's error. Readings for cross-validation as in\n    fig3-overall-decoding-accuracy. Reproduced when, under one reading, accuracy falls in both\n    populations, the map population's drop summed over 11 to 23 mm exceeds its drop summed over 7\n    and 9 mm, and the four values are within tolerance; partially reproduced when the falls and\n    the distance pattern hold but values do not.\n- id: figs6-opto-local-inhibition-gain\n  statement: >-\n    Optogenetic silencing of local PrV inhibitory neurons (GtACR in vGat-Cre mice) strongly\n    inhibits 18 of 112 units (putative inhibitory neurons); among 71 distance-tuned units, 17 are\n    inhibited and 16 disinhibited by light, and disinhibited units keep their preferred distance,\n    so local inhibition affects gain without changing distance preference.\n  source: Results, Inhibition contributes to the PrV map code, paragraph 2; Figure S6B-G\n  quote: >-\n    Among the 112 well-isolated units, 18 were putative inhibitory neurons expressing GtACR, as\n    they were strongly inhibited during the \"Laser ON\" period (modulation index ≤ −0.5 ... Of\n    distance-tuned units (71/112), 17 were opto-inhibited ... Sixteen units showed a reduction\n    in inhibition under the \"Laser ON\" condition (modulation index > 0 ... Nonetheless, these\n    opto-disinhibited neurons, regardless of whether they were proximity or map cells, retained\n    their preferred distance\n  expected:\n  - quantity: GtACR units\n    value: 112\n    tolerance: 11.2\n  - quantity: strongly inhibited units (MI at most -0.5)\n    value: 18\n    tolerance: 1.8\n  - quantity: distance-tuned units\n    value: 71\n    tolerance: 7.1\n  - quantity: inhibited distance-tuned units\n    value: 17\n    tolerance: 1.7\n  - quantity: disinhibited distance-tuned units\n    value: 16\n    tolerance: 1.6\n  criterion: >-\n    MI = (FR on - FR off) / (FR on + FR off) of mean wall-period rates; a unit is modulated when\n    its bootstrap CI on MI excludes zero; strongly inhibited MI <= -0.5, inhibited -0.5 < MI < 0,\n    disinhibited MI > 0 (Methods). The paper does not give the CI level or what is resampled;\n    readings, 95% percentile CI from 10,000 resamples (the paper's bootstrap elsewhere) of (a)\n    passes within each laser condition, (b) passes within each condition and distance. Tuning is\n    classified on laser-off passes at the five distances (7 to 23 mm in 4-mm steps). Reproduced\n    when the five counts are within tolerance under one reading and at least 12 of the\n    disinhibited tuned units have the same preferred distance with laser on as off; the paper\n    says all retained it but gives no number, so the share is reported. The 17 inhibited units\n    are counted among tuned units with MI below 0 (strongly or not); whether the 18 strongly\n    inhibited are inside the 17 is not said, so both counts are compared as printed.\n- id: figs6i-telc-kinematics-unchanged\n  statement: >-\n    Chronic TeLC expression in SpVi does not change whisker kinematics during wall passes\n    (whisker-array midpoint angle; mean difference 0.84 degrees, Wald t = 1.02, p = 0.31).\n  source: Results, Inhibition contributes to the PrV map code, paragraph 4; Figure S6I\n  quote: >-\n    Chronic TeLC expression in SpVi did not significantly alter whisker kinematics during wall\n    passes, as measured by whisker array midpoint angle (mean difference across distance = 0.84°;\n    two-tailed Wald's t -test: t = 1.02, p = 0.31\n  statistics:\n  - test: two-tailed Wald t-test on the TeLC fixed effect of a linear mixed-effects model\n    statistic: t = 1.02\n    p: 0.31\n    n: 15 sessions from 6 wild-type and 15 sessions from 6 SpVi-TeLC mice\n  expected:\n  - quantity: mean difference in midpoint angle, TeLC minus wild type\n    value: 0.84\n    tolerance: 0.084\n    unit: degrees\n  - quantity: group mean change in midpoint angle, wild type\n    value: -5.35\n    tolerance: 0.445\n    unit: degrees\n  - quantity: group mean change in midpoint angle, SpVi-TeLC\n    value: -4.51\n    tolerance: 0.738\n    unit: degrees\n  criterion: >-\n    A claim of absence, judged on the paper's test (Methods, Whisker Kinematics, Wild-Type vs\n    SpVi-TeLC). Per pass, the change in midpoint angle averaged across tracked whiskers per\n    frame; fitlme by maximum likelihood, theta_mid ~ TeLC + distance + (1|subject) + (1|session),\n    two-sided Wald test of TeLC at p < 0.05. Reproduced when p >= 0.05, and no per-distance model\n    theta_mid ~ TeLC + (1|subject) + (1|session) gives p < 0.05 (Figure S6I legend); not\n    reproduced otherwise. The effect size is reported either way. The legend's group means\n    carry its printed spread as tolerance.\n- id: telc-unit-yield\n  statement: >-\n    In SpVi-TeLC mice, 587 of 665 sorted PrV units from 11 mice passed the unit criteria, of\n    which 395 were wall-responsive and 252 wall-activated and distance-tuned.\n  source: Methods, Isolation of Single Unit Activity; Figure 5C, E legends\n  quote: >-\n    in TeLC experiments, 587 of 665 units (11 mice)\n  expected:\n  - quantity: TeLC units passing criteria\n    value: 587\n    tolerance: 58.7\n  - quantity: TeLC wall-responsive units\n    value: 395\n    tolerance: 39.5\n  - quantity: TeLC activated and distance-tuned units\n    value: 252\n    tolerance: 25.2\n  - quantity: TeLC mice\n    value: 11\n    tolerance: 0\n  criterion: >-\n    Unit criteria and classification as in the opening comment (the same code,\n    Fig5CE_TeLC_heatmap_stacked_bar.m). Reproduced when all four values are within tolerance\n    under one responsiveness reading.\n- id: fig5d-telc-preferred-closer\n  statement: >-\n    Wall-activated, distance-tuned units in SpVi-TeLC mice prefer closer distances than those in\n    wild-type mice.\n  source: Results, Inhibition contributes to the PrV map code, paragraph 4; Figure 5C-D\n  quote: >-\n    Comparison of normalized tuning curves of all wall-activated, distance-tuned units revealed a\n    reduction in the proportion of map units in SpVi-TeLC mice ( Figure 5C ) relative to\n    wild-type mice ( Figure 2D ), shifting the population to prefer closer distances ( Figure 5D\n    )\n  statistics:\n  - test: one-tailed two-sample Kolmogorov-Smirnov test\n    p: 8.02e-5\n    n: 472 wild-type and 252 SpVi-TeLC units\n  depends_on:\n  - fig2-distance-tuned-counts\n  - telc-unit-yield\n  criterion: >-\n    Preferred distance (maximum of the mean tuning curve, binned to the nine centres) of\n    activated, distance-tuned units; one-tailed two-sample K-S test that TeLC preferred distances\n    are smaller (Fig5D_TeLC_Pref_Dist_CDF.m, kstest2 with Tail smaller, wild type first).\n    Population readings: (a) activated and distance-tuned (Figure 5D legend, \"same units in C\");\n    (b) activated without the tuning requirement (the code's mask1 and mask2). Reproduced when p\n    < 0.05 under reading (a); the result under (b) is shown as a variant.\n- id: fig5e-telc-category-shift\n  statement: >-\n    Among wall-responsive units, SpVi-TeLC mice have nearly threefold fewer map units than\n    wild-type mice (5.8 against 15.4%), more proximity units (47.9 against 34.6%) and modestly\n    fewer suppressed-only units (10.9 against 15.5%).\n  source: Results, Inhibition contributes to the PrV map code, paragraph 4; Figure 5E\n  quote: >-\n    In particular, the proportion of map units was nearly threefold lower in SpVi-TeLC mice than\n    in wild-type mice (5.8% vs 15.4%; Z -statistic: 4.721, p = 1.2×10 −6 ), whereas the\n    proportion of proximity units increased (47.9% vs 34.6%; Z -statistic: −4.33, p = 7.5×10 −6\n    ) ... The proportion of suppressed units decreased modestly (10.9% vs 15.5%; Z -statistic:\n    2.15, p = 0.02)\n  statistics:\n  - about: map units\n    test: one-tailed two-proportion Z-test\n    statistic: Z = 4.721\n    p: 1.2e-6\n    n: 768 wild-type and 395 SpVi-TeLC wall-responsive units\n  - about: proximity units\n    test: one-tailed two-proportion Z-test\n    statistic: Z = -4.33\n    p: 7.5e-6\n    n: 768 wild-type and 395 SpVi-TeLC wall-responsive units\n  - about: suppressed-only units\n    test: one-tailed two-proportion Z-test\n    statistic: Z = 2.15\n    p: 0.02\n    n: 768 wild-type and 395 SpVi-TeLC wall-responsive units\n  depends_on:\n  - fig2f-tuning-categories\n  - telc-unit-yield\n  expected:\n  - quantity: map share, SpVi-TeLC\n    value: 5.8\n    tolerance: 0.58\n    unit: percent of wall-responsive units\n  - quantity: proximity share, SpVi-TeLC\n    value: 47.9\n    tolerance: 4.79\n    unit: percent of wall-responsive units\n  - quantity: suppressed-only share, SpVi-TeLC\n    value: 10.9\n    tolerance: 1.09\n    unit: percent of wall-responsive units\n  criterion: >-\n    Shares of the five categories among wall-responsive units in each group; pooled two-proportion\n    Z = (p_WT - p_TeLC) / SE, one-tailed in the paper's direction (map and suppressed-only lower,\n    proximity higher in TeLC; Methods; Fig5CE code). The Methods' denominator is \"the total number\n    of recorded units\" while the legend and the code use wall-responsive units; readings (a)\n    wall-responsive units (768 and 395, main), (b) all units passing criteria (1141 and 587).\n    Reproduced when the three tests give p < 0.05 in the stated directions and the three TeLC\n    shares are within tolerance under reading (a); partially reproduced when the map and\n    proximity tests hold but the suppressed-only test or a share does not.\n- id: fig5e-telc-untuned-ambiguous-unchanged\n  statement: >-\n    The shares of untuned (25.3 against 23.0%) and ambiguous (10.1 against 11.5%) units do not\n    differ between SpVi-TeLC and wild-type mice.\n  source: Results, Inhibition contributes to the PrV map code, paragraph 4; Figure 5E legend\n  quote: >-\n    whereas the proportions of untuned (25.3% vs 23.0%; Z -statistic: −0.86, p = 0.39) and\n    ambiguous units (10.1% vs 11.5%; Z -statistic: 0.62, p = 0.53) remained unchanged\n  statistics:\n  - about: untuned units\n    test: two-tailed two-proportion Z-test\n    statistic: Z = -0.86\n    p: 0.39\n  - about: ambiguous units\n    test: two-tailed two-proportion Z-test\n    statistic: Z = 0.62\n    p: 0.53\n  depends_on:\n  - fig5e-telc-category-shift\n  criterion: >-\n    A claim of absence, judged on the paper's test, two-tailed pooled two-proportion Z-tests\n    (Figure 5E legend; code) on shares of wall-responsive units, at p < 0.05. Reproduced when\n    neither test gives p < 0.05; not reproduced when either does. The difference in share is\n    reported for each.\n- id: figs6j-telc-untuned-higher-firing\n  statement: >-\n    Untuned units in SpVi-TeLC mice fire more than in wild-type mice at baseline (10.01 against\n    6.93 sp/s) and during wall passes (9.64 against 6.32 sp/s).\n  source: Results, Inhibition contributes to the PrV map code, paragraph 5; Figure S6J\n  quote: >-\n    During both baseline and wall-passing periods, untuned units in SpVi-TeLC mice exhibited\n    significantly higher firing rates than those in the wild-type population, consistent with\n    loss of long-range inhibitory inputs from SpVi (baseline: 10.01 ± 2.431 vs 6.93 ± 0.947 sp/s,\n    p = 3.98 × 10 −5 ; wall passes: 9.64 ± 2.772 vs. 6.32 ± 0.953 sp/s, p =9.64 × 10 −4 ;\n    one-tailed K-S tests\n  statistics:\n  - about: baseline rates\n    test: one-tailed two-sample Kolmogorov-Smirnov test\n    p: 3.98e-5\n    corrected: Bonferroni, four comparisons (alpha 0.0125)\n  - about: wall-pass rates averaged across distances\n    test: one-tailed two-sample Kolmogorov-Smirnov test\n    p: 9.64e-4\n    corrected: Bonferroni, four comparisons (alpha 0.0125)\n  depends_on:\n  - fig2f-tuning-categories\n  - telc-unit-yield\n  expected:\n  - quantity: mean baseline rate, TeLC untuned\n    value: 10.01\n    tolerance: 2.431\n    unit: sp/s\n  - quantity: mean wall rate, TeLC untuned\n    value: 9.64\n    tolerance: 2.772\n    unit: sp/s\n  criterion: >-\n    Per-unit mean baseline rate and wall rate averaged across distances; one-tailed two-sample\n    K-S tests (TeLC higher), significant at 0.0125 (Figure S6K legend, four comparisons). The\n    baseline p-value is printed as 3.98 x 10^-5 in the text and 3.98 x 10^-3 in the legend; both\n    are below 0.0125. Untuned population readings: (a) wall-responsive but not distance-tuned\n    (177 wild type, the population whose 6.93 and 6.32 sp/s match Figure S4); (b) the Table S5\n    \"untuned\" sets (550 wild type, 294 TeLC), every unit outside the activated-tuned and\n    suppressed-only groups. Reproduced when both tests give p < 0.0125 and both TeLC means are\n    within tolerance under one reading.\n- id: figs6k-telc-tuned-baseline-similar\n  statement: >-\n    Wall-activated, distance-tuned units in SpVi-TeLC mice have baseline firing comparable to\n    wild type (5.60 against 5.46 sp/s).\n  source: Results, Inhibition contributes to the PrV map code, paragraph 5; Figure S6K left\n  quote: >-\n    In contrast, distance-tuned units in SpVi-TeLC mice showed baseline activity comparable to\n    that of wild-type mice in the absence of wall contact (5.60 ± 0.845 vs. 5.46 ± 0.670 sp/s;\n    one-tailed K-S test: p = 0.14)\n  statistics:\n  - test: one-tailed two-sample Kolmogorov-Smirnov test\n    p: 0.14\n    n: 252 SpVi-TeLC and 472 wild-type units\n  depends_on:\n  - fig5d-telc-preferred-closer\n  expected:\n  - quantity: mean baseline rate, TeLC activated tuned units\n    value: 5.6\n    tolerance: 0.845\n    unit: sp/s\n  criterion: >-\n    A claim of absence, judged on the paper's test, a one-tailed two-sample K-S test (TeLC\n    higher) of per-unit mean baseline rates of activated, distance-tuned units, at the legend's\n    Bonferroni level 0.0125. Reproduced when p >= 0.0125; not reproduced when p < 0.0125. The\n    result at 0.05 and the difference of means are reported as well.\n- id: figs6k-telc-tuned-wall-higher\n  statement: >-\n    During wall contact, wall-activated, distance-tuned units in SpVi-TeLC mice fire more than in\n    wild type (9.96 against 9.02 sp/s, averaged across distances).\n  source: Results, Inhibition contributes to the PrV map code, paragraph 5; Figure S6K right\n  quote: >-\n    but exhibited significantly greater wall-evoked firing (9.96 ± 1.209 vs. 9.02 ± 1.005 sp/s;\n    one-tailed K-S test: p = 9.34 × 10 −3\n  statistics:\n  - test: one-tailed two-sample Kolmogorov-Smirnov test\n    p: 9.34e-3\n    corrected: Bonferroni, four comparisons (alpha 0.0125)\n    n: 252 SpVi-TeLC and 472 wild-type units\n  depends_on:\n  - fig5d-telc-preferred-closer\n  expected:\n  - quantity: mean wall rate, TeLC activated tuned units\n    value: 9.96\n    tolerance: 1.209\n    unit: sp/s\n  - quantity: mean wall rate, wild-type activated tuned units\n    value: 9.02\n    tolerance: 1.005\n    unit: sp/s\n  criterion: >-\n    Per-unit wall rate (3 to 11 s) averaged across the nine distances; one-tailed two-sample K-S\n    test (TeLC higher). Reproduced when p < 0.0125 and both means are within tolerance; partially\n    reproduced when 0.0125 <= p < 0.05 or the test holds with a mean out of tolerance.\n- id: figs6l-telc-increase-at-close-distances\n  statement: >-\n    The TeLC increase in firing of activated, distance-tuned units is distance dependent, largest\n    at 7 mm (4.74 sp/s) and significant only at 7 and 9 mm, whereas untuned units show a roughly\n    uniform increase of about 2 sp/s, significant at every distance.\n  source: Results, Inhibition contributes to the PrV map code, paragraph 5; Figure S6L; Table S5\n  quote: >-\n    This enhancement was distance dependent, with the largest increase at the closest wall\n    distance ( Supplemental Figure S6L , bottom; Table S5 ). Thus, SpVi inhibition appears to be\n    strongest at close distances for distance-tuned units\n  statistics:\n  - about: tuned units, 7 mm\n    test: two-tailed Wilcoxon rank-sum test\n    p: 3.13e-6\n    corrected: Bonferroni over nine distances (alpha 0.00556)\n    ci:\n      level: 0.95\n      low: 2.09\n      high: 7.45\n      unit: sp/s\n    n: 472 wild-type and 252 SpVi-TeLC units\n  - about: tuned units, 9 mm\n    test: two-tailed Wilcoxon rank-sum test\n    p: 1.74e-3\n    corrected: Bonferroni over nine distances (alpha 0.00556)\n    ci:\n      level: 0.95\n      low: -0.04\n      high: 5.02\n      unit: sp/s\n  - about: untuned units, 7 mm\n    test: two-tailed Wilcoxon rank-sum test\n    p: 4.38e-4\n    corrected: Bonferroni over nine distances (alpha 0.00556)\n    ci:\n      level: 0.95\n      low: 0.95\n      high: 3.85\n      unit: sp/s\n    n: 550 wild-type and 294 SpVi-TeLC units\n  depends_on:\n  - fig5d-telc-preferred-closer\n  expected:\n  - quantity: TeLC minus wild-type mean rate at 7 mm, tuned units\n    value: 4.74\n    tolerance: 2.68\n    unit: sp/s\n  - quantity: TeLC minus wild-type mean rate at 9 mm, tuned units\n    value: 2.53\n    tolerance: 2.57\n    unit: sp/s\n  - quantity: TeLC minus wild-type mean rate at 23 mm, tuned units\n    value: -0.16\n    tolerance: 1.03\n    unit: sp/s\n  - quantity: TeLC minus wild-type mean rate at 7 mm, untuned units\n    value: 2.38\n    tolerance: 1.47\n    unit: sp/s\n  criterion: >-\n    Per distance, per-unit mean wall rate; TeLC minus wild-type difference of means with a\n    bootstrap 95% CI, and a two-tailed Wilcoxon rank-sum test at the Bonferroni level 0.00556\n    (Table S5; Figure S6L legend). Tolerances are the larger half of each Table S5 CI around its\n    mean. Populations as Table S5 (tuned 472 and 252; untuned 550 and 294). Reproduced when, for\n    tuned units, the largest difference is at 7 mm, the tests are significant at 7 and 9 mm and at\n    no distance from 11 to 23 mm, and, for untuned units, every distance is significant, with the\n    four values within tolerance; partially reproduced when the tuned-unit difference is largest\n    at 7 mm and significant there but the pattern elsewhere differs.\n- id: fig6-model-telc-loses-map\n  statement: >-\n    A feedforward model in which PrV neurons sum sparse sigmoidal TG excitation and SpVi-relayed\n    inhibition yields both proximity-like and map-like tuning across 1,225 model neurons; halving\n    long-range inhibition loses map units and expands proximity units.\n  source: Results, Inhibition contributes to the PrV map code, paragraphs 6-7; Figure 6C-F\n  quote: >-\n    When long-range inhibitory input to each PrV neuron was reduced by 50% to simulate\n    TeLC-mediated silencing of SpVi inhibition, the model showed a loss of map units and a\n    corresponding expansion of proximity units ( Figure 6D – F , right)\n  data: elsewhere\n  where: github.com/wanglab-neuro/2026_Xiao-Severson_Peri-head-distance at commit b1a9f3c (PrV_simulation); Zenodo doi:10.5281/zenodo.20330279\n  expected:\n  - quantity: model neurons\n    value: 1225\n    tolerance: 0\n  - quantity: distance-tuned model neurons, control\n    value: 590\n    tolerance: 59\n  - quantity: distance-tuned model neurons, 50% inhibition\n    value: 636\n    tolerance: 63.6\n  criterion: >-\n    A simulation, not a test on recorded data. Run PrV_simulation/simulate_prv.py at the commit\n    with its defaults (M1 = 20, seed 42, p_untuned 0.4, long_inh_gain 10, local_inh_gain 1.7),\n    without and with --telc (telc_inh_scale 0.5); classification as in the Methods (untuned when\n    max - min < 0.1 over nine bins, suppressed when max below zero, proximity when the peak is at\n    bin 0, map when it is later). Reproduced when the map share of distance-tuned model neurons\n    falls and the proximity share rises with --telc, and the two tuned counts are within\n    tolerance. The Methods' equations and the code's defaults are both recorded; where they\n    differ (the code adds local excitation and inhibition terms the Methods do not write), the\n    code is run, as only it gives the figure's numbers.\n- id: fig6ghi-tuning-shape-telc\n  statement: >-\n    Compared with wild type, activated, distance-tuned units in SpVi-TeLC mice show little change\n    in tuning width, a modest increase in tuning amplitude and a pronounced shift of monotonicity\n    toward proximity-like (near-preferring) tuning, a pattern the model with reduced inhibition\n    reproduces.\n  source: Results, Inhibition contributes to the PrV map code, paragraph 7; Figure 6G-I\n  quote: >-\n    This simulated manipulation also recapitulated the experimental population-level changes in\n    tuning curve shape ( Figure 6G – I ; see STAR Methods ): tuning width changed relatively\n    little, tuning amplitude showed a modest rightward shift, and monotonicity exhibited a\n    pronounced leftward shift toward more proximity-like responses\n  depends_on:\n  - fig5d-telc-preferred-closer\n  criterion: >-\n    Experimental part, on 472 wild-type and 252 SpVi-TeLC activated, distance-tuned units\n    (Methods, Distance Tuning Curve Shape; Fig6GHI_left_TC_shape_analysis.m). Width is the full\n    width at half maximum above the 4.5-s baseline, in mm, by linear interpolation, truncated at\n    the sampled edges, undefined units dropped; amplitude is peak minus baseline in sp/s;\n    monotonicity is (far-edge minus near-edge response) / peak after subtracting the curve's\n    minimum. The paper reports no test. Readings for \"shift\": (a) difference of medians; (b)\n    difference of means. Reproduced when, under both readings, TeLC monotonicity is lower than\n    wild type and TeLC amplitude is higher, and the width shift, expressed as a fraction of the\n    pooled interquartile range, is smaller than the monotonicity shift so expressed. The model\n    part (Fig6GHI_right_model_TC_shape_analysis.m, simulation outputs) is reported, not judged.\n"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  python tools/claims_check.py claims/001687/10.1016-j.neuron.2026.05.027.yaml paper/10.1016-j.neuron.2026.05.027.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  python - <<'EOF'
p='claims/001687/10.1016-j.neuron.2026.05.027.yaml'
s=open(p).read()
a=s.index("  statistics:\n  - about: map population, full array")
b=s.index("  depends_on:\n  - fig4c-map-units-after-cut")
s=s[:a]+s[b:]
open(p,'w').write(s)
EOF
python tools/claims_check.py claims/001687/10.1016-j.neuron.2026.05.027.yaml paper/10.1016-j.neuron.2026.05.027.txt; grep -n -i "rather\|—" claims/001687/*.yaml; python -c "
import yaml;d=yaml.safe_load(open('claims/001687/10.1016-j.neuron.2026.05.027.yaml'));c=d['claims']
print(len(c), sum('quote' in x for x in c), sum('statistics' in x for x in c), sum('criterion' in x for x in c), sum('expected' in x for x in c))"
```

Result: not kept, because it reads the paper's text.

**Agent**

Checker passes. A last scan for ": " inside plain scalars:

**Agent calls Bash**

```bash
cd  grep -n -E "^\s*-?\s*[a-z_]+: [^>\"].*: " claims/001687/*.yaml; awk '/: >-$/{blk=1;next} /^ *-? *[a-z_]+:/{blk=0} !blk && /^    [^ -].*: /' claims/001687/*.yaml | head; git status --short
```

```
difference: 1.66 × 10 −5 mm −1 ) changes, with no significant differences from the
    test: two-tailed paired t-test across mice
    p: 0.03
    corrected: Bonferroni, alpha 0.017
    n: 4 mice
    test: two-tailed paired t-test across mice
    p: 0.04
    corrected: Bonferroni, alpha 0.017
    n: 4 mice
    test: two-tailed paired t-test across mice
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
[... 2 more lines not kept]
```

**Agent**

I wrote the claims file at `claims/001687/10.1016-j.neuron.2026.05.027.yaml`. The quote checker passes: 41 claims, 41 quotes, 39 statistical values found, 0 problems. Nothing is committed.

**Text read.** The accepted author manuscript from PubMed Central (NIHMS2191201 / PMC13336321), fetched 2026-10-20. It has the main text, the STAR Methods, the legends of Figures 1–6, and the supplement PDF, which holds the legends of Figures S1–S6 and Tables S2–S5. I did not read the version of record or open any figure.

**Code read.** github.com/wanglab-neuro/2026_Xiao-Severson_Peri-head-distance at commit b1a9f3c (Zenodo doi:10.5281/zenodo.20330279). I read the MATLAB scripts behind Figures 2–6 and S1, the NWB helper scripts and the circuit model. The helpers show the deposited NWB files are meant to carry the paper's own unit labels (wall_responsive, wall_tuned, tuning_type and so on). I did not read the spike-sorting submodule.

**Claims.** All 41 have quotes; 19 carry statistics, 33 have expected values and 41 have criteria.
- They cover the awake vs anesthetized whisker video (S1), the tungsten recordings (S2) and the silicon-probe unit counts and categories (Fig 2F).
- Firing-rate comparisons (S4A–C), preferred distances, the half-split stability check, unit depth and the three time windows each have a claim.
- Population decoding has claims for overall accuracy, per-distance accuracy, error, the single-neuron decoders and the SVM check (Figure 3, S5, Tables S2–S4).
- Whisker cutting has seven claims: baseline, wall firing, per-unit changes, map and proximity units after the cut, decoding, and the unit total.
- Also covered: the GtACR opto experiment, the TeLC claims (kinematics, unit yield, preferred-distance shift, category shares, firing rates, Table S5) and the circuit model.
- The model claim is marked `data: elsewhere` and is run from the repository. Seven claims of absence are each judged on the paper's own test.

**Details left open, with the readings named:**
- **Responsiveness correction.** The Methods print only "p < 0.05"; the code applies BH-FDR across distances. I followed the code and named uncorrected as the variant.
- **Decoding cross-validation.** 10-fold in the Methods (main reading) against 15 splits in the code (variant). The code also z-scores the features, which the Methods don't mention; I followed the code.
- **Decoding window.** The text says "sustained period" while the Methods, code and Table S2 use 3–11 s. Readings: 3–11 s and 4.5–9.5 s.
- **S4B baseline.** Readings: the baseline of the passes at the same distance, or over all passes. The paper's 6.36 sp/s differs from the 5.46 sp/s it gives for the all-pass baseline.
- **Wall firing in whisker cutting.** Median over distances (code) or mean over passes (Methods).
- **Per-unit cutting tests.** Three corrections appear: uncorrected (Results), BH-FDR (Methods and code), Bonferroni (Methods and code). Two pass sets in the code.
- **After cutting.** Whether "remained tuned" requires activation; how a gain change is measured.
- **Tungsten categories.** The silicon-probe rule, or preferred distance alone.
- **Opto bootstrap.** The CI level and what is resampled.
- **TeLC "untuned".** The 177-unit untuned group of Figure S4, or Table S5's 550 and 294.
- **Z-test denominator.** Wall-responsive units or all units.
- **Fig 5D population.** Activated and tuned, or activated only (the code's mask).
- **Temporal windows.** Whether responsiveness is re-tested in each window.
- **Descriptive claims.** Where the paper reports no test (bending, stability, depth, tuning shape), the criteria use pairs of summaries, such as median and mean, and require both to agree.
- **Model.** The code is run, since it adds local terms the Methods' equations don't write.

**Inconsistencies in the paper,** recorded in the file:
- 472 + 213 − 29 = 656 tuned units implies 184 suppressed-only and 112 untuned, but Figure 2F gives 119 and 177.
- The Figure 4B legend gives ± 2.986 where the text gives ± 1.338.
- The Figure S6J legend prints p = 3.98×10⁻³ where the text prints 3.98×10⁻⁵.
- The Methods call the ± on firing-rate comparisons a bootstrap CI, while the legends call it SEM.
- Figure 3C plots SEM while Tables S2–S3 give 95% CI.
- In the code as read, the combined map + proximity decoder group does not use the 36 + 82 subsample. The claims follow the Methods.

**Missing.** Table S1 (mouse sex, age and figure assignments) and Table S6 (test statistics, degrees of freedom and p-values for all analyses) are named but not in the supplement file. No claim needed them, since every number used is in the text, the legends or Tables S2–S5, so I went ahead. The cost is that the opening comment cannot give subject sex and age, and no degrees of freedom are recorded.

## End of run

36 turns, 9 minutes, result: success.
