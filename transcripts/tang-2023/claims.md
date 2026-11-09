# 000447 · claims · run 39968700902

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cat docs/protocol.md; ls claims/001453/ paper/; ls claims | head; ls claims/000447 2>/dev/null
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
ls claims/001453/ paper/; ls claims/000447 2>&1; wc -c paper/*
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cat claims/001453/10.1016-j.cub.2025.04.027.yaml | head -250
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
[... 230 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "paper/10.1016-j.celrep.2023.112246.txt"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd paper; python3 -c "
s=open('10.1016-j.celrep.2023.112246.txt').read()
print(s[51000:90000])"
```

```
<persisted-output>
Output too large (38.3KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/c8833086-8f5a-40e7-a3b2-e2b8bb29ccfd/tool-results/bylydr8y4.txt

Preview (first 2KB):
n decoders. For cross-validation decoders, we considered all 35 dichotomies that divide the 8 clusters in Figures 4A and 4B into 2 groups of 4 conditions. 35 For each dichotomy, the binary decoder was built using a 4-fold cross-validation, of which data samples of all conditions were split into 4 groups with one group as the test data ( Figures S7C and S7D ). For all the binary decoders, we used a C-Support Vector Machine (SVM) with a linear kernel through the libsvm library. 79 Significance was estimated using permutation of trial labels ( n = 1,000 times ). We also tested the CCGP against a geometric random model that destroys the geometrical structure but preserves within-condition noise structure in the data ( Figures S7A and S7B ), as in previous studies. 35 , 55 To achieve this, the noise clouds (the trial-by-trial firing rates of each condition) were rotated by permuting the axes of the firing rate space, and we repeated this procedure for each cluster separately ( Figures S7A , left). We then computed the CCGP as described above on these moved clusters to obtain a null model CCGP value ( Figures S7A , right), and repeated this 100 times to get a null distribution ( Figures S7B ). Statistical analysis Data analysis was performed using custom routines in MATLAB (MathWorks) and GraphPad Prism 9 (GraphPad Software). We used nonparametric and two-tailed tests for statistical comparisons throughout the paper, unless otherwise noted. We used ANOVA for multiple comparisons of Gaussian distributions, followed by a Tukey’s test, when appropriate. For non-Gaussian distributions of multiple groups, we used Kruskal-Wallis test with post hoc analysis performed using a Dunn’s test. p < 0.05 was considered the cutoff for statistical significance. Boxplots show m
[... 2 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/c8833086-8f5a-40e7-a3b2-e2b8bb29ccfd/tool-results/bylydr8y4.txt"
}
```

```
1	n decoders. For cross-validation decoders, we considered all 35 dichotomies that divide the 8 clusters in Figures 4A and 4B into 2 groups of 4 conditions. 35 For each dichotomy, the binary decoder was built using a 4-fold cross-validation, of which data samples of all conditions were split into 4 groups with one group as the test data ( Figures S7C and S7D ). For all the binary decoders, we used a C-Support Vector Machine (SVM) with a linear kernel through the libsvm library. 79 Significance was estimated using permutation of trial labels ( n = 1,000 times ). We also tested the CCGP against a geometric random model that destroys the geometrical structure but preserves within-condition noise structure in the data ( Figures S7A and S7B ), as in previous studies. 35 , 55 To achieve this, the noise clouds (the trial-by-trial firing rates of each condition) were rotated by permuting the axes of the firing rate space, and we repeated this procedure for each cluster separately ( Figures S7A , left). We then computed the CCGP as described above on these moved clusters to obtain a null model CCGP value ( Figures S7A , right), and repeated this 100 times to get a null distribution ( Figures S7B ). Statistical analysis Data analysis was performed using custom routines in MATLAB (MathWorks) and GraphPad Prism 9 (GraphPad Software). We used nonparametric and two-tailed tests for statistical comparisons throughout the paper, unless otherwise noted. We used ANOVA for multiple comparisons of Gaussian distributions, followed by a Tukey’s test, when appropriate. For non-Gaussian distributions of multiple groups, we used Kruskal-Wallis test with post hoc analysis performed using a Dunn’s test. p < 0.05 was considered the cutoff for statistical significance. Boxplots show median, 75th (box), and 90th (whiskers) percentile, unless indicated otherwise. All heat maps were obtained using perceptually uniform colormaps from MatPlotLib. 83 , 82 No statistical methods were used to pre-deter
[... 254 more lines not kept]
```

**Agent**

Main text and STAR Methods are read. Next I'm checking whether the supplement text is in the file.

**Agent calls Bash**

```bash
cd paper; grep -n -o "Figure S[0-9]\. [A-Z][^.]*" 10.1016-j.celrep.2023.112246.txt | head -30; grep -n "SUPPLEMENT\|Supplement" 10.1016-j.celrep.2023.112246.txt | cut -c1-200
```

```
562:Figure S1. Configuration of recording rooms and memory performance in familiar-novel environments
582:Figure S2. Electrode locations and cell clusters in different environments
602:Figure S3. Remapping properties of CA1 and PFC cells
622:Figure S4. Reward representation in CA1 and PFC across environments
640:Figure S5. Robust path-equivalent representation that generalizes across trajectories and environments in PFC, but not in 
663:Figure S6. Distance relationship in the original high-dimensional neural space
675:Figure S7. CCGP null models and decoding accuracy for all possible dichotomies
7:319 nihpa Cell reports Cell Rep PMC10124109 10124109 10124109 NIHMS1887302 36924498 10.1016/j.celrep.2023.112246 Geometric transformation of cognitive maps for generalization across hippocampal-pref
46:602, 123–128. 10.1038/s41586-021-04268-7. 87. Campbell MG, Attinger A, Ocko SA, Ganguli S, and Giocomo LM (2021). Distance-tuned neurons drive specialized path integration calculations in medial en
548:##### Supplement: NIHMS1887302-supplement-1.pdf
552:Supplemental information
```

**Agent calls Bash**

```bash
cd paper; sed -n '540,800p' 10.1016-j.celrep.2023.112246.txt
```

```
[84] Dynamic analysis of learning in behavioral experiments. J. Neurosci.. 2004. 10.1523/JNEUROSCI.2908-03.2004

[85] Hippocampal-prefrontal reactivation during learning is stronger in awake compared with sleep states. J. Neurosci.. 2017. 10.1523/JNEUROSCI.2291-17.2017

[86] Toroidal topology of population activity in grid cells. Nature. 2022. 10.1038/s41586-021-04268-7

[87] Distance-tuned neurons drive specialized path integration calculations in medial entorhinal cortex. Cell Rep.. 2021. 10.1016/j.celrep.2021.109669

##### Supplement: NIHMS1887302-supplement-1.pdf

=== page 1 ===
Cell Reports, Volume 42
Supplemental information
Geometric transformation
of cognitive maps for generalization
across hippocampal-prefrontal circuits
Wenbo Tang, Justin D. Shin, and Shantanu P. Jadhav

=== page 2 ===
 
[... 153 more lines not kept]
```

**Agent**

The full text, STAR Methods and supplement are all there. Next I'll get the paper's code and the dandiset's title and description.

**Agent calls Bash**

```bash
cd $TMPDIR && git clone -q https://github.com/JadhavLab/GeometricTransformation && cd GeometricTransformation && git log -1 --format='%H %cd' && find . -type f -not -path './.git/*' | head -100; curl -s https://api.dandiarchive.org/api/dandisets/000447/ | python3 -c "import json,sys;d=json.load(sys.stdin);print(d['draft_version']['name'])"; curl -s https://api.dandiarchive.org/api/dandisets/000447/versions/draft/info/ | python3 -c "import json,sys;d=json.load(sys.stdin)['metadata'];print(d.get('description'));print(d.get('relatedResource'))"
```

Result: the fetched text is not kept.

**Agent**

The code repo is at commit 5e55e69. The dandiset holds the N, F and N′ epochs only, so the de novo learning and the second group of animals are probably not in it. Now reading the code.

**Agent calls Bash**

```bash
cd $TMPDIR/GeometricTransformation && cat README.txt && wc -l */*.m */*/*.m && cat Figure1/*.m
```

```
+-------------------------------------------------------------------------+
|      Geometric transformation of cognitive maps for generalization      |
|                    across hippocampal-prefrontal circuits               |
+-------------------------------------------------------------------------+
README.txt
Copyright (C) 2023, Wenbo Tang, version 1.0
All rights reserved.



BRIEF
=====

Code accompanying the paper: Tang, W., Shin, J. D. & Jadhav, S. P. (2023). Geometric transformation of cognitive maps for generalization across hippocampal-prefrontal circuits. Cell Reports.


GETTING STARTED
===============

Launch MATLAB and cd into the directory containing the code (e.g. '/CellRep_2023/').
[... 289 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/GeometricTransformation/Figure2 && cat cal_PVsimilarity.m poolcells_acrossep.m DFSwb_HPexpt_placefield2_savefields_crossvalid_fun.m
```

```
%---------------------------------------------------------------%
%  This is the main script for calculating population vector    %
%  (PV) similarity  -- Wenbo Tang (Jan 05, 2023)                %
%---------------------------------------------------------------%
clc
close all
clear all;
%%
% set directory
famnov_dir = '/Volumes/NovelFamiliar/';
%%
% the animal list
animal_list = {'AM2','JS17','JS21','ZT2','JS34'};
day = 1;
pos_interp = (0:0.01:1)';%position bins; 2-cm spatial bin
%%
PVcorr_all_PFC_FN = [];
PVcorr_all_CA1_FN = [];
PVcorr_all_PFC_NN = [];
PVcorr_all_CA1_NN = [];
[... 486 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/GeometricTransformation/Figure2 && cat decoding_position_CA1_novelfamiliar_cross.m decoding_position_novelfamiliar_templateN2_batch.m decoding_position_novelfamiliar_batch.m
```

```
function decodinginfo = decoding_position_CA1_novelfamiliar_cross(animalprefix,day,ep,linfields,decoded_trajtime)
%---------------------------------------------------------------%
%  This is the function for CA1 decoding of spatial locations   %
%  during the test trial (cross-validation procedure)           %
%  -- Wenbo Tang (Jan 05, 2023)                                 %
%---------------------------------------------------------------%

% INPUTS:
%
%    animalprefix = animal prefix.
%    day = experimental day.
%    ep = epoch.
%    linfields = linearized place fields with a standardized structure (leave out the testing trial).
%    decoded_bins = time bins to be decoded during the testing trial
%
% OUTPUTS:
%
%    decodinginfo for the time bins to be decoded during the testing trial
%%
% set animal directory
[... 389 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/GeometricTransformation/Figure2 && diff decoding_position_CA1_novelfamiliar_cross.m decoding_position_PFC_novelfamiliar_cross.m | head -60; cat decoding_position_novelfamiliar_trial_batch.m; sed -n 1,80p decoding_position_CA1_novelfamiliar_trial.m; grep -n "shuffle\|randperm\|median\|kruskal\|ranksum\|signrank" *.m
```

```
1c1
< function decodinginfo = decoding_position_CA1_novelfamiliar_cross(animalprefix,day,ep,linfields,decoded_trajtime)
---
> function decodinginfo = decoding_position_PFC_novelfamiliar_cross(animalprefix,day,ep,linfields,decoded_trajtime)
3c3
< %  This is the function for CA1 decoding of spatial locations   %
---
> %  This is the function for PFC decoding of spatial locations   %
50a51
> 
62,65c63,64
<             if isfield(tetinfo{day}{ep_curr}{ttt},'descrip')
<                 if strcmp(tetinfo{day}{ep_curr}{ttt}.descrip,'riptet')
<                     detect_tet = [detect_tet ttt];
<                 end
---
>             if strcmp(tetinfo{day}{ep_curr}{ttt}.area,'PFC')
>                 detect_tet = [detect_tet ttt];
78c77
<         if  strcmp(tetinfo{day}{ep_curr}{tet}.area,'CA1')
[... 198 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/GeometricTransformation/Figure2 && sed -n 80,223p decoding_position_CA1_novelfamiliar_trial.m; sed -n 1,60p matchidx_acrossep.m
```

```
for track = 1:4
                temp1 = linfield1{track};
                pos1 = temp1(:,1);
                lintrack1 = ones(size(pos1))*track;
                occnormrate1 = temp1(:,5);
                
                linfield_hp = [linfield_hp;occnormrate1];

                pos_hp = [pos_hp;pos1];
                lintrack_hp = [lintrack_hp;lintrack1];
           end
           if (max(linfield_hp) >= 3) % peak firing rate max larger than 3 Hz
               a = find(isnan(linfield_hp));
               %pad nan
               if ~isempty(a)
                    [lo,hi]= findcontiguous(a);  %find contiguous NaNs
                    for ii = 1:length(lo) 
                        if lo(ii) > 1 & hi(ii) < length(linfield_hp)
                            fill = linspace(linfield_hp(lo(ii)-1), ...
                                linfield_hp(hi(ii)+1), hi(ii)-lo(ii)+1);
[... 184 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/GeometricTransformation && sed -n 1,80p Figure2/cal_confusionMat_novelfamiliar.m; cat Figure3/cal_SI.m
```

```
%---------------------------------------------------------------%
%  This is the main script for plotting the confusion matrix    %
%  -- Wenbo Tang (Jan 05, 2023)                                 %
%---------------------------------------------------------------%
clc;
clear all
close all;
%%
animalprefix_list = {'AM2','JS17','JS21','ZT2','JS34'};
day = 1;
eps = 4;
usingN2 = 1; % 1, decoding using N' rate maps; 0, decoding using rate maps of the current session
CTXHP = 0; % CTXHP = 1, PFC; CTXHP = 0, CA1
famnov_dir = '/Volumes/NovelFamiliar/'; % set directory

% directory for saved decoding results
filedir = '/Tang_CellRep_2023/Figure2/Decodepos/';
%%
for theAnimal = 1:length(animalprefix_list)
    animalprefix = animalprefix_list{theAnimal};
[... 179 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/GeometricTransformation && sed -n 120,171p Figure2/cal_confusionMat_novelfamiliar.m
```

```
end
            [X,Y] = meshgrid(id_all,id_all);
            [Xp,Yp] = meshgrid(1:round(trackid_raw(track)/4),1:round(trackid_raw(track)/4));
            try
                temp = interp2(X,Y,actual_matrix,Xp,Yp);
            catch
                temp = interp2(X(1:end-1,1:end-1),Y(1:end-1,1:end-1),actual_matrix,Xp,Yp);
            end
            temp(isnan(temp)) = 0;
            try
                actual_matrix_all =...
                            actual_matrix_all +temp;
            catch
                  actual_matrix_all =...
                            actual_matrix_all +temp(1:end-1,1:end-1);
            end
            try
                temp2 = interp2(X,Y,decoded_matrix,Xp,Yp);
            catch
                temp2 = interp2(X(1:end-1,1:end-1),Y(1:end-1,1:end-1),decoded_matrix,Xp,Yp);
[... 33 more lines not kept]
```

**Agent**

SI code: SI(IN) compares linearized trajectories 2 and 4, SI(OUT) compares 1 and 3. A cell is kept only when both its IN pair and its OUT pair peak above 3 Hz. Next, the UMAP and distance code.

**Agent calls Bash**

```bash
cd $TMPDIR/GeometricTransformation && sed -n 60,165p Figure2/matchidx_acrossep.m | grep -n "intersect\|unique\|setdiff\|ismember" ; cat Figure3/cal_UMAP.m
```

```
11:        cellind = setdiff(cellind_raw,exclude_list,'rows');
52:        cellind_ctx = setdiff(cellind_raw,exclude_list,'rows');
69:                   if ~isempty(find(ismember(ctxidx_temp,ctxmatchind(i,:),'rows'),1))
70:                       ctx_rowidx_temp(i) = find(ismember(ctxidx_temp,ctxmatchind(i,:),'rows'),1);
81:                   if ~isempty(find(ismember(hpidx_temp,hpmatchind(i,:),'rows'),1))
82:                       hp_rowidx_temp(i) = find(ismember(hpidx_temp,hpmatchind(i,:),'rows'),1);
98:    ctxi1 = intersect(ctxi1,ctxrowidx{eps(i+1)});
99:    hpi1 = intersect(hpi1,hprowidx{eps(i+1)});
%---------------------------------------------------------------%
%  This is the main script for UMAP transformation of neuronal  %
%  population activity. The UMAP MATLAB toolbox (V4.1) is       %
%  needed (https://www.mathworks.com/matlabcentral/fileexchange/%
%  71902-uniform-manifold-approximation-and-projection-umap).   %
%  -- Wenbo Tang (Jan 07, 2023)                                 %
%---------------------------------------------------------------%
clc
clear all
close all
%%
animalprefix_list = {'AM2','JS17','JS21','ZT2','JS34'};% all animals
[... 171 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/GeometricTransformation && cat .gitattributes; sed -n 1,275p Figure3/cal_UMAP_INSeq_distance.m | sed -n '/spike_umap = run_umap/,$p'
```

```
# Auto detect text files and perform LF normalization
* text=auto
    spike_umap = run_umap(spike_matrix,'min_dist',0.6,'n_neighbors',50,'metric','cosine','n_components',3,'template_file','all_PFCumap_trials_ep6.mat');
else
    spike_umap = run_umap(spike_matrix,'min_dist',0.6,'n_neighbors',50,'metric','cosine','n_components',3,'template_file','all_CA1umap_trials_ep6.mat');
end
%%
% create an unique vector of trajectory labels
traj_label = [];
for tracknum = 1:4
    temp_label = pos_interp + tracknum -1;
    traj_label = [traj_label,temp_label];
end
%%
% calculate INSeq distance
umap_dist_inseq = []; % reset matrix
for track = [1,3]
    if track == 1
        alt_track = 4; %INSeq pair 1, INR-OUTL
    else
[... 121 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/GeometricTransformation/Figure3 && sed -n '/create an unique vector/,/plot results/p' cal_UMAP_TrajPhase_vs_Spatial_distance.m; grep -n "ranksum\|signrank\|ttest" *.m Supplemental/*.m ../Figure4/*.m ../Figure4/Supplemental/*.m
```

```
% create an unique vector of trajectory labels
traj_label = [];
for tracknum = 1:4
    temp_label = pos_interp + tracknum -1;
    traj_label = [traj_label,temp_label];
end
%%
% calculate distance of neural state aligned by spatial location
umap_dist_spatial = [];
for i = 1:length(traj_label(:,1))
    for track = [1,3]
        current_label = traj_label(i,track);
        label_ids = find(spike_matrix_label == current_label);
        spike_umap_currenttraj= spike_umap(label_ids,:);
        if track == 1
           alt_label = traj_label(i,2);%spatial location aligned; INL-OUTL
        else
           alt_label = traj_label(i,4);%spatial location aligned; INR-OUTR
        end
        label_ids_alt = find(spike_matrix_label == alt_label);
[... 27 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/GeometricTransformation/Figure3 && sed -n '/run_umap/,/plot results/p' cal_UMAP_FNdistance.m | head -120; grep -n "shuffle\|randperm" cal_UMAP_FNdistance_shuffle.m | head
```

```
spike_umap = run_umap(spike_matrix,'min_dist',0.6,'n_neighbors',50,'metric','cosine','n_components',3,'template_file','all_PFCumap_trials_ep6.mat');
else
    spike_umap = run_umap(spike_matrix,'min_dist',0.6,'n_neighbors',50,'metric','cosine','n_components',3,'template_file','all_CA1umap_trials_ep6.mat');
end
% UMAP transformed trajectories
spike_umap_avg = spike_umap;
spike_umap_avg_label = spike_matrix_label;
%%
% add back the file folder needed
addpath(genpath('[removed: a home directory path]/Src_Matlab'))
% gather data from the F session
ep = 4; %epoch 4, F
trialnum_all = [];
for theAnimal = 1:length(animalprefix_list)
    animalprefix = animalprefix_list{theAnimal};
    dir = sprintf('%s/%s_direct/',famnov_dir,animalprefix); % set directory
    %%
    trajinfo = loaddatastruct(dir, animalprefix, 'trajinfo', day); % get trajinfo
    %---------trajtime--------%
    trajbound = trajinfo{day}{ep}.trajbound;
[... 107 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/GeometricTransformation/Figure3 && sed -n '/exclude bins with less than 5 cells active/,$p' cal_UMAP_FNdistance.m | sed -n 12,90p; sed -n 175,200p cal_UMAP_FNdistance_shuffle.m
```

```
spike_matrix_label = spike_matrix_label(validid);
%%
% remove the file folder that has functions with the same name as those in the UMAP toolbox
rmpath(genpath('[removed: a home directory path]/Src_Matlab'))
% use template
if CTXHP
    spike_umap = run_umap(spike_matrix,'min_dist',0.6,'n_neighbors',50,'metric','cosine','n_components',3,'template_file','all_PFCumap_trials_ep6.mat');
else
    spike_umap = run_umap(spike_matrix,'min_dist',0.6,'n_neighbors',50,'metric','cosine','n_components',3,'template_file','all_CA1umap_trials_ep6.mat');
end
% UMAP transformed trajectories
spike_umap_avg = spike_umap;
spike_umap_avg_label = spike_matrix_label;
%%
% add back the file folder needed
addpath(genpath('[removed: a home directory path]/Src_Matlab'))
% gather data from the F session
ep = 4; %epoch 4, F
trialnum_all = [];
for theAnimal = 1:length(animalprefix_list)
[... 86 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/GeometricTransformation/Figure3 && sed -n '/F session/,$p' cal_UMAP_FNdistance.m | grep -v "^\s*$" | sed -n '/run_umap/,/figure/p' | tail -40; sed -n 200,268p cal_UMAP_FNdistance_shuffle.m | grep -n "shuf\|ep =\|template"
```

```
spike_umap = run_umap(spike_matrix,'min_dist',0.6,'n_neighbors',50,'metric','cosine','n_components',3,'template_file','all_PFCumap_trials_ep6.mat');
else
    spike_umap = run_umap(spike_matrix,'min_dist',0.6,'n_neighbors',50,'metric','cosine','n_components',3,'template_file','all_CA1umap_trials_ep6.mat');
end
spike_umap_ep4 = spike_umap;
spike_umap_ep4_label = spike_matrix_label;
%%
% calculate the within-cluster distance
umap_dist_ep4 = zeros(length(spike_umap_avg_label),1);
for i = 1:length(spike_umap_avg_label)
    current_label = spike_umap_avg_label(i);
    label_ids = find(spike_umap_ep4_label == current_label);
    spike_umap_ep4_tmp = spike_umap_ep4(label_ids,:);
    dist_tmp = sum((spike_umap_ep4_tmp'-spike_umap_avg(i,:)').^2).^0.5; % Euclidean distance
    umap_dist_ep4(i) = nanmean(dist_tmp);
end
%%
%-------plot results-------%
% load shuffled result
if CTXHP
[... 20 more lines not kept]
```

**Agent**

Figure 3 code is read. The cell-ID shuffle for Figure 3J permutes cells once per trial and projects through the N′ template. Now Figure 4 (CCGP).

**Agent calls Bash**

```bash
cd $TMPDIR/GeometricTransformation/Figure4 && cat decoding_CCGP_linearSVM_simple.m CCGP_trajPhase.m; sed -n 1,225p cal_all_dichotomies.m | grep -v "^\s*%\?$" | sed -n '/trialnum = min/,$p' | head -120
```

```
function [accuracy_training,accuracy_test,accuracy_shuffle,p_value,Model] = decoding_CCGP_linearSVM_simple(dat_all,figopt)
%---------------------------------------------------------------%
%  This is the function for cross-condition generalization
%  performance using linear decoder (linear SVMs)               %
%  -- Wenbo Tang (Jul 13, 2022)                                 %
%---------------------------------------------------------------%

% INPUTS:
%
%    dat_all = all data, with struct:
%    dat_all.Features = Features (3 umap dims x N data points)for training trials
%    dat_all.trajlabel = Trial Labels (1 x N data points) for training trials
%    dat_all.Features_test = Features for testing trials
%    dat_all.trajlabel_test = Trial Labels for testing trials
%
%    figopt = 1, plotting the decision boundary defined by the classifer; 0, not plotting
%
% OUTPUTS:
%
%    accuracy_training = prediction accuracy for training trials
[... 344 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/GeometricTransformation/Figure4 && sed -n 10,100p CCGP_taskSeq.m; grep -n "ep\b\|ep =\|template\|Features_test\b =\|testing\|training" CCGP_environment.m | head -40
```

```
addpath(genpath('[removed: a home directory path]/MATLAB/libsvm-3.22')); % add the libsvm toolbox in path
%%
pos_interp = (0:0.005:1)';% position bins, normalized
CTXHP = 0;% CA1 = 0 , PFC = 1;
figopt = 1; % plot  CCGP result?
seg_id = [0.3,0.8]; % phase id separate early vs. late phases; 30% and 80%
% separate clusters into different sets
testing_sets = [1,3,0.3;4,2,0.3;1,3,0.8;4,2,0.8]; %[traj_id1,traj_id2, seg_id]
% load clusters (dichotomies)
if CTXHP
    load('PFC_clusters_data');
else
    load('CA1_clusters_data');
end
%%
% CCGP using linear SVMs
training_ids = combnk(1:4,3); % leave one data set out
% combination loop
for current_set = 1:length(testing_sets(:,1))
    % gather data
[... 106 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/GeometricTransformation/Figure4 && grep -n "load\|accuracy_all\|median\|mean(" CCGP_environment.m CCGP_trajPhase.m CCGP_taskSeq.m | head; grep -n "ep = \|save" cal_all_dichotomies.m; sed -n 1,96p Supplemental/decoding_dichotomy_main.m | grep -v "^\s*$" | sed -n 1,96p | grep -n "nchoosek\|combnk\|fold\|crossval\|cvpartition\|load\|ranksum" ; cat Supplemental/decoding_dichotomy_linearSVM.m | sed -n 20,61p
```

```
CCGP_environment.m:18:% load clusters (dichotomies)
CCGP_environment.m:20:    load('PFC_clusters_data_ep4'); % clusters in F
CCGP_environment.m:23:    load('PFC_clusters_data'); % clusters in N'
CCGP_environment.m:25:    load('CA1_clusters_data_ep4'); % clusters in F
CCGP_environment.m:28:    load('CA1_clusters_data'); % clusters in N'
CCGP_environment.m:119:    accuracy_all_trajphase(current_set) = accuracy_test;
CCGP_environment.m:224:    accuracy_all_taskseq(current_set) = accuracy_test;
CCGP_environment.m:228:accuracy_all = [accuracy_all_trajphase,accuracy_all_taskseq];
CCGP_environment.m:243:scatter([0.96,0.97,0.98,0.99,1.01,1.02,1.03,1.04],accuracy_all,40,'kd')
CCGP_trajPhase.m:17:% load clusters (dichotomies)
15:ep = 6; %epoch, F = 4, N' = 6
19:savedata = 0; % save clusters?
207:%---save clusters?---%
208:if savedata
212:            save('PFC_clusters_data.mat','spike_umap_seg','spike_matrix_label_seg');
214:            save('PFC_clusters_data_ep4.mat','spike_umap_seg','spike_matrix_label_seg');
220:            save('CA1_clusters_data.mat','spike_umap_seg','spike_matrix_label_seg');
222:            save('CA1_clusters_data_ep4.mat','spike_umap_seg','spike_matrix_label_seg');
18:C_g = combnk(1:8,4); %randomly take 4 clusters out of 8
21:% load clusters (dichotomies)
[... 45 more lines not kept]
```

**Agent**

Code reading is done. Last, a quick look at the path-equivalence script before writing the file.

**Agent calls Bash**

```bash
cd $TMPDIR/GeometricTransformation/Figure3/Supplemental && sed -n 30,135p cal_path_equivalence.m | grep -v "^\s*$"
```

```
exclude_list = [];%JS34
    end
    %%
    % get cell indices, exclude interneurons
    if CTXHP
        [cellind, ~] = matchidx_acrossep(dir, animalprefix, day, exclude_list); %(tet, cell)
    else
        [~, cellind] = matchidx_acrossep(dir, animalprefix, day, exclude_list); %(tet, cell)
    end
    cellnum = length(cellind(:,1));
    %%
    load(sprintf('%s%slinfields0%d.mat',dir,animalprefix,day)); % get linearized place fields
    %%
    temp = zeros(cellnum,length(eps)); %reset matrix
    %-----gather rate maps-----%
    for i = 1:cellnum
          cind = cellind(i,:);
          for ep = eps
              if (length(linfields{day}{ep})>= cind(1))
                    if  (length(linfields{day}{ep}{cind(1)})>= cind(2))
[... 80 more lines not kept]
```

**Agent**

I've read all the code. Before writing, I'll check the rest of the example file and the schema the checker expects.

**Agent calls Bash**

```bash
sed -n 250,600p claims/001453/10.1016-j.cub.2025.04.027.yaml | grep -n "^  [a-z_]*:\|^- \|^[a-z]" | awk -F: '{print $1":"$2}' | sort -t: -k2 -u | head -40; ls tools; grep -rn "kind\|data:" docs/*.md | grep -i "kind:\|with_labels\|elsewhere" | head
```

```
5:  quote
4:  source
2:  statement
6:  statistics
1:- id
__pycache__
agent_run.py
archive_transcripts.sh
build_site.py
build_targets.py
claims_check.py
conversion_issue.py
datasets.py
entry.py
flagged.py
get_papers.sh
notify.py
papers_manifest.py
progress.py
readme_row.py
[... 11 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 1,80p tools/claims_check.py; grep -n "def \|KEYS\|allowed\|fields" tools/entry.py | grep -i claim | head -30
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

[... 61 more lines not kept]
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
import json;s=json.load(open('schemas/claims.schema.json'));print(json.dumps(s['\$defs'],indent=1)[:4000])"; sed -n 205,262p docs/protocol.md
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
[... 140 more lines not kept]
```

**Agent calls Write**

```json
{
 "file_path": "claims/000447/10.1016-j.celrep.2023.112246.yaml",
 "content": "# Claims for Tang, Shin & Jadhav (2023), Cell Reports 42, 112246, on dandiset 000447.\n# Written by an agent (model \"claude-opus-5-5\", Claude Code in GitHub Actions), 2026-10-23,\n# protocol pilot-10 as stated in docs/protocol.md.\n#\n# Text read. The NIH author manuscript in PubMed Central (PMC10124109, NIHMS1887302) as served by\n# Europe PMC, with its STAR Methods and figure legends, and the supplement\n# (NIHMS1887302-supplement-1.pdf, Figures S1 to S7 and their legends), all from\n# paper/10.1016-j.celrep.2023.112246.txt. The version of record was not read. The PDF of the\n# supplement was not opened; its text was enough. One value of the Methods is garbled in the\n# text. The 1D Gaussian that smooths the linearized rate maps reads \"(s = σ cm\" with the\n# number lost (Methods, Spatial fields and linearization). Criteria that use it name it as open.\n#\n# Code read. github.com/JadhavLab/GeometricTransformation at commit\n# 5e55e69f2f089adcfd65bbfae42ec80e60e9903d (16 March 2023), MATLAB. It holds the scripts behind\n# Figures 1 to 4 and S3, S5, S6, S7C-D. They are the behavioural summary, PV similarity, Bayesian\n# decoding, selectivity index, path equivalence, UMAP embedding and distances, CCGP and the 35\n# dichotomies. It does not hold the code that computes rate maps (the Frank/Jadhav lab\n# \"time-filter framework\" in Src_Matlab and usrlocal, not public in this repository). It also\n# lacks the code for the rate-overlap and single-cell spatial correlation of Figure S3A, the\n# ramping cells of Figure S4, the cell-ID shuffles of Figure 2E and the geometric random model\n# of Figure S7A-B. The UMAP templates it loads (all_PFCumap_trials_ep6.mat,\n# all_CA1umap_trials_ep6.mat), its saved performance files, rate maps and single-trial rate maps\n# are not in the repository. The statistical tests were run in GraphPad Prism (Methods), not in\n# the code.\n#\n# Choices the code settles where the Methods are silent, followed below. Epochs 2, 4 and 6 of day 1\n# are N, F and N'. Well 1 is the center, well 2 the left and well 3 the right well, so linearized\n# trajectories 1 to 4 are OUT_L (center to left), IN_L, OUT_R and IN_R. Linear positions are\n# distance from the center well, so inbound trajectories run backwards in that coordinate and\n# phase (distance from the start) is the reversed index for them. CA1 putative principal cells\n# have a mean rate below 7 Hz. PFC cells carry the label PFC. Both need more than 100 spikes in an\n# epoch. Each animal also has a hard-coded list of putative interneurons, given as tetrode and\n# cell pairs (AM2 [6,9]; JS21 [6,3; 6,6; 6,7; 6,8; 7,1; 21,1; 22,1; 25,1]; JS17 [6,1; 7,1]; ZT2\n# [31,1; 31,5; 32,2; 27,1; 14,10]; JS34 none). The cells used for the manifolds, the selectivity\n# index and path equivalence are those found in all three epochs (matchidx_acrossep.m). Animals\n# are AM2, JS17, JS21, ZT2 and JS34.\n#\n# Data the paper used. Five adult male Long-Evans rats with 32 to 64 tetrodes in dorsal CA1 and\n# medial PFC (mainly prelimbic), recorded with SpikeGadgets (spikes 30 kHz, 600 Hz to 6 kHz; LFP\n# 1.5 kHz; overhead camera 30 fps with headstage LEDs). Each learned the W-maze continuous\n# alternation task de novo in a familiar room (8 sessions in a day), then on a later day ran one\n# session in a novel room (N), one in the familiar room (F) and one more in the novel room (N'),\n# each 15 to 20 min, interleaved with rest in a sleep box. Measured variables are spike times of\n# clustered single units, position and speed, linearized position and trajectory type (IN_R,\n# OUT_L, IN_L, OUT_R), reward-well visits and whether each trial was correct, and LFP. A second\n# group of three rats from earlier studies (refs 23 and 85) ran F-N-F'-N' on two days after 5\n# days of training; only their behaviour is used (Figure 1C, S1C). The dandiset's description\n# says each file holds three epochs, novel, familiar and novel again, with spikes, LFP, position\n# and trajectory information. The de novo learning sessions and the F-N-F'-N' rats are data the\n# paper names; the paper says its raw data are on Brandeis servers, available on request, so they\n# are not public anywhere else. No claim uses outside data. Cell counts the attempt can check its\n# selection against are 98 CA1 and 171 PFC cells for the pseudo-population (claim\n# manifold-cell-counts).\nschema_version: 2\ndataset:\n  archive: dandi\n  id: \"000447\"\npaper: doi:10.1016/j.celrep.2023.112246\nclaims:\n- id: fig1b-faster-novel-learning\n  statement: All five rats acquired the task faster in the novel environment than during de novo\n    learning; proportion correct over the first 50 trials is higher in novel learning.\n  source: Figure 1B; Results, Rats generalize learned rules across contexts, paragraph 2\n  quote: Compared with de novo learning, all animals acquired the inbound and outbound task rules\n    faster in the novel environment\n  criterion: Proportion correct is the state-space estimate of the probability of a correct trial\n    (Smith et al. 2004, ref 84; Methods), with background probability 1/3 for inbound and\n    outbound trials combined, as cal_behavperform.m sets it. As behavperform_gather.m does, the\n    novel curve is trials 1 to 50 of the novel sessions (N and N' run together) and the de novo\n    curve is trials 1 to 50 of de novo learning. Reproduced when, for every one of the five rats,\n    the mean of the novel curve over the 50 trials exceeds the mean of the de novo curve. Needs\n    the de novo learning sessions.\n- id: fig1-denovo-final-performance\n  statement: Final performance at the end of de novo learning was 84.3% correct (SD 7.7%).\n  source: Results, Rats generalize learned rules across contexts, paragraph 2\n  quote: final performance, 84.3% ± 7.7%, mean ± SD\n  expected:\n  - quantity: mean proportion correct, final de novo session, across five rats\n    value: 84.3\n    tolerance: 7.7\n    unit: percent\n  criterion: Per rat, the mean of the state-space estimate over the trials of the last de novo\n    session (behavperform_gather.m); the mean over the five rats. Tolerance is the stated SD.\n    Needs the de novo learning sessions.\n- id: fig1c-session-performance\n  statement: Proportion correct differs across de novo session 1, final de novo session, N, F and\n    N', with performance in N above the first de novo session.\n  source: Figure 1C\n  quote: Proportion correct against session number (data points for individual animals;\n    repeated-measures ANOVA with Tukey’s post hoc, F = 40.48 , n.s., p > 0.75 , ***p = 0.0002,\n    **p = 0.0045)\n  statistics:\n  - about: across the five session groups\n    test: repeated-measures ANOVA\n    statistic: F = 40.48\n    p: 0.05\n    p_relation: \"<\"\n    n: 5 rats\n  - about: Tukey post hoc pair (pair not named in the legend)\n    test: Tukey's post hoc\n    p: 0.0002\n  - about: Tukey post hoc pair (pair not named in the legend)\n    test: Tukey's post hoc\n    p: 0.0045\n  - about: Tukey post hoc pair (pair not named in the legend)\n    test: Tukey's post hoc\n    p: 0.75\n    p_relation: \">\"\n  criterion: Per rat and session, the mean of the state-space estimate over the session's trials\n    (behavperform_gather.m), for de novo session 1, final de novo session, N, F and N'. A\n    repeated-measures ANOVA over the five groups with Tukey's post hoc. The legend does not say\n    which pairs the three post hoc values belong to. Reproduced when the ANOVA has p < 0.05 and\n    Tukey's test puts N above de novo session 1 at p < 0.05; the post hoc p for every pair is\n    reported. Needs the de novo learning sessions.\n- id: fig1c-familiar-above-novel\n  statement: In both groups of rats, performance in the familiar environment is higher than in\n    the novel one whatever the order of exposure (N-F-N' group in Figure 1C, F-N-F'-N' group in\n    Figure S1C).\n  source: Results, Rats generalize learned rules across contexts, paragraph 2; Figure 1C;\n    Figure S1C\n  quote: We found that for both animal groups, the performance in the familiar environment was\n    significantly higher than that in the novel one regardless of the order of experience\n  statistics:\n  - about: F-N-F'-N' group, familiar against novel sessions\n    test: repeated-measures ANOVA with Tukey's post hoc\n    statistic: F = 48.98\n    p: 0.0053\n    n: 3 rats\n  - about: F-N-F'-N' group, a second Tukey pair (pair not named)\n    test: repeated-measures ANOVA with Tukey's post hoc\n    p: 0.0005\n    p_relation: \"<\"\n    n: 3 rats\n  criterion: Session means of the state-space estimate as in fig1c-session-performance. For the\n    N-F-N' rats, reproduced when Tukey's post hoc of the repeated-measures ANOVA of Figure 1C\n    puts F above N at p < 0.05 (F above N' is reported too). The F-N-F'-N' rats are from earlier\n    experiments; their part is tested only if their behaviour is in the dataset, the same way\n    (F and F' above N and N', p < 0.05).\n- id: figs1b-first-session-inbound-outbound\n  statement: In the first session, both inbound and outbound performance are higher in novel\n    learning (N) than in de novo learning.\n  source: Figure S1B\n  quote: Note the higher performance for both inbound and outbound during novel learning than de\n    novo learning (****p < 0.0001, rank-sum tests)\n  statistics:\n  - test: rank-sum tests\n    p: 0.0001\n    p_relation: \"<\"\n  criterion: The legend does not give the unit of the rank-sum test; with five rats a p below\n    0.0001 needs more samples, so the samples are trials. The state-space estimate of proportion\n    correct is computed separately for inbound and outbound trials with background probability\n    0.5, as cal_behavperform.m notes for that split. Readings for the samples are (a) the\n    trial-by-trial estimates of all five rats pooled, first de novo session against N; (b) the\n    binary correct or incorrect outcomes of the same trials. Reproduced when, under each reading,\n    the rank-sum test gives p < 0.05 with novel higher, for inbound and for outbound. Needs the\n    de novo learning sessions.\n- id: cells-per-session\n  statement: Cells were tracked across environments, with 30.5 (SD 9.8) CA1 and 37.4 (SD 19.3)\n    PFC cells per session per animal.\n  source: Results, PFC spatial map generalizes, while CA1 completely remaps, across contexts,\n    paragraph 1\n  quote: Cells were stably tracked across environments (mean ± SD = 30.5 ± 9.8 CA1 and 37.4 ± 19.3\n    PFC cells per session per animal\n  expected:\n  - quantity: CA1 cells per session per animal, mean\n    value: 30.5\n    tolerance: 9.8\n  - quantity: PFC cells per session per animal, mean\n    value: 37.4\n    tolerance: 19.3\n  criterion: Cells as the Methods select them, well isolated units with at least 100 spikes in the\n    session, putative interneurons excluded; for the interneurons, the code's rules (CA1 mean rate\n    below 7 Hz, the per-animal exclusion lists). Counted per animal and per session (N, F, N'),\n    giving 15 counts per region; mean and SD over them. Tolerance is the stated SD. The paper\n    does not say whether a cell recorded in all three sessions is counted once per session (the\n    reading used) or once per animal; the second is shown as a variant.\n- id: figs3a-ca1-global-remapping\n  statement: CA1 spatial similarity between the two environments is no different from that of\n    cell-ID shuffles, that is, CA1 remaps globally.\n  source: Results, PFC spatial map generalizes, while CA1 completely remaps, across contexts,\n    paragraph 1; Figure S3A\n  quote: Notably, the distributions of CA1 spatial-representation similarity between two\n    environments were not different from distributions obtained by shuffling cell identities in\n    the same environment\n  criterion: A claim of absence, judged on the paper's test, a one-way ANOVA with Tukey's post hoc\n    (Figure S3A legend) over the CA1 groups N-N', F-N' and shuffle. Spatial similarity is the\n    Pearson correlation of a cell's linearized rate maps (4 trajectories, 2-cm bins) between two\n    sessions (Methods). The shuffle pairs a cell's map in F with a different cell's map in the\n    novel environment (Methods). Cells are the spatially tuned cells of the PV analysis (peak\n    above 3 Hz in either session of the pair, cal_PVsimilarity.m), which the paper's text does\n    not restate for this panel. Reproduced when Tukey's test finds no difference (p > 0.05)\n    between CA1 F-N' and shuffle; the effect size is given either way. Rate maps use the open\n    smoothing width named in fig2d-pv-similarity.\n  depends_on:\n  - fig2d-pv-similarity\n- id: figs3a-pfc-similar-ca1-lower\n  statement: Single-cell rate overlap and spatial correlation of PFC cells across environments\n    (F-N') are as large as across repeated exposures to the novel environment (N-N'), whereas in\n    CA1 they are lower across environments.\n  source: Figure S3A\n  quote: Note that the similarity of PFC firing across familiar-novel environments (F-N’) was as\n    large as with repeated exposures of the novel environment (N-N’; n.s., p > 0.05), in contrast\n    to CA1 (*p = 0.012, ****p < 0.0001, one-way ANOVA with Tukey’s post hoc)\n  statistics:\n  - about: PFC, F-N' against N-N'\n    test: one-way ANOVA with Tukey's post hoc\n    p: 0.05\n    p_relation: \">\"\n  - about: CA1, F-N' against N-N' (one of the two measures, not named)\n    test: one-way ANOVA with Tukey's post hoc\n    p: 0.012\n  - about: CA1, F-N' against N-N' (the other measure)\n    test: one-way ANOVA with Tukey's post hoc\n    p: 0.0001\n    p_relation: \"<\"\n  criterion: Rate overlap is the mean rate in the less active session over that in the more active\n    one; spatial similarity is the Pearson correlation of linearized rate maps (Methods). The\n    paper does not say how the mean rate is taken; readings are (a) the mean of the linearized\n    rate map, (b) spikes over time in the session's run periods. One-way ANOVA with Tukey's post\n    hoc per measure and region over N-N', F-N' and shuffle. Reproduced when, for both measures,\n    PFC F-N' does not differ from N-N' (p > 0.05, judged on the paper's test) and CA1 F-N' is\n    below N-N' at p < 0.05; partially reproduced when this holds for one measure. Cells as in\n    figs3a-ca1-global-remapping.\n  depends_on:\n  - figs3a-ca1-global-remapping\n- id: fig2d-pv-similarity\n  statement: PFC population-vector similarity across environments (F-N') is as high as across\n    repeated exposures to the novel environment (N-N'), while CA1 PV similarity is lower across\n    environments than within the novel environment, where the CA1 map is reinstated.\n  source: Figure 2C and 2D; Results, PFC spatial map generalizes, while CA1 completely remaps,\n    across contexts, paragraphs 1 and 2\n  quote: the PFC spatial-representation similarity between two different environments was just as\n    large as with repeated testing in the same environment\n  statistics:\n  - about: across the four region and environment-pair groups of per-animal means\n    test: repeated-measures ANOVA\n    statistic: F = 83.24\n    p: 0.05\n    p_relation: \"<\"\n    n: 5 rats\n  - about: PFC, F-N' against N-N' (the n.s. pair)\n    test: Tukey's post hoc\n    p: 0.41\n    n: 5 rats\n  - about: CA1, F-N' against N-N'\n    test: Tukey's post hoc\n    p: 0.01\n    n: 5 rats\n  criterion: As cal_PVsimilarity.m computes it, per animal and region. Cells pass the Methods'\n    rules for either session of the pair (more than 100 spikes, interneurons excluded) and are\n    spatially tuned (linearized peak rate above 3 Hz in either session). Each trajectory's\n    linearized rate map is interpolated to 101 bins of normalized length (about 2 cm, as the\n    Methods' 2-cm bins), NaN runs filled linearly, the four trajectories concatenated. PV\n    similarity is the Pearson correlation, bin by bin, of the PVs of two sessions; per animal,\n    the mean over bins. Pairs are N-N' (epochs 2 and 6) and F-N' (epochs 4 and 6). The 1D\n    smoothing width is garbled in the text; the readings are (a) 8 cm, the σ given for the 2D\n    maps in the sentence before, and (b) no width the text fixes, so 4 cm and 2 cm are run as\n    variants; the outcome is the one (a) gives if (a) and the variants agree, and is otherwise\n    methods_underspecified. Rate maps use run periods above 5 cm/s with SWR times excluded and\n    occupancy above 20 ms (Methods). Reproduced when a repeated-measures ANOVA over the four\n    groups (CA1 N-N', CA1 F-N', PFC N-N', PFC F-N') has p < 0.05, Tukey's test finds CA1 F-N'\n    below CA1 N-N' (p < 0.05), and PFC F-N' does not differ from PFC N-N' (p > 0.05, a claim of\n    absence on the paper's test).\n- id: fig2e-ca1-error-familiar\n  statement: Decoding with N' rate maps, CA1 position error is higher in F than in N, and in F no\n    better than with cell-ID shuffled templates.\n  source: Figure 2E; Results, PFC spatial map generalizes, while CA1 completely remaps, across\n    contexts, paragraph 4\n  quote: the error between actual and reconstructed positions in the familiar environment was\n    significantly higher than that in the novel environment and no better than chance for CA1\n  statistics:\n  - about: CA1, F against N\n    test: Kruskal-Wallis test with Dunn's post hoc\n    p: 0.0001\n    p_relation: \"<\"\n  - about: CA1 in F against its cell-ID shuffle (the n.s. comparison)\n    test: Wilcoxon paired test\n    p: 0.14\n  criterion: Decoder as the Methods give it. A memoryless Bayesian decoder with Poisson spiking\n    and a uniform prior over position and trajectory type; templates are the N' linearized rate\n    maps of cells with peak rate at least 3 Hz; spikes in N and F in 200-ms windows; run periods\n    above 5 cm/s; positions within 15 cm of a reward well excluded; the decoded position is the\n    maximum of the posterior, the error the linear distance from the actual position. The Methods\n    say the window moves \"with 50 ms overlap\", a 150-ms step; the code\n    (decoding_position_*_novelfamiliar_cross.m) steps by 50 ms and keeps only bins in its theta\n    periods, which are variants. As the code does, a bin is decoded when its positions lie on one\n    trajectory and at least one cell fires, and the error is measured along the four\n    trajectories laid end to end, so a decode onto the wrong trajectory is far. Time bins pooled\n    over the five rats. Kruskal-Wallis over CA1 N, CA1 F, PFC N and PFC F with Dunn's post hoc.\n    The shuffle permutes cell identities of the N' rate maps (Methods). The paper does not say\n    how many shuffles or what the Wilcoxon test pairs; readings are (a) each bin's error against\n    its error under one shuffle, (b) against its median error over 100 shuffles. Reproduced when\n    Dunn's test puts CA1 F above CA1 N at p < 0.05 and, under each shuffle reading, the CA1 F\n    errors do not differ from the shuffle at p < 0.05 (a claim of absence on the Wilcoxon paired\n    test).\n  depends_on:\n  - fig2d-pv-similarity\n- id: fig2e-pfc-error-stable\n  statement: Decoding with N' rate maps, PFC position error is similar in N and F, and in both\n    well above chance (below the cell-ID shuffles).\n  source: Figure 2E; Results, PFC spatial map generalizes, while CA1 completely remaps, across\n    contexts, paragraph 4\n  quote: whereas PFC decoding was well above chance and similar across environments\n  statistics:\n  - about: PFC, N against F\n    test: Kruskal-Wallis test with Dunn's post hoc\n    p: 0.99\n    p_relation: \">\"\n  - about: a comparison with cell-ID shuffles (not named)\n    test: Wilcoxon paired test\n    p: 0.0023\n  - about: comparisons with cell-ID shuffles (not named)\n    test: Wilcoxon paired test\n    p: 0.0001\n    p_relation: \"<\"\n  criterion: Decoding, groups, test and shuffle readings as in fig2e-ca1-error-familiar.\n    Reproduced when Dunn's test finds no difference between PFC N and PFC F (p > 0.05, a claim of\n    absence on the paper's test) and, under each shuffle reading, PFC errors in N and in F are\n    below their shuffles by the Wilcoxon paired test at p < 0.05.\n  depends_on:\n  - fig2e-ca1-error-familiar\n- id: fig2f-switch-dynamics\n  statement: After the switch from N to F, CA1 decoding error rises within the first trial, while\n    PFC decoding error stays stable.\n  source: Figure 2F; Results, PFC spatial map generalizes, while CA1 completely remaps, across\n    contexts, paragraph 4\n  quote: Interestingly, the decoding error rapidly increased during the first trial after\n    environment switching for CA1 but remained stable for PFC\n  statistics:\n  - about: CA1, trial -1 against trial 1\n    test: Kruskal-Wallis test with Dunn's post hoc\n    p: 0.038\n  - about: PFC, trial -1 against trial 1\n    test: Kruskal-Wallis test with Dunn's post hoc\n    p: 0.99\n    p_relation: \">\"\n  criterion: Decoding with N' templates as in fig2e-ca1-error-familiar, per trial, errors pooled\n    over the five rats. Methods' decoder settings are the main reading; the code's\n    (decoding_position_*_novelfamiliar_trial.m) are a variant (non-overlapping 200-ms bins, no\n    speed or theta filter, more than one active cell, the decode restricted to the current\n    trajectory, absolute error). The paper does not define trial -1. Readings are (a) the last N\n    trial before the switch; (b) the code's, which takes the first 10 trials of N and of F and\n    labels the N trials -10 to -1, so trial -1 is the tenth N trial. Kruskal-Wallis over the\n    trials from -10 to 10 with Dunn's post hoc, per region. Reproduced when, under each reading,\n    CA1 trial 1 exceeds trial -1 at p < 0.05 and PFC trial 1 does not differ from trial -1\n    (p > 0.05, a claim of absence on the paper's test).\n  depends_on:\n  - fig2e-ca1-error-familiar\n- id: figs3c-pfc-assimilation\n  statement: PFC PV similarity across environments grows with experience (F-N' higher than F-N),\n    while CA1 does not change (F-N against F-N' not different) and stays below N-N'.\n  source: Figure S3C; Results, PFC spatial map generalizes, while CA1 completely remaps, across\n    contexts, paragraph 2\n  quote: Furthermore, there was greater assimilation of PFC representations across environments\n    with experience, while CA1 place cells maintained their independent representations\n  statistics:\n  - about: CA1, F-N against F-N'\n    test: one-way ANOVA with Tukey's post hoc\n    p: 0.093\n  - about: PFC, F-N against F-N'\n    test: one-way ANOVA with Tukey's post hoc\n    p: 0.0001\n    p_relation: \"<\"\n  - about: CA1, F-N' against N-N'\n    test: one-way ANOVA with Tukey's post hoc\n    p: 0.0001\n    p_relation: \"<\"\n  - about: PFC, F-N' against N-N'\n    test: one-way ANOVA with Tukey's post hoc\n    p: 0.0013\n  criterion: PV similarity per spatial bin as in fig2d-pv-similarity, bins pooled over the five\n    rats (the cumulative distributions of the panel), for F-N, F-N' and N-N'. One-way ANOVA per\n    region with Tukey's post hoc. Reproduced when PFC F-N' exceeds PFC F-N at p < 0.05, CA1 F-N\n    and F-N' do not differ (p > 0.05, a claim of absence on the paper's test), and CA1 F-N' is\n    below CA1 N-N' at p < 0.05. The PFC F-N' against N-N' difference is reported.\n  depends_on:\n  - fig2d-pv-similarity\n- id: figs3d-pfc-similarity-over-trials\n  statement: Over trials in the novel environment, PFC similarity to the familiar map rises from\n    the first to the last trial, while CA1 similarity does not change.\n  source: Figure S3D\n  quote: PV similarity between novel and familiar environments over trials in the novel\n    environment\n  statistics:\n  - about: CA1, first against last trial\n    test: one-way ANOVA with Tukey's post hoc\n    p: 0.99\n    p_relation: \">\"\n  - about: PFC, first against last trial\n    test: one-way ANOVA with Tukey's post hoc\n    p: 0.0001\n    p_relation: \"<\"\n  criterion: Single-trial rate maps in the novel environment against session-averaged F rate maps;\n    only trials with at least 80% of spatially tuned cells active (legend); PV similarity per bin\n    as in fig2d-pv-similarity. The paper does not say which novel trials. Readings are (a) the\n    trials of N followed by those of N', (b) N alone, (c) N' alone. The single-trial map\n    smoothing is that of the session maps (open, as in fig2d-pv-similarity). One-way ANOVA over\n    trials with Tukey's post hoc on per-bin values. Reproduced when, under each reading, PFC last\n    trial exceeds first trial at p < 0.05 and CA1 first and last do not differ (p > 0.05).\n  depends_on:\n  - fig2d-pv-similarity\n- id: figs4-ramping-fraction\n  statement: Ramping cells make up 16.4% of CA1 cell samples (81 of 495) and 18.1% of PFC cell\n    samples (115 of 636), a cell sample being one cell on one trajectory type.\n  source: Figure S4A and S4B legend\n  quote: ramping cells identified here (CA1 ... 81/495 = 16.4% cell samples; PFC ... 115/636 = 18.1%\n    cell samples across all sessions\n  expected:\n  - quantity: CA1 ramping cell samples, fraction\n    value: 16.4\n    tolerance: 1.64\n    unit: percent\n  - quantity: PFC ramping cell samples, fraction\n    value: 18.1\n    tolerance: 1.81\n    unit: percent\n  - quantity: CA1 cell samples\n    value: 495\n    tolerance: 49.5\n  - quantity: PFC cell samples\n    value: 636\n    tolerance: 63.6\n  criterion: A session-averaged linearized rate map on one trajectory is ramping when the linear\n    regression of rate on traversed position toward the reward has Pearson r > 0.5 and p < 0.05,\n    its peak rate is at least 3 Hz, and its peak lies within 20 cm of the reward location\n    (Methods). The paper does not say which positions enter the regression or which cells form\n    the denominator. Readings for the denominator are (a) cell samples of all three sessions\n    pooled (\"across all sessions\"), (b) N' only (\"identified in N'\"), each over cells with a\n    valid rate map on the trajectory. The regression runs over the whole trajectory up to the\n    reward well. Reproduced when the two fractions are within tolerance under one reading.\n- id: figs4-ramping-generalization\n  statement: PFC ramping cells generalize their reward representation across environments,\n    whereas CA1 ramping cells remap, and the generalization of ramping cells is similar to that of\n    other cells in each region.\n  source: Results, PFC spatial map generalizes, while CA1 completely remaps, across contexts,\n    paragraph 3; Figure S4A to S4C\n  quote: We found that PFC ramping cells generalized reward representations, but the CA1\n    representation remapped across environments ... In addition, the generalization for reward\n    ramping cells was seen to a similar degree to other cells within regions\n  statistics:\n  - about: a comparison not named (n.s.)\n    test: Kruskal-Wallis test with Dunn's post hoc\n    p: 0.05\n  - about: comparisons not named\n    test: Kruskal-Wallis test with Dunn's post hoc\n    p: 0.0001\n    p_relation: \"<\"\n  criterion: PV similarity per bin as in fig2d-pv-similarity, computed separately for ramping cells\n    (identified in N', figs4-ramping-fraction) and other cells, for N-N' and F-N', bins pooled\n    over rats. Kruskal-Wallis over the eight groups (region, ramping or other, environment pair)\n    with Dunn's post hoc. Reproduced when (1) CA1 ramping F-N' is below CA1 ramping N-N' at\n    p < 0.05; (2) PFC ramping F-N' does not differ from PFC ramping N-N' (p > 0.05); (3) ramping\n    and other cells do not differ (p > 0.05) for the same region and environment pair. Parts (2)\n    and (3) are claims of absence on Dunn's test. Partially reproduced when (1) and (2) hold but\n    not (3).\n  depends_on:\n  - figs4-ramping-fraction\n- id: figs4d-reward-location-similarity\n  statement: PV similarity between the environments at the reward wells is the same as at other\n    locations, in both regions.\n  source: Results, PFC spatial map generalizes, while CA1 completely remaps, across contexts,\n    paragraph 3; Figure S4D\n  quote: Finally, in both regions, the similarity of population activity across different\n    environments at reward wells was the same as other locations\n  statistics:\n  - test: Grubbs' test for outliers\n    p: 0.05\n    p_relation: \">\"\n  criterion: A claim of absence on the paper's test. F-N' PV similarity per linear bin over the\n    four trajectories, mean over the five rats (fig2d-pv-similarity), per region. Grubbs' test\n    (two-sided, alpha 0.05) on the bin values; reproduced when no bin at a reward well is an\n    outlier. Which bins count as at a reward well is not given; the bins at the start and end of\n    each trajectory (the well) are used, and the paper's figure marks the wells at the trajectory\n    ends.\n  depends_on:\n  - fig2d-pv-similarity\n- id: figs5d-path-equivalence\n  statement: PFC cells show stronger path equivalence (similar firing at the same trajectory phase\n    across trajectory types) than CA1 cells.\n  source: Figure S5D; Results, Distinct geometries of CA1 and PFC representations, paragraph 1\n  quote: Stronger path equivalence in PFC than CA1 (***p = 0.0004, ****p < 0.0001, F = 25.37,\n    one-way ANOVA with Tukey’s post hoc)\n  statistics:\n  - test: one-way ANOVA\n    statistic: F = 25.37\n    p: 0.05\n    p_relation: \"<\"\n  - about: a PFC against CA1 pair (not named)\n    test: Tukey's post hoc\n    p: 0.0004\n  - about: PFC against CA1 pairs (not named)\n    test: Tukey's post hoc\n    p: 0.0001\n    p_relation: \"<\"\n  criterion: The path-equivalent coefficient R of a cell is the median, over the six pairs of the\n    four trajectory types, of the Pearson correlation of rate maps aligned from trajectory start\n    to end (Methods; cal_path_equivalence.m, which reverses the inbound maps, interpolates to the\n    first trajectory's bins and drops NaN bins). Cells are those found in all three sessions.\n    Groups are the six region by session groups (N, F, N'), as the code plots them. One-way\n    ANOVA with Tukey's post hoc. Reproduced when, in each session, PFC R exceeds CA1 R at\n    p < 0.05; partially reproduced when it holds in one or two sessions.\n- id: figs5e-path-equivalence-stable\n  statement: The path-equivalent coefficient of PFC cells is strongly correlated between\n    environments (r = 0.64), more so than that of CA1 cells (r = 0.21).\n  source: Figure S5E\n  quote: Path-equivalent coefficient is more strongly correlated between environments for PFC than\n    CA1 (****p < 0.0001, Z = 4.25, comparing correlation coefficients; PFC, r = 0.64, p = 8.43e-21;\n    CA1, r = 0.21, p = 0.035; Pearson correlation)\n  statistics:\n  - about: PFC against CA1 correlation coefficients\n    test: comparison of correlation coefficients\n    statistic: Z = 4.25\n    p: 0.0001\n    p_relation: \"<\"\n  - about: PFC, between environments\n    test: Pearson correlation\n    statistic: r = 0.64\n    p: 8.43e-21\n  - about: CA1, between environments\n    test: Pearson correlation\n    statistic: r = 0.21\n    p: 0.035\n  expected:\n  - quantity: PFC Pearson r of R between environments\n    value: 0.64\n    tolerance: 0.064\n  - quantity: CA1 Pearson r of R between environments\n    value: 0.21\n    tolerance: 0.021\n  criterion: R as in figs5d-path-equivalence. The legend does not say which novel session; readings\n    are F against N', F against N. The test comparing the two r values is taken as Fisher's z for\n    independent correlations, the usual test of that name. Reproduced when under one reading both\n    r values are within tolerance and Fisher's z gives p < 0.05 with PFC higher; partially\n    reproduced when PFC r is significantly above CA1 r but a value is out of tolerance.\n  depends_on:\n  - figs5d-path-equivalence\n- id: figs5f-path-equivalence-vs-selectivity\n  statement: Path equivalence and task-sequence selectivity are uncorrelated across cells.\n  source: Figure S5F\n  quote: Path equivalence and task-sequence selectivity are two uncorrelated measures (n.s., all p’s\n    > 0.05; Pearson correlation)\n  statistics:\n  - test: Pearson correlation\n    p: 0.05\n    p_relation: \">\"\n  criterion: A claim of absence on the paper's test, Pearson correlation per region of R\n    (figs5d-path-equivalence) against SI(IN) and against SI(OUT) (fig3d-selectivity-index), cell\n    samples per session. The paper does not say whether the signed or absolute SI is used; both\n    are run. Reproduced when no correlation has p < 0.05 under the signed reading and under the\n    absolute one; when only one reading finds a correlation the claim is methods_underspecified.\n  depends_on:\n  - figs5d-path-equivalence\n  - fig3d-selectivity-index\n- id: fig3d-selectivity-index\n  statement: Inbound and outbound trajectory selectivity indices are negatively correlated in PFC\n    (r = -0.5), reflecting task-sequence selectivity, and positively correlated in CA1 (r = 0.56),\n    reflecting spatial coverage.\n  source: Figure 3D; Results, Distinct geometries of CA1 and PFC representations, paragraph 1\n  quote: As a result, the selectivity indices of IN (IN L vs. IN R ) and OUT (OUT L vs. OUT R )\n    trajectories exhibited a positive correlation for CA1 and an opposite, negative correlation\n    for PFC\n  statistics:\n  - about: PFC, SI(IN) against SI(OUT)\n    test: Pearson correlation\n    statistic: r = -0.5\n    p: 1.35e-16\n  - about: CA1, SI(IN) against SI(OUT)\n    test: Pearson correlation\n    statistic: r = 0.56\n    p: 1.39e-11\n  expected:\n  - quantity: PFC Pearson r, SI(IN) against SI(OUT)\n    value: -0.5\n    tolerance: 0.05\n  - quantity: CA1 Pearson r, SI(IN) against SI(OUT)\n    value: 0.56\n    tolerance: 0.056\n  criterion: SI = (FR_L - FR_R)/(FR_L + FR_R) with FR the mean rate of the linearized rate map on\n    the left or right trajectory, for IN (IN_L, IN_R) and OUT (OUT_L, OUT_R) (Methods). As cal_SI.m\n    does, the right map is interpolated to the left map's bins, means over bins valid on both, and\n    a cell sample counts when the peak rate exceeds 3 Hz on the IN pair and on the OUT pair. Cells\n    found in all three sessions. Each dot is a cell sample in one session (legend; Methods,\n    \"rate maps in different sessions were analyzed separately\"); the paper does not say which\n    sessions enter the panel. Readings are (a) N, F and N' pooled, (b) N' alone, (c) F alone.\n    Reproduced when, under one reading, both r are within tolerance and p < 0.05 with the signs\n    given; when no reading puts both in tolerance but every reading gives PFC r < 0 and CA1 r > 0\n    at p < 0.05, partially reproduced. The p-values printed \"1.35e16\" and \"1.39e11\" have lost\n    their minus signs in the text; they are read as 1.35e-16 and 1.39e-11.\n- id: fig3e-selectivity-stable\n  statement: Trajectory selectivity is stable across environments for PFC cells (r = 0.49 between\n    familiar and novel) but not for CA1 cells (r = 0.12, not significant).\n  source: Figure 3E; Results, Distinct geometries of CA1 and PFC representations, paragraph 1\n  quote: Finally, consistent with spatial remapping results, these properties were stable across\n    environments for PFC neurons but not CA1\n  statistics:\n  - about: PFC, SI in F against SI in the novel environment\n    test: Pearson correlation\n    statistic: r = 0.49\n    p: 2.77e-14\n  - about: CA1, SI in F against SI in the novel environment\n    test: Pearson correlation\n    statistic: r = 0.12\n    p: 0.22\n  expected:\n  - quantity: PFC Pearson r, SI in F against novel\n    value: 0.49\n    tolerance: 0.049\n  - quantity: CA1 Pearson r, SI in F against novel\n    value: 0.12\n    tolerance: 0.012\n  criterion: SI as in fig3d-selectivity-index, with SI(IN) and SI(OUT) pooled in one correlation\n    per region (both shown in the panel, one r given). The legend says \"novel environment\"\n    without naming the session; readings are N' and N. Reproduced when, under one reading, PFC r\n    is within tolerance with p < 0.05 and CA1 r is not significant (p > 0.05, Pearson, the\n    paper's test). Partially reproduced when the PFC correlation is significant and the CA1 one is\n    not but a value is out of tolerance.\n  depends_on:\n  - fig3d-selectivity-index\n- id: manifold-cell-counts\n  statement: The pseudo-populations pooled across animals for the manifold analyses hold 98 CA1 and\n    171 PFC cells.\n  source: STAR Methods, Characterization of neural manifold, paragraph 1; Figure 3F and 3G legend\n  quote: all spatially-tuned units that were active in both environments were pooled across\n    animals to build a pseudo-population of neurons ( n = 98 CA1 and 171 PFC cells, respectively)\n  expected:\n  - quantity: CA1 cells in the pseudo-population\n    value: 98\n    tolerance: 9.8\n  - quantity: PFC cells in the pseudo-population\n    value: 171\n    tolerance: 17.1\n  criterion: The Methods select spatially tuned units active in both environments; the code\n    (cal_UMAP.m with matchidx_acrossep.m) takes every unit found in all three sessions that passes\n    the inclusion rules, with no tuning threshold. Readings are (a) the Methods' (units active in\n    N, F and N' with a linearized peak rate of at least 3 Hz in at least one session), (b) the\n    code's. Reproduced when both counts are within tolerance under one reading; the reading that\n    matches is used for the manifold claims, and if both match, (a).\n- id: fig3fg-manifold-shapes\n  statement: UMAP embeddings show that PFC population activity lies on a ring-shaped manifold,\n    whereas the CA1 manifold has a double V shape resembling the W-maze.\n  source: Figure 3F and 3G; Results, Distinct geometries of CA1 and PFC representations,\n    paragraph 2\n  quote: This unsupervised algorithm revealed that the population activity of PFC cells resides on\n    a ring-shaped manifold, making it distinct from the CA1 neural manifold with a double “V”\n    shape that topologically resembles the physical spatial structure of the W-maze\n  criterion: Embedding as the Methods give it. Single-trial linearized rate maps of the\n    pseudo-population cells (manifold-cell-counts) in N', with the minimum number of trials per\n    trajectory type across animals from the first trial, binned at 1 cm. Bins with fewer than 5\n    active cells are dropped. UMAP with 3 dimensions, cosine metric, 50 neighbours, min_dist 0.6.\n    The code bins each trajectory at 1/200 of its normalized length (201 bins), a variant. The\n    random seed and the UMAP implementation are standard choices (the paper's fitted templates\n    are not public; the code notes that a new fit gives a quantitatively similar result). The\n    paper gives no measure of the ring or V shapes; it validates the embedding by the distance\n    tests of Figure 3H to 3J. The embedding is shown, and the outcome is that of\n    fig3h-inseq-outseq-distance and fig3i-phase-location-distance (reproduced when both are,\n    partially when one is).\n  depends_on:\n  - manifold-cell-counts\n  - fig3h-inseq-outseq-distance\n  - fig3i-phase-location-distance\n- id: fig3h-inseq-outseq-distance\n  statement: In the PFC manifold, trajectories of the same task sequence (InSeq) are closer than\n    trajectories out of sequence (OutSeq); in the CA1 manifold, OutSeq pairs with the same spatial\n    coverage are closer than InSeq pairs.\n  source: Figure 3H; Results, Distinct geometries of CA1 and PFC representations, paragraph 3\n  quote: we found that the distance between two InSeq trajectories was significantly smaller than\n    two OutSeq ones in the PFC manifold, whereas OutSeq pairs with same spatial coverages had\n    smaller distances than InSeq pairs in the CA1 manifold\n  statistics:\n  - test: rank-sum test\n    p: 0.0001\n    p_relation: \"<\"\n  criterion: Embedding as in fig3fg-manifold-shapes. InSeq pairs are OUT_L with IN_R and OUT_R\n    with IN_L; OutSeq pairs are OUT_L with IN_L and OUT_R with IN_R. For every pair of single\n    trials of the two types, the mean Euclidean distance over matched bins in the 3D embedding\n    (cal_UMAP_INSeq_distance.m). The Methods do not say how bins are matched for this panel;\n    the code matches by spatial location for CA1 and by trajectory phase for PFC, which is\n    followed. Matching both regions the same way (by phase, by location) is shown as a variant.\n    Rank-sum test of InSeq against OutSeq trial-pair distances per region. Reproduced when PFC\n    InSeq < OutSeq and CA1 OutSeq < InSeq, each at p < 0.05.\n  depends_on:\n  - manifold-cell-counts\n- id: fig3i-phase-location-distance\n  statement: PFC neural states at the same trajectory phase are closer than those at the same\n    spatial location, while CA1 shows the opposite.\n  source: Figure 3I; Results, Distinct geometries of CA1 and PFC representations, paragraph 3\n  quote: As a result, the distances between PFC neural states for the same trajectory phases were\n    significantly smaller than those for the same spatial locations, while the opposite is true\n    for CA1\n  statistics:\n  - test: rank-sum test\n    p: 0.0001\n    p_relation: \"<\"\n  criterion: Embedding as in fig3fg-manifold-shapes. The Methods take same-phase distances from\n    pairs of the same task sequence and same-location distances from pairs on the same side of\n    the maze, which is the main reading. The code (cal_UMAP_TrajPhase_vs_Spatial_distance.m)\n    takes both from the same-side pairs (OUT_L with IN_L, OUT_R with IN_R), aligned by phase or by\n    location, a variant. Distances are Euclidean in the 3D embedding between all states at the\n    matched bins of the two types, pooled. Rank-sum test of phase against location distances per\n    region. Reproduced when PFC phase < location and CA1 location < phase, each at p < 0.05.\n  depends_on:\n  - manifold-cell-counts\n- id: fig3j-familiar-novel-manifold\n  statement: The PFC manifold is preserved across environments (F states lie closer to N' states\n    than cell-ID shuffles do), while the distortion of the CA1 manifold is similar to that of\n    random shuffles.\n  source: Figure 3J; Results, Distinct geometries of CA1 and PFC representations, paragraph 3\n  quote: We found that the geometric structure of the PFC manifold was largely preserved across\n    environments, whereas the distortion of the CA1 manifold was similar to that from random\n    shuffles\n  statistics:\n  - about: CA1, F-N' against shuffle (the n.s. test of the panels)\n    test: rank-sum test\n    p: 0.16\n  - about: PFC, F-N' against shuffle\n    test: rank-sum test\n    p: 0.0001\n    p_relation: \"<\"\n  criterion: F single-trial activity embedded with the UMAP fitted on N' (template transform,\n    Methods). For each N' state, the mean Euclidean distance to all F states of the same\n    trajectory type and location (Methods; cal_UMAP_FNdistance.m). The chance level shuffles\n    cell identities of the N' activity and embeds it with the same fit; the code draws a new\n    permutation for each trial and runs it once (cal_UMAP_FNdistance_shuffle.m), which is\n    followed. Rank-sum of real against shuffle distances per region. Reproduced when PFC F-N'\n    distances are below the shuffle at p < 0.05 and CA1 F-N' distances do not differ from the\n    shuffle (p > 0.05, a claim of absence on the paper's test).\n  depends_on:\n  - manifold-cell-counts\n- id: figs6-high-dimensional-distances\n  statement: The distance relationships of Figure 3H to 3J hold in the original high-dimensional\n    neural space.\n  source: Figure S6; Results, Distinct geometries of CA1 and PFC representations, paragraph 3\n  quote: In all the cases above, the distance relationship of neural states, which determines the\n    representational geometry, was preserved between the low-dimensional manifold space and the\n    original high-dimensional neural space\n  statistics:\n  - about: the n.s. comparison (not named)\n    test: rank-sum test\n    p: 0.75\n  - about: the other comparisons\n    test: rank-sum test\n    p: 0.0001\n    p_relation: \"<\"\n  criterion: As fig3h-inseq-outseq-distance, fig3i-phase-location-distance and\n    fig3j-familiar-novel-manifold, with Euclidean distances between population vectors of the\n    pseudo-population (Methods, \"distance was computed identically, except for the number of\n    dimensions\"; Figure3/Supplemental/cal_PV_*.m). Reproduced when all three reproduce in the\n    neural space; partially reproduced when one or two do.\n  depends_on:\n  - fig3h-inseq-outseq-distance\n  - fig3i-phase-location-distance\n  - fig3j-familiar-novel-manifold\n- id: fig4d-pfc-ccgp\n  statement: In PFC, the cross-condition generalization performance (CCGP) for trajectory phase,\n    task sequence and environment is high and above trial-label shuffles for every decoder.\n  source: Figure 4D; Results, Distinct abstraction in CA1 and PFC, paragraph 2\n  quote: We found that the CCGP for all three task variables showed high accuracy for PFC\n  statistics:\n  - test: trial-label permutation test\n    p: 0.001\n    p_relation: \"<\"\n    n: 1,000 shuffles\n  criterion: Clusters are the N' (and for the environment, F) embedded states at 20% to 30% and\n    70% to 80% of trajectory length from the start of each of the 4 trajectory types, 8 clusters\n    (Methods; cal_all_dichotomies.m); features are the 3 UMAP coordinates. Linear C-SVM (libsvm,\n    linear kernel, default cost 1), accuracy balanced over the two classes\n    (decoding_CCGP_linearSVM_simple.m). Trajectory phase is trained on 3 trajectory types and\n    tested on the fourth (4 decoders); task sequence is trained on one phase pair and tested on\n    the held-out pair (4 decoders, CCGP_taskSeq.m); environment applies the decoders trained in N'\n    to F (8 decoders, CCGP_environment.m). Significance permutes the labels of training and test\n    sets 1,000 times; p is the fraction of shuffles above the real CCGP. Reproduced when every one\n    of the 16 PFC decoders has p < 0.001 (no shuffle above it).\n  depends_on:\n  - manifold-cell-counts\n- id: fig4d-ca1-ccgp-chance\n  statement: In CA1, CCGP for trajectory phase, task sequence and environment is at or below chance\n    by the trial-label permutation test.\n  source: Figure 4D; Results, Distinct abstraction in CA1 and PFC, paragraph 2\n  quote: Note that all dichotomies can be accurately decoded in PFC (****p < 0.001) but not in CA1\n    (n.s., p > 0.05 , trial-label permutation test)\n  statistics:\n  - test: trial-label permutation test\n    p: 0.05\n    p_relation: \">\"\n    n: 1,000 shuffles\n  criterion: A claim of absence on the paper's test. CCGP as in fig4d-pfc-ccgp for the 16 CA1\n    decoders. Reproduced when no CA1 decoder has p < 0.05; the CCGP values are reported either\n    way.\n  depends_on:\n  - fig4d-pfc-ccgp\n- id: figs7b-geometric-null\n  statement: Against a geometric random model that keeps within-condition noise but destroys the\n    geometry, PFC CCGP is significant while CA1 CCGP is not.\n  source: Figure S7B; Results, Distinct abstraction in CA1 and PFC, paragraph 2\n  quote: CCGP for trajectory phases (circles), task sequences (triangles), and environments\n    (diamonds; horizontal lines, median) against the null-distributions of the geometric random\n    model (red horizontal line shown the 95th percentile; n.s., p > 0.05, **p = 0.0026, ****p\n    <0.0001)\n  statistics:\n  - about: CA1 (n.s.)\n    test: geometric random model\n    p: 0.05\n    p_relation: \">\"\n  - about: a comparison not named\n    test: geometric random model\n    p: 0.0026\n  - about: comparisons not named\n    test: geometric random model\n    p: 0.0001\n    p_relation: \"<\"\n  criterion: Each cluster's noise cloud (trial-by-trial values of the condition) is rotated by\n    permuting the axes of the firing rate space, separately per cluster, and CCGP is recomputed\n    (fig4d-pfc-ccgp), 100 times (Methods). No code for this model is in the repository. The\n    paper does not say in which space the axes are permuted or what is done with the cluster\n    centres (the legend of S7A says \"rotation-translation\"). Readings are (a) permute the 3 UMAP\n    coordinates of each cluster's points about its centroid; (b) permute the neuron axes of each\n    cluster's population vectors and embed them with the N' fit. Reproduced when, under each\n    reading, the PFC CCGP of each variable exceeds the 95th percentile of its null and no CA1\n    CCGP does.\n  depends_on:\n  - fig4d-pfc-ccgp\n- id: figs7d-dichotomies-decodable\n  statement: With traditional cross-validated decoders, most of the 35 dichotomies of the 8\n    clusters are decoded accurately in both CA1 and PFC, with similar accuracy in the two regions.\n  source: Figure S7D; Results, Distinct abstraction in CA1 and PFC, paragraph 2\n  quote: we found that most of the dichotomies were accurately separated in both CA1 and PFC,\n    suggesting that both regions contain a similar amount of decodable variables\n  statistics:\n  - about: PFC against CA1 decoding accuracy over 35 dichotomies\n    test: rank-sum test\n    p: 0.17\n    n: 35 dichotomies per region\n  criterion: The 35 balanced dichotomies of the 8 clusters of fig4d-pfc-ccgp (4 against 4), each\n    decoded by a linear C-SVM with 4-fold cross-validation (libsvm -v 4; decoding_dichotomy_*.m)\n    on the 3 UMAP coordinates; significance by 1,000 trial-label shuffles, p the fraction of\n    shuffles above. Reproduced when more than half of the 35 dichotomies have p < 0.05 in each\n    region (\"most\") and the rank-sum test of PFC against CA1 accuracies does not find a\n    difference (p > 0.05, a claim of absence on the paper's test).\n  depends_on:\n  - fig4d-pfc-ccgp\n"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
python tools/claims_check.py claims/000447/10.1016-j.celrep.2023.112246.yaml paper/10.1016-j.celrep.2023.112246.txt; grep -nP "[^\x00-\x7F]" claims/000447/*.yaml | grep -v "quote\|^\S*:\s" | head; grep -n "—\|rather" claims/000447/*.yaml
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
python3 - <<'E'
import re
for i,l in enumerate(open('claims/000447/10.1016-j.celrep.2023.112246.yaml'),1):
    if l.lstrip().startswith('#'): continue
    s=re.sub(r'^\s*(- )?[a-z_]+: ','',l)
    if ': ' in s: print(i,l.rstrip())
E
```

```
(Bash completed with no output)
```

**Agent calls Bash**

```bash
python3 -c "
import yaml;d=yaml.safe_load(open('claims/000447/10.1016-j.celrep.2023.112246.yaml'))['claims']
print(len(d),sum('quote' in c for c in d),sum('statistics' in c for c in d),sum('criterion' in c for c in d),sum('expected' in c for c in d))"
```

```
32 32 25 32 7
```

**Agent**

I wrote `claims/000447/10.1016-j.celrep.2023.112246.yaml`. The quote checker passes except for one p-value the text prints garbled ("1.39e11" in the Figure 3D legend); I read it as 1.39e-11. Nothing is committed.

**Text read.** The NIH author manuscript (PMC10124109, NIHMS1887302) as served by Europe PMC: main text, STAR Methods, figure legends, and the supplement PDF's text (Figures S1 to S7). I did not read the version of record, and the supplement text was clean enough that I didn't open the PDF.

**Code read.** github.com/JadhavLab/GeometricTransformation at commit 5e55e69. Where the Methods are silent, it settles:
- which epochs are N, F and N′;
- which reward well is center, left and right, and so the order of the four trajectories;
- the rules for excluding interneurons;
- the cells used;
- the CCGP and SVM details.

**Claims.**
- 32 claims, all with quotes and all with criteria.
- 25 carry statistics (52 values) and 7 carry expected numbers.
- All are `data: dataset`; the paper uses no outside data.
- They cover Figure 1 and S1 (behaviour), the cell counts, Figures 2, S3 and S4 (remapping, PV similarity, decoding, ramping cells), Figures 3, S5 and S6 (selectivity index, path equivalence, manifolds and distances) and Figures 4 and S7 (CCGP, geometric null model, the 35 dichotomies).

**Details left open, with the readings named:**
- **Rate-map smoothing (garbled in the text, "s = σ cm").** Main reading 8 cm, the σ of the 2D maps; 4 and 2 cm are run as variants.
- **Decoding windows.** The Methods say a 200 ms window "with 50 ms overlap" (a 150 ms step); the code steps 50 ms and keeps only theta periods, which is the variant.
- **Figure 2F, which trial is "−1".** Either the last N trial, or the code's 10th N trial.
- **Figure 2E shuffles.** How many, and what the Wilcoxon test pairs: one shuffle per bin, or the median of 100.
- **Rate overlap (Figure S3A).** Mean of the rate map, or spikes over time.
- **Figure S3D.** The novel trials are N then N′, N alone, or N′ alone.
- **Ramping denominator (Figure S4).** All sessions pooled, or N′ alone.
- **Selectivity index (Figure 3D).** Sessions pooled, N′ alone, or F alone. Figure 3E and S5E: whether "novel" means N′ or N.
- **Figure S5F.** Signed or absolute selectivity index.
- **Manifold cells.** The Methods require spatially tuned cells; the code applies no tuning filter. The expected counts of 98 CA1 and 171 PFC cells decide between them.
- **Distance alignment.**
  - Figure 3H: the Methods are silent; I followed the code, which aligns CA1 by location and PFC by phase.
  - Figure 3I: the Methods and the code disagree. The Methods' pairing is the main reading and the code's is a variant.
  - UMAP bins: the Methods say 1 cm, the code uses normalized length (variant).
- **Geometric null model (Figure S7).** No code; the axes are permuted either in UMAP space or in neuron space.
- **Interpretations I made, not set by the paper.**
  - "Most" dichotomies (Figure S7D) is read as more than half.
  - Which bins count as the reward wells (Figure S4D).
  - The Fisher z test for comparing two correlations (Figure S5E).
  - For the manifold shapes (Figure 3F, 3G), the paper gives no measure. That claim takes its outcome from the distance claims for Figure 3H and 3I.

**Missing that claims need:**
- **Data likely not in the dandiset.** The de novo learning sessions (Figure 1B, 1C, S1B) and the second group of three rats run F-N-F′-N′ (Figure S1C) are probably absent; the dandiset holds only the N, F and N′ epochs. The paper says its raw data are on Brandeis servers, available on request.
- **Absent from the repository.** The code that computes the rate maps, the saved UMAP templates, and code for Figures S3A, S4, the 2E shuffles and the S7 null model.
- **Unlabelled post hoc p-values.** Several legends (Figures 1C, 2E, S3A, S4C, S5D, S6, S7B) give p-values without saying which pair each belongs to.

## End of run

36 turns, 8 minutes, result: success.
