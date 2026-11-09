# crcns-pfc-2 · claims · run 42367886320

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  grep -n "^#" docs/protocol.md | head -50; ls claims/001453 claims/crcns-pfc-2 paper/ 2>&1
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  sed -n 1,185p docs/protocol.md
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
[... 165 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat claims/001453/*.yaml | head -200; wc -l paper/*.txt; head -30 paper/10.1038-nn.2134.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  sed -n 200,400p claims/001453/*.yaml; cat tools/claims_check.py | head -80
```

```
relatively constant velocity.
  source: Results, Larval DC exhibit higher average swimming speeds, paragraph 1; Figure 1C and
    Figure S1D
  quote: These visually evoked bouts in ZF consist of sharp velocity increases ... followed by
    interbout glides, resulting in characteristic periodic patterns. While DC also match the optic
    flow direction, they swim continuously, maintaining a relatively constant velocity
  criterion: The paper shows this with representative traces and a bout analysis whose bout
    files are not in the dandiset, so a measure is fixed here. Per trial, positions resampled
    to 30 Hz between 3 and 35 s, instantaneous speed, and the ratio of its median to its mean
    (near 1 for steady swimming, low for bursts); per fish, the median over all trials of all
    stimulus codes. Reproduced when the ZF fish have lower ratios than the DC fish by a
    two-sided Mann-Whitney test at p < 0.05.
- id: fig1cef-representative-values
  statement: In representative trials ZF bouts reach a peak velocity of 44.7 mm/s with a median
    of 1.8 mm/s, DC swim at a median of 13.7 mm/s to forward motion; to oblique motion ZF show
    a median angular velocity of 12.0 degrees/s and median peak angular acceleration of 174
    degrees/s2, and DC an average peak of 103 degrees/s2 to rightward motion.
  source: Results, Larval DC exhibit higher average swimming speeds, paragraph 1, and Results, Optic
    flow induces angular matching and turns in DC, paragraph 1; Figure 1C, 1E and 1F
  quote: sharp velocity increases (peak velocity = 44.7 mm/s, median velocity = 1.8 mm/s) ...
[... 182 more lines not kept]
```

**Agent**

Now read the paper.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1038-nn.2134.txt",
 "limit": 700
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1038-nn.2134.txt",
 "offset": 700,
 "limit": 800
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1038-nn.2134.txt",
 "offset": 1500,
 "limit": 870
}
```

Result: not kept, because it reads the paper's text.

**Agent**

Full text, Methods and supplement are present; the paper links no code. Let me check the data description and how a CRCNS claims file names its dataset.

**Agent calls Bash**

```bash
cd  sed -n 1,120p paper/pfc-2.data-description.txt; ls claims/ | grep crcns; head -40 claims/crcns-hc-11/*.yaml 2>/dev/null; grep -n -A12 '"dataset"' schemas/claims.schema.json | head -60
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  grep -n -B2 -A6 "^dataset:" claims/crcns-hc-11/*.yaml; grep -n '"description"' schemas/claims.schema.json | sed -n 1,60p | cut -c1-220
```

```
93-# outcome is the one all its readings give.
94-schema_version: 2
95:dataset:
96-  archive: crcns
97-  id: hc-11
98-  doi: 10.6080/K0862DC5
99-paper: doi:10.1126/science.aad1935
100-claims:
101-- id: place-cell-count
4:  "description": "Draft. To be revised after the pilot.",
18:      "description": "The dataset the claims are tested on: the archive and the dataset's identifier there.",
27:          "description": "The archive that holds the dataset, in lower case: dandi, ebrains, openneuro, dryad, zenodo, figshare and so on.",
32:          "description": "The dataset's identifier in that archive, e.g. 000003 on DANDI.",
37:          "description": "The dataset's DOI, when it has one: an identifier that holds across archives.",
74:            "description": "Stable within the file, e.g. fig2b.",
79:            "description": "The finding in one or two sentences, in words. Not a copy of the figure.",
84:            "description": "Where the paper shows it, precise enough to find without searching: a figure panel, e.g. 'Figure 2B', or a section and paragraph, e.g. 'Results, Place fields, paragraph 3'.",
88:            "description": "A finding the paper reports (`finding`, the default), or a check the registry adds that the dataset is the data the paper's outside material describes (`link`: the paper's tables, source da
95:            "description": "The sentence of the paper that states the finding, word for word, from the place `source` names, so a reader can check the statement against the paper. Cut with '...' where it runs long. Fr
100:            "description": "For a finding with no quote: why the statement is the author's reading and not a sentence of the paper, e.g. 'Numbers from Supplementary Table 1; no sentence states them.'",
[... 15 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n -i "doi\|10.6080\|cite\|rat \|EE\b" paper/pfc-2.data-description.txt | head -30; sed -n 120,433p paper/pfc-2.data-description.txt | grep -v "^\s*$" | head -150; sed -n 60,140p schemas/claims.schema.json; sed -n 150,200p schemas/claims.schema.json
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  sed -n 230,285p schemas/claims.schema.json; grep -n "doi\|DOI" paper/pfc-2.data-description.txt | tail -5; tail -40 paper/pfc-2.data-description.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  sed -n 330,395p paper/pfc-2.data-description.txt
```

Result: not kept, because it reads the paper's text.

**Agent**

Let me look at Figures 2 and 3 and 7 to read numbers the text garbles.

**Agent calls Bash**

```bash
cd  python -c "
import fitz,os
d=fitz.open('paper/10.1038-nn.2134.pdf')
for p in [2,3,7]:
    d[p].get_pixmap(dpi=130).save(os.environ['TMPDIR']+f'/p{p+1}.png')
"; ls $TMPDIR
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  which pdftoppm mutool; ls .venv 2>/dev/null | head; python -c "import pypdfium2" 2>&1
```

```
Exit code 1
Traceback (most recent call last):
  File "<string>", line 1, in <module>
    import pypdfium2
ModuleNotFoundError: No module named 'pypdfium2'
```

**Agent calls Read**

```json
{
 "file_path": "paper/10.1038-nn.2134.pdf",
 "pages": "3-4"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  grep -rn -i "s\.d\.\|standard deviation\|spread" claims/crcns-*/*.yaml | grep -i toler | head -10
```

```
claims/crcns-bf-1/10.1073-pnas.1712431115.yaml:310:    tolerance (the reported spread, which the paper does not name). If the data set has no day labels, the two arena sessions are
claims/crcns-bf-1/10.1073-pnas.1712431115.yaml:469:    Mann-Whitney test the variant. Tolerances are the reported spread.
claims/crcns-bf-1/10.1073-pnas.1712431115.yaml:677:    within tolerance (10% for the count, the reported spread for the duration), durations fall
claims/crcns-bf-1/10.1073-pnas.1712431115.yaml:703:  - fig3a-bf-gamma-reduction and fig3c-home-cage-above-both-sessions, the tolerance was called the reported SEM; the paper does not label the spread of 35 +/- 3% or 5.62 +/- 1.2%, so it is now called the reported spread.
claims/crcns-ear-1/10.1085-jgp.201912447.yaml:196:  criterion: Tolerances are the spread the paper states. Mean CLW (shared method) over the cells of
claims/crcns-ear-1/10.1085-jgp.201912447.yaml:262:  criterion: Tolerances are the stated standard deviations. alpha(V0.5) per cell by the shared
claims/crcns-ear-1/10.1085-jgp.201912447.yaml:299:  criterion: Tolerances are the stated standard deviations. The pigmented values times four are
claims/crcns-ear-1/10.1085-jgp.201912447.yaml:332:  criterion: Tolerances are the standard deviations Table 1 prints. alphaB = 4 alpha(V0.5) and z =
claims/crcns-ear-1/10.1085-jgp.201912447.yaml:481:  criterion: Tolerances are the stated standard deviations. V0.5 corrected for the pipette drop
claims/crcns-ear-1/10.1085-jgp.201912447.yaml:600:  criterion: Tolerances are the standard deviations Table 2 prints. One-way ANOVA of corrected V0.5
```

**Agent**

The paper links no analysis code (only KlustaKwik for sorting), and the PDF pages cannot be rendered here (no poppler), so figure-only numbers stay unread. Writing the claims file now.

**Agent calls Write**

```json
{
 "file_path": "claims/crcns-pfc-2/10.1038-nn.2134.yaml",
 "content": "# Claims for Fujisawa, Amarasingham, Harrison & Buzsaki (2008), Nature Neuroscience 11:823-833,\n# on CRCNS data set pfc-2 (doi:10.6080/K01V5BWK).\n# Written by an agent (model \"claude-opus-5-5\", Claude Code, runner \"GitHub Actions\"), 2026-11-07,\n# protocol as stated in docs/protocol.md (Reader).\n#\n# Text read: the version of record (PDF supplied by a person, text by PyMuPDF), main text, figure\n# legends and Methods, with its supplement (Supplementary Note, legends of Supplementary Figures\n# 1 to 16, references). The PDF pages could not be rendered in this run, so numbers and\n# significance marks printed only inside figure panels (Figure 2b, 2d, 2e, 3e, 3f, 7b, the\n# supplementary panels) are not recorded; the claims rest on the text and legends. Figure 2d\n# (mean firing rates, t-test marks) and Figure 2e (fraction of maze length discriminated) have\n# no claim for that reason: what the marks compare is shown only in the panels. The paper links\n# no analysis code; the only link is to the KlustaKwik spike sorter. None was read.\n#\n# Data the paper used. Four adult male rats (3 to 5 months old) trained on an odor-based delayed\n# matching-to-sample task on a figure-eight T-maze: a nose-poke in the start box gives a cheese or\n# chocolate odor, which signals the reward in the right or left goal arm (the pairing varied\n# across rats). Mean correct performance in recording sessions 91.9%. One 8-shank, 64-site silicon\n# probe per rat (200 um shank separation, 8 staggered sites per shank) in anterior cingulate (area\n# 24) and dorsal prelimbic (area 32) cortex; three rats in layer 2/3, one in layer 5. Wideband\n# signals at 20 kHz, spikes sorted with KlustaKwik and manual adjustment; two head LEDs tracked at\n# 40 Hz. 633 well isolated units in total. Each trial's path is linearised to a normalised\n# position from 0 (the odor sampling location) to 1 (the reward area), total length 230 cm, and\n# labelled LEFT or RIGHT by the goal arm. Figure 2a and Figure 3 use one layer 2/3 session (117\n# neurons, 1172 pairs) and one layer 5 session (142 neurons). The CRCNS description of pfc-2 lists\n# PFC (64 channels) and CA1 recordings from three rats (EE, FF, GG) during the working memory\n# task, with sleep and a spontaneous alternation task on some days, and states that session\n# EE.188 is the session of Figures 2A and 3D. The paper's counts are over four rats; the author\n# decides how a data set of three rats bears on them.\n#\n# Shared method, from the Methods unless stated.\n# - Firing-rate differences (LEFT against RIGHT, or any two trial labels). Spikes are placed at\n#   the normalised position at which they occur; the PSTH per condition is the sum of Gaussian\n#   kernels (bandwidth 0.05 normalised length) over the condition's spikes, divided by the number\n#   of trials of that condition. Statistic D0(x) = left PSTH minus right PSTH. Labels are permuted\n#   M times; pointwise two-sided bands, and global bands found by the stepping procedure (the\n#   smallest pointwise band whose global acceptance level is alpha). A segment is significant\n#   when the global band is broken; its extent is where the pointwise band is broken (Figure 1c\n#   legend, Supplementary Figure 4E). Level alpha = 0.05 (Figure 1c legend, P < 0.05). M is not\n#   given: a standard choice (1,000, the number the paper uses for jitter) is used, as the number\n#   of permutations should not change the outcome. Whether error trials enter is not said; the\n#   paper reports performance separately and does not mention them in any analysis (open:\n#   readings T-a correct trials only, T-b all trials).\n# - Monosynaptic connections. Every spike of each neuron is jittered uniformly on [-5, +5] ms,\n#   1,000 surrogates. The cross-correlogram over latencies [-5, +5] ms; pointwise and global bands\n#   at the 99% level, the global band from the maximum and minimum of each surrogate. A\n#   connection is excitatory (peak) or inhibitory (trough) when the counts break the global band\n#   anywhere in [1, 4] ms. Pairs are counted in both directions. The Results add onset below 5 ms\n#   and a narrow peak (2 ms or less). The CCG bin width is not given (open: readings B-a 1 ms,\n#   B-b 0.5 ms). Supplementary Figure 9 says spikes of one of the two neurons were jittered; the\n#   Methods jitter each spike of each neuron, which is used, and jittering one neuron is a\n#   variant. How the 2 ms width is measured is not given (open: readings W-a, the [1, 4] ms global\n#   band test alone as the Methods state it; W-b, also requiring the run of bins above the\n#   pointwise 99% band to span 2 ms or less). Figure 3b includes spikes from intertrial\n#   intervals, so a pair's CCG uses the whole task session.\n# - Cell types. A reference cell with a significant short-latency peak is a putative pyramidal\n#   cell, one with a significant trough a putative interneuron (Results; Figure 3a legend). A unit\n#   with both is not covered by the paper (open; readings C-a unclassified, C-b excluded from the\n#   denominators).\n# - Position of excess coincidences. Coincident events are spike pairs with 1 <= tdiff <= 4 ms,\n#   placed at the position where they occur, smoothed with the same 0.05 kernel and divided by\n#   the number of trials; surrogates by jittering on [-5, +5] ms (1,000, as for the CCG, since this\n#   section gives no number); pointwise and global one-sided bands for excess; global level\n#   P < 0.01 (Figure 4 and 5 panels, text \"P < 0.01\").\nschema_version: 2\ndataset:\n  archive: crcns\n  id: pfc-2\n  doi: 10.6080/K01V5BWK\npaper: doi:10.1038/nn.2134\nclaims:\n- id: unit-count\n  statement: A total of 633 well-isolated units were recorded from anterior cingulate and dorsal\n    prelimbic cortex in four rats.\n  source: Results, paragraph 1\n  quote: We recorded a total of 633 well-isolated units from the anterior cingulate area (area 24)\n    and dorsal prelimbic area (area 32) of the medial prefrontal cortex (mPFC)\n  expected:\n    quantity: well-isolated mPFC units, all rats and sessions\n    value: 633\n    tolerance: 63.3\n    unit: units\n  criterion: The number of distinct sorted PFC units over all working memory task recordings.\n    The paper does not say whether a unit recorded on several days counts once per day; units are\n    counted per recording day, as each day is sorted separately.\n- id: task-performance\n  statement: The rats performed the task with a mean of 91.9% correct choices during the recording\n    sessions.\n  source: Methods, Behavioral task\n  quote: In the recording sessions, the mean correct performance was 91.9%.\n  expected:\n    quantity: mean percentage of correct trials over recording sessions\n    value: 91.9\n    tolerance: 9.19\n    unit: percent\n  criterion: Correct trials over all trials, per session, averaged over the working memory\n    sessions. Not testable if the data hold correct trials only.\n- id: fig2c-synchrony-by-layer\n  statement: About 10% of layer 2/3 neurons and 20% of layer 5 neurons fire at least one spike in a\n    given 100 ms window, and this fraction is roughly constant across the maze.\n  source: Results, Medial prefrontal cortical units predict behavioral choice, paragraph 3; Figure\n    2c; Discussion, paragraph 2\n  quote: the fraction of simultaneously active neurons (10% and 20% in 100-ms windows, layers 2/3\n    and 5, respectively; Fig. 2c) were relatively constant in all segments of the maze\n  expected:\n  - quantity: mean percentage of layer 2/3 neurons active in a 100 ms window\n    value: 10\n    tolerance: 1\n    unit: percent\n  - quantity: mean percentage of layer 5 neurons active in a 100 ms window\n    value: 20\n    tolerance: 2\n    unit: percent\n  criterion: Per Figure 2c legend, the percentage of the session's neurons firing at least one\n    spike in consecutive 100 ms windows, averaged over the windows that fall within trials\n    (Figure 2c is plotted against normalised position). Which sessions is open. Readings (a) the\n    two sessions of Figure 2a (layer 2/3, 117 neurons; layer 5, 142 neurons); (b) all sessions of\n    each layer pooled. Reproduced when both values are within tolerance under one reading, and\n    the mean over windows in each tenth of the maze stays within 50% of the overall mean (a\n    standard choice for \"relatively constant\", the paper gives no test).\n- id: fig2-population-uniform\n  statement: Individual neurons fire transiently at specific locations, but the population as a\n    whole fires relatively uniformly over the whole maze.\n  source: Results, Medial prefrontal cortical units predict behavioral choice, paragraph 3; Figure\n    2a and 2b\n  quote: viewed as a population, the firing properties of mPFC neurons were quite homogeneous\n    ... individual neurons fired transiently, but, as a whole, the population of neurons fired\n    relatively uniformly over the entire apparatus\n  criterion: The paper gives no measure or test. Per neuron, the left and right PSTHs as in the\n    shared method; the positions of the neurons' peak rates (as Figure 2a orders them). Reproduced\n    when, in each Figure 2a session, the peak positions cover the maze with no tenth of the maze\n    holding more than twice or less than half its expected share (a chi-square test against\n    uniform at p < 0.05 is reported as a variant), and the population mean rate per tenth stays\n    within 50% of its overall mean. These thresholds are standard choices, not the paper's.\n- id: lifetime-width\n  statement: Most neurons are active over a similar stretch of the maze, 0.27 (62 cm) +/- 0.17 (39\n    cm) of normalised length (mean +/- s.d.), measured between the 50% boundaries of the peak rate.\n  source: Results, Medial prefrontal cortical units predict behavioral choice, paragraph 3;\n    Supplementary Figure 2B\n  quote: most neurons were generically active for similar standardized distances of 0.27 (62 cm)\n    ± 0.17 (39 cm) (mean ± s.d.) in the maze (as determined by the 50% firing boundaries of the\n    peak firing rate\n  expected:\n  - quantity: mean width of firing at 50% of peak, normalised length\n    value: 0.27\n    tolerance: 0.17\n  - quantity: s.d. of width across neurons, normalised length\n    value: 0.17\n    tolerance: 0.017\n  criterion: Width of the PSTH (shared method) between the 50% boundaries of its peak\n    (Supplementary Figure 2B). The tolerance on the mean is the stated s.d.; the s.d. has 10%.\n    Open details and readings. Which PSTH is (a) each neuron's PSTH over all trials; (b) the left\n    and right PSTHs as two entries; (c) the PSTH of the condition with the higher peak. The width\n    is (i) the contiguous run around the peak above 50% or (ii) the total length above 50%.\n    Neurons are all units in the task sessions. Reproduced when both values are within tolerance\n    under one combination.\n- id: trajectory-divergence\n  statement: Left and right running paths overlap in the stem and diverge significantly from\n    position 0.30; head directions diverge from 0.24.\n  source: Results, Medial prefrontal cortical units predict behavioral choice, paragraph 4;\n    Supplementary Figure 3B\n  quote: Left and right lap trajectories in segments 0 to 0.3 of the central arm overlapped; they\n    began to differ significantly at position 0.3 ... Significant separation of left/right\n    trajectories and head directions emerged at position 0.30 and 0.24, respectively (p<0.01)\n  statistics:\n  - test: permutation test with global bands, left and right labels shuffled\n    p: 0.01\n    p_relation: \"<\"\n  expected:\n  - quantity: first position of significant left-right difference in path\n    value: 0.30\n    tolerance: 0.03\n    unit: normalised position\n  - quantity: first position of significant left-right difference in head direction\n    value: 0.24\n    tolerance: 0.024\n    unit: normalised position\n  criterion: The permutation test of the shared method (Supplementary Figure 3B) at global level\n    0.01, applied to position and head direction as functions of normalised position. Open\n    details. The variable for the path is (a) the lateral (x) coordinate or (b) the distance\n    between each trial's position and the mean path; head direction is the angle between the two\n    LEDs. The session is the Figure 2a layer 2/3 session (Supplementary Figure 3A uses it), with\n    all sessions shown as a variant. Reproduced when, under one reading, the first globally\n    significant position is within tolerance for both.\n- id: side-arm-selectivity-by-layer\n  statement: In the side arms (positions 0.5 to 1) the fraction of neurons firing differently on\n    left and right trials is almost twice as large in layer 5 (40%) as in layer 2/3 (22%).\n  source: Results, Medial prefrontal cortical units predict behavioral choice, paragraph 4; Figure\n    2b\n  quote: The fraction of trajectory-selective neurons in the side arms (positions 0.5–1) was\n    almost twice as large in deep (layer 5, 40%) than in superficial (layer 2/3, 22%) neurons\n  expected:\n  - quantity: layer 5 neurons with a significant left-right segment in positions 0.5 to 1\n    value: 40\n    tolerance: 4\n    unit: percent\n  - quantity: layer 2/3 neurons with a significant left-right segment in positions 0.5 to 1\n    value: 22\n    tolerance: 2.2\n    unit: percent\n  criterion: The permutation test of the shared method per neuron, pooled from all rats and\n    sessions of each layer (Figure 2b legend). Open details. A neuron counts when (a) any part of\n    a significant segment lies in 0.5 to 1, or (b) the global band is broken within 0.5 to 1.\n    Reproduced when both values are within tolerance under one reading.\n- id: central-arm-selectivity\n  statement: A smaller fraction of neurons, 16% in layer 2/3 and 18% in layer 5, already fire\n    differently on left and right trials in the central arm (positions 0 to 0.3), where paths and\n    head directions are indistinguishable.\n  source: Results, Medial prefrontal cortical units predict behavioral choice, paragraph 4; Figure\n    2b\n  quote: a sizable but smaller fraction of neurons in both layer 2/3 and layer 5 (16% and 18%,\n    respectively; Fig. 2b) was also differentially active in the central arm (segments 0–0.3)\n  depends_on:\n  - side-arm-selectivity-by-layer\n  expected:\n  - quantity: layer 2/3 neurons with a significant left-right segment in positions 0 to 0.3\n    value: 16\n    tolerance: 1.6\n    unit: percent\n  - quantity: layer 5 neurons with a significant left-right segment in positions 0 to 0.3\n    value: 18\n    tolerance: 1.8\n    unit: percent\n  criterion: As side-arm-selectivity-by-layer, for positions 0 to 0.3, with the same readings.\n    Reproduced when both values are within tolerance under one reading.\n- id: odor-selective-fraction\n  statement: About a quarter of neurons (26% in one layer 2/3 session) fire at significantly\n    different rates during nose-poking for the two odors.\n  source: Results, Medial prefrontal cortical units predict behavioral choice, paragraph 4;\n    Supplementary Figure 6B\n  quote: Approximately one-quarter of the neurons showed significantly different ... firing rates\n    in response to one of the two odorants ... Although 26% of neurons showed significant odor\n    preference (t-test, p<.05)\n  expected:\n    quantity: neurons with different nose-poke firing rates for the two odors\n    value: 26\n    tolerance: 2.6\n    unit: percent\n  criterion: Per neuron, the firing rate during each trial's nose-poke (Supplementary Figure 6,\n    duration of nose-poking from the photoelectric sensor), left (one odor) against right (the\n    other) trials, t-test at p < 0.05 (Supplementary Figure 6B). The session is the Figure 2a\n    layer 2/3 session. Open, the t-test form; readings (a) Student's two-sample, (b) Welch.\n    Reproduced when the fraction is within tolerance under one reading.\n- id: odor-unrelated-to-stem\n  statement: Neurons' odor preference during nose-poking is unrelated to their left-right\n    differences in the stem and side arms, so odor traces do not explain the stem selectivity.\n  source: Results, paragraph continuing on page 4; Supplementary Figure 6B\n  quote: we ruled out this possibility after examining, and finding no reliable relationship\n    among, the differential firing patterns in the stem area and during nose poking\n  depends_on:\n  - odor-selective-fraction\n  - central-arm-selectivity\n  criterion: A claim of absence for which the paper names no test. Readings (a) a Fisher exact\n    test of odor-selective against stem-selective classification over the session's neurons;\n    (b) the correlation across neurons between the nose-poke rate difference and the mean left\n    minus right PSTH in 0 to 0.3, tested at p < 0.05. Reproduced when neither reading finds an\n    association at p < 0.05 with the same sign of preference; the size of each is reported.\n- id: retrospective-coding-rare\n  statement: Only a small fraction of neurons fire differently according to the reward location of\n    the previous trial.\n  source: Results, page 4, paragraph 1; Supplementary Figures 7 and 8\n  quote: found only spare evidence that any neurons fired differentially on the basis of previously\n    visited positions ... Note that only a small fraction of neurons show retrospective coding\n  depends_on:\n  - side-arm-selectivity-by-layer\n  criterion: The permutation test of the shared method with trials labelled by the previous\n    trial's reward side (Supplementary Figure 7, P < 0.05). The sessions are the Figure 2a\n    sessions (Supplementary Figures 7 and 8 are layer 2/3 and layer 5). \"Small\" is not defined;\n    reproduced when, in each layer, the fraction of neurons with a significant segment for\n    previous-trial labels is less than half the fraction for current-trial labels (a standard\n    choice, not the paper's).\n- id: connection-counts\n  statement: Of 62,408 directed cell pairs, 495 (0.79%) show a short-latency narrow peak or trough\n    in the cross-correlogram, 0.55% excitatory and 0.24% inhibitory, and 0.17% of pairs are\n    reciprocally connected.\n  source: Results, Characterization of mPFC neurons and their connections, paragraph 4; Figure 3e\n  quote: Of the 62,408 cell pairs (counting each literal pair twice, corresponding to the two\n    directions), 495 (0.79%) had short latency ... 0.55% excitatory connections and 0.24%\n    inhibitory connections (single directions); 0.17% of cell pairs were connected reciprocally\n  expected:\n  - quantity: directed pairs of simultaneously recorded units\n    value: 62408\n    tolerance: 6240.8\n    unit: pairs\n  - quantity: directed pairs with a significant short-latency peak or trough\n    value: 0.79\n    tolerance: 0.079\n    unit: percent\n  - quantity: excitatory connections\n    value: 0.55\n    tolerance: 0.055\n    unit: percent of directed pairs\n  - quantity: inhibitory connections\n    value: 0.24\n    tolerance: 0.024\n    unit: percent of directed pairs\n  - quantity: reciprocally connected pairs\n    value: 0.17\n    tolerance: 0.017\n    unit: percent of pairs\n  criterion: The jitter method of the shared method over every ordered pair of units recorded in\n    the same session. Runs readings B-a and B-b (bin width) with W-a and W-b (width rule). The\n    denominator of the reciprocal fraction is open; readings (a) directed pairs, (b) unordered\n    pairs. Reproduced when the three directed percentages are within tolerance under one\n    combination and the reciprocal fraction under one of its readings; the pair count is\n    reported against 62,408.\n- id: cell-type-fractions\n  statement: By their cross-correlogram interactions 32.5% of units are putative pyramidal cells\n    and 12.5% putative interneurons; 50.7% of the targets of excitatory cells themselves suppress\n    other neurons; the ratio of pyramidal cells to interneurons is 2.82 +/- 0.51 (s.d.).\n  source: Results, Characterization of mPFC neurons and their connections, paragraph 4\n  quote: a sizable fraction of the recorded units could be classified as putative pyramidal cells\n    (32.5%) or inhibitory interneurons (12.5%). A large percentage of the postsynaptic targets of\n    the putative excitatory cells (50.7%) were suppressing other neurons ... The ratio of putative\n    principal cells to inhibitory interneurons in the entire population, identified by\n    physiological criteria, was 2.82 ± 0.51 (s.d.)\n  depends_on:\n  - connection-counts\n  expected:\n  - quantity: putative pyramidal cells\n    value: 32.5\n    tolerance: 3.25\n    unit: percent of units\n  - quantity: putative interneurons\n    value: 12.5\n    tolerance: 1.25\n    unit: percent of units\n  - quantity: targets of excitatory cells that are putative interneurons\n    value: 50.7\n    tolerance: 5.07\n    unit: percent\n  - quantity: ratio of putative pyramidal cells to interneurons\n    value: 2.82\n    tolerance: 0.51\n  criterion: Cell types as in the shared method from the connections of connection-counts, with\n    readings C-a and C-b. The 50.7% is the fraction of distinct units receiving a significant\n    excitatory peak that themselves have a significant trough as reference. The ratio is a mean\n    over units of analysis the paper does not name; readings (a) per session, (b) per rat. The\n    ratio's tolerance is the stated s.d. Reproduced when all four values are within tolerance\n    under one combination of readings.\n- id: pyr-pyr-connections\n  statement: Monosynaptic excitation between putative pyramidal cells is rare, found in 0.12% of\n    layer 2/3 and 0.27% of layer 5 pairs.\n  source: Results, Characterization of mPFC neurons and their connections, paragraph 4\n  quote: Monosynaptic excitation between putative pyramidal cells was detected in 0.12% of layer\n    2/3 and 0.27% of layer 5 pairs\n  depends_on:\n  - cell-type-fractions\n  expected:\n  - quantity: layer 2/3 pairs with pyramidal to pyramidal excitation\n    value: 0.12\n    tolerance: 0.012\n    unit: percent\n  - quantity: layer 5 pairs with pyramidal to pyramidal excitation\n    value: 0.27\n    tolerance: 0.027\n    unit: percent\n  criterion: Excitatory connections whose target is also a putative pyramidal cell. The\n    denominator is open; readings (a) all directed pairs of the layer, (b) directed pairs of two\n    putative pyramidal cells. Reproduced when both values are within tolerance under one reading.\n- id: fig3b-session-connections\n  statement: In the single layer 2/3 session of Figure 3b (1172 pairs), 48 connections have a\n    putative pyramidal reference cell and 30 a putative interneuron; in the layer 5 session of\n    Supplementary Figure 11 (about 1422 pairs) the numbers are 73 and 25.\n  source: Figure 3b legend; Results, paragraph 5 of the section; Supplementary Figure 11 legend\n  quote: Figure 3b illustrates significant peaks and troughs of crosscorrelograms of 1172 pairs of\n    layer 2/3 cells (13,572 matrix points) simultaneously recorded in a single session\n  depends_on:\n  - connection-counts\n  expected:\n  - quantity: layer 2/3 session, connections with a pyramidal reference cell\n    value: 48\n    tolerance: 4.8\n  - quantity: layer 2/3 session, connections with an interneuron reference cell\n    value: 30\n    tolerance: 3\n  - quantity: layer 5 session, connections with a pyramidal reference cell\n    value: 73\n    tolerance: 7.3\n  - quantity: layer 5 session, connections with an interneuron reference cell\n    value: 25\n    tolerance: 2.5\n  criterion: The jitter method on the Figure 2a sessions (117 and 142 neurons). Whether the\n    counts are significant pixels (directed pairs) or reference cells is open; readings (a)\n    directed connections, (b) distinct reference cells. Reproduced when all four are within\n    tolerance under one combination of readings with B-a or B-b and W-a or W-b.\n- id: fig3d-hub\n  statement: A large part of the recorded neurons belong to a single interconnected circuit, 39 of\n    117 in the layer 2/3 session and 45 of 142 in the layer 5 session.\n  source: Figure 3d; Results, page 6, paragraph 2; Supplementary Figure 11C\n  quote: a large portion of the active neurons (39 of the 117) belonged to a single\n    interconnected circuit ... a large fraction (45 of 142 total) belonged to a single \"hub\" of\n    network\n  depends_on:\n  - fig3b-session-connections\n  expected:\n  - quantity: neurons in the largest connected circuit, layer 2/3 session\n    value: 39\n    tolerance: 3.9\n  - quantity: neurons in the largest connected circuit, layer 5 session\n    value: 45\n    tolerance: 4.5\n  criterion: The largest connected component of the graph of excitatory and inhibitory\n    connections, edges taken as undirected (Figure 3d draws uni- and bidirectional links).\n    Reproduced when both counts are within tolerance under one of the readings of\n    fig3b-session-connections.\n- id: fig3f-distance\n  statement: Most connected pairs are on the same shank and connection probability falls rapidly\n    with the distance between the neurons, yet connections are found up to 1,200 um apart.\n  source: Figure 3f; Results, page 6, paragraph 1\n  quote: most functionally connected pairs were detected locally and recorded by the same probe\n    shank. The probability of putative connections decreased rapidly as a function of distance\n    between the somata of the recorded pair (Fig. 3f), but connections were detected between\n    neurons up to 1,200 mm apart\n  depends_on:\n  - connection-counts\n  criterion: Connection probability (excitatory and inhibitory separately, as Figure 3e and 3f)\n    by shank separation (same shank, 200 to 1,200 um, the Figure 3f axis), with exact\n    Clopper-Pearson 99% intervals (Figure 3 legend). Reproduced when more connected pairs are on\n    the same shank than on all other shanks together, the same-shank probability is above the\n    200 um probability with non-overlapping intervals, and at least one connection is found at\n    1,000 um or more. Distance from estimated soma positions (Figure 3c, ref. 18) is not used, as\n    the estimation method is not given in the paper.\n- id: nearby-pyr-int-probability\n  statement: Connection probability between nearby (under 200 um) putative pyramidal cells and\n    interneurons is 1 to 2%.\n  source: Supplementary Note, Potential caveat with the cross-correlation method, paragraph 3\n  quote: The 1-2% connection probability we detected between the physiologically identified nearby\n    (<200 μm) pyramidal cell-interneuron pairs by the cross-correlation method\n  depends_on:\n  - cell-type-fractions\n  expected:\n    quantity: probability of a connection between a putative pyramidal cell and interneuron on the\n      same shank\n    value: 1.55\n    tolerance: 0.65\n    unit: percent\n  criterion: The range 1 to 2% widened by 10% of each bound (0.9 to 2.2%). \"Nearby (under 200\n    um)\" is read as the same shank. Direction is open; readings (a) pyramidal to interneuron\n    excitatory connections over such directed pairs, (b) a connection in either direction over\n    unordered pairs. Reproduced when the value lies in the range under one reading.\n- id: connected-cells-trajectory-specific\n  statement: Most putative pyramidal cells (72.2% in layer 2/3, 84.7% in layer 5) and many\n    interneurons (58.3% and 83%) fire differently on left and right trajectories.\n  source: Results, pages 6 and 7; Figure 3c; Supplementary Figure 11B\n  quote: In addition to a large fraction of putative pyramidal cells (72.2% and 84.7% in layers 2/3\n    and 5, respectively), many interneurons (58.3% and 83% in layers 2/3 and 5, respectively) ...\n    were also trajectory specific\n  depends_on:\n  - fig3b-session-connections\n  - side-arm-selectivity-by-layer\n  expected:\n  - quantity: trajectory-specific putative pyramidal cells, layer 2/3\n    value: 72.2\n    tolerance: 7.22\n    unit: percent\n  - quantity: trajectory-specific putative pyramidal cells, layer 5\n    value: 84.7\n    tolerance: 8.47\n    unit: percent\n  - quantity: trajectory-specific putative interneurons, layer 2/3\n    value: 58.3\n    tolerance: 5.83\n    unit: percent\n  - quantity: trajectory-specific putative interneurons, layer 5\n    value: 83\n    tolerance: 8.3\n    unit: percent\n  criterion: A cell is trajectory specific when the permutation test of the shared method gives a\n    significant segment anywhere on the maze (Figure 3c colours R, L or R and L). Which cells is\n    open; readings (a) the identified cells of the two Figure 3 sessions, (b) all sessions of each\n    layer. Reproduced when all four values are within tolerance under one reading.\n- id: no-spatial-clustering\n  statement: Left- and right-specific neurons are not clustered on the probe but spread over the\n    whole recorded volume.\n  source: Results, page 7, paragraph 1; Figure 3c; Discussion, paragraph 2\n  quote: left and right trajectory-specific neurons (Fig. 1c and Fig. 2) were not clustered\n    together but occupied a large neuronal volume\n  depends_on:\n  - connected-cells-trajectory-specific\n  criterion: A claim of absence with no test in the paper. Reading, a chi-square test of shank\n    against class (left, right, both, none) in each Figure 3 session, and, as a variant, all\n    sessions. Reproduced when no session shows an association at p < 0.05; the effect size\n    (Cramer's V) is reported.\n- id: position-dependent-transmission\n  statement: Of 343 pairs with significant excitatory monosynaptic connections, 67 show\n    identifiable position dependence of excess short-latency coincidences.\n  source: Results, Behavioral modulation of monosynaptic interactions, paragraph 1; Figure 4b;\n    Supplementary Figure 12\n  quote: Across all sessions, out of 343 pairs with significant excitatory monosynaptic connections\n    in all sessions, 67 pairs showed identifiable position dependence in monosynaptic\n    interactions by this measure\n  depends_on:\n  - connection-counts\n  expected:\n  - quantity: pairs with significant excitatory monosynaptic connections\n    value: 343\n    tolerance: 34.3\n    unit: pairs\n  - quantity: pairs with position-dependent excess coincidences\n    value: 67\n    tolerance: 6.7\n    unit: pairs\n  criterion: Position of excess coincidences as in the shared method, at global P < 0.01. Open\n    details and readings. Trials are (a) left and right analysed separately, a pair counting when\n    either shows dependence, (b) all trials together. Position dependence is (i) a globally\n    significant region anywhere, or (ii) a globally significant region together with a part of\n    the maze where the pointwise band is not broken. The jitter surrogates jitter every spike of\n    both cells (Methods), with jittering the presynaptic cell only (Supplementary Figure 12B) as a\n    variant. Reproduced when both counts, or the fraction 67/343 (19.5%, tolerance 2.0 points),\n    are within tolerance under one combination.\n- id: fig5a-session-selective-connections\n  statement: In the layer 2/3 session of Figure 3d, 15 of 36 excitatory connections are active\n    selectively in maze segments of left or right trajectories.\n  source: Figure 5a legend\n  quote: Putative monosynaptic connections that were active selectively in maze segments during\n    left or right turn trajectories (15 of 36 excitatory connections; same set of neurons, and\n    session, as in Fig. 3d)\n  depends_on:\n  - position-dependent-transmission\n  expected:\n  - quantity: excitatory connections in the session\n    value: 36\n    tolerance: 3.6\n  - quantity: connections with position or trajectory selective excess coincidences\n    value: 15\n    tolerance: 1.5\n  criterion: The method and readings of position-dependent-transmission, on the Figure 3d session\n    (EE.188 by the data set's description). Reproduced when both counts are within tolerance under\n    one combination. The 36 here and the 48 of Figure 3b count different things in the paper;\n    the reading that gives 36 is reported.\n- id: fig4-pair-156-136\n  statement: Pair 156-136, on different shanks, keeps steady firing rates between positions 0.2 and\n    0.5 on left trials, yet excess short-latency coincidences occur only between 0.4 and 0.6.\n  source: Figure 4; Results, Behavioral modulation of monosynaptic interactions, paragraph 2\n  quote: cell pair 156-136, recorded from different electrode shanks, maintained steady firing\n    rates between maze segments 0.2 and 0.5, yet short-latency coincident spikes significantly in\n    excess of firing rate–controlled coincidences (the ‘expected coincidence rate’) occurred only\n    between maze locations 0.4 and 0.6\n  expected:\n  - quantity: start of the significant region\n    value: 0.4\n    tolerance: 0.04\n    unit: normalised position\n  - quantity: end of the significant region\n    value: 0.6\n    tolerance: 0.06\n    unit: normalised position\n  criterion: Cells 156 (presynaptic) and 136 in the session of Figure 3d, left trials (Figure 4a\n    legend), position of excess coincidences as in the shared method at global P < 0.01, extent\n    by the pointwise band. Reproduced when the only significant region starts and ends within\n    tolerance, and each cell's PSTH between 0.2 and 0.5 varies by less than 50% of its maximum (a\n    standard choice for \"steady\"). Cell numbers are the paper's; whether the data set uses the\n    same numbering is the author's to find.\n- id: fig5b-example-pairs\n  statement: In pair 197-201 transmission is significant only between 0.4 and 0.5 of left trials\n    although the expected coincidence rate is as high from 0 to 0.5; pair 49-52 transmits only on\n    left trials; pair 186-201 only toward the end of the right arm although expected\n    coincidences are higher earlier.\n  source: Figure 5b; Results, Behavioral modulation of monosynaptic interactions, paragraph 2\n  quote: in pair 197-201, the expected coincidence rate was equally high between maze locations 0\n    and 0.5 of the left trials, yet significant spike transmission was detected only between maze\n    locations 0.4 and 0.5 (Fig. 5b). In pair 49-52, the expected coincidence rate in the first two\n    segments was equally high on left and on right trajectory trials, yet significant spike\n    transmission was detected only on left trajectory trials. In pair 186-201, significant\n    effects were observed only toward the end of the right arm\n  expected:\n  - quantity: pair 197-201, start of the significant region, left trials\n    value: 0.4\n    tolerance: 0.04\n    unit: normalised position\n  - quantity: pair 197-201, end of the significant region, left trials\n    value: 0.5\n    tolerance: 0.05\n    unit: normalised position\n  criterion: As fig4-pair-156-136, in the same session. Reproduced when 197-201 meets its\n    expected values on left trials, 49-52 has a significant region on left and none on right\n    trials, and 186-201 has its only significant region on right trials beyond position 0.75 (a\n    standard reading of \"toward the end of the right arm\"). Partially reproduced when two of the\n    three pairs hold.\n- id: thinning-preserves-dependence\n  statement: In several pairs, position-dependent transmission remains after spikes are thinned so\n    that both cells fire at a flat rate over the region examined.\n  source: Results, Behavioral modulation of monosynaptic interactions, paragraph 1; Methods,\n    Controlling for power; Supplementary Figure 13\n  quote: Applying this approach, we indeed found that in several cases, the conclusion of\n    position-dependent synaptic efficacy remained unaltered after thinning\n  depends_on:\n  - position-dependent-transmission\n  criterion: Per the Methods, for a pair and a region with enough firing and differential\n    coincidences, spikes are removed one at a time, chosen at random within [-s, +s] around the\n    PSTH maximum (s = 0.05, the kernel bandwidth), until the PSTH minimum is within 10% of the\n    maximum, for both cells; then the position test of the shared method. The region is open\n    (the paper chose it per example); readings (a) positions 0.2 to 0.5 as in Supplementary\n    Figure 13A, (b) for each position-dependent pair, the smallest span holding its significant\n    region and an equal length of non-significant maze next to it. Thinning is random; ten\n    repetitions with fixed seeds. Reproduced when at least two pairs keep, in the majority of\n    repetitions, a globally significant region and a non-significant part of the region under\n    one reading.\n- id: fig6-depression-facilitation\n  statement: Comparing first spikes of trains with later spikes, about equal shares of pairs show\n    depressing (12.7%) and facilitating (10.7%) spike transmission; 32.2% of the significant pairs\n    are on different shanks.\n  source: Figure 6c; Results, page 8, paragraph 1\n  quote: we found that approximately equal percentages of neuron pairs showed firing\n    pattern–dependent depressing (12.7%) and facilitating (10.7%) effects (Fig. 6c) ... Among the\n    significant pairs, 32.2% were recorded by different shanks\n  depends_on:\n  - connection-counts\n  expected:\n  - quantity: pairs with significant depression\n    value: 12.7\n    tolerance: 1.27\n    unit: percent\n  - quantity: pairs with significant facilitation\n    value: 10.7\n    tolerance: 1.07\n    unit: percent\n  - quantity: significant pairs on different shanks\n    value: 32.2\n    tolerance: 3.22\n    unit: percent\n  criterion: Presynaptic spikes labelled first (preceded by at least 200 ms without spikes) or\n    second-and-later (within 40 ms of the previous spike) (Results; Figure 6b legend). For each\n    label, the standardized peak height (h minus the jitter mean, over the jitter s.d.;\n    Supplementary Figure 9B). Difference of the two heights; labels shuffled for a two-sided\n    permutation test at P < 0.10 (Figure 6c legend, Supplementary Figure 16); depression is\n    first above later. Open details and readings. Pairs are (a) the 343 excitatory connections,\n    (b) all 495 connections. The peak height h is (i) the largest bin in [1, 4] ms, (ii) the sum\n    over [1, 4] ms. Whether a later spike must belong to a train begun after 200 ms of silence is\n    open; readings (x) yes, (y) any spike within 40 ms of the previous. Number of permutations a\n    standard 1,000. Reproduced when all three values are within tolerance under one combination.\n- id: fig6b-convergent-examples\n  statement: Two putative pyramidal cells converging on one layer 2/3 interneuron behave\n    oppositely; cell 197 depresses with spike repetition while the first spikes of cell 186 are\n    ineffective and its later spikes drive the interneuron.\n  source: Figure 6b; Results, pages 7 and 8; Supplementary Figure 14\n  quote: Figure 6b shows a putative layer 2/3 interneuron innervated by two pyramidal cells, with\n    ... pyramidal cell 197 showing a depressing effect with spike repetition. In contrast, the\n    first spike of spike trains of cell 186 was ineffective\n  depends_on:\n  - fig6-depression-facilitation\n  criterion: Cells 197 and 186 onto 201 (Supplementary Figure 14) in the Figure 3d session, the\n    measure of fig6-depression-facilitation. Reproduced when 197-201 has a first-spike height\n    above its later-spike height and 186-201 the reverse, each significant at P < 0.10 under one\n    of its readings.\n- id: fig7-supralinear-coincidence\n  statement: Coincident spikes of two or more presynaptic cells within 5 ms discharge their\n    common target interneuron supralinearly, more than the sum of their separate effects, while\n    coincidences in windows over 10 ms add only linearly.\n  source: Figure 7a and 7b; Results, page 8, paragraph 2; Discussion, paragraph 4\n  quote: Coincident discharge of two presynaptic neurons within 5 ms was more effective than the sum\n    of the effects of nonsynchronous spikes (Fig. 7a), and coincidence of three or four spikes\n    resulted in a supralinear effect in various independently tested cell assemblies (Fig. 7b)\n    ... showed only a linear additive effect on the cooperative ability of presynaptic neurons to\n    discharge a postsynaptic partner\n  depends_on:\n  - cell-type-fractions\n  expected:\n    quantity: satellites (putative pyramidal cells converging on one interneuron)\n    value: 14\n    tolerance: 1.4\n  criterion: A satellite is an interneuron with its convergent excitatory presynaptic cells\n    (Figure 7a). For each event, the number of distinct presynaptic cells spiking within the\n    window (2, 5, 10 and 20 ms, Figure 7a), and the spike transmission probability, the fraction\n    of events followed by a target spike. Open details and readings. The target spike window is\n    1 to 4 ms after the last presynaptic spike (the coincidence lag of the Methods). The minimum\n    number of presynaptic cells in a satellite is not given; reading two or more. Supralinear is\n    (a) above k times the one-spike probability, (b) above 1 - (1 - p1)^k, the probability of\n    independent effects. The paper reports no test. Reproduced when, under one reading, the mean\n    over satellites with 5 ms windows (Figure 7b) is above the linear prediction for 2 and for 3\n    coincident spikes in most satellites, and with 20 ms windows it is not above the prediction\n    by more than its s.d. over satellites. The satellite count is reported against 14.\n- id: speed-not-correlated\n  statement: Firing rates show no net positive relationship with running speed; the distribution\n    of rate-speed correlations is symmetric around zero.\n  source: Supplementary Figure 3C\n  quote: The symmetry of these histograms around 0 suggests that, unlike in the hippocampus, this\n    population of neurons does not exhibit a net positive relationship between firing rate and\n    speed.\n  criterion: Per Supplementary Figure 3C, trials divided into 0.5 s bins, mean rate and speed per\n    bin, the correlation coefficient per neuron over bins. A claim of absence with no test named;\n    reading, a two-sided Wilcoxon signed-rank test of the correlations against 0 over all neurons,\n    and within putative pyramidal cells and interneurons. Reproduced when the median correlation\n    over all neurons is not significantly above 0 at p < 0.05; the median and the test are\n    reported for every group. Speed from the LED midpoint, smoothed over the 0.5 s bin.\n- id: population-vector-width\n  statement: Population vector correlations fall off over similar distances throughout the maze,\n    0.18 +/- 0.087 of normalised length in layer 2/3 and 0.27 +/- 0.13 in layer 5.\n  source: Supplementary Figure 2A\n  quote: Neuronal populations were relatively evenly correlated throughout the maze segments with\n    0.18(41cm) ± 0.087(29cm) (L2/3) and 0.27(62cm) ± 0.13(30cm) (L5) in normalized length\n  expected:\n  - quantity: layer 2/3 correlation width\n    value: 0.18\n    tolerance: 0.087\n    unit: normalised length\n  - quantity: layer 5 correlation width\n    value: 0.27\n    tolerance: 0.13\n    unit: normalised length\n  criterion: Population vectors of PSTHs (shared method) at each position, the correlation matrix\n    between positions, as Supplementary Figure 2A. The width is not defined in the paper; reading,\n    for each position, the length around the diagonal over which the correlation stays above half\n    its diagonal value, mean +/- s.d. over positions. Which trials are open; readings (a) left\n    and right PSTHs concatenated in each vector, (b) all trials. The Figure 2a sessions.\n    Tolerances are the stated s.d. Reproduced when both values are within tolerance under one\n    reading.\n"
}
```

```
File created successfully at: claims/crcns-pfc-2/10.1038-nn.2134.yaml (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd  python tools/claims_check.py claims/crcns-pfc-2/10.1038-nn.2134.yaml paper/10.1038-nn.2134.txt
```

Result: not kept, because it reads the paper's text.

**Agent**

The legend precedes the Results sentence in the text; reorder the fragments.

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/crcns-pfc-2/10.1038-nn.2134.yaml",
 "old_string": "  quote: we found that approximately equal percentages of neuron pairs showed firing\n    pattern–dependent depressing (12.7%) and facilitating (10.7%) effects (Fig. 6c) ... Among the\n    significant pairs, 32.2% were recorded by different shanks",
 "new_string": "  quote: Among the significant pairs, 32.2% were recorded by different shanks ... we found that\n    approximately equal percentages of neuron pairs showed firing pattern–dependent depressing\n    (12.7%) and facilitating (10.7%) effects (Fig. 6c)"
}
```

```
The file claims/crcns-pfc-2/10.1038-nn.2134.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd  python tools/claims_check.py claims/crcns-pfc-2/10.1038-nn.2134.yaml paper/10.1038-nn.2134.txt; grep -n " — \|—\|rather" claims/crcns-pfc-2/10.1038-nn.2134.yaml
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  f=claims/crcns-pfc-2/10.1038-nn.2134.yaml
python - "$f" <<'EOF'
import sys
p=sys.argv[1]; s=open(p).read()
reps=[("    one combination. The 36 here and the 48 of Figure 3b count different things in the paper;\n    the reading that gives 36 is reported.",
"    one combination. Figure 3b reports 48 connections with a pyramidal reference cell in the same\n    session; the paper does not say how the 36 relate to them, and the readings that give each are\n    reported."),
("  source: Results, paragraph continuing on page 4; Supplementary Figure 6B",
"  source: Results, Medial prefrontal cortical units predict behavioral choice, paragraph 4 (end,\n    page 4); Supplementary Figure 6B"),
("  source: Results, page 4, paragraph 1; Supplementary Figures 7 and 8",
"  source: Results, Medial prefrontal cortical units predict behavioral choice, paragraph 4 (end,\n    page 4); Supplementary Figures 7 and 8")]
for a,b in reps:
    assert a in s, a[:40]; s=s.replace(a,b)
open(p,'w').write(s)
EOF
python tools/claims_check.py $f paper/10.1038-nn.2134.txt
```

Result: not kept, because it reads the paper's text.

**Agent**

I wrote the claims file `claims/crcns-pfc-2/10.1038-nn.2134.yaml`, and the quote checker passes it with no problems. The file has 30 claims. All 30 have quotes, 30 have criteria, and 1 has a statistics entry: the permutation test, p < 0.01, for where left and right running paths separate.

**Text read:** the version of record (main text, Methods, figure legends) and the supplement (Supplementary Note and the legends of Supplementary Figures 1 to 16). Nothing the results rest on is missing. The paper links no analysis code; its only link is to the KlustaKwik spike sorter. The data description was read only to see what the data set holds: three of the paper's four rats (EE, FF, GG), with session EE.188 named as the one used for Figures 2A and 3D.

**What the claims cover:**
- Counts: unit count, task performance.
- Population activity: firing synchrony and how widely each neuron fires along the maze, by layer.
- Behaviour: where running path and head direction differ between left and right trials.
- Left/right selectivity: in the side arms and central arm, odor selectivity and its independence from stem selectivity, coding of the previous trial's reward side.
- Connections: counts, cell-type fractions, pyramidal-to-pyramidal connections, the Figure 3b and 3d session counts, connection probability against distance, the 1 to 2% rate for nearby pyramidal-interneuron pairs, and the left/right selectivity of connected cells.
- No spatial clustering of left- and right-specific cells.
- Position-dependent transmission: 67 of 343 pairs, 15 of 36 in one session, the example pairs of Figures 4 and 5, and the thinning control.
- Figure 6 depression and facilitation (12.7%, 10.7%) and its examples.
- Figure 7 supralinear effect of coincident inputs.
- No correlation with running speed; population vector correlation widths.

**Details the paper leaves open, with the readings named:**
- **Cross-correlogram bin width:** 1 ms or 0.5 ms.
- **Narrow-peak rule (2 ms or less):** the global-band test alone, or also requiring the run of bins above the pointwise band to span 2 ms or less.
- **Which spikes are jittered:** the Methods jitter every spike of both neurons; jittering one neuron (as Supplementary Figures 9 and 12 say) is a variant.
- **Units with both a peak and a trough:** left unclassified, or excluded.
- **Error trials:** correct trials only, or all trials.
- **Number of label permutations:** not given; the 1,000 used for jitter is taken as the standard choice.
- **Sessions:** the two example sessions, or all sessions by layer. This applies to synchrony, connected-cell selectivity and population vectors.
- **Firing width:** which PSTH (all trials, left and right separately, or the condition with the higher peak), and whether the width is the run around the peak or the total length above 50%.
- **Path variable for left/right separation:** lateral coordinate, or distance from the mean path.
- **Side-arm counting:** a significant segment overlapping positions 0.5 to 1, or the global band broken within that range.
- **Odor test:** Student's or Welch t-test.
- **Denominators:** for reciprocal pairs, for pyramidal-to-pyramidal connections (all pairs or pyramidal pairs), for depression and facilitation (343 or 495 pairs), and for the pyramidal/interneuron ratio (per session or per rat).
- **Position dependence:** left and right trials separately or pooled, and any significant region or a significant region plus a non-significant one.
- **Depression/facilitation measure:** peak height as the largest bin or the sum over 1 to 4 ms, and whether later spikes must belong to a train that began after 200 ms of silence.
- **Supralinear effect:** above k times the single-spike probability, or above 1 − (1 − p1)^k.
- **Thinning region:** positions 0.2 to 0.5, or a region chosen per pair.

**Criteria with no basis in the paper:** where the paper gives no test or definition, I fixed a test or threshold myself and marked it as a standard choice, not the paper's. This covers "relatively constant", population uniformity, "small fraction" for previous-trial coding, odor/stem independence, no clustering on the probe, no speed correlation, "steady" rates, and "toward the end of the right arm".

**Missing from what was supplied:** the PDF pages could not be rendered here, so numbers and significance marks shown only inside figure panels were not read (Figures 2b, 2d, 2e, 3e, 3f, 7b and the supplementary panels). Figures 2d (firing rates, t-test marks) and 2e have no claim for that reason. The paper's counts cover four rats, while the data set holds three.

## End of run

22 turns, 5 minutes, $1.90 at API prices, result: success.
