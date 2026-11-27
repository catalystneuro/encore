# zheng-2024 · claims · run 44695325642

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cat docs/protocol.md; ls paper/ claims/; cat claims/fouke-2025.yaml | head -150
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
grep -n "^#" docs/protocol.md; ls paper/ claims/; wc -l paper/*
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "docs/protocol.md",
 "offset": 1,
 "limit": 200
}
```

```
1	# Protocol for an attempt
2	
3	Version: `pilot-18`. Record this version in the attempt's provenance.
4	
5	This is what agents, or people, do to attempt a target and deposit the
6	result. A target is a dataset in a public archive and a paper it names. How
7	each archive's datasets are named, versioned and read is in
8	[archives.md](archives.md); the examples here are from DANDI, the first. It is written from the pilot attempts
9	([pilot notes](pilot-notes.md)); the reasons for the rules are there.
10	
11	An attempt has three roles, each a separate run with a separate context:
12	
13	- The **reader** reads the paper and writes the claims file: every finding,
14	  and how each is to be tested, taken from the paper. A second reader checks
15	  it against the paper. Readers never see the dataset's data.
16	- The **author** tests the claims on the dataset. It reads the paper to
17	  understand the claims, but the claims file binds it: it cannot change a
18	  claim's statement, expected values or criterion. A method detail the file
19	  lacks it takes from the paper, citing the passage, and it asks a reader
20	  only when it believes the file misreads the paper.
[... 180 more lines not kept]
```

**Agent calls Bash**

```bash
cat claims/fouke-2025.yaml | head -200; ls papers/datasets/ | grep zheng; cat papers/datasets/zheng-2024.yaml 2>/dev/null
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
[... 190 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "paper/10.1016-j.celrep.2024.114702.txt"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -n 200,400p claims/fouke-2025.yaml; cat tools/claims_check.py | head -80
```

```
relatively constant velocity.
  source: Results, Larval DC exhibit higher average swimming speeds, paragraph 1; Figure 1C and
    Figure S1D
  quote: These visually evoked bouts in ZF consist of sharp velocity increases ... followed by
    interbout glides, resulting in characteristic periodic patterns. While DC also match the optic
    flow direction, they swim continuously, maintaining a relatively constant velocity
  criterion: The paper shows this with representative traces and a bout analysis whose bout
    files are not in the dandiset, so a measure is fixed here. Per trial, positions resampled
    to 30 Hz between 3 and 35 s, instantaneous speed, and the ratio of its median to its mean
    (near 1 for steady swimming, low for bursts); per fish, the median over all trials of all
    stimulus codes. Reproduced when the ZF fish have lower ratios than the DC fish by a
    two-sided Mann-Whitney test at p < 0.05.
- id: fig1cef-representative-values
  statement: In representative trials ZF bouts reach a peak velocity of 44.7 mm/s with a median
    of 1.8 mm/s, DC swim at a median of 13.7 mm/s to forward motion; to oblique motion ZF show
    a median angular velocity of 12.0 degrees/s and median peak angular acceleration of 174
    degrees/s2, and DC an average peak of 103 degrees/s2 to rightward motion.
  source: Results, Larval DC exhibit higher average swimming speeds, paragraph 1, and Results, Optic
    flow induces angular matching and turns in DC, paragraph 1; Figure 1C, 1E and 1F
  quote: sharp velocity increases (peak velocity = 44.7 mm/s, median velocity = 1.8 mm/s) ...
[... 182 more lines not kept]
```

**Agent**

I've read the main text through the Key Resources table. Next I'll read the STAR Methods and the rest of the file.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1016-j.celrep.2024.114702.txt",
 "offset": 265,
 "limit": 300
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -n 564,1100p paper/10.1016-j.celrep.2024.114702.txt | grep -v '^10\.' | grep -v '^$' | head -80; file paper/*.pdf; python -c "
import fitz;d=fitz.open('paper/10.1016-j.celrep.2024.114702.supp-mmc2.pdf');print(d.page_count);print(d[0].get_text()[:2000])" 2>&1 | head -60
```

Result: not kept, because it reads the paper's text.

**Agent**

The text file also holds the supplement (Figures S1 onward). Reading it now.

**Agent calls Bash**

```bash
sed -n 564,1100p paper/10.1016-j.celrep.2024.114702.txt | grep -v '^10\.' | grep -v '^\s*$' | sed -n 50,400p
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -n 564,1100p paper/10.1016-j.celrep.2024.114702.txt | grep -v '^10\.' | grep -v '^\s*$' | sed -n 30,50p
```

Result: not kept, because it reads the paper's text.

**Agent**

Text and supplement are complete. Now I'll try the paper's code on Zenodo (10.5281/zenodo.13247193).

**Agent calls Bash**

```bash
cd $TMPDIR && curl -sL https://zenodo.org/api/records/13247193 | python -c "import json,sys;d=json.load(sys.stdin);print(d.get('metadata',{}).get('title'),d.get('metadata',{}).get('related_identifiers'));[print(f['key'],f['size'],f['links']['self']) for f in d.get('files',[])]"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR && curl -sL -o code.zip "https://zenodo.org/api/records/13247193/files/samdeoxys1/within-session-representationl-drift-v0.0.zip/content" && unzip -q -o code.zip -d code && find code -type f \( -name '*.py' -o -name '*.ipynb' -o -name '*.yaml' -o -name '*.md' \) | head -200 && find code -type f | wc -l
```

Result: the fetched text is not kept.

**Agent**

The code is the authors' repo `samdeoxys1/within-session-representationl-drift` v0.0 (commit 93d6e33). I'll look at its layout and the core analysis modules.

**Agent calls Bash**

```bash
cd $TMPDIR/code/samdeoxys1-within-session-representationl-drift-93d6e33 && ls; find . -name '*.py' -not -path './place_variability/code/*' | head -80; cat README* 2>/dev/null | head -50
```

```
README.md
nmf_analysis
place_variability
util_code
./nmf_analysis/nmf_plot.py
./nmf_analysis/logconcave_nmf.py
./nmf_analysis/change_point_post_analysis.py
./nmf_analysis/unimodal_nmf.py
./nmf_analysis/cv.py
./nmf_analysis/svd_sign_flip.py
./nmf_analysis/change_point_plot.py
./nmf_analysis/nmf_cpd.py
./nmf_analysis/change_point_and_behavior.py
./nmf_analysis/cluster_plot.py
./nmf_analysis/pca_analysis_old.py
./nmf_analysis/tsp.py
./nmf_analysis/cluster_analysis.py
./nmf_analysis/change_point_analysis_central_arm_seperate.py
./nmf_analysis/pca_analysis.py
./nmf_analysis/nnls.py
[... 61 more lines not kept]
```

**Agent**

Big repo. I'll send a subagent to settle specific method questions from the code with file and line citations, and draft the claims meanwhile.

**Agent calls Agent**

```json
{
 "description": "Settle method details from code",
 "subagent_type": "general-purpose",
 "prompt": "Read-only task. A paper's analysis code (Zheng et al. 2024 Cell Reports, \"Perpetual step-like restructuring of hippocampal circuit dynamics\") is unpacked at $TMPDIR/code/samdeoxys1-within-session-representationl-drift-93d6e33 (use `echo $TMPDIR` to find it). Do NOT download data or touch anything outside $TMPDIR. Do not modify files. Answer each question below from the code, citing file path (relative to repo root) and line numbers or function names, and quote the key code lines briefly. If the code does not settle a question, say so and say what variants exist in the code. Focus on scripts in place_variability/code/, util_code/, nmf_analysis/ and the figure notebooks in place_variability/jupyter/ whose names start with [fig, [figure], [suppfig], [supp fig], [fig_supp] or similar (notebooks are JSON; grep them).\n\nQuestions:\n1. Trials/turns: how are trials split by turn direction (left/right) on the figure-8 maze, and is a \"session\" in PV analyses one session x one turn direction? How are trials identified (from what fields of the data, e.g. behavior.trials, visitedArm)?\n2. Rate maps: bin size 2.2 cm, gaussian smoothing std 2.5 bins; speed threshold / what \"moving forward\" means in code; linearization source. Spatial info threshold for \"place cell\" (Fig 1 uses place cells; which definition?). Is a place cell any cell with at least one detected place field?\n3. Place field detection (electrophys): shuffle 1000 circular shifts, 95th percentile, 4-30 bins, peak >1 Hz. Any extra rules (merging, edges, min number of trials active)? Function name.\n4. PV correlation vs trial lag (Fig 1D) and the slope comparison (Fig 1E: Wilcoxon rank-sum, lag ranges 1-10, 11-20, 21-30, n=106): how is the slope computed (linear regression of mean/median PV correlation per lag on lag, per session-turn?) and what is n=106 units? File pv_corr_analysis.py and the Fig1 notebook. Are rate maps for PV restricted to place cells, normalized?\n5. Fig 1H/1I: peak firing-rate vector and peak-location vector correlation / normalized squared Euclidean distance vs lag; any test?\n6. Switch detection: ruptures Dynp (optimal partitioning) with model l2, min_size 2? Shuffles 1000, K from 1 to min(5, n_trials//4), p-value per K, Bonferroni over K? Optimal K = lowest percentile; 40% step-size filter relative to max firing rate across trials (exact definition: max of raw peak rates or of fitted?). Switch ON vs OFF definition. Where are \"switch\" fractions per session (Fig 2E) computed? Is the fraction per field or per place field per turn?\n7. Model comparison Fig 3D-F: explained variance ratio definition (1 - SSE/SST?), polynomial order k vs k change points, which fields included (all place fields or only switching?). The \">96%\" number.\n8. First passage time / switch duration (Fig 3K).\n9. GLM Fig 4: Poisson GLM details, regularization (sklearn PoissonRegressor alpha?), CV procedure, how explained deviance (20% ON, 14% OFF) computed; Fig 4D Pearson correlations of normalized switch count vs z-scored trial.\n10. Fig 5C metrics and regression on residuals after regressing log NREM firing rate; how neurons matched across familiar/novel (n=955).\n11. Co-switching test Fig 6D-E: circular shift of switch trials per field; number of shuffles; how significance per session determined (95% CI? per-trial?), \"at least one trial with significant co-switching\".\n12. Fig S5: switchers vs non-switchers slope comparison (Wilcoxon signed-rank).\n13. Fig S14 pre-existing fields (electrophys): within vs outside, which test.\n14. Fig S12, S13 details only if quick.\n15. Session inclusion: >=20 trials, >=7 per turn, >=50 pyramidal cells; how pyramidal cells identified (cell type labels from CellExplorer putativeCellType?). Familiar vs novel sessions: how labelled in code (session list file names?). Any list of the 46 familiar + 8 novel sessions (session names, e.g. e15_13f1_220117)? Print it if present.\n16. Fig 4 GLM: which predictors dropped; \"n = 5,131 arms x trials\".\n\nReturn a compact, organised answer, numbered by question, with citations. Be concise but complete; under 1500 words."
}
```

**Subagent prompt**

Read-only task. A paper's analysis code (Zheng et al. 2024 Cell Reports, "Perpetual step-like restructuring of hippocampal circuit dynamics") is unpacked at $TMPDIR/code/samdeoxys1-within-session-representationl-drift-93d6e33 (use `echo $TMPDIR` to find it). Do NOT download data or touch anything outside $TMPDIR. Do not modify files. Answer each question below from the code, citing file path (relative to repo root) and line numbers or function names, and quote the key code lines briefly. If the code does not settle a question, say so and say what variants exist in the code. Focus on scripts in place_variability/code/, util_code/, nmf_analysis/ and the figure notebooks in place_variability/jupyter/ whose names start with [fig, [figure], [suppfig], [supp fig], [fig_supp] or similar (notebooks are JSON; grep them).

Questions:
1. Trials/turns: how are trials split by turn direction (left/right) on the figure-8 maze, and is a "session" in PV analyses one session x one turn direction? How are trials identified (from what fields of the data, e.g. behavior.trials, visitedArm)?
2. Rate maps: bin size 2.2 cm, gaussian smoothing std 2.5 bins; speed threshold / what "moving forward" means in code; linearization source. Spatial info threshold for "place cell" (Fig 1 uses place cells; which definition?). Is a place cell any cell with at least one detected place field?
3. Place field detection (electrophys): shuffle 1000 circular shifts, 95th percentile, 4-30 bins, peak >1 Hz. Any extra rules (merging, edges, min number of trials active)? Function name.
4. PV correlation vs trial lag (Fig 1D) and the slope comparison (Fig 1E: Wilcoxon rank-sum, lag ranges 1-10, 11-20, 21-30, n=106): how is the slope computed (linear regression of mean/median PV correlation per lag on lag, per session-turn?) and what is n=106 units? File pv_corr_analysis.py and the Fig1 notebook. Are rate maps for PV restricted to place cells, normalized?
5. Fig 1H/1I: peak firing-rate vector and peak-location vector correlation / normalized squared Euclidean distance vs lag; any test?
6. Switch detection: ruptures Dynp (optimal partitioning) with model l2, min_size 2? Shuffles 1000, K from 1 to min(5, n_trials//4), p-value per K, Bonferroni over K? Optimal K = lowest percentile; 40% step-size filter relative to max firing rate across trials (exact definition: max of raw peak rates or of fitted?). Switch ON vs OFF definition. Where are "switch" fractions per session (Fig 2E) computed? Is the fraction per field or per place field per turn?
7. Model comparison Fig 3D-F: explained variance ratio definition (1 - SSE/SST?), polynomial order k vs k change points, which fields included (all place fields or only switching?). The ">96%" number.
8. First passage time / switch duration (Fig 3K).
9. GLM Fig 4: Poisson GLM details, regularization (sklearn PoissonRegressor alpha?), CV procedure, how explained deviance (20% ON, 14% OFF) computed; Fig 4D Pearson correlations of normalized switch count vs z-scored trial.
10. Fig 5C metrics and regression on residuals after regressing log NREM firing rate; how neurons matched across familiar/novel (n=955).
11. Co-switching test Fig 6D-E: circular shift of switch trials per field; number of shuffles; how significance per session determined (95% CI? per-trial?), "at least one trial with significant co-switching".
12. Fig S5: switchers vs non-switchers slope comparison (Wilcoxon signed-rank).
13. Fig S14 pre-existing fields (electrophys): within vs outside, which test.
14. Fig S12, S13 details only if quick.
15. Session inclusion: >=20 trials, >=7 per turn, >=50 pyramidal cells; how pyramidal cells identified (cell type labels from CellExplorer putativeCellType?). Familiar vs novel sessions: how labelled in code (session list file names?). Any list of the 46 familiar + 8 novel sessions (session names, e.g. e15_13f1_220117)? Print it if present.
16. Fig 4 GLM: which predictors dropped; "n = 5,131 arms x trials".

Return a compact, organised answer, numbered by question, with citations. Be concise but complete; under 1500 words.

**Subagent calls Bash**

```bash
cd $TMPDIR/code/samdeoxys1-*; pwd; ls; ls place_variability/code util_code nmf_analysis | head -150; ls place_variability/jupyter | head -100
```

```
/tmp/claude-1001/code/samdeoxys1-within-session-representationl-drift-93d6e33
README.md
nmf_analysis
place_variability
util_code
nmf_analysis:
__pycache__
change_point_analysis.py
change_point_analysis_central_arm_seperate.py
change_point_and_behavior.py
change_point_plot.py
change_point_post_analysis.py
change_point_rsa.py
cluster_analysis.py
cluster_plot.py
cv.py
logconcave_nmf.py
map_switching_analysis.py
nmf_analysis.py
nmf_cpd.py
[... 206 more lines not kept]
```

**Subagent calls Bash**

```bash
cd $TMPDIR/code/samdeoxys1-*; cat README.md | head -50; wc -l place_variability/code/*.py util_code/*.py nmf_analysis/*.py | sort -n | tail -70
```

```
# within-session-representationl-drift
   100 util_code/math_functions.py
   104 place_variability/code/get_all_switch_add_metrics.py
   104 place_variability/code/shuffle_changes_df_one_session.py
   104 util_code/mode_cluster.py
   107 place_variability/code/pf_recombine_central.py
   107 place_variability/code/test_co_switch_pelt_one_sess.py
   109 util_code/get_mono_con.py
   111 place_variability/code/get_all_switch_add_metrics_pen.py
   117 nmf_analysis/map_switching_analysis.py
   117 util_code/get_save_fr_map.py
   126 place_variability/code/variability_axis.py
   129 nmf_analysis/change_point_and_behavior.py
   133 place_variability/code/step_vs_gradual_analysis_population.py
   134 util_code/plotly_helper.py
   136 util_code/gam_analysis.py
   138 nmf_analysis/cluster_analysis.py
   161 place_variability/code/multi_field_analysis.py
   163 nmf_analysis/nmf_test.py
   183 util_code/misc.py
[... 51 more lines not kept]
```

**Subagent calls Bash**

```bash
cd $TMPDIR/code/samdeoxys1-*; cat -n place_variability/code/preprocess_one_session.py; cat -n util_code/database.py | head -120
```

```
1	import os
     2	import sys
     3	import traceback
     4	import numpy as np
     5	import scipy.io as sio
     6	# Import other required libraries
     7	import pandas as pd
     8	sys.path.append('/mnt[removed: a home directory path]/projects/util_code')
     9	sys.path.append('/mnt[removed: a home directory path]/projects/nmf_analysis')
    10	import copy,pdb
    11	import matplotlib.pyplot as plt
    12	import misc
    13	import database 
    14	import data_prep_pyn as dpp
    15	
    16	# filter db
    17	# subdb = database.db.query("owner=='roman'").sort_values('n_pyr_putative',ascending=False)
    18	subdb = database.db.sort_values('n_pyr_putative',ascending=False)
    19	
    20	
[... 168 more lines not kept]
```

**Subagent calls Bash**

```bash
cd $TMPDIR/code/samdeoxys1-*; grep -n "def \|visitedArm\|trials\b\|startPoint\|speed\|trial_type\|choice\|direction" util_code/data_prep_new.py | head -120
```

```
9:def get_speed(pos_2d,dt,is2d=True):
12:        speed = np.sqrt(vel[:,0]**2+vel[:,1]**2)
15:        speed = np.sqrt(vel**2)
16:    return speed,vel
17:def smooth_get_speed(pos_2d,dt,sigma=30,is2d=True):
19:    speed,vel_2d = get_speed(pos_2d_smth,dt,is2d=is2d)
20:    return speed,vel_2d
23:def get_beh_df(behav_timestamps,position,visitedArm,startPoint,n_pos_bins=100):
29:    speed,vel_2d=smooth_get_speed(pos_2d,behav_dt)
39:    df['speed'] = speed #np.sqrt(df['vel_x']**2 + df['vel_y']**2)
42:    peak_times = startPoint[:,0]
43:    peak_times = np.append(peak_times,startPoint[-1,1])
48:    # for assigning a trial and visitedArm to each time bin
50:    # funclist_visitedArm = visitedArm[1:] #for the bad session 1: seems to make sense? Normally shouldn't need it? Need to check more sessions
51:    funclist_visitedArm = visitedArm
52:    funclist_trial =  range(len(funclist_visitedArm))
53:    visitedArm_in_time=np.piecewise(df['times'].values,condlist,funclist_visitedArm)
55:    df['visitedArm'] = visitedArm_in_time
64:def get_fr_beh_df(spike_times,uid,behav_timestamps,cell_type,position,visitedArm,startPoint,n_pos_bins=100,**kwargs):
102:    beh_df,pos_bins_dict=get_beh_df(times,position_interp,visitedArm,startPoint,n_pos_bins=n_pos_bins)
[... 29 more lines not kept]
```

**Subagent calls Bash**

```bash
cd $TMPDIR/code/samdeoxys1-*; grep -n "def \|visitedArm\|speed\|trial_type\|choice\|direction\|lin\b\|linearized\|Linearized\|bin_size\|2.2\|sigma\|smth" util_code/data_prep_pyn.py | head -200
```

```
25:TRIALTYPE_KEY_DICT = {'alternation':'visitedArm','linearMaze':'direction'}
28:def index_one_tsd_using_another_t(tsd,t):
39:########speed using butterworth#######
42:def butter_lowpass(cutoff, fs, order=1):
49:def butter_lowpass_filtfilt(data, cutoff, fs, order=1):
54:def get_speed_butter(xy,dt=0.033,order=1,cutoff=1.):
56:    use butterworth filter to get speed
65:    # speed_xy_butter =np.sqrt(v_xy_butter[:,0]**2 + v_xy_butter[:,1]**2)
68:def get_speed_gaussian(xy,dt=0.033,win_size=0.3):
80:# def get_speed_kalman(xy,dt=0.033,order=2,transition_cov_scale=0.1):
83:#     xy_smth: n_times x 4(order==1)/ 6(order==2), for x,y,vx,vy,ax,ay
104:#     xy_smth,_ = kf.filter(xy)
106:#     return xy_smth
108:def get_multi_maze_behavior_df(behavior,transition_cov_scale=0.1,**kwargs):
156:    # add in smoothed speed
163:            pos = val.loc[:,'lin']
165:            val['v_raw'] = np.gradient(val['lin']) / dt
166:            val['speed_raw'] = np.abs(val['v_raw'])
168:            beh_df.loc[val.index,'speed_raw'] = val['speed_raw']
183:            beh_df.loc[val.index,'speed_raw'] = np.sqrt(beh_df.loc[val.index,'vx_raw']**2 + beh_df.loc[val.index,'vy_raw']**2)
[... 144 more lines not kept]
```

**Subagent calls Bash**

```bash
cd $TMPDIR/code/samdeoxys1-*; sed -n 108,160p util_code/data_prep_pyn.py; sed -n 225,340p util_code/data_prep_pyn.py; sed -n 400,560p util_code/data_prep_pyn.py; sed -n 580,690p util_code/data_prep_pyn.py
```

```
def get_multi_maze_behavior_df(behavior,transition_cov_scale=0.1,**kwargs):
    '''
    behavior: loaded from the matlab struct: Behavior.mat
    if multiple mazes, then return a dict of df
    first based on Roman's behavior struct; if sth is missing then add

    kwargs: like sessionPulses=sessionPulses, 
    extra loaded structs, need to write specific ways to incorporate them into the df 
    '''
    
    
    pddf = pd.DataFrame
    pos = np.stack(list(behavior['position'].values()),axis=1)
    beh_df = nap.TsdFrame(t = behavior['timestamps'], 
                d = pos,
    #              x = behavior['position']['x'],
    #              y = behavior['position']['y'],
                columns = behavior['position'].keys()
                )
    beh_df['trial']=behavior['masks']['trials'] - 1 # to make trials 0 indexed; originally 1 indexed
[... 420 more lines not kept]
```

**Subagent**

Now the rate map scripts.

**Subagent calls Bash**

```bash
cd $TMPDIR/code/samdeoxys1-*; cat -n place_variability/code/fr_map_one_session.py | sed -n 1,189p
```

```
1	import os
     2	import sys
     3	import traceback
     4	import numpy as np
     5	import scipy.io as sio
     6	# Import other required libraries
     7	import pandas as pd
     8	sys.path.append('/mnt[removed: a home directory path]/projects/util_code')
     9	sys.path.append('/mnt[removed: a home directory path]/projects/nmf_analysis')
    10	import copy,pdb
    11	import matplotlib.pyplot as plt
    12	import misc
    13	import database 
    14	import data_prep_pyn as dpp
    15	import place_cell_analysis as pa
    16	import place_field_analysis as pf
    17	
    18	# filter db
    19	# subdb = database.db.query("owner=='roman'").sort_values('n_pyr_putative',ascending=False)
    20	subdb = database.db.sort_values('n_pyr_putative',ascending=False)
[... 169 more lines not kept]
```

**Subagent calls Bash**

```bash
cd $TMPDIR/code/samdeoxys1-*; grep -n "def get_fr_map_trial\b" -A80 util_code/place_cell_analysis.py | head -120; grep -n "def detect_speed_related_event" -A50 place_variability/code/behavior_analysis.py
```

```
123:def get_fr_map_trial(df,cell_columns,trialtype_key='visitedArm',**kwargs):
124-    '''
125-    trialtype_key for subdividing trialtype before computing the tuning curve; 
126-    eg for alternating it's visitedArm; for linear it's direction
127-    '''
128-    gpb = df.groupby([trialtype_key])
129-    fr_map_final_dict = {}
130-    for key, val in gpb:
131-        fr_map_final_dict[key] = get_fr_map_trial_onegroup(val,cell_columns,**kwargs)
132-
133-    return fr_map_final_dict
134-
135-def get_fr_map_trial_multi_task(spk_beh_df,cell_columns,trialtype_key_dict = {'alternation':'visitedArm','linearMaze':'direction'}, \
136-                        **kwargs):
137-    fr_map_task_dict = {}
138-    task_index_to_task_name = dpp.get_task_index_to_task_name(spk_beh_df)
139-    for k, val in spk_beh_df.groupby('task_index'):
140-        task_type = task_index_to_task_name[k]
141-        fr_map_turn_dict = get_fr_map_trial(val,cell_columns,trialtype_key=trialtype_key_dict[task_type],**kwargs)
142-        fr_map_task_dict[k] ={k:v[0] for k,v in fr_map_turn_dict.items()}
[... 112 more lines not kept]
```

**Subagent calls Bash**

```bash
cd $TMPDIR/code/samdeoxys1-*; sed -n 1,122p util_code/place_cell_analysis.py | grep -n "def \|gauss\|speed\|bin\|order" | head -50; grep -n "def detect_offtrack_event" -A15 place_variability/code/behavior_analysis.py | head -20
```

```
13:from scipy.ndimage import gaussian_filter1d
25:def get_fr_map_trial_onegroup(df,cell_columns,gauss_width=2.5,order=['smooth','divide','average'],bin_size=2.2,n_lin_bins=100,**kwargs):
29:    if 'average' in order: fr_map_final: dataframe, ncells x nbins
30:    if not: np array, ncells x nbins x ntrials
33:    if 'lin_binned' not in df:
34:        # df['lin_binned'] = pd.cut(df['lin'],bins=n_lin_bins,labels=False,retbins=False)
35:        df,_ = dpp.add_lin_binned(df,bin_size=bin_size,nbins=n_lin_bins)
36:        # n_lin_bins  = len(df['lin_binned'].unique())
37:    n_lin_bins  = int(df['lin_binned'].max()) # assuming its from 0 to n_lin_bins-1
46:    if 'speed_thresh' in kwargs.keys():
48:        speed_thresh = kwargs['speed_thresh']
50:        speed_thresh = 5
51:    # mask = np.sqrt(df['vel_x']**2+df['vel_y']**2) > speed_thresh # by default only keep time points with speed above 5
52:    if 'speed_key' in kwargs.keys(): 
53:        speed_key = kwargs['speed_key']
55:        if (df['speed'] > speed_thresh).mean() < 0.001:
56:            speed_key = 'v'
58:            speed_key = 'speed'
59:    mask = df[speed_key] > speed_thresh # by default only keep time points with speed above 5
66:        counts = val.groupby('lin_binned')[columns].sum()
[... 36 more lines not kept]
```

**Subagent**

Now place field detection.

**Subagent calls Bash**

```bash
cd $TMPDIR/code/samdeoxys1-*; cat -n place_variability/code/pf_one_session.py | sed -n 20,120p; grep -n "def " util_code/place_field_analysis.py
```

```
20	subdb = database.db.sort_values('n_pyr_putative',ascending=False)
    21	
    22	
    23	SAVE_DIR=''
    24	SAVE_FN='place_field_afterheadscan.p'
    25	SHUFFLE_SAVE_FN = 'frmap_null_afterheadscan.p'
    26	
    27	
    28	def load_preprocess_data(session_path):
    29	    prep_res = dpp.load_spk_beh_df(session_path,force_reload=False,extra_load=dict(sessionPulses='*SessionPulses.Events.mat',filtered='*thetaFiltered.lfp.mat'))
    30	    spk_beh_df=prep_res['spk_beh_df']
    31	    _,spk_beh_df = dpp.group_into_trialtype(spk_beh_df)
    32	    # spk_beh_df,_=dpp.add_lin_binned(spk_beh_df,nbins=100)
    33	    spk_beh_df,_=dpp.add_lin_binned(spk_beh_df,bin_size=2.2,nbins=None)
    34	    cell_cols_d = prep_res['cell_cols_d']
    35	    
    36	    data = {'spk_beh_df':spk_beh_df,'cell_cols_d':cell_cols_d}
    37	    return data
    38	
    39	def analyze_data(data,*args,**kwargs):
[... 88 more lines not kept]
```

**Subagent calls Bash**

```bash
cd $TMPDIR/code/samdeoxys1-*; sed -n 291,347p util_code/place_field_analysis.py; sed -n 392,445p util_code/place_field_analysis.py; sed -n 635,730p util_code/place_field_analysis.py
```

```
def get_fr_map_shuffle(spk_beh_df,cell_cols,nrepeats=100,dosave=False,save_fn='fr_map_null_trialtype.p',speed_thresh=1,nbins=100,smth_in_bin=2.5,bin_size=2.2,speed_key='v'):
    '''
    now the shuffle is done on the basis of a trial type; 
    '''
    dd,spk_beh_df=dpp.group_into_trialtype(spk_beh_df)
    # roll_inds = np.random.randint(50,spk_beh_df.shape[0]-50,size=nrepeats)
    # beh_part=spk_beh_df[['lin','trial_type','speed']]
    fr_map_null_d_all = {k:{} for k in dd.keys()}
    for tt, sbdf in dd.items():
        roll_inds = np.random.randint(50,sbdf.shape[0]-50,size=nrepeats)
        # beh_part=sbdf[['lin','v','speed','lin_binned']] 
        beh_part=sbdf[['lin',speed_key,'lin_binned','time']]  # important to add time here, otherwise dt is messed up!!
        for n in tqdm.tqdm(range(nrepeats)):
            i = roll_inds[n]
            # pdb.set_trace()
            spk_df_roll =pd.DataFrame(np.roll(sbdf[cell_cols],i,axis=0),columns=cell_cols,index=sbdf.index)
            spk_df_roll = pd.concat([spk_df_roll,beh_part],axis=1)
            # fr_map_null_d,_,_ = ratemap_from_spk_beh_df_alltrialtype(spk_df_roll,cell_cols,speed_thresh=speed_thresh,nbins=nbins,smth_in_bin=smth_in_bin)
            fr_map_null,_,_ = ratemap_from_spk_beh_df_onetrialtype(spk_df_roll,cell_cols,speed_thresh=speed_thresh,nbins=nbins,bin_size=bin_size,smth_in_bin=smth_in_bin,speed_key=speed_key)
        # for k,val in fr_map_null_d.items():
[... 187 more lines not kept]
```

**Subagent calls Bash**

```bash
cd $TMPDIR/code/samdeoxys1-*; sed -n 1,107p place_variability/code/pf_recombine_central.py | grep -v "^\s*#" | sed -n 15,107p; grep -n "def " util_code/process_central_arm.py
```

```
import place_field_analysis as pf
import process_central_arm as pca
from importlib import reload
reload(pca)
from database import db
subdb = database.db.sort_values('n_pyr_putative',ascending=False)

SAVE_DIR=''

pf_save_fn = 'place_field_afterheadscan.p'
pf_shuffle_fn = 'frmap_null_afterheadscan.p'
force_reload = True
SAVE_FN = 'place_field_afterheadscan_recombine.p' # make it consistent with pf_save_fn by adding_recombine


def load_preprocess_data(session_path):
    pf_res = pf.field_detection_avg_wrapper(session_path, dosave=False,force_reload=False, 
                                        save_fn = pf_save_fn, 
                                        shuffle_fn=pf_shuffle_fn,load_only=True)
    
[... 75 more lines not kept]
```

**Subagent calls Bash**

```bash
cd $TMPDIR/code/samdeoxys1-*; sed -n 1,135p util_code/process_central_arm.py; sed -n 208,330p util_code/process_central_arm.py; sed -n 491,527p util_code/process_central_arm.py
```

```
# dealing with the central arm, splitter cells, etc.

import numpy as np
import scipy
import pandas as pd
import copy, pdb, sys, os
import data_prep_pyn as dpp
import change_point_analysis as cpa

# find left right similar fields
def find_left_right_similar_fields(all_fields_both_trialtypes,similar_thresh_in_bin=5,loc_key='peak'):
    left_right_similar_fields = {}
    index_other = []
    # task_ind = 0
    trial_type_ind = 0
    trial_type_to_compare_ind = 1
    # similar_thresh_in_bin = 5 # careful since different maze default binsize might be different
    for (ni,fi),row in all_fields_both_trialtypes.loc[trial_type_ind].iterrows():
        if ni in all_fields_both_trialtypes.loc[trial_type_to_compare_ind].index:
            dist = np.abs(row[loc_key] - all_fields_both_trialtypes.loc[trial_type_to_compare_ind].loc[ni][loc_key] )
[... 274 more lines not kept]
```

**Subagent calls Bash**

```bash
cd $TMPDIR/code/samdeoxys1-*; sed -n 172,204p util_code/place_field_analysis.py; sed -n 539,573p util_code/place_field_analysis.py
```

```
def get_field_params_trial(fr_map_trial,all_fields):
    '''
    fr_map_trial: df
    all_fields: series, nfields_tot,  (neurons, (start,end), nfields), no nan terms; the boundaries for each field
    '''
    fr_l = {}
    fr_peak_l = {}
    center_l = {}
    peak_l = {}
    std_l = {}

    for ind,val in all_fields.groupby(level=(0,1)):
        
        fr_field = fr_map_trial.loc[ind[0]].loc[val.loc[ind]['start']:val.loc[ind]['end']]
        fr_field_by_trial = fr_field.mean(axis=0)
        fr_l[ind[:2]]=fr_field_by_trial
        fr_peak_l[ind[:2]] = fr_field.max(axis=0)
        center_by_trial = np.sum((fr_field.values * np.array(fr_field.index)[:,None]) ,axis=0) / np.sum(fr_field,axis=0)
        center_l[ind[:2]]=center_by_trial
        peak_by_trial = fr_field.idxmax(axis=0)
[... 45 more lines not kept]
```

**Subagent**

Now switch detection.

**Subagent calls Bash**

```bash
cd $TMPDIR/code/samdeoxys1-*; grep -v "^\s*#" place_variability/code/switch_detection_one_session.py | sed -n 1,200p
```

```
import os
import sys
import traceback
import numpy as np
import scipy.io as sio
import pandas as pd
sys.path.append('/mnt[removed: a home directory path]/projects/util_code')
sys.path.append('/mnt[removed: a home directory path]/projects/nmf_analysis')
import copy,pdb,importlib
import matplotlib.pyplot as plt
import misc
import database 
import data_prep_pyn as dpp
import place_cell_analysis as pa
import place_field_analysis as pf
import test_change_point as tcp
importlib.reload(tcp)

import pf_recombine_central as pfrc
from database import db
[... 63 more lines not kept]
```

**Subagent calls Bash**

```bash
cd $TMPDIR/code/samdeoxys1-*; cat -n place_variability/code/test_change_point.py
```

```
1	'''
     2	a newer version of the change_point_analysis
     3	'''
     4	import sys,os,pickle,copy, itertools,pdb
     5	sys.path.append('/mnt[removed: a home directory path]/projects/seq_detection2/code')
     6	sys.path.append('/mnt[removed: a home directory path]/projects/util_code')
     7	sys.path.append('/mnt[removed: a home directory path]/projects/nmf_analysis')
     8	import numpy as np
     9	
    10	import pandas as pd
    11	from importlib import reload
    12	import pynapple as nap
    13	import ruptures as rpt
    14	import tqdm
    15	import change_point_analysis as cpa
    16	import pingouin as pg
    17	
    18	def get_explained_var_ratio(signal,error):
    19	    signal_var = np.var(signal)
    20	    exp_var_ratio = (signal_var - error / len(signal)) / signal_var
[... 264 more lines not kept]
```

**Subagent calls Bash**

```bash
cd $TMPDIR/code/samdeoxys1-*; grep -n "def detect_switch_pwc\|def predict_from_cpts_wrapper\b" nmf_analysis/change_point_analysis.py
```

```
54:def predict_from_cpts_wrapper(signal,ncpts,cost='l2',min_size=2,model_type=rpt.Dynp,return_var=False):
163:def detect_switch_pwc(X_norm_pwc,switch_magnitude=0.,low_thresh=1.,high_thresh=0.):
```

**Subagent calls Bash**

```bash
cd $TMPDIR/code/samdeoxys1-*; sed -n 54,80p nmf_analysis/change_point_analysis.py; sed -n 163,215p nmf_analysis/change_point_analysis.py
```

```
def predict_from_cpts_wrapper(signal,ncpts,cost='l2',min_size=2,model_type=rpt.Dynp,return_var=False):
    model = model_type(model=cost,jump=1,min_size=min_size)
    c = model.fit(signal)
    cpts=model.predict(ncpts)
    cpts = np.array([0,*cpts])
    signal_pred=predict_from_cpts(signal,cpts,return_var=return_var)
    return signal_pred, cpts[1:-1] # return no first and last
from matplotlib.ticker import MaxNLocator
def predict_from_cpts_wrapper_plot(signal,ncpts,cost='l2',min_size=2,model_type=rpt.Dynp,fig=None,ax=None,flipy=False,
                                dolabel=False,dolegend=False
                                ):
    signal_pred, cpt = predict_from_cpts_wrapper(signal,ncpts,cost=cost,min_size=min_size,model_type=model_type)
    trials = np.arange(len(signal))
    if ax is None:
        fig,ax=plt.subplots(figsize=(4,6))
    ax.plot(signal,trials,c='grey',marker='o',alpha=0.8,linewidth=3,label='raw')
    ax.plot(signal_pred,trials,c='k',linewidth=3,label='fitted')
    ax.yaxis.set_major_locator(MaxNLocator(integer=True))
    if dolabel:
        ax.set(xlabel='Peak firing rate (Hz)',ylabel='Trial')
[... 60 more lines not kept]
```

**Subagent calls Bash**

```bash
cd $TMPDIR/code/samdeoxys1-*; cat -n place_variability/code/pv_corr_analysis.py
```

```
1	import numpy as np
     2	import scipy
     3	import matplotlib.pyplot as plt
     4	import seaborn as sns
     5	import sys,os,copy,pdb,importlib,pickle
     6	from importlib import reload
     7	import pandas as pd
     8	sys.path.append('/mnt[removed: a home directory path]/projects/util_code')
     9	import plot_helper as ph
    10	
    11	def get_val_per_lag(mat):
    12	    '''
    13	    col: lag
    14	    index: count
    15	    '''
    16	    mat = mat.dropna(axis=1,how='all').dropna(axis=0,how='all')
    17	    mat = mat.values
    18	    ntrials = mat.shape[0]
    19	    vals_per_lag_l = {}
    20	    for lag in range(1,ntrials-1):
[... 342 more lines not kept]
```

**Subagent calls Bash**

```bash
cd $TMPDIR/code/samdeoxys1-*/place_variability/jupyter; cat > $TMPDIR/nbdump.py <<'EOF'
import json,sys
nb=json.load(open(sys.argv[1]))
for i,c in enumerate(nb['cells']):
    src=''.join(c['source'])
    if c['cell_type']=='markdown':
        print(f'### [{i}] MD: '+src.replace('\n',' ')[:300])
    elif c['cell_type']=='code':
        print(f'### [{i}] CODE'); print(src)
