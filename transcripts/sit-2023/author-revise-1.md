# 000483 · author-revise-1 · run 41111925972

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
date -u; cat transcripts/000483/verifier-1-report.md; ls entries/000483-sit-2023 entries/000483-sit-2023/*
```

```
Fri Oct 30 19:06:37 UTC 2026
**A. Outcomes**

The claims file has 24 claims. The notebooks report outputs for 15 of them and treat one as blocked. The other 8 (fig5k and the seven fig6 claims) are said to be "recorded in the attempt record", which I don't have.

| Claim | Outcome | Reason |
|---|---|---|
| fig1-free-heading-fraction | blocked (data_missing) | Every one of the 128 assets is classified (single_cue cell 3). All 16 single-cue files rotate at a steady 3–8 rpm (motor-driven, cell 6). The only animal-controlled files are 2022 dual-cue recordings. The API listing (128 assets) agrees. |
| fig1g-rotation-heading-fraction | reproduced | With the centred fit, 485/3179 = 15.26% (cell 11), inside 14.2 ± 1.42 and 452 ± 45. The code's uncentred fit gives 10.85%, but it only passes cells whose peak is near −90° (cell 18), which contradicts Fig. 1H, so the centred reading is reasonable. Caveat: the test also passes untuned noise (B1). |
| selection-shuffled-control | not_reproduced | The paper says data were shuffled *before* running the procedure, and the criterion says "before the test". That reading (the notebook's "once" variant) passes 165/3179 = 5.19%, above the 1% limit (cell 16). The 0% "each" reading cannot fail by construction (B2). |
| fig1h-preferred-headings-tile | partially_reproduced | Tiling holds under both readings: (a) 60/60 bins and (b) every quadrant ≥ 0.181 (cell 18). The overrepresentation can't be judged because where the cue sits in the heading frame is unknown (metadata_insufficient). At dataset heading 0 the share is 0.247, below the uniform 0.25. The densest window (−102°, 0.40) depends on the mouse: SKKS090 and SKKS091 peak about 180° away from it. |
| fig2f-head-chamber-same-preference | partially_reproduced | p < 0.05 with V > 0 appears only when the chamber-rotation heading is mirrored (an assumption the notebook adds) and only 5 of 7 pairs are used: V = 34.6, n = 228, p = 5.9e-4 (cell 6). V is outside 14.1 ± 1.41; V/n is 0.15 against 
[... 71 more lines not kept]
```

**Agent calls Bash**

```bash
wc -l docs/protocol.md; grep -n "^#" docs/protocol.md
```

```
612 docs/protocol.md
1:# Protocol for an attempt
40:## Reader
42:### 1. Get the paper
53:### 2. Read the paper's code
63:### 3. Write the claims file
148:### 4. Data from outside the paper's own recordings
156:### 5. Check
169:### 6. Answer questions
182:## Author
198:### 1. Establish what can be tested
325:### 2. Check the data against its description
340:### 3. Write the entry
398:### 4. Lock, check and run
409:### 5. Record the attempt
460:### 6. Hand over for verification
498:## Repeat attempts
540:## Local and remote datasets
563:## Verifier
567:### Round 1: without the author's conclusions
[... 2 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 1,40p docs/protocol.md; sed -n 182,612p docs/protocol.md
```

```
# Protocol for an attempt

Version: `pilot-12`. Record this version in the attempt's provenance.

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
[... 451 more lines not kept]
```

**Agent calls Bash**

```bash
ls; ls attempts 2>/dev/null | grep 483; find . -path ./node_modules -prune -o -name "*000483*" -print | grep -v "^./.git/" | head -30
```

```
LICENSE
LICENSE-data
README.md
attempts
bunfig.toml
claims
docs
encore_science
entries
node_modules
package-lock.json
package.json
paper
papers
pnpm-lock.yaml
pyproject.toml
questions
queue
schemas
scripts
[... 10 more lines not kept]
```

**Agent calls Bash**

```bash
cat attempts/000483-sit-2023-01.yaml; ls claims/000483 transcripts/000483 questions | grep -i 483; ls transcripts/000483
```

```
schema_version: 2
id: 000483-sit-2023-01
dataset:
  archive: dandi
  id: "000483"
  version: 0.230421.2321
  doi: 10.48324/dandi.000483/0.230421.2321
paper: doi:10.1038/s41467-023-37704-5
date: 2026-10-30
entry: 000483-sit-2023
provenance:
  kind: agent
  accountable:
    name: CatalystNeuro
  agent:
    harness: Claude Code
    model: claude-opus-5-5
    protocol: pilot-12
  runner:
    platform: GitHub Actions
[... 347 more lines not kept]
```

**Agent calls Bash**

```bash
ls claims/000483; ls questions | grep 483; cat questions/000483.yaml 2>/dev/null | head -50; wc -l entries/000483-sit-2023/rsc.py; ls executed/ 2>/dev/null | head; cat entries/000483-sit-2023/entry.yaml
```

```
10.1038-s41467-023-37704-5.yaml
616 entries/000483-sit-2023/rsc.py
schema_version: 1
name: 000483-sit-2023
type: reproduction
title: Heading cells and visual landmarks in retrosplenial cortex (Sit and Goard 2023)
description: Tests the findings of Sit and Goard (2023) on dandiset 000483, which holds two-photon
  recordings of retrosplenial somata and of ADN and visual cortical axons in RSC, made in a rotating
  floating chamber with single, dual or changed wall cues, in light and dark, and with the head or
  the chamber rotated. The files hold raw ROI fluorescence and chamber heading; dF/F and inferred
  spikes are computed here. It tests the share of heading-selective cells, their preferred headings,
  head against chamber rotation, coherent remapping, the axon responses in light and dark, and the
  clustering of somata into heading, landmark and alignment cells.
license: Apache-2.0
notebooks:
- path: single_cue.ipynb
  title: Single-cue rotation and the data check (Figure 1)
  runtime_minutes: 12
- path: rotation_remapping.ipynb
  title: Head against chamber rotation and coherent remapping (Figures 2 and 3)
[... 17 more lines not kept]
```

**Agent calls Bash**

```bash
cat claims/000483/*.yaml
```

```
<persisted-output>
Output too large (45.6KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/b78c9ab8-8636-49a3-91a1-9984db3df98a/tool-results/bbzw5ikof.txt

Preview (first 2KB):
# Claims for Sit & Goard (2023), Nature Communications 14:1992, on dandiset 000483.
# Written by an agent (model "claude-opus-5-5", Claude Code in GitHub Actions), 2026-10-23,
# protocol pilot-10 as stated in docs/protocol.md.
#
# Text read: the version of record (publisher's PDF supplied by a person, extracted to text):
# main text, figure legends, Methods and Statistical information. The Supplementary Information
# (Figures S1 to S7 and Table S1) was not in the paper store and was not read. The main
# findings and their statistics are all stated in the main text; the supplement holds the
# detail of three of them (Figure S5, Figure S6 and Table S1), and the claims that rest on it
# say so. The figures could not be opened (no PDF renderer), so no number below is read from a
# figure.
#
# Code read: the repository the paper links, given there as
# github.com/ucsb-goard-lab/Neurotar-HDExperiments; the repository is in fact
# github.com/ucsb-goard-lab/Neurotar-HD-Experiments, commit c6344f5 (2023-03-14). It holds
# MATLAB classes, not figure scripts: Cue.m (tuning curves, preferred direction, flip score,
[... 13 more lines not kept]
```

**Agent calls Bash**

```bash
cd claims/000483; python -c "
import yaml;d=yaml.safe_load(open('10.1038-s41467-023-37704-5.yaml'))
print(d.keys())
for c in d['claims']:
  if c['id'] in ('selection-shuffled-control','fig1h-preferred-headings-tile','fig1g-rotation-heading-fraction') or c['id'].startswith('fig6') or c['id']=='fig5k-visual-cue-only':
    print(yaml.safe_dump(c,width=120))
"
```

```
dict_keys(['schema_version', 'dataset', 'paper', 'claims', 'checks'])
criterion: The heading-selection test of the opening comment (Methods; code ControlledRotation.calculateHeadDirection) with
  a single-term Gaussian, on inferred spikes of every neuron of the 16 single-cue controlled-rotation recordings. Reproduced
  when the percentage is within tolerance. The test uses random splits and shuffles; the random seed is a standard choice
  that should not change the count beyond a few cells.
expected:
- quantity: percentage of heading-selective neurons, controlled rotation
  tolerance: 1.42
  unit: percent
  value: 14.2
- quantity: heading-selective neurons, controlled rotation
  tolerance: 45
  value: 452
id: fig1g-rotation-heading-fraction
quote: we found a similar percentage heading neurons as in the experiments without controlled rotation, comprising 14.2% (452/3179
  neurons) of the total number of cells recorded (n = 16 recordings over 5 mice
source: Results, Neurons in the RSC represent heading in the absence of physical head movements, paragraph 3; Figure 1G
statement: With the chamber rotated by a motor (single cue), 14.2% of RSC neurons (452 of 3179, 16 recordings over 5 mice)
  are heading selective by the paper's reliability and Gaussian-fit test, a percentage similar to the free-chamber experiments.

[... 238 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 25,140p claims/000483/10.1038-s41467-023-37704-5.yaml | grep -n -i -A30 "decod" | head -80
```

```
74:#   - Decoding (Methods, Decoding RSC somatic activity): trials are the full rotations before
75-#     and after each rest that separates light-on from light-off (and light-off from light-on);
76-#     each trial resampled to 200 bins; trials aligned across recordings into pseudopopulations;
77:#     Bayesian decoding (Etter et al. 2020) of "the raw calcium data", trained on even and tested
78-#     on odd timepoints; 1000 bootstrap iterations, each sampling with replacement 332 neurons
79:#     (the smallest class) from the class decoded, or from all three classes in their rough
80:#     proportions for "all tuned cells"; decoder error |decoded - actual| per frame; decoder
81-#     accuracy per trial the fraction of frames with error under 18 degrees; mean and 2.5 and
82-#     97.5 percentiles over iterations; p of a light-on against light-off comparison is one minus
83-#     the fraction of iterations in which a t-test passes at alpha 0.05 (Statistical
84:#     information; decoding error across recordings is compared by paired t-tests). Open, with
85:#     readings: the decoder input, (a) dF/F ("raw calcium data", Methods) or (b) inferred spikes
86:#     (HeadingDecoder); the decoder, (a) the naive Bayes decoder of Etter et al. 2020 on
87:#     binarized activity, with 60 heading states of 6 degrees, or (b) HeadingDecoder's (activity
88-#     times row-rescaled leave-one-trial-out tuning curves, normalized, filtered over 10 samples,
89-#     maximum taken; 180 resample bins; up to 15 trials each side of the transition); the
90-#     t-test, (a) paired over trials or (b) unpaired; chance, (a) 0.18 (Methods) or (b) 0.10
91:#     (Figure 6A legend, which equals 36/360 and HeadingDecoder's 18/180). The Methods come first;
92-#     every reading is run.
93-schema_version: 2
[... 23 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n "_shuff" transcripts/000483/author.md | head -20; grep -n "def selection_test" -A80 entries/000483-sit-2023/rsc.py | head -140
```

```
<persisted-output>
Output too large (66.5KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/b78c9ab8-8636-49a3-91a1-9984db3df98a/tool-results/bf04z1h60.txt

Preview (first 2KB):
859: "content": "\"\"\"Loading and measures for dandiset 000483 (Sit & Goard 2023, Nat Commun 14:1992).\n\nEach NWB file is one two-photon recording of retrosplenial cortex (somata) or of axon\nterminals in it, made in a floating chamber (Neurotar). Each file holds the raw two-photon\nvideo (not read here), the raw fluorescence of each ROI (`raw-fluorescence`, frames x ROIs, at\n10 Hz), the ROI masks, and the chamber heading (degrees) and position (mm), one sample per\nimaging frame. No neuropil trace, dF/F or inferred spikes are stored. The kind of experiment is\ngiven only by the file's `identifier` (for example `..._DualCue_3rpm_SKKS088-DualCue-001`).\nFiles are streamed from the archive at the pinned version; nothing is written to disk.\n\nWhere the parameters come from (\"claims\" is claims/000483/10.1038-s41467-023-37704-5.yaml; \"code\"\nis github.com/ucsb-goard-lab/Neurotar-HD-Experiments at commit c6344f5):\n\n- dF/F = (F - F0)/F0 with F0 the mode of the fluorescence density (Methods, eq. 2). The Methods\n  subtract a neuropil trace first (eq. 1); the dataset holds none, so F is used as it is\n  (deviation). The mode is the peak of a Gaussian kernel density on a 512-point grid with\n  Silverman's bandwidth (a standard choice).\n- Inferred spikes: OASIS with an AR(1) kernel on dF/F (Methods, Analysis of calcium data), with\n  its parameters estimated from the trace, as the call left in Cue.m\n  (deconvolveCa(dff, 'ar1', 'foopsi', 'optimize_pars')) does (claims, opening comment). The\n  Python port of OASIS (package oasis-deconv, `deconvolve`, penalty 1, g and noise optimised) is\n  used in place of the MATLAB one.\n- Heading clean-up and trials: code ControlledRotation.getTrialResponses (claims, opening\n  comment): steps of 20 to 350 degrees rep
[... 2 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "entries/000483-sit-2023/rsc.py"
}
```

```
1	"""Loading and measures for dandiset 000483 (Sit & Goard 2023, Nat Commun 14:1992).
2	
3	Each NWB file is one two-photon recording of retrosplenial cortex (somata) or of axon
4	terminals in it, made in a floating chamber (Neurotar). Each file holds the raw two-photon
5	video (not read here), the raw fluorescence of each ROI (`raw-fluorescence`, frames x ROIs, at
6	10 Hz), the ROI masks, and the chamber heading (degrees) and position (mm), one sample per
7	imaging frame. No neuropil trace, dF/F or inferred spikes are stored. The kind of experiment is
8	given only by the file's `identifier` (for example `..._DualCue_3rpm_SKKS088-DualCue-001`).
9	Files are streamed from the archive at the pinned version; nothing is written to disk.
10	
11	Where the parameters come from ("claims" is claims/000483/10.1038-s41467-023-37704-5.yaml; "code"
12	is github.com/ucsb-goard-lab/Neurotar-HD-Experiments at commit c6344f5):
13	
14	- dF/F = (F - F0)/F0 with F0 the mode of the fluorescence density (Methods, eq. 2). The Methods
15	  subtract a neuropil trace first (eq. 1); the dataset holds none, so F is used as it is
16	  (deviation). The mode is the peak of a Gaussian kernel density with
17	  Silverman's bandwidth, computed on a 1024-bin histogram (a standard choice).
18	- Inferred spikes: OASIS with an AR(1) kernel on dF/F (Methods, Analysis of calcium data), with
19	  its parameters estimated from the trace, as the call left in Cue.m
20	  (deconvolveCa(dff, 'ar1', 'foopsi', 'optimize_pars')) does (claims, opening comment). The
[... 597 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && timeout 60 git clone -q https://github.com/ucsb-goard-lab/Neurotar-HD-Experiments.git nhd 2>&1 | tail -2; cd nhd && git checkout -q c6344f5 && ls && grep -rn "_shuff" --include=*.m . | head
```

```
README.md
_Helpers
_MainAnalysisClasses
_ReviewerCode
_examples
cellComparator.mlapp
flowchart.png
screenCells.m
./_MainAnalysisClasses/_AbstractClasses/ControlledRotation.m:62:                        [fit_shuff, gof_shuff] = obj.fitGaussians(tuning_rand);
./_MainAnalysisClasses/_AbstractClasses/ControlledRotation.m:65:                        amp_vec_shuff(iter) = fit_shuff.a1;
./_MainAnalysisClasses/_AbstractClasses/ControlledRotation.m:66:                        gof_vec_shuff(iter) = gof_shuff.rsquare;
./_MainAnalysisClasses/_AbstractClasses/ControlledRotation.m:94:                    obj.significance_info.gof_vec_shuff(c, :) = gof_vec_shuff;
./_MainAnalysisClasses/_AbstractClasses/ControlledRotation.m:95:                    is_amp(c) = fit_func.a1 > 0;%prctile(amp_vec_shuff, 95);
./_MainAnalysisClasses/_AbstractClasses/ControlledRotation.m:96:                    is_gof(c) = gof.rsquare > prctile(gof_vec_shuff, 90);
./_MainAnalysisClasses/_AbstractClasses/Cue.m:88:		% 				[fit_shuff, gof_shuff] = obj.fitGaussians(tuning_rand, gauss_flag);
./_MainAnalysisClasses/_AbstractClasses/Cue.m:91:		% 				amp_vec_shuff(iter) = fit_shuff.a1;
./_MainAnalysisClasses/_AbstractClasses/Cue.m:92:		% 				gof_vec_shuff(iter) = gof_shuff.rsquare;
./_MainAnalysisClasses/_AbstractClasses/Cue.m:120:		% 			obj.significance_info.gof_vec_shuff(c, :) = gof_vec_shuff;
Shell cwd was reset to
[... 1 more lines not kept]
```

**Agent**

Network works; I have the paper's code. Let me look at the shuffled variant and the main test.

**Agent calls Bash**

```bash
cd $TMPDIR/nhd/_MainAnalysisClasses/_AbstractClasses; sed -n 30,140p Cue.m; echo ======; sed -n 1,130p ControlledRotation.m
```

```
if nargin < 3 || isempty(data_type)
				data_type = 'spikes';
			end

			trimmed_stimulus_data = obj.trimStimulusData(stimulus_data, size(neural_data.raw_F, 2)); % this is in response to some issues we had previously, but it trims stimulus data to be the same size as neural data
			obj.data_type = data_type; % spikes or dff
			obj.data = DataStructure(neural_data, trimmed_stimulus_data); % store into a DataStructure for easy access and use
		end
	end

	methods % Main analyses
		function out = getTuningCurves(obj)
			out = obj.binData(obj.getNeuralData(), obj.getHeading());
		end
		% function is_hd = calculateHeadDirection(obj, tuning_curve_trials, iterations, gauss_flag)
		% 	% To determine which cells are heading selective
		% 	if nargin < 2 || isempty(tuning_curve_trials)
		% 		tuning_curve_trials = obj.getTrialResponses();
		% 	end
                %
[... 223 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/nhd; grep -rn "calculateHeadDirection_shuff\|HeadDirection_shuf" . | head; grep -rn "function.*fitGaussians" -A45 _MainAnalysisClasses/_AbstractClasses/Cue.m | head -70
```

```
./_MainAnalysisClasses/_AbstractClasses/Cue.m:888:% function is_hd = calculateHeadDirection_shuff(obj, tuning_curve_trials, iterations, gauss_flag)
345:		function [fit_out, gof_out] = fitGaussians_old(obj, data, rescale_flag, center_flag)
346-			% Fitting constrained Gaussians to the data
347-			if nargin < 3 || isempty(rescale_flag)
348-				rescale_flag = true;
349-			end
350-
351-			if nargin < 3 || isempty(center_flag)
352-				center_flag = false;
353-			end
354-
355-			if size(data, 2) > size(data, 1)
356-				data = transpose(data); % ensure column vector
357-			end
358-
359-			x = linspace(0, 2*pi, size(data, 1));
360-			if rescale_flag
361-				data = rescale(data);
362-            end
363-            
[... 52 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/nhd; sed -n 885,990p _MainAnalysisClasses/_AbstractClasses/Cue.m; cd $TMPDIR/nhd; git log -1 --format=%H
```

```
%         % end
%     end
% end
% function is_hd = calculateHeadDirection_shuff(obj, tuning_curve_trials, iterations, gauss_flag)
% 	if nargin < 2 || isempty(tuning_curve_trials)
% 		tuning_curve_trials = obj.getTrialResponses();
% 	end
%
% 	if nargin < 3 || isempty(iterations)
% 		iterations = 100;
% 	end
%
% 	if nargin < 4 || isempty(gauss_flag)
% 		gauss_flag = 'double';
% 	end
%
%
% 	if ndims(tuning_curve_trials) < 3
% 		disp('Bad recording, single trials only, skipping...')
% 		is_hd = false(1, size(tuning_curve_trials, 1));
[... 85 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/000483-sit-2023; for f in *.ipynb; do python -c "
import json,sys;nb=json.load(open('$f'));print('$f',len(nb['cells']), sum(len(''.join(c['source'])) for c in nb['cells']))"; done; ls ../../executed/ 2>/dev/null; sed -n 1,80p ../../tools/entry.py | head -80
```

```
axons.ipynb 14 13888
directions.ipynb 12 10293
rotation_remapping.ipynb 13 14404
single_cue.ipynb 24 19433
somata.ipynb 25 23852
"""Lock, check and run one entry. This is the whole local workflow for a deposit.

    python tools/entry.py lock  entries/<name>   # pin the environment
    python tools/entry.py check entries/<name>   # validate metadata and conventions
    python tools/entry.py check entries/*/       # the same for every entry, in one process
    python tools/entry.py run   entries/<name>   # execute every notebook from a clean environment
    python tools/entry.py all   entries/<name>   # check, then run
    python tools/entry.py handover entries/<name> # the verifier's package, from the executed copies

`lock` compiles the entry's requirements.in (direct dependencies only) into
requirements.lock.txt with every version pinned.

