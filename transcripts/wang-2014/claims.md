# wang-2014 · claims · run 42689411219

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  grep -n "^#" docs/protocol.md | head -50; ls paper/; ls claims | head; wc -l paper/*
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "docs/protocol.md",
 "limit": 195
}
```

```
1	# Protocol for an attempt
2	
3	Version: `pilot-14`. Record this version in the attempt's provenance.
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
[... 175 more lines not kept]
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

**Agent calls Read**

```json
{
 "file_path": "paper/10.1038-nn.3904.txt"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1038-nn.3904.txt",
 "offset": 1147,
 "limit": 900
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  head -80 paper/hc-5.data-description.txt; cat papers/datasets/wang-2014.yaml 2>/dev/null; grep -n "wang-2014" -r papers/keys.yaml | head; grep -in "github\|code avail\|software" paper/10.1038-nn.3904.txt | head
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  sed -n 80,286p paper/hc-5.data-description.txt | grep -in -B2 -A2 "muscimol\|inject\|saline\|wheel\|platform\|novel\|i01_maze1" | head -60; ls claims | wc -l; sed -n 1,40p tools/claims_check.py
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  grep -l "archive: crcns" claims/*.yaml | head -3; f=$(grep -l "archive: crcns" claims/*.yaml | head -1); sed -n 1,40p $f; grep -n "kind\|data:" schemas/claims.schema.json | head -30
```

```
claims/bruno-2017.yaml
claims/deweese-2004.yaml
claims/eyherabide-2008.yaml
# Claims for Bruno, Frost & Humphries (2017), eLife 6:e27342, "A spiral attractor network drives
# rhythmic locomotion", doi:10.7554/elife.27342, on CRCNS data set apl-1 (doi:10.6080/K0SN074B).
# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"), 2026-11-08,
# protocol as stated in docs/protocol.md (Reader), version pilot-13.
#
# Text read: the version of record (PMC5546814, open access), as JATS XML flattened to text under
# paper/: main text, Materials and methods, and the legends of Figures 1 to 8 and of all twelve
# figure supplements. The paper has no other supplementary file. No PDF of the paper was supplied,
# and none was needed: no claim rests on a number shown only in a figure. The extraction garbles
# some formulas: the Gaussian width reads "σ = {median ISI in population}/12" (a square root may be
# lost) and the rotation period reads "ω = 2πbΔt"; the code settles the second (see below).
# The data set's description (paper/apl-1.data-description.txt) was read only to know what it
# holds; no claim comes from it.
#
# Code read: https://github.com/mdhumphries/AplysiaAttractorAnalysis, commit e5f28e98 (2018-07-11),
# MATLAB, linked from the paper's Data and code availability. Analysis/DataSet_Properties.m builds
# the spike-density functions and the PCA; Analysis/Classify_attractors/ holds the recurrence
[... 28 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 40,120p claims/bruno-2017.yaml; python -c "
import json;s=json.load(open('schemas/claims.schema.json'));print(json.dumps(s,indent=0)[:5000])"
```

```
# eigenvalue.
#
# Places where the code and the Methods differ, each named again in the claims it touches:
# (1) the Gaussian SD: the Methods give the median ISI divided by 12 (or its square root, if the
# extraction lost it); the code uses the median ISI itself, and computes it from the post-onset
# ISIs of all recordings of the same stimulation number read so far, not of the recording alone;
# (2) the number of PCs: the Methods say at least 80% of variance; the recurrence code keeps the
# PCs whose cumulative variance is at most 80% (sum(prctVar <= 0.8)), the manifold code the
# smallest number reaching at least 80%; (3) the dominant period: the Methods and Figure 2F say
# the mean recurrence time of the dominant peak, the code stores and plots the median;
# (4) P10 decoding: the Methods fit 40 s windows stepped by 1 s with histories 50 to 200 ms; the
# code trains on 50% of the post-33 s series, steps 0.2 s, and tries histories 50 to 250 ms;
# (5) the period-change permutation test: 10000 permutations in the Methods, 100000 in the code,
# which permutes the pooled time and period values and is one-sided in the direction of rho.
# Following the protocol, the Methods are the main reading and the code's choice is a variant.
#
# Data the paper used. Aplysia californica, isolated cerebral, pleural and pedal ganglia (15 to
# 17 C). Voltage-sensitive dye RH-155 imaged with a 464-element photodiode array at 1600 Hz over
# the dorsal pedal ganglion, bandpassed 5 to 100 Hz and spike-sorted by independent component
# analysis. 10 preparations, three evoked bouts of fictive locomotion each (30 evoked population
[... 271 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python -c "
import json;s=json.load(open('schemas/claims.schema.json'));print(json.dumps(s['\$defs'],indent=0))" | head -120
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
cd  grep -n -B3 -A8 "model simulation\|simulat" claims/*.yaml | grep -n "data:\|criterion\|inferred" | head -20
```

```
53:claims/athalye-2023.yaml:1013:  criterion: Simulation as in Methods, Optimal feedback control model and simulation. Per session,
85:claims/athalye-2023.yaml:1095:  criterion: On the simulations of fig6c and fig6d, commands discretized and tuples of 15 or more
104:claims/athalye-2023.yaml-1142-  - fig6g-ofc-uses-distinct-patterns, added the Table S2 statistics for the decoder-null comparison's own No Dynamics Model against shuffle (Figure 6H, z = 0.611 and 0.449), and the criterion now requires that absence too and the per-session Mann-Whitney absences of the legends.
106:claims/athalye-2023.yaml-1144-  - figs1d-command-subtrajectories-differ, the criterion now says why the Statistics Summary's "behavior-preserving shuffle" for Figures S1D and S1E is not used (that shuffle leaves commands unchanged); the Methods and the legend give subsampling of the matched pool.
166:claims/buccino-2020.yaml-96-  criterion: Each of the five files named in the opening comment is present, and a recording of mouse
180:claims/buccino-2020.yaml-195-  criterion: 'Sorters, agreement graph and k as in the opening comment. Two details are open. The recording:
216:claims/buccino-2020.yaml-252-  criterion: Sorters as in the opening comment, with the same parameters as on the real recording, on
229:claims/buccino-2020.yaml-265-  criterion: Precision and recall per ground-truth unit from the ground-truth comparison of the opening
241:claims/buccino-2020.yaml-283-  criterion: Accuracy per ground-truth unit as in fig2s1a-precision-recall-bias; ground-truth SNR as in
253:claims/buccino-2020.yaml-301-  criterion: 'Scores per ground-truth unit as in fig2s1a-precision-recall-bias. The paper reports no test
293:claims/buccino-2020.yaml-380-  criterion: Unit classes as in fig2e-ks2-unit-types. Reproduced when HDSort's false positive count is
342:claims/buccino-2024.yaml-234-  data: elsewhere
344:claims/buccino-2024.yaml-236-  criterion: The ground-truth template (repository fitting/extracellular/temp
[... 7 more lines not kept]
```

**Agent**

Next I'm checking the Supplementary Fig. 12f figure for where the periphery border sits, since no text gives it. I'm also checking Fig. 4b's P value against the text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1038-nn.3904.supp.pdf",
 "pages": "28"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1038-nn.3904.pdf",
 "pages": "2-4"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd $TMPDIR && python -c "
import fitz
d=fitz.open('paper/10.1038-nn.3904.supp.pdf'); p=d[27]; p.get_pixmap(dpi=110).save('s28.png')
d=fitz.open('paper/10.1038-nn.3904.pdf'); d[3].get_pixmap(dpi=110).save('m4.png'); d[1].get_pixmap(dpi=110).save('m2.png')
" && ls
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  sed -n 870,900p claims/dehaqani-2024.yaml; grep -rn "no recorded data\|uses no data\|model only" claims/*.yaml | head -5
```

```
criterion: A claim of absence. Concentration coefficients of the two populations of
    fig5gh-mechanosensitive-as-good (all neurons meeting each rule); two-sample
    Kolmogorov-Smirnov test; reproduced when p >= 0.05, not reproduced otherwise.
- id: fig6-simulation-mechanosensory-rescues
  statement: In a population simulated from the fitted coefficients, an inhalation-driven
    concentration change makes concentration decoding across inhalation speeds worse than within
    speed as the change grows, and adding the mechanosensory input restores decoding of the true
    concentration for any change.
  source: Results, Airflow information affords tolerance to flow-dependent concentration
    fluctuations, paragraph 1; Figures 6B and 6C; STAR Methods, Simulation of sniff-induced
    concentration changes
  quote: Consistently, decoders trained on the responses during slow and fast inhalations
    classified the odor concentration worse than decoders trained using only one inhalation speed
    as the simulated influence of the airflow on the concentration increased (Figure 6C).
    However, supplementing this population with mechanosensory responses was sufficient to reduce
    ambiguity and retrieve the actual concentration for any DIC (Figures 6B and 6C).
  depends_on:
  - fig5ef-correlated-subpopulations
  criterion: Simulated per STAR Methods, R = Poisson(a I + b Cn) with Cn = log(Ce + k I Ce), Ce
    0.01, 0.1, 1%, k from 0 to 1, a and b the linear-model coefficients of
[... 16 more lines not kept]
```

**Agent**

The paper is complete: the version of record with its Online Methods and supplement, and it links no code. I'm writing the claims file now.

**Agent calls Write**

```json
{
 "file_path": "claims/wang-2014.yaml",
 "content": "# Claims for Wang, Romani, Lustig, Leonardo & Pastalkova (2015), Nature Neuroscience 18, 282-288,\n# \"Theta sequences are essential for internally generated hippocampal firing fields\",\n# doi:10.1038/nn.3904, on CRCNS data set hc-5.\n# Written by an agent (model \"claude-opus-5-5\", Claude Code, runner \"GitHub Actions\"), 2026-11-09,\n# protocol as stated in docs/protocol.md (Reader), version pilot-14.\n#\n# Text read: the version of record (paper/10.1038-nn.3904.txt, extracted from the publisher PDF),\n# with its main text, figure legends, Online Methods, and the Supplementary Information PDF\n# (Supplementary Modeling, Supplementary Table 1, legends of Supplementary Figures 1 to 17). The\n# figures were not rendered (no PDF renderer in this run); the figure text the extraction keeps\n# (axis labels, P values printed on panels) was read from the text file. Where a panel's printed P\n# differs from the Results, the claim says so. The paper links no analysis or model code, so no\n# code was read. The data set's description (paper/hc-5.data-description.txt) was read only to\n# know what it holds: one rat (i01) recorded with silicon probes in left and right CA1 and right\n# entorhinal cortex, in sessions of the left/right alternation task with wheel runs, home-cage\n# wheel running and large 2D platform exploration; it names this paper among three that used\n# these data. It does not mention injections. Whether its sessions are the paper's pre, muscimol\n# and post sessions is the author's to find. No claim comes from it.\n#\n# Data the paper used (Online Methods; Results). Male Long-Evans rats, two 64-channel silicon\n# probes in dorsal CA1 of both hemispheres, a guide cannula above the medial septum (MS); 20 kHz\n# wideband, LED tracked by an overhead camera at 30 Hz. (1) Alternation task: 3 rats in a\n# two-arm maze (arms 150 cm long, 25 cm wide) with a running wheel in the delay area behind two\n# doors; doors open after 9 (rat 1) or 10 s (rats 2, 3) of running, the counter resetting if speed\n# falls below 18.5 cm/s; reward for left-right alternation. A muscimol recording has a pre session\n# (25-30 trials), a muscimol session (from about 20 min after 500 nl muscimol 0.125 mg/ml into\n# MS, over 40 trials) and a post session (about 4 h after, 25-30 trials); saline controls. The text\n# gives 15 muscimol and 7 control recordings; Figure 1 and most legends give 13 muscimol\n# recordings from 3 animals, Supplementary Figure 1 7 saline recordings from 2 animals. 158 wheel\n# neurons and 160 maze neurons with firing fields. (2) Novel linear track (150 x 150 cm, 25-30 cm\n# wide): muscimol 290 neurons from 2 animals, control 136 neurons from 2 animals. (3) Large novel\n# platform (150 x 150 cm, walls), muscimol or saline, about 1 h, post session about 6 h after;\n# counts differ between text and legends (claim fig5c-platform-info). (4) Smaller platform, 223\n# neurons from 2 animals. (5) Repeated visits of the same large platform on days 1 to 3 under\n# muscimol, each followed by a post-muscimol visit, then 3 days of familiarization and a\n# muscimol visit (39 to 75 neurons from 3 animals). Spikes sorted with KlustaKwik on the merged\n# pre, muscimol and post sessions, so a unit is the same across sessions of a day.\n#\n# Methods common to the claims, from the Online Methods unless said otherwise; each criterion\n# refers to these by name.\n# - Wheel runs: each aligned to the start of the 9 or 10 s of running before the doors open;\n#   runs before left and before right arm choices analysed separately. Maze runs: from entering\n#   the straight part of an arm to arrival at the water port; outbound and inbound separately.\n# - Episode fields (Episode cell firing fields; Supplementary Fig. 17a): spikes at 1,250 Hz\n#   referenced to run onset, smoothed with a Gaussian (s.d. 75 ms), averaged over trials. Keep\n#   neurons with mean rate FRm >= 0.1 Hz and a peak-to-mean ratio against Thp2m = 3; segments at\n#   or above FRm*Thp2m; edges where the rate falls below Thh = 0.9 FRm and Thl = 0.3 FRm; a field\n#   spans the two Thl crossings when the margin between the Thh and Thl crossings is small; it\n#   needs at least two spikes per trial on average, a size of at most 4 s and spikes in at least\n#   40% of trials. Place fields in the maze use the same detection on the rate profile in time.\n#   Open: (i) the Methods print \"FRp2m <= Thp2m\"; with that sign no rate could exceed FRm*Thp2m\n#   (except at equality), so the ratio is read as FRp2m >= 3; (ii) \"small\" for the margin is not\n#   given; readings at most 0.5 s and at most 1 s; (iii) the paper adjusted some parameters by\n#   visual inspection, which cannot be repeated; the default values are used and this is a\n#   deviation. A field sequence orders neurons by the latency Tc of the field centre, from the\n#   pre session (the largest-peak field when several), else from the post session.\n#   \"Excitatory neurons\" are not defined; readings: the data set's own cell-type labels if it\n#   has them, otherwise all units (the paper's selection rests on firing fields).\n# - Maze spatial maps: position at each spike, Gaussian smoothing (s.d. 17.5 camera pixels),\n#   divided by occupancy.\n# - Open-field maps (platform and, as one reading, the linear track): spike and occupancy maps,\n#   smoothed by adaptive binning (ref. 54, Markus et al. 1995). Units kept with mean rate > 0.4\n#   and < 5 Hz, refractory violation < 0.3, Mahalanobis distance from the noise cluster > 10 and\n#   minimal spike amplitude 200 uV, with or without a clear field. Open: the spatial bin and the\n#   adaptive-binning constant; readings 2.5 cm and 5 cm bins, the constant of ref. 54 and half and\n#   double it. The units of \"refractory violation < 0.3\" are not given; readings: 0.3% and a\n#   fraction 0.3 of interspike intervals under 2 ms.\n# - Firing field information: I = sum over bins of lambda(x)/lambda log2(lambda(x)/lambda) p(x)\n#   (ref. 55), on the episode profile over time or the place map over distance. The time bin of\n#   the wheel profile is open; readings: the smoothed profile at 1,250 Hz samples, and 75 ms bins.\n# - Theta modulation: spikes convolved with a Gaussian (s.d. 1 ms), autocorrelogram, Thomson\n#   multitaper spectrum (NW = 4), power 6-9 Hz over power 5-40 Hz. The autocorrelogram's span is\n#   not given; readings +/-0.5 s and +/-1 s.\n# - Theta phase: one CA1 pyramidal-layer LFP channel, second-order Chebyshev type II filter 4-25\n#   Hz, peaks 0 deg, troughs 180 deg, zero crossings 90 or 270 deg, linear interpolation between.\n# - Theta sequence detection (Fig. 2e,j; Supplementary Fig. 17b): recordings with more than eight\n#   episode or place cells; windows of the session's mean theta cycle length, stepped by 25 ms;\n#   windows with mean speed above 18.5 cm/s (wheel) or 30 cm/s (maze) and at least two active\n#   field neurons. Score: over all pairs of spikes in the window, +1 when their order matches the\n#   field sequence, -1 otherwise. Shuffle: reassign each spike to a neuron active in the window,\n#   keeping spike times and the number of active neurons, 10,000 times; a window is significant\n#   when its score exceeds 95% of its shuffles; it is qualified when the best ordering of its\n#   spikes could reach that level. Percentage of significant sequences = significant / qualified.\n#   Chance: the same percentage per shuffle across windows; the figure's chance level is the 95th\n#   percentile over all recordings. Recordings kept when a control session (pre or post) beats\n#   chance, each session has more than 100 qualified windows, and the ratio of qualified fractions\n#   between sessions of a day is at most 7. Open: pairs of spikes from the same neuron and pairs\n#   at equal times; standard choice, scored 0.\n# - Statistics: the Methods name the Wilcoxon signed-rank test (WSR), Spearman correlation and the\n#   Kolmogorov-Smirnov test, and say \"All of our tests were one sided.\" The Results also use\n#   Kruskal-Wallis tests, and Supplementary Figures 11, 12 and 15 the Wilcoxon rank-sum test.\n#   Every test below is one-sided in the stated direction unless said otherwise.\n# - The muscimol period: Fig. 2a counts trials \"during the effect\", and Supplementary Fig. 3b\n#   excluded trials before a late onset of the effect, without a rule. Readings: (a) all trials of\n#   the muscimol session; (b) muscimol-session trials from the first one whose normalized theta\n#   power (fig1d-theta-power) is below the lowest pre-session trial, a rule fixed here because the\n#   paper gives none.\n#\n# Not made into claims: Supplementary Figure 2 (relation of firing to time, distance and theta\n# cycles on the wheel), which the Results cite only for the cell count and state no finding from;\n# the saline controls of Supplementary Figures 1c, 4b,c and 7, of which the Results state no\n# finding; the 2D model of Supplementary Figure 10a and the depression-model comparison of\n# Supplementary Figure 10d-g.\nschema_version: 2\npaper: doi:10.1038/nn.3904\nclaims:\n- id: cells-per-recording\n  statement: On average per recording the paper isolated 42.8, 15 and 16.38 episode cells and\n    19.6, 11 and 10.33 place cells in rats 1, 2 and 3.\n  source: Online Methods, Episode cell firing fields, paragraph 2; Firing fields of place cells in\n    the alternation task\n  quote: 'On average, we isolated the following number of episode cells per recording: rat 1, 42.8;\n    rat 2, 15; rat 3, 16.38 ... On average, we isolated the following number of place cells per\n    recording: rat 1, 19.6; rat 2, 11; rat 3, 10.33'\n  expected:\n  - quantity: episode cells per recording, rat 1\n    value: 42.8\n    tolerance: 4.28\n  - quantity: episode cells per recording, rat 2\n    value: 15\n    tolerance: 1.5\n  - quantity: episode cells per recording, rat 3\n    value: 16.38\n    tolerance: 1.64\n  - quantity: place cells per recording, rat 1\n    value: 19.6\n    tolerance: 1.96\n  - quantity: place cells per recording, rat 2\n    value: 11\n    tolerance: 1.1\n  - quantity: place cells per recording, rat 3\n    value: 10.33\n    tolerance: 1.03\n  criterion: Cells counted with the episode-field and place-field detection of the opening\n    comment, in the pre or post session, averaged over the alternation-task recordings of a rat.\n    The paper does not say which rat is which, so the claim holds when the data set's rat\n    matches both counts of any one of the three rats. Open, with readings run each - (a) a neuron\n    counts once when it has a field before left or right runs (or on any maze trajectory); (b)\n    each neuron-and-trajectory pair counts. A deviation if the default detection parameters are\n    used (the paper adjusted some by eye).\n- id: fig1d-theta-power\n  statement: Muscimol in the medial septum reduced the amplitude of hippocampal theta by 81 +/-\n    14%.\n  source: Results, MS inactivation impairs memory and the wheel firing fields, paragraph 1; Figure\n    1d and Supplementary Figure 1a,b\n  quote: After the injection, the amplitude of hippocampal theta rhythm was reduced by 81 ± 14%\n    (Wilcoxon signed-rank test (WSR), P < 0.001\n  statistics:\n  - test: Wilcoxon signed-rank test\n    p: 0.001\n    p_relation: <\n    n: 13 recordings from 3 animals (Figure 1 legend); the text gives 15 muscimol recordings\n  expected:\n    quantity: reduction of normalized theta power, muscimol against pre\n    value: 81\n    tolerance: 14\n    unit: '%'\n  criterion: As the Methods (LFP power), Thomson multitaper spectra (NW = 4), the peak power in\n    6-10 Hz per trial, normalized by the pre-session value and averaged across trials; reduction\n    is 1 minus the muscimol mean. Reproduced when the reduction is within tolerance and a\n    one-sided WSR over recordings has p < 0.001. Open, with readings run each - the periods\n    analysed (wheel runs, as Supplementary Fig. 1b shows; maze runs; both); the \"30\" printed after\n    NW = 4 (read as the number of samples ... not given; readings a 1 s and a 2 s window with\n    2NW-1 tapers); the LFP channel (the one of Theta phase estimation); the muscimol period\n    readings (a) and (b) of the opening comment.\n- id: fig1e-performance\n  statement: Muscimol degraded performance in the alternation task from 94 +/- 5% correct before\n    the injection to 61 +/- 15% correct.\n  source: Results, MS inactivation impairs memory and the wheel firing fields, paragraph 1; Figure\n    1e and Supplementary Figure 1c\n  quote: 'the animals’ performance in the memory task was severely degraded ... (pre-muscimol: 94 ±\n    5% correct, muscimol: 61 ± 15% correct; WSR, P < 0.001'\n  statistics:\n  - test: Wilcoxon signed-rank test\n    p: 0.001\n    p_relation: <\n    n: 13 recordings from 3 animals (Figure 1 legend)\n  expected:\n  - quantity: correct choices, pre session\n    value: 94\n    tolerance: 5\n    unit: '%'\n  - quantity: correct choices, muscimol session\n    value: 61\n    tolerance: 15\n    unit: '%'\n  criterion: Per session, correct (alternating) arm choices over all choices, from the maze\n    events; muscimol period readings (a) and (b) of the opening comment. Reproduced when both\n    values are within tolerance and the muscimol value is lower than pre by a one-sided WSR over\n    recordings at p < 0.001.\n- id: fig1e-performance-restored\n  statement: Performance in the memory task was restored several hours after the injection.\n  source: Results, MS inactivation impairs memory and the wheel firing fields, paragraph 1; Figure\n    1e (Post)\n  quote: The performance of the animals in the memory task was restored several hours after the\n    injection\n  statistics:\n  - about: muscimol against post session (P printed on Figure 1e)\n    test: Wilcoxon signed-rank test (Methods, Statistics)\n    p: 0.001\n    p_relation: <\n    n: 13 recordings from 3 animals\n  depends_on:\n  - fig1e-performance\n  criterion: Performance as in fig1e-performance. Figure 1e prints two P < 0.001, read as pre\n    against muscimol and muscimol against post. Reproduced when the post session is higher than\n    the muscimol session by a one-sided WSR over recordings at p < 0.001.\n- id: figs1-activity-unchanged\n  statement: The overall activity of the animals was not altered by muscimol, though running speed\n    was slightly reduced on the wheel and in the maze.\n  source: Results, MS inactivation impairs memory and the wheel firing fields, paragraph 1;\n    Supplementary Figure 1d-h\n  quote: The overall activity of the animals was not altered (Supplementary Fig. 1d–h), although\n    running speeds were slightly reduced in both the maze and the wheel.\n  criterion: A claim of absence for which the paper reports no test. Measures from Supplementary\n    Figure 1 - running speed on the wheel and in the maze (1d) and the time spent in the delay\n    area before a wheel run is initiated (1f). Test from the Methods' list, WSR over recordings,\n    pre against muscimol, at 0.05. Reproduced when the delay time does not differ (two-sided\n    reading and one-sided longer reading both shown) and the mean wheel and maze speeds are lower\n    under muscimol; the size of each change is reported. \"Slightly\" is not quantified, so the\n    size of the speed reduction is reported and does not decide the outcome.\n- id: fig2c-wheel-field-info\n  statement: Firing field information of wheel neurons with fields fell from 1.7 +/- 0.8 bits\n    before the injection to 0.6 +/- 0.5 bits under muscimol.\n  source: Results, MS inactivation impairs memory and the wheel firing fields, paragraph 2; Figure\n    2c and Supplementary Figure 4c\n  quote: 'Firing field information, a measure that quantifies the prominence of firing fields above\n    baseline (Online Methods), decreased significantly after the injection (pre-muscimol: 1.7 ±\n    0.8 bits, post-muscimol: 0.6 ± 0.5 bits, Kolmogorov-Smirnov test (K-S), P < 0.001'\n  statistics:\n  - test: Kolmogorov-Smirnov test\n    p: 0.001\n    p_relation: <\n    n: 158 neurons from 3 animals\n  expected:\n  - quantity: firing field information on the wheel, pre\n    value: 1.7\n    tolerance: 0.8\n    unit: bits\n  - quantity: firing field information on the wheel, muscimol\n    value: 0.6\n    tolerance: 0.5\n    unit: bits\n  criterion: Neurons with an episode field in the pre or post session (Firing field sequence of\n    episode cells), information on the trial-averaged smoothed rate over time, per session. The\n    text labels the second value \"post-muscimol\"; it is read as the muscimol session, since the\n    sentence says \"after the injection\" and the Figure 2c legend and its \"(P < 0.001)\" compare\n    pre with muscimol. Reproduced when both means are within tolerance and a one-sided K-S test\n    finds muscimol lower than pre at p < 0.001. Readings run each - the wheel time bin, the\n    margin threshold, the neuron count rule of cells-per-recording, and the muscimol period\n    readings, all from the opening comment.\n- id: fig2b-wheel-sequence-lost\n  statement: The ordered sequence of firing fields on the wheel was gone under muscimol.\n  source: Results, MS inactivation impairs memory and the wheel firing fields, paragraph 2; Figure\n    2b and Supplementary Figures 3a and 4a\n  quote: Firing fields on the wheel (158 neurons with firing fields from 3 animals; Supplementary\n    Fig. 2a–d) and their ordered sequences were gone after the injection\n  depends_on:\n  - fig2c-wheel-field-info\n  criterion: The paper gives no number for the wheel. Field sequence similarity as the Methods\n    define it (Firing field sequence similarity) - per recording and session, the vector of\n    latencies to each field neuron's peak rate, and the Spearman correlation between sessions.\n    Readings, run each - (a) per recording, the pre-muscimol correlation is not significantly\n    positive (one-sided Spearman, p >= 0.05) while pre-post is (p < 0.05), in most recordings;\n    (b) over recordings, the pre-muscimol correlations are lower than the pre-post correlations\n    by a one-sided WSR at p < 0.05. Reproduced when the readings agree that the order is lost.\n- id: figs4a-residual-fields-early\n  statement: Only a few wheel neurons kept or formed firing fields under muscimol, and all of these\n    fields lay in the first second of wheel running.\n  source: Results, MS inactivation impairs memory and the wheel firing fields, paragraph 2;\n    Supplementary Figure 4a\n  quote: We observed only a few cells that maintained or formed firing fields after the injection\n    (Supplementary Fig. 4a). Notably, all of these fields were located in the first second of\n    wheel running.\n  depends_on:\n  - fig2c-wheel-field-info\n  criterion: Episode fields detected in the muscimol session as in the opening comment. \"Only a\n    few\" is not quantified; readings, run each - fewer than 10% and fewer than 20% of the neurons\n    with fields in the pre or post session. \"Located in the first second\" read as (a) field\n    centre within 0-1 s of run onset, (b) field onset within 0-1 s. Reproduced when the count\n    holds under one count reading and every muscimol field meets the location under one\n    location reading; the count and the location of each field are reported.\n- id: fig2d-wheel-rate\n  statement: The mean firing rate of wheel neurons fell from 1.2 +/- 0.1 Hz to 0.9 +/- 0.1 Hz\n    under muscimol.\n  source: Results, MS inactivation impairs memory and the wheel firing fields, paragraph 2; Figure\n    2d and Supplementary Figure 4c\n  quote: The average firing rate of cells on the wheel decreased from 1.2 ± 0.1 Hz to 0.9 ± 0.1 Hz\n    (WSR, P < 0.001\n  statistics:\n  - test: Wilcoxon signed-rank test\n    p: 0.001\n    p_relation: <\n    n: 158 neurons from 3 animals\n  depends_on:\n  - fig2c-wheel-field-info\n  expected:\n  - quantity: mean firing rate on the wheel, pre\n    value: 1.2\n    tolerance: 0.1\n    unit: Hz\n  - quantity: mean firing rate on the wheel, muscimol\n    value: 0.9\n    tolerance: 0.1\n    unit: Hz\n  criterion: The neurons of fig2c-wheel-field-info; per neuron, spikes over time during wheel runs\n    in each session. Reproduced when both means are within tolerance and a one-sided paired WSR\n    over neurons finds muscimol lower at p < 0.001.\n- id: fig2e-wheel-theta-sequences\n  statement: The percentage of windows with significant theta sequences during wheel running fell\n    from 7.8 +/- 0.4% to 5.5 +/- 0.5% under muscimol, against a chance level of 5.3%.\n  source: Results, MS inactivation impairs memory and the wheel firing fields, paragraph 2; Figure\n    2e and Supplementary Figure 5a,b\n  quote: 'theta sequences on the wheel were also lost after the injection (see Online Methods;\n    pre-muscimol: 7.8 ± 0.4%, muscimol: 5.5 ± 0.5% ... chance level = 5.3%, WSR, P < 0.005'\n  statistics:\n  - test: Wilcoxon signed-rank test\n    p: 0.005\n    p_relation: <\n    n: 13 recordings from 3 animals (Figure 2 legend); the Methods select 9 recordings from 3\n      animals for the wheel\n  expected:\n  - quantity: percentage of significant theta sequences on the wheel, pre\n    value: 7.8\n    tolerance: 0.4\n    unit: '%'\n  - quantity: percentage of significant theta sequences on the wheel, muscimol\n    value: 5.5\n    tolerance: 0.5\n    unit: '%'\n  - quantity: chance level, wheel\n    value: 5.3\n    tolerance: 0.53\n    unit: '%'\n  depends_on:\n  - fig2c-wheel-field-info\n  criterion: Theta sequence detection of the opening comment on the wheel, with the episode field\n    sequence of each recording and trajectory. The recordings tested are open - (a) the 9 that\n    pass the Methods' selection, (b) all 13 muscimol recordings of the legend. Reproduced when,\n    under one reading, both means are within tolerance and a one-sided WSR over recordings finds\n    muscimol lower at p < 0.005. Figure 2e prints \"P < 0.005\" twice, read as pre against\n    muscimol and muscimol against post; the second is shown.\n- id: fig2h-maze-field-info\n  statement: In the maze arms, firing field information fell slightly but significantly under\n    muscimol, from 1.4 +/- 0.67 to 1.2 +/- 0.8 bits, while firing fields were maintained.\n  source: Results, MS inactivation impairs memory and the wheel firing fields, paragraph 3; Figure\n    2f-h and Supplementary Figures 6 and 7\n  quote: 'There was a small, but significant, decrease in firing field information (pre-muscimol:\n    1.4 ± 0.67 bits, muscimol: 1.2 ± 0.8 bits; K-S, P < 0.05'\n  statistics:\n  - test: Kolmogorov-Smirnov test\n    p: 0.05\n    p_relation: <\n    n: 160 neurons from 3 animals\n  expected:\n  - quantity: firing field information in the maze, pre\n    value: 1.4\n    tolerance: 0.67\n    unit: bits\n  - quantity: firing field information in the maze, muscimol\n    value: 1.2\n    tolerance: 0.8\n    unit: bits\n  criterion: Place cells with a field in the pre or post session, detected on the rate in time\n    (Firing fields of place cells in the alternation task); information on the spatial map over\n    distance along the arm, per trajectory (arm and direction). Reproduced when both means are\n    within tolerance and a one-sided K-S test finds muscimol lower at p < 0.05. Readings run each\n    - information on the spatial map (as the Methods say) and on the rate profile in time; the\n    neuron count rule of cells-per-recording; the muscimol period readings.\n- id: fig2i-maze-order-preserved\n  statement: The order of firing fields along the maze arms was preserved under muscimol; sequence\n    similarity between sessions was r = 0.4 +/- 0.06 and did not differ among the session pairs.\n  source: Results, MS inactivation impairs memory and the wheel firing fields, paragraph 3; Figure\n    2g,i\n  quote: but the order of firing fields along the maze arms was preserved (r = 0.4 ± 0.06,\n    Kruskal-Wallis test (K-W), df = 2, P > 0.05\n  statistics:\n  - test: Kruskal-Wallis test\n    statistic: df = 2\n    p: 0.05\n    p_relation: '>'\n    n: 160 neurons from 3 animals\n  expected:\n    quantity: firing field sequence similarity (Spearman r) between sessions\n    value: 0.4\n    tolerance: 0.06\n  depends_on:\n  - fig2h-maze-field-info\n  criterion: Firing field sequence similarity as the Methods define it, the Spearman correlation\n    between the vectors of peak locations of the place cells in two sessions, per recording and\n    trajectory, for the three pairs pre-muscimol, pre-post and muscimol-post. The mean over all\n    values is compared with 0.4. The absence is judged on the paper's test, a Kruskal-Wallis test\n    across the three pair types (df = 2), reproduced when p >= 0.05 and not reproduced when\n    p < 0.05; the group medians are reported either way. The mean must also lie within tolerance.\n- id: fig2j-maze-theta-sequences\n  statement: Theta sequences in the maze were severely reduced by muscimol, from 12.3 +/- 1.2% to\n    7.9 +/- 0.7% of windows, against a chance level of 6%, despite abundant familiar cues.\n  source: Results, MS inactivation impairs memory and the wheel firing fields, paragraph 3; Figure\n    2j and Supplementary Figure 8a,b\n  quote: 'theta sequences were severely affected by the injection (see Online Methods;\n    pre-muscimol: 12.3 ± 1.2%, muscimol: 7.9 ± 0.7%, chance level: 6%; WSR, P < 0.001'\n  statistics:\n  - test: Wilcoxon signed-rank test\n    p: 0.001\n    p_relation: <\n    n: 13 recordings from 3 animals (Figure 2 legend); the Methods select 5 recordings from 2\n      animals for the maze\n  expected:\n  - quantity: percentage of significant theta sequences in the maze, pre\n    value: 12.3\n    tolerance: 1.2\n    unit: '%'\n  - quantity: percentage of significant theta sequences in the maze, muscimol\n    value: 7.9\n    tolerance: 0.7\n    unit: '%'\n  - quantity: chance level, maze\n    value: 6\n    tolerance: 0.6\n    unit: '%'\n  depends_on:\n  - fig2h-maze-field-info\n  criterion: Theta sequence detection of the opening comment in the maze, with the place field\n    sequence of each trajectory. Recordings - (a) the 5 that pass the Methods' selection, (b) all\n    13 of the legend. The Results give P < 0.001; the panel prints P < 0.01 and P < 0.005. Reproduced\n    when, under one recording reading, both means are within tolerance and a one-sided WSR over\n    recordings finds muscimol lower at p < 0.001; partially reproduced when the means hold and\n    the test gives p < 0.01 only (the panel's value).\n- id: figs5-compression-lost\n  statement: Under muscimol the theta-timescale order of pairs of field neurons no longer followed\n    the distance between their fields (compression index) and fewer multi-cell CCG sequences were\n    found, on the wheel and in the maze.\n  source: Supplementary Figures 5c-h and 8c-e; Online Methods, Compression index and Multiple-cell\n    CCG derived sequence\n  inferred: No sentence states this result. The Results cite Supplementary Figures 5a-h and 8a-e\n    for the loss of theta sequences, and the legends show long against short timescale CCG peaks\n    and counts of high-score sequences for pre, muscimol and post; the statement is a reading of\n    those legends and of the Methods.\n  depends_on:\n  - fig2c-wheel-field-info\n  - fig2h-maze-field-info\n  criterion: As the Methods (Compression index) - pairs of field neurons with more than 50 counts\n    in a +/-0.7 s CCG of 3 ms bins; theta-timescale offset at the peak within +/-210 ms of the CCG\n    smoothed with a 12 ms Gaussian, discarded beyond 195 ms; field offset at the peak within\n    +/-1,650 ms of the CCG smoothed with a 150 ms Gaussian, discarded beyond 1,500 ms; Spearman\n    correlation of the two per recording and session. The paper reports no test or value; the\n    judgement is fixed here. Reproduced when the pre and post correlations are positive with\n    one-sided p < 0.05 in most recordings and the muscimol correlation is lower than pre by a\n    one-sided WSR over recordings at p < 0.05, in each environment. The multiple-cell CCG\n    sequences (10 ms bins, +/-80 ms, score rules of the Methods) are counted per session and\n    reported; fewer under muscimol in most recordings is shown as support, not as the test.\n- id: fig3c-model-theta-builds-fields\n  statement: In a recurrent network model with asymmetric connections, short-term depression and\n    facilitation, and theta input but no sensory cues, a bump of activity travels in each theta\n    cycle (theta sequences) and neurons fire over several cycles (firing fields); removing the\n    theta input disrupts both.\n  source: Results, Network model reproduced the effect of MS inactivation, paragraphs 1 and 3;\n    Figure 3c; Supplementary Modeling\n  quote: As a result, individual neurons fire during several subsequent theta cycles, forming theta\n    modulated firing fields (Fig. 3c and Supplementary Fig. 9e–g), despite complete absence of\n    sensory cues. ... This manipulation resulted in the disruption of firing fields and theta\n    sequences in the model (Fig. 3c)\n  criterion: A simulation; it uses no recorded data. The rate model of Supplementary Modeling\n    (equations 1-3) with N = 100, tau = 10 ms, J1 = 15, J0 = 30, tau_R = 0.1 s, tau_F = 0.3 s,\n    U = 0.05, g = 1.5, k = 2.5, delta = 0.2 rad, Ornstein-Uhlenbeck noise (10 ms, s.d. 5), and the\n    external currents of Supplementary Table 1 (theta/no cues - I = 2, I_theta = 30, I_L = 0,\n    f = 7 Hz; no theta/no cues - I = 2, I_theta = 0). Open - the duration, integration step,\n    initial state and seed; standard choices (10 s, 0.1 ms Euler, uniform low rates, several\n    seeds). Theta sequences measured as the bump's displacement within each cycle; fields as the\n    duration over which a unit's rate, smoothed over a cycle, stays above half its peak.\n    Reproduced when, with theta, the bump moves within each cycle and units fire over several\n    consecutive cycles (fields longer than three cycles), and without theta neither holds.\n- id: fig3d-model-cues-keep-fields\n  statement: With a slowly moving familiar cue input added to the model, removing theta still\n    disrupts theta sequences, but firing fields are maintained when the cue input is strong\n    enough.\n  source: Results, Network model reproduced the effect of MS inactivation, paragraph 4; Figure 3d\n  quote: Once we removed the theta input, the theta sequences were disrupted despite the presence\n    of sensory cues, similar to the effect observed in the absence of the cues. However, firing\n    fields were maintained with a sufficiently strong cue input (Fig. 3d)\n  depends_on:\n  - fig3c-model-theta-builds-fields\n  criterion: A simulation; it uses no recorded data. As fig3c-model-theta-builds-fields, with the\n    cue currents of Supplementary Table 1 (theta/cues - I = 2, I_theta = 30, I_L = 5, f = 8 Hz;\n    no theta/cues - I = 2, I_theta = 0, I_L = 5). The speed of the cue location theta_ext(t) is\n    not given for Figure 3d (the 2D case uses 2 pi/5 rad/s); readings - that speed, and the\n    \"slow\" and \"fast\" cue speeds of the Figure 3d legend read as half and twice it. Reproduced when,\n    under a cue speed reading, without theta the within-cycle sequences are gone but units keep\n    fields that follow the cue.\n- id: figs10-model-dc-no-fields\n  statement: Without theta, raising the nonspecific input of the model produces fast sequential\n    activity, not firing fields.\n  source: Results, Network model reproduced the effect of MS inactivation, paragraph 3;\n    Supplementary Figure 10b,c\n  quote: We tested whether an increase of the nonspecific input to the network would be able to\n    support firing fields in the absence of theta, but the model generated fast sequential\n    activity (Supplementary Fig. 10b,c) instead of firing fields.\n  depends_on:\n  - fig3c-model-theta-builds-fields\n  criterion: A simulation; it uses no recorded data. As fig3c-model-theta-builds-fields without\n    theta, with I raised; the high value is not given (Supplementary Fig. 10b says \"high\n    amplitude of DC input\"); readings I = 4, 6 and 10. Reproduced when, at the raised input, the\n    bump moves through the network faster than the field sequence speed with theta and units\n    do not fire over durations as long as the fields with theta.\n- id: fig4b-linear-track-info\n  statement: On a novel linear track, many neurons had firing fields with high information under\n    muscimol (0.95 +/- 0.04 bits) as in the post-muscimol recording (0.81 +/- 0.03 bits), with no\n    significant difference.\n  source: Results, Place fields on a novel linear track after MS inactivation; Figure 4a,b\n  quote: 'We observed many firing fields with high firing field information on the novel linear\n    track during both muscimol and post-muscimol recordings (firing field information, muscimol:\n    0.95 ± 0.04 bits, post-muscimol: 0.81 ± 0.03 bits; WSR, P = 0.23'\n  statistics:\n  - test: Wilcoxon signed-rank test\n    p: 0.23\n    n: 290 neurons from 2 animals\n  expected:\n  - quantity: firing field information on the novel linear track, muscimol\n    value: 0.95\n    tolerance: 0.04\n    unit: bits\n  - quantity: firing field information on the novel linear track, post-muscimol\n    value: 0.81\n    tolerance: 0.03\n    unit: bits\n  criterion: All units passing the open-field unit criteria (the Figure 4b count, 290, includes\n    neurons with no field). Map readings, run each - the open-field adaptive-binning map, and\n    the maze map (Gaussian s.d. 17.5 pixels) over distance along the track. A claim of absence\n    on the paper's test, a paired WSR over neurons - reproduced when it does not find muscimol\n    lower than post at 0.05 (one-sided, the direction of a loss of fields), not reproduced when\n    it does; the two-sided p is shown. Figure 4b prints P = 0.022 against P = 0.23 in the text;\n    both are reported. The means must also be within tolerance.\n- id: fig4b-linear-track-theta-modulation\n  statement: Theta modulation of spiking on the novel linear track was lower under muscimol (0.15\n    +/- 0.002) than after recovery (0.22 +/- 0.004), confirming the injection was effective.\n  source: Results, Place fields on a novel linear track after MS inactivation; Figure 4b\n  quote: 'we compared theta modulation of the cell firing between the conditions and found a\n    significant reduction of theta modulation during the muscimol recordings (theta modulation,\n    muscimol: 0.15 ± 0.002, post-muscimol: 0.22 ± 0.004; WSR, P = 1.2 × 10−25'\n  statistics:\n  - test: Wilcoxon signed-rank test\n    p: 1.2e-25\n    n: 290 neurons from 2 animals\n  expected:\n  - quantity: theta modulation, muscimol\n    value: 0.15\n    tolerance: 0.002\n  - quantity: theta modulation, post-muscimol\n    value: 0.22\n    tolerance: 0.004\n  criterion: Theta modulation of the opening comment for the units of fig4b-linear-track-info.\n    Reproduced when both means are within tolerance (the paper's s.e.m.) and a one-sided paired\n    WSR finds muscimol lower at p < 0.0001 (the panel's bound); the p-value is reported against\n    1.2e-25. Partially reproduced when the test holds and the means are within 10% of the\n    paper's values. Readings - the autocorrelogram span of the opening comment.\n- id: fig4a-linear-track-remap\n  statement: Although the sensory cues were the same, firing fields completely remapped between\n    the muscimol and post-muscimol recordings on the novel linear track.\n  source: Results, Place fields on a novel linear track after MS inactivation; Figure 4a\n  quote: Notably, despite the fact that the sensory cues were the same during the muscimol and\n    post-muscimol recordings, firing fields between the muscimol and post-muscimol recordings\n    completely remapped (Fig. 4)\n  depends_on:\n  - fig4b-linear-track-info\n  criterion: The paper gives no measure of remapping. Readings, run each - (a) per neuron, the\n    Pearson correlation of its muscimol and post-muscimol rate maps, against the correlations of\n    mismatched neuron pairs of the same recording; (b) the distance between its muscimol and\n    post-muscimol map peaks, against mismatched pairs. \"Completely\" is read as the matched values\n    being no closer than the mismatched ones by a one-sided K-S test at 0.05 (a test the\n    Methods list). Reproduced when both readings find no difference; the medians are reported.\n    Neurons with information of at least 1.1 bits in either session (the Supplementary Fig. 12f\n    threshold for a good field) and all neurons are shown.\n- id: figs11-control-fields-stable\n  statement: Firing fields formed on a novel linear track under control conditions are more\n    stable over two subsequent visits than those formed under muscimol.\n  source: Results, Place fields on a novel linear track after MS inactivation; Supplementary Figure\n    11a,b\n  quote: suggesting that firing fields formed in the absence of MS inputs are less stable than\n    firing fields formed under controlled conditions (Supplementary Fig. 11a,b)\n  depends_on:\n  - fig4a-linear-track-remap\n  criterion: The control recordings (136 neurons from 2 animals, two visits Control 1 and Control\n    2). The remapping measures of fig4a-linear-track-remap between the two control visits.\n    Reproduced when, under each reading, the control matched values are closer than their\n    mismatched pairs (one-sided K-S, p < 0.05) and closer than the muscimol against post values\n    (one-sided K-S, p < 0.05). Supplementary Fig. 11b also compares information and theta\n    modulation between visits by a Wilcoxon rank-sum test; those are reported.\n- id: fig5c-platform-info\n  statement: On a large novel platform, firing field information after muscimol was much lower\n    (0.62 +/- 0.04 bits) than in controls (1.1 +/- 0.04 bits); neurons fired almost independently\n    of position.\n  source: Results, No place fields on a novel platform after MS inactivation, paragraph 2; Figure\n    5b,c and Supplementary Figures 12a,b and 13\n  quote: After the injection, the firing field information was significantly lower (0.62 ± 0.04\n    bits) than in the control group (1.1 ± 0.04 bits; K-W, H = 81.35, P = 1.6 × 10−17\n  statistics:\n  - test: Kruskal-Wallis test\n    statistic: H = 81.35\n    p: 1.6e-17\n    n: 145 muscimol neurons from 5 animals and 247 control neurons from 4 animals (text); the\n      Figure 5c legend gives 223 neurons from 5 recordings and 372 neurons from 7 recordings\n  expected:\n  - quantity: firing field information, large novel platform, muscimol\n    value: 0.62\n    tolerance: 0.04\n    unit: bits\n  - quantity: firing field information, large novel platform, control\n    value: 1.1\n    tolerance: 0.04\n    unit: bits\n  criterion: Open-field maps and unit criteria of the opening comment, first exposure to the\n    large novel platform, muscimol against saline control recordings. Readings, run each - the\n    neuron sets of the text (145 and 247, also in Supplementary Fig. 12) and of the legend (223\n    and 372); bin and smoothing readings of the opening comment. Reproduced when, under one\n    reading, both means are within tolerance and a Kruskal-Wallis test of muscimol against\n    control gives p < 0.001 with muscimol lower; H and p are reported against 81.35 and 1.6e-17.\n    The data set holds one rat; if it lacks a control or muscimol group, the comparison its\n    sessions allow (muscimol against post-muscimol on the platform) is shown as a variant.\n- id: fig5b-platform-wall-fields\n  statement: Under muscimol on the novel platform, the few neurons that formed firing fields did so\n    close to the walls and corners.\n  source: Results, No place fields on a novel platform after MS inactivation, paragraph 2;\n    Supplementary Figures 12f,g and 13\n  quote: We found that hippocampal neurons were active almost independently of animals’ position\n    ... In some recordings, a few neurons formed firing fields in close proximity of walls and\n    corners of the platform\n  depends_on:\n  - fig5c-platform-info\n  criterion: Neurons of fig5c-platform-info with information above 1.1 bits (Supplementary Fig.\n    12f legend), muscimol recordings. Each field peak is assigned to the periphery or the middle;\n    the border is a dashed line in Supplementary Fig. 12f whose position the text does not give;\n    readings 15 cm and 25 cm from the walls. Reproduced when, under each reading, more of these\n    peaks lie at the periphery than its share of the platform area predicts (one-sided binomial\n    test at 0.05, as a test is not given), and the number of such neurons is a minority of all\n    muscimol neurons; counts reported.\n- id: figs14-no-stable-fields\n  statement: Over an hour on the novel platform under muscimol, no stable firing fields formed;\n    firing field information did not differ between four 15-min segments.\n  source: Results, No place fields on a novel platform after MS inactivation, paragraph 2;\n    Supplementary Figure 14\n  quote: However, we did not observe any stable firing fields (K-W, firing field information\n    between four 15-min segments, df = 3, χ2 = 6.22, P = 0.1\n  statistics:\n  - test: Kruskal-Wallis test\n    statistic: chi2(3) = 6.22\n    p: 0.1\n  depends_on:\n  - fig5c-platform-info\n  criterion: A claim of absence on the paper's test. The muscimol platform recordings cut into\n    four 15-min segments (0-15, 15-30, 30-45, 45-60 min); information per neuron and segment;\n    Kruskal-Wallis across the four segments (df = 3). Reproduced when p >= 0.05 and the segment\n    means stay low (below the control mean of fig5c-platform-info); not reproduced when p < 0.05\n    with a rising trend. Chi-squared and p are reported against 6.22 and 0.1.\n- id: figs15-higher-speed\n  statement: After the injection animals ran faster on the platform, but this change was not\n    specific to the novel environment.\n  source: Results, No place fields on a novel platform after MS inactivation, paragraph 2;\n    Supplementary Figure 15a-c\n  quote: We observed several changes in the behavior of animals after the injection, such as higher\n    running speed (Supplementary Fig. 15a–c) and stereotyped patterns of exploration, but none of\n    these changes could explain these results because they were not specific to the novel\n    environment.\n  criterion: Mean running speed per recording from the tracked position, muscimol against post\n    (or control) recordings, on the novel and the familiar platform, by a one-sided Wilcoxon\n    rank-sum test at 0.05 (the test of the Supplementary Fig. 15 legend). Reproduced when speed is\n    higher after muscimol on the novel platform and also on the familiar platform. Open - the\n    speed smoothing; standard choice, positions smoothed over 0.5 s.\n- id: figs16-small-platform\n  statement: On a smaller novel platform under muscimol, one animal formed place fields and the\n    other did not.\n  source: Results, No place fields on a novel platform after MS inactivation, paragraph 3;\n    Supplementary Figure 16a,b\n  quote: in that one animal formed and one animal did not form place fields on a small novel\n    platform\n  criterion: The smaller platform recordings (223 neurons from 2 animals), information per neuron\n    in the muscimol and post-muscimol sessions. \"Formed place fields\" is not defined; readings,\n    run each - (a) the muscimol information is not lower than post by a one-sided WSR at 0.05;\n    (b) the share of neurons above 1.1 bits under muscimol is at least half that of post.\n    Reproduced when, under a reading, one animal meets it and the other does not. The data set\n    holds one rat; it can show one of the two outcomes only.\n- id: fig6-repeated-muscimol-low\n  statement: On days 1 to 3 of muscimol visits to the same novel platform, firing field information\n    stayed low (0.63 +/- 0.07, 0.69 +/- 0.06 and 0.9 +/- 0.08 bits).\n  source: Results, Multiple visits are required to form compound place fields; Figure 6\n  quote: 'Firing field information remained low during all three muscimol recordings (day 1: 0.63 ±\n    0.07 bits, day 2: 0.69 ± 0.06 bits, day 3: 0.9 ± 0.08 bits'\n  expected:\n  - quantity: firing field information, muscimol, day 1\n    value: 0.63\n    tolerance: 0.07\n    unit: bits\n  - quantity: firing field information, muscimol, day 2\n    value: 0.69\n    tolerance: 0.06\n    unit: bits\n  - quantity: firing field information, muscimol, day 3\n    value: 0.9\n    tolerance: 0.08\n    unit: bits\n  criterion: Open-field maps and unit criteria of the opening comment; the recordings on three\n    consecutive days in the same platform (39 to 75 neurons from 3 animals). Reproduced when each\n    day's mean is within tolerance and below the same day's post-muscimol mean\n    (fig6-repeated-post-normal).\n- id: fig6-repeated-post-normal\n  statement: After recovery on each of days 1 to 3, firing fields on the same platform were normal,\n    with high information (1.1 +/- 0.08, 1.5 +/- 0.07 and 1.3 +/- 0.08 bits).\n  source: Results, Multiple visits are required to form compound place fields; Figure 6\n  quote: 'we observed normal firing fields with high firing field information (day 1: 1.1 ± 0.08\n    bits, day 2: 1.5 ± 0.07 bits, day 3: 1.3 ± 0.08 bits'\n  expected:\n  - quantity: firing field information, post-muscimol, day 1\n    value: 1.1\n    tolerance: 0.08\n    unit: bits\n  - quantity: firing field information, post-muscimol, day 2\n    value: 1.5\n    tolerance: 0.07\n    unit: bits\n  - quantity: firing field information, post-muscimol, day 3\n    value: 1.3\n    tolerance: 0.08\n    unit: bits\n  criterion: As fig6-repeated-muscimol-low, the post-muscimol visits. Reproduced when each day's\n    mean is within tolerance.\n- id: fig6-familiar-impervious\n  statement: Only after 3 days of familiarization without injections did firing fields on the\n    platform become impervious to MS inactivation (1.24 +/- 0.1 bits under muscimol).\n  source: Results, Multiple visits are required to form compound place fields; Figure 6\n  quote: Only after a 3-d familiarization without any injection did firing fields became impervious\n    to the effect of the inactivation (1.24 ± 0.1 bits\n  expected:\n    quantity: firing field information, muscimol, familiar platform\n    value: 1.24\n    tolerance: 0.1\n    unit: bits\n  depends_on:\n  - fig6-repeated-muscimol-low\n  criterion: As fig6-repeated-muscimol-low, the muscimol visit after familiarization. Reproduced\n    when the mean is within tolerance and higher than each day 1-3 muscimol mean (one-sided\n    Wilcoxon rank-sum, the test of the Supplementary Fig. 15 legend for these data, p < 0.05).\n"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/wang-2014.yaml",
 "old_string": "the \"30\" printed after\n    NW = 4 (read as the number of samples ... not given; readings a 1 s and a 2 s window with\n    2NW-1 tapers);",
 "new_string": "the \"30\" printed after\n    NW = 4, which the Methods do not explain (readings a 1 s and a 2 s window, 2NW-1 tapers);"
}
```

```
The file claims/wang-2014.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd  python tools/claims_check.py claims/wang-2014.yaml paper/10.1038-nn.3904.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  grep -n "—\|rather" claims/wang-2014.yaml; grep -c "criterion:" claims/wang-2014.yaml; git status --short
```

```
29
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
?? claims/wang-2014.yaml
?? scripts
```

**Agent**

I wrote `claims/wang-2014.yaml`, and the quote checker passes it: 29 claims, 28 quotes, 13 statistical values, 0 problems.

**Text read:** the version of record (`paper/10.1038-nn.3904.txt`), with the main text, legends and Online Methods, plus the supplement (Supplementary Modeling, Table 1, and the legends of Supplementary Figs. 1–17). Nothing the results rest on is missing. The paper links no code, so none was read. I could not render any figure pages because no PDF renderer was installed. I used the figure labels that survived in the text file instead.

**Claims:**
- **Quotes:** 28 of the 29 have one. The exception is `figs5-compression-lost`, which is marked `inferred`: the compression index and CCG sequence results appear only in the Supplementary Figs. 5 and 8 legends and the Methods.
- **Statistics:** 13 claims carry them, as WSR, K-S and Kruskal-Wallis tests.
- **Criteria:** all 29 have one.
- **Without recorded data:** 3 claims are model simulations (Fig. 3c, Fig. 3d, Supplementary Fig. 10b,c).
- **About the dataset:** the hc-5 description covers one rat and does not mention injections. Claims that need groups or a second animal (Fig. 5c, Supplementary Fig. 16) say so; whether the sessions are the muscimol ones is for the author to find.

**Details the paper leaves open, with the readings named:**
- **Peak-to-mean rule:** the Methods print "FRp2m ≤ Thp2m". That sign cannot work, so I read it as ≥ 3.
- **"Small" field margin:** at most 0.5 s or at most 1 s.
- **Parameters adjusted by eye:** this cannot be repeated, so the default values are used and recorded as a deviation.
- **"Excitatory" neurons:** the dataset's own labels, or all units.
- **Muscimol period:** all trials of the muscimol session, or the trials after theta power drops (I set that threshold myself).
- **Time bin for information on the wheel:** 1,250 Hz samples or 75 ms bins.
- **Open-field maps:** 2.5 or 5 cm bins, and the ref. 54 adaptive-binning constant, halved or doubled.
- **Refractory-violation units:** 0.3% or a fraction of 0.3.
- **Autocorrelogram span:** ±0.5 s or ±1 s.
- **The unexplained "30" in the LFP multitaper:** a 1 s or a 2 s window.
- **Recordings for theta sequences:** 9 on the wheel and 5 in the maze (Methods selection), or 13 (legends).
- **Platform neuron counts:** 145 and 247 in the text, or 223 and 372 in the Fig. 5 legend.
- **Periphery border in Supplementary Fig. 12f:** 15 or 25 cm from the walls.
- **Model details:** the cue speed and the "high" DC input are not given.
- **Undefined words:** "complete remapping", "only a few" and "formed place fields" each get readings in their claims.
- **Tests chosen in the claims file:** for the unquantified claims (wheel sequence loss, compression, remapping, and stability under control conditions), the tests come from the Methods' list (WSR, Spearman, K-S, one-sided). The paper does not apply them to these findings.

**Discrepancies inside the paper, recorded in the claims:**
- **Fig. 4b:** the panel prints P = 0.022, the text P = 0.23.
- **Fig. 2j:** the panel prints P < 0.01 and P < 0.005, the text P < 0.001.
- **Wheel information:** the text labels the second value "post-muscimol", but it is the muscimol session.
- **Muscimol recordings:** the text gives 15, the legends 13.

**Missing:** nothing from the paper that a claim needed.

## End of run

20 turns, 6 minutes, $1.89 at API prices, result: success.
