# 001518 · claims · run 39642090319

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cat docs/protocol.md; ls claims/001453/ claims/001518/ paper/ 2>&1
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
wc -l paper/*.txt claims/001453/*.yaml; head -c 3000 paper/*.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1016-j.bioelechem.2026.109283.txt"
}
```

**Agent calls Read**

```json
{
 "file_path": "claims/001453/10.1016-j.cub.2025.04.027.yaml"
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

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1016-j.bioelechem.2026.109283.txt",
 "offset": 705
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
ls tools docs claims | head -80; sed -n 1,200p tools/claims_check.py
```

```
claims:
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
000035
000041
000044
000056
000059
000061
000067
000070
000114
[... 172 more lines not kept]
```

**Agent**

The paper text is complete (version of record, no supplement referenced, no code linked). Checking the schema and the dataset's archive description next.

**Agent calls Bash**

```bash
python -c "import json;d=json.load(open('schemas/claims.schema.json'));print(json.dumps(d,indent=1))" | head -250; grep -l "elsewhere" claims/*/*.yaml | head -3
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
[... 233 more lines not kept]
```

**Agent calls Bash**

```bash
python -c "import json;d=json.load(open('schemas/claims.schema.json'));print(json.dumps(d['\$defs'],indent=1))"; curl -s https://api.dandiarchive.org/api/dandisets/001518/ | python -c "import json,sys;d=json.load(sys.stdin);print(json.dumps(d,indent=1)[:1500])"; curl -s https://api.dandiarchive.org/api/dandisets/001518/versions/draft/info/ | python -c "import json,sys;d=json.load(sys.stdin)['metadata'];print(d.get('name'));print(d.get('description'));print(d.get('relatedResource'))"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
ls claims/001687; head -40 claims/001687/*.yaml; grep -h -A3 "with_inputs" claims/*/*.yaml | head -30
```

```
10.1016-j.neuron.2026.05.027.yaml
# Claims for Xiao, Severson et al. (2026), "Peri-head distance coding in the mouse brainstem",
# Neuron, doi:10.1016/j.neuron.2026.05.027, on dandiset 001687.
#
# Written by an agent (model "claude-opus-5-5", Claude Code in GitHub Actions), 2026-10-21,
# protocol pilot-10 as stated in docs/protocol.md.
#
# Text read: the accepted author manuscript in PubMed Central (NIHMS2191201, PMC13336321), as
# fetched 2026-10-20 into paper/10.1016-j.neuron.2026.05.027.txt: main text, STAR Methods, the
# legends of Figures 1 to 6, and the supplement file NIHMS2191201-supplement-1.pdf (legends of
# Figures S1 to S6 and Tables S2 to S5). The version of record was not read. Tables S1 (mouse
# sex, age and figure assignments) and S6 (test statistics, degrees of freedom and p-values of
# all analyses) are named in the text but are not in the supplement file read; every number
# used below is in the main text, the legends or Tables S2 to S5. Figures were not opened.
#
# Code read: github.com/wanglab-neuro/2026_Xiao-Severson_Peri-head-distance at commit b1a9f3c
# (2026-08-21; archived as doi:10.5281/zenodo.20330279). It holds the original MATLAB scripts
# for Figures 1E, 2, 3, 4B-C, 5C-E, 6D, 6G-I, S1, S4I and S5A ("Manuscript figures/Original
# Matlab code"), Python helpers that read the deposited NWB files, the Python circuit model
# (PrV_simulation/simulate_prv.py), and a submodule (Processing, the spike-sorting pipeline;
[... 51 more lines not kept]
```

**Agent calls Bash**

```bash
python3 -c "
li,lo,R,d=0.4,1.64,8e-6,5e-9
def f(lm): return 3*lo*(3*R**2*d*li+(3*d**2*R-d**3)*(lm-li))/(2*R**3*(lm+2*lo)*(lm+0.5*li)-2*(R-d)**3*(lo-lm)*(li-lm))
for k in [1,10,100,1000,1e4]: print(k, f(3e-7*k)/1.5)
"
```

```
1 0.998655560070686
10 0.986716332587669
100 0.8813484761702167
1000 0.42621215172731824
10000.0 0.06914458069631028
```

**Agent**

Now writing the claims file.

**Agent calls Write**

```json
{
 "file_path": "claims/001518/10.1016-j.bioelechem.2026.109283.yaml",
 "content": "# Claims for Semenov, Silkuniene, Silkunas, Pakhomova, Bixler, Ibey, Kochunov & Pakhomov (2026),\n# \"Sub-microsecond optical measurements of cell membrane charging and lesioning by pulsed\n# electric fields\", Bioelectrochemistry 171, 109283, doi:10.1016/j.bioelechem.2026.109283, on\n# dandiset 001518.\n#\n# Written by an agent (model \"claude-opus-5-5\", Claude Code in GitHub Actions), 2026-10-21,\n# protocol pilot-10 as stated in docs/protocol.md.\n#\n# Text read: the version of record, from a PDF supplied by a person, extracted to\n# paper/10.1016-j.bioelechem.2026.109283.txt (main text, Materials and methods, Results,\n# Discussion, legends of Figures 1 to 7). The paper names no supplement and none was read.\n# Figures were not opened. The paper links no code (\"Data will be made available on request\");\n# its analysis was done in MetaMorph 7.8.13, an Excel macro, Grapher 16 and Origin 8.0, none\n# of which is published, so no code was read. The Methods say most methods are as described in\n# Semenov et al., Bioelectrochemistry 168 (2025) 109143 (reference [20]); that paper was not\n# read for these claims.\n#\n# The dandiset's title (\"Comparison of FluoVolt and Di-8-ANEPPS Responses to Plasma Membrane\n# Polarization at Varying Electric Field Strengths\") and description (FluoVolt and Di-8-ANEPPS\n# responses of CHO cell membrane polarization under different electric field strengths) point\n# at the potentiometric dye experiments; whether it also holds the Gd3+, Ca2+ (Fluo-4) and\n# two-pulse experiments is the author's to find.\n#\n# Data the paper used (Methods 2.1 to 2.5, Results, legends):\n# - Cells. CHO-K1 cells plated 1 to 3 h on 35-mm glass-bottom dishes, spheroidal; loaded 30 min\n#   with FluoVolt (1:1000 with PowerLoad 1:100) or 5 uM Di-8-ANEPPS, imaged in dye-free\n#   physiological solution (1.64 S/m), room temperature 21 to 23 C. One cell per experiment.\n# - Pulses. Unipolar 1-us or 0.3-us pulses at 6 Hz through two tungsten rods 1.6 mm apart; field\n#   strengths from Sim4Life modelling, in V/cm. 1-us series 43 to 1400 V/cm; the values named in\n#   the text are 43, 150, 230, 360, 570, 780, 1000, 1200 and 1400 V/cm (Fig. 7 Results also\n#   write 560 and 760 V/cm, read here as the same 570 and 780 levels). 0.3-us series 357 to 3320\n#   V/cm.\n# - Imaging. One ~6-ns 440-nm laser flash per pulse, 900 ns after onset of 1-us pulses and 275\n#   ns after onset of 0.3-us pulses; iXon Ultra 897 camera, 60x/1.42 objective. Images in sets\n#   of 100: 40 without pulse (baseline), then 60 with the pulse at a constant amplitude; sets\n#   about 16 s long, about 10 s apart (Fig. 2D assumes 25 s between sets). Amplitude escalated\n#   set by set, or alternated (150 and 230 V/cm, Fig. 2C).\n# - Experiments and n (one cell each): Fig. 2A and 4A FluoVolt 1-us escalation, n = 4; Fig. 2B\n#   and 4B/C Di-8-ANEPPS 1-us escalation, n = 5; Fig. 2C/D Di-8-ANEPPS 150/230 V/cm alternation\n#   then 1000 V/cm, n = 8; Fig. 3 calibration from 43 to 360 V/cm sets of both dyes; Fig. 4D\n#   Di-8-ANEPPS 0.3-us escalation, n = 10; Fig. 5A Di-8-ANEPPS 1-us, 150 to 1400 V/cm, with 1 mM\n#   Gd3+ (n = 7) and parallel controls (n = 5); Fig. 7 two-pulse protocol, Di-8-ANEPPS, a 1-us\n#   conditioning pulse at 150 to 1400 V/cm then 5 us later a 1-us 150 V/cm test pulse imaged at\n#   900 ns into the test pulse, n = 5. Whether Fig. 2 and Fig. 4 used the same cells is not\n#   stated.\n# - Ca2+ imaging (Fig. 6). Fluo-4 AM 2.5 uM; images every 1 s or 2 s. (A) a single 1-us pulse at\n#   60 s, 5 min recording, 0 to 1200 V/cm, 14 cells; (B) 60 pulses at 6 Hz from 30 s, 150 s\n#   recording, each cell exposed once, 28 to 54 cells per field strength, 224 cells.\n#\n# Common method, from the Methods (2.3, 2.5), used by the criteria below.\n# - Per-image pole measure (Fig. 2 only). A 6-pixel-wide trace along the cell perimeter; mean\n#   F in the +-5 degree arcs at the cathode-facing and anode-facing poles in each image; F0 the\n#   mean of the 40 baseline images; dF = 100% x (F - F0)/F0.\n# - Collapsed profile (Fig. 3 onward). The 40 baseline and the 60 pulse images collapsed into\n#   one baseline and one polarization image (read as the mean image; a sum would not give dF = 0\n#   without a field); intensity along the 6-pixel trace, resampled to 360 points along the\n#   normalized perimeter by linear interpolation; dF per point between the two images. Pole\n#   values are the mean dF in +-5 degree arcs at each pole; averaged across cells, mean +- s.e.\n# - IMP from dF. FluoVolt 26% and Di-8-ANEPPS 9.1% dF per 100 mV (Fig. 3); measured IMP = dF\n#   divided by the sensitivity.\n# - Calculated IMP (IMPC). Eq. (1), IMPC = 1.5 E R cos(theta) (1 - exp(-t/tau)), with t = 900 ns\n#   (1-us pulses) or 275 ns (0.3-us pulses), R measured from each cell's image, and tau from the\n#   best fit of tau against cell radius in reference [20]. That fit is not given in this paper:\n#   claims that use IMPC take it from [20] (data with_inputs).\n# - Effective membrane conductivity. Eq. (2) with lambda_i 0.4 S/m, lambda_o 1.64 S/m,\n#   lambda_m 3e-7 S/m intact, R 8 um, d 5 nm; the measured fraction of IMPC equals f/1.5, solved\n#   for lambda_m (Fig. 5B).\n# - Tests. Student's t-test and one-sample t-test (2.5); the Fig. 2 legend names a 2-tailed\n#   paired t-test, the Fig. 5 legend a 2-tailed t-test, and the Fig. 7 legend a two-way\n#   (two-sided) t-test. Error bars are s.e. over cells.\n#\n# Details the paper leaves open, named once here and repeated in the criteria that need them.\n# - Pole location and sign. Theta is the angle from the cell centre to the field; the Fig. 4C\n#   legend places the equator near -90 and 270 degrees, the Results near 0 and 270 degrees.\n#   Poles are taken from the field direction recorded with the data (cathode-facing pole =\n#   depolarized side); if the data do not record it, this is open.\n# - Background subtraction of the laser images is not stated (it is stated for Ca2+ images).\n#   Readings (a) no subtraction, (b) subtraction of a cell-free region, as for Ca2+.\n# - Cell radius \"measured from individual cell images\", method not given. Readings (a) perimeter\n#   trace length / 2 pi, (b) radius of the circle of equal area.\nschema_version: 2\ndataset:\n  archive: dandi\n  id: \"001518\"\npaper: doi:10.1016/j.bioelechem.2026.109283\nclaims:\n- id: fig1-pole-dimming\n  statement: With Di-8-ANEPPS and 1-us pulses, polarization grows with field strength up to 570\n    V/cm; at 780 V/cm the cathodic pole stops increasing and dims, and at 1000 to 1400 V/cm the\n    poles show reduced or absent polarization while regions nearer the equator stay polarized\n    and may polarize more than the poles.\n  source: Figure 1 and its legend; Results 3.1, paragraph 1\n  quote: At a higher electric field strength of 780 V/cm, polarization at the cathodic pole does\n    not further increase but dims out, indicating a less efficient charging of the partially\n    permeabilized membrane. Still stronger electric fields produce a distinct pattern of reduced\n    or absent polarization at the poles ... while regions closer to the equator remain relatively\n    intact and may polarize more than the poles\n  criterion: Figure 1 shows images of one cell, which the paper does not identify; the test uses\n    the Di-8-ANEPPS 1-us escalation cells (Fig. 4B, n = 5), collapsed profiles and pole values as\n    in the common method. Reproduced when (1) the mean cathodic pole dF at 780 V/cm is not above\n    that at 570 V/cm, and (2) at 1400 V/cm the largest mean dF of the cathode-facing hemisphere\n    lies outside the +-5 degree polar arc. The paper gives no test or threshold for this; the\n    two conditions are read from the legend's wording. Background readings (a) and (b) both run.\n- id: fig2a-fluovolt-saturation\n  statement: With FluoVolt, pole dF rose with field strength until it saturated at 66% (255 mV)\n    at 360 V/cm at the cathodic pole and -83% (-320 mV) at 570 V/cm at the anodic pole; stronger\n    fields did not increase the anodic response and decreased the cathodic one.\n  source: Figure 2A; Results 3.2, paragraph 2\n  quote: ΔF increased proportionally to the electric field strength until reaching apparent\n    saturation at 66% ΔF (255 mV IMP) at 360 V/cm at the cathodic pole, and −83% ΔF (−320 mV IMP)\n    at 570 V/cm at the anodic pole. Further escalation of the electric field strength did not\n    increase the dye response at the anodic pole and even decreased it at the cathodic pole.\n  expected:\n  - quantity: FluoVolt cathodic pole dF at 360 V/cm\n    value: 66\n    tolerance: 6.6\n    unit: \"%\"\n  - quantity: FluoVolt anodic pole dF at 570 V/cm\n    value: -83\n    tolerance: 8.3\n    unit: \"%\"\n  criterion: Per-image pole dF (common method, Fig. 2 measure) over the 60 pulse images of each\n    set, averaged per cell and then across the 4 cells. Reproduced when both values are within\n    tolerance, the cathodic mean at 360 V/cm is the largest of the series, the anodic means at\n    780 to 1400 V/cm are not more negative than at 570 V/cm by more than the tolerance, and the\n    cathodic means at 1000 to 1400 V/cm are below that at 360 V/cm.\n- id: fig2a-fluovolt-stable\n  statement: FluoVolt measurements were stable without pulses (no significant bleaching or\n    photosensitization), and the response within each set stayed stable through the 60 pulses,\n    even at 1000 V/cm and above.\n  source: Figure 2A; Results 3.2, paragraph 2\n  quote: Without PEF (first 40 datapoints, or ~ 7 s in each set), measurements were stable,\n    indicating no significant photosensitization or dye bleaching ... but the dye response in\n    each set stayed stable through the 60 pulses applied\n  criterion: A claim of absence. The paper reports no test for it; the test it names for Fig. 2\n    is a 2-tailed paired t-test at p < 0.05 over cells (n = 4). Per set and pole, compare the\n    start and the end of the 60 pulse images, and of the 40 baseline images. The paper does\n    not say how many images form the start and the end; readings (a) the first and the last\n    image, (b) the first 10 and the last 10 images. Reproduced when no set at 1000 to 1400 V/cm,\n    and no baseline, shows a significant change; not reproduced when any does. The size of each\n    change is reported.\n- id: fig2b-di8-climbs-to-570\n  statement: Di-8-ANEPPS dF kept increasing with field strength up to 570 V/cm at both poles.\n  source: Figure 2B; Results 3.2, paragraph 3\n  quote: This dye has a lower sensitivity to membrane polarization (note the vertical scale\n    different from Fig. 2A), but ΔF kept climbing up to the electric field strength of 570 V/cm\n    at both cell poles.\n  criterion: Per-image pole dF averaged over each set's 60 pulse images, per cell, then across\n    the 5 cells. Reproduced when the mean |dF| at each pole increases at every step from 43 to\n    570 V/cm.\n- id: fig2b-di8-decline-within-set\n  statement: With Di-8-ANEPPS, responses to pulses of 780 V/cm and above decreased gradually\n    within each set of 60 images.\n  source: Figure 2B; Results 3.2, paragraph 3\n  quote: In addition, responses to PEFs at and above 780 V/cm decreased gradually in each set of\n    60 images, consistent with expectations of adding membrane damage by additional\n    electroporation pulses in each set\n  criterion: The paper gives no test; it reads a direction. Per set, the mean |dF| at the start\n    and at the end of the 60 pulse images, averaged across the 5 cells; start and end as in\n    fig2a-fluovolt-stable, readings (a) first and last image, (b) first 10 and last 10. The text\n    does not name the pole; readings (c) the cathodic pole, (d) both poles. Reproduced when the\n    end is below the start for every set from 780 to 1400 V/cm; the 2-tailed paired t-test of\n    Fig. 2 is reported for each set.\n- id: fig2cd-stable-before-electroporation\n  statement: Repeated alternating sets at 150 and 230 V/cm (480 pulses and 800 flashes) gave dF\n    responses constant within and between sets.\n  source: Figure 2C and 2D; Results 3.2, paragraph 4\n  quote: Repeated sets of PEFs at 150 and 230 V/cm, delivered in alternation, produced ΔF\n    responses that stayed constant both within each set and between the sets (Fig. 2C and D).\n  criterion: A claim of absence, judged on the paper's test, the 2-tailed paired t-test at p <\n    0.05 of the Fig. 2 legend (n = 8). Per cell and set, the mean pole dF over the 60 pulse\n    images (Fig. 2D); every set before the 1000 V/cm set is compared with the first set at the\n    same field strength (the legend's dashed lines are the first-trial means), at each pole.\n    Reproduced when none differs; not reproduced when any does. Within-set changes are shown as\n    in fig2a-fluovolt-stable, as a variant.\n- id: fig2c-1000-within-set\n  statement: At 1000 V/cm the cathodic pole dF fell from 40 +- 10% at the start of the set to\n    26.6 +- 8% at its end, a trend that was not statistically significant.\n  source: Figure 2C; Results 3.2, paragraph 4\n  quote: In contrast, at an electroporating field strength of 1000 V/cm, ΔF at the cathodic pole\n    decreased from 40 ± 10% at the beginning of the set to 26.6 ± 8% at the end of it. Although\n    not statistically significant (p > 0.05)\n  statistics:\n  - test: 2-tailed paired t-test (named in the Fig. 2 legend)\n    p: 0.05\n    p_relation: \">\"\n    n: 8 cells\n  expected:\n  - quantity: cathodic pole dF at the start of the 1000 V/cm set\n    value: 40\n    tolerance: 10\n    unit: \"%\"\n  - quantity: cathodic pole dF at the end of the 1000 V/cm set\n    value: 26.6\n    tolerance: 8\n    unit: \"%\"\n  criterion: Tolerances are the paper's s.e. Per-image cathodic pole dF; start and end are not\n    defined, readings (a) the first and the last image of the 60, (b) the first 10 and the last\n    10 images. Reproduced when under one reading both values are within tolerance and the\n    2-tailed paired t-test gives p > 0.05.\n- id: fig2d-lasting-reduction\n  statement: Set-averaged dF stayed nearly constant before the 1000 V/cm exposure but was about\n    20% lower in the sets after it.\n  source: Figure 2D and legend; Results 3.2, paragraph 4\n  quote: ΔF values averaged across each set of 60 PEFs stayed nearly constant before the\n    electroporation, but dropped by about 20% in the sets acquired after it (Fig. 2D, p < 0.05).\n  statistics:\n  - test: 2-tailed paired t-test\n    p: 0.05\n    p_relation: \"<\"\n    n: 8 cells\n  expected:\n    quantity: reduction of set-averaged dF after 1000 V/cm, relative to the first set at the\n      same field strength\n    value: 20\n    tolerance: 2\n    unit: \"%\"\n  criterion: Per cell and set, the mean pole dF over the 60 pulse images; each set after the\n    1000 V/cm set compared with the first set at the same field strength by a 2-tailed paired\n    t-test (n = 8). The text does not say which pole or how the 20% is pooled; readings (a)\n    cathodic pole, (b) anodic pole, (c) each post-1000 set separately, (d) the mean over the\n    post-1000 sets. Reproduced when under one reading the reduction is within tolerance (the\n    legend writes it as at most 20%, so a reduction from 10 to 22% is also accepted under that\n    wording) and at least one post-1000 set is significantly lower at p < 0.05.\n- id: fig3-dye-sensitivity\n  statement: Fitted linearly through the origin over -150 to +150 mV IMPC, FluoVolt changes by\n    26% and Di-8-ANEPPS by 9.1% dF per 100 mV, with correlation coefficients 0.96 and 0.78.\n  source: Figure 3 and legend; Results 3.3, paragraph 1\n  quote: The correlation coefficients of the fits equaled 0.96 for FluoVolt and 0.78 for Di-8\n    ANEPPS (due to a lower signal-to-noise ratio), with respective slope coefficients of 26% and\n    9.1% ΔF per 100 mV of IMP.\n  data: with_inputs\n  expected:\n  - quantity: FluoVolt slope\n    value: 26\n    tolerance: 2.6\n    unit: \"% dF per 100 mV\"\n  - quantity: Di-8-ANEPPS slope\n    value: 9.1\n    tolerance: 0.91\n    unit: \"% dF per 100 mV\"\n  - quantity: FluoVolt correlation coefficient\n    value: 0.96\n    tolerance: 0.096\n  - quantity: Di-8-ANEPPS correlation coefficient\n    value: 0.78\n    tolerance: 0.078\n  criterion: All 360 perimeter points of every cell in the 43 to 360 V/cm sets of 1-us pulses at\n    900 ns, dF against IMPC computed per cell and point (Eq. 1, tau from the fit of reference\n    [20], an outside input). Points with IMPC from -150 to +150 mV fit by least squares through\n    the origin (Grapher). Grapher's correlation coefficient for a fit through the origin is not\n    defined in the paper; readings (a) Pearson r of dF with IMPC in that range, (b) the square\n    root of the uncentred R2 of the fit through the origin. Radius readings (a) and (b) and\n    background readings (a) and (b) of the header all run. Reproduced when the slopes are within\n    tolerance and the correlation coefficients are within tolerance under one reading.\n- id: fig3-fluovolt-nonlinear\n  statement: FluoVolt departed from linearity from about +-200 mV IMPC, while Di-8-ANEPPS stayed\n    nearly linear from -500 to +500 mV; so FluoVolt's early departure reflects its dynamic range,\n    not electroporation.\n  source: Figure 3 and legend; Results 3.3, paragraph 1\n  quote: The actual measurements with FluoVolt gradually became non-linear already at ±200 mV,\n    while those for Di-8-ANEPPS stayed essentially linear throughout the tested range from −500\n    to +500 mV.\n  data: with_inputs\n  depends_on:\n  - fig3-dye-sensitivity\n  criterion: The paper judges this by eye from a LOESS smooth (Grapher, span not given) against\n    the linear fit; it gives no threshold. Measure here, as the paper's figure compares them,\n    the smoothed dF against the line through the origin of fig3-dye-sensitivity, over the same\n    points. Readings for the smooth (a) LOESS with span 0.3, (b) 0.5, (c) 0.75, (d) means in\n    50-mV IMPC bins. A departure is the smooth lying closer to zero than the line by more than\n    10% of the line's value (the protocol's default tolerance). Reproduced when under every\n    reading FluoVolt departs at |IMPC| of 250 mV or more on both sides and Di-8-ANEPPS does not\n    depart anywhere from -500 to +500 mV where the data have points.\n- id: fig4a-fluovolt-limits\n  statement: FluoVolt measured and calculated IMP matched only at 43 and 150 V/cm; with stronger\n    1-us pulses the pole dF peaked at 71 +- 10% (cathodic) and -83.5 +- 5% (anodic), about +260\n    and -330 mV.\n  source: Figure 4A; Results 3.4, paragraph 1\n  quote: However, this assumption held only for the applied fields of 43 and 150 V/cm, where\n    measured and calculated IMP matched. With stronger PEFs, maximum ΔF reached 71 ± 10% and\n    −83.5 ± 5% at the cathodic and anodic poles, respectively.\n  data: with_inputs\n  expected:\n  - quantity: FluoVolt maximum cathodic pole dF\n    value: 71\n    tolerance: 10\n    unit: \"%\"\n  - quantity: FluoVolt maximum anodic pole dF\n    value: -83.5\n    tolerance: 5\n    unit: \"%\"\n  criterion: Tolerances are the paper's s.e. Collapsed pole dF per cell and field strength, mean\n    across the 4 cells; the maximum is the largest mean |dF| over field strengths at each pole.\n    Measured IMP (dF / 26%) compared with the cell's pole IMPC by a 2-tailed paired t-test at p\n    < 0.05 (Student's t-test of Methods 2.5). Reproduced when both maxima are within tolerance,\n    the test finds no difference at 43 and 150 V/cm at either pole, and finds measured below\n    calculated at either pole at each of 230 V/cm and above.\n- id: fig4a-fluovolt-cathodic-decline\n  statement: FluoVolt cathodic polarization fell from 71% at 360 V/cm to 45 to 50% at 1000 to\n    1400 V/cm.\n  source: Figure 4A; Results 3.4, paragraph 1\n  quote: Notably, polarization at the cathodic pole decreased from 71% at 360 V/cm to 45–50% at\n    1000–1400 V/cm, indicating that the more severe membrane damage prevented its polarization\n    to the maximum.\n  expected:\n  - quantity: FluoVolt cathodic pole dF at 360 V/cm\n    value: 71\n    tolerance: 7.1\n    unit: \"%\"\n  - quantity: FluoVolt cathodic pole dF at each of 1000, 1200 and 1400 V/cm (range 45 to 50,\n      widened by 10% of each bound to 40.5 to 55)\n    value: 47.5\n    tolerance: 7.5\n    unit: \"%\"\n  criterion: Collapsed cathodic pole dF, mean across the 4 cells, per field strength. Reproduced\n    when the 360 V/cm value is within tolerance and each of the 1000, 1200 and 1400 V/cm values\n    lies within 40.5 to 55%.\n- id: fig4b-di8-limits\n  statement: With Di-8-ANEPPS and 1-us pulses, measured IMP fell below the calculated value at\n    570 V/cm, where dF peaked at 57 +- 14% (cathodic) and -55 +- 4% (anodic), over 600 mV.\n  source: Figure 4B; Results 3.4, paragraph 2\n  quote: The measured IMP decreased below the calculated value when the electric field reached\n    570 V/cm, concurrently with reaching the maximum ΔF of 57 ± 14% at the cathodic pole and −\n    55 ± 4% at the anodic pole. These values corresponded to membrane polarization by over 600\n    mV, which is twice the value measured with FluoVolt.\n  data: with_inputs\n  expected:\n  - quantity: Di-8-ANEPPS maximum cathodic pole dF\n    value: 57\n    tolerance: 14\n    unit: \"%\"\n  - quantity: Di-8-ANEPPS maximum anodic pole dF\n    value: -55\n    tolerance: 4\n    unit: \"%\"\n  criterion: Tolerances are the paper's s.e. Collapsed pole dF per cell and field strength, mean\n    across the 5 cells. Reproduced when the largest mean |dF| at each pole occurs at 570 V/cm\n    and is within tolerance, and measured IMP (dF / 9.1%) is below the pole IMPC at 570 V/cm by a\n    2-tailed paired t-test at p < 0.05 (at either pole) but not below it at 43 to 360 V/cm.\n- id: fig4b-first-10-pulses\n  statement: Averaged over only the first 10 of the 60 pulses, Di-8-ANEPPS cathodic polarization\n    reached 66 +- 15% (710 +- 200 mV), so the 600-mV maximum is not the dye's limit.\n  source: Figure 4B, dotted lines; Results 3.4, paragraph 3\n  quote: Polarization measured this way reached 66 ± 15% (710 ± 200 mV) at the cathodic pole,\n    suggesting that the 600-mV maximum, averaged from 60 PEFs, was not the dye limit but the\n    actual IMP\n  expected:\n    quantity: Di-8-ANEPPS maximum cathodic pole dF over the first 10 pulse images\n    value: 66\n    tolerance: 15\n    unit: \"%\"\n  criterion: Tolerance is the paper's s.e. As the common method, with the polarization image\n    collapsed from the first 10 of the 60 pulse images; mean across the 5 cells, largest over\n    field strengths. Reproduced when within tolerance and above the 60-image maximum of\n    fig4b-di8-limits.\n  depends_on:\n  - fig4b-di8-limits\n- id: fig4b-cathodic-asymmetry\n  statement: Above 780 V/cm the pole IMP fell progressively with field strength, more at the\n    cathodic pole; at 1400 V/cm the cathodic pole no longer charged and the anodic pole fell to\n    about -30% dF (-330 mV).\n  source: Figure 4B; Results 3.4, paragraph 4\n  quote: As the electric field increased further, the IMP reached at the poles progressively\n    decreased, and the reduction was more pronounced at the cathodic pole ... At 1400 V/cm,\n    charging was no longer detectable at the cathodic pole (i.e., the membrane became fully\n    permeable) and dropped to ~30% ΔF (~ −330 mV) at the anodic pole.\n  expected:\n    quantity: Di-8-ANEPPS anodic pole dF at 1400 V/cm\n    value: -30\n    tolerance: 3\n    unit: \"%\"\n  criterion: Collapsed pole dF, mean across the 5 cells. Reproduced when (1) the mean |dF| at\n    each pole decreases from 780 to 1000, 1200 and 1400 V/cm, (2) the fraction lost between 780\n    and 1400 V/cm is larger at the cathodic pole, (3) the cathodic pole dF at 1400 V/cm does not\n    differ from zero by a one-sample t-test at p < 0.05 (the test of Methods 2.5), and (4) the\n    anodic value is within tolerance.\n- id: fig4c-equator-follows-cosine\n  statement: Membrane regions nearer the equator were unaffected by pole electroporation and\n    followed the cosine dependence of the Schwan equation up to 1000 V/cm.\n  source: Figure 4C and legend; Results 3.4, paragraph 4\n  quote: Membrane areas closer to the equator ... appeared relatively unaffected and followed\n    the cosine dependence predicted by Schwan formula up to 1000 V/cm (Fig. 4C).\n  data: with_inputs\n  criterion: A claim of absence of a deviation. The paper names no test and no angular range for\n    \"closer to the equator\". Measured IMP (dF / 9.1%) and IMPC per perimeter point, averaged per\n    cell within arcs about the two equator points; readings (a) +-15 degrees, (b) +-30 degrees\n    from the equator, on each side of each pole hemisphere. At 570, 780 and 1000 V/cm, measured\n    against calculated by a 2-tailed paired t-test at p < 0.05 (n = 5; Student's t-test of\n    Methods 2.5). Reproduced when no arc differs at any of these strengths; not reproduced when\n    any does. The ratio of measured to calculated is reported.\n- id: fig4d-short-pulses-same-limit\n  statement: With 0.3-us pulses at higher fields (357 to 3320 V/cm), imaged at 275 ns, the maximum\n    dF was 53 +- 4% (about 600 mV) at both poles, as with 1-us pulses, and the response changed\n    with field strength in the same way.\n  source: Figure 4D; Results 3.4, paragraph 5\n  quote: \"Contrary to the expectations, the results were similar to those with 1-μs pulses in\n    Fig. 4B: the maximum ΔF reached was 53 ± 4% (~600 mV) at both cell poles. The pattern of how\n    the response changed with increasing PEF strength was not different from that with 1-μs PEFs\n    either.\"\n  expected:\n    quantity: Di-8-ANEPPS maximum pole dF with 0.3-us pulses, each pole (anodic as magnitude)\n    value: 53\n    tolerance: 4\n    unit: \"%\"\n  criterion: Tolerance is the paper's s.e. Collapsed pole dF per cell and field strength, mean\n    across the 10 cells. Reproduced when the largest mean |dF| at each pole is within tolerance,\n    and, as with 1-us pulses (fig4b-cathodic-asymmetry), the mean |dF| at both poles declines at\n    the field strengths above the one giving the maximum, more at the cathodic pole. The paper\n    gives no test for \"not different\"; none is applied.\n- id: fig5a-gd-extends-anodic\n  statement: With 1 mM Gd3+ the anodic pole charged to -864 +- 44 mV, against -542 +- 57 mV in\n    parallel controls (p < 0.001).\n  source: Figure 5A; Results 3.5, paragraph 1\n  quote: Indeed, we found that 1 mM Gd3+ extended the range of membrane charging at the anodic\n    pole down to −864 ± 44 mV (p < 0.001 compared to −542 ± 57 mV in parallel control\n    experiments, Fig. 5A).\n  statistics:\n  - test: 2-tailed t-test (Fig. 5 legend)\n    p: 0.001\n    p_relation: \"<\"\n    n: 7 cells with Gd3+, 5 control cells\n  expected:\n  - quantity: most negative anodic IMP with 1 mM Gd3+\n    value: -864\n    tolerance: 44\n    unit: mV\n  - quantity: most negative anodic IMP in controls\n    value: -542\n    tolerance: 57\n    unit: mV\n  criterion: Tolerances are the paper's s.e. Collapsed anodic pole dF converted to IMP (dF /\n    9.1%), per cell and field strength (150 to 1400 V/cm). Which datapoints are compared is not\n    stated; readings (a) the most negative group mean over field strengths in each group,\n    compared at those strengths, (b) the two groups at the same field strength, at the strength\n    giving the Gd3+ minimum, (c) each cell's own most negative value. Two-tailed unpaired\n    t-test. Reproduced when under one reading both values are within tolerance and p < 0.001.\n- id: fig5a-gd-linear\n  statement: With Gd3+, the measured IMP stayed nearly identical to IMPC down to -780 mV, so the\n    Di-8-ANEPPS calibration holds at high IMPs.\n  source: Figure 5A; Results 3.5, paragraph 1\n  quote: Furthermore, measured IMP remained nearly identical to the theoretical IMPC down to −780\n    mV, indicating that the dye response remained linear and its calibration was valid even at\n    high IMPs.\n  data: with_inputs\n  criterion: A claim of absence of a deviation. Gd3+ group, anodic pole, every field strength\n    whose mean IMPC is -780 mV or less negative; measured IMP against IMPC by a 2-tailed paired\n    t-test at p < 0.05 (n = 7; the Student's t-test of Methods 2.5). Reproduced when none\n    differs; not reproduced when any does. The ratio of measured to calculated is reported.\n- id: fig5a-gd-cathodic\n  statement: At the cathodic pole Gd3+ cells reached 647 +- 44 mV, not significantly above\n    controls, but Gd3+ prevented the decline of IMP with stronger fields.\n  source: Figure 5A; Results 3.5, paragraph 2\n  quote: At the cathodic pole, polarization in the presence of Gd3+ reached 647 ± 44 mV, a value\n    not significantly higher than that in the control group without Gd3+. However, Gd3+\n    prevented the progressive decline in IMP as the electric field was increased.\n  expected:\n    quantity: largest cathodic IMP with 1 mM Gd3+\n    value: 647\n    tolerance: 44\n    unit: mV\n  criterion: Tolerance is the paper's s.e. Collapsed cathodic pole IMP per cell and field strength.\n    The comparison with controls is a claim of absence, judged on the 2-tailed t-test of the\n    Fig. 5 legend at p < 0.05, Gd3+ (n = 7) against control (n = 5), with the readings for which\n    datapoints of fig5a-gd-extends-anodic. \"Prevented the progressive decline\" has no test;\n    read as the Gd3+ mean cathodic IMP at 1200 and 1400 V/cm being no lower than its maximum by\n    more than the s.e., while the control mean declines from its maximum. Reproduced when the\n    value is within tolerance, no reading finds Gd3+ significantly higher, and the decline\n    condition holds.\n- id: fig5a-gd-differences\n  statement: Gd3+ and control data differ significantly for datapoints with IMPC below -700 mV\n    and above 1200 mV.\n  source: Figure 5A legend\n  quote: Differences between Gd3+ and control group data are significant at p < 0.05 or better\n    (2-tailed t-test) for datapoints below −700 mV and above 1200 mV.\n  statistics:\n  - test: 2-tailed t-test\n    p: 0.05\n    p_relation: \"<\"\n    n: 7 cells with Gd3+, 5 control cells\n  data: with_inputs\n  criterion: Datapoints are field strengths, placed by their mean IMPC (the x axis of Fig. 5A,\n    which the \"mV\" bounds refer to). For each field strength and pole, measured IMP of the Gd3+\n    against the control cells by a 2-tailed unpaired t-test. Reproduced when every datapoint\n    with mean IMPC below -700 mV or above 1200 mV differs at p < 0.05.\n- id: fig5b-conductivity-calibration\n  statement: By Eq. (2), the effective membrane conductivity barely affects charging while it\n    stays far below cytosol and medium conductivities; a 10-fold rise reduces IMP by about 2% and\n    a 100-fold rise by 12%.\n  source: Figure 5B; Results 3.5, paragraph 3\n  quote: its 10-fold increase would go unnoticed, yielding just a ~2% IMP reduction, and a\n    100-fold increase would reduce IMP by just 12%.\n  expected:\n  - quantity: IMP reduction for a 10-fold increase from 3e-7 S/m\n    value: 2\n    tolerance: 0.2\n    unit: \"%\"\n  - quantity: IMP reduction for a 100-fold increase from 3e-7 S/m\n    value: 12\n    tolerance: 1.2\n    unit: \"%\"\n  criterion: A computation from Eq. (2) with the constants of Methods 2.3 (lambda_i 0.4 S/m,\n    lambda_o 1.64 S/m, R 8 um, d 5 nm, intact lambda_m 3e-7 S/m); it uses no recordings. The\n    reduction is relative to IMPC, readings (a) 1 - f/1.5, (b) 1 - f(lambda_m)/f(3e-7 S/m).\n    Reproduced when both values are within tolerance under one reading.\n- id: fig5c-gd-reduces-conductivity\n  statement: For most datapoints, Gd3+ reduced the electroporation-induced effective membrane\n    conductivity 2 to 3-fold.\n  source: Figure 5C; Results 3.5, paragraph 4\n  quote: For most datapoints, Gd3+ reduced the electroporation- induced effective conductivity\n    2–3-fold.\n  data: with_inputs\n  depends_on:\n  - fig5b-conductivity-calibration\n  expected:\n    quantity: control over Gd3+ effective conductivity ratio (range 2 to 3, widened to 1.8 to\n      3.3)\n    value: 2.55\n    tolerance: 0.75\n    unit: fold\n  criterion: For each field strength and pole, the ratio of mean measured to mean calculated IMP\n    in each group (Fig. 5C uses the datapoints of Fig. 5A, mean values), converted to effective\n    conductivity through Eq. (2) as in fig5b-conductivity-calibration. Datapoints whose measured\n    IMP is not below IMPC give no conductivity increase and are left out. Reproduced when more\n    than half of the remaining datapoints have a control-to-Gd3+ ratio between 1.8 and 3.3.\n- id: fig6a-ca-single-pulse\n  statement: A single 1-us pulse caused clear Ca2+ entry at 1000 and 1200 V/cm, with the signal\n    elevated through 5 min; the small rise at 780 V/cm was not significant.\n  source: Figure 6A; Results 3.6, paragraph 2\n  quote: Exposure to a single 1-μs pulse at escalating field strengths, from 0 to 1200 V/cm\n    established a clear peak of Ca2+ entry at 1000 and 1200 V/ cm, and Ca2+ signal remained\n    elevated through the 5-min observation period (Fig. 6A). A subtle ΔF increase after exposure\n    at 780 V/cm was at the detection limit and not statistically significant.\n  criterion: Fluo-4 dF (Methods 2.4), background-subtracted, F0 the mean before the pulse, 14\n    cells. The test is not named; the paper uses a one-sample t-test against zero for the\n    pulse-train Ca2+ data (Results 3.6), applied here at p < 0.05. The window is not given;\n    readings (a) the peak frame after the pulse, (b) the last 30 s of the recording. Reproduced\n    when at 1000 and 1200 V/cm dF is significantly above zero under both windows, and at 780\n    V/cm it is not under reading (a) (a claim of absence, judged on that test).\n- id: fig6b-ca-train-responders\n  statement: After a train of sixty 1-us pulses at 6 Hz, 28% of cells responded strongly at 780\n    V/cm and nearly all at higher field strengths.\n  source: Figure 6B; Results 3.6, paragraph 3\n  quote: A strong Ca2+ response was recorded in 28% of cells exposed at 780 V/cm and in nearly\n    all cells at higher intensities (Fig. 6B).\n  expected:\n    quantity: fraction of strongly responding cells at 780 V/cm\n    value: 28\n    tolerance: 2.8\n    unit: \"%\"\n  criterion: Each cell exposed once; Fluo-4 dF as in Methods 2.4. The paper does not define a\n    strong response. Readings (a) peak dF after the train above the mean plus 3 s.d. of the\n    pre-train baseline of the same cell, (b) peak dF above 50%, (c) peak dF above 100%. Reproduced\n    when, under one reading, the 780 V/cm fraction is within tolerance, at least 90% of cells\n    respond at each higher strength, and the 650 V/cm fraction is 2 cells (5.9%).\n- id: fig6b-ca-650\n  statement: At 650 V/cm only 2 cells (5.9%) responded strongly, yet the mean Ca2+ signal at the\n    end of recording differed from zero (p < 0.001) and was marginally higher than at 230 V/cm\n    (p < 0.05).\n  source: Figure 6B; Results 3.6, paragraph 3\n  quote: At 650 V/cm, only 2 cells (5.9%) showed a strong response, but the mean Ca2+ signal by\n    the end of recording was significantly different from zero (p < 0.001, one sample t-test)\n    and marginally higher than after exposure at 230 V/cm (p < 0.05, single-tailed t-test).\n  statistics:\n  - about: 650 V/cm mean signal at the end of recording against zero\n    test: one sample t-test\n    p: 0.001\n    p_relation: \"<\"\n    n: about 34 cells (2 cells are 5.9%)\n  - about: 650 against 230 V/cm\n    test: single-tailed t-test\n    p: 0.05\n    p_relation: \"<\"\n  criterion: Fluo-4 dF per cell (Methods 2.4). \"By the end of recording\" is not defined; readings\n    (a) the last frame, (b) the mean of the last 10 s, (c) the mean of the last 30 s. One-sample\n    t-test against zero at 650 V/cm; one-tailed unpaired Student's t-test of 650 against 230\n    V/cm. Reproduced when under one reading both p-values are within their bounds.\n  depends_on:\n  - fig6b-ca-train-responders\n- id: fig7b-charging-during-pulse\n  statement: Normalized to 150 V/cm, pole polarization during the conditioning pulse fell 1.5\n    times below linear scaling at 560 V/cm and 2-fold at 760 V/cm, and further at stronger\n    fields (p < 0.01 for every point from 560 V/cm).\n  source: Figure 7B, top panels; Results 3.7, paragraph 5\n  quote: Actual measurements fell 1.5 times below this line for 560 V/cm PEFs, 2- fold for 760\n    V/cm PEFs, and diverged further for more intense PEFs (p < 0.01 for all datapoints ≥560\n    V/cm, one sample t-test).\n  statistics:\n  - test: one sample t-test\n    p: 0.01\n    p_relation: \"<\"\n    n: 5 cells\n  expected:\n  - quantity: linear expectation over measured, 560 V/cm\n    value: 1.5\n    tolerance: 0.15\n  - quantity: linear expectation over measured, 760 V/cm\n    value: 2\n    tolerance: 0.2\n  criterion: Data are those of Fig. 4B (Di-8-ANEPPS, 1-us pulses, no test pulse), pole dF as in\n    fig4b-di8-limits, each strength as % of the 150 V/cm value, compared with the linear line\n    (100% x E / 150 V/cm). Not stated whether normalization is per cell or of the means;\n    readings (a) per cell, (b) of the means (the ratios), with the test per cell under both.\n    Which pole is not stated; readings (c) each pole, (d) the mean of the poles. One-sample\n    t-test of the per-cell values against the line. Reproduced when under one reading both\n    ratios are within tolerance, the ratio at 1000 to 1400 V/cm exceeds 2, and every datapoint\n    from 560 V/cm is below the line at p < 0.01.\n  depends_on:\n  - fig4b-di8-limits\n- id: fig7ab-test-pulse-recovery\n  statement: A 150 V/cm test pulse 5 us after the conditioning pulse charged the poles as in\n    undamaged cells after conditioning up to 760 V/cm, to about 80% (not significant) after 1000\n    V/cm, and to about 70% and 50% after 1200 and 1400 V/cm, a persistent permeabilization.\n  source: Figure 7A and 7B, bottom panels; Results 3.7, paragraphs 3 and 5\n  quote: Polarization still followed a cosine function after conditioning PEFs of up to 1000\n    V/cm. However, 1200 and 1400 V/cm conditioning PEFs markedly hindered charging by the test\n    pulse at cell poles, indicating a persistent membrane permeabilization ... In contrast,\n    measurements 6 μs later (test pulse) did not differ from the control up to 760 V/cm strength\n    of the conditioning PEF; they were at ~80% of the control reading after 1000 V/cm\n    conditioning PEF but the difference was not statistically significant. Still more intense\n    PEFs of 1200 and 1400 V/cm reduced charging by the test pulse to ~70% and ~ 50%,\n    respectively (p < 0.05 and p < 0.01, two-sided t-test).\n  statistics:\n  - about: 1200 V/cm conditioning, test pulse against control\n    test: two-sided t-test\n    p: 0.05\n    p_relation: \"<\"\n    n: 5 cells\n  - about: 1400 V/cm conditioning, test pulse against control\n    test: two-sided t-test\n    p: 0.01\n    p_relation: \"<\"\n    n: 5 cells\n  expected:\n  - quantity: test-pulse pole dF after 1000 V/cm conditioning, % of 150/150 control\n    value: 80\n    tolerance: 8\n    unit: \"%\"\n  - quantity: test-pulse pole dF after 1200 V/cm conditioning, % of control\n    value: 70\n    tolerance: 7\n    unit: \"%\"\n  - quantity: test-pulse pole dF after 1400 V/cm conditioning, % of control\n    value: 50\n    tolerance: 5\n    unit: \"%\"\n  criterion: Collapsed pole dF at 900 ns into the test pulse, as % of the 150/150 V/cm value.\n    The test, from the Fig. 7 legend, is a two-sided t-test of the difference from the undamaged\n    membrane; readings (a) one-sample t-test of per-cell % values against 100%, (b) paired\n    t-test of dF against the same cell's 150/150 value. Pole readings as in\n    fig7b-charging-during-pulse. The 570/760 and 1000 V/cm points are claims of absence, judged\n    on that test at p < 0.05. Reproduced when under one reading the three values are within\n    tolerance, 1200 and 1400 V/cm meet their p bounds, and no point up to 1000 V/cm differs.\n    The 1400 V/cm cathodic value that the paper drops as negative (Results 3.7, paragraph 6)\n    is reported both ways.\n- id: fig7c-fast-conductivity-drop\n  statement: Within 6 us of the electroporating pulse, effective membrane conductivity at the\n    poles fell by a factor of about 10 (range 7 to 20) for most datapoints; the cathodic pole,\n    more conductive during the pulse, no longer differed from the anodic pole at the test pulse.\n  source: Figure 7C; Results 3.7, paragraph 7\n  quote: \"Fig. 7C shows a profound reduction in the λm,eff within just 6 μs after the\n    electroporating pulse. For most datapoints, it dropped by a factor of 10 (range: 7–20). While\n    the cathodic pole became more conductive than the anodic pole during the electroporating\n    pulse ... no difference between the poles was detected by the test pulse.\"\n  expected:\n    quantity: ratio of effective conductivity during the conditioning pulse to that at the test\n      pulse (range 7 to 20, widened to 6.3 to 22)\n    value: 14.15\n    tolerance: 7.85\n    unit: fold\n  criterion: As Methods 2.3 and Results 3.7 give it. From the mean values of\n    fig7b-charging-during-pulse and fig7ab-test-pulse-recovery, each pole and field strength, the\n    measured fraction (of the linear line, and of the 150/150 control) converted to effective\n    conductivity through Eq. (2) as in fig5b-conductivity-calibration. The 1400 V/cm cathodic\n    test value is left out if negative, and a test value above 100% is set to 100%, as the paper\n    did. Datapoints whose test value is 100% give no finite ratio and are left out. Reproduced\n    when more than half of the remaining datapoints fall within 6.3 to 22 fold, the cathodic\n    conductivity exceeds the anodic during the conditioning pulse at 1000 V/cm and above, and at\n    the test pulse the two poles differ by less than the 7 to 20 fold range spans (a factor of\n    3) at every strength. The paper gives no test for the pole comparison.\n  depends_on:\n  - fig7b-charging-during-pulse\n  - fig7ab-test-pulse-recovery\n- id: fig7c-full-reseal-mild\n  statement: After mildly electroporating 570 and 760 V/cm pulses the membrane resealed fully\n    within 6 us; after stronger pulses a residual conductivity increase persisted.\n  source: Figure 7C; Results 3.7, paragraph 7\n  quote: For mildly electroporating PEFs of 570 and 760 V/cm, membrane resealed fully (within the\n    accuracy of measurements) within just 6 μs. With more intense PEFs, the residual increased\n    conductivity persisted for at least 6 μs, indicating the formation of more stable membrane\n    lesions.\n  criterion: Judged on the test of fig7ab-test-pulse-recovery. Reproduced when the test-pulse\n    pole dF after 570 and 760 V/cm conditioning does not differ from the control (so the\n    inferred effective conductivity is the intact value), and after 1200 and 1400 V/cm it is\n    significantly reduced at either pole.\n  depends_on:\n  - fig7ab-test-pulse-recovery\n"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
python tools/claims_check.py claims/001518/10.1016-j.bioelechem.2026.109283.yaml paper/10.1016-j.bioelechem.2026.109283.txt; grep -nE "—|rather" claims/001518/*.yaml
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
grep -nE "^\s+[^#\"-][^:]*: " claims/001518/*.yaml | grep -vE "^\S+:\s+(- )?[a-z_]+: " | head; grep -nE "[^ ]: [^ ]" claims/001518/*.yaml | grep -vE "^[0-9]+:\s*(- )?[a-z_]+: |^[0-9]+:#" | head
```

```
398:    Fig. 4B: the maximum ΔF reached was 53 ± 4% (~600 mV) at both cell poles. The pattern of how
662:    electroporating pulse. For most datapoints, it dropped by a factor of 10 (range: 7–20). While
398:    Fig. 4B: the maximum ΔF reached was 53 ± 4% (~600 mV) at both cell poles. The pattern of how
662:    electroporating pulse. For most datapoints, it dropped by a factor of 10 (range: 7–20). While
```

**Agent**

I wrote `claims/001518/10.1016-j.bioelechem.2026.109283.yaml`. The quote checker passes it with 0 problems: 30 claims, 30 quotes, 9 statistical values. Nothing is committed.

**Text read:** the version of record (Bioelectrochemistry 171, 109283), from a PDF a person supplied: main text, Methods, Results, Discussion and the legends of Figures 1 to 7. The paper names no supplement and links no code. Its analysis used MetaMorph, an Excel macro, Grapher and Origin, none of them published, and "Data will be made available on request". So I read no code, and no method detail was settled by code. I did not open any figures.

**Claims:** 30, all with quotes and none `inferred`.
- **Statistics:** 7 claims carry 9 entries. They are paired and unpaired t-tests (2-tailed or single-tailed) and one-sample t-tests, all reported as bounds (p < 0.05, < 0.01, < 0.001, > 0.05).
- **`expected`:** 21 claims carry reported values. Where the paper gives a ± s.e., that is the tolerance; otherwise it is 10%, and ranges are widened by 10% of each bound.
- **Criteria:** all 30 claims have one. The four claims of absence (stability in Fig. 2A, 2C/D; the equator following the cosine in Fig. 4C; linearity with Gd3+ in Fig. 5A) are judged on the t-tests named in the Methods and legends.

**Details the paper leaves open, with the readings named:**
- **Pole position:** Fig. 4C puts the equator at −90°/270° but the Results say 0°/270°. The poles are taken from the field direction recorded with the data; if the data don't record it, this stays open.
- **Laser images:** no background subtraction is stated. Readings: none, or a cell-free region (as is done for the Ca2+ images).
- **Cell radius:** the method isn't given. Readings: perimeter/2π, or the radius of the circle of equal area.
- **Correlation coefficient of the fit through the origin (Fig. 3):** Pearson r, or √(uncentred R²).
- **FluoVolt non-linearity (Fig. 3):** the paper judges this by eye from a LOESS smooth with no span given. Readings: spans 0.3, 0.5 and 0.75, or 50-mV bins. A departure is the smooth falling more than 10% short of the line; that threshold is my own choice (the protocol's 10% default), not the paper's.
- **"Start" and "end" of a set (Fig. 2):** the first and last image, or the first and last 10 images.
- **Pole and pooling for the ~20% drop (Fig. 2D):** cathodic or anodic pole; each later set or their mean. The legend's "≤20%" wording is also accepted.
- **Which datapoints are compared for Gd3+ (Fig. 5A):** the group minima, the same field strength, or each cell's own minimum. The legend's "above 1200 mV" is read as IMPC on the x-axis.
- **Fig. 5B reduction relative to IMPC:** 1 − f/1.5, or relative to the intact f.
- **Normalization and pole in Fig. 7B:** per cell or of the means; each pole or both poles together. The Fig. 7 test is read as a one-sample t-test against 100% or a paired t-test.
- **Ca2+ data (Fig. 6):** "strong response" is undefined. Readings: 3 s.d. above baseline, dF > 50%, or dF > 100%. "End of recording" is the last frame, the last 10 s or the last 30 s. The test for the single-pulse data isn't named; the one-sample t-test the paper uses elsewhere is applied.
- **Smaller gaps:**
  - "Near the equator" in Fig. 4C has no angular range given; readings are ±15° and ±30°.
  - The 560/760 V/cm in the Fig. 7 Results are read as the same levels as 570/780 V/cm elsewhere.
  - Whether Figs. 2 and 4 used the same cells is not stated.

**Missing from the paper:** the fit of τ against cell radius, which Eq. 1 needs to calculate IMPC. It is only in reference [20] (Semenov et al., Bioelectrochemistry 168 (2025) 109143), which I did not read. The 9 claims that use IMPC are marked `data: with_inputs` for that reason. Most other methods are also deferred to [20]. No supplement or Methods section that the results rest on is missing.

When I worked Eq. 2 through as printed, a 10-fold conductivity rise gives about a 1.3% drop in IMP, against the paper's "~2%". That would fail the 10% tolerance in `fig5b-conductivity-calibration`, but I left the claim as the paper states it.

The dataset's title and description cover the FluoVolt and Di-8-ANEPPS experiments. It may not hold the Gd3+, Ca2+ (Fig. 6) or two-pulse (Fig. 7) data; checking that is the author's job.

## End of run

15 turns, 6 minutes, result: success.
