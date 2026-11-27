# mckenzie-2025 · claims · run 45860558929

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cat docs/protocol.md; ls paper/ claims/ tools/
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
grep -n "^#" docs/protocol.md; ls paper/ claims/ tools/
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
wc -l paper/*.txt; head -c 3000 paper/*.txt; ls papers/datasets/ | grep mckenzie; cat papers/datasets/mckenzie-2025.yaml 2>/dev/null; sed -n 1,80p tools/claims_check.py
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
grep -n "" paper/*.txt | awk -F: '$1>0' | grep -v "^[0-9]*:10\.[0-9]" | grep -v "^[0-9]*:$" | head -400
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-registry-encore-registry/f64371d5-8e54-4dd6-8e6d-2ed3d79472b5/tool-results/b75quyn3v.txt"
}
```

```
1	1:DOI: 10.7554/elife.105183
2	2:Version: version of record
3	3:Source: find_reuse cache
4	4:Stored: 2026-11-10
5	5:Extracted: as fetched
6	6:------------------------------------------------------------------------
7	7:Event boundaries drive norepinephrine release and distinctive neural representations of space in the rodent hippocampus
8	9:Abstract
9	10:Episodic memories are temporally segmented around event boundaries that tend to coincide with moments of environmental change. During these times, the state of the brain should change rapidly, or reset, to ensure that the information encountered before and after an event boundary is encoded in different neuronal populations. Norepinephrine (NE) is thought to facilitate this network reorganization. However, it is unknown whether event boundaries drive NE release in the hippocampus and, if so, how NE release relates to changes in hippocampal firing patterns. The advent of the new GRABNE sensor now allows for the measurement of NE binding with sub-second resolution. Using this tool in mice, we tested whether NE is released into the dorsal hippocampus during event boundaries defined by unexpected transitions between spatial contexts and presentations of novel objections. We found that NE binding dynamics were well explained by the time elapsed after each of these environmental changes, and were not related to conditioned behaviors, exploratory bouts of movement, or reward. Familiarity with a spatial context accelerated the rate in which phasic NE binding decayed to baseline. Knowing when NE is elevated, we tested how hippocampal coding of space differs during these moments. Immediately after context transitions we observed relatively unique patterns of neural spiking which settled into a modal state at a similar rate in which NE returned to baseline. These results are consistent with a model wherein NE release drives hippocampal representations away from a steady-state attractor. We hypothesize that the distinctive neu
[... 168 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-registry-encore-registry/f64371d5-8e54-4dd6-8e6d-2ed3d79472b5/tool-results/b75quyn3v.txt",
 "offset": 178,
 "limit": 225
}
```

```
178	595:Over weeks, mice were over-trained on a spatial alternation task in a figure-eight maze (see Huszar et al. 2022, for full details). Animals were water restricted before the start of experiments and familiarized with the figure-eight maze. Mice were trained to visit alternate arms between trials to receive a water reward in the first corner reached after making a correct left/right turn after which, a 5-s delay in the start area was introduced between trials. To explore the reorganization of place tuning across different environments, the same mice were introduced to novel environments after running in the familiar figure-8 maze. In the sessions analyzed here (N=8), animals underwent recording sessions consisting of a ∼120-min home cage period, running on the familiar figure-eight maze, ∼60-min home cage period, running in a novel environment, followed by a final ∼120-min home cage period. In some sessions, animals were exposed to two distinct novel environments, with a ∼60-min home cage period in between (only one transition to a novel environment was chosen per session to analyze here). We considered transitions to novel linear tracks (N = 3 sessions), novel figure-8 mazes (N = 3 sessions), and a novel arena (N = 1 session). Mazes were placed in distinct recording rooms, or in different corners of the same recording room, with distinct enclosures to ensure unique visual cues. Mouse position was captured with head-mounted red LEDs.
179	597:Spiking analysis
180	599:Spikes were extracted and classified into putative single units using KiloSort1158 and manually curated in phy159. Pyramidal neurons were separated from interneurons based on waveform shape and bursting statistics and only pyramidal cell spiking was analyzed.
181	601:ACG slope analysis
182	603:Population firing rates were calculated in 100-ms bins by counting the number of spikes observed in that period and then z-scoring over the first 1000-s after transfer. All vectors within a session were corre
[... 219 more lines not kept]
```

**Agent calls Bash**

```bash
grep -n -i -E "github|code avail|data avail|zenodo|osf\.io|figshare|buzsakilab|databank" paper/*.txt | cut -c1-300; sed -n 300,323p paper/*.txt | cut -c1-200
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -n 985,1062p paper/*.txt | cut -c1-300; sed -n 85,140p docs/protocol.md >/dev/null; ls schemas/; python -c "import json;d=json.load(open('schemas/claims.schema.json'));print(json.dumps(d,indent=1)[:6000])"
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
python -c "import json;d=json.load(open('schemas/claims.schema.json'));print(json.dumps(d['\$defs'],indent=1)); print(list(d['properties']))"; grep -l "relation: reuses" papers/datasets/*.yaml | head -3
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
[... 86 more lines not kept]
```

**Agent calls Bash**

```bash
head -40 claims/burman-2023.yaml; grep -n -B2 -A3 "data: elsewhere\|not public\|own recordings" claims/burman-2023.yaml claims/alasfour-2024.yaml | head -60
```

```
# Claims for Burman, Brodersen, Raimondo, Sen & Akerman (2023), Neuron 111, 3531-3540,
# "Active cortical networks promote shunting fast synaptic inhibition in vivo", on dandiset 000458.
# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"),
# 2026-11-10, protocol pilot-14 as stated in docs/protocol.md (Reader, steps 1 to 4).
#
# Text read. The version of record (open access, CC BY), full text from Europe PMC (PMC11913778),
# in paper/10.1016-j.neuron.2023.08.005.txt: Summary, Introduction, Results, the legends of
# Figures 1 to 4, Discussion, STAR Methods with Tables 1 and 2, and Data and code availability.
# The supplement (Document S1, Figures S1 to S7 and their legends) is not in the text, and no PDF
# was supplied. No claim on the dandiset needs it except figs6-rate-regressed, whose method is
# only in the Figure S6 legend; that claim names readings. The claims on Figures S2 to S5 and S7
# rest on the main-text sentences that cite them, and their tests are not known here.
#
# Code read. (1) gist.github.com/paulbrodersen/a77bcf5e06ae27fa96923cb313a02ccf, revision
# 43a13d89441b7f56e835e84fa5811d9567917daf, burman_et_al_2023_neuropixel_data_analysis.py: reads
# the 17 NWB sessions of DANDI:000458 (version 0.230317.0039, named in its docstring) and writes,
# per unit, evoked firing rate, peri-stimulus histogram entropy and synchrony for the awake and
# isoflurane epochs. It does not hold the exclusion step, the statistics or the plots.
# (2) gist.github.com/paulbrodersen/2ce61e4e57c7659b727d30e3e1e0128f, revision
# f6a05661c10051560aa381e334099efd8521617b, burman_et_al_2023_neuronal_network_simulation.py: the
[... 54 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 40,120p claims/burman-2023.yaml
```

```
# al. (2023), DANDI:000458 (key resources table; claims/claar-2023.yaml describes it): head-fixed
# mice with up to three Neuropixels probes and a bipolar stimulating electrode in layer 2/3 or 5/6
# of SSp or MOs, single electrical pulses delivered awake and under isoflurane. The paper uses 17
# recordings in 16 mice (sub-569073 has two sessions); units are regular spiking units of the
# stimulated area, 662 after exclusion. Measured variables used: unit spike times, waveform
# duration and location; trial times, stimulus type, behavioral epoch, validity and stimulation
# target region.
# Network models (Figures 4E to 4H, S7) are generated by the paper's simulation code (data
# elsewhere, where names the code).
#
# Method for the claims on DANDI:000458, fixed from the Methods ("Pre-processing of Neuropixels
# dataset", "Characterization of stimulus-evoked spiking responses", "Statistical analyses") and
# the analysis gist (1). Cited in the criteria as N1 to N8.
# N1 Sessions. The 17 sessions listed in the gist (see dataset-sessions-link).
# N2 Units. Regular spiking units, waveform duration of 0.4 ms or more (Methods; the gist uses
#    strictly more than 0.4, which is shown as a variant). Area, open between two readings:
#    (A1) the Methods, units whose location annotation is "SSp-ll" or "SSp-tr", or "MOs",
#    whichever area was electrically stimulated in the session; (A2) the gist, units whose
#    location's first three characters are among the session's estim_target_region values of
#    its electrical trials.
[... 61 more lines not kept]
```

**Agent calls Bash**

```bash
curl -s https://api.dandiarchive.org/api/dandisets/000552/versions/0.230630.2304/info/ | python -c "import json,sys;d=json.load(sys.stdin);m=d['metadata'];print(m['name']);print(m.get('description'));print(m.get('assetsSummary',{}).get('numberOfSubjects'))"
```

Result: the fetched text is not kept.

**Agent calls Write**

```json
{
 "file_path": "claims/mckenzie-2025.yaml",
 "content": "# Claims for McKenzie, Sommer, Donaldson, Pimentel, Kakani, Choi, Newman & English (2025), eLife\n# 14:RP105183, \"Event boundaries drive norepinephrine release and distinctive neural\n# representations of space in the rodent hippocampus\", tested on DANDI:000552.\n# Written by an agent (model \"claude-opus-5-5\", Claude Code, runner \"GitHub Actions\"), 2026-11-26,\n# protocol pilot-19 as stated in docs/protocol.md (Reader, steps 1 to 4).\n#\n# Text read. paper/10.7554-elife.105183.txt, the eLife page of Reviewed Preprint version 1\n# (January 31, 2025, marked \"Not revised\"; the file header calls it the version of record).\n# It holds the Abstract, Introduction, Results with the legends of Figures 1 to 8, Discussion,\n# Methods, and the legends of Supplemental Figures S1 to S7. There is no separate supplement\n# beyond those figures, and no PDF was supplied; no figure was opened.\n#\n# Code read. None. The paper links no analysis code and has no code or data availability\n# statement. The photometry models were fit in MATLAB R2021b with fmincon (Methods).\n#\n# Data the paper used, as it reports them.\n# Fiber photometry (Figures 1 to 6, S1 to S5). C57BL/6J mice (N = 8, 3 female), GRAB-NE\n# (AAV9-hSyn-NE2h) in left dorsal CA1 with a fiber over it; 465 nm and 405 nm excitation,\n# sampled at 1017.3 Hz; SignalNE in baseline standard deviations, smoothed with a 1 s Gaussian.\n# Paradigms: novel arenas over 10 days (HC-A-HC, with B and C on days 1 and 10), five novel\n# objects for 5 min each (6 mice in the tests), a water-rewarded 1.2 m linear track (110\n# sessions), the track with a novel object (5 or 6 mice), desipramine and yohimbine injections.\n# Behavior from DeepLabCut ear positions. These recordings are not in DANDI:000552 and the paper\n# deposits them nowhere. Their claims are kept; they cannot be tested on this dandiset.\n# Electrophysiology (Figures 7, 8, S6, S7). Reanalysis of the Huszar et al. (2022) data,\n# DANDI:000552 version 0.230630.2304 (Methods, Electrophysiology subjects), which the archive\n# titles \"Preconfigured dynamics in the hippocampus are guided by embryonic birthdate and rate of\n# neurogenesis\". Three mice (e13_26m1, e15_13f1, e16_3m2), silicon probes in right dorsal CA1,\n# 30 kHz. Each analyzed session (N = 8) is about 120 min home cage, running on the familiar\n# figure-eight maze, about 60 min home cage, running in a novel environment, about 120 min home\n# cage; one novel transition per session. Novel environments are listed as 3 linear tracks, 3\n# figure-eight mazes and 1 arena, which sums to 7, not 8 (see E1). Variables used: pyramidal unit\n# spike times, LED head position, broadband LFP for ripples, and the epoch times of the home cage\n# and maze periods.\n#\n# Method for the claims on DANDI:000552, from the Methods (Spiking analysis, ACG slope analysis,\n# Reset analysis, Place field detection, Ripple detection, Reactivation analysis) and the figure\n# legends. Cited in the criteria as E1 to E10.\n# E1 Sessions. The 8 sessions of the three mice named above with a familiar figure-eight run\n#    followed by a novel environment (Methods, Behavioral testing). The listed environment types\n#    sum to 7; the df of 7 in every test implies 8 sessions. Open: the author takes the sessions\n#    of those mice that fit the description, reports how many there are and of which type, and\n#    runs the tests on all of them. Where a session has two novel environments, which one was\n#    chosen is open: (a) the first, (b) the second; both are run.\n# E2 Transition. The time the mouse is placed in the maze, read as the start of the maze epoch.\n#    Transfer and settling are measured from it.\n# E3 Units. Pyramidal cells only, separated \"based on waveform shape and bursting statistics\"\n#    (Methods, Spiking analysis), as in Huszar et al. (2022). No thresholds are given. The\n#    dataset's own putative cell type labels are used; if it has none, the separation is open\n#    and is recorded as a deviation.\n# E4 Population vectors. Spike counts of each unit in 100 ms bins, each unit z-scored over the\n#    first 1000 s after transfer (Methods, ACG slope analysis). The similarity matrix is the\n#    Pearson correlation of every pair of vectors in the maze epoch.\n# E5 Nearest neighbors. For each 100 ms bin, the 3 most correlated vectors among bins recorded in\n#    the same location (minimum occupancy 1 s), averaged, then smoothed with a 1 s Gaussian\n#    kernel (Methods, Reset analysis). Location bins are 1 x 1 cm, the only bin size the Methods\n#    give (Place field detection), read as applying here. The Methods compare each moment with\n#    \"any other moment\", so only the bin itself is excluded; a variant that also excludes the\n#    contiguous run of bins in the same location is shown, not judged. Whether a speed filter\n#    applies is open: (a) all bins, (b) only bins above 5 cm/s, the threshold of Place field\n#    detection; both are run.\n# E6 Windows. \"First minute\" is 0 to 60 s after transfer. \"10 minutes into the session\" is read\n#    as 600 to 660 s, as Figure 8B states (\"10-11 minutes\"); Figure S6 says \"Minute 10\", which\n#    can also be read as 540 to 600 s, run as a second reading for Figure S6 and Figure 7E, 7F\n#    and S7G, S7H.\n# E7 Statistics. Each test reports t(7) over 8 sessions; with one value per session and\n#    condition this is a paired (one-sample on differences) Student t-test, two-sided, p < 0.05.\n#    The paper does not name sidedness; two-sided is a standard choice.\n# E8 Speed and acceleration. The Methods give the Kalman filter only for the photometry mice;\n#    for the electrophysiology they do not say. Readings: (a) a second-order Kalman filter on\n#    the LED position, as in the photometry Methods; (b) finite differences of position\n#    smoothed with a 1 s Gaussian.\n# E9 Ripples. Broadband LFP bandpassed at 130 to 200 Hz (fourth-order Chebyshev), normalized\n#    squared signal, peaks above 5 SD, edges at 2 SD, duration 20 to 200 ms (Methods, Ripple\n#    detection). The channel is not named; a channel in the CA1 pyramidal layer is used. If the\n#    dataset holds the ripple events of Huszar et al. (2022), they are used as a variant.\n# E10 Reactivation. For each ripple, each unit's spike count over the ripple divided by its\n#    duration; Pearson correlation with each 100 ms track vector; null by moving each unit's\n#    value on a ripple to a random other ripple, 1000 times; a ripple reactivates a moment when\n#    its R exceeds 99.9% of shuffles (Methods, Reactivation analysis). Pre and post windows are\n#    open: the Methods say ripples \"within 30 minutes of the beginning of the session and within\n#    30 minutes after the session\". Readings: (a) the 30 min of home cage before the novel run\n#    and the 30 min after it; (b) the first 30 min of the recording day and the 30 min after the\n#    novel run. Whether the track vectors are z-scored (E4) or raw counts is open; both are run.\n#    The shuffle is done within each of the pre and post sets of ripples, a standard choice.\n#\n# Tolerances. 10% of the reported value, or a reported range widened by 10% of each bound.\nschema_version: 2\npaper: doi:10.7554/elife.105183\nclaims:\n- id: figs1a-desipramine\n  statement: The NE reuptake inhibitor desipramine increases SignalNE relative to vehicle injections.\n  source: Results, SignalNE exponentially decays after transfer to a novel arena (opening paragraph);\n    Figure S1A\n  quote: the noradrenergic reuptake inhibitor desipramine caused a significant increase in SignalNE relative\n    to vehicle injections (Figure S1A)\n  criterion: Not testable on DANDI:000552; the photometry recordings are not deposited. The paper reports\n    no test statistic for this comparison.\n- id: figs1b-yohimbine\n  statement: The alpha2 receptor antagonist yohimbine disrupts the normal increase in SignalNE after context\n    transition.\n  source: Results, opening paragraph; Figure S1B\n  quote: noradrenergic α2 receptor antagonism with yohimbine (from which GRABNE was derived) disrupted normally\n    strong SignalNE (Figure S1B)\n  criterion: Not testable on DANDI:000552; the photometry recordings are not deposited.\n- id: fig1d-arena-decay\n  statement: Averaged over all exposures, SignalNE increases immediately on entry to a novel arena and decays\n    exponentially to a steady state over minutes.\n  source: Results, SignalNE exponentially decays after transfer to a novel arena, paragraph 1; Figure 1D\n  quote: Averaging across all exposures, SignalNE increased immediately upon entry to the testing arena and\n    exponentially decayed to a steady state over minutes (Figure 1D)\n  criterion: Not testable on DANDI:000552; the photometry recordings are not deposited.\n- id: figs1e-univariate-covariates\n  statement: In univariate analyses SignalNE is positively co-modulated with acceleration, modestly with velocity,\n    and negatively with distance to the edge of the arena.\n  source: Results, SignalNE exponentially decays after transfer to a novel arena, paragraph 1; Figure S1E\n  quote: Univariate analysis revealed strong, positive co-modulation of SignalNE with acceleration (t(7) =\n    4.54, p = 0.002) and modest positive correlation with velocity (t(7) = 2.32, p = 0.05)(Figure S1E). SignalNE\n    also correlated with distance to the edge of the environment (t(7) = -2.37, p = 0.05)\n  statistics:\n  - about: acceleration\n    test: t-test\n    statistic: t(7) = 4.54\n    p: 0.002\n    n: 8 mice\n  - about: velocity\n    test: t-test\n    statistic: t(7) = 2.32\n    p: 0.05\n    n: 8 mice\n  - about: distance to edge\n    test: t-test\n    statistic: t(7) = -2.37\n    p: 0.05\n    n: 8 mice\n  criterion: Not testable on DANDI:000552; the photometry recordings are not deposited.\n- id: fig1e-arena-time-from-transition\n  statement: In a backward stepwise regression of SignalNE in novel arenas, only removing the terms for time\n    from context transition significantly worsens cross-validated model performance; acceleration, velocity,\n    distance from edge and time from rearing do not.\n  source: Results, SignalNE exponentially decays after transfer to a novel arena, paragraph 2; Figure 1E\n  quote: Significant decreases in model fit were only observed after dropping the time from context entry\n    independent variable (Figure 1E)\n  statistics:\n  - test: Student t-test on percent change in CVMSE against 0\n    statistic: t(7) = 3.30\n    p: 0.01\n    n: 8 mice\n  criterion: Not testable on DANDI:000552; the photometry recordings are not deposited.\n- id: fig2c-track-time-from-transition\n  statement: On a familiar linear track with water reward, SignalNE rises on entry and decays to a steady\n    state, and only removing time from track entry significantly worsens the model; reward and movement terms\n    do not.\n  source: Results, SignalNE exponentially decays after transfer to a familiar linear track, paragraph 2;\n    Figure 2B and 2C\n  quote: The stepwise regression analysis showed that removing time from entry, but no other term, significantly\n    decreased our ability to predict fluctuations in SignalNE (Figure 2C)\n  statistics:\n  - test: Student t-test on percent change in CVMSE against 0\n    statistic: t(7) = 7.20\n    p: 0.0008\n    n: 8 mice\n  criterion: Not testable on DANDI:000552; the photometry recordings are not deposited.\n- id: figs2-no-reward-modulation\n  statement: Hippocampal SignalNE on the linear track is not modulated around reward delivery or movement.\n  source: Results, SignalNE exponentially decays after transfer to a familiar linear track, paragraph 2;\n    Figure S2\n  quote: Hippocampal NE was not modulated around reward delivery (signaled with an audible solenoid click)\n    nor movement (Figure S2)\n  criterion: Not testable on DANDI:000552; the photometry recordings are not deposited. The paper reports\n    no test for this absence.\n- id: fig3d-object-introduction\n  statement: Each of five novel objects induces phasic NE release on introduction, and only removing time\n    from object introduction significantly worsens the model; object sampling, movement and distance from\n    edge do not.\n  source: Results, SignalNE exponentially decays after introduction of a novel object, paragraph 3; Figure\n    3C and 3D (legend labels both C)\n  quote: Backward stepwise regression analysis revealed that the time from object introduction was the only\n    term whose absence significantly decreased CVMSE (Figure 3D)\n  statistics:\n  - test: Student t-test on percent change in CVMSE against 0\n    statistic: t(5) = 3.54\n    p: 0.017\n    n: 6 mice\n  criterion: Not testable on DANDI:000552; the photometry recordings are not deposited.\n- id: figs3-object-order-and-sampling\n  statement: NE release after object introduction is not systematically related to the object's ordinal\n    position, nor coordinated with individual object samples.\n  source: Results, SignalNE exponentially decays after introduction of a novel object, paragraph 3; Figure\n    S3A to S3D\n  quote: NE release dynamics were not systemically related to the ordinal position of the object in the\n    sequence (Figure S3 A-C). NE release was also not coordinated with individual object samples (Figure\n    S3D)\n  criterion: Not testable on DANDI:000552; the photometry recordings are not deposited. The paper reports\n    no test for either absence.\n- id: fig4b-novel-object-on-track\n  statement: A novel object placed on the familiar linear track does not change SignalNE dynamics after transfer\n    to the track; the decay constant is unchanged, and time from transfer remains the only significant model\n    term.\n  source: Results, Novel objects do not affect SignalNE around spatial context transitions, paragraph 1;\n    Figure 4B and 4C\n  quote: Though mice reliably stopped to inspect the novel object, no difference in SignalNE was observed\n    between the novel object and control conditions (Figure 4)\n  statistics:\n  - about: decay constant, novel object against control\n    test: t-test\n    statistic: t(4) = 1.47\n    p: 0.22\n  - about: removal of time from track transfer\n    test: Student t-test on percent change in CVMSE against 0\n    statistic: t(5) = 3.22\n    p: 0.03\n  criterion: Not testable on DANDI:000552; the photometry recordings are not deposited.\n- id: fig5d-decay-hastens-with-days\n  statement: Over 10 days of exposure to an arena, the decay rate (tau) of SignalNE after transfer changes\n    systematically with experience while its amplitude (beta) does not, and decay after transfer to the home\n    cage is faster than after any arena day.\n  source: Results, Experience accelerates the decay of SignalNE after spatial context transitions, paragraph\n    2; Figure 5C and 5D\n  quote: The rate of SignalNE decay (τ; mixed-effects linear model, t(73) = 2.31, p = 0.02), and not amplitude\n    (β; mixed-effects linear model, t(73) = 1.16, p = 0.25), systematically changed as a function of the number\n    of days of experience\n  statistics:\n  - about: tau against days\n    test: mixed-effects linear model, days fixed, subject random slopes and intercepts\n    statistic: t(73) = 2.31\n    p: 0.02\n  - about: beta against days\n    test: mixed-effects linear model, days fixed, subject random slopes and intercepts\n    statistic: t(73) = 1.16\n    p: 0.25\n  - about: each arena day against home cage transfer (printed as p ≤0.01)\n    p: 0.01\n    p_relation: <\n  criterion: Not testable on DANDI:000552; the photometry recordings are not deposited.\n- id: figs4-behavior-day1-day2\n  statement: On the first day in the arena, compared with the second, mice tend to accelerate more, rear more\n    often and stay closer to the perimeter.\n  source: Results, Experience accelerates the decay of SignalNE after spatial context transitions, paragraph\n    1; Figure S4\n  quote: Comparing the first and second days of testing, mice tended to display higher levels of acceleration,\n    rear more often, and spend more time close to the perimeter during first-time arena exposure (Figure S4)\n  criterion: Not testable on DANDI:000552; the photometry recordings are not deposited.\n- id: fig6-recent-history\n  statement: After the linear track, SignalNE in the home cage rises like after the arena but then decays\n    faster and falls further below baseline; the track's decay constant is comparable to that of arena days\n    3 to 4, and time from home cage entry is the only significant model term after either.\n  source: Results, Familiarity is not the sole determinant of the decay of SignalNE after spatial context\n    transitions, paragraph 1; Figure 6A to 6C; Figure S5\n  quote: The rate of SignalNE decay was faster (Figure 6B) and the NE decrease was larger (Figure 6C) after\n    linear track exposure as compared to experience in the arena\n  statistics:\n  - about: NE decrease after track against after arena\n    test: t-test\n    statistic: t(5) = 3.74\n    p: 0.005\n  - about: removal of time from home cage entry, after arena\n    test: Student t-test on percent change in CVMSE against 0\n    statistic: t(7) = 2.62\n    p: 0.03\n  - about: removal of time from home cage entry, after track\n    test: Student t-test on percent change in CVMSE against 0\n    statistic: t(5) = 4.44\n    p: 0.007\n  criterion: Not testable on DANDI:000552; the photometry recordings are not deposited.\n- id: ephys-ensemble-size\n  statement: The analyzed CA1 ensembles contain on average 253.8 neurons per session, ranging from 191 to 363.\n  source: Results, CA1 spatial code takes minutes to settle after context transition, paragraph 2\n  quote: mean ensemble = 253.8 neurons, range = 191-363 neurons, bin size = 100-ms\n  expected:\n  - quantity: mean number of neurons per session\n    value: 253.8\n    tolerance: 25.4\n    unit: neurons\n  - quantity: smallest ensemble\n    value: 191\n    tolerance: 19.1\n    unit: neurons\n  - quantity: largest ensemble\n    value: 363\n    tolerance: 36.3\n    unit: neurons\n  criterion: Over the sessions of E1. Which units are counted is open between (a) the pyramidal units of\n    E3, as the Methods analyze only those, and (b) all units of the session. Reproduced when, under one reading,\n    the mean is within tolerance and every session lies within 191 to 363 widened by 10% of each bound (172\n    to 399).\n- id: figs6b-decorrelation-novel\n  statement: In a novel environment, CA1 population vectors decorrelate faster with lag in the first minute\n    after transfer than at minute 10.\n  source: Results, CA1 spatial code takes minutes to settle after context transition, paragraph 1; Figure\n    S6A and S6B\n  quote: in novel environments, the rate of decorrelation was indeed faster in the first minute after transfer\n    as compared to later in the session (Figure S6 A,B)\n  statistics:\n  - test: t-test\n    statistic: t(7) = 3.07\n    p: 0.018\n    n: 8 sessions\n  criterion: 'Methods, ACG slope analysis, with E1 to E4, E6, E7. For each session and window (minute 1, minute\n    10), the mean Pearson R between population vectors as a function of lag from 0.1 to 10 s, fit with an\n    exponential with three free parameters, R(lag) = beta exp(-lag/tau) + c; the decay rate is 1/tau. The\n    Methods'' \"100-s moving average\" is open: (a) the curve is computed over the bins of each 60 s window\n    as Figure S6A labels them (Minute 1, Minute 10); (b) the curve is computed over a 100 s window starting\n    at the window''s start. Both are run, with both readings of minute 10 (E6). Reproduced when the decay\n    rate is higher in minute 1 than minute 10 by the paired t-test over sessions at p < 0.05.'\n  depends_on:\n  - ephys-ensemble-size\n- id: figs6d-decorrelation-familiar\n  statement: In the familiar environment the decorrelation rate does not differ between the first minute\n    and minute 10 after transfer.\n  source: Results, CA1 spatial code takes minutes to settle after context transition, paragraph 1; Figure\n    S6C and S6D\n  quote: Such a relationship was not observed in a familiar space (Figure S6 C,D)\n  statistics:\n  - test: t-test\n    statistic: t(7) = 0.50\n    p: 0.63\n    n: 8 sessions\n  criterion: A claim of absence, judged on the paper's test, a t-test over 8 sessions (E7) at p < 0.05, on\n    the decay rates of figs6b-decorrelation-novel computed for the familiar figure-eight run. Reproduced\n    when the minute 1 against minute 10 difference is not significant; not reproduced when it is. The effect\n    size is reported either way. The open readings of figs6b-decorrelation-novel apply; absence is judged\n    under the reading (a) with minute 10 as 600 to 660 s, the others shown.\n  depends_on:\n  - figs6b-decorrelation-novel\n- id: fig7ab-umap-embedding\n  statement: A 2D UMAP embedding of 100 ms population vectors maps the spatial layout of the environment,\n    and moments just after transition lie at the periphery of the representational space.\n  source: Results, CA1 spatial code takes minutes to settle after context transition, paragraph 2; Figure\n    7A and 7B\n  quote: Color coding by position shows that the CA1 representational space maps the spatial layout of the\n    environment (Figure 7A). Color coding by time shows that moments immediately following the transition\n    are associated with unusual representations, which can be seen at the periphery of the representational\n    state space (Figure 7B)\n  criterion: The paper shows one example session and gives no UMAP parameters or measure. UMAP is run with\n    the umap-learn defaults on the population vectors of E4 (a standard choice). The paper fixes no measure,\n    so these are named as assumptions; position mapping is judged by a nearest-neighbor regression of position\n    from the 2D embedding (5-fold, contiguous blocks) explaining more variance than with position shuffled\n    in blocks, and periphery by a larger mean distance from the embedding's median of first-minute bins than\n    of later bins. Reproduced when both hold in most sessions.\n- id: fig7e-novel-settling\n  statement: In a novel environment, population vectors in the first minute after transfer correlate less\n    with their nearest neighbors at the same location than those 10 minutes into the session; representations\n    settle into a steady state over several minutes.\n  source: Results, CA1 spatial code takes minutes to settle after context transition, paragraph 2; Figure\n    7C and 7E\n  quote: This nearest-neighbor search revealed that early moments were associated with neural activity that\n    poorly correlated with activity recorded in the same location later in the session (Figure 7 C,D)\n  statistics:\n  - test: t-test\n    statistic: t(7) = 8.05\n    p: 0.00009\n    n: 8 sessions\n  criterion: 'Methods, Reset analysis, with E1 to E7. Per session, the mean of the smoothed nearest-neighbor\n    correlation over the bins of minute 1 and of minute 10. Reproduced when minute 1 is lower by the paired\n    t-test over sessions at p < 0.05, under one combination of the readings of E1, E5 and E6; all combinations\n    are shown. \"Several minutes\" is not measured by the paper; the per-minute session mean is shown and that\n    part is not judged.'\n  depends_on:\n  - ephys-ensemble-size\n- id: fig7f-familiar-settling\n  statement: In the familiar environment, too, population vectors in the first minute correlate less with\n    their same-location nearest neighbors than those 10 minutes in.\n  source: Figure 7D and 7F\n  quote: Same as Panel E recorded in a familiar environment (t(7) = 8.20, p = 0.00008)\n  statistics:\n  - test: t-test\n    statistic: t(7) = 8.20\n    p: 0.00008\n    n: 8 sessions\n  criterion: As fig7e-novel-settling, on the familiar figure-eight run of each session.\n  depends_on:\n  - fig7e-novel-settling\n- id: fig7g-familiar-more-similar-early\n  statement: Initial representations are more correlated with their nearest neighbors in the familiar environment\n    than in the novel one, and they settle more rapidly in the familiar environment.\n  source: Results, CA1 spatial code takes minutes to settle after context transition, paragraph 2; Figure\n    7G\n  quote: Initial representations were more correlated to their nearest neighbors in a familiar environment\n    as compared to those recorded in a novel environment (t(7) = 7.58, p = 0.0001)\n  statistics:\n  - test: t-test\n    statistic: t(7) = 7.58\n    p: 0.0001\n    n: 8 sessions\n  criterion: Per session, the first-minute mean nearest-neighbor correlation (fig7e-novel-settling) in the\n    familiar run against the novel run. Reproduced when familiar is higher by the paired t-test over sessions\n    at p < 0.05, under one combination of the readings of E1 and E5.\n  depends_on:\n  - fig7e-novel-settling\n  - fig7f-familiar-settling\n- id: figs7ab-in-field-out-field\n  statement: Settling involves an increase over time of firing within each neuron's place field and a decrease\n    of out-of-field firing, in novel and familiar environments.\n  source: Results, CA1 spatial code takes minutes to settle after context transition, paragraph 2; Figure\n    S7A and S7B\n  quote: Settling involved both an increase of activity within a neuron's place field and a decrease in out-of-field\n    firing (Figure S7 A,B)\n  criterion: 'Methods, Place field detection: 1 x 1 cm bins, bins above 5 cm/s, occupancy over 1 s; field\n    bounds where the unnormalized rate exceeds 5 Hz; the deviation of each 100 ms z-scored rate from the\n    neuron''s mean map value at that location (Figure S7A legend). The paper reports no test. As a standard\n    choice, per session the in-field and out-of-field deviations averaged over neurons in each minute, and\n    the slope of a linear fit over the first 10 minutes. Reproduced when, in each environment, the mean slope\n    is positive in field and negative out of field, each by a one-sample t-test over sessions at p < 0.05\n    (an assumption, as the paper gives no test).'\n  depends_on:\n  - ephys-ensemble-size\n- id: figs7cd-movement-not-time-locked\n  statement: For the most similar pairs of moments, the absolute differences in velocity and acceleration\n    show no systematic relationship with time after transfer.\n  source: Results, CA1 spatial code takes minutes to settle after context transition, paragraph 2; Figure\n    S7C and S7D\n  quote: When comparing pairs of moments with the highest representational similarity, there was no systematic\n    relationship between time after transfer and |Δvel|NN or |Δacc|NN (Figure S7 C-F)\n  criterion: 'Methods, Reset analysis, with E5 and E8. Whether |dvel|NN and |dacc|NN are taken over (a) the\n    3 nearest neighbors, as the Methods say (\"the time bins with the highest ... correlations\"), or (b) the\n    single nearest one, as the Figure S7C legend says (\"another 100-ms time bin\"), is open; both are run.\n    The paper reports no test for this absence. As a standard choice, per session the Spearman correlation\n    of each measure with time after transfer over the first 10 minutes; reproduced when its mean over sessions\n    does not differ from 0 by a t-test at p < 0.05, in novel and familiar runs. The values are reported either\n    way.'\n  depends_on:\n  - fig7e-novel-settling\n- id: figs7ef-time-explains-similarity\n  statement: Modeling nearest-neighbor similarity as a function of time from transfer, |dvel|NN and |dacc|NN,\n    only removing time from transition significantly decreases cross-validated prediction, in novel and familiar\n    environments.\n  source: Results, CA1 spatial code takes minutes to settle after context transition, paragraph 2; Figure\n    S7E and S7F\n  quote: Only removing time from transition significantly decreased ability to predict nearest neighbor correlations\n    (Figure S7 E,F)\n  statistics:\n  - about: novel environment\n    test: t-test on change in CVMSE\n    statistic: t(7) = 3.52\n    p: 0.01\n    n: 8 sessions\n  - about: familiar environment\n    test: t-test on change in CVMSE\n    statistic: t(7) = 3.12\n    p: 0.017\n    n: 8 sessions\n  criterion: 'Methods, Reset analysis: cross-validation withholds each session and reports its CVMSE; the\n    change is the percent change in CVMSE on dropping each variable, tested against 0 by a Student t-test\n    over sessions (Methods, Statistical modeling of SignalNE), p < 0.05. The model''s form is not given for\n    the electrophysiology. Readings: (a) the photometry model''s form, time from transition as a fast positive\n    and a slow negative exponential, |dvel|NN and |dacc|NN as linear terms, and an intercept, fit by bounded\n    least squares; (b) a linear model on the three variables. The readings of figs7cd-movement-not-time-locked\n    and E8 apply. Reproduced when, under one reading, dropping time is significant and dropping either movement\n    term is not, in both environments.'\n  depends_on:\n  - figs7cd-movement-not-time-locked\n- id: figs7gh-unconditioned-similarity\n  statement: When representational similarity is not conditioned on location, first-minute patterns are still\n    less correlated with the rest of the session than those 10 minutes in, in novel and familiar environments.\n  source: Results, CA1 spatial code takes minutes to settle after context transition, paragraph 2; Figure\n    S7G and S7H\n  quote: Similar results were found when representational similarity was not conditioned on the mouse's location\n    (Figure S7 G,H)\n  statistics:\n  - about: novel environment\n    test: t-test\n    statistic: t(7) = 5.23\n    p: 0.001\n    n: 8 sessions\n  - about: familiar environment\n    test: t-test\n    statistic: t(7) = 5.60\n    p: 0.0008\n    n: 8 sessions\n  criterion: As fig7e-novel-settling, with the 3 most similar vectors taken from all bins of the run regardless\n    of location. Reproduced when minute 1 is lower than minute 10 at p < 0.05 in both environments.\n  depends_on:\n  - fig7e-novel-settling\n- id: fig8b-late-moments-reactivated\n  statement: Moments 10 to 11 minutes after a novel context transition are more likely to be reactivated in\n    post-experience ripples than moments 0 to 1 minutes after it.\n  source: Results, No preferential reactivation of moments following transition, paragraph 1; Figure 8A and\n    8B\n  quote: Contrary to expectations, the pattern of activity observed towards the end of the session was more\n    likely to be reactivated in the ripples that followed the experience (Figure 8 A,B)\n  statistics:\n  - test: t-test\n    statistic: t(7) = 2.46\n    p: 0.04\n    n: 8 sessions\n  criterion: 'Methods, Ripple detection and Reactivation analysis, with E1 to E4, E7, E9 and E10. Per session,\n    for each 100 ms moment the percentage of post ripples that reactivate it; the mean over moments in 600\n    to 660 s and in 0 to 60 s after transfer. Reproduced when the late value is higher by the paired t-test\n    over sessions at p < 0.05, under one combination of the readings of E1 and E10.'\n  depends_on:\n  - ephys-ensemble-size\n- id: fig8d-familiar-no-difference\n  statement: In the familiar environment, early and late moments do not differ in reactivation rate.\n  source: Results, No preferential reactivation of moments following transition, paragraph 1; Figure 8C and\n    8D\n  quote: There is no difference in reactivation rate for early vs late moment in a familiar environment (t(7)\n    = 0.40, p = 0.70)\n  statistics:\n  - test: t-test\n    statistic: t(7) = 0.40\n    p: 0.7\n    n: 8 sessions\n  criterion: A claim of absence, judged on the paper's t-test over 8 sessions (E7) at p < 0.05, as fig8b-late-moments-reactivated\n    on the familiar figure-eight run, with pre and post ripples taken around that run (E10 applied to it).\n    Reproduced when the early against late difference is not significant; not reproduced when it is. Effect\n    size reported either way; absence is judged under readings E10 (a) with z-scored track vectors, the others\n    shown.\n  depends_on:\n  - fig8b-late-moments-reactivated\n- id: fig8-no-pre-reactivation\n  statement: Track activity patterns show no evidence of being present in ripples recorded before the experience.\n  source: Results, No preferential reactivation of moments following transition, paragraph 1; Figure 8A\n  quote: nor any evidence that the pattern of activity observed on the track was present in ripples recorded\n    prior to the experience\n  criterion: The paper gives no test; Figure 8A compares the pre-ripple percentages with the false positive\n    rate of 0.1% (Methods, Reactivation analysis). As a standard choice, per session the mean over moments\n    of the percentage of pre ripples that reactivate each moment; reproduced when its mean over sessions is\n    not above 0.1% by a one-sided one-sample t-test at p < 0.05, in novel and familiar runs. Values reported\n    either way.\n  depends_on:\n  - fig8b-late-moments-reactivated\n- id: ne-and-settling-time-course\n  statement: The time course of hippocampal representational stabilization qualitatively matches that of\n    NE decay, in novel and familiar environments.\n  source: Results, CA1 spatial code takes minutes to settle after context transition, paragraph 2 (last\n    sentence); Discussion, The LC contribution to long-term changes in neural coding\n  quote: The time course of representational stabilization qualitatively matched that of NE decay in both\n    novel and familiar environments suggesting a potential link between NE release and atypical spiking behavior\n  criterion: Not testable on DANDI:000552 alone, as the NE half is in the undeposited photometry recordings,\n    and the paper compares the two only by eye. The settling half is tested by fig7e-novel-settling, fig7f-familiar-settling\n    and fig7g-familiar-more-similar-early.\n  depends_on:\n  - fig7g-familiar-more-similar-early\n"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
python tools/claims_check.py claims/mckenzie-2025.yaml paper/10.7554-elife.105183.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
grep -n -E "—|–|rather" claims/mckenzie-2025.yaml; python -c "
import yaml;d=yaml.safe_load(open('claims/mckenzie-2025.yaml'));c=d['claims'];print(len(c),sum('statistics' in x for x in c),sum('criterion' in x for x in c),sum('expected' in x for x in c))"
```

```
28 16 28 1
```

**Agent**

I've written `claims/mckenzie-2025.yaml`. The quote checker passes: 28 claims, 28 quotes, 25 statistical values, 0 problems. Nothing is committed.

**Text read.** `paper/10.7554-elife.105183.txt` is eLife Reviewed Preprint version 1 (January 31, 2025, marked "Not revised"), although its header says "version of record". It has the main text, all eight figure legends, the Methods, and the legends of Supplemental Figures S1 to S7. There is no other supplement and no PDF, and I opened no figure. The paper links no code and has no data or code availability statement.

**Claims.**
- **Totals:** all 28 have quotes, 16 record statistics, 28 have criteria, and 1 has expected values (ensemble size: mean 253.8 neurons, range 191 to 363).
- **Photometry (13 claims, Figures 1 to 6 and S1 to S5):** these recordings are the paper's own and are not in DANDI:000552. The paper deposits them nowhere, so these claims are marked not testable.
- **Spiking (14 claims, Figures 7, 8, S6 and S7):** these reuse the Huszar et al. 2022 data in DANDI:000552 (version 0.230630.2304; 3 mice, 8 sessions).
- **Cross-dataset (1 claim):** the paper's by-eye match between NE decay and the time course of representational settling.

**Details the paper leaves open, with the readings named:**
- **Session count:** the novel environments are listed as 3 linear tracks, 3 figure-eight mazes and 1 arena, which is 7, but every test has 7 degrees of freedom, which implies 8 sessions. The author takes every session that fits the description and reports the count. Where a session has two novel environments, the paper doesn't say which was used, so both the first and the second are run.
- **Cell types:** no thresholds are given for separating pyramidal cells. The criteria use the dataset's own labels.
- **Nearest-neighbour search:**
  - The 1×1 cm location bin is borrowed from the place-field section.
  - Only the bin itself is excluded, because the text says "any other moment".
  - Speed filter: either none or 5 cm/s.
  - Nearest neighbours for the movement differences: 3 (Methods) or 1 (Figure S7C legend).
- **"Minute 10":** either 600 to 660 s (as Figure 8B states) or 540 to 600 s.
- **Decorrelation fit (Figure S6):** the "100-s moving average" is read either as the 60 s windows the figure labels or as a 100 s window. The fitted form is R = β·exp(−lag/τ) + c, and the decay rate is 1/τ.
- **Speed and acceleration:** either the Kalman filter used for the photometry mice or smoothed finite differences.
- **Figure S7E/F model:** either the two-exponential form of the photometry model or a linear model.
- **Ripples:** the recording channel is not named. The pre-experience window is either the 30 min before the novel run or the first 30 min of the recording day. The track vectors are either z-scored or raw counts.
- **Tests:** t(7) over 8 sessions is read as a paired t-test. Two-sided is a standard choice.
- **Claims where the paper gives no test or measure:** the UMAP embedding, in-field versus out-of-field firing, the movement differences over time, and the absence of pre-experience reactivation. Their criteria use a standard choice and mark it as an assumption.

**Missing from the paper:** the photometry data, so 13 claims cannot be tested. No analysis code exists to settle the open choices above.

## End of run

18 turns, 4 minutes, $1.44 at API prices, result: success.
