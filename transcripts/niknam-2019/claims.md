# niknam-2019 · claims · run 42934302816

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  grep -n "^#" docs/protocol.md | head -50; ls paper/; ls claims | head; wc -l paper/*
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

**Agent calls Bash**

```bash
cd  sed -n 1,140p paper/10.1371-journal.pcbi.1007275.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1371-journal.pcbi.1007275.txt"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1371-journal.pcbi.1007275.txt",
 "offset": 126,
 "limit": 180
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1371-journal.pcbi.1007275.txt",
 "offset": 306,
 "limit": 60
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  head -40 paper/mt-3.data-description.txt; cat papers/datasets/niknam-2019.yaml; ls claims | grep -i nik; ls transcripts/niknam-2019 2>/dev/null
```

Result: not kept, because it reads the paper's text.

**Agent**

Now the paper's code.

**Agent calls Bash**

```bash
cd $TMPDIR && git clone -q https://github.com/nnategh/SFA-Models && cd SFA-Models && git log -1 --format='%H %cd' && find . -type f -not -path './.git/*' | head -100 && find . -type f -not -path './.git/*' | wc -l
```

```
1438dde9dd3207348ec0df1e5c4dd2a7b014e68e Fri Dec 20 14:28:34 2019 -0700
./lib/nonlin/inv_phi.m
./lib/nonlin/logsig.m
./lib/nonlin/phi.m
./lib/nonlin/dphi.m
./lib/get/get_f_knl_stm.m
./lib/get/get_s_knls.m
./lib/get/get_a_knl_stm.m
./lib/get/get_dll.m
./lib/get/get_resp.m
./lib/get/get_mean_resp.m
./lib/get/get_stim.m
./lib/get/get_fr0.m
./lib/get/get_s_fr.m
./lib/get/get_nonlin_params.m
./lib/get/get_info.m
./lib/plot/plot_ks.m
./lib/plot/plot_f_knl_stm.m
./lib/plot/plot_mean_resp.m
./lib/plot/plot_s_fr.m
[... 79 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/SFA-Models && find . -type f -not -path './.git/*' -not -path './assets/data/*' | tail -10; cat README.md main.m; wc -l lib/*/*.m | sort -n | tail -30
```

```
./lib/load/code2stim.m
./lib/load/load_data.m
./lib/load/load_map.m
./lib/load/get_id.m
./lib/load/load_model.m
./lib/load/load_file.m
./main.m
./README.md
./LICENSE
./.gitignore
# Statistical analysis of perisaccadic responses [[View Article]](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1007275)

