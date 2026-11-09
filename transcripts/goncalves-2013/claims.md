# crcns-ssc-8 · claims · run 42460454788

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  grep -n "^#" docs/protocol.md | head -50; ls paper/ claims/001453/ claims/crcns-ssc-8 2>&1
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  sed -n 1,184p docs/protocol.md
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
[... 163 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat claims/001453/*.yaml | head -200; wc -l paper/*.txt claims/001453/*.yaml
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  sed -n 200,321p claims/001453/*.yaml
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
[... 102 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat paper/10.1038-nn.3415.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  cat paper/ssc-8.data-description.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1038-nn.3415.txt"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  ls claims | head -50; grep -l "archive: crcns" -r claims | head -3; grep -n "archive" docs/archives.md | head -20
```

```
000003
000004
000005
000006
000008
000009
000010
000011
000013
000015
000016
000017
000019
000023
000034
000035
000036
000037
000041
000044
[... 51 more lines not kept]
```

**Agent calls Bash**

```bash
cd  head -60 claims/crcns-pfc-2/*.yaml; grep -n "checks\|status\|ready" claims/crcns-pfc-2/*.yaml | head
```

```
# Claims for Fujisawa, Amarasingham, Harrison & Buzsaki (2008), Nature Neuroscience 11:823-833,
# on CRCNS data set pfc-2 (doi:10.6080/K01V5BWK).
# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"), 2026-11-07,
# protocol as stated in docs/protocol.md (Reader).
#
# Text read: the version of record (PDF supplied by a person, text by PyMuPDF), main text, figure
# legends and Methods, with its supplement (Supplementary Note, legends of Supplementary Figures
# 1 to 16, references). The PDF pages could not be rendered in this run, so numbers and
# significance marks printed only inside figure panels (Figure 2b, 2d, 2e, 3e, 3f, 7b, the
# supplementary panels) are not recorded; the claims rest on the text and legends. Figure 2d
# (mean firing rates, t-test marks) and Figure 2e (fraction of maze length discriminated) have
# no claim for that reason: what the marks compare is shown only in the panels. The paper links
# no analysis code; the only link is to the KlustaKwik spike sorter. None was read.
#
# Data the paper used. Four adult male rats (3 to 5 months old) trained on an odor-based delayed
# matching-to-sample task on a figure-eight T-maze: a nose-poke in the start box gives a cheese or
# chocolate odor, which signals the reward in the right or left goal arm (the pairing varied
# across rats). Mean correct performance in recording sessions 91.9%. One 8-shank, 64-site silicon
# probe per rat (200 um shank separation, 8 staggered sites per shank) in anterior cingulate (area
# 24) and dorsal prelimbic (area 32) cortex; three rats in layer 2/3, one in layer 5. Wideband
[... 43 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 60,140p claims/crcns-pfc-2/*.yaml; sed -n 1,60p tools/claims_check.py
```

```
# - Position of excess coincidences. Coincident events are spike pairs with 1 <= tdiff <= 4 ms,
#   placed at the position where they occur, smoothed with the same 0.05 kernel and divided by
#   the number of trials; surrogates by jittering on [-5, +5] ms (1,000, as for the CCG, since this
#   section gives no number); pointwise and global one-sided bands for excess; global level
#   P < 0.01 (Figure 4 and 5 panels, text "P < 0.01").
schema_version: 2
dataset:
  archive: crcns
  id: pfc-2
  doi: 10.6080/K01V5BWK
paper: doi:10.1038/nn.2134
claims:
- id: unit-count
  statement: A total of 633 well-isolated units were recorded from anterior cingulate and dorsal
    prelimbic cortex in four rats.
  source: Results, paragraph 1
  quote: We recorded a total of 633 well-isolated units from the anterior cingulate area (area 24)
    and dorsal prelimbic area (area 32) of the medial prefrontal cortex (mPFC)
  expected:
    quantity: well-isolated mPFC units, all rats and sessions
[... 121 more lines not kept]
```

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
[... 185 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python -c "
import json;s=json.load(open('schemas/claims.schema.json'));print(json.dumps(s['\$defs'],indent=1))"
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

**Agent calls Write**

```json
{
 "file_path": "claims/crcns-ssc-8/10.1038-nn.3415.yaml",
 "content": "# Claims for Goncalves, Anstey, Golshani & Portera-Cailliau (2013), Nature Neuroscience 16:903-909,\n# on CRCNS data set ssc-8 (doi:10.6080/K0X63K3X).\n# Written by an agent (model \"claude-opus-5-5\", Claude Code, runner \"GitHub Actions\"), 2026-11-08,\n# protocol as stated in docs/protocol.md (Reader, version pilot-13).\n#\n# Text read: the version of record, PMC3695061 (open access), Europe PMC full-text XML flattened\n# to text: abstract, Introduction, Results, Discussion and Online Methods. The text holds no\n# figure legends and no supplement (Supplementary Figures 1 to 4 are cited but not supplied), and\n# no PDF was supplied. Every claim below rests on numbers printed in the Results text; details\n# that the legends or the supplement may have given (the correlation measure of Fig. 1, how\n# Fig. 1d was binned, the panels of Suppl. Figs. 1 to 4) are treated as open. The paper links no\n# analysis code. It names outside software only (ScanImage, the iPeak package, Chronux); none\n# was read, and none of it settles a detail used here.\n#\n# Data the paper used. Male and female C57Bl/6 wild-type (WT) and Fmr1 -/- (KO) mice, P9 to P40,\n# head-fixed and unanesthetized unless stated. Layer 2/3 barrel cortex, right hemisphere, bulk\n# loaded with Oregon Green BAPTA-1 AM; two-photon imaging at 3.9 Hz (512 x 128 pixels), or\n# 15.6 Hz in one control experiment. Several 3-min movies concatenated per mouse; contours of\n# cells drawn on the mean image, astrocytes (sulforhodamine-101) excluded; dF/F per cell, low-pass\n# filtered and deconvolved; firing rates extrapolated from the deconvolved traces. Ages P9-11,\n# P14-16 and P30-40; mice per group 12, 9 and 8 WT, 9, 10 and 8 KO (Fig. 1e). Other experiments,\n# not in the CRCNS description: whole-cell current-clamp recordings of L2/3 neurons at P14-16\n# (7 WT and 12 KO mice; Up/Down state and fast oscillatory activity segments), EEG recorded with\n# calcium imaging in a subset of mice (3-min recordings; L/H power, 0.5-4 Hz over 20-60 Hz), and\n# imaging under isoflurane at P14-16. The CRCNS description of ssc-8 lists, for the two\n# genotypes and three age groups, raw TIFF movies of unanesthetized mice at 3.9 Hz (one per\n# animal, 6 to 13 animals per group, 40 to 149 neurons, about 7 to 8 min each), the estimated\n# firing rates of each neuron (frames by neurons) and the cell-to-cell distances in microns. It\n# names no EEG, whole-cell or isoflurane data.\n#\n# Shared method, from the Online Methods and Results unless stated.\n# - Traces. The Methods compute firing rates and \"pair-wise continuous-trace cross-correlations\"\n#   from the deconvolved dF/F traces, citing their earlier study (ref. 15) for the detail. Which\n#   trace enters the correlation is open: reading T-a, the deconvolved traces (the data set's\n#   estimated firing rates); reading T-b, the low-pass filtered dF/F traces, which would need the\n#   cells to be segmented anew from the raw movies, as no contours are deposited.\n# - Correlation measure. The Results report \"Similar results ... using the Pearson method\", so\n#   the main measure is not Pearson, and the text does not name it. Readings: C-a, Spearman rank\n#   correlation at zero lag; C-b, the zero-lag normalised cross-correlation of the traces without\n#   mean subtraction (sum of x times y over the square root of the product of the sums of\n#   squares). Pearson is the paper's own variant (claim pearson-genotype).\n# - Pairs and units. \"Cells within 100 um\" is read as pairs whose distance in the data set's\n#   distance matrix is below 100 um. The n in every calcium imaging comparison is mice (or\n#   recordings for the EEG subset), so each mouse's value is the mean over its pairs (or cells),\n#   and tests are run on mouse values. Errors are s.e.m. over mice (Statistical Analyses).\n# - Tests. Unpaired two-tailed Student's t-test unless stated; alpha 0.05; post hoc p-values\n#   Bonferroni adjusted. The genotype by age comparison is an unequal-variance 2 x 3 fixed-effects\n#   ANOVA with Satterthwaite error degrees of freedom (Statistical Analyses). How it is fitted is\n#   not given; a standard choice is weighted least squares with each of the six groups weighted by\n#   the inverse of its variance and Satterthwaite degrees of freedom for each contrast, which\n#   should not change the outcome against other fits of the same model.\n# - Firing rate per mouse. The mean over cells of each cell's mean estimated rate over the\n#   recording. The data descriptor does not give the unit of the estimated rates; if they are per\n#   frame they are multiplied by 3.9 to give Hz (the author decides from the data which holds).\nschema_version: 2\ndataset:\n  archive: crcns\n  id: ssc-8\n  doi: 10.6080/K0X63K3X\npaper: doi:10.1038/nn.3415\nclaims:\n- id: group-sizes\n  statement: The calcium imaging of unanesthetized mice comprises 12, 9 and 8 WT mice and 9, 10 and\n    8 Fmr1 -/- mice at P9-11, P14-16 and P30-40.\n  source: Results, Cortical network synchrony is high in Fmr1 -/- mice, paragraph 1; Fig. 1e\n  quote: n = 12, 9, 8 WT mice at P9-11, P14-16, and P30-40, respectively and n = 9, 10, 8 Fmr1 –/–\n    mice at the same ages, respectively\n  expected:\n  - quantity: WT mice, P9-11\n    value: 12\n    tolerance: 0\n    unit: mice\n  - quantity: WT mice, P14-16\n    value: 9\n    tolerance: 0\n    unit: mice\n  - quantity: WT mice, P30-40\n    value: 8\n    tolerance: 0\n    unit: mice\n  - quantity: KO mice, P9-11\n    value: 9\n    tolerance: 0\n    unit: mice\n  - quantity: KO mice, P14-16\n    value: 10\n    tolerance: 0\n    unit: mice\n  - quantity: KO mice, P30-40\n    value: 8\n    tolerance: 0\n    unit: mice\n  criterion: The number of recordings (one per mouse, per the data descriptor) in each genotype\n    and age group. Tolerance 0, not 10%, as a count of mice is matched exactly or not. The\n    peaks of synchrony comparison gives n = 9 KO and 10 WT at P14-16 (claim fig2b-peak-frequency),\n    the reverse of Fig. 1e; the data set's P14-16 counts are reported against both.\n- id: fig1d-distance-dependent-decorrelation\n  statement: In WT mice, the drop in pairwise correlation from P9-11 (12 mice) to P14-16 (9 mice)\n    is largest for cells less than 100 um apart (mean difference 0.223) and smaller for cells\n    100-200 um (0.159) and more than 200 um apart (0.067, not significant).\n  source: Results, Cortical network synchrony is high in Fmr1 -/- mice, paragraph 1; Fig. 1d\n  quote: cell pairs located within 100 µm of one another displayed the largest differences in\n    pair-wise correlation coefficients between P9-11 (n = 12 mice) and P14-16 (n = 9 mice),\n    compared to cells farther apart (mean difference 0.223, p<0.0001 for cells <100 μm apart,\n    0.159, p<0.0001 for cells 100-200 μm apart and 0.067, p=0.0598 for cells >200 μm apart;\n    two-way ANOVA with Bonferroni corrected p values\n  statistics:\n  - about: P9-11 against P14-16, pairs under 100 um\n    test: two-way ANOVA, Bonferroni corrected post hoc\n    p: 0.0001\n    p_relation: \"<\"\n    corrected: Bonferroni\n    n: 12 and 9 WT mice\n  - about: P9-11 against P14-16, pairs 100-200 um\n    test: two-way ANOVA, Bonferroni corrected post hoc\n    p: 0.0001\n    p_relation: \"<\"\n    corrected: Bonferroni\n    n: 12 and 9 WT mice\n  - about: P9-11 against P14-16, pairs over 200 um\n    test: two-way ANOVA, Bonferroni corrected post hoc\n    p: 0.0598\n    corrected: Bonferroni\n    n: 12 and 9 WT mice\n  expected:\n  - quantity: mean correlation difference P9-11 minus P14-16, pairs under 100 um\n    value: 0.223\n    tolerance: 0.0223\n  - quantity: mean correlation difference P9-11 minus P14-16, pairs 100-200 um\n    value: 0.159\n    tolerance: 0.0159\n  - quantity: mean correlation difference P9-11 minus P14-16, pairs over 200 um\n    value: 0.067\n    tolerance: 0.0067\n  criterion: WT mice only (the n match the WT groups of Fig. 1e). Per mouse, the mean correlation\n    over its pairs in each of the three distance bins the text names (under 100, 100 to 200,\n    over 200 um), with the shared correlation readings. A two-way ANOVA on age (P9-11, P14-16)\n    and distance bin, then per bin the age difference with Bonferroni correction over the three\n    bins. The two-way ANOVA's form is not given (the text does not say whether bin is a repeated\n    factor); readings A-a, ordinary two-way ANOVA with bin as a between factor; A-b, mouse as a\n    repeated measure over bins. Reproduced when, under one reading of trace, measure and ANOVA,\n    the three differences are within tolerance, the first two have corrected p < 0.05 and the\n    third does not, and the difference falls with distance.\n- id: fig1e-age-decrease\n  statement: For cell pairs within 100 um, correlation decreases significantly with age in both WT\n    and Fmr1 -/- mice.\n  source: Results, Cortical network synchrony is high in Fmr1 -/- mice, paragraph 1; Fig. 1e\n  quote: When we quantified pairwise correlation coefficients for cells within 100 μm, we found a\n    statistically significant age-dependent decrease in network synchrony for both WT and Fmr1 –/–\n    mice (two-way unequal variance ANOVA, p<0.01 for both genotypes\n  statistics:\n  - about: age effect, WT\n    test: two-way unequal variance ANOVA\n    p: 0.01\n    p_relation: \"<\"\n    n: 12, 9 and 8 WT mice\n  - about: age effect, Fmr1 -/-\n    test: two-way unequal variance ANOVA\n    p: 0.01\n    p_relation: \"<\"\n    n: 9, 10 and 8 Fmr1 -/- mice\n  depends_on:\n  - group-sizes\n  criterion: Per mouse, the mean correlation of pairs under 100 um. The text does not say which\n    term of the 2 x 3 model gives \"p<0.01 for both genotypes\". Readings E-a, within the\n    unequal-variance 2 x 3 model, a 2-degree-of-freedom contrast of the three ages within each\n    genotype; E-b, a separate one-way unequal-variance (Welch) ANOVA of age per genotype.\n    Reproduced when, under one reading, both genotypes have p < 0.01 and the P9-11 mean exceeds\n    the P30-40 mean in each; partially reproduced when one genotype meets this.\n- id: genotype-pooled-ages\n  statement: Pooling all ages, correlation coefficients are higher in Fmr1 -/- than WT mice (0.265\n    +/- 0.009 against 0.230 +/- 0.008, p = 0.0057).\n  source: Results, Cortical network synchrony is high in Fmr1 -/- mice, paragraph 1; Fig. 1e\n  quote: we found significantly higher correlation coefficients for cell pairs in Fmr1 –/– mice when\n    pooling data for all ages (average corr. coefficient 0.230 ± 0.008 for WT vs. 0.265 ± 0.009 for\n    Fmr1 –/– , p = 0.0057, two-way unequal variance ANOVA)\n  statistics:\n  - about: genotype main effect, all ages\n    test: two-way unequal variance ANOVA\n    p: 0.0057\n    n: 29 WT and 27 Fmr1 -/- mice\n  expected:\n  - quantity: mean correlation, WT, all ages\n    value: 0.230\n    tolerance: 0.008\n  - quantity: mean correlation, Fmr1 -/-, all ages\n    value: 0.265\n    tolerance: 0.009\n  depends_on:\n  - group-sizes\n  criterion: Tolerances are the paper's s.e.m. Pairs under 100 um, as in the preceding sentence of\n    the paragraph (reading P-a); all pairs is reading P-b, since the sentence does not repeat the\n    distance. The genotype main effect of the unequal-variance 2 x 3 ANOVA on mouse means. How\n    the pooled average is formed is open; readings M-a, the mean over all mice of a genotype;\n    M-b, the mean of the three age means. Reproduced when, under one reading of trace, measure,\n    pairs and average, the genotype effect has p < 0.05 with KO higher and both means are within\n    tolerance; partially reproduced when the test holds and no reading brings both means within\n    tolerance.\n- id: pearson-genotype\n  statement: With Pearson correlation, pooled over ages, coefficients are again higher in Fmr1 -/-\n    than WT mice (0.196 +/- 0.010 against 0.164 +/- 0.009, p = 0.026).\n  source: Results, Cortical network synchrony is high in Fmr1 -/- mice, paragraph 1; Suppl. Fig. 1\n    (not in the text read)\n  quote: Similar results were found when we calculated correlation coefficients using the Pearson\n    method (average corr. coefficient 0.164 ± 0.009 for WT vs. 0.196 ± 0.010 for Fmr1 –/– , p =\n    0.026, two-way unequal-variance ANOVA\n  statistics:\n  - about: genotype main effect, all ages, Pearson\n    test: two-way unequal-variance ANOVA\n    p: 0.026\n  expected:\n  - quantity: mean Pearson correlation, WT, all ages\n    value: 0.164\n    tolerance: 0.009\n  - quantity: mean Pearson correlation, Fmr1 -/-, all ages\n    value: 0.196\n    tolerance: 0.010\n  depends_on:\n  - group-sizes\n  criterion: As genotype-pooled-ages, with the zero-lag Pearson correlation as the measure and\n    the same readings of trace, pairs and average. Tolerances are the paper's s.e.m.\n- id: fig1ef-p14-16-difference\n  statement: The genotype difference is largest at P14-16, where correlation is 0.210 +/- 0.011 in\n    Fmr1 -/- against 0.172 +/- 0.012 in WT mice (p = 0.032).\n  source: Results, Cortical network synchrony is high in Fmr1 -/- mice, paragraph 1; Fig. 1e and 1f\n  quote: The difference in correlation coefficients was most pronounced at P14-16 (0.172 ± 0.012 for\n    WT vs. 0.210 ± 0.011 for Fmr1 –/– , p=0.032, t-test\n  statistics:\n  - test: t-test\n    p: 0.032\n    n: 9 WT and 10 Fmr1 -/- mice\n  expected:\n  - quantity: mean correlation, pairs under 100 um, WT P14-16\n    value: 0.172\n    tolerance: 0.012\n  - quantity: mean correlation, pairs under 100 um, Fmr1 -/- P14-16\n    value: 0.210\n    tolerance: 0.011\n  depends_on:\n  - group-sizes\n  criterion: Pairs under 100 um (Fig. 1e), mouse means, unpaired two-tailed t-test. Tolerances\n    are the paper's s.e.m. Reproduced when, under one reading of trace and measure, p < 0.05 with\n    KO higher and both means are within tolerance, and the KO minus WT difference at P14-16 is\n    larger than at P9-11 and at P30-40 (\"most pronounced\"); partially reproduced when the test\n    holds and only part of the rest does.\n- id: p30-40-no-difference\n  statement: By P30-40 the genotype difference in correlation has decreased and is not significant\n    (0.144 +/- 0.008 in Fmr1 -/- against 0.123 +/- 0.008 in WT, p = 0.075).\n  source: Results, Cortical network synchrony is high in Fmr1 -/- mice, paragraph 1; Fig. 1e\n  quote: By P30-40, this difference in correlation coefficients in mice of both genotypes had\n    decreased (0.144 ± 0.008 vs. 0.123 ± 0.008 for Fmr1 –/– and WT respectively, p = 0.075, t-test)\n  statistics:\n  - test: t-test\n    p: 0.075\n    n: 8 WT and 8 Fmr1 -/- mice\n  expected:\n  - quantity: mean correlation, pairs under 100 um, Fmr1 -/- P30-40\n    value: 0.144\n    tolerance: 0.008\n  - quantity: mean correlation, pairs under 100 um, WT P30-40\n    value: 0.123\n    tolerance: 0.008\n  depends_on:\n  - group-sizes\n  criterion: A claim of absence, judged on the paper's test, an unpaired two-tailed t-test on mouse\n    means of pairs under 100 um at alpha 0.05. Reproduced when the test finds no difference\n    (p >= 0.05) under the reading of trace and measure that best matches claim\n    fig1ef-p14-16-difference; not reproduced when it finds one. The difference and the means\n    are reported either way, against the tolerances (the paper's s.e.m.).\n- id: fig2b-peak-frequency\n  statement: The frequency of peaks of synchrony at P14-16 is slightly but not significantly higher\n    in Fmr1 -/- mice (0.060 +/- 0.007 against 0.053 +/- 0.006 peaks per s, p = 0.45).\n  source: Results, Cortical network synchrony is high in Fmr1 -/- mice, paragraph 2; Fig. 2b\n  quote: The frequency of peaks of synchrony was slightly higher in Fmr1 –/– mice at P14-16, but the\n    difference was not significant (0.060 ± 0.007 vs. 0.053 ± 0.006 peaks per s for Fmr1 –/– and\n    WT, n = 9 and 10 mice, respectively; p=0.45; t-test\n  statistics:\n  - test: t-test\n    p: 0.45\n    n: 9 Fmr1 -/- and 10 WT mice, as printed\n  expected:\n  - quantity: peaks of synchrony per s, Fmr1 -/- P14-16\n    value: 0.060\n    tolerance: 0.007\n    unit: 1/s\n  - quantity: peaks of synchrony per s, WT P14-16\n    value: 0.053\n    tolerance: 0.006\n    unit: 1/s\n  criterion: A claim of absence, judged on the paper's test, an unpaired two-tailed t-test on mouse\n    values at alpha 0.05. Peaks of synchrony as the Methods define them; per frame, the percent of\n    cells active; each cell's deconvolved trace shuffled 100 times keeping its mean; per shuffle\n    the peak percent active; the 95th percentile of these 100 peaks is the threshold; an event\n    starts when the percent active crosses above it and ends when it falls below. Frequency is\n    events over recording time (3.9 Hz frames). Open, and run under each reading. When a cell is\n    \"active\" in a frame (R-a, estimated rate above 0; R-b, estimated spikes in the frame of at\n    least 1). How a trace is shuffled (S-a, random permutation of its frames; S-b, circular shift\n    by a random offset). Reproduced when the test finds no difference under the readings, not\n    reproduced when it finds one; the means are reported against the tolerances (the paper's\n    s.e.m.). The text's n (9 KO, 10 WT) is the reverse of Fig. 1e's P14-16 groups; the test is run\n    on the data set's P14-16 mice as they are.\n- id: fig2c-participation\n  statement: At P14-16 a higher proportion of neurons participates in peaks of synchrony in Fmr1\n    -/- than in WT mice (0.380 +/- 0.023 against 0.300 +/- 0.017, p = 0.023).\n  source: Results, Cortical network synchrony is high in Fmr1 -/- mice, paragraph 2; Fig. 2c\n  quote: However the proportion of neurons that participated in peaks of synchrony was significantly\n    higher in Fmr1 –/– mice than in WT mice at P14-16 (0.380 ± 0.023 vs. 0.300 ± 0.017 for Fmr1 –/–\n    and WT respectively; p = 0.023; t-test\n  statistics:\n  - test: t-test\n    p: 0.023\n  expected:\n  - quantity: proportion of neurons in peaks of synchrony, Fmr1 -/- P14-16\n    value: 0.380\n    tolerance: 0.023\n  - quantity: proportion of neurons in peaks of synchrony, WT P14-16\n    value: 0.300\n    tolerance: 0.017\n  depends_on:\n  - fig2b-peak-frequency\n  criterion: Events as in fig2b-peak-frequency, with its readings R and S. How the proportion is\n    formed is open; readings Q-a, per event the fraction of the mouse's cells active in any frame\n    of the event, averaged over the mouse's events; Q-b, the fraction of the mouse's cells active\n    in at least one event. Unpaired two-tailed t-test on mouse values. Reproduced when, under one\n    reading, p < 0.05 with KO higher and both means are within tolerance (the paper's s.e.m.);\n    partially reproduced when the test holds and the means are not both within tolerance.\n- id: imaging-firing-rate-no-genotype-difference\n  statement: Firing rates extrapolated from the calcium imaging by deconvolution do not differ\n    between genotypes at any age.\n  source: Results, Cortical network synchrony is high in Fmr1 -/- mice, paragraph 2 (data not shown)\n  quote: we calculated neuronal firing rates, as extrapolated from calcium imaging data by temporal\n    deconvolution (see Methods), but could not detect differences between genotypes at any age\n    using this method (not shown)\n  depends_on:\n  - group-sizes\n  criterion: A claim of absence. The paper names no test for it; the Methods' test for two groups\n    is the unpaired two-tailed Student's t-test at alpha 0.05, used here per age on mouse firing\n    rates (shared method). Reproduced when no age shows a difference; not reproduced when any\n    does. The means and differences are reported for each age.\n- id: unanesthetized-p14-16-values\n  statement: In unanesthetized P14-16 mice the extrapolated firing rate is 0.30 +/- 0.03 Hz in WT\n    and 0.29 +/- 0.03 Hz in Fmr1 -/- mice, and the correlation of pairs within 100 um is 0.17 +/-\n    0.01 in WT mice.\n  source: Results, Network activity is unchanged by anesthesia in mutant mice, paragraphs 1 and 2;\n    Fig. 6\n  quote: significantly higher in isoflurane-anesthetized WT mice than in unanesthetized WT mice\n    (0.24 ± 0.02 vs. 0.17 ± 0.01, n = 9 and 9 mice ... isoflurane had a significant effect on\n    extrapolated firing rates of L2/3 neurons in WT mice (0.30 ± 0.03 vs. 0.21 ± 0.02 Hz for\n    unanesthetized and isoflurane, respectively ... but did not change neuronal firing in Fmr1 –/–\n    mice (0.29± 0.03 vs. 0.27 ± 0.02 Hz for unanesthetized and isoflurane, respectively\n  expected:\n  - quantity: extrapolated firing rate, WT P14-16 unanesthetized\n    value: 0.30\n    tolerance: 0.03\n    unit: Hz\n  - quantity: extrapolated firing rate, Fmr1 -/- P14-16 unanesthetized\n    value: 0.29\n    tolerance: 0.03\n    unit: Hz\n  - quantity: mean correlation, pairs under 100 um, WT P14-16 unanesthetized\n    value: 0.17\n    tolerance: 0.01\n  depends_on:\n  - group-sizes\n  criterion: Tolerances are the paper's s.e.m. The unanesthetized groups of Fig. 6 (9 WT and 10\n    Fmr1 -/- mice) are read as the P14-16 mice of Fig. 1e, as the counts match; the text does not\n    say so. Firing rate per mouse as in the shared method. Reproduced when all three values are\n    within tolerance under one reading of trace and measure (for the correlation) and of rate\n    unit; partially reproduced when the two firing rates are.\n- id: wholecell-updown-firing\n  statement: In whole-cell recordings at P14-16, L2/3 neurons of Fmr1 -/- mice fire 3-fold more than\n    WT neurons during Up/Down states (0.40 +/- 0.05 Hz against 0.13 +/- 0.04 Hz).\n  source: Results, High firing rates during Up/Down states Fmr1 -/- mice, paragraph 1; Fig. 3e\n  quote: We discovered that L2/3 neurons in Fmr1 –/– mice had 3-fold higher firing rates than WT\n    mice during Up-Down states (0.40 ± 0.05 Hz, n = 6 recordings from 6 cells in 4 mice vs. 0.13 ±\n    0.04 Hz, n = 5 recordings from 5 cells in 5 mice; Bonferroni corrected p = 0.040, 2-way ANOVA\n  statistics:\n  - test: 2-way ANOVA, Bonferroni corrected\n    p: 0.040\n    corrected: Bonferroni\n    n: 6 Fmr1 -/- recordings (6 cells, 4 mice) and 5 WT recordings (5 cells, 5 mice)\n  expected:\n  - quantity: firing rate in Up/Down segments, Fmr1 -/-\n    value: 0.40\n    tolerance: 0.05\n    unit: Hz\n  - quantity: firing rate in Up/Down segments, WT\n    value: 0.13\n    tolerance: 0.04\n    unit: Hz\n  criterion: Whole-cell data. Spikes by a -20 mV threshold; 30 s epochs classed as Up/Down when the\n    mean of 20 two-Gaussian mixture fits (EM) has a mixing fraction from 25/75 to 45/55 and mode\n    separation over 5 mV, else FOA; the cell exclusions of the Methods. A 2-way ANOVA of genotype\n    by state on recording rates, Bonferroni corrected post hoc for genotype within Up/Down.\n    Reproduced when p < 0.05 with KO higher and both rates within tolerance (the paper's s.e.m.).\n- id: wholecell-state-modulation\n  statement: Neither genotype shows a significant change of firing rate between brain states in\n    whole-cell recordings; WT neurons tend to fire more in FOA (0.290 +/- 0.158 Hz) than in Up/Down\n    segments (0.133 +/- 0.036 Hz), and Fmr1 -/- neurons tend the other way.\n  source: Results, High firing rates during Up/Down states Fmr1 -/- mice, paragraph 1; Fig. 3e\n  quote: There was a trend toward higher firing rates in WT mice during FOA segments compared to\n    Up/Down states, but this was not significant (0.133 ± 0.036 Hz, n = 5 recordings from 5 cells\n    in 5 mice vs. 0.290 ± 0.158 Hz, n = 4 recordings from 4 cells in 4 mice, Bonferroni corrected p\n    = 0.41, 2-way ANOVA ... There was also an opposite trend for Fmr1 –/– mice, which showed a\n    tendency toward higher firing rates during Up/Down states compared to FOA\n  statistics:\n  - about: WT, FOA against Up/Down\n    test: 2-way ANOVA, Bonferroni corrected\n    p: 0.41\n    corrected: Bonferroni\n    n: 5 Up/Down and 4 FOA WT recordings\n  expected:\n  - quantity: WT firing rate, Up/Down segments\n    value: 0.133\n    tolerance: 0.036\n    unit: Hz\n  - quantity: WT firing rate, FOA segments\n    value: 0.290\n    tolerance: 0.158\n    unit: Hz\n  criterion: A claim of absence, judged on the paper's test, the Bonferroni corrected post hoc of\n    the 2-way ANOVA of wholecell-updown-firing, state within genotype, at alpha 0.05. The values\n    are read with 0.133 Hz as Up/Down, since it has the n of the WT Up/Down group above. Reproduced\n    when neither genotype shows a significant state effect; the direction in each genotype is\n    reported.\n- id: fig3f-foa-time\n  statement: Neurons of Fmr1 -/- and WT mice spend about the same fraction of time in the FOA state\n    (56% and 52%).\n  source: Results, High firing rates during Up/Down states Fmr1 -/- mice, paragraph 1; Fig. 3f\n  quote: recorded neurons in Fmr1 –/– mice spent approximately the same amount of time as WT mice in\n    the FOA brain state (56% and 52%, respectively\n  expected:\n  - quantity: percent of recording in FOA, Fmr1 -/-\n    value: 56\n    tolerance: 5.6\n    unit: percent\n  - quantity: percent of recording in FOA, WT\n    value: 52\n    tolerance: 5.2\n    unit: percent\n  criterion: Whole-cell data, epochs classed as in wholecell-updown-firing. The paper gives no\n    test; reproduced when both values are within tolerance.\n- id: ap-kinetics-similar\n  statement: Action potential kinetics do not differ between WT and Fmr1 -/- mice.\n  source: Results, High firing rates during Up/Down states Fmr1 -/- mice, paragraph 1; Suppl. Fig. 2\n    (not in the text read)\n  quote: we established that action potential kinetics were indistinguishable between WT and Fmr1\n    –/– mice\n  criterion: A claim of absence. Which kinetic measures and which test are in Suppl. Fig. 2, which\n    was not supplied; the Methods' default is the unpaired two-tailed t-test at alpha 0.05.\n    Readings for the measures are AP half-width, amplitude and threshold, each tested per cell.\n    Reproduced when none differs.\n- id: fig4-updown-properties-similar\n  statement: L2/3 Up states do not differ between WT and Fmr1 -/- mice at P14-16 in duration (1.30\n    +/- 0.06 s against 1.29 +/- 0.14 s), frequency (0.38 against 0.36 Hz) or Up-Down step (7.05\n    against 8.85 mV).\n  source: Results, High firing rates during Up/Down states Fmr1 -/- mice, paragraph 2; Fig. 4a-e\n  quote: we found no significant differences between WT and Fmr1 –/– mice in the duration of Up\n    states (1.30 ± 0.06 s, n = 5 cells vs.1.29 ± 0.14 s, n = 6 cells, respectively; p = 0.92,\n    t-test; Fig. 4a-c ), in the frequency of Up states (0.38 ± 0.03 Hz vs. 0.36 ± 0.02 Hz; p = 0.64,\n    t-test; Fig. 4d ), or in the Up-Down step (7.05 ± 0.86 mV vs. 8.85 ± 0.99 mV; p = 0.21, t-test\n  statistics:\n  - about: Up state duration\n    test: t-test\n    p: 0.92\n    n: 5 WT and 6 Fmr1 -/- cells\n  - about: Up state frequency\n    test: t-test\n    p: 0.64\n    n: 5 WT and 6 Fmr1 -/- cells\n  - about: Up-Down step\n    test: t-test\n    p: 0.21\n    n: 5 WT and 6 Fmr1 -/- cells\n  expected:\n  - quantity: Up state duration, WT\n    value: 1.30\n    tolerance: 0.06\n    unit: s\n  - quantity: Up state duration, Fmr1 -/-\n    value: 1.29\n    tolerance: 0.14\n    unit: s\n  - quantity: Up state frequency, WT\n    value: 0.38\n    tolerance: 0.03\n    unit: Hz\n  - quantity: Up state frequency, Fmr1 -/-\n    value: 0.36\n    tolerance: 0.02\n    unit: Hz\n  - quantity: Up-Down step, WT\n    value: 7.05\n    tolerance: 0.86\n    unit: mV\n  - quantity: Up-Down step, Fmr1 -/-\n    value: 8.85\n    tolerance: 0.99\n    unit: mV\n  criterion: A claim of absence, judged on the paper's tests, unpaired two-tailed t-tests per cell\n    at alpha 0.05. Up and Down states as the Methods define them (3 Hz low-pass; per minute, mean\n    voltage plus or minus half the s.d. as thresholds; Up when above for at least 1 s, Down when\n    below for at least 0.85 s). Reproduced when no measure differs; values reported against the\n    tolerances (the paper's s.e.m.).\n- id: fig4f-spikes-per-up-state\n  statement: Fmr1 -/- neurons tend to fire more action potentials per active Up state than WT\n    neurons (2.57 +/- 0.38 against 1.67 +/- 0.18), but the difference is not significant.\n  source: Results, High firing rates during Up/Down states Fmr1 -/- mice, paragraph 2; Fig. 4f\n  quote: Although we found a strong trend toward a higher number of action potentials per active Up\n    state in Fmr1 –/– mice, this difference was not significant (2.57 ± 0.38, n = 6 cells vs. 1.67±\n    0.18, n = 5 cells spikes in Fmr1 –/– and WT mice, respectively; p = 0.079, t-test\n  statistics:\n  - test: t-test\n    p: 0.079\n    n: 6 Fmr1 -/- and 5 WT cells\n  expected:\n  - quantity: spikes per active Up state, Fmr1 -/-\n    value: 2.57\n    tolerance: 0.38\n  - quantity: spikes per active Up state, WT\n    value: 1.67\n    tolerance: 0.18\n  criterion: A claim of absence, judged on the paper's test, an unpaired two-tailed t-test per cell\n    at alpha 0.05; an active Up state has 1 or more spikes. Reproduced when the test finds no\n    difference; values reported against the tolerances (the paper's s.e.m.).\n- id: fig4g-up-state-firing-probability\n  statement: The probability of firing during an Up state is 2-fold higher in Fmr1 -/- than in WT\n    neurons (0.45 +/- 0.05 against 0.21 +/- 0.05, p = 0.009).\n  source: Results, High firing rates during Up/Down states Fmr1 -/- mice, paragraph 2; Fig. 4g\n  quote: In contrast, the firing probability during any given Up state was 2-fold higher in the\n    mutants (0.45 ± 0.05, n = 6 cells vs. 0.21 ± 0.05, n = 5 cells; p = 0.009, t-test\n  statistics:\n  - test: t-test\n    p: 0.009\n    n: 6 Fmr1 -/- and 5 WT cells\n  expected:\n  - quantity: fraction of Up states with a spike, Fmr1 -/-\n    value: 0.45\n    tolerance: 0.05\n  - quantity: fraction of Up states with a spike, WT\n    value: 0.21\n    tolerance: 0.05\n  criterion: Per cell, the fraction of Up states with 1 or more spikes; unpaired two-tailed t-test.\n    Reproduced when p < 0.05 with KO higher and both values within tolerance (the paper's s.e.m.).\n- id: fig5c-firing-vs-lh-p14-16\n  statement: At P14-16 the extrapolated firing rate correlates with EEG L/H power in Fmr1 -/- mice\n    (r2 = 0.676) but not in WT mice (r2 = 0.046).\n  source: Results, Brain state-dependent defects in activity modulation, paragraph 1; Fig. 5c\n  quote: we found that firing rates (extrapolated from calcium traces) did not vary significantly\n    between recordings exhibiting high L/H power (expected during sleep) or low L/H power (expected\n    during wakefulness) (r 2 = 0.046, n = 13 recordings, p = 0.481, F-test ... In contrast, the\n    firing of L2/3 neurons in Fmr1 –/– mice at P14-16 (n = 5 mice, average age 15.0 days) was\n    significantly correlated with L/H power (r 2 = 0.676, n = 10 recordings p = 0.004, F-test\n  statistics:\n  - about: WT\n    test: F-test\n    statistic: r2 = 0.046\n    p: 0.481\n    n: 13 recordings from 5 WT mice\n  - about: Fmr1 -/-\n    test: F-test\n    statistic: r2 = 0.676\n    p: 0.004\n    n: 10 recordings from 5 Fmr1 -/- mice\n  expected:\n  - quantity: r2, firing rate against L/H power, WT\n    value: 0.046\n    tolerance: 0.0046\n  - quantity: r2, firing rate against L/H power, Fmr1 -/-\n    value: 0.676\n    tolerance: 0.0676\n  criterion: Needs the EEG recorded with each 3-min imaging recording. Per recording, the mean\n    extrapolated firing rate and L/H power (0.5-4 Hz over 20-60 Hz, Chronux spectra); linear\n    regression, F-test. Reproduced when the KO slope is significant (p < 0.05) and the WT one is\n    not, with r2 within tolerance.\n- id: p30-40-firing-vs-lh\n  statement: At P30-40 firing rate still correlates with L/H power in Fmr1 -/- mice (r2 = 0.73) but\n    not in WT mice (r2 = 0.027).\n  source: Results, Brain state-dependent defects in activity modulation, paragraph 1 (not shown)\n  quote: The strong correlation between neuronal firing and L/H power in the EEG was still present\n    at P30-40 in Fmr1 –/– mice, but not WT mice (r 2 = 0.73, n = 10 recordings from 4 mice, p =\n    0.002 for Fmr1 –/– vs. r 2 = 0.027, n = 10 WT recordings from 4 mice, p = 0.65 for WT, F-test\n  statistics:\n  - about: Fmr1 -/-\n    test: F-test\n    statistic: r2 = 0.73\n    p: 0.002\n    n: 10 recordings from 4 Fmr1 -/- mice\n  - about: WT\n    test: F-test\n    statistic: r2 = 0.027\n    p: 0.65\n    n: 10 recordings from 4 WT mice\n  expected:\n  - quantity: r2, firing rate against L/H power, Fmr1 -/- P30-40\n    value: 0.73\n    tolerance: 0.073\n  - quantity: r2, firing rate against L/H power, WT P30-40\n    value: 0.027\n    tolerance: 0.0027\n  criterion: As fig5c-firing-vs-lh-p14-16, at P30-40.\n- id: fig5d-correlation-vs-lh\n  statement: Pairwise correlation shows a nearly significant trend to rise with L/H power in Fmr1\n    -/- mice at P14-16 (r2 = 0.347, p = 0.073) and none in WT mice (r2 = 0.027).\n  source: Results, Brain state-dependent defects in activity modulation, paragraph 1; Fig. 5d\n  quote: Pair-wise correlation coefficients (as determined from calcium traces; 100 μm distance\n    between pairs) showed a nearly-significant trend toward higher synchrony with higher L/H power\n    in Fmr1 –/– mice at P14-16, but not in WT mice (r 2 = 0.347, n = 10 recordings, with p=0.073 vs.\n    r 2 = 0.027, n = 13 recordings with p = 0.649, F-test\n  statistics:\n  - about: Fmr1 -/-\n    test: F-test\n    statistic: r2 = 0.347\n    p: 0.073\n    n: 10 recordings\n  - about: WT\n    test: F-test\n    statistic: r2 = 0.027\n    p: 0.649\n    n: 13 recordings\n  criterion: A claim of absence for both genotypes at alpha 0.05, judged on the paper's F-test of\n    the regression of recording correlation (pairs under 100 um) on L/H power. Reproduced when\n    neither slope is significant; the KO slope's sign and p are reported.\n- id: fig5ef-slow-wave-epochs\n  statement: In EEG epochs with L/H power above 200, Fmr1 -/- mice have higher firing rates (0.27 +/-\n    0.017 against 0.22 +/- 0.0096 Hz) and higher correlation (0.25 +/- 0.014 against 0.20 +/-\n    0.015) than WT mice.\n  source: Results, Brain state-dependent defects in activity modulation, paragraph 1; Fig. 5e and 5f\n  quote: when we examined only EEG epochs with L/H power > 200 ... we found that Fmr1 –/– mice had\n    higher firing rates (0.27 ± 0.017 Hz, n = 5 Fmr1 –/– recordings vs. 0.22 ± 0.0096 Hz, n = 6 WT\n    recordings, p=0.023, t-test; Fig. 5e ) and higher correlation coefficients than WT mice (0.25 ±\n    0.014, n = 5 Fmr1 –/– recordings, 0.20 ± 0.015, n = 6 WT recordings, p=0.039, t-test\n  statistics:\n  - about: firing rate\n    test: t-test\n    p: 0.023\n    n: 5 Fmr1 -/- and 6 WT recordings\n  - about: correlation\n    test: t-test\n    p: 0.039\n    n: 5 Fmr1 -/- and 6 WT recordings\n  expected:\n  - quantity: firing rate, L/H over 200, Fmr1 -/-\n    value: 0.27\n    tolerance: 0.017\n    unit: Hz\n  - quantity: firing rate, L/H over 200, WT\n    value: 0.22\n    tolerance: 0.0096\n    unit: Hz\n  - quantity: correlation, L/H over 200, Fmr1 -/-\n    value: 0.25\n    tolerance: 0.014\n  - quantity: correlation, L/H over 200, WT\n    value: 0.20\n    tolerance: 0.015\n  criterion: Needs the EEG. Recordings with L/H power above 200, P14-16; unpaired two-tailed\n    t-tests. Reproduced when both tests give p < 0.05 with KO higher and the values are within\n    tolerance (the paper's s.e.m.).\n- id: suppl4a-firing-vs-correlation\n  statement: Across recordings, firing rate and correlation are strongly correlated in Fmr1 -/- mice\n    (r2 = 0.65) but not in WT mice (r2 = 0.005).\n  source: Results, Brain state-dependent defects in activity modulation, paragraph 2; Suppl. Fig. 4a\n    (not in the text read)\n  quote: whereas in WT mice they are not correlated (r 2 =0.005, n = 13 recordings, p=0.46, F-test),\n    in Fmr1 –/– mice they were highly correlated (r 2 =0.65, n = 10 recordings, p=0.0027; F-test\n  statistics:\n  - about: WT\n    test: F-test\n    statistic: r2 = 0.005\n    p: 0.46\n    n: 13 recordings\n  - about: Fmr1 -/-\n    test: F-test\n    statistic: r2 = 0.65\n    p: 0.0027\n    n: 10 recordings\n  expected:\n  - quantity: r2, correlation against firing rate, WT\n    value: 0.005\n    tolerance: 0.0005\n  - quantity: r2, correlation against firing rate, Fmr1 -/-\n    value: 0.65\n    tolerance: 0.065\n  criterion: The recordings are those of the EEG subset at P14-16 (13 WT, 10 KO), each a 3-min\n    imaging recording. Per recording, mean extrapolated firing rate and mean correlation of pairs\n    under 100 um; linear regression, F-test. Reproduced when the KO slope is significant\n    (p < 0.05) and positive and the WT one is not. One value per mouse of the data set is not the\n    paper's sample (n is recordings); the author decides whether the data set holds the 3-min\n    recordings.\n- id: fig5g-lh-power-similar\n  statement: Average L/H power is similar in WT and Fmr1 -/- mice (176.1 +/- 29.55 against 180.2\n    +/- 30.58, p = 0.92).\n  source: Results, Brain state-dependent defects in activity modulation, paragraph 2; Fig. 5g\n  quote: the average L/H power was similar between WT and Fmr1 –/– mice (176.1 ± 29.55, n = 10\n    recordings, 180.2 ± 30.58, n = 13 recordings, respectively, p = 0.92, t-test\n  statistics:\n  - test: t-test\n    p: 0.92\n  expected:\n  - quantity: mean L/H power, first group as printed (WT)\n    value: 176.1\n    tolerance: 29.55\n  - quantity: mean L/H power, second group as printed (Fmr1 -/-)\n    value: 180.2\n    tolerance: 30.58\n  criterion: A claim of absence, judged on the paper's unpaired two-tailed t-test on recordings at\n    alpha 0.05. The text assigns n = 10 to WT and 13 to Fmr1 -/-, the reverse of the n in Fig. 5c\n    (13 WT, 10 KO recordings); readings G-a as printed; G-b with the groups swapped. Reproduced\n    when the test finds no difference; values reported under both readings.\n- id: fast-imaging-control\n  statement: Imaging at 15.6 Hz, firing rates again rise with L/H power in Fmr1 -/- mice (r2 = 0.38)\n    but not in WT mice (r2 = 0.11) at P14-16.\n  source: Results, Brain state-dependent defects in activity modulation, paragraph 3 (not shown)\n  quote: when we performed calcium imaging at 15.6 Hz (which provides better spike detection) we\n    again found that firing rates increased significantly with higher L/H power in Fmr1 –/– mice,\n    but not WT mice at P14-16 (r 2 = 0.38, n = 12 recordings from 4 mice, p = 0.032 in Fmr1 –/– vs.\n    r 2 = 0.11, n = 10 recordings from 5 mice, p = 0.35 in WT, F-test\n  statistics:\n  - about: Fmr1 -/-\n    test: F-test\n    statistic: r2 = 0.38\n    p: 0.032\n    n: 12 recordings from 4 Fmr1 -/- mice\n  - about: WT\n    test: F-test\n    statistic: r2 = 0.11\n    p: 0.35\n    n: 10 recordings from 5 WT mice\n  expected:\n  - quantity: r2, 15.6 Hz, Fmr1 -/-\n    value: 0.38\n    tolerance: 0.038\n  - quantity: r2, 15.6 Hz, WT\n    value: 0.11\n    tolerance: 0.011\n  criterion: As fig5c-firing-vs-lh-p14-16, on the 15.6 Hz recordings.\n- id: fig6-isoflurane-wt-correlation\n  statement: Isoflurane raises correlation of pairs within 100 um in WT mice at P14-16 (0.24 +/- 0.02\n    against 0.17 +/- 0.01 unanesthetized, p = 0.0045).\n  source: Results, Network activity is unchanged by anesthesia in mutant mice, paragraph 1; Fig. 6a\n    and 6c\n  quote: We confirmed that pair-wise correlation coefficients for cells within 100 μm were\n    significantly higher in isoflurane-anesthetized WT mice than in unanesthetized WT mice (0.24 ±\n    0.02 vs. 0.17 ± 0.01, n = 9 and 9 mice, respectively; p=0.0045, t-test\n  statistics:\n  - test: t-test\n    p: 0.0045\n    n: 9 anesthetized and 9 unanesthetized WT mice\n  expected:\n  - quantity: mean correlation, WT isoflurane\n    value: 0.24\n    tolerance: 0.02\n  - quantity: mean correlation, WT unanesthetized\n    value: 0.17\n    tolerance: 0.01\n  criterion: Needs imaging under isoflurane. Mouse means of pairs under 100 um, unpaired two-tailed\n    t-test. Reproduced when p < 0.05 with isoflurane higher and both values within tolerance.\n- id: fig6-isoflurane-ko-correlation\n  statement: Isoflurane does not change correlation in Fmr1 -/- mice at P14-16 (0.21 +/- 0.01 against\n    0.18 +/- 0.01, p = 0.14).\n  source: Results, Network activity is unchanged by anesthesia in mutant mice, paragraph 1; Fig. 6b\n    and 6d\n  quote: In contrast, correlation coefficients in Fmr1 –/– mice were unchanged by isoflurane\n    anesthesia (0.21 ± 0.01 vs. 0.18 ± 0.01, n=10 and 10 mice, respectively, p=0.14, t-test\n  statistics:\n  - test: t-test\n    p: 0.14\n    n: 10 and 10 Fmr1 -/- mice\n  criterion: A claim of absence, judged on the paper's unpaired two-tailed t-test at alpha 0.05.\n    The text does not say which value is anesthetized. Readings I-a, 0.21 isoflurane and 0.18\n    unanesthetized, in the order of the WT sentence; I-b, 0.21 unanesthetized, matching the\n    Fig. 1e P14-16 KO value (0.210). Reproduced when the test finds no difference; the values are\n    reported under both readings.\n- id: fig6-isoflurane-firing\n  statement: Isoflurane lowers extrapolated firing rates in WT mice (0.30 +/- 0.03 to 0.21 +/- 0.02\n    Hz, p = 0.0084) but does not change them in Fmr1 -/- mice (0.29 +/- 0.03 to 0.27 +/- 0.02 Hz,\n    p = 0.62).\n  source: Results, Network activity is unchanged by anesthesia in mutant mice, paragraph 2\n  quote: isoflurane had a significant effect on extrapolated firing rates of L2/3 neurons in WT mice\n    (0.30 ± 0.03 vs. 0.21 ± 0.02 Hz for unanesthetized and isoflurane, respectively, p=0.0084,\n    t-test), but did not change neuronal firing in Fmr1 –/– mice (0.29± 0.03 vs. 0.27 ± 0.02 Hz\n    for unanesthetized and isoflurane, respectively, p=0.62, t-test\n  statistics:\n  - about: WT\n    test: t-test\n    p: 0.0084\n  - about: Fmr1 -/-\n    test: t-test\n    p: 0.62\n  expected:\n  - quantity: firing rate, WT isoflurane\n    value: 0.21\n    tolerance: 0.02\n    unit: Hz\n  - quantity: firing rate, Fmr1 -/- isoflurane\n    value: 0.27\n    tolerance: 0.02\n    unit: Hz\n  depends_on:\n  - unanesthetized-p14-16-values\n  criterion: Needs imaging under isoflurane. Mouse firing rates (shared method), unpaired\n    two-tailed t-tests. Reproduced when WT shows p < 0.05 with isoflurane lower and KO shows no\n    difference at alpha 0.05, with the values within tolerance (the paper's s.e.m.); the\n    unanesthetized values are claim unanesthetized-p14-16-values.\n"
}
```

```
File created successfully at: claims/crcns-ssc-8/10.1038-nn.3415.yaml (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd  python tools/claims_check.py claims/crcns-ssc-8/10.1038-nn.3415.yaml paper/10.1038-nn.3415.txt; grep -n "—\|rather" claims/crcns-ssc-8/*.yaml
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  python -c "
import yaml;d=yaml.safe_load(open('claims/crcns-ssc-8/10.1038-nn.3415.yaml'))
c=d['claims'];print(len(c),sum('statistics' in x for x in c),sum(len(x.get('statistics',[])) for x in c),sum('criterion' in x for x in c),sum('expected' in x for x in c))
import re
for x in c:
  for k,v in x.items():
    if isinstance(v,str) and ': ' in v: print(x['id'],k)
"
```

```
28 23 35 28 23
```

**Agent**

I wrote `claims/crcns-ssc-8/10.1038-nn.3415.yaml`. The quote checker reports 28 claims, 28 quotes, 35 statistical values and 0 problems.

**Text read:** the version of record, PMC3695061 (open access), taken from the Europe PMC full-text XML. It has the main text and the Online Methods. Three things were missing:
- **Figure legends:** not in the text.
- **Supplement:** Supplementary Figs. 1 to 4 are cited but were not supplied.
- **PDF:** none was supplied.

I went ahead because every number the claims use is printed in the Results text. The paper links no analysis code, so none was read.

**Claims:** 28 findings, every one with a quote and none under `inferred`. 23 have statistics (35 tests in all), 23 have expected values, and all 28 have a criterion. Where the paper gives an s.e.m., that is the tolerance. Mouse counts have tolerance 0, with the reason stated. Every claim uses the default `data` (the paper's own recordings). The dataset can test 11 claims: group sizes, Fig. 1d, Fig. 1e, the genotype difference pooled over ages, Pearson, P14-16, P30-40, Fig. 2b, Fig. 2c, imaging firing rates, and the unanesthetized P14-16 values. The other 17 need whole-cell, EEG, isoflurane or 15.6 Hz data, which the CRCNS description does not list.

**Details the paper leaves open, with the readings named:**
- **Trace used for correlation:** T-a, the deconvolved traces (the dataset's estimated rates); T-b, ΔF/F traces, which would mean segmenting the cells again.
- **Correlation measure:** it is not Pearson, since Pearson is given as the alternative. C-a, Spearman at zero lag; C-b, zero-lag normalised cross-correlation without mean subtraction.
- **Fig. 1d ANOVA form:** A-a, distance bin as a between factor; A-b, mouse as a repeated measure.
- **Fig. 1e age test:** E-a, a within-genotype contrast in the 2×3 model; E-b, a Welch ANOVA for each genotype.
- **Pooled-ages comparison:** which pairs (P-a, under 100 µm; P-b, all pairs) and how the mean is formed (M-a, over all mice; M-b, the mean of the three age means).
- **Peaks of synchrony:** when a cell is active (R-a, rate above 0; R-b, at least 1 spike per frame), how traces are shuffled (S-a, permutation; S-b, circular shift), and how participation is measured (Q-a, per event; Q-b, at least one event).
- **Fig. 2b group sizes:** n is printed as 9 KO and 10 WT, the reverse of Fig. 1e.
- **Fig. 5g group sizes:** n is printed as 10 WT and 13 KO, the reverse of Fig. 5c. G-a, as printed; G-b, swapped.
- **Fig. 6 KO correlation:** the text does not say which value is under isoflurane. I-a, 0.21 is isoflurane; I-b, 0.21 is unanesthetized.
- **Unit of the estimated rates:** the descriptor does not say, so the rates are either Hz or per frame (times 3.9).
- **Unanesthetized Fig. 6 groups:** read as the Fig. 1e P14-16 mice, because the counts match.
- **Fitting the unequal-variance ANOVA:** I used weighted least squares with Satterthwaite degrees of freedom as a standard choice.
- **Imaging firing-rate absence claim:** the paper names no test, so it uses the Methods' default t-test.

**Missing material a claim needed:** Supplementary Fig. 2, for the measures and test behind "action potential kinetics were indistinguishable"; readings are named in that claim. Supplementary Figs. 1 and 4a, and the Fig. 1 legend, which may have named the correlation measure; I treated it as open.

Nothing was committed.

## End of run

16 turns, 4 minutes, $1.32 at API prices, result: success.
