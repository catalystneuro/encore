# 000959 · claims-check · run 39870437751

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
ls claims/000959/ paper/; grep -n "Reader" -A40 docs/protocol.md | head -120
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -n 76,200p docs/protocol.md; python tools/claims_check.py claims/000959/10.1016-j.neuron.2024.05.004.yaml paper/10.1016-j.neuron.2024.05.004.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cat claims/000959/10.1016-j.neuron.2024.05.004.yaml
```

```
<persisted-output>
Output too large (59.2KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/ddb6d341-eefa-49d6-9818-d26b052861da/tool-results/bpo5zinnt.txt

Preview (first 2KB):
# Claims for Fan, Dal Monte, Nair, Fagan & Chang (2024) on dandiset 000959.
# Written by an agent (model "claude-opus-5-5", Claude Code in GitHub Actions), 2026-10-22,
# protocol pilot-10 as stated in docs/protocol.md.
#
# Text read: the accepted author manuscript in PubMed Central (PMC11309918, NIHMS1994226),
# main text, figure legends and STAR Methods, with its one supplement
# (NIHMS1994226-supplement-1.pdf, Table S1 and the legends of Figures S1 to S4). The version of
# record (Neuron 112(15) 2631-2644.e6) was not read. The Results point to "Supplementary
# Results" for the Mouth stimulation experiments and the post-gaze window; the supplement holds
# no such section, and these results are given in the STAR Methods of the manuscript
# ("Gaze distance analyses" and "Gaze distance analyses (Mouth stimulation)"), which were read.
#
# Code read: github.com/changlabneuro/microstim-ofc-social-attention, commit cc0bf994 (2024-10-15),
# the analysis code named in Data and code availability (also Zenodo doi:10.5281/zenodo.11110139).
# It holds MATLAB scripts for every analysis of the paper ("Scripts for social attention":
# Get data, Overall gaze behavior and number of stims, Heatmap, Spatial dimension, Temporal
[... 12 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "claims/000959/10.1016-j.neuron.2024.05.004.yaml"
}
```

```
1	# Claims for Fan, Dal Monte, Nair, Fagan & Chang (2024) on dandiset 000959.
2	# Written by an agent (model "claude-opus-5-5", Claude Code in GitHub Actions), 2026-10-22,
3	# protocol pilot-10 as stated in docs/protocol.md.
4	#
5	# Text read: the accepted author manuscript in PubMed Central (PMC11309918, NIHMS1994226),
6	# main text, figure legends and STAR Methods, with its one supplement
7	# (NIHMS1994226-supplement-1.pdf, Table S1 and the legends of Figures S1 to S4). The version of
8	# record (Neuron 112(15) 2631-2644.e6) was not read. The Results point to "Supplementary
9	# Results" for the Mouth stimulation experiments and the post-gaze window; the supplement holds
10	# no such section, and these results are given in the STAR Methods of the manuscript
11	# ("Gaze distance analyses" and "Gaze distance analyses (Mouth stimulation)"), which were read.
12	#
13	# Code read: github.com/changlabneuro/microstim-ofc-social-attention, commit cc0bf994 (2024-10-15),
14	# the analysis code named in Data and code availability (also Zenodo doi:10.5281/zenodo.11110139).
15	# It holds MATLAB scripts for every analysis of the paper ("Scripts for social attention":
16	# Get data, Overall gaze behavior and number of stims, Heatmap, Spatial dimension, Temporal
17	# dimension, Inter-individual dynamics, Saccade kinematics) and older scripts (stim/, script/).
18	# It starts from intermediate files (fixation events, ROIs, positions, stimulation and sham
19	# times) made by an upstream pipeline that is not in the repository, and it calls functions
20	# of outside packages (bfw, shared_utils, dsp3). The causal decomposition itself was run
[... 1111 more lines not kept]
```

**Agent calls Bash**

```bash
wc -l paper/*.txt; ls -la paper/
```

Result: not kept, because it reads the paper's text.

**Agent**

The checker passes (36 claims, 0 problems). Now reading the paper text to check each claim.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1016-j.neuron.2024.05.004.txt",
 "limit": 400
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1016-j.neuron.2024.05.004.txt",
 "offset": 400,
 "limit": 450
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1016-j.neuron.2024.05.004.txt",
 "offset": 850,
 "limit": 430
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
awk 'NR>=1 && NR<=399' paper/10.1016-j.neuron.2024.05.004.txt | awk '{print NR": "$0}' | cut -c1-3000 | head -c 60000
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd paper; awk 'NR>=33 && NR<=110' 10.1016-j.neuron.2024.05.004.txt | fold -w 4000
```

```
<persisted-output>
Output too large (29.7KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/ddb6d341-eefa-49d6-9818-d26b052861da/tool-results/bfxr2xyab.txt

Preview (first 2KB):
Summary

Neurons from multiple prefrontal areas encode several key variables of social gaze interaction. To explore the causal roles of the primate prefrontal cortex in real-life gaze interaction, we applied weak closed-loop microstimulations that were precisely triggered by specific social gaze events. Microstimulations of the orbitofrontal cortex, but not the dorsomedial prefrontal cortex or the anterior cingulate cortex, enhanced momentary dynamic social attention in the spatial dimension by decreasing distance of fixations relative to partner’s eyes and in the temporal dimension by reducing the inter-looking interval and the latency to reciprocate other’s directed gaze. By contrast, on a longer timescale, microstimulations of the dorsomedial prefrontal cortex modulated inter-individual gaze dynamics relative to one’s own gaze positions. These findings demonstrate that multiple regions in the primate prefrontal cortex may serve as functionally accessible nodes in controlling different aspects of dynamic social attention and suggest their potential for a therapeutic brain interface.

Keywords: Closed-loop microstimulation, dynamic social attention, real-life social gaze interaction, naturalistic social behavior, prefrontal cortex, orbitofrontal cortex, dorsomedial prefrontal cortex, anterior cingulate cortex, nonhuman primates

eTOC Blurb

Fan and Dal Monte et al. apply closed-loop microstimulations in prefrontal areas when monkeys interact with gaze. Stimulations of orbitofrontal cortex enhance momentary spatial and temporal social attention, whereas stimulations of dorsomedial prefrontal cortex modulate inter-individual gaze dynamics. These regions causally control social attention with potential for therapeutic brain interface.

Graphical Abstract


[... 4 more lines not kept]
```

**Agent calls Bash**

```bash
fold -s -w 200 paper/10.1016-j.neuron.2024.05.004.txt | sed -n '1,/Supplement: NIHMS/p' > $TMPDIR/p.txt; wc -l $TMPDIR/p.txt; echo $TMPDIR
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/p.txt",
 "offset": 40,
 "limit": 260
}
```

```
40	inter-individual gaze dynamics relative to one’s own gaze positions. These findings demonstrate that multiple regions in the primate prefrontal cortex may serve as functionally accessible nodes in 
41	controlling different aspects of dynamic social attention and suggest their potential for a therapeutic brain interface.
42	
43	Keywords: Closed-loop microstimulation, dynamic social attention, real-life social gaze interaction, naturalistic social behavior, prefrontal cortex, orbitofrontal cortex, dorsomedial prefrontal 
44	cortex, anterior cingulate cortex, nonhuman primates
45	
46	eTOC Blurb
47	
48	Fan and Dal Monte et al. apply closed-loop microstimulations in prefrontal areas when monkeys interact with gaze. Stimulations of orbitofrontal cortex enhance momentary spatial and temporal social 
49	attention, whereas stimulations of dorsomedial prefrontal cortex modulate inter-individual gaze dynamics. These regions causally control social attention with potential for therapeutic brain 
50	interface.
51	
52	Graphical Abstract
53	
54	Introduction
55	
56	The prefrontal cortex evolved to process a wide range of information in order to adaptively guide behaviors in complex environments1. For social animals, it has been hypothesized that the prefrontal 
57	cortex, and other brain regions, prioritize social information to successfully navigate volatile social environments involving multiple conspecifics in group settings2–5. In many primate species, 
58	social gaze plays a pivotal role in conveying essential social information6, and several prefrontal brain regions are known to exhibit selective neural activity for social gaze interaction7,8. While 
59	multiple subregions in the primate temporal and posterior parietal cortices, including the gaze-following patch, have been widely implicated in the perceptual aspects of social gaze9–13, the 
[... 240 more lines not kept]
```

**Agent calls Bash**

```bash
grep -n "STAR\|Methods\|Experimental setup\|Closed-loop microstimulation protocol\|Gaze distance analyses\|Gaze latency\|Inter-individual\|Fixation density\|Saccade\|Pupil\|Quantification" $TMPDIR/p.txt | head -60
```

```
89:areas in live social gaze interaction, we applied weak, real-time, closed-loop microstimulations (75 μA, 100 Hz, 200 msec; STAR Methods; see Discussion for more information on microstimulation 
91:social gaze condition (Eyes stimulation; Fig. 1A, left; Fig. S1A; STAR Methods) or on a random dot motion (RDM) stimulus (presented on a mini monitor positioned in front of M2’s face) in the 
98:Figure 1. Experimental setup and microstimulation design.
132:microstimulation or sham; STAR Methods; Supplementary Results) in the visual space surrounding the Eyes and whole Face (union of Eyes and non-eye Face) of the partner monkey. Differences in such 
136:post-gaze epoch and the center of partner’s Eyes in the live social gaze condition (Fig. 2B, left, social gaze distance; STAR Methods) or the center of RDM stimulus in the non-social control 
170:interaction or when the stimulus had a behavioral meaning. Separate control experiments (Mouth stimulation; STAR Methods; Supplementary Results) revealed that such microstimulation effect could be 
181:to partner’s Eyes in the live social gaze condition, inter-looking interval; Fig. 3A; STAR Methods). Microstimulations of OFC decreased this inter-looking interval (Fig. 3B, p = 0.035, Wilcoxon 
204:whole Face within 5 sec after the onset of a microstimulation or sham that was triggered by fixation to partner’s Eyes (reciprocation latency; Fig. 3C; STAR Methods). On the day level, 
232:during the post-gaze epoch and controlled for saccades (Fig. 4A–B; STAR Methods). This allowed us to calculate a relative causal strength index that showed how much the gaze behaviors of one monkey 
234:stimulations (late epoch) from each day (STAR Methods). While microstimulations of OFC enhanced momentary dynamic social attention as shown in the previous sections, they did not seem to impact gaze 
236:> 0.16). Further, to examine whether inter-individual gaze dynamics were modulated by where oneself was looking in space, we correlated social gaze d
[... 11 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/p.txt",
 "offset": 374,
 "limit": 225
}
```

```
374	STAR Methods
375	RESOURCE AVAILABILITY
376	Lead contact
377	
378	Further information and requests for resources and reagents should be directed to and will be fulfilled by the lead contact, Steve W. C. Chang ([removed: an e-mail address]).
379	
380	Material availability
381	
382	This study did not generate new unique reagents.
383	
384	Data and code availability
385	
386	Behavioral and neural data presented in this paper are available through the DANDI archive (https://dandiarchive.org/dandiset/000959) and the main analysis codes are available at 
387	https://github.com/changlabneuro/microstim-ofc-social-attention.
388	
389	EXPERIMENTAL MODEL AND SUBJECT DETAILS
390	Animals
391	
392	Two adult male rhesus macaques (Macaca mulatta) were involved as stimulated monkeys (M1; monkeys L and T; both aged 10 years, weighing 15.7 kg and 14.1 kg, respectively). For each M1, unrelated 
393	monkey E (female, aged 10 years, weighing 10.9 kg) served as a partner monkey (M2). M2 was previously housed in the same colony room with M1s and other rhesus macaques and later moved to an adjacent 
[... 205 more lines not kept]
```

**Agent**

Methods read. Now checking whether the cited code is reachable, to verify the code-based method details.

**Agent calls Bash**

```bash
cd $TMPDIR && timeout 120 git clone -q https://github.com/changlabneuro/microstim-ofc-social-attention code 2>&1 | tail -3; cd code 2>/dev/null && git log -1 --format='%h %ad' && find . -name "*.m" | head -80
```

```
cc0bf99 Tue Oct 15 17:55:53 2024 -0400
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
[... 62 more lines not kept]
```

**Agent**

The code is reachable (commit cc0bf99, matching the file). Spot-checking the code details the criteria rely on.

**Agent calls Bash**

```bash
cd "$TMPDIR/code/Scripts for social attention"; ls "Get data" 2>/dev/null; ls; grep -rn "ipsi\|contra" --include=*.m . | grep -iv "plot\|title\|ylabel\|xlabel\|legend" | head -40
```

```
S1_Get_data_dot_Lynch.m
S1_Get_data_dot_Tarantino.m
S1_Get_data_gaze_Lynch.m
S1_Get_data_gaze_Tarantino.m
S2_Dot_Data_Combined.m
S2_Gaze_Data_Combined.m
S3_Basic_Dot_Matrices_Combined.m
S3_Basic_Gaze_Matrices_Combined.m
Get data
Heatmap
Inter-individual dynamics
Overall gaze behavior and number of stims
Saccade kinematics
Spatial dimension
Temporal dimension
./Spatial dimension/S2_Gaze_Stats_Basic_Behaviors_Combined.m:411:%% Comparing stim effect across contra and ipsi (paired)
./Spatial dimension/S2_Gaze_Stats_Basic_Behaviors_Combined.m:413:[p_OFC, h_OFC] = signrank(Gaze.Current_Stim.OFC.m1_distance_to_eyes_ipsi.All.mean-Gaze.Current_Sham.OFC.m1_distance_to_eyes_ipsi.All.mean, Gaze.Current_Stim.OFC.m1_distance_to_eyes_contra.All.mean-Gaze.Current_Sham.OFC.m1_distance_to_eyes_contra.All.mean);
./Spatial dimension/S2_Gaze_Stats_Basic_Behaviors_Combined.m:414:[p_dmPFC, h_dmPFC] = signrank(Gaze.Current_Stim.dmPFC.m1_distance_to_eyes_ipsi.All.mean-Gaze.Current_Sham.dmPFC.m1_distance_to_eyes_ipsi.All.mean, Gaze.Current_Stim.dmPFC.m1_distance_to_eyes_contra.All.mean-Gaze.Current_Sham.dmPFC.m1_distance_to_eyes_contra.All.mean);
./Spatial dimension/S2_Gaze_Stats_Basic_Behaviors_Combined.m:415:[p_ACCg, h_ACCg] = signrank(Gaze.Current_Stim.ACCg.m1_distance_to_eyes_ipsi.All.mean-Gaze.Current_Sham.ACCg.m1_distance_to_eyes_ipsi.All.mean, Gaze.Current_Stim.ACCg.m1_distance_to_eyes_contra.All.mean-Gaze.Current_Sham.ACCg.m1_distance_to_eyes_contra.All.mean);
./Spatial dimension/S2_Gaze_Stats_Basic_Behaviors_Combined.m:417:[p_OFC_Lynch, h_OFC_Lynch] = signrank(Gaze.Current_Stim.OFC.m1_distance_to_eyes_ipsi.Lynch.mean-Gaze.Current_Sham.OFC.m1_distance_to_eyes_ipsi.Lynch.mean, Gaze.Current_Stim.OFC.m1_distance_to_eyes_contra.Lynch.mean-Gaze.Current_Sham.OFC.m1_distance_to_eyes_contra.Lynch.mean);
[... 36 more lines not kept]
```

**Agent calls Bash**

```bash
cd "$TMPDIR/code/Scripts for social attention/Get data"; wc -l *.m; grep -n "ipsi\|contra\|face_center\|center\|previous\|-1)\|end-5000\|5000\|stim_times\|sham" S1_Get_data_gaze_Lynch.m | head -60
```

```
326 S1_Get_data_dot_Lynch.m
   326 S1_Get_data_dot_Tarantino.m
   384 S1_Get_data_gaze_Lynch.m
   384 S1_Get_data_gaze_Tarantino.m
    52 S2_Dot_Data_Combined.m
    20 S2_Gaze_Data_Combined.m
   722 S3_Basic_Dot_Matrices_Combined.m
  1463 S3_Basic_Gaze_Matrices_Combined.m
  3677 total
87:        % Get the center of ROI for eyes
88:        center_roi_m1_eyes=[(roi_m1_eyes(1)+roi_m1_eyes(3))/2 (roi_m1_eyes(2)+roi_m1_eyes(4))/2];
89:        center_roi_m2_eyes=[(roi_m2_eyes(1)+roi_m2_eyes(3))/2 (roi_m2_eyes(2)+roi_m2_eyes(4))/2];
91:        GazeData.(field_id).(run_id).center_roi_m1_eyes=center_roi_m1_eyes;
92:        GazeData.(field_id).(run_id).center_roi_m2_eyes=center_roi_m2_eyes;
105:        % Get the center of ROI for mouth
106:        center_roi_m1_mouth=[(roi_m1_mouth(1)+roi_m1_mouth(3))/2 (roi_m1_mouth(2)+roi_m1_mouth(4))/2];
107:        center_roi_m2_mouth=[(roi_m2_mouth(1)+roi_m2_mouth(3))/2 (roi_m2_mouth(2)+roi_m2_mouth(4))/2];
109:        GazeData.(field_id).(run_id).center_roi_m1_mouth=center_roi_m1_mouth;
110:        GazeData.(field_id).(run_id).center_roi_m2_mouth=center_roi_m2_mouth;
123:        % Get the center of ROI for face
[... 31 more lines not kept]
```

**Agent calls Bash**

```bash
cd "$TMPDIR/code/Scripts for social attention/Get data"; sed -n 140,212p S1_Get_data_gaze_Lynch.m; diff S1_Get_data_gaze_Lynch.m S1_Get_data_gaze_Tarantino.m | head -30
```

```
GazeData.(field_id).(run_id).x_m2=x_m2;
        GazeData.(field_id).(run_id).y_m2=y_m2; 
            
        % Get different types of events
        GazeData.(field_id).(run_id).labels=Gaze.(field_id).(run_id).events.labels;
        GazeData.(field_id).(run_id).events=Gaze.(field_id).(run_id).events.events;
        GazeData.(field_id).(run_id).categories=Gaze.(field_id).(run_id).events.categories;
        
        % Label contra- or ipsi- lateral for each event (Lynch's chamber is
        % on the left side of the head)

        for nevent=1:length(GazeData.(field_id).(run_id).events)

            start_idx=GazeData.(field_id).(run_id).events(nevent,1);
            end_idx=GazeData.(field_id).(run_id).events(nevent,2);
            m1_x=mean(GazeData.(field_id).(run_id).x_m1(1,start_idx:end_idx),'omitnan');
            m2_x=mean(GazeData.(field_id).(run_id).x_m2(1,start_idx:end_idx),'omitnan');
            
            if m1_x < GazeData.(field_id).(run_id).center_roi_m2_face(1)
                GazeData.(field_id).(run_id).event_info_m1(nevent,:)=table(GazeData.(field_id).(run_id).events(nevent,:),string('ipsi'));
[... 84 more lines not kept]
```

**Agent calls Bash**

```bash
cd "$TMPDIR/code/Scripts for social attention/Get data"; sed -n 60,135p S1_Get_data_gaze_Lynch.m
```

```
fieldname=fieldnames(Gaze);

for k=1:size(fieldname,1)
    field_id=char(fieldname(k));
    
    field_run=fieldnames(Gaze.(field_id));
    
    for l=1:size(field_run,1)
        
        run_id=char(field_run(l));
        
        % Get offsets
        Offsets_m1=Gaze.(field_id).(run_id).offsets.m1;
        Offsets_m2=Gaze.(field_id).(run_id).offsets.m2;
        Offsets_m2_m1=Gaze.(field_id).(run_id).offsets.m2_to_m1;
        
        % ROI info for eyes (m1 roi is m2's eyes from m1's perspective)
        roi_m1_eyes=Gaze.(field_id).(run_id).rois.m1.rects(ROI_eyes);
        roi_m2_eyes=Gaze.(field_id).(run_id).rois.m2.rects(ROI_eyes);
        roi_m1_eyes([1,3])=roi_m1_eyes([1,3])+Offsets_m1(1);
[... 57 more lines not kept]
```

**Agent calls Bash**

```bash
cd "$TMPDIR/code/Scripts for social attention/Get data"; grep -n "center_roi" S3_Basic_Gaze_Matrices_Combined.m S3_Basic_Dot_Matrices_Combined.m S1_Get_data_dot_Lynch.m | head -30; grep -n "Get the center\|roi_m1_eyes=\|rects(" S1_Get_data_dot_Lynch.m | head
```

```
S3_Basic_Gaze_Matrices_Combined.m:37:            GazeMatrices.(field_id).(run_id).center_roi_m1_eyes=GazeData.(field_id).(run_id).center_roi_m1_eyes;
S3_Basic_Gaze_Matrices_Combined.m:38:            GazeMatrices.(field_id).(run_id).center_roi_m2_eyes=GazeData.(field_id).(run_id).center_roi_m2_eyes;
S3_Basic_Gaze_Matrices_Combined.m:39:            GazeMatrices.(field_id).(run_id).center_roi_m1_face=GazeData.(field_id).(run_id).center_roi_m1_face;
S3_Basic_Gaze_Matrices_Combined.m:40:            GazeMatrices.(field_id).(run_id).center_roi_m2_face=GazeData.(field_id).(run_id).center_roi_m2_face;
S3_Basic_Gaze_Matrices_Combined.m:41:            GazeMatrices.(field_id).(run_id).center_roi_m1_mouth=GazeData.(field_id).(run_id).center_roi_m1_mouth;
S3_Basic_Gaze_Matrices_Combined.m:42:            GazeMatrices.(field_id).(run_id).center_roi_m2_mouth=GazeData.(field_id).(run_id).center_roi_m2_mouth;
S3_Basic_Gaze_Matrices_Combined.m:590:                    GazeMatrices.(field_id).(run_id).(stim_id).m1_distance_to_eyes(1,n_m1_all)=sqrt((GazeMatrices.(field_id).(run_id).(stim_id).mean_x_m1(1,n_m1_all)-GazeMatrices.(field_id).(run_id).center_roi_m1_eyes(1)).^2+(GazeMatrices.(field_id).(run_id).(stim_id).mean_y_m1(1,n_m1_all)-GazeMatrices.(field_id).(run_id).center_roi_m1_eyes(2)).^2);
S3_Basic_Gaze_Matrices_Combined.m:591:                    GazeMatrices.(field_id).(run_id).(stim_id).m1_distance_to_mouth(1,n_m1_all)=sqrt((GazeMatrices.(field_id).(run_id).(stim_id).mean_x_m1(1,n_m1_all)-GazeMatrices.(field_id).(run_id).center_roi_m1_mouth(1)).^2+(GazeMatrices.(field_id).(run_id).(stim_id).mean_y_m1(1,n_m1_all)-GazeMatrices.(field_id).(run_id).center_roi_m1_mouth(2)).^2);
S3_Basic_Gaze_Matrices_Combined.m:592:                    GazeMatrices.(field_id).(run_id).(stim_id).m1_distance_to_face(1,n_m1_all)=sqrt((GazeMatrices.(field_id).(run_id).(stim_id).mean_x_m1(1,n_m1_all)-GazeMatrices.(field_id).(run_id).center_roi_m1_face(1)).^2+(GazeMatrices.(field_id).(run_id).(stim_id).mean_y
[... 32 more lines not kept]
```

**Agent calls Bash**

```bash
cd "$TMPDIR/code/Scripts for social attention/Get data"; grep -n "center_roi_m2_face\|center_roi_m1_face\|roi_m2_face=\|roi_m2_face(\[" S1_Get_data_dot_Lynch.m S1_Get_data_dot_Tarantino.m | head; grep -n "stim_ts\|5000\|length(.*t)\|(n-1)\|nstim-1\|labels(" S3_Basic_Gaze_Matrices_Combined.m | head -40
```

```
S1_Get_data_dot_Lynch.m:114:        roi_m2_face=Dot.(field_id).(run_id).rois.m2.rects(ROI_face);
S1_Get_data_dot_Lynch.m:117:        roi_m2_face([1,3])=Offsets_m2_m1(1)-(roi_m2_face([1,3])+Offsets_m2(1));
S1_Get_data_dot_Lynch.m:118:        roi_m2_face([2,4])=roi_m2_face([2,4])+Offsets_m2(2);
S1_Get_data_dot_Lynch.m:121:        DotData.(field_id).(run_id).roi_m2_face=roi_m2_face;
S1_Get_data_dot_Lynch.m:124:        center_roi_m1_face=[(roi_m1_face(1)+roi_m1_face(3))/2 (roi_m1_face(2)+roi_m1_face(4))/2];
S1_Get_data_dot_Lynch.m:125:        center_roi_m2_face=[(roi_m2_face(1)+roi_m2_face(3))/2 (roi_m2_face(2)+roi_m2_face(4))/2];
S1_Get_data_dot_Lynch.m:127:        DotData.(field_id).(run_id).center_roi_m1_face=center_roi_m1_face;
S1_Get_data_dot_Lynch.m:128:        DotData.(field_id).(run_id).center_roi_m2_face=center_roi_m2_face;
S1_Get_data_dot_Lynch.m:151:            if m1_x < DotData.(field_id).(run_id).center_roi_m2_face(1)
S1_Get_data_dot_Lynch.m:153:            elseif m1_x > DotData.(field_id).(run_id).center_roi_m2_face(1)
46:            stim_ts=GazeData.(field_id).(run_id).stim_ts;
48:            for nstim=1:length(stim_ts)        
51:                if GazeData.(field_id).(run_id).stim_ts(nstim) >= min(GazeData.(field_id).(run_id).t) && GazeData.(field_id).(run_id).stim_ts(nstim) < max(GazeData.(field_id).(run_id).t)-5
59:                GazeMatrices.(field_id).(run_id).stim_time=vertcat(GazeMatrices.(field_id).(run_id).stim_time, GazeData.(field_id).(run_id).stim_ts(nstim,1));
63:                fixation_m1_eye_idx=find(GazeData.(field_id).(run_id).m1_eye.Var1(:,11)>=stim_ts(nstim)+look_back & GazeData.(field_id).(run_id).m1_eye.Var1(:,11)<stim_ts(nstim)+look_ahead);
90:                fixation_m1_eye_ipsi_idx=find(GazeData.(field_id).(run_id).m1_eye.Var1(:,11)>=stim_ts(nstim)+look_back & GazeData.(field_id).(run_id).m1_eye.Var1(:,11)<stim_ts(nstim)+look_ahead & GazeData.(field_id).(run_id).m1_eye.Var2=='ipsi');
117:                fixation_m1_eye_contra_id
[... 34 more lines not kept]
```

**Agent calls Bash**

```bash
cd "$TMPDIR/code/Scripts for social attention/Get data"; sed -n 20,62p S3_Basic_Gaze_Matrices_Combined.m; grep -n "all_stim_labels\|stim_id\s*=" S3_Basic_Gaze_Matrices_Combined.m | head
```

```
fieldname=fieldnames(GazeData);

    for k=1:size(fieldname,1)
        field_id=char(fieldname(k));    
        field_run=fieldnames(GazeData.(field_id));
        
        for l=1:size(field_run,1)
            run_id=char(field_run(l));
            
            % get ROI info
            GazeMatrices.(field_id).(run_id).roi_m1_eyes=GazeData.(field_id).(run_id).roi_m1_eyes;
            GazeMatrices.(field_id).(run_id).roi_m2_eyes=GazeData.(field_id).(run_id).roi_m2_eyes;
            GazeMatrices.(field_id).(run_id).roi_m1_face=GazeData.(field_id).(run_id).roi_m1_face;
            GazeMatrices.(field_id).(run_id).roi_m2_face=GazeData.(field_id).(run_id).roi_m2_face;
            GazeMatrices.(field_id).(run_id).roi_m1_mouth=GazeData.(field_id).(run_id).roi_m1_mouth;
            GazeMatrices.(field_id).(run_id).roi_m2_mouth=GazeData.(field_id).(run_id).roi_m2_mouth;
    
            GazeMatrices.(field_id).(run_id).center_roi_m1_eyes=GazeData.(field_id).(run_id).center_roi_m1_eyes;
            GazeMatrices.(field_id).(run_id).center_roi_m2_eyes=GazeData.(field_id).(run_id).center_roi_m2_eyes;
            GazeMatrices.(field_id).(run_id).center_roi_m1_face=GazeData.(field_id).(run_id).center_roi_m1_face;
[... 26 more lines not kept]
```

**Agent calls Bash**

```bash
cd "$TMPDIR/code/Scripts for social attention"; grep -rn "previous_label\|current_label\|Current_Stim\b\|Previous" "Spatial dimension/S1_Gaze_Results_Combined.m" | head -20; sed -n 1,60p "Spatial dimension/S1_Gaze_Results_Combined.m"
```

```
50:            if isequal(GazeMatrices.(field_id).(run_id).current_label(nstim,:),'sham') && isequal(GazeMatrices.(field_id).(run_id).current_label(nstim-1,:),'sham')                    
52:            elseif isequal(GazeMatrices.(field_id).(run_id).current_label(nstim,:),'stim') && isequal(GazeMatrices.(field_id).(run_id).current_label(nstim-1,:),'sham')     
54:            elseif isequal(GazeMatrices.(field_id).(run_id).current_label(nstim,:),'sham') && isequal(GazeMatrices.(field_id).(run_id).current_label(nstim-1,:),'stim')      
56:            elseif isequal(GazeMatrices.(field_id).(run_id).current_label(nstim,:),'stim') && isequal(GazeMatrices.(field_id).(run_id).current_label(nstim-1,:),'stim')   
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
[... 45 more lines not kept]
```

**Agent calls Bash**

```bash
cd "$TMPDIR/code/Scripts for social attention/Get data"; sed -n 270,384p S1_Get_data_gaze_Lynch.m
```

```
m2_neface_ind = m2_mouth_ind | m2_nenmface_ind;
            m2_wholeface_ind = m2_eye_ind | m2_mouth_ind | m2_nenmface_ind;
            m2_all_ind = m2_eye_ind | m2_mouth_ind | m2_nenmface_ind | m2_everywhere_ind;
            
            % mutual events
            mutual_eye_ind = mutual_ind & eye_ind & non_nan_ind;
            mutual_mouth_ind = mutual_ind & mouth_ind & non_nan_ind;
            mutual_face_ind = mutual_ind & face_ind & non_nan_ind;
            mutual_wholeface_ind = mutual_eye_ind | mutual_mouth_ind | mutual_face_ind;
    
            % Events
            
            % exclulsive m1 events (use ipsi/contra label from m1's perspective)
            GazeData.(field_id).(run_id).m1_eye=GazeData.(field_id).(run_id).event_info_m1(m1_eye_ind,:);
            GazeData.(field_id).(run_id).m1_mouth=GazeData.(field_id).(run_id).event_info_m1(m1_mouth_ind,:);
            GazeData.(field_id).(run_id).m1_nenmface=GazeData.(field_id).(run_id).event_info_m1(m1_nenmface_ind,:);
            GazeData.(field_id).(run_id).m1_everywhere=GazeData.(field_id).(run_id).event_info_m1(m1_everywhere_ind,:);
    
            GazeData.(field_id).(run_id).m1_neface=GazeData.(field_id).(run_id).event_info_m1(m1_neface_ind,:);
            GazeData.(field_id).(run_id).m1_wholeface=GazeData.(field_id).(run_id).event_info_m1(m1_wholeface_ind,:);
[... 94 more lines not kept]
```

**Agent calls Bash**

```bash
cd "$TMPDIR/code/Scripts for social attention/Get data"; sed -n 225,270p S1_Get_data_gaze_Lynch.m; sed -n 556,600p S3_Basic_Gaze_Matrices_Combined.m
```

```
fieldname=fieldnames(GazeData);

    for k=1:size(fieldname,1)
        field_id=char(fieldname(k));    
        field_run=fieldnames(GazeData.(field_id));
        
        for l=1:size(field_run,1)
            run_id=char(field_run(l));
            
            % get indices of all types of events
            labels= GazeData.(field_id).(run_id).labels;
            event_label_column_names = GazeData.(field_id).(run_id).categories;
            roi_ind = strcmp( event_label_column_names, 'roi' );
            looks_by_ind = strcmp( event_label_column_names, 'looks_by' );
            m1_ind = strcmp( labels(:, looks_by_ind), 'm1' );
            m2_ind = strcmp( labels(:, looks_by_ind), 'm2' );
            mutual_ind = strcmp( labels(:, looks_by_ind), 'mutual' );
    
            % eye_ind is eyes
            eye_ind = strcmp( labels(:, roi_ind), 'eyes_nf' );
[... 71 more lines not kept]
```

**Agent calls Bash**

```bash
cd "$TMPDIR/code/Scripts for social attention/Temporal dimension"; grep -n "mutual\|m1_wholeface\|5000\|5)\|look_ahead\|NaN\|min(" "Inter-looking interval/S1_Gaze_M1_Latency_Combined.m" | head -30; grep -n "mutual\|wholeface\|all_face\|5\b\|NaN" "Reciprocation latency/S1_Gaze_ITI_Combined.m" | head -40
```

```
23:        [sorted_start_time_eyes,sorted_order_eyes]=sort(vertcat(GazeData.(field_id).(run_id).m1_eye.Var1(:,7),GazeData.(field_id).(run_id).mutual_eye.Var1(:,7)));
24:        [sorted_start_time_mouth,sorted_order_mouth]=sort(vertcat(GazeData.(field_id).(run_id).m1_mouth.Var1(:,7),GazeData.(field_id).(run_id).mutual_mouth.Var1(:,7)));
25:        [sorted_start_time_wholeface,sorted_order_wholeface]=sort(vertcat(GazeData.(field_id).(run_id).m1_wholeface.Var1(:,7),GazeData.(field_id).(run_id).mutual_wholeface.Var1(:,7)));
30:            if GazeData.(field_id).(run_id).stim_ts(nstim) >= min(GazeData.(field_id).(run_id).t) && GazeData.(field_id).(run_id).stim_ts(nstim) < max(GazeData.(field_id).(run_id).t)-5
42:                    m1_behavior.(field_id).(run_id).(stim_id).m1_latency_eyes=NaN;
49:                    m1_behavior.(field_id).(run_id).(stim_id).m1_latency_mouth=NaN;
56:                    m1_behavior.(field_id).(run_id).(stim_id).m1_latency_face=NaN;
18:        sorted_events.all_face.(field_id).(run_id).stim_ts=GazeData.(field_id).(run_id).stim_ts;
19:        sorted_events.all_face.(field_id).(run_id).all_stim_labels=GazeData.(field_id).(run_id).all_stim_labels;
20:        sorted_events.all_face.(field_id).(run_id).t=GazeData.(field_id).(run_id).t;
28:        m1_start_time.whole_face=GazeData.(field_id).(run_id).m1_wholeface.Var1(:,7);
29:        m1_end_time.whole_face=GazeData.(field_id).(run_id).m1_wholeface.Var1(:,8);   
32:        m2_start_time.whole_face=GazeData.(field_id).(run_id).m2_wholeface.Var1(:,9);
33:        m2_end_time.whole_face=GazeData.(field_id).(run_id).m2_wholeface.Var1(:,10);
48:        % combine m1 whole face and m2 whole face and mutual whole face
49:        m1_start_time.all_face=vertcat(GazeData.(field_id).(run_id).m1_wholeface.Var1(:,7), GazeData.(field_id).(run_id).mutual_wholeface.Var1(:,7));
50:        m1_end_time.all_face=vertcat(GazeData.(field_id).(run_id).m1_wholeface.Var1(:,8), GazeData.(field_id).(run_id).mutual_wholeface.
[... 31 more lines not kept]
```

**Agent calls Bash**

```bash
cd "$TMPDIR/code/Scripts for social attention/Temporal dimension"; sed -n 26,62p "Inter-looking interval/S1_Gaze_M1_Latency_Combined.m"; sed -n 100,118p "Reciprocation latency/S1_Gaze_ITI_Combined.m"; sed -n 160,240p "Reciprocation latency/S1_Gaze_ITI_Combined.m"
```

```
for nstim=1:length(GazeData.(field_id).(run_id).stim_ts)        
            stim_id=char(strcat('stim_',num2str(nstim)));
        
            if GazeData.(field_id).(run_id).stim_ts(nstim) >= min(GazeData.(field_id).(run_id).t) && GazeData.(field_id).(run_id).stim_ts(nstim) < max(GazeData.(field_id).(run_id).t)-5
                
                m1_behavior.(field_id).(run_id).stim_ts=[m1_behavior.(field_id).(run_id).stim_ts GazeData.(field_id).(run_id).stim_ts(nstim)];
                m1_behavior.(field_id).(run_id).all_stim_labels=[m1_behavior.(field_id).(run_id).all_stim_labels GazeData.(field_id).(run_id).all_stim_labels(nstim)];

                stim_idx_start=find(GazeData.(field_id).(run_id).t<=GazeData.(field_id).(run_id).stim_ts(nstim),1,'last');
                stim_idx_end=stim_idx_start+time_window*1000-1;

                m1_first_looking_eyes=sorted_start_time_eyes(find(sorted_start_time_eyes>stim_idx_start,1,'first'));
                if m1_first_looking_eyes<stim_idx_end
                    m1_behavior.(field_id).(run_id).(stim_id).m1_latency_eyes=m1_first_looking_eyes-stim_idx_start;
                else
                    m1_behavior.(field_id).(run_id).(stim_id).m1_latency_eyes=NaN;
                end

                m1_first_looking_mouth=sorted_start_time_mouth(find(sorted_start_time_mouth>stim_idx_start,1,'first'));
                if m1_first_looking_mouth<stim_idx_end
[... 117 more lines not kept]
```

**Agent calls Bash**

```bash
cd "$TMPDIR/code/Scripts for social attention"; grep -n "all_face\|whole_face" "Temporal dimension/Reciprocation latency/S2_Gaze_ITI_Stats_Combined.m" "Temporal dimension/Reciprocation latency/S3_Gaze_ITI_Across_Trials.m" | head -8; grep -n "08122019\|12222021\|11052021\|12172021\|11042021\|90\|45" "Inter-individual dynamics/Epoch/S1_Gaze_Time_Epoch.m" | head -20
```

```
Temporal dimension/Reciprocation latency/S2_Gaze_ITI_Stats_Combined.m:52:ROI={'whole_face','all_face'};
Temporal dimension/Reciprocation latency/S2_Gaze_ITI_Stats_Combined.m:162:ROI={'whole_face','all_face'};
Temporal dimension/Reciprocation latency/S2_Gaze_ITI_Stats_Combined.m:275:fieldname=fieldnames(ITI_Day.all_face);
Temporal dimension/Reciprocation latency/S2_Gaze_ITI_Stats_Combined.m:280:    number_stim_total(1,k)=length(ITI_Day.all_face.(field_id).current_stim.average_iti);
Temporal dimension/Reciprocation latency/S2_Gaze_ITI_Stats_Combined.m:281:    number_stim_nonNaN(1,k)=sum(~isnan(ITI_Day.all_face.(field_id).current_stim.average_iti));
Temporal dimension/Reciprocation latency/S2_Gaze_ITI_Stats_Combined.m:283:    number_sham_total(1,k)=length(ITI_Day.all_face.(field_id).current_sham.average_iti);
Temporal dimension/Reciprocation latency/S2_Gaze_ITI_Stats_Combined.m:284:    number_sham_nonNaN(1,k)=sum(~isnan(ITI_Day.all_face.(field_id).current_sham.average_iti));
Temporal dimension/Reciprocation latency/S2_Gaze_ITI_Stats_Combined.m:293:fieldname=fieldnames(iti.all_face);
1:%% Divide time into early (1-45) and late (46-90) epoches
97:% 76 days with more than 90 stims 
98:% Five days excluded: 08122019 OFC Lynch, 11042021 Tarantino ACCg, 11052021 Tarantino dmPFC, 12172021 Tarantino dmPFC, 12222021 Tarantino OFC)
100:%% Put information together for each time bin (1-45, 46-90 stims)
103:time_bin={'stim_1_45','stim_46_90'};
132:    if number_stim>=90
136:            if count_stim<=45
139:                    Decomp_Temporal.(field_id).stim_1_45.stim.stim_time=[Decomp_Temporal.(field_id).stim_1_45.stim.stim_time Decomp_day.(field_id).stim_time(1,ntrial)];
140:                    Decomp_Temporal.(field_id).stim_1_45.stim.current_label=[Decomp_Temporal.(field_id).stim_1_45.stim.current_label,{Decomp_day.(field_id).current_label(1,ntrial)}];
141:                    Decomp_Temporal.(field_id).stim_1_45.stim.m1_distance_to_eyes_contra=[Decomp_Temporal.(field_id).stim_1
[... 11 more lines not kept]
```

**Agent calls Bash**

```bash
cd "$TMPDIR/code/Scripts for social attention/Inter-individual dynamics/Epoch"; sed -n 104,137p S1_Gaze_Time_Epoch.m; grep -n "fitlm\|signrank\|sham\|stim\.\|deg\|pix" S3_Gaze_Correlation_by_Epoch.m | head -30
```

```
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
[... 44 more lines not kept]
```

**Agent calls Bash**

```bash
cd "$TMPDIR/code/Scripts for social attention/Inter-individual dynamics/Epoch"; wc -l *.m; sed -n 1,23p S3_Gaze_Correlation_by_Epoch.m; sed -n 69,200p S3_Gaze_Correlation_by_Epoch.m | grep -v "^\s*$" | head -90
```

```
251 S1_Gaze_Time_Epoch.m
  298 S2_Gaze_CDI_by_Epoch.m
  883 S3_Gaze_Correlation_by_Epoch.m
 1432 total
%% Calculate correlation between causal index and distance to eyes for stim in late and early epoches

% Upload Decomp_Temporal_Combined.mat and Decomp_Temporal_shuffled_Combined.mat 

h = 27; % monitor height in cm
d = 50; % subject to monitor in cm
r=768; % monitor height in pixel

deg_per_px = rad2deg(atan2(.5*h, d)) / (.5*r); 
px_per_deg = 1/deg_per_px;

fieldname=fieldnames(Decomp_Temporal_shuffled);
time_bin={'stim_1_45','stim_46_90'};

for k=1:size(fieldname,1)
    field_id=char(fieldname(k));
[... 98 more lines not kept]
```

**Agent calls Bash**

```bash
cd "$TMPDIR/code/Scripts for social attention/Inter-individual dynamics"; grep -rn "randperm\|shuffle\|_null\b\|eyes_null" --include=*.m . | grep -v "^\S*:\s*%" | head -20
```

```
./Epoch/S3_Gaze_Correlation_by_Epoch.m:12:fieldname=fieldnames(Decomp_Temporal_shuffled);
./Epoch/S3_Gaze_Correlation_by_Epoch.m:50:            [Corr_combined_stim_shuffled.(field_id).(bin_id).distance.rho(rep), Corr_combined_stim_shuffled.(field_id).(bin_id).distance.p(rep)]=corr(deg_per_px*Decomp_Temporal_shuffled.(field_id).(bin_id).stim.m1_distance_to_eyes(rep,:)',Decomp_Temporal_shuffled.(field_id).(bin_id).stim.causal_m1m2_eyes_null(rep,:)','Type','Spearman','Rows','pairwise');
./Epoch/S3_Gaze_Correlation_by_Epoch.m:51:            [Corr_combined_stim_shuffled.(field_id).(bin_id).ipsi.rho(rep), Corr_combined_stim_shuffled.(field_id).(bin_id).ipsi.p(rep)]=corr(deg_per_px*Decomp_Temporal_shuffled.(field_id).(bin_id).stim.m1_distance_to_eyes_ipsi(rep,:)',Decomp_Temporal_shuffled.(field_id).(bin_id).stim.causal_m1m2_eyes_null(rep,:)','Type','Spearman','Rows','pairwise');
./Epoch/S3_Gaze_Correlation_by_Epoch.m:52:            [Corr_combined_stim_shuffled.(field_id).(bin_id).contra.rho(rep), Corr_combined_stim_shuffled.(field_id).(bin_id).contra.p(rep)]=corr(deg_per_px*Decomp_Temporal_shuffled.(field_id).(bin_id).stim.m1_distance_to_eyes_contra(rep,:)',Decomp_Temporal_shuffled.(field_id).(bin_id).stim.causal_m1m2_eyes_null(rep,:)','Type','Spearman','Rows','pairwise');
./Epoch/S3_Gaze_Correlation_by_Epoch.m:54:            mdl_stim_distance_shuffled.(bin_id)=fitlm(deg_per_px*Decomp_Temporal_shuffled.(field_id).(bin_id).stim.m1_distance_to_eyes(rep,:)',Decomp_Temporal_shuffled.(field_id).(bin_id).stim.causal_m1m2_eyes_null(rep,:)');
./Epoch/S3_Gaze_Correlation_by_Epoch.m:55:            mdl_stim_ipsi_shuffled.(bin_id)=fitlm(deg_per_px*Decomp_Temporal_shuffled.(field_id).(bin_id).stim.m1_distance_to_eyes_ipsi(rep,:)',Decomp_Temporal_shuffled.(field_id).(bin_id).stim.causal_m1m2_eyes_null(rep,:)');
./Epoch/S3_Gaze_Correlation_by_Epoch.m:56:            mdl_stim_contra_shuffled.(bin_id)=fitlm(deg_per_px*Decomp_Temporal_shuffled.(field_id).(bin_id).stim.m1_distance_to_eyes_con
[... 14 more lines not kept]
```

**Agent calls Bash**

```bash
cd "$TMPDIR/code/Scripts for social attention/Inter-individual dynamics/Epoch"; grep -n "signrank\|median\|sum(.*>\|sum(.*<\|/1000\|p_perm\|permut" S3_Gaze_Correlation_by_Epoch.m | head -30; grep -n "sum(.*>\|sum(.*<\|/1000\|permut\|median" "../../Saccade kinematics/S6_Gaze_Saccade_Kinematics_Combined.m" | head
```

```
230:        [Stats.p.(monkey_id).OFC.stim.(distance_id).rho, Stats.h.(monkey_id).OFC.stim.(distance_id).rho] = signrank(OFC.(monkey_id).stim_late.(distance_id).rho, OFC.(monkey_id).stim_early.(distance_id).rho);
231:        [Stats.p.(monkey_id).OFC.stim.(distance_id).p, Stats.h.(monkey_id).OFC.stim.(distance_id).p] = signrank(OFC.(monkey_id).stim_late.(distance_id).p, OFC.(monkey_id).stim_early.(distance_id).p);
232:        [Stats.p.(monkey_id).OFC.stim.(distance_id).slope, Stats.h.(monkey_id).OFC.stim.(distance_id).slope] = signrank(OFC.(monkey_id).stim_late.(distance_id).slope, OFC.(monkey_id).stim_early.(distance_id).slope);
234:        [Stats.p.(monkey_id).OFC.sham.(distance_id).rho, Stats.h.(monkey_id).OFC.sham.(distance_id).rho] = signrank(OFC.(monkey_id).sham_late.(distance_id).rho, OFC.(monkey_id).sham_early.(distance_id).rho);
235:        [Stats.p.(monkey_id).OFC.sham.(distance_id).p, Stats.h.(monkey_id).OFC.sham.(distance_id).p] = signrank(OFC.(monkey_id).sham_late.(distance_id).p, OFC.(monkey_id).sham_early.(distance_id).p);
236:        [Stats.p.(monkey_id).OFC.sham.(distance_id).slope, Stats.h.(monkey_id).OFC.sham.(distance_id).slope] = signrank(OFC.(monkey_id).sham_late.(distance_id).slope, OFC.(monkey_id).sham_early.(distance_id).slope);
238:        Epoch_results.(monkey_id).OFC.stim.(distance_id).rho = median(OFC.(monkey_id).stim_late.(distance_id).rho-OFC.(monkey_id).stim_early.(distance_id).rho,'omitnan');
239:        Epoch_results.(monkey_id).OFC.stim.(distance_id).p = median(OFC.(monkey_id).stim_late.(distance_id).p-OFC.(monkey_id).stim_early.(distance_id).p,'omitnan');
240:        Epoch_results.(monkey_id).OFC.stim.(distance_id).slope = median(OFC.(monkey_id).stim_late.(distance_id).slope-OFC.(monkey_id).stim_early.(distance_id).slope,'omitnan');
242:        Epoch_results.(monkey_id).OFC.stim.(distance_id).rho_shuffled = median(OFC.(monkey_id).stim_late.(distance_id).rho_shuffled-OFC.(monkey_id).stim_early.(distance_id).rho_shuffled,2,'omitnan');
[... 31 more lines not kept]
```

**Agent calls Bash**

```bash
cd "$TMPDIR/code"; diff -q stim/S5_Pupil_Size.m "Scripts for social attention/Saccade kinematics/S5_Pupil_Size.m"; grep -n "700\|signrank\|fdr\|whole\|face\|10)" "Scripts for social attention/Saccade kinematics/S5_Pupil_Size.m" | head -20
```

```
78:face_rois = nan( rows(eyes_tbl), 4 );
102:  face_rois(i, :) = int_tbl.m1_rois{mi}.rects('face');
117:accept_within_face = false( size(fix_traces, 1), 1 );
122:  ib = shared_utils.rect.inside( face_rois(i, :), x, y );
123:  accept_within_face(i) = all( ib(t_subset) );
168:ok_traces = accept_within_face;
198:  stats.ps(i, :) = arrayfun( @(x) signrank(...
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd "$TMPDIR/code/Scripts for social attention/Overall gaze behavior and number of stims"; grep -n "fdr\|signrank\|ranksum\|mean(\|sum(" S3_Stats_ROI_number_duration_final.m S1_Total_Number_of_Stim_Combined.m | head -30; grep -n "mean(\|sum(\|length(" S2_Gaze_ROI_number_duration_Combined.m | head -12
```

```
S3_Stats_ROI_number_duration_final.m:100:    [Stats.All_day.(monkey_id).total_number.eye_neface_p,Stats.All_day.(monkey_id).total_number.eye_neface_h]=signrank(Gaze_summary.All_day.(monkey_id).m1_eye.total_number,Gaze_summary.All_day.(monkey_id).m1_neface.total_number);
S3_Stats_ROI_number_duration_final.m:101:    [Stats.All_day.(monkey_id).total_number.eye_dot_p,Stats.All_day.(monkey_id).total_number.eye_dot_h]=signrank(Gaze_summary.All_day.(monkey_id).m1_eye.total_number,Dot_summary.All_day.(monkey_id).m1_eye.total_number);
S3_Stats_ROI_number_duration_final.m:103:    [Stats.All_day.(monkey_id).average_duration.eye_neface_p,Stats.All_day.(monkey_id).average_duration.eye_neface_h]=signrank(Gaze_summary.All_day.(monkey_id).m1_eye.average_duration,Gaze_summary.All_day.(monkey_id).m1_neface.average_duration);
S3_Stats_ROI_number_duration_final.m:104:    [Stats.All_day.(monkey_id).average_duration.eye_dot_p,Stats.All_day.(monkey_id).average_duration.eye_dot_h]=signrank(Gaze_summary.All_day.(monkey_id).m1_eye.average_duration,Dot_summary.All_day.(monkey_id).m1_eye.average_duration);
S3_Stats_ROI_number_duration_final.m:121:        [Stats.(region_id).(monkey_id).total_number.eye_neface_p,Stats.(region_id).(monkey_id).total_number.eye_neface_h]=signrank(Gaze_summary.(region_id).(monkey_id).m1_eye.total_number,Gaze_summary.(region_id).(monkey_id).m1_neface.total_number);
S3_Stats_ROI_number_duration_final.m:122:        [Stats.(region_id).(monkey_id).total_number.eye_dot_p,Stats.(region_id).(monkey_id).total_number.eye_dot_h]=signrank(Gaze_summary.(region_id).(monkey_id).m1_eye.total_number,Dot_summary.(region_id).(monkey_id).m1_eye.total_number);
S3_Stats_ROI_number_duration_final.m:124:        [Stats.(region_id).(monkey_id).average_duration.eye_neface_p,Stats.(region_id).(monkey_id).average_duration.eye_neface_h]=signrank(Gaze_summary.(region_id).(monkey_id).m1_eye.average_duration,Gaze_summary.(region_id).(monkey_id).m1_neface.average_duration);
S3_Stats_ROI_number_durat
[... 28 more lines not kept]
```

**Agent calls Bash**

```bash
cd "$TMPDIR/code/Scripts for social attention/Overall gaze behavior and number of stims"; sed -n 158,200p S3_Stats_ROI_number_duration_final.m; grep -n "fdr" S1_Total_Number_of_Stim_Combined.m | head
```

```
save('Gaze_Dot_Comparison_ROI_Stats_Region_Combined.mat','Stats_region','-v7.3')

%% fdr correction

% All days (no need to correct, only one comparison)

total_number_p_raw=[Stats.All_day.(monkey_id).total_number.eye_neface_p Stats.(region_id).(monkey_id).total_number.eye_dot_p];
total_number_p_correct=dsp3.fdr([Stats.All_day.(monkey_id).total_number.eye_neface_p Stats.(region_id).(monkey_id).total_number.eye_dot_p]);

average_duration_p_raw=[Stats.(region_id).(monkey_id).average_duration.eye_neface_p Stats.(region_id).(monkey_id).average_duration.eye_dot_p];
average_duration_p_correct=dsp3.fdr([Stats.(region_id).(monkey_id).average_duration.eye_neface_p Stats.(region_id).(monkey_id).average_duration.eye_dot_p]);

% By region 1-2: eyes vs. neface and eyes vs. dot for OFC
% By region 3-4: eyes vs. neface and eyes vs. dot for ACCg
% By region 5-6: eyes vs. neface and eyes vs. dot for dmPFC
% By region 7-9: OFC vs. ACCg, OFC vs. dmPFC, ACCg vs. dmPFC for Eyes
% By region 10-12: OFC vs. ACCg, OFC vs. dmPFC, ACCg vs. dmPFC for Neface
% By region 13-15: OFC vs. ACCg, OFC vs. dmPFC, ACCg vs. dmPFC for Dots

By_region_total_number_p_raw=[Stats.OFC.All.total_number.eye_neface_p   Stats.OFC.All.total_number.eye_dot_p...
[... 29 more lines not kept]
```

**Agent calls Bash**

```bash
cd "$TMPDIR/code/Scripts for social attention/Overall gaze behavior and number of stims"; sed -n 1,60p S1_Total_Number_of_Stim_Combined.m | grep -v "^\s*$" | head -50; sed -n 175,192p S1_Total_Number_of_Stim_Combined.m
```

```
%% Total number of stim/sham per day
% Upload Gaze_Basic_Behavior_Day_Combined.mat from Basic behaviors, 0_1.5
% folder
fieldname=fieldnames(Gaze_Day);
for k=1:size(fieldname,1)
    field_id=char(fieldname(k));    
    Number_Gaze.(field_id).stim=size(Gaze_Day.(field_id).current_stim.fixation_m1_eye_number,2);
    Number_Gaze.(field_id).sham=size(Gaze_Day.(field_id).current_sham.fixation_m1_eye_number,2);
end
% Upload Dot_Basic_Behavior_Day_Combined.mat from Basic behaviors, 0_1.5
% folder
fieldname=fieldnames(Dot_Day);
for k=1:size(fieldname,1)
    field_id=char(fieldname(k));    
    Number_Dot.(field_id).stim=size(Dot_Day.(field_id).current_stim.fixation_m1_eye_number,2);
    Number_Dot.(field_id).sham=size(Dot_Day.(field_id).current_sham.fixation_m1_eye_number,2);
end
%% Variables and day information 
% All days
OFC_day.All={'07202019'  '07312019'  '08052019'  '08122019'  '08292019' ...
[... 43 more lines not kept]
```

**Agent calls Bash**

```bash
cd "$TMPDIR/code/Scripts for social attention/Saccade kinematics"; grep -ln "current_eye\|current_event\|trigger" *.m; grep -n "current_eye\|current_event\|trigger\|mutual" S1_Gaze_Saccade_Control_Lynch.m | head -20
```

```
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd "$TMPDIR/code"; grep -rln "current_looking\|duration_current\|before_stim\|look_back=-\|look_back = -" --include=*.m . | head; grep -rn "look_back\s*=" --include=*.m . | head
```

```
./stim/model_gaze_data.m
./stim/get_mean_gaze_position_before_stim.m
./Scripts for social attention/Saccade kinematics/S1_Gaze_Saccade_Control_Tarantino.m:7:look_back=0;
./Scripts for social attention/Saccade kinematics/S1_Gaze_Saccade_Control_Lynch.m:7:look_back=0;
./Scripts for social attention/Inter-individual dynamics/Causal Decomposition Index/S1_Gaze_Binned_Distance_Combined.m:3:look_back = 0;
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd "$TMPDIR/code/Scripts for social attention/Heatmap"; ls; grep -n "zscore\|sum(\|/\s*(\|flip\|fliplr\|40\|mean(" *.m | head -30
```

```
S1_Gaze_Fixation_Heatmap.m
S2_Gaze_Plotting_heatmap.m
S1_Gaze_Fixation_Heatmap.m:101:deg_per_px = rad2deg(atan2(.5*h, d)) / (.5*r); 
S1_Gaze_Fixation_Heatmap.m:120:        center = [ mean(roi([1, 3])), mean(roi([2, 4])) ];
S1_Gaze_Fixation_Heatmap.m:152:    ROI.eyes(k,:)=mean(roi_eyes,1,'omitnan');
S1_Gaze_Fixation_Heatmap.m:153:    ROI.mouth(k,:)=mean(roi_mouth,1,'omitnan');
S1_Gaze_Fixation_Heatmap.m:154:    ROI.face(k,:)=mean(roi_face,1,'omitnan');
S1_Gaze_Fixation_Heatmap.m:156:    mats{k} = (mats_stim{k}-mats_sham{k}) / sum( mats_sham{k}(:) + mats_stim{k}(:) );
S1_Gaze_Fixation_Heatmap.m:175:    deg_per_px = rad2deg(atan2(.5*h, d)) / (.5*r); 
S1_Gaze_Fixation_Heatmap.m:183:    center = [ mean(roi([1, 3])), mean(roi([2, 4])) ];
S2_Gaze_Plotting_heatmap.m:22:    '03182022'  '04012022'  '05032022'  '05122022'  '05142022'...
S2_Gaze_Plotting_heatmap.m:44:    '03182022'  '04012022'  '05032022'  '05122022'  '05142022'...
S2_Gaze_Plotting_heatmap.m:47:%% Plotting heatmaps for two monkeys separately and combined (without flipping)
S2_Gaze_Plotting_heatmap.m:82:    flip_y = true;   
S2_Gaze_Plotting_heatmap.m:83:    if ( flip_y )
S2_Gaze_Plotting_heatmap.m:84:        filtered = flipud( filtered );
S2_Gaze_Plotting_heatmap.m:88:    rectangle('Position',[mean(Gaze_ROI.eyes(OFC.(monkey_id).idx,1)) mean(Gaze_ROI.eyes(OFC.(monkey_id).idx,2))...
S2_Gaze_Plotting_heatmap.m:89:        mean(Gaze_ROI.eyes(OFC.(monkey_id).idx,3)-Gaze_ROI.eyes(OFC.(monkey_id).idx,1)) mean(Gaze_ROI.eyes(OFC.(monkey_id).idx,4)-Gaze_ROI.eyes(OFC.(monkey_id).idx,2))],'EdgeColor','r'); hold on
S2_Gaze_Plotting_heatmap.m:90:    rectangle('Position',[mean(Gaze_ROI.mouth(OFC.(monkey_id).idx,1)) mean(Gaze_ROI.mouth(OFC.(monkey_id).idx,2))...
S2_Gaze_Plotting_heatmap.m:91:        mean(Gaze_ROI.mouth(OFC.(monkey_id).idx,3)-Gaze_ROI.mouth(OFC.(monkey_id).idx,1)) mean(Gaze_ROI.mouth(OFC.(monkey_id).idx,4)-Gaze_ROI.mouth(OFC.(monkey_id).idx,2))],'EdgeColor','k'); hold on
[... 13 more lines not kept]
```

**Agent calls Bash**

```bash
cd "$TMPDIR/code/Scripts for social attention"; grep -n "m1_all\|mutual\|events\b\|looks_by" Heatmap/S1_Gaze_Fixation_Heatmap.m | head; grep -n "m1_all\|mutual" "Get data/S3_Basic_Dot_Matrices_Combined.m" | head -5; grep -n "m1_all\|mutual\|m1_distance" "Inter-individual dynamics/Causal Decomposition Index/S1_Gaze_Binned_Distance_Combined.m" | head -5
```

```
581:                fixation_m1_all_idx=find(DotData.(field_id).(run_id).m1_all.Var1(:,11)>=stim_ts(nstim)+look_back & DotData.(field_id).(run_id).m1_all.Var1(:,11)<stim_ts(nstim)+look_ahead);
583:                if isempty(fixation_m1_all_idx)
584:                    DotMatrices.(field_id).(run_id).(stim_id).fixation_m1_all_number=0;
585:                    DotMatrices.(field_id).(run_id).(stim_id).fixation_m1_all_number_NaN=NaN;
586:                    DotMatrices.(field_id).(run_id).(stim_id).fixation_m1_all_duration(1,:)=0;
68:            distance.(field_id).(run_id).(stim_id).m1_distance_to_eyes=sqrt((distance.(field_id).(run_id).(stim_id).x_m1_binned-GazeData.(field_id).(run_id).center_roi_m1_eyes(1)).^2+(distance.(field_id).(run_id).(stim_id).y_m1_binned-GazeData.(field_id).(run_id).center_roi_m1_eyes(2)).^2);         
69:            distance.(field_id).(run_id).(stim_id).m1_distance_to_mouth=sqrt((distance.(field_id).(run_id).(stim_id).x_m1_binned-GazeData.(field_id).(run_id).center_roi_m1_mouth(1)).^2+(distance.(field_id).(run_id).(stim_id).y_m1_binned-GazeData.(field_id).(run_id).center_roi_m1_mouth(2)).^2);
70:            distance.(field_id).(run_id).(stim_id).m1_distance_to_face=sqrt((distance.(field_id).(run_id).(stim_id).x_m1_binned-GazeData.(field_id).(run_id).center_roi_m1_face(1)).^2+(distance.(field_id).(run_id).(stim_id).y_m1_binned-GazeData.(field_id).(run_id).center_roi_m1_face(2)).^2);
Shell cwd was reset to
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/000959/10.1016-j.neuron.2024.05.004.yaml",
 "old_string": "# Euclidean distance from that position to the centre of the partner's Eyes ROI (the RDM ROI in\n# control sessions). A trial's distance is the mean over its fixations; a day's value is the\n# mean over its trials of a type, ignoring trials with no fixation. A fixation is contralateral\n# or ipsilateral by the side of the mean horizontal gaze position of its event relative to the\n# centre of the partner's whole Face ROI: for monkey L (left chamber) left of centre is\n# ipsilateral, for monkey T (right chamber) right of centre is ipsilateral. Day-level",
 "new_string": "# Euclidean distance from that position to the centre of the partner's Eyes ROI (the RDM ROI in\n# control sessions). A trial's distance is the mean over its fixations; a day's value is the\n# mean over its trials of a type, ignoring trials with no fixation. Which fixations enter the\n# distance: the Methods say \"all M1's fixations\"; the code (S3_Basic_Gaze_Matrices_Combined.m,\n# m1_all, built in S1_Get_data_gaze_Lynch.m) takes only events labelled looks_by m1, which\n# it calls \"exclusive m1 events\", and leaves out M1 fixations labelled mutual. The Methods\n# reading (M1-only and mutual events) is the main one and the code's (M1-only events) is a\n# variant, shown for every distance claim. A fixation is contralateral\n# or ipsilateral by the side of the mean horizontal gaze position of its event relative to the\n# centre of the whole Face ROI of M2's calibration (center_roi_m2_face in S1_Get_data_gaze_Lynch.m\n# and _Tarantino.m: M2's Face ROI, which is M1's own face, mirrored into M1's coordinates with\n# the m2_to_m1 offset; this is not the centre of the partner's face, center_roi_m1_face):\n# for monkey L (left chamber) left of centre is\n# ipsilateral, for monkey T (right chamber) right of centre is ipsilateral. Day-level"
}
```

```
The file claims/000959/10.1016-j.neuron.2024.05.004.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/000959/10.1016-j.neuron.2024.05.004.yaml",
 "old_string": "    (whole Face minus Eyes) over the social sessions, compared with a two-sided signed-rank\n    test over the 27 days of each area, FDR-corrected (Benjamini-Hochberg) with the Eyes against\n    RDM test of the same area, as in S3_Stats_ROI_number_duration_final.m. The Methods say",
 "new_string": "    (whole Face minus Eyes) over the social sessions, compared with a two-sided signed-rank\n    test over the 27 days of each area, FDR-corrected (Benjamini-Hochberg, dsp3.fdr) over the 15\n    day-count tests of S3_Stats_ROI_number_duration_final.m (By_region_total_number_p_correct,\n    both monkeys combined; Eyes against non-eye Face and Eyes against RDM for each area, and\n    the rank-sum tests between areas for Eyes, non-eye Face and RDM). The Methods say"
}
```

```
The file claims/000959/10.1016-j.neuron.2024.05.004.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/000959/10.1016-j.neuron.2024.05.004.yaml",
 "old_string": "    of sham trials, two-sided signed-rank test over OFC days. Reproduced when the combined test",
 "new_string": "    of sham trials, two-sided signed-rank test over OFC days. The outcome is judged on the\n    Methods reading of the fixations (M1-only and mutual events); the code's M1-only reading is\n    shown as a variant (opening comment). Reproduced when the combined test"
}
```

```
The file claims/000959/10.1016-j.neuron.2024.05.004.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/000959/10.1016-j.neuron.2024.05.004.yaml",
 "old_string": "    control-session trials with distances to the RDM centre. The hemifield split uses the same\n    reference as in the code for social sessions, the centre of the partner's whole Face ROI.",
 "new_string": "    control-session trials with distances to the RDM centre. The hemifield split uses the same\n    reference as the code uses for social sessions, center_roi_m2_face (S1_Get_data_dot_Lynch.m\n    and _Tarantino.m; opening comment)."
}
```

```
The file claims/000959/10.1016-j.neuron.2024.05.004.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/000959/10.1016-j.neuron.2024.05.004.yaml",
 "old_string": "    the rest of the face), counting M1-only and mutual events as the code does\n    (fixation_m1_eye_number and fixation_m1_wholeface_number in S3_Basic_Gaze_Matrices_Combined.m,\n    which use M1-only events); day means per trial type; signed-rank test over OFC days for each",
 "new_string": "    the rest of the face), counting M1-only events as the code does\n    (fixation_m1_eye_number and fixation_m1_wholeface_number in S3_Basic_Gaze_Matrices_Combined.m,\n    which use M1-only events); day means per trial type; signed-rank test over OFC days for each"
}
```

```
The file claims/000959/10.1016-j.neuron.2024.05.004.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/000959/10.1016-j.neuron.2024.05.004.yaml",
 "old_string": "  criterion: Slopes as in ofc-slope-unchanged-by-epoch for dmPFC and ACCg days. Reproduced when the\n    dmPFC contralateral test gives p < 0.1 with late slopes larger (median late minus early\n    positive), the dmPFC both-hemifields test gives p < 0.05 in the same direction, and the dmPFC\n    ipsilateral and the ACCg tests give p >= 0.05; partially reproduced when the direction holds\n    and only some of these do. The 0.1 bound is taken from the paper's own marking of p = 0.054\n    as \"p ≈ 0.05\". Results under each reading of the causal decomposition are shown.",
 "new_string": "  criterion: Slopes as in ofc-slope-unchanged-by-epoch for dmPFC and ACCg days. Reproduced when the\n    dmPFC contralateral test gives p at most 0.0594 (the reported 0.054 widened by 10%, the\n    protocol's default tolerance; the paper marks it \"p ≈ 0.05\") with late slopes larger (median\n    late minus early positive), the dmPFC both-hemifields test gives p < 0.05 in the same\n    direction, and the dmPFC ipsilateral and the ACCg tests give p >= 0.05; partially reproduced\n    when the direction holds and only some of these do. Results under each reading of the\n    causal decomposition are shown."
}
```

```
The file claims/000959/10.1016-j.neuron.2024.05.004.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/000959/10.1016-j.neuron.2024.05.004.yaml",
 "old_string": "    From the Methods and S1_Gaze_Time_Epoch.m and S3_Gaze_Correlation_by_Epoch.m. The real\n    statistic is the median over days of the late minus early slope. Null: within each day the\n    90 stimulation trials are permuted 1,000 times and split into the first 45 and the next 45,\n    slopes refitted, and for each permutation the median over days of the slope difference is\n    taken. The p-value computation is not in the repository; the readings are (a) one-sided in",
 "new_string": "    From the Methods, the Figure 4D and S4E legends, S1_Gaze_Time_Epoch.m and\n    S3_Gaze_Correlation_by_Epoch.m. The real statistic is the median over days of the late minus\n    early slope (S3_Gaze_Correlation_by_Epoch.m). Null, from the Methods: within each day the\n    90 stimulation trials are permuted 1,000 times and split into the first 45 and the next 45,\n    slopes refitted, and for each permutation the median over days of the slope difference is\n    taken. The repository does not build this null: S3_Gaze_Correlation_by_Epoch.m loads a\n    precomputed Decomp_Temporal_shuffled file whose causal strength field is named\n    causal_m1m2_eyes_null, so whether the null also uses causal strengths from a null\n    decomposition is open; the Methods construction above, with the real causal strengths\n    carried with their trials, is used. The p-value computation is not in the repository; the readings are (a) one-sided in"
}
```

```
The file claims/000959/10.1016-j.neuron.2024.05.004.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
grep -n "^checks\|^[a-z_]*:" claims/000959/10.1016-j.neuron.2024.05.004.yaml; tail -3 claims/000959/10.1016-j.neuron.2024.05.004.yaml; grep -rn "kind: agent" claims/*/*.yaml | head -2
```

```
75:schema_version: 2
76:dataset:
79:paper: doi:10.1016/j.neuron.2024.05.004
80:claims:
    gives the fraction of shuffled median differences beyond the real median, on its side, as
    the code does. Direction groups II, IC, CI and CC by the hemifields of start and end,
    signed-rank against zero per group. Reproduced when no test gives p < 0.05.
claims/000005/10.1038-nn.4412.yaml:1094:  kind: agent
claims/000006/10.1038-s41586-018-0642-9.yaml:843:  kind: agent
```

**Agent calls Bash**

```bash
sed -n '/^checks:/,$p' claims/000005/10.1038-nn.4412.yaml | head -20
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
cat >> claims/000959/10.1016-j.neuron.2024.05.004.yaml <<'EOF'
checks:
- date: 2026-10-22
  kind: agent
  model: claude-opus-5-5
  ready: true
  changes:
  - Header, hemifield split. The header said fixations are split at the centre of the partner's whole Face ROI. S1_Get_data_gaze_Lynch.m and _Tarantino.m (and the dot scripts) split at center_roi_m2_face, the centre of M2's Face ROI (M1's own face) mirrored into M1's coordinates, not at center_roi_m1_face. Corrected; this applies to fig2e-ofc-contralateral, fig2e-dmpfc-accg-no-hemifield-effect, fig2gh-nonsocial-no-hemifield-effect, methods-mouth-stimulation-no-effect, methods-eyes-vs-mouth-bootstrap and the epoch slope claims.
  - Header, fixations entering the distance. The Methods say social gaze distance uses "all M1's fixations"; the code (m1_all in S3_Basic_Gaze_Matrices_Combined.m) uses only events labelled looks_by m1 and drops M1 fixations labelled mutual. The header did not say this. Added it, with the Methods reading as the main one and the code's as a variant, as the protocol orders when Methods and code disagree.
  - fig2c-ofc-social-gaze-distance. The criterion now says the outcome is judged on the Methods reading of the fixations and the code's M1-only reading is shown as a variant.
  - fig2gh-nonsocial-no-hemifield-effect. Same correction of the hemifield reference as the header.
  - figs1e-eyes-more-than-face. The criterion put the FDR correction over two tests (Eyes against non-eye Face and Eyes against RDM of one area). S3_Stats_ROI_number_duration_final.m corrects the per-area figure values over 15 day-count tests (By_region_total_number_p_correct, all monkeys). Corrected; figs1e-eyes-vs-rdm-comparable refers to it and follows.
  - methods-ofc-no-change-in-fixation-number. The criterion said the code counts M1-only and mutual events and, in the same sentence, that it uses M1-only events. The code uses M1-only events; removed the contradiction.
  - fig4c-dmpfc-slope-late-greater. The criterion's bound p < 0.1 for the dmPFC contralateral test was not from the paper. Replaced by the reported p = 0.054 widened by 10% (p at most 0.0594), the protocol's default tolerance.
  - fig4d-dmpfc-slope-permutation. The criterion credited the null construction to S1_Gaze_Time_Epoch.m, which does not build it; no script in the repository does. The construction is now credited to the Methods and legends, and the criterion says the code loads a precomputed shuffled file.
  - Open, fig4d-dmpfc-slope-permutation. The shuffled file's causal strength field is named causal_m1m2_eyes_null, which may mean the code's null also takes causal strengths from a null decomposition. The Methods describe only reshuffling the trial order. The Methods construction is used.
  - Open, header. The hemifield reference is read from the code's ROI handling and its comment "m1 roi is m2's eyes from m1's perspective". That rois.m2 holds M1's face as M2 sees it is an inference from that comment and from M2's distance using center_roi_m2_eyes.
  - Checked and unchanged. Every other statement, source, quote, statistic and expected value matches the paper. Code details checked at commit cc0bf99 and found as cited: trial selection and dropping the first trial, own-type grouping, the inter-looking interval and reciprocation latency computations, the 12-test FDR families for stimulation counts, the five excluded epoch days, the fitlm slopes on stimulation trials, the heatmap normalisation, the one-sided permutation p of Fig. 5G, and the pupil script. The paper's main findings each have a claim.
EOF
python tools/claims_check.py claims/000959/10.1016-j.neuron.2024.05.004.yaml paper/10.1016-j.neuron.2024.05.004.txt; grep -n ": .*: " claims/000959/10.1016-j.neuron.2024.05.004.yaml | grep -v "^\s*[0-9]*:\s*#" | grep "^[0-9]*:  - [A-Z]" | head
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -i 's/found as cited: trial selection/found as cited, namely trial selection/' claims/000959/10.1016-j.neuron.2024.05.004.yaml && python tools/claims_check.py claims/000959/10.1016-j.neuron.2024.05.004.yaml paper/10.1016-j.neuron.2024.05.004.txt && grep -c "—\|rather" claims/000959/10.1016-j.neuron.2024.05.004.yaml; git status --short
```

Result: not kept, because it reads the paper's text.

**Agent**

The claims file for DANDI:000959 is ready for an attempt (`ready: true`). I found five errors and two muddled criteria, all fixed. Two points stay open.

**Checker:** `36 claims, 36 quotes, 132 statistical values, 0 problems`, both before and after my edits.

The paper's analysis code is public, so I cloned it to a temp folder to check the details the criteria take from it. It is at commit cc0bf99, the commit the file cites.

**Changes, by claim**
- **Header, hemifield split (an error):** the header said fixations are split left/right at the centre of the partner's face. The code splits at `center_roi_m2_face`: the face ROI from the partner's calibration, which is the stimulated monkey's own face, mapped into the stimulated monkey's coordinates. This affects fig2e-ofc-contralateral, fig2e-dmpfc-accg-no-hemifield-effect, fig2gh-nonsocial-no-hemifield-effect, the two Mouth claims and the epoch slope claims.
- **Header, which fixations enter the distance (an error):** the Methods say social gaze distance uses all of the stimulated monkey's fixations. The code uses only fixations labelled as that monkey's alone and drops those labelled mutual; the header didn't say so. The protocol says Methods come first when they and the code disagree, so the Methods reading is now the main one and the code's is a variant.
- **fig2c-ofc-social-gaze-distance:** the criterion now says the outcome is judged on the Methods reading, with the code's reading shown as a variant.
- **fig2gh-nonsocial-no-hemifield-effect (an error):** same hemifield-reference fix as the header.
- **figs1e-eyes-more-than-face (an error):** the FDR correction was described as covering two tests. The code corrects over 15 day-count tests. figs1e-eyes-vs-rdm-comparable refers to this criterion, so it follows.
- **methods-ofc-no-change-in-fixation-number:** one sentence said the code counts both kinds of fixation and also that it counts only the monkey's own. It counts only the monkey's own; fixed.
- **fig4c-dmpfc-slope-late-greater (an error):** the bound p < 0.1 was made up. It is now the reported p = 0.054 plus 10% (p ≤ 0.0594), the protocol's default tolerance.
- **fig4d-dmpfc-slope-permutation (an error):** the criterion said `S1_Gaze_Time_Epoch.m` builds the shuffled null. No script in the repository builds it. The construction is now credited to the Methods and figure legends, and the criterion says the code loads a precomputed shuffled file.

**What remains open** (both recorded under `checks`)
- **fig4d null:** the shuffled file's causal-strength field is named `causal_m1m2_eyes_null`. That may mean the code's null also uses causal strengths from a null decomposition, which the Methods don't describe. The Methods construction is used.
- **Hemifield reference:** my reading of what `rois.m2` holds rests on a code comment ("m1 roi is m2's eyes from m1's perspective") and on how the partner's distance is computed. It is an inference, not something the code states.

Everything else matches the paper: statements, sources, quotes, statistics and expected values. The other code details the criteria cite are as described: trial selection, the latency calculations, the stimulation-count tests, the five excluded epoch days, the slope fits, the heatmap normalisation, the Fig. 5G permutation p-value and the pupil analysis. Each main finding has a claim, and all claims come from this paper.

Only `claims/000959/` was changed; nothing is committed or pushed.

## End of run

52 turns, 5 minutes, result: success.
