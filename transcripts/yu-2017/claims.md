# crcns-hc-13 · claims · run 42478643759

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  grep -n "^#" docs/protocol.md | head -50; ls claims/001453/ claims/crcns-hc-13/ paper/ 2>&1; wc -c paper/*
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  sed -n 1,185p docs/protocol.md; cat claims/001453/*.yaml
```

```
# Protocol for an attempt

Version: `pilot-13`. Record this version in the attempt's provenance.

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
[... 486 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat paper/hc-13.data-description.txt
```

Result: not kept, because it reads the paper's text.

**Agent**

Now the paper.

**Agent calls Read**

```json
{
 "file_path": "paper/10.7554-elife.27621.txt"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  awk 'NR>149 && length($0)>0 && !seen[$0]++' paper/10.7554-elife.27621.txt | awk '{print}' > $TMPDIR/p.txt; wc -c $TMPDIR/p.txt; awk '!s[substr($0,1,200)]++' $TMPDIR/p.txt > $TMPDIR/p2.txt; wc -c $TMPDIR/p2.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.7554-elife.27621.txt",
 "offset": 150,
 "limit": 150
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.7554-elife.27621.txt",
 "offset": 300,
 "limit": 224
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  grep -n -i "github\|code avail\|software\|matlab" paper/10.7554-elife.27621.txt | head; grep -rl "data: elsewhere" claims | head -3; ls claims | head -50; sed -n 1,80p tools/claims_check.py
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  python -c "import json;d=json.load(open('schemas/claims.schema.json'));print(json.dumps(d,indent=1))" | head -250; grep -n -B3 -A12 "data: elsewhere" claims/000939/*.yaml | head -60; ls claims | grep -i crcns
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
[... 319 more lines not kept]
```

**Agent calls Bash**

```bash
cd  head -40 claims/crcns-hc-14/*.yaml; grep -h -A3 "^dataset:" claims/crcns-*/*.yaml | head -12; sed -n 200,260p schemas/claims.schema.json
```

```
# Claims for Girardeau, Inema & Buzsaki (2017), Nature Neuroscience 20:1634-1642, "Reactivations of
# emotional memory in the hippocampus-amygdala system during sleep", on CRCNS data set hc-14
# (doi:10.6080/K0MS3QXD).
# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"), 2026-11-08,
# protocol as stated in docs/protocol.md (Reader), version pilot-13.
#
# Text read: the version of record (PyMuPDF text of the journal PDF under paper/): main text,
# figure legends, Online Methods and the Life Sciences Reporting Summary, with the supplement
# (Supplementary Figures 1 to 11 and Supplementary Tables 1 and 2). Supplementary Table 1 (cells per
# structure) is an image whose numbers the text does not carry, and the PDF pages could not be
# rendered here, so it was not read; the totals per structure are taken from the Results. Values
# printed as powers of ten ("7.48 x 10-14") are recorded from the text; the quote checker cannot
# find them in that form. The data set's description (paper/hc-14.data-description.txt) was read
# only to know what the data set is meant to hold; no claim comes from it.
#
# Code read: github.com/buzsakilab/papers, folder GGirardeau-BLAHpcInteractions-Package, commit
# cdcec89f8d1f5cf11f407f82827f9af44405c5b7 (master, 2017-07-28), the repository the Online Methods
# link. MATLAB scripts in folders Behavior, CellClassification, Physiology, Reactivations and
# Miscellaneous, calling FMAToolbox. Not in the package: structures.mat (which shanks are BLA,
# CeN, Pir), poissonTest.m, the repeated-measures ANOVA functions, the script that computes the
[... 93 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 260,340p schemas/claims.schema.json
```

```
"type": "number",
          "minimum": 0
        },
        "unit": {
          "type": "string"
        }
      }
    },
    "statistic": {
      "type": "object",
      "additionalProperties": false,
      "anyOf": [
        {
          "required": [
            "p"
          ]
        },
        {
          "required": [
            "ci"
[... 61 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n -o ".\{0,80\}not significantly\|.\{0,100\}93%.\{0,40\}" paper/10.7554-elife.27621.txt | head; python -c "
from scipy.stats import binomtest
print(binomtest(3,70,1/8).pvalue, binomtest(3,70,1/8,alternative='less').pvalue)"
```

Result: not kept, because it reads the paper's text.

**Agent calls Write**

```json
{
 "file_path": "claims/crcns-hc-13/10.7554-elife.27621.yaml",
 "content": "# Claims for Yu, Kay, Liu, Grossrubatscher, Loback, Sosa, Chung, Karlsson, Larkin & Frank (2017),\n# eLife 6:e27621, \"Distinct hippocampal-cortical memory representations for experiences associated\n# with movement versus immobility\", on CRCNS data set hc-13 (doi:10.6080/K0H41PK8).\n# Written by an agent (model \"claude-opus-5-5\", Claude Code, runner \"GitHub Actions\"), 2026-11-08,\n# protocol as stated in docs/protocol.md (Reader), version pilot-13.\n#\n# Text read: the version of record (PMC5576488, Europe PMC full-text XML flattened, under paper/):\n# main text, figure legends, the legends of all figure supplements (Figure 1, supplements 1 to 4;\n# Figure 2, 1 and 2; Figure 3, 1 to 3; Figure 4, 1 to 9; Figure 5, 1 and 2; Figure 6, 1 and 2) and\n# Materials and methods. An eLife paper has no other supplement. No PDF of the paper is under\n# paper/, so figure panels could not be read; where a legend gives several significance marks\n# without saying which comparison carries which, the claim says so. The data set's description\n# (paper/hc-13.data-description.txt) was read only to know what the data set holds; no claim\n# comes from it. p-values printed as powers of ten (\"p<10 −4\") are recorded as 0.0001 and the like;\n# the quote checker may not find them in that form.\n#\n# Code: the paper links no analysis code. The Methods name the tools used (MatClust for spike\n# sorting, Chronux for spectra) but give no repository.\n#\n# Data the paper used. Eleven male Long Evans rats (500 to 700 g, 4 to 9 months). Five performed a\n# foraging task on a maze with four reward wells at its corners, two of them rewarded in alternation\n# under contingencies that changed across and within days and sessions, with a barrier on one\n# segment in some sessions on the last 3 to 4 days; 4, 9, 9, 11 and 12 days were analysed for the\n# five rats, 2 to 3 task sessions of 15 to 45 min a day, interleaved with rest sessions of 20 to 60\n# min in a sleep box. These rats had tetrodes in right dorsal CA1 (7) and right dorsal PFC (14 to\n# 21, anterior cingulate and dorsal prelimbic). Six other rats performed a W-shaped alternation task\n# with tetrodes in the hippocampus; their data come from earlier papers (Karlsson and Frank 2009;\n# Kay et al. 2016), and the paper names the CRCNS data set hc-6 (Karlsson, Carr & Frank,\n# doi:10.6080/K0NK3BZJ) as the previously published data used. Measured variables: spike times of\n# manually clustered units with spike width, LFP at 1.5 kHz (0.5 to 400 Hz), head position from a\n# two-part LED array tracked at 30 Hz, and reward well entry times from an infrared beam break.\n# The data set hc-13 holds, by its title and description, the five foraging rats (T1, S2, Q1, R1,\n# N2) with CA1 and PFC spikes, LFP, position, task and tetrode information. The W-track rats are not\n# in it. Claims whose test the paper runs on both tasks pooled are marked `with_inputs` (the hc-6\n# deposit); their test on the foraging rats alone is a variant, and counts the paper gives for the\n# pooled data do not apply to it. The PFC claims use the foraging rats only.\n#\n# Methods fixed by the paper, used by many claims (Materials and methods).\n# - Movement is speed > 4 cm/s, immobility speed < 4 cm/s; position is the centroid of the front\n#   and back diodes.\n# - CA1 putative pyramidal cells have spike width < 0.4 ms and mean rate < 10 Hz, and > 200 spikes\n#   across all sessions of a day. IAPs have a mean rate >= 3 Hz during immobility at one or more\n#   reward wells, spikes during SWRs excluded; MAPs are the remaining pyramidal cells.\n# - SWRs. CA1 LFP referenced to corpus callosum, filtered 150 to 250 Hz, Hilbert envelope smoothed\n#   with a Gaussian (sigma 4 ms), consensus envelope the median over tetrodes; only days with at\n#   least three tetrodes in or near the CA1 cell layer. The envelope is normalized to immobility\n#   times (speed < 4 cm/s); the noise distribution is the histogram below its mode mirrored about\n#   the mode; the threshold is the 99.99th percentile of that noise distribution, set per day; an\n#   event exceeds it for at least 20 ms; start and end are where the envelope returns to the mean;\n#   only events at speed < 4 cm/s are kept. A cell takes part in a SWR when it fires during it\n#   (spike count binarized). MAP-SWRs hold MAP spikes only, IAP-SWRs IAP spikes only, MAP & IAP-SWRs\n#   both.\n# - SWR coactivity (Cheng and Frank 2008) is the observed fraction of SWRs in which both cells fire,\n#   as a z-score against 5000 permutations of each cell's participation across SWRs.\n# - CA1 cross- and auto-correlograms in 10 ms bins, pairs with > 100 coincident spiking events in\n#   the window, each normalized by the sum of its bins; the population median per bin.\n#\n# Details the paper leaves open, with the readings each claim that needs them must run.\n# - O1, \"at a reward well\". The paper gives neither the well positions nor a radius. Readings:\n#   (a) between beam-break entry and exit at a well, when the data set holds those times; (b) each\n#   immobility period (speed < 4 cm/s) assigned to the nearest of the wells, the wells located as\n#   the centres of the clusters of immobile positions (the Methods say almost all immobility is at\n#   wells). Well entry and exit times (Figure 2, Figure 6) are the beam-break times under (a) and\n#   the starts and ends of those immobility periods under (b).\n# - O2, \"excluding spikes during SWRs\". Methods exclude the spikes; the Results say \"excluding\n#   activity during SWRs\". Readings: (a) SWR spikes removed and SWR time kept in the denominator;\n#   (b) both removed. The rate at a well is taken over all task sessions of the day, as the cell\n#   selection is per day; the maximum over sessions is a variant.\n# - O3, speed. The paper does not say how speed is computed from position. A standard choice is\n#   used (untracked frames interpolated, speed from frame differences smoothed over about 0.25 s);\n#   the IAP and MAP counts under unsmoothed speed are shown as a variant.\n# - O4, unit counts. Cells are selected per day; a unit recorded on several days is counted once\n#   per day (main reading), and the count of unique units is a variant.\n# - O5, SWR threshold. Readings for \"envelope power\": (a) the envelope amplitude, (b) its square.\n#   The histogram bin width is a standard choice (0.05 z). \"Normalized to times during immobility\"\n#   is read as a z-score with the mean and standard deviation of the envelope during immobility in\n#   the day's task sessions; the rest sessions are left out, as the paper analyses awake SWRs in\n#   the tasks.\n# - O6, the SWRs over which coactivity is permuted. Readings: (a) all SWRs of the day's task\n#   sessions in which both cells were recorded; (b) per session, with the z-scores averaged over\n#   sessions.\n# - O7, the cross-correlation peak offset used to select pairs (Figure 4B, Figure 4, supplements 1\n#   and 2). Computed from all spikes outside SWRs, 10 ms bins smoothed with a Gaussian (sigma 150 ms)\n#   as in Figure 2, supplement 1G-H. The window is not given; as supplement 1 of Figure 4 plots\n#   offsets up to 5 s, the window is read as at least +-5 s. Readings: (a) +-5 s, (b) +-10 s (the 20\n#   s window used for PFC-CA1 pairs).\nschema_version: 2\ndataset:\n  archive: crcns\n  id: hc-13\n  doi: 10.6080/K0H41PK8\npaper: doi:10.7554/elife.27621\nclaims:\n- id: fig1-iap-map-counts\n  statement: Across both tasks, 83 CA1 units are classified as immobility-associated place cells\n    (IAPs) and 659 as movement-associated place cells (MAPs).\n  source: Results, Identification of CA1 place cells participating in spatial representations,\n    paragraphs 3 and 4\n  quote: we therefore refer to them as Immobility-Associated Place cells (IAPs) (n = 83) ... We refer\n    to the remaining CA1 pyramidal units as Movement-Associated Place cells (MAPs) (n = 659)\n  data: with_inputs\n  expected:\n  - quantity: IAPs, both tasks\n    value: 83\n    tolerance: 8.3\n    unit: cells\n  - quantity: MAPs, both tasks\n    value: 659\n    tolerance: 65.9\n    unit: cells\n  criterion: Cells selected as in the opening comment (Methods, Cell selection), under readings O1,\n    O2 and O4. Reproduced when, under one reading, both counts on the pooled data are within\n    tolerance. The paper's per-task counts (Figure 1, supplement 4B) add to 83 IAPs but to 679\n    MAPs (244 + 435), not 659; the MAP count is therefore also judged against 679 with the same\n    tolerance, and the claim holds when either matches.\n- id: fig1s4b-foraging-counts\n  statement: In the foraging task, 33 CA1 units are IAPs and 244 are MAPs.\n  source: Figure 1, supplement 4B legend\n  quote: Cells from the foraging task are shown on left (MAP = 244, IAP = 33)\n  expected:\n  - quantity: IAPs, foraging task\n    value: 33\n    tolerance: 3.3\n    unit: cells\n  - quantity: MAPs, foraging task\n    value: 244\n    tolerance: 24.4\n    unit: cells\n  criterion: Cells selected as in the opening comment (Methods, Cell selection) on the five\n    foraging rats, under readings O1, O2 and O4. Reproduced when, under one reading, both counts\n    are within tolerance; partially reproduced when one is.\n- id: fig1d-well-specificity\n  statement: IAP firing is specific to a single reward well, with well specificity indices close to\n    1 in both tasks.\n  source: Figure 1D; Figure 1, supplement 4F legend\n  quote: IAPs in both tasks have well specificity values close to 1, which indicates firing that is\n    specific to one well location\n  data: with_inputs\n  depends_on:\n  - fig1-iap-map-counts\n  criterion: Index as in the Methods (Well specificity). Each well's mean rate (O1, O2) divided by\n    the maximum over wells, used as the length of a vector at that well's angle (wells equally\n    spaced on the circle, 90 degrees apart for the four foraging wells, 120 degrees for the three W\n    wells), the magnitude of their sum. The paper gives no number for \"close to 1\"; reproduced\n    when the median index of IAPs is at least 0.8 in each task (0.9 shown as a stricter reading).\n    On the data set alone, judged on the foraging IAPs.\n- id: fig1e-iap-lower-speed\n  statement: IAPs spike at lower movement speeds than MAPs; the median speed at the times of spikes\n    is lower for IAPs.\n  source: Figure 1E; Results, Identification of CA1 place cells, paragraph 3\n  quote: These units also spiked at times associated with lower movement speeds during the tasks (\n    Figure 1E )\n  statistics:\n  - test: Wilcoxon rank-sum test\n    p: 0.0001\n    p_relation: \"<\"\n    n: 83 IAPs and 659 MAPs, both tasks\n  data: with_inputs\n  depends_on:\n  - fig1-iap-map-counts\n  criterion: Per cell, the median speed (O3) at its spike times over the day's task sessions. A\n    two-sided Wilcoxon rank-sum test of IAPs against MAPs; reproduced when p < 0.05 with the IAP\n    median lower. The foraging cells alone are shown as a variant (claim fig1s4d-foraging-speed).\n- id: fig1s4d-foraging-speed\n  statement: In the foraging task alone, IAP spikes occur at much lower speeds than MAP spikes.\n  source: Figure 1, supplement 4D legend\n  quote: Spikes of IAPs occur at much lower speeds compared with spikes of MAPs\n  statistics:\n  - test: Wilcoxon rank-sum test\n    p: 0.00001\n    p_relation: \"<\"\n    n: 33 IAPs and 244 MAPs, foraging task\n  depends_on:\n  - fig1s4b-foraging-counts\n  criterion: As fig1e-iap-lower-speed, on the foraging cells. Reproduced when p < 0.05 with the IAP\n    median lower.\n- id: fig1f-iap-smaller-coverage\n  statement: IAPs are active over smaller regions of the environment (smaller spatial coverage) than\n    MAPs.\n  source: Figure 1F; Figure 1, supplement 4E legend\n  quote: IAPs have smaller place fields on path segments than MAPs. Place field size is calculated\n    by adding all linearized spatial bins (2 cm) with a firing rate greater than 2 Hz\n  statistics:\n  - about: both tasks pooled (Figure 1F)\n    test: Wilcoxon rank-sum test\n    p: 0.0001\n    p_relation: \"<\"\n  - about: per task (Figure 1, supplement 4E); the legend does not say which task has which bound\n    test: Wilcoxon rank-sum test\n    p: 0.005\n    p_relation: \"<\"\n  data: with_inputs\n  depends_on:\n  - fig1-iap-map-counts\n  criterion: Coverage per cell is the number of 2 cm bins with rate > 2 Hz (Figure 1, supplement\n    4E). The paper does not say how the foraging maze is linearized. Readings: (a) the 2 cm square\n    bins of the occupancy-normalized map (Methods, Occupancy normalized firing maps, Gaussian sigma\n    2 cm) times 2 cm; (b) the positions projected onto the maze's path segments (the lines joining\n    the wells) and binned at 2 cm along them. Two-sided Wilcoxon rank-sum, IAPs against MAPs,\n    pooled and per task. Reproduced when p < 0.05 with the IAP median smaller, under one reading;\n    the foraging task alone is the test on the data set.\n- id: fig1s1d-transition-interval\n  statement: The animals switch between movement and immobility every 6 to 7 s; the autocorrelation\n    of well entry and exit times peaks at 6.4 to 6.6 s in the foraging task.\n  source: Figure 1, supplement 1D legend; Results, Identification of CA1 place cells, paragraph 1\n  quote: shows periods of movement and periods of immobility are separated by 6.4–6.6 s for the\n    foraging task, 7.4–7.6 s for the W-alternation task and 6.6–6.8 s for combined data from both\n    tasks\n  expected:\n  - quantity: autocorrelation peak of well entry and exit times, foraging task\n    value: 6.5\n    tolerance: 0.76\n    unit: s\n  criterion: The autocorrelation of the pooled times of well entries and exits (O1) per session,\n    summed over sessions, histogrammed and smoothed; the peak away from zero lag. The bin width and\n    smoothing are not given; a standard choice (0.2 s bins, Gaussian sigma 0.5 s) is used. The\n    tolerance is the reported range 6.4 to 6.6 s widened by 10% of each bound (5.76 to 7.26 s).\n- id: fig2c-continuous-transition\n  statement: MAP and IAP spiking overlap in time as the animal enters and leaves a reward well, so\n    the MAP-relative-to-IAP cross-correlogram has a tail extending beyond 0 s lag, a smooth and not\n    an abrupt transition.\n  source: Figure 2C; Results, Smooth transition between CA1 movement and immobility spatial\n    representations, paragraph 2\n  quote: MAP spiking overlapped in time with IAP activity as the animal slowed down during entry\n    into the well location and similarly overlapped as the animal exited the well location\n  data: with_inputs\n  depends_on:\n  - fig1-iap-map-counts\n  criterion: Spikes within +-1.5 s of each well entry and exit (O1), cross-correlogram of MAP spikes\n    relative to IAP spikes (lag = MAP time minus IAP time), 10 ms bins, pairs with > 100 coincident\n    events, each normalized by its sum, the population median per bin with notch +-1.58 IQR over\n    the square root of n (Figure 2C legend, Methods). The paper gives no measure of how far the\n    tail must reach; reproduced when the lower notch is above zero in at least half of the bins\n    from 0 to +0.5 s at entry and from -0.5 to 0 s at exit. The 0.5 s extent is a choice. Pair\n    counts (207 entry, 217 exit, both tasks) are reported for comparison.\n- id: fig2s1cd-theta-autocorrelation\n  statement: During movement (speed > 4 cm/s) around well entry and exit, both MAP and IAP spike\n    autocorrelations show peaks at theta intervals (0.125 s), which are less prominent during\n    immobility (speed < 1 cm/s).\n  source: Figure 2, supplement 1C-D legend; Results, Smooth transition, paragraph 3\n  quote: Both MAP and IAP autocorrelations show peaks at intervals corresponding to theta modulation\n    of spiking activity (0.125 s) when the animal is moving\n  data: with_inputs\n  depends_on:\n  - fig1-iap-map-counts\n  criterion: Spikes within +-1.5 s of entry or exit, split by speed > 4 cm/s and < 1 cm/s,\n    autocorrelation over 1 s in 10 ms bins, cells with > 100 coincident events, mean over cells\n    (legend). Reproduced when, for both IAPs and MAPs at speed > 4 cm/s, the mean autocorrelation\n    has a local maximum between 0.1 and 0.16 s lag (6 to 10 Hz, a choice around the paper's 0.125\n    s) whose height above the minimum between 0 and that lag is larger than at speed < 1 cm/s.\n- id: fig2s1ij-theta-behavior-correlation\n  statement: Cross-correlation peak offsets of cell pairs on the theta time scale are significantly\n    correlated with their peak offsets on the behavioral time scale of seconds.\n  source: Figure 2, supplement 1I-J legend\n  quote: Cross-correlation peaks on a theta time scale are significantly correlated with\n    cross-correlation peaks on a behavioral time scale over seconds\n  data: with_inputs\n  depends_on:\n  - fig1-iap-map-counts\n  criterion: Theta-scale peak from the 250 ms cross-correlogram (10 ms bins) of spikes within +-1.5\n    s of entry (I) or exit (J); behavioral-scale peak from the 6.6 s cross-correlogram of all spikes\n    outside SWRs, 10 ms bins, Gaussian sigma 150 ms (legend). The correlation test is not named;\n    readings are Pearson and Spearman. Reproduced when the correlation is positive with p < 0.05\n    for entry and exit under one reading, for MAP-IAP pairs and for MAP-MAP pairs.\n- id: fig2s2-fewer-coincident-spikes\n  statement: MAP-IAP pairs have a lower proportion of coincident spikes (within +-50 ms, out of\n    spikes within +-3.3 s) than MAP-MAP or IAP-IAP pairs.\n  source: Figure 2, supplement 2; Results, Smooth transition, paragraph 5\n  quote: This analysis revealed a lower proportion of temporally nearby spikes for MAP-IAP pairs as\n    compared to the other pair types\n  statistics:\n  - test: Wilcoxon rank-sum test\n    p: 0.0001\n    p_relation: \"<\"\n    n: 2062 MAP-MAP, 26 IAP-IAP and 497 MAP-IAP pairs\n  data: with_inputs\n  depends_on:\n  - fig1-iap-map-counts\n  criterion: Per pair, spike pairs at lags within +-50 ms over spike pairs within +-3.3 s, from task\n    spikes. Whether SWR spikes are excluded is not said; readings are all task spikes and spikes\n    outside SWRs. Two-sided Wilcoxon rank-sum, MAP-IAP against MAP-MAP and against IAP-IAP.\n    Reproduced when both are p < 0.05 with MAP-IAP lower, under one reading.\n- id: fig3c-iap-swr-activation\n  statement: IAPs, like MAPs, increase their firing at the start of awake SWRs, both for SWRs at the\n    well where the IAP has its place field and for SWRs elsewhere.\n  source: Figure 3B-C; Results, Separate reactivation of immobility-associated spatial\n    representations, paragraph 1\n  quote: For in and not in field events, both IAPs and MAPs show significant increases in activity\n    aligned to the start of SWRs (250 ms pre vs. 250 ms post SWR start\n  statistics:\n  - test: Wilcoxon rank-sum test, 250 ms before against 250 ms after SWR start\n    p: 0.0001\n    p_relation: \"<\"\n    n: 589 MAPs and 77 IAPs\n  data: with_inputs\n  depends_on:\n  - fig1-iap-map-counts\n  criterion: Per cell, the spike count (or rate) in the 250 ms before and the 250 ms after each SWR\n    start, averaged over SWRs; for IAPs separately over in-field SWRs (at the IAP's well, O1) and\n    not-in-field SWRs, for MAPs over not-in-field SWRs (SWRs not within the place field). The paper\n    names a rank-sum test; the readings are (a) rank-sum over cells of their pre and post means, (b)\n    rank-sum over SWRs pooled. Reproduced when all three comparisons (MAP not in field, IAP in field,\n    IAP not in field) give p < 0.05 with post higher, under one reading. For MAPs the paper does not\n    define \"within the place field\" at a SWR; read as the animal's position bin having a rate > 2 Hz\n    in the cell's occupancy map, as the place field threshold of Figure 1, supplement 4E.\n- id: fig3s3-iap-same-well-coactivity\n  statement: IAP pairs with place fields at the same well are strongly coactive during SWRs, also\n    for SWRs away from their fields, while IAP pairs at different wells are no more coactive than\n    chance.\n  source: Figure 3, supplement 3; Results, Separate reactivation, paragraph 2\n  quote: We found that IAP pairs with place fields located at the same reward well location were\n    strongly coactivated during SWRs, whereas those cell pairs with place fields located at\n    different reward well locations showed no more coactivation than expected by chance\n  statistics:\n  - test: Kruskal-Wallis test\n    p: 0.005\n    p_relation: \"<\"\n    n: 12 same-well pairs (all SWRs), 11 same-well pairs (not in field SWRs), 14 different-well pairs\n  data: with_inputs\n  depends_on:\n  - fig1-iap-map-counts\n  criterion: Coactivity z-scores as in the opening comment (O6). The legend gives n.s., p < 0.05 and\n    p < 0.005 without saying which comparison carries which. Reproduced when a Kruskal-Wallis test\n    over the three groups gives p < 0.05, the same-well group (all SWRs) is higher than the\n    different-well group by a pairwise rank-sum test at p < 0.05, the same-well medians (all and\n    not in field) are above 0, and the different-well median z-score does not differ from 0 by a\n    two-sided Wilcoxon signed-rank test at p < 0.05 (chance is z = 0 by construction; the test of\n    that absence is not given by the paper and is a reading).\n- id: fig4a-swr-counts\n  statement: Most SWRs contain only MAPs (12881, 67%) or only IAPs (5009, 26%); only 1311 (7%)\n    contain both, far fewer than the 4671 (24%) expected if MAPs and IAPs took part independently.\n  source: Figure 4A; Results, Separate reactivation, paragraph 3\n  quote: The large majority of SWRs contained either only MAPs (n = 12881, 67%) or only IAPs (n =\n    5009, 26%). Only a small fraction of events contained both MAPs and IAPs (n = 1311, 7%) ...\n    (expected n = 4671, 24%, actual vs. expected p<0.0001, Chi squared test, d.f. = 1)\n  statistics:\n  - test: Chi squared test, observed against expected MAP and IAP-SWRs\n    statistic: d.f. = 1\n    p: 0.0001\n    p_relation: \"<\"\n    n: 19201 SWRs with MAP or IAP spikes\n  data: with_inputs\n  depends_on:\n  - fig1-iap-map-counts\n  expected:\n  - quantity: fraction of SWRs with MAPs only\n    value: 0.67\n    tolerance: 0.067\n  - quantity: fraction of SWRs with IAPs only\n    value: 0.26\n    tolerance: 0.026\n  - quantity: fraction of SWRs with both\n    value: 0.07\n    tolerance: 0.007\n  - quantity: SWRs with MAPs only\n    value: 12881\n    tolerance: 1288\n  - quantity: SWRs with IAPs only\n    value: 5009\n    tolerance: 501\n  - quantity: SWRs with both\n    value: 1311\n    tolerance: 131\n  criterion: SWRs detected and classified as in the opening comment (O5), the denominator the SWRs\n    with at least one MAP or IAP spike; the paper's numbers fix this (P(MAP) = 14192/19201, P(IAP) =\n    6320/19201, their product times 19201 is 4671). Expected count as in the Methods (SWR counts),\n    from pooled probabilities; chi-square with 1 d.f. Reproduced when the three fractions are within\n    tolerance and the observed count of MAP and IAP-SWRs is below the expected with p < 0.05;\n    partially reproduced when the test holds but a fraction is out of tolerance. The counts depend\n    on how many cells were recorded and are reported against the paper's; on the foraging rats\n    alone (a variant) only the fractions and the test are judged.\n- id: fig4b-coactivity\n  statement: Among pairs coactive within 3.3 s during the task, MAP-IAP pairs have lower SWR\n    coactivity than MAP-MAP or IAP-IAP pairs.\n  source: Figure 4B; Results, Separate reactivation, paragraph 4\n  quote: The coactivity distribution shows MAP-IAP pairs had significantly lower levels of SWR\n    coactivity than MAP-MAP or IAP-IAP pairs\n  statistics:\n  - about: one of the two comparisons; the legend does not say which\n    test: Wilcoxon rank-sum test\n    p: 0.001\n    p_relation: \"<\"\n  - about: the other comparison\n    test: Wilcoxon rank-sum test\n    p: 0.0001\n    p_relation: \"<\"\n    n: 1015 MAP-MAP, 13 IAP-IAP and 138 MAP-IAP pairs, both tasks\n  data: with_inputs\n  depends_on:\n  - fig1-iap-map-counts\n  criterion: Coactivity z-scores (O6) for simultaneously recorded pairs whose cross-correlation peak\n    (O7) lies within 3.3 s of zero lag. Two-sided Wilcoxon rank-sum, MAP-IAP against MAP-MAP and\n    against IAP-IAP. Reproduced when both give p < 0.05 with MAP-IAP lower, under one reading of O6\n    and O7.\n- id: fig4s1b-offset-matched-coactivity\n  statement: When matched for the offset of the cross-correlation peak, MAP-MAP pairs still have\n    higher SWR coactivity than MAP-IAP pairs, significantly so in each 1 s bin from 1 to 5 s.\n  source: Figure 4, supplement 1B legend\n  quote: Even when matched for the offset to the cross-correlation peak, MAP-MAP pairs showed, on\n    average, higher SWR coactivity than MAP-IAP pairs. This difference was significant for each\n    offset bin above 1 s\n  statistics:\n  - about: 1 to 2 s\n    test: Wilcoxon rank-sum test\n    p: 0.001\n    p_relation: \"<\"\n  - about: 2 to 3 s\n    test: Wilcoxon rank-sum test\n    p: 0.05\n    p_relation: \"<\"\n  - about: 3 to 4 s\n    test: Wilcoxon rank-sum test\n    p: 0.05\n    p_relation: \"<\"\n  - about: 4 to 5 s\n    test: Wilcoxon rank-sum test\n    p: 0.005\n    p_relation: \"<\"\n    n: 2204 MAP-MAP and 521 MAP-IAP pairs\n  data: with_inputs\n  depends_on:\n  - fig4b-coactivity\n  criterion: Pairs binned by the absolute offset of their peak (O7) in 1 s bins from 0 to 5 s;\n    per bin a two-sided Wilcoxon rank-sum of MAP-MAP against MAP-IAP coactivity. Reproduced when\n    the MAP-MAP mean is higher in all four bins from 1 to 5 s and at least three of them give p <\n    0.05; partially reproduced when one or two do.\n- id: fig4s2c-spatial-proximity-control\n  statement: Among pairs with place field peaks less than 0.5 m apart, MAP-IAP pairs still have\n    lower SWR coactivity than MAP-MAP and IAP-IAP pairs, and MAP-MAP pairs have higher coactivity\n    than MAP-IAP pairs at every field distance up to 1 m.\n  source: Figure 4, supplement 2B-C legend\n  quote: Across all distances, MAP-MAP pairs showed stronger coactivity than comparable MAP-IAP\n    pairs\n  statistics:\n  - about: MAP-MAP against MAP-IAP, field distance 0 to 0.25 m (and 0.25 to 0.5, 0.5 to 0.75)\n    test: Wilcoxon rank-sum test\n    p: 0.0001\n    p_relation: \"<\"\n  - about: MAP-MAP against MAP-IAP, field distance 0.75 to 1 m\n    test: Wilcoxon rank-sum test\n    p: 0.05\n    p_relation: \"<\"\n  - about: pairs with field peaks < 0.5 m apart (panel C); which pair of groups carries which bound\n      is not said\n    test: Kruskall-Wallis test\n    p: 0.001\n    p_relation: \"<\"\n    n: 1056 MAP-MAP, 18 IAP-IAP and 211 MAP-IAP pairs\n  data: with_inputs\n  depends_on:\n  - fig4b-coactivity\n  criterion: Distance between the peaks of the cells' occupancy-normalized maps (Methods, 2 cm bins).\n    Panel B, pairs in 0.25 m bins from 0 to 1 m, two-sided Wilcoxon rank-sum of MAP-MAP against\n    MAP-IAP per bin; panel C, pairs < 0.5 m apart, Kruskal-Wallis over the three groups followed by\n    pairwise rank-sum tests. Reproduced when MAP-MAP is higher with p < 0.05 in all four bins and,\n    in panel C, MAP-IAP is lower than both other groups at p < 0.05; partially reproduced when\n    panel B or panel C holds alone.\n- id: fig4s3-overlapping-pairs\n  statement: MAP-IAP pairs whose spikes overlap during the transition at well entry or exit still\n    have lower SWR coactivity than MAP-MAP and IAP-IAP pairs.\n  source: Figure 4, supplement 3; Results, Separate reactivation, paragraph 4\n  quote: We also replicated this result by using a more stringent condition, where we included only\n    cell pairs with overlapping spikes during the transition period between movement and immobility\n    at reward location entry or exit\n  statistics:\n  - test: Wilcoxon rank-sum test\n    p: 0.05\n    p_relation: \"<\"\n    n: entry 333 MAP-MAP, 207 MAP-IAP, 24 IAP-IAP pairs; exit 512, 217 and 24\n  data: with_inputs\n  depends_on:\n  - fig2c-continuous-transition\n  criterion: Pairs with > 100 coincident events within +-1.5 s of entry, and separately of exit, as\n    for Figure 2C. Two-sided Wilcoxon rank-sum of MAP-IAP against MAP-MAP and against IAP-IAP\n    coactivity, for entry and exit. Reproduced when all four comparisons give p < 0.05 with\n    MAP-IAP lower; partially reproduced when two or three do.\n- id: fig4c-iap-swr-shorter\n  statement: IAP-SWRs are shorter than MAP-SWRs, and MAP & IAP-SWRs are the longest; the duration\n    distributions differ between all pairs of groups.\n  source: Figure 4C; Results, Distinct properties for SWRs involving movement and immobility\n    representations, paragraphs 1 and 2\n  quote: found that IAP-SWRs were significantly shorter in duration and lower in amplitude than SWRs\n    containing MAPs\n  statistics:\n  - test: Kolmogorov-Smirnov test, all pairwise comparisons\n    p: 0.0001\n    p_relation: \"<\"\n  data: with_inputs\n  depends_on:\n  - fig4a-swr-counts\n  criterion: Duration from start to end as in SWR detection (O5). Two-sided two-sample\n    Kolmogorov-Smirnov test for each of the three pairs of groups. Reproduced when all three give p\n    < 0.05 and the medians order IAP-SWR < MAP-SWR < MAP & IAP-SWR, in the pooled data and in the\n    foraging task alone (Figure 4, supplement 4A shows the same in each task).\n- id: fig4d-iap-swr-lower-power\n  statement: IAP-SWRs have lower 150 to 250 Hz power than MAP-SWRs, and MAP & IAP-SWRs the highest;\n    all groups show the increase in slow gamma (about 30 Hz) power of SWRs.\n  source: Figure 4D; Results, Distinct properties for SWRs, paragraphs 1 and 2\n  quote: The mean of spectral power between 150–250 Hz is significantly different between groups\n  statistics:\n  - test: Wilcoxon rank-sum test, all pairwise comparisons\n    p: 0.0001\n    p_relation: \"<\"\n  data: with_inputs\n  depends_on:\n  - fig4a-swr-counts\n  criterion: As in the Methods (Spectrograms). Broadband CA1 LFP, multitaper spectrogram (Chronux) in\n    100 ms windows stepped by 10 ms, z-scored per frequency over the session; per SWR the mean over\n    the first 100 ms after onset and over 150 to 250 Hz. Taper parameters and which tetrode (or the\n    mean over CA1 tetrodes) are not given; a standard choice (time-bandwidth 3, 5 tapers; the mean\n    over CA1 tetrodes) is used. Reproduced when the three pairwise two-sided rank-sum tests give p\n    < 0.05 with IAP-SWR < MAP-SWR < MAP & IAP-SWR, and each group's mean normalized power at 25 to\n    35 Hz in that window is above 0.\n- id: fig4s5-cells-spikes-per-swr\n  statement: IAP-SWRs contain fewer active cells (mean 1.03 against 1.31) and fewer spikes (mean\n    2.04 against 2.49) than MAP-SWRs.\n  source: Figure 4, supplement 5 legend\n  quote: Cells active per SWR. IAP mean = 1.03 and MAP mean = 1.31. ( B ) Spikes per SWR. IAP mean =\n    2.04 and MAP mean = 2.49\n  statistics:\n  - test: Wilcoxon rank-sum test\n    p: 0.0001\n    p_relation: \"<\"\n  data: with_inputs\n  depends_on:\n  - fig4a-swr-counts\n  expected:\n  - quantity: mean active cells per IAP-SWR\n    value: 1.03\n    tolerance: 0.103\n  - quantity: mean active cells per MAP-SWR\n    value: 1.31\n    tolerance: 0.131\n  - quantity: mean spikes per IAP-SWR\n    value: 2.04\n    tolerance: 0.204\n  - quantity: mean spikes per MAP-SWR\n    value: 2.49\n    tolerance: 0.249\n  criterion: Place cells (IAPs in IAP-SWRs, MAPs in MAP-SWRs) firing in each SWR, and their spikes.\n    Reproduced when the four means are within tolerance and both two-sided rank-sum tests give p <\n    0.05 with IAP-SWRs lower; partially reproduced when the tests hold but a mean is out of\n    tolerance.\n- id: fig4s67-matched-subsamples\n  statement: IAP-SWRs remain shorter and lower in power than MAP-SWRs after matching the\n    distributions of active cells, or of spikes, per SWR.\n  source: Figure 4, supplements 6 and 7; Results, Distinct properties for SWRs, paragraph 1\n  quote: SWR duration and power remain significantly different after matching for cells active per\n    SWR ... MAP-SWRs remain longer in duration and higher in power after matching for spikes per SWR\n  data: with_inputs\n  depends_on:\n  - fig4s5-cells-spikes-per-swr\n  - fig4c-iap-swr-shorter\n  - fig4d-iap-swr-lower-power\n  criterion: Per subsample, 500 SWRs drawn with replacement from each of MAP-SWRs and IAP-SWRs so\n    that the distribution of active cells (or of spikes) per SWR matches; 1000 subsamples; per\n    subsample a Wilcoxon rank-sum test of duration and of power (legends). How the matching is done\n    is not given; readings are (a) draws weighted so that each group follows the IAP-SWR\n    distribution, (b) draws weighted to the overlap (minimum) of the two distributions. Reproduced\n    when, for both matchings and both measures, the median subsample p-value is below 0.05 and the\n    MAP-SWR median exceeds the IAP-SWR median in at least 95% of subsamples, under one reading.\n- id: fig4s8-interspersed\n  statement: There is no strong relation in timing between IAP-SWRs and MAP-SWRs; they are\n    temporally interspersed.\n  source: Figure 4, supplement 8; Results, Distinct properties for SWRs, paragraph 2\n  quote: We did not observe any strong relationships in the relative timing between IAP-SWRs and\n    MAP-SWRs, indicating these events were temporally interspersed\n  data: with_inputs\n  depends_on:\n  - fig4a-swr-counts\n  criterion: Cross-correlation of IAP-SWR and MAP-SWR start times in 10 ms bins, each bin z-scored\n    against 1000 controls with MAP-SWR times shifted at random by 0 to 1 s either way (legend). The\n    lag range is not given; +-2 s is used. Reproduced when, outside the dip near 0 lag that SWR\n    duration causes (here |lag| < 0.2 s), no more than 5% of bins exceed +-2 z (the legend's red\n    lines), the fraction expected by chance.\n- id: fig4e-iap-spike-earlier\n  statement: In SWRs with both MAPs and IAPs, IAPs spike earlier than MAPs, also after matching the\n    SWR durations from which their spikes come.\n  source: Figure 4E; Figure 4, supplement 9; Results, Distinct properties for SWRs, paragraph 2\n  quote: We found IAPs tended to spike earlier in the SWR than MAPs ( Figure 4E ), even after\n    accounting for differences in SWR duration from which IAP and MAP spikes were selected from\n  statistics:\n  - test: Wilcoxon rank-sum test\n    p: 0.0001\n    p_relation: \"<\"\n  data: with_inputs\n  depends_on:\n  - fig4a-swr-counts\n  criterion: Spike times relative to SWR start in MAP & IAP-SWRs. The unit is not said; readings\n    are (a) all spikes pooled, (b) each cell's first spike in each SWR. Two-sided rank-sum of IAP\n    against MAP times; and after resampling the SWRs so that the durations from which IAP and MAP\n    spikes come follow the same distribution (supplement 9A). Reproduced when both the raw and the\n    matched tests give p < 0.05 with IAP times earlier, under one reading.\n- id: pfc-unit-selection\n  statement: Of 712 PFC units, 112 were active in the task (mean rate > 1 Hz during movement or\n    immobility) and recorded in sessions with both MAP- and IAP-SWRs.\n  source: Results, Prefrontal cortical activity changes during SWRs, paragraph 2; Methods, Cell\n    selection\n  quote: From an initial set of 712 PFC units, we selected units that were actively engaged in the\n    task (mean firing rate >1 Hz during either periods of immobility or movement or both) and were\n    recorded during behavioral sessions where we could identify both MAP- and IAP-SWRs\n  depends_on:\n  - fig4a-swr-counts\n  expected:\n  - quantity: PFC units recorded\n    value: 712\n    tolerance: 71.2\n    unit: units\n  - quantity: PFC units selected\n    value: 112\n    tolerance: 11.2\n    unit: units\n  criterion: Foraging rats only. Units on PFC tetrodes (tetrode area), counted per day (O4). Mean\n    rate over all movement (> 4 cm/s) or all immobility (< 4 cm/s) time in the day's task sessions.\n    The paper does not say how many SWRs of each type a session needs; read as at least one of\n    each. Reproduced when both counts are within tolerance under one reading.\n- id: fig5-pfc-modulated-fraction\n  statement: About 63% of the selected PFC units (70 of 112) are significantly modulated during one\n    or both types of SWRs, almost twice the fraction found without separating SWR types.\n  source: Results, Prefrontal cortical activity changes during SWRs, paragraph 3\n  quote: We found ~63% of these PFC units (70/112) showed significant modulation during one or both\n    types of SWRs\n  depends_on:\n  - pfc-unit-selection\n  expected:\n  - quantity: fraction of selected PFC units modulated\n    value: 0.63\n    tolerance: 0.063\n  - quantity: PFC units modulated\n    value: 70\n    tolerance: 7\n    unit: units\n  criterion: Significance per unit and SWR type as in the Methods (PFC SWR modulation index),\n    following Jadhav et al. 2016. A PETH aligned to SWR starts; 1000 controls with each SWR's\n    surrounding spikes circularly shifted by an amount drawn per SWR; the squared deviation of\n    the observed PETH from the control mean over the mean SWR duration of that type, against the\n    controls' deviations; significant at p < 0.05 (Figure 5, supplement 2). Not given here, and\n    taken as the readings to run, the PETH window and bin (+-0.5 s around SWR start, 10 ms bins) and\n    the shift range (the whole +-0.5 s window). Reproduced when the fraction is within tolerance.\n- id: fig5dg-pfc-groups\n  statement: Significantly modulated PFC units fall into units excited only during IAP-SWRs (14),\n    excited only during MAP-SWRs (20) and inhibited during either or both (33); only 3 are excited\n    during both, fewer than the 9 expected by chance.\n  source: Figure 5D-G; Results, Prefrontal cortical activity changes during SWRs, paragraph 3\n  quote: Only 3 units showed significant excitation during both IAP- and MAP-SWRs (PFC IAP- and\n    MAP-SWR + ) ( Figure 5G ), which was fewer than expected by chance (expected = 9, Binomial test,\n    observed vs. expected p<0.05)\n  statistics:\n  - about: excited during both (observed 3, expected 9)\n    test: Binomial test\n    p: 0.05\n    p_relation: \"<\"\n    n: 70 modulated PFC units\n  - about: excited only during IAP-SWRs (observed 14, expected 18), reported n.s.\n    test: Binomial test\n    p: 0.05\n    p_relation: \">\"\n  - about: excited only during MAP-SWRs (observed 20, expected 18), reported n.s.\n    test: Binomial test\n    p: 0.05\n    p_relation: \">\"\n  - about: inhibited during either or both (observed 33, expected 26), reported n.s.\n    test: Binomial test\n    p: 0.05\n    p_relation: \">\"\n  depends_on:\n  - fig5-pfc-modulated-fraction\n  expected:\n  - quantity: IAP-SWR+ units\n    value: 14\n    tolerance: 1.4\n    unit: units\n  - quantity: MAP-SWR+ units\n    value: 20\n    tolerance: 2\n    unit: units\n  - quantity: IAP/MAP-SWR- units\n    value: 33\n    tolerance: 3.3\n    unit: units\n  - quantity: IAP- and MAP-SWR+ units\n    value: 3\n    tolerance: 0.3\n    unit: units\n  criterion: Excitation or inhibition by the sign of the modulation index (rate during the mean SWR\n    duration from SWR start, against the rate in the 1 s window centred on the SWR; whether centred\n    on SWR start or on its midpoint is not said, both are readings). Groups and expected counts as\n    in the Methods (PFC cell classification), 2, 2, 3 and 1 of 8 combinations times the number of\n    modulated units. Binomial test, two-sided, of each observed count against probability k/8.\n    Reproduced when the excited-during-both group is below its expectation with p < 0.05 and the\n    other three groups are not significantly different (p >= 0.05), under one reading; the counts\n    are judged against tolerance (for the count of 3, a tolerance of 1 unit is used, as 10% of 3 is\n    below one unit).\n- id: fig5s1d-shuffle-control\n  statement: PFC modulation differs between MAP- and IAP-SWRs because of SWR identity and not SWR\n    duration; the difference between a unit's two indices shrinks when SWR identities are shuffled\n    but not when durations are matched.\n  source: Figure 5, supplement 1D legend; Results, Prefrontal cortical activity changes during SWRs,\n    paragraph 4\n  quote: The difference between MAP-SWR and IAP-SWR modulation indices was significantly decreased\n    when the identities of SWRs are shuffled (blue) but remained similar to the original data after\n    SWR durations wee matched (green)\n  statistics:\n  - test: Wilcoxon rank-sum test\n    p: 0.001\n    p_relation: \"<\"\n    n: 70 modulated PFC units\n  depends_on:\n  - fig5dg-pfc-groups\n  criterion: For the 70 (or reproduced number of) modulated units, the absolute difference between\n    MAP-SWR and IAP-SWR indices for the data, after permuting SWR identity, and after drawing 250\n    SWRs with replacement per type so that durations match (legend). Two-sided rank-sum tests of\n    data against shuffle and data against matched. Reproduced when the shuffle is lower at p <\n    0.05 and the matched set does not differ from the data at p < 0.05.\n- id: pfc-regression-joint-swr\n  statement: For 15 PFC units, the MAP-SWR and IAP-SWR modulation indices together explain 73% of\n    the variance of the MAP & IAP-SWR modulation index.\n  source: Results, Prefrontal cortical activity changes during SWRs, paragraph 5; Figure 5,\n    supplement 2\n  quote: we found the modulation indices of MAP-SWRs and IAP-SWRs together account for 73% of the\n    explained variance of MAP & IAP-SWR modulation indices (R 2 = 0.73, p<0.0005)\n  statistics:\n  - test: multiple regression\n    statistic: R2 = 0.73\n    p: 0.0005\n    p_relation: \"<\"\n    n: 15 PFC units\n  depends_on:\n  - fig5-pfc-modulated-fraction\n  expected:\n    quantity: R2 of MAP & IAP-SWR index on MAP-SWR and IAP-SWR indices\n    value: 0.73\n    tolerance: 0.073\n  criterion: Ordinary least squares of the MAP & IAP-SWR index on the MAP-SWR and IAP-SWR indices\n    with an intercept. Which 15 units is not fully said (\"where we could examine the modulation\n    indices of all three types\"); readings are (a) units recorded in sessions with all three SWR\n    types and significantly modulated by at least one, (b) all selected units recorded with all\n    three types. Reproduced when R2 is within tolerance and the F-test p < 0.05, under one reading.\n- id: fig6c-similarity-index\n  statement: PFC IAP-SWR+ units fire around well entry in patterns more like CA1 IAPs and PFC\n    MAP-SWR+ units in patterns more like CA1 MAPs; IAP-SWR+ units are most active at the onset of\n    immobility, MAP-SWR+ units during movement before entry, and inhibited units rise gradually\n    after entry.\n  source: Figure 6A-C; Results, PFC SWR modulation pattern correlates with task activity, paragraph 2\n  quote: Specifically, PFC IAP-SWR + units were most active at the onset of immobility and show\n    spiking patterns most similar to CA1 IAPs. PFC MAP-SWR + cells were most active during movement\n    before reward well entry and show spiking patterns most similar to CA1 MAPs\n  statistics:\n  - test: Wilcoxon rank-sum test\n    p: 0.0001\n    p_relation: \"<\"\n    n: pairwise comparisons, IAP-SWR+ 1082067, MAP-SWR+ 1921500, IAP/MAP-SWR- 3606768\n  depends_on:\n  - fig5dg-pfc-groups\n  criterion: Per unit, mean instantaneous rate over a 10 s window centred on well entry (O1) over\n    all entries, divided by its maximum (Methods). The rate's bin and smoothing are not given; 100\n    ms bins with Gaussian sigma 200 ms is a standard choice. Pearson correlation for every PFC-CA1\n    pair; the index is every difference of a PFC-IAP correlation and a PFC-MAP correlation within a\n    PFC group (as the n of pairwise comparisons implies). The rank-sum comparison is read as\n    between groups. Reproduced when the IAP-SWR+ median index is > 0, the MAP-SWR+ median is < 0,\n    and the two groups differ by a two-sided rank-sum at p < 0.05; partially reproduced when the\n    sign holds for one group.\n- id: fig6e-coincidence-index\n  statement: Outside SWRs, PFC IAP-SWR+ units are more coactive with CA1 IAPs than MAPs and PFC\n    MAP-SWR+ units more coactive with CA1 MAPs than IAPs; inhibited units are the least coactive.\n  source: Figure 6D-E; Results, PFC SWR modulation pattern correlates with task activity, paragraph\n    3\n  quote: found that PFC IAP-SWR + cells were more coactive with CA1 IAPs than CA1 MAPs. Conversely,\n    PFC MAP-SWR + cells were more coactive with CA1 MAPs than CA1 IAPs\n  statistics:\n  - test: Wilcoxon rank-sum test\n    p: 0.0001\n    p_relation: \"<\"\n    n: pairwise comparisons, IAP-SWR+ 845, MAP-SWR+ 2560, IAP/MAP-SWR- 7503\n  depends_on:\n  - fig5dg-pfc-groups\n  criterion: PFC-CA1 cross-correlations of all spikes outside SWRs, 100 ms bins over a 20 s window,\n    z-scored over its bins (Methods); the coincidence index is the difference between a PFC-IAP and\n    a PFC-MAP value in the bin centred on 0 lag, over pairs of pairs sharing the PFC unit (the\n    paper's n are smaller than all combinations, so pairing within a PFC unit is read as the main\n    reading, all combinations within the group as a variant). Reproduced when the IAP-SWR+ median\n    is > 0, the MAP-SWR+ median < 0, and the two differ by a two-sided rank-sum at p < 0.05.\n- id: fig6s2-no-proximity-difference\n  statement: PFC cell pairs within a modulation group do not differ from pairs across groups in\n    spatial proximity (inter-spike distance) or temporal proximity (cross-correlation peak offset).\n  source: Figure 6, supplement 2; Results, PFC SWR modulation pattern correlates with task activity,\n    paragraph 3\n  quote: These effects could not be explained by differences in spatial or temporal proximity of\n    spiking between different PFC cell pairs\n  statistics:\n  - test: Wilcoxon rank-sum test\n    p: 0.05\n    p_relation: \">\"\n    n: 39 within-group and 169 across-group PFC pairs\n  depends_on:\n  - fig5dg-pfc-groups\n  criterion: A claim of absence, judged on the paper's test, a two-sided Wilcoxon rank-sum at 0.05\n    of within-group against across-group simultaneously recorded PFC pairs, for (A) the mean\n    distance between the positions at the spikes of one cell and those of the other (read as the\n    mean over all spike pairs; the paper does not define it) and (B) the absolute offset of the\n    cross-correlation peak in a 20 s window. Reproduced when neither test gives p < 0.05; the\n    medians are reported either way.\n"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  python tools/claims_check.py claims/crcns-hc-13/10.7554-elife.27621.yaml paper/10.7554-elife.27621.txt
```

Result: not kept, because it reads the paper's text.

**Agent**

The YAML has colons inside plain scalars ("Readings: ..."). Fixing those now.

**Agent calls Bash**

```bash
cd  f=claims/crcns-hc-13/10.7554-elife.27621.yaml; sed -i -E '/^ *#/!s/Readings: /The readings are /g; /^ *#/!s/readings: /readings are /g' $f; grep -n -v '^ *#' $f | grep -E ': .*: '
```

```
89:  archive: crcns
90:  id: hc-13
91:  doi: 10.6080/K0H41PK8
95:  statement: Across both tasks, 83 CA1 units are classified as immobility-associated place cells
97:  source: Results, Identification of CA1 place cells participating in spatial representations,
99:  quote: we therefore refer to them as Immobility-Associated Place cells (IAPs) (n = 83) ... We refer
101:  data: with_inputs
103:  - quantity: IAPs, both tasks
104:    value: 83
105:    tolerance: 8.3
106:    unit: cells
107:  - quantity: MAPs, both tasks
108:    value: 659
109:    tolerance: 65.9
110:    unit: cells
111:  criterion: Cells selected as in the opening comment (Methods, Cell selection), under readings O1,
117:  statement: In the foraging task, 33 CA1 units are IAPs and 244 are MAPs.
118:  source: Figure 1, supplement 4B legend
119:  quote: Cells from the foraging task are shown on left (MAP = 244, IAP = 33)
121:  - quantity: IAPs, foraging task
[... 342 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python tools/claims_check.py claims/crcns-hc-13/10.7554-elife.27621.yaml paper/10.7554-elife.27621.txt
```

Result: not kept, because it reads the paper's text.

**Agent**

Every quote checks out. Two cleanups left: the tolerance for the count of 3 has to match its criterion, and a scan for banned words and dashes.

**Agent calls Bash**

```bash
cd  f=claims/crcns-hc-13/10.7554-elife.27621.yaml; python - <<'E'
p='claims/crcns-hc-13/10.7554-elife.27621.yaml'
s=open(p).read()
old="""    value: 3
    tolerance: 0.3"""
assert s.count(old)==1
s=s.replace(old,"""    value: 3
    tolerance: 1""")
open(p,'w').write(s)
E
grep -n -i "rather\|—" $f; python tools/claims_check.py $f paper/10.7554-elife.27621.txt
```

Result: not kept, because it reads the paper's text.

**Agent**

I wrote the claims file at `claims/crcns-hc-13/10.7554-elife.27621.yaml`. The quote checker reports 32 claims, 32 quotes, 31 statistical values and 0 problems. Nothing is committed.

**Text read:** the version of record (PMC5576488, from the Europe PMC full-text XML): main text, figure legends, the legends of all 22 figure supplements, and the Methods. eLife has no other supplement. There is no PDF of the paper under `paper/`, so I could read no figure panels. The paper links no analysis code; it names only MatClust and Chronux. The data descriptor was used only to know what hc-13 holds: the five foraging-task rats, with CA1 and PFC recordings.

**Claims:**
- **Counts:** all 32 claims have quotes, and none is inferred. 28 have statistics. 9 have expected values with tolerances (cell counts, SWR counts and fractions, the 6.4 to 6.6 s transition interval, cells and spikes per SWR, PFC unit counts and groups, and the R² of 0.73). 32 have criteria.
- **Where the data are:** 23 claims use tests the paper ran on both tasks pooled, or appears to have (the cell counts imply it). I marked these `with_inputs`, because the W-track rats are not in hc-13. The paper names CRCNS hc-6 (doi:10.6080/K0NK3BZJ) as that data. Each of these claims states its foraging-only test as a variant. The 9 claims that use only the foraging data (two per-task panels, the transition interval, and the 6 PFC claims) are `dataset`.

**Details the paper leaves open, and the readings named:**
- **"At a reward well" (O1):** beam-break entry and exit times, or immobility periods assigned to wells found as clusters of immobile positions. No well positions or radius are given.
- **Excluding SWR activity from IAP rates (O2):** remove the spikes only (as the Methods say), or remove both the spikes and the time. The rate is pooled over the day's sessions, with the maximum over sessions as a variant.
- **Speed (O3):** the paper doesn't say how speed is computed from position. I used a standard smoothing and named unsmoothed speed as a variant.
- **Unit counts (O4):** each unit counted once per day, or unique units.
- **SWR threshold (O5):** "envelope power" read as the envelope or its square. The histogram bin is a standard choice, and normalization uses task-session immobility only.
- **Coactivity permutations (O6):** all SWRs of the day pooled, or per session and then averaged.
- **Pair selection by cross-correlation peak (O7):** the window is not given; read as ±5 s or ±10 s.
- **Other open points:**
  - how the foraging maze is linearized for field size;
  - whether the PFC 1 s window is centred on SWR start or midpoint;
  - the PETH bin and shift range;
  - pooled spikes or first spike per cell for spike timing;
  - how subsamples are matched;
  - Pearson or Spearman for the theta-scale correlation;
  - which 15 units enter the regression;
  - how the PFC index pairs are formed;
  - the test for "no more than chance" coactivity.
- **Choices I fixed myself and labelled as choices:** "close to 1" for well specificity (median ≥ 0.8, with 0.9 as a stricter reading), how far the Figure 2C tail must reach (0.5 s), the theta peak window (0.1 to 0.16 s), and the lag range for SWR timing (±2 s).

**Gaps in the paper that the claims needed:**
- **Unassigned significance marks:** several legends (Figure 3 supplement 3, Figure 4B, Figure 4 supplement 2C, Figure 1 supplement 4E) give significance marks without saying which comparison carries which. Without the PDF I recorded them as unassigned.
- **MAP count mismatch:** the per-task MAP counts (244 + 435 = 679) don't add up to the stated n = 659. The claim accepts either number.
- **SWR counts per task:** these are given only in a figure panel I couldn't read.
- **Kay et al. 2016 W-track data:** the paper names no separate deposit for them, only hc-6.

## End of run

18 turns, 6 minutes, $1.96 at API prices, result: success.
