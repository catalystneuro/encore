# 000959 · claims · run 39869052814

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cat docs/protocol.md; ls claims/001453/ claims/000959/ paper/; ls claims | head
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -n '/^## Reader/,/^## Author/p' docs/protocol.md; ls claims/001453/ claims/000959/ paper/
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cat claims/001453/*.yaml | head -150; wc -l paper/*.txt; head -40 paper/*.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1016-j.neuron.2024.05.004.txt",
 "offset": 40,
 "limit": 600
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -n '/^## Author/,$p' docs/protocol.md | grep -n -i -A3 "schema\|kind:" | head -60; ls tools; ls claims | wc -l
```

```
52:     or subjects, a claim of its own (`kind: link`) tests the link. Link
53-     claims are the registry's checks, not findings of the paper, so the
54-     author adds them to the claims file; they are the only claims the
55-     author writes. A link claim says how
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
runner
[... 5 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "paper/10.1016-j.neuron.2024.05.004.txt",
 "offset": 40,
 "limit": 300
}
```

Result: not kept, because it reads the paper's text.

**Agent**

Lines are long; reading in smaller chunks.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1016-j.neuron.2024.05.004.txt",
 "offset": 40,
 "limit": 150
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1016-j.neuron.2024.05.004.txt",
 "offset": 189,
 "limit": 60
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd paper; grep -n -i "supplement\|^Figure S\|Supplementary Results\|Table S1" 10.1016-j.neuron.2024.05.004.txt | sed -n '1,80p' | cut -c1-200
```

```
5:Extracted: as fetched; with 1 supplement file(s) from PubMed Central, downloaded in a browser (PMC11309918), PDFs extracted with PyMuPDF (dehyphenated, NFKC), Word files with textutil
55:Two unique pairs of rhesus macaques (M1: stimulated monkey or ‘self’, monkeys L and T; M2: partner monkey or ‘other’, monkey E) engaged in spontaneous face-to-face social gaze interaction8,23 while
61:(A) Experimental paradigm for studying the functional role of the primate prefrontal cortex in naturalistic social gaze interaction. Left, live social gaze condition where each real-time microstimu
69:To address this question, we first constructed a fixation density map for each trial considering all fixations during the analyzed post-gaze epoch (within 1.5 sec after the onset of a microstimulat
79:Crucially, these stimulation effects of OFC were exclusively observed in the live social gaze condition (i.e., microstimulations triggered by looking at partner’s Eyes) and not in the non-social ga
174:All animals received a surgically implanted headpost (Grey Matter Research) for restraining their head movement. A second surgery was performed on the two M1 animals to implant a custom chamber (R
219:Supplementary Material
221:NIHMS1994226-supplement-1.pdf (2.9MB, pdf)
371:This section collects any data citations, data availability statements, or supplementary materials included in this article.
373:Supplementary Materials
375:NIHMS1994226-supplement-1.pdf (2.9MB, pdf)
398:Supplementary Material
607:##### Supplement: NIHMS1994226-supplement-1.pdf
610:Supplemental Information  
612:This Supplemental Information contains: 
613:Supplemental Table, Title, and Legend 
614:Supplemental Figures, Titles, and Legends 
621:Supplemental Table, Title, and Legend 
1134:Table S1. Montreal Neurological Institute (MNI) coordinates of microstimulation sites (Related to 
1144:Supplemental Figures, Titles, and Legends 
[... 4 more lines not kept]
```

**Agent calls Bash**

```bash
cd paper; sed -n '1134,1273p' 10.1016-j.neuron.2024.05.004.txt | grep -v '^\s*$' | awk 'length>3' | head -200
```

```
Table S1. Montreal Neurological Institute (MNI) coordinates of microstimulation sites (Related to 
Fig. 1). This table lists the MNI coordinates [1-3] of individual microstimulation sites in the orbitofrontal 
cortex (OFC), the dorsomedial prefrontal cortex (dmPFC), and the gyrus of anterior cingulate cortex 
(ACCg) from monkey L and monkey T in the main Eyes stimulation experiments and additional 
microstimulation sites from monkey T in the Mouth stimulation control experiments. R: right; A: anterior; 
S: superior.   
=== page 3 ===
Supplemental Figures, Titles, and Legends 
Figure S1. Experimental setup, additional analyses for the non-social control condition, and 
naturalistic gaze behaviors (Related to Fig. 1). (A) Pictures of the experimental setup where a pair of 
=== page 4 ===
monkeys would sit in primate chairs facing each other for live social gaze interaction (animals not shown) 
[4]. The two middle monitors could be lowered down or raised up by using a remote hydraulic system so 
that the monkeys were able to or not able to see each other. When the middle monitors were lowered down, 
the stimulated monkey had full visual access to the partner monkey’s head (or the mini monitor presenting 
RDM stimulus that completely blocked partner monkey’s face), the primate chair, and the white wall in the 
background. We tried to make the environment as simple as possible to minimize visual distraction. (B) 
Diagram of the closed-loop microstimulation design for the non-social control condition. To avoid 
overstimulation of brain tissue, any two consecutive trials (including both microstimulations and shams) 
had to be at least 5 sec apart; for every four trials, two microstimulations and two shams were randomly 
[... 75 more lines not kept]
```

**Agent calls Bash**

```bash
cd paper; sed -n '600,640p' 10.1016-j.neuron.2024.05.004.txt; grep -n "=== page" 10.1016-j.neuron.2024.05.004.txt; grep -n -i "results" 10.1016-j.neuron.2024.05.004.txt | cut -c1-120; sed -n '249,370p' 10.1016-j.neuron.2024.05.004.txt | cut -c1-200 | head -60
```

```
10.3758/BF03195489

10.16910/jemr.7.1.1

10.1167/14.2.18

##### Supplement: NIHMS1994226-supplement-1.pdf

=== page 1 ===
Supplemental Information  
 
This Supplemental Information contains: 
Supplemental Table, Title, and Legend 
Supplemental Figures, Titles, and Legends 
 
 

=== page 2 ===
 
2 
[... 100 more lines not kept]
```

**Agent calls Bash**

```bash
cd paper; sed -n '368,410p' 10.1016-j.neuron.2024.05.004.txt | cut -c1-300
```

```
91.Otero-Millan J, Castro JLA, Macknik SL, and Martinez-Conde S (2014). Unsupervised clustering method to detect microsaccades. Journal of Vision 14, 18–18. 10.1167/14.2.18. [DOI] [PubMed] [Google Scholar]
Associated Data

This section collects any data citations, data availability statements, or supplementary materials included in this article.

Supplementary Materials
1
NIHMS1994226-supplement-1.pdf (2.9MB, pdf)
Data Availability Statement

Behavioral and neural data presented in this paper are available through the DANDI archive (https://dandiarchive.org/dandiset/000959) and the main analysis codes are available at https://github.com/changlabneuro/microstim-ofc-social-attention.

ACTIONS
View on publisher site
PDF (2.7 MB)
Cite
Collections
Permalink
RESOURCES
Similar articles
[... 23 more lines not kept]
```

**Agent**

I've read the paper (PMC author manuscript plus supplement). Now the linked code.

**Agent calls Bash**

```bash
cd $TMPDIR && git clone -q https://github.com/changlabneuro/microstim-ofc-social-attention.git code && cd code && git log -1 --format='%H %ci' && find . -type f -not -path './.git/*' | head -100 && find . -type f -not -path './.git/*' | wc -l; cat README* 2>/dev/null | head -60
```

```
cc0bf994fc4879f30a620521b6c235ebfb2412a7 2024-10-15 17:55:53 -0400
./stim/save_spike_ts.m
./stim/plot_rdm_value.m
./stim/plot_pupil.m
./stim/plot_plx_online_sorted.m
./stim/parse_siqi_xls.m
./stim/overlay_rois.m
./stim/model_gaze_data.m
./stim/linearize_gaze_data.m
./stim/get_spike_ts.m
./stim/get_mean_gaze_position_before_stim.m
./stim/get_day_labels.m
./stim/find_outlier_mua_sessions.m
./stim/debug_mua.m
./stim/S5_Pupil_Size.m
./script/wb_channel_str.m
./script/to_mua_tbl.m
./script/signal_to_mua.m
./script/save_new_mua.m
./script/run_saccade_detection.m
[... 81 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/code/"Scripts for social attention"; wc -l */*.m */*/*.m */*/*/*.m 2>/dev/null | tail -1; cat "Spatial dimension/S1_Gaze_Results_Combined.m"
```

```
14383 total
%% Put information together for each trial (four categories: sham_sham, sham_stim, stim_sham, and stim_stim; plus two general categories: current_sham and current_stim)

fieldname=fieldnames(GazeMatrices);

for k=1:size(fieldname,1)
    field_id=char(fieldname(k));
    field_run=fieldnames(GazeMatrices.(field_id));
    
    for l=1:size(field_run,1)
        run_id=char(field_run(l));
        field_stim=fieldnames(GazeMatrices.(field_id).(run_id));
        
        GazeResults.(field_id).(run_id).roi_m1_eyes=GazeMatrices.(field_id).(run_id).roi_m1_eyes;
        GazeResults.(field_id).(run_id).roi_m2_eyes=GazeMatrices.(field_id).(run_id).roi_m2_eyes;
        GazeResults.(field_id).(run_id).roi_m1_mouth=GazeMatrices.(field_id).(run_id).roi_m1_mouth;
        GazeResults.(field_id).(run_id).roi_m2_mouth=GazeMatrices.(field_id).(run_id).roi_m2_mouth;
        GazeResults.(field_id).(run_id).roi_m1_face=GazeMatrices.(field_id).(run_id).roi_m1_face;
        GazeResults.(field_id).(run_id).roi_m2_face=GazeMatrices.(field_id).(run_id).roi_m2_face;
        
[... 277 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/code/"Scripts for social attention"; wc -l */*.m */*/*.m */*/*/*.m | sort -n | tail -50; sed -n '1,200p' "Spatial dimension/S2_Gaze_Stats_Basic_Behaviors_Combined.m" | grep -v '^\s*$' | head -150
```

```
wc: '*/*/*/*.m': No such file or directory
    20 Get data/S2_Gaze_Data_Combined.m
    52 Get data/S2_Dot_Data_Combined.m
    81 Overall gaze behavior and number of stims/S2_Dot_ROI_number_duration_Combined.m
    93 Inter-individual dynamics/Causal Decomposition Index/S1_Gaze_Binned_Distance_Combined.m
    93 Overall gaze behavior and number of stims/S2_Gaze_ROI_number_duration_Combined.m
   138 Saccade kinematics/S1_Gaze_Saccade_Control_Tarantino.m
   139 Saccade kinematics/S1_Gaze_Saccade_Control_Lynch.m
   145 Saccade kinematics/S3_Gaze_Saccade_Control_Combined.m
   187 Temporal dimension/Inter-looking interval/S1_Dot_M1_Latency_Combined.m
   187 Temporal dimension/Inter-looking interval/S1_Gaze_M1_Latency_Combined.m
   202 Heatmap/S1_Gaze_Fixation_Heatmap.m
   208 Overall gaze behavior and number of stims/S3_Stats_ROI_number_duration_final.m
   213 Saccade kinematics/S5_Pupil_Size.m
   223 Saccade kinematics/S2_Gaze_Saccade_Data_Combined.m
   237 Temporal dimension/Inter-looking interval/S2_Dot_M1_Latency_Stats_Combined.m
   237 Temporal dimension/Inter-looking interval/S2_Gaze_M1_Latency_Stats_Combined.m
   238 Spatial dimension/S1_Dot_Results_Combined.m
   245 Inter-individual dynamics/Causal Decomposition Index/S3_Gaze_CDI.m
   251 Inter-individual dynamics/Epoch/S1_Gaze_Time_Epoch.m
[... 176 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/code/"Scripts for social attention"; grep -n -i "1500\|1\.5\|5000\|ipsi\b\|contra =\|distance_to_eyes\s*=\|pdist\|sqrt\|deg\|pixel\|cm\|flip\|> *0\b\|< *0\b" "Get data/S3_Basic_Gaze_Matrices_Combined.m" | head -60
```

```
7: GazeMatrices = basic_gaze_matrices( GazeData, 0, 1.5 );
90:                fixation_m1_eye_ipsi_idx=find(GazeData.(field_id).(run_id).m1_eye.Var1(:,11)>=stim_ts(nstim)+look_back & GazeData.(field_id).(run_id).m1_eye.Var1(:,11)<stim_ts(nstim)+look_ahead & GazeData.(field_id).(run_id).m1_eye.Var2=='ipsi');
173:                fixation_m1_mouth_ipsi_idx=find(GazeData.(field_id).(run_id).m1_mouth.Var1(:,11)>=stim_ts(nstim)+look_back & GazeData.(field_id).(run_id).m1_mouth.Var1(:,11)<stim_ts(nstim)+look_ahead & GazeData.(field_id).(run_id).m1_mouth.Var2=='ipsi');
256:                fixation_m1_nenmface_ipsi_idx=find(GazeData.(field_id).(run_id).m1_nenmface.Var1(:,11)>=stim_ts(nstim)+look_back & GazeData.(field_id).(run_id).m1_nenmface.Var1(:,11)<stim_ts(nstim)+look_ahead & GazeData.(field_id).(run_id).m1_nenmface.Var2=='ipsi');
339:                fixation_m1_everywhere_ipsi_idx=find(GazeData.(field_id).(run_id).m1_everywhere.Var1(:,11)>=stim_ts(nstim)+look_back & GazeData.(field_id).(run_id).m1_everywhere.Var1(:,11)<stim_ts(nstim)+look_ahead & GazeData.(field_id).(run_id).m1_everywhere.Var2=='ipsi');
422:                fixation_m1_neface_ipsi_idx=find(GazeData.(field_id).(run_id).m1_neface.Var1(:,11)>=stim_ts(nstim)+look_back & GazeData.(field_id).(run_id).m1_neface.Var1(:,11)<stim_ts(nstim)+look_ahead & GazeData.(field_id).(run_id).m1_neface.Var2=='ipsi');
505:                fixation_m1_wholeface_ipsi_idx=find(GazeData.(field_id).(run_id).m1_wholeface.Var1(:,11)>=stim_ts(nstim)+look_back & GazeData.(field_id).(run_id).m1_wholeface.Var1(:,11)<stim_ts(nstim)+look_ahead & GazeData.(field_id).(run_id).m1_wholeface.Var2=='ipsi');
574:                    GazeMatrices.(field_id).(run_id).(stim_id).m1_distance_to_eyes=NaN;
590:                    GazeMatrices.(field_id).(run_id).(stim_id).m1_distance_to_eyes(1,n_m1_all)=sqrt((GazeMatrices.(field_id).(run_id).(stim_id).mean_x_m1(1,n_m1_all)-GazeMatrices.(field_id).(run_id).center_roi_m1_eyes(1)).^2+(GazeMatrices.(field_id
[... 41 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/code/"Scripts for social attention"; sed -n '1,90p' "Get data/S3_Basic_Gaze_Matrices_Combined.m" | grep -v '^\s*$' | cut -c1-250
```

```
%% Upload Gaze_Data_Combined_Updated.mat
%% Specify time window
% look_back is negative and look_ahead is positive
 GazeMatrices = basic_gaze_matrices( GazeData, 0, 1.5 );
 % GazeMatrices = basic_gaze_matrices( GazeData, 0, 3 );
save('Gaze_Matrices_Combined_0_15_updated.mat','GazeMatrices','-v7.3')
%save('Gaze_Matrices_Combined_0_3.mat','GazeMatrices','-v7.3')
%% Calculate the basic gaze metrices within [look_back, look_ahead] aligned to each stim/sham (exclude stim/sham that happens within 5sec from the end of a run)
% total number, average duration, and total duration of different events 
% pupil size and average distance during different events
function GazeMatrices = basic_gaze_matrices(GazeData, look_back, look_ahead) 
fieldname=fieldnames(GazeData);
    for k=1:size(fieldname,1)
        field_id=char(fieldname(k));    
        field_run=fieldnames(GazeData.(field_id));
        for l=1:size(field_run,1)
            run_id=char(field_run(l));
            % get ROI info
            GazeMatrices.(field_id).(run_id).roi_m1_eyes=GazeData.(field_id).(run_id).roi_m1_eyes;
            GazeMatrices.(field_id).(run_id).roi_m2_eyes=GazeData.(field_id).(run_id).roi_m2_eyes;
[... 47 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/code/"Scripts for social attention"; grep -v '^\s*$' "Get data/S1_Get_data_gaze_Lynch.m" | cut -c1-250 | head -200
```

```
%% Load files and create "Gaze" variable
files = dir('*.mat');
filesname = {files.name};
sortedfilesname = natsort(filesname);
characterfile=char(sortedfilesname);
% stringfile is the file names in right order: 1, 2, ... 9, 10, 11
stringfile=deblank(string(characterfile));
% datafile is the first 8 digit of the file names (Data)
datefile=string(characterfile(:,1:8));
% date is distinct experiment days
date=unique(datefile);
for i=1:length(date)
    string_binary=strfind(stringfile,date(i));
    string=cellfun(@(a)~isempty(a) && a>0,string_binary);
    stringindex=find(string==1);
    for j=stringindex(1):stringindex(end)
        filename=cellstr(extractBefore(stringfile(j),'.mat'));
        filename2=stringfile(j);
        day_char=char(strcat('data_',date(i)));
        run_char=char(strcat('run_',num2str(j)));
[... 181 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/code; diff "Scripts for social attention/Get data/S1_Get_data_gaze_Lynch.m" "Scripts for social attention/Get data/S1_Get_data_gaze_Tarantino.m"; grep -rn -i "deg\b\|degree\|px\|pix\|visual angle\|atan" --include=*.m . | cut -c1-220 | head -40
```

```
30c30
<         Gaze.(day_char).(run_char).events = load(append('/Volumes/Brains/BRAINS Microstimulation/Data/intermediates/raw_events_Lynch_gaze/',filename2)).var;
---
>         Gaze.(day_char).(run_char).events = load(append('/Volumes/Brains/BRAINS Microstimulation/Data/intermediates/raw_events_Tarantino_gaze_eyes/',filename2)).var;
50c50
< save('Gaze_Lynch.mat','Gaze','-v7.3')
---
> save('Gaze_Tarantino.mat','Gaze','-v7.3')
76c76
<         % ROI info for eyes (m1 roi is m2's eyes from m1's perspective)
---
>         % ROI info for eyes
148,149c148,149
<         % Label contra- or ipsi- lateral for each event (Lynch's chamber is
<         % on the left side of the head)
---
>         % Label contra- or ipsi- lateral for each event (Tarantino's chamber is
>         % on the right side of the head)
157,158c157,158
<             
[... 65 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/code/"Scripts for social attention"; grep -n -i "px2deg\|/ *[0-9][0-9]\.\|\*[0-9.]*\b.*dist\|ylabel" "Spatial dimension/S3_Plotting_Basic_Behaviors_Combined.m" "Spatial dimension/S3_Plotting_Basic_Behaviors_Combined_Hemisphere.m" | head -20; grep -rn "px2deg" ../ | grep -i "function" ; grep -rn "bfw\." --include=*.m .. | grep -v px2deg | cut -c1-150 | head
```

```
../stim/plot_pupil.m:98:  inds = non_nan(bfw.find_nearest(curr_t(non_nan), ta));
../stim/get_mean_gaze_position_before_stim.m:4:ps = bfw.matched_files( ...
../stim/S5_Pupil_Size.m:98:  inds = non_nan(bfw.find_nearest(curr_t(non_nan), ta));
../script/save_new_mua.m:41:  ps = bfw.matched_files( ...
../script/save_new_mua.m:202:  %   [psth, psth_t] = bfw.event_psth( evts, {kept_ts}, evt_I, spk_I, -0.1, 5, 0.1 );
../script/save_new_mua.m:203:    [psth, psth_t] = bfw.event_psth( evts, {kept_ts}, evt_I, spk_I, psth_lb, psth_la, bin_w );
../script/revisit_mua.m:111:% [mua1_psth, psth_t] = bfw.trial_psth( mua1_t(:), align_ts(:), lb, la, bw );
../script/revisit_mua.m:114:% mua2_psth = bfw.trial_psth( mua2_t(:), align_ts(:), lb, la, bw );
../script/plot_stim_psd.m:4:[psd, psd_labs, psd_f, psd_t] = bfw.load_time_frequency_measure(psd_mats ...
../script/plot_new_mua.m:384:ps = bfw.matched_files( ...
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/code/"Scripts for social attention"; grep -n -i "distance\|label\|36\|1024" "Spatial dimension/S3_Plotting_Basic_Behaviors_Combined_Hemisphere.m" | head -30
```

```
55:Gaze_variables_distance={'m1_distance_to_eyes','m1_distance_to_mouth','m1_distance_to_face'};
58:n_m1=1:length(Gaze_variables_distance);
63:    gaze_variables=char(Gaze_variables_distance(ngaze));
91:            line_labels=cell( size(line_hs));
99:                line_labels{m} = OFC_day.(monkey_id){m};
101:            legend( vertcat(line_hs{:}), line_labels, 'Location', 'westoutside', 'FontSize',7);
106:            clear X Y m colorInd line_hs line_labels
118:            line_labels=cell( size(line_hs));
126:                line_labels{m} = ACCg_day.(monkey_id){m};
128:            legend( vertcat(line_hs{:}), line_labels, 'Location', 'westoutside', 'FontSize',7);
133:            clear X Y m colorInd line_hs line_labels
145:            line_labels=cell( size(line_hs));
153:                line_labels{m} = dmPFC_day.(monkey_id){m};
155:            legend( vertcat(line_hs{:}), line_labels, 'Location', 'westoutside', 'FontSize',7);
160:            clear X Y m colorInd line_hs line_labels
180:Dot_variables_distance={'m1_distance_to_eyes','m1_distance_to_mouth','m1_distance_to_face'};
183:n_m1=1:length(Dot_variables_distance);
188:    gaze_variables=char(Dot_variables_distance(ngaze));
216:            line_labels=cell( size(line_hs));
224:                line_labels{m} = OFC_day.(monkey_id){m};
[... 11 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/code/"Scripts for social attention"; sed -n '200,424p' "Spatial dimension/S2_Gaze_Stats_Basic_Behaviors_Combined.m" | grep -v '^\s*$' | grep -v "ACCg\|dmPFC" | cut -c1-300 | head -80
```

```
else
            end
            % OFC 
            if isequal(sum(~isnan(Sham_Sham.OFC.(gaze_variables).(monkey_id).(type_id)) & ~isnan(Stim_Sham.OFC.(gaze_variables).(monkey_id).(type_id))),0)
            Stats_median.p.OFC.current_sham.(gaze_variables).(monkey_id).(type_id) = NaN;
            Stats_median.h.OFC.current_sham.(gaze_variables).(monkey_id).(type_id) = NaN;
            Stats_mean.p.OFC.current_sham.(gaze_variables).(monkey_id).(type_id) = NaN;
            Stats_mean.h.OFC.current_sham.(gaze_variables).(monkey_id).(type_id) = NaN;
            else
            [Stats_median.p.OFC.current_sham.(gaze_variables).(monkey_id).(type_id), Stats_median.h.OFC.current_sham.(gaze_variables).(monkey_id).(type_id)] = signrank(Sham_Sham.OFC.(gaze_variables).(monkey_id).(type_id), Stim_Sham.OFC.(gaze_variables).(monkey_id).(type_id));
            [Stats_mean.h.OFC.current_sham.(gaze_variables).(monkey_id).(type_id), Stats_mean.p.OFC.current_sham.(gaze_variables).(monkey_id).(type_id)] = ttest(Sham_Sham.OFC.(gaze_variables).(monkey_id).(type_id), Stim_Sham.OFC.(gaze_variables).(monkey_id).(type_id));
            end
            if isequal(sum(~isnan(Sham_Stim.OFC.(gaze_variables).(monkey_id).(type_id)) & ~isnan(Stim_Stim.OFC.(gaze_variables).(monkey_id).(type_id))),0)
            Stats_median.p.OFC.current_stim.(gaze_variables).(monkey_id).(type_id) = NaN;
            Stats_median.h.OFC.current_stim.(gaze_variables).(monkey_id).(type_id) = NaN;
            Stats_mean.p.OFC.current_stim.(gaze_variables).(monkey_id).(type_id) = NaN;
            Stats_mean.h.OFC.current_stim.(gaze_variables).(monkey_id).(type_id) = NaN;
            else
            [Stats_median.p.OFC.current_stim.(gaze_variables).(monkey_id).(type_id), Stats_median.h.OFC.current_stim.(gaze_variables).(monkey_id).(type_id)] = signrank(Sham_Stim.OFC.(gaze_variables).(monkey_id).(type_id), Stim_Stim.OFC.(gaze_variables).(monkey_id).(type_id));
            [Stats_mean.h.OFC.current_stim.(gaze_variables).(mon
[... 61 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/code/"Scripts for social attention"; grep -rn "signrank\|ranksum\|permut\|randperm\|1000" "Spatial dimension/S3_Plotting_Basic_Behaviors_Combined_Hemisphere.m" "Spatial dimension/S3_Plotting_Basic_Behaviors_Combined.m" | cut -c1-300 | head -20
```

```
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/code/"Scripts for social attention/Temporal dimension"; grep -v '^\s*$' "Inter-looking interval/S1_Gaze_M1_Latency_Combined.m" | cut -c1-260
```

```
%% Load Gaze_Data_Combined.mat 
% Get m1 events
fieldname=fieldnames(GazeData);
time_window=5; %sec
for k=1:size(fieldname,1)
    field_id=char(fieldname(k));    
    field_run=fieldnames(GazeData.(field_id));
    for l=1:size(field_run,1)
        run_id=char(field_run(l));
        m1_behavior.(field_id).(run_id).stim_ts=[];
        m1_behavior.(field_id).(run_id).all_stim_labels=[];
        % column 7 is m1 start index; column 8 is m1 end index
        % column 9 is m2 start index; column 10 is m2 end index
        % column 11 is m1 start time; column 12 is m1 end time
        % column 13 is m2 start time; column 14 is m2 end time
        [sorted_start_time_eyes,sorted_order_eyes]=sort(vertcat(GazeData.(field_id).(run_id).m1_eye.Var1(:,7),GazeData.(field_id).(run_id).mutual_eye.Var1(:,7)));
        [sorted_start_time_mouth,sorted_order_mouth]=sort(vertcat(GazeData.(field_id).(run_id).m1_mouth.Var1(:,7),GazeData.(field_id).(run_id).mutual_mouth.Var1(:,7)));
        [sorted_start_time_wholeface,sorted_order_wholeface]=sort(vertcat(GazeData.(field_id).(run_id).m1_wholeface.Var1(:,7),GazeData.(field_id).(run_id).mutual_wholeface.Var1(:,7)));
        for nstim=1:length(GazeData.(field_id).(run_id).stim_ts)        
            stim_id=char(strcat('stim_',num2str(nstim)));
[... 101 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/code/"Scripts for social attention/Temporal dimension"; grep -v '^\s*$' "Reciprocation latency/S1_Gaze_ITI_Combined.m" | cut -c1-260 | sed -n '1,140p'
```

```
%% Load Gaze_Data_Combined.mat 
% Combine m1 whole face events and m2 whole face events and sort based on
% start time
fieldname=fieldnames(GazeData);
for k=1:size(fieldname,1)
    field_id=char(fieldname(k));    
    field_run=fieldnames(GazeData.(field_id));
    for l=1:size(field_run,1)
        run_id=char(field_run(l));
        sorted_events.whole_face.(field_id).(run_id).stim_ts=GazeData.(field_id).(run_id).stim_ts;
        sorted_events.whole_face.(field_id).(run_id).all_stim_labels=GazeData.(field_id).(run_id).all_stim_labels;
        sorted_events.whole_face.(field_id).(run_id).t=GazeData.(field_id).(run_id).t;
        sorted_events.all_face.(field_id).(run_id).stim_ts=GazeData.(field_id).(run_id).stim_ts;
        sorted_events.all_face.(field_id).(run_id).all_stim_labels=GazeData.(field_id).(run_id).all_stim_labels;
        sorted_events.all_face.(field_id).(run_id).t=GazeData.(field_id).(run_id).t;
        % column 7 is m1 start index; column 8 is m1 end index
        % column 9 is m2 start index; column 10 is m2 end index
        % column 11 is m1 start time; column 12 is m1 end time
        % column 13 is m2 start time; column 14 is m2 end time
        % combine m1 whole face and m2 whole face
[... 121 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/code/"Scripts for social attention/Temporal dimension"; grep -v '^\s*$' "Reciprocation latency/S1_Gaze_ITI_Combined.m" | cut -c1-260 | sed -n '140,240p'; grep -n "iti\b\|all_face\|whole_face\|ranksum\|signrank\|nstim=\|nstim =" "Reciprocation latency/S2_Gaze_ITI_Stats_Combined.m" "Reciprocation latency/S3_Gaze_ITI_Across_Trials.m" | cut -c1-200 | head -40
```

```
if m2_start_idx_whole_face(n_m2_whole_face)+m2_length_whole_face(n_m2_whole_face)<=length(contains_m2_whole_face)  
                            iti.whole_face.(field_id).(run_id).(stim_id).frequency=[iti.whole_face.(field_id).(run_id).(stim_id).frequency m2_length_whole_face(n_m2_whole_face)];
                            if iti_events.whole_face.(field_id).(run_id).(stim_id).events(m2_start_idx_whole_face(n_m2_whole_face)+m2_length_whole_face(n_m2_whole_face)-1,2)<=iti_events.whole_face.(field_id).(run_id).(stim_id).events(m2_start_idx_whole_face(n_
                                iti.whole_face.(field_id).(run_id).(stim_id).duration=[iti.whole_face.(field_id).(run_id).(stim_id).duration...
                                sum(iti_events.whole_face.(field_id).(run_id).(stim_id).events(m2_start_idx_whole_face(n_m2_whole_face):m2_start_idx_whole_face(n_m2_whole_face)+m2_length_whole_face(n_m2_whole_face)-1,2)-iti_events.whole_face.(field_id).(run_id
                            else
                                iti.whole_face.(field_id).(run_id).(stim_id).duration=[iti.whole_face.(field_id).(run_id).(stim_id).duration...
                                sum(iti_events.whole_face.(field_id).(run_id).(stim_id).events(m2_start_idx_whole_face(n_m2_whole_face):m2_start_idx_whole_face(n_m2_whole_face)+m2_length_whole_face(n_m2_whole_face)-1,2)-iti_events.whole_face.(field_id).(run_id
                                +iti_events.whole_face.(field_id).(run_id).(stim_id).events(m2_start_idx_whole_face(n_m2_whole_face)+m2_length_whole_face(n_m2_whole_face),1)-iti_events.whole_face.(field_id).(run_id).(stim_id).events(m2_start_idx_whole_face(n_m
                            end
                                iti.whole_face.(field_id).(run_id).(stim_id).iti=[iti.whole_face.(field_id).(run_id).(stim_id).iti...
                                iti_events.whole_face.(field_id).(run_id).(stim_id).events(m2_start_idx_whole_face(n_m2_whole_face)+m2_length_whole_face(n_m2_whole_face),1)-i
[... 118 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/code/"Scripts for social attention/Temporal dimension"; sed -n '56,105p' "Reciprocation latency/S3_Gaze_ITI_Across_Trials.m" | cut -c1-300; sed -n '230,280p' "Reciprocation latency/S1_Gaze_ITI_Combined.m" | grep -n "mean\|average" | cut -c1-250 | head
```

```
for ngaze=1:length(Gaze_variables)

     gaze_variables=char(Gaze_variables(ngaze));
     monkey_names={'All', 'Lynch', 'Tarantino'};
        
    for nmonkey=1:3
        monkey_id=char(monkey_names(nmonkey));
    
        Current_Sham.(ROI_id).OFC.(gaze_variables).(monkey_id).mean=[];
        Current_Stim.(ROI_id).OFC.(gaze_variables).(monkey_id).mean=[];
       
        for nOFC=1:length(OFC_day.(monkey_id))
        
            field_id=char(strcat('data_',OFC_day.(monkey_id)(nOFC)));
        
            Current_Sham.(ROI_id).OFC.(gaze_variables).(monkey_id).mean=[Current_Sham.(ROI_id).OFC.(gaze_variables).(monkey_id).mean ITI_Day.(ROI_id).(field_id).current_sham.(gaze_variables)];
            Current_Stim.(ROI_id).OFC.(gaze_variables).(monkey_id).mean=[Current_Stim.(ROI_id).OFC.(gaze_variables).(monkey_id).mean ITI_Day.(ROI_id).(field_id).current_stim.(gaze_variables)];

        end

[... 31 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/code/"Scripts for social attention/Temporal dimension"; grep -n "average_iti=\[" "Reciprocation latency/S1_Gaze_ITI_Combined.m" | cut -c1-300 | head -3; grep -n "ranksum\|signrank" "Inter-looking interval/"*.m | cut -c1-200 | head; grep -n "m1_latency_face" "Inter-looking interval/S3_Gaze_M1_Latency_Across_Trials.m" | head -3
```

```
334:                ITIResults.(ROI_id).(field_id).(run_id).(stim_label{i}).average_iti=[];
362:                    ITIResults.(ROI_id).(field_id).(run_id).(label).average_iti=[ITIResults.(ROI_id).(field_id).(run_id).(label).average_iti mean(iti.(ROI_id).(field_id).(run_id).(stim_id).iti,'omitnan')];
407:            ITI_Day.(ROI_id).(field_id).(stim_label{i}).average_iti=[];
Inter-looking interval/S2_Dot_M1_Latency_Stats_Combined.m:100:        [Stats_mean.p.OFC.current.(gaze_variables).(monkey_id).mean,Stats_mean.h.OFC.current.(gaze_variables).(monkey_id).mean] = signrank
Inter-looking interval/S2_Dot_M1_Latency_Stats_Combined.m:108:        [Stats_mean.p.ACCg.current.(gaze_variables).(monkey_id).mean,Stats_mean.h.ACCg.current.(gaze_variables).(monkey_id).mean] = signra
Inter-looking interval/S2_Dot_M1_Latency_Stats_Combined.m:116:        [Stats_mean.p.dmPFC.current.(gaze_variables).(monkey_id).mean,Stats_mean.h.dmPFC.current.(gaze_variables).(monkey_id).mean] = sign
Inter-looking interval/S2_Gaze_M1_Latency_Stats_Combined.m:100:        [Stats_mean.p.OFC.current.(gaze_variables).(monkey_id).mean,Stats_mean.h.OFC.current.(gaze_variables).(monkey_id).mean] = signran
Inter-looking interval/S2_Gaze_M1_Latency_Stats_Combined.m:108:        [Stats_mean.p.ACCg.current.(gaze_variables).(monkey_id).mean,Stats_mean.h.ACCg.current.(gaze_variables).(monkey_id).mean] = signr
Inter-looking interval/S2_Gaze_M1_Latency_Stats_Combined.m:116:        [Stats_mean.p.dmPFC.current.(gaze_variables).(monkey_id).mean,Stats_mean.h.dmPFC.current.(gaze_variables).(monkey_id).mean] = sig
Inter-looking interval/S3_Gaze_M1_Latency_Across_Trials.m:99:        [Stats.p.OFC.current.(gaze_variables).(monkey_id), Stats.h.OFC.current.(gaze_variables).(monkey_id)] = ranksum(Current_Sham.(gaze_v
Inter-looking interval/S3_Gaze_M1_Latency_Across_Trials.m:100:        [Stats.p.dmPFC.current.(gaze_variables).(monkey_id), Stats.h.dmPFC.current.(gaze_variables).(monkey_id)] = ranksum(Current_Sham.(g
Inter-looking 
[... 3 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/code/"Scripts for social attention/Temporal dimension"; sed -n '60,75p;98,101p' "Inter-looking interval/S2_Gaze_M1_Latency_Stats_Combined.m" | cut -c1-250; diff "Inter-looking interval/S1_Gaze_M1_Latency_Combined.m" "Inter-looking interval/S1_Dot_M1_Latency_Combined.m"
```

```
Current_Stim.OFC.(gaze_variables).(monkey_id).mean=[];
    
        for nOFC=1:length(OFC_day.(monkey_id))
    
            field_id=char(strcat('data_',OFC_day.(monkey_id)(nOFC)));
    
            Current_Sham.OFC.(gaze_variables).(monkey_id).mean=[Current_Sham.OFC.(gaze_variables).(monkey_id).mean mean(m1_behavior_day.(field_id).current_sham.(gaze_variables),'omitnan')];
            Current_Stim.OFC.(gaze_variables).(monkey_id).mean=[Current_Stim.OFC.(gaze_variables).(monkey_id).mean mean(m1_behavior_day.(field_id).current_stim.(gaze_variables),'omitnan')];
            
        end

        Current_Sham.ACCg.(gaze_variables).(monkey_id).mean=[];
        Current_Stim.ACCg.(gaze_variables).(monkey_id).mean=[];
    
        for nACCg=1:length(ACCg_day.(monkey_id))
    
        Stats_mean.h.OFC.current.(gaze_variables).(monkey_id).mean = NaN;
        else
        [Stats_mean.p.OFC.current.(gaze_variables).(monkey_id).mean,Stats_mean.h.OFC.current.(gaze_variables).(monkey_id).mean] = signrank(Current_Sham.OFC.(gaze_variables).(monkey_id).mean, Current_Stim.OFC.(gaze_variables).(monkey_id).mean);
        end
[... 38 more lines not kept]
```

**Agent**

Spatial and temporal code read. Now the causal-decomposition and epoch scripts.

**Agent calls Bash**

```bash
cd $TMPDIR/code/"Scripts for social attention/Inter-individual dynamics"; for f in "Causal Decomposition Index/S1_Gaze_Binned_Distance_Combined.m" "Causal Decomposition Index/S2_Gaze_Get_CDI.m"; do echo "=== $f"; grep -v '^\s*$' "$f" | grep -v "^\s*clear" | cut -c1-230; done | head -260
```

```
=== Causal Decomposition Index/S1_Gaze_Binned_Distance_Combined.m
%% Load Gaze_Data_Combined.mat 
look_back = 0;
look_ahead = 5;
fieldname=fieldnames(GazeData);
for k=1:size(fieldname,1)
    field_id=char(fieldname(k));    
    field_run=fieldnames(GazeData.(field_id));
    for l=1:size(field_run,1)
        run_id=char(field_run(l));
        distance.(field_id).(run_id).stim_ts=[];
        distance.(field_id).(run_id).all_stim_labels=[];
        for nstim=1:length(GazeData.(field_id).(run_id).stim_ts)        
            stim_id=char(strcat('stim_',num2str(nstim)));
            if GazeData.(field_id).(run_id).stim_ts(nstim) >= min(GazeData.(field_id).(run_id).t) && GazeData.(field_id).(run_id).stim_ts(nstim) < max(GazeData.(field_id).(run_id).t)-5
            distance.(field_id).(run_id).stim_ts=[distance.(field_id).(run_id).stim_ts GazeData.(field_id).(run_id).stim_ts(nstim)];
            distance.(field_id).(run_id).all_stim_labels=[distance.(field_id).(run_id).all_stim_labels GazeData.(field_id).(run_id).all_stim_labels(nstim)];
            stim_idx=find(GazeData.(field_id).(run_id).t<=GazeData.(field_id).(run_id).stim_ts(nstim),1,'last');
            sample_range_start=stim_idx+look_back*1000;
            sample_range_end=stim_idx+look_ahead*1000-1; 
[... 186 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/code/"Scripts for social attention/Inter-individual dynamics/Epoch"; grep -n -i "45\|90\|polyfit\|fitlm\|regress\|corr\|randperm\|shuffle\|1000\|signrank\|current_stim\|current_sham\|excl\|>=" S1_Gaze_Time_Epoch.m | cut -c1-220 | head -40
```

```
1:%% Divide time into early (1-45) and late (46-90) epoches
97:% 76 days with more than 90 stims 
98:% Five days excluded: 08122019 OFC Lynch, 11042021 Tarantino ACCg, 11052021 Tarantino dmPFC, 12172021 Tarantino dmPFC, 12222021 Tarantino OFC)
100:%% Put information together for each time bin (1-45, 46-90 stims)
103:time_bin={'stim_1_45','stim_46_90'};
132:    if number_stim>=90
136:            if count_stim<=45
139:                    Decomp_Temporal.(field_id).stim_1_45.stim.stim_time=[Decomp_Temporal.(field_id).stim_1_45.stim.stim_time Decomp_day.(field_id).stim_time(1,ntrial)];
140:                    Decomp_Temporal.(field_id).stim_1_45.stim.current_label=[Decomp_Temporal.(field_id).stim_1_45.stim.current_label,{Decomp_day.(field_id).current_label(1,ntrial)}];
141:                    Decomp_Temporal.(field_id).stim_1_45.stim.m1_distance_to_eyes_contra=[Decomp_Temporal.(field_id).stim_1_45.stim.m1_distance_to_eyes_contra Decomp_day.(field_id).m1_distance_to_eyes_contra(1,ntrial
142:                    Decomp_Temporal.(field_id).stim_1_45.stim.m1_distance_to_eyes_ipsi=[Decomp_Temporal.(field_id).stim_1_45.stim.m1_distance_to_eyes_ipsi Decomp_day.(field_id).m1_distance_to_eyes_ipsi(1,ntrial)];
143:                    Decomp_Temporal.(field_id).stim_1_45.stim.m1_distance_to_eyes=[Decomp_Temporal.(field_id).stim_1_45.stim.m1_distance_to_eyes Decomp_day.(field_id).m1_distance_to_eyes(1,ntrial)];
144:                    Decomp_Temporal.(field_id).stim_1_45.stim.causal_m1m2_eyes_true=[Decomp_Temporal.(field_id).stim_1_45.stim.causal_m1m2_eyes_true Decomp_day.(field_id).causal_m1m2_eyes_true(1,ntrial)];
147:                    Decomp_Temporal.(field_id).stim_1_45.sham.stim_time=[Decomp_Temporal.(field_id).stim_1_45.sham.stim_time Decomp_day.(field_id).stim_time(1,ntrial)];
148:                    Decomp_Temporal.(field_id).stim_1_45.sham.current_label=[Decomp_Temporal.(field_id).stim_1_45.sham.current_label, {Decomp_day.(field_id).current_label(1,ntrial)}];
149:        
[... 25 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/code/"Scripts for social attention/Inter-individual dynamics/Epoch"; sed -n '100,138p;186,251p' S1_Gaze_Time_Epoch.m | grep -v '^\s*$' | cut -c1-200; grep -n "polyfit\|fitlm\|regress\|randperm\|signrank\|median\|1000\|NaN\|isnan" S3_Gaze_Correlation_by_Epoch.m | cut -c1-220 | head -40
```

```
%% Put information together for each time bin (1-45, 46-90 stims)
fieldname=fieldnames(Decomp_day);
time_bin={'stim_1_45','stim_46_90'};
for k=1:size(fieldname,1)
    field_id=char(fieldname(k));
    for n_bin=1:2
        bin_id=char(time_bin(n_bin));
        Decomp_Temporal.(field_id).(bin_id).stim.stim_time=[];
        Decomp_Temporal.(field_id).(bin_id).stim.current_label=[];
        Decomp_Temporal.(field_id).(bin_id).stim.m1_distance_to_eyes_contra=[];
        Decomp_Temporal.(field_id).(bin_id).stim.m1_distance_to_eyes_ipsi=[];
        Decomp_Temporal.(field_id).(bin_id).stim.m1_distance_to_eyes=[];
        Decomp_Temporal.(field_id).(bin_id).stim.causal_m1m2_eyes_true=[];
        Decomp_Temporal.(field_id).(bin_id).sham.stim_time=[];
        Decomp_Temporal.(field_id).(bin_id).sham.current_label=[];
        Decomp_Temporal.(field_id).(bin_id).sham.m1_distance_to_eyes_contra=[];
        Decomp_Temporal.(field_id).(bin_id).sham.m1_distance_to_eyes_ipsi=[];
        Decomp_Temporal.(field_id).(bin_id).sham.m1_distance_to_eyes=[];
        Decomp_Temporal.(field_id).(bin_id).sham.causal_m1m2_eyes_true=[];
    end
[... 91 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/code; grep -rn "deg_per_px *=" --include=*.m . | head; grep -n "sum(\|perm\|_shuffled *[<>]" "Scripts for social attention/Inter-individual dynamics/Epoch/S3_Gaze_Correlation_by_Epoch.m" | cut -c1-250 | head -20; grep -rln "1000" "Scripts for social attention/Saccade kinematics"
```

```
./script/Fixation_Heatmap.m:101:deg_per_px = rad2deg(atan2(.5*h, d)) / (.5*r); 
./script/Fixation_Heatmap.m:175:    deg_per_px = rad2deg(atan2(.5*h, d)) / (.5*r); 
./Scripts for social attention/Spatial dimension/S3_Plotting_Basic_Behaviors_Combined_Hemisphere.m:51:deg_per_px = rad2deg(atan2(.5*h, d)) / (.5*r); 
./Scripts for social attention/Spatial dimension/S3_Plotting_Basic_Behaviors_Combined.m:57:deg_per_px = rad2deg(atan2(.5*h, d)) / (.5*r); 
./Scripts for social attention/Inter-individual dynamics/Epoch/S3_Gaze_Correlation_by_Epoch.m:9:deg_per_px = rad2deg(atan2(.5*h, d)) / (.5*r); 
./Scripts for social attention/Heatmap/S1_Gaze_Fixation_Heatmap.m:101:deg_per_px = rad2deg(atan2(.5*h, d)) / (.5*r); 
./Scripts for social attention/Heatmap/S1_Gaze_Fixation_Heatmap.m:175:    deg_per_px = rad2deg(atan2(.5*h, d)) / (.5*r); 
788:        OFC_nonNaN.(monkey_id).stim_late.distance=[OFC_nonNaN.(monkey_id).stim_late.distance sum(~isnan(Decomp_Temporal.(field_id).stim_46_90.stim.m1_distance_to_eyes) & ~isnan(Decomp_Temporal.(field_id).stim_46_90.stim.causal_m1m2_eyes_true))];
789:        OFC_nonNaN.(monkey_id).stim_late.contra=[OFC_nonNaN.(monkey_id).stim_late.contra sum(~isnan(Decomp_Temporal.(field_id).stim_46_90.stim.m1_distance_to_eyes_contra) & ~isnan(Decomp_Temporal.(field_id).stim_46_90.stim.causal_m1m2_eyes_true))
790:        OFC_nonNaN.(monkey_id).stim_late.ipsi=[OFC_nonNaN.(monkey_id).stim_late.ipsi sum(~isnan(Decomp_Temporal.(field_id).stim_46_90.stim.m1_distance_to_eyes_ipsi) & ~isnan(Decomp_Temporal.(field_id).stim_46_90.stim.causal_m1m2_eyes_true))];
792:        OFC_nonNaN.(monkey_id).stim_early.distance=[OFC_nonNaN.(monkey_id).stim_early.distance sum(~isnan(Decomp_Temporal.(field_id).stim_1_45.stim.m1_distance_to_eyes) & ~isnan(Decomp_Temporal.(field_id).stim_1_45.stim.causal_m1m2_eyes_true))];
793:        OFC_nonNaN.(monkey_id).stim_early.contra=[OFC_nonNaN.(monkey_id).stim_early.contra sum(~isnan(Decomp_Temporal.(field_id).stim_1_45.stim.m1_distance_to_ey
[... 18 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/code; sed -n '1,12p' "Scripts for social attention/Inter-individual dynamics/Epoch/S3_Gaze_Correlation_by_Epoch.m"; grep -n "slope\b\|Estimate\|Coefficients" "Scripts for social attention/Inter-individual dynamics/Epoch/S3_Gaze_Correlation_by_Epoch.m" | head -5; grep -n "prctile\|>=\|<=\|/1000\|/ 1000" "Scripts for social attention/Inter-individual dynamics/Epoch/S3_Gaze_Correlation_by_Epoch.m" | head
```

```
%% Calculate correlation between causal index and distance to eyes for stim in late and early epoches

% Upload Decomp_Temporal_Combined.mat and Decomp_Temporal_shuffled_Combined.mat 

h = 27; % monitor height in cm
d = 50; % subject to monitor in cm
r=768; % monitor height in pixel

deg_per_px = rad2deg(atan2(.5*h, d)) / (.5*r); 
px_per_deg = 1/deg_per_px;

fieldname=fieldnames(Decomp_Temporal_shuffled);
40:        mdl.(field_id).(bin_id).stim_distance_slope=mdl_stim_distance.(bin_id).Coefficients.Estimate(2);
41:        mdl.(field_id).(bin_id).stim_ipsi_slope=mdl_stim_ipsi.(bin_id).Coefficients.Estimate(2);
42:        mdl.(field_id).(bin_id).stim_contra_slope=mdl_stim_contra.(bin_id).Coefficients.Estimate(2);
44:        mdl.(field_id).(bin_id).sham_distance_slope=mdl_sham_distance.(bin_id).Coefficients.Estimate(2);
45:        mdl.(field_id).(bin_id).sham_ipsi_slope=mdl_sham_ipsi.(bin_id).Coefficients.Estimate(2);
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/code; grep -rn -i "shuffled.*>\|shuffled.*<\|>.*shuffled\|<.*shuffled\|p_perm\|perm_p" --include=*.m . | cut -c1-220 | head -10
```

```
./Scripts for social attention/Saccade kinematics/S6_Gaze_Saccade_Kinematics_Combined.m:344:        percent.OFC.(monkey_id)=sum(median(Kinematics.OFC.(monkey_id).stim.slope_shuffled-Kinematics.OFC.(monkey_id).sham.slope_
./Scripts for social attention/Saccade kinematics/S6_Gaze_Saccade_Kinematics_Combined.m:346:        percent.OFC.(monkey_id)=sum(median(Kinematics.OFC.(monkey_id).stim.slope_shuffled-Kinematics.OFC.(monkey_id).sham.slope_
./Scripts for social attention/Saccade kinematics/S6_Gaze_Saccade_Kinematics_Combined.m:351:        percent.dmPFC.(monkey_id)=sum(median(Kinematics.dmPFC.(monkey_id).stim.slope_shuffled-Kinematics.dmPFC.(monkey_id).sham.
./Scripts for social attention/Saccade kinematics/S6_Gaze_Saccade_Kinematics_Combined.m:353:        percent.dmPFC.(monkey_id)=sum(median(Kinematics.dmPFC.(monkey_id).stim.slope_shuffled-Kinematics.dmPFC.(monkey_id).sham.
./Scripts for social attention/Saccade kinematics/S6_Gaze_Saccade_Kinematics_Combined.m:358:        percent.ACCg.(monkey_id)=sum(median(Kinematics.ACCg.(monkey_id).stim.slope_shuffled-Kinematics.ACCg.(monkey_id).sham.slo
./Scripts for social attention/Saccade kinematics/S6_Gaze_Saccade_Kinematics_Combined.m:360:        percent.ACCg.(monkey_id)=sum(median(Kinematics.ACCg.(monkey_id).stim.slope_shuffled-Kinematics.ACCg.(monkey_id).sham.slo
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/code; sed -n '340,362p' "Scripts for social attention/Saccade kinematics/S6_Gaze_Saccade_Kinematics_Combined.m" | cut -c1-330
```

```
monkey_id=char(monkey_names(nmonkey));
    
    OFC_effect=Kinematics.OFC.(monkey_id).stim.slope-Kinematics.OFC.(monkey_id).sham.slope;
    if median(OFC_effect)>0
        percent.OFC.(monkey_id)=sum(median(Kinematics.OFC.(monkey_id).stim.slope_shuffled-Kinematics.OFC.(monkey_id).sham.slope_shuffled,2,'omitnan') > median(OFC_effect))/1000; 
    else
        percent.OFC.(monkey_id)=sum(median(Kinematics.OFC.(monkey_id).stim.slope_shuffled-Kinematics.OFC.(monkey_id).sham.slope_shuffled,2,'omitnan') < median(OFC_effect))/1000; 
    end

    dmPFC_effect=Kinematics.dmPFC.(monkey_id).stim.slope-Kinematics.dmPFC.(monkey_id).sham.slope;
    if median(dmPFC_effect)>0
        percent.dmPFC.(monkey_id)=sum(median(Kinematics.dmPFC.(monkey_id).stim.slope_shuffled-Kinematics.dmPFC.(monkey_id).sham.slope_shuffled,2,'omitnan') > median(dmPFC_effect))/1000; 
    else
        percent.dmPFC.(monkey_id)=sum(median(Kinematics.dmPFC.(monkey_id).stim.slope_shuffled-Kinematics.dmPFC.(monkey_id).sham.slope_shuffled,2,'omitnan') < median(dmPFC_effect))/1000; 
    end

    ACCg_effect=Kinematics.ACCg.(monkey_id).stim.slope-Kinematics.ACCg.(monkey_id).sham.slope;
    if median(ACCg_effect)>0
        percent.ACCg.(monkey_id)=sum(median(Kinematics.ACCg.(monkey_id).stim.slope_shuffled-Kinematics.ACCg.(monkey_id).sham.slope_shuffled,2,'omitnan') > median(ACCg_effect))/1000; 
    else
[... 3 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/code/"Scripts for social attention"; grep -n "ranksum\|signrank\|fdr\|mafdr\|bh\b" "Overall gaze behavior and number of stims/"*.m | cut -c1-230 | head -30
```

```
Overall gaze behavior and number of stims/S1_Total_Number_of_Stim_Combined.m:139:    [Stats.Gaze.(monkey_id).stim.OFC_dmPFC.p, Stats.Gaze.(monkey_id).stim.OFC_dmPFC.h] = ranksum(Number.(monkey_id).OFC.gaze_stim, Number.(monkey_id)
Overall gaze behavior and number of stims/S1_Total_Number_of_Stim_Combined.m:140:    [Stats.Gaze.(monkey_id).stim.dmPFC_ACCg.p, Stats.Gaze.(monkey_id).stim.dmPFC_ACCg.h] = ranksum(Number.(monkey_id).dmPFC.gaze_stim, Number.(monkey
Overall gaze behavior and number of stims/S1_Total_Number_of_Stim_Combined.m:141:    [Stats.Gaze.(monkey_id).stim.ACCg_OFC.p, Stats.Gaze.(monkey_id).stim.ACCg_OFC.h] = ranksum(Number.(monkey_id).ACCg.gaze_stim, Number.(monkey_id).
Overall gaze behavior and number of stims/S1_Total_Number_of_Stim_Combined.m:143:    [Stats.Dot.(monkey_id).stim.OFC_dmPFC.p, Stats.Dot.(monkey_id).stim.OFC_dmPFC.h] = ranksum(Number.(monkey_id).OFC.dot_stim, Number.(monkey_id).dm
Overall gaze behavior and number of stims/S1_Total_Number_of_Stim_Combined.m:144:    [Stats.Dot.(monkey_id).stim.dmPFC_ACCg.p, Stats.Dot.(monkey_id).stim.dmPFC_ACCg.h] = ranksum(Number.(monkey_id).dmPFC.dot_stim, Number.(monkey_id
Overall gaze behavior and number of stims/S1_Total_Number_of_Stim_Combined.m:145:    [Stats.Dot.(monkey_id).stim.ACCg_OFC.p, Stats.Dot.(monkey_id).stim.ACCg_OFC.h] = ranksum(Number.(monkey_id).ACCg.dot_stim, Number.(monkey_id).OFC
Overall gaze behavior and number of stims/S1_Total_Number_of_Stim_Combined.m:147:    [Stats.Gaze.(monkey_id).sham.OFC_dmPFC.p, Stats.Gaze.(monkey_id).sham.OFC_dmPFC.h] = ranksum(Number.(monkey_id).OFC.gaze_sham, Number.(monkey_id)
Overall gaze behavior and number of stims/S1_Total_Number_of_Stim_Combined.m:148:    [Stats.Gaze.(monkey_id).sham.dmPFC_ACCg.p, Stats.Gaze.(monkey_id).sham.dmPFC_ACCg.h] = ranksum(Number.(monkey_id).dmPFC.gaze_sham, Number.(monkey
Overall gaze behavior and number of stims/S1_Total_Number_of_Stim_Combined.m:149:    [Stats.Gaze.(monkey_id).sham.ACCg_OFC.p, Stats.Gaze.(monkey_id).sha
[... 22 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/code/"Scripts for social attention"; sed -n '175,205p' "Overall gaze behavior and number of stims/S1_Total_Number_of_Stim_Combined.m" | cut -c1-300; sed -n '1,30p' "Overall gaze behavior and number of stims/S1_Total_Number_of_Stim_Combined.m" | cut -c1-200 | grep -v '^\s*$' | head -30
```

```
%% fdr correction

% Social 

total_number_social_stim_p_raw=[Stats.Gaze.All.stim.OFC_dmPFC.p Stats.Gaze.All.stim.dmPFC_ACCg.p Stats.Gaze.All.stim.ACCg_OFC.p...
    Stats.Gaze.Lynch.stim.OFC_dmPFC.p Stats.Gaze.Lynch.stim.dmPFC_ACCg.p Stats.Gaze.Lynch.stim.ACCg_OFC.p...
    Stats.Gaze.Tarantino.stim.OFC_dmPFC.p Stats.Gaze.Tarantino.stim.dmPFC_ACCg.p Stats.Gaze.Tarantino.stim.ACCg_OFC.p...
    Stats.Gaze.LynchTarantino.stim.OFC.p Stats.Gaze.LynchTarantino.stim.dmPFC.p Stats.Gaze.LynchTarantino.stim.ACCg.p];
total_number_social_stim_p_correct=dsp3.fdr(total_number_social_stim_p_raw);

total_number_social_sham_p_raw=[Stats.Gaze.All.sham.OFC_dmPFC.p Stats.Gaze.All.sham.dmPFC_ACCg.p Stats.Gaze.All.sham.ACCg_OFC.p...
    Stats.Gaze.Lynch.sham.OFC_dmPFC.p Stats.Gaze.Lynch.sham.dmPFC_ACCg.p Stats.Gaze.Lynch.sham.ACCg_OFC.p...
    Stats.Gaze.Tarantino.sham.OFC_dmPFC.p Stats.Gaze.Tarantino.sham.dmPFC_ACCg.p Stats.Gaze.Tarantino.sham.ACCg_OFC.p...
    Stats.Gaze.LynchTarantino.sham.OFC.p Stats.Gaze.LynchTarantino.sham.dmPFC.p Stats.Gaze.LynchTarantino.sham.ACCg.p];
total_number_social_sham_p_correct=dsp3.fdr(total_number_social_sham_p_raw);

% Non-social

total_number_nonsocial_stim_p_raw=[Stats.Dot.All.stim.OFC_dmPFC.p Stats.Dot.All.stim.dmPFC_ACCg.p Stats.Dot.All.stim.ACCg_OFC.p...
    Stats.Dot.Lynch.stim.OFC_dmPFC.p Stats.Dot.Lynch.stim.dmPFC_ACCg.p Stats.Dot.Lynch.stim.ACCg_OFC.p...
[... 30 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/code/"Scripts for social attention/Saccade kinematics"; grep -n "700\|0.7\|face\|signrank\|bin\|0.01" S5_Pupil_Size.m | cut -c1-200 | head -30; grep -n "look_ahead\|1.5\|first\|macro\|micro" S2_Gaze_Saccade_Data_Combined.m S3_Gaze_Saccade_Control_Combined.m | cut -c1-200 | head -20
```

```
11:int_tbl = shared_utils.io.fload( fullfile(data_root, 'intermediates/combined_tables/int_tbl.mat') );
70:la = 0.7; % look ahead
78:face_rois = nan( rows(eyes_tbl), 4 );
102:  face_rois(i, :) = int_tbl.m1_rois{mi}.rects('face');
116:t_subset = time_axis <= 0.7;
117:accept_within_face = false( size(fix_traces, 1), 1 );
122:  ib = shared_utils.rect.inside( face_rois(i, :), x, y );
123:  accept_within_face(i) = all( ib(t_subset) );
165:t_subset = time_axis <= 0.7;
168:ok_traces = accept_within_face;
198:  stats.ps(i, :) = arrayfun( @(x) signrank(...
S2_Gaze_Saccade_Data_Combined.m:13:% datafile is the first 8 digit of the file names (Data)
S2_Gaze_Saccade_Data_Combined.m:34:        Gaze.(day_char).(run_char).saccades_time = load(append('/Volumes/Brains/BRAINS Microstimulation/Data/intermediates/saccades/',filename2)).microsaccades;
S2_Gaze_Saccade_Data_Combined.m:57:% datafile is the first 8 digit of the file names (Data)
S2_Gaze_Saccade_Data_Combined.m:78:        Dot.(day_char).(run_char).saccades_time = load(append('/Volumes/Brains/BRAINS Microstimulation/Data/intermediates/saccades/',filename2)).microsaccades;
S2_Gaze_Saccade_Data_Combined.m:101:% datafile is the first 8 digit of the file names (Data)
S2_Gaze_Saccade_Data_Combined.m:122:        Gaze.(day_char).(run_char).saccades_time = load(append('/Volumes/Brains/BRAINS Microstimulation/Data/intermediates/saccades/',filename2)).microsaccades;
S2_Gaze_Saccade_Data_Combined.m:145:% datafile is the first 8 digit of the file names (Data)
S2_Gaze_Saccade_Data_Combined.m:166:        Dot.(day_char).(run_char).saccades_time = load(append('/Volumes/Brains/BRAINS Microstimulation/Data/intermediates/saccades/',filename2)).microsaccades;
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd  grep -rl "000959" --include=*.{yaml,json,md,csv,tsv} . 2>/dev/null | head;
```

```
./targets/dandisets.json
./papers/manifest.yaml
```

**Agent calls Bash**

```bash
cd  python3 -c "
import json;d=json.load(open('targets/dandisets.json'))
items=d if isinstance(d,list) else d.get('dandisets',d)
for x in (items if isinstance(items,list) else items.values()):
    if '000959' in json.dumps(x): print(json.dumps(x,indent=1)[:3000])
"; grep -n -B2 -A12 "000959" papers/manifest.yaml | head -40
```

```
[
 {
  "dandiset": "000003",
  "name": "Physiological Properties and Behavioral Correlates of Hippocampal Granule Cells and Mossy Cells",
  "published_version": "0.260218.2052",
  "asset_count": 101,
  "size_gb": 2559.25,
  "data_standards": [
   "Neurodata Without Borders (NWB)"
  ],
  "species": [
   "House mouse"
  ],
  "approaches": [
   "electrophysiological approach",
   "behavioral approach"
  ],
  "papers": [
   {
    "doi": "10.1016/j.neuron.2016.12.011",
[... 114 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python3 -c "
import json;d=json.load(open('targets/dandisets.json'))
for x in d:
    if x['dandiset']=='000959': print(json.dumps(x,indent=1))
"
```

```
Exit code 1
Traceback (most recent call last):
  File "<string>", line 4, in <module>
    if x['dandiset']=='000959': print(json.dumps(x,indent=1))
       ~^^^^^^^^^^^^
TypeError: string indices must be integers, not 'str'
```

**Agent calls Bash**

```bash
cd  python3 -c "
import json;d=json.load(open('targets/dandisets.json'))
print(type(d), list(d)[:5] if isinstance(d,dict) else '')
L=d['dandisets'] if isinstance(d,dict) and 'dandisets' in d else d
for x in L:
    if isinstance(x,dict) and x.get('dandiset')=='000959': print(json.dumps(x,indent=1))
"
```

```
<class 'dict'> ['schema_version', 'generated', 'source', 'counts', 'targets']
```

**Agent calls Bash**

```bash
cd  python3 -c "
import json;d=json.load(open('targets/dandisets.json'))
for x in d['targets']:
    if x.get('dandiset')=='000959': print(json.dumps(x,indent=1))
"
```

```
{
 "dandiset": "000959",
 "name": "Closed-loop microstimulations of the orbitofrontal cortex during real-life gaze interaction enhance dynamic social attention",
 "published_version": "0.261020.0242",
 "asset_count": 1705,
 "size_gb": 25.96,
 "data_standards": [
  "Neurodata Without Borders (NWB)"
 ],
 "species": [
  "Macaca mulatta - Rhesus monkey"
 ],
 "approaches": [
  "behavioral approach"
 ],
 "papers": [
  {
   "doi": "10.1016/j.neuron.2024.05.004",
   "title": "Closed-loop microstimulations of the orbitofrontal cortex during real-life gaze interaction enhance dynamic social attention",
   "relation": "IsDescribedBy",
[... 6 more lines not kept]
```

**Agent**

Now I'll check the checker's expected schema before writing.

**Agent calls Bash**

```bash
cd  sed -n '1,80p' tools/claims_check.py; grep -n "kind\|data:\|p_relation\|corrected" tools/claims_check.py | head -30; grep -rn "corrected:" claims/*/*.yaml | head -3; grep -rn "elsewhere\|with_labels" docs/protocol.md | head -5
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

