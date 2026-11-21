# wang-2025 · claims · run 44781477597

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  grep -n "^#" docs/protocol.md | head -50; ls paper/ | grep -i wang; ls claims | head; wc -l claims/fouke-2025.yaml
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  sed -n 1,200p docs/protocol.md; ls paper/; ls paper | grep -i wang
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  f=paper/10.1038-s41593-025-02114-x.txt; wc -l $f; head -30 $f; grep -n -i "supplement\|^#\|methods" $f | head -60; cat claims/fouke-2025.yaml | head -120; cat papers/datasets/wang-2025.yaml
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  f=paper/10.1038-s41593-025-02114-x.txt; awk '{print NR": "length($0)": "substr($0,1,100)}' $f | awk -F': ' '$2>200'
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  f=paper/10.1038-s41593-025-02114-x.txt; sed -n 242p $f | fold -w 2000 -s; sed -n 243,375p $f
```

Result: not kept, because it reads the paper's text.

**Agent**

I'm reading the full paper text now (it is one long line; I'm splitting it into readable chunks).

**Agent calls Bash**

```bash
cd  f=paper/10.1038-s41593-025-02114-x.txt; mkdir -p $TMPDIR/w; sed -n 242p $f | fold -w 3000 -s > $TMPDIR/w/body.txt; wc -l $TMPDIR/w/body.txt; sed -n 243,375p $f | head -c 3000
```

Result: not kept, because it reads the paper's text.

**Agent**

Supplement is present. Reading the main body.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/w/body.txt"
}
```

```
1	Download PDF Subjects Computational neuroscience Motor control Abstract Movement-related activity has been detected across much of the brain, including sensory and motor regions. However, much remains unknown regarding the distribution of movement-related activity across brain regions, and how this activity relates to neural computation. Here we analyzed movement-related activity in brain-wide recordings of more than 50,000 neurons in mice performing a decision-making task. We used multiple machine learning methods to predict neural activity from videography and found that movement-related signals differed across areas, with stronger movement signals close to the motor periphery and in motor-associated subregions. Delineating activity that predicts or follows movement revealed fine-scale structure of sensory and motor encoding across and within brain areas. Through single-trial video-based predictions of behavior, we identified activity modulation by uninstructed movements and their impact on choice-related activity analysis. Our work provides a map of movement encoding across the brain and approaches for linking neural activity, uninstructed movements and decision-making. Similar content being viewed by others A brain-wide map of neural activity during complex behaviour Article Open access 03 September 2025 How distributed is the brain-wide network that is recruited for cognition? Article 04 December 2025 Sensory expectations shape neural population dynamics in motor circuits Article 29 October 2025 Main A standard view of the function of the nervous system is the translation of sensory inputs into action 1 , 2 , 3 . According to this view, the brain is parcellated into sensory and motor areas, with association areas in between 4 . On the other hand, decades of neurophysiological recordings have found activity related to movement throughout sensory and motor regions of the brain. For example, neurons in visual cortical areas are modulated by eye movement in prima
[... 19 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/w/body.txt",
 "offset": 21
}
```

```
21	Fig. 6e , AUCs from the jaw and the nose markers were used as features, and mouse identity was used as cluster labels. We note that we used only sessions where the trial type was predictable from either jaw or nose (AUC equal to or higher than 0.65) and only mice that had two or more of such predictable sessions. Testing against spatial discontinuity with nearest-neighbor explained variance difference distribution To test whether spatially closer neurons have smaller difference in their explained variance than expected by chance within thalamus (Fig. 3e ), we first identified neurons within each nucleus and calculated the cumulative distribution function for the explained variance difference between nearest neighbors. As a control we randomly shuffled the neurons’ explained variance values within each nucleus separately and calculated the cumulative distribution function for the explained variance difference in the shuffled sample. We repeated the shuffle 1,000 times to establish a null-distribution and bootstrap P value. Test against spatial uniformity To test against spatial uniformity (Figs. 3 and 7 and Extended Data Fig. 9 ) of a given scalar statistic (explained variance, single-neuron AUC) given the fixed sampling provided by the CCF coordinates, we split the brain into cubic voxels (0.2 mm cubed for Fig. 3 and 0.5 mm cubed for Fig. 7 and Extended Data Fig. 9 , but the results do not depend on the specific choice of this size) and grouped neurons based on these voxels. We then calculated an F -statistic for this grouping using one-way F -test. As a control we randomly shuffled the scalar statistics of interest (explained variance, single-neuron AUC) across neurons while keeping the CCF coordinates fixed; we used the same cubic voxels as before to group the shuffled neurons and calculated an F -statistic for this shuffle control using one-way F -test. We repeated the shuffle 10,000 times to establish a null-distribution and bootstrap P value. Data pooling Th
[... 10 more lines not kept]
```

**Agent**

Main text, Methods and Extended Data legends are complete. Now the rest of the supplement, the example file and the checker.

**Agent calls Bash**

```bash
cd  f=paper/10.1038-s41593-025-02114-x.txt; sed -n 243,375p $f | tail -n +100 | tr '\n' ' ' ; echo; echo ----; cat claims/fouke-2025.yaml
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  sed -n 1,60p tools/claims_check.py; ls docs; grep -l "readings" claims/*.yaml | head -3; cat papers/datasets/wang-2025.yaml 2>/dev/null; grep -n -A3 "wang-2025" papers/keys.yaml
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

[... 71 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python -c "import json;d=json.load(open('schemas/claims.schema.json'));print(json.dumps(d,indent=1))" | head -200
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
[... 180 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python -c "import json;d=json.load(open('schemas/claims.schema.json'));print(json.dumps(d,indent=1))" | sed -n 200,400p; head -40 claims/armstrong-2026.yaml
```

```
"then": {
       "required": [
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
[... 174 more lines not kept]
```

**Agent**

Now the paper's code (druckmann-lab/MapVideoAnalysis).

**Agent calls Bash**

```bash
cd $TMPDIR && git clone -q https://github.com/druckmann-lab/MapVideoAnalysis.git 2>&1 | tail -2; cd MapVideoAnalysis && git log -1 --format='%H %ad' && find . -type f -not -path './.git/*' | head -100 && cat README* | head -80
```

```
7d276243db16db5af6da68a48de7720ef77007c2 Tue Nov 10 15:02:08 2026 -0800
./Archive/play_around_with_old_data.ipynb
./Archive/subregion_summary_plot.ipynb
./Archive/getting_started.ipynb
./Archive/medulla_plots.py
./Archive/midbrain_subregions.ipynb
./Archive/striatum_plots.py
./Archive/thalamus_subregions.ipynb
./Archive/align_test_train_folds.ipynb
./Archive/epoch_comparisons.ipynb
./Archive/striatum_subregions.ipynb
./Archive/plot_for_nuo.ipynb
./Archive/download_allen_svg.py
./Archive/redo_auc_analysis.ipynb
./Archive/functions.py
./Archive/egde_effects_in_timeshift_analysis.ipynb
./Archive/read_firing_rates.ipynb
./Archive/other_cortex.ipynb
./Archive/single_animal_comparisons.ipynb
./Archive/replot_old_auc_analysis_data.ipynb
[... 161 more lines not kept]
```

**Agent**

Fetching the dataset's title and description from DANDI (metadata only).

**Agent calls Bash**

```bash
curl -s https://api.dandiarchive.org/api/dandisets/000363/versions/draft/info/ | python -c "import json,sys;d=json.load(sys.stdin);m=d.get('metadata',d);print(m.get('name'));print(m.get('description'));print([v.get('identifier') for v in []])"; curl -s "https://api.dandiarchive.org/api/dandisets/000363/versions/" | python -c "import json,sys;d=json.load(sys.stdin);print([r['version'] for r in d['results']])"
```

Result: the fetched text is not kept.

**Agent**

Reading the code for method details now.

**Agent calls Bash**

```bash
cd $TMPDIR/MapVideoAnalysis; wc -l VideoAnalysisUtils/*.py Sherlock/*.py | sort -n | tail -40
```

```
41 VideoAnalysisUtils/plot_style.py
    45 Sherlock/collect_e2e_single_neuron_data.py
    54 Sherlock/get_large_diff_by_avg_method_neurons.py
    59 Sherlock/medulla_population_decoding.py
    64 Sherlock/collect_trial_motor_type_aucs.py
    75 Sherlock/collect_delay_fr_video_predictions_groups.py
    75 Sherlock/collect_trial_type_labels_for_fig6.py
    80 Sherlock/collect_combined_methods_r2.py
    81 Sherlock/collect_delay_choice_selectivity_video_pred_sub.py
    82 Sherlock/align_test_train_folds_for_end_to_end_training.py
    82 Sherlock/collect_single_neuron_data.py
    90 Sherlock/generate_trial_fold_inds.py
   100 Sherlock/calculate_delay_choice_selectivity_with_video_pred_subtraction.py
   101 Sherlock/calculate_delay_fr_video_prediction_trial_types.py
   108 Sherlock/align_markers.py
   113 Sherlock/align_embed_vecs.py
   113 Sherlock/collect_r2_embed_timeshift_keepfolds.py
   114 Sherlock/calculate_trial_motor_type_aucs.py
   115 Sherlock/generate_5fold_cv_indices.py
   115 Sherlock/generate_single_train_test_split.py
[... 21 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/MapVideoAnalysis; cat VideoAnalysisUtils/functions_for_r2.py
```

```
import numpy as np
import os
from sklearn.model_selection import StratifiedKFold
from sklearn.linear_model import RidgeCV
from sklearn.metrics import r2_score

def get_file_paths(directory):
    """
    Get a list of full file paths in a given directory.

    Parameters:
    directory : str
        The path to the directory.

    Returns:
    list
        List of full file paths.
    """
    directory = os.path.abspath(directory)
    file_paths = []
[... 564 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/MapVideoAnalysis/Sherlock; cat calculate_r2_embed_single_split.py; sed -n 1,200p combine_methods_r2.py
```

```
'''
This script is used to predict firing rates from embedding vectors 
using a single train/test split that matched what is used for the
end-to-end method. 

This is to make the fairest comparison between the two methods for 
Fig 2.

2024.06.25. Balint
'''

import numpy as np
from sklearn.linear_model import RidgeCV
import os
import pickle
import sys
import time
import local_env
from VideoAnalysisUtils import functions_for_r2 as func

[... 321 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/MapVideoAnalysis/Sherlock; cat generate_single_train_test_split.py | sed -n 1,115p
```

```
import numpy as np
from sklearn.linear_model import RidgeCV
import os
from sklearn.model_selection import StratifiedKFold
from sklearn.model_selection import StratifiedShuffleSplit
from sklearn.linear_model import RidgeCV
from sklearn.metrics import r2_score
import pickle
import sys
import time
import local_env
from VideoAnalysisUtils import functions_for_r2 as func
start_time = time.time()

cv = 1
test_size = 64
random_seed = 0

aligned_embed_data_folder = '/oak/stanford/groups/shauld/kurgyis/data/Map_aligned_embed_vecs/'
save_folder = '/oak/stanford/groups/shauld/kurgyis/data/MAP_train_test_split_inds/'
[... 95 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/MapVideoAnalysis/Notebooks; cat > $TMPDIR/nbsrc.py <<'EOF'
import json,sys
nb=json.load(open(sys.argv[1]))
for i,c in enumerate(nb['cells']):
    if c['cell_type']=='code':
        print(f"# --- cell {i}")
        print(''.join(c['source']))
        for o in c.get('outputs',[]):
            if o.get('output_type')=='stream':
                t=''.join(o['text']); print('# OUT:', t[:1500])
            elif 'data' in o and 'text/plain' in o['data']:
                print('# OUT:', ''.join(o['data']['text/plain'])[:800])
EOF
python $TMPDIR/nbsrc.py fig2_plot.ipynb
```

```
# --- cell 1
%load_ext autoreload
%autoreload 2

import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import pickle
from scipy import stats

import local_env
import VideoAnalysisUtils.functions as func
import VideoAnalysisUtils.plotting_utils as plt_utils
import VideoAnalysisUtils.plot_style as style
# OUT: [removed: a home directory path]/Research/MapVideoAnalysis/python38_venv/lib/python3.8/site-packages/pandas/compat/__init__.py:120: UserWarning: Could not import the lzma module. Your installed Python is incomplete. Attempting to use lzma compression will result in a RuntimeError.
  warnings.warn(msg)

# --- cell 2
figfolder = '../figs/manuscript_drafts/'
[... 389 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/MapVideoAnalysis/VideoAnalysisUtils; grep -n "def \|^class " plotting_utils.py | head -150; grep -n "def " functions.py
```

```
10:def load_anatomy_tif(tif_path):
34:def get_2D_grid_averages_with_count(best_times, ccf_coords, voxel_size = 300, projection_axis = 0):
88:def get_2D_count_fractions(best_times, ccf_coords, subset_inds, voxel_size = 300, projection_axis = 0):
129:def plot_best_times_2d_heatmap(ax, best_times, ccf_coords, 
226:class Figure2():
228:    def __init__(self):
246:    def load_data(self, datafolder = '../data/', 
273:    def plot_single_neuron_example(self, ax, id = 1, xlim = [-3,1.2], print_epochs = False, add_legend = False, legend_anchor = (.02, 1.4)):
308:    def _calc_mean_and_sem(self, array):
313:    def get_barplot_statistics(self, fr_threshold = 2, r2_threshold = 0.01, fr_filter = 'epoch', epoch = 'response', stat_method = 'embedding'):
375:    def plot_barplot_with_sem(self, ax, 
453:    def plot_methods_scatter(self, ax, x_method = 'marker', y_method = 'embed',  fr_filter = 'avg', epoch = 'response', fr_threshold = 2, r2_threshold = 0.005):
472:    def get_method_comparison_stats(self, fr_filter = 'avg', epoch = 'response', fr_threshold = 2, r2_threshold = 0.005):
501:    def plot_anatomy_slice(self, ax,
520:    def plot_saggital_heatmap(self, fig = None, ax = None, 
582:    def plot_coronal_heatmap(self, fig = None, ax = None, 
642:    def plot_horizontal_heatmap(self, fig = None, ax = None, 
703:    def _p_value_to_str(self,p):
713:    def _statistics_decorator_from_p_values(self,ax, p_values, 
767:    def plot_fig2_main(self,):
[... 95 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/MapVideoAnalysis/VideoAnalysisUtils; sed -n 226,500p plotting_utils.py; sed -n 130,281p functions.py
```

