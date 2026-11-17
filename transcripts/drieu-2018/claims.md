# drieu-2018 · claims · run 42861933921

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  grep -n "^#" docs/protocol.md | head -50; ls paper/; head -30 paper/*.txt; wc -l paper/*.txt
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
cd  cat claims/fouke-2025.yaml; ls claims tools
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
[... 613 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat papers/datasets/drieu-2018.yaml; grep -l "crcns" claims/*.yaml | head; grep -A3 "^dataset:" $(grep -l "archive: crcns" claims/*.yaml | head -2)
```

```
# The datasets this paper is tested on (docs/paper-first.md).
schema_version: 1
paper: doi:10.1126/science.aat2952
title: Nested sequences of hippocampal assemblies during behavior support subsequent sleep replay
datasets:
- archive: crcns
  id: hc-18
  relation: primary
claims/asari-2009.yaml
claims/bruno-2017.yaml
claims/deweese-2004.yaml
claims/eyherabide-2008.yaml
claims/farrell-2020.yaml
claims/goncalves-2013.yaml
claims/gu-2011.yaml
claims/henze-2000.yaml
claims/holdgraf-2016.yaml
claims/jadhav-2016.yaml
claims/bruno-2017.yaml:dataset:
claims/bruno-2017.yaml-  archive: crcns
[... 7 more lines not kept]
```

**Agent**

Now the paper.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1126-science.aat2952.txt",
 "limit": 700
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1126-science.aat2952.txt",
 "offset": 700,
 "limit": 900
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1126-science.aat2952.txt",
 "offset": 1600,
 "limit": 1100
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1126-science.aat2952.txt",
 "offset": 2700,
 "limit": 1100
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  python -c "
import fitz
d=fitz.open('paper/10.1126-science.aat2952.supp.pdf'); print(len(d)); print(d[0].get_text()[:1500])
d=fitz.open('paper/10.1126-science.aat2952.pdf'); print(len(d)); print(d[4].get_text()[:3000])
"; timeout 20 git ls-remote https://github.com/michael-zugaro/FMAToolbox 2>&1 | head -3
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1126-science.aat2952.pdf",
 "pages": "5"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  python -c "
import pypdf
r=pypdf.PdfReader('paper/10.1126-science.aat2952.supp.pdf'); print(len(r.pages)); print(r.pages[0].extract_text()[:800])
" 2>&1 | head -30; cd $TMPDIR && git clone -q https://github.com/michael-zugaro/FMAToolbox && cd FMAToolbox && git log -1 --format='%H %ad' && ls
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd $TMPDIR/FMAToolbox; ls Analyses Unfinished General | head -150; grep -rli "replay\|quadrant\|bias" --include=*.m . | head -30
```

```
Analyses:
ActivityTemplates.m
AngularVelocity.m
BrainStates.m
CCG.m
CCGParameters.m
CSD.m
CV.m
CofiringCoefficient.m
CoherenceBands.m
CompareDistributions.m
Contents.m
CountSpikesPerCycle.m
DefineZone.m
Distance.m
FieldPSP.m
FieldShift.m
FilterLFP.m
FindDeltaWaves.m
FindRipples.m
[... 125 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/FMAToolbox/Analyses; for f in TestRemapping FieldShift MapStats PhasePrecession FindRipples FindSubcycles ReconstructPosition FiringCurve; do echo "=== $f"; sed -n '/^function/,/^%  Copyright/p' $f.m | head -70; done
```

```
=== TestRemapping
function [h,p,cr,ca] = TestRemapping(control,repeat,test,varargin)

%TestRemapping - Test if firing fields remap (or shift) between two conditions.
%
%  To test for random remapping between a control and a test condition, we
%  first estimate for each place cell the absolute field shift between the two
%  conditions, as the mode of the spatial cross-correlogram between the
%  respective firing fields. We then divide this value by the average field
%  size across conditions, yielding a relative shift. This measures by how much
%  the field moves between the two conditions, in proportion to the field size.
%  To account for baseline variability, we also estimate the relative field
%  shift between two repetitions of the control condition, and subtract it from
%  the relative shift in the test condition. This (unsigned) corrected shift is
%  averaged over all cells.
%
%  To test if this is significantly different from random remapping, we generate
%  a distribution of corrected relative shifts under the null hypothesis of
%  random remapping. This is done by randomly permuting the test firing fields
%  between the cells (bootstrap).
[... 534 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 20,112p paper/hc-18.data-description.txt; python tools/claims_check.py --help 2>&1 | head -20
```

Result: not kept, because it reads the paper's text.

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
import json;s=json.load(open('schemas/claims.schema.json'));print(json.dumps(s['\$defs'],indent=1)); print([k for k in s['properties']])"
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
[... 83 more lines not kept]
```

**Agent calls Write**

```json
{
 "file_path": "claims/drieu-2018.yaml",
 "content": "# Claims for Drieu, Todorova & Zugaro (2018), Science 362, 675-679, tested on CRCNS hc-18.\n# Written by an agent (model \"claude-opus-5-5\", Claude Code, runner \"GitHub Actions\"),\n# 2026-11-10, protocol pilot-14 as stated in docs/protocol.md.\n#\n# Text read: the version of record (main text, figure legends of Figs. 1 to 3), and the\n# author manuscript (HAL hal-02330673v1) for its Materials and Methods, the Fig. 4 legend and\n# supplementary figures S1 to S13 with their legends. The extracted text of the version of\n# record lacks its page 5 (Fig. 4 and the closing paragraphs), so the Fig. 4 legend is quoted\n# from the author manuscript. Where the two versions print different bounds, the version of\n# record is recorded: Fig. 1C peak rate P < 10^-3 (manuscript 10^-4); Fig. 1E V-test\n# P < 10^-10 (manuscript 10^-11). The Data analysis section of the Methods says that the\n# acquisition paragraph covers \"three rats\" with tetrodes and \"three rats\" with octrodes,\n# while the paper reports five rats throughout; five is taken as the count.\n#\n# Data the paper used (Methods, Animal training, Behavioural task; Fig. 1A; fig. S1): five\n# adult male Long-Evans rats, each tested on a single day in a novel room, so one session\n# per rat. Each session is baseline sleep, Passive 1 travel (treadmill off), sleep, Active\n# travel (treadmill on), sleep, Passive 2 travel, sleep. Each travel condition was 2 x ~15\n# laps on a 2.20 m x 1.30 m obround track, always forward at ~45-50 cm/s; each sleep epoch\n# ~90 min in a flower pot. Measured: sorted CA1 units (pyramidal cells and interneurons),\n# LFP at 1250 Hz, and head position from one or two LEDs (30 Hz video, resampled at\n# 39.0625 Hz). The data set's description (CRCNS hc-18) says it holds 5 sessions, one\n# per rat, with spikes, LFP, positions and event files; it also says custom scripts are\n# provided in the archive. Those are part of the dataset's files and were not read here.\n#\n# Code read: FMAToolbox (github.com/michael-zugaro/FMAToolbox, commit 6bbb366, 2018-03-27),\n# the toolbox the Methods name for all analyses. It holds general functions (FiringCurve,\n# MapStats, TestRemapping, FieldShift, PhasePrecession, ReconstructPosition, FindSubcycles,\n# FindRipples, MTSpectrum and others) but not the paper's own scripts for trajectory\n# scores, quadrant scores, z-proportions or pairwise bias correlations. Where the Methods\n# and the toolbox defaults disagree (field threshold 30% in the Methods, 20% by default;\n# ripple thresholds 1 and 3 s.d. and 20 to 110 ms in the Methods, 2 and 5 s.d. and 20 to\n# 100 ms by default; decoding bins), the Methods are followed.\n#\n# Common methods, all from the Materials and Methods of the author manuscript; the criteria\n# below refer to them by name.\n# - Units: putative pyramidal cells by k-means on waveform width, trough-to-peak duration\n#   and firing rate; only clusters with L-ratio < 0.05 (Data acquisition and preprocessing).\n# - Awake spike analyses restricted to linear velocity > 5 cm/s (Firing fields).\n# - Firing curves on the linearized track, kernel method, 2.4 cm bins, Gaussian kernel\n#   4.5 cm. A field is the set of contiguous bins holding the peak (peak at least 1 Hz in\n#   Active, 0.7 Hz in Passive) with rate above 30% of the peak; a place cell is a pyramidal\n#   cell with at least one field (Firing fields). Open: a minimum field size. Readings: (a)\n#   none, as the Methods give none; (b) FiringCurve's default of 10 bins.\n# - Theta cycles: start at peaks of the theta-band (6-10 Hz) filtered LFP; cycles shorter\n#   than 80 ms or longer than 200 ms dropped; only runs of at least three contiguous cycles\n#   kept (Theta power, frequency and cycles). Peaks and troughs for asymmetry and phase\n#   precession from the LFP filtered at 1-40 Hz (Theta asymmetry and phase precession).\n#   Open: the LFP channel. Readings: (a) one CA1 pyramidal-layer channel per rat with the\n#   largest theta power; (b) the mean of the pyramidal-layer channels, as for ripples.\n#   Open: how spike phase is assigned. Readings: (a) linear interpolation between the\n#   1-40 Hz peaks (0) and troughs (pi); (b) Hilbert phase of the theta-band filtered LFP.\n# - Bayesian decoding (Bayesian trajectory decoding): occupancy prior, Poisson likelihood,\n#   trained on each travel session and applied to that session (theta sequences, windows\n#   of pi/3, six per cycle) and to the following sleep (replay, 20 ms windows). Baseline\n#   sleep is decoded with the model of the travel session whose post-sleep it is compared\n#   with. Only events with at least three units, and candidate events lasting > 60 ms.\n#   Position bins 2.4 cm, as for firing curves; ReconstructPosition's default of 200 bins\n#   is a variant.\n# - Trajectory score and slope (Assessing trajectories): R(v, rho) is the mean probability\n#   within d = 45 cm of a line, maximized over all v and rho whose total distance is under\n#   the 6 m track length, the line wrapping around the track. Significance from 5000\n#   shuffles, each circularly shifting the decoded probabilities within each window by a\n#   random number of bins; Monte Carlo p is the proportion of shuffled scores above the\n#   observed one; significant at p <= 0.05. Normalized score is (score - mean of shuffled\n#   scores) / s.d. of shuffled scores. Open: how slopes per phase window become m/s.\n#   Readings: (a) with each cycle's duration; (b) with the session's mean theta period.\n# - Quadrant score (same section): the central zone of the decoded matrix, +/-1.5 m around\n#   the current position and +/-2/3 cycle around the trough, split in four quadrants;\n#   (bottom left + top right - top left - bottom right) / sum of all four.\n# - Z-proportions (Assessing trajectories, Z-proportions): the score-slope matrix of event\n#   proportions, each cell z-scored against the same cell of 5000 shuffled matrices. The\n#   bin sizes are not given; a 0.05 score by 3 m/s slope grid is used as a standard choice,\n#   and readings with half and double these sizes are shown.\n# - SWS (Candidate replay events): k-means on the theta (6-10 Hz) / delta (1-4 Hz) ratio of\n#   sleep spectrograms; epochs > 120 s, gaps < 1 s bridged. Candidate events: place-cell\n#   spike count in 1 ms bins, Gaussian smoothing s.d. 10 ms, peak > 3 s.d., bounded where\n#   it falls back to the mean, events > 500 ms excluded. Open: over what the mean and s.d.\n#   are taken. Readings: (a) all SWS of the sleep session; (b) the whole sleep session.\n# - Ripples (Ripple detection): pyramidal-layer channels filtered 100-250 Hz and averaged,\n#   minus the averaged 300-500 Hz signal; negative values dropped, positive values z-scored;\n#   above 1 s.d. with a peak above 3 s.d.; events <= 20 ms or >= 110 ms excluded.\n# - Pairwise bias correlation (Pairwise bias correlations): bias matrix per sequence,\n#   cosine between bias matrices over neurons that fired in both, sequences with at least\n#   three common neurons, autocorrelations dropped; a pair is significant when it exceeds\n#   95% of a surrogate built by shuffling spike order in the second sequence. For Figs. 3G\n#   and 4G each condition is cut in 20 temporal bins; median over pairs within a session,\n#   then median over sessions. Open: the number of surrogates (a standard 1000 is used; it\n#   only sets the resolution of the 95% bound) and which theta cycles count as sequences.\n#   Readings: (a) every analysed theta cycle with at least three active place cells; (b)\n#   only cycles with a significant trajectory score.\n# - Statistics (Data analysis and statistics): two-tailed throughout. Gaussian paired data,\n#   repeated-measures ANOVA, post hoc paired t-tests with Bonferroni correction;\n#   non-Gaussian independent data, Kruskal-Wallis, post hoc Wilcoxon rank-sum with\n#   Bonferroni correction; non-Gaussian paired data, Friedman, post hoc signed-rank;\n#   proportions, binomial proportion test; a median against a single value, Wilcoxon\n#   signed-rank; distributions, Kolmogorov-Smirnov. Gaussianity by Jarque-Bera. With three\n#   conditions the Bonferroni levels are 0.05/3 = 0.017, 0.01/3 = 0.0033 and\n#   0.001/3 = 0.00033, as the legends print.\nschema_version: 2\npaper: doi:10.1126/science.aat2952\nclaims:\n- id: figs1-travel-similar\n  statement: Train velocity, number of laps and travel duration did not differ between\n    Passive 1, Active and Passive 2 (repeated-measures ANOVA, P > 0.05 for each, 5 rats).\n  source: Results, paragraph 5; fig. S1B to S1D and legend\n  quote: The train velocity, number of laps, and travel duration were similar in all\n    conditions for all rats (fig. S1, B to D)\n  statistics:\n  - about: train velocity\n    test: repeated measures ANOVA\n    p: 0.05\n    p_relation: \">\"\n    n: 5 rats\n  - about: number of laps\n    test: repeated measures ANOVA\n    p: 0.05\n    p_relation: \">\"\n    n: 5 rats\n  - about: travel duration\n    test: repeated measures ANOVA\n    p: 0.05\n    p_relation: \">\"\n    n: 5 rats\n  expected:\n  - quantity: train velocity, Passive 1, mean over rats\n    value: 46.80\n    tolerance: 2.04\n    unit: cm/s\n  - quantity: train velocity, Active, mean over rats\n    value: 47.87\n    tolerance: 1.83\n    unit: cm/s\n  - quantity: train velocity, Passive 2, mean over rats\n    value: 46.73\n    tolerance: 1.85\n    unit: cm/s\n  - quantity: laps, Passive 1, mean over rats\n    value: 38.2\n    tolerance: 2.8\n  - quantity: laps, Active, mean over rats\n    value: 30.8\n    tolerance: 2.24\n  - quantity: laps, Passive 2, mean over rats\n    value: 32.2\n    tolerance: 1.77\n  - quantity: travel duration, Passive 1, mean over rats\n    value: 8.24\n    tolerance: 0.69\n    unit: min\n  - quantity: travel duration, Active, mean over rats\n    value: 6.50\n    tolerance: 0.33\n    unit: min\n  - quantity: travel duration, Passive 2, mean over rats\n    value: 7.20\n    tolerance: 0.51\n    unit: min\n  criterion: Tolerances are the s.e.m. the fig. S1 legend gives. Per rat and condition, the\n    mean train velocity over the travel (from tracked head position on the linearized\n    track), the number of completed laps and the duration of the travel session. The\n    paper does not say how velocity is averaged; readings are (a) over all position\n    samples of the session, (b) over samples above 5 cm/s, the Methods' threshold for awake\n    analyses. A claim of absence, judged on the paper's test, a repeated-measures ANOVA\n    over the 5 rats for each measure. Reproduced when all three ANOVAs give P > 0.05 and at\n    least seven of the nine means are within tolerance; the effect sizes are reported.\n- id: fig1c-field-size-similar\n  statement: Place field size was the same in the three travel conditions (Kruskal-Wallis,\n    P > 0.05).\n  source: Fig. 1C and legend; Results, paragraph 5\n  quote: Place field size was maintained across travel conditions [Kruskal-Wallis (KW) test,\n    P > 0.05]\n  statistics:\n  - test: Kruskal-Wallis\n    p: 0.05\n    p_relation: \">\"\n  depends_on:\n  - figs2b-place-cell-count\n  criterion: A claim of absence. Field size of every place field (Common methods, Firing\n    curves), pooled over rats per condition, compared with a Kruskal-Wallis test across\n    the three conditions as the legend states. Reproduced when P > 0.05, not reproduced\n    when P <= 0.05; the median sizes are reported. Open is whether a cell with two fields\n    contributes both; readings (a) the field holding the peak only, (b) every field.\n- id: fig1c-peak-rate-lower-passive1\n  statement: Place-cell peak firing rates were lower in Passive 1 than in Active.\n  source: Fig. 1C and legend\n  quote: Peak firing rates were somewhat lower in Passive 1 than in Active (KW test, ***P <\n    10–3)\n  statistics:\n  - test: Kruskal-Wallis\n    p: 0.001\n    p_relation: \"<\"\n  depends_on:\n  - figs2b-place-cell-count\n  criterion: Peak in-field rate of each place cell (Common methods, Firing curves), pooled\n    over rats per condition. Kruskal-Wallis across the three conditions, then a post hoc\n    Wilcoxon rank-sum Passive 1 against Active with Bonferroni correction (Methods,\n    Data analysis and statistics). Reproduced when the post hoc test gives P < 0.001/3 with\n    the Passive 1 median lower; partially reproduced when it is significant at 0.05/3 only.\n    The legend's P could also be the Kruskal-Wallis test itself; that reading (P < 0.001\n    with Passive 1 lowest) is shown as well, and either reading reproduces.\n- id: figs2b-place-cell-count\n  statement: Fewer place cells were recorded in Passive 1 (94) than in Active (150) and\n    Passive 2 (135), a difference significant across rats (repeated-measures ANOVA, P <\n    0.05).\n  source: fig. S2B and legend; Results, paragraph 5\n  quote: However, peak firing rates and place cell count were somewhat reduced during\n    passive travels\n  statistics:\n  - test: repeated measures ANOVA\n    p: 0.05\n    p_relation: \"<\"\n    n: 5 rats\n  expected:\n  - quantity: place cells in Passive 1, all rats\n    value: 94\n    tolerance: 9.4\n  - quantity: place cells in Active, all rats\n    value: 150\n    tolerance: 15\n  - quantity: place cells in Passive 2, all rats\n    value: 135\n    tolerance: 13.5\n  criterion: Place cells by the Methods' definition (Common methods, Units and Firing\n    curves), counted per rat and condition and summed over rats; a repeated-measures ANOVA\n    of the per-rat counts across conditions. Reproduced when all three totals are within\n    tolerance under one field-size reading and the ANOVA gives P < 0.05; partially\n    reproduced when the totals hold but not the test, or the order (Passive 1 lowest) and\n    the test hold but not the totals. The counts rest on unit sorting and the k-means\n    classification, which are redone or taken from the dataset's clusters as the author\n    finds them.\n- id: figs2c-track-coverage\n  statement: In every travel condition the place fields together covered the whole track.\n  source: Results, paragraph 5; fig. S2C\n  quote: together covered the entire train track (fig. S2C)\n  depends_on:\n  - figs2b-place-cell-count\n  criterion: The percentage of linearized track bins (2.4 cm) inside at least one place\n    field, per condition. The paper gives no number (fig. S2C plots it, and no value is\n    legible in the text) and no threshold for entire; 95% is used as the threshold, a\n    choice made here. Readings are (a) fields pooled over all rats; (b) each rat\n    separately. Reproduced when coverage is at least 95% in all three conditions under\n    reading (a), and the per-rat values are reported.\n- id: fig1d-no-remapping-p1-active\n  statement: Place fields did not remap between Passive 1 and Active; the mean unsigned\n    proportional field shift was smaller than under random remapping (P < 0.01, 2000\n    bootstraps), and peak-location shifts were non-uniform and centred on zero (Rayleigh\n    P < 0.001, V-test P < 10^-4).\n  source: Fig. 1D and legend; Results, paragraph 5\n  quote: Firing fields did not remap between Passive 1 and Active. Left; Mean unsigned\n    proportional shift s (vertical gray line; **P < 0.01) and s distribution for n = 2000\n    bootstrapped remapping data sets\n  statistics:\n  - about: mean unsigned proportional shift against shuffled cell identities\n    test: bootstrap\n    p: 0.01\n    p_relation: \"<\"\n    n: 2000 bootstrapped remapping data sets\n  - about: uniformity of angular peak shifts\n    test: Rayleigh test\n    p: 0.001\n    p_relation: \"<\"\n  - about: mean angular shift against 0\n    test: V-test\n    p: 0.0001\n    p_relation: \"<\"\n  depends_on:\n  - figs2b-place-cell-count\n  criterion: Following the Methods (Firing fields, paragraph 2) and FMAToolbox\n    TestRemapping and FieldShift. For each place cell, the shift is the mode of the spatial\n    cross-correlogram of its two firing curves divided by its mean field size; the mean\n    unsigned shift is compared with 2000 shuffles of cell identity in the test condition;\n    p is the proportion of shuffled means at or below the observed one. Then peak locations\n    as angles on the obround track, differences tested with a Rayleigh test and a V-test\n    against 0. Open, with readings run each; (a) cells with a field in both conditions,\n    (b) cells with a field in either; the cross-correlogram (a) circular, as the track is\n    a closed loop, (b) linear, TestRemapping's default; no repeat-control correction, as\n    the Methods mention none (TestRemapping with the control given twice). Reproduced when\n    all three tests reach their legend bounds under one reading; partially reproduced when\n    the bootstrap test and the V-test are significant at 0.05 only.\n- id: fig1e-no-remapping-active-p2\n  statement: Place fields did not remap between Active and Passive 2 (bootstrap P ~ 0;\n    Rayleigh P < 10^-9; V-test P < 10^-10).\n  source: Fig. 1E and legend\n  quote: Firing fields also did not remap between Active and Passive 2. Data are displayed as\n    in (D). Left; ***P ~ 0. Inset; Rayleigh test, P < 10–9; V-test against 0, P < 10–10.\n  statistics:\n  - about: mean unsigned proportional shift against shuffled cell identities\n    test: bootstrap\n    p: 0\n    n: 2000 bootstrapped remapping data sets\n  - about: uniformity of angular peak shifts\n    test: Rayleigh test\n    p: 1.0e-09\n    p_relation: \"<\"\n  - about: mean angular shift against 0\n    test: V-test\n    p: 1.0e-10\n    p_relation: \"<\"\n  depends_on:\n  - figs2b-place-cell-count\n  criterion: As fig1d-no-remapping-p1-active, Active as control and Passive 2 as test. P ~ 0\n    is read as no shuffled mean at or below the observed one in 2000. Reproduced when the\n    bootstrap gives P < 0.001 and the Rayleigh and V-tests reach P < 10^-9 and P < 10^-10;\n    partially reproduced when all three are significant at 0.001 only.\n- id: figs2d-stability-p1-p2\n  statement: Place fields were also stable between Passive 1 and Passive 2 (bootstrap P <\n    0.02; V-test P < 0.05), though the angular shifts did not depart from uniformity by the\n    Rayleigh test (P > 0.05).\n  source: fig. S2D and legend\n  quote: Stability of place fields between Passive 1 and Passive 2. Top, mean unsigned\n    proportional shift σ (∗P < 0.02). ... Inset, circular distribution of angular differences\n    between in-field peak firing rates (Rayleigh test, P > 0.05, V-test against 0, ∗P < 0.05)\n  statistics:\n  - about: mean unsigned proportional shift against shuffled cell identities\n    test: bootstrap\n    p: 0.02\n    p_relation: \"<\"\n    n: 2000 bootstrap random remapping data sets\n  - about: uniformity of angular peak shifts\n    test: Rayleigh test\n    p: 0.05\n    p_relation: \">\"\n  - about: mean angular shift against 0\n    test: V-test\n    p: 0.05\n    p_relation: \"<\"\n  depends_on:\n  - figs2b-place-cell-count\n  criterion: As fig1d-no-remapping-p1-active, Passive 1 as control and Passive 2 as test.\n    Reproduced when the bootstrap gives P < 0.02 and the V-test P < 0.05 under one reading;\n    the Rayleigh result is reported, and it is judged as the paper's test of absence\n    (not significant at 0.05).\n- id: fig2b-theta-frequency-unchanged\n  statement: Theta frequency did not differ between travel conditions (repeated-measures\n    ANOVA, P > 0.90).\n  source: Fig. 2B, top, and legend; Results, paragraph 6\n  quote: Theta frequency was unchanged across conditions [top; repeated-measures analysis of\n    variance (ANOVA), P > 0.90]\n  statistics:\n  - test: repeated measures ANOVA\n    p: 0.9\n    p_relation: \">\"\n  criterion: A claim of absence. Multitaper power spectrum of the detrended LFP per rat and\n    condition (Methods, Theta power, frequency and cycles); theta frequency as the mode in\n    6-10 Hz. Repeated-measures ANOVA across the three conditions with rats as subjects.\n    Reproduced when P > 0.05 (the paper's test finds no effect), and the P is reported\n    against the paper's 0.90. The LFP used is open (Common methods, Theta cycles), and so\n    is whether it is restricted to velocity > 5 cm/s; readings (a) all of the travel\n    session, (b) only samples above 5 cm/s.\n- id: fig2b-theta-power-reduced\n  statement: Theta power was lower during passive travel than active travel\n    (repeated-measures ANOVA, P < 10^-6), with power reduced at both the fundamental and\n    the first harmonic.\n  source: Fig. 2A and 2B, middle, and legend; Results, paragraph 6\n  quote: However, during passive travel, power was slightly reduced at both the fundamental\n    frequency and the first harmonic\n  statistics:\n  - test: repeated measures ANOVA\n    p: 1.0e-06\n    p_relation: \"<\"\n  - about: post hoc comparisons\n    test: paired Student's t-test\n    p: 0.0033\n    p_relation: \"<\"\n    corrected: Bonferroni\n  criterion: Power spectra per rat and condition normalized as (S_ij - mu_j) / sigma_j over\n    the conditions of rat j; theta power as the maximum in 6-10 Hz (Methods, Theta power,\n    frequency and cycles). Repeated-measures ANOVA, post hoc paired t-tests with Bonferroni\n    correction (Methods, statistics). The unit the ANOVA runs over is open, since P <\n    10^-6 is hard to reach with 5 rats; readings (a) one value per rat and condition, (b)\n    one value per spectrogram window, paired by rat. Reproduced when, under one reading,\n    the ANOVA gives P < 0.001 and both passive conditions are lower than Active in the post\n    hoc tests at 0.05/3; partially reproduced when the direction holds with the ANOVA\n    significant at 0.05 only. The first-harmonic power (12-20 Hz peak) is reported.\n- id: fig2b-theta-asymmetry-reduced\n  statement: The shape of theta cycles changed during passive travel, with decreased cycle\n    asymmetry (Kruskal-Wallis, P < 10^-84).\n  source: Fig. 2B, bottom, and legend; Results, paragraph 6\n  quote: whereas theta power (middle; repeated-measures ANOVA, P < 10–6) and shape (bottom,\n    theta asymmetry; KW test, P < 10–84) were altered during passive travel\n  statistics:\n  - test: Kruskal-Wallis\n    p: 1.0e-84\n    p_relation: \"<\"\n  - about: post hoc comparisons\n    test: Wilcoxon rank-sum\n    p: 0.00033\n    p_relation: \"<\"\n    corrected: Bonferroni\n  criterion: Per theta cycle (Common methods, Theta cycles), asymmetry log(dt2/dt1), dt1 from\n    cycle start to trough and dt2 from trough to cycle end, on the 1-40 Hz LFP (Methods,\n    Theta asymmetry and phase precession); cycles pooled over rats. Kruskal-Wallis across\n    conditions, post hoc rank-sum with Bonferroni correction. Decreased asymmetry is read\n    as median asymmetry closer to zero (smaller absolute value) in each passive condition\n    than in Active. Reproduced when the Kruskal-Wallis P < 10^-10 and both passive\n    conditions differ from Active at 0.001/3 in that direction; partially reproduced when\n    significant at 0.05 only.\n- id: fig2cd-spike-bursts-slower\n  statement: Place cells oscillated faster than theta during active travel, while during\n    passive travel their spike bursts recurred at lower frequencies, closer to theta\n    frequency.\n  source: Fig. 2C and 2D and legend; fig. S4A; Results, paragraph 6\n  quote: place cells continued to oscillate slightly faster than theta (i.e., phase\n    precession) during active travel, whereas this was reduced in passive travel\n  statistics:\n  - about: spectral modes, overall or first comparison\n    p: 1.0e-06\n    p_relation: \"<\"\n  - about: spectral modes, second comparison\n    p: 0.02\n    p_relation: \"<\"\n  criterion: Per place cell, spike times converted to unwrapped theta phase / 2 pi and a\n    multitaper spectrum of this spike train taken (Methods, Theta burst frequency); its\n    mode within 0.75 to 1.25 cycle^-1 (fig. S4A legend), cells without a peak there\n    dropped. The legend names no test for Fig. 2D; by the Methods' rules for independent\n    non-Gaussian data this is Kruskal-Wallis with rank-sum post hoc tests. Which pairs the\n    two P values belong to is open; readings (a) Kruskal-Wallis P < 10^-6 and one post hoc\n    pair at 0.02, (b) Passive 1 against Active and Active against Passive 2. Spectrum\n    parameters are not given; the chronux defaults (time-bandwidth 3, 5 tapers) are used\n    as a standard choice. Reproduced when the median mode in Active exceeds those of both\n    passive conditions, the Active-Passive 1 difference reaches P < 10^-6 and the\n    Active-Passive 2 difference P < 0.02 under one reading; partially reproduced when the\n    ordering holds with both differences significant at 0.05.\n- id: figs4b-proportions-oscillating-precessing\n  statement: Fewer place cells oscillated faster than theta in passive travel (36/94 Passive\n    1, 90/150 Active, 63/135 Passive 2), and fewer were significantly phase precessing\n    (14/94, 53/150, 21/135).\n  source: fig. S4B and legend\n  quote: Proportion of place cells oscillating faster than theta frequency (top, Passive 1;\n    36/94, Active; 90/150, Passive 2; 63/135) and proportion of significant phase-precessing\n    cells (bottom, Passive 1; 14/94, Active; 53/150, Passive 2; 21/135)\n  depends_on:\n  - figs2b-place-cell-count\n  - fig2cd-spike-bursts-slower\n  expected:\n  - quantity: proportion oscillating faster than theta, Passive 1\n    value: 0.383\n    tolerance: 0.038\n  - quantity: proportion oscillating faster than theta, Active\n    value: 0.6\n    tolerance: 0.06\n  - quantity: proportion oscillating faster than theta, Passive 2\n    value: 0.467\n    tolerance: 0.047\n  - quantity: proportion significantly phase precessing, Passive 1\n    value: 0.149\n    tolerance: 0.015\n  - quantity: proportion significantly phase precessing, Active\n    value: 0.353\n    tolerance: 0.035\n  - quantity: proportion significantly phase precessing, Passive 2\n    value: 0.156\n    tolerance: 0.016\n  criterion: Oscillating faster than theta is a spectral mode above 1 cycle^-1 (as in\n    fig2cd-spike-bursts-slower); the denominator is all place cells of the condition, as\n    the legend's fractions show. Significant precession is a significant linear-circular\n    regression of in-field spike phase on linearized position (Methods, Theta asymmetry\n    and phase precession; ref. 43), at p < 0.05, a level the paper does not state but\n    the usual one. The figure marks the Active proportions as differing, by the binomial\n    proportion test of the Methods. Reproduced when at least five of the six proportions\n    are within tolerance and Active exceeds both passive conditions by binomial\n    proportion tests at P < 0.05 for both measures.\n- id: fig2f-phase-precession-degraded\n  statement: The distribution of phase precession slopes over all place cells differed\n    between passive and active travel, indicating an overall degradation of phase\n    precession in passive travel.\n  source: Fig. 2E and 2F and legend; Results, paragraph 6\n  quote: Distribution of phase precession slopes for all place cells (Kolmogorov-Smirnov\n    test, **P < 0.008, *P < 0.04; colored dashed vertical lines are medians)\n  statistics:\n  - about: one pair of conditions\n    test: Kolmogorov-Smirnov\n    p: 0.008\n    p_relation: \"<\"\n  - about: the other pair of conditions\n    test: Kolmogorov-Smirnov\n    p: 0.04\n    p_relation: \"<\"\n  depends_on:\n  - figs2b-place-cell-count\n  criterion: Slope of the linear-circular regression of in-field spike phase on position\n    normalized to field size (rad per field size), for every place cell (Methods, Theta\n    asymmetry and phase precession). Two-sample KS tests. The legend does not say which\n    pairs; readings are (a) Passive 1 against Active and Active against Passive 2, in\n    either assignment of the two P values. Reproduced when both Active comparisons reach\n    P < 0.04 and one reaches P < 0.008, with the Active median slope more negative than\n    both passive medians; partially reproduced when one comparison is significant at 0.05.\n- id: figs4de-precession-range-similar\n  statement: Among significantly phase-precessing cells, phase precession range and slopes\n    did not differ between passive and active travel (Kruskal-Wallis and KS tests, P >\n    0.05).\n  source: fig. S4C to S4E and legend; Results, paragraph 6\n  quote: in phase-precessing neurons, phase range was similar in all conditions (26) (fig.\n    S4, C to E)\n  statistics:\n  - about: precession range\n    test: Kruskal-Wallis\n    p: 0.05\n    p_relation: \">\"\n  - about: distributions of significant slopes\n    test: Kolmogorov-Smirnov\n    p: 0.05\n    p_relation: \">\"\n  - about: median significant slopes\n    test: Kruskal-Wallis\n    p: 0.05\n    p_relation: \">\"\n  depends_on:\n  - figs4b-proportions-oscillating-precessing\n  criterion: A claim of absence, on significantly precessing cells only. Range is the phase\n    change over the field from the regression (slope times normalized field size, in\n    degrees per field size, as fig. S4D's axis), following ref. 26 as the paper cites\n    it. Kruskal-Wallis across conditions for range and for slope, and KS tests between\n    pairs of conditions for slopes. Reproduced when none of these tests gives P < 0.05;\n    not reproduced when any does. Effect sizes reported.\n- id: fig3b-average-theta-reconstruction\n  statement: Averaged over all theta cycles of all rats, the reconstruction of position\n    across theta phase had trajectory score 0.17 and slope 6 cm/cycle in Passive 1, 0.23\n    and 48 cm/cycle in Active, and 0.19 and 21 cm/cycle in Passive 2.\n  source: Fig. 3B and legend; Results, paragraph 8\n  quote: This was confirmed over all theta cycles for all rats (Fig. 3B and fig. S5)\n  expected:\n  - quantity: average reconstruction trajectory score, Passive 1\n    value: 0.17\n    tolerance: 0.017\n  - quantity: average reconstruction trajectory score, Active\n    value: 0.23\n    tolerance: 0.023\n  - quantity: average reconstruction trajectory score, Passive 2\n    value: 0.19\n    tolerance: 0.019\n  - quantity: average reconstruction slope, Passive 1\n    value: 6\n    tolerance: 3\n    unit: cm/cycle\n  - quantity: average reconstruction slope, Active\n    value: 48\n    tolerance: 4.8\n    unit: cm/cycle\n  - quantity: average reconstruction slope, Passive 2\n    value: 21\n    tolerance: 3\n    unit: cm/cycle\n  criterion: The assignment of the three printed pairs to Passive 1, Active and Passive 2\n    is read from the panel order, the same order as the matching panels of figs. S7A, S8A\n    and S9A. Decoded probabilities per phase window centred on the animal's position and\n    averaged over cycles (Methods, Bayesian trajectory decoding, paragraph 2), then scored\n    over the averaged cycle (Common methods, Trajectory score). Every slope the paper\n    prints for these averages is a multiple of 3 cm/cycle, so the slope grid moves in\n    steps of 3; the tolerance for the two smaller slopes is one step, where 10% would be\n    below it. Reproduced when at least five of the six values are within tolerance and\n    Active has the highest score and slope.\n- id: figs5b-per-rat-reconstruction\n  statement: Across the five rats, the trajectory scores, slopes and quadrant scores of the\n    average theta reconstructions differed between conditions (repeated-measures ANOVA, P\n    = 0.008, 0.007 and 0.004), higher in Active.\n  source: fig. S5A and S5B\n  inferred: The P values are printed only inside fig. S5B, whose legend says only that it\n    shows the scores, slopes and quadrant scores of the reconstructions in (A); the order\n    of the three P values follows the panel order in the extracted text, and higher in\n    Active is read from the per-rat values of fig. S5A.\n  statistics:\n  - about: trajectory score\n    test: repeated measures ANOVA\n    p: 0.008\n    n: 5 rats\n  - about: slope\n    test: repeated measures ANOVA\n    p: 0.007\n    n: 5 rats\n  - about: quadrant score\n    test: repeated measures ANOVA\n    p: 0.004\n    n: 5 rats\n  depends_on:\n  - fig3b-average-theta-reconstruction\n  criterion: Per rat and condition, the average reconstruction as in\n    fig3b-average-theta-reconstruction, its trajectory score and slope, and the quadrant\n    score (Common methods). Repeated-measures ANOVA across conditions over the 5 rats for\n    each. Reproduced when all three give P < 0.05 with the Active mean highest; partially\n    reproduced for two of three.\n- id: fig3c-theta-scores-above-chance\n  statement: Normalized trajectory scores of theta sequences were better than chance in all\n    three conditions, and differed between conditions (Kruskal-Wallis, P < 10^-23).\n  source: Fig. 3C, left, and legend; Results, paragraph 8\n  quote: Whereas normalized trajectory scores were significantly better than chance in all\n    conditions (Fig. 3C)\n  statistics:\n  - about: across conditions\n    test: Kruskal-Wallis\n    p: 1.0e-23\n    p_relation: \"<\"\n  - about: post hoc comparisons\n    test: Wilcoxon rank-sum\n    p: 0.00033\n    p_relation: \"<\"\n    corrected: Bonferroni\n  criterion: Normalized score of every theta-cycle candidate event (Common methods,\n    Trajectory score), pooled over rats. Better than chance is a median normalized score\n    above 0 by a Wilcoxon signed-rank test (Methods, statistics) in each condition.\n    Kruskal-Wallis across conditions and post hoc rank-sum tests with Bonferroni\n    correction. Reproduced when all three signed-rank tests give P < 0.05 with medians\n    above 0 and the Kruskal-Wallis gives P < 10^-10; partially reproduced when the\n    above-chance tests hold and the Kruskal-Wallis is significant at 0.05 only. Which\n    pairs differ, and in which direction, is reported.\n- id: fig3c-proportion-significant-theta\n  statement: The proportion of significant theta sequences (significant score, positive\n    slope) was 7.95% in Passive 1, 13.61% in Active and 9.05% in Passive 2, each above\n    shuffled control, and Active exceeded both passive conditions.\n  source: Fig. 3C, right, and legend; Methods, Assessing trajectories, paragraph 4\n  quote: Proportion of significant theta sequences (Passive 1; 7.95%, Active; 13.61%,\n    Passive 2; 9.05%; all proportions are significantly greater than shuffled control\n    proportions, Monte Carlo test, P ~ 0; binomial proportion tests, *P < 0.05, ***P <\n    0.001)\n  statistics:\n  - about: each proportion against shuffled control proportions\n    test: Monte Carlo test\n    p: 0\n  - about: between conditions\n    test: binomial proportion test\n    p: 0.001\n    p_relation: \"<\"\n  expected:\n  - quantity: significant theta sequences, Passive 1\n    value: 7.95\n    tolerance: 0.795\n    unit: percent\n  - quantity: significant theta sequences, Active\n    value: 13.61\n    tolerance: 1.361\n    unit: percent\n  - quantity: significant theta sequences, Passive 2\n    value: 9.05\n    tolerance: 0.905\n    unit: percent\n  - quantity: significant theta sequences without slope restriction, Passive 1\n    value: 14.66\n    tolerance: 1.466\n    unit: percent\n  - quantity: significant theta sequences without slope restriction, Active\n    value: 20.20\n    tolerance: 2.02\n    unit: percent\n  - quantity: significant theta sequences without slope restriction, Passive 2\n    value: 16.37\n    tolerance: 1.637\n    unit: percent\n  criterion: Events with Monte Carlo p <= 0.05 and positive slope, over all analysed theta\n    cycles pooled over rats (Methods, Assessing trajectories, paragraph 4); the\n    unrestricted proportions count significant events of any slope. Each against the\n    proportion of shuffled events passing the same rule. Binomial proportion tests between\n    conditions. The legend marks one pair at *P < 0.05 and others at P < 0.001; read as\n    Active against each passive condition at P < 0.001 and Passive 1 against Passive 2 at\n    P < 0.05. Reproduced when at least four of the six values are within tolerance, all\n    proportions exceed the shuffled ones, and Active exceeds both passive conditions at P\n    < 0.001; partially reproduced when the order and tests hold but fewer values match.\n- id: fig3d-theta-slopes-steeper-active\n  statement: Slopes of significant theta sequences were steeper during active travel than\n    in either passive condition, while the two passive conditions did not differ.\n  source: Fig. 3D and legend; fig. S5C and S5D; Results, paragraph 8\n  quote: slopes were significantly steeper during active travel (Fig. 3D and fig. S5, C and\n    D)\n  statistics:\n  - about: slope distributions, Passive 1 against Active\n    test: Kolmogorov-Smirnov\n    p: 1.0e-16\n    p_relation: \"<\"\n  - about: slope distributions, Active against Passive 2\n    test: Kolmogorov-Smirnov\n    p: 1.0e-18\n    p_relation: \"<\"\n  - about: slope distributions, Passive 1 against Passive 2\n    test: Kolmogorov-Smirnov\n    p: 0.05\n    p_relation: \">\"\n  - about: significant slopes across conditions\n    test: Kruskal-Wallis\n    p: 1.0e-20\n    p_relation: \"<\"\n  depends_on:\n  - fig3c-proportion-significant-theta\n  criterion: Slopes in m/s (Common methods, Trajectory score; both conversion readings) of\n    the theta sequences with significant scores. Signed slope distributions compared by\n    two-sample KS tests; slopes across conditions by Kruskal-Wallis. Whether fig. S5D uses\n    signed or absolute slopes is open; both are shown. Reproduced when both Active\n    comparisons give P < 10^-6 with the Active median higher, and Passive 1 against\n    Passive 2 gives P > 0.05 (a claim of absence on the paper's KS test); partially\n    reproduced when the Active comparisons hold at 0.001 only or the passive pair differs.\n- id: fig3e-joint-score-slope-theta\n  statement: Joint analysis of trajectory scores and slopes showed a much greater\n    proportion of high-score, high-slope theta sequences during active travel.\n  source: Fig. 3E and legend; Results, paragraph 8\n  quote: Joint analysis of trajectory scores and slopes revealed a much greater proportion\n    of high-value pairs during active travel (Fig. 3E)\n  depends_on:\n  - fig3c-proportion-significant-theta\n  criterion: The z-proportion matrix per condition (Common methods, Z-proportions), events\n    pooled over rats. High-value pairs are not defined; read as cells with trajectory score\n    above the 95th percentile of the pooled shuffled scores and positive slope above 3\n    m/s (the slope sign of forward theta sequences). Reproduced when, under each bin-size\n    reading, the summed positive z-proportion of that region is larger in Active than in\n    each passive condition, and the proportion of events in that region is higher in\n    Active by a binomial proportion test at P < 0.05.\n- id: fig3f-quadrant-scores\n  statement: Quadrant scores of theta cycles were greater during active travel, remained\n    very low in passive travel, and were higher in Passive 2 than in Passive 1\n    (Kruskal-Wallis, P < 10^-24).\n  source: Fig. 3F and legend; Results, paragraphs 8 and 9\n  quote: Quadrant scores were significantly greater for active travel (clear trajectories)\n    and remained very low for passive travel (degraded trajectories) (Fig. 3F and fig.\n    S5B). ... Note that reconstruction quality and quadrant scores were higher in Passive 2\n    than in Passive 1 (Fig. 3, E and F)\n  statistics:\n  - about: across conditions\n    test: Kruskal-Wallis\n    p: 1.0e-24\n    p_relation: \"<\"\n  - about: post hoc comparisons\n    test: Wilcoxon rank-sum\n    p: 0.00033\n    p_relation: \"<\"\n    corrected: Bonferroni\n  - about: the weakest post hoc comparison, read as Passive 1 against Passive 2\n    test: Wilcoxon rank-sum\n    p: 0.017\n    p_relation: \"<\"\n    corrected: Bonferroni\n  criterion: Quadrant score per theta cycle (Common methods), pooled over rats.\n    Kruskal-Wallis and post hoc rank-sum tests with Bonferroni correction. Reproduced when\n    the Kruskal-Wallis gives P < 10^-10, Active exceeds both passive conditions at\n    0.001/3, and Passive 2 exceeds Passive 1 at 0.05/3; partially reproduced when Active is\n    highest at 0.05/3 but Passive 2 does not exceed Passive 1.\n- id: fig3g-theta-self-consistency\n  statement: Theta sequences were most self-consistent in Active, more so in Passive 2 than\n    in Passive 1, with no consistency in Passive 1 and progressive decay during Passive 2.\n  source: Fig. 3G and legend; fig. S6A and legend; Results, paragraph 9\n  quote: This was further supported by higher self-consistency of theta sequences (31) in\n    Passive 2 than in Passive 1, whereas Active sequences were the most self-consistent\n    (Fig. 3G and fig. S6A).\n  statistics:\n  - about: proportion of significantly correlated sequence pairs between conditions\n    test: binomial proportion test\n    p: 0.001\n    p_relation: \"<\"\n  criterion: Pairwise bias correlations between theta sequences of the same condition\n    (Common methods, Pairwise bias correlation), both sequence readings. Per condition, the\n    mean correlation over pairs (compared by Kruskal-Wallis, as fig. S6A names) and the\n    proportion of significantly correlated pairs (binomial proportion tests). Reproduced\n    when the proportion is highest in Active and higher in Passive 2 than Passive 1, with\n    those differences at P < 0.001, and the Kruskal-Wallis is significant at 0.05. The\n    20-bin matrices of Fig. 3G are reported, with the Passive 1 mean correlation and its\n    Wilcoxon signed-rank test against 0.\n- id: figs7-control-cell-count\n  statement: With Active and Passive 2 restricted to random subsets matching the Passive 1\n    place-cell count, theta sequences were still degraded in passive travel; slopes,\n    normalized scores and quadrant scores still differed.\n  source: fig. S7 and legend; Methods, Bayesian trajectory decoding, control (i)\n  quote: Reduced cell count does not account for theta sequence degradation during passive\n    travel.\n  statistics:\n  - about: slopes, Passive 1 against Active\n    test: Kolmogorov-Smirnov\n    p: 1.0e-13\n    p_relation: \"<\"\n  - about: slopes, Active against Passive 2\n    test: Kolmogorov-Smirnov\n    p: 1.0e-43\n    p_relation: \"<\"\n  - about: slopes, Passive 1 against Passive 2\n    test: Kolmogorov-Smirnov\n    p: 0.05\n    p_relation: \">\"\n  - about: slopes of significant sequences\n    test: Kruskal-Wallis\n    p: 1.0e-39\n    p_relation: \"<\"\n  - about: normalized score\n    test: Kruskal-Wallis\n    p: 1.0e-09\n    p_relation: \"<\"\n  - about: quadrant score\n    test: Kruskal-Wallis\n    p: 1.0e-75\n    p_relation: \"<\"\n  depends_on:\n  - fig3d-theta-slopes-steeper-active\n  - fig3f-quadrant-scores\n  criterion: Per rat, random subsets of Active and Passive 2 place cells matching the\n    Passive 1 count, 30 repetitions, up to 300 theta cycles per subset (Methods, control\n    (i)); the analyses of Fig. 3D, 3C and 3F repeated. Reproduced when the Active\n    comparisons of slopes give P < 10^-6 with Active steeper, the Kruskal-Wallis tests of\n    score and quadrant score give P < 10^-6 with Active highest, and Passive 1 against\n    Passive 2 slopes gives P > 0.05; partially reproduced when the Active effects hold at\n    0.001 only.\n- id: figs8-control-firing-rate\n  statement: With Active and Passive 2 spikes downsampled to match the Passive 1 median\n    firing rate, theta sequences were still degraded in passive travel.\n  source: fig. S8 and legend; Methods, Bayesian trajectory decoding, control (ii)\n  quote: Reduced firing rate does not account for theta sequence degradation during passive\n    travel.\n  statistics:\n  - about: slopes, Passive 1 against Active\n    test: Kolmogorov-Smirnov\n    p: 1.0e-09\n    p_relation: \"<\"\n  - about: slopes, Active against Passive 2\n    test: Kolmogorov-Smirnov\n    p: 1.0e-09\n    p_relation: \"<\"\n  - about: slopes, Passive 1 against Passive 2\n    test: Kolmogorov-Smirnov\n    p: 0.1\n    p_relation: \">\"\n  - about: slopes of significant sequences\n    test: Kruskal-Wallis\n    p: 1.0e-11\n    p_relation: \"<\"\n  - about: normalized score\n    test: Kruskal-Wallis\n    p: 1.0e-10\n    p_relation: \"<\"\n  - about: quadrant score\n    test: Kruskal-Wallis\n    p: 1.0e-07\n    p_relation: \"<\"\n  - about: firing rates after downsampling\n    test: Kruskal-Wallis\n    p: 0.9\n    p_relation: \">\"\n  expected:\n  - quantity: place-cell firing rate after downsampling, Passive 1\n    value: 0.905\n    tolerance: 0.145\n    unit: Hz\n  - quantity: place-cell firing rate after downsampling, Active\n    value: 0.933\n    tolerance: 0.083\n    unit: Hz\n  - quantity: place-cell firing rate after downsampling, Passive 2\n    value: 0.829\n    tolerance: 0.130\n    unit: Hz\n  depends_on:\n  - fig3d-theta-slopes-steeper-active\n  - fig3f-quadrant-scores\n  criterion: Tolerances are the spread the fig. S8F legend gives. Per rat, spikes of the\n    most active Active and Passive 2 place cells randomly removed until the median rate is\n    below the Passive 1 median (Methods, control (ii); fig. S8 legend). Which rate is\n    matched is open; readings (a) mean rate over the travel session, (b) peak in-field\n    rate. Reproduced when the Active effects (slopes, score, quadrant score) hold at P <\n    10^-6, Passive 1 against Passive 2 slopes gives P > 0.1, and the rate comparison gives\n    P > 0.05; partially reproduced when the Active effects hold at 0.001 only.\n- id: figs9-control-decoding-quality\n  statement: With passive-travel theta cycles restricted to low decoding-error periods\n    matching Active, slopes and quadrant scores still differed between conditions,\n    while normalized scores no longer did (Kruskal-Wallis, P > 0.05).\n  source: fig. S9 and legend; Methods, Bayesian trajectory decoding, control (iii)\n  quote: Reduced decoding quality cannot account for theta sequence degradation during\n    passive travel.\n  statistics:\n  - about: slopes, Passive 1 against Active\n    test: Kolmogorov-Smirnov\n    p: 1.0e-09\n    p_relation: \"<\"\n  - about: slopes, Active against Passive 2\n    test: Kolmogorov-Smirnov\n    p: 1.0e-16\n    p_relation: \"<\"\n  - about: slopes, Passive 1 against Passive 2\n    test: Kolmogorov-Smirnov\n    p: 0.05\n    p_relation: \">\"\n  - about: slopes of significant sequences\n    test: Kruskal-Wallis\n    p: 1.0e-15\n    p_relation: \"<\"\n  - about: normalized score\n    test: Kruskal-Wallis\n    p: 0.05\n    p_relation: \">\"\n  - about: quadrant score\n    test: Kruskal-Wallis\n    p: 1.0e-16\n    p_relation: \"<\"\n  expected:\n  - quantity: decoding error after restriction, Passive 1\n    value: 0.802\n    tolerance: 0.018\n  - quantity: decoding error after restriction, Active\n    value: 0.80\n    tolerance: 0.023\n  - quantity: decoding error after restriction, Passive 2\n    value: 0.802\n    tolerance: 0.014\n  depends_on:\n  - fig3d-theta-slopes-steeper-active\n  - fig3f-quadrant-scores\n  criterion: Tolerances are the spread the fig. S9F legend gives; the unit of the error is\n    not printed and is read as metres (fig. S9F axis \"Error (m)\"). Reconstruction errors\n    in 500 ms bins per condition; high-error bins progressively excluded in Passive 1 and\n    Passive 2 until their median error is below the Active median; theta cycles in the kept\n    bins decoded (Methods, control (iii)). Open is the order of exclusion; read as the\n    highest-error bin first. Reproduced when the Active effects on slopes and quadrant\n    scores hold at P < 10^-6, the normalized-score Kruskal-Wallis gives P > 0.05 (absence,\n    on the paper's test), and the errors are within tolerance; partially reproduced when\n    the Active effects hold at 0.001 only or the normalized scores differ.\n- id: figs10-control-lap-variability\n  statement: With the decoder retrained on each lap, theta sequences were still degraded in\n    passive travel.\n  source: fig. S10 and legend; Methods, Bayesian trajectory decoding, control (iv)\n  quote: Trial-to-trial field variability does not account for theta sequence degradation\n    during passive travel.\n  statistics:\n  - about: slopes, Passive 1 against Active\n    test: Kolmogorov-Smirnov\n    p: 1.0e-12\n    p_relation: \"<\"\n  - about: slopes, Active against Passive 2\n    test: Kolmogorov-Smirnov\n    p: 1.0e-13\n    p_relation: \"<\"\n  - about: slopes, Passive 1 against Passive 2\n    test: Kolmogorov-Smirnov\n    p: 0.05\n    p_relation: \">\"\n  - about: slopes of significant sequences\n    test: Kruskal-Wallis\n    p: 1.0e-18\n    p_relation: \"<\"\n  - about: normalized score\n    test: Kruskal-Wallis\n    p: 1.0e-27\n    p_relation: \"<\"\n  - about: quadrant score\n    test: Kruskal-Wallis\n    p: 1.0e-09\n    p_relation: \"<\"\n  depends_on:\n  - fig3d-theta-slopes-steeper-active\n  - fig3f-quadrant-scores\n  criterion: The decoder trained on each lap and applied to that lap's theta cycles\n    (Methods, control (iv)). Open is whether a lap is decoded from its own firing curves\n    or from those of the other laps; readings (a) its own lap, as the text reads, (b)\n    the other laps. Reproduced when the Active effects on slopes, scores and quadrant\n    scores hold at P < 10^-6 and Passive 1 against Passive 2 slopes gives P > 0.05;\n    partially reproduced when the Active effects hold at 0.001 only.\n- id: figs11-sleep-sessions-similar\n  statement: SWS duration, number and rate of candidate events and ripple rate did not\n    differ between sleep sessions (repeated-measures ANOVA, P > 0.05), and candidate events\n    coincided with ripples alike in all sessions (KS, P > 0.05).\n  source: fig. S11 and legend; Results, paragraph 11\n  quote: The average SWS duration, number and rate of candidate events, and ripple\n    occurrence rate were not significantly different across animals (fig. S11, B and D to\n    F)\n  statistics:\n  - about: SWS duration\n    test: repeated measures ANOVA\n    p: 0.05\n    p_relation: \">\"\n  - about: number of candidate events, their frequency, ripple rates\n    test: repeated measures ANOVA\n    p: 0.05\n    p_relation: \">\"\n  - about: timing of candidate events relative to ripple peaks, between all pairs of\n      conditions\n    test: Kolmogorov-Smirnov\n    p: 0.05\n    p_relation: \">\"\n  criterion: The main text says across animals; the legend says between sleep conditions;\n    the legend's comparison (rats as subjects, conditions as the factor) is the one tested.\n    SWS, candidate events and ripples as in Common methods, per rat and sleep session.\n    Fig. S11B includes baseline sleep, fig. S11D to F only the three post-travel sessions.\n    A claim of absence on the paper's tests. Reproduced when none of the four ANOVAs and\n    none of the KS tests of event-to-ripple-peak times gives P < 0.05; not reproduced when\n    any does. The fraction of candidate events within 0.1 s of a ripple peak is reported.\n- id: fig4b-replay-scores-vs-baseline\n  statement: Replay trajectory scores, relative to baseline sleep, were improved only in\n    sleep after Active and after Passive 2 (Kruskal-Wallis, P < 10^-17).\n  source: Fig. 4B and legend; Results, paragraph 12\n  quote: scores were significantly improved relative to baseline (31) only in sleep sessions\n    following Active and Passive 2 (Fig. 4B)\n  statistics:\n  - about: across conditions\n    test: Kruskal-Wallis\n    p: 1.0e-17\n    p_relation: \"<\"\n  - about: post hoc comparisons\n    test: Wilcoxon rank-sum\n    p: 0.00033\n    p_relation: \"<\"\n    corrected: Bonferroni\n  - about: comparisons other than post hoc\n    p: 0.001\n    p_relation: \"<\"\n  depends_on:\n  - figs11-sleep-sessions-similar\n  criterion: Per rat, each post-sleep candidate event's trajectory score relative to\n    baseline sleep as (score - median baseline score) / (third - first quartile of baseline\n    scores), baseline events decoded with the same travel model; pooled over rats\n    (Methods, Assessing trajectories, paragraph 3). Improved relative to baseline is a\n    median above 0 by a Wilcoxon signed-rank test (Methods, statistics). Reproduced when\n    the medians after Active and after Passive 2 are above 0 at P < 0.01, the median after\n    Passive 1 is not above 0 at P < 0.05, and the Kruskal-Wallis across the three sessions\n    gives P < 10^-6; partially reproduced when after-Active alone is above 0 at P < 0.05.\n- id: fig4c-replay-slopes-steeper-active\n  statement: Replay slopes were steeper in sleep after Active than after either passive\n    travel, while sleep after Passive 1 and Passive 2 did not differ.\n  source: Fig. 4C and legend; fig. S13B and legend; Results, paragraph 12\n  quote: In addition, slopes were significantly steeper following Active (Fig. 4C and fig.\n    S13B).\n  statistics:\n  - about: absolute slopes across sleep sessions\n    test: Kruskal-Wallis\n    p: 1.0e-27\n    p_relation: \"<\"\n  - about: slope distributions, sleep after Passive 1 against after Active\n    test: Kolmogorov-Smirnov\n    p: 1.0e-08\n    p_relation: \"<\"\n  - about: slope distributions, sleep after Active against after Passive 2\n    test: Kolmogorov-Smirnov\n    p: 1.0e-06\n    p_relation: \"<\"\n  - about: slope distributions, sleep after Passive 1 against after Passive 2\n    test: Kolmogorov-Smirnov\n    p: 0.05\n    p_relation: \">\"\n  depends_on:\n  - figs11-sleep-sessions-similar\n  criterion: Slopes in m/s of the candidate events of each post-travel sleep session\n    (Common methods, Trajectory score; 20 ms windows). Fig. 4C uses absolute slopes;\n    whether all events or only those with significant scores is open, and both are run\n    (fig. S13 shows significant events). Reproduced when the Kruskal-Wallis gives P <\n    10^-10 with sleep after Active highest, both Active KS comparisons give P < 10^-4, and\n    the passive pair gives P > 0.05; partially reproduced when the Active effect holds at\n    0.001 only.\n- id: fig4d-joint-score-slope-replay\n  statement: Joint analysis of replay trajectory scores and slopes showed a much greater\n    proportion of high-score, high-slope events in sleep after Active.\n  source: Fig. 4D and legend; fig. S13C and S13D; Results, paragraph 12\n  quote: Joint analysis of trajectory scores and slopes confirmed a much greater proportion\n    of high-value pairs after active travel\n  depends_on:\n  - fig4c-replay-slopes-steeper-active\n  criterion: As fig3e-joint-score-slope-theta, on candidate events of each post-travel\n    sleep session, with high-value cells read as score above the 95th percentile of the\n    shuffled scores and absolute slope above 3 m/s (replay runs in both directions). The\n    proportion ratio of fig. S13D (Methods, Z-proportions and proportion ratios) is shown\n    as well. Reproduced when, under each bin-size reading, the summed positive\n    z-proportion of that region is largest after Active and the proportion of events in it\n    is higher after Active than after each passive travel by a binomial proportion test at\n    P < 0.05.\n- id: fig4e-replay-proportion-vs-baseline\n  statement: Relative to baseline sleep, the proportion of significant replay events was\n    not increased after Passive 1, was boosted after Active, and was intermediate but\n    significantly increased after Passive 2.\n  source: Fig. 4E and legend; Results, paragraph 13\n  quote: We did not observe replay during sleep following Passive 1 (Fig. 4E) ... Trajectory\n    replay was then boosted in sleep following Active (Fig. 4E) ... an intermediate but\n    significant level of reactivation was observed following Passive 2 (Fig. 4E)\n  statistics:\n  - about: post-sleep against baseline proportions\n    test: binomial proportion test\n    p: 0.001\n    p_relation: \"<\"\n  - about: the weaker significant comparison\n    test: binomial proportion test\n    p: 0.01\n    p_relation: \"<\"\n  depends_on:\n  - figs11-sleep-sessions-similar\n  criterion: Proportion of candidate events with Monte Carlo p <= 0.05 in each post-travel\n    sleep session and in baseline sleep decoded with the same travel model, pooled over\n    rats; the ratio post / baseline as plotted, and binomial proportion tests of post\n    against baseline (Methods, statistics). Whether a positive slope is also required, as\n    for theta sequences, is open; readings (a) significant score only, (b) significant\n    score and slope above 0. Which of the legend's two levels goes with which comparison\n    is not printed; read as after Active against baseline at P < 0.001 and after Passive 2\n    against baseline at P < 0.01, with the after-Active ratio largest. For Passive 1, a\n    claim of absence on the paper's binomial test. Reproduced when, under one reading,\n    after Passive 1 is not different from baseline (P >= 0.05), after Active is higher at\n    P < 0.001, after Passive 2 is higher at P < 0.01, and the after-Active ratio is largest.\n- id: fig4f-forward-replay-after-active\n  statement: Forward and reverse replay events were equally common in sleep after passive\n    travel, while sleep after Active held more forward than reverse events.\n  source: Fig. 4F and legend; Results, paragraph 13\n  quote: Although forward and backward trajectories were found in equal proportions during\n    sleep after passive travel, only active travel resulted in a greater proportion of\n    forward replay actually reflecting awake experience (Fig. 4F).\n  statistics:\n  - test: binomial proportion test\n    p: 0.001\n    p_relation: \"<\"\n  depends_on:\n  - fig4e-replay-proportion-vs-baseline\n  criterion: Among significant replay events of each post-travel session, forward events\n    have a positive slope (the train always moved forward along the linearized track;\n    Methods, Animal training) and reverse events a negative one. The binomial proportion\n    test compares the forward and reverse proportions; the comparison is open, readings\n    (a) forward against reverse proportion within the session (equivalently against 0.5),\n    (b) the session's forward proportion against baseline sleep's. Reproduced when, under\n    one reading, after Active forward exceeds reverse at P < 0.001 and after both passive\n    travels the test finds no difference (P >= 0.05, absence on the paper's test).\n- id: fig4g-theta-replay-correlation-active\n  statement: Theta sequences correlated selectively with candidate replay events in the\n    sleep that followed them only for Active.\n  source: Fig. 4G and legend; fig. S6B and S6C and legend; Results, paragraph 13\n  quote: a direct comparison of theta and replay sequences (31) highlighted a selective ...\n    correlation between theta sequences in Active and candidate replay events in\n    subsequent sleep (Fig. 4G and fig. S6, B and C)\n  statistics:\n  - about: proportion of significantly correlated theta-replay pairs\n    test: binomial proportion test\n    p: 0.001\n    p_relation: \"<\"\n  depends_on:\n  - fig3g-theta-self-consistency\n  criterion: Pairwise bias correlations between theta sequences of each travel session and\n    candidate events of its post-sleep, and of baseline sleep (Common methods, Pairwise\n    bias correlation; fig. S6B and S6C). Reproduced when the proportion of significantly\n    correlated pairs Active-post-Active exceeds Active-baseline at P < 0.001 by a binomial\n    proportion test while neither passive session's pairs with its post-sleep exceed its\n    pairs with baseline at P < 0.05; partially reproduced when the Active effect holds at\n    0.05 only. Mean correlations, compared by Kruskal-Wallis as fig. S6 names, are\n    reported.\n- id: figs12-ripple-restricted\n  statement: Restricting candidate events to ripples left the replay results unchanged;\n    scores relative to baseline, slopes, the boost after Active and the forward bias after\n    Active all held.\n  source: fig. S12 and legend; Results, paragraph 11\n  quote: results remained unchanged when candidate events were restricted to ripples (fig.\n    S12)\n  statistics:\n  - about: scores relative to baseline\n    test: Kruskal-Wallis\n    p: 1.0e-15\n    p_relation: \"<\"\n  - about: slopes, sleep after Passive 1 against after Active\n    test: Kolmogorov-Smirnov\n    p: 1.0e-05\n    p_relation: \"<\"\n  - about: slopes, sleep after Active against after Passive 2\n    test: Kolmogorov-Smirnov\n    p: 1.0e-05\n    p_relation: \"<\"\n  - about: slopes, sleep after Passive 1 against after Passive 2\n    test: Kolmogorov-Smirnov\n    p: 0.05\n    p_relation: \">\"\n  - about: absolute slopes\n    test: Kruskal-Wallis\n    p: 1.0e-27\n    p_relation: \"<\"\n  depends_on:\n  - fig4b-replay-scores-vs-baseline\n  - fig4c-replay-slopes-steeper-active\n  - fig4e-replay-proportion-vs-baseline\n  - fig4f-forward-replay-after-active\n  criterion: Candidate events kept only when they overlap a detected ripple (Common methods,\n    Ripples); the analyses of Fig. 4B, 4C, 4E and 4F repeated. Restricted to ripples is\n    open; readings (a) any overlap with a ripple, (b) the event's peak inside a ripple.\n    Reproduced when the four claims' criteria hold on the restricted events, with the\n    p-value bounds of this legend in place of theirs; partially reproduced when two or\n    three do.\n"
}
```

```
File created successfully at: claims/drieu-2018.yaml (file state is current in your context — no need to Read it back)
```

**Agent**

I replaced colons inside four quotes, which breaks the word-for-word rule. Fixing them with single-quoted scalars.

**Agent calls Bash**

```bash
cd  python - <<'EOF'
p='claims/drieu-2018.yaml'
s=open(p).read()
rep={
"""  quote: Firing fields did not remap between Passive 1 and Active. Left; Mean unsigned
    proportional shift s (vertical gray line; **P < 0.01) and s distribution for n = 2000
    bootstrapped remapping data sets""":
"""  quote: 'Firing fields did not remap between Passive 1 and Active. Left: Mean unsigned
    proportional shift s (vertical gray line; **P < 0.01) and s distribution for n = 2000
    bootstrapped remapping data sets'""",
"""  quote: Firing fields also did not remap between Active and Passive 2. Data are displayed as
    in (D). Left; ***P ~ 0. Inset; Rayleigh test, P < 10–9; V-test against 0, P < 10–10.""":
"""  quote: 'Firing fields also did not remap between Active and Passive 2. Data are displayed as
    in (D). Left: ***P ~ 0. Inset: Rayleigh test, P < 10–9; V-test against 0, P < 10–10.'""",
"""  quote: Proportion of place cells oscillating faster than theta frequency (top, Passive 1;
    36/94, Active; 90/150, Passive 2; 63/135) and proportion of significant phase-precessing
    cells (bottom, Passive 1; 14/94, Active; 53/150, Passive 2; 21/135)""":
"""  quote: 'Proportion of place cells oscillating faster than theta frequency (top, Passive 1:
    36/94, Active: 90/150, Passive 2: 63/135) and proportion of significant phase-precessing
    cells (bottom, Passive 1: 14/94, Active: 53/150, Passive 2: 21/135)'""",
"""  quote: Proportion of significant theta sequences (Passive 1; 7.95%, Active; 13.61%,
    Passive 2; 9.05%; all proportions are significantly greater than shuffled control
    proportions, Monte Carlo test, P ~ 0; binomial proportion tests, *P < 0.05, ***P <
    0.001)""":
"""  quote: 'Proportion of significant theta sequences (Passive 1: 7.95%, Active: 13.61%,
    Passive 2: 9.05%; all proportions are significantly greater than shuffled control
    proportions, Monte Carlo test, P ~ 0; binomial proportion tests, *P < 0.05, ***P <
    0.001)'""",
"""while the paper reports five rats throughout; five is taken as the count.""":
"""while the paper reports five rats throughout; five is taken as the count.""",
"""# P < 10^-10 (manuscript 10^-11). The Data analysis section of the Methods says that the
# acquisition paragraph covers "three rats" with tetrodes and "three rats" with octrodes,""":
"""# P < 10^-10 (manuscript 10^-11). The Methods' Data acquisition paragraph describes
# "three rats" with tetrodes and "three rats" with octrodes,""",
}
for a,b in rep.items():
    assert a in s, a[:60]
    s=s.replace(a,b)
open(p,'w').write(s)
EOF
grep -n "—\|rather" claims/drieu-2018.yaml; python tools/claims_check.py claims/drieu-2018.yaml paper/10.1126-science.aat2952.txt
```

Result: not kept, because it reads the paper's text.

**Agent**

Checker passes. Now I check that no plain scalar contains a colon followed by a space, and count the claims with criteria.

**Agent calls Bash**

```bash
cd  python - <<'EOF'
import yaml
n=yaml.compose(open('claims/drieu-2018.yaml'))
bad=[]
def walk(x):
    if isinstance(x,yaml.ScalarNode):
        if x.style is None and ': ' in x.value: bad.append(x.value[:80])
    elif isinstance(x,yaml.SequenceNode):
        for i in x.value: walk(i)
    elif isinstance(x,yaml.MappingNode):
        for k,v in x.value: walk(k); walk(v)
walk(n); print(bad)
d=yaml.safe_load(open('claims/drieu-2018.yaml'))['claims']
print(len(d), sum('criterion' in c for c in d), sum('statistics' in c for c in d), sum('expected' in c for c in d))
EOF
git status --short
```

```
[]
35 35 30 7
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
?? claims/drieu-2018.yaml
?? scripts
```

**Agent**

I wrote `claims/drieu-2018.yaml`, and the quote checker passes it with 0 problems (all 86 recorded statistical values found in the text). Nothing is committed.

**Text read**
- The version of record, for the main text and the Fig. 1–3 legends.
- The author manuscript (HAL hal-02330673v1), for the Methods, the Fig. 4 legend and figs. S1–S13 with their legends.
- Page 5 of the version of record (Fig. 4 and the closing paragraphs) is missing from the extracted text, so the Fig. 4 legend is quoted from the manuscript. I could not render PDF pages because poppler is not installed, so some figure values could not be read.
- Code: FMAToolbox at commit 6bbb366. It has general functions (decoding, remapping test, ripple detection, field statistics) but not the paper's scripts for trajectory scores, quadrant scores, z-proportions or bias correlations. Where its defaults differ from the Methods, the claims follow the Methods.
- The dataset's description says the authors' own scripts are in the archive. I did not read them, since they are part of the dataset's files.

**Counts**
- 35 claims: 34 have quotes, and 1 (fig. S5B per-rat ANOVAs) is marked inferred.
- 30 have statistics, 7 have expected values, and all 35 have criteria.

**Discrepancies noted in the opening comment**
- The two versions print different P bounds for Fig. 1C (10⁻³ against 10⁻⁴) and Fig. 1E (10⁻¹⁰ against 10⁻¹¹); the version of record is used.
- The Methods describe "three rats" with tetrodes and "three rats" with octrodes, though the paper has five rats.
- The main text compares sleep measures "across animals", while the fig. S11 legend compares them between sleep conditions; the legend's comparison is tested.

**Details the paper leaves open, with the readings named**
- **Place fields:** minimum field size (none, or the toolbox default of 10 bins); whether a cell's second field counts.
- **Theta LFP:** which channel (the one with the most theta power, or the mean of the pyramidal-layer channels); spike phase (interpolated between peaks and troughs, or the phase of the theta-filtered signal).
- **Slopes:** conversion to m/s (each cycle's duration, or the mean theta period).
- **Joint score-slope plots:** matrix bin sizes (a standard grid, plus half and double); what counts as "high-value" (score above the shuffled 95th percentile and slope above 3 m/s).
- **Sleep events:** whether the candidate-event mean and s.d. come from SWS only or the whole sleep session; whether "restricted to ripples" means any overlap or the event's peak inside a ripple.
- **Remapping:** which cells enter (field in both conditions, or in either); circular or linear cross-correlogram.
- **Unassigned P values:** which pairs the P values belong to in Figs. 2D, 2F, 3C and 4E.
- **Fig. 2B power:** the unit of the ANOVA (per rat, or per spectrogram window), since P < 10⁻⁶ is hard to reach with 5 rats.
- **Replay proportion (Fig. 4E):** whether a positive slope is also required.
- **Forward replay (Fig. 4F):** compared with reverse within the session, or with baseline sleep.
- **Bias correlations:** which theta cycles count as sequences (all analysed cycles, or only significant ones).
- **Smaller choices made outright:** fig. S8 matches mean rate or peak in-field rate; fig. S9 drops bins highest-error first; fig. S10 decodes each lap from its own laps or the others.
- **Fixed choices that cannot change the outcome:** chronux defaults for spectra, 1000 surrogates for bias correlations.
- **Choices made here:** 95% as the threshold for "covered the entire track", because fig. S2C's values are not legible in the text; and the assignment of the Fig. 3B and fig. S5B values to conditions, read from panel order.

**Missing from the paper:** the paper's own scripts are not linked (only the general toolbox).

The repository also has untracked files I did not create (`.bashrc`, `.idea`, `scripts` and others). I left them alone; only the claims file is mine.

## End of run

20 turns, 6 minutes, $2.23 at API prices, result: success.
