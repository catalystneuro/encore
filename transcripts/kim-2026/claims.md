# 001868 · claims · run 39543425324

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cat docs/protocol.md; ls claims/001453/ paper/ claims/001868 2>&1; ls tools
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cat claims/001453/*.yaml | head -150; wc -l paper/*.txt; head -30 paper/*.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.64898-2026.06.05.730421.txt",
 "offset": 30
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -n 150,320p claims/001453/*.yaml; python tools/claims_check.py --help 2>&1 | head -20
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
[... 161 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "paper/10.64898-2026.06.05.730421.txt",
 "offset": 30,
 "limit": 60
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.64898-2026.06.05.730421.txt",
 "offset": 90,
 "limit": 70
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.64898-2026.06.05.730421.txt",
 "offset": 160,
 "limit": 105
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
grep -rli "supplement.*not\|not.*supplement" claims/ | head; grep -rh -i -m3 "supplement" claims/*/*.yaml | head -30; ls transcripts | head -50
```

```
claims/000003/10.1016-j.neuron.2016.12.011.yaml
claims/ebrains-q0fg-1x8/10.1016-j.neuron.2023.04.008.yaml
claims/000061/10.1038-nn.4637.yaml
claims/002020/10.1101-2025.01.14.630383.yaml
claims/crcns-ret-1/10.1242-dev.027912.yaml
claims/000971/10.1016-j.cub.2022.01.055.yaml
claims/000059/10.1016-j.neuron.2020.05.023.yaml
claims/000625/10.1016-j.neuron.2020.09.013.yaml
claims/001084/10.1016-j.neuron.2023.12.011.yaml
claims/000009/10.1038-nature22324.yaml
# supplementary figures (S1 to S7) were not available; claims citing them rest on the main text.
# paper/), with its Online Methods and its one supplement PDF (Supplementary Figures 1 to 14 and
# Supplementary Tables 1 and 2). PDF pages were opened only to read Supplementary Table 2, the
# boundary drawn in Supplementary Figure 6, the number of phase bins in Supplementary Figure 2d,
# Figs 1 to 10 legends and the Reporting Summary. The Supplementary Information (Supplementary
# quoted from the main text, which cites Supplementary Table 1.
  source: Results, Two types of PT neuron in layer 5, paragraph 5; Supplementary Table 1 (not in the
# Extended Data Tables 1 and 2 (descriptions of the t-types), the Supplementary Files 1 to 3
# was supplied, so no figure could be read. Not in the text: the Supplementary Information
# Supplementary Tables 1 and 2 (animals, coordinates, photostimulus powers, viruses). The claims
[... 70 more lines not kept]
```

**Agent calls Bash**

```bash
grep -rl "001868" --include=*.json --include=*.yaml --include=*.md --include=*.csv . 2>/dev/null | grep -v transcripts | head;
```

```
./targets/dandisets.json
./papers/manifest.yaml
```

**Agent calls Bash**

```bash
python -c "
import json;d=json.load(open('targets/dandisets.json'))
items=d if isinstance(d,list) else d.get('dandisets',d)
for x in (items if isinstance(items,list) else items.values()):
  if '001868' in json.dumps(x): print(json.dumps(x,indent=1)[:4000])
"; grep -n -A12 "001868" papers/manifest.yaml
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
[... 153 more lines not kept]
```

**Agent calls Bash**

```bash
python -c "
import json;d=json.load(open('targets/dandisets.json'))
for x in d:
  if x['dandiset']=='001868': print(json.dumps(x,indent=1))
"
```

```
Exit code 1
Traceback (most recent call last):
  File "<string>", line 4, in <module>
    if x['dandiset']=='001868': print(json.dumps(x,indent=1))
       ~^^^^^^^^^^^^
TypeError: string indices must be integers, not 'str'
```

**Agent calls Bash**

```bash
python -c "
import json;d=json.load(open('targets/dandisets.json'))
print(type(d), list(d)[:5] if isinstance(d,dict) else '')
s=json.dumps(d); i=s.find('\"001868\"'); print(s[i-50:i+1500])
"
```

```
<class 'dict'> ['schema_version', 'generated', 'source', 'counts', 'targets']
escription"}], "catalystneuro": []}, {"dandiset": "001868", "name": "Chronic electrophysiology and two-photon calcium imaging of mouse primary somatosensory cortex during intracortical microstimulation learning", "published_version": "0.260715.2016", "asset_count": 85, "size_gb": 7.5, "data_standards": ["Neurodata Without Borders (NWB)"], "species": ["Mus musculus - House mouse"], "approaches": ["behavioral approach", "electrophysiological approach", "microscopy approach; cell population imaging"], "papers": [{"doi": "10.64898/2026.06.05.730421v1", "title": "Learning induces activation-mechanism\u2013dependent neural plasticity in an intracortical microstimulation task", "relation": "IsDescribedBy", "resource_type": "Preprint", "preprint": true}], "catalystneuro": []}, {"dandiset": "001871", "name": "Data for fly navigational responses exploiting plume-specific odor motion and gradient cues", "published_version": "0.260630.1657", "asset_count": 136, "size_gb": 26.91, "data_standards": ["Neurodata Without Borders (NWB)"], "species": ["Drosophila melanogaster - Fruit fly"], "approaches": ["behavioral approach"], "papers": [{"doi": "10.1007/s00348-018-2591-3", "title": "Quantification of airborne odor plumes using planar laser-induced fluorescence", "relation": "References", "resource_type": "JournalArticle", "preprint": false}], "catalystneuro": []}, {"dandiset": "001878", "name": "Standardized behavioral segmentation datasets", "published_version": null, "asset_count": 6, "size_gb": 0.23, "data_standards": ["Neurodata Without
```

**Agent calls Bash**

```bash
cd $TMPDIR && git clone -q https://github.com/XieLuanLab/icms-activation-plasticity && cd icms-activation-plasticity && git log -1 --format='%H %cd' && find . -type f -not -path './.git/*' | head -100 && cat README* | head -80
```

```
d1922d16913b50bf6338ff4e0c2953cb8ef43d15 Wed Jul 15 15:33:04 2026 -0500
./requirements.txt
./python/utils/plotting.py
./python/utils/longitudinal.py
./python/utils/filters.py
./python/utils/config.py
./python/utils/__init__.py
./python/fig_s9/generate_figure.py
./python/fig_s8/generate_figure.py
./python/fig_s7/generate_figure.py
./python/fig_s6/generate_figure.py
./python/fig_s5/generate_figure.py
./python/fig_s4/generate_figure.py
./python/fig_s3/generate_figure.py
./python/fig_s1/generate_figure.py
./python/fig6/stats_table.py
./python/fig6/pop_coupling.py
./python/fig6/hit_miss_psth.py
./python/fig6/hit_miss_histograms.py
./python/fig6/example_raster_and_fr.py
[... 155 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/icms-activation-plasticity && find . -type f -not -path './.git/*' | tail -n +101; wc -l python/utils/*.py python/fig4/*.py python/fig5/*.py python/fig6/*.py
```

```
./processing/batch_process/postprocessing/responses_v2/stim_condition_response_v2.py
./processing/batch_process/postprocessing/responses_v2/session_responses_v2.py
./processing/batch_process/postprocessing/responses_v2/response_plotting_util.py
./processing/batch_process/postprocessing/responses_v2/response_plotting.py
./processing/batch_process/postprocessing/responses_v2/pulse_locked_response_metrics.py
./processing/batch_process/postprocessing/responses_v2/__init__.py
./processing/batch_process/postprocessing/longitudinal_data_utils.py
./processing/batch_process/postprocessing/__init__.py
./processing/batch_process/__init__.py
./processing/__init__.py
./matlab/report_stat.m
./matlab/load_data.m
./matlab/fig_s2/figs2f_neurons_at_threshold.m
./matlab/fig_s2/figs2e_control_vs_behavior_count.m
./matlab/fig_s2/figs2d_control_vs_behavior_density.m
./matlab/fig_s2/figs2abc_density_lines_rings.m
./matlab/fig3/fig3jlmn_subset_analysis.m
./matlab/fig3/fig3i_histogram.m
./matlab/fig3/fig3def_plot.m
./matlab/fig3/fig3def_longitudinal_trends.m
[... 41 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/icms-activation-plasticity/python && cat utils/config.py utils/filters.py utils/longitudinal.py fig4/modulation_over_time.py fig4/modulated_unit_count.py fig4/cell_type_histogram.py
```

```
"""Global configuration for figure generation scripts.

All paths are relative to the repository root. No hardcoded absolute paths.
"""
from pathlib import Path

# Repository root: two levels up from python/utils/
REPO_ROOT = Path(__file__).resolve().parents[2]
DATA_DIR = REPO_ROOT / 'data'
OUTPUT_DIR = REPO_ROOT / 'output'

# Ensure output directory exists
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Animal IDs
EXPERIMENTAL_ANIMALS = ['ICMS92', 'ICMS93', 'ICMS98', 'ICMS100', 'ICMS101']
ALL_ANIMALS = ['ICMS83'] + EXPERIMENTAL_ANIMALS  # ICMS83 + experimental

# Display names for manuscript
MOUSE_NAMES = {
[... 509 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/icms-activation-plasticity/python && cat utils/plotting.py fig5/generate_figure5.py
```

```
"""Shared plotting utilities and global style."""
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

PALETTE = sns.color_palette("deep")


def apply_global_style():
    """Apply consistent matplotlib styling for all figures."""
    mpl.rcParams.update({
        'font.family': 'sans-serif',
        'font.sans-serif': ['Arial'],
        'font.size': 7,
        'axes.titlesize': 7,
        'figure.titlesize': 7,
        'legend.fontsize': 7,
        'axes.labelsize': 7,
        'xtick.labelsize': 7,
[... 310 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/icms-activation-plasticity/python && cat fig6/hit_miss_histograms.py fig6/pop_coupling.py; sed -n 1,196p fig6/hit_miss_psth.py
```

```
"""Hit vs miss delta_spks histograms and KL divergence (700ms and 120ms)."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from scipy.stats import mannwhitneyu, entropy
from scipy.stats.mstats import winsorize
from statsmodels.stats.multitest import multipletests

from utils.config import DF_MERGED_PATH, OUTPUT_DIR
from utils.plotting import apply_global_style, PALETTE, sig_text

FIG_DIR = OUTPUT_DIR / 'fig6'
FIG_DIR.mkdir(parents=True, exist_ok=True)
[... 479 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/icms-activation-plasticity && grep -rn "rel_week\s*=\|'rel_week'\]\s*=\|rel_day\s*=\|\"rel_week\"\]\s*=" --include=*.py . | head -20; grep -rln "hit_miss_psth\|delta_spks\|t_to_max_10ms_smoothed\|pli\b\|PLI\|pulse_locked_index" --include=*.py .
```

```
./python/utils/longitudinal.py:38:            vals = cur_df[cur_df['rel_week'] == week][var].dropna()
./python/fig_s7/generate_figure.py:51:            df.loc[(df['animal_id'] == aid) & (df['session_date'] == s), 'rel_week'] = (
./python/fig_s5/generate_figure.py:79:            vals = cur_df[cur_df['rel_week'] == week][metric].dropna()
./python/fig_s5/generate_figure.py:583:        df.loc[mask, 'rel_week'] = np.where(days == 0, 0,
./python/fig_s5/generate_figure.py:586:    df['rel_week'] = df['rel_week'].astype(int)
./python/fig_s4/generate_figure.py:195:                vals = cd[cd['rel_week'] == wk][var].dropna()
./python/fig_s3/generate_figure.py:102:            vals = cur_df[cur_df['rel_week'] == week][var].dropna()
./python/fig_s3/generate_figure.py:243:        vals = week_med[week_med['rel_week'] == wk]['week_median_z'].dropna()
./python/fig_s1/generate_figure.py:107:            rel_day = rel_days[idx]
./python/fig_s1/generate_figure.py:108:            rel_week = math.ceil(rel_day / 7) if rel_day > 0 else 0
./python/fig6/stats_table.py:59:        pl_hit = pl_df[(pl_df['rel_week'] == week) & (pl_df['trial_outcome'] == 'hit')][delta_col]
./python/fig6/stats_table.py:60:        pl_miss = pl_df[(pl_df['rel_week'] == week) & (pl_df['trial_outcome'] == 'miss')][delta_col]
./python/fig6/stats_table.py:61:        npl_hit = npl_df[(npl_df['rel_week'] == week) & (npl_df['trial_outcome'] == 'hit')][delta_col]
./python/fig6/stats_table.py:62:        npl_miss = npl_df[(npl_df['rel_week'] == week) & (npl_df['trial_outcome'] == 'miss')][delta_col]
./python/fig6/hit_miss_histograms.py:67:        pl_hit = pl_df[(pl_df['rel_week'] == week) & (pl_df['trial_outcome'] == 'hit')][delta_col]
./python/fig6/hit_miss_histograms.py:68:        pl_miss = pl_df[(pl_df['rel_week'] == week) & (pl_df['trial_outcome'] == 'miss')][delta_col]
./python/fig6/hit_miss_histograms.py:69:        npl_hit = npl_df[(npl_df['rel_week'] == week) & (npl_df['trial_outcome'] == 'hit')][delta_col]
./python/fig
[... 26 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/icms-activation-plasticity && sed -n 570,600p python/fig_s5/generate_figure.py; sed -n 135,160p processing/pop_coupling/fig_utils.py; wc -l processing/batch_process/postprocessing/responses_v3/*.py; grep -n "rel_day\|rel_week\|z_score\|t_to_max\|pli\|PLI\|pulse_lock\|delta_spks\|baseline_too_slow\|paired\|ttest" processing/batch_process/postprocessing/responses_v3/*.py processing/batch_process/stage4_postprocess.py | head -80
```

```
})

    if missing:
        raise FileNotFoundError('Missing movement-onset source files:\n' +
                                '\n'.join(missing))

    df = pd.DataFrame(records)
    for aid in df['animal_id'].unique():
        mask = df['animal_id'] == aid
        dates = df.loc[mask, 'session'].apply(
            lambda s: datetime.strptime(s, '%d-%b-%Y'))
        first = dates.min()
        days = (dates - first).dt.days
        df.loc[mask, 'rel_week'] = np.where(days == 0, 0,
                                            np.ceil(days / 7).astype(int))

    df['rel_week'] = df['rel_week'].astype(int)
    return df


[... 95 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/icms-activation-plasticity/processing/batch_process/postprocessing && sed -n 1,488p responses_v3/stim_condition_response.py; cat responses_v3/window_config.py
```

```
"""
Refactored stimulus condition response classes with parameterized analysis windows.

Changes from v2:
- TrainResponse accepts window_config instead of hardcoded different_window_flag
- Hardcoded 700ms values replaced with window_config / timing_params references
- Constructor uses keyword arguments for clarity
"""
import numpy as np
import spikeinterface.full as si
import batch_process.postprocessing.stim_response_util as stim_response_util
import batch_process.postprocessing.responses_v2.pulse_locked_response_metrics as plrm
import batch_process.util.template_util as template_util
from batch_process.postprocessing.responses_v3.window_config import WindowConfig


class StimConditionResponse:
    """Stim condition response: contains a TrainResponse and PulseResponse."""

    def __init__(self, stim_timestamps, stim_channel, stim_current, unit_response):
[... 534 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/icms-activation-plasticity/processing/batch_process/postprocessing && grep -n "def \|null\|percentile\|99\|shuffle" responses_v2/pulse_locked_response_metrics.py | head -60; grep -n "def analyze_stimulus_train_response" -A80 stim_response_util.py | grep -n "ttest\|z_score\|sigma\|mean_fr\|std" ; grep -n "def get_time_max_fr" -A15 stim_response_util.py; grep -n "def compute_smoothed_firing_rate" -A25 stim_response_util.py
```

```
6:def get_baseline_interval_start_times(stim_timestamps, timing_params):
32:def get_spike_prob_distribution(raster_array, timing_params, subsample_fraction=1):
72:def get_latency(bin_centers, prob_spike):
77:def get_bootstrapped_metrics(raster_array, timing_params, subsample_fraction, num_iterations=100, return_summary=True):
102:def calculate_pulse_locked_index(bin_centers, spike_prob_distribution, timing_params):
138:def get_null_distribution(
196:def is_pulse_locked(stim_pli, phase_lock_indices):
197:    return stim_pli > np.percentile(phase_lock_indices, 99)
678:def get_time_max_fr(bin_centers, firing_rate, bin_min=None, bin_max=None):
679-    if len(firing_rate) == 0:  # Check if all_spikes is empty
680-        return np.nan
681-
682-    if bin_min is not None and bin_max is not None:
683-        mask = (bin_centers >= bin_min) & (bin_centers <= bin_max)
684-        bin_centers = bin_centers[mask]
685-        firing_rate = firing_rate[mask]
686-
687-    index = np.argmax(firing_rate)
688-    return bin_centers[index]
689-
[... 31 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/icms-activation-plasticity/processing/batch_process/postprocessing && sed -n 1,200p responses_v2/pulse_locked_response_metrics.py; sed -n 232,250p stim_response_util.py; grep -n "ttest\|z_score\|pre_stim_sigma\|np.std" stim_response_util.py | head -30
```

```
import batch_process.postprocessing.stim_response_util as stim_response_util
import numpy as np
import matplotlib.pyplot as plt


def get_baseline_interval_start_times(stim_timestamps, timing_params):

    trains = stim_response_util.group_stim_pulses_into_trains(
        stim_timestamps, timing_params)

    fs = timing_params["fs"]
    stim_duration_ms = timing_params["stim_duration_ms"]
    pulse_win_ms = timing_params["pulse_win_ms"]
    baseline_interval_start_times = []

    for train in trains:
        first_pulse_ts = train[0]
        # Get baseline window before first pulse of stim train
        # Baseline window size is same as stim train size
        baseline_start = int(first_pulse_ts - stim_duration_ms * fs / 1000)
[... 210 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/icms-activation-plasticity/processing && grep -rn "pre_stim_threshold\s*=\|max_spike_prob\"\?\s*[:=]\|'max_spike_prob'\|\"max_spike_prob\"\|bin_width_ms\"\?\s*[:=]\|'bin_width_ms'\s*:\|pulse_win_ms'\s*:\|blank_ms'\s*:" . | head -20; sed -n 560,600p batch_process/postprocessing/stim_response_util.py
```

```
./control/postprocessing/process_control_responses.py:70:                        "max_spike_prob": np.max(pr.stim_metrics["mean_prob_spike"]),
./batch_process/stage4_postprocess.py:81:def store_result(stim_response, results, pre_stim_threshold=0.5):
./batch_process/stage4_postprocess.py:106:            "max_spike_prob": np.max(pr.stim_metrics["mean_prob_spike"]),
./batch_process/postprocessing/responses_v3/process_stim_responses.py:16:def store_result(stim_response, results, include=True, pre_stim_threshold=0.5):
./batch_process/postprocessing/responses_v3/process_stim_responses.py:41:            "max_spike_prob": np.max(pr.stim_metrics["mean_prob_spike"]),
./batch_process/postprocessing/responses_v2/response_plotting_util.py:559:def plot_z_scores(responses, axs, pre_stim_threshold=0.5):
./batch_process/postprocessing/responses_v2/response_plotting.py:28:    pre_stim_threshold = 0.5  # Pre-stimulus firing rate threshold to be included
./batch_process/postprocessing/responses_v2/pulse_locked_response_metrics.py:34:    bin_width_ms = timing_params["bin_width_ms"]
    stim_spikes_count = [len(spikes) for spikes in train_spike_times]
    pre_stim_spikes_count = [len(spikes) for spikes in pre_stim_spike_times]

    # Create dictionaries for spike times and indices
    spike_times_dict = {
        'pre_stim_spike_times': pre_stim_spike_times,
        'train_spike_times': train_spike_times,
        'post_stim_spike_times': post_stim_spike_times
    }

    spike_indices_dict = {
        'pre_stim_spike_indices': pre_stim_spike_indices,
[... 30 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/icms-activation-plasticity/matlab && cat fig2/fig2a_thresholds.m fig2/fig2c_neuron_counts.m | grep -v "^\s*%" | grep -v "^\s*$" | head -200
```

```
if ~exist('DATA_ROOT','var'), run(fullfile(pwd, 'matlab', 'config.m')); end
load(FIG2_DATA);
weeks = [];
thresholds = [];
for animal_index = 1:6
    dayThresholds = daysThresholdsAll{animal_index}(:);
    daysTrained = ones(3, 1) * daysTrainedAll{animal_index};
    daysTrained = daysTrained(:);
    weeks_of_training = ceil(daysTrained / 7);
    valid_idx = dayThresholds ~= 0 & weeks_of_training < 5;
    thresholds = [thresholds; dayThresholds(valid_idx)];
    weeks = [weeks; weeks_of_training(valid_idx)];
end
figure;
scatter(weeks, thresholds, 50, 'filled', 'MarkerFaceAlpha', 0.6);
xlabel('Week of Training');
ylabel('Threshold');
title('Thresholds vs Training Week');
xlim([-0.5, 4.5])
xticks(0:4)
[... 131 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/icms-activation-plasticity/matlab && cat report_stat.m | grep -v "^\s*%" | head -40; for f in fig2/fig2e_density_r50_5uA.m fig2/fig2g_neurons_density_threshold.m; do echo "=== $f"; grep -v "^\s*%" $f | grep -iv "set(\|color\|font\|xlim\|ylim\|xtick\|ytick\|legend\|xlabel\|ylabel\|^\s*$\|fig2svg\|scatter\|plot(\|patch" ; done
```

```
function report_stat(csvPath, panel, comparison, vals1, vals2)

    n1 = numel(vals1);
    n2 = numel(vals2);
    med1 = median(vals1, 'omitnan');
    med2 = median(vals2, 'omitnan');

    [p, ~, stats] = ranksum(vals1, vals2);

    W = stats.ranksum;
    U = W - n1*(n1+1)/2;

    if isfield(stats, 'zval')
        Z = stats.zval;
        r = abs(Z) / sqrt(n1 + n2);
    else
        Z = NaN;
        r = NaN;
    end

[... 192 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/icms-activation-plasticity/matlab && for f in fig3/fig3def_longitudinal_trends.m fig3/fig3jlmn_subset_analysis.m fig3/fig3_stats.m; do echo "=== $f"; grep -v "^\s*%" $f | grep -iv "set(\|color\|font\|xlim\|ylim\|xtick\|ytick\|legend\|xlabel\|ylabel\|^\s*$\|fig2svg\|scatter(\|plot(\|patch\|title(\|hold \|figure" ; done | head -400
```

```
=== fig3/fig3def_longitudinal_trends.m
if ~exist('DATA_ROOT','var'), run(fullfile(pwd, 'matlab', 'config.m')); end
metrics = {mergedDFF, mergedTrendsOnset, mergedTrendsDur};
metricNames = {'Maximum \DeltaF/F', 'Spike Onset (ms)', 'Spike Duration (ms)'};
panelNames = {'D', 'E', 'F'};
if exist('weekTimepoints', 'var')
    wkTP = weekTimepoints;
else
    wkTP = 0:4;
end
for t = 1:3
    metricTrend = metrics{t};
    fprintf('\n========================================\n');
    fprintf('Panel %s: %s\n', panelNames{t}, metricNames{t});
    fprintf('========================================\n');
    fprintf('Total response units (rows in mergedDFF): %d\n', size(metricTrend, 1));
    fprintf('\nValid data points per week:\n');
    totalDataPoints = 0;
    for w = 1:5
        valid_w = isfinite(metricTrend(:,w)) & metricTrend(:,w) ~= 0;
[... 347 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/icms-activation-plasticity && grep -rn "subsetMerged\|mean.*std\|std.*mean" matlab/fig3/fig3i_histogram.m | head; grep -rln "subsetMerged" . ; grep -v "^\s*%" matlab/fig3/fig3i_histogram.m | grep -iv "set(\|color\|font\|xlim\|ylim\|xtick\|ytick\|legend\|xlabel\|ylabel\|^\s*$\|fig2svg\|title(\|hold \|figure" | head -60
```

```
13:thresh = mean(lateVals) + std(lateVals);
./processing/imaging/planar/roiPLotter2_exploringCode.m
./processing/imaging/planar/roiPLotter2Miss.m
./matlab/fig3/fig3jlmn_subset_analysis.m
./matlab/fig3/fig3_stats.m
./matlab/fig3/fig3_pipeline_counts.m
if ~exist('DATA_ROOT','var'), run(fullfile(pwd, 'matlab', 'config.m')); end
load(fullfile(DATA_ROOT, 'fig3def_plot_data.mat'));
earlyVals = reshape(mergedDFF(:,1:2), 1, []);
earlyVals = earlyVals(isfinite(earlyVals));
lateVals = reshape(mergedDFF(:,4:5), 1, []);
lateVals = lateVals(isfinite(lateVals));
thresh = mean(lateVals) + std(lateVals);
fprintf('Early (weeks 0-1): n=%d, mean=%.3f\n', numel(earlyVals), mean(earlyVals));
fprintf('Late (weeks 3-4): n=%d, mean=%.3f\n', numel(lateVals), mean(lateVals));
fprintf('Above threshold: %d\n', sum(lateVals > thresh));
fprintf('Below threshold: %d\n', sum(lateVals <= thresh));
binWidth = 0.08;
edgesBelow = fliplr(thresh:-binWidth:0.2);
edgesAbove = thresh:binWidth:3.7;
[... 9 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/icms-activation-plasticity/processing/imaging/planar && grep -n "subsetMerged\|subset" roiPLotter2_exploringCode.m | head -30
```

```
2647:            % subset = ascend; % slope trend
2648:            % subset2 = nonmon | decend; 
2652:            % subset = ascendGain; % gain trend
2653:            % subset2 = nonmonGain | decendGain; 
2655:            subset = ascendEnd; % max end trend
2656:            subset2 = nonmonEnd | decendEnd; 
2730:    %% Plot spatial distribution of subset and non-subset populations   
2733:    metricTrendInvROI = allTrendsRoiCh(subset2,:);
2734:    metricTrendROI = allTrendsRoiCh(subset,:);
3382:allSubset{animal} = subset;
3391:%     subset = subset1;
3392:%     subset2 = nonmon;
3462:        metricTrendInv = metricTrend(subset2,:);
3463:        metricTrend = metricTrend(subset,:);
3504:%     subset = subset1;
3505:%     subset2 = nonmon;
3575:        metricTrendInv = metricTrend(subset2,:);
3576:        metricTrend = metricTrend(subset,:);
3735:% %     subset = subset1;
3736:% %     subset2 = nonmon;
[... 11 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/icms-activation-plasticity/processing/imaging/planar && grep -n "ascendEnd\s*=\|ascendEnd =\|decendEnd\s*=\|nonmonEnd\s*=\|endThresh\|maxEnd" roiPLotter2_exploringCode.m | head -20
```

```
2640:        nonmonEnd = true(size(metricTrend,1),1);
2641:        ascendEnd = fMax > (mean(fMax) + std(fMax));
2642:        decendEnd = fMax < (mean(fMax) - std(fMax));
2643:        nonmonEnd(ascendEnd==1) = 0;
2644:        nonmonEnd(decendEnd==1) = 0;
Shell cwd was reset to
[... 1 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/icms-activation-plasticity/processing/imaging/planar && sed -n 2600,2645p roiPLotter2_exploringCode.m
```

```
%     curData = AllData{datSet};
        %     regions = curData.regions;
        %     curPx = regions(curROIs(datSet)).PixelList;
        %     cents(r,:) = mean(curPx,1);
        % end
        % curDists = pdist2(mean(chanPositions,1),cents);
        % scatter(curDists,fitM)
        % xlabel('Neuron Distance (\mum)')
        % ylabel(strcat(ytext,{' '},'Slope'))
        % title(strcat(titleTxt,{' '},'Activation Distance'))
        % combineFileName = strcat(curFld,'DistanceTrends',svTxt,'.fig');
        % % saveas(curFig,combineFileName);  
        % combineFileName = strcat(curFld,'DistanceTrends',svTxt,'.tif');
        % % saveas(curFig,combineFileName);
        % close(curFig)
        
        
        
        
        
[... 26 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/icms-activation-plasticity/processing/imaging/planar && grep -n "fMax\s*=" roiPLotter2_exploringCode.m | head; grep -n "fMax\s*=" -B3 -A3 roiPLotter2_exploringCode.m | head -30
```

```
2521:        fMax = zeros(size(metricTrend,1),1);
2518-        fitM = zeros(size(metricTrend,1),1);
2519-        allP = zeros(size(metricTrend,1),2);
2520-        fGain = zeros(size(metricTrend,1),1);
2521:        fMax = zeros(size(metricTrend,1),1);
2522-        bMax = zeros(size(metricTrend,1),1);
2523-
2524-        % curFig = figure();
Shell cwd was reset to
[... 1 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/icms-activation-plasticity/processing/imaging/planar && sed -n 2524,2570p roiPLotter2_exploringCode.m | grep -v "^\s*%"
```

```
for i = 1:size(metricTrend,1) % Add check if metricTrend is all NaNs

            d = daysTrained;
            m = metricTrend(i,:);

            if(numel(m)==sum(isnan(m)))
                continue
            end
            d(isnan(m)) = [];
            m(isnan(m)) = [];
            p = polyfit(d, m, 1);
            fitM(i) = p(1);
            allP(i,:) = p;
            fGain(i) = m(end)-m(1);
            fMax(i) = m(end);
            bMax(i) = m(1);
        end
Shell cwd was reset to
[... 1 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/icms-activation-plasticity && grep -rln "psignifit\|ps.psignifit\|sigmoid" . | head; grep -rn "delta_spks\s*=\|'delta_spks'\]\s*=\|bin_centers\|hit_miss_psth.npz" --include=*.py processing python | grep -v "^python/fig6/hit_miss_psth.py" | head -20
```

```
./processing/dataloader.py
./processing/batch_process/util/curate_util.py
./processing/batch_process/postprocessing/stim_response_util.py
processing/batch_process/postprocessing/stim_response_util.py:232:    bin_centers = bins[:-1] + bin_size / 2
processing/batch_process/postprocessing/stim_response_util.py:255:    return smoothed_rate, binned_firing_rate, bin_centers
processing/batch_process/postprocessing/stim_response_util.py:668:    bin_centers = bins[:-1] + bin_size / 2
processing/batch_process/postprocessing/stim_response_util.py:673:    time_to_max = bin_centers[np.argmax(hist)]
processing/batch_process/postprocessing/stim_response_util.py:675:    return bin_centers, hist, time_to_max
processing/batch_process/postprocessing/stim_response_util.py:678:def get_time_max_fr(bin_centers, firing_rate, bin_min=None, bin_max=None):
processing/batch_process/postprocessing/stim_response_util.py:683:        mask = (bin_centers >= bin_min) & (bin_centers <= bin_max)
processing/batch_process/postprocessing/stim_response_util.py:684:        bin_centers = bin_centers[mask]
processing/batch_process/postprocessing/stim_response_util.py:688:    return bin_centers[index]
processing/batch_process/postprocessing/stim_response_util.py:691:def get_time_to_fr_threshold_crossing(bin_centers, firing_rate, pre_stim_mean_fr, pre_stim_std_fr, bin_min=None, bin_max=None):
processing/batch_process/postprocessing/stim_response_util.py:695:        mask = (bin_centers >= bin_min) & (bin_centers <= bin_max)
processing/batch_process/postprocessing/stim_response_util.py:696:        bin_centers = bin_centers[mask]
processing/batch_process/postprocessing/stim_response_util.py:699:    for index, t in enumerate(bin_centers):
processing/batch_process/postprocessing/responses_v3/stim_condition_response.py:266:            self.baseline_metrics["bin_centers"],
processing/batch_process/postprocessing/responses_v3/stim_condition_response.py:274:            self.stim_metrics["bin_centers"],
processing/batch
[... 5 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/icms-activation-plasticity && grep -n "psignifit\|sigmoid" processing/dataloader.py | head
```

```
10:# Lazy import: psignifit only needed for threshold calculation
11:# import psignifit as ps
464:        options = {"sigmoidName": "norm",
490:                psignifit_data = np.column_stack(
494:                psignifit_data = np.row_stack(
495:                    [catch_trial_row, psignifit_data])
497:                import psignifit as ps
498:                result = ps.psignifit(psignifit_data, options)
Shell cwd was reset to
[... 1 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/icms-activation-plasticity && sed -n 440,530p processing/dataloader.py
```

```
self.trial_df = trial_df
        return self.trial_df

    def get_hit_trials_stim_timestamps(self):
        self.hit_trials_stim_timestamps = []
        for _, trial in self.trial_df.iterrows():
            if (trial['response'] == 1) & (trial['current'] > 0):
                self.hit_trials_stim_timestamps.append(
                    trial['stim_timestamps'])

        self.hit_trials_df = self.trial_df[(
            self.trial_df['current'] > 0) & (self.trial_df['response'] == 1)].reset_index(drop=True)

    def get_miss_trials_stim_timestamps(self):
        self.miss_trials_stim_timestamps = []
        for _, trial in self.trial_df.iterrows():
            if (trial['response'] == 0) & (trial['current'] > 0):
                self.miss_trials_stim_timestamps.append(
                    trial['stim_timestamps'])

[... 73 more lines not kept]
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
python -c "
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
cd $TMPDIR/icms-activation-plasticity && for f in python/fig_s1/generate_figure.py python/fig_s3/generate_figure.py python/fig_s4/generate_figure.py python/fig_s7/generate_figure.py python/fig_s8/generate_figure.py python/fig_s9/generate_figure.py; do echo "=== $f"; head -30 $f | grep -v "^import\|^from\|^sys"; grep -n "mannwhitneyu(\|wilcoxon(\|fisher_exact(\|linregress\|polyfit\|alternative=\|filter_\w*(\|def \w*(" $f | head -40; done
```

```
=== python/fig_s1/generate_figure.py
"""Figure S1 — Behavioral characterization.

Panels:
  A: Response time histogram
  B: CDF of response times
  C: Psychometric curves (example session)
  D: Detection thresholds over weeks (individual animals)
  E: Response times over weeks (individual animals)

Usage:
    python python/fig_s1/generate_figure.py
"""

matplotlib.use('Agg')


41:def _get_rel_days(sessions):
59:def plot_rt_histogram_and_cdf():
95:def plot_detection_thresholds():
[... 153 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/icms-activation-plasticity && sed -n 30,115p python/fig_s7/generate_figure.py; sed -n 160,175p python/fig_s1/generate_figure.py; sed -n 166,200p python/fig_s1/generate_figure.py | grep -n "mannwhit\|median\|rt\b" ; sed -n 180,240p python/fig_s3/generate_figure.py
```

```
FIG_DIR = OUTPUT_DIR / 'fig_s7'
FIG_DIR.mkdir(parents=True, exist_ok=True)

SCATTER_SIZE = 5


def load_control():
    df = pd.read_csv(CONTROL_CSV)
    if 'animal' in df.columns:
        df = df.rename(columns={'animal': 'animal_id'})

    for aid in df['animal_id'].unique():
        mask = df['animal_id'] == aid
        sessions = df.loc[mask, 'session_date'].unique()
        dates = sorted([datetime.strptime(s, '%Y-%m-%d') for s in sessions])
        first_date = dates[0]
        for s in sessions:
            d = datetime.strptime(s, '%Y-%m-%d')
            delta = (d - first_date).days
            df.loc[(df['animal_id'] == aid) & (df['session_date'] == s), 'rel_day'] = delta
[... 146 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/icms-activation-plasticity/matlab && grep -n "ranksum\|report_stat\|curCurr\s*=\|weeks\s*[<>]=\?\|kruskal\|anova" fig_s2/*.m | head -30
```

```
fig_s2/figs2abc_density_lines_rings.m:29:        curCurr = targetCurrents(cIdx);
fig_s2/figs2d_control_vs_behavior_density.m:37:curCurr = 5; min_neurons = 1;
fig_s2/figs2d_control_vs_behavior_density.m:156:p_count = ranksum(allVals(allWeeks<=1), allVals(allWeeks>=2));
fig_s2/figs2d_control_vs_behavior_density.m:158:b_p_count = ranksum(b_allVals_plot(b_allWeeks_plot<=1), b_allVals_plot(b_allWeeks_plot>=2));
fig_s2/figs2d_control_vs_behavior_density.m:162:report_stat(statsCSV, 'SFig2D', 'control_density early(0-1) vs late(2-3)', ...
fig_s2/figs2d_control_vs_behavior_density.m:164:report_stat(statsCSV, 'SFig2D', 'behavior_density_5uA early(0-1) vs late(2-3)', ...
fig_s2/figs2e_control_vs_behavior_count.m:37:curCurr = 5;
fig_s2/figs2e_control_vs_behavior_count.m:157:p_count = ranksum(allVals(allWeeks<=1), allVals(allWeeks>=2));
fig_s2/figs2e_control_vs_behavior_count.m:159:b_p_count = ranksum(b_allVals_plot(b_allWeeks_plot<=1), b_allVals_plot(b_allWeeks_plot>=2));
fig_s2/figs2e_control_vs_behavior_count.m:163:report_stat(statsCSV, 'SFig2E', 'control_count early(0-1) vs late(2-3)', ...
fig_s2/figs2e_control_vs_behavior_count.m:165:report_stat(statsCSV, 'SFig2E', 'behavior_count_5uA early(0-1) vs late(2-3)', ...
fig_s2/figs2f_neurons_at_threshold.m:136:[pval, ~, ~] = ranksum(early_vals, late_vals);
fig_s2/figs2f_neurons_at_threshold.m:140:report_stat(statsCSV, 'SFig2F', 'neuron_count_threshold early(0-1) vs late(2-4)', early_vals, late_vals);
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/icms-activation-plasticity/python && sed -n 379,418p fig_s8/generate_figure.py; grep -n "def generate\|mannwhitneyu(\|alternative=\|filter_\w*(\|RAW_DF_120\|stim_current\|collapse\|CURRENTS" fig_s5/generate_figure.py | head -40
```

```
def plot_panel_d(fig, gs_d, raw_df, tracked_set):
    """Modulation trends restricted to tracked units.

    1 row x 4 cols: PL z-score | NPL z-score | PL t2max | NPL t2max
    """
    df_pl = filter_pl(raw_df)
    df_npl = filter_npl(raw_df)

    pl_tracked = filter_to_tracked(df_pl, tracked_set)
    npl_tracked = filter_to_tracked(df_npl, tracked_set)
    pl_tracked = pl_tracked[pl_tracked['rel_week'] <= 4]
    npl_tracked = npl_tracked[npl_tracked['rel_week'] <= 4]

    print(f'  PL tracked rows: {len(pl_tracked)}, NPL tracked rows: {len(npl_tracked)}')

    gs_inner = gs_d.subgridspec(1, 4, wspace=0.4)

    panels = [
        (0, 0, pl_tracked, 'z_score', 'Modulation (z)', 'PL', 'two-sided', Z_CLIP),
        (0, 1, npl_tracked, 'z_score', '', 'NPL', 'two-sided', Z_CLIP),
[... 48 more lines not kept]
```

**Agent calls Write**

```json
{
 "file_path": "claims/001868/10.64898-2026.06.05.730421.yaml",
 "content": "# Claims for Kim, Lycke, Zolotavin, Montes, Xie & Luan (2026), \"Learning induces\n# activation-mechanism-dependent neural plasticity in an intracortical microstimulation task\",\n# on dandiset 001868.\n# Written by an agent (model \"claude-opus-5-5\", Claude Code in GitHub Actions), 2026-10-21,\n# protocol pilot-10 as stated in docs/protocol.md.\n#\n# Text read: the bioRxiv preprint, version 1 (doi:10.64898/2026.06.05.730421v1), from its JATS\n# XML (paper/10.64898-2026.06.05.730421.txt): main text, figure legends of Figures 1 to 7 and\n# Materials and Methods. No PDF was supplied. The supplementary materials (figs. S1 to S9 and\n# their legends) were not available: the \"Supporting information\" section of the text is empty.\n# The main findings rest on Figures 2 to 6, which are in the text. Claims about findings shown\n# only in the supplement are written from the main-text sentence that states them, and their\n# methods are taken from the paper's code for that supplementary figure; the figure itself was\n# not read. The code's README calls the paper accepted at Science Advances; the version of\n# record was not read.\n#\n# Code read: github.com/XieLuanLab/icms-activation-plasticity at commit d1922d16913b50bf6338ff4e\n# 0c2953cb8ef43d15 (2026-07-15), archived as Zenodo doi:10.5281/zenodo.19561006 (v1.0). It holds\n# python/ (figure scripts for Figs. 4 to 6 and figs. S1, S3 to S9, reading processed tables from\n# a data/ folder on Zenodo), matlab/ (figure scripts for Figs. 2, 3 and fig. S2) and processing/\n# (the upstream pipeline from raw recordings: artifact removal and Mountainsort5 sorting,\n# per-response metrics in processing/batch_process/postprocessing/, pulse-locking in\n# responses_v2/pulse_locked_response_metrics.py, psychometric thresholds in processing/\n# dataloader.py, population coupling in processing/pop_coupling/, imaging ROI analysis in\n# processing/imaging/). Where the Methods leave a choice open, the criteria below follow the\n# code and say so.\n#\n# Data the paper used. 12 Thy1-GCaMP6s mice (C57BL/6J-Tg(Thy1-GCaMP6s)GP4.3Dkim/J): 6 behavioural\n# mice (4 male, 2 female; the code calls them ICMS92, ICMS93, ICMS98, ICMS100, ICMS101 and\n# ICMS83, shown as Mouse 1 to Mouse 6) and 6 control mice from an earlier study (ref. 22) that\n# were stimulated, imaged and recorded without behavioural training (the code's control\n# coupling uses ICMS43, ICMS45, ICMS48, ICMS54 and ICMS56). Each mouse carries a 32-channel\n# ultraflexible NET in S1 under a cranial window. Behavioural mice did an ICMS detection task\n# (turn a wheel within the 700 ms, 100 Hz train; 3 uL water), in sessions of four 100-trial\n# blocks (10 catch trials at 0 uA and 90 stimulation trials, 3 channels x 3 currents x 10),\n# plus a fifth block for planar imaging, over about four weeks. Measured variables: trial\n# outcomes (hit, miss, catch responses), response times and wheel movement onset (rotary\n# encoder, 5 animals); 30 kHz electrophysiology from the NET, spike sorted (973 units, 6\n# animals); volumetric two-photon imaging (25 um steps, 300 um depth, 30 fps, 1 x 1 mm) and\n# planar imaging at 100 um depth (ROIs, dF/F, OASIS-deconvolved spikes), with longitudinal\n# tracking of planar ROIs in 3 animals (Mouse1 to Mouse3). Only 4, 5 and 6 uA are analysed.\n# Weeks of training: in the code, week = ceil(days since the animal's first session / 7), with\n# the first session as week 0; early phase = weeks 0 and 1, late phase = weeks 2 to 4; later\n# sessions are left out. The dandiset title (\"Chronic electrophysiology and two-photon calcium\n# imaging of mouse primary somatosensory cortex during intracortical microstimulation learning\")\n# says it holds these data; whether it holds the control mice is for the author to find.\n#\n# Outside data (step 4). The paper deposits \"processed imaging and electrophysiological\n# datasets\" at Zenodo doi:10.5281/zenodo.17727762; the code's README instead points to figure\n# source data at Zenodo doi:10.5281/zenodo.21382755 and to this dandiset (version 0.260715.2016)\n# for the processed recordings. Raw recordings are available on request only. No claim below\n# needs outside data: every test is meant to run on the dandiset's own recordings, so all are\n# data: dataset. The Zenodo tables may help the author check the dandiset against the paper's\n# per-response tables.\n#\n# Conventions used in the criteria, all from the code unless marked:\n# - Electrophysiology \"responses\" are one unit in one stimulation channel and current\n#   condition (Methods). Modulated responses pass the code's filter_modulated (python/utils/\n#   filters.py): two-sided paired t-test of per-trial spike counts during the train against\n#   the 700 ms before it, p < 0.05, with z-score > 0 (an increase); more than 50 spikes; more\n#   than 5 trials; pre-stimulus rate at least 0.5 Hz; current 4 to 6 uA; week below 5;\n#   stimulation channels seen on fewer than 5 distinct days dropped; z-score below 100 (Fig. 4)\n#   or below 50 (filter_pl and filter_npl defaults, Fig. 5). The Methods give the t-test, 50\n#   spikes and 0.5 Hz; the rest is the code's.\n# - Modulation score = (mean rate during the train - mean pre-stimulus rate) / SD across trials\n#   of the pre-stimulus rate (Methods; stim_response_util.py). Time to maximum firing rate =\n#   argmax, between 0 and 700 ms, of the trial-averaged rate in 10 ms bins smoothed with a\n#   Gaussian of sigma 20 ms (column t_to_max_10ms_smoothed).\n# - Pulse-locking: spikes in each 10 ms interpulse interval in 0.5 ms bins, first 1.5 ms and last\n#   0.5 ms blanked (Methods); PLI = mean of the 3 bins around the peak minus the median bin, on\n#   the spike-probability curve averaged over 500 bootstrap draws of 20% of trials; pulse-locked\n#   when PLI exceeds the 99th percentile of 100 PLIs from uniformly placed spikes of the same\n#   count (pulse_locked_response_metrics.py). Peak spike probability = max of that mean curve.\n# - Putative pyramidal cells have trough-to-peak at or above 0.45 ms, interneurons below (Fig. 4H\n#   legend; cell_type_histogram.py).\n# - Early-against-late tests on responses pool all animals, per current, with two-sided\n#   Mann-Whitney U tests (legends; utils/longitudinal.py). The ephys effect size r is the\n#   rank-biserial 1 - 2U/(n_early n_late), positive when late is higher; the imaging r is\n#   |Z|/sqrt(N) (matlab/report_stat.m).\nschema_version: 2\ndataset:\n  archive: dandi\n  id: \"001868\"\npaper: doi:10.64898/2026.06.05.730421\nclaims:\n- id: fig2a-threshold-decrease\n  statement: Behavioural detection thresholds were lower in the late phase (weeks 2 to 4) than in\n    the early phase (weeks 0 to 1), falling from a median of 5.5 uA to 4.2 uA.\n  source: Results, Behavioral learning enhances ICMS-evoked population activation over time,\n    paragraph 1; Figure 2A\n  quote: The detection thresholds in the late phase were significantly lower than those in the\n    early phase ( Fig. 2A ), decreasing from a median of 5.5 µA to 4.2 µA (n early = 43, n late =\n    80, p = 7.68e-6, r = 0.40).\n  statistics:\n  - test: two-sided Mann-Whitney U test\n    statistic: r = 0.40\n    p: 7.68e-6\n    n: 43 early and 80 late channel-session thresholds, 6 animals, 18 channels\n  expected:\n  - quantity: median early-phase detection threshold\n    value: 5.5\n    tolerance: 0.55\n    unit: uA\n  - quantity: median late-phase detection threshold\n    value: 4.2\n    tolerance: 0.42\n    unit: uA\n  criterion: One threshold per stimulation channel and session, the mean of its four block\n    thresholds (Methods, Analysis of behavioral data). Each block threshold is fitted as in\n    processing/dataloader.py, with python-psignifit 4 (sigmoid \"norm\", experiment type \"YesNo\"),\n    on the channel's hits per current with the block's 10 catch trials added as a 0 uA point, and\n    read as the current at 0.5 of the fitted sigmoid (getThreshold 0.5). Weeks as in the header;\n    thresholds of 0 and weeks above 4 dropped (fig2a_thresholds.m). Two-sided Mann-Whitney U,\n    weeks 0 to 1 against weeks 2 to 4. Open, could change the outcome - which sessions count\n    (Methods, \"Only data that included 4, 5, and 6 μA stimulation amplitudes were analyzed\"),\n    read as (a) every session with a threshold for that channel (as fig2a_thresholds.m does, on\n    a precomputed table), or (b) only sessions in which 4, 5 and 6 uA were all presented on that\n    channel. Reproduced when, under a reading, p < 0.05 with the late median lower and both\n    medians within tolerance; partially reproduced when the test holds but a median falls\n    outside tolerance.\n- id: fig2a-steepest-early\n  statement: Thresholds fell most steeply in weeks 0 to 1 and changed more gradually, with\n    relative stability, in weeks 2 to 4; an exponential fit describes the decline.\n  source: Results, Behavioral learning enhances ICMS-evoked population activation over time,\n    paragraph 1; Figure 2A legend\n  quote: Over the weeks of behavioral learning, detection thresholds decreased ( Fig. 2A and fig.\n    S1D), with the steepest decline occurring during weeks 0–1, followed by more gradual changes\n    and relative stability in weeks 2–4.\n  depends_on:\n  - fig2a-threshold-decrease\n  criterion: On the channel-session thresholds of fig2a-threshold-decrease (under the reading\n    that claim matched), plotted against week, the legend's exponential fit. Its form is not\n    given (the fit is not in the code); readings are (a) a exp(-b week) + c and (b) a exp(-b\n    week), by least squares. Reproduced when, under both forms, the fitted curve decreases and\n    falls more between weeks 0 and 2 than between weeks 2 and 4, and the drop in the weekly\n    median between weeks 0 and 2 also exceeds that between weeks 2 and 4.\n- id: fig2b-example-recruitment\n  statement: In one representative animal at a fixed 4 uA, the number of ICMS-activated neurons in\n    the same field of view grew from 71 in week 0 to 114 in week 1 and 220 in week 2.\n  source: Results, Behavioral learning enhances ICMS-evoked population activation over time,\n    paragraph 2; Figure 2B\n  quote: In one representative animal at a fixed stimulation current of 4 µA, the number of\n    ICMS-activated neurons increased over time within the same field of view (FOV), with\n    progressively more cells recruited from week 0 (71 neurons) to week 1 (114 neurons) and to\n    week 2 (220 neurons)\n  expected:\n  - quantity: activated neurons, week 0, 4 uA\n    value: 71\n    tolerance: 7.1\n  - quantity: activated neurons, week 1, 4 uA\n    value: 114\n    tolerance: 11.4\n  - quantity: activated neurons, week 2, 4 uA\n    value: 220\n    tolerance: 22\n  criterion: Activated volumetric ROIs counted as in the Methods (Detection and quantification\n    of ICMS-evoked Ca2+ activation) and fig2c_neuron_counts.m (activated ROIs within 800 um of\n    the stimulation site). The paper names neither the animal, the channel nor the session.\n    Readings are every animal and stimulation channel with 4 uA sessions in weeks 0, 1 and 2,\n    taking one session per week (any session in that week). Reproduced when one animal and\n    channel gives all three counts within tolerance and increasing; partially reproduced when an\n    animal and channel gives three increasing counts with a two-fold or larger rise from week 0\n    to week 2 but not all within tolerance. The best match is reported with how many readings\n    were searched.\n- id: fig2c-count-increase\n  statement: The number of ICMS-activated neurons was larger in the late than in the early phase at\n    each of 4, 5 and 6 uA.\n  source: Results, Behavioral learning enhances ICMS-evoked population activation over time,\n    paragraph 2; Figure 2C\n  quote: \"resulting in significantly larger activated populations at all current levels in the\n    late learning phase than in the early phase ( Fig. 2C , 4 µA: n early = 13, n late = 41, p =\n    0.043, r = 0.28; 5 µA: n early = 20, n late = 35, p = 0.015, r = 0.33; 6 µA: n early = 22, n\n    late = 26, p = 0.0069, r = 0.39)\"\n  statistics:\n  - about: 4 uA, early against late\n    test: two-sided Mann-Whitney U test\n    statistic: r = 0.28\n    p: 0.043\n    n: 13 early and 41 late values\n  - about: 5 uA, early against late\n    test: two-sided Mann-Whitney U test\n    statistic: r = 0.33\n    p: 0.015\n    n: 20 early and 35 late values\n  - about: 6 uA, early against late\n    test: two-sided Mann-Whitney U test\n    statistic: r = 0.39\n    p: 0.0069\n    n: 22 early and 26 late values\n  criterion: As fig2c_neuron_counts.m does. Per animal, stimulation channel and current, the\n    count of activated volumetric ROIs within 800 um of the stimulation site in each session\n    (zero counts dropped), then the median over sessions of each week, giving one value per\n    animal, channel, current and week; the code skips the third channel of ICMS100. Per\n    current, a two-sided Mann-Whitney U test of week 0 to 1 values against week 2 to 4 values.\n    Reproduced when all three currents give p < 0.05 with the late median higher; partially\n    reproduced when one or two do. The legend's \"each dot represents an activation metric for a\n    given channel, session, and animal\" (one value per session, not per week) is run as a\n    variant.\n- id: fig2e-density-and-radius-increase\n  statement: At 5 uA, the density of activated neurons within 200 um of the stimulation site and\n    the activation radius (the distance enclosing 50% of activated neurons) both increased from\n    the early to the late phase.\n  source: Results, Behavioral learning enhances ICMS-evoked population activation over time,\n    paragraph 3; Figure 2D and 2E\n  quote: resulting in significantly higher activation density with learning within a radius of 200\n    μm ( Fig. 2E , n early = 22, n late = 40; p = 0.015, r = 0.31). ... we defined the distance\n    enclosing 50% of all activated neurons as the activation radius (Methods), which also\n    increased over time ( Fig. 2E, p = 1.1e-5, r = 0.56).\n  statistics:\n  - about: density within 200 um, early against late, 5 uA\n    test: two-sided Mann-Whitney U test\n    statistic: r = 0.31\n    p: 0.015\n    n: 22 early and 40 late channel-session values\n  - about: activation radius, early against late, 5 uA\n    test: two-sided Mann-Whitney U test\n    statistic: r = 0.56\n    p: 1.1e-5\n    n: 22 early and 40 late channel-session values\n  criterion: As fig2e_density_r50_5uA.m does, at 5 uA. One value per animal, channel and session\n    from the 3-D distances of activated ROIs to the stimulation site, kept between 0 and 800 um\n    - density = number within 200 um divided by the volume of a 200 um sphere; activation\n    radius = median distance (Methods, \"The enclosing radius was defined as the median distance\n    of activated neurons\"). Two-sided Mann-Whitney U, weeks 0 to 1 against 2 to 4. The script\n    loops over all animals but the last in its list (numel(anID)-1), while the legend says 6\n    animals; readings are (a) all 6 animals and (b) the code's first 5. Reproduced when, under a\n    reading, both tests give p < 0.05 with late higher; partially reproduced when one does.\n- id: figs2-density-peak-200um\n  statement: Activation density, in concentric 100 um shells around the stimulation site, peaked\n    at around 200 um.\n  source: Results, Behavioral learning enhances ICMS-evoked population activation over time,\n    paragraph 3 (fig. S2A, B, not available)\n  quote: The activation density peaked at around 200 μm (fig. S2A, B), consistent with previous\n    studies in the absence of behavioral learning( 5 ).\n  criterion: Density per shell = activated ROIs with distance in (r - 100, r] um divided by the\n    shell volume, shells of 100 um out to 500 um (Methods; fig2e_density_r50_5uA.m), per animal,\n    channel and session, then the median over these per shell, at each of 4, 5 and 6 uA. The\n    supplementary figure is not available, so which current and which summary it shows are open;\n    the readings are the three currents. Reproduced when, at every current, the highest median\n    density is in the 100 to 200 um or the 200 to 300 um shell; partially reproduced when that\n    holds at one or two currents.\n- id: fig2fg-stable-at-threshold\n  statement: When the current was set to each session's detection threshold, neither the density of\n    activated neurons within 200 um nor the total number of activated neurons differed between the\n    early and late phases.\n  source: Results, Behavioral learning enhances ICMS-evoked population activation over time,\n    paragraph 4; Figure 2F and 2G\n  quote: Notably, when the stimulation current was adjusted to the behavioral detection threshold\n    for each session ( Fig. 2F, G ), both the activation density and number of activated neurons\n    remained stable across learning phases (n early = 32, n late = 69; density: p = 0.511, r =\n    0.07; total number: p = 0.253, r = 0.11).\n  statistics:\n  - about: density within 200 um at threshold, early against late\n    test: two-sided Mann-Whitney U test\n    statistic: r = 0.07\n    p: 0.511\n    n: 32 early and 69 late channel-session values\n  - about: number of activated neurons at threshold, early against late\n    test: two-sided Mann-Whitney U test\n    statistic: r = 0.11\n    p: 0.253\n    n: 32 early and 69 late channel-session values\n  depends_on:\n  - fig2a-threshold-decrease\n  criterion: A claim of absence, judged on the paper's test. As fig2g_neurons_density_threshold.m\n    does, for each animal, channel and session, the session's threshold (fig2a-threshold-decrease)\n    rounded to the nearest integer current; the activated ROIs at that current within 800 um give\n    the count, and those within 200 um over the 200 um sphere volume give the density. Two-sided\n    Mann-Whitney U, weeks 0 to 1 against 2 to 4, at alpha 0.05. Reproduced when neither test\n    finds a difference; not reproduced when either does. Medians and r are reported either way.\n- id: figs2-control-recruitment-stable\n  statement: In control animals without ICMS behavioural learning, the number and spatial\n    distribution of activated neurons stayed stable and resembled those of the first training\n    weeks.\n  source: Results, Behavioral learning enhances ICMS-evoked population activation over time,\n    paragraph 3 (fig. S2E, F, not available)\n  quote: Importantly, in control animals not undergoing ICMS-driven behavioral learning, both the\n    number and spatial distribution of activated neurons remained stable and resembled those in\n    the initial training weeks (fig. S2E, F), confirming that the expansion of the activated\n    population is learning dependent.\n  criterion: A claim of absence, judged on the test of the paper's code, since the supplement is\n    not available. As figs2e_control_vs_behavior_count.m and figs2d_control_vs_behavior_density.m\n    do, at 5 uA in the control mice, the per channel and session count of activated ROIs within\n    800 um and the density within 200 um, compared between weeks 0 to 1 and weeks 2 and later\n    by two-sided Mann-Whitney U at alpha 0.05. Reproduced when neither test finds a difference\n    in the controls; not reproduced when either does. The control medians are also set against\n    the behavioural mice's week 0 to 1 medians at 5 uA and reported, without deciding the\n    outcome. Blocked if the dandiset holds no control mice.\n- id: fig3b-tracked-counts\n  statement: Among 10,608 planar ROIs tracked across weeks in 3 animals, 4469 were activated by\n    ICMS; 114 were activated in all weeks, 370 in 4 of 5 weeks, and 2063 in only one session.\n  source: Results, Longitudinal tracking of individual neurons reveals learning-sensitive\n    subpopulations, paragraph 1; Figure 3B\n  quote: Among 10,608 tracked neurons in 3 animals, 4469 neurons were activated by ICMS. Among the\n    ICMS-activated neurons, 114 were activated at all weeks, 370 neurons were activated in 4 out\n    of 5 weeks, and 2063 were only activated in one session ( Fig. 3B ).\n  expected:\n  - quantity: tracked planar neurons\n    value: 10608\n    tolerance: 1060.8\n  - quantity: tracked neurons activated by ICMS\n    value: 4469\n    tolerance: 446.9\n  - quantity: activated in all weeks\n    value: 114\n    tolerance: 11.4\n  - quantity: activated in 4 of 5 weeks\n    value: 370\n    tolerance: 37\n  - quantity: activated in only one session\n    value: 2063\n    tolerance: 206.3\n  criterion: Planar ROIs matched across weekly sessions as in the Methods (Alignment and unit\n    tracking via Ca2+ imaging), or by the dandiset's own cross-session ROI identities if it holds\n    them; an ROI is activated in a session when its trial-averaged dF/F within the stimulation\n    window exceeds the mean + 2 SD of its whole trace for more than 5 frames with onset before\n    700 ms (Methods), at any channel and current. Reproduced when all five counts are within\n    tolerance; partially reproduced when the total and activated counts are within tolerance but\n    some of the three longevity counts are not.\n- id: fig3def-stable-cells\n  statement: Neurons reliably activated and tracked across all or all but one of the sessions\n    showed no change in maximum dF/F or response duration over training, and their fluorescence\n    onset times decreased.\n  source: Results, Longitudinal tracking of individual neurons reveals learning-sensitive\n    subpopulations, paragraph 2; Figure 3D to 3F\n  quote: On average, these longitudinally stable cells exhibited no significant changes in either\n    ΔF/F max or fluorescence duration (n = 226, Wilcoxon signed-rank tests; p = 0.8478, r < 0.01\n    for ΔF/F max and p = 0.8306, r = 0.01 for duration), and a significant decrease in\n    fluorescence onset times (Wilcoxon signed-rank tests, p = 5.72e-11, r = 0.30) over time (\n    Fig. 3D–F ).\n  statistics:\n  - about: maximum dF/F, early against late\n    test: Wilcoxon signed-rank test\n    statistic: r < 0.01\n    p: 0.8478\n    n: 226 tracked response units, 3 animals\n  - about: response duration, early against late\n    test: Wilcoxon signed-rank test\n    statistic: r = 0.01\n    p: 0.8306\n    n: 226 tracked response units, 3 animals\n  - about: onset time, early against late\n    test: Wilcoxon signed-rank test\n    statistic: r = 0.30\n    p: 5.72e-11\n    n: 226 tracked response units, 3 animals\n  expected:\n  - quantity: stable tracked response units\n    value: 226\n    tolerance: 22.6\n  criterion: Tracked units are the planar ROI and current pairs activated in all sessions, or all\n    but one, in which that current was applied (Results); the code's tracking keeps ROIs present\n    in at least 4 sessions for Mouse1 and 3 for Mouse2 and Mouse3 (Methods). Per unit, the mean of\n    its weekly values over weeks 0 and 1 and over weeks 2 to 4, units lacking either dropped, then\n    a Wilcoxon signed-rank test (as the legend and fig3def_longitudinal_trends.m; fig3_stats.m\n    runs a rank-sum test on the same values, shown as a variant). Onset decrease is reproduced\n    when p < 0.05 with late onset earlier. The two absences (maximum dF/F, duration) are judged\n    on the signed-rank test at alpha 0.05, reproduced when it finds no change. The claim is\n    reproduced when all three parts hold, partially when one or two do.\n- id: fig3i-more-high-intensity-cells\n  statement: By week 4, more tracked neurons had fluorescence intensities above the mean + STD of\n    the distribution than at week 0.\n  source: Results, Longitudinal tracking of individual neurons reveals learning-sensitive\n    subpopulations, paragraph 2; Figure 3I\n  quote: By week 4, more neurons exhibited fluorescence intensities exceeding mean + STD ( Fig. 3I\n    ), indicating enhanced excitability.\n  criterion: As fig3i_histogram.m does, on the tracked units of fig3def-stable-cells, the\n    threshold is the mean + SD of the late maximum dF/F values (weeks 3 and 4 pooled in that\n    script). Reproduced when the fraction of unit values above that threshold is larger in weeks\n    3 to 4 than in weeks 0 to 1, in the pooled data and in at least 2 of the 3 animals (the\n    figure shows one representative animal, which is not named). Fractions and counts are\n    reported per animal.\n  depends_on:\n  - fig3def-stable-cells\n- id: fig3j-subgroup-increase\n  statement: Tracked neurons with high maximum dF/F in the final week showed significant increases\n    in fluorescence over training, while the remaining neurons did not; the two groups were similar\n    in weeks 0 and 1 and diverged from week 2 to week 4.\n  source: Results, Longitudinal tracking of individual neurons reveals learning-sensitive\n    subpopulations, paragraph 2; Figure 3J\n  quote: These neurons showed significant increases in fluorescence over training, whereas the\n    remaining neurons (blue) did not (two-sided Mann-Whitney U test; red ... p = 9.76e-4, r =\n    0.32; blue ... p = 0.1176, r = 0.08). The high intensity subgroup initially exhibited\n    fluorescence comparable to the rest of the population (week 0 ... p = 0.5078, r = 0.0355;\n    week 1 ... p = 0.0988, r = 0.0885) but diverged over time, showing significantly stronger\n    responses by week 2 (p = 0.0018, r = 0.16) that persisted until the end of learning (week 3\n    ... p = 8.62e-15, r = 0.41; week 4 ... p = 2.48e-9, r = 0.31).\n  statistics:\n  - about: high-intensity subgroup, early against late\n    test: two-sided Mann-Whitney U test\n    statistic: r = 0.32\n    p: 9.76e-4\n    n: 52 early and 57 late\n  - about: remaining neurons, early against late\n    test: two-sided Mann-Whitney U test\n    statistic: r = 0.08\n    p: 0.1176\n    n: 174 early and 220 late\n  - about: subgroup against remaining, week 0\n    test: two-sided Mann-Whitney U test\n    statistic: r = 0.0355\n    p: 0.5078\n  - about: subgroup against remaining, week 1\n    test: two-sided Mann-Whitney U test\n    statistic: r = 0.0885\n    p: 0.0988\n  - about: subgroup against remaining, week 2\n    test: two-sided Mann-Whitney U test\n    statistic: r = 0.16\n    p: 0.0018\n  - about: subgroup against remaining, week 3\n    test: two-sided Mann-Whitney U test\n    statistic: r = 0.41\n    p: 8.62e-15\n  - about: subgroup against remaining, week 4\n    test: two-sided Mann-Whitney U test\n    statistic: r = 0.31\n    p: 2.48e-9\n  depends_on:\n  - fig3def-stable-cells\n  criterion: The subgroup, as the processing code defines it (roiPLotter2_exploringCode.m,\n    ascendEnd) - per animal, the tracked units whose last non-missing maximum dF/F exceeds the\n    mean + SD of those last values; the remaining group is every other tracked unit. The fixed\n    threshold of fig3i_histogram.m (mean + SD of pooled week 3 and 4 values) is a variant.\n    As fig3jlmn_subset_analysis.m, for each group the per-unit means over weeks 0 to 1 and over\n    weeks 2 to 4, compared by a two-sided Mann-Whitney U test; and per week, subgroup against\n    remaining values (zeros and missing dropped), two-sided Mann-Whitney U. Reproduced when the\n    subgroup increases (p < 0.05, late higher), the remaining group shows no change at alpha\n    0.05, the week 0 and week 1 comparisons are not significant and weeks 2, 3 and 4 are, with\n    the subgroup higher. Partially reproduced when the subgroup increase and at least two of the\n    week 2 to 4 differences hold but another part fails.\n- id: fig3lm-subgroup-spikes-latency\n  statement: In the high-intensity subgroup, deconvolved spike counts rose and spike onset latency\n    fell from the early to the late phase, while the remaining neurons changed little; the\n    subgroup matched the rest in weeks 0 and 1 and differed from week 2 to week 4 in both\n    measures.\n  source: Results, Longitudinal tracking of individual neurons reveals learning-sensitive\n    subpopulations, paragraph 3; Figure 3L and 3M\n  quote: neurons in the high intensity subgroup exhibited a significant increase in spike counts\n    and a decrease in spike onset latency from early to late phases, while the remaining neurons\n    exhibited little change. This subset initially showed spike counts and onset latency\n    comparable to the rest of the population ... but diverged from week 2 to week 4\n  statistics:\n  - about: spike count, subgroup against remaining, week 0\n    test: two-sided Mann-Whitney U test\n    statistic: r < 0.01\n    p: 0.9699\n  - about: spike count, subgroup against remaining, week 1\n    test: two-sided Mann-Whitney U test\n    statistic: r = 0.08\n    p: 0.1076\n  - about: spike count, subgroup against remaining, week 2\n    test: two-sided Mann-Whitney U test\n    statistic: r = 0.14\n    p: 0.007\n  - about: spike count, subgroup against remaining, week 3\n    test: two-sided Mann-Whitney U test\n    statistic: r = 0.40\n    p: 3.13e-14\n  - about: spike count, subgroup against remaining, week 4\n    test: two-sided Mann-Whitney U test\n    statistic: r = 0.30\n    p: 1.16e-8\n  - about: onset latency, subgroup against remaining, week 0\n    test: two-sided Mann-Whitney U test\n    statistic: r < 0.01\n    p: 0.8767\n  - about: onset latency, subgroup against remaining, week 1\n    test: two-sided Mann-Whitney U test\n    statistic: r = 0.02\n    p: 0.6763\n  - about: onset latency, subgroup against remaining, week 2\n    test: two-sided Mann-Whitney U test\n    statistic: r = 0.10\n    p: 0.0442\n  - about: onset latency, subgroup against remaining, week 3\n    test: two-sided Mann-Whitney U test\n    statistic: r = 0.16\n    p: 0.0024\n  - about: onset latency, subgroup against remaining, week 4\n    test: two-sided Mann-Whitney U test\n    statistic: r = 0.14\n    p: 0.0059\n  depends_on:\n  - fig3j-subgroup-increase\n  criterion: Same groups and per-week tests as fig3j-subgroup-increase, on the OASIS-deconvolved\n    spike count and spike onset of each tracked unit (fig3jlmn_subset_analysis.m). The paper\n    reports no test for the within-group early-against-late change, so that part is read from\n    the same two-sided Mann-Whitney U on per-unit early and late means as in Fig. 3J. Reproduced\n    when, for both measures, weeks 0 and 1 show no subgroup difference and weeks 2, 3 and 4 show\n    one at p < 0.05 (more spikes, earlier onset in the subgroup); partially reproduced when that\n    holds for one measure or for at least two of weeks 2 to 4 in each.\n- id: fig3n-late-recruited\n  statement: Neurons recruited only in the last week had lower maximum dF/F and fewer deconvolved\n    spikes than the high-intensity subgroup in weeks 2 to 4, with similar onset time; they also had\n    lower fluorescence than all tracked neurons at week 0, and the enhanced subgroup in weeks 2\n    to 4 had higher dF/F, more spikes and shorter spike onset than tracked neurons at week 0.\n  source: Results, Longitudinal tracking of individual neurons reveals learning-sensitive\n    subpopulations, paragraph 4; Figure 3N\n  quote: Neurons recruited exclusively during the last week of training exhibited lower ΔF/F max\n    values (Kruskal-Wallis tests with Tukey-Kramer post-hoc correction, p = 3.09e-19; n wk0 = 23,\n    n wk2-4 = 57, n wk4 = 700) and fewer deconvolved spikes (p = 3.29e-17) than the\n    high-intensity subgroup during weeks 2–4 while activation onset time remained similar between\n    the two groups (p = 0.0633).\n  statistics:\n  - about: maximum dF/F, three groups\n    test: Kruskal-Wallis test with Tukey-Kramer post-hoc correction\n    p: 3.09e-19\n    n: 23 week-0, 57 weeks 2-4 subgroup, 700 week-4 newly recruited\n  - about: deconvolved spikes, three groups\n    test: Kruskal-Wallis test with Tukey-Kramer post-hoc correction\n    p: 3.29e-17\n  - about: onset time, newly recruited against subgroup weeks 2-4\n    test: Kruskal-Wallis test with Tukey-Kramer post-hoc correction\n    p: 0.0633\n  - about: fluorescence, newly recruited week 4 against tracked week 0\n    test: Tukey-Kramer post-hoc\n    p: 0.0349\n  - about: maximum dF/F, subgroup weeks 2-4 against tracked week 0\n    test: Tukey-Kramer post-hoc\n    p: 0.0114\n  - about: spike count, subgroup weeks 2-4 against tracked week 0\n    test: Tukey-Kramer post-hoc\n    p: 0.0059\n  - about: spike onset, subgroup weeks 2-4 against tracked week 0\n    test: Tukey-Kramer post-hoc\n    p: 0.003\n  depends_on:\n  - fig3j-subgroup-increase\n  criterion: As fig3jlmn_subset_analysis.m, three groups per measure (maximum dF/F, spike count,\n    spike onset) - group 2, the subgroup's per-unit mean over weeks 2 to 4; group 3, the values of\n    planar ROIs activated only in the last week; group 1, week 0 values. Kruskal-Wallis, then\n    Tukey-Kramer comparisons (MATLAB multcompare defaults). Group 1 is open, could change the\n    outcome - the legend says \"all longitudinally recruited neurons at week 0\" while the code\n    takes the subgroup's week 0 values (n wk0 = 23 is closer to the code's); readings are (a)\n    all tracked units at week 0 and (b) the subgroup at week 0. Reproduced when, under a\n    reading, group 3 is below group 2 in dF/F and spike count at p < 0.05, group 3 against group\n    2 in onset is not significant, group 3 is below group 1 in dF/F, and group 2 exceeds group 1\n    in dF/F and spike count and has earlier spike onset, all at p < 0.05. Partially reproduced\n    when the group 3 against group 2 parts hold but some week 0 comparison fails. The text also\n    says newly recruited neurons had \"shorter deconvolved spike onset (p = 0.479)\" than week 0,\n    which its own p does not support; that part is reported but not judged.\n- id: fig4-unit-counts\n  statement: Electrophysiology recorded 973 units in 6 animals (672 putative pyramidal, 301\n    interneurons); 484 were significantly modulated by the 700 ms train (311 pyramidal, 173\n    interneurons), with a bimodal spike-width distribution like the full population.\n  source: Results, Chronic electrophysiology confirms learning-driven strengthening of\n    neuromodulation, paragraphs 1, 3 and 4; Figure 4H\n  quote: Modulated units (n = 484; 311 pyramidal, 173 interneuron) showed a bimodal spike-width\n    distribution similar to the full recorded population (n = 973; 672 pyramidal, 301\n    interneuron) ( Fig. 4H ), confirming robust spike detection on both cell types.\n  expected:\n  - quantity: recorded units\n    value: 973\n    tolerance: 97.3\n  - quantity: recorded putative pyramidal units\n    value: 672\n    tolerance: 67.2\n  - quantity: recorded putative interneurons\n    value: 301\n    tolerance: 30.1\n  - quantity: modulated units\n    value: 484\n    tolerance: 48.4\n  - quantity: modulated putative pyramidal units\n    value: 311\n    tolerance: 31.1\n  - quantity: modulated putative interneurons\n    value: 173\n    tolerance: 17.3\n  criterion: As cell_type_histogram.py, units counted once per animal, session and unit (so a\n    neuron recorded in several sessions counts in each), trough-to-peak above 0 kept, pyramidal at\n    or above 0.45 ms. Modulated units are those with at least one modulated response under\n    filter_modulated with z-score below 100. Reproduced when all six counts are within\n    tolerance; partially reproduced when the totals (973 and 484) are within tolerance but a\n    cell-type split is not. Whether the dataset's units are per session or tracked across\n    sessions is the author's to establish; the criterion counts per session as the code does.\n- id: fig4d-waveform-separation\n  statement: Stimulation-evoked waveforms matched the same unit's non-stimulation waveforms and\n    stayed distinct from nearby units; within-unit distances in PC space were smaller than\n    between-unit distances.\n  source: Results, Chronic electrophysiology confirms learning-driven strengthening of\n    neuromodulation, paragraph 2; Figure 4D\n  quote: \"within-unit Euclidean distances in the PC space (between stimulation and non-stimulation\n    waveforms of the same unit; n = 243) are significantly smaller than the between-unit distances\n    (between stimulation waveforms of different nearby units; n = 801; p = 1.6e-31, r = 0.49)\"\n  statistics:\n  - test: two-sided Mann-Whitney U test\n    statistic: r = 0.49\n    p: 1.6e-31\n    n: 243 within-unit and 801 between-unit distances\n  criterion: As the Methods (Spike sorting during stimulation) describe, each waveform is the\n    vector of functional channels x 90 samples (3 ms), projected on the first 10 principal\n    components; within-unit distance = Euclidean distance between the centroids of a unit's\n    stimulation and non-stimulation spikes; between-unit distance = between the stimulation\n    centroids of two units within 240 um or no more than four contacts apart. Two-sided\n    Mann-Whitney U (legend). Reproduced when within-unit distances are smaller at p < 0.05; also\n    reported for 3, 5, 7, 15 and 20 PCs (Results). Blocked if the dataset does not hold\n    per-spike waveforms or a way to separate stimulation from non-stimulation spikes.\n- id: fig4g-modulated-count-mouse1\n  statement: In Mouse 1 at 4 uA, the number of modulated units per stimulation channel increased\n    moderately from the early to the late phase, while there was no significant group-level change\n    in modulated unit numbers.\n  source: Results, Chronic electrophysiology confirms learning-driven strengthening of\n    neuromodulation, paragraph 3; Figure 4G\n  quote: electrophysiological recordings detected only a moderate increase in modulated unit numbers\n    in some animals ( Fig. 4F, G , n early = 8, n late = 21, p = 0.044, r = 0.42) and no\n    significant group-level change, likely due to the sparser spatial sampling of electrophysiology.\n  statistics:\n  - about: Mouse 1, 4 uA, early against late\n    test: one-sided Mann-Whitney U test\n    statistic: r = 0.42\n    p: 0.044\n    n: 8 early and 21 late channel-session counts\n  criterion: As modulated_unit_count.py, for ICMS92 (Mouse 1) at 4 uA, the number of distinct units\n    with a modulated response (filter_modulated, z-score below 100) per session and stimulation\n    channel; one-sided Mann-Whitney U, early less than late. The increase is reproduced when p <\n    0.05. The group-level absence has no stated test; read as the same one-sided test on the\n    counts of all 6 animals pooled, at each of 4, 5 and 6 uA, at alpha 0.05, and holds when none\n    of the three is significant. Reproduced when both parts hold; partially reproduced when the\n    Mouse 1 increase holds and the group test is significant at one current only.\n- id: fig4i-pyramidal-modulation-increase\n  statement: Increases in modulation strength over training were driven by putative pyramidal\n    cells, at 4, 5 and 6 uA, while interneurons showed no significant change in modulation.\n  source: Results, Chronic electrophysiology confirms learning-driven strengthening of\n    neuromodulation, paragraph 4; Figure 4I\n  quote: Notably, increases in modulation strength and decreases in latency were driven primarily by\n    pyramidal cells (modulation strength 4 μA ... p = 2.6e-5, r = 0.25; 5 μA ... p = 5.3e-5, r =\n    0.22; 6 µA ... p = 2.0e-4, r = 0.23 ... whereas interneurons showed little significant change (\n    Fig. 4I–J , modulation strength 4 µA ... p = 0.39, r = 0.07; 5 µA ... p = 0.45, r = -0.05; 6\n    µA ... p = 0.24, r = 0.10\n  statistics:\n  - about: pyramidal modulation, 4 uA\n    test: two-sided Mann-Whitney U test\n    statistic: r = 0.25\n    p: 2.6e-5\n  - about: pyramidal modulation, 5 uA\n    test: two-sided Mann-Whitney U test\n    statistic: r = 0.22\n    p: 5.3e-5\n  - about: pyramidal modulation, 6 uA\n    test: two-sided Mann-Whitney U test\n    statistic: r = 0.23\n    p: 2.0e-4\n  - about: interneuron modulation, 4 uA\n    test: two-sided Mann-Whitney U test\n    statistic: r = 0.07\n    p: 0.39\n    n: 69 early and 254 late responses\n  - about: interneuron modulation, 5 uA\n    test: two-sided Mann-Whitney U test\n    statistic: r = -0.05\n    p: 0.45\n    n: 113 early and 180 late responses\n  - about: interneuron modulation, 6 uA\n    test: two-sided Mann-Whitney U test\n    statistic: r = 0.10\n    p: 0.24\n    n: 122 early and 86 late responses\n  criterion: As modulation_over_time.py, modulated responses (filter_modulated, z-score below 100)\n    split by cell type; per current, modulation scores of weeks 0 to 1 against weeks 2 to 4, all\n    animals pooled, two-sided Mann-Whitney U. Pyramidal increase holds when all three currents\n    give p < 0.05 with late higher. Interneuron absence is judged on the same test at alpha 0.05\n    and holds when no current is significant. Reproduced when both hold; partially reproduced\n    when the pyramidal increase holds at one or two currents, or holds at all three while an\n    interneuron current is significant.\n- id: fig4j-pyramidal-latency\n  statement: Time to maximum firing rate of putative pyramidal cells decreased from early to late\n    phases at 5 and 6 uA but not at 4 uA; in interneurons it did not change at 4 or 5 uA and\n    changed at 6 uA.\n  source: Results, Chronic electrophysiology confirms learning-driven strengthening of\n    neuromodulation, paragraph 4; Figure 4J\n  quote: latency 4 µA ... p = 0.32, r = -0.06; 5 µA ... p = 1.7e-3, r = -0.17; 6 µA ... p =\n    0.049, r = -0.12), whereas interneurons showed little significant change ( Fig. 4I–J ,\n    modulation strength 4 µA ... latency 4 µA ... p = 0.88, r = -0.01; 5 µA ... p = 0.31, r = 0.07;\n    6 µA ... p = 0.010, r = 0.21).\n  statistics:\n  - about: pyramidal latency, 4 uA\n    test: two-sided Mann-Whitney U test\n    statistic: r = -0.06\n    p: 0.32\n  - about: pyramidal latency, 5 uA\n    test: two-sided Mann-Whitney U test\n    statistic: r = -0.17\n    p: 1.7e-3\n  - about: pyramidal latency, 6 uA\n    test: two-sided Mann-Whitney U test\n    statistic: r = -0.12\n    p: 0.049\n  - about: interneuron latency, 4 uA\n    test: two-sided Mann-Whitney U test\n    statistic: r = -0.01\n    p: 0.88\n  - about: interneuron latency, 5 uA\n    test: two-sided Mann-Whitney U test\n    statistic: r = 0.07\n    p: 0.31\n  - about: interneuron latency, 6 uA\n    test: two-sided Mann-Whitney U test\n    statistic: r = 0.21\n    p: 0.01\n  criterion: Same responses and test as fig4i-pyramidal-modulation-increase, on time to maximum\n    firing rate (t_to_max_10ms_smoothed). Reproduced when pyramidal latency is lower late at 5\n    and 6 uA (p < 0.05) and not significant at 4 uA, and interneuron latency is not significant\n    at 4 and 5 uA. Partially reproduced when the pyramidal decrease holds at one of 5 and 6 uA.\n    The interneuron 6 uA result (r = 0.21, an increase) is reported but not judged.\n- id: figs3-modulation-at-threshold-stable\n  statement: When stimulation currents were set to session-specific detection thresholds, the\n    modulation score of modulated units stayed stable across training.\n  source: Results, Chronic electrophysiology confirms learning-driven strengthening of\n    neuromodulation, paragraph 3 (fig. S3D, not available)\n  quote: When stimulation currents were adjusted to session-specific detection thresholds, the\n    modulation score of these units remained stable across training (fig. S3D).\n  depends_on:\n  - fig2a-threshold-decrease\n  criterion: A claim of absence, judged on the test of the paper's code (fig_s3 plot_modulation_\n    at_threshold), since the supplement is not available. Each session's channel threshold rounded\n    to the nearest integer current, kept between 4 and 6 uA; the median z-score of modulated\n    responses (z-score below 100) at that channel and current per session, then the median over\n    sessions of each week, one value per animal, channel and week; one-sided Mann-Whitney U,\n    early less than late, at alpha 0.05. Reproduced when the test finds no increase; not\n    reproduced when it does.\n- id: fig5d-pl-identity-stable\n  statement: Over 80% of units kept their pulse-locked or non-pulse-locked identity at a given\n    stimulation contact as current increased from 4 to 6 uA.\n  source: Results, Millisecond pulse-locking dynamics differentiate learning-induced plasticity,\n    paragraph 2; Figure 5D\n  quote: Indeed, over 80% of units retained their PL and NPL identity at a given stimulation contact\n    as current amplitude increased ( Fig. 5D ).\n  expected:\n  - quantity: unit-channel pairs with responses at two or more currents\n    value: 729\n    tolerance: 72.9\n  criterion: As generate_figure5.py plot_pie, modulated responses (filter_modulated defaults) grouped\n    by animal, session, stimulation channel and unit, kept when at least two currents are present;\n    a pair is \"All PL\" or \"Not PL\" when it is pulse-locked at all or none of its currents.\n    Reproduced when the sum of those two fractions exceeds 0.80; partially reproduced between\n    0.70 and 0.80.\n- id: fig5e-pyramidal-fraction\n  statement: Putative pyramidal cells were more prevalent among pulse-locked units (76.2%) than\n    among non-pulse-locked units (49.8%).\n  source: Results, Millisecond pulse-locking dynamics differentiate learning-induced plasticity,\n    paragraph 2; Figure 5E\n  quote: Pyramidal cells are more prevalent among PL units than NPL units ( Fig. 5E , PL 76.2%,\n    NPL 49.8%; two-sided Fisher’s exact test; p = 1.6e-9)\n  statistics:\n  - test: two-sided Fisher's exact test\n    p: 1.6e-9\n  expected:\n  - quantity: pyramidal fraction among PL units\n    value: 76.2\n    tolerance: 7.62\n    unit: percent\n  - quantity: pyramidal fraction among NPL units\n    value: 49.8\n    tolerance: 4.98\n    unit: percent\n  criterion: A unit is pulse-locked at a current when pulse-locked at the majority of its\n    stimulation channels, and pulse-locked overall when pulse-locked at the majority of its\n    currents (Methods; generate_figure5.py plot_pyr_fraction, majority meaning more than half),\n    per animal, session and unit, from modulated responses. Two-sided Fisher's exact test on\n    the 2 x 2 table of PL status by cell type. Reproduced when p < 0.05 with the PL fraction\n    higher and both fractions within tolerance; partially reproduced when the test holds but a\n    fraction is outside tolerance.\n- id: fig5-pl-npl-counts\n  statement: The longitudinal comparison used 265 pulse-locked and 219 non-pulse-locked units across\n    6 animals.\n  source: Results, Millisecond pulse-locking dynamics differentiate learning-induced plasticity,\n    paragraph 3\n  quote: Importantly, PL and NPL responses exhibited distinct longitudinal changes during behavioral\n    learning (n = 265 PL and 219 NPL units across 6 animals).\n  expected:\n  - quantity: pulse-locked units\n    value: 265\n    tolerance: 26.5\n  - quantity: non-pulse-locked units\n    value: 219\n    tolerance: 21.9\n  criterion: 265 + 219 = 484, the modulated units of fig4-unit-counts, so each unit carries one\n    label. The unit-level label is open; readings are (a) the two-step majority rule of\n    fig5e-pyramidal-fraction, and (b) PL when any of the unit's modulated responses is\n    pulse-locked. Reproduced when, under a reading, both counts are within tolerance.\n  depends_on:\n  - fig4-unit-counts\n- id: fig5fg-pl-modulation-latency\n  statement: Pulse-locked responses increased their modulation from early to late phases at all\n    three currents and decreased their time to maximum firing rate at 5 and 6 uA but not 4 uA.\n  source: Results, Millisecond pulse-locking dynamics differentiate learning-induced plasticity,\n    paragraph 3; Figure 5F and 5G\n  quote: Specifically, PL modulation increased from early to late phases across all current\n    amplitudes (4 μA ... p = 3.3e-5, r = 0.23; 5 µA ... p = 2.4e-4, r = 0.20; 6 µA ... p =\n    6.4e-5, r = 0.26), and latency decreased significantly at 5 and 6 μA (4 µA ... p = 0.35, r =\n    -0.05; 5 µA ... p = 5.9e-3, r = -0.15; 6 µA ... p = 0.040, r = -0.14).\n  statistics:\n  - about: PL modulation, 4 uA\n    test: two-sided Mann-Whitney U test\n    statistic: r = 0.23\n    p: 3.3e-5\n    n: 136 early and 469 late responses\n  - about: PL modulation, 5 uA\n    test: two-sided Mann-Whitney U test\n    statistic: r = 0.20\n    p: 2.4e-4\n    n: 188 early and 285 late responses\n  - about: PL modulation, 6 uA\n    test: two-sided Mann-Whitney U test\n    statistic: r = 0.26\n    p: 6.4e-5\n    n: 179 early and 135 late responses\n  - about: PL latency, 4 uA\n    test: two-sided Mann-Whitney U test\n    statistic: r = -0.05\n    p: 0.35\n  - about: PL latency, 5 uA\n    test: two-sided Mann-Whitney U test\n    statistic: r = -0.15\n    p: 5.9e-3\n  - about: PL latency, 6 uA\n    test: two-sided Mann-Whitney U test\n    statistic: r = -0.14\n    p: 0.04\n  criterion: As generate_figure5.py plot_pl_features, pulse-locked modulated responses (filter_pl,\n    z-score below 50); per current, weeks 0 to 1 against 2 to 4, all animals pooled, two-sided\n    Mann-Whitney U on z-score and on t_to_max_10ms_smoothed. Reproduced when modulation is\n    higher late at all three currents and latency lower late at 5 and 6 uA (p < 0.05), with 4 uA\n    latency not significant; partially reproduced when modulation increases at one or two\n    currents, or latency decreases at only one of 5 and 6 uA. The response counts per current\n    are reported against the paper's.\n- id: fig5h-pl-spike-probability\n  statement: Peak spike probability within the 10 ms interpulse interval of pulse-locked responses\n    increased over time at 5 and 6 uA, not at 4 uA.\n  source: Results, Millisecond pulse-locking dynamics differentiate learning-induced plasticity,\n    paragraph 3; Figure 5H\n  quote: At the finer 10-ms interpulse scale, PL responses also showed increased peak spike\n    probability over time at 5 and 6 μA ( Fig. 5H, p = 0.22, r = 0.07; 5 µA ... p = 0.028, r =\n    0.12; 6 µA ... p = 0.010, r = 0.17).\n  statistics:\n  - about: 4 uA\n    test: two-sided Mann-Whitney U test\n    statistic: r = 0.07\n    p: 0.22\n  - about: 5 uA\n    test: two-sided Mann-Whitney U test\n    statistic: r = 0.12\n    p: 0.028\n  - about: 6 uA\n    test: two-sided Mann-Whitney U test\n    statistic: r = 0.17\n    p: 0.01\n  criterion: Same responses and test as fig5fg-pl-modulation-latency, on max_spike_prob (the\n    maximum of the bootstrap-mean interpulse spike-probability curve, header). Reproduced when 5\n    and 6 uA give p < 0.05 with late higher; partially reproduced when one does.\n- id: figs4-npl-no-change\n  statement: Non-pulse-locked responses showed no significant change in modulation or time to\n    maximum firing rate from early to late phases.\n  source: Results, Millisecond pulse-locking dynamics differentiate learning-induced plasticity,\n    paragraph 3 (fig. S4D, E, not available)\n  quote: At the coarse 700-ms train level, increases in modulation strength and decreases in latency\n    were driven exclusively by PL responses ( Fig. 5F, G ), whereas NPL responses showed no\n    significant changes (fig. S4D, E).\n  criterion: A claim of absence, judged on the test of the paper's code (fig_s4 plot_npl_metrics),\n    since the supplement is not available. Non-pulse-locked modulated responses (filter_npl,\n    z-score below 50); per current 4, 5 and 6 uA, weeks 0 to 1 against 2 to 4, two-sided\n    Mann-Whitney U on z-score and on t_to_max_10ms_smoothed, at alpha 0.05. Reproduced when none\n    of the six tests is significant; not reproduced when any is. Effect sizes reported either\n    way.\n- id: figs4-conduction-velocity\n  statement: Spike latency of pulse-locked responses increased linearly with distance from the\n    stimulation site, giving conduction velocities of 0.2 to 0.27 m/s, while latency jitter did not\n    vary with distance.\n  source: Results, Millisecond pulse-locking dynamics differentiate learning-induced plasticity,\n    paragraph 2 (fig. S4B, C, not available)\n  quote: Supporting these classifications, spike latency of PL responses increased linearly with\n    distance from the stimulation site, consistent with action potential propagation along axons\n    (fig. S4B). Linear fits to the monotonically increasing segment yielded conduction velocities\n    of 0.2 – 0.27 m/s\n  expected:\n    quantity: conduction velocity range over currents\n    value: 0.235\n    tolerance: 0.062\n    unit: m/s\n  criterion: The range rule applies, so the claim holds for velocities within 0.18 to 0.297 m/s\n    (the range widened by 10% of each bound); the expected value is the range's centre with that\n    span. The paper's latency is the bootstrap mean latency of the interpulse spike-probability\n    curve (pulse_locked_response_metrics.py) and its jitter the bootstrap SD; distance is from\n    the unit's estimated location to the stimulation contact. The \"monotonically increasing\n    segment\" (fig_s4 plot_latency_jitter, not read in full here, holds the binning and segment\n    choice the author should follow) is open beyond the code. Reproduced when, at each of 4, 5\n    and 6 uA, the slope of a linear fit of latency on distance over that segment is positive\n    and gives a velocity in range, and a linear fit of jitter on distance has a slope not\n    different from 0 at p < 0.05.\n- id: fig5-tracked-units\n  statement: UnitMatch tracking yielded 34 units spanning early and late phases across 6 animals,\n    with between-session waveform distances of tracked units 6.8-fold smaller than distances to\n    nearby non-matched units; in these units PL modulation increased over training while NPL\n    modulation did not, and PL time to maximum firing rate decreased.\n  source: Results, Millisecond pulse-locking dynamics differentiate learning-induced plasticity,\n    paragraph 5; Figure 5I to 5M (fig. S8, not available)\n  quote: This yielded 34 tracked units spanning both early and late learning phases across 6\n    animals (fig. S8A, B). ... Waveform distances between sessions of the same tracked unit were\n    6.8-fold smaller than distances to nearby (within 2 channels) non-matched units in the same\n    session (p = 6.6e-83, Mann-Whitney U; fig. S8C) ... Analyses of the 34 tracked units support\n    the main findings PL modulation increased significantly over training while NPL modulation\n    did not, and PL time to maximum firing rate decreased (fig. S8D).\n  statistics:\n  - about: within-track against nearby non-matched waveform distances\n    test: Mann-Whitney U test\n    p: 6.6e-83\n  expected:\n  - quantity: tracked units spanning early and late phases\n    value: 34\n    tolerance: 3.4\n  - quantity: ratio of non-matched to within-track waveform distance\n    value: 6.8\n    tolerance: 0.68\n  criterion: Tracks as in the Methods (Unit tracking via electrophysiological recording)\n    with UnitMatchPy - match probability above 0.75 linked by connected components, best match\n    kept per session, consecutive-session probability at least 0.5, at least 3 sessions, tracks\n    with median pairwise waveform distance above 3 times the global median dropped, sessions\n    above 5 times the track median dropped, kept when spanning weeks 0 to 1 and 2 to 4. If the\n    dataset gives cross-session unit identities, those are used instead and the difference is\n    reported. Distance comparison as fig_s8 plot_panel_c, one-sided Mann-Whitney U (within less\n    than cross). Modulation and latency trends as fig_s8 plot_panel_d - PL and NPL filtered\n    responses of tracked units, per current, two-sided Mann-Whitney U early against late.\n    Reproduced when the count and ratio are within tolerance, the distance test gives p < 0.05,\n    PL modulation increases at p < 0.05 at one current or more, NPL modulation is significant at\n    none, and PL latency decreases at one current or more; partially reproduced when tracks and\n    distances hold but a trend part fails.\n- id: figs5-movement-onset\n  statement: Wheel-movement onset, in 5 animals with reliable encoder recordings, decreased with\n    training; median onsets were 122 ms in the fastest animal (Mouse 1), 135 ms across all hit\n    trials and 129 ms in the late phase.\n  source: Results, Millisecond pulse-locking dynamics differentiate learning-induced plasticity,\n    paragraph 4 (fig. S5A to D, not available)\n  quote: We evaluated three candidate cutoffs from stimulation onset the median wheel-movement\n    onset in the fastest animal (Mouse 1, 122 ms; fig. S5D), the median onset across all hit\n    trials (135 ms), and the median onset during the late training phase (129 ms), which was\n    faster than in the early phase (fig. S5D).\n  expected:\n  - quantity: median movement onset, Mouse 1\n    value: 122\n    tolerance: 12.2\n    unit: ms\n  - quantity: median movement onset, all hit trials\n    value: 135\n    tolerance: 13.5\n    unit: ms\n  - quantity: median movement onset, late phase\n    value: 129\n    tolerance: 12.9\n    unit: ms\n  criterion: Movement onset per hit trial from the rotary encoder; the onset definition is in the\n    code that built the onset table (fig_s5 build_movement_onset_df reads precomputed source\n    files) and not in the Methods, so it is open; the author takes it from the dandiset's own\n    movement annotation if there is one and otherwise names the readings. Early against late as\n    fig_s5 generate_onset_early_late_panel, two-sided Mann-Whitney U on trial onsets, weeks 0 to\n    1 against 2 to 4. Reproduced when the three medians are within tolerance and late is faster\n    at p < 0.05; partially reproduced when late is faster but a median falls outside tolerance.\n- id: figs5-120ms-window\n  statement: Restricting the analysis to the first 120 ms after stimulation onset, before movement,\n    gave results consistent with the 700 ms window for the distinct longitudinal changes of PL and\n    NPL cells.\n  source: Results, Millisecond pulse-locking dynamics differentiate learning-induced plasticity,\n    paragraph 4 (fig. S5E to H, not available)\n  quote: This analysis yielded results consistent with those obtained using the longer 700 ms window\n    (fig. S5E-H), supporting that the distinct longitudinal changes of PL and NPL cells arise from\n    responses to ICMS rather than movement-related activity.\n  depends_on:\n  - fig5fg-pl-modulation-latency\n  - figs4-npl-no-change\n  criterion: As fig_s5 (raw_df_sym120ms), responses recomputed with a symmetric window, baseline\n    -120 to 0 ms and stimulation 0 to 120 ms (window_config.py symmetric_120ms), modulated, PL\n    and NPL filters with z-score below 100; per current, two-sided Mann-Whitney U early against\n    late on z-score for PL and NPL. \"Consistent\" is read as - PL modulation higher late at p <\n    0.05 at 2 or more of the 3 currents, and NPL modulation not significant at 2 or more.\n    Reproduced when both hold; partially reproduced when one does.\n- id: figs6-imaging-short-window\n  statement: Using only the first five imaging frames after ICMS onset, both recruitment of tracked\n    neurons and the response amplitude of the increasing subset rose significantly from early to\n    late training.\n  source: Results, Millisecond pulse-locking dynamics differentiate learning-induced plasticity,\n    paragraph 4 (fig. S6, not available)\n  quote: Both recruitment of tracked neurons and the response amplitude of the increasing subset (\n    Fig. 3J ) increased significantly from early to late training (fig. S6B, C), consistent with\n    the findings from the full response window.\n  depends_on:\n  - fig3j-subgroup-increase\n  criterion: Planar ROIs whose response crosses the activation threshold after the first five\n    frames following ICMS onset (about 132 to 165 ms) are excluded (Results). The supplement is\n    not available and the code that builds these data (processing/imaging/movement_control/\n    export_*.m) only exports them, so the measures are read as - recruitment = number of tracked\n    ROIs activated per session and channel; amplitude = maximum dF/F of the Fig. 3J subgroup in\n    the first five frames. Both compared early against late by two-sided Mann-Whitney U, as the\n    paper's other imaging tests. Reproduced when both increase at p < 0.05; partially reproduced\n    when one does.\n- id: figs7-control-no-change\n  statement: In control animals without behavioural learning, neither PL nor NPL cells showed\n    significant changes in modulation, time to maximum firing rate or peak spike probability.\n  source: Results, Millisecond pulse-locking dynamics differentiate learning-induced plasticity,\n    paragraph 4 (fig. S7, not available)\n  quote: Furthermore, in the control group without behavioral learning, neither PL nor NPL cells\n    showed significant changes in any of these metrics (fig. S7), further supporting that the\n    longitudinal changes observed in the learning group are associated with behavioral learning.\n  criterion: A claim of absence, judged on the test of the paper's code (fig_s7), since the\n    supplement is not available. Control mice at 5 uA; responses with modulated, p < 0.05,\n    z-score > 0, week below 5, baseline at least 0.5 Hz, more than 5 trials and more than 15\n    spikes (the code's control threshold, lower than the 50 of the Methods; 50 is shown as a\n    variant). Weeks from each control animal's first session. Two-sided Mann-Whitney U, weeks 0\n    to 1 against 2 to 4, on PL z-score, NPL z-score, PL and NPL time to maximum firing rate, and\n    PL peak spike probability, at alpha 0.05. Reproduced when none of the five is significant;\n    not reproduced when any is. Blocked if the dandiset holds no control mice.\n- id: fig6c-kl-divergence\n  statement: Hit-miss separation of per-trial spike changes, measured by KL divergence, increased\n    over time for both PL and NPL responses, and NPL responses separated hit from miss trials more\n    than PL responses in both early and late phases.\n  source: Results, Differential behavioral correlates of pulse-locked and non-pulse-locked neurons,\n    paragraph 2; Figure 6B and 6C\n  quote: While both PL and NPL separation between hit and miss trials increased over time (PL p FDR\n    = 7.2e-26, r = 0.18; NPL p FDR = 6.1e-3, r = 0.05), NPL responses showed greater separation\n    between hit and miss trials than PL responses in both early (p FDR = 7.3e-116, r = 1.00) and\n    late (p FDR = 7.3e-116, r = 0.34) phases.\n  statistics:\n  - about: PL, early against late\n    test: two-sided Mann-Whitney U test\n    statistic: r = 0.18\n    p: 7.2e-26\n    corrected: FDR (Benjamini-Hochberg)\n  - about: NPL, early against late\n    test: two-sided Mann-Whitney U test\n    statistic: r = 0.05\n    p: 6.1e-3\n    corrected: FDR (Benjamini-Hochberg)\n  - about: NPL against PL, early\n    test: two-sided Mann-Whitney U test\n    statistic: r = 1.00\n    p: 7.3e-116\n    corrected: FDR (Benjamini-Hochberg)\n  - about: NPL against PL, late\n    test: two-sided Mann-Whitney U test\n    statistic: r = 0.34\n    p: 7.3e-116\n    corrected: FDR (Benjamini-Hochberg)\n  criterion: Per trial, delta spikes = spikes in the 700 ms train minus spikes in the preceding\n    700 ms (Results), for every trial of every modulated response, labelled by its response's PL\n    status and by outcome (hit or miss). As hit_miss_histograms.py, per week 0 to 4 and per PL\n    class, hit and miss values winsorized at 1% on each side; 1000 bootstrap draws (with\n    replacement) of 40% of the smaller group's size from each; KL divergence (scipy entropy) of\n    hit from miss histograms on 25 bins over -30 to 50, with 1e-8 added. Early = draws from weeks\n    0 and 1 pooled, late = weeks 2 to 4. Four two-sided Mann-Whitney U tests on the bootstrap\n    values (PL early against late, NPL early against late, PL against NPL early and late), FDR\n    Benjamini-Hochberg. The p-values depend on the number of draws, so the outcome rests on\n    direction and significance. Reproduced when PL and NPL each increase and NPL exceeds PL in\n    both phases, all at corrected p < 0.05; partially reproduced when NPL exceeds PL in both\n    phases but an increase fails. The per-trial table (df_merged.pkl) was built outside the\n    repository; which trials it holds (all currents 4 to 6 uA, modulated responses) is taken as\n    the paper's text implies.\n- id: fig6d-hit-miss-divergence-onset\n  statement: PL responses showed no significant hit-miss divergence in firing rate at any time,\n    while NPL responses diverged from 65 ms after ICMS onset in the early phase and from 35 ms in\n    the late phase, both before movement onset.\n  source: Results, Differential behavioral correlates of pulse-locked and non-pulse-locked neurons,\n    paragraph 3; Figure 6D\n  quote: Despite an increase in KL divergence from early to late learning, PL responses did not show\n    any significant hit-miss divergence at any time point. In contrast, NPL responses diverged\n    significantly beginning at 65 ms post-ICMS onset during the early period. With training, the\n    onset of divergence in NPL neurons shifted earlier to 35 ms.\n  expected:\n  - quantity: NPL divergence onset, early phase\n    value: 65\n    tolerance: 6.5\n    unit: ms\n  - quantity: NPL divergence onset, late phase\n    value: 35\n    tolerance: 3.5\n    unit: ms\n  criterion: As hit_miss_psth.py, per group (PL or NPL, early or late) a hit and a miss array of\n    firing-rate traces, one row per unit; per time bin a two-sided Mann-Whitney U, signed -log10\n    p, clusters of contiguous bins with |value| > -log10(0.05), cluster mass = sum; 1000\n    label permutations of rows (seed 42) give the null of the maximum cluster mass; clusters with\n    p < 0.05 are significant and the onset is the start bin centre of a significant cluster. The\n    traces were precomputed (hit_miss_psth.npz) outside the repository, so the bin width and\n    smoothing are open; the legend says \"Trial median responses\". Readings are 10 ms bins\n    smoothed with a Gaussian of sigma 20 ms (the code's train-response rate) and 2 ms bins\n    smoothed with sigma 5 ms (the code's fine rate), each the median over a unit's hit or miss\n    trials. The code takes the last significant cluster's onset; the first is also reported.\n    The tolerances on 65 and 35 ms are 10%, finer than either bin width allows, so an onset\n    within one bin width of the paper's value also counts. Reproduced when, under a reading, PL\n    has no significant cluster in either phase, NPL has one in both, and the onsets match;\n    partially reproduced when the PL-against-NPL pattern holds but an onset does not match.\n- id: fig6f-population-coupling\n  statement: PL population coupling increased from early to late phases while NPL coupling stayed\n    stable, and NPL units had higher population coupling than PL units in both phases.\n  source: Results, Differential behavioral correlates of pulse-locked and non-pulse-locked neurons,\n    paragraph 4; Figure 6F\n  quote: PL coupling increased over time ( Fig. 6F , n early = 494, n late = 899, p FDR = 1.95e-6,\n    r = 0.16) while NPL coupling remained stable (n early = 263, n late = 553, p FDR = 0.33, r =\n    -0.04). ... In both early and late learning phases, NPL units exhibited significantly higher\n    population coupling than PL units (early p FDR = 3.4e-25, r = 0.46; late p FDR = 1.7e-22, r =\n    0.31)\n  statistics:\n  - about: PL, early against late\n    test: two-sided Mann-Whitney U test\n    statistic: r = 0.16\n    p: 1.95e-6\n    corrected: FDR (Benjamini-Hochberg)\n    n: 494 early and 899 late\n  - about: NPL, early against late\n    test: two-sided Mann-Whitney U test\n    statistic: r = -0.04\n    p: 0.33\n    corrected: FDR (Benjamini-Hochberg)\n    n: 263 early and 553 late\n  - about: NPL against PL, early\n    test: two-sided Mann-Whitney U test\n    statistic: r = 0.46\n    p: 3.4e-25\n    corrected: FDR (Benjamini-Hochberg)\n  - about: NPL against PL, late\n    test: two-sided Mann-Whitney U test\n    statistic: r = 0.31\n    p: 1.7e-22\n    corrected: FDR (Benjamini-Hochberg)\n  criterion: Population coupling as the Methods (Population coupling) - per stimulation condition,\n    spikes within stimulation trains concatenated; population rate of all other modulated units\n    in 1 ms bins, Gaussian sigma 10 ms, mean-centred; coupling = spike-triggered population rate\n    at zero lag; normalized by the median of 200 absolute circular-shift values; units with\n    fewer than 50 stimulation spikes excluded. As pop_coupling.py, PL and NPL values from 4, 5\n    and 6 uA pooled, a session early when its week is below 2, all 6 animals; four two-sided\n    Mann-Whitney U tests with FDR Benjamini-Hochberg. Reproduced when PL increases (corrected p\n    < 0.05), NPL early against late is not significant at corrected alpha 0.05, and NPL exceeds\n    PL in both phases; partially reproduced when the NPL-over-PL difference holds in both phases\n    but one of the longitudinal parts fails.\n- id: figs9-coupling-robust-and-control\n  statement: The higher population coupling of NPL than PL units held within the 120 ms pre-motion\n    window and was absent in control animals without behavioural learning.\n  source: Results, Differential behavioral correlates of pulse-locked and non-pulse-locked neurons,\n    paragraph 4 (fig. S9B, C, not available)\n  quote: This difference remained robust when computed within the 120 ms pre-motion time window\n    (fig. S9B) and was absent in control animals without behavioral learning (fig. S9C)\n  depends_on:\n  - fig6f-population-coupling\n  criterion: As fig_s9, coupling from the first 120 ms of each train for the behavioural mice and\n    from the full train for the control mice (Methods), with the tests of fig6f-population-\n    coupling. Holds for the 120 ms window when NPL exceeds PL in both phases at corrected p <\n    0.05. The control part is a claim of absence, judged on the same tests in the controls at\n    corrected alpha 0.05 (NPL against PL in each phase not significant). Reproduced when both\n    parts hold; partially reproduced when one does; blocked in its control part if the dandiset\n    holds no control mice.\n"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
python tools/claims_check.py claims/001868/10.64898-2026.06.05.730421.yaml paper/10.64898-2026.06.05.730421.txt
```

Result: not kept, because it reads the paper's text.

**Agent**

Find every plain scalar line with ": " inside values.

**Agent calls Bash**

```bash
cd claims/001868 && grep -nE '^\s+[^ "#-][^:]*: .*: ' *.yaml | head; grep -nE '^\s{4,}[^ ].*: ' *.yaml | grep -vE '^\s*[0-9]+:\s+(-\s)?[a-z_]+: ' | head -30
```

```
172:    0.043, r = 0.28; 5 µA: n early = 20, n late = 35, p = 0.015, r = 0.33; 6 µA: n early = 22, n
171:    late learning phase than in the early phase ( Fig. 2C , 4 µA: n early = 13, n late = 41, p =
172:    0.043, r = 0.28; 5 µA: n early = 20, n late = 35, p = 0.015, r = 0.33; 6 µA: n early = 22, n
250:    remained stable across learning phases (n early = 32, n late = 69; density: p = 0.511, r =
251:    0.07; total number: p = 0.253, r = 0.11).
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001868/10.64898-2026.06.05.730421.yaml",
 "old_string": "  quote: Notably, when the stimulation current was adjusted to the behavioral detection threshold\n    for each session ( Fig. 2F, G ), both the activation density and number of activated neurons\n    remained stable across learning phases (n early = 32, n late = 69; density: p = 0.511, r =\n    0.07; total number: p = 0.253, r = 0.11).",
 "new_string": "  quote: \"Notably, when the stimulation current was adjusted to the behavioral detection threshold\n    for each session ( Fig. 2F, G ), both the activation density and number of activated neurons\n    remained stable across learning phases (n early = 32, n late = 69; density: p = 0.511, r =\n    0.07; total number: p = 0.253, r = 0.11).\""
}
```

```
The file claims/001868/10.64898-2026.06.05.730421.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd  && python tools/claims_check.py claims/001868/10.64898-2026.06.05.730421.yaml paper/10.64898-2026.06.05.730421.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  && python - <<'EOF'
import re
p='claims/001868/10.64898-2026.06.05.730421.yaml'
s=open(p).read()
reps=[
("""  quote: Pyramidal cells are more prevalent among PL units than NPL units ( Fig. 5E , PL 76.2%,
    NPL 49.8%; two-sided Fisher’s exact test; p = 1.6e-9)""",
"""  quote: "Pyramidal cells are more prevalent among PL units than NPL units ( Fig. 5E , PL: 76.2%,
    NPL: 49.8%; two-sided Fisher’s exact test; p = 1.6e-9)\""""),
("""    session (p = 6.6e-83, Mann-Whitney U; fig. S8C) ... Analyses of the 34 tracked units support
    the main findings PL modulation increased significantly over training while NPL modulation
    did not, and PL time to maximum firing rate decreased (fig. S8D).""",
"""    session (p = 6.6e-83, Mann-Whitney U; fig. S8C) ... Analyses of the 34 tracked units support
    the main findings ... PL modulation increased significantly over training while NPL modulation
    did not, and PL time to maximum firing rate decreased (fig. S8D)."""),
("""  quote: We evaluated three candidate cutoffs from stimulation onset the median wheel-movement""",
"""  quote: We evaluated three candidate cutoffs from stimulation onset ... the median wheel-movement"""),
("""    over time (PL p FDR
    = 7.2e-26, r = 0.18; NPL p FDR = 6.1e-3, r = 0.05)""","""    over time (PL ... p FDR
    = 7.2e-26, r = 0.18; NPL ... p FDR = 6.1e-3, r = 0.05)"""),
("""    -0.04). ... In both early and late learning phases, NPL units exhibited significantly higher
    population coupling than PL units (early p FDR = 3.4e-25, r = 0.46; late p FDR = 1.7e-22, r =
    0.31)""","""    -0.04). ... In both early and late learning phases, NPL units exhibited significantly higher
    population coupling than PL units (early ... p FDR = 3.4e-25, r = 0.46; late ... p FDR =
    1.7e-22, r = 0.31)"""),
]
for a,b in reps:
    assert a in s, a[:60]
    s=s.replace(a,b)
open(p,'w').write(s)
EOF
grep -n "over time (PL" claims/001868/*.yaml; python tools/claims_check.py claims/001868/10.64898-2026.06.05.730421.yaml paper/10.64898-2026.06.05.730421.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  && python - <<'EOF'
p='claims/001868/10.64898-2026.06.05.730421.yaml'
s=open(p).read()
reps=[
("""  quote: Pyramidal cells are more prevalent among PL units than NPL units ( Fig. 5E , PL 76.2%,
    NPL 49.8%; two-sided Fisher’s exact test; p = 1.6e-9)""",
"""  quote: "Pyramidal cells are more prevalent among PL units than NPL units ( Fig. 5E , PL: 76.2%,
    NPL: 49.8%; two-sided Fisher’s exact test; p = 1.6e-9)\""""),
("""support
    the main findings PL modulation""","""support
    the main findings ... PL modulation"""),
("""stimulation onset the median wheel-movement""","""stimulation onset ... the median wheel-movement"""),
("""increased over time (PL p FDR
    = 7.2e-26, r = 0.18; NPL p FDR""","""increased over time (PL ...
    p FDR = 7.2e-26, r = 0.18; NPL ... p FDR"""),
("""population coupling than PL units (early p FDR = 3.4e-25, r = 0.46; late p FDR = 1.7e-22, r =
    0.31)""","""population coupling than PL units (early ... p FDR = 3.4e-25, r = 0.46; late ... p FDR =
    1.7e-22, r = 0.31)"""),
]
for a,b in reps:
    assert a in s, a[:60]
    s=s.replace(a,b)
open(p,'w').write(s)
EOF
python tools/claims_check.py claims/001868/10.64898-2026.06.05.730421.yaml paper/10.64898-2026.06.05.730421.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  && grep -n "—\|rather" claims/001868/*.yaml; grep -n "2.0e-4" paper/*.txt | cut -c1-80
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -n 963,968p claims/001868/*.yaml
```

```
source: Results, Millisecond pulse-locking dynamics differentiate learning-induced plasticity,
    paragraph 4 (fig. S5E to H, not available)
  quote: This analysis yielded results consistent with those obtained using the longer 700 ms window
    (fig. S5E-H), supporting that the distinct longitudinal changes of PL and NPL cells arise from
    responses to ICMS rather than movement-related activity.
  depends_on:
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001868/10.64898-2026.06.05.730421.yaml",
 "old_string": "    (fig. S5E-H), supporting that the distinct longitudinal changes of PL and NPL cells arise from\n    responses to ICMS rather than movement-related activity.",
 "new_string": "    (fig. S5E-H), supporting that the distinct longitudinal changes of PL and NPL cells arise from\n    responses to ICMS"
}
```

```
The file claims/001868/10.64898-2026.06.05.730421.yaml has been updated successfully.
```

**Agent calls Bash**

```bash
python tools/claims_check.py claims/001868/10.64898-2026.06.05.730421.yaml paper/10.64898-2026.06.05.730421.txt; python -c "
import yaml;d=yaml.safe_load(open('claims/001868/10.64898-2026.06.05.730421.yaml'))
c=d['claims'];print(len(c),sum('quote' in x for x in c),sum('statistics' in x for x in c),sum('criterion' in x for x in c),sum('expected' in x for x in c))"; git status --short
```

Result: not kept, because it reads the paper's text.

**Agent**

Before finishing, I'll read the conduction-velocity code that the criterion currently calls "not read in full", so that detail is settled from the code and not left open.

**Agent calls Bash**

```bash
sed -n 45,160p $TMPDIR/icms-activation-plasticity/python/fig_s4/generate_figure.py
```

```
def plot_latency_jitter(raw_df):
    print('Latency and jitter vs stim distance...')
    df = filter_modulated(raw_df, max_z_score=100).copy()
    df['distance_from_stim'] = abs(df['stim_ch_depth_um'] - df['unit_depth_um'])

    X = pd.DataFrame({
        'stim_current': df['stim_current'],
        'distance_from_stim': df['distance_from_stim'],
        'jitter': df['jitter'],
        'latency': df['latency'],
    })
    y = df['is_pulse_locked'].astype(int)
    X = X.dropna()
    y = y.loc[X.index]

    bin_edges = np.arange(60, 800 + 120, 120)
    bin_labels = [f'{s}\u2013{e}' for s, e in zip(bin_edges[:-1], bin_edges[1:])]
    bin_centers = [(s + e) / 2 for s, e in zip(bin_edges[:-1], bin_edges[1:])]
    label_to_center = dict(zip(bin_labels, bin_centers))

[... 97 more lines not kept]
```

**Agent calls Bash**

```bash
python - <<'EOF'
p='claims/001868/10.64898-2026.06.05.730421.yaml'
s=open(p).read()
i=s.index("  criterion: The range rule applies, so the claim holds for velocities")
j=s.index("- id: fig5-tracked-units")
new="""  criterion: The range rule applies, so the claim holds for velocities within 0.18 to 0.297 m/s
    (the range widened by 10% of each bound); the expected value is the range's centre with that
    span. As fig_s4 plot_latency_jitter, pulse-locked modulated responses (z-score below 100) per
    current; distance = |stimulation contact depth - unit depth| in um; latency = the response's
    interpulse spike latency (bootstrap mean of the peak time of the spike-probability curve,
    pulse_locked_response_metrics.py) and jitter its trial-to-trial spread (the table's jitter
    column, built outside the repository; read as the bootstrap SD of latency, with its square as a
    variant since the code labels the axis ms^2). The "monotonically increasing segment" is the
    code's 120 to 840 um range - responses there binned in 120 um bins (edges 60, 180, ..., 780),
    median latency per bin, OLS of bin medians on bin centres, velocity = 1e-3 / slope m/s
    (slope in ms/um). Reproduced when the velocity at each of 4, 5 and 6 uA is within range and
    an OLS of jitter on distance over all PL responses has a slope not different from 0 at p <
    0.05; partially reproduced when the velocities hold at one or two currents, or all hold but
    the jitter slope is significant.
"""
s=s[:i]+new+s[j:]
open(p,'w').write(s)
EOF
python tools/claims_check.py claims/001868/10.64898-2026.06.05.730421.yaml paper/10.64898-2026.06.05.730421.txt; grep -c "rather\|—" claims/001868/*.yaml
```

Result: not kept, because it reads the paper's text.

**Agent**

I wrote `claims/001868/10.64898-2026.06.05.730421.yaml`. Nothing is committed.

**Text read:** the bioRxiv preprint, version 1, from its JATS XML. It has the main text, the legends of Figures 1 to 7 and the Methods. There is no PDF.

**Missing from the paper text:** the supplement (figs. S1 to S9 and their legends). Its "Supporting information" section is empty. I went ahead because the main findings rest on Figures 2 to 6, which are in the text. Ten claims rest on supplementary figures (S2, S3D, S4, S5, S6, S7, S8, S9). Each quotes the main-text sentence that states the finding and takes its method from the paper's code for that figure; the figures themselves could not be read.

**Code read:** github.com/XieLuanLab/icms-activation-plasticity at commit d1922d16 (Zenodo 10.5281/zenodo.19561006). It holds the Python figure scripts for the electrophysiology, the MATLAB scripts for the imaging and the upstream processing pipeline. It settled most method details the Methods leave open: how weeks are numbered, the unit filters, the pulse-locking test and its null, the modulation score, the psignifit settings, the KL bootstrap, the cluster test and population coupling.

**Claims:** 36. All 36 have quotes and criteria, 18 record statistics and 12 have expected values. All are `data: dataset`. The paper's Zenodo deposits are named in the opening comment, but no claim needs them.

**Quote check:** the checker passes every quote. It flags one value, p = 2.0e-4 in `fig4i-pyramidal-modulation-increase`, which it cannot match in that format. I confirmed by reading that the text prints exactly that value (line 93).

**Details left open, with the readings named:**
- **Which sessions count for thresholds (Fig. 2A):** every session with a threshold, or only sessions where 4, 5 and 6 µA were all given on that channel.
- **Form of the exponential fit (Fig. 2A):** with or without an offset.
- **The representative animal (Fig. 2B):** not named; every animal and channel at 4 µA is searched.
- **Animals in Fig. 2E:** the legend says all 6; the script uses the first 5.
- **Week-0 comparison group (Fig. 3N):** the legend says all tracked neurons at week 0; the code uses the high-intensity subgroup at week 0.
- **High-intensity subgroup threshold (Fig. 3J):** a per-animal threshold on each neuron's last value (the processing code) is the main reading; the pooled weeks 3 and 4 threshold (the figure script) is a variant.
- **Fig. 3D to F test:** the legend and one script use a Wilcoxon signed-rank test; another script uses a rank-sum test, kept as a variant.
- **Unit-level PL label behind "265 PL and 219 NPL":** the two-step majority rule, or PL if any of the unit's responses is pulse-locked.
- **Group-level modulated-unit test (Fig. 4G):** the paper names none; read as the same one-sided test at each of 4, 5 and 6 µA.
- **Firing-rate traces for the hit-miss cluster test (Fig. 6D):** built outside the repository; 10 ms bins with 20 ms smoothing, or 2 ms bins with 5 ms smoothing. The code takes the last significant cluster's onset; the first is also reported.
- **Movement-onset definition (fig. S5):** not in the Methods or the repository code.
- **Imaging short-window measures (fig. S6):** read as recruitment count and subgroup amplitude.
- **Jitter (fig. S4):** read as the SD of latency, with its square as a variant.
- **Control spike threshold (fig. S7):** the code uses 15 spikes against 50 in the Methods; 50 is the variant.

**Problems in the paper and code:**
- The text says newly recruited neurons had "shorter" spike onset than week 0 at p = 0.479, which is not significant. That part is reported but not judged.
- The paper's data statement and the code README give different Zenodo DOIs (17727762 and 21382755).
- Whether the dandiset holds the control mice is for the author to find. The two control claims and the control part of the fig. S9 claim are blocked if it does not.

## End of run

55 turns, 9 minutes, result: success.
