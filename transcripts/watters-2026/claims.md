# 000620 · claims · run 39924248065

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cat docs/protocol.md; ls claims/001453/ claims/000620/ paper/ 2>&1; ls tools
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -n '/^## Reader/,/^## [A-QS-Z]/p' docs/protocol.md; ls claims/001453/ claims/000620/ paper/ 2>&1; ls tools
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd paper; wc -l *.txt; head -20 10.64898-2026.01.27.702062.txt; echo ----; head -20 10.64898-2026.10.17.759839.txt
```

```
404 10.64898-2026.01.27.702062.txt
  2139 10.64898-2026.10.17.759839.txt
  2543 total
DOI: 10.64898/2026.01.27.702062
Version: preprint, version 1
Source: bioRxiv JATS XML (api.biorxiv.org)
Stored: 2026-10-20
Extracted: JATS XML flattened
------------------------------------------------------------------------
Working Memory of Multi-Object Scenes in Primate Frontal Cortex

## Abstract

Working memory allows primates to reason about complex scenes, yet how the brain maintains multiple objects in memory simultaneously remains unclear. Competing theories propose that objects are stored in discrete slots 1 , 2 , represented dynamically through switching 3 – 6 , or encoded by weighted combinations of single-object representations 7 – 11 . We formalized these hypotheses in terms of their quantitative predictions at the level of single neurons and tested them against densely recorded neural data from the dorsomedial frontal cortex and frontal eye field of monkeys trained to perform a novel multi-object working-memory task. Across cross-validated neural data, a Gain model, where population activity reflects weighted compositions of individual object responses, consistently outperformed Slot and Switching models. Trial-specific gain estimates predicted behavioral errors and reaction times, indicating that these latent weights capture meaningful fluctuations in memory fidelity. All results replicated in an independent dataset with different spatial configurations. Together, our work provides a rigorous framework to adjudicate a longstanding debate about how the frontal cortex retains multiple objects, identifying a weighted-sum representation as the format that best explains the neural data.

## Introduction