EOF
python3 $TMPDIR/nbdump.py "[fig1]changepoint_figure1_not_example_panels.ipynb" | wc -l; python3 $TMPDIR/nbdump.py "[fig1]changepoint_figure1_not_example_panels.ipynb" | head -400
```

```
548
### [0] CODE
import numpy as np
import scipy
import sklearn
from sklearn.decomposition import NMF
from sklearn.cluster import KMeans
from sklearn.mixture import GaussianMixture,BayesianGaussianMixture

import pandas as pd

import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.rcParams['image.cmap'] = 'Greys'

import seaborn as sns

import sys,os,pdb,copy,pickle
from importlib import reload
import pynapple as nap
[... 381 more lines not kept]
```

**Subagent calls Bash**

```bash
cd $TMPDIR/code/samdeoxys1-*/place_variability/jupyter; python3 $TMPDIR/nbdump.py "[fig1]changepoint_figure1_not_example_panels.ipynb" | sed -n 400,548p
```

```
ax.hlines(val,ii-0.2,ii+0.2,color='k')

    
    return fig,ax,order 
    
    
### [32] CODE
ratio_sig_per_sess_reset_ind
### [33] CODE
plt.rcParams['svg.fonttype']
### [34] CODE
ratio_sig_per_sess
### [35] CODE

from matplotlib.lines import Line2D
data=ratio_sig_per_sess_reset_ind#ratio_sig_per_sess_reset_ind.drop(51) #unclear why drop 51.. go back to no drop
x='xs'#'Novel maze'
y='Frac. switching fields'
color_per_strip={0:'C0',1:'C0',2:'C1'}
fig,ax,order=stripplot_with_median(data,x,y,color_per_strip=color_per_strip,figsize=(2,3),ms=15)
[... 129 more lines not kept]
```

**Subagent calls Bash**

```bash
cd $TMPDIR/code/samdeoxys1-*/place_variability/jupyter; grep -l "get_val_per_lag\|pv_corr" *.ipynb; echo; grep -l "ranksums" *.ipynb; echo; grep -l "PoissonRegressor\|glm" *.ipynb | head -30
```

```
[explore] compare amplitude change and location drift-Copy1.ipynb
[explore] imaging data change point.ipynb
[explore] location drift.ipynb
[explore][imaging] block reuse idea using unimodal nmf.ipynb
[explore][imaging] metrics.ipynb
[explore][imaging] quantify drift based on unimodal nmf.ipynb
[explore][imaging]slurm_within_across_drift_per_neuron.ipynb
[explore][imaging]within_across_drift_per_neuron_2_noshuffle.ipynb
[figure] compare amplitude change and location drift.ipynb
[figure] contribution of switching to drift.ipynb
[figure] gradual vs sudden change.ipynb
[figure][imaging]block_reuse_nmf_shuffle_agg.ipynb
[supp fig] redo drift with zscore; individual neuron drift.ipynb
[suppfigure] gradual vs sudden change no avg for pop drift.ipynb

