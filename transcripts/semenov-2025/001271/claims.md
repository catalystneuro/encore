# 001271 · claims · run 39772419187

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cat docs/protocol.md; ls claims/001453/ paper/ claims/001271 2>&1; ls tools
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cat claims/001453/*.yaml | head -150; wc -l paper/*.txt; head -40 paper/*.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -n 25,200p claims/001453/*.yaml; wc -l paper/*.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1016-j.xcrp.2025.102660.txt"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
python3 -c "
t=open('paper/10.1016-j.xcrp.2025.102660.txt').read()
print(t[52300:85000])"
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/ddc1181a-edf9-4d2b-869a-37594436b28b/tool-results/b4h73w70c.txt"
}
```

```
1	ices, Sunnyvale, CA). The standard imaging protocol started 50 ms before sine wave stimulation and continued for 250 ms during and about 90 ms after the stimulation, generating 1,200 images per stimulation session. After the first session, the stimulus amplitude was increased if no APs were detected or decreased to find the threshold if multiple APs were evoked. The imaging/stimulation sessions were repeated multiple times with 20–60 s intervals between them, either at escalating voltages or by choosing voltages randomly. In experiments aimed at determining the excitation thresholds ( Figure 2D ), the sine wave amplitude was adjusted up or down in 5%–10% steps until the minimal voltages eliciting 1 and 5 APs were determined. Next, we switched to a different stimulus type (e.g., from a modulated to an unmodulated signal or from 2 to 20 kHz) and repeated the search for the 1- and 5-AP thresholds. The emission intensity over the entire cell soma (F) was quantified using either Fiji ImageJ 1.53C (National Institutes of Health, USA) or MetaMorph 7.7 (Molecular Devices, San Jose, CA). The mean value over a time interval preceding the electrical stimulation was used as a 100% reference ( F 0 ) . Emission change in each frame ( Δ F ) in the sequence was determined as Δ F = 100 % × ( F − F 0 ) ∕ F 0 . APs were readily identifiable as brief emission upticks. For experiments, we selected neurons whose APs peaked at a more than 5% Δ F and lasted about 10 ms (typical values: 11.3% ± 0.9% Δ F and 8 ± 0.7 ms duration, excluding afterhyperpolarization; mean ± SEM, n = 22). Traces of the optical membrane potential were not filtered or modified in any way (except for long recordings in Figure 3C , which were corrected for bleaching by subtracting a trace without APs). The maximum AP firing rate was measured as the inverse of the peak-to-peak time interval between the first two APs evoked in each stimulation session. Traces of the optical membrane potential, as well as other graphs,
[... 108 more lines not kept]
```

**Agent calls Bash**

```bash
cd paper; grep -n -o "SUPPLEMENT.\{0,300\}\|Supplement.\{0,200\}" 10.1016-j.xcrp.2025.102660.txt | head; python3 -c "
t=open('10.1016-j.xcrp.2025.102660.txt').read()
i=t.find('Figure S1',60000); print(len(t)); 
import re
for m in re.finditer('=====|-----|supp',t): print(m.start(), t[m.start():m.start()+100].replace('\n',' '))
"
```

```
7:Supplementary Material 1 Supplemental information can be found online at https://doi.org/10.1016/j.xcrp.2025.102660 . Highlights High-frequency sine waves excite neurons without modulation Neurons show sustaine
53:Supplementary Materials 1
370:Supplement: NIHMS2098259-supplement-1.pdf
374:Supplemental information 
111393
163 supplement file(s) from the PMC Open Access cloud data (PMC12320893), PDFs extracted with PyMuPDF (d
308 ------------------------------------------------------------------------ 319 nihpa Cell reports. Phy
313 ------------------------------------------------------------------- 319 nihpa Cell reports. Physical
318 -------------------------------------------------------------- 319 nihpa Cell reports. Physical scie
323 --------------------------------------------------------- 319 nihpa Cell reports. Physical science C
328 ---------------------------------------------------- 319 nihpa Cell reports. Physical science Cell R
333 ----------------------------------------------- 319 nihpa Cell reports. Physical science Cell Rep Ph
338 ------------------------------------------ 319 nihpa Cell reports. Physical science Cell Rep Phys Sc
343 ------------------------------------- 319 nihpa Cell reports. Physical science Cell Rep Phys Sci PMC
348 -------------------------------- 319 nihpa Cell reports. Physical science Cell Rep Phys Sci PMC12320
353 --------------------------- 319 nihpa Cell reports. Physical science Cell Rep Phys Sci PMC12320893 1
358 ---------------------- 319 nihpa Cell reports. Physical science Cell Rep Phys Sci PMC12320893 123208
363 ----------------- 319 nihpa Cell reports. Physical science Cell Rep Phys Sci PMC12320893 12320893 12
368 ------------ 319 nihpa Cell reports. Physical science Cell Rep Phys Sci PMC12320893 12320893 1232089
373 ------- 319 nihpa Cell reports. Physical science Cell Rep Phys Sci PMC12320893 12320893 12320893 NIH
[... 3 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 365,572p paper/10.1016-j.xcrp.2025.102660.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
ls claims/ | grep -E "00103|00127"; for d in 001272 001273 001274; do ls claims/$d; head -40 claims/$d/*.yaml; done
```

```
000127
001038
001272
001273
001274
001276
001277
10.1016-j.xcrp.2025.102660.yaml
# Claims for Semenov, Kim, Silkuniene & Pakhomov (2025), Cell Reports Physical Science 6, 102660,
# on dandiset 001272.
# Written by an agent (model "claude-opus-5-5", Claude Code in GitHub Actions), 2026-10-22, under
# docs/protocol.md version pilot-10, as the reader.
#
# Text read. The NIH author manuscript (NIHMS2098259, PMC12320893) as served by Europe PMC, with its
# main text, figure legends and STAR Methods, and the supplement (NIHMS2098259-supplement-1.pdf,
# Figures S1 to S4 and Table S1, the Key Resource Table), all in
# paper/10.1016-j.xcrp.2025.102660.txt. The version of record was not read. No main-text PDF was
# available; the supplement's figures were read from their legends only. Values shown only in
# figures (the traces of Figure S1, the n per group of Figure 2D) are not used.
#
[... 110 more lines not kept]
```

**Agent calls Bash**

```bash
grep -rn -A6 "001271 holds\|001271" claims/001273/*.yaml claims/001272/*.yaml claims/001274/*.yaml | head -40; wc -l claims/00127*/*.yaml
```

```
claims/001273/10.1016-j.xcrp.2025.102660.yaml:40:# code availability) without saying which figure is in which. From their titles only: 001271 holds
claims/001273/10.1016-j.xcrp.2025.102660.yaml-41-# tetrodotoxin (Figure S2), 001272 Di-8-ANEPPS (Figure S1), 001274 sine wave polarization (Figures
claims/001273/10.1016-j.xcrp.2025.102660.yaml-42-# 5, 6, S3), 001030 and 001032 to 001035 the 250-ms and 2-s sine wave stimulation (Figures 1 to 3).
claims/001273/10.1016-j.xcrp.2025.102660.yaml-43-# The paper also lists 001031, which no claim here is assigned to.
claims/001273/10.1016-j.xcrp.2025.102660.yaml-44-# Claims on those are data elsewhere, as read from the titles. The 2-us, 257 V/cm pulse recordings
claims/001273/10.1016-j.xcrp.2025.102660.yaml-45-# of the nine cells of Figures 5 and 6 may be in 001274 or here; the author finds where.
claims/001273/10.1016-j.xcrp.2025.102660.yaml-46-#
--
claims/001273/10.1016-j.xcrp.2025.102660.yaml:398:  where: DANDI:001271 (assigned from its title)
claims/001273/10.1016-j.xcrp.2025.102660.yaml-399-  criterion: Per neuron, sessions before and about 5 min after TTX or vehicle at the same field
claims/001273/10.1016-j.xcrp.2025.102660.yaml-400-    (Figure S2 legend). Reproduced when, in every TTX neuron, APs (as in fig1-pure-sine-excites-all)
claims/001273/10.1016-j.xcrp.2025.102660.yaml-401-    present before are absent after and the mean dF over the last 100 ms of the stimulus is above
claims/001273/10.1016-j.xcrp.2025.102660.yaml-402-    5% before and below it after, while vehicle neurons keep their response. The window and level
claims/001273/10.1016-j.xcrp.2025.102660.yaml-403-    are standard choices.
claims/001273/10.1016-j.xcrp.2025.102660.yaml-404-- id: fig6-sine-less-than-pulse
--
claims/001272/10.1016-j.xcrp.2025.102660.yaml:43:# stimulation at varying frequencies) hold the FluoVolt experiments of Figures 1 to 3, 001271
claims/001272/10.1016-j.xcrp.2025.102660.yaml-44-# tetrodotoxin (Figure S2), 001273 the 2-us pulse kinet
[... 28 more lines not kept]
```

**Agent**

The full text and supplement are present; the paper links no code. Next I'll fetch 001271's title and description from DANDI.

**Agent calls Bash**

```bash
curl -s https://api.dandiarchive.org/api/dandisets/001271/ | python3 -c "import json,sys; d=json.load(sys.stdin); print(json.dumps(d,indent=1)[:1500])"; curl -s "https://api.dandiarchive.org/api/dandisets/001271/versions/draft/info/" | python3 -c "import json,sys; d=json.load(sys.stdin); m=d['metadata']; print(m.get('name')); print(m.get('description')); print(m.get('relatedResource')); print(m.get('keywords'))"
```

Result: the fetched text is not kept.

**Agent**

001271 is the tetrodotoxin experiment (Figure S2). Now I'll read the sibling claims file for 001272, which covers the same kind of fast imaging, so the format stays consistent.

**Agent calls Read**

```json
{
 "file_path": "claims/001272/10.1016-j.xcrp.2025.102660.yaml",
 "offset": 40
}
```

```
40	# The claims on the Figure S1 experiment are data dataset. The paper deposited its raw images in
41	# ten dandisets (Data and code availability) without saying which figure is in which. From their
42	# titles only, 001030 (2-kHz sine waves, effect of the field) and 001032 to 001035 (sine wave
43	# stimulation at varying frequencies) hold the FluoVolt experiments of Figures 1 to 3, 001271
44	# tetrodotoxin (Figure S2), 001273 the 2-us pulse kinetics (Figure 4), 001274 sine wave
45	# polarization (Figures 5, 6, S3); 001031 (100-kHz bipolar pulses) matches no figure. Claims on
46	# those are data elsewhere, and the comparisons of Di-8-ANEPPS with FluoVolt are data with_inputs,
47	# their FluoVolt side taken from 001030 and 001032 to 001035.
48	#
49	# Method details fixed from the paper, used by the Figure S1 criteria.
50	# (F1) F is the mean emission over the entire cell soma per frame, F0 the mean over an interval
51	# before the stimulus, dF = 100% (F - F0)/F0 (Methods, Recording of the optical APs). For
52	# Di-8-ANEPPS the trace is inverted, -dF, so that depolarization is upward (Methods; Figure S1
53	# legend; Results, "APs were identified by the reduction instead of the increase of emission").
54	# The Methods say the scale of "Figure S2" was inverted; that set is the Di-8-ANEPPS one of
55	# Figure S1, whose legend says its traces were inverted, so S2 there is read as S1.
56	# (F2) Traces are not filtered or modified in any way (Methods); no detrending or smoothing.
57	# (F3) The stimulus is a 250-ms, 2-kHz unmodulated sine wave (Figure S1 legend), starting 50 ms
58	# into the session (Methods); the onset and the field strength of each session are taken from the
59	# dataset, and the 50 ms is used when the onset is not given there.
[... 460 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "paper/10.1016-j.xcrp.2025.102660.supp.pdf",
 "pages": "3"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
python3 -c "
import fitz
d=fitz.open('paper/10.1016-j.xcrp.2025.102660.supp.pdf'); p=d[2]
print(p.get_text())
p.get_pixmap(dpi=110).save('$TMPDIR/s2.png')
"; echo $TMPDIR
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
python3 -c "import pypdf" 2>&1; pip list 2>/dev/null | grep -i -E "pdf|mupdf|pillow"; which mutool gs convert magick qpdf
```

```
Exit code 1
Traceback (most recent call last):
  File "<string>", line 1, in <module>
    import pypdf
ModuleNotFoundError: No module named 'pypdf'
```

**Agent calls Bash**

```bash
pip install -q --target $TMPDIR/pylib pymupdf 2>&1 | tail -2; PYTHONPATH=$TMPDIR/pylib python3 -c "
import fitz
d=fitz.open('paper/10.1016-j.xcrp.2025.102660.supp.pdf'); p=d[2]
print(repr(p.get_text()))
p.get_pixmap(dpi=120).save('$TMPDIR/s2.png')
"
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/s2.png"
}
```

Result: no output.

**Agent calls Bash**

```bash
sed -n 1,80p tools/claims_check.py; grep -n "data\b\|'where'\|ALLOWED\|keys" tools/claims_check.py | head -30
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

