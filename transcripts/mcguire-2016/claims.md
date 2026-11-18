# mcguire-2016 · claims · run 42876479824

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  grep -n "^#" docs/protocol.md | head -50; ls paper/; wc -l paper/*
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  sed -n 1,198p docs/protocol.md
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
[... 177 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat claims/fouke-2025.yaml | head -150; cat papers/datasets/mcguire-2016.yaml
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
[... 138 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 150,400p claims/fouke-2025.yaml | grep -n -A30 "^checks\|^- id: fig1g" | head -60; tail -30 claims/fouke-2025.yaml
```

```
n: 4 ZF fish, 1887 swims
  - about: tail angle, ZF against DC, turn-inducing stimuli
    test: two-way ANOVA, Tukey post hoc
    p: 0.05
    p_relation: "<"
- id: fig4f-longer-on-duration
  statement: Swim-onset-associated neurons in DC have a longer active (ON) phase than in ZF,
    while non-motor-associated neurons have similar ON durations.
  source: Figure 4E and 4F
  quote: While the active, above baseline, ‘ON’ duration of neural activity for non-motor associated
    neurons is similar in ZF and DC, swim start-associated neurons in DC show a significantly longer
    activity phase than ZF
  statistics:
  - test: two-way ANOVA, Tukey post-hoc
    p: 0.05
    p_relation: "<"
    n: 4 ZF and 2 DC fish
- id: fig4hi-vspn-lateralized
  statement: Motor-associated neurons in the putative ventromedial spinal projection neurons of
    both species encode turn direction in a lateralized way, correlating more with ipsilateral
[... 10 more lines not kept]
```

**Agent**

Now the paper.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1371-journal.pbio.1002549.txt"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1371-journal.pbio.1002549.txt",
 "offset": 344
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  head -80 paper/ssc-4.data-description.txt; grep -n -i "github\|code\|http" paper/10.1371-journal.pbio.1002549.txt | head; ls claims | head -3; python tools/claims_check.py --help 2>&1 | head
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  cat schemas/claims.schema.json | head -200
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
[... 180 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 200,400p schemas/claims.schema.json; ls claims/ | grep -i "ssc\|crcns" ; grep -l "crcns" claims/*.yaml | head -3
```

```
"then": {
              "required": [
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
[... 137 more lines not kept]
```

**Agent calls Bash**

```bash
cd  ls -t claims | head -3; f=$(ls -t claims/*.yaml | head -1); head -40 $f
```

```
zhong-2026.yaml
zhu-2022.yaml
zhuang-2025.yaml
# Claims for Zhuang, Lemak, Sridhar & Nelson (2025), Brain 149:238-251, on dandiset 001177.
# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"), 2026-10-28,
# protocol pilot-12 as stated in docs/protocol.md. The writer did not look at the dandiset's data or
# files; only its title and description on the archive were read. Claim fig1fg-delay-discounting
# was added by the check of 2026-10-28.
#
# Text read: the version of record (open access, CC BY), full text as served by Europe PMC
# (PMC12597312), with its one supplement, awaf312_supplementary_data.pdf (Figures S1 to S8 and
# legends, Supplementary Materials and methods, and Table 1, "Experimental analysis and
# statistics"). Figure panels of the main paper were not available as images; values in the main
# figure legends were read from the text. The pie-chart percentages of Figures S5D and S8A-B were
# read from the supplement PDF (pages 7 and 10), as the text holds only the legends.
#
# Code read. The paper links (1) UCSF-Nelson-Lab/ICD-Cognitive-Analysis, tag ICD, commit 5528e22
# (Zenodo doi:10.5281/zenodo.10703139, record 10703140): Python scripts that count task events per
# block of the delay discounting task (delay_discounting_task.py, phase2.py, phase3.py) and
# Summary_Cognitive.m, which averages each mouse's sessions within a condition, fits
[... 23 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n -m3 "^schema_version\|^paper:\|^dataset" claims/zhuang-2025.yaml; grep -n "S1 Data\|supporting information\|journal.pbio" claims/*.yaml | grep -i "where" | head -5
```

```
79:schema_version: 2
80:dataset:
83:paper: doi:10.1093/brain/awaf312
```

**Agent**

The full text has the main text, Methods and the supplement legends. The paper links no code. I'll write the claims file now.

**Agent calls Write**

```json
{
 "file_path": "claims/mcguire-2016.yaml",
 "content": "# Claims for McGuire, Telian, Laboy-Juarez, Miyashita, Lee, Smith & Feldman (2016), PLoS Biology\n# 14(8) e1002549, on CRCNS ssc-4.\n# Written by an agent (model \"claude-opus-5-5\", Claude Code, runner \"GitHub Actions\"), 2026-11-10,\n# protocol pilot-14 as stated in docs/protocol.md. The writer did not look at the dataset's data or\n# files; only its title and the summary of its data descriptor were read, to know which experiments\n# it holds.\n#\n# Text read: the version of record (open access), full text as served by Europe PMC (PMC5004814,\n# JATS XML flattened), with the Methods and the legends of the supporting information (S1 to S7\n# Figs, S1 Table, S1 and S2 Data). The contents of S1 Table (baseline firing rates by layer and unit\n# type, DOCX) and of S1 and S2 Data (XLSX) are not in the text; no claim rests on numbers found only\n# there. No PDF was supplied, so no figure could be read. Table 1 is garbled in the text: its\n# sequence rows read \"FFF 34 120 65.7 Right\", \"FMS 34 132 54.4 Right\", \"SMF 34 132 54.7 Left\", \"SSS\n# 34 148 44.6 Left\" under headers that do not fit. They are read here as interpulse interval (ms),\n# duration (ms, matching the 120 to 148 ms of the Results), mean speed (mm/s, ordered as the\n# Results say) and rewarded port.\n#\n# Code read: none. The paper links no code. The Methods say the regression was run in Matlab and\n# the decoders in Python with scikit-learn; neither script is published.\n#\n# Data the paper used. Female Long-Evans rats (>3 months). Task: the rat enters a nose poke with\n# its right C, D and E row whiskers on a panel; 75 to 100 ms later the panel delivers one of four\n# three-impulse sequences, FFF, FMS, SMF or SSS (F, M, S impulses of 16, 22, 28 ms; 34 ms gap\n# between impulses; impulse onsets 50 to 62 ms apart); the rat holds 250 ms, then chooses the right\n# port (rewarded for FFF and FMS) or the left (SMF and SSS). Eight rats were trained on this task\n# (behaviour, Figure 2, S2 Fig); six also ran a fixed-panel control. Two other rats (58B, 60W) ran\n# an FSFS against SFFS task without recordings (Figure 3). Recordings: four tetrodes in S1 (C1-4,\n# D2-4, E3 columns), advanced about 140 um every one or two sessions from L2/3 to L6, 80 sessions\n# in five rats (18FB, 18Ri, 18Ro, 62BS, 107St), 306 single units and 167 multi-unit clusters (473\n# units). Each unit has a depth (layer boundaries L2/3 200-650 um, L4 650-975, L5a 975-1285, L5b\n# 1285-1575, L6 1575-2200 um), a single or multi-unit label, and an RS or FS label (FS when\n# trough-to-peak width < 0.375 ms). Per trial: stimulus, nose poke entry, stimulus onset, drink\n# port choice and nose poke withdrawal time. The panel speed profile of each sequence is in S1 Fig\n# and S2 Data. High-speed video of 43 trials (4 rats) is summarised in S6 Fig, with data in S2\n# Data. The dataset's descriptor says it holds the spike and trial data of the five recorded rats\n# over 80 sessions, the basis of Figures 4 to 9.\n#\n# Method details used across claims, from the Methods. Temporally modulated units: permutation\n# test on 10-ms bins, 10,000 permutations, p < 0.05 (Methods, Temporal response modulation). PSTHs\n# in 1 ms bins aligned to first impulse onset. Mean impulse-evoked rate in 5-35 ms after impulse\n# onset; impulse baseline 0-10 ms before impulse onset; impulse-responsive units by t test of the\n# two (Methods, Stimulus-evoked responses). Unit classes from the regression of firing rate (5-ms\n# bins, 0-180 ms after stimulus onset, all trials of each sequence) on panel speed integrated over\n# 5 to 180 ms windows (Methods, Stimulus regression). Decoders per Methods, Neural Decoders.\nschema_version: 2\npaper: doi:10.1371/journal.pbio.1002549\nclaims:\n- id: fig2ab-fms-smf-not-discriminated\n  statement: All eight rats discriminated FFF from SSS but treated FMS and SMF as equivalent and\n    intermediate; seven of eight showed no difference between FMS and SMF, and one rat (62SC) made\n    more right choices to FMS than to SMF.\n  source: Results, Behavioral Discrimination of FFF, FMS, SMF, and SSS Sequences, paragraph 3;\n    Figure 2A and 2B\n  quote: Seven out of eight rats failed to differentiate at all between FMS from SMF stimuli\n    (proportion test, Bonferroni-adjusted p -value >0.00625). One rat (62SC) showed modest but\n    significant discrimination, with more right-side choices to FMS than SMF stimuli ( p = 0.0039).\n  statistics:\n  - about: FMS against SMF right-choice fraction, each of seven rats\n    test: proportion test\n    p: 0.00625\n    p_relation: \">\"\n    corrected: Bonferroni\n    n: seven rats\n  - about: FMS against SMF right-choice fraction, rat 62SC\n    test: proportion test\n    p: 0.0039\n    n: one rat\n  criterion: Per rat, over all its FFF-FMS-SMF-SSS sessions pooled, the fraction of right-port\n    choices for each stimulus (Figure 2B, \"all behavior sessions\"). FMS against SMF is compared by\n    a two-proportion test at the Bonferroni level 0.05/8 = 0.00625 (Results). The paper does not\n    say which proportion test; the readings are (a) the chi-square test of two proportions with\n    continuity correction, (b) the same without it (a two-proportion z test). Which trials count\n    is also open; the readings are (i) all completed trials, (ii) completed trials excluding\n    premature withdrawals and trials with no choice. Reproduced when, for every rat the data hold,\n    FFF has a higher right-choice fraction than SSS, FMS and SMF both lie between them, and FMS\n    against SMF is not significant at 0.00625 for every rat but 62SC, under one reading. The paper\n    tests eight rats; if the data hold fewer, the result is stated for those held and is at most\n    partially reproduced.\n- id: training-days\n  statement: Rats trained on FFF-FMS-SMF-SSS discrimination for 14.2 days on average (s.d. 4.4,\n    range 8 to 22).\n  source: Results, Behavioral Discrimination of FFF, FMS, SMF, and SSS Sequences, paragraph 3\n  quote: After 14.2 ± 4.4 (standard deviation [s.d.]) (range: 8–22) d of training on\n    FFF-FMS-SMF-SSS discrimination, all eight rats successfully discriminated FFF from SSS stimuli\n  expected:\n  - quantity: mean days of FFF-FMS-SMF-SSS training per rat\n    value: 14.2\n    tolerance: 4.4\n    unit: days\n  - quantity: fewest days of training\n    value: 8\n    tolerance: 0.8\n    unit: days\n  - quantity: most days of training\n    value: 22\n    tolerance: 2.2\n    unit: days\n  criterion: Days are counted per rat as the distinct days with FFF-FMS-SMF-SSS sessions. The\n    tolerance on the mean is the stated s.d. The paper counts eight rats; the result is stated for\n    the rats the data hold.\n- id: fig2c-choice-follows-mean-speed\n  statement: Relative right-port choice (fraction of right choices for a stimulus minus the mean\n    over all stimuli) was strongly related to the mean speed of the sequence for all rats.\n  source: Results, Behavioral Discrimination of FFF, FMS, SMF, and SSS Sequences, paragraph 3;\n    Figure 2C\n  quote: Right drink port choice was strongly related to mean sequence speed for all rats ( Fig 2C\n    ).\n  criterion: Relative right choice per rat and stimulus as defined in the Results (fraction right\n    for the stimulus minus the mean fraction right over the four stimuli). Mean speeds from Table 1\n    (65.7, 54.4, 54.7 and 44.6 mm/s for FFF, FMS, SMF, SSS; see the opening comment on the garbled\n    table). The paper names no test or measure for \"strongly related\". The readings are (a) for\n    each rat, relative right choice ordered FFF > (FMS and SMF) > SSS; (b) for each rat, a\n    positive Pearson correlation of relative right choice with mean speed over the four stimuli\n    with r > 0.8. Reproduced when every rat the data hold satisfies one reading; partially when\n    all but one do.\n- id: fig2d-fixed-panel-impairs\n  statement: Fixing the panel in place, with the piezo moving behind it, impaired FFF against SSS\n    discrimination in all but one of six rats tested.\n  source: Results, Behavioral Discrimination of FFF, FMS, SMF, and SSS Sequences, paragraph 4;\n    Figure 2D; S2B Fig\n  quote: Panel fixation strongly impaired behavioral discrimination in all but one rat\n  statistics:\n  - about: FFF minus SSS right-choice fraction, fixed-panel against normal sessions\n    test: two-sided paired t test\n    p: 0.012\n  criterion: Per rat, discrimination as the fraction of right choices to FFF minus that to SSS\n    (S2B Fig), on the fixed-panel session and on the final normal session before it. Paired t\n    test across rats, two-sided (S2B Fig legend). Reproduced when the fixed-panel value is lower\n    in all rats but one and p < 0.05. The d-prime of Figure 2D is shown as a variant, computed as\n    z(right on FFF) minus z(right on SSS); the correction for rates of 0 or 1 is not given and is\n    a standard choice (add 0.5 to counts) that cannot change the sign. If the data hold no\n    fixed-panel sessions the claim cannot be tested on them.\n- id: dprime-fff-sss-range\n  statement: Discrimination of FFF against SSS in normal sessions was modest, with d-prime from 0.5\n    to 1.5 across rats.\n  source: Discussion, Behavioral Integration of Stimulus Sequences, paragraph 2; Figure 2D\n  quote: 'Task performance was relatively low (d-prime for FFF versus SSS: 0.5–1.5), as in a prior\n    study [ 13 ]'\n  expected:\n  - quantity: lowest per-rat d-prime, FFF against SSS\n    value: 0.5\n    tolerance: 0.05\n  - quantity: highest per-rat d-prime, FFF against SSS\n    value: 1.5\n    tolerance: 0.15\n  criterion: Per rat, d-prime as z(fraction right on FFF) minus z(fraction right on SSS) over its\n    normal sessions. Which sessions enter is open; the readings are (a) all FFF-FMS-SMF-SSS\n    sessions pooled, (b) the mean of per-session d-prime. Reproduced when every rat's value lies\n    in 0.45 to 1.65 under one reading.\n- id: fig3-fsfs-sffs-intensity-only\n  statement: Two rats discriminated FSFS from SFFS when the sequences differed in mean speed (70\n    and 69.2% correct) but not when mean speed was the same (52 and 53%), even after more than 20\n    days; d-prime was 1.02 against 0.12.\n  source: Results, Discrimination of FSFS versus SFFS Sequences, paragraph 2; Figure 3B and 3C\n  quote: Both rats consistently discriminated FSFS from SFFS when they had different mean speed\n    (58B: 70 ± 1.5% correct, 60W: 69.2 ± 1.6%), but not when they had the same mean speed, even\n    after >20 cumulative days of training (58B: 52 ± 0.8% correct; 60W: 53 ± 0.8% correct). This\n    was evident in the d-prime measure of discrimination between FSFS and SFSF stimuli, which was\n    1.02 for different-intensity stimuli and 0.12 for same-intensity stimuli\n  data: elsewhere\n  where: PLOS Biology supporting information of doi:10.1371/journal.pbio.1002549, S1 Data (XLSX,\n    data for Figure 3)\n  expected:\n  - quantity: 58B percent correct, different intensity\n    value: 70\n    tolerance: 1.5\n    unit: percent\n  - quantity: 60W percent correct, different intensity\n    value: 69.2\n    tolerance: 1.6\n    unit: percent\n  - quantity: 58B percent correct, same intensity\n    value: 52\n    tolerance: 0.8\n    unit: percent\n  - quantity: 60W percent correct, same intensity\n    value: 53\n    tolerance: 0.8\n    unit: percent\n  - quantity: d-prime, different intensity\n    value: 1.02\n    tolerance: 0.102\n  - quantity: d-prime, same intensity\n    value: 0.12\n    tolerance: 0.012\n  criterion: These rats were not recorded (\"No recordings were performed\", Methods), so the\n    dataset does not hold them. Percent correct is the mean over sessions with its SEM (Figure 3\n    legend), the tolerance used here. The d-prime is the mean over sessions and over the two\n    rats (Figure 3C, \"mean ± SEM across sessions\"); the text does not say whether the two rats\n    are averaged; the readings are (a) the mean of both rats' session values, (b) each rat\n    separately.\n- id: units-recorded\n  statement: The recordings yielded 306 single units and 167 multi-unit clusters (473 units) over\n    80 sessions in five rats, 3.8 single units per session on average (range 0 to 11).\n  source: Results, S1 Recordings during Behavioral Discrimination, paragraph 1\n  quote: Spike sorting yielded 3.8 (range: 0–11) well-separated single units per recording session\n    ( Fig 4B ). ... We obtained 306 single units and 167 multi-unit clusters (total: 473 units)\n    across 80 recording sessions in five rats (18FB, 18Ri, 18Ro, 62BS, 107St)\n  expected:\n  - quantity: single units\n    value: 306\n    tolerance: 30.6\n  - quantity: multi-unit clusters\n    value: 167\n    tolerance: 16.7\n  - quantity: recording sessions\n    value: 80\n    tolerance: 0\n  - quantity: rats\n    value: 5\n    tolerance: 0\n  - quantity: mean single units per session\n    value: 3.8\n    tolerance: 0.38\n  - quantity: most single units in one session\n    value: 11\n    tolerance: 1.1\n  criterion: Counted from the units as deposited, single and multi by their labels. Sessions and\n    rats are whole numbers that a deposit of the same recordings fixes, so their tolerance is 0.\n- id: baseline-rates\n  statement: Mean firing rate in the 25-ms prestimulus baseline in the nose poke was 6 to 10 Hz\n    across layers for RS units, 8 to 32 Hz for FS units, and higher for multi-unit clusters.\n  source: Results, S1 Recordings during Behavioral Discrimination, paragraph 2; S1 Table\n  quote: Mean firing rate during a 25-ms prestimulus baseline period in the nose poke was 6–10 Hz\n    across layers for RS units, 8–32 Hz for FS units, and higher for multi-unit clusters ( S1 Table\n    ).\n  expected:\n  - quantity: lowest layer mean baseline rate, RS single units\n    value: 6\n    tolerance: 0.6\n    unit: Hz\n  - quantity: highest layer mean baseline rate, RS single units\n    value: 10\n    tolerance: 1\n    unit: Hz\n  - quantity: lowest layer mean baseline rate, FS single units\n    value: 8\n    tolerance: 0.8\n    unit: Hz\n  - quantity: highest layer mean baseline rate, FS single units\n    value: 32\n    tolerance: 3.2\n    unit: Hz\n  criterion: Baseline is the 25 ms before first impulse onset, over all trials; per unit the mean\n    rate, then the mean over units in each layer (L2/3, L4, L5a, L5b, L6) and type (RS single, FS\n    single, multi-unit). All units, modulated or not (S1 Table legend). Reproduced when every layer\n    mean of RS units lies in 5.4 to 11 Hz and of FS units in 7.2 to 35.2 Hz, and the multi-unit\n    mean exceeds the RS mean in most layers. A layer whose RS and FS means both fall inside but\n    whose extreme sits off a bound is still reproduced; the range bounds are checked as given.\n- id: temporal-modulation-count\n  statement: 305 of 473 units (63.5%) had firing rates significantly modulated in time during the\n    nose poke period.\n  source: Results, S1 Recordings during Behavioral Discrimination, paragraph 3; Methods, Temporal\n    response modulation\n  quote: Three hundred five out of 473 units (63.5%) showed significant temporal modulation.\n  expected:\n  - quantity: temporally modulated units\n    value: 305\n    tolerance: 30.5\n  - quantity: percent of units temporally modulated\n    value: 63.5\n    tolerance: 6.35\n    unit: percent\n  criterion: The Methods fix 10-ms bins, 10,000 permutations of spike times and p < 0.05. Two\n    details are open. The window is \"0–180 ms after NP entry\" in the Methods but \"the stimulus\n    presentation period\" in the same sentence, and the stimulus starts 75 to 100 ms after entry;\n    the readings are (a) 0 to 180 ms after nose poke entry, (b) 0 to 180 ms after stimulus onset,\n    the window of the regression. The statistic compared with the permuted spikes is not named\n    (the Methods cite ref. 55); the readings are (i) the variance across bins of the trial-averaged\n    10-ms PSTH, (ii) the sum over bins of squared deviations of the PSTH from the mean permuted\n    PSTH. Spikes are permuted uniformly in time within the window on each trial. Reproduced when\n    one reading gives a count within tolerance.\n- id: modulated-higher-baseline\n  statement: Temporally modulated units were distributed uniformly across columns and layers and had\n    higher baseline firing rates than non-modulated units.\n  source: Results, S1 Recordings during Behavioral Discrimination, paragraph 3; Figure 4C; S3B Fig\n  quote: Temporally modulated units were distributed uniformly across whisker columns and layers (\n    Fig 4C ) and had higher baseline firing rates than non-modulated units ( S3B Fig ).\n  depends_on:\n  - temporal-modulation-count\n  criterion: Baseline as in baseline-rates. S3B Fig shows RS single units by layer, mean ± SEM.\n    Reproduced when the mean baseline rate of modulated RS single units exceeds that of\n    non-modulated RS single units in most layers. \"Uniformly\" has no test in the paper; the\n    fraction of modulated units per layer is reported, and a chi-square test of layer against\n    modulation at 0.05 is shown as a variant (a standard choice).\n- id: fig4d-evoked-modulation-by-layer\n  statement: The mean impulse-evoked firing rate modulation, above the pre-impulse baseline, was\n    14.2 Hz in L2/3, 15.2 in L4, 6.3 in L5a, 14.4 in L5b and 7.0 in L6, greatest in L2/3, L4 and L5b.\n  source: Results, S1 Recordings during Behavioral Discrimination, paragraph 4; Figure 4D\n  quote: The mean impulse-evoked firing rate modulation (in Hz above pre-impulse baseline) was 14.2\n    ± 2.3 in L2/3, 15.2 ± 1.9 in L4, 6.3 ± 1.2 in L5a, 14.4 ± 2.3 in L5b, and 7.0 ± 1.5 in L6 ( n =\n    28–82 units per layer).\n  depends_on:\n  - temporal-modulation-count\n  expected:\n  - quantity: evoked modulation L2/3\n    value: 14.2\n    tolerance: 2.3\n    unit: Hz\n  - quantity: evoked modulation L4\n    value: 15.2\n    tolerance: 1.9\n    unit: Hz\n  - quantity: evoked modulation L5a\n    value: 6.3\n    tolerance: 1.2\n    unit: Hz\n  - quantity: evoked modulation L5b\n    value: 14.4\n    tolerance: 2.3\n    unit: Hz\n  - quantity: evoked modulation L6\n    value: 7.0\n    tolerance: 1.5\n    unit: Hz\n  criterion: Temporally modulated units by layer. Per the Methods (Stimulus-evoked responses), the\n    modulation is the maximum or minimum rate in a 40-ms window after impulse onset (PSTH in 1-ms\n    bins, smoothed with a 10-ms boxcar) minus the mean rate 0 to 10 ms before impulse onset; the\n    tolerance is the reported spread, taken as SEM across units. Open details, with readings.\n    Maximum or minimum: (a) the extreme of larger absolute deviation, signed; (b) its absolute\n    value. Pooling: (i) the PSTH over all impulses of all sequences pooled, one value per unit;\n    (ii) one value per impulse and sequence, averaged per unit. Reproduced when all five layer\n    values fall within tolerance under one combination, and partially when L5a and L6 are the two\n    lowest layers under one combination but some values fall outside.\n- id: latency-by-layer\n  statement: Among impulse-responsive units, peak response latency was shortest in L4, L5a and L5b\n    (9.8, 10.3 and 12.0 ms) and longest in L2/3 and L6 (13.8 and 16.1 ms).\n  source: Results, S1 Recordings during Behavioral Discrimination, paragraph 4\n  quote: Among units with significant impulse responses, peak response latency was shortest in L4,\n    L5a, and L5b (9.8, 10.3, and 12.0 ms) and longest in L2/3 and L6 (13.8 and 16.1 ms).\n  depends_on:\n  - temporal-modulation-count\n  expected:\n  - quantity: latency L4\n    value: 9.8\n    tolerance: 0.98\n    unit: ms\n  - quantity: latency L5a\n    value: 10.3\n    tolerance: 1.03\n    unit: ms\n  - quantity: latency L5b\n    value: 12.0\n    tolerance: 1.2\n    unit: ms\n  - quantity: latency L2/3\n    value: 13.8\n    tolerance: 1.38\n    unit: ms\n  - quantity: latency L6\n    value: 16.1\n    tolerance: 1.61\n    unit: ms\n  criterion: Impulse-responsive units are those whose mean rate 5 to 35 ms after impulse onset\n    exceeds the rate 0 to 10 ms before it by t test (Methods); open are (a) a paired t test across\n    trials, one-sided, (b) the same two-sided, both at 0.05, a standard level. Latency is the time\n    of the maximum in the 40-ms window after impulse onset of the 10-ms smoothed PSTH (Methods),\n    with impulses pooled as in fig4d-evoked-modulation-by-layer reading (i). The summary over units\n    is open; the readings are the mean and the median. Reproduced when all five values fall\n    within tolerance under one reading, and partially when only the ordering (L4, L5a, L5b below\n    L2/3 and L6) holds.\n- id: fig4d-gradual-decrease\n  statement: Superimposed on the phasic impulse responses, average firing rate decreased gradually\n    during the nose poke period in all layers except L5a.\n  source: Results, S1 Recordings during Behavioral Discrimination, paragraph 4; Figure 4D\n  quote: Superimposed on these phasic responses to individual impulses was a gradual decrease in\n    average firing rate during the nose poke period, observed in all layers except L5a ( Fig 4D ).\n  depends_on:\n  - temporal-modulation-count\n  criterion: Population PSTH of temporally modulated units by layer, 1-ms bins aligned to first\n    impulse onset, all sequences. The paper gives no measure of the decrease. The readings are (a)\n    the slope of a linear fit to the population PSTH from the start of the 25-ms baseline to 180\n    ms after onset is negative; (b) the mean rate in the last 30 ms of that span is below the mean\n    rate in the 25-ms baseline. Reproduced when one reading shows a decrease in L2/3, L4, L5b and\n    L6 and none in L5a.\n- id: fig6-regression-significant\n  statement: Of the 305 temporally modulated units, 204 had a significant regression of firing\n    rate on integrated panel speed for at least one of the 36 integration windows.\n  source: Results, Regression Analysis to Identify Fast- and Slow-Time Scale Units, paragraph 1;\n    Methods, Stimulus regression\n  quote: Two hundred four units showed a significant regression for at least one stimulus\n    integration window (α = 0.05/36 = 0.0014, using Bonferroni correction for the multiple\n    regressions).\n  depends_on:\n  - temporal-modulation-count\n  expected:\n    quantity: units with a significant regression\n    value: 204\n    tolerance: 20.4\n  criterion: Per the Methods and Results, firing rate in 5-ms bins from 0 to 180 ms after stimulus\n    onset, over all trials of each of the four sequences (36 bins times 4 sequences), is regressed\n    on panel speed integrated over the window ending at the start of that bin, for windows of 5\n    to 180 ms in 5-ms steps; one linear regression per window (\"a total of 36 regressions\"); a\n    unit is significant when any window has p < 0.05/36. Panel speed is the speed profile of each\n    sequence (S1 Fig, S2 Data, or the dataset's stimulus record). Integrated speed as a sum or a\n    mean over the window gives the same R2 and p, so the choice cannot change the outcome; the sum\n    is used. Speed is taken as the absolute value of panel velocity, as \"speed\" implies.\n- id: fig6e-unit-classes\n  statement: Units were classed by best-fit integration window as Fast (5 to 20 ms, 158 units, 52%,\n    positive slopes), Medium (25 to 55 ms, 52 units, largely negative slopes), Slow Positive (51)\n    and Slow Negative (44); 44% of units had very fast (5 to 10 ms) windows.\n  source: Results, Regression Analysis to Identify Fast- and Slow-Time Scale Units, paragraphs 2\n    and 3; Figure 6E; Discussion, Stimulus Encoding in S1, paragraph 1\n  quote: Empirically, units with 5–20 ms best integration windows (Fast units; n = 158) had positive\n    slopes. Units with 25–55 ms integration windows were rarer (Medium units; n = 52) and had\n    largely negative slopes. Units with slow (55–180 ms) integration windows had either positive\n    regression slope (Slow Positive units; n = 51) or negative regression slope (Slow Negative\n    units; n = 44).\n  depends_on:\n  - fig6-regression-significant\n  expected:\n  - quantity: Fast units\n    value: 158\n    tolerance: 15.8\n  - quantity: Medium units\n    value: 52\n    tolerance: 5.2\n  - quantity: Slow Positive units\n    value: 51\n    tolerance: 5.1\n  - quantity: Slow Negative units\n    value: 44\n    tolerance: 4.4\n  - quantity: percent of temporally modulated units that are Fast\n    value: 52\n    tolerance: 5.2\n    unit: percent\n  - quantity: percent of temporally modulated units with 5-10 ms best window\n    value: 44\n    tolerance: 4.4\n    unit: percent\n  criterion: Best window is the one with the highest R2 (Methods). Two details are open. Which\n    units are classed; the four counts sum to 305, all temporally modulated units, while the\n    Methods take the best window only for the 204 with a significant regression; the readings are\n    (a) all 305 units classed by their highest-R2 window, (b) only the 204. The 55-ms window is\n    Medium in the Results (\"25–55 ms\") and Slow in the Figure 6D legend (\"best integration window\n    <55 ms\" for Fast and Medium); the readings are (i) 55 ms Slow, (ii) 55 ms Medium. The slope sign\n    is that of the best window's regression. Reproduced when, under one combination, the counts\n    are within tolerance, most Fast units have positive slopes and most Medium units negative.\n- id: fig6fg-laminar-classes\n  statement: Fast units were 73% of temporally modulated units in L2/3 and L4, 50% in L5 and 23% in\n    L6; slow units were 13% in L2/3 and L4, 31% in L5 and 56% in L6.\n  source: Results, Regression Analysis to Identify Fast- and Slow-Time Scale Units, paragraph 3;\n    Figure 6F and 6G\n  quote: Fast units were 73% of temporally modulated units in L2/3 and L4, 50% in L5, and 23% in L6.\n    ... Overall, slow units were 13% of temporally responsive units in L2/3 and L4, 31% in L5 and\n    56% in L6.\n  depends_on:\n  - fig6e-unit-classes\n  expected:\n  - quantity: Fast percent, L2/3 and L4\n    value: 73\n    tolerance: 7.3\n    unit: percent\n  - quantity: Fast percent, L5\n    value: 50\n    tolerance: 5\n    unit: percent\n  - quantity: Fast percent, L6\n    value: 23\n    tolerance: 2.3\n    unit: percent\n  - quantity: Slow percent, L2/3 and L4\n    value: 13\n    tolerance: 1.3\n    unit: percent\n  - quantity: Slow percent, L5\n    value: 31\n    tolerance: 3.1\n    unit: percent\n  - quantity: Slow percent, L6\n    value: 56\n    tolerance: 5.6\n    unit: percent\n  criterion: Layers from depth with the Methods' boundaries, L5 being L5a and L5b together.\n    Denominator is the temporally modulated units in each layer group; slow units are Slow\n    Positive and Slow Negative together. Readings as in fig6e-unit-classes. A second reading of\n    the \"73% ... in L2/3 and L4\" is that each of L2/3 and L4 separately is about 73%; both are\n    shown. Reproduced when all six values fall within tolerance under one reading; partially when\n    the gradient (Fast falling and Slow rising from superficial to deep) holds but values fall\n    outside.\n- id: fig7c-fast-impulse-velocity\n  statement: In Fast units the evoked rate after an impulse was greater for F than S impulses and\n    intermediate for M impulses.\n  source: Results, Fast and Medium Time Scale Units, paragraph 2; Figure 7C left\n  quote: The firing rate of Fast units ( n = 158) in a brief window after each impulse was greater\n    for F versus S impulses, and intermediate for M impulses ( Fig 7C , left).\n  depends_on:\n  - fig6e-unit-classes\n  criterion: Per Fast unit and impulse type (all F, M or S impulses of all sequences), the net\n    evoked rate is the mean rate 5 to 35 ms after impulse onset minus the rate 0 to 10 ms before it\n    (Figure 7C legend, \"post-impulse rate–pre-impulse rate\", with the windows of the Methods).\n    Reproduced when the mean over Fast units orders F > M > S. The paper reports no test; a paired\n    t test of F against S across units is shown as a variant.\n- id: fig7c-fast-sequence-rate\n  statement: Mean firing rate of Fast units over the whole sequence (0 to 150 ms) followed the mean\n    speed of the sequence, highest for FFF, lowest for SSS, and intermediate and equal for FMS and\n    SMF.\n  source: Results, Fast and Medium Time Scale Units, paragraph 2; Figure 7C right\n  quote: Mean firing rate measured over the entire duration of a sequence (0–150 ms after sequence\n    onset) varied closely with mean speed of the sequence, being highest for FFF, lowest for SSS,\n    and intermediate and equal for FMS and SMF ( Fig 7C , right).\n  depends_on:\n  - fig6e-unit-classes\n  criterion: Per Fast unit and sequence, the mean rate 0 to 150 ms after onset above the\n    pre-stimulus baseline (Figure 7C legend); the baseline window is open, with readings (a) the\n    25 ms before onset (as in baseline-rates), (b) 0 to 10 ms before onset (the impulse baseline of\n    the Methods). Reproduced when the mean over units orders FFF > FMS and SMF > SSS and FMS and SMF\n    are equal, judged (no test is given) by a paired t test across units that is not significant\n    at 0.05, a standard choice that is named here as such.\n- id: fig7-fff-adaptation\n  statement: Fast RS single units adapted modestly in FFF trains, with pulse 2 to pulse 1 ratio 0.80\n    and pulse 3 to pulse 1 ratio 0.70, significant by t test.\n  source: Results, Fast and Medium Time Scale Units, paragraph 1; S4 Fig\n  quote: Adaptation within each train was quantified as mean firing rate to pulse N/pulse 1 and was\n    modest in FFF trains (2/1: 0.80 ± 0.11, 3/1: 0.70 ± 0.14, p < 0.05 by t test, n = 61 single RS\n    units with significant response to F impulses)\n  statistics:\n  - test: t test\n    p: 0.05\n    p_relation: \"<\"\n    n: 61 Fast RS single units with significant response to F impulses\n  depends_on:\n  - fig6e-unit-classes\n  expected:\n  - quantity: FFF pulse 2/pulse 1 ratio\n    value: 0.80\n    tolerance: 0.11\n  - quantity: FFF pulse 3/pulse 1 ratio\n    value: 0.70\n    tolerance: 0.14\n  criterion: Units are Fast RS single units with a significant response to F impulses (impulse\n    responsive by the Methods' t test); expected 61. Evoked rate is the rate 5 to 35 ms after\n    impulse onset above the pre-sequence baseline (S4 Fig legend); the baseline window is open as\n    in fig7c-fast-sequence-rate. The tolerance is the reported SEM. Open are (a) the mean of\n    per-unit ratios, (b) the ratio of the population means; and the test, (i) a one-sample t test\n    of per-unit ratios against 1, (ii) a paired t test of pulse N against pulse 1 rates. Reproduced\n    when both ratios are within tolerance and the test gives p < 0.05 under one combination.\n- id: fig7-sss-no-adaptation\n  statement: Adaptation was statistically absent in SSS trains (pulse 2/pulse 1 ratio 1.09, pulse\n    3/pulse 1 ratio 0.86).\n  source: Results, Fast and Medium Time Scale Units, paragraph 1; S4 Fig\n  quote: statistically absent in SSS trains (2/1: 1.09 ± 0.26, 3/1: 0.86 ± 0.35, all mean ± SEM)\n  depends_on:\n  - fig7-fff-adaptation\n  expected:\n  - quantity: SSS pulse 2/pulse 1 ratio\n    value: 1.09\n    tolerance: 0.26\n  - quantity: SSS pulse 3/pulse 1 ratio\n    value: 0.86\n    tolerance: 0.35\n  criterion: The same units, measures and readings as fig7-fff-adaptation. A claim of absence,\n    judged on the paper's t test at 0.05 (the readings of the test are those of\n    fig7-fff-adaptation, as the paper does not say which t test). Reproduced when neither ratio\n    differs significantly from 1 (or pulse N from pulse 1) and the ratios are within tolerance.\n- id: s4-fms-middle-pulse\n  statement: The middle M pulse appeared weaker in FMS than in SMF sequences in Fast RS single\n    units, but the difference was not significant.\n  source: Results, Fast and Medium Time Scale Units, paragraph 3; S4A Fig\n  quote: the middle M pulse in FMS sequences appeared weaker than in SMF sequences, though this did\n    not achieve statistical significance ( p = 0.08, paired t test, n = 61 units)\n  statistics:\n  - test: paired t test\n    p: 0.08\n    n: 61 Fast RS single units\n  depends_on:\n  - fig7-fff-adaptation\n  criterion: The same 61 units; evoked rate to pulse 2 (5 to 35 ms after its onset, above\n    pre-sequence baseline, S4 Fig legend) in FMS against SMF. A claim of absence judged on the\n    paper's paired t test at 0.05. Reproduced when the mean FMS response is lower and p >= 0.05;\n    the size of the difference is reported.\n- id: fig7de-medium-suppressed\n  statement: Medium units were suppressed by F, M and S impulses and did not distinguish impulse\n    identity or sequence identity.\n  source: Results, Fast and Medium Time Scale Units, paragraph 4; Figure 7D and 7E\n  quote: In firing rate analysis, these cells were inhibited by F, M, and S impulses and did not\n    distinguish either individual impulse identity or whole sequence identity ( Fig 7D and 7E ).\n  depends_on:\n  - fig6e-unit-classes\n  criterion: Net evoked rates as in fig7c-fast-impulse-velocity and mean sequence rates as in\n    fig7c-fast-sequence-rate, for Medium units. Suppression holds when the mean net evoked rate is\n    negative for each of F, M and S. The paper reports no test for the absence of a difference;\n    the standard choice named here is paired t tests across units, F against S impulses and FFF\n    against SSS sequences, at 0.05. Reproduced when all three means are negative and neither test\n    is significant.\n- id: fig8a-slow-positive-no-sequence-difference\n  statement: Slow Positive units showed small, sustained responses mostly to the second and third\n    impulses, evident for F and M but not S impulses, and their mean firing did not differ between\n    FFF, FMS, SMF and SSS.\n  source: Results, Slow Positive and Slow Negative Units, paragraph 1; Figure 8A\n  quote: Responses were small and sustained (unlike the large, transient responses by Fast units)\n    and were evident for F and M impulses but not S impulses ( Fig 8A ). However, mean firing was\n    not different for FFF, FMS, SMF, or SSS trains\n  depends_on:\n  - fig6e-unit-classes\n  criterion: Slow Positive units, all layers. Net evoked rates per impulse type as in\n    fig7c-fast-impulse-velocity, and mean rate 0 to 150 ms after onset per sequence as in\n    fig7c-fast-sequence-rate. F and M responses hold when their mean net evoked rate is positive\n    and the S response when it is near zero; no test is given, and the standard choice named here\n    is a one-sample t test against 0 at 0.05 (F and M significant, S not). For the sequences, the\n    paper reports no test; the standard choice is a one-way repeated-measures ANOVA across units\n    on the four sequence rates at 0.05, not significant. Reproduced when both parts hold.\n- id: fig8b-slow-negative-no-impulse-response\n  statement: Slow Negative units did not respond to impulses, and their firing declined steadily\n    over time.\n  source: Results, Slow Positive and Slow Negative Units, paragraph 1; Figure 8B\n  quote: Slow negative units did not respond to impulses at all, and firing rate steadily declined\n    over time, not locked to panel impulses ( Fig 8B ).\n  depends_on:\n  - fig6e-unit-classes\n  criterion: Slow Negative units. No impulse response holds when the mean net evoked rate (as in\n    fig7c-fast-impulse-velocity) is not positive for F, M or S impulses (one-sample t test against\n    0 at 0.05, a standard choice). The decline holds when the population PSTH slope over 0 to 180\n    ms after onset is negative (linear fit, a standard choice). Reproduced when both hold.\n- id: fig8d-slow-positive-right-choice-l5\n  statement: Slow Positive units fired more on right-choice trials (contralateral to the recording)\n    for all stimuli; right-choice bias, measured 5 to 50 ms after the start of the final impulse,\n    was significant in L5a and L5b but not in other layers.\n  source: Results, Slow Positive and Slow Negative Units, paragraph 2; Figure 8C and 8D\n  quote: Slow Positive units fired more on trials when the rat chose right (contralateral to the S1\n    recording). ... We quantified right-choice bias as the firing rate difference on right versus\n    left trials, measured 5–50 ms after the start of the final impulse. Right-choice bias was\n    significant for Slow Positive units in L5a and L5b, but not other layers ( Fig 8D ).\n  statistics:\n  - about: right against left choice rate, one of the significant groups of Figure 8D (the text\n      does not say which)\n    test: paired t test\n    p: 0.022\n  - about: right against left choice rate, one of the significant groups of Figure 8D (the text\n      does not say which)\n    test: paired t test\n    p: 9.5e-4\n  - about: right against left choice rate, one of the significant groups of Figure 8D (the text\n      does not say which)\n    test: paired t test\n    p: 7.5e-5\n  depends_on:\n  - fig6e-unit-classes\n  criterion: Per Slow Positive unit, the mean rate 5 to 50 ms after onset of the third impulse on\n    right-choice and on left-choice trials; per layer, a paired t test across units at 0.05\n    (Figure 8D legend). Which trials enter is open; the readings are (a) all trials with a choice,\n    pooled over the four sequences, (b) the difference computed within each sequence and averaged.\n    Reproduced when L5a and L5b are significant with right higher and L2/3, L4 and L6 are not,\n    under one reading. The three printed p-values cannot be matched to layers from the text (no\n    figure was read); they are reported beside the values found.\n- id: fig8d-fast-medium-no-choice-bias\n  statement: Fast and Medium units showed no right-choice bias, and choice-related activity was\n    absent in L4 Fast units.\n  source: Results, Slow Positive and Slow Negative Units, paragraph 2; Figure 8D right and 8E\n    bottom\n  quote: Choice-related activity was absent in fast time scale units in L4 ( Fig 8E ).\n  depends_on:\n  - fig6e-unit-classes\n  criterion: A claim of absence, judged on the paper's tests. For Fast and Medium units by layer,\n    the paired t test of fig8d-slow-positive-right-choice-l5 at 0.05; for L4 Fast units, the\n    sliding paired t test of fig8e-choice-divergence-125ms. Reproduced when the L4 Fast units show\n    no significant bias by either test; the other layers are reported. Effect sizes are given\n    either way.\n- id: fig8e-choice-divergence-125ms\n  statement: In L5 Slow Positive units, firing on right- and left-choice trials diverged after the\n    second impulse and was consistently significant by 125 ms, before the earliest withdrawals (150\n    ms) and the mean withdrawal time (190 ms).\n  source: Results, Slow Positive and Slow Negative Units, paragraph 2; Figure 8E\n  quote: Firing rate began to diverge on right versus left choice trials after the second impulse\n    and was consistently significant by 125 ms, which is during the third impulse ( p < 0.05,\n    sliding paired t test) ( Fig 8E ). This preceded the earliest withdrawals (150 ms) and mean\n    withdrawal time (190 ms).\n  statistics:\n  - test: sliding paired t test\n    p: 0.05\n    p_relation: \"<\"\n  depends_on:\n  - fig8d-slow-positive-right-choice-l5\n  expected:\n  - quantity: time from which right and left differ consistently\n    value: 125\n    tolerance: 12.5\n    unit: ms\n  - quantity: earliest nose poke withdrawal after stimulus onset\n    value: 150\n    tolerance: 15\n    unit: ms\n  - quantity: mean nose poke withdrawal after stimulus onset\n    value: 190\n    tolerance: 19\n    unit: ms\n  criterion: L5 (L5a and L5b) Slow Positive units; per unit the PSTH averaged over the four\n    sequences for right- and left-choice trials; at each time a paired t test across units at\n    0.05. The sliding window is not given; the readings are (a) 10-ms windows (the smoothing of the\n    Methods) stepped by 1 ms, (b) 5-ms bins (the regression bins). \"Consistently significant by\"\n    is read as the start of the first run of significant times that lasts to the end of the third\n    impulse. Withdrawal times are taken from stimulus onset over the same trials; \"earliest\" is\n    read as (i) the minimum, (ii) the 1st percentile. Reproduced when all three values fall within\n    tolerance under one reading.\n- id: s5-slow-positive-no-integration\n  statement: Within right- or left-choice trials, L5 Slow Positive units fired little to pulses 1 and\n    2, and their pulse 3 firing was the same for FFF, FMS, SMF and SSS and did not correlate with\n    mean speed of the sequence or of the last two impulses.\n  source: Results, Slow Positive and Slow Negative Units, paragraph 3; S5 Fig\n  quote: Pulse 3 firing rate was higher but was essentially identical for FFF, FMS, SMF, and SSS\n    sequences and did not correlate with mean speed of the entire sequence or of the last two\n    impulses.\n  depends_on:\n  - fig8d-slow-positive-right-choice-l5\n  criterion: L5a and L5b Slow Positive units; evoked rate per impulse as in S4 Fig (5 to 35 ms after\n    onset, above pre-sequence baseline), separately for right- and left-choice trials. The paper\n    reports no test. The standard choices named here are a one-way repeated-measures ANOVA across\n    units on pulse 3 rates over the four sequences at 0.05, and a Pearson correlation of the four\n    population pulse 3 rates with sequence mean speed and with the mean speed of pulses 2 and 3\n    (from the S1 Fig speed profiles). Reproduced when, in both choice groups, the ANOVA is not\n    significant and neither correlation is significant at 0.05.\n- id: s6-head-position-choice\n  statement: In high-speed video of 43 trials, head angle and whisker tip trajectories did not differ\n    between right- and left-choice trials, while head position differed modestly from 100 ms, by\n    0.6 mm at 125 ms.\n  source: Results, Slow Positive and Slow Negative Units, paragraph 4; S6 Fig\n  quote: Head angle and whisker tip trajectories were invariant between right- and left-choice\n    trials. Head position differed modestly between right- and left-choice trials beginning at 100\n    ms, with a 0.6 mm difference at 125 ms ( S6 Fig ).\n  data: elsewhere\n  where: PLOS Biology supporting information of doi:10.1371/journal.pbio.1002549, S2 Data (XLSX,\n    data for S6 Fig)\n  expected:\n    quantity: right-left head position difference at 125 ms\n    value: 0.6\n    tolerance: 0.06\n    unit: mm\n  criterion: Tracked positions from the video data (S2 Data), 22 left- and 21 right-choice trials.\n    The test behind \"significant\" in the S6 Fig legend is not named; the readings are an unpaired\n    t test at each frame at 0.05, and the same with Welch's correction. Reproduced when head x\n    position differs from about 100 ms with a difference near 0.6 mm at 125 ms, and head angle and\n    whisker tip do not differ at any frame.\n- id: s7-no-fs-l5-slow-positive\n  statement: All response classes included RS units; few FS units were in the Slow classes and none\n    among L5 Slow Positive units.\n  source: Results, RS and FS Single Units, paragraph 1; S7 Fig\n  quote: Among L5 Slow Positive units, both RS units and multi-unit clusters had similar\n    choice-related firing, and no FS units existed in this category ( S7 Fig ).\n  depends_on:\n  - fig6e-unit-classes\n  criterion: FS and RS by the 0.375 ms width threshold (Methods), as labelled in the data.\n    Reproduced when every class holds RS units and L5 Slow Positive units hold no FS single unit.\n- id: fig9b-stimulus-decoder-fast-medium\n  statement: A decoder built from all Fast and Medium units with 10-ms bins identified the sequence\n    with 83% accuracy (74% for FMS to 88% for FFF; chance 25%), and identified FMS and SMF with 78%\n    accuracy.\n  source: Results, Neural Decoding of Stimulus Identity and Behavioral Choice, paragraph 2; Figure\n    9B\n  quote: This model predicted sequence identity, using one single-trial spike train per model unit,\n    with 83% overall accuracy (range: 74% for FMS to 88% for FFF spike trains). ... Remarkably, this\n    model identified SMF and FMS sequences with 78% accuracy, even though rats could not.\n  depends_on:\n  - fig6e-unit-classes\n  expected:\n  - quantity: overall accuracy\n    value: 83\n    tolerance: 8.3\n    unit: percent\n  - quantity: accuracy for FMS\n    value: 74\n    tolerance: 7.4\n    unit: percent\n  - quantity: accuracy for FFF\n    value: 88\n    tolerance: 8.8\n    unit: percent\n  - quantity: accuracy for FMS and SMF\n    value: 78\n    tolerance: 7.8\n    unit: percent\n  criterion: Per the Methods (Neural Decoders) each unit has four logistic functions (one per\n    stimulus, one against all) on spike counts in 10-ms bins 0 to 150 ms after onset; 70% of each\n    unit's trials fit, the rest test; each unit's outputs normalised to equal weight; population\n    prediction the stimulus of highest summed probability, the test trial for each unit drawn at\n    random from its test trials of that stimulus (units recorded in different sessions combined\n    as independent); 300 repeats, mean performance. Open, with readings. The logistic regression\n    penalty and the use of \"k-fold cross-validation\": (a) scikit-learn LogisticRegression defaults\n    (L2, C = 1); (b) LogisticRegressionCV choosing C by 5-fold cross-validation on the 70%. Output\n    normalisation: (i) each unit's four probabilities divided by their sum; (ii) unnormalised. The\n    number of pseudo-trials per stimulus per repeat is not given, and is a standard choice (100)\n    that changes only the precision. All trials enter, correct and incorrect, as the text does not\n    restrict them. \"SMF and FMS with 78%\" is read as the mean of their two diagonal entries.\n    Reproduced when all values fall within tolerance under one combination.\n- id: fig9c-best-units-short-windows\n  statement: The individual units with the best stimulus prediction in the Fast/Medium decoder were\n    those with 5 to 10 ms best integration windows.\n  source: Results, Neural Decoding of Stimulus Identity and Behavioral Choice, paragraph 2; Figure\n    9C\n  quote: The individual neurons with best stimulus prediction were those with 5–10 ms best\n    integration windows ( Fig 9C ).\n  depends_on:\n  - fig9b-stimulus-decoder-fast-medium\n  criterion: Per unit, percent correct of its own classifier (10-ms bins) on its test trials,\n    averaged over repeats, grouped by best integration window (Figure 9C). Reproduced when the\n    mean percent correct is highest in the 5-ms or 10-ms group and the top-ranked units are mostly\n    from those groups (more than half of the top 10%, a standard choice).\n- id: fig9b-stimulus-decoder-slow-chance\n  statement: A decoder built from all Slow units with 10-ms bins predicted sequence identity near\n    chance (32%, not different from chance).\n  source: Results, Neural Decoding of Stimulus Identity and Behavioral Choice, paragraph 2; Figure\n    9B\n  quote: A second decoder constructed of all Slow units, also using 10 ms bins, predicted sequence\n    identity at near chance levels (32% correct, not significantly different from chance, p = 0.47)\n  statistics:\n  - about: Slow decoder accuracy against chance (25%)\n    p: 0.47\n  depends_on:\n  - fig9b-stimulus-decoder-fast-medium\n  expected:\n    quantity: Slow decoder overall accuracy\n    value: 32\n    tolerance: 3.2\n    unit: percent\n  criterion: Slow Positive and Slow Negative units, the decoder of fig9b-stimulus-decoder-fast-medium\n    with its readings. A claim of absence; the paper does not name its test against chance. The\n    readings are (a) the fraction of the 300 repeats at or below 25%, two-sided; (b) a binomial\n    test of the pooled test predictions against 0.25. Reproduced when accuracy is within tolerance\n    and the test is not significant at 0.05 under one reading.\n- id: fig9d-single-bin-decoder\n  statement: Decoding from mean firing rate in a single 150-ms bin reduced Fast/Medium decoder\n    accuracy to 43% and did not improve Slow decoder accuracy.\n  source: Results, Neural Decoding of Stimulus Identity and Behavioral Choice, paragraph 2; Figure\n    9D\n  quote: Decoding from mean firing rate in a single 150-ms bin substantially reduced Fast/Medium\n    decoder accuracy (43% correct) and did not improve Slow decoder accuracy ( Fig 9D ).\n  depends_on:\n  - fig9b-stimulus-decoder-slow-chance\n  expected:\n    quantity: Fast/Medium decoder accuracy, single 150-ms bin\n    value: 43\n    tolerance: 4.3\n    unit: percent\n  criterion: As fig9b-stimulus-decoder-fast-medium with one bin of 0 to 150 ms, with the same\n    readings. Reproduced when the Fast/Medium accuracy is within tolerance and the Slow single-bin\n    accuracy is not above its 10-ms accuracy by more than the 3.2-point tolerance of that value.\n- id: fig9e-temporal-pattern-decoding\n  statement: Fast/Medium decoders trained on rate-normalized spike trains performed well (80%),\n    while time-scrambling spikes within trials abolished performance.\n  source: Results, Neural Decoding of Stimulus Identity and Behavioral Choice, paragraph 3; Figure\n    9E\n  quote: Fast/Medium decoders trained on rate-normalized data performed well (80% correct), but\n    time-scrambling spikes abolished performance ( Fig 9E ).\n  depends_on:\n  - fig9b-stimulus-decoder-fast-medium\n  expected:\n    quantity: Fast/Medium accuracy, rate-normalized\n    value: 80\n    tolerance: 8\n    unit: percent\n  criterion: As fig9b-stimulus-decoder-fast-medium with 10-ms bins. Rate-normalized trains are each\n    trial's 15-bin count vector divided by its Euclidean norm (Methods; the text prints\n    \"-Euclidean norm\", read as the L2 norm); trials with no spikes stay zero. Time-scrambled trains\n    have spike times shuffled within the 0 to 150 ms window of each trial (Methods). \"Abolished\"\n    has no number; the readings are (a) not above chance by the tests of\n    fig9b-stimulus-decoder-slow-chance; (b) below 32%, the Slow decoder's near-chance value.\n    Reproduced when the rate-normalized accuracy is within tolerance and the scrambled accuracy\n    meets one reading.\n- id: fig9f-choice-decoder\n  statement: A choice decoder from Slow units predicted drink port choice at 65% (chance 50%) from a\n    single 150-ms bin or from the last 100 ms before nose poke withdrawal, while one from Fast and\n    Medium units could not predict choice.\n  source: Results, Neural Decoding of Stimulus Identity and Behavioral Choice, paragraph 4; Figure\n    9F\n  quote: A choice decoder based on Fast/Medium units was unable to predict drink port choice ...\n    A choice decoder based on Slow units successfully predicted drink port choice using a single\n    150-ms bin, or mean firing rate in the last 100 ms before nose poke withdrawal (65% correct for\n    both models) ( Fig 9F ).\n  depends_on:\n  - fig6e-unit-classes\n  expected:\n  - quantity: Slow choice decoder accuracy, single 150-ms bin\n    value: 65\n    tolerance: 6.5\n    unit: percent\n  - quantity: Slow choice decoder accuracy, last 100 ms before withdrawal\n    value: 65\n    tolerance: 6.5\n    unit: percent\n  criterion: Per the Methods, one logistic function per unit, fit on trials of all four stimuli, and\n    tested separately within FFF, FMS, SMF and SSS trials; population choice the one of highest\n    summed probability, test trials drawn per unit from trials of the chosen stimulus and the\n    true choice; fitting and repeats as in fig9b-stimulus-decoder-fast-medium, with its readings.\n    Open is how the four per-stimulus accuracies are summarised; the readings are (a) their mean,\n    (b) the accuracy over all test trials pooled. Also open is how test trials of each choice are\n    drawn; the readings are (i) equal numbers of right and left (so chance is 50%, as the legend\n    says), (ii) in proportion to the data. Fast/Medium is \"unable\" when its accuracy is within the\n    10% tolerance of 50% (45 to 55%) under one reading. Reproduced when the Slow values are within\n    tolerance and Fast/Medium is unable, for both windows.\n- id: fig9g-l5b-slow-positive-best-choice\n  statement: The units with the best choice prediction were Slow Positive units located primarily in\n    L5b.\n  source: Results, Neural Decoding of Stimulus Identity and Behavioral Choice, paragraph 4; Figure\n    9G\n  quote: Post-hoc analysis showed that units with best choice prediction were Slow Positive units\n    located primarily in L5b ( Fig 9G ).\n  depends_on:\n  - fig9f-choice-decoder\n  criterion: Per Slow unit, percent correct of its own choice classifier on a single 100-ms bin\n    before withdrawal (Figure 9G legend), grouped by layer and Slow Positive or Negative.\n    Reproduced when the group with the highest mean is L5b Slow Positive, or (a second reading of\n    \"primarily\") when more than half of the top 10% of units (a standard choice) are L5b Slow\n    Positive units.\n"
}
```

```
File created successfully at: claims/mcguire-2016.yaml (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd  python tools/claims_check.py claims/mcguire-2016.yaml paper/10.1371-journal.pbio.1002549.txt; grep -n -- "—\|rather" claims/mcguire-2016.yaml
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  grep -n ": .*: \|^    .*: " claims/mcguire-2016.yaml | grep -v "^[0-9]*:#"
```

```
59:    test: proportion test
60:    p: 0.00625
61:    p_relation: ">"
62:    corrected: Bonferroni
63:    n: seven rats
65:    test: proportion test
66:    p: 0.0039
67:    n: one rat
83:  quote: After 14.2 ± 4.4 (standard deviation [s.d.]) (range: 8–22) d of training on
87:    value: 14.2
88:    tolerance: 4.4
89:    unit: days
91:    value: 8
92:    tolerance: 0.8
93:    unit: days
95:    value: 22
96:    tolerance: 2.2
97:    unit: days
124:    test: two-sided paired t test
125:    p: 0.012
[... 191 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python3 - <<'EOF'
import re
p='claims/mcguire-2016.yaml'
s=open(p).read()
lines=s.split('\n')
out=[];i=0
starts=[83,154,196,515,543,750]
# find quote blocks containing ': ' and single-quote them
res=[]
i=0
while i<len(lines):
    l=lines[i]
    if l.startswith('  quote: ') and not l.startswith("  quote: '"):
        j=i+1
        while j<len(lines) and lines[j].startswith('    ') and not re.match(r'^    \S+:( |$)',lines[j]) :
            j+=1
        block=lines[i:j]
        text=' '.join([block[0][9:]]+[b[4:] for b in block[1:]])
        if ': ' in text or ' #' in text:
            assert "'" not in text, text
            block[0]="  quote: '"+block[0][9:]
            block[-1]=block[-1]+"'"
        res.extend(block); i=j; continue
    res.append(l); i+=1
s='\n'.join(res)
s=s.replace("Open details, with readings.\n    Maximum or minimum: (a)","Open details, with readings.\n    For maximum or minimum, (a)")
s=s.replace("value. Pooling: (i)","value. For pooling, (i)")
s=s.replace('penalty and the use of "k-fold cross-validation": (a)','penalty and the use of "k-fold cross-validation" allow (a)')
s=s.replace("normalisation: (i) each","normalisation may be (i) each")
open(p,'w').write(s)
EOF
grep -n "Output$\|Output normalisation" claims/mcguire-2016.yaml; python tools/claims_check.py claims/mcguire-2016.yaml paper/10.1371-journal.pbio.1002549.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  python3 - <<'EOF'
import re
p='claims/mcguire-2016.yaml'
lines=open(p).read().split('\n')
res=[];i=0
while i<len(lines):
    l=lines[i]
    if l.startswith('  quote: ') and not l.startswith("  quote: '"):
        j=i+1
        while j<len(lines) and lines[j].startswith('    ') and not re.match(r'^    [a-z_]+:( |$)',lines[j]):
            j+=1
        block=lines[i:j]
        text=' '.join([block[0][9:]]+[b[4:] for b in block[1:]])
        if ': ' in text:
            assert "'" not in text, text
            block[0]="  quote: '"+block[0][9:]; block[-1]+="'"
        res.extend(block); i=j; continue
    res.append(l); i+=1
open(p,'w').write('\n'.join(res))
EOF
python tools/claims_check.py claims/mcguire-2016.yaml paper/10.1371-journal.pbio.1002549.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  grep -n "quote: '" claims/mcguire-2016.yaml; grep -c -- "—" claims/mcguire-2016.yaml; grep -n -i "rather" claims/mcguire-2016.yaml; python3 -c "
import yaml;d=yaml.safe_load(open('claims/mcguire-2016.yaml'))
print(sum('statistics' in c for c in d['claims']), sum('criterion' in c for c in d['claims']), sum('expected' in c for c in d['claims']))"
```

```
83:  quote: 'After 14.2 ± 4.4 (standard deviation [s.d.]) (range: 8–22) d of training on
137:  quote: 'Task performance was relatively low (d-prime for FFF versus SSS: 0.5–1.5), as in a prior
155:  quote: 'Both rats consistently discriminated FSFS from SFFS when they had different mean speed
196:  quote: 'Spike sorting yielded 3.8 (range: 0–11) well-separated single units per recording session
515:  quote: 'Adaptation within each train was quantified as mean firing rate to pulse N/pulse 1 and was
543:  quote: 'statistically absent in SSS trains (2/1: 1.09 ± 0.26, 3/1: 0.86 ± 0.35, all mean ± SEM)'
750:  quote: 'This model predicted sequence identity, using one single-trial spike train per model unit,
0
7 37 20
```

**Agent**

I've written `claims/mcguire-2016.yaml`. The quote checker reports 37 claims, 37 quotes, 10 statistical values and 0 problems. I made no commit.

**Text read.** The version of record, open access (PMC5004814, Europe PMC JATS full text). It includes the main text, the Methods, and the legends of S1 to S7 Figs, S1 Table and S1/S2 Data. No PDF was supplied. The paper links no code: its Methods name Matlab for the regression and Python with scikit-learn for the decoders, but publish neither.

**Claims.** 37 findings, every one with a quote and none inferred. 7 claims carry statistics (10 values), 37 have a criterion and 20 have expected values. They cover:
- **Behaviour:** Figure 2, S2 Fig, and the d-prime range of 0.5 to 1.5.
- **FSFS/SFFS task (Figure 3):** `data: elsewhere`, from S1 Data, because those rats were not recorded.
- **Recordings:** unit counts, baseline rates, temporal modulation, evoked modulation and latency by layer.
- **Regression:** the 204 significant units, the four unit classes, and their laminar fractions.
- **Fast and Medium units:** coding and adaptation (Figure 7, S4 Fig).
- **Slow units:** choice coding (Figure 8, S5 Fig), plus S6 head movement (`data: elsewhere`, from S2 Data) and S7 unit types.
- **Decoders:** Figure 9B to 9G.

**Details the paper leaves open, with the readings named:**
- **Temporal modulation window:** the Methods say 0 to 180 ms after nose poke entry, but also call it the stimulus period, and the stimulus starts 75 to 100 ms after entry. Readings: after entry, or after stimulus onset.
- **Permutation statistic:** not named. Readings: PSTH variance across bins, or summed squared deviation from the permuted PSTH.
- **Which units are classed:** the class counts sum to 305 (all modulated units), but only 204 had a significant regression. Readings: classify all 305, or only the 204.
- **The 55 ms window:** Medium in the Results, Slow in the Figure 6D legend. Both readings are named.
- **Evoked modulation:** signed or absolute extreme; impulses pooled, or one value per impulse and sequence.
- **Impulse-responsive t test:** one-sided or two-sided.
- **Latency summary:** mean or median across units.
- **Pre-sequence baseline window:** the 25 ms before onset, or 0 to 10 ms before.
- **Adaptation ratio:** mean of per-unit ratios, or ratio of population means. Test: one-sample t test against 1, or paired t test of pulse N against pulse 1.
- **Proportion test for FMS against SMF:** with or without continuity correction; and which trials count.
- **"Strongly related" (Figure 2C):** ordering by mean speed, or a Pearson r above 0.8.
- **Gradual firing decrease:** the slope of a linear fit, or the end of the period against baseline.
- **Sliding t-test window:** 10 ms in 1 ms steps, or 5 ms bins; "earliest withdrawal" as the minimum or the 1st percentile.
- **Decoder:**
  - Regularisation: scikit-learn defaults, or C chosen by 5-fold cross-validation.
  - Output normalisation: probabilities divided by their sum, or none.
  - Test against chance (Slow decoder, p = 0.47): fraction of repeats at or below 25%, or a binomial test.
  - "Abolished" (time-scrambled): not above chance, or below 32%.
  - Choice-decoder summary: mean of the four stimulus accuracies, or all trials pooled; test trials of each choice drawn balanced or in proportion.
  - "Primarily L5b" (Figure 9G): highest group mean, or majority of the top 10% of units.
- **Absence claims with no test in the paper** (Medium units, Slow Positive across sequences, S5 Fig): each uses a standard test (paired t test or repeated-measures ANOVA at 0.05), and each criterion says that choice is not the paper's.

**Missing from what was supplied:**
- **No PDF:** Figure 8D's three p-values (0.022, 9.5e-4, 7.5e-5) cannot be matched to layers from the text. They are recorded without that assignment.
- **Garbled Table 1:** its sequence columns don't line up with their headers. I read them as interpulse interval, duration, mean speed and rewarded port, and the opening comment says so.
- **Not in the text:** the contents of S1 Table and of S1/S2 Data. No claim rests on them alone, except the two `data: elsewhere` claims, which take their data from S1 Data and S2 Data.
- **Typo in the paper:** the Methods' "-Euclidean norm" is read as the L2 norm.

## End of run

18 turns, 5 minutes, $1.68 at API prices, result: success.