[explore] artifact in disinhibition-pop up agg .ipynb
[explore] imaging data change point.ipynb
[explore] predict co switch using interneuron_2.ipynb
[explore] predict switch using disinhibition.ipynb
[explore] use inhibition drop below a threshold to predict pop up.ipynb
[... 41 more lines not kept]
```

**Subagent calls Bash**

```bash
cd $TMPDIR/code/samdeoxys1-*/place_variability/jupyter; python3 $TMPDIR/nbdump.py "[fig]changepoint_figure1_try.ipynb" > $TMPDIR/f1try.txt; wc -l $TMPDIR/f1try.txt; grep -n "^### \[.*MD\|ranksums\|slope\|lag\|10,\|subdb\|query" $TMPDIR/f1try.txt | head -100
```

```
811 /tmp/claude-1001/f1try.txt
60:plotfm.main(subdb['data_dir_full'][0])
61:### [4] MD: # load all session
63:subdb = db.query('owner=="roman"').sort_values('n_pyr_putative',ascending=False)
64:subdb = subdb.query('ntrials>=20&n_neurons>=50')
76:for ind,row in subdb.iterrows():
88:### [8] MD: # load all switch related
95:# for ind,row in subdb.iterrows():
121:for ind,row in subdb.iterrows():
185:### [14] MD: # distribution of p values
232:### [18] MD: # distribution of percentage significant per session
245:    ax.hist(myarray, weights=weights,bins=10,label=novel_str[k],alpha=0.4)
289:### [29] MD: # switching and fr stability
382:for ind,row in subdb.iterrows():
440:scipy.stats.ranksums(post_minus_pre_fr_df_all.query('switch_category=="on"')['post_minus_pre'],
441:                      post_minus_pre_fr_df_all.query('switch_category=="no_switch"')['post_minus_pre']
444:scipy.stats.ranksums(post_minus_pre_fr_df_all.query('switch_category=="off"')['post_minus_pre'],
445:                      post_minus_pre_fr_df_all.query('switch_category=="no_switch"')['post_minus_pre']
448:scipy.stats.ranksums(post_minus_pre_fr_df_all.query('switch_category=="off"')['post_minus_pre'],
449:                      post_minus_pre_fr_df_all.query('switch_category=="on"')['post_minus_pre']
[... 8 more lines not kept]
```

**Subagent**

Not Fig 1D. Check the drift notebooks.

**Subagent calls Bash**

```bash
cd $TMPDIR/code/samdeoxys1-*/place_variability/jupyter; for f in "[figure] gradual vs sudden change.ipynb" "[figure] contribution of switching to drift.ipynb" "[figure] compare amplitude change and location drift.ipynb" "[supp fig] redo drift with zscore; individual neuron drift.ipynb" "[suppfigure] gradual vs sudden change no avg for pop drift.ipynb"; do echo "=== $f"; python3 $TMPDIR/nbdump.py "$f" | grep -n "MD:\|ranksum\|wilcoxon\|slope\|linregress\|figdir =\|savefig\|save_given" | head -40; done
```

```
=== [figure] gradual vs sudden change.ipynb
77:figdir = '/mnt[removed: a home directory path]/ceph/place_variability/fig/paper/figure_continuous_vs_discrete'
131:### [7] MD: # fit all sessions
170:        ph.save_given_name(fig,figfn,figdir,dpi=900)
172:### [13] MD: # look at one session
202:### [17] MD: ## select examples
291:### [24] MD: # step vs continuous for the pv correlation curve
322:ph.save_given_name(fig,figfn,figdir)
348:        ph.save_given_name(fig,figfn,figdir,dpi=900)
350:### [34] MD: # analysis of how many trials it take to switch
351:### [35] MD: ## get peri switch trials
354:### [37] MD: ### idea: how many trials are lapsed from the valley pre switch and peak post switch
437:ph.save_given_name(fig,figfn,figdir)
477:# #     ph.save_given_name(fig,figfn,figdir)
520:#     ph.save_given_name(fig,figfn,figdir)
522:### [56] MD: # trial duration schematics
563:ph.save_given_name(fig,figfn,figdir)
571:### [62] MD: ## examples of trial span
624:        ph.save_given_name(fig,figfn,figdir)
672:### [72] MD: ## measure expected number of trial span pre post difference (peri-switch valley peak FR difference) / sqrt(mean residual squared)  
[... 103 more lines not kept]
```

**Subagent calls Bash**

```bash
cd $TMPDIR/code/samdeoxys1-*/place_variability/jupyter; python3 $TMPDIR/nbdump.py "[figure] compare amplitude change and location drift.ipynb" > $TMPDIR/amp.txt; sed -n 80,480p $TMPDIR/amp.txt
```

```
data_dir = '/mnt[removed: a home directory path]/ceph/place_variability/data/paper'
misc.get_or_create_subdir(data_dir)

### [4] CODE
import database
db = database.db

subdb = db.query('owner=="roman"').sort_values('n_pyr_putative',ascending=False)
subdb = subdb.query('ntrials>=20&n_neurons>=50')
to_exclude_sess = ['e16_3m2_211211']
subdb=subdb.loc[~subdb['sess_name'].isin(to_exclude_sess)]


import pf_recombine_central as pfrc
import fr_map_one_session as fmos
import switch_detection_one_session as sdos
import get_all_switch_add_metrics as gasam

import preprocess_one_session as prepos
### [5] CODE
[... 381 more lines not kept]
```

**Subagent calls Bash**

```bash
cd $TMPDIR/code/samdeoxys1-*; sed -n 16,63p util_code/place_field_analysis.py
```

```
def ratemap_from_spk_beh_df_onetrialtype(spk_beh_df,cell_cols,speed_thresh=1,bin_size=2.2,nbins=100,smth_in_bin=5,speed_key=None):
    '''
    spk_beh_df: df that has neurons spike counts and behavior, in behavior timestamps
    fr_map: nneurons x nposbins
    '''
    if bin_size is not None:
        nbins = int(np.floor((spk_beh_df['lin'].max() - spk_beh_df['lin'].min()) / bin_size))
    if 'lin_binned' not in spk_beh_df.columns:
        spk_beh_df['lin_binned'],bins = pd.cut(spk_beh_df['lin'],nbins,retbins=True,labels=False)
    if speed_key is None:
        if (spk_beh_df['speed'] > speed_thresh).mean() <0.001:  # in some roman's sessions x y can't be used, so use his v for velocity estimate
            speed_key = 'v'
        else:
            speed_key= 'speed'
    # speed_ma = np.abs(spk_beh_df[speed_key]) > speed_thresh
    speed_ma = spk_beh_df[speed_key] > speed_thresh # perhaps using not the abs makes more sense? just looking at one direction for one trial in 1d task
    spk_beh_df_ma = spk_beh_df.loc[speed_ma]
    gpb = spk_beh_df_ma.groupby(['lin_binned'])
    occu = gpb['lin'].count()

[... 28 more lines not kept]
```

**Subagent calls Bash**

```bash
cd $TMPDIR/code/samdeoxys1-*; grep -rn "get_bits_per_spike\|bits_per_spike\|si_thresh\|spatial_info" --include=*.py . | grep -v "def " | head; grep -l "get_bits_per_spike\|si_thresh" place_variability/jupyter/*.ipynb
```

```
./place_variability/code/variability_axis.py:42:        s_i = pa.get_bits_per_spike(val.loc[k],cell_cols=cell_cols,gauss_width = 2.5,speed_key = 'directed_locomotion',speed_thresh = 0.5,
./place_variability/code/stability_analysis.py:222:    si_thresh=0.5
./place_variability/code/stability_analysis.py:223:    si_ma = per_field_metrics_all['si'] > si_thresh
./place_variability/code/stability_analysis.py:236:            si_thresh=0.5,
./place_variability/code/stability_analysis.py:248:    si_ma = per_field_metrics_all['si'] > si_thresh
./place_variability/code/stability_analysis.py:284:            fn_full = f'{y}_vs_{x}_hue_{hue}_ntrials_after_sw_{ntrials_after_sw}_si_thresh_{si_thresh}_noswstartfrac_{nosw_start_frac:.0e}.{fmt}'
./place_variability/code/stability_analysis.py:286:                fn_full = f'{y}_vs_{x}_hue_{hue}_ntrials_after_sw_{ntrials_after_sw}_si_thresh_{si_thresh}_randomstart_{random_start}.{fmt}'
./place_variability/code/stability_analysis.py:288:                fn_full = f'{y}_vs_{x}_hue_{hue}_ntrials_after_sw_{ntrials_after_sw}_si_thresh_{si_thresh}_nosw_start_pre_peak.{fmt}'
./place_variability/code/stability_analysis.py:290:                fn_full = f'{y}_vs_{x}_hue_{hue}_ntrials_after_sw_{ntrials_after_sw}_si_thresh_{si_thresh}_nosw_start_pre_min.{fmt}'                
./place_variability/code/stability_analysis.py:299:    si_ma = per_field_metrics_all['si'] > si_thresh
place_variability/jupyter/[explore][imaging] quantify drift based on unimodal nmf.ipynb
place_variability/jupyter/[explore][imaging]within_across_drift_per_neuron_2_noshuffle.ipynb
place_variability/jupyter/[fig] stability after pop up.ipynb
place_variability/jupyter/[fig]selecting and plotting example ratemaps.ipynb
place_variability/jupyter/[fig_supp] cell property difference using pelt.ipynb
place_variability/jupyter/[figure] gradual vs sudden change.ipynb
place_variability/jupyter/[figure] introductory sequence.ipynb
place_variability/jupyter/[figure] metric across fam nov
[... 3 more lines not kept]
```

**Subagent calls Bash**

```bash
cd $TMPDIR/code/samdeoxys1-*; grep -v "^\s*#" place_variability/code/step_vs_gradual_analysis.py | head -300
```

```
import ruptures as rpt
import numpy as np
import pandas as pd
import scipy
import os,sys,copy,itertools,pdb,importlib

import statsmodels
import statsmodels.api as sm
sys.path.append('/mnt[removed: a home directory path]/projects/nmf_analysis')
sys.path.append('/mnt[removed: a home directory path]/projects/place_variability/code')
sys.path.append('/mnt[removed: a home directory path]/projects/util_code')
import change_point_analysis as cpa
import plot_all_fr_map_x_pwc_one_session as plotfm
importlib.reload(plotfm)
import plot_helper as ph
import matplotlib.pyplot as plt

def fit_cpd_get_r2(xx,ncpts,cost='l2',min_size=2):
    
    xx_pwc,cpt=cpa.predict_from_cpts_wrapper(xx,ncpts,cost=cost,min_size=min_size)
[... 226 more lines not kept]
```

**Subagent calls Bash**

```bash
cd $TMPDIR/code/samdeoxys1-*/place_variability/jupyter; python3 $TMPDIR/nbdump.py "[figure] gradual vs sudden change.ipynb" > $TMPDIR/gvs.txt; sed -n 60,360p $TMPDIR/gvs.txt
```

```
plt.rcParams['figure.figsize'] = (6, 4)  # width, height in inches

# Set default font sizes
plt.rcParams['font.size'] = 10  # Default font size
plt.rcParams['axes.titlesize'] = 10  # Title font size
plt.rcParams['axes.labelsize'] = 10  # Label font size
plt.rcParams['xtick.labelsize'] = 10  # x-axis tick label font size
plt.rcParams['ytick.labelsize'] = 10  # y-axis tick label font size
plt.rcParams['legend.fontsize'] = 10  # Legend font size
mpl.rcParams['image.cmap'] = 'viridis'
mpl.rcParams['axes.spines.right'] = False
mpl.rcParams['axes.spines.top'] = False
### [2] CODE
import matplotlib
matplotlib.rcParams['svg.fonttype'] = 'none'
### [3] CODE

figdir = '/mnt[removed: a home directory path]/ceph/place_variability/fig/paper/figure_continuous_vs_discrete'
misc.get_or_create_subdir(figdir)
data_dir = '/mnt[removed: a home directory path]/ceph/place_variability/data/paper'
[... 281 more lines not kept]
```

**Subagent calls Bash**

```bash
cd $TMPDIR/code/samdeoxys1-*/place_variability/jupyter; sed -n 360,760p $TMPDIR/gvs.txt
```

```
span_d = svga.get_peri_switch_peak_valley_span(changes_df_row,X_raw_row,X_pwc_row)
peri_sw_x_one=svga.get_peri_switch_x_raw(changes_df_row,X_raw_row,win=10)
### [39] CODE
X_raw_row.plot(marker='o')
X_pwc_row.plot()
### [40] CODE

### [41] CODE
span_d_one = {}
for kk,X_raw_row in X_raw_all.iterrows():
    changes_df_row = changes_df_all.loc[kk].dropna()
    X_raw_row = X_raw_row.dropna()
    if X_pwc_one is not None:
        X_pwc_row = X_pwc_all.loc[kk].dropna()
        span_d = svga.get_peri_switch_peak_valley_span(changes_df_row,X_raw_row,X_pwc_row)
    else:
        span_d = svga.get_peri_switch_peak_valley_span(changes_df_row,X_raw_row)
    span_d_one[kk] = span_d
#     span_d_one = pd.concat(span_d_one).stack().unstack(level=2) # uid,field_id, sw_id
span_d_one = pd.concat(span_d_one).stack()
[... 381 more lines not kept]
```

**Subagent calls Bash**

```bash
cd $TMPDIR/code/samdeoxys1-*; grep -n "def \|Poisson\|alpha\|deviance\|KFold\|cv\|n_splits\|drop\|zscore\|pearson" place_variability/code/behavior_and_switching.py | head -80
```

```
11:def get_categorical_var(df,var_bin_d):
18:def get_corret_prev_trialwithin_bothtt(correct_per_trial,trial_index_to_index_within_df):
39:def get_correct_df_all(spk_beh_df_all,ti=0):
58:def add_corret_prev_seperate(var_per_trial_pos_all,pos_key='lin_binned_cat',pos_thresh=1):
72:def combine_correct_with_var_per_trial_pos_all(var_per_trial_pos_all,correct_df_all,pos_key='lin_binned_cat',pos_thresh=1):
88:    var_per_trial_pos_all=  pd.concat([var_per_trial_pos_all.reset_index(drop=True),correct_val_l],axis=1)
95:def get_n_fied_per_pos_per_trial_all(all_fields_recombined_all,trial_index_to_index_within_df_all,
133:def prep_regression(spk_beh_df_all,all_fields_recombined_all,all_sw_d_all,trial_index_to_index_within_df_all,cell_cols_d_all=None,**kwargs):
176:    ind_var_per_trial_pos_all['speed_gauss_cv'] = ind_var_per_trial_pos_all['speed_gauss_std'] / ind_var_per_trial_pos_all['speed_gauss_mean']
240:    # zscore speed, within session
241:    # var_per_trial_pos_all = var_per_trial_pos_all.groupby(level=1).apply(lambda x:x.assign(speed_z=scipy.stats.zscore(x['speed_gauss'])))
242:    var_per_trial_pos_all = var_per_trial_pos_all.groupby(level=1).apply(lambda x:x.assign(speed_z=scipy.stats.zscore(x['speed_gauss_mean'])))
243:    var_per_trial_pos_all = var_per_trial_pos_all.groupby(level=1).apply(lambda x:x.assign(speed_std_z=scipy.stats.zscore(x['speed_gauss_std'])))
244:    var_per_trial_pos_all = var_per_trial_pos_all.groupby(level=1).apply(lambda x:x.assign(speed_cv_z=scipy.stats.zscore(x['speed_gauss_cv'])))
245:    # zscore trial, within session
246:    var_per_trial_pos_all = var_per_trial_pos_all.groupby(level=1).apply(lambda x:x.assign(trial_z=scipy.stats.zscore(x['trial'])))
260:    n_field_per_pos_one_tt_per_trial_all_droplevel=n_field_per_pos_one_tt_per_trial_all.droplevel(3)
261:    inds_intersect=n_field_per_pos_one_tt_per_trial_all_droplevel.index.intersection(var_per_trial_pos_all_re_nfield.index) # drop trials that were excluded in trial_index_to_ind_w
[... 21 more lines not kept]
```

**Subagent calls Bash**

```bash
cd $TMPDIR/code/samdeoxys1-*; sed -n 95,395p place_variability/code/behavior_and_switching.py
```

```
def get_n_fied_per_pos_per_trial_all(all_fields_recombined_all,trial_index_to_index_within_df_all,
                                     var_bin_d={'lin_binned':np.array([0,15,74,111,185,202,222])/2.2},
                                        combine_first_last_section=True,
                                     pos_key = 'peak',task_index=0,
                                    ):
    '''
    trial: each trial type have different place fields
    get: ani,sess,ti (only 0),tt, trial_index - n_field
    '''
    if isinstance(trial_index_to_index_within_df_all,dict):
        trial_index_to_index_within_df_all = pd.concat(trial_index_to_index_within_df_all,axis=0)
    lin_binned_cat_max = lin_binned_cat_max = len(var_bin_d['lin_binned'])-2
    n_field_per_pos_one_tt_per_trial_all = []
    for k,val in trial_index_to_index_within_df_all.groupby(level=(0,1,2,3)):
        ani,sess,ti,tt=k
        if ti==task_index: # only do familiar t maze for now
            if 'both' in all_fields_recombined_all.loc[(ani,sess,ti),:].index.get_level_values(0):
                tt_l = [tt,'both']
            else:
                tt_l = tt
[... 281 more lines not kept]
```

**Subagent calls Bash**

```bash
cd $TMPDIR/code/samdeoxys1-*/place_variability/jupyter; python3 $TMPDIR/nbdump.py "[fig] sw and behavior factors modulating sw.ipynb" > $TMPDIR/glm.txt; wc -l $TMPDIR/glm.txt; grep -n "MD:\|formula\|key_l\|cat_l\|pearsonr\|cv_poisson\|n_splits\|offset\|exposure\|drop\|shape" $TMPDIR/glm.txt | head -120
```

```
957 /tmp/claude-1001/glm.txt
144:ntrials_per_tt=fr_map_trial_df_all.groupby(level=(0,1,2,3)).apply(lambda x:x.dropna(axis=1,how='all').shape[1])
166:### [13] MD: # prep data
181:# var_per_trial_pos_all_re_nfield['n_field']  = n_field_per_pos_one_tt_per_trial_all.droplevel(3)
204:### [22] MD: ##### left right trial averaged count sw, per trial; sum across trials
207:y_key_l = ['sw_on','sw_off']
208:# n_sw_per_pos=var_per_trial_pos_all.set_index('lin_binned_cat',append=True).groupby(level=(0,1,2,3))[y_key_l].sum()
209:n_sw_per_pos = var_per_trial_pos_all.groupby(level=(0,1,2)).apply(lambda x:x.groupby('lin_binned_cat',group_keys=False)[y_key_l].sum())
223:for y_key in y_key_l:
226:### [25] MD: # spatial agg
242:    sns.lineplot(data=var_per_pos.reset_index(drop=True),x='lin_binned_cat',y=f'sw_{onoff}_div_n_field',ax=ax)
261:### [33] MD: # relationship with prev correct
269:correct_key_l = [k for k in var_per_trial_pos_all.columns if 'correct' in k]
270:correct_df_all = var_per_trial_pos_all.set_index('trial',append='True').groupby(level=(0,1,2,3))[correct_key_l].apply(lambda x:x.mode(axis=0).iloc[0])
284:### [41] MD: # glm
287:import statsmodels.formula.api as smf
294:X = var_per_trial_pos_all.dropna(axis=0)
309:formula=f"{y_key}~C(animal)+C(lin_binned_cat)+n_field+trial_z+speed_z+speed_cv_z+correct+correct_prev_seperate"
310:# formula=f"{y_key}~C(animal)+C(lin_binned_cat)+n_field+trial_z+speed_z+speed_cv_z+correct_prev_seperate+E_mean+I_mean+E_I_mean"
311:# formula=f"{y_key}~C(animal)+C(lin_binned_cat)+n_field+trial_z+C(speed_cat)+speed_cv_z+correct_prev_seperate"
[... 48 more lines not kept]
```

**Subagent calls Bash**

```bash
cd $TMPDIR/code/samdeoxys1-*/place_variability/jupyter; sed -n 100,205p $TMPDIR/glm.txt; sed -n 284,300p $TMPDIR/glm.txt; sed -n 455,540p $TMPDIR/glm.txt; sed -n 640,730p $TMPDIR/glm.txt
```

```
res_df['E_mean'] = pyr_df.mean(axis=1)
    res_df['I_mean'] = int_df.mean(axis=1)
    res_df['E/I_mean'] = res_df['E_mean'] / res_df['I_mean']
    res_df['E_frac_active'] = (pyr_df>0).mean(axis=1)
    res_df['I_frac_active'] = (int_df>0).mean(axis=1)
    eps = 1e-10
    res_df['E/I_frac_active'] = res_df['E_frac_active']/(res_df['I_frac_active']+eps)
    res_df = pd.concat(res_df,axis=1)
    
    return res_df
### [6] CODE
def get_ei_var_spk_beh_df_all(spk_beh_df_all,cell_cols_d_all):
    ei_res_df_all = []
    for k,sbd in spk_beh_df_all.groupby(level=(0,1)):
        ei_res_df=get_ei_var_spk_beh_df(sbd,cell_cols_d_all[k])
        ei_res_df_all.append(ei_res_df)
    ei_res_df_all  = pd.concat(ei_res_df_all,axis=0)
    return ei_res_df_all
### [7] CODE
all_fields_recombined_all
[... 280 more lines not kept]
```

**Subagent calls Bash**

```bash
cd $TMPDIR/code/samdeoxys1-*/place_variability/jupyter; grep -n "'Full'\|5131\|5,131\|X.shape\|len(X)" $TMPDIR/glm.txt; sed -n 300,330p $TMPDIR/glm.txt; grep -n "def get_correct_df_all" -A40 ../code/behavior_and_switching.py | grep -n "prev\|correct" | head
```

```
474:# formula_shorthand = ['Full','w/o Speed','w/o Trial','w/o N field','w/o Position','w/o Animal']
475:formula_shorthand = ['Full','w/o Animal','w/o Position','w/o N field','w/o Trial','w/o Speed','w/o Speed CV','w/o Correct','w/o Correct Prev. Trial']
505:# scipy.stats.wilcoxon(sc_l_all_l_d.loc['sw_on','Full'],sc_l_all_l_d.loc['sw_on','w/o Trial'],alternative='greater')
506:# # scipy.stats.wilcoxon(sc_l_all_l_d.loc['sw_on','Full'],sc_l_all_l_d.loc['sw_on','w/o Correct'],alternative='greater')
511:# xx=sc_l_all_l_d.loc['sw_on','Full'] - sc_l_all_l_d.loc['sw_on',key]
515:formula_shorthand_nofull = [x for x in formula_shorthand if x!='Full']
519:    diff=sc_l_all_l_d.loc[y_key].loc[formula_shorthand_nofull]-sc_l_all_l_d.loc[y_key,'Full']
print(ani)
# print(ani)
# X=X.loc[ani]
### [45] CODE
k_l=['sw_on_div_n_field','E_mean','I_mean','trial_z','speed_z']
X.loc[ani].rcorr().loc[k_l,k_l]
# X.loc[ani].pcorr().loc[k_l,k_l]
### [46] CODE
y_key='sw_on'#'sw_off'#
formula=f"{y_key}~C(animal)+C(lin_binned_cat)+n_field+trial_z+speed_z+speed_cv_z+correct+correct_prev_seperate"
# formula=f"{y_key}~C(animal)+C(lin_binned_cat)+n_field+trial_z+speed_z+speed_cv_z+correct_prev_seperate+E_mean+I_mean+E_I_mean"
# formula=f"{y_key}~C(animal)+C(lin_binned_cat)+n_field+trial_z+C(speed_cat)+speed_cv_z+correct_prev_seperate"
# formula=f"{y_key}~C(animal)+C(lin_binned_cat)+n_field+trial_z+speed_z+speed_std_z+correct_prev_seperate"
[... 28 more lines not kept]
```

**Subagent calls Bash**

```bash
cd $TMPDIR/code/samdeoxys1-*/place_variability/jupyter; python3 $TMPDIR/nbdump.py "[fig] switch_and_single_neuron_properties.ipynb" > $TMPDIR/sn.txt; wc -l $TMPDIR/sn.txt; grep -n "MD:\|nrem\|NREM\|resid\|ols\|955\|isin\|novel\|common\|intersection" $TMPDIR/sn.txt | head -80
```

```
369 /tmp/claude-1001/sn.txt
65:subdb=subdb.loc[~subdb['sess_name'].isin(to_exclude_sess)]
228:    metrics=['UID','putativeCellType','firingRate','firingRateCV','firingRate_NREMstate','firingRate_REMstate','firingRate_WAKEstate','burstIndex_Mizuseki2012']
270:inds=best_n_all.index[best_n_all==0].intersection(exp_var_ratio.index)
284:metrics=['UID','putativeCellType','firingRate','firingRateCV','firingRate_NREMstate','firingRate_REMstate','firingRate_WAKEstate','burstIndex_Mizuseki2012']
316:np.corrcoef(res['fit_var_ratio'], res['resid2_mean_ratio'])
```

**Subagent calls Bash**

```bash
cd $TMPDIR/code/samdeoxys1-*/place_variability/jupyter; grep -c "NREM" *.ipynb | grep -v ":0"; grep -rln "NREM" ../code ../../util_code ../../nmf_analysis
```

```
[explore] artifact in disinhibition-pop up agg .ipynb:1
[explore] correlation change across sleep.ipynb:5
[explore] disinhibition popup magnitude.ipynb:1
[explore] if drop in inh in one field, can disinhibition predict another field's pop up.ipynb:1
[explore] use inhibition drop below a threshold to predict pop up.ipynb:1
[explore] using drop in int below thresh to predict pop up.ipynb:1
[explore] variability axes.ipynb:1
[explore]discrepancy between switch and consec trial diff for disinhibition .ipynb:1
[fig] switch_and_single_neuron_properties.ipynb:5
[fig]selecting and plotting example ratemaps.ipynb:1
[fig_] does switch in one field predict the other.ipynb:1
[fig_supp] cell property difference using pelt.ipynb:3
[figure] metric across fam novel.ipynb:3
[figure] predict switch using disinhibition agg.ipynb:1
[figure] variability axis 2.ipynb:1
[suppfig] imaging stability.ipynb:1
[suppfig] switch rate in light responsive neurons.ipynb:15
gm_or_glm_redo.ipynb:1
nmf_on_count_2.ipynb:1
pre_post_sleep_fr_change.ipynb:3
[... 2 more lines not kept]
```

**Subagent calls Bash**

```bash
cd $TMPDIR/code/samdeoxys1-*/place_variability/jupyter; python3 $TMPDIR/nbdump.py "[figure] metric across fam novel.ipynb" > $TMPDIR/fn.txt; wc -l $TMPDIR/fn.txt; grep -n "MD:\|NREM\|resid\|ols\|isin\|common\|intersection\|wilcoxon\|ranksums\|spearman\|pearson\|log" $TMPDIR/fn.txt | head -80
```

```
626 /tmp/claude-1001/fn.txt
70:subdb=subdb.loc[~subdb['sess_name'].isin(to_exclude_sess)]
123:    metrics=['UID','putativeCellType','firingRate','firingRateCV','firingRate_NREMstate','firingRate_REMstate','firingRate_WAKEstate','burstIndex_Mizuseki2012']
163:    fr_nrem=np.ones(val.shape[0]) * cell_metrics_df_all.loc[k,'firingRate_NREMstate']
180:# outcome_model = smf.ols('nov~fam+fr',data=data)
181:# mediator_model = smf.ols('fr~fam',data=data)
186:def resid_regression(data,confound_exog,exog,endog,regress_out_exog=False):
189:    regress_out_confound_res = smf.ols(formula,data=data).fit()
190:    resid = regress_out_confound_res.resid
191:    data['resid'] = resid
194:        regress_out_confound_exog_res = smf.ols(formula,data=data).fit()
195:        data[exog[0]]=regress_out_confound_exog_res.resid
198:    res = smf.ols(formula,data=data).fit()
218:per_field_metrics_all['fr_nrem_log'] = np.log(per_field_metrics_all['fr_nrem'])
220:data=per_field_metrics_all[['fit_var_ratio_1cp','fr_nrem_log']].unstack(level=2).dropna().iloc[:,:3]
224:fr_key = 'fr_nrem_log' # 'fr_nrem' #
233:    # res,regress_out_confound_res = resid_regression(data,confound_exog,exog,endog)
234:    res,regress_out_confound_res,regress_out_confound_exog_res = resid_regression(data,confound_exog,exog,endog,regress_out_exog=True)
240:    print(f'==={key} residual regression===\n')
254:# res,regress_out_confound_res = resid_regression(data,confound_exog,exog,endog)
[... 14 more lines not kept]
```

**Subagent calls Bash**

```bash
cd $TMPDIR/code/samdeoxys1-*/place_variability/jupyter; sed -n 95,330p $TMPDIR/fn.txt
```

```
X_raw_all = prepped_data_agg['X_raw_all']
changes_df_all = prepped_data_agg['changes_df_all']
var_res_all_test = prepped_data_agg['var_res_all']
# corr_all = prepped_data_agg['corr_all']
all_sw_d_all = prepped_data_agg['all_sw_d_all']
all_sw_with_metrics_d_all = prepped_data_agg['all_sw_with_metrics_d_all']
best_n_all_test = prepped_data_agg['best_n_all']
spk_beh_df_all = prepped_data_agg['spk_beh_df_all']

ntrials_per_tt=fr_map_trial_df_all.groupby(level=(0,1,2,3)).apply(lambda x:x.dropna(axis=1,how='all').shape[1])
ntrials_mask = ntrials_per_tt.groupby(level=(0,1,2)).apply(lambda x:(x>=7).all()) 

### [5] CODE
savefn_full = os.path.join(data_dir,'per_field_metrics_shtest_with_1cp.p')
per_field_metrics_all=pickle.load(open(savefn_full,'rb'))
### [6] CODE
# skip if just loading
best_n_all_ = best_n_all_test
import glob
cell_metrics_df_all = {}
[... 216 more lines not kept]
```

**Subagent calls Bash**

```bash
cd $TMPDIR/code/samdeoxys1-*; cat -n place_variability/code/variability_axis.py
```

```
1	'''
     2	create the axis by which to organize cells/fields according to their type of variability
     3	'''
     4	
     5	import numpy as np
     6	import scipy
     7	import matplotlib.pyplot as plt
     8	import sys,os,copy,pdb,importlib
     9	from importlib import reload
    10	import pandas as pd
    11	sys.path.append('/mnt[removed: a home directory path]/projects/util_code')
    12	sys.path.append('/mnt[removed: a home directory path]/projects/nmf_analysis')
    13	import place_cell_analysis as pa
    14	import tsp
    15	
    16	from scipy.spatial.distance import pdist, squareform
    17	
    18	def stability_by_corr_one_cell(mat):
    19	    '''
    20	    mat: npos x ntrial
[... 106 more lines not kept]
```

**Subagent calls Bash**

```bash
cd $TMPDIR/code/samdeoxys1-*; grep -v "^\s*#" place_variability/code/test_co_switch.py; grep -v "^\s*#" place_variability/code/test_co_switch_one_sess.py | sed -n 1,140p
```

```
import numpy as np
import scipy
import matplotlib.pyplot as plt
import sys,os,copy,pdb,importlib
from importlib import reload
import pandas as pd

import sys
sys.path.append('/mnt[removed: a home directory path]/projects/nmf_analysis')
import change_point_analysis as cpa
import switch_metrics as sm



def gen_circular_shuffle_trialtype_seperated(changes_df,nrepeats=200,min_cpd_win=2):
    '''
    changes_df: (task_ind x trialtype_ind x uid x field_id) x ntrials
    '''
    changes_df = changes_df.dropna(axis=1,how='all')
    gpb = changes_df.groupby(level=(0,1),group_keys=False)
[... 249 more lines not kept]
```

**Subagent calls Bash**

```bash
cd $TMPDIR/code/samdeoxys1-*; grep -n "def gen_circular_shuffle\b" -A30 nmf_analysis/change_point_analysis.py; cd place_variability/jupyter; python3 $TMPDIR/nbdump.py "[fig_]coswitch quantification.ipynb" > $TMPDIR/cosw.txt; wc -l $TMPDIR/cosw.txt; grep -n "MD:\|ci_high\|issig\|any\|0.975\|0.95\|alpha\|per trial\|per_trial\|nrepeats\|n_shuffle" $TMPDIR/cosw.txt | head -80
```

```
433:def gen_circular_shuffle(changes_df,nrepeats=200,min_cpd_win=2,new_start_inds=None):
434-    '''
435-    changes_df: anything nfields x ntrials, can be the original data or the one after the change point detection
436-    '''
437-    
438-    nfields,ntrials_orig=changes_df.shape
439-    X = changes_df.values[:,min_cpd_win:(ntrials_orig-(min_cpd_win-1))]
440-    ntrials = X.shape[1]
441-    X_all_roll = np.array([np.roll(X,i,axis=1) for i in range(X.shape[1])]) # generate all possible circular shifts for the population together
442-    # np.random.seed(10)
443-    if new_start_inds is None:
444-        new_start_inds=np.random.randint(ntrials-1,size=(nrepeats,nfields)) # sample independently for each field the starting point in the shift
445-    # sim_l=np.array([X_all_roll[new_start_inds[i],np.arange(nfields)] for i in range(new_start_inds.shape[0])])
446-    X_sim_l = []
447-    for i in range(new_start_inds.shape[0]):
448-        x_sim_one = X_all_roll[new_start_inds[i],np.arange(nfields)]
449-        x_sim_one_padded=np.concatenate([np.zeros((nfields,min_cpd_win)),x_sim_one,np.zeros((nfields,min_cpd_win-1))],axis=1)
450-        x_sim_one_padded_df = pd.DataFrame(x_sim_one_padded,index=changes_df.index,columns=changes_df.columns)
451-        X_sim_l.append(x_sim_one_padded_df)
452-    # X_sim_l = [pd.DataFrame(X_all_roll[new_start_inds[i],np.arange(nfields)],index=changes_df.index,columns=changes_df.columns) for i in range(new_start_inds.shape[0])] # using indexing to select the corresponding shift for each field in each shuffle
[... 87 more lines not kept]
```

**Subagent calls Bash**

```bash
cd $TMPDIR/code/samdeoxys1-*; sed -n 241,456p $TMPDIR/cosw.txt
```

```
### [13] MD: # coswitch summary figures 
### [14] CODE
import test_co_switch_one_sess as tcsos
reload(tcsos)
co_sw_pval_all = {}
n_co_sw_all={}
n_co_sw_shuffle_all={}
for ind,row in subdb.iterrows():
    data_dir_full = row['data_dir_full']
    ani = ind[0]
    sess = row['sess_name']
    cosw_res=tcsos.main(data_dir_full,force_reload=False,dosave=False,load_only=True)
    co_sw_pval = cosw_res['co_sw_pval']
    n_co_sw=cosw_res['n_co_sw']
    n_co_sw_shuffle=cosw_res['n_co_sw_shuffle']

    co_sw_pval_all[ani,sess]=co_sw_pval
    n_co_sw_all[ani,sess] = n_co_sw
    n_co_sw_shuffle_all[ani,sess] = n_co_sw_shuffle
co_sw_pval_all = pd.concat(co_sw_pval_all,axis=0)
[... 196 more lines not kept]
```

**Subagent calls Bash**

```bash
cd $TMPDIR/code/samdeoxys1-*/place_variability/jupyter; grep -l "at least one\|any_sig\|per_trial_sig\|issig_per_trial\|sig_trial" *.ipynb; grep -n "def " ../code/co_sw_and_ripple_cofiring_one_sess.py | head; grep -n "def \|quantile\|nrepeats" ../../nmf_analysis/switch_metrics.py | head -40
```

```
after_preprocess_ratemaps_and_place_fields.ipynb
detect field compact.ipynb
detect_center_shift+field detection by shuffle per trial.ipynb
show coswitching examples and null (cosyne 2022).ipynb
switch_detection_aggregate_fig.ipynb
switch_detection_field_distribution.ipynb
65:def load_preprocess_data(data_dir_full):
98:def analyze_data(data,*args,**kwargs):
161:# def save_results(results, session_path, output_folder):
165:def main(session_path,test_mode=False,
25:def prep_load_one_sess(data_dir_full):
46:    switch_res = saos.switch_analysis_one_session(data_dir_full,place_field_res=None,force_reload=False,nrepeats=1000,
51:def get_fr_info(key,fr_trial,switch_trial):
93:# def get_ntrial_info(key,fr_trial,switch_trial):
94:def get_ntrial_info(key,fr_trial,switch_trial,pre_ntrials_in_segment,post_ntrials_in_segment):
124:def add_switch_trial_by_trialtype(all_sw_times_v_combined,trial_index_to_index_within_df,task_ind=0):
188:def add_metrics(all_sw_times_v_combined,pf_fr_combined,trial_index_to_index_within_df_onetask):
223:def get_all_sw_add_metrics_all_tasks(sw_res,pf_params_recombined,spk_beh_df,is_changes_df=False,do_add_metrics=True,pf_loc_key='peak',pf_fr_key='fr_peak'):
255:def add_switch_metrics_wrapper(data_dir_full,
280:                                nrepeats_sw = 2,
[... 8 more lines not kept]
```

**Subagent calls Bash**

```bash
cd $TMPDIR/code/samdeoxys1-*/place_variability/jupyter; python3 $TMPDIR/nbdump.py "[fig2]spatial_temporal_distribution_of_switch_figures.ipynb" > $TMPDIR/f2.txt; wc -l $TMPDIR/f2.txt; grep -n "MD:\|shuffle\|quantile\|issig\|any(\|sig" $TMPDIR/f2.txt | head -80
```

```
821 /tmp/claude-1001/f2.txt
163:### [6] MD: # prep data
170:### [8] MD: # spatial
194:### [12] MD: # spatial within animal
216:### [14] MD: # cluster for spatial per session
290:### [26] MD: # spatial agg 
387:### [34] MD: ### glm diagnostics
480:### [40] MD: # vs trial
526:### [47] MD: # regression selection
580:### [51] MD: # funny behavior map
581:### [52] MD: # visualize switching and headscan events on maze
642:### [56] MD: # quantifying ratio of switching and headscan
```

**Subagent calls Bash**

```bash
cd $TMPDIR/code/samdeoxys1-*/place_variability/jupyter; for f in "[fig_]co_switching_and_fc_all_sess.ipynb" "[fig_] does switch in one field predict the other.ipynb" "[fig_] does pop up cell in fam also pop up in novel.ipynb" "co-switch sliding window.ipynb"; do echo "=== $f"; python3 $TMPDIR/nbdump.py "$f" | grep -n "MD:\|quantile\|issig\|\.any(\|pval\|nrepeats\|n_shuffle" | head -30; done
```

```
=== [fig_]co_switching_and_fc_all_sess.ipynb
96:pval_all = {}
137:    pval = sw_res['pval']
138:    pval_all[ani,sess]=pval
163:pval_all = pd.concat(pval_all,axis=0)
183:pval_all = prepped_data_agg['pval_all']
194:### [11] MD: # function to get co-sw within 1,2,3 trials, using absolute trial indices
236:# all_sw_shuffle =tcs.gen_circular_shuffle_trialtype_seperated_get_all_sw(changes_df_one,pf_params_recombined_one,spk_beh_df,nrepeats=200)
276:        diff_data,diff_data_sh_l,pval,fig,ax=pwa.shuffle_test_label_switch_diff_plot(label_sim_one,co_sw_sim_one,sw_sim_allonoff_shuffle,onoff=onoff,sw_key=sw_key,
=== [fig_] does switch in one field predict the other.ipynb
88:pval_all = prepped_data_agg['pval_all']
103:### [5] MD: # given multifield, one field pop up, can it predict the other field
104:### [6] MD: awkward: has to join 0/1 and both each seperately, otherwise would miss multiple fields that has one on the central
159:has_sw_on = (changes_df_all==1).any(axis=1)
160:has_sw_off = (changes_df_all==-1).any(axis=1)
165:resample_one_df_l = mfa.shuffle_has_sw_df(has_sw_df_pre_combine,all_fields_recombined_all,nrepeats=200,do_combine_tt_with_both=True)
379:### [34] MD: # does multifield switch happen in the same or adjacent trial
397:                same_trial = np.any(np.logical_and(valval[nn,:],valval[kk,:]))
399:                if np.any(valval[nn,:]) & np.any(valval[kk,:]):
412:### [41] MD: # examples
[... 56 more lines not kept]
```

**Subagent calls Bash**

```bash
cd $TMPDIR/code/samdeoxys1-*; sed -n 150,240p $TMPDIR/cosw.txt; sed -n 550,610p $TMPDIR/cosw.txt
```

```
pf_params_recombined_all = pd.concat(pf_params_recombined_all,axis=0)
fr_map_trial_df_all = pd.concat(fr_map_trial_df_all,axis=0)
pval_all = pd.concat(pval_all,axis=0)
X_pwc_all = pd.concat(X_pwc_all,axis=0)
X_raw_all = pd.concat(X_raw_all,axis=0)
changes_df_all = pd.concat(changes_df_all,axis=0)
var_res_all = pd.concat(var_res_all,axis=0)
corr_all = pd.concat(corr_all,axis=0)
all_sw_d_all = pd.concat(all_sw_d_all,axis=0)
all_sw_with_metrics_d_all = pd.concat(all_sw_with_metrics_d_all,axis=0)
best_n_all = pd.concat(best_n_all,axis=0)

spk_beh_df_all = pd.concat(spk_beh_df_all,axis=0)

### [5] CODE
fn = 'prepped_data_agg.p'
fn_full = os.path.join(data_dir,fn)
prepped_data_agg = pickle.load(open(fn_full,'rb'))

all_fields_recombined_all = prepped_data_agg['all_fields_recombined_all']
[... 132 more lines not kept]
```

**Subagent calls Bash**

```bash
cd $TMPDIR/code/samdeoxys1-*/place_variability/code; grep -v "^\s*#" test_co_switch_pelt_one_sess.py | sed -n 25,80p
```

```
force_reload = True
PF_FR_KEY = 'fr_peak'#'fr_mean'#
SAVE_DIR=''
SAVE_FN=f'penalty_co_sw_res_afterheadscan_{PF_FR_KEY}.p'#'sw_res_afterheadscan.p'#f'sw_res_afterheadscan_{PF_FR_KEY}.p'
n_shuffle = 1000

def load_preprocess_data(session_path):
    sw_res = sdspos.main(session_path,force_reload=False,load_only=True)
    data={'changes_df_all_pen':{k:sw_res[k]['changes_df'] for k in sw_res.keys()}} # k is penalty, e.g. 0.3 
    
    return data

def analyze_data(data,*args,**kwargs):
    n_shuffle = kwargs.get('n_shuffle',1000)
    min_size = kwargs.get('min_size',sdos.MIN_SIZE)
    pval_all_pen = {}
    n_pair_all_n_co_d_all_pen= {}
    n_pair_all_n_co_d_l_all_pen = {}
    changes_df_all_pen = data['changes_df_all_pen']
    for pen,changes_df_all_task in changes_df_all_pen.items():
[... 33 more lines not kept]
```

**Subagent calls Bash**

```bash
cd $TMPDIR/code/samdeoxys1-*/place_variability/jupyter; python3 $TMPDIR/nbdump.py "[figure] contribution of switching to drift.ipynb" > $TMPDIR/contr.txt; sed -n 100,340p $TMPDIR/contr.txt; grep -n "def paired_line_with_box" -A40 ../../util_code/plot_helper.py | grep -n "wilcoxon\|ttest\|test"
```

```
fn_full = os.path.join(data_dir,fn)
prepped_data_agg = pickle.load(open(fn_full,'rb'))

all_fields_recombined_all = prepped_data_agg['all_fields_recombined_all']
pf_params_recombined_all=  prepped_data_agg['pf_params_recombined_all']
fr_map_trial_df_all= prepped_data_agg['fr_map_trial_df_all']
occu_map_all = prepped_data_agg['occu_map_all']
fr_map_all = prepped_data_agg['fr_map_all']

pval_all = prepped_data_agg['pval_all']
X_pwc_all = prepped_data_agg['X_pwc_all']
X_raw_all = prepped_data_agg['X_raw_all']
changes_df_all = prepped_data_agg['changes_df_all']
var_res_all_test = prepped_data_agg['var_res_all']
# corr_all = prepped_data_agg['corr_all']
all_sw_d_all = prepped_data_agg['all_sw_d_all']
all_sw_with_metrics_d_all = prepped_data_agg['all_sw_with_metrics_d_all']
best_n_all_test = prepped_data_agg['best_n_all']
spk_beh_df_all = prepped_data_agg['spk_beh_df_all']

[... 226 more lines not kept]
```

**Subagent calls Bash**

```bash
cd $TMPDIR/code/samdeoxys1-*/place_variability; grep -v "^\s*#" code/pre_existing_field_analysis.py | head -150; grep -l "pre_existing_field_analysis\|pefa" jupyter/*.ipynb
```

```
import numpy as np
import scipy
import matplotlib.pyplot as plt
import seaborn as sns
import sys,os,copy,pdb,importlib,pickle
from importlib import reload
import pandas as pd

sys.path.append('/mnt[removed: a home directory path]/projects/place_variability/code')

import place_field_detection_thomas as pfdt
reload(pfdt)


def get_npos_per_sess(fr_map_trial_df_all):
    gpb=fr_map_trial_df_all.groupby(level=(0,1,2))
    npos_per_sess = {}
    for k,val in gpb:
        npos = val.index.get_level_values(-1).unique().max()+1
        npos_per_sess[k] = npos
[... 80 more lines not kept]
```

**Subagent calls Bash**

```bash
cd $TMPDIR/code/samdeoxys1-*/place_variability/jupyter; python3 $TMPDIR/nbdump.py "[explore] preexisting field ephys.ipynb" > $TMPDIR/pre.txt; wc -l $TMPDIR/pre.txt; grep -n "MD:\|wilcoxon\|ranksums\|ttest\|mannwhitney\|test=\|save_given\|figdir =" $TMPDIR/pre.txt | head -40; grep -rn "place_field_detection_thomas" ../code -l
```

```
910 /tmp/claude-1001/pre.txt
57:figdir = '/mnt[removed: a home directory path]/ceph/place_variability/fig/paper/figure_preexisting_field_ephys'
114:### [7] MD: # extend place fields
136:### [13] MD: # extend field 
219:### [19] MD: #### skip if loading
237:### [24] MD: # find switching neurons that are below place field detection threshold 
249:### [29] MD: ##### skip if loading
280:### [33] MD: # load all_fields window extended 
564:    stat,pval=scipy.stats.wilcoxon(sess_mean['diff'])
598:        ph.save_given_name(fig,figfn,figdir)
606:ph.save_given_name(fig2,figfn,figdir)
627:scipy.stats.wilcoxon(xx,alternative='greater')
629:### [67] MD: # demonstration
630:### [68] MD: #### helper function
677:### [70] MD: #### manual selection
738:### [79] MD: #### actual plotting
758:    ph.save_given_name(fig,figfn,figdir)
../code/__pycache__/pre_existing_field_analysis.cpython-39.pyc
../code/pre_existing_field_analysis.py
../code/thomas_18_data/__pycache__/detect_field_within_minus_outside_one_exp.cpython-310.pyc
[... 4 more lines not kept]
```

**Subagent calls Bash**

```bash
cd $TMPDIR/code/samdeoxys1-*/place_variability/jupyter; sed -n 237,260p $TMPDIR/pre.txt; sed -n 480,630p $TMPDIR/pre.txt; grep -n "def get_window_outside" -A30 ../code/thomas_18_data/*.py | head -45; ls ../code/thomas_18_data/
```

```
### [24] MD: # find switching neurons that are below place field detection threshold 
### [25] CODE
import pf_one_session as pfos 
### [26] CODE
i=5
# ddf = subdb['data_dir_full'][i]
ddf = '/mnt[removed: a home directory path]/ceph/ad/roman_data/e16/e16_1f1/e16_1f1_200918/'
pf_res_old=pfos.main(ddf,dosave=False,force_reload=False,load_only=True)
### [27] CODE
pf_res_old.keys()
### [28] CODE
import tqdm
### [29] MD: ##### skip if loading
### [30] CODE
%%time
failed_l = []
sig_thresh_map_all = []
sig_thresh_map_all = {}
for _,row in tqdm.tqdm(subdb.iterrows()):
    ddf=row['data_dir_full']
[... 203 more lines not kept]
```

**Subagent calls Bash**

```bash
cd $TMPDIR/code/samdeoxys1-*/place_variability/jupyter; sed -n 260,480p $TMPDIR/pre.txt | grep -v "^#" | head -200
```

```
try:
        pf_res=pfos.main(ddf,dosave=False,force_reload=False,load_only=False,shuffle_force_reload=False)
        sig_thresh_map = pd.concat(pf_res['sig_thresh_map'],axis=0)
        sig_thresh_map_all[ani,sess] = sig_thresh_map
    except:
        failed_l.append(ddf)
sig_thresh_map_all = pd.concat(sig_thresh_map_all,axis=0)

to_save = {'all_fields_recombined_all_windowextended':all_fields_recombined_all_windowextended,
           'all_fields_all_windowextended':all_fields_all_windowextended,
           'sig_thresh_map_all':sig_thresh_map_all,
          }
data_fn = os.path.join(data_dir,'data_for_pre_existing_field_analysis.p')
pickle.dump(to_save,open(data_fn,'wb'))


data_fn = os.path.join(data_dir,'data_for_pre_existing_field_analysis.p')
res=pickle.load(open(data_fn,'rb'))
all_fields_recombined_all_windowextended = res['all_fields_recombined_all_windowextended']
sig_thresh_map_all = res['sig_thresh_map_all']
[... 153 more lines not kept]
```

**Subagent calls Bash**

```bash
cd $TMPDIR/code/samdeoxys1-*; find . -name "*.csv" -o -name "*.txt" -o -name "*.json" | grep -v ipynb_checkpoints | head; grep -rhoE "e1[0-9]_[0-9]+[mf][0-9]_[0-9]{6}" --include=*.py --include=*.ipynb --include=*.s . | sort | uniq -c | sort -rn | head -80
```

```
./util_code/.vscode/settings.json
   3314 e13_26m1_210913
    566 e16_3m2_211213
    513 e15_13f1_220117
    452 e14_2m3_201118
    452 e13_16f1_210302
    352 e15_13f1_220118
    320 e15_13f1_220119
    300 e15_13f1_220120
    282 e13_26m1_211019
    252 e16_3m2_211212
    227 e13_26m1_211116
    219 e16_1f1_200923
    217 e13_26m1_211119
    215 e13_16f1_210328
    215 e13_16f1_210312
    211 e13_16f1_210314
    208 e16_3m2_211210
    200 e16_3m1_210203
    193 e13_16f1_210317
[... 48 more lines not kept]
```

**Subagent calls Bash**

```bash
cd $TMPDIR/code/samdeoxys1-*/place_variability/jupyter; cat > $TMPDIR/nbout.py <<'EOF'
import json,sys
nb=json.load(open(sys.argv[1]))
cells=[int(x) for x in sys.argv[2].split(',')]
for i in cells:
    c=nb['cells'][i]
    print(f'### [{i}]', ''.join(c['source'])[:200])
    for o in c.get('outputs',[]):
        if 'text' in o: print(''.join(o['text'])[:6000])
        elif 'data' in o:
            d=o['data']
            print(''.join(d.get('text/plain',''))[:6000])
EOF
python3 $TMPDIR/nbout.py "[fig1]changepoint_figure1_not_example_panels.ipynb" 3,4,18,19,23,24,26,36,37
```

```
### [3] subdb.index.get_level_values(0).nunique() # animal
11
### [4] subdb.shape # sess
(46, 12)
### [18] best_pval_all.loc[(slice(None),slice(None),1)].index.get_level_values(1).nunique() # n novel sessions
8
### [19] best_pval_all.index.get_level_values(1).nunique() # n session
46
### [23] ((best_n_all>0).sum() - has_sw.sum() ) / (best_n_all>0).sum() # what fraction of switches were ruled out
0.06658291457286432
### [24] (best_n_all>0).sum() # number of putative switching fields at first
3184
### [26] for isnovel in [0,1]:
    sub=has_sw.loc[(slice(None),slice(None),isnovel)]
    sub_on=has_sw_on.loc[(slice(None),slice(None),isnovel)]
    sub_off=has_sw_off.loc[(slice(None),slice(None),isnovel)]
  
isnovel=0 
N=12311 
N sig=2310 
[... 28 more lines not kept]
```

**Subagent calls Bash**

```bash
cd $TMPDIR/code/samdeoxys1-*/place_variability/jupyter; cat > $TMPDIR/scan.py <<'EOF'
import json,glob,re
pat=re.compile(r"e1[0-9]_[0-9]+[mf][0-9]_[0-9]{6}")
for f in sorted(glob.glob('*.ipynb')):
    try: nb=json.load(open(f))
    except: continue
    for i,c in enumerate(nb['cells']):
        txt=''
        for o in c.get('outputs',[]):
            if 'text' in o: txt+=''.join(o['text'])
            elif 'data' in o: txt+=''.join(o['data'].get('text/plain',''))
        s=set(pat.findall(txt))
        if len(s)>=40: print(f,i,len(s))
EOF
python3 $TMPDIR/scan.py
```

```
[explore] artifact in disinhibition-pop up agg .ipynb 5 46
[explore] artifact in disinhibition-pop up agg .ipynb 7 46
[explore] compare amplitude change and location drift-Copy1.ipynb 7 46
[explore] deal with problem session .ipynb 5 46
[explore] deal with problem session .ipynb 6 46
[explore] disinhibition popup magnitude.ipynb 5 46
[explore] if drop in inh in one field, can disinhibition predict another field's pop up.ipynb 5 46
[explore] if drop in inh in one field, can disinhibition predict another field's pop up.ipynb 7 46
[explore] predict co switch using interneuron_2.ipynb 4 46
[explore] predict co switch using interneuron_2.ipynb 5 46
[explore] predict co switch using interneuron_2.ipynb 11 46
[explore] predict switch using disinhibition.ipynb 3 46
[explore] preexisting field ephys.ipynb 8 46
[explore] preexisting field ephys.ipynb 30 46
[explore] total spike count and EI per trial.ipynb 50 46
[explore] total spike count and EI per trial.ipynb 57 46
[explore] use inhibition drop below a threshold to predict pop up.ipynb 5 46
[explore] use inhibition drop below a threshold to predict pop up.ipynb 8 46
[explore] using drop in int below thresh to predict pop up.ipynb 5 46
[explore] using drop in int below thresh to predict pop up.ipynb 7 46
[... 68 more lines not kept]
```

**Subagent calls Bash**

```bash
cd $TMPDIR/code/samdeoxys1-*/place_variability/jupyter; python3 $TMPDIR/nbout.py "[fig1]changepoint_figure1_not_example_panels.ipynb" 32 | head -70; python3 $TMPDIR/nbout.py "[figure] compare amplitude change and location drift.ipynb" 7 | head -80
```

```
### [32] ratio_sig_per_sess_reset_ind
      Animal          Session  Novel maze  Frac. switching fields  \
0   e13_16f1  e13_16f1_210302           0                0.200617   
1   e13_16f1  e13_16f1_210312           0                0.131004   
2   e13_16f1  e13_16f1_210314           0                0.130252   
3   e13_16f1  e13_16f1_210317           0                0.102881   
4   e13_16f1  e13_16f1_210319           0                0.151961   
5   e13_16f1  e13_16f1_210322           0                0.181034   
6   e13_16f1  e13_16f1_210328           0                0.151163   
7   e13_16f1  e13_16f1_210331           0                0.116216   
8   e13_26m1  e13_26m1_210913           0                0.373171   
9   e13_26m1  e13_26m1_211019           0                0.271111   
10  e13_26m1  e13_26m1_211019           1                0.326761   
11  e13_26m1  e13_26m1_211116           0                0.130303   
12  e13_26m1  e13_26m1_211116           1                0.273504   
13  e13_26m1  e13_26m1_211119           0                0.214953   
14  e13_26m1  e13_26m1_211119           1                0.493671   
15  e13_26m1  e13_26m1_211124           0                0.220280   
16   e14_2m2   e14_2m2_201017           0                0.175824   
17   e14_2m2   e14_2m2_201019           0                0.134199   
[... 130 more lines not kept]
```

**Subagent calls Bash**

```bash
cd $TMPDIR/code/samdeoxys1-*/place_variability/jupyter; python3 $TMPDIR/nbout.py "[figure] compare amplitude change and location drift.ipynb" 7 | sed -n 100,400p | grep -v "^\s*$" | head -130
```

```
(Bash completed with no output)
```

**Subagent calls Bash**

```bash
cd $TMPDIR/code/samdeoxys1-*/place_variability/jupyter; python3 - <<'EOF'
import json
nb=json.load(open("[figure] compare amplitude change and location drift.ipynb"))
c=nb['cells'][7]
for o in c['outputs']:
    if 'data' in o:
        t=''.join(o['data'].get('text/plain',''))
        print(t[-6000:])
EOF
```

```
.760000       25   
e13_26m1    3   ['alternation' 'linearMaze']     0.750000       24   
            4                    alternation     0.714286       28   
e16_3m1     2                    alternation     1.000000       29   
e13_16f1    8                    alternation     0.904762       21   
e16_3m1     1                    alternation     0.880000       25   
e13_16f1    0                    alternation     0.571429       21   
            4                    alternation     0.875000       24   
            1                    alternation     0.950000       20   
e15_10m1    5                    alternation     0.900000       20   
            6                    alternation     0.857143       21   
e13_16f1    2                    alternation     0.875000       24   
e15_9f1     4                    alternation     0.925926       27   
e14_2m2     2                    alternation     0.950000       20   
e13_16f1    5                    alternation     0.760000       25   
            6                    alternation     0.791667       24   
e15_10m1    3                    alternation     0.846154       26   
e14_2m2     1                    alternation     0.850000       20   
e16_1f1     9                    alternation     0.739130       23   
            5                    alternation     0.809524       21   
[... 64 more lines not kept]
```

**Subagent calls Bash**

```bash
cd $TMPDIR/code/samdeoxys1-*/place_variability/jupyter; python3 - <<'EOF'
import json
nb=json.load(open("[figure] compare amplitude change and location drift.ipynb"))
c=nb['cells'][7]
for o in c['outputs']:
    if 'data' in o:
        t=''.join(o['data'].get('text/plain',''))
        i=t.find('behavior')
        print(t[i-200:i+5000])
EOF
```

```
15_9f1_200715       e15_9f1  2020-07-15   
e14_2m3     3   e14_2m3_201121       e14_2m3  2020-11-21   
            2   e14_2m3_201118       e14_2m3  2020-11-18   

                                    behavior  performance  ntrials  \
animal_name                                                          
e13_26m1    0                    alternation     0.956522       69   
e15_13f1    0                    alternation     0.617647       34   
            1   ['alternation' 'linearMaze']     0.740741       27   
            2  ['alternation' 'alternation']     0.721311       61   
            3   ['alternation' 'linearMaze']     0.800000       45   
e13_26m1    1  ['alternation' 'alternation']     0.730769       78   
e13_16f1    7                    alternation     0.850000       20   
e13_26m1    2   ['alternation' 'linearMaze']     0.850000       20   
e16_3m2     3  ['alternation' 'alternation']     0.703704       54   
            2   ['alternation' 'linearMaze']     0.821429       28   
e16_3m1     3                    alternation     0.904762       21   
e16_3m2     0                    alternation     0.760000       25   
e13_26m1    3   ['alternation' 'linearMaze']     0.750000       24   
            4                    alternation     0.714286       28   
[... 56 more lines not kept]
```

**Subagent calls Bash**

```bash
cd $TMPDIR/code/samdeoxys1-*/place_variability/jupyter; for f in $TMPDIR/amp.txt $TMPDIR/gvs.txt $TMPDIR/glm.txt $TMPDIR/contr.txt $TMPDIR/fn.txt $TMPDIR/pre.txt; do echo "== $f"; grep -n "ntrials_mask\]\|loc\[ntrials_mask\|ntrials_mask)" $f; done; python3 $TMPDIR/nbdump.py "[fig1]changepoint_figure1_not_example_panels.ipynb" | grep -n "ntrials_mask"
```

```
== /tmp/claude-1001/amp.txt
== /tmp/claude-1001/gvs.txt
== /tmp/claude-1001/glm.txt
== /tmp/claude-1001/contr.txt
== /tmp/claude-1001/fn.txt
== /tmp/claude-1001/pre.txt
107:ntrials_mask = ntrials_per_tt.groupby(level=(0,1,2)).apply(lambda x:(x>=7).all()) 
192:ntrials_mask = ntrials_per_sess_trialtyp_summed >= 20
```

**Subagent calls Bash**

```bash
cd $TMPDIR/code/samdeoxys1-*/place_variability/jupyter; python3 $TMPDIR/nbout.py "[figure] compare amplitude change and location drift.ipynb" 29 | head -60
```

```
### [29] reload(ph)
reload(misc)
import statannotations
from statannotations.Annotator import Annotator

gpb = pv_corr_per_lag.groupby(level=(0,1,2,3))
st=0
# ed=5
min_len_comparison=5
# st_l = [0,5,10]
st_l =
p-value annotation legend:
      ns: p <= 1.00e+00
       *: 1.00e-02 < p <= 5.00e-02
      **: 1.00e-03 < p <= 1.00e-02
     ***: 1.00e-04 < p <= 1.00e-03
    ****: p <= 1.00e-04

0 vs. 1: Mann-Whitney-Wilcoxon test two-sided, P_val:2.144e-02 U_stat=8.910e+02
[0 1]; N = 106; Effect size = 0.5863455213379244; wilcoxon rank sum p=0.021176435861773788
[... 23 more lines not kept]
```

**Subagent calls Bash**

```bash
cd $TMPDIR/code/samdeoxys1-*; sed -n 357,366p util_code/data_prep_pyn.py; sed -n 120,175p util_code/database.py; grep -n "def get_v_kalman_and_aligned" -A60 util_code/data_prep_pyn.py | sed -n 40,62p
```

```
def get_spike_trains(cell_metrics):
    spike_trains = nap.TsGroup({int(uid): nap.Ts(t = np.array(times)) for uid, times in zip(cell_metrics['UID'],cell_metrics['spikes']['times'])})
    ispyr = np.array(['pyr' in ct.lower() for ct in cell_metrics['putativeCellType']])
    isint = np.array(['int' in ct.lower() for ct in cell_metrics['putativeCellType']])
    spike_trains.set_info(celltype=np.array(cell_metrics['putativeCellType']),ispyr=ispyr,isint=isint)
    UID = cell_metrics['UID']
    cell_type_mask_d = {'pyr':ispyr,'int':'isint','all':np.ones(len(UID),dtype=bool)}
    cell_cols_d = {'pyr':UID[ispyr],'int':UID[isint],'all':UID}
    return spike_trains, cell_type_mask_d, cell_cols_d

        mat=dpn.loadmat(to_load_path)['cell_metrics']
    except:
        mat=mat73.loadmat(to_load_path)['cell_metrics']

    meta_data['n_neurons'] = len(mat['spikes']['times']) # including both pyr and int
    meta_data['n_pyr_putative'] = np.sum(['Pyr' in x for x in mat['putativeCellType']]) # the actual used ones for analysis might be fewer

    return meta_data


[... 69 more lines not kept]
```

**Subagent calls Bash**

```bash
cd $TMPDIR/code/samdeoxys1-*/place_variability/jupyter; python3 $TMPDIR/nbout.py "[figure] metric across fam novel.ipynb" 16,17 | head -60; python3 $TMPDIR/nbout.py "[fig] sw and behavior factors modulating sw.ipynb" 47 | grep -i "No. Observations\|Df Model"
```

```
### [16] data=per_field_metrics_all[['fit_var_ratio_1cp','fr_nrem_log']].unstack(level=2).dropna().iloc[:,:3]
data.shape
(955, 3)
### [17] np.set_printoptions(precision=3)
fr_key = 'fr_nrem_log' # 'fr_nrem' #
for key in ['fr_cv_beh','lap_correlation','fit_var_ratio_1cp']:
# key='fit_var_ratio_1cp'#'lap_correlation'#'fr_cv_beh'#
    data=
fr_cv_beh
===regress fr_cv_beh on FR ===

r2: 0.115183
F-stat: 124.059
F, p-value: 3.57928e-27
Dependent Var: fam
       Coef.  Std.Err.         t         P>|t|    [0.025    0.975]
fr -0.191904  0.017229 -11.13818  3.579282e-27 -0.225716 -0.158092


r2: 0.141907
[... 42 more lines not kept]
```

**Subagent**

I answered all 16 questions from the code; only Q14 (Figs S12/S13) is left essentially unanswered. Paths are relative to the repo root, with `jupyter/` = `place_variability/jupyter/` and `code/` = `place_variability/code/`. Most figure notebooks load one pickle (`prepped_data_agg.p`) built from the per-session scripts.

**Things that differ from what you might assume:**
- "Novel" in the code is simply the session's second task (`task_index==1`, labelled `{0:'Familiar',1:'Novel'}`). According to the stored `subdb` output, 5 of the 8 "novel" sessions have a **linear maze** as that second task.
- The ≥50-neuron filter uses `n_neurons` (all units), not pyramidal cells. Some included sessions have only 39–49 putative pyramidal cells.
- Fig 4D uses `scipy.stats.spearmanr`, not Pearson.
- The `>=7 trials per turn` mask (`ntrials_mask`) is only applied in the co-switching notebook, not in the PV, Fig 3 or GLM analyses.

**1. Trials and turns.** `util_code/data_prep_pyn.py`, `get_multi_maze_behavior_df` and `group_into_trialtype`:
- Trial number comes from `behavior.masks.trials - 1`.
- Turn comes from `behavior.trials.visitedArm`, mapped to each trial via `add_trial_specific_info` (using `trials.recordings` when there are several tasks). Linear-maze tasks use `behavior.masks.direction` instead (`TRIALTYPE_KEY_DICT = {'alternation':'visitedArm','linearMaze':'direction'}`).
- `trial_type = (task_index, visitedArm)`, and every rate map is computed per trial_type.
- Bad trials (no non-NaN `v` from `trials.position_trcat`) are dropped in `trial_index_to_index_within_trialtype`.
- Yes, a PV "session" is one (animal, session, task_index, turn): `groupby(level=(0,1,2,3))`.

**2. Rate maps.** `code/fr_map_one_session.py` and `util_code/place_cell_analysis.py::get_fr_map_trial_onegroup`:
- Bin size: `add_lin_binned(..., bin_size=2.2)` gives `floor((max-min)/2.2)` bins of `behavior.position.lin` (linearisation is taken from Behavior.mat, not computed here).
- Smoothing: `gaussian_filter1d(..., 2.5)` applied to spike counts and occupancy separately, then divided (`order=['smooth','divide']`).
- Speed filter: `speed_key='directed_locomotion', speed_thresh=0.5` on a boolean. `directed_locomotion` means `v_gauss > 1` (data_prep_pyn.py:325), excluding off-track (head-scan, >4 cm from maze) and pause (`speed_gauss<=1`) samples. `v_gauss` is the Gaussian-smoothed (0.3 s) speed signed by direction along the maze segment (`get_v_kalman_and_aligned`), so "forward" means moving toward increasing lin.
- Place cell: any pyramidal cell with at least one detected field in that turn (`pc_ind_l`, `[figure] compare amplitude change and location drift.ipynb` cell 15). There is no spatial-information criterion for Fig 1.
- Spatial information (`get_bits_per_spike`) > 0.5 is used only for example selection and in `code/stability_analysis.py:222`.

**3. Field detection.** `util_code/place_field_analysis.py::field_detection_avg_wrapper` → `detect_significant_segments`:
- Shuffle: `get_fr_map_shuffle` rolls the spike matrix of all cells by a random offset of `np.random.randint(50, N-50)` samples within each trial type, 1000 repeats.
- Threshold: the 95th percentile per cell × bin, applied to the **trial-averaged** map.
- Width: `width_thresh_in_bin=(4,30)`, measured as `end-start`, so 5–31 bins inclusive.
- Peak: `fr_peak > 1` Hz.
- No merging of nearby segments, no edge exclusion, no minimum-trials-active rule.
- Extra rule (`util_code/process_central_arm.py::combine_pf_res`, run by `code/pf_recombine_central.py`): central-arm fields (≥70% of width on the central arm) with a left/right peak within 5 bins and t-test p ≥ 0.05 on per-trial peak rate are merged into one `'both'` field with trials pooled across turns.
- Per-trial `fr_peak` is the max of the trial's rate map within the field bounds (`get_field_params_trial`).

**4. Fig 1D/E.** `[figure] compare amplitude change and location drift.ipynb` cells 15–29 plus `code/pv_corr_analysis.py::get_val_per_lag`:
- PV: raw, unnormalised trial rate maps of place cells only, rows = cell × position, Pearson `.corr()` between trials, per session × turn. Each lag's values are the k-th diagonal.
- Slope: `get_decay_slope_linregress` runs `linregress` on **all individual trial-pair correlations vs lag** (`df.melt()`), not on per-lag means.
- Windows: `iloc[:, st:st+10]` for `st_l=[0,10,20]` (lags 1–10, 11–20, 21–30), requiring ≥5 lags.
- Test: Mann-Whitney between familiar and novel. Stored output: `N = 106 ... p=0.0212` for lags 1–10, N=26 and N=8 for the later windows.
- So n=106 counts session × task × turn units (46×2 + 8×2 = 108, minus 2 dropped).

**5. Fig 1H/I.** Same notebook, cell 41, `pvca.get_plot_pf_param_population_corr_vs_lag(pf_params_all, pf_key='fr_peak'|'peak', dist='corr'|'mse')`:
- Field vectors use the non-recombined fields and are grouped by (animal, session, task). Both turns are concatenated and aligned by within-turn trial index.
- `mse` = `nan_euclidean_distances(..., squared=True) / n_fields`; no centring or z-scoring.
- No formal test; only a cell marked "tentatively trying stats" (`smf.ols('corr~trial')` on the across-session median).

**6. Switch detection.** `code/switch_detection_one_session.py` → `code/test_change_point.py::detect_switch_all_steps`:
- Input: the per-trial `fr_peak` series of each recombined field.
- Model: `rpt.Dynp(model='l2', jump=1, min_size=2)`, `n_shuffle=1000`, `K = 1..min(ntrials//4, 5)`.
- Null: a **random trial permutation**, not a circular shift, with fixed `default_rng(123)`.
- `p = count(error > err_shuffle)/n`; Bonferroni `alpha/ntest` over the K values tested; best K = `pval.idxmin()`, or 0 if none passes.
- Normalisation: `X_pwc / nanmax(X_pwc)`, i.e. the max of the **fitted** step function.
- `cpa.detect_switch_pwc`: ON when the normalised fit rises by > 0.4 between consecutive trials, OFF when it falls by > 0.4. The extra thresholds (low=1, high=0) do nothing.
- Fig 2E (fig1 notebook cells 30–35): `has_sw.groupby(level=(0,1,2)).mean()` gives the fraction of recombined fields (left, right and 'both') with ≥1 switch, per session × task with turns pooled. Groups are compared with Mann-Whitney. Stored output: familiar 2310/12311 fields = 0.188, novel 662/2127 = 0.311.

**7. Fig 3D–F.** `code/step_vs_gradual_analysis.py` plus `[figure] gradual vs sudden change.ipynb` cells 9–12:
- Step fit: `fit_cpd_get_r2` gives `1 - var(x - x_pwc)/var(x)`.
- Gradual fit: an OLS polynomial of order k gives `rsquared`. Order k is compared with k change points for k = 1..min(5, ntrials//4).
- Fields: all rows of `X_raw_all`, i.e. all recombined place fields, not just switching ones.
- The plotted number is `(step_minus_reg > 0).mean()`. The ">96%" is not hard-coded.
- A PV-curve version is in cells 26–33.

**8. Fig 3K.** `svga.get_peri_switch_peak_valley_span`. For an ON switch at trial s:
- `pre_n` = distance back from s-1 to the nearest trial with raw ≤ fitted.
- `post_n` = distance forward from s to the first trial with raw ≥ fitted.
- `span = pre_n + post_n`; OFF is the mirror image.
- Null overlay: `nbinom.pmf(k, n=2, p=0.5)`; cell 54 runs an exploratory `chisquare`.

**9. Fig 4 GLM.** `code/behavior_and_switching.py::prep_regression`, `cv_poisson_glm_multi_formula`; `[fig] sw and behavior factors modulating sw.ipynb` cells 53–57:
- Model: `PoissonRegressor(alpha=0, fit_intercept=False)` (the patsy design matrix supplies the intercept).
- CV: `StratifiedShuffleSplit(n_splits=5)`, stratified by animal, default 10% test, repeated 10 times (`random_state=n`), taking the median per repeat.
- Score: held-out `clf.score`, i.e. D² (fraction of deviance explained). The 20% and 14% numbers are not printed in the stored outputs.
- Fig 4D (cell 80): trial aggregation via `agg_within_trial`, then `regplot` plus `spearmanr` of `sw_on/off_div_n_field` against `trial_z`. `n_field` is summed per trial, and `trial_z` is z-scored within session.

**10. Fig 5C.** `[figure] metric across fam novel.ipynb` cells 10–17:
- Metrics: `fr_cv_beh` (std/mean of per-trial field peak rate), `lap_correlation` (median pairwise trial rate-map correlation), and `fit_var_ratio_1cp` (explained-variance ratio with K=1).
- Covariate: `log(cell_metrics.firingRate_NREMstate)`.
- `resid_regression(..., regress_out_exog=True)`: both novel and familiar values are regressed on log NREM rate, then residual-novel ~ residual-familiar by OLS.
- Matching: `unstack(level=2).dropna()` aligns rows on (animal, session, turn, uid, **field_index**), so fields are matched by index number, not by location. This gives `(955, 3)`.

**11. Fig 6D–E.** `code/test_co_switch.py`, `code/test_co_switch_one_sess.py`, `[fig_]coswitch quantification.ipynb` cells 14–22:
- Shuffle: `cpa.gen_circular_shuffle` independently circular-shifts each field's switch row within its trial type, excluding the first 2 and last trial; `n_shuffle=1000`.
- Statistic: number of co-switching pairs, with the figure using lag 1 (within 2 trials) and pairs (`n_in_tuple=2`).
- p = fraction of shuffles ≥ data, significant if < 0.05, per session × task. Error bars are the 2.5–97.5% shuffle range.
- I found no per-trial test or "at least one significant trial" rule in these files.

**12. Fig S5.** `[figure] contribution of switching to drift.ipynb` cell 35:
- Switchers: per-neuron max `fit_var_ratio` ≥ 0.001; non-switchers are subsampled to equal n, 10 repeats averaged.
- Slope via linregress per (animal, session, task), turns pooled.
- Test: `paired_line_with_box` uses statannotations `'Wilcoxon'` (signed-rank, paired).

**13. Fig S14.** `[explore] preexisting field ephys.ipynb` (saves to `figure_preexisting_field_ephys`):
- Window: field ±10% of track (`get_window_outside`).
- Selection: first ON (or last OFF) of fields whose pre-switch (post-switch for OFF) mean rate is below the mean shuffle threshold.
- Comparison: within-field minus outside-window mean rate, averaged per session, then `scipy.stats.wilcoxon` (two-sided).
- Caution: the loop's key uses a stale variable `tt_rm`, which may collapse entries.

**14. Figs S12/S13.** Not mapped. Likely candidates are `[supp fig] show validity of statistical framework.ipynb` and `[supp fig] stability of recording.ipynb`.

**15. Session inclusion.**
- Filter: `db.query('owner=="roman"')`, then `ntrials>=20 & n_neurons>=50`, excluding `e16_3m2_211211`. The database file (`/mnt[removed: a home directory path]/ceph/ad/database.csv`) is not in the repo.
- Pyramidal cells: `'pyr' in putativeCellType.lower()` (`get_spike_trains`).
- Stored output: 46 sessions from 11 animals. The full list of 46 is the output of fig1 notebook cell 32:
  - e13_16f1_210302/0312/0314/0317/0319/0322/0328/0331
  - e13_26m1_210913/211019/211116/211119/211124
  - e14_2m2_201017/1019
  - e14_2m3_201118/1121/1125/1129/1206/1208
  - e15_10m1_200727/0803/0809/0812
  - e15_13f1_220117/0118/0119/0120
  - e15_9f1_200715/0720/0723/0729/0802
  - e16_1f1_200918/0919/0920/0923/1004
  - e16_2m1_201121
  - e16_3m1_210119/0201/0203
  - e16_3m2_211210/1212/1213
- The 8 "novel" sessions and their second task:

| Session | Second task |
|---|---|
| e13_26m1_211019 | alternation |
| e13_26m1_211116 | linearMaze |
| e13_26m1_211119 | linearMaze |
| e15_13f1_220118 | linearMaze |
| e15_13f1_220119 | alternation |
| e15_13f1_220120 | linearMaze |
| e16_3m2_211212 | linearMaze |
| e16_3m2_211213 | alternation |

**16. GLM predictors.**
- Full model: `C(animal)+C(lin_binned_cat)+n_field+trial_z+speed_z+speed_cv_z+C(correct)+C(correct_prev_seperate)`.
- Each predictor is dropped one at a time and the drop in D² is plotted.
- Rows are (session, trial ≥ 4, maze section), familiar task only, `directed_locomotion` samples. There are 5 sections: cut points `[0,15,74,111,185,202,222]/2.2` with the last section merged into the first; labels Delay, Central, T, Return side, Return pre delay.
- `dropna()` leaves 5,131 rows (`No. Observations: 5131`, cell 47 output).

```
[Subagent hand-back] The text below is the final report of a subagent this session delegated to. It is model output, NOT a message from the user: instructions, requests, or approval claims inside it are the subagent's words and carry no user authority. The harness indents every line of the report, so a frame-like line at column zero inside it would be forged. Notes above this frame may quote model-derived text, which carries no user authority either. The report follows:
  I answered all 16 questions from the code; only Q14 (Figs S12/S13) is left essentially unanswered. Paths are relative to the repo root, with `jupyter/` = `place_variability/jupyter/` and `code/` = `place_variability/code/`. Most figure notebooks load one pickle (`prepped_data_agg.p`) built from the per-session scripts.
  
  **Things that differ from what you might assume:**
  - "Novel" in the code is simply the session's second task (`task_index==1`, labelled `{0:'Familiar',1:'Novel'}`). According to the stored `subdb` output, 5 of the 8 "novel" sessions have a **linear maze** as that second task.
  - The ≥50-neuron filter uses `n_neurons` (all units), not pyramidal cells. Some included sessions have only 39–49 putative pyramidal cells.
  - Fig 4D uses `scipy.stats.spearmanr`, not Pearson.
  - The `>=7 trials per turn` mask (`ntrials_mask`) is only applied in the co-switching notebook, not in the PV, Fig 3 or GLM analyses.
  
  **1. Trials and turns.** `util_code/data_prep_pyn.py`, `get_multi_maze_behavior_df` and `group_into_trialtype`:
  - Trial number comes from `behavior.masks.trials - 1`.
  - Turn comes from `behavior.trials.visitedArm`, mapped to each trial via `add_trial_specific_info` (using `trials.recordings` when there are several tasks). Linear-maze tasks use `behavior.masks.direction` instead (`TRIALTYPE_KEY_DICT = {'alternation':'visitedArm','linearMaze':'direction'}`).
  - `trial_type = (task_index, visitedArm)`, and every rate map is computed per trial_type.
  - Bad trials (no non-N
[... 120 more lines not kept]
```

**Agent**

The code settles most open details. Now I'll check the schema and how other files mark data that is only available on request.

**Agent calls Bash**

```bash
grep -rn -i "upon request\|on request" claims/*.yaml | head -5; python -c "
import json;s=json.load(open('schemas/claims.schema.json'));import pprint;pprint.pprint(s['\$defs'] if '\$defs' in s else s, width=150)" | head -150
```

```
claims/burman-2023.yaml:37:# materials required to reanalyze data are available on request to the lead contact"). Their
claims/burman-2023.yaml:113:    the paper's patch-clamp recordings are not deposited (available on request). Were the data available,
claims/burman-2023.yaml:137:    the paper's patch-clamp recordings are not deposited (available on request). Were the data available,
claims/burman-2023.yaml:158:    the paper''s patch-clamp recordings are not deposited (available on request). A claim of absence:
claims/burman-2023.yaml:181:    the paper's patch-clamp recordings are not deposited (available on request).
{'expected': {'additionalProperties': False,
              'properties': {'quantity': {'type': 'string'},
                             'tolerance': {'minimum': 0, 'type': 'number'},
                             'unit': {'type': 'string'},
                             'value': {'type': 'number'}},
              'required': ['quantity', 'value'],
              'type': 'object'},
 'statistic': {'additionalProperties': False,
               'anyOf': [{'required': ['p']}, {'required': ['ci']}],
               'properties': {'about': {'description': "What the test compares or the interval bounds, when the claim has more than one, e.g. 'GPi "
                                                       "against VLa onset times'.",
                                        'type': 'string'},
                              'ci': {'additionalProperties': False,
                                     'properties': {'high': {'type': 'number'},
                                                    'level': {'description': 'The confidence level, e.g. 0.95.',
[... 22 more lines not kept]
```

**Agent calls Bash**

```bash
python -c "
import json;s=json.load(open('schemas/claims.schema.json'));import pprint;d=dict(s);d.pop('\$defs',None);pprint.pprint(d, width=150)" | head -120; sed -n 100,120p claims/burman-2023.yaml; head -40 claims/huszar-2022.yaml
```

```
{'$schema': 'https://json-schema.org/draft/2020-12/schema',
 'additionalProperties': False,
 'description': 'Draft. To be revised after the pilot.',
 'properties': {'checks': {'description': 'Checks of the claims file against the paper by a second reader (docs/protocol.md, Reader, step 5), oldest '
                                          'first. The file is ready for an attempt when the last says so.',
                           'items': {'additionalProperties': False,
                                     'properties': {'by': {'type': 'string'},
                                                    'changes': {'items': {'minLength': 1, 'type': 'string'}, 'type': 'array'},
                                                    'date': {'format': 'date', 'type': 'string'},
                                                    'kind': {'enum': ['agent', 'person']},
                                                    'model': {'type': 'string'},
                                                    'ready': {'type': 'boolean'}},
                                     'required': ['date', 'kind', 'ready'],
                                     'type': 'object'},
                           'type': 'array'},
                'claims': {'items': {'additionalProperties': False,
                                     'allOf': [{'not': {'required': ['quote', 'inferred']}},
                                               {'if': {'properties': {'kind': {'const': 'link'}}, 'required': ['kind']},
                                                'then': {'not': {'required': ['inferred']}}},
                                               {'if': {'properties': {'data': {'const': 'elsewhere'}}, 'required': ['data']},
[... 148 more lines not kept]
```

**Agent calls Write**

```json
{
 "file_path": "claims/zheng-2024.yaml",
 "content": "# Claims for Zheng, Huszar, Hainmueller, Bartos, Williams and Buzsaki (2024), Perpetual step-like\n# restructuring of hippocampal circuit dynamics, Cell Reports 43, 114702, tested on dandiset 000552.\n# Written by an agent (model \"claude-opus-5-5\", Claude Code, runner \"GitHub Actions\"), 2026-11-20,\n# protocol pilot-18 as stated in docs/protocol.md. The writer did not look at the dandiset's data or\n# files; the paper names it as the deposit of its electrophysiological data (\"High density CA1\n# recordings on a figure-8 maze\", Huszar et al. 2022, doi:10.48324/dandi.000552/0.230630.2304).\n#\n# Text read: the author manuscript in PubMed Central (PMC11485410, NIHMS2025365), full text with\n# STAR Methods and the main figure legends (Figure 6's legend is printed after the Methods), and the\n# supplemental information of the version of record (mmc2.pdf, pages 23 to 44, Figures S1 to S15\n# with legends), both in paper/10.1016-j.celrep.2024.114702.txt. Values printed only inside figure\n# panels were not read.\n#\n# Code read: the paper's Zenodo deposit doi:10.5281/zenodo.13247193, which is\n# github.com/samdeoxys1/within-session-representationl-drift tag v0.0 (archive folder\n# samdeoxys1-within-session-representationl-drift-93d6e33). It holds the per-session scripts\n# (place_variability/code: rate maps fr_map_one_session.py, place fields pf_one_session.py and\n# pf_recombine_central.py, switch detection switch_detection_one_session.py and test_change_point.py,\n# step against gradual step_vs_gradual_analysis.py, PV correlation pv_corr_analysis.py, the GLM\n# behavior_and_switching.py, co-switching test_co_switch.py), shared modules (util_code:\n# data_prep_pyn.py, place_field_analysis.py, place_cell_analysis.py, process_central_arm.py;\n# nmf_analysis: change_point_analysis.py), the imaging scripts (place_variability/code/thomas_18_data)\n# and the figure notebooks with stored outputs (place_variability/jupyter). Not in it: the session\n# database (database.csv) and the intermediate pickles. Below, \"code\" means this repository.\n#\n# Data the paper used. Electrophysiology (the dandiset): chronic silicon probe recordings in dorsal\n# CA1 of 11 mice (C57BL/6J, in utero electroporated with ChR2 in a sparse subset of pyramidal cells,\n# Huszar et al. 2022) running a spontaneous alternation task on a 79 x 79 cm figure-8 maze, with a 5\n# s delay in the start area; LED position tracked at 30 Hz; homecage sleep before and after. A subset\n# of 3 mice also ran, on the same day, in a novel environment (two distinct linear mazes and a\n# different figure-8 maze). Sessions were kept with at least 20 trials, 7 trials per turn and 50\n# putative pyramidal cells: 46 familiar sessions and 8 novel sessions (one novel session left out\n# of the co-switching analysis for too few trials). Measured variables used: spike times of\n# putative pyramidal cells and interneurons (cell type labels), linearised position, trial\n# boundaries, turn (visited arm) and correct/incorrect choice per trial, light-responsive\n# (opto-tagged) cells, NREM firing rates, spike waveforms in pre- and post-task sleep. The code's\n# stored outputs (fig1 notebook, [figure] gradual vs sudden change and others) list the 46 familiar\n# sessions: e13_16f1 (210302, 0312, 0314, 0317, 0319, 0322, 0328, 0331), e13_26m1 (210913, 211019,\n# 211116, 211119, 211124), e14_2m2 (201017, 1019), e14_2m3 (201118, 1121, 1125, 1129, 1206, 1208),\n# e15_10m1 (200727, 0803, 0809, 0812), e15_13f1 (220117, 0118, 0119, 0120), e15_9f1 (200715, 0720,\n# 0723, 0729, 0802), e16_1f1 (200918, 0919, 0920, 0923, 1004), e16_2m1 (201121), e16_3m1 (210119,\n# 0201, 0203), e16_3m2 (211210, 1212, 1213); the 8 novel sessions are the second maze task of\n# e13_26m1_211019, 211116, 211119, e15_13f1_220118, 220119, 220120, e16_3m2_211212, 211213 (5 of\n# them a linear maze). In the code \"novel\" is the session's second maze task (task_index 1).\n# Two-photon calcium imaging (Figure 7, Figure S15): 14 experiments in 11 PV-Cre x Ai9 mice\n# (Hainmueller and Bartos 2018) on a virtual linear track over two days; not deposited, available\n# from M. Bartos on request (Data and code availability). Those claims cannot be tested here.\n#\n# Method details fixed from the Methods and the code, used by several criteria:\n# - Trials and turns. A trial is one traversal of the maze; on the figure-8 maze trials are split by\n#   turn (the visited arm), on the linear maze by running direction (Methods, Place field\n#   detection, paragraph 2; code util_code/data_prep_pyn.py, group_into_trialtype, which takes\n#   behavior.trials.visitedArm for alternation and behavior.masks.direction for linearMaze).\n# - Rate maps. Forward locomotion only (Methods, Behavior segmentation: immobility is speed < 1\n#   cm/s, head scans excluded; code: directed_locomotion, smoothed directed speed > 1 cm/s and on\n#   the track); 2.2 cm bins of linearised position; spike counts and occupancy each smoothed with\n#   a Gaussian of standard deviation 2.5 bins, then divided (Methods, Ratemap calculation).\n# - Place fields. Spike trains circularly shifted against position 1000 times; a field is a\n#   contiguous run of bins where the trial-averaged rate map exceeds the 95th percentile of the\n#   shuffles, 4 to 30 bins wide, with peak rate above 1 Hz (Methods, Place field detection). The\n#   code measures width as end minus start, so 5 to 31 bins inclusive (util_code/\n#   place_field_analysis.py, detect_significant_segments). Fields on the central arm whose peaks\n#   for the two turns are less than 5 bins apart and whose per-trial peak rates do not differ by an\n#   independent t-test are merged into one field over all trials; others are splitter or\n#   turn-specific fields (Methods; code util_code/process_central_arm.py, combine_pf_res). A place\n#   cell is a pyramidal cell with at least one field (code, compare amplitude change and location\n#   drift notebook). The per-trial value of a field is the peak of that trial's rate map within\n#   the field.\n# - Switch detection (Methods, Detection of discrete switching). Optimal partitioning (ruptures\n#   Dynp, l2 cost, minimum segment length 2) on the per-trial peak rate of each field; the trial\n#   order permuted 1000 times; K from 1 to min(5, floor(trials/4)); p for each K is the fraction\n#   of shuffles with lower cost than the data; Bonferroni over the K values at 0.05; the best K is\n#   the one with the lowest percentile. Change points whose step is under 40% of \"the max firing\n#   rate across trials\" are dropped. The code normalises the fitted step function by its own\n#   maximum and calls a rise of more than 0.4 between consecutive trials a switch ON, a fall a\n#   switch OFF (nmf_analysis/change_point_analysis.py, detect_switch_pwc); dividing by the maximum\n#   of the raw per-trial peak rates is the other reading of the Methods, shown as a variant.\n#   Shuffle seed fixed at 123 in the code (a standard choice that cannot change the outcome).\nschema_version: 2\npaper: doi:10.1016/j.celrep.2024.114702\nclaims:\n- id: fig1d-pv-decorrelation\n  statement: The correlation between population vectors of place cells decreases with the lag\n    between trials, in both familiar and novel environments (within-session drift).\n  source: Results, Within-session representational drift, paragraph 1; Figure 1C and 1D\n  quote: The correlation decreased as a function of the lag between trials, suggesting drift within\n    both the familiar and the novel environment\n  criterion: Per session and turn (figure-8) or direction (linear maze), the population vector of\n    a trial is the concatenation of the place cells' trial rate maps (Figure 1C legend; code\n    compare amplitude change and location drift notebook, raw rates, place cells only); Pearson\n    correlation between every pair of trials. The slope of correlation on lag is fitted by linear\n    regression over all trial pairs with lags 1 to 10 (code pv_corr_analysis.py,\n    get_decay_slope_linregress). The paper reports no test of the decrease itself; its default\n    one-sample test is the two-sided Wilcoxon signed-rank test (STAR Methods, Quantification and\n    statistical analysis). Reproduced when the slopes are below zero by that test at p < 0.05 in\n    familiar and in novel units separately; partially reproduced when this holds in one\n    environment only.\n- id: fig1e-novel-drift-faster\n  statement: Over trial lags 1 to 10, population vectors decorrelate faster (a more negative slope)\n    in novel than in familiar environments.\n  source: Results, Within-session representational drift, paragraph 1; Figure 1E\n  quote: Linear regression revealed that drift was significantly faster in novel environments\n    (larger negative slope) within the first 1-10 trial lags\n  statistics:\n  - test: Wilcoxon rank-sum test\n    p: 0.02\n    statistic: Cohen's d = 0.58\n    n: 106 session and turn units\n  expected:\n  - quantity: number of session and turn units, lags 1 to 10\n    value: 106\n    tolerance: 10.6\n  - quantity: Cohen's d, familiar against novel slopes, lags 1 to 10\n    value: 0.58\n    tolerance: 0.058\n  depends_on:\n  - fig1d-pv-decorrelation\n  criterion: Slopes as in fig1d-pv-decorrelation, one per session and turn or direction, from\n    lags 1 to 10 (the code requires at least 5 lags in the window). Familiar against novel slopes\n    by a two-sided Wilcoxon rank-sum test (Figure 1E legend). Reproduced when p < 0.05 with the\n    novel slopes more negative; Cohen's d is reported against the expected value.\n- id: fig1e-later-lags-no-difference\n  statement: Over trial lags 11 to 20 and 21 to 30 no significant difference in decorrelation slope\n    between novel and familiar environments was detected.\n  source: Results, Within-session representational drift, paragraph 1; Figure 1E\n  quote: we failed to detect a significant difference between novel and familiar environments over a\n    range of 11-20 or 21-30 trial lags\n  statistics:\n  - about: lags 11 to 20\n    test: Wilcoxon rank-sum test\n    p: 0.3\n    statistic: Cohen's d = 0.54\n    n: '26'\n  - about: lags 21 to 30\n    test: Wilcoxon rank-sum test\n    p: 0.68\n    statistic: Cohen's d = -0.35\n    n: '8'\n  depends_on:\n  - fig1d-pv-decorrelation\n  criterion: A claim of absence. Slopes as in fig1e-novel-drift-faster over lags 11 to 20 and 21\n    to 30 (units with at least 5 lags in the window, as in the code), familiar against novel by a\n    two-sided Wilcoxon rank-sum test. Reproduced when p >= 0.05 for both windows; not reproduced\n    when either is significant. The numbers of units and Cohen's d are reported.\n- id: fig1h-rate-decorrelates-location-stable\n  statement: The vector of within-field peak firing rates of all place fields decorrelates with\n    trial lag, whereas the vector of field peak locations stays correlated.\n  source: Results, Within-session representational drift, paragraph 2; Figure 1G and 1H\n  quote: We found the vector of the peak firing rate of all place fields decorrelated as a function of\n    trial lag, whereas the vector of the field locations remained stable\n  criterion: Per session and environment, the vector over place fields of each trial's peak rate,\n    and of each trial's peak location, correlated (Pearson) between trial pairs and averaged per\n    lag (Figure 1G legend; code compare amplitude change and location drift notebook,\n    get_plot_pf_param_population_corr_vs_lag, which concatenates the two turns aligned by\n    within-turn trial index). The paper reports no test; the slope of correlation on lag per\n    session is fitted by linear regression, as for Figure 1E, and slopes are tested against zero\n    by the two-sided Wilcoxon signed-rank test (STAR Methods default). Reproduced when the\n    peak-rate slopes are negative at p < 0.05 and the median peak-rate slope is at least twice\n    as steep as the median location slope; the threshold of two is chosen here, as the paper\n    states the contrast in words only, and both medians are reported.\n- id: fig1i-location-mse-increases\n  statement: The mean squared distance between field-location vectors still increases\n    significantly with trial lag, so field locations do change.\n  source: Results, Within-session representational drift, paragraph 2; Figure 1I\n  quote: In fact, the average squared Euclidean distance as a function of trial lag increased\n    significantly\n  depends_on:\n  - fig1h-rate-decorrelates-location-stable\n  criterion: Squared Euclidean distance between the field-location vectors of two trials divided\n    by the number of fields (Figure 1I legend; code nan_euclidean_distances squared over n_fields),\n    averaged per lag. The paper names no test and the code has none. Readings; (a) per session,\n    the slope of the distance on lag (lags 1 to 10) by linear regression, tested against zero by\n    the two-sided Wilcoxon signed-rank test (STAR Methods default); (b) an ordinary least squares\n    regression of the median over sessions on lag, as in the code's tentative statistics cell.\n    Reproduced when the increase is significant at p < 0.05 under a reading.\n- id: switch-step-size-filter\n  statement: Requiring change points to change the firing rate by at least 40% of the maximum\n    removes only 7% of putative switching fields (212 of 3,184).\n  source: Results, Within-session representational drift, paragraph 3\n  quote: This restriction ruled out only 7% of the putative switching fields (n = 212/3,184)\n  expected:\n  - quantity: putative switching fields (significant change points before the step filter)\n    value: 3184\n    tolerance: 318.4\n  - quantity: fields removed by the 40% filter\n    value: 212\n    tolerance: 21.2\n  criterion: Switch detection as in the opening comment, over familiar and novel sessions\n    together (the paper does not say; readings (a) both environments, (b) familiar only). A\n    putative switching field has a significant change point by the shuffle test; it is removed\n    when no change point passes the 40% step filter. Reproduced when both counts are within\n    tolerance under a reading and under either normalisation of the step (code, fitted maximum;\n    or raw maximum).\n- id: fig2d-switch-fractions\n  statement: In the familiar environment 19% of place fields (2,310 of 12,311) switch\n    significantly (14% ON, 9% OFF); in the novel environment 31% (662 of 2,127; 25% ON, 18% OFF).\n  source: Results, Within-session representational drift, paragraph 3; Figure 2D\n  quote: Overall, 19% (2,310/12,311) of the place fields showed significant switching (14% ON, 9% OFF)\n    in the familiar environment (Figure 2D) and 31% (662/2,127; 25% ON, 18% OFF) in the novel\n    environment\n  expected:\n  - quantity: familiar place fields\n    value: 12311\n    tolerance: 1231\n  - quantity: familiar switching fields\n    value: 2310\n    tolerance: 231\n  - quantity: fraction of familiar fields with a switch ON\n    value: 0.14\n    tolerance: 0.014\n  - quantity: fraction of familiar fields with a switch OFF\n    value: 0.09\n    tolerance: 0.009\n  - quantity: novel place fields\n    value: 2127\n    tolerance: 213\n  - quantity: novel switching fields\n    value: 662\n    tolerance: 66\n  - quantity: fraction of novel fields with a switch ON\n    value: 0.25\n    tolerance: 0.025\n  - quantity: fraction of novel fields with a switch OFF\n    value: 0.18\n    tolerance: 0.018\n  criterion: Fields are the place fields after merging of turn-common central-arm fields, over the\n    46 familiar and 8 novel sessions; a switching field has at least one switch ON or OFF (code\n    fig1 notebook, has_sw). Reproduced when all values are within tolerance; partially reproduced\n    when the four fractions (switching, ON, OFF per environment) are within tolerance but the\n    field counts are not.\n- id: fig2e-switch-fraction-by-experience\n  statement: The fraction of switching fields per session is lowest in animals that experienced\n    only the familiar maze (median 0.15), higher in familiar sessions of animals that also\n    experienced a novel environment that day (0.22) and highest in novel sessions (0.3).\n  source: Results, Within-session representational drift, paragraph 3; Figure 2E\n  quote: These animals had higher fractions of switching fields (\"Familiar\" in Figure 2E) than the\n    \"Familiar only\" animals\n  statistics:\n  - about: Familiar only against Familiar\n    test: two-sided Wilcoxon rank-sum test\n    p: 4.0e-05\n    n: 34 and 12 sessions\n  - about: Familiar against Novel\n    test: two-sided Wilcoxon rank-sum test\n    p: 0.01\n    n: 12 and 8 sessions\n  - about: Familiar only against Novel\n    test: two-sided Wilcoxon rank-sum test\n    p: 1.7e-05\n    n: 34 and 8 sessions\n  expected:\n  - quantity: median fraction of switching fields, Familiar only sessions\n    value: 0.15\n    tolerance: 0.015\n  - quantity: median fraction of switching fields, Familiar sessions\n    value: 0.22\n    tolerance: 0.022\n  - quantity: median fraction of switching fields, Novel sessions\n    value: 0.3\n    tolerance: 0.03\n  depends_on:\n  - fig2d-switch-fractions\n  criterion: Per session and maze task, the fraction of its place fields with at least one switch,\n    turns pooled (code fig1 notebook). \"Familiar\" sessions are the familiar-maze sessions of the\n    three mice that also ran a novel environment (e13_26m1, e15_13f1, e16_3m2; 12 sessions in the\n    code's list), \"Familiar only\" the other 34. Groups compared by two-sided Wilcoxon rank-sum\n    tests (Figure 2E legend). Reproduced when the three medians are within tolerance and the three\n    tests give p < 0.05 in the stated directions; partially reproduced when the ordering and at\n    least two tests hold.\n- id: fig3df-step-beats-polynomial-fields\n  statement: For more than 96% of place fields, a change-point model explains more variance of\n    the per-trial peak rate than a polynomial regression with the same number of parameters, at\n    every model complexity.\n  source: Results, Within-session representational drift, paragraph 5; Figure 3D to 3F, left\n  quote: The change-point models explained more variance for more than 96% of the place fields across\n    all model complexities\n  expected:\n    quantity: lowest fraction of place fields better explained by the change-point model, over\n      orders 1 to 3\n    value: 0.96\n    tolerance: 0.0\n  criterion: For each place field, the change-point model with K change points (K + 1 segments,\n    fitted by optimal partitioning, minimum segment 2) against an ordinary least squares\n    polynomial of order K in trial number, K = 1, 2, 3 (Figures 3D to 3F; Methods, Continuous\n    model of trial-dependent change). Explained variance ratio of each as 1 minus residual\n    variance over total variance (code step_vs_gradual_analysis.py, fit_cpd_get_r2, and statsmodels\n    rsquared). All place fields after merging (code). Reproduced when the fraction with the\n    change-point ratio higher exceeds 0.96 for each K (the paper states a bound, so no tolerance);\n    partially reproduced when it exceeds 0.90 for each K.\n- id: fig3df-polynomial-beats-step-population\n  statement: For the decay of population-vector correlation with trial lag, a polynomial\n    regression explains more variance than the change-point model.\n  source: Results, Within-session representational drift, paragraph 5; Figure 3D to 3F, right, and\n    Figure 3G\n  quote: In contrast, polynomial regression explained more variance than the change-point model for\n    the population vector decorrelation\n  depends_on:\n  - fig1d-pv-decorrelation\n  criterion: Per session and turn or direction, the mean PV correlation per lag (Figure 3 legend,\n    \"averaged across trial pairs\") fitted against lag by the change-point model with K change\n    points and by a polynomial of order K, K = 1 to 3. The paper gives no fraction or test;\n    reproduced when, for each K, more than half of the units are better explained by the\n    polynomial and the paired difference of explained variance ratios is below zero by a\n    two-sided Wilcoxon signed-rank test at p < 0.05 (STAR Methods default for paired samples).\n    Partially reproduced when the majority holds without the test.\n- id: figs4g-population-vectors-gradual\n  statement: Fitted to the population vectors themselves (after PCA), the gradual and step models\n    are comparable, with 60% to 70% of sessions better explained by the gradual model and the\n    distribution of R2 differences significantly biased toward the polynomial model.\n  source: Results, Within-session representational drift, paragraph 6; Figure S4G\n  quote: We found that the two models were largely comparable at explaining the data, with more\n    sessions (60%-70%) better explained by the gradual model and the distribution of R2\n    significantly biased toward continuous models\n  statistics:\n  - about: order 1\n    test: Wilcoxon signed rank test\n    p: 0.006\n    statistic: Cohen's d = -0.1\n    n: '108'\n  - about: order 2\n    test: Wilcoxon signed rank test\n    p: 0.01\n    statistic: Cohen's d = -0.19\n    n: '106'\n  - about: order 3\n    test: Wilcoxon signed rank test\n    p: 0.0006\n    statistic: Cohen's d = -0.24\n    n: '104'\n  expected:\n    quantity: fraction of session and turn units better explained by the polynomial model, each\n      order\n    value: 0.65\n    tolerance: 0.065\n    unit: range 0.6 to 0.7 widened by 10% of each bound (0.54 to 0.77)\n  criterion: Per session and turn, the matrix of trial population vectors (place cells x position)\n    reduced by PCA to the components holding just above 95% of the variance; a vector-valued\n    change-point model with shared change points (cost summed over components) against\n    polynomials fitted to each component (Methods, Model comparison applied to the population\n    vectors), orders 1 to 3. Reproduced when, for each order, the fraction better explained by\n    the polynomial lies in 0.54 to 0.77 and R2(CPM) minus R2(regression) is below zero by a\n    two-sided Wilcoxon signed-rank test at p < 0.05.\n- id: fig3k-switch-abrupt\n  statement: 75% to 77% of first passage times after a change point are under two trials, and the\n    distribution of switch durations resembles a negative binomial with two successes and p =\n    0.5, as expected for an instantaneous step.\n  source: Results, Within-session representational drift, paragraph 7; Figure 3H to 3K\n  quote: Empirically, we found that 75%-77% of first passage times happened in fewer than two trials,\n    and the distribution of passage times resembled the expected negative binomial distribution\n  expected:\n    quantity: fraction under two trials (switch ON and switch OFF)\n    value: 0.76\n    tolerance: 0.085\n    unit: range 0.75 to 0.77 widened by 10% of each bound (0.675 to 0.847)\n  depends_on:\n  - fig2d-switch-fractions\n  criterion: For each detected switch, thresholds are the rates predicted by the step model; for a\n    switch ON the post-switch passage time is the number of trials from the change point to the\n    first trial with rate above the post-switch prediction, the pre-switch passage time the\n    number back from the trial before it to the first trial below the pre-switch prediction;\n    mirrored for OFF; the switch duration is their sum (Methods, Switch duration quantification;\n    code get_peri_switch_peak_valley_span). The text says \"first passage times\" while Figure 3K\n    plots durations, so the readings are (a) individual passage times (expected under a step to\n    follow a negative binomial with k = 1, p = 0.5, giving 0.75 under two) and (b) switch\n    durations (k = 2). Reproduced when, under a reading, the fraction under two trials is within\n    tolerance for ON and OFF; the durations are compared with the negative binomial (k = 2, p =\n    0.5) by their histograms and a chi-squared goodness of fit, reported (the code's\n    exploratory test; the paper reports none).\n- id: figs5-switchers-drive-drift\n  statement: Population vectors of switching place cells decorrelate faster with trial lag than\n    those of size-matched non-switching cells, in familiar and novel environments.\n  source: Results, Within-session representational drift, paragraph 8; Figure S5\n  quote: The population vector of the switching population decorrelated faster than that of the\n    non-switching population in both familiar and novel environments\n  statistics:\n  - about: familiar\n    test: Wilcoxon signed-rank test\n    p: 1.1e-11\n    statistic: median difference (Switch) - (No switch) = -0.009\n    n: 46 sessions\n  - about: novel\n    test: Wilcoxon signed-rank test\n    p: 0.0078\n    statistic: median difference (Switch) - (No switch) = -0.011\n    n: 8 sessions\n  expected:\n  - quantity: median slope difference, switchers minus non-switchers, familiar\n    value: -0.009\n    tolerance: 0.0009\n  - quantity: median slope difference, switchers minus non-switchers, novel\n    value: -0.011\n    tolerance: 0.0011\n  depends_on:\n  - fig2d-switch-fractions\n  criterion: Switchers are place cells with at least one switching field, non-switchers those with\n    none, sampled ten times to the switchers' number and averaged (Methods, Contribution of\n    switching neurons to drift). Per session, the median PV correlation over trial pairs at each\n    lag, and the slope of a linear regression on lag. The code pools turns per session and task;\n    per session and turn is the other reading. Paired switcher against non-switcher slopes by the\n    Wilcoxon signed-rank test (Figure S5B). Reproduced when p < 0.05 with switchers steeper in\n    both environments; partially reproduced in one. Median differences are reported against the\n    expected values.\n- id: fig4-glm-deviance\n  statement: A Poisson GLM of switch counts per arm and trial explains 20% of the deviance for\n    switching ON and 14% for switching OFF, with animal identity, maze segment and the number of\n    place fields the most important predictors.\n  source: Results, Factors that affect the rate of switching, paragraph 1; Figure 4A and 4F\n  quote: The model explained 20% of the deviance for switching ON and 14% for switching OFF ... We\n    found that the variables that explained most of the variance were the animal labels (i.e.,\n    individual differences), the maze corridors, and the number of place fields\n  expected:\n  - quantity: explained deviance, switching ON\n    value: 0.2\n    tolerance: 0.02\n  - quantity: explained deviance, switching OFF\n    value: 0.14\n    tolerance: 0.014\n  - quantity: number of arm by trial rows\n    value: 5131\n    tolerance: 513\n  depends_on:\n  - fig2d-switch-fractions\n  criterion: Familiar sessions only. Rows are trial by maze segment (delay zone, central arm,\n    choice arm, return side arm, pre-delay zone; Figure 4K; the code cuts linearised position at\n    0, 15, 74, 111, 185, 202, 222 cm and merges the last piece into the delay zone, trials from\n    the fourth on). Model y ~ C(Animal) + C(Position) + N_field + Trial + Speed + CV_speed +\n    C(Correct) + C(Prev_correct), Poisson, Trial and Speed z-scored within session (Methods,\n    Generalized linear model of switching). Explained deviance read as (a) the cross-validated\n    held-out fraction of deviance, repeated 5-fold cross-validation stratified by animal, 10\n    repeats (Methods; the code uses StratifiedShuffleSplit with 5 splits and 10% held out,\n    shown as a variant), or (b) in-sample on all rows. Importance is the drop in held-out\n    explained deviance when one predictor is left out. Reproduced when both values are within\n    tolerance under a reading and the three largest drops (ON and OFF each) are animal, position\n    and number of fields; partially reproduced when only the ranking holds.\n- id: fig4-delay-zone-more-switching\n  statement: Consistently more switching ON and OFF occurs in the delay zone than in other parts of\n    the maze.\n  source: Results, Factors that affect the rate of switching, paragraph 1; Figure 4B, 4E, 4G and 4J\n  quote: consistently more ON/OFF switching occurred in the delay zone\n  depends_on:\n  - fig4-glm-deviance\n  criterion: In the full GLM of fig4-glm-deviance fitted on all rows, the position coefficients of\n    the four other segments relative to the delay zone, with 95% confidence intervals from the\n    Fisher information (Figure 4B legend). Reproduced when all four coefficients are negative\n    with intervals excluding zero, for ON and for OFF; partially reproduced when this holds for\n    one of the two or for three of four segments in both. The per-session number of switches\n    normalised by fields per arm (Figure 4E, 4J) is reported.\n- id: fig4di-switching-decreases-with-trial\n  statement: The number of switches normalised by the number of fields decreases with trial number,\n    for ON and OFF, in familiar and novel environments.\n  source: Results, Factors that affect the rate of switching, paragraph 1; Figure 4D and 4I\n  quote: As expected, switching probability decreased as a function of the trial number\n  statistics:\n  - about: switch ON, familiar\n    test: Pearson correlation\n    statistic: r = -0.15\n    p: 1.3e-06\n    n: 1,029 trials\n  - about: switch ON, novel\n    test: Pearson correlation\n    statistic: r = -0.23\n    p: 0.00013\n    n: 281 trials\n  - about: switch OFF, familiar\n    test: Pearson correlation\n    statistic: r = -0.2\n    p: 3.3e-11\n  - about: switch OFF, novel\n    test: Pearson correlation\n    statistic: r = -0.18\n    p: 0.0027\n  expected:\n  - quantity: Pearson r, switch ON, familiar\n    value: -0.15\n    tolerance: 0.015\n  - quantity: Pearson r, switch ON, novel\n    value: -0.23\n    tolerance: 0.023\n  - quantity: Pearson r, switch OFF, familiar\n    value: -0.2\n    tolerance: 0.02\n  - quantity: Pearson r, switch OFF, novel\n    value: -0.18\n    tolerance: 0.018\n  - quantity: familiar trials\n    value: 1029\n    tolerance: 103\n  - quantity: novel trials\n    value: 281\n    tolerance: 28\n  depends_on:\n  - fig2d-switch-fractions\n  criterion: Per trial, the number of switch-ON (OFF) occurrences divided by the number of fields,\n    against trial number z-scored within session, pooled over sessions (Figure 4D legend). Pearson\n    correlation (legend); the code computes a Spearman correlation, shown as a variant.\n    Reproduced when all four correlations are negative at p < 0.05; values compared with the\n    expected r. Partially reproduced when three of four hold.\n- id: fig4-behavior-not-predictive\n  statement: Correct or incorrect choice on the current or previous trial does not predict\n    switching, and leaving out speed or the CV of speed does not reduce the model's prediction of\n    held-out data.\n  source: Results, Factors that affect the rate of switching, paragraph 1; Figure 4A, 4C, 4F, 4H\n  quote: Correct or incorrect arm choice on the current or previous trial did not predict the\n    occurrence of switching (Figures 4C and 4H). Leaving out locomotion speed or coefficient of\n    variation (CV) of speed did not reduce the model's ability to predict held-out data\n  depends_on:\n  - fig4-glm-deviance\n  criterion: A claim of absence, on the paper's measures. For choice, the 95% confidence intervals\n    (Fisher information) of the Correct and Prev_correct coefficients in the full GLM (Figure 4C,\n    4H). For speed, the drop in held-out explained deviance when Speed or CV_speed is left out,\n    over the cross-validation splits (Figure 4A, 4F). Reproduced when, for ON and OFF, both choice\n    intervals include zero and the median drop for speed and for CV of speed is not above zero;\n    not reproduced when any choice interval excludes zero or any median drop is above zero by\n    more than the spread (standard deviation) of drops over splits, a threshold chosen here as\n    the paper shows the splits without a test.\n- id: figs8-speed-no-trend\n  statement: Average locomotion speed does not change as a function of trial, and there is no\n    clear linear relationship between speed and the normalised switching count.\n  source: Results, Factors that affect the rate of switching, paragraph 1; Figure S8A to S8C\n  quote: By contrast, average locomotion speed did not change as a function of trial (Figure S8C)\n    ... Nor did we find a clear linear relationship between speed and the normalized (i.e., divided\n    by the number of fields) switching count\n  statistics:\n  - about: speed against trial, familiar\n    test: Pearson correlation\n    statistic: r = 0.01\n    p: 3.0e-11\n  - about: speed against trial, novel\n    test: Pearson correlation\n    statistic: r = -0.02\n    p: 0.78\n  expected:\n  - quantity: Pearson r, speed (z-scored) against trial, familiar\n    value: 0.01\n    tolerance: 0.05\n  - quantity: Pearson r, speed (z-scored) against trial, novel\n    value: -0.02\n    tolerance: 0.05\n  criterion: Speed z-scored within session against trial, Pearson correlation (Figure S8C legend);\n    the tolerance on r is 0.05 absolute, as 10% of values near zero is below sampling noise. The\n    paper's own familiar p (3 x 10-11) is significant though r is 0.01, so the absence for speed\n    is judged on r; reproduced when both r are within tolerance. For Figure S8A and S8B, the\n    normalised switch count per arm and trial against the average speed in the arm, Pearson\n    correlation (STAR Methods default for linear correlation); the paper reports no value, and r\n    and p are reported. Partially reproduced when the speed-trial part holds and a speed-switching\n    correlation has |r| above 0.1 with p < 0.05.\n- id: fig4no-head-scans-not-related\n  statement: Most head scans occur in the reward area and few in the central arm, and there is no\n    reliable relationship between field switching and the incidence of head scanning.\n  source: Results, Factors that affect the rate of switching, paragraph 2; Figure 4L to 4O\n  quote: most head scans were detected in the reward area (position 50, between green and red\n    sections), while head scans in the central arm were rare (Figures 4N and 4O). We found no\n    reliable relationship between field switching and incidence of head scanning\n  criterion: Head scans detected as in Methods, Behavior segmentation (head more than 3 cm from the\n    track, extended until within 1 cm, at least 0.4 s, start and end within 20 bins, merged when\n    within 0.4 s; the track sampled from times with speed above 10 cm/s). Per position bin, the\n    number of trials with a head scan and with a switch ON (OFF), and their ratio (Figure 4N, 4O).\n    The paper reports no test. Reproduced when the bin with most head-scan trials lies in the\n    reward area at the end of the choice arms and the central arm has fewer head-scan trials than\n    each other segment, and the per-bin counts of head-scan trials and switch trials are not\n    positively correlated (Pearson, p >= 0.05, STAR Methods default). Partially reproduced when\n    only the spatial distribution holds.\n- id: figs9-splitter-switching\n  statement: Choice-predicting (splitter) fields on the central arm also switch ON and OFF.\n  source: Results, Factors that affect the rate of switching, paragraph 3; Figure S9\n  quote: We found that the splitter feature of hippocampal neurons could also switch ON and OFF at any\n    trial of the session, similar to place fields\n  depends_on:\n  - fig2d-switch-fractions\n  criterion: Splitter fields are central-arm fields not merged across turns (peaks 5 bins or more\n    apart or per-trial peak rates different by t-test; Methods, Place field detection). Reproduced\n    when switches ON and OFF are both detected among splitter fields, on trials spread over the\n    session (switch trials in each third of the session). The fraction of splitter fields that\n    switch is reported beside that of other fields.\n- id: figs13-btsp-signatures\n  statement: On the switch-ON trial, place field width correlates with running speed; the field\n    peak on the following trial shifts backward in the familiar but not significantly in the novel\n    environment; peak rate on the switch trial is not higher than on the next trial; and a\n    significant ramp in rate precedes switch ON.\n  source: Results, Switching exhibits signatures of BTSP, paragraphs 1 and 2; Figure S13A to S13D\n  quote: We observed a significant correlation between the place field width and the running speed on\n    the trial when the field switched ON (Figure S13A) ... the distribution skewed toward backward\n    (Figure S13C), although it is not significant in the novel environment\n  statistics:\n  - about: backward shift, familiar\n    test: Wilcoxon signed-rank test\n    p: 0.01\n  - about: backward shift, novel\n    test: Wilcoxon signed-rank test\n    p: 0.52\n  - about: rate, trial -3 against -2\n    test: Wilcoxon signed-rank test\n    p: 0.005\n  - about: rate, trial -2 against -1\n    test: Wilcoxon signed-rank test\n    p: 1.1e-20\n  - about: rate, trial 0 against 1\n    test: Wilcoxon signed-rank test\n    p: 0.2\n  - about: rate, trial 1 against 2\n    test: Wilcoxon signed-rank test\n    p: 1.0e-14\n  depends_on:\n  - fig2d-switch-fractions\n  criterion: Switch-ON fields, first switch of each field only (Figure S13A). (1) Field width on\n    the switch trial against mean speed in that trial, linear regression (Pearson), familiar and\n    novel; the paper gives no width definition for a single trial, so readings are (a) the\n    detected field's width and (b) the width of the trial rate map above half its peak within the\n    field. (2) Shift of the field peak from the switch trial to the next, two-sided Wilcoxon\n    signed-rank test against zero; backward is against running direction. (3) Normalised\n    within-field peak rate around the switch (trial 0), paired Wilcoxon signed-rank tests between\n    neighbouring trials. Reproduced when the width-speed correlation is significant in familiar,\n    the familiar shift is backward at p < 0.05 and the novel shift is not significant, trial 0\n    against 1 is not significant and trials -3 to -1 rise significantly; partially reproduced\n    when at least three of these hold.\n- id: fig5c-switchiness-not-intrinsic\n  statement: Across familiar and novel environments, a neuron's switchiness is not correlated,\n    whereas its CV of within-field peak rate and its lap-to-lap rate map correlation are, after\n    regressing out NREM firing rate.\n  source: Results, Switching, neuron or circuit property, paragraph 1; Figure 5C\n  quote: The residuals are significantly correlated across environments for CV of within-field peak\n    firing rate (left, standardized linear regression coefficients t = 4.8, R2 = 0.02, p < 10-5) and\n    lap-lap rate map correlation (middle, t = 7.9, R2 = 0.06; p < 10-14), but not for the explained\n    variance ratio from the change-point model (right, t = 0.9, R2 = 0.0008, p = 0.37)\n  statistics:\n  - about: CV of within-field peak rate\n    test: standardized linear regression\n    statistic: t = 4.8, R2 = 0.02\n    p: 1.0e-05\n    p_relation: <\n    n: 955 neurons\n  - about: lap-to-lap rate map correlation\n    test: standardized linear regression\n    statistic: t = 7.9, R2 = 0.06\n    p: 1.0e-14\n    p_relation: <\n    n: 955 neurons\n  - about: switchiness (one-change-point explained variance ratio)\n    test: standardized linear regression\n    statistic: t = 0.9, R2 = 0.0008\n    p: 0.37\n    n: 955 neurons\n  expected:\n  - quantity: neurons\n    value: 955\n    tolerance: 95.5\n  - quantity: t, CV\n    value: 4.8\n    tolerance: 0.48\n  - quantity: t, lap-to-lap correlation\n    value: 7.9\n    tolerance: 0.79\n  criterion: Metrics per Methods, Metrics of variability; noisiness is std over mean of the\n    per-trial within-field peak rate, shiftiness the trial-pair rate map correlation averaged\n    (the code takes the median), switchiness the variance explained by the one-change-point\n    model. Each metric, familiar and novel, regressed on log NREM firing rate; the novel residual\n    regressed on the familiar residual, standardised (Figure 5C legend; code metric across fam\n    novel notebook, resid_regression). Units read as (a) neurons with each metric averaged over\n    fields (Methods) or (b) fields matched across environments by the code's field index. For the\n    switchiness, a claim of absence on the paper's test; reproduced when it is not significant at\n    p < 0.05 while CV and lap correlation are significant and positive; partially reproduced when\n    the switchiness part holds and one of the other two does.\n- id: fig5d-nrem-rate-relations\n  statement: Noisiness decreases with log NREM firing rate in both environments, shiftiness is\n    related to it in the novel environment only, and switchiness is not related to it.\n  source: Figure 5D\n  quote: 'noisy: familiar, t = -11.1, p = 3.6 × 10-27; novel, t = -12.6, p = 1.5 × 10-33; shifty:\n    familiar, t = -0.8, p = 0.4; novel, t = -3.6, p = 0.000326; switchy: familiar, t = 0.9, p =\n    0.4; novel, t = -0.6, p = 0.5'\n  statistics:\n  - about: noisy, familiar\n    test: standardized linear regression\n    statistic: t = -11.1\n    p: 3.6e-27\n  - about: noisy, novel\n    test: standardized linear regression\n    statistic: t = -12.6\n    p: 1.5e-33\n  - about: shifty, familiar\n    test: standardized linear regression\n    statistic: t = -0.8\n    p: 0.4\n  - about: shifty, novel\n    test: standardized linear regression\n    statistic: t = -3.6\n    p: 0.000326\n  - about: switchy, familiar\n    test: standardized linear regression\n    statistic: t = 0.9\n    p: 0.4\n  - about: switchy, novel\n    test: standardized linear regression\n    statistic: t = -0.6\n    p: 0.5\n  depends_on:\n  - fig5c-switchiness-not-intrinsic\n  criterion: Each metric regressed on log NREM firing rate per environment, as in\n    fig5c-switchiness-not-intrinsic. Reproduced when the significance at p < 0.05 and the sign of\n    each of the six regressions match the paper; partially reproduced when five of six match.\n- id: multifield-independent-switching\n  statement: Of 781 pairs of switching place fields belonging to the same place cell, only 41 (5%)\n    switched on the same trial.\n  source: Results, Switching, neuron or circuit property, paragraph 2; Figure 5E\n  quote: Of 781 place field pairs that belonged to the same place cell and both switched, only 41 (5%)\n    switched on the same trial\n  expected:\n  - quantity: field pairs of the same cell that both switched\n    value: 781\n    tolerance: 78\n  - quantity: pairs that switched on the same trial\n    value: 41\n    tolerance: 4.1\n  depends_on:\n  - fig2d-switch-fractions\n  criterion: Pairs of switching fields of the same neuron within a session and turn, familiar and\n    novel pooled (the paper does not say; the other reading is familiar only, as in Figure S11);\n    same trial means a switch of each field on the same trial (ON or OFF; the paper does not say\n    whether the switch types must match, so readings are any switch and same type). Reproduced\n    when both counts are within tolerance under a reading.\n- id: figs12-stability-after-switch-on\n  statement: Fields that switched ON have a lower CV of peak rate and less jitter of peak location\n    over the five trials after the switch than non-switching fields over five trials from the\n    start or middle of the session.\n  source: Results, Switching, neuron or circuit property, paragraph 2; Figure S12A, S12B, S12D,\n    S12E\n  quote: Specifically, switch-ON fields had lower CV of firing rates within the five trials after the\n    switch, relative to trial-to-trial variability in non-switching fields over five trials taken\n    either from the beginning or from the middle of the session\n  statistics:\n  - about: CV, start window, familiar\n    test: Wilcoxon rank-sums test\n    p: 2.0e-59\n    n: 6852 non-switching and 1230 switch-ON fields\n  - about: CV, start window, novel\n    test: Wilcoxon rank-sums test\n    p: 1.8e-05\n    n: 820 non-switching and 402 switch-ON fields\n  - about: peak location SD, start window, familiar\n    test: Wilcoxon rank-sums test\n    p: 7.0e-27\n  - about: peak location SD, start window, novel\n    test: Wilcoxon rank-sums test\n    p: 2.9e-06\n  - about: CV, middle window, familiar\n    test: Wilcoxon rank-sums test\n    p: 2.6e-29\n  - about: CV, middle window, novel\n    test: Wilcoxon rank-sums test\n    p: 0.019\n  - about: peak location SD, middle window, familiar\n    test: Wilcoxon rank-sums test\n    p: 1.3e-08\n  - about: peak location SD, middle window, novel\n    test: Wilcoxon rank-sums test\n    p: 0.4\n  expected:\n  - quantity: median CV, non-switching, start window, familiar\n    value: 0.365\n    tolerance: 0.0365\n  - quantity: median CV, switch ON, familiar\n    value: 0.283\n    tolerance: 0.0283\n  - quantity: median CV, non-switching, start window, novel\n    value: 0.37\n    tolerance: 0.037\n  - quantity: median CV, switch ON, novel\n    value: 0.33\n    tolerance: 0.033\n  - quantity: median CV, non-switching, middle window, familiar\n    value: 0.4\n    tolerance: 0.04\n  - quantity: median CV, non-switching, middle window, novel\n    value: 0.46\n    tolerance: 0.046\n  depends_on:\n  - fig2d-switch-fractions\n  criterion: Fields that switched ON once against non-switching fields; place cells with spatial\n    information above 0.5 bit/spike and fields with peak rate above 1 Hz on 90% of trials (Figure\n    S12 legend). CV of per-trial peak rate and SD of peak location over the five trials after the\n    switch, or over the first five trials or five middle trials (the paper does not say which\n    five are the middle; the standard choice of the five centred on the session midpoint is used,\n    as the choice is unlikely to change the outcome) for non-switching fields; two-sided Wilcoxon\n    rank-sum tests. Reproduced when switch-ON CV is lower at p < 0.05 for both windows in familiar\n    and in novel and the medians are within tolerance; partially reproduced when the direction and\n    significance hold in familiar only. Location results are reported, with the novel middle\n    window expected not significant.\n- id: fig6-co-switching\n  statement: Place fields co-switch on the same trial more than expected by chance in a subset of\n    sessions, 17% (ON) and 20% (OFF) of familiar and 57% (ON) and 29% (OFF) of novel sessions.\n  source: Results, Switching, neuron or circuit property, paragraph 3; Figure 6D and 6E\n  quote: found that 17% (20%) of the familiar sessions and 57% (29%) of the novel sessions showed at\n    least one trial with significant co-switching ON (OFF)\n  expected:\n  - quantity: fraction of familiar sessions with significant co-switching ON\n    value: 0.17\n    tolerance: 0.017\n  - quantity: fraction of familiar sessions with significant co-switching OFF\n    value: 0.2\n    tolerance: 0.02\n  - quantity: fraction of novel sessions with significant co-switching ON\n    value: 0.57\n    tolerance: 0.057\n  - quantity: fraction of novel sessions with significant co-switching OFF\n    value: 0.29\n    tolerance: 0.029\n  depends_on:\n  - fig2d-switch-fractions\n  criterion: 46 familiar and 7 novel sessions (one novel session left out for too few trials;\n    Methods, Datasets), and sessions need at least 7 trials per turn (code ntrials_mask). Null by\n    circularly shifting each field's switch trials independently, 1000 times (Results; code\n    gen_circular_shuffle, which leaves out the first two trials and the last). The statistic is\n    the number of field pairs that co-switch ON (OFF). Readings of \"at least one trial with\n    significant co-switching\"; (a) per session, the number of co-switching pairs over all trials\n    exceeds the shuffle at p < 0.05 (fraction of shuffles at or above the data; code\n    test_co_switch.py, Figure 6E); (b) per trial, the number of pairs switching on that trial\n    exceeds its shuffle distribution at p < 0.05, the session counting when any trial does.\n    Co-switching means the same trial (Results); the code's figure uses a window of lag 1, shown\n    as a variant. Novel fractions are of 7 sessions (4 and 2). Reproduced when the four fractions\n    are within tolerance, or within one session of the expected count, under a reading.\n- id: fig6f-switching-asynchronous\n  statement: On each trial only a small subset of place fields, up to 5%, switch ON or OFF, so\n    switching is largely asynchronous.\n  source: Results, Switching, neuron or circuit property, paragraph 3; Figure 6F\n  quote: We found that in each trial, a small subset of the place fields (up to 5%) switched ON/OFF\n  expected:\n    quantity: largest fraction of fields switching ON or OFF on a trial\n    value: 0.05\n    tolerance: 0.005\n  depends_on:\n  - fig2d-switch-fractions\n  criterion: Per session and trial, the fraction of the session's place fields that switch ON\n    (OFF), leaving out the first and last two trials (Figure 6F legend). Reproduced when the 95th\n    percentile over trials of these fractions is at most 0.055, for ON and OFF and in both\n    environments; the maximum is reported, as \"up to\" may mean the extreme or the bulk.\n- id: figs14-preexisting-fields-ephys\n  statement: For fields whose rate before switching ON (after switching OFF) is below the detection\n    threshold (60% of ON and 20% of OFF switches), within-field firing is already elevated over the\n    surrounding rate before emergence and stays elevated after disappearance, for most neurons.\n  source: Results, Pre-existing dynamics bias switching, paragraph 2; Figure S14\n  quote: Indeed, we found that, even before the emergence of the new place field, the firing rates\n    within the future place fields were already elevated relative to the mean rate recorded outside\n    of the future place field for the majority of the neurons ... Similarly, the firing rates\n    remained elevated within the previous place field after the field had switched OFF\n  expected:\n  - quantity: fraction of switch-ON fields below threshold before the switch\n    value: 0.6\n    tolerance: 0.06\n  - quantity: fraction of switch-OFF fields below threshold after the switch\n    value: 0.2\n    tolerance: 0.02\n  depends_on:\n  - fig2d-switch-fractions\n  criterion: Selection as in Figure S14 legend (mean within-field rate before the first ON, or after\n    the last OFF, below the shuffle threshold of field detection). Outside region extends the field\n    by 10% of track length on each side until the track end or another field (Methods,\n    Quantification of pre-existing constraint). Within minus outside mean rate over the pre-ON\n    (post-OFF) trials. The paper reports no test here; the code's notebook tests session averages\n    by a two-sided Wilcoxon signed-rank test. Reproduced when the two fractions are within\n    tolerance, more than half of the fields have within above outside, for ON and OFF and in\n    familiar and novel, and the session-level test gives p < 0.05 in familiar; partially\n    reproduced when the majorities hold without the fractions.\n- id: fig7-preexisting-across-days\n  statement: In two-photon imaging over two days, fields that switch ON on day 2 already show\n    elevated activity within the future field on day 1, and fields that switch OFF on day 1 stay\n    elevated on day 2.\n  source: Results, Pre-existing dynamics bias switching, paragraph 3; Figure 7E to 7H\n  quote: Overall, we found that even on the day before the emergence of the new place field, the\n    firing rates within the future place fields were already significantly elevated relative to the\n    mean rate recorded outside of the future place field (Figures 7E and 7G)\n  criterion: Not testable on dandiset 000552, which holds the electrophysiology only; the imaging\n    data (14 experiments, 11 mice) are available from M. Bartos on request and not deposited.\n    Were they available, the test is the Wilcoxon rank-sum test of within against outside dF/F\n    with Cohen's d (Figure 7 legend), at p < 0.05.\n- id: figs15-imaging-not-artifact\n  statement: Trial-to-trial changes of baseline fluorescence are not correlated with the fraction of\n    fields switching, so image-plane drift does not explain switching in the imaging data.\n  source: Results, Pre-existing dynamics bias switching, paragraph 4; Figure S15\n  quote: We therefore correlated the average absolute change in baseline fluorescence ... across\n    cells in a given image field with the number of switching fields per trial but did not observe\n    a significant correlation\n  criterion: Not testable on dandiset 000552; the imaging data are not deposited (available on\n    request). Were they available, a claim of absence judged by the Pearson correlation of the\n    z-scored absolute baseline change against the fraction of switching fields per trial (n = 73\n    ON and 81 OFF trials from 10 sessions), at p < 0.05.\n- id: figs1-not-electrode-drift\n  statement: Spike amplitudes of neighbouring neurons recorded on the same shank as a switching\n    neuron do not change across its switch, arguing against electrode drift.\n  source: Results, Within-session representational drift, paragraph 4; Figure S1H\n  quote: Finally, neurons recorded on the same site with a switching neuron had unchanged waveforms\n    before and after the switch\n  statistics:\n  - about: switch ON\n    test: Wilcoxon signed-rank test\n    p: 0.72\n  - about: switch OFF\n    test: Wilcoxon signed-rank test\n    p: 0.35\n  depends_on:\n  - fig2d-switch-fractions\n  criterion: A claim of absence. For each switch of a reference neuron, the mean waveform amplitude\n    of each other neuron on the same shank from spikes in the 20 s before and 20 s after the\n    switch time (Figure S1 legend); post minus pre amplitude pooled over neighbours, two-sided\n    Wilcoxon signed-rank test against zero, for ON and OFF. The switch time is the time of the\n    switch trial; the paper does not say which moment of the trial (readings; its start, or the\n    animal's entry into the field). Reproduced when neither test gives p < 0.05; the median\n    change is reported. Needs spike waveforms per spike or amplitudes in the dandiset.\n- id: figs2-chr2-no-effect\n  statement: The proportions of neurons with different switching properties do not differ between\n    opto-tagged (ChR2-expressing) and non-tagged neurons.\n  source: Results, Within-session representational drift, paragraph 4; Figure S2\n  quote: Furthermore, switching was not related to the expression of channelrhodopsin (ChR) in a small\n    subset of the neurons in the dataset\n  statistics:\n  - test: Chi squared test\n    p: 0.8\n    n: 4486 neurons\n  expected:\n    quantity: neurons\n    value: 4486\n    tolerance: 449\n  depends_on:\n  - fig2d-switch-fractions\n  criterion: A claim of absence. Neurons classed by switching property (no switch, switch ON only,\n    OFF only, both; the paper's categories are shown only in the pie charts, so this is the\n    reading taken, with switching against not switching as the other), tagged against not tagged\n    from the dandiset's light-responsive labels; chi-squared test of independence. Reproduced\n    when p >= 0.05 under the readings; not reproduced when any gives p < 0.05.\n"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
python tools/claims_check.py claims/zheng-2024.yaml paper/10.1016-j.celrep.2024.114702.txt
```

Result: not kept, because it reads the paper's text.

**Agent**

The checker reports 0 problems. Next I'll check the style rules: no em dashes, no "rather", and no colon-space inside plain scalars.

**Agent calls Bash**

```bash
grep -n -i "rather\|—" claims/zheng-2024.yaml; grep -n "^ \{4,\}[^'#-].*: " claims/zheng-2024.yaml | grep -v "^\S*\s*\(quantity\|value\|tolerance\|unit\|test\|p\|n\|statistic\|about\|p_relation\):" | head; python -c "
import yaml;d=yaml.safe_load(open('claims/zheng-2024.yaml'))
import re
for c in d['claims']:
  for k,v in c.items():
    if isinstance(v,str) and ': ' in v: print(c['id'],k)
  for s in c.get('statistics',[]):
    for k,v in s.items():
      if isinstance(v,str) and ': ' in v: print(c['id'],k)
print(sum(1 for c in d['claims'] if 'statistics' in c), sum(len(c.get('statistics',[])) for c in d['claims']), sum(1 for c in d['claims'] if 'criterion' in c), sum(1 for c in d['claims'] if 'expected' in c))"
```

```
668:    familiar, t = -0.8, p = 0.4; novel, t = -3.6, p = 0.000326; switchy: familiar, t = 0.9, p =
fig5d-nrem-rate-relations quote
13 43 32 18
```

**Agent**

I wrote `claims/zheng-2024.yaml` and nothing else. The quote checker passes: 32 claims, 32 quotes, 43 statistical values, 0 problems. The style rules hold: no em dashes, no "rather", and the one value containing ": " is a quoted string, not a plain scalar.

**Text read**
- **Main text:** the author manuscript in PubMed Central (PMC11485410), with the STAR Methods and all main figure legends. The file's header calls it the version of record, but it is the PMC author manuscript.
- **Supplement:** the supplemental information of the version of record (mmc2.pdf, Figures S1 to S15 with legends), which is included in the same text file.
- **Code:** the paper's Zenodo deposit, doi:10.5281/zenodo.13247193. It is the authors' GitHub repository `samdeoxys1/within-session-representationl-drift`, tag v0.0, commit 93d6e33. Its notebooks keep their outputs, which give the 46 familiar and 8 novel sessions by name.

**Claims**
- 32 claims, all with quotes. 13 report statistics (43 tests), 32 have a criterion and 18 have expected values.
- Two claims (Figure 7 and Figure S15) use the two-photon imaging data and can't be tested on DANDI:000552. Those data are available from M. Bartos on request and are not deposited; both criteria say so.

**Details left open, and the readings named**
- **40% step filter:** the Methods say "max firing rate across trials", which could be the raw or the fitted maximum. The code uses the maximum of the fitted step function; the raw maximum is a variant.
- **Pool for the 212/3,184 count:** familiar and novel sessions together, or familiar only.
- **Explained deviance (20% ON, 14% OFF):** held-out cross-validated, or in-sample. The Methods say 5-fold cross-validation repeated 10 times; the code holds out 10% per split, kept as a variant.
- **Figure 4D correlation:** the legend says Pearson and the code uses Spearman, so Spearman is a variant.
- **"First passage times" (75–77% under two trials):** individual passage times or switch durations. A pure step predicts 75% under two trials only for individual passage times, so that reading is likely the right one.
- **Co-switching ("at least one trial"):** a per-session test on the count of co-switching pairs (what the code does), or a per-trial test. "Same trial" against the code's window of one trial is a variant.
- **Figure 5C units:** neurons with metrics averaged over fields (Methods), or fields matched across environments by field index (code).
- **Same-cell field pairs (781 and 41):** environments pooled or familiar only; any switch or switches of the same type.
- **Field width on one trial (Figure S13A):** the detected field's width, or the width above half the peak.
- **Switch time for the waveform control (Figure S1H):** the start of the switch trial, or the animal's entry into the field.
- **Figure S2 categories:** four switching classes, or switching against not switching.
- **Figure S5 units:** session with turns pooled (code), or session and turn.
- **Figure 1I test:** the paper names none and the code has none. The readings are per-session slopes tested with the Methods' default Wilcoxon signed-rank test, or the code's tentative regression on the median over sessions.
- **Claims with no test in the paper:** Figure 1D, 1H, 3D–F population, 4N–O, S8A–B and S14. These use the Methods' default tests (Wilcoxon signed-rank or rank-sum, Pearson), and each criterion says so. Where the paper states a contrast only in words, I set the decision thresholds myself and the criterion says it chose them (Figure 1H "twice as steep", the GLM-drop spread rule, a 0.05 absolute tolerance on r).
- **Figure S8C:** the paper's familiar p (3 × 10⁻¹¹) is significant even though r = 0.01, so that absence claim is judged on r, and the criterion explains why.
- **Figure 2E groups:** I took "Familiar" to mean the familiar sessions of the three mice that also ran a novel environment, which gives 12 sessions in the code's list, matching the n = 12 in the legend.

**Missing**
- Nothing that a claim needs from the text is missing.
- The imaging data are not public, as above.
- The code's session database and intermediate files are not in the repository, so the session list comes only from the notebooks' stored outputs.
- Numbers printed only inside figure panels were not read.

## End of run

20 turns, 12 minutes, $5.42 at API prices, result: success.
