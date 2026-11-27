# schapiro-2024 · claims · run 45669382914

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cat docs/protocol.md; ls paper/ claims/ tools/; cat claims/fouke-2025.yaml
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
grep -n "^#" docs/protocol.md | head -60; ls paper/ claims/ tools/
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
3	Version: `pilot-19`. Record this version in the attempt's provenance.
4	
5	This is what agents, or people, do to attempt a target and deposit the
6	result. A target is a dataset in a public archive and a paper it names. How
7	each archive's datasets are named, versioned and read is in
8	[archives.md](archives.md); the examples here are from DANDI, the first. It is written from the pilot attempts
9	([pilot notes](https://github.com/encorescience/encore-registry/blob/main/docs/pilot-notes.md)); the reasons for the rules are there.
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

**Agent calls Read**

```json
{
 "file_path": "claims/fouke-2025.yaml"
}
```

```
1	# Claims for Fouke, He, Loring & Naumann (2025) on dandiset 001453.
2	# Source: the accepted author manuscript in PubMed Central (PMC12218792), full text, read
3	# from its Results, figure legends and STAR Methods. The version of record is not open access.
4	#
5	# When these criteria were written, the author had seen the data check only: the file list,
6	# subject metadata, frame rates, units, trial structure and stimulus codes of every file, and
7	# the extent of positions. No claim's analysis had been run. The author had also read the
8	# outputs printed in the paper's own analysis notebook (Fig1-S1.ipynb, GitLab commit 33a5c29),
9	# which include per-stimulus median speeds and angular velocities and its statistics.
10	#
11	# The dandiset holds only the freely swimming tracking data of Figure 1 and Figure S1. Its
12	# stimulus codes 0 to 20 carry no names. The names come from the paper's code and from the
13	# stimulus software's protocol file (see stimulus-code-link), so the claims that need them
14	# use outside data and depend on that claim.
15	#
16	# Method choices fixed here, from the paper's Fig1-S1.ipynb where the Methods are silent: a
17	# trial is one stim_index; tracked frames only; positions smoothed with a Savitzky-Golay filter
18	# (21 frames, order 2); trials rejected when the absolute cumulative heading change exceeds
19	# 1000 degrees in the first 10 s or 2000 degrees in the first 35 s, or the mean speed exceeds
20	# 100 mm/s; measures taken from 3 s to 35 s after the first frame (the 3 s stationary phase is
[... 302 more lines not kept]
```

**Agent calls Bash**

```bash
wc -l paper/*.txt; cat paper/*.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-registry-encore-registry/d2665079-c30c-4a47-89a4-6b2018ac5d3a/tool-results/bnuzm21sq.txt"
}
```

```
1	276 paper/10.7554-elife.98844.txt
2	DOI: 10.7554/elife.98844
3	Version: as served by europe_pmc
4	Source: europe_pmc (PMC11479588, open access JATS)
5	Stored: 2026-11-25
6	Extracted: JATS XML flattened
7	------------------------------------------------------------------------
8	I h block reveals separation of timescales in pyloric rhythm response to temperature changes in Cancer borealis
9	
10	Motor systems operate over a range of frequencies and relative timing (phase). We studied the role of the hyperpolarization-activated inward current (I h ) in regulating these features in the pyloric rhythm of the stomatogastric ganglion (STG) of the crab, Cancer borealis, as temperature was altered from 11°C to 21°C. Under control conditions, rhythm frequency increased monotonically with temperature, while the phases of the pyloric dilator (PD), lateral pyloric (LP), and pyloric (PY) neurons remained constant. Blocking I h with cesium (Cs + ) phase advanced PD offset, LP onset, and LP offset at 11°C, and the latter two further advanced as temperature increased. In Cs + the frequency increase with temperature diminished and the Q 10 of the frequency dropped from ~1.75 to ~1.35. Unexpectedly in Cs + , the frequency dynamics became non-monotonic during temperature transitions; frequency initially dropped as temperature increased, then rose once temperature stabilized, creating a characteristic ‘jag’. Interestingly, these jags persisted during temperature transitions in Cs + when the pacemaker was isolated by picrotoxin, although the temperature-induced change in frequency recovered to control levels. Overall, these data suggest that I h plays an important role in maintaining smooth transitory responses and persistent frequency increases by different mechanisms in the pyloric circuitry during temperature fluctuations.
11	
12	## Introduction
13	
14	Many repetitive motor patterns, such as breathing, walking, and swimming, operate over a wide range of frequency and relative timing
[... 264 more lines not kept]
```

**Agent calls Bash**

```bash
grep -l "archive: dryad" claims/*.yaml | head -5; grep -h -i -B1 -A3 "code.*inside the dataset\|code is deposited\|deposited with the data\|in the dataset itself" claims/*.yaml | head -40; sed -n 1,80p tools/claims_check.py
```

```
claims/dias-2025.yaml
claims/didion-gency-2024.yaml
claims/wang-2024.yaml
# Code. The paper's Key Resources Table and Data and Software Availability say the custom MATLAB
# code is deposited with the data at CRCNS (http://crcns.org). By the data descriptor it is the
# analysis_scripts directory of pfc-5 itself (<metric>_compute, <metric>_stat_group,
# <metric>_stat_group_hem, subfunctions; FieldTrip). Being among the data set's files, it was
# not read in this run, and no commit is recorded. Every method below is from the paper's text.
--
#   128, 152.5 Hz) do not lie on one log grid from 1 to 192 Hz (13.5 to 16 is a ratio of 1.19,
#   16 to 22.5 of 1.41). The bank is to be taken from the analysis scripts deposited with the data;
#   failing those, centres that reproduce the named frequencies and counts are chosen and stated,
#   as an assumption. This could move a peak by one bin.
# M3. Task-induced power z. Baseline power pooled per channel and frequency, r points (r = trials
--
#
# Code. The paper's Data Availability says its custom MATLAB code is deposited at CRCNS with the
# data. By the data descriptor it is the analysis_scripts directory of data set fcx-3 itself. It is
# one of the data set's files, which this reader does not open, so it was not read and no commit is
# recorded. Every method below is from the paper's text. Where the scripts settle a detail named as
[... 97 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 1,40p claims/wang-2024.yaml; python -c "import json;d=json.load(open('schemas/claims.schema.json'));print(json.dumps(d,indent=1)[:5000])"
```

```
# Claims for Wang, Wang, Yang, Lu, Fields, Xu, Shen, Wei & Friman (2024), Evolution Letters,
# doi:10.1093/evlett/qrad056, on Dryad dataset doi:10.5061/dryad.tdz08kq5d.
# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"), 2026-10-27,
# protocol as stated in docs/protocol.md.
#
# Text read: the version of record, full text from Europe PMC (PMC10959482, full-text XML), with
# Methods, figure legends, Table 1, and the supplement (qrad056_suppl, Supplementary Figures
# S1 to S5 and Tables S1 to S6, including the ANOVA tables S1 to S3). The dataset's files were not
# opened. Its archive entry names one Excel workbook of the data for all figures and a README.
#
# Code read: the analysis code the Dryad entry links, Zenodo record 8420504
# (doi:10.5281/zenodo.8420504), one file all_r_scripts.R (md5 cff6a1c2e424a2f74ec289cd4888afa8).
# It holds plotting code for Figures 1B, 1C, 2 and 3, the growth-curve fits and a summarySE helper.
# It holds no ANOVA. What it settles: growth parameters are fitted with grofit gcFitModel at its
# default settings, which fit the logistic, Richards, Gompertz and exponential Gompertz models and
# keep the one with the lowest AIC (grofit 1.1.1-1 source, grofit.control and gcFitModel); the
# Methods say a logistic model, so logistic is the main reading here and the code's AIC choice is a
# variant. Failed fits are set to 0 in the code. The ancestral twitching diameter drawn as the
# dashed line of Figure 2D is 9.38 cm.
#
[... 168 more lines not kept]
```

**Agent calls Bash**

```bash
python -c "import json;d=json.load(open('schemas/claims.schema.json'));print(json.dumps(d,indent=1)[5000:])" | head -150; ls papers/datasets/ | grep schapiro; cat papers/datasets/schapiro-2024.yaml 2>/dev/null
```

```
`: the archive and the pinned identifier of the data, e.g. 'PRIDE PXD012345' or 'Zenodo doi:10.5281/zenodo.123'.",
      "type": "string",
      "minLength": 1
     },
     "datasets": {
      "description": "Only when the paper is tested on more than one dataset: the folder names of those this claim rests on.",
      "type": "array",
      "items": {
       "type": "string"
      },
      "minItems": 1
     }
    },
    "allOf": [
     {
      "not": {
       "required": [
        "quote",
        "inferred"
       ]
[... 140 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && timeout 120 git clone -q --depth 1 https://github.com/sg-s/crabsort && cd crabsort && git log -1 --format='%H %cd' && ls
```

```
ee237eaea4565d4139a31a40fe180f884175a20b Thu Sep 22 16:40:39 2022 -0400
+crabsort
+csCluster
+csLoadFile
+csRedDim
@crabsort
LICENSE.txt
README.md
build
build_number
crabsort.sublime-project
default.m
docs
functionSignatures.json
helper-scripts
kapalin.json
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/crabsort && head -40 README.md; grep -rli "burst\|phase\|Q10\|temperature" --include=*.m . | head -20
```

````
# 🦀 crabsort

[![GitHub last commit](https://img.shields.io/github/last-commit/sg-s/crabsort.svg)]()


# Installation

## Using git

Clone these repos:

```
# bash
git clone https://github.com/sg-s/crabsort
git clone https://github.com/sg-s/puppeteer
git clone https://github.com/sg-s/srinivas.gs_mtools
```

and add the all to your MATLAB path. 

[... 35 more lines not kept]
````

**Agent**

Crabsort is mainly the spike sorter but has a few helper analysis functions; checking whether they bear on the paper's burst or Q10 definitions.

**Agent calls Bash**

```bash
cd $TMPDIR/crabsort && cat +crabsort/computePeriods.m | head -80; grep -rli "q10\|Q_10" . | head
```

```
% computes metrics on a bunch of data generated
% by crabsort.consolidate

function data_out = computePeriods(data, varargin)




if length(data) > 1
	for i = 1:length(data)
		data_out(i) = crabsort.computePeriods(data(i), varargin{:});
	end
	return
end


options.neurons = {};
options.ibis = [];
options.min_spikes_per_burst = 1;

[... 62 more lines not kept]
```

**Agent calls Bash**

```bash
grep -h -i "tolerance.*SD\|SD.*tolerance\|spread" claims/*.yaml | head -15
```

```
Tolerances are the paper's stated spread for the rates, one 5 ms bin for the epoch 2 peak time
    readings (e) relative to the position at t = 0; (f) the readings of fig2b-lateral-spread
- id: fig2b-lateral-spread
  - {quantity: SD of lateral distance at t = 0, value: 0.55, tolerance: 0.055, unit: cm}
  - {quantity: SD of lateral distance at t = 3 s, value: 2.30, tolerance: 0.23, unit: cm}
  - {quantity: SD of lateral distance at t = 2 s, value: 1.49, tolerance: 0.149, unit: cm}
    from 0.2 to 1.8 s. Tolerances are the paper's SD. Reproduced when all four means fall within
    0 to 1 s, (f) 0 to 1.8 s (the turn). Tolerances are the paper's SD for FT and RT, 10% for the
  - {quantity: SD of streak index, value: 1.36, tolerance: 0.136}
  - fig2a-success-rate. Lateral position relative to t = 0 was stated as fixed; the paper does not set the zero. Named it open, with the readings of fig2b-lateral-spread.
  criterion: Tolerances are 10% of each mean; the printed SDs (0.61, 0.77, 1.25, 16.9 Hz) are the
    spread over cells, not an uncertainty of the mean, and are reported for comparison (within
  criterion: Tolerances are the stated SDs, as the paper gives them as the spread of the values
    tolerance or below 0.1 s, and the mean SD after 0.5 s is within 25% of kappa (a plateau);
    cells of each class (Table S1). The tolerance is the paper's stated spread (protocol
```

**Agent calls Write**

```json
{
 "file_path": "claims/schapiro-2024.yaml",
 "content": "# Claims for Schapiro, Rittenberg, Kenngott & Marder (2024), eLife, doi:10.7554/elife.98844, on Dryad\n# dataset doi:10.5061/dryad.1rn8pk129 (\"Effects of Cs on temperature response of C. borealis pyloric\n# rhythm\").\n# Written by an agent (model \"claude-opus-5-5\", Claude Code, runner \"GitHub Actions\"), 2026-11-25,\n# protocol as stated in docs/protocol.md (version pilot-19).\n#\n# Text read: the version of record, full text from Europe PMC (PMC11479588, open access JATS), with\n# Results, Discussion, Methods, the figure legends of Figures 1 to 6, Figure 1-figure supplement 1\n# (the paper's only supplement) and Table 1. The dataset's files were not opened.\n#\n# Code. The Data availability statement says the code and data to reproduce the results and figures\n# were uploaded to the Dryad dataset itself. Being among the dataset's files, that code was not read\n# in this run and no commit is recorded. The Methods also link Crabsort (github.com/sg-s/crabsort,\n# commit ee237eaea4565d4139a31a40fe180f884175a20b, read), the MATLAB spike-sorting software used to\n# detect and assign spikes. It holds the sorting interface, file loading, clustering and generic\n# helpers (computePeriods, consolidate); the paper does not say those helpers were used, and nothing\n# in it fixes the frequency, Q10, phase or jag measures below. Every method below is from the paper's\n# text. Where the deposited scripts settle a detail named as open here, the author may follow them\n# and should say so.\n#\n# Data the paper used, as it reports them.\n# - Isolated stomatogastric nervous systems of adult Cancer borealis (STG desheathed), acquired\n#   November 2022 to December 2023. Extracellular recordings of lvn, pdn and pyn; intracellular\n#   recordings of PD, LP and PY somata; 10 kHz sampling; dish temperature from a thermocouple within\n#   1 cm of the STG.\n# - Step protocol (Figure 1A, Methods, Temperature protocol). 2 min at 11 degrees C, then steps of\n#   2 degrees C to 21 degrees C, each allowed to stabilize over 4 min; return to 11 degrees C; 10 min\n#   solution change; the protocol repeated in the other condition. Conditions saline and 5 mM CsCl,\n#   order randomized; N=21 experiments with both (Figures 1, 3, 5, 6; PY phases in 12 of them).\n# - Control experiments with two consecutive saline step protocols, N=6 (Figure 1E and 1F).\n# - Picrotoxin experiments, N=6: saline and Cs+ in random order, then Cs+ + 10^-5 M picrotoxin\n#   (Figure 4). The paper does not say whether these 6 are among the 21.\n# - Voltage clamp of PD and LP at 11 and 21 degrees C, saline and Cs+: held at -50 mV, steps to\n#   -100 to -120 mV for 12 s (Figure 1-figure supplement 1); 4 PD and 3 LP cells at 11 degrees C,\n#   3 PD and 5 LP cells at 21 degrees C.\n# - Measured variables: spike times of PD, LP and PY; temperature; membrane potential; clamp\n#   current.\n#\n# Method fixed by the paper and used throughout (Methods, Analysis; Results, section 1).\n# - PD bursts are two or more consecutive PD spikes separated from the next burst by at least\n#   200 ms. Period is the time between the first spikes of consecutive PD bursts; frequency is its\n#   inverse. Phase of an event is its delay from the first PD spike of the cycle divided by the\n#   period. Onset is the neuron's first spike in the cycle, offset its last.\n# - The frequency at a holding temperature is the mean over the times the preparation was within\n#   0.3 degrees C of the target (Results, The steady-state frequency increase, paragraph 3).\n# - Jag measure: frequency and temperature smoothed with a moving average over 30 and 10 pyloric\n#   cycles; a cycle is temperature-increasing when the smoothed temperature rose by more than\n#   0.01 degrees C from the previous cycle, otherwise stable; among increasing cycles, the percent\n#   with a smoothed frequency decrease of more than 0.002 Hz per cycle; among stable cycles, the\n#   percent with an increase of more than 0.002 Hz per cycle.\n# - Phase constancy: per experiment and condition, a line fitted to mean phase against temperature;\n#   slopes tested against zero across experiments by Wilcoxon signed-rank (non-normal) or one-sample\n#   t-test (normal), Bonferroni-adjusted for 10 tests (5 phases by 2 conditions).\n# - Normality by Shapiro-Wilk decides parametric or non-parametric tests; where the paper names the\n#   test used for a comparison, that test is used.\n# - Summary values are mean +- SD over experiments or cells.\n#\n# Details the paper leaves open, used by several claims (each claim names the ones it rests on).\n# - O1, Q10. \"as described previously (Tang et al., 2010)\", with no formula. Readings are (a) a fit\n#   of f = f11 * Q10^((T - 11)/10) to the six holding-temperature mean frequencies by nonlinear least\n#   squares; (b) a straight-line fit of log10 frequency on temperature, Q10 = 10^(10 * slope);\n#   (c) the two-point ratio (f21/f11)^(10/10).\n# - O2, which 11 degrees C. The holding period at 11 degrees C is read as the first one of each\n#   condition's step protocol (the 2 min before the first step); the return to 11 degrees C after\n#   21 degrees C is a variant.\n# - O3, jag smoothing and span. MATLAB movmean is centred by default; a centred window is the main\n#   reading, a trailing window a variant. The span of cycles is (a) the step protocol from the first\n#   cycle at 11 degrees C to the end of the 21 degrees C hold; (b) the whole recording of the\n#   condition, cooling included, cycles that did not warm counted as stable as the Methods' wording\n#   allows. The per-cycle temperature is the mean over the cycle (\"change in mean temperature\",\n#   Results, Cs+ revealed dynamic transitory frequency response, paragraph 2).\n# - O4, cycles that form a phase at a temperature. (a) cycles within 0.3 degrees C of the target,\n#   as for frequency; (b) all cycles of the holding period (yellow in Figure 1A). For the slope,\n#   (a) a line through the six per-temperature means; (b) a line through all cycles' phases against\n#   their temperature.\n# - O5, Tukey HSD after a one-way repeated-measures ANOVA. (a) MATLAB multcompare on the fitted\n#   repeated-measures model (Tukey-Kramer on paired differences); (b) the classic Tukey HSD using the\n#   ANOVA's within-subject error term. Both are reported.\n# - O6, LP and PY onset and offset. The first and last spike of the neuron between the first spikes\n#   of two consecutive PD bursts (standard choice; the paper gives no burst rule for LP and PY).\n#\n# Tolerances. Where the paper gives mean +- SD, the tolerance is the stated SD, the paper's own\n# spread (protocol, Reader, step 3); a count or a number without spread has 10%.\nschema_version: 2\npaper: doi:10.7554/elife.98844\nclaims:\n- id: figs1-ih-reduced-11c\n  statement: At 11 degrees C and -110 mV, Ih in PD and LP cells was 1.5 nA in saline and 0.23 nA in\n    Cs+, a reduction of 93% (4 PD and 3 LP cells, paired t-test p = 0.0005).\n  source: Results, The steady-state frequency increase in response to elevated temperature was\n    decreased by Cs+, paragraph 1; Figure 1-figure supplement 1A and 1C\n  quote: At 11°C and –110 mV, I h was 1.5±0.83 nA in saline and 0.23±.5 nA in Cs + , a reduction of\n    93±30% (4 PD cells, 3 LP cells, paired Student’s t-test; p=0.0005)\n  statistics:\n  - test: paired Student's t-test\n    p: 0.0005\n    n: 4 PD and 3 LP cells\n  expected:\n  - quantity: Ih at -110 mV, 11 degrees C, saline\n    value: 1.5\n    tolerance: 0.83\n    unit: nA\n  - quantity: Ih at -110 mV, 11 degrees C, Cs+\n    value: 0.23\n    tolerance: 0.5\n    unit: nA\n  - quantity: reduction of Ih in Cs+, 11 degrees C\n    value: 93\n    tolerance: 30\n    unit: percent\n  criterion: Ih is the difference between the initial current needed to hold the step to -110 mV\n    and the steady-state current (Results, paragraph 1; Figure 1-figure supplement 1 legend). The\n    paper does not fix the windows. Readings are (a) initial current as the mean over the first\n    100 ms after the capacitive transient, steady state as the mean over the last 1 s of the 12 s\n    step; (b) initial current as the extreme current in the first 500 ms after the transient,\n    steady state as the last 1 s. Reduction per cell is 100 * (1 - Ih Cs / Ih saline), averaged\n    over cells; the ratio of the means is a variant. Reproduced when, under one reading, the\n    values are within tolerance and a paired t-test of saline against Cs+ gives p < 0.05.\n- id: figs1-ih-reduced-21c\n  statement: At 21 degrees C and -110 mV, Ih was 3.2 nA in saline and 0.6 nA in Cs+, a reduction\n    of 78% (5 LP and 3 PD cells, paired t-test p = 0.02).\n  source: Results, The steady-state frequency increase in response to elevated temperature was\n    decreased by Cs+, paragraph 1; Figure 1-figure supplement 1B and 1D\n  quote: At 21°C and –110 mV, I h was 3.2±2.3 nA in saline and 0.6±.8 nA in Cs + , a reduction of\n    78±20% (5 LP cells, 3 PD cells, paired Student’s t-test; p=0.02)\n  statistics:\n  - test: paired Student's t-test\n    p: 0.02\n    n: 5 LP and 3 PD cells\n  expected:\n  - quantity: Ih at -110 mV, 21 degrees C, saline\n    value: 3.2\n    tolerance: 2.3\n    unit: nA\n  - quantity: Ih at -110 mV, 21 degrees C, Cs+\n    value: 0.6\n    tolerance: 0.8\n    unit: nA\n  - quantity: reduction of Ih in Cs+, 21 degrees C\n    value: 78\n    tolerance: 20\n    unit: percent\n  criterion: As figs1-ih-reduced-11c, on the cells clamped at 21 degrees C.\n- id: fig1-cs-lower-frequency-11c\n  statement: At 11 degrees C pyloric frequency was lower in Cs+ than in saline (0.9 against\n    1.2 Hz, paired t-test p < 0.001).\n  source: Results, The steady-state frequency increase in response to elevated temperature was\n    decreased by Cs+, paragraph 2\n  quote: In Cs + at 11°C, the pyloric frequency was significantly decreased compared to control\n    conditions (saline ... 1.2±0.2 Hz; Cs + 0.9±0.2 Hz, paired Student’s t-test; p < 0.001)\n  statistics:\n  - test: paired Student's t-test\n    p: 0.001\n    p_relation: \"<\"\n    n: 21 experiments\n  expected:\n  - quantity: mean pyloric frequency at 11 degrees C, saline\n    value: 1.2\n    tolerance: 0.2\n    unit: Hz\n  - quantity: mean pyloric frequency at 11 degrees C, Cs+\n    value: 0.9\n    tolerance: 0.2\n    unit: Hz\n  criterion: Per experiment and condition, the mean PD burst frequency over times within 0.3 degrees\n    C of 11 degrees C, at the first 11 degrees C hold of the condition (O2). Reproduced when both\n    means are within tolerance and a paired t-test over the 21 experiments gives p < 0.05 with Cs+\n    lower.\n- id: fig1d-difference-grows-with-temperature\n  statement: The difference between a preparation's frequency in saline and in Cs+ increased\n    significantly as temperature increased.\n  source: Results, The steady-state frequency increase, paragraph 3; Figure 1D\n  quote: As temperature increased, the difference between a preparation’s frequency in saline and Cs\n    + significantly increased (one-way repeated measures ANOVA [F(5,85) = 43.259, p<0.001, N=21])\n  statistics:\n  - test: one-way repeated measures ANOVA\n    statistic: F(5,85) = 43.259\n    p: 0.001\n    p_relation: \"<\"\n    n: 21 experiments\n  criterion: Per experiment, saline minus Cs+ mean frequency at each of the six holding\n    temperatures (within 0.3 degrees C of 11, 13, 15, 17, 19 and 21 degrees C); a one-way\n    repeated-measures ANOVA on temperature. The printed degrees of freedom, F(5,85), imply 18\n    experiments, not 21; readings are (a) every experiment with values at all six temperatures in\n    both conditions; (b) the 21 experiments, with any missing value handled as MATLAB ranova does\n    (dropping the experiment). Reproduced when, under one reading, the temperature effect has\n    p < 0.05 and the mean difference at 21 degrees C exceeds that at 11 degrees C. The number of\n    experiments entering is reported.\n- id: fig1e-q10-lower-in-cs\n  statement: The Q10 of pyloric frequency was lower in Cs+ (1.3) than in saline (1.7), paired t-test\n    p < 0.001, N=21.\n  source: Results, The steady-state frequency increase, paragraph 3; Figure 1E\n  quote: The mean Q 10 of the pyloric frequency was significantly lower in Cs + (1.3±0.5) than in\n    control (1.7±0.3) ( Figure 1E )\n  statistics:\n  - test: paired Student's t-test\n    p: 0.001\n    p_relation: \"<\"\n    n: 21 experiments\n  expected:\n  - quantity: mean Q10 of frequency, saline\n    value: 1.7\n    tolerance: 0.3\n  - quantity: mean Q10 of frequency, Cs+\n    value: 1.3\n    tolerance: 0.5\n  criterion: Q10 per experiment and condition from the six holding-temperature mean frequencies,\n    under the readings of O1. Reproduced when, under one reading, both means are within tolerance\n    and a paired t-test gives p < 0.05 with Cs+ lower.\n- id: fig1f-two-saline-frequency-change-same\n  statement: In experiments with two consecutive saline step protocols, the frequency change from\n    11 to 21 degrees C did not differ between the first (0.9 Hz) and second (0.8 Hz) protocol.\n  source: Results, The steady-state frequency increase, paragraph 4; Figure 1F\n  quote: The mean difference in frequency between 21°C and 11°C for the first (0.9±0.3 Hz) and\n    second temperature changes (0.8±0.3 Hz) were not significantly different ( Figure 1F )\n  statistics:\n  - test: paired Student's t-test\n    p: 0.14\n    n: 6 experiments\n  expected:\n  - quantity: frequency change 11 to 21 degrees C, first saline protocol\n    value: 0.9\n    tolerance: 0.3\n    unit: Hz\n  - quantity: frequency change 11 to 21 degrees C, second saline protocol\n    value: 0.8\n    tolerance: 0.3\n    unit: Hz\n  criterion: A claim of absence. Per experiment and protocol, mean frequency within 0.3 degrees C of\n    21 degrees C minus that of 11 degrees C; a paired t-test over the 6 experiments, the paper's\n    test (Figure 1F legend). Reproduced when p >= 0.05, not reproduced when p < 0.05; the mean\n    difference is reported either way.\n- id: fig1e-two-saline-q10-same\n  statement: In the two-saline experiments the Q10 of the first protocol (2.0) did not differ from\n    that of the second (1.8).\n  source: Results, The steady-state frequency increase, paragraph 4; Figure 1E legend\n  quote: the mean Q 10 of the first temperature increase (2.0±0.4) was not significantly different\n    than the mean Q 10 of the second temperature increase (1.8±0.4)\n  statistics:\n  - test: paired Student's t-test\n    p: 0.14\n    n: 6 experiments\n  expected:\n  - quantity: mean Q10, first saline protocol\n    value: 2.0\n    tolerance: 0.4\n  - quantity: mean Q10, second saline protocol\n    value: 1.8\n    tolerance: 0.4\n  criterion: A claim of absence, judged on a paired t-test of the two Q10 values over the 6\n    experiments (Figure 1E legend). Q10 under the readings of O1; the absence is judged under each\n    and reported for all. Reproduced when p >= 0.05, not reproduced when p < 0.05.\n- id: fig1e-saline-q10-same-across-designs\n  statement: The saline Q10 did not differ between experiments with two saline protocols and those\n    with one saline and one Cs+ protocol.\n  source: Results, The steady-state frequency increase, paragraph 4; Figure 1E legend\n  quote: Q 10 was also not significantly different between the mean Q 10 of the experiments with two\n    saline temperature changes those that experienced one saline and one Cs + temperature change\n    (two-sample t-test, p=0.26)\n  statistics:\n  - test: two-sample t-test\n    p: 0.26\n    n: 6 two-saline and 21 saline and Cs+ experiments\n  criterion: A claim of absence, judged on a two-sample t-test. The legend's \"mean Q 10 of the\n    experiments with two saline temperature changes\" is read as each of the 6 experiments' mean of\n    its two saline Q10 values, against the 21 saline Q10 values; the first saline Q10 alone and the\n    12 pooled values are variants. Q10 under O1. Reproduced when p >= 0.05, not reproduced when\n    p < 0.05.\n- id: fig2c-decrease-by-depolarizing-phase\n  statement: In Cs+, the frequency decrease right after a temperature increase came from an\n    elongation of the PD depolarizing phase, with bursting and repolarization phases maintained.\n  source: Results, Cs+ revealed dynamic transitory frequency response, paragraph 1; Figure 2C; also\n    Figure 4G for Cs+ + PTX\n  quote: Alignment of each PD cycle during this window to the first PD spike reveals that the\n    decrease in frequency was due to elongation of the depolarizing phase and not the bursting,\n    repolarization, or inhibitory phases\n  criterion: The paper shows this in one example preparation, not identified, for the step from 13\n    toward 15 degrees C, and gives no measure. A measure is fixed here from the legend's phases. On\n    the intracellular PD trace, per cycle, burst duration (first to last spike), repolarization\n    (last spike to the voltage minimum), and depolarization (voltage minimum to the next first\n    spike). In each Cs+ experiment with intracellular PD, cycles of the 30 s before the 13 to 15\n    degrees C step are compared with the cycles of the first 30 s of warming in which the period\n    exceeds the pre-step mean. Reproduced when, in most such experiments, the depolarizing phase\n    accounts for more than half of the period increase. Partially reproduced when this holds in the\n    example-like experiments with the largest decrease only. Not testable without intracellular PD\n    traces.\n- id: fig3d-freq-decrease-while-warming\n  statement: Among temperature-increasing cycles, the percent with a frequency decrease was higher\n    in Cs+ (31.4%) than in saline (7.5%), and higher in Cs+ in 20 of 21 experiments.\n  source: Results, Cs+ revealed dynamic transitory frequency response, paragraph 2; Figure 3D\n  quote: In Cs + , the mean percent of temperature-increasing pyloric cycles in which the frequency\n    decreased (31.4±15%) was significantly higher than in control (7.5±5%) ( Figure 3D , paired\n    Student’s t-test, N=21, p<0.001)\n  statistics:\n  - test: paired Student's t-test\n    p: 0.001\n    p_relation: \"<\"\n    n: 21 experiments\n  expected:\n  - quantity: percent of temperature-increasing cycles with frequency decrease, Cs+\n    value: 31.4\n    tolerance: 15\n    unit: percent\n  - quantity: percent of temperature-increasing cycles with frequency decrease, saline\n    value: 7.5\n    tolerance: 5\n    unit: percent\n  - quantity: experiments with a higher percent in Cs+ than saline\n    value: 20\n    tolerance: 2\n    unit: of 21\n  criterion: The jag measure as the Methods fix it (header), under the readings of O3. Reproduced\n    when, under one reading, both means and the count are within tolerance and a paired t-test\n    gives p < 0.05 with Cs+ higher.\n- id: fig3e-freq-increase-when-stable\n  statement: Among temperature-stable cycles, the percent with a frequency increase was higher in\n    Cs+ (27.6%) than in saline (14.1%), and higher in Cs+ in 20 of 21 experiments.\n  source: Results, Cs+ revealed dynamic transitory frequency response, paragraph 2; Figure 3E\n  quote: In Cs + , the mean percent of temperature-stable cycles in which frequency increased in Cs +\n    (27.6±6%) was significantly higher than in control (14.1±5%) ( Figure 3E , paired Student’s\n    t-test, N=21, p<0.001)\n  statistics:\n  - test: paired Student's t-test\n    p: 0.001\n    p_relation: \"<\"\n    n: 21 experiments\n  expected:\n  - quantity: percent of temperature-stable cycles with frequency increase, Cs+\n    value: 27.6\n    tolerance: 6\n    unit: percent\n  - quantity: percent of temperature-stable cycles with frequency increase, saline\n    value: 14.1\n    tolerance: 5\n    unit: percent\n  - quantity: experiments with a higher percent in Cs+ than saline\n    value: 20\n    tolerance: 2\n    unit: of 21\n  criterion: As fig3d-freq-decrease-while-warming, for stable cycles and increases of more than\n    0.002 Hz per cycle.\n- id: fig4c-ptx-restores-frequency-change\n  statement: The frequency change from 11 to 21 degrees C differed by condition; it was smaller in\n    Cs+ than in saline or in Cs+ + PTX, with no difference between saline and Cs+ + PTX.\n  source: Results, In Cs+, follower neurons determined frequency-temperature sensitivity, paragraph\n    1; Figure 4C\n  quote: change in frequency in Cs + was significantly lower than in either control or Cs + +PTX (\n    Figure 4C ) with no significant difference between control and Cs + +PTX\n  statistics:\n  - test: one-way repeated measures ANOVA\n    statistic: F(2,10) = 12.272\n    p: 0.002\n    n: 6 experiments\n  - about: pairwise comparisons of conditions\n    test: post hoc Tukey's honestly significant difference\n    p: 0.05\n    p_relation: \"<\"\n  criterion: Per experiment and condition, mean frequency within 0.3 degrees C of 21 degrees C minus\n    that of 11 degrees C; a one-way repeated-measures ANOVA on condition over the 6 picrotoxin\n    experiments, then Tukey HSD under the readings of O5. Reproduced when, under one reading, the\n    condition effect has p < 0.05, Cs+ is significantly lower than both saline and Cs+ + PTX, and\n    saline against Cs+ + PTX is not significant (the paper's test, as a claim of absence).\n- id: fig4d-ptx-keeps-decrease-while-warming\n  statement: The percent of temperature-increasing cycles with a frequency decrease differed by\n    condition; it was higher in Cs+ and in Cs+ + PTX than in saline, with no difference between Cs+\n    and Cs+ + PTX.\n  source: Results, In Cs+, follower neurons determined frequency-temperature sensitivity, paragraph\n    2; Figure 4D\n  quote: The probability of frequency decrease while temperature increased was lower in control than\n    in either Cs + or Cs + +PTX ( Figure 4D ), with no difference between Cs + and Cs + +PTX\n  statistics:\n  - test: one-way repeated measures ANOVA\n    statistic: F(2,10) = 13.077\n    p: 0.002\n    n: 6 experiments\n  - about: pairwise comparisons of conditions\n    test: Tukey's honestly significant difference\n    p: 0.05\n    p_relation: \"<\"\n  criterion: The jag measure (header) under the readings of O3, per experiment and condition; a\n    one-way repeated-measures ANOVA on condition, then Tukey HSD under O5. Reproduced when, under\n    one reading, the condition effect has p < 0.05, both Cs+ conditions are significantly above\n    saline, and Cs+ against Cs+ + PTX is not significant.\n- id: fig4e-stable-increase-ordering\n  statement: The percent of temperature-stable cycles with a frequency increase differed between\n    all three conditions, lowest in saline, middle in Cs+ and highest in Cs+ + PTX.\n  source: Results, In Cs+, follower neurons determined frequency-temperature sensitivity, paragraph\n    2; Figure 4E\n  quote: the probability of frequency increase while temperature was stable was significantly\n    different between all three conditions... control was lowest, Cs + was in the middle, and Cs +\n    +PTX was greatest\n  statistics:\n  - test: one-way repeated measures ANOVA\n    statistic: F(2,10) = 69.572\n    p: 0.001\n    p_relation: \"<\"\n    n: 6 experiments\n  - about: pairwise comparisons of conditions\n    test: Tukey's honestly significant difference\n    p: 0.05\n    p_relation: \"<\"\n  criterion: As fig4d-ptx-keeps-decrease-while-warming, for stable cycles with an increase. The\n    legend names the Cs+ against saline and Cs+ + PTX against Cs+ comparisons; the Results say all\n    three differ. Reproduced when, under one reading, the condition effect has p < 0.05, the means\n    are ordered saline < Cs+ < Cs+ + PTX, and all three pairs are significant; partially reproduced\n    when the two pairs the legend names are significant and saline against Cs+ + PTX also is, but\n    the ordering is not as stated, or when two of the three pairs are significant with the stated\n    ordering.\n- id: fig5b-pd-burst-shorter\n  statement: At 11 degrees C the PD burst was modestly shorter in Cs+ (144 ms) than in saline\n    (164 ms).\n  source: Results, Phase of PD and LP advanced in Cs+, paragraph 1; Figure 5B\n  quote: The time of PD bursting was significantly but modestly shorter in Cs + ( Figure 5B ,\n    saline ... 164±34 ms, Cs + ... 144±18 ms)\n  statistics:\n  - test: Wilcoxon signed-rank test\n    p: 0.019\n    n: 21 experiments\n  expected:\n  - quantity: PD burst duration at 11 degrees C, saline\n    value: 164\n    tolerance: 34\n    unit: ms\n  - quantity: PD burst duration at 11 degrees C, Cs+\n    value: 144\n    tolerance: 18\n    unit: ms\n  criterion: PD burst duration is first to last spike of the burst; per experiment the mean over the\n    11 degrees C cycles under O2 and O4. Reproduced when both means are within tolerance and a\n    Wilcoxon signed-rank test gives p < 0.05 with Cs+ shorter.\n- id: table1-pd-off-advanced\n  statement: At 11 degrees C, PD OFF phase was advanced in Cs+ (0.12) compared with saline (0.19).\n  source: Results, Phase of PD and LP advanced in Cs+, paragraph 1; Table 1; Figure 5C\n  quote: the phase of PD OFF (percentage of period at which PD stops firing) was significantly\n    advanced in Cs + compared to control\n  statistics:\n  - test: paired Student's t-test\n    p: 0.001\n    p_relation: \"<\"\n    n: 21 experiments\n  expected:\n  - quantity: PD OFF phase at 11 degrees C, saline\n    value: 0.19\n    tolerance: 0.04\n  - quantity: PD OFF phase at 11 degrees C, Cs+\n    value: 0.12\n    tolerance: 0.03\n  criterion: Phase as the Methods define it, per experiment the mean over 11 degrees C cycles under\n    O2 and O4, onsets and offsets as O6. Reproduced when, under one reading, both means are within\n    tolerance and a paired t-test (Table 1, T) gives p < 0.05 with Cs+ lower.\n- id: table1-lp-on-advanced\n  statement: At 11 degrees C, LP ON phase was advanced in Cs+ (0.29) compared with saline (0.40).\n  source: Results, Phase of PD and LP advanced in Cs+, paragraph 1; Table 1; Figure 5C\n  quote: LP onset, which follows PD offset, was also phase advanced in Cs + conditions compared to\n    control\n  statistics:\n  - test: paired Student's t-test\n    p: 0.001\n    p_relation: \"<\"\n    n: 21 experiments\n  expected:\n  - quantity: LP ON phase at 11 degrees C, saline\n    value: 0.40\n    tolerance: 0.05\n  - quantity: LP ON phase at 11 degrees C, Cs+\n    value: 0.29\n    tolerance: 0.05\n  criterion: As table1-pd-off-advanced, for LP onset.\n- id: table1-lp-off-advanced\n  statement: At 11 degrees C, LP OFF phase was advanced in Cs+ (0.56) compared with saline (0.66).\n  source: Results, Phase of PD and LP advanced in Cs+, paragraph 2; Table 1; Figure 5C\n  quote: LP OFF was also significantly advanced in Cs +\n  statistics:\n  - test: paired Student's t-test\n    p: 0.001\n    p_relation: \"<\"\n    n: 21 experiments\n  expected:\n  - quantity: LP OFF phase at 11 degrees C, saline\n    value: 0.66\n    tolerance: 0.05\n  - quantity: LP OFF phase at 11 degrees C, Cs+\n    value: 0.56\n    tolerance: 0.06\n  criterion: As table1-pd-off-advanced, for LP offset.\n- id: table1-py-phase-unchanged\n  statement: At 11 degrees C, PY ON (0.58 against 0.60) and PY OFF (0.87 against 0.90) phases did\n    not differ between saline and Cs+.\n  source: Results, Phase of PD and LP advanced in Cs+, paragraph 2; Table 1\n  quote: PY ON and PY OFF were not significantly different between Cs + and control\n  statistics:\n  - about: PY ON\n    test: paired Student's t-test\n    p: 0.86\n    n: 12 experiments\n  - about: PY OFF\n    test: Wilcoxon signed-rank test\n    p: 0.91\n    n: 12 experiments\n  expected:\n  - quantity: PY ON phase at 11 degrees C, saline\n    value: 0.58\n    tolerance: 0.11\n  - quantity: PY ON phase at 11 degrees C, Cs+\n    value: 0.60\n    tolerance: 0.11\n  - quantity: PY OFF phase at 11 degrees C, saline\n    value: 0.87\n    tolerance: 0.20\n  - quantity: PY OFF phase at 11 degrees C, Cs+\n    value: 0.90\n    tolerance: 0.19\n  criterion: A claim of absence, judged on the paper's tests (Table 1), a paired t-test for PY ON\n    and a Wilcoxon signed-rank test for PY OFF over the 12 experiments with PY. Phases as\n    table1-pd-off-advanced. Reproduced when both give p >= 0.05; not reproduced when either gives\n    p < 0.05; the mean differences are reported either way.\n- id: fig5d-pdoff-lpon-delay-smaller\n  statement: The phase delay between PD OFF and LP ON was smaller in Cs+ (0.17) than in saline\n    (0.21), so LP ON advanced more than the PD OFF advance explains.\n  source: Results, Phase of PD and LP advanced in Cs+, paragraph 1; Figure 5D\n  quote: the delay between PD OFF and LP ON phase was significantly smaller in Cs + compared to\n    control ( Figure 5D , saline ... 0.21±0.06, Cs + ... 0.17±0.04)\n  statistics:\n  - test: paired Student's t-test\n    p: 0.0048\n    n: 21 experiments\n  expected:\n  - quantity: LP ON minus PD OFF phase at 11 degrees C, saline\n    value: 0.21\n    tolerance: 0.06\n  - quantity: LP ON minus PD OFF phase at 11 degrees C, Cs+\n    value: 0.17\n    tolerance: 0.04\n  criterion: Per experiment, the mean of LP ON phase minus PD OFF phase over 11 degrees C cycles\n    (O2, O4; the difference of the two means is a variant). Reproduced when both means are within\n    tolerance and a paired t-test gives p < 0.05 with Cs+ smaller.\n- id: lp-duty-cycle-preserved\n  statement: LP duty cycle did not differ between saline and Cs+ at 11 degrees C.\n  source: Results, Phase of PD and LP advanced in Cs+, paragraph 2\n  quote: LP OFF was also significantly advanced in Cs + , and subsequently duty cycle (percent of the\n    period a neuron is firing) was preserved (paired Student’s t-test, N=21, p=0.448)\n  statistics:\n  - test: paired Student's t-test\n    p: 0.448\n    n: 21 experiments\n  criterion: A claim of absence. LP duty cycle per cycle is (last LP spike minus first LP spike) over\n    the period, the mean over 11 degrees C cycles (O2, O4). A paired t-test over 21 experiments, the\n    paper's test. Reproduced when p >= 0.05, not reproduced when p < 0.05; the mean difference is\n    reported either way.\n- id: matched-period-lp-earlier\n  statement: In cycles of matched period between saline at 11 degrees C and Cs+, PD bursts were\n    51 ms shorter in Cs+ while LP fired 91 ms earlier and PY latency did not change (1.9 ms), and\n    the PD offset advance did not correlate with the LP onset advance.\n  source: Results, Phase of PD and LP advanced in Cs+, paragraph 3\n  quote: Although PD burst duration was only 51±30 ms shorter in Cs + , LP fired 91±68 ms earlier.\n    Conversely, PY latency did not change in these matched frequency samples (1.9±100 ms earlier).\n    There was no correlation between how advanced PD’s offset was between control and Cs +\n    conditions and how much LP’s onset advanced in these matched period samples (Pearson\n    correlation; r(21)=0.26, p=0.2928)\n  statistics:\n  - about: correlation of PD offset advance with LP onset advance\n    test: Pearson correlation\n    statistic: r(21) = 0.26\n    p: 0.2928\n  expected:\n  - quantity: PD burst duration shortening in Cs+, matched period\n    value: 51\n    tolerance: 30\n    unit: ms\n  - quantity: LP onset latency advance in Cs+, matched period\n    value: 91\n    tolerance: 68\n    unit: ms\n  - quantity: PY onset latency advance in Cs+, matched period\n    value: 1.9\n    tolerance: 100\n    unit: ms\n  criterion: The paper does not say how periods were matched. Readings are (a) per experiment, the\n    Cs+ holding temperature whose mean period is nearest the saline 11 degrees C mean period, with\n    latencies and durations as means over those holds; (b) per experiment, Cs+ cycles whose period\n    is within 2% of the saline 11 degrees C mean period (a standard choice, the paper gives no\n    bound). Latencies are from the first PD spike to the first LP or PY spike (O6); advance is\n    saline minus Cs+. Reproduced when, under one reading, the three means are within tolerance, LP\n    advance exceeds PD shortening, and the Pearson correlation across experiments of PD offset\n    advance (ms) with LP onset advance (ms) has p >= 0.05 (a claim of absence, the paper's test).\n    The printed r(21) implies 23 pairs by the degrees-of-freedom convention, while r = 0.26 with\n    p = 0.2928 fits about 18 pairs; the number of pairs used is reported.\n- id: fig6a-lp-off-advances-saline\n  statement: In saline, LP OFF phase advanced modestly with temperature, by 0.07 per 10 degrees C;\n    all other phases were constant.\n  source: Results, Phase constancy with increasing temperature was reduced by Cs+, paragraph 1;\n    Figure 6A and 6B\n  quote: In control conditions, LP OFF modestly advanced with temperature, with a mean advance of\n    0.07±0.07 per 10°C (Wilcoxon signed-rank test, N=21, p<0.01)\n  statistics:\n  - test: Wilcoxon signed-rank test\n    p: 0.01\n    p_relation: \"<\"\n    corrected: Bonferroni, 10 tests\n    n: 21 experiments\n  expected:\n  - quantity: LP OFF phase advance per 10 degrees C, saline (minus the fitted slope times 10)\n    value: 0.07\n    tolerance: 0.07\n  criterion: Per experiment, a line of phase on temperature under O4; slope per 10 degrees C, an\n    advance being a negative slope. Wilcoxon signed-rank test against zero over 21 experiments,\n    p multiplied by 10 (Bonferroni, Methods). Reproduced when, under one reading, the mean advance\n    is within tolerance and the adjusted p < 0.01, with the slope negative.\n- id: fig6a-lp-advances-cs\n  statement: In Cs+, LP ON and LP OFF advanced with temperature, by 0.05 and 0.14 per 10 degrees C.\n  source: Results, Phase constancy with increasing temperature was reduced by Cs+, paragraph 2;\n    Figure 6A and 6C\n  quote: In Cs + , LP ON and LP OFF advanced with temperature, with a mean advance of 0.05±0.05 per\n    10°C and 0.14±0.09 per 10°C respectively (Wilcoxon signed-rank test, N=21, p<0.01)\n  statistics:\n  - test: Wilcoxon signed-rank test\n    p: 0.01\n    p_relation: \"<\"\n    corrected: Bonferroni, 10 tests\n    n: 21 experiments\n  expected:\n  - quantity: LP ON phase advance per 10 degrees C, Cs+\n    value: 0.05\n    tolerance: 0.05\n  - quantity: LP OFF phase advance per 10 degrees C, Cs+\n    value: 0.14\n    tolerance: 0.09\n  criterion: As fig6a-lp-off-advances-saline, for LP ON and LP OFF in Cs+. Reproduced when both\n    hold; partially reproduced when one does.\n- id: fig6a-pd-py-phase-constant\n  statement: PD and PY phases were constant with temperature in both saline and Cs+.\n  source: Results, Phase constancy with increasing temperature was reduced by Cs+, paragraph 2;\n    Figure 6A\n  quote: PD and PY phase constancy was not significantly altered in either condition\n  criterion: A claim of absence, on the paper's test. For PD OFF, PY ON and PY OFF in each\n    condition (6 tests; N=21 for PD, 12 for PY), the slope of phase on temperature (O4) tested\n    against zero by Wilcoxon signed-rank or one-sample t-test as Shapiro-Wilk on the slopes\n    decides, p multiplied by 10. Reproduced when none has adjusted p < 0.05; not reproduced when\n    any does, naming it. LP ON in saline, which the Results also count as constant, is reported\n    the same way. Mean slopes are reported either way.\n"
}
```

```
File created successfully at: claims/schapiro-2024.yaml (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
python tools/claims_check.py claims/schapiro-2024.yaml paper/10.7554-elife.98844.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
grep -n -i "rather\|—" claims/schapiro-2024.yaml; python -c "import yaml;yaml.safe_load(open('claims/schapiro-2024.yaml'))" && echo ok; git status --short
```

```
ok
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
?? claims/schapiro-2024.yaml
?? scripts
```

**Agent**

I wrote `claims/schapiro-2024.yaml`, and the quote checker passes it: 25 claims, 25 quotes, 27 statistical values, 0 problems.

**Text read.** The eLife version of record, from Europe PMC (PMC11479588, open-access JATS). It has the Results, Discussion, Methods, the Figure 1 to 6 legends, Table 1, and Figure 1–figure supplement 1, which is the paper's only supplement. Nothing the claims needed was missing, and I didn't open the PDF.

**Code.** The paper says its analysis code is deposited inside the Dryad dataset. That makes it one of the dataset's files, so I didn't read it and no commit is recorded. The paper also links Crabsort, its spike-sorting software; I read it at commit ee237ea, and it fixes none of the measures.

**Claims.** All 25 have quotes, none is inferred, 25 have criteria and 24 have statistics. They cover:
- Ih reduction at 11 and 21 °C.
- Frequency at 11 °C, the saline minus Cs+ difference growing with temperature, and the lower Q10 in Cs+.
- Three controls with two saline runs, which are absence claims.
- The example where the depolarizing phase lengthens.
- The percentages of frequency falling during warming and rising during stable temperature.
- The three picrotoxin ANOVAs.
- PD burst duration and the Table 1 phases (PY unchanged is an absence claim).
- The delay from PD OFF to LP ON, and LP duty cycle (an absence claim).
- Period-matched latencies with their correlation.
- Phase slopes with temperature.

**Details the paper leaves open, with the readings named:**
- **Q10:** the paper only says "as described previously". Readings are (a) a nonlinear exponential fit, (b) a straight line through log frequency, or (c) the ratio of frequencies at 21 and 11 °C.
- **Which 11 °C hold:** the first hold of each condition is the main reading; the return to 11 °C after 21 °C is a variant.
- **Smoothing for the frequency "jag" measure:** a centred moving average is the main reading and a trailing one a variant. The span is either the step protocol only or the whole recording with cooling counted as stable.
- **Which cycles make up a phase at a temperature:** either cycles within 0.3 °C of the target or the whole holding period. The slope is either a line through the per-temperature means or through all cycles.
- **Tukey's test after the repeated-measures ANOVA:** MATLAB's `multcompare` on the repeated-measures model, or the classic Tukey test on the ANOVA's error term.
- **LP and PY onset and offset:** first and last spike within each PD cycle, used as a standard choice.
- **Ih windows:** the paper doesn't say over which times the initial and steady-state currents are taken; two readings are named.
- **Period matching:** either the Cs+ hold nearest in period, or cycles within 2% of the period (the 2% is my standard choice).
- **Depolarizing-phase claim (Figure 2C):** the paper shows only an example and defines no measure, so I set one from the phases the legend names.

**Inconsistencies in the paper, recorded in the criteria:**
- Figure 1D reports F(5,85) with N=21, but those degrees of freedom imply 18 experiments. Both readings are named.
- The period-matched correlation, r(21)=0.26 with p=0.2928, doesn't match the stated number of pairs. The author is to report how many pairs were used.

**Also unstated:** whether the 6 picrotoxin experiments are among the 21.

Tolerances are the paper's stated SDs, as the protocol directs, which makes them loose for some means; counts use 10%.

## End of run

17 turns, 4 minutes, $1.38 at API prices, result: success.
