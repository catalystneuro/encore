# fedele-2017 · claims · run 42687110517

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cat docs/protocol.md; ls paper/ | grep -i fedele; cat claims/fouke-2025.yaml
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
grep -n "^#" docs/protocol.md | head -60; ls paper/ | grep -i fedele
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
ls paper/ | head -50; ls paper | wc -l
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cat claims/fouke-2025.yaml | head -150; wc -c paper/*.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1038-s41598-017-13064-1.txt"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd paper; grep -n "Patient\|ILAE\|Table\|Figure\|^[A-Za-z].\{40,\}" 10.1038-s41598-017-13064-1.txt | awk -F: '$1>1176' | head -80; tail -40 10.1038-s41598-017-13064-1.txt
```

```
1213:Patient 4
1214:ILAE 1
1315:Patient 5
1316:ILAE 1
1417:Patient 6
1418:ILAE 1
1519:Patient 7
1520:ILAE 3
1621:Patient 8
1622:ILAE 3
1723:Patient 9
1724:ILAE 5
1825:Patient 10
1826:ILAE 1
1971:Patient 11
1972:ILAE 1
2256:Patient 12
2257:ILAE 1
2414:Patient 13
2415:ILAE 1
[... 54 more lines not kept]
```

**Agent**

Main text, Methods and supplement (Table S1) are all present. Next: the dataset description and the linked code.

**Agent calls Bash**

```bash
cat paper/ieeg-1.data-description.txt; ls papers/datasets/ | grep fedele; cat papers/datasets/fedele-2017.yaml 2>/dev/null
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  grep -n "with_labels\|with_inputs\|elsewhere" docs/*.md | head -30; ls claims | head -50; ls tools
```

```
docs/design.md:118:  elsewhere. This is the guard against a result that only looks right.
docs/pilot-notes.md:95:  with outside data (`data: dandiset` or `with_inputs`), and the dashboard
docs/pilot-notes.md:107:RDMs that are not public, are now marked `with_inputs`, and its attempt
docs/pilot-notes.md:123:  `data: with_labels`, for outside sources that only name or map codes the
docs/pilot-notes.md:162:adds a fourth data kind, `elsewhere`, for a claim whose data the dandiset
docs/pilot-notes.md:166:dandiset's claims and from `with_inputs` claims. It is never blocked with
docs/pipeline.md:49:`other_data` (a research paper whose data are elsewhere; `data_in` says where),
docs/pipeline.md:68:aside, are mostly on data elsewhere stops the chain before its checkpoint.
docs/protocol.md:149:     `with_labels`, `with_inputs` or `elsewhere` (step 4, and author, step
docs/protocol.md:156:     rests on it. A claim on data in none of them is `data: elsewhere`, or
docs/protocol.md:227:4. Decide what comes from outside the dataset. Data from elsewhere may be
docs/protocol.md:236:     `data: with_labels`, `data: with_inputs` or `data: elsewhere`. The
docs/protocol.md:237:     `with_inputs` and `elsewhere` claims are counted apart, each group on
docs/protocol.md:239:   - `with_labels` is for outside sources that only name or map codes the
docs/protocol.md:261:   - `elsewhere` is for a claim whose data the dataset does not hold at
docs/protocol.md:270:   - The notes of a `with_inputs` claim say which side a difference comes
docs/protocol.md:281:     `data: elsewhere` instead (step 4).
amjad-2025.yaml
armstrong-2026.yaml
ashworth-2025.yaml
[... 81 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "docs/protocol.md",
 "offset": 225,
 "limit": 60
}
```

```
225	   why in the notebook's header. If versions differ in content the analysis
226	   uses, show the difference.
227	4. Decide what comes from outside the dataset. Data from elsewhere may be
228	   used only when the claims file says the paper relies on it, it is public,
229	   and it is pinned: a DOI, or a repository at a commit. Record each under
230	   `inputs` in the attempt. A claim whose outside input is not public is
231	   blocked with `data_missing`, and its notes say where you looked.
232	
233	   The registry judges the dataset, so claims that use outside data are
234	   kept apart:
235	   - Each claim says what its test uses: `data: dataset` (the default),
236	     `data: with_labels`, `data: with_inputs` or `data: elsewhere`. The
237	     `with_inputs` and `elsewhere` claims are counted apart, each group on
238	     its own; the others count towards what is said about the dataset.
239	   - `with_labels` is for outside sources that only name or map codes the
240	     dataset already holds, such as stimulus names for its stimulus codes.
241	     They bring in no measurements. A link claim must confirm the names, and
242	     the missing names are recorded as a finding (`metadata_insufficient`).
243	   - When outside data has to be matched to the dataset's cells, sessions
244	     or subjects, a claim of its own (`kind: link`) tests the link. Link
[... 40 more lines not kept]
```

**Agent calls Bash**

```bash
cd  head -80 claims/fedele-2020.yaml; grep -n "data:" claims/fedele-2020.yaml claims/boran-2019.yaml | sort | uniq -c | head; sed -n 150,400p claims/fouke-2025.yaml | grep -n "checks\|kind\|where\|code:" | head
```

```
# Claims for Fedele, Tzovara et al. (2020), NeuroImage 213, 116705, on dandiset 000576.
# Written by an agent (model "claude-opus-5-5", Claude Code in GitHub Actions), 2026-10-23,
# protocol pilot-10 as stated in docs/protocol.md.
#
# Text read: the version of record (PDF supplied by a person, text extracted with PyMuPDF),
# main text, figure legends, Tables 1 and 2 and Methods. Table 2 was read from the extracted
# text, in which minus signs print as a replacement glyph; its signs agree with the counts the
# Results give (12 of 14 negative DELTA MI, HGP MI positive in 7 of 7 nSOZ and negative in 6 of
# 7 SOZ amygdalae). The PDF pages could not be rendered here. The supplement (Appendix A, online)
# was not supplied; the text cites it only for Fig. S2 (waveforms and inter-spike intervals of
# the neurons of each patient), which carries no finding. The Results also cite "Methods 7.8"
# for the other spectral bands; no such section exists in the text, and section 4.8 lists the
# bands without results.
# The data descriptor of the same data (Fedele et al. 2021, Sci Data, doi:10.1038/s41597-020-00790-x,
# in paper/) was read for the layout of the deposited data only; no claim is taken from it.
#
# Code: the paper links no analysis code. The data descriptor says scripts for reading the NIX
# files and for its own Figs 2 and 3 come with the G-Node and OpenNeuro deposits; these are not
# the paper's analysis and were not read. Every method below is from the paper's Methods (4.7
# to 4.11), Results and figure legends.
[... 67 more lines not kept]
```

**Agent**

Now the code the paper links (HFO-detect-matlab).

**Agent calls Bash**

```bash
cd $TMPDIR && git clone -q https://github.com/HFO-detect/HFO-detect-matlab.git && cd HFO-detect-matlab && git log -3 --format="%H %ad %s" && find . -type f -not -path "./.git/*" | head -80
```

```
f39736734031c9e37e0b101536be8d8be35906db Fri Jul 14 09:28:03 2017 +0200 morphology detector done (Burnos et al. 2016)
770267907def75ee5f88b7b921910ef6ab014ba6 Fri Jul 14 09:27:15 2017 +0200 Adjustments in output structure creation
6c4401b2258a847e78ca54de07701d5b32f46580 Thu Jul 13 12:00:48 2017 +0200 Morphology detector (Fedele et al. 2016)
./sim/hfo.m
./sim/brownnoise.m
./sim/pinknoise.m
./sim/wavelet_spike.m
./sim/wavelet.m
./hfo-detect-toolbox/Morphology Detector/st_cleaned.m
./hfo-detect-toolbox/Morphology Detector/func_prepareMorphologyDetector.m
./hfo-detect-toolbox/Morphology Detector/func_doMorphologyDetector.m
./hfo-detect-toolbox/Morphology Detector/data_example.mat
./hfo-detect-toolbox/Morphology Detector/st.m
./hfo-detect-toolbox/Morphology Detector/example.m
./hfo-detect-toolbox/Morphology Detector/Filter_AsBurnos2016.mat
./signal_transform/compute_stenergy.m
./signal_transform/compute_teager_energy.m
./signal_transform/compute_line_lenght.m
./signal_transform/compute_hilbert_envelope.m
./signal_transform/compute_rms.m
[... 28 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/HFO-detect-matlab/hfo-detect-toolbox/"Morphology Detector"; wc -l *.m; cat func_prepareMorphologyDetector.m example.m; grep -n "FRandR\|overlap\|Ripple\|FastRipple\|time_thr\|20\b\|0.01\|0.02" func_doMorphologyDetector.m | head -60
```

```
8 example.m
  548 func_doMorphologyDetector.m
  105 func_prepareMorphologyDetector.m
  340 st.m
  276 st_cleaned.m
 1277 total
% ===================================================================================
% *** Function DETECTOR MCGILL

function [sig ] = func_prepareMorphologyDetector(data, p)
p.limitFrequencyST = p.lp;


%% %%%%%%%%%%%%%%%%%%%%%%%%%%%% reading the signals
display(['%%%%%%%%%%%%% START ANALYSIS ' datestr(now,'dd-mm-yyyy HH-MM-SS') ' %%%%%%%%%%%%%%%%'])
display(' ')

%% read visual markings and filter data
sig=struct;

[... 114 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR; which pdftoppm pdfinfo; python -c "import fitz;print(fitz.__doc__)"; pdfinfo paper/*MOESM1*.pdf | grep Pages
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1038-s41598-017-13064-1.supp-41598_2017_13064_MOESM1_ESM.pdf",
 "pages": "2"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd $TMPDIR; python -m venv v >/dev/null && v/bin/pip -q install pymupdf 2>&1 | tail -2; v/bin/python -c "
import fitz
d=fitz.open('paper/10.1038-s41598-017-13064-1.supp-41598_2017_13064_MOESM1_ESM.pdf')
print(len(d))
for i,p in enumerate(d):
  print(i, len(p.get_images()), len(p.get_drawings()), p.get_text()[:60].replace('\n',' | '))
"
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd $TMPDIR; v/bin/python -c "
import pymupdf as fitz
d=fitz.open('paper/10.1038-s41598-017-13064-1.supp-41598_2017_13064_MOESM1_ESM.pdf')
p=d[2]; print(p.rect)
pix=p.get_pixmap(dpi=110); pix.save('s3.png'); print(pix.width,pix.height)
"
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/s3.png"
}
```

Result: no output.

**Agent calls Bash**

```bash
cd $TMPDIR; v/bin/python -c "
import pymupdf as fitz
d=fitz.open('paper/10.1038-s41598-017-13064-1.supp-41598_2017_13064_MOESM1_ESM.pdf')
p=d[2]
pix=p.get_pixmap(dpi=300, clip=fitz.Rect(60,60,560,110)); pix.save('p1.png')
"
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/p1.png"
}
```

Result: no output.

## Prompt

[Image: original 2084x209, displayed at 2000x201. Multiply coordinates by 1.04 to map to original image.]

**Agent calls Bash**

```bash
cd  sed -n 1,60p tools/claims_check.py; grep -n "^  [a-z_]*:" -h claims/*.yaml | sed 's/:.*//' | sort | uniq -c | sort -rn | head -30
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