Primates routinely reason about complex visual scenes that contain multiple objects, each with distinct identities, locations, and behavioral relevance. This capacity depends critically on a memory system that can hold information about multiple objects. Yet despite dec
[... 26 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "paper/10.64898-2026.01.27.702062.txt"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.64898-2026.01.27.702062.txt",
 "offset": 241
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  head -150 claims/001453/*.yaml; grep -n "^  - id\|^- id\|^checks" claims/001453/*.yaml | head; wc -l claims/001453/*.yaml
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
[... 141 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 150,321p claims/001453/*.yaml; sed -n 1,80p tools/claims_check.py
```

```
data: with_labels
  depends_on:
  - stimulus-code-link
  criterion: For each fish, the mean of its median angular velocities for the rightward
    stimuli (right, forward right, backward right) minus the mean for the leftward stimuli
    (left, forward left, backward left). Reproduced when this difference is greater than zero
    in each species by a one-sided Wilcoxon signed-rank test at p < 0.05; partially reproduced
    when it holds in one species only. The per-stimulus species medians are reported as well.
- id: fig1h-zf-higher-angular-acceleration
  statement: Across directional stimuli ZF have higher angular acceleration than DC, and the
    distributions of the two species differ for every stimulus.
  source: Results, Optic flow induces angular matching and turns in DC, paragraph 2; Figure 1H
    (Kruskal-Wallis test with Bonferroni correction)
  quote: Across directional stimuli, ZF maintained higher angular acceleration than DC
  statistics:
  - test: Kruskal-Wallis test
    p: 0.05
    p_relation: "<"
    corrected: Bonferroni
  data: with_labels
[... 232 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat schemas/claims.schema.json | head -200
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
[... 180 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 200,400p schemas/claims.schema.json
```

```
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
          "date": {
            "type": "string",
            "format": "date"
          },
          "kind": {
            "enum": [
[... 127 more lines not kept]
```

**Agent**

Now the code repository.

**Agent calls Bash**

```bash
cd $TMPDIR && git clone -q https://github.com/jazlab/multi_object_memory_2025 mom 2>&1 | tail -3; cd mom && git log -1 --format='%H %cd' && find . -type f -not -path './.git/*' | head -200 && cat README.md | head -150
```

```
6e4b333b78cd4461e6373a42378535e8fd392cdb Tue Feb 3 14:20:46 2026 -0500
./task_visualization/videos_with_neurons/Perle_2022-05-31.mp4
./task_visualization/task_state.py
./task_visualization/resources/objects/tomato.jpg
./task_visualization/resources/objects/strawberry.jpg
./task_visualization/resources/objects/plum.jpg
./task_visualization/resources/objects/kiwi.jpg
./task_visualization/resources/objects/c.jpg
./task_visualization/resources/objects/banana.jpg
./task_visualization/resources/objects/b.jpg
./task_visualization/resources/objects/apple.jpg
./task_visualization/resources/objects/a.jpg
./task_visualization/resources/foveal_window.npy
./task_visualization/resources/background_noise.npy
./task_visualization/resources/audio/click_2.mp3
./task_visualization/resources/audio/click_1.mp3
./task_visualization/resources/audio/click_0.mp3
./task_visualization/renderer.py
./task_visualization/gifs/Perle_2022-06-01_trial_200.gif
./task_visualization/gif_writer.py
[... 331 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/mom; find figures behavior_processing phys_processing -type f \( -name '*.py' -o -name '*.ipynb' -o -name '*.md' \) | grep -v readme_visuals; ls; cat phys_processing/spikes_to_trials/constants.py phys_processing/README.md | head -150
```

```
figures/supp_fig_stimulus/selectivity_correlation/selectivity_correlation.ipynb
figures/supp_fig_stimulus/selectivity_correlation/run_cache_data.py
figures/supp_fig_stimulus/orthogonality/run_cache_data.py
figures/supp_fig_stimulus/orthogonality/orthogonality.ipynb
figures/supp_fig_stimulus/firing_rate_correlation/firing_rate_correlation.ipynb
figures/supp_fig_noise_corr/plot_example_units.ipynb
figures/supp_fig_hyperparams/hyperparams.ipynb
figures/supp_fig_general_slot/general_slot.ipynb
figures/supp_fig_decoding/modeling/trainer.py
figures/supp_fig_decoding/modeling/run_training.py
figures/supp_fig_decoding/modeling/run_2_triangle_complement.py
figures/supp_fig_decoding/modeling/run_2_triangle.py
figures/supp_fig_decoding/modeling/run_2_ring.py
figures/supp_fig_decoding/modeling/run_1_triangle.py
figures/supp_fig_decoding/modeling/models.py
figures/supp_fig_decoding/modeling/labelers.py
figures/supp_fig_decoding/modeling/dataset.py
figures/supp_fig_decoding/modeling/config_2_triangle_complement.py
figures/supp_fig_decoding/modeling/config_2_triangle.py
figures/supp_fig_decoding/modeling/config_2_ring.py
[... 147 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/mom; cat > /tmp/nb.py 2>/dev/null || true; cat > $TMPDIR/nb.py <<'EOF'
import json,sys
for f in sys.argv[1:]:
    nb=json.load(open(f))
    print("=====",f)
    for c in nb['cells']:
        if c['cell_type']=='code':
            print(''.join(c['source']))
            for o in c.get('outputs',[]):
                t=o.get('text') or o.get('data',{}).get('text/plain')
                if t: print('  >>', ''.join(t)[:600])
            print('---')
        else:
            print('#MD', ''.join(c['source'])[:400])
EOF
python $TMPDIR/nb.py figures/figure_1/performance/performance.ipynb figures/figure_1/reaction_times/reaction_times.ipynb; cat behavior_processing/README.md; sed -n 1,200p behavior_processing/load_triangle_data.py
```

```
Exit code 143
Command timed out after 1h 0m 0s
```

**Agent calls Bash**

```bash
cd $TMPDIR/mom; cat > $TMPDIR/nb.py <<'EOF'
import json,sys
for f in sys.argv[1:]:
    nb=json.load(open(f))
    print("=====",f)
    for c in nb['cells']:
        if c['cell_type']=='code':
            print(''.join(c['source']))
            for o in c.get('outputs',[]):
                t=o.get('text') or o.get('data',{}).get('text/plain')
                if t: print('  >>', ''.join(t)[:600])
            print('---')
        else:
            print('#MD', ''.join(c['source'])[:400])
EOF
python $TMPDIR/nb.py figures/figure_1/performance/performance.ipynb figures/figure_1/reaction_times/reaction_times.ipynb < /dev/null; cat behavior_processing/README.md
```

```
===== figures/figure_1/performance/performance.ipynb
#MD # Notebook to generate performance plot for each monkey.

This notebook requires the processed behavior data for the triangle task, saved
in `../../../cache/behavior/triangle.csv`. This can be downloaded from the GitHub
repo or can be generated by running the script
`../../../behavior_processing/run_cache_data.py`.
"""Imports."""

from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

import sys
sys.path.append('../../../behavior_processing')
import load_triangle_data
import load_ring_data

# Matplotlib settings
[... 244 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/mom; cat behavior_processing/load_triangle_data.py behavior_processing/load_ring_data.py; sed -n 1,400p behavior_processing/run_cache_data.py
```

```
"""Utilities for triangle dataset analysis."""

from pathlib import Path

import numpy as np
import pandas as pd

DATA_PATH = Path(__file__).parent / "../cache/behavior_processing/triangle.csv"
RADIUS = 0.35  # Radius of the triangle
TRIANGLE_THETAS = [
    0,  # right
    2 * np.pi / 3,  # top-left
    4 * np.pi / 3,  # bottom-left
]
TRIANGLE_POSITIONS = [
    (RADIUS * np.cos(theta), RADIUS * np.sin(theta))
    for theta in TRIANGLE_THETAS
]


[... 422 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/mom; cat phys_processing/spikes_to_trials/run_firing_rates_per_phase.py; sed -n 1,200p phys_processing/spikes_to_trials/run_spikes_per_trial.py
```

```
"""Run this script to compute and cache firing rates per phase.

Usage:
$ python3 run_firing_rates_per_phase.py

For this script to work, you need to have already run the spike counts script
"run_spikes_per_trial.py" to generate spike counts for each unit.

This computes a dataframe for each session with columns:
- probe
- quality
- unit
- trial
- firing_rate_stimulus
- firing_rate_delay

This dataframe is saved to a file
"../cache/phys_processing/spikes_to_trials/delay_phase_firing_rates/$SUBJECT/$SESSION/fr.csv"

This script requires the following cached data:
[... 407 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/mom; cat phys_processing/selectivity/auc.py; sed -n 1,200p phys_processing/selectivity/run_cache_selectivity.py; cat phys_modeling/training/unit_filters.py phys_modeling/training/trial_filters.py
```

```
"""ROC analysis."""

import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt


def _compute_auc(labels):
    """Compute area under the ROC curve."""
    if labels.ndim != 2 or labels.shape[1] != 2:
        raise ValueError("Labels must be a 2D array with two columns.")

    # Compute ROC curve
    tp = np.cumsum(labels[:, 0])
    fp = np.cumsum(labels[:, 1])
    fn = np.sum(labels[:, 0]) - tp
    tn = np.sum(labels[:, 1]) - fp
    tpr = tp / (tp + fn)
    fpr = fp / (fp + tn)
[... 395 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/mom; sed -n 200,320p phys_processing/selectivity/run_cache_selectivity.py; cat phys_modeling/README.md | head -120
```

```
continue

            # Load behavior data for this session
            session_behavior_triangle = triangle_behavior[
                (triangle_behavior["subject"] == subject)
                & (triangle_behavior["session"] == session)
            ]
            session_behavior_ring = ring_behavior[
                (ring_behavior["subject"] == subject)
                & (ring_behavior["session"] == session)
            ]
            if len(session_behavior_triangle) > 0:
                print(f"Triangle data found")
                session_behavior = session_behavior_triangle
            elif len(session_behavior_ring) > 0:
                print(f"Ring data found")
                session_behavior = session_behavior_ring
            else:
                raise ValueError("No behavior data found")

[... 117 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/mom; python $TMPDIR/nb.py figures/figure_2/selectivity/selectivity.ipynb figures/figure_2/noise_correlations/plot_noise_vs_signal_correlation.ipynb < /dev/null | grep -v "^plt.rcParams" | head -400; cat figures/figure_2/noise_correlations/README.md
```

```
===== figures/figure_2/selectivity/selectivity.ipynb
#MD # Notebook to generate selectivity plots.

This notebook requires the cached selectivity data in
`../../../cache/phys_processing/selectivity`. See
`../../../phys_processing/selectivity` for details of how to generate this.

This notebook generates selectivity plots for both monkeys for both Triangle and
Ring datasets, and saves these plots to the current directory.

At the bottom of this notebook 
"""Imports."""

from matplotlib import pyplot as plt
from matplotlib import patheffects
import numpy as np
import pandas as pd
from pathlib import Path
import seaborn as sns

[... 325 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/mom; cat figures/figure_2/noise_correlations/run_compute_triangle.py
```

```
"""Compute and cache delay phase noise correlations for the triangle dataset.

This will compute the noise correlations for all triangle dataset sessions and
save them to `../../../cache/figures/figure_2/noise_correlations`.
"""

from pathlib import Path

import numpy as np
import pandas as pd

_BEHAVIOR_CACHE_PATH_TRIANGLE = Path(
    "../../../cache/behavior_processing/triangle.csv"
)
_SELECTIVITY_DATA_DIR = Path("../../../cache/phys_processing/selectivity")
_FIRING_RATES_DATA_DIR = Path(
    "../../../cache/phys_processing/spikes_to_trials/delay_phase_firing_rates"
)
_WRITE_DIR = Path(
    "../../../cache/figures/figure_2/noise_correlations_triangle"
[... 276 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/mom; python $TMPDIR/nb.py figures/figure_4/model_comparison/model_comparison.ipynb < /dev/null | grep -v "^plt.rcParams" | head -300
```

```
===== figures/figure_4/model_comparison/model_comparison.ipynb
#MD # Notebook to generate model likelihood plot

This notebook requires the modeling results data, saved in
`../../cache/phys_modeling_logs/main`. This can be downloaded from the OSF
repo or can be generated by training the models yourself.
"""Imports."""

import json
import torch
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
from pathlib import Path
from scipy import stats as scipy_stats

# Matplotlib settings
---
"""Load results."""
[... 280 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/mom; python $TMPDIR/nb.py figures/figure_4/model_comparison/model_comparison.ipynb < /dev/null | grep -v "^plt.rcParams" | sed -n 300,500p | grep -v "^\s*$"
```

```
# Add scatterplot of means
    mean_per_session_df = subject_df.groupby(["model", "session"])[["num_neurons", "prob"]].mean().reset_index()
    mean_per_session_df = mean_per_session_df.sort_values(by=["model", "prob"]).reset_index(drop=True)
    mean_per_session_df["model"] = mean_per_session_df["model"].map(
        {name: i for i, name in enumerate(MODEL_ORDER)})
    for i in range(3):
        y_mean = np.mean(mean_per_session_df[mean_per_session_df["model"] == i]["prob"])
        y_ci = scipy_stats.sem(mean_per_session_df[mean_per_session_df["model"] == i]["prob"]) * 1.96
        y_safezone = (y_mean - y_ci - 0.01, y_mean + y_ci + 0.01)
        for j, row in mean_per_session_df[mean_per_session_df["model"] == i].iterrows():
            parity = j % 2
            mean_per_session_df.loc[j, "model"] += _add_x_jitter(
                row,
                y_safezone,
                parity,
            )
    sns.scatterplot(
        data=mean_per_session_df,
        x="model",
        y="prob",
[... 59 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/mom; python $TMPDIR/nb.py figures/figure_4/attention_behavior/performance_reaction_time.ipynb < /dev/null | grep -v "^plt.rcParams" | grep -v "^\s*$" | head -400
```

```
===== figures/figure_4/attention_behavior/performance_reaction_time.ipynb
#MD # Notebook to generate attention versus performance plots.
This notebook requires the processed behavior data for the triangle task, saved
in `../../../cache/behavior/triangle.csv`. This can be downloaded from the OSF
repo or can be generated by running the script
`../../../behavior_processing/run_cache_data.py`.
This notebook also requires the modeling results data, saved in
`../../cache/phys_m
"""Imports."""
import json
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
from pathlib import Path
from scipy.stats import pearsonr
import sys
sys.path.append('../../../behavior_processing')
import load_triangle_data
# Matplotlib settings
[... 381 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/mom; python $TMPDIR/nb.py figures/figure_5/attention_behavior/performance.ipynb figures/figure_5/attention_behavior/reaction_time.ipynb < /dev/null | grep -v "^plt.rcParams" | grep -v "^\s*$" | grep -v Warning | head -400
```

```
===== figures/figure_5/attention_behavior/performance.ipynb
#MD # Notebook to generate attention versus performance plots.
This notebook requires the processed behavior data for the triangle task, saved
in `../../../cache/behavior/triangle.csv`. This can be downloaded from the OSF
repo or can be generated by running the script
`../../../behavior_processing/run_cache_data.py`.
This notebook also requires the modeling results data, saved in
`../../cache/phys_m
"""Imports."""
import json
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
from pathlib import Path
from scipy.stats import pearsonr
import sys
sys.path.append('../../../behavior_processing')
import load_ring_data
# Matplotlib settings
[... 381 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/mom; python $TMPDIR/nb.py figures/figure_5/attention_behavior/reaction_time.ipynb < /dev/null | grep -v "^plt.rcParams" | grep -v "^\s*$" | grep -v Warning | sed -n 95,250p | grep -n "groupby\|pearsonr\|regplot\|data=\|Subject\|R =\|filter\|num_objects\|>>"
```

```
9:    & (df_attn["num_objects"] == 2)
51:    df_subject_per_trial = df_subject.groupby(
60:    sns.regplot(
62:        data=df_subject_per_trial,
71:        data=df_subject_per_trial,
92:    corr = pearsonr(x_vals, y_vals)[0]
93:    p_value = pearsonr(x_vals, y_vals)[1]
101:    print(f"R = {corr:8f}, corr_sem: {corr_sem}, p-value: {p_value}")
130:  >> R = -0.136126, corr_sem: 0.011361280559181086, p-value: 3.6735048073961366e-35
131:R = -0.028062, corr_sem: 0.011823567832684246, p-value: 0.017902380132983994
133:  >> <Figure size 1350x750 with 2 Axes>
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/mom; for f in figures/figure_5/model_comparison/model_comparison.ipynb figures/figure_4/model_comparison/identifiability.ipynb figures/supp_fig_controls/controls.ipynb figures/supp_fig_general_slot/general_slot.ipynb; do python $TMPDIR/nb.py $f < /dev/null | grep -v Warning | grep -A40 ">>" | grep -v "^\s*$" | head -60; done
```

```
>> Elgar 2022-09-06
Elgar 2022-09-07
Elgar 2022-09-09
Elgar 2022-09-10
Elgar 2022-09-11
Elgar 2022-09-12
Elgar 2022-09-13
Elgar 2022-09-14
Elgar 2022-09-15
Elgar 2022-09-20
Perle 2022-06-07
Perle 2022-06-09
Perle 2022-06-10
Perle 2022-06-11
Perle 2022-06-12
Perle 2022-06-13
Perle 2022-06-14
Perle 2022-06-15
Perle 2022-06-16
Perle 2022-06-19
[... 124 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/mom; python $TMPDIR/nb.py figures/figure_5/model_comparison/model_comparison.ipynb < /dev/null | grep -B2 -A30 "Subject: Elgar$" | head -50; python $TMPDIR/nb.py figures/figure_5/model_comparison/model_comparison.ipynb figures/supp_fig_controls/controls.ipynb figures/supp_fig_general_slot/general_slot.ipynb figures/figure_4/model_comparison/identifiability.ipynb < /dev/null | grep -n "=====\|ttest\|if p <\|trials_per_bootstrap=\|_compute_bootstrap_probs(\|SEEDS =\|MODEL_DIRS = \|BASE_RESULTS_DIR =\|DATASETS ="
```

```
print(f"Number of sessions where Gain model is best: {gain_best_count} / {len(gain_best)}\n")

  >> Subject: Elgar
Mean probabilities per model:
model
Gain         0.382799
Slot         0.311215
Switching    0.305986
Name: prob, dtype: float64
Number of sessions where Gain model is best: 9 / 10

Subject: Perle
Mean probabilities per model:
model
Gain         0.569743
Slot         0.221950
Switching    0.208307
Name: prob, dtype: float64
Number of sessions where Gain model is best: 10 / 10

[... 47 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/mom; cat phys_modeling/configs/neural/triangle_gain.py; sed -n 1,140p phys_modeling/training/dataset.py
```

```
"""Config."""


def _get_dataset_config():
    config = dict(
        constructor=dict(
            module="dataset",
            method="Dataset",
        ),
        kwargs=dict(
            subject="Perle",
            session="2022-06-01",
            # session='2022-05-31',
            # subject='Elgar',
            # session='2022-08-26',
            # session='2022-08-22',
            phase="delay",
            unit_filter=dict(
                constructor=dict(
                    module="unit_filters",
[... 197 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/mom; cat phys_modeling/constants.py; sed -n 140,260p phys_modeling/training/dataset.py | grep -n "def \|min_\|test\|rand"
```

```
"""Constants."""

import os
from pathlib import Path

################################################################################
####  Paths
################################################################################

_CURRENT_DIR = Path(os.path.realpath(__file__)).parent
SPIKES_PER_TRIAL_DIR = (
    _CURRENT_DIR / "../cache/phys_processing/spikes_to_trials/spikes_per_trial"
)
BEHAVIOR_DIR_TRIANGLE = (
    _CURRENT_DIR / "../cache/behavior_processing/triangle.csv"
)
BEHAVIOR_DIR_RING = _CURRENT_DIR / "../cache/behavior_processing/ring.csv"
SELECTIVITY_DIR = _CURRENT_DIR / "../cache/phys_processing/selectivity"

################################################################################
[... 23 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -rl "000620" --include=*.json --include=*.yaml --include=*.md --include=*.csv . 2>/dev/null | grep -v "^./transcripts" | head
```

```
./targets/dandisets.json
./papers/manifest.yaml
./attempts/000130-sohn-2019-01.yaml
```

**Agent calls Bash**

```bash
cd  python - <<'EOF'
import json
d=json.load(open('targets/dandisets.json'))
items = d if isinstance(d,list) else d.get('dandisets', d)
for x in (items if isinstance(items,list) else items.values()):
    if '000620' in json.dumps(x)[:300]:
        print(json.dumps(x,indent=1)[:3000]); break
EOF
grep -n -B2 -A8 "000620" papers/manifest.yaml | head -30
```

```
876-    pdf: false
877-    supplements: 0
878:  '000620':
879-  - doi: 10.64898/2026.01.27.702062
880-    status: stored
881-    version: preprint, version 1
882-    source: bioRxiv JATS XML (api.biorxiv.org)
883-    pdf: false
884-    supplements: 0
885-  - doi: 10.64898/2026.10.17.759839
886-    status: stored
```

**Agent calls Bash**

```bash
cd  grep -n -A12 '"000620"' targets/dandisets.json | head -40
```

```
2976:   "dandiset": "000620",
2977-   "name": "Multi-object working memory in macaque frontal cortex (N. Watters, J. Gabel, J. Tenenbaum, M. Jazayeri)",
2978-   "published_version": "0.261019.2000",
2979-   "asset_count": 142,
2980-   "size_gb": 5490.11,
2981-   "data_standards": [
2982-    "Neurodata Without Borders (NWB)"
2983-   ],
2984-   "species": [
2985-    "Macaca mulatta - Rhesus monkey"
2986-   ],
2987-   "approaches": [
2988-    "electrophysiological approach",
```

**Agent calls Bash**

```bash
cd $TMPDIR/mom; sed -n 1,400p figures/figure_5/noise_correlations/run_compute_ring.py | grep -v "^\s*$" | head -220
```

```
"""Compute and cache delay phase noise correlations for the ring dataset.
This will compute the noise correlations for all ring dataset sessions and
save them to `../../../cache/figures/figure_5/noise_correlations`.
"""
import sys
from pathlib import Path
import numpy as np
import pandas as pd
from scipy.stats import pearsonr
sys.path.append("../../../behavior_processing")
import load_ring_data
_BASE_NEURAL_DIR = Path(
    "../../../cache/phys_processing/spikes_to_trials/delay_phase_firing_rates"
)
_BASE_SELECTIVITY_DIR = Path("../../../cache/phys_processing/selectivity")
_BASE_WRITE_DIR = Path(
    "../../../cache/figures/figure_5/noise_correlations_ring"
)
def cache_noise_correlations(df_behavior):
    subject = df_behavior.subject.unique()
[... 193 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/mom; python $TMPDIR/nb.py figures/figure_5/noise_correlations/noise_correlations.ipynb figures/figure_5/performance_reaction_time/performance.ipynb < /dev/null | grep -v "^plt.rcParams" | grep -v "^\s*$" | grep -v Warning | grep -n "df\[\|bin\|>>\|filter\|mean_firing\|significant\|Monkey\|lineplot\|task\|load_data" | head -60
```

```
24:        df['subject'] = subject_dir.name
25:        df['session'] = session_dir.name
28:df = df[
29:    (df["num_signal_trials"] >= 50)
30:    & (df["num_noise_trials"] >= 200)
33:  >> Index(['unit_0', 'unit_1', 'signal_ccs', 'noise_ccs', 'num_signal_trials',
45:    df_subjects = df[df["subject"].isin(subjects)].copy().reset_index(drop=True)
46:    # Make bins for signal correlation
47:    bin_edges = np.linspace(-span, span, _NUM_BINS + 1)
48:    bin_centers = (bin_edges[1:] + bin_edges[:-1]) / 2
49:    bin_edges[0] = -np.inf
50:    bin_edges[-1] = np.inf
51:    df_subjects["signal_corr_bin"] = pd.cut(df_subjects["signal_ccs"], bin_edges, labels=bin_centers)
56:        sns.lineplot(
59:            x="signal_corr_bin",
66:    sns.lineplot(
69:        x="signal_corr_bin",
79:        ax.set_title('Monkey ' + subjects[0][0])
81:        ax.set_title('Monkeys ' + ' and '.join([s[0] for s in subjects]))
85:  >> <Figure size 870x870 with 1 Axes>
[... 41 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/mom; python $TMPDIR/nb.py figures/figure_5/noise_correlations/noise_correlations.ipynb < /dev/null | grep -v "^plt.rcParams" | grep -v "^\s*$" | sed -n 36,50p; python $TMPDIR/nb.py figures/supp_fig_decoding/analysis/decodability.ipynb figures/supp_fig_attn_distribution/attention_distribution.ipynb < /dev/null | grep -v "^plt.rcParams" | grep -v "^\s*$" | grep -v Warning | grep -n ">>\|SESSIONS\|session\|shuffle" | head -40
```

```
---
"""Make plot."""
SUBJECTS_SPANS = [
    (('Perle',), 0.8, (-0.16, 0.25)),
    (('Elgar',), 0.3, (-0.1, 0.15)),
    (('Perle', 'Elgar'), 0.8, (-0.16, 0.28)),
]
_NUM_BINS = 8
for subjects, span, ylim in SUBJECTS_SPANS:
    df_subjects = df[df["subject"].isin(subjects)].copy().reset_index(drop=True)
    # Make bins for signal correlation
    bin_edges = np.linspace(-span, span, _NUM_BINS + 1)
    bin_centers = (bin_edges[1:] + bin_edges[:-1]) / 2
    bin_edges[0] = -np.inf
    bin_edges[-1] = np.inf
27:    "session": [],
37:            for subject_session_dir in brain_area_dir.iterdir():
38:                subject = subject_session_dir.stem.split("_")[0]
39:                session = subject_session_dir.stem.split("_")[1]
40:                if session not in ["2022-06-01", "2022-06-04", "2022-05-31"]:
[... 25 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/mom; cat figures/supp_fig_decoding/modeling/README.md | head -40; grep -v "^\s*$" figures/supp_fig_decoding/modeling/config_1_triangle.py | head -80; grep -n "class\|def \|loss\|argmax\|softmax\|mse" figures/supp_fig_decoding/modeling/models.py figures/supp_fig_decoding/modeling/trainer.py | head -40
```

````
# Decoding Models

This directory contains code for running decoding models.

## Getting Started

To train a decoding model, run
```
$ python run_training.py
```
Be sure to run this from a virtual environment with the dependencies in
`../requirements.txt` installed. Also be sure to have cached the spiking data
(see `../../phys_processing/spikes_to_trials/run_spikes_per_trial.py` for
details).

This will train a decoding model, by default on 1-object Triangle dataset
conditions. To decoding models on other datasets, change the `_CONFIG` flag at
the top of `run_training.py`.

## Running sweeps
[... 81 more lines not kept]
````

**Agent**

I have what I need from the paper and code. Writing the claims file now.

**Agent calls Bash**

```bash
cd $TMPDIR/mom; grep -n "SPIKE_COUNT\|min_trials\|time_noise\|kappa\|stop_step" phys_modeling/configs/neural/ring_gain.py phys_modeling/configs/neural/triangle_slot_partition.py | head; grep -n "num_slots\|n_slots" phys_modeling/configs/neural/*.py | head -5; ls cache 2>/dev/null | head
```

```
phys_modeling/configs/neural/ring_gain.py:47:            time_noise_sigma=0.1,
phys_modeling/configs/neural/ring_gain.py:69:            stop_step=None,
phys_modeling/configs/neural/triangle_slot_partition.py:51:            time_noise_sigma=0.1,
phys_modeling/configs/neural/triangle_slot_partition.py:74:            stop_step=None,
phys_modeling/configs/neural/ring_slot.py:50:            n_slots=2,
phys_modeling/configs/neural/ring_slot_partition.py:50:            n_slots=2,
phys_modeling/configs/neural/triangle_slot.py:53:            n_slots=2,
phys_modeling/configs/neural/triangle_slot_partition.py:53:            n_slots=2,
placeholder.txt
Shell cwd was reset to
```

**Agent calls Write**

```json
{
 "file_path": "claims/000620/10.64898-2026.01.27.702062.yaml",
 "content": "# Claims for Watters, Gabel, Tenenbaum & Jazayeri (2026), \"Working Memory of Multi-Object Scenes in\n# Primate Frontal Cortex\", on dandiset 000620.\n#\n# Provenance: written by an agent (model \"claude-opus-5-5\", Claude Code in GitHub Actions),\n# 2026-10-23, protocol pilot-10 as stated in docs/protocol.md.\n#\n# Text read: the bioRxiv preprint, version 1 (doi:10.64898/2026.01.27.702062), full text from the\n# bioRxiv JATS XML (paper/10.64898-2026.01.27.702062.txt): main text, Methods, and the legends of\n# Extended Data Figures 1 to 11. There is no separate supplement. No PDF was supplied, so figure\n# panels could not be looked at; the JATS text drops the display equations of the models (they are\n# described in words in the Results and Methods) and garbles the statistics of Extended Data Fig. 8a.\n#\n# Code read: https://github.com/jazlab/multi_object_memory_2025 at commit\n# 6e4b333b78cd4461e6373a42378535e8fd392cdb (2026-02-03), the repository the Methods link. It holds\n# behavior_processing/ (NWB trials to per-trial tables, with \"correct\" and reaction time),\n# phys_processing/ (per-trial spike counts in 10 ms bins, delay-phase rates, AUC selectivity and the\n# unit selection for modeling), phys_modeling/ (the Slot, Switching and Gain models in PyTorch, their\n# configs, training, synthetic data and sweeps), and figures/ (one notebook per panel, several with\n# printed outputs). Intermediate results (fitted models, caches) are on OSF (osf.io/vyw49), named by\n# the code's README, not by the paper; no claim's test uses them.\n#\n# Data the paper used. Two rhesus macaques: Monkey P (female, 10 years, 8 kg; \"Perle\" in the code)\n# and Monkey E (male, 10 years, 12 kg; \"Elgar\"). Task: fixation, 1 s stimulus of 1 to 3 fruit images\n# (apple, blueberry, orange during physiology; ids \"a\", \"b\", \"c\" in the code) at 8.4 degrees\n# eccentricity, 1 s delay, a cue (one of the shown fruits) at fixation for 180 ms, then a saccade to\n# the remembered location of the cued object. Two datasets. Triangle: 1 to 3 objects on the vertices\n# of an equilateral triangle (right, top-left, bottom-left), in performance-conditioned blocks, with\n# 10% of 2- and 3-object trials at random positions (excluded from analysis); 24 sessions, 10 from P\n# (2022-05-26 to 2022-06-05 in the code) and 14 from E (2022-08-19 to 2022-09-05). Ring: 1 or 2\n# objects at positions uniform on a circle, plus 5% left/right 2-object trials; 22 sessions, 10 from P\n# and 12 from E (the code's Ring model comparison lists 20, 10 per monkey: P 2022-06-07 to 06-19, E\n# 2022-09-06 to 09-20). Recording: right DMFC with a Neuropixels 1.0 probe (probe \"s0\" in the code)\n# and left FEF with 64-channel Plexon V-probes (\"vprobe0\", \"vprobe1\"); Kilosort 2.5, units labelled\n# single (\"good\") or multi-unit (\"mua\"); each unit has a stable interval (the code reads it from the\n# units table as obs_trials). Measured variables: trial events (stimulus, delay, cue, response,\n# feedback onsets), object positions and identities, the target, the response position and time,\n# broken fixation, and spike times.\n#\n# Shared definitions, cited from the paper or its code, used by the criteria below.\n# T1 trials. Completed trials only, those without broken fixation and with a finite response time\n#   (behavior_processing/run_cache_data.py). Triangle analyses use only trials whose objects all lie\n#   on the triangle vertices (Methods, Behavioral Task, paragraph on the Triangle dataset; code\n#   on_triangle). Ring analyses use all conditions (Methods, \"We used all conditions for analysis\");\n#   the code drops the left/right 2-object trials from selectivity and modeling\n#   (phys_modeling/training/trial_filters.py), shown as a variant.\n# T2 correct. Methods (Feedback phase) say a response is correct within 2.4 degrees of the target\n#   centre; the code (load_triangle_data.py, load_ring_data.py) uses 0.2 arena widths, 4.8 degrees.\n#   Open; both readings are run wherever correctness enters.\n# T3 reaction time. Response time minus cue onset (code); the Fig. 1c legend says cue onset to onset\n#   of the response saccade and drops saccades earlier than 180 ms as broken fixation.\n# T4 delay-phase rate. Spike count from delay onset to cue onset divided by its duration\n#   (phys_processing/spikes_to_trials/run_firing_rates_per_phase.py; Extended Data Fig. 2 legend);\n#   stimulus-phase rate from stimulus onset to delay onset (0 to 1000 ms). The models use 1000 to\n#   2000 ms after stimulus onset in 10 ms bins (phys_modeling/constants.py).\n# T5 units. Spikes outside a unit's stable interval excluded; units with delay-phase mean rate below\n#   1 Hz excluded (Methods, Data Processing; code threshold > 1 Hz). The Methods also exclude units\n#   stable for fewer than 500 trials; the code's modeling dataset requires 200 trials per unit and 5\n#   units per trial (phys_modeling/training/dataset.py). Both qualities, good and mua, are used by the\n#   code everywhere (unit_filters.py, selectivity notebook).\n# T6 AUC. As in Methods, Receiver-Operator Characteristics, on 1-object trials: for each pair of the\n#   three labels the AUC folded to be at least 0.5; the unit's value is the largest AUC among pairs\n#   with p < 0.05, or the largest overall if none is. Ring trials are labelled by the nearest triangle\n#   vertex (three 120-degree sectors). The p-value is open: the Methods shuffle labels 1,000 times;\n#   the code (phys_processing/selectivity/auc.py) uses 5,000 bootstrap resamples, takes the pair of\n#   lowest p when none is significant, and drops the Ring left/right trials. Both are run. The Fig. 2b\n#   legend calls the AUC values cross-validated; neither the Methods nor the code says how, so the\n#   uncross-validated value of the Methods is used and this is recorded as a deviation.\n# T7 modeling. As in Methods, Modeling to Model Comparison, with the code's configs\n#   (phys_modeling/configs/neural/{triangle,ring}_{slot_partition,switching,gain}.py). Units entered\n#   when position or identity AUC > 0.65 with p < 0.05 and delay rate > 1 Hz (Methods, Model-Fitting;\n#   run_cache_selectivity.py). The main Slot model is the disjoint-neuron one (\"slot_partition\") with\n#   2 slots. Ten train/test splits per session (seeds 2 to 11 in the code), each neuron-trial pair in\n#   test with probability 0.2. Temporal noise kappa (0 to 200 ms by 20 ms) and the stopping step\n#   (within 10,000 steps) tuned per session and model on two splits. Adam, learning rate 0.003,\n#   gradient clipping 1, per-trial parameters frozen for the first 1000 steps. Model likelihood of a\n#   split is, as in figures/figure_4/model_comparison/model_comparison.ipynb, the mean over 1000\n#   bootstraps of the softmax across the three models of the test log-likelihood summed over 100\n#   neuron-trial pairs drawn with replacement; a session's value is the mean over its splits.\n# T8 gain. A trial's gain of an object is the sigmoid of the fitted W at the stopping step of each\n#   split (\"attention.npy\" in the code); \"averaged over random seeds\" means over the ten splits.\nschema_version: 2\ndataset:\n  archive: dandi\n  id: \"000620\"\npaper: doi:10.64898/2026.01.27.702062\nclaims:\n- id: fig1b-performance-load\n  statement: In both monkeys accuracy falls as the number of objects grows, yet stays far above the\n    chance of saccading to a random stimulus object for two- and three-object stimuli.\n  source: Results, Task, Behavior, and Hypotheses, paragraph 1; Figure 1b\n  quote: Animals learned the task and exhibited variable reaction times, with error rates increasing\n    as the number of objects grew ... However, performance remained far above chance for two- and\n    three-object stimuli\n  criterion: >-\n    Per monkey, the fraction correct (T2) of completed trials (T1) for 1, 2 and 3 objects; chance is\n    1/n, as the Fig. 1b legend defines it. Reproduced when, for both monkeys, the fraction falls from\n    1 to 2 to 3 objects and the 2- and 3-object fractions lie above 1/2 and 1/3. The paper gives no\n    test; \"far above\" is not given a number, so the margin is reported and not judged. Which trials\n    form the figure is open: (a) Triangle trials on the triangle only, as the paper's\n    figures/figure_1/performance/performance.ipynb plots; (b) Triangle and Ring trials pooled, as the\n    legend says (the Ring has no 3-object trials). Each reading is run under both correctness radii\n    of T2. For reference, that notebook printed, for reading (a) with the code's radius, P 0.953,\n    0.93, 0.692 and E 0.928, 0.759, 0.561 for 1, 2, 3 objects; these are reported against, not used\n    to judge.\n- id: fig1c-reaction-times\n  statement: Reaction times, from cue onset to the response saccade, vary from trial to trial, with\n    trials faster than 180 ms counted as broken fixation.\n  source: Results, Task, Behavior, and Hypotheses, paragraph 1; Figure 1c legend\n  quote: Animals learned the task and exhibited variable reaction times\n  criterion: >-\n    Per monkey, reaction times (T3) of completed Triangle trials on the triangle, correct and\n    incorrect apart, as in figures/figure_1/reaction_times/reaction_times.ipynb, which bins them from\n    100 to 600 ms and shows 150 to 500 ms. The paper fixes no measure of variability. Reproduced when\n    the distribution of each monkey is not degenerate (interquartile range above one 10 ms bin) and\n    its median lies inside the plotted 150 to 500 ms range; the histograms, quartiles and the share\n    of trials under 180 ms are reported.\n- id: ext1-misbinding-errors\n  statement: A common error is a saccade to the location of a non-target stimulus object, reporting\n    the cued identity at the wrong location.\n  source: Discussion, Position-identity binding, paragraph 1; Extended Data Fig. 1\n  quote: A common error in our task occurs when the monkey reports the identity of an object at the\n    wrong location ( Extended Data Fig. 1 ), consistent with misbinding in working memory\n  criterion: >-\n    Completed Triangle trials on the triangle with 2 or 3 objects, per monkey. Each response is\n    assigned to the triangle vertex within the correctness radius (T2), as in load_triangle_data.py\n    (response_location), and counted by target location and response location as in Extended Data\n    Fig. 1. Among incorrect trials, the share whose response lies at a non-target object's vertex.\n    The paper gives no number for \"common\"; two readings are run, (a) these responses are the largest\n    class of errors (against responses at an empty vertex or at no vertex), and (b) they are more\n    than half of the errors. Reproduced when both readings hold for both monkeys and both set sizes;\n    otherwise the shares are reported and the claim is judged on the readings that agree.\n- id: triangle-unit-counts\n  statement: The Triangle dataset holds 4,688 neurons, 2,937 in DMFC and 1,751 in FEF, from 24\n    sessions, 10 from Monkey P and 14 from Monkey E.\n  source: Results, The Triangle Dataset, paragraph 1; Methods, Neurophysiology, last paragraph\n  quote: We recorded 4,688 well-isolated neurons (2,937 from DMFC and 1,751 from FEF) in the Triangle\n    dataset across 24 sessions\n  expected:\n  - quantity: Triangle units, total\n    value: 4688\n    tolerance: 469\n  - quantity: Triangle units, DMFC\n    value: 2937\n    tolerance: 294\n  - quantity: Triangle units, FEF\n    value: 1751\n    tolerance: 175\n  - quantity: Triangle sessions, Monkey P\n    value: 10\n    tolerance: 0\n  - quantity: Triangle sessions, Monkey E\n    value: 14\n    tolerance: 0\n  criterion: >-\n    Sessions are the counts stated in Methods, Neurophysiology, so no tolerance. Unit counts take the\n    default 10%. Which units are counted is open: (a) good and mua units with delay-phase rate above\n    1 Hz on Triangle trials, which is how figures/figure_2/selectivity/selectivity.ipynb printed\n    4688, 2937 and 1751; (b) as (a) and also stable for at least 500 trials (T5, Methods); (c) good\n    units only, reading \"well-isolated\" literally. Reproduced when all five values match under one\n    reading. DMFC is probe s0, FEF the V-probes.\n- id: ring-unit-counts\n  statement: The Ring dataset holds 3,051 neurons, 1,712 in DMFC and 1,339 in FEF, from 22 sessions,\n    10 from Monkey P and 12 from Monkey E.\n  source: Results, Replication of the Results with the Ring Dataset, paragraph 1; Methods,\n    Neurophysiology, last paragraph\n  quote: We recorded 3,051 well-isolated neurons (1,712 from DMFC and 1,339 from FEF) across 22\n    neurophysiology sessions\n  expected:\n  - quantity: Ring units, total\n    value: 3051\n    tolerance: 305\n  - quantity: Ring units, DMFC\n    value: 1712\n    tolerance: 171\n  - quantity: Ring units, FEF\n    value: 1339\n    tolerance: 134\n  - quantity: Ring sessions, Monkey P\n    value: 10\n    tolerance: 0\n  - quantity: Ring sessions, Monkey E\n    value: 12\n    tolerance: 0\n  criterion: >-\n    As triangle-unit-counts, with the same three readings, on Ring trials. The paper's Ring notebooks\n    list 20 sessions (10 per monkey); the session dates found are reported against both counts.\n- id: ext2-stimulus-delay-activity\n  statement: Neurons are typically active in both the stimulus and the delay phase, and a unit's\n    spatial preference is similar across the two phases.\n  source: Results, The Triangle Dataset, paragraph 1; Extended Data Fig. 2a and 2b\n  quote: We found that neurons were typically active in both stimulus and delay phases ( Extended\n    Data Fig. 2 )\n  criterion: >-\n    Triangle units (T5), per monkey. Panel a, the stimulus-phase (0 to 1000 ms after stimulus onset)\n    against the delay-phase mean rate (T4) per unit; panel b, per unit and triangle location, the\n    1-object mean rate at that location divided by the unit's mean over locations, stimulus phase\n    against delay phase, for DMFC and FEF apart, as the legend defines it. The paper gives no test.\n    Readings of \"typically active in both\": (a) the Pearson and (b) the Spearman correlation across\n    units of panel a's rates is positive at p < 0.05, for both monkeys; panel b is judged the same\n    way per monkey and area. Reproduced when both readings hold for panel a and for at least three of\n    the four panel b plots; the correlations are reported.\n- id: ext3ab-decoding\n  statement: Single-trial delay-phase activity carries information about object positions and\n    identities, decoded above a shuffled-label control.\n  source: Results, The Triangle Dataset, paragraph 1; Extended Data Fig. 3a and 3b\n  quote: We also found that neural activity contained information about object positions and\n    identities ( Extended Data Fig. 3a-b )\n  criterion: >-\n    As the Extended Data Fig. 3 legend and figures/supp_fig_decoding/ fix it, on the three Triangle\n    sessions with the most units entering the models (T7; the code's analysis notebook uses Perle\n    2022-05-31, 2022-06-01 and 2022-06-04): a linear decoder (MSE loss to a one-hot target, L1\n    weight 0.003, SGD at learning rate 0.01, 10,000 steps, config_1_triangle.py) from single-trial\n    rates of the stimulus and delay phases, ten 80/20 train/test splits, against the same with\n    shuffled labels. Panel a decodes the location or identity of 1-object trials; panel b, on\n    2-object trials, the absent location or identity. The paper sets no rule for \"above control\";\n    readings (a) the neural accuracy exceeds the shuffled accuracy in all ten splits; (b) the mean\n    neural accuracy exceeds the shuffled mean by more than two standard deviations of the shuffled\n    splits. Reproduced when, under both readings, delay-phase position and identity decoding of\n    panel a are above control in all three sessions; panel b is reported, with the legend's 66%\n    mark.\n- id: ext3c-decoder-orthogonality\n  statement: The coding axes of a two-object decoder come out nearly orthogonal even for synthetic\n    data with no slot structure, so decoder orthogonality does not diagnose slots.\n  source: Methods, Decoding Analyses, paragraphs 1 and 4; Extended Data Fig. 3c\n  quote: However, we found that this orthogonality resulted even on synthetic data that was\n    specifically not Slot-like. In other words, orthogonality of these decoding subspaces is not\n    diagnostic of object slots.\n  criterion: >-\n    The 2-object decoder of Methods, Decoding Analyses (two linear decoders and a per-trial\n    assignment sigma pressed to be binary; figures/supp_fig_decoding/modeling/models.py,\n    LinearModel2Objects) fitted on 2-object trials of the three sessions of ext3ab-decoding, and on\n    the Receptive Field and Orthogonal synthetic datasets built from them as Methods describe;\n    angles between corresponding columns of W0 and W1 for each location, over ten bootstraps, Triangle\n    and Ring. The paper gives no threshold for \"orthogonal\". Reproduced when the angles for the\n    neural data and for the Receptive Field data are both centred near 90 degrees, read as (a) a\n    median between 75 and 105 degrees and (b) a median within 10 degrees of the Orthogonal dataset's\n    median; both readings are reported and the claim holds when they agree.\n- id: fig2b-selectivity-range\n  statement: Delay-phase position and identity AUCs on 1-object trials span a wide range across\n    units.\n  source: Results, The Triangle Dataset, paragraph 1; Figure 2b\n  quote: A Receiver Operating Characteristic analysis of firing rates in the delay phase revealed a\n    wide range of selectivities for position and identity across neurons ( Fig. 2b )\n  criterion: >-\n    Position and identity AUC (T6) of every Triangle unit (T5) per monkey, with significance at\n    p < 0.05 as the legend shades it. The paper gives no number for \"wide\". Reproduced when, for both\n    monkeys and both features, the AUCs run from near 0.5 (lowest decile below 0.6) to high values\n    (highest decile above 0.7), with both significant and non-significant units present; the\n    deciles are reported under both p-value methods of T6. These cut-offs are the agent's reading of\n    \"wide range\" and are recorded as such.\n- id: fig2d-signal-noise-triangle\n  statement: In the Triangle dataset, pairs of neurons with similar 1-object tuning have positive\n    noise correlations on 2-object trials, and dissimilarly tuned pairs negative ones.\n  source: Results, The Triangle Dataset, paragraph 2; Figure 2d\n  quote: Pairs of neurons with similar selectivities on 1-object trials tended to have positive noise\n    correlations on 2-object trials ... Conversely, dissimilarly tuned pairs of neurons tended to have\n    negative noise correlations.\n  criterion: >-\n    Pairs of simultaneously recorded Triangle units, per monkey, delay-phase rates (T4). Main method,\n    Methods, Noise Correlations: signal correlation is the correlation across the 9 1-object\n    conditions of the two units' mean rates, pairs dropped unless each condition has at least 3\n    trials; noise correlation is the mean over the 18 2-object conditions (identity included) with\n    at least 3 shared trials of the across-trial correlation. Variant, the paper's\n    figures/figure_2/noise_correlations/run_compute_triangle.py: per pair and per triple of two\n    1-object conditions and their 2-object composite, the signal correlation from the two 1-object\n    conditions with trials shuffled between units, the noise correlation on the composite, units\n    above 1 Hz, rows kept with more than 5 trials in each condition. As in\n    plot_noise_vs_signal_correlation.ipynb, signal correlation is cut into 6 bins with edges at\n    linspace(-0.8, 0.8, 7), ends open, and the mean noise correlation per bin is shown with its 95%\n    confidence interval. The paper gives no test. Reproduced when, for both monkeys, the bin of\n    highest signal correlation has a mean noise correlation above zero and the lowest bin one below\n    zero, each with a 95% interval excluding zero; partially reproduced when only the rise from the\n    lowest to the highest bin holds (non-overlapping intervals). Both methods are run; when they\n    differ the claim is methods_underspecified.\n- id: fig4a-gain-best-triangle\n  statement: On the Triangle dataset the Gain model has a higher cross-validated model likelihood\n    than the Slot and Switching models, in 88% of sessions and in every session with at least 100\n    simultaneously recorded units.\n  source: Results, Modeling Results, paragraph 1; Figure 4a\n  quote: Across sessions, the Gain model had a higher cross-validated likelihood than the Slot and\n    Switching models ( Fig. 4a ). This held for 88% of sessions, including all sessions with at least\n    100 simultaneously recorded units.\n  statistics:\n  - about: Gain against Slot and against Switching, mean model likelihood, per monkey\n    test: significance of the difference of the mean (Figure 4a brackets)\n    p: 0.05\n    p_relation: \"<\"\n    n: 10 sessions of Monkey P and 14 of Monkey E, 10 train/test splits each\n  expected:\n  - quantity: share of Triangle sessions where Gain has the highest model likelihood\n    value: 0.88\n    tolerance: 0.088\n  - quantity: share of Triangle sessions with at least 100 modeled units where Gain is highest\n    value: 1.0\n    tolerance: 0\n  criterion: >-\n    Models fitted and compared as T7 on all 24 Triangle sessions. A session's winner is the model of\n    highest mean model likelihood over its splits. The test behind the brackets is, in\n    model_comparison.ipynb, an independent two-sample t-test (scipy ttest_ind) between two models'\n    session-by-split likelihoods, per monkey; the legend marks p < 0.05 while the notebook draws\n    brackets at p < 0.01, and both thresholds are reported. Reproduced when Gain's mean likelihood\n    exceeds both others' for both monkeys with t-test p < 0.05, and the two expected shares hold.\n    \"At least 100 units\" is read as at least 100 modeled units (T7); the notebook's > 100 is shown\n    as a variant. Unit stability threshold of T5 (500 against 200 trials) is run both ways. The\n    paper's notebook printed 12 of 14 sessions for E and 10 of 10 for P. A full refit is the test;\n    the bracket pattern of the figure could not be read (no PDF).\n- id: ext6-gain-best-areas\n  statement: The Gain model's advantage holds in DMFC alone, in FEF alone, and in single neurons\n    alone.\n  source: Results, Modeling Results, paragraph 1; Extended Data Fig. 6\n  quote: The results were consistent across both DMFC and FEF ( Extended Data Fig. 6 )\n  depends_on:\n  - fig4a-gain-best-triangle\n  criterion: >-\n    As fig4a-gain-best-triangle, restricted as the Extended Data Fig. 6 legend fixes it to 8 Triangle\n    sessions (the four with the most units from each monkey), refitted with units from DMFC only\n    (probe s0), FEF only (V-probes), and good units only (unit_filters.py qualities). Reproduced\n    when, in each of the three restrictions, Gain has the highest mean model likelihood and differs\n    from each other model by the t-test of fig4a at p < 0.05; partially reproduced when this holds in\n    two of three.\n- id: ext5-general-slot\n  statement: Letting slots be arbitrary linear subspaces (the General Slot model) does not change the\n    model comparison; Gain still wins.\n  source: Results, Slot hypothesis, paragraph 1; Methods, General Slot Model; Extended Data Fig. 5\n  quote: we found that relaxing this assumption and allowing the slots to be linear subspaces in\n    neural activity space does not qualitatively change our results ( Extended Data Fig. 5 )\n  depends_on:\n  - fig4a-gain-best-triangle\n  criterion: >-\n    As fig4a-gain-best-triangle on the 24 Triangle sessions with the General Slot model\n    (configs/neural/triangle_slot.py, 2 slots) in place of the disjoint Slot model. Reproduced when\n    Gain's mean likelihood exceeds General Slot's and Switching's for both monkeys at t-test\n    p < 0.05.\n- id: fig4b-identifiability\n  statement: Applied to synthetic spike trains sampled from each fitted model, the full fitting and\n    comparison pipeline recovers the generating model, Slot, Switching or Gain.\n  source: Results, Modeling Results, paragraph 3; Methods, Validation Using Synthetic Data; Figure\n    4b\n  quote: This analysis confirmed that our model comparison reliably recovered the ground truth for\n    each of the Slot, Switching, and Gain models ( Fig. 4b )\n  depends_on:\n  - fig4a-gain-best-triangle\n  criterion: >-\n    As Methods, Validation Using Synthetic Data, with phys_modeling/synthetic_datasets and\n    configs/synthetic: the ten Triangle sessions with the most units (five per monkey), one shared\n    split, each model at its stopping step sampled as Poisson spikes with kappa 0; kappa and stopping\n    step re-tuned; models refitted; model likelihood as T7 but over 300 neuron-trial pairs. The\n    number of new splits is open: two (Methods) or five (seeds 3 to 7 in\n    figures/figure_4/model_comparison/identifiability.ipynb); both are allowed, the run states which.\n    Reproduced when, for each of the three generating models, that model has the highest mean\n    likelihood and beats each other model by the t-test of fig4a at p < 0.05.\n- id: nslots-two-best\n  statement: Two slots give the best cross-validated likelihood for the Slot model on both datasets\n    and both monkeys.\n  source: Methods, Slot Model, paragraphs 1 and 2\n  quote: Through hyperparameter sweeping, we found that N slots = 2 provided the best cross-validated\n    performance on both the Triangle and Ring dataset for both monkeys.\n  criterion: >-\n    As Methods, Slot Model, paragraph 2: for each monkey and dataset, 4 random sessions, N slots of\n    1, 2, 3 and 4, two random splits each, mean test log-likelihood. Reproduced when 2 is best on\n    average in all four monkey and dataset combinations. The random sessions are drawn with a fixed\n    seed and named.\n- id: ext11-kappa-tuning\n  statement: For most sessions the best temporal smoothness kappa lies inside the sweep, is broadly\n    the same across models, and is lower in sessions with more units.\n  source: Methods, Tuning the Temporal Smoothness and Training Steps, paragraphs 1 and 2; Extended\n    Data Fig. 11\n  quote: We found that for most sessions, cross-validated likelihood was maximized for a value of κ\n    somewhere in the middle of our sweep. Furthermore, this optimal value of κ was broadly consistent\n    across models.\n  depends_on:\n  - fig4a-gain-best-triangle\n  criterion: >-\n    From the kappa sweeps of T7 on the Triangle sessions. Reproduced when (i) in more than half of\n    sessions and models the best kappa is neither 0 nor 200 ms; (ii) per session the best kappas of\n    the three models span at most 60 ms (three sweep steps) in more than half of sessions; (iii) the\n    Spearman correlation across sessions of unit count and best kappa is negative. The paper gives no\n    numbers for (ii) and (iii); the 60 ms span is the agent's reading of \"broadly consistent\" and is\n    reported with the full table, so the claim is judged on (i) and (iii) when (ii) disagrees.\n- id: ext7-gains-distributed\n  statement: The Gain model's per-trial gains are spread across objects and do not pick one object\n    per trial.\n  source: Results, Gain model predictions for behavioral errors and reaction times, paragraph 1;\n    Extended Data Fig. 7c\n  quote: These gains were distributed across the objects and did not sparsely select one object per\n    trial ( Extended Data Fig. 7 )\n  depends_on:\n  - fig4a-gain-best-triangle\n  criterion: >-\n    Gains (T8) of the fitted Gain models on 3-object Triangle trials, per monkey and object location,\n    as Extended Data Fig. 7c plots them\n    (figures/supp_fig_attn_distribution/attention_distribution.ipynb). The paper fixes no measure of\n    sparsity. Readings, both run; (a) the share of trials with one gain above 0.9 and the other two\n    below 0.1; (b) the same with 0.8 and 0.2. Reproduced when under both readings fewer than half\n    of trials are one-object selections, for both monkeys. The Slot and Switching attention values of\n    panels a and b are shown for comparison.\n- id: fig4c-gain-performance-triangle\n  statement: On 3-object Triangle trials, performance is higher when the target object's\n    neurally inferred delay gain is higher (R = 0.35 for Monkey P, 0.26 for Monkey E).\n  source: Results, Gain model predictions for behavioral errors and reaction times, paragraph 1;\n    Figure 4c legend\n  quote: Strikingly, performance was higher for objects with higher delay-phase gains ( Fig. 4c ) ...\n    The regression is significantly positive for both monkeys ( R = 0. 35±0. 04, p < 10 −9 for Monkey\n    P; R = 0. 26±0. 04, p < 10 −7 for Monkey E)\n  statistics:\n  - about: Monkey P\n    test: linear regression (Pearson correlation)\n    statistic: R = 0.35 ± 0.04\n    p: 1.0e-9\n    p_relation: \"<\"\n  - about: Monkey E\n    test: linear regression (Pearson correlation)\n    statistic: R = 0.26 ± 0.04\n    p: 1.0e-7\n    p_relation: \"<\"\n  expected:\n  - quantity: R, target gain against performance, Monkey P\n    value: 0.35\n    tolerance: 0.04\n  - quantity: R, target gain against performance, Monkey E\n    value: 0.26\n    tolerance: 0.04\n  depends_on:\n  - fig4a-gain-best-triangle\n  criterion: >-\n    As figures/figure_4/attention_behavior/performance_reaction_time.ipynb: completed 3-object\n    Triangle trials with a gain (T8); for each session, split and target location, the mean target\n    gain and the mean performance (T2); Pearson R and its p across these points per monkey (the\n    notebook had 300 points for P and 420 for E); the ± is the standard deviation of R over 1000\n    bootstrap resamples of the points. Reproduced when R lies within the paper's ± of the value and\n    p is below the paper's bound, for both monkeys; partially reproduced when R is positive with\n    p < 0.05 in both but outside tolerance. Both correctness radii (T2) are run.\n- id: fig4d-gain-rt-triangle\n  statement: On correct 3-object Triangle trials, the residual target gain is negatively correlated\n    with residual reaction time (R = -0.14 for Monkey P, -0.04 for Monkey E).\n  source: Results, Gain model predictions for behavioral errors and reaction times, paragraph 1;\n    Figure 4d legend\n  quote: residual gains were negatively correlated with residual reaction times ( Fig. 4d ) ... The\n    regression slope is significantly negative for both monkeys ( R =− 0. 14±0. 016, p < 10 −10 for\n    Monkey P; R =− 0. 04±0. 015, p = 0. 007 for Monkey E)\n  statistics:\n  - about: Monkey P\n    test: linear regression (Pearson correlation)\n    statistic: R = -0.14 ± 0.016\n    p: 1.0e-10\n    p_relation: \"<\"\n  - about: Monkey E\n    test: linear regression (Pearson correlation)\n    statistic: R = -0.04 ± 0.015\n    p: 0.007\n  expected:\n  - quantity: R, residual target gain against residual reaction time, Monkey P\n    value: -0.14\n    tolerance: 0.016\n  - quantity: R, residual target gain against residual reaction time, Monkey E\n    value: -0.04\n    tolerance: 0.015\n  depends_on:\n  - fig4a-gain-best-triangle\n  criterion: >-\n    Correct completed 3-object Triangle trials. Within each group of trials with the same stimulus\n    (locations and identities), cue (target) and session, the target gain is de-meaned and scaled to\n    variance 1 and the reaction time (T3) de-meaned, as the legend says; Pearson R across trials per\n    monkey, ± as in fig4c-gain-performance-triangle. Order of steps is open: (a) gains averaged over\n    the ten splits, then normalized (legend); (b) normalized within each split, then averaged per\n    trial (performance_reaction_time.ipynb). Reproduced when, under one reading, R lies within the\n    paper's ± and p is below the paper's bound for both monkeys; both readings are reported.\n    Partially reproduced when R is negative with p < 0.05 in both monkeys but outside tolerance.\n- id: ext8-slot-switching-behavior\n  statement: The relations of attention to accuracy and reaction time are weaker for the Slot and\n    Switching models than for the Gain model.\n  source: Results, Gain model predictions for behavioral errors and reaction times, paragraph 1;\n    Extended Data Fig. 8 legend\n  quote: These behavioral relationships were weaker for the Slot and Switching models ( Extended Data\n    Fig. 8 )\n  statistics:\n  - about: Slot attention against reaction time, Monkey P (panel b)\n    test: linear regression (Pearson correlation)\n    statistic: R = -0.03 ± 0.017\n    p: 0.034\n  - about: Slot attention against reaction time, Monkey E (panel b)\n    test: linear regression (Pearson correlation)\n    statistic: R = -0.01 ± 0.014\n    p: 0.4\n  - about: Switching attention against performance, Monkey P (panel c)\n    test: linear regression (Pearson correlation)\n    statistic: R = 0.65 ± 0.02\n    p: 1.0e-10\n    p_relation: \"<\"\n  - about: Switching attention against performance, Monkey E (panel c)\n    test: linear regression (Pearson correlation)\n    statistic: R = 0.34 ± 0.04\n    p: 1.0e-10\n    p_relation: \"<\"\n  - about: Switching attention against reaction time, Monkey P (panel d)\n    test: linear regression (Pearson correlation)\n    statistic: R = -0.05 ± 0.016\n    p: 0.002\n  - about: Switching attention against reaction time, Monkey E (panel d)\n    test: linear regression (Pearson correlation)\n    statistic: R = -0.03 ± 0.014\n    p: 0.063\n  expected:\n  - quantity: R, Slot attention against reaction time, Monkey P\n    value: -0.03\n    tolerance: 0.017\n  - quantity: R, Slot attention against reaction time, Monkey E\n    value: -0.01\n    tolerance: 0.014\n  - quantity: R, Switching attention against performance, Monkey P\n    value: 0.65\n    tolerance: 0.02\n  - quantity: R, Switching attention against performance, Monkey E\n    value: 0.34\n    tolerance: 0.04\n  - quantity: R, Switching attention against reaction time, Monkey P\n    value: -0.05\n    tolerance: 0.016\n  - quantity: R, Switching attention against reaction time, Monkey E\n    value: -0.03\n    tolerance: 0.014\n  depends_on:\n  - fig4c-gain-performance-triangle\n  - fig4d-gain-rt-triangle\n  criterion: >-\n    The analyses of fig4c and fig4d with the Slot model's attention (1 if the object is assigned to a\n    slot, summed over slots as the notebook does with MODEL_NAME triangle_slot_partition) and the\n    Switching model's attention (fraction of delay time steps the object is active) in place of the\n    gain. Panel a's statistics are garbled in the text (only \"−4 for Monkey P; −10 for Monkey E\"\n    survives), so panel a is reported without expected values. The paper's own panel c values exceed\n    the Gain model's R for performance, so \"weaker\" can only be read on reaction time and on panel b\n    and d significance; the claim is judged on the reaction-time relation. Reproduced when the\n    expected values hold within the paper's ± and the Gain model's reaction-time R (fig4d) is more\n    negative than the Slot's and the Switching's for both monkeys; the performance comparison is\n    reported. The legend calls panel b \"not significant for either monkey\" while printing p = 0.034\n    for Monkey P; recorded as printed.\n- id: fig5ab-ring-behavior\n  statement: Both monkeys perform well on the Ring dataset, with reaction-time variability like that\n    on the Triangle dataset.\n  source: Results, Replication of the Results with the Ring Dataset, paragraph 1; Figure 5a and 5b;\n    Extended Data Fig. 9a and 9b\n  quote: Both monkeys performed well on the Ring dataset and exhibited reaction-time variability\n    similar to the Triangle dataset\n  criterion: >-\n    Completed Ring trials (T1), per monkey and pooled, fraction correct (T2) for 1 and 2 objects and\n    the reaction-time distribution (T3), as figures/figure_5/performance_reaction_time/. The paper\n    gives no number. Reproduced when the 2-object fraction correct is above chance (1/2) for both\n    monkeys and each monkey's Ring reaction-time interquartile range is within a factor of 1.5 of its\n    Triangle one; the factor is the agent's reading of \"similar\" and the ranges are reported. For\n    reference, the paper's notebook printed P 0.958 and 0.903, E 0.945 and 0.756 for 1 and 2 objects\n    with the code's radius.\n- id: fig5cd-ring-tuning\n  statement: Ring neurons in DMFC and FEF show a variety of spatial receptive fields and diverse\n    delay-phase position and identity selectivities, as in the Triangle dataset.\n  source: Results, Replication of the Results with the Ring Dataset, paragraph 1; Figure 5c and 5d;\n    Extended Data Fig. 9c\n  quote: These neurons showed a variety of spatial receptive fields in both DMFC and FEF ( Fig. 5c ;\n    Extended Data Fig. 9c ) and diverse selectivities to position and identity in delay-phase firing\n    rates ( Fig. 5d ), similar to the Triangle dataset\n  depends_on:\n  - fig2b-selectivity-range\n  criterion: >-\n    Position and identity AUC (T6) of Ring units, judged as fig2b-selectivity-range. Tuning curves as\n    Methods, Ring Dataset Tuning Curves (256 points on the ring, 100 bootstraps of 100 1-object\n    trials, Gaussian kernel of 2.4 degrees); \"variety\" is judged by the preferred angles of units\n    with significant position AUC, reproduced when in each area they fall in all three 120-degree\n    sectors.\n- id: fig5e-signal-noise-ring\n  statement: In the Ring dataset, noise correlation rises with signal correlation, as in the Triangle\n    dataset.\n  source: Results, Replication of the Results with the Ring Dataset, paragraph 1; Figure 5e;\n    Extended Data Fig. 9d\n  quote: We also found a positive relationship between signal correlation and noise correlation (\n    Fig. 5e ; Extended Data Fig. 9d ), corroborating our findings in the Triangle dataset\n  criterion: >-\n    As Methods, Ring Dataset Signal and Noise Correlations (the Methods call it Fig. 5c), on pairs\n    of Ring units: trials embedded in 6 dimensions (x and y of each fruit, 0 when absent); signal\n    correlation on 1-object trials between one unit's rate and the other's on the nearest-neighbour\n    trial. The noise correlation is open between (a) the Methods' wording, per 2-object trial the\n    correlation of the two units over its 10 nearest-neighbour trials, averaged over trials, and (b)\n    the paper's figures/figure_5/noise_correlations/run_compute_ring.py, each trial's rate minus\n    the mean of its 10 neighbours, one Pearson correlation of these residuals across trials. Pairs\n    kept with at least 50 1-object and 200 2-object trials (noise_correlations.ipynb); 8 bins of\n    signal correlation with edges at linspace(-s, s, 9), s 0.8 for P and pooled, 0.3 for E. The paper\n    gives no test. Reproduced when, per monkey, the mean noise correlation of the highest bin\n    exceeds that of the lowest with non-overlapping 95% intervals; when the readings differ the claim\n    is methods_underspecified.\n- id: fig5f-gain-best-ring\n  statement: On the Ring dataset the Gain model again has higher model likelihood than the Slot and\n    Switching models, for both monkeys.\n  source: Results, Replication of the Results with the Ring Dataset, paragraph 2; Figure 5f\n  quote: As in the Triangle dataset, the Gain model had higher model likelihood than the Slot and\n    Switching models for both monkeys ( Fig. 5f )\n  statistics:\n  - about: Gain against Slot and against Switching, per monkey\n    test: significance of the difference of the mean (Figure 4a format)\n    p: 0.05\n    p_relation: \"<\"\n  criterion: >-\n    As fig4a-gain-best-triangle on the Ring sessions, with configs/neural/ring_*.py (2 slots,\n    positional noise 0.05). Which sessions is open; (a) all 22 recorded sessions; (b) the 20 the\n    paper's figures/figure_5/model_comparison/model_comparison.ipynb lists. Trials per T1, with and\n    without the left/right trials. Reproduced when, under one reading, Gain's mean likelihood exceeds\n    both others for both monkeys with t-test p < 0.05. The notebook printed 10 of 10 sessions for P\n    and 9 of 10 for E with Gain highest; reported for comparison.\n- id: fig5g-gain-performance-ring\n  statement: On 2-object Ring trials, performance rises with the target object's gain (R = 0.042 for\n    Monkey P, 0.01 for Monkey E).\n  source: Results, Replication of the Results with the Ring Dataset, paragraph 2; Figure 5g legend\n  quote: Regression is significantly positive ( R = 0. 042±0. 003, p < 10 −10 ) ... Regression is\n    significantly positive ( R = 0. 01±0. 003, p = 0. 006)\n  statistics:\n  - about: Monkey P\n    test: linear regression (Pearson correlation)\n    statistic: R = 0.042 ± 0.003\n    p: 1.0e-10\n    p_relation: \"<\"\n  - about: Monkey E\n    test: linear regression (Pearson correlation)\n    statistic: R = 0.01 ± 0.003\n    p: 0.006\n  expected:\n  - quantity: R, target gain against performance, Ring, Monkey P\n    value: 0.042\n    tolerance: 0.003\n  - quantity: R, target gain against performance, Ring, Monkey E\n    value: 0.01\n    tolerance: 0.003\n  depends_on:\n  - fig5f-gain-best-ring\n  criterion: >-\n    As figures/figure_5/attention_behavior/performance.ipynb: completed 2-object Ring trials, one\n    point per trial and split, Pearson R of the target gain (T8) with performance (T2) per monkey, ±\n    the standard deviation of R over 1000 bootstraps; the legend says \"over all trials\". Reproduced\n    when R lies within the paper's ± and p is below the paper's bound for both monkeys; partially\n    reproduced when R is positive with p < 0.05 in both but outside tolerance.\n- id: fig5h-gain-rt-ring\n  statement: On correct 2-object Ring trials, residual target gain is negatively correlated with\n    residual reaction time (R = -0.13 for Monkey P, -0.03 for Monkey E).\n  source: Results, Replication of the Results with the Ring Dataset, paragraph 2; Figure 5h legend;\n    Methods, Ring Dataset Normalized Target Gain\n  quote: The regression is significantly negative for both monkeys ( R =− 0. 13±0. 011, p < 10 −10\n    for Monkey P, R =− 0. 03±0. 012, p = 0. 018 for Monkey E)\n  statistics:\n  - about: Monkey P\n    test: linear regression (Pearson correlation)\n    statistic: R = -0.13 ± 0.011\n    p: 1.0e-10\n    p_relation: \"<\"\n  - about: Monkey E\n    test: linear regression (Pearson correlation)\n    statistic: R = -0.03 ± 0.012\n    p: 0.018\n  expected:\n  - quantity: R, residual target gain against residual reaction time, Ring, Monkey P\n    value: -0.13\n    tolerance: 0.011\n  - quantity: R, residual target gain against residual reaction time, Ring, Monkey E\n    value: -0.03\n    tolerance: 0.012\n  depends_on:\n  - fig5f-gain-best-ring\n  criterion: >-\n    As Methods, Ring Dataset Normalized Target Gain (which calls the panels 5e and 5f), and\n    figures/figure_5/attention_behavior/reaction_time.ipynb: correct completed 2-object Ring trials;\n    per session and split, each trial's target gain and reaction time minus the mean over other\n    trials with the same target identity and target angle within 90 degrees, the gain residuals\n    scaled to variance 1; residuals averaged over splits per trial; Pearson R per monkey, ± as above.\n    Reproduced when R lies within the paper's ± and p is below the paper's bound for both monkeys;\n    partially reproduced when R is negative with p < 0.05 in both but outside tolerance.\n"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  timeout 300 python tools/claims_check.py claims/000620/10.64898-2026.01.27.702062.yaml paper/10.64898-2026.01.27.702062.txt < /dev/null
```

Result: not kept, because it reads the paper's text.

**Agent**

The checker requires quote fragments in text order, and the Fig. 4 legend comes before the Results paragraph in the file. Reordering those two quotes.

**Agent calls Bash**

```bash
cd  python - <<'EOF'
p='claims/000620/10.64898-2026.01.27.702062.yaml'
s=open(p).read()
old_c="""  quote: Strikingly, performance was higher for objects with higher delay-phase gains ( Fig. 4c ) ...
    The regression is significantly positive for both monkeys ( R = 0. 35±0. 04, p < 10 −9 for Monkey
    P; R = 0. 26±0. 04, p < 10 −7 for Monkey E)
"""
new_c="""  quote: The regression is significantly positive for both monkeys ( R = 0. 35±0. 04, p < 10 −9 for
    Monkey P; R = 0. 26±0. 04, p < 10 −7 for Monkey E) ... Strikingly, performance was higher for
    objects with higher delay-phase gains ( Fig. 4c )
"""
old_d="""  quote: residual gains were negatively correlated with residual reaction times ( Fig. 4d ) ... The
    regression slope is significantly negative for both monkeys ( R =− 0. 14±0. 016, p < 10 −10 for
    Monkey P; R =− 0. 04±0. 015, p = 0. 007 for Monkey E)
"""
new_d="""  quote: The regression slope is significantly negative for both monkeys ( R =− 0. 14±0. 016, p < 10
    −10 for Monkey P; R =− 0. 04±0. 015, p = 0. 007 for Monkey E) ... residual gains were negatively
    correlated with residual reaction times ( Fig. 4d )
"""
assert old_c in s and old_d in s
s=s.replace(old_c,new_c).replace(old_d,new_d)
s=s.replace("source: Results, Gain model predictions for behavioral errors and reaction times, paragraph 1;\n    Figure 4c legend","source: Figure 4c legend; Results, Gain model predictions for behavioral errors and reaction\n    times, paragraph 1")
s=s.replace("source: Results, Gain model predictions for behavioral errors and reaction times, paragraph 1;\n    Figure 4d legend","source: Figure 4d legend; Results, Gain model predictions for behavioral errors and reaction\n    times, paragraph 1")
open(p,'w').write(s)
EOF
timeout 300 python tools/claims_check.py claims/000620/10.64898-2026.01.27.702062.yaml paper/10.64898-2026.01.27.702062.txt < /dev/null
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  f=claims/000620/10.64898-2026.01.27.702062.yaml; grep -n "—\|rather" $f; python - <<'EOF'
import yaml
d=yaml.safe_load(open('claims/000620/10.64898-2026.01.27.702062.yaml'))
c=d['claims']
print(len(c), sum('quote' in x for x in c), sum('statistics' in x for x in c), sum(len(x.get('statistics',[])) for x in c), sum('criterion' in x for x in c), sum('expected' in x for x in c))
EOF
grep -nE "^\s+(statement|source|quote|criterion|quantity|about|test|statistic|n|inferred): [^>].*: " $f | head; git status --short
```

```
26 26 7 16 26 8
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
?? claims/000620/
?? scripts
```

**Agent calls Bash**

```bash
cd  grep -nE ": " claims/000620/10.64898-2026.01.27.702062.yaml | grep -vE "^[0-9]+:#|^[0-9]+:\s*-? ?[a-z_]+: " | head
```

```
99:    form the figure is open: (a) Triangle trials on the triangle only, as the paper's
156:    default 10%. Which units are counted is open: (a) good and mua units with delay-phase rate above
198:    Readings of "typically active in both": (a) the Pearson and (b) the Spearman correlation across
211:    2022-05-31, 2022-06-01 and 2022-06-04): a linear decoder (MSE loss to a one-hot target, L1
260:    Methods, Noise Correlations: signal correlation is the correlation across the 9 1-object
264:    figures/figure_2/noise_correlations/run_compute_triangle.py: per pair and per triple of two
345:    configs/synthetic: the ten Triangle sessions with the most units (five per monkey), one shared
348:    number of new splits is open: two (Methods) or five (seeds 3 to 7 in
359:    As Methods, Slot Model, paragraph 2: for each monkey and dataset, 4 random sessions, N slots of
426:    As figures/figure_4/attention_behavior/performance_reaction_time.ipynb: completed 3-object
```

**Agent calls Bash**

```bash
cd  python - <<'EOF'
import yaml
d=yaml.safe_load(open('claims/000620/10.64898-2026.01.27.702062.yaml'))
for c in d['claims']:
    for k,v in c.items():
        if k!='criterion' and isinstance(v,str) and ': ' in v: print(c['id'],k)
        if isinstance(v,list):
            for e in v:
                if isinstance(e,dict):
                    for kk,vv in e.items():
                        if isinstance(vv,str) and ': ' in vv: print(c['id'],kk)
EOF
```

```
(Bash completed with no output)
```

**Agent**

I wrote `claims/000620/10.64898-2026.01.27.702062.yaml`. The quote checker reports 26 claims, 26 quotes, 16 statistical values and 0 problems. Nothing is committed.

**Text read.** I read the bioRxiv preprint, version 1, from its JATS XML: the main text, the Methods, and the legends of Extended Data Figs. 1 to 11. The paper has no separate supplement. There was no PDF for this paper, so I could not look at any figure panel, and the XML version leaves out the model equations (the models are still described in words). The `paper/` folder also holds a second paper, "A Relational Code for Objects…" (doi:10.64898/2026.10.17.759839). It is not the paper this run was asked to cover, so I did not use it.

**Code read.** I read `jazlab/multi_object_memory_2025` at commit 6e4b333: the behaviour and physiology processing, the model code and its settings, and the figure notebooks, several of which print their results.

**Claims.** There are 26, and every one has a quote and a criterion. Seven have statistics (16 entries); eight have expected values with tolerances. They cover:
- behaviour (Fig. 1b and 1c, and Extended Data Fig. 1);
- neuron and session counts for both datasets;
- activity in the stimulus and delay phases, and decoding (Extended Data Figs. 2 and 3);
- selectivity (AUC) and the signal versus noise correlation relationship (Figs. 2b, 2d and 5e);
- the model comparison (Figs. 4a and 5f), the brain-area controls, the general Slot model, the synthetic-data recovery test (Fig. 4b), and the choices of two slots and of temporal smoothing;
- whether the gains are spread across objects (Extended Data Fig. 7);
- gain against accuracy and reaction time (Figs. 4c, 4d, 5g and 5h), and the same for the Slot and Switching models (Extended Data Fig. 8).

For the correlation values I used the paper's own ± as the tolerance; the code shows it is the standard deviation of R over 1,000 bootstrap resamples.

**Details left open, with the readings named for each:**
- **What counts as correct:** within 2.4° of the target (Methods) or 4.8° (code). Both are run.
- **Trials in Fig. 1b:** Triangle trials only (code) or Triangle and Ring pooled (legend).
- **Which units are counted:** good and multi-units above 1 Hz (this is how the code reproduces 4,688); the same plus at least 500 stable trials (Methods); or single units only ("well-isolated").
- **Minimum stable trials per unit for modelling:** 500 (Methods) or 200 (code).
- **AUC p-value:** 1,000 label shuffles (Methods) or 5,000 bootstrap resamples (code). The legend calls the AUC values "cross-validated", but neither the Methods nor the code says how; I recorded this as a deviation.
- **Triangle noise correlations:** the Methods' 9 and 18 conditions, or the code's method built on triples of conditions.
- **Ring noise correlations:** a correlation over each trial's 10 nearest trials (Methods wording), or residuals from those neighbours (code).
- **Significance level in Fig. 4a:** p < 0.05 (legend) or p < 0.01 (where the code draws its brackets). The test itself is an independent t-test (code).
- **"At least 100 units":** ≥ 100 or > 100.
- **Order of steps in Fig. 4d:** average the gains over splits then normalise (legend), or normalise then average (code).
- **Ring sessions:** the 22 recorded or the 20 the code lists. Ring left/right trials are included (Methods) or excluded (code).
- **Synthetic-data test:** 2 new train/test splits (Methods) or 5 (code).
- **Descriptive words with no number or test** ("wide", "common", "similar", "typically", "broadly consistent", "distributed"): each criterion names two readings, or states the cut-off as my own reading of the word.

**Problems in the paper that bear on claims:**
- The statistics for Extended Data Fig. 8a are garbled; only "−4 … −10" survives, and the R values are missing.
- The Extended Data Fig. 8b legend says "not significant for either monkey" yet prints p = 0.034 for Monkey P.
- The Switching model's R for accuracy (0.65 and 0.34) is higher than the Gain model's, which contradicts "weaker" for accuracy. So that claim is judged on reaction time.
- The paper says Gain wins in 88% of sessions; the code's printed output gives 22 of 24 (92%). That is within the 10% tolerance.
- Some figure references in the paper point to the wrong panels (the Methods cite Fig. 5c and 5e–f for what are 5e and 5g–h; the Results cite Extended Data Fig. 8 for what is Fig. 9).
- Without the figures I could not check which significance brackets Fig. 4a actually shows.

## End of run

43 turns, 67 minutes, result: success.