[... 69 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python3 -c "
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
cd  python3 -c "
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
cd $TMPDIR/code; grep -rn -i "zscore\|bootstrap\|randsample\|datasample" --include=*.m . | cut -c1-200 | head; grep -rln -i "mouth" --include=*.m "Scripts for social attention" | head -3; ls "Scripts for social attention"/Heatmap
```

```
./stim/plot_plx_online_sorted.m:49:    wf_ts = randsample( ts, min(numel(ts), num_wfs) );
./script/plot_new_mua.m:709:  med_dist(mi) = zscore( med_dist(mi) );
./script/plot_new_mua.m:710:  med_mua(mi) = zscore( med_mua(mi) );
./script/debug_filter_unsorted_spike_ts.m:106:    eg_spike_ts = sort( randsample(kept_ts, 100) );    
./script/Fitting_Distance_Model.m:123:      resamp = randsample( ni, nc, true );
./script/Fitting_Distance_Model.m:130:      resamp = randsample( nc, ni, true );
./script/Fitting_Distance_Model.m:198:            keep_target = randsample( target_inds, num_trials );
./script/Fitting_Distance_Model.m:211:                keep_ipsi_indicies = randsample(ipsi_indices,num_contra);
./script/Fitting_Distance_Model.m:215:            %   hint: `help randsample`
Scripts for social attention/Temporal dimension/Inter-looking interval/S3_Gaze_M1_Latency_Across_Trials.m
Scripts for social attention/Temporal dimension/Inter-looking interval/S2_Gaze_M1_Latency_Stats_Combined.m
Scripts for social attention/Temporal dimension/Inter-looking interval/S2_Dot_M1_Latency_Stats_Combined.m
S1_Gaze_Fixation_Heatmap.m
S2_Gaze_Plotting_heatmap.m
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/code/"Scripts for social attention/Heatmap"; grep -n -i "std\|mean(\|norm\|grid\|-20\|20\|flip\|minus\|stim.*sham\|- *sham" S1_Gaze_Fixation_Heatmap.m S2_Gaze_Plotting_heatmap.m | cut -c1-220 | head -40
```

```
S1_Gaze_Fixation_Heatmap.m:1:%% Put information together for each trial (four categories: sham_sham, sham_stim, stim_sham, and stim_stim; plus two general categories: current_sham and current_stim)
S1_Gaze_Fixation_Heatmap.m:27:        stim_label={char('sham_sham') char('sham_stim') char('stim_sham') char('stim_stim') char('current_sham') char('current_stim')};
S1_Gaze_Fixation_Heatmap.m:51:            if isequal(GazeMatrices.(field_id).(run_id).current_label(nstim,:),'sham') && isequal(GazeMatrices.(field_id).(run_id).current_label(nstim-1,:),'sham')                    
S1_Gaze_Fixation_Heatmap.m:53:            elseif isequal(GazeMatrices.(field_id).(run_id).current_label(nstim,:),'stim') && isequal(GazeMatrices.(field_id).(run_id).current_label(nstim-1,:),'sham')     
S1_Gaze_Fixation_Heatmap.m:55:            elseif isequal(GazeMatrices.(field_id).(run_id).current_label(nstim,:),'sham') && isequal(GazeMatrices.(field_id).(run_id).current_label(nstim-1,:),'stim')      
S1_Gaze_Fixation_Heatmap.m:120:        center = [ mean(roi([1, 3])), mean(roi([2, 4])) ];
S1_Gaze_Fixation_Heatmap.m:139:        heatmap_sham = histogram_heatmap( pos_sham, -20:20, -20:20 );
S1_Gaze_Fixation_Heatmap.m:140:        heatmap_stim = histogram_heatmap( pos_stim, -20:20, -20:20 );
S1_Gaze_Fixation_Heatmap.m:152:    ROI.eyes(k,:)=mean(roi_eyes,1,'omitnan');
S1_Gaze_Fixation_Heatmap.m:153:    ROI.mouth(k,:)=mean(roi_mouth,1,'omitnan');
S1_Gaze_Fixation_Heatmap.m:154:    ROI.face(k,:)=mean(roi_face,1,'omitnan');
S1_Gaze_Fixation_Heatmap.m:156:    mats{k} = (mats_stim{k}-mats_sham{k}) / sum( mats_sham{k}(:) + mats_stim{k}(:) );
S1_Gaze_Fixation_Heatmap.m:183:    center = [ mean(roi([1, 3])), mean(roi([2, 4])) ];
S2_Gaze_Plotting_heatmap.m:4:OFC_day.All={'07202019'  '07312019'  '08052019'  '08122019'  '08292019' ...
S2_Gaze_Plotting_heatmap.m:5:    '09052019'  '09192019'  '10012019'  '11052019'   '12122019' ...  
S2_Gaze_Plotting_heatmap.m:6:    '12182019'  '01032020'  '01102020'  '01242020'  '0
[... 25 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/code/"Scripts for social attention/Overall gaze behavior and number of stims"; grep -n "signrank\|ranksum\|fdr" S3_Stats_ROI_number_duration_final.m | cut -c1-250 | head -30; grep -n "number\b\|= *size\|length(" S2_Gaze_ROI_number_duration_Combined.m | head
```

```
100:    [Stats.All_day.(monkey_id).total_number.eye_neface_p,Stats.All_day.(monkey_id).total_number.eye_neface_h]=signrank(Gaze_summary.All_day.(monkey_id).m1_eye.total_number,Gaze_summary.All_day.(monkey_id).m1_neface.total_number);
101:    [Stats.All_day.(monkey_id).total_number.eye_dot_p,Stats.All_day.(monkey_id).total_number.eye_dot_h]=signrank(Gaze_summary.All_day.(monkey_id).m1_eye.total_number,Dot_summary.All_day.(monkey_id).m1_eye.total_number);
103:    [Stats.All_day.(monkey_id).average_duration.eye_neface_p,Stats.All_day.(monkey_id).average_duration.eye_neface_h]=signrank(Gaze_summary.All_day.(monkey_id).m1_eye.average_duration,Gaze_summary.All_day.(monkey_id).m1_neface.average_duration);
104:    [Stats.All_day.(monkey_id).average_duration.eye_dot_p,Stats.All_day.(monkey_id).average_duration.eye_dot_h]=signrank(Gaze_summary.All_day.(monkey_id).m1_eye.average_duration,Dot_summary.All_day.(monkey_id).m1_eye.average_duration);
121:        [Stats.(region_id).(monkey_id).total_number.eye_neface_p,Stats.(region_id).(monkey_id).total_number.eye_neface_h]=signrank(Gaze_summary.(region_id).(monkey_id).m1_eye.total_number,Gaze_summary.(region_id).(monkey_id).m1_neface.total_numbe
122:        [Stats.(region_id).(monkey_id).total_number.eye_dot_p,Stats.(region_id).(monkey_id).total_number.eye_dot_h]=signrank(Gaze_summary.(region_id).(monkey_id).m1_eye.total_number,Dot_summary.(region_id).(monkey_id).m1_eye.total_number);
124:        [Stats.(region_id).(monkey_id).average_duration.eye_neface_p,Stats.(region_id).(monkey_id).average_duration.eye_neface_h]=signrank(Gaze_summary.(region_id).(monkey_id).m1_eye.average_duration,Gaze_summary.(region_id).(monkey_id).m1_neface
125:        [Stats.(region_id).(monkey_id).average_duration.eye_dot_p,Stats.(region_id).(monkey_id).average_duration.eye_dot_h]=signrank(Gaze_summary.(region_id).(monkey_id).m1_eye.average_duration,Dot_summary.(region_id).(monkey_id).m1_eye.average_d
131:    [Stats_region.(monkey_id).total_number.m1_eye.O
[... 32 more lines not kept]
```

**Agent**

I have what I need from the paper and code. Writing the claims file now.

**Agent calls Write**

```json
{
 "file_path": "claims/000959/10.1016-j.neuron.2024.05.004.yaml",
 "content": "# Claims for Fan, Dal Monte, Nair, Fagan & Chang (2024) on dandiset 000959.\n# Written by an agent (model \"claude-opus-5-5\", Claude Code in GitHub Actions), 2026-10-22,\n# protocol pilot-10 as stated in docs/protocol.md.\n#\n# Text read: the accepted author manuscript in PubMed Central (PMC11309918, NIHMS1994226),\n# main text, figure legends and STAR Methods, with its one supplement\n# (NIHMS1994226-supplement-1.pdf, Table S1 and the legends of Figures S1 to S4). The version of\n# record (Neuron 112(15) 2631-2644.e6) was not read. The Results point to \"Supplementary\n# Results\" for the Mouth stimulation experiments and the post-gaze window; the supplement holds\n# no such section, and these results are given in the STAR Methods of the manuscript\n# (\"Gaze distance analyses\" and \"Gaze distance analyses (Mouth stimulation)\"), which were read.\n#\n# Code read: github.com/changlabneuro/microstim-ofc-social-attention, commit cc0bf994 (2024-10-15),\n# the analysis code named in Data and code availability (also Zenodo doi:10.5281/zenodo.11110139).\n# It holds MATLAB scripts for every analysis of the paper (\"Scripts for social attention\":\n# Get data, Overall gaze behavior and number of stims, Heatmap, Spatial dimension, Temporal\n# dimension, Inter-individual dynamics, Saccade kinematics) and older scripts (stim/, script/).\n# It starts from intermediate files (fixation events, ROIs, positions, stimulation and sham\n# times) made by an upstream pipeline that is not in the repository, and it calls functions\n# of outside packages (bfw, shared_utils, dsp3). The causal decomposition itself was run\n# outside the repository; only its output folder name is given\n# (cd_output_null_02_1000_150_100_10). The repository also holds zipped processed data folders;\n# these were not opened.\n#\n# Data the paper used. Two male rhesus macaques were stimulated (M1, monkey L, \"Lynch\" in the\n# code, chamber on the left; monkey T, \"Tarantino\", chamber on the right); one female, monkey E,\n# was the partner (M2) of both. Eyes stimulation experiments: 27 days per stimulated area (OFC,\n# dmPFC, ACCg), 15 per area from monkey L and 12 from monkey T, 81 days in all; the code lists\n# the days by date. Each day alternated live social gaze sessions (about 10 for L, 9 to 11; about\n# 15 for T, 14 to 15) and non-social control sessions with a random dot motion (RDM) stimulus in\n# front of M2's face (about 5; 4 to 8 for L, 5 for T), 300 s each with 180 s breaks. Mouth\n# stimulation control experiments: 5 days per area from monkey T. Gaze positions and pupil\n# size of both monkeys at 1000 Hz (EyeLink 1000); in control sessions M2's gaze is not usable.\n# Each trial is a microstimulation (75 uA, 100 Hz, 200 ms) or a sham, triggered with\n# probability 0.5 by an online fixation (150 ms window, dispersion below 1 degree) in the Eyes\n# ROI (or the RDM ROI, or the Mouth ROI), trials at least 5 s apart, two stimulations and two\n# shams in every four. Variables used: stimulation and sham times and labels, M1 and M2 gaze\n# positions, fixations (EyeMMV, t1 = 1.18 and t2 = 0.59 degrees, minimum 70 ms), the Eyes,\n# Face, Mouth and RDM ROIs per day, gaze events labelled M1-only, M2-only or mutual, pupil\n# size, saccades. Raw neural signals and multi-unit activity were recorded (Fig. 1D) but no\n# finding below rests on them.\n#\n# Method choices fixed here from the code where the Methods are silent, for every claim that\n# uses trials. A trial is kept when its time lies within the run and more than 5 s before the\n# run's last sample; the first trial of each run is dropped (the code labels each trial by the\n# one before it). Trials are grouped by their own type (stimulation or sham). The post-gaze\n# epoch takes the fixations whose start time lies in [0, 1.5) s after the trial time. A\n# fixation's position is the mean of its gaze samples; its social gaze distance is the\n# Euclidean distance from that position to the centre of the partner's Eyes ROI (the RDM ROI in\n# control sessions). A trial's distance is the mean over its fixations; a day's value is the\n# mean over its trials of a type, ignoring trials with no fixation. A fixation is contralateral\n# or ipsilateral by the side of the mean horizontal gaze position of its event relative to the\n# centre of the partner's whole Face ROI: for monkey L (left chamber) left of centre is\n# ipsilateral, for monkey T (right chamber) right of centre is ipsilateral. Day-level\n# comparisons are two-sided Wilcoxon signed-rank tests over days; trial-level comparisons are\n# two-sided Wilcoxon rank-sum tests over the trials of all days of an area pooled. \"Both\n# monkeys combined\" is all 27 days of an area. Distances in the code are in pixels, converted\n# to degrees for plots with h = 27 cm, d = 50 cm and 768 pixels (the Methods give 36 cm to the\n# middle monitor); rank tests do not depend on that scale.\n#\n# Details open in the paper and the code, named in the claims that need them: the padding of\n# the Eyes ROI (the Methods text reads \"adding a padding of to the center of each eye\", the\n# number is missing), the smoothing used to fill gaps before the causal decomposition and the\n# decomposition's settings, the side of the permutation test for the slope difference, the\n# bootstrap p-value of the Mouth comparison, and how the \"diff\" values and the 41% and 86%\n# figures are averaged.\nschema_version: 2\ndataset:\n  archive: dandi\n  id: \"000959\"\npaper: doi:10.1016/j.neuron.2024.05.004\nclaims:\n- id: design-days-per-area\n  statement: Eyes stimulation was applied on 27 days per stimulated area (OFC, dmPFC and ACCg),\n    15 per area from monkey L and 12 per area from monkey T, and Mouth stimulation on 5 days per\n    area from monkey T.\n  source: STAR Methods, Closed-loop microstimulation protocol, paragraph 1; Figure 1B legend\n  quote: In our main experiments (Eyes stimulation; n = 15 per area from monkey L and n = 12 per\n    area from monkey T)\n  expected:\n  - quantity: Eyes stimulation days per area, monkey L\n    value: 15\n    tolerance: 0\n  - quantity: Eyes stimulation days per area, monkey T\n    value: 12\n    tolerance: 0\n  - quantity: Mouth stimulation days per area, monkey T\n    value: 5\n    tolerance: 0\n  criterion: Counts of days, so no tolerance; a day counts when it holds stimulation and sham\n    trials of the named experiment and area. The code's day lists (S2_Gaze_Stats_Basic_Behaviors_Combined.m)\n    give the dates of the 81 Eyes stimulation days. Reproduced when every count matches;\n    partially reproduced when the Eyes counts match and the Mouth days are not in the dataset.\n- id: design-sessions-per-day\n  statement: Each day held on average 10 live social gaze sessions (9 to 11) and 5 non-social\n    control sessions (4 to 8) for monkey L, and 15 social (14 to 15) and 5 control sessions for\n    monkey T, each 300 s long.\n  source: STAR Methods, Experimental setup, paragraph 2\n  quote: Each data collection day consisted of a total of alternating 10 live social gaze sessions\n    and 5 non-social control sessions on average for monkey L (9-11 social and 4-8 control sessions\n    across all days) and alternating 15 live social gaze sessions and 5 non-social control sessions\n    on average for monkey T (14-15 social and 5 control sessions across all days). Each session\n    lasted 300 sec.\n  expected:\n  - quantity: mean social sessions per day, monkey L\n    value: 10\n    tolerance: 1\n  - quantity: mean control sessions per day, monkey L\n    value: 5\n    tolerance: 0.5\n  - quantity: mean social sessions per day, monkey T\n    value: 15\n    tolerance: 1.5\n  - quantity: mean control sessions per day, monkey T\n    value: 5\n    tolerance: 0.5\n  - quantity: session duration\n    value: 300\n    tolerance: 30\n    unit: s\n  criterion: Over the Eyes stimulation days. The reported ranges (9 to 11, 4 to 8, 14 to 15, 5)\n    are checked as ranges widened by 10% of each bound. Reproduced when all means and ranges hold.\n- id: fig1e-stim-counts-comparable\n  statement: In the live social gaze condition, the total numbers of microstimulations and of shams\n    per day were comparable across the three stimulated areas and between the two monkeys.\n  source: Results, opening section, paragraph 2; Figure 1E legend\n  quote: The total number of microstimulations (and shams) received per day was comparable across\n    the three stimulated regions and comparable between the two animals both in the social gaze and\n    non-social control conditions (Fig. 1E, live social gaze condition, all p > 0.90\n  statistics:\n  - test: Wilcoxon rank sum, two-sided\n    p: 0.9\n    p_relation: \">\"\n    corrected: FDR\n    n: 15 days per area for monkey L and 12 for monkey T\n  criterion: A claim of absence, judged on the paper's test. Per day, the number of\n    microstimulation trials and of sham trials of the social sessions, counted as in\n    S1_Total_Number_of_Stim_Combined.m (the trials kept for analysis). Wilcoxon rank-sum tests,\n    two-sided, between each pair of areas for both monkeys combined and for each monkey, and\n    between the monkeys for each area, 12 tests for stimulations and 12 for shams, each set\n    FDR-corrected (Benjamini-Hochberg; the code calls dsp3.fdr, an outside package). Reproduced\n    when no corrected p is below 0.05; the smallest corrected p is reported, and whether all\n    exceed 0.90.\n- id: figs1d-stim-counts-nonsocial\n  statement: In the non-social control condition the numbers of microstimulations and shams per\n    day were also comparable across areas and between monkeys.\n  source: Results, opening section, paragraph 2; Figure S1D legend\n  quote: Fig. S1D, non-social control condition, all p > 0.10\n  statistics:\n  - test: Wilcoxon rank sum, two-sided\n    p: 0.1\n    p_relation: \">\"\n    corrected: FDR\n  criterion: As fig1e-stim-counts-comparable, on the control (RDM) sessions. Reproduced when no\n    FDR-corrected p is below 0.05; whether all exceed 0.10 is reported.\n- id: figs1e-eyes-more-than-face\n  statement: The stimulated monkeys made significantly more fixations per day on the partner's\n    Eyes than on the non-eye Face, for days of all three stimulated areas.\n  source: Results, opening section, paragraph 2; Figure S1E\n  quote: The total number of fixations on partner's Eyes per day was significantly higher than\n    fixations on non-eye Face for all three stimulated brain regions (Fig. S1E, top, all p < 10−4,\n    Wilcoxon signed rank, two-sided, FDR-corrected)\n  statistics:\n  - test: Wilcoxon signed rank, two-sided\n    p: 0.0001\n    p_relation: \"<\"\n    corrected: FDR\n    n: 27 days per area\n  criterion: Per day, the number of M1 fixations in the Eyes ROI and in the non-eye Face ROI\n    (whole Face minus Eyes) over the social sessions, compared with a two-sided signed-rank\n    test over the 27 days of each area, FDR-corrected (Benjamini-Hochberg) with the Eyes against\n    RDM test of the same area, as in S3_Stats_ROI_number_duration_final.m. The Methods say\n    \"total number ... for each day\"; the code takes the mean over the day's sessions of the\n    per-session count. Readings (a) the day's total and (b) the mean per session; they give the\n    same ranks only when session numbers are equal. Reproduced when, under each reading, Eyes\n    exceed non-eye Face with corrected p < 0.05 for all three areas; the p-values are compared\n    with 10^-4.\n- id: figs1e-eyes-vs-rdm-comparable\n  statement: The number of fixations on the partner's Eyes per day was comparable to the number of\n    fixations on the RDM stimulus, for days of all three areas.\n  source: Results, opening section, paragraph 2; Figure S1E\n  quote: the total number of fixations on partner's Eyes per day was comparable to fixations on the\n    RDM stimulus for days involving the three stimulated regions (Fig. S1E, top, all p > 0.30)\n  statistics:\n  - test: Wilcoxon signed rank, two-sided\n    p: 0.3\n    p_relation: \">\"\n    corrected: FDR\n  criterion: A claim of absence, judged on the paper's test. Per day, M1 fixations in the Eyes ROI\n    in social sessions against fixations in the RDM ROI in control sessions, paired by day,\n    two-sided signed-rank test per area, FDR-corrected as in figs1e-eyes-more-than-face, under\n    the same two readings of the day count. Reproduced when no corrected p is below 0.05 under\n    the paper's reading (a); reading (b) is shown as the code's variant.\n- id: fig2a-density-map-ofc\n  statement: After OFC microstimulations, compared with shams, the stimulated monkey's fixations in\n    the 1.5 s post-gaze epoch were more clustered around the partner monkey.\n  source: Results, Closed-loop microstimulations of OFC facilitate momentary social attention in\n    the spatial dimension, paragraph 2; Figure 2A\n  quote: Specifically, microstimulations of OFC led to more clustered subsequent gaze fixations\n    around the partner monkey (Fig. 2A\n  criterion: >-\n    From the Methods (Fixation density map): fixations of the post-gaze epoch assigned to 1-degree\n    squares of a 40 by 40 degree grid centred on the partner's Eyes ROI, counts summed per day for\n    stimulation and for sham trials, the stimulation minus sham difference averaged over days\n    per area, monkey T's maps flipped horizontally. The normalisation is given two ways, and\n    both are run: (1) the Methods, each day's maps z-scored over grid squares before the\n    difference; (2) the code (S1_Gaze_Fixation_Heatmap.m), the difference divided by the day's\n    total count of stimulation and sham fixations. The paper reads the map by eye and gives no\n    measure of \"more clustered\"; the readings named are (a) the averaged difference summed over\n    squares inside the whole Face ROI is positive, and (b) the same inside the Eyes ROI. The\n    claim is reproduced when the OFC map is positive under every reading and normalisation, not\n    reproduced when it is negative under all, and blocked as methods_underspecified when they\n    differ. dmPFC and ACCg values are reported alongside.\n- id: fig2c-ofc-social-gaze-distance\n  statement: OFC microstimulations decreased the social gaze distance, the mean distance of the\n    stimulated monkey's fixations in the post-gaze epoch from the centre of the partner's Eyes,\n    compared with shams; the effect held in each monkey.\n  source: Results, Closed-loop microstimulations of OFC facilitate momentary social attention in\n    the spatial dimension, paragraph 3; Figure 2C legend\n  quote: microstimulations of OFC significantly decreased the average distance of one's own gaze\n    positions in space relative to partner's Eyes during the post-gaze epoch, compared to shams\n    (Fig. 2C, p < 0.001, Wilcoxon signed rank, two-sided\n  statistics:\n  - about: OFC, both monkeys combined\n    test: Wilcoxon signed rank, two-sided\n    p: 0.001\n    p_relation: \"<\"\n    n: 27 OFC days\n  - about: OFC, monkey L\n    test: Wilcoxon signed rank, two-sided\n    p: 0.008\n    n: 15 OFC days\n  - about: OFC, monkey T\n    test: Wilcoxon signed rank, two-sided\n    p: 0.002\n    n: 12 OFC days\n  criterion: Social gaze distance per trial and per day as in the opening comment (STAR Methods,\n    Gaze distance analyses; S3_Basic_Gaze_Matrices_Combined.m, S1_Gaze_Results_Combined.m and\n    S2_Gaze_Stats_Basic_Behaviors_Combined.m), day means of stimulation trials against day means\n    of sham trials, two-sided signed-rank test over OFC days. Reproduced when the combined test\n    gives p < 0.001 with the median day difference (stimulation minus sham) negative, and each\n    monkey's test gives p < 0.05 in the same direction; partially reproduced when the combined\n    test gives p < 0.05 in that direction but a monkey's does not or the combined p is not below\n    0.001. The p-values are compared with the reported ones.\n- id: fig2c-dmpfc-accg-no-distance-effect\n  statement: Microstimulations of dmPFC or ACCg did not change social gaze distance.\n  source: Results, Closed-loop microstimulations of OFC facilitate momentary social attention in\n    the spatial dimension, paragraph 3; Figure 2C\n  quote: By contrast, we did not observe such stimulation effect on social gaze distance for dmPFC\n    (Fig. 2C, p = 0.361) or ACCg (Fig. 2C, p = 0.374)\n  statistics:\n  - about: dmPFC\n    test: Wilcoxon signed rank, two-sided\n    p: 0.361\n    n: 27 dmPFC days\n  - about: ACCg\n    test: Wilcoxon signed rank, two-sided\n    p: 0.374\n    n: 27 ACCg days\n  criterion: A claim of absence, judged on the paper's test, as in fig2c-ofc-social-gaze-distance\n    for dmPFC and ACCg days. Reproduced when neither test gives p < 0.05; the median day\n    differences and p-values are reported.\n- id: fig2e-ofc-contralateral\n  statement: The OFC effect on social gaze distance was stronger for fixations in the hemifield\n    contralateral to the stimulated hemisphere; it was significant for contralateral fixations,\n    not for ipsilateral ones, and the contralateral effect exceeded the ipsilateral one.\n  source: Results, Closed-loop microstimulations of OFC facilitate momentary social attention in\n    the spatial dimension, paragraph 3; Figure 2E legend\n  quote: >-\n    Notably, the observed stimulation effect of OFC was more pronounced for gaze fixations in the\n    contralateral visual field of the stimulated brain hemisphere (Fig. 2D–E; contralateral: p <\n    0.001; significant statistics for individual animals are reported in the figure legend;\n    ipsilateral: p = 0.068; contralateral vs. ipsilateral: p = 0.026, Wilcoxon signed rank,\n    two-sided)\n  statistics:\n  - about: contralateral, stimulation against sham, both monkeys\n    test: Wilcoxon signed rank, two-sided\n    p: 0.001\n    p_relation: \"<\"\n    n: 27 OFC days\n  - about: contralateral, monkey L\n    test: Wilcoxon signed rank, two-sided\n    p: 0.015\n  - about: contralateral, monkey T\n    test: Wilcoxon signed rank, two-sided\n    p: 0.012\n  - about: ipsilateral, stimulation against sham, both monkeys\n    test: Wilcoxon signed rank, two-sided\n    p: 0.068\n  - about: contralateral against ipsilateral effect, both monkeys\n    test: Wilcoxon signed rank, two-sided\n    p: 0.026\n  - about: contralateral against ipsilateral effect, monkey L\n    test: Wilcoxon signed rank, two-sided\n    p: 0.073\n  - about: contralateral against ipsilateral effect, monkey T\n    test: Wilcoxon signed rank, two-sided\n    p: 0.204\n  criterion: >-\n    Fixations split by hemifield as in the opening comment (S1_Get_data_gaze_Lynch.m and\n    _Tarantino.m), social gaze distance per trial and day computed within each hemifield. The\n    effect of a day is the stimulation minus sham difference of day means. Tests from the\n    Methods: signed-rank of stimulation against sham per hemifield, and signed-rank of the\n    contralateral effect against the ipsilateral effect paired by day (the code holds no script\n    for this last test; the pairing by day follows from the Methods' \"Wilcoxon signed rank test\n    ... between hemifields\"). Days without fixations in a hemifield are left out of that test.\n    Reproduced when the contralateral test gives p < 0.05 with negative median effect, the\n    ipsilateral test gives p >= 0.05, and the contralateral against ipsilateral test gives\n    p < 0.05 with the contralateral effect more negative. Partially reproduced when only the\n    contralateral effect holds. Per-monkey values are reported and compared.\n- id: fig2e-dmpfc-accg-no-hemifield-effect\n  statement: For dmPFC and ACCg there was no stimulation effect on social gaze distance in either\n    hemifield, and no difference between hemifields.\n  source: Results, Closed-loop microstimulations of OFC facilitate momentary social attention in\n    the spatial dimension, paragraph 3; Figure 2E\n  quote: >-\n    Again, no such effect was observed in either hemifield for dmPFC (Fig. 2E, contralateral: p =\n    0.501; ipsilateral: p = 0.149; contralateral vs. ipsilateral: p = 0.230) or ACCg (Fig. 2E, p =\n    0.442; p = 0.517; p = 0.564)\n  statistics:\n  - about: dmPFC contralateral\n    test: Wilcoxon signed rank, two-sided\n    p: 0.501\n  - about: dmPFC ipsilateral\n    test: Wilcoxon signed rank, two-sided\n    p: 0.149\n  - about: dmPFC contralateral against ipsilateral\n    test: Wilcoxon signed rank, two-sided\n    p: 0.23\n  - about: ACCg contralateral\n    test: Wilcoxon signed rank, two-sided\n    p: 0.442\n  - about: ACCg ipsilateral\n    test: Wilcoxon signed rank, two-sided\n    p: 0.517\n  - about: ACCg contralateral against ipsilateral\n    test: Wilcoxon signed rank, two-sided\n    p: 0.564\n  criterion: A claim of absence, judged on the paper's tests as in fig2e-ofc-contralateral for\n    dmPFC and ACCg. Reproduced when none of the six tests gives p < 0.05; effects and p-values\n    are reported.\n- id: fig2f-nonsocial-no-distance-effect\n  statement: In the non-social control condition, microstimulations of none of the three areas\n    changed the distance of fixations from the centre of the RDM stimulus.\n  source: Results, Closed-loop microstimulations of OFC facilitate momentary social attention in\n    the spatial dimension, paragraph 4; Figure 2F\n  quote: Crucially, these stimulation effects of OFC were exclusively observed in the live social\n    gaze condition ... and not in the non-social gaze control condition using the RDM stimulus with\n    no behavioral meaning to monkeys (Fig. 2F, OFC\n  statistics:\n  - about: OFC\n    test: Wilcoxon signed rank, two-sided\n    p: 0.118\n  - about: dmPFC\n    test: Wilcoxon signed rank, two-sided\n    p: 0.719\n  - about: ACCg\n    test: Wilcoxon signed rank, two-sided\n    p: 0.302\n  criterion: A claim of absence, judged on the paper's test. Non-social gaze distance as social gaze\n    distance with the centre of the RDM ROI in place of the Eyes (STAR Methods, Gaze distance\n    analyses, last sentence; S1_Dot_Results_Combined.m), on control-session trials, signed-rank\n    over days per area. Reproduced when no area gives p < 0.05.\n- id: fig2gh-nonsocial-no-hemifield-effect\n  statement: In the non-social control condition there was no stimulation effect in either\n    hemifield, and no hemifield difference, for any area.\n  source: Results, Closed-loop microstimulations of OFC facilitate momentary social attention in\n    the spatial dimension, paragraph 4; Figure 2G-H\n  quote: >-\n    The absence of stimulation effect for the RDM stimulus was also found when gaze fixation\n    locations were split by hemifield for OFC (Fig. 2G–H; contralateral: p = 0.097; ipsilateral: p\n    = 0.249; contralateral vs. ipsilateral: p = 0.442), dmPFC (p = 0.374; p = 0.517; p = 0.773) or\n    ACCg (p = 0.532; p = 0.943; p = 0.171)\n  statistics:\n  - about: OFC contralateral\n    test: Wilcoxon signed rank, two-sided\n    p: 0.097\n  - about: OFC ipsilateral\n    test: Wilcoxon signed rank, two-sided\n    p: 0.249\n  - about: OFC contralateral against ipsilateral\n    test: Wilcoxon signed rank, two-sided\n    p: 0.442\n  - about: dmPFC contralateral\n    test: Wilcoxon signed rank, two-sided\n    p: 0.374\n  - about: dmPFC ipsilateral\n    test: Wilcoxon signed rank, two-sided\n    p: 0.517\n  - about: dmPFC contralateral against ipsilateral\n    test: Wilcoxon signed rank, two-sided\n    p: 0.773\n  - about: ACCg contralateral\n    test: Wilcoxon signed rank, two-sided\n    p: 0.532\n  - about: ACCg ipsilateral\n    test: Wilcoxon signed rank, two-sided\n    p: 0.943\n  - about: ACCg contralateral against ipsilateral\n    test: Wilcoxon signed rank, two-sided\n    p: 0.171\n  criterion: A claim of absence, judged on the paper's tests, as fig2e-ofc-contralateral on\n    control-session trials with distances to the RDM centre. The hemifield split uses the same\n    reference as in the code for social sessions, the centre of the partner's whole Face ROI.\n    Reproduced when none of the nine tests gives p < 0.05.\n- id: methods-ofc-distance-longer-windows\n  statement: The OFC decrease of social gaze distance also held within 2 s and within 3 s after the\n    trial for both monkeys combined and for monkey L, not for monkey T.\n  source: STAR Methods, Gaze distance analyses, paragraph 1\n  quote: In fact, the effect was present and lasted longer beyond 1.5 sec in one of the stimulated\n    monkeys (within 2 sec after trial onset\n  statistics:\n  - about: within 2 s, both monkeys\n    test: Wilcoxon signed rank, two-sided\n    p: 0.003\n  - about: within 2 s, monkey L\n    test: Wilcoxon signed rank, two-sided\n    p: 0.008\n  - about: within 2 s, monkey T\n    test: Wilcoxon signed rank, two-sided\n    p: 0.204\n  - about: within 3 s, both monkeys\n    test: Wilcoxon signed rank, two-sided\n    p: 0.004\n  - about: within 3 s, monkey L\n    test: Wilcoxon signed rank, two-sided\n    p: 0.007\n  - about: within 3 s, monkey T\n    test: Wilcoxon signed rank, two-sided\n    p: 0.204\n  criterion: As fig2c-ofc-social-gaze-distance with the window [0, 2) s and [0, 3) s (the code's\n    alternative call basic_gaze_matrices(GazeData, 0, 3)). Reproduced when, for both windows, the\n    combined and monkey L tests give p < 0.05 with stimulation below sham and the monkey T test\n    gives p >= 0.05; partially reproduced when the combined tests hold.\n- id: methods-ofc-no-change-in-fixation-number\n  statement: OFC microstimulations did not change the number of fixations within the partner's Eyes\n    or whole Face in the post-gaze window, in either monkey, for windows of 1.5, 2 or 3 s.\n  source: STAR Methods, Gaze distance analyses, paragraph 2\n  quote: Following OFC microstimulations, unlike more clustered subsequent gaze fixations around\n    another social agent, we did not observe any change in the total number of fixations within\n    partner's Eyes (within 1.5 sec\n  statistics:\n  - about: Eyes, 1.5 s, each monkey\n    test: Wilcoxon signed rank, two-sided\n    p: 0.18\n    p_relation: \">\"\n  - about: Eyes, 2 s\n    test: Wilcoxon signed rank, two-sided\n    p: 0.24\n    p_relation: \">\"\n  - about: Eyes, 3 s\n    test: Wilcoxon signed rank, two-sided\n    p: 0.3\n    p_relation: \">\"\n  - about: whole Face, 1.5 s\n    test: Wilcoxon signed rank, two-sided\n    p: 0.12\n    p_relation: \">\"\n  - about: whole Face, 2 s\n    test: Wilcoxon signed rank, two-sided\n    p: 0.2\n    p_relation: \">\"\n  - about: whole Face, 3 s\n    test: Wilcoxon signed rank, two-sided\n    p: 0.22\n    p_relation: \">\"\n  criterion: A claim of absence, judged on the paper's tests. Per trial, the number of M1 fixations\n    starting in the window and lying in the Eyes ROI, or in the whole Face ROI (Eyes, Mouth and\n    the rest of the face), counting M1-only and mutual events as the code does\n    (fixation_m1_eye_number and fixation_m1_wholeface_number in S3_Basic_Gaze_Matrices_Combined.m,\n    which use M1-only events); day means per trial type; signed-rank test over OFC days for each\n    monkey. Readings for the events counted are (a) M1-only events, as the code, (b) M1-only and\n    mutual events. Reproduced when no test gives p < 0.05 under the code's reading (a); reading\n    (b) is shown.\n- id: methods-ofc-longer-face-looking\n  statement: With OFC microstimulations the stimulated monkey spent more time looking within the\n    partner's whole Face in the post-gaze epoch (48.9 ms more than with shams, both monkeys\n    combined), and more weakly within the Eyes; dmPFC and ACCg showed no such effect.\n  source: STAR Methods, Gaze distance analyses, paragraph 2\n  quote: With OFC microstimulations, the monkeys spent more time looking within the partner's whole\n    Face (p = 0.003, stim minus sham difference = 48.9 msec for both monkeys combined; p = 0.008,\n    diff = 66.6 msec for monkey L and p = 0.129, diff = 39.5 msec for monkey T)\n  statistics:\n  - about: OFC whole Face, both monkeys\n    test: Wilcoxon signed rank, two-sided\n    p: 0.003\n  - about: OFC whole Face, monkey L\n    test: Wilcoxon signed rank, two-sided\n    p: 0.008\n  - about: OFC whole Face, monkey T\n    test: Wilcoxon signed rank, two-sided\n    p: 0.129\n  - about: dmPFC whole Face, both monkeys\n    test: Wilcoxon signed rank, two-sided\n    p: 0.683\n  - about: ACCg whole Face, both monkeys\n    test: Wilcoxon signed rank, two-sided\n    p: 0.848\n  - about: OFC Eyes, both monkeys\n    test: Wilcoxon signed rank, two-sided\n    p: 0.044\n  expected:\n  - quantity: OFC whole Face total duration, stimulation minus sham, both monkeys\n    value: 48.9\n    tolerance: 4.89\n    unit: ms\n  - quantity: same, monkey L\n    value: 66.6\n    tolerance: 6.66\n    unit: ms\n  - quantity: same, monkey T\n    value: 39.5\n    tolerance: 3.95\n    unit: ms\n  - quantity: dmPFC whole Face difference, both monkeys\n    value: -14.5\n    tolerance: 1.45\n    unit: ms\n  - quantity: ACCg whole Face difference, both monkeys\n    value: 3.4\n    tolerance: 0.34\n    unit: ms\n  - quantity: OFC Eyes difference, both monkeys\n    value: 16.5\n    tolerance: 1.65\n    unit: ms\n  criterion: Per trial, the summed duration of M1 fixations starting in [0, 1.5) s and lying in the\n    whole Face ROI or in the Eyes ROI (fixation_m1_wholeface_totalduration and\n    fixation_m1_eye_totalduration in the code, M1-only events, 0 when none); day means per trial\n    type; signed-rank test over days. How \"diff\" is taken is not stated; the readings are (a) the\n    median over days of the stimulation minus sham day means, (b) the mean over days of that\n    difference. Reproduced when the OFC whole Face test gives p < 0.05 with stimulation longer,\n    dmPFC and ACCg give p >= 0.05, the OFC Eyes test gives p < 0.05, and under one reading the\n    OFC whole Face differences fall within tolerance. Partially reproduced when the tests hold\n    and no reading matches the numbers.\n- id: methods-mouth-stimulation-no-effect\n  statement: When microstimulations were triggered by looking at the partner's Mouth (or at an RDM\n    stimulus at the Mouth location), none of the three areas changed social or non-social gaze\n    distance, in either hemifield.\n  source: STAR Methods, Gaze distance analyses (Mouth stimulation); Results, Closed-loop\n    microstimulations of OFC facilitate momentary social attention in the spatial dimension,\n    paragraph 4\n  quote: On the day level, none of the three brain regions had any microstimulation effect on social\n    gaze distance (OFC\n  statistics:\n  - about: social, OFC\n    test: Wilcoxon signed rank, two-sided\n    p: 1\n    n: 5 days from monkey T\n  - about: social, dmPFC\n    test: Wilcoxon signed rank, two-sided\n    p: 1\n  - about: social, ACCg\n    test: Wilcoxon signed rank, two-sided\n    p: 0.125\n  - about: social, each hemifield, all areas\n    test: Wilcoxon signed rank, two-sided\n    p: 0.18\n    p_relation: \">\"\n  - about: non-social, OFC\n    test: Wilcoxon signed rank, two-sided\n    p: 1\n  - about: non-social, dmPFC\n    test: Wilcoxon signed rank, two-sided\n    p: 0.188\n  - about: non-social, ACCg\n    test: Wilcoxon signed rank, two-sided\n    p: 0.188\n  - about: non-social, each hemifield, all areas\n    test: Wilcoxon signed rank, two-sided\n    p: 0.06\n    p_relation: \">\"\n  criterion: A claim of absence, judged on the paper's test. Social gaze distance on Mouth\n    stimulation days as in fig2c-ofc-social-gaze-distance with the centre of the partner's Mouth\n    ROI (same size as the Eyes ROI without padding), and non-social distance to the centre of the\n    RDM ROI at the Mouth location; signed-rank over the 5 days per area, both hemifields and each\n    hemifield. The code in the repository holds no Mouth-stimulation script; the trial handling\n    of the Eyes analysis is used. Reproduced when no test gives p < 0.05. If the dataset does not\n    hold the Mouth stimulation days the claim cannot be tested.\n- id: methods-eyes-vs-mouth-bootstrap\n  statement: For contralateral fixations, the OFC stimulation effect on social gaze distance was\n    significantly more negative in Eyes stimulation than in Mouth stimulation, but not for\n    ipsilateral fixations or both hemifields combined; the difference was stronger using monkey\n    T's Eyes days only.\n  source: STAR Methods, Gaze distance analyses (Mouth stimulation)\n  quote: For fixations in the contralateral hemifield, microstimulation effect (stimulation minus\n    sham) of OFC led to significantly smaller social gaze distance in Eyes stimulation compared to\n    Month stimulation (p = 0.009), while no effect was observed for fixations in the ipsilateral\n    hemifield (p = 0.724) or when both hemifields combined (p = 0.799)\n  statistics:\n  - about: contralateral, all Eyes days\n    test: bootstrap, 1,000 resamples of 5 days with replacement\n    p: 0.009\n  - about: ipsilateral, all Eyes days\n    test: bootstrap\n    p: 0.724\n  - about: both hemifields, all Eyes days\n    test: bootstrap\n    p: 0.799\n  - about: contralateral, monkey T Eyes days\n    test: bootstrap\n    p: 0.005\n  - about: ipsilateral, monkey T Eyes days\n    test: bootstrap\n    p: 0.654\n  - about: both hemifields, monkey T Eyes days\n    test: bootstrap\n    p: 0.51\n  depends_on:\n  - methods-mouth-stimulation-no-effect\n  criterion: From the Methods. The OFC effect per day is the stimulation minus sham difference of\n    day-mean social gaze distance. 5 days are drawn with replacement from the 27 OFC Eyes days (or\n    the 12 of monkey T) 1,000 times, the median effect of each draw is taken, and the 1,000\n    medians are compared with the median effect of the 5 OFC Mouth days. The p-value is not\n    defined in the paper and no code holds it; the readings are (a) the fraction of bootstrap\n    medians at or above the Mouth median (one-sided, Eyes smaller), (b) twice the smaller tail\n    fraction (two-sided). The seed is a standard choice and is recorded. Reproduced when, under\n    a reading, the contralateral p values are below 0.05 and the ipsilateral and combined ones are\n    not, for both the all-days and the monkey-T comparisons; the outcome follows the rule for\n    several readings.\n- id: fig3b-ofc-inter-looking-interval\n  statement: OFC microstimulations decreased the inter-looking interval, the latency of the\n    stimulated monkey to look back at the partner's whole Face within 5 s after the trial,\n    compared with shams; dmPFC and ACCg microstimulations did not.\n  source: Results, Microstimulations of OFC also promote momentary social attention in the temporal\n    dimension, Inter-looking interval, paragraph 1; Figure 3B legend\n  quote: Microstimulations of OFC decreased this inter-looking interval (Fig. 3B, p = 0.035, Wilcoxon\n    signed rank, two-sided; see Fig. S3A for an alternative visualization). However, we did not\n    observe such stimulation effect for dmPFC (Fig. 3B, p = 0.792) or ACCg (Fig. 3B, p = 0.291)\n  statistics:\n  - about: OFC, both monkeys\n    test: Wilcoxon signed rank, two-sided\n    p: 0.035\n    n: 27 OFC days\n  - about: OFC, monkey L\n    test: Wilcoxon signed rank, two-sided\n    p: 0.188\n  - about: OFC, monkey T\n    test: Wilcoxon signed rank, two-sided\n    p: 0.092\n  - about: dmPFC\n    test: Wilcoxon signed rank, two-sided\n    p: 0.792\n  - about: ACCg\n    test: Wilcoxon signed rank, two-sided\n    p: 0.291\n  criterion: From the Methods (Gaze latency analyses) and S1_Gaze_M1_Latency_Combined.m. Per trial,\n    the time from the trial sample to the start of the first M1-only or mutual whole Face event\n    that starts after it and within 5,000 samples (5 s); no such event leaves the trial out\n    (NaN). Day means per trial type, ignoring NaN; signed-rank over days. Reproduced when OFC gives\n    p < 0.05 with stimulation shorter and dmPFC and ACCg give p >= 0.05; per-monkey values are\n    reported (the paper finds neither significant alone).\n- id: ili-nonsocial-no-effect\n  statement: The inter-looking interval did not change with stimulation in the non-social control\n    condition, for any area.\n  source: Results, Microstimulations of OFC also promote momentary social attention in the temporal\n    dimension, Inter-looking interval, paragraph 1\n  quote: Further, this reduction of inter-looking interval from OFC microstimulations was specific\n    to social attention as no effect was observed in the non-social gaze condition\n  statistics:\n  - about: OFC\n    test: Wilcoxon signed rank, two-sided\n    p: 0.773\n  - about: dmPFC\n    test: Wilcoxon signed rank, two-sided\n    p: 0.08\n  - about: ACCg\n    test: Wilcoxon signed rank, two-sided\n    p: 0.943\n  criterion: A claim of absence, judged on the paper's test, as fig3b-ofc-inter-looking-interval on\n    control sessions with the corresponding whole Face ROI and M1 events only\n    (S1_Dot_M1_Latency_Combined.m). Reproduced when no area gives p < 0.05.\n- id: ili-missing-trials-41\n  statement: On 41% of microstimulation and sham trials per day on average, the stimulated monkey\n    did not look back at the partner's whole Face within the 5 s window.\n  source: Results, Microstimulations of OFC also promote momentary social attention in the temporal\n    dimension, Inter-looking interval, paragraph 1\n  quote: the stimulated monkey did not look back at the partner's whole Face during the examined\n    time window on 41% of microstimulation and sham trials per day on average\n  expected:\n    quantity: mean over days of the fraction of trials with no inter-looking interval\n    value: 41\n    tolerance: 4.1\n    unit: \"%\"\n  depends_on:\n  - fig3b-ofc-inter-looking-interval\n  criterion: Per day, the fraction of analysed social-session trials (stimulation and sham\n    together) whose inter-looking interval is NaN, averaged over days. The days averaged over are\n    not stated; the readings are (a) all 81 Eyes stimulation days, (b) the 27 OFC days.\n    Reproduced when a reading falls within tolerance.\n- id: figs3b-ili-trial-level\n  statement: With all trials of each area pooled across days, OFC microstimulations still decreased\n    the inter-looking interval, while dmPFC and ACCg did not.\n  source: Results, Microstimulations of OFC also promote momentary social attention in the temporal\n    dimension, Inter-looking interval, paragraph 1; Figure S3B legend\n  quote: Nevertheless, when we combined all trials for each stimulated region, we still observed\n    similar results to the day-level analysis above (Fig. S3B, OFC\n  statistics:\n  - about: OFC, both monkeys\n    test: Wilcoxon rank sum, two-sided\n    p: 0.01\n  - about: OFC, monkey L\n    test: Wilcoxon rank sum, two-sided\n    p: 0.026\n  - about: OFC, monkey T\n    test: Wilcoxon rank sum, two-sided\n    p: 0.143\n  - about: dmPFC\n    test: Wilcoxon rank sum, two-sided\n    p: 0.301\n  - about: ACCg\n    test: Wilcoxon rank sum, two-sided\n    p: 0.602\n  depends_on:\n  - fig3b-ofc-inter-looking-interval\n  criterion: Trial inter-looking intervals as in fig3b-ofc-inter-looking-interval, stimulation\n    trials against sham trials of all days of an area pooled, rank-sum test\n    (S3_Gaze_M1_Latency_Across_Trials.m). Reproduced when OFC gives p < 0.05 with stimulation\n    shorter and dmPFC and ACCg give p >= 0.05.\n- id: figs3c-reciprocation-day-level-none\n  statement: At the day level, microstimulations did not significantly reduce the reciprocation\n    latency in any area; on 86% of trials per day on average there was no sequence of the partner\n    looking at the stimulated monkey followed by the stimulated monkey looking back.\n  source: Results, Reciprocation latency, paragraph 1; Figure S3C legend\n  quote: On the day level, microstimulations did not seem to greatly reduce such reciprocation\n    latency (Fig. S3C–D, OFC\n  statistics:\n  - about: OFC\n    test: Wilcoxon signed rank, two-sided\n    p: 0.13\n  - about: dmPFC\n    test: Wilcoxon signed rank, two-sided\n    p: 0.701\n  - about: ACCg\n    test: Wilcoxon signed rank, two-sided\n    p: 0.4\n  expected:\n    quantity: mean over days of the fraction of trials with no M2-then-M1 sequence\n    value: 86\n    tolerance: 8.6\n    unit: \"%\"\n  criterion: >-\n    Reciprocation latency per trial from S1_Gaze_ITI_Combined.m (\"all_face\" events): whole Face\n    events of M1 and of M2 that start in the 5 s after the trial, mutual events counted for both;\n    for each run of consecutive M2 events followed by an M1 event, the time from the start of the\n    run's first M2 event to the start of that M1 event; the trial's value is the mean over such\n    sequences, NaN when there is none. Day means per trial type ignoring NaN; signed-rank over\n    days. A claim of absence for the tests: reproduced when no area gives p < 0.05. The 86% is the\n    per-day fraction of analysed trials with NaN, averaged over days, under the readings (a) all\n    81 days, (b) the 27 OFC days; it is reported against its tolerance and is part of the claim.\n- id: fig3d-ofc-reciprocation-latency\n  statement: With trials pooled across days, OFC microstimulations decreased the latency of the\n    stimulated monkey to reciprocate the partner's gaze to his face; dmPFC and ACCg did not.\n  source: Results, Reciprocation latency, paragraph 1; Figure 3D legend\n  quote: When combining all trials for each stimulated region, we observed that microstimulations of\n    OFC decreased reciprocation latency (Fig. 3D, p = 0.011, Wilcoxon rank sum, two-sided). We again\n    did not observe such stimulation effect for dmPFC (Fig. 3D, p = 0.777) or ACCg (Fig. 3D, p =\n    0.368)\n  statistics:\n  - about: OFC, both monkeys\n    test: Wilcoxon rank sum, two-sided\n    p: 0.011\n  - about: OFC, monkey L\n    test: Wilcoxon rank sum, two-sided\n    p: 0.074\n  - about: OFC, monkey T\n    test: Wilcoxon rank sum, two-sided\n    p: 0.079\n  - about: dmPFC\n    test: Wilcoxon rank sum, two-sided\n    p: 0.777\n  - about: ACCg\n    test: Wilcoxon rank sum, two-sided\n    p: 0.368\n  depends_on:\n  - figs3c-reciprocation-day-level-none\n  criterion: Trial reciprocation latencies as in figs3c-reciprocation-day-level-none, stimulation\n    trials against sham trials of all days of an area pooled, NaN trials left out, rank-sum test\n    (S3_Gaze_ITI_Across_Trials.m). Reproduced when OFC gives p < 0.05 with stimulation shorter\n    and dmPFC and ACCg give p >= 0.05.\n- id: partner-monkey-unchanged\n  statement: Microstimulations in none of the areas changed the partner monkey's social gaze\n    distance, inter-looking interval or reciprocation latency.\n  source: Results, Microstimulations do not change momentary social attention in the unstimulated\n    animal, paragraph 1\n  quote: Therefore, we did not find any evidence that the social gaze behaviors of the unstimulated\n    monkey were altered on a short timescale during social gaze interactions.\n  statistics:\n  - about: M2 social gaze distance, OFC\n    test: Wilcoxon signed rank, two-sided\n    p: 0.118\n  - about: M2 social gaze distance, dmPFC\n    test: Wilcoxon signed rank, two-sided\n    p: 0.302\n  - about: M2 social gaze distance, ACCg\n    test: Wilcoxon signed rank, two-sided\n    p: 0.064\n  - about: M2 inter-looking interval, OFC\n    test: Wilcoxon signed rank, two-sided\n    p: 1\n  - about: M2 inter-looking interval, dmPFC\n    test: Wilcoxon signed rank, two-sided\n    p: 0.866\n  - about: M2 inter-looking interval, ACCg\n    test: Wilcoxon signed rank, two-sided\n    p: 0.249\n  - about: M2 reciprocation latency, OFC\n    test: Wilcoxon signed rank, two-sided\n    p: 0.665\n  - about: M2 reciprocation latency, dmPFC\n    test: Wilcoxon signed rank, two-sided\n    p: 0.773\n  - about: M2 reciprocation latency, ACCg\n    test: Wilcoxon signed rank, two-sided\n    p: 0.701\n  criterion: >-\n    A claim of absence, judged on the paper's tests (signed-rank over days per area). M2 social\n    gaze distance: M2 fixations starting in [0, 1.5) s, distance to the centre of M1's Eyes ROI\n    (m2_distance_to_eyes in the code). M2 inter-looking interval, from the Results: the latency\n    between the first and second M2 whole Face events within 5 s after the trial. M2 reciprocation\n    latency, from the Results: the latency of M2 to look at M1's whole Face within 5 s after the\n    trial when M2 was being looked at by M1. The code in the repository has no script for the two\n    M2 latencies; whether the latency is taken from the trial time or from the start of the M1\n    look is open for the reciprocation latency, readings (a) from the start of the M1 whole Face\n    event, (b) from the trial time. Reproduced when no test gives p < 0.05 under every reading.\n- id: figs4a-causal-strength-no-stim-effect\n  statement: Microstimulations did not change the relative causal strength of gaze between the\n    monkeys in any area.\n  source: Results, Do microstimulations of OFC also lead to longer timescale modulation of social\n    gaze exchanges?, paragraph 1; Figure S4A legend\n  quote: We did not observe stimulation effect on the magnitudes of relative causal strength (OFC\n    ... dmPFC ... ACCg\n  statistics:\n  - about: OFC\n    test: Wilcoxon signed rank, two-sided\n    p: 0.239\n  - about: dmPFC\n    test: Wilcoxon signed rank, two-sided\n    p: 0.962\n  - about: ACCg\n    test: Wilcoxon signed rank, two-sided\n    p: 0.361\n  criterion: >-\n    A claim of absence, judged on the paper's test. Relative causal strength per trial from the\n    causal decomposition analysis of Yang, Peng and Huang (2018; code at\n    github.com/accyang/causal-decomposition-analysis) of the moment-by-moment social gaze distance\n    of M1 (to M2's Eyes centre) and of M2 (to M1's Eyes centre), in 10 ms bins\n    (S1_Gaze_Binned_Distance_Combined.m), over the post-gaze epoch; the trial value is the mean\n    over IMFs of the M1-to-M2 relative causal strength (S2_Gaze_Get_CDI.m). Trials are excluded\n    when either monkey has more than 1 s of continuous NaN samples or when the ends of a smoothed\n    gap are more than 20 degrees apart (Methods). Open, with no source: the smoothing used to fill\n    gaps between fixations, and the decomposition's noise level, ensemble size and other settings.\n    The output folder name cd_output_null_02_1000_150_100_10 suggests noise 0.2, 1,000 ensembles\n    and 150 bins (1.5 s); this is taken as reading (a), and reading (b) is the defaults of the\n    Yang et al. code with the same 150 bins. Linear interpolation over gaps is the gap filling\n    under both, named as a standard choice that the paper does not fix. Day means per trial type,\n    signed-rank over days per area. Reproduced when no area gives p < 0.05 under each reading.\n- id: figs4b-causal-strength-no-epoch-effect\n  statement: Neither trial type nor time epoch (first 45 against next 45 stimulations) changed the\n    relative causal strength in any area.\n  source: Results, Do microstimulations of OFC also lead to longer timescale modulation of social\n    gaze exchanges?, paragraph 1; Figure S4B legend\n  quote: We did not observe effect of microstimulation trial type or time epoch on relative casual\n    strength (OFC\n  statistics:\n  - about: OFC, all comparisons\n    test: Wilcoxon signed rank, two-sided\n    p: 0.16\n    p_relation: \">\"\n  - about: dmPFC, all comparisons\n    test: Wilcoxon signed rank, two-sided\n    p: 0.67\n    p_relation: \">\"\n  - about: ACCg, all comparisons\n    test: Wilcoxon signed rank, two-sided\n    p: 0.46\n    p_relation: \">\"\n  depends_on:\n  - figs4a-causal-strength-no-stim-effect\n  - epoch-days-76-of-81\n  criterion: A claim of absence, judged on the paper's tests. Epochs as in epoch-days-76-of-81;\n    day means of relative causal strength for stimulation and sham trials in each epoch; the\n    paper does not list the comparisons; the readings are (a) the four pairs that differ in one\n    factor (stimulation against sham within each epoch, early against late within each trial\n    type), (b) all six pairs of the four groups. Reproduced when no test gives p < 0.05 under each\n    reading.\n- id: epoch-days-76-of-81\n  statement: 76 of the 81 days had at least 90 microstimulations and entered the epoch analysis;\n    the five excluded were 1 OFC day of monkey L and, of monkey T, 1 OFC, 2 dmPFC and 1 ACCg day.\n  source: STAR Methods, Inter-individual gaze dynamics analyses, paragraph 2\n  quote: 76 out of 81 days had at least 90 stimulations. The 5 days excluded from further analysis\n    were 1 day from monkey L with OFC microstimulations, 1 day from monkey T OFC, 2 days from monkey\n    T dmPFC, and 1 day from monkey T ACCg.\n  expected:\n    quantity: days with at least 90 stimulations\n    value: 76\n    tolerance: 0\n  criterion: A count of days with named composition, so no tolerance; the code\n    (S1_Gaze_Time_Epoch.m) names the excluded days, 08122019 (L, OFC), 12222021 (T, OFC), 11052021\n    and 12172021 (T, dmPFC), 11042021 (T, ACCg). Stimulations are counted (a) among the analysed\n    trials (first trial of each run and trials in the last 5 s dropped), as the code counts them,\n    or (b) among all stimulations delivered. Reproduced when a reading gives 76 days with the\n    named composition.\n- id: ofc-slope-unchanged-by-epoch\n  statement: For OFC, the slope of the fitted relation between social gaze distance and relative\n    causal strength did not differ between the early and late epochs, for both hemifields\n    combined, contralateral or ipsilateral fixations.\n  source: Results, Do microstimulations of OFC also lead to longer timescale modulation of social\n    gaze exchanges?, paragraph 1; Figure 4C; Figure S4C-D\n  quote: >-\n    we correlated social gaze distance and relative causal strength (STAR Methods) and found the\n    slope of this fitted correlation comparable between early and late epochs for OFC (Fig. S4C,\n    both hemifields combined: p = 0.757; Fig. 4C, contralateral: p = 0.882; Fig. S4D, ipsilateral:\n    p = 0.098)\n  statistics:\n  - about: both hemifields\n    test: Wilcoxon signed rank, two-sided\n    p: 0.757\n  - about: contralateral\n    test: Wilcoxon signed rank, two-sided\n    p: 0.882\n  - about: ipsilateral\n    test: Wilcoxon signed rank, two-sided\n    p: 0.098\n  depends_on:\n  - figs4a-causal-strength-no-stim-effect\n  - epoch-days-76-of-81\n  criterion: A claim of absence, judged on the paper's test. From the Methods and\n    S3_Gaze_Correlation_by_Epoch.m. For each day and epoch, an ordinary least squares fit (fitlm)\n    of relative causal strength on social gaze distance (in degrees) over the stimulation trials\n    of the epoch; distance is the trial mean over fixations in the post-gaze epoch, overall,\n    contralateral or ipsilateral. Late against early slopes, signed-rank over OFC days.\n    Reproduced when no test gives p < 0.05, under each reading of figs4a-causal-strength-no-stim-effect.\n- id: fig4c-dmpfc-slope-late-greater\n  statement: For dmPFC, the slope of the relation between contralateral social gaze distance and\n    relative causal strength was larger in the late than in the early epoch (p = 0.054, at the\n    margin), and significantly so for both hemifields combined; not for ipsilateral fixations,\n    and not for ACCg.\n  source: Figure 4C legend; Figure S4C-D legends\n  quote: For dmPFC, the slope of this fitted correlation was stronger for the late epoch than early\n    epoch (p = 0.054 for both monkeys combined; p = 0.048 for monkey L and p = 0.625 for monkey T)\n  statistics:\n  - about: dmPFC contralateral, both monkeys\n    test: Wilcoxon signed rank, two-sided\n    p: 0.054\n  - about: dmPFC contralateral, monkey L\n    test: Wilcoxon signed rank, two-sided\n    p: 0.048\n  - about: dmPFC contralateral, monkey T\n    test: Wilcoxon signed rank, two-sided\n    p: 0.625\n  - about: dmPFC both hemifields\n    test: Wilcoxon signed rank, two-sided\n    p: 0.037\n  - about: ACCg both hemifields\n    test: Wilcoxon signed rank, two-sided\n    p: 0.77\n  - about: dmPFC ipsilateral\n    test: Wilcoxon signed rank, two-sided\n    p: 0.757\n  - about: ACCg ipsilateral\n    test: Wilcoxon signed rank, two-sided\n    p: 0.381\n  depends_on:\n  - ofc-slope-unchanged-by-epoch\n  criterion: Slopes as in ofc-slope-unchanged-by-epoch for dmPFC and ACCg days. Reproduced when the\n    dmPFC contralateral test gives p < 0.1 with late slopes larger (median late minus early\n    positive), the dmPFC both-hemifields test gives p < 0.05 in the same direction, and the dmPFC\n    ipsilateral and the ACCg tests give p >= 0.05; partially reproduced when the direction holds\n    and only some of these do. The 0.1 bound is taken from the paper's own marking of p = 0.054\n    as \"p ≈ 0.05\". Results under each reading of the causal decomposition are shown.\n- id: fig4d-dmpfc-slope-permutation\n  statement: Against a null from shuffling the order of each day's 90 stimulations, the dmPFC\n    increase of the contralateral slope from early to late epoch was significant (p = 0.015), not\n    for both hemifields combined or ipsilateral fixations.\n  source: Results, Do microstimulations of OFC also lead to longer timescale modulation of social\n    gaze exchanges?, paragraph 2; Figure 4D legend; Figure S4E-F legends\n  quote: However, the slope of this fitted correlation for dmPFC was stronger for the late epoch than\n    early epoch, specifically for gaze fixations in the contralateral hemifield (Fig. 4D; p = 0.015,\n    permutation test\n  statistics:\n  - about: dmPFC contralateral, both monkeys\n    test: permutation test, 1,000 shuffles\n    p: 0.015\n  - about: dmPFC contralateral, monkey L\n    test: permutation test\n    p: 0.038\n  - about: dmPFC contralateral, monkey T\n    test: permutation test\n    p: 0.068\n  - about: dmPFC both hemifields\n    test: permutation test\n    p: 0.131\n  - about: dmPFC ipsilateral\n    test: permutation test\n    p: 0.455\n  depends_on:\n  - fig4c-dmpfc-slope-late-greater\n  criterion: >-\n    From the Methods and S1_Gaze_Time_Epoch.m and S3_Gaze_Correlation_by_Epoch.m. The real\n    statistic is the median over days of the late minus early slope. Null: within each day the\n    90 stimulation trials are permuted 1,000 times and split into the first 45 and the next 45,\n    slopes refitted, and for each permutation the median over days of the slope difference is\n    taken. The p-value computation is not in the repository; the readings are (a) one-sided in\n    the direction of the real median, the fraction of null medians beyond it, as the code\n    computes the permutation p of Fig. 5G (S6_Gaze_Saccade_Kinematics_Combined.m), (b)\n    two-sided, twice that fraction. Reproduced when dmPFC contralateral gives p < 0.05 with a\n    positive real median and the both-hemifields and ipsilateral tests give p >= 0.05; the\n    outcome follows the rule for several readings, and per-monkey values are reported. (The\n    Figure S4F legend prints a \"* p < 0.05\" key while the Results give p = 0.455; the Results\n    value is used.)\n- id: dmpfc-slope-positive\n  statement: For dmPFC, the slope of the relation between social gaze distance and relative causal\n    strength was on average positive in both epochs, so that the closer the stimulated monkey\n    looked to the partner, the more his gaze was led by the partner.\n  source: Results, Do microstimulations of OFC also lead to longer timescale modulation of social\n    gaze exchanges?, paragraph 2\n  quote: Specifically, the slope of this examined correlation on average was positive in both early\n    and late epochs for gaze fixations in both hemifields for dmPFC\n  depends_on:\n  - fig4c-dmpfc-slope-late-greater\n  criterion: Slopes as in ofc-slope-unchanged-by-epoch, dmPFC days. \"On average\" is read as the mean\n    over days, with the median as a second reading. \"In both hemifields\" is read as (a) the slope\n    with both hemifields combined, (b) the contralateral and the ipsilateral slopes each.\n    Reproduced when the average slope is positive in both epochs under every reading; the\n    outcome follows the rule for several readings. No test is reported for this sign.\n- id: fig5a-trigger-duration-unchanged\n  statement: Microstimulations of OFC or dmPFC did not change the duration of the Eyes fixation that\n    triggered the trial.\n  source: Results, Microstimulation effects of OFC and dmPFC are not driven by low-level properties\n    of saccades, paragraph 1; Figure 5A\n  quote: Importantly, the observed effects of OFC and dmPFC microstimulations were not driven by any\n    change in the duration of current looking to partner's Eyes that triggered a microstimulation or\n    sham (Fig. 5A, OFC\n  statistics:\n  - about: OFC\n    test: Wilcoxon signed rank, two-sided\n    p: 0.302\n  - about: dmPFC\n    test: Wilcoxon signed rank, two-sided\n    p: 0.269\n  criterion: A claim of absence, judged on the paper's test. Per trial, the duration of the M1 Eyes\n    event in progress at the trial time; day means per trial type; signed-rank over days.\n    Readings for the events (the code for this panel is not among the scripts read) are (a)\n    M1-only and mutual Eyes events, (b) M1-only events. Reproduced when neither area gives\n    p < 0.05 under each reading.\n- id: fig5b-pupil-unchanged\n  statement: Pupil size did not differ between microstimulation and sham trials in any 10 ms bin of\n    the 700 ms after trial onset, for any area.\n  source: Results, Microstimulation effects of OFC and dmPFC are not driven by low-level properties\n    of saccades, paragraph 1; Figure 5B legend\n  quote: No difference was observed for pupil size between the two trial types throughout the\n    700-msec period following trial onset for any of the three stimulated regions.\n  statistics:\n  - test: Wilcoxon signed rank, two-sided, per 10 ms bin\n    p: 0.05\n    p_relation: \">\"\n  criterion: A claim of absence, judged on the paper's test. From the Methods and\n    stim/S5_Pupil_Size.m. Trials where M1's gaze stays within the partner's whole Face ROI for the\n    whole 700 ms after the trial; M1 pupil size averaged over trials per day and type in 10 ms\n    bins; signed-rank per bin over days, uncorrected. Reproduced when no bin of any area gives\n    p < 0.05; the number of bins below 0.05 is reported.\n- id: fig5cd-saccade-counts-unchanged\n  statement: The numbers of microsaccades and macrosaccades in the post-gaze epoch did not differ\n    between microstimulation and sham trials for OFC or dmPFC.\n  source: Results, Microstimulation effects of OFC and dmPFC are not driven by low-level properties\n    of saccades, paragraph 1; Figure 5C-D\n  quote: number of microsaccades (Fig. 5C, OFC\n  statistics:\n  - about: microsaccades, OFC\n    test: Wilcoxon signed rank, two-sided\n    p: 0.456\n  - about: microsaccades, dmPFC\n    test: Wilcoxon signed rank, two-sided\n    p: 0.581\n  - about: macrosaccades, OFC\n    test: Wilcoxon signed rank, two-sided\n    p: 0.055\n  - about: macrosaccades, dmPFC\n    test: Wilcoxon signed rank, two-sided\n    p: 0.23\n  criterion: A claim of absence, judged on the paper's test. Saccades detected by the unsupervised\n    clustering method of Otero-Millan et al. (2014); a saccade lying strictly within a fixation\n    interval (EyeMMV) is a microsaccade, any other a macrosaccade (Methods). Counts per trial in\n    the post-gaze epoch, day means per type, signed-rank over days. If the dataset holds no\n    saccade events, the detection must be run with the Otero-Millan code (outside software) and\n    the claim is with_inputs for that run. Reproduced when no test gives p < 0.05.\n- id: fig5e-h-saccade-kinematics-unchanged\n  statement: Microstimulations of OFC or dmPFC did not change macrosaccade peak velocity, the slope\n    of peak velocity on amplitude, or that slope by saccade direction.\n  source: Results, Microstimulation effects of OFC and dmPFC are not driven by low-level properties\n    of saccades, paragraph 1; Figure 5E-H\n  quote: macrosaccade peak velocity (Fig. 5E, OFC\n  statistics:\n  - about: peak velocity, OFC\n    test: Wilcoxon signed rank, two-sided\n    p: 0.848\n  - about: peak velocity, dmPFC\n    test: Wilcoxon signed rank, two-sided\n    p: 1\n  - about: slope difference against zero, OFC\n    test: Wilcoxon signed rank, two-sided\n    p: 0.665\n  - about: slope difference against zero, dmPFC\n    test: Wilcoxon signed rank, two-sided\n    p: 0.904\n  - about: slope difference, OFC\n    test: permutation test\n    p: 0.515\n  - about: slope difference, dmPFC\n    test: permutation test\n    p: 0.164\n  - about: by direction, OFC\n    test: Wilcoxon signed rank, two-sided\n    p: 0.47\n    p_relation: \">\"\n  - about: by direction, dmPFC\n    test: Wilcoxon signed rank, two-sided\n    p: 0.31\n    p_relation: \">\"\n  depends_on:\n  - fig5cd-saccade-counts-unchanged\n  criterion: A claim of absence, judged on the paper's tests. From the Methods and\n    S6_Gaze_Saccade_Kinematics_Combined.m. The first macrosaccade of each trial's post-gaze epoch;\n    day mean peak velocity per type, signed-rank. Per day, a linear fit of peak velocity on\n    amplitude for stimulation and for sham trials, the slope difference tested against zero by\n    signed-rank; the permutation test shuffles the trial labels 1,000 times within each day and\n    gives the fraction of shuffled median differences beyond the real median, on its side, as\n    the code does. Direction groups II, IC, CI and CC by the hemifields of start and end,\n    signed-rank against zero per group. Reproduced when no test gives p < 0.05.\n"
}
```

```
File created successfully at: claims/000959/10.1016-j.neuron.2024.05.004.yaml (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd  python tools/claims_check.py claims/000959/10.1016-j.neuron.2024.05.004.yaml paper/10.1016-j.neuron.2024.05.004.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  grep -n "—\|rather" claims/000959/*.yaml; grep -c "statistics:" claims/000959/*.yaml; grep -c "criterion:" claims/000959/*.yaml; git status --short
```

```
30
36
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
?? claims/000959/
?? scripts
```

**Agent**

I wrote `claims/000959/10.1016-j.neuron.2024.05.004.yaml`. The quote checker reports 36 claims, 36 quotes, 132 statistical values and 0 problems. Nothing is committed.

**Text read.** I read the PubMed Central author manuscript (PMC11309918): main text, figure legends and STAR Methods, plus its one supplement, which holds Table S1 and the legends of Figures S1 to S4. I did not read the version of record. The Results refer to "Supplementary Results" for the Mouth-stimulation control and the post-gaze window. The supplement has no such section, but those results appear in the manuscript's STAR Methods, so nothing a claim needed was missing.

**Code read.** I read the analysis code at github.com/changlabneuro/microstim-ofc-social-attention, commit cc0bf994. It is MATLAB that starts from intermediate files made by a pipeline not in the repository, and it calls outside packages (bfw, shared_utils, dsp3). Where the code settles something the Methods leave open, I followed it and said so in the file:
- which trials are kept (the first trial of each run and trials in the last 5 s of a run are dropped);
- the post-gaze window is [0, 1.5) s by fixation start time;
- how ipsilateral and contralateral are defined for each monkey;
- how the two latencies are measured;
- the 10 ms bins and the regression used for the slope analysis;
- the FDR families.

Where the code and the Methods disagree, the Methods give the main result and the code's choice is shown as a variant. This applies to the heatmap (the Methods z-score it, the code divides by total count) and to the per-day fixation count (a day total in the Methods, a mean per session in the code).

**Counts.**
- 36 claims, all with quotes, none marked `inferred`.
- 34 claims carry statistics (132 values recorded); 6 carry expected values.
- All 36 have criteria, and all use the dataset as their data.
- Many claims are of absence (no effect for dmPFC, ACCg, the non-social condition, the partner monkey, and the pupil and saccade controls). Each is judged on the paper's own test.

**Details the paper leaves open, and the readings named for each:**
- **Heatmap "more clustered":** the summed stimulation-minus-sham difference inside the Face ROI or inside the Eyes ROI, each under both normalisations.
- **Per-day fixation count:** day total, or mean per session.
- **"diff" in the face-looking durations:** the median over days of the day differences, or their mean.
- **41% and 86% of trials:** averaged over all 81 days, or over the 27 OFC days.
- **Mouth bootstrap p-value:** one-sided or two-sided (no code for it).
- **Slope permutation p-value:** one-sided in the observed direction, as the code does for Fig. 5G, or two-sided.
- **Causal decomposition:** the paper doesn't give the gap-filling smoothing or the decomposition settings. Reading (a) uses settings guessed from the output folder name (noise 0.2, 1,000 ensembles, 150 bins); reading (b) uses the defaults of the original authors' code. Linear interpolation over gaps is a standard choice I named, not one the paper makes.
- **Fig. S4B comparisons:** the four single-factor pairs, or all six pairs.
- **"76 of 81 days with at least 90 stimulations":** counted among analysed trials, or among all delivered.
- **Partner reciprocation latency:** timed from the start of M1's look, or from the trial time.
- **Trigger-fixation duration and fixation counts:** M1-only events, or M1-only plus mutual.
- **"Positive slope on average":** mean or median, and combined hemifields or each hemifield.

**Gaps in the paper itself:**
- The Eyes ROI padding value is missing from the text ("adding a padding of to the center of each eye").
- The repository has no code for the Mouth-stimulation analysis, the partner-monkey latencies, the contralateral-versus-ipsilateral test, or the causal decomposition run.
- The Methods put the middle monitor at 36 cm, but the code converts pixels to degrees with 50 cm. This changes no rank test.
- The Fig. S4F legend shows a "* p < 0.05" key, while the Results give p = 0.455; I used the Results value.

## End of run

54 turns, 8 minutes, result: success.
