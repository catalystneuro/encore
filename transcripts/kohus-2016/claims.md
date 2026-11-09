# crcns-hc-7 · claims · run 42213956872

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cat docs/protocol.md; ls claims/001453/ claims/crcns-hc-7/ paper/;
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -n '/^### 3. Write the claims file/,/^## Author/p' docs/protocol.md
```

```
### 3. Write the claims file

Write `claims/<folder>/<doi with / replaced by ->.yaml`. Its opening comment
says which text was read (the version of record or a preprint version, and the
supplement), and describes the data the paper used: the subjects, sessions,
conditions and measured variables, as the paper reports them, so that the
author can find them in the dataset.

   - One claim per finding, at the level of a figure panel or a reported
     number when the full text is available. Cover the paper's main findings,
     including those the dataset cannot test.
   - `statement`: the finding in words. `source`: where the paper shows it,
     precise enough to find without searching: a figure panel, or a section
     and paragraph ("Results, Place fields, paragraph 3").
   - `quote`: the sentence at `source` that states the finding, copied word
     for word from the full text, cut with "..." where it runs long. It lets a
     reader check the statement against the paper without opening it. For a
     finding shown only in a figure, quote the legend or the sentence of the
     Results that cites the panel.
   - `inferred`: every finding has a quote or, when no sentence of the paper
