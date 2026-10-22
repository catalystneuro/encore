# 001357 · claims · run 39674958376

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cat docs/protocol.md; ls claims/001453/ paper/ claims/001357 2>&1; ls tools
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cat claims/001453/*.yaml | head -200; wc -l paper/*.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1523-jneurosci.1893-23.2024.txt"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1523-jneurosci.1893-23.2024.txt",
 "offset": 1131,
 "limit": 860
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
grep -n -i -E "github|code avail|data avail|dandi|osf|zenodo|supplement|extended data" paper/*.txt | head; sed -n 200,400p claims/001453/*.yaml; ls claims | head -50; git log -3 --stat | head -30
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -n 1,80p claims/001361/*.yaml; cat tools/claims_check.py | head -80
```

```
# Claims for Sosa, Plitt & Giocomo (2025), "A flexible hippocampal population code for experience
# relative to reward", Nature Neuroscience 28, 1497-1509, on dandiset 001361.
# Written by an agent (model "claude-opus-5-5", Claude Code in GitHub Actions), 2026-10-21, protocol
# pilot-10 as stated in docs/protocol.md.
#
# Text read: the version of record, open access, as served by Europe PMC (PMC12229899), with the
# main text, figure legends, Extended Data Figs. 1-10 legends and Methods, and the one supplement
# file in the PMC deposit, the Nature Portfolio Reporting Summary (41593_2025_1985_MOESM1_ESM.pdf).
# The Source Data files are not part of the text read. The paper names a bioRxiv preprint (4 Feb
# 2024, "Hippocampal sequences span experience relative to rewards"), which was not read.
#
# Code read: github.com/GiocomoLab/Sosa_et_al_2024 at commit adf0f9ed3defa22275d92fa0ed996f47008e05b3
# (11 Jun 2025). It holds the package src/reward_relative (dayData.py for session and cell
# classes, spatial.py for place cells and remapping categories, behavior.py for licking, decode.py
# for the circular regression decoder, glmUtils.py for the GLM design, kMeansDistScore.py and
# regression.py for the distance score and sigmoid, multiDayROIAlign.py for cross-day matching,
# plotUtils.py for the mixed models) and one notebook per figure (Fig1_Ext1 to Fig8_Ext10_DistanceScore,
# Ext3_FieldQuant, Ext7_Anatomical_Map), with jupytext .md copies cited below as "notebook.md:line".
# The spatial information, its shuffle and the ROI matching run in the external package TwoPUtils
# (M. Plitt), which the repository does not hold; for these the Methods alone fix the method.
[... 140 more lines not kept]
```

**Agent calls Bash**

```bash
curl -s https://api.dandiarchive.org/api/dandisets/001357/ | python -c "import json,sys;d=json.load(sys.stdin);print(json.dumps(d,indent=1)[:3000])"; curl -s "https://api.dandiarchive.org/api/dandisets/001357/versions/draft/info/" | python -c "import json,sys;d=json.load(sys.stdin)['metadata'];print(d.get('name'));print(d.get('description'));print(d.get('relatedResource'));print(d.get('assetsSummary'))"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cat schemas/claims.schema.json | head -200; git ls-remote https://github.com/mazerj/pype3 HEAD
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
[... 181 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 200,400p schemas/claims.schema.json; grep -l -i "simulation" claims/*/*.yaml | head -3
```

```
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
          "date": {
            "type": "string",
            "format": "date"
          },
          "kind": {
            "enum": [
[... 130 more lines not kept]
```

**Agent calls Bash**

```bash
grep -n -i -B3 -A12 "simulat" claims/000009/*.yaml | head -60
```

```
646-    value: 1.8
647-    tolerance: 0.7
648-    unit: ms
649:  criterion: A simulation, not a test on recorded data; its parameters are in the Supplementary
650-    information, which is not in the text read. Cannot be specified from the text; recorded so the
651-    finding is covered.
652-- id: fig5-weak-photoinhibition-rates
653-  statement: Weak thalamus photoinhibition (20-fold weaker, 0.5 mW) significantly changed the spike rate
654-    of 83 of 160 ALM neurons, with a mean reduction of 1.2 spikes per s; 39% of the changed neurons
655-    (32/83) increased their rate.
656-  source: Results, Thalamus contributes to selectivity in ALM, paragraph 1; Figure 5b
657-  quote: 83 /160 of ALM neurons showed statistically significant changes in mean spike rate during
658-    photoinhibition ( t -test; average reduction of spike rate, 1.2 ± 0.2 spikes per s, mean ± SEM, n =
659-    160; Fig. 5a, b ). A substantial fraction of these neurons (39%, 32/83) showed increases in spike
660-    rate
661-  depends_on:
```

**Agent**

The full text (version of record) is here and there is no supplement. The paper links no analysis code; the only link is the stimulus software pype3. Writing the claims file now.

**Agent calls Bash**

```bash
grep -n -E "density|shared noise|consistent between the two animals" paper/*.txt | head; grep -c "" paper/*.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Write**

```json
{
 "file_path": "claims/001357/10.1523-jneurosci.1893-23.2024.yaml",
 "content": "# Claims for Namima, Kempkes, Zamarashkina, Owen & Pasupathy (2025), \"High-Density Recording\n# Reveals Sparse Clusters (But Not Columns) for Shape and Texture Encoding in Macaque V4\",\n# J Neurosci 45(5) e1893232024, on dandiset 001357.\n# Written by an agent (model \"claude-opus-5-5\", Claude Code in GitHub Actions), 2026-10-21, protocol\n# pilot-10 as stated in docs/protocol.md.\n#\n# Text read: the version of record (PDF supplied by a person, text extracted with PyMuPDF), with\n# the main text, Materials and Methods, and figure legends. The paper has no supplement. The PDF\n# was not opened; the text was enough.\n#\n# Code: the paper links no analysis code and gives no code or data availability statement. The\n# only link it gives is the stimulus software, pype (reference Mazer 2013,\n# github.com/mazerj/pype3, HEAD at 49056d6f7e02bb217b2f044dba6ec7a33173b4ca on 2026-10-21). It\n# runs the stimuli and the fixation task and holds none of the analyses, so it settles no method\n# detail here. The analyses were written in MATLAB (fit.m, confint.m, conv2.m, the cortex-lab\n# Spikes toolbox) by the authors and are not public. The noise-corrected correlation follows\n# Pospisil and Bair (2021, J Neurosci 41 5638), which the paper cites and does not link; its method\n# is taken from this paper's Methods alone.\n#\n# Data the paper used: two rhesus macaques, M1 (female, 6.0 kg, Neuropixels 1.0) and M2 (male,\n# 9.2 kg, Neuropixels NP1010), dorsal V4 of the right hemisphere, one acute penetration per day.\n# Passive fixation; 4 to 8 stimuli per trial, each 200 ms with 200 ms gaps. Spikes sorted with\n# Kilosort 2.0 or 2.5 and curated in phy; only units labelled \"good\" are analysed. Experiments:\n# (1) main shape test, 15 shapes x 8 rotations = 120 shapes, each dark (4 cd/m2) or bright\n# (12 cd/m2) cyan on an 8 cd/m2 background, 30 sessions in M1 and 44 in M2, median 5 repeats\n# (minimum 3); (2) texture test, 40 grayscale textures, original and contrast-reversed, at one of 8\n# random rotations per presentation, 17 sessions in M1 and 34 in M2, median 8 repeats (minimum 4);\n# in M1 shape and texture tests were run in different sessions, in M2 both in 34 sessions;\n# (3) position control, 15 shapes at one rotation each, dark only, at the aggregate RF center and\n# 1/2 RF diameter north, south, east and west, 33 of the 44 M2 sessions; (4) RF localization on a\n# 31x31 or 41x41 grid, 80 or 100 ms presentations, every session; blank presentations give the\n# baseline. Measured variables: spike times of good units, each unit's axial position on the probe\n# (center of mass of the waveform template across channels), stimulus identity, contrast,\n# rotation, position and onset (photodiode), and, for the CSD claims only, the LF signal (2.5 kHz).\n# Penetrations are named M1pN and M2pN in the paper (M2p6, M1p12, M2p9, M2p28, M2p51, M1p5); the\n# paper does not say how N is assigned. The dandiset's description names the shape and texture\n# sets and also a third texture version (spectrally matched noise) that the paper does not use.\n#\n# Outside data. The shapes are the set of Pasupathy and Connor (2001, J Neurophysiol 86 2505); the\n# Gabor fits and the angular position x curvature (APC) fits need the shapes' images and boundary\n# curvature descriptions, which this paper neither prints nor deposits. Those claims are\n# data with_inputs, the input being the Pasupathy and Connor (2001) shape set and its APC\n# descriptions, wherever the author finds them public and pinned. All other claims use the\n# recordings (data dataset).\n#\n# Shared method, from the Methods (cited per section), used by every claim below unless the claim\n# says otherwise.\n# - Firing rate (Methods, Data analysis, Firing rate computation): spike count 30 to 200 ms after\n#   stimulus onset, averaged over repeats; baseline the same window on blank presentations.\n# - Responsive neurons (Methods, Dataset and data inclusion criteria): good units with a mean\n#   response at least 5 spikes/s above baseline to at least one shape (for shape analyses) or one\n#   texture (for texture analyses) at either contrast. All good units, responsive or not, set the\n#   most superficial neuron of the penetration (depth zero).\n# - Depth and distance (Methods, Depth from the most superficial neuron): depth is the axial\n#   position on the probe of the template center of mass relative to the most superficial good\n#   unit; inter-neuron distance is the absolute difference of depths in micrometers.\n# - Tuning similarity (Methods, Tuning similarity and contrast invariance): for two neurons, the\n#   noise-corrected correlation of Pospisil and Bair (2021) between their responses across the\n#   stimuli of one contrast: square-root transformed spike counts per repeat, bias terms\n#   subtracted from the numerator and denominator of r squared, the square root of the quotient,\n#   given the sign of Pearson's r of the mean responses and truncated to [-1, 1]. Tuning\n#   invariance is the same measure between one neuron's responses to the dark and to the bright\n#   version of each stimulus (original and contrast-reversed for textures). A value is unreliable,\n#   and left out, when its bootstrap confidence limit (500 resamples of repeats with replacement)\n#   is above 0.5. OPEN, and able to change outcomes: (i) \"the confidence limit was >0.5\" can be\n#   read as (a) the width of the bootstrap interval (upper minus lower bound) above 0.5 or (b) its\n#   half-width above 0.5; (ii) the interval's level is not given; the reading is 95%, the level\n#   the paper uses for its regressions. Each claim that rests on reliability is run under (a) and\n#   (b).\n# - Isimilarity and Ssimilarity (Methods, Clusters of similarly tuned neurons): for each neuron and\n#   each contrast separately, an ordinary least-squares line of its reliable tuning similarities\n#   with every other responsive neuron of the penetration against inter-neuron distance;\n#   Isimilarity is the intercept, Ssimilarity the slope, each significant when its 95% confidence\n#   interval (t based, as MATLAB confint gives it) excludes zero. Neurons with two or fewer\n#   reliable similarities at a contrast have no line at that contrast. The neuron's similarity with\n#   itself is not a data point (\"a neuron and all other neurons\"). OPEN, and able to change the\n#   counts: the population results give one Isimilarity per neuron (n = 1,848 of 1,850 neurons)\n#   without saying which contrast; Figure 3C uses dark shapes. The readings are (a) dark,\n#   (b) bright, (c) significant at either contrast. Claims that count neurons with significant\n#   Isimilarity are run under each.\nschema_version: 2\ndataset:\n  archive: dandi\n  id: \"001357\"\npaper: doi:10.1523/jneurosci.1893-23.2024\nclaims:\n- id: methods-sessions-and-neurons\n  statement: The shape test was run in 30 sessions in M1 and 44 in M2, the texture test in 17 and\n    34, and the position control in 33 M2 sessions; the responsiveness criterion excluded 461 and\n    366 neurons and left 1,850 neurons for shape and 979 for texture analyses.\n  source: Materials and Methods, Dataset and data inclusion criteria, paragraphs 1 and 2\n  quote: We conducted 30 and 44 sessions of the main shape test in M1 and M2, respectively. The\n    position control experiment with shape stimuli was conducted in 33 of 44 sessions in M2 only.\n    The texture test was conducted in 17 and 34 sessions in M1 and M2, respectively ... This\n    excluded 461 and 366 neurons across our dataset for shape and texture analyses and left 1,850\n    and 979 neurons, respectively\n  expected:\n  - quantity: shape sessions, M1\n    value: 30\n    tolerance: 3\n  - quantity: shape sessions, M2\n    value: 44\n    tolerance: 4.4\n  - quantity: texture sessions, M1\n    value: 17\n    tolerance: 1.7\n  - quantity: texture sessions, M2\n    value: 34\n    tolerance: 3.4\n  - quantity: position control sessions, M2\n    value: 33\n    tolerance: 3.3\n  - quantity: responsive neurons, shape\n    value: 1850\n    tolerance: 185\n  - quantity: responsive neurons, texture\n    value: 979\n    tolerance: 97.9\n  - quantity: excluded neurons, shape\n    value: 461\n    tolerance: 46.1\n  - quantity: excluded neurons, texture\n    value: 366\n    tolerance: 36.6\n  criterion: Sessions counted per monkey and test. Responsive neurons are good units passing the\n    5 spikes/s criterion of the opening comment, counted once per session and test; excluded\n    neurons are good units of those sessions that fail it. Reproduced when every value is within\n    tolerance; partially reproduced when the session counts are and a neuron count is not.\n- id: ex-m2p6-cluster\n  statement: In penetration M2p6, 24 well-isolated neurons were recorded over about 2,400 um; a\n    group of superficial neurons (1 to 9, over 540 um) had similar shape tuning at both\n    contrasts, and with dark shapes neurons 1 to 9, 14 and 17 had a significant positive\n    Isimilarity with a negative slope, while most other, deeper neurons did not.\n  source: Results, Example penetration, paragraphs 1 and 2; Figures 2A, 3A and 3C\n  quote: We recorded 24 well-isolated neurons in this session (Fig. 2A, left, #1-#24; superficial to\n    deep) over a ∼2,400 μm length of the probe ... a small group of neurons (#1-#9) spread over a\n    540 μm extent of the probe in the superficial cortex (Fig. 2A, left) exhibited high similarity in\n    their responses to the tested shapes ... For some neurons (Neurons #1-9, #14, and #17),\n    regression lines were characterized by a large positive y-intercept (Isimilarity) significantly\n    different from zero (p < 0.05, solid lines) and a negative slope (Ssimilarity)\n  statistics:\n  - about: Isimilarity of neurons 1 to 9, 14 and 17, dark shapes\n    test: 95% confidence interval of the regression intercept\n    p: 0.05\n    p_relation: \"<\"\n    n: 24 neurons\n  expected:\n  - quantity: responsive neurons in M2p6\n    value: 24\n    tolerance: 2.4\n  - quantity: probe length spanned by M2p6 neurons\n    value: 2400\n    tolerance: 240\n    unit: um\n  - quantity: neurons with significant positive Isimilarity, dark shapes\n    value: 11\n    tolerance: 1.1\n  criterion: M2p6 is not identified in the paper beyond its name; the readings are (a) the sixth\n    M2 session in recording order among shape sessions, (b) the sixth M2 session in recording\n    order among all sessions, (c) the M2 session the dataset itself labels p6 or penetration 6,\n    each accepted only when its responsive-neuron count is within tolerance of 24. Neurons are\n    numbered by depth. Isimilarity with dark shapes as in the opening comment. Reproduced when the\n    expected values hold and at least 7 of neurons 1 to 9 have a significant positive intercept;\n    partially reproduced when the session is found and fewer hold.\n- id: ex-m2p6-pairs\n  statement: In M2p6, neurons 3 and 8, 260 um apart, have tuning similarity 0.82 at both contrasts,\n    while neurons 18 and 19, 80 um apart, have similarity 0.00 (dark) and -0.25 (bright), though\n    both pairs respond over a broad range.\n  source: Results, Example penetration, paragraph 2; Figure 3B\n  quote: For example, Neurons #3 and #8, recorded on contacts 260 μm apart, share a great deal of\n    similarity in tuning (rsimilarity = 0.82), but Neurons #18 and #19 recorded on contacts 80 μm\n    apart do not (rsimilarity= 0; Fig. 3B)\n  depends_on:\n  - ex-m2p6-cluster\n  expected:\n  - quantity: similarity of neurons 3 and 8, dark\n    value: 0.82\n    tolerance: 0.082\n  - quantity: similarity of neurons 3 and 8, bright\n    value: 0.82\n    tolerance: 0.082\n  - quantity: similarity of neurons 18 and 19, dark\n    value: 0.0\n    tolerance: 0.1\n  - quantity: similarity of neurons 18 and 19, bright\n    value: -0.25\n    tolerance: 0.025\n  - quantity: distance between neurons 3 and 8\n    value: 260\n    tolerance: 26\n    unit: um\n  - quantity: distance between neurons 18 and 19\n    value: 80\n    tolerance: 8\n    unit: um\n  criterion: Noise-corrected similarity as in the opening comment. The paper gives the distances\n    between the contacts nearest each neuron's center of mass (Figure 2A legend); the template\n    center-of-mass distance is shown as a variant. The tolerance of the zero value is 0.1, since\n    10% of zero is no tolerance; 0.1 is 5% of the measure's range of 2. Reproduced when every\n    value is within tolerance; partially reproduced when the 3 and 8 values are and an 18 and 19\n    value is not, or the reverse.\n- id: ex-m2p6-invariance\n  statement: In M2p6, shape tuning was contrast-invariant (invariance above 0.5) for 19 of the 24\n    neurons, whatever their Isimilarity.\n  source: Results, Example penetration, paragraph 3; Figure 3D\n  quote: For a majority of neurons recorded on this day (19/24 neurons), contrast invariance of\n    shape tuning was high (>0.5) regardless of the value of Isimilarity\n  depends_on:\n  - ex-m2p6-cluster\n  expected:\n    quantity: M2p6 neurons with shape tuning invariance above 0.5\n    value: 19\n    tolerance: 1.9\n  criterion: Tuning invariance as in the opening comment, over the 120 shapes. Unreliable values\n    count as not above 0.5. Reproduced when the count is within tolerance under reliability\n    reading (a) or (b).\n- id: ex-csd-sinks\n  statement: The CSD shows a current sink taken as layer 4 at about 1,073 um below the most\n    superficial neuron, 53 ms after stimulus onset, in M2p6, and at 570 um, 52 ms, in M1p12, with\n    no other sink deeper in M1p12.\n  source: Results, Example penetration, paragraph 1, and paragraph 4; Figures 2B and 4G\n  quote: Current source density analysis (CSD, see Materials and Methods) reveals a current sink at\n    ∼53 ms after stimulus onset at a recording depth of ∼1,073 μm relative to the most\n    superficially recorded neuron in this session ... We found that a current sink with short\n    latency (∼52 ms) emerged at a shallow depth along the penetration (570 of 2,580 μm, Fig. 4G),\n    but no other sinks were evident deeper in the cortex\n  depends_on:\n  - ex-m2p6-cluster\n  - ex-m1p12-no-cluster\n  expected:\n  - quantity: M2p6 sink depth\n    value: 1073\n    tolerance: 107.3\n    unit: um\n  - quantity: M2p6 sink latency\n    value: 53\n    tolerance: 5.3\n    unit: ms\n  - quantity: M1p12 sink depth\n    value: 570\n    tolerance: 57\n    unit: um\n  - quantity: M1p12 sink latency\n    value: 52\n    tolerance: 5.2\n    unit: ms\n  criterion: CSD as in Materials and Methods, Current source and sink profile along the probe. LF\n    downsampled to 1 kHz, mean subtracted, scaled to volts, third-order Butterworth band-pass 0.5\n    to 100 Hz; the LF after the first stimulus of each trial averaged over trials, Gaussian\n    smoothed over 10 adjacent contacts, second spatial derivative over three neighboring\n    contacts, Gaussian smoothed over 10 contacts again, sign inverted, per column of contacts.\n    OPEN: the Gaussian's width, the column shown, and how the sink is located are not given; the\n    readings are (a) the earliest sink peak after stimulus onset and (b) the largest sink in 0 to\n    100 ms, each on every column, reproduced when one column under one reading gives all values\n    within tolerance. Depth is relative to the most superficial good unit. Needs the LF signal.\n- id: ex-m1p12-no-cluster\n  statement: In penetration M1p12, 42 neurons over 2,580 um showed no clustered shape tuning at\n    either contrast; only one neuron had a significant Isimilarity, although most had high\n    contrast invariance of shape tuning.\n  source: Results, Example penetration, paragraph 4; Figures 4A, 4B, 4D and 4F\n  quote: Here, we studied the responses of 42 neurons over a 2,580 μm distance (Fig. 4A) ... The\n    y-intercept for the regression line was significantly different from zero for only one neuron\n    (solid line) ... Neurons in this penetration did not exhibit shape tuning that was similar to\n    their neighbors (filled), but most neurons did exhibit high shape tuning invariance\n  expected:\n  - quantity: responsive neurons in M1p12\n    value: 42\n    tolerance: 4.2\n  - quantity: probe length spanned by M1p12 neurons\n    value: 2580\n    tolerance: 258\n    unit: um\n  - quantity: M1p12 neurons with significant Isimilarity, dark shapes\n    value: 1\n    tolerance: 0\n  criterion: M1p12 is found as M2p6 is in ex-m2p6-cluster (readings a to c, accepted when the\n    count is within tolerance of 42). Isimilarity with dark shapes, as Figure 4D is said to\n    follow Figure 3C. The count of 1 is small, so it takes no relative tolerance; reproduced when\n    at most 2 neurons have a significant intercept and more than half of the neurons have\n    reliable tuning invariance above 0.5 (the threshold the paper uses for \"high\" in the M2p6\n    example); partially reproduced when the count holds and the invariance part does not.\n- id: ex-m1p12-strong-responses\n  statement: In M1p12, peak responses exceeded 15 spikes/s in 28 neurons for dark and 26 for bright\n    shapes, so the lack of clustering was not due to weak responses.\n  source: Results, Example penetration, paragraph 4; Figure 4C\n  quote: peak responses were often high (exceeding 15 spikes/s in 28/26 neurons for dark/bright\n    stimuli)\n  depends_on:\n  - ex-m1p12-no-cluster\n  expected:\n  - quantity: M1p12 neurons with peak dark response above 15 spikes/s\n    value: 28\n    tolerance: 2.8\n  - quantity: M1p12 neurons with peak bright response above 15 spikes/s\n    value: 26\n    tolerance: 2.6\n  criterion: Peak response is the largest mean rate over the 120 shapes of one contrast, 30 to 200\n    ms. OPEN whether baseline is subtracted; Figure 4C plots baseline-subtracted rates. The\n    readings are (a) baseline-subtracted and (b) raw. Reproduced when both values are within\n    tolerance under one reading.\n- id: pop-significant-isimilarity\n  statement: Of 1,850 neurons in 74 sessions (6 to 76 per penetration), a minority, 344 (203 in M1,\n    141 in M2), had a significantly positive Isimilarity with a negative Ssimilarity, reflecting\n    similarity with nearby neurons that declined with distance; the majority (1,504) had an\n    Isimilarity not significantly above zero.\n  source: Results, Population results, shape tuning, paragraph 1; Figure 5A\n  quote: We studied the responses of 1,850 neurons across 74 recording sessions (M1, 30; M2, 44),\n    ranging from 6 to 76 neurons per penetration ... we found a minority of neurons (344/1,850; M1,\n    203; M2, 141; Fig. 5A, blue) with positive Isimilarity, significantly different from zero (p <\n    0.05), and a negative Ssimilarity ... The majority (n = 1,504) had Isimilarity that was not\n    significantly greater than zero\n  statistics:\n  - test: 95% confidence interval of the regression intercept\n    p: 0.05\n    p_relation: \"<\"\n    n: 1,850 neurons, 74 penetrations\n  depends_on:\n  - methods-sessions-and-neurons\n  expected:\n  - quantity: neurons with significant positive Isimilarity\n    value: 344\n    tolerance: 34.4\n  - quantity: of which in M1\n    value: 203\n    tolerance: 20.3\n  - quantity: of which in M2\n    value: 141\n    tolerance: 14.1\n  - quantity: neurons with Isimilarity not significantly above zero\n    value: 1504\n    tolerance: 150.4\n  - quantity: fewest responsive neurons in a penetration\n    value: 6\n    tolerance: 0.6\n  - quantity: most responsive neurons in a penetration\n    value: 76\n    tolerance: 7.6\n  criterion: Isimilarity as in the opening comment, under contrast readings (a) dark, (b) bright,\n    (c) either, crossed with reliability readings (a) and (b). OPEN whether the 344 also require\n    a negative slope; 344 + 1,504 = 1,848, the neurons with a line, suggests the count is of\n    significant positive intercepts alone, the slope being described. The readings are (i)\n    significant positive intercept and (ii) significant positive intercept with negative slope.\n    Reproduced when one reading puts the four counts within tolerance.\n- id: pop-intercept-slope-correlation\n  statement: Across neurons Isimilarity and Ssimilarity are strongly negatively correlated (r =\n    -0.745), and a significantly positive slope is almost absent; only one neuron (in M2) had both a\n    significantly positive Isimilarity and a significantly positive Ssimilarity.\n  source: Results, Population results, shape tuning, paragraph 1\n  quote: Overall, Isimilarity and Ssimilarity were significantly negatively correlated (r = −0.745,\n    p < 0.0001, n = 1,848), and we seldom found neurons associated with positive Ssimilarity, i.e.,\n    similarity that increased with distance: only one neuron (in M2) was associated with a\n    significantly positive Isimilarity and Ssimilarity\n  statistics:\n  - test: correlation\n    statistic: r = -0.745\n    p: 0.0001\n    p_relation: \"<\"\n    n: 1,848 neurons\n  depends_on:\n  - pop-significant-isimilarity\n  expected:\n  - quantity: correlation of Isimilarity and Ssimilarity\n    value: -0.745\n    tolerance: 0.0745\n  - quantity: neurons with significantly positive Isimilarity and Ssimilarity\n    value: 1\n    tolerance: 0\n  criterion: OPEN which correlation; the paper names Pearson's for other plain r values (Figure 5E)\n    and Spearman's where it uses it, so the readings are (a) Pearson and (b) Spearman, under the\n    contrast readings of the opening comment. Reproduced when one reading gives r within\n    tolerance with p < 0.0001 and at most 2 neurons with both significantly positive (the count of\n    1 takes an absolute margin of 1, as a relative tolerance on 1 is meaningless).\n- id: pop-dark-bright-consistent\n  statement: Isimilarity from dark and from bright shapes is consistent across neurons (Spearman's\n    r = 0.435, n = 1,847).\n  source: Results, Population results, shape tuning, paragraph 1; Figure 5B\n  quote: We also found that tuning similarity (Isimilarity) based on responses to dark and bright\n    stimuli was consistent (Fig. 5B)\n  statistics:\n  - test: Spearman's rank correlation\n    statistic: r = 0.435\n    p: 0.0001\n    p_relation: \"<\"\n    n: 1,847 neurons\n  depends_on:\n  - pop-significant-isimilarity\n  expected:\n    quantity: Spearman's r, Isimilarity dark against bright\n    value: 0.435\n    tolerance: 0.0435\n  criterion: Neurons with an Isimilarity at both contrasts (Materials and Methods, Statistical\n    tests). Reproduced when r is within tolerance and p < 0.0001, under either reliability\n    reading.\n- id: pop-contrast-invariance\n  statement: Contrast-invariant shape tuning is widespread; more than half of the neurons are\n    well driven and contrast invariant, with a median correlation between dark and bright responses\n    of 0.64.\n  source: Results, Population results, shape tuning, paragraph 2\n  quote: contrast-invariant shape tuning was widely prevalent across our dataset ... more than half\n    of the recorded neurons were well-driven and exhibited contrast-invariant shape tuning (median\n    correlation between responses to dark and bright stimuli in individual penetrations = 0.64)\n  depends_on:\n  - methods-sessions-and-neurons\n  expected:\n    quantity: median shape tuning invariance\n    value: 0.64\n    tolerance: 0.064\n  criterion: Tuning invariance as in the opening comment. The Methods (Statistical tests) take \"the\n    median of tuning invariance for shape for all recorded neurons\"; the Results say \"in\n    individual penetrations\". The readings are (a) the median over all neurons, (b) the median of\n    the per-penetration medians, each with unreliable values (c) left out or (d) counted as 0.\n    Reproduced when one reading gives a median within tolerance.\n- id: pop-sparse-across-penetrations\n  statement: Neurons with significant Isimilarity occur in small, sparse clusters in 55 of the 74\n    penetrations; only 28 penetrations have five or more such neurons, and 20 penetrations yielded\n    more than 30 neurons.\n  source: Results, Population results, shape tuning, paragraph 2; Figure 5A\n  quote: Neurons with high similarity in tuning (Fig. 5A) were widely distributed across 55 of the 74\n    penetrations in small, sparse clusters (blue). Only 28 penetrations had five or more neurons\n    with significant Isimilarity (Fig. 5A asterisks) ... simultaneous recordings from >30 neurons\n    (achieved on 20/74 penetrations)\n  depends_on:\n  - pop-significant-isimilarity\n  expected:\n  - quantity: penetrations with at least one neuron with significant Isimilarity\n    value: 55\n    tolerance: 5.5\n  - quantity: penetrations with five or more such neurons\n    value: 28\n    tolerance: 2.8\n  - quantity: penetrations with more than 30 responsive neurons\n    value: 20\n    tolerance: 2\n  criterion: Under the readings of pop-significant-isimilarity. Reproduced when one reading puts\n    all three values within tolerance.\n- id: pop-asymptote-20-percent\n  statement: When more than 30 neurons were recorded, the percentage of neurons with significant\n    Isimilarity levels off at about 20%, so shape clusters are not columnar.\n  source: Results, Population results, shape tuning, paragraph 2; Figure 5C\n  quote: When the number of recorded neurons was >30, the percentage of neurons with significant\n    Isimilarity asymptoted to ∼20% (Fig. 5C) suggesting that shape clusters were not \"columnar\"\n    extending across laminae in V4\n  depends_on:\n  - pop-sparse-across-penetrations\n  expected:\n    quantity: percentage of neurons with significant Isimilarity, penetrations with more than 30\n      neurons\n    value: 20\n    tolerance: 2\n    unit: percent\n  criterion: OPEN how the asymptote is summarized; the paper shows a scatter. The readings are (a)\n    the median of per-penetration percentages over penetrations with more than 30 neurons and (b)\n    the pooled percentage over their neurons, under the readings of pop-significant-isimilarity.\n    Reproduced when one reading is within tolerance; partially reproduced when none is but one\n    lies between 10% and 30% (a level far from all-layer clustering, which the statement rests\n    on).\n- id: pop-mean-isimilarity-yield\n  statement: In penetrations with few neurons the mean Isimilarity varies widely across\n    penetrations; with more than 30 neurons it levels off.\n  source: Results, Population results, shape tuning, paragraph 2; Figure 5D\n  quote: For penetrations with low neural yield, the standard deviation of Isimilarity across neurons\n    was large leading to great variability in the mean across penetrations; with larger yield (>30\n    neurons), mean of Isimilarity asymptoted (Fig. 5D)\n  depends_on:\n  - pop-significant-isimilarity\n  criterion: The paper reports no test. Per penetration the mean Isimilarity. Reproduced when the\n    standard deviation of the penetration means is smaller for penetrations with more than 30\n    neurons than for those with 30 or fewer, under the contrast reading that reproduces\n    pop-significant-isimilarity (all three shown); the two standard deviations and a Levene test\n    are reported.\n- id: pop-recording-density\n  statement: The fraction of neurons with significant Isimilarity is only weakly related to the\n    recording density (Pearson's r = 0.236, p = 0.0429).\n  source: Results, Population results, shape tuning, paragraph 2; Figure 5E legend\n  quote: We did not find a strong relationship between recording density and fraction of neurons\n    with significant Isimilarity (Fig. 5E) ... Pearson's correlation coefficient, r = 0.236, p =\n    0.0429\n  statistics:\n  - test: Pearson's correlation\n    statistic: r = 0.236\n    p: 0.0429\n    n: 74 penetrations\n  depends_on:\n  - pop-significant-isimilarity\n  expected:\n    quantity: Pearson's r, percentage with significant Isimilarity against recording density\n    value: 0.236\n    tolerance: 0.0236\n  criterion: The legend defines density as the depth range of the penetration's neurons divided by\n    their number, while the axis reads number of neurons per um. The readings are (a) neurons per\n    um and (b) um per neuron, crossed with the readings of pop-significant-isimilarity.\n    Reproduced when one reading gives r within tolerance and p < 0.05.\n- id: pop-within-vs-across-sessions\n  statement: Neurons within a penetration have slightly more similar shape tuning than neurons from\n    different sessions (mean correlation 0.0582 against 0.0022), and more so within 200 um (0.0918\n    against 0.0435 further apart), but all means are weak.\n  source: Results, Population results, shape tuning, paragraph 3\n  quote: The mean of the correlation coefficient between the responses of neuron pairs recorded in\n    different sessions was slightly but significantly less than that between simultaneously\n    recorded neuron pairs (0.0022 vs 0.0582, respectively; Welch's t test, p < 0.0001) ... The mean\n    correlation coefficient was even greater when it was based on neurons within a penetration\n    separated by ≤200 μm (0.0918) than neurons that were further apart (0.0435; Welch's t test, p <\n    0.0001). Importantly, the means were quite weak in all three cases\n  statistics:\n  - about: different sessions against same session pairs\n    test: Welch's t test\n    p: 0.0001\n    p_relation: \"<\"\n  - about: same-session pairs within 200 um against further apart\n    test: Welch's t test\n    p: 0.0001\n    p_relation: \"<\"\n  depends_on:\n  - methods-sessions-and-neurons\n  expected:\n  - quantity: mean correlation, pairs from different sessions\n    value: 0.0022\n    tolerance: 0.00022\n  - quantity: mean correlation, pairs from the same session\n    value: 0.0582\n    tolerance: 0.00582\n  - quantity: mean correlation, same-session pairs within 200 um\n    value: 0.0918\n    tolerance: 0.00918\n  - quantity: mean correlation, same-session pairs more than 200 um apart\n    value: 0.0435\n    tolerance: 0.00435\n  criterion: Welch's t test as in Materials and Methods, Statistical tests. OPEN, all able to change\n    the means. (1) The coefficient; \"the correlation coefficient between shape responses\" may be\n    (a) Pearson's r of mean rates over the 120 shapes or (b) the noise-corrected similarity.\n    (2) The contrast; (a) dark, (b) bright, (c) both contrasts as separate pairs. (3) The\n    cross-session pairs; (a) all pairs of responsive neurons from different sessions or (b) only\n    pairs within one monkey. Reproduced when both tests give p < 0.0001 in the stated direction\n    under every reading and all four means are within tolerance under one reading; partially\n    reproduced when the directions and p hold under every reading and no reading matches the\n    means. The 10% tolerance on means near zero is very tight; the size of the differences is\n    reported either way.\n- id: orientation-sf-isimilarity\n  statement: Tuning similarity computed from orientation x spatial frequency fits (12 Gabor filters)\n    to the shape responses is also diverse among nearby neurons, and its Isimilarity correlates\n    with the Isimilarity from the shape responses (Spearman's r = 0.588, n = 1,848).\n  source: Results, Tuning for stimulus orientation, paragraph 1; Figures 6A and 6B\n  quote: Our results show that tuning preferences for orientation were quite diverse for nearby\n    neurons, similar to our results based on shape responses (Fig. 6A). Across all penetrations,\n    Isimilarity based on orientation × SF was strongly correlated with those based on shape\n    responses\n  statistics:\n  - test: Spearman's correlation\n    statistic: r = 0.588\n    p: 0.0001\n    p_relation: \"<\"\n    n: 1,848 neurons\n  data: with_inputs\n  depends_on:\n  - pop-significant-isimilarity\n  expected:\n    quantity: Spearman's r, Isimilarity orientation x SF against shape\n    value: 0.588\n    tolerance: 0.0588\n  criterion: Materials and Methods, Feature models; shape responses fit as a linear weighted sum of\n    the outputs of 12 Gabor filters (4 orientations x 3 spatial frequencies) applied to the shape\n    images; similarity is Pearson's r of fitted responses; Isimilarity as in the opening\n    comment. Needs the shape images (Pasupathy and Connor 2001). OPEN, able to change the result;\n    the filters' spatial frequencies, envelope, phase and pooling, and the fitting method, are not\n    given (the paper cites Portilla and Simoncelli 2000 for the filters). The readings are (a)\n    the energy of each subband of a steerable pyramid with 4 orientations and 3 scales summed\n    over the image, and (b) quadrature Gabor energy at 4 orientations and 3 octave-spaced\n    frequencies summed over the image, each fit by least squares; with the contrast readings of\n    the opening comment. Reproduced when all readings give r within tolerance and p < 0.0001;\n    blocked as methods_underspecified when they differ in outcome.\n- id: orientation-auc-coarse-clusters\n  statement: Assayed at a coarse scale with two orthogonal orientations of the spindle shape, some\n    penetrations consist entirely of neurons preferring horizontal or vertical, and in others the\n    preference switches along the probe, as with optical imaging, even where single-neuron shape\n    clustering is not extensive.\n  source: Results, Tuning for stimulus orientation, paragraph 2; Figures 6C and 6D\n  quote: We found penetrations that entirely consisted of neurons with preference for horizontal or\n    vertical orientations (Fig. 6C) or penetrations where preference of neurons switched from one\n    to the other (Fig. 6D), similar to what has been observed with optical imaging techniques\n  criterion: Materials and Methods, Feature models; per neuron the AUC between spike counts (30 to\n    200 ms, per presentation) for shape 1 at 0 and 180 degrees and at 90 and 270 degrees, both\n    contrasts pooled, above 0.5 meaning vertical; averaged over neurons in 100 um depth bins. The\n    examples are M2p6 and M1p5. A penetration is all-one-preference when every occupied bin is on\n    one side of 0.5, and switching when bins on both sides form one change along depth. OPEN\n    which rotation is horizontal depends on the dataset's rotation labels and on shape 1 being\n    the spindle (Figure 1B). Reproduced when at least one penetration of each kind exists among\n    the 74 and M2p6 and M1p5 are each of one kind; the counts of each kind are reported.\n- id: apc-peaks-sparse-clustering\n  statement: Along angular position and curvature separately, clustering of tuning peaks is sparse;\n    of 59 penetrations with at least four neurons well fit by the APC model, only 7 (angular\n    position) and 5 (curvature) show a significant positive correlation between peak difference and\n    distance, and only 9 and 5 sessions have smaller mean and STD of the differences than a\n    permutation null.\n  source: Results, Tuning for curvature or angular position, paragraph 1\n  quote: Across 59 penetrations which included at least four neurons well-fit by the angular\n    position × curvature model, only 7 (5) penetrations exhibited statistically significant positive\n    correlation between the ΔAP (ΔCV) and inter-neuron distance (data not shown) ... we found that\n    a minority (nine and five) of sessions exhibited smaller mean and STD than the null\n    distributions (data not shown). These results indicate that evidence for clustered tuning is\n    sparse in our dataset\n  data: with_inputs\n  depends_on:\n  - methods-sessions-and-neurons\n  expected:\n  - quantity: penetrations with at least four well-fit neurons\n    value: 59\n    tolerance: 5.9\n  - quantity: penetrations with significant positive correlation, delta AP against distance\n    value: 7\n    tolerance: 0.7\n  - quantity: penetrations with significant positive correlation, delta CV against distance\n    value: 5\n    tolerance: 0.5\n  - quantity: sessions below the permutation null, AP\n    value: 9\n    tolerance: 0.9\n  - quantity: sessions below the permutation null, CV\n    value: 5\n    tolerance: 0.5\n  criterion: Materials and Methods, Feature models and Statistical tests; shape responses fit with\n    the 4D APC Gaussian of Pasupathy and Connor (2001) (one angular position Gaussian, three\n    curvature Gaussians for adjoining segments); well fit means goodness of fit r > 0.5 (Figure 7A\n    legend); delta AP is the circular absolute difference of AP peaks (0 to 180 degrees), delta\n    CV the absolute difference of central curvature peaks; per penetration Pearson's r of the\n    difference against inter-neuron distance over all pairs; the permutation null shuffles AP and\n    CV values across penetrations, 1,000 times, and a session counts when its mean and STD are\n    below the one-tailed 95% limit. Needs the shapes' boundary curvature descriptions (Pasupathy\n    and Connor 2001). OPEN, able to change counts; (1) the fitting procedure and which contrast's\n    responses are fit (readings dark, bright, both); (2) \"statistically significant positive\n    correlation\" as (a) two-sided p < 0.05 with r > 0 or (b) one-sided p < 0.05; (3) \"mean and\n    STD\" as (a) both below the limit or (b) either. Reproduced when every reading gives a\n    minority of penetrations and sessions (under half of the 59) and one reading puts the counts\n    within tolerance; partially reproduced when the minority holds and no reading matches the\n    counts.\n- id: apc-example-m2p51\n  statement: In M2p51, 33 neurons well fit by the APC model show mild clustering of angular position\n    peaks (superficial neurons near 330 degrees, deeper ones near 180), with a significant positive\n    correlation between delta AP and distance (r = 0.407) and none in that direction for curvature\n    (r = -0.109).\n  source: Results, Tuning for curvature or angular position, paragraph 1; Figure 7\n  quote: The distribution of angular position peaks shows mild clustering with superficial neurons\n    (magenta) tuned to features pointing to the lower right (∼330°) and deeper neurons (cyan) tuned\n    to features pointing to the left (∼180°). This relationship can be visualized by the\n    statistically significant positive correlation between inter-neuron distance and difference in\n    angular position tuning peaks (ΔAP) for all pairs of neurons (Fig. 7B). No such relationship is\n    evident along the curvature dimension (Fig. 7C)\n  statistics:\n  - about: delta AP against distance\n    test: Pearson's correlation\n    statistic: r = 0.407\n    p: 0.0001\n    p_relation: \"<\"\n    n: all pairs of 33 neurons\n  - about: delta CV against distance\n    test: Pearson's correlation\n    statistic: r = -0.109\n    p: 0.012\n    n: all pairs of 33 neurons\n  data: with_inputs\n  depends_on:\n  - apc-peaks-sparse-clustering\n  expected:\n  - quantity: well-fit neurons in M2p51\n    value: 33\n    tolerance: 3.3\n  - quantity: Pearson's r, delta AP against distance\n    value: 0.407\n    tolerance: 0.0407\n  - quantity: Pearson's r, delta CV against distance\n    value: -0.109\n    tolerance: 0.0109\n  criterion: Method and readings as in apc-peaks-sparse-clustering; M2p51 found as in\n    ex-m2p6-cluster, accepted when its well-fit count is within tolerance. Reproduced when the\n    three values are within tolerance under one reading; partially reproduced when the AP\n    correlation is significantly positive and the CV correlation is not, without matching values.\n- id: gyrus-penetrations-consistent\n  statement: Restricted to the 18 M2 penetrations centered on the V4 gyrus, the percentage of\n    neurons with significant Isimilarity is consistent with the whole population, also when only\n    neurons within about 1,500 um of the most superficial neuron are kept.\n  source: Results, Penetration trajectory, paragraph 1; Figure 8C\n  quote: When we restricted our analyses to 18 penetrations centered on the V4 gyrus (Fig. 8B,\n    rectangles), our results were consistent withwhat we observedacross the population (Fig. 8C,\n    compare gray and black dots) ... clusters were sparse even when we restricted our analyses to\n    the superficial cortex in those 18 penetrations, e.g., by considering neurons within ∼1,500 μm\n    of the superficial neuron in each penetration\n  depends_on:\n  - pop-significant-isimilarity\n  criterion: The 18 penetrations are those at the eight grid locations away from both meridians\n    (Figure 8B legend), identified in the paper only graphically (Figure 5A diamonds, Figure 8B);\n    the paper lists neither the sessions nor their grid coordinates, so the claim needs the\n    dataset to identify them. The paper reports no test of \"consistent\". The readings are (a) a\n    two-sided Mann-Whitney test of per-penetration percentages, the 18 against the other 56,\n    finds no difference at p < 0.05, and (b) the pooled percentage of the 18 penetrations with\n    more than 30 neurons is within the 10 to 30% band of pop-asymptote-20-percent. The 1,500 um\n    restriction recomputes Isimilarity on neurons within 1,500 um of depth zero. Reproduced when\n    both readings hold with and without the restriction.\n- id: texture-sparse-clusters\n  statement: For textures, of 979 neurons in 51 sessions (6 to 83 per penetration), a small subset\n    (207; 18 in M1, 189 in M2) across 34 of 51 penetrations (7 in M1, 27 in M2) showed clustered\n    selectivity, and 16 penetrations had five or more neurons with significant Isimilarity.\n  source: Results, Population results, texture tuning, paragraph 1; Figure 9A\n  quote: We studied the responses of 979 neurons across 51 sessions (M1, 17; M2, 34) ... (ranging\n    from 6 to 83 per penetration). As with shape stimuli, we found that a small subset of neurons\n    (207/ 979; M1, 18; M2, 189) across 34/51 (M1, 7; M2, 27) penetrations showed clustered\n    selectivity ... Across the 51 penetrations, 16 penetrations had five or more neurons that\n    exhibited regression lines with statistically significant intercepts (Fig. 9A, asterisks)\n  depends_on:\n  - methods-sessions-and-neurons\n  expected:\n  - quantity: neurons with significant Isimilarity, texture\n    value: 207\n    tolerance: 20.7\n  - quantity: of which in M1\n    value: 18\n    tolerance: 1.8\n  - quantity: of which in M2\n    value: 189\n    tolerance: 18.9\n  - quantity: penetrations with at least one such neuron\n    value: 34\n    tolerance: 3.4\n  - quantity: penetrations with at least one such neuron, M1\n    value: 7\n    tolerance: 0.7\n  - quantity: penetrations with at least one such neuron, M2\n    value: 27\n    tolerance: 2.7\n  - quantity: penetrations with five or more such neurons\n    value: 16\n    tolerance: 1.6\n  - quantity: most responsive neurons in a texture penetration\n    value: 83\n    tolerance: 8.3\n  criterion: As pop-significant-isimilarity, over the 40 textures with original and\n    contrast-reversed versions in place of dark and bright (contrast readings (a) original, (b)\n    contrast-reversed, (c) either), rotations pooled per texture as the Methods present them\n    (rotation is randomized to remove local orientation). The Methods exclude 48 of 979 neurons\n    with too few reliable similarities. Reproduced when one reading puts the counts within\n    tolerance; partially reproduced when the total and penetration counts are and a per-monkey\n    count is not.\n- id: texture-original-reversed-consistent\n  statement: Texture Isimilarity from original and contrast-reversed textures is consistent across\n    neurons (Spearman's r = 0.464, n = 905).\n  source: Results, Population results, texture tuning, paragraph 1; Figure 9B\n  quote: Tuning similarity based on both sets of texture data (original and contrast-reversed) was\n    highly consistent (Fig. 9B)\n  statistics:\n  - test: Spearman's rank correlation\n    statistic: r = 0.464\n    p: 0.0001\n    p_relation: \"<\"\n    n: 905 neurons\n  depends_on:\n  - texture-sparse-clusters\n  expected:\n  - quantity: Spearman's r, texture Isimilarity original against contrast-reversed\n    value: 0.464\n    tolerance: 0.0464\n  - quantity: neurons with Isimilarity for both versions\n    value: 905\n    tolerance: 90.5\n  criterion: Reproduced when r is within tolerance with p < 0.0001, under either reliability\n    reading.\n- id: texture-asymptote-20-percent\n  statement: For textures as for shapes, the fraction of neurons with a significant intercept levels\n    off at about 20% when many neurons are recorded.\n  source: Results, Population results, texture tuning, paragraph 1; Figure 10\n  quote: Our results from texture (Fig. 10, black symbols) are consistent with those from shape (Fig.\n    10, gray symbols): the fraction of neurons with a significant intercept asymptote to ∼20% when\n    the number of recorded neurons was large\n  depends_on:\n  - texture-sparse-clusters\n  expected:\n    quantity: percentage of neurons with significant texture Isimilarity, penetrations with more than\n      30 neurons\n    value: 20\n    tolerance: 2\n    unit: percent\n  criterion: As pop-asymptote-20-percent, on the texture penetrations, taking more than 30 neurons\n    as \"large\", the yield the paper uses for shapes. Readings (a) median of per-penetration\n    percentages and (b) pooled percentage. Reproduced when one reading is within tolerance;\n    partially reproduced when none is but one lies between 10% and 30%.\n- id: position-optimal-consistent\n  statement: In 33 M2 penetrations (723 neurons), Isimilarity computed from responses at each\n    neuron's optimal stimulus position correlates positively with Isimilarity at the aggregate RF\n    center (r = 0.325), so stimulus position and RF scatter do not explain the sparse clusters.\n  source: Results, Position invariance for shape tuning similarity, paragraph 1; Figure 12B\n  quote: We found a statistically significant positive correlation between Isimilarity in the RF\n    aggregate center versus RF optimal positions (r = 0.325, p < 0.0001, Fig. 12B). These results\n    provide evidence against the possibility that stimulus position and RF variability contributed\n    to the sparsity of clusters\n  statistics:\n  - test: Spearman's correlation\n    statistic: r = 0.325\n    p: 0.0001\n    p_relation: \"<\"\n    n: 723 neurons, 33 penetrations\n  depends_on:\n  - methods-sessions-and-neurons\n  expected:\n  - quantity: Spearman's r, Isimilarity optimal position against center\n    value: 0.325\n    tolerance: 0.0325\n  - quantity: neurons in the position test\n    value: 723\n    tolerance: 72.3\n  criterion: Materials and Methods, RF localization, paragraph 2; per neuron the optimal position\n    is the one of the five with the greatest variance-to-mean ratio of mean rates over the 15\n    shapes; similarity between two neurons uses each neuron's responses at its own optimal\n    position; Isimilarity as in the opening comment. The Results text says the comparison is with\n    \"responses to stimuli at the aggregate RF center\" of the position test, while the Figure 12B\n    axis says \"Isimilarity (shape test)\". The readings are (a) the center position of the position\n    test and (b) the main shape test with dark shapes (the position test's contrast). Spearman's\n    r as Figure 12B names it. Reproduced when every reading gives a positive r with p < 0.0001 and\n    one gives r within tolerance.\n- id: position-examples-invariant\n  statement: In two example penetrations, the pattern of tuning similarity is the same at all five\n    stimulus positions; a small cluster at every position in M2p9 and none at any position in\n    M2p28.\n  source: Results, Position invariance for shape tuning similarity, paragraph 1; Figures 11A and 11C\n  quote: Results from two representative recording sessions are shown in Figure 11A,C, and in both\n    cases, tuning similarity patterns were similar across all five positions\n  depends_on:\n  - methods-sessions-and-neurons\n  criterion: The paper shows the matrices and gives no measure. Sessions found as in\n    ex-m2p6-cluster, accepted when the neuron counts match Figure 11 (16 in M2p9, 55 in M2p28)\n    within 10%. Similarity matrices over the 15 shapes at each position, as in the opening\n    comment. The reading here, as the paper gives no measure, is Pearson's r between the reliable\n    off-diagonal similarities at each displaced position and at the center. Reproduced when all\n    eight correlations (four positions, two penetrations) are positive with p < 0.05.\n- id: simulation-random-with-domains\n  statement: Simulated oblique penetrations through gradual tuning progressions in angular position\n    and curvature give similarity matrices unlike the V4 data, while random tuning peaks\n    interleaved with short stretches of similar tuning reproduce the observed localized clusters.\n  source: Results, Simulation of tuning progression, paragraph 1; Figure 13\n  quote: The resulting similarity matrices (Fig. 13A-C, bottom panels) were quite unlike our V4 data\n    (compare with Figs. 3, 4). Random choice of tuning peaks in the APC space produced similarity\n    matrices reminiscent of the majority of V4 data ... the observed patterns correspond best to\n    random selectivity interspersed with small domains of similar tuning for shapes\n  data: with_inputs\n  criterion: A simulation, not a test on recorded data, judged by eye in the paper. Its parameters\n    are partly given (30 model neurons, 2D Gaussian tuning in APC space with SDs drawn from normal\n    distributions of mean 60 degrees, SD 10, and mean 0.5, SD 0.1; Poisson spike counts; three\n    repeats in the Figure 13 legend, 200 ms trains in the Methods); peak amplitudes and the\n    progression step sizes are not. Recorded so the finding is covered; it cannot be tested on\n    the dataset.\n"
}
```

```
File created successfully at: claims/001357/10.1523-jneurosci.1893-23.2024.yaml (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
python tools/claims_check.py claims/001357/10.1523-jneurosci.1893-23.2024.yaml paper/10.1523-jneurosci.1893-23.2024.txt; grep -n -E "[^\"']: " claims/001357/*.yaml | grep -v -E "^\s*[0-9]+:\s*(#|-? ?[a-z_]+: )" | head
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
grep -n -E " #|: " claims/001357/*.yaml | grep -v -E "^[0-9]+:#" | grep -v -E "^[0-9]+:\s*-? ?[a-z_]+: "
```

```
138:    their responses to the tested shapes ... For some neurons (Neurons #1-9, #14, and #17),
171:    similarity in tuning (rsimilarity = 0.82), but Neurons #18 and #19 recorded on contacts 80 μm
252:    OPEN: the Gaussian's width, the column shown, and how the sink is located are not given; the
351:    similarity that increased with distance: only one neuron (in M2) was associated with a
769:    10, gray symbols): the fraction of neurons with a significant intercept asymptote to ∼20% when
```

**Agent calls Bash**

```bash
cd claims/001357 && python - <<'EOF'
import re
p='10.1523-jneurosci.1893-23.2024.yaml'
s=open(p).read()
s=s.replace("    OPEN: the Gaussian's width","    OPEN, the Gaussian's width")
# convert quotes containing '#' or ': ' to folded block scalars
out=[];lines=s.split('\n');i=0
while i<len(lines):
    l=lines[i]
    if l.startswith('  quote: '):
        j=i+1
        while j<len(lines) and lines[j].startswith('    '): j+=1
        block=[l[len('  quote: '):]]+[x[4:] for x in lines[i+1:j]]
        text=' '.join(block)
        if '#' in text or ': ' in text:
            out.append('  quote: >-'); out+=['    '+b for b in block]
        else: out+=lines[i:j]
        i=j; continue
    out.append(l); i+=1
open(p,'w').write('\n'.join(out))
EOF
cd ../.. && python tools/claims_check.py claims/001357/10.1523-jneurosci.1893-23.2024.yaml paper/10.1523-jneurosci.1893-23.2024.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001357/10.1523-jneurosci.1893-23.2024.yaml",
 "old_string": "These results indicate that evidence for clustered tuning is\n    sparse in our dataset",
 "new_string": "These results indicate that evidence for clustered tuning ...\n    is sparse in our dataset"
}
```

```
The file claims/001357/10.1523-jneurosci.1893-23.2024.yaml has been updated successfully.
```

**Agent calls Bash**

```bash
python tools/claims_check.py claims/001357/10.1523-jneurosci.1893-23.2024.yaml paper/10.1523-jneurosci.1893-23.2024.txt; grep -n -E "—|rather" claims/001357/*.yaml; python -c "
import yaml;d=yaml.safe_load(open('claims/001357/10.1523-jneurosci.1893-23.2024.yaml'))
c=d['claims'];print(len(c),sum('quote' in x for x in c),sum('statistics' in x for x in c),sum('criterion' in x for x in c),[x['id'] for x in c if x.get('data')])"
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd claims/001357 && python - <<'EOF'
p='10.1523-jneurosci.1893-23.2024.yaml'
s=open(p).read()
a="""    value: 1
    tolerance: 0
"""
print(s.count(a))
s=s.replace(a,"""    value: 1
    tolerance: 1
""")
s=s.replace("The count of 1 is small, so it takes no relative tolerance; reproduced when\n    at most 2 neurons","The count of 1 takes an absolute tolerance of 1, as 10% of 1 is less than\n    one neuron; reproduced when at most 2 neurons")
open(p,'w').write(s)
EOF
cd ../.. && python tools/claims_check.py claims/001357/10.1523-jneurosci.1893-23.2024.yaml paper/10.1523-jneurosci.1893-23.2024.txt; grep -n "absolute" claims/001357/*.yaml
```

Result: not kept, because it reads the paper's text.

**Agent**

I've written `claims/001357/10.1523-jneurosci.1893-23.2024.yaml`. The quote checker reports 0 problems (27 claims, 27 quotes, 12 statistical values). Nothing is committed.

**Text read:** the version of record, from the PDF supplied by a person and extracted as text: main text, Materials and Methods, and figure legends. The paper has no supplement, so none was needed, and I didn't need to open the PDF.

**Code:** the paper links no analysis code and has no code or data availability statement. The analyses were in the authors' own MATLAB code, which is not public. The only link is to the stimulus software, pype (github.com/mazerj/pype3, HEAD 49056d6f). It settles no analysis detail.

**Claims:** 27 in all.
- **Quotes:** all 27 have one; none needed an `inferred` note.
- **Statistics:** 10 claims record the paper's tests.
- **Criteria:** all 27 have one.
- **Outside data:** 4 claims are `with_inputs` because they need the shape images and curvature descriptions of Pasupathy & Connor (2001), which this paper neither prints nor deposits. They are the Gabor (orientation × spatial frequency) fits, the two angular position × curvature model claims, and the simulation. The simulation is recorded so the finding is covered but can't be tested on the dataset.
- **Recorded data:** the other 23 use the recordings.

**Details the paper leaves open, with the readings named for each:**
- **Reliability cut-off:** "confidence limit >0.5" is read as (a) the full width of the bootstrap interval or (b) its half-width. The interval's level isn't given; I used 95%, the level the paper uses for its regressions.
- **Which contrast gives the population Isimilarity:** dark, bright, or significant at either.
- **Whether the 344 neurons also need a negative slope:** yes or no. The counts (344 + 1,504 = 1,848) suggest the count is of significant intercepts alone.
- **Isimilarity–Ssimilarity correlation type:** Pearson or Spearman.
- **Median invariance of 0.64:** the median over all neurons, or the median of per-penetration medians (the Methods and the Results say different things); unreliable values either left out or counted as 0.
- **Welch's test (same versus different sessions):** Pearson or noise-corrected correlation; dark, bright or both contrasts; cross-session pairs from all sessions or within one monkey only.
- **Recording density (Fig. 5E):** neurons per µm (the axis label) or µm per neuron (the legend). This is an inconsistency within the paper.
- **The ~20% level (shape and texture):** the median of per-penetration percentages, or the pooled percentage, over penetrations with more than 30 neurons.
- **Gabor filter bank:** frequencies, envelope, phase and pooling aren't given. Readings: a steerable pyramid, or quadrature Gabor energy.
- **Angular position × curvature model:** the fitting procedure and the contrast used aren't given; significance as one- or two-sided; a session counted when both its mean and standard deviation fall below the null limit, or either.
- **Position test (Fig. 12B):** the comparison is with the position test's center position (the Results text) or with the main shape test (the figure's axis).
- **CSD:** the smoothing width, which column of contacts, and how the sink is picked. Readings: the earliest sink, or the largest one.
- **Peak responses in M1p12:** baseline-subtracted or raw.
- **Penetration names (M2p6, M1p12, M2p9, M2p28, M2p51, M1p5):** how the numbers are assigned isn't said. Readings: order among shape sessions, order among all sessions, or the dataset's own label. Each is accepted only when the neuron count matches the paper's.

**Missing from the paper that claims need:**
- **The 18 gyral penetrations:** they are identified only in figures (Fig. 5A, Fig. 8B), with no session list or grid coordinates. "Consistent" also has no test; I named two readings.
- **Position-invariance examples (Fig. 11):** the paper gives no measure of similarity across positions, so the criterion's measure is a stated reading, not the paper's.
- **The simulation (Fig. 13):** peak amplitudes and step sizes aren't given.
- **CSD claim:** it needs the LF signal. The archive's summary lists only units and electrode groups, so the dataset may not hold it.

## End of run

19 turns, 5 minutes, result: success.