```
class Figure2():

    def __init__(self):
        self.single_neuron_inds = {1:59, 2:4, 3:61, 4:45}
        self.single_trial_inds = {1:1, 2:5, 3:2, 4:8}
        self.areas = ['Medulla', 'Midbrain', 'ALM', 'Striatum', 'Thalamus']
        self.image_res = 20 # mu m
        self.ap_lim = [1500,13500]
        self.ml_lim = [900,10800]
        self.dv_lim = [8000,0]
        self.anatomy_alpha = 0.9
        self.ap_slice = slice(int(self.ap_lim[0] / self.image_res), int(self.ap_lim[1] / self.image_res))
        self.ml_slice = slice(int(self.ml_lim[0] / self.image_res), int(self.ml_lim[1] / self.image_res))
        self.dv_slice = slice(int(self.dv_lim[1] / self.image_res), int(self.dv_lim[0] / self.image_res))

        self.ap_cut = 350
        self.ml_cut = 250
        self.dv_cut = 210
        return

[... 409 more lines not kept]
```

**Agent**

Code confirms many details (insertion = probe file, Bonferroni ×10, improvement as per-neuron ratio averaged per session). Continuing with the time-offset, thalamus and choice/movement code.

**Agent calls Bash**

```bash
cd $TMPDIR/MapVideoAnalysis/VideoAnalysisUtils; sed -n 909,1075p plotting_utils.py; sed -n 1262,1300p plotting_utils.py; sed -n 1884,1907p plotting_utils.py
```

```
class Figure3():
    def __init__(self):
        self.areas = ['Medulla','Midbrain', 'ALM', 'Striatum', 'Thalamus']
        self.image_res = 20 # mu m
        self.ap_lim = [1500,13500]
        self.ml_lim = [900,10800]
        self.dv_lim = [8000,0]

        self.ap_slice = slice(int(self.ap_lim[0] / self.image_res), int(self.ap_lim[1] / self.image_res))
        self.ml_slice = slice(int(self.ml_lim[0] / self.image_res), int(self.ml_lim[1] / self.image_res))
        self.dv_slice = slice(int(self.dv_lim[1] / self.image_res), int(self.dv_lim[0] / self.image_res))

        self.ap_cut = 350
        self.ml_cut = 250
        self.dv_cut = 210

        self.global_offset_vec = np.array([5700, 0, 5400])

        self.view_to_vlim = {'positive fraction': [0,1],
                             'negative fraction': [0,1],
[... 211 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/MapVideoAnalysis; sed -n 3101,3398p VideoAnalysisUtils/plotting_utils.py | grep -v "^\s*$" | head -300
```

```
class Figure7():
    def __init__(self):
        self.thalamus_use_nuclei = [
            #'Anteromedial nucleus', #AN
            'Central medial nucleus of the thalamus', # CN
            'Central lateral nucleus of the thalamus', #CN
            'Mediodorsal nucleus of thalamus', #MD
            #'Medial geniculate complex', #MGN
            'Paracentral nucleus', #PC
            #'Parafascicular nucleus', #PF
            'Posterior complex of the thalamus', #PO
            #'Paraventricular nucleus of the thalamus', #PVN
            #'Reticular nucleus of the thalamus', #RT
            #'Submedial nucleus of the thalamus', #SMN
            'Ventral anterior-lateral complex of the thalamus', #VAL
            'Ventral medial nucleus of the thalamus', #VM
            'Ventral posterior complex of the thalamus', #VPN - this is 4 subnuclei
        ]
        self.thalamus_use_short_names = [
            #'AM',
[... 237 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/MapVideoAnalysis/Notebooks; for n in fig4_plot timeshift_plots supp_fig_S6; do echo "=== $n"; python $TMPDIR/nbsrc.py $n.ipynb | grep -v "^\s*$" | grep -n -i -B3 -A12 "mannwhitney\|spearman\|ttest\|benjamini\|fdr\|multipletests" | head -150; done
```

```
=== fig4_plot
=== timeshift_plots
366-use_inds = {k: np.intersect1d(v,threshold_inds) for k,v in inds.items() if np.intersect1d(v,threshold_inds).shape[0] > n_min}
367-# --- cell 30
368-delta_r2 = 1.2
369:from scipy.stats import ttest_1samp
370-delta_inds = np.where((r2.max(axis = 0) / r2.mean(axis = 0)) > delta_r2)[0]
371-f,_ = plt.subplots(len(list(use_inds.keys())),2, figsize = (15,20))
372-f.suptitle('Best time dist & shifted r2 maps, epoch: %s, r2_method: %s, fr_min=%.2f, r2_min=%.2f, delta_r2=%.2f'%(epoch,r2_method,fr_threshold,r2_threshold,delta_r2), fontsize = 16)
373-for i, area in enumerate(use_inds.keys()):
374-    _this_inds = np.intersect1d(use_inds[area], delta_inds)
375-    plt.subplot(len(list(use_inds.keys())),2,2*i+1)
376-    _mean = best_times[_this_inds].mean()
377-    _meadian = np.median(best_times[_this_inds])
378-    plt.hist(best_times[_this_inds], bins = 31, color = cc[i])
379-    a,b = plt.ylim()
380:    t_stat, p_value = ttest_1samp(best_times[_this_inds], 0)
381-    significance_str = '***' if p_value < .001 else '**' if p_value < .01 else '*' if p_value < .05 else ''
382-    plt.plot([_mean, _mean], [a,b], 'k--', label = '%s mean = %.2f ms'%(significance_str,_mean))
383-    plt.plot([],[],' ', label = 'p_value = %.2E'%p_value)
[... 142 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/MapVideoAnalysis; grep -rln "alternative" --include=*.ipynb --include=*.py . | grep -v Archive; for n in Notebooks/fig4_plot.ipynb Notebooks/fig3_plot.ipynb; do echo "=== $n"; python $TMPDIR/nbsrc.py $n | grep -v "^\s*$" | grep -n -i -B2 -A8 "alternative\|spearman\|uniformity\|f_oneway\|# OUT" | head -120; done
```

```
./VideoAnalysisUtils/plotting_utils.py
./Notebooks/fig6_plot_clean.ipynb
./Notebooks/fig6_plots.ipynb
./Notebooks/fig7_plot.ipynb
=== Notebooks/fig4_plot.ipynb
19-import VideoAnalysisUtils.plot_style as style
20-from mpl_toolkits.axes_grid1 import make_axes_locatable
21:# OUT: The autoreload extension is already loaded. To reload it, use:
22-  %reload_ext autoreload
23-# --- cell 3
24-figfolder = '../figs/manuscript_drafts/'
25-os.makedirs(figfolder, exist_ok=True)
26-# --- cell 4
27-class Annotation_from_Coords():
28-    def __init__(self, datafolder = '../data/', tif_name = 'Annotation_new_10_ds222_32bit.tif', csv_name = 'mousebrainontology_2.csv'):
29-        self.image_data = self.load_tif_fast(datafolder + tif_name)
--
86-image_plot_AP_group1 = 340
87-image_plot_AP_group2 = 330
88:# OUT: Loading ../data/Annotation_new_10_ds222_32bit.tif...
[... 227 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/MapVideoAnalysis; sed -n 1955,2264p VideoAnalysisUtils/plotting_utils.py | grep -v "^\s*$"
```

```
class Figure4():
    def __init__(self):
        self.thalamus_use_nuclei = [
            #'Anteromedial nucleus', #AN
            'Central medial nucleus of the thalamus', # CN
            'Central lateral nucleus of the thalamus', #CN
            'Mediodorsal nucleus of thalamus', #MD
            #'Medial geniculate complex', #MGN
            'Paracentral nucleus', #PC
            #'Parafascicular nucleus', #PF
            'Posterior complex of the thalamus', #PO
            #'Paraventricular nucleus of the thalamus', #PVN
            #'Reticular nucleus of the thalamus', #RT
            #'Submedial nucleus of the thalamus', #SMN
            'Ventral anterior-lateral complex of the thalamus', #VAL
            'Ventral medial nucleus of the thalamus', #VM
            'Ventral posterior complex of the thalamus', #VP - this is 4 subnuclei
        ]
        self.short_names_correct_allen = [
            #'AM',
[... 231 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/MapVideoAnalysis; python $TMPDIR/nbsrc.py Notebooks/thalamus_nn_and_spatial_noise.ipynb | grep -v "^\s*$" | head -250
```

```
# --- cell 1
%load_ext autoreload
%autoreload 2
import os, json
import numpy as np
import matplotlib.pyplot as plt
import math
import sys
from mpl_toolkits.mplot3d import axes3d, Axes3D
import scipy.io as spio
from scipy import stats
import pandas as pd
import pickle
import local_env
import VideoAnalysisUtils.functions as func
import VideoAnalysisUtils.plotting_utils as plt_utils
# --- cell 2
figfolder = '../figs/thalamus/'
datafolder = '../data/'
os.makedirs(os.path.abspath(figfolder), exist_ok=True)
[... 231 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/MapVideoAnalysis; python $TMPDIR/nbsrc.py Notebooks/thalamus_nn_and_spatial_noise.ipynb | grep -v "^\s*$" | sed -n 250,420p | grep -n -i -B4 -A10 "p_value\|uniformity\|mean(\|# OUT" | head -120
```

```
5-# --- cell 21
6-nn_auc = {}
7-shuffle_auc = {}
8-auc_diff = {}
9:p_values = {}
10-for k,v in r2_diff_nn_dict.items():
11-    nn_sorted = np.sort(v)
12-    max_nn_r2 = nn_sorted[-1]
13-    nn_cdf = np.linspace(0,1,nn_sorted.shape[0])
14-    nn_auc[k] = func.calculate_auc(nn_sorted, nn_cdf)
15-    auc_diff[k] = []
16-    for i in range(N_shuffle):
17-        shuffle_sorted = np.sort(subnuclei_separate_shuffle_r2[k][i])
18-        shuffle_cdf = np.linspace(0,1, shuffle_sorted.shape[0])
19-        max_shuffle_r2 = shuffle_sorted[-1]
--
27-            _nn_cdf = nn_cdf
28-            _shuffle_sorted = np.append(shuffle_sorted,[max_nn_r2])
29-            _shuffle_cdf = np.append(shuffle_cdf, [1])
30-        auc_diff[k].append(func.calculate_auc(_nn_sorted, _nn_cdf) - func.calculate_auc(_shuffle_sorted, _shuffle_cdf))
[... 101 more lines not kept]
```

**Agent**

Now the choice-decoding (Fig. 6) and choice/movement neuron (Fig. 7) code.

**Agent calls Bash**

```bash
cd $TMPDIR/MapVideoAnalysis; for n in fig6_plot_clean fig7_plot; do echo "=== $n"; python $TMPDIR/nbsrc.py Notebooks/$n.ipynb | grep -v "^\s*$" | grep -v "^\s*#" | head -400 | cut -c1-220; done > $TMPDIR/fig67.txt; wc -l $TMPDIR/fig67.txt; head -300 $TMPDIR/fig67.txt
```

```
802 /tmp/claude-1001/fig67.txt
=== fig6_plot_clean
%load_ext autoreload
%autoreload 2
import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from scipy import stats
import pandas as pd
import pickle
from PIL import Image
import local_env
import VideoAnalysisUtils.functions as func
import VideoAnalysisUtils.plotting_utils as plt_utils
import VideoAnalysisUtils.plot_style as style
  warnings.warn(msg)
figfolder = '../figs/manuscript_drafts/'
os.makedirs(figfolder, exist_ok=True)
fig6 = plt_utils.Figure6()
[... 282 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/MapVideoAnalysis; sed -n 300,802p $TMPDIR/fig67.txt | grep -n -i -B3 -A6 "binom\|calinski\|pearson\|roc\|ttest\|wilcox\|mannwh\|print\|uniformity" | head -200
```

```
38-ccf_coords = fig6.auc_delay_data['ccf_coords']
39-motor_auc = fig6.auc_delay_data['motor_type_auc_test']
40-trial_auc = fig6.auc_delay_data['trial_type_auc_test']
41:p_motor, f_motor, shuffle_motor = func.spatial_uniformity_test(motor_auc, ccf_coords, voxel_size = 500, n_shuffle = 1000, rng_seed = 0, return_raw_stats = True)
42-plt.figure(figsize = (3,2))
43-plt.hist(shuffle_motor, bins = 20, color = 'gray')
44-plt.axvline(f_motor, color = 'red')
45:print(p_motor)
46:p_trial, f_trial, shuffle_trial = func.spatial_uniformity_test(trial_auc, ccf_coords, voxel_size = 500, n_shuffle = 1000, rng_seed = 0, return_raw_stats = True)
47-plt.figure(figsize = (3,2))
48-plt.hist(shuffle_trial, bins = 20, color = 'gray')
49-plt.axvline(f_trial, color = 'red')
50:print(p_trial)
51:p_diff, f_diff, shuffle_diff = func.spatial_uniformity_test(trial_auc - motor_auc, ccf_coords, voxel_size = 500, n_shuffle = 1000, rng_seed = 0, return_raw_stats = True)
52-plt.figure(figsize = (3,2))
53-plt.hist(shuffle_diff, bins = 20, color = 'gray')
54-plt.axvline(f_diff, color = 'red')
55:print(p_diff)
56-fig6.get_medulla_alm_fraction_stats()
57-ALM motor: 148, ALM trial: 710, ALM both: 73, ratio: 4.80
[... 85 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/MapVideoAnalysis; grep -rl -i "calinski" . | grep -v "^./.git"; sed -n 2353,2440p VideoAnalysisUtils/plotting_utils.py | grep -v "^\s*$"; sed -n 2520,2545p VideoAnalysisUtils/plotting_utils.py; sed -n 2719,2780p VideoAnalysisUtils/plotting_utils.py
```