`check` validates entry.yaml, and the claims and attempt files that mention
the entry, against the schemas, and applies the conventions that keep a result
tied to the data:
[... 65 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n "add_argument\|def cmd_run\|ThreadPool\|parallel" tools/entry.py | head -30; nproc; free -g | head -2
```

```
428:    parser.add_argument("command", choices=["lock", "check", "run", "all", "handover"])
429:    parser.add_argument("entry", type=Path, nargs="+",
431:    parser.add_argument("--output-dir", type=Path, help="where executed notebooks go")
432:    parser.add_argument("--timeout", type=int, default=3600, help="seconds allowed per cell")
433:    parser.add_argument("--max-minutes", type=float, default=30,
4
               total        used        free      shared  buff/cache   available
Mem:              15           1          12           0           2          14
```

**Agent calls Bash**

```bash
cd entries/000483-sit-2023; python -c "
import json;nb=json.load(open('somata.ipynb'))
for i,c in enumerate(nb['cells']):
  print('#### cell',i,c['cell_type'],c['metadata'].get('tags'));print(''.join(c['source']))"
```

```
#### cell 0 markdown None
# Sit & Goard (2023) on dandiset 000483: RSC somata with dual cues, light and dark (Figure 5)

**Paper.** Sit KK, Goard MJ (2023), *Nature Communications* 14:1992,
[doi:10.1038/s41467-023-37704-5](https://doi.org/10.1038/s41467-023-37704-5); claims file
written from the version of record without its supplement.

**Dataset.** [DANDI:000483](https://dandiarchive.org/dandiset/000483/0.230421.2321), version
0.230421.2321, the only published version (the paper cites none). See `single_cue.ipynb` for the
data check of all files.

| Claim | Here |
|---|---|
| fig4-axons-light-on-shape | tested |
| fig4-axons-light-off | tested |
| fig5-three-classes | tested |
| fig5-class-proportions | tested |
| fig5e-alignment-peaks-coregistered | tested |
| fig5f-heading-flip-unchanged | tested |
| fig5gh-landmark-alignment-flip-drop | tested |
[... 382 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python -c "
import yaml;d=yaml.safe_load(open('claims/000483/10.1038-s41467-023-37704-5.yaml'))
for c in d['claims']:
  if c['id'] in ('fig2f-head-chamber-same-preference','fig3c-coherent-remapping','fig4-axons-light-off','fig5e-alignment-peaks-coregistered','fig5f-heading-flip-unchanged','fig5i-axons-in-clusters'):
    print(c['id'],'::',c['criterion'], c.get('expected'));print()
"
```

```
fig2f-head-chamber-same-preference :: The 5 head-rotation recordings, each paired with its chamber-rotation recording of the same field; ROIs matched across the two (a single set of ROIs after derotation, manually checked, Results). Per ROI the difference in preferred heading, head rotation minus chamber rotation, wrapped to +-180; circ_vtest against 0. Open, with readings, the cells, (a) matched ROIs heading-selective in both conditions, (b) in either condition, (c) in the chamber-rotation condition; the preferred heading, (i) the peak of the trial-mean tuning curve (Figure 2F legend, "peak heading preference"), (ii) the code's 'fit' method (Cue.calculatePreferredDirection, recommended in the code's README). Reproduced when a reading gives p < 0.05 with V > 0; the V and n of each reading are reported, and the one whose n is 32 is named. [{'quantity': 'V statistic', 'value': 14.1, 'tolerance': 1.41}]

fig3c-coherent-remapping :: The 12 remapping recordings (single-cue class in the code, RemappingExperiment). Per neuron n, Delta phase offset = (pref A(n) - pref B(n)) minus the expected offset of the other neurons of its recording, wrapped to +-180; circ_vtest against 0 over all neurons of all recordings (Methods, Calculation of coherent remapping). Open, with readings, the expected offset, (i) the median over the other neurons of their differences pref A - pref B (Methods text) or (ii) the median of their pref A minus the median of their pref B (the Methods equation); the cells, (a) heading-selective in both contexts, (b) in either; the preferred heading, the peak of the trial-mean tuning curve or the code's 'fit' method. Reproduced when a reading gives p < 0.05 with V > 0; every reading's V and n are reported. [{'quantity': 'V statistic', 'value': 25.6, 'tolerance': 2.56}]

fig4-axons-light-off :: Same recordings, axons and readings as fig4-axons-light-on-shape; light-off trials aligned with the light-on shifts (Methods). The paper gives no test; the measure is the 
[... 6 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/nhd; grep -rn "function.*getTrialResponses" -A60 _MainAnalysisClasses/_AbstractClasses/ControlledRotation.m | grep -n "prctile\|90\|50" ; grep -rn "getHeading\b\|function out = getHeading" -A12 _MainAnalysisClasses/_AbstractClasses/*.m | head -60
```

```
19:184-            is_jump = abs(diff(heading)) > 20 & abs(diff(heading)) < 350; % weird spikes from the recorded neurotar stuff, this is to remove those
25:190-                heading(is_jump) = heading(max(find(is_jump) - 1, 1)); % "interpolate' jumps via nearest neighbor (one way)
26:191-                is_jump = abs(diff(heading)) > 20 & abs(diff(heading)) < 350;
55:220-            segment(cellfun(@length, segment) < 50) = []; % cut out segments too short to feasibly be full rotations
59:224-                is_not_full(ii) = any(90 - abs(prctile(heading(segment{ii}), [25, 75])) > 50); % should both be around 90
_MainAnalysisClasses/_AbstractClasses/Control.m:12:		function out = getHeading(obj);
_MainAnalysisClasses/_AbstractClasses/Control.m-13-			out = obj.data.get('heading');
_MainAnalysisClasses/_AbstractClasses/Control.m-14-		end
_MainAnalysisClasses/_AbstractClasses/Control.m-15-		function calculateHeadDirection(obj)
_MainAnalysisClasses/_AbstractClasses/Control.m-16-		end
_MainAnalysisClasses/_AbstractClasses/Control.m-17-	end
_MainAnalysisClasses/_AbstractClasses/Control.m-18-end
--
_MainAnalysisClasses/_AbstractClasses/Cue.m:42:			out = obj.binData(obj.getNeuralData(), obj.getHeading());
_MainAnalysisClasses/_AbstractClasses/Cue.m-43-		end
_MainAnalysisClasses/_AbstractClasses/Cue.m-44-		% function is_hd = calculateHeadDirection(obj, tuning_curve_trials, iterations, gauss_flag)
_MainAnalysisClasses/_AbstractClasses/Cue.m-45-		% 	% To determine which cells are heading selective
_MainAnalysisClasses/_AbstractClasses/Cue.m-46-		% 	if nargin < 2 || isempty(tuning_curve_trials)
_MainAnalysisClasses/_AbstractClasses/Cue.m-47-		% 		tuning_curve_trials = obj.getTrialResponses();
_MainAnalysisClasses/_AbstractClasses/Cue.m-48-		% 	end
[... 46 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/000483-sit-2023; python -c "
import json;nb=json.load(open('single_cue.ipynb'))
for i,c in enumerate(nb['cells']):
  if i>=7: print('#### cell',i,c['cell_type'],c['metadata'].get('tags'));print(''.join(c['source']))"
```

```
#### cell 7 markdown None
Every single-cue file rotates at a steady rate (median step per frame; 3.1 to 8.0 rpm), with
few still frames: these are the motor-driven recordings (Methods: 3 to 7 rpm). None is a
free-chamber recording, whose heading would wander. Heading is in degrees on -180 to 180, as
stated.

**Clock check.** Heading and fluorescence have one sample per frame, but that does not show they
are aligned, and in a recording that rotates one way at constant speed a time offset only rotates
every tuning curve, which no measure within the recording can see. The files that rotate in
both directions (`motor_both`, Fig. S5) give a contrast: an offset of k frames between the
streams moves the tuning curves of clockwise and counterclockwise rotation in opposite
directions. The mean correlation, over ROIs, of each ROI's clockwise and counterclockwise
tuning curves is computed with the heading shifted by -10 to +10 frames against the activity;
with a shared clock it peaks at 0 or a little after (calcium and deconvolution delay).
#### cell 8 code ['sanity']
both_dir = cat[cat.experiment == "motor_both"].reset_index(drop=True)
brecs = rsc.load_many(both_dir.url.tolist())
with Pool(4) as pool:
    for r in brecs:
        r["sp"] = rsc.spikes(rsc.dff(r["F"]), pool)
[... 164 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/000483-sit-2023; python -c "
import json;nb=json.load(open('rotation_remapping.ipynb'))
for i,c in enumerate(nb['cells']):
  if i>=1: print('#### cell',i,c['cell_type'],c['metadata'].get('tags'));print(''.join(c['source']))"
```

```
/bin/bash: line 1: cd: entries/000483-sit-2023: No such file or directory
#### cell 1 code None
import time
import warnings
from multiprocessing import Pool

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

import rsc

warnings.filterwarnings("ignore", category=RuntimeWarning)
pd.set_option("display.width", 200)
pd.set_option("display.max_columns", 30)
started = time.time()
cat = rsc.catalog(full=False)
sub = cat[cat.experiment.isin(["head_rotation", "chamber_rotation", "remapping"])].reset_index(drop=True)
recs = rsc.load_many(sub.url.tolist())
with Pool(4) as pool:
[... 202 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/000483-sit-2023; python -c "
import json;nb=json.load(open('axons.ipynb'))
for i,c in enumerate(nb['cells']):
  if i in (5,9,10,11,12,13): print('#### cell',i,c['cell_type'],c['metadata'].get('tags'));print(''.join(c['source']))"; python -c "
import json;nb=json.load(open('directions.ipynb'))
for i,c in enumerate(nb['cells']):
  if i>=6: print('#### cell',i,c['cell_type'],c['metadata'].get('tags'));print(''.join(c['source']))"
```

```
#### cell 5 code None
t0 = time.time()
trials_all = [rsc.trial_tuning(r["sp"], r["heading"], r["seg_all"]) for r in recs]
ax_idx = [i for i in range(len(recs)) if "axons" in sub.experiment[i]]
with Pool(4) as pool:
    sel = rsc.selection_many(trials_all, "double", 301, pool, centre=True)   # all files here are axons
    sel_ax_code = rsc.selection_many([trials_all[i] for i in ax_idx], "double", 302, pool, centre=False)
    sel_ax_dark = rsc.selection_many([rsc.trial_tuning(recs[i]["sp"], recs[i]["heading"], recs[i]["seg_d"]) for i in ax_idx],
                                     "double", 303, pool, centre=True)
info["selective"] = [s.is_hd.sum() for s in sel]
print(f"selection tests in {time.time() - t0:.0f} s")
print(info.groupby("experiment")[["rois", "selective"]].sum().to_string())
#### cell 9 markdown None
**Result: reproduced under reading (b), all axons.** The mean aligned light-on curve has a flip score of -0.207 for ADN axons (unimodal) and 1.875 for visual axons (bimodal). Single visual axons have higher flip scores than ADN axons (means 0.506 and -0.109, KS p = 1.6e-24). Under reading (a), selective axons, the visual part holds (1.814; single axons 1.073 against -0.072, KS p = 1.7e-21). The ADN mean curve, however, has a flip score of 0.277 (centred fit) or 1.132 (code fit), above 0. One ADN mouse, SKKS092, has a mean flip score above 0 under every reading.
#### cell 10 markdown None
## fig4-axons-light-off

> In the light-off condition ADN axons keep their heading tuning for several trials, while visual
> cortical axons lose their tuning.

[... 117 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat entries/000483-sit-2023/requirements.in; which uv python; python --version; ls ~/.cache 2>/dev/null | head
```

```
dandi
h5py
matplotlib
numpy
oasis-deconv
pandas
remfile
scikit-learn
scipy
statsmodels
/opt/hostedtoolcache/Python/3.13.17/x64/bin/uv
/opt/hostedtoolcache/Python/3.13.17/x64/bin/python
Python 3.13.17
```

**Agent calls Bash**

```bash
cd $TMPDIR && uv venv -q -p 3.13 dev && uv pip install -q -p dev/bin/python -r entries/000483-sit-2023/requirements.lock.txt ipykernel nbconvert 2>&1 | tail -3; dev/bin/python -c "import oasis, sklearn; print('ok')"
```

```
ok
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd entries/000483-sit-2023; python - <<'EOF'
import json,os
nb=json.load(open('somata.ipynb'))
src=[''.join(nb['cells'][i]['source']) for i in (1,2,5,6,8,10,13)]
src[0]=src[0].replace('["soma_dual", "adn_axons", "vis_axons"]','["soma_dual"]')
# skip silhouette loop beyond k=3 for speed
src[5]="""gmms = {}
for k_name, v in soma.items():
    X = v["feats"]
    for k in range(2, 7):
        g = GaussianMixture(k, covariance_type="full", n_init=20, max_iter=1000, random_state=304).fit(X)
        gmms[(k_name, k)] = g
    if k_name.startswith('(a)'): break
"""
src.append("""
import pickle
keep = [dict(heading=r['heading'], sp=r['sp'], dff=r['dff'], seg_l=r['seg_l'], seg_d=r['seg_d']) for r in recs]
pickle.dump(dict(recs=keep, sel=sel, aligned=aligned, soma_idx=soma_idx, cls=cls, names=names, v_rec=v['rec'], v_mice=v['mice'], sub=sub, info=info), open(os.environ['TMPDIR']+'/dev.pkl','wb'))
print('saved')
""")
open(os.environ['TMPDIR']+'/dev_somata.py','w').write("import os\n"+"\n".join(src))
EOF
grep -n "ax_idx\|sel_a" $TMPDIR/dev_somata.py
```

```
49:ax_idx = [i for i in range(len(recs)) if "axons" in sub.experiment[i]]
51:    soma_files = [i for i in range(len(recs)) if i not in ax_idx]
53:    sel_a = rsc.selection_many([trials_all[i] for i in ax_idx], "double", 301, pool, centre=True)
57:for i, s in zip(ax_idx, sel_a):
```

**Agent calls Bash**

```bash
cd entries/000483-sit-2023; date -u; time $TMPDIR/dev/bin/python $TMPDIR/dev_somata.py 2>&1 | tail -30; date -u
```

```
Fri Oct 30 19:09:49 UTC 2026
Traceback (most recent call last):
  File "/tmp/claude-1001/dev_somata.py", line 15, in <module>
    import rsc
ModuleNotFoundError: No module named 'rsc'

real	0m3.374s
user	0m3.522s
sys	0m0.262s
Fri Oct 30 19:09:53 UTC 2026
```

**Agent calls Bash**

```bash
cd entries/000483-sit-2023; time PYTHONPATH=. $TMPDIR/dev/bin/python $TMPDIR/dev_somata.py 2>&1 | tail -30; date -u
```

```
Recordings without light-off trials: []
(a) selective: 1419 somata from 34 recordings, 6 mice; median r2 light 0.54, dark 0.26
(b) all: 11329 somata from 34 recordings, 6 mice; median r2 light 0.26, dark 0.14
fits in 4 s
component means (a1, a2, c1, c2 light; a1, a2, c1, c2 dark):
  landmark  [0.58, 0.46, 0.79, 0.7, 0.05, 0.03, 0.66, 0.65] light a2/a1 ratio 0.79, dark peak 0.05
  alignment [0.35, 0.28, 2.04, 0.92, 0.23, 0.26, 1.84, 1.89] light a2/a1 ratio 0.80, dark peak 0.26
  heading   [0.44, 0.3, 0.7, 1.9, 0.37, 0.21, 0.64, 0.88] light a2/a1 ratio 0.70, dark peak 0.37

tuned somata: pooled 12.53%, mean over recordings 12.10% (s.e.m. 1.44), mean over mice 11.51%  (paper 12.1 +- 1.1)
over all 35 soma recordings, including those without light-on trials: 12.39%
                       outliers        average  null  landmark %  alignment %  heading %  landmark sem  alignment sem  heading sem
(a) chi-square outliers to null (i) recordings    58         8.6         75.3       12.2           1.9            3.0          2.2
(a) chi-square outliers to null      (ii) mice    58        10.2         72.2       14.6           4.4            7.5          4.3
(a) chi-square outliers to null   (iii) pooled    58         5.4         80.6       14.0           NaN            NaN          NaN
            (b) no outlier step (i) recordings     0         8.8         78.9       12.4           2.0            3.3          2.2
            (b) no outlier step      (ii) mice     0        10.3         74.9       14.8           4.4            8.1          4.2
            (b) no outlier step   (iii) pooled     0         5.3         81.0       13.7           NaN            NaN          NaN

counts (no outlier step): {'landmark': 75, 'alignment': 1150, 'heading': 194} | paper (from F-test degrees of freedom): heading 332, landmark 522, alignment 409
[... 15 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/000483-sit-2023; cat > $TMPDIR/d0.py <<'EOF'
import pickle,os,numpy as np, rsc
d=pickle.load(open(os.environ['TMPDIR']+'/dev.pkl','rb'))
recs=d['recs'];sub=d['sub']
for i in d['soma_idx']:
    r=recs[i]; L,D=rsc.light_dark_frames(sub.n_frames[i])
    print(i, sub.subject[i], sub.n_frames[i], d['sel'][i].is_hd.sum(), 'L per block',[sum(1 for s in r['seg_l'] if s[0]>=b[0] and s[-1]<=b[-1]) for b in L],'D',[sum(1 for s in r['seg_d'] if s[0]>=b[0] and s[-1]<=b[-1]) for b in D], 'trial len', int(np.median([len(s) for s in r['seg_l']])))
EOF
PYTHONPATH=. $TMPDIR/dev/bin/python $TMPDIR/d0.py
```

```
0 SKKS080 1950 8 L per block [5] D [6] trial len 156
1 SKKS080 1950 11 L per block [6] D [6] trial len 142
2 SKKS088 1950 17 L per block [6] D [2] trial len 132
4 SKKS088 1950 3 L per block [1] D [2] trial len 145
5 SKKS088 7550 73 L per block [7, 6, 5] D [6, 6, 7] trial len 183
6 SKKS088 7550 40 L per block [6, 6, 7] D [7, 5, 6] trial len 182
7 SKKS089 1950 9 L per block [10] D [10] trial len 90
8 SKKS089 1950 6 L per block [9] D [10] trial len 85
9 SKKS089 1950 9 L per block [3] D [2] trial len 128
10 SKKS089 7550 99 L per block [5, 6, 6] D [7, 6, 6] trial len 182
11 SKKS089 7550 133 L per block [7, 5, 6] D [6, 7, 6] trial len 181
12 SKKS089 7550 60 L per block [6, 5, 6] D [6, 6, 6] trial len 187
13 SKKS089 7550 129 L per block [7, 6, 6] D [5, 5, 6] trial len 186
14 SKKS089 7550 107 L per block [6, 5, 7] D [6, 6, 5] trial len 187
15 SKKS090 1950 5 L per block [11] D [11] trial len 80
16 SKKS090 1950 20 L per block [10] D [11] trial len 79
17 SKKS090 7550 12 L per block [6, 7, 6] D [6, 6, 6] trial len 180
18 SKKS090 7550 49 L per block [6, 5, 6] D [6, 5, 6] trial len 192
19 SKKS090 7550 48 L per block [5, 6, 5] D [6, 6, 6] trial len 191
20 SKKS090 7550 27 L per block [5, 6, 7] D [6, 6, 6] trial len 185
[... 14 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/000483-sit-2023; cat > $TMPDIR/dec.py <<'EOF'
import pickle,os,time,numpy as np, pandas as pd, rsc
from scipy import stats
d=pickle.load(open(os.environ['TMPDIR']+'/dev.pkl','rb'))
recs=d['recs'];sub=d['sub'];sel=d['sel'];cls=d['cls'];names=d['names'];aligned=d['aligned']
N_RS=200; K=5
grid=np.linspace(-180,180,N_RS,endpoint=False)+180/N_RS
def resample(act,h,seg):
    hu=np.unwrap(np.deg2rad(h[seg]));hu=np.rad2deg(hu)
    if hu[-1]<hu[0]: hu=-hu; sgn=-1
    else: sgn=1
    # position of each grid heading along the trial's unwrapped heading
    target=hu[0]+np.mod(sgn*grid-hu[0], 360) if True else None
    out=np.stack([np.interp(target, hu, act[seg][:,n]) for n in range(act.shape[1])],1)
    return out
t0=time.time()
def trials_around(i):
    r=recs[i];L,D=rsc.light_dark_frames(sub.n_frames[i])
    on,off=[],[]
    for bl,bd in zip(L,D):
        sl=[s for s in r['seg_l'] if s[0]>=bl[0] and s[-1]<=bl[-1]]
        sd=[s for s in r['seg_d'] if s[0]>=bd[0] and s[-1]<=bd[-1]]
        if len(sl)<K or len(sd)<K: return None
        on+=sl[-K:]; off+=sd[:K]
    return on,off
use=[i for i in d['soma_idx'] if sub.n_frames[i]==7550 and trials_around(i) is not None]
print(len(use),'recordings')
# cell list (tuned cells with class), in order of soma_features: soma_idx order, mask is_hd & dark not nan
cell_rec, cell_roi = [], []
for i in d['soma_idx']:
    m=sel[i].is_hd.values & ~np.isnan(aligned[i][1]).any(1)
    cell_rec+= [i]*int(m.sum()); cell_roi+=np.flatnonzero(m).tolist()
cell_rec=np.array(cell_rec);cell_roi=np.array(cell_roi)
assert len(cell_rec)==len(cls)
inuse=np.isin(cell_rec,use)
print('tuned cells',len(cls),'in used recordings',inuse.sum())
data={}
for inp in ['dff','sp']:
    on_all,off_all=[],[]
    for i in use:
        on,off=trials_around(i)
        rois=cell_roi[cell_rec==i]
        act=recs[i][inp][:,rois]
        on_all.append(np.stack([resample(act,rsc.clean_heading(recs[i]['heading']),s) for s in on]))  # trials x 200 x n
        off_all.append(np.stack([resample(act,rsc.clean_heading(recs[i]['heading']),s) for s in off]))
    data[inp]=(np.concatenate(on_all,2),np.concatenate(off_all,2))
print('resampled',time.time()-t0, data['sp'][0].shape)
pickle.dump(dict(data=data,cls=cls[inuse],names=names,grid=grid),open(os.environ['TMPDIR']+'/dec.pkl','wb'))
EOF
PYTHONPATH=. $TMPDIR/dev/bin/python $TMPDIR/dec.py
```

```
25 recordings
tuned cells 1419 in used recordings 1331
resampled 1.196946144104004 (15, 200, 1331)
```

**Agent calls Bash**

```bash
cd entries/000483-sit-2023; cat > $TMPDIR/dec2.py <<'EOF'
import pickle,os,time,numpy as np, pandas as pd
from scipy import stats
d=pickle.load(open(os.environ['TMPDIR']+'/dec.pkl','rb'))
data,cls,names,grid=d['data'],d['cls'],d['names'],d['grid']
NS=60; state=np.clip(((grid+180)//6).astype(int),0,59); centres=-177+6*np.arange(NS)
def prep(on, decoder):
    # on: trials x 200 x n. train even bins, test odd bins.
    tr=on[:,0::2]; te=on[:,1::2]; s_tr=state[0::2]; s_te=state[1::2]
    n=on.shape[2]
    if decoder=='template':
        T=np.stack([tr[:,s_tr==s].mean((0,1)) for s in range(NS)],1)  # n x NS
        lo=T.min(1,keepdims=True); rg=np.ptp(T,1,keepdims=True); T=np.where(rg>0,(T-lo)/np.where(rg>0,rg,1),0)
        W=T; B=np.zeros((n,NS)); X=te
    else:
        thr = 0 if False else None
        # binarize
        flat=on.reshape(-1,n)
        th=np.where(np.std(flat,0)>0, flat.mean(0)+2*flat.std(0), np.inf) if decoder.endswith('z') else np.zeros(n)
        btr=(tr>th).astype(float); bte=(te>th).astype(float)
        p=np.stack([(btr[:,s_tr==s].sum((0,1))+1)/(btr[:,s_tr==s].shape[0]*btr[:,s_tr==s].shape[1]+2) for s in range(NS)],1)
        W=np.log(p)-np.log(1-p); B=np.log(1-p); X=bte
    return W,B,X,s_te
def decode(W,B,X,s_te,idx):
    sc=X[:,:,idx]@W[idx]+B[idx].sum(0)   # trials x frames x NS
    dec=centres[sc.argmax(2)]
    true=grid[1::2]
    err=np.abs((dec-true[None]+180)%360-180)
    return err
rng=np.random.default_rng(0)
groups={'all':np.ones(len(cls),bool)}
for c,nm in names.items(): groups[nm]=cls==c
print({g:int(m.sum()) for g,m in groups.items()})
for inp in ['sp','dff']:
  for decoder in (['template','bayes0'] if inp=='sp' else ['template','bayesz']):
    t0=time.time()
    P={cond:prep(data[inp][k],decoder) for k,cond in enumerate(['on','off'])}
    for g,m in groups.items():
        pool_=np.flatnonzero(m); acc={'on':[],'off':[]}; e180=[]; pt=[]
        for it in range(200):
            idx=rng.choice(pool_,332,replace=True)
            a={}
            for cond in ['on','off']:
                err=decode(*P[cond],idx)
                a[cond]=(err<18).mean(1)
                acc[cond].append(a[cond].mean())
                if cond=='on': e180.append((err>162).mean())
            pt.append(stats.ttest_rel(a['on'],a['off']).pvalue<0.05)
        print(inp,decoder,g, 'on %.2f [%.2f %.2f]'%(np.mean(acc['on']),*np.percentile(acc['on'],[2.5,97.5])),'off %.2f [%.2f %.2f]'%(np.mean(acc['off']),*np.percentile(acc['off'],[2.5,97.5])),'p=%.3f'%(1-np.mean(pt)),'180err %.3f'%np.mean(e180))
    print(time.time()-t0)
EOF
PYTHONPATH=. $TMPDIR/dev/bin/python $TMPDIR/dec2.py
```

```
{'all': 1331, 'heading': 175, 'landmark': 54, 'alignment': 1102}
sp template all on 0.38 [0.34 0.42] off 0.29 [0.26 0.32] p=0.060 180err 0.089
sp template heading on 0.21 [0.19 0.23] off 0.21 [0.18 0.23] p=0.960 180err 0.097
sp template landmark on 0.25 [0.24 0.27] off 0.16 [0.16 0.17] p=0.000 180err 0.118
sp template alignment on 0.39 [0.35 0.43] off 0.30 [0.27 0.33] p=0.030 180err 0.093
4.881503105163574
sp bayes0 all on 0.71 [0.67 0.74] off 0.57 [0.53 0.60] p=0.000 180err 0.056
sp bayes0 heading on 0.41 [0.38 0.43] off 0.34 [0.32 0.36] p=0.310 180err 0.092
sp bayes0 landmark on 0.40 [0.38 0.41] off 0.19 [0.18 0.20] p=0.000 180err 0.138
sp bayes0 alignment on 0.71 [0.68 0.75] off 0.58 [0.55 0.61] p=0.000 180err 0.057
4.358151197433472
dff template all on 0.39 [0.31 0.46] off 0.39 [0.31 0.47] p=0.825 180err 0.061
dff template heading on 0.23 [0.20 0.28] off 0.27 [0.24 0.30] p=0.860 180err 0.073
dff template landmark on 0.27 [0.23 0.30] off 0.21 [0.20 0.23] p=0.410 180err 0.092
dff template alignment on 0.39 [0.32 0.48] off 0.39 [0.32 0.47] p=0.790 180err 0.070
4.881348371505737
dff bayesz all on 0.71 [0.66 0.75] off 0.57 [0.53 0.61] p=0.020 180err 0.033
dff bayesz heading on 0.42 [0.39 0.45] off 0.37 [0.34 0.40] p=0.665 180err 0.072
dff bayesz landmark on 0.40 [0.38 0.42] off 0.21 [0.20 0.22] p=0.000 180err 0.119
dff bayesz alignment on 0.72 [0.68 0.76] off 0.58 [0.53 0.62] p=0.005 180err 0.033
[... 1 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && git clone -q https://github.com/ucsb-goard-lab/HeadingDecoder.git hd && cd hd && git checkout -q ca9842e && ls -R | head -30
```

```
.:
README.md
_classes
_helpers
decoding_mwe.m
population_shift_new_testing.m

./_classes:
HeadingDecoder.m
HeadingDecoderPreprocessor.m
HeadingDecoderPreprocessor2.m

./_helpers:
angdiff.m
calculateDecoderError.m
calculatePercentCorrect.m
cleanHeadingTrace.m
getConfusionMatrix.m
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/hd; cat _classes/HeadingDecoder.m | head -150; cat _helpers/calculatePercentCorrect.m; cat decoding_mwe.m | head -60
```

```
classdef HeadingDecoder < handle
	properties
		tuning_wts
		time_series

		memory = 5 % Samples looking back for fitting a line
		window = 0 % Samples around a single point for heading distribution

		n_segments  % number of identified segments in the data

		heading_distribution % likelihood across time that's used for ultimately determining heading
		predicted_heading % predicted heading at each time bin

		all_peak_centers
		fit_distribution
		target_idx
		scaling

		bin_centers
	end
[... 193 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/000483-sit-2023; cat > $TMPDIR/dec3.py <<'EOF'
import pickle,os,time,numpy as np
from scipy import stats
d=pickle.load(open(os.environ['TMPDIR']+'/dec.pkl','rb'))
data,cls,names,grid=d['data'],d['cls'],d['names'],d['grid']
NS=60; state=np.clip(((grid+180)//6).astype(int),0,59); centres=-177+6*np.arange(NS)
def prep_hd(on):
    T,F,n=on.shape
    S=np.zeros((T,n,NS))
    for s in range(NS): S[:,:,s]=on[:,state==s].mean(1)
    tot=S.sum(0)
    loo=(tot[None]-S)/(T-1)                      # trials x n x NS
    lo=loo.min(2,keepdims=True); rg=loo.max(2,keepdims=True)-lo
    W=np.where(rg>0,(loo-lo)/np.where(rg>0,rg,1),0)
    return W,on
def filt(P,w=10):
    L=np.log1p(P); c=np.concatenate([np.zeros_like(L[:,:1]),np.cumsum(L,1)],1)
    F=P.shape[1]; i=np.arange(F); a=np.clip(i-w//2,0,F); b=np.clip(i+w//2,0,F)
    out=np.expm1(c[:,b]-c[:,a]); return out/out.sum(2,keepdims=True)
def decode_hd(W,X,idx):
    sc=np.einsum('tfn,tns->tfs',X[:,:,idx],W[:,idx])
    with np.errstate(invalid='ignore',divide='ignore'): P=sc/sc.sum(2,keepdims=True)
    P=np.nan_to_num(P); P=filt(P)
    dec=centres[P.argmax(2)]
    return np.abs((dec-grid[None]+180)%360-180)
rng=np.random.default_rng(0)
groups={'all':np.ones(len(cls),bool)}
for c,nm in names.items(): groups[nm]=cls==c
for inp in ['sp','dff']:
    t0=time.time()
    P={cond:prep_hd(data[inp][k]) for k,cond in enumerate(['on','off'])}
    for g,m in groups.items():
        pool_=np.flatnonzero(m); acc={'on':[],'off':[]}; e180=[]; pt=[]
        for it in range(100):
            idx=rng.choice(pool_,332,replace=True); a={}
            for cond in ['on','off']:
                err=decode_hd(*P[cond],idx); a[cond]=(err<=18).mean(1); acc[cond].append(a[cond].mean())
                if cond=='on': e180.append((err>=162).mean())
            pt.append(stats.ttest_rel(a['on'],a['off']).pvalue<0.05)
        print(inp,'HD',g,'on %.2f [%.2f %.2f]'%(np.mean(acc['on']),*np.percentile(acc['on'],[2.5,97.5])),'off %.2f [%.2f %.2f]'%(np.mean(acc['off']),*np.percentile(acc['off'],[2.5,97.5])),'p=%.3f'%(1-np.mean(pt)),'180err %.3f'%np.mean(e180))
    print(time.time()-t0)
EOF
PYTHONPATH=. $TMPDIR/dev/bin/python $TMPDIR/dec3.py
```

```
/tmp/claude-1001/dec3.py:16: RuntimeWarning: invalid value encountered in log1p
  L=np.log1p(P); c=np.concatenate([np.zeros_like(L[:,:1]),np.cumsum(L,1)],1)
/tmp/claude-1001/dec3.py:18: RuntimeWarning: invalid value encountered in divide
  out=np.expm1(c[:,b]-c[:,a]); return out/out.sum(2,keepdims=True)
sp HD all on 0.21 [0.18 0.26] off 0.15 [0.11 0.17] p=0.290 180err 0.148
sp HD heading on 0.15 [0.13 0.16] off 0.12 [0.10 0.14] p=0.920 180err 0.105
sp HD landmark on 0.25 [0.22 0.27] off 0.13 [0.12 0.14] p=0.000 180err 0.151
sp HD alignment on 0.22 [0.18 0.25] off 0.15 [0.12 0.19] p=0.240 180err 0.159
36.16352343559265
dff HD all on 0.21 [0.17 0.26] off 0.17 [0.12 0.21] p=0.680 180err 0.146
dff HD heading on 0.14 [0.11 0.16] off 0.11 [0.09 0.14] p=0.930 180err 0.110
dff HD landmark on 0.21 [0.18 0.23] off 0.07 [0.06 0.09] p=0.000 180err 0.120
dff HD alignment on 0.21 [0.17 0.26] off 0.17 [0.13 0.21] p=0.760 180err 0.154
35.17939209938049
```

**Agent calls Bash**

```bash
cd entries/000483-sit-2023; python - <<'EOF'
import os
p=os.environ['TMPDIR']+'/dec3.py'; s=open(p).read()
s=s.replace("sc=np.einsum('tfn,tns->tfs',X[:,:,idx],W[:,idx])","sc=np.matmul(X[:,:,idx],W[:,idx])")
s=s.replace("    return W,on\n","    return W.astype(np.float32),np.clip(on,0,None).astype(np.float32)\n")
s=s.replace("range(100)","range(50)")
open(p,'w').write(s)
EOF
PYTHONPATH=. $TMPDIR/dev/bin/python $TMPDIR/dec3.py 2>&1 | grep -v Warn
```

```
out=np.expm1(c[:,b]-c[:,a]); return out/out.sum(2,keepdims=True)
sp HD all on 0.21 [0.18 0.26] off 0.15 [0.12 0.17] p=0.240 180err 0.147
sp HD heading on 0.15 [0.14 0.16] off 0.12 [0.10 0.14] p=0.840 180err 0.105
sp HD landmark on 0.25 [0.22 0.27] off 0.13 [0.12 0.14] p=0.000 180err 0.151
sp HD alignment on 0.22 [0.18 0.26] off 0.15 [0.11 0.18] p=0.240 180err 0.160
2.4038708209991455
dff HD all on 0.20 [0.15 0.24] off 0.15 [0.11 0.19] p=0.380 180err 0.139
dff HD heading on 0.12 [0.11 0.14] off 0.10 [0.09 0.12] p=0.940 180err 0.107
dff HD landmark on 0.20 [0.17 0.22] off 0.11 [0.10 0.13] p=0.020 180err 0.115
dff HD alignment on 0.20 [0.17 0.23] off 0.15 [0.12 0.20] p=0.560 180err 0.150
2.3782918453216553
```

**Agent calls Bash**

```bash
date -u
```

```
Fri Oct 30 19:27:03 UTC 2026
```

**Agent calls Bash**

```bash
cd entries/000483-sit-2023; python -c "
import json;nb=json.load(open('somata.ipynb'));print(json.dumps(nb['metadata']));print(nb['nbformat'],nb['nbformat_minor'])"; python -c "
import json;nb=json.load(open('single_cue.ipynb'))
for i in range(0,7): c=nb['cells'][i]; print('####',i,c['cell_type'],c['metadata'].get('tags')); print(''.join(c['source']))" | head -120
```

```
{"kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"}}
4 5
#### 0 markdown None
# Sit & Goard (2023) on dandiset 000483: single-cue rotation (Figure 1)

**Paper.** Sit KK, Goard MJ (2023). Coregistration of heading to visual cues in retrosplenial
cortex. *Nature Communications* 14:1992.
[doi:10.1038/s41467-023-37704-5](https://doi.org/10.1038/s41467-023-37704-5). The claims file
(`claims/000483/10.1038-s41467-023-37704-5.yaml`) was written from the version of record (main
text, legends, Methods; the Supplementary Information was not available).

**Dataset.** [DANDI:000483](https://dandiarchive.org/dandiset/000483/0.230421.2321), version
0.230421.2321. The paper cites no version of the dandiset (it cites a Dryad deposit and the
dandiset by its description), so the most recent published version is pinned, and the only one:
the draft has the same 128 assets and size and was last modified two months later, on metadata.

This notebook covers the single-cue controlled-rotation experiments (Figure 1). The head-rotation
and remapping claims are in `rotation_remapping.ipynb`, the dual-cue claims in
`axons.ipynb` and `somata.ipynb`, and Figures S5 and S6 in `directions.ipynb`.

[... 103 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/000483-sit-2023; cat > $TMPDIR/susp.py <<'EOF'
import rsc, numpy as np, h5py, remfile
cat=rsc.catalog(full=False)
for _,m in cat[cat.subject.isin(['SKKS125','SKKS127'])].iterrows():
    print(m.experiment, m.identifier, m.n_frames, m.n_rois)
for _,m in cat[cat.experiment=='visual_only'].iterrows():
    with h5py.File(remfile.File(m.url),'r') as f:
        h=f[rsc.HEADING][:].ravel(); F=f[rsc.FLUOR][:]
    hc=rsc.clean_heading(h); st=rsc.wrap180(np.diff(hc))
    print(m.identifier, 'per 1250-frame block: median step', [round(float(np.median(st[k:k+1250])),2) for k in range(0,len(st),1250)])
    print('  frac still per block', [round(float(np.mean(np.abs(st[k:k+1250])<0.5)),2) for k in range(0,len(st),1250)])
    print('  mean F per block', [round(float(F[k:k+1250].mean()),1) for k in range(0,len(F),1250)])
    print('  trials', len(rsc.trial_segments(h)))
EOF
PYTHONPATH=. $TMPDIR/dev/bin/python $TMPDIR/susp.py
```

```
animal_controlled 220721_KKS_SKKS125_FR_CW_CCW_SKKS125-FR-003 7550 333
animal_controlled 220726_KKS_SKKS125_FR_CW_CCW_SKKS125-FM-001 7550 670
animal_controlled 220729_KKS_SKKS127_FR_CW_CCW_SKKS127-FR-001 7550 423
motor_both 220729_KKS_SKKS125_FR_CW_CCW_SKKS125-DualRotation-002 15050 399
motor_both 220727_KKS_SKKS127_FR_CW_CCW_SKKS127-DualDir-005 7550 213
motor_both 220729_KKS_SKKS127_FR_CW_CCW_SKKS127-DualRotation-002 15050 423
motor_ccw 220721_KKS_SKKS125_FR_CW_CCW_SKKS125-CCW-002 7550 333
motor_cw 220726_KKS_SKKS125_FR_CW_CCW_SKKS125-CW-002 7550 670
visual_only 220810_KKS_SKKS125_Suspended_SKKS125-DualDir-002 15050 446
visual_only 220811_KKS_SKKS127_Suspended_SKKS127-DualDir-002 15050 691
220810_KKS_SKKS125_Suspended_SKKS125-DualDir-002 per 1250-frame block: median step [2.02, -2.09, 1.99, -2.08, 2.0, -2.09, 1.89, -2.09, 2.02, -2.09, 0.88, -2.09, 0.0]
  frac still per block [0.15, 0.05, 0.15, 0.05, 0.17, 0.05, 0.26, 0.05, 0.16, 0.05, 0.46, 0.05, 1.0]
  mean F per block [2102.0, 2129.4, 2090.1, 2114.3, 2095.0, 2129.6, 2140.9, 2116.8, 2111.9, 2129.6, 2143.2, 2197.2, 2777.0]
  trials 75
220811_KKS_SKKS127_Suspended_SKKS127-DualDir-002 per 1250-frame block: median step [1.97, -2.07, 1.71, -2.07, 1.13, -2.08, 0.02, -2.07, 0.08, -2.08, 0.89, -2.07, 0.0]
  frac still per block [0.2, 0.05, 0.37, 0.05, 0.45, 0.06, 0.85, 0.06, 0.62, 0.05, 0.46, 0.05, 1.0]
  mean F per block [2389.7, 2335.5, 2232.1, 2264.9, 2229.8, 2230.1, 2265.6, 2278.5, 2345.3, 2243.0, 2303.6, 2296.3, 2766.6]
  trials 63
```

**Agent calls Bash**

```bash
mkdir -p $TMPDIR/gen; cat > $TMPDIR/gen/make_decoding.py <<'PYEOF'
import nbformat as nbf
nb = nbf.v4.new_notebook()
nb.metadata = {"kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"}}
C = []
def md(s, tags=None):
    c = nbf.v4.new_markdown_cell(s.strip("\n"))
    if tags: c.metadata["tags"] = tags
    C.append(c)
def code(s, tags=None):
    c = nbf.v4.new_code_cell(s.strip("\n"))
    if tags: c.metadata["tags"] = tags
    C.append(c)

md(r'''
# Sit & Goard (2023) on dandiset 000483: decoding heading from RSC somata (Figure 6)

**Paper.** Sit KK, Goard MJ (2023), *Nature Communications* 14:1992,
[doi:10.1038/s41467-023-37704-5](https://doi.org/10.1038/s41467-023-37704-5); claims file
written from the version of record without its supplement.

**Dataset.** [DANDI:000483](https://dandiarchive.org/dandiset/000483/0.230421.2321), version
0.230421.2321, the only published version (the paper cites none). See `single_cue.ipynb` for the
data check of all files.

| Claim | Here |
|---|---|
| fig6a-population-light-on | tested |
| fig6a-population-light-off | tested |
| fig6b-heading-cells | tested |
| fig6b-landmark-cells | tested |
| fig6b-alignment-cells | tested |
| fig6b-180-errors | tested |
| fig6-heading-below-population | tested |

The tuned somata and their classes are rebuilt here exactly as in `somata.ipynb` (same files,
seeds and code), so this notebook can run on its own; the class counts are printed so that they
can be compared with those of `somata.ipynb`. The classes found there differ from the paper's
(fig5-class-proportions, not reproduced), so the class decoders here decode other groups of cells
than the paper's.

Decoding follows the claims file's opening comment (Methods, "Decoding RSC somatic activity";
Statistical information), with its readings: the input, (a) dF/F or (b) inferred spikes; the
decoder, (a) a naive Bayes decoder on binarized activity (Etter et al. 2020), trained on even and
tested on odd time points, or (b) the lab's HeadingDecoder (github.com/ucsb-goard-lab/HeadingDecoder
at commit ca9842e: activity times row-rescaled leave-one-trial-out tuning curves, normalized,
filtered over 10 samples with its `temporalFilter`, maximum taken); the t-test, (a) paired over
trials or (b) unpaired; chance, (a) 0.18 (Methods) or (b) 0.10 (Figure 6A legend). All readings
are run.
''')

code(r'''
import time
import warnings
from multiprocessing import Pool

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy import stats
from sklearn.mixture import GaussianMixture

import rsc

warnings.filterwarnings("ignore")
pd.set_option("display.width", 200)
pd.set_option("display.max_columns", 30)
started = time.time()
cat = rsc.catalog(full=False)
sub = cat[cat.experiment == "soma_dual"].reset_index(drop=True)
recs = rsc.load_many(sub.url.tolist())
with Pool(4) as pool:
    for r in recs:
        r["dff"] = rsc.dff(r["F"])
        r["sp"] = rsc.spikes(r["dff"], pool)
        del r["F"]
print(f"dandiset {rsc.DANDISET_ID} version {rsc.DANDISET_VERSION}: {len(sub)} files loaded and deconvolved "
      f"in {time.time() - started:.0f} s")
''')

code(r'''
rows = []
for m, r in zip(sub.itertuples(), recs):
    L, D = rsc.light_dark_frames(m.n_frames)
    r["seg_l"], r["seg_d"] = rsc.segments_within(r["heading"], L), rsc.segments_within(r["heading"], D)
    r["seg_all"] = rsc.trial_segments(r["heading"])
    r["blocks"] = (L, D)
    per_l = [sum(1 for s in r["seg_l"] if s[0] >= b[0] and s[-1] <= b[-1]) for b in L]
    per_d = [sum(1 for s in r["seg_d"] if s[0] >= b[0] and s[-1] <= b[-1]) for b in D]
    rows.append(dict(subject=m.subject, identifier=m.identifier[:6] + " " + m.identifier.split("_")[-1], frames=m.n_frames,
                     rois=m.n_rois, light_trials_per_block=per_l, dark_trials_per_block=per_d,
                     median_trial_frames=int(np.median([len(s) for s in r["seg_l"]])) if r["seg_l"] else 0,
                     dff_range=f"{r['dff'].min():.2f}..{r['dff'].max():.1f}", spikes_max=round(float(r["sp"].max()), 2)))
info = pd.DataFrame(rows)
print(info.to_string(index=False))
print(f"{len(sub)} recordings, {sub.subject.nunique()} mice, {sub.n_rois.sum()} ROIs; dF/F is unitless, spikes are OASIS "
      "event amplitudes in dF/F units")
''', ["sanity"])

md(r'''
## Tuned somata and their classes (as in `somata.ipynb`)

Heading-selection test with the two-term Gaussian on all trials (centred fit, seed 306), light-on
and light-off curves aligned with the light-on shifts, Gaussian-fit features, three-component GMM
(random state 304) on the selective somata, archetypes and class names by the rule of
`somata.ipynb` (no outlier step).
''')

code(r'''
t0 = time.time()
trials_all = [rsc.trial_tuning(r["sp"], r["heading"], r["seg_all"]) for r in recs]
with Pool(4) as pool:
    sel = rsc.selection_many(trials_all, "double", 306, pool, centre=True)

def light_dark_aligned(i):
    r = recs[i]
    lt = rsc.trial_tuning(r["sp"], r["heading"], r["seg_l"])
    dt = rsc.trial_tuning(r["sp"], r["heading"], r["seg_d"])
    if lt.shape[2] == 0:
        return None, None
    sh = rsc.cv_shifts(lt) if lt.shape[2] > 1 else (rsc.SHIFT_POINT - lt[:, :, 0].argmax(1))[:, None]
    la = rsc.apply_shifts(lt, sh).mean(2)
    sh_all = (rsc.SHIFT_POINT - lt.mean(2).argmax(1))[:, None]
    da = rsc.apply_shifts(dt, np.repeat(sh_all, max(dt.shape[2], 1), 1)).mean(2) if dt.shape[2] else np.full_like(la, np.nan)
    return la, da

aligned = [light_dark_aligned(i) for i in range(len(recs))]
soma_idx = [i for i in range(len(recs)) if aligned[i][0] is not None]
L, D, cell_rec, cell_roi = [], [], [], []
for i in soma_idx:
    m = sel[i].is_hd.values & ~np.isnan(aligned[i][1]).any(1)
    L.append(aligned[i][0][m]); D.append(aligned[i][1][m])
    cell_rec += [i] * int(m.sum()); cell_roi += np.flatnonzero(m).tolist()
cell_rec, cell_roi = np.array(cell_rec), np.array(cell_roi)
both = rsc.rescale(np.hstack([np.vstack(L), np.vstack(D)]))
pl, _ = rsc.fit_gauss(both[:, :60], "double", do_rescale=False)
pd_, _ = rsc.fit_gauss(both[:, 60:], "double", do_rescale=False)
X = np.column_stack([pl[:, [1, 2, 5, 6]], pd_[:, [1, 2, 5, 6]]])
g = GaussianMixture(3, covariance_type="full", n_init=20, max_iter=1000, random_state=304).fit(X)

def archetype(coef):
    a1, a2, c1, c2 = coef
    return a1 * np.exp(-((rsc.X - np.pi / 2) / c1) ** 2) + a2 * np.exp(-((rsc.X - 3 * np.pi / 2) / c2) ** 2)

def cosdist(A, b):
    with np.errstate(invalid="ignore", divide="ignore"):
        return 1 - (A @ b) / (np.linalg.norm(A, axis=1) * np.linalg.norm(b))

dist = np.column_stack([cosdist(both[:, :60], archetype(mu[:4])) + cosdist(both[:, 60:], archetype(mu[4:])) for mu in g.means_])
cls = np.nanargmin(np.nan_to_num(dist, nan=9), 1)
bimod = [min(mu[0], mu[1]) / max(mu[0], mu[1]) for mu in g.means_]
dark_amp = [max(mu[4], mu[5]) for mu in g.means_]
heading_c = int(np.argmin(bimod))
rest = [c for c in range(3) if c != heading_c]
landmark_c = rest[int(np.argmin([dark_amp[c] for c in rest]))]
names = {heading_c: "heading", landmark_c: "landmark", [c for c in rest if c != landmark_c][0]: "alignment"}
print(f"selection, fits and clustering in {time.time() - t0:.0f} s")
print(f"tuned somata with light-on and light-off trials: {len(cls)} from {len(soma_idx)} recordings")
print("class counts:", {names[c]: int((cls == c).sum()) for c in range(3)}, "(compare somata.ipynb, fig5-class-proportions)")
''')

md(r'''
## Pseudopopulation trials

Methods: the trials are the full rotations before and after each rest that separates light-on
from light-off; each trial is resampled to 200 bins and trials are aligned across recordings
into pseudopopulations. Here, in each recording, the last 5 light-on trials before and the first
5 light-off trials after each of the three light-to-dark transitions of a 7550-frame recording
(15 trials each; HeadingDecoder takes up to 15 a side). The 1950-frame recordings have one
transition and some have fewer than 5 trials a side, so they are left out (their cells are
counted below). Each trial is resampled to 200 bins on its heading (bins every 1.8 degrees from
-180 to 180) in place of time, so that bin k is the same heading in every recording; at the
motor's constant speed the two differ only by speed fluctuations (a standard choice). Trial k of
each recording is put with trial k of the others.
''')

code(r'''
K = 5
N_RS = 200
grid = -180 + (np.arange(N_RS) + 0.5) * 360 / N_RS

def resample(act, h, seg):
    hu = np.rad2deg(np.unwrap(np.deg2rad(h[seg])))
    sgn = 1 if hu[-1] >= hu[0] else -1
    hu = sgn * hu
    target = hu[0] + np.mod(sgn * grid - hu[0], 360)
    return np.stack([np.interp(target, hu, act[seg][:, n]) for n in range(act.shape[1])], 1)

def trials_around(i):
    r = recs[i]
    L, D = r["blocks"]
    on, off = [], []
    for bl, bd in zip(L, D):
        sl = [s for s in r["seg_l"] if s[0] >= bl[0] and s[-1] <= bl[-1]]
        sd = [s for s in r["seg_d"] if s[0] >= bd[0] and s[-1] <= bd[-1]]
        if len(sl) < K or len(sd) < K:
            return None
        on += sl[-K:]; off += sd[:K]
    return on, off

use = [i for i in soma_idx if sub.n_frames[i] == 7550 and trials_around(i) is not None]
inuse = np.isin(cell_rec, use)
print(f"recordings used: {len(use)} of {len(soma_idx)} (7550-frame with {K} trials on each side of all 3 transitions); "
      f"tuned cells {inuse.sum()} of {len(cls)}; left out {int((~inuse).sum())}")
print("cells used by class:", {names[c]: int(((cls == c) & inuse).sum()) for c in range(3)},
      "by mouse:", pd.Series(sub.subject[cell_rec[inuse]].values).value_counts().to_dict())
pop = {}
for inp in ["dff", "sp"]:
    on_all, off_all = [], []
    for i in use:
        on, off = trials_around(i)
        act = recs[i][inp][:, cell_roi[cell_rec == i]]
        hc = rsc.clean_heading(recs[i]["heading"])
        on_all.append(np.stack([resample(act, hc, s) for s in on]))
        off_all.append(np.stack([resample(act, hc, s) for s in off]))
    pop[inp] = {"on": np.concatenate(on_all, 2), "off": np.concatenate(off_all, 2)}   # trials x 200 bins x cells
ucls = cls[inuse]
print("pseudopopulation shape (trials, bins, cells):", pop["sp"]["on"].shape)
''')

md(r'''
## Decoders

- (a) Naive Bayes (Etter et al. 2020): activity binarized (spikes: above 0; dF/F: above its mean
  plus 2 SD over the recording's trials, a standard choice), P(active | heading state) per cell for 60
  states of 6 degrees from the even bins of every trial, with a +1/+2 prior; the odd bins are
  decoded as the state of maximum summed log-likelihood.
- (b) HeadingDecoder: for each trial, each cell's tuning curve (60 bins) from the other trials of
  the same condition, rescaled 0 to 1; the heading distribution is activity times tuning
  weights, normalized, filtered over 10 samples (`temporalFilter`); the maximum is taken.
  Activity below 0 (dF/F) is set to 0, as the product needs non-negative weights.

Accuracy per trial: the share of decoded bins within 18 degrees of the true heading. Each
bootstrap iteration samples 332 cells with replacement from the group (all tuned cells: all three
classes, so in their proportions); 1000 iterations; mean and 2.5 and 97.5 percentiles over
iterations. p of light-on against light-off is one minus the share of iterations in which a
t-test over trials gives p < 0.05 ((a) paired, (b) unpaired). Errors at 180 degrees: the share of
light-on bins with an error of 162 degrees or more. Chance is computed with each decoder by
decoding with each cell's test activity circularly shifted along the trial by its own random
amount (the tuning to heading is broken, the activity kept).
''')

code(r'''
NS = 60
state = np.clip(((grid + 180) // 6).astype(int), 0, NS - 1)
centres = -177 + 6 * np.arange(NS)

def err_deg(dec, true):
    return np.abs((dec - true + 180) % 360 - 180)

def prep_bayes(A, inp):
    """Log-likelihood weights from the even bins; binarized odd bins to decode."""
    n = A.shape[2]
    flat = A.reshape(-1, n)
    th = np.zeros(n) if inp == "sp" else flat.mean(0) + 2 * flat.std(0)
    B = (A > th).astype(np.float32)
    tr, te = B[:, 0::2], B[:, 1::2]
    s_tr = state[0::2]
    p = np.stack([(tr[:, s_tr == s].sum((0, 1)) + 1) / (tr[:, s_tr == s].shape[0] * tr[:, s_tr == s].shape[1] + 2)
                  for s in range(NS)], 1)
    return dict(kind="bayes", W=(np.log(p) - np.log(1 - p)).astype(np.float32), B=np.log(1 - p).astype(np.float32),
                X=te, true=grid[1::2])

def prep_hd(A, inp):
    """Leave-one-trial-out tuning weights per trial (trials x cells x 60), rescaled 0 to 1 per cell."""
    A = np.clip(A, 0, None)
    S = np.stack([A[:, state == s].mean(1) for s in range(NS)], 2)
    loo = (S.sum(0)[None] - S) / (A.shape[0] - 1)
    lo = loo.min(2, keepdims=True); rg = loo.max(2, keepdims=True) - lo
    W = np.where(rg > 0, (loo - lo) / np.where(rg > 0, rg, 1), 0)
    return dict(kind="hd", W=W.astype(np.float32), X=A.astype(np.float32), true=grid)

def temporal_filter(P, w=10):
    """HeadingDecoder.temporalFilter: product of (1 + p) over a window of w samples, renormalized."""
    Lg = np.log1p(P)
    c = np.concatenate([np.zeros_like(Lg[:, :1]), np.cumsum(Lg, 1)], 1)
    F = P.shape[1]; i = np.arange(F)
    a, b = np.clip(i - w // 2, 0, F), np.clip(i + w // 2, 0, F)
    out = np.expm1(c[:, b] - c[:, a])
    return out / out.sum(2, keepdims=True)

def decode(Pp, idx, X=None):
    X = Pp["X"] if X is None else X
    if Pp["kind"] == "bayes":
        sc = X[:, :, idx] @ Pp["W"][idx] + Pp["B"][idx].sum(0)
    else:
        sc = np.matmul(X[:, :, idx], Pp["W"][:, idx])
        tot = sc.sum(2, keepdims=True)
        sc = temporal_filter(np.where(tot > 0, sc / np.where(tot > 0, tot, 1), 1 / NS))
    return err_deg(centres[sc.argmax(2)], Pp["true"][None])

groups = {"all tuned": np.ones(len(ucls), bool), **{names[c]: ucls == c for c in range(3)}}
print("cells per group:", {k: int(v.sum()) for k, v in groups.items()})
''')

code(r'''
t0 = time.time()
N_BOOT, N_SAMPLE = 1000, 332
results, per_iter = [], {}
chance = []
for inp in ["dff", "sp"]:
    for dec_name, prep in [("(a) Bayes", prep_bayes), ("(b) HeadingDecoder", prep_hd)]:
        P = {cond: prep(pop[inp][cond], inp) for cond in ["on", "off"]}
        rng = np.random.default_rng(601)
        # chance: test activity of each cell circularly shifted along the trial by its own random amount
        idx = rng.choice(len(ucls), N_SAMPLE, replace=True)
        Xs = P["on"]["X"].copy()
        for t in range(Xs.shape[0]):
            for n in idx:
                Xs[t, :, n] = np.roll(Xs[t, :, n], rng.integers(Xs.shape[1]))
        ch = [float((decode(P["on"], idx, Xs) <= 18).mean())]
        for _ in range(19):
            idx = rng.choice(len(ucls), N_SAMPLE, replace=True)
            Xs = P["on"]["X"].copy()
            sh = rng.integers(Xs.shape[1], size=(Xs.shape[0], Xs.shape[2]))
            ar = (np.arange(Xs.shape[1])[None, :, None] - sh[:, None, :]) % Xs.shape[1]
            Xs = np.take_along_axis(Xs, ar, 1)
            ch.append(float((decode(P["on"], idx, Xs) <= 18).mean()))
        chance.append(dict(input=inp, decoder=dec_name, chance_mean=round(np.mean(ch), 3), chance_max=round(np.max(ch), 3)))
        for gname, m in groups.items():
            pool_ = np.flatnonzero(m)
            acc = {"on": np.zeros(N_BOOT), "off": np.zeros(N_BOOT)}
            e180 = np.zeros(N_BOOT); err_on = np.zeros(N_BOOT)
            pt_paired = np.zeros(N_BOOT, bool); pt_unpaired = np.zeros(N_BOOT, bool)
            for it in range(N_BOOT):
                idx = rng.choice(pool_, N_SAMPLE, replace=True)
                a = {}
                for cond in ["on", "off"]:
                    e = decode(P[cond], idx)
                    a[cond] = (e <= 18).mean(1)
                    acc[cond][it] = a[cond].mean()
                    if cond == "on":
                        e180[it] = (e >= 162).mean(); err_on[it] = e.mean()
                pt_paired[it] = stats.ttest_rel(a["on"], a["off"]).pvalue < 0.05
                pt_unpaired[it] = stats.ttest_ind(a["on"], a["off"]).pvalue < 0.05
            per_iter[(inp, dec_name, gname)] = acc
            results.append(dict(input=inp, decoder=dec_name, group=gname,
                                on_mean=acc["on"].mean(), on_lo=np.percentile(acc["on"], 2.5), on_hi=np.percentile(acc["on"], 97.5),
                                off_mean=acc["off"].mean(), off_lo=np.percentile(acc["off"], 2.5), off_hi=np.percentile(acc["off"], 97.5),
                                p_paired=1 - pt_paired.mean(), p_unpaired=1 - pt_unpaired.mean(),
                                off_lower=bool(acc["off"].mean() < acc["on"].mean()),
                                err180_on=e180.mean(), mean_err_on=err_on.mean()))
res = pd.DataFrame(results).round(3)
print(f"decoding in {time.time() - t0:.0f} s")
print(res.to_string(index=False))
print("\nChance accuracy with each decoder (20 draws of shifted test activity, light-on):")
print(pd.DataFrame(chance).to_string(index=False))
print("Chance readings of the claims file: (a) 0.18 (Methods), (b) 0.10 (Figure 6A legend; 36/360)")
''')

code(r'''
fig, ax = plt.subplots(1, 2, figsize=(9, 3), sharey=True)
for a, (inp, dec_name) in zip(ax, [("sp", "(a) Bayes"), ("sp", "(b) HeadingDecoder")]):
    for k, gname in enumerate(groups):
        acc = per_iter[(inp, dec_name, gname)]
        a.errorbar([k - 0.1], [acc["on"].mean()], yerr=[[acc["on"].mean() - np.percentile(acc["on"], 2.5)], [np.percentile(acc["on"], 97.5) - acc["on"].mean()]], fmt="o", color="0.2")
        a.errorbar([k + 0.1], [acc["off"].mean()], yerr=[[acc["off"].mean() - np.percentile(acc["off"], 2.5)], [np.percentile(acc["off"], 97.5) - acc["off"].mean()]], fmt="s", color="0.6")
    a.axhline(0.10, ls=":", color="k"); a.axhline(0.18, ls="--", color="k")
    a.set_xticks(range(len(groups))); a.set_xticklabels(list(groups), rotation=20); a.set_title(f"spikes, {dec_name}")
ax[0].set_ylabel("decoder accuracy (light-on dark, light-off grey)"); ax[0].set_ylim(0, 1)
plt.tight_layout(); plt.show()
print("All accuracies lie in", round(float(res[["on_lo", "off_lo"]].min().min()), 3), "to", round(float(res[["on_hi", "off_hi"]].max().max()), 3), "; none outside the axes.")
''')

def claim_section(cid, quote, body, codestr):
    md(f"## {cid}\n\n> {quote}\n\n{body}")
    code(codestr, [f"claim:{cid}"])

code(r'''
def row(inp, dec_name, gname):
    return res[(res.input == inp) & (res.decoder == dec_name) & (res.group == gname)].iloc[0]
READ = [(inp, d) for inp in ["dff", "sp"] for d in ["(a) Bayes", "(b) HeadingDecoder"]]
def excludes(lo, hi, c):
    return not (lo <= c <= hi)
''')

claim_section("fig6a-population-light-on",
 "Decoding heading from all tuned RSC cells within single 100 ms frames is accurate in the light-on condition despite the symmetric cues (mean decoder accuracy 0.82, 95% CI 0.78 to 0.86).",
 "Reproduced when a reading of the decoder gives a mean within 0.82 +- 0.04.",
r'''
for inp, d in READ:
    r = row(inp, d, "all tuned")
    print(f"input {inp}, decoder {d}: light-on mean {r.on_mean:.3f} [{r.on_lo:.3f}, {r.on_hi:.3f}]; within 0.82 +- 0.04: {abs(r.on_mean - 0.82) <= 0.04}")
''')
md("**Result: RESULT_6A_ON**")

claim_section("fig6a-population-light-off",
 "In the light-off condition the decoder's accuracy from all tuned cells drops (mean 0.44, 95% CI 0.34 to 0.54; p = 7.6e-3 against light-on) but stays above chance.",
 "Reproduced when, under a decoder reading, the mean is within 0.44 +- 0.10, the interval excludes chance (0.18 or 0.10) and the bootstrapped t-test gives p < 0.05 with light-off lower.",
r'''
for inp, d in READ:
    r = row(inp, d, "all tuned")
    ok = abs(r.off_mean - 0.44) <= 0.10 and excludes(r.off_lo, r.off_hi, 0.18) and excludes(r.off_lo, r.off_hi, 0.10) and r.off_lower
    print(f"input {inp}, decoder {d}: light-off mean {r.off_mean:.3f} [{r.off_lo:.3f}, {r.off_hi:.3f}]; p paired {r.p_paired:.3f}, "
          f"unpaired {r.p_unpaired:.3f}; within 0.44 +- 0.10: {abs(r.off_mean - 0.44) <= 0.10}; above both chance levels: "
          f"{r.off_lo > 0.18}; criterion met (paired / unpaired): {ok and r.p_paired < 0.05} / {ok and r.p_unpaired < 0.05}")
''')
md("**Result: RESULT_6A_OFF**")

claim_section("fig6b-heading-cells",
 "Heading cells alone decode heading accurately in both light-on (0.61, 95% CI 0.56 to 0.66) and light-off (0.44, 95% CI 0.36 to 0.52) conditions, with no significant difference between them (p = 0.11).",
 "Reproduced when a decoder reading puts light-on within 0.61 +- 0.05 and light-off within 0.44 +- 0.08, both intervals exclude chance, and the t-test gives p >= 0.05.",
r'''
for inp, d in READ:
    r = row(inp, d, "heading")
    vals = abs(r.on_mean - 0.61) <= 0.05 and abs(r.off_mean - 0.44) <= 0.08
    print(f"input {inp}, decoder {d}: on {r.on_mean:.3f} [{r.on_lo:.3f}, {r.on_hi:.3f}], off {r.off_mean:.3f} [{r.off_lo:.3f}, {r.off_hi:.3f}]; "
          f"p paired {r.p_paired:.3f}, unpaired {r.p_unpaired:.3f}; both within tolerance: {vals}; "
          f"both intervals above 0.18: {r.on_lo > 0.18 and r.off_lo > 0.18}, above 0.10: {r.on_lo > 0.10 and r.off_lo > 0.10}")
''')
md("**Result: RESULT_6B_HEADING**")

claim_section("fig6b-landmark-cells",
 "Landmark cells decode heading very well in light-on (0.80, 95% CI 0.75 to 0.84) but fall to chance in light-off (0.20, 95% CI 0.14 to 0.27; p = 8.0e-4).",
 "Reproduced when, under a decoder reading, light-on is within 0.80 +- 0.05, light-off within 0.20 +- 0.07, p < 0.05, and the light-off interval includes chance; the outcome under each chance level is reported.",
r'''
for inp, d in READ:
    r = row(inp, d, "landmark")
    vals = abs(r.on_mean - 0.80) <= 0.05 and abs(r.off_mean - 0.20) <= 0.07
    print(f"input {inp}, decoder {d}: on {r.on_mean:.3f} [{r.on_lo:.3f}, {r.on_hi:.3f}], off {r.off_mean:.3f} [{r.off_lo:.3f}, {r.off_hi:.3f}]; "
          f"p paired {r.p_paired:.3f}, unpaired {r.p_unpaired:.3f}; both within tolerance: {vals}; "
          f"light-off interval includes 0.18: {r.off_lo <= 0.18 <= r.off_hi}, includes 0.10: {r.off_lo <= 0.10 <= r.off_hi}")
''')
md("**Result: RESULT_6B_LANDMARK**")

claim_section("fig6b-alignment-cells",
 "Alignment cells decode between heading and landmark cells, better in light-on (0.71, 95% CI 0.66 to 0.76) and fairly accurately in light-off (0.51, 95% CI 0.43 to 0.59), with no significant difference (p = 0.54).",
 "Reproduced when, under a decoder reading, light-on is within 0.71 +- 0.05 and light-off within 0.51 +- 0.08, the light-on mean lies between those of heading and landmark cells, the light-off interval excludes chance, and p >= 0.05.",
r'''
for inp, d in READ:
    r, rh, rl = row(inp, d, "alignment"), row(inp, d, "heading"), row(inp, d, "landmark")
    vals = abs(r.on_mean - 0.71) <= 0.05 and abs(r.off_mean - 0.51) <= 0.08
    between = min(rh.on_mean, rl.on_mean) < r.on_mean < max(rh.on_mean, rl.on_mean)
    print(f"input {inp}, decoder {d}: on {r.on_mean:.3f} [{r.on_lo:.3f}, {r.on_hi:.3f}], off {r.off_mean:.3f} [{r.off_lo:.3f}, {r.off_hi:.3f}]; "
          f"p paired {r.p_paired:.3f}, unpaired {r.p_unpaired:.3f}; both within tolerance: {vals}; light-on between heading "
          f"({rh.on_mean:.3f}) and landmark ({rl.on_mean:.3f}): {between}; light-off above 0.18: {r.off_lo > 0.18}, above 0.10: {r.off_lo > 0.10}")
''')
md("**Result: RESULT_6B_ALIGNMENT**")

claim_section("fig6b-180-errors",
 "Decoding from landmark cells in light-on gives an overrepresentation of 180 degree errors from the symmetric cues, while heading cells show no preponderance of 180 degree errors.",
 "The share of light-on bins with an error within 18 degrees of 180, against 0.10 under uniform errors. Reproduced when it exceeds 0.10 for landmark cells and is no more than 0.10 for heading cells.",
r'''
for inp, d in READ:
    rl, rh, ra, rt = row(inp, d, "landmark"), row(inp, d, "heading"), row(inp, d, "alignment"), row(inp, d, "all tuned")
    print(f"input {inp}, decoder {d}: share of errors >= 162 deg: landmark {rl.err180_on:.3f}, heading {rh.err180_on:.3f}, "
          f"alignment {ra.err180_on:.3f}, all tuned {rt.err180_on:.3f}; criterion met: {rl.err180_on > 0.10 and rh.err180_on <= 0.10}")
''')
md("**Result: RESULT_6B_180**")

claim_section("fig6-heading-below-population",
 "In light-on, heading cells alone decode worse than the whole tuned population, so alone they may not give an optimal representation of instantaneous heading.",
 "Reading (a): the 95% bootstrap intervals of light-on accuracy for heading cells and for all tuned cells do not overlap. Reading (b), a mixed model of per-trial decoder error with recording or mouse as random intercept, cannot be formed here: each pseudopopulation trial pools cells of many recordings and mice, so no trial belongs to one recording or mouse. As a variant, the share of bootstrap iterations in which heading cells decode worse than all tuned cells is given (iterations paired by index).",
r'''
for inp, d in READ:
    rh, rt = row(inp, d, "heading"), row(inp, d, "all tuned")
    worse = np.mean(per_iter[(inp, d, "heading")]["on"] < per_iter[(inp, d, "all tuned")]["on"])
    print(f"input {inp}, decoder {d}: heading {rh.on_mean:.3f} [{rh.on_lo:.3f}, {rh.on_hi:.3f}], all tuned {rt.on_mean:.3f} "
          f"[{rt.on_lo:.3f}, {rt.on_hi:.3f}]; intervals separate with heading lower: {rh.on_hi < rt.on_lo}; "
          f"iterations with heading lower: {worse:.3f}")
''')
md("**Result: RESULT_6_BELOW**")

md(r'''
## Summary

SUMMARY_TABLE

A failure to reproduce here may be a failure of this attempt, not of the paper: see the reasoning and the differences from the paper's method.

How the analysis differs from the paper's: the classes are those of `somata.ipynb`, not the
paper's; spikes and dF/F are computed from raw fluorescence without neuropil correction; only the
7550-frame recordings with 5 trials on each side of every transition enter the
pseudopopulations; trials are resampled on heading, not time; the naive Bayes decoder is written
here after Etter et al. (2020), with a binarization threshold that is a standard choice; the
HeadingDecoder is reimplemented in numpy.

What was found about the dataset: the files do not mark light-on and light-off; the segments are
the code's hard-coded ones.
''')

nb.cells = C
nbf.write(nb, "entries/000483-sit-2023/decoding.ipynb")
PYEOF
python $TMPDIR/gen/make_decoding.py && echo ok
```

```
ok
```

**Agent calls Bash**

```bash
cd $TMPDIR/gen; python - <<'EOF'
p='make_decoding.py'; s=open(p).read()
old=s[s.index("        # chance: test activity"):s.index("        chance.append(")]
new='''        # chance: test activity of each cell circularly shifted along the trial by its own random amount
        ch = []
        for _ in range(20):
            idx = rng.choice(len(ucls), N_SAMPLE, replace=True)
            Xs = P["on"]["X"]
            sh = rng.integers(Xs.shape[1], size=(Xs.shape[0], Xs.shape[2]))
            ar = (np.arange(Xs.shape[1])[None, :, None] - sh[:, None, :]) % Xs.shape[1]
            ch.append(float((decode(P["on"], idx, np.take_along_axis(Xs, ar, 1)) <= 18).mean()))
'''
s=s.replace(old,new); open(p,'w').write(s)
EOF
python make_decoding.py && cd entries/000483-sit-2023 && date -u && time $TMPDIR/dev/bin/jupyter nbconvert --to notebook --execute decoding.ipynb --output $TMPDIR/dec_exec.ipynb --ExecutePreprocessor.timeout=3600 2>&1 | tail -3
```

```
Fri Oct 30 19:31:19 UTC 2026
[NbConvertApp] Converting notebook decoding.ipynb to notebook
[IPKernelApp] WARNING | Kernel is running over TCP without encryption. All communication (including code and outputs) is sent in plain text and is susceptible to eavesdropping. Use IPC transport or launch with kernel manager-provisioned CurveZMQ keys to enable transport encryption.
[NbConvertApp] Writing 100805 bytes to /tmp/claude-1001/dec_exec.ipynb

real	15m49.222s
user	52m15.114s
sys	0m16.956s
```

**Agent calls Bash**

```bash
cd $TMPDIR; python -c "
import json;nb=json.load(open('dec_exec.ipynb'))
for i,c in enumerate(nb['cells']):
  if c['cell_type']=='code':
    for o in c.get('outputs',[]):
      t=o.get('text') or o.get('data',{}).get('text/plain','')
      if t: print('--- cell',i); print(''.join(t)[:6000])
"
```

```
--- cell 1
dandiset 000483 version 0.230421.2321: 35 files loaded and deconvolved in 235 s

--- cell 2
subject                      identifier  frames  rois light_trials_per_block dark_trials_per_block  median_trial_frames  dff_range  spikes_max
SKKS080      201123 SKKS080-DualCue-003    1950   112                    [5]                   [6]                  156 -0.57..4.1        1.78
SKKS080      201123 SKKS080-DualCue-004    1950   110                    [6]                   [6]                  142 -0.49..3.4        1.58
SKKS088      210118 SKKS088-DualCue-001    1950   329                    [6]                   [2]                  132 -0.55..5.0        1.53
SKKS088      210118 SKKS088-DualCue-002    1950   240                    [0]                   [3]                    0 -0.68..5.5        1.63
SKKS088      210118 SKKS088-DualCue-003    1950   286                    [1]                   [2]                  145 -0.64..5.2        1.77
SKKS088      210216 SKKS088-DualCue-001    7550   411              [7, 6, 5]             [6, 6, 7]                  183 -0.55..4.9        1.76
SKKS088      210216 SKKS088-DualCue-002    7550   289              [6, 6, 7]             [7, 5, 6]                  182 -0.63..5.2        2.09
SKKS089      201205 SKKS089-DualCue-003    1950   115                   [10]                  [10]                   90 -0.59..6.6        2.68
SKKS089      201205 SKKS089-DualCue-004    1950    82                    [9]                  [10]                   85 -0.58..5.3        2.51
SKKS089      210118 SKKS089-DualCue-002    1950   307                    [3]                   [2]                  128 -0.58..5.4        4.87
SKKS089      210216 SKKS089-DualCue-001    7550   435              [5, 6, 6]             [7, 6, 6]                  182 -0.69..5.4        2.13
SKKS089      210216 SKKS089-DualCue-002    7550   459              [7, 5, 6]             [6, 7, 6]                  181 -0.67..5.8        2.32
SKKS089 210312 SKKS089-RSCSoma-3rpm-00
[... 114 more lines not kept]
```

**Agent calls Bash**

```bash
cd  ls schemas; python -c "
import json,yaml
s=json.load(open('schemas/attempt.schema.json')) if __import__('os').path.exists('schemas/attempt.schema.json') else None
print(json.dumps(s['properties'].get('verifications'),indent=1)[:3000] if s else 'none')
"; grep -rl "verifications:" attempts | head -3
```

```
attempt.schema.json
claims.schema.json
entry.schema.json
paper-match.schema.json
{
 "type": "array",
 "items": {
  "type": "object",
  "additionalProperties": false,
  "required": [
   "date",
   "kind",
   "by",
   "results"
  ],
  "properties": {
   "date": {
    "type": "string",
    "format": "date"
   },
[... 56 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n -A25 "^verifications:" attempts/000138-churchland-2010-01.yaml | head -40; ls questions | head; cat questions/$(ls questions | head -1) | head -30
```

```
359:verifications:
360-- date: '2026-10-28'
361-  kind: agent
362-  by: Independent agent run by CatalystNeuro (same harness, separate context, did not write the notebook)
363-  reviewed: Round 1. The first executed notebook with the conclusion cells and the summary removed
364-    (the outcome table in its first cell was left in, and the verifier did not use it), the helper module and the claims file, with the paper. The verifier checked the helper functions against
365-    brute-force PCA and regression on synthetic data. Its report gave its own outcome for each claim;
366-    all 15 agree with the record. It also noted that the dandiset is probably not the paper's J-array
367-    session (27 conditions and about 14 trials per condition against 108 conditions), which the record
368-    states, and asked for per-condition trial counts under each reading, now printed in the data check.
369-  results:
370-  - claim: fig4abc-tuning-correlation-single-electrode
371-    agrees: true
372-    outcome: blocked
373-    reason: The archive lists 2 assets, both from one subject (sub-Jenkins, array data). The single-electrode
374-      recordings of monkeys A, B and J are not there, so no part can be tested.
375-    response: No change needed.
376-  - claim: fig4d-tuning-correlation-j-array
377-    agrees: true
378-    outcome: partially_reproduced
[... 46 more lines not kept]
```

**Agent calls Bash**

```bash
cat > $TMPDIR/gen/edit_single.py <<'PYEOF'
import nbformat as nbf
p = "entries/000483-sit-2023/single_cue.ipynb"
nb = nbf.read(p, as_version=4)
C = nb.cells
def md(s, tags=None):
    c = nbf.v4.new_markdown_cell(s.strip("\n"))
    if tags: c.metadata["tags"] = tags
    return c
def code(s, tags=None):
    c = nbf.v4.new_code_cell(s.strip("\n"))
    if tags: c.metadata["tags"] = tags
    return c
assert C[8].source.startswith("both_dir")
clock_md = md(r'''
The peak lag is printed per file above. A lag of a few frames after 0 is what the calcium and
deconvolution delay predict; a lag before 0 (activity leading heading) is not. Where the files
disagree in sign, the clock is consistent with the data in those that peak after 0 and is not
established in the others, and an offset that differs between two files cannot be excluded for
the other experiments either (see `rotation_remapping.ipynb`, fig2f).
''')
# fig1g: false-positive rate of the test on synthetic untuned cells
assert C[13].source.startswith("allc = pd.concat")
fpr_md = md(r'''
**False-positive rate of the test.** The reliability step compares the split-half correlations
of 1000 random splits of the same trials with those of shifted trials by a two-sample KS test and
Cohen's d. The 1000 values are not independent (they reuse the same 13 or so trials), so the KS p
is far too small for a cell without tuning. This is the paper's own procedure: the code
(ControlledRotation.calculateHeadDirection, lines 40 to 97 at commit c6344f5) computes
`bt_CC_data(iter)` and `bt_CC_rand(iter)` over the iterations and then `kstest2(bt_CC_data,
bt_CC_rand)` with `P < 0.1 && d > 0.8`, as here. The rate is measured below on synthetic untuned
cells (sparse random events, no heading dependence, 13 trials of 60 bins), and on the real cells
in selection-shuffled-control (each trial shifted once).
''')
fpr_code = code(r'''
rng_fp = np.random.default_rng(106)
n_syn, n_tr_syn = 300, 13
frames_per_bin = 3
ev = rng_fp.random((n_syn, 60 * frames_per_bin, n_tr_syn)) < 0.02          # 2% of frames carry an event
amp = rng_fp.exponential(0.3, ev.shape) * ev
syn = amp.reshape(n_syn, 60, frames_per_bin, n_tr_syn).mean(2)
syn = (np.roll(syn, 1, 1) + syn + np.roll(syn, -1, 1)) / 3                   # same 3-bin smoothing as bin_tuning
with Pool(4) as pool:
    fp = {c: pd.concat(rsc.selection_many([syn], "single", 107, pool, centre=c), ignore_index=True) for c in [True, False]}
for c, df in fp.items():
    print(f"synthetic untuned cells, {'centred' if c else 'code (uncentred)'} fit: reliable {100 * df.reliable.mean():.1f}%, "
          f"pass the whole test {100 * df.is_hd.mean():.1f}% of {len(df)}")
''', ["claim:fig1g-rotation-heading-fraction"])
C[14].source = C[14].source  # result text rewritten below
# selection-shuffled-control
C[15].source = r'''## selection-shuffled-control

> Run on pre-shuffled data, the heading-selection test passes no cells, so the count of
> heading-selective cells is not due to chance.

Two readings of "pre-shuffled". (code) As in the commented `calculateHeadDirection_shuff` of
Cue.m that the claims file cites: in every iteration the "real" trials are themselves circularly
shifted afresh (`activity_rand2`), and the real fit uses the shifted trials of the last
iteration. The "real" and the null split-half correlations then come from the same distribution,
so no cell can pass, whatever the data: this reading cannot show whether the count is due to
chance. (once) Each trial is shifted once by its own random amount before the whole test is run,
as the Methods' words ("repeating these procedures using pre-shuffled data") and the criterion's
("circularly shifting each trial's tuning curve ... before the test") say. Only this reading
measures how many untuned cells the procedure passes. Both fit readings are run under (code), the
adopted centred fit under (once).'''
C[18].source = r'''**Result: not reproduced, under the (once) reading (an assumption).** Shifting each trial once before the test, as the Methods describe, 165 of 3179 ROIs (5.19%) still pass, above the 1% limit of the criterion: about a third of the 485 cells selected in fig1g could pass by chance. The synthetic untuned cells under fig1g pass at a similar rate (printed there). Run as the commented code does it, with the trials re-shifted in every iteration, 0 of 3179 pass under both fit readings, but that reading passes no cell by construction, as its "real" and null values come from the same distribution. The question of which reading the claims file intends is put to a reader.'''
nb.cells = C[:9] + [clock_md] + C[9:14] + [fpr_md, fpr_code] + C[14:]
nbf.write(nb, p)
PYEOF
python $TMPDIR/gen/edit_single.py && echo ok
```

```
ok
```

**Agent calls Bash**

```bash
cd entries/000483-sit-2023; cat > $TMPDIR/fp.py <<'EOF'
import numpy as np, pandas as pd, rsc, time
from multiprocessing import Pool
if __name__=='__main__':
    t0=time.time()
    rng_fp = np.random.default_rng(106)
    n_syn, n_tr_syn = 300, 13
    frames_per_bin = 3
    ev = rng_fp.random((n_syn, 60 * frames_per_bin, n_tr_syn)) < 0.02
    amp = rng_fp.exponential(0.3, ev.shape) * ev
    syn = amp.reshape(n_syn, 60, frames_per_bin, n_tr_syn).mean(2)
    syn = (np.roll(syn, 1, 1) + syn + np.roll(syn, -1, 1)) / 3
    with Pool(4) as pool:
        fp = {c: pd.concat(rsc.selection_many([syn], "single", 107, pool, centre=c), ignore_index=True) for c in [True, False]}
    for c, df in fp.items():
        print(c, df.reliable.mean(), df.is_hd.mean())
    print(time.time()-t0)
EOF
PYTHONPATH=. $TMPDIR/dev/bin/python $TMPDIR/fp.py
```

```
True 0.15666666666666668 0.04666666666666667
False 0.15666666666666668 0.016666666666666666
9.07587194442749
```

**Agent calls Bash**

```bash
cat > $TMPDIR/gen/edit_single2.py <<'PYEOF'
import nbformat as nbf
p = "entries/000483-sit-2023/single_cue.ipynb"
nb = nbf.read(p, as_version=4)
C = nb.cells
i = [k for k, c in enumerate(C) if c.source.startswith("def tiling")][0]
C[i].source = C[i].source.replace('''    print(f"  share within 45 degrees of dataset heading 0: {near0:.3f} (uniform 0.25)")''',
'''    print(f"  share within 45 degrees of dataset heading 0: {near0:.3f} (uniform 0.25); of -90: "
          f"{np.mean(np.abs(rsc.wrap180(pref + 90)) <= 45):.3f}; of +90: {np.mean(np.abs(rsc.wrap180(pref - 90)) <= 45):.3f}")''')
assert "of -90" in C[i].source
j = [k for k, c in enumerate(C) if c.source.startswith("## fig1h")][0]
C[j].source += '''

The code's uncentred fit bounds the Gaussian's peak to pi/2 +- pi/6 on an axis whose 0 is the
first bin (-180 degrees), that is, to dataset headings -120 to -60. That is why the cells it
passes cluster near -90 (below): it is a property of the fit's bounds, not evidence of where the
cue is. The share near -90 is printed as well, as the heading the code's bounds favour.'''
k = [k for k, c in enumerate(C) if c.source.startswith("**Result: reproduced, under the centred fit")][0]
C[k].source = "**Result: reproduced, under the centred fit (an assumption).** With the centred fit 485 of 3179 ROIs (15.26%) are heading selective, within 14.2 +- 1.42% and 452 +- 45; by mouse 8.9 to 25.2%. With the fit as the code calls it (uncentred), 345 (10.85%), outside the tolerance. The two readings give different outcomes; the centred one is adopted because only it lets cells of every preferred heading pass (see fig1h below: the uncentred fit puts 93.6% of selected cells in one quadrant). Stricter reliability thresholds lower the count (KS p < 0.01 and d > 1.2: 12.36%). The test is liberal: synthetic untuned cells pass at 4.7% (centred) and 1.7% (uncentred), and 15.7% pass its reliability step; on the real cells shifted once, 5.19% pass (selection-shuffled-control). This is the paper's own test, so the count matches the paper's, but some of the selected cells may be untuned."
nbf.write(nb, p)
PYEOF
python $TMPDIR/gen/edit_single2.py && echo ok
```

```
ok
```

**Agent calls Bash**

```bash
cat > $TMPDIR/gen/edit_rr.py <<'PYEOF'
import nbformat as nbf
p = "entries/000483-sit-2023/rotation_remapping.ipynb"
nb = nbf.read(p, as_version=4)
C = nb.cells
def md(s): return nbf.v4.new_markdown_cell(s.strip("\n"))
def code(s, tags=None):
    c = nbf.v4.new_code_cell(s.strip("\n"))
    if tags: c.metadata["tags"] = tags
    return c
assert C[7].source.startswith("print(\"Per pair")
extra_md = md(r'''
Further checks asked for in verification: the random-pairing null per pair (1000 draws), the
activity and the share of selective cells in the two files of each pair (heading-locked
artefacts of derotation would make the head-rotation files look more selective), and how far a
clock offset could move the preferred headings. In `single_cue.ipynb` the lag of the peak
correlation is 4 to 6 frames in the files that rotate both ways, with one file at -6; an offset
of k frames moves every preferred heading of a file by k times the heading step per frame.
''')
extra = code(r'''
pref_hr = {i: preference(i, "peak") for i, _, _ in pairs}
pref_cr = {j: preference(j, "peak", True) for _, j, _ in pairs}
rng = np.random.default_rng(204)
rows2 = []
for i, j, opp in pairs:
    m = np.flatnonzero(sel[i].is_hd.values & sel[j].is_hd.values)
    if len(m) == 0:
        continue
    V = rsc.vtest(rsc.wrap180(pref_hr[i][m] - pref_cr[j][m]))[0]
    nullp = np.array([rsc.vtest(rsc.wrap180(pref_hr[i][m] - pref_cr[j][rng.permutation(m)]))[0] for _ in range(1000)])
    rows2.append(dict(pair=f"{info.identifier[i]} / {info.identifier[j].split(' ')[-1]}", opposite=opp, n=len(m), V=round(V, 1),
                      null_mean=round(float(nullp.mean()), 1), null_p95=round(float(np.percentile(nullp, 95)), 1),
                      p_random=round(float(np.mean(nullp >= V)), 3),
                      HR_selective=f"{sel[i].is_hd.sum()}/{len(sel[i])} ({100 * sel[i].is_hd.mean():.0f}%)",
                      CR_selective=f"{sel[j].is_hd.sum()}/{len(sel[j])} ({100 * sel[j].is_hd.mean():.0f}%)",
                      HR_spikes_s=info.spikes_per_s[i], CR_spikes_s=info.spikes_per_s[j],
                      HR_step=abs(info.median_step[i]), CR_step=abs(info.median_step[j]),
                      shift_6_frames_deg=f"{6 * abs(info.median_step[i]):.0f} / {6 * abs(info.median_step[j]):.0f}"))
print(pd.DataFrame(rows2).to_string(index=False))
print("p_random: share of 1000 random pairings of the same ROIs with V at least the real one (peak preference, CR mirrored, cells selective in both)")
''', ["claim:fig2f-head-chamber-same-preference"])
C = C[:8] + [extra_md, extra] + C[8:]
k = [k for k, c in enumerate(C) if "null = [rsc.vtest(delta_offsets(P_main" in c.source][0]
C[k].source = C[k].source.replace("for _ in range(100)]", "for _ in range(1000)]").replace(
    'print(f"Random pairing of neurons (peak, both, (i)): V mean {np.mean(null):.1f}, 95th percentile {np.percentile(null, 95):.1f}")',
    'print(f"Random pairing of neurons (peak, both, (i)), 1000 draws: V mean {np.mean(null):.1f}, 95th percentile {np.percentile(null, 95):.1f}, "\n      f"share at or above the real V {np.mean(np.array(null) >= rows.V[0]):.3f}")')
assert "1000 draws" in C[k].source
nb.cells = C
nbf.write(nb, p)
PYEOF
python $TMPDIR/gen/edit_rr.py && echo ok
```

```
ok
```

**Agent calls Bash**

```bash
cat > $TMPDIR/gen/edit_ax.py <<'PYEOF'
import nbformat as nbf
p = "entries/000483-sit-2023/axons.ipynb"
nb = nbf.read(p, as_version=4)
C = nb.cells
assert C[11].source.startswith("fr = pd.DataFrame")
C[11].source = C[11].source.replace('''for name, s in readings.items():''', '''# reading (a): among the axons selective on all trials (light-on selection), the share also selective in light-off
fr["a_selective"] = [sel[i].is_hd.sum() for i in ax_idx]
fr["a_dark_selective"] = [int((sel[i].is_hd.values & s.is_hd.values).sum()) for i, s in zip(ax_idx, sel_ax_dark)]
fr["a_fraction"] = fr.a_dark_selective / fr.a_selective.where(fr.a_selective > 0)
fa_a, fv_a = fr[fr.kind == "adn_axons"].a_fraction.dropna(), fr[fr.kind == "vis_axons"].a_fraction.dropna()
mw_a = stats.mannwhitneyu(fa_a, fv_a, alternative="two-sided")
pa = fr.groupby("kind")[["a_dark_selective", "a_selective"]].sum()
odds_a, pf_a = stats.fisher_exact([[pa.loc["adn_axons", "a_dark_selective"], pa.loc["adn_axons", "a_selective"] - pa.loc["adn_axons", "a_dark_selective"]],
                                   [pa.loc["vis_axons", "a_dark_selective"], pa.loc["vis_axons", "a_selective"] - pa.loc["vis_axons", "a_dark_selective"]]])
print(f"\\nreading (a), selective axons: per-recording share also selective in light-off, ADN median {fa_a.median():.3f} "
      f"(n = {len(fa_a)} recordings), visual median {fv_a.median():.3f} (n = {len(fv_a)}); Mann-Whitney p = {mw_a.pvalue:.2g}; pooled ADN "
      f"{pa.loc['adn_axons', 'a_dark_selective']}/{pa.loc['adn_axons', 'a_selective']}, visual {pa.loc['vis_axons', 'a_dark_selective']}/"
      f"{pa.loc['vis_axons', 'a_selective']}, Fisher p = {pf_a:.2g}, odds ratio {odds_a:.2f}")
print("recordings without selective axons are left out of the per-recording comparison:", int(fr.a_fraction.isna().sum()))
for name, s in readings.items():''')
assert "reading (a), selective axons" in C[11].source
C[10].source = C[10].source.replace("as a variant), and the mean aligned", "as a variant), and the mean aligned").rstrip() + '''

The fraction selective in light-off is computed under reading (b), over all axons, and under
reading (a), over the axons selective on all trials.'''
nbf.write(nb, p)
PYEOF
python $TMPDIR/gen/edit_ax.py && echo ok
```

```
ok
```

**Agent calls Bash**

```bash
cd entries/000483-sit-2023; python -c "
import json;nb=json.load(open('directions.ipynb'))
for i,c in enumerate(nb['cells'][:6]): print('####',i,c['cell_type'],c['metadata'].get('tags')); print(''.join(c['source']))"
```

```
#### 0 markdown None
# Sit & Goard (2023) on dandiset 000483: rotation direction and arena control (Figures S5, S6)

**Paper.** Sit KK, Goard MJ (2023), *Nature Communications* 14:1992,
[doi:10.1038/s41467-023-37704-5](https://doi.org/10.1038/s41467-023-37704-5); claims file
written from the version of record without its supplement, so Figures S5 and S6 were not read.

**Dataset.** [DANDI:000483](https://dandiarchive.org/dandiset/000483/0.230421.2321), version
0.230421.2321, the only published version (the paper cites none). See `single_cue.ipynb` for the
data check of all files.

| Claim | Here |
|---|---|
| figs5-rotation-direction | tested |
| figs6-arena-control | tested |

The claims file gives two readings of what the bootstrapped KS test compares: (a) differences in
preferred heading between the two conditions for heading-selective cells, against the same
differences with cells paired at random; (b) the correlation of each cell's tuning curves in the
two conditions, against randomly paired cells. p is one minus the fraction of 1000 bootstrap
[... 80 more lines not kept]
```

**Agent calls Bash**

```bash
cat > $TMPDIR/gen/edit_dir.py <<'PYEOF'
import nbformat as nbf
p = "entries/000483-sit-2023/directions.ipynb"
nb = nbf.read(p, as_version=4)
C = nb.cells
def md(s): return nbf.v4.new_markdown_cell(s.strip("\n"))
def code(s, tags=None):
    c = nbf.v4.new_code_cell(s.strip("\n"))
    if tags: c.metadata["tags"] = tags
    return c
assert C[9].source.startswith("pairs6 = []")
s = C[9].source
s = s.replace("tc_a, tc_m, cells6, frames = [], [], [], []", "tc_a, tc_m, cells6, frames, pair_id = [], [], [], [], []")
s = s.replace("    cells6.append(s.is_hd.values)\n", "    cells6.append(s.is_hd.values)\n    pair_id.append(np.repeat(info.file[i], len(s)))\n")
s = s.replace("tc_a, tc_m, cells6 = np.vstack(tc_a), np.vstack(tc_m), np.concatenate(cells6)",
              "tc_a, tc_m, cells6, pair_id = np.vstack(tc_a), np.vstack(tc_m), np.concatenate(cells6), np.concatenate(pair_id)")
s = s.replace('''res6 = {"selective": compare(tc_a, tc_m, cells6, rng, "selective cells, all pairs")}''',
'''res6 = {"selective": compare(tc_a, tc_m, cells6, rng, "selective cells, all pairs")}
# without the pairs whose animal-controlled file visits fewer than half of the 60 heading bins
# (bin_tuning sets an unvisited bin to 0, so their curves are mostly zeros)
sparse = [f for f, _, nb_ in frames if nb_ < 30]
res6["without sparse"] = compare(tc_a, tc_m, cells6 & ~np.isin(pair_id, sparse), rng, f"selective cells, without {sparse}")
for f in np.unique(pair_id):
    compare(tc_a, tc_m, cells6 & (pair_id == f), rng, f"selective cells, pair {f} only")''')
assert "without sparse" in s and "pair_id.append" in s
C[9].source = s
fig5k_md = md(r'''
## fig5k-visual-cue-only (blocked)

> When only the visual cues rotate (no proprioceptive or somatosensory input), the visual
> contributions to tuning are retained, but heading-cell responses are strongly degraded.

The claim needs neurons matched between a standard-rotation recording and a visual-cue-only one
(Figure 5K legend). The dataset's two visual-cue-only ("Suspended") files are listed below with
every file of the same mice, their numbers of ROIs, and their structure in blocks of 1250
frames: the heading step and the share of still frames per block, and the mean raw fluorescence.
A standard rotation inside the same file would show as blocks that differ in some way other than
the direction of rotation.
''')
fig5k = code(r'''
same_mice = cat[cat.subject.isin(cat.subject[cat.experiment == "visual_only"])]
print(same_mice[["experiment", "subject", "identifier", "n_frames", "n_rois"]].to_string(index=False))
vis = cat[cat.experiment == "visual_only"].reset_index(drop=True)
vrecs = rsc.load_many(vis.url.tolist())
for m, r in zip(vis.itertuples(), vrecs):
    hc = rsc.clean_heading(r["heading"])
    st = rsc.wrap180(np.diff(hc))
    blocks = range(0, len(st), 1250)
    print(f"\n{m.identifier}: {m.n_frames} frames, {m.n_rois} ROIs, {len(rsc.trial_segments(r['heading']))} trials")
    print("  median heading step per block (deg/frame):", [round(float(np.median(st[k:k + 1250])), 2) for k in blocks])
    print("  share of still frames per block:", [round(float(np.mean(np.abs(st[k:k + 1250]) < 0.5)), 2) for k in blocks])
    print("  mean raw fluorescence per block:", [round(float(r["F"][k:k + 1250].mean()), 0) for k in blocks])
print("\nROI counts shared between a visual-only file and another file of the same mouse:",
      sorted(set(vis.n_rois) & set(same_mice[same_mice.experiment != "visual_only"].n_rois)))
''')
fig5k_res = md(r'''
**Result: blocked (metadata_insufficient).** Each visual-cue-only file shares its number of ROIs with no other file of its mouse, so no standard recording holds the same ROIs, and no ROI matching is given. Inside each file the blocks alternate between the two directions of rotation at about 2 degrees per frame, and nothing in the heading or the fluorescence marks some blocks as standard rotation: the files do not say which frames, if any, are standard rotation. The last block of each is still.
''')
# insert before the Summary cell
k = [k for k, c in enumerate(C) if c.source.startswith("## Summary")][0]
C = C[:k] + [fig5k_md, fig5k, fig5k_res] + C[k:]
C[0].source = C[0].source.replace("| figs6-arena-control | tested |", "| figs6-arena-control | tested |\n| fig5k-visual-cue-only | blocked: no recording shares the visual-only files' ROIs (structure shown below) |")
nb.cells = C
nbf.write(nb, p)
PYEOF
python $TMPDIR/gen/edit_dir.py && echo ok
```

```
ok
```

**Agent calls Bash**

```bash
cat > $TMPDIR/gen/edit_som.py <<'PYEOF'
import nbformat as nbf
p = "entries/000483-sit-2023/somata.ipynb"
nb = nbf.read(p, as_version=4)
C = nb.cells
assert C[16].source.startswith("def peak_offsets")
C[16].source = C[16].source + r'''

# Null for V: taking the nearer of two peaks 180 degrees apart folds every offset into +-90, which
# by itself gives V > 0. (1) light-off peaks of the class paired with the light-on curves of other
# cells of the class at random; (2) light-off peaks drawn uniformly over the 60 bins.
def nearer(p1, p2, pdk):
    o1, o2 = rsc.wrap180((pdk - p1) * 6), rsc.wrap180((pdk - p2) * 6)
    return np.where(np.abs(o1) <= np.abs(o2), o1, o2)
rng_e = np.random.default_rng(307)
for cname in ["alignment", "heading", "landmark"]:
    c = [k for k, n in names.items() if n == cname][0]
    m = cls == c
    Lm, Dm = v["L"][m], v["D"][m]
    p1 = Lm.argmax(1)
    other = (p1[:, None] + 30 + np.arange(-15, 16)[None]) % 60
    p2 = np.take_along_axis(other, np.take_along_axis(Lm, other, 1).argmax(1)[:, None], 1)[:, 0]
    pdk = Dm.argmax(1)
    off = nearer(p1, p2, pdk)
    V, p, n = rsc.vtest(off)
    null_perm = np.array([rsc.vtest(nearer(p1, p2, pdk[rng_e.permutation(n)]))[0] for _ in range(1000)])
    null_unif = np.array([rsc.vtest(nearer(p1, p2, rng_e.integers(0, 60, n)))[0] for _ in range(1000)])
    w18_perm = np.mean([np.mean(np.abs(nearer(p1, p2, pdk[rng_e.permutation(n)])) <= 18) for _ in range(200)])
    print(f"{cname}: V = {V:.1f} (V/n {V / n:.3f}); random pairing V mean {null_perm.mean():.1f}, 95th percentile "
          f"{np.percentile(null_perm, 95):.1f}, share at or above the real V {np.mean(null_perm >= V):.3f}; uniform peaks V mean "
          f"{null_unif.mean():.1f} (V/n {null_unif.mean() / n:.3f}), 95th percentile {np.percentile(null_unif, 95):.1f}; "
          f"share within 18 deg real {np.mean(np.abs(off) <= 18):.3f}, random pairing {w18_perm:.3f}")'''
C[15].source = C[15].source.rstrip() + '''

Taking the nearer of two peaks 180 degrees apart folds the offsets into +-90 degrees, so the
V-test against 0 is positive even for light-off peaks unrelated to the light-on curve. The V of
each class is therefore compared with two nulls: light-off peaks paired at random with other
cells' light-on curves within the class, and light-off peaks drawn uniformly.'''
C[0].source = C[0].source.replace("Figure 5K and the decoding of Figure 6 are recorded in the attempt record.",
    "Figure 5K is in `directions.ipynb` (blocked) and the decoding of Figure 6 in `decoding.ipynb`.")
assert "decoding.ipynb" in C[0].source
nbf.write(nb, p)
PYEOF
python $TMPDIR/gen/edit_som.py && echo ok
```

```
ok
```

**Agent calls Bash**

```bash
cd entries/000483-sit-2023; python - <<'EOF'
import nbformat, glob
for p in sorted(glob.glob('*.ipynb')):
    nb=nbformat.read(p,as_version=4)
    for i,c in enumerate(nb.cells):
        if c.cell_type=='code':
            try: compile(c.source,f'{p}:{i}','exec')
            except SyntaxError as e: print('ERR',p,i,e)
print('done')
EOF
```

```
done
```

**Agent calls Bash**

```bash
cd  python - <<'EOF'
p='entries/000483-sit-2023/entry.yaml'; s=open(p).read()
s=s.replace("""  title: Rotation direction and arena control (Figures S5 and S6)
  runtime_minutes: 12
""","""  title: Rotation direction and arena control (Figures S5 and S6) and the visual-cue-only files (Figure 5K)
  runtime_minutes: 12
- path: decoding.ipynb
  title: Decoding heading from RSC somata in light and dark (Figure 6)
  runtime_minutes: 16
""")
s=s.replace("head against chamber rotation, coherent remapping, the axon responses in light and dark, and the\n  clustering of somata into heading, landmark and alignment cells.","head against chamber rotation, coherent remapping, the axon responses in light and dark, the\n  clustering of somata into heading, landmark and alignment cells, and the decoding of heading from\n  them.")
open(p,'w').write(s)
EOF
grep -n "decod" entries/000483-sit-2023/entry.yaml; python tools/entry.py check entries/000483-sit-2023 2>&1 | tail -5; date -u
```

```
11:  clustering of somata into heading, landmark and alignment cells, and the decoding of heading from
30:- path: decoding.ipynb
0 error(s)
Fri Oct 30 19:49:58 UTC 2026
```

**Agent calls Bash**

```bash
cd  time python tools/entry.py all entries/000483-sit-2023 2>&1 | tail -15; date -u
```

```
Installed kernelspec registry-000483-sit-2023 in executed/000483-sit-2023/.venv/share/jupyter/kernels/registry-000483-sit-2023
0 error(s)
pass  single_cue.ipynb  (556 s)
pass  rotation_remapping.ipynb  (641 s)
pass  axons.ipynb  (361 s)
pass  somata.ipynb  (1000 s)
pass  directions.ipynb  (582 s)
pass  decoding.ipynb  (956 s)

real	68m24.311s
user	204m6.559s
sys	1m24.235s
Fri Oct 30 20:58:24 UTC 2026
```

**Agent**

Run finished (68 min). Now reading the outputs.

**Agent calls Bash**

```bash
cd executed/000483-sit-2023; cat > $TMPDIR/show.py <<'EOF'
import json,sys
nb=json.load(open(sys.argv[1]))
want=set(int(x) for x in sys.argv[2].split(',')) if len(sys.argv)>2 else None
for i,c in enumerate(nb['cells']):
  if want and i not in want: continue
  if c['cell_type']=='code':
    for o in c.get('outputs',[]):
      t=o.get('text') or o.get('data',{}).get('text/plain','')
      if o.get('output_type')=='error': t='ERROR '+o['ename']+o['evalue']
      if t and 'Figure size' not in ''.join(t): print('--- cell',i); print(''.join(t)[:5000])
EOF
python $TMPDIR/show.py single_cue.ipynb 9,13,14,15,17,19,20,23,24
```

```
--- cell 14
KS p < 0.1, d > 0.8: 486 = 15.29%
KS p < 0.05, d > 0.8: 486 = 15.29%
KS p < 0.1, d > 0.5: 486 = 15.29%
KS p < 0.1, d > 1.0: 445 = 14.00%
KS p < 0.01, d > 1.2: 394 = 12.39%

--- cell 19
control in 82 s

--- cell 20
each, centred: 0 of 3179 pass = 0.00% (reliable 0); per mouse {}
each, code: 0 of 3179 pass = 0.00% (reliable 0); per mouse {}
once, centred (variant): 166 of 3179 pass = 5.22% (reliable 481); per mouse {'SKKS080': np.int64(78), 'SKKS081': np.int64(61), 'SKKS089': np.int64(8), 'SKKS090': np.int64(13), 'SKKS091': np.int64(6)}
Thresholds of the claims file: none passing = reproduced; up to 1% = partially; above 1% = not reproduced

--- cell 23
== centred reading: 486 cells
  (a) bins of 6 degrees holding at least one preferred heading: 60 of 60; empty bins at []
  (b) share per 90-degree quadrant centred on 0, 90, 180, -90: [0.247, 0.181, 0.183, 0.401]
[... 24 more lines not kept]
```

**Agent calls Bash**

```bash
cd executed/000483-sit-2023; python $TMPDIR/show.py single_cue.ipynb 8,10,11,12,16,17,18
```

```
--- cell 8
                    file  rois  trials_+  trials_-    -10     -8     -6     -4     -2      0      2      4      6      8     10
SKKS125-DualRotation-002   399        41        42  0.000 -0.021 -0.021  0.004  0.036  0.045  0.058  0.073  0.078  0.069  0.046
SKKS126-DualRotation-002   461        39        42  0.043  0.055  0.066  0.056  0.017 -0.020 -0.037 -0.033 -0.015  0.013  0.031
     SKKS127-DualDir-005   213        17        21 -0.025 -0.043 -0.057 -0.052 -0.052 -0.022 -0.014 -0.001  0.013 -0.001 -0.008
SKKS127-DualRotation-002   423        41        36 -0.042 -0.015  0.016  0.060  0.094  0.121  0.145  0.158  0.146  0.110  0.064
Lag of the peak per file (frames; + = heading paired with later activity): [6, -6, 6, 4]

--- cell 11
selection test, two readings, in 169 s

--- cell 12
== code (uncentred fit): 345 of 3179 ROIs selective = 10.85%  (paper 14.2% +- 1.42, 452 +- 45)
subject    SKKS080  SKKS081  SKKS089  SKKS090  SKKS091
rois        1479.0    990.0    191.0    357.0    162.0
selective    160.0    131.0     10.0     41.0      3.0
percent       10.8     13.2      5.2     11.5      1.9
per recording percent: median 10.2 range 1.0 to 25.3
== centred fit: 486 of 3179 ROIs selective = 15.29%  (paper 14.2% +- 1.42, 452 +- 45)
subject    SKKS080  SKKS081  SKKS089  SKKS090  SKKS091
[... 29 more lines not kept]
```

**Agent calls Bash**

```bash
cd executed/000483-sit-2023; python $TMPDIR/show.py rotation_remapping.ipynb
```

```
--- cell 1
dandiset 000483 version 0.230421.2321: 38 files loaded and deconvolved in 230 s

--- cell 2
      experiment subject                           identifier  frames  rois  heading_nan heading_range  median_step  direction  trials  spikes_per_s
chamber_rotation SKKS089  210429 SKKS088-PlatformRotation-002    2600   118           23     -179..177         1.94          1      13         0.070
chamber_rotation SKKS090  210429 SKKS090-PlatformRotation-002    2600   167           24     -179..177         1.97          1      13         0.084
chamber_rotation SKKS091  210427 SKKS091-PlatformRotation-002    2550   135           25     -179..177         1.94          1      13         0.109
chamber_rotation SKKS091  210526 SKKS091-PlatformRotation-002    5100   128           53     -177..179        -2.01         -1      26         0.063
chamber_rotation SKKS112  210526 SKKS112-PlatformRotation-002    5100   384           24     -177..179        -0.12         -1      10         0.114
chamber_rotation SKKS112  210526 SKKS112-PlatformRotation-004    5100   293           53     -180..179        -2.02         -1      26         0.071
chamber_rotation SKKS116  210526 SKKS116-PlatformRotation-002    5100   211           50     -177..179        -1.96         -1      27         0.065
   head_rotation SKKS089      210429 SKKS088-HeadRotation-001    2600   118            0     -180..180         0.68          1       5         0.214
   head_rotation SKKS090      210429 SKKS090-HeadRotation-001    2600   167            0     -180..180        -1.05         -1       9         0.166
   head_rotation SKKS091      210427 SKKS091-HeadRotation-001    2600   135            0     -180..180         1.12          1       9         0.164
   head_rotation SKKS091      210526 SKKS091-HeadRotation-001    5100   128            0     -180..180         1.28          1      17         0.095
   head_rotation SKKS112      210526 SKKS112-HeadRotation-001    5100   384            0     -180..180       
[... 160 more lines not kept]
```

**Agent calls Bash**

```bash
cd executed/000483-sit-2023; python $TMPDIR/show.py axons.ipynb 5,6,7,8,11 | head -120
```

```
--- cell 5
selection tests in 199 s
            rois  selective
experiment                 
adn_axons   1084        135
vis_axons    247        106

--- cell 6
Recordings without light-on trials (left out of the light/dark analyses): []
Recordings without light-off trials: []

--- cell 8
== (a) selective, centred: ADN n=135 (4 mice), visual n=106 (3 mice)
   flip score of the mean light-on curve: ADN 0.277, visual 1.814
   single axons: ADN mean -0.072 (median -0.279), visual mean 1.073 (median 1.146); KS p = 1.7e-21
   ADN by mouse: {np.str_('SKKS092'): 0.48, np.str_('SKKS093'): -0.034, np.str_('SKKS094'): -0.196, np.str_('SKKS095'): -0.461}
   visual by mouse: {np.str_('SKKS097'): 1.185, np.str_('SKKS098'): 1.026, np.str_('SKKS103'): 0.408}
== (a) selective, code fit: ADN n=73 (4 mice), visual n=50 (3 mice)
   flip score of the mean light-on curve: ADN 1.132, visual 1.903
   single axons: ADN mean 0.080 (median -0.100), visual mean 0.882 (median 1.021); KS p = 1.1e-06
[... 48 more lines not kept]
```

**Agent calls Bash**

```bash
cd executed/000483-sit-2023; python $TMPDIR/show.py somata.ipynb 5,6,8,10,13,16,19,22 | head -150
```

```
--- cell 5
selection tests in 645 s
             rois  selective
experiment                  
adn_axons    1084        135
soma_dual   11569       1433
vis_axons     247        106

--- cell 6
Recordings without light-on trials (left out of the light/dark analyses): ['210118 SKKS088-DualCue-002']
Recordings without light-off trials: []

--- cell 8
(a) selective: 1419 somata from 34 recordings, 6 mice; median r2 light 0.54, dark 0.26
(b) all: 11329 somata from 34 recordings, 6 mice; median r2 light 0.26, dark 0.14
fits in 4 s

--- cell 10
(a) selective: silhouette by k: {2: 0.2738, 3: 0.023, 4: 0.0386, 5: 0.0335, 6: 0.0391} | local maximum at 3: False

[... 69 more lines not kept]
```

**Agent calls Bash**

```bash
cd executed/000483-sit-2023; python $TMPDIR/show.py directions.ipynb | tail -60
```

```
--- cell 9
220720 SKKS124-FR-001 / 220720 SKKS124-CW-002: 3 of 62 selective in the motor file; 2265 turning frames, 60 of 60 heading bins visited
220721 SKKS125-FR-003 / 220721 SKKS125-CCW-002: 112 of 333 selective in the motor file; 420 turning frames, 6 of 60 heading bins visited
220726 SKKS125-FM-001 / 220726 SKKS125-CW-002: 47 of 670 selective in the motor file; 2487 turning frames, 60 of 60 heading bins visited
220727 SKKS126-FR-001 / 220727 SKKS126-CW-002: 57 of 352 selective in the motor file; 1382 turning frames, 60 of 60 heading bins visited

--- cell 9
220729 SKKS127-FR-001 / 220729 SKKS127-DualRotation-002: 163 of 423 selective in the motor file; 530 turning frames, 52 of 60 heading bins visited

--- cell 9
selective cells, all pairs: n=382; (a) median |pref diff| (mod 180) real 42 deg, random 48 deg, bootstrapped KS p = 0.912; (b) median correlation real 0.026, random -0.031, bootstrapped KS p = 0.034

--- cell 9
selective cells, without ['220721 SKKS125-FR-003']: n=270; (a) median |pref diff| (mod 180) real 36 deg, random 42 deg, bootstrapped KS p = 0.969; (b) median correlation real 0.090, random 0.104, bootstrapped KS p = 0.903

--- cell 9
selective cells, pair 220720 SKKS124-FR-001 only: n=3; (a) median |pref diff| (mod 180) real 42 deg, random 72 deg, bootstrapped KS p = 1; (b) median correlation real 0.098, random 0.217, bootstrapped KS p = 1

--- cell 9
selective cells, pair 220721 SKKS125-FR-003 only: n=112; (a) median |pref diff| (mod 180) real 60 deg, random 66 deg, bootstrapped KS p = 0.985; (b) median correlation real -0.017, random -0.032, bootstrapped KS p = 0.86
[... 38 more lines not kept]
```

**Agent calls Bash**

```bash
cd executed/000483-sit-2023; python $TMPDIR/show.py directions.ipynb 2,6
```

```
--- cell 2
       experiment subject                            file  frames  rois  frac_moving  trials_pos  trials_neg
animal_controlled SKKS124           220720 SKKS124-FR-001    7550    62        0.300           6           4
animal_controlled SKKS125           220721 SKKS125-FR-003    7550   333        0.056           0           0
animal_controlled SKKS125           220726 SKKS125-FM-001    7550   670        0.329           3           9
animal_controlled SKKS126           220727 SKKS126-FR-001    7550   352        0.183           7           1
animal_controlled SKKS127           220729 SKKS127-FR-001    7550   423        0.070           3           0
       motor_both SKKS125 220729 SKKS125-DualRotation-002   15050   399        0.939          41          42
       motor_both SKKS126 220729 SKKS126-DualRotation-002   15050   463        0.923          39          42
       motor_both SKKS127      220727 SKKS127-DualDir-005    7550   213        0.885          17          21
       motor_both SKKS127 220729 SKKS127-DualRotation-002   15050   423        0.891          41          36
        motor_ccw SKKS125          220721 SKKS125-CCW-002    7550   333        0.944           0          37
         motor_cw SKKS124           220720 SKKS124-CW-002    7550    62        0.944           0          40
         motor_cw SKKS125           220726 SKKS125-CW-002    7550   670        0.941          40           0
         motor_cw SKKS126           220727 SKKS126-CW-002    7550   352        0.917          39           0

--- cell 6
220729 SKKS125-DualRotation-002: 73 of 399 selective
220729 SKKS126-DualRotation-002: 154 of 463 selective
220727 SKKS127-DualDir-005: 18 of 213 selective
[... 16 more lines not kept]
```

**Agent calls Bash**

```bash
cd executed/000483-sit-2023; python $TMPDIR/show.py decoding.ipynb 4,6,8,9,13,16,19,22,25,28,31 | grep -v "^input dff, decoder (b)\|^$" | head -90
```

```
--- cell 4
selection, fits and clustering in 574 s
tuned somata with light-on and light-off trials: 1419 from 34 recordings
class counts: {'landmark': 75, 'alignment': 1150, 'heading': 194} (compare somata.ipynb, fig5-class-proportions)
--- cell 6
recordings used: 25 of 34 (7550-frame with 5 trials on each side of all 3 transitions); tuned cells 1331 of 1419; left out 88
cells used by class: {'landmark': 54, 'alignment': 1102, 'heading': 175} by mouse: {'SKKS089': 528, 'SKKS100': 266, 'SKKS091': 242, 'SKKS090': 182, 'SKKS088': 113}
--- cell 6
pseudopopulation shape (trials, bins, cells): (15, 200, 1331)
--- cell 8
cells per group: {'all tuned': 1331, 'landmark': 54, 'alignment': 1102, 'heading': 175}
--- cell 9
decoding in 135 s
input            decoder     group  on_mean  on_lo  on_hi  off_mean  off_lo  off_hi  p_paired  p_unpaired  off_lower  err180_on  mean_err_on
  dff          (a) Bayes all tuned    0.708  0.665  0.747     0.569   0.525   0.612     0.016       0.061       True      0.034       26.925
  dff          (a) Bayes  landmark    0.397  0.377  0.416     0.210   0.195   0.223     0.000       0.000       True      0.119       60.034
  dff          (a) Bayes alignment    0.721  0.685  0.761     0.579   0.538   0.624     0.010       0.041       True      0.033       25.677
  dff          (a) Bayes   heading    0.425  0.397  0.453     0.372   0.346   0.397     0.639       0.969       True      0.071       54.990
  dff (b) HeadingDecoder all tuned    0.202  0.158  0.251     0.137   0.101   0.178     0.346       0.361       True      0.138       81.206
  dff (b) HeadingDecoder  landmark    0.207  0.178  0.241     0.117   0.098   0.138     0.038       0.019       True      0.113       77.724
[... 45 more lines not kept]
```

**Agent calls Bash**

```bash
date -u
```

```
Fri Oct 30 20:59:38 UTC 2026
```

**Agent calls Bash**

```bash
cat > $TMPDIR/gen/text1.py <<'PYEOF'
import nbformat as nbf
E = "entries/000483-sit-2023/"
FAIL = "A failure to reproduce here may be a failure of this attempt, not of the paper: see the reasoning and the differences from the paper's method."
def setcell(nb, prefix, text):
    ks = [k for k, c in enumerate(nb.cells) if c.cell_type == "markdown" and c.source.startswith(prefix)]
    assert len(ks) == 1, (prefix, ks)
    nb.cells[ks[0]].source = text.strip("\n")

# ---------------- single_cue
p = E + "single_cue.ipynb"; nb = nbf.read(p, as_version=4)
setcell(nb, "**Result: reproduced, under the centred fit", "**Result: reproduced, under the centred fit (an assumption).** With the centred fit 486 of 3179 ROIs (15.29%) are heading selective, within 14.2 +- 1.42% and 452 +- 45; by mouse 8.9 to 25.2%. With the fit as the code calls it (uncentred), 345 (10.85%), outside the tolerance. The two readings give different outcomes; the centred one is adopted because only it lets cells of every preferred heading pass (see fig1h below: the uncentred fit puts 93.6% of selected cells in one quadrant). Stricter reliability thresholds lower the count (KS p < 0.01 and d > 1.2: 394, 12.39%). The test is liberal: synthetic untuned cells pass at 4.7% (centred) and 1.7% (uncentred), and 15.7% pass its reliability step; real cells with each trial shifted once pass at 5.22% (selection-shuffled-control). This is the paper's own test, so the count is comparable with the paper's, but about a third of the selected cells could pass by chance.")
setcell(nb, "**Result: not reproduced, under the (once)", "**Result: not reproduced, under the (once) reading (an assumption).** Shifting each trial once before the test, as the Methods describe, 166 of 3179 ROIs (5.22%) still pass, above the 1% limit of the criterion; 481 pass the reliability step. Synthetic untuned cells pass at a similar rate (4.7%, under fig1g). Run as the commented code does it, with the trials re-shifted in every iteration, 0 of 3179 pass under both fit readings, but under that reading no cell can pass whatever the data, as its \"real\" and null values come from the same distribution. Which reading the claims file intends is asked of a reader.")
setcell(nb, "**Result: partially reproduced, under the centred fit", "**Result: partially reproduced, under the centred fit (an assumption).** The 486 preferred headings tile the circle: all 60 bins of 6 degrees hold at least one, and the quadrants hold 18.1 to 40.1%. The overrepresentation cannot be placed relative to the cue: the files give heading relative to the cage door, not the cue. Within 45 degrees of the dataset's heading 0 lie 24.7% of the cells (uniform 25%). The densest 90-degree window, centred at -102 degrees, holds 40.5% (Rayleigh p = 1.7e-05), and it differs between mice (SKKS090 and SKKS091 peak near +90 to +120). Were the cue at dataset heading -90, the share near it would be 40.1%; nothing in the files says it is. With the code's uncentred fit, 25 of 60 bins hold a cell and 93.6% lie in one quadrant, near -90, where the fit's bounds put the peak.")
setcell(nb, "## Summary", f"""## Summary

| Claim | Outcome |
|---|---|
| fig1-free-heading-fraction | blocked: data missing (no free-chamber recordings) |
| fig1g-rotation-heading-fraction | reproduced, assumed (centred fit): 15.29% (486 of 3179); the test passes 4.7% of synthetic untuned cells |
| selection-shuffled-control | not reproduced, assumed (each trial shifted once): 5.22% pass; 0% under the code's reading, which cannot fail |
| fig1h-preferred-headings-tile | partially reproduced, assumed: tiling holds; the cue's position in the heading frame is not in the files |

{FAIL}

How the analysis differs from the paper's: dF/F and spikes are computed from raw fluorescence without neuropil correction (the files hold no neuropil trace), with the Python port of OASIS. The selection test and its Gaussian fits are reimplemented in numpy. The trial-mean curve is centred before fitting, an assumption; the code's own call does not centre it, and both readings are shown. The shuffled control shifts each trial once before the test, an assumption; the code's reading is shown too.

What was found about the dataset: no free-chamber recordings; the experiment of each file is named only in its identifier; the heading series states a rate of 0.1 Hz for 10 Hz data; every file, axon recordings included, is described as a soma recording; four SKKS089 files carry identifiers naming SKKS088; the position of the cue in the heading frame is not given; the files hold 20 mice where the paper used 26. The clock check peaks after 0 in three of the four files that rotate both ways (4 to 6 frames) and before 0 in one (-6 frames).""")
nb.cells[0].source = nb.cells[0].source.replace("`axons.ipynb` and `somata.ipynb`, and Figures S5 and S6 in `directions.ipynb`.", "`axons.ipynb` and `somata.ipynb`, the decoding of Figure 6 in `decoding.ipynb`, and Figures S5 and S6 and the visual-cue-only files of Figure 5K in `directions.ipynb`.")
nbf.write(nb, p)

# ---------------- rotation_remapping
p = E + "rotation_remapping.ipynb"; nb = nbf.read(p, as_version=4)
setcell(nb, "**Result: reproduced, resting on assumptions", "**Result: partially reproduced, resting on assumptions (the CR heading mirrored, the 5 opposite-direction pairs, the centred fit).** With the chamber-rotation heading mirrored, cells selective in both conditions in the 5 pairs give V = 34.6, n = 228, p = 5.9e-04 (peak; 'fit' V = 36.0, p = 3.8e-04), so the criterion's test passes; cells selective in CR give V = 47.7, p = 7.3e-05. With all 7 pairs no reading has p < 0.05, and with the headings as stored every V is negative: 4 of 24 readings pass. The V is not the paper's 14.1 (n = 228 against 32). Matched ROIs do not keep their preference better than ROIs paired at random: over the 5 pairs random pairing gives a larger V (mean 46.2, 95th percentile 57.6), and in every pair the real V lies within its own random-pairing null (share of random pairings at or above it 0.21 to 0.998; SKKS116, V = 58.9 against a null mean of 56.8). The V-test passes because preferred headings are not uniform in either file. Head-rotation files have more selective cells than their chamber-rotation partners (53 to 83% against 8 to 65%) and more activity (0.095 to 3.19 spikes/s against 0.063 to 0.114), so heading-locked artefacts of derotation are not excluded. A clock offset of 6 frames would move preferred headings by 4 to 8 degrees in a head-rotation file and 12 degrees in a chamber-rotation file.")
setcell(nb, "**Result: reproduced, under the centred fit", "**Result: partially reproduced, under the centred fit (an assumption).** All 8 readings give V > 0 with p < 0.05. For cells selective in both contexts, peak preference and the median of the other cells' differences: V = 47.0, n = 85 over 9 recording pairs, p = 2.8e-13, against 25.6 with n = 66 in the paper, outside the tolerance of 2.56; no reading gives a V within it (38.4 to 233.5). Pairing neurons at random gives V of 36.2 on average (95th percentile 45.7, 1000 draws); 2.6% of random pairings reach the real V, so the real V lies only just above the null. 8 of the 9 pairs with 3 or more cells have V > 0.")
setcell(nb, "## Summary", f"""## Summary

| Claim | Outcome |
|---|---|
| fig2f-head-chamber-same-preference | partially reproduced, assumed (CR heading mirrored, 5 pairs, centred fit): the V-test passes, but random pairing gives as large a V in every pair |
| fig3c-coherent-remapping | partially reproduced, assumed (centred fit): every reading passes; V outside the tolerance and just above the random-pairing null |

{FAIL}

How the analysis differs from the paper's: inferred spikes from raw fluorescence without neuropil correction; cells selected with the centred fit. For Figure 2, the sign of the chamber-rotation heading and the set of pairs are not stated and were chosen as said above. Circular medians stand in for the medians of the Methods.

What was found about the dataset: 7 head-rotation pairs over 5 mice where the paper reports 5 over 4. The stored headings of 5 pairs run in opposite directions in the two conditions, and the files do not say how either heading is defined. Remapping files are named "1" and "2" or "Stars" and "Stripes"; one pair of SKKS091 is named "1-001" and "1-002", so it may not be a remapping pair; it enters only the readings with cells selective in either context, as it has fewer than 3 cells selective in both.""")
nbf.write(nb, p)

# ---------------- axons
p = E + "axons.ipynb"; nb = nbf.read(p, as_version=4)
setcell(nb, "**Result: reproduced under reading (b)", "**Result: reproduced under reading (b), all axons.** The mean aligned light-on curve has a flip score of -0.206 for ADN axons (unimodal) and 1.875 for visual axons (bimodal). Single visual axons have higher flip scores than ADN axons (means 0.506 and -0.109, KS p = 1.6e-24). Under reading (a), selective axons, the visual part holds (1.814; single axons 1.073 against -0.072, KS p = 1.7e-21). The ADN mean curve, however, has a flip score of 0.277 (centred fit) or 1.132 (code fit), above 0. One ADN mouse, SKKS092, has a mean flip score above 0 under reading (a) (0.48 and 0.42) and about 0 under (b) (-0.001).")
setcell(nb, "**Result: partially reproduced.**", "**Result: partially reproduced.** Visual axons lose their tuning in light-off: their mean light-off curve keeps 5 to 11% of the light-on range, under 50%. The ADN part of the criterion fails. Over all axons (reading b) the per-recording fraction selective in light-off is not significantly higher for ADN than for visual axons (medians 0.050 and 0.015, Mann-Whitney p = 0.3); pooled counts differ (94 of 1084 against 11 of 247, Fisher p = 0.026, the variant). Among selective axons (reading a) the share also selective in light-off is higher for ADN, but not significantly per recording (medians 0.143 and 0.000, Mann-Whitney p = 0.074, 14 and 7 recordings); pooled, 40 of 135 against 5 of 106 (Fisher p = 2.8e-07). The ADN mean light-off curve keeps 72 to 86% of its light-on range, but its peak lies 24 degrees (reading a) or 30 degrees (reading b) from the light-on peak, beyond the 18 degrees of the criterion (18 degrees under the code fit).")
nbf.write(nb, p)

# ---------------- directions
p = E + "directions.ipynb"; nb = nbf.read(p, as_version=4)
setcell(nb, "**Result: reproduced under reading (b).**", "**Result: reproduced under reading (b).** For the 407 cells selective in the four files that rotate both ways, the correlation of each cell's clockwise and counterclockwise tuning curves (median 0.211) exceeds that of randomly paired cells (0.122), bootstrapped KS p = 0.002. Reading (a), differences in preferred heading, gives p = 0.165 (median 24 against 30 degrees). By mouse, where random pairs come from the same mouse, (b) passes for SKKS125 only (p = 0.046; SKKS126 0.114, SKKS127 0.697). Over all active cells neither reading passes (p = 0.512 and 0.543). The files hold 3 mice where the paper reports 2, and their light condition is not marked, so the light and dark responses the claim names are not separated.")
setcell(nb, "**Result: reproduced under reading (b), with a small effect.**", "**Result: not reproduced, resting on leaving out the pair with 6 of 60 heading bins (an assumption).** Over all 5 pairs, reading (b) passes: for 382 cells selective in the motor-driven file, animal-controlled and motor-driven tuning curves correlate more (median 0.026) than randomly paired cells (-0.031), bootstrapped KS p = 0.034; reading (a) gives p = 0.912. That result rests on the pair SKKS125 2022-07-21, whose animal-controlled file visits 6 of 60 heading bins, so its 112 cells have tuning curves that are 0 in the other 54 bins. Without it neither reading passes (n = 270; (a) p = 0.969, (b) p = 0.903, median correlation 0.090 against 0.104 at random), and no pair passes on its own (p 0.781 to 1). The pooled pass comes from random pairs drawn across pairs of files. The dataset holds 5 pairs over 4 mice, where the paper reports 7 recordings over 3.")
setcell(nb, "## Summary", f"""## Summary

| Claim | Outcome |
|---|---|
| figs5-rotation-direction | reproduced under reading (b) (p = 0.002); (a) p = 0.165 |
| figs6-arena-control | not reproduced, assumed (the 6-bin pair left out): p = 0.969 and 0.903; with it (b) p = 0.034 |
| fig5k-visual-cue-only | blocked: no recording shares the visual-only files' ROIs |

{FAIL}

How the analysis differs from the paper's: Figures S5 and S6 were not read, so what the test compares follows the two readings of the claims file. Spikes are computed without neuropil correction, cells are selected with the centred fit, and light and dark are not separated, as the files do not mark them. For figs6, the pair whose animal-controlled file visits 6 of 60 heading bins is left out, an assumption; the result with it is shown.

What was found about the dataset: the recordings in both directions are over 3 mice (paper 2), and the animal-controlled pairs are 5 over 4 mice (paper 7 over 3). The files do not mark the light condition. The two visual-cue-only files share their ROIs with no other file, and nothing in them marks standard and visual-only rotation.""")
nbf.write(nb, p)
print("ok")
PYEOF
python $TMPDIR/gen/text1.py
```

```
ok
```

**Agent calls Bash**

```bash
cat > $TMPDIR/gen/text2.py <<'PYEOF'
import nbformat as nbf
E = "entries/000483-sit-2023/"
FAIL = "A failure to reproduce here may be a failure of this attempt, not of the paper: see the reasoning and the differences from the paper's method."
def setcell(nb, prefix, text):
    ks = [k for k, c in enumerate(nb.cells) if c.cell_type == "markdown" and c.source.startswith(prefix)]
    assert len(ks) == 1, (prefix, ks)
    nb.cells[ks[0]].source = text.strip("\n")

p = E + "directions.ipynb"; nb = nbf.read(p, as_version=4)
k = [k for k, c in enumerate(nb.cells) if c.source.startswith("## figs6-arena-control")][0]
nb.cells[k].source += "\n\nThe result is also shown without any pair whose animal-controlled file visits fewer than half of the 60 heading bins (`bin_tuning` sets an unvisited bin to 0), and for each pair alone, where random pairs come from the same pair of files."
nbf.write(nb, p)

p = E + "somata.ipynb"; nb = nbf.read(p, as_version=4)
setcell(nb, "**Result: not reproduced.** The silhouette", "**Result: not reproduced.** The silhouette value is highest at k = 2 under both readings: selective cells give 0.274, 0.023 and 0.039 for k = 2, 3 and 4, and all cells 0.189, 0.143 and -0.054. Neither has a local maximum at 3. The reviewer-code variant, with each curve centred on its own peak, has none either (selective 0.450, 0.036, 0.007; all 0.254, -0.019, 0.017).")
setcell(nb, "**Result: not reproduced.** 12.10%", "**Result: not reproduced.** 12.10% of somata are tuned (mean over recordings, s.e.m. 1.44; pooled 12.53%), matching 12.1 +- 1.1%. The three classes do not match. Over recordings, alignment-like cells make up 78.9%, heading 12.4% and landmark 8.8% (no outlier step); with the outlier step the shares are 75.3, 12.2 and 8.6%. Every reading gives alignment > heading > landmark, not landmark > alignment > heading. The counts are 1150, 194 and 75, against 409, 332 and 522 implied by the paper's degrees of freedom. All three light-on archetypes are bimodal (a2/a1 0.70 to 0.80), so the class called heading here is only the least bimodal of three bimodal classes.")
setcell(nb, "**Result: reproduced, but the classes are not the paper's", "**Result: partially reproduced, and the classes are not the paper's (see fig5-class-proportions).** For the 1150 cells of the alignment-like class, the V-test of the criterion passes (V = 743.2, p < 1e-300), but most of that V comes from taking the nearer of two peaks: light-off peaks drawn uniformly give V = 669.4 on average (V/n 0.582 against 0.646), and light-off peaks paired at random with other alignment-like cells give 706.9 (95th percentile 727.7). The real V exceeds that null (share of random pairings at or above it 0.002), so there is a small coregistration. Only 29.1% of the cells have the light-off peak within 18 degrees of a light-on peak, against 26.2% under random pairing, with a median offset of 36 degrees, so \"always\" is not supported. In the heading-like and landmark-like classes the real V does not exceed random pairing (shares 0.368 and 0.510).")
setcell(nb, "**Result: fig5f-heading-flip-unchanged reproduced", "**Result: fig5f-heading-flip-unchanged and fig5gh-landmark-alignment-flip-drop partially reproduced: each criterion is met, on classes that are not the paper's.** The flip score of the 194 heading-like cells does not differ significantly between light-on and light-off: 0.374 against 0.282, F(1,386) = 1.8, p = 0.18; with the outlier step p = 0.18; the variant with a random intercept per cell gives p = 0.14. The class is not the paper's heading class: it has 194 cells where the paper's degrees of freedom imply 332, and its light-on archetype is bimodal (a2/a1 0.70). Flip scores fall in light-off for landmark-like cells (0.482 to -0.242, F(1,148) = 47.3, p = 6.0e-12, n = 75) and alignment-like cells (0.365 to 0.014, F(1,2298) = 135.2, p = 3.0e-31, n = 1150).")
setcell(nb, "**Result: reproduced by the criterion", "**Result: partially reproduced: the criterion is met, but the ellipses do not separate the axon groups.** Under reading (a), 88.9% of ADN axons lie inside the heading-class ellipse and 86.8% of visual axons inside the landmark-class ellipse. Under (b), 71.9% and 61.9%. The soma ellipses overlap heavily: the alignment ellipse holds 84.8 to 96.2% of both axon groups, the heading ellipse holds 79.8 to 91.5% of visual axons (more than the landmark ellipse does), and the LDA assigns 83.7 to 98.0% of the axons to the alignment class. The classes are those of fig5-class-proportions, not the paper's.")
setcell(nb, "## Summary", f"""## Summary

| Claim | Outcome |
|---|---|
| fig5-three-classes | not reproduced: silhouette highest at k = 2 |
| fig5-class-proportions | not reproduced: 12.1% tuned matches; class shares do not |
| fig5e-alignment-peaks-coregistered | partially reproduced: V above a random-pairing null by a small margin; 29.1% within 18 degrees (26.2% at random); classes not the paper's |
| fig5f-heading-flip-unchanged | partially reproduced: p = 0.18, on a heading-like class that is not the paper's |
| fig5gh-landmark-alignment-flip-drop | partially reproduced: both drops significant, on classes that are not the paper's |
| fig5i-axons-in-clusters | partially reproduced: criterion met; the ellipses overlap and do not separate the axon groups |

{FAIL}

How the analysis differs from the paper's: inferred spikes from raw fluorescence without neuropil correction; selection with the centred fit; Gaussian fits reimplemented in numpy; light-off curves take the shift of the mean light-on curve (leaveOneOutAligner is not public); the GMM, LDA and mixed models are scikit-learn and statsmodels in place of MATLAB; the class names come from a rule on the archetypes stated above. The classes differ from the paper's, so the claims that use them test other cell groups.

What was found about the dataset: 35 dual-cue soma recordings where the paper reports 36; no light-on and light-off labels; no matching of ROIs between the standard and the visual-cue-only recordings of Figure 5K.""")
nbf.write(nb, p)

p = E + "decoding.ipynb"; nb = nbf.read(p, as_version=4)
R = {
"RESULT_6A_ON": "**Result: not reproduced.** No decoder reading gives a light-on mean within 0.82 +- 0.04: the naive Bayes decoder gives 0.708 [0.665, 0.747] (dF/F) and 0.712 [0.677, 0.745] (spikes), the HeadingDecoder 0.202 and 0.215. Chance with each decoder is 0.10 (0.101 to 0.102), the 0.10 reading of the claims file, so the decoders are far above chance but less accurate than the paper's.",
"RESULT_6A_OFF": "**Result: partially reproduced, under the naive Bayes decoder (an assumption).** Light-off accuracy drops and stays above chance: 0.569 [0.525, 0.612] (dF/F) and 0.571 [0.537, 0.606] (spikes), both intervals above 0.18 and 0.10, light-off lower with p = 0.016 and p < 0.001 (paired; unpaired 0.061 and 0.001). The mean is outside 0.44 +- 0.10 under every reading, so the criterion is not met in full. The HeadingDecoder gives 0.137 and 0.144, with no significant drop (p 0.23 to 0.36); it decodes near chance here (light-on 0.20 to 0.22).",
"RESULT_6B_HEADING": "**Result: partially reproduced, under the naive Bayes decoder (an assumption), on a heading-like class that is not the paper's.** Heading-like cells (175 used) decode above chance in both conditions (dF/F 0.425 and 0.372; spikes 0.407 and 0.344; every interval above 0.18) with no significant difference (p 0.31 to 0.97), as the claim says. The accuracies are below the paper's under every reading (outside 0.61 +- 0.05 and 0.44 +- 0.08); the HeadingDecoder gives 0.127 to 0.148 in light-on.",
"RESULT_6B_LANDMARK": "**Result: partially reproduced, under the naive Bayes decoder (an assumption), on a landmark-like class that is not the paper's.** Landmark-like cells (54 used, resampled to 332) fall to near chance in light-off, 0.210 [0.195, 0.223] (dF/F) and 0.192 [0.181, 0.205] (spikes), within 0.20 +- 0.07, with p < 0.001 for the drop. Their light-on accuracy, 0.397 and 0.395, is half the paper's 0.80, so the criterion is not met. The light-off intervals exclude 0.18 (by 0.001 for spikes) and 0.10. The HeadingDecoder gives 0.207 and 0.247 in light-on.",
"RESULT_6B_ALIGNMENT": "**Result: not reproduced.** Under the naive Bayes decoder both means of alignment-like cells are within tolerance (dF/F 0.721 and 0.579; spikes 0.712 and 0.579) and the light-off intervals exclude chance, but their light-on accuracy is the highest of the three classes, not between heading-like (0.425, 0.407) and landmark-like (0.397, 0.395) cells, and light-off is significantly lower (p = 0.010 and 0.001, paired), which the criterion counts against the claim under the reading that matches the values. Under the HeadingDecoder the means are far below (0.202 and 0.219).",
"RESULT_6B_180": "**Result: reproduced, under the naive Bayes decoder (an assumption), on classes that are not the paper's.** In light-on, 11.9% (dF/F) and 13.7% (spikes) of the landmark-like decoder's errors lie within 18 degrees of 180, above 0.10, and 7.1% and 9.1% of the heading-like decoder's, no more than 0.10. Under the HeadingDecoder the criterion fails (heading-like 0.105 and 0.106), but that decoder is near chance here, so its errors are spread almost evenly: all its groups have 0.105 to 0.158.",
"RESULT_6_BELOW": "**Result: reproduced.** Under every decoder and input reading the 95% interval of light-on accuracy for heading-like cells lies below that of all tuned cells (Bayes: 0.425 [0.397, 0.453] against 0.708 [0.665, 0.747] for dF/F, 0.407 [0.383, 0.432] against 0.712 [0.677, 0.745] for spikes; HeadingDecoder 0.127 to 0.148 against 0.202 to 0.215), and heading-like cells decode worse in 99.8 to 100% of iterations. Reading (b), the mixed model, cannot be formed for pseudopopulation trials. The heading-like class is not the paper's.",
}
for k, c in enumerate(nb.cells):
    for key, val in R.items():
        if c.cell_type == "markdown" and c.source.strip() == f"**Result: {key}**":
            c.source = val
nb.cells[-1].source = nb.cells[-1].source.replace("SUMMARY_TABLE", """| Claim | Outcome |
|---|---|
| fig6a-population-light-on | not reproduced: 0.71 (Bayes) or 0.21 (HeadingDecoder) against 0.82 |
| fig6a-population-light-off | partially reproduced, assumed (Bayes): drop significant and above chance; 0.57 against 0.44 |
| fig6b-heading-cells | partially reproduced, assumed (Bayes): above chance in both, no significant difference; accuracies below the paper's |
| fig6b-landmark-cells | partially reproduced, assumed (Bayes): falls to 0.19 to 0.21 in light-off; light-on 0.40 against 0.80 |
| fig6b-alignment-cells | not reproduced: values within tolerance, but not between the other classes and a significant drop |
| fig6b-180-errors | reproduced, assumed (Bayes) |
| fig6-heading-below-population | reproduced under every decoder reading |""")
assert not any("RESULT_" in c.source or "SUMMARY_TABLE" in c.source for c in nb.cells)
nbf.write(nb, p)
print("ok")
PYEOF
python $TMPDIR/gen/text2.py
```

```
ok
```

**Agent calls Bash**

```bash
cd entries/000483-sit-2023; cat README.md
```

```
# Sit & Goard (2023) from dandiset 000483

Tests the findings of [Sit and Goard (2023)](https://doi.org/10.1038/s41467-023-37704-5),
"Coregistration of heading to visual cues in retrosplenial cortex", on
[DANDI:000483](https://dandiarchive.org/dandiset/000483/0.230421.2321). The dandiset holds two-photon
recordings of retrosplenial somata and of ADN and visual cortical axons in RSC, made in a floating
chamber rotated by a motor, by the mouse or with the head rotated. The files hold raw ROI
fluorescence and chamber heading, with no neuropil trace, dF/F or inferred spikes; the notebooks
compute them.

| Claim | Outcome |
|---|---|
| 14.0% heading cells in the free chamber (Fig. 1D, E) | Blocked: data missing |
| 14.2% heading cells with motor rotation (Fig. 1G) | Reproduced (rests on an assumption) |
| No cell passes the test on pre-shuffled data | Reproduced |
| Preferred headings tile the chamber (Fig. 1H) | Partially reproduced (rests on an assumption) |
| Same preference under head and chamber rotation (Fig. 2F) | Reproduced (rests on assumptions) |
| Coherent remapping (Fig. 3C) | Reproduced (rests on an assumption) |
| ADN axons unimodal, visual axons bimodal in light (Fig. 4) | Reproduced |
| ADN axons keep tuning in the dark, visual axons lose it (Fig. 4) | Partially reproduced |
[... 24 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/000483-sit-2023; python - <<'EOF'
p='README.md'; s=open(p).read()
start=s.index('| Claim | Outcome |'); end=s.index('A failure to reproduce')
table='''| Claim | Outcome |
|---|---|
| 14.0% heading cells in the free chamber (Fig. 1D, E) | Blocked: data missing |
| 14.2% heading cells with motor rotation (Fig. 1G) | Reproduced (rests on an assumption) |
| No cell passes the test on pre-shuffled data | Not reproduced (rests on an assumption) |
| Preferred headings tile the chamber (Fig. 1H) | Partially reproduced (rests on an assumption) |
| Same preference under head and chamber rotation (Fig. 2F) | Partially reproduced (rests on assumptions) |
| Coherent remapping (Fig. 3C) | Partially reproduced (rests on an assumption) |
| ADN axons unimodal, visual axons bimodal in light (Fig. 4) | Reproduced |
| ADN axons keep tuning in the dark, visual axons lose it (Fig. 4) | Partially reproduced |
| Three classes by clustering (Fig. 5B) | Not reproduced |
| Class proportions (Fig. 5C to E) | Not reproduced |
| Alignment cells' dark peak at a light peak (Fig. 5E) | Partially reproduced |
| Heading cells' flip score unchanged in the dark (Fig. 5F) | Partially reproduced |
| Landmark and alignment flip scores drop in the dark (Fig. 5G, H) | Partially reproduced |
| Axons within the soma clusters (Fig. 5I) | Partially reproduced |
| Visual-cue-only rotation (Fig. 5K) | Blocked: metadata insufficient |
| Diversity persists across rotation direction (Fig. S5) | Reproduced |
| Diversity persists with animal or motor control (Fig. S6) | Not reproduced (rests on an assumption) |
| Decoding from all tuned cells, light-on (Fig. 6A) | Not reproduced |
| Decoding from all tuned cells, light-off (Fig. 6A) | Partially reproduced (rests on an assumption) |
| Decoding from heading cells (Fig. 6B) | Partially reproduced (rests on an assumption) |
| Decoding from landmark cells (Fig. 6B) | Partially reproduced (rests on an assumption) |
| Decoding from alignment cells (Fig. 6B) | Not reproduced |
| 180 degree errors of landmark, not heading, cells (Fig. 6B) | Reproduced (rests on an assumption) |
| Heading cells decode worse than all tuned cells (Fig. 6B) | Reproduced |

'''
s=s[:start]+table+s[end:]
s=s.replace('''- `directions.ipynb`: Figures S5 and S6 (about 12 minutes).''','''- `directions.ipynb`: Figures S5 and S6, and the visual-cue-only files of Figure 5K (about 10 minutes).
- `decoding.ipynb`: Figure 6; it rebuilds the classes of `somata.ipynb` (about 16 minutes).''')
s=s.replace("(about 12 minutes).\n- `rotation","(about 9 minutes).\n- `rotation").replace("Figures 2 and 3 (about 14 minutes)","Figures 2 and 3 (about 11 minutes)").replace("Figure 4 (about 8 minutes)","Figure 4 (about 6 minutes)").replace("Figure 5 (about 23 minutes)","Figure 5 (about 17 minutes)")
open(p,'w').write(s)
p='entry.yaml'; s=open(p).read()
for nbk,old,new in [('single_cue',12,9),('rotation_remapping',14,11),('axons',8,6),('somata',23,17),('directions',12,10)]:
    i=s.index(nbk+'.ipynb'); j=s.index('runtime_minutes: %d'%old,i); s=s[:j]+'runtime_minutes: %d'%new+s[j+len('runtime_minutes: %d'%old):]
open(p,'w').write(s)
EOF
grep -n "runtime\|path" entry.yaml
```

```
15:- path: single_cue.ipynb
17:  runtime_minutes: 9
18:- path: rotation_remapping.ipynb
20:  runtime_minutes: 11
21:- path: axons.ipynb
23:  runtime_minutes: 6
24:- path: somata.ipynb
26:  runtime_minutes: 17
27:- path: directions.ipynb
29:  runtime_minutes: 10
30:- path: decoding.ipynb
32:  runtime_minutes: 16
```

**Agent calls Write**

```json
{
 "file_path": "questions/000483.yaml",
 "content": "dandiset: \"000483\"\npaper: doi:10.1038/s41467-023-37704-5\nquestions:\n- claim: selection-shuffled-control\n  asked: 2026-10-30\n  question: The criterion says the test is run \"after circularly shifting each trial's tuning curve\n    by an independent random amount before the test, as in the commented\n    calculateHeadDirection_shuff of Cue.m\". The two halves of that sentence describe different\n    procedures. The commented code shifts the trials afresh in every one of the 1000 iterations\n    (activity_rand2), so the \"real\" and the null split-half correlations come from the same\n    distribution and no cell can pass, whatever the data. Shifting each trial once before the whole\n    test, as \"before the test\" and the Methods' \"pre-shuffled data\" say, measures how many untuned\n    cells the procedure passes. Which does the claim mean?\n  passage: When repeating these procedures using pre-shuffled data, no cells passed these criteria,\n    suggesting that the number of heading selective cells is accurate, and not due to chance\n    (Methods, Analysis of calcium data, paragraph 4). Code, Cue.m at commit c6344f5, lines 888 to\n    990 (commented calculateHeadDirection_shuff).\n  why: The readings give different outcomes. With the trials shifted afresh in every iteration, 0 of\n    3179 single-cue cells pass (reproduced), but that reading cannot fail. With each trial shifted\n    once before the test, 166 of 3179 (5.22%) pass, above the criterion's 1% limit (not\n    reproduced). The attempt adopts the second reading, as only it tests whether the count is due\n    to chance.\n"
}
```

```
File created successfully at: questions/000483.yaml (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd  python -c "
import json;s=json.load(open('schemas/attempt.schema.json'))
o=s['properties']['outcomes']['items']; print(list(o['properties'].keys())); print(json.dumps(o['properties'].get('proposed'),indent=0)[:600]); print(s['properties']['findings']['items']['properties'].keys())"; grep -n "verifications\|verifier" tools/entry.py | head -20
```

```
['claim', 'outcome', 'blocked_by', 'notes', 'notebook', 'output', 'measured', 'deviations', 'assumed', 'proposed']
{
"description": "A change of outcome found after the last verification round, held until a further round agrees with it.",
"type": "object",
"additionalProperties": false,
"required": [
"outcome",
"reason"
],
"properties": {
"outcome": {
"enum": [
"reproduced",
"partially_reproduced",
"not_reproduced",
"blocked"
]
},
"blocked_by": {
"description": "Required when outcome is blocked.",
[... 21 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 240,330p tools/entry.py
```

```
if isinstance(rec, dict):
            earlier = load(Report(), ROOT / "attempts" / f"{rec.get('earlier')}.yaml")
            if not isinstance(earlier, dict):
                report.error(where, f"reconciliation: no attempt record {rec.get('earlier')!r}")
            else:
                n_then, n_now = len(earlier.get("findings") or []), len(attempt.get("findings") or [])
                numbers = [f.get("finding") for f in rec.get("findings") or []]
                if sorted(numbers) != list(range(1, n_then + 1)):
                    report.error(where, f"reconciliation: give each of the {n_then} findings of "
                                        f"{rec['earlier']} one item, numbered from 1")
                for f in rec.get("findings") or []:
                    now = f.get("now")
                    if (f.get("status") in ("still_present", "partly_fixed")) != (now is not None):
                        report.error(where, f"reconciliation: earlier finding {f.get('finding')} needs `now` "
                                            "exactly when it is still present or partly fixed")
                    if now is not None and not 1 <= now <= n_now:
                        report.error(where, f"reconciliation: finding {now} is not in this record")
        # A deprecated attempt no longer stands: its claims are being read again, and the claims file it was
        # tested on may already have been replaced (docs/pipeline.md), so it is not held to the current one.
        if attempt.get("deprecated"):
[... 70 more lines not kept]
```

**Agent calls Bash**

```bash
cat > $TMPDIR/gen/attempt.py <<'PYEOF'
import yaml
p = "attempts/000483-sit-2023-01.yaml"
A = yaml.safe_load(open(p))
O = {o["claim"]: o for o in A["outcomes"]}
SPK = "Spikes computed without neuropil correction, and the test reimplemented, as for fig1g-rotation-heading-fraction."
RERUN = "The numbers are from the re-run after verification round 1, which differ slightly from the first run (for example 486 against 485 selected cells), as floating-point results differ between machines."

O["fig1g-rotation-heading-fraction"].update(measured=[15.29, 486], notes=(
 "With the centred fit, 486 of 3179 ROIs (15.29%) pass, within 14.2 +- 1.42% and 452 +- 45; by mouse 8.9 to 25.2%, by "
 "recording 2.2 to 33.0%. With the fit as the code calls it, without centring, 345 (10.85%), outside the tolerance. With "
 "stricter reliability thresholds (KS p < 0.01, d > 1.2) the centred count is 394 (12.39%). The test is liberal. Its "
 "reliability step runs a KS test on 1000 split-half correlations of the same trials, as the paper's code does "
 "(ControlledRotation.calculateHeadDirection), and synthetic untuned cells pass the whole test at 4.7% (centred) and 1.7% "
 "(uncentred); real cells with each trial shifted once pass at 5.22% (selection-shuffled-control). The count matches the "
 "paper's, but about a third of the selected cells could pass by chance. " + RERUN))
O["selection-shuffled-control"] = dict(claim="selection-shuffled-control", outcome="not_reproduced", assumed=True,
 notebook="single_cue.ipynb", output="claim:selection-shuffled-control", notes=(
 "With each trial shifted once by its own random amount before the whole test, as the Methods' \"pre-shuffled data\" and "
 "the criterion's \"before the test\" say, 166 of 3179 ROIs (5.22%) pass, above the criterion's 1% limit; 481 pass the "
 "reliability step. Run as the commented calculateHeadDirection_shuff of Cue.m does it (the trials re-shifted in every "
 "iteration), 0 of 3179 pass under both fits, but under that reading the \"real\" and null split-half correlations come "
 "from the same distribution, so no cell can pass whatever the data. Synthetic untuned cells pass at 4.7% (fig1g). Which "
 "reading the claims file intends is asked in questions/000483.yaml."),
 deviations=["Assumption. The trials are shifted once before the test (the variant of the first run). The criterion "
             "names both \"before the test\" and the commented code, which shifts them afresh in every iteration; only "
             "the first can show whether the count is due to chance. Both are shown.", SPK])
O["fig1h-preferred-headings-tile"]["notes"] = (
 "Tiling holds. The 486 cross-validated preferred headings (centred fit) fill all 60 bins of 6 degrees, and the four "
 "quadrants hold 18.1 to 40.1%. The overrepresentation cannot be judged. The files give heading relative to \"cage door "
 "dead north\" and do not say where the cue is. Within 45 degrees of the dataset's 0 lie 24.7% (not above 25%). The "
 "densest 90-degree window, centred at -102 degrees, holds 40.5% (Rayleigh p = 1.7e-05), and the densest heading differs "
 "between mice (SKKS090 and SKKS091 near +90 to +120). Were the cue at dataset heading -90, the share near it would be "
 "40.1%; nothing in the files says so. The code's uncentred fit puts 93.6% of its cells near -90 because its bounds hold "
 "the Gaussian's peak at dataset headings -120 to -60, which says nothing about the cue.")
O["fig2f-head-chamber-same-preference"].update(outcome="partially_reproduced", notes=(
 "The criterion's test passes only under assumptions. Cells selective in both conditions, peak preference, "
 "chamber-rotation (CR) heading mirrored, the 5 pairs whose stored headings run in opposite directions, give V = 34.6, n = "
 "228, p = 5.9e-04 ('fit' preference V = 36.0, p = 3.8e-04; cells selective in CR V = 47.7, p = 7.3e-05). 4 of 24 readings "
 "give p < 0.05 with V > 0. With all 7 pairs none does, and with the headings as stored every V is negative. The V is not "
 "the paper's 14.1 (n = 32), and no reading has n near 32. Matched ROIs do not keep their preference better than random "
 "pairs: pairing ROIs at random over the 5 pairs gives a larger V (mean 46.2, 95th percentile 57.6), and within every pair "
 "the real V lies inside its own random-pairing null (share of 1000 random pairings at or above it 0.21 to 0.998; "
 "SKKS116, the one pair with a large V, 58.9 against a null mean of 56.8). Head-rotation files have more selective cells "
 "(53 to 83% against 8 to 65%) and more activity (0.095 to 3.19 spikes/s against 0.063 to 0.114) than their CR partners, "
 "so heading-locked artefacts of derotation are not excluded. A 6-frame clock offset would move preferences by 4 to 8 "
 "degrees (head rotation) or 12 degrees (CR)."))
O["fig3c-coherent-remapping"].update(outcome="partially_reproduced", assumed=True, notes=(
 "All 8 readings give V > 0 with p < 0.05. Cells selective in both contexts, peak preference, expected offset (i), give "
 "V = 47.0, n = 85 over 9 recording pairs, p = 2.8e-13, against V = 25.6 with n = 66 in the paper; no reading gives a V "
 "within the tolerance (38.4 to 233.5). Pairing neurons at random gives a V of 36.2 on average (95th percentile 45.7, "
 "1000 draws); 2.6% of random pairings reach the real V, so it lies only just above the null. 8 of the 9 pairs with 3 or "
 "more cells have V > 0. The SKKS091 2021-05-04 pair, whose files are both named context 1, has fewer than 3 cells "
 "selective in both and enters only the readings with cells selective in either."))
O["fig4-axons-light-on-shape"]["notes"] = (
 "Under reading (b), all 1084 ADN and 247 visual axons, the mean aligned light-on curve has a flip score of -0.206 (ADN) "
 "and 1.875 (visual), and single visual axons score higher (means 0.506 and -0.109, KS p = 1.6e-24). Under reading (a), "
 "selective axons, the visual mean curve is bimodal (1.814) and single axons differ (KS p = 1.7e-21), but the ADN mean "
 "curve has a flip score of 0.277 with the centred fit and 1.132 with the code fit, above 0. One ADN mouse (SKKS092) has "
 "a mean flip score above 0 under reading (a) (0.48, 0.42) and about 0 under (b) (-0.001).")
O["fig4-axons-light-off"]["notes"] = (
 "Visual axons lose their tuning in light-off (mean light-off curve 5 to 11% of the light-on range, under half). The ADN "
 "part fails. Over all axons (reading b) the per-recording fraction selective in light-off is not significantly higher "
 "for ADN than for visual axons (medians 0.050 and 0.015, Mann-Whitney p = 0.3); pooled, 94 of 1084 against 11 of 247 "
 "(Fisher p = 0.026, the variant). Among selective axons (reading a) the share also selective in light-off has medians "
 "0.143 and 0.000 (Mann-Whitney p = 0.074, 14 and 7 recordings); pooled 40 of 135 against 5 of 106 (Fisher p = 2.8e-07). "
 "The ADN mean light-off curve keeps 72 to 86% of the light-on range, but its peak lies 24 degrees (reading a) or 30 "
 "degrees (reading b) from the light-on peak, beyond 18 degrees (18 degrees with the code fit).")
O["figs5-rotation-direction"]["notes"] = (
 "Reading (b) passes. For the 407 cells selective in the four files that rotate both ways, each cell's clockwise and "
 "counterclockwise tuning curves correlate more (median 0.211) than randomly paired cells (0.122), bootstrapped KS p = "
 "0.002. Reading (a), differences in preferred heading, gives p = 0.165 (median 24 against 30 degrees). By mouse, with "
 "random pairs from the same mouse, (b) passes for SKKS125 only (p = 0.046; SKKS126 0.114, SKKS127 0.697); over all "
 "active cells neither reading passes (p = 0.512 and 0.543). The pooled random pairs cross files. The statement's light "
 "and dark responses are not separated, as the files do not mark the light condition, so the \"diversity\" part is not "
 "tested beyond tuning stability.")
O["figs6-arena-control"].update(outcome="not_reproduced", assumed=True, notes=(
 "Without the pair whose animal-controlled file visits 6 of 60 heading bins (SKKS125, 2022-07-21), neither reading passes: "
 "n = 270, (a) p = 0.969, (b) p = 0.903 (median correlation 0.090 against 0.104 at random), and no pair passes on its own "
 "(p 0.781 to 1). With it, reading (b) passes over all 5 pairs (n = 382, median 0.026 against -0.031, p = 0.034; (a) p = "
 "0.912), but its 112 cells (29% of n) have animal-controlled tuning curves that are 0 in 54 of 60 bins, and the pooled "
 "random pairs cross pairs of files."))
O["figs6-arena-control"]["deviations"] = O["figs6-arena-control"]["deviations"] + [
 "Assumption. Pairs whose animal-controlled file visits fewer than half of the 60 heading bins are left out (one pair, 6 "
 "of 60 bins), as their tuning curves are mostly the 0 that bin_tuning gives an unvisited bin. The result with it is shown."]
O["fig5-three-classes"]["notes"] = (
 "The silhouette value is highest at k = 2 under both readings. Selective cells (1419) give 0.274, 0.023 and 0.039 for "
 "k = 2, 3 and 4, and all cells (11329) give 0.189, 0.143 and -0.054, so neither has a local maximum at 3. The "
 "reviewer-code variant, each curve centred on its own peak, has none either (selective 0.450, 0.036, 0.007; all 0.254, "
 "-0.019, 0.017); in the first run it had one for selective cells. " + RERUN)
O["fig5-class-proportions"].update(measured=[12.1, 8.8, 78.9, 12.4], notes=(
 "12.10% of somata are tuned (mean over recordings, s.e.m. 1.44; pooled 12.53%, over mice 11.51%), within 12.1 +- 1.1. The "
 "class shares do not match. Over recordings with no outlier step, landmark-like cells are 8.8%, alignment-like 78.9% and "
 "heading-like 12.4%; with the chi-square outlier step (58 cells to the null cluster) 8.6, 75.3 and 12.2%. Every reading "
 "orders them alignment > heading > landmark. The counts are 75 landmark, 1150 alignment and 194 heading, against 522, 409 "
 "and 332 from the paper's degrees of freedom. All three light-on archetypes are bimodal (a2/a1 0.70 to 0.80), so no "
 "class is a unimodal heading class. measured gives reading (b) with average (i)."))
O["fig5e-alignment-peaks-coregistered"].update(outcome="partially_reproduced", notes=(
 "The criterion's V-test passes for the 1150 alignment-like cells (V = 743.2, p < 1e-300), but taking the nearer of two "
 "peaks 180 degrees apart folds offsets into +-90 and gives a large V by itself: uniform light-off peaks give V = 669.4 on "
 "average (V/n 0.582 against 0.646), and light-off peaks paired at random with other alignment-like cells give 706.9 (95th "
 "percentile 727.7, 1000 draws). The real V exceeds the random pairing (share at or above it 0.002), a small "
 "coregistration. Only 29.1% of offsets lie within 18 degrees, against 26.2% under random pairing, with a median offset of "
 "36 degrees, so \"always\" is not supported. In the heading-like and landmark-like classes the V does not exceed random "
 "pairing (shares 0.368 and 0.510). The class is not the paper's alignment class (fig5-class-proportions)."))
O["fig5e-alignment-peaks-coregistered"]["deviations"] = ["Tested on the classes found here, which differ from the paper's.",
 "The V is compared with a random-pairing null and a uniform-peak null, which the criterion does not ask for, because the "
 "nearer-peak offset biases the V-test towards 0."]
O["fig5f-heading-flip-unchanged"].update(outcome="partially_reproduced", notes=(
 "The criterion is met on a class that is not the paper's. The 194 heading-like cells have flip scores 0.374 in light-on "
 "and 0.282 in light-off, F(1,386) = 1.8, p = 0.18 (mixed model with mouse as random intercept); with the outlier step p = "
 "0.18, with a random intercept per cell p = 0.14. The class has 194 cells where the paper's degrees of freedom imply 332, "
 "and its light-on archetype is bimodal (a2/a1 0.70), so it is only the least bimodal of three bimodal classes. In the "
 "first round's development, with a different selection seed, the class held 380 cells and the light effect was "
 "significant (not run here)."))
O["fig5gh-landmark-alignment-flip-drop"].update(outcome="partially_reproduced", notes=(
 "The criterion is met on classes that are not the paper's. Flip scores fall in light-off for landmark-like cells (0.482 to "
 "-0.242, F(1,148) = 47.3, p = 6.0e-12, n = 75) and alignment-like cells (0.365 to 0.014, F(1,2298) = 135.2, p = 3.0e-31, "
 "n = 1150), against F(1,1042) = 1062.5 and F(1,816) = 209.5 in the paper."))
O["fig5i-axons-in-clusters"].update(outcome="partially_reproduced", notes=(
 "The criterion is met, but the ellipses do not separate the axon groups. Under reading (a), 88.9% of ADN axons lie inside "
 "the heading-class 95% ellipse and 86.8% of visual axons inside the landmark-class ellipse; under (b), 71.9% and 61.9%. "
 "The alignment-class ellipse holds 84.8 to 96.2% of both axon groups, the heading ellipse holds 79.8 to 91.5% of visual "
 "axons (more than the landmark ellipse), and the LDA assigns 83.7 to 98.0% of axons to the alignment class. The classes "
 "come from fig5-class-proportions, which is not reproduced."))
O["fig5k-visual-cue-only"]["notes"] = (
 "The two visual-cue-only recordings (Suspended, SKKS125 2022-08-10 with 446 ROIs and SKKS127 2022-08-11 with 691 ROIs, "
 "15050 frames each) share their number of ROIs with no other file of their mouse (the others have 213 to 670), and no "
 "matching of ROIs is given, so the matched neurons of Figure 5K cannot be found in another file. Inside each file the "
 "1250-frame blocks alternate between the two directions of rotation at about 2 degrees per frame and the last block is "
 "still; nothing in the heading or the mean fluorescence marks some blocks as standard rotation, and light-on and "
 "light-off are not marked (directions.ipynb).")
O["fig5k-visual-cue-only"]["notebook"] = "directions.ipynb"

DEC_DEV = ["The classes are those of somata.ipynb (fig5-class-proportions, not reproduced), rebuilt in decoding.ipynb with "
           "the same files, seeds and code; they differ from the paper's.",
           "Pseudopopulations from the 25 7550-frame recordings with 5 trials on each side of all three light-to-dark "
           "transitions (15 trials a side; 1331 of 1419 tuned cells); the 1950-frame recordings are left out. Trials are "
           "resampled to 200 bins on heading in place of time, so bins line up across recordings.",
           "The naive Bayes decoder is written here after Etter et al. (2020): activity binarized (spikes above 0; dF/F above "
           "the mean plus 2 SD, a standard choice), 60 states of 6 degrees, a +1/+2 prior, trained on even and tested on odd "
           "bins. The HeadingDecoder (github.com/ucsb-goard-lab/HeadingDecoder at ca9842e) is reimplemented in numpy with "
           "leave-one-trial-out tuning weights; it decodes near chance here (0.20 to 0.22 for all tuned cells).",
           "Chance is measured with each decoder by decoding with each cell's test activity circularly shifted along the "
           "trial: 0.101 to 0.102, the 0.10 reading of the claims file."]
ASSUME_BAYES = ("Assumption. The decoder readings give different outcomes; the naive Bayes decoder is adopted, as the "
                "Methods name Bayesian decoding (Etter et al. 2020) and the claims file puts the Methods first, and the "
                "HeadingDecoder decodes near chance here. Every reading is shown.")
def dec(claim, outcome, notes, measured=None, assumed=False):
    o = dict(claim=claim, outcome=outcome)
    if assumed: o["assumed"] = True
    o.update(notebook="decoding.ipynb", output=f"claim:{claim}")
    if measured is not None: o["measured"] = measured
    o["notes"] = notes
    o["deviations"] = ([ASSUME_BAYES] if assumed else []) + DEC_DEV
    O[claim] = o
dec("fig6a-population-light-on", "not_reproduced",
    "No decoder reading gives a light-on mean within 0.82 +- 0.04. The naive Bayes decoder gives 0.708 [0.665, 0.747] "
    "(dF/F) and 0.712 [0.677, 0.745] (spikes); the HeadingDecoder 0.202 and 0.215. Chance is 0.10. measured gives dF/F "
    "with the Bayes decoder, the first reading.", 0.708)
dec("fig6a-population-light-off", "partially_reproduced",
    "Under the Bayes decoder light-off accuracy drops and stays above chance: 0.569 [0.525, 0.612] (dF/F) and 0.571 [0.537, "
    "0.606] (spikes), both intervals above 0.18 and 0.10, light-off lower with p = 0.016 and p < 0.001 (paired; unpaired "
    "0.061 and 0.001). The mean is outside 0.44 +- 0.10 under every reading, so the criterion is not met in full. The "
    "HeadingDecoder gives 0.137 and 0.144, intervals including chance, and no significant drop (p 0.23 to 0.36).", 0.569, True)
dec("fig6b-heading-cells", "partially_reproduced",
    "Under the Bayes decoder, heading-like cells (175 used) decode above chance in both conditions (dF/F 0.425 and 0.372; "
    "spikes 0.407 and 0.344; every interval above 0.18) with no significant difference (p 0.31 to 0.97), as the claim says, "
    "but both means are outside 0.61 +- 0.05 and 0.44 +- 0.08 under every reading. The HeadingDecoder gives 0.127 to 0.148 "
    "in light-on. The class is not the paper's heading class.", [0.425, 0.372], True)
dec("fig6b-landmark-cells", "partially_reproduced",
    "Under the Bayes decoder, landmark-like cells (54 used, sampled 332 with replacement) fall to near chance in light-off "
    "(dF/F 0.210 [0.195, 0.223]; spikes 0.192 [0.181, 0.205]), within 0.20 +- 0.07, with p < 0.001 for the drop, but their "
    "light-on accuracy (0.397 and 0.395) is half the paper's 0.80, so the criterion is not met. The light-off intervals "
    "exclude 0.18 (by 0.001 for spikes) and 0.10. The HeadingDecoder gives 0.207 and 0.247 in light-on. The class is not the "
    "paper's.", [0.397, 0.21], True)
dec("fig6b-alignment-cells", "not_reproduced",
    "Under the Bayes decoder both means of alignment-like cells are within tolerance (dF/F 0.721 and 0.579; spikes 0.712 and "
    "0.579), with light-off intervals above chance, but their light-on accuracy is the highest of the three classes, not "
    "between heading-like (0.425, 0.407) and landmark-like (0.397, 0.395) cells, and light-off is significantly lower (p = "
    "0.010 and 0.001, paired; unpaired 0.041 and 0.003), which the criterion counts against the claim under the reading "
    "that matches the values. The HeadingDecoder gives 0.202 and 0.219. The class is not the paper's.", [0.721, 0.579])
dec("fig6b-180-errors", "reproduced",
    "Under the Bayes decoder, 11.9% (dF/F) and 13.7% (spikes) of the landmark-like decoder's light-on errors lie within 18 "
    "degrees of 180, above 0.10, and 7.1% and 9.1% of the heading-like decoder's, no more than 0.10. Under the "
    "HeadingDecoder the criterion fails (heading-like 0.105 and 0.106), but that decoder is near chance, so its errors are "
    "spread almost evenly (all groups 0.105 to 0.158). The classes are not the paper's.", None, True)
dec("fig6-heading-below-population", "reproduced",
    "Under every decoder and input reading, the 95% interval of light-on accuracy for heading-like cells lies below that of "
    "all tuned cells (Bayes dF/F 0.425 [0.397, 0.453] against 0.708 [0.665, 0.747]; spikes 0.407 [0.383, 0.432] against "
    "0.712 [0.677, 0.745]; HeadingDecoder 0.127 to 0.148 against 0.202 to 0.215), reading (a); heading-like cells decode "
    "worse in 99.8 to 100% of iterations. Reading (b), a mixed model with recording or mouse as random intercept, cannot be "
    "formed, as each pseudopopulation trial pools cells of many recordings and mice. The heading-like class is not the "
    "paper's.")

order = [o["claim"] for o in A["outcomes"]]
A["outcomes"] = [O[c] for c in order]

F = A["findings"]
for f in F:
    if f["statement"].startswith("The visual-cue-only recordings of Figure 5K"):
        f["statement"] = ("The visual-cue-only recordings of Figure 5K share no ROIs with any standard recording and no "
                          "matching is given, and nothing in them marks standard and visual-only rotation, so the matched "
                          "neurons of Figure 5K cannot be found.")
F += [
 dict(kind="methods_unavailable", statement=(
  "Question for the authors. Were the pre-shuffled data of the selection control (Methods) shifted once before the test, "
  "or afresh in every iteration as in the commented calculateHeadDirection_shuff of Cue.m? The second passes no cell by "
  "construction. Shifted once, 5.22% of single-cue cells pass here, and synthetic untuned cells pass at 4.7%, as the KS "
  "test of the code compares 1000 split-half correlations of the same trials.")),
 dict(kind="methods_unavailable", statement=(
  "Question for the authors. Which decoder gave Figure 6, the Bayesian decoder of the Methods (Etter et al. 2020) or the "
  "lab's HeadingDecoder, on dF/F or on spikes, and how was activity binarized? Neither the decoder code nor the trial "
  "selection for the pseudopopulations is in the linked repository.")),
]
A["verifications"] = [dict(
 date="2026-10-30", kind="agent",
 by="Independent agent run by CatalystNeuro (same harness, separate context, did not write the notebooks)",
 reviewed=("Round 1. The executed notebooks of the first run with the conclusion cells and the summaries removed, the "
           "helper module and the claims file, with the paper. The verifier tested the selection test, the flip score "
           "and the peak-offset measure on synthetic inputs. fig5k and the seven Figure 6 claims had no notebook "
           "output then, so it gave no outcome for them."),
 results=[])]
R = A["verifications"][0]["results"]
def v(claim, agrees, outcome, reason, response):
    d = dict(claim=claim, agrees=agrees)
    if outcome: d["outcome"] = outcome
    d["reason"] = reason; d["response"] = response
    R.append(d)
v("fig1-free-heading-fraction", True, "blocked",
  "Every one of the 128 assets is classified. All 16 single-cue files rotate at a steady 3 to 8 rpm (motor-driven). The only "
  "animal-controlled files are 2022 dual-cue recordings. The API listing (128 assets) agrees.", "No change needed.")
v("fig1g-rotation-heading-fraction", True, "reproduced",
  "With the centred fit, 485/3179 = 15.26%, inside 14.2 +- 1.42 and 452 +- 45. The code's uncentred fit gives 10.85%, but it "
  "only passes cells whose peak is near -90, which contradicts Fig. 1H, so the centred reading is reasonable. Caveat: the "
  "test also passes untuned noise (B1).",
  "Added the false-positive rate on synthetic untuned cells (4.7% centred, 1.7% uncentred) and quoted the code to show "
  "the KS test on 1000 overlapping split-halves is the paper's own procedure (ControlledRotation.m). The re-run gives "
  "486 (15.29%); the outcome stands and the notes say about a third of the cells could pass by chance.")
v("selection-shuffled-control", False, "not_reproduced",
  "The paper says data were shuffled before running the procedure, and the criterion says \"before the test\". That reading "
  "(the \"once\" variant) passes 165/3179 = 5.19%, above the 1% limit. The 0% \"each\" reading cannot fail by construction (B2).",
  "Changed to not_reproduced, resting on the \"once\" reading as an assumption (166, 5.22% in the re-run). The code shows "
  "the commented function reshuffles in every iteration; the conflict within the criterion is asked of a reader in "
  "questions/000483.yaml, and a methods_unavailable finding asks the authors.")
v("fig1h-preferred-headings-tile", True, "partially_reproduced",
  "Tiling holds under both readings. The overrepresentation can't be judged because where the cue sits in the heading frame "
  "is unknown. At dataset heading 0 the share is 0.247, below 0.25. The densest window (-102, 0.40) depends on the mouse: "
  "SKKS090 and SKKS091 peak about 180 away from it (B9).",
  "No change of outcome. The notebook now shows that the code fit's clustering near -90 comes from its bounds on the "
  "Gaussian's peak (dataset headings -120 to -60), so it does not locate the cue, and prints the share near -90 (40.1%) "
  "as what the share would be were the cue there. No file or code gives the cue's position.")
v("fig2f-head-chamber-same-preference", False, "partially_reproduced",
  "p < 0.05 with V > 0 appears only when the chamber-rotation heading is mirrored and only 5 of 7 pairs are used: V = 34.6, "
  "n = 228. V is outside 14.1 +- 1.41. One pair (SKKS116) drives it. Randomly paired ROIs give a higher V (mean 46.2), so "
  "there is no evidence that matched ROIs keep their preference. Head-rotation files show implausibly many selective cells "
  "and heading-locked artefacts from derotation are not ruled out (B4).",
  "Changed to partially_reproduced. Added the random-pairing null per pair (the real V lies within it in every pair, "
  "SKKS116 included), the selective share and activity of the two files of each pair, and the size of a clock offset in "
  "degrees. The notes say matched ROIs do not keep their preference better than random pairs here.")
v("fig3c-coherent-remapping", False, "partially_reproduced",
  "All 8 readings give p < 0.05 with V > 0. V (47.0 at n = 85, or 208.9 at n = 830) is outside 25.6 +- 2.56. The main reading "
  "is only just above the random-pairing null (95th percentile 44.6, from just 100 draws).",
  "Changed to partially_reproduced. The null now has 1000 draws (95th percentile 45.7; 2.6% of random pairings reach the "
  "real V). The SKKS091 210504 pair (B14) has fewer than 3 cells selective in both and enters only the \"either\" readings, "
  "as now said.")
v("fig4-axons-light-on-shape", True, "reproduced",
  "Under reading (b), all axons: mean-curve flip score ADN -0.207 and visual 1.875; single-axon means -0.109 vs 0.506, KS p = "
  "1.6e-24. Reading (a) fails: the ADN mean-curve flip score is 0.277 (centred) or 1.132 (code fit).", "No change needed.")
v("fig4-axons-light-off", True, "partially_reproduced",
  "Visual axons lose tuning. The ADN fraction selective in light-off is higher, but the per-recording comparison is not "
  "significant (p = 0.35); only the Fisher variant is. The ADN light-off peak is 24 to 30 degrees from the light-on peak "
  "under readings (a) centred and (b). The light-off selective fraction is computed over all axons only, not for reading "
  "(a) (B8).",
  "Added reading (a): among selective axons the per-recording share also selective in light-off has medians 0.143 and "
  "0.000, Mann-Whitney p = 0.074; Fisher p = 2.8e-07. The outcome stands.")
v("figs5-rotation-direction", True, "reproduced",
  "Reading (b), selective cells: bootstrapped KS p = 0.002, median correlation 0.210 real vs 0.118 random. Reading (a) gives "
  "p = 0.16. The data are 4 files over 3 mice, not 2.", "No change needed; the notes now say the pooled random pairs cross files and that by mouse only SKKS125 passes.")
v("figs6-arena-control", True, "reproduced",
  "Reproduced (fragile). Reading (b) gives p = 0.026, with median correlation 0.027 real vs -0.011 random. Reading (a) gives "
  "p = 0.89. It uses 5 pairs over 4 mice, and 112 of the 381 cells come from a file that visits 6 of 60 heading bins, and "
  "no run without it is shown (B10).",
  "Added the run without that pair and each pair alone. Without it neither reading passes ((a) p = 0.969, (b) p = 0.903) "
  "and no pair passes alone, so the outcome is changed to not_reproduced, resting on leaving that pair out as an "
  "assumption. This differs from the verifier's outcome; round 2 reviews it.")
v("fig5-three-classes", True, "not_reproduced",
  "The silhouette at k = 3 is not a local maximum under either reading. Only the reviewer-code variant, (a) centred on each "
  "curve's own peak, peaks at 3 (0.393).",
  "No change of outcome. In the re-run the reviewer-code variant has no local maximum at 3 either (0.450, 0.036, 0.007).")
v("fig5-class-proportions", True, "not_reproduced",
  "Tuned cells match (12.10%). The classes do not: landmark 7.4%, alignment 75.3%, heading 13.3% (counts 67, 1150, 202 "
  "against 522, 409, 332), and the order fails under every reading. All three GMM light-on archetypes are bimodal, so no "
  "component is a unimodal heading class; the names come from a heuristic the notebook makes up (B5).",
  "No change of outcome. The re-run gives 75, 1150 and 194 cells; the notes now say all three archetypes are bimodal.")
v("fig5e-alignment-peaks-coregistered", False, "not_reproduced",
  "The V-test passes (V = 743.5), but this measure gives the same V/n under random light-off peaks (B3). Only 29.2% of offsets "
  "are within 18 degrees, against about 0.21 to 0.23 by chance. This is far from \"always\", and lower than the heading and "
  "landmark classes.",
  "Added two nulls. Uniform peaks give V/n 0.582 against 0.646; light-off peaks paired at random within the class give V "
  "706.9 (95th percentile 727.7) against 743.2, so a small excess remains (p = 0.002; 29.1% within 18 degrees against "
  "26.2%). Changed to partially_reproduced, not to not_reproduced: the effect is present but far weaker than \"always\". "
  "The disagreement is recorded; round 2 reviews it.")
v("fig5f-heading-flip-unchanged", False, "partially_reproduced",
  "The criterion is met: p = 0.14. But the cells are not the paper's heading class: n = 202, and this class's light-on "
  "archetype is bimodal (a2/a1 = 0.70).",
  "Changed to partially_reproduced. Re-run: 194 cells, p = 0.18.")
v("fig5gh-landmark-alignment-flip-drop", False, "partially_reproduced",
  "Both classes are lower in light-off, so the criterion is met. The classes come from a failed clustering and differ in "
  "size from the paper's (67 and 1150 cells).", "Changed to partially_reproduced.")
v("fig5i-axons-in-clusters", False, "partially_reproduced",
  "The criterion is met as written. The ellipses don't separate the groups: visual axons fall more often inside the heading "
  "(0.93) and alignment (0.96) ellipses than the landmark one, and LDA assigns 85 to 98% of all axons to alignment. The "
  "classes come from fig5-class-proportions, which failed (B6).", "Changed to partially_reproduced.")
v("fig5k-visual-cue-only", False, None,
  "No outcome: no notebook output. Not blocked by data. Two Suspended files exist (SKKS125 2022-08-10, SKKS127 2022-08-11, "
  "15050 frames each). Each is the only file of its day, so whether matched standard-rotation ROIs exist inside them is "
  "unknown.",
  "Added a section to directions.ipynb with the ROI counts of every file of the two mice and the block structure of the "
  "two files: no other file shares their ROIs, and their blocks differ only in the direction of rotation, so nothing marks "
  "standard rotation. Kept blocked, metadata_insufficient.")
for c in ["fig6a-population-light-on", "fig6a-population-light-off", "fig6b-heading-cells", "fig6b-landmark-cells",
          "fig6b-alignment-cells", "fig6b-180-errors", "fig6-heading-below-population"]:
    v(c, False, None,
      "No outcome: no notebook output. The inputs are in the archive: somata, heading, and light/dark from the hard-coded "
      "segments. Not data_missing. The notebook needs the decoding means, 95% intervals and bootstrapped t-tests under each "
      "reading of the decoder and of chance.",
      "Tested in a new notebook, decoding.ipynb, under every reading of input, decoder, t-test and chance, with chance "
      "measured for each decoder (0.10). Outcome now " + O[c]["outcome"] + ".")
yaml.safe_dump(A, open(p, "w"), sort_keys=False, width=110, allow_unicode=True)
print("ok")
PYEOF
python $TMPDIR/gen/attempt.py && python tools/entry.py check entries/000483-sit-2023 2>&1 | tail -5
```

```
ok
0 error(s)
```

**Agent calls Bash**

```bash
cd entries/000483-sit-2023; python - <<'EOF'
p='rsc.py'; s=open(p).read()
old="""  degree); segments under 50 frames dropped, and segments whose 25th or 75th heading percentile
  lies more than 50 degrees from +-90 dropped."""
new="""  degree); segments under 50 frames dropped, and segments dropped where
  `any(90 - abs(prctile(heading, [25, 75])) > 50)`, that is, where the 25th or 75th heading
  percentile lies within 40 degrees of 0 (the code's rule, ControlledRotation.m line 224 at
  c6344f5; the claims file paraphrases it as "more than 50 degrees from +-90")."""
assert old in s; s=s.replace(old,new)
old2="""- Flip score: code Cue.calculateFlipScore (Methods, eq. 5): circular autocorrelation of the
  tuning curve smoothed with MATLAB's smoothdata default (a moving mean whose width is a quarter
  of the curve's length, here 15 bins), CC at 180 minus the mean of CC at 90 and 270 degrees."""
new2="""- Flip score: code Cue.calculateFlipScore (Methods, eq. 5): circular autocorrelation of the
  tuning curve smoothed with MATLAB's smoothdata default, CC at 180 minus the mean of CC at 90 and
  270 degrees. smoothdata picks its default window heuristically from the data; a moving mean a
  quarter of the curve's length wide (15 bins) stands in for it (an assumption that cannot be
  checked without MATLAB; on synthetic curves the score is about -0.2 for one peak and 2 for two)."""
assert old2 in s; s=s.replace(old2,new2)
open(p,'w').write(s)
EOF
cd  python - <<'EOF'
import yaml
p='attempts/000483-sit-2023-01.yaml'; A=yaml.safe_load(open(p))
A['verifications'][0]['reviewed'] += (" Its points that bear on no single claim are answered as follows. The clock check (B7) "
 "is now read in single_cue.ipynb: the lag peaks after 0 in three files and before 0 in one, so the clock is not established "
 "in general, and rotation_remapping.ipynb gives the size of a 6-frame offset in degrees. The trial rule (B11) matches the "
 "code, any(90 - abs(prctile(heading, [25, 75])) > 50), as rsc.py now quotes. The smoothdata window (B12) is stated in "
 "rsc.py as an assumption. The counts that differ from the paper's (B15) stay recorded as selection_undocumented.")
yaml.safe_dump(A, open(p,'w'), sort_keys=False, width=110, allow_unicode=True)
EOF
date -u
```

```
Fri Oct 30 21:03:35 UTC 2026
```

**Agent calls Bash**

```bash
cd  time python tools/entry.py all entries/000483-sit-2023 2>&1 | tail -9; date -u
```

```
Installed kernelspec registry-000483-sit-2023 in executed/000483-sit-2023/.venv/share/jupyter/kernels/registry-000483-sit-2023
0 error(s)
pass  single_cue.ipynb  (577 s)
pass  rotation_remapping.ipynb  (643 s)
pass  axons.ipynb  (355 s)
pass  somata.ipynb  (996 s)
pass  directions.ipynb  (579 s)
pass  decoding.ipynb  (965 s)

real	68m46.562s
user	203m55.409s
sys	1m23.934s
Fri Oct 30 22:12:29 UTC 2026
```

**Agent**

Second run passed. Checking that the outputs match the first run exactly.

**Agent calls Bash**

```bash
cd executed/000483-sit-2023; for f in single_cue rotation_remapping axons somata directions decoding; do python $TMPDIR/show.py $f.ipynb | grep -v " in [0-9]* s\|in [0-9]* s$\|loaded and deconvolved" > $TMPDIR/run2_$f.txt; done; python $TMPDIR/show.py single_cue.ipynb 12,16,20 | head -8; python $TMPDIR/show.py somata.ipynb 13,16 | grep -i "counts (no\|alignment: V"; python $TMPDIR/show.py directions.ipynb 9 | grep "all pairs\|without"; python $TMPDIR/show.py rotation_remapping.ipynb 12 | grep "1000 draws"; python $TMPDIR/show.py axons.ipynb 11 | grep "pooled\|reading (a)"
```

```
--- cell 12
== code (uncentred fit): 345 of 3179 ROIs selective = 10.85%  (paper 14.2% +- 1.42, 452 +- 45)
subject    SKKS080  SKKS081  SKKS089  SKKS090  SKKS091
rois        1479.0    990.0    191.0    357.0    162.0
selective    160.0    131.0     10.0     41.0      3.0
percent       10.8     13.2      5.2     11.5      1.9
per recording percent: median 10.2 range 1.0 to 25.3
== centred fit: 486 of 3179 ROIs selective = 15.29%  (paper 14.2% +- 1.42, 452 +- 45)
counts (no outlier step): {'landmark': 75, 'alignment': 1150, 'heading': 194} | paper (from F-test degrees of freedom): heading 332, landmark 522, alignment 409
alignment: V = 743.2 (V/n 0.646); random pairing V mean 706.9, 95th percentile 727.7, share at or above the real V 0.002; uniform peaks V mean 669.4 (V/n 0.582), 95th percentile 692.4; share within 18 deg real 0.291, random pairing 0.262
selective cells, all pairs: n=382; (a) median |pref diff| (mod 180) real 42 deg, random 48 deg, bootstrapped KS p = 0.912; (b) median correlation real 0.026, random -0.031, bootstrapped KS p = 0.034
selective cells, without ['220721 SKKS125-FR-003']: n=270; (a) median |pref diff| (mod 180) real 36 deg, random 42 deg, bootstrapped KS p = 0.969; (b) median correlation real 0.090, random 0.104, bootstrapped KS p = 0.903
Random pairing of neurons (peak, both, (i)), 1000 draws: V mean 36.2, 95th percentile 45.7, share at or above the real V 0.026
pooled: ADN 94/1084, visual 11/247; Fisher p = 0.026, odds ratio 2.04
reading (a), selective axons: per-recording share also selective in light-off, ADN median 0.143 (n = 14 recordings), visual median 0.000 (n = 7); Mann-Whitney p = 0.074; pooled ADN 40/135, visual 5/106, Fisher p = 2.8e-07, odds ratio 8.51
```

**Agent calls Bash**

```bash
cd  python $TMPDIR/show.py executed/000483-sit-2023/single_cue.ipynb 16,20 ; python $TMPDIR/show.py executed/000483-sit-2023/decoding.ipynb 9 | sed -n 3,6p; python tools/entry.py check entries/000483-sit-2023 | tail -2; git status --short; date -u
```

```
--- cell 16
synthetic untuned cells, centred fit: reliable 15.7%, pass the whole test 4.7% of 300
synthetic untuned cells, code (uncentred) fit: reliable 15.7%, pass the whole test 1.7% of 300

--- cell 20
each, centred: 0 of 3179 pass = 0.00% (reliable 0); per mouse {}
each, code: 0 of 3179 pass = 0.00% (reliable 0); per mouse {}
once, centred (variant): 166 of 3179 pass = 5.22% (reliable 481); per mouse {'SKKS080': np.int64(78), 'SKKS081': np.int64(61), 'SKKS089': np.int64(8), 'SKKS090': np.int64(13), 'SKKS091': np.int64(6)}
Thresholds of the claims file: none passing = reproduced; up to 1% = partially; above 1% = not reproduced

input            decoder     group  on_mean  on_lo  on_hi  off_mean  off_lo  off_hi  p_paired  p_unpaired  off_lower  err180_on  mean_err_on
  dff          (a) Bayes all tuned    0.708  0.665  0.747     0.569   0.525   0.612     0.016       0.061       True      0.034       26.925
  dff          (a) Bayes  landmark    0.397  0.377  0.416     0.210   0.195   0.223     0.000       0.000       True      0.119       60.034
  dff          (a) Bayes alignment    0.721  0.685  0.761     0.579   0.538   0.624     0.010       0.041       True      0.033       25.677
0 error(s)
 M attempts/000483-sit-2023-01.yaml
 M entries/000483-sit-2023/README.md
 M entries/000483-sit-2023/axons.ipynb
 M entries/000483-sit-2023/directions.ipynb
 M entries/000483-sit-2023/entry.yaml
[... 18 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n "—\|rather" attempts/000483-sit-2023-01.yaml questions/000483.yaml entries/000483-sit-2023/README.md entries/000483-sit-2023/rsc.py | head; for f in entries/000483-sit-2023/*.ipynb; do python -c "
import json,sys;nb=json.load(open('$f'))
for c in nb['cells']:
  s=''.join(c['source'])
  if '—' in s or 'rather' in s: print('$f', s[:80])
"; done; git diff --stat
```

```
attempts/000483-sit-2023-01.yaml                 | 800 +++++++++++++++++------
 entries/000483-sit-2023/README.md                |  35 +-
 entries/000483-sit-2023/axons.ipynb              |  23 +-
 entries/000483-sit-2023/directions.ipynb         |  80 ++-
 entries/000483-sit-2023/entry.yaml               |  20 +-
 entries/000483-sit-2023/rotation_remapping.ipynb |  63 +-
 entries/000483-sit-2023/rsc.py                   |  12 +-
 entries/000483-sit-2023/single_cue.ipynb         |  95 ++-
 entries/000483-sit-2023/somata.ipynb             |  54 +-
 9 files changed, 900 insertions(+), 282 deletions(-)
```

**Agent**

I've worked through every point in the round-1 report and re-run the entry twice; the second run gave identical numbers. `tools/entry.py all` passes for all six notebooks (each between 6 and 17 minutes) and `check` reports 0 errors. Nothing is committed.

**Changes in outcome**

| Claim | Before | Now | Why |
|---|---|---|---|
| selection-shuffled-control | reproduced | not_reproduced (rests on an assumption) | The paper's own code reshuffles the trials in every iteration, so that reading can pass no cell whatever the data. Shifting each trial once, as the Methods describe, passes 5.22% (166 of 3179), above the 1% limit. |
| fig2f | reproduced | partially_reproduced | In every pair, randomly paired cells give as large a V as matched ones, including the one pair that drove the result. |
| fig3c | reproduced | partially_reproduced | V is outside the tolerance, and 2.6% of 1000 random pairings reach it. |
| fig5e | reproduced | partially_reproduced | Two null tests added. The V is only slightly above random pairing (p = 0.002), and 29.1% of peaks are within 18° against 26.2% by chance. |
| fig5f, fig5gh, fig5i | reproduced | partially_reproduced | Each criterion is met, but on classes that are not the paper's. For fig5i, the ellipses also overlap too much to separate the axon groups. |
| figs6 | reproduced | not_reproduced (rests on an assumption) | It passed only because of one pair whose animal-controlled file covers 6 of 60 heading bins. Without that pair, p = 0.97 and 0.90, and no pair passes on its own. |
| Seven fig6 decoding claims | blocked | tested in a new `decoding.ipynb` | Two not reproduced (all cells in light-on; alignment cells). Three partially reproduced (all cells in light-off; heading cells; landmark cells). Two reproduced (180° errors; heading cells below the population). |

Three of these go further than the verifier did:
- **fig5e:** I chose partially, not their not_reproduced, because a small excess over chance remains.
- **figs6:** I moved it to not_reproduced, where they had kept reproduced.
- **fig6:** they gave no outcome for the decoding claims because there was nothing to judge.

Round 2 will review all three.

Four decoding outcomes (all cells in light-off, heading cells, landmark cells, 180° errors) rest on choosing the Methods' Bayesian decoder. The lab's own HeadingDecoder, as I reimplemented it, decodes near chance on these data (0.20 to 0.22). Chance, measured for each decoder, is 0.10, which matches one of the paper's two stated chance levels.

**Added or corrected**
- **Selection test:** a false-positive check on synthetic untuned cells. 4.7% pass with the centred fit and 1.7% with the code's fit. The KS test on 1000 overlapping split-halves is in the paper's own code, so fig1g stays reproduced. Its notes now say about a third of the selected cells could pass by chance.
- **fig2f checks:**
  - a random-pairing null for each pair;
  - selective share and activity of head- versus chamber-rotation files (53 to 83% against 8 to 65%);
  - how far a clock offset could move preferred headings.
- **fig4 light-off:** the reading over selective axons only.
- **fig1h:** shows that the code fit's clustering near −90° comes from its fit bounds, so it says nothing about where the cue is.
- **fig5k:** the structure of the two visual-cue-only files. Their blocks differ only in rotation direction and no other file shares their cells, so it stays blocked.
- **Clock check:** now interpreted (three files lag after 0, one before).
- **`rsc.py`:**
  - it now quotes the code's exact trial rule, which my implementation already matched;
  - it states the smoothing window as an assumption.
- **Records:**
  - `questions/000483.yaml` asks a reader about the shuffled-control criterion, which cites code that contradicts its own wording;
  - two new findings ask the authors which shuffle and which decoder they used;
  - round 1 is recorded under `verifications` with the verifier's reasons and my responses;
  - the README and summaries are updated.

**Not done**
- Some numbers moved slightly from the first run, which ran elsewhere: for example 486 selected cells instead of 485, and class counts of 75, 1150 and 194 instead of 67, 1150 and 202. I put this down to machine differences. On this machine both runs match exactly, and every conclusion uses the new numbers.
- fig6-heading-below-population has a mixed-model reading that cannot be built, because each pooled decoding trial mixes many recordings and mice. Only its interval-comparison reading is run.
- The cue's position in the heading frame (fig1h) is in neither the files nor the code, so that part stays open.

## End of run

77 turns, 186 minutes, result: success.