[... 63 more lines not kept]
```

**Agent calls Bash**

```bash
python3 -c "
import json;s=json.load(open('schemas/claims.schema.json'))
c=s['\$defs'] if '\$defs' in s else s.get('definitions')
print(json.dumps(s,indent=0)[:4000])"
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
[... 120 more lines not kept]
```

**Agent**

Nothing is missing: the main text, STAR Methods and supplement (Figures S1 to S4, Table S1) are all there, and the paper reports no code. Now writing the claims file.

**Agent calls Write**

```json
{
 "file_path": "claims/001271/10.1016-j.xcrp.2025.102660.yaml",
 "content": "# Claims for Semenov, Kim, Silkuniene & Pakhomov (2025), Cell Reports Physical Science 6, 102660,\n# on dandiset 001271.\n# Written by an agent (model \"claude-opus-5-5\", Claude Code in GitHub Actions), 2026-10-22, under\n# docs/protocol.md version pilot-10, as the reader.\n#\n# Text read. The NIH author manuscript (NIHMS2098259, PMC12320893) as served by Europe PMC, with its\n# main text, figure legends and STAR Methods, and the supplement (NIHMS2098259-supplement-1.pdf,\n# Figures S1 to S4 and Table S1, the Key Resource Table), all in\n# paper/10.1016-j.xcrp.2025.102660.txt. The version of record was not read. No main-text PDF was\n# available, so Figures 1 to 6 could not be looked at. Page 3 of the supplement PDF (Figure S2) was\n# looked at to read its layout, as its legend does not give it: three neurons, one vehicle\n# control tested at 45, 63 and 72 V/cm and two TTX neurons tested at 90, 108 and 117 V/cm and at\n# 54, 72 and 81 V/cm, each at the same fields before and after the solution change, with APs at\n# the lower fields and a depolarization with small oscillations at the highest before the change.\n# These values orient the author only; no claim rests on them.\n#\n# Code. The paper states \"This paper does not report original code\". It names the software used:\n# Fiji ImageJ 1.53C or MetaMorph 7.7 for soma emission, Grapher 16 for traces and linear\n# regression, Origin 8.0 for fits, Sim4Life 5.2 for the field, and RStudio in Table S1. No\n# repository was read, so no method detail below is settled by code.\n#\n# Data the paper used. E18 Sprague-Dawley rat hippocampal neurons (BrainBits), cultured about one\n# week on 12-mm coverslips. A single neuron with no apparent somatic contact is centred in the\n# field, with a bipolar tungsten electrode (two 100-um rods, 120-um gap, 45 degrees, tips 50 um\n# above the coverslip) and the neuron centred in the gap. Fast imaging of the optical membrane\n# potential, 64 x 64 pixels after 4 x 4 binning, at 3,130 or 3,086.4 frames/s, 1,200 images per\n# session (50 ms before, 250 ms during and about 90 ms after the stimulus), sessions 20 to 60 s\n# apart, fields escalated or in a random order. F is the emission over the entire soma, F0 its mean\n# before the stimulus, and dF = 100% (F - F0)/F0. Most neurons were stained with FluoVolt and\n# recorded with 250-ms unmodulated or 20-Hz modulated sine waves at 2 and 20 kHz (Figures 1, 2), in\n# NaCl (16.4 mS/cm) or sodium gluconate (8.4 mS/cm) solution (Figure 3A, 3B), with 2-s ramped 2-kHz\n# sine waves (Figure 3C), with Di-8-ANEPPS on eight neurons (Figure S1) and with 1 uM tetrodotoxin\n# (Figure S2). Strobe imaging with 2-us pulses and single sine wave beats measured membrane charging\n# (Figures 4 to 6, S3).\n#\n# This dandiset. Its title and description on DANDI (\"Tetrodotoxin Blockade of Sodium Channels\n# Abolishes Action Potential Formation During Intense Sinewave Stimulation\"; 1 uM TTX \"suppressed\n# action potentials, as expected, and completely prevented sustained depolarization\") match the\n# Figure S2 experiment. As the paper reports it, FluoVolt-stained neurons were stimulated by\n# unmodulated 250-ms, 2-kHz sine waves at several field strengths (V/cm) in the standard NaCl\n# solution, and again about 5 min after the solution was replaced by the same solution with 1 uM\n# TTX (Tocris) or without it (vehicle control). The measured variable is the soma emission per\n# frame; per session, the field strength, the solution (before, TTX, vehicle) and the session\n# order. The paper gives no count of TTX or vehicle neurons; the Methods say representative traces\n# come from at least 4, usually 8 to 15, replications in different cells. The claims on the Figure\n# S2 experiment are data dataset. The paper deposited its raw images in ten dandisets (Data and\n# code availability) without saying which figure is in which. From their titles only, 001030\n# (2-kHz sine waves, effect of the field) and 001032 to 001035 (sine wave stimulation at varying\n# frequencies) hold the FluoVolt experiments of Figures 1 to 3, 001272 Di-8-ANEPPS (Figure S1),\n# 001273 the 2-us pulse kinetics (Figure 4), 001274 sine wave polarization (Figures 5, 6, S3);\n# 001031 (100-kHz bipolar pulses) matches no figure. Claims on those are data elsewhere, and the\n# claims files of 001272, 001273 and 001274 hold fuller criteria for theirs.\n#\n# Method details fixed from the paper, used by the Figure S2 criteria.\n# (F1) F is the mean emission over the entire cell soma per frame, F0 the mean over an interval\n# before the stimulus, dF = 100% (F - F0)/F0 (Methods, Recording of the optical APs). FluoVolt\n# emission rises with depolarization, so traces are not inverted.\n# (F2) Traces are not filtered or modified in any way (Methods); no detrending or smoothing.\n# (F3) The stimulus is a 250-ms, 2-kHz unmodulated sine wave (Figure S2 legend), starting 50 ms into\n# the session (Methods); the onset, the field and the solution of each session are taken from the\n# dataset, and the 50 ms is used when the onset is not given there.\n# (F4) Sessions after the change are those about 5 min after the solution was replaced by TTX or\n# vehicle (Figure S2 legend); the solution of each session is taken from the dataset.\n# (F5) The maximum firing rate of a session is the inverse of the peak-to-peak interval between its\n# first two APs (Methods).\n# (F6) The two-sided Student's t test, paired or unpaired as appropriate, at p < 0.05, is the paper's\n# test where a criterion needs one (Methods, Quantification and statistical analysis). The paper\n# reports no test for Figure S2.\n#\n# Details the paper leaves open, with the readings named. Every Figure S2 criterion runs every\n# combination of the readings below; a claim is decided when all give its outcome, and blocked as\n# methods_underspecified when they give different outcomes.\n# (O1) The soma outline is not given. ROIs are taken from the dataset when it holds them. When it\n# does not, readings (a) the connected component nearest the image centre (the Methods centre the\n# neuron) of an Otsu threshold of the mean pre-stimulus frame, (b) that mask eroded by 2 pixels, to\n# leave out the neurite bases at its edge. Otsu and the 2 pixels are standard choices.\n# (O2) The length of the F0 interval is not given (\"a time interval preceding the electrical\n# stimulation\"); readings (a) all frames before the onset (about 50 ms), (b) the last 20 ms before\n# the onset. This is unlikely to change an outcome.\n# (O3) AP detection is given only as \"brief emission upticks\", in neurons selected for APs above 5%\n# dF lasting about 10 ms (typical 11.3% and 8 ms). An AP is a local maximum of dF with width at half\n# height between 2 and 20 ms (\"about 10 ms\"; the bounds are a standard choice) and at least 5 ms\n# from a larger maximum (standard choice; the paper's highest rates, 60 to 90 Hz, give intervals\n# over 11 ms). Readings of the height (a) above 5% dF (the Methods' selection level), (b) above 5 SD\n# of dF before the onset. After TTX, (a) and (b) are applied with the level of the same neuron's\n# sessions before the change, so that a drop of the baseline noise cannot create APs.\n# (O4) \"Sustained depolarization\" is not defined by a measure. It is no AP in the last 100 ms of the\n# stimulus while the mean dF over that window is above, reading (a) 5 SD of dF before the onset,\n# (b) half the median AP height of the neuron before the change. The 100-ms window is a standard\n# choice. \"Sustained firing\" is, as a standard choice, at least three APs with one in the last 50 ms\n# of the stimulus.\n# (O5) Which session pairs are compared before and after the change is not stated beyond the\n# legend's \"recorded first ... and again\"; readings (a) every field tested both before and after,\n# (b) only the highest field tested both before and after.\nschema_version: 2\ndataset:\n  archive: dandi\n  id: \"001271\"\npaper: doi:10.1016/j.xcrp.2025.102660\nclaims:\n- id: figs2-neurons-tested\n  statement: The tetrodotoxin experiment was replicated in several neurons, with vehicle controls; the\n    representative traces of Figure S2 come from at least 4 independent replications in different\n    cells.\n  source: Figure S2 legend; Methods, Quantification and statistical analysis\n  quote: Representative traces of the optical membrane potentials were selected from at least 4 and\n    usually 8-15 independent replications in different cells\n  expected:\n  - quantity: neurons tested with TTX\n    value: 4\n    tolerance: 0\n    unit: neurons, at least\n  criterion: Neurons are counted from the dataset's subjects, sessions or cell identifiers, each\n    recording counted once (author, step 1), and split into TTX and vehicle by the dataset's\n    session metadata. The paper does not say whether the 4 replications count TTX neurons alone;\n    readings (a) at least 4 TTX neurons, (b) at least 4 neurons over TTX and vehicle together.\n    As a reported number read two ways, reproduced when either reading holds (protocol, step 3).\n    The tolerance is 0 on a lower bound. The number of vehicle neurons is reported; the legend\n    shows one, so at least one vehicle neuron is expected and its absence is reported as a\n    finding.\n- id: figs2-before-firing-then-depolarization\n  statement: Before the drug, unmodulated 2-kHz sine waves evoked repetitive APs at lower fields and,\n    at the most intense fields, a sustained depolarization in which APs merged into small\n    oscillations.\n  source: Results, Tetrodotoxin blocks sustained depolarization, paragraph 1; Results, Stimulation by\n    2- and 20-kHz unmodulated sine waves, paragraph 1; Figure S2\n  quote: The sustained depolarization induced by intense unmodulated sine waves ( Figures 1 and 3 )\n    was immediately reversible upon stimulus cessation\n  inferred: The paper states this pattern for Figures 1 and 3; for the Figure S2 neurons it is shown\n    only in the traces before the change, and the legend's \"abolishes both firing and sustained\n    depolarization\" implies both were present before.\n  criterion: F1 to F3, under O1 to O4, sessions before the change only. Per neuron, the session at its\n    highest field and its sessions at lower fields. Reproduced when every neuron (TTX and vehicle)\n    has APs in some session, and more than half of them (a standard choice; the paper gives no\n    fraction) show sustained depolarization (O4) at their highest field and APs without sustained\n    depolarization at a lower field. The AP count and the maximum firing rate (F5) per session are\n    reported against field.\n- id: figs2-depolarization-reversible\n  statement: The sustained depolarization induced by intense unmodulated sine waves reversed\n    immediately when the stimulus ended, so it was not membrane electroporation, which would take\n    seconds or longer to repair.\n  source: Results, Tetrodotoxin blocks sustained depolarization, paragraph 1\n  quote: The sustained depolarization induced by intense unmodulated sine waves ( Figures 1 and 3 )\n    was immediately reversible upon stimulus cessation. It was not related to membrane\n    electroporation, which would take seconds or longer to repair\n  depends_on:\n  - figs2-before-firing-then-depolarization\n  criterion: F1 to F3, under O1 to O4, all sessions with sustained depolarization (O4), before the\n    change and in vehicle neurons. \"Immediately\" is not quantified; readings of the window after\n    the stimulus (a) 10 to 40 ms after its end, (b) the last 40 ms of the recording (the Methods\n    give about 90 ms after the stimulus). Reproduced when, in every such session, the mean dF in\n    the window is below the O4 level of that reading. A further check, from the paper's \"seconds or\n    longer\", is that F0 of the next session of the same neuron (20 to 60 s later) is within 10%\n    (a standard choice) of the F0 of the session before; it is reported, not judged. Windows are\n    standard choices; the claim is tested on the Figure S2 neurons, while the paper's sentence\n    cites Figures 1 and 3.\n- id: figs2-ttx-abolishes-aps\n  statement: 1 uM tetrodotoxin abolished the APs evoked by unmodulated 250-ms, 2-kHz sine waves.\n  source: Results, Tetrodotoxin blocks sustained depolarization, paragraph 1; Figure S2 legend\n  quote: the inhibition of sodium channels with 1 μM tetrodotoxin not only abolished the APs\n  depends_on:\n  - figs2-before-firing-then-depolarization\n  criterion: F1 to F4, under O1 to O3 and O5. Per TTX neuron, session pairs at the same field before\n    and after TTX. Reproduced when, in every TTX neuron, no AP is detected in any session after\n    TTX at a field where APs were detected before; not reproduced when any such session has an\n    AP. The AP counts before and after per pair are reported.\n- id: figs2-ttx-blocks-sustained-depolarization\n  statement: Tetrodotoxin also fully blocked the sustained depolarization caused by intense sine\n    waves, consistent with the depolarization arising from repeated activation of voltage-gated\n    sodium channels by the cycling de- and hyperpolarization of the membrane.\n  source: Results, Tetrodotoxin blocks sustained depolarization, paragraph 1; Figure S2 legend\n  quote: Consistent with this hypothesis, the inhibition of sodium channels with 1 μM tetrodotoxin not\n    only abolished the APs but also fully blocked the sustained depolarization\n  depends_on:\n  - figs2-before-firing-then-depolarization\n  criterion: F1 to F4, under O1, O2, O4 and O5. Per TTX neuron, the session pairs at the same field\n    where sustained depolarization (O4) was present before TTX. Reproduced when, in every such pair,\n    sustained depolarization is absent after TTX, and the mean dF over the last 100 ms of the\n    stimulus after TTX is below the O4 level. \"Fully\" is read as that level; the mean dF over the\n    window before and after is reported per pair, with a two-sided paired t test (F6) over pairs\n    shown as a variant, not judged. Blocked (other) when no TTX neuron has sustained depolarization\n    before TTX.\n- id: figs2-vehicle-keeps-response\n  statement: In vehicle controls, recorded about 5 min after the solution was replaced by the same\n    solution without TTX, the firing and sustained depolarization persisted.\n  source: Figure S2 legend; Methods, Quantification and statistical analysis\n  inferred: No sentence states the vehicle result. The Figure S2 legend says the neurons were recorded\n    again after replacement by the same solution \"with 1 μM TTX or without it (vehicle control)\",\n    the Methods list \"vehicle controls in experiments with tetrodotoxin\", and the legend's title\n    attributes the loss of firing and depolarization to TTX, which implies the vehicle neurons kept\n    them; Figure S2 shows this in one neuron.\n  depends_on:\n  - figs2-before-firing-then-depolarization\n  criterion: F1 to F4, under O1 to O5. Per vehicle neuron, session pairs at the same field before and\n    after the change. Reproduced when, in every vehicle neuron, every pair with APs before has APs\n    after, and every pair with sustained depolarization (O4) before has it after. AP counts and\n    the maximum firing rate (F5) per pair are reported; the paper does not say whether the response\n    must be unchanged, so a decline is reported, not judged. Blocked (other) when the dataset holds\n    no vehicle neuron.\n- id: ap-amplitude-duration\n  statement: Neurons were selected for APs peaking above 5% dF and lasting about 10 ms; typical APs\n    were 11.3% dF high and 8 ms long, excluding the afterhyperpolarization.\n  source: Methods, Recording of the optical APs and data analyses\n  quote: we selected neurons whose APs peaked at a more than 5% Δ F and lasted about 10 ms (typical\n    values; 11.3% ± 0.9% Δ F and 8 ± 0.7 ms duration, excluding afterhyperpolarization; mean ± SEM,\n    n = 22)\n  expected:\n  - quantity: mean AP peak over neurons\n    value: 11.3\n    tolerance: 0.9\n    unit: percent dF\n  - quantity: mean AP duration over neurons\n    value: 8\n    tolerance: 0.7\n    unit: ms\n  criterion: F1 and F2, under O1 to O3, sessions before the change. The paper does not say which 22\n    neurons these are or which experiments they come from; the neurons of this dataset are tested\n    as neurons the same selection was applied to, and a mismatch may come from that. Per neuron,\n    the mean peak dF and duration of its APs. Which APs are measured is not given; readings (a) all\n    APs before the change, (b) the first AP of each session, which is not merged with others. The\n    duration measure is not given; readings (a) width at half height, (b) time from the rise to\n    the return to F0 on the decay, ending at the first crossing of F0 (so the afterhyperpolarization\n    is left out). Reproduced when the means over neurons are within the paper's SEM under every\n    reading; partially reproduced when every neuron has APs above 5% dF and lasting 2 to 20 ms\n    (O3) but a mean falls outside. The number of neurons with APs above 5% is reported.\n- id: fig1-pure-sine-excites-all\n  statement: Unmodulated 250-ms sine waves at 2 and 20 kHz excited every neuron tested, with APs\n    100 to 200 ms after onset near threshold, firing rate rising to a ceiling of 60 to 90 Hz, and\n    sustained depolarization at the highest fields.\n  source: Results, Stimulation by 2- and 20-kHz unmodulated sine waves, paragraph 1; Figures 1A to 1C\n    and inset\n  quote: Pure sine waves at 2 and even 20 kHz excited 100% of neurons ... at near-threshold electric\n    field strengths, isolated APs emerged with a delay of 100-200 ms after the sine wave onset ...\n    The maximum firing rate increased linearly until reaching a ceiling of 60-90 Hz\n  data: elsewhere\n  where: DANDI:001030 and 001032 to 001035 (assigned from their titles; the paper does not map\n    figures to dandisets)\n  expected:\n  - quantity: fraction of neurons excited\n    value: 100\n    tolerance: 10\n    unit: percent\n  criterion: F1 to F3, F5, O1 to O4 of the header, for FluoVolt sessions of unmodulated sine waves.\n    A neuron's threshold is the lowest field of a session with at least one AP during the\n    stimulus (Figure 2D legend). Reproduced when, under every reading, at least 90% of neurons\n    are excited at each frequency, the median over neurons of the highest maximum firing rate lies\n    within 54 to 99 Hz (60 to 90 Hz widened by 10% of each bound) and the median first-AP latency\n    at threshold lies within 90 to 220 ms (100 to 200 ms widened the same way). Whether the\n    ceiling is meant for the median neuron or every neuron is open (the inset shows three); both\n    are reported and the median decides. Sustained depolarization (O4) at the highest field is\n    reported, not judged, as the paper gives no fraction of neurons.\n- id: fig1-20khz-needs-twice-the-field\n  statement: All excitation thresholds at 20 kHz were about 2-fold higher than at 2 kHz.\n  source: Results, Excitation thresholds are similar or lower for pure 2- and 20-kHz sine waves than\n    those for modulated sine waves, paragraph 1; Figure 2D\n  quote: All thresholds at 20 kHz were about 2-fold higher than at 2 kHz ( p < 0.0001, two-tailed\n    unpaired t test)\n  statistics:\n  - about: 20 kHz against 2 kHz, all thresholds\n    test: two-tailed unpaired t test\n    p: 0.0001\n    p_relation: \"<\"\n  data: elsewhere\n  where: DANDI:001032 to 001035 (assigned from their titles)\n  expected:\n  - quantity: ratio of mean 20-kHz to mean 2-kHz threshold, each stimulus and AP count\n    value: 2\n    tolerance: 0.2\n  criterion: Thresholds for at least 1 and at least 5 APs during the 250-ms stimulus (Figure 2D\n    legend), from the threshold search of the Methods (5% to 10% steps), with the AP readings of\n    the header. The paper gives one p over \"all thresholds\"; readings (a) one test per stimulus\n    (modulated or not) and AP count, each p < 0.0001, (b) one test pooling the four. Reproduced\n    when each ratio is within tolerance and 20 against 2 kHz reaches p < 0.0001 under every\n    reading; blocked as methods_underspecified when they disagree.\n- id: fig2d-modulated-thresholds-higher\n  statement: Thresholds for sine waves modulated at 20 Hz were significantly higher than for pure\n    sine waves at the same carrier, for 5 APs at 2 kHz and for 1 and 5 APs at 20 kHz, so modulation\n    did not lower excitation thresholds; the 2-kHz unmodulated 1-AP threshold was 57.7 V/cm.\n  source: Results, Excitation thresholds are similar or lower for pure 2- and 20-kHz sine waves than\n    those for modulated sine waves, paragraph 1; Figure 2D; Results, Asymmetric and less-efficient\n    membrane charging, last paragraph\n  quote: thresholds for modulated sine waves, which emulate the TI stimulus at the target, were\n    significantly higher than those for pure sine waves at the same frequency ... p = 0.0079 ...\n    p = 0.0142 and p = 0.0037\n  statistics:\n  - about: modulated against unmodulated, 2 kHz, 5 APs\n    test: two-tailed unpaired t test\n    p: 0.0079\n  - about: modulated against unmodulated, 20 kHz, 1 AP\n    test: two-tailed unpaired t test\n    p: 0.0142\n  - about: modulated against unmodulated, 20 kHz, 5 APs\n    test: two-tailed unpaired t test\n    p: 0.0037\n  data: elsewhere\n  where: DANDI:001032 to 001035 (assigned from their titles)\n  expected:\n  - quantity: mean unmodulated 2-kHz 1-AP threshold\n    value: 57.7\n    tolerance: 3.6\n    unit: V/cm\n  criterion: Thresholds as in fig1-20khz-needs-twice-the-field. Two-tailed unpaired t tests, as the\n    Figure 2D legend names them. Reproduced when the three modulated thresholds are higher with\n    p < 0.05 (Methods), the 1-AP threshold at 2 kHz is not lower for modulated waves at p < 0.05, and\n    the mean 2-kHz unmodulated 1-AP threshold is within the paper's SEM, under every AP reading;\n    blocked as methods_underspecified when they disagree.\n- id: fig2-modulated-locks-to-beats\n  statement: With 20-Hz modulation, firing above threshold locked to the beats, one AP near the peak\n    of each of the five beats and at most two per beat (ten in all), and modulated sine waves\n    triggered no sustained firing or sustained depolarization.\n  source: Results, Stimulation by 2- and 20-kHz sinusoids modulated at 20 Hz, paragraph 1; Figures 2A\n    and 2B\n  quote: single APs emerged near the peak of each beat, so the firing rate equaled the modulation\n    rate ... the maximum number of APs evoked by five beats was limited to ten. Unlike pure sine\n    waves, modulated stimuli did not trigger sustained firing or sustained depolarization\n  data: elsewhere\n  where: DANDI:001032 to 001035 (assigned from their titles)\n  criterion: AP readings of the header, modulated sessions only. The 250-ms wave holds five 50-ms\n    beats (Results), and modulated waves begin and end at minimal amplitude (Methods, Pulsed laser\n    fluorescence microscopy), so each beat peaks 25 ms into it; the dataset's stimulus record is\n    used instead when it gives the envelope. The paper does not quantify \"near the peak\"; as\n    standard choices, reproduced when no session has more than 10 APs, in sessions with 5 APs or\n    more most APs fall within 12.5 to 37.5 ms of each 50-ms beat, and no session shows sustained\n    firing or sustained depolarization (O4).\n- id: fig2c-pure-more-aps\n  statement: In the same neuron at the same field strength, pure sine waves triggered more APs than\n    modulated ones, and the threshold was typically lower for unmodulated signals.\n  source: Results, Stimulation by 2- and 20-kHz sinusoids modulated at 20 Hz, paragraph 2; Figures 2A\n    to 2C\n  quote: the threshold was typically lower for unmodulated signals ( Figures 2A - 2C ). At the same\n    field strengths, pure sine waves triggered a larger number of APs\n  data: elsewhere\n  where: DANDI:001032 to 001035 (assigned from their titles)\n  criterion: AP readings of the header. Pairs are a neuron's modulated and unmodulated sessions at the\n    same carrier and field. The paper reports no test; reproduced when the unmodulated count is\n    larger in more pairs than the reverse, and the unmodulated threshold lower in more neurons than\n    the reverse, under every reading. A two-sided paired t test (F6) of the counts is reported.\n- id: fig3b-low-conductivity-halves-threshold\n  statement: Lowering solution conductivity from 16.4 to 8.4 mS/cm with sodium gluconate reversibly\n    lowered excitation thresholds about 2-fold at all sine wave frequencies from 2 to 20 kHz.\n  source: Results, Decreased extracellular conductivity lowers excitation thresholds, paragraph 1;\n    Figures 3A and 3B\n  quote: Switching to the NaGlu-based solution reversibly and reproducibly decreased excitation\n    thresholds ~2-fold across all sine wave frequencies tested\n  data: elsewhere\n  where: DANDI:001030 and 001032 to 001035 (assigned from their titles)\n  expected:\n  - quantity: ratio of NaCl to NaGlu mean 1-AP threshold, each frequency\n    value: 2\n    tolerance: 0.2\n  criterion: 1-AP thresholds for 250-ms unmodulated sine waves per frequency and solution, 4 to 8\n    neurons per point (Figure 3B legend), AP readings of the header. Reproduced when the ratio is\n    within tolerance at every frequency under every reading.\n- id: fig3-not-heating\n  statement: Excitation by pure sine waves was not caused by heating; the adiabatic temperature rise\n    was 2.5 C after 250 ms at 63 V/cm in NaCl solution, at most 1.24 C for the same stimulus in\n    the low-conductivity solution, and 4.1 C at 81 V/cm in NaCl.\n  source: Results, Decreased extracellular conductivity lowers excitation thresholds, paragraph 2;\n    Figure 3A\n  quote: the maximum theoretical temperature rise (assuming no heat dissipation 43 ) was 2.5°C after\n    250 ms of near-threshold stimulation at 2 kHz, 63 V/cm, in the NaCl-based solution ... These\n    observations prove that excitation by pure sine waves was not caused by heating\n  data: elsewhere\n  where: DANDI:001030 or 001032 to 001035 for the Figure 3A responses (assigned from their titles);\n    the temperatures are calculated from the field, duration and conductivity, not measured\n  expected:\n  - quantity: adiabatic rise, 63 V/cm, 250 ms, 16.4 mS/cm\n    value: 2.5\n    tolerance: 0.25\n    unit: degrees C\n  - quantity: adiabatic rise, 63 V/cm, 250 ms, 8.4 mS/cm\n    value: 1.24\n    tolerance: 0.124\n    unit: degrees C\n  - quantity: adiabatic rise, 81 V/cm, 250 ms, 16.4 mS/cm\n    value: 4.1\n    tolerance: 0.41\n    unit: degrees C\n  criterion: The rise is sigma E^2 t over the volumetric heat capacity (reference 43, cited for the\n    adiabatic assumption). The paper does not give the heat capacity or whether E is the peak or\n    the RMS field; readings (a) peak, (b) RMS, each with the heat capacity of water (4.18 J per\n    cm3 per K, a standard choice). Reproduced when all three are within tolerance under a reading;\n    since these are calculated numbers read two ways, that reading is reported. That the Figure 3A\n    neuron fired at 63 V/cm in NaGlu as at 81 V/cm in NaCl is tested as in\n    fig3b-low-conductivity-halves-threshold.\n- id: fig3c-sustained-firing-2s\n  statement: In the low-conductivity solution, a 2-s unmodulated 2-kHz sine wave ramped over 250 ms\n    evoked firing for its whole duration, rising with field until replaced by a firing block with\n    sustained depolarization.\n  source: Results, Decreased extracellular conductivity lowers excitation thresholds, paragraph 3;\n    Figure 3C\n  quote: we observed sustained firing for the entire duration of the sine wave ( Figure 3C ). The rate\n    of firing increased with the electric field strength until it was replaced by a firing block\n    and sustained depolarization\n  data: elsewhere\n  where: DANDI:001030 (assigned from its title)\n  criterion: Traces corrected for bleaching by subtracting a trace without APs (Methods); AP readings\n    of the header. Reproduced when an intermediate field has APs in the last 250 ms of the stimulus,\n    the AP count rises with field up to some field, and the highest field shows sustained\n    depolarization (O4, over the last 250 ms of the stimulus). The windows are standard choices.\n- id: figs1-di8-same-as-fluovolt\n  statement: With Di-8-ANEPPS in place of FluoVolt, in eight neurons, the effects of 2-kHz sine waves\n    were not different, so the excitation by unmodulated sine waves is not a sensitization by\n    FluoVolt.\n  source: Results, Sensitivity to unmodulated sine waves was not caused by FluoVolt dye, paragraph 1;\n    Figure S1\n  quote: Experiments were performed on eight neurons using different electric field strengths tested\n    in a random sequence ... Overall, stimulation effects were not different from those observed\n    with FluoVolt dye\n  data: elsewhere\n  where: DANDI:001272 (assigned from its title)\n  criterion: As in the claims file for DANDI:001272 (figs1-eight-neurons and\n    figs1-effects-same-as-fluovolt), which tests this finding on its own data.\n- id: fig4-pooled-time-constants\n  statement: Membrane charging by 2-us pulses is fast; pooled over 19 experiments, charging and\n    discharging time constants averaged 0.7 and 0.91 us at the cathodic pole and 0.65 and 0.8 us at\n    the anodic pole, so membranes charge fully within each sine wave cycle up to 100 to 200 kHz.\n  source: Results, Kinetics of membrane charging by pulsed electric fields, the paragraph after the\n    Figure 4 legend; Figures 4D and 4E\n  quote: The time constants pooled together for all cells averaged 0.7 ± 0.08 (charging) and 0.91 ±\n    0.08 (discharging) μs for the cathodic cell pole and 0.65 ± 0.05 and 0.8 ± 0.07 μs for the\n    anodic pole, respectively (mean ± SEM, n = 19)\n  data: elsewhere\n  where: DANDI:001273 (assigned from its title)\n  expected:\n  - quantity: charging tau, cathodic pole\n    value: 0.7\n    tolerance: 0.08\n    unit: us\n  - quantity: discharging tau, cathodic pole\n    value: 0.91\n    tolerance: 0.08\n    unit: us\n  - quantity: charging tau, anodic pole\n    value: 0.65\n    tolerance: 0.05\n    unit: us\n  - quantity: discharging tau, anodic pole\n    value: 0.8\n    tolerance: 0.07\n    unit: us\n  criterion: Fits and readings as in the claims file for DANDI:001273 (fig4-pooled-time-constants),\n    which tests this claim on its own data; tolerances are the paper's SEMs.\n- id: fig4-orientation-and-poles\n  statement: Aligning elongated cells with the field doubled the time constants; the maximum optical\n    TMP and the time constants did not differ between the cathode- and anode-facing poles; and\n    discharging was slower than charging except in elongated cells aligned with the field.\n  source: Results, Kinetics of membrane charging by pulsed electric fields, the paragraph after the\n    Figure 4 legend; Figures 4D and 4E\n  quote: Δ F max did not differ at the cathodic and anodic cell poles, indicating the lack of\n    rectification of the applied electric field ... Aligning elongated cells with the electric\n    field doubled the time constants ... discharging time constants were always larger than the\n    charging ones in the same cell ( p < 0.001, paired t test)\n  statistics:\n  - about: elongated cells, parallel against perpendicular\n    test: paired t test\n    p: 0.001\n    p_relation: \"<\"\n  - about: elongated parallel against random cells\n    test: unpaired t test\n    p: 0.01\n    p_relation: \"<\"\n  - about: discharging against charging tau\n    test: paired t test\n    p: 0.001\n    p_relation: \"<\"\n  data: elsewhere\n  where: DANDI:001273 (assigned from its title)\n  criterion: As in the claims file for DANDI:001273 (fig4-orientation-time-constants,\n    fig4-no-pole-difference and fig4-discharging-slower), which tests each part on its own data;\n    reproduced when all three are reproduced there. The Figure 4 legend gives other bounds and\n    test types for these comparisons (p < 0.01, paired two-tailed, charging against\n    discharging; p < 0.01, unpaired two-tailed, between orthogonal orientations); the statistics\n    above are the Results'.\n- id: fig6-sine-less-than-pulse\n  statement: FluoVolt sensitivity to 2-kHz sine waves (11.8% per 1 kV/cm) was 42% of that to 2-us\n    pulses (28% per 1 kV/cm) and smaller in every ROI, with sine waves polarizing the two poles more\n    asymmetrically than pulses.\n  source: Results, Asymmetric and less-efficient membrane charging by sine waves compared to pulses,\n    paragraphs 2 to 5; Figures 5, 6B to 6D and S3\n  quote: All numbers were invariably smaller than those measured for the same ROIs with the pulse (\n    Figure 6D ). The electric field sensitivity averaged across all ROIs in all the cells was 11.8% ±\n    1.7% per 1 kV/cm, just 42% of the value for the 2-μs pulses\n  data: elsewhere\n  where: DANDI:001274 (assigned from its title)\n  expected:\n  - quantity: mean pulse sensitivity over the 18 ROIs\n    value: 28\n    tolerance: 2.5\n    unit: percent per kV/cm\n  - quantity: mean sine wave sensitivity over the 18 ROIs\n    value: 11.8\n    tolerance: 1.7\n    unit: percent per kV/cm\n  - quantity: mean sine over mean pulse sensitivity\n    value: 42\n    tolerance: 4.2\n    unit: percent\n  criterion: Measures and readings as in the claims file for DANDI:001274 (fig6b-pulse-sensitivity,\n    fig6c-sine-sensitivity, fig6d-sine-less-than-pulse, fig5-sine-asymmetry-c7 and\n    figs3-sine-asymmetry-c8), which tests this finding on its own data; tolerances are the paper's\n    SEMs, and 10% for the ratio.\n- id: threshold-depolarization-estimate\n  statement: The 2-kHz AP threshold of 57.7 V/cm times the sine wave sensitivity gives a 0.68%\n    emission change, about 6.8 mV, so the threshold depolarization is 5 to 15 mV, as with\n    intracellular current injection.\n  source: Results, Asymmetric and less-efficient membrane charging by sine waves compared to pulses,\n    last paragraph\n  quote: This threshold corresponds to a 0.68% ± 0.11% FluoVolt emission change (11.8 × 57.7/1,000)\n    ... a 0.68% emission change corresponds to a 6.8-mV depolarization at the AP threshold\n  data: elsewhere\n  where: DANDI:001032 to 001035 for the threshold and DANDI:001274 for the sensitivity (assigned from\n    their titles)\n  depends_on:\n  - fig2d-modulated-thresholds-higher\n  - fig6-sine-less-than-pulse\n  expected:\n  - quantity: emission change at the 2-kHz AP threshold\n    value: 0.68\n    tolerance: 0.11\n    unit: percent\n  - quantity: depolarization at the 2-kHz AP threshold\n    value: 6.8\n    tolerance: 1.1\n    unit: mV\n  criterion: Mean sine sensitivity of fig6-sine-less-than-pulse times the mean unmodulated 2-kHz 1-AP\n    threshold of fig2d-modulated-thresholds-higher, divided by 1,000, and that times 10 mV per 1%\n    (the calibration of reference 47 as the paper uses it). Tolerances are the paper's, the last\n    being 0.11% times 10 mV per 1%. Reproduced when both are within tolerance.\n"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001271/10.1016-j.xcrp.2025.102660.yaml",
 "old_string": "10 ms (typical\n    values; 11.3% ± 0.9% Δ F and 8 ± 0.7 ms duration, excluding afterhyperpolarization; mean ± SEM,\n    n = 22)",
 "new_string": "10 ms (typical\n    values ... 11.3% ± 0.9% Δ F and 8 ± 0.7 ms duration, excluding afterhyperpolarization ... mean ±\n    SEM, n = 22)"
}
```

```
The file claims/001271/10.1016-j.xcrp.2025.102660.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
python tools/claims_check.py claims/001271/10.1016-j.xcrp.2025.102660.yaml paper/10.1016-j.xcrp.2025.102660.txt; grep -n " — \|rather" claims/001271/*.yaml
```

Result: not kept, because it reads the paper's text.

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001271/10.1016-j.xcrp.2025.102660.yaml",
 "old_string": "    2- and 20-kHz unmodulated sine waves, paragraph 1; Figure S2\n  quote: The sustained depolarization induced by intense unmodulated sine waves ( Figures 1 and 3 )\n    was immediately reversible upon stimulus cessation\n  inferred: The paper states this pattern for Figures 1 and 3; for",
 "new_string": "    2- and 20-kHz unmodulated sine waves, paragraph 1; Figure S2\n  inferred: The paper states this pattern for Figures 1 and 3 (\"At the highest field strengths,\n    multiple APs coalesced into low-amplitude oscillations on top of a continuous depolarization\");\n    for"
}
```

```
The file claims/001271/10.1016-j.xcrp.2025.102660.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
python tools/claims_check.py claims/001271/10.1016-j.xcrp.2025.102660.yaml paper/10.1016-j.xcrp.2025.102660.txt; python3 -c "
import yaml;d=yaml.safe_load(open('claims/001271/10.1016-j.xcrp.2025.102660.yaml'))
c=d['claims'];print(len(c),sum('quote' in x for x in c),sum('statistics' in x for x in c),sum('criterion' in x for x in c),sum('inferred' in x for x in c),[x['id'] for x in c if x.get('data','dataset')=='dataset'])"
```

Result: not kept, because it reads the paper's text.

**Agent**

I wrote `claims/001271/10.1016-j.xcrp.2025.102660.yaml`, and the quote checker passes it: 20 claims, 18 quotes, 7 statistical values, 0 problems. Nothing is committed.

**Text read.** I read the NIH author manuscript (NIHMS2098259, PMC12320893) as served by Europe PMC: main text, figure legends and STAR Methods. I also read the supplement (Figures S1 to S4 and Table S1). I did not read the version of record. There was no main-text PDF, so Figures 1 to 6 were never seen. I opened page 3 of the supplement PDF only to see how Figure S2 is laid out: one vehicle neuron and two TTX neurons, each tested at the same fields before and after the change. No claim rests on what I read there. The paper says it reports no original code, so no repository was read.

**This dandiset.** Its DANDI title and description match the tetrodotoxin experiment of Figure S2. The paper deposited its data in ten dandisets without saying which figure is in which, so the other dandisets were assigned from their titles only.

**Claims.**
- **Tested on this dandiset (7):** how many neurons were tested; firing and then sustained depolarization before the drug; the depolarization reversing when the stimulus ends; TTX abolishing the APs; TTX blocking the sustained depolarization; vehicle neurons keeping their response; AP height and duration (11.3% ΔF and 8 ms).
- **Tested elsewhere (13):** the main findings of Figures 1 to 4, 6 and S1, the heating calculation, and the threshold estimate of 6.8 mV, each pointing to the dandiset its title suggests. For the Figure S1, 4 and 6 claims, the criteria defer to the existing claims files for 001272, 001273 and 001274.
- **Quotes:** 18 of 20 have one. The other two carry a note saying they are read from the figure, because no sentence states them: the pre-drug firing and depolarization pattern in the Figure S2 neurons, and the vehicle result.
- **Statistics:** 3 claims carry the paper's tests (7 values in all). The paper reports no test for Figure S2.
- **Criteria:** all 20 have one.

**Details the paper leaves open, and the readings named:**
- **O1, soma outline:** use the dataset's ROI; if it has none, (a) an Otsu mask of the component nearest the image centre, or (b) that mask eroded by 2 pixels.
- **O2, baseline (F0) window:** (a) all frames before the stimulus, or (b) the last 20 ms before it.
- **O3, AP detection height:** (a) above 5% ΔF, or (b) above 5 SD of the pre-stimulus trace. After TTX, the level is taken from the same neuron's sessions before the drug. The width bounds (2 to 20 ms) are a standard choice.
- **O4, sustained depolarization:** no AP in the last 100 ms of the stimulus while the mean ΔF there is above (a) 5 SD of the baseline, or (b) half the neuron's median AP height.
- **O5, which sessions are compared before and after:** (a) every field tested both times, or (b) only the highest such field.
- **"Immediately reversible":** the ΔF window after the stimulus is (a) 10 to 40 ms after it ends, or (b) the last 40 ms of the recording.
- **Neuron count:** "at least 4 replications" counts (a) TTX neurons only, or (b) TTX and vehicle neurons together.
- **Which 22 neurons the AP height and duration come from:** the paper does not say. Readings: (a) all APs or (b) only each session's first AP; duration as (a) half-height width or (b) time from rise back to F0.
- **Heating formula:** the field is (a) peak or (b) RMS, with the heat capacity of water as a standard choice.
- **Fractions such as "more than half":** the paper gives none, so these thresholds are labelled as standard choices.

**Missing from the paper:**
- No count of TTX or vehicle neurons.
- No sentence stating the vehicle result.
- No mapping of figures to dandisets.
- No source for the 22 neurons behind the typical AP values.
- No formula for the temperature rise.
- No code.

## End of run

25 turns, 4 minutes, result: success.