```
class Figure6():
    def __init__(self):
        self.example_marker_inds = [1]
        self.example_neuron_inds = [7,8]
        self.areas = ['Midbrain', 'Thalamus', 'Striatum', 'ALM', 'Somatosensory areas', 'Medulla']
        self.image_res = 20 # mu m
        self.ap_lim = [1500,13500]
        self.ml_lim = [900,10800]
        self.dv_lim = [8000,0]
        self.ap_slice = slice(int(self.ap_lim[0] / self.image_res), int(self.ap_lim[1] / self.image_res))
        self.ml_slice = slice(int(self.ml_lim[0] / self.image_res), int(self.ml_lim[1] / self.image_res))
        self.dv_slice = slice(int(self.dv_lim[1] / self.image_res), int(self.dv_lim[0] / self.image_res))
        self.ap_cut = 350
        self.ml_cut = 250
        self.dv_cut = 210
        self.view_to_vlim = {'motor fraction': [0,0.05],
                             'trial fraction': [0,0.15],
                             'motor average': [0.45,0.6],
                             'trial average': [0.45,0.6],
                             'motor-trial average': [-0.2,0.2],
[... 142 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/MapVideoAnalysis; python $TMPDIR/nbsrc.py Notebooks/fig6_plot_clean.ipynb | grep -n -A8 "get_medulla_alm_fraction_stats\|print(p_motor)\|print(p_trial)\|print(p_diff)" | head -60; grep -rn "def \|AUC\|roc_auc" Sherlock/collect_trial_type_labels_for_fig6.py Sherlock/calculate_delay_fr_video_prediction_trial_types.py | head -40
```

```
479:print(p_motor)
480-# OUT: 0.0
481-
482-# OUT: <Figure size 900x600 with 1 Axes>
483-# --- cell 25
484-p_trial, f_trial, shuffle_trial = func.spatial_uniformity_test(trial_auc, ccf_coords, voxel_size = 500, n_shuffle = 1000, rng_seed = 0, return_raw_stats = True)
485-# --- cell 26
486-plt.figure(figsize = (3,2))
487-plt.hist(shuffle_trial, bins = 20, color = 'gray')
--
489:print(p_trial)
490-# OUT: 0.0
491-
492-# OUT: <Figure size 216x144 with 1 Axes>
493-# --- cell 27
494-p_diff, f_diff, shuffle_diff = func.spatial_uniformity_test(trial_auc - motor_auc, ccf_coords, voxel_size = 500, n_shuffle = 1000, rng_seed = 0, return_raw_stats = True)
495-# --- cell 28
496-plt.figure(figsize = (3,2))
497-plt.hist(shuffle_diff, bins = 20, color = 'gray')
--
[... 18 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/MapVideoAnalysis; cat Sherlock/collect_trial_type_labels_for_fig6.py | sed -n 1,75p; sed -n 1,114p Sherlock/calculate_trial_motor_type_aucs.py
```

```
import pickle
import numpy as np
import os
import glob

old_ephys_folder = '/scratch/users/kurgyis/data/aiden_fr_files/stride17_bw40/'
new_ephys_folder = '/oak/stanford/groups/shauld/kurgyis/data/Map_ULTIMATE_preprocessed/stride3_bw40/'

cal4cat_filename = '/oak/stanford/groups/shauld/kurgyis/data/AUC_analysis/cal4cat-delay.pickle'
save_filename = '/oak/stanford/groups/shauld/kurgyis/data/AUC_analysis/trial_type_labels.pickle'

cal4cat = pickle.load(open(cal4cat_filename, 'rb'))

save_dict = {}

for short_sess_name in cal4cat.keys():
    print(short_sess_name)
    search_pattern = os.path.join(old_ephys_folder, short_sess_name) + '*'

    # List all files matching the pattern
[... 169 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/MapVideoAnalysis; grep -n "def \|C\b\|Cs\|LogisticRegression\|LeaveOneOut\|param_grid\|cv" VideoAnalysisUtils/functions_for_auc.py | head -40; python $TMPDIR/nbsrc.py Notebooks/from_ccn/AUC-Analaysis.ipynb | grep -v "^\s*$" | head -150 | cut -c1-200
```

```
7:def random_split(trial_labels, cv = 20, random_seed = 42):
15:        cv : int, optional
28:    cv_inds = np.array_split(trial_inds, cv)
31:    for ii in range(cv):
32:        train_inds = np.concatenate([cv_inds[jj] for jj in range(cv) if jj != ii])
33:        test_inds = cv_inds[ii]
40:def calculate_single_neuron_auc_from_classification(
43:    cv = 20, 
56:    Calculate AUC for a single neuron using classification.
64:        cv : int, optional
91:            AUC for the test set, averaged across folds if `concat_folds` is False.
93:            AUC for the training set, averaged across folds if `concat_folds` is False.
111:        split_inds_dict = random_split(trial_labels, cv = cv, random_seed = _seed)
113:        for ii in range(cv):
128:    for ii in range(cv):
148:        test_labels = np.concatenate([trial_labels[split_inds_dict['test'][ii]] for ii in range(cv)])
149:        train_labels = np.concatenate([trial_labels[split_inds_dict['train'][ii]] for ii in range(cv)])
156:            auc_test = np.array([roc_auc_score(trial_labels[split_inds_dict['test'][ii]], test_scores[ii]) for ii in range(cv)])
157:            auc_train = np.array([roc_auc_score(trial_labels[split_inds_dict['train'][ii]], train_scores[ii]) for ii in range(cv)])
159:            auc_test = np.mean([roc_auc_score(trial_labels[split_inds_dict['test'][ii]], test_scores[ii]) for ii in range(cv)])
[... 160 more lines not kept]
```

**Agent**

Paper Fig. 6 (choice decoding from video, Calinski–Harabasz) is not in MapVideoAnalysis. Checking the linked BehaviorVideo repo.

**Agent calls Bash**

```bash
cd $TMPDIR && git clone -q https://github.com/kurgyis/BehaviorVideo.git 2>&1|tail -1; cd BehaviorVideo && git log -1 --format='%H %ad' && find . -type f -not -path './.git/*' | head -60; grep -rli "calinski\|auc_analysis\|cal4cat" . | grep -v .git/ | head
```

```
fatal: could not read Username for 'https://github.com': No such device or address
/bin/bash: line 1: cd: BehaviorVideo: No such file or directory
./w/body.txt
./MapVideoAnalysis/Archive/redo_auc_analysis.ipynb
./MapVideoAnalysis/Archive/replot_old_auc_analysis_data.ipynb
./MapVideoAnalysis/Notebooks/fig6_plot_clean.ipynb
./MapVideoAnalysis/Notebooks/from_ccn/AUC-Analaysis.ipynb
./MapVideoAnalysis/Notebooks/fig6_plots.ipynb
./MapVideoAnalysis/Notebooks/medulla_population_decoding.ipynb
./MapVideoAnalysis/Sherlock/calculate_delay_choice_selectivity_with_video_pred_subtraction.py
./MapVideoAnalysis/Sherlock/collect_trial_type_labels_for_fig6.py
./MapVideoAnalysis/Sherlock/collect_trial_motor_type_aucs.py
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && (git clone -q https://github.com/druckmann-lab/VideoAnalysisTools.git 2>&1|tail -1; cd VideoAnalysisTools 2>/dev/null && git log -1 --format='%H' && find . -type f -not -path './.git/*' | head -30); cd $TMPDIR/MapVideoAnalysis; grep -rln "LogisticRegression" --include=*.py --include=*.ipynb . | grep -v Archive; head -40 VideoAnalysisUtils/population_decoding_utils.py
```

```
585062563c6c8e1b5c288094113391892259902a
./notebooks/README.md
./notebooks/ae_for_taiga.ipynb
./configs/crop_configs/alm_side.json
./configs/README.md
./requirements_cpu.txt
./tests/test_data/example_images.npy
./tests/test_dataset.py
./src/behavioral_autoencoder/data_utils.py
./src/behavioral_autoencoder/dataset.py
./src/setup.py
./README.md
./VideoAnalysisUtils/functions_for_r2.py
./VideoAnalysisUtils/population_decoding_utils.py
import pickle
import os 
import numpy as np
from sklearn.model_selection import StratifiedKFold, GridSearchCV
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score
[... 35 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/MapVideoAnalysis; python $TMPDIR/nbsrc.py Notebooks/fig7_plot.ipynb | grep -v "^\s*$" | grep -n -i -B2 -A4 "alternative\|tau = \|# OUT: [A-Z]" | cut -c1-250 | head -120
```

```
359-# --- cell 26
360-np.argmax(alm_r2.mean(axis = -1), axis = 0)
361:# OUT: array([17, 22, 20, ..., 14, 15, 14])
362-# --- cell 27
363-best_time_r2.shape
364-# OUT: (1059, 5)
365-# --- cell 28
--
411-    a,b = ax.get_ylim()
412-    if zero_line: ax.plot([0,0], [0,1.1*b], ':', color = 'black',)
413:    ax.plot([mean, mean], [0,1.1*b], 'w--',  lw = 2 ,label = r'$\tau = %.1f \pm %.1f$ ms'%(mean,sem))
414-    if print_label:
415:        print('%s, tau = %.1f +/- %.1f ms'%(area_name,mean,sem))
416-    ax.set_ylim(0,1.1*b)
417-    ax.set_title('%s, n=%d'%(area_name,len(area_best_times)))
418-    ax.set_xlabel('Best time shift (ms)')
419-    ax.set_ylabel('Number of neurons')
--
486-plt.hist(best_times[inds_dict[area2]], bins = 31, color = 'lightblue')
487-plt.title('%s, n=%d'%(area2, inds_dict[area2].shape[0]))
[... 101 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/MapVideoAnalysis; python - <<'EOF'
import json
nb=json.load(open('Notebooks/fig7_plot.ipynb'))
for i,c in enumerate(nb['cells']):
    if c['cell_type']=='code' and 2<=i<=53:
        s=''.join(c['source'])
        if 'plot(' in s and 'subplots' not in s and len(s)>1500: s=s[:600]+'\n...'
        print('# --- cell',i); print(s)
EOF
```

```
# --- cell 2
figfolder = '../figs/manuscript_drafts/'
os.makedirs(figfolder, exist_ok=True)
# --- cell 3
#r2_new = pickle.load(open('../data/final/r2_embed_cv_timeshift.pkl', 'rb'))
r2_new = pickle.load(open('[removed: a home directory path]/STANFORD/Druckmann/VideoAnalysis/data/r2_embed_cv_timeshift_long.pkl', 'rb'))
timeshifts = np.arange(-60,62,2, dtype = int)
method_to_string = {'old': '_old', 'old_clipped': '_old', 'new': ''}
datafolder = '../data/'
allen_hierarchy_name = 'mousebrainontology_heirarchy_cortexMaskExclusions21_sc.xlsx'
region2color = {'ALM': [0, 0.6, 0.6], 
                'Medulla': [1, 0.6, 1], 
                'Midbrain': [1, 0.2, 1], 
                'Striatum': [0.2, 0.8, 1], 
                'Thalamus': [1, 0.4, 0.6], 
                'Pons': [1, 0.7, 0.3], 
                'Cerebellum': [1, 1, 0], 
                'Hypothalamus': [1, 0.33, 0], 
                'Hippocampus': [0.45, 0.9, 0.25], 
                'Orbital': [0, 0.57, 0.22], 
[... 601 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/MapVideoAnalysis; python $TMPDIR/nbsrc.py Notebooks/supp_fig_S6.ipynb | grep -v "^\s*$" | grep -n "# OUT\|# --- cell\|r2_noshift =\|load(" | head -60; sed -n 40,135p VideoAnalysisUtils/functions_for_auc.py | grep -n "C\|Grid\|LeaveOneOut\|Logistic\|seed\|repeat"
```

```
1:# --- cell 1
18:# OUT: [removed: a home directory path]/Research/MapVideoAnalysis/python38_venv/lib/python3.8/site-packages/pandas/compat/__init__.py:120: UserWarning: Could not import the lzma module. Your installed Python is incomplete. Attempting to use lzma compression will result in a RuntimeError.
20:# --- cell 2
23:# --- cell 4
24:r2_new = pickle.load(open('../data/final/r2_embed_cv_timeshift.pkl', 'rb'))
45:# --- cell 5
46:r2_noshift = r2_new['5_0']['%s_r2%s'%(epoch,method_to_string[r2_method])].copy()
57:# --- cell 6
62:# --- cell 8
71:# OUT: <Figure size 1080x216 with 5 Axes>
72:# --- cell 9
82:# OUT: <Figure size 1296x216 with 10 Axes>
83:# --- cell 10
97:# OUT: <Figure size 1296x216 with 10 Axes>
98:# --- cell 11
99:# --- cell 13
137:# OUT: Medulla -0.06410234479496886 0.21769598985642807 992
142:# OUT: <Figure size 777.6x129.6 with 10 Axes>
143:# --- cell 14
194:# OUT: Medulla -0.06410234479496886 0.21769598985642807 992
[... 20 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/MapVideoAnalysis; sed -n 1,40p VideoAnalysisUtils/functions_for_auc.py; sed -n 95,140p VideoAnalysisUtils/functions_for_auc.py; grep -n "aligned_auc\|calculate_auc\|cv\b\|cv =" Sherlock/calculate_delay_choice_selectivity_with_video_pred_subtraction.py | head
```

