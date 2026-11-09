# 001603 · claims · run 39603818050

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cat docs/protocol.md; ls claims/001603 claims/001453 paper/
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -n '/^## Reader/,/^## Author/p' docs/protocol.md
```

```
## Reader

### 1. Get the paper

The workflow puts the paper's full text, and its PDF where there is one, under
`paper/`: the main text, the Methods, and the supplement. Read the text; open
the PDF only to read a figure or a table the text garbles. If the full text is
not there, or lacks the Methods or a supplement the results rest on, stop:
write no claims, and end with a report that names what is missing, so that it
can be supplied. Never write claims from the abstract. Do not copy figures.
Do not look at the dataset's data: its title and description on the archive
are enough to know which paper and which experiments it is meant to hold.

### 2. Read the paper's code

Read the code the paper links to before writing criteria. Say what it holds,
and record the repository and commit read. Where the Methods leave a choice
open and the code settles it, follow the code and say so. Where they disagree,
follow the Methods for the main result and name the code's choice as a
variant. When more sources disagree (the Methods, the analysis code, the
[... 116 more lines not kept]
```

**Agent calls Bash**

```bash
cat claims/001453/*.yaml | head -250; wc -l claims/001453/*.yaml; ls docs tools
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
[... 261 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 250,321p claims/001453/*.yaml; wc -c paper/10.1038-s41593-025-02111-0.txt; head -30 paper/10.1038-s41593-025-02111-0.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
f=claims/001453/*.yaml; sed -n 300,321p $f | cut -c1-300; echo ----; head -c 3000 paper/10.1038-s41593-025-02111-0.txt; echo; wc -c paper/10.1038-s41593-025-02111-0.txt
```

Result: not kept, because it reads the paper's text.

**Agent**

I've read the protocol and the example file. The paper text is the NIH author manuscript (PMC12912721) with one supplement PDF. Next I'll read it in full.

**Agent calls Bash**

```bash
cd paper; wc -l 10.1038-s41593-025-02111-0.txt; awk '{print NR": "length($0)}' 10.1038-s41593-025-02111-0.txt | sort -t: -k2 -n -r | head
```

```
1076 10.1038-s41593-025-02111-0.txt
7: 108197
137: 272
109: 253
89: 252
79: 236
19: 224
41: 219
33: 210
145: 210
21: 199
```

**Agent calls Bash**

```bash
cd  sed -n 7p paper/10.1038-s41593-025-02111-0.txt | fold -s -w 200 > $TMPDIR/main.txt; wc -l $TMPDIR/main.txt; echo $TMPDIR
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/main.txt"
}
```

```
1	pmc Nat Neurosci Nat Neurosci 319 nihpa 9809671 Nature neuroscience 1097-6256 1546-1726 pmc-is-collection-domain yes pmc-collection-title NIHPA Author Manuscripts PMC12912721 PMC12912721.1 12912721 
2	12912721 NIHMS2139360 41286447 10.1038/s41593-025-02111-0 NIHMS2139360 NIHPA2139360 1 Article Preconfigured neuronal firing sequences in human brain organoids van der Molen Tjitse 1 2 3 4 Spaeth Alex 
3	2 5 Chini Mattia 6 Hernandez Sebastian 2 5 Kaurala Gregory A. 1 2 Schweiger Hunter E. 2 7 Duncan Cole 1 2 McKenna Sawyer 1 Geng Jinghui 2 5 Lim Max 3 4 Bartram Julian 8 Gänswein Tobias 8 Dendukuri 
4	Aditya 9 Zhang Zongren 10 Gonzalez-Ferrer Jesus 1 2 Bhaskaran-Nair Kiran 11 Morson Aidan L. 12 Harder Cole R.K. 7 Petzold Linda R. 9 Alam El Din Dowlette-Mary 13 Laird Jason 13 Schenke Maren 13 
5	Smirnova Lena 13 Colquitt Bradley M. 2 7 14 Mostajo-Radji Mohammed A. 2 Hansma Paul K. 3 10 Teodorescu Mircea 2 5 Hierlemann Andreas 8 Hengen Keith B. 11 Hanganu-Opatz Ileana L. 6 Kosik Kenneth S. 3 
6	4 Sharf Tal 1 2 14 * 1 Department of Biomolecular Engineering, University of California Santa Cruz, Santa Cruz, CA 95064, USA 2 UC Santa Cruz Genomics Institute, University of California Santa Cruz, 
7	Santa Cruz, CA 95060, USA 3 Neuroscience Research Institute, University of California Santa Barbara, Santa Barbara, CA 93106, USA. 4 Department of Molecular, Cellular and Developmental Biology, 
8	University of California Santa Barbara, Santa Barbara, CA 93106, USA 5 Department of Electrical and Computer Engineering, University of California Santa Cruz, Santa Cruz, CA 95064, USA 6 Institute of 
9	Developmental Neuroscience, Center for Molecular Neurobiology, Hamburg Center of Neuroscience, University Medical Center Hamburg-Eppendorf, 20251 Hamburg, Germany 7 Department of Molecular, Cell and 
10	Developmental Biology, University of California, Santa Cruz, CA 95064, USA 8 Department of Biosystems Science and Engineering, ETH Zürich, Klingelbergstrasse 48, 4056 Basel, Switzerland 9 De
[... 283 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/main.txt",
 "offset": 294
}
```

```
294	dimensionality reduction step, the firing rate data was normalized for each unit individually using the z -score method, which centers the data around zero mean and unit standard deviation. The 
295	dimensionality reduction was performed on three separate selections of units: all units, backbone units only and non-rigid units only. The cumulative sum of the variance explained per PC was computed 
296	for the PCs ordered from high variance to low. For each recording, the results for all units were subtracted from the results for backbone units only and non-rigid units only. Negative values mean 
297	that the cumulative sum of the variance explained by all units is larger than for the subset of units and positive values mean that the cumulative sum of the variance explained by all units is 
298	smaller. Furthermore, the sum of the variance explained by the first three PCs was computed and divided by the summed explained variance of the first X principal components, where X is the lowest 
299	number of total PCs from the three selections, all units, backbone and non-rigid. This was done to account for differences in the total number of PCs per selection. This value was computed for the 
300	original data and for 100 different shuffled spike matrices and the results from the original spike matrices were normalized using the (A−B)/(A+B) strategy, where A is the measured value and B is the 
301	averaged value computed over the 100 shuffled datasets. These scores were compared between the three selections and between the different model types as described in Methods : statistical analyses 
302	for model comparisons . Randomized recording Randomization of single-unit spike times were performed based on the methods of Okun et al . 38 , 68 to preserve each neuron’s mean firing rate as well as 
303	the population averaged firing rate distribution. This is necessary to avoid trivial differences that would arise simply by changes in the mean firing rate of a neuron. Briefly,
[... 249 more lines not kept]
```

**Agent**

Main text and Methods read. The Methods here have no HMM or criticality section, so I'll check whether the supplement covers them.

**Agent calls Bash**

```bash
cd  sed -n '8,$p' paper/10.1038-s41593-025-02111-0.txt > $TMPDIR/supp.txt; wc -l -c $TMPDIR/supp.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/supp.txt"
}
```

```
1	
2	Preconfigured neuronal firing sequences in human brain organoids
3	
4	[1] Llinás, R. R. & Paré, D. Of dreaming and wakefulness. Neuroscience 44, 521–535 (1991). 10.1016/0306-4522(91)90075-Y
5	
6	[2] Song, S., Sjöström, P. J., Reigl, M., Nelson, S. & Chklovskii, D. B. Highly nonrandom features of synaptic connectivity in local cortical circuits. PLoS Biol. 3, e68 (2005).
7	
8	[3] Buzsáki, G. & Mizuseki, K. The log-dynamic brain: how skewed distributions affect network operations. Nat. Rev. Neurosci. 15, 264–278 (2014). 10.1038/nrn3687
9	
10	[4] Luczak, A., Barthó, P. & Harris, K. D. Spontaneous events outline the realm of possible sensory responses in neocortical populations. Neuron 62, 413–425 (2009). 10.1016/j.neuron.2009.03.014
11	
12	[5] Hemberger, M., Shein-Idelson, M., Pammer, L. & Laurent, G. Reliable sequential activation of neural assemblies by single pyramidal cells in a three-layered cortex. Neuron 104, 353–369 (2019). 10.1016/j.neuron.2019.07.017
13	
14	[6] Riquelme, J. L., Hemberger, M., Laurent, G. & Gjorgjieva, J. Single spikes drive sequential propagation and routing of activity in a cortical network. eLife 12, e79928 (2023). 10.7554/eLife.79928
15	
16	[7] Luczak, A., McNaughton, B. L. & Harris, K. D. Packet-based communication in the cortex. Nat. Rev. Neurosci. 16, 745–755 (2015). 10.1038/nrn4026
17	
18	[8] Pastalkova, E., Itskov, V., Amarasingham, A. & Buzsáki, G. Internally generated cell assembly sequences in the rat hippocampus. Science 321, 1322–1327 (2008). 10.1126/science.1159775
19	
20	[9] Dragoi, G. & Tonegawa, S. Preplay of future place cell sequences by hippocampal cellular assemblies. Nature 469, 397–401 (2011). 10.1038/nature09633
[... 737 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/supp.txt",
 "offset": 758
}
```

```
758	PIPseq data analysis 
759	Samples were pooled and sequenced on the AVITI PE75 Flowcell ~900M reads at the UCDavis 
760	Technologies Core. The sequencing data was then processed using the PIPseeker pipeline 
761	(PIPseeker v3.3, Fluent BioSciences), using the mouse genome GRCm39 (GENCODE vM29 
762	2022.04, Ensembl 106)16. We used the default parameters to process the FASTQ files, perform 
763	mapping, transcript counting and cell calling.  
764	Sensitivity 5 matrices were used for downstream analysis using R package Seurat (version 
765	5.1.0)17. Souporcell was used for genotype demultiplexing and doublet identification18. Doublets 
766	were also identified using the R package DoubletFinder v2.0.419. 
767	Cells were filtered based on doublet identification, with greater than 20% mitochondrial genes, 
768	less than the 5th percentile unique genes detected, and greater than 50,000 total RNA counts. The 
769	
770	=== page 34 ===
771	raw gene count matrices were normalized with SCTransform function while regressing out 
772	mitochondrial genes identified the top 3,000 highly variable genes. Principal component analysis 
773	was performed and clusters were identified by the FindNeighbors function using 40 principal 
774	components (chosen based on visual inspection of the elbow plot). The function FindClusters 
775	was run with resolutions of 2, 1, and 0.5 with leiden clustering. The clusters were then embedded 
776	and visualized with Uniform Manifold Approximation and Projection (UMAP)20 and the 
777	resolution of 0.5 was chosen based on visual inspection of marker genes to represent the best 
[... 293 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && git clone -q https://github.com/braingeneers/Protosequences && cd Protosequences && git log -1 --format='%H %ci' && find . -type f -not -path './.git/*' | head -100 && find . -type f -not -path './.git/*' | wc -l
```

```
e9a79c459361e7d0eca280d11f592b1f4262f6ee 2025-05-19 08:31:56 +0200
./burst_clustering_analysis_python/PR_LabeledBursts.py
./burst_clustering_analysis_python/Main.py
./burst_clustering_analysis_python/Group_AvgStdColumn_BoxSaved.py
./burst_clustering_analysis_python/ExtractBurst_ElbowSeeds.py
./burst_clustering_analysis_python/Column_Heatmap.py
./burst_clustering_analysis_python/CV_Score_csv.py
./burst_clustering_analysis_python/Boxplot.py
./README.md
./Processed_data/Figure7/unit_pair_avg.xlsx
./Processed_data/Figure7/single_unit.xlsx
./Processed_data/Figure7/pca.xlsx
./Processed_data/Figure7/lag_data.xlsx
./Processed_data/Figure7/dimensions.xlsx
./Processed_data/Figure6/corr_pairs.xlsx
./Processed_data/Figure6/b2bcorr.xlsx
./Processed_data/Figure3/corr_pairs.xlsx
./Processed_data/Figure2/peak_times.xlsx
./Processed_data/Figure2/b2bcorr.xlsx
./Processed_data/Figure1/peak_times.xlsx
[... 38 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/Protosequences && cat README.md && wc -l Main_analyses_matlab/* HMM_analysis_python/* Criticality_analysis/* burst_clustering_analysis_python/*
```

```
# Protosequences
Analysis code for the paper "Protosequences in brain organoids model intrinsic brain states"

Use Main_analyses_matlab/preprocess_ks.m to inspect and preprocess the kilosort2 spike times into spike matrices. These spike matrices are subsequently used in Main_analyses_matlab/process_data_backbone.m and HMM_analysis_python for further processing the data. The remainder of the scripts plot the processed results.

For questions about the scripts and data, reach out to [removed: an e-mail address]
   215 Main_analyses_matlab/plot_develomental_analysis.m
  1215 Main_analyses_matlab/plot_multi_rec_figs_backbone.m
  1034 Main_analyses_matlab/plot_multi_rec_rand_figs_backbone.m
  1071 Main_analyses_matlab/plot_single_rec_figs_backbone.m
   329 Main_analyses_matlab/plot_time_diff_analysis.m
   147 Main_analyses_matlab/preprocess_ks.m
   812 Main_analyses_matlab/process_data_backbone.m
    83 Main_analyses_matlab/shuffle_spike_mats.py
    10 HMM_analysis_python/Dockerfile
   476 HMM_analysis_python/Fig5.py
   456 HMM_analysis_python/Supplements.py
    14 HMM_analysis_python/cv_worker.py
   138 HMM_analysis_python/do_cv.py
   147 HMM_analysis_python/fit_hmms.py
[... 18 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/Protosequences/Main_analyses_matlab/process_data_backbone.m"
}
```

```
1	%% load data
2	
3	% load data
4	load('t_spk_mat_sorted.mat')
5	
6	% make empty result array for shuffled datasets
7	t_spk_mat_all_shuf = [];
8	
9	% get list of all files in the directory
10	all_files = dir;
11	
12	% for each file
13	for file = 1:length(all_files)
14	    
15	    % if the file contains the right substring
16	    if contains(all_files(file).name, 't_spk_mat_sorted_shuff')
17	        
18	        % load data
19	        shuf_cont = load(all_files(file).name);
20	        
[... 793 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/Protosequences && cat Main_analyses_matlab/preprocess_ks.m Main_analyses_matlab/shuffle_spike_mats.py
```

```
%% load spike data and burst edges

% set paths to all the recordings you want to process
rec_paths = [""]; % add path to where kilosort outputs are saved

% for each recording
for rec = rec_paths  
    
    % load sorted spike data
    ks_spk_data_ont = load(strcat(rec, 't_spk_mat_ks.mat')); % change to appropriate file name
    units = ks_spk_data_ont.units;
    fs = double(ks_spk_data_ont.fs);
    locations = ks_spk_data_ont.locations;
    
    % make empty result arrays
    t_spk_mat = zeros(180000, length(units));
    spike_times = cell(length(units),1);
    xy_raw = zeros(length(units), 2);
    chan_num_sorted = zeros(length(units), 1);
    
[... 211 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/Protosequences/Main_analyses_matlab && grep -n "^%%\|THRESH\|FRAC\|= [0-9]" plot_multi_rec_figs_backbone.m | head -120
```

```
1:%% load data
27:for array = 1:length(rec_paths)
58:%% set recording names
71:%% Show Log-Normal fit to firing rate distribution
76:ARRAY_OI = 1; % which array to use for panel A
95:for array = 1:length(spk_count)
115:for array = 1:size(av_rate, 2)
193:ax.FontSize = 14;
232:ax.FontSize = 14;
252:ax.FontSize = 14;
268:ax.FontSize = 14;
273:%% compare average firing rate
279:MIN_SPIKES = 30;
292:for array = 1:length(spk_count)
309:    tick_locs(array) = 1.5+(array-1)*2;        
346:%% Show Log-Normal fit to firing rate distribution
359:for array = 1:length(spk_count)
388:for array = 1:size(plot_metric, 2)
429:ax.FontSize = 14;
452:ax.FontSize = 14;
[... 44 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/Protosequences/Main_analyses_matlab && sed -n 273,300p plot_multi_rec_figs_backbone.m; sed -n 726,760p plot_multi_rec_figs_backbone.m; sed -n 802,850p plot_multi_rec_figs_backbone.m
```

```
%% compare average firing rate
% (Fig S1D, S30A)
% S1D = Load organoid recordings only
% S30A = Load all recordings

% only plot results for units with at least MIN_SPIKES in recording
MIN_SPIKES = 30;

% specify plot colors
box_colors = repmat(["r", "b"], 1,length(spk_count));

% make empty result arrays
vectorized_data = [];
unit_type_group = [];
org_type_group = [];
boxplot_group = [];
tick_locs = zeros(1,length(spk_count));

% for each array
for array = 1:length(spk_count)
[... 93 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/Protosequences && for f in Plotting_notebooks_python/Fig*.ipynb; do echo "== $f"; python3 -c "
import json,sys
nb=json.load(open('$f'))
for c in nb['cells']:
    if c['cell_type']=='code':
        s=''.join(c['source'])
        print('---');print(s[:1500])
" | head -80; done 2>&1 | head -300
```

```
== Plotting_notebooks_python/Fig1.ipynb
---
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# load data
width = pd.read_excel('load burst_width.xlsx here')
peaks = pd.read_excel('load peak_times.xlsx here')
---
# plot the burst width across organoids
plt.figure()
sns.violinplot(x='organoid', y='width', cut=0,
               density_norm='width', data=width)
plt.ylabel('Burst width (ms)')
plt.xlabel('Individual organoid')
---
# plot the peak time of individual units
plt.figure()
sns.violinplot(x='organoid', y='peak_times', cut=0,
[... 183 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/Protosequences/Processed_data && python3 -c "
import pandas as pd,glob
for f in sorted(glob.glob('*/*.xlsx')):
    d=pd.read_excel(f)
    print('==',f,d.shape); print(d.head(3).to_string())
    for c in d.columns:
        if d[c].dtype==object and d[c].nunique()<12: print(c, d[c].value_counts().to_dict())
" 2>&1 | head -150
```

```
Traceback (most recent call last):
  File "<string>", line 2, in <module>
    import pandas as pd,glob
ModuleNotFoundError: No module named 'pandas'
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/Protosequences/Processed_data && python3 -c "import openpyxl" 2>&1; for f in */*.xlsx; do echo "== $f"; unzip -p "$f" xl/sharedStrings.xml 2>/dev/null | head -c 600; echo; unzip -p "$f" xl/worksheets/sheet1.xml | grep -o '<dimension ref="[^"]*"'; done
```

```
Traceback (most recent call last):
  File "<string>", line 1, in <module>
    import openpyxl
ModuleNotFoundError: No module named 'openpyxl'
== Figure1/burst_width.xlsx
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<sst xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main" count="2" uniqueCount="2"><si><t>organoid</t></si><si><t>width</t></si></sst>
<dimension ref="A1:B148"
== Figure1/peak_times.xlsx
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<sst xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main" count="2" uniqueCount="2"><si><t>organoid</t></si><si><t>peak_times</t></si></sst>
<dimension ref="A1:B7207"
== Figure2/b2bcorr.xlsx
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<sst xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main" count="749" uniqueCount="7"><si><t>NaN</t></si><si><t>b2bcorr</t></si><si><t>group</t></si><si><t>organoid</t></si><si><t>label</t></si><si><t>b</t></si><si><t>nr</t></si></sst>
<dimension ref="A1:D508"
== Figure2/peak_times.xlsx
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<sst xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main" count="684" uniqueCount="3"><si><t>NaN</t></si><si><t>unit</t></si><si><t>peak_time</t></si></sst>
<dimension ref="A1:B1243"
[... 33 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/Protosequences && cat HMM_analysis_python/lmem.R Criticality_analysis/plot_results_boxplot.py Criticality_analysis/r_download.sh; head -50 Criticality_analysis/d2_nocriter.csv; cat HMM_analysis_python/justfile
```

```
library('dplyr')
library('lme4')
library('lmerTest')
library('emmeans')

dimensions <- read.csv("dimensions.csv")
dsub = dimensions[dimensions$theta == 0.75, ]
# Make a LMEM of this current subset of the data.
sample_type <- factor(dsub$sample_type)
sample_id <- factor(dsub$sample_id)
model <- glmer(dsub$dims ~ sample_type + (1 | sample_id), family=poisson(link="log"))
emmeans(model, pairwise ~ sample_type)

df <- do.call(rbind, lapply(split(dimensions, dimensions$theta), function(dsub) {
		# Make a LMEM of this current subset of the data.
		sample_type <- factor(dsub$sample_type)
		sample_id <- factor(dsub$sample_id)
		model <- glmer(dsub$dims ~ sample_type + (1 | sample_id), family=poisson(link="log"))
		# Calculate the significance scores and add the theta column.
		ret <- summary(emmeans(model, pairwise ~ sample_type)$contrasts)
[... 168 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/Protosequences/HMM_analysis_python && grep -n "svm\|SVC\|ttest\|LeaveOneOut\|n_states\|bin_size\|surr\|experiments\|source\|def \|backbone\|rsm\|K =" Fig5.py | head -80
```

```
12:from sklearn.model_selection import LeaveOneOut, cross_validate
28:bin_size_ms = 30
29:n_stateses = np.arange(10, 31)
34:with tqdm(total=2 * len(ORGANOIDS) * (1 + len(n_stateses))) as pbar:
35:    rasters_real, rasters_rsm = {}, {}
36:    rasterses = dict(real=rasters_real, rsm=rasters_rsm)
39:        for surr, rs in rasterses.items():
40:            r, ms = rs[exp] = get_raster(DATA_SOURCE, exp, bin_size_ms, surr), []
46:            for n in n_stateses:
47:                m = Model(DATA_SOURCE, exp, bin_size_ms, n)
54:    meanfr = r._raster.mean() / r.bin_size_ms * 1000
59:consistency_real, consistency_rsm = [
65:def separability(X, n_nonrigid):
68:    nonrigid units first, followed by the backbone, and return its accuracy according to
71:    cv = LeaveOneOut()
79:    sep_on_states = {
92:    states_fr = stats.ttest_1samp(sep_on_states[e], sep_on_fr[e])
95:reals = np.hstack(list(sep_on_states.values()))
108:n_states = 20
110:model = models[np.nonzero(n_stateses == n_states)[0][0]]
[... 23 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/Protosequences/HMM_analysis_python && grep -n "svm\|SVC\|ttest\|LeaveOneOut\|Poisson\|chi2\|dimensionality\|explained\|theta\|traversal\|rsm\|randomize\|def " Supplements.py hmmsupport.py fit_hmms.py | head -100
```

```
Supplements.py:26:    state_traversal_df,
Supplements.py:53:    _rs: dict[str, dict[str, tuple[Raster, list[Model]]]] = dict(real={}, rsm={})
Supplements.py:54:    rasters_real, rasters_rsm = _rs["real"], _rs["rsm"]
Supplements.py:56:        for surr in ["real", "rsm"]:
Supplements.py:79:# Vectors of the first ten explained variance ratios for all of the experiments.
Supplements.py:80:pve_real, pve_rsm = [
Supplements.py:82:        e: np.array([m.pca.explained_variance_ratio_[:10] for m in ms])
Supplements.py:85:    for rs in [rasters_real, rasters_rsm]
Supplements.py:89:def components_required(exp, thresh, rsm=False, which_models=None):
Supplements.py:90:    scores = (pve_rsm if rsm else pve_real)[exp]
Supplements.py:101:def dimensions_required(experiments, xs, rsm=False, which_models=None):
Supplements.py:106:                    components_required(exp, x, rsm=rsm, which_models=which_models)
Supplements.py:115:def poisson_test(data):
Supplements.py:118:    variance than a K-dimensional multivariate Poisson distribution with the same
Supplements.py:128:    # Dividing by the expected variance, which for Poisson is the mean.
Supplements.py:133:    return stats.chi2(dof).cdf(statistic)
Supplements.py:136:def unit_consistency(model, raster):
Supplements.py:162:def mean_consistency(exp):
Supplements.py:165:    models where the unit is too consistent to be Poisson, weighted by how frequently
Supplements.py:167:    trivially Poisson.
[... 69 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/Protosequences/HMM_analysis_python && sed -n 1,110p Fig5.py; sed -n 160,220p hmmsupport.py; sed -n 285,300p hmmsupport.py; sed -n 79,100p Supplements.py
```

```
# Fig5.py
# Generate figure 5 and supplementary figures 25 and 27.
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from joblib import parallel_backend
from matplotlib.ticker import PercentFormatter
from scipy import stats
from sklearn.decomposition import PCA
from sklearn.linear_model import SGDClassifier
from sklearn.model_selection import LeaveOneOut, cross_validate
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from tqdm import tqdm

from hmmsupport import (
    DATA_SOURCE,
    GROUP_EXPERIMENTS,
    Model,
[... 188 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/Protosequences/HMM_analysis_python && grep -n "pca\|PCA\|GROUP_EXPERIMENTS\|DATA_SOURCE =" -A3 hmmsupport.py | head -60; sed -n 60,100p hmmsupport.py; cat fit_hmms.py | sed -n 1,60p
```

```
704:        for model, exps in GROUP_EXPERIMENTS.items()
705-        for exp in exps
706-        for n_states, stats in zip(n_stateses, distinct_states_traversed(exp))
707-    )
--
710:DATA_SOURCE = "org_and_slice"
711-GROUP_NAME = {
712-    "HO": "Human Organoid",
713-    "MO": "Murine Organoid",
--
717:GROUP_EXPERIMENTS = {
718-    "HO": [
719-        "L1_t_spk_mat_sorted",
720-        "L2_7M_t_spk_mat_sorted",
--
761:    for group, exps in GROUP_EXPERIMENTS.items()
762-    for i, exp in enumerate(exps)
763-}
764-
--
[... 108 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/Protosequences/HMM_analysis_python && sed -n 700,773p hmmsupport.py; grep -n "self.pca\|\.pca" hmmsupport.py Supplements.py | head
```

```
)

    return pd.DataFrame(
        dict(sample_type=model, sample_id=exp, K=n_states) | stats
        for model, exps in GROUP_EXPERIMENTS.items()
        for exp in exps
        for n_states, stats in zip(n_stateses, distinct_states_traversed(exp))
    )


DATA_SOURCE = "org_and_slice"
GROUP_NAME = {
    "HO": "Human Organoid",
    "MO": "Murine Organoid",
    "MS": "Murine Acute Slice",
    "Pr": "Murine Primary Culture",
}
GROUP_EXPERIMENTS = {
    "HO": [
        "L1_t_spk_mat_sorted",
[... 58 more lines not kept]
```

**Agent calls Bash**

```bash
curl -s https://api.dandiarchive.org/api/dandisets/001603/ | python3 -c "import json,sys; d=json.load(sys.stdin); print(json.dumps(d,indent=1)[:1500])"; curl -s "https://api.dandiarchive.org/api/dandisets/001603/versions/draft/info/" | python3 -c "import json,sys; d=json.load(sys.stdin); m=d.get('metadata',d); print(m.get('name')); print(m.get('description')); print(m.get('version')); print(json.dumps(m.get('assetsSummary'),indent=0)[:1500])"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
sed -n 1,80p tools/claims_check.py; grep -n "kind\|data\b\|'data'\|\"data\"\|FIELDS\|allowed" tools/claims_check.py tools/entry.py | head -40
```

```
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

import html
import re
import sys
import unicodedata
from pathlib import Path

[... 96 more lines not kept]
```

**Agent calls Bash**

```bash
python3 -c "
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
python3 -c "
import json;s=json.load(open('schemas/claims.schema.json'));print(json.dumps(s['\$defs'],indent=1)[:4000])"
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
cd $TMPDIR/Protosequences/Main_analyses_matlab && sed -n 71,135p plot_multi_rec_figs_backbone.m; sed -n 346,400p plot_multi_rec_figs_backbone.m
```

```
%% Show Log-Normal fit to firing rate distribution
% (Fig S1A-C)
% S1A-C = Load organoid recordings only

% select parameters
ARRAY_OI = 1; % which array to use for panel A
BIN_EDGES = linspace(0,10,21); % binning data for histogram
FIT_LN_RANGE = [-5,2]; % fitting range for ln of rate

% define bin centers
bin_centers = BIN_EDGES(2:end)-0.5*diff(BIN_EDGES);

% define log-normal distribution
log_norm_dist = @(b,x) 1./(x(:,1) .* b(1) .* sqrt(2 .* pi)) .* exp(-1 .* ( ( log(x(:,1)) - b(2) ).^2 / ( 2 .* b(1) ).^2 )) ;
est_initial_log_norm_dist = [1, 0.25];

% define normal distribution
norm_dist = @(b,x) 1/(b(1) * sqrt(2 * pi)) * exp(-0.5 * ( (x(:,1) - b(2) ) ./ b(1) ).^2);
est_initial_norm_dist = [1, 0.25];

[... 102 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/Protosequences/Main_analyses_matlab && sed -n 135,200p plot_multi_rec_figs_backbone.m | grep -v "^\s*$" | head -60; grep -n "r_squared\|histcounts\|fitnlm\|Rsquared" plot_multi_rec_figs_backbone.m
```

```
% obtain r_squared value of fit
    r_squared_vals(array) = mdl.Rsquared.Ordinary;
    % call subplot for fitted models
    subplot(1,3,2)
    hold on
    % make histogram of log(rate) values
    [log_counts, edges] = histcounts(log(av_rate{array}), ceil(length(log(av_rate{array}))^0.4), 'Normalization','probability');
    % compute bin centers for ln data
    bin_centers_ln_plot = edges(2:end)-diff(edges);
    % find maximum index with nonzero values
    max_index = max(find(log_counts > 0));
    % combine x and y values in table
    tbl = table(bin_centers_ln_plot(1:max_index)', log_counts(1:max_index)');
    % fit normal distribution
    mdl = fitnlm(tbl, norm_dist, est_initial_norm_dist);        
    % Extract the coefficient values from the the model object.
    coefficients = mdl.Coefficients{:, 'Estimate'};
    % get x and y values for fitted model
    ln_xFitted = linspace(FIT_LN_RANGE(1), FIT_LN_RANGE(2), 301)';
    ln_yFitted = norm_dist(coefficients,ln_xFitted);
[... 40 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/Protosequences/Main_analyses_matlab && grep -n "anova\|%%\|rec_paths\|age" plot_develomental_analysis.m | head -30; grep -n "%%\|ttest\|WIND\|NORM" plot_single_rec_figs_backbone.m | head -60
```

```
1:%% load data
4:ages = ["6", "7", "8"]; % specify which ages to use
10:scaf_units = cell(length(organoids),length(ages));
11:non_scaf_units = cell(length(organoids),length(ages));
12:frac_per_unit = cell(length(organoids),length(ages));
13:av_rate = cell(length(organoids),length(ages));
14:av_btb_corr_scores = cell(length(organoids),length(ages));
15:all_pw_corr_vals = cell(length(organoids),length(ages));
19:for age = 1:length(ages)
25:        s_rec_met = load(strcat(LOAD_PATH, sprintf("%s_%sM_single_recording_metrics", organoids(array), ages(age))));
28:        scaf_units{array, age} = s_rec_met.scaf_units;
29:        non_scaf_units{array, age} = s_rec_met.non_scaf_units;
30:        frac_per_unit{array, age} = s_rec_met.frac_per_unit;
31:        av_rate{array, age} = s_rec_met.spk_count./(size(s_rec_met.rate_mat,1)/1000);
32:        av_btb_corr_scores{array, age} = s_rec_met.av_btb_corr_scores;
33:        all_pw_corr_vals{array, age} = s_rec_met.all_pw_corr_vals;
39:%% Plot fraction of scaffold units at different ages
43:frac_scaf = zeros(length(organoids), length(ages));
44:leg_lab = strings(1,length(ages));
47:for age = 1:length(ages)
[... 35 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/Protosequences/Main_analyses_matlab && sed -n 690,740p plot_single_rec_figs_backbone.m
```

```
% plot variance of all pairwise cosine similarities
    plot(frame_range, std(all_pairwise), "Color", "r", "LineWidth", 2)
    
    % add axis label
    ylabel("STD burst similarity")

    set(gca,'FontSize',14)
    set(gca,'linewidth',3)
    
    
    % initiate subplot for burst similarity for scaf, non-scaf and rand
    subplot(2,3,5)
    hold on
    
    % plot average cosine similarity
    sc_h = plot(frame_range, mean_cos_sim_scaf, "k", "LineWidth", 2);
    nsc_h = plot(frame_range, mean_cos_sim_non_scaf, "k--", "LineWidth", 2);
    r_h = plot(frame_range, mean_cos_sim_rand, "k:", "LineWidth", 2);
    
    % make empty result array for significance scores
[... 31 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/Protosequences/Processed_data/Figure7 && for f in lag_data single_unit; do echo == $f; unzip -p $f.xlsx xl/sharedStrings.xml | grep -o '<t>[a-z_ -]*</t>' | sort | uniq -c | sort -rn | head -12; done; unzip -p dimensions.xlsx xl/sharedStrings.xml | grep -o '<t>[^<]*</t>' | head -45 | tr '\n' ' '
```

```
== lag_data
      1 <t>unit_pair_numbers</t>
      1 <t>shuff_labels</t>
      1 <t>sample_type</t>
      1 <t>sample_labels</t>
      1 <t>o</t>
      1 <t>mouse_primary</t>
      1 <t>mouse_organoid</t>
      1 <t>mouse slice</t>
      1 <t>lag_vals_log</t>
      1 <t>lag_vals</t>
      1 <t>human_organoid</t>
== single_unit
      1 <t>unit_numbers</t>
      1 <t>shuff_labels</t>
      1 <t>scaf_labels</t>
      1 <t>sample_type</t>
      1 <t>sample_labels</t>
      1 <t>o</t>
      1 <t>non-rigid</t>
[... 7 more lines not kept]
```

**Agent**

Most of the structure is settled. Three details to check before writing: the burst-clustering k selection, the HMM cross-validation split, and the state-traversal measure.

**Agent calls Bash**

```bash
cd $TMPDIR/Protosequences && sed -n 1,139p burst_clustering_analysis_python/ExtractBurst_ElbowSeeds.py | grep -v "^\s*#\|^\s*$" | head -90; sed -n 100,160p HMM_analysis_python/hmmsupport.py; sed -n 653,700p HMM_analysis_python/hmmsupport.py
```

```
import matplotlib.pyplot as plt
import numpy as np
import pickle as pkl
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from scipy.io import loadmat
import mat73
def extract_columns(data, indices):
    extracted_columns = []
    for index_pair in indices:
        start_index, end_index = index_pair
        extracted_columns.append(data[:, int(start_index):int(end_index) + 1])
    return extracted_columns
def kmeans_clustering_elbow(data, k, random_state):
    kmeans = KMeans(n_clusters=k, init="k-means++", random_state=random_state)
    kmeans.fit(data)
    dist = kmeans.inertia_
    return dist
def kmeans_clustering_sil_coef(data, k, random_state):
    kmeans = KMeans(n_clusters=k, init="k-means++", random_state=random_state)
[... 180 more lines not kept]
```

**Agent**

I have what I need: the full text, the supplement, and the code at commit e9a79c4. Now writing the claims file.

**Agent calls Write**

```json
{
 "file_path": "claims/001603/10.1038-s41593-025-02111-0.yaml",
 "content": "# Claims for van der Molen, Spaeth, Chini et al. (2025), \"Preconfigured neuronal firing sequences in\n# human brain organoids\", Nature Neuroscience, doi:10.1038/s41593-025-02111-0, on dandiset 001603.\n# Written by an agent (model \"claude-opus-5-5\", Claude Code in GitHub Actions), 2026-10-21, protocol\n# version pilot-10 as stated in docs/protocol.md.\n#\n# Text read. The NIH author manuscript in PubMed Central (PMC12912721.1, NIHMS2139360), as served by\n# NCBI PMC on 2026-10-20: main text, Methods, figure legends and Extended Data legends (Figs. 1 to 8),\n# with the publisher's Supplementary Information PDF (41593_2025_2111_MOESM1_ESM.pdf; Supplementary\n# Figures 1 to 27 and Supplementary Methods). Not the typeset version of record. Figures were not\n# opened; every number below is from the text.\n#\n# Code read. https://github.com/braingeneers/Protosequences at commit e9a79c4 (2025-05-19), the\n# repository named under Code Availability. It holds MATLAB scripts for the spike matrices, bursts,\n# backbone units, firing rates, burst-to-burst and pairwise correlations, burst similarity and PCA\n# (Main_analyses_matlab, process_data_backbone.m above all), the Python spike shuffling\n# (shuffle_spike_mats.py), the HMM analysis in Python with SSM (HMM_analysis_python, with lmem.R for\n# the HMM statistics), the burst clustering in Python (burst_clustering_analysis_python), the d2\n# results and plotting (Criticality_analysis; the d2 code itself is downloaded from figshare article\n# 25927081, Sooter et al.), plotting notebooks, and processed per-figure tables (Processed_data). The\n# R scripts for the linear mixed-effects models of Figs. 2, 3, 6 and 7 are not in it.\n#\n# Data the paper used (its Methods, legends and code). Spontaneous activity on CMOS high-density\n# microelectrode arrays (MaxWell; 1,020 recording electrodes, 20 kHz), band-passed 300 to 6000 Hz,\n# sorted with Kilosort2 and curated (ISI violation at most 0.3, mean rate at least 0.05 Hz, SNR at\n# least 5). Units are spike-sorted single units; the measured variable is their spike times.\n#   - HO1 to HO4. Human brain organoid slices (500 um) from Sharf et al. 2022, MaxOne; the \"four\n#     organoids\" of Figs. 1D, 1E, 2E, 2G and 3E (code names L1, L2_7M, L3_7M, L5). Also longitudinal\n#     recordings of human organoids at 6, 7 and 8 months (Supplementary Fig. 2; ages from\n#     plot_develomental_analysis.m) and two recordings 4 h apart of HO2 and HO3 (Supplementary Fig. 8).\n#   - HO5 to HO8. Whole human organoids (NIBSC8 iPSC line) from Alam El Din et al. 2025, MaxTwo\n#     6-well arrays (code names well1, well4, well5, well6). HO1 to HO8 are the \"8 organoids\" of\n#     Extended Data Fig. 1, Figs. 4E and 5 and Fig. 7.\n#   - MO1 to MO9. Murine ESC-derived dorsal forebrain organoids (lines C57BL/6, E14TG2a, KH2), plated\n#     whole at about 30 days (Fig. 7, Extended Data Fig. 8). MO10 to MO14. Murine organoids recorded\n#     at baseline, after 10 uM gabazine, then after 10 uM NBQX with 20 uM R-CPP (Extended Data Fig.\n#     4). Longitudinal murine organoid recordings with ages in weeks (Supplementary Fig. 2).\n#   - MS. Six acute coronal slices of somatosensory cortex from P12 to P14 C57BL/6JRj pups, both\n#     sexes, MaxOne (code names M1S1, M1S2, M2S1, M2S2, M3S1, M3S2, so three animals with two slices\n#     each; the Fig. 6 legend says n = 6 mice, the Results n = 6 slices).\n#   - Pr1 to Pr8. Dissociated two-dimensional primary cortical cultures, Pr1 to Pr4 from Yuan et al.\n#     2020 (E18 Wistar rat cortex, 20 days in vitro), Pr5 to Pr8 from Bartram et al. 2024. The paper\n#     calls them murine primary cultures.\n# The dandiset's description says it holds all these (raw and sorted for MO and MS, sorted only for\n# the sourced HO and Pr recordings).\n#\n# Methods common to the claims, from the Methods and process_data_backbone.m unless named otherwise.\n#   - Spike matrix at 1 ms resolution (preprocess_ks.m). Recording length, open. The Methods take\n#     \"the first x minutes\" of each recording so that it holds about 40 bursts; the code keeps 180 s\n#     for HO1 to HO4, MS and Pr and 600 s for HO5 to HO8 and MO (hmmsupport.py KEEP_DURATION; the\n#     shuffles use 180 s). Readings (a) the code's lengths, (b) the shortest initial segment holding 38\n#     to 40 bursts. Both are run where the outcome could depend on it.\n#   - Population rate. Spikes summed over units per 1 ms frame, a 20 ms moving mean, then a Gaussian\n#     window of 100 ms (MATLAB smoothdata 'gaussian' with window 100). Burst peaks with findpeaks at\n#     4 x RMS of that rate, minimum peak distance 700 ms (Methods; up to 2000 ms for long bursts; the\n#     code uses 800 ms, a variant). Burst start and end, the nearest frames where that rate falls\n#     below 10% of the peak. Burst peak time, the maximum between start and end of a finer rate (5 ms\n#     moving mean, 5 ms Gaussian). Bursts within 450 ms of the start or 1000 ms of the end are dropped\n#     (code). For primary cultures, 20 ms moving mean, 50 ms Gaussian, 3 x RMS and a 20% edge.\n#   - Backbone units. Units with at least two spikes between burst start and end in every burst\n#     (human organoids and primary cultures); in at least 80% of bursts for murine organoids. For\n#     slices the Methods and Supplementary Fig. 1 say 90% and the Fig. 6B legend says 70%; both are\n#     readings wherever slices enter. All other units are non-rigid.\n#   - Unit firing rate. The inverse inter-spike interval held between spikes, smoothed with a 50 ms\n#     Gaussian (code compute_rate_isi), for units with at least 30 spikes (Methods; the code applies\n#     the 30-spike rule in the group comparisons). \"Burst-only\" rates use spikes inside burst windows.\n#   - Randomized recordings. The Okun et al. swap, which keeps each unit's spike count and each frame's\n#     population count, with 5 swaps per spike (shuffle_spike_mats.py); 100 shuffled matrices per\n#     recording. The random seed is a standard choice and cannot change an outcome beyond noise.\n#   - Normalization to shuffles, (A - B)/(A + B) with A the measured value and B the mean over the 100\n#     shuffles.\n#   - Statistics. Linear mixed-effects models (lme4 lmer, lmerTest, type III) with \"organoid\" (the\n#     recording) or \"unit ID\" as random effect; right-skewed data log-transformed; post hoc with\n#     emmeans. Where a claim gives no other rule, it is reproduced when the effect has the paper's\n#     direction with p < 0.05 by the paper's test, and the p found is reported beside the paper's.\n#     Where the random-effect structure is not given, the reading is a random intercept per recording;\n#     for slices a random intercept per animal is a second reading.\n#   - Where the readings of a method detail give different outcomes, the claim is\n#     methods_underspecified with every result shown. Where only the meaning of a reported number is\n#     in doubt, the claim holds if it matches under any reading.\nschema_version: 2\ndataset:\n  archive: dandi\n  id: \"001603\"\npaper: doi:10.1038/s41593-025-02111-0\nclaims:\n- id: methods-burst-count\n  statement: The analysed segment of each recording holds about 40 population bursts (38 ± 4,\n    mean ± SE).\n  source: Methods, Comparing data from different sources\n  quote: The recording durations per data source were selected so that each recording contained\n    around 40 bursts (38 ± 4 bursts, mean ± SE)\n  expected:\n  - quantity: mean number of bursts per recording, over the 31 recordings of Fig. 7\n    value: 38\n    tolerance: 4\n  criterion: Bursts detected as in the opening comment over HO1 to HO8, MO1 to MO9, MS and Pr1 to\n    Pr8, under the code's recording lengths (reading a). Reproduced when the mean count is within\n    tolerance. Reading (b) fixes the count by construction and is not a test of it.\n- id: fig1c-example-burst-count\n  statement: In the example human organoid of Figs. 1 and 2, 46 bursts occur in a three-minute\n    interval.\n  source: Figure 1C legend; Figure 2C legend\n  quote: The population firing rate (gray lines) is plotted relative to the burst peak for 46 burst\n    events measured across a three-minute interval for the same organoid\n  expected:\n  - quantity: number of bursts in 180 s of the example organoid\n    value: 46\n    tolerance: 4.6\n  criterion: The example organoid is not named in the paper (the HMM code uses HO1 as its example).\n    Bursts detected as in the opening comment on the first 180 s of each of HO1 to HO4, with a\n    minimum peak distance of 700 ms (Methods) and 800 ms (code variant). Reproduced when one of the\n    four recordings gives a count within tolerance; that recording is the example organoid for\n    claims fig4d-burst-similarity and fig4f-pca-variance.\n- id: ed1c-lognormal-rates\n  statement: In each of the 8 human organoids the distribution of unit mean firing rates is well fit\n    by a lognormal distribution (R² 0.97 ± 0.04, mean ± STD), while the rates of backbone units\n    alone are not (R² 0.45 ± 0.30).\n  source: Results, Temporal dynamics of neuronal firing sequences, paragraph 1; Extended Data Fig. 1A\n    to C\n  quote: we observed that the distribution of firing rates follows a heavy-tailed, right-skewed\n    lognormal distribution ( n = 8, R 2 = 0.97 ± 0.04, Extended Data Fig. 1A – C ) ... Backbone\n    neurons alone are not well described by a lognormal distribution. R 2 values are 0.45±0.30 across\n    the 8 human brain organoids\n  expected:\n  - quantity: mean R² over HO1 to HO8, all units\n    value: 0.97\n    tolerance: 0.04\n  - quantity: mean R² over HO1 to HO8, backbone units only\n    value: 0.45\n    tolerance: 0.30\n  criterion: Mean rate per unit is its spike count over the recording length. The fit is open\n    between the Methods and code and the Extended Data Fig. 1C legend. Readings (a) a lognormal\n    density fitted by nonlinear least squares to the probability histogram of rates in 20 bins from\n    0 to 10 Hz, ordinary R² (Methods, and plot_multi_rec_figs_backbone.m, whose density divides by\n    (2 sigma)^2 where the standard form has 2 sigma^2, shown as a variant); (b) a normal density\n    fitted to the probability histogram of log rates in ceil(n^0.4) bins (legend). Units either all\n    sorted units (code) or those with at least 30 spikes (Methods). Reproduced when, under one\n    reading, both means are within tolerance; partially reproduced when only the all-unit mean is.\n- id: fig1d-burst-duration\n  statement: Burst durations in the human organoids are on the order of 10² ms.\n  source: Results, Temporal dynamics of neuronal firing sequences, paragraph 1; Figure 1D;\n    Supplementary Fig. 1C\n  quote: Bursts exhibited consistent rate profiles within organoids ( Fig. 1C ), with durations\n    spanning timescales on the order of ≈ 10 2 milliseconds ( Fig. 1D , Supplementary Fig. 1 C )\n  criterion: Burst duration is end minus start as in the opening comment (10% of peak on the coarse\n    population rate). \"On the order of 10² ms\" is read as the decade from 100 to 1000 ms, a standard\n    reading. Reproduced when the median burst duration of each of HO1 to HO4 (Fig. 1D) lies in that\n    decade; partially reproduced when three of the four do. The medians of all 31 recordings\n    (Supplementary Fig. 1C) are reported.\n- id: fig1e-peaks-near-burst-peak\n  statement: Most units reach their peak firing rate close to the peak of the population burst.\n  source: Results, Temporal dynamics of neuronal firing sequences, paragraph 1; Figure 1E\n  quote: A majority of units firing rates peaked in close proximity to the population burst maxima (\n    Fig. 1E )\n  criterion: Peak time per unit and burst, the time of its maximum rate between burst start and end\n    relative to the burst peak, in bursts where it fires at least two spikes (Methods). HO1 to HO4.\n    \"Close proximity\" is not fixed by the paper. Readings for the quantity, (i) each unit's median\n    peak time, (ii) all unit-burst peak times pooled; for the bound, (a) within 50 ms and (b) within\n    100 ms of the burst peak (the Results speak of lags near 10 ms and sequences of about 10² ms).\n    Reproduced when more than half of the values fall within the bound in each organoid, under every\n    reading.\n- id: fig2-backbone-fraction\n  statement: Backbone units, which fire at least twice in every burst, are 28% ± 14% (mean ± STD) of\n    the units in the 8 human organoids.\n  source: Results, Temporal dynamics of neuronal firing sequences, paragraph 3; Supplementary Fig. 1A\n  quote: Backbone units, comprising 28% ± 14% (mean ± STD) of total neurons ( n = 8 organoids,\n    Supplementary Fig. 1 )\n  expected:\n  - quantity: mean backbone fraction over HO1 to HO8\n    value: 0.28\n    tolerance: 0.14\n  - quantity: standard deviation of the backbone fraction over HO1 to HO8\n    value: 0.14\n    tolerance: 0.014\n  criterion: Backbone units as in the opening comment. The denominator can be read as (a) all sorted\n    units in the recording or (b) units with at least 30 spikes. Reproduced when the mean and the\n    standard deviation are both within tolerance under one reading; partially reproduced when only\n    the mean is. The tolerance on the mean is the paper's stated spread.\n- id: fig2e-b2b-correlation\n  statement: Backbone units have higher burst-to-burst correlations of their firing rate than\n    non-rigid units.\n  source: Figure 2E legend; Results, Temporal dynamics of neuronal firing sequences, paragraph 3\n  quote: Backbone neurons consistently exhibited higher burst-to-burst correlation coefficients\n    compared to non-rigid units ( P < 10 −16 , two-sided linear mixed-effects model, n = 4 organoids\n    and 507 single-units)\n  statistics:\n  - test: two-sided linear mixed-effects model\n    p: 1.0e-16\n    p_relation: \"<\"\n    n: 4 organoids and 507 single units\n  expected:\n  - quantity: number of units in the test, HO1 to HO4\n    value: 507\n    tolerance: 51\n  criterion: Burst-to-burst correlation per unit as in the Methods. Burst-only rates; for each pair\n    of bursts, the rate from 250 ms before to 500 ms after each burst peak, MATLAB xcorr with maxlag\n    10 ms and 'coeff' normalization, maximum over lags; mean over all pairs of bursts in which the\n    unit has at least 2 spikes in that window. Units kept when they have at least 2 spikes in at\n    least 30% of bursts (Methods; the code keeps units with at least 2 spikes in at least 70% of\n    bursts, a variant) and at least 30 spikes (code). HO1 to HO4 (code, Fig 2E comment). Test,\n    correlation on unit type with a random intercept per organoid. Reproduced when backbone units are\n    higher with p < 0.05; the unit count is reported against 507.\n- id: fig2g-variance-latency\n  statement: Among backbone units, the variance of firing-rate peak times across bursts grows with\n    the unit's position in the sequence, so later-firing units are more variable.\n  source: Results, Temporal dynamics of neuronal firing sequences, paragraph 3; Figure 2F and 2G\n  quote: Finally, the variability of firing peak times increased with their average latency ( Fig.\n    2F ), a relationship consistently observed across organoids ( Fig. 2G , P < 10 −5 , linear\n    mixed-effects model)\n  statistics:\n  - about: Results\n    test: linear mixed-effects model\n    p: 1.0e-5\n    p_relation: \"<\"\n  - about: Figure 2G legend, relation between relative firing rate peak and peak time variance\n    test: two-sided linear mixed-effects model\n    p: 1.0e-6\n    n: four organoids\n  criterion: Per backbone unit of HO1 to HO4, the median and the variance of its peak time over the\n    bursts in which it fires at least two spikes (Methods). The \"relative position of the peak (from\n    0 to 1)\" of the Methods is read as (a) the unit's rank by median peak time scaled to 0 to 1, or\n    (b) its median peak time rescaled over the backbone period to 0 to 1. Model, variance on\n    relative position with a random intercept per organoid. Reproduced when the slope is positive\n    with p < 0.05 under both readings.\n- id: ed3f-burst-cluster-variability\n  statement: When bursts are clustered by their pairwise unit correlation matrices, the firing rates\n    of non-rigid units vary more between clusters than those of backbone units.\n  source: Results, Temporal dynamics of neuronal firing sequences, paragraph 2; Extended Data Fig. 3F\n  quote: Clustering bursts by their pairwise correlation matrix confirmed that backbone patterns were\n    preserved across clusters, whereas non-rigid units varied substantially ( P < 10 −20 , linear\n    mixed-effects model; Extended Data Fig. 3 )\n  statistics:\n  - test: two-sided linear mixed-effect model\n    p: 1.0e-20\n    p_relation: \"<\"\n  criterion: As in the Supplementary Methods, Burst clustering, and ExtractBurst_ElbowSeeds.py. Per\n    burst, the burst-only rates from 250 ms before to 500 ms after the peak, the correlation matrix\n    of all unit pairs (numpy corrcoef), its lower triangle as a vector; k-means++ on these vectors\n    for k from 2 upward, the best of several seeds per k. The elbow is picked by eye in the paper;\n    readings (a) the knee of the SSE curve by the kneedle rule, (b) the k with the largest\n    silhouette coefficient (the code computes both). Per unit, the CV (STD over mean) of its mean\n    rate across clusters. Recordings, HO1 to HO8; the paper shows HO5 (Or5) as its example and does\n    not name the set, so HO1 to HO4 alone is a second reading. Test, CV on unit type with a random\n    intercept per organoid. Reproduced when non-rigid CV is higher with p < 0.05 under every reading.\n- id: ed4b-gabazine-more-bursts\n  statement: In murine organoids, blocking GABA-A receptors with gabazine increases the number of\n    population bursts.\n  source: Results, Temporal dynamics of neuronal firing sequences, paragraph 2; Extended Data Fig. 4B\n  quote: Meanwhile, the number of bursts increase after gabazine treatment ( P < 0.05, two-sided\n    linear mixed-effect model)\n  statistics:\n  - test: two-sided linear mixed-effect model\n    p: 0.05\n    p_relation: \"<\"\n    n: 5 murine organoids (MO10 to MO14)\n  criterion: Bursts detected as in the opening comment in the baseline and gabazine recordings of\n    MO10 to MO14. Burst count (or rate, if the recordings differ in length) on condition with a\n    random intercept per organoid. Reproduced when gabazine is higher with p < 0.05.\n- id: ed4b-nbqx-cpp-abolish-bursts\n  statement: Blocking AMPA and NMDA receptors with NBQX and R-CPP abolishes population bursts in\n    murine organoids.\n  source: Results, Temporal dynamics of neuronal firing sequences, paragraph 2; Extended Data Fig. 4B\n  quote: Note that bursting disappears after NBQX and R-CPP treatment reflected as a significant\n    decrease in bursting compared to baseline conditions ( P < 0.001, two-sided linear mixed-effect\n    model)\n  statistics:\n  - test: two-sided linear mixed-effect model\n    p: 0.001\n    p_relation: \"<\"\n    n: 5 murine organoids (MO10 to MO14)\n  criterion: As in ed4b-gabazine-more-bursts, baseline against NBQX with R-CPP. Reproduced when the\n    count falls with p < 0.05 and the treated recordings hold no burst or nearly none (at most one\n    per recording, given that the paper says bursting disappears).\n- id: ed4c-gabazine-participation\n  statement: Gabazine increases the fraction of bursts in which units fire at least two spikes.\n  source: Extended Data Fig. 4C\n  quote: The fraction of bursts in which units are active increases significantly after gabazine\n    treatment ( P < 10 −7 , two-sided linear mixed-effect model)\n  statistics:\n  - test: two-sided linear mixed-effect model\n    p: 1.0e-7\n    p_relation: \"<\"\n    n: 5 murine organoids (MO10 to MO14)\n  criterion: Per unit and recording, the fraction of bursts with at least two spikes between burst\n    start and end. Units are matched between conditions only if the dataset identifies them across\n    recordings (the paper records \"the same electrode configuration\"); otherwise units are pooled per\n    condition. Model, fraction on condition with a random intercept per organoid (and per unit when\n    matched). Reproduced when gabazine is higher with p < 0.05.\n- id: ed4d-gabazine-rank-order\n  statement: Gabazine makes the order of backbone sequences more consistent across bursts.\n  source: Extended Data Fig. 4D\n  quote: There is a significant increase in backbone sequence order similarity after treatment with\n    gabazine ( P < 10 −20 , two-sided linear mixed-effect model)\n  statistics:\n  - test: two-sided linear mixed-effect model\n    p: 1.0e-20\n    p_relation: \"<\"\n    n: 5 murine organoids (MO10 to MO14)\n  criterion: As in the Supplementary Methods, Firing rate peak rank order correlations. Per burst,\n    the backbone units ranked by their peak rate time; Spearman correlation for every pair of bursts;\n    each normalized to the mean over 100 shuffles. The legend says z-scored and the Supplementary\n    Methods say (A - B)/(A + B); both are readings. Backbone units defined per recording with the\n    80% murine organoid threshold. Model, normalized correlation of burst pairs on condition with a\n    random intercept per organoid. Reproduced when gabazine is higher with p < 0.05 under both\n    readings.\n- id: supp2a-backbone-fraction-declines\n  statement: The fraction of backbone units declines as human and murine organoids mature.\n  source: Results, Temporal dynamics of neuronal firing sequences, paragraph 2; Supplementary Fig. 2A\n  quote: Longitudinal recordings showed that the relative fraction of backbone units declined over\n    development ( Supplementary Fig. 2 )\n  criterion: No test is reported. Backbone fraction per organoid and age (human organoids at 6, 7\n    and 8 months per plot_develomental_analysis.m; murine organoids at their recorded weeks).\n    Readings for \"declined\", (a) the mean fraction over organoids is lower at the oldest age than at\n    the youngest, (b) it is lower at the oldest age in every organoid. Reproduced when this holds\n    for both human and murine organoids under both readings; partially reproduced when it holds for\n    one of them.\n- id: supp2c-b2b-increases-with-age\n  statement: The burst-to-burst correlation of units increases over development in human and murine\n    organoids, and backbone units are higher than non-rigid units at every age.\n  source: Results, Temporal dynamics of neuronal firing sequences, paragraph 3; Supplementary Fig. 2C\n  quote: Their firing patterns remained stable across hours ( Supplementary Fig. 8 ) and persisted\n    over months, with correlations increasing during development in both human and murine organoids\n    ( Supplementary Fig. 2C , P < 10 −5 , two-way ANOVA)\n  statistics:\n  - about: human organoids, effect of age\n    test: two-way ANOVA\n    p: 4.14e-6\n  - about: murine organoids, effect of age\n    test: two-way ANOVA\n    p: 9.45e-9\n  criterion: Burst-to-burst correlation per unit as in fig2e-b2b-correlation, for each organoid and\n    age. Two-way ANOVA of unit correlations on age and unit type (the second factor is not named;\n    unit type is the reading the panel's layout implies, organoid is a second reading). Reproduced\n    when the age effect has p < 0.05 with correlations higher at older ages in both groups, and\n    backbone means exceed non-rigid means at every age.\n- id: supp8-backbone-stable-4h\n  statement: Units classed as backbone in one recording are mostly classed as backbone again 4 h\n    later, and backbone units keep more consistent firing patterns across the two recordings than\n    non-rigid units.\n  source: Supplementary Fig. 8A and 8E\n  quote: the majority of units that was detected as a backbone unit at time point 0-hour was also\n    detected as backbone unit at time point 4-hour (top left) for both organoids\n  criterion: HO2 and HO3, recordings at 0 h and 4 h. Units must be identified across the two\n    recordings; the paper does not say how, so this is tested only if the dataset links them (for\n    example by joint sorting). Reproduced when more than half of the 0 h backbone units are backbone\n    at 4 h in both organoids, and the mean 0-to-4 h burst-to-burst correlation (bursts paired across\n    recordings, Methods) is higher for backbone than for non-rigid units in both.\n- id: ed5-shuffle-reduces-b2b\n  statement: Randomizing spike times while keeping unit and population rates reduces burst-to-burst\n    correlations.\n  source: Results, Temporal dynamics of neuronal firing sequences, paragraph 3; Extended Data Fig.\n    5D; Supplementary Fig. 9A\n  quote: Randomized spike trains that preserved mean and single-unit firing rates abolished sequences\n    and significantly reduced burst-to-bust correlations ( Extended Data Fig. 5 , Supplementary Figs.\n    9 - 10 )\n  criterion: Burst-to-burst correlation per unit as in fig2e-b2b-correlation on the real and on the\n    100 shuffled matrices, HO1 to HO8. No test is named. Readings (a) a linear mixed-effects model of\n    correlation on data type (real or shuffled mean) with random intercepts for unit and organoid,\n    (b) the normalized value (A - B)/(A + B) tested above 0 with a random intercept per organoid,\n    one-sided as in Extended Data Fig. 2F. Reproduced when real exceeds shuffled with p < 0.05 for\n    backbone units under both readings.\n- id: fig3e-pairwise-correlation\n  statement: Pairwise cross-correlations of firing rates are higher between backbone units than\n    between backbone and non-rigid units or between non-rigid units.\n  source: Figure 3E legend; Results, Backbone units are a highly correlated ensemble\n  quote: Correlations between backbone units (blue) are significantly higher ( P < 10 −20 , 2-sided\n    linear mixed effects model, n = 4 organoids and 34,056 single unit pairs) than the\n    cross-correlations between pairs of backbone and non-rigid units (gray) and pairs of non-rigid\n    units (yellow)\n  statistics:\n  - test: two-sided linear mixed effects model\n    p: 1.0e-20\n    p_relation: \"<\"\n    n: 4 organoids and 34,056 single unit pairs\n  expected:\n  - quantity: number of unit pairs, HO1 to HO4\n    value: 34056\n    tolerance: 3406\n  criterion: As in the Methods, Pairwise firing rate correlations. Burst-only rates over the whole\n    recording, MATLAB xcorr with maxlag 350 ms and 'coeff', maximum over lags; units with at least\n    30 spikes (legend, code). HO1 to HO4 (code comment for Fig. 3E). Model, correlation on pair type\n    with a random intercept per organoid, emmeans contrasts. Reproduced when backbone pairs exceed\n    both other pair types with p < 0.05.\n- id: fig3f-backbone-pairs-in-tail\n  statement: The distribution of pairwise correlations is skewed and roughly lognormal, and\n    backbone-backbone pairs lie in its upper tail in every organoid.\n  source: Figure 3F legend; Results, Backbone units are a highly correlated ensemble\n  quote: The histogram of all pairwise cross-correlations follows a skewed, lognormal distribution (\n    x -axis is log scale). The pairwise connections between pairs of backbone units populate the tail\n    of this distribution for all organoids\n  depends_on:\n  - fig3e-pairwise-correlation\n  criterion: Pairwise correlations as in fig3e-pairwise-correlation, HO1 to HO4. The paper marks the\n    mean of the backbone-backbone correlations on each histogram and fixes no bound for the tail.\n    Readings, that mean lies above (a) the 75th or (b) the 90th percentile of all pairs. Reproduced\n    when this holds in all four organoids under both readings. The skew of all pairs and the R² of a\n    normal fit to their logarithm (Supplementary Fig. 12C) are reported, not judged.\n- id: fig4d-burst-similarity\n  statement: Across pairs of bursts, the population firing vectors of backbone units are more similar\n    (cosine similarity) throughout the backbone window than those of non-rigid units or of shuffled\n    data.\n  source: Figure 4D legend; Results, Population firing rate timing across burst epochs, paragraph 1\n  quote: Backbone units consistently display significantly higher similarity throughout the backbone\n    window compared with non-rigid or shuffled controls ( P < 10 −20 , paired two-sided t-test)\n  statistics:\n  - test: paired two-sided t-test\n    p: 1.0e-20\n    p_relation: \"<\"\n  depends_on:\n  - fig1c-example-burst-count\n  criterion: As in the Methods, Burst similarity score, and comp_burst_sim in the code. At each 1 ms\n    frame relative to the burst peak, the cosine similarity of the unit rate vectors of every pair of\n    bursts. The code z-scores each unit's rate over the recording first (the Methods are silent, the\n    code is followed) and uses full rates for real data and burst-only rates for the shuffles.\n    Backbone window, from the earliest to the latest median peak time of backbone units. At each\n    frame of the window, a paired two-sided t-test over burst pairs (lower triangle) of backbone\n    against non-rigid and backbone against shuffled, at Bonferroni alpha 0.05 over frames (code).\n    Example organoid from fig1c-example-burst-count. Reproduced when backbone is higher and\n    significant at every frame of the window for both comparisons; partially reproduced when that\n    holds for at least 90% of frames. HO1 to HO8 are reported.\n- id: fig4e-similarity-rises-at-backbone-onset\n  statement: In every human organoid the burst similarity rises from the onset of the backbone period\n    and stays high during it.\n  source: Results, Population firing rate timing across burst epochs, paragraph 1; Figure 4E;\n    Supplementary Fig. 13D\n  quote: Across organoids, burst similarity increased at backbone onset and plateaued during their\n    activation ( Fig. 4E , Supplementary Fig. 13D , n = 8 organoids)\n  criterion: Burst similarity over all units as in fig4d-burst-similarity, for HO1 to HO8, within each\n    backbone period. No test is reported. Reproduced when, in all 8 organoids, the mean similarity\n    over the backbone period exceeds its value at the first frame of the period; partially\n    reproduced when that holds in 6 or 7.\n- id: supp13-top-correlated-units-similarity\n  statement: The 20% of units with the highest average pairwise correlation give a higher burst\n    similarity than all units together, and the 20% with the lowest give a lower one.\n  source: Results, Population firing rate timing across burst epochs, paragraph 1; Supplementary Fig.\n    13A to C\n  quote: Notably, the top 20th percentile of highly correlated units (from Fig. 3C ) generated\n    significantly higher burst similarity than the full population, with the effect diminishing as\n    larger percentiles were included ( Supplementary Fig. 13A , C ). Conversely, the lowest 20th\n    percentile reduced similarity\n  depends_on:\n  - fig1c-example-burst-count\n  - fig3e-pairwise-correlation\n  criterion: Units ranked by their mean pairwise correlation (Fig. 3C matrix); burst similarity of the\n    top 20% and of the bottom 20% against all units at every frame of the backbone window by a\n    paired two-sided t-test over burst pairs (Methods), in the example organoid. Reproduced when the\n    top 20% are higher and the bottom 20% lower, each significant at p < 0.05 Bonferroni-corrected\n    over frames, at a majority of frames of the backbone window. The difference in summed\n    similarity for top against bottom percentiles from 20 to 95 is reported.\n- id: fig4f-pca-variance\n  statement: In the example organoid, the first two principal components of backbone unit rates\n    explain 73% of their variance against 25% for non-rigid units, and across organoids backbone\n    units need fewer components than all units while non-rigid units need more.\n  source: Results, Population firing rate timing across burst epochs, paragraph 2; Figure 4F and 4G;\n    Supplementary Fig. 14\n  quote: When populations were divided, backbone units captured far more variance (73%) in the first\n    two PCs compared to non-rigid units (25%) ( Fig. 4F middle/right, Fig. 4G , Supplementary Figs.\n    14 - 15 )\n  expected:\n  - quantity: variance explained by the first two PCs, backbone units, example organoid\n    value: 73\n    tolerance: 7.3\n    unit: percent\n  - quantity: variance explained by the first two PCs, non-rigid units, example organoid\n    value: 25\n    tolerance: 2.5\n    unit: percent\n  depends_on:\n  - fig1c-example-burst-count\n  criterion: PCA as in compute_manifolds of the code, on burst-only rates, each unit mean-centred and\n    scaled to unit standard deviation (the Methods' z-score), by SVD, for all, backbone and non-rigid\n    units. The example organoid is the one of fig1c-example-burst-count; if none matches there, any of\n    HO1 to HO8 that matches counts, as the number's subject is not named. Reproduced when both\n    percentages are within tolerance and, in every organoid of HO1 to HO8, the cumulative variance of\n    the first two PCs is higher for backbone than for all units and lower for non-rigid than for all\n    units; partially reproduced when only the across-organoid pattern holds.\n- id: supp18-hmm-likelihood-real-above-shuffled\n  statement: Hidden Markov models fitted to the organoid spike trains give a higher held-out log\n    likelihood on real data than on randomized data with the same unit and population rates.\n  source: Results, Revealing temporal structure with a hidden Markov model, paragraph 1;\n    Supplementary Fig. 18\n  quote: Log likelihood is always greater for real than for randomized data, with no overlap between\n    the distributions for real and shuffled data\n  criterion: Poisson-observation HMMs (SSM), 30 ms bins, K from 10 to 30, fitted by EM (code\n    tolerance 1e-3, at most 5000 iterations), for HO1 to HO8 (Supplementary Methods). Validation by\n    5-fold cross-validation. The Supplementary Methods fit each fold on a random 80% of the data and\n    score the other 20%; the code (cv_scores) holds out a random 10% of the time bin by unit entries\n    instead, shown as a variant. Score, held-out log likelihood per entry on real data against the\n    randomized (Okun) surrogate in the held-out region. Reproduced when real exceeds surrogate in\n    every fold, K and organoid.\n- id: fig5c-states-converge-at-peak\n  statement: The diversity of HMM states is high before and after bursts and reaches a minimum near\n    the burst peak, where states follow a stereotyped path.\n  source: Results, Revealing temporal structure with a hidden Markov model, paragraph 2; Figure 5C;\n    Supplementary Fig. 19B\n  quote: Notably, entropy consistently approaches a local minimum near burst peaks, indicating a\n    convergence toward specific states with higher transition probabilities during the initiation of\n    sequential activation patterns\n  criterion: HMMs as in supp18-hmm-likelihood-real-above-shuffled fitted to the full data; most likely\n    state per bin (the code uses SSM most_likely_states); per bin from 500 ms before to 500 ms after\n    each burst peak, the Shannon entropy of the state distribution across bursts (Supplementary Fig.\n    19B), per model, then averaged over K. \"Near burst peaks\" is not fixed; readings, the minimum lies\n    (a) within 90 ms (three bins) of the peak, (b) within the backbone window. Reproduced when, in at\n    least 6 of the 8 organoids, the minimum is near the peak and lower than the entropy at both ends\n    of the window, under both readings.\n- id: fig5d-backbone-more-states\n  statement: Backbone units are active across a larger pool of HMM states than non-rigid units.\n  source: Results, Revealing temporal structure with a hidden Markov model, paragraph 3; Figure 5D;\n    Supplementary Fig. 21\n  quote: Backbone ensembles spanned a larger pool of HMM states than non-rigid units ( Fig. 5D ,\n    Supplementary Fig. 21 )\n  depends_on:\n  - fig5c-states-converge-at-peak\n  criterion: Consistency of a unit in a state, the fraction of the state's realizations (bins where\n    it is most probable) in which the unit fires at least once (Supplementary Methods). The size of\n    the \"pool\" is not defined; readings (a) the number of states with consistency above 0.5, (b) the\n    mean consistency over states. HO1 to HO8, K from 10 to 30. No test is reported; a linear\n    mixed-effects model on unit type with random intercepts for organoid and K. Reproduced when\n    backbone is higher with p < 0.05 under both readings.\n- id: fig5f-svm-states-beat-rate\n  statement: A linear classifier on HMM state consistency separates backbone from non-rigid units\n    with 83.9% ± 12.0% accuracy, above the 63.2% ± 10.4% reached with firing rate alone.\n  source: Results, Revealing temporal structure with a hidden Markov model, paragraph 3; Figure 5F\n  quote: Linear support vector machine classifiers trained on hidden state features distinguished\n    backbone from non-rigid units with 83.9% ± 12.0% accuracy, significantly exceeding the 63.2% ±\n    10.4% achieved when using firing rate alone ( Fig. 5F )\n  statistics:\n  - test: two-sided Student's t-test\n    p: 0.00021\n    n: 8 organoids\n  expected:\n  - quantity: accuracy on state features, mean over all models of HO1 to HO8\n    value: 83.9\n    tolerance: 12.0\n    unit: percent\n  - quantity: accuracy on firing rate, mean over HO1 to HO8\n    value: 63.2\n    tolerance: 10.4\n    unit: percent\n  depends_on:\n  - fig5d-backbone-more-states\n  criterion: Features per unit, its K consistencies; classifier, standardization then a linear SVM\n    (the code uses sklearn SGDClassifier with its default hinge loss), leave-one-out accuracy over\n    units; baseline, the same classifier on the unit's mean rate (Fig5.py). K from 10 to 30, so 21\n    models per organoid; means and SDs pooled over models (states) and over organoids (rate), as\n    Fig5.py prints them. The tolerances are the paper's stated spreads. The test is open; readings\n    (a) a paired two-sided t-test over the 8 organoids of mean state accuracy against rate accuracy\n    (legend, n = 8), (b) per organoid a one-sample t-test of the 21 state accuracies against the rate\n    accuracy (Fig5.py), required in all 8 (\"in all cases\"). Classifier seeds are a standard choice.\n    Reproduced when both means are within tolerance and states beat rate with p < 0.05 under both\n    readings.\n- id: fig6f-slice-b2b-correlation\n  statement: In neonatal mouse cortical slices, backbone units have higher burst-to-burst\n    correlations than non-rigid units.\n  source: Figure 6F legend; Results, Endogenous sequences in early developing neonatal cortex,\n    paragraph 2\n  quote: Backbone units consistently exhibited higher correlations than non-rigid units (P < 10 −20 ,\n    two-sided linear mixed-effects model, n = 6 mice and 959 single units)\n  statistics:\n  - test: two-sided linear mixed-effects model\n    p: 1.0e-20\n    p_relation: \"<\"\n    n: 6 mice (six slices) and 959 single units\n  expected:\n  - quantity: number of units in the test, six slices\n    value: 959\n    tolerance: 96\n  criterion: As fig2e-b2b-correlation, on the six slices, with the backbone threshold at 90%\n    (Methods) and at 70% (Fig. 6B legend), and a random intercept per slice or per animal. Reproduced\n    when backbone units are higher with p < 0.05 under every reading.\n- id: fig6g-slice-pairwise-correlation\n  statement: In neonatal slices, backbone-backbone pairs are more strongly correlated than mixed or\n    non-rigid pairs.\n  source: Figure 6G legend\n  quote: Backbone–backbone correlations were significantly stronger than mixed or non-rigid pairs (P\n    < 10 −20 , two-sided linear mixed-effects model, n = 6 mice and 125607 single unit pairs)\n  statistics:\n  - test: two-sided linear mixed-effects model\n    p: 1.0e-20\n    p_relation: \"<\"\n    n: 6 mice (six slices) and 125607 single unit pairs\n  expected:\n  - quantity: number of unit pairs, six slices\n    value: 125607\n    tolerance: 12561\n  criterion: As fig3e-pairwise-correlation, on the six slices, with the slice readings of\n    fig6f-slice-b2b-correlation. Reproduced when backbone pairs exceed both other types with p < 0.05\n    under every reading.\n- id: fig7a-backbone-higher-rate\n  statement: Backbone units fire at higher rates than non-rigid units in every model type (human and\n    murine organoids, neonatal slices and primary cultures).\n  source: Results, Comparing sequences across neurodevelopmental models, paragraph 1; Figure 7A\n  quote: Backbone neurons had significantly higher firing rates than non-rigid counterparts ( Fig. 7A\n    , P < 10 −6 , linear mixed-effects model, Supplementary Fig. 23 )\n  statistics:\n  - about: Results\n    test: linear mixed-effects model\n    p: 1.0e-6\n    p_relation: \"<\"\n  - about: Figure 7A legend, backbone against non-rigid within each model type\n    test: two-sided linear mixed-effects model with interactions for unit type and model type\n    p: 1.0e-20\n    p_relation: \"<\"\n    n: human organoids 8 (1048 units), murine organoids 9 (1179 units), slices 6 (786 units),\n      primary cultures 8 (1048 units)\n  expected:\n  - quantity: units, human organoids\n    value: 1048\n    tolerance: 105\n  - quantity: units, murine organoids\n    value: 1179\n    tolerance: 118\n  - quantity: units, neonatal slices\n    value: 786\n    tolerance: 79\n  - quantity: units, primary cultures\n    value: 1048\n    tolerance: 105\n  criterion: Mean rate per unit (spike count over recording length), units with at least 30 spikes,\n    log10-transformed (Fig7.ipynb plots log10 rate; Methods log-transform skewed data). Model, log\n    rate on unit type, model type and their interaction with a random intercept per recording;\n    emmeans contrasts of backbone against non-rigid within each model type. Thresholds per model type\n    as in the opening comment, with both slice readings. Reproduced when backbone is higher with p <\n    0.05 in all four model types; partially reproduced in two or three. Unit counts are reported (the\n    paper gives 1048 for both human organoids and primary cultures).\n- id: fig7a-primary-higher-rate\n  statement: Primary cultures fire at higher rates than organoids and neonatal slices, in both unit\n    groups.\n  source: Results, Comparing sequences across neurodevelopmental models, paragraph 1; Figure 7A\n  quote: However, primary cultures exhibited overall higher firing rates across both populations ( P\n    < 10 −10 for organoids and neonatal slices)\n  statistics:\n  - test: linear mixed-effects model\n    p: 1.0e-10\n    p_relation: \"<\"\n  depends_on:\n  - fig7a-backbone-higher-rate\n  criterion: Model of fig7a-backbone-higher-rate; emmeans contrasts of primary cultures against each\n    of the other three model types, within backbone and within non-rigid units. Reproduced when all\n    six contrasts favour primary cultures with p < 0.05; partially reproduced when at least four do.\n- id: fig7b-normalized-b2b\n  statement: After normalization to shuffled data, backbone units remain more correlated from burst\n    to burst than non-rigid units in organoids and neonatal slices, and backbone units of organoids\n    and slices are more correlated than those of primary cultures.\n  source: Results, Comparing sequences across neurodevelopmental models, paragraph 1; Figure 7B\n  quote: After normalization relative to randomized data, backbone units remained significantly more\n    correlated than non-rigid units in organoids and slices ( P < 10 −10 and P = 7×10 −4 , linear\n    mixed-effects model)\n  statistics:\n  - about: Results, organoids, backbone against non-rigid\n    test: linear mixed-effects model\n    p: 1.0e-10\n    p_relation: \"<\"\n  - about: Results, slices, backbone against non-rigid\n    test: linear mixed-effects model\n    p: 7.0e-4\n  - about: Figure 7B legend, human organoids\n    test: two-sided linear mixed-effects model with interactions for unit type and model type\n    p: 1.0e-20\n    p_relation: \"<\"\n  - about: Figure 7B legend, murine organoids\n    test: two-sided linear mixed-effects model with interactions for unit type and model type\n    p: 0.0011\n  - about: Figure 7B legend, murine slices\n    test: two-sided linear mixed-effects model with interactions for unit type and model type\n    p: 0.0066\n  criterion: Burst-to-burst correlation per unit as in fig2e-b2b-correlation, normalized as (A -\n    B)/(A + B) to the 100 shuffles (Methods; btb_corr_m in the code's single_unit table). Model as in\n    fig7a-backbone-higher-rate on the normalized value (not log-transformed). Reproduced when backbone\n    exceeds non-rigid with p < 0.05 in human organoids, murine organoids and slices, and backbone\n    units of each of these three exceed those of primary cultures with p < 0.05; partially\n    reproduced when only the within-type contrasts hold. The Results and the legend print different\n    p-values for the same panel; both are recorded.\n- id: fig7b-primary-no-b2b-difference\n  statement: In primary cultures, normalized burst-to-burst correlations do not differ between\n    backbone and non-rigid units.\n  source: Results, Comparing sequences across neurodevelopmental models, paragraph 1; Figure 7B\n  quote: whereas no significant difference was observed in primary cultures ( P = 0.06)\n  statistics:\n  - about: Results\n    test: linear mixed-effects model\n    p: 0.06\n  - about: Figure 7B legend\n    test: two-sided linear mixed-effects model with interactions for unit type and model type\n    p: 0.93\n  depends_on:\n  - fig7b-normalized-b2b\n  criterion: A claim of absence, judged on the paper's test, the contrast of backbone against\n    non-rigid in primary cultures in the model of fig7b-normalized-b2b at alpha 0.05. Reproduced when\n    p >= 0.05, not reproduced when p < 0.05; the effect size is given either way.\n- id: fig7c-normalized-pairwise\n  statement: After normalization to shuffled data, backbone-backbone pairs are more correlated than\n    non-rigid pairs in human and murine organoids.\n  source: Figure 7C legend\n  quote: Backbone pairs showed significantly higher correlations in organoids (human: P = 9 × 10 −7 ;\n    murine: P = 1 × 10 −8 ), but not in slices ( P = 0.10) or primaries ( P = 0.16)\n  statistics:\n  - about: human organoids\n    test: two-sided linear mixed-effects model with interactions for unit type and model type\n    p: 9.0e-7\n  - about: murine organoids\n    test: two-sided linear mixed-effects model with interactions for unit type and model type\n    p: 1.0e-8\n  criterion: Pairwise correlations as in fig3e-pairwise-correlation, normalized as (A - B)/(A + B) to\n    the 100 shuffles; per recording, the median over pairs of each type (med_corr in the code's\n    unit_pair_avg table, which Fig7.ipynb plots). Model, the per-recording median on pair type\n    (backbone-backbone, non-rigid-non-rigid), model type and their interaction with a random\n    intercept per recording; emmeans contrast within each model type. Reproduced when backbone pairs\n    are higher with p < 0.05 in both human and murine organoids. Pair-level values with a random\n    intercept per recording are a variant.\n- id: fig7c-slices-primaries-no-pair-difference\n  statement: Normalized pairwise correlations of backbone pairs do not differ from those of\n    non-rigid pairs in slices or in primary cultures.\n  source: Figure 7C legend\n  quote: but not in slices ( P = 0.10) or primaries ( P = 0.16)\n  statistics:\n  - about: slices\n    test: two-sided linear mixed-effects model with interactions for unit type and model type\n    p: 0.10\n  - about: primary cultures\n    test: two-sided linear mixed-effects model with interactions for unit type and model type\n    p: 0.16\n  depends_on:\n  - fig7c-normalized-pairwise\n  criterion: A claim of absence, judged on the contrasts of the model of fig7c-normalized-pairwise\n    at alpha 0.05, with both slice readings. Reproduced when both are non-significant; partially\n    reproduced when one is; not reproduced when neither is. Effect sizes are given.\n- id: fig7c-backbone-pairs-above-random\n  statement: Backbone-backbone pairs in organoids and slices are more correlated than in randomized\n    data, while in primary cultures they are not.\n  source: Results, Comparing sequences across neurodevelopmental models, paragraph 2\n  quote: Backbone-to-backbone pairs in organoids and slices exhibited significantly higher\n    correlations compared to randomized controls ( P < 10 −10 , linear mixed-effects model), an\n    effect not observed in primary cultures ( P > 0.99)\n  statistics:\n  - about: organoids and slices\n    test: linear mixed-effects model\n    p: 1.0e-10\n    p_relation: \"<\"\n  - about: primary cultures\n    test: linear mixed-effects model\n    p: 0.99\n    p_relation: \">\"\n  depends_on:\n  - fig7c-normalized-pairwise\n  criterion: Normalized backbone-backbone pair correlations, (A - B)/(A + B), tested above 0 per model\n    type with a linear mixed-effects model and a random intercept per recording, one-sided as in\n    Extended Data Fig. 2F (the Results do not name the sidedness; two-sided is a variant).\n    Reproduced when the value is above 0 with p < 0.05 in organoids and in slices and not\n    significant in primary cultures (the absence judged on the same test at alpha 0.05).\n- id: fig7d-lag-times\n  statement: Lags of maximum cross-correlation between backbone units are longer in human and murine\n    organoids than in primary cultures, and longer in human organoids than in murine organoids or\n    slices.\n  source: Results, Comparing sequences across neurodevelopmental models, paragraph 2; Figure 7D\n  quote: Correlation Lag-times between backbone units were larger for organoids compared to primary\n    cultures (human organoid vs primary: P = 1 × 10 −8 ; murine organoids vs primary: P = 0.011),\n    with human organoid differing from murine organoids ( P = 0.0096) and slices ( P = 0.0002)\n  statistics:\n  - about: human organoids against primary cultures\n    test: two-sided linear mixed-effects model\n    p: 1.0e-8\n  - about: murine organoids against primary cultures\n    test: two-sided linear mixed-effects model\n    p: 0.011\n  - about: human against murine organoids\n    test: two-sided linear mixed-effects model\n    p: 0.0096\n  - about: human organoids against slices\n    test: two-sided linear mixed-effects model\n    p: 0.0002\n  - about: Results, human organoids against primary cultures\n    test: linear mixed-effects model\n    p: 1.0e-7\n    p_relation: \"<\"\n  criterion: Per backbone pair, the lag of the maximum pairwise correlation (fig3e-pairwise-correlation,\n    maxlag 350 ms), absolute and log10-transformed (lag_vals_log in the code's lag_data table).\n    Zero lags have no logarithm and the code's handling is not shown; readings (a) drop them, (b)\n    set them to 1 ms. Model, log lag on model type with a random intercept per recording; emmeans\n    contrasts. Reproduced when the four contrasts have the paper's direction with p < 0.05 under both\n    readings; partially reproduced when the two contrasts against primary cultures do.\n- id: fig7d-murine-organoids-slices-same-lag\n  statement: Backbone lag times do not differ between murine organoids and slices.\n  source: Figure 7D legend\n  quote: Murine organoids vs slices ( P = 0.47) and primary cultures were not significant ( P = 0.53)\n  statistics:\n  - about: murine organoids against slices\n    test: two-sided linear mixed-effects model\n    p: 0.47\n  - about: second contrast, read as slices against primary cultures\n    test: two-sided linear mixed-effects model\n    p: 0.53\n  depends_on:\n  - fig7d-lag-times\n  criterion: A claim of absence on the model of fig7d-lag-times at alpha 0.05. The legend's second\n    contrast reads as murine organoids against primary cultures, which the same legend reports as P\n    = 0.011, so it is read as slices against primary cultures. Reproduced when murine organoids\n    against slices is non-significant; the slices against primary cultures contrast is reported and\n    judged the same way.\n- id: fig7e-pca-backbone-variance\n  statement: In human and murine organoids, backbone units explain a larger normalized fraction of\n    variance in the first three principal components than non-rigid units; slices and primary\n    cultures show no such difference.\n  source: Results, Comparing sequences across neurodevelopmental models, paragraph 3; Figure 7E;\n    Supplementary Fig. 15\n  quote: Differences were significant for organoids (human: P = 2 × 10 −7 ; murine: P = 0.036), but\n    not slices ( P = 0.29) or primaries ( P = 0.21)\n  statistics:\n  - about: human organoids\n    test: two-sided linear mixed-effects model with interactions for unit type and model type\n    p: 2.0e-7\n  - about: murine organoids\n    test: two-sided linear mixed-effects model with interactions for unit type and model type\n    p: 0.036\n  - about: slices\n    test: two-sided linear mixed-effects model with interactions for unit type and model type\n    p: 0.29\n  - about: primary cultures\n    test: two-sided linear mixed-effects model with interactions for unit type and model type\n    p: 0.21\n  - about: Results, organoids against other model types\n    test: linear mixed-effects model\n    p: 0.001\n    p_relation: \"<\"\n  criterion: PCA as in fig4f-pca-variance. Per recording and unit set, the variance of the first three\n    PCs divided by that of the first X PCs, X the smallest number of PCs among all, backbone and\n    non-rigid units; normalized as (A - B)/(A + B) to 100 shuffles (Methods; m_value in the code's\n    pca table; Supplementary Fig. 15 says the shuffle mean was subtracted, a variant). Model, value\n    on unit type (backbone, non-rigid), model type and their interaction with a random intercept per\n    recording. Reproduced when backbone exceeds non-rigid with p < 0.05 in human and murine organoids\n    and the contrasts in slices and primary cultures are non-significant at alpha 0.05 (absence on\n    the same test); partially reproduced when only the organoid contrasts hold. The Results also say\n    organoid backbone units exceed those of other model types; that contrast is reported.\n- id: fig7f-hmm-dimensionality\n  statement: HMM state spaces are higher-dimensional in human and murine organoids than in primary\n    cultures.\n  source: Results, Comparing sequences across neurodevelopmental models, paragraph 4; Figure 7F;\n    Supplementary Fig. 25\n  quote: With θ = 0.75, human organoids were separable from slice data ( P = 0.04, linear\n    mixed-effects model with Poisson observations), while primary cultures had significantly lower\n    dimensionality than both human ( P < 0.0001) and murine organoids ( P = 0.003) ( Fig. 7F )\n  statistics:\n  - about: primary cultures against human organoids, Results\n    test: linear mixed-effects model with Poisson observations\n    p: 0.0001\n    p_relation: \"<\"\n  - about: primary cultures against murine organoids, Results\n    test: linear mixed-effects model with Poisson observations\n    p: 0.003\n  - about: human organoids against slices, Results\n    test: linear mixed-effects model with Poisson observations\n    p: 0.04\n  - about: human organoids against primary cultures, Figure 7F legend\n    test: two-sided linear mixed-effects model\n    p: 1.2e-6\n  - about: murine organoids against primary cultures, Figure 7F legend\n    test: two-sided linear mixed-effects model\n    p: 0.0026\n  - about: murine organoids against slices, Figure 7F legend\n    test: two-sided linear mixed-effects model\n    p: 0.51\n  criterion: HMMs as in supp18-hmm-likelihood-real-above-shuffled for all 31 recordings, K from 10 to\n    30. Per model, PCA of the K by units matrix of Poisson rates (exp of the fitted log lambdas,\n    Supplements.py); dimensionality, the smallest number of components whose cumulative explained\n    variance exceeds theta = 0.75 (counted up to 10). Test as in lmem.R, a Poisson GLMM (glmer, log\n    link) of dimensionality on model type with a random intercept per recording, emmeans pairwise\n    contrasts (Tukey adjustment, the emmeans default). Reproduced when primary cultures are lower\n    than human and murine organoids with p < 0.05. The human organoid against slice contrast is\n    reported; the legend's \"but not compared with slices\" next to P = 0.036 is not judged.\n- id: supp24c-nonrigid-more-variable\n  statement: Non-rigid units fire more irregularly (higher CV2) than backbone units in every model\n    type.\n  source: Results, Comparing sequences across neurodevelopmental models, paragraph 4; Supplementary\n    Fig. 24C\n  quote: The CV2 scores are significantly larger for non-rigid units compared to backbone units,\n    reflecting a more Poisson-like firing of non-rigid units (Human organoids P ≤ 10-20, Murine\n    organoids P ≤ 10-20, Murine slices P = 7x10-13, Murine primary cultures P ≤ 10-20\n  statistics:\n  - about: human organoids\n    test: two-sided linear mixed-effect model with sample as grouping variable\n    p: 1.0e-20\n    p_relation: \"<\"\n    n: 31 samples\n  - about: murine organoids\n    test: two-sided linear mixed-effect model with sample as grouping variable\n    p: 1.0e-20\n    p_relation: \"<\"\n    n: 31 samples\n  - about: murine slices\n    test: two-sided linear mixed-effect model with sample as grouping variable\n    p: 7.0e-13\n    n: 31 samples\n  - about: primary cultures\n    test: two-sided linear mixed-effect model with sample as grouping variable\n    p: 1.0e-20\n    p_relation: \"<\"\n    n: 31 samples\n  criterion: CV2 per unit as in Holt et al. (mean over consecutive interval pairs of 2|I2 - I1|/(I2 +\n    I1)), units with at least 30 spikes. The panel does not say whether raw or shuffle z-scored CV2\n    (Methods) is tested; readings (a) raw, (b) z-scored to the 100 shuffles. Model, CV2 on unit type,\n    model type and their interaction with a random intercept per recording. Reproduced when non-rigid\n    exceeds backbone with p < 0.05 in all four model types under both readings. (The paper prints\n    \"P ≤ 10-20\"; p_relation \"<\" stands for it.)\n- id: supp10b-rank-order-by-model\n  statement: The consistency of backbone sequence order across bursts differs between model types,\n    and is higher in human organoids than in primary cultures.\n  source: Supplementary Fig. 10B\n  quote: Main effect of sample type P = 0.004 ... Human organoids vs Murine primary cultures P = 0.0004\n  statistics:\n  - about: main effect of sample type\n    test: two-sided linear mixed-effect model with sample as grouping variable\n    p: 0.004\n    n: 31 samples\n  - about: human organoids against primary cultures\n    test: two-sided linear mixed-effect model with sample as grouping variable\n    p: 0.0004\n    n: 31 samples\n  criterion: Normalized Spearman rank-order correlations of backbone sequences for all burst pairs as\n    in ed4d-gabazine-rank-order, both normalization readings. Model, value on model type with a\n    random intercept per recording. Reproduced when the main effect and the human organoid against\n    primary culture contrast (higher in organoids) have p < 0.05 under both readings. The other five\n    contrasts (P = 0.066, 0.061, 0.99, 0.38, 0.65) are reported.\n- id: supp26-state-traversal\n  statement: HMM state traversal rates during the backbone period are higher in primary cultures than\n    in human organoids and slices, while human and murine organoids do not differ.\n  source: Results, Comparing sequences across neurodevelopmental models, paragraph 4; Supplementary\n    Fig. 26\n  quote: In particular, human and murine organoid cannot be distinguished (P = 0.93), whereas the\n    higher state traversal rate of murine primary cultures is significantly different from that of\n    human organoids (P = .021) and murine acute slices (P < 0.0001) but not significant relative to\n    murine organoids (P = 0.064)\n  statistics:\n  - about: human against murine organoids\n    test: linear mixed-effects model\n    p: 0.93\n  - about: primary cultures against human organoids\n    test: linear mixed-effects model\n    p: 0.021\n  - about: primary cultures against slices\n    test: linear mixed-effects model\n    p: 0.0001\n    p_relation: \"<\"\n  - about: primary cultures against murine organoids\n    test: linear mixed-effects model\n    p: 0.064\n  depends_on:\n  - fig7f-hmm-dimensionality\n  criterion: As state_traversal_df in hmmsupport.py. Per model and burst, the number of distinct most\n    likely states in the bins of the backbone window after the peak offset, averaged over bursts and\n    divided by the window length. Model as in lmem.R, rate on model type plus K (as a factor) with a\n    random intercept per recording, emmeans pairwise contrasts. Reproduced when primary cultures\n    exceed human organoids and slices with p < 0.05 and the human against murine organoid contrast\n    is non-significant (absence at alpha 0.05); the primary against murine organoid contrast is\n    reported.\n- id: supp27-d2-near-critical\n  statement: A subset of every preparation type shows near-critical temporal dynamics (d2 between 0\n    and 0.1), and shuffling spike times raises d2 well above that.\n  source: Results, Firing pattern stability, paragraph 1; Supplementary Fig. 27A; Supplementary\n    Methods, d2 calculation\n  quote: Spike-time shuffling consistently abolished temporal criticality across preparations,\n    producing significantly larger d 2 values ( P < 10 −10 compared to intact data, two-sided Welch\n    t-test)\n  statistics:\n  - about: Results\n    test: two-sided Welch t-test\n    p: 1.0e-10\n    p_relation: \"<\"\n  - about: Supplementary Fig. 27A legend\n    test: two-sided Welch t-test\n    p: 2.84e-31\n  expected:\n  - quantity: human organoids passing the AR fit check\n    value: 3\n    tolerance: 0\n  - quantity: murine organoids passing\n    value: 7\n    tolerance: 0\n  - quantity: slices passing\n    value: 4\n    tolerance: 0\n  - quantity: primary cultures passing\n    value: 7\n    tolerance: 0\n  criterion: As the Supplementary Methods, d2 calculation. Spike counts over all units in 30 ms bins,\n    z-scored; an order-20 AR model by Yule-Walker; d2 from the AR coefficients with the code of Sooter\n    et al. (figshare article 25927081, version 1, as r_download.sh fetches). Shuffled control, each\n    neuron's spike times shuffled independently keeping its rate (not the Okun swap). Preparations\n    are kept when the AR model's simulated avalanche size and duration distributions and power\n    spectrum lie within one order of magnitude of the data's; the comparison is not specified\n    further, so counts that differ by one are reported as near matches. The counts are exact numbers\n    of recordings and are given no tolerance; reproduced when shuffled d2 exceeds intact d2 by a\n    two-sided Welch t-test with p < 0.05 and the kept intact preparations have d2 at most 0.1;\n    partially reproduced when the test holds but the counts differ. The code's table lists 7 primary\n    cultures (Pr5 absent) of the 8.\n- id: ed2d-alam-el-din-rates\n  statement: Backbone units have higher mean rates than non-rigid units in the Sharf organoid slices\n    (HO1 to HO4) but not in the whole Alam El Din organoids (HO5 to HO8).\n  source: Extended Data Fig. 2D\n  quote: (Sharf et al. P < 10 −20 , Alam El Din et al . P = 0.40, two-sided linear mixed-effect model,\n    n = 4 organoids each)\n  statistics:\n  - about: Sharf et al. recordings\n    test: two-sided linear mixed-effect model\n    p: 1.0e-20\n    p_relation: \"<\"\n    n: 4 organoids\n  - about: Alam El Din et al. recordings\n    test: two-sided linear mixed-effect model\n    p: 0.40\n    n: 4 organoids\n  criterion: Log mean rate per unit (units with at least 30 spikes) on unit type with a random\n    intercept per organoid, fitted separately to HO1 to HO4 and to HO5 to HO8. Reproduced when the\n    Sharf fit has backbone higher with p < 0.05 and the Alam El Din fit has p >= 0.05 (absence judged\n    on the same test); the effect sizes are given.\n- id: ed2e-alam-el-din-b2b\n  statement: Rate-normalized burst-to-burst correlations are higher for backbone than non-rigid units\n    in both sets of human organoid recordings.\n  source: Extended Data Fig. 2E\n  quote: Note the significant difference between backbone and non-rigid units present for both sets\n    of recordings (Sharf et al . P = 1×10 −10 , Alam El Din et al . P = 0.0092, two-sided linear\n    mixed-effect model, n = 4 organoids each)\n  statistics:\n  - about: Sharf et al. recordings\n    test: two-sided linear mixed-effect model\n    p: 1.0e-10\n    n: 4 organoids\n  - about: Alam El Din et al. recordings\n    test: two-sided linear mixed-effect model\n    p: 0.0092\n    n: 4 organoids\n  criterion: Normalized burst-to-burst correlation as in fig7b-normalized-b2b (\"after average rate\n    normalization\"), on unit type with a random intercept per organoid, fitted separately to HO1 to\n    HO4 and HO5 to HO8. Reproduced when backbone is higher with p < 0.05 in both.\n- id: ed2f-backbone-pairs-above-zero\n  statement: In both sets of human organoid recordings, only backbone pairs have rate-normalized\n    pairwise correlations significantly above zero.\n  source: Extended Data Fig. 2F\n  quote: Note that only the normalized correlation for backbone pairs are significantly larger than 0\n    for both sets of recordings (Sharf et al . P = 0.0001, 0.145 and 1 respectively, Alam El Din et al\n    . P = 7×10 −11 , 1 and 1 respectively, one-sided linear mixed-effect model, n = 4 organoids each)\n  statistics:\n  - about: Sharf et al., backbone pairs\n    test: one-sided linear mixed-effect model\n    p: 0.0001\n    n: 4 organoids\n  - about: Sharf et al., backbone and non-rigid pairs\n    test: one-sided linear mixed-effect model\n    p: 0.145\n    n: 4 organoids\n  - about: Sharf et al., non-rigid pairs\n    test: one-sided linear mixed-effect model\n    p: 1\n    n: 4 organoids\n  - about: Alam El Din et al., backbone pairs\n    test: one-sided linear mixed-effect model\n    p: 7.0e-11\n    n: 4 organoids\n  - about: Alam El Din et al., backbone and non-rigid pairs\n    test: one-sided linear mixed-effect model\n    p: 1\n    n: 4 organoids\n  - about: Alam El Din et al., non-rigid pairs\n    test: one-sided linear mixed-effect model\n    p: 1\n    n: 4 organoids\n  criterion: Normalized pairwise correlations as in fig7c-normalized-pairwise, per pair, for each pair\n    type; one-sided test of the intercept above 0 in a linear mixed-effects model with a random\n    intercept per organoid, separately for HO1 to HO4 and HO5 to HO8. Reproduced when backbone pairs\n    are above 0 with p < 0.05 in both sets and the other two pair types are not (absence at alpha\n    0.05); partially reproduced when the backbone result holds but another type is also significant.\n- id: supp5-murine-organoid-forebrain-identity\n  statement: Single-cell RNA sequencing shows that the murine ESC organoids are of predominantly\n    forebrain identity and express AMPA, NMDA and GABA receptor subunit genes.\n  source: Supplementary Fig. 5B and 5C\n  quote: Expression patterns of brain-region specific marker genes reveal predominant forebrain\n    identity of the murine brain organoids used in this study\n  data: elsewhere\n  where: NCBI GEO GSE290330\n  criterion: The PIPseq data of 30-day organoids from three lines (4031 cells after filtering), as in\n    the Supplementary Methods (Seurat 5.1.0, SCTransform, 40 PCs, Leiden clustering at resolution\n    0.5, canonical markers). Not testable on the dandiset, which holds electrophysiology only.\n    Reproduced when forebrain markers (for example Foxg1, Emx1) are expressed in most neuronal\n    clusters and region markers of mid- and hindbrain are not.\n"
}
```

```
File created successfully at: claims/001603/10.1038-s41593-025-02111-0.yaml (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
python tools/claims_check.py claims/001603/10.1038-s41593-025-02111-0.yaml paper/10.1038-s41593-025-02111-0.txt 2>&1 | head -40
```

Result: not kept, because it reads the paper's text.

**Agent**

As expected, the two quotes containing "human: P" break YAML. I'll make those two quotes double-quoted scalars and fix the supp5 criterion, which named markers the paper does not list.

**Agent calls Bash**

```bash
cd claims/001603 && python3 - <<'EOF'
p='10.1038-s41593-025-02111-0.yaml'
s=open(p).read()
old1='''  quote: Backbone pairs showed significantly higher correlations in organoids (human: P = 9 × 10 −7 ;
    murine: P = 1 × 10 −8 ), but not in slices ( P = 0.10) or primaries ( P = 0.16)'''
new1='''  quote: "Backbone pairs showed significantly higher correlations in organoids (human: P = 9 × 10 −7 ;
    murine: P = 1 × 10 −8 ), but not in slices ( P = 0.10) or primaries ( P = 0.16)"'''
old2='''  quote: Differences were significant for organoids (human: P = 2 × 10 −7 ; murine: P = 0.036), but
    not slices ( P = 0.29) or primaries ( P = 0.21)'''
new2='''  quote: "Differences were significant for organoids (human: P = 2 × 10 −7 ; murine: P = 0.036), but
    not slices ( P = 0.29) or primaries ( P = 0.21)"'''
old3='''    Reproduced when forebrain markers (for example Foxg1, Emx1) are expressed in most neuronal
    clusters and region markers of mid- and hindbrain are not.'''
new3='''    The markers are those of Supplementary Fig. 5B, which the text does not list, so the set of
    markers and what counts as predominant are open; the claim is recorded and not tested here.'''
for o,n in [(old1,new1),(old2,new2),(old3,new3)]:
    assert o in s, o[:40]
    s=s.replace(o,n)
open(p,'w').write(s)
EOF
cd ../.. && python tools/claims_check.py claims/001603/10.1038-s41593-025-02111-0.yaml paper/10.1038-s41593-025-02111-0.txt 2>&1 | tail -40
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd claims/001603 && python3 - <<'EOF'
import re
p='10.1038-s41593-025-02111-0.yaml'
s=open(p).read()
old='''  quote: Correlation Lag-times between backbone units were larger for organoids compared to primary
    cultures (human organoid vs primary: P = 1 × 10 −8 ; murine organoids vs primary: P = 0.011),
    with human organoid differing from murine organoids ( P = 0.0096) and slices ( P = 0.0002)'''
assert old in s
s=s.replace(old, old.replace('quote: Corr','quote: "Corr').replace('( P = 0.0002)','( P = 0.0002)"'))
open(p,'w').write(s)
# find remaining plain scalars with ': ' after the key
for i,l in enumerate(s.split('\n'),1):
    body=l.split(': ',1)[1] if re.match(r'^\s*(- )?[a-z_]+: ',l) else l
    if ': ' in body and not body.lstrip().startswith('"') and not l.lstrip().startswith('#'):
        print(i,l)
EOF
cd ../.. && python tools/claims_check.py claims/001603/10.1038-s41593-025-02111-0.yaml paper/10.1038-s41593-025-02111-0.txt 2>&1 | tail -40
```

Result: not kept, because it reads the paper's text.

**Agent**

The checker passes: 48 claims, 48 quotes, 71 statistical values, 0 problems. Last, a scan of my prose for em dashes, "rather", and colon-space in plain scalars.

**Agent calls Bash**

```bash
f=claims/001603/10.1038-s41593-025-02111-0.yaml; grep -n "—\|rather" $f; python3 -c "
import yaml;d=yaml.safe_load(open('$f'))
c=d['claims'];print(len(c),'claims;',sum('quote' in x for x in c),'quotes;',sum('statistics' in x for x in c),'with statistics;',sum('criterion' in x for x in c),'with criteria;',sum('expected' in x for x in c),'with expected')"
```

```
48 claims; 48 quotes; 31 with statistics; 48 with criteria; 12 with expected
```

**Agent**

I've written `claims/001603/10.1038-s41593-025-02111-0.yaml`. `tools/claims_check.py` finds no problems: 48 claims, 48 quotes, 71 statistical values. Nothing is committed.

**Text read.** The NIH author manuscript in PubMed Central (PMC12912721.1), not the typeset version of record. It has the main text, Methods, figure legends and Extended Data legends. I also read the Supplementary Information PDF, which has Supplementary Figs. 1 to 27 and the Supplementary Methods. Nothing the claims rest on is missing: the HMM, d2, rank-order and burst-clustering methods are all in the Supplementary Methods.

**Code read.** github.com/braingeneers/Protosequences at commit e9a79c4 (2025-05-19). It holds the MATLAB scripts for bursts, backbone units, correlations, burst similarity and PCA; the Python spike shuffling; the HMM code with `lmem.R`; the burst clustering; and per-figure processed tables. The R models for Figs. 2, 3, 6 and 7 are not in it.

**Claims.**
- 48 claims, all with quotes and criteria.
- 31 have statistics.
- 12 have expected values.
- One claim (murine organoid scRNA-seq, Supp. Fig. 5) is `data: elsewhere`, at GEO GSE290330. The dandiset holds only electrophysiology, and that claim is recorded but not tested because the paper does not list its markers.
- The rest use the dataset.
- Seven are claims of absence: two in Fig. 7B and 7C, plus Fig. 7D, Fig. 7E's slices and primaries, Fig. 7F, Supp. Fig. 26 and Extended Data Fig. 2D.

**Where the Methods and the code disagree** (the Methods are followed, the code is run as a variant):
- **Minimum gap between bursts:** 700 ms in the Methods, 800 ms in the code.
- **Units kept for burst-to-burst correlation:** at least 2 spikes in at least 30% of bursts (Methods), against at least 70% (code).
- **HMM cross-validation:** an 80/20 split (Supplementary Methods), against holding out 10% of time-bin by unit entries (code).
- **Lognormal fit:** the code's density divides by (2σ)² where the standard form has 2σ².

**Details the paper leaves open, with the readings named:**
- **Recording length:** the code's 180 s or 600 s, or the first segment holding about 40 bursts.
- **Backbone threshold for slices:** 90% (Methods, Supp. Fig. 1) or 70% (Fig. 6B legend). The random effect for slices is per slice or per animal, since the legend says n = 6 mice.
- **R² of the lognormal fit:** a lognormal fitted to the rate histogram, or a normal fitted to the log-rate histogram. Either over all units or over units with at least 30 spikes.
- **Backbone fraction denominator:** all sorted units, or units with at least 30 spikes.
- **"Close proximity" (Fig. 1E):** within 50 ms or within 100 ms of the burst peak, on per-unit medians or on pooled peak times.
- **Relative position (Fig. 2G):** rank scaled to 0 to 1, or median peak time rescaled over the backbone period.
- **Burst-clustering k:** the knee of the SSE curve, or the largest silhouette coefficient.
- **Rank-order normalization:** z-score or (A−B)/(A+B).
- **Second factor of the Supp. Fig. 2 two-way ANOVA:** unit type or organoid.
- **Sidedness and form of "significantly reduced" after shuffling:** a model of real against shuffled values, or a one-sided test of the normalized value above 0.
- **"Tail" (Fig. 3F):** the backbone-pair mean above the 75th or the 90th percentile of all pairs.
- **Entropy minimum (Fig. 5C):** within 90 ms of the peak, or within the backbone window.
- **"Pool of states" (Fig. 5D):** states with consistency above 0.5, or mean consistency over states.
- **Fig. 5F test:** a paired t-test over the 8 organoids, or per-organoid one-sample t-tests as in the code.
- **Zero lags in Fig. 7D:** dropped, or set to 1 ms.
- **CV2:** raw or z-scored to shuffles.
- **The d2 exclusion rule:** "more than one order of magnitude" is not specified further.

**Gaps that limit testing:**
- The example organoid of Figs. 1, 2 and 4 is not named. It is to be found by its 46 bursts in three minutes.
- No way to match units across recordings is given, which Supp. Fig. 8 (4 h stability) and the gabazine participation analysis need. These are tested only if the dataset links units.
- The text and legends print different p-values for Figs. 7B, 7D and 7F, and both are recorded.
- The paper gives 1048 units for both human organoids and primary cultures, so one of those counts may be a copying error.
- The Fig. 7D legend contradicts itself on murine organoids against primary cultures. I read its second contrast as slices against primary cultures.

## End of run

43 turns, 10 minutes, result: success.
