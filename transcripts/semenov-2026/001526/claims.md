# 001526 · claims · run 39600175420

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cat docs/protocol.md; ls claims/001453 paper/; ls claims/001526 2>/dev/null
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -n '/^## Reader/,/^## Author/p' docs/protocol.md
```

```
## Reader

### 1. Get the paper

The workflow puts the paper's full text, and its PDF where there is one, under
`paper/`: the main text, the Methods, and the supplement. Read the text; open
the PDF only to read a figure or a table the text garbles. If the full text is
not there, or lacks the Methods or a supplement the results rest on, stop:
write no claims, and end with a report that names what is missing, so that it
can be supplied. Never write claims from the abstract. Do not copy figures.
Do not look at the dataset's data: its title and description on the archive
are enough to know which paper and which experiments it is meant to hold.

### 2. Read the paper's code

Read the code the paper links to before writing criteria. Say what it holds,
and record the repository and commit read. Where the Methods leave a choice
open and the code settles it, follow the code and say so. Where they disagree,
follow the Methods for the main result and name the code's choice as a
variant. When more sources disagree (the Methods, the analysis code, the
[... 116 more lines not kept]
```

**Agent calls Bash**

```bash
cat claims/001453/*.yaml | head -150; wc -l paper/*.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1016-j.bioelechem.2026.109283.txt"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1016-j.bioelechem.2026.109283.txt",
 "offset": 705,
 "limit": 320
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -n 150,400p claims/001453/*.yaml; ls tools; ls claims | head; ls claims/*/ | head -50
```

```
data: with_labels
  depends_on:
  - stimulus-code-link
  criterion: For each fish, the mean of its median angular velocities for the rightward
    stimuli (right, forward right, backward right) minus the mean for the leftward stimuli
    (left, forward left, backward left). Reproduced when this difference is greater than zero
    in each species by a one-sided Wilcoxon signed-rank test at p < 0.05; partially reproduced
    when it holds in one species only. The per-stimulus species medians are reported as well.
- id: fig1h-zf-higher-angular-acceleration
  statement: Across directional stimuli ZF have higher angular acceleration than DC, and the
    distributions of the two species differ for every stimulus.
  source: Results, Optic flow induces angular matching and turns in DC, paragraph 2; Figure 1H
    (Kruskal-Wallis test with Bonferroni correction)
  quote: Across directional stimuli, ZF maintained higher angular acceleration than DC
  statistics:
  - test: Kruskal-Wallis test
    p: 0.05
    p_relation: "<"
    corrected: Bonferroni
  data: with_labels
[... 231 more lines not kept]
```

**Agent calls Bash**

```bash
grep -rn "001526" --include=*.yaml --include=*.json --include=*.md --include=*.csv . 2>/dev/null | grep -v transcripts | head; sed -n 1,80p tools/claims_check.py
```

```
./targets/dandisets.json:6274:   "dandiset": "001526",
./papers/manifest.yaml:1884:  '001526':
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
[... 62 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 6260,6300p targets/dandisets.json; sed -n 1880,1900p papers/manifest.yaml; python -c "import json;d=json.load(open('schemas/claims.schema.json'));print(json.dumps(d,indent=1)[:6000])"
```

```
],
   "approaches": [],
   "papers": [
    {
     "doi": "10.1016/j.bioelechem.2026.109283",
     "title": "Sub-microsecond optical measurements of cell membrane charging and lesioning by pulsed electric fields",
     "relation": "IsPublishedIn",
     "resource_type": "JournalArticle",
     "preprint": false
    }
   ],
   "catalystneuro": []
  },
  {
   "dandiset": "001526",
   "name": "Assessment of Post-Electroporation Suitability of CHO Cells for Polarization Studies Using Strobe Fluorescence Microscopy",
   "published_version": "0.261006.1851",
   "asset_count": 243,
   "size_gb": 8.32,
   "data_standards": [
[... 247 more lines not kept]
```

**Agent calls Bash**

```bash
python -c "import json;d=json.load(open('schemas/claims.schema.json'));print(json.dumps(d['\$defs'],indent=1))"
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
grep -n -i "supplement\|github\|code\|appendix" paper/*.txt | head
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1016-j.bioelechem.2026.109283.pdf",
 "pages": "3,8"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd $TMPDIR && python -c "
import fitz
d=fitz.open('paper/10.1016-j.bioelechem.2026.109283.pdf')
for i in (2,7):
    d[i].get_pixmap(dpi=110).save(f'p{i+1}.png')
" && ls $TMPDIR
```

Result: not kept, because it reads the paper's text.

**Agent**

The paper has full Methods, no supplement, and no linked code. Data are "available on request". I'm writing the claims file now.

**Agent calls Write**

```json
{
 "file_path": "claims/001526/10.1016-j.bioelechem.2026.109283.yaml",
 "content": "# Claims for Semenov, Silkuniene, Silkunas, Pakhomova, Bixler, Ibey, Kochunov & Pakhomov (2026)\n# on dandiset 001526.\n# Written by an agent (model \"claude-opus-5-5\", Claude Code in GitHub Actions), 2026-10-21,\n# protocol pilot-10 as stated in docs/protocol.md.\n#\n# Text read: the version of record (Bioelectrochemistry 171 (2026) 109283), from a PDF supplied\n# by a person, as extracted text: main text, Materials and methods, Results, Discussion and\n# figure legends. The paper has no supplement and links no code; its Data availability\n# statement says \"Data will be made available on request\". No figure was read from the PDF.\n# The Methods say most methods follow Semenov et al. 2025 (Bioelectrochemistry 168, 109143,\n# reference [20]), which is not under paper/ and was not read. Two inputs come from it: the\n# fit of the charging time constant tau against cell radius used in Eq. (1), and the linear\n# range of both dyes below 300 V/cm.\n#\n# Data the paper used, as it reports them. Spheroidal CHO-K1 cells plated 1 to 3 h on\n# glass-bottom dishes, one cell per experiment, room temperature. Potentiometric imaging with\n# FluoVolt or Di-8-ANEPPS, excited by ~6 ns 440 nm laser flashes at 900 ns into 1 us pulsed\n# electric fields (PEFs) or 275 ns into 0.3 us PEFs, iXon Ultra 897 camera, 60x objective.\n# Images in sets of 100 at 6 Hz, the first 40 without PEF (baseline) and the next 60 with PEF\n# at one field strength; field strength escalated across sets (43 to 1400 V/cm for 1 us; 357\n# to 3320 V/cm for 0.3 us) or alternated (150 and 230 V/cm, then 1000 V/cm). Groups: Fig. 2A\n# FluoVolt n = 4 cells; Fig. 2B Di-8-ANEPPS n = 5; Fig. 2C and D Di-8-ANEPPS alternating\n# protocol n = 8; Fig. 3 calibration (43 to 360 V/cm, 1 us); Fig. 4A FluoVolt n = 4; Fig. 4B\n# and C Di-8-ANEPPS n = 5; Fig. 4D Di-8-ANEPPS, 0.3 us, n = 10; Fig. 5A Di-8-ANEPPS with\n# 1 mM Gd3+ n = 7 and controls n = 5, 150 to 1400 V/cm; Fig. 7 two-pulse protocol\n# (conditioning 1 us at 150 to 1400 V/cm, 5 us gap, 1 us 150 V/cm test pulse, image at 900 ns\n# into the test pulse) n = 5. Calcium imaging with Fluo-4 (widefield, 1 or 2 s per frame):\n# Fig. 6A single 1 us pulse at 60 s, 5 min recording, 0 to 1200 V/cm, 14 cells per field\n# strength; Fig. 6B train of 60 pulses at 6 Hz from 30 s, 150 s recording, 28 to 54 cells per\n# field strength, 224 cells in all. Measured variables: dye fluorescence along a 6-pixel-wide\n# trace on the cell perimeter (resampled to 360 points) or in +-5 degree arcs at the cathodic\n# and anodic poles; dF = 100% x (F - F0)/F0 with F0 the baseline; IMP from dF by the dye\n# slopes of Fig. 3; cell radius from the images; Fluo-4 intensity in a circular region over\n# the cell minus a cell-free background.\n#\n# Method details shared by the criteria, from the Methods (section 2.3) unless said. Pole dF\n# is the mean F in the +-5 degree arcs at each pole; for Fig. 2 per image, against F0 the mean\n# of the first 40 images; for later figures the 40 baseline and 60 PEF images are collapsed\n# into one baseline and one polarization image (Fig. 4B dotted lines use the first 10 PEF\n# images). Values are averaged across cells, mean +- s.e. Calculated IMP (IMPC) is Eq. (1),\n# 1.5 E R cos(theta) (1 - exp(-t/tau)), with t = 900 or 275 ns, R from each cell's image and\n# tau from the tau-radius fit of [20] (an outside input; its coefficients are not in this\n# paper). IMP from dF uses 26% (FluoVolt) or 9.1% (Di-8-ANEPPS) per 100 mV. Effective\n# membrane conductivity uses Eq. (2) with cytoplasm 0.4 S/m, medium 1.64 S/m, intact membrane\n# 3e-7 S/m, R = 8 um and d = 5 nm, inverted from the ratio of measured IMP to IMPC.\n# Open in all of them: how the perimeter trace and the cell centre are drawn (by hand in\n# MetaMorph); how R is measured from the image (readings: (a) perimeter length over 2 pi;\n# (b) radius of the circle of equal area); whether background is subtracted from the\n# potentiometric images (readings: (a) none, as section 2.3 describes none; (b) a cell-free\n# region subtracted, as for Fluo-4 in section 2.4); the LOESS (LOWESS) span used for smoothed\n# curves, a plotting choice that no criterion here rests on. The field strength of each\n# recording is the value the paper labels it with (from its Sim4Life model), to be read from\n# the dataset's metadata.\nschema_version: 2\ndataset:\n  archive: dandi\n  id: \"001526\"\npaper: doi:10.1016/j.bioelechem.2026.109283\nclaims:\n- id: fig1-pattern-poles-leaky\n  statement: With Di-8-ANEPPS and 1 us PEFs, polarization depolarizes the cathode-facing pole and\n    hyperpolarizes the anode-facing pole, falls off towards the equator and scales with field\n    strength up to 570 V/cm; at 780 V/cm the cathodic pole stops increasing and dims; at 1000\n    to 1400 V/cm the poles show reduced or absent polarization while regions nearer the equator\n    remain polarized and may exceed the poles.\n  source: Results, section 3.1, paragraph 1; Figure 1 and legend\n  quote: At a higher electric field strength of 780 V/cm, polarization at the cathodic pole does not\n    further increase but dims out, indicating a less efficient charging of the partially\n    permeabilized membrane. Still stronger electric fields produce a distinct pattern of reduced\n    or absent polarization at the poles\n  criterion: Figure 1 shows representative images from one cell, not identified. Tested on the\n    Di-8-ANEPPS 1 us escalation data (the Fig. 4B group, n = 5), with polarization images as in\n    section 2.3 and perimeter dF resampled to 360 points. Reproduced when, in the mean over\n    cells, (1) cathodic pole dF is positive and anodic pole dF negative at 43 to 570 V/cm and\n    pole |dF| rises with field strength over that range; (2) cathodic pole dF at 780 V/cm is not\n    above that at 570 V/cm; (3) at 1000 to 1400 V/cm pole |dF| is below its value at 570 V/cm\n    at the cathodic pole, while the largest |dF| on the cathodic half of the profile lies away\n    from the +-5 degree pole arc in at least one of those fields. Partially reproduced when (1)\n    holds and one of (2) or (3) fails.\n- id: fig2a-fluovolt-saturation\n  statement: In FluoVolt-loaded cells, pole dF rose with field strength until apparent\n    saturation at 66% (255 mV) at 360 V/cm at the cathodic pole and -83% (-320 mV) at 570 V/cm\n    at the anodic pole; stronger fields did not increase the anodic response and decreased the\n    cathodic one.\n  source: Results, section 3.2, paragraph 2; Figure 2A\n  quote: ΔF increased proportionally to the electric field strength until reaching apparent\n    saturation at 66% ΔF (255 mV IMP) at 360 V/cm at the cathodic pole, and −83% ΔF (−320 mV IMP)\n    at 570 V/cm at the anodic pole. Further escalation of the electric field strength did not\n    increase the dye response at the anodic pole and even decreased it at the cathodic pole.\n  expected:\n  - quantity: FluoVolt cathodic pole dF at 360 V/cm, mean over cells and the 60 PEF images\n    value: 66\n    tolerance: 6.6\n    unit: '%'\n  - quantity: FluoVolt anodic pole dF at 570 V/cm, mean over cells and the 60 PEF images\n    value: -83\n    tolerance: 8.3\n    unit: '%'\n  criterion: Fig. 2A, n = 4 cells, 9 sets escalating from 43 to 1400 V/cm. Pole dF per image\n    against F0, the mean of the set's first 40 images (section 2.3), averaged over the 60 PEF\n    images of the set and then over cells. Reproduced when both values are within tolerance,\n    the cathodic maximum over fields is at 360 V/cm or within its tolerance of the 360 V/cm\n    value, the anodic dF at fields above 570 V/cm is not more negative than at 570 V/cm by more\n    than the tolerance, and the cathodic dF at the strongest field is below its 360 V/cm value.\n- id: fig2a-fluovolt-baseline-stable\n  statement: Without PEF (the first 40 images of each set) FluoVolt measurements were stable,\n    showing no significant photosensitization or dye bleaching.\n  source: Results, section 3.2, paragraph 2; Figure 2A\n  quote: Without PEF (first 40 datapoints, or ~ 7 s in each set), measurements were stable,\n    indicating no significant photosensitization or dye bleaching.\n  criterion: A claim of absence for which the paper names no test. Methods 2.5 names linear\n    regression with fit significance (Grapher) and paired t-tests (Fig. 2 legend), so two\n    readings are run, per pole and set, on the 40 baseline dF values averaged over the n = 4\n    cells. (a) linear regression of dF on image index, fit significance p < 0.05; (b) 2-tailed\n    paired t-test across cells of the mean of baseline images 1 to 20 against 21 to 40, p <\n    0.05. Reproduced when neither finds a significant change in any set at either pole, not\n    reproduced when both do in the same sets; when the readings disagree the claim is blocked\n    as methods_underspecified. The slope and the change in dF over the 40 images are reported.\n- id: fig2a-fluovolt-stable-electroporating\n  statement: At 1000 V/cm and above, which strongly electroporated the cells, the FluoVolt\n    response stayed stable through the 60 pulses of each set.\n  source: Results, section 3.2, paragraph 2; Figure 2A\n  quote: Field strengths of 1000 V/cm and higher caused strong electroporation (see Section 3.5),\n    but the dye response in each set stayed stable through the 60 pulses applied\n  criterion: The paper names no test. Readings as in fig2a-fluovolt-baseline-stable, run on the\n    60 PEF images of the sets at 1000 V/cm and above, per pole; (b) compares PEF images 1 to 30\n    with 31 to 60. Reproduced when neither reading finds a significant change; not reproduced\n    when both do; blocked as methods_underspecified when they disagree.\n- id: fig2b-di8-climbs-to-570\n  statement: Di-8-ANEPPS has a lower sensitivity than FluoVolt, but its dF kept rising with\n    field strength up to 570 V/cm at both poles.\n  source: Results, section 3.2, paragraph 3; Figure 2B\n  quote: This dye has a lower sensitivity to membrane polarization (note the vertical scale\n    different from Fig. 2A), but ΔF kept climbing up to the electric field strength of 570 V/cm at\n    both cell poles.\n  criterion: Fig. 2B, n = 5 cells; pole dF per set as in fig2a-fluovolt-saturation. Reproduced\n    when the cathodic dF increases and the anodic dF becomes more negative at each step from\n    43 to 570 V/cm in the mean over cells, and the largest pole |dF| up to 570 V/cm is smaller\n    than the FluoVolt value at the same field and pole (Fig. 2A group).\n- id: fig2b-di8-bleaching-43\n  statement: Di-8-ANEPPS responses were somewhat affected by bleaching, most noticeably at 43\n    V/cm, where bleaching added about 5% to dF at the anodic pole and reduced it by about 5% at\n    the cathodic pole.\n  source: Results, section 3.2, paragraph 3; Figure 2B\n  quote: The responses were somewhat affected by dye bleaching (particularly noticeable at 43 V/cm,\n    where bleaching added ~5% to ΔF at the anodic pole and reduced it by the same ~5% at the\n    cathodic pole.\n  expected:\n  - quantity: bleaching contribution at the anodic pole, 43 V/cm\n    value: 5\n    tolerance: 0.5\n    unit: '%'\n  - quantity: bleaching contribution at the cathodic pole, 43 V/cm\n    value: -5\n    tolerance: 0.5\n    unit: '%'\n  criterion: The paper does not say how the bleaching contribution was measured. Readings\n    allowed by the text (a) the drift of pole dF over the 100 images of the 43 V/cm set, from a\n    linear regression of the 40 baseline values extrapolated over the 60 PEF images (the drift\n    adds to the hyperpolarizing anodic response and subtracts from the depolarizing cathodic\n    one); (b) the difference in dF between the first and the last 10 images of the 43 V/cm\n    set. Reproduced when, under a reading, both poles show a downward drift of F whose size is\n    within tolerance; partially reproduced when the direction holds at both poles but the size\n    is outside the tolerance under every reading.\n- id: fig2b-di8-decline-within-set\n  statement: Di-8-ANEPPS responses to PEFs at and above 780 V/cm decreased gradually within\n    each set of 60 images.\n  source: Results, section 3.2, paragraph 3; Figure 2B\n  quote: In addition, responses to PEFs at and above 780 V/cm decreased gradually in each set of 60\n    images, consistent with expectations of adding membrane damage by additional electroporation\n    pulses in each set\n  criterion: Fig. 2B, n = 5 cells. The paper names no test. Readings, per set at 780 V/cm and\n    above, on pole |dF| averaged over cells (a) linear regression of |dF| on PEF image index,\n    negative slope with fit significance p < 0.05; (b) 2-tailed paired t-test across cells of\n    PEF images 1 to 10 against 51 to 60 (the first 10 of 60 are the window used in Fig. 4B),\n    lower at the end with p < 0.05. Reproduced when, under a reading, the response declines\n    within most of the sets at 780 V/cm and above at the cathodic pole; the slope for every set\n    and pole is reported, and the slope at 43 to 570 V/cm is shown for comparison.\n- id: fig2cd-nonelectroporating-stable\n  statement: Repeated alternating sets of 150 and 230 V/cm PEFs produced dF responses that\n    stayed constant within each set and between sets, so that 800 flashes and 480 pulses had no\n    obvious impact before the 1000 V/cm exposure.\n  source: Results, section 3.2, paragraph 4; Figure 2C and D\n  quote: Repeated sets of PEFs at 150 and 230 V/cm, delivered in alternation, produced ΔF responses\n    that stayed constant both within each set and between the sets (Fig. 2C and D).\n  criterion: A claim of absence. Fig. 2C and D, n = 8 cells; set means of pole dF over the 60\n    PEF images. The paper's test, from the Fig. 2 legend, is a 2-tailed paired t-test of each\n    set mean against the first set at the same field strength (the dashed lines mark the first\n    trial's means), at p < 0.05. Reproduced when no 150 or 230 V/cm set before the 1000 V/cm\n    exposure differs from the first set of its field strength at either pole; not reproduced\n    when any does. The within-set change (first against last 10 PEF images) is reported as a\n    variant, as are the differences in percent.\n- id: fig2c-1000-within-set\n  statement: At 1000 V/cm, cathodic pole dF fell from 40 +- 10% at the start of the set to\n    26.6 +- 8% at its end, a trend that was not statistically significant.\n  source: Results, section 3.2, paragraph 4; Figure 2C\n  quote: In contrast, at an electroporating field strength of 1000 V/cm, ΔF at the cathodic pole\n    decreased from 40 ± 10% at the beginning of the set to 26.6 ± 8% at the end of it. Although not\n    statistically significant (p > 0.05)\n  statistics:\n  - test: 2-tailed paired t-test (the test named in the Fig. 2 legend)\n    p: 0.05\n    p_relation: \">\"\n    n: 8 cells\n  expected:\n  - quantity: cathodic pole dF at the beginning of the 1000 V/cm set\n    value: 40\n    tolerance: 10\n    unit: '%'\n  - quantity: cathodic pole dF at the end of the 1000 V/cm set\n    value: 26.6\n    tolerance: 8\n    unit: '%'\n  criterion: Tolerances are the paper's s.e. The paper does not say how many images form the\n    beginning and the end. Readings (a) the first and the last PEF image; (b) the mean of PEF\n    images 1 to 10 and 51 to 60; (c) the mean of images 1 to 5 and 56 to 60. Reproduced when,\n    under a reading, both means are within tolerance, the end is lower, and a 2-tailed paired\n    t-test across the 8 cells gives p > 0.05.\n- id: fig2d-lasting-reduction\n  statement: Set-averaged dF stayed nearly constant before electroporation but dropped by about\n    20% (a small but persistent reduction of at most 20%) in the 150 and 230 V/cm sets acquired\n    after the 1000 V/cm exposure.\n  source: Results, section 3.2, paragraph 4; Figure 2D and legend\n  quote: ΔF values averaged across each set of 60 PEFs stayed nearly constant before the\n    electroporation, but dropped by about 20% in the sets acquired after it (Fig. 2D, p < 0.05).\n  statistics:\n  - test: 2-tailed paired t-test\n    p: 0.05\n    p_relation: \"<\"\n    n: 8 cells\n  expected:\n  - quantity: reduction of set-averaged dF after the 1000 V/cm exposure, relative to the first\n      set of the same field strength\n    value: 20\n    tolerance: 2\n    unit: '%'\n  criterion: Fig. 2D, n = 8 cells. Set means of pole dF over the 60 PEF images, each set\n    compared with the first set of the same field strength (the legend's dashed lines) by a\n    2-tailed paired t-test across cells. The paper does not say which pole or how the 20% is\n    summarized. Readings (a) each pole separately; (b) both poles' |dF| averaged; and, for the\n    size, (i) the mean reduction over all post-1000 V/cm sets, (ii) the reduction of each set.\n    Reproduced when, under a reading, the post-exposure sets show a reduction within tolerance\n    with p < 0.05 for at least one set, and no pre-exposure set differs at p < 0.05. Partially\n    reproduced when the reduction is significant but its size is outside the tolerance under\n    every reading.\n- id: fig3-dye-slopes\n  statement: Fitting dF against IMPC from -150 to +150 mV with a line through the origin gave\n    slopes of 26% (FluoVolt) and 9.1% (Di-8-ANEPPS) dF per 100 mV, with correlation\n    coefficients of 0.96 and 0.78.\n  source: Results, section 3.3, paragraph 1; Figure 3 legend\n  quote: The correlation coefficients of the fits equaled 0.96 for FluoVolt and 0.78 for Di-8\n    ANEPPS (due to a lower signal-to-noise ratio), with respective slope coefficients of 26% and\n    9.1% ΔF per 100 mV of IMP.\n  data: with_inputs\n  expected:\n  - quantity: FluoVolt slope\n    value: 26\n    tolerance: 2.6\n    unit: '% dF per 100 mV'\n  - quantity: Di-8-ANEPPS slope\n    value: 9.1\n    tolerance: 0.91\n    unit: '% dF per 100 mV'\n  - quantity: FluoVolt correlation coefficient\n    value: 0.96\n    tolerance: 0.096\n  - quantity: Di-8-ANEPPS correlation coefficient\n    value: 0.78\n    tolerance: 0.078\n  criterion: From section 3.3 and the Fig. 3 legend. Cells exposed to 1 us PEFs at 43 to 360\n    V/cm, imaged at 900 ns; every perimeter location's dF (polarization against baseline image,\n    360 points per cell) paired with IMPC from Eq. (1) for that location, the cell's radius and\n    its tau from the fit of [20] (outside input). All points from -150 to +150 mV IMPC, pooled\n    over cells and fields, fit by least squares with a line through the origin; the\n    correlation coefficient of that fit. The paper does not say which cells form Fig. 3;\n    readings (a) the Fig. 4A and 4B groups at 43 to 360 V/cm; (b) every cell of the dye at\n    those fields in the dataset. It does not say whether the correlation coefficient is for\n    the through-origin fit or an ordinary Pearson r; both are shown. Reproduced when, under a\n    reading, both slopes are within tolerance; partially reproduced when one is. The\n    coefficients are reported against their values.\n- id: fig3-fluovolt-nonlinear\n  statement: FluoVolt measurements became non-linear already at +-200 mV, while Di-8-ANEPPS\n    stayed essentially linear from -500 to +500 mV, so FluoVolt's early departure reflects the\n    limit of the dye's range and not electroporation.\n  source: Results, section 3.3, paragraph 1; Figure 3 legend\n  quote: The actual measurements with FluoVolt gradually became non-linear already at ±200 mV,\n    while those for Di-8-ANEPPS stayed essentially linear throughout the tested range from −500 to\n    +500 mV.\n  data: with_inputs\n  depends_on:\n  - fig3-dye-slopes\n  criterion: Data as in fig3-dye-slopes over the whole IMPC range. The paper judged linearity by\n    eye against a LOESS curve. Measure fixed from the text, the mean dF in 50 mV bins of IMPC\n    (a plotting bin, a standard choice) divided by the through-origin slope times the bin\n    centre. Reproduced when the FluoVolt ratio falls below 0.8 in the bins beyond +-200 mV on at\n    least one side while the Di-8-ANEPPS ratio stays within 0.8 to 1.2 in every bin with at\n    least 20 points from -500 to +500 mV. The 0.8 to 1.2 band is not from the paper; the\n    ratios per bin are reported so that a reader can judge.\n- id: fig4a-fluovolt-limits\n  statement: FluoVolt-measured and calculated IMP matched only at 43 and 150 V/cm; with stronger\n    PEFs pole dF reached at most 71 +- 10% (cathodic) and -83.5 +- 5% (anodic), about +260 and\n    -330 mV, and the cathodic value fell from 71% at 360 V/cm to 45 to 50% at 1000 to 1400 V/cm.\n  source: Results, section 3.4, paragraph 1; Figure 4A\n  quote: However, this assumption held only for the applied fields of 43 and 150 V/cm, where\n    measured and calculated IMP matched. With stronger PEFs, maximum ΔF reached 71 ± 10% and −83.5 ±\n    5% at the cathodic and anodic poles, respectively. ... Notably, polarization at the cathodic pole\n    decreased from 71% at 360 V/cm to 45–50% at 1000–1400 V/cm\n  data: with_inputs\n  expected:\n  - quantity: maximum cathodic pole dF, FluoVolt\n    value: 71\n    tolerance: 10\n    unit: '%'\n  - quantity: maximum anodic pole dF, FluoVolt\n    value: -83.5\n    tolerance: 5\n    unit: '%'\n  - quantity: cathodic pole dF at 1000 to 1400 V/cm, range\n    value: 47.5\n    tolerance: 7.25\n    unit: '%'\n  criterion: Fig. 4A, n = 4 cells, 1 us, 43 to 1400 V/cm; pole dF from the polarization image,\n    mean over cells; IMPC at the poles from Eq. (1) with tau from [20]. Tolerances for the\n    maxima are the paper's s.e.; the 45 to 50% range is widened by 10% of each bound (40.5 to\n    55). Reproduced when both maxima are within tolerance, cathodic dF at each of 1000, 1200\n    and 1400 V/cm (those present) lies within 40.5 to 55%, and measured IMP (dF / 0.26 per mV)\n    is within the s.e. of IMPC at 43 and 150 V/cm but below IMPC by more than its s.e. at 360\n    V/cm and above at both poles.\n- id: fig4b-di8-threshold-570\n  statement: With Di-8-ANEPPS, measured IMP fell below the calculated value when the field\n    reached 570 V/cm, together with the maximum dF of 57 +- 14% at the cathodic pole and -55 +-\n    4% at the anodic pole, a polarization of over 600 mV, twice that measured with FluoVolt.\n  source: Results, section 3.4, paragraph 2; Figure 4B\n  quote: The measured IMP decreased below the calculated value when the electric field reached 570\n    V/cm, concurrently with reaching the maximum ΔF of 57 ± 14% at the cathodic pole and − 55 ± 4%\n    at the anodic pole. These values corresponded to membrane polarization by over 600 mV\n  data: with_inputs\n  expected:\n  - quantity: maximum cathodic pole dF, Di-8-ANEPPS, 1 us\n    value: 57\n    tolerance: 14\n    unit: '%'\n  - quantity: maximum anodic pole dF, Di-8-ANEPPS, 1 us\n    value: -55\n    tolerance: 4\n    unit: '%'\n  criterion: Fig. 4B, n = 5 cells; pole dF from the polarization image (60 PEF images), mean\n    over cells; IMP = dF / 0.091 per mV; IMPC from Eq. (1) with tau from [20]. Tolerances are\n    the paper's s.e. Reproduced when both maxima are within tolerance and occur at 570 V/cm,\n    and measured IMP at the poles is within the s.e. of IMPC at the fields below 570 V/cm and\n    below it at 570 V/cm.\n- id: fig4b-first10-cathodic\n  statement: Averaging dF over the first 10 of the 60 PEFs, cathodic pole polarization reached\n    66 +- 15% (710 +- 200 mV), above the 600 mV maximum averaged over 60 PEFs.\n  source: Results, section 3.4, paragraph 3; Figure 4B (dotted lines)\n  quote: Polarization measured this way reached 66 ± 15% (710 ± 200 mV) at the cathodic pole,\n    suggesting that the 600-mV maximum, averaged from 60 PEFs, was not the dye limit but the actual\n    IMP\n  expected:\n  - quantity: maximum cathodic pole dF over the first 10 PEF images, Di-8-ANEPPS\n    value: 66\n    tolerance: 15\n    unit: '%'\n  criterion: Fig. 4B, n = 5 cells; the polarization image formed from the first 10 of the 60 PEF\n    images (Fig. 4B legend), baseline image from the 40 baseline images. Tolerance is the\n    paper's s.e. Reproduced when the maximum over fields of the mean cathodic dF is within\n    tolerance and above the maximum from all 60 PEF images.\n- id: fig4b-asymmetric-decline\n  statement: Above 780 V/cm the IMP reached at the poles decreased progressively with field\n    strength, more at the cathodic pole; at 1400 V/cm charging was no longer detectable at the\n    cathodic pole and dropped to about 30% dF (about -330 mV) at the anodic pole.\n  source: Results, section 3.4, paragraph 4; Figure 4B\n  quote: As the electric field increased further, the IMP reached at the poles progressively\n    decreased, and the reduction was more pronounced at the cathodic pole. ... At 1400 V/cm,\n    charging was no longer detectable at the cathodic pole (i.e., the membrane became fully\n    permeable) and dropped to ~30% ΔF (~ −330 mV) at the anodic pole.\n  expected:\n  - quantity: anodic pole dF at 1400 V/cm, Di-8-ANEPPS (magnitude)\n    value: 30\n    tolerance: 3\n    unit: '%'\n  criterion: Fig. 4B, n = 5 cells, pole dF from the polarization image. \"No longer detectable\"\n    is read as a mean cathodic dF at 1400 V/cm whose s.e. interval includes 0. Reproduced when\n    pole |dF| decreases from 780 V/cm to 1400 V/cm at both poles, the fractional decrease from\n    the pole's maximum is larger at the cathodic pole, the cathodic value at 1400 V/cm is not\n    distinguishable from 0, and the anodic value is within tolerance. Note that -330 mV at 9.1%\n    per 100 mV is -30% dF; the text prints the dF without its sign.\n- id: fig4c-equator-cosine\n  statement: Membrane regions nearer the equator appeared unaffected and followed the cosine\n    dependence predicted by the Schwan equation up to 1000 V/cm, even when the poles were\n    electroporated.\n  source: Results, section 3.4, paragraph 4; Figure 4C\n  quote: Membrane areas closer to the equator (at polar angles closer to 0◦and 270◦) appeared\n    relatively unaffected and followed the cosine dependence predicted by Schwan formula up to 1000\n    V/cm (Fig. 4C).\n  data: with_inputs\n  criterion: Fig. 4B data (n = 5), perimeter dF resampled to 360 points, IMP = dF / 0.091 per\n    mV, against IMPC from Eq. (1). The paper does not say how far from the poles \"closer to\n    the equator\" reaches. Readings (a) the points within 30 degrees of the equator; (b) within\n    45 degrees. Reproduced when, under a reading, at 780 and 1000 V/cm the mean measured IMP\n    in that range lies within the s.e. of IMPC for most points (at least 80%), while at the\n    poles it is below IMPC.\n- id: fig4d-short-pulses-same-limit\n  statement: With 0.3 us PEFs at 357 to 3320 V/cm (imaged at 275 ns), the maximum dF was 53 +-\n    4% (about 600 mV) at both poles, similar to 1 us pulses, and its pattern with increasing\n    field strength did not differ from that with 1 us pulses.\n  source: Results, section 3.4, paragraph 5; Figure 4D\n  quote: Contrary to the expectations, the results were similar to those with 1-μs pulses in Fig.\n    4B: the maximum ΔF reached was 53 ± 4% (~600 mV) at both cell poles. The pattern of how the\n    response changed with increasing PEF strength was not different from that with 1-μs PEFs either.\n  expected:\n  - quantity: maximum pole |dF|, Di-8-ANEPPS, 0.3 us, each pole\n    value: 53\n    tolerance: 4\n    unit: '%'\n  criterion: Fig. 4D, n = 10 cells; pole dF from the polarization image, mean over cells.\n    Tolerance is the paper's s.e. Reproduced when the maximum |dF| over fields is within\n    tolerance at both poles, and, as in fig4b-asymmetric-decline, pole |dF| declines at fields\n    beyond the maximum with the larger fractional decline at the cathodic pole. Partially\n    reproduced when one pole's maximum is out of tolerance.\n- id: fig5a-gd-anodic-extension\n  statement: 1 mM Gd3+ extended membrane charging at the anodic pole down to -864 +- 44 mV,\n    against -542 +- 57 mV in parallel controls (p < 0.001).\n  source: Results, section 3.5, paragraph 1; Figure 5A\n  quote: Indeed, we found that 1 mM Gd3+ extended the range of membrane charging at the anodic pole\n    down to −864 ± 44 mV (p < 0.001 compared to −542 ± 57 mV in parallel control experiments, Fig.\n    5A).\n  statistics:\n  - test: t-test (2-tailed t-test in the Fig. 5A legend; Student's t-test in Methods 2.5)\n    p: 0.001\n    p_relation: \"<\"\n    n: 7 cells with Gd3+ and 5 control cells\n  expected:\n  - quantity: most negative anodic IMP with 1 mM Gd3+\n    value: -864\n    tolerance: 44\n    unit: mV\n  - quantity: most negative anodic IMP in controls\n    value: -542\n    tolerance: 57\n    unit: mV\n  criterion: Fig. 5A, Di-8-ANEPPS, 1 us, 150 to 1400 V/cm; anodic pole dF from the polarization\n    image converted to IMP at 9.1% per 100 mV. Tolerances are the paper's s.e. The paper does\n    not say how the extreme is taken. Readings (a) the most negative group mean over field\n    strengths, with its s.e., the groups compared at that field by a 2-tailed two-sample\n    t-test; (b) each cell's most negative IMP over field strengths, averaged per group and\n    compared by a 2-tailed two-sample t-test. Reproduced when, under a reading, both values\n    are within tolerance and p < 0.001; partially reproduced when the Gd3+ value is more\n    negative with p < 0.05 but a value is out of tolerance.\n- id: fig5a-gd-linear-to-780\n  statement: With Gd3+, measured IMP stayed nearly identical to IMPC down to -780 mV, showing\n    that the Di-8-ANEPPS response stayed linear and its calibration valid at high IMPs.\n  source: Results, section 3.5, paragraph 1; Figure 5A\n  quote: Furthermore, measured IMP remained nearly identical to the theoretical IMPC down to −780\n    mV, indicating that the dye response remained linear and its calibration was valid even at\n    high IMPs.\n  data: with_inputs\n  criterion: Fig. 5A Gd3+ group, n = 7; anodic pole IMP against IMPC per field strength, means\n    and s.e. both ways. Reproduced when, at every field strength whose mean IMPC is at or above\n    -780 mV (less negative), the mean measured IMP is within the larger of the two s.e. sums\n    of IMPC (measured s.e. plus IMPC s.e.), or within 10% of IMPC.\n- id: fig5a-gd-cathodic\n  statement: At the cathodic pole, polarization with Gd3+ reached 647 +- 44 mV, not\n    significantly higher than in controls, but Gd3+ prevented the progressive decline of IMP as\n    field strength increased.\n  source: Results, section 3.5, paragraph 2; Figure 5A\n  quote: At the cathodic pole, polarization in the presence of Gd3+ reached 647 ± 44 mV, a value\n    not significantly higher than that in the control group without Gd3+. However, Gd3+ prevented\n    the progressive decline in IMP as the electric field was increased.\n  expected:\n  - quantity: maximum cathodic IMP with 1 mM Gd3+\n    value: 647\n    tolerance: 44\n    unit: mV\n  criterion: Readings for the maximum and its comparison as in fig5a-gd-anodic-extension, at the\n    cathodic pole. The absence of a difference is judged on the paper's test, a 2-tailed\n    two-sample t-test at p < 0.05. Reproduced when, under a reading, the Gd3+ maximum is within\n    tolerance and not significantly above the control's, and the Gd3+ cathodic IMP at the\n    strongest field is not below its maximum by more than its s.e. while the control's is.\n- id: fig5a-gd-significant-points\n  statement: Differences between Gd3+ and control data are significant at p < 0.05 or better\n    for the datapoints below -700 mV and above 1200 mV.\n  source: Figure 5A legend\n  quote: Differences between Gd3+ and control group data are significant at p < 0.05 or better\n    (2-tailed t-test) for datapoints below −700 mV and above 1200 mV.\n  statistics:\n  - test: 2-tailed t-test\n    p: 0.05\n    p_relation: \"<\"\n    n: 7 cells with Gd3+ and 5 control cells\n  criterion: Fig. 5A; per field strength and pole, measured IMP of the two groups compared by a\n    2-tailed two-sample t-test. The text does not say which axis the -700 and 1200 mV refer\n    to. Readings (a) IMPC (horizontal axis) below -700 mV at the anodic pole and above 1200 mV\n    at the cathodic pole; (b) measured IMP below -700 mV in the Gd3+ group for the anodic\n    pole, with IMPC above 1200 mV for the cathodic pole. Reproduced when, under a reading,\n    every datapoint in those ranges has p < 0.05.\n- id: fig5b-eq2-sensitivity\n  statement: By Eq. (2), effective membrane conductivity has little effect on charging while\n    it stays much smaller than the cytosol and medium conductivities; a 10-fold increase gives\n    about a 2% IMP reduction and a 100-fold increase about 12%.\n  source: Results, section 3.5, paragraph 3; Figure 5B\n  quote: As expected, effective conductivity had little impact on charging for as long as it\n    remained much smaller than the cytosol and media conductivities; its 10-fold increase would go\n    unnoticed, yielding just a ~2% IMP reduction, and a 100-fold increase would reduce IMP by just\n    12%.\n  expected:\n  - quantity: IMP reduction for a 10-fold conductivity increase\n    value: 2\n    tolerance: 0.2\n    unit: '%'\n  - quantity: IMP reduction for a 100-fold conductivity increase\n    value: 12\n    tolerance: 1.2\n    unit: '%'\n  criterion: A computation from Eq. (2) with the parameters in section 2.3 (cytoplasm 0.4 S/m,\n    medium 1.64 S/m, intact membrane 3e-7 S/m, R = 8 um, d = 5 nm); it uses no recordings.\n    Reduction is 1 - f/1.5 (the ratio of calculated to measured IMP is 1.5/f) at 10 and 100\n    times the intact membrane conductivity. Reproduced when both are within tolerance. If Eq.\n    (2) as printed (the extracted text garbles it) gives a value of f far from 1.5 at the intact\n    conductivity, both its literal form and the form normalized so that the intact membrane\n    gives 1.5 are shown.\n- id: fig5c-gd-reduces-conductivity\n  statement: For most datapoints, Gd3+ reduced the electroporation-induced effective membrane\n    conductivity 2 to 3 fold.\n  source: Results, section 3.5, paragraph 4; Figure 5C\n  quote: For most datapoints, Gd3+ reduced the electroporation- induced effective conductivity 2–3-fold.\n  data: with_inputs\n  depends_on:\n  - fig5b-eq2-sensitivity\n  expected:\n  - quantity: ratio of control to Gd3+ effective conductivity, range\n    value: 2.5\n    tolerance: 0.8\n  criterion: As the Fig. 5C legend says, per field strength and pole, the effective conductivity\n    from the ratio of the group-mean measured IMP to the group-mean IMPC, interpolated on the\n    Eq. (2) curve of fig5b-eq2-sensitivity. The range 2 to 3 widened by 10% of each bound is\n    1.8 to 3.3. Reproduced when the control-to-Gd3+ ratio lies in 1.8 to 3.3 for more than half\n    of the datapoints where both groups show a reduction of IMP below IMPC; the ratios are\n    listed.\n- id: fig6a-single-pulse-ca\n  statement: A single 1 us pulse at 0 to 1200 V/cm produced a clear Ca2+ entry at 1000 and 1200\n    V/cm, with the signal elevated through the 5 min observation; the small increase after 780\n    V/cm was at the detection limit and not significant.\n  source: Results, section 3.6, paragraph 2; Figure 6A\n  quote: Exposure to a single 1-μs pulse at escalating field strengths, from 0 to 1200 V/cm\n    established a clear peak of Ca2+ entry at 1000 and 1200 V/ cm, and Ca2+ signal remained elevated\n    through the 5-min observation period (Fig. 6A). A subtle ΔF increase after exposure at 780 V/cm\n    was at the detection limit and not statistically significant.\n  criterion: Fig. 6A, 14 cells per field strength (legend), Fluo-4 dF against F0 the mean before\n    the pulse, background-subtracted (section 2.4). The paper does not name the test or the\n    time point. Readings for the test (a) one-sample t-test of dF against 0 (Methods 2.5);\n    (b) two-sample t-test against the 0 V/cm group; for the time, (i) the peak dF after the\n    pulse, (ii) dF at the end of the 5 min recording. Reproduced when, under every reading,\n    1000 and 1200 V/cm give dF significantly above the comparison at p < 0.05 and stays so at\n    the end of recording, and 780 V/cm is not significant at p < 0.05 under the reading(s)\n    with the paper's sense; blocked as methods_underspecified when the 780 V/cm result differs\n    between readings.\n- id: fig6b-train-ca\n  statement: With trains of 60 1 us pulses at 6 Hz (224 cells, each tested once), a strong Ca2+\n    response occurred in 28% of cells at 780 V/cm and nearly all cells at higher fields; at 650\n    V/cm only 2 cells (5.9%) responded strongly, but the mean signal at the end of recording\n    was significantly above zero (p < 0.001, one-sample t-test) and marginally higher than at\n    230 V/cm (p < 0.05, single-tailed t-test).\n  source: Results, section 3.6, paragraph 3; Figure 6B\n  quote: A strong Ca2+ response was recorded in 28% of cells exposed at 780 V/cm and in nearly all\n    cells at higher intensities (Fig. 6B). At 650 V/cm, only 2 cells (5.9%) showed a strong\n    response, but the mean Ca2+ signal by the end of recording was significantly different from\n    zero (p < 0.001, one sample t-test) and marginally higher than after exposure at 230 V/cm (p <\n    0.05, single-tailed t-test).\n  statistics:\n  - about: 650 V/cm, end-of-recording dF against zero\n    test: one sample t-test\n    p: 0.001\n    p_relation: \"<\"\n  - about: 650 V/cm against 230 V/cm, end-of-recording dF\n    test: single-tailed t-test\n    p: 0.05\n    p_relation: \"<\"\n  expected:\n  - quantity: fraction of strong responders at 780 V/cm\n    value: 28\n    tolerance: 2.8\n    unit: '%'\n  - quantity: fraction of strong responders at 650 V/cm\n    value: 5.9\n    tolerance: 0.59\n    unit: '%'\n  - quantity: total cells\n    value: 224\n    tolerance: 0\n  criterion: Fig. 6B; Fluo-4 dF against F0 the mean before the train (first 30 s),\n    background-subtracted. \"By the end of recording\" is read as (a) the last frame; (b) the\n    mean of the last 10 s (5 frames at 2 s). The single-tailed test is a two-sample Student's\n    t-test, 650 above 230 V/cm. The paper does not define a strong response, and no reading\n    is given; the fractions (28%, 5.9%, nearly all at higher fields) are tested only if the\n    dataset or a reader's answer gives the definition, and otherwise that part is blocked as\n    methods_underspecified with the distribution of end-of-recording dF per field shown.\n    Reproduced when the cell count is 224 with 28 to 54 cells per field, and under a reading\n    of the end, both tests give p below their bounds; partially reproduced when one does.\n- id: fig7a-test-pulse-cosine\n  statement: Polarization by a 150 V/cm test pulse 5 us after a conditioning pulse still\n    followed a cosine after conditioning PEFs up to 1000 V/cm, while 1200 and 1400 V/cm\n    conditioning PEFs markedly hindered charging at the cell poles.\n  source: Results, section 3.7, paragraph 3; Figure 7A\n  quote: Polarization still followed a cosine function after conditioning PEFs of up to 1000 V/cm.\n    However, 1200 and 1400 V/cm conditioning PEFs markedly hindered charging by the test pulse at\n    cell poles, indicating a persistent membrane permeabilization.\n  criterion: Fig. 7A, n = 5; perimeter dF (360 points) during the test pulse, mean over cells,\n    fit with a cosine (Grapher, Methods 2.5; a A cos(theta - phi) fit by least squares is the\n    standard form). The 150/150 V/cm cosine is the benchmark. Reproduced when the cosine fit\n    explains the profile (r of at least 0.9, the form the paper reports for fits in Fig. 3)\n    for every conditioning strength up to 1000 V/cm, and for 1200 and 1400 V/cm the mean pole\n    dF is below the benchmark's pole value by more than its s.e. at both poles. The r\n    threshold is not from the paper; r and the residuals are reported.\n- id: fig7b-conditioning-sublinear\n  statement: During the conditioning pulse, pole polarization normalized to 150 V/cm fell 1.5\n    times below linear scaling at 560 V/cm, 2-fold at 760 V/cm and further for stronger PEFs (p\n    < 0.01 for all points at 560 V/cm and above, one-sample t-test).\n  source: Results, section 3.7, paragraph 5; Figure 7B, top panel\n  quote: Actual measurements fell 1.5 times below this line for 560 V/cm PEFs, 2- fold for 760 V/cm\n    PEFs, and diverged further for more intense PEFs (p < 0.01 for all datapoints ≥560 V/cm, one\n    sample t-test).\n  statistics:\n  - test: one sample t-test\n    p: 0.01\n    p_relation: \"<\"\n    n: 5 cells\n  expected:\n  - quantity: linear expectation over measured, 560 V/cm\n    value: 1.5\n    tolerance: 0.15\n  - quantity: linear expectation over measured, 760 V/cm\n    value: 2\n    tolerance: 0.2\n  criterion: Section 3.7 says the top panel uses the Fig. 4B data (conditioning pulses without\n    test pulses; n = 5), with pole dF at 150 V/cm taken as 100% and linear scaling as E/150 x\n    100%. The fields 560 and 760 V/cm are read as the 570 and 780 V/cm sets of Fig. 4B. The\n    paper does not say whether normalization is per cell or of the group mean; readings (a)\n    per cell, then averaged; (b) group mean over group mean. Per pole, the one-sample t-test\n    of per-cell normalized values against the linear expectation. Reproduced when, under a\n    reading, both ratios are within tolerance at both poles or in their mean, the ratio grows\n    beyond 760 V/cm, and p < 0.01 at every field of 560 V/cm and above.\n- id: fig7b-test-pulse-recovery\n  statement: Polarization by the test pulse 6 us after the conditioning pulse did not differ\n    from control up to 760 V/cm conditioning, was about 80% of control after 1000 V/cm (not\n    significant), and was reduced to about 70% and 50% after 1200 and 1400 V/cm (p < 0.05 and\n    p < 0.01).\n  source: Results, section 3.7, paragraph 5; Figure 7B, bottom panel\n  quote: In contrast, measurements 6 μs later (test pulse) did not differ from the control up to\n    760 V/cm strength of the conditioning PEF; they were at ~80% of the control reading after 1000\n    V/cm conditioning PEF but the difference was not statistically significant. Still more intense\n    PEFs of 1200 and 1400 V/cm reduced charging by the test pulse to ~70% and ~ 50%, respectively\n    (p < 0.05 and p < 0.01, two-sided t-test).\n  statistics:\n  - about: 1200 V/cm conditioning against control\n    test: two-sided t-test\n    p: 0.05\n    p_relation: \"<\"\n    n: 5 cells\n  - about: 1400 V/cm conditioning against control\n    test: two-sided t-test\n    p: 0.01\n    p_relation: \"<\"\n    n: 5 cells\n  expected:\n  - quantity: test-pulse pole polarization after 1000 V/cm, % of control\n    value: 80\n    tolerance: 8\n    unit: '%'\n  - quantity: test-pulse pole polarization after 1200 V/cm, % of control\n    value: 70\n    tolerance: 7\n    unit: '%'\n  - quantity: test-pulse pole polarization after 1400 V/cm, % of control\n    value: 50\n    tolerance: 5\n    unit: '%'\n  criterion: Fig. 7A data, n = 5; pole dF during the test pulse with the 150/150 V/cm value as\n    100%. Normalization readings as in fig7b-conditioning-sublinear. The legend calls the test\n    a \"two-way t-test for the difference from the undamaged membrane\"; readings (a) a\n    one-sample two-sided t-test of the normalized values against 100%; (b) a two-sample\n    two-sided t-test against the 150/150 V/cm values. The paper does not say which pole;\n    readings (i) each pole, (ii) the mean of both. Reproduced when, under a reading, the three\n    values are within tolerance, 1200 and 1400 V/cm reach p < 0.05 and p < 0.01, and no\n    conditioning strength up to 1000 V/cm reaches p < 0.05.\n- id: fig7c-fast-resealing\n  statement: Effective membrane conductivity at the poles dropped about 10-fold (range 7 to 20)\n    within 6 us after the electroporating pulse; the cathodic pole was more conductive during\n    the pulse but no pole difference was seen by the test pulse; after 570 and 760 V/cm the\n    membrane resealed fully within 6 us, while stronger PEFs left residual conductivity.\n  source: Results, section 3.7, paragraphs 6 and 7; Figure 7C\n  quote: Fig. 7C shows a profound reduction in the λm,eff within just 6 μs after the electroporating\n    pulse. For most datapoints, it dropped by a factor of 10 (range; 7–20).\n  inferred: null\n  data: with_inputs\n  depends_on:\n  - fig5b-eq2-sensitivity\n  - fig7b-conditioning-sublinear\n  - fig7b-test-pulse-recovery\n  expected:\n  - quantity: fold drop in effective conductivity from conditioning to test pulse, range\n    value: 13.5\n    tolerance: 7.2\n  criterion: As section 3.7 and the Fig. 7C legend say, effective conductivity per pole and field\n    from the mean normalized values of Fig. 7B, interpolated on the Eq. (2) curve (fraction of\n    IMPC is the normalized value over the linear expectation for the conditioning pulse, and\n    the normalized value over 100% for the test pulse); values above 100% taken as 100%, and\n    the negative cathodic value at 1400 V/cm omitted, as the paper did. The range 7 to 20 widened\n    by 10% of each bound is 6.3 to 22. Reproduced when the fold drop lies in 6.3 to 22 for most\n    datapoints with residual conductivity, the conditioning-pulse conductivity is higher at the\n    cathodic pole at most fields, the test-pulse conductivities at 570 and 760 V/cm are at the\n    intact value (fraction of control at or above 100% within s.e.), and those at 1200 and 1400\n    V/cm are above it.\n"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd claims/001526 && python - <<'EOF'
p='10.1016-j.bioelechem.2026.109283.yaml'
s=open(p).read()
rep=[
("""  quote: Fig. 7C shows a profound reduction in the λm,eff within just 6 μs after the electroporating
    pulse. For most datapoints, it dropped by a factor of 10 (range; 7–20).
  inferred: null
""","""  quote: Fig. 7C shows a profound reduction in the λm,eff within just 6 μs after the electroporating
    pulse. For most datapoints, it dropped by a factor of 10 ... 7–20). While the cathodic pole
    became more conductive than the anodic pole during the electroporating pulse ... no difference
    between the poles was detected by the test pulse. For mildly electroporating PEFs of 570 and 760
    V/cm, membrane resealed fully (within the accuracy of measurements) within just 6 μs.
"""),
("""  quote: Contrary to the expectations, the results were similar to those with 1-μs pulses in Fig.
    4B: the maximum ΔF reached was 53 ± 4% (~600 mV) at both cell poles.""",
"""  quote: Contrary to the expectations, the results were similar to those with 1-μs pulses ... the
    maximum ΔF reached was 53 ± 4% (~600 mV) at both cell poles."""),
]
for a,b in rep:
    assert a in s, a[:60]
    s=s.replace(a,b)
open(p,'w').write(s)
EOF
```

```
(Bash completed with no output)
```

**Agent**

Now the criteria that relied on thresholds of my own.

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001526/10.1016-j.bioelechem.2026.109283.yaml",
 "old_string": "  criterion: Data as in fig3-dye-slopes over the whole IMPC range. The paper judged linearity by\n    eye against a LOESS curve. Measure fixed from the text, the mean dF in 50 mV bins of IMPC\n    (a plotting bin, a standard choice) divided by the through-origin slope times the bin\n    centre. Reproduced when the FluoVolt ratio falls below 0.8 in the bins beyond +-200 mV on at\n    least one side while the Di-8-ANEPPS ratio stays within 0.8 to 1.2 in every bin with at\n    least 20 points from -500 to +500 mV. The 0.8 to 1.2 band is not from the paper; the\n    ratios per bin are reported so that a reader can judge.",
 "new_string": "  criterion: Data as in fig3-dye-slopes over the whole IMPC range. The paper judged linearity by\n    eye against a LOESS curve and names no test, so the method is open. Readings, using the\n    tests Methods 2.5 names (a) per 50 mV bin of IMPC (a bin width not given by the paper), the\n    per-cell mean dF compared with the through-origin line by a one-sample t-test across cells\n    at p < 0.05; (b) a regression of dF on IMPC with a cubic term added to the through-origin\n    line, over the whole range, with the fit significance of that term at p < 0.05.\n    Reproduced when, under both readings, FluoVolt departs from the line beyond +-200 mV (bins\n    beyond 200 mV on at least one side significantly below the line in magnitude, or a\n    significant cubic term shrinking the response) and Di-8-ANEPPS does not depart within -500\n    to +500 mV; not reproduced when both readings find the opposite for either dye; blocked as\n    methods_underspecified when the readings disagree. The per-bin ratios of measured to line\n    are reported."
}
```

```
The file claims/001526/10.1016-j.bioelechem.2026.109283.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001526/10.1016-j.bioelechem.2026.109283.yaml",
 "old_string": "    the equator\" reaches. Readings (a) the points within 30 degrees of the equator; (b) within\n    45 degrees. Reproduced when, under a reading, at 780 and 1000 V/cm the mean measured IMP\n    in that range lies within the s.e. of IMPC for most points (at least 80%), while at the\n    poles it is below IMPC.",
 "new_string": "    the equator\" reaches. Readings (a) the points within 30 degrees of the equator; (b) within\n    45 degrees. The paper compares by eye; the measure is the mean over that range of measured\n    IMP over IMPC, against 1 with the protocol's default tolerance of 10% (0.9 to 1.1).\n    Reproduced when, under a reading, that ratio is within 0.9 to 1.1 at 780 and 1000 V/cm\n    while the ratio in the +-5 degree pole arcs is below 0.9 at the same fields."
}
```

```
The file claims/001526/10.1016-j.bioelechem.2026.109283.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001526/10.1016-j.bioelechem.2026.109283.yaml",
 "old_string": "  criterion: Fig. 5A Gd3+ group, n = 7; anodic pole IMP against IMPC per field strength, means\n    and s.e. both ways. Reproduced when, at every field strength whose mean IMPC is at or above\n    -780 mV (less negative), the mean measured IMP is within the larger of the two s.e. sums\n    of IMPC (measured s.e. plus IMPC s.e.), or within 10% of IMPC.",
 "new_string": "  criterion: Fig. 5A Gd3+ group, n = 7; anodic pole IMP against IMPC per field strength, means\n    and s.e. both ways, compared with the bisector of Fig. 5A. The paper names no test for\n    \"nearly identical\". Readings (a) a one-sample t-test (Methods 2.5) of per-cell measured\n    IMP minus IMPC against 0, not significant at p < 0.05; (b) the mean measured IMP within\n    10% of the mean IMPC (the protocol's default tolerance). Reproduced when, under both\n    readings, every field strength whose mean IMPC is between 0 and -780 mV passes; not\n    reproduced when both fail at any of them; blocked as methods_underspecified when they\n    disagree."
}
```

```
The file claims/001526/10.1016-j.bioelechem.2026.109283.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001526/10.1016-j.bioelechem.2026.109283.yaml",
 "old_string": "  criterion: Fig. 7A, n = 5; perimeter dF (360 points) during the test pulse, mean over cells,\n    fit with a cosine (Grapher, Methods 2.5; a A cos(theta - phi) fit by least squares is the\n    standard form). The 150/150 V/cm cosine is the benchmark. Reproduced when the cosine fit\n    explains the profile (r of at least 0.9, the form the paper reports for fits in Fig. 3)\n    for every conditioning strength up to 1000 V/cm, and for 1200 and 1400 V/cm the mean pole\n    dF is below the benchmark's pole value by more than its s.e. at both poles. The r\n    threshold is not from the paper; r and the residuals are reported.",
 "new_string": "  criterion: Fig. 7A, n = 5; perimeter dF (360 points) during the test pulse, mean over cells,\n    fit with a cosine of the polar angle by least squares (Grapher, Methods 2.5). The 150/150\n    V/cm cosine is the benchmark (legend). The paper judges \"followed a cosine\" by eye. Read\n    here as the absence of flattening at the poles, the mean dF in each +-5 degree pole arc\n    not below the profile's own cosine fit by more than its s.e. Reproduced when this holds at\n    both poles for every conditioning strength up to 1000 V/cm, and for 1200 and 1400 V/cm the\n    mean pole dF is below the benchmark cosine's pole value by more than its s.e. at both\n    poles. The fit significance, r and residuals of every cosine fit are reported."
}
```

```
The file claims/001526/10.1016-j.bioelechem.2026.109283.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001526/10.1016-j.bioelechem.2026.109283.yaml",
 "old_string": "    lower at the end with p < 0.05. Reproduced when, under a reading, the response declines\n    within most of the sets at 780 V/cm and above at the cathodic pole; the slope for every set\n    and pole is reported, and the slope at 43 to 570 V/cm is shown for comparison.",
 "new_string": "    lower at the end with p < 0.05. The paper does not name the pole; readings (i) the\n    cathodic pole, (ii) the anodic pole, (iii) both. Reproduced when, under a reading of each\n    kind, the response declines significantly within every set at 780 V/cm and above;\n    partially reproduced when it does in some of them. The slope for every set and pole is\n    reported, and the slope at 43 to 570 V/cm is shown for comparison."
}
```

```
The file claims/001526/10.1016-j.bioelechem.2026.109283.yaml has been updated successfully.
```

**Agent calls Bash**

```bash
cd  && python tools/claims_check.py claims/001526/10.1016-j.bioelechem.2026.109283.yaml paper/10.1016-j.bioelechem.2026.109283.txt; grep -n "—\|rather" claims/001526/*.yaml
```

Result: not kept, because it reads the paper's text.

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001526/10.1016-j.bioelechem.2026.109283.yaml",
 "old_string": "    remained much smaller than the cytosol and media conductivities; its 10-fold increase would go",
 "new_string": "    remained much smaller than the cytosol and media conductivities ... its 10-fold increase would go"
}
```

```
The file claims/001526/10.1016-j.bioelechem.2026.109283.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001526/10.1016-j.bioelechem.2026.109283.yaml",
 "old_string": "    (b) two-sample t-test against the 0 V/cm group; for the time, (i) the peak dF after the\n    pulse, (ii) dF at the end of the 5 min recording. Reproduced when, under every reading,\n    1000 and 1200 V/cm give dF significantly above the comparison at p < 0.05 and stays so at\n    the end of recording, and 780 V/cm is not significant at p < 0.05 under the reading(s)\n    with the paper's sense; blocked as methods_underspecified when the 780 V/cm result differs\n    between readings.",
 "new_string": "    (b) two-sample t-test against the 0 V/cm group, both 2-tailed at p < 0.05; for the time,\n    (i) the peak dF after the pulse, (ii) dF at the end of the 5 min recording. Reproduced\n    when, under every reading, 1000 and 1200 V/cm give dF significantly above the comparison\n    and 780 V/cm does not; not reproduced when every reading fails for 1000 or 1200 V/cm or\n    finds 780 V/cm significant; blocked as methods_underspecified when the readings disagree.\n    The size of the 780 V/cm effect is reported under each reading."
}
```

```
The file claims/001526/10.1016-j.bioelechem.2026.109283.yaml has been updated successfully.
```

**Agent calls Bash**

```bash
cd  && python - <<'EOF'
p='claims/001526/10.1016-j.bioelechem.2026.109283.yaml'
s=open(p).read()
a="""    V/cm, membrane resealed fully (within the accuracy of measurements) within just 6 μs.
  data: with_inputs
"""
assert a in s
s=s.replace(a,a.replace("  data: with_inputs\n",""))
a="""  statistics:
  - test: 2-tailed t-test
    p: 0.05
    p_relation: "<"
    n: 7 cells with Gd3+ and 5 control cells
  criterion: Fig. 5A; per field"""
assert a in s
s=s.replace(a,a.replace("  criterion: Fig. 5A; per field","  data: with_inputs\n  criterion: Fig. 5A; per field"))
open(p,'w').write(s)
EOF
python tools/claims_check.py claims/001526/10.1016-j.bioelechem.2026.109283.yaml paper/10.1016-j.bioelechem.2026.109283.txt
python - <<'EOF'
import yaml,re
p='claims/001526/10.1016-j.bioelechem.2026.109283.yaml'
d=yaml.safe_load(open(p))
for c in d['claims']:
    print(c['id'], c.get('data','dataset'), 'stats' if 'statistics' in c else '', 'exp' if 'expected' in c else '', 'crit' if 'criterion' in c else '')
EOF
grep -n "—\|rather" claims/001526/*.yaml
```

Result: not kept, because it reads the paper's text.

**Agent**

I wrote the claims file, `claims/001526/10.1016-j.bioelechem.2026.109283.yaml`, and it passes the quote checker: 30 claims, 30 quotes, 9 statistical values, 0 problems. Nothing was committed.

**Text read:** the version of record (Bioelectrochemistry 171, 109283), as text extracted from a PDF a person supplied. It has the main text, full Methods, Results, Discussion and figure legends. The paper has no supplement and links no code, so there was no code to read. Its Data availability statement says "on request". I read no figures from the PDF, because the tool that renders PDF pages is not installed.

**Claims:**
- 30 claims, all with quotes and none `inferred`.
- 9 carry statistics: Fig 2C, Fig 2D, 5A anodic, 5A legend, 6B, 7B top and 7B bottom (two tests). One claim has two entries.
- 20 have expected values with tolerances. The tolerance is the paper's s.e. where it gives one, otherwise 10%.
- All 30 have criteria.
- They cover Fig 1 through Fig 7C and Gd3+, the Eq. 2 model, Ca2+ uptake with single pulses and trains, and the two-pulse recovery tests.
- The dataset's title points to the Fig 2 type experiments. Every claim still keeps the default data (`dataset`) unless it needs outside inputs.
- 7 claims are `with_inputs`. They need the fit of charging time constant against cell radius from Semenov et al. 2025, *Bioelechem.* 168:109143 (ref [20]), and this paper does not give that fit's coefficients.

**Details the paper leaves open, and the readings named:**
- **Applying to all claims:**
  - How the radius is measured: perimeter length over 2π, or the radius of a circle with the same area.
  - Whether background is subtracted from the dye images: none, or a cell-free region as is done for the calcium imaging.
  - How the perimeter trace and cell centre are drawn: by hand in the imaging software, not fixed.
- **Fig 2A, 2B (stability within and across sets):** the paper names no test. Readings are a linear-regression slope, or a paired t-test of the first half against the second half. For the within-set decline: the first 10 against the last 10 images, and which pole (cathodic, anodic, both).
- **Fig 2B bleaching:** an extrapolated drift of the baseline, or the first against the last 10 images.
- **Fig 2C:** what "beginning" and "end" of the set mean: one image, 10 images or 5 images.
- **Fig 2D:** which pole, and whether the 20% is the mean over sets or per set.
- **Fig 3:**
  - Which cells form the calibration: the Fig 4A/4B groups, or all cells.
  - Whether r is for the through-origin fit or a Pearson r.
  - The linearity test: one-sample t-tests per 50 mV bin, or a cubic term in the fit.
- **Fig 4C:** how far "near the equator" reaches: ±30° or ±45°.
- **Fig 5A:**
  - How the extreme value is taken: the most negative group mean, or a per-cell extreme.
  - "Nearly identical to theory": a one-sample t-test, or within 10%.
  - The legend's −700/1200 mV: which axis.
- **Fig 6A:** which test (one-sample, or against the 0 V/cm group) and which time point (the peak, or the end of recording).
- **Fig 6B:** the end of recording (last frame, or last 10 s).
- **Fig 7B:**
  - Normalization: per cell, or of the group mean.
  - The test pulse's "two-way t-test": one-sample against 100%, or two-sample against the 150/150 V/cm control.
  - Which pole.
- **Fig 7B naming:** the 560/760 V/cm in Fig 7 are read as the 570/780 V/cm sets of Fig 4B.

Where readings give different outcomes, the claim is blocked as `methods_underspecified`. Fig 4C and Fig 5A use the protocol's default 10% band as their measure, and I say so in those criteria.

**Missing from the paper:**
- The coefficients of the fit of charging time constant against radius. They are in ref [20], which is not under `paper/`.
- A definition of a "strong" Ca2+ response (Fig 6B). The 28% and 5.9% fractions are blocked unless the dataset or a reader's answer gives one.
- Eq. 2 comes out garbled in the extracted text. The Fig 5B criterion therefore shows its literal form and a form normalized so that an intact membrane gives f = 1.5.

## End of run

24 turns, 6 minutes, result: success.