```
from sklearn.linear_model import RidgeClassifierCV
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import roc_auc_score
import numpy as np


def random_split(trial_labels, cv = 20, random_seed = 42):
    """
    Randomly splits trials into training and testing sets for cross-validation.

    Parameters
    ----------
        trial_labels : array-like
            Labels for each trial, used to determine the split.
        cv : int, optional
            Number of cross-validation folds, by default 20.
        random_seed : int, optional
            Seed for random number generator, by default 42.
    Returns
    -------
[... 69 more lines not kept]
```

**Agent**

I have what I need from the paper and code. Writing the claims file now.

**Agent calls Bash**

```bash
cd  f=paper/10.1038-s41593-025-02114-x.txt; for s in "0.176 ± 0.06" "note insertions" "P < 1 × 10" "R = 0.1, P = 0.0014" "p = 3e7" "signed-tank" "Ventral posterior complex of the thalamus;" "(0.1764 ± 0.0061, n = 36) vs Midbrain (0.1043"; do grep -c -F "$s" $f | sed "s/^/$s => /"; done
```

Result: not kept, because it reads the paper's text.

**Agent calls Write**

```json
{
 "file_path": "claims/wang-2025.yaml",
 "content": "# Claims for Wang, Kurgyis, Chen, Kang, Chen, Liu, Liu, Svoboda, Li & Druckmann (2025), \"Brain-wide\n# analysis reveals movement encoding structured across and within brain areas\", Nature Neuroscience,\n# doi:10.1038/s41593-025-02114-x, on dandiset 000363 (Mesoscale Activity Map Dataset), which the\n# paper reuses.\n# Written by an agent (model \"claude-opus-5-5\", Claude Code, runner \"GitHub Actions\"), 2026-11-20,\n# protocol as stated in docs/protocol.md (pilot-18).\n#\n# Text read. The version of record (published 18 November 2025, open access), full text from the\n# publisher's page: main text, figure legends, Methods, Extended Data Figs. 1 to 10 legends. The\n# Supplementary Information PDF (41593_2025_2114_MOESM1_ESM.pdf; Supplementary Discussion on the\n# session-independent autoencoder, Supplementary Table 1 on thalamic nuclei, Supplementary Figs. 1\n# and 2) was read from its extracted text in the same file. The Reporting Summary and the three\n# Supplementary Videos were not read; no claim rests on them. Figures were not opened; every\n# number used below is printed in the text or a legend.\n#\n# Code read. github.com/druckmann-lab/MapVideoAnalysis at commit 7d27624 (7d276243db16db5af6da68a48de7720ef77007c2),\n# the repository the paper links (Zenodo doi:10.5281/zenodo.16740762). It holds the package\n# VideoAnalysisUtils (ridge prediction and explained variance, functions_for_r2.py; single-neuron\n# choice and movement AUCs, functions_for_auc.py; area selection, nearest-neighbour and spatial\n# uniformity tests, functions.py; figure classes and their statistics, plotting_utils.py, where\n# the paper's Figs. 2, 4, 3, 5 and 7 are the classes Figure2, Figure3, Figure4, Figure7 and\n# Figure6), the cluster scripts under Sherlock/ (train/test splits, ridge fits at each time shift,\n# AUC runs) and figure notebooks under Notebooks/ with their printed outputs. The deep networks\n# (autoencoder, end-to-end) are in a separate repository, github.com/kurgyis/BehaviorVideo, which\n# could not be fetched (not public at the time of reading); a light version is at\n# github.com/druckmann-lab/VideoAnalysisTools (commit 5850625), read only for its file list. The\n# code that decodes choice from video (Fig. 6, the Calinski-Harabasz scores, the correlation with\n# performance, and the single-trial video predictions used in Fig. 7) is not in either repository:\n# MapVideoAnalysis reads its output from a precomputed file (cal4cat-delay.pickle). Details of Fig. 6\n# that the Methods leave open are therefore open below.\n# Where the Methods are silent the criteria follow this code and say so. Where the code differs from\n# the Methods, the Methods come first and the code's choice is named as a variant. Some printed\n# outputs in the notebooks differ from the paper (the method improvements print as 174%, 377% and 83%\n# against the paper's 155%, 330% and 76%), so the code's data files are not exactly those of the\n# paper; the claims hold to the paper's numbers.\n#\n# Data the paper describes. A reanalysis of the Mesoscale Activity Map data (Chen et al., Cell 2024,\n# ref. 30; DANDI 000363, cited as version 0.230822.0128; the code's README cites 0.231012.2129). The\n# Methods say 28 mice (25 VGAT-ChR2-EYFP, one C57BL/6J, one Sst-IRES-Cre x Ai32, one Emx1-IRES-Cre x\n# R26-LNL-GtACR1-Fred-Kv2.1), 3 to 7 months old; the Supplementary Discussion says 22 mice and 100\n# sessions for the session-independent autoencoder. Task. Delayed response; a series of pure tones\n# in the sample epoch (12 kHz instructs lick left, 3 kHz lick right), a 1.2 s delay without licking,\n# then a go cue and a response epoch of directional licking for water. Epochs in the code, relative\n# to the go cue: sample -1.85 to -1.2 s, delay -1.2 to 0 s, response 0 to 1.5 s; the epoch averages\n# leave out 150 ms at each edge, which the code takes as -1.7 to -1.35, -1.05 to -0.15 and 0.15 to\n# 1.2 s. Trials with photoinhibition, free water, early licks or no response are excluded from all\n# analyses. Recordings. Two to five Neuropixels probes at once, in ALM (both hemispheres in some\n# sessions), medulla, midbrain, striatum, thalamus and other areas; Kilosort spike sorting with the\n# project's quality control; each unit registered to the Allen CCF v3 with an annotation. More than\n# 50,000 neurons in total. Firing rates are spike counts in 40 ms bins at a 3.4 ms stride; neurons\n# below 2 Hz are excluded. Video. 300 Hz side and bottom views of face and paws; only the side view\n# is used. DeepLabCut markers (jaw, nose and tongue in the Results and Fig. 1e; the Methods list\n# jaw, paws and tongue), with 5-sigma velocity outliers imputed and the occluded tongue set to its\n# mean. A 16-dimensional autoencoder embedding per frame (encoder as given in the Methods, linear\n# decoder, one per session). Sample sizes. 105 sessions for the method comparison (Fig. 2), 106\n# sessions for choice decoding (Fig. 6), 87 sessions in Fig. 7d, 80 sessions with video choice AUC\n# above 0.6. Insertions per area for Fig. 2b: medulla 36, midbrain 79, ALM 77, striatum 67,\n# thalamus 62. An insertion in the code is one probe file of one session (a region and hemisphere).\n#\n# Outside data. The paper states that all data are on DANDI. The authors also deposited processed\n# data for the figures (Zenodo doi:10.5281/zenodo.16740783; it holds the Allen hierarchy table\n# mousebrainontology_heirarchy_cortexMaskExclusions21_sc.xlsx that the code uses to group CCF labels\n# into areas) and go-cue aligned single-trial autoencoder embeddings (a Google Drive folder linked\n# from the code's README, not pinned). The claims use the dataset; whether it holds the raw video\n# the embeddings and end-to-end networks need is the author's to find, and the authors' embeddings\n# are the named alternative input. The grouping of CCF labels into areas can be rebuilt from the\n# Allen ontology (structure tree) where the Zenodo table is not used.\n#\n# Method choices fixed from the paper and code, used by many claims.\n# - Prediction of activity (Methods, Prediction of neural activity). At each time bin t, features at\n#   five frames t-6.8, t-3.4, t, t+3.4 and t+6.8 ms are concatenated (80 dimensions for the\n#   embedding, 15 for three markers) and ridge regression predicts every neuron's rate at t across\n#   trials. The penalty is chosen by inner fivefold cross-validation from 0.001, 0.01, 0.1, 1 and 10\n#   (code, RidgeCV).\n# - Explained variance (Methods, Epoch-averaged explained variance; code). R2 (sklearn r2_score) of\n#   the test-trial rates at each time bin, negatives set to 0, averaged over folds, then over the\n#   bins of the epoch with 150 ms trimmed at each edge.\n# - Neuron filter. Rate above 2 Hz and explained variance above 0.01 (Methods). The code uses the\n#   epoch rate for the area comparison, the trial-average rate elsewhere, and 0.005 in place of 0.01\n#   for the method comparison; these are named in the criteria.\n# - Splits. Fig. 2 and Extended Data Figs. 2 and 3: one stratified random split with 64 test trials\n#   (strata lick direction by correctness), the same for all three methods (Methods; code uses\n#   StratifiedShuffleSplit, random_state 0). Figs. 3 to 5: fivefold cross-validation stratified by\n#   lick direction and correctness. Figs. 6 and 7: correct trials only, 20-fold cross-validation.\n# - Areas. Medulla, Midbrain, Striatum and Thalamus are the neurons whose CCF annotation falls under\n#   that Allen structure; ALM is the neurons of the probes targeted to ALM (code, get_single_area_inds:\n#   the probe file name contains ALM), and ALM neurons are removed from other cortical groups.\nschema_version: 2\npaper: doi:10.1038/s41593-025-02114-x\nclaims:\n- id: data-scale\n  statement: The analysis covers more than 50,000 neurons recorded in more than a dozen cortical and\n    subcortical structures, simultaneously with high-speed video of orofacial movements.\n  source: Main text, Introduction, paragraph 4\n  quote: we analyzed recordings of more than 50,000 neurons, recorded in more than a dozen cortical\n    and subcortical structures, simultaneously with high-speed video of orofacial movements\n  criterion: Counted over the sessions of the dataset with video, after the paper's trial\n    exclusions. Reproduced when the number of units passing the dataset's quality labels exceeds\n    50,000 and they fall in more than 12 distinct Allen structures at the level of the areas the\n    paper names (for example ALM, other isocortex, striatum, thalamus, midbrain, medulla, pons,\n    cerebellum). The paper does not say whether the count is before or after the 2 Hz filter; both\n    counts are reported, and the claim holds if either exceeds 50,000.\n- id: fig2b-medulla-vs-midbrain\n  statement: In the response epoch, variance explained by the embedding-based video prediction is\n    larger in medulla than in midbrain (0.176 against 0.104, insertion averages).\n  source: Results, Neural activity explained by movement differs across brain areas, paragraph 3;\n    Figure 2b; Extended Data Fig. 3 legend\n  quote: Variance explained in the medulla was significantly larger than midbrain (medulla explained\n    variance from the embedding method 0.176 ± 0.06 s.e.m., n = 36 insertions compared with 0.104 ±\n    0.004, n = 79 of midbrain, P < 0.001, Mann–Whitney test\n  statistics:\n  - test: two-sided Mann-Whitney U test, Bonferroni corrected (Fig. 2b legend)\n    p: 0.001\n    p_relation: \"<\"\n    corrected: Bonferroni\n    n: 36 medulla and 79 midbrain insertions\n  expected:\n  - quantity: medulla response-epoch explained variance, mean over insertions\n    value: 0.176\n    tolerance: 0.0061\n  - quantity: midbrain response-epoch explained variance, mean over insertions\n    value: 0.104\n    tolerance: 0.004\n  - quantity: medulla insertions\n    value: 36\n    tolerance: 3.6\n  - quantity: midbrain insertions\n    value: 79\n    tolerance: 7.9\n  criterion: Tolerances are the s.e.m. the paper gives. The main text prints the medulla s.e.m. as\n    0.06; Extended Data Fig. 3 gives 0.1764 ± 0.0061 for the same value, so 0.006 is taken as meant.\n    Method as in the opening comment, single 64-trial test split, response epoch. Per the code\n    (Figure2.get_barplot_statistics), neurons with response-epoch rate above 2 Hz and explained\n    variance above 0.01 under all three methods; each insertion's value is the mean of its neurons;\n    two-sided Mann-Whitney U on the insertion values, p multiplied by 10 (all pairs of the five\n    areas). Reproduced when both means are within tolerance and the corrected p < 0.001 with medulla\n    higher. If the end-to-end network cannot be trained, the filter on the embedding and marker\n    values alone is used and this is recorded as a deviation.\n- id: fig2b-area-ordering\n  statement: Movement-related activity is present in all five areas, and explained variance in the\n    response epoch follows the distance to the sensory or motor periphery, highest in medulla, lowest\n    in thalamus, with midbrain, ALM and striatum in between and not different from each other.\n  source: Results, Neural activity explained by movement differs across brain areas, paragraph 3;\n    Figure 2a,b; Extended Data Fig. 3 legend (response epoch)\n  quote: Explained variance followed a logical progression, with greater explained variance in areas\n    closer to the sensory or motor periphery (Fig. 2b ).\n  statistics:\n  - about: medulla against each of midbrain, ALM, striatum and thalamus\n    test: two-tailed Mann-Whitney U test\n    p: 1.04e-11\n    corrected: Bonferroni\n    n: 36, 79, 77, 67 and 62 insertions\n  - about: thalamus against midbrain, ALM and striatum (largest of the three p)\n    test: two-tailed Mann-Whitney U test\n    p: 8.26e-09\n    corrected: Bonferroni\n  - about: midbrain against ALM\n    test: two-tailed Mann-Whitney U test\n    p: 0.314\n    corrected: Bonferroni\n  - about: midbrain against striatum\n    test: two-tailed Mann-Whitney U test\n    p: 0.0999\n    corrected: Bonferroni\n  - about: ALM against striatum\n    test: two-tailed Mann-Whitney U test\n    p: 1\n    corrected: Bonferroni\n  expected:\n  - quantity: medulla, response epoch, insertion mean\n    value: 0.1764\n    tolerance: 0.0061\n  - quantity: midbrain, response epoch, insertion mean\n    value: 0.1043\n    tolerance: 0.004\n  - quantity: ALM, response epoch, insertion mean\n    value: 0.0923\n    tolerance: 0.0037\n  - quantity: striatum, response epoch, insertion mean\n    value: 0.0912\n    tolerance: 0.0034\n  - quantity: thalamus, response epoch, insertion mean\n    value: 0.0611\n    tolerance: 0.0026\n  criterion: Tolerances are the s.e.m. in Extended Data Fig. 3. Method as in fig2b-medulla-vs-midbrain,\n    all ten pairs, Bonferroni factor 10. Reproduced when the five means are within tolerance, the\n    seven pairs involving medulla or thalamus are significant at corrected p < 0.05 in the direction\n    of the paper, and the three pairs among midbrain, ALM and striatum are not (corrected p > 0.05).\n    Partially reproduced when the order medulla, then midbrain/ALM/striatum, then thalamus holds and\n    all seven significant pairs hold, but some means fall outside tolerance.\n  depends_on:\n  - fig2b-medulla-vs-midbrain\n- id: edfig3-epochs\n  statement: Explained variance is larger in the response epoch, with its licking, than in the sample\n    and delay epochs, but the differences between areas are preserved in the sample and delay epochs,\n    with medulla highest and thalamus lowest.\n  source: Results, Neural activity explained by movement differs across brain areas, paragraph 4;\n    Extended Data Figs. 2 and 3\n  quote: Comparison across epochs suggested that a large portion of activity was correlated with\n    licking and associated facial movements (Extended Data Fig. 2 ), but the relative differences in\n    movement encoding between areas were preserved (Extended Data Fig. 3 ).\n  statistics:\n  - about: sample epoch, medulla against thalamus\n    test: two-tailed Mann-Whitney U test\n    p: 3.77e-07\n    corrected: Bonferroni\n    n: 36 medulla and 57 thalamus insertions\n  - about: delay epoch, medulla against thalamus\n    test: two-tailed Mann-Whitney U test\n    p: 8.06e-10\n    corrected: Bonferroni\n    n: 36 medulla and 53 thalamus insertions\n  - about: sample epoch, medulla against midbrain\n    test: two-tailed Mann-Whitney U test\n    p: 0.0785\n    corrected: Bonferroni\n  - about: delay epoch, medulla against midbrain\n    test: two-tailed Mann-Whitney U test\n    p: 0.0304\n    corrected: Bonferroni\n  expected:\n  - quantity: sample epoch, medulla\n    value: 0.0833\n    tolerance: 0.0066\n  - quantity: sample epoch, midbrain\n    value: 0.0632\n    tolerance: 0.0039\n  - quantity: sample epoch, ALM\n    value: 0.0629\n    tolerance: 0.0047\n  - quantity: sample epoch, striatum\n    value: 0.0586\n    tolerance: 0.0046\n  - quantity: sample epoch, thalamus\n    value: 0.0364\n    tolerance: 0.0027\n  - quantity: delay epoch, medulla\n    value: 0.0927\n    tolerance: 0.0065\n  - quantity: delay epoch, midbrain\n    value: 0.069\n    tolerance: 0.0045\n  - quantity: delay epoch, ALM\n    value: 0.0654\n    tolerance: 0.0069\n  - quantity: delay epoch, striatum\n    value: 0.0594\n    tolerance: 0.0063\n  - quantity: delay epoch, thalamus\n    value: 0.0347\n    tolerance: 0.0028\n  criterion: Insertion means of embedding-based explained variance per epoch, tolerances the s.e.m. in\n    Extended Data Fig. 3; method as in fig2b-medulla-vs-midbrain with the epoch's own rate filter.\n    Reproduced when (a) in every area the response-epoch mean exceeds both the sample and delay\n    means, and (b) in both the sample and delay epochs medulla has the highest and thalamus the\n    lowest mean, and thalamus is significantly lower than each other area (corrected p < 0.05), as\n    in the legend. The ten means are reported against their tolerances.\n  depends_on:\n  - fig2b-area-ordering\n- id: fig2e-method-improvement\n  statement: The more expressive models predict activity better; the embedding improves on markers by\n    155%, end-to-end learning on markers by 330% and on the embedding by 76%, averaged over 105\n    sessions.\n  source: Results, Neural activity explained by movement differs across brain areas, paragraph 4;\n    Figure 2c-e legend\n  quote: improvement in explained variance for embedding-based approach versus marker-based approach,\n    improvement = 155 ± 5% s.e.m., n = 105 sessions, P < 0.001; end-to-end learning versus\n    marker-based approach, improvement = 330 ± 9% s.e.m., n = 105 sessions, P < 0.001; end-to-end\n    learning versus embedding-based approach, improvement = 76 ± 3% s.e.m., n = 105 sessions, P <\n    0.001, one-sided Wilcoxon signed-tank test with Bonferroni correction\n  statistics:\n  - about: embedding against marker\n    test: one-sided Wilcoxon signed-rank test\n    p: 0.001\n    p_relation: \"<\"\n    corrected: Bonferroni\n    n: 105 sessions\n  - about: end-to-end against marker\n    test: one-sided Wilcoxon signed-rank test\n    p: 0.001\n    p_relation: \"<\"\n    corrected: Bonferroni\n    n: 105 sessions\n  - about: end-to-end against embedding\n    test: one-sided Wilcoxon signed-rank test\n    p: 0.001\n    p_relation: \"<\"\n    corrected: Bonferroni\n    n: 105 sessions\n  expected:\n  - quantity: mean improvement, embedding over marker\n    value: 155\n    tolerance: 5\n    unit: percent\n  - quantity: mean improvement, end-to-end over marker\n    value: 330\n    tolerance: 9\n    unit: percent\n  - quantity: mean improvement, end-to-end over embedding\n    value: 76\n    tolerance: 3\n    unit: percent\n  - quantity: sessions\n    value: 105\n    tolerance: 10.5\n  criterion: Tolerances are the s.e.m. given. Response epoch, single 64-trial test split. Per the\n    code (Figure2.get_method_comparison_stats), neurons with trial-average rate above 2 Hz and\n    explained variance above 0.005 under all three methods; per neuron, improvement = (EV_better -\n    EV_worse) / EV_worse; per session, the mean over its neurons; the mean and s.e.m. over sessions;\n    a Wilcoxon signed-rank test of the session means against zero, one-sided p (two-sided p halved)\n    times 3. The Methods' threshold of 0.01 is the variant. Reproduced when all three improvements\n    are positive with corrected p < 0.001 and within tolerance; partially reproduced when the\n    ordering end-to-end > embedding > marker holds with p < 0.001 but the percentages fall outside\n    tolerance (the mean of a ratio is sensitive to the filter; the code's own output prints 174%,\n    377% and 83%). The end-to-end network is as the Methods describe (three residual blocks, batch\n    norm, max pooling, linear output, one network per session and area); its training settings\n    (optimizer, epochs, input frames) are not in the paper or the code read and are open; the\n    author states the choices used.\n- id: fig2-ordering-across-methods\n  statement: The ordering of brain areas by predictive power is the same for the marker, embedding\n    and end-to-end approaches.\n  source: Results, Neural activity explained by movement differs across brain areas, paragraph 4;\n    Figure 2b; Extended Data Fig. 3\n  quote: The ordering of brain areas in terms of predictive power was preserved across approaches,\n    despite the greater predictive power of the more expressive models\n  criterion: Insertion means of response-epoch explained variance per area, for each method, method\n    as in fig2b-area-ordering. The paper does not say what \"ordering\" covers when areas do not differ\n    (midbrain, ALM and striatum are not different under the embedding). Readings. (a) The strict rank\n    of all five areas is the same under the three methods. (b) Under each method medulla has the\n    highest and thalamus the lowest mean, and the middle three may change order. Reproduced under\n    either reading; the three rank orders are reported.\n  depends_on:\n  - fig2b-area-ordering\n- id: edfig1-reliable-unpredicted\n  statement: Some neurons with highly reliable trial-to-trial responses are poorly predicted from\n    video; 196 such neurons are found in the whole dataset, some apparently representing the\n    auditory cues.\n  source: Results, Neural activity explained by movement differs across brain areas, paragraph 4;\n    Methods, Identifying neurons with reliable firing patterns and poor video prediction; Extended\n    Data Fig. 1\n  quote: We have found a total of 196 such neurons in the whole dataset.\n  expected:\n    quantity: neurons with reliable firing and poor video prediction\n    value: 196\n    tolerance: 19.6\n  criterion: Selection from the Methods. Embedding-based response-epoch explained variance below 0.1,\n    mean correlation of single-trial rate traces with the trial-average trace above 0.4, and time\n    average of the across-trial rate variance below 100 per second squared (code,\n    get_mean_corr_and_trial_to_trial_variance, which correlates each trial with the trial average\n    over the whole trial window). The paper does not say which split or rate filter; readings are the\n    single 64-trial split of Fig. 2 and the fivefold cross-validated values of Figs. 3 to 5, with the\n    2 Hz filter. Reproduced when the count is within 10% of 196 under one reading. The paper's\n    statement that some of these neurons follow the auditory cues is shown by example only and is\n    not tested.\n- id: fig3-thalamus-nonuniform\n  statement: Variance explained is not uniform across the thalamus.\n  source: Results, Neural activity explained by movement differs across brain areas, paragraph 5;\n    Figure 3a-d; Methods, Test against spatial uniformity\n  quote: We found that explained variance was nonuniform across the thalamus (Fig. 3a–d , test against\n    spatial uniformity, P < 0.0001, and Methods ).\n  statistics:\n  - test: one-way F-test across 0.2 mm voxels against a shuffle null\n    p: 0.0001\n    p_relation: \"<\"\n  criterion: Methods, Test against spatial uniformity. Thalamic neurons of the seven nuclei of\n    fig3f-thalamic-nuclei (code, thalamus_nn_and_spatial_noise.ipynb) grouped into 0.2 mm cubic voxels\n    of CCF coordinates; F statistic of a one-way ANOVA of response-epoch explained variance (fivefold\n    cross-validated, zero shift) across voxels; null from 10,000 shuffles of the values across\n    neurons with coordinates fixed; p is the fraction of shuffled F at or above the observed F.\n    Reproduced when p < 0.0001 (no shuffle reaches the observed F).\n  depends_on:\n  - fig3f-thalamic-nuclei\n- id: fig3e-nearest-neighbor\n  statement: Explained variance changes smoothly across thalamus; the difference in explained variance\n    between nearest-neighbour neurons is smaller than in a shuffle control.\n  source: Results, Neural activity explained by movement differs across brain areas, paragraph 5;\n    Figure 3e; Methods, Testing against spatial discontinuity\n  quote: We found that variance explained was significantly smaller between nearest-neighbor pairs,\n    indicating spatially structured smooth changes in variance explained across thalamus (Fig. 3e ,\n    nearest-neighbor difference in explained variance smaller than shuffle control, P < 1 × 10 −3 ).\n  statistics:\n  - test: shuffle (bootstrap) test, 1,000 shuffles within nuclei\n    p: 0.001\n    p_relation: \"<\"\n  criterion: Methods and code (functions.get_NN_r2_dist; thalamus_nn_and_spatial_noise.ipynb). Within\n    each of the seven nuclei, each neuron's absolute difference in explained variance to its nearest\n    neighbour in CCF space; pooled over nuclei. Null, 1,000 shuffles of explained variance across\n    neurons within each nucleus. The statistic is the area under the cumulative distribution of the\n    differences, data minus shuffle (code, calculate_auc on the sorted values); p is the fraction of\n    shuffles in which the data area is not larger. Reproduced when p < 0.001.\n  depends_on:\n  - fig3f-thalamic-nuclei\n- id: fig3f-thalamic-nuclei\n  statement: Seven thalamic nuclei have enough neurons for analysis (CN 235, MD 1,112, PCN 268, PO 600,\n    VAL 457, VM 221, VP 651), and explained variance differs significantly among them.\n  source: Results, Neural activity explained by movement differs across brain areas, paragraph 5;\n    Figure 3f legend; Supplementary Table 1; Extended Data Fig. 4\n  quote: For seven of the nuclei, we had a sufficient number of recorded neurons for analysis\n    (threshold set at 100 ... Explained variance based on the embedding method varied significantly\n    among nuclei (Fig. 3c,d,f and see Extended Data Fig. 4 for pairwise statistics).\n  statistics:\n  - test: pairwise two-tailed Mann-Whitney U tests with Bonferroni correction (Extended Data Fig. 4)\n    p: 0.1\n    p_relation: \"<\"\n    corrected: Bonferroni\n  expected:\n  - quantity: CN neurons\n    value: 235\n    tolerance: 23.5\n  - quantity: MD neurons\n    value: 1112\n    tolerance: 111.2\n  - quantity: PCN neurons\n    value: 268\n    tolerance: 26.8\n  - quantity: PO neurons\n    value: 600\n    tolerance: 60\n  - quantity: VAL neurons\n    value: 457\n    tolerance: 45.7\n  - quantity: VM neurons\n    value: 221\n    tolerance: 22.1\n  - quantity: VP neurons\n    value: 651\n    tolerance: 65.1\n  criterion: Nuclei as in Supplementary Table 1 (CN is the central lateral and central medial nuclei\n    pooled; VP is the ventral posterior complex with its posterolateral and posteromedial parts and\n    their parvicellular parts). Neurons with trial-average rate above 2 Hz and fivefold\n    cross-validated response-epoch explained variance above 0.01; nuclei with more than 100 such\n    neurons kept (code, Figure4.get_thalamus_nuclei_inds). Reproduced when the same seven nuclei pass\n    the threshold, the counts are within 10%, and at least one pair of nuclei differs in explained\n    variance by two-tailed Mann-Whitney U at Bonferroni-corrected p < 0.05 (21 pairs), with VAL lower\n    than PO, VM and VP as in thalamus-ev-not-rate.\n- id: thalamus-ev-not-rate\n  statement: Differences in explained variance among thalamic nuclei are not explained by spike rate;\n    rates do not differ among PO, VAL, VM and VP, while explained variance in VAL differs from PO,\n    VM and VP.\n  source: Results, Neural activity explained by movement differs across brain areas, paragraph 5;\n    Extended Data Fig. 4\n  quote: Spike rate differences did not explain differences in variance explained (spike rate\n    difference not significant between posterior complex (PO), ventral anterior–lateral complex (VAL),\n    ventral medial nucleus (VM) and ventral posterior complex (VP), P > 0.1, yet variance explained\n    differed significantly between VAL and PO/VM/VP, P < 1 × 10 −3 , one-way F -test between these\n    four nuclei\n  statistics:\n  - about: spike rate across PO, VAL, VM and VP\n    test: one-way F-test\n    p: 0.1\n    p_relation: \">\"\n  - about: explained variance across PO, VAL, VM and VP\n    test: one-way F-test\n    p: 0.001\n    p_relation: \"<\"\n  criterion: Neurons as in fig3f-thalamic-nuclei. One-way ANOVA (F-test) across the four nuclei of\n    trial-average spike rate, and of response-epoch explained variance (code,\n    Figure4.get_barplot_stats). Reproduced when the rate test gives p > 0.1, the explained-variance\n    test gives p < 0.001, and the VAL mean is the lowest of the four. The absence half is judged on\n    the paper's F-test alone.\n  depends_on:\n  - fig3f-thalamic-nuclei\n- id: supfig2-noise-injection\n  statement: The nearest-neighbour smoothness in thalamus survives spatial noise added to the neuron\n    positions, remaining significant up to Gaussian noise of 100 um variance.\n  source: Supplementary Figure 2 legend\n  quote: Differences between shuffle and data are statistically significant up to the injection of\n    Gaussian noise with 100 μm variance (in all three directions) with p=0.003\n  statistics:\n  - test: comparison against shuffle control\n    p: 0.003\n  criterion: As fig3e-nearest-neighbor, after adding independent Gaussian noise to each CCF\n    coordinate, averaged over 20 noise draws. The legend says \"variance\" in micrometres; readings are\n    a standard deviation of 100 um and a variance of 100 um squared (standard deviation 10 um).\n    Reproduced when, under one reading, the data differ from the shuffle at p < 0.05 at that noise\n    level.\n  depends_on:\n  - fig3e-nearest-neighbor\n- id: fig4b-medulla-leads\n  statement: Neurons in the medulla are best predicted by video shifted into the future (activity\n    leads movement), visible both per neuron and in the area average, part of an anterior-posterior\n    pattern across the brain.\n  source: Results, Dissecting putative motor and sensory neural signals, paragraph 2; Figure 4b,c;\n    Extended Data Fig. 5\n  quote: A strong anterior–posterior pattern emerged, with neurons in the medulla having a strong\n    preference for video-shifts into future time points that was also apparent when averaging neurons\n    within brain regions and comparing across brain regions (Fig. 4b )\n  criterion: Methods, Analyzing optimal time-offsets, and code (Figure3). Response epoch, embedding,\n    fivefold cross-validation; the feature window shifted by tau from -102 to +102 ms in steps of\n    6.8 ms (positive tau uses future frames); for each tau the epoch-averaged explained variance;\n    neurons with trial-average rate above 2 Hz, zero-shift explained variance above 0.01, and peak\n    over tau at least 1.2 times the mean over tau. Area curves are each neuron's explained variance\n    normalized to its value at zero shift, averaged over neurons. Reproduced when the medulla curve\n    peaks at a positive shift and medulla has the highest mean best offset and the highest fraction\n    of neurons with positive best offset of the five areas.\n- id: edfig6-offset-ev-correlation\n  statement: Outside the medulla, a neuron's best time offset is positively correlated with its\n    explained variance, so that more motor-related neurons are better predicted; in medulla the\n    correlation is not significant.\n  source: Results, Dissecting putative motor and sensory neural signals, paragraph 2; Extended Data\n    Fig. 6 legend\n  quote: We observed that the best time-offset was positively correlated with the explained variance\n    of the neurons (Extended Data Fig. 6 ) with the exception of medulla\n  statistics:\n  - about: medulla\n    test: Spearman rank correlation\n    statistic: R = -0.06\n    p: 0.22\n    corrected: Bonferroni\n    n: 992 neurons\n  - about: midbrain\n    test: Spearman rank correlation\n    statistic: R = 0.17\n    p: 6.0e-12\n    corrected: Bonferroni\n    n: 1,702 neurons\n  - about: ALM\n    test: Spearman rank correlation\n    statistic: R = 0.22\n    p: 2.0e-12\n    corrected: Bonferroni\n    n: 1,059 neurons\n  - about: striatum\n    test: Spearman rank correlation\n    statistic: R = 0.15\n    p: 3.0e-07\n    corrected: Bonferroni\n    n: 1,171 neurons\n  - about: thalamus\n    test: Spearman rank correlation\n    statistic: R = 0.13\n    p: 5.0e-12\n    corrected: Bonferroni\n    n: 2,881 neurons\n  expected:\n  - quantity: medulla Spearman R\n    value: -0.06\n    tolerance: 0.006\n  - quantity: midbrain Spearman R\n    value: 0.17\n    tolerance: 0.017\n  - quantity: ALM Spearman R\n    value: 0.22\n    tolerance: 0.022\n  - quantity: striatum Spearman R\n    value: 0.15\n    tolerance: 0.015\n  - quantity: thalamus Spearman R\n    value: 0.13\n    tolerance: 0.013\n  - quantity: medulla neurons\n    value: 992\n    tolerance: 99.2\n  - quantity: midbrain neurons\n    value: 1702\n    tolerance: 170.2\n  - quantity: ALM neurons\n    value: 1059\n    tolerance: 105.9\n  - quantity: striatum neurons\n    value: 1171\n    tolerance: 117.1\n  - quantity: thalamus neurons\n    value: 2881\n    tolerance: 288.1\n  criterion: Neurons and offsets as in fig4b-medulla-leads; the best offset is the arg max of the\n    fold-averaged explained variance over tau; Spearman correlation per area between best offset and\n    zero-shift response-epoch explained variance (code, supp_fig_S6.ipynb, which prints R = -0.064, p\n    = 0.22 for medulla), p times 5. The legend prints the striatum p as \"3e7\", read as 3e-7. The\n    claim holds (reproduced) when medulla has corrected p > 0.1 and the other four areas have positive\n    R with corrected p < 0.001; the R values and counts are judged against their tolerances (10%) and\n    reported. A 10% tolerance on an R of 0.06 is narrow; R within 0.03 of the paper's value with the\n    same significance outcome counts as a match, as the paper prints R to two decimals.\n  depends_on:\n  - fig4b-medulla-leads\n- id: fig5a-somatosensory-vs-alm\n  statement: Somatosensory cortex neurons follow movement (mean best offset -12.8 ms) while ALM neurons\n    lead it (8.7 ms), and the two distributions differ.\n  source: Results, Dissecting putative motor and sensory neural signals, paragraph 3; Figure 5a\n  quote: somatosensory areas mean time-offset, −12.8 ± 1.1 ms s.e.m., n = 870 neurons; ALM mean\n    time-offset, 8.7 ± 1.5 ms s.e.m., n = 1,059 neurons; the two distributions are different at P <\n    0.0001, one-sided Mann–Whitney U test\n  statistics:\n  - test: one-sided Mann-Whitney U test\n    p: 0.0001\n    p_relation: \"<\"\n    n: 870 somatosensory and 1,059 ALM neurons\n  expected:\n  - quantity: somatosensory mean best offset\n    value: -12.8\n    tolerance: 1.1\n    unit: ms\n  - quantity: ALM mean best offset\n    value: 8.7\n    tolerance: 1.5\n    unit: ms\n  - quantity: somatosensory neurons\n    value: 870\n    tolerance: 87\n  - quantity: ALM neurons\n    value: 1059\n    tolerance: 105.9\n  criterion: Tolerances on the means are the s.e.m. given. Neurons as in fig4b-medulla-leads;\n    somatosensory areas is the Allen structure of that name without ALM neurons. How a neuron's best\n    offset is formed is open. Readings. (a) The tau that maximizes the fold-averaged explained\n    variance (Methods). (b) The mean over the five folds of each fold's best tau (the code,\n    fig7_plot.ipynb, whose printed means match the paper's -12.8, 8.7, -11.6, 5.8, 0.0 and 19.3 ms\n    under this reading). Test as the paper states, one-sided Mann-Whitney U (somatosensory lower),\n    with a Bonferroni factor of 3 (the three pairs reported) or 4 (the code's four pairs, which add\n    sensory medulla against gigantocellular nucleus); the code's two-sided test is a variant.\n    Reproduced when, under one reading, both means and counts are within tolerance and p < 0.0001.\n  depends_on:\n  - fig4b-medulla-leads\n- id: fig5b-po-vs-vm\n  statement: In thalamus, the sensory nucleus PO follows movement (mean best offset -11.6 ms) and the\n    motor nucleus VM leads it (5.8 ms).\n  source: Results, Dissecting putative motor and sensory neural signals, paragraph 3; Figure 5b\n  quote: sensory thalamus PO followed movement (mean time-offset, −11.6 ± 1.4 ms s.e.m., n = 516\n    neurons) and motor thalamus VM led movement (mean time-offset, 5.8 ± 3.4 ms s.e.m., n = 134\n    neurons)\n  statistics:\n  - test: one-sided Mann-Whitney U test\n    p: 0.001\n    p_relation: \"<\"\n    corrected: Bonferroni\n    n: 516 PO and 134 VM neurons\n  expected:\n  - quantity: PO mean best offset\n    value: -11.6\n    tolerance: 1.4\n    unit: ms\n  - quantity: VM mean best offset\n    value: 5.8\n    tolerance: 3.4\n    unit: ms\n  - quantity: PO neurons\n    value: 516\n    tolerance: 51.6\n  - quantity: VM neurons\n    value: 134\n    tolerance: 13.4\n  criterion: As fig5a-somatosensory-vs-alm (same readings for the offset and the correction), PO and\n    VM as Allen structures. Reproduced when, under one reading, both means and counts are within\n    tolerance and the corrected one-sided p < 0.001.\n  depends_on:\n  - fig5a-somatosensory-vs-alm\n- id: fig5c-pretectal-vs-scm\n  statement: In midbrain, the pretectal region has a mean best offset near zero (0.0 ms) and the\n    motor-related superior colliculus leads movement (19.3 ms).\n  source: Results, Dissecting putative motor and sensory neural signals, paragraph 3; Figure 5c\n  quote: In midbrain (Fig. 5c ), we found a significant difference between pretectal region (mean\n    time-offset, 0.0 ± 2.8 ms s.e.m., n = 203) and motor-related superior colliculus (mean\n    time-offset, 19.3 ± 1.8 ms s.e.m., n = 612)\n  statistics:\n  - test: one-sided Mann-Whitney U test\n    p: 0.001\n    p_relation: \"<\"\n    corrected: Bonferroni\n    n: 203 pretectal and 612 superior colliculus neurons\n  expected:\n  - quantity: pretectal mean best offset\n    value: 0.0\n    tolerance: 2.8\n    unit: ms\n  - quantity: superior colliculus, motor related, mean best offset\n    value: 19.3\n    tolerance: 1.8\n    unit: ms\n  - quantity: pretectal neurons\n    value: 203\n    tolerance: 20.3\n  - quantity: superior colliculus neurons\n    value: 612\n    tolerance: 61.2\n  criterion: As fig5a-somatosensory-vs-alm, with the Allen structures pretectal region and superior\n    colliculus, motor related. Reproduced when, under one reading, both means and counts are within\n    tolerance and the corrected one-sided p < 0.001.\n  depends_on:\n  - fig5a-somatosensory-vs-alm\n- id: fig5-significant-offsets\n  statement: Within each area, neurons have heterogeneous best offsets, and some neurons' offsets\n    differ significantly from zero.\n  source: Results, Dissecting putative motor and sensory neural signals, paragraph 3; Figure 5 legend;\n    Methods, Analyzing optimal time-offsets\n  quote: Neurons within each brain area had heterogeneous video-activity shift preference (Fig. 5 ),\n    suggesting rich encoding of movement.\n  criterion: Methods. For each neuron of the six areas of Fig. 5, the best offsets of the five folds\n    tested against zero with a one-sample t-test; Benjamini-Hochberg control at Q = 0.05 within each\n    area (the code's final figure uses Q = 0.01, a variant). Reproduced when every one of the six\n    areas has neurons with significantly positive and neurons with significantly negative offsets,\n    or, failing that, best offsets spanning both signs with at least one significant neuron in each\n    area. With five folds the t-test has 4 degrees of freedom and offsets that are equal in all folds\n    give an undefined t; such neurons are counted as not tested, and their number is reported.\n  depends_on:\n  - fig5a-somatosensory-vs-alm\n- id: fig4e-alm-depth\n  statement: Within ALM, best time offset increases with cortical depth, from sensory-like (following)\n    signals superficially to motor-like (leading) signals in deeper layers.\n  source: Results, Dissecting putative motor and sensory neural signals, paragraph 4; Figure 4d,e\n    legend\n  quote: Spearman rank correlation between cortical depth and best time-offset is R = 0.1, P = 0.0014,\n    n = 1,059 neurons.\n  statistics:\n  - test: Spearman rank correlation\n    statistic: R = 0.1\n    p: 0.0014\n    n: 1,059 neurons\n  expected:\n  - quantity: Spearman R, ALM depth against best offset\n    value: 0.1\n    tolerance: 0.01\n  criterion: ALM neurons as in fig5a-somatosensory-vs-alm. Depth is the distance along the\n    dorsal-ventral CCF axis from the most dorsal ALM neuron (code, Figure3.get_alm_depth_stats with\n    angle 0, which prints R = 0.098, p = 0.00139, n = 1059), and the best offset is reading (a) of\n    fig5a (the arg max of the fold-averaged curve), as in that code. Reproduced when R > 0 with p <\n    0.01 (the main text's threshold) and R is within 0.01 of 0.1; partially reproduced when R > 0 and\n    p < 0.01 but R is outside tolerance.\n  depends_on:\n  - fig5a-somatosensory-vs-alm\n- id: fig6a-choice-from-video\n  statement: Single-trial choice can be decoded from video; at chance before the sample epoch (AUC\n    0.51), above chance in the sample and delay epochs (0.66) before any instructed movement, and\n    near perfect after the go cue (0.99).\n  source: Results, Analyzing and interpreting uninstructed movements, paragraph 1; Figure 6a,b\n  quote: We found that before the sample epoch, predictions of choice were at chance (area under the\n    curve (AUC) of receiver operating characteristic (ROC) was 0.51 ± 0.06 s.d., n = 106 sessions\n    ... In the sample and delay epochs, the mean AUC increased significantly (0.66 ± 0.12 s.d., n =\n    106 sessions ... (0.99 ± 0.01 s.d., n = 106 sessions, mean AUC ROC of the second half of response\n    epoch)\n  expected:\n  - quantity: AUC before sample epoch, mean over sessions\n    value: 0.51\n    tolerance: 0.06\n  - quantity: AUC, second half of sample epoch and delay epoch, mean over sessions\n    value: 0.66\n    tolerance: 0.12\n  - quantity: AUC, second half of response epoch, mean over sessions\n    value: 0.99\n    tolerance: 0.01\n  - quantity: sessions\n    value: 106\n    tolerance: 10.6\n  criterion: Tolerances are the session s.d. the paper gives (the stated spread). Correct trials only,\n    20-fold stratified cross-validation (Methods, Trial selection), embedding features, ROC AUC of the\n    test predictions per time bin. The decoder is not described and its code is not public. Readings\n    for the decoder. (a) L2 logistic regression with the penalty chosen by nested cross-validation,\n    on the 80-dimensional five-frame embedding window at each time bin (the features of the\n    paper's activity prediction; the authors' output files carry a \"nbr5\" key); (b) the same on the\n    16-dimensional embedding of the single frame. Readings for the pre-sample window. (a) all bins\n    before sample onset in the analysed window (the code's window starts 3 s before the go cue,\n    so -3 to -1.85 s); (b) the last 0.5 s before sample onset. The \"significant\" increase has no\n    named test; it is judged by a paired Wilcoxon signed-rank test of the session values, sample and\n    delay against pre-sample, at p < 0.05. Reproduced when, under one pair of readings, the three\n    means are within tolerance and the increase is significant.\n- id: fig6d-mouse-clustering\n  statement: Choice predictability from video during the sample epoch varies widely across sessions\n    but less within mice than across mice; sessions of the same mouse cluster.\n  source: Results, Analyzing and interpreting uninstructed movements, paragraph 2; Figure 6b-d; Methods,\n    Calinski-Harabasz clustering score\n  quote: Variability in predictability of actions from video was smaller within mice than across mice,\n    consistent with the notion that individual animals adopted relatively consistent uninstructed\n    movements (Fig. 6d , Calinski–Harabasz clustering score 41 for clustering of within-animal points\n    10.45, compared with null model value of 1.02 ± 0.37 s.d.\n  statistics:\n  - test: Calinski-Harabasz score against a permutation null (1,000 label shuffles)\n    statistic: CH = 10.45, null 1.02 ± 0.37 s.d.\n    p: 0.001\n    p_relation: \"<\"\n  expected:\n  - quantity: Calinski-Harabasz score, mouse labels\n    value: 10.45\n    tolerance: 1.045\n  - quantity: null mean Calinski-Harabasz score\n    value: 1.02\n    tolerance: 0.37\n  criterion: Methods. Feature, each session's embedding-based choice AUC in the sample epoch (Fig. 6d\n    axis label); clusters, mouse identity; sklearn calinski_harabasz_score; null, 1,000 random\n    reassignments of the mouse labels; p is the fraction of null scores at or above the observed.\n    Decoder as in fig6a-choice-from-video. The Methods' note that only sessions with jaw or nose AUC\n    of at least 0.65 and mice with two or more such sessions were used follows the Fig. 6e sentence;\n    readings are (a) the filter applies only to Fig. 6e and Fig. 6d uses all sessions, (b) it applies\n    to both. Reproduced when, under one reading, the score is within tolerance and p < 0.001;\n    partially reproduced when p < 0.001 but the score is outside tolerance.\n  depends_on:\n  - fig6a-choice-from-video\n- id: fig6-marker-vs-embedding-decoding\n  statement: Single markers predict choice less well than the full-video embedding in the response\n    epoch (AUC 0.88 against 0.96).\n  source: Results, Analyzing and interpreting uninstructed movements, paragraph 4\n  quote: Despite the weaker predictive power of single markers (response epoch ... 0.88 ± 0.01 s.e.m.,\n    n = 106 sessions; embedding ... 0.96 ± 0.00 s.e.m., n = 106, P < 1 × 10 −6 , n = 106 sessions)\n  statistics:\n  - test: not named\n    p: 1.0e-06\n    p_relation: \"<\"\n    n: 106 sessions\n  expected:\n  - quantity: marker response-epoch choice AUC\n    value: 0.88\n    tolerance: 0.01\n  - quantity: embedding response-epoch choice AUC\n    value: 0.96\n    tolerance: 0.005\n  criterion: Tolerances are the s.e.m. given; the embedding s.e.m. is printed as 0.00, and half the\n    last printed digit (0.005) is used. Decoder readings as fig6a-choice-from-video. Open details and\n    their readings. The response-epoch window, (a) the whole response epoch (this sentence prints 0.96\n    for the embedding, against 0.99 for the second half in fig6a) or (b) its second half. The marker\n    features, (a) the jaw and nose markers each alone, taking the better per session, (b) the jaw\n    alone, (c) all three markers together. The test, a paired Wilcoxon signed-rank test over sessions\n    (as in Fig. 2), or a paired t-test. Reproduced when, under one combination, both means are within\n    tolerance and p < 1e-6 with the embedding higher; partially reproduced when the embedding is\n    significantly higher but a mean falls outside tolerance.\n  depends_on:\n  - fig6a-choice-from-video\n- id: fig6e-marker-clustering\n  statement: With single markers the mouse-specific structure of uninstructed movements remains; for\n    some mice the nose is more informative than the jaw and for others the jaw more than the nose.\n  source: Results, Analyzing and interpreting uninstructed movements, paragraph 4; Figure 6e\n  quote: the heterogeneity of uninstructed trial-related movements across mice was still present (Fig.\n    6e , Calinski–Harabasz clustering score for clustering of within-animal points 12.57, compared with\n    null model value of 1.05 ± 0.54 s.d.\n  statistics:\n  - test: Calinski-Harabasz score against a permutation null (1,000 label shuffles)\n    statistic: CH = 12.57, null 1.05 ± 0.54 s.d.\n    p: 0.001\n    p_relation: \"<\"\n  expected:\n  - quantity: Calinski-Harabasz score, nose and jaw AUCs, mouse labels\n    value: 12.57\n    tolerance: 1.257\n  - quantity: null mean Calinski-Harabasz score\n    value: 1.05\n    tolerance: 0.54\n  criterion: Methods. Features, per session the delay-epoch choice AUC from the nose marker alone and\n    from the jaw marker alone (two dimensions); clusters, mouse identity; only sessions with jaw or\n    nose AUC of at least 0.65 and mice with two or more such sessions; null and p as in\n    fig6d-mouse-clustering. Decoder readings as fig6a-choice-from-video, applied to the marker\n    positions. Reproduced when the score is within tolerance and p < 0.001, and both kinds of mice\n    occur (some with nose AUC above jaw AUC in most of their sessions, some the reverse).\n  depends_on:\n  - fig6a-choice-from-video\n- id: edfig7-performance-correlation\n  statement: Choice-related preparatory movements in the sample and delay epochs are positively\n    correlated with the animal's task performance in the session.\n  source: Results, Analyzing and interpreting uninstructed movements, paragraph 4; Extended Data Fig. 7\n  quote: we found that such task-related preparatory movements during sample and delay epochs were\n    positively correlated with the animal’s performance on a given session ( r = 0.33, n = 106\n    sessions, P < 0.001; Extended Data Fig. 7 and Methods )\n  statistics:\n  - test: correlation (r)\n    statistic: r = 0.33\n    p: 0.001\n    p_relation: \"<\"\n    n: 106 sessions\n  expected:\n    quantity: correlation of video choice AUC with session performance\n    value: 0.33\n    tolerance: 0.033\n  criterion: Per session, the mean embedding-based choice AUC and the fraction of correct trials among\n    the paper's included trials. The Methods referred to do not describe this analysis. Readings for\n    the AUC, (a) the delay epoch (Extended Data Fig. 7 legend), (b) the second half of the sample\n    epoch and the delay epoch (as in fig6a). Readings for r, Pearson (the symbol r) or Spearman.\n    Reproduced when, under one reading, r is within tolerance and p < 0.001; partially reproduced when\n    r > 0 with p < 0.001 but outside tolerance.\n  depends_on:\n  - fig6a-choice-from-video\n- id: fig7b-jaw-differs\n  statement: Within a choice, trials with different video predictions differ in behaviour; delay-epoch\n    jaw height differs between R-vR and R-vL in 56 of 80 sessions and between L-vR and L-vL in 56 of\n    80 sessions.\n  source: Results, Activity related to uninstructed movement and decision-making, paragraph 2; Figure 7b\n  quote: jaw height was significantly different across same choice groups with different video\n    predictions in most sessions (Fig. 7b , significantly differentiated R-vR versus R-vL in 56 of 80\n    sessions and in 56 of 80 sessions for L-vR versus L-vL, P < 0.05; only sessions with moderate and\n    higher behavioral predictability were chosen for this analysis, defined as AUC > 0.6\n  expected:\n  - quantity: sessions with R-vR and R-vL jaw height different\n    value: 56\n    tolerance: 5.6\n  - quantity: sessions with L-vR and L-vL jaw height different\n    value: 56\n    tolerance: 5.6\n  - quantity: sessions with video choice AUC above 0.6\n    value: 80\n    tolerance: 8\n  criterion: Correct trials split by choice and by the delay-epoch single-trial video prediction (vL or\n    vR) from the decoder of fig6a-choice-from-video. The cut that assigns a trial to vL or vR is not\n    given; the standard reading is the predicted class (probability 0.5), with the test-fold\n    prediction for each trial. Sessions with delay-epoch AUC above 0.6 (the authors' AUC notebook\n    prints 80 of 106 effective sessions). Per session, mean jaw height (vertical position of the jaw\n    marker) over the delay epoch per trial, compared between the two video groups within each choice\n    at p < 0.05; the test is not named, readings are a two-sided Mann-Whitney U test and a two-sided\n    Welch t-test. Reproduced when, under one reading, both counts are within tolerance. The 80\n    sessions are reported against the paper's count.\n  depends_on:\n  - fig6a-choice-from-video\n- id: fig7c-modulation-nonuniform\n  statement: The proportions of choice-modulated and uninstructed movement-modulated neurons, and the\n    relative strength of the two kinds of modulation, vary across the brain, although the two types\n    are intermingled within each area.\n  source: Results, Activity related to uninstructed movement and decision-making, paragraph 3; Figure\n    7c,d; Extended Data Fig. 9\n  quote: The relative proportions of choice-modulated and uninstructed movement-modulated neurons varied\n    across the brain (Fig. 7c,d and Extended Data Fig. 9 ; AUC test against spatial uniformity, P <\n    0.001), but the two types of neurons were spatially intermingled within each area.\n  statistics:\n  - about: choice AUC and uninstructed movement AUC\n    test: test against spatial uniformity (one-way F across 0.5 mm voxels, shuffle null)\n    p: 0.001\n    p_relation: \"<\"\n  - about: difference of choice and uninstructed movement AUC\n    test: test against spatial uniformity\n    p: 0.001\n    p_relation: \"<\"\n  criterion: Single-neuron AUCs as in fig7d-alm-midbrain-vs-medulla. Methods, Test against spatial\n    uniformity, with 0.5 mm voxels and 10,000 shuffles (the code ran 1,000, a variant); applied to the\n    choice AUC, the movement AUC and their difference (code, fig6_plot_clean.ipynb). Reproduced when\n    all three give p < 0.001. \"Intermingled\" is not tested by the paper and is reported only (the\n    fraction of 0.5 mm voxels with at least ten neurons that hold both a choice-modulated and a\n    movement-modulated neuron).\n  depends_on:\n  - fig7d-alm-midbrain-vs-medulla\n- id: fig7d-alm-midbrain-vs-medulla\n  statement: ALM and midbrain neurons are more often choice-modulated relative to uninstructed\n    movement-modulated than medulla neurons (ratio of choice- to movement-modulated neurons, ALM 4.8,\n    midbrain 4.3, medulla 1.2).\n  source: Results, Activity related to uninstructed movement and decision-making, paragraph 3; Figure 7d\n  quote: ALM and midbrain neurons were more likely to be choice-modulated than medulla neurons\n    (proportion of choice- to uninstructed movement-modulated neurons, ALM 4.8 versus medulla 1.2, P <\n    0.001; midbrain 4.3 versus medulla 1.2, P < 0.001, binomial test with Bonferroni correction)\n  statistics:\n  - about: ALM against medulla\n    test: binomial test\n    p: 0.001\n    p_relation: \"<\"\n    corrected: Bonferroni\n  - about: midbrain against medulla\n    test: binomial test\n    p: 0.001\n    p_relation: \"<\"\n    corrected: Bonferroni\n  expected:\n  - quantity: ALM ratio of choice- to movement-modulated neurons\n    value: 4.8\n    tolerance: 0.48\n  - quantity: midbrain ratio\n    value: 4.3\n    tolerance: 0.43\n  - quantity: medulla ratio\n    value: 1.2\n    tolerance: 0.12\n  - quantity: sessions in Fig. 7d\n    value: 87\n    tolerance: 8.7\n  criterion: Methods, Defining choice- and uninstructed movement-modulated neurons. Correct trials in\n    four groups (L-vL, L-vR, R-vR, R-vL) from the delay-epoch video prediction (fig7b-jaw-differs);\n    sessions with fewer than 20 trials in any group excluded. Per neuron, delay-epoch mean rate\n    (-1.2 to 0 s); choice AUC is the test-fold ROC AUC of a regularized classifier separating L from R\n    within vL and within vR, averaged over the two; movement AUC likewise separates vL from vR within L\n    and within R; 20-fold cross-validation, AUC averaged over folds. Classifier, regularized logistic\n    regression with the penalty from nested leave-one-out cross-validation (Methods); the code uses\n    RidgeClassifierCV with balanced class weights and 20 random folds, a variant. A neuron is choice-\n    (movement-) modulated when its choice (movement) AUC is at least 0.65 and the other is below\n    0.65; the ratio is the count of choice-only over movement-only neurons (code,\n    get_medulla_alm_fraction_stats, which prints medulla 171/142, ALM 710/148, midbrain 678/159).\n    Test (code), two-sided binomial test of medulla's choice-only count out of its choice-only plus\n    movement-only count against the pooled proportion of the two areas compared, p times 2.\n    Reproduced when the three ratios are within tolerance and both corrected p < 0.001.\n  depends_on:\n  - fig7b-jaw-differs\n- id: edfig10-subtraction-consistent\n  statement: Subtracting the video-predicted activity and reassessing choice selectivity gives results\n    largely consistent with the trial-grouping approach.\n  source: Results, Activity related to uninstructed movement and decision-making, paragraph 3; Extended\n    Data Fig. 10; Methods, Defining choice-modulated neurons after subtraction of movement-related\n    activity\n  quote: We also tested a different approach, predicting and then subtracting movement-related neural\n    activity, followed by reassessing choice selectivity, and found largely consistent results\n    (Extended Data Fig. 10 ).\n  criterion: Methods. Per neuron, the embedding-predicted rate (fivefold cross-validated, zero shift)\n    subtracted at each time bin; delay-epoch mean residual; regularized logistic regression of choice\n    with fivefold cross-validation and nested selection of the penalty (code, functions_for_r2.calculate_auc,\n    C in 0.01, 0.1, 1, 10, 100); choice-modulated when AUC > 0.65. The paper gives no measure of\n    consistency; the one fixed here, from Extended Data Fig. 10c, is that in each of the six areas of\n    Fig. 7d the fraction classified choice-modulated after subtraction is higher among the\n    trial-grouping choice-modulated neurons than among the trial-grouping movement-modulated\n    neurons. Reproduced when this holds in at least five of the six areas; partially reproduced in\n    three or four. The Spearman correlation of the two choice AUCs across neurons is reported.\n  depends_on:\n  - fig7d-alm-midbrain-vs-medulla\n- id: supp-session-independent-autoencoder\n  statement: A session-independent encoder trained on 40 sessions predicts activity much better than\n    markers in both training and held-out sessions and slightly worse than session-specific\n    autoencoders.\n  source: Supplementary Discussion, Session-independent auto-encoder; Methods, Convolutional\n    autoencoder\n  quote: In both training set and hold-out set, the session-independent auto-encoder’s performance is\n    much better than that of using the markers (in the training sessions exp. var. difference 18.2%\n    +/- 1.2% sem, n=122 recordings, p<0.001. In the hold-out sessions difference 16.5% +/- 1.1% sem,\n    n=192 recordings, p<0.001), though it’s slightly worse than that of the session-dependent (in the\n    training sessions exp. var. difference 3.6% +/- 1.1% sem, n=122 recordings, p<0.001. In the\n    hold-out sessions, difference 12.8% +/- 3.0% sem, n=192 recordings, p<0.001)\n  statistics:\n  - about: session-independent against markers, training sessions\n    test: not named\n    p: 0.001\n    p_relation: \"<\"\n    n: 122 recordings\n  - about: session-independent against markers, held-out sessions\n    test: not named\n    p: 0.001\n    p_relation: \"<\"\n    n: 192 recordings\n  - about: session-dependent against session-independent, training sessions\n    test: not named\n    p: 0.001\n    p_relation: \"<\"\n    n: 122 recordings\n  - about: session-dependent against session-independent, held-out sessions\n    test: not named\n    p: 0.001\n    p_relation: \"<\"\n    n: 192 recordings\n  expected:\n  - quantity: explained variance difference, independent minus markers, training sessions\n    value: 18.2\n    tolerance: 1.2\n    unit: percent\n  - quantity: explained variance difference, independent minus markers, held-out sessions\n    value: 16.5\n    tolerance: 1.1\n    unit: percent\n  - quantity: explained variance difference, dependent minus independent, training sessions\n    value: 3.6\n    tolerance: 1.1\n    unit: percent\n  - quantity: explained variance difference, dependent minus independent, held-out sessions\n    value: 12.8\n    tolerance: 3.0\n    unit: percent\n  criterion: One or two sessions from each of the 22 mice (40 sessions) train a shared encoder with\n    session-specific linear decoders; the other 60 sessions are held out; embeddings predict rates by\n    ridge regression as for the session-specific embedding. Open details. Which sessions are trained\n    on (a random choice is the standard; the result is reported for one seed); what a \"recording\" is\n    (readings, one probe insertion of a session, or one area of a session); and whether the\n    difference is relative (percent of the marker value, as in fig2e) or absolute (explained variance\n    points times 100). Test, a paired Wilcoxon signed-rank test over recordings (as in Fig. 2), at\n    p < 0.001. Reproduced when, under one reading, the four differences are positive with p < 0.001\n    and within tolerance; partially reproduced when the signs and significance hold but values fall\n    outside tolerance. Training settings of the encoder are not in the paper or the code read and are\n    open; the author states those used.\n  depends_on:\n  - fig2e-method-improvement\n"
}
```

