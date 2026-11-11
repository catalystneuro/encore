# niknam-2019 · claims-check · run 42936492107

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  ls paper/; cat claims/niknam-2019.yaml; python tools/claims_check.py claims/niknam-2019.yaml paper/*.txt; sed -n '/Reader/,/^## /p' docs/protocol.md | head -80
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  python tools/claims_check.py claims/niknam-2019.yaml paper/10.1371-journal.pcbi.1007275.txt | tail -20; wc -l claims/niknam-2019.yaml paper/*.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "claims/niknam-2019.yaml"
}
```

```
1	# Claims for Niknam, Akbarian, Clark, Zamani, Noudoost & Nategh (2019), "Characterizing and
2	# dissociating multiple time-varying modulatory computations influencing neuronal activity",
3	# PLoS Comput Biol, doi:10.1371/journal.pcbi.1007275, tested on CRCNS:mt-3.
4	# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"),
5	# 2026-11-11, protocol pilot-14 as stated in docs/protocol.md.
6	#
7	# Text read. paper/10.1371-journal.pcbi.1007275.txt, the version of record (PMC6759185, open
8	# access, Europe PMC full-text XML flattened). It holds the abstract, Introduction, Results,
9	# Discussion, Methods, the legends of Figures 1 to 8, the legends of S1 to S6 Fig and S1 to S3
10	# Movie, and the Data Availability statement. No PDF was supplied, so no figure could be read.
11	# The supplement figures themselves are not in the text, only their legends; the numbers the
12	# results rest on are in the Results text and the legends, so the supplement's absence does not
13	# block a claim. Lost in extraction: every displayed equation (Eqs 1 to 14, including the
14	# parameter-selection threshold, Eq 10; the classification measures of the dichotomous analysis;
15	# the prevalence-map indicator m(t, tau); the maximum-detectability definition) and the whole
16	# reference list, so ref [48] (the N-model), ref [49] (the McNemar mid-P test) and ref [73]
17	# (Chen et al., algorithm 2) are known only by number.
18	#
19	# Code. https://github.com/nnategh/SFA-Models, commit 1438dde9dd3207348ec0df1e5c4dd2a7b014e68e
20	# (2019-12-20), linked in Methods (A-model framework) and Data Availability. MATLAB. It holds
[... 1009 more lines not kept]
```

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
 "file_path": "claims/niknam-2019.yaml",
 "offset": 1029
}
```

**Agent calls Read**

```json
{
 "file_path": "paper/10.1371-journal.pcbi.1007275.txt",
 "offset": 126
}
```

```
1029	    perisaccadic effects, paragraph 3; Figure 7A and 7B
1030	  quote: >-
1031	    This high variability means that fewer effects reach statistical significance, as
1032	    reflected in the low values of the experimental maps in comparison with the
1033	    model-predicted ones.
1034	  data: with_labels
1035	  depends_on:
1036	  - fig7-prevalence-maps-correlate
1037	  criterion: >-
1038	    On the maps of fig7-prevalence-maps-correlate, under the reading it reproduced with (or
1039	    reading a when none did). Reproduced when, for each of the three effects, the mean over
1040	    pixels of the recorded map is below that of the model map; partially reproduced for two
1041	    of the three.
1042	- id: fig8c-example-neuron-detectability
1043	  statement: In an example neuron, detectability of RF probes at ~60 ms latency is lost ~60 ms
1044	    after the saccade; at about the same time FF and ST probes become detectable at ~100 ms
1045	    latency, and from ~100 ms after the saccade the new RF (former FF) is detected at ~60 ms
1046	    latency.
1047	  source: Results, The model produces predictions about the time course and contribution of
1048	    perisaccadic modulatory sources to the neuron's instantaneous firing rate, paragraph 4;
[... 233 more lines not kept]
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1371-journal.pcbi.1007275.txt",
 "offset": 126,
 "limit": 100
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1371-journal.pcbi.1007275.txt",
 "offset": 226,
 "limit": 80
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  sed -n '306,481p' paper/10.1371-journal.pcbi.1007275.txt | cut -c1-1500 | grep -v '^$' | grep -v 'additional data file' | awk '!seen[$0]++'
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  grep -n -i -E 'tolerance|threshold|claim of absence|two-sided|one-sided|checks|ready' docs/protocol.md | head -80
```

```
14:  and how each is to be tested, taken from the paper. A second reader checks
21:- The **verifier** checks the author's work and must not be the author.
100:     numbers the attempt must match, with tolerances, stay in `expected`.
101:     Record only tests whose result is the finding. A significance threshold
106:   - `expected`: each reported number the claim rests on, with a tolerance.
110:     widened by 10% of each bound. Give the reason for any other tolerance.
122:     bins, thresholds, what a measure is compared with) is taken from the
137:   - For a claim of absence ("no difference", "did not change"), the
138:     criterion names the test and threshold the paper used. The claim is
175:A second reader, in a separate run, checks the claims file against the paper:
179:the paper's and are results, not thresholds; that every part of every
182:show is wrong, and records each change, with its reason, under `checks` at
183:the end of the file. A claims file is ready for an attempt when its last check
192:takes it from the paper. The reader, who has not seen the data, checks each
212:it got, then write the attempt record and run the entry's checks. A record
246:     dataset already holds, such as stimulus names for its stimulus codes.
251:     claims are the registry's checks, not findings of the paper, so the
308:   a window, a threshold, what a measure is compared with), take it from the
414:   - When a threshold or criterion is a choice, show how the result changes
438:near a threshold can move when a random split changes.
[... 4 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 85,200p docs/protocol.md; sed -n 240,260p docs/protocol.md
```

```
reader check the statement against the paper without opening it. For a
     finding shown only in a figure, quote the legend or the sentence of the
     Results that cites the panel.
   - `inferred`: every finding has a quote or, when no sentence of the paper
     states it (numbers only in a table, a result spread over several
     legends), a short note under `inferred` saying so. The statement is
     then a reading of the paper, and the note says what it was
     read from.
   - `statistics`: the statistical support the paper reports for the
     finding, one entry per test or interval: what it compares (`about`,
     when there is more than one), the `test` and `statistic` as named, the
     `p`-value as a number (a bound such as "p < 0.05" is `p: 0.05` with
     `p_relation: "<"`; a printed "P = 0" is recorded as 0), any `corrected`
     for multiple comparisons, a confidence interval (`ci`), and `n` in
     words. It records the paper; the
     numbers the attempt must match, with tolerances, stay in `expected`.
     Record only tests whose result is the finding. A significance threshold
     used to select or count units, cells or pairs ("238 of 288 neurons were
     better fit, p < 0.05") is a method, not a result, and is left out.
     Leave the field out when the paper reports no test or interval for the
[... 117 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n -i -E 'expected|checks|ready|changes' tools/claims_check.py | head -40; grep -l -E '^checks:' claims/*.yaml | head -3
```

```
5:Validates the file against schemas/claims.schema.json, checks every quote word for word
claims/alasfour-2024.yaml
claims/andrews-2024.yaml
claims/armstrong-2026.yaml
```

**Agent calls Bash**

```bash
cd  python -c "
import json;s=json.load(open('schemas/claims.schema.json'));
import pprint
def find(o,k,path=''):
  if isinstance(o,dict):
    for kk,v in o.items():
      if kk==k: print(path+'/'+kk, json.dumps(v)[:600])
      find(v,k,path+'/'+kk)
  elif isinstance(o,list):
    for i,v in enumerate(o): find(v,k,path+f'[{i}]')
find(s,'expected'); find(s,'checks')"; sed -n '/^checks:/,$p' claims/andrews-2024.yaml | head -30
```

```
/properties/claims/items/properties/expected {"description": "The reported numbers the claim rests on, each with a tolerance: one, or a list.", "oneOf": [{"$ref": "#/$defs/expected"}, {"type": "array", "minItems": 1, "items": {"$ref": "#/$defs/expected"}}]}
/$defs/expected {"type": "object", "additionalProperties": false, "required": ["quantity", "value"], "properties": {"quantity": {"type": "string"}, "value": {"type": "number"}, "tolerance": {"type": "number", "minimum": 0}, "unit": {"type": "string"}}}
/properties/checks {"description": "Checks of the claims file against the paper by a second reader (docs/protocol.md, Reader, step 5), oldest first. The file is ready for an attempt when the last says so.", "type": "array", "items": {"type": "object", "additionalProperties": false, "required": ["date", "kind", "ready"], "properties": {"date": {"type": "string", "format": "date"}, "kind": {"enum": ["agent", "person"]}, "model": {"type": "string"}, "by": {"type": "string"}, "ready": {"type": "boolean"}, "changes": {"type": "array", "items": {"type": "string", "minLength": 1}}}}}
checks:
- date: 2026-11-10
  kind: agent
  model: claude-opus-5-5
  ready: true
  changes:
  - fig3a-spontaneous-reduction. The statement said firing "recovers after light-OFF"; the paper does not say so and ST2 gives pre against OFF as significant in 3C (adjusted p 1.26e-13). Now says the OFF rate is higher than the light-ON rate, which is what ST2 and the criterion test.
  - chr2-increase. "returned to baseline" is not in the paper; restated as the Extended Data Fig. 8 test gives it (pre against OFF not significant).
  - zero-mg-isolated-bursts. The paper names two different second slices. Extended Data Fig. 9 shows 10F and 9E; the Extended Data Fig. 5 legend shows isolated bursts in 10F and 11G. The claim fixed 10F and 9E and still cited Extended Data Fig. 5g; both pairs are now readings. Said that the peak thresholds and the 1 minute spacing are not from the paper.
  - fig4-firing-propaga
[... 7 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && timeout 60 git clone -q https://github.com/nnategh/SFA-Models sfa 2>&1 | tail -2; cd sfa 2>/dev/null && git log -1 --format='%H %ad' && ls lib/*
```

```
1438dde9dd3207348ec0df1e5c4dd2a7b014e68e Fri Dec 20 14:28:34 2019 -0700
lib/get:
get_a_knl_stm.m
get_dll.m
get_f_knl_stm.m
get_fr0.m
get_info.m
get_mean_resp.m
get_nonlin_params.m
get_resp.m
get_s_fr.m
get_s_knls.m
get_stim.m

lib/load:
code2stim.m
get_filename.m
get_id.m
load_avg_model.m
load_data.m
[... 43 more lines not kept]
```

**Agent**

Code repo reachable; spot-checking the code settings the opening comment relies on.

**Agent calls Bash**

```bash
cd $TMPDIR/sfa; cat lib/get/get_info.m lib/load/load_trials.m lib/get/get_fr0.m lib/get/get_dll.m; grep -n -i -E 'std|1\.5|sigma' lib/make/make_profile.m | head; grep -n -E 'r_max|rmax|1000|b0' lib/make/select_bases.m lib/nonlin/phi.m | head; grep -n -E 'probe_list|movmean|smooth|ub|lb' lib/models/fmodel.m | head -30
```

```
function [info] = get_info()
    % Get global information
    %
    % Returns
    % -------
    % - info: struct
    %   - width: scaler
    %     Width of the probes' board
    %   - height: scaler
    %     Height of the probes' board
    %   - times: vector
    %     Saccade aligned study times
    %   - num_times: scalar
    %     Number of study times
    %   - num_delays: scalar
    %     Number of delays
    %   - probe_time_resolution: scaler
    %     Duration that a probe is on
    %   - num_folds: scalar
    %     Number of folds
[... 280 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/sfa; sed -n 40,70p lib/models/fmodel.m; sed -n 95,112p lib/models/fmodel.m; grep -n -E 'stim|>|== ' lib/get/get_mean_resp.m | head -20; grep -n -E 'mean|fmodel|knl' lib/models/amodel.m | head
```

```
end

function centers = get_centers(session,channel)
% Get centers of Gaussians

data = load_main_lists();
probes = data.probe_list;

idx = (probes(:,1) == session) & (probes(:,2) == channel);

centers.RF = probes(idx,3:4);
centers.FF = probes(idx,5:6);
centers.ST = probes(idx,7:8);
end

function [] = fit_model(profile,filename)
% Find optimum parameters

info = get_info();
foptions = info.foptions;
[... 44 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/sfa; grep -n 'time_th' lib/models/fmodel.m | head -3; grep -rn 'ind2sub\|sub2ind' lib | head -5
```

```
83:time_th = 100;
101:        if t < time_th
lib/get/get_mean_resp.m:37:probe = sub2ind([width,height],probe(1),probe(2));
lib/make/decide_bases.m:37:        prb = sub2ind(sz,x,y);
lib/make/make_profile.m:34:        index = sub2ind(sz,x,y);
lib/make/make_profile.m:42:            [ip,jp] = ind2sub([size(t_map,1),size(t_map,2)],idx_significant_bases(int_B));
lib/make/fit_model.m:367:        [x,y] = ind2sub([size(stim,2),size(stim,3)],str2double(agenda(4:end)));
Shell cwd was reset to
[... 1 more lines not kept]
```

**Agent**

Code settings in the opening comment match the repository at 1438dde (splits, sigma 1.5, r_max 1000, bounds at t ≥ 100 ms, 10-point smoothing, get_fr0 NULL). Now editing.

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/niknam-2019.yaml",
 "old_string": "#    condition, the same pooled over the trials of each condition; (c) unpaired, all\n#    presentations, one-sided rank-sum, the test the Methods use for model predictions.",
 "new_string": "#    condition, the same pooled over the trials of each condition; (c) unpaired, all\n#    presentations, one-sided rank-sum, the test the Methods use for model predictions. The\n#    Methods name the signed-rank test for recorded responses, so (c) is a variant that is\n#    shown but does not decide an outcome; \"one reading of O1\" below means (a) or (b)."
}
```

```
The file claims/niknam-2019.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/niknam-2019.yaml",
 "old_string": "    normalized late response to an FF probe rises from 0.90 during fixation to 1.30 just\n    before the saccade, at a longer latency than the RF response.",
 "new_string": "    normalized response to an FF probe rises from 0.90 during fixation to 1.30 just before\n    the saccade."
}
```

```
The file claims/niknam-2019.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/niknam-2019.yaml",
 "old_string": "    variants), on test trials, per neuron. A claim of absence, judged on the paper's test, a\n    two-sided Wilcoxon signed-rank test over 41 neurons at p < 0.05 (Results paragraph 3,\n    \"In all comparisons\"): reproduced when it does not find perisaccadic above fixation, not\n    reproduced when it does. The means and the effect size are reported either way.",
 "new_string": "    variants), on test trials, per neuron. A claim of absence, judged on the paper's test, a\n    Wilcoxon signed-rank test over 41 neurons at p < 0.05 (Results paragraph 3, \"In all\n    comparisons\"): reproduced when it does not find perisaccadic above fixation, not\n    reproduced when it does. The paper does not say whether the test is one- or two-sided;\n    two-sided is used as the standard choice and the one-sided p (perisaccadic above\n    fixation) is shown. The means and the effect size are reported either way."
}
```

```
The file claims/niknam-2019.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/niknam-2019.yaml",
 "old_string": "    when both medians are within tolerance and a two-sided Wilcoxon signed-rank test on the\n    per-neuron ratios gives F above S at p < 0.05; partially reproduced when the test holds\n    but a median is outside tolerance.",
 "new_string": "    when both medians are within tolerance and a two-sided Wilcoxon signed-rank test on the\n    per-neuron ratios gives F above S at p < 0.05; partially reproduced when the test holds\n    but a median is outside tolerance. The paper does not state the sidedness; two-sided is a\n    standard choice and the one-sided p is shown. How a neuron with a fixation Delta LL per\n    spike at or below zero enters the ratio is not stated; such neurons are counted and the\n    test is shown with and without them."
}
```

```
The file claims/niknam-2019.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/niknam-2019.yaml",
 "old_string": "    shuffled distributions, p < 1e-9. Candidates are the neurons with both FF- and\n    ST-remapping in response and model. Reproduced",
 "new_string": "    shuffled distributions, p < 1e-9. Candidates are the neurons with both FF- and\n    ST-remapping in response and model; the paper does not say the example is one of them,\n    so this is an assumption (the example shows FF and ST detection), and the other neurons\n    of the 41 are searched as a variant and reported. Reproduced"
}
```

```
The file claims/niknam-2019.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/niknam-2019.yaml",
 "old_string": "    parameters and c of the neurons with FF-remapping in both response and model, centres\n    taken relative to the FF probe and spreads in units of probe spacing (the code's\n    parameters are already in grid units, fmodel.m), averaged;",
 "new_string": "    parameters and c of the neurons with FF-remapping in both response and model, in units\n    of probe spacing (the code's parameters are already in grid units, fmodel.m), averaged.\n    The Methods say only that the variables were normalized by the probe distance; how the\n    centres of neurons with different RF and FF probes are aligned before averaging is not\n    stated. The centres are taken relative to each neuron's FF probe, an assumption; since a\n    single Gaussian's detectability at its own centre does not depend on where the centre\n    lies, the choice is not expected to change the outcome."
}
```

```
The file claims/niknam-2019.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/niknam-2019.yaml",
 "old_string": "    stated. The centres are taken relative to each neuron's FF probe, an assumption; since a\n    single Gaussian's detectability at its own centre does not depend on where the centre\n    lies, the choice is not expected to change the outcome.",
 "new_string": "    stated. The centres are taken relative to each neuron's FF probe, an assumption;\n    averaging absolute grid positions would mix neurons whose FF lies at different probes."
}
```

```
The file claims/niknam-2019.yaml has been updated successfully.
```

**Agent calls Bash**

```bash
cd  cat >> claims/niknam-2019.yaml <<'EOF'
checks:
- date: 2026-11-11
  kind: agent
  model: claude-opus-5-5
  ready: true
  changes:
  - fig1c-ff-remapping. The statement said the FF response comes "at a longer latency than the RF response" and called the 0.90 to 1.30 values the "late" response; the quoted sentence says neither, and its criterion does not test latency, which fig1-remapping-longer-latency holds. Removed both.
  - O1 (opening comment), and through it fig1b to fig1e, fig1-example-neurons and the fig5b and fig6 claims. Reading (c), an unpaired rank-sum test, is not the test the Methods name for recorded responses (one-sided signed-rank). It is now a variant that is shown and does not decide an outcome.
  - fig5a-n-model-no-perisaccadic-gain. The criterion called the paper's test two-sided; the paper gives only "the Wilcoxon signed-rank test". Now says sidedness is not stated, uses two-sided as a standard choice and shows the one-sided p.
  - fig5c-f-higher-ratio-than-s. Same for sidedness. Added that the paper does not say how neurons with fixation Delta LL per spike at or below zero enter the per-neuron ratio; both ways are shown.
  - fig8c-example-neuron-detectability. Restricting the candidates to neurons with both remapping effects in response and model is not in the paper; marked as an assumption, with all 41 neurons as a reported variant.
  - fig8e-population-ff-detectability (and fig8e-population-st-detectability, which follows it). Centres taken relative to the FF probe are not in the Methods, which say only that the variables were normalized by the probe distance; marked as an assumption.
  - Checked, unchanged. Every quoted number, SE used as tolerance, p-value and count against the Results, Methods and legends; the percent changes of fig5c-percent-changes agree with the slopes by the Methods formulas to rounding. The code settings in the opening comment (get_info.m times, delays, lags, num_folds and splits; load_trials.m condition-wise split; make_profile.m sigma 1.5; select_bases.m r_max 1000 and b0; fmodel.m probe_list columns, bounds for t >= 100 ms and 10-point smoothing; get_fr0.m and get_dll.m NULL model and pooling; amodel.m kernel averaging) were confirmed at commit 1438dde.
  - Open. fig1-remapping-longer-latency rests on a measure the paper does not name (peak latency of the smoothed population curve); the 50-75 and 80-150 ms ranges may simply be the Methods' analysis windows, so the claim mostly tests the windows chosen.
  - Open. The paper says the F-model "performs as well as the S-model" in reproducing the perisaccadic effects (Fig 5B) but gives no test of F against S; there is no claim for it, and the fig5b claims report the four measures per model for comparison.
  - Open. The N-model claims depend on ref [48], which the text read does not list (O8).
  - Open. Which subpopulation the example neurons of Figs 1, 6 and 8 belong to is not stated; their claims search all neurons and are weak tests.
EOF
python tools/claims_check.py claims/niknam-2019.yaml paper/10.1371-journal.pcbi.1007275.txt | tail -3; grep -n ' — \|rather' claims/niknam-2019.yaml | head
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  sed -n '/^checks:/,$p' claims/niknam-2019.yaml | grep -n ': ' ; git status --short
```

```
2:- date: 2026-11-11
3:  kind: agent
4:  model: claude-opus-5-5
5:  ready: true
 M claims/niknam-2019.yaml
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
?? scripts
```

**Agent**

I checked `claims/niknam-2019.yaml` against the paper and made six corrections. It is ready for an attempt, though four problems stay open (listed below). Nothing is committed.

**Checker:** `claims/niknam-2019.yaml: 34 claims, 33 quotes, 28 statistical values, 0 problems` (the same before and after my edits).

**Verified, unchanged:** every quoted number, standard error used as a tolerance, p-value and neuron count matches the Results, Methods and legends. The percentage changes in fig5c-percent-changes follow from the slopes by the Methods' formulas, up to rounding. I cloned the code repository at commit 1438dde and confirmed the settings the opening comment takes from it: the time and delay ranges, the condition-wise 35/35/30 split, the 1.5 SD selection threshold, r_max = 1000, the F-model bounds and smoothing, and how the null model and pooling work.

**Changes, by claim:**
- **fig1c-ff-remapping:** I removed "at a longer latency than the RF response" and the word "late" from the statement. The quoted sentence says neither, and its criterion doesn't test latency; fig1-remapping-longer-latency already covers that.
- **O1, the shared note on how the signed-rank test pairs counts** (it affects the fig1, fig5b and fig6 claims): reading (c), an unpaired rank-sum test, is not the test the Methods name for recorded responses. It is now a variant that is shown but cannot decide an outcome.
- **fig5a-n-model-no-perisaccadic-gain:** the criterion called the paper's test two-sided, but the paper doesn't say. It now says sidedness isn't stated, uses two-sided as a standard choice, and shows the one-sided p.
- **fig5c-f-higher-ratio-than-s:** the same sidedness fix. I also noted that the paper doesn't say how neurons with zero or negative fixation performance enter the per-neuron ratio, so the test is shown with and without them.
- **fig8c-example-neuron-detectability:** limiting the search for the example neuron to neurons with both remapping effects is not in the paper. It is now marked as an assumption, and all 41 neurons are searched as a reported variant.
- **fig8e-population-ff-detectability** (fig8e-population-st-detectability follows it): aligning each neuron's Gaussian centres to its FF probe before averaging is not in the Methods. It is now marked as an assumption.

**Still open** (each recorded in the `checks` entry):
- **fig1-remapping-longer-latency:** the paper names no measure, so the claim uses peak latency of the population curve. The 50-75 and 80-150 ms ranges in the paper may just be the analysis windows from Methods.
- **No claim for one finding:** the paper says the F-model "performs as well as the S-model" for Fig 5B but reports no test of F against S.
- **N-model claims:** these rely on ref [48], which the text doesn't list. They are blocked if the attempt can't identify it.
- **Example neurons:** the paper doesn't identify which neurons are the examples in Figs 1, 6 and 8, so those claims search all neurons and are weak tests.

**Ready:** yes. The check entry is appended under `checks` with `ready: true`.

## End of run

27 turns, 3 minutes, $1.65 at API prices, result: success.