[... 71 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python -c "
import json;s=json.load(open('schemas/claims.schema.json'))
print(json.dumps(s,indent=0)[:6000])"
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
[... 270 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python -c "
import json;s=json.load(open('schemas/claims.schema.json'))
print(json.dumps(s['\$defs']['statistic'],indent=0))"
```

```
{
"type": "object",
"additionalProperties": false,
"anyOf": [
{
"required": [
"p"
]
},
{
"required": [
"ci"
]
}
],
"properties": {
"about": {
"description": "What the test compares or the interval bounds, when the claim has more than one, e.g. 'GPi against VLa onset times'.",
"type": "string"
},
[... 57 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR; v/bin/pip -q install scipy numpy statsmodels 2>&1 | grep -v notice; v/bin/python -c "
import numpy as np
from scipy import stats
from statsmodels.stats.proportion import proportion_confint as pc
g=[12,29,13,41,14,11,36,37,25,25,10,25,19]; b=[42,15,46,45,30,11,16]
print(np.mean(b),np.std(b,ddof=1),np.mean(g),np.std(g,ddof=1))
print(stats.ranksums(b,g), stats.mannwhitneyu(b,g,method='exact'), stats.mannwhitneyu(b,g,method='asymptotic'), stats.mannwhitneyu(b,g,method='asymptotic',use_continuity=False))
for k,n in [(13,13),(4,7),(13,16),(17,20),(13,20),(4,5),(15,16),(19,20),(7,13),(3,7),(7,11),(3,9),(10,20),(9,13),(2,7),(9,14),(2,6),(11,20)]:
  print(k,n,[tuple(np.round(np.array(pc(k,n,method=m))*100,1)) for m in ['beta','wilson','normal']])
for t in [[[4,0],[3,13]],[[4,0],[1,15]],[[3,6],[4,7]],[[2,4],[5,9]]]:
  print(t, stats.chi2_contingency(t,correction=False)[:2], stats.chi2_contingency(t,correction=True)[:2], stats.fisher_exact(t))
"
```

```
29.285714285714285 15.293945269444437 22.846153846153847 10.675877433464613
RanksumsResult(statistic=np.float64(1.188643277625491), pvalue=np.float64(0.2345800700938523)) MannwhitneyuResult(statistic=np.float64(60.5), pvalue=np.float64(0.27492260061919505)) MannwhitneyuResult(statistic=np.float64(60.5), pvalue=np.float64(0.24965499988272144)) MannwhitneyuResult(statistic=np.float64(60.5), pvalue=np.float64(0.23369917011909358))
13 13 [(np.float64(75.3), np.float64(100.0)), (np.float64(77.2), np.float64(100.0)), (np.float64(100.0), np.float64(100.0))]
4 7 [(np.float64(18.4), np.float64(90.1)), (np.float64(25.0), np.float64(84.2)), (np.float64(20.5), np.float64(93.8))]
13 16 [(np.float64(54.4), np.float64(96.0)), (np.float64(57.0), np.float64(93.4)), (np.float64(62.1), np.float64(100.0))]
17 20 [(np.float64(62.1), np.float64(96.8)), (np.float64(64.0), np.float64(94.8)), (np.float64(69.4), np.float64(100.0))]
13 20 [(np.float64(40.8), np.float64(84.6)), (np.float64(43.3), np.float64(81.9)), (np.float64(44.1), np.float64(85.9))]
4 5 [(np.float64(28.4), np.float64(99.5)), (np.float64(37.6), np.float64(96.4)), (np.float64(44.9), np.float64(100.0))]
15 16 [(np.float64(69.8), np.float64(99.8)), (np.float64(71.7), np.float64(98.9)), (np.float64(81.9), np.float64(100.0))]
19 20 [(np.float64(75.1), np.float64(99.9)), (np.float64(76.4), np.float64(99.1)), (np.float64(85.4), np.float64(100.0))]
7 13 [(np.float64(25.1), np.float64(80.8)), (np.float64(29.1), np.float64(76.8)), (np.float64(26.7), np.float64(80.9))]
3 7 [(np.float64(9.9), np.float64(81.6)), (np.float64(15.8), np.float64(75.0)), (np.float64(6.2), np.float64(79.5))]
7 11 [(np.float64(30.8), np.float64(89.1)), (np.float64(35.4), np.float64(84.8)), (np.float64(35.2), np.float64(92.1))]
3 9 [(np.float64(7.5), np.float64(70.1)), (np.float64(12.1), np.float64(64.6)), (np.float64(2.5), np.float64(64.1))]
10 20 [(np.float64(27.2), np.float64(72.8)), (np.float64(29.9), np.float64(70.1)), (np.float64(28.1), np.float64(71.9))]

[... 10 more lines not kept]
```

**Agent calls Write**

```json
{
 "file_path": "claims/fedele-2017.yaml",
 "content": "# Claims for Fedele, Burnos, Boran, Krayenbuehl, Hilfiker, Grunwald & Sarnthein (2017),\n# Scientific Reports 7, 13836, on CRCNS ieeg-1.\n# Written by an agent (model \"claude-opus-5-5\", Claude Code, runner \"GitHub Actions\"),\n# 2026-11-09, protocol pilot-14 as stated in docs/protocol.md.\n#\n# Text read: the version of record (PMC5653833, Europe PMC JATS XML flattened), main text,\n# Tables 1 and 2, figure legends and Methods, and the supplement (41598_2017_13064_MOESM1_ESM.pdf,\n# from the publisher), which holds only Table S1. The text of Table S1 keeps the channel names\n# and rates but loses its colours; the PDF page was rendered to read them: channels excluded\n# from the analysis are filled gray, resected channels (RA) red, and the HFO area of each HFO\n# type green, cell by cell in the Ripples, FR and FRandR rows. The colours are vector fills in\n# the PDF and can be read programmatically. The CRCNS data description (paper/ieeg-1.data-\n# description.txt) was read for the layout of the deposit only; no claim is taken from it.\n#\n# Code: the Methods link https://github.com/HFO-detect/HFO-detect-matlab, read at commit\n# f39736734031c9e37e0b101536be8d8be35906db (2017-07-14). It holds the HFO detectors only: the\n# morphology detector of Burnos et al. 2016 (hfo-detect-toolbox/Morphology Detector, with\n# Filter_AsBurnos2016.mat, the Stockwell transform st.m, and the detector parameters in\n# func_prepareMorphologyDetector.m: minimum duration 0.02 s for ripples and 0.01 s for FR, as\n# the Methods say; filtering with filtfilt), plus line-length and RMS detectors. The function\n# it calls, RUN_MorphologyDetector, is not in the repository. It holds no code for the FRandR\n# overlap, the HFO rates, the HFO area, the test-retest analysis, the outcome statistics or the\n# spectral analysis. Those methods come from the paper alone. The deposit holds the detected\n# events (R, FR and FRandR start and end samples per bipolar channel), so the detector need not\n# be rerun for any claim except as a check.\n#\n# Data the paper used (Results paragraph 1, Table 1, Methods). 20 consecutive patients with\n# drug-resistant focal epilepsy operated after invasive monitoring, March 2012 to April 2016:\n# 9 with mesial temporal lobe epilepsy (TLE, patients 1 to 9, bilateral depth electrodes in\n# amygdala, hippocampus, entorhinal and perirhinal cortex) and 11 with extratemporal epilepsy\n# (ETE, patients 10 to 20, grids, strips and depth electrodes). Outcome by ILAE class (Table 1):\n# ILAE 1 in patients 1 to 6 and 10 to 16 (13 seizure free); ILAE 3 in 7 and 8; ILAE 5 in 9, 17,\n# 18 and 20; ILAE 6 in 19. Follow-up months per patient in Table 1. Recordings: iEEG at 4 kHz,\n# down-sampled to 2 kHz, common intracranial reference, transformed to bipolar channels. From\n# each night up to six 5-minute intervals of interictal slow-wave sleep, at least 3 h from\n# seizures; nights and intervals per patient in Table 1 (1 to 6 nights, 1 to 39 intervals).\n# Channels where stimulation evoked motor or language responses were excluded; in TLE only the\n# 3 most mesial bipolar channels of each electrode were kept (gray cells of Table S1 mark the\n# exclusions). Measured variables: detected ripples (80-250 Hz), fast ripples (FR, 250-500 Hz)\n# and FR co-occurring with ripples (FRandR), their rates per channel in events/min (Table S1),\n# the resected channels (Table S1, red), and outcome (Table 1).\n#\n# Methods fixed by the paper and used by several claims:\n# - HFO rate of a channel: events per minute (Table S1, Fig. 3A).\n# - HFO area (Methods, Definition of the HFO area by rate thresholding): the channels whose rate\n#   exceeds the 95th percentile of the patient's distribution of channel rates, computed with\n#   Matlab prctile.m (its default method: sorted values placed at percentiles 100(i-0.5)/n,\n#   linear interpolation, the extreme values beyond the end points). One area per HFO type.\n# - Outcome classes (Methods, Clinical validation): TP, HFO area not fully inside the RA (at\n#   least one area channel not resected) and recurrent seizures (ILAE 2-6); FP, not fully inside\n#   and ILAE 1; FN, fully inside and recurrent seizures; TN, fully inside and ILAE 1. PPV, NPV,\n#   sensitivity, specificity and accuracy as defined there. 95% CI by the binomial method for\n#   n < 10 and the asymptotic method for n > 10; significance at p < 0.05.\n# - Test-retest (Methods, Test-retest reliability): for each pair of 5-min intervals the\n#   normalized scalar product of the channel rate vectors; null from 5000 random permutations of\n#   the channel order of each interval; a pair is significant when its scalar product exceeds\n#   the 97.5th percentile of the null. Nights: the mean rate of each night, pairs of nights.\n#\n# Open details, each with the readings the text allows (the author runs them all):\n# - How a channel's rate is pooled over intervals: (a) all events over the total recorded time\n#   of the patient; (b) the mean over intervals of per-interval rates; (c) the mean over nights\n#   of per-night mean rates (Methods, Test-retest, \"we took the mean HFO rate for each night\").\n#   Fig. 3 legend says the HFO area \"averaged over all intervals\"; (d) a channel is in the area\n#   when it is in the per-interval area in at least half of the intervals. Table S1's rates\n#   (claim table-s1-rates) decide among (a) to (c); the reading that matches them is used for\n#   the area in every other claim, and (d) is shown as a variant.\n# - Which channels enter the percentile: (a) the channels not grayed in Table S1; (b) all bipolar\n#   channels of the deposit. \"Exceeds\" is read as strictly greater (Methods, \"exceeded\"); greater\n#   or equal is a variant.\n# - The resected channels come from Table S1 (red), unless the deposit marks them; the paper\n#   names no other source.\n# - The HFO type of the test-retest values of Table 1: Fig. 3 shows FRandR; Table 1 does not\n#   say. Readings: (a) FRandR; (b) ripples; (c) FR.\n# - The permutation null: (a) one null per interval pair (each interval's channel order\n#   permuted 5000 times); (b) one null pooled over all pairs of the patient, as Fig. 3B plots a\n#   single random distribution.\n# - \"Normalized scalar product\": the dot product divided by the product of the vector norms\n#   (cosine), the standard meaning; the paper says it is about 1 for overlapping distributions,\n#   which this reading gives for non-negative rates.\n# - The test of the follow-up comparison and the chi2 tests are named but not their variants;\n#   see the claims.\n#\n# Inconsistencies in the paper: the specificity CI is 78-100% in the Results and 75-100% in the\n# Discussion; the Clopper-Pearson interval for 13/13 is 75.3-100%. The Table 1 legend gives\n# test-retest medians for TLE patients \"irrespective of outcome\" as >98%; Table 1 gives 0.67 for\n# patient 8 (ILAE 3) and 1.00 for patient 9 (ILAE 5), whose median is 0.835. The Fig. 1 legend\n# labels PR \"posterior hippocampus left\". Patient 19 has a 4 x 8 grid in the Discussion and an\n# 8 x 4 grid in Table 1.\nschema_version: 2\npaper: doi:10.1038/s41598-017-13064-1\nclaims:\n- id: cohort\n  statement: The study included 20 patients, 9 with mesial temporal lobe epilepsy and 11 with\n    extratemporal epilepsy; 13 became seizure free (ILAE 1) and 7 had recurrent seizures, a\n    seizure-free rate of 65%.\n  source: Results, paragraph 1; Table 1\n  quote: We included 20 patients (Table 1 ) of whom 9 with mesial temporal lobe epilepsy (TLE)\n    and 11 with extratemporal epilepsy (ETE). Complete seizure freedom (ILAE 1 - International\n    League Against Epilepsy, class 1) was reached in 13 patients, while 7 patients suffered from\n    recurrent seizures (seizure-free rate = 65%)\n  statistics:\n  - about: seizure-free rate\n    ci:\n      level: 0.95\n      low: 41\n      high: 85\n      unit: \"%\"\n    n: 20 patients\n  expected:\n  - quantity: patients\n    value: 20\n    tolerance: 0\n  - quantity: TLE patients\n    value: 9\n    tolerance: 0\n  - quantity: ETE patients\n    value: 11\n    tolerance: 0\n  - quantity: seizure-free patients (ILAE 1)\n    value: 13\n    tolerance: 0\n  criterion: Counts of patients are exact (tolerance 0, as they are counts of whole patients).\n    The epilepsy type and ILAE class of each patient are compared with Table 1. Reproduced when\n    the deposit holds 20 patients and the counts match; the per-patient comparison is reported.\n- id: table1-nights-intervals\n  statement: The number of recorded nights and of 5-minute intervals varies across patients as\n    listed in Table 1 (from 1 night and 1 interval in patients 7 and 17 to 6 nights in patient 4\n    and 39 intervals in patient 3).\n  source: Methods, Data selection; Table 1, columns Nights and Intervals\n  quote: The amount of nights and intervals varied across patients (Table 1 ).\n  criterion: For each patient the count of distinct nights and of 5-minute intervals in the\n    deposit is compared with Table 1 (Nights; Intervals). Reproduced when all 20 patients match\n    on both; partially reproduced when at least 16 match on both; not reproduced otherwise.\n    Every mismatch is listed.\n- id: hfo-amplitudes\n  statement: Detected ripples had median amplitude 27.4 microvolt peak-to-peak (interquartile\n    range 15.0) and FR median amplitude 9.2 microvolt peak-to-peak (interquartile range 7.5).\n  source: Results, The HFO area predicted seizure outcome, paragraph 1\n  quote: Automatic HFO detection yielded ripples (median amplitude 27.4 µVpp (peak-to-peak),\n    interquartile range 15.0 µVpp) and FR (median amplitude 9.2 µVpp, interquartile range 7.5\n    µVpp)\n  expected:\n  - quantity: ripple median amplitude\n    value: 27.4\n    tolerance: 2.74\n    unit: microvolt peak-to-peak\n  - quantity: ripple amplitude interquartile range\n    value: 15.0\n    tolerance: 1.5\n    unit: microvolt peak-to-peak\n  - quantity: FR median amplitude\n    value: 9.2\n    tolerance: 0.92\n    unit: microvolt peak-to-peak\n  - quantity: FR amplitude interquartile range\n    value: 7.5\n    tolerance: 0.75\n    unit: microvolt peak-to-peak\n  criterion: Events are the deposit's R and FR markings on the bipolar channels (Methods, Data\n    acquisition, bipolar montage). The paper does not say on which signal the amplitude is\n    taken or how events are pooled. Readings of the signal; (a) the band-passed signal of the\n    event's band, with the detector's filters (Methods; ripples 80-240 Hz, FR 250-490 Hz, FIR\n    equiripple, applied with filtfilt as in func_prepareMorphologyDetector.m, coefficients\n    Filter_AsBurnos2016.mat of the linked repository), amplitude = maximum minus minimum\n    within the event; (b) the same on the unfiltered bipolar signal. Readings of the pooling;\n    (i) all events of all patients pooled; (ii) only events on channels not excluded (Table S1\n    gray). Reproduced when, under one reading, all four values are within tolerance; partially\n    reproduced when the two medians are.\n- id: followup-not-different\n  statement: Mean follow-up was 29 +- 15 months for patients with poor outcome and 23 +- 11\n    months for good outcome, and the two distributions did not differ (Wilcoxon rank sum test,\n    p = 0.25).\n  source: Results, The HFO area predicted seizure outcome, paragraph 1; Table 1, column\n    Postoperative follow-up\n  quote: The mean follow-up for poor outcome (29 ± 15 mo) was longer than for good outcome (23 ±\n    11 mo) but the two distributions are indistinguishable (Wilcoxon rank sum test, p = 0.25)\n  statistics:\n  - test: Wilcoxon rank sum test\n    p: 0.25\n    n: 7 patients with poor outcome and 13 with good outcome\n  expected:\n  - quantity: mean follow-up, poor outcome (ILAE 2-6)\n    value: 29\n    tolerance: 2.9\n    unit: months\n  - quantity: mean follow-up, good outcome (ILAE 1)\n    value: 23\n    tolerance: 2.3\n    unit: months\n  - quantity: SD of follow-up, poor outcome\n    value: 15\n    tolerance: 1.5\n    unit: months\n  - quantity: SD of follow-up, good outcome\n    value: 11\n    tolerance: 1.1\n    unit: months\n  criterion: A claim of absence, judged on the paper's test, a Wilcoxon rank sum test of\n    follow-up months between ILAE 1 and ILAE 2-6 patients at p < 0.05 (Methods, Clinical\n    validation). Follow-up months come from the deposit when it holds them, else from Table 1.\n    The paper does not say whether the exact or the normal approximation was used; the\n    approximation with continuity correction (Matlab ranksum's default for these sizes) is\n    the main reading and the exact test a variant. SD is the sample SD (n - 1). Reproduced\n    when p >= 0.05 and the means and SDs are within tolerance; the p-value is reported.\n- id: table-s1-rates\n  statement: The per-channel rates of ripples, FR and FRandR (events/min) of every patient are\n    those listed in Table S1, and the channels marked there as the HFO area of each type are\n    those whose rate exceeds the 95th percentile.\n  source: Supplementary Table 1S\n  quote: The rates of ripple, FR and FRandR events are given in events/minute for each channel.\n    Channels with the HFO rate exceeding the 95% percentile of the HFO distribution define the\n    HFO area and are highlighted in green.\n  criterion: Rates per channel from the deposit's R, FR and FRandR markings, under readings\n    (a), (b) and (c) of the pooling over intervals named in the opening comment. Channels are\n    matched by their bipolar label. A channel's rate matches when it is within 10% of the Table\n    S1 value or within 0.1 events/min (the table's rounding), whichever is larger. Reproduced\n    when, under one reading, at least 95% of the channel and type values of all 20 patients\n    match; partially reproduced at 80% or more. The HFO area per patient and type is then\n    computed as in the opening comment and compared with the green cells of Table S1; the\n    count of patient and type areas that agree exactly is reported. The reading that matches\n    best is used for the HFO area in the dependent claims.\n- id: fig1-patient4\n  statement: In patient 4 (right hippocampal sclerosis, seizure free) the HFO types differ in\n    their distribution over channels; several channels have FRandR rate 0; the ripple area was\n    not resected, and the FRandR area, channel AR1-AR2, was resected.\n  source: Figure 1E-G legend\n  quote: Note that several channels have FRandR rate = 0. ... The ripple area was not resected (\n    E ). The resection of the FRandR area ( G , channel AR1-AR2) led to seizure freedom.\n  depends_on:\n  - table-s1-rates\n  criterion: Patient 4's channel rates and HFO areas as in table-s1-rates, on the mesial\n    temporal channels the figure shows (the channels not grayed in Table S1). Reproduced when\n    the FRandR area is AR1-2 alone and resected, the ripple area contains at least one channel\n    outside the RA (Table S1 red), and at least two channels have FRandR rate 0.0 at the\n    precision of Table S1.\n- id: frandr-area-resection-per-patient\n  statement: The FRandR area was fully inside the resected area in all 13 seizure-free patients\n    and in 3 of the 7 patients with recurrent seizures (7, 8, 9), and not fully resected in 4\n    patients with recurrent seizures (17, 18, 19, 20).\n  source: Table 1, column FRandR area resected?; Discussion, FRandR in patients with recurrent\n    seizures, paragraphs 1-2\n  quote: Among the 7 patients with recurrent seizures, FRandR were fully resected in 3 FN and\n    not fully resected in 4 TP\n  depends_on:\n  - table-s1-rates\n  expected:\n  - quantity: patients with FRandR area fully resected among the 13 seizure-free\n    value: 13\n    tolerance: 0\n  - quantity: patients with FRandR area fully resected among the 7 with recurrent seizures\n    value: 3\n    tolerance: 0\n  criterion: FRandR area per patient as in the opening comment, resected channels from Table S1\n    (red) unless the deposit marks them. A patient's area is fully resected when every area\n    channel is resected. The per-patient result is compared with Table 1 (FRandR area resected?\n    Y for 1-16, N for 17-20). Reproduced when all 20 patients agree; partially reproduced when\n    the counts are off by one patient. Readings of the pooling and of the channel set as in\n    the opening comment; the outcome is the one they all give, or as stated there.\n- id: ripple-fr-area-resection-per-patient\n  statement: The ripple and FR areas were resected in the patients marked in Table 1 (ripple\n    area resected in 7 of 13 seizure-free and 4 of 7 recurrent-seizure patients; FR area in 9\n    of 13 and 5 of 7).\n  source: Table 1, columns Ripple area resected? and FR area resected?\n  inferred: Per-patient values read from Table 1; the counts follow from the column values and\n    match Table 2. No sentence states them.\n  depends_on:\n  - table-s1-rates\n  expected:\n  - quantity: ripple area fully resected, seizure free\n    value: 7\n    tolerance: 0\n  - quantity: ripple area fully resected, recurrent seizures\n    value: 4\n    tolerance: 0\n  - quantity: FR area fully resected, seizure free\n    value: 9\n    tolerance: 0\n  - quantity: FR area fully resected, recurrent seizures\n    value: 5\n    tolerance: 0\n  criterion: As frandr-area-resection-per-patient, for ripples and FR. Reproduced when at least\n    19 of 20 patients agree with Table 1 for each type and the counts match; partially\n    reproduced when at least 17 of 20 agree for each.\n- id: table2-frandr-prediction\n  statement: Defining the HFO area by FRandR, its resection predicted seizure outcome with\n    specificity 100% (CI 78-100%), sensitivity 57% (CI 18-90%), NPV 81% (CI 54-96%), PPV 100%,\n    and accuracy 85% (CI 62-97%, p = 0.002, chi2 test).\n  source: Results, The HFO area predicted seizure outcome, paragraph 1; Table 2\n  quote: When defining the HFO area by FRandR (FRandR area, Fig. 1 ), we achieved specificity\n    100%, CI [78–100%] ... The low sensitivity (57%, CI [18–90%]) ... Analogous considerations\n    hold for the NPV (81%, CI [54–96%]) ... Therefore, the overall accuracy of our algorithm\n    (85%, CI [62–97%], p = 0.002 chi2-test)\n  statistics:\n  - about: specificity\n    ci:\n      level: 0.95\n      low: 78\n      high: 100\n      unit: \"%\"\n    n: 13 seizure-free patients\n  - about: sensitivity\n    ci:\n      level: 0.95\n      low: 18\n      high: 90\n      unit: \"%\"\n    n: 7 patients with recurrent seizures\n  - about: NPV\n    ci:\n      level: 0.95\n      low: 54\n      high: 96\n      unit: \"%\"\n    n: 16 patients with the FRandR area fully resected\n  - about: accuracy\n    test: chi2-test\n    p: 0.002\n    ci:\n      level: 0.95\n      low: 62\n      high: 97\n      unit: \"%\"\n    n: 20 patients\n  depends_on:\n  - frandr-area-resection-per-patient\n  expected:\n  - quantity: specificity\n    value: 100\n    tolerance: 0\n    unit: \"%\"\n  - quantity: sensitivity\n    value: 57\n    tolerance: 0\n    unit: \"%\"\n  - quantity: NPV\n    value: 81\n    tolerance: 0\n    unit: \"%\"\n  - quantity: PPV\n    value: 100\n    tolerance: 0\n    unit: \"%\"\n  - quantity: accuracy\n    value: 85\n    tolerance: 0\n    unit: \"%\"\n  criterion: Counts TP, FP, FN, TN from frandr-area-resection-per-patient and the definitions of\n    Methods, Clinical validation; percentages rounded to whole numbers must equal the paper's\n    (tolerance 0, as each is a ratio of small whole counts and any change of one patient moves\n    it by more than 4 points). CIs by the Clopper-Pearson binomial method, which gives every\n    printed interval except the specificity lower bound (75.3, which the Discussion prints as\n    75); the asymptotic (Wald) method the Methods name for n > 10 is shown as a variant. The\n    chi2 test is on the 2 x 2 table of area resection (fully, not fully) by outcome (ILAE 1,\n    ILAE 2-6); the paper does not say which variant; readings (a) Pearson without continuity\n    correction (gives p = 0.0023 on the paper's counts), (b) with Yates correction, (c) Fisher's\n    exact test. Reproduced when the five percentages match and p < 0.05 under reading (a).\n- id: table2-ripple-fr-prediction\n  statement: With the area defined by ripples, specificity was 54%, sensitivity 43%, NPV 64%,\n    PPV 33% and accuracy 50%; by FR, 69%, 29%, 64%, 33% and 55%.\n  source: Table 2\n  inferred: Values read from Table 2; no sentence of the text states them.\n  depends_on:\n  - ripple-fr-area-resection-per-patient\n  expected:\n  - quantity: ripple specificity\n    value: 54\n    tolerance: 0\n    unit: \"%\"\n  - quantity: ripple sensitivity\n    value: 43\n    tolerance: 0\n    unit: \"%\"\n  - quantity: ripple NPV\n    value: 64\n    tolerance: 0\n    unit: \"%\"\n  - quantity: ripple PPV\n    value: 33\n    tolerance: 0\n    unit: \"%\"\n  - quantity: ripple accuracy\n    value: 50\n    tolerance: 0\n    unit: \"%\"\n  - quantity: FR specificity\n    value: 69\n    tolerance: 0\n    unit: \"%\"\n  - quantity: FR sensitivity\n    value: 29\n    tolerance: 0\n    unit: \"%\"\n  - quantity: FR NPV\n    value: 64\n    tolerance: 0\n    unit: \"%\"\n  - quantity: FR PPV\n    value: 33\n    tolerance: 0\n    unit: \"%\"\n  - quantity: FR accuracy\n    value: 50\n    tolerance: 0\n    unit: \"%\"\n  criterion: As table2-frandr-prediction, for ripples and FR, without CIs or test. Tolerance 0\n    on percentages rounded to whole numbers, for the reason given there. The FR accuracy in\n    Table 2 is 55%; the expected value listed as 50 above is an error of this file only if\n    Table 2 says otherwise, and Table 2 governs. Reproduced when all ten values match.\n- id: frandr-more-specific\n  statement: The FRandR area was more specific in predicting seizure freedom than the ripple\n    and FR areas separately (specificity 100% against 54% and 69%).\n  source: Table 2 legend; Discussion, FRandR are more specific than FR and ripple separately,\n    paragraph 1\n  quote: Defining the HFO area by FR co-occurring with ripples was more specific in predicting\n    seizure freedom than FR and ripples separately.\n  depends_on:\n  - table2-frandr-prediction\n  - table2-ripple-fr-prediction\n  criterion: The paper reports no test of the difference. Reproduced when the FRandR\n    specificity exceeds both the ripple and the FR specificity computed in the claims it\n    depends on.\n- id: engel-prediction\n  statement: Taking Engel class I (ILAE 1-3) as good outcome, the FRandR area gives sensitivity\n    80% (CI 28-99%), NPV 94% (CI 70-100%) and accuracy 95% (CI 75-100%, p = 0.001, chi2 test).\n  source: Results, The HFO area predicted seizure outcome, paragraph 1\n  quote: When taking as outcome measure the Engel class I (ILAE 1–3), values improve to\n    sensitivity 80%, CI [28–99%], NPV 94%, CI [70 100%], and accuracy 95%, CI [75 100%], p =\n    0.001 (chi2-test)\n  statistics:\n  - about: sensitivity\n    ci:\n      level: 0.95\n      low: 28\n      high: 99\n      unit: \"%\"\n    n: 5 patients with ILAE 4-6\n  - about: NPV\n    ci:\n      level: 0.95\n      low: 70\n      high: 100\n      unit: \"%\"\n    n: 16 patients with the FRandR area fully resected\n  - about: accuracy\n    test: chi2-test\n    p: 0.001\n    ci:\n      level: 0.95\n      low: 75\n      high: 100\n      unit: \"%\"\n    n: 20 patients\n  depends_on:\n  - frandr-area-resection-per-patient\n  expected:\n  - quantity: sensitivity\n    value: 80\n    tolerance: 0\n    unit: \"%\"\n  - quantity: NPV\n    value: 94\n    tolerance: 0\n    unit: \"%\"\n  - quantity: accuracy\n    value: 95\n    tolerance: 0\n    unit: \"%\"\n  criterion: As table2-frandr-prediction with ILAE 1-3 as good outcome (patients 7 and 8 move\n    from FN to TN). The chi2 readings are those named there; on the paper's counts (a) gives p\n    = 0.0001, (b) p = 0.0012 and (c) p = 0.0010, so the printed value fits (b) or (c), while\n    the p = 0.002 of table2-frandr-prediction fits (a). Reproduced when the three percentages\n    match and p < 0.05 under every reading; each p-value is reported.\n- id: ete-soz-not-resected\n  statement: In all seizure-free ETE patients (10-16) the resection was limited to 1-2 cm2 and\n    the seizure onset zone was not fully resected, while the FRandR area was always fully\n    resected.\n  source: Discussion, FRandR predict seizure freedom in the individual patient, paragraph 2\n  quote: While the SOZ was therefore not fully resected in all ETE patients, the HFO area as\n    defined by FRandR was always fully resected.\n  depends_on:\n  - frandr-area-resection-per-patient\n  criterion: Needs the SOZ channels of patients 10-16, which the paper does not list (it shows\n    them only for patient 17, Fig. 2B). Reproduced when, for each of patients 10-16, at least\n    one SOZ channel is outside the RA and the FRandR area is fully inside it. The resection\n    size cannot be tested from channel data and is not judged.\n- id: fig2-patient17\n  statement: In patient 17 (recurrent seizures) the resected area does not comprise all\n    channels of the HFO area, and the HFO area is smaller than the seizure onset zone.\n  source: Figure 2B-C legend\n  quote: The HFO area (contacts filled yellow) is smaller than the SOZ. ( C ) The resected area\n    (RA) does not comprise all channels of the HFO area.\n  depends_on:\n  - table-s1-rates\n  criterion: FRandR area of patient 17 as in table-s1-rates; resected channels from Table S1\n    (red). Reproduced when at least one FRandR area channel is outside the RA and at least one\n    is inside it (Discussion, \"parts of the HFO area were indeed included\"). The comparison\n    with the SOZ is tested only if the SOZ channels are available, as fewer area channels than\n    SOZ channels.\n- id: fig3-patient1\n  statement: In patient 1 (seizure free) the FRandR area was channel PHR1-2 in each of 4 nights\n    and in the resected area for all intervals, and 99% of the scalar products between interval\n    pairs exceeded significance.\n  source: Figure 3A-C legend\n  quote: The HFO area comprises channel PHR1-2 for each night. The HFO area was stable over\n    nights and included in the RA. ... 99% of the true distribution exceeded significance ...\n    The HFO area was inside the resected area for all intervals.\n  depends_on:\n  - table-s1-rates\n  expected:\n  - quantity: fraction of significant interval-pair scalar products, patient 1\n    value: 0.99\n    tolerance: 0.099\n  criterion: FRandR rates of patient 1 per night (mean over the night's intervals) and per\n    interval; the HFO area per night and per interval by the 95th percentile rule; test-retest\n    as in the opening comment, readings (a) and (b) of the permutation null. Reproduced when\n    the area is PHR1-2 in every night, every per-interval area lies inside the RA (Table S1\n    red), and the fraction is within tolerance under one reading. With intervals that have no\n    FRandR on any channel the area is empty, which counts as inside the RA.\n- id: test-retest-group\n  statement: Across 18 patients the share of significant scalar products had median 97.5%\n    (lower quartile 67%) over pairs of 5-minute intervals and median 100% (lower quartile 100%)\n    over pairs of nights.\n  source: Results, Test-retest reliability of the spatial distribution of HFO rates, paragraph\n    2; Table 1, columns Test - retest intervals and nights\n  quote: Across the group of 18 patients (Table 1 ), the percentage of significant scalar\n    products had median of 97.5% (lower quartile 67%) when taking pairs of all 5 minutes\n    intervals, and a median of 100% (lower quartile 100%) when taking pairs of entire nights.\n  expected:\n  - quantity: median share of significant interval pairs\n    value: 97.5\n    tolerance: 9.75\n    unit: \"%\"\n  - quantity: lower quartile, interval pairs\n    value: 67\n    tolerance: 6.7\n    unit: \"%\"\n  - quantity: median share of significant night pairs\n    value: 100\n    tolerance: 10\n    unit: \"%\"\n  - quantity: lower quartile, night pairs\n    value: 100\n    tolerance: 10\n    unit: \"%\"\n  criterion: Test-retest as in the opening comment, on the 18 patients with more than one\n    interval (all but 7 and 17; night pairs exist only for the 16 with more than one night).\n    Quartiles with Matlab prctile (the Methods name it for percentiles). HFO type readings (a)\n    FRandR, (b) ripples, (c) FR, and permutation null readings (a) and (b) of the opening\n    comment. Reproduced when, under one reading, the four values are within tolerance. The\n    per-patient values are compared with Table 1 and the count within 0.1 of it is reported.\n- id: test-retest-by-group\n  statement: Over intervals, the median share of significant scalar products was above 98% in\n    TLE patients irrespective of outcome, 97% in ETE patients with good outcome and only 36% in\n    ETE patients with poor outcome.\n  source: Results, Test-retest reliability of the spatial distribution of HFO rates, paragraph\n    2; Discussion, Automated detection predicts seizure outcome, paragraph 2\n  quote: Over the intervals of TLE patients, the median was >98% irrespective of outcome. Over\n    the intervals of ETE patients, the median was 97% for patients with good outcome and only\n    36% for patients with poor outcome.\n  depends_on:\n  - test-retest-group\n  expected:\n  - quantity: median, TLE patients\n    value: 98\n    unit: \"%\"\n  - quantity: median, ETE patients with good outcome (10-16)\n    value: 97\n    tolerance: 9.7\n    unit: \"%\"\n  - quantity: median, ETE patients with poor outcome (18-20)\n    value: 36\n    tolerance: 3.6\n    unit: \"%\"\n  criterion: Per-patient interval values from test-retest-group, under the reading that\n    reproduced it. The paper reports no test. \"Irrespective of outcome\" is read two ways; (a)\n    the median over all 8 TLE patients with more than one interval exceeds 98% (Table 1 gives\n    0.985); (b) the median exceeds 98% within each outcome group (Table 1 gives 0.985 for ILAE\n    1 and 0.835 for patients 8 and 9, so the paper's own table does not support (b)). The TLE\n    part is judged on (a), median at least 98% minus 10% of 98. Reproduced when the three\n    values are within tolerance and the ETE poor-outcome median is the lowest.\n- id: spectral-classes\n  statement: Of 6182 FRandR events on the highest-rate FRandR channel in each patient's HFO\n    area, 45% had two spectral peaks (second peak median 240 Hz), 28% one peak in the HFO range\n    (median 184 Hz) and 27% no prominent peak above 100 Hz.\n  source: Results, Spectral analysis of ripples co-occurring with FR, paragraph 1; Figure 4\n  quote: Out of 6182 detected events, 45% exhibited two distinct peaks in ripple and FR band with\n    the second peak at median frequency 240 Hz (Fig. 4A ), 28% had only one peak in the HFO\n    range (median frequency 184 Hz, Fig. 4B ), and 27% did not show a prominent peak >100 Hz in\n    the HFO range.\n  depends_on:\n  - table-s1-rates\n  expected:\n  - quantity: FRandR events analysed\n    value: 6182\n    tolerance: 618\n  - quantity: bimodal events\n    value: 45\n    tolerance: 4.5\n    unit: \"%\"\n  - quantity: median frequency of the second peak, bimodal\n    value: 240\n    tolerance: 24\n    unit: Hz\n  - quantity: unimodal events\n    value: 28\n    tolerance: 2.8\n    unit: \"%\"\n  - quantity: median peak frequency, unimodal\n    value: 184\n    tolerance: 18.4\n    unit: Hz\n  - quantity: events without a peak\n    value: 27\n    tolerance: 2.7\n    unit: \"%\"\n  criterion: From the Methods, Spectral analysis. Per patient, the bipolar channel of the FRandR\n    area with the highest FRandR rate; every FRandR event on it; Stockwell transform of 0.6 s of\n    signal centred on the event (st.m of the linked repository); the instantaneous power\n    spectrum averaged over the duration of the FR part of the event (the deposit's FR marking\n    overlapping the FRandR); a fit of four gaussians to the spectrum over 80-500 Hz by least\n    squares (lsqcurvefit); peaks and troughs found on the fitted curve. Bimodal, a trough\n    between 150 and 250 Hz and at least one peak above 200 Hz; unimodal, a single peak above\n    100 Hz detectable in the ripple band; otherwise no peak. Open, with readings; the centre of\n    the 0.6 s window, (a) the FRandR midpoint, (b) the FR midpoint; the signal transformed, (a)\n    the unfiltered bipolar signal, (b) the signal high-passed at 80 Hz; the gaussian starting\n    values and bounds, not given, (a) four gaussians at 100, 200, 300 and 400 Hz with widths\n    of 50 Hz, (b) starting peaks at the four largest local maxima of the spectrum; a peak, (a)\n    a local maximum of the fitted curve, (b) a fitted gaussian centre with positive amplitude\n    inside the band. Patients whose FRandR area is empty contribute no events. The event count\n    tolerance is 10%. Reproduced when the three shares are within tolerance under one reading\n    and the two median frequencies are; partially reproduced when the shares are in the same\n    order (bimodal largest) under one reading.\n- id: spectral-tle-ete-no-difference\n  statement: The spectral classes of FRandR events did not differ significantly between TLE\n    and ETE channels.\n  source: Results, Spectral analysis of ripples co-occurring with FR, paragraph 1\n  quote: No significant difference was observed between TLE and ETE channels.\n  depends_on:\n  - spectral-classes\n  criterion: A claim of absence; the paper names no test, only significance at p < 0.05\n    (Methods, Clinical validation). Main reading, a chi2 test of the 3 x 2 table of spectral\n    class (bimodal, unimodal, none) by epilepsy type over events, at p < 0.05. Variant, a\n    Wilcoxon rank sum test of the per-patient bimodal fraction between the 9 TLE and 11 ETE\n    channels. Reproduced when the main test gives p >= 0.05; the class shares per group and\n    the variant are reported.\n- id: tp-patients-hfo-area-location\n  statement: In the patients whose HFO area was not fully resected, the area lay outside the\n    resection; in patient 18 over occipital contacts ipsilateral to a resection that included\n    parietal cortex, in patient 19 over the parietal and not the resected temporal cavernoma,\n    and in patient 20 at the anterior margin while the resection was at the posterior margin\n    of the occipito-temporal gyrus.\n  source: Discussion, FRandR in patients with recurrent seizures, paragraph 2\n  quote: In patient 18, our analysis identified the HFO area over occipital contacts ipsilateral\n    to the resection, which included parietal cortex. ... The HFO area included the parietal\n    cavernoma but not the temporal cavernoma. The surgical choice was to resect only the\n    temporal cavernoma. In patient 20, the resection included the seizure onset area in the\n    posterior margin of the left occipito-temporal gyrus but the HFO area was in the anterior\n    margin.\n  depends_on:\n  - frandr-area-resection-per-patient\n  criterion: FRandR area channels of patients 18, 19 and 20 as in frandr-area-resection-per-\n    patient. Channel locations from the deposit's electrode schemes and channel labels. For\n    each patient, reproduced when at least one area channel lies outside the RA in the region\n    the Discussion names (patient 18, an occipital contact; patient 19, a contact of the\n    parietal grid; patient 20, an anterior contact of the grid). Judged per patient; reproduced\n    when all three hold, partially when one or two do. Where a contact's region cannot be read\n    from the schemes, that patient is not judged and the notes say why.\n"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/fedele-2017.yaml",
 "old_string": "  - quantity: FR accuracy\n    value: 50\n    tolerance: 0\n    unit: \"%\"\n  criterion: As table2-frandr-prediction, for ripples and FR, without CIs or test. Tolerance 0\n    on percentages rounded to whole numbers, for the reason given there. The FR accuracy in\n    Table 2 is 55%; the expected value listed as 50 above is an error of this file only if\n    Table 2 says otherwise, and Table 2 governs. Reproduced when all ten values match.",
 "new_string": "  - quantity: FR accuracy\n    value: 55\n    tolerance: 0\n    unit: \"%\"\n  criterion: As table2-frandr-prediction, for ripples and FR, without CIs or test. Tolerance 0\n    on percentages rounded to whole numbers, for the reason given there. Reproduced when all\n    ten values match."
}
```

```
The file claims/fedele-2017.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/fedele-2017.yaml",
 "old_string": "  - quantity: median, TLE patients\n    value: 98\n    unit: \"%\"",
 "new_string": "  - quantity: median, TLE patients\n    value: 98\n    tolerance: 9.8\n    unit: \"%\""
}
```

```
The file claims/fedele-2017.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd  python tools/claims_check.py claims/fedele-2017.yaml paper/10.1038-s41598-017-13064-1.txt; python -c "
import yaml,re
t=open('claims/fedele-2017.yaml').read()
print('emdash' if '—' in t else 'ok', 'rather' in t.lower())
d=yaml.safe_load(t)
c=d['claims'];print(len(c),sum('quote' in x for x in c),sum('statistics' in x for x in c),sum('criterion' in x for x in c))"
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  grep -nE "^\s{4,}.*: " claims/fedele-2017.yaml | grep -v "^\S*\s*-\? *[a-z_]*: " | head; git status --short
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
?? claims/fedele-2017.yaml
?? scripts
```

**Agent**

I wrote `claims/fedele-2017.yaml`: 20 claims. The quote checker reports 18 quotes, 19 statistical values and 0 problems. Nothing is committed.

**Text read**
- The version of record (PMC5653833, from the JATS XML): main text, Tables 1 and 2, figure legends and Methods.
- The supplement, which holds only Table S1 (per-channel rates). Its text kept the names and rates but lost the colours. I rendered the PDF page to read them: gray marks excluded channels, red marks resected channels, and green marks the HFO area of each HFO type.
- The linked repository, HFO-detect-matlab at commit f397367. It holds only the HFO detectors. There is no code for the FRandR overlap, the rates, the HFO area, the test-retest analysis, the outcome statistics or the spectral analysis, so those methods come from the paper alone.

**Claims**
- **Counts:** 20 claims, 18 with quotes. The other two (ripple and FR resection per patient, and the ripple and FR rows of Table 2) are marked `inferred`, read from the tables. 4 claims carry statistics and all 20 have criteria.
- **Coverage:**
  - The cohort, and nights and intervals per patient.
  - HFO amplitudes.
  - Follow-up time by outcome, a claim of absence (Wilcoxon p = 0.25).
  - Table S1 rates and HFO areas.
  - Patient 4 (Fig. 1), patient 17 (Fig. 2) and patient 1 (Fig. 3).
  - Whether the FRandR, ripple and FR areas were resected, patient by patient.
  - The Table 2 values for FRandR, ripples and FR, and that FRandR is more specific than ripples or FR.
  - The Engel class I results.
  - The seizure onset zone in the ETE patients.
  - Test-retest results for the whole group and by subgroup.
  - The spectral classes, and no TLE/ETE difference in them (a claim of absence).
  - Where the HFO area lay in patients 18 to 20.
- **Data:** every claim uses `data: dataset`. The resected channels come from Table S1 (red) unless the deposit marks them.

**Details the paper leaves open, with the readings named**
- **Channel rate over intervals:** (a) all events over total time, (b) mean of per-interval rates, (c) mean of per-night means, (d) a channel is in the area when it is in at least half of the per-interval areas. The Table S1 rates decide among (a) to (c); (d) is a variant.
- **Channels in the 95th percentile:** the non-gray channels or all channels. "Exceeds" is read as strictly greater; greater-or-equal is a variant. The percentile method is fixed by the paper (Matlab `prctile`).
- **HFO type behind the Table 1 test-retest values:** FRandR, ripples or FR.
- **Permutation null:** one per interval pair, or one pooled per patient.
- **Amplitude:** taken on the band-filtered or the raw signal, and pooled over all channels or only non-excluded ones.
- **Follow-up test:** rank-sum by normal approximation with continuity correction (main) or exact.
- **Chi-square test:** Pearson uncorrected, Yates, or Fisher. On the paper's counts, its p = 0.002 fits uncorrected Pearson, but its Engel p = 0.001 fits Yates or Fisher.
- **Confidence intervals:** Clopper-Pearson reproduces every printed interval except one bound (see below). The asymptotic method the Methods name for n > 10 is a variant.
- **Spectral analysis:** window centre, signal transformed, starting values for the gaussian fit, and what counts as a peak.
- **TLE/ETE spectral test:** the paper names none; chi-square is the main reading and a rank-sum test a variant.
- **TLE "irrespective of outcome":** read as all TLE patients pooled, because Table 1 itself gives 0.835 for the poor-outcome TLE patients.

**Inconsistencies in the paper, recorded in the opening comment**
- The specificity CI is 78–100% in the Results and 75–100% in the Discussion; Clopper-Pearson gives 75.
- The TLE test-retest median above conflicts with Table 1.
- The Fig. 1 legend labels PR as "posterior hippocampus left".
- Patient 19's grid is 4 × 8 in the Discussion and 8 × 4 in Table 1.

**Missing from the paper**
- The seizure onset zone channels are given only for patient 17 (Fig. 2B). The claims on the ETE patients' onset zone and on patient 17's onset zone need them; their criteria say so.
- The paper's own analysis code is not public.

## End of run

31 turns, 5 minutes, $1.66 at API prices, result: success.