```
File created successfully at: claims/wang-2025.yaml (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd  python tools/claims_check.py claims/wang-2025.yaml paper/10.1038-s41593-025-02114-x.txt; echo exit=$?
```

Result: not kept, because it reads the paper's text.

**Agent**

The supplement text carries line numbers between lines, so quotes there need cuts. Fixing those two.

**Agent calls Bash**

```bash
cd  grep -n -A1 "Differences between shuffle\|significant up to the\|In both training set\|auto-encoder’s performance\|sessions exp. var. difference\|hold-out sessions difference\|it’s slightly worse\|difference 12.8" paper/10.1038-s41593-025-02114-x.txt | cat -A | cut -c1-140 | head -30
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  python - <<'EOF'
p='claims/wang-2025.yaml'
s=open(p).read()
old_a=s[s.index("  quote: Differences between shuffle"):s.index("  statistics:\n  - test: comparison against shuffle control")]
new_a="""  quote: Differences between shuffle and data are statistically ... significant up to the injection
    of Gaussian noise with 100 μm variance (in all three directions) ... with p=0.003
"""
s=s.replace(old_a,new_a)
old_b=s[s.index("  quote: In both training set and hold-out set"):s.index("  statistics:\n  - about: session-independent against markers, training sessions")]
new_b="""  quote: In both training set and hold-out set, the session-independent ... auto-encoder’s
    performance is much better than that of using the markers (in the training ... sessions exp. var.
    difference 18.2% +/- 1.2% sem, n=122 recordings, p<0.001. In the ... hold-out sessions difference
    16.5% +/- 1.1% sem, n=192 recordings, p<0.001), though ... it’s slightly worse than that of the
    session-dependent (in the training sessions exp. var. ... difference 12.8% +/- 3.0% sem, n=192
    recordings, p<0.001)
"""
s=s.replace(old_b,new_b)
open(p,'w').write(s)
EOF
sed -n 283p paper/10.1038-s41593-025-02114-x.txt; python tools/claims_check.py claims/wang-2025.yaml paper/10.1038-s41593-025-02114-x.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  grep -n -i "rather\|—" claims/wang-2025.yaml; python - <<'EOF'
import yaml
d=yaml.safe_load(open('claims/wang-2025.yaml'))
print(len(d['claims']), sum('quote' in c for c in d['claims']), sum('statistics' in c for c in d['claims']), sum('criterion' in c for c in d['claims']), sum('expected' in c for c in d['claims']))
EOF
# plain scalars with ': ' — scan raw lines that are not comments and whose value part contains ': '
python - <<'EOF'
import re
for i,l in enumerate(open('claims/wang-2025.yaml'),1):
    if l.lstrip().startswith('#'): continue
    m=re.match(r'^(\s*-?\s*[a-z_]+:\s)(.*)$',l)
    body=m.group(2) if m else l.strip()
    if ': ' in body and not body.startswith(('"',"'")): print(i,l.rstrip())
EOF
```

