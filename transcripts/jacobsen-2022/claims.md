# jacobsen-2022 · claims · run 43669007533

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
grep -n "^#" docs/protocol.md; ls paper/ claims/ | head -50
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -n 1,200p docs/protocol.md; ls -la paper/
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cat claims/fouke-2025.yaml | head -150; cat papers/datasets/jacobsen-2022.yaml
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
[... 137 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "paper/10.1016-j.crmeth.2022.100221.txt"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1016-j.crmeth.2022.100221.txt",
 "offset": 650,
 "limit": 650
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1016-j.crmeth.2022.100221.txt",
 "offset": 1300,
 "limit": 600
}
```

Result: not kept, because it reads the paper's text.

**Agent**

Full text, STAR Methods and supplement tables are present. The supplementary figure pages (23 to 26) came out as images with no text, so I'm reading those pages from the PDF.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1016-j.crmeth.2022.100221.pdf",
 "pages": "23-26"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd $TMPDIR && python -c "
import fitz
d=fitz.open('paper/10.1016-j.crmeth.2022.100221.pdf')
for i in [22,23,24,25,4,8]:
    p=d[i]; p.get_pixmap(dpi=110).save(f'p{i+1}.png')
print(len(d))
"; ls $TMPDIR
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
pip install --quiet pymupdf 2>&1 | tail -2; python -c "
import fitz,os
t=os.environ['TMPDIR']
d=fitz.open('paper/10.1016-j.crmeth.2022.100221.pdf')
for i in [22,23,24,25,4]:
    d[i].get_pixmap(dpi=110).save(f'{t}/p{i+1}.png')
print(len(d))
"; ls $TMPDIR
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
pip install --quiet --target $TMPDIR/py pymupdf 2>&1 | tail -2; PYTHONPATH=$TMPDIR/py python -c "
import fitz,os
t=os.environ['TMPDIR']
d=fitz.open('paper/10.1016-j.crmeth.2022.100221.pdf')
for i in [22,23,24,25,4]:
    d[i].get_pixmap(dpi=110).save(f'{t}/p{i+1}.png')
print(len(d))
"; ls $TMPDIR
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/p23.png"
}
```

Result: no output.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/p24.png"
}
```

Result: no output.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/p25.png"
}
```

Result: no output.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/p26.png"
}
```

Result: no output.

**Agent calls Bash**

```bash
PYTHONPATH=$TMPDIR/py python -W ignore -c "
import pymupdf,os
t=os.environ['TMPDIR']
d=pymupdf.open('paper/10.1016-j.crmeth.2022.100221.pdf')
p=d[8]; r=p.rect
p.get_pixmap(dpi=160, clip=pymupdf.Rect(0,0,r.width,r.height*0.62)).save(f'{t}/p9.png')
"
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/p9.png"
}
```

Result: no output.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/p5.png"
}
```

Result: no output.

**Agent calls Bash**

```bash
curl -s https://api.dandiarchive.org/api/dandisets/000230/versions/0.220506.1516/ | python -c "import json,sys;d=json.load(sys.stdin);print(d.get('name'));print(d.get('description'))"; ls tools/claims_check.py; grep -n "schema_version\|kind\|statistics\|ci\b" tools/claims_check.py | head -30
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
sed -n 1,140p tools/claims_check.py; grep -rh "^  data:\|^    data:\|^  kind:" claims/*.yaml | sort | uniq -c
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

[... 99 more lines not kept]
```

**Agent calls Bash**

```bash
python -c "
import json;s=json.load(open('schemas/claims.schema.json'))
print(json.dumps(s,indent=1)[:6000])"
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
[... 181 more lines not kept]
```

**Agent calls Bash**

```bash
python -c "
import json;s=json.load(open('schemas/claims.schema.json'))
print(json.dumps(s,indent=1)[6000:12000])"; grep -l "histolog\|not deposited\|not in the dataset" claims/*.yaml | head -5
```

```
required": [
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
    "properties": {
[... 138 more lines not kept]
```

**Agent**

Supplementary legends read from the PDF. The paper links no analysis code ("This paper does not report original code"). Now reading pie-chart proportions in Figures 3 and 4.

**Agent calls Bash**

```bash
PYTHONPATH=$TMPDIR/py python -W ignore -c "
import pymupdf,os
t=os.environ['TMPDIR']
d=pymupdf.open('paper/10.1016-j.crmeth.2022.100221.pdf')
for i in [5,6]:
    p=d[i]; r=p.rect
    p.get_pixmap(dpi=150, clip=pymupdf.Rect(0,0,r.width,r.height*0.75)).save(f'{t}/q{i+1}.png')
"
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/q6.png"
}
```

