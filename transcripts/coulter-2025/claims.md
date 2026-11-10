# coulter-2025 · claims · run 42729157391

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
grep -n "^#" docs/protocol.md | head -50; ls paper/ claims/ | head -50
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -n 1,192p docs/protocol.md; ls -la paper/
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cat claims/fouke-2025.yaml | head -150; cat papers/datasets/coulter-2025.yaml
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
[... 137 more lines not kept]
```

**Agent calls Bash**

```bash
cat paper/10.1016-j.neuron.2024.12.023.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1016-j.neuron.2024.12.023.txt"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1016-j.neuron.2024.12.023.txt",
 "offset": 925
}
```

Result: not kept, because it reads the paper's text.

**Agent**

The full text, STAR Methods and supplement (with Table S1) are all present. Next, the paper's code (Zenodo 14522610) and the dandiset's description.

**Agent calls Bash**

```bash
curl -sL https://zenodo.org/api/records/14522610 | python -c "import json,sys;d=json.load(sys.stdin);print(d['metadata']['title']);print(d['metadata'].get('related_identifiers'));[print(f['key'],f['links']['self']) for f in d['files']]"; curl -sL https://api.dandiarchive.org/api/dandisets/001280/versions/0.241218.2300/ | python -c "import json,sys;d=json.load(sys.stdin);print(d['name']);print(d['description']);print(d.get('assetsSummary'))"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR && curl -sL -o code.zip "https://zenodo.org/api/records/14522610/files/LorenFrankLab/hippocampus_content_neurofeedback-v0.0.4.zip/content" && unzip -qo code.zip && ls -R LorenFrankLab* | head -80; curl -s https://api.github.com/repos/LorenFrankLab/hippocampus_content_neurofeedback/git/refs/tags/v0.0.4
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR/LorenFrankLab-hippocampus_content_neurofeedback-b27655c && cat README.md && wc -l hippocampus_content_neurofeedback/*.py && python -c "
import json;nb=json.load(open('hippocampus_content_neurofeedback/single_cell_summary_plots-share-v3.ipynb'))
print(len(nb['cells']))
for i,c in enumerate(nb['cells']):
  s=''.join(c['source'])
  if c['cell_type']=='markdown': print(i,'MD',s[:200].replace('\n',' | '))
"
```

````
# Package Name
Add package description

### Installation
```bash
pip install package_name
```
Or
```bash
conda install -c edeno package_name
```
Or
```bash
git clone <package.git>
pip install .
```

### Usage

### Developer Installation
[... 44 more lines not kept]
````

**Agent calls Bash**

```bash
cd $TMPDIR/LorenFrankLab-hippocampus_content_neurofeedback-b27655c && python -c "
import json;nb=json.load(open('hippocampus_content_neurofeedback/single_cell_summary_plots-share-v3.ipynb'))
for i,c in enumerate(nb['cells']):
  s=''.join(c['source'])
  print('##### CELL',i,c['cell_type']);print(s)
" > $TMPDIR/nb.txt; wc -l $TMPDIR/nb.txt
```

```
6654 /tmp/claude-1001/nb.txt
Shell cwd was reset to
```

**Agent calls Grep**

```json
{
 "pattern": "mixedlm|mannwhitney|linregress|zscore|chi2|rayleigh|proportions_ztest|pearson|spearman|ols\\(|smf\\.|> ?67|>= ?67|0\\.9|read_csv|read_pickle|pd\\.read|##### CELL",
 "path": "/tmp/claude-1001/nb.txt",
 "output_mode": "content",
 "head_limit": 0
}
```

```
1:##### CELL 0 code
4:##### CELL 1 code
20:##### CELL 2 code
28:##### CELL 3 code
30:##### CELL 4 markdown
32:##### CELL 5 code
39:##### CELL 6 code
73:##### CELL 7 code
106:##### CELL 8 markdown
108:##### CELL 9 code
262:##### CELL 10 markdown
264:##### CELL 11 code
289:##### CELL 12 markdown
291:##### CELL 13 code
314:##### CELL 14 code
341:##### CELL 15 code
389:##### CELL 16 markdown
391:##### CELL 17 code
411:##### CELL 18 code
444:##### CELL 19 code
[... 239 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/nb.txt",
 "offset": 1,
 "limit": 420
}
```

```
1	##### CELL 0 code
2	%reload_ext autoreload
3	%autoreload 2
4	##### CELL 1 code
5	import os
6	import numpy as np
7	import pandas as pd
8	import datajoint as dj
9	import pynwb
10	# ignore datajoint+jupyter async warnings
11	import warnings
12	warnings.simplefilter('ignore', category=DeprecationWarning)
13	warnings.simplefilter('ignore', category=ResourceWarning)
14	warnings.simplefilter('ignore', category=UserWarning)
15	warnings.simplefilter('ignore', category=PendingDeprecationWarning)
16	warnings.simplefilter('ignore', category=FutureWarning)
17	#warnings.simplefilter('ignore', category=SettingWithCopyWarning)
18	
19	
20	##### CELL 2 code
[... 400 more lines not kept]
```

**Agent calls Bash**

```bash
grep -n -i "with_inputs\|with_labels\|elsewhere" docs/*.md | head -30
```

```
docs/design.md:118:  elsewhere. This is the guard against a result that only looks right.
docs/pilot-notes.md:95:  with outside data (`data: dandiset` or `with_inputs`), and the dashboard
docs/pilot-notes.md:107:RDMs that are not public, are now marked `with_inputs`, and its attempt
docs/pilot-notes.md:123:  `data: with_labels`, for outside sources that only name or map codes the
docs/pilot-notes.md:162:adds a fourth data kind, `elsewhere`, for a claim whose data the dandiset
docs/pilot-notes.md:166:dandiset's claims and from `with_inputs` claims. It is never blocked with
docs/pipeline.md:49:`other_data` (a research paper whose data are elsewhere; `data_in` says where),
docs/pipeline.md:68:aside, are mostly on data elsewhere stops the chain before its checkpoint.
docs/protocol.md:149:     `with_labels`, `with_inputs` or `elsewhere` (step 4, and author, step
docs/protocol.md:156:     rests on it. A claim on data in none of them is `data: elsewhere`, or
docs/protocol.md:227:4. Decide what comes from outside the dataset. Data from elsewhere may be
docs/protocol.md:236:     `data: with_labels`, `data: with_inputs` or `data: elsewhere`. The
docs/protocol.md:237:     `with_inputs` and `elsewhere` claims are counted apart, each group on
docs/protocol.md:239:   - `with_labels` is for outside sources that only name or map codes the
docs/protocol.md:261:   - `elsewhere` is for a claim whose data the dataset does not hold at
docs/protocol.md:270:   - The notes of a `with_inputs` claim say which side a difference comes
docs/protocol.md:281:     `data: elsewhere` instead (step 4).
```

**Agent calls Bash**

```bash
sed -n 225,285p docs/protocol.md
```

```
why in the notebook's header. If versions differ in content the analysis
   uses, show the difference.
4. Decide what comes from outside the dataset. Data from elsewhere may be
   used only when the claims file says the paper relies on it, it is public,
   and it is pinned: a DOI, or a repository at a commit. Record each under
   `inputs` in the attempt. A claim whose outside input is not public is
   blocked with `data_missing`, and its notes say where you looked.

   The registry judges the dataset, so claims that use outside data are
   kept apart:
   - Each claim says what its test uses: `data: dataset` (the default),
     `data: with_labels`, `data: with_inputs` or `data: elsewhere`. The
     `with_inputs` and `elsewhere` claims are counted apart, each group on
     its own; the others count towards what is said about the dataset.
   - `with_labels` is for outside sources that only name or map codes the
     dataset already holds, such as stimulus names for its stimulus codes.
     They bring in no measurements. A link claim must confirm the names, and
     the missing names are recorded as a finding (`metadata_insufficient`).
   - When outside data has to be matched to the dataset's cells, sessions
     or subjects, a claim of its own (`kind: link`) tests the link. Link
[... 41 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/LorenFrankLab-hippocampus_content_neurofeedback-b27655c/hippocampus_content_neurofeedback && for f in *.py; do echo "=== $f"; head -40 $f | grep -v "^\s*$" | head -25; done 2>/dev/null | head -300
```

```
=== __init__.py
# flake8: noqa
=== mcoulter_arm_end_assemblies.py
# required packages:
import datajoint as dj
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import sys
from hippocampus_content_neurofeedback.mcoulter_reward_cluster_list import RewardClusterList
from hippocampus_content_neurofeedback.mcoulter_realtime_filename import RealtimeFilename
from hippocampus_content_neurofeedback.mcoulter_arm_end_clusters import ArmEndClusters
from spyglass.decoding.v0.sorted_spikes import SortedSpikesIndicator
from spyglass.common import IntervalList
from spyglass.spikesorting.v0 import Waveforms, CuratedSpikeSorting
from spyglass.mcoulter_statescript_rewards import (StatescriptReward)
from spyglass.utils.nwb_helper_fn import close_nwb_files
import pprint
import warnings
# import matplotlib.pyplot as plt
[... 281 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/LorenFrankLab-hippocampus_content_neurofeedback-b27655c/hippocampus_content_neurofeedback && sed -n 40,865p mcoulter_realtime_posterior_sum.py | grep -v "^\s*#\s*print\|^\s*$"
```

```
<persisted-output>
Output too large (32.2KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/71848366-dcb5-425d-9e94-3dcad2ca00d9/tool-results/b7ebqj0ms.txt

Preview (first 2KB):
schema = dj.schema("mcoulter_realtime_posterior_sum")
# parameters to calculate place field
@schema
class RealtimePosteriorSumParameters(dj.Manual):
    definition = """
    posterior_sum_param_name : varchar(500)
    ---
    posterior_sum_parameters : mediumblob
    """
    # can include description above
    # description : varchar(500)
    def insert_default(self):
        posterior_sum_parameters = {}
        posterior_sum_parameters["well_distance_max"] = 17
        posterior_sum_parameters["center_well_pos"] = [449, 330]
        posterior_sum_parameters[
[... 47 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/71848366-dcb5-425d-9e94-3dcad2ca00d9/tool-results/b7ebqj0ms.txt",
 "offset": 60
}
```

```
60	    non_engaged_time : double
61	    task2_center_velocity : double
62	    arm1_angles_dict : blob
63	    arm2_angles_dict : blob
64	    arm1_x1_dict : blob
65	    arm1_y1_dict : blob
66	    arm2_x1_dict : blob
67	    arm2_y1_dict : blob
68	    """
69	    def make(self, key):
70	        print(f"Computing realtime posterior sum for: {key}")
71	        def find_nearest(array, value):
72	            array = np.asarray(array)
73	            idx = (np.abs(array - value)).argmin()
74	            return array[idx], idx
75	        plot_on = False
76	        plot_2 = False
77	        if (
78	            key["nwb_file_name"].split("2")[0]
79	            == key["realtime_filename"].split("_")[3]
[... 640 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/nb.txt",
 "offset": 1191,
 "limit": 320
}
```

```
1191	##### CELL 38 markdown
1192	## Figure 4
1193	##### CELL 39 code
1194	# figure 4A - head direction example
1195	##### CELL 40 code
1196	# load and plot posterior - head direction
1197	file = open('/stelmo/mcoulter/coulter_all_figures/figure2a_decode.pkl','rb')
1198	posterior_to_plot = pickle.load(file)
1199	file.close()
1200	
1201	posterior_to_plot_reset = posterior_to_plot.reset_index()
1202	
1203	posterior_offline1 = posterior_to_plot.iloc[:,27:68]
1204	posterior_offline2 = posterior_offline1.fillna(0)
1205	post_heatmap = posterior_offline2.transpose()
1206	post_heatmap = post_heatmap.iloc[::-1]
1207	
1208	# size for individual reward events: (5,6)
1209	matplotlib.rcParams.update({'font.size': 12})
1210	gs_kw = dict(height_ratios=[1])
[... 300 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/nb.txt",
 "offset": 1821,
 "limit": 350
}
```

```
1821	##### CELL 55 code
1822	# grouped analysis: LME
1823	
1824	import statsmodels.api as sm
1825	import statsmodels.formula.api as smf
1826	
1827	arthur_first = arthur_head_dir_target.copy()
1828	arthur_second = arthur_content_target.copy()
1829	                         
1830	ginny_first = ginny_head_dir_target.copy()
1831	ginny_second = ginny_content_target.copy()
1832	                         
1833	tonks_first = tonks_head_dir_target.copy()
1834	tonks_second = tonks_content_target.copy()
1835	                         
1836	molly_first = molly_head_dir_target.copy()
1837	molly_second = molly_content_target.copy()
1838	                         
1839	ron_first = ron_head_dir_target.copy()
1840	ron_second = ron_content_target.copy()
[... 330 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/LorenFrankLab-hippocampus_content_neurofeedback-b27655c/hippocampus_content_neurofeedback && python -c "
import json;nb=json.load(open('single_cell_summary_plots-share-v3.ipynb'))
print(nb.get('metadata'))
for i,c in enumerate(nb['cells']):
  for o in c.get('outputs',[]):
    t=o.get('text') or o.get('data',{}).get('text/plain')
    if t: print('## OUT',i); print(''.join(t)[:1500])
"
```

```
{'kernelspec': {'display_name': 'Python 3 (ipykernel)', 'language': 'python', 'name': 'python3'}, 'language_info': {'codemirror_mode': {'name': 'ipython', 'version': 3}, 'file_extension': '.py', 'mimetype': 'text/x-python', 'name': 'python', 'nbconvert_exporter': 'python', 'pygments_lexer': 'ipython3', 'version': '3.9.13'}}
## OUT 6
<matplotlib.collections.LineCollection at 0x7f42719818b0>
## OUT 6
<Figure size 1400x600 with 2 Axes>
## OUT 7
<matplotlib.collections.LineCollection at 0x7f428d735310>
## OUT 7
<Figure size 1400x600 with 2 Axes>
## OUT 18
<matplotlib.collections.LineCollection at 0x7f42700305e0>
## OUT 18
<Figure size 600x600 with 2 Axes>
## OUT 19
<matplotlib.collections.LineCollection at 0x7f4272cf44c0>
## OUT 19
<Figure size 600x600 with 2 Axes>
## OUT 20
<matplotlib.collections.LineCollection at 0x7f42842c2f40>
## OUT 20
[... 640 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/nb.txt",
 "offset": 543,
 "limit": 240
}
```

```
543	##### CELL 22 code
544	# load dictionaries
545	
546	# key
547	#ginny_trajectory_dict = {}
548	#ginny_trajectory_dict[1] =      ginny_total 
549	#ginny_trajectory_dict[2] =       ginny_arm_base 
550	#ginny_trajectory_dict[3] =       ginny_med_traj 
551	#ginny_trajectory_dict[4] =      ginny_long_traj 
552	#ginny_trajectory_dict[5] =       ginny_remote_distance 
553	#ginny_trajectory_dict[6] =       ginny_arm_end 
554	#ginny_trajectory_dict[7] =       ginny_jumps 
555	#ginny_trajectory_dict[8] =      ginny_longtraj 
556	#ginny_trajectory_dict[9] =      ginny_medtraj 
557	#ginny_trajectory_dict[10] =     ginny_armbase_brain_state 
558	
559	fileObj = open('/stelmo/mcoulter/coulter_all_figures/pippin_trajectory_dict_no_lfp.pkl', 'rb')
560	traj_dict = pickle.load(fileObj)
561	file.close()
562	pippin_total = traj_dict[1]
[... 220 more lines not kept]
```

**Agent calls Grep**

```json
{
 "pattern": "med_traj|long_traj|arm_base_1bin|remote_distance|linregress|rayleigh|chi2|speed|velocity.*4|> ?0\\.2|ripple_times|Kay_ripple_detector\\(",
 "path": "/tmp/claude-1001/LorenFrankLab-hippocampus_content_neurofeedback-b27655c/hippocampus_content_neurofeedback",
 "output_mode": "content",
 "head_limit": 80
}
```

```
/tmp/claude-1001/LorenFrankLab-hippocampus_content_neurofeedback-b27655c/hippocampus_content_neurofeedback/mcoulter_reward_cluster_list.py:188:                #   & {'place_field_param_name': '5cm_speed'}).fetch('sort_group_id'))
/tmp/claude-1001/LorenFrankLab-hippocampus_content_neurofeedback-b27655c/hippocampus_content_neurofeedback/mcoulter_theta_phase_shuffles.py:299:                    # lets just do 1000 times - need to start with 5000 to get ~1000 with speed >4
/tmp/claude-1001/LorenFrankLab-hippocampus_content_neurofeedback-b27655c/hippocampus_content_neurofeedback/mcoulter_theta_phase_shuffles.py:366:                        # get position and generate smooth speed
/tmp/claude-1001/LorenFrankLab-hippocampus_content_neurofeedback-b27655c/hippocampus_content_neurofeedback/mcoulter_theta_phase_shuffles.py:374:                            "speed_smooth"
/tmp/claude-1001/LorenFrankLab-hippocampus_content_neurofeedback-b27655c/hippocampus_content_neurofeedback/mcoulter_theta_phase_shuffles.py:376:                            spyglass_position_df["head_speed"], 2
/tmp/claude-1001/LorenFrankLab-hippocampus_content_neurofeedback-b27655c/hippocampus_content_neurofeedback/mcoulter_theta_phase_shuffles.py:495:                            # need to add smooth speed from position_df to lfp timestamps
/tmp/claude-1001/LorenFrankLab-hippocampus_content_neurofeedback-b27655c/hippocampus_content_neurofeedback/mcoulter_theta_phase_shuffles.py:499:                            print(merged_df[merged_df['speed_smooth']>4].shape)
/tmp/claude-1001/LorenFrankLab-hippocampus_content_neurofeedback-b27655c/hippocampus_content_neurofeedback/mcoulter_theta_phase_shuffles.py:510:                                    mvt_random = random_df[random_df['speed_smooth']>4]
/tmp/claude-1001/LorenFrankLab-hippocampus_content_neurofeedback-b27655c/hippocampus_content_neurofeedback/mcoulter_realtime_lfp_spectogram.py:338:        speed_thresh = lfp_posterior_sum_parameters['speed_thresh']
/tmp/claude-1001
[... 72 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/LorenFrankLab-hippocampus_content_neurofeedback-b27655c/hippocampus_content_neurofeedback && grep -n "insert_default" -A30 mcoulter_realtime_lfp_posterior_sum.py | head -50; grep -n "Kay_ripple\|zscore_threshold\|minimum_duration\|speed_thresh\|min_diff\|> 0.4\|>0.4\|random\b\|np.random\|smooth_speed\|head_speed\|gaussian\|17" mcoulter_realtime_lfp_posterior_sum.py | head -80
```

```
72:    def insert_default(self):
73-        lfp_posterior_sum_parameters = {}
74-        lfp_posterior_sum_parameters["well_distance_max"] = 17
75-        lfp_posterior_sum_parameters["center_well_pos"] = [449, 330]
76-        lfp_posterior_sum_parameters["arm_posterior_fraction"] = 0.4
77-        lfp_posterior_sum_parameters["center_posterior_fraction"] = 0.6
78-        lfp_posterior_sum_parameters[
79-            "file_directory"
80-        ] = "/cumulus/mcoulter/tonks/realtime_merged/"
81-        self.insert1(
82-            ["default", lfp_posterior_sum_parameters], skip_duplicates=True
83-        )
84-
85-
86-# select parameters
87-@schema
88-class LFPPosteriorSumSelection(dj.Manual):
89-    definition = """
90-    -> RealtimeFilename
91-    -> LFPPosteriorSumParameters
[... 48 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/LorenFrankLab-hippocampus_content_neurofeedback-b27655c/hippocampus_content_neurofeedback && sed -n 690,760p mcoulter_realtime_lfp_posterior_sum.py; sed -n 960,1100p mcoulter_realtime_lfp_posterior_sum.py; sed -n 1210,1300p mcoulter_realtime_lfp_posterior_sum.py
```

```
elif key["nwb_file_name"] == "molly20220324_.nwb" and pos_name == 'pos 3 valid times':
                    sort_interval = sort_intervals[0]
                elif key["nwb_file_name"] == "molly20220324_.nwb" and pos_name == 'pos 6 valid times':
                    sort_interval = sort_intervals[1]

                elif pos_name == all_pos[0]:
                    sort_interval = sort_intervals[0]
                elif pos_name == all_pos[1]:
                    sort_interval = sort_intervals[0]
                elif pos_name == all_pos[2]:
                    sort_interval = sort_intervals[1]

                # get position and generate smooth speed
                spyglass_position_df = (
                    IntervalPositionInfo
                    & {"nwb_file_name": key["nwb_file_name"]}
                    & {"interval_list_name": pos_name}
                    & {"position_info_param_name": "default_decoding"}
                ).fetch1_dataframe()
                spyglass_position_df[
[... 284 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/LorenFrankLab-hippocampus_content_neurofeedback-b27655c/hippocampus_content_neurofeedback && grep -n "def \|insert_default\|FastICA\|ica\|marchenko\|lambda_max\|eig\|> *100\|>100\|random\|target_assembl\|zscore\|bin_size\|0.03\|900\|strength\|weight" mcoulter_reward_assemblies.py | head -120
```

```
10:from spyglass.decoding import SortedSpikesIndicator
51:    def insert_default(self):
59:            ["default", assembly_parameters], skip_duplicates=True
74:# this is the computed table - basically it has the results of the analysis
84:    def make(self, key):
108:        def marcenkopastur(significance):
110:                nbins = significance.nbins
111:                nneurons = significance.nneurons
112:                tracywidom = significance.tracywidom
114:                # calculates statistical threshold from Marcenko-Pastur distribution
121:        def getlambdacontrol(zactmat_):
123:                significance_ = PCA()
124:                significance_.fit(zactmat_.T)
125:                lambdamax_ = np.max(significance_.explained_variance_)
129:        def binshuffling(zactmat,significance):
131:                np.random.seed()
133:                lambdamax_ = np.zeros(significance.nshu)
134:                for shui in range(significance.nshu):
137:                                randomorder = np.argsort(np.random.rand(significance.nbins))
138:                                zactmat_[neuroni,:] = activity[randomorder]
[... 63 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/LorenFrankLab-hippocampus_content_neurofeedback-b27655c/hippocampus_content_neurofeedback && sed -n 40,75p mcoulter_reward_assemblies.py; sed -n 760,872p mcoulter_reward_assemblies.py; grep -n "insert_default" -A25 mcoulter_arm_end_assemblies.py | head -40; grep -n "target\|random\|100\|> 0.4\|>0.4\|max(" mcoulter_arm_end_assemblies.py | head -80
```

```
@schema
class CellAssemblyParameters(dj.Manual):
    definition = """
    assembly_param_name : varchar(500)
    ---
    assembly_parameters : blob
    """

    # can include description above
    # description : varchar(500)

    def insert_default(self):
        assembly_parameters = {}
        assembly_parameters["cluster_type"] = 'new_100ms'
        assembly_parameters["sum_bins"] = 5
        assembly_parameters["nshu"] = 100
        assembly_parameters["percentile"] = 99.5

        self.insert1(
            ["default", assembly_parameters], skip_duplicates=True
[... 179 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/LorenFrankLab-hippocampus_content_neurofeedback-b27655c/hippocampus_content_neurofeedback && sed -n 330,460p mcoulter_arm_end_assemblies.py; sed -n 610,650p mcoulter_arm_end_assemblies.py
```

```
import scipy.optimize as optimize
                        rowind,colind = optimize.linear_sum_assignment(-simmat)
                        
                        rowind = fillmissingidxs(rowind,np.size(simmat,0))
                        colind = fillmissingidxs(colind,np.size(simmat,1))
                        
                        return simmat,rowind,colind
                else:
                        return simmat

        # need to insert a copy of target arm dictionaries
        # target dict for all days
        ron_all_dict = {'ron20210811_.nwb':2,'ron20210812_.nwb':2,
                        'ron20210813_.nwb':1,'ron20210814_.nwb':1,
                        'ron20210816_.nwb':2,'ron20210817_.nwb':2,'ron20210818_.nwb':2,
                        'ron20210819_.nwb':1,'ron20210820_.nwb':1,'ron20210821_.nwb':1,
                        'ron20210822_.nwb':2,'ron20210823_.nwb':2,'ron20210824_.nwb':2,
                        'ron20210825_.nwb':1,'ron20210826_.nwb':1,'ron20210827_.nwb':1,
                        'ron20210828_.nwb':2,'ron20210829_.nwb':2,'ron20210830_.nwb':2,
                        'ron20210831_.nwb':1,'ron20210901_.nwb':1,'ron20210902_.nwb':1} 
[... 152 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 3249,3270p $TMPDIR/nb.txt; echo ----; sed -n 3609,3650p $TMPDIR/nb.txt; echo ----; sed -n 4190,4256p $TMPDIR/nb.txt; echo; sed -n 4336,4370p $TMPDIR/nb.txt
```

```
##### CELL 88 code
import xarray as xr
import matplotlib.pyplot as plt
import pickle
from pynwb import NWBFile, TimeSeries, NWBHDF5IO
import matplotlib
##### CELL 89 code
# Figure 6A - examples
##### CELL 90 code
# load data
import pickle
import matplotlib.pyplot as plt
import numpy as np

# cell 10_2 - spike raster
fileObj = open('/stelmo/mcoulter/coulter_all_figures/figure_3a_cell_10_2_raster.pkl', 'rb')
cell1_raster = pickle.load(fileObj)
fileObj.close()
# cell 10_2 - place field
fileObj = open('/stelmo/mcoulter/coulter_all_figures/figure_3a_cell_10_2_place_field.pkl', 'rb')
[... 149 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 3483,3608p $TMPDIR/nb.txt | grep -v "^\s*$" | head -130
```

```
##### CELL 93 code
# Figure 6D and 6F - assembly activity times
##### CELL 94 code
# plot assembly times
fileObj = open('/stelmo/mcoulter/coulter_all_figures/figure_cell_assembly_plot.pkl', 'rb')
assembly_plot_dict = pickle.load(fileObj)
fileObj.close()
assembly_0_plot_x = assembly_plot_dict['assem_0_x']
assembly_0_plot_y = assembly_plot_dict['assem_0_y']
assembly_1_plot_x = assembly_plot_dict['assem_1_x']
assembly_1_plot_y = assembly_plot_dict['assem_1_y']
assembly_7_plot_x = assembly_plot_dict['assem_7_x']
assembly_7_plot_y = assembly_plot_dict['assem_7_y']
assembly_21_plot_x = assembly_plot_dict['assem_21_x']
assembly_21_plot_y = assembly_plot_dict['assem_21_y']
reward_times_plot = assembly_plot_dict['reward_times']
target_times_plot = assembly_plot_dict['target_times']
# reward: 900-1000, remote content: 935-965
start_time = 1636330955.311
first_time = 900
[... 90 more lines not kept]
```

**Agent calls Bash**

```bash
grep -n "fold\|ratio\|np.mean(.*no_reward\|np.median(.*no_reward\|/np.mean\|/np.median\|content 1\|head dir 1" $TMPDIR/nb.txt | head -30; sed -n 1688,1760p $TMPDIR/nb.txt
```

```
40:# decoding: arm exploration
56:gs_kw = dict(height_ratios=[1])
62:fig.suptitle('Tonks - arm exploration')
89:gs_kw = dict(height_ratios=[1])
426:gs_kw = dict(height_ratios=[1])
459:gs_kw = dict(height_ratios=[1])
492:gs_kw = dict(height_ratios=[1])
525:gs_kw = dict(height_ratios=[1])
849:gs_kw = dict(height_ratios=[1])
903:gs_kw = dict(height_ratios=[1])
957:gs_kw = dict(height_ratios=[1])
1011:gs_kw = dict(height_ratios=[1])
1210:gs_kw = dict(height_ratios=[1])
1247:gs_kw = dict(height_ratios=[1])
1692:arthur_content_end_norm = np.array(arthur_content_target)/np.mean(np.array(arthur_head_dir_target))
1693:arthur_head_dir_end_norm = np.array(arthur_head_dir_target)/np.mean(np.array(arthur_head_dir_target))
1695:ginny_content_end_norm = np.array(ginny_content_target)/np.mean(np.array(ginny_head_dir_target))
1696:ginny_head_dir_end_norm = np.array(ginny_head_dir_target)/np.mean(np.array(ginny_head_dir_target))
1698:tonks_content_end_norm = np.array(tonks_content_target)/np.mean(np.array(tonks_head_dir_target))
1699:tonks_head_dir_end_norm = np.array(tonks_head_dir_target)/np.mean(np.array(tonks_head_dir_target))
[... 83 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 5217,5262p $TMPDIR/nb.txt; sed -n 5537,5575p $TMPDIR/nb.txt; sed -n 5937,5975p $TMPDIR/nb.txt
```

```
##### CELL 127 code
# target content
fileObj = open('/stelmo/mcoulter/coulter_all_figures/pippin_lfp_remote.pkl', 'rb')
lfp_dict = pickle.load(fileObj)
fileObj.close()
pippin_target_still = lfp_dict['still']
pippin_target_mvt = lfp_dict['mvt']
pippin_target_rip = lfp_dict['rip']

fileObj = open('/stelmo/mcoulter/coulter_all_figures/tonks_lfp_remote.pkl', 'rb')
lfp_dict = pickle.load(fileObj)
fileObj.close()
tonks_target_still = lfp_dict['still']
tonks_target_mvt = lfp_dict['mvt']
tonks_target_rip = lfp_dict['rip']

fileObj = open('/stelmo/mcoulter/coulter_all_figures/ginny_lfp_remote.pkl', 'rb')
lfp_dict = pickle.load(fileObj)
fileObj.close()
ginny_target_still = lfp_dict['still']
[... 104 more lines not kept]
```

**Agent calls Bash**

```bash
grep -l "data: elsewhere" claims/*.yaml | head -3; f=$(grep -l "data: elsewhere" claims/*.yaml | head -1); grep -n -B3 -A8 "data: elsewhere" $f | head -40; grep -h -A6 "^outside_data\|^inputs:\|^external" claims/*.yaml | head -30; sed -n 1,80p tools/claims_check.py
```

```
claims/azcorra-2023.yaml
claims/berg-2020.yaml
claims/bouabid-2026.yaml
726-  quote: nuclei with fewer than 500 unique features were removed from each dataset ... In total, the
727-    integration resulted in a final dataset of 12,065 nuclei, with a mean UMI count of 3,435 and a
728-    mean of 1,683 features.
729:  data: elsewhere
730-  where: GEO GSE222558 (samples GSM6926026 and GSM6926027)
731-  expected:
732-  - quantity: Nuclei after quality control
733-    value: 12065
734-    tolerance: 1206.5
735-  - quantity: Mean UMI count per nucleus
736-    value: 3435
737-    tolerance: 343.5
--
747-    paragraph 1
748-  quote: Expression of Aldh1a1 and Anxa1, the latter of which is expressed only within a subset of
749-    Aldh1a1-expressing neurons.
750:  data: elsewhere
[... 103 more lines not kept]
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
  "paper",
  "claims"
 ],
 "properties": {
  "schema_version": {
   "const": 2
  },
  "dataset": {
   "description": "Before the cutover to paper-first records, the dataset a per-dataset claims file was read for. A paper's own claims file (claims/<paper>.yaml) leaves it out.",
   "type": "object",
   "additionalProperties": false,
   "required": [
[... 181 more lines not kept]
```

**Agent calls Bash**

```bash
python -c "
import json;s=json.load(open('schemas/claims.schema.json'));print(json.dumps(s,indent=1)[6000:])"; head -30 claims/azcorra-2023.yaml
```

```
required": [
        "where"
       ]
      }
     }
    ]
   }
  },
  "checks": {
   "description": "Checks of the claims file against the paper by a second reader (docs/protocol.md, Reader, step 5), oldest first. The file is ready for an attempt when the last says so.",
   "type": "array",
   "items": {
    "type": "object",
    "additionalProperties": false,
    "required": [
     "date",
     "kind",
     "ready"
    ],
    "properties": {
[... 163 more lines not kept]
```

**Agent calls Bash**

```bash
grep -l "written by an agent\|Written by an agent" claims/*.yaml | head -3; f=$(grep -l "ritten by an agent" claims/*.yaml | tail -1); sed -n 1,40p $f
```

```
claims/armstrong-2026.yaml
claims/ashworth-2025.yaml
claims/athalye-2023.yaml
# Claims for Zhuang, Lemak, Sridhar & Nelson (2025), Brain 149:238-251, on dandiset 001177.
# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"), 2026-10-28,
# protocol pilot-12 as stated in docs/protocol.md. The writer did not look at the dandiset's data or
# files; only its title and description on the archive were read. Claim fig1fg-delay-discounting
# was added by the check of 2026-10-28.
#
# Text read: the version of record (open access, CC BY), full text as served by Europe PMC
# (PMC12597312), with its one supplement, awaf312_supplementary_data.pdf (Figures S1 to S8 and
# legends, Supplementary Materials and methods, and Table 1, "Experimental analysis and
# statistics"). Figure panels of the main paper were not available as images; values in the main
# figure legends were read from the text. The pie-chart percentages of Figures S5D and S8A-B were
# read from the supplement PDF (pages 7 and 10), as the text holds only the legends.
#
# Code read. The paper links (1) UCSF-Nelson-Lab/ICD-Cognitive-Analysis, tag ICD, commit 5528e22
# (Zenodo doi:10.5281/zenodo.10703139, record 10703140): Python scripts that count task events per
# block of the delay discounting task (delay_discounting_task.py, phase2.py, phase3.py) and
# Summary_Cognitive.m, which averages each mouse's sessions within a condition, fits
[... 23 more lines not kept]
```

**Agent calls Bash**

```bash
curl -sL "https://datadryad.org/api/v2/datasets/doi%3A10.5061%2Fdryad.dz08kps72" | python -c "import json,sys;d=json.load(sys.stdin);print(d.get('title'));print(d.get('versionNumber'),d.get('publicationDate'));print(d.get('abstract','')[:1500])"
```

Result: the fetched text is not kept.

**Agent**

Code reading is done. The paper's analysis runs on the real-time decoder output deposited on Dryad, together with the dandiset's raw spikes, LFP and position. I'll write the claims file now.

**Agent calls Write**

```json
{
 "file_path": "claims/coulter-2025.yaml",
 "content": "# Claims for Coulter, Gillespie, Chu, ..., Eden, Kemere & Frank (2025), Neuron 113:949-961,\n# \"Closed-loop modulation of remote hippocampal representations with neurofeedback\", on dandiset\n# 001280 (version 0.241218.2300, the version the paper cites).\n# Written by an agent (model \"claude-opus-5-5\", Claude Code, runner \"GitHub Actions\"), 2026-11-10,\n# protocol pilot-14 as stated in docs/protocol.md. The writer did not look at the dandiset's data or\n# files; only its title and description on the archive were read.\n#\n# Text read: the version of record (open access, CC BY), from a PDF supplied by a person, with its\n# supplement (Figures S1 to S7 and their legends, and Table S1, \"Number of samples and statistical\n# tests for main figures\"), as the extracted text paper/10.1016-j.neuron.2024.12.023.txt. The text\n# is complete (Results, legends, STAR Methods, supplement). Its minus signs in exponents are garbled\n# (\"p = 3.9e?11\"); they were read as minus signs. No figure image was needed.\n#\n# Code read. The paper links (1) the analysis code and figure notebook, Zenodo\n# doi:10.5281/zenodo.14522610, which is LorenFrankLab/hippocampus_content_neurofeedback tag v0.0.4,\n# commit b27655c66cba8dbbcf2c23ada594f9d8852f8844; (2) the real-time decoder (Zenodo\n# doi:10.5281/zenodo.14399029, the version used), not read, as no criterion rests on it. The\n# repository holds DataJoint/Spyglass table classes that compute per-session quantities from the\n# real-time decoder files and the Spyglass database (mcoulter_realtime_posterior_sum.py for target\n# representation, mcoulter_realtime_lfp_posterior_sum.py for brain state, mcoulter_*assemblies.py\n# for cell assemblies, mcoulter_theta_phase_shuffles.py for theta phase), and one notebook,\n# single_cell_summary_plots-share-v3.ipynb, that loads per-session and per-assembly summaries from\n# pickles (\"all files with path beginning with '/stelmo/mcoulter/coulter_all_figures' are in the\n# Dryad repository\"), makes the figures and runs the tests, with its printed outputs. The code that\n# classifies detected events (Figure 3) and computes the Figure 6 summaries from assembly activity\n# is not in the repository. What the code settles is cited in each criterion.\n# From the code: rat 1 = pippin, rat 2 = tonks, rat 3 = ginny, rat 4 = ron, rat 5 = molly, rat 6 =\n# arthur (notebook cell 2); the target arm of each recording day, for head direction and\n# neurofeedback days, is listed in mcoulter_arm_end_assemblies.py (dictionaries ron_all_dict and so\n# on, keyed by NWB file name). The decoder's linearized position has 41 bins of 5 cm, x00 to x40:\n# box x00-x08, arm 1 x13-x24, arm 2 x29-x40; arm ends (25 cm) x20-x24 and x36-x40; arm bases\n# (25 cm) x13-x17 and x29-x33 (mcoulter_realtime_posterior_sum.py). Distance to the center port\n# is the distance of the smoothed head position (smooth_x, smooth_y) from the center well position\n# in pixels times 0.222 cm per pixel.\n#\n# Data the paper used. Six adult male Long Evans rats (6 to 9 months), each with a 64-tetrode\n# microdrive in dorsal CA1 (both hemispheres); SpikeGadgets/Trodes recording at 30 kHz; position\n# from red and green headstage LEDs, 30 Hz camera, which also give head direction. Three sessions a\n# day of 40 to 45 min in a Y-shaped track (center box with a central reward port, two arms with\n# ports at their ends). Each session has an exploration phase (10 to 15 min; lit ports guide 12\n# visits to each arm end, randomly ordered, with returns to the center) and a feedback phase (30 min\n# or 75 rewards, whichever comes first) in which reward is only at the center port, after a tone,\n# for a nosepoke within 3 s. Days 1 to 4 are head direction feedback (tone for a head turn of 30\n# degrees to the left, arm 1, or right, arm 2; target switched after 2 days); then remote\n# representation neurofeedback, target the distal 25 cm of arm 1 or arm 2, switched every 3 days,\n# for 6 days (rat 1) or 18 days (rats 2 to 6). The tone was triggered by the real-time clusterless\n# decoder (6 ms bins) when, over a 30 ms running average, more than 40% of the posterior was in the\n# target arm end, less than 20% in the opposite arm and less than 20% in the box, at least 2\n# tetrodes (1 for rat 1) had spatially specific spikes, and the rat was less than 17 cm from the\n# center port. Sessions with high-quality decoding were included (Figure S1D, n = 19, 62, 53, 55,\n# 62, 63 sessions for rats 1 to 6). Measured variables the analyses use: the decoder's posterior\n# over linearized position for every 6 ms bin, actual position, task phase and detection (reward)\n# events; spike-sorted single units (MountainSort4); LFP (SWR detection, theta phase from a tetrode\n# in stratum oriens); head speed.\n#\n# Where the data are. The paper deposits the raw recordings on DANDI (doi:10.48324/dandi.001280/\n# 0.241218.2300; the archive's title is the paper's and its description says CA1 extracellular\n# recordings from male Long Evans rats during a neurofeedback task) and the real-time decoder\n# output, and the summarized results the notebook loads, on Dryad (doi:10.5061/dryad.dz08kps72,\n# version 7 of 2025-01-17). The decoded posteriors on which Figures 1, 3, 4, 5, S1 to S5 rest are\n# the real-time decoder's own output, so those claims are data elsewhere, on Dryad, and are to be\n# tested on its decoder files (rec_4 decoder, rec_7 occupancy, rec_11 and rec_12 stimulation\n# messages in each session's HDF5 file, as the code reads them), not on the summary pickles,\n# which can serve as a check. Figures 6, 7, S6 and S7 combine the decoder output with spikes, LFP\n# and position from the raw recordings, so they are with_inputs. Rewards (Figures 2 and S2D) are\n# events of the raw recordings.\n#\n# Statistics as the code runs them, for every claim that cites them: Mann-Whitney U is\n# scipy.stats.mannwhitneyu with its default two-sided alternative (the printed p of rat 1 in\n# Figure 4C, U = 0 for 12 against 3 sessions, p = 0.0044, is the exact two-sided value); the LME\n# is statsmodels smf.mixedlm(\"arm_representation ~ content_sessions\", groups = rat), REML, fit with\n# lbfgs, on the raw (not normalized) per-session values, with a random intercept per rat (the code\n# codes head direction sessions 1 and neurofeedback 0, which flips the sign of the coefficient but\n# not p); grouped regressions z-score each rat's values (scipy.stats.zscore) and run\n# scipy.stats.linregress on the pooled values against session.\nschema_version: 2\npaper: doi:10.1016/j.neuron.2024.12.023\nclaims:\n- id: fig2-max-rewards-neurofeedback\n  statement: Every rat reached the maximum of 75 rewards in at least one remote representation\n    neurofeedback session, with substantial variability across sessions and rats.\n  source: Results, Closed-loop hippocampal neurofeedback, paragraph 4; Figure 2\n  quote: Further, all six rats also reached the maximal number of rewards per session during remote\n    representation neurofeedback, although there was substantial variability across sessions and\n    rats.\n  criterion: A reward is a reward delivery at the center port during the feedback phase of a\n    neurofeedback session, counted from the recordings' behavioral events (the Methods say reward\n    port nosepokes were saved in the NWB file). Reproduced when each of the six rats has at least\n    one neurofeedback session with 75 rewards (the per-session maximum, Figure 2 legend). The\n    per-session counts are also compared with those the notebook lists for Figure 2 (cell 11,\n    \"checked with daily data records\"); the code's lists for rats 3 and 4 are identical, which\n    looks like a copying error, so rat 3's list is not used for the comparison.\n- id: figs2d-head-direction-rewards\n  statement: All six rats rapidly and consistently reached the maximum number of rewards per session\n    with head direction feedback.\n  source: Results, Closed-loop hippocampal neurofeedback, paragraph 4; Figure S2D\n  quote: Behavioral results showed that all six rats were able to rapidly and consistently maximize\n    the number of rewards per session with behavioral feedback based on head direction (Figure\n    S2D).\n  criterion: Rewards per head direction feedback session (12 per rat) counted as in\n    fig2-max-rewards-neurofeedback. The paper gives no threshold for \"rapidly and consistently\";\n    the notebook's counts (cell 28) have 75 rewards in at least 10 of 12 sessions in every rat. The\n    reading used is that each rat reaches 75 rewards in more than half of its head direction\n    sessions and in at least one of the three sessions of its first day. Reproduced when this\n    holds in all six rats.\n- id: session-inclusion-decoding-quality\n  statement: A small number of sessions with low-quality decoding were excluded; the included\n    sessions number 19, 62, 53, 55, 62 and 63 for rats 1 to 6.\n  source: Results, Closed-loop hippocampal neurofeedback, paragraph 5; STAR Methods, Data inclusion;\n    Figure S1D and S2B legends\n  quote: A small number of lower-quality decoding sessions were excluded from further analyses.\n  data: elsewhere\n  where: Dryad doi:10.5061/dryad.dz08kps72 (version 7), real-time decoder output files\n  expected:\n  - quantity: Included sessions, rat 1\n    value: 19\n    tolerance: 1.9\n  - quantity: Included sessions, rat 2\n    value: 62\n    tolerance: 6.2\n  - quantity: Included sessions, rat 3\n    value: 53\n    tolerance: 5.3\n  - quantity: Included sessions, rat 4\n    value: 55\n    tolerance: 5.5\n  - quantity: Included sessions, rat 5\n    value: 62\n    tolerance: 6.2\n  - quantity: Included sessions, rat 6\n    value: 63\n    tolerance: 6.3\n  criterion: The Methods define a high-quality session as one in which, during the exploration phase,\n    when the rat was running outward from the box and in the end of the target arm, the posterior\n    maximum of the decoded position was in the target arm in at least 65% of 6 ms time bins. Two\n    details are open. \"Running outward\" needs a speed threshold and a direction; the readings are\n    (a) head speed above 4 cm/s (the movement threshold of Figures S2C and 7) with linear position\n    increasing, (b) any bin with linear position increasing. \"The target arm\" can be (a) the\n    session's target arm, or (b) each arm in turn, the session passing when both do. The counts in\n    Figure S1D are compared with the sessions each reading includes; the notebook's counts of good\n    and bad sessions (cell 13, 19/11, 62/1, 53/13, 55/11, 62/4, 62/4) are shown beside them.\n    Reproduced when, under one reading, every rat's count is within tolerance.\n- id: decoded-spike-fraction\n  statement: With a decoding latency of 30 ms, the real-time decoder decoded 90 to 99% of incoming\n    spikes, about one million spikes per session.\n  source: STAR Methods, Real-time spatial decoding; Figure S1D and S1E\n  quote: With a decoding latency of 30 msec, 90-99% of incoming spikes were decoded.\n  data: elsewhere\n  where: Dryad doi:10.5061/dryad.dz08kps72 (version 7), real-time decoder output files\n  expected:\n  - quantity: Fraction of spikes decoded per session, range across sessions\n    value: 0.945\n    tolerance: 0.054\n  criterion: Per included session, the fraction of spikes not dropped (Figure S1E, dropped means\n    latency above 30 ms) out of all spikes the decoder received (Figure S1D). The range 90 to 99%\n    widened by 10% of each bound is 81% to 100%. Reproduced when at least 90% of included sessions\n    lie in 81% to 100% and the median session lies in 90% to 99%.\n- id: fig1b-s3c-detection-content\n  statement: The representations that triggered reward during neurofeedback were specific to the\n    target arm end, while at head direction detections the decoder mostly represented the rat's\n    current location in the box.\n  source: Results, Closed-loop hippocampal neurofeedback, paragraph 5; Figure 1B right; Figure S3C\n  quote: As expected, the spatial content was specific to the chosen remote target, while during head\n    direction feedback sessions, the rat's current location was typically represented\n  data: elsewhere\n  where: Dryad doi:10.5061/dryad.dz08kps72 (version 7), real-time decoder output files\n  criterion: As in Figure S3C, the posterior averaged over the 30 ms (5 bins of 6 ms) that triggered\n    each detection, then averaged over detections, separately for arm 1 neurofeedback, arm 2\n    neurofeedback and head direction feedback sessions. Reproduced when, for both neurofeedback\n    groups, the summed average posterior in the target arm end exceeds that in the box and in the\n    opposite arm, and, for head direction detections, the summed average posterior in the box\n    (x00-x08) exceeds that in either arm end.\n- id: fig3b-jump-fraction\n  statement: Across rats, 65 to 75% of detected representations included only the target location\n    or jumped from the current location to the target.\n  source: Results, Closed-loop hippocampal neurofeedback, paragraph 6; Figure 3A and 3B\n  quote: Across all rats, 65%–75% of detected representations included only the target location or\n    jumped from the current location to the target\n  data: elsewhere\n  where: Dryad doi:10.5061/dryad.dz08kps72 (version 7), real-time decoder output files\n  expected:\n    quantity: Fraction of detected events classed as jump, per rat\n    value: 0.70\n    tolerance: 0.125\n  criterion: Events are the reward-triggering detections of the included neurofeedback sessions,\n    each with the 90 ms before detection (Figure 3B legend). The categories are from the Figure 3A\n    legend, jump (posterior mass above 0.4 in the 25 cm at the end of the arm) and jump and arm base\n    (posterior mass above 0.2 in the 15 cm at the base of the arm). The notebook (cell 23) takes the\n    jump fraction as (all events minus arm-base events) over all events. Open, as the classifying\n    code is not in the repository, is whether arm-base mass counts in (a) any 6 ms bin of the 90 ms\n    window, or (b) the posterior summed over the window; and whether the 15 cm are (a) the first\n    three bins of the arm (x13-x15, x29-x31) or (b) three bins of the 25 cm arm base. The range 65 to\n    75% widened by 10% of each bound is 58.5% to 82.5%. Reproduced when, under one reading, every\n    rat's jump fraction lies in it.\n- id: fig3b-trajectory-fraction\n  statement: Only 1 to 4% of detected representations were sequential trajectories down the length\n    of the arm.\n  source: Results, Closed-loop hippocampal neurofeedback, paragraph 6; Figure 3A and 3B\n  quote: Across all rats, 65%–75% of detected representations ... were sequential trajectories down\n    the length of the arm\n  data: elsewhere\n  where: Dryad doi:10.5061/dryad.dz08kps72 (version 7), real-time decoder output files\n  depends_on:\n  - fig3b-jump-fraction\n  expected:\n    quantity: Fraction of detected events classed as trajectories, per rat\n    value: 0.025\n    tolerance: 0.0175\n  criterion: Events as in fig3b-jump-fraction. The Figure 3A legend defines a medium trajectory as a\n    representation with a significant linear regression covering at least 35 cm in the target arm,\n    and a long trajectory as one covering at least 45 cm. Open are (1) which category the 1 to 4%\n    counts, (a) long trajectories, (b) medium and long together; (2) the regression, read as a\n    linear regression of the posterior-maximum position on time over the bins of the 90 ms window\n    whose maximum lies in the target arm, significant at p < 0.05, with covered distance the span of\n    fitted positions, and as variant the regression weighted by the posterior over all target-arm\n    bins. The range widened by 10% of each bound is 0.9% to 4.4%. Reproduced when, under one\n    reading, every rat's fraction lies in it.\n- id: figs4a-jump-distance\n  statement: Most detected representations (60 to 78% across rats) jumped at least 50 cm from the\n    rat's current location.\n  source: Results, Closed-loop hippocampal neurofeedback, paragraph 6; Figure S4A\n  quote: Most representations (60%–78%) jumped at least 50 cm from the rat's current location (Figure\n    S4A).\n  data: elsewhere\n  where: Dryad doi:10.5061/dryad.dz08kps72 (version 7), real-time decoder output files\n  expected:\n    quantity: Fraction of detected events with jump distance of 50 cm or more, per rat\n    value: 0.69\n    tolerance: 0.129\n  criterion: For each detected event, the distance between the rat's position and the nearest\n    high-confidence representation in the target arm (posterior mass above 0.4), including the 90\n    ms before detection (Figure S4A legend); the notebook (cells 57 and 58) takes the fraction of\n    events with distance of 50 cm or more from a 5 cm histogram. Open is what \"high-confidence\n    representation\" is; the readings are (a) the nearest position bin of the target arm in which a\n    6 ms bin's posterior summed over the 25 cm target arm end exceeds 0.4, measured as the linear\n    distance from the rat's linearized position to that bin, (b) the same with the nearest single\n    position bin holding posterior above 0.4 anywhere in the target arm. The range widened by 10% of\n    each bound is 54% to 85.8%. Reproduced when, under one reading, every rat's fraction lies in it.\n- id: fig3c-arm-base-visible\n  statement: The visible beginning of the target arm (its first 5 cm) was represented in only 7 to 19%\n    of detected events across rats, so visible cues contributed to few events.\n  source: Results, Closed-loop hippocampal neurofeedback, paragraph 7; Figure 3C\n  quote: these representations were present in 7%–19% of events across rats (Figure 3C)\n  data: elsewhere\n  where: Dryad doi:10.5061/dryad.dz08kps72 (version 7), real-time decoder output files\n  depends_on:\n  - fig3b-jump-fraction\n  expected:\n    quantity: Fraction of detected events representing the first 5 cm of the target arm, per rat\n    value: 0.13\n    tolerance: 0.079\n  criterion: Events as in fig3b-jump-fraction; the first 5 cm of the target arm is bin x13 (arm 1) or\n    x29 (arm 2). The paper does not say how much posterior counts as representing it; the readings\n    are (a) posterior above 0.2 in that bin in any 6 ms bin of the 90 ms window (the arm-base\n    threshold of Figure 3A), (b) above 0.4, (c) that bin being the posterior maximum in any 6 ms bin.\n    The range widened by 10% of each bound is 6.3% to 20.9%. Reproduced when, under one reading,\n    every rat's fraction lies in it.\n- id: fig3d-reward-port\n  statement: Detected remote representations only occasionally included the reward port location (the\n    last 5 cm of the arm), in 13 to 22% of events across rats.\n  source: Results, Closed-loop hippocampal neurofeedback, paragraph 7; Figure 3D\n  quote: detected remote representations only occasionally included a representation of the reward\n    port location ... showing that generation of remote representations was not primarily driven by\n    the target being a reward location\n  data: elsewhere\n  where: Dryad doi:10.5061/dryad.dz08kps72 (version 7), real-time decoder output files\n  depends_on:\n  - fig3b-jump-fraction\n  expected:\n    quantity: Fraction of detected events representing the last 5 cm of the target arm, per rat\n    value: 0.175\n    tolerance: 0.067\n  criterion: Events as in fig3b-jump-fraction; the last 5 cm is bin x24 (arm 1) or x40 (arm 2). The\n    readings of \"a representation of\" are those of fig3c-arm-base-visible, (a) posterior above 0.2,\n    (b) above 0.4, (c) posterior maximum, in any 6 ms bin of the 90 ms window. The range 13 to 22%\n    widened by 10% of each bound is 11.7% to 24.2%. Reproduced when, under one reading, every rat's\n    fraction lies in it.\n- id: figs4b-target-arm-majority\n  statement: At target representation times (more than 40% of the posterior in the target arm end,\n    rat at the center port), the majority of the posterior was almost always in the target arm, with\n    much less in the opposite arm or the box.\n  source: Results, Increased representation of the target location, paragraph 1; Figure S4B\n  quote: During these periods, the majority of the representation was almost always within the\n    target arm\n  data: elsewhere\n  where: Dryad doi:10.5061/dryad.dz08kps72 (version 7), real-time decoder output files\n  criterion: Target representation times are 6 ms bins of the feedback phase (taskState 2) with the\n    rat within 17 cm of the center port and the posterior summed over the target arm end above 0.4\n    (mcoulter_realtime_posterior_sum.py; Figure 4B legend), over neurofeedback sessions. For each\n    bin, the posterior summed over the whole target arm (x13-x24 or x29-x40), the opposite arm and\n    the box (x00-x08). The Figure S4B legend says \"nearly all times of target representation had at\n    least 50% representation in the target arm\"; \"nearly all\" is read as at least 90% of bins.\n    Reproduced when, in every rat, at least 90% of target representation bins have at least 0.5 of\n    the posterior in the target arm and the median posterior in the opposite arm and in the box are\n    each below that in the target arm.\n- id: fig4c-target-increase\n  statement: Representations of the target arm end were about 2-fold more prevalent during\n    neurofeedback sessions than during head direction feedback sessions with similar reward, in 5 of\n    6 rats individually and in a grouped mixed-effects analysis.\n  source: Results, Increased representation of the target location, paragraph 2; Figure 4C and 4E;\n    Table S1, Figure 4c\n  quote: Representations of the target region were approximately 2-fold more prevalent during\n    neurofeedback sessions compared with head direction feedback sessions (Figures 4C and 4E,\n    individually significant in 5 of 6 rats\n  statistics:\n  - about: grouped analysis, all data\n    test: linear mixed effects model, session type as test variable\n    p: 3.9e-11\n    n: 148 sessions of 6 rats\n  - about: rat 1\n    test: Mann-Whitney\n    p: 0.0044\n    n: 12 head direction and 3 neurofeedback sessions\n  - about: rat 2\n    test: Mann-Whitney\n    p: 0.0049\n    n: 12 head direction and 33 neurofeedback sessions\n  - about: rat 3\n    test: Mann-Whitney\n    p: 0.0014\n    n: 10 head direction and 16 neurofeedback sessions\n  - about: rat 4\n    test: Mann-Whitney\n    p: 5.5e-5\n    n: 10 head direction and 16 neurofeedback sessions\n  - about: rat 5\n    test: Mann-Whitney\n    p: 0.015\n    n: 11 head direction and 11 neurofeedback sessions\n  - about: rat 6\n    test: Mann-Whitney\n    p: 0.52\n    n: 9 head direction and 5 neurofeedback sessions\n  data: elsewhere\n  where: Dryad doi:10.5061/dryad.dz08kps72 (version 7), real-time decoder output files\n  depends_on:\n  - session-inclusion-decoding-quality\n  expected:\n  - quantity: Neurofeedback target representation relative to head direction feedback\n    value: 2.0\n    tolerance: 0.2\n  - quantity: Sessions per rat (head direction, neurofeedback), rats 1 to 6, as Table S1\n    value: 148\n    tolerance: 14.8\n  criterion: Sessions are the included sessions with more than 90% of the possible 75 rewards (68 or\n    more, Figure 4B legend), head direction and neurofeedback. The per-session measure is from\n    mcoulter_realtime_posterior_sum.py, the fraction of 6 ms decoder bins in the feedback phase\n    (taskState 2) with the rat less than 17 cm from the center port in which the posterior summed\n    over the session's target arm end (x20-x24 for arm 1, x36-x40 for arm 2) exceeds 0.4; the target\n    arm of head direction sessions is the arm of the rewarded head direction, from the code's\n    per-day dictionaries. Per rat, a two-sided Mann-Whitney U test of head direction against\n    neurofeedback sessions; grouped, the LME described in the opening comment. The fold change is\n    the notebook's (cell 52), each session's value divided by the mean of its rat's head direction\n    sessions, then the mean over all neurofeedback sessions pooled. Reproduced when neurofeedback is\n    higher in at least 5 rats with p < 0.05 in 5 rats, the LME p < 0.05 with neurofeedback higher,\n    and the fold change is within tolerance; partially reproduced when the LME holds but fewer rats\n    are individually significant or the fold change is out of tolerance. The session counts per rat\n    are compared with Table S1 (12/3, 12/33, 10/16, 10/16, 11/11, 9/5).\n- id: figs5a-target-increase-no-trigger\n  statement: The increase in target representation during neurofeedback holds when the\n    tone-triggering representations are removed.\n  source: Results, Increased representation of the target location, paragraph 2; Figure S5A\n  quote: Representations of the target region were approximately 2-fold more prevalent ...\n    tone-triggering representation removed\n  statistics:\n  - about: grouped analysis, tone-triggering representation removed\n    test: linear mixed effects model, session type as test variable\n    p: 3.6e-11\n    n: 148 sessions of 6 rats\n  data: elsewhere\n  where: Dryad doi:10.5061/dryad.dz08kps72 (version 7), real-time decoder output files\n  depends_on:\n  - fig4c-target-increase\n  criterion: As fig4c-target-increase, with the measure computed without the bins of the\n    tone-triggering representation. The code (mcoulter_realtime_posterior_sum.py, no_reward_time)\n    removes, for each reward message more than 1 s (30000 samples) after the previous one, the 5\n    decoder bins (30 ms) ending at it, then takes the fraction over the remaining center-port bins.\n    Reproduced when the LME p < 0.05 with neurofeedback higher. The notebook's fold change for this\n    measure (cell 72, 1.90) is reported beside the result.\n- id: fig4d-arm-base-no-increase\n  statement: Representation of a closer, non-rewarded control location, the base of the target arm,\n    was not more prevalent during neurofeedback than during head direction feedback, in any rat or\n    grouped.\n  source: Results, Increased representation of the target location, paragraph 2; Figure 4D and 4E;\n    Table S1, Figure 4d\n  quote: representations of a physically closer location (the base of the target arm) were not more\n    prevalent in neurofeedback sessions compared with head direction feedback sessions (Figures 4D\n    and 4E, non-significant in each rat\n  statistics:\n  - about: grouped analysis\n    test: linear mixed effects model, session type as test variable\n    p: 0.54\n    n: 148 sessions of 6 rats\n  - about: rat 1\n    test: Mann-Whitney\n    p: 0.23\n  - about: rat 2\n    test: Mann-Whitney\n    p: 0.43\n  - about: rat 3\n    test: Mann-Whitney\n    p: 0.77\n  - about: rat 4\n    test: Mann-Whitney\n    p: 0.30\n  - about: rat 5\n    test: Mann-Whitney\n    p: 0.32\n  - about: rat 6\n    test: Mann-Whitney\n    p: 0.80\n  data: elsewhere\n  where: Dryad doi:10.5061/dryad.dz08kps72 (version 7), real-time decoder output files\n  depends_on:\n  - fig4c-target-increase\n  criterion: A claim of absence, judged on the paper's tests. Sessions and measure as in\n    fig4c-target-increase with the posterior summed over the 25 cm base of the target arm (x13-x17\n    or x29-x33). Reproduced when the two-sided Mann-Whitney test has p >= 0.05 in every rat and the\n    LME has p >= 0.05; not reproduced when the LME or any rat shows a significant increase. The\n    fold change (notebook cell 53, 1.05) and each p are reported.\n- id: figs5c-opposite-arm-no-increase\n  statement: Representation of the end of the opposite, non-target arm was not enriched during\n    neurofeedback compared with head direction feedback.\n  source: Results, Increased representation of the target location, paragraph 2; Figure S5C\n  quote: Likewise, representation of the end of the opposite (nontarget) arm was not enriched (Figure\n    S5C\n  statistics:\n  - about: grouped analysis\n    test: linear mixed effects model, session type as test variable\n    p: 0.067\n    n: 148 sessions of 6 rats\n  data: elsewhere\n  where: Dryad doi:10.5061/dryad.dz08kps72 (version 7), real-time decoder output files\n  depends_on:\n  - fig4c-target-increase\n  criterion: A claim of absence, judged on the paper's test, the grouped LME. Sessions and measure as\n    in fig4c-target-increase with the posterior summed over the end of the arm opposite the target\n    (x36-x40 when the target is arm 1, x20-x24 when it is arm 2). Reproduced when the LME has p >=\n    0.05; not reproduced when it finds a significant increase. The per-rat Mann-Whitney tests and\n    the fold change (notebook cell 80, 1.50) are reported as variants.\n- id: reward-target-correlation\n  statement: Task performance (rewards per session) and the amount of target representation were\n    significantly positively correlated in five of six rats (rats 1, 2, 3, 5 and 6) and weakly\n    negatively correlated in rat 4.\n  source: Results, Increased representation of the target location, paragraph 2\n  quote: We also examined the relationship between task performance (number of rewards received) and\n    the amount of target representation and found that these measures were significantly positively\n    correlated in five of the six animals\n  statistics:\n  - about: rats 1, 2, 3, 5 and 6, positive correlation\n    test: correlation\n    p: 0.01\n    p_relation: <\n  - about: rat 4, negative correlation\n    test: correlation\n    p: 0.022\n  data: elsewhere\n  where: Dryad doi:10.5061/dryad.dz08kps72 (version 7), real-time decoder output files\n  depends_on:\n  - fig4c-target-increase\n  criterion: Per session, rewards (reward messages, as the code counts them) and the target\n    representation fraction of fig4c-target-increase. The paper names neither the correlation nor\n    the sessions, and the code does not hold this analysis. The readings are the correlation\n    (a) Pearson, (b) Spearman, over the sessions (a) all included neurofeedback sessions (the\n    Figure 5 set, n 7, 50, 42, 44, 50, 51), (b) all included sessions, head direction and\n    neurofeedback. Reproduced when, under one reading, rats 1, 2, 3, 5 and 6 have a positive\n    correlation with p < 0.01 and rat 4 a negative correlation with p < 0.05; partially reproduced\n    when at least four of rats 1, 2, 3, 5 and 6 do.\n- id: fig5b-target-increase-over-time\n  statement: Across all included neurofeedback sessions, target representation increased over time,\n    although the target switched every 3 days, individually in 4 of 6 rats and in a grouped\n    regression of z-scored values.\n  source: Results, Increased representation of the target location, paragraph 3; Figure 5B and 5C;\n    Table S1, Figures 5b and 5c\n  quote: the overall prevalence of the target representation increased over time (Figure 5,\n    individually significant in 4 of 6 animals\n  statistics:\n  - about: grouped analysis, all data\n    test: linear regression of Z scored values\n    p: 0.0001\n    n: 7, 50, 42, 44, 50 and 51 sessions for rats 1 to 6\n  data: elsewhere\n  where: Dryad doi:10.5061/dryad.dz08kps72 (version 7), real-time decoder output files\n  depends_on:\n  - fig4c-target-increase\n  criterion: Sessions are all included neurofeedback sessions (no reward selection; n from Table\n    S1). The measure is that of fig4c-target-increase for the session's target arm. Per rat,\n    scipy.stats.linregress of the measure on session; grouped, each rat's values z-scored and\n    pooled, then linregress on session (notebook cells 64 and 65). Open is the session variable;\n    the readings are (a) the session's position in the rat's neurofeedback series, counting\n    excluded sessions (1 to 18 or 1 to 54), (b) the index among the included sessions. Reproduced\n    when, under one reading, at least 4 rats have a positive slope with p < 0.05 and the grouped\n    slope is positive with p < 0.05; partially reproduced when the grouped slope holds and 2 or 3\n    rats do.\n- id: figs5b-over-time-no-trigger\n  statement: The increase of target representation over time holds with the tone-triggering\n    representations removed.\n  source: Results, Increased representation of the target location, paragraph 3; Figure S5B\n  quote: the overall prevalence of the target representation increased over time ...\n    tone-triggering representation removed\n  statistics:\n  - about: grouped analysis, tone-triggering representation removed\n    test: linear regression of Z scored values\n    p: 0.0002\n    n: 7, 50, 42, 44, 50 and 51 sessions for rats 1 to 6\n  data: elsewhere\n  where: Dryad doi:10.5061/dryad.dz08kps72 (version 7), real-time decoder output files\n  depends_on:\n  - fig5b-target-increase-over-time\n  - figs5a-target-increase-no-trigger\n  criterion: As fig5b-target-increase-over-time with the measure of\n    figs5a-target-increase-no-trigger, under the same session-variable readings. Reproduced when,\n    under one reading, the grouped slope is positive with p < 0.05.\n- id: fig5-arm-base-no-change-over-time\n  statement: Representation of the base of the target arm showed no consistent change over time,\n    with a significant increase in only one rat and no grouped trend.\n  source: Results, Increased representation of the target location, paragraph 3; Figure 5B and 5C\n  quote: By contrast, there was no consistent change in the representation of the base of the target\n    arm (Figure 5, significant increase in only one animal\n  statistics:\n  - about: grouped analysis\n    test: linear regression of Z scored values\n    p: 0.7\n    n: 7, 50, 42, 44, 50 and 51 sessions for rats 1 to 6\n  data: elsewhere\n  where: Dryad doi:10.5061/dryad.dz08kps72 (version 7), real-time decoder output files\n  depends_on:\n  - fig5b-target-increase-over-time\n  criterion: A claim of absence, judged on the paper's grouped test. As\n    fig5b-target-increase-over-time with the arm-base measure of fig4d-arm-base-no-increase.\n    Reproduced when the grouped regression of z-scored values has p >= 0.05 and at most one rat\n    has a significant positive slope; not reproduced when the grouped slope is significant. The\n    per-rat slopes and p, including significant decreases, are reported.\n- id: figs5d-opposite-arm-increase-over-time\n  statement: Representation of the opposite arm end also increased over time.\n  source: Results, Increased representation of the target location, paragraph 3; Figure S5D\n  quote: Finally, we noted that representation of the opposite arm end also increased over time\n    (Figure S5D\n  statistics:\n  - test: linear regression of Z scored values\n    p: 0.004\n    n: 7, 50, 42, 44, 50 and 51 sessions for rats 1 to 6\n  data: elsewhere\n  where: Dryad doi:10.5061/dryad.dz08kps72 (version 7), real-time decoder output files\n  depends_on:\n  - fig5b-target-increase-over-time\n  criterion: As fig5b-target-increase-over-time with the opposite-arm measure of\n    figs5c-opposite-arm-no-increase. Reproduced when, under one reading of the session variable,\n    the grouped slope is positive with p < 0.05.\n- id: fig6e-target-assemblies-at-detection\n  statement: At reward-triggering detections, target-representing cell assemblies were about 89 times\n    more active than at random times and about 26 times more active than non-target assemblies, in\n    every rat.\n  source: Results, Remote representations engage hippocampal cell assemblies, paragraphs 3 and 4;\n    Figure 6E; Table S1, Figure 6e\n  quote: these assemblies were about 89 times more active at detection times compared with random\n    times (Figures 6D and 6E, each rat p < 0.001, Mann-Whitney test) and were about 26 times more\n    active than non-target assemblies\n  statistics:\n  - about: target assemblies at detection against random times, each rat\n    test: Mann-Whitney\n    p: 0.001\n    p_relation: <\n    n: 8, 126, 81, 57, 85 and 53 target assemblies for rats 1 to 6\n  - about: target against non-target assemblies at detection, each rat\n    test: Mann-Whitney\n    p: 0.001\n    p_relation: <\n    n: 8, 126, 81, 57, 85 and 53 target and 72, 694, 527, 568, 578 and 769 non-target assemblies\n  data: with_inputs\n  depends_on:\n  - session-inclusion-decoding-quality\n  expected:\n  - quantity: Target assembly activity at detection relative to random times\n    value: 89\n    tolerance: 8.9\n  - quantity: Target assembly activity at detection relative to non-target assemblies\n    value: 26\n    tolerance: 2.6\n  criterion: Assemblies per neurofeedback session from the isolated single units (MountainSort4,\n    noise and multiunit clusters removed), by combined PCA and ICA (Lopes-dos-Santos et al. 2013),\n    with spike counts in 30 ms bins (STAR Methods, Cell assembly analysis). The code\n    (mcoulter_reward_assemblies.py, mcoulter_arm_end_assemblies.py) z-scores each unit, takes the\n    number of assemblies from a circular-shift null (100 shuffles, 99.5th percentile of the largest\n    eigenvalue) and FastICA patterns, and activation strength as in Lopes-dos-Santos (zero\n    diagonal); it sums 5 indicator bins and prints this as 10 ms, against 30 ms in the Methods, so\n    30 ms is the main reading and 10 ms a variant. Assemblies with maximum strength above 100 are\n    kept (Figure 6E legend). Open is how an assembly is classed as target; the readings are (a) its\n    activation strength during the exploration phase, binned by linearized position, peaks in the\n    target arm end, (b) its mean activation during exploration is higher in the target arm end than\n    in any other 25 cm segment, (c) as the code's mcoulter_arm_end_assemblies.py, assemblies built\n    from cells with more than 30 spikes in the target arm end. Activity at detection is the\n    strength in the bin containing each detection, averaged per assembly over detections; random\n    times are center-port feedback times drawn uniformly, as many as the detections. Per rat,\n    two-sided Mann-Whitney tests over assemblies. The fold change is open, (a) ratio of means over\n    assemblies pooled across rats, (b) ratio of medians, (c) mean of the per-rat ratios of means.\n    Reproduced when both comparisons have p < 0.001 in every rat with target higher and, under one\n    reading, both fold changes are within tolerance; partially reproduced when the tests hold but\n    no reading gives both fold changes.\n- id: fig6g-target-assemblies-outside-detection-random\n  statement: Outside rewarded detections, at times of target representation, target assemblies were\n    about 3.9 times more active than at random times, significantly in 5 of 6 rats and grouped.\n  source: Results, Remote representations engage hippocampal cell assemblies, paragraph 4; Figure\n    6G; Table S1, Figure 6g\n  quote: During these periods, target assemblies were about 3.9 times more active than at random\n    times\n  statistics:\n  - about: 5 of 6 rats\n    test: Mann-Whitney\n    p: 0.001\n    p_relation: <\n  - about: rat 1\n    test: Mann-Whitney\n    p: 0.16\n    n: 8 target assemblies\n  - about: grouped analysis of all rats\n    test: linear mixed effects model\n    p: 3.2e-27\n  data: with_inputs\n  depends_on:\n  - fig6e-target-assemblies-at-detection\n  expected:\n    quantity: Target assembly activity at target representation times relative to random times\n    value: 3.9\n    tolerance: 0.39\n  criterion: Assemblies, target class and random times as in fig6e-target-assemblies-at-detection.\n    Target representation times are center-port feedback bins with more than 40% of the posterior\n    in the target arm end (Figure 6G legend) outside detection events; the readings of \"outside\"\n    are (a) excluding the 30 ms that triggered each detection, (b) also excluding the 10 s after\n    each reward (the post-reward window of mcoulter_realtime_posterior_sum.py). Per rat, two-sided\n    Mann-Whitney over assemblies; grouped, the LME of the opening comment with condition (target\n    times against random times) as test variable and rat as group (notebook cell 103). Reproduced\n    when at least 5 rats have p < 0.001 with target times higher, the LME has p < 0.05, and under\n    one reading the fold change (readings of fig6e) is within tolerance.\n- id: fig6g-target-vs-nontarget-outside-detection\n  statement: At target representation times outside rewarded detections, target assemblies were\n    about 1.7 times more active than non-target assemblies, significantly in 4 of 6 rats (3 at p <\n    0.001, 1 at p = 0.005) and grouped.\n  source: Results, Remote representations engage hippocampal cell assemblies, paragraph 4; Figure\n    6G; Table S1, Figure 6g\n  quote: and were about 1.7 times more active than non-target assemblies at these same times\n  statistics:\n  - about: 3 of 6 rats\n    test: Mann-Whitney\n    p: 0.001\n    p_relation: <\n  - about: 1 rat\n    test: Mann-Whitney\n    p: 0.005\n  - about: 2 rats\n    test: Mann-Whitney\n    p: 0.4\n  - about: 2 rats, second\n    test: Mann-Whitney\n    p: 0.45\n  - about: grouped analysis\n    test: linear mixed effects model\n    p: 9.5e-18\n  data: with_inputs\n  depends_on:\n  - fig6g-target-assemblies-outside-detection-random\n  expected:\n    quantity: Target relative to non-target assembly activity at target representation times\n    value: 1.7\n    tolerance: 0.17\n  criterion: As fig6g-target-assemblies-outside-detection-random, comparing target with non-target\n    assemblies at the same times. Reproduced when at least 4 rats have p < 0.01 with target higher,\n    the LME has p < 0.05, and under one reading the fold change is within tolerance; partially\n    reproduced when the LME holds but fewer rats do.\n- id: figs6bc-active-cells\n  statement: Detection events engaged several neurons, an average of 1.8 to 8.1 highly weighted\n    target-assembly cells active just before each detection across rats, 10 to 14% of the\n    high-weight cells.\n  source: Results, Remote representations engage hippocampal cell assemblies, paragraph 5; Figure S6B\n    and S6C\n  quote: Across all sessions, rats had an average of 1.8–8.1 cells active immediately preceding each\n    detection event, ... which corresponded to 10%–14% of high-weight cells\n  data: with_inputs\n  depends_on:\n  - fig6e-target-assemblies-at-detection\n  expected:\n  - quantity: Mean active high-weight cells per detection, per rat\n    value: 4.95\n    tolerance: 3.33\n  - quantity: Fraction of high-weight cells active per detection, per rat\n    value: 0.12\n    tolerance: 0.034\n  criterion: High-weight cells are cells whose weight in a target assembly is more than 5 s.d. above\n    the mean weight (Figure S6B legend); a cell is active if it spikes within 100 ms before the\n    detection. Detections are the reward times (n 322, 2999, 1970, 1737, 2037 and 1176). Open is\n    whether the mean and s.d. are over (a) the weights of that assembly, (b) all weights of the\n    session's assemblies; and whether a cell in several target assemblies counts once (main) or per\n    assembly. The ranges widened by 10% of each bound are 1.62 to 8.91 cells and 9% to 15.4%.\n    Reproduced when, under one reading, every rat's mean and fraction lie in them.\n- id: figs6ef-similarity-to-exploration\n  statement: Spiking patterns at remote representation times were more similar to patterns during\n    exploration than patterns at random times, by cosine distance and by PCA explained variance, in\n    each rat.\n  source: Results, Remote representations engage hippocampal cell assemblies, paragraph 5; Figure S6E\n    and S6F\n  quote: two additional analyses examining cosine distances and explained variances indicated that\n    spiking patterns during remote representation times were more similar to patterns seen during\n    actual exploration than to patterns seen at random times\n  statistics:\n  - about: cosine distance, remote representation against random times, each rat\n    test: Mann-Whitney\n    p: 0.0001\n    p_relation: <\n  - about: explained variance, remote representation against random times, each rat\n    test: Mann-Whitney\n    p: 0.0001\n    p_relation: <\n  data: with_inputs\n  depends_on:\n  - session-inclusion-decoding-quality\n  criterion: From the Figure S6E and S6F legends. Cells with more than 50 spikes and mean rate below\n    7 Hz; population vectors of spike counts in 50 ms windows. (E) cosine distance between each\n    exploration visit to the target location and remote representations, and between exploration\n    visits and random times. (F) a PCA fit to the 12 exploration visits to the target location,\n    and the variance it explains in the 50 ms vectors of reward-triggering representations and of\n    random feedback times. Open are the window of an exploration visit (read as the time the rat\n    spends in the 25 cm target arm end on each visit) and where the 50 ms is placed (read as ending\n    at the detection). Reproduced when in every rat the cosine distance is smaller and the explained\n    variance higher for remote representations than for random times, each with two-sided\n    Mann-Whitney p < 0.0001.\n- id: figs6d-no-consistent-remapping\n  statement: There was no consistent remapping of activity from the target location to the center\n    port after high-reward sessions; one rat (rat 4) showed a significantly larger increase for the\n    center port.\n  source: Results, Remote representations engage hippocampal cell assemblies, paragraph 6; Figure S6D\n  quote: This was not consistently true across animals, but there was some evidence for remapping in\n    one of the six animals\n  statistics:\n  - about: rat 4, center port against target region change\n    test: Mann-Whitney\n    p: 0.003\n  data: with_inputs\n  depends_on:\n  - fig4c-target-increase\n  criterion: From the Figure S6D legend, after each high-reward session (more than 90% of possible\n    rewards), the change in representation of the center reward port and of the target region in\n    the next session. The measure is open; the readings are (a) the change in the decoder's\n    exploration-phase encoding, read as the fraction of single units with place-field peaks at the\n    center port and in the target arm end, (b) the change in the per-session fraction of\n    center-port time with posterior above 0.4 at the center port and in the target arm end, as in\n    fig4c-target-increase. Reproduced when, under one reading, the direction of the difference\n    (center port against target) is not the same in all six rats and at most one rat has a\n    two-sided Mann-Whitney p < 0.05.\n- id: fig7b-swr-fraction\n  statement: Remote representations occurred mainly during stillness (head speed below 4 cm/s) but\n    outside SWRs; only 6 to 11% of remote representations were associated with SWRs.\n  source: Results, Brain state during remote representation events, paragraph 2; Figure 7A and 7B\n  quote: Strikingly, remote representations were primarily expressed during stillness (head speed < 4\n    cm/s) but outside of clearly identifiable SWR events ... only 6%–11% of remote representations\n    were associated with SWRs\n  data: with_inputs\n  depends_on:\n  - figs4b-target-arm-majority\n  expected:\n    quantity: Fraction of remote representations associated with SWRs, per rat\n    value: 0.085\n    tolerance: 0.033\n  criterion: Remote representations are the target representation bins of\n    figs4b-target-arm-majority in neurofeedback sessions (Figure 7B legend). Brain state per 6 ms\n    bin, as mcoulter_realtime_lfp_posterior_sum.py does it, SWR when the bin overlaps an SWR\n    interval, otherwise movement when the head speed (Gaussian-smoothed, sigma 2 samples) exceeds 4\n    cm/s and stillness below it. SWRs are detected by \"previously described methods\" (ref. 25,\n    Gillespie et al. 2021); the code uses Spyglass RippleTimesV1 with the Kay consensus detector,\n    whose stored parameters are not in the repository, so the parameters of ref. 25 are used. Open\n    is the session set; readings (a) the neurofeedback sessions with Figure 7 data (Table S1, Figure\n    7c), (b) these pooled with head direction sessions. \"Primarily\" is read as (a) stillness outside\n    SWRs above 50% of remote representations, (b) the largest of the three states. The range 6 to\n    11% widened by 10% of each bound is 5.4% to 12.1%. Reproduced when, under one reading, every\n    rat's SWR fraction lies in it and stillness outside SWRs is primary.\n- id: fig7b-neurofeedback-vs-head-direction-state\n  statement: Compared with head direction feedback, remote representations during neurofeedback\n    occurred more often during movement and less often during SWRs, in each rat.\n  source: Results, Brain state during remote representation events, paragraph 3; Figure 7B\n  quote: During neurofeedback, remote representations were more likely to occur during movement and\n    less likely to occur during SWRs as compared with head direction feedback\n  statistics:\n  - about: movement fraction and SWR fraction, each rat\n    test: chi-squared test and post hoc Z test of proportions\n    p: 0.001\n    p_relation: <\n  data: with_inputs\n  depends_on:\n  - fig7b-swr-fraction\n  criterion: Brain states as in fig7b-swr-fraction, for remote representation bins during head\n    direction and neurofeedback sessions. Per rat, a chi-squared test of the 2 by 3 table (session\n    type by movement, stillness, SWR) of bin counts, then two-proportion z tests of the movement\n    fraction and of the SWR fraction; the code for these tests is not in the repository. Open is\n    the counting unit; readings (a) 6 ms bins, (b) events, runs of consecutive bins. Reproduced\n    when, under one reading, in every rat the chi-squared test and both z tests have p < 0.001 with\n    neurofeedback higher for movement and lower for SWR.\n- id: fig7b-swr-vs-random\n  statement: Within neurofeedback sessions, SWRs were more frequent at remote representation times\n    than at random center-port times in 5 of 6 rats.\n  source: Results, Brain state during remote representation events, paragraph 4; Figure 7B\n  quote: SWRs were more frequent during times of remote representation compared with random times in\n    5 of 6 rats\n  statistics:\n  - about: SWR fraction, each of 5 rats\n    test: chi-squared test and post hoc Z test of proportions\n    p: 0.001\n    p_relation: <\n  data: with_inputs\n  depends_on:\n  - fig7b-swr-fraction\n  criterion: Brain states as in fig7b-swr-fraction; random times are center-port feedback bins drawn\n    at random, as many as the remote representation bins (np.random.choice in\n    mcoulter_realtime_lfp_posterior_sum.py). Tests and counting-unit readings as in\n    fig7b-neurofeedback-vs-head-direction-state. Reproduced when, under one reading, at least 5 rats\n    have a higher SWR fraction at remote representation times with p < 0.001.\n- id: fig7c-non-swr-target-increase\n  statement: Target representations outside SWRs consistently increased with neurofeedback compared\n    with head direction feedback, in 5 of 6 rats and grouped.\n  source: Results, Brain state during remote representation events, paragraph 2; Figure 7C; Table S1,\n    Figure 7c\n  quote: Furthermore, target representations outside SWRs consistently increased in prevalence with\n    neurofeedback\n  statistics:\n  - about: grouped analysis\n    test: linear mixed effects model\n    p: 1.3e-11\n    n: 141 sessions of 6 rats\n  - about: rat 1\n    test: Mann-Whitney\n    p: 0.012\n    n: 8 head direction and 3 neurofeedback sessions\n  - about: rat 2\n    test: Mann-Whitney\n    p: 0.0079\n    n: 12 head direction and 33 neurofeedback sessions\n  - about: rat 3\n    test: Mann-Whitney\n    p: 0.00079\n    n: 10 head direction and 15 neurofeedback sessions\n  - about: rat 4\n    test: Mann-Whitney\n    p: 5.5e-5\n    n: 10 head direction and 16 neurofeedback sessions\n  - about: rat 5\n    test: Mann-Whitney\n    p: 0.023\n    n: 11 head direction and 9 neurofeedback sessions\n  - about: rat 6\n    test: Mann-Whitney\n    p: 0.36\n    n: 9 head direction and 5 neurofeedback sessions\n  data: with_inputs\n  depends_on:\n  - fig4c-target-increase\n  - fig7b-swr-fraction\n  criterion: Sessions as in fig4c-target-increase less those missing for Figure 7 (STAR Methods, Data\n    inclusion; Table S1 n). The measure is that of fig4c-target-increase restricted to bins not\n    associated with SWRs (SWR assignment of fig7b-swr-fraction); the readings of its denominator are\n    (a) all center-port feedback bins, (b) the center-port bins outside SWRs. Per rat, two-sided\n    Mann-Whitney; grouped, the LME of the opening comment (notebook cell 138). Reproduced when,\n    under one reading, at least 5 rats have neurofeedback higher with p < 0.05 and the LME has p <\n    0.05 with neurofeedback higher.\n- id: fig7c-swr-target-no-consistent-increase\n  statement: Target representations during SWRs did not consistently increase with neurofeedback,\n    significant in only 1 of 6 rats and not grouped.\n  source: Results, Brain state during remote representation events, paragraph 2; Figure 7C; Table S1,\n    Figure 7c\n  quote: while representations associated with SWRs did not consistently increase across animals\n  statistics:\n  - about: grouped analysis\n    test: linear mixed effects model\n    p: 0.056\n    n: 141 sessions of 6 rats\n  - about: rat 2, the one significant rat\n    test: Mann-Whitney\n    p: 0.0011\n  data: with_inputs\n  depends_on:\n  - fig7c-non-swr-target-increase\n  criterion: A claim of absence, judged on the paper's grouped test. As\n    fig7c-non-swr-target-increase with the bins associated with SWRs (denominator readings (a) all\n    center-port bins, (b) center-port SWR bins). Reproduced when the LME has p >= 0.05 and at most\n    one rat has p < 0.05 with neurofeedback higher; not reproduced when the LME finds a significant\n    increase. Each rat's p and the effect are reported.\n- id: figs7a-theta-phase\n  statement: Remote representations during movement were locked to theta phase in every rat, and in 5\n    of 6 rats they were more prevalent in late theta phases.\n  source: Results, Brain state during remote representation events, paragraph 2; Figure S7A\n  quote: These representations were associated with specific theta phases in all rats ... and in 5 of\n    6 rats, remote representations were more prevalent in late theta phases.\n  statistics:\n  - about: each rat\n    test: Rayleigh test\n    p: 0.0001\n    p_relation: <\n    n: 13822, 42027, 21747, 76860, 37556 and 71226 representation times for rats 1 to 6\n  data: with_inputs\n  depends_on:\n  - fig7b-swr-fraction\n  criterion: Remote representation bins during movement (speed above 4 cm/s), theta phase from one\n    tetrode in stratum oriens (STAR Methods, LFP analysis), band 5 to 11 Hz and Hilbert phase as in\n    the code (Spyglass LFPBandV1 \"Theta 5-11 Hz\", compute_signal_phase). Rayleigh test per rat.\n    Figure S7A bins phase into 10 equal bins and builds a null from random movement bins of the\n    same number, 1000 times, 95% interval (mcoulter_theta_phase_shuffles.py). Open is what \"late\"\n    phases are, as the paper gives no phase reference; the readings are (a) the bins exceeding the\n    null's 95% interval lie in the half cycle after the theta trough, (b) the circular mean phase\n    lies in that half cycle, with the trough located from the LFP itself (minimum of the band-passed\n    signal). Reproduced when every rat has Rayleigh p < 0.0001 and, under one reading, at least 5\n    rats have late-phase preference.\n- id: figs7b-no-lfp-signature\n  statement: No specific LFP signature was found for remote representations during stillness outside\n    SWRs, although some rats had increased power above 100 Hz.\n  source: Results, Brain state during remote representation events, paragraph 5; Figure S7B\n  quote: We were not able to identify such a signature, although some rats had increased power >100\n    Hz, potentially reflecting high gamma activity or spiking (Figure S7B).\n  data: with_inputs\n  depends_on:\n  - fig7b-swr-fraction\n  criterion: Spectrograms of 1 s around remote representation times during stillness outside SWRs,\n    in 1 s non-overlapping bins (Figure S7B legend, n 1071, 16032, 13605, 17164, 15025, 14241), from\n    a tetrode in the cell layer (referenced) and one above it (unreferenced), as change from random\n    center-port times. The paper gives no test; the reading is a z-scored power change outside the\n    95% interval of random times. Reproduced when no frequency band below 100 Hz shows a power\n    change in the same direction in all six rats, and at least one rat shows increased power above\n    100 Hz.\n- id: figs7c-multiunit-peak\n  statement: Multiunit spiking peaked at the time of remote representations.\n  source: Results, Brain state during remote representation events, paragraph 5; Figure S7C\n  quote: Indeed, and as expected, multiunit spiking activity peaked at the time of remote\n    representations (Figure S7C).\n  data: with_inputs\n  depends_on:\n  - fig7b-swr-fraction\n  criterion: Mean multiunit spike rate (all spikes above threshold on the CA1 tetrodes) in 1 s around\n    remote representation times in 1 s non-overlapping bins (Figure S7C legend, n 1840, 18211,\n    22150, 21021, 23581, 23092), against random times, with 95% confidence intervals of the mean.\n    The rate bin is not given; 10 ms is used as a standard choice. Reproduced when, in every rat,\n    the rate peaks within 30 ms of the representation time and the peak lies above the random\n    times' 95% interval.\n- id: figs7d-jump-trajectory-state\n  statement: Jump and trajectory representations both occurred during movement, stillness and SWRs,\n    with no consistent difference in brain state between them across rats.\n  source: Results, Brain state during remote representation events, paragraph 5; Figure S7D\n  quote: We found both jump and trajectory representations across moving, still, and SWR periods with\n    no consistent effects of prevalence across animals (Figure S7D).\n  data: with_inputs\n  depends_on:\n  - fig3b-trajectory-fraction\n  - fig7b-swr-fraction\n  criterion: Events classed as jump (confined to the target location, with or without the center port)\n    or trajectory (significant linear regression covering at least 35 cm in the target arm) as in\n    fig3b-jump-fraction and fig3b-trajectory-fraction (Figure S7D legend), each assigned a brain\n    state as in fig7b-swr-fraction at its detection time. The paper gives no test; per rat, a\n    chi-squared test of class by state. Reproduced when each class occurs in each state, and no\n    state is more frequent for one class than the other with p < 0.05 in the same direction in all\n    six rats.\n"
}
```

Result: not kept, because it reads the paper's text.

**Agent**

I'll fix the range tolerances so each one matches the range widened by 10% of each bound, then run the checker.

**Agent calls Bash**

```bash
python - <<'EOF'
import re
p='claims/coulter-2025.yaml'
s=open(p).read()
rep=[
("    value: 0.945\n    tolerance: 0.054","    value: 0.945\n    tolerance: 0.135"),
("    value: 0.70\n    tolerance: 0.125","    value: 0.705\n    tolerance: 0.12"),
("    value: 0.025\n    tolerance: 0.0175","    value: 0.0265\n    tolerance: 0.0175"),
("    value: 0.69\n    tolerance: 0.129","    value: 0.699\n    tolerance: 0.159"),
("    value: 0.13\n    tolerance: 0.079","    value: 0.136\n    tolerance: 0.073"),
("    value: 0.175\n    tolerance: 0.067","    value: 0.1795\n    tolerance: 0.0625"),
("    value: 4.95\n    tolerance: 3.33","    value: 5.265\n    tolerance: 3.645"),
("    value: 0.12\n    tolerance: 0.034","    value: 0.122\n    tolerance: 0.032"),
("    value: 0.085\n    tolerance: 0.033","    value: 0.0875\n    tolerance: 0.0335"),
]
for a,b in rep:
    assert s.count(a)==1,a
    s=s.replace(a,b)
open(p,'w').write(s)
EOF
grep -n "—\|rather" claims/coulter-2025.yaml; python -c "
import yaml;d=yaml.safe_load(open('claims/coulter-2025.yaml'))
for c in d['claims']:
  for k,v in c.items():
    if isinstance(v,str) and ': ' in v: print(c['id'],k)
print(len(d['claims']))"; python tools/claims_check.py claims/coulter-2025.yaml paper/10.1016-j.neuron.2024.12.023.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/coulter-2025.yaml",
 "old_string": "  - quantity: Sessions per rat (head direction, neurofeedback), rats 1 to 6, as Table S1\n    value: 148",
 "new_string": "  - quantity: Sessions in the comparison, all rats and both session types (Table S1)\n    value: 148"
}
```

```
The file claims/coulter-2025.yaml has been updated successfully.
```

**Agent calls Bash**

```bash
python tools/claims_check.py claims/coulter-2025.yaml paper/10.1016-j.neuron.2024.12.023.txt; git status --short claims/
```

Result: not kept, because it reads the paper's text.

**Agent**

I wrote `claims/coulter-2025.yaml` with 35 claims. Every quote passes the checker. Three p-values are flagged because the text prints them with a garbled minus sign (3.9e-11, 3.6e-11 and 1.3e-11, lines 302 and 526); I read them there and they are recorded correctly.

**Text read:** the version of record (Neuron 113:949–961, CC BY), with the STAR Methods and the full supplement (Figures S1 to S7 legends and Table S1). Nothing the claims need is missing from the text.

**Code read:** LorenFrankLab/hippocampus_content_neurofeedback, tag v0.0.4, commit b27655c (Zenodo 10.5281/zenodo.14522610). It contains the scripts that compute the per-session numbers, and one notebook that runs the tests from summary files on Dryad. The code fixes these details:
- the position bins of the arm ends, arm bases and box;
- the 17 cm limit to the center port and the 0.4 posterior threshold;
- how the tone-triggering bins are removed;
- the way the "2-fold" figure is normalized;
- the mixed-model formula, the two-sided Mann-Whitney test, and the regression on per-rat z-scored values;
- the speed smoothing, how bins are assigned to SWRs, and the 5–11 Hz theta band;
- the rat names and the target arm on each day.

**Where the data are:** the decoded positions are the real-time decoder's output, which the paper put on Dryad (doi:10.5061/dryad.dz08kps72), not on DANDI.
- **On the dataset (2 claims):** the reward counts (Figure 2, Figure S2D).
- **Elsewhere, on Dryad (19 claims):** Figures 1, 3, 4 and 5, Figures S1 to S5, and the reward-to-representation correlation.
- **With inputs (14 claims):** Figures 6 and 7, S6 and S7. These combine the decoder output with spikes, LFP and position from the raw recordings.

**Counts:** 35 claims; all 35 have quotes, 23 have statistics (47 values), 35 have criteria, and 17 have expected values.

**Details the paper and code leave open, with the readings named:**
- **Session quality rule:** what "running outward" means (speed above 4 cm/s, or any outward bin) and which arm is meant (the target arm, or each arm in turn).
- **Figure 3 event classes** (their code isn't in the repository):
  - whether arm-base mass is counted per bin or summed over the 90 ms window;
  - which three bins make up the 15 cm arm base;
  - whether the 1–4% counts long trajectories only, or medium and long together;
  - how the trajectory regression is done (posterior-maximum position, or posterior-weighted).
- **Figure 3C/D:** the threshold for "representing" a 5 cm bin (posterior above 0.2, above 0.4, or that bin being the maximum).
- **Figure S4A:** what counts as a "high-confidence representation" (summed over the arm end, or a single bin).
- **Reward-representation correlation:** Pearson or Spearman, and over neurofeedback sessions only or all sessions.
- **Figure 5:** the session index (the position in the full series, or among included sessions only).
- **Figure 6:**
  - assembly bins: 30 ms in the Methods, while the code's binning is labelled 10 ms (kept as a variant);
  - how an assembly is classed as target (three readings);
  - how the fold changes are taken (ratio of means, ratio of medians, or mean of per-rat ratios);
  - what "outside detection" excludes (the 30 ms window only, or also the 10 s after each reward);
  - how the mean and SD behind the high-weight cutoff are computed (Figure S6B);
  - the exploration-visit window and the 50 ms placement (Figure S6E/F).
- **Figure S6D:** the remapping measure.
- **Figure 7:**
  - which sessions count (neurofeedback only, or pooled with head direction);
  - "primarily" (more than 50%, or the largest state);
  - whether the chi-squared tests count bins or events;
  - the denominator for the SWR and non-SWR measures (all center-port bins, or only the SWR or non-SWR bins).
- **Figure S7:**
  - the "late" theta phase reference;
  - for S7B, S7C and S7D the paper gives no test, so I set thresholds myself and say so in each criterion.

**Missing from the paper and its code:**
- The SWR detection parameters: the Methods only cite ref. 25, and the code's stored parameters aren't in the repository. The author has to take them from ref. 25.
- The code for the Figure 3 event classification, the Figure 6 per-assembly summaries and the chi-squared tests.
- The notebook's reward-count lists for rats 3 and 4 are identical, which looks like a copying error, so rat 3's list is not used for comparison.

## End of run

41 turns, 10 minutes, $3.70 at API prices, result: success.