```
29 29 21 29 19
```

**Agent calls Bash**

```bash
cd  git status --short
```

```
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
?? claims/wang-2025.yaml
?? scripts
```

**Agent**

I've written `claims/wang-2025.yaml` with 29 claims. The quote checker passes except for one value. The striatum p-value in the Extended Data Fig. 6 legend is printed as "p = 3e7". A p-value can't be above 1, so I recorded it as 3e-07, and the criterion says so.

**Text read**
- The version of record (Nature Neuroscience, 18 Nov 2025): main text, figure legends, Methods and the Extended Data legends.
- The Supplementary Information PDF, read from its extracted text: the session-independent autoencoder section, Supplementary Table 1 and Supplementary Figs. 1–2.
- Nothing the results rest on is missing. I did not read the Reporting Summary or the Supplementary Videos.

**Code read**
- `druckmann-lab/MapVideoAnalysis` at commit 7d276243. It settles most details, including the region groupings, filters, epoch windows, Bonferroni factors, ridge penalties, the 64-trial split and how the improvement percentages are computed.
- The deep-network repository `kurgyis/BehaviorVideo` could not be fetched: the clone asked for login, so it is private or gone.
- The code that decodes choice from video (all of Fig. 6, and the single-trial labels Fig. 7 uses) is in neither repository. MapVideoAnalysis only reads its precomputed output.
- Some of the code's printed outputs don't match the paper. The method improvements print as 174/377/83% against the paper's 155/330/76%. The claims keep the paper's numbers.