Result: no output.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/q7.png"
}
```

Result: no output.

**Agent**

Now writing the claims file.

**Agent calls Write**

```json
{
 "file_path": "claims/jacobsen-2022.yaml",
 "content": "# Claims for Jacobsen, Nair, Obenhaus, Donato, Slettmoen, Moser & Moser (2022), \"All-viral\n# tracing of monosynaptic inputs to single birthdate-defined neurons in the intact brain\",\n# Cell Reports Methods 2, 100221, tested on DANDI:000230.\n#\n# Written by an agent (model \"claude-opus-5-5\", Claude Code, runner \"GitHub Actions\"),\n# 2026-11-15, protocol pilot-14 as stated in docs/protocol.md.\n#\n# Text read: the version of record (PDF supplied by a person, paper and supplement), as\n# paper/10.1016-j.crmeth.2022.100221.txt: main text, figure legends, STAR Methods, and the\n# supplement's Tables S1 and S2. The supplement's Figures S1 to S4 and their legends are images\n# in the PDF and do not appear in the text; they were read from PDF pages 23 to 26. Values read\n# from figures (pie charts of Figures 3 and 4, latency, fidelity and firing rates printed in\n# Figures 5C, S3 and S4) were read from the PDF and are marked as such.\n#\n# Code: the paper reports no original code (\"This paper does not report original code\"). The\n# STAR Methods say the electrophysiology was analysed \"with custom Python code ... as reported\n# in Rowland et al. (2018)\" (eLife 7, doi:10.7554/eLife.36664), and that head direction score and\n# mean vector length were calculated as described there. No repository is linked, so none was\n# read. Where a criterion needs a cell classification or score, it is taken from Rowland et al.\n# (2018), as the Methods direct; the reader has not read that paper, and the author takes the\n# definitions and thresholds from it.\n#\n# Data the paper used.\n# - Single-cell tracing (Figures 2 to 4, S2; Table S1): 31 wild-type C57BL/6JBomTac mice\n#   injected in utero at E13 with diluted AAV-CKII-Cre, then as adults with AAV-hS-FLEX-TVA-HA-\n#   N2cG into the right dorsal hippocampus and, at least 2 weeks later, RABV-tdTomato (or\n#   RABV-ChR2-YFP for animal 59457); perfused 16 to 30 days after the rabies injection. Measured\n#   by histology (40 um sagittal sections, antibody staining for HA or 2A helper tags, confocal\n#   checks of colocalization): starter cells, rabies-positive cells in the dorsal hippocampus and\n#   entorhinal cortex, their spread along the longitudinal axis, and input cell types. Four\n#   control mice (Table S2, 99864, 99584, 99877, 99878) had no Cre and 28 days of rabies.\n# - Optogenetic tagging (Figures 5, S3, S4; Table S2): two mice. Mouse 58313 (F, E12 undiluted\n#   Cre in utero, 404.8 nl helper virus, RABV-ChR2-YFP, perfused 30 days after rabies; Figures 5\n#   and S4) and mouse 70375 (M, Cre and helper virus mixed and injected as an adult, RABV-ChR2-\n#   YFP, 20 days; Figure S3). Each carried an optrode (four tetrodes, 16 channels, optic fibre)\n#   in the right MEC. Sessions 14 to 19 days after the rabies injection, up to two per day: about\n#   30 min of open-field foraging (1 x 1 m box, white cue card), then laser trials in a holding\n#   box (473 nm, 1 ms pulses at 10 Hz, 7.5 to 15.14 mW at the patch cable). Spikes stored at\n#   48 kHz, position and head direction from two LEDs at 50 Hz, laser TTL on a digital input.\n#   Spikes of both parts were sorted together with KlustaKwik and manual refinement. Cells are\n#   labelled in the figures by tetrode (T) and cell ID (C).\n# - Two-photon imaging (Figures 6, 7): mouse 58253 (E14, RABV-GCaMP6f, prism, benchtop\n#   microscope, about 30 Hz) and mouse 60388 (E13 single-cell protocol, AAV-Syn-GCaMP6m in MEC,\n#   RABV-tdTomato, GRIN lens and prism, two-photon miniscope at about 7.52 Hz). Traces are dF/F\n#   from Suite2p ROIs.\n#\n# The Data and code availability section says the electrophysiology data were deposited on\n# DANDI (000230, version 0.220506.1516). The archive's title and description name the paper and\n# the photostimulation power set points (20 and 40 mW set, 7.5 and 15.1 mW actual). The\n# histology counts and the imaging data are not said to be deposited anywhere; the claims on\n# them are listed with data from the paper's own recordings, and the author will find whether\n# the dandiset holds them. The counts of Table S1 are printed in the supplement.\n#\n# Shared definitions, from the STAR Methods (\"Analysis of electrophysiology data\").\n# - Latency: the mean, over laser pulses followed by a spike within 10 ms, of the time from the\n#   pulse to the first spike; pulses with no spike within 10 ms are left out.\n# - Fidelity: the percentage of laser pulses followed by a spike within 10 ms.\n# - Open: the time of a pulse. Readings (a) the TTL onset, (b) the TTL offset 1 ms later. (a) is\n#   the plain reading of \"the average time between a laser pulse ... and the first spike\".\n# - Open: what makes a cell \"responsive\". The Results say cells \"responded robustly to laser\n#   stimulation with a 2- to 4-ms latency\" and the Figure 5C legend says \"robust and reliable\n#   responses\"; no threshold is given. Readings (R-a) latency between 2 and 4 ms and fidelity at\n#   least 11.64%, the lowest fidelity among the cells Figure 5C shows as responsive; (R-b)\n#   latency between 2 and 4 ms and more pulses followed by a spike within 10 ms than pulses\n#   preceded by one in the 10 ms before (one-sided paired test, p < 0.05).\n# - Open-field firing rate: the values above the path plots are \"the average firing rate for\n#   the open field session\", read as spikes over session duration.\nschema_version: 2\npaper: doi:10.1016/j.crmeth.2022.100221\nclaims:\n- id: fig2a-four-or-fewer-starters\n  statement: With the single-cell protocol, starter cells could be identified conclusively in 15\n    of 31 animals (48%), and each of these had four or fewer starter cells.\n  source: Results, A virus-based method for targeting a single cell and identifying its inputs,\n    paragraph 4; Figure 2A\n  quote: With this approach, we could unambiguously target four or fewer starter cells in 48% of\n    animals (15 of 31) (Figure 2A)\n  expected:\n  - quantity: fraction of animals with conclusive starter cells\n    value: 48.4\n    tolerance: 4.8\n    unit: percent\n  - quantity: animals with conclusive starter cells\n    value: 15\n    tolerance: 1.5\n    unit: animals\n  criterion: Counted from histology, with the classification of the STAR Methods\n    (Conclusive/inconclusive classification) over the 31 animals of Table S1, after the\n    exclusions the Methods name (two missed injections, one lost section). Reproduced when the\n    count and fraction are within tolerance and no conclusive animal has more than four starter\n    cells.\n- id: fig2a-starter-count-distribution\n  statement: Among the 31 single-cell animals, 4 had zero starter cells, 5 one, 2 two, 2 three\n    and 2 four, and 16 were inconclusive.\n  source: Figure 2A; Table S1\n  inferred: Counts read from the bar chart of Figure 2A and the Starter cells column of Table\n    S1; no sentence gives them.\n  expected:\n  - quantity: animals with 0 starter cells\n    value: 4\n  - quantity: animals with 1 starter cell\n    value: 5\n  - quantity: animals with 2 starter cells\n    value: 2\n  - quantity: animals with 3 starter cells\n    value: 2\n  - quantity: animals with 4 starter cells\n    value: 2\n  - quantity: inconclusive animals\n    value: 16\n  criterion: Counts of animals are small integers, so they are to match exactly (a tolerance of\n    10% is less than one animal). Reproduced when all six counts match.\n- id: fig2a-single-starter-rate\n  statement: A single starter cell was labelled in 5 of the 15 conclusive animals (33%), an\n    overall success rate of 16% (5 of 31) for targeting a single hippocampal cell.\n  source: Results, A virus-based method for targeting a single cell and identifying its inputs,\n    paragraph 4; Figure 2A\n  quote: In this group, a single starter cell was labeled 33% of the time (5 of 15) (Figure 2A),\n    resulting in an overall success rate of 16% (5 of 31) for targeting a single cell in the\n    hippocampus\n  expected:\n  - quantity: single starter cell, fraction of conclusive animals\n    value: 33\n    tolerance: 3.3\n    unit: percent\n  - quantity: single starter cell, fraction of all animals\n    value: 16\n    tolerance: 1.6\n    unit: percent\n  depends_on:\n  - fig2a-four-or-fewer-starters\n- id: no-starter-cells-in-mec\n  statement: No starter cells were found in the MEC.\n  source: Results, A virus-based method for targeting a single cell and identifying its inputs,\n    paragraph 3\n  quote: No starter cells were found in the MEC.\n  criterion: Reproduced when no cell in the entorhinal sections of the single-cell animals shows\n    both a helper tag and the rabies payload under the STAR Methods classification.\n- id: fig2b-rabies-cells-increase-with-time\n  statement: The number of rabies-positive cells in the ipsilateral dorsal hippocampus increases\n    with the days after the rabies injection (Spearman R = 0.58, p = 0.0014, n = 27 animals).\n  source: Figure 2B, left, and legend; Results, A virus-based method for targeting a single cell\n    and identifying its inputs, paragraph 4\n  quote: the total number of rabies-positive cells observed in the ipsilateral dorsal hippocampus\n    increases as a function of days after the rabies injection (R = 0.58, p = 0.0014, Spearman's\n    rho, n = 27 animals not including control animals)\n  statistics:\n  - test: Spearman's rho\n    statistic: R = 0.58\n    p: 0.0014\n    n: 27 animals, single-cell animals without the four with zero starter cells, no controls\n  expected:\n  - quantity: Spearman R, rabies-positive cells in dorsal hippocampus against days with rabies\n    value: 0.58\n    tolerance: 0.058\n  criterion: Over the animals of Table S1 with rabies-positive cells (the legend leaves out\n    animals with zero starter cells and the control animals), Spearman's rank correlation of\n    the count of rabies-positive cells in the dorsal hippocampus (starter cells included, as in\n    Table S1) against days with rabies. Reproduced when R is within tolerance and p < 0.05.\n- id: fig2b-conclusive-more-than-control\n  statement: Conclusive animals (days 26 to 30) have more rabies-positive cells in the dorsal\n    hippocampus than the no-Cre control animals, which were all inconclusive.\n  source: Figure 2B, right, and legend\n  quote: the number of rabies-positive cells is larger in conclusive animals compared with control\n    animals, which were all inconclusive (p = 0.0159, Wilcoxon rank-sum test, n = 5 conclusive and\n    4 control animals\n  statistics:\n  - test: Wilcoxon rank-sum test\n    p: 0.0159\n    n: 5 conclusive and 4 control animals\n  criterion: Conclusive animals with 26 to 30 days of rabies (the x-axis label of the panel; in\n    Table S1 these are 60652, 60823, 60259, 60824 and 60219) against the four no-Cre controls of\n    Table S2. Two-sided Wilcoxon rank-sum test of the counts. Reproduced when p < 0.05 with the\n    conclusive median higher. With 5 and 4 animals and no ties, complete separation gives the\n    exact two-sided p of 0.0159.\n- id: figs2a-spread-increases-with-time\n  statement: The spread of rabies-positive cells along the longitudinal axis of the dorsal\n    hippocampus increases with days after the rabies injection (Spearman r = 0.54, p = 0.0036,\n    n = 27 animals).\n  source: Figure S2A, left, and legend; Results, A virus-based method for targeting a single cell\n    and identifying its inputs, paragraph 4\n  quote: longer expression times of the RABV increased the number of rabies-positive cells (Figure\n    2B), the anatomical area over which they were found in the dorsal hippocampus (Figure S2A)\n  statistics:\n  - test: Spearman's rho\n    statistic: r = 0.54\n    p: 0.0036\n    n: 27 animals, not including control animals\n  expected:\n  - quantity: Spearman r, spread against days with rabies\n    value: 0.54\n    tolerance: 0.054\n  criterion: The legend of Figure S2A (read from the PDF; the supplement's legends are not in\n    the text) says spread is \"calculated based on the number of sections in which rabies-positive\n    cells were observed\", leaving out the ventral hippocampus; sections are 40 um sagittal\n    sections (STAR Methods, Histology). Spread in um is read as that number of sections times\n    40 um. Reproduced when Spearman r is within tolerance and p < 0.05 over the same 27 animals\n    as fig2b-rabies-cells-increase-with-time.\n- id: figs2a-conclusive-spread-more-than-control\n  statement: The spread of rabies-positive cells in the hippocampus is larger in conclusive\n    animals (days 26 to 30) than in no-Cre controls (p = 0.0317, Wilcoxon rank sum, 5 and 4\n    animals).\n  source: Figure S2A, right, and legend; Results, A virus-based method for targeting a single cell\n    and identifying its inputs, paragraph 5\n  quote: Although some spurious rabies expression was observed in the hippocampus, the number and\n    anatomical ... spread of rabies-positive cells was significantly lower than in conclusive\n    animals (Figures 2B and S2A)\n  statistics:\n  - test: Wilcoxon rank sum\n    p: 0.0317\n    n: 5 conclusive and 4 control animals\n  criterion: The same animals as fig2b-conclusive-more-than-control and the spread measure of\n    figs2a-spread-increases-with-time; two-sided Wilcoxon rank-sum test. Reproduced when\n    p < 0.05 with the conclusive median higher.\n- id: figs2b-mec-inputs-increase-with-time\n  statement: Longer rabies expression increases the number of input cells labelled in the MEC;\n    MEC-labelled cells appear only in animals with 22 or more days of rabies.\n  source: Results, A virus-based method for targeting a single cell and identifying its inputs,\n    paragraph 4; Figure S2B\n  quote: As expected, longer expression times of the RABV increased ... as well as the number of\n    input cells labeled in the more distant MEC (Figure S2B)\n  criterion: The paper reports no test for this panel. Counts of rabies-positive cells in the\n    ipsilateral MEC against days with rabies over the 27 animals of fig2b-rabies-cells-increase-\n    with-time. Readings (a) Spearman's rank correlation positive with p < 0.05, the test the\n    paper uses for the parallel panels Figures 2B and S2A; (b) no animal below 22 days has MEC\n    cells, as the panel shows. Reproduced when a reading holds. Table S1 gives entorhinal cortex\n    counts (EC), and Figure S2B MEC counts; the two are taken to be the same cells, which the\n    paper does not state.\n- id: controls-no-mec-spread\n  statement: In no-Cre control animals rabies did not spread to the MEC, even with 2.5 times the\n    volume and a higher titre (10^11 infectious particles/ml) of helper virus.\n  source: Results, A virus-based method for targeting a single cell and identifying its inputs,\n    paragraph 5; Figures S2B and S1C\n  quote: and spread to the MEC did not occur (Figure S2B), not even when a larger volume (2.5\n    times more) and higher titer (1011 infectious particles/ml) of the helper virus were used\n    (Figure S1C)\n  criterion: Reproduced when the four no-Cre controls of Table S2 (28 days) and the high-titre\n    control 79986 (138 nl, 14 days) have no rabies-positive cells in the MEC.\n- id: figs1a-no-expression-without-tva\n  statement: Without Cre and helper virus, RABV-tdTomato alone produces no tdTomato expression\n    in the hippocampus, so unpseudotyped rabies virus does not contribute to the labelling.\n  source: Results, A virus-based method for targeting a single cell and identifying its inputs,\n    paragraph 5; Figure S1A, left\n  quote: This can be due to the presence of unpseudotyped RABVs ... The former does not seem to be\n    an issue here (Figure S1A)\n  criterion: Reproduced when mouse 72359 (Table S2, RABV-tdTomato only, 14 days) shows no\n    tdTomato-expressing cells in the hippocampus.\n- id: figs1b-sparse-cre\n  statement: Diluted AAV-CKII-Cre injected in utero at E13 leaves only a few Cre-expressing\n    cells in the adult hippocampus.\n  source: Results, A virus-based method for targeting a single cell and identifying its inputs,\n    paragraph 2; Figure S1B\n  quote: only a few cells express Cre in the adult hippocampus of these animals (Figure S1B)\n  criterion: The paper gives no count. Judged on mice 58482 and 58483 (Table S2, E13, 1:500\n    Cre, AAV1-CAG-FLEX-tdTomato in the adult); reproduced when tdTomato-expressing cells in\n    their hippocampus are sparse, read as individually separable cells and not a filled layer,\n    as in the panel.\n- id: fig3-inputs-reflect-starter-identity\n  statement: The inputs of a single starter cell reflect its identity; a CA3 pyramidal starter\n    cell (16 days) and a CA2 stratum oriens interneuron starter cell (30 days) in neighbouring\n    regions received very different sets of hippocampal inputs.\n  source: Results, A virus-based method for targeting a single cell and identifying its inputs,\n    paragraph 4; Figure 3B and D\n  quote: The identity of the inputs reflected the identity of the starter cell (Figures 3 and 4),\n    which is an important indication that the RABV is indeed transsynaptic. For example, the\n    constellation of inputs a single pyramidal neuron and a single interneuron received was very\n    different despite them being located in neighboring regions (distal CA3 and CA2) in the\n    hippocampus (Figure 3)\n  expected:\n  - quantity: input cells to the CA3 pyramidal starter (animal 59457)\n    value: 7\n  - quantity: CA pyramidal cell inputs, CA3 pyramidal starter\n    value: 85.7\n    tolerance: 8.6\n    unit: percent\n  - quantity: granule cell inputs, CA3 pyramidal starter\n    value: 14.3\n    tolerance: 1.4\n    unit: percent\n  - quantity: input cells to the interneuron starter (animal 60219)\n    value: 26\n  - quantity: CA pyramidal cell inputs, interneuron starter\n    value: 65.4\n    tolerance: 6.5\n    unit: percent\n  - quantity: interneuron inputs, interneuron starter\n    value: 30.8\n    tolerance: 3.1\n    unit: percent\n  - quantity: granule cell inputs, interneuron starter\n    value: 3.8\n    tolerance: 0.4\n    unit: percent\n  criterion: Percentages read from the pie charts of Figure 3B and D; input counts from the\n    legends (n = 7 and n = 26 input cells), matching Table S1 less the starter cell. Counts are\n    to match exactly; with 7 and 26 cells each percentage is a whole number of cells, so a\n    percentage matches when the number of cells of that type matches (6 and 1 of 7; 17, 8 and 1\n    of 26). Reproduced when the counts by type match and the interneuron starter receives\n    interneuron inputs while the pyramidal starter receives none.\n- id: fig4a-distant-granule-input\n  statement: After 20 days of rabies, a single granule cell starter received input from one other\n    granule cell more than 320 um away along the longitudinal axis.\n  source: Results, Targeting single starter cells in the hippocampus highlights granule-granule\n    cell connectivity, paragraph 1; Figure 4A legend\n  quote: After 20 days of rabies expression, one granule cell was found to receive input from\n    another granule cell located several hundred micrometers away along the longitudinal axis of\n    the hippocampus (Figure 4A)\n  expected:\n  - quantity: distance from starter to input cell along the longitudinal axis, lower bound\n    value: 320\n    unit: um\n  criterion: Animal 60047 (Table S1, 20 days, 1 granule cell starter, 2 rabies cells). Reproduced\n    when the one input is a granule cell more than 320 um from the starter along the\n    longitudinal axis, as the legend states (\"more than 320 mm away\", um garbled in the text).\n- id: fig4b-granule-inputs-dominate\n  statement: After 26 days, a single granule cell starter had 35 hippocampal input cells, 80% of\n    them granule cells; subtracting the highest background count of the controls (18) still\n    leaves 58.8% granule cell inputs.\n  source: Results, Targeting single starter cells in the hippocampus highlights granule-granule\n    cell connectivity, paragraph 1; Figure 4B\n  quote: After 26 days (in a different animal), the virus had spread to a total of 35 input cells in\n    the hippocampus, 80% of which were other granule cells (Figure 4B). Even when accounting for\n    background expression, granule cells were still the dominant input type\n  expected:\n  - quantity: hippocampal input cells (animal 60652)\n    value: 35\n  - quantity: granule cell inputs\n    value: 28\n  - quantity: granule cell fraction of inputs\n    value: 80.0\n    tolerance: 8.0\n    unit: percent\n  - quantity: granule cell fraction after subtracting 18 background cells\n    value: 58.8\n    tolerance: 5.9\n    unit: percent\n  - quantity: other dentate cell fraction\n    value: 11.4\n    tolerance: 1.1\n    unit: percent\n  - quantity: glia fraction\n    value: 5.7\n    tolerance: 0.6\n    unit: percent\n  - quantity: interneuron fraction\n    value: 2.9\n    tolerance: 0.3\n    unit: percent\n  criterion: The background correction is the paper's, (28 - 18)/(35 - 18), with 18 the highest\n    rabies-positive count among the control animals. Counts are to match exactly (each type\n    fraction is a whole number of cells, 28, 4, 2 and 1 of 35); the type fractions other than\n    granule cells were read from the pie chart. Reproduced when the counts match and the\n    corrected fraction is above 50%.\n- id: fig4-subgranular-inputs\n  statement: Many granule cell inputs lay in the subgranular zone, suggesting immature granule\n    cells; 1 of 1 after 20 days and 11 of 28 after 26 days.\n  source: Results, Targeting single starter cells in the hippocampus highlights granule-granule\n    cell connectivity, paragraph 1\n  quote: a substantial number of their inputs was found in the subgranular zone (1 of 1 granule cell\n    inputs after 20 days, 11 of 28 after 26 days)\n  expected:\n  - quantity: subgranular granule cell inputs, 20 days (animal 60047)\n    value: 1\n  - quantity: subgranular granule cell inputs, 26 days (animal 60652)\n    value: 11\n  criterion: Counts are to match exactly.\n- id: fig4c-dg-starter-local-and-mec-inputs\n  statement: A single dentate gyrus starter cell (possibly a molecular layer perforant\n    path-associated interneuron) had 34 hippocampal input cells and 4 input cells in the MEC\n    after 28 days.\n  source: Figure 4C legend\n  quote: The pie chart (center left) shows the proportions of hippocampal input cell types to the\n    single starter cell highlighted on the left 28 days after the rabies injection (n = 34 input\n    cells in the hippocampus to a single starter cell)\n  expected:\n  - quantity: hippocampal input cells (animal 60259)\n    value: 34\n  - quantity: MEC input cells\n    value: 4\n  - quantity: CA pyramidal cell inputs\n    value: 41.2\n    tolerance: 4.1\n    unit: percent\n  - quantity: granule cell inputs\n    value: 32.4\n    tolerance: 3.2\n    unit: percent\n  - quantity: other dentate, glia and interneuron inputs, each\n    value: 8.8\n    tolerance: 0.9\n    unit: percent\n  criterion: Fractions read from the pie chart of Figure 4C. Counts are to match exactly (14, 11,\n    3, 3 and 3 of 34; 4 MEC cells). Reproduced when the counts match.\n- id: cytotoxicity-after-30-days\n  statement: When targeting single cells, cell damage was typically not seen until more than 30\n    days after the rabies injection; dendritic blebbing appeared at 34 days.\n  source: Discussion, paragraph 4; Figure 7A legend\n  quote: we typically did not see cell damage until more than 30 days after the rabies injection\n    when attempting to target single cells (Figure 7A)\n  criterion: The paper gives no measure of cell damage beyond the image. Reproduced when the\n    hippocampal sections of mouse 60388 (34 days) show dendritic blebbing and those of the\n    single-cell animals of Table S1 (16 to 30 days) do not, judged by eye.\n- id: fig5c-functional-cell-types\n  statement: In mice with widespread RABV-ChR2-YFP expression, MEC recordings include grid, head\n    direction and border cells, so the network as a whole is not disrupted by the rabies\n    expression.\n  source: Results, The functional properties of input cells to birthdate-defined cell populations\n    can be determined with optogenetics in vivo, paragraph 3; Figures 5C and S4\n  quote: We found several functional cell types, including grid, head direction, and border cells\n    (Figures 5C and S4), indicating that the network as a whole was not affected by the widespread\n    rabies expression\n  criterion: Open-field sessions of mice 58313 and 70375. Grid, head direction and border cells\n    are classified with the scores and thresholds of Rowland et al. (2018), which the STAR\n    Methods cite for the analysis; this paper gives no score or threshold of its own except\n    that it shows a head direction score and mean vector length (Figure S4). Reproduced when at\n    least one unit of each of the three types is found. The example units named in the figures\n    (grid cells T1 C89, 19 days, Figure 5C, and T1 C50, 19 days, Figure S4; head direction cell\n    T4 C16, 17 days; border cell T4 C50, 18 days; all mouse 58313) are reported with their\n    scores, when the dandiset's unit labels allow them to be found.\n- id: fig5c-responsive-grid-cell\n  statement: Among the cells that responded to laser stimulation with a 2 to 4 ms latency, a sign\n    of direct ChR2 activation and so of a monosynaptic projection to the hippocampus, were grid\n    cells.\n  source: Results, The functional properties of input cells to birthdate-defined cell populations\n    can be determined with optogenetics in vivo, paragraph 3; Figure 5C\n  quote: Cells that responded robustly to laser stimulation with a 2- to 4-ms latency (demonstrating\n    direct activation as opposed to later, ... included grid cells (Figure 5C)\n  depends_on:\n  - fig5c-functional-cell-types\n  criterion: Latency, fidelity and responsiveness as defined in the opening comment, with both\n    responsiveness readings (R-a, R-b) and both pulse-time readings. The 2 to 4 ms range, a\n    reported range, is widened to 1.8 to 4.4 ms. Reproduced when, under one reading, at least\n    one unit classed as a grid cell in fig5c-functional-cell-types is responsive. The number of\n    responsive units and their types are reported.\n- id: fig5c-example-cells\n  statement: Three example responsive cells of mouse 58313 had these open-field rates, latencies\n    and fidelities; a grid cell (T1 C89, 19 days) 1.10 Hz, 2.75 ms, 40.73%; a high-rate cell\n    (T1 C57, 17 days) 12.67 Hz, 3.90 ms, 35.64%; a low-rate cell (T1 C52, 17 days) 0.30 Hz,\n    2.65 ms, 11.64%.\n  source: Figure 5C\n  inferred: Values printed in the panels of Figure 5C, read from the PDF; the legend names the\n    cells and days but no sentence gives the values.\n  expected:\n  - quantity: T1 C89 open-field rate\n    value: 1.10\n    tolerance: 0.11\n    unit: Hz\n  - quantity: T1 C89 latency\n    value: 2.75\n    tolerance: 0.275\n    unit: ms\n  - quantity: T1 C89 fidelity\n    value: 40.73\n    tolerance: 4.07\n    unit: percent\n  - quantity: T1 C57 open-field rate\n    value: 12.67\n    tolerance: 1.27\n    unit: Hz\n  - quantity: T1 C57 latency\n    value: 3.90\n    tolerance: 0.39\n    unit: ms\n  - quantity: T1 C57 fidelity\n    value: 35.64\n    tolerance: 3.56\n    unit: percent\n  - quantity: T1 C52 open-field rate\n    value: 0.30\n    tolerance: 0.03\n    unit: Hz\n  - quantity: T1 C52 latency\n    value: 2.65\n    tolerance: 0.265\n    unit: ms\n  - quantity: T1 C52 fidelity\n    value: 11.64\n    tolerance: 1.16\n    unit: percent\n  criterion: Latency and fidelity as defined in the opening comment, under both pulse-time\n    readings. The units are found by tetrode and cell ID in the session of the stated day. Where\n    the dandiset does not keep those labels, the unit on tetrode 1 of that session whose\n    open-field rate is closest to the printed value is taken, and the match is marked as\n    resting on that choice. Which of the day's sessions (up to two per day) is meant is not\n    stated; each is tried. Reproduced when all nine values are within tolerance under one\n    reading; partially reproduced when the latencies all lie within 1.8 to 4.4 ms but other\n    values miss.\n- id: figs3-stable-input-cell\n  statement: The firing properties of one input cell stayed stable across six sessions on three\n    days (14, 15 and 16 days after the rabies injection); it responded to every laser session\n    with a latency of 2.50 to 2.95 ms.\n  source: Results, The functional properties of input cells to birthdate-defined cell populations\n    can be determined with optogenetics in vivo, paragraph 3; Figure S3B\n  quote: The firing properties of an individual input cell were also found to remain stable for at\n    least 3 days of continuous rabies expression (Figure S3)\n  expected:\n  - quantity: open-field rate, day 14 sessions 1 and 2\n    value: 0.89\n    tolerance: 0.089\n    unit: Hz\n  - quantity: open-field rate, day 14 session 2\n    value: 1.06\n    tolerance: 0.106\n    unit: Hz\n  - quantity: open-field rate, day 15 session 1\n    value: 0.28\n    tolerance: 0.028\n    unit: Hz\n  - quantity: open-field rate, day 15 session 2\n    value: 1.61\n    tolerance: 0.161\n    unit: Hz\n  - quantity: open-field rate, day 16 session 1\n    value: 0.95\n    tolerance: 0.095\n    unit: Hz\n  - quantity: open-field rate, day 16 session 2\n    value: 1.84\n    tolerance: 0.184\n    unit: Hz\n  - quantity: latencies, six sessions in order\n    value: 2.83\n    tolerance: 0.283\n    unit: ms\n  - quantity: latency, day 14 session 2\n    value: 2.95\n    tolerance: 0.295\n    unit: ms\n  - quantity: latency, day 15 session 1\n    value: 2.77\n    tolerance: 0.277\n    unit: ms\n  - quantity: latency, day 15 session 2\n    value: 2.77\n    tolerance: 0.277\n    unit: ms\n  - quantity: latency, day 16 session 1\n    value: 2.58\n    tolerance: 0.258\n    unit: ms\n  - quantity: latency, day 16 session 2\n    value: 2.50\n    tolerance: 0.25\n    unit: ms\n  - quantity: fidelity, day 14 session 1\n    value: 27.64\n    tolerance: 2.76\n    unit: percent\n  - quantity: fidelity, day 14 session 2\n    value: 48.00\n    tolerance: 4.80\n    unit: percent\n  - quantity: fidelity, day 15 session 1\n    value: 68.71\n    tolerance: 6.87\n    unit: percent\n  - quantity: fidelity, day 15 session 2\n    value: 64.36\n    tolerance: 6.44\n    unit: percent\n  - quantity: fidelity, day 16 session 1\n    value: 76.73\n    tolerance: 7.67\n    unit: percent\n  - quantity: fidelity, day 16 session 2\n    value: 81.82\n    tolerance: 8.18\n    unit: percent\n  criterion: Mouse 70375 (Table S2). Values printed in the panels of Figure S3B, read from the\n    PDF, in session order (left to right). Laser trials were 1 ms pulses at 10 Hz and 7.5 mW\n    (legend of Figure S3B). The paper does not say how the same cell was matched across\n    sessions; the Methods say the tetrodes were not turned down between these sessions. The\n    unit is taken as the one sorted under the same cluster label in all six sessions when the\n    dandiset keeps one; otherwise as the unit whose waveform on the four channels best matches\n    across sessions, a choice the paper does not make and which is marked as an assumption.\n    Reproduced when the unit is found in all six sessions, every latency lies within 1.8 to 4.4\n    ms, and at least 15 of the 18 values are within tolerance; partially reproduced when the\n    unit is found and responsive in every session but fewer values match.\n- id: figs4-nonresponsive-cells\n  statement: Some MEC cells recorded in the same area did not respond to laser stimulation,\n    among them a head direction cell (T4 C16, 17 days, head direction score 0.81, mean vector\n    length 0.90, peak rate 9.02 Hz, open-field rate 1.05 Hz), a border cell (T4 C50, 18 days,\n    1.69 Hz) and a grid cell (T1 C50, 19 days, 0.78 Hz).\n  source: Figure S4\n  inferred: Read from Figure S4 and its legend in the PDF (the supplement's legends are not in\n    the text); no sentence of the main text states it.\n  expected:\n  - quantity: T4 C16 head direction score\n    value: 0.81\n    tolerance: 0.081\n  - quantity: T4 C16 mean vector length\n    value: 0.90\n    tolerance: 0.09\n  - quantity: T4 C16 peak firing rate of the head direction tuning curve\n    value: 9.02\n    tolerance: 0.90\n    unit: Hz\n  - quantity: T4 C16 open-field rate\n    value: 1.05\n    tolerance: 0.105\n    unit: Hz\n  - quantity: T4 C50 open-field rate\n    value: 1.69\n    tolerance: 0.169\n    unit: Hz\n  - quantity: T1 C50 open-field rate\n    value: 0.78\n    tolerance: 0.078\n    unit: Hz\n  criterion: Mouse 58313; laser trials of 1 ms pulses at 10 Hz and 7.5 mW (legend). Head\n    direction score and mean vector length as in Rowland et al. (2018), as the STAR Methods\n    state. Units found as in fig5c-example-cells. Reproduced when the three units are not\n    responsive under either responsiveness reading and the values are within tolerance.\n- id: responsive-cells-at-19-days\n  statement: Laser-responsive cells with clear spatial firing patterns could be identified for at\n    least 19 days after the rabies injection.\n  source: Results, The functional properties of input cells to birthdate-defined cell populations\n    can be determined with optogenetics in vivo, paragraph 3; Figure 5C\n  quote: responsive cells with clear spatial firing patterns could be identified for at least 19\n    days after the rabies injection (Figure 5C)\n  depends_on:\n  - fig5c-responsive-grid-cell\n  criterion: Reproduced when a session 19 or more days after the rabies injection holds a unit\n    that is responsive (either reading) and classed as a grid, head direction or border cell\n    under Rowland et al. (2018). \"Clear spatial firing patterns\" is read as one of these\n    classes; the paper's example is the grid cell T1 C89.\n- id: mec-inputs-from-two-weeks\n  statement: In the optogenetic experiments, input cells could be detected in the MEC from about\n    2 weeks after the rabies injection.\n  source: Results, The functional properties of input cells to birthdate-defined cell populations\n    can be determined with optogenetics in vivo, paragraph 3\n  quote: In these experiments, input cells could be detected in the MEC from approximately 2 weeks\n    after the rabies injection.\n  criterion: The sentence does not say whether detection was by recording or by histology. Read\n    as detection by recording, the test available in the dandiset; reproduced when the earliest\n    session holding a responsive unit (either reading) is about 14 days after the rabies\n    injection (12 to 16 days, 2 weeks widened by 10% of each bound around 14 days, read as 14\n    plus or minus 1.4 days, rounded out). Figure S3 shows such a unit at day 14.\n- id: fig6b-imaged-input-cells\n  statement: Two-photon imaging through a prism in a head-fixed mouse identified several MEC cells\n    expressing RABV-GCaMP6f, that is, cells projecting to an E14 birthdate-matched hippocampal\n    population; five such cells were imaged 19 days after the rabies injection, with different\n    activity onsets.\n  source: Results, In vivo two-photon calcium imaging enables functional detection of distant input\n    cells to birthdate-defined cell populations, paragraph 1; Figure 6B\n  quote: This enabled us to perform two-photon imaging in awake, head-fixed mice and identify\n    several cells projecting to a population of birthdate-matched cells in the hippocampus\n    (Figure 6B)\n  expected:\n  - quantity: imaged input cells in the field of view\n    value: 5\n  criterion: Mouse 58253, benchtop recording 19 days after the rabies injection, about 2 min long\n    (legend), Suite2p ROIs and dF/F as in the STAR Methods (neuropil coefficient 0.7; baseline\n    the median of the lowest 20% of frames after Hanning smoothing; the window length is not\n    given and is a standard choice). Reproduced when five cells are found in the field and\n    at least two show calcium transients with different onset times.\n- id: fig7b-dual-labelled-input-cell\n  statement: With GCaMP6m expressed in the MEC by AAV and RABV-tdTomato injected into the\n    hippocampus, a two-photon miniscope identified in vivo an MEC cell expressing both, an input\n    to the targeted hippocampal starter cells, next to a GCaMP6m-only cell, 29 days after the\n    rabies injection.\n  source: Results, In vivo two-photon calcium imaging enables functional detection of distant input\n    cells to birthdate-defined cell populations, paragraph 2; Figure 7B\n  quote: When the RABV reached the MEC, we were able to identify a cell expressing both the calcium\n    indicator and tdTomato in vivo with a two-photon miniscope (Figure 7B\n  criterion: Mouse 60388, miniscope recording 29 days after the rabies injection, dual channel.\n    Reproduced when a GCaMP6m ROI with calcium transients coincides with a tdTomato-positive cell\n    in the mean red-channel image.\n"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
f=claims/jacobsen-2022.yaml
python - <<'EOF'
p='claims/jacobsen-2022.yaml'
s=open(p).read()
s=s.replace("open-field rate, day 14 sessions 1 and 2","open-field rate, day 14 session 1")
s=s.replace("quantity: latencies, six sessions in order","quantity: latency, day 14 session 1")
old="""injection (12 to 16 days, 2 weeks widened by 10% of each bound around 14 days, read as 14
    plus or minus 1.4 days, rounded out). Figure S3 shows such a unit at day 14."""
new="""injection, within 10% of 14 days (12.6 to 15.4 days). Figure S3 shows such a unit at day
    14."""
assert old in s; s=s.replace(old,new)
open(p,'w').write(s)
import yaml
d=yaml.safe_load(s)
def walk(x,path=""):
    if isinstance(x,dict):
        for k,v in x.items(): walk(v,path+"/"+str(k))
    elif isinstance(x,list):
        for i,v in enumerate(x): walk(v,path+f"[{i}]")
    elif isinstance(x,str) and (": " in x or "—" in x or "rather" in x): print("BAD",path,x[:80])
walk(d)
EOF
python tools/claims_check.py $f paper/10.1016-j.crmeth.2022.100221.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
f=claims/jacobsen-2022.yaml
python - <<'EOF'
p='claims/jacobsen-2022.yaml'
s=open(p).read()
old="quote: This enabled us to perform two-photon imaging in awake, head-fixed mice and identify"
assert old in s
s=s.replace(old,"quote: This enabled us to perform ... imaging in awake, head-fixed mice and identify")
open(p,'w').write(s)
EOF
python tools/claims_check.py $f paper/10.1016-j.crmeth.2022.100221.txt
```

Result: not kept, because it reads the paper's text.

**Agent**

All quotes pass. The two flagged p-values are in the Figure S2A legend, which exists only as an image (PDF page 24), where I confirmed them. I'll note that in the file header.

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/jacobsen-2022.yaml",
 "old_string": "# Figures 5C, S3 and S4) were read from the PDF and are marked as such.",
 "new_string": "# Figures 5C, S3 and S4) were read from the PDF and are marked as such. The quote checker cannot\n# find the p-values 0.0036 and 0.0317 (Figure S2A legend) because that legend is not in the\n# text; both were confirmed by reading PDF page 24."
}
```

```
The file claims/jacobsen-2022.yaml has been updated successfully. (note: the file had been modified on disk since you last read it — the edit applied cleanly, but the file contains other changes not in your context. Read it before edits that depend on surrounding content.)
```

**Agent calls Bash**

```bash
python tools/claims_check.py claims/jacobsen-2022.yaml paper/10.1016-j.crmeth.2022.100221.txt; git status --short claims/; grep -c "criterion:" claims/jacobsen-2022.yaml; grep -c "statistics:" claims/jacobsen-2022.yaml
```

Result: not kept, because it reads the paper's text.

**Agent**

I wrote `claims/jacobsen-2022.yaml` with 27 claims. All 24 quotes pass the checker. The checker still reports 2 problems: two p-values it cannot find in the text file. Both are in the Figure S2A legend, which exists only as an image in the PDF. I read them on PDF page 24 and noted this in the file header. Nothing is committed.

**Text read**
- Version of record (Cell Reports Methods 2, 100221), with STAR Methods and Supplementary Tables S1 and S2 from the `.txt` file.
- Figures S1 to S4 and their legends are images only, so I read them from PDF pages 23 to 26. I also read the values printed in Figures 3, 4 and 5C from the PDF.
- The paper says "This paper does not report original code", so there was no repository to read. The Methods send the electrophysiology analysis, including the head direction score and mean vector length, to Rowland et al. 2018 (eLife). The criteria point the author there for those definitions, and I did not read that paper.

**Claims**
- 27 claims: 24 with quotes, 3 marked `inferred`. Those three hold values read from figures: Fig 2A starter-count distribution, Fig 5C example cells, Fig S4 non-responsive cells.
- 4 claims carry statistics:
  - two Spearman correlations: R = 0.58, p = 0.0014; r = 0.54, p = 0.0036
  - two Wilcoxon rank-sum tests: p = 0.0159 and p = 0.0317
- 26 claims have criteria.
- Topics covered: success rates, the starter-count distribution, rabies spread over time and against controls, input cell composition for the single starter cells in Figs 3 and 4, specificity controls (S1), cytotoxicity, the optogenetic tagging results (Figs 5C, S3, S4), and the two imaging examples (Figs 6B, 7B).

**Details the paper leaves open, with the readings named**
- **Pulse time for latency and fidelity:** (a) TTL onset, (b) TTL offset.
- **What makes a cell "responsive":** (R-a) latency 2 to 4 ms and fidelity at least 11.64%, the lowest fidelity among the cells Figure 5C shows as responsive; (R-b) latency 2 to 4 ms and significantly more spikes in the 10 ms after pulses than in the 10 ms before.
- **Grid, head direction and border cell classification:** this paper gives no scores or thresholds of its own, so the criteria defer to Rowland et al. 2018, as its Methods do.
- **Units in the figures:** the cells are labelled by tetrode and cell ID (T1 C89 etc.). If the dandiset does not keep those labels, the fallback is a rate match on the same tetrode. Which of a day's two sessions is meant is also unstated, so each is tried.
- **Tracking one cell across sessions (Fig S3):** not described. The readings are the same cluster label in all sessions, or a waveform match, marked as an assumption.
- **MEC count against days (Fig S2B):** no test is reported. Readings: (a) Spearman p < 0.05, as for the parallel panels; (b) no MEC cells before 22 days.
- **"Detected from about 2 weeks":** the text does not say whether this means by recording or by histology. I read it as by recording.
- **Other:** the Hanning window length for dF/F is not given (a standard choice is allowed). Table S1's "EC" counts are taken to be the same as Figure S2B's "MEC" counts, which the paper does not state.

**Missing**
- Nothing a claim needs is missing from the paper.
- Data: the paper says it deposited only the electrophysiology on DANDI. The histology counts, starter-cell classification and imaging data are not said to be deposited anywhere. So the 18 histology and 2 imaging claims will likely not be testable on 000230; only the 7 electrophysiology claims are expected to be.
- The per-animal counts for the no-Cre controls (rabies cells and spread) are not tabulated anywhere. They appear only as points in Figures 2B and S2A.

## End of run

30 turns, 5 minutes, $1.93 at API prices, result: success.
