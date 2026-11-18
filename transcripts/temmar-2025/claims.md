# temmar-2025 · claims · run 43198101326

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  grep -n "^#" docs/protocol.md | head -50; ls paper/ claims/; wc -c paper/*
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  sed -n 1,200p docs/protocol.md
```

```
# Protocol for an attempt

Version: `pilot-14`. Record this version in the attempt's provenance.

This is what agents, or people, do to attempt a target and deposit the
result. A target is a dataset in a public archive and a paper it names. How
each archive's datasets are named, versioned and read is in
[archives.md](archives.md); the examples here are from DANDI, the first. It is written from the pilot attempts
([pilot notes](pilot-notes.md)); the reasons for the rules are there.

An attempt has three roles, each a separate run with a separate context:

- The **reader** reads the paper and writes the claims file: every finding,
  and how each is to be tested, taken from the paper. A second reader checks
  it against the paper. Readers never see the dataset's data.
- The **author** tests the claims on the dataset. It reads the paper to
  understand the claims, but the claims file binds it: it cannot change a
  claim's statement, expected values or criterion. A method detail the file
  lacks it takes from the paper, citing the passage, and it asks a reader
  only when it believes the file misreads the paper.
[... 179 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat claims/fouke-2025.yaml
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
[... 301 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "paper/10.52202-085713-4642.txt"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  grep -n "=== \|Appendix\|^[A-C]\.[0-9]\|^Supplement" paper/10.52202-085713-4642.txt | sed -n 1,200p
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.52202-085713-4642.txt",
 "offset": 1095,
 "limit": 420
}
```

Result: not kept, because it reads the paper's text.

**Agent**

The full text, appendices and supplement are all present. Next I'll skim the checklist section and fetch the linked code.

**Agent calls Bash**

```bash
cd  sed -n 776,1095p paper/10.52202-085713-4642.txt | grep -n -i -B2 -A6 "justification" | grep -v "^\-\-$" | grep -i -A5 "justification" | head -120
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd $TMPDIR && git clone -q https://github.com/chesteklab/LINK_dataset.git && cd LINK_dataset && git log -1 --format='%H %cd' && git ls-files | head -100
```

```
5e1c36a1282f90abb8d96963920a8b1fdd27a6e7 Tue Oct 20 15:27:03 2026 -0400
.gitignore
README.md
__init__.py
data/readme.md
data_plotting/__init__.py
data_plotting/bci_decoding_plots.py
data_plotting/dataset_overview.py
data_plotting/dimensionality_across_days_analysis.py
data_plotting/readme.md
data_plotting/signal_changes_plotter.py
data_plotting/single_channel_tuning.py
data_processing/bci_decoding/__init__.py
data_processing/bci_decoding/data_utils.py
data_processing/bci_decoding/eval_singleday_models.py
data_processing/bci_decoding/eval_singleday_models_multithread.py
data_processing/bci_decoding/eval_singleday_models_multithread_updatenorm.py
data_processing/bci_decoding/lstm.py
data_processing/bci_decoding/metrics.py
data_processing/bci_decoding/nn_utils.py
[... 64 more lines not kept]
```

**Agent**

Code cloned (commit 5e1c36a). Now reading the analysis modules for Figures 2 to 5.

**Agent calls Bash**

```bash
cd $TMPDIR/LINK_dataset; wc -l data_processing/signal_changes/*.py data_plotting/signal_changes_plotter.py data_processing/single_channel_tuning/*.py data_processing/bci_decoding/*.py data_processing/stability/stability/*.py data_processing/continual_learning/*.py data_processing/pop_level_analyses/*.py data_plotting/*.py generate_figures.py; cat data_processing/signal_changes/signal_changes.py
```

```
1 data_processing/signal_changes/__init__.py
   444 data_processing/signal_changes/signal_changes.py
   120 data_processing/signal_changes/signal_utils.py
    87 data_plotting/signal_changes_plotter.py
     2 data_processing/single_channel_tuning/__init__.py
   290 data_processing/single_channel_tuning/tuning_plotter.py
   358 data_processing/single_channel_tuning/tuning_utils.py
     1 data_processing/bci_decoding/__init__.py
    93 data_processing/bci_decoding/data_utils.py
   332 data_processing/bci_decoding/eval_singleday_models.py
   414 data_processing/bci_decoding/eval_singleday_models_multithread.py
   492 data_processing/bci_decoding/eval_singleday_models_multithread_updatenorm.py
    47 data_processing/bci_decoding/lstm.py
    60 data_processing/bci_decoding/metrics.py
   256 data_processing/bci_decoding/nn_utils.py
   208 data_processing/bci_decoding/train_models_singleday.py
   155 data_processing/stability/stability/multiday_eval.py
   145 data_processing/stability/stability/plot_continual_learning_final.py
   121 data_processing/stability/stability/trainer_multiday.py
   152 data_processing/continual_learning/analyze_continual_learning_days.py
[... 459 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/LINK_dataset; cat data_processing/signal_changes/signal_utils.py data_plotting/signal_changes_plotter.py; grep -n "def \|sbp\b\|0.25\|tcr\|> *1\|50\b" utils/data_tools.py | head -60
```

```
import numpy as np
import pandas as pd
import os
import pickle
import glob
import re
from tqdm import tqdm
from datetime import datetime
import ast
from utils.data_tools import *

# # server_dir = "/run/user/1000/gvfs/smb-share:server=cnpl-drmanhattan.engin.umich.edu,share=share/"
# # data_path = os.path.join(server_dir, 'Student Folders','Nina_Gill','data','only_good_days')
# data_path = "Z:\Student Folders\\Nina_Gill\data\only_good_days"
# output_path = "Z:\Student Folders\Hisham_Temmar\\big_dataset\output\signal_quality"


# data_path = "C:\\Files\\UM\\ND\\SFN\\only_good_days"
# output_path = 'C:\\Files\\UM\\ND\\github\\big_nhp_dataset_code\\outputs'
binsize = 20
[... 190 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/LINK_dataset; sed -n 1,358p data_processing/single_channel_tuning/tuning_utils.py
```

```
import pandas as pd
import os
import numpy as np
from scipy import stats
from sklearn.linear_model import LinearRegression
from sklearn.feature_selection import mutual_info_regression
import pickle
import glob
import tqdm
import pdb
import matplotlib.colors as colors
import matplotlib.pyplot as plt
import sys
import matplotlib as mpl
#some basic text parameters for figures
from utils import mpl_config

bin_size = 20
def compute_channel_tuning(neural, full_behavior, velocity_tuning = False):
    if velocity_tuning:
[... 339 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/LINK_dataset; cat data_processing/bci_decoding/train_models_singleday.py data_processing/bci_decoding/metrics.py data_processing/bci_decoding/data_utils.py
```

```
import os
import pickle
import sys
import pandas as pd
import random
import numpy as np
import torch
import time
from sklearn.linear_model import Ridge
from torch.utils.data import DataLoader
from sklearn.preprocessing import StandardScaler
import torch.nn as nn

from lstm import LSTMModel
from data_utils import prep_data_and_split
from nn_utils import FingerDataset, create_optimizer_and_scheduler, train_model, SequenceScaler

"""
Script for training an LSTM and a Ridge Regression model on every day of the dataset.
Models are saved as .pkl files.
[... 343 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/LINK_dataset; sed -n 1,332p data_processing/bci_decoding/eval_singleday_models.py | grep -v "^\s*#" | grep -v "^\s*$" | head -260
```

```
import os
import pickle
import sys
import pandas as pd
import numpy as np
import torch
import time
import datetime
from tqdm import tqdm
from torch.utils.data import DataLoader
from sklearn.preprocessing import StandardScaler
from lstm import LSTMModel
from data_utils import prep_data_and_split
from nn_utils import SequenceScaler, FingerDataset
from metrics import calculate_mse_per_dof, calculate_correlation_per_dof, calculate_r2_per_dof
"""
Script for evaluating all trained models (LSTM and Ridge Regression) on every day of the dataset.
Results are saved as a CSV file with the following columns:
- Train day
- Train dataset type (CO/RD)
[... 188 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/LINK_dataset; grep -n "Scaler\|scaler\|norm\|Day_diff\|100\|abs" data_processing/bci_decoding/eval_singleday_models_multithread*.py | head -40; echo ----; grep -v "^\s*#" data_plotting/bci_decoding_plots.py | grep -v "^\s*$"
```

```
data_processing/bci_decoding/eval_singleday_models_multithread.py:11:from sklearn.preprocessing import StandardScaler
data_processing/bci_decoding/eval_singleday_models_multithread.py:17:from nn_utils import SequenceScaler, FingerDataset
data_processing/bci_decoding/eval_singleday_models_multithread.py:43:MAX_NUM_CLOSE_DAYS = 100
data_processing/bci_decoding/eval_singleday_models_multithread.py:45:# data_folder = '/run/user/1000/gvfs/smb-share:server=cnpl-drmanhattan.engin.umich.edu,share=share/Student Folders/Hisham_Temmar/big_dataset/2_autotrimming_and_preprocessing/preprocessing_092024_no7822nofalcon'
data_processing/bci_decoding/eval_singleday_models_multithread.py:95:def predict_lstm(model, input_scaler, output_scaler, test_neural, device, batch_size=512):
data_processing/bci_decoding/eval_singleday_models_multithread.py:101:        input_scaler: SequenceScaler for neural data
data_processing/bci_decoding/eval_singleday_models_multithread.py:102:        output_scaler: StandardScaler for kinematics data
data_processing/bci_decoding/eval_singleday_models_multithread.py:115:    test_neural_scaled = input_scaler.transform(test_neural)
data_processing/bci_decoding/eval_singleday_models_multithread.py:135:    predictions = output_scaler.inverse_transform(predictions_scaled)
data_processing/bci_decoding/eval_singleday_models_multithread.py:175:    if LIMIT_EVALS_TO_CLOSE_DAYS and np.abs(day_diff) > MAX_NUM_CLOSE_DAYS:
data_processing/bci_decoding/eval_singleday_models_multithread.py:180:        lstm_model, input_scaler, output_scaler = pickle.load(f)
data_processing/bci_decoding/eval_singleday_models_multithread.py:193:            predictions = predict_lstm(lstm_model, input_scaler, output_scaler, test_neural, device)
data_processing/bci_decoding/eval_singleday_models_multithread.py:207:                'Day_diff': day_diff,
data_processing/bci_decoding/eval_singleday_models_multithread.py:244:    if LIMIT_EVALS_TO_CLOSE_DAYS and np.abs(day_diff) > MAX_NUM_CLOSE_DAYS:

[... 199 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/LINK_dataset; grep -v "^\s*#" generate_figures.py | grep -v "^\s*$"; echo -----; grep -v "^\s*#" data_processing/stability/stability/trainer_multiday.py | grep -v "^\s*$" | head -120
```

```
from data_plotting import create_dimensionality_across_days_figures
from data_plotting import create_dataset_overview_figure
from data_plotting import create_signal_quality_figure
from data_plotting import create_single_channel_tuning_figure
from data_plotting import creat_all_decoding_figures
import argparse
import sys
def parse():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--plot",
        choices=[
            "bci_decoding",
            "dimensionality_across_days",
            "dataset_overview",
            "signal_quality",
            "single_channel_tuning"
        ],
        required=False
    )
[... 183 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/LINK_dataset; grep -v "^\s*#" data_processing/stability/stability/multiday_eval.py | grep -v "^\s*$" | head -150; grep -n "exp\|curve_fit\|180\|10\]" data_processing/stability/stability/*.ipynb | head -40
```

```
<persisted-output>
Output too large (614.4KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/a718371c-3348-4ba5-a51e-178f5d3b917b/tool-results/b533vj4bk.txt

Preview (first 2KB):
data_dir = "../../link_dataset_pkl"
neural_decoding_dir = "[removed: a home directory path]/Code/Chang/neuraldecoding"
target_day = '20210731'
cfg_path = "config_LSTM_cpu"
import os
import argparse
import datetime
parser = argparse.ArgumentParser()
parser.add_argument('--trial_name', type=str, default=None, help='Trial name for saving results')
args = parser.parse_args()
if args.trial_name is None:
    trial_name = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M')
else:
    trial_name = args.trial_name
import sys
import os
[... 46 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/LINK_dataset/data_processing/stability/stability; python3 - <<'E'
import json
for nb in ['multiday_plotter.ipynb','stability_plotter.ipynb']:
    d=json.load(open(nb))
    print('#####',nb)
    for c in d['cells']:
        if c['cell_type']=='code':
            s=''.join(c['source'])
            if any(k in s for k in ['exp','curve_fit','fit','sem','day_diff','<=']):
                print('-----');print(s[:2500])
E
```

```
##### multiday_plotter.ipynb
-----
df_filtered = df[(df['relative_days'] >= -185) & (df['relative_days'] <= 180)]
df_filtered
-----
grouped_df = df_filtered.groupby(['train_duration', 'relative_days']).agg({
    'r_mean': 'mean',
    'r2': ['mean', 'sem'],
    'mse_mean': 'mean'
}).reset_index()
grouped_df.columns = ['train_duration', 'relative_days', 'r_mean', 'r2', 'r2_sem', 'mse_mean']
grouped_df
-----
from scipy.optimize import curve_fit
from scipy.io import savemat

durs = [1,5]
#durs = [1,2]
colours = ['#FF8400', '#33B597']
#colours = ['darkblue', 'orange']
[... 220 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/LINK_dataset/data_processing/continual_learning; grep -n "seed\|30\b\|120\|300\|durations\|amount\|200\|norm\|lr\|iter\|epoch" continual_learning_lstm.py | head -70; grep -n "seed\|30\|baseline\|day 0\|mean" plot_continual_learning_final.py | head -30
```

```
27:   - Update only the input (neural) normalizer, keep output normalizer fixed
61:    '2022-09-30', # 20
67:# NUM_FINETUNE_SAMPLES_LIST = [30*32, 60*32, 120*32, 300*32]  # Different numbers of samples to sweep over (OLD - asumming 32ms bins)
68:NUM_FINETUNE_SAMPLES_LIST = [30*50, 60*50, 120*50, 300*50]  # Different numbers of samples to sweep over (New - assuming 20ms bins)
70:MAX_DAYS_TO_TEST = 200       # Maximum number of days to test (set to None for all available days)
72:MAX_DAY_DIFFERENCE = 200    # If not None, will stop if day diff is greater than this
74:# Option to force a specific number of finetune iterations for a given number of finetune samples
75:# (using this after we've already run the sweep)
78:    30*50: 50,
80:    120*50: 250,
81:    300*50: 500,
84:FINETUNE_ITERATIONS_LIST = [10, 20, 50, 250, 500]         # Different numbers of finetune iterations to sweep over
97:NUM_TRAIN_TRIALS = 300
105:lstm_hidden_size = 300
111:initial_num_iterations = 2000
112:initial_start_lr = 2e-4
113:initial_end_lr = 1e-5
117:# finetune_num_iterations is now handled by FINETUNE_ITERATIONS_LIST sweep
118:finetune_start_lr = 2e-4       # Lower learning rate for fine-tuning
119:finetune_end_lr = 1e-5
[... 64 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/LINK_dataset/data_processing/continual_learning; sed -n 20,100p continual_learning_lstm.py; sed -n 440,560p continual_learning_lstm.py | grep -v "^\s*#" | grep -v "^\s*$" | head -90
```

```
"""
Continual Learning Script for LSTM Models

This script implements a continual learning strategy for LSTM models:
1. Train an initial LSTM model on a specified starting day
2. For each consecutive day in the dataset:
   - Fine-tune the model using only a limited number of samples from that day
   - Update only the input (neural) normalizer, keep output normalizer fixed
   - Evaluate on the full test set of that day
3. Track performance across days

Results are saved as CSV with performance metrics for each day.
"""

########################################################
# Configuration Parameters
########################################################

data_folder = '../../link_dataset_pkl'
results_folder = 'continual_learning_results'
[... 148 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/LINK_dataset/data_processing/pop_level_analyses; grep -n "def \|PCA(\|zscore\|StandardScaler\|quarter\|n_components\|37\|jerk\|year" population_level_analyses.py | head -80
```

```
13:from sklearn.preprocessing import StandardScaler
21:def load_channel_population_data(data):
35:def load_all_datasets(data_folder = '../../Hisham_Temmar/big_dataset/2_autotrimming_and_preprocessing/preprocessing_092024_no7822nofalcon', total_datasets = None):
89:def prepare_tuning_data(results, normalize = True, normalize_all = True):
132:def normalize_data(df, data_type, normalization_method, pca_by_day = False):
138:        scaler = StandardScaler().fit(all_data)
150:            scaled_data = StandardScaler().fit_transform(data)
152:                pca = PCA(n_components=3)
175:def day_by_day_PCA(df_tuning, threshold = 80):
187:        pca = PCA()
218:def explained_var_over_time(df_tuning):
224:    # Create quarter labels
226:    quarters = pd.PeriodIndex(dates, freq='Q').quarter
227:    years = pd.PeriodIndex(dates, freq='Q').year
228:    quarter_labels = [f'Q{q} {y}' for q, y in zip(quarters, years)]
230:    # Group data by quarters
231:    quarter_groups = pd.DataFrame({
233:        'quarter_label': quarter_labels
234:    }).groupby('quarter_label')
239:    # display(quarter_groups)
[... 61 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat papers/datasets/temmar-2025.yaml 2>/dev/null; sed -n 1,60p tools/claims_check.py | head -60; grep -n "kind\|schema_version" claims/fouke-2025.yaml | head
```

```
# The datasets this paper is tested on (docs/paper-first.md).
schema_version: 1
paper: doi:10.52202/085713-4642
title: 'Long-term Intracortical Neural activity and Kinematics (LINK): An intracortical neural dataset
  for chronic brain-machine interfaces, neuroscience, and machine learning'
datasets:
- archive: dandi
  id: '001201'
  relation: primary
"""Check a claims file against the full text of its paper.

    python tools/claims_check.py claims/<dandiset>/<doi>.yaml paper/<text>.txt [more texts ...]

Validates the file against schemas/claims.schema.json, checks every quote word for word
(fragments split on "...", found in order) and looks for every recorded p-value and
confidence-interval bound in the text. The text may be plain text, HTML or JATS XML; several
files (a paper and its supplement) are searched together. A value printed in a form the
checker does not know (a garbled PDF glyph, "p = 0.04, 0.05 and 0.16") is reported, to be
confirmed by reading. Exits non-zero on any problem.
"""
[... 51 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python3 -c "
import json;s=json.load(open('schemas/claims.schema.json'))
import pprint
def find(o,k):
    if isinstance(o,dict):
        for a,b in o.items():
            if a==k: print(json.dumps(b,indent=1)[:3000]); return True
            if find(b,k): return True
    elif isinstance(o,list):
        for x in o:
            if find(x,k): return True
find(s,'claim') or print(list(s.get('\$defs',s.get('definitions',{})).keys()))
"
```

```
['expected', 'statistic']
```

**Agent calls Bash**

```bash
cd  python3 -c "
import json;s=json.load(open('schemas/claims.schema.json'))
c=s['properties']['claims']['items']
print(json.dumps(c,indent=1)[:4000]); print(list(s['properties']))"
```

```
{
 "type": "object",
 "additionalProperties": false,
 "required": [
  "id",
  "statement",
  "source"
 ],
 "properties": {
  "id": {
   "description": "Stable within the file, e.g. fig2b.",
   "type": "string",
   "pattern": "^[a-z0-9]+(-[a-z0-9]+)*$"
  },
  "statement": {
   "description": "The finding in one or two sentences, in words. Not a copy of the figure.",
   "type": "string",
   "minLength": 1
  },
  "source": {
[... 119 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python3 -c "
import json;s=json.load(open('schemas/claims.schema.json'))
print(json.dumps(s['\$defs'],indent=1)[:3000])"
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
cd $TMPDIR/LINK_dataset/data_processing; python3 - <<'E'
import json
d=json.load(open('signal_changes/signal_qual.ipynb'))
for c in d['cells']:
    if c['cell_type']=='code':
        s=''.join(c['source'])
        if any(k in s for k in ['bank','active','linregress','regplot','Lateral','Medial']):
            print('-----');print(s[:3000])
E
cat stability/stability/config_LSTM/preprocessing/*.yaml stability/stability/config_LSTM/trainer/trainer.yaml | head -80
```

```
preprocessing_decoder: 
  order: [dict1, split1, add_history1, update_normalize_sequence, tensor1, tuple_out]
  content:
    dict1:
      type: Dict2DataDictBlock
      params:
        neural_type: sbp
    split1:
      type: DataSplitBlock
      params:
        split_ratio: 0.9
        split_seed: -1
    add_history1:
      type: AddHistoryBlock
      params:
        location: ['neural_train', 'neural_test']
        seq_length: 20
    update_normalize_sequence:
      type: UpdateNormalizationBlock
      params:
[... 61 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/LINK_dataset; grep -rln "Medial\|inactive" --include=*.py --include=*.ipynb . ; grep -rn "std_multiplier=\|std_multiplier =" data_processing/pop_level_analyses/*.py data_plotting/*.py | head; grep -n "Lateral\|Medial\|bank" utils/*.py data_plotting/single_channel_tuning.py data_processing/single_channel_tuning/tuning_plotter.py | head -20
```

```
./tutorials/01_Starting_with_NWB_Data.ipynb
data_processing/pop_level_analyses/population_level_analyses.py:591:def trim_neural_data_at_movement_onset_std_and_smooth(data_dict, std_multiplier=2, sigma=5, display_alignment=False, trim_pt = movement_onset, direction_key = None, position_data = None):
data_processing/pop_level_analyses/population_level_analyses.py:675:    processed_neural_data_for_direction, kinematics_data = trim_method(neural_data_for_direction, std_multiplier=2, sigma=0, display_alignment=False, trim_pt = trim_pt, direction_key = direction_key)
data_processing/pop_level_analyses/population_level_analyses.py:1331:    processed_neural_data_for_direction, kinematics_data = trim_method(neural_data_for_direction, std_multiplier=2, sigma=sigma, display_alignment=display_alignment, trim_pt = trim_pt, direction_key = direction_key)
data_plotting/single_channel_tuning.py:61:        # print(f'bank_{i} avg iqr: {np.mean(np.sum(xerr))}')
data_processing/single_channel_tuning/tuning_plotter.py:138:def plot_tuning_histogram(ax, tuning_avgs, metric = 'std', type='ang', bins = 10, colour = 'blue', banks = [(0, 32), (32, 64), (64, 96)]):
data_processing/single_channel_tuning/tuning_plotter.py:143:    if not banks:
data_processing/single_channel_tuning/tuning_plotter.py:148:        sns.pointplot(data=tuning_avgs, x='bank', y=key, hue='bank', ax=ax, errorbar='sd')
data_processing/single_channel_tuning/tuning_plotter.py:149:        mn = tuning_avgs.groupby('bank')[key].mean()
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/LINK_dataset; sed -n 560,640p data_processing/pop_level_analyses/population_level_analyses.py; sed -n 132,175p data_processing/pop_level_analyses/population_level_analyses.py
```

```
## Trim Methods ##
def max_jerk(trial_data, kinematics, std_multiplier):
    
    mvmt_idx, _ = movement_onset(trial_data, kinematics, std_multiplier)
    if mvmt_idx < 3:
        ind = -1
    else:
        acceleration = np.hstack(([0], np.diff(kinematics)))
        jerk = np.hstack(([0], np.diff(acceleration)))
        ind = np.argmax(abs(jerk[:mvmt_idx]))
    return ind, 0

def movement_onset(trial_data, kinematics, std_multiplier):
    # Use first 10% of trial kinematics as baseline
    baseline_period = kinematics[:int(kinematics.shape[0] * 0.1)]
    baseline_mean = np.mean(baseline_period)
    baseline_std = np.std(baseline_period)

    # Calculate threshold
    threshold = baseline_mean + (baseline_std * std_multiplier)
[... 105 more lines not kept]
```

**Agent**

I have everything I need. Writing the claims file now.

**Agent calls Write**

```json
{
 "file_path": "claims/temmar-2025.yaml",
 "content": "# Claims for Temmar et al. (2025), \"Long-term Intracortical Neural activity and Kinematics\n# (LINK)\", NeurIPS 2025 Datasets and Benchmarks track, on dandiset 001201.\n# Written by an agent (model \"claude-opus-5-5\", Claude Code, runner \"GitHub Actions\"),\n# 2026-11-12, protocol pilot-14 as stated in docs/protocol.md.\n#\n# Text read: the version of record (open-access PDF from the Curran Associates NeurIPS 2025\n# proceedings, extracted to paper/10.52202-085713-4642.txt), main text, figure legends and\n# checklist, and the supplement (Supplementary Materials and Appendices, from OpenReview):\n# Appendix A (task, implants, feature extraction), B (curation, file format), C (analysis\n# methods) and Figures S1 to S6. The paper reports no statistical test for any finding; its\n# findings are slopes of linear fits, counts, R2 values and visual descriptions of figures.\n#\n# Code read: github.com/chesteklab/LINK_dataset at commit 5e1c36a1282f90abb8d96963920a8b1fdd27a6e7\n# (2026-10-20). It holds the NWB-to-pickle converter (utils/), the signal-change analysis\n# (data_processing/signal_changes: mean SBP per channel and day, active channels, participation\n# ratio), single-channel tuning (data_processing/single_channel_tuning/tuning_utils.py), the\n# population PCA analysis (data_processing/pop_level_analyses/population_level_analyses.py),\n# single-day RR and LSTM decoders and their cross-day evaluation (data_processing/bci_decoding),\n# the multi-day training (data_processing/stability/stability, which calls an outside library,\n# \"neuraldecoding\", not in the repository) and the continual fine-tuning\n# (data_processing/continual_learning/continual_learning_lstm.py), with the figure scripts in\n# data_plotting/. Code facts used below are cited by file.\n#\n# Data the paper used: one male rhesus macaque, Monkey N (age 7 to 11), with two 64-channel Utah\n# arrays in the hand area of right precentral gyrus (a third array in somatosensory cortex was\n# not recorded). 96 of the 128 motor channels were recorded, in three 32-channel banks (A to C),\n# one bank on the lateral array and two on the medial array (Figure 1C, Figure S1; channels\n# numbered 0 to 95). Task: a 2-DOF finger task, index (IDX) and middle-ring-small (MRS) finger\n# groups moved with the left hand in a manipulandum, positions 0 (full extension) to 1 (full\n# flexion), 750 ms hold, juice reward; two target styles, center-out (CO, 8 directions at 20, 30\n# or 40% of the arc, every other trial a return to [0.5, 0.5]) and random (RD). Only successful\n# trials, the first 375 after filtering, per session. 312 sessions on 303 days spanning 1,242 days\n# (days 349 to 1591 after implant, January 2020 to February 2024); on 9 days both a CO and an RD\n# session. Measured variables per 20 ms bin: spiking-band power (SBP, 300 to 1000 Hz band, mean\n# magnitude) and threshold crossing counts (TCR, -4.5 x RMS threshold) on 96 channels, and the\n# position and velocity of both finger groups; per trial, start and stop times, target positions,\n# target style and timeout; per channel, bank, array, row, column and impedance. One NWB file per\n# session.\n#\n# Code choices that fix details the text leaves open, used below unless a criterion says\n# otherwise: SBP values in the converted data are multiplied by 0.25 to give microvolts and TCR\n# counts per bin by 50 to give Hz (tuning_utils.py, signal_changes.py, signal_utils.py); on days\n# with two sessions the mean SBP and the tuning use both sessions concatenated, and the active\n# channel count and participation ratio use the CO session (signal_utils.py); slopes are\n# scipy linregress on days since the first session (signal_changes.py).\nschema_version: 2\ndataset:\n  archive: dandi\n  id: \"001201\"\npaper: doi:10.52202/085713-4642\nclaims:\n- id: dataset-sessions\n  statement: The dataset holds 312 sessions recorded on 303 days spanning 1,242 days, two sessions\n    (one CO, one RD) on 9 days, each session 375 successful trials, from days 349 to 1591 after\n    implant.\n  source: Section 3, The LINK Dataset, paragraph 1 (page 4); Appendix B.1 and B.2; Appendix A.2\n  quote: on 303 days spanning 1,242 days. The dataset comprises 312 ’sessions’ of 375 (mostly)\n    contiguous trial acquisitions. Each session contains one of two variations to the task,\n    ‘center-out’ or ‘random’, described below. On 9 days, two sessions are available as both tasks\n    were performed.\n  expected:\n  - quantity: number of sessions\n    value: 312\n    tolerance: 0\n  - quantity: number of recording days\n    value: 303\n    tolerance: 0\n  - quantity: span from first to last recording day\n    value: 1242\n    tolerance: 0\n    unit: days\n  - quantity: days with two sessions\n    value: 9\n    tolerance: 0\n  - quantity: trials per session\n    value: 375\n    tolerance: 0\n  criterion: These are counts of the deposit as the paper describes it, so the tolerance is zero\n    and not 10%. Sessions are the NWB files; days are distinct session dates; the span is last\n    date minus first date. Reproduced when all five match; partially reproduced when the session\n    and trial counts match and one of the others differs. A session with a trial count other\n    than 375 is listed. The dates are also compared with the stated range of days 349 to 1591\n    after implant (Appendix A.2) only if the dataset gives the implant date.\n- id: dataset-contents\n  statement: Each session holds SBP and TCR for 96 motor-cortex channels and the position and\n    velocity of the two finger groups in 20 ms bins, with per-trial target positions, start times,\n    lengths and target style, and per-channel array locations and impedances.\n  source: Section 3, The LINK Dataset, paragraph 1 (page 4); Section 3.3; Appendix B.3\n  quote: In each session, we provide neural data preprocessed into two neural features in 20ms\n    bins... spiking-band power (SBP) and threshold crossing rate (TCR). We also provide the position\n    and velocity of the 2DOF at the same resolution.\n  criterion: Reproduced when every session file holds 96-channel SpikingBandPower and\n    ThresholdCrossings series and index and MRS position and velocity series, all at 20 ms\n    sampling (timestamps spaced 0.02 s), a trials table with the columns Appendix B.3 lists, and\n    an electrodes table with bank, row, column and impedance columns. Partially reproduced when\n    a few files lack a part; each gap is listed. Velocity is checked against the difference of\n    consecutive binned positions, as Appendix A.3 defines it.\n- id: figs2-throughput-improves\n  statement: The monkey's real-time task performance, measured as average Fitts' law throughput\n    per day, appears to improve gradually over the dataset.\n  source: Appendix A.1, paragraph 2; Figure S2\n  quote: In S2, we show the average throughput across all trials for each day, and noted that\n    Monkey N’s performance appears to gradually improve throughout the course of the dataset.\n  criterion: Throughput per trial is computed \"as described in [1]\" (Nason et al. 2021), which is\n    not part of this paper, and the code holds no throughput function, so its form is open. The\n    readings named are (a) index of difficulty log2(1 + D/W) over acquisition time, with D the\n    Euclidean distance in the 2-DOF position space from the previous targets to the current\n    targets and W the target width of 0.15 (Appendix A.1), acquisition time being the trial\n    length minus the 750 ms hold; (b) the same with the trial length including the hold; (c)\n    the sum over the two finger groups of each group's log2(1 + D/W), over the time of (a).\n    Per day, the mean over all trials of both sessions. Reproduced when, under one reading, a\n    linear fit of daily mean throughput on date has a positive slope with p < 0.05 (two-sided\n    linregress; the paper gives no test, so the threshold is a standard choice and not the\n    paper's).\n- id: fig2a-sbp-decline\n  statement: Average SBP across channels decreased gradually by about 0.033 microvolts per month,\n    as estimated by a linear model fit to every channel's mean SBP on every day.\n  source: Section 4.1, paragraph 1; Figure 2A and legend\n  quote: Average SBP across channels decreased gradually by approximately 0.033 μV per month, as\n    estimated by a linear model.\n  expected:\n  - quantity: slope of mean SBP over time\n    value: -0.033\n    tolerance: 0.0033\n    unit: microvolts per month\n  criterion: As in signal_utils.calc_avg_sbps and signal_changes.create_avg_sbp_plot. Per day and\n    channel the mean of SBP over all bins of the day (both sessions concatenated on two-session\n    days), multiplied by 0.25 to give microvolts; one ordinary least-squares line (scipy\n    linregress) fit to all channel-day points on days since the first day, with no outliers\n    removed (the legend's outliers are only marked on the plot); the slope per day times 30.44\n    days per month. The legend prints the slope as 0.033 without a sign while the text says\n    decreased; the expected value is negative. Open detail, which could change the outcome by a\n    factor of four, is the unit of SBP in the NWB files. The readings are (a) the NWB values\n    multiplied by 0.25 as the code does to the converted data (when the NWB series stores the\n    raw xPC units); (b) the NWB values in the unit their conversion attribute gives, when that is\n    already microvolts. Reproduced when the slope is within tolerance under one reading; the\n    supplement's overall slope of -1.11e-3 per day (Appendix C.2), which is the same number per\n    day, is reported alongside.\n- id: fig2a-irregular-shifts\n  statement: Groups of channels show irregular SBP shifts in some periods, for example from about\n    July to November 2022, and these shifts did not affect overall decoding performance.\n  source: Section 4.1, paragraph 1; Figure 2A\n  quote: There are periods where groups of channels exhibit irregular shifts (e.g. ~2022-07 to\n    ~2022-11), but these did not affect overall decoding performance.\n  depends_on:\n  - fig4a-sameday-stable\n  criterion: The paper gives no measure of a shift or of \"did not affect\"; both are fixed here as\n    choices not in the paper. A shift is a channel whose mean SBP on a day differs from its median\n    over the preceding 30 days of sessions by more than three times that window's median absolute\n    deviation. The claim holds (reproduced) when in July to November 2022 at least five channels\n    shift on the same day on at least one day, and the same-day LSTM and RR R2 of fig4a-sameday-stable\n    for sessions in that window have medians within the 10th to 90th percentile range of all\n    sessions' values. Partially reproduced when only one of the two parts holds.\n- id: fig2b-active-channels-decrease\n  statement: The number of active channels, those with mean TCR above 1 Hz on a day, appears to\n    decrease over time.\n  source: Section 4.1, paragraph 2; Figure 2B and legend\n  quote: During iBMI experiments, we can roughly estimate the number of active channels by counting\n    those with mean TCR > 1 Hz, shown in Figure 2B. Note that this appears to decrease over time.\n  criterion: As in signal_utils.calc_pr_all_days. Per day, TCR counts per 20 ms bin times 50 give\n    Hz; a channel is active when its mean over all bins of the session exceeds 1 Hz; the CO\n    session is used on two-session days, the RD session otherwise. Reproduced when a linear fit\n    of the daily count on days since the first day has a negative slope with p < 0.05 (two-sided\n    linregress; the paper gives no test, so this is a standard choice). The counts in the first\n    and last 30 sessions are reported.\n- id: fig2c-pr-decline\n  statement: The participation ratio of the active channels' SBP decreased by about 0.07 per month,\n    as estimated by a linear model.\n  source: Section 4.1, paragraph 2; Figure 2C and legend\n  quote: a linear model estimated that PR decreased by ~0.07 PR per month\n  expected:\n  - quantity: slope of participation ratio over time\n    value: -0.07\n    tolerance: 0.007\n    unit: PR per month\n  depends_on:\n  - fig2b-active-channels-decrease\n  criterion: As in signal_utils.calc_pr_all_days and participation_ratio. Per day, the active\n    channels of fig2b-active-channels-decrease (CO session on two-session days); the SBP of those\n    channels over all bins of the session, mean-subtracted per channel and not z-scored; the\n    eigenvalues of its covariance; PR = (sum of eigenvalues) squared over the sum of squared\n    eigenvalues (Gao et al., cited as [68]). Days with no active channel are skipped. A linear fit\n    (linregress) of PR on days since the first day; slope per day times 30.44. Reproduced when the\n    slope is within tolerance. Using both sessions on two-session days is shown as a variant.\n- id: fig2c-ten-dimensions\n  statement: Generally, 10 dimensions were sufficient to capture the majority of the variance of\n    the active channels.\n  source: Section 4.1, paragraph 2; Figure 2C\n  quote: Generally, 10 dimensions were sufficient to capture the majority of the variance in active\n    channels\n  depends_on:\n  - fig2c-pr-decline\n  criterion: The paper does not say how the sentence was measured. The readings are (a) the daily\n    PR of fig2c-pr-decline is at most 10 (the paper says PR roughly corresponds to the number of\n    dimensions explaining 80% of the variance); (b) the first 10 principal components of the\n    active channels' mean-subtracted SBP explain more than 50% of its variance; (c) the same at\n    more than 80%. Reproduced when, under one reading, it holds on more than half of the days\n    (\"generally\"); the fraction of days is reported under each reading.\n- id: figs4-bank-slopes\n  statement: Mean SBP decreases over time in each 32-channel bank, with lower overall activity and\n    a shallower slope on the lateral bank (-0.58e-3) than on the two medial banks (-1.34e-3 and\n    -1.40e-3), against -1.11e-3 for all channels.\n  source: Appendix C.2, paragraph after Figure S3; Figure S4; Section 4.1, paragraph 2\n  quote: The slopes of the best-fit lines for the Lateral, Medial 1, and Medial 2 groups were −0.58\n    × 10−3, −1.34 × 10−3, and −1.40 × 10−3 respectively. This is compared to −1.11 × 10−3 for the\n    overall SBP. This is largely because the average SBP is generally higher on the medial arrays\n  expected:\n  - quantity: slope, lateral bank\n    value: -0.00058\n    tolerance: 0.000058\n    unit: microvolts per day\n  - quantity: slope, medial 1 bank\n    value: -0.00134\n    tolerance: 0.000134\n    unit: microvolts per day\n  - quantity: slope, medial 2 bank\n    value: -0.0014\n    tolerance: 0.00014\n    unit: microvolts per day\n  - quantity: slope, all channels\n    value: -0.00111\n    tolerance: 0.000111\n    unit: microvolts per day\n  depends_on:\n  - fig2a-sbp-decline\n  criterion: The unit of the slopes is not printed; microvolts per day is the reading consistent\n    with the overall slope and the 0.033 microvolts per month of Figure 2A. The code for Figure S4\n    is not in the repository. Bank membership and which bank is lateral, Medial 1 and Medial 2\n    come from the electrodes table (bank and array columns) and Figure S1. Open detail, which\n    could change the slopes, is what the line is fit to; the readings are (a) all channel-day mean\n    SBP values of the bank, as the overall slope is computed in the code; (b) the per-day mean over\n    the bank's channels (the Figure S4 legend says the mean SBP for each bank was calculated for\n    each day). The SBP unit readings of fig2a-sbp-decline apply. Reproduced when, under one\n    reading, all four slopes are within tolerance and the lateral bank's mean SBP over the dataset\n    is below each medial bank's; partially reproduced when the ordering of slopes (lateral\n    shallowest, all negative) holds but values fall outside tolerance.\n- id: figs5-active-inactive-slopes\n  statement: Grouped per session into active and inactive channels by TCR, mean SBP of active\n    channels declines faster (-1.29e-3) than all channels, while the slope for inactive channels\n    is near zero (0.54e-3), and inactive channels have lower SBP.\n  source: Appendix C.2, paragraph after Figure S3; Figure S5; Section 4.1, paragraph 2\n  quote: The slopes of the best-fit lines here were −1.29 × 10−3, and 0.54 × 10−3. As might be\n    expected, the slope for the inactive channels was near 0\n  expected:\n  - quantity: slope, active channels\n    value: -0.00129\n    tolerance: 0.000129\n    unit: microvolts per day\n  - quantity: slope, inactive channels\n    value: 0.00054\n    tolerance: 0.000054\n    unit: microvolts per day\n  depends_on:\n  - fig2b-active-channels-decrease\n  criterion: Active means mean TCR above 1 Hz in the session, as in Section 4.1 and the code\n    (the supplement's \"average TCR < 1Hz\" for active is read as a typo, since it calls the others\n    inactive and the main text uses > 1 Hz). Classification is per session as the supplement says.\n    The order of the two printed slopes is read as active then inactive, as the sentence that\n    follows confirms. The fit readings (a) and (b) and the unit readings of figs4-bank-slopes\n    apply; the code for Figure S5 is not in the repository. Reproduced when, under one reading,\n    both slopes are within tolerance and inactive channels have the lower mean SBP. Section 4.1\n    says all categories decreased, which the positive inactive slope contradicts; the sign found\n    is reported.\n- id: fig2d-population-drift\n  statement: In a PCA fit to SBP z-scored per channel across the whole dataset, the per-day and\n    per-quarter centroids of the top 3 PCs move through PC space over time, while the standard\n    deviation of the top 3 PCs per quarter changes little except in two quarters.\n  source: Section 4.1, paragraphs 3 and 4; Figure 2D and legend; Appendix C.3\n  quote: Visually, these centroids appear to move throughout the PCA space over time, and except\n    for two quarters, the standard deviation of the top 3 PCs does not exhibit large changes.\n  criterion: Method from Appendix C.3 and population_level_analyses.normalize_data (method all).\n    SBP of all sessions concatenated, z-scored per channel over the whole dataset, PCA\n    (scikit-learn) to 3 components, scores grouped by day and by calendar quarter; centroid and\n    standard deviation per group. The paper judges this visually; the decision rule is a choice\n    not in the paper. Movement holds when the distance between the first and last quarter's\n    centroids exceeds the mean within-quarter standard deviation (root mean square over the 3\n    PCs). Stable spread holds when at most two quarters have a 3-PC standard deviation more than\n    25% away from the median over quarters. Reproduced when both hold; partially reproduced when\n    one does. The centroid path and the per-quarter standard deviations are shown.\n- id: fig2e-trajectories-separable\n  statement: Average neural trajectories in the top 3 PCs for the eight movement directions remain\n    visually separable in both the first year (2020) and the last (2023) of the dataset.\n  source: Section 4.1, paragraph 4; Figure 2E and legend; Appendix C.3\n  quote: The trajectories shown remain visually separable at the beginning and end of the dataset.\n  criterion: Method from Appendix C.3. Per day, SBP z-scored per channel and a PCA fit for that\n    day, top 3 PCs; CO and RD trials both used; each trial labelled with one of eight directions\n    by the angle of the vector from the previous trial's targets to its targets (IDX on x, MRS on\n    y), in 45-degree sectors centred on the eight directions (Figure S6); movement onset as the\n    first bin where the velocity of the dominant finger (MRS for MRS-dominant directions, IDX\n    otherwise) leaves the mean plus or minus one standard deviation of the first 10% of the\n    trial's velocities; alignment at the maximum absolute jerk (second difference of velocity)\n    before onset; 37 bins from the alignment point; averaged per year and direction. The code\n    uses 2 standard deviations and a window from 150 ms before to 600 ms after the alignment\n    point (population_level_analyses.py); this is shown as a variant. The paper judges\n    separability visually; the rule here is a choice not in the paper. For 2020 and 2023 each,\n    trials' 37-bin trajectories in the 3 PCs are classified by direction with a nearest-centroid\n    classifier under 5-fold cross-validation. Reproduced when accuracy exceeds chance (1/8) by a\n    one-sided binomial test at p < 0.05 in both years; partially reproduced in one year.\n- id: fig3b-two-channels\n  statement: Channel 7 is strongly tuned to MRS flexion throughout the dataset, whereas channel 32\n    shows large shifts in tuning angle; both are active, with average TCR above 1 Hz across the\n    dataset.\n  source: Section 4.2, paragraph 1; Figure 3B and legend\n  quote: Channel 7 was strongly tuned to MRS flexion throughout the dataset, whereas channel 32\n    exhibited large shifts in tuning angle.\n  criterion: Tuning as in Appendix C.2 and tuning_utils.compute_channel_tuning. Per day (both\n    sessions concatenated), each channel's SBP z-scored; for lags of 0 to 10 bins (behaviour at\n    t plus lag), a linear regression with intercept of IDX and MRS position on the channel's SBP;\n    the two coefficients form a vector; the lag with the largest vector norm is kept. Angle is\n    atan2(MRS, IDX), so 0 degrees is IDX flexion and 90 degrees MRS flexion; strength is the norm.\n    Appendix C.2 says position or velocity; the main text and the code use position, which is\n    followed. Circular median and circular IQR per channel as in calc_medians_iqrs. Channels are\n    numbered 0 to 95 as in Figure S1. The decision rule is a choice not in the paper. Reproduced\n    when channel 7's circular median angle is within 45 degrees of 90, its circular IQR is below\n    45 degrees and its median strength is above the median over channels; channel 32's circular\n    IQR is larger than channel 7's and above the median circular IQR over channels; and both\n    channels' mean TCR over the dataset exceeds 1 Hz.\n- id: fig3cd-tuning-stable\n  statement: Per-channel tuning angles and strengths generally appear consistent through the\n    dataset, and in most channels the circular IQR of tuning angle is small, so their tunings did\n    not change much.\n  source: Section 4.2, paragraph 1; Figure 3C, 3D and 3E; Discussion, paragraph 3\n  quote: In most channels, the circular IQR of tuning angles was small, suggesting their tunings\n    did not change much throughout the dataset.\n  depends_on:\n  - fig3b-two-channels\n  criterion: Tuning as in fig3b-two-channels. The paper does not fix what a small circular IQR\n    is. The readings are (a) below 45 degrees (one of the eight 45-degree movement sectors of\n    Appendix C.3); (b) below 90 degrees. The channels counted are (i) all 96, or (ii) the channels\n    active (mean TCR above 1 Hz) over the dataset. Reproduced when, under one pair of readings,\n    more than half of the channels have a small circular IQR; the distribution of circular IQRs\n    is shown.\n- id: fig3d-weak-channels-low-tcr\n  statement: Many channels have very low tuning strength throughout the arrays' lifespan, and such\n    channels typically have low average TCR per day.\n  source: Section 4.2, paragraph 1; Figure 3D; Figure S3; Appendix C.2, paragraph after Figure S3\n  quote: many channels have very low tuning strengths throughout the lifespan of the arrays. Such\n    channels also typically showed low average TCRs per day, as shown in Figure S3.\n  depends_on:\n  - fig3b-two-channels\n  criterion: Tuning strength as in fig3b-two-channels; mean TCR per channel and day in Hz, as\n    tuning_utils.compute_tuning_data saves it. The test is a choice not in the paper. Across the\n    96 channels, the Spearman correlation between median tuning strength and median daily TCR is\n    positive with p < 0.05, and the channels in the lowest quartile of median strength have a\n    lower median TCR than the others (Mann-Whitney, p < 0.05). Reproduced when both hold;\n    partially reproduced when one does.\n- id: fig3e-array-tuning\n  statement: Channels on the medial array are mainly tuned to MRS flexion, with some to IDX\n    flexion, while channels on the lateral array are more tuned to extension of both fingers, so\n    channels on the same array tend to have similar tuning angles.\n  source: Section 4.2, paragraph 1; Figure 3E; Discussion, paragraph 3\n  quote: it appears that channels in the medial array (see Figure 1) are mainly tuned to MRS\n    flexion, with some IDX flexion, while channels in the lateral array are more tuned to\n    extension of both DOF.\n  depends_on:\n  - fig3b-two-channels\n  criterion: Per channel, the circular median tuning angle of fig3b-two-channels; array from the\n    electrodes table. In the code's convention MRS flexion is 90 degrees, IDX flexion 0, IDX\n    extension 180 and MRS extension -90, so extension of both is -135. The sectors are a choice\n    not in the paper; each is a quadrant widened by half a 45-degree sector. Reproduced when more\n    than half of medial channels have a circular median angle between -22.5 and 112.5 degrees with\n    more of them within 45 degrees of 90 than within 45 degrees of 0, and more than half of\n    lateral channels have one between -202.5 and -67.5 degrees (centred on -135). The channels\n    counted are all channels or only active ones (two readings); reproduced under either.\n    Partially reproduced when one array holds.\n- id: fig4a-sameday-stable\n  statement: Same-day decoding accuracy (R2 averaged across the four outputs on the 75 hold-out\n    trials) remains relatively stable over the dataset, with most shifts shared by RR and LSTM.\n  source: Section 4.3, paragraph 1; Figure 4A and legend; Discussion, paragraphs 1 and 4\n  quote: Within-day decoding accuracy remains relatively stable across time, and the majority of\n    shifts in accuracy are reflected in both decoders\n  criterion: Decoders as in Appendix C.1 and bci_decoding/train_models_singleday.py. Per session,\n    the first 300 trials train and the last 75 test. SBP is z-scored per channel on the training\n    trials (Appendix C.1 says for both decoders; the code fits no scaler for RR, shown as a\n    variant). RR is sklearn Ridge, alpha 0.1, intercept, 8 bins of history (768 inputs). The LSTM\n    has 96 inputs, hidden size 300, 1 layer, a linear readout of position and velocity of both\n    fingers at the last of 20 bins; Adam, batch 64, 2000 iterations, learning rate decaying\n    linearly from 2e-4 to 1e-5, weight decay 0.001, outputs z-scored on the training data, and\n    Gaussian noise added to the inputs (standard deviation 0.1 per sample and 0.2 per sequence\n    bias), as in the code and [6]. R2 per output (sklearn r2_score), averaged over the four.\n    Sessions on two-session days are evaluated separately, as in the code. The code's test set\n    stops at the start of the last trial (74 trials); the 75 trials of the Methods are used. The\n    decision rules are choices not in the paper. Stable holds when the slope of a linear fit of\n    same-day R2 on date is not negative with p < 0.05 (two-sided) for either decoder, the Discussion\n    saying the decline in neural activity did not correspond to decreases in decoding\n    performance. Shared shifts hold when the Pearson correlation across sessions between RR and\n    LSTM same-day R2 is positive with p < 0.05. Reproduced when both hold; partially reproduced\n    when one does.\n- id: fig4a-lstm-beats-rr\n  statement: The LSTM outperformed ridge regression in same-day decoding on every day.\n  source: Discussion, paragraph 4; Figure 4A\n  quote: While the LSTM outperformed RR on every day, we noted that there were baseline shifts in\n    decoding performance that impacted both decoders\n  depends_on:\n  - fig4a-sameday-stable\n  criterion: Same-day R2 averaged across outputs, as in fig4a-sameday-stable. Reproduced when LSTM\n    R2 exceeds RR R2 on every session; partially reproduced when it does on at least 90% of\n    sessions (a choice not in the paper); not reproduced otherwise. The sessions where RR is higher\n    are listed, and the LSTM is retrained with two further seeds on those sessions to show whether\n    the result rests on the seed (42 in the code).\n- id: fig4bc-dof-accuracy\n  statement: Decoding of finger positions is more accurate than of velocities, and MRS predictions\n    are more accurate than IDX predictions.\n  source: Section 4.3, paragraph 1; Figure 4B and 4C\n  quote: In general, the position accuracies of the two finger groups outperformed velocities, and\n    MRS predictions outperformed IDX predictions, suggesting there may be more information\n    regarding the MRS finger group in the neural data than IDX.\n  depends_on:\n  - fig4a-sameday-stable\n  criterion: Same-day R2 per output from fig4a-sameday-stable. For each decoder, the median over\n    sessions of each of IDX position, MRS position, IDX velocity and MRS velocity. Reproduced when,\n    for both decoders, both position medians exceed both velocity medians, and MRS exceeds IDX for\n    position and for velocity; partially reproduced when the orderings hold for one decoder or\n    only one of the two orderings holds for both. The fraction of sessions in which each ordering\n    holds is reported (\"in general\").\n- id: fig4d-cross-day-decay\n  statement: Decoders tested on hold-out sets of other days within 100 days of training lose\n    accuracy sharply in the short term, with the decay stabilising at longer offsets; neither RR\n    nor LSTM generalises well, the LSTM is better at every offset, and both follow a similar decay.\n  source: Section 4.3, paragraph 2; Figure 4D and legend; Discussion, paragraph 4\n  quote: LSTM outperformed RR on all days, but both followed a similar decay curve.\n  depends_on:\n  - fig4a-sameday-stable\n  criterion: Every single-day decoder of fig4a-sameday-stable is evaluated on the 75 hold-out\n    trials of every session within 100 days of its training day, with no retraining; R2 averaged\n    across outputs; evaluations grouped by day offset (test date minus training date) and\n    averaged, with standard errors. Two details are open, and each reading is run. Day offset is\n    (a) signed, from -100 to 100, as bci_decoding_plots.plot_performance_across_days plots it, or\n    (b) its absolute value. Input normalization on the test day is (i) the training day's\n    parameters, as Appendix C.1 states for Figure 5, or (ii) refit on the test day's first 300\n    trials, as eval_singleday_models_multithread_updatenorm.py does (the plotting code draws both\n    versions). The rules are choices not in the paper. Reproduced when, under one pair of\n    readings, the LSTM mean exceeds the RR mean at every offset with data; the mean R2 at offsets\n    of 1 to 5 days is below the offset-0 mean by more than the drop from offsets 1 to 5 to offsets\n    90 to 100; and the two curves, each divided by its offset-0 value, correlate with Pearson r\n    above 0.9 across offsets. Partially reproduced when the LSTM is better at 90% or more of\n    offsets and the other two parts hold.\n- id: suppc1-shuffle-baseline\n  statement: With neural and behavioural hold-out data shuffled independently on one session, RR\n    gives an average R2 of -0.166 and the LSTM of -0.156.\n  source: Appendix C.1, Decoder Evaluation paragraph\n  quote: RR had an average R2 of -0.166, and LSTM had an average R2 of -0.156.\n  expected:\n  - quantity: RR R2 on shuffled hold-out data\n    value: -0.166\n    tolerance: 0.0166\n  - quantity: LSTM R2 on shuffled hold-out data\n    value: -0.156\n    tolerance: 0.0156\n  depends_on:\n  - fig4a-sameday-stable\n  criterion: The session is not named and the shuffle is not described beyond \"independently\n    shuffled the neural and behavioral data of the holdout set\". Read as permuting the time bins\n    of the hold-out SBP and, separately, of the hold-out kinematics, then predicting with that\n    day's decoders and scoring against the shuffled kinematics. Because one unnamed session could\n    be any of 312, the claim is judged on the median over all sessions (one shuffle each, seed 0).\n    Reproduced when both medians are within tolerance; partially reproduced when both are\n    negative but one or both fall outside it. Shuffling trials as whole units is shown as a\n    variant.\n- id: fig5a-multiday-short-term\n  statement: Training the LSTM on up to five consecutive past sessions reduces the initial drop in\n    performance within about 5 days of training and improves performance over time, but slightly\n    lowers day-0 performance.\n  source: Section 4.3, paragraph 3; Figure 5A and legend\n  quote: Multi-day training, reduced the initial decrease in performance (within ~5 days of\n    training), improving performance over time, but did not seem to impact the longer term decay,\n    and slightly decreases day 0 performance.\n  criterion: Method from Section 4.3 and Appendix C.1. For each eligible day 0, LSTMs (the\n    architecture and training of fig4a-sameday-stable) trained on the training trials of the\n    latest 1 to 5 sessions up to and including day 0; each evaluated on the hold-out trials of\n    every session within 180 days after day 0, input normalization held at the training\n    parameters (Appendix C.1, Figure 5). Days with two sessions and the first 10 sessions are\n    excluded (Section 4.3); the legend reports 283 days, and the count found is reported. The code\n    (stability/trainer_multiday.py and config_LSTM) differs, skipping only the first 5 sessions,\n    splitting each session 90/10, refitting input normalization on the test data and adding no\n    noise; it is shown as a variant. R2 averaged over outputs, then over day 0s per relative day.\n    Reproduced when, for 5 sessions against 1 session, the mean R2 over relative days 1 to 5 is\n    higher, the drop from day 0 to that mean is smaller, and the day-0 R2 is lower; partially\n    reproduced when the first two hold and day 0 is not lower.\n- id: fig5a-long-term-decay\n  statement: Double-exponential fits to the single-session and five-session conditions over 0 to\n    180 days show steeper decay for single-session training; the initial decay decreases with\n    more training sessions, but the long-term decay is not significantly affected.\n  source: Section 4.3, paragraph 3; Figure 5A\n  quote: A double-exponential fit (Fig. 5A) to the single-session and 5-session conditions over all\n    evaluation sessions (within 180 days of day 0) show steeper decays in the single-session case,\n    confirming our observations... the initial decay decreases with more training sessions, but the\n    long-term decay is not significantly affected.\n  depends_on:\n  - fig5a-multiday-short-term\n  criterion: As in stability_plotter.ipynb (plot_multiday_training). The mean R2 per relative day\n    from 0 to 180 for 1 and 5 training sessions is fit with a*exp(b*x) + c*exp(d*x) by\n    scipy curve_fit, initial values (0.374, 0.00365, 0.134, 0.140) and maxfev 10000 as in the\n    notebook; the component with the larger absolute rate is the initial decay, the other the\n    long-term decay. The paper names no test for \"not significantly\"; the test here is a choice\n    not in the paper, approximate 95% intervals of the rates from the fit covariance. Reproduced\n    when the initial-decay rate is more negative for 1 session than for 5, the predicted drop\n    from day 0 to day 5 is larger for 1 session, and the 95% intervals of the two long-term rates\n    overlap. Not reproduced when the long-term rates' intervals do not overlap, with the size of\n    the difference given. A fit that does not converge is reported with the residuals.\n- id: fig5b-finetune\n  statement: Continual daily fine-tuning of an LSTM on 30 s to 5 min of each new session's data,\n    over up to 200 days from 20 seed days, reduces both short- and long-term decay, and with 120 s\n    or 300 s later decoders outperform the day-0 decode.\n  source: Section 4.3, paragraphs 3 and 4; Figure 5B and legend\n  quote: Fine-tuning with as little as 30 s of data helped reduce both the short and long-term\n    decays in accuracy... In fact, fine-tuning on 120s or 300s led to later decoders outperforming\n    the baseline day 0 decode.\n  depends_on:\n  - fig5a-multiday-short-term\n  criterion: As in continual_learning_lstm.py. Seed days are the 20 listed in STARTING_DAYS (the\n    paper says approximately evenly spaced); an LSTM is trained on the seed day as in\n    fig4a-sameday-stable, then for each later session up to 200 days out it is fine-tuned on the\n    last 30, 60, 120 or 300 s (1500, 3000, 6000 or 15000 bins) of that session's 300 training\n    trials, with 50, 250, 250 or 500 iterations and learning rate from 2e-4 to 1e-5, the input\n    normalizer refit on those samples and the output normalizer kept, and evaluated on that\n    session's hold-out trials; CO is used on two-session days. R2 is averaged across the 20 seeds\n    per relative day. The comparison without fine-tuning is open; the readings are (a) the\n    single-session curve of fig5a-multiday-short-term and (b) the LSTM curve of\n    fig4d-cross-day-decay at positive offsets. Reproduced when, under one reading, 30 s\n    fine-tuning has higher mean R2 than the comparison both over relative days 1 to 10 and over\n    days 100 to 200, and for 120 s and 300 s the mean R2 over days 100 to 200 exceeds the mean\n    day-0 R2 of the seed decoders. Partially reproduced when only one of the two parts holds.\n"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  python tools/claims_check.py claims/temmar-2025.yaml paper/10.52202-085713-4642.txt; grep -n ': .*: \|—\|rather' claims/temmar-2025.yaml | grep -v "^[0-9]*:#" | grep -v "^\s*[0-9]*:\s*- quantity\|quote: \|criterion: \|statement: \|source: " | head
```

Result: not kept, because it reads the paper's text.

**Agent**

The checker passes. A last scan for ": " inside values, em dashes and the banned word:

**Agent calls Bash**

```bash
cd  python3 - <<'E'
import re
for i,l in enumerate(open('claims/temmar-2025.yaml'),1):
    if l.lstrip().startswith('#'): continue
    body=re.sub(r'^\s*(- )?[a-z_]+: ','',l)
    if ': ' in body or '—' in l or re.search(r'\brather\b',l): print(i,l.rstrip())
E
```

```
(Bash completed with no output)
```

**Agent**

I've written `claims/temmar-2025.yaml` and the quote checker passes: 24 claims, 24 quotes, 0 problems. Nothing is committed.

**Text read:** the version of record (the NeurIPS 2025 Datasets and Benchmarks proceedings PDF, as text), including the checklist, plus the supplement from OpenReview: Appendices A to C and Figures S1 to S6. Nothing the claims need is missing. I also read the paper's code, github.com/chesteklab/LINK_dataset at commit 5e1c36a.

**Claims:** 24, all with quotes and none marked `inferred`.
- **Statistics:** none. The paper reports no statistical test or confidence interval for any finding.
- **Expected values:** 6 claims carry them:
  - the dataset counts, with zero tolerance because they count the deposit itself;
  - the SBP slope of -0.033 µV per month;
  - the participation-ratio slope of -0.07 per month;
  - four per-bank SBP slopes and two active/inactive slopes;
  - the shuffled-data R² values (RR -0.166, LSTM -0.156).
- **Criteria:** all 24 have one. Where the paper judges something by eye ("appears", "visually separable", "relatively stable"), I set a decision rule and the criterion says it is not the paper's.

**Details the paper leaves open, with the readings named:**
- **SBP unit in the NWB files:** either scale by 0.25, as the code does, or use the file's stated unit. This could change the slopes by a factor of 4.
- **Figure S4/S5 slopes:** the line is fit either to every channel-day value or to per-day group means. The unit is read as µV/day, and the code for these figures is not in the repository.
- **"Active" channels in the supplement:** it says "< 1 Hz", which I read as a typo for > 1 Hz. It also says the inactive-channel slope is positive, which contradicts the main text's "all categories decreased".
- **"10 dimensions" capturing most of the variance:** read as a participation ratio of at most 10, or the top 10 PCs explaining more than 50%, or more than 80%.
- **Fitts' law throughput:** the formula is only cited (Nason et al.). Three forms are named: with or without the hold time, and Euclidean distance versus a per-finger sum.
- **"Small" circular IQR of tuning angle:** read as under 45° or under 90°, counting all channels or only active ones.
- **Figure 4D:** day offsets signed or absolute, and test-day normalization either held from the training day or refit on the test day (the code makes both).
- **Shuffled baseline:** the session is not named, so I judge it on the median over all sessions.
- **Figure 5B:** the no-fine-tuning comparison is read as either the single-session curve of Figure 5A or the LSTM curve of Figure 4D.

**Where the Methods and the code disagree:** I followed the Methods and named the code's choice as a variant.
- RR inputs: the Methods z-score them; the code does not.
- Movement onset: 1 SD in the Methods, 2 SD in the code, with a different trimming window.
- Fig. 5A: the Methods exclude the first 10 sessions and hold the training-day normalization fixed. The code excludes only the first 5, splits each session 90/10, refits normalization on the test data and adds no training noise.
- Fig. 5B: the code refits the input normalizer each day, which conflicts with the Methods sentence about Figure 5.
- Test set: the code's ends one trial short (74 trials, not 75).

**Missing from the paper:**
- No statistical tests for anything.
- The phrase "long-term decay is not significantly affected" (Fig. 5A) names no test. The criterion uses overlap of the fitted decay rates' confidence intervals, which is my choice, not the paper's.
- The Fig. 5A multi-day training depends on an outside library ("neuraldecoding") that is not in the repository.

## End of run

31 turns, 5 minutes, $2.46 at API prices, result: success.
