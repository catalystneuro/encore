# peron-2015 · claims · run 42691798626

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cat docs/protocol.md; ls paper/ claims/ | head -50; cat claims/fouke-2025.yaml
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
grep -n "^#" docs/protocol.md; ls paper/ | grep -i peron; ls claims | head
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "docs/protocol.md",
 "offset": 1,
 "limit": 192
}
```

```
1	# Protocol for an attempt
2	
3	Version: `pilot-14`. Record this version in the attempt's provenance.
4	
5	This is what agents, or people, do to attempt a target and deposit the
6	result. A target is a dataset in a public archive and a paper it names. How
7	each archive's datasets are named, versioned and read is in
8	[archives.md](archives.md); the examples here are from DANDI, the first. It is written from the pilot attempts
9	([pilot notes](pilot-notes.md)); the reasons for the rules are there.
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
[... 172 more lines not kept]
```

**Agent calls Bash**

```bash
ls -la paper/; cat claims/fouke-2025.yaml
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
ls claims | grep -i peron; cat papers/datasets/peron-2015.yaml 2>/dev/null; head -60 paper/10.1016-j.neuron.2015.03.027.txt; wc -l paper/*.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1016-j.neuron.2015.03.027.txt",
 "offset": 60,
 "limit": 700
}
```

Result: not kept, because it reads the paper's text.

**Agent**

Reading the paper text; the main body is there. Next I'll check whether the Supplemental Experimental Procedures are included.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1016-j.neuron.2015.03.027.txt",
 "offset": 760,
 "limit": 700
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
grep -n "=== page\|Supplemental\|SUPPLEMENT" paper/10.1016-j.neuron.2015.03.027.txt | tail -40
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1016-j.neuron.2015.03.027.txt",
 "offset": 1610,
 "limit": 440
}
```

Result: not kept, because it reads the paper's text.

**Agent**

Full text, Methods and supplement are all present. The paper links no analysis code, only the data DOI. Next I'll read the dataset description to see which experiments the dataset holds.

**Agent calls Bash**

```bash
cat paper/ssc-1.data-description.txt | head -150; grep -rn "github\|code" paper/10.1016-j.neuron.2015.03.027.txt | head
```

Result: not kept, because it reads the paper's text.

**Agent**

The dataset description covers the eight volume-imaging mice. The paper links no analysis code. Next I'll look at a recent claims file to match the conventions for provenance and fields.

**Agent calls Bash**

```bash
head -60 claims/espinosa-2017.yaml; grep -n "kind:\|data: \|open\|reading" claims/espinosa-2017.yaml | head -30; sed -n 1,80p tools/claims_check.py
```

```
# Claims for Espinosa, Alonso, Morales, Espinosa, Chavez & Fuentealba (2017), "Basal Forebrain
# Gating by Somatostatin Neurons Drives Prefrontal Cortical Activity", Cereb Cortex 29:42-53
# (advance access 17 November 2017), doi:10.1093/cercor/bhx302, tested on CRCNS bf-2 ("Basal
# forebrain extracellular recordings of anesthetized mice with somatostatin positive neurons
# optogenetically inhibited", doi:10.6080/K0MG7MQW).
# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"), 2026-11-09,
# protocol pilot-14 as stated in docs/protocol.md (Reader).
#
# Text read. The version of record with its supplement, as supplied under paper/
# (10.1093-cercor-bhx302.txt, PyMuPDF text of the journal PDF and of the supplementary PDF
# bhx302suppmat_161017.pdf): Methods, Results, Discussion, figure legends, and the supplement
# (Supplementary Figures 1 to 14, Supplementary Tables 1 to 3, the legends of Supplementary Movies 1
# to 3). The figures were read from their legends and the Results sentences that cite them. The
# supplementary movies were not supplied; no claim rests on them. Supplementary Table 2 prints
# p as "4.94E-04" and the Figure 1D legend prints "4.10×10−5"; the quote checker does not find
# these forms, so they were confirmed by reading.
#
# Code. The paper links no analysis code of its own. It names the tools it used: KlustaKwik
# (github.com/kwikteam/klustakwik2) for spike sorting, the Chronux toolbox for multitaper spectra
# and coherence, eegfilt.m from EEGLAB for the slow-band filter, circ_corrcl.m from CircStat, MATLAB
[... 150 more lines not kept]
```

**Agent calls Bash**

```bash
python -c "import json;d=json.load(open('schemas/claims.schema.json'));print(json.dumps(d,indent=1))" | head -200; grep -n "^dataset\|^  archive\|^  id\|^paper\|^schema" claims/espinosa-2017.yaml
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
[... 182 more lines not kept]
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

**Agent**

The text garbles Figure 3, Figure 8 and Figure 6, so I'll render those PDF pages to read them.

**Agent calls Bash**

```bash
cd $TMPDIR && python -c "
import fitz
d=fitz.open('paper/10.1016-j.neuron.2015.03.027.pdf')
for i in [5,8,10,3,6]:
    d[i].get_pixmap(dpi=130).save(f'p{i+1}.png')
" && ls $TMPDIR
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

Read tool can open PDF pages directly.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1016-j.neuron.2015.03.027.pdf",
 "pages": "6"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1016-j.neuron.2015.03.027.pdf",
 "pages": "11"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
pip install --quiet pymupdf 2>&1 | tail -2; python -c "import fitz; print(fitz.__doc__)"
```

```
Exit code 1
[notice] A new release of pip is available: 26.2.2 -> 26.3
[notice] To update, run: pip install --upgrade pip
Traceback (most recent call last):
  File "<string>", line 1, in <module>
    import fitz; print(fitz.__doc__)
    ^^^^^^^^^^^
ModuleNotFoundError: No module named 'fitz'
```

**Agent calls Bash**

```bash
pip install --user pymupdf 2>&1 | tail -3; python -m pip show pymupdf | head -3; python -c "import pymupdf; print('ok')"
```

```
Exit code 1

[notice] A new release of pip is available: 26.2.2 -> 26.3
[notice] To update, run: pip install --upgrade pip
WARNING: Package(s) not found: pymupdf
Traceback (most recent call last):
  File "<string>", line 1, in <module>
    import pymupdf; print('ok')
    ^^^^^^^^^^^^^^
ModuleNotFoundError: No module named 'pymupdf'
```

**Agent calls Bash**

```bash
python -c "import json;d=json.load(open('schemas/claims.schema.json'));print(json.dumps(d['properties']['claims']['items']['allOf'][2:],indent=1))"; grep -n "elsewhere" -A3 claims/*.yaml | grep -n "where:" | head -5
```

```
[
 {
  "if": {
   "properties": {
    "data": {
     "const": "elsewhere"
    }
   },
   "required": [
    "data"
   ]
  },
  "then": {
   "required": [
    "where"
   ]
  }
 }
]
2:claims/azcorra-2023.yaml-730-  where: GEO GSE222558 (samples GSM6926026 and GSM6926027)
[... 4 more lines not kept]
```

**Agent**

I have all the text I need. Now writing the claims file.

**Agent calls Write**

```json
{
 "file_path": "claims/peron-2015.yaml",
 "content": "# Claims for Peron, Freeman, Iyer, Guo & Svoboda (2015), \"A Cellular Resolution Map of Barrel Cortex\n# Activity during Tactile Behavior\", Neuron 86:783-799, doi:10.1016/j.neuron.2015.03.027, tested on\n# CRCNS ssc-1 (calcium imaging in vibrissal S1 of mice performing a pole localization task,\n# doi:10.6080/K0TB14TN).\n# Written by an agent (model \"claude-opus-5-5\", Claude Code, runner \"GitHub Actions\"), 2026-11-09,\n# protocol pilot-14 as stated in docs/protocol.md (Reader).\n#\n# Text read. The version of record with its Supplemental Information, as supplied under paper/\n# (10.1016-j.neuron.2015.03.027.txt, PyMuPDF text of the journal PDF followed by the supplement):\n# Summary, Results, Discussion, Experimental Procedures, figure legends, and the supplement (legends\n# of Figures S1 to S7, Table S1, Supplemental Experimental Procedures). The PDF pages could not be\n# rendered in this run (no renderer was available), so the numbers printed only inside the panels of\n# Figures 3, 6 and 8 (the per-population percentages of Figure 3, the Pearson r and p of Figure 8E,\n# 8I and 8K) were not read and no expected value rests on them. The figures were read from their\n# legends and the Results sentences that cite them.\n#\n# Code. The paper links no analysis code. It names ScanImage (scanimage.org) for acquisition, the\n# Janelia Whisker Tracker (Clack et al., 2012), BControl for the task, and \"a custom, automated MATLAB\n# package\" for whisker identity, none of which settles an analysis choice. Every method below is from\n# the Experimental Procedures, the Results, the figure legends or the Supplemental Experimental\n# Procedures.\n#\n# Data the paper describes (Table S1, Experimental Procedures).\n# (1) Volume imaging, 8 mice (an171923, an194181, an194672, an197522, an198503, an229716, an229717,\n#     an229719): six Emx1-Cre x Rosa26-LSL-H2B-mCherry (red nuclei in excitatory neurons), one\n#     Gad2-T2A-NLS-mCherry (an194181, red nuclei in GABAergic neurons), one C57BL/6 without a red\n#     marker (an171923). Spared whiskers C2, D2, D2, D2, C3, C2, D3, D2 in that order (Table S1). Each\n#     mouse has two volumes of eight subvolumes; a subvolume is three planes 15 um apart (600 x 600 um,\n#     512 x 512 pixels) imaged at 7 Hz, each subvolume over 4.0 sessions on average (range 1 to 8),\n#     data pooled across sessions. L1 to L3 over 360 um of depth. Core counts are 82,732 L2/3\n#     excitatory neurons, 777 L1 neurons, 3,806 L2/3 GABAergic neurons and 2,469 L5 apical dendrites\n#     imaged in deep L3 (Figure 3 prints n=2496 for L5).\n# (2) Imaging during learning, 4 of these mice (an194181, an194672, an197522, an198503): one subvolume\n#     of three planes 120 um apart tracked from the start of training, 7, 10, 13 and 17 sessions; 1,612,\n#     1,913, 1,552 and 1,301 neurons imaged during learning (Table S1).\n# (3) L4 axon imaging in L2/3, 3 Scnn1a-Tg3-Cre mice (an224823, an227254, an238004) with FLEX GCaMP6s;\n#     six subvolumes, grid ROIs of 12 x 12 um on a 25 um grid (Figure S5).\n# (4) Anesthetized against awake directionality imaging, 3 Emx1-Cre x LSL-H2B-mCherry mice (an257218,\n#     an257219, an257221), passive piezo deflection under 0.5% isoflurane (Figure 8G to 8K).\n# (5) Simultaneous imaging of L5A somata and deep L3 apical dendrites, 42 pairs from 3 mice (Figure S4);\n#     the mice are not named.\n# Behavior: trials with a 1 s sample epoch (pole in reach), 1 s delay, a 50 ms auditory reward cue and\n# a response epoch; correct response right for proximal pole positions, left for the distal position;\n# trial types hit and error, left and right, and no response. Whisker video at 500 Hz gives whisker\n# angle (theta, positive for protraction) and curvature change (delta kappa, negative for touches\n# during protraction, zero outside touch), and touch times verified by hand. The data set's\n# description (CRCNS ssc-1 data description, version 0.8) speaks of the eight volume-imaging mice,\n# with per-session and per-volume MATLAB structures holding ROI masks, raw fluorescence, dF/F,\n# extracted calcium events, whisker angle, curvature, touch times, trial types, timing and outcomes,\n# and raw images and whisker videos. Whether it holds the learning, L4 axon, anesthetized and L5-soma\n# data, the high-resolution stacks and the column outlines is for the author to find.\n#\n# Shared method, from the Experimental Procedures, used by the criteria below unless a claim says\n# otherwise.\n# M1 Activity. All analyses use the event-based dF/F (events convolved with their rise and decay),\n#    \"unless noted\" (Results, Imaging Large Neuronal Populations, paragraph 8; Calcium Imaging\n#    Analysis, step 5). Where the data set holds the events or event-based trace, they are used as\n#    given; the event detector is not rerun.\n# M2 Active. Event rate > 0.0083 Hz (Figure 3A legend).\n# M3 Task related. Per ROI and per correct trial type (left, right), the fraction of trials with an\n#    event in each trial-aligned time bin; events shuffled in time 10,000 times; task related when the\n#    real peak exceeds the 95th percentile of shuffled peaks for at least one trial type (Model-Free\n#    Analysis, paragraph 1). Open: the bin width (readings are one imaging frame at 7 Hz, and the\n#    frame rate of the subvolume as acquired, the same thing for volume data) and the shuffle scope\n#    (readings are events shuffled within each trial, and across the whole session).\n# M4 Trial-type discrimination. Per neuron, ROC on the decision variable \"dot product of the trial's\n#    PSTH with the mean respond-left PSTH minus that with the mean respond-right PSTH\", PSTH from the\n#    event trace without decay, activity up to the reward cue, correct and error trials, no-response\n#    trials excluded, AUC above the 95th percentile of 100 label shuffles; pooled across all volumetric\n#    sessions (Model-Free Analysis, paragraph 2; Results, Task-Related Activity, paragraph 4). Open:\n#    whether the trial itself is left out of the mean PSTH (readings are included, and left out); the\n#    time bin of the PSTH (one frame is the standard choice).\n# M5 Encoding model. Per neuron, dF/F modelled as f1(theta)*k1 + f2(delta kappa)*k2 with Gaussian\n#    noise; f1, f2 sums of 16 tent functions, applied at 500 Hz and linearly downsampled to 7 Hz; k1, k2\n#    of 14 time points (2 s); fit by alternating least squares (3 to 5 iterations), nonlinearities\n#    rescaled to 0..1 after each iteration; smoothness prior with inverse covariance the second\n#    difference matrix (2 on the diagonal, -1 off it); 5-fold cross-validation across trials, Rfit the\n#    Pearson r of held-out predicted and actual dF/F. A neuron encodes touch (whisking) when the model\n#    fit with curvature (angle) alone has Rfit above the 95th percentile of 100 fits to time-shuffled\n#    traces made by redistributing the neuron's events at random with their rise and decay; both\n#    significant is \"mixed\". For volume data the fit uses all sessions pooled; for learning, single\n#    sessions with the 99th percentile; for maps (Figures 7, 8D, S5), the 99th percentile (Model-Based\n#    Encoding Analysis). Open, and able to change the counts: (a) the penalty scale, which the paper\n#    chose \"from a cross-validated inspection of a random subset of ROIs\" without giving it; readings\n#    are a single scale chosen by cross-validated Rfit over a log grid on a random subset of ROIs and\n#    applied to all, and a scale chosen per neuron by cross-validation; (b) the tent knots, not placed\n#    by the paper; readings are 16 knots equally spaced over the range of the variable, and at its\n#    quantiles; (c) the kernel lags, readings are lags 0 to 13 frames after the input (causal) and\n#    lags centred on 0; (d) which frames enter the fit, readings are all imaged frames of the trials,\n#    and the trial frames only. Touch and whisking bouts are aligned at first touch and at the first\n#    frame where the Hilbert amplitude of whisking exceeds 10 degrees (Supplemental Experimental\n#    Procedures); used for display only.\n# M6 Columns and layers. The principal column is the barrel column of the spared whisker, from\n#    confocal sections, two-photon L4 images, intrinsic signal imaging and the neuropil touch signal\n#    (Figure S1). Laminar borders as in Experimental Procedures (Two Photon Imaging, paragraph 4).\n#    The author uses the column and layer labels the data set carries; if it carries none, the claims\n#    that need them are blocked, as no rule here could redraw them.\n# M7 Summaries. Percentages given \"n = 8 mice\" are read as the mean and spread over mice of per-mouse\n#    fractions. Where the paper does not say, the spread is read as SD (the paper states \"mean ± SD\"\n#    for the behavioral numbers, learning numbers and dendrite numbers); a reading as SEM is shown as\n#    a variant. Pooled fractions over all mice (Figure 3, which prints pooled n) are a second reading.\n#\n# Discrepancies in the paper. L5 apical dendrites are 2,469 in the Results and n=2496 in Figure 3.\n# Mice reaching criterion are \"n = 8 mice\" in the Results, while Figure 1E legend marks some mice as\n# not imaged during training. The Experimental Procedures say \"Four ... imaging planes were acquired at\n# 7 Hz\", the Results three planes per subvolume; the fourth is the fly-back frame, discarded.\n# The Summary gives \"300 layer (L) 2/3 pyramidal neurons (17%)\" per column for each of touch and\n# whisking; the Discussion gives 12% touch, 12% whisking and 5% both in the principal column.\nschema_version: 2\npaper: doi:10.1016/j.neuron.2015.03.027\nclaims:\n- id: table-s1-roi-counts\n  statement: The eight volume-imaging mice have ROI counts (neurons and apical dendrites) of 11,031,\n    9,637, 13,788, 16,200, 8,288, 12,293, 19,012 and 18,125, with spared whiskers C2, D2, C2, D2, C3,\n    C2, D3 and D2 (an171923, an194181, an194672, an197522, an198503, an229716, an229717, an229719).\n  source: Table S1\n  inferred: Numbers from Table S1; no sentence states them. The table text was read from the\n    extracted supplement.\n  expected:\n  - quantity: total ROI count over the eight volume-imaging mice\n    value: 108374\n    tolerance: 10837\n    unit: ROIs\n  criterion: Per mouse, the number of somatic and apical dendrite ROIs in the volume-imaging data\n    (not the L4 axon or anesthetized mice) and the spared whisker. Reproduced when every mouse's count\n    is within 10% of its Table S1 value and the spared whiskers match; partially reproduced when at\n    least six mice match. The total is shown with them.\n- id: fig2-core-counts\n  statement: The core data set comprises 82,732 excitatory L2/3 neurons, 777 L1 neurons and 3,806\n    L2/3 GABAergic neurons from 8 mice, and 2,469 L5 apical dendrites imaged in deep L3.\n  source: Results, Imaging Large Neuronal Populations in Behaving Mice, paragraphs 6 and 9; Figure 3\n  quote: Our core data set comprised 82,732 excitatory L2/3 neurons, 777 L1 neurons, and 3,806 L2/3\n    GABAergic neurons (n = 8 mice\n  expected:\n  - quantity: L2/3 excitatory neurons\n    value: 82732\n    tolerance: 8273\n  - quantity: L1 neurons\n    value: 777\n    tolerance: 78\n  - quantity: L2/3 GABAergic neurons\n    value: 3806\n    tolerance: 381\n  - quantity: L5 apical dendrites\n    value: 2469\n    tolerance: 247\n  criterion: Counts of ROIs by class (L1, L2/3 excitatory, L2/3 GABAergic, L5 apical dendrite) over the\n    8 volume-imaging mice, using the class labels the data set carries. For apical dendrites the\n    readings are 2,469 (Results) and 2,496 (Figure 3); either matches. Reproduced when all four counts\n    are within tolerance; partially reproduced when two or three are.\n- id: results-gaba-fraction\n  statement: GABAergic neurons are 4.3% of the 86,538 L2/3 neurons recorded, about a third of those\n    expected, so sampling of GABAergic neurons is incomplete.\n  source: Results, Imaging Large Neuronal Populations in Behaving Mice, paragraph 6\n  quote: We found 3,806 GABAergic neurons among 86,538 neurons in L2/3 (4.3%)\n  expected:\n  - quantity: GABAergic fraction of L2/3 neurons\n    value: 4.3\n    tolerance: 0.43\n    unit: percent\n  - quantity: L2/3 neurons\n    value: 86538\n    tolerance: 8654\n- id: fig2e-fraction-imaged\n  statement: In L2/3, 76% ± 6% of red nuclei counted in the high-resolution stacks had a corresponding\n    ROI, and a barrel column holds 1,796 ± 299 L2/3 pyramidal neurons (n = 5 volumes).\n  source: Results, Imaging Large Neuronal Populations in Behaving Mice, paragraph 6; Figure 2E\n  quote: In L2/3, 76% ± 6% of red nuclei had corresponding ROIs ... Our count for L2/3 pyramidal\n    neurons per barrel column (1,796 ± 299; n = 5 volumes\n  expected:\n  - quantity: fraction of L2/3 red nuclei with ROIs\n    value: 76\n    tolerance: 6\n    unit: percent\n  - quantity: L2/3 pyramidal neurons per barrel column\n    value: 1796\n    tolerance: 299\n  criterion: Nuclei detected in the red channel of the reference stack by a 3D Gaussian mixture model\n    looking for spheres 10 um in diameter, with the expected nuclear pixel fraction set by eye per\n    stack (Two Photon Imaging, paragraph 3); imaging planes aligned to the stack; the fraction of L2/3\n    nuclei with an ROI per volume, over 5 volumes. The nuclear pixel fraction and the distance within\n    which a nucleus counts as matched are not given; the nuclei counts the data set carries are used\n    when it has them, and otherwise the claim is blocked as methods_underspecified. Which 5 volumes is\n    open; readings are any 5 Emx1-Cre x LSL-H2B-mCherry volumes and the means over all such volumes.\n- id: fig1e-days-to-criterion\n  statement: Mice reached criterion performance (d-prime > 1.5) after 11 ± 4 days of training (mean ±\n    SD, n = 8 mice).\n  source: Results, Imaging Large Neuronal Populations in Behaving Mice, paragraph 2; Figure 1E\n  quote: Mice reached criterion level performance (d-prime > 1.5, or approximately 70% trials correct;\n    Figure 1E) after 11 ± 4 days (mean ± SD; n = 8 mice) of training\n  expected:\n    quantity: training days to criterion\n    value: 11\n    tolerance: 4\n    unit: days\n  criterion: d-prime per training day from hits and false alarms over left and right trials, with\n    right-lick trials as signal (the paper does not say which side is signal; d-prime is symmetric\n    under the swap). Days to criterion is the first day with d-prime > 1.5. Readings for the first day\n    counted are the first training day as day 1, and the first day of the full task (Figure 6D legend\n    says the first day was a simplified task). Reproduced when the mean over the mice with training\n    records is within tolerance under one reading. Blocked when the data set lacks training sessions.\n- id: results-trials-per-session\n  statement: Mice performed 245 ± 71 trials per session during imaging.\n  source: Results, Imaging Large Neuronal Populations in Behaving Mice, paragraph 2\n  quote: Mice performed 245 ± 71 trials per session during imaging\n  expected:\n    quantity: trials per imaging session\n    value: 245\n    tolerance: 71\n    unit: trials\n  criterion: The number of behavioral trials per volume-imaging session. Readings are the mean over all\n    sessions pooled, and the mean of per-mouse means. Reproduced when one reading is within tolerance.\n- id: results-whisking-amplitude\n  statement: The task elicited larger amplitude whisker movements than similar two-position tasks,\n    55.5 ± 13.3 degrees (mean ± SD, n = 8 mice) against about 20 degrees.\n  source: Results, Imaging Large Neuronal Populations in Behaving Mice, paragraph 2\n  quote: our task elicited larger amplitude whisker movements (approximately 20\n  expected:\n    quantity: whisker movement amplitude\n    value: 55.5\n    tolerance: 13.3\n    unit: degrees\n  criterion: The paper does not define the amplitude measure. Readings are (a) the per-trial range of\n    whisker angle (maximum minus minimum) over the trial, (b) the same over the sample epoch, (c) the\n    peak Hilbert amplitude of whisking per trial (the amplitude the Supplemental Experimental\n    Procedures use for bout onset); each averaged per mouse, then over 8 mice. Reproduced when the mean\n    over mice is within tolerance under one reading. The degree values printed in the text are\n    garbled in the extraction; the quote stops before them.\n- id: fig1g-early-stereotypy\n  statement: Whisker movements became stereotyped early in training, while performance rose more\n    gradually.\n  source: Results, Imaging Large Neuronal Populations in Behaving Mice, paragraph 2; Figures 1E to 1G\n  quote: Whisker movements became stereotyped early during training (Figure 1G; Supplemental\n    Experimental Procedures) (Huber et al., 2012), whereas behavioral performance increased more\n    gradually (Figure 1E)\n  criterion: Stereotypy per day as in the Supplemental Experimental Procedures, the R2 of each trial's\n    whisker angle vector with the mean vector of its trial type (left or right, correct or error),\n    averaged with weights by trials per type; for the three mice with the longest training\n    videography (Figure 1G legend). The angle vector's window is not given; readings are the whole\n    trial and the sample epoch. Reproduced when, for at least two of the three mice, stereotypy reaches\n    90% of its final-two-day mean on an earlier training day than d-prime reaches 90% of its final\n    two-day mean. Blocked when the data set lacks training videography.\n- id: supp-trim-all-chance\n  statement: After all whiskers were trimmed, performance fell to chance (d-prime -0.03 ± 0.11, mean ±\n    SD, n = 4 mice), so mice used touch to solve the task.\n  source: Supplemental Experimental Procedures, Behavioral training, paragraph 2\n  quote: After trimming all whiskers, performance fell to chance level (d-prime -0.03 ± 0.11, mean ±\n    S.D., n=4 mice), confirming that mice used tactile cues to solve the task\n  expected:\n    quantity: d-prime after trimming all whiskers\n    value: -0.03\n    tolerance: 0.11\n- id: figs4-dendrite-soma\n  statement: Activity in L5 apical dendrites imaged in deep L3 reports somatic activity; 91.0% ± 15.1% of\n    somatic events had dendritic events and 90.9% ± 12.7% the reverse (845 events, 42 pairs, 3 mice),\n    and the soma-dendrite correlation (0.63 ± 0.11) did not differ from that of a model with perfect\n    event correspondence (0.69 ± 0.28, Wilcoxon signed rank p = 0.063).\n  source: Results, Imaging Large Neuronal Populations in Behaving Mice, paragraph 9; Figure S4\n  quote: manual inspection of 845 events (n = 42 dendrite-soma pairs, n = 3 mice) revealed that 91.0% ±\n    15.1% of somatic events (mean ± SD) had corresponding dendritic events, and 90.9% ± 12.7% of\n    dendritic events had corresponding somatic events ... the correlation between the somatic and\n    dendritic signals was 0.63 ± 0.11 ... was similar to the experimentally measured correlation\n    (Wilcoxon signed rank test, p = 0.063\n  statistics:\n  - about: somatic against dendritic signal correlation\n    test: Pearson's R\n    p: 0.001\n    p_relation: \"<\"\n    n: 42 pairs\n  - about: measured against modelled correlation\n    test: Wilcoxon signed rank test\n    p: 0.063\n    n: 42 pairs\n  expected:\n  - quantity: soma-dendrite correlation\n    value: 0.63\n    tolerance: 0.11\n  - quantity: modelled correlation\n    value: 0.69\n    tolerance: 0.28\n  criterion: Pearson r of somatic and dendritic dF/F per pair (raw or event-based is not said; readings\n    are both). The event matching was by hand and is not repeated; the matching fractions are compared\n    only if the data set records them. The model convolves each pair's events with\n    compartment-specific kernels and adds compartment-specific noise, whose sizes are not given;\n    readings are the kernels and noise SD estimated from each compartment's own trace. Reproduced when\n    the measured r is within tolerance and, under one reading, the signed-rank test of measured against\n    modelled r gives p >= 0.05. Blocked when the data set lacks the L5-L3 pairs.\n- id: fig3a-active-fraction\n  statement: Most neurons were not silent; L2/3 excitatory neurons had the lowest proportion of active\n    neurons, 67% ± 5.4% (n = 8 mice).\n  source: Results, Task-Related Activity, paragraph 1; Figure 3A\n  quote: The lowest proportion of active neurons was seen in L2/3 excitatory neurons (67% ± 5.4%; n = 8\n    mice\n  expected:\n    quantity: active fraction, L2/3 excitatory\n    value: 67\n    tolerance: 5.4\n    unit: percent\n  criterion: Active as M2, event rate > 0.0083 Hz over the neuron's imaged time. Reproduced when the L2/3\n    excitatory fraction (M7 readings) is within tolerance and is the lowest of L1, L2/3 excitatory, L2/3\n    GABAergic and L5 dendrite fractions.\n- id: fig3b-task-related\n  statement: 40% of neurons showed task-related activity, lowest in L2/3 (39% ± 2.9%), intermediate in L5\n    excitatory neurons (43% ± 4.1%) and high in GABAergic neurons of L1 (57% ± 12%) and L2/3 (63% ± 7%).\n  source: Results, Task-Related Activity, paragraph 2; Figure 3B\n  quote: Overall, 40% of neurons showed task-related activity (Figure 3B). The proportion of task-related\n    neurons was lowest in L2/3 (39% ± 2.9%), intermediate for L5 excitatory neurons (43% ± 4.1%), and\n    high for GABAergic neurons, both in L1 and L2/3 (57% ± 12% and 63% ± 7%, respectively\n  expected:\n  - quantity: task-related fraction, all neurons\n    value: 40\n    tolerance: 4\n    unit: percent\n  - quantity: task-related fraction, L2/3 excitatory\n    value: 39\n    tolerance: 2.9\n    unit: percent\n  - quantity: task-related fraction, L5 excitatory\n    value: 43\n    tolerance: 4.1\n    unit: percent\n  - quantity: task-related fraction, L1 GABAergic\n    value: 57\n    tolerance: 12\n    unit: percent\n  - quantity: task-related fraction, L2/3 GABAergic\n    value: 63\n    tolerance: 7\n    unit: percent\n  criterion: Task related as M3, over all ROIs of each class (not only active ones; the paper does not\n    restrict, and Figure 3B prints n equal to the class totals). The \"overall\" fraction pools all\n    classes. Reproduced when, under one reading of M3 and M7, all five values are within tolerance and\n    the order L2/3 < L5 < GABAergic holds; partially reproduced when the order holds and at least three\n    values are within tolerance.\n- id: fig4d-sample-epoch-principal\n  statement: Activity of L2/3 neurons spans the trial with a bias toward the sample epoch, and in the\n    principal column sample-epoch activity is elevated relative to surround columns for all excitatory\n    classes.\n  source: Results, Task-Related Activity, paragraph 3; Figures 4C and 4D\n  quote: Across the population, activity spanned the behavioral trial (Figure 4C), with a pronounced\n    bias toward the sample epoch during which the animal interacted with the stimulus. In the principal\n    barrel column, activity in the sample epoch was substantially elevated relative to surround\n    columns for all excitatory neuron classes examined\n  criterion: For task-related ROIs (M3), the peak time of the trial-averaged activity (Figure 4C, 4D);\n    the fraction of peaks per unit time in the sample epoch against the rest of the trial up to 2 s\n    after the reward cue. Reproduced when, for L2/3 excitatory neurons, the density of peaks in the\n    sample epoch is the highest of the epochs (pre-trial, sample, delay, response), and, for L2/3 and\n    L5 excitatory classes, the fraction of task-related ROIs peaking in the sample epoch is higher in\n    the principal column than in surround columns (M6). The epochs come from each trial's timing.\n- id: fig4d-gaba-reward-cue\n  statement: GABAergic neurons in L1 and L2/3 show, besides a sample-epoch peak, activity around the\n    reward cue, most prominent in surround columns.\n  source: Results, Task-Related Activity, paragraph 3; Figure 4D\n  quote: In addition to a response peak during the sample epoch, GABAergic neurons in L1 and L2/3 were\n    active around the reward cue, which was especially prominent in surround columns\n  criterion: As fig4d-sample-epoch-principal. \"Around the reward cue\" is not bounded; readings are 0.5 s\n    and 1 s either side of the cue. Reproduced when, under one reading, the fraction of task-related\n    GABAergic ROIs (L1 and L2/3 together and each) peaking around the cue exceeds that of L2/3\n    excitatory neurons, and is higher in surround than in principal columns.\n  depends_on:\n  - fig4d-sample-epoch-principal\n- id: fig3c-discriminative\n  statement: Among L2/3 excitatory neurons in the principal column 9.7% ± 8.5% discriminated trial type\n    above chance; L5 excitatory (17.3% ± 7.1%) and L2/3 GABAergic neurons (20.7% ± 11.5%) did better,\n    and most neuropil ROIs were discriminative (56.1% ± 31.4%).\n  source: Results, Task-Related Activity, paragraph 4; Figure 3C\n  quote: Among L2/3 excitatory neurons in the principal column, 9.7% ± 8.5% discriminated trial type\n    above chance level (n = 8 mice; Figure 3C). L5 excitatory (17.3% ± 7.1%) and L2/3 GABAergic neurons\n    (20.7% ± 11.5%) performed better. A majority of neuropil ROIs were discriminative (56.1% ± 31.4%\n  expected:\n  - quantity: discriminative fraction, L2/3 excitatory, principal column\n    value: 9.7\n    tolerance: 8.5\n    unit: percent\n  - quantity: discriminative fraction, L5 excitatory\n    value: 17.3\n    tolerance: 7.1\n    unit: percent\n  - quantity: discriminative fraction, L2/3 GABAergic\n    value: 20.7\n    tolerance: 11.5\n    unit: percent\n  - quantity: discriminative fraction, L2/3 neuropil\n    value: 56.1\n    tolerance: 31.4\n    unit: percent\n  criterion: Discriminative as M4. Whether the L5, GABAergic and neuropil fractions are of the principal\n    column only is not said; readings are principal column, and all columns. Reproduced when, under one\n    reading of M4 and M7, all four fractions are within tolerance and the L2/3 excitatory fraction is\n    the lowest of the four.\n- id: fig3d-principal-touch-whisking-equal\n  statement: In the principal column, L2/3 excitatory neurons were equally likely to represent whisking\n    (17.0% ± 5.2%) and touch (16.8% ± 9.0%; Wilcoxon signed rank p = 0.938, n = 8 mice).\n  source: Results, Encoding Model of Neural Coding, paragraph 3; Figure 3D\n  quote: Layer 2/3 excitatory neurons were equally likely to show representation of whisking and touch\n    within the principal column (17.0% ± 5.2% and 16.8% ± 9.0%, respectively; p = 0.938, Wilcoxon\n    signed rank test, n = 8 mice\n  statistics:\n  - test: Wilcoxon signed rank test\n    p: 0.938\n    n: 8 mice\n  expected:\n  - quantity: whisking fraction, L2/3 excitatory, principal column\n    value: 17.0\n    tolerance: 5.2\n    unit: percent\n  - quantity: touch fraction, L2/3 excitatory, principal column\n    value: 16.8\n    tolerance: 9.0\n    unit: percent\n  criterion: Classes as M5 at the 95th percentile, fractions including mixed neurons in each (17% each,\n    against 12% + 5% in the Discussion), per mouse over principal-column L2/3 excitatory neurons (M6). A\n    claim of absence for the comparison; judged on the paper's test, a Wilcoxon signed rank test of\n    touch against whisking fractions over 8 mice, at p < 0.05. Reproduced when, under one reading of\n    M5, both fractions are within tolerance and the test gives p >= 0.05; the difference is reported.\n- id: fig3d-surround-whisking-dominates\n  statement: In surround columns whisking representation dominated touch among L2/3 excitatory neurons\n    (15.0% ± 3.9% against 8.9% ± 2.0%, p = 0.008).\n  source: Results, Encoding Model of Neural Coding, paragraph 3; Figure 3D\n  quote: In surround columns, whisking representation dominated (15.0% ± 3.9% whisking versus 8.9% ± 2.0%\n    touch; p = 0.008\n  statistics:\n  - test: Wilcoxon signed rank test\n    p: 0.008\n    n: 8 mice\n  expected:\n  - quantity: whisking fraction, L2/3 excitatory, surround columns\n    value: 15.0\n    tolerance: 3.9\n    unit: percent\n  - quantity: touch fraction, L2/3 excitatory, surround columns\n    value: 8.9\n    tolerance: 2.0\n    unit: percent\n  criterion: As fig3d-principal-touch-whisking-equal, over surround-column neurons. The test is not\n    named in the sentence; it is read as the Wilcoxon signed rank test of the preceding sentence.\n    Reproduced when, under one reading of M5, both fractions are within tolerance and the test gives\n    p < 0.05 with whisking higher; partially reproduced when the test holds and one fraction is out of\n    tolerance.\n- id: fig3d-population-encoding\n  statement: About a quarter of L2/3 excitatory neurons encoded whisker movement or touch, the lowest of\n    any group; L2/3 GABAergic and L5 excitatory neurons represented whisking more often than touch; the\n    neuropil was dominated by touch but most ROIs also encoded whisking.\n  source: Results, Encoding Model of Neural Coding, paragraph 3; Figure 3D\n  quote: Overall, about a quarter of L2/3 excitatory neurons encoded whisker movement or touch, the\n    lowest proportion observed for any group. Among L2/3 GABAergic neurons as well as L5 excitatory\n    neurons, whisker movements were represented by a larger proportion of neurons compared to touch.\n    The neuropil was dominated by touch, but it also showed detectable encoding of whisker movements in\n    the majority of ROIs\n  expected:\n    quantity: fraction of L2/3 excitatory neurons encoding touch or whisking\n    value: 25\n    tolerance: 2.5\n    unit: percent\n  criterion: Classes as M5. \"About a quarter\" is read as 25% with the 10% tolerance. Reproduced when,\n    under one reading of M5 and M7, the L2/3 excitatory fraction encoding either is within tolerance and\n    lower than that of L1, L2/3 GABAergic and L5 neurons; whisking exceeds touch in L2/3 GABAergic and\n    L5 neurons; and in neuropil ROIs touch exceeds whisking and more than half encode whisking.\n    Partially reproduced when at least three of these four parts hold.\n- id: discussion-principal-exclusive-classes\n  statement: In the principal column 12% of L2/3 neurons reported touch only, 12% whisker movements\n    only, and 5% both.\n  source: Discussion, paragraph 3\n  quote: In the principal column, 12% of L2/3 neurons reported touch, 12% reported whisker movements, and\n    5% reported both\n  expected:\n  - quantity: touch-only fraction, principal column L2/3\n    value: 12\n    tolerance: 1.2\n    unit: percent\n  - quantity: whisking-only fraction, principal column L2/3\n    value: 12\n    tolerance: 1.2\n    unit: percent\n  - quantity: mixed fraction, principal column L2/3\n    value: 5\n    tolerance: 0.5\n    unit: percent\n  criterion: Classes as M5. Readings are fractions pooled over the 8 mice (Figure 3D, n = 14,165 principal\n    column neurons per the figure text), and means of per-mouse fractions. \"Touch\" and \"whisking\" are\n    read as exclusive of \"both\", as 12 + 5 = 17 matches the Results. Reproduced when, under one reading,\n    all three are within tolerance; partially reproduced when two are.\n  depends_on:\n  - fig3d-principal-touch-whisking-equal\n- id: fig6b-touch-fraction-stable\n  statement: During learning the fraction of touch neurons was constant (days 1 and 2 0.15 ± 0.05, 5 and\n    4 days before the end 0.14 ± 0.06, final two days 0.15 ± 0.07; first against final p = 1, middle\n    against final p = 0.573, Wilcoxon rank-sum, n = 4 mice).\n  source: Results, Imaging during Learning, paragraph 2; Figure 6B\n  quote: The fraction of touch neurons was constant from the start or middle of training relative to the\n    end of training (Figure 6B) ... final two days 0.15 ± 0.07; first two versus final two p = 1 ...\n    Wilcoxon rank-sum test; middle versus final p = 0.573\n  statistics:\n  - about: first two against final two days\n    test: Wilcoxon rank-sum test\n    p: 1\n    n: 4 mice, 2 days per mouse\n  - about: middle two against final two days\n    test: Wilcoxon rank-sum test\n    p: 0.573\n    n: 4 mice, 2 days per mouse\n  expected:\n  - quantity: touch fraction, days 1 and 2\n    value: 0.15\n    tolerance: 0.05\n  - quantity: touch fraction, 5 and 4 days before end\n    value: 0.14\n    tolerance: 0.06\n  - quantity: touch fraction, final two days\n    value: 0.15\n    tolerance: 0.07\n  criterion: Per session, M5 fit to that session with the 99th percentile criterion and only the\n    eventual spared whisker's angle and curvature, over L2/3 excitatory neurons imaged during learning;\n    two sessions per animal per group (Model-Based Encoding Analysis, paragraph 7). The rank-sum test\n    is read as over 8 values per group (4 mice x 2 days), as \"n = 4 mice, 2 days per mouse\" states; a\n    test on 4 per-mouse means is a variant. A claim of absence; reproduced when both tests give p >=\n    0.05 and the three means are within tolerance; the differences are reported.\n- id: fig6b-whisking-fraction-early\n  statement: The fraction of whisking neurons increased during early training only (0.13 ± 0.04, 0.20 ±\n    0.09, 0.19 ± 0.05; first against final p = 0.010, middle against final p = 0.798).\n  source: Results, Imaging during Learning, paragraph 2; Figure 6B\n  quote: The fraction of whisking neurons increased, but only during early training (days 1 and 2\n    whisking fraction\n  statistics:\n  - about: first two against final two days\n    test: Wilcoxon rank-sum test\n    p: 0.01\n    n: 4 mice, 2 days per mouse\n  - about: middle two against final two days\n    test: Wilcoxon rank-sum test\n    p: 0.798\n    n: 4 mice, 2 days per mouse\n  expected:\n  - quantity: whisking fraction, days 1 and 2\n    value: 0.13\n    tolerance: 0.04\n  - quantity: whisking fraction, 5 and 4 days before end\n    value: 0.20\n    tolerance: 0.09\n  - quantity: whisking fraction, final two days\n    value: 0.19\n    tolerance: 0.05\n  criterion: As fig6b-touch-fraction-stable. Reproduced when the three means are within tolerance, the\n    first-against-final test gives p < 0.05 with the final fraction higher, and the middle-against-final\n    test gives p >= 0.05. Partially reproduced when the tests hold and a mean is out of tolerance.\n  depends_on:\n  - fig6b-touch-fraction-stable\n- id: fig6c-no-trimming-expansion\n  statement: After trimming to a single whisker the ratio of touch-neuron fractions inside to outside the\n    principal column did not change (days 0 and 1 1.29 ± 0.31, days 4 and 5 1.55 ± 0.71, days 9 and 10\n    1.31 ± 0.39; early against middle p = 1, early against late p = 0.937, n = 3 mice).\n  source: Results, Imaging during Learning, paragraph 3; Figure 6C\n  quote: We found no change in the ratio of the number of touch neurons (inside-to-outside) following\n    trimming ... early versus middle ... early versus late p = 0.937). Thus, we did not detect enhanced\n    representation of the spared whisker\n  statistics:\n  - about: early against middle\n    p: 1\n    n: 3 mice\n  - about: early against late\n    p: 0.937\n    n: 3 mice\n  expected:\n  - quantity: inside-to-outside touch ratio, days 0 and 1\n    value: 1.29\n    tolerance: 0.31\n  - quantity: inside-to-outside touch ratio, days 4 and 5\n    value: 1.55\n    tolerance: 0.71\n  - quantity: inside-to-outside touch ratio, days 9 and 10\n    value: 1.31\n    tolerance: 0.39\n  criterion: Per session M5 at the 99th percentile on the spared whisker's variables, touch fraction\n    inside the principal column over that outside (M6), days counted from trimming (day 0). The test is\n    not named; it is read as the Wilcoxon rank-sum test of the preceding paragraph, over 6 values per\n    group (3 mice x 2 days). A claim of absence; reproduced when both tests give p >= 0.05 and the three\n    means are within tolerance. Which 3 of the 4 learning mice is not said; all mice imaged at least 10\n    days after trimming are used.\n- id: fig6d-neurometric-flat\n  statement: Discrimination by ensembles of ten individually discriminative L2/3 neurons exceeded\n    behavioral performance even early in training and stayed flat during learning (75% ± 4%, 75% ± 5%,\n    78% ± 5% on first, middle and final two days; p = 0.959, 0.721 and 0.505).\n  source: Results, Imaging during Learning, paragraph 4; Figure 6D\n  quote: Discrimination by small L2/3 ensembles (ten individually discriminative neurons; Experimental\n    Procedures) exceeded behavioral performance (O'Connor et al., 2010b), even during early training\n    (Figure 6D). Neurometric performance remained flat during learning\n  statistics:\n  - about: first two against middle two days\n    p: 0.959\n    n: 4 mice\n  - about: first two against final two days\n    p: 0.721\n    n: 4 mice\n  - about: middle two against final two days\n    p: 0.505\n    n: 4 mice\n  expected:\n  - quantity: neurometric performance, first two days\n    value: 75\n    tolerance: 4\n    unit: percent correct\n  - quantity: neurometric performance, middle two days\n    value: 75\n    tolerance: 5\n    unit: percent correct\n  - quantity: neurometric performance, final two days\n    value: 78\n    tolerance: 5\n    unit: percent correct\n  criterion: Per day and animal, neurons discriminative by M4 that day; 100 groups of ten drawn at\n    random; a naive Bayes decoder with Gaussian classes and zero covariance, 5-fold cross-validation\n    (80% train, 20% test), left against right correct response, hits and errors (Model-Free Analysis,\n    paragraph 3). Open, and able to change the values; the decoder's input per trial is not given\n    (readings are the mean event-trace response over the sample epoch, and over the trial up to the\n    reward cue), and the summary per day is the best group in the Figure 6D legend but not in the\n    Methods (readings are the best of 100 groups, and their mean). The test is not named; read as the\n    Wilcoxon rank-sum test of the preceding paragraphs. Reproduced when, under one reading, the three\n    means are within tolerance, no pair differs at p < 0.05, and the first-two-day neurometric mean\n    exceeds the first-two-day psychometric percent correct.\n  depends_on:\n  - fig6d-psychometric-improves\n- id: fig6d-psychometric-improves\n  statement: Psychometric performance of the learning mice improved from chance (52% ± 2% on the first two\n    days) to criterion levels (66% ± 7% on the final two days).\n  source: Results, Imaging during Learning, paragraph 4; Figure 6D\n  quote: In contrast, psychometric performance improved gradually from chance level to criterion levels\n    over the course of training (first two days\n  expected:\n  - quantity: percent correct, first two days\n    value: 52\n    tolerance: 2\n    unit: percent\n  - quantity: percent correct, final two days\n    value: 66\n    tolerance: 7\n    unit: percent\n  criterion: Percent correct over trials with a response, per session, for the 4 learning mice; the first\n    training day is excluded (Figure 6D legend). Readings for \"first two days\" are training days 2 and 3\n    (first with the full task), and days 1 and 2 of imaging. Reproduced when both means are within\n    tolerance under one reading.\n- id: fig6efg-rfit-vectors-stabilize\n  statement: Individual L2/3 neuron representations stabilized after the first few days of training;\n    population Rfit vectors from early days predicted those of later days poorly, while vectors from\n    later days predicted subsequent days better.\n  source: Results, Imaging during Learning, paragraph 5; Figures 6E to 6G\n  quote: Individual L2/3 neuron representations stabilized after the first few days of training (Figure\n    6E) ... population Rfit vectors from early training days were poor predictors of Rfit vectors on\n    subsequent days (quantified using Pearson's R), whereas the Rfit vectors in later training were\n    better predictors of Rfit vectors of subsequent days\n  criterion: Per session M5 fits, touch (and whisking) Rfit vector over neurons imaged on both days;\n    Pearson r between days for all day pairs (Figure 6G). Which neurons enter the vector is not given;\n    readings are all neurons imaged on both days, and neurons that pass the 99th percentile on either\n    day. Reproduced when, for at least three of four mice under one reading, the mean r of a day with\n    the subsequent days is lower for the first two days than for the days 5 and 4 before the end, for\n    touch.\n- id: fig6h-days-different\n  statement: Relative to the first imaging day 77% ± 26% of subsequent days had distinct touch\n    representations, against 17% ± 33% from 5 days before the final day; for whisking 60% ± 43% fell to\n    33% ± 36% (n = 4 mice).\n  source: Results, Imaging during Learning, paragraphs 6 and 7; Figure 6H\n  quote: Relative to the first day of imaging, 77 % ± 26% (n = 4 mice) of subsequent days were different,\n    whereas 5 days prior to the final training day, only 17% ± 33 % of subsequent days were different\n  expected:\n  - quantity: touch, fraction of subsequent days different from day 1\n    value: 77\n    tolerance: 26\n    unit: percent\n  - quantity: touch, fraction different from 5 days before end\n    value: 17\n    tolerance: 33\n    unit: percent\n  - quantity: whisking, fraction different from day 1\n    value: 60\n    tolerance: 43\n    unit: percent\n  - quantity: whisking, fraction different from 5 days before end\n    value: 33\n    tolerance: 36\n    unit: percent\n  criterion: Each session split trial-wise into two equal, interdigitated pseudo sessions, M5 fit to each,\n    the Rfit vectors correlated; 25 repeats give the intra-day distribution. A later day is distinct when\n    its inter-day r falls below the 5th percentile of the intra-day r of the earlier day (Results,\n    paragraph 6; Figure 6G legend). How 25 different splits arise from interdigitated halves is not\n    said; readings are random assignment of each consecutive pair of trials (one to each half), and\n    random equal halves. Neuron set as in fig6efg-rfit-vectors-stabilize. Reproduced when, under one\n    reading, the touch values are within tolerance and fall from day 1 to 5 days before the end in at\n    least three mice; the whisking values are reported against tolerance.\n  depends_on:\n  - fig6efg-rfit-vectors-stabilize\n- id: fig7-touch-declines-surround\n  statement: The proportion of L2/3 excitatory neurons encoding touch declined by half from the principal\n    column to the surround columns (p = 0.008, Wilcoxon signed rank, n = 8 mice), with a similar profile\n    in L1 (p = 0.031).\n  source: Results, Spatial Organization of Sensory Coding, paragraph 1; Figures 7B and 7C\n  quote: The proportion of L2/3 excitatory neurons encoding touch declined by half when moving from the\n    principal column to the surround columns (Figures 7B and 7C; p = 0.008, Wilcoxon signed rank test,\n    n = 8 mice). A similar spatial profile was observed in L1 (p = 0.031\n  statistics:\n  - about: L2/3 excitatory, principal against surround touch fraction\n    test: Wilcoxon signed rank test\n    p: 0.008\n    n: 8 mice\n  - about: L1, principal against surround touch fraction\n    test: Wilcoxon signed rank test\n    p: 0.031\n  expected:\n    quantity: ratio of surround to principal touch fraction, L2/3 excitatory\n    value: 0.5\n    tolerance: 0.05\n  criterion: Touch fractions per mouse as M5 at the 95th percentile, principal against surround (M6),\n    signed-rank test over mice. The ratio readings are the ratio of means over mice (8.9 / 16.8 = 0.53\n    in the Results) and the mean of per-mouse ratios. Reproduced when both tests give p < 0.05 with the\n    principal fraction higher and the ratio is within tolerance under one reading; partially reproduced\n    when the L2/3 test holds and the L1 test or the ratio does not.\n  depends_on:\n  - fig3d-principal-touch-whisking-equal\n  - fig3d-surround-whisking-dominates\n- id: fig3d-touch-uniform-l5-gaba\n  statement: Touch-encoding L5 neurons and L2/3 GABAergic neurons were equally likely in principal and\n    surround columns (p = 0.383 and p = 0.578).\n  source: Results, Spatial Organization of Sensory Coding, paragraph 1; Figure 3D\n  quote: touch-encoding L5 neurons (p = 0.383) and L2/3 GABAergic neurons (p = 0.578) were equally likely\n    in the center and surround columns\n  statistics:\n  - about: L5\n    test: Wilcoxon signed rank test\n    p: 0.383\n  - about: L2/3 GABAergic\n    test: Wilcoxon signed rank test\n    p: 0.578\n  criterion: A claim of absence, judged on the paper's test, the Wilcoxon signed rank test over mice of\n    principal against surround touch fractions (as for L2/3 in the same paragraph), at p < 0.05.\n    Reproduced when neither test finds a difference; not reproduced when either does. The differences\n    are reported. Mice without neurons of a class in both regions are left out.\n- id: fig7-whisking-uniform\n  statement: Representation of whisking was uniform across neurons inside and outside the principal\n    column, so touch neurons were mainly confined to the principal column while whisking neurons were\n    spread uniformly.\n  source: Results, Spatial Organization of Sensory Coding, paragraph 1; Figure 7C\n  quote: Representation of whisking was uniform across neurons inside and outside the principal column.\n    Thus, touch neurons were primarily confined to the principal column, whereas whisking neurons were\n    distributed uniformly\n  criterion: A claim of absence. The paper gives no test for whisking; the test of the same paragraph is\n    applied, a Wilcoxon signed rank test over 8 mice of principal against surround whisking fractions of\n    L2/3 excitatory neurons (M5), at p < 0.05. Reproduced when it finds no difference; the means (17.0%\n    and 15.0% in the Results) are reported.\n- id: fig7ab-salt-and-pepper\n  statement: Touch and whisking L2/3 neurons are intermingled; the pairwise distances among neurons of a\n    category do not differ from those among all neurons.\n  source: Results, Spatial Organization of Sensory Coding, paragraphs 1 and 3; Figures 7A, 7B and S6\n  quote: We found no difference when comparing the distribution of pairwise distances among neurons of a\n    category (touch, whisking, and mixed) to the pairwise distance distribution among all neurons\n  criterion: Per mouse and category (touch, whisking, mixed), within and outside the principal column,\n    the distribution of pairwise 3D distances among L2/3 excitatory neurons of the category against\n    1,000 random draws of the same number of neurons from all neurons in the same region (Figure S6\n    legend), with a 2.5 to 97.5 percentile envelope. A claim of absence; the paper names no further\n    test, so the claim is reproduced when, for each mouse and category, the category's histogram (10 um\n    bins, a standard choice) leaves the envelope in no more than 5% of bins over the range below 300 um,\n    and not reproduced when it leaves it in a run of three or more bins below 50 um in most mice (the\n    clustering the paper rules out).\n- id: fig4-neuropil-sample-principal\n  statement: The L2/3 neuropil signal was temporally more concentrated in the sample epoch and spatially\n    more concentrated in the principal column than L2/3 somata.\n  source: Results, Spatial Organization of Sensory Coding, paragraph 2; Figures 4C, 4D and S3\n  quote: The neuropil signal was temporally more concentrated in the sample epoch and spatially more\n    concentrated in the principal column\n  criterion: For task-related neuropil ROIs and L2/3 excitatory somata (M3), the fraction of activity\n    peaks in the sample epoch, and the touch fraction (M5) in principal against surround columns.\n    Reproduced when the neuropil exceeds the somata on both, pooled over 8 mice, and in at least six\n    mice for the sample-epoch fraction.\n- id: figs5-l4-neuropil-correlation\n  statement: The touch map of L4 axons correlated best with that of the L2/3 neuropil (r = 0.60), less\n    with L2/3 somata (0.41), and somata with neuropil least (0.36).\n  source: Results, Spatial Organization of Sensory Coding, paragraph 2; Figure S5\n  quote: the correlation between L4 axon and L2/3 neuropil touch maps was highest of the three possible\n    pairings (L4-neuropil Pearson's R\n  expected:\n  - quantity: L4 axon against L2/3 neuropil touch map r\n    value: 0.60\n    tolerance: 0.06\n  - quantity: L4 axon against L2/3 somata touch map r\n    value: 0.41\n    tolerance: 0.041\n  - quantity: L2/3 somata against neuropil touch map r\n    value: 0.36\n    tolerance: 0.036\n  criterion: Arc-row touch fraction maps, 15 x 15 um voxels spanning depth, pooled over mice and folded\n    from four quadrants into one about the principal column centre, with the 99th percentile criterion\n    (Model-Based Encoding Analysis, paragraph 8); Pearson r over voxels present in both maps. Which\n    voxels enter (all, or only those with a minimum ROI count) is not given; readings are all voxels\n    with at least one ROI in both maps, and voxels within one barrel width of the centre. Reproduced\n    when the order L4-neuropil > L4-somata > somata-neuropil holds and the three r are within tolerance\n    under one reading; partially reproduced when the order holds only. Blocked when the data set lacks\n    the L4 axon mice.\n- id: fig8b-direction-tuned\n  statement: Most L2/3 touch neurons were directionally tuned, with about equal numbers preferring\n    protraction and retraction; tuning was typically strong (DI near 1 or -1), and few neurons were\n    intermediate.\n  source: Results, Directional Tuning in vS1, paragraph 2; Figure 8B\n  quote: The majority of L2/3 touch neurons were directionally tuned (Figures 8A and 8B), with an\n    approximately equal number of neurons preferring protraction and retraction. Directional tuning was\n    typically strong ... Relatively few neurons showed an intermediate level of tuning\n  criterion: DI from the curvature nonlinearity f2 of M5, (amplitude at the maximal protraction delta kappa\n    minus amplitude at the maximal retraction delta kappa) over their sum, positive for protraction,\n    protraction being negative delta kappa (Experimental Procedures, paragraph after the encoding\n    model). Open; \"maximal\" delta kappa is read as (a) the most extreme values of the neuron's fitted\n    range (end knots), and (b) the extreme 1st and 99th percentiles of touch delta kappa. Touch neurons\n    at the 95th percentile. Reproduced when, under one reading, more than half have |DI| > 0.5, the\n    protraction share of tuned neurons is between 40% and 60%, and |DI| between 0.25 and 0.75 holds\n    fewer neurons than |DI| > 0.75.\n- id: figs7-direction-stable\n  statement: L2/3 directional tuning was stable during learning; the mean pairwise RMS difference of touch\n    receptive fields across days (0.273, n = 118 neurons) was below the 5th percentile of the shuffled\n    distribution (0.425) for 97.8% of neurons.\n  source: Results, Directional Tuning in vS1, paragraph 2; Figure S7\n  quote: The difference between touch receptive fields among days (grand mean of RMS difference\n    0.273; n = 118 neurons) was below the 5th percentile of the shuffled distribution (0.425; shuffling\n    by neuron identity) for 97.8% of the neurons examined\n  expected:\n  - quantity: grand mean RMS difference\n    value: 0.273\n    tolerance: 0.0273\n  - quantity: 5th percentile of shuffled RMS\n    value: 0.425\n    tolerance: 0.0425\n  - quantity: neurons below the shuffled 5th percentile\n    value: 97.8\n    tolerance: 2.2\n    unit: percent\n  - quantity: neurons examined\n    value: 118\n    tolerance: 12\n  criterion: Learning mice, per-session M5 fits; touch neurons at the 99th percentile with touch Rfit >\n    0.25 (Model-Based Encoding Analysis, last paragraph); per neuron the mean RMS over all pairs of days\n    on which it is a touch cell of the curvature nonlinearities (0..1). Open; the shuffle by neuron\n    identity pairs a neuron's curve on one day with another neuron's on another; readings are a null\n    over random neuron pairs on the same day pairs, and over random neuron pairs on any days. The\n    nonlinearities must be compared on a common delta kappa grid; the tent knots are used. The\n    percentage tolerance is bounded at 100%. Reproduced when, under one reading, all four values are\n    within tolerance; partially reproduced when the share below the null is above 90% only.\n- id: fig8de-direction-topography\n  statement: Protraction-preferring touch neurons were more abundant in and near the column of the whisker\n    anterior to the spared one, retraction-preferring neurons in and near the column of the posterior\n    whisker, giving a trend in DI along the whisker row.\n  source: Results, Directional Tuning in vS1, paragraph 3; Figures 8C to 8E\n  quote: neurons sensitive to protraction touch were more abundant in and near the barrel column of the\n    whisker anterior to the spared one, with retraction-sensitive neurons more abundant in and near the\n    column of the whisker posterior to the spared one\n  statistics:\n  - test: Pearson correlation, linear fit of binned DI against row position\n    p: 0.05\n    p_relation: \"<\"\n  criterion: Touch neurons at the 99th percentile (Experimental Procedures), DI as fig8b-direction-tuned,\n    averaged in 45 um bins along the row axis, positive toward anterior whiskers (Figure 8E legend);\n    Pearson r of bin means against position, pooled over 7 mice (Figure 8D legend). The r and p are\n    printed only in the figure, which was not read, so p < 0.05 is the bound taken as the paper's\n    finding of a trend. Reproduced when r > 0 with p < 0.05. The row axis and the principal column\n    centre must come from the data set (M6); if absent, the claim is blocked.\n  depends_on:\n  - fig8b-direction-tuned\n- id: results-di-magnitude-similar\n  statement: DI magnitudes inside and outside the principal column were similar (p = 0.333, Wilcoxon\n    rank-sum), so the spatial trend reflects a change in preference among neurons of similar tuning\n    strength.\n  source: Results, Directional Tuning in vS1, paragraph 3\n  quote: DI magnitudes inside and outside the principal column were similar (p = 0.333, Wilcoxon rank-sum\n    test\n  statistics:\n  - test: Wilcoxon rank-sum test\n    p: 0.333\n  criterion: A claim of absence, judged on the paper's test, a Wilcoxon rank-sum test of |DI| of touch\n    neurons inside against outside the principal column (neurons pooled over mice, as a rank-sum on\n    neurons), at p < 0.05. Reproduced when it finds no difference; the medians are reported.\n  depends_on:\n  - fig8de-direction-topography\n- id: fig8e-l4-neuropil-direction-map\n  statement: L4 axons and the L2/3 neuropil show a directional map along the row similar to that of L2/3\n    excitatory neurons, so the L2/3 directional topography is likely inherited from L4.\n  source: Results, Directional Tuning in vS1, paragraph 4; Figure 8E\n  quote: we observed a directional map, similar to that observed in L2/3 excitatory neurons, in the\n    activity of both L4 axons and the L2/3 neuropil\n  criterion: As fig8de-direction-topography, for L4 axon ROIs and L2/3 neuropil ROIs. Reproduced when both\n    give r > 0 with p < 0.05; partially reproduced when one does. Blocked for L4 when the data set lacks\n    the L4 axon mice.\n  depends_on:\n  - fig8de-direction-topography\n- id: fig8h-passive-active-overlap\n  statement: Different neurons encode passive deflection and active touch; only 8% of neurons with touch\n    responses under anesthesia also responded to touch during behavior, with 6.5% expected by chance (n\n    = 3 mice).\n  source: Results, Directional Tuning in vS1, paragraph 6; Figures 8G and 8H\n  quote: Surprisingly, only 8% of neurons showing touch responses under anesthesia showed touch responses\n    during behavior, with 6.5% expected by chance\n  expected:\n  - quantity: fraction of passive-responsive neurons also touch-responsive in behavior\n    value: 8\n    tolerance: 0.8\n    unit: percent\n  - quantity: chance overlap\n    value: 6.5\n    tolerance: 0.65\n    unit: percent\n  criterion: Passive responders are ROIs whose trial-locked mean response exceeds the 95th percentile of an\n    event-shuffled null and whose event rate exceeds 0.01 Hz (Experimental Procedures, last paragraph of\n    Model-Based Encoding Analysis); active touch neurons by M5 at the 95th percentile. Chance is read as\n    the active touch fraction among all ROIs imaged in both conditions. The response window is not given;\n    readings are the 1 s and 2 s after deflection onset. Reproduced when, under one reading, both values\n    are within tolerance. Blocked when the data set lacks the anesthetized mice.\n- id: fig8i-no-anesthetized-topography\n  statement: Under anesthesia, neurons showed no detectable topography of directional tuning.\n  source: Results, Directional Tuning in vS1, paragraph 6; Figure 8I\n  quote: we did not detect topography in directional tuning for neurons in anesthetized mice\n  criterion: A claim of absence. DI under anesthesia, (R - F) / (R + F) of peak dF/F to rearward and forward\n    deflection for responsive ROIs (as fig8h-passive-active-overlap), averaged in 45 um bins along the row\n    as in Figure 8E; the paper's test is the Pearson correlation of the linear fit (Figure 8I as 8E).\n    Reproduced when p >= 0.05; the r is reported.\n  depends_on:\n  - fig8h-passive-active-overlap\n- id: fig8jk-neuropil-anesthetized\n  statement: The neuropil remained direction selective under anesthesia, with forward deflection evoking\n    responses in and near the column of the whisker anterior to the deflected one, as in anesthetized rats;\n    this is the same spatial map as active protraction touch but with opposite lateral force.\n  source: Results, Directional Tuning in vS1, paragraphs 5 and 7; Figures 8F, 8J and 8K\n  quote: The neuropil signal was still direction selective under anesthesia (Figure 8J). Moreover, the\n    topography of neuropil directionality under anesthesia was consistent with that observed in\n    anesthetized rats (Kremer et al., 2011\n  criterion: As fig8i-no-anesthetized-topography for neuropil ROIs, with DI defined so that forward\n    preference is positive in the anterior direction of the row axis. Reproduced when the binned DI\n    against row position has p < 0.05 with forward preference toward anterior columns, and the\n    fraction of responsive neuropil ROIs with |DI| > 0.5 exceeds half.\n  depends_on:\n  - fig8h-passive-active-overlap\n- id: figs3d-neuropil-correction\n  statement: Without peri-somatic neuropil correction more neurons are classed as touch; the corrected\n    fraction is consistent with electrophysiology.\n  source: Figure S3D\n  quote: Touch fraction among neurons without peri-somatic neuropil correction (above) and with correction\n    (below). The bottom plot is consistent with electrophysiological results\n  criterion: Neuropil correction F_ROI - 1.0 x F_neuropil (annulus 3 to 13 um from the ROI edge, excluding\n    pixels with neighbour correlation above 0.2 and ROI pixels), clipped at baseline; F0 over a 3 min\n    window at a skew-dependent percentile (Calcium Imaging Analysis, step 4). The skew to percentile map\n    is not given; readings are the 5th percentile for all and the median for all. Touch fraction by M5\n    on dF/F from uncorrected and corrected traces, with events re-extracted only if the data set does\n    not hold uncorrected events. Reproduced when the uncorrected touch fraction exceeds the corrected\n    one for L2/3 excitatory neurons pooled and in at least six mice. Blocked when the data set holds\n    neither raw ROI and neuropil fluorescence nor uncorrected events.\n- id: discussion-correlation-more-touch\n  statement: A correlation-based classification of the same data classifies a larger proportion of neurons\n    as touch than the encoding model.\n  source: Discussion, paragraph 5\n  quote: Applying a correlation-based approach to our data set classifies a larger proportion of neurons as\n    touch\n  criterion: The correlation-based approach is not specified. Readings are the Pearson r of each neuron's\n    dF/F with the curvature change (absolute, downsampled to 7 Hz) above the 95th percentile of the same\n    r on the event-shuffled traces of M5, and the r with a binary touch trace convolved with the\n    neuron's events' decay. Reproduced when, under one reading, the correlation touch fraction of L2/3\n    excitatory neurons exceeds the M5 touch fraction pooled and in at least six mice.\n  depends_on:\n  - fig3d-principal-touch-whisking-equal\n- id: methods-event-detection\n  statement: On simultaneous imaging and cell-attached data from mouse visual cortex, degraded to this\n    study's dwell time and rate, the event detector found 54% ± 10% of single action potentials at a\n    false positive rate of 0.01 Hz (n = 7 neurons).\n  source: Experimental Procedures, Calcium Imaging Analysis, paragraph after step 5\n  quote: For a false-positive detection rate of 0.01 Hz, 54% ± 10% of single action potentials (mean ±\n    SD; n = 7 neurons) were detected\n  data: elsewhere\n  where: Simultaneous imaging and cell-attached data of Chen et al. (2013b), Nature 499:295-300, as the\n    paper cites them; the paper names no archive or identifier\n  expected:\n    quantity: single action potentials detected at 0.01 Hz false positives\n    value: 54\n    tolerance: 10\n    unit: percent\n  criterion: The detector as Calcium Imaging Analysis step 5 (template bank of rise 3 to 5 frames, decay 7\n    to 35 frames; candidates from large second derivatives; noise sigma from a Savitzky-Golay residual;\n    accept when RMS difference < sigma and mean amplitude > sigma; peel and repeat). The degradation to\n    the volume-imaging dwell time, the Savitzky-Golay window and the detection matching window are not\n    given; this claim is outside the data set and is listed for completeness.\n"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
python tools/claims_check.py claims/peron-2015.yaml paper/10.1016-j.neuron.2015.03.027.txt
```

Result: not kept, because it reads the paper's text.

**Agent**

Four quotes miss: three because I dropped colons the text has, one because the text prints "retractionsensitive". Fixing them.

**Agent calls Bash**

```bash
python - <<'EOF'
p='claims/peron-2015.yaml'
s=open(p).read()
rep=[("""  quote: After trimming all whiskers, performance fell to chance level (d-prime -0.03 ± 0.11, mean ±
    S.D., n=4 mice), confirming that mice used tactile cues to solve the task""",
"""  quote: After trimming all whiskers, performance fell to chance level ... 0.11, mean ± S.D., n=4 mice),
    confirming that mice used tactile cues to solve the task"""),
("""    end of training (Figure 6B) ... final two days 0.15 ± 0.07; first two versus final two p = 1 ...""",
"""    end of training (Figure 6B) ... 0.15 ± 0.07; first two versus final two p = 1 ..."""),
("""  quote: The difference between touch receptive fields among days (grand mean of RMS difference
    0.273; n = 118 neurons) was below""",
"""  quote: The difference between touch receptive fields among days (grand mean of RMS difference ...
    0.273; n = 118 neurons) was below"""),
("""    whisker anterior to the spared one, with retraction-sensitive neurons more abundant in and near the""",
"""    whisker anterior to the spared one, with retractionsensitive neurons more abundant in and near the"""),
]
for a,b in rep:
    assert a in s, a[:40]
    s=s.replace(a,b)
open(p,'w').write(s)
EOF
python tools/claims_check.py claims/peron-2015.yaml paper/10.1016-j.neuron.2015.03.027.txt
```

Result: not kept, because it reads the paper's text.

**Agent**

All quotes pass. I'll remove one statistics entry: on fig8de I recorded p < 0.05, but the paper prints that p only inside the figure, which I couldn't read. Then I'll run the style checks.

**Agent calls Bash**

```bash
python - <<'EOF'
p='claims/peron-2015.yaml'
s=open(p).read()
a="""  statistics:
  - test: Pearson correlation, linear fit of binned DI against row position
    p: 0.05
    p_relation: "<"
  criterion: Touch neurons at the 99th"""
assert a in s
s=s.replace(a,"  criterion: Touch neurons at the 99th")
open(p,'w').write(s)
EOF
grep -n "—\|rather" claims/peron-2015.yaml; python tools/claims_check.py claims/peron-2015.yaml paper/10.1016-j.neuron.2015.03.027.txt
python - <<'EOF'
import yaml
d=yaml.safe_load(open('claims/peron-2015.yaml'))
c=d['claims']
print(len(c), sum('quote' in x for x in c), sum('statistics' in x for x in c), sum(len(x.get('statistics',[])) for x in c), sum('criterion' in x for x in c), sum('expected' in x for x in c))
EOF
```

Result: not kept, because it reads the paper's text.

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/peron-2015.yaml",
 "old_string": "# Mice reaching criterion are \"n = 8 mice\" in the Results, while Figure 1E legend marks some mice as\n# not imaged during training. The Experimental",
 "new_string": "# The Experimental"
}
```

```
The file claims/peron-2015.yaml has been updated successfully. (note: the file had been modified on disk since you last read it — the edit applied cleanly, but the file contains other changes not in your context. Read it before edits that depend on surrounding content.)
```

**Agent calls Bash**

```bash
python tools/claims_check.py claims/peron-2015.yaml paper/10.1016-j.neuron.2015.03.027.txt; git status --short
```

Result: not kept, because it reads the paper's text.

**Agent**

I wrote `claims/peron-2015.yaml` with 43 claims, and the checker passes: 42 quotes found word for word, 18 statistical values, 0 problems.

**Text read:** the version of record with its full Supplemental Information (Figures S1 to S7 legends, Table S1, Supplemental Experimental Procedures), from `paper/10.1016-j.neuron.2015.03.027.txt`. The paper links no analysis code. It names only ScanImage, the Janelia Whisker Tracker, BControl and an unnamed MATLAB package, and none of these settles an analysis choice. I could not render the PDF here (no renderer was available and installing one failed). So numbers printed only inside the figures were not read, and no claim rests on them: the per-population percentages of Figure 3 and the Pearson r and p of Figures 8E, 8I and 8K.

**Counts:**
- 43 claims, 42 with quotes. The one without is `table-s1-roi-counts`, marked `inferred` because Table S1 has no sentence stating it.
- 10 claims carry 18 statistics entries.
- 41 have criteria and 27 have expected values.
- One claim, the event-detector validation, uses data from elsewhere: the Chen et al. 2013b recordings, for which the paper gives no archive. All others use the dataset.
- The dataset description mentions the eight volume-imaging mice. Whether it also holds the learning mice, L4 axon mice, anesthetized mice, L5 soma–dendrite pairs, high-resolution stacks and column outlines is left for the author to find.

**Details the paper leaves open, with the readings named.** Shared methods M1 to M7 are in the opening comment.
- **Task-related test:** the time bin (one 7 Hz frame), and whether events are shuffled within each trial or across the session.
- **Trial-type discrimination:** whether the trial itself is left out of the mean PSTH (in or out).
- **Encoding model:**
  - penalty scale: one value chosen by cross-validation on a random subset of ROIs, or one per neuron;
  - tent knots: equally spaced over the variable's range, or at its quantiles;
  - kernel lags: causal, or centred on zero;
  - frames entering the fit: all imaged frames, or trial frames only.
- **Summaries:** mean of per-mouse fractions or fractions pooled over mice; ± read as SD, with SEM as a variant.
- **Whisking amplitude:** range over the trial, range over the sample epoch, or peak Hilbert amplitude.
- **Days to criterion:** day 1 counted from the first training day, or from the first day of the full task.
- **Learning statistics:** the rank-sum test over 8 day values per group, with per-mouse means as a variant. For the trimming and neurometric tests, which the paper does not name, I read them as rank-sum tests.
- **Neurometric decoder:** its input (sample epoch, or up to the reward cue); the score per day (best of 100 groups, or their mean).
- **Pseudo-session splits:** random pairs of consecutive trials, or random halves. Rfit-vector neuron set: all neurons imaged on both days, or those passing on either day.
- **Directionality index:** "maximal" curvature change read as the end knots, or the 1st and 99th percentiles.
- **Tuning-stability shuffle:** a null of random neuron pairs on the same day pairs, or on any days.
- **Map voxels entering the L4 and neuropil correlations:** all shared voxels, or those within one barrel width of the centre.
- **Anesthetized response window:** 1 s or 2 s after deflection.
- **F0 percentile by skew:** 5th percentile for all, or the median for all.
- **The Discussion's "correlation-based approach":** two possible definitions, given in the claim.
- **Other open details:**
  - the mouse sets behind the "n = 5 volumes" and the "3 trimmed mice";
  - the nucleus-matching parameters for the fraction of neurons imaged (that claim is blocked as underspecified unless the dataset carries the nuclei counts);
  - the clustering threshold for the pairwise-distance test (the paper names no test, so a threshold is set in that claim).

**Missing or inconsistent in the paper:**
- The p-values for several tests are given without the test named (surround whisking against touch, the L5 and GABAergic comparisons, trimming, neurometric). I read them as the test of the neighbouring sentence and said so in each claim.
- The r and p for the directional maps are printed only in the figures, which I could not read.
- Apical dendrite counts disagree: 2,469 in the Results, 2,496 in Figure 3. The claim accepts either.
- Principal and surround column labels and the row axis are needed by many claims; without them in the dataset those claims are blocked.

As instructed, I committed nothing.

## End of run

27 turns, 6 minutes, $2.06 at API prices, result: success.