**Counts**
- 29 claims; 29 have quotes, so none needed an `inferred` note.
- 21 have statistics; all 29 have criteria; 19 have expected values.
- Everything is `data: dataset`, since the paper says all its data are on DANDI. Whether the dandiset holds the raw video is for the author to find. If it doesn't, the authors' outside deposits are named as the alternative input: processed data on Zenodo (10.5281/zenodo.16740783) and an unpinned Google Drive folder of embeddings.

**Details left open, and the readings named for each**
- **Fig. 5 time offsets:**
  - A neuron's best offset is either the arg max of the fold-averaged curve (the Methods' wording) or the mean of each fold's best offset (the code; its printed means match the paper's).
  - The Bonferroni factor is ×3 or ×4.
  - The code runs the test two-sided; that is named as a variant of the paper's one-sided test.
  - The FDR threshold is Q = 0.05 (Methods), with the code's 0.01 as a variant.
- **Fig. 6 decoder:** either L2 logistic regression on the 5-frame embedding window, or on a single frame. The pre-sample window is either all bins before sample onset (−3 to −1.85 s) or the last 0.5 s. The test behind "increased significantly" isn't named.
- **Fig. 6d clustering:** the session filter in the Methods either applies only to Fig. 6e or to both 6d and 6e.
- **Marker vs embedding decoding (0.88 vs 0.96):**
  - Window: the whole response epoch or its second half.
  - Marker features: the better of jaw or nose, jaw alone, or all three markers.
  - Test: Wilcoxon signed-rank or paired t-test.