In this paper, three perisaccadic response modulations were studied: saccadic suppression, FF-remapping, and ST-remapping. Saccadic suppression was defined as a significant decrease in the mean firing rate of the neuron over the early response window (50-75 ms after stimulus onset) in response to a stimulus presented in the RF probe location shortly before a saccade (-30 to 0 ms from saccade onset), compared to the same stimulus presented during fixation (-500 to -100 ms from saccade onset). In the same way, the FF- and ST-remapping in a neuron were defined as increases in the mean firing rate of the neuron in the late response window (80-150 ms after stimulus onset) to a stimulus presented in the FF or ST probe location shortly before saccade (-50 to 0 ms from saccade onset) compared to the same stimulus presented during fixation (-500 to -100 ms from saccade onset). In all three cases, the statistical significance was tested by comparing the perisaccadic and fixation firing rates using the Wilcoxon one-sided signed-rank test, and a p-value of less than 0.05 was considered statistically significant.
Note that all statistical analyses were performed on spike counts without any smoothing. For graphical purposes, however, the spike trains were smoothed by convolving with a 21 ms Gaussian window. The response of a neuron to a stimulus presented in a given time interval was estimated by averaging the stimulus-aligned spike trains from 0 to 150 ms after stimulus onset. Due to differences in the mean firing activity of MT neurons, their perisaccadic and fixation responses were normalized by dividing by the grand mean of their firing rates (from 0-150 m
[... 164 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/SFA-Models/lib && cat get/get_dll.m get/get_mean_resp.m get/get_info.m make/make_result.m load/load_trials.m get/get_fr0.m get/get_nonlin_params.m
```

```
function dll = get_dll(session,channel,fold,trials,times)
% Get true delta log-likelihood of specific neuron
%
% Parameters
% ----------
% - session: scalar
%   Session number with format: yyyymmdd
% - channel: scalar
%   Channel number
% - fold: integer scalar
%   Fold number
% - trials: vector
%   Trial indeces
% - times: vector
%   Time of study
%
% Returns
% -------
% - dll: scalar
%   Delta log-likelihood
[... 483 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/SFA-Models/lib && cat models/smodel.m models/amodel.m make/select_bases.m | head -400
```

```
function smodel(session,channel)
% State-variable generalized linear model framework
%
% Parameters
% ----------
% - session: scalar
%   Session number with format: yyyymmdd
% - channel: scalar
%   Channel number

fprintf('===== S-Model =====\n\n');
main_timer = tic();

% Select bases
method_timer = tic();
fprintf('----- Selct probes'' bases -----\n\n');
select_bases(session,channel);
toc(method_timer);

% Make profile
[... 373 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/SFA-Models/lib && cat nonlin/phi.m make/decide_bases.m make/make_knots.m make/make_bases.m; cat models/fmodel.m; sed -n 1,140p make/make_model.m
```

```
function [y] = phi(x,param)
% scaled/biased logarithmic sigmoid: a * s(x - b)
%
% Parameters
% ----------
% - x: array
%   Input
% - param: [scalar, scalar]
%   Scale and bias parameters
%
% Returns
% -------
% - y: array
%   Output

y = param(1) .* logsig(x - param(2));
end

function [map,delay_bases,time_bases] = decide_bases(session,channel,sigma)
% Decide about resolution of bases
[... 432 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/SFA-Models/lib && sed -n 1,120p make/fit_model.m; grep -n "1e-2\|0.01\|tol\|improvement" make/fit_model.m | head -30
```

```
function [] = fit_model(profile,session,channel,fold)
% Fit neural model
%
% Parameters
% ----------
% - profile: struct
%   Neural profile
% - session: scalar
%   Session number with format: yyyymmdd
% - channel: scalar
%   Channel number
% - fold: scalar
%   Fold number


info = get_info();

save_timer = tic();

% remove `test` data
[... 111 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/SFA-Models/lib && grep -rn "decide_bases\|sigma" --include=*.m . | grep -v "^./make/decide_bases.m" ; cat make/make_profile.m load/load_main_lists.m load/load_data.m plot/plot_results.m plot/plot_mean_resp.m | head -250
```

```
./make/make_profile.m:11:sigma = 1.5;
./make/make_profile.m:29:[decided_map,B_d,B_t] = decide_bases(session,channel,sigma);
function [] = make_profile(session,channel)
% Make neural profiles
%
% Parameters
% ----------
% - session: scalar
%   Session number with format: yyyymmdd
% - channel: scalar
%   Channel number

sigma = 1.5;

info = get_info();
width = info.width;
height = info.height;

set_of_trials = load_trials(session,channel);

[... 212 more lines not kept]
```

**Agent**

Paper and code read. The code covers the S/F/A-model fits and ΔLL/spk but none of the statistical tests. Checking the data descriptor for which experiments the dataset holds.

**Agent calls Bash**

```bash
cd  sed -n 40,132p paper/mt-3.data-description.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  ls tools schema* 2>/dev/null | head -30; grep -n "kind\|data\b\|with_labels\|allowed\|KEYS\|keys" tools/claims_check.py | head -40
```

```
schemas:
attempt.schema.json
claims.schema.json
entry.schema.json
paper-match.schema.json

tools:
__pycache__
agent_run.py
archive_transcripts.sh
archives
backfill_summaries.py
blind.sh
build_dryad_targets.py
build_figshare_targets.py
build_openneuro_targets.py
build_reuse_targets.py
build_site.py
build_targets.py
changed_entries.py
[... 12 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python -c "
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
cd  python -c "
import json;s=json.load(open('schemas/claims.schema.json'));print(json.dumps(s,indent=1)[6000:])"; ls claims | grep -c yaml; grep -l "crcns" claims/*.yaml | head -3
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
[... 137 more lines not kept]
```

**Agent calls Bash**

```bash
cd  ls -t claims | head -3; head -30 claims/$(ls -t claims | head -1)
```

```
zhong-2026.yaml
zhuang-2025.yaml
zhu-2022.yaml
# Claims for Zhong, Katkov & Tsodyks (2026), "Synaptic Theory of Chunking in Working Memory",
# eLife, doi:10.7554/elife.109538, tested on DANDI:000207.
# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"),
# 2026-11-10, protocol pilot-14 as stated in docs/protocol.md.
#
# Text read. paper/10.7554-elife.109538.txt, fetched from eLife's site. Its header says
# "version of record", but the page it holds is the eLife Reviewed Preprint version 1
# (doi:10.7554/eLife.109538.1, 9 January 2026, "Not revised"). It holds the main text, the
# Methods (sections A to E), the legends of Figures 1 to 4 and of the supplementary Figures S1
# to S3, and the Data availability statement. No PDF was supplied. The equations (1) to (15)
# and the values of Table I (simulation parameters) did not survive extraction; Eq. (1) is
# known from the text as M* = 2^(C-1) ("M ∗ = 24−1 = 8" for C = 4, and "M ∗ = 2C−1" in the
# Figure 4 legend, superscripts lost). Figure axes and plotted values could not be read.
#
# Code. The paper links none. Data availability says "The code for simulation will be made
# available in a Github repository at a later stage"; no analysis code for Figure 3 or Figure 4
# is named. No repository or commit was read.
[... 13 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 365,480p paper/10.1371-journal.pcbi.1007275.txt | grep -n "^48\|Niknam\|Chen\|McNemar\|Fagerland"
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  grep -n "^## References" -A3 paper/10.1371-journal.pcbi.1007275.txt | head; grep -n "Nonstationary\|nonstationary generalized\|mid-p\|mid-P" paper/10.1371-journal.pcbi.1007275.txt | tail -5
```

Result: not kept, because it reads the paper's text.

**Agent**

I've finished reading the paper and code. The reference list and equations didn't survive extraction, and the N-model is not in the linked code; I'll name these as open. Writing the claims file now.

**Agent calls Write**

```json
{
 "file_path": "claims/niknam-2019.yaml",
 "content": "# Claims for Niknam, Akbarian, Clark, Zamani, Noudoost & Nategh (2019), \"Characterizing and\n# dissociating multiple time-varying modulatory computations influencing neuronal activity\",\n# PLoS Comput Biol, doi:10.1371/journal.pcbi.1007275, tested on CRCNS:mt-3.\n# Written by an agent (model \"claude-opus-5-5\", Claude Code, runner \"GitHub Actions\"),\n# 2026-11-11, protocol pilot-14 as stated in docs/protocol.md.\n#\n# Text read. paper/10.1371-journal.pcbi.1007275.txt, the version of record (PMC6759185, open\n# access, Europe PMC full-text XML flattened). It holds the abstract, Introduction, Results,\n# Discussion, Methods, the legends of Figures 1 to 8, the legends of S1 to S6 Fig and S1 to S3\n# Movie, and the Data Availability statement. No PDF was supplied, so no figure could be read.\n# The supplement figures themselves are not in the text, only their legends; the numbers the\n# results rest on are in the Results text and the legends, so the supplement's absence does not\n# block a claim. Lost in extraction: every displayed equation (Eqs 1 to 14, including the\n# parameter-selection threshold, Eq 10; the classification measures of the dichotomous analysis;\n# the prevalence-map indicator m(t, tau); the maximum-detectability definition) and the whole\n# reference list, so ref [48] (the N-model), ref [49] (the McNemar mid-P test) and ref [73]\n# (Chen et al., algorithm 2) are known only by number.\n#\n# Code. https://github.com/nnategh/SFA-Models, commit 1438dde9dd3207348ec0df1e5c4dd2a7b014e68e\n# (2019-12-20), linked in Methods (A-model framework) and Data Availability. MATLAB. It holds\n# the S-model fit (lib/models/smodel.m; parameter selection in lib/make/select_bases.m and\n# decide_bases.m; coordinate-ascent fit in lib/make/fit_model.m; condition-wise\n# train/validation/test split in lib/load/load_trials.m), the F-model fit\n# (lib/models/fmodel.m), the A-model average (lib/models/amodel.m), Delta LL per spike\n# (lib/get/get_dll.m), mean stimulus-aligned responses (lib/get/get_mean_resp.m) and plots. Its\n# README restates the Methods. It holds no code for the N-model, the Wilcoxon tests, the\n# McNemar test, the classification measures, the partial F-models, the robust regression, the\n# prevalence maps, the ROC detectability analysis or the synthetic neurons. It also holds\n# assets/data/*.mat (copies of the neuron files; not opened) and assets/data/main_lists.mat,\n# whose probe_list fmodel.m reads as each neuron's RF, FF and ST probe (columns 3-4, 5-6,\n# 7-8). Settings the code fixes where the Methods are silent: kernels span -540 to +540 ms from\n# saccade and delays 1 to 150 ms (get_info.m); trials are split by condition, 35% of conditions\n# for test, then 35% training and 30% validation (load_trials.m); the parameter-selection\n# threshold is |mean - control mean| >= 1.5 control SD (make_profile.m, README Eq 10); r_max is\n# fixed at 1000 spk/s and b0 = f^-1 of the mean rate over bins with a probe on screen\n# (select_bases.m make_params, phi.m); F-model delay bins as in get_info.m lags; bounds for\n# t >= 100 ms tie the RF Gaussian centre to the RF probe with spread at most 1 (fmodel.m); the\n# F-kernel is smoothed with a 10-point moving average over delay (fmodel.m). Where the code\n# and Methods disagree, the Methods are the main reading and the code a variant: get_fr0.m\n# uses as NULL model the S-model's offset and post-spike kernels without stimulus kernels, the\n# Methods a constant average rate; amodel.m averages kernels, the Methods average the\n# Gaussian parameters; get_info.m sets num_folds = 1, the Methods fit ten S-models;\n# get_mean_resp.m takes every ms a probe is on, the Methods take stimulus onset.\n#\n# Data the paper used (Methods, Experimental paradigm and data acquisition). Two adult male\n# rhesus monkeys; 41 single MT neurons (of 49 isolated; 8 dropped for no probe response), 11\n# sessions, saccades leftward in 9 sessions (27 neurons) and rightward in 2 (14 neurons).\n# Visually guided saccade task, fixation point at centre, saccade target 10 deg horizontal,\n# fixation 600-750 ms before the go cue. Throughout each trial (2100-2300 ms) white 0.5 deg\n# probes flashed for 7 ms each, one at a time, on a 9 x 9 grid, in a pseudorandom order (a\n# \"condition\") of 81 probes. Variables per neuron, per the dataset's description: stimcode\n# (trial x ms, probe index 0-81), conds (condition per trial), resp (trial x ms spikes, 1 ms\n# bins) and tsaccade (saccade onset per trial, ms). The grid geometry in dva, the saccade\n# direction and the ST position on the grid are not among the variables the description lists;\n# the RF, FF and ST probes are in the code repository's main_lists.mat (see O3).\n#\n# Shared definitions, cited, used by the criteria below.\n# D1 Locations (Methods, Receptive field, future field, and saccade target location\n#    estimation). RF is the probe with the highest firing rate for stimuli shown -500 to -100\n#    ms from saccade, counted 50-75 ms after probe onset. FF is the RF probe shifted by the\n#    rounded saccade vector. ST is, of the 4 x 4 probes around the target and excluding the FF\n#    and its neighbours, the probe with the largest late (80-150 ms) increase for stimuli at\n#    -50 to 0 ms against fixation.\n# D2 Recorded effects (Methods, Statistical analysis of perisaccadic responses). Suppression is\n#    a decrease in spike count 50-75 ms after an RF probe shown -30 to 0 ms from saccade onset,\n#    against the same probe shown -500 to -100 ms. FF and ST remapping are increases in spike\n#    count 80-150 ms after an FF or ST probe shown -50 to 0 ms, against -500 to -100 ms. Test\n#    one-sided Wilcoxon signed-rank, p < 0.05, uncorrected, on spike counts.\n# D3 Normalized responses (same section, paragraph 2). The response is the average\n#    stimulus-aligned spike train 0-150 ms after onset; each neuron's perisaccadic and fixation\n#    responses are divided by the mean of their two means over 0-150 ms, then averaged over\n#    neurons; SE across neurons. Plots smooth with a Gaussian of FWHM 13 ms.\n# D4 Models (Methods, S-model, F-model and A-model frameworks; code above). S-model, Eq 1 with\n#    a sigmoid, 1 ms bins, B-spline bases with the knots stated in Methods, parameter\n#    selection over 100 random 65% subsets against shuffled responses, block coordinate\n#    ascent on training data while validation likelihood rises, test 35% withheld. F-model\n#    fitted to the S-kernels per time and delay bin with the bounds stated in Methods,\n#    fixation kernel from -400 to -300 ms. A-model from ten S-model and F-model fits on random\n#    65% subsets with Gaussian parameters and c averaged. \"Model\" from Fig 6 on is the A-model\n#    (Results, \"From now on\").\n# D5 Delta LL per spike (Methods, Model evaluation). Point-process log-likelihood of the test\n#    spikes with true spike history, minus that of a NULL model, divided by the spike count, in\n#    bits. Perisaccadic spikes are those 0 to 150 ms after saccade onset, fixation spikes those\n#    450 to 0 ms before.\n# D6 Model-predicted effects (Methods, Statistical analysis of model predictions). 1000\n#    stimulus sequences given to each fitted model with simulated spike history (ref [73],\n#    algorithm 2; the code's make_result.m make_resp draws spikes from the rate step by step);\n#    effects defined with the windows of D2 on the predicted rate, tested with a one-sided\n#    Wilcoxon rank-sum test, p < 0.05; normalized as D3 on predicted rates.\n#\n# Open details, with the readings the text allows (each criterion names the ones it uses).\n# O1 Pairing for the signed-rank test of D2. The Methods name a paired test but not the pairs.\n#    (a) per trial, mean count over the trial's presentations in the perisaccadic window\n#    against its mean over presentations in the fixation window, trials with both; (b) per\n#    condition, the same pooled over the trials of each condition; (c) unpaired, all\n#    presentations, one-sided rank-sum, the test the Methods use for model predictions.\n# O2 What counts as a presentation. (i) the onset ms of each 7 ms probe (Methods, \"stimulus\n#    onset\"); (ii) every ms the probe is on, as get_mean_resp.m does. (i) is the main reading.\n# O3 RF, FF and ST probes. (a) probe_list in main_lists.mat of the code repository; (b)\n#    recomputed by D1, possible for RF from the dataset alone, for FF and ST only with the\n#    saccade vector and target position on the grid. (a) is the main reading; claim\n#    probe-locations-link checks it.\n# O4 The value reported for a subpopulation's normalized response. (a) mean over the effect's\n#    window (50-75 ms or 80-150 ms after onset) of the normalized response, averaged over\n#    neurons, the reading Fig 6's text states (\"over the early response window\"); (b) the\n#    value at the peak, within that window, of the neuron-averaged curve smoothed as D3.\n# O5 The NULL model of D5. (a) constant at the neuron's mean rate over all trials (r0 of the\n#    S-model framework); (b) constant at the mean rate of the evaluated test trials; (c) the\n#    code's get_fr0.m (offset and post-spike kernels without stimulus kernels), a variant.\n#    Whether D5 is pooled over all test trials of a neuron or averaged per trial is settled\n#    by get_dll.m: pooled.\n# O6 The sequences of D6, \"the same as those for the experimental paradigm\". (a) the\n#    recorded conditions resampled, each with a recorded saccade time; (b) new pseudorandom\n#    81-probe sequences of 7 ms probes, saccade at a recorded time drawn at random.\n# O7 Nulling a source in the partial F-models (Methods, The perisaccadic to fixation\n#    performance ratio analysis, paragraph 2). (a) for each time and delay bin, the Gaussian's\n#    parameters taken from a randomly drawn time between -400 and -300 ms at the same delay\n#    bin; (b) one randomly drawn fixation time per model, used for all times.\n# O8 The N-model (ref [48]). This paper does not describe its fitting beyond Fig 4 and the\n#    Results paragraph on it, the code holds none, and the reference list is missing from the\n#    text read. The author takes it from ref [48] if it can be identified (the Introduction\n#    calls it the nonstationary generalized linear model, NSGLM, of the same group); if not,\n#    claims that need it are blocked.\nschema_version: 2\npaper: doi:10.1371/journal.pcbi.1007275\nclaims:\n- id: probe-locations-link\n  kind: link\n  statement: The RF, FF and ST probe of each neuron listed in the code repository's\n    main_lists.mat correspond to the dataset's neurons, and the RF probe recomputed from the\n    dataset by the Methods' definition matches the listed one.\n  source: Methods, Receptive field, future field, and saccade target location estimation; code\n    lib/models/fmodel.m (get_centers) at commit 1438dde\n  data: with_labels\n  criterion: >-\n    Neurons are matched by session and channel (file name, and probe_list columns 1 and 2, as\n    fmodel.m reads them). The link holds (reproduced) when all 41 analysed neurons are listed\n    and, for at least 37 of them (90%), the probe with the highest mean spike count 50-75 ms\n    after onset of probes shown -500 to -100 ms from saccade (D1, onset reading O2 i) is the\n    listed RF probe or one of its eight neighbours; partially reproduced for 29 to 36; not\n    reproduced below 29. For each neuron the FF minus RF offset is reported, with its sign\n    taken as the saccade direction, against the paper's 27 leftward and 14 rightward neurons.\n- id: methods-neuron-counts\n  statement: Of 49 well-isolated MT neurons, 41 responded to the probes and were analysed;\n    they come from 11 sessions, 27 neurons from 9 sessions with leftward saccades and 14 from 2\n    sessions with rightward saccades.\n  source: Methods, Experimental paradigm and data acquisition, paragraph 1\n  quote: >-\n    In total, data were recorded from 41 MT neurons during 11 recording sessions. In 9\n    recording sessions, the saccades were made to the left (27 of 41 neurons), and in 2\n    recording sessions, the saccades were made to the right (14 of 41 neurons).\n  data: with_labels\n  depends_on:\n  - probe-locations-link\n  expected:\n  - quantity: neurons analysed\n    value: 41\n    tolerance: 0\n  - quantity: sessions\n    value: 11\n    tolerance: 0\n  - quantity: neurons with leftward saccades\n    value: 27\n    tolerance: 0\n  - quantity: neurons with rightward saccades\n    value: 14\n    tolerance: 0\n  criterion: >-\n    Counts are exact, so no tolerance. Sessions are the first 8 digits of the file name\n    (dataset description). Saccade direction is not a variable of the dataset; it is read as\n    the sign of the horizontal FF minus RF offset from probe_list (O3 a), with the grid's\n    orientation taken from the code's ind2sub([9,9]) indexing. Reproduced when all four\n    counts match.\n- id: fig1b-saccadic-suppression\n  statement: Eight neurons show significant saccadic suppression; for them the average\n    normalized response to an RF probe drops from 2.53 to 1.51 when the probe appears just\n    before the saccade.\n  source: Results, Saccades modulate the responses of MT neurons, paragraph 1; Figure 1B\n  quote: >-\n    For the subpopulation of neurons with significant saccadic suppression (see Methods ),\n    the average normalized response dropped from 2.53 ± 0.37 to 1.51 ± 0.29 (mean ± SE).\n  data: with_labels\n  depends_on:\n  - probe-locations-link\n  expected:\n  - quantity: neurons with significant saccadic suppression\n    value: 8\n    tolerance: 0.8\n  - quantity: normalized RF response during fixation, suppressed neurons\n    value: 2.53\n    tolerance: 0.37\n  - quantity: normalized RF response perisaccadic, suppressed neurons\n    value: 1.51\n    tolerance: 0.29\n  criterion: >-\n    Neurons classified by D2 (suppression) with RF from O3 a. The count is taken under each\n    pairing of O1 (a, b, c) and each presentation reading of O2 (i main, ii variant). The\n    normalized values follow D3 and O4 (a main, b variant), on the neurons the same reading\n    selects. Tolerances are the paper's SE for the normalized values and 10% for the count.\n    Reproduced when, under one reading of O1 with O2 i, the count and both values are within\n    tolerance and the perisaccadic value is below the fixation value; partially reproduced\n    when the direction and one of the three numbers hold.\n- id: fig1c-ff-remapping\n  statement: Twenty-three neurons show significant FF-remapping; for them the average\n    normalized late response to an FF probe rises from 0.90 during fixation to 1.30 just\n    before the saccade, at a longer latency than the RF response.\n  source: Results, Saccades modulate the responses of MT neurons, paragraph 1; Figure 1C\n  quote: >-\n    For the subpopulation of neurons with significant FF-remapping, the average normalized\n    response to FF stimuli increased from 0.90 ± 0.03 to 1.30 ± 0.08 (mean ± SE).\n  data: with_labels\n  depends_on:\n  - probe-locations-link\n  expected:\n  - quantity: neurons with significant FF-remapping\n    value: 23\n    tolerance: 2.3\n  - quantity: normalized FF response during fixation, remapping neurons\n    value: 0.9\n    tolerance: 0.03\n  - quantity: normalized FF response perisaccadic, remapping neurons\n    value: 1.3\n    tolerance: 0.08\n  criterion: >-\n    As fig1b-saccadic-suppression, with the FF-remapping test of D2 (FF probe, -50 to 0 ms,\n    late window 80-150 ms) and O4 on the late window. Reproduced when, under one reading of\n    O1 with O2 i, the count and both values are within tolerance with the perisaccadic value\n    above the fixation value; partially reproduced when the direction and one of the three\n    numbers hold.\n- id: fig1d-st-remapping\n  statement: Thirty-seven neurons show significant ST-remapping; for them the average\n    normalized late response to a probe near the saccade target rises from 0.83 during\n    fixation to 1.35 just before the saccade.\n  source: Results, Saccades modulate the responses of MT neurons, paragraph 1; Figure 1D\n  quote: >-\n    For the subpopulation of neurons with significant ST-remapping, the average normalized ST\n    response increased from 0.83 ± 0.03 to 1.35 ± 0.06 (mean ± SE).\n  data: with_labels\n  depends_on:\n  - probe-locations-link\n  expected:\n  - quantity: neurons with significant ST-remapping\n    value: 37\n    tolerance: 3.7\n  - quantity: normalized ST response during fixation, remapping neurons\n    value: 0.83\n    tolerance: 0.03\n  - quantity: normalized ST response perisaccadic, remapping neurons\n    value: 1.35\n    tolerance: 0.06\n  criterion: >-\n    As fig1c-ff-remapping, with the ST probe. The ST probe is itself chosen by D1 as the probe\n    with the largest perisaccadic late increase, so the test is on the probe that selection\n    picked; this is the paper's procedure. Same rule for reproduced and partially reproduced.\n- id: fig1e-ff-and-st-remapping\n  statement: Twenty-two neurons show both FF- and ST-remapping; for them the normalized FF\n    response rises from 0.90 to 1.32 and the normalized ST response from 0.80 to 1.46.\n  source: Results, Saccades modulate the responses of MT neurons, paragraph 1; Figure 1E\n  quote: >-\n    For the subpopulation of neurons with significant FF- and ST-remapping, the average\n    normalized FF response increased from 0.90 ± 0.03 to 1.32 ± 0.08 (mean ± SE), and the\n    average normalized ST response increased from 0.80 ± 0.03 to 1.46 ± 0.08 (mean ± SE).\n  data: with_labels\n  depends_on:\n  - fig1c-ff-remapping\n  - fig1d-st-remapping\n  expected:\n  - quantity: neurons with both FF- and ST-remapping\n    value: 22\n    tolerance: 2.2\n  - quantity: normalized FF response during fixation, both effects\n    value: 0.9\n    tolerance: 0.03\n  - quantity: normalized FF response perisaccadic, both effects\n    value: 1.32\n    tolerance: 0.08\n  - quantity: normalized ST response during fixation, both effects\n    value: 0.8\n    tolerance: 0.03\n  - quantity: normalized ST response perisaccadic, both effects\n    value: 1.46\n    tolerance: 0.08\n  criterion: >-\n    The neurons significant in both fig1c-ff-remapping and fig1d-st-remapping under the same\n    reading. Reproduced when, under one reading of O1 with O2 i, the count and all four values\n    are within tolerance with both increases; partially reproduced when both increases hold\n    and at least two of the five numbers are within tolerance.\n- id: fig1-remapping-longer-latency\n  statement: Perisaccadic FF and ST responses come at a longer latency (80-150 ms after the\n    probe) than RF responses (50-75 ms).\n  source: Results, Saccades modulate the responses of MT neurons, paragraph 1; Figure 1C and 1D\n  quote: >-\n    Note that the perisaccadic FF response occurs at longer latency than RF responses\n    (neurons responding 50–75 ms after stimulus onset for the RF, vs. 80–150 ms after stimulus\n    onset for the FF).\n  data: with_labels\n  depends_on:\n  - fig1c-ff-remapping\n  - fig1d-st-remapping\n  criterion: >-\n    The paper states this from the plotted responses of Fig 1, which cannot be read here; no\n    measure is named. Measure fixed from D3, the plotted quantity. For each subpopulation,\n    the neuron-averaged normalized response 0-150 ms after onset, smoothed with a Gaussian of\n    FWHM 13 ms (D3): the latency of the peak of the fixation RF response over all 41 neurons,\n    and of the perisaccadic FF response (FF-remapping neurons) and ST response (ST-remapping\n    neurons). Reproduced when the RF peak lies within 50-75 ms and both remapped peaks within\n    80-150 ms; partially reproduced when the remapped peaks are later than the RF peak but one\n    lies outside its stated range.\n- id: fig1-example-neurons\n  statement: In example neurons the RF response falls from 60.89 to 40.49 spk/s before the\n    saccade; the late FF response rises from 7.90 to 18.42 spk/s; the late ST response rises\n    from 23.80 to 64.64 spk/s; and in a neuron with both effects FF rises from 15.83 to 39.10\n    and ST from 16.15 to 36.17 spk/s, each with p < 0.001.\n  source: Results, Saccades modulate the responses of MT neurons, paragraph 1; Figure 1B to 1E,\n    left panels\n  quote: >-\n    For the example neuron, the average response to an RF stimulus dropped from 60.89 ± 2.82\n    (mean ± SE) spk/s during fixation to 40.49 ± 12.64 (mean ± SE) spk/s when the stimulus\n    appeared just prior to saccade onset (example neuron, p < 0.001).\n  statistics:\n  - about: each of the five example-neuron comparisons\n    test: Wilcoxon one-sided signed-rank test (Methods, Statistical analysis of perisaccadic\n      responses)\n    p: 0.001\n    p_relation: \"<\"\n  data: with_labels\n  depends_on:\n  - probe-locations-link\n  expected:\n  - quantity: example neuron, RF response during fixation\n    value: 60.89\n    tolerance: 2.82\n    unit: spk/s\n  - quantity: example neuron, RF response perisaccadic\n    value: 40.49\n    tolerance: 12.64\n    unit: spk/s\n  - quantity: example neuron, late FF response during fixation\n    value: 7.9\n    tolerance: 1.02\n    unit: spk/s\n  - quantity: example neuron, late FF response perisaccadic\n    value: 18.42\n    tolerance: 3.56\n    unit: spk/s\n  - quantity: example neuron, late ST response during fixation\n    value: 23.8\n    tolerance: 1.77\n    unit: spk/s\n  - quantity: example neuron, late ST response perisaccadic\n    value: 64.64\n    tolerance: 7.91\n    unit: spk/s\n  - quantity: example neuron with both effects, late FF response during fixation\n    value: 15.83\n    tolerance: 0.91\n    unit: spk/s\n  - quantity: example neuron with both effects, late FF response perisaccadic\n    value: 39.1\n    tolerance: 5.14\n    unit: spk/s\n  - quantity: example neuron with both effects, late ST response during fixation\n    value: 16.15\n    tolerance: 0.94\n    unit: spk/s\n  - quantity: example neuron with both effects, late ST response perisaccadic\n    value: 36.17\n    tolerance: 4.49\n    unit: spk/s\n  criterion: >-\n    The paper does not identify the example neurons. Rates are mean spike counts per second\n    over the effect's window (50-75 ms for RF, 80-150 ms \"late\" for FF and ST) after\n    presentations in the windows of D2, SE across presentations, presentations by O2 (i main,\n    ii variant). The other quotes of the paragraph give the FF, ST and both-effects values.\n    For each of the four examples, every neuron among the 41 is searched. Reproduced when,\n    for each example, at least one neuron has both values within tolerance and a significant\n    change by D2 under one reading of O1; partially reproduced when this holds for two or\n    three of the four examples. The matching neurons are named.\n- id: fig3-example-trial-predictions\n  statement: In example test trials of three neurons the S- and F-models follow the recorded\n    firing rate, with Delta LL per spike up to 1.12 bits/spk for the S-model and 0.81 for the\n    F-model in the best trials, and 0.19 to 0.46 (S) and 0.05 to 0.41 (F) in median trials.\n  source: Results, The time-varying encoding models accurately predict single trial spike\n    response modulations across saccades, paragraph 1; Figure 3\n  quote: >-\n    The trials on the left show examples of high prediction accuracy (from top to bottom, Δ\n    LL / spk = 1.12, 0.80, and 0.63 bits/spk for the S-model; and Δ LL / spk = 0.81, 0.47,\n    and 0.55 bits/spk for the F-model)\n  criterion: >-\n    Illustrative. The paper does not identify the neurons or trials, and the test split is\n    random (load_trials.m), so the values cannot be matched. Not judged on its own; the\n    claims on Fig 5A test prediction accuracy over the population. The author reports, for\n    each neuron, the best and median per-trial Delta LL per spike (D5) over its test trials\n    for the S- and F-models, for comparison only.\n- id: fig5a-n-model-no-perisaccadic-gain\n  statement: The N-model predicts perisaccadic spikes no better than fixation spikes (0.13\n    against 0.12 bits/spk, p = 0.26).\n  source: Results, The time-varying encoding models accurately predict single trial spike\n    response modulations across saccades, paragraph 3; Figure 5A\n  quote: >-\n    The N-model is no better at predicting the spike times during the perisaccadic period\n    compared to the fixation period (Δ LL / spk = 0.12 ± 0.02 (mean ± SE) bits/spk during\n    fixation vs. 0.13 ± 0.02 (mean ± SE) bits/spk during saccade, p-value = 0.26).\n  statistics:\n  - test: Wilcoxon signed-rank test\n    p: 0.26\n    n: 41 neurons\n  expected:\n  - quantity: N-model Delta LL per spike, fixation\n    value: 0.12\n    tolerance: 0.02\n    unit: bits/spk\n  - quantity: N-model Delta LL per spike, perisaccadic\n    value: 0.13\n    tolerance: 0.02\n    unit: bits/spk\n  criterion: >-\n    Needs the N-model (O8). Delta LL per spike by D5 with NULL model O5 (a main; b, c\n    variants), on test trials, per neuron. A claim of absence, judged on the paper's test, a\n    two-sided Wilcoxon signed-rank test over 41 neurons at p < 0.05 (Results paragraph 3,\n    \"In all comparisons\"): reproduced when it does not find perisaccadic above fixation, not\n    reproduced when it does. The means and the effect size are reported either way.\n- id: fig5a-s-model-perisaccadic-better\n  statement: The S-model predicts perisaccadic spikes better than fixation spikes (0.30\n    against 0.24 bits/spk, p < 0.001).\n  source: Results, The time-varying encoding models accurately predict single trial spike\n    response modulations across saccades, paragraph 3; Figure 5A\n  quote: >-\n    For the S-model, the prediction accuracy increases in the perisaccadic period (Δ LL / spk\n    = 0.24 ± 0.02 (mean ± SE) bits/spk during fixation vs. 0.30 ± 0.02 (mean ± SE) bits/spk\n    during saccade, p-value < 0.001).\n  statistics:\n  - test: Wilcoxon signed-rank test\n    p: 0.001\n    p_relation: \"<\"\n    n: 41 neurons\n  expected:\n  - quantity: S-model Delta LL per spike, fixation\n    value: 0.24\n    tolerance: 0.02\n    unit: bits/spk\n  - quantity: S-model Delta LL per spike, perisaccadic\n    value: 0.3\n    tolerance: 0.02\n    unit: bits/spk\n  criterion: >-\n    One S-model per neuron fitted by D4 (code settings as listed in the opening comment),\n    evaluated on its withheld test trials with true spike history (Methods, Model\n    evaluation), D5 with NULL model O5 (a main; b, c variants). Reproduced when, under one\n    reading of O5, both means are within tolerance and a Wilcoxon signed-rank test over the 41\n    neurons gives perisaccadic above fixation at p < 0.05; partially reproduced when the test\n    holds but a mean is outside tolerance. Because the split and parameter selection are\n    random, the author reports the spread over at least three random splits if run time\n    allows.\n- id: fig5a-f-model-perisaccadic-better\n  statement: The F-model also predicts perisaccadic spikes better than fixation spikes (0.18\n    against 0.14 bits/spk, p = 0.003).\n  source: Results, The time-varying encoding models accurately predict single trial spike\n    response modulations across saccades, paragraph 3; Figure 5A\n  quote: >-\n    The F-model, despite being based on an approximation of the S-model, also shows greater\n    prediction accuracy during the perisaccadic period compared to fixation (Δ LL / spk =\n    0.14 ± 0.01 (mean ± SE) bits/spk during fixation vs. 0.18 ± 0.02 (mean ± SE) bits/spk\n    during saccade, p-value = 0.003).\n  statistics:\n  - test: Wilcoxon signed-rank test\n    p: 0.003\n    n: 41 neurons\n  depends_on:\n  - fig5a-s-model-perisaccadic-better\n  - probe-locations-link\n  data: with_labels\n  expected:\n  - quantity: F-model Delta LL per spike, fixation\n    value: 0.14\n    tolerance: 0.01\n    unit: bits/spk\n  - quantity: F-model Delta LL per spike, perisaccadic\n    value: 0.18\n    tolerance: 0.02\n    unit: bits/spk\n  criterion: >-\n    The F-model of D4 built from the same S-model fit (centres from O3 a, as fmodel.m), with\n    the S-model's post-spike and offset kernels (Results, Fig 4 paragraph), on the same test\n    trials. Same rule as fig5a-s-model-perisaccadic-better.\n- id: fig5a-s-f-beat-n-model\n  statement: Both the S- and F-models outperform the N-model in the fixation and perisaccadic\n    periods.\n  source: Results, The time-varying encoding models accurately predict single trial spike\n    response modulations across saccades, paragraph 3; Figure 5A\n  quote: >-\n    Both the S-, and F-models outperform the N-model during both the fixation (S-model vs.\n    N-model: p-value < 0.001; F-model vs. N-model: p-value = 0.001) and perisaccadic (S-model\n    vs. N-model: p-value < 0.001; F-model vs. N-model: p-value < 0.001) periods.\n  statistics:\n  - about: S- against N-model, fixation\n    test: Wilcoxon signed-rank test\n    p: 0.001\n    p_relation: \"<\"\n    n: 41 neurons\n  - about: F- against N-model, fixation\n    test: Wilcoxon signed-rank test\n    p: 0.001\n    n: 41 neurons\n  - about: S- against N-model, perisaccadic\n    test: Wilcoxon signed-rank test\n    p: 0.001\n    p_relation: \"<\"\n    n: 41 neurons\n  - about: F- against N-model, perisaccadic\n    test: Wilcoxon signed-rank test\n    p: 0.001\n    p_relation: \"<\"\n    n: 41 neurons\n  depends_on:\n  - fig5a-n-model-no-perisaccadic-gain\n  - fig5a-s-model-perisaccadic-better\n  - fig5a-f-model-perisaccadic-better\n  data: with_labels\n  criterion: >-\n    Needs the N-model (O8). Per-neuron Delta LL per spike of these claims, compared by a\n    Wilcoxon signed-rank test over 41 neurons. Reproduced when all four comparisons show the\n    S- or F-model higher at p < 0.05; partially reproduced for two or three.\n- id: fig5b-st-remapping-better-than-n\n  statement: The S-, F- and A-models all reproduce which neurons show ST-remapping\n    significantly better than the N-model.\n  source: Results, The time-varying encoding models accurately predict single trial spike\n    response modulations across saccades, paragraph 4; Figure 5B\n  quote: >-\n    The S-, F-, and A-models all significantly outperform the N-model in terms of reproducing\n    the ST-remapping effect (S-model vs. N-model: p = 0.004, F-model vs. N-model: p = 0.006,\n    and F-model vs. N-model: p = 0.006).\n  statistics:\n  - about: S- against N-model\n    test: one-tailed mid P-value McNemar test\n    p: 0.004\n    n: 41 neurons\n  - about: F- against N-model\n    test: one-tailed mid P-value McNemar test\n    p: 0.006\n    n: 41 neurons\n  - about: third comparison, printed \"F-model vs. N-model\", read as the A-model\n    test: one-tailed mid P-value McNemar test\n    p: 0.006\n    n: 41 neurons\n  data: with_labels\n  depends_on:\n  - fig1d-st-remapping\n  criterion: >-\n    Needs the N-model (O8). Per neuron, the recorded classification of D2 (all trials, O1 and\n    O2 readings as in fig1d-st-remapping) against the model classification of D6 (sequences\n    O6 a main, b variant), each model fitted as D4. A model is correct for a neuron when the\n    two agree (Methods, Dichotomous analysis). The one-tailed mid-P McNemar test on the\n    discordant neurons between each model and the N-model (ref [49]; the standard mid-P\n    binomial form). The text prints \"F-model vs. N-model\" twice; the third value is read as\n    the A-model, the only model the sentence names that it otherwise lacks. Reproduced when\n    all three models beat the N-model at p < 0.05; partially reproduced for one or two. The\n    four measures of Fig 5B (sensitivity, accuracy, the geometric mean of sensitivity and\n    precision, F-measure with alpha 1/2) are reported for each model.\n- id: fig5b-ff-remapping-a-model-only\n  statement: For FF-remapping only the A-model reproduces the classification of neurons\n    significantly better than the N-model; the S- and F-models do not.\n  source: Results, The time-varying encoding models accurately predict single trial spike\n    response modulations across saccades, paragraph 4; Figure 5B\n  quote: >-\n    For the FF-remapping effect, the A-model significantly outperforms the N-model (p =\n    0.048); the S- and F- models did not significantly outperform the N-model (S-model vs.\n    N-model: p = 0.17, and F-model vs. N-model: p = 0.08).\n  statistics:\n  - about: A- against N-model\n    test: one-tailed mid P-value McNemar test\n    p: 0.048\n    n: 41 neurons\n  - about: S- against N-model\n    test: one-tailed mid P-value McNemar test\n    p: 0.17\n    n: 41 neurons\n  - about: F- against N-model\n    test: one-tailed mid P-value McNemar test\n    p: 0.08\n    n: 41 neurons\n  data: with_labels\n  depends_on:\n  - fig1c-ff-remapping\n  criterion: >-\n    As fig5b-st-remapping-better-than-n, for FF-remapping. The S- and F-model parts are\n    claims of absence judged on the same test at p < 0.05. Reproduced when the A-model beats\n    the N-model at p < 0.05 and the S- and F-models do not; partially reproduced when two of\n    the three outcomes match.\n- id: fig5b-suppression-no-difference\n  statement: No model differs significantly from the N-model in reproducing saccadic\n    suppression, suggesting that a global gain change suffices for it.\n  source: Results, The time-varying encoding models accurately predict single trial spike\n    response modulations across saccades, paragraph 4; Figure 5B\n  quote: >-\n    Finally, we did not find any significant difference between the S-, F-, and A-models and\n    N-model in terms of reproducing the saccadic suppression effect\n  statistics:\n  - about: S- against N-model\n    test: one-tailed mid P-value McNemar test\n    p: 0.38\n    n: 41 neurons\n  - about: F- against N-model\n    test: one-tailed mid P-value McNemar test\n    p: 0.17\n    n: 41 neurons\n  - about: third comparison, printed \"F-model vs. N-model\", read as the A-model\n    test: one-tailed mid P-value McNemar test\n    p: 0.11\n    n: 41 neurons\n  data: with_labels\n  depends_on:\n  - fig1b-saccadic-suppression\n  criterion: >-\n    A claim of absence on the paper's test, the one-tailed mid-P McNemar test at p < 0.05, as\n    fig5b-st-remapping-better-than-n for saccadic suppression. Reproduced when none of the\n    three models beats the N-model; not reproduced when any does. The p-values and the\n    discordant counts are reported either way.\n- id: fig5c-f-higher-ratio-than-s\n  statement: The F-model has a higher perisaccadic to fixation performance ratio than the\n    S-model (median 1.51 against 1.33, p = 0.003), so it better reproduces perisaccadic\n    changes specifically.\n  source: Results, The time-varying encoding models accurately predict single trial spike\n    response modulations across saccades, paragraph 5\n  quote: >-\n    The S-model has a lower perisaccadic to fixation ratio compared to the F-model (1.33 ±\n    0.99 (median ± SE) for the S-model vs. 1.51 ± 0.25 (median ± SE) for the F-model,\n    Wilcoxon signed‐rank p‐value = 0.003)\n  statistics:\n  - test: Wilcoxon signed-rank test\n    p: 0.003\n  data: with_labels\n  depends_on:\n  - fig5a-f-model-perisaccadic-better\n  expected:\n  - quantity: S-model perisaccadic to fixation ratio, median\n    value: 1.33\n    tolerance: 0.99\n  - quantity: F-model perisaccadic to fixation ratio, median\n    value: 1.51\n    tolerance: 0.25\n  criterion: >-\n    Per neuron, the ratio of perisaccadic to fixation Delta LL per spike (D5, O5 a main) over\n    the test trials with a probe at the RF, FF or ST location during -50 to 0 ms from saccade\n    (Methods, The perisaccadic to fixation performance ratio analysis, paragraph 1). The SE of\n    a median is not defined in the paper; it is not used beyond the tolerance. Reproduced\n    when both medians are within tolerance and a two-sided Wilcoxon signed-rank test on the\n    per-neuron ratios gives F above S at p < 0.05; partially reproduced when the test holds\n    but a median is outside tolerance.\n- id: fig5c-source-contributions\n  statement: The F-model's perisaccadic to fixation ratio (1.35) falls to 0.28 without any\n    source; adding the FF source alone restores most of it (0.95), more than RF (0.53) or ST\n    (0.48), and removing FF lowers it most (0.72, against 1.20 without RF and 1.27 without ST).\n  source: Results, The time-varying encoding models accurately predict single trial spike\n    response modulations across saccades, paragraph 5; Figure 5C, top; S6 Fig\n  quote: >-\n    The F-model which incorporates all three sources has the highest perisaccadic to fixation\n    performance ratio (1.35 ± 0.09), and eliminating any individual source decreases the\n    perisaccadic to fixation performance ratio (-RF: 1.20 ± 0.11, -FF: 0.72 ± 0.08, -ST: 1.27\n    ± 0.11).\n  data: with_labels\n  depends_on:\n  - fig5a-f-model-perisaccadic-better\n  expected:\n  - quantity: no-source ratio\n    value: 0.28\n    tolerance: 0.08\n  - quantity: +RF ratio\n    value: 0.53\n    tolerance: 0.09\n  - quantity: +FF ratio\n    value: 0.95\n    tolerance: 0.14\n  - quantity: +ST ratio\n    value: 0.48\n    tolerance: 0.09\n  - quantity: F-model ratio\n    value: 1.35\n    tolerance: 0.09\n  - quantity: -RF ratio\n    value: 1.2\n    tolerance: 0.11\n  - quantity: -FF ratio\n    value: 0.72\n    tolerance: 0.08\n  - quantity: -ST ratio\n    value: 1.27\n    tolerance: 0.11\n  criterion: >-\n    Partial F-models by nulling Gaussians as O7 (a main, b variant). For each model, the\n    slope of a zero-intercept robust regression of perisaccadic on fixation Delta LL per spike\n    over the 41 neurons (MATLAB fitlm, RobustOpts 'fair', S6 Fig legend; an equivalent\n    iteratively reweighted least-squares fit with the fair weight and its default tuning\n    constant 1.4 is acceptable), with the trials of fig5c-f-higher-ratio-than-s; tolerances\n    are the paper's slope SE. Reproduced when, under one reading of O7, the ordering holds\n    (no-source lowest, F-model highest, +FF the highest single source, -FF the lowest\n    single-source removal) and at least six of the eight slopes are within tolerance;\n    partially reproduced when the ordering holds with fewer values in tolerance.\n- id: fig5c-percent-changes\n  statement: Adding the RF, FF or ST source raises the ratio by 23.38%, 62.65% and 18.89% of\n    the F-model's total gain over the no-source model, and removing them lowers it by 14.79%,\n    59.38% and 7.87%.\n  source: Results, The time-varying encoding models accurately predict single trial spike\n    response modulations across saccades, paragraph 5; Figure 5C, bottom\n  quote: >-\n    As seen, adding the RF, FF, or ST source improves the perisaccadic to fixation ratio by\n    23.38%, 62.65%, and 18.89%, respectively, and eliminating the RF, FF, or ST source\n    decreases the ratio by 14.79%, 59.38%, and 7.87%, respectively.\n  data: with_labels\n  depends_on:\n  - fig5c-source-contributions\n  expected:\n  - quantity: increase with RF only\n    value: 23.38\n    tolerance: 2.34\n    unit: \"%\"\n  - quantity: increase with FF only\n    value: 62.65\n    tolerance: 6.27\n    unit: \"%\"\n  - quantity: increase with ST only\n    value: 18.89\n    tolerance: 1.89\n    unit: \"%\"\n  - quantity: decrease without RF\n    value: 14.79\n    tolerance: 1.48\n    unit: \"%\"\n  - quantity: decrease without FF\n    value: 59.38\n    tolerance: 5.94\n    unit: \"%\"\n  - quantity: decrease without ST\n    value: 7.87\n    tolerance: 0.79\n    unit: \"%\"\n  criterion: >-\n    From the slopes of fig5c-source-contributions, by the formulas of Methods, The\n    perisaccadic to fixation performance ratio analysis, paragraph 4 (increase = (+X minus\n    no-source) over (F minus no-source); decrease = (-X minus F) over (no-source minus F)),\n    tolerance 10%. Reproduced when FF has the largest increase and the largest decrease and\n    at least four of the six values are within tolerance; partially reproduced when the FF\n    ordering holds with fewer.\n- id: fig6a-model-saccadic-suppression\n  statement: The model reproduces saccadic suppression in 7 of the 8 suppressed neurons; for\n    them the recorded normalized early response drops from 2.48 to 1.38 and the predicted one\n    from 1.59 to 1.06.\n  source: Results, The model captures the spatial and temporal characteristics of the\n    perisaccadic effects, paragraph 2; Figure 6A\n  quote: >-\n    For this subpopulation, the average normalized response over the early response window\n    dropped from 2.48 ± 0.42 to 1.38 ± 0.30 (mean ± SE), and the average predicted firing\n    rate over the same response window decreased from 1.59 ± 0.16 to 1.06 ± 0.09 (mean ±\n    SE).\n  data: with_labels\n  depends_on:\n  - fig1b-saccadic-suppression\n  expected:\n  - quantity: neurons with suppression in both response and A-model\n    value: 7\n    tolerance: 0.7\n  - quantity: recorded normalized early response, fixation\n    value: 2.48\n    tolerance: 0.42\n  - quantity: recorded normalized early response, perisaccadic\n    value: 1.38\n    tolerance: 0.3\n  - quantity: predicted normalized early response, fixation\n    value: 1.59\n    tolerance: 0.16\n  - quantity: predicted normalized early response, perisaccadic\n    value: 1.06\n    tolerance: 0.09\n  criterion: >-\n    A-model per neuron (D4; ten fits on 65% subsets, Gaussian parameters averaged; the\n    code's kernel average as a variant). Model classification by D6 (O6 a main, b variant),\n    recorded classification by D2 under the reading that reproduced fig1b-saccadic-suppression.\n    Recorded values by D3 and O4 a (early window); predicted values normalized the same way\n    on predicted rates (Methods, Statistical analysis of model predictions, paragraph 2).\n    Reproduced when the count and at least three of the four values are within tolerance,\n    with decreases in both recorded and predicted values; partially reproduced when both\n    decreases hold and the count is at least half of the recorded suppressed neurons.\n- id: fig6b-model-ff-remapping\n  statement: The model reproduces FF-remapping in 20 of the 23 remapping neurons; for them the\n    recorded normalized late FF response rises from 0.89 to 1.36 and the predicted one from\n    0.93 to 1.19.\n  source: Results, The model captures the spatial and temporal characteristics of the\n    perisaccadic effects, paragraph 2; Figure 6B\n  quote: >-\n    For this subpopulation, the average normalized response over the late response window\n    increased from 0.89 ± 0.03 to 1.36 ± 0.08 (mean ± SE), and the average normalized\n    predicted firing rate over the same response window increased from 0.93 ± 0.02 to 1.19 ±\n    0.04 (mean ± SE).\n  data: with_labels\n  depends_on:\n  - fig1c-ff-remapping\n  expected:\n  - quantity: neurons with FF-remapping in both response and A-model\n    value: 20\n    tolerance: 2\n  - quantity: recorded normalized late FF response, fixation\n    value: 0.89\n    tolerance: 0.03\n  - quantity: recorded normalized late FF response, perisaccadic\n    value: 1.36\n    tolerance: 0.08\n  - quantity: predicted normalized late FF response, fixation\n    value: 0.93\n    tolerance: 0.02\n  - quantity: predicted normalized late FF response, perisaccadic\n    value: 1.19\n    tolerance: 0.04\n  criterion: >-\n    As fig6a-model-saccadic-suppression, for FF-remapping with the late window. Same rule,\n    with increases in place of decreases.\n- id: fig6c-model-st-remapping\n  statement: The model reproduces ST-remapping in 24 of the 37 remapping neurons; for them the\n    recorded normalized late ST response rises from 0.79 to 1.48 and the predicted one from\n    0.92 to 1.19.\n  source: Results, The model captures the spatial and temporal characteristics of the\n    perisaccadic effects, paragraph 2; Figure 6C\n  quote: >-\n    For this subpopulation, the average normalized response over the late response window\n    increased from 0.79 ± 0.03 to 1.48 ± 0.07 (mean ± SE), and the average normalized\n    predicted firing rate over the same response window increased from 0.92 ± 0.02 to 1.19 ±\n    0.04 (mean ± SE).\n  data: with_labels\n  depends_on:\n  - fig1d-st-remapping\n  expected:\n  - quantity: neurons with ST-remapping in both response and A-model\n    value: 24\n    tolerance: 2.4\n  - quantity: recorded normalized late ST response, fixation\n    value: 0.79\n    tolerance: 0.03\n  - quantity: recorded normalized late ST response, perisaccadic\n    value: 1.48\n    tolerance: 0.07\n  - quantity: predicted normalized late ST response, fixation\n    value: 0.92\n    tolerance: 0.02\n  - quantity: predicted normalized late ST response, perisaccadic\n    value: 1.19\n    tolerance: 0.04\n  criterion: >-\n    As fig6b-model-ff-remapping, for the ST probe. Same rule.\n- id: fig6d-model-ff-and-st-remapping\n  statement: The model reproduces both remapping effects in 17 of the 22 neurons that show\n    both; for them recorded FF and ST responses rise from 0.88 to 1.43 and 0.78 to 1.56, and\n    predicted ones from 0.92 to 1.22 and 0.91 to 1.23.\n  source: Results, The model captures the spatial and temporal characteristics of the\n    perisaccadic effects, paragraph 2; Figure 6D\n  quote: >-\n    For this subpopulation, the average normalized response to FF and ST stimuli over the\n    late response window increased from 0.88 ± 0.03 to 1.43 ± 0.09 (mean ± SE) and from 0.78\n    ± 0.04 to 1.56 ± 0.09 (mean ± SE) respectively, and the average predicted firing rate in\n    response to FF and ST stimuli over the same response window increased from 0.92 ± 0.02 to\n    1.22 ± 0.05 (mean ± SE) and from 0.91 ± 0.02 to 1.23 ± 0.06 (mean ± SE) respectively.\n  data: with_labels\n  depends_on:\n  - fig1e-ff-and-st-remapping\n  - fig6b-model-ff-remapping\n  - fig6c-model-st-remapping\n  expected:\n  - quantity: neurons with both effects in both response and A-model\n    value: 17\n    tolerance: 1.7\n  - quantity: recorded normalized late FF response, fixation\n    value: 0.88\n    tolerance: 0.03\n  - quantity: recorded normalized late FF response, perisaccadic\n    value: 1.43\n    tolerance: 0.09\n  - quantity: recorded normalized late ST response, fixation\n    value: 0.78\n    tolerance: 0.04\n  - quantity: recorded normalized late ST response, perisaccadic\n    value: 1.56\n    tolerance: 0.09\n  - quantity: predicted normalized late FF response, fixation\n    value: 0.92\n    tolerance: 0.02\n  - quantity: predicted normalized late FF response, perisaccadic\n    value: 1.22\n    tolerance: 0.05\n  - quantity: predicted normalized late ST response, fixation\n    value: 0.91\n    tolerance: 0.02\n  - quantity: predicted normalized late ST response, perisaccadic\n    value: 1.23\n    tolerance: 0.06\n  criterion: >-\n    Neurons with both effects in both the response and the model, by the readings of\n    fig6b-model-ff-remapping and fig6c-model-st-remapping. Reproduced when the count and at\n    least six of the eight values are within tolerance, with all four increases; partially\n    reproduced when all increases hold with fewer values in tolerance.\n- id: fig6-example-neuron-predictions\n  statement: For the example neurons of Fig 1 the model-predicted rates show the same\n    effects; the early RF rate falls from 22.69 to 15.72 spk/s, the late FF rate rises from\n    8.01 to 11.64, the late ST rate from 24.53 to 47.24, and in the neuron with both effects\n    FF from 17.39 to 32.12 and ST from 15.85 to 33.11 spk/s.\n  source: Results, The model captures the spatial and temporal characteristics of the\n    perisaccadic effects, paragraph 2; Figure 6A to 6D, top panels\n  quote: >-\n    For this neuron, the average model-predicted firing rate over the early response window\n    (50–75 ms after stimulus onset) in response to an RF stimulus dropped from 22.69 ± 0.78\n    (mean ± SE) spk/s during fixation to 15.72 ± 1.72 (mean ± SE) spk/s when the stimulus\n    appeared just prior to saccade onset (example neuron, p < 0.001).\n  statistics:\n  - about: each of the five example-neuron comparisons\n    test: one-sided Wilcoxon rank-sum test (Methods, Statistical analysis of model predictions)\n    p: 0.001\n    p_relation: \"<\"\n  data: with_labels\n  depends_on:\n  - fig1-example-neurons\n  expected:\n  - quantity: example neuron, predicted early RF rate, fixation\n    value: 22.69\n    tolerance: 0.78\n    unit: spk/s\n  - quantity: example neuron, predicted early RF rate, perisaccadic\n    value: 15.72\n    tolerance: 1.72\n    unit: spk/s\n  - quantity: example neuron, predicted late FF rate, fixation\n    value: 8.01\n    tolerance: 0.06\n    unit: spk/s\n  - quantity: example neuron, predicted late FF rate, perisaccadic\n    value: 11.64\n    tolerance: 0.36\n    unit: spk/s\n  - quantity: example neuron, predicted late ST rate, fixation\n    value: 24.53\n    tolerance: 0.39\n    unit: spk/s\n  - quantity: example neuron, predicted late ST rate, perisaccadic\n    value: 47.24\n    tolerance: 2.25\n    unit: spk/s\n  - quantity: example neuron with both effects, predicted late FF rate, fixation\n    value: 17.39\n    tolerance: 0.38\n    unit: spk/s\n  - quantity: example neuron with both effects, predicted late FF rate, perisaccadic\n    value: 32.12\n    tolerance: 2.5\n    unit: spk/s\n  - quantity: example neuron with both effects, predicted late ST rate, fixation\n    value: 15.85\n    tolerance: 0.36\n    unit: spk/s\n  - quantity: example neuron with both effects, predicted late ST rate, perisaccadic\n    value: 33.11\n    tolerance: 1.98\n    unit: spk/s\n  criterion: >-\n    On the neurons fig1-example-neurons matched, the A-model's predicted rates (D6, O6 a\n    main), SE across presentations. The paper's SE for model predictions depends on its\n    random sequences and fits; the direction and a significant one-sided rank-sum test are\n    the main test. Reproduced when, for each matched example, the change has the paper's\n    direction with p < 0.05 and at least one of its two values is within tolerance; partially\n    reproduced when the direction and the test hold for all examples but values do not; not\n    testable when fig1-example-neurons matched no neuron.\n- id: fig7-prevalence-maps-correlate\n  statement: The model-predicted maps of how many neurons show each effect, over time from\n    saccade and from stimulus onset, correlate with the recorded maps (r = 0.65 for\n    suppression, 0.60 for FF-remapping, 0.62 for ST-remapping, each p < 0.001).\n  source: Results, The model captures the spatial and temporal characteristics of the\n    perisaccadic effects, paragraph 3; Figure 7\n  quote: >-\n    Strong correlations between the experimental and model-predicted values confirmed the\n    model ability to replicate the timing and frequency of occurrence of effects across the\n    population (saccadic suppression, r = 0.65, p < 0.001; FF-remapping, r = 0.60, p < 0.001;\n    and ST-remapping = 0.62, p < 0.001; Pearson product-moment correlation).\n  statistics:\n  - about: saccadic suppression\n    test: Pearson product-moment correlation\n    statistic: r = 0.65\n    p: 0.001\n    p_relation: \"<\"\n  - about: FF-remapping\n    test: Pearson product-moment correlation\n    statistic: r = 0.60\n    p: 0.001\n    p_relation: \"<\"\n  - about: ST-remapping\n    test: Pearson product-moment correlation\n    statistic: r = 0.62\n    p: 0.001\n    p_relation: \"<\"\n  data: with_labels\n  depends_on:\n  - fig6a-model-saccadic-suppression\n  - fig6b-model-ff-remapping\n  - fig6c-model-st-remapping\n  expected:\n  - quantity: r, saccadic suppression maps\n    value: 0.65\n    tolerance: 0.065\n  - quantity: r, FF-remapping maps\n    value: 0.6\n    tolerance: 0.06\n  - quantity: r, ST-remapping maps\n    value: 0.62\n    tolerance: 0.062\n  criterion: >-\n    Methods, Prevalence of the perisaccadic effects. For each neuron with the effect in both\n    response and model (from the fig6 claims), and each time t from saccade and latency tau,\n    m(t, tau) is 1 when rates at latency tau after probes at the effect's location shown at t\n    differ from rates at tau after the same probe shown -500 to -100 ms, in the effect's\n    direction, by a one-sided Wilcoxon rank-sum test at p < 0.05 (the indicator equation is\n    lost; this is the reading of its text), else 0; the map is the percentage of neurons\n    with 1. Recorded rates are spike trains smoothed with a Gaussian of FWHM 33 ms; model rates\n    the A-model's predicted rates (D6). Open, with readings. The grid of t and tau, (a) 1 ms\n    steps, (b) 7 ms steps (one probe duration); the pixels correlated, (a) all t of the model\n    span (-540 to 540 ms, get_info.m) and tau 1 to 150 ms, (b) t from -50 to 150 ms (the\n    perisaccadic stimulus and spike windows of Methods, Model evaluation) and tau 1 to 150 ms.\n    Pearson r across pixels. Reproduced when, under one combination of readings, all three\n    r are within tolerance and p < 0.001; partially reproduced when all three are positive\n    with p < 0.001 but one or more is outside tolerance.\n- id: fig7-experimental-maps-lower\n  statement: The recorded prevalence maps have lower values than the model-predicted maps,\n    because smoothed recorded rates are more variable and fewer comparisons reach\n    significance.\n  source: Results, The model captures the spatial and temporal characteristics of the\n    perisaccadic effects, paragraph 3; Figure 7A and 7B\n  quote: >-\n    This high variability means that fewer effects reach statistical significance, as\n    reflected in the low values of the experimental maps in comparison with the\n    model-predicted ones.\n  data: with_labels\n  depends_on:\n  - fig7-prevalence-maps-correlate\n  criterion: >-\n    On the maps of fig7-prevalence-maps-correlate, under the reading it reproduced with (or\n    reading a when none did). Reproduced when, for each of the three effects, the mean over\n    pixels of the recorded map is below that of the model map; partially reproduced for two\n    of the three.\n- id: fig8c-example-neuron-detectability\n  statement: In an example neuron, detectability of RF probes at ~60 ms latency is lost ~60 ms\n    after the saccade; at about the same time FF and ST probes become detectable at ~100 ms\n    latency, and from ~100 ms after the saccade the new RF (former FF) is detected at ~60 ms\n    latency.\n  source: Results, The model produces predictions about the time course and contribution of\n    perisaccadic modulatory sources to the neuron's instantaneous firing rate, paragraph 4;\n    Figure 8C\n  quote: >-\n    The neuron can detect stimuli presented in the RF location with a latency of ~60 ms; it\n    loses its ability to detect stimuli in the original RF location after the saccade (~60 ms\n    after saccade onset).\n  data: with_labels\n  depends_on:\n  - fig6b-model-ff-remapping\n  - fig6c-model-st-remapping\n  criterion: >-\n    The example neuron is not identified. Detectability by Methods, Spatiotemporal\n    detectability analysis. 1000 sequences to the A-model (O6 a main), simulated history\n    (ref [73]); for each probe, time t and latency tau, the AUC between predicted rates at t\n    after a probe at that location at t - tau and the same rates paired with trial-shuffled\n    stimuli; significance by a two-sample t-test of the AUC against 100 AUCs between two\n    shuffled distributions, p < 1e-9. Candidates are the neurons with both FF- and\n    ST-remapping in response and model. Reproduced when at least one candidate shows, by\n    significant detectability with peak at latency over 50 ms: RF peak latency 50-75 ms\n    before the saccade, RF detectability ending between 30 and 100 ms after saccade onset, FF\n    and ST peak latencies of 80 to 130 ms around that time, and FF detected at 50-75 ms\n    latency from about 100 ms after the saccade. Partially reproduced when a candidate shows\n    the RF loss and the long-latency FF or ST detection but not all four. The tolerance on\n    the \"~\" times (plus or minus about 30 ms) is fixed here and is a reading of \"~\".\n- id: fig8d-equal-detectability-at-55ms\n  statement: For the example neuron 55 ms after the saccade, FF and ST probes reach peak\n    detectability at longer latencies than the RF probe but with nearly equal peak values.\n  source: Results, The model produces predictions about the time course and contribution of\n    perisaccadic modulatory sources to the neuron's instantaneous firing rate, paragraph 4;\n    Figure 8D\n  quote: >-\n    As seen, peak detectability at the FF and ST locations occurs at longer latencies than\n    peak detectability for the RF location; however, peak detectability values for the FF\n    and ST locations are nearly equal to the original RF.\n  data: with_labels\n  depends_on:\n  - fig8c-example-neuron-detectability\n  criterion: >-\n    On the neuron fig8c-example-neuron-detectability matched, at t = 55 ms after saccade\n    onset (Figure 8C legend), the latency and AUC at peak over tau for the RF, FF and ST\n    probes. \"Nearly equal\" is not quantified in the paper; read here as FF and ST peak AUC\n    within 10% of the RF peak AUC above chance (AUC minus 0.5). Reproduced when both FF and ST\n    peak later than RF and both are nearly equal by that reading; partially reproduced when\n    the latency order holds only. Not testable when no neuron matched.\n- id: fig8e-example-neuron-time-course\n  statement: The example neuron detects FF probes at ~90 ms latency from ~65 ms before the\n    saccade, loses them 25 ms later, detects them again from ~13 ms after the saccade for ~60\n    ms, and detects ST probes at ~130 ms latency from 66 to 130 ms after the saccade.\n  source: Results, The model produces predictions about the time course and contribution of\n    perisaccadic modulatory sources to the neuron's instantaneous firing rate, paragraph 5;\n    Figure 8E, left\n  quote: >-\n    Next, ~65 ms before the saccade, the neuron can also detect stimuli presented at the FF\n    location ~90 ms earlier (blue circles). This ability to detect FF stimuli disappears 25\n    ms later, then reemerges ~13 ms after the saccade (with a latency of ~80–100 ms) and\n    persists for ~60 ms.\n  data: with_labels\n  depends_on:\n  - fig8c-example-neuron-detectability\n  criterion: >-\n    On the neuron fig8c-example-neuron-detectability matched, the maximum significant\n    detectability over tau (only peaks at tau over 50 ms) and its latency at each t, smoothed\n    over t with a 7 ms moving average (Methods, Spatiotemporal detectability analysis,\n    paragraph 2), for the RF, FF and the probe closest to the ST. Reproduced when the FF and ST\n    epochs and latencies quoted match within about 30 ms (the reading of \"~\" of\n    fig8c-example-neuron-detectability); partially reproduced when the post-saccadic FF\n    epoch and the ST epoch match but the presaccadic FF epoch does not. Not testable when no\n    neuron matched.\n- id: fig8e-population-ff-detectability\n  statement: A synthetic neuron built from the FF-remapping subpopulation detects FF probes at\n    60-90 ms latency from ~50 ms before to ~60 ms after the saccade, after which the FF latency\n    returns to ~60 ms, the FF having become the new RF.\n  source: Results, The model produces predictions about the time course and contribution of\n    perisaccadic modulatory sources to the neuron's instantaneous firing rate, paragraph 6;\n    Figure 8E, middle\n  quote: >-\n    From ~50 ms before to ~60 ms after a saccade, the population can detect FF stimuli with\n    latencies of ~60–90 ms, indicating that the neural population is detecting stimuli\n    appearing in the FF ~140 to ~0 ms before the saccade.\n  data: with_labels\n  depends_on:\n  - fig6b-model-ff-remapping\n  criterion: >-\n    Methods, Spatiotemporal detectability analysis, paragraph 4. The A-model Gaussian\n    parameters and c of the neurons with FF-remapping in both response and model, centres\n    taken relative to the FF probe and spreads in units of probe spacing (the code's\n    parameters are already in grid units, fmodel.m), averaged; a synthetic neuron with only\n    the FF Gaussian (RF and ST amplitudes zero), detectability as\n    fig8c-example-neuron-detectability with significance p < 1e-7. Which fixation kernel,\n    post-spike and offset kernels, b0 and r_max the synthetic neuron uses is not stated.\n    Readings, (a) the averages of those of the same neurons, (b) the fixation kernel set to\n    zero and the rest averaged. Reproduced when, under one reading, significant FF\n    detectability at 55 to 100 ms latency spans from 20 to 80 ms before to 30 to 90 ms after\n    the saccade, and the latency is 50-75 ms after that; partially reproduced when the\n    long-latency epoch holds and the return to short latency does not.\n- id: fig8e-population-st-detectability\n  statement: A synthetic neuron built from the ST-remapping subpopulation detects ST probes at\n    long latencies (~100-120 ms) from 45 ms before to 15 ms after the saccade and again from 74\n    to 114 ms after it.\n  source: Results, The model produces predictions about the time course and contribution of\n    perisaccadic modulatory sources to the neuron's instantaneous firing rate, paragraph 6;\n    Figure 8E, right\n  quote: >-\n    Similar to the FF-remapping effect, the population can detect ST stimuli at longer\n    latencies (~100–120 ms) from 45 before to 15 ms after a saccade and from 74 to 114 ms\n    after a saccade.\n  data: with_labels\n  depends_on:\n  - fig6c-model-st-remapping\n  criterion: >-\n    As fig8e-population-ff-detectability, with the ST Gaussian only, for the neurons with\n    ST-remapping in both response and model. Reproduced when, under one reading, significant\n    ST detectability at 90 to 130 ms latency occurs in two epochs within about 30 ms of\n    -45 to 15 ms and 74 to 114 ms from saccade onset; partially reproduced when one of the two\n    epochs matches.\n- id: figs4-f-model-share-of-s-model\n  statement: The F-model reaches about 60% of the S-model's performance in Delta LL per spike.\n  source: S4 Fig legend\n  quote: >-\n    The F-model, despite being based on an approximation of the S-model, has a performance of\n    the order of ~60% of the performance of the S-model, in terms of Δ LL / spk (see Fig 5A\n    ).\n  depends_on:\n  - fig5a-s-model-perisaccadic-better\n  - fig5a-f-model-perisaccadic-better\n  data: with_labels\n  expected:\n    quantity: F-model Delta LL per spike as a share of the S-model's\n    value: 60\n    tolerance: 6\n    unit: \"%\"\n  criterion: >-\n    The ratio of the mean F-model to the mean S-model Delta LL per spike over the 41 neurons\n    from the fig5a claims. Which period is meant is not stated; readings, (a) fixation, (b)\n    perisaccadic, (c) the two pooled. Reproduced when one reading is within tolerance.\n- id: figs5-spike-history-no-effect\n  statement: Using simulated or no spike history in place of the true history does not\n    change the S-model's performance significantly in either period, and the S-model with\n    either still predicts perisaccadic spikes better than fixation spikes.\n  source: S5 Fig legend, panels B and C\n  quote: >-\n    There is no significant difference between the results obtained from the true-history\n    model, the simulated-history model, and the no-history model.\n  statistics:\n  - about: true against no history, fixation (0.24 against 0.23 bits/spk)\n    test: Wilcoxon signed-rank test\n    p: 0.98\n    n: 41 neurons\n  - about: true against no history, perisaccadic (0.30 against 0.30 bits/spk)\n    test: Wilcoxon signed-rank test\n    p: 0.87\n    n: 41 neurons\n  - about: true against simulated history, fixation (0.24 against 0.23 bits/spk)\n    test: Wilcoxon signed-rank test\n    p: 0.48\n    n: 41 neurons\n  - about: true against simulated history, perisaccadic (0.30 against 0.29 bits/spk)\n    test: Wilcoxon signed-rank test\n    p: 0.99\n    n: 41 neurons\n  - about: no history, perisaccadic against fixation\n    test: Wilcoxon signed-rank test\n    p: 0.001\n    p_relation: \"<\"\n    n: 41 neurons\n  - about: simulated history, perisaccadic against fixation\n    test: Wilcoxon signed-rank test\n    p: 0.001\n    p_relation: \"<\"\n    n: 41 neurons\n  depends_on:\n  - fig5a-s-model-perisaccadic-better\n  expected:\n  - quantity: no-history S-model Delta LL per spike, fixation\n    value: 0.23\n    tolerance: 0.02\n    unit: bits/spk\n  - quantity: no-history S-model Delta LL per spike, perisaccadic\n    value: 0.3\n    tolerance: 0.02\n    unit: bits/spk\n  - quantity: simulated-history S-model Delta LL per spike, fixation\n    value: 0.23\n    tolerance: 0.02\n    unit: bits/spk\n  - quantity: simulated-history S-model Delta LL per spike, perisaccadic\n    value: 0.29\n    tolerance: 0.02\n    unit: bits/spk\n  criterion: >-\n    The fitted S-model of fig5a-s-model-perisaccadic-better evaluated on the same test\n    trials with the history term removed (no history) or with history simulated by drawing\n    spikes from the model rate step by step (ref [73], algorithm 2; the code's make_result.m\n    make_resp), D5 and O5 as in that claim. The no-difference parts are claims of absence on\n    the paper's test, a Wilcoxon signed-rank test over 41 neurons at p < 0.05. Reproduced when\n    none of the four true-against-other tests is significant and both perisaccadic-against-\n    fixation tests are significant with perisaccadic higher; not reproduced when any of the\n    four finds a difference. The means are reported against the expected values.\n- id: figs1-rf-centres\n  statement: In leftward-saccade sessions the RF centres lie on average 5.81 dva right and\n    5.23 dva below fixation; in rightward-saccade sessions 6.49 dva left and 7.44 dva below.\n  source: S1 Fig legend, panel B\n  quote: >-\n    In the sessions where the saccades were made to the left, the average center of the\n    receptive fields was 5.81 ± 3.63 (mean ± SD) dva rightward, and 5.23 ± 2.08 (mean ± SD)\n    dva downward.\n  data: with_inputs\n  expected:\n  - quantity: RF centre, leftward sessions, horizontal (rightward)\n    value: 5.81\n    tolerance: 0.58\n    unit: dva\n  - quantity: RF centre, leftward sessions, vertical (downward)\n    value: 5.23\n    tolerance: 0.52\n    unit: dva\n  - quantity: RF centre, rightward sessions, horizontal (leftward)\n    value: 6.49\n    tolerance: 0.65\n    unit: dva\n  - quantity: RF centre, rightward sessions, vertical (downward)\n    value: 7.44\n    tolerance: 0.74\n    unit: dva\n  criterion: >-\n    RF maps from responses to each probe shown 700 to 140 ms before saccade, 50-70 ms after\n    onset, interpolated by a factor of 1000, centre of the contour at 95% of the maximum (S1\n    Fig legend; centre taken as the centroid of the region above 95%, a standard choice).\n    Converting grid positions to dva needs each session's grid position and spacing, which\n    the dataset's description does not list; they are outside inputs (the paper gives only\n    their ranges, Methods paragraph 1). The SDs given are spreads across neurons, not\n    uncertainties of the mean, so the tolerance is 10%. Reproduced when all four values are\n    within tolerance; blocked when the grid geometry cannot be found.\n"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  python tools/claims_check.py claims/niknam-2019.yaml paper/10.1371-journal.pcbi.1007275.txt; python - <<'E'
import yaml,json,jsonschema,re
d=yaml.safe_load(open('claims/niknam-2019.yaml'))
jsonschema.validate(d,json.load(open('schemas/claims.schema.json')))
print(len(d['claims']), sum('quote' in c for c in d['claims']), sum('statistics' in c for c in d['claims']), sum('criterion' in c for c in d['claims']))
E
grep -n "—\|rather" claims/niknam-2019.yaml; grep -nE "^\s+[a-z_]+: [^>\"].*: " claims/niknam-2019.yaml; grep -nE "^\s{4,}[^ -].*: " claims/niknam-2019.yaml | grep -v "^\S*\s*- \|quantity\|value\|tolerance\|unit\|test\|about\|p\b\|n:" | head
```

Result: not kept, because it reads the paper's text.

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
?? claims/niknam-2019.yaml
?? scripts
```

**Agent**

I wrote `claims/niknam-2019.yaml`. It passes the quote checker (34 claims, 33 quotes, 0 problems) and the claims schema. Nothing is committed.

**Text read.** The version of record (PMC6759185, Europe PMC full-text XML) was used. It includes the Methods, all figure legends, and the legends for S1–S6 Fig and S1–S3 Movie. There was no PDF, so no figure could be read. The supplement figures exist only as legends, but every number the claims use is in the Results or a legend.

**Code read.** github.com/nnategh/SFA-Models at commit 1438dde. It contains the S-, F- and A-model fits, the ΔLL/spk calculation, and `main_lists.mat`, which lists each neuron's RF, FF and ST probe. It has no code for the N-model, any statistical test, the partial models, the prevalence maps or the ROC detectability analysis.

**Claims.**
- **34 claims:** 1 link claim (the code's RF/FF/ST probe list checked against the dataset) and 33 findings. All 33 findings have quotes.
- **12 claims have statistics**, 28 entries in total: Wilcoxon signed-rank and rank-sum tests, one-tailed mid-P McNemar tests, and Pearson correlations.
- **All 34 have a criterion.** 30 have expected values; the tolerance is the paper's SE where it gives one and 10% otherwise.
- **Coverage:** Fig 1 (effect counts and normalized responses, latency, example neurons), Fig 3, Fig 5A–C, Fig 6A–D plus its example neurons, Fig 7 (two claims), Fig 8C/D/E, S1, S4 and S5, and the neuron counts from the Methods.
- **Data:** most claims are `with_labels`, because they need the RF/FF/ST probes from the code repository. The S1 claim (RF centres in dva) is `with_inputs`, because it needs each session's grid geometry, which the dataset description does not list.

**Open details and the readings named for each.** These are O1–O8 in the opening comment, plus a few within single claims.
- **O1, pairing for the signed-rank test on recorded data:** per trial, per condition, or an unpaired rank-sum test.
- **O2, what counts as a presentation:** the onset millisecond of each probe (the Methods), or every millisecond the probe is on (what the code does, kept as a variant).
- **O3, RF/FF/ST probes:** the code's `probe_list`, or recomputed from the Methods. Only RF can be recomputed from the dataset alone.
- **O4, subpopulation normalized value:** the mean over the effect's response window, or the peak of the smoothed curve.
- **O5, NULL model for ΔLL/spk:** the session mean rate or the mean rate over test trials. The code's `get_fr0` (offset and post-spike kernels only) is a variant.
- **O6, the 1000 stimulus sequences:** resampled recorded conditions, or new pseudorandom sequences.
- **O7, nulling a source in the partial F-models:** a fixation-period time drawn per time point, or one drawn per model.
- **Code that disagrees with the Methods:** the code averages kernels for the A-model and makes only one fit; I followed the Methods (ten fits, averaged Gaussian parameters). The code fixes r_max at 1000 spk/s, which I followed because the Methods don't say how the empirical maximum is measured. The 1.5 SD parameter-selection threshold comes from the code, because the equation for it was lost.
- **Fig 7 maps:** the time grid (1 ms or 7 ms steps) and which pixels are correlated (the full model span, or −50 to 150 ms around the saccade).
- **Fig 8 synthetic neurons:** whether the kernels the paper doesn't state are averaged over neurons or the fixation kernel is set to zero.
- **S4:** which period the "~60%" refers to (fixation, perisaccadic, or both pooled).
- **Example neurons (Figs 1, 6, 8):** the paper doesn't identify them, so each criterion searches all 41 neurons for a match.

**Missing from the paper.**
- **The reference list** is absent from the text. So ref [48] (the N-model), [49] (the McNemar mid-P test) and [73] (Chen et al., algorithm 2) are known only by number. The N-model is not described in this paper and is not in the code, so the 5 claims comparing against it (2 on Fig 5A, 3 on Fig 5B) depend on finding ref [48] (O8). If it can't be found, they are blocked.
- **All displayed equations** were lost in extraction. That includes Eq 10, the classification measures, and the prevalence-map indicator; I read these from the surrounding text and the code's README.
- **Grid geometry in dva** is not among the dataset's listed variables, which the S1 claim needs.

One typo in the paper: it prints "F-model vs. N-model" twice in the Fig 5B sentences, and I read the third comparison as the A-model.

## End of run

26 turns, 7 minutes, $2.50 at API prices, result: success.
