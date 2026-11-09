# 001047 · claims · run 39849456014

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cat docs/protocol.md; ls claims/001453/ claims/ paper/ | head -50; ls claims/001047 2>/dev/null
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -n '/^### 3. Write the claims file/,/^## Author/p' docs/protocol.md; ls claims/001453/ paper/
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cat claims/001453/*.yaml | head -150; wc -c paper/*.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cat paper/*.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/a9cafdc2-320e-49ff-885a-0ced17b0db81/tool-results/bdktmelz0.txt"
}
```

```
1	DOI: 10.1016/j.bioelechem.2025.109016
2	Version: as served by ncbi_pmc
3	Source: ncbi_pmc+crossref (paper-text-fetcher)
4	Stored: 2026-10-20
5	Extracted: as fetched
6	------------------------------------------------------------------------
7	pmc Bioelectrochemistry Bioelectrochemistry 319 nihpa 100953583 Bioelectrochemistry (Amsterdam, Netherlands) 1567-5394 1878-562X pmc-is-collection-domain yes pmc-collection-title NIHPA Author Manuscripts PMC12331426 PMC12331426.1 12331426 12331426 NIHMS2087238 40460713 10.1016/j.bioelechem.2025.109016 NIHMS2087238 NIHPA2087238 1 Article MHz compression of pulse packets facilitates remote focusing of electroporation Silkuniene Giedre Silkunas Mantas Pakhomova Olga N. Semenov Iurii Pakhomov Andrei G. * Frank Reidy Research Center for Bioelectrics, Old Dominion University, Norfolk, VA 23508, USA Author contributions A.G.P.: Conceptualization, Methodology, Formal Analysis, Writing - Original Draft, Supervision, Visualization, Funding acquisition G.S.: Methodology, Formal Analysis, Visualization, Data Curation, Software, Validation, Investigation, Writing Original Draft M.S.: Methodology, Formal Analysis, Writing - Original Draft, Visualization, Investigation I.S.: Methodology, Formal Analysis, Writing-Review and Editing O.N.P .: Methodology, Writing-Review and Editing, Resources. * Corresponding author: Andrei G. Pakhomov, Frank Reidy Research Center for Bioelectrics Old Dominion University, 4211 Monarch Way., Suite 300, Norfolk, VA 23508, Fax: +1(757)4511010, [removed: an e-mail address] ; [removed: an e-mail address] , 12 2025 31 5 2025 166 494632 109016 109016 04 06 2025 31 05 2026 31 05 2026 09 08 2025 31 05 2026 This file is available for text mining. It may also be used consistent with the principles of fair use under the copyright law. Stimulation by pulsed electric fields (PEFs) normally follows PEF strength and weakens with distance from electrodes. Bipolar cancellation, caused by the electric field reversal, can offset this dependence. Remo
[... 21 more lines not kept]
```

**Agent**

The full text is there (author manuscript from PMC, no supplement listed). Checking the rest of the file, the dataset's description, and the schema.

**Agent calls Bash**

```bash
sed -n '29,109p' paper/*.txt | cut -c1-200 | grep -v '^\[' | grep -v '^$' | head; grep -rl "001047" --include=*.yaml --include=*.md --include=*.json . 2>/dev/null | head; ls docs tools schemas 2>/dev/null
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
python -c "
import json;d=json.load(open('targets/dandisets.json'))
items=d if isinstance(d,list) else d.get('dandisets',d)
for x in (items if isinstance(items,list) else items.values()):
  if '001047' in json.dumps(x): print(json.dumps(x,indent=1)[:3000])
"; grep -n -B2 -A10 "001047" papers/manifest.yaml; cat schemas/claims.schema.json | head -200
```

```
[
 {
  "dandiset": "000003",
  "name": "Physiological Properties and Behavioral Correlates of Hippocampal Granule Cells and Mossy Cells",
  "published_version": "0.260218.2052",
  "asset_count": 101,
  "size_gb": 2559.25,
  "data_standards": [
   "Neurodata Without Borders (NWB)"
  ],
  "species": [
   "House mouse"
  ],
  "approaches": [
   "electrophysiological approach",
   "behavioral approach"
  ],
  "papers": [
   {
    "doi": "10.1016/j.neuron.2016.12.011",
[... 312 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n '200,400p' schemas/claims.schema.json; python -c "
import json;d=json.load(open('targets/dandisets.json'))
for x in d:
  if x.get('dandiset')=='001047': print(json.dumps(x,indent=1))
"
```

```
Exit code 1
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
[... 133 more lines not kept]
```

**Agent calls Bash**

```bash
python -c "
import json;d=json.load(open('targets/dandisets.json'))
print(type(d), list(d)[:5] if isinstance(d,dict) else '')
s=json.dumps(d); i=s.find('\"001047\"'); print(s[i-50:i+2500])
"
```

```
<class 'dict'> ['schema_version', 'generated', 'source', 'counts', 'targets']
int": false}], "catalystneuro": []}, {"dandiset": "001047", "name": "Optimizing NG-CanCan Protocol Delivery with MHz Compression to Minimize Near-Electrode Ablation", "published_version": "0.250701.1609", "asset_count": 88, "size_gb": 17.25, "data_standards": ["Neurodata Without Borders (NWB)"], "species": ["Mus musculus - House mouse", "Cricetulus griseus - Cricetulus aureus"], "approaches": [], "papers": [{"doi": "10.1016/j.bioelechem.2025.109016", "title": "MHz compression of pulse packets facilitates remote focusing of electroporation", "relation": "IsPublishedIn", "resource_type": "JournalArticle", "preprint": false}], "catalystneuro": []}, {"dandiset": "001048", "name": "Plasma membrane conductance changes in response to supraphysiological hyperpolarization", "published_version": "0.250701.1624", "asset_count": 7, "size_gb": 4.79, "data_standards": ["Neurodata Without Borders (NWB)"], "species": ["Homo sapiens - Human"], "approaches": [], "papers": [{"doi": "10.1016/j.xcrp.2025.102660", "title": "Excitation and polarization of isolated neurons by high-frequency sine waves for temporal interference stimulation", "relation": "IsPublishedIn", "resource_type": "JournalArticle", "preprint": false}], "catalystneuro": []}, {"dandiset": "001051", "name": "Large-scale Neuropixels recordings through SHIELD implant during visual change detection task with dynamic gating of engagement", "published_version": "0.260922.1827", "asset_count": 666, "size_gb": 1808.07, "data_standards": ["Neurodata Without Borders (NWB)"], "species": ["Mus musculus - House mouse"], "approaches": ["electrophysiological approach"], "papers": [{"doi": "10.1016/j.neuron.2024.06.015", "title": "SHIELD: Skull-shaped hemispheric implants enabling large-scale electrophysiology datasets in the mouse brain", "relation": "IsDescribedBy", "resource_type": "JournalArticle", "preprint": false}], "catalystneuro": []}, {"dandiset": "
[... 1 more lines not kept]
```

**Agent calls Bash**

```bash
ls claims/001048; head -60 claims/001048/*.yaml; sed -n '1,60p' tools/claims_check.py
```

```
10.1016-j.xcrp.2025.102660.yaml
# Claims for Semenov, Kim, Silkuniene & Pakhomov (2025), Cell Reports Physical Science 6, 102660,
# on dandiset 001048.
# Written by an agent (model "claude-opus-5-5", Claude Code in GitHub Actions), 2026-10-22, under
# docs/protocol.md version pilot-10, as the reader.
#
# Text read. The NIH author manuscript (NIHMS2098259, PMC12320893) as served by Europe PMC: main
# text, figure legends and STAR Methods, with the supplement (NIHMS2098259-supplement-1.pdf, Figures
# S1 to S4 and Table S1, the Key Resource Table), all in paper/10.1016-j.xcrp.2025.102660.txt. The
# version of record was not read. There is no PDF of the main text, so Figures 1 to 6 were not seen;
# no claim needed a figure the text does not describe.
#
# Code. The paper states "This paper does not report original code". It names the software used:
# Fiji ImageJ 1.53C or MetaMorph 7.7 for soma emission, Grapher 16 for traces and linear regression,
# Origin 8.0 for exponential fits and their standard errors, Sim4Life 5.2 for the field, and RStudio
# in Table S1. No repository was read, so no method detail below is settled by code.
#
# This dandiset does not hold the paper's data. Its title and description on DANDI (version
# 0.250701.1624) are "Plasma membrane conductance changes in response to supraphysiological
# hyperpolarization", a study of membrane lesions made by hyperpolarization in HEK cells ("diffuse
[... 101 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n '60,140p' claims/001048/*.yaml
```

```
# (F6) The test, where the paper names none, is a two-sided Student's t test, paired or unpaired as
# appropriate, at p < 0.05 (Methods, Quantification and statistical analysis); error bars are SEM.
# (F7) Strobe data (Methods, Pulsed laser fluorescence microscopy). F per frame in the de- and
# hyperpolarized ROIs, scaled to a debris ROI; F0 the mean before the pulse, or for sine waves the
# mean over the first and last cycles; charging fit dF = dFmax (1 - exp(-t/tau)) over time into the
# pulse, discharging fit dF = dFmax exp(-t/tau) over time after it. The pulse sensitivity is dF
# averaged from 1 to 2 us into the pulse, normalized to 1 kV/cm (Results; Figure 6B legend); the sine
# sensitivity is the regression coefficient of the oscillation, after subtraction of a LOESS fit of
# the whole-cell response, on the field (Results; Figure 6C legend).
#
# Details the paper leaves open, with the readings named. Each criterion that uses one runs every
# reading; a claim is decided when all readings give its outcome, and blocked as
# methods_underspecified when they give different outcomes.
# (O1) The soma outline is not given. ROIs are taken from the dataset when it holds them; otherwise
# readings (a) the connected component nearest the image centre (the Methods centre the neuron) of
# an Otsu threshold of the mean pre-stimulus frame, (b) that mask eroded by 2 pixels. Otsu and the 2
# pixels are standard choices.
# (O2) The F0 interval is "a time interval preceding the electrical stimulation"; readings (a) all
# frames before the onset, (b) the last 20 ms before it.
# (O3) AP detection is given only as "brief emission upticks", in neurons selected for APs above 5%
[... 61 more lines not kept]
```

**Agent calls Write**

```json
{
 "file_path": "claims/001047/10.1016-j.bioelechem.2025.109016.yaml",
 "content": "# Claims for Silkuniene, Silkunas, Pakhomova, Semenov & Pakhomov (2025), Bioelectrochemistry 166,\n# 109016, on dandiset 001047.\n# Written by an agent (model \"claude-opus-5-5\", Claude Code in GitHub Actions), 2026-10-22, under\n# docs/protocol.md version pilot-10, as the reader.\n#\n# Text read. The NIH author manuscript (NIHMS2087238, PMC12331426) as served by PMC: abstract, main\n# text, Materials and methods, Results, Discussion and figure legends (Figures 1 to 7), in\n# paper/10.1016-j.bioelechem.2025.109016.txt. PMC lists no supplement and the text cites none. The\n# version of record was not read. There is no PDF, so Figures 1 to 7 were not seen; values shown only\n# in a figure (the packet rates tested, the burst numbers, the measured distances, per-group means)\n# are not known here and no claim rests on reading them from a figure.\n#\n# Code. The paper links no code; its Data availability says \"Data will be made available on\n# request\". It names the software: MetaMorph 7.8.13 for intensities, RStudio, Excel and Grapher 16\n# for processing, fits and plots, Sim4Life Lite 7.0.1.8169 for the field. No repository was read, so\n# no method detail below is settled by code.\n#\n# The dandiset. Its title on DANDI (version 0.250701.1609) is \"Optimizing NG-CanCan Protocol Delivery\n# with MHz Compression to Minimize Near-Electrode Ablation\", species house mouse and Chinese hamster,\n# and it names this paper (IsPublishedIn). It is taken to hold the monolayer images of this paper (CT26\n# are mouse cells, CHO hamster cells). Whether it holds the thermometry images (Figure 2) is the\n# author's to find.\n#\n# Data the paper used. CT26 mouse colon carcinoma and CHO-K1 cell monolayers in 6-well plates. Four\n# hollow 2.8-mm needle electrodes in a square with 15.3-mm diagonals, touching the monolayer or raised\n# 1 or 2 mm above it. Packets of 16 pulses (Figure 1B), first pulse 7.2 kV, later pairs 12.5% lower\n# per phase; 9 packets per burst, bursts at 1 Hz, applied from 4 directions (\"2 bursts (x4)\" is 8\n# bursts). Controls deliver only the first pulse of each packet. Measured variables are stitched\n# whole-well images taken with a 4x objective: Hoechst 33342 (DAPI cube) before exposure, YO-PRO-1\n# (YP, FITC cube) 30 min after exposure, and for killing experiments propidium (Pr, Cy3 cube) 2 h\n# after, with Hoechst re-imaged. Experiment sets: (S1) CT26, 600-ns pulses, 2 bursts (x4), packet\n# rate 1 Hz to 0.208333 MHz (packets with no interval; \"0.2 MHz\") and control, n = 3 per CANCAN rate\n# and n = 5 controls (Figures 3, 4), with one subset also measured parallel to the array sides\n# (Figure 3C); (S2) CT26, 0.2 MHz, 2 bursts (x4), electrodes at 0, 1 or 2 mm, YP n = 6 to 7 and Pr n\n# = 4 to 5 (Figure 5); (S3) CT26, packets of 300-, 600- or 900-ns pulses with no interval, 18, 9 or\n# 6 packets per 43.2-us burst, 2 bursts (x4), n = 5 each (Figure 6); (S4) CT26 (n = 3 to 5) and CHO\n# (n = 4), 0.2 MHz, several burst numbers up to 6 bursts (x4) (Figure 7); (S5) thermochromic film\n# images after 2 and 6 bursts at 0.2 MHz without rotation (Figure 2). The text names the rates 1 Hz,\n# 1 kHz, 10 kHz and 0.2 MHz; the log fit over 1 Hz to 10 kHz has n = 15 at n = 3 per rate, so five\n# rates were tested up to 10 kHz, plus 0.2 MHz.\n#\n# Method details fixed from the paper, used by the criteria.\n# (F1) Intensity is the mean YP (or Pr) emission in 325 x 406 um ROIs placed along the diagonals of\n# the square, joining the electrode footprints, at distances x (mm) from the array centre; in the\n# Figure 3C subset, also along lines through the centre parallel to the sides (Methods 2.5).\n# (F2) Background is the mean of 3 ROIs inside one electrode footprint, subtracted from every ROI\n# (Methods 2.5).\n# (F3) The two diagonals of a well are pooled as one experiment; n counts wells (Methods 2.5; Figure\n# 3B legend). Data are mean +/- s.e. over experiments (Methods 2.5).\n# (F4) YP profiles are fitted with YP(x) = a (b/2)^2 / (x^2 + (b/2)^2), a the peak at x = 0 and b\n# the FWHM (Methods 2.5). Pr profiles are fitted with Pr(x) = a exp(-x^2 / (2 sigma^2)), FWHM about\n# 2.4 sigma (Methods 2.5). Fits are least squares (Grapher), a standard reading of \"fitted\".\n# (F5) FWHM per condition is the mean of FWHM values from Lorentzian fits of each experiment (Results\n# 3.1; Figure 4C and 6D legends).\n# (F6) Fitted ranges: -4 to 4 mm for Figures 3 and 4 (Results 3.1; Figure 3B legend), -5 to 5 mm\n# for Figure 5 (Results 3.2; Figure 5B legend) and the mean profiles of Figure 6 (Figure 6B legend).\n# (F7) Tests are two-sided Student's t tests, with Bonferroni correction where several groups are\n# compared, at p < 0.05 (Methods 2.5). A trend's slope is tested with a two-sided one-sample t test\n# of the regression slope (Figure 4C, 6D, 7 legends).\n# (F8) The paper's own reading of its plots: \"A gap exceeding the length of the error bars indicates\n# a significant difference at p<0.05\" (Methods 2.5). Claims the paper states without a test are\n# judged by this rule on mean +/- s.e., as the paper asks its reader to judge them.\n# (F9) Fields from the paper's simulation, not from the data: a 7.2-kV first pulse gives 3.3 kV/cm at\n# the centre, 9.4 kV/cm at 6 mm and 13.5 kV/cm at 7 mm toward the active electrode (Methods 2.2).\n# (F10) Percent of the diagonal: FWHM / 15.3 mm x 100 (Figure 4C legend, right axis; 1.7 mm is given\n# as 11.1%).\n#\n# Details the paper leaves open, with the readings named. Each criterion that uses one runs every\n# reading; a claim is decided when all readings give its outcome, and blocked as\n# methods_underspecified when they give different outcomes.\n# (O1) ROI positions along a diagonal are not given. Positions are taken from the dataset when it\n# holds them; otherwise readings (a) ROIs centred at whole-mm distances (0, 1, ... 7 mm each way; the\n# text names only whole-mm distances: 0, 6, 7 mm and fit limits 4, 5, 6 mm), (b) contiguous ROIs\n# from the centre outward. Which ROI side lies along the diagonal is not given; 406 um along the\n# diagonal is used as a standard choice that cannot move a centre by more than 0.04 mm.\n# (O2) \"Pooled\" diagonals. Readings (a) the two diagonals averaged at each signed position (profiles\n# run from -x to x, as plotted in Figures 3B, 5B, 6B), (b) all four half-diagonals averaged at each\n# distance (Figure 4A legend, \"measurements in 4 diagonal directions from the center were pooled\").\n# Fits under (b) use the folded profile mirrored to -x.\n# (O3) The fitted range for per-experiment FWHM. Methods say \"limited to 4-6 mm\"; Figures 3 and 4\n# use 4 mm, Figure 5 and 6B use 5 mm, Figure 6D refers to the method of 3.1 (4 mm), Figure 7 gives\n# none. Readings for Figure 6D, (a) -4 to 4 mm, (b) -5 to 5 mm; for Figure 7, (a) 4, (b) 5, (c) 6 mm.\n# (O4) Regressions over experiments or means. The Figure 4C fit uses n = 15 individual experiments;\n# for Figures 6D and 7 readings are (a) per-experiment values, (b) group means.\n# (O5) The near-electrode distance of the 40-fold ratio. Readings (a) 6 mm, (b) 7 mm (both are \"near\n# electrodes\" in Results 3.1 and Figure 4B).\n#\n# Data. Every claim uses the paper's own recordings (data dataset). The field values of F9 come from\n# the paper's simulation and are taken from the text; no claim tests them.\nschema_version: 2\ndataset:\n  archive: dandi\n  id: \"001047\"\npaper: doi:10.1016/j.bioelechem.2025.109016\nclaims:\n- id: fig2-heating\n  statement: With packets at the maximum rate, heating followed the field and was largest near the\n    electrodes; after 2 bursts it was confined to about 2 mm next to the electrodes and could exceed\n    30 C but not 44 C; after 6 bursts it spread further, exceeding 30 C even near the centre, yet\n    never exceeded 44 C.\n  source: Methods 2.3, paragraph 1; Figure 2\n  quote: With 2 bursts ( Fig. 2A ), heating was restricted to an approximately 2-mm zone next to\n    electrodes, where it could reach over 30 °C but did not exceed 44 °C. With 6 bursts ( Fig. 2B ),\n    heating was more widespread ... Temperature could exceed 30 °C even near the center of the\n    array, but did not exceed 44 °C even near the electrodes.\n  criterion: Film images at the end of the 2nd and 6th burst (Methods 2.3). Temperature classes from\n    the calibrated colour transitions, black to red, green, blue and back to black at 25, 26, 30 and\n    44 C (Methods 2.3). The hue limits of the colours are not given; readings (a) red below 45,\n    green 75 to 165, blue 180 to 270 degrees of hue, (b) red below 30, green 90 to 150, blue 195 to\n    255 degrees, with black any pixel of value below 0.2 (standard choices). Above 30 C is blue;\n    above 44 C is black after blue, that is a dark pixel inside a blue region. Reproduced when, under\n    every reading, the 2-burst image has blue pixels only within 2.5 mm of an electrode edge\n    (\"approximately 2-mm\"), the 6-burst image has blue pixels within 2 mm of the centre, and neither\n    image has a dark pixel enclosed by blue outside the electrode footprints. Blocked when the dataset\n    holds no film images.\n- id: fig3a-centre-enhanced\n  statement: Every CANCAN protocol enhanced electroporation at the array centre, while in the control\n    (single unipolar pulse per packet) YP uptake decreased gradually toward the centre.\n  source: Results 3.1, paragraph 2; Figure 3A\n  quote: All CANCAN protocols visibly enhanced electroporation at the center of the array, in\n    contrast to its gradual decrease toward the center in the control ( Fig. 3A ).\n  criterion: Set S1, F1 to F3, O1, O2. For each CANCAN rate, the mean diagonal profile has its\n    maximum at x = 0 (reading (b) of O1 allows the ROI nearest 0); for the control, the mean at x = 0\n    is below the means at 6 and 7 mm by a gap larger than the error bars (F8). Reproduced when both\n    hold for every rate under every reading.\n- id: fig3bc-rate-suppresses-off-target\n  statement: Raising the packet rate from 1 Hz to 0.2 MHz suppressed electroporation better both near\n    the electrodes (diagonal profile) and at the perimeter between electrodes (profile parallel to\n    the sides).\n  source: Results 3.1, paragraph 2; Figure 3B, 3C\n  quote: The most conspicuous effect of increasing the packet rate from 1 Hz to 0.208333 MHz\n    (abbreviated to 0.2 MHz below and in figure legends) was better suppression of electroporation\n    both near electrodes ( Fig. 3B ) and at the perimeter between electrodes ( Fig. 3C ).\n  criterion: Set S1, F1 to F3, F8, O1, O2. Near electrodes is YP at 6 and 7 mm on the diagonals. The\n    perimeter is not given as a distance; readings (a) the outermost ROIs of the parallel profile,\n    (b) the mean of the parallel ROIs at 4 mm or more from the centre. Reproduced when, under every\n    reading, mean YP at 0.2 MHz is below that at 1 Hz with a gap larger than the error bars (F8) at\n    6 mm, at 7 mm and at the perimeter; a two-sided t test at each is reported. Blocked for the\n    perimeter part when the dataset has no parallel measurements.\n- id: fig3-lorentzian-profile\n  statement: The decline of YP emission from the centre was bell-shaped and fitted a Lorentzian\n    function over -4 to 4 mm nearly perfectly (R > 0.9, p < 0.001) for every packet rate.\n  source: Results 3.1, paragraph 3; Figure 3B, 3C legend; Methods 2.5\n  quote: The fit correlation with data in the −4 to 4 mm radius was nearly perfect (R>0.9, p<0.001).\n  statistics:\n  - about: correlation of the Lorentzian fit with the data, -4 to 4 mm\n    statistic: R > 0.9\n    p: 0.001\n    p_relation: \"<\"\n  - about: significance of each YP fit in Figures 3, 5 and 6\n    p: 0.0001\n    p_relation: \"<\"\n  expected:\n    quantity: Pearson correlation of fitted and measured mean YP, -4 to 4 mm, each rate\n    value: 0.9\n    tolerance: 0\n  criterion: Set S1, F1 to F4, F6, O1, O2. For each CANCAN rate, the Lorentzian (F4) is fitted to the\n    mean diagonal profile over -4 to 4 mm and to the parallel profile where present. R is the Pearson\n    correlation of fitted and measured values over that range, and p its test. Reproduced when R\n    exceeds 0.9 with p < 0.001 for every rate and profile under every reading; the threshold 0.9 is\n    the paper's bound, so the tolerance is zero.\n- id: fig3-tail-deviation-falls-with-rate\n  statement: Beyond the fitted range, the data deviated from the Lorentzian fit less as the packet\n    rate increased.\n  source: Results 3.1, paragraph 3; Figure 3B, 3C\n  quote: The deviation of experimental data from the fits at larger distances from the center\n    diminished with increasing the packet repetition rate, highlighting better suppression of the\n    off-target electroporation.\n  depends_on:\n  - fig3-lorentzian-profile\n  criterion: Set S1, fits of fig3-lorentzian-profile extended to all distances (Figure 3B legend, the\n    plots were extended to the x-axis limits). The deviation is the mean of (data - fit) over ROIs\n    beyond 4 mm. The paper does not say in which units; readings (a) a.u., (b) percent of the fitted\n    peak a. Reproduced when, under every reading, the deviation is largest at 1 Hz and smallest at\n    0.2 MHz, and its Spearman correlation with rate over the tested rates is negative (a standard\n    measure of a monotone trend, as the paper names none).\n- id: fig4b-centre-no-rate-effect\n  statement: YP uptake at the array centre showed no significant effect of packet rate.\n  source: Results 3.1, paragraph 4; Figure 4B\n  quote: YP intensity in the center showed no significant effect of the packet rate ( t -test with\n    Bonferroni correction, Fig. 4B ).\n  criterion: A claim of absence, judged on the paper's test. Set S1, F1 to F3, O2; per experiment the\n    background-subtracted YP at x = 0. Two-sided Student's t tests with Bonferroni correction (F7).\n    The set of comparisons is not given; readings (a) each rate against 1 Hz (as in Figure 4C), (b)\n    all pairs of rates. Reproduced when no corrected comparison has p < 0.05; not reproduced when\n    any does. Group means and the largest ratio between rates are reported either way.\n- id: fig4b-near-electrode-decline\n  statement: In contrast to the centre, YP uptake at 6 and 7 mm from the centre (1.65 and 0.65 mm from\n    the electrodes) declined steeply as the packet rate increased.\n  source: Results 3.1, paragraph 4; Figure 4B\n  quote: It contrasted with a steep, packet rate-dependent decline of YP uptake at 6 and 7 mm from\n    the center (i.e., 1.65 and 0.65 mm from electrodes).\n  criterion: Set S1, F1 to F3, O2. At 6 mm and at 7 mm, a power function YP = c rate^k is fitted to\n    YP against packet rate (Figure 4B legend, best fits using power function), by least squares on\n    the group means (the legend fits the plotted means). Reproduced when k < 0 at both distances and\n    mean YP at 0.2 MHz is below that at 1 Hz with a gap larger than the error bars (F8) at both;\n    the fit to per-experiment values is shown as a variant.\n- id: fig4b-40-fold-ratio\n  statement: At 0.2 MHz, YP uptake at the centre was 40 times that near the electrodes, despite the\n    field there being about 4 times weaker (3.3 against about 14 kV/cm).\n  source: Results 3.1, paragraph 3 (sic, the paragraph on the ratio); Figure 4B; Abstract\n  quote: Now, by increasing the packet repetition rate to 0.2 MHz, we achieved a 40-fold difference (\n    Fig. 4B ), despite using a bigger array with larger reduction of the electric field from\n    electrodes to the center.\n  expected:\n    quantity: ratio of mean YP at the centre to mean YP near electrodes, 0.2 MHz\n    value: 40\n    tolerance: 4\n  criterion: Set S1 at 0.2 MHz, F1 to F3, F9, O2, O5. The ratio of group-mean background-subtracted\n    YP at x = 0 to that at the near-electrode distance. Reproduced when the ratio is within 36 to 44\n    under one reading of O5 and O2 (the paper names one number for a choice it leaves open).\n- id: fig4c-fwhm-falls-with-rate\n  statement: Higher packet rates focused electroporation into a smaller spot; the FWHM fell from\n    about 4 mm at 1 Hz to about 2 mm at 1 kHz, 10 kHz and 0.2 MHz (p = 0.03, 0.02 and 0.09 against 1\n    Hz), and could be under 15% of the inter-electrode gap.\n  source: Results 3.1, paragraphs 5 and 6; Figure 4C\n  quote: FWHM decreased from ~4 mm at 1 Hz to ~2 mm at 1 kHz, 10 kHz, and 0.2 MHz packet rates (p =\n    0.03; 0.02, and 0.09, respectively; t -test with Bonferroni correction).\n  statistics:\n  - about: 1 kHz against 1 Hz\n    test: t-test\n    p: 0.03\n    corrected: Bonferroni\n    n: 3 experiments per rate\n  - about: 10 kHz against 1 Hz\n    test: t-test\n    p: 0.02\n    corrected: Bonferroni\n    n: 3 experiments per rate\n  - about: 0.2 MHz against 1 Hz\n    test: t-test\n    p: 0.09\n    corrected: Bonferroni\n    n: 3 experiments per rate\n  expected:\n  - quantity: mean FWHM at 1 Hz\n    value: 4\n    tolerance: 0.4\n    unit: mm\n  - quantity: mean FWHM at 1 kHz\n    value: 2\n    tolerance: 0.2\n    unit: mm\n  - quantity: mean FWHM at 10 kHz\n    value: 2\n    tolerance: 0.2\n    unit: mm\n  - quantity: mean FWHM at 0.2 MHz\n    value: 2\n    tolerance: 0.2\n    unit: mm\n  criterion: Set S1, F1 to F7, F10, O1, O2. Per experiment, the Lorentzian fitted over -4 to 4 mm\n    gives b; FWHM per rate is the mean over experiments. Two-sided t tests of each rate against 1\n    Hz, Bonferroni over the rates compared with 1 Hz. Reproduced when the four means are within\n    tolerance, 1 kHz and 10 kHz differ from 1 Hz at corrected p < 0.05 (the legend marks them with\n    *p<0.05), and at least one rate has mean FWHM below 15% of 15.3 mm (2.3 mm). Partially\n    reproduced when the tests hold but a mean is outside tolerance. The 0.2 MHz comparison (p =\n    0.09) is reported, not required.\n- id: fig4c-log-trend\n  statement: FWHM fell logarithmically with packet rate from 1 Hz to 10 kHz (R = 0.77, p < 0.001; n\n    = 15), with no further narrowing from 10 kHz to 0.2 MHz.\n  source: Results 3.1, paragraph 5; Figure 4C legend\n  quote: FWHM decrease followed the logarithmic dependence from 1 Hz to 10 kHz (correlation\n    coefficient R = 0.77, p<0.001), but there was no further focality increase when the packet rate\n    increased from 10 kHz to 0.2 MHz.\n  statistics:\n  - about: log fit of FWHM against packet rate, 1 Hz to 10 kHz\n    statistic: R = 0.77\n    p: 0.001\n    p_relation: \"<\"\n    n: 15 experiments (0.2 MHz excluded)\n  - about: slope of the log fit\n    test: 2-sided, one-sample t test\n    p: 0.0001\n    p_relation: \"<\"\n    n: 15 experiments\n  expected:\n    quantity: correlation coefficient of FWHM with log packet rate, 1 Hz to 10 kHz\n    value: 0.77\n    tolerance: 0.077\n  depends_on:\n  - fig4c-fwhm-falls-with-rate\n  criterion: Per-experiment FWHM from fig4c-fwhm-falls-with-rate, rates 1 Hz to 10 kHz, 0.2 MHz left\n    out (Figure 4C legend). FWHM = m log(rate) + c by least squares; R is the absolute Pearson\n    correlation of FWHM with log rate; the slope is tested by a two-sided t test. Reproduced when R\n    is within tolerance, the slope is negative with p < 0.001, and mean FWHM at 0.2 MHz is not below\n    that at 10 kHz by a gap larger than the error bars (F8). Partially reproduced when the slope is\n    negative with p < 0.05 but R or p falls short.\n- id: fig5-raised-electrodes-weaken-centre\n  statement: With MHz-CANCAN there was practically no YP staining near electrodes, and raising the\n    electrodes 1 or 2 mm above the monolayer weakened electroporation in the central spot.\n  source: Results 3.2, paragraph 1; Figure 5A, 5B\n  quote: With MHz-CANCAN (CT26 cells, 2 bursts (x4), Fig. 4 ), there was practically no YP staining\n    near electrodes to start with, so the only clear effect of raising electrodes was the weakening\n    of electroporation in the central spot.\n  criterion: Set S2, F1 to F3, F8, O2. YP in percent of the mean 0-mm peak (Figure 5B legend). The\n    centre is x = 0. Reproduced when mean centre YP at 1 mm and at 2 mm elevation are each below 0 mm\n    with a gap larger than the error bars (F8), and at 0 mm mean YP at 7 mm is under 10% of the centre\n    (practically none; the 40-fold ratio of fig4b-40-fold-ratio is 2.5%). Two-sided t tests are\n    reported.\n- id: fig5ab-yp-spot-slightly-larger-than-pr\n  statement: The central spot of YP staining (electroporation) was only slightly larger than the spot\n    of Pr staining (cell killing).\n  source: Results 3.2, paragraph 1; Figure 5A, 5B\n  quote: Somewhat unexpectedly, the central spot of YP staining (electroporation) was just slightly\n    larger than the spot of Pr staining (cell killing; Fig 5A and B ).\n  criterion: Set S2, each elevation, F1 to F4, F6, O2. FWHM of the Lorentzian fit to mean YP and of\n    the Gaussian fit to mean Pr over -5 to 5 mm (Figure 5B legend); the Gaussian FWHM is 2.4 sigma as\n    the Methods give it, and 2.355 sigma as a variant. The paper bounds \"slightly\" by no number;\n    readings (a) YP FWHM / Pr FWHM between 1 and 1.25, (b) between 1 and 1.5. Reproduced when the\n    ratio falls in the range under every reading at 0 mm elevation (the panel the text cites first);\n    other elevations are reported.\n- id: fig5b-gaussian-pr-lorentzian-yp\n  statement: Pr intensity declined from the peak as a Gaussian and YP as a Lorentzian; for the 0-mm\n    data the R2 was 0.92 (Lorentzian) against 0.96 (Gaussian) for Pr, and 0.98 against 0.95 for YP,\n    fitted from -5 to 5 mm with p < 0.0001.\n  source: Results 3.2, paragraph 2; Figure 5B\n  quote: For Pr data in the left panel of Fig. 5B , the coefficient of determination increased from\n    0.92 for Lorentzian fit to 0.96 for Gaussian fit. YP data showed the opposite trend, with the\n    coefficients of 0.98 and 0.95 for Lorentzian and Gaussian fits, respectively (for all these\n    fits, the fitted region was from −5 to 5 mm, p<0.0001).\n  statistics:\n  - about: each of the four fits\n    p: 0.0001\n    p_relation: \"<\"\n  expected:\n  - quantity: R2 of Lorentzian fit to Pr\n    value: 0.92\n    tolerance: 0.092\n  - quantity: R2 of Gaussian fit to Pr\n    value: 0.96\n    tolerance: 0.096\n  - quantity: R2 of Lorentzian fit to YP\n    value: 0.98\n    tolerance: 0.098\n  - quantity: R2 of Gaussian fit to YP\n    value: 0.95\n    tolerance: 0.095\n  criterion: Set S2, 0-mm elevation. The left panel of Figure 5B is not named; it is read as the 0-mm\n    panel, the one whose peak is 100% (legend). Mean profiles in percent, F4 fits over -5 to 5 mm,\n    O1, O2. R2 is 1 - SSres / SStot over the fitted points. Reproduced when every R2 is within\n    tolerance and the ordering holds (Gaussian above Lorentzian for Pr, Lorentzian above Gaussian for\n    YP) under every reading; partially when the values are within tolerance but an ordering fails.\n- id: fig5c-nuclear-yp-centre\n  statement: In the central spot cells showed bright nuclear YP staining, indicating irreversible\n    damage, while farther out reversibly electroporated cells were weakly stained with less contrast\n    between nucleus and cytoplasm; cells inside the electrode footprint were unstained though present\n    (Hoechst).\n  source: Results 3.2, paragraph 1; Figure 5C\n  quote: Indeed, a closer examination of the central spot confirmed bright YP staining of cell nuclei\n    ( Fig. 5C , zone 1), which is indicative of the irreversible membrane damage and cell death.\n    Reversible electroporation is distinguished by a much weaker YP staining and smaller difference\n    in staining of the nucleus and cytoplasm, such as in zones 2 and 3 in Fig. 5C .\n  criterion: Set S2 at 0 mm. Zone locations are shown only in Figure 5A, not seen; readings for the\n    zones are zone 1 within 1 mm of the centre, zones 2 and 3 between 3 and 6 mm along a diagonal,\n    and the footprint inside an electrode wall. Nuclei are Hoechst-positive objects (Otsu threshold,\n    a standard choice); the cytoplasm is a ring around each nucleus, readings (a) 2 to 4 um, (b) 4 to\n    8 um. Reproduced when, under every reading, median nuclear YP in zone 1 exceeds that in zones 2\n    and 3, the median nucleus to cytoplasm YP ratio is higher in zone 1, footprint YP is below zones\n    2 and 3, and the footprint has Hoechst-positive nuclei. Blocked when the dataset lacks\n    full-resolution Hoechst and YP images of these wells.\n- id: fig6b-900ns-peak-not-significant\n  statement: The central YP peak was highest for 900-ns pulses, but not significantly different from\n    300- or 600-ns pulses.\n  source: Results 3.3, paragraph 2; Figure 6B\n  quote: The central peak of YP uptake was higher for 900-ns pulses, but the difference from the other\n    two pulse durations was not statistically significant (CT26 cells, 2 bursts (x4), Fig. 6B ).\n  criterion: A claim of absence, judged on the paper's test. Set S3, F1 to F3, O2; per experiment YP at\n    x = 0. Two-sided t tests of 900 ns against 300 ns and against 600 ns, Bonferroni over the two\n    (F7). Reproduced when the 900-ns mean is the highest and neither corrected p is below 0.05; not\n    reproduced when either is. Effect sizes are reported.\n- id: fig6c-normalized-decline-similar\n  statement: Normalized to the central peak, the sideways decline of YP was similar for the three\n    pulse durations.\n  source: Results 3.3, paragraph 2; Figure 6C\n  quote: When the peak YP emission was taken as 100%, its decline sideways was similar for the three\n    tested pulse durations ( Fig. 6C ).\n  criterion: Set S3, F1 to F3, O1, O2, each profile in percent of its value at x = 0 (Methods 2.5;\n    Figure 6C legend, the same data normalized to the peak). Whether each experiment or each mean is\n    normalized is not given; readings (a) each experiment, then mean +/- s.e., (b) the mean profile,\n    with s.e. scaled by the same factor. Judged by the paper's error-bar rule (F8). Reproduced when,\n    under every reading, no distance has two durations whose means differ by a gap larger than the\n    error bars.\n- id: fig6d-fwhm-falls-with-duration\n  statement: Longer pulses focused electroporation into a smaller spot; the FWHM fell with pulse\n    duration (slope p = 0.003), 600- and 900-ns pulses differed from 300 ns, and 900-ns packets gave\n    FWHM 1.7 +/- 0.08 mm, 11.1 +/- 0.6% of the gap between electrodes.\n  source: Results 3.3, paragraph 2; Figure 6D legend\n  quote: However, a more detailed analysis based on fitting of individual experiments (as described\n    in 3.1 ) revealed significant sharpening of the central peak when packets were built from 600-\n    and 900-ns pulses ( Fig. 6D ). The slope coefficient of the logarithmic fit of the data was\n    different from zero at p = 0.003 (one sample, 2-sided t -test). 900-ns pulse packets reduced FWHM\n    to 1.7 ± 0.08 mm, that was 11.1 ± 0.6% of the gap between electrodes.\n  statistics:\n  - about: slope of FWHM against pulse duration\n    test: one sample, 2-sided t-test\n    p: 0.003\n    n: 5 experiments per duration\n  - about: one of 600 or 900 ns against 300 ns (the legend marks * and ** without the text naming\n      which)\n    test: 2-sided t-test\n    p: 0.028\n    corrected: Bonferroni\n    n: 5 experiments per duration\n  - about: the other of 600 or 900 ns against 300 ns\n    test: 2-sided t-test\n    p: 0.0072\n    corrected: Bonferroni\n    n: 5 experiments per duration\n  expected:\n  - quantity: mean FWHM, 900-ns packets\n    value: 1.7\n    tolerance: 0.08\n    unit: mm\n  - quantity: mean FWHM, 900-ns packets, percent of 15.3 mm\n    value: 11.1\n    tolerance: 0.6\n    unit: percent\n  criterion: Set S3, F1 to F5, F7, F10, O1 to O4. Per-experiment Lorentzian FWHM. The trend's form is\n    open, as the text says \"logarithmic fit\" and the legend \"best linear fit\"; readings (a) FWHM\n    against duration, (b) FWHM against log duration, each slope tested by a two-sided t test.\n    Two-sided t tests of 600 ns and 900 ns against 300 ns, Bonferroni over the two. Reproduced when,\n    under every reading, the slope is negative with p < 0.05, both comparisons have corrected p <\n    0.05 and the 900-ns FWHM is within tolerance (the paper's s.e.). Partially reproduced when the\n    slope holds but a comparison or the value fails.\n- id: fig7be-peak-grows-with-bursts\n  statement: The central YP peak grew linearly with the number of bursts in both CT26 and CHO cells\n    (slope p < 0.001), except that it saturated after 6 bursts (x4) in CT26 cells.\n  source: Results 3.4, paragraph 2; Figure 7B, 7E legend\n  quote: Increasing the number of bursts increased the amplitude of the central peak of YP uptake in\n    both CT26 and CHO cells ( Fig 7A and D ). The increase was linear in both cell lines, except\n    when it reached saturation after 6 bursts (x4) in CT26 cells ( Fig. 7B and E ).\n  statistics:\n  - about: slope of central YP against bursts, CT26 (6 bursts (x4) excluded)\n    test: 2-sided one-sample t test\n    p: 0.001\n    p_relation: \"<\"\n    n: 3 to 5 experiments per burst number\n  - about: slope of central YP against bursts, CHO\n    test: 2-sided one-sample t test\n    p: 0.001\n    p_relation: \"<\"\n    n: 4 experiments per burst number\n  criterion: Set S4, F1 to F3, F7, O2, O4. Per experiment YP at x = 0 against the number of bursts;\n    linear least squares, the CT26 6-burst point left out (Figure 7B legend). Saturation is read\n    from the legend's 95% confidence band: the CT26 6-burst mean lies below the band of the fit\n    extrapolated to 6 bursts. Reproduced when both slopes are positive with p < 0.001 and the\n    saturation holds; partially when a slope is positive with p < 0.05 only, or saturation fails.\n- id: fig7cf-fwhm-bursts\n  statement: The FWHM of the central peak increased in proportion to the number of bursts in CT26\n    cells (slope p < 0.001) but not in CHO cells (p = 0.44).\n  source: Results 3.4, paragraph 2; Figure 7C, 7F legend\n  quote: Concurrently, FWHM of the central peak increased proportionally to the burst number in CT26\n    cells, but not in CHO cells ( Fig. 7C and F ).\n  statistics:\n  - about: slope of FWHM against bursts, CT26\n    test: 2-sided one-sample t test\n    p: 0.001\n    p_relation: \"<\"\n  - about: slope of FWHM against bursts, CHO\n    test: 2-sided one-sample t test\n    p: 0.44\n  criterion: Set S4, F1 to F5, F7, O1 to O4. Per-experiment Lorentzian FWHM against burst number,\n    linear least squares, slope tested two-sided. CHO 1-burst wells are left out (Figure 7 legend,\n    too small to measure FWHM). Whether the CT26 6-burst point enters the FWHM fit is not said\n    (the legend excludes it only from 7B); readings (a) included, (b) excluded. Reproduced when,\n    under every reading, the CT26 slope is positive with p < 0.001 and the CHO slope has p >= 0.05\n    (a claim of absence on the paper's test). Partially when the CT26 slope is positive with p <\n    0.05 only.\n- id: fig7-sharpest-one-burst\n  statement: One burst (x4) in CT26 cells gave the sharpest peak of the study, FWHM 1.1 +/- 0.1 mm,\n    7.3% of the inter-electrode gap and 2.3% of the array area, with YP near the electrodes 40 to 50\n    times smaller than at the centre.\n  source: Results 3.4, paragraph 3; Figure 7A, 7C\n  quote: That being said, 1 burst (x4) in CT26 cells produced the sharpest peak of electroporation\n    seen in this study: at FWHM of 1.1 ± 0.1 mm, it occupied just 7.3% of the inter-electrode gap and\n    2.3% of the electrode array area. Off-target effects, characterized by YP emission near\n    electrodes, were 40–50 times smaller than at the remote target.\n  depends_on:\n  - fig7cf-fwhm-bursts\n  expected:\n  - quantity: mean FWHM, CT26, 1 burst (x4)\n    value: 1.1\n    tolerance: 0.1\n    unit: mm\n  - quantity: FWHM in percent of 15.3 mm\n    value: 7.3\n    tolerance: 0.73\n    unit: percent\n  - quantity: ratio of centre YP to near-electrode YP, CT26, 1 burst (x4)\n    value: 45\n    tolerance: 9\n  criterion: Set S4, CT26 1-burst wells, FWHM as in fig7cf-fwhm-bursts with every reading of O3. The\n    ratio uses group means at x = 0 and near the electrodes (O5); the reported range 40 to 50 widened\n    by 10% of each bound gives 36 to 55, coded as 45 +/- 9 (so 36 to 54, with 55 also accepted). The\n    area percentage is not tested, as the paper does not say how it was computed from the FWHM.\n    Reproduced when the FWHM is within the paper's s.e. and is the smallest mean FWHM of any group in\n    sets S1, S3 and S4, the percent is within tolerance, and the ratio is within 36 to 55, under one\n    reading of O3 and O5 (the paper names one value for choices it leaves open).\n"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd claims/001047 && f=10.1016-j.bioelechem.2025.109016.yaml && python - <<'EOF'
import re
f='10.1016-j.bioelechem.2025.109016.yaml'
s=open(f).read()
s=s.replace("source: Results 3.1, paragraph 3 (sic, the paragraph on the ratio); Figure 4B; Abstract","source: Results 3.1, the sentences on the ratio of YP uptake in the center and near electrodes; Figure 4B; Abstract")
s=s.replace("""    value: 45
    tolerance: 9
  criterion: Set S4, CT26 1-burst wells, FWHM as in fig7cf-fwhm-bursts with every reading of O3. The
    ratio uses group means at x = 0 and near the electrodes (O5); the reported range 40 to 50 widened
    by 10% of each bound gives 36 to 55, coded as 45 +/- 9 (so 36 to 54, with 55 also accepted). The""","""    value: 45.5
    tolerance: 9.5
  criterion: Set S4, CT26 1-burst wells, FWHM as in fig7cf-fwhm-bursts with every reading of O3. The
    ratio uses group means at x = 0 and near the electrodes (O5); the reported range 40 to 50 widened
    by 10% of each bound gives 36 to 55, coded as 45.5 +/- 9.5. The""")
open(f,'w').write(s)
EOF
cd ../.. && python tools/claims_check.py claims/001047/$f paper/10.1016-j.bioelechem.2025.109016.txt; grep -n '—\|rather' claims/001047/$f
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
f=claims/001047/10.1016-j.bioelechem.2025.109016.yaml; sed -i "s/from the legend's 95% confidence band: the CT26/from the legend's 95% confidence band; the CT26/" $f; grep -n '[^ ]: ' $f | grep -v '^[0-9]*:#' | grep -vE '^[0-9]+: *(- )?[a-z_]+: ' ; python tools/claims_check.py $f paper/10.1016-j.bioelechem.2025.109016.txt; grep -n '—\|rather' $f
```

Result: not kept, because it reads the paper's text.

**Agent**

The quote has "study: at" in the paper; I'll cut the quote at the colon with "..." instead.

**Agent calls Bash**

```bash
f=claims/001047/10.1016-j.bioelechem.2025.109016.yaml; sed -i '476s/seen in this study: at FWHM/seen in this study ... at FWHM/' $f; python tools/claims_check.py $f paper/10.1016-j.bioelechem.2025.109016.txt; grep -n '—\|rather' $f
```

Result: not kept, because it reads the paper's text.

**Agent**

I wrote `claims/001047/10.1016-j.bioelechem.2025.109016.yaml`. The quote checker passes: 20 claims, 20 quotes, 15 statistical values, 0 problems.

**Text read.** The NIH author manuscript from PMC (NIHMS2087238, PMC12331426): main text, Methods, Results, Discussion and the legends of Figures 1 to 7. PMC lists no supplement and the paper cites none. I did not read the version of record. There is no PDF, so I saw none of the figures. The paper links no code ("Data will be made available on request"), so no method detail is settled by code. The dataset's title on DANDI and its species (mouse and hamster) match the paper's CT26 and CHO monolayer experiments.

**Claims.**
- **Count:** 20 claims, all quoted and none inferred.
- **Statistics:** 7 claims carry them, 15 entries in all. They are the fit p-values, the t-tests against 1 Hz with Bonferroni correction (p = 0.03, 0.02, 0.09), R = 0.77, the slope tests (p < 0.0001, 0.003, < 0.001, 0.44) and p = 0.028 and 0.0072 in Figure 6D.
- **Criteria:** all 20 have one. Three are claims of absence judged on the paper's own test: no rate effect at the centre, 900 ns not significantly higher, and no burst effect on the FWHM in CHO cells.
- **Coverage:** heating (Fig. 2); centre enhancement and off-target suppression (Fig. 3); Lorentzian fit and tail deviation; the 40-fold ratio; FWHM against packet rate and the log trend (Fig. 4); 3D experiments, YP against Pr spot size, the fit R² values and nuclear staining (Fig. 5); pulse duration (Fig. 6); burst number in both cell lines and the sharpest peak (Fig. 7).
- **Method details fixed from the paper (F1 to F10):** ROI size, background subtraction, pooling, the Lorentzian and Gaussian formulas, fit ranges, t-tests with Bonferroni, and percent of the 15.3 mm diagonal. For claims the paper states without a test, I used its own rule: a gap between error bars longer than the bars means p < 0.05.

**Details left open, with the readings named:**
- **O1, ROI positions:** ROIs at whole-mm distances, or contiguous ROIs. Which ROI side lies along the diagonal is a standard choice.
- **O2, "pooled" diagonals:** two diagonals averaged at each signed position, or all four half-diagonals averaged by distance. Figures 3B and 4A word this differently.
- **O3, fit range for FWHM in single experiments:** ±4 or ±5 mm for Figure 6D; ±4, ±5 or ±6 mm for Figure 7 (the Methods say "4–6 mm").
- **O4, what the regressions fit:** values from single experiments, or group means (Figures 6D and 7).
- **O5, "near electrodes" for the ratios:** 6 mm or 7 mm.
- **Figure 6D trend:** the text says "logarithmic fit" and the legend says "best linear fit"; both are run.
- **Figure 6D p-values:** which of 600 or 900 ns has p = 0.028 and which 0.0072 is not said.
- **Figure 6C normalization:** each experiment normalized, or the mean profile.
- **Figure 7C:** whether the CT26 6-burst point enters the FWHM fit.
- **Figure 3C "perimeter":** the outermost parallel ROIs, or all parallel ROIs at 4 mm or more.
- **Tail deviation:** measured in a.u. or in percent of the peak.
- **"Slightly larger" (YP against Pr spot):** a ratio of 1 to 1.25, or 1 to 1.5. The paper gives no bound.
- **Heating colours:** two sets of hue limits, as the paper gives none.
- **Figure 5C zones and the cytoplasm ring:** two ring widths. The zone positions are shown only in the figure.

**Missing from the paper:**
- The packet rates and burst numbers tested and the measured distances are only in the figures, which I could not see.
- How "2.3% of the electrode array area" was computed is not given, so that number is not tested.
- The Figure 4A legend cites "Fig. 2" for its data, which looks like a typo for Fig. 3.
- No code or data repository is linked.

## End of run

16 turns, 4 minutes, result: success.