[... 100 more lines not kept]
```

**Agent calls Bash**

```bash
ls claims/001453/ claims/crcns-hc-7/ paper/; head -c 6000 claims/001453/*.yaml; wc paper/*
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -n '1,400p' paper/10.1113-jp272231.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -n '200,400p' claims/001453/*.yaml | head -150; ls tools
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
[... 129 more lines not kept]
```

**Agent calls Bash**

```bash
tail -60 claims/001453/*.yaml; grep -n "kind\|data:" claims/001453/*.yaml | head -30; cat paper/hc-7.data-description.txt
```

Result: not kept, because it reads the paper's text.

**Agent**

Read the protocol, the example claims file and the data descriptor. Now reading the rest of the paper.

**Agent calls Bash**

```bash
sed -n '400,1100p' paper/10.1113-jp272231.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -n '1100,2000p' paper/10.1113-jp272231.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -n '2000,2900p' paper/10.1113-jp272231.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -n '2900,3888p' paper/10.1113-jp272231.txt | grep -v '^[0-9. ]*$' | head -600
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
grep -n -i "github\|supplement\|supporting\|modeldb\|code avail\|Table 4\b" paper/10.1113-jp272231.txt | head; sed -n '3700,3888p' paper/10.1113-jp272231.txt | grep -v "^[A-Z][a-z]* [A-Z]" | tail -60
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -n '1,80p' tools/claims_check.py; grep -n "def \|normal" tools/claims_check.py | head -40
```

```
"""Check a claims file against the full text of its paper.

    python tools/claims_check.py claims/<dandiset>/<doi>.yaml paper/<text>.txt [more texts ...]

Validates the file against schemas/claims.schema.json, checks every quote word for word
(fragments split on "...", found in order) and looks for every recorded p-value and
confidence-interval bound in the text. The text may be plain text, HTML or JATS XML; several
files (a paper and its supplement) are searched together. A value printed in a form the
checker does not know (a garbled PDF glyph, "p = 0.04, 0.05 and 0.16") is reported, to be
confirmed by reading. Exits non-zero on any problem.
"""

from __future__ import annotations

import html
import re
import sys
import unicodedata
from pathlib import Path

[... 68 more lines not kept]
```

**Agent**

The paper is the version of record, with full Methods. It links no code and has no supplement, only the CRCNS dataset. Next I'm checking the claims schema, then I'll write the file.

**Agent calls Bash**

```bash
cat schemas/claims.schema.json | head -200
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
[... 180 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n '200,400p' schemas/claims.schema.json; ls claims | head -50; ls claims | grep -i crcns
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
[... 192 more lines not kept]
```

**Agent calls Bash**

```bash
ls claims/crcns-ear-1; head -50 claims/crcns-ear-1/*.yaml
```

```
10.1085-jgp.201912447.yaml
# Claims for Farrell, Skidmore, Rajasekharan & Brownell (2020), J Gen Physiol 152(7), "A novel
# theoretical framework reveals more than one voltage-sensing pathway in the lateral membrane of
# outer hair cells", doi:10.1085/jgp.201912447, on CRCNS data set ear-1 (doi:10.6080/K0571975).
# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"), 2026-11-06,
# protocol as stated in docs/protocol.md (Reader), version pilot-13.
#
# Text read: the version of record (PMC7335013, open access), as supplied under paper/ (Europe PMC
# JATS XML flattened to text): Introduction, Theoretical model, the section on expressions for the
# experimental parameters, Materials and methods, Results, Discussion, the legends of Figures 1 to 5
# and S1 to S7, and Tables 1 to 3. No PDF was supplied.
# Missing from the text. (1) Every displayed equation (Eqs. 1 to 9) is lost in the flattening; only
# the prose around them is there. The forms used below were rebuilt from that prose and checked
# against the paper's own numbers, and each is marked as a reconstruction where a criterion uses it.
#   Eq. 2c, the charge density, dVmin_exp = QTm / CLW (prose; Fig. S1 legend gives QTm 3.02 pC and
#     CLW 18.56 pF, 0.163 V).
#   Eq. 3a, V0.5 = Vd - dVmin_exp / 2 (prose; slope -1/2, intercept Vd, "Vd was the only free
#     parameter"); with Eq. 3b, Vh = V0.5 - dVmin_exp / 2 and Vd = V0.5 + dVmin_exp / 2.
#   Eq. 5, z = n delta = alphaB kB T / e0 (Table 1, alphaB 37.3 and z 0.96 at 24 C).
#   Eq. 8d, alphaB = 4 alpha(V0.5) (Results, 9.32 and 8.08 V-1 against Table 1, 37.3 and 32.3 V-1).
[... 31 more lines not kept]
```

**Agent calls Bash**

```bash
grep -n -A5 "^schema_version" claims/crcns-ear-1/*.yaml; grep -n "elsewhere\|with_inputs\|data: " claims/crcns-ear-1/*.yaml | head
```

```
69:schema_version: 2
70-dataset:
71-  archive: crcns
72-  id: ear-1
73-  doi: 10.6080/K0571975
74-paper: doi:10.1085/jgp.201912447
768:  data: with_inputs
786:  data: with_inputs
1102:  data: with_inputs
1141:  data: with_inputs
1151:  data: with_inputs
1163:  data: with_inputs
```

**Agent calls Bash**

```bash
cd $TMPDIR && python -c "
import fitz
d=fitz.open('paper/10.1113-jp272231.pdf')
print(len(d))
for p in [13,14,15,16,18,19,22,25]:
    d[p-1].get_pixmap(dpi=130).save(f'p{p}.png')
"; ls $TMPDIR
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
which pdftoppm mutool; python -c "import pypdfium2" 2>&1; python -c "import pdfplumber" 2>&1
```

```
Exit code 1
Traceback (most recent call last):
  File "<string>", line 1, in <module>
    import pypdfium2
ModuleNotFoundError: No module named 'pypdfium2'
Traceback (most recent call last):
  File "<string>", line 1, in <module>
    import pdfplumber
ModuleNotFoundError: No module named 'pdfplumber'
```

**Agent**

No PDF rendering library here, so I'm reading the figure pages through the Read tool.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1113-jp272231.pdf",
 "pages": "13-14"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Write**

```json
{
 "file_path": "claims/crcns-hc-7/10.1113-jp272231.yaml",
 "content": "# Claims for Kohus, Kali, Rovira-Esteban, Schlingloff, Papp, Freund, Hajos & Gulyas (2016), J Physiol,\n# \"Properties and dynamics of inhibitory synaptic communication within the CA3 microcircuits of\n# pyramidal cells and interneurons expressing parvalbumin or cholecystokinin\", doi:10.1113/jp272231,\n# on CRCNS data set hc-7 (doi:10.6080/K0MK69T5).\n# Written by an agent (model \"claude-opus-5-5\", Claude Code, runner \"GitHub Actions\"), 2026-11-06,\n# protocol as stated in docs/protocol.md (Reader), version pilot-13.\n#\n# Text read: the version of record (J Physiol 2016, pp 1 to 30), as supplied under paper/ (text\n# extracted from the PDF with PyMuPDF): Key points, Methods, Results, Discussion, the legends of\n# Figures 1 to 13 and Tables 1 to 4. The paper has no supplement. The PDF could not be opened as\n# images in this run (no renderer installed), so values printed only inside figures (the medians of\n# Fig. 4B, 5C, 5Db, 6B and C, 7, 10, 11B and 12) were not read; claims on those figures rest on the\n# Results and the legends. In the extracted Table 4 the columns for the connection type specific\n# parameters (tau_r, tau_e, a_e, k_e) are empty; their values are taken from the Figure 11 legend.\n# In the CCK+BC to PC row of Table 4 the three values given with quartiles (0.15, 10.9, 499) are read\n# as U0, tau_f and Imax, since tau_r is fitted per type (12.9 s, Fig. 11 legend) and has no quartiles.\n#\n# Code. The paper links no code. Its Methods name in-house and third-party programs (Stimulog, EVAN,\n# MATLAB 7.0.4 and Delphi 6.0 scripts, a feature extraction script by M. Rozsa modified by S. Kali,\n# software for asynchronous charge by D. Gemes, Origin 9.0 for exponential fits and statistics); none\n# is published. Every method below is from the paper's text.\n#\n# Data the paper used. Acute horizontal hippocampal slices (250 to 350 um) from BAC-PV-eGFP and\n# BAC-CCK-DsRed mice of both sexes, postnatal day 18 to 25, CA3 area, modified aCSF (3.5 mM K, 1.6 mM\n# Ca, 1.2 mM Mg), 30 to 32 C, NBQX 20 uM and AP-5 50 uM, AM251 1 uM for CCK+ cells. Paired whole-cell\n# recordings: presynaptic interneuron in current clamp at -65 mV, driven by 1 ms, 1500 pA current\n# pulses; postsynaptic cell in voltage clamp at -60 mV; 3 kHz low-pass, 10 kHz sampling. Mostly high\n# KCl pipette solution in both cells; in some pairs low KCl (presynaptic) and high CsCl (postsynaptic).\n# Cell types identified post hoc (biocytin, ankyrin G for AACs, CB1 for CCK+ cells): PV+ basket\n# cells (PV+BC), axo-axonic cells (AAC), CCK+ basket cells (CCK+BC) and CCK+ dendritic-region\n# targeting cells (CCK+DTI), and pyramidal cells (PC). Protocols: 10 APs at 1, 5, 10, 20, 40, 80,\n# 160 and 320 Hz followed by an 11th AP after 1000 ms; RIP (a single AP, then after 1000 ms four APs\n# at 160 Hz); EPI (a single AP, then after 1000 ms 30 APs at 160 Hz and four at 320 Hz); recovery\n# (two RIP trains 50, 100, 200, 300, 500, 800 or 1200 ms apart). Pairs reported: interneuron to PC,\n# high KCl, PV+BC 8, AAC 9, CCK+BC 14, CCK+DTI 8 (Fig. 4, 5; 10-AP trains PV+BC 6, AAC 8, CCK+BC 6,\n# CCK+DTI 3 or 4, Fig. 6; recovery PV+BC 7, AAC 9, CCK+BC 11); with CsCl, PV+BC 9, AAC 10, CCK+BC 6;\n# interneuron to interneuron, PV+BC to PV+BC 16 (13 with 10-AP trains), CCK+BC to CCK+BC 6, CCK+DTI\n# to CCK+DTI 4, nine CCK+ to CCK+ pairs with trains (Fig. 10), heterogeneous pairs 2 each. Measured\n# variables: uIPSC 10 to 90% rise time, decay time constant, latency, amplitude (with failures),\n# potency (without failures), transmission probability, amplitudes normalized to the first IPSC,\n# asynchronous charge. Not paired recordings: current-step responses of 67 interneurons (40 features,\n# Tables 1 and 2, Fig. 2), connection testing of all filled pairs (Fig. 3, Table 3), spontaneous IPSCs\n# in PCs and interneurons (Fig. 12), local field potentials of SWRs in slices and optogenetic SWRs in\n# PV-Cre x ChR2 mice aged P60 to 300 in 450 um slices (Fig. 13). By its description the CRCNS data\n# set holds the paired recordings (raw pre- and postsynaptic sweeps and per-sweep amplitude and\n# success tables) of the eight connection types under the stimulation protocols above; it is not\n# described as holding the current-step, connectivity, spontaneous IPSC or field potential data.\n#\n# Shared method details, used by the criteria below.\n# M1. uIPSC measures (Methods, Electrophysiological recordings and analysis, paragraph 6; Fig. 4B\n#   legend): rise time, decay time constant, latency, potency and transmission probability on the\n#   averaged events excluding failures; amplitude on averaged events including failures; latency from\n#   the presynaptic AP peak to the uIPSC start, the start being the intersection of the baseline with\n#   a line fitted to the 10 to 90% rising phase; decay a single exponential fit to the decaying phase\n#   of the average; transmission probability the fraction of APs followed by a uIPSC.\n# M2. Failures. The paper does not say how a failure is scored. Readings: (a) the success and\n#   amplitude scored per sweep by the authors, as the data set's own tables hold them; (b) a\n#   detection on the raw sweeps, a uIPSC being a peak in the response window larger than three\n#   standard deviations of the pre-AP baseline (a standard choice, not the paper's).\n# M3. Which APs are \"single\" (Results, The type of interneuron determines the properties of uIPSCs\n#   onto PCs, paragraph 1; Fig. 4Ca; Fig. 8A legend). Readings: (a) the single AP that precedes the\n#   RIP train by 1000 ms (Methods, paragraph on protocols); (b) the ten APs of the 1 Hz train (the\n#   Fig. 8A legend shows uIPSCs \"triggered by 10 single action potentials\"); (c) both pooled.\n# M4. Amplitude in trains. The paper does not fix the window or baseline. Readings: (a) the per-sweep\n#   amplitudes of the data set's tables, averaged over sweeps; (b) the peak of the sweep-averaged\n#   trace in the interval from the AP to the next AP (or 10 ms after the last AP), measured from the\n#   current just before that AP. Relative amplitude is the mean amplitude at each AP divided by the\n#   mean amplitude of the first IPSC of the same train (Methods, paragraph 6), per pair; the group\n#   value is the median over pairs (Fig. 6C and 9B legends; Statistical analysis).\n# M5. Sweeps. The Methods say each pattern was repeated 10 (trains) or 10 or 20 times (RIP, EPI); the\n#   Results say 20 bursts were averaged. All sweeps of a protocol are used. The Fig. 5A legend speaks\n#   of a \"steady-state average\"; whether any first sweeps were left out is not said, so a variant\n#   leaving out the first three sweeps is shown where a criterion depends on sweep averages.\n# M6. Tests (Methods, Statistical analysis): Kruskal-Wallis across groups, post hoc Mann-Whitney U\n#   with Bonferroni correction; the number of comparisons is not given, so the factor is the number of\n#   pairwise comparisons among the groups of that panel (3 for three groups); Pearson chi-squared for\n#   connection probabilities. A threshold of p < 0.05 unless the claim states another.\n# M7. Tolerances. Values reported as median (first quartile, third quartile) use the paper's stated\n#   spread: the tolerance is the distance from the median to the nearer quartile, so the value holds\n#   when it falls within the reported interquartile range on that side. Other values use 10%.\nschema_version: 2\ndataset:\n  archive: crcns\n  id: hc-7\n  doi: 10.6080/K0MK69T5\npaper: doi:10.1113/jp272231\nclaims:\n- id: fig2b-pv-cck-clusters\n  statement: Hierarchical clustering of 67 CA3 interneurons on principal components of 40\n    electrophysiological features gives two clusters that match PV+ and CCK+ cells with more than\n    98% overlap; a single PV+ cell falls in the CCK+ cluster.\n  source: Results, Hierarchical clustering based on electrophysiological properties identifies\n    interneuron types, paragraphs 1 and 2; Figure 2B, left\n  quote: We found that the cells clearly formed two separate clusters based on their physiological\n    features ... the two main clusters corresponded almost perfectly to PV+ and CCK+ cells,\n    respectively, with only a single PV+ cell misplaced into the group of CCK+ cells. This resulted in\n    a more than 98% overlap between the anatomical and physiological classification\n  expected:\n  - quantity: agreement between the two clusters and the anatomical class\n    value: 98\n    tolerance: 2\n    unit: percent\n  criterion: Methods, Electrophysiological characterization and clustering of cell types. The 40\n    features of Tables 1 and 2 from the 800 ms current steps; PCA on the features, keeping the\n    components that carry most of the variance; hierarchical clustering with Euclidean distance and\n    Ward linkage, cut into two clusters. The paper does not say whether features were standardized\n    before PCA or how many components were kept (\"solutions involving different numbers of principal\n    components were tested\"). Readings, (a) z-scored features, components explaining 80% of the\n    variance; (b) z-scored features, components with eigenvalue above 1; (c) raw features, same two\n    rules. Reproduced when under one reading the two-cluster cut agrees with the PV+/CCK+ labels for\n    at least 98% of cells (at most one cell of 67 misplaced). The tolerance of 2 points is the step\n    between \"more than 98%\" and the next lower whole percent.\n- id: fig2b-pvbc-aac-clusters\n  statement: Reclustering the 26 PV+ cells gives two groups, one mostly PV+BCs (13 of 16) and one\n    mostly AACs (8 of 10), an overall match of about 83%.\n  source: Results, Hierarchical clustering based on electrophysiological properties identifies\n    interneuron types, paragraph 3; Figure 2B, right\n  quote: one cluster contained predominantly PV+BCs (13 of 16) and the other contained mainly AACs\n    (eight of 10), with an overall match of\n  expected:\n  - quantity: overall match of PV+ subclusters with PV+BC/AAC identity\n    value: 83\n    tolerance: 8.3\n    unit: percent\n  criterion: As fig2b-pv-cck-clusters, on the 26 PV+ cells alone, with the same readings. Reproduced\n    when under one reading the two-cluster cut matches the anatomical PV+BC/AAC labels for 75 to 91%\n    of cells (83% within 10%) with each cluster holding a majority of one type.\n  depends_on:\n  - fig2b-pv-cck-clusters\n- id: cck-no-subclusters\n  statement: Clustering the CCK+ cells reveals no well-separated subgroups matching CCK+BCs and\n    CCK+DTIs, which form a physiological continuum.\n  source: Results, Hierarchical clustering based on electrophysiological properties identifies\n    interneuron types, paragraph 4\n  quote: the branching structure of hierarchical clustering did not reveal any well-separated\n    clusters, and the clusters that could be defined did not show any correspondence to the two major\n    anatomical subclasses of CCK+ neurons\n  criterion: As fig2b-pv-cck-clusters, on the CCK+ cells alone, with the same readings. The paper\n    reports no test; the correspondence is judged by the agreement of a two-cluster cut with the\n    CCK+BC/CCK+DTI labels against the agreement of the larger class alone. Reproduced when under every\n    reading the agreement is no more than 10 points above the agreement given by assigning every cell\n    to the larger class.\n  depends_on:\n  - fig2b-pv-cck-clusters\n- id: table1-pv-cck-features\n  statement: PV+ and CCK+ interneurons differ in single-cell physiology; PV+ cells have a lower input\n    resistance, fire more APs at most and have narrower APs than CCK+ cells.\n  source: Results, Hierarchical clustering based on electrophysiological properties identifies\n    interneuron types, paragraph 2; Table 1\n  quote: PV+ and CCK+ neurons were significantly different from each other at the population level\n    according to several features, including input resistance, membrane time constant, the maximal\n    rate of firing for any input level ... (all P < 0.01, Mann-Whitney U test)\n  statistics:\n  - about: input resistance\n    test: Mann-Whitney U test\n    p: 0.001\n  - about: membrane time constant\n    test: Mann-Whitney U test\n    p: 0.002\n  - about: maximal AP number for any input current\n    test: Mann-Whitney U test\n    p: 1.5e-7\n  - about: AP half-width\n    test: Mann-Whitney U test\n    p: 1.4e-6\n  expected:\n  - quantity: input resistance, PV+\n    value: 55.64\n    tolerance: 11.68\n    unit: MOhm\n  - quantity: input resistance, CCK+\n    value: 107.89\n    tolerance: 43.55\n    unit: MOhm\n  - quantity: maximal AP number for any input current, PV+\n    value: 145.5\n    tolerance: 16.5\n  - quantity: maximal AP number for any input current, CCK+\n    value: 58.0\n    tolerance: 10.25\n  - quantity: AP half-width, PV+\n    value: 0.32\n    tolerance: 0.05\n    unit: ms\n  - quantity: AP half-width, CCK+\n    value: 0.50\n    tolerance: 0.10\n    unit: ms\n  criterion: Features as in Table 1, from the current-step responses (Methods, Electrophysiological\n    characterization and clustering of cell types); the feature definitions are those of an\n    unpublished script, so a feature is computed by the standard definition its name gives (input\n    resistance from the steady response to the small hyperpolarizing steps, half-width at half the\n    AP amplitude from threshold). Medians per class; two-sided Mann-Whitney U test. Reproduced when\n    every listed median is within tolerance (the nearer quartile, M7) and every listed test gives p\n    < 0.01 in the reported direction.\n- id: table2-pvbc-aac-features\n  statement: Morphologically identified PV+BCs and AACs differ in input resistance, rheobase, maximal\n    AP number, AP width and after-hyperpolarization; AACs have a higher input resistance, a lower\n    rheobase and fire more APs at most.\n  source: Results, Hierarchical clustering based on electrophysiological properties identifies\n    interneuron types, paragraph 3; Table 2\n  quote: Morphologically identified PV+BCs and AACs differed significantly in terms of input\n    resistance, rheobase current, maximal AP number, AP width, and duration and amplitude of AHP\n    (Table 2) (all P < 0.01, Mann-Whitney U test)\n  statistics:\n  - about: maximal AP number for any input current\n    test: Mann-Whitney U test\n    p: 0.001\n  - about: AP half-width\n    test: Mann-Whitney U test\n    p: 0.004\n  - about: AP width\n    test: Mann-Whitney U test\n    p: 0.007\n  expected:\n  - quantity: input resistance, PV+BC\n    value: 42.12\n    tolerance: 8.9\n    unit: MOhm\n  - quantity: input resistance, AAC\n    value: 79.47\n    tolerance: 9.29\n    unit: MOhm\n  - quantity: rheobase, PV+BC\n    value: 250\n    tolerance: 50\n    unit: pA\n  - quantity: rheobase, AAC\n    value: 100\n    tolerance: 15\n    unit: pA\n  - quantity: maximal AP number, PV+BC\n    value: 109\n    tolerance: 27.5\n  - quantity: maximal AP number, AAC\n    value: 162\n    tolerance: 7.5\n  criterion: As table1-pv-cck-features, for PV+BCs against AACs. Reproduced when every listed median\n    is within tolerance and input resistance, rheobase and maximal AP number differ in the reported\n    direction with Mann-Whitney p < 0.01. Table 2 prints some of the \"all P < 0.01\" features at P =\n    0.02 (AHP amplitude, new method) and 0.01 or more (AHP duration, old method); those are reported\n    and not judged.\n- id: fig3-cp-pv\n  statement: Connection probability is high among PV+ cells, 50% (22 of 44 pairs); 66.6% among\n    PV+BCs (20 of 30, six unidirectional and seven bidirectional pairs); PV+BCs contact AACs (2 of 4)\n    but AACs contact neither PV+BCs nor AACs, a highly significant difference.\n  source: Results, Frequency of interactions among homogeneous and heterogeneous types of\n    inhibitory neurons, paragraph 4; Figure 3A; Table 3\n  quote: From a total of 44 putative cell pairs (including PV+BCs and AACs), we found 22 pairs (CP =\n    50%). The CP among PV+BCs was 66.6% (six unidirectional and seven bidirectional pairs ... We\n    found two PV+BC to AAC pairs (CP = 50%). On the other hand, no AAC to PV+BC or AAC to AAC\n    connections were found. The difference in the likelihood with which PV+BCs and AACs contacted\n    other PV+ interneurons was highly significant (P = 6.21 × 10-4; chi-squared)\n  statistics:\n  - about: PV+BC against AAC as presynaptic partner of PV+ cells\n    test: Pearson's chi-squared test\n    p: 6.21e-4\n  expected:\n  - quantity: CP among PV+ cells\n    value: 50\n    tolerance: 5\n    unit: percent\n  - quantity: CP among PV+BCs\n    value: 66.6\n    tolerance: 6.66\n    unit: percent\n  - quantity: CP from PV+BC to AAC\n    value: 50\n    tolerance: 5\n    unit: percent\n  - quantity: CP from AAC to PV+ cells\n    value: 0\n    tolerance: 0\n    unit: percent\n  criterion: CP is the fraction of connected pairs among all tested unidirectional pairs whose\n    presynaptic axon was preserved (Results, same section, paragraph 3). Counts as in Figure 3A (22/44,\n    20/30, 2/4, 0/4, 0/6). Reproduced when the counts of tested and connected pairs give the\n    expected values and a Pearson chi-squared test of connected against unconnected, PV+BC against\n    AAC as presynaptic cell, gives p < 0.001. Needs the record of unconnected tested pairs.\n- id: fig3-cp-cck\n  statement: Connection probability among CCK+ cells is 28% (14 of 50), with frequent bidirectional\n    connections, but only within CCK+BCs (42.85%) and within CCK+DTIs (45.45%); none between the two\n    subtypes, a significant preference for the same partner type.\n  source: Results, Frequency of interactions among homogeneous and heterogeneous types of\n    inhibitory neurons, paragraph 5; Figure 3A; Table 3\n  quote: The CP between CCK+ cells was relatively high (28%), with frequent bidirectional\n    connections; however, we observed synaptic coupling only between homogeneous CCK+BC (CPCCK+BC =\n    42.85%) and CCK+DTI (CPCCK+DTI = 45.45%) pairs. The preference of CCK+ interneurons for\n    homologous postsynaptic partners was highly significant (P = 9.42 × 10-4)\n  statistics:\n  - test: Pearson's chi-squared test\n    p: 9.42e-4\n  expected:\n  - quantity: CP among CCK+ cells\n    value: 28\n    tolerance: 2.8\n    unit: percent\n  - quantity: CP among CCK+BCs\n    value: 42.85\n    tolerance: 4.29\n    unit: percent\n  - quantity: CP among CCK+DTIs\n    value: 45.45\n    tolerance: 4.55\n    unit: percent\n  - quantity: CP between CCK+BCs and CCK+DTIs, either direction\n    value: 0\n    tolerance: 0\n    unit: percent\n  criterion: As fig3-cp-pv; counts as in Figure 3A (14/50, 9/21, 5/11, 0/9, 0/9). The chi-squared\n    test compares connected against unconnected pairs for same-type against different-type pairs.\n    Reproduced when the expected values hold and p < 0.001.\n- id: fig3-cp-pv-cck\n  statement: Connections between PV+ and CCK+ interneurons are rare (2 of 14 in each direction);\n    interneurons connect preferentially within their main class, and PV+ cells preferentially target\n    PV+ cells over CCK+ cells.\n  source: Results, Frequency of interactions among homogeneous and heterogeneous types of\n    inhibitory neurons, paragraph 6; Figure 3A; Table 3\n  quote: From a total of 28 trials among PV+ and CCK+ cells, only two PV+ to CCK+ and two CCK+ to PV+\n    pairs were found. Overall, PV+ and CCK+ interneurons showed a greater probability of targeting\n    interneurons within the same main class (P = 0.0175) and PV+ cells in particular preferentially\n    targeted other PV+ interneurons\n  statistics:\n  - about: within against between main class\n    test: Pearson's chi-squared test\n    p: 0.0175\n  - about: PV+ presynaptic cells, PV+ against CCK+ targets\n    test: Pearson's chi-squared test\n    p: 0.0181\n  expected:\n  - quantity: CP from PV+ to CCK+\n    value: 14.3\n    tolerance: 1.43\n    unit: percent\n  - quantity: CP from CCK+ to PV+\n    value: 14.3\n    tolerance: 1.43\n    unit: percent\n  criterion: As fig3-cp-pv; 2/14 in each direction (Figure 3A). The two tests as described in the\n    quote, chi-squared on connected against unconnected pairs. Reproduced when the counts hold and\n    both tests give p < 0.05.\n- id: fig4b-in-pc-kruskal-wallis\n  statement: uIPSCs evoked in PCs by PV+BCs, AACs and CCK+BCs differ in 10 to 90% rise time,\n    latency, amplitude, synaptic potency and transmission probability.\n  source: Results, The type of interneuron determines the properties of uIPSCs onto PCs, paragraph\n    2; Figure 4B\n  quote: the three perisomatic region-targeting interneuron-evoked uIPSCs were different in 10-90%\n    rise time (Kruskal-Wallis ANOVA P = 0.027), latency (Kruskal-Wallis ANOVA - P = 7.49 × 10-4),\n    amplitude (Kruskal-Wallis ANOVA - P = 0.001), synaptic potency (Kruskal-Wallis ANOVA, P = 0.004)\n    and transmission probability (Kruskal-Wallis ANOVA - P = 0.003)\n  statistics:\n  - about: 10 to 90% rise time\n    test: Kruskal-Wallis ANOVA\n    p: 0.027\n    n: 8 PV+BC, 9 AAC and 14 CCK+BC to PC pairs\n  - about: latency\n    test: Kruskal-Wallis ANOVA\n    p: 7.49e-4\n  - about: amplitude\n    test: Kruskal-Wallis ANOVA\n    p: 0.001\n  - about: synaptic potency\n    test: Kruskal-Wallis ANOVA\n    p: 0.004\n  - about: transmission probability\n    test: Kruskal-Wallis ANOVA\n    p: 0.003\n  criterion: Pairs recorded with high KCl solution in both cells. Per pair, the measures of M1 on\n    single-AP uIPSCs (M3 readings a to c), failures by M2 readings a and b. Kruskal-Wallis across the\n    three presynaptic types for each measure. Reproduced when under one reading of M2 and M3 all five\n    measures give p < 0.05; partially reproduced when three or four do. The decay time constant was\n    not reported as different; its p is shown.\n- id: fig4b-in-pc-posthoc\n  statement: PV+BC and AAC uIPSCs onto PCs rise faster, have shorter latency and larger amplitude\n    than CCK+BC uIPSCs; AAC uIPSCs have larger potency, and higher transmission probability, than\n    CCK+BC uIPSCs.\n  source: Results, The type of interneuron determines the properties of uIPSCs onto PCs, paragraph\n    2; Figure 4B\n  quote: uIPSCs mediated by PV+BCs (n = 8) and AACs (n = 9) had a significantly faster 10-90% rise,\n    shorter latency and larger peak amplitude compared to CCK+BC-PC pairs (n = 14). Moreover, AAC-PC\n    pairs had a larger synaptic potency than CCK+BC-PC pairs, and CCK+BC-PC pairs had a significantly\n    smaller transmission probability than AAC-PC pairs\n  statistics:\n  - test: Mann-Whitney U test, post hoc\n    corrected: Bonferroni\n    p: 0.05\n    p_relation: \"<\"\n    n: 8 PV+BC, 9 AAC and 14 CCK+BC to PC pairs\n  criterion: As fig4b-in-pc-kruskal-wallis; post hoc two-sided Mann-Whitney U tests, Bonferroni\n    factor 3 (M6). Eight comparisons are claimed (PV+BC and AAC against CCK+BC for rise time, latency\n    and amplitude; AAC against CCK+BC for potency and for transmission probability). Reproduced when\n    under one reading of M2 and M3 all eight hold at corrected p < 0.05 in the stated direction;\n    partially reproduced when at least five do.\n  depends_on:\n  - fig4b-in-pc-kruskal-wallis\n- id: fig4c-cckdti-pc-silent-single-ap\n  statement: Seven of eight CCK+DTI to PC pairs transmit neither for a single AP nor for an AP after\n    a RIP burst; a single AP evokes a uIPSC only after an EPI burst.\n  source: Results, The type of interneuron determines the properties of uIPSCs onto PCs, paragraph\n    1; Figure 4Ca and Cb\n  quote: CCK+DTIs (seven of eight) did not transmit either for a single AP or for an AP following a\n    RIP protocol AP burst ... A single AP evoked transmission only if it was preceded by an EPI\n    burst-stimulation train\n  expected:\n  - quantity: CCK+DTI to PC pairs without uIPSCs to single APs\n    value: 7\n    tolerance: 0\n    unit: pairs of 8\n  criterion: For each CCK+DTI to PC pair, transmission probability of the single AP before the RIP\n    train and of the single AP before the EPI train (1600 ms after the previous EPI train), failures\n    by M2. A pair transmits when its transmission probability exceeds that seen in the same window\n    with no AP (the baseline crossing rate of reading b), or any success under reading a. Reproduced\n    when 7 of 8 pairs do not transmit to the single AP before RIP while at least one transmits to the\n    single AP that follows an EPI train. The tolerance is 0 as the claim is a count of pairs; if the\n    data set holds fewer pairs, the fraction is judged (at least 85% silent).\n- id: fig7a-cscl-kinetics\n  statement: Recording PCs with high CsCl (and interneurons with low KCl) gives longer 10 to 90%\n    rise times and latencies for all three perisomatic interneuron types than high KCl in both cells,\n    and larger amplitude and potency for CCK+BC to PC uIPSCs.\n  source: Results, The type of interneuron determines the properties of uIPSCs onto PCs, paragraph\n    3; Figure 7A\n  quote: all three types of PTI-mediated uIPSCs recorded on PCs with high CsCl-based intrapipette\n    solution had a significantly longer 10-90% rise time value and latency. Additionally, the\n    CsCl-based solution increased both the amplitude and synaptic potency of uIPSCs between\n    CCK+BC-PC pairs\n  statistics:\n  - test: Mann-Whitney U test, post hoc\n    p: 0.05\n    p_relation: \"<\"\n    n: high KCl 8 PV+BC, 9 AAC, 14 CCK+BC pairs; CsCl 9 PV+BC, 10 AAC, 6 CCK+BC pairs\n  criterion: Measures as fig4b-in-pc-kruskal-wallis, readings M2 and M3. For each presynaptic type,\n    two-sided Mann-Whitney U test of CsCl against high KCl pairs. The paper says \"post hoc\" without a\n    correction for this panel; readings, (a) uncorrected, (b) Bonferroni factor 3 (three cell types).\n    Reproduced when under one reading of M2, M3 and the correction, rise time and latency are longer\n    with CsCl in all three types and CCK+BC amplitude and potency are larger, at p < 0.05 (eight\n    comparisons); partially reproduced when at least five hold. Needs the pairs to be labelled by\n    pipette solution.\n- id: fig5c-pv-rip-depression\n  statement: Under the RIP protocol (four APs at 160 Hz) PV+BC to PC pairs show short-term\n    depression at the 3rd and 4th AP, and AAC to PC pairs already at the 2nd AP.\n  source: Results, Cell type-specific short-term plasticity characterizes the synaptic transmission\n    of interneurons onto PCs, paragraph 3 (Transmission of PV+ cells is depressing and homogenous);\n    Figure 5C\n  quote: PV+BC-PC pairs (n = 8) expressed short-term depression in response to the 3rd and 4th APs of\n    the RIP protocol, whereas AAC-PC pairs (n = 9) ) expressed short-term depression in response to\n    the 2nd AP\n  statistics:\n  - test: not named; asterisks in Figure 5C\n    p: 0.05\n    p_relation: \"<\"\n    n: 8 PV+BC and 9 AAC to PC pairs\n  criterion: High KCl pairs. Per pair, relative amplitudes of the four RIP IPSCs (M4 readings a and\n    b, M5), normalized to the first of the four. The paper does not name the test behind the Fig. 5C\n    asterisks. Readings, (a) Wilcoxon signed-rank test of the per-pair relative amplitude at AP n\n    against 1; (b) Mann-Whitney U test of the per-pair relative amplitudes at AP n against those at\n    AP 1 (all equal to 1), the paper's named two-group test. Reproduced when under one reading of\n    M4 and of the test, the PV+BC medians at the 3rd and 4th AP and the AAC median at the 2nd AP are\n    below 1 with p < 0.05. Whether the PV+BC 2nd AP is also depressed is reported.\n- id: fig5c-cck-rip-facilitation\n  statement: CCK+BC to PC (n = 14) and CCK+DTI to PC (n = 4) pairs on average show strong short-term\n    facilitation, although individual pairs can show either facilitation or depression.\n  source: Results, Cell type-specific short-term plasticity characterizes the synaptic transmission\n    of interneurons onto PCs, paragraph 5 (Transmission of CCK+ cells is variable); Figure 5C\n  quote: IPSCs between CCK+BC to PC (n = 14) and CCK+DTI-PC pairs (n = 4) on average were\n    characterized by powerful short-term facilitation; however, individual cell pairs could display\n    both short-term facilitation and short-term depression\n  criterion: As fig5c-pv-rip-depression, RIP protocol. Reproduced when for CCK+BC to PC pairs the\n    median relative amplitude at the 2nd to 4th AP is above 1 at two or more of the three APs, the\n    same holds for the CCK+DTI pairs that transmit under RIP, and at least one CCK+ pair has a\n    relative amplitude below 1 at the 4th AP. Pairs whose first IPSC is all failures under M2 cannot\n    be normalized and are counted apart.\n- id: fig5db-recovery\n  statement: After a RIP train, PV+BC to PC (n = 7) and AAC to PC (n = 9) transmission recovers\n    gradually with the interval to a second RIP train, while CCK+BC to PC transmission (n = 11) rises\n    and falls with the interval; PV+BC and CCK+BC pairs differ at several intervals.\n  source: Results, Cell type-specific short-term plasticity characterizes the synaptic transmission\n    of interneurons onto PCs, paragraph 4; Figure 5Da and Db\n  quote: PV+BC to PC (n = 7) and AAC to PC (n = 9) transmission gradually recovered, whereas CCK+BC to\n    PC transmission (n = 11) showed a more complex (increasing and decreasing) behaviour depending on\n    the interstimulus interval\n  statistics:\n  - about: PV+BC against CCK+BC to PC, recovery ratio at given intervals\n    test: not named; asterisks in Figure 5Db\n    p: 0.05\n    p_relation: \"<\"\n  criterion: Recovery ratio, the amplitude of the first IPSC of the second RIP train over that of the\n    first IPSC of the first train (Methods, paragraph on protocols; Fig. 5Db legend), per pair and\n    interval (50 to 1200 ms), amplitudes by M4. Gradual recovery, the median ratio over PV+BC pairs,\n    and over AAC pairs, rises with the interval (Spearman correlation of ratio with interval above 0\n    with p < 0.05 over the pair by interval values), below 1 at 50 ms. Complex behaviour, the CCK+BC\n    median ratio is not monotonic in interval (at least one rise followed by a fall of more than 10%\n    of the ratio). Difference, two-sided Mann-Whitney U test of PV+BC against CCK+BC at each\n    interval; the paper gives no correction (readings uncorrected and Bonferroni over 7 intervals).\n    Reproduced when all three parts hold under one reading of M4, with at least one interval\n    significant.\n- id: fig6-pv-trains-depression\n  statement: PV+BC to PC (n = 6) and AAC to PC (n = 8) pairs show purely short-term depression to 10\n    APs at 1 to 320 Hz and to the EPI protocol, more pronounced at higher frequencies, with IPSCs\n    synchronous to the APs even under EPI.\n  source: Results, Cell type-specific short-term plasticity characterizes the synaptic transmission\n    of interneurons onto PCs, paragraph 3; Figure 6A and C\n  quote: PV+BC to PC (n = 6) and AAC to PC (n = 8) pairs displayed purely short-term depression in\n    response to 10 APs at frequencies between 1 and 320 Hz and to our EPI protocol. The short-term\n    depression becomes more prominent with increasing frequency\n  criterion: Per pair and protocol, relative amplitudes (M4, M5); medians over pairs (Fig. 6C\n    legend). Purely depressing, the median relative amplitude of APs 2 to 10 is below 1 at every\n    frequency and for the EPI protocol, for each of the two types (a value up to 1.05 at a single AP\n    is allowed as noise, a standard choice). More prominent with frequency, the median over pairs of\n    the mean relative amplitude of APs 2 to 10 falls with frequency (Spearman correlation below 0 with\n    p < 0.05 over the pair by frequency values). Reproduced when both hold for both types under one\n    reading of M4.\n- id: fig6-cckbc-pc-trains\n  statement: All CCK+BC to PC pairs (n = 6) facilitate at 1 to 40 Hz; at 80 Hz and above and under\n    EPI the facilitation of the 1st to 5th APs turns into depression later in the train.\n  source: Results, Cell type-specific short-term plasticity characterizes the synaptic transmission\n    of interneurons onto PCs, paragraph 6; Figure 6A and C\n  quote: All CCK+BC-PC pairs (n = 6) were characterized by short-term facilitation at frequencies\n    between 1 and 40 Hz. At higher frequencies (80 Hz, 160 Hz, 320 Hz; EPI protocol) the transient\n    short-term facilitation of the 1st to 5th APs turned later into short-term depression\n  criterion: As fig6-pv-trains-depression. Facilitation at 1 to 40 Hz, for every pair the mean\n    relative amplitude of APs 2 to 10 is above 1 at each of 1, 5, 10, 20 and 40 Hz. At 80, 160 and\n    320 Hz and EPI, the median over pairs is above 1 at some AP from 2 to 5 and below 1 at the last\n    AP of the train. Reproduced when both hold under one reading of M4; partially reproduced when\n    facilitation holds for at least five of six pairs and the high-frequency pattern for at least\n    three of the four protocols.\n- id: fig6-cckbc-async-onset\n  statement: At CCK+BC to PC pairs asynchronous release appears only during the EPI protocol, between\n    the 10th and 19th AP (median 11, interquartile range 10 to 14).\n  source: Results, Cell type-specific short-term plasticity characterizes the synaptic transmission\n    of interneurons onto PCs, paragraph 6; Figure 6A\n  quote: Asynchronous release at CCK+BC-PCpairsappearedonlyduringtheEPIprotocol between the 10th and\n    19th AP [median (interquartile range) 11 (10-14)]\n  expected:\n  - quantity: AP index of asynchronous release onset, CCK+BC to PC, EPI\n    value: 11\n    tolerance: 1\n  criterion: The paper does not say how the onset of asynchronous release is determined. The\n    immediate asynchronous charge at each AP is computed as in the Methods (Asynchronous charge\n    calculation, a template from the averaged 11th IPSC, synchronous release reconstructed and\n    subtracted, 100 Hz low-pass, window the interval to the next AP). Readings for the onset, (a)\n    the first AP after which the immediate asynchronous charge stays above two standard deviations of\n    the charge in equal windows of the pre-train baseline for at least three APs; (b) the first AP\n    after which the current between APs no longer returns to within 10% of the IPSC peak of the\n    baseline (a standard choice). Reproduced when under one reading the median onset is 10 to 12 (11\n    against the nearer quartile 10, M7, and 10% above), onsets lie within 9 to 21 (10 to 19 widened by\n    10%), and no pair shows asynchronous release under the 10-AP trains by the same rule.\n- id: cckdti-pc-transmission\n  statement: Of eight CCK+DTI to PC pairs, four respond at low frequencies (1 to 40 Hz) or to RIP; in\n    these the first AP of trains evokes an IPSC only from about the fourth sweep, transmission\n    facilitates at 10 Hz but depresses at 40 and 160 Hz; the other four transmit, with depression,\n    only under EPI.\n  source: Results, Cell type-specific short-term plasticity characterizes the synaptic transmission\n    of interneurons onto PCs, paragraph 7; Figures 5A and 6A\n  quote: From a total of eight CCK+DTI-PC pairs, only four pairs responded to stimulation already at\n    low frequencies (1-40 Hz) or to RIP protocol with clearly distinguishable inhibitory transmission\n    ... the first AP of stimulation trains resulted in an IPSC starting from the fourthtraceonaverage\n    ... Transmission was characterized by short-term facilitation at 10 Hz (n = 3) but turned into\n    short-term depression at 40 Hz (n = 3) and 160 Hz (n = 4) stimulation. In the remaining four\n    CCK+DTI-PC pairs, inhibitory transmission (showing short-term depression) was observed only for\n    the stronger and longer lasting EPI stimulation train\n  expected:\n  - quantity: CCK+DTI to PC pairs transmitting at 1 to 40 Hz or RIP\n    value: 4\n    tolerance: 0\n    unit: pairs of 8\n  - quantity: first sweep with an IPSC to the first AP, mean over responding pairs\n    value: 4\n    tolerance: 0.4\n    unit: sweep index\n  criterion: Transmission per pair as in fig4c-cckdti-pc-silent-single-ap (M2), relative amplitudes\n    by M4. Reproduced when four of eight pairs transmit at 1 to 40 Hz or RIP, the mean first\n    successful sweep is within tolerance, and in the responding pairs the median mean relative\n    amplitude of APs 2 to 10 is above 1 at 10 Hz and below 1 at 40 and 160 Hz, while the other pairs\n    transmit only under EPI with the last-AP relative amplitude below 1. Partially reproduced when\n    the counts hold and the frequency pattern holds at two of the three frequencies.\n- id: cckdti-async-onset\n  statement: At CCK+DTI to PC pairs asynchronous release appears earlier than at CCK+BCs, between the\n    7th and 13th AP of the EPI protocol (median 7, interquartile range 7 to 9) and in trains at 160 Hz\n    and above (median 7, interquartile range 6 to 8).\n  source: Results, Cell type-specific short-term plasticity characterizes the synaptic transmission\n    of interneurons onto PCs, paragraph 8; Figure 6A and C\n  quote: In the CCK+DTIs, asynchronous release appeared earlier than for the CCK+BCs - between the 7th\n    and 13th AP of the EPI protocol [median (interquartile range) 7 (7-9)] and above 160 Hz stimulation\n    [median (interquartile range) 7 (6-8)]\n  expected:\n  - quantity: AP index of asynchronous release onset, CCK+DTI to PC, EPI\n    value: 7\n    tolerance: 0.7\n  - quantity: AP index of asynchronous release onset, CCK+DTI to PC, trains at 160 Hz and above\n    value: 7\n    tolerance: 1\n  criterion: Onset readings as fig6-cckbc-async-onset. For EPI the nearer quartile equals the median,\n    so the tolerance is 10%; for trains the nearer quartile (6) gives 1. \"Above 160 Hz\" is read two\n    ways, (a) the 160 and 320 Hz trains pooled, (b) the 320 Hz train alone. Reproduced when under\n    one reading both medians are within tolerance and the CCK+DTI EPI onset median is lower than the\n    CCK+BC one.\n  depends_on:\n  - fig6-cckbc-async-onset\n- id: async-charge-epi-vs-160\n  statement: At CCK+BC to PC pairs the EPI protocol triggers a larger asynchronous charge after the\n    last AP than 160 Hz trains, while the charge is unchanged between the two patterns at PV+BC, AAC\n    and CCK+DTI to PC pairs.\n  source: Results, Cell type-specific short-term plasticity characterizes the synaptic transmission\n    of interneurons onto PCs, paragraph 9; Figure 6A\n  quote: At CCK+BC-PC pairs, the EPI protocol triggered a significantly larger asynchronous charge\n    compared to 160 Hz stimulation (Mann-Whitney U test - P = 0.002), whereas the charge transfer at\n    PV+BC to PC (Mann-Whitney U test - P = 0.17) and AAC-PC pairs (Mann-Whitney U test - P = 0.27) was\n    unchanged between the two stimulus patterns. We did not find any significant difference in the\n    asynchronous charge transfer at CCK+DTI-PC pairs (Mann-Whitney U test - P = 0.9)\n  statistics:\n  - about: CCK+BC to PC, EPI against 160 Hz\n    test: Mann-Whitney U test\n    p: 0.002\n  - about: PV+BC to PC, EPI against 160 Hz\n    test: Mann-Whitney U test\n    p: 0.17\n  - about: AAC to PC, EPI against 160 Hz\n    test: Mann-Whitney U test\n    p: 0.27\n  - about: CCK+DTI to PC, EPI against 160 Hz\n    test: Mann-Whitney U test\n    p: 0.9\n  criterion: Charge in the 500 ms window after the last AP of the EPI protocol and of the 10-AP 160\n    Hz train (paragraph 9). The paper says asynchronous charge; readings, (a) the delayed asynchronous\n    charge of the Methods (the 100 Hz low-pass original trace minus the reconstructed synchronous\n    trace, 500 ms after the last AP); (b) the area under the mean trace in that window minus the area\n    of an equal window at least 500 ms later (the total charge method of the Methods, applied to the\n    window). Two-sided Mann-Whitney U test per type, EPI against 160 Hz, as the paper names it.\n    Reproduced when under one reading CCK+BC gives p < 0.05 with EPI larger, and the absence parts\n    hold on the paper's test, PV+BC, AAC and CCK+DTI each p >= 0.05; partially reproduced when\n    CCK+BC holds and one absence part fails.\n- id: decay-epi-vs-160\n  statement: The decay time constant after the last AP lengthens under EPI compared with 160 Hz\n    trains, from 13.01 to 103.65 ms at CCK+BC to PC pairs and from 36.82 to 138.71 ms at CCK+DTI to PC\n    pairs.\n  source: Results, Cell type-specific short-term plasticity characterizes the synaptic transmission\n    of interneurons onto PCs, paragraph 9; Figure 6B\n  quote: the decay time (τ) of release prolonged significantly during EPI protocol compared to 160 Hz\n    stimulation at both CCK+BC-PC (from 13.01 ms to 103.65 ms; Mann-WhitneyUtest - P =0.01) and\n    CCK+DTI-PC pairs (from 36.82 ms to 138.71 ms; Mann-Whitney U test - P = 0.01)\n  statistics:\n  - about: CCK+BC to PC\n    test: Mann-Whitney U test\n    p: 0.01\n  - about: CCK+DTI to PC\n    test: Mann-Whitney U test\n    p: 0.01\n  expected:\n  - quantity: decay time constant after 10th AP at 160 Hz, CCK+BC to PC, median\n    value: 13.01\n    tolerance: 1.3\n    unit: ms\n  - quantity: decay time constant after last EPI AP, CCK+BC to PC, median\n    value: 103.65\n    tolerance: 10.37\n    unit: ms\n  - quantity: decay time constant after 10th AP at 160 Hz, CCK+DTI to PC, median\n    value: 36.82\n    tolerance: 3.68\n    unit: ms\n  - quantity: decay time constant after last EPI AP, CCK+DTI to PC, median\n    value: 138.71\n    tolerance: 13.87\n    unit: ms\n  criterion: Per pair, a single exponential fitted to the decay of the averaged current after the\n    10th AP of the 160 Hz train and after the last AP of the EPI protocol (Fig. 6A legend), medians\n    over pairs (Fig. 6B legend). The fit window is not given; readings, (a) from the peak to 500 ms\n    after the last AP (the window of the charge analysis); (b) from the peak to the return to\n    baseline, the first point within 5% of the peak above baseline. Two-sided Mann-Whitney U test,\n    EPI against 160 Hz. Reproduced when under one reading the four medians are within tolerance and\n    both tests give p < 0.05; partially reproduced when both tests hold with EPI longer but some\n    medians fall outside tolerance. Fig. 6B also reports PV+BC and AAC values (asterisks on CCK+BC and\n    \"PTI\"), not given in the text; these are shown and not judged.\n- id: fig7b-cscl-stp\n  statement: With the CsCl (postsynaptic) and low KCl (presynaptic) solutions short-term depression\n    at the 3rd and 4th RIP APs is larger at AAC to PC pairs, and short-term facilitation is smaller at\n    CCK+BC to PC pairs, than with high KCl.\n  source: Results, Cell type-specific short-term plasticity characterizes the synaptic transmission\n    of interneurons onto PCs, paragraph 11; Figure 7B\n  quote: The use of different intrapipette solutions significantly increased the short-term\n    depression between AACs and PCs, and decreased the short-term facilitation of CCK+BC-PC pairs,\n    compared to values of short-term plasticity observed with high KCl-based intrapipette solution\n  statistics:\n  - test: not named; asterisks in Figure 7B\n    p: 0.05\n    p_relation: \"<\"\n  criterion: RIP relative amplitudes (M4) at the 3rd and 4th AP (Fig. 7B legend), per pair, CsCl\n    pairs against high KCl pairs, two-sided Mann-Whitney U test per type and AP (the paper's\n    two-group test). Reproduced when under one reading of M4 the AAC relative amplitudes are lower\n    with CsCl at the 3rd and 4th AP and the CCK+BC relative amplitudes are lower with CsCl at the 3rd\n    and 4th AP, each p < 0.05; partially reproduced when two or three of the four hold. Needs the pairs\n    to be labelled by pipette solution.\n  depends_on:\n  - fig7a-cscl-kinetics\n- id: fig8-pvbc-pvbc-uipsc\n  statement: uIPSCs between PV+BCs (n = 16) are fast (10 to 90% rise time 0.63 ms, decay time\n    constant 3.17 ms), with short latency (0.76 ms), large amplitude (81.18 pA) and transmission\n    probability of 1.\n  source: Results, Properties of uIPSCs among interneurons are also connection type specific,\n    paragraph 2; Figure 8B\n  quote: uIPSCs at PV+BC to PV+BC pairs (n = 16) were fast (10-90% rise time, 0.63 ms; decay time\n    constant, 3.17 ms) with short latency (0.76 ms), large amplitude (81.18 pA) and high transmission\n    probability (P = 1)\n  expected:\n  - quantity: 10 to 90% rise time, median\n    value: 0.63\n    tolerance: 0.063\n    unit: ms\n  - quantity: decay time constant, median\n    value: 3.17\n    tolerance: 0.317\n    unit: ms\n  - quantity: latency, median\n    value: 0.76\n    tolerance: 0.076\n    unit: ms\n  - quantity: amplitude, median\n    value: 81.18\n    tolerance: 8.12\n    unit: pA\n  - quantity: transmission probability, median\n    value: 1.0\n    tolerance: 0.1\n  criterion: Measures of M1, single APs by M3 (the Fig. 8A legend favours reading b, the 1 Hz train),\n    failures by M2, median over pairs (Fig. 8B legend). Reproduced when under one reading of M2 and\n    M3 all five medians are within tolerance; partially reproduced when three or four are.\n- id: fig8-cck-pairs-uipsc\n  statement: uIPSCs between CCK+BCs (n = 6) have rise and decay times like those between PV+BCs\n    (0.63 and 3.65 ms) but significantly longer latency (1.59 ms) and lower transmission probability\n    (0.7); uIPSCs between CCK+DTIs (n = 4) are slowest (rise 0.98 ms, decay 4.47 ms, latency 1.52 ms),\n    smallest (43.71 pA) and least reliable (0.55).\n  source: Results, Properties of uIPSCs among interneurons are also connection type specific,\n    paragraph 2; Figure 8B\n  quote: The properties of inhibitory synapses among CCK+BCs (n = 6) were similar to PV+BC to PV+BC\n    synapses with respect to the 10-90% rise time (0.63 ms) and decay time constant (3.65 ms); however,\n    uIPSCs were evoked with a significantly longer latency (1.59 ms) and lower transmission\n    probability (P = 0.7). Finally, we found that synapses between CCK+DTI pairs (n = 4) had the\n    slowest time course of rise time (0.98 ms), decay time (4.47 ms) and latency (1.52 ms), with the\n    smallest amplitude (43.71 pA) and lowest transmission probability (0.55)\n  statistics:\n  - about: CCK+BC against PV+BC pairs, latency and transmission probability\n    test: Mann-Whitney U test, post hoc\n    corrected: Bonferroni\n    p: 0.05\n    p_relation: \"<\"\n    n: 16 PV+BC, 6 CCK+BC and 4 CCK+DTI pairs\n  expected:\n  - quantity: CCK+BC pairs, 10 to 90% rise time\n    value: 0.63\n    tolerance: 0.063\n    unit: ms\n  - quantity: CCK+BC pairs, decay time constant\n    value: 3.65\n    tolerance: 0.365\n    unit: ms\n  - quantity: CCK+BC pairs, latency\n    value: 1.59\n    tolerance: 0.159\n    unit: ms\n  - quantity: CCK+BC pairs, transmission probability\n    value: 0.7\n    tolerance: 0.07\n  - quantity: CCK+DTI pairs, 10 to 90% rise time\n    value: 0.98\n    tolerance: 0.098\n    unit: ms\n  - quantity: CCK+DTI pairs, decay time constant\n    value: 4.47\n    tolerance: 0.447\n    unit: ms\n  - quantity: CCK+DTI pairs, latency\n    value: 1.52\n    tolerance: 0.152\n    unit: ms\n  - quantity: CCK+DTI pairs, amplitude\n    value: 43.71\n    tolerance: 4.37\n    unit: pA\n  - quantity: CCK+DTI pairs, transmission probability\n    value: 0.55\n    tolerance: 0.055\n  criterion: As fig8-pvbc-pvbc-uipsc. Kruskal-Wallis across the three pair types, post hoc\n    Mann-Whitney U with Bonferroni factor 3 (M6). Reproduced when under one reading of M2 and M3 at\n    least seven of the nine medians are within tolerance and CCK+BC pairs have a longer latency and\n    lower transmission probability than PV+BC pairs at corrected p < 0.05; partially reproduced when\n    the tests hold and four to six medians are within tolerance. With six and four pairs, the\n    corrected Mann-Whitney test can reach p < 0.05 only with complete separation; the uncorrected p\n    is also shown.\n  depends_on:\n  - fig8-pvbc-pvbc-uipsc\n- id: fig8-cckbc-vs-cckdti-pairs\n  statement: Among CCK+ pairs, uIPSC decay, latency, amplitude and transmission probability are\n    similar between CCK+BC and CCK+DTI pairs, but CCK+BC uIPSCs rise significantly faster.\n  source: Results, Properties of uIPSCs among interneurons are also connection type specific,\n    paragraph 2; Figure 8B\n  quote: The decay time constant, latency, amplitude and transmission probability of uIPSCs among\n    CCK+BC and CCK+DTI pairs were similar, although the 10-90% rise time of uIPSCs mediated by\n    CCK+BCs was significantly faster compared to CCK+DTI pairs\n  statistics:\n  - about: 10 to 90% rise time, CCK+BC against CCK+DTI pairs\n    test: Mann-Whitney U test, post hoc\n    corrected: Bonferroni\n    p: 0.05\n    p_relation: \"<\"\n  criterion: As fig8-cck-pairs-uipsc, post hoc Mann-Whitney U test with Bonferroni factor 3. The\n    similarity is a claim of absence, judged on that test at corrected p < 0.05. Reproduced when the\n    rise time differs (CCK+BC faster) and decay, latency, amplitude and transmission probability do\n    not; partially reproduced when the rise time holds and one of the four absences fails. Under\n    the stated correction a 6 against 4 Mann-Whitney test has a smallest two-sided p of 0.0095, times\n    3 is 0.029, so complete separation is needed for the rise time.\n  depends_on:\n  - fig8-cck-pairs-uipsc\n- id: fig9-pvbc-pvbc-depression\n  statement: Transmission between PV+BCs (n = 13) depresses during 10-AP trains at all frequencies\n    from 1 to 320 Hz, more strongly at higher frequencies.\n  source: Results, Short-term depression among PV+BC pairs is frequency-dependent, paragraph 2;\n    Figure 9B, left\n  quote: The transmission was characterized by short-term depression (Fig. 9B); the amplitude of\n    triggered IPSCs decreased during the train of 10 APs at all frequencies. Moreover, as shown in Fig.\n    9, the short-term depression became more prominent as the frequency ofstimulation was increased\n  criterion: As fig6-pv-trains-depression, for PV+BC to PV+BC pairs (M4, M5). Reproduced when under\n    one reading of M4 the median relative amplitude at the 10th AP is below 1 at all eight frequencies\n    and the median mean relative amplitude of APs 2 to 10 falls with frequency (Spearman correlation\n    below 0, p < 0.05, over pair by frequency values).\n- id: fig9-pvbc-pvbc-transmission-probability\n  statement: Between PV+BCs the transmission probability starts to fall at 80 Hz (to 0.9 at the 10th\n    AP), falls by 5 to 10% at the 8th to 10th AP at 160 Hz, and lies between 0.8 and 0.9 from the 3rd\n    to the 10th AP at 320 Hz; it recovers by the 11th AP.\n  source: Results, Short-term depression among PV+BC pairs is frequency-dependent, paragraph 2;\n    Figure 9B, right\n  quote: the transmission probability started to decrease at 80 Hz stimulation (at the 10th AP to 0.9;\n    fast gamma frequency range). Increasing the frequency of stimulation to 160 Hz (SWR frequency\n    range), we observed a 5-10% decrease of transmission probability at the 8th to 10th AP, whereas,\n    at 320 Hz stimulation, the inhibitory transmission became less effective between the 3rd and 10th\n    AP (transmission probability between 0.8 and 0.9)\n  expected:\n  - quantity: transmission probability at the 10th AP, 80 Hz, median over pairs\n    value: 0.9\n    tolerance: 0.09\n  - quantity: decrease of transmission probability at the 8th to 10th AP, 160 Hz\n    value: 7.5\n    tolerance: 3.25\n    unit: percent\n  - quantity: transmission probability at the 3rd to 10th AP, 320 Hz, median over pairs\n    value: 0.85\n    tolerance: 0.14\n  criterion: Per pair and AP, the fraction of sweeps with a uIPSC (M2), median over pairs (Fig. 9B\n    legend). The 160 Hz decrease is read relative to the first AP; the reported range 5 to 10% widened\n    by 10% of each bound gives 4.5 to 11 (7.75 plus or minus 3.25). The 320 Hz range 0.8 to 0.9\n    widened gives 0.72 to 0.99 for every AP from the 3rd to the 10th. Below 80 Hz the median is 1 at\n    every AP. Reproduced when under one reading of M2 all hold and the 11th AP median is at least\n    0.95 at every frequency; partially reproduced when the 80 Hz and 320 Hz parts hold.\n  depends_on:\n  - fig9-pvbc-pvbc-depression\n- id: fig9-pvbc-pvbc-recovery-11th\n  statement: Between PV+BCs a 1 s pause does not fully relieve depression, and the recovery of the\n    11th IPSC does not depend on the frequency of the preceding train.\n  source: Results, Short-term depression among PV+BC pairs is frequency-dependent, paragraph 3;\n    Figure 9B, left\n  quote: The 1 s interstimulus interval was not sufficient to completely recover synaptic depression\n    and the level of recovery was similar, regardless of the previous train frequency (Kruskal-Wallis\n    ANOVA - P = 0.152)\n  statistics:\n  - test: Kruskal-Wallis ANOVA\n    p: 0.152\n    n: 13 PV+BC to PV+BC pairs, trains at 5 to 320 Hz\n  criterion: Per pair, the 11th IPSC amplitude over the first (M4), for trains at 5 to 320 Hz\n    (paragraph 3). Incomplete recovery, the median over pairs is below 1 at every frequency. Absence\n    of a frequency effect, Kruskal-Wallis across the seven frequencies on the per-pair values, as the\n    paper did (groups treated as independent though the pairs repeat), not significant at p < 0.05.\n    A Friedman test over pairs with all frequencies is shown as a variant. Reproduced when both hold.\n  depends_on:\n  - fig9-pvbc-pvbc-depression\n- id: fig10-cck-cck-heterogeneity\n  statement: Transmission between CCK+ cells is heterogeneous; all connections facilitate, four of\n    nine pairs release only synchronously while five show frequency-dependent strong asynchronous\n    release, and both BC and DTI pairs show either pattern.\n  source: Results, Interactions among CCK+ interneurons show heterogeneous dynamics regardless of\n    axonal location, paragraphs 2 and 3; Figure 10Aa to Ac\n  quote: Although short-term facilitation was a common feature of all connections, four out of nine\n    cells evoked only synchronous transmitter release (Fig. 10Aa), whereas five of them showed a\n    frequency-dependent strong asynchronous release (Fig. 10Ab). Both BCs and DTIs could show either\n    of these patterns\n  expected:\n  - quantity: CCK+ to CCK+ pairs with only synchronous release\n    value: 4\n    tolerance: 0\n    unit: pairs of 9\n  - quantity: CCK+ to CCK+ pairs with asynchronous release\n    value: 5\n    tolerance: 0\n    unit: pairs of 9\n  criterion: CCK+BC to CCK+BC and CCK+DTI to CCK+DTI pairs, 10-AP trains. Asynchronous release in a\n    pair is judged by the onset rule of fig6-cckbc-async-onset (both readings) at 40 Hz and above\n    (paragraph 4 places its appearance after the 5th AP at 40 and 160 Hz). Reproduced when under one\n    reading four pairs show none and five show it (if the data set holds a different number of pairs,\n    when the fraction with asynchronous release is 45 to 66%, 5 of 9 within 10% of each count), both\n    types are among each group, and every pair has a relative amplitude above 1 at some AP of the 10\n    or 40 Hz train.\n  depends_on:\n  - fig6-cckbc-async-onset\n- id: fig10-cck-cck-frequency\n  statement: Between CCK+ cells IPSC amplitudes facilitate at 10 and 40 Hz, while at 160 Hz they show\n    no consistent change or a mixture of depression and facilitation.\n  source: Results, Interactions among CCK+ interneurons show heterogeneous dynamics regardless of\n    axonal location, paragraph 3; Figure 10Ac\n  quote: the amplitude of evoked IPSCs among CCK+ cells displayed short-term facilitation at 10 and\n    40 Hz stimulation. On the other hand, the amplitude of individual IPSCs at 160 Hz stimulation was\n    characterized by no consistent change or by a mixture of short-term depression and short-term\n    facilitation\n  criterion: Relative amplitudes (M4, M5) per pair. Reproduced when under one reading of M4 the median\n    over pairs of the mean relative amplitude of APs 2 to 10 is above 1 at 10 and at 40 Hz, and at 160\n    Hz the pairs are mixed (at least one pair above 1 and one below 1) or the median is within 0.9 to\n    1.1.\n- id: fig10-cck-cck-async\n  statement: In the five CCK+ pairs with asynchronous release, release is synchronous at 10 Hz but\n    asynchronous after the 5th AP at 40 and 160 Hz, and persists after the train for 69.8 to 339.6 ms,\n    a duration independent of frequency; the total charge depends on the presynaptic frequency.\n  source: Results, Interactions among CCK+ interneurons show heterogeneous dynamics regardless of\n    axonal location, paragraph 4; Figure 10Ac and Ad\n  quote: In five CCK+ to CCK+ cell pairs, transmitter release was synchronous at 10 Hz stimulation\n    but, at 40 and 160 Hz stimulation, asynchronous release appeared after the 5th AP (immediate\n    asynchronous release). This asynchronous release persisted after the end of stimulation train,\n    lasting 69.8-339.6 ms for different cells (delayed asynchronousrelease).Itsdurationwasindependentofthe\n    frequency of stimulation train (data not shown). However, the total inhibitory charge during the\n    stimulation train (including a 500 ms window following the end of the 10th ... AP) was determined\n    by the frequency of presynaptic APs\n  expected:\n  - quantity: duration of delayed asynchronous release, range over pairs, shortest\n    value: 69.8\n    tolerance: 6.98\n    unit: ms\n  - quantity: duration of delayed asynchronous release, range over pairs, longest\n    value: 339.6\n    tolerance: 33.96\n    unit: ms\n  criterion: For the pairs with asynchronous release (fig10-cck-cck-heterogeneity). Onset by the rule\n    of fig6-cckbc-async-onset. Duration of delayed release, the time from the last AP to the point\n    where the low-pass (100 Hz) residual current (original minus reconstructed synchronous, Methods)\n    returns within two standard deviations of baseline, a standard choice the paper does not state.\n    Total charge as the Methods define it (area under the mean trace during the train and 500 ms\n    after, minus an equal window at least 500 ms later). Frequency dependence of total charge,\n    Kruskal-Wallis across 10 to 320 Hz at p < 0.05 (the paper's test for several groups); duration\n    independent of frequency, the same test not significant. Reproduced when under one reading the\n    onset is after the 5th AP at 40 and 160 Hz and absent at 10 Hz in at least four of five pairs,\n    the durations lie within 62.8 to 373.6 ms (the range widened by 10% of each bound), and both tests\n    go as stated.\n  depends_on:\n  - fig10-cck-cck-heterogeneity\n- id: fig10bd-be-async-charge\n  statement: Between CCK+ cells immediate asynchronous charge per AP rises from 10 to 40 Hz, starting\n    near the 5th AP, and falls at higher frequencies; delayed asynchronous charge grows with frequency\n    and saturates at 160 Hz.\n  source: Results, Interactions among CCK+ interneurons show heterogeneous dynamics regardless of\n    axonal location, paragraph 5; Figure 10Bd and Be\n  quote: immediate asynchronous charge increased with increasing frequency between 10 and 40 Hz,\n    starting around the 5th AP. However, at higher frequencies, immediate asynchronous charge started\n    to drop ... delayed asynchronous charge strongly potentiated in a frequency-dependent manner, and\n    saturated at 160 Hz\n  criterion: Methods, Asynchronous charge calculation. Template, a difference of two exponentials\n    (Eq. 6) fitted to the average of all 11th IPSCs; delay from the rise onset; the synchronous trace\n    rebuilt by adding templates at each AP plus the delay, scaled to the averaged IPSC amplitude at\n    that AP; original and rebuilt traces low-pass filtered at 100 Hz; immediate charge per AP over the\n    interval to the next AP (100, 50, 25, 12.5, 6.25, 3.125 ms at 10 to 320 Hz); delayed charge in the\n    500 ms after the 10th AP. The filter type and order are not given; a standard choice (fourth-order\n    zero-phase Butterworth) is used and named. Median over pairs with asynchronous release. Reproduced\n    when the median immediate charge summed over APs 5 to 10 is larger at 40 than at 10 Hz and smaller\n    at 320 than at 40 Hz, and the median delayed charge rises from 10 to 160 Hz (each step not lower\n    than the previous by more than 10%) with 320 Hz within 20% of 160 Hz.\n  depends_on:\n  - fig10-cck-cck-heterogeneity\n- id: fig11-model-pv-udr\n  statement: For PV+BC to PV+BC, PV+BC to PC and AAC to PC connections a purely depressing\n    Tsodyks-Markram model fits adequately; adding use-dependent replenishment lowers the summed\n    squared error by 35%, 22% and 34%, while adding facilitation gives no significant improvement; the\n    BIC favours the depressing model with use-dependent replenishment.\n  source: Results, Simple mathematical models of short-term plasticity effectively capture the\n    temporal properties of transmission, paragraphs 3 and 5; Figure 11A and B\n  quote: the combined sum of squared error decreased by 35% for PV+BC to PV+BC connections, by 22% for\n    PV+BC to PC connections, and by 34% for AAC to PC connections when use-dependent replenishment was\n    assumed). Adding synaptic facilitation to the model did not lead to any significant improvement\n    for these three types of connection ... The BIC clearly favoured the purely depressing model which\n    included use-dependent replenishment for PV+BC to PV+BC, PV+BC to PC and AAC to PC connections\n  expected:\n  - quantity: decrease of combined SSE with UDR, PV+BC to PV+BC\n    value: 35\n    tolerance: 3.5\n    unit: percent\n  - quantity: decrease of combined SSE with UDR, PV+BC to PC\n    value: 22\n    tolerance: 2.2\n    unit: percent\n  - quantity: decrease of combined SSE with UDR, AAC to PC\n    value: 34\n    tolerance: 3.4\n    unit: percent\n  criterion: Methods, Modelling the short-term plasticity, Eqs. 1 to 5; Results, same section,\n    paragraph 3; Table 4 legend. Data, per connection the mean IPSC amplitudes (pA, M4) of the 10-AP\n    trains at 1 to 320 Hz with the 11th AP, all frequencies fitted together. Four models, TM\n    depressing (Eqs. 1, 5), TM depressing plus facilitating (Eqs. 1, 2, 5), UDR depressing (Eqs. 1, 3,\n    4, 5), UDR plus facilitation; n = 1 and p = p0 before the first spike. U0 (p0), tau_f and Imax are\n    fitted per connection, the other parameters (tau_r, tau_e, a_e, k_e) jointly per connection type\n    (Table 4 legend; Fig. 11C legend). Not stated, and so open, the optimizer, the error weighting and\n    the BIC's form. Readings, (a) unweighted sum of squared errors in pA squared over all APs and\n    connections, BIC = N ln(SSE/N) + k ln N with N the number of fitted amplitudes and k the number of\n    free parameters; (b) the same with each connection's errors divided by its first-IPSC amplitude\n    squared. Fits started from several initial points (a standard choice). The SSE decrease is 1 minus\n    SSE(UDR depressing)/SSE(TM depressing), per type. Reproduced when under one reading the three\n    decreases are within tolerance, the lowest BIC is the UDR depressing model for all three types,\n    and adding facilitation to UDR lowers the SSE by less than 10%; partially reproduced when the BIC\n    ranking holds and the decreases lie within 10 to 50%.\n- id: fig11-model-cck-facilitation\n  statement: CCK+BC to PC connections are best fitted by a Tsodyks-Markram model with depression and\n    significant facilitation, better than the purely depressing model; use-dependent replenishment\n    does not improve the fit, and the BIC favours the depressing-facilitating model.\n  source: Results, Simple mathematical models of short-term plasticity effectively capture the\n    temporal properties of transmission, paragraphs 4 and 5; Figure 11A and B\n  quote: The parameters of the best-fitting Tsodyks-Markram model indicated a significant degree of\n    synaptic facilitation, and showed a better fit than the purely depressing model (Fig. 11B and C).\n    On the other hand, allowing the replenishment of resources to be use-dependent did not lead to a\n    better fit for these connections ... the depressing-facilitating model (without use-dependent\n    replenishment) provided the best fit for CCK+BC to PC connections\n  criterion: As fig11-model-pv-udr, for CCK+BC to PC connections (CCK+DTI to PC pairs were not\n    modelled, paragraph 4). Reproduced when under one reading the lowest BIC is the TM depressing plus\n    facilitating model and its SSE is lower than that of the TM depressing model.\n  depends_on:\n  - fig11-model-pv-udr\n- id: table4-model-parameters\n  statement: The best-fitting models give per-connection medians of U0 0.31, 0.33 and 0.26 and Imax\n    410, 289 and 646 pA for PV+BC to PV+BC, PV+BC to PC and AAC to PC, and for CCK+BC to PC U0 0.15,\n    tau_f 10.9 and Imax 499 pA, with type parameters tau_r 1.08, 1.62, 1.70 and 12.9 s.\n  source: Table 4; Figure 11 legend\n  inferred: Numbers from Table 4 and the Figure 11 legend; no sentence of the Results states them.\n    The CCK+BC column assignment (U0, tau_f, Imax) is read from the table header, as the extracted\n    text lost the empty cells.\n  expected:\n  - quantity: U0, PV+BC to PV+BC\n    value: 0.31\n    tolerance: 0.03\n  - quantity: Imax, PV+BC to PV+BC\n    value: 410\n    tolerance: 140\n    unit: pA\n  - quantity: U0, PV+BC to PC\n    value: 0.33\n    tolerance: 0.09\n  - quantity: Imax, PV+BC to PC\n    value: 289\n    tolerance: 36\n    unit: pA\n  - quantity: U0, AAC to PC\n    value: 0.26\n    tolerance: 0.04\n  - quantity: Imax, AAC to PC\n    value: 646\n    tolerance: 182\n    unit: pA\n  - quantity: U0, CCK+BC to PC\n    value: 0.15\n    tolerance: 0.03\n  - quantity: tau_f, CCK+BC to PC\n    value: 10.9\n    tolerance: 3.7\n    unit: ms\n  - quantity: Imax, CCK+BC to PC\n    value: 499\n    tolerance: 209\n    unit: pA\n  - quantity: tau_r, PV+BC to PV+BC\n    value: 1.08\n    tolerance: 0.108\n    unit: s\n  - quantity: tau_r, PV+BC to PC\n    value: 1.62\n    tolerance: 0.162\n    unit: s\n  - quantity: tau_r, AAC to PC\n    value: 1.70\n    tolerance: 0.17\n    unit: s\n  - quantity: tau_r, CCK+BC to PC\n    value: 12.9\n    tolerance: 1.29\n    unit: s\n  criterion: Fits as fig11-model-pv-udr with the best model per type (UDR depressing for the three PV+\n    types; TM depressing plus facilitating for CCK+BC to PC). The tau_r values are those of the Figure\n    11 legend, which gives them for the most comprehensive model; for the best models the extracted\n    Table 4 lost them, so tau_r is judged in the comprehensive model. Table 4 prints tau_f in ms\n    while the Results say tau_f is larger for CCK+BC than for PV+ connections; the unit is taken as\n    printed. Reproduced when under one reading at least 10 of the 13 values are within tolerance;\n    partially reproduced when at least 6 are.\n  depends_on:\n  - fig11-model-pv-udr\n  - fig11-model-cck-facilitation\n- id: fig11c-parameter-differences\n  statement: In the most comprehensive model the per-connection parameters differ between connection\n    types; tau_f is larger for CCK+BC to PC than for all PV+ connections, U0 is smaller for CCK+BC to\n    PC than for PV+BC to PV+BC and PV+BC to PC, and Imax is smaller for PV+BC to PC than for the other\n    three types.\n  source: Results, Simple mathematical models of short-term plasticity effectively capture the\n    temporal properties of transmission, paragraph 6; Figure 11C\n  quote: the values of all parameters for which cell-specific or run-specific values were fitted\n    showed connection type-specific differences (Kruskal-Wallis ANOVA; P = 0.0021 for U0, P = 0.0012\n    for τf and P = 5.8 × 10-7 for Imax)\n  statistics:\n  - about: U0\n    test: Kruskal-Wallis ANOVA\n    p: 0.0021\n  - about: tau_f\n    test: Kruskal-Wallis ANOVA\n    p: 0.0012\n  - about: Imax\n    test: Kruskal-Wallis ANOVA\n    p: 5.8e-7\n  - about: tau_f, CCK+BC to PC against AAC to PC\n    test: post hoc comparison\n    p: 0.001\n    p_relation: \"<\"\n  - about: tau_f, CCK+BC to PC against PV+BC to PC\n    test: post hoc comparison\n    p: 0.01\n    p_relation: \"<\"\n  - about: tau_f, CCK+BC to PC against PV+BC to PV+BC\n    test: post hoc comparison\n    p: 0.05\n    p_relation: \"<\"\n  - about: U0, CCK+BC to PC against PV+BC to PV+BC and PV+BC to PC\n    test: post hoc comparison\n    p: 0.01\n    p_relation: \"<\"\n  - about: Imax, PV+BC to PC against each other type\n    test: post hoc comparison\n    p: 0.001\n    p_relation: \"<\"\n  criterion: Fits of the comprehensive model (UDR with facilitation) as fig11-model-pv-udr; per\n    connection U0, tau_f and Imax. Kruskal-Wallis across the four types, post hoc Mann-Whitney U with\n    Bonferroni factor 6 (six pairs of four types, M6). Reproduced when under one reading the three\n    Kruskal-Wallis tests give p < 0.05 and at least five of the six named post hoc differences hold at\n    corrected p < 0.05 in the stated direction; partially reproduced when the Kruskal-Wallis tests\n    hold and two to four post hoc differences do.\n  depends_on:\n  - fig11-model-pv-udr\n- id: fig11-model-prediction\n  statement: Models fitted to the 10-AP trains predict responses to RIP and EPI patterns, purely\n    depressing UDR models for the three PV+ connection types and depressing-facilitating models for\n    CCK+BC to PC.\n  source: Results, Simple mathematical models of short-term plasticity effectively capture the\n    temporal properties of transmission, paragraph 7; Figure 11A and B\n  quote: We found that purely depressing models (with UDR) predicted the behaviour of PV+BC to PV+BC,\n    PV+BCtoPCandAACtoPCsynapseswellalsofornatural activitypatterns,whereasthebehaviourofCCK+BCtoPC\n    connections was best described by depressing-facilitating models of short-term plasticity\n  criterion: Fig. 11 legend. Models fitted as fig11-model-pv-udr on the 10-AP trains; test data the\n    mean RIP and EPI amplitudes (M4), with only A (Imax) refitted per connection. Reproduced when\n    under one reading the test mean squared error is lowest for a UDR depressing model (with or\n    without facilitation) for each PV+ type and for a model with facilitation for CCK+BC to PC.\n  depends_on:\n  - fig11-model-pv-udr\n  - fig11-model-cck-facilitation\n- id: fig12-sipsc-kinetics\n  statement: Spontaneous IPSCs decay faster in PV+BCs (n = 8) and AACs (n = 6) than in PCs (n = 10)\n    and CCK+BCs (n = 9); rise time differs only between AACs and CCK+BCs, and sIPSC amplitude and\n    frequency do not differ among cell types.\n  source: Results, IPSCs onto interneurons are more rapid than on PCs, paragraphs 2 and 4; Figure 12\n  quote: The spontaneous IPSCs onto PV+BCs (n = 8) and AACs (n = 6) decayed significantly faster\n    compared to those measured in PCs (n = 10) and CCK+BCs (n = 9). The only difference in the 10-90%\n    rise time value was between AACs and CCK+BCs ... We did not find significant differences in the\n    amplitude and frequency of sIPSCs among cell types\n  statistics:\n  - test: not named; asterisks in Figure 12\n    p: 0.05\n    p_relation: \"<\"\n    n: 10 PC, 8 PV+BC, 6 AAC and 9 CCK+BC\n  criterion: sIPSCs recorded at -60 mV with high KCl, NBQX and AP-5. Event detection is not described;\n    a standard template or threshold detection is used and named. Per cell, the averaged sIPSC, its\n    10 to 90% rise time and single exponential decay, the median amplitude and the mean interevent\n    interval. Kruskal-Wallis, post hoc Mann-Whitney with Bonferroni factor 6 (M6). Reproduced when\n    decay is shorter in PV+BC and in AAC than in PC and in CCK+BC (four comparisons, corrected p <\n    0.05), rise time differs only for AAC against CCK+BC, and the amplitude and interevent interval\n    tests are not significant. Needs the sIPSC recordings, which the data set is not described as\n    holding.\n- id: decay-pc-vs-interneuron\n  statement: uIPSCs from PV+BCs and CCK+BCs decay more slowly in PCs than in homologous interneurons\n    (PV+BC, 7.31 against 3.17 ms; CCK+BC, 6.34 against 4.47 ms).\n  source: Results, IPSCs onto interneurons are more rapid than on PCs, paragraph 3\n  quote: the decay time constant of uIPSCs originated from PV+BCs and CCK+BCs was significantly\n    longer on PCs than on homologous interneuron pairs (PV+BC, 7.31 vs. 3.17 ms, Mann-Whitney U test -\n    P = 0.001; CCK+BC, 6.34 vs. 4.47 ms, Mann-Whitney U test - P = 0.001)\n  statistics:\n  - about: PV+BC to PC against PV+BC to PV+BC\n    test: Mann-Whitney U test\n    p: 0.001\n    n: 8 PV+BC to PC and 16 PV+BC to PV+BC pairs\n  - about: CCK+BC to PC against CCK+BC to CCK+BC\n    test: Mann-Whitney U test\n    p: 0.001\n    n: 14 CCK+BC to PC and 6 CCK+BC to CCK+BC pairs\n  expected:\n  - quantity: decay time constant, PV+BC to PC, median\n    value: 7.31\n    tolerance: 0.731\n    unit: ms\n  - quantity: decay time constant, PV+BC to PV+BC, median\n    value: 3.17\n    tolerance: 0.317\n    unit: ms\n  - quantity: decay time constant, CCK+BC to PC, median\n    value: 6.34\n    tolerance: 0.634\n    unit: ms\n  - quantity: decay time constant, CCK+BC to interneuron, median\n    value: 4.47\n    tolerance: 0.447\n    unit: ms\n  criterion: Decay as M1 on single-AP uIPSCs (M2, M3), high KCl pairs. The paper is inconsistent on\n    the interneuron value for CCK+BCs, 4.47 ms here but 3.65 ms for CCK+BC pairs and 4.47 ms for\n    CCK+DTI pairs in paragraph 2 of the section on uIPSCs among interneurons. Readings for the CCK+BC\n    comparison group, (a) CCK+BC to CCK+BC pairs (the text's \"homologous interneuron pairs\"); (b)\n    CCK+DTI to CCK+DTI pairs (the pairs whose median is 4.47 ms); (c) both pooled. Two-sided\n    Mann-Whitney U test. Reproduced when under one reading both tests give p < 0.05 with PC decay\n    longer and at least three of the four medians are within tolerance.\n  depends_on:\n  - fig4b-in-pc-kruskal-wallis\n  - fig8-cck-pairs-uipsc\n- id: fig13-pvbc-pc-recovery-halftime\n  statement: Transmission at PV+BC to PC synapses recovers after a RIP train with a half-time of\n    495.8 ms (interquartile range 343.6 to 648.0, n = 7), close to the recovery of SWR amplitude.\n  source: Results, Possible physiological significance of short-term plasticity in SWR generation,\n    paragraphs 2 and 3; Figure 13B\n  quote: This recovery was close to the recovery half-time of PV+BC to PC IPSCs (495.8 (343.6-648.0)\n    ms) (Fig. 13B)\n  expected:\n  - quantity: recovery half-time of PV+BC to PC IPSCs, median over pairs\n    value: 495.8\n    tolerance: 147.8\n    unit: ms\n  criterion: Recovery ratios per pair as fig5db-recovery (intervals 50 to 1200 ms). The fit is not\n    given; Fig. 13B labels the value \"Tau (median)\" while the text calls it a half-time. Readings, (a)\n    per pair, a single exponential r(t) = 1 - (1 - r0) exp(-t/tau) fitted to the ratios, the value\n    being tau; (b) the same fit, the value being tau ln 2; (c) a free plateau, r(t) = rmax - (rmax -\n    r0) exp(-t/tau), value tau; (d) as (c), value tau ln 2. Median over pairs. Tolerance, the distance\n    to the nearer quartile (M7). Reproduced when the median is within tolerance under one reading.\n  depends_on:\n  - fig5db-recovery\n- id: fig13a-swr-refractory\n  statement: Spontaneous SWRs in CA3 slices have a minimum interval of about 200 ms, and SWR\n    amplitude recovers with the time since the previous SWR with a half-time of 501.8 ms\n    (interquartile range 374.2 to 699.3, n = 8).\n  source: Results, Possible physiological significance of short-term plasticity in SWR generation,\n    paragraph 2; Figure 13A\n  quote: we found that there was a minimum time between SWRs, corresponding to an absolute refractory\n    period ... Plotting the relationship between the amplitude of SWRs and the time subsequent to the\n    previous SWR revealed that the amplitude recovered with a half-time of 501.8 (374.2-699.3) ms\n  expected:\n  - quantity: half-time of SWR amplitude recovery, median over slices\n    value: 501.8\n    tolerance: 127.6\n    unit: ms\n  - quantity: minimum interval between SWRs\n    value: 200\n    tolerance: 20\n    unit: ms\n  criterion: Local field potentials in CA3 (Methods, paragraph on field recordings). SWR detection is\n    not described in this paper (it refers to Schlingloff et al. 2014); the detection used is named.\n    Per slice, SWR amplitude against the interval from the previous SWR, fitted as in\n    fig13-pvbc-pc-recovery-halftime (its four readings, with amplitude in place of the ratio); median\n    over slices. Reproduced when under one reading the median is within tolerance and the shortest\n    interval is 180 to 220 ms. Needs field potential recordings, which the data set is not described as\n    holding.\n- id: fig13c-optogenetic-swr\n  statement: SWRs evoked by optogenetic activation of PV+ cells grow with the time since the previous\n    spontaneous SWR, none being evoked within 100 ms, with a recovery half-time of 451 ms\n    (interquartile range 300.3 to 570.6, n = 4), similar to spontaneous SWRs and PV+BC to PC IPSCs.\n  source: Results, Possible physiological significance of short-term plasticity in SWR generation,\n    paragraph 3; Figure 13C\n  quote: The shorter the time, the smaller the amplitude of light-triggered SWR; at short intervals of\n    less than 100 ms, no SWRs could be evoked. Moreover, the recovery half-time of light-evoked SWRs\n    (451 (300.3-570.6) ms) was similar to the recovery half-time of spontaneous SWR amplitude and\n    recovery half-time of IPSCs between PV+BC-PC pairs\n  expected:\n  - quantity: recovery half-time of light-evoked SWR amplitude, median\n    value: 451\n    tolerance: 119.6\n    unit: ms\n  criterion: As fig13a-swr-refractory, with the amplitude of SWRs evoked by 10 ms light pulses against\n    the time since the previous spontaneous SWR. Reproduced when the median is within tolerance under\n    one reading and no SWR is evoked at intervals under 100 ms. Needs the optogenetic recordings, which\n    the data set is not described as holding.\n"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
python tools/claims_check.py claims/crcns-hc-7/10.1113-jp272231.yaml paper/10.1113-jp272231.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd tools && python -c "
import yaml,sys
from claims_check import flattenings, norm
t=flattenings(open('../paper/10.1113-jp272231.txt').read())
tight=t[2]
d=yaml.safe_load(open('../claims/crcns-hc-7/10.1113-jp272231.yaml'))
bad='fig3-cp-pv-cck fig4b-in-pc-kruskal-wallis fig6-pv-trains-depression fig6-cckbc-pc-trains cckdti-async-onset async-charge-epi-vs-160 decay-epi-vs-160 fig9-pvbc-pvbc-recovery-11th fig10-cck-cck-heterogeneity decay-pc-vs-interneuron fig13-pvbc-pc-recovery-halftime'.split()
for c in d['claims']:
  if c['id'] not in bad: continue
  for f in c['quote'].split('...'):
    f=norm(f).strip(' .,;').replace(' ','')
    if f in tight: continue
    lo=0
    for k in range(len(f)):
      if f[:k+1] not in tight: break
    i=tight.find(f[:k])
    print(c['id'],'| ok:',f[:k][-30:],'| quote:',f[k:k+30],'| text:',tight[i+k:i+k+30])
"
```

Result: not kept, because it reads the paper's text.

**Agent**

Eleven quotes fail, all for two reasons: I had swapped colons for dashes, and some sentences run across figure text at page breaks. Fixing them with "..." cuts.

**Agent calls Bash**

```bash
cd  && python - <<'EOF'
p='claims/crcns-hc-7/10.1113-jp272231.yaml'
s=open(p).read()
rep=[
("""  quote: the three perisomatic region-targeting interneuron-evoked uIPSCs were different in 10-90%
    rise time (Kruskal-Wallis ANOVA P = 0.027), latency (Kruskal-Wallis ANOVA - P = 7.49 × 10-4),
    amplitude (Kruskal-Wallis ANOVA - P = 0.001), synaptic potency (Kruskal-Wallis ANOVA, P = 0.004)
    and transmission probability (Kruskal-Wallis ANOVA - P = 0.003)""",
"""  quote: the three perisomatic region-targeting interneuron-evoked uIPSCs were different in 10-90%
    rise time (Kruskal-Wallis ANOVA P = 0.027), latency (Kruskal-Wallis ANOVA ... P = 7.49 × 10-4),
    amplitude (Kruskal-Wallis ANOVA ... P = 0.001), synaptic potency (Kruskal-Wallis ANOVA, P = 0.004)
    and transmission probability (Kruskal-Wallis ANOVA ... P = 0.003)"""),
("interneurons within the same main class (P = 0.0175) and PV+ cells in particular preferentially\n    targeted other PV+ interneurons",
 "interneurons within the same main class (P = 0.0175) and PV+ cells in particular preferentially ...\n    targeted other PV+ interneurons"),
("depression becomes more prominent with increasing frequency", "depression becomes more prominent with ... increasing frequency"),
("(80 Hz, 160 Hz, 320 Hz; EPI protocol) the transient\n    short-term", "(80 Hz, 160 Hz, 320 Hz; EPI protocol) the transient ...\n    short-term"),
("than for the CCK+BCs - between the 7th", "than for the CCK+BCs ... between the 7th"),
("(Mann-Whitney U test - P = 0.002)", "(Mann-Whitney U test ... P = 0.002)"),
("(Mann-Whitney U test - P = 0.17)", "(Mann-Whitney U test ... P = 0.17)"),
("(Mann-Whitney U test - P = 0.27)", "(Mann-Whitney U test ... P = 0.27)"),
("(Mann-Whitney U test - P = 0.9)", "(Mann-Whitney U test ... P = 0.9)"),
("Mann-WhitneyUtest - P =0.01)", "Mann-WhitneyUtest ... P =0.01)"),
("(from 36.82 ms to 138.71 ms; Mann-Whitney U test - P = 0.01)", "(from 36.82 ms to 138.71 ms; Mann-Whitney U test ... P = 0.01)"),
("(Kruskal-Wallis\n    ANOVA - P = 0.152)", "(Kruskal-Wallis\n    ANOVA ... P = 0.152)"),
("frequency-dependent strong asynchronous release (Fig. 10Ab). Both", "frequency-dependent strong ... asynchronous release (Fig. 10Ab). Both"),
("7.31 vs. 3.17 ms, Mann-Whitney U test -\n    P = 0.001; CCK+BC, 6.34 vs. 4.47 ms, Mann-Whitney U test - P = 0.001)",
 "7.31 vs. 3.17 ms, Mann-Whitney U test ...\n    P = 0.001; CCK+BC, 6.34 vs. 4.47 ms, Mann-Whitney U test ... P = 0.001)"),
("  quote: This recovery was close to", "  quote: recovery was close to"),
]
for a,b in rep:
    assert a in s, a[:60]
    s=s.replace(a,b)
open(p,'w').write(s)
EOF
python tools/claims_check.py claims/crcns-hc-7/10.1113-jp272231.yaml paper/10.1113-jp272231.txt
```

Result: not kept, because it reads the paper's text.

**Agent**

Checker passes: 0 problems. Now checking the style rules (no ": " inside values, no em dashes, no "rather") and fixing two numbers in fig9.

**Agent calls Bash**

```bash
f=claims/crcns-hc-7/10.1113-jp272231.yaml; grep -n "—\|rather" $f; grep -nE "^\s+[^#].*: " $f | grep -vE "^\s*[0-9]+:\s*(- )?[a-z_]+: " | head; grep -nE "^\s*(- )?[a-z_]+: .*: " $f | head
```

```
(Bash completed with no output)
```

**Agent calls Bash**

```bash
python - <<'EOF'
p='claims/crcns-hc-7/10.1113-jp272231.yaml'
s=open(p).read()
rep=[
("""    value: 7.5
    tolerance: 3.25""","""    value: 7.75
    tolerance: 3.25"""),
("""    value: 0.85
    tolerance: 0.14""","""    value: 0.855
    tolerance: 0.135"""),
("""by 10% of each bound gives 4.5 to 11 (7.75 plus or minus 3.25). The 320 Hz range 0.8 to 0.9
    widened gives 0.72 to 0.99""","""by 10% of each bound gives 4.5 to 11 (7.75 plus or minus 3.25). The 320 Hz range 0.8 to 0.9
    widened gives 0.72 to 0.99 (0.855 plus or minus 0.135)"""),
("""    the tests hold and four to six medians are within tolerance. With six and four pairs, the
    corrected Mann-Whitney test can reach p < 0.05 only with complete separation; the uncorrected p
    is also shown.""","""    the tests hold and four to six medians are within tolerance. The uncorrected p is also shown."""),
]
for a,b in rep:
    assert a in s, a[:60]
    s=s.replace(a,b)
open(p,'w').write(s)
EOF
python tools/claims_check.py claims/crcns-hc-7/10.1113-jp272231.yaml paper/10.1113-jp272231.txt; git status --short
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
python -c "
import yaml;d=yaml.safe_load(open('claims/crcns-hc-7/10.1113-jp272231.yaml'))['claims']
print(len(d),sum('quote' in c for c in d),sum('statistics' in c for c in d),sum(len(c.get('statistics',[])) for c in d),sum('criterion' in c for c in d),sum('expected' in c for c in d))"
```

```
43 42 19 41 43 23
```

**Agent**

I wrote `claims/crcns-hc-7/10.1113-jp272231.yaml`, and the quote checker reports 0 problems. Nothing is committed.

**Text read.** The version of record (J Physiol 2016), text extracted from the PDF. It has the Methods, Results, Discussion, the legends of Figs. 1 to 13 and Tables 1 to 4. The paper has no supplement and links no code: its analysis software is named in the Methods but not published. I read the data descriptor only to see what the data set holds: paired recordings for eight connection types under the stimulation protocols.

**Counts.** 43 claims. 42 have quotes; one (`table4-model-parameters`) has an `inferred` note, because its numbers come from Table 4 and the Fig. 11 legend. 19 claims carry 41 statistical entries, all 43 have criteria, and 23 have expected values. Some claims test data the data set is not described as holding. These are clustering and cell features (Fig. 2, Tables 1 and 2), connection probability (Fig. 3), spontaneous IPSCs (Fig. 12) and field-potential and optogenetic ripples (Fig. 13A, C). I wrote them as claims and say so in their criteria.

**Details the paper leaves open, with the readings named:**
- **Failures:** the authors' per-sweep success tables, or a detection at 3 standard deviations of baseline (a standard choice, not the paper's).
- **Which APs count as "single":** the AP 1000 ms before the RIP burst, the 1 Hz train, or both pooled.
- **Amplitude in trains:** the per-sweep tables, or the peak of the averaged trace above a local baseline.
- **Sweeps:** all sweeps are used. A variant drops the first three, for the "steady-state average" the Fig. 5A legend mentions.
- **Bonferroni factor:** not stated; taken as the number of pairwise group comparisons.
- **Unnamed tests behind the asterisks in Figs. 5C, 5Db and 7B:** a Wilcoxon signed-rank test against 1, or a Mann-Whitney test. Correction is uncorrected or Bonferroni.
- **Onset of asynchronous release:** a charge above 2 standard deviations, or the current between APs failing to return to baseline.
- **Window for the decay fit:** 500 ms after the last AP, or the return to baseline.
- **Model fitting:** unweighted squared error or squared error normalised to the first IPSC, with BIC = N ln(SSE/N) + k ln N.
- **Recovery half-time:** the fit has a fixed plateau or a free one, and the value is reported as τ or as τ ln 2.
- **PCA for clustering:** z-scored or raw features, and components kept to 80% of variance or with eigenvalue above 1.
- **"Above 160 Hz":** the 160 and 320 Hz trains pooled, or 320 Hz alone.
- **CCK+BC interneuron comparison group:** the paper prints 4.47 ms here but 3.65 ms elsewhere, so the group is CCK+BC pairs, CCK+DTI pairs, or both pooled.

**Missing from the paper:**
- **Figure values:** the PDF could not be opened as images (no renderer is installed here). Values printed only inside figures are not used, such as the Fig. 4B medians and the Figs. 5, 6, 7, 10 and 12 panels. Those claims rest on the Results and the legends.
- **Table 4:** the extracted text lost its per-type parameter columns, so those values come from the Fig. 11 legend. In the CCK+BC row, I assigned the three values to U0, τf and Imax from the header.
- **Undescribed methods:** the paper does not describe sIPSC or ripple detection, the feature definitions, or the filter type. Where a criterion needs one, a standard choice is used and named as such.

## End of run

27 turns, 8 minutes, $2.56 at API prices, result: success.