- **Correlation with performance (r = 0.33):** the AUC from the delay epoch or from the sample plus delay epochs; Pearson or Spearman.
- **Fig. 7b jaw height:** the test isn't named; Mann–Whitney or Welch t-test. The vL/vR cut is taken as the predicted class.
- **Fig. 7 classifier:** logistic regression with leave-one-out penalty selection (Methods), with the code's RidgeClassifierCV as a variant. The uniformity test uses 10,000 shuffles (Methods), with the code's 1,000 as a variant.
- **Extended Data Fig. 1 (196 neurons):** whether it uses the single split or the cross-validated values.
- **Supplementary Fig. 2:** the noise level "100 µm variance" is read as either a standard deviation of 100 µm or a variance of 100 µm².
- **Session-independent autoencoder:** what a "recording" is (one probe insertion, or one area of a session); whether the difference is relative or absolute; which sessions are trained on; and the test.
- **Network training settings** for the end-to-end network and the autoencoder are in neither the paper nor the code read; the author will state the ones used.
- **Fig. 2 method comparison:** the code's neuron filter (0.005) is named against the Methods' 0.01.
- **Extended Data Fig. 10:** the paper gives no measure of "largely consistent", so I set one from panel c.
- **Fig. 2 ordering across methods:** whether it means the strict order of all five areas or only medulla first and thalamus last.

**Missing from the paper**
- The video choice decoder: its method and code (affects all Fig. 6 claims and the Fig. 7 trial groups).
- The training settings for the deep networks.
- The main text prints the medulla s.e.m. as 0.06; Extended Data Fig. 3 shows it should be 0.006.
- Animal counts disagree: 28 mice in the Methods, 22 in the Supplement.
- The tracked markers disagree: jaw, nose and tongue in the Results, jaw, paws and tongue in the Methods.

## End of run

48 turns, 8 minutes, $3.99 at API prices, result: success.
