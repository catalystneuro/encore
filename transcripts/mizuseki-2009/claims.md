# mizuseki-2009 · claims · run 42691760728

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cat docs/protocol.md | sed -n '/Reader/,$p' | head -300; ls paper/; ls claims | head; wc -l paper/*
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
head -60 paper/10.1016-j.neuron.2009.08.037.txt; grep -n -i "supplement\|Figure S\|Table S" paper/10.1016-j.neuron.2009.08.037.txt | head -80
```

Result: not kept, because it reads the paper's text.

**Agent**

Full text with supplement is present. Let me read it.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1016-j.neuron.2009.08.037.txt",
 "offset": 60,
 "limit": 740
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "claims/fouke-2025.yaml"
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

**Agent calls Read**

```json
{
 "file_path": "paper/10.1016-j.neuron.2009.08.037.txt",
 "offset": 1030,
 "limit": 900
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
head -40 paper/hc-2.data-description.txt; ls claims | wc -l; grep -l "crcns" claims/*.yaml | head; cat papers/datasets/mizuseki-2009.yaml 2>/dev/null
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
head -40 claims/henze-2000.yaml; ls schemas 2>/dev/null; ls docs; grep -rn "code:" claims/*.yaml | head -5
```

```
# Claims for Henze, Borhegyi, Csicsvari, Mamiya, Harris & Buzsaki (2000), J Neurophysiol 84:390-400,
# "Intracellular Features Predicted by Extracellular Recordings in the Hippocampus In Vivo",
# doi:10.1152/jn.2000.84.1.390, on CRCNS data set hc-1 (doi:10.6080/K02Z13FP).
# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"), 2026-11-08,
# protocol as stated in docs/protocol.md (Reader), version pilot-13.
#
# Text read: the version of record, as supplied under paper/ (PyMuPDF text of the journal PDF):
# Introduction, Methods, Results, Discussion and the legends of Figures 1 to 8. The paper has no
# supplement and links no analysis code, so no code was read. The PDF could not be rendered here
# (no renderer installed), so values printed only inside figures were not read. The extracted
# text prints the signs =, <, >, plus/minus and "approximately" as a replacement character; they
# were read from the PDF's content streams, where they are glyphs of the Universal-GreekwithMathPi
# font ("5" is =, "6" is plus/minus, "," is <, "." is >, ";" is approx.) and of
# MathematicalPi-One ("#" is less or equal, "$" is greater or equal). So: start 0.01 +/- 0.02 (SD)
# ms and end 0.02 +/- 0.14 ms earlier; durations 1.28 +/- 0.18 and 1.27 +/- 0.19 ms; "R = 0.66,
# P < 0.03"; negative peak 0.20 +/- 0.08 ms before the intracellular peak; Fig. 4D "R = 0.40;
# P < 0.0001"; Fig. 4D bursts at approx. 200 Hz with "< 5-ms inter-spike intervals"; Fig. 4A to C
# first interspike interval approx. 10 ms; Fig. 5 "n = 202" pyramidal cells and "n = 43"
# interneurons, "P < 0.001" and "P < 0.003" in the legend, "P < 0.003" in the Results; largest
# spikes recorded "< 50 um" from the soma; small spikes "< 60 uV" at "> 50 um"; nothing at
[... 41 more lines not kept]
```

**Agent calls Bash**

```bash
python -c "import json;d=json.load(open('schemas/claims.schema.json'));print(json.dumps(d,indent=1)[:6000])"; sed -n 40,80p claims/henze-2000.yaml
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
[... 222 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 1,80p claims/fedele-2017.yaml; python -c "import json;d=json.load(open('schemas/claims.schema.json'));print(json.dumps(d['\$defs'],indent=1)); print(list(d['properties']))"
```

```
# Claims for Fedele, Burnos, Boran, Krayenbuehl, Hilfiker, Grunwald & Sarnthein (2017),
# Scientific Reports 7, 13836, on CRCNS ieeg-1.
# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"),
# 2026-11-09, protocol pilot-14 as stated in docs/protocol.md.
#
# Text read: the version of record (PMC5653833, Europe PMC JATS XML flattened), main text,
# Tables 1 and 2, figure legends and Methods, and the supplement (41598_2017_13064_MOESM1_ESM.pdf,
# from the publisher), which holds only Table S1. The text of Table S1 keeps the channel names
# and rates but loses its colours; the PDF page was rendered to read them: channels excluded
# from the analysis are filled gray, resected channels (RA) red, and the HFO area of each HFO
# type green, cell by cell in the Ripples, FR and FRandR rows. The colours are vector fills in
# the PDF and can be read programmatically. The CRCNS data description (paper/ieeg-1.data-
# description.txt) was read for the layout of the deposit only; no claim is taken from it.
#
# Code: the Methods link https://github.com/HFO-detect/HFO-detect-matlab, read at commit
# f39736734031c9e37e0b101536be8d8be35906db (2017-07-14). It holds the HFO detectors only: the
# morphology detector of Burnos et al. 2016 (hfo-detect-toolbox/Morphology Detector, with
# Filter_AsBurnos2016.mat, the Stockwell transform st.m, and the detector parameters in
# func_prepareMorphologyDetector.m: minimum duration 0.02 s for ripples and 0.01 s for FR, as
# the Methods say; filtering with filtfilt), plus line-length and RMS detectors. The function
[... 163 more lines not kept]
```

**Agent**

Full text and supplement are present; the paper links no code. Next I'll read the figure numbers (Fig. 3D, Fig. 7, Table S1) from the PDF.

**Agent calls Bash**

```bash
cd $TMPDIR && python -c "
import fitz
d=fitz.open('paper/10.1016-j.neuron.2009.08.037.pdf')
for i in [3,5,6,8]:
    d[i].get_pixmap(dpi=150).save(f'm{i+1}.png')
s=fitz.open('paper/10.1016-j.neuron.2009.08.037.supp.pdf')
print(len(s))
for i in [8,9,15,17]:
    s[i].get_pixmap(dpi=130).save(f's{i+1}.png')
" && ls
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
which pdftoppm mutool gs convert magick; python -c "import pypdfium2" 2>&1; python -c "import pdfplumber" 2>&1; ls .venv 2>/dev/null | head; uv --version 2>&1
```

```
Traceback (most recent call last):
  File "<string>", line 1, in <module>
    import pypdfium2
ModuleNotFoundError: No module named 'pypdfium2'
Traceback (most recent call last):
  File "<string>", line 1, in <module>
    import pdfplumber
ModuleNotFoundError: No module named 'pdfplumber'
uv 0.13.7 (x86_64-unknown-linux-gnu)
```

**Agent calls Bash**

```bash
cd $TMPDIR && uv run --no-project --with pymupdf python -c "
import fitz
d=fitz.open('paper/10.1016-j.neuron.2009.08.037.pdf')
for i in [3,6,8]:
    d[i].get_pixmap(dpi=160).save(f'm{i+1}.png')
s=fitz.open('paper/10.1016-j.neuron.2009.08.037.supp.pdf')
print(len(s))
for i in [8,9]:
    s[i].get_pixmap(dpi=130).save(f's{i+1}.png')
" 2>&1 | tail -3; ls $TMPDIR
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/m4.png"
}
```

Result: no output.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/m9.png"
}
```

Result: no output.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/s10.png"
}
```

Result: no output.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/s9.png"
}
```

Result: no output.

**Agent**

Table S1 and Fig. 7 numbers are legible. Zooming on Fig. 3D/H and Fig. 4 to read the significance marks and arrows.

**Agent calls Bash**

```bash
cd $TMPDIR && uv run --no-project --with pymupdf python -c "
import pymupdf as fitz
d=fitz.open('paper/10.1016-j.neuron.2009.08.037.pdf')
p=d[3]; r=p.rect
clip=fitz.Rect(r.width*0.8,r.height*0.12,r.width*0.97,r.height*0.5)
p.get_pixmap(dpi=400,clip=clip).save('f3d.png')
d[5].get_pixmap(dpi=170).save('m6.png')
d[6].get_pixmap(dpi=150).save('m7.png')
" 2>&1 | grep -v Warn
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/f3d.png"
}
```

Result: no output.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/m6.png"
}
```

Result: no output.

**Agent calls Bash**

```bash
sed -n 40,140p paper/hc-2.data-description.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -n 1,80p tools/claims_check.py
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

[... 61 more lines not kept]
```

**Agent**

Now writing the claims file.

**Agent calls Write**

```json
{
 "file_path": "claims/mizuseki-2009.yaml",
 "content": "# Claims for Mizuseki, Sirota, Pastalkova & Buzsaki (2009), Neuron 64, 267-280, \"Theta Oscillations\n# Provide Temporal Windows for Local Circuit Computation in the Entorhinal-Hippocampal Loop\",\n# doi:10.1016/j.neuron.2009.08.037, on CRCNS data set hc-2.\n# Written by an agent (model \"claude-opus-5-5\", Claude Code, runner \"GitHub Actions\"), 2026-11-09,\n# protocol as stated in docs/protocol.md (Reader).\n#\n# Text read: the version of record with its supplement (Supplemental Data, 678d1873-mmc1_1.pdf),\n# as supplied under paper/ (PyMuPDF text): main text, figure legends, the short Experimental\n# Procedures, the Supplemental Experimental Procedures, Table S1 and the legends of Figures S1 to\n# S19. The text prints degree signs, minus signs and \"approximately\" as a replacement character;\n# those values were read from the PDF. Table S1 is an image in the supplement and was read from\n# the rendered page. Figure 3D and 3H (significance marks), Figure 4 (arrows) and Figure 7 (the\n# percentages and n above each panel) were read from the rendered pages. The CRCNS data\n# description (paper/hc-2.data-description.txt) was read for the layout of the deposit only; no\n# claim comes from it.\n#\n# Code: the paper links no code. Its analyses were \"carried out by custom-written MATLAB-based\n# software\" (Supplemental Experimental Procedures), not published with it. Every method below\n# comes from the paper and its supplement alone.\n#\n# Data the paper used (Results paragraph 1, Supplemental Experimental Procedures, Table S1).\n# Five male Long-Evans rats (ec12, ec13, ec14, ec16, i01), a 4-shank silicon probe in the right\n# dorsocaudal medial entorhinal cortex (EC), moved between sessions over 4 to 12 weeks, and in\n# four rats a second probe (4 or 8 shanks) in the right dorsal hippocampus, in the CA1 or CA3\n# pyramidal layer or the dentate gyrus (DG) granule cell layer; rat ec12 had no hippocampal probe,\n# and in rat i01 the EC layers could not be verified by histology (i01 theta reference is CA1).\n# Tasks: linear track (250 cm), open field (\"square\", 180 x 180 or 120 x 120 cm, chasing water or\n# Froot Loops), T-maze alternation with wheel-running delay, rewarded wheel running. Wideband\n# signal at 20 kHz, LFP at 1250 Hz, position from two head LEDs at 30 Hz. Units sorted with\n# KlustaKwik and Klusters; sessions on different days clustered separately, so a neuron may be\n# counted more than once; neurons tested in several sessions were analysed session by session\n# (Table S1 legend). Cells per Table S1: EC 2744 (EC2 569, EC3 820, EC5 723, layer unknown 632,\n# excluded), CA1 3864 (3270 principal, 464 interneurons), CA3 876, DG 175. EC layers EC1 to EC5\n# (EC5 covers EC5 and EC6) from sharp-wave and theta reversals and histology (Figure 1, S1).\n# Measured variables: spike times and waveforms per unit, LFP per site, position, task.\n#\n# The CRCNS data set hc-2, by its title and description, is meant to hold recordings of this\n# study. Whether it holds the EC recordings, the hippocampal recordings of every rat, the tasks\n# other than the open field, the cell-type and layer labels, and the theta epochs, is for the\n# author to find. Many claims below need EC or CA3/DG neurons, or tasks, that it may not hold.\n#\n# Methods fixed by the paper and used by several claims (Supplemental Experimental Procedures,\n# unless another place is cited):\n# - Theta epochs: ratio of power in the 5-11 Hz band to the 1-4 and 12-14 Hz bands of EC3 LFP,\n#   with manual adjustment; walking/running epochs only.\n# - Theta phase: LFP filtered 5-11 Hz (Figure S9 legend); peaks found as positive-to-negative\n#   zero crossings of dy/dt, phase linearly interpolated between peaks, peak = 0 and 360 degrees,\n#   trough = 180 (the \"maxima method\", used in all figures but S9). Reference LFP is EC3 unless\n#   stated (Results, Physiological identification of EC layers; Figure S10 uses CA1 pyramidal).\n# - Single-cell theta modulation: units with at least 50 spikes and rate > 0.1 Hz in theta epochs;\n#   Rayleigh test, p < 0.01; preferred phase = circular mean, modulation depth = mean resultant\n#   length R.\n# - Cell types: hippocampal principal cells and interneurons from autocorrelograms, waveforms and\n#   rates; EC types from monosynaptic interactions (jitter test, [-5, 5] ms, 1000 surrogates, 99%\n#   global bands over [-20, 20] ms, significant bins at [1, 5] ms) and a hyperplane on\n#   trough-to-peak latency and waveform asymmetry (Figure 2C).\n# - Instantaneous rate of a spike: the number of the neuron's spikes in a 250 ms window centred\n#   on it, in categories 1 to >= 10 spikes (4 to >= 40 Hz). Burst spikes: an ISI before or after\n#   < 6 ms; single spikes: both ISIs > 20 ms.\n# - Pair cross-correlograms over [-200, 200] ms, normalised by (1 - |t|/T) for segment length T.\n#   Group CCGs: summed counts, Gaussian smoothing SD 5 ms, jitter +/-125 ms, 99.9% global band\n#   over [-150, 150] ms, significant bins at p < 0.001. Pair offsets: CCG smoothed SD 10 ms,\n#   1000 jitter surrogates (+/-125 ms), 95% global band over [-150, 150] ms; a pair is\n#   significant when its peak is outside the band and the smoothed CCG has more than 100 events\n#   in [-150, 150] ms; the offset is the peak time in [-150, 150] ms; offset histogram in 5 ms\n#   bins smoothed with [0.25, 0.5, 0.25], 95% global band against a uniform distribution.\n# - Linear track place fields: 5 cm bins per direction, no smoothing; a field is a run of at\n#   least 3 bins above 10% of the track peak, extended until the rate rises again or falls below\n#   1% of peak; fields with fewer than 50 spikes or including a turn are dropped; spatial\n#   coherence is the correlation of each bin's rate with its neighbours' rates (Hafting et al.,\n#   2008); phase precession only in fields with coherence > 0.7, by rotating phase in 1 degree\n#   steps and taking the phase-position correlation at the rotation with the largest R2.\n#\n# Open details shared by several claims, with the readings the paper allows:\n# - (O1) \"Neighbouring bins\" in spatial coherence: (a) the two adjacent bins, (b) the mean of\n#   the two adjacent bins correlated with each bin. Hafting et al. (2008), which the paper\n#   cites, is the source; the author follows it if it settles the point.\n# - (O2) How a session's units that recur in several sessions are counted: (a) session by\n#   session, as the Table S1 legend says the paper did; (b) once per unit. Reading (a) is the\n#   paper's and decides; (b) is a variant.\n# - (O3) Filter used for 5-11 Hz theta: not named; a zero-phase band-pass filter is the\n#   standard choice and cannot move peak times by more than a few degrees.\n# - (O4) For the open-field and task splits, what counts as a session of a task is the\n#   session's task label.\nschema_version: 2\npaper: doi:10.1016/j.neuron.2009.08.037\nclaims:\n- id: tables1-cell-counts\n  statement: The study recorded 2744 EC neurons (EC2 569, EC3 820, EC5 723, and 632 of unknown\n    layer that were excluded) and 3864 CA1, 876 CA3 and 175 DG neurons; CA1 held 3270 principal\n    cells and 464 interneurons, of which ec13 gave 940 and 205, ec14 832 and 80, ec16 528 and 44,\n    and i01 970 and 135; 1083 CA1 principal cells and 188 CA1 interneurons were tested in the open\n    field.\n  source: Table S1\n  inferred: Numbers only in Table S1, an image in the supplement read from the rendered page; no\n    sentence states them. The sessions-by-task counts count a neuron once per task.\n  expected:\n  - quantity: EC neurons, total\n    value: 2744\n    tolerance: 274\n  - quantity: CA1 neurons, total\n    value: 3864\n    tolerance: 386\n  - quantity: CA1 principal cells\n    value: 3270\n    tolerance: 327\n  - quantity: CA1 interneurons\n    value: 464\n    tolerance: 46\n  - quantity: CA1 principal cells, rat ec13\n    value: 940\n    tolerance: 94\n  - quantity: CA1 principal cells, rat ec14\n    value: 832\n    tolerance: 83\n  - quantity: CA1 principal cells, rat ec16\n    value: 528\n    tolerance: 53\n  - quantity: CA1 interneurons, rat ec13\n    value: 205\n    tolerance: 20\n  - quantity: CA1 interneurons, rat ec14\n    value: 80\n    tolerance: 8\n  - quantity: CA1 interneurons, rat ec16\n    value: 44\n    tolerance: 4\n  - quantity: CA1 principal cells tested in the open field (square)\n    value: 1083\n    tolerance: 108\n  - quantity: CA1 interneurons tested in the open field (square)\n    value: 188\n    tolerance: 19\n  criterion: Counts of well-isolated units (cluster index 2 and above) per region, cell type and\n    rat, counted session by session as the Table S1 legend says (O2, reading a), with once per\n    unit as a variant. Each count present in the dataset is compared on its own; counts for\n    regions, rats or tasks the dataset does not hold are reported as not testable. The open-field\n    counts are the \"square\" column of Table S1.\n- id: fig2c-ec-cell-classes\n  statement: About 30% of EC neurons (820 of 2744) were identified as excitatory or inhibitory by\n    monosynaptic interactions; with waveform asymmetry and trough-to-peak latency, 2047 (74.6%)\n    were classed as putative principal cells and 590 (21.5%) as putative interneurons.\n  source: Results, Physiological identification of entorhinal neuron types, paragraph 1; Figure 2C\n  quote: Approximately 30% of EC neurons were identified physiologically by their monosynaptic\n    interactions (820 out of 2744 neurons in five rats) ... the majority of the EC neurons were\n    classified as putative principal cells (2047 neurons, 74.6%\n  expected:\n  - quantity: fraction of EC neurons identified by monosynaptic interactions\n    value: 0.30\n    tolerance: 0.03\n  - quantity: fraction of EC neurons classed as putative principal cells\n    value: 0.746\n    tolerance: 0.075\n  - quantity: fraction of EC neurons classed as putative interneurons\n    value: 0.215\n    tolerance: 0.022\n  criterion: Monosynaptic pairs by the paper's jitter test (Supplemental Experimental Procedures,\n    Cell Type Classification; [-5, 5] ms jitter, 1000 surrogates, 99% global band over [-20, 20]\n    ms, a significant peak or trough in any 1 ms bin at [1, 5] ms, the 0-1 ms bin ignored for\n    same-shank pairs). The visual inspection that removed spurious pairs cannot be repeated and\n    is open; readings (a) all pairs the test finds, (b) different-shank pairs only (Figure S3,\n    206 excitatory and 97 inhibitory). The hyperplane on trough-to-peak latency and asymmetry is\n    fitted to the identified cells; the classifier is not named, so a linear classifier (linear\n    discriminant) is the reading, as the text says \"hyperplane\". If the dataset holds the\n    paper's cell-type labels, the fractions are taken from them and the recomputation is a\n    variant.\n- id: figs4-ec2-bursting\n  statement: EC2 principal cells burst at short interspike intervals (< 6 or 10 ms) more than EC3\n    and EC5 principal cells, and all EC layers burst less than any hippocampal group; in the\n    hippocampus CA1 bursts less than CA3 and DG, and CA3 less than DG.\n  source: Results, Physiological identification of entorhinal neuron types, paragraph 2; Figure\n    2D; Figure S4D and S4E\n  quote: EC2 principle cells have larger bursting index than both EC3 and EC5 principal cell\n    groups ... All EC layers have smaller bursting index than any hippcampal groups ... In the\n    hippocampus, CA1 has smaller bursting index than CA3 and DG ... and CA3 has smaller bursting\n    index than DG\n  statistics:\n  - about: EC2 against EC3 and EC5 principal cells\n    test: two-sample Kolmogorov-Smirnov test, one-sided\n    p: 1.0e-116\n    p_relation: \"<\"\n  - about: every EC layer against every hippocampal group\n    test: two-sample Kolmogorov-Smirnov test, one-sided\n    p: 1.0e-50\n    p_relation: \"<\"\n  - about: CA1 against CA3 and DG\n    test: two-sample Kolmogorov-Smirnov test, one-sided\n    p: 1.0e-12\n    p_relation: \"<\"\n  - about: CA3 against DG\n    test: two-sample Kolmogorov-Smirnov test, one-sided\n    p: 0.01\n    p_relation: \"<\"\n  criterion: Bursting index of each principal cell, the ratio of ISIs < 6 ms (and, separately,\n    < 10 ms) to all ISIs (Figure S4D, S4E legend), from spikes in theta epochs during walking\n    (Figure S4 title). Each ordering is tested by a one-sided two-sample Kolmogorov-Smirnov test\n    at p < 0.05, for both ISI cut-offs. Reproduced when every ordering the dataset can test holds\n    at both cut-offs; partially reproduced when some hold; the orderings needing groups the\n    dataset lacks are not testable.\n- id: fig1-ec3-ca1-theta-coherence\n  statement: Theta recorded in EC3 is typically in phase with CA1 pyramidal layer theta (less than\n    90 degrees shift in all experiments) and highly coherent with it (coherence 0.6 to 0.9).\n  source: Results, Physiological identification of entorhinal cortical layers, paragraph 2;\n    Figure 1B and 1C; Figure S10 legend\n  quote: EC3 theta was typically in phase ... and highly coherent (0.6–0.9\n  expected:\n  - quantity: EC3 to CA1 pyramidal layer theta coherence, per session\n    value: 0.75\n    tolerance: 0.21\n  - quantity: EC3 to CA1 pyramidal layer theta phase shift, largest over sessions\n    value: 90\n    tolerance: 9\n    unit: degrees\n  criterion: Sessions with both an EC3 site and a CA1 pyramidal layer site. Coherence in the\n    theta band during theta epochs; the range 0.6 to 0.9 widened by 10% of each bound gives 0.54\n    to 0.99 (the expected value above states that range). The paper does not say how coherence\n    is estimated or over which band; readings (a) multitaper coherence at the theta peak\n    frequency, (b) the mean over 5-11 Hz, the band the paper uses for theta. The phase shift is\n    the circular mean phase difference of the 5-11 Hz filtered signals; Figure S10 reports 0 to\n    80 degrees, CA1 leading. Reproduced when, under one reading, every session's coherence lies\n    in 0.54 to 0.99 and every shift is below 99 degrees; partially reproduced when at least half\n    the sessions do. Not testable when the dataset holds no EC3 LFP.\n- id: fig1-layer-reversals\n  statement: CA1 sharp-wave ripples are associated with a negative wave in EC3 to EC6 that\n    reverses polarity between EC2 and EC3, while theta waves are in phase from EC3 to EC6 and\n    reverse between EC1 and EC3.\n  source: Results, Physiological identification of entorhinal cortical layers, paragraph 1;\n    Figure 1B and 1C\n  quote: Sharp-wave ripples recorded from the CA1 pyramidal layer were associated with a negative\n    wave in EC3 to EC6, with a polarity reversal between EC2 and EC3 layers ... theta waves were\n    in phase from EC3 to EC6 and reversed between EC1 and EC3\n  criterion: Ripples detected in the CA1 pyramidal layer during non-theta periods (140-230 Hz,\n    RMS in 17 ms windows, threshold 7 SD above the mean; Supplemental Experimental Procedures)\n    and EC LFP averaged around the ripple power peak; theta waves averaged around CA1 theta peaks\n    (Figure 1B legend). Layers as the dataset labels them. Reproduced when the ripple-triggered\n    EC wave is negative at EC3 and EC5 sites and positive or absent at EC2 sites, and the theta\n    average at EC1 sites is opposite in sign (phase difference above 90 degrees) to that at EC3\n    and EC5 sites, which are within 90 degrees of each other. Not testable without EC sites of\n    known layer.\n- id: fig3-interneurons-min-ascending\n  statement: Interneurons in all regions, and principal cells other than EC3, are least active on\n    the ascending phase of EC3 theta.\n  source: Results, Theta-phase relationship of entorhinal and hippocampal neurons, paragraphs 1\n    and 2; Figure 3A, 3B, 3E and 3F; Figure S5\n  quote: Overall, with the exception of EC3 pyramidal cells, principal cells and interneurons in\n    the hippocampus and EC were least active on the ascending phase of the EC3 theta\n  criterion: Population phase histogram of all spikes of each group (10 degree bins, all neurons\n    whether or not modulated; Figure 3A, 3E), referenced to EC3 theta by the maxima method. The\n    ascending phase is the half cycle from trough (180) to peak (360). Readings for the phase\n    range (a) the ascending half cycle, 180 to 360 degrees; (b) the shaded column of Figure 3,\n    which the figure draws at roughly 280 to 340 degrees (read from the plot, not stated). For\n    each interneuron group (CA1, CA3, DG, EC2, EC3, EC5) and each non-EC3 principal group, the\n    bin of minimum probability is found. Reproduced when, under one reading, the minimum falls in\n    the range for every group the dataset holds, EC5 principal cells excepted when their\n    histogram is flat (claim fig3-ec5-weakest); partially reproduced when it does for most. With\n    CA1 only, the claim is tested on CA1 principal cells and interneurons, with CA1 pyramidal\n    layer theta as the reference if EC3 LFP is absent (Figure S10 permits it, with the 0 to 80\n    degree shift recorded).\n- id: fig3-dg-ca3-precede-ca1\n  statement: DG and CA3 principal neurons share a similar theta phase and precede the firing of\n    CA1 pyramidal cells by 90 to 120 degrees.\n  source: Results, Theta-phase relationship of entorhinal and hippocampal neurons, paragraph 1;\n    Figure 3A to 3C\n  quote: Dentate putative principal neurons and CA3 pyramidal cells shared a similar phase space,\n    preceding the firing of CA1 pyramidal cells by 90\n  expected:\n    quantity: phase lead of DG and of CA3 principal cells over CA1 pyramidal cells\n    value: 105\n    tolerance: 24\n    unit: degrees\n  criterion: The range 90 to 120 degrees widened by 10% of each bound gives 81 to 132 (stated above\n    as 105 +/- 24, rounded outward). The paper does not say which phase of a group is compared.\n    Readings (a) the circular mean of preferred phases of significantly modulated cells (group\n    mean lines, Figure 3C); (b) the peak of the population spike histogram (Figure 3A, 10 degree\n    bins). Reproduced when, under one reading, both CA3 and DG lead CA1 by 81 to 132 degrees.\n    Not testable without CA3 or DG neurons.\n- id: fig3-ec-opposite-to-targets\n  statement: EC2 and EC3 principal neurons fire, on average, out of phase with each other, and each\n    has a preferred phase approximately opposite to that of its hippocampal targets (EC2 against\n    DG and CA3, EC3 against CA1).\n  source: Results, Theta-phase relationship of entorhinal and hippocampal neurons, paragraph 1;\n    Figure 3A to 3C\n  quote: EC2 and EC3 principal neurons, the main afferents to dentate/CA3 and CA1 neurons,\n    respectively ... fired, on average, out-of-phase from each other and, unexpectedly, had\n    preferred discharge phases approximately opposite to those of their target hippocampal\n    neurons\n  criterion: Group phases as in fig3-dg-ca3-precede-ca1, readings (a) and (b). \"Out of phase\" and\n    \"approximately opposite\" have no threshold in the paper. The paper calls a shift under 90\n    degrees \"in phase\" (Results, EC3 theta \"typically in phase (<90 degrees shift\"), so the\n    readings for opposite are (i) a difference of more than 90 degrees, (ii) a difference within\n    45 degrees of 180. Reproduced when, under reading (i) with either group phase, all three\n    differences (EC2-EC3, EC2-DG/CA3, EC3-CA1) exceed 90 degrees; the result under (ii) is\n    reported. Not testable without EC principal cells.\n- id: fig3c-ec3-subset-locked\n  statement: A small subset of EC3 principal cells fires in phase with the EC2 population, and this\n    subgroup has the strongest theta phase locking (largest mean resultant lengths) of all EC3\n    cells.\n  source: Results, Theta-phase relationship of entorhinal and hippocampal neurons, paragraph 2;\n    Figure 3B and 3C\n  quote: A small subset of EC3 pyramidal cells though fired in phase with the EC2 population (Figures\n    3B and 3C), and this subgroup showed the strongest theta phase locking\n  criterion: Significantly modulated EC3 principal cells. The paper does not define the subgroup.\n    Readings (a) cells whose preferred phase is within 90 degrees of the EC2 group mean phase;\n    (b) within 45 degrees. The subgroup must be a minority (under half) of the EC3 cells, and its\n    mean resultant lengths larger than those of the other EC3 cells by a Wilcoxon rank sum test\n    at p < 0.05 (the paper's test for R in Figure 3D; the paper reports no test for this\n    comparison). Reproduced when both hold under one reading. Not testable without EC3 and EC2\n    principal cells.\n- id: fig3-ec5-weakest\n  statement: A subset of EC5 principal neurons is significantly phase locked, but their preferred\n    phases are relatively uniformly distributed, so EC5 principal cells are the least theta\n    modulated population.\n  source: Results, Theta-phase relationship of entorhinal and hippocampal neurons, paragraph 2;\n    Figure 3A to 3D\n  quote: Although a subset of individual EC5 principal neurons had significant theta phase locking,\n    their preferred phases showed a relatively uniform distribution in the population ... As a\n    result, the EC5 principal cells were least modulated by the theta cycle as a population\n  criterion: Population modulation from the pooled spike histogram of each principal group (Figure\n    3A). The measure is not named; readings (a) the mean resultant length of all pooled spikes,\n    (b) the ratio of maximum to minimum of the 10 degree histogram. Reproduced when, under one\n    reading, EC5 has the lowest value of the principal groups the dataset holds and, for the\n    uniformity of preferred phases, the mean resultant length of the significantly modulated EC5\n    cells' preferred phases is below that of each other principal group. Not testable without\n    EC5 principal cells.\n- id: fig3d-ec2-strongest-modulation\n  statement: Among EC principal cells and among EC interneurons, EC2 cells have the largest mean\n    resultant length and the highest percentage of significantly theta-modulated cells.\n  source: Results, Theta-phase relationship of entorhinal and hippocampal neurons, paragraph 2;\n    Figure 3D and 3H\n  quote: In the EC, EC2 neurons showed the strongest theta modulation as a population (Figures 3A,\n    3E, and S4) and had the highest percentage of theta-modulated cells (Figures 3D and 3H)\n  statistics:\n  - about: mean R, EC2 against EC3 and against EC5 principal cells (red asterisks, Figure 3D)\n    test: Wilcoxon rank sum test\n    p: 1.0e-11\n    p_relation: \"<\"\n  - about: percent modulated, EC2 against EC3 and against EC5 principal cells (red asterisks,\n      Figure 3D)\n    test: chi-square independence test\n    p: 1.0e-11\n    p_relation: \"<\"\n  - about: mean R, EC2 against EC3 and against EC5 interneurons (red asterisks, Figure 3H)\n    test: Wilcoxon rank sum test\n    p: 1.0e-11\n    p_relation: \"<\"\n  - about: percent modulated, EC2 against EC3 interneurons (Figure 3H, double asterisk)\n    test: chi-square independence test\n    p: 0.05\n    p_relation: \"<\"\n  - about: percent modulated, EC2 against EC5 interneurons (Figure 3H, single asterisk)\n    test: chi-square independence test\n    p: 1.0e-4\n    p_relation: \"<\"\n  criterion: Significant modulation and R as in the shared methods (at least 50 spikes, rate > 0.1\n    Hz, Rayleigh p < 0.01); mean R over significantly modulated cells, compared by Wilcoxon rank\n    sum test; the fraction modulated over all cells passing the spike and rate criteria, compared\n    by chi-square test of independence (Figure 3D legend). Reproduced when, for principal cells\n    and for interneurons, EC2 exceeds EC3 and EC5 in both measures with p < 0.05; partially\n    reproduced when it holds for one cell class or one measure. Not testable without EC cells.\n    The significance marks were read from the figure; the legend prints \"**p < 0.05, *p < 10-4,\n    red *p < 10-11\".\n- id: fig3d-hippocampal-modulation\n  statement: Among hippocampal principal cells, CA1 pyramidal cells have a lower mean resultant\n    length than CA3 and DG cells and a lower percentage of theta-modulated cells than CA3 and DG.\n  source: Figure 3D\n  inferred: Read from the bars and significance marks of Figure 3D (CA1 against CA3 and DG); no\n    sentence of the text states the hippocampal comparisons.\n  statistics:\n  - about: mean R, CA1 against CA3 and against DG principal cells (red asterisks)\n    test: Wilcoxon rank sum test\n    p: 1.0e-11\n    p_relation: \"<\"\n  - about: mean R, CA3 against DG principal cells (black single asterisk)\n    test: Wilcoxon rank sum test\n    p: 1.0e-4\n    p_relation: \"<\"\n  - about: percent modulated, CA1 against CA3 (single asterisk) principal cells\n    test: chi-square independence test\n    p: 1.0e-4\n    p_relation: \"<\"\n  - about: percent modulated, CA1 against DG (double asterisk) principal cells\n    test: chi-square independence test\n    p: 0.05\n    p_relation: \"<\"\n  expected:\n  - quantity: mean R of significantly modulated CA1 pyramidal cells (read from the bar)\n    value: 0.19\n    tolerance: 0.019\n  - quantity: percent of CA1 pyramidal cells significantly modulated (read from the bar)\n    value: 84\n    tolerance: 8.4\n    unit: percent\n  criterion: As fig3d-ec2-strongest-modulation, for CA1, CA3 and DG principal cells. Reproduced when\n    CA1 is below CA3 and DG in both measures at p < 0.05. The two expected values are read from\n    the bar heights of Figure 3D at the figure's resolution and test CA1 alone where CA3 and DG\n    are absent.\n- id: figs8-task-invariance\n  statement: The theta phase relations of neurons in the different EC layers and hippocampal\n    regions are essentially identical across the linear track, open field, T maze and wheel tasks.\n  source: Results, Theta-phase relationship of entorhinal and hippocampal neurons, paragraph 3;\n    Figure S8\n  quote: Although slight variations were observed, the theta phase relations of neurons in different\n    EC layers and hippocampal regions were essentially identical across different testing\n    conditions (Figure S8)\n  criterion: Preferred phases of significantly modulated cells per group and task (Figure S8). The\n    paper gives no test or threshold. Readings for \"essentially identical\" (a) the circular mean\n    preferred phase of each group differs by less than 45 degrees between any two tasks, (b) by\n    less than 90 degrees (the paper's in-phase bound, Results). Reproduced when the group order\n    of phases holds in every task and reading (b) holds; reading (a) is reported. With one task\n    in the dataset, not testable.\n- id: figs9-phase-method\n  statement: Preferred theta phases are similar whether phase is computed from theta peaks, troughs\n    or the Hilbert transform of 5-11 Hz filtered LFP.\n  source: Results, Theta-phase relationship of entorhinal and hippocampal neurons, paragraph 3;\n    Figure S9\n  quote: Similar results were obtained using the peak or trough ... or the Hilbert transform of the\n    theta band-filtered LFP to compute theta phase (Figure S9)\n  criterion: For each group the dataset holds, the circular mean preferred phase of significantly\n    modulated cells under each of the three methods (Supplemental Experimental Procedures). The\n    paper gives no threshold; readings (a) within 45 degrees, (b) within 90 degrees between\n    methods. Reproduced when (b) holds for every group; (a) is reported.\n- id: figs10-ca1-reference\n  statement: With CA1 pyramidal layer theta instead of EC3 theta as the reference, the relative\n    phase distributions of the groups are the same, with CA1 theta leading EC3 by 0 to 80 degrees\n    across rats and sessions.\n  source: Results, Theta-phase relationship of entorhinal and hippocampal neurons, paragraph 3;\n    Figure S10\n  quote: Zero to 80o (CA1 slightly precedes EC3) phase shifts were observed between the CA1\n    pyramidal layer and EC3 in different rats/sessions\n  expected:\n    quantity: CA1 to EC3 theta phase lead, range over sessions\n    value: 40\n    tolerance: 48\n    unit: degrees\n  criterion: Sessions with both a CA1 pyramidal layer and an EC3 site. The range 0 to 80 degrees\n    widened by 10% of each bound is 0 to 88 (stated above as 40 +/- 48, so -8 to 88). Session\n    shift is the circular mean difference of the peak-referenced phases. Reproduced when every\n    session's shift lies in that range and the group mean preferred phases under the two\n    references differ by about the session shift (each group's difference within 45 degrees of\n    the mean session shift; the threshold is not in the paper). Not testable without EC3 LFP.\n- id: fig4a-ec-hippocampus-offsets\n  statement: Large time offsets of 50 to 85 ms separate EC2 principal cells from CA3 and DG\n    principal cells, and EC3 from CA1 principal cells; EC2-DG and EC2-CA3 group cross-correlograms\n    are the most theta modulated and EC3-CA1 modestly.\n  source: Results, Temporal relationship between entorhinal and hippocampal neurons, paragraph 1;\n    Figure 4A\n  quote: large time offsets (50 to 85 ms) were present between EC2 and CA3/dentate principal cells\n    and between EC3 and CA1 pyramidal neurons (black arrows in Figure 4A)\n  statistics:\n  - about: significant peak bins of group cross-correlograms\n    test: spike jitter test (uniform [-125, 125] ms), 99.9% global band\n    p: 0.001\n    p_relation: \"<\"\n  expected:\n    quantity: time from the EC reference spike to the peak of the target group's activity\n    value: 67.5\n    tolerance: 26\n    unit: ms\n  criterion: Group cross-correlograms with the EC principal cell as reference (Figure 4A, time zero\n    the reference spike; arrows point to positive lags), computed as in the shared methods. The\n    range 50 to 85 ms widened by 10% of each bound is 45 to 93.5 ms. The peak taken is open;\n    readings (a) the first significant peak (bins above the 99.9% band) of the smoothed group\n    CCG at positive lag, (b) the mode of the smoothed distribution of pair offsets at positive\n    lag. Reproduced when, under one reading, EC2-DG, EC2-CA3 and EC3-CA1 all peak at 45 to 93.5\n    ms. Theta modulation of the group CCG is compared by the CCG's peak-to-trough ratio over\n    [-150, 150] ms (a measure the paper does not name) and reported. Not testable without EC\n    neurons.\n- id: fig4a-pair-offset-ranges\n  statement: Most EC2-DG, EC2-CA3 and EC3-CA1 principal pairs have temporal offsets in [-60, 0] ms\n    or [60, 120] ms, and only a minority peak at [0, 30] ms.\n  source: Results, Temporal relationship between entorhinal and hippocampal neurons, paragraph 1;\n    Figure 4A, black histograms\n  quote: Most of EC2-DG, EC2-CA3, and EC3-CA1 principalprincipal neuron pairs had temporal offsets\n    at\n  criterion: Significantly correlated pairs and their offsets as in the shared methods (Supplemental\n    Experimental Procedures, temporal offsets). The quote is cut where the PDF text garbles the\n    minus sign; the passage continues \"[-60 to 0] ms or [60 to 120] ms, and only a minority of\n    pairs had peaks at [0 to 30] ms\". Reproduced when, for each of the three categories, more\n    than half of the significant pairs fall in [-60, 0] or [60, 120] ms and fewer than half in\n    [0, 30] ms; partially reproduced for one or two categories.\n- id: fig4a-ec5-ca1-flat\n  statement: The group cross-correlogram and the distribution of temporal offsets between CA1 and\n    EC5 principal cells are essentially flat, while those of EC2-EC5 and EC3-EC5 pairs are more\n    strongly theta modulated.\n  source: Results, Temporal relationship between entorhinal and hippocampal neurons, paragraph 1;\n    Figure 4A\n  quote: The group cross-correlogram and the distribution of temporal offsets between CA1 and EC5\n    principal cell pairs was essentially flat, whereas those of EC2-EC5 and EC3-EC5 pairs were\n    more strongly theta modulated\n  criterion: A claim of absence for CA1-EC5, judged on the paper's tests (Figure 4 legend,\n    Supplemental Experimental Procedures). The offset distribution is tested against the 95%\n    global band for a uniform distribution; flat when the smoothed distribution stays inside the\n    band. The group CCG's significant bins (99.9% jitter band) are reported. Reproduced when the\n    CA1-EC5 offset distribution stays inside the band and the EC2-EC5 and EC3-EC5 distributions\n    leave it; the peak-to-trough ratio of the smoothed group CCGs is given for all three. Not\n    testable without EC5 and CA1 neurons recorded together.\n- id: fig4-ec2-ec3-opposite-lags\n  statement: EC2 and EC3 principal cells fire with time lags corresponding to opposite theta phases;\n    EC2 principal-EC2/3 interneuron pairs have small offsets and EC3 principal-EC2/3 interneuron\n    pairs large ones; EC2 principal-DG/CA3 interneuron and EC3 principal-CA1 interneuron pairs\n    also have large offsets.\n  source: Results, Temporal relationship between entorhinal and hippocampal neurons, paragraph 1;\n    Figure 4A and 4B\n  quote: Principal cells of EC2 and EC3 fired with time lags corresponding to preferences of opposite\n    phases of the theta cycle (Figure 4A). EC2 principal cell-EC2/3 interneuron pairs had small,\n    whereas EC3 principal cell-EC2/3 interneuron pairs had large temporal offsets\n  criterion: Peak of the smoothed group CCG within [-150, 150] ms, as in the shared methods. The\n    paper assumes 1 theta cycle = 125 ms (Figure S11 legend), so opposite phases are a lag near\n    62.5 ms. \"Small\" and \"large\" have no threshold; readings (a) small is within 20 ms of zero\n    and large beyond 40 ms; (b) small is below a quarter cycle (31 ms) and large above it.\n    Reproduced when, under one reading, the EC2-EC3 lag is large and every pairing falls in the\n    class the statement gives. Not testable without EC neurons.\n- id: figs11-phase-time-agreement\n  statement: The time offsets of individual neuron pairs correlate closely with the differences\n    between their preferred theta phases.\n  source: Figure S11 legend\n  quote: Note close correlation between results obtained from phase offset and time offset\n    calculations\n  criterion: Pairs whose members are both significantly theta modulated and whose CCG has more\n    than 100 events in [-150, 150] ms (Figure S11 legend). For each pair, the preferred phase\n    difference converted to time with 1 cycle = 125 ms, against the peak time of the smoothed\n    (SD 10 ms) CCG. The paper gives no statistic; \"close correlation\" is read as a circular-linear\n    or, after unwrapping to [-62.5, 62.5] ms, Pearson correlation above 0.5 with p < 0.05 (the\n    threshold is not in the paper). Tested on any pair category the dataset holds, CA1-CA1 pairs\n    included.\n- id: fig5-rate-phase-shift\n  statement: As instantaneous firing rate rises, EC2 and CA1 principal cells shift to progressively\n    earlier theta phases (by more than 150 degrees), EC2 cells also losing phase locking, while\n    DG and CA3 cells shift less than 90 degrees without a change in modulation depth, and EC3\n    cells as a population change little.\n  source: Results, Rate versus phase relationship, paragraph 1; Figure 5A; Figure S12A\n  quote: Firing rate changes were moderately correlated with the preferred phases of DG and CA3\n    principal neurons ... In contrast, as firing rate increased, EC2 and CA1 principal neurons\n    advanced to progressively earlier phases\n  expected:\n  - quantity: phase advance of EC2 and of CA1 principal cells from 4 Hz to >= 40 Hz, lower bound\n    value: 150\n    tolerance: 15\n    unit: degrees\n  - quantity: phase shift of DG and of CA3 principal cells, upper bound\n    value: 90\n    tolerance: 9\n    unit: degrees\n  criterion: Spikes binned by instantaneous rate (1 to >= 10 spikes per 250 ms); per category, cells\n    with at least 50 spikes in it and Rayleigh p < 0.01 (Figure 5A legend); group mean preferred\n    phase and mean R per category. The shift is the circular difference of group means between\n    the 4 Hz and >= 40 Hz categories, a phase advance being a move to earlier phase. Reproduced\n    when EC2 and CA1 advance by more than 135 degrees and DG and CA3 shift by less than 99\n    degrees. The single-cell shifts of Figure S12A (cells modulated in both categories) are\n    reported as a variant. EC2's decreasing R is judged by the sign of the Spearman correlation\n    of group R with rate category. Groups the dataset lacks are not testable; CA1 alone is tested\n    on its own.\n- id: fig5b-burst-double-peak\n  statement: Burst spikes (ISI < 6 ms) tend to occupy the same theta phase as fast spikes (>= 40 Hz),\n    but in EC2 and CA1 principal cells the burst probability has two small peaks.\n  source: Results, Rate versus phase relationship, paragraph 2; Figure 5B; Figure S12B\n  quote: bursts tended to occupy similar theta phase as sustained fastfrequency spikes\n  criterion: Phase histograms (10 degree bins, all neurons; Figure 5B) of burst spikes (an ISI before\n    or after < 6 ms) and of >= 40 Hz spikes. Similar phase is read as circular means within 90\n    degrees (the paper's in-phase bound; no threshold given). The double peak has no test in the\n    paper; readings (a) two local maxima of the histogram smoothed over 3 bins, separated by at\n    least 60 degrees, each above the histogram mean; (b) a two-component von Mises mixture\n    preferred over one component by BIC. Reproduced when bursts and fast spikes are within 90\n    degrees in every group the dataset holds and CA1 (and EC2, when present) shows two peaks\n    under one reading.\n- id: figs13-interneuron-rate\n  statement: Firing rate and bursting shift interneurons' theta phase only marginally (less than 30\n    degrees).\n  source: Results, Rate versus phase relationship, paragraph 2; Figure S13\n  quote: Firing rate and bursting, in the frequency range similar to principal cells, marginally\n    affected the interneuron's spiking phase\n  expected:\n    quantity: largest group-mean phase shift of interneurons between 4 Hz, >= 40 Hz and burst\n      spikes\n    value: 30\n    tolerance: 3\n    unit: degrees\n  criterion: As fig5-rate-phase-shift, for interneurons. Reproduced when, in every interneuron group\n    the dataset holds, the group mean preferred phases at 4 Hz, >= 40 Hz and for burst spikes\n    differ pairwise by less than 33 degrees.\n- id: fig6-hippocampal-precession\n  statement: Hippocampal principal neurons in all subregions show robust phase precession on the\n    linear track, even at peak rates as low as 5 Hz, whereas EC fields with high spatial\n    coherence are often but not always associated with precession.\n  source: Results, Phase precession in the hippocampus and EC, paragraph 1; Figure 6\n  quote: Hippocampal principal neurons in all subregions showed a robust phase precession slope\n    (Figures 6H–6J), even at peak firing rates as low as 5 Hz\n  criterion: Linear track place fields as in the shared methods. Reproduced when, in every\n    hippocampal region the dataset holds, more than half of fields with coherence > 0.7 have a\n    negative phase-position correlation, including fields whose peak rate is under 10 Hz. Not\n    testable without linear track sessions.\n- id: fig7a-precession-strength\n  statement: On the linear track, a smaller share of EC place fields than hippocampal place fields\n    has spatial coherence above 0.7 (CA1 37.8% of 1169, CA3 32.1% of 106, DG 28.3% of 60, EC2 10%\n    of 210, EC3 10.9% of 175, EC5 6.8% of 148); among EC cells EC2 has the highest proportion of\n    negatively correlated fields, and all hippocampal regions a higher proportion than EC2.\n  source: Results, Phase precession in the hippocampus and EC, paragraph 2; Figure 7A\n  quote: Among EC cells, EC2 cells had the highest proportion of negatively correlated place fields,\n    but neurons in all hippocampal regions had higher proportion of negatively correlated fields\n    than EC2 (Figure 7A)\n  expected:\n  - quantity: CA1 fields with coherence above 0.7\n    value: 37.8\n    tolerance: 3.8\n    unit: percent of 1169 fields\n  - quantity: CA1 place fields on the linear track\n    value: 1169\n    tolerance: 117\n  - quantity: CA3 fields with coherence above 0.7\n    value: 32.1\n    tolerance: 3.2\n    unit: percent of 106 fields\n  - quantity: DG fields with coherence above 0.7\n    value: 28.3\n    tolerance: 2.8\n    unit: percent of 60 fields\n  - quantity: EC2 fields with coherence above 0.7\n    value: 10\n    tolerance: 1\n    unit: percent of 210 fields\n  - quantity: EC3 fields with coherence above 0.7\n    value: 10.9\n    tolerance: 1.1\n    unit: percent of 175 fields\n  - quantity: EC5 fields with coherence above 0.7\n    value: 6.8\n    tolerance: 0.7\n    unit: percent of 148 fields\n  criterion: Fields, coherence and phase-position correlation as in the shared methods, with\n    readings O1 for coherence. \"Negatively correlated\" is not defined further; readings (a) a\n    correlation below zero, (b) a correlation below zero with p < 0.05. Reproduced when the\n    percentages of the groups the dataset holds are within tolerance and the ordering of\n    negatively correlated proportions (each hippocampal region above EC2, EC2 above EC3 and EC5)\n    holds under one reading. The percentages and the n above each panel were read from Figure 7A.\n- id: figs15-ec3-no-precession\n  statement: EC3 principal cells, as a group, show no phase change with position within firing\n    fields, while the mean phase shifts in other layers and regions are comparable.\n  source: Results, Phase precession in the hippocampus and EC, paragraph 2; Figure S15\n  quote: Principal neurons in EC3, as a group, did not show phase changes with position within\n    firing fields\n  criterion: A claim of absence, judged as Figure S15 shows it. Fields with coherence >= 0.7; mean\n    circular phase per 10% segment of each field, then the mean of field means with a 95%\n    confidence interval per segment. Reproduced when, for EC3, the confidence intervals of the\n    first and last segments overlap, and for the other groups they do not; the size of each\n    group's first-to-last shift is given. Not testable without EC3 linear track fields.\n- id: fig7b-frequency-shift\n  statement: On the linear track the great majority of hippocampal principal cells and a smaller\n    fraction of EC principal cells oscillate faster than EC3 theta (positive unit-LFP frequency\n    shift); significant theta power was found in 76.2% of 1448 CA1, 72.0% of 239 CA3, 76.8% of 69\n    DG, 62.5% of 413 EC2, 28.7% of 397 EC3 and 16.9% of 604 EC5 principal cells.\n  source: Results, Phase precession in the hippocampus and EC, paragraph 3; Figure 7B\n  quote: the great majority of hippocampal principal cells and a smaller fraction of EC principal\n    neurons oscillated faster (frequency shift >0) than the simultaneously recorded EC3 LFP theta\n    on the linear track\n  expected:\n  - quantity: CA1 principal cells with significant theta power, linear track\n    value: 76.2\n    tolerance: 7.6\n    unit: percent of 1448\n  - quantity: CA3 principal cells with significant theta power, linear track\n    value: 72.0\n    tolerance: 7.2\n    unit: percent of 239\n  - quantity: DG principal cells with significant theta power, linear track\n    value: 76.8\n    tolerance: 7.7\n    unit: percent of 69\n  - quantity: EC2 principal cells with significant theta power, linear track\n    value: 62.5\n    tolerance: 6.3\n    unit: percent of 413\n  - quantity: EC3 principal cells with significant theta power, linear track\n    value: 28.7\n    tolerance: 2.9\n    unit: percent of 397\n  - quantity: EC5 principal cells with significant theta power, linear track\n    value: 16.9\n    tolerance: 1.7\n    unit: percent of 604\n  criterion: All spikes of a principal cell in theta epochs of a task; multitaper spectra of spike\n    trains and LFP (Jarvis and Mitra, 2001); the shift is the lag of the peak of the\n    cross-correlation of the two power spectra over 5-12 Hz (Supplemental Experimental\n    Procedures). Significant theta power when the mean integrated power at peak +/- 0.5 Hz is 30%\n    above that of both the 4-6 Hz and 12-14 Hz bands (Figure S16 legend). Taper parameters and\n    the spectral resolution are not given; readings (a) time-bandwidth 3 with 5 tapers, (b)\n    time-bandwidth 5 with 9 tapers, spectra at 0.1 Hz resolution (standard choices). Reproduced\n    when the percentages are within tolerance for the groups the dataset holds and more than\n    half of the cells with significant theta power in each hippocampal region have a positive\n    shift, with smaller fractions in each EC layer. EC3 theta as reference; local theta is a\n    variant the paper reports as identical.\n- id: figs16-open-field-smallest-shift\n  statement: The unit-LFP frequency shift results hold in each task separately, with the smallest\n    shift in the open field for every neuron type.\n  source: Results, Phase precession in the hippocampus and EC, paragraph 3; Figure S16\n  quote: the overall results were the same when data obtained from recordings in the linear track,\n    open field, T maze, and rewarded wheel-running task were analyzed separately, with the\n    smallest magnitude of the unit-LFP frequency shift present in the open field for all neuron\n    types\n  criterion: As fig7b-frequency-shift, per task. The magnitude compared is not named; readings (a)\n    the median shift of cells with significant theta power, (b) the mean. Reproduced when, under\n    one reading, the open field gives the smallest value of the tasks the dataset holds for every\n    group. With the open field alone, only the presence of a positive median shift in the open\n    field is reported, and the comparison is not testable.\n- id: figs18-spike-phase-spectrum\n  statement: The spike phase spectrum confirms the unit-LFP frequency comparison, with peaks above 1\n    (faster than theta) for phase precessing cells.\n  source: Results, Phase precession in the hippocampus and EC, paragraph 3; Figure S17 and S18\n  quote: The spike phase spectrum method (Figures 6A, 6F–6J, and S18) confirmed the phase precession\n    results obtained by the unit versus LFP oscillation frequency comparison\n  criterion: EC3 theta phase by the maxima method, unwrapped (jumps of pi or more replaced by their\n    2 pi complement), assigned to spikes by linear interpolation; multitaper spectrum of the\n    spike train in unwrapped phase; significant when mean power at peak +/- 0.025 is 50% above\n    both the 0.5-0.85 and 1.3-1.8 bands (Figure S18 legend). Taper settings open as in\n    fig7b-frequency-shift. Reproduced when the fraction of cells with a peak above 1 orders the\n    groups as the fraction with a positive shift in fig7b-frequency-shift does, and the cell-wise\n    signs agree for most cells significant under both methods.\n  depends_on:\n  - fig7b-frequency-shift\n- id: fig7-ca1-highest-precession\n  statement: Only a minority of EC principal cells show high spatial coherence and phase\n    precession, while most keep a constant theta phase preference; precession is most prevalent and\n    strongest in CA1, and exceptional in EC3.\n  source: Results, Phase precession in the hippocampus and EC, paragraph 4; Figure 7\n  quote: These findings demonstrate that only a minority of principal cells in the EC show high\n    spatial coherence and phase precession, while the majority of neurons keep a constant theta\n    phase preference. The highest prevalence and strongest phase precession was observed in the\n    CA1 region\n  criterion: From the measures of fig7a-precession-strength and fig7b-frequency-shift. Reproduced\n    when CA1 has the highest fraction of cells with a positive frequency shift and the most\n    negative median phase-position correlation of all groups the dataset holds, and EC3 the\n    lowest fraction of the EC layers. With CA1 alone, not testable as a comparison.\n  depends_on:\n  - fig7a-precession-strength\n  - fig7b-frequency-shift\n- id: fig8-ec-population-predicts-sinks\n  statement: The peak firing of EC3 and EC2 principal populations precedes the theta sinks in CA1\n    stratum lacunosum-moleculare and the dentate molecular layer by the delay expected from axon\n    conduction (about 30 degrees, about 10 ms), while firing of the target populations is delayed\n    by about half a theta cycle.\n  source: Figure 8; Discussion, EC contribution to theta LFP, paragraph 1\n  quote: Note that while the population peak of an upstream layer correctly predicts the timing of\n    the dendritic sink in its target layer, spiking activity in the downstream target population is\n    substantially delayed\n  data: with_inputs\n  criterion: The sink phases come from Montgomery et al. (2009), whose CSD theta traces Figure 8\n    shows; the paper names no archive for them. The author pins them if they are public, else\n    the claim is blocked. Population peaks are the maxima of the 10 degree pooled phase\n    histograms of EC2 and EC3 principal cells (Figure 3A); reproduced when each peak precedes its\n    target sink by 0 to 60 degrees (30 degrees, widened to the half-width of the CSD phase\n    uncertainty, a choice not in the paper) and the target population's histogram peak follows\n    the sink by more than 90 degrees.\n- id: figs2-ripple-sequence\n  statement: During sharp wave ripples, onset and peak delays of principal cells and interneurons\n    increase by 15 to 25 ms along the CA1-EC5-EC3-EC2 axis; CA1 pyramidal cells increase firing\n    about 6-fold and CA1 interneurons about 3-fold, while EC principal cells are recruited more\n    weakly than EC interneurons in every layer.\n  source: Figure S2 legend\n  quote: Note increasing onset and peak delays of both principal cells and interneurons (15-25 msec)\n    in the CA1-EC5-EC3-EC2 axis. Note also a ~6-fold firing increase of CA1 pyramidal cells and\n    ~3-fold increase of CA1 interneurons during ripples\n  expected:\n  - quantity: CA1 pyramidal cell firing increase during ripples\n    value: 6\n    tolerance: 0.6\n    unit: fold\n  - quantity: CA1 interneuron firing increase during ripples\n    value: 3\n    tolerance: 0.3\n    unit: fold\n  - quantity: delay between successive stages of CA1-EC5-EC3-EC2\n    value: 20\n    tolerance: 7.5\n    unit: ms\n  criterion: Ripples in the CA1 pyramidal layer during non-theta periods (140-230 Hz, RMS in 17 ms\n    windows, 7 SD threshold), spikes aligned to the ripple power peak, mean rate per group\n    (Figure S2 legend). Fold increase is the peak rate over the baseline rate; the baseline\n    window is not given, readings (a) -500 to -250 ms, (b) the mean rate outside ripples. The\n    delay range 15 to 25 ms widened by 10% of each bound is 13.5 to 27.5 ms. Reproduced when the\n    CA1 fold increases are within tolerance under one reading and, where EC groups are present,\n    each successive stage peaks 13.5 to 27.5 ms later than the one before.\n- id: figs19-fast-firing-minority\n  statement: In every region most principal neuron spikes occur at low instantaneous rates;\n    spikes at high rates are a minority in the EC.\n  source: Figure 8 legend; Figure S19 legend\n  quote: In each region and layer, most principal neurons are silent or fire at low rates, with only\n    a minority of neurons discharging at high frequency at a given time\n  criterion: Instantaneous rate per spike as in the shared methods; per region, the fraction of\n    principal-cell spikes in theta epochs in the >= 40 Hz category, and in categories of 4 to 12\n    Hz. Reproduced when, in every group the dataset holds, more spikes fall at 4 to 12 Hz than at\n    >= 40 Hz, and for EC groups the >= 40 Hz fraction is below one half.\n"
}
```

Result: not kept, because it reads the paper's text.

**Agent**

Fixing a few tolerance ranges and the Figure 8 criterion so that it uses the paper's own ~30° figure.

**Agent calls Bash**

```bash
python - <<'EOF'
p='claims/mizuseki-2009.yaml'
s=open(p).read()
reps=[
("""    value: 0.75
    tolerance: 0.21""","""    value: 0.765
    tolerance: 0.225"""),
("""    value: 105
    tolerance: 24
    unit: degrees
  criterion: The range 90 to 120 degrees widened by 10% of each bound gives 81 to 132 (stated above
    as 105 +/- 24, rounded outward).""","""    value: 106.5
    tolerance: 25.5
    unit: degrees
  criterion: The range 90 to 120 degrees widened by 10% of each bound gives 81 to 132 (stated above
    as 106.5 +/- 25.5)."""),
("""    value: 40
    tolerance: 48
    unit: degrees
  criterion: Sessions with both a CA1 pyramidal layer and an EC3 site. The range 0 to 80 degrees
    widened by 10% of each bound is 0 to 88 (stated above as 40 +/- 48, so -8 to 88).""","""    value: 44
    tolerance: 44
    unit: degrees
  criterion: Sessions with both a CA1 pyramidal layer and an EC3 site. The range 0 to 80 degrees
    widened by 10% of each bound is 0 to 88 (stated above as 44 +/- 44)."""),
("""    value: 67.5
    tolerance: 26
    unit: ms""","""    value: 69.25
    tolerance: 24.25
    unit: ms"""),
("""    value: 20
    tolerance: 7.5
    unit: ms""","""    value: 20.5
    tolerance: 7
    unit: ms"""),
("""    the claim is blocked. Population peaks are the maxima of the 10 degree pooled phase
    histograms of EC2 and EC3 principal cells (Figure 3A); reproduced when each peak precedes its
    target sink by 0 to 60 degrees (30 degrees, widened to the half-width of the CSD phase
    uncertainty, a choice not in the paper) and the target population's histogram peak follows
    the sink by more than 90 degrees.""","""    the claim is blocked. Both must be on the same theta reference; Figure 8 uses EC3 theta for
    units, and how the CSD phases of Montgomery et al. were referred to it is not said (open).
    Population peaks are the maxima of the 10 degree pooled phase histograms of EC2 and EC3
    principal cells (Figure 3A). The expected delay is "within an ~30 degree theta phase delay"
    (Discussion, EC contribution to theta LFP), widened by 10% to 0 to 33 degrees. "Offset by a
    half theta cycle" (Discussion, paragraph 1) has readings (a) the target population peak
    (DG/CA3 for the molecular layer sink, CA1 for the lacunosum-moleculare sink) follows the
    sink by more than 90 degrees, (b) by 180 +/- 45 degrees. Reproduced when both EC peaks
    precede their sinks by 0 to 33 degrees and the targets follow under reading (a); (b) is
    reported."""),
("""  criterion: Linear track place fields as in the shared methods. Reproduced when, in every
    hippocampal region the dataset holds, more than half of fields""","""  criterion: Linear track place fields as in the shared methods. "Robust" has no threshold in
    the paper; it is read as reproduced when, in every
    hippocampal region the dataset holds, more than half of fields"""),
]
for a,b in reps:
    assert a in s, a[:60]
    s=s.replace(a,b)
open(p,'w').write(s)
EOF
grep -n "rather\|—" claims/mizuseki-2009.yaml; python tools/claims_check.py claims/mizuseki-2009.yaml paper/10.1016-j.neuron.2009.08.037.txt
```

Result: not kept, because it reads the paper's text.

**Agent**

Four quotes cross page breaks or figure legends in the extracted text; cutting them with "...". The 10⁻⁴ p-values are printed with a garbled minus in the text; I read them from the PDF.

**Agent calls Bash**

```bash
python - <<'EOF'
p='claims/mizuseki-2009.yaml'
s=open(p).read()
reps=[
("""  quote: EC2 and EC3 principal neurons, the main afferents to dentate/CA3 and CA1 neurons,
    respectively ... fired,""","""  quote: EC2 and EC3 principal neurons, the main afferents to dentate/CA3 ... fired,"""),
("""principal cell pairs was essentially flat, whereas those of EC2-EC5 and EC3-EC5 pairs were
    more strongly theta modulated""","""principal cell pairs was essentially flat, whereas those of EC2-EC5 pairs and EC3-EC5 pairs
    were more strongly theta modulated"""),
("""  quote: Among EC cells, EC2 cells had the highest proportion of negatively correlated place fields,
    but neurons""","""  quote: Among EC cells, EC2 cells had the highest proportion of ... negatively correlated place
    fields, but neurons"""),
("""    results obtained by the unit versus LFP oscillation frequency comparison""","""    results obtained by the unit ... versus LFP oscillation frequency comparison"""),
]
for a,b in reps:
    assert a in s, a[:60]
    s=s.replace(a,b)
open(p,'w').write(s)
EOF
python tools/claims_check.py claims/mizuseki-2009.yaml paper/10.1016-j.neuron.2009.08.037.txt; grep -nP "^\s+[^#\n]*[^\"']: \S" claims/mizuseki-2009.yaml | grep -vP "^\d+:\s*-?\s*[a-z_]+: " | head
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
git status --short; grep -c "rather\|—" claims/mizuseki-2009.yaml
```

```
?? .bash_profile
?? .bashrc
?? .gitconfig
?? .idea
?? .mcp.json
?? .profile
?? .ripgreprc
?? .vscode
?? .zprofile
?? .zshrc
?? claims/mizuseki-2009.yaml
?? scripts
0
```

**Agent**

I wrote `claims/mizuseki-2009.yaml` and did not commit it.

**Text read.** I read the version of record with its supplement: the Supplemental Experimental Procedures, Table S1 and the legends of Figures S1 to S19. The extracted text garbles degree and minus signs, so I read those values from the PDF. Table S1 is an image, so I read it from the rendered page, as I did the Fig. 3D/3H significance marks, the Fig. 4 arrows and the Fig. 7 percentages and n. Nothing the claims needed was missing. The paper links no code (its analysis used unpublished custom MATLAB), so every method comes from the paper and supplement.

**Counts.** There are 33 claims. 31 have quotes and 2 are `inferred`: the Table S1 cell counts, and the hippocampal comparisons in Fig. 3D, which only the figure shows. There are 14 recorded statistics: one-sided KS tests for bursting, Wilcoxon rank-sum and chi-square tests for Fig. 3D/H, and the jitter test for group cross-correlograms. Every claim has a criterion, and 13 have expected values. One claim, the Fig. 8 sink timing, is `with_inputs`, because its CSD sink phases come from Montgomery et al. 2009 and the paper names no archive for them.

**Quote check.** `tools/claims_check.py` reports 3 remaining problems. All are the p < 10⁻⁴ bound, which the text prints as "10�4". I confirmed it from the rendered Fig. 3 legend.

**Details the paper leaves open, with the readings named:**
- **Spatial coherence:** "neighbouring bins" means either the two adjacent bins, or each bin against the mean of its neighbours.
- **Counting units:** session by session, as the Table S1 legend says the paper did, with once per unit as a variant.
- **EC cell classification:** the visual pruning of spurious pairs can't be repeated, so the readings are all jitter-detected pairs, or different-shank pairs only. The "hyperplane" classifier is read as a linear discriminant.
- **EC3–CA1 coherence:** the estimator and band are not given. Readings: at the theta peak, or the mean over 5–11 Hz.
- **Group phase:** the circular mean of significantly modulated cells' preferred phases, or the peak of the pooled spike histogram.
- **"Ascending phase" minimum:** 180–360°, or the shaded column, about 280–340° as read from the figure.
- **"Approximately opposite":** more than 90° apart (by symmetry with the paper's own "<90° = in phase"), or within 45° of 180°.
- **Thresholds the paper doesn't give:**
  - **Fig. 3C EC3 subgroup:** within 90° or 45° of the EC2 mean.
  - **Fig. 4 offsets:** what counts as "small" or "large".
  - **Similarity across tasks and phase methods:** within 45° or 90°.
  - **"Close correlation" in Fig. S11:** a correlation above 0.5.
  - **"Robust" precession:** more than half of fields.
  - **"Two small peaks" in burst firing:** two local maxima, or a two-component mixture.
- **Which peak sets the 50–85 ms offset:** the first significant peak of the group cross-correlogram, or the mode of the pair-offset distribution.
- **"Negatively correlated" fields in Fig. 7A:** r < 0, or r < 0 with p < 0.05.
- **Multitaper settings for Fig. 7B and Fig. S18:** time-bandwidth 3 with 5 tapers, or 5 with 9.
- **Open-field shift magnitude:** median or mean shift.
- **Ripple fold-increase baseline:** −500 to −250 ms, or the rate outside ripples.
- **Fig. 8:** how the CSD phases of Montgomery et al. were referred to EC3 theta. "Half a cycle" is read as more than 90°, or 180 ± 45°.

**Missing for claims.** The Fig. 8 CSD sink phases have no archive the paper names. Hippocampal Fig. 3D values exist only as bar heights, read approximately. The CRCNS data description suggests hc-2 holds only CA1 recordings in the open field, which I didn't check further. If so, the many claims that need EC, CA3/DG or other tasks will be untestable, and each criterion says so.

## End of run

26 turns, 6 minutes, $2.17 at API prices, result: success.
