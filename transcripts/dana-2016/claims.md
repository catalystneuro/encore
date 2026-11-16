# dana-2016 · claims · run 42940865809

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  grep -n "^#" docs/protocol.md | head -50; ls paper/; ls claims | head; wc -c paper/*
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  sed -n 1,200p docs/protocol.md
```

```
# Protocol for an attempt

Version: `pilot-14`. Record this version in the attempt's provenance.

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
[... 179 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat claims/fouke-2025.yaml | head -150; cat paper/cai-2.data-description.txt; cat papers/datasets/dana-2016.yaml
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  sed -n 150,400p claims/fouke-2025.yaml; wc -l paper/10.7554-elife.12727.txt; head -30 paper/10.7554-elife.12727.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  grep -n "^## " paper/10.7554-elife.12727.txt
```

Result: not kept, because it reads the paper's text.

**Agent**

I'm reading the Results now; the paper text has the Methods and the two supplementary files are screening tables.

**Agent calls Read**

```json
{
 "file_path": "paper/10.7554-elife.12727.txt",
 "offset": 33,
 "limit": 80
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  python3 - <<'E'
L=open('paper/10.7554-elife.12727.txt').read().split('\n')
seen=[]
out=[]
for i,l in enumerate(L[111:330],start=112):
    s=l.strip()
    if not s or s.startswith('DOI:'): continue
    if any(s in p for p in seen): continue
    seen.append(s); out.append(f"{i}: {s}")
print('\n'.join(out))
E
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/ae78a345-9991-46db-905e-314924fcef2d/tool-results/bgcc1iohf.txt"
}
```

```
1	113: ( a ) Top, schematic of the experiment. Bottom, image of V1 L2/3 cells expressing jRGECO1a (left), and the same field of view color-coded according to the neurons’ preferred orientation (hue) and response amplitude (brightness). ( b ) Example traces from three L2/3 neurons expressing jRGECO1a (left) and jRCaMP1a (right). Single trials (gray) and averages of 5 trials (blue and black for jRGECO1a and jRCaMP1a respectively) are overlaid. Eight grating motion directions are indicated by arrows and shown above traces. The preferred stimulus is the direction evoking the largest response. jRGECO1a traces correspond to the cells indicated in panel a (see also Video 1 ). ( c ) Average response of neurons to their preferred stimulus (175 cells, R-GECO1; 310, R-CaMP2; 395, jRGECO1a; 347, jRCaMP1a; 95, jRCaMP1b. n=4 mice for jRGECO1a and jRCaMP1a, n=3 mice for all other constructs. Panels c-f are based on the same data set. ( d ) Fourier spectra normalized to the amplitude at 0 Hz for neurons driven with 1 Hz drifting gratings, transduced with RCaMP1h, R-GECO1, R-CaMP2, jRGECaMP1a, jRCaMP1b, and jRGECO1a. Inset, zoomed-in view of 1 Hz response amplitudes. ( e ) Fraction of cells detected as responding to visual stimulus (ANOVA test, p<0.01) when expressing different calcium indicators. This fraction was 8- and 6-fold higher for jRCaMP1a and jRCaMP1b compared to RCaMP1h, respectively, and 60% higher for jRGECO1a compared to R-GECO1 (Wilcoxon rank sum test; *, p<0.05; **, p<0.01; ***, p<0.001). Error bars correspond to s.e.m (26 fields-of-view, RCaMP1h; 45, jRCaMP1a; 31, jRCaMP1b; 30, R-GECO1; 40, jRGECO1a; 33, R-CaMP2; 23, GCaMP6s; 29, GCaMP6f) ( f ) Distribution of ΔF/F amplitude for the preferred stimulus. A right-shifted curve, such as jRGECO1a vs. R-GECO1 or jRCaMP1a/b vs. jRCaMP1h, indicates enhancement of response amplitude (75 percentile values of 0.36 and 0.27 vs. 0.18 for jRCaMP1a and jRCaMP1b vs. RCaMP1h, and 0.66 vs. 0.38 for jRGECO1a vs. GCaMP6f, respectively)
[... 43 more lines not kept]
```

**Agent**

Now the Methods.

**Agent calls Bash**

```bash
cd  sed -n 329,420p paper/10.7554-elife.12727.txt | grep -v '^$'
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  grep -n -o -i ".\{100\}\(github\|crcns\|code avail\|source code\|dryad\).\{100\}" paper/10.7554-elife.12727.txt | head; sed -n 487,505p paper/10.7554-elife.12727.txt; python3 -c "
import openpyxl
for f in ['paper/10.7554-elife.12727.supp-elife-12727-supp1-v2.xlsx','paper/10.7554-elife.12727.supp-elife-12727-supp2-v2.xlsx']:
  wb=openpyxl.load_workbook(f,read_only=True)
  for ws in wb.worksheets:
    print(f,ws.title,ws.max_row,ws.max_column)
    for r in list(ws.iter_rows(values_only=True))[:4]: print(r)
"
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  sed -n 1,60p tools/claims_check.py; ls schemas 2>/dev/null; grep -l "archive: crcns" claims/*.yaml | head -3
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

[... 48 more lines not kept]
```

**Agent calls Bash**

```bash
cd  head -40 claims/bruno-2017.yaml; python3 -c "
import json;s=json.load(open('schemas/claims.schema.json'));print(json.dumps(s,indent=1)[:5000])"
```

```
# Claims for Bruno, Frost & Humphries (2017), eLife 6:e27342, "A spiral attractor network drives
# rhythmic locomotion", doi:10.7554/elife.27342, on CRCNS data set apl-1 (doi:10.6080/K0SN074B).
# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"), 2026-11-08,
# protocol as stated in docs/protocol.md (Reader), version pilot-13.
#
# Text read: the version of record (PMC5546814, open access), as JATS XML flattened to text under
# paper/: main text, Materials and methods, and the legends of Figures 1 to 8 and of all twelve
# figure supplements. The paper has no other supplementary file. No PDF of the paper was supplied,
# and none was needed: no claim rests on a number shown only in a figure. The extraction garbles
# some formulas: the Gaussian width reads "σ = {median ISI in population}/12" (a square root may be
# lost) and the rotation period reads "ω = 2πbΔt"; the code settles the second (see below).
# The data set's description (paper/apl-1.data-description.txt) was read only to know what it
# holds; no claim comes from it.
#
# Code read: https://github.com/mdhumphries/AplysiaAttractorAnalysis, commit e5f28e98 (2018-07-11),
# MATLAB, linked from the paper's Data and code availability. Analysis/DataSet_Properties.m builds
# the spike-density functions and the PCA; Analysis/Classify_attractors/ holds the recurrence
# analysis (Analyse_by_Recurrence_Points.m, LocalLinearDynamics.m, recurrence_point_results_Viz.m),
# manifold comparisons (Are_sequential_attractors_the_same.m and _CommonAxes.m,
# Initial_Conditions.m), perturbations (Are_jumps_perturbations_or_transitions2.m), period change
[... 168 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python3 -c "
import json;s=json.load(open('schemas/claims.schema.json'));print(json.dumps(s,indent=1)[5000:12000])"; sed -n 40,80p claims/bruno-2017.yaml
```

```
`: the archive and the pinned identifier of the data, e.g. 'PRIDE PXD012345' or 'Zenodo doi:10.5281/zenodo.123'.",
      "type": "string",
      "minLength": 1
     },
     "datasets": {
      "description": "Only when the paper is tested on more than one dataset: the folder names of those this claim rests on.",
      "type": "array",
      "items": {
       "type": "string"
      },
      "minItems": 1
     }
    },
    "allOf": [
     {
      "not": {
       "required": [
        "quote",
        "inferred"
       ]
[... 227 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python3 - <<'E'
import zipfile,re
for f in ['paper/10.7554-elife.12727.supp-elife-12727-supp1-v2.xlsx','paper/10.7554-elife.12727.supp-elife-12727-supp2-v2.xlsx']:
    z=zipfile.ZipFile(f)
    print(f,[n for n in z.namelist() if 'sheet' in n or 'shared' in n])
    s=z.read('xl/sharedStrings.xml').decode()
    t=re.findall(r'<t[^>]*>([^<]*)</t>',s)
    print(len(t),t[:60])
E
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  python3 - <<'E'
import zipfile,re
for f in ['paper/10.7554-elife.12727.supp-elife-12727-supp1-v2.xlsx']:
    z=zipfile.ZipFile(f)
    s=z.read('xl/sharedStrings.xml').decode()
    t=re.findall(r'<t[^>]*>([^<]*)</t>',s)
    print([x for x in t if not re.match(r'^[A-Z]\d+[A-Z]',x)][:80])
    w=z.read('xl/worksheets/sheet1.xml').decode()
    rows=re.findall(r'<row[^>]*>(.*?)</row>',w)[:4]
    for r in rows: print(r[:1500]); print()
E
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  python3 - <<'E'
import zipfile,re
for f in ['paper/10.7554-elife.12727.supp-elife-12727-supp1-v2.xlsx','paper/10.7554-elife.12727.supp-elife-12727-supp2-v2.xlsx']:
    z=zipfile.ZipFile(f)
    t=re.findall(r'<si>(.*?)</si>',z.read('xl/sharedStrings.xml').decode(),re.S)
    t=[''.join(re.findall(r'<t[^>]*>([^<]*)</t>',x)) for x in t]
    w=z.read('xl/worksheets/sheet1.xml').decode()
    rows=re.findall(r'<row[^>]*>(.*?)</row>',w)
    print(f,len(rows))
    for r in rows:
        cells=re.findall(r'<c r="([A-Z]+)\d+"[^>]*?(t="s")?[^>]*>(?:<v>([^<]*)</v>)?',r)
        vals=[(t[int(v)] if ts else v) for c,ts,v in cells]
        if any(k in ' '.join(map(str,vals)) for k in ['jR','R-CaMP2','RCaMP1h"','R-GECO1"','base','Number']) or rows.index(r)<3:
            print(vals)
E
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  python3 - <<'E'
import zipfile,re
for f in ['paper/10.7554-elife.12727.supp-elife-12727-supp1-v2.xlsx','paper/10.7554-elife.12727.supp-elife-12727-supp2-v2.xlsx']:
    z=zipfile.ZipFile(f)
    t=re.findall(r'<si>(.*?)</si>',z.read('xl/sharedStrings.xml').decode(),re.S)
    t=[''.join(re.findall(r'<t[^>]*>([^<]*)</t>',x)) for x in t]
    w=z.read('xl/worksheets/sheet1.xml').decode()
    rows=re.findall(r'<row[^>]*>(.*?)</row>',w)
    out=[]
    for r in rows:
        vals=[]
        for attrs,v in re.findall(r'<c ([^>]*?)(?:/>|>(?:<v>([^<]*)</v>)?</c>)',r):
            vals.append(t[int(v)] if 't="s"' in attrs and v else v)
        out.append(vals)
    print(f,len(out))
    for i,v in enumerate(out):
        s=' '.join(map(str,v))
        if i<4 or any(k in s for k in ['jR','R-CaMP2','"RCaMP1h"','"R-GECO1"']): print(i,v)
    # count single mutation rows with 1AP>1 and p<0.01
E
```

Result: not kept, because it reads the paper's text.

**Agent calls Write**

```json
{
 "file_path": "claims/dana-2016.yaml",
 "content": "# Claims for Dana, Mohar, Sun, Narayan, Gordus, Hasseman, Tsegaye, Holt, Hu, Walpita, Patel,\n# Macklin, Bargmann, Ahrens, Schreiter, Jayaraman, Looger, Svoboda & Kim (2016), eLife 5:e12727,\n# \"Sensitive red protein calcium indicators for imaging neural activity\", doi:10.7554/elife.12727,\n# on CRCNS data set cai-2 (doi:10.6080/K0W37T87).\n# Written by an agent (model \"claude-opus-5-5\", Claude Code, runner \"GitHub Actions\"), 2026-11-11,\n# protocol as stated in docs/protocol.md (Reader), version pilot-14.\n#\n# Text read: the version of record (PMC4846379, open access), as JATS XML flattened to text under\n# paper/: main text, Materials and methods, and the legends of Figures 1 to 9, their figure\n# supplements, Videos 1 and 2 and the source-data legends. Supplementary files 1 and 2 (the\n# neuronal culture screening results for RCaMP1h and R-GECO1 variants, one row per variant: wells,\n# mutations, 1, 3, 10 and 160 AP dF/F0, 10 AP half decay time and F0 normalized to GFP, each\n# relative to the parent, with p-values) were read for their column headings and the rows of the\n# named sensors. The tables of Figure 2, source data 1 (biophysical properties of purified\n# proteins) and Figure 7, source data 1 to 3 (Drosophila NMJ summaries) are not in the text, only\n# their legends; no claim below rests on a number found only there. No PDF was supplied; no claim\n# needs a number read from a figure.\n#\n# Code: the paper links no analysis code. The data set's description (paper/cai-2.data-description.txt,\n# read only to know what the data set holds) says the data set includes the MATLAB script\n# data_analysis_for_CRCNS_jRGECO1a.m, with find_no_event.m and find_nspike_event.m, used \"to\n# analyze the jRGECO1a data files, and produce the data presented in Dana et al., 2016 (Figure 4)\".\n# Being a file of the data set, it was not read here. It is the paper's own analysis code for\n# Figure 4: where a criterion below names readings of a detail the Methods leave open, the reading\n# that script implements is the main one, and the others are variants; where the script and the\n# Methods disagree, the Methods are the main reading (protocol, Reader, step 2).\n#\n# Data the paper used. Cultured rat hippocampal neurons (96-well field-stimulation screen, 35 Hz\n# imaging); purified proteins; mouse V1 in vivo two-photon imaging of L2/3 (and L4 to L6) neurons\n# expressing red GECIs by AAV, anesthetized mice viewing drifting gratings (8 directions, 5 trials,\n# 4 s blank and 4 s grating), 16 to 180 days after injection; Drosophila larval NMJ boutons;\n# zebrafish trigeminal neurons; C. elegans ASH and AWC neurons.\n# The data set cai-2 holds, by its description, only the simultaneous imaging and loose-seal\n# cell-attached recordings of Figure 4: L2/3 V1 neurons of anesthetized mice viewing drifting\n# gratings, jRGECO1a (11 cells; imaged at 30 Hz) and jRCaMP1a (10 cells; 15 Hz), small fields of\n# view (typically 40x40 um), with per recording the raw soma (ROI) fluorescence, the neuropil\n# fluorescence, raw and high-pass filtered electrophysiology (10 kHz) and detected spikes; the\n# stimulus contrast and orientation are not included. The paper reports 6 mice for jRGECO1a and 5\n# for jRCaMP1a. So the Figure 4 claims (fig4-*) are the ones this data set can test. The other\n# claims rest on the paper's other recordings, which the paper does not deposit (data: dataset,\n# blocked as data missing), on the supplementary tables (data: elsewhere), or on Chen et al.\n# (2013b) for GCaMP6 values.\n#\n# Method of Figure 4 as the paper gives it (Methods, Simultaneous electrophysiology and functional\n# imaging in V1, paragraphs 2 and 3; Analysis of V1 functional imaging, paragraph 1; Figure 4\n# legend): ring-shaped ROIs over the cytosol, neuropil subtracted as F_cell = F_measured - r F_neuropil\n# with r = 0.7; single-AP events isolated from other APs by more than 1 s; n-AP events are n APs\n# within a time bin (jRGECO1a 100 ms for 2 APs, plus 25 ms per added AP, to 250 ms for 8;\n# jRCaMP1a 150 ms for 2 APs, plus 50 ms per added AP, to 350 ms for 6 to 8), isolated from other\n# APs by more than 1 s; noise traces from periods without APs (jRGECO1a 4 s bins, jRCaMP1a 5 s\n# bins); F0 the mean of the 10 frames before the first AP; peak dF/F0 the maximum of the dF/F0\n# trace after the first spike (for noise traces, the maximal dF/F0 value); templates are the mean\n# n-AP response traces, made unit vectors by subtracting the mean and normalizing; responses and\n# noise traces are projected on them, and d-prime and ROC curves come from these projections.\n# Half rise and decay times from 2 AP responses with no AP in the 2 s before, an exponential decay\n# fitted to each trace, only traces with small fitting error kept (16 per indicator).\n# Details the paper leaves open, named again in the claims they touch: (1) the length and start of\n# the response and noise trace segments used for projection; (2) the window in which the peak\n# dF/F0 is taken; (3) whether templates are built from the same events they score; (4) how\n# \"accuracy (5% false-positive rate)\" is computed; (5) how the half rise time is measured and which\n# fit error selects the 16 traces.\nschema_version: 2\npaper: doi:10.7554/elife.12727\nclaims:\n- id: screen-single-mutations-improved\n  statement: In the neuronal culture screen, 353 of 934 single-mutation RCaMP1h variants and 187 of\n    689 single-mutation R-GECO1 variants had a higher 1 AP dF/F0 amplitude than their parent.\n  source: Results, Protein engineering, paragraph 3; Figure 1c and 1d; Supplementary files 1 and 2\n  quote: Numerous single mutations (353/934 RCaMP1h; 187/689 R-GECO1, Supplementary files 1 – 2 )\n    improved sensitivity compared to the parent proteins (higher ΔF/F 0 amplitude in response to\n    one AP; p<0.01, Wilcoxon rank sum test)\n  data: elsewhere\n  where: eLife supplementary files 1 and 2 of the paper (doi:10.7554/eLife.12727.030 and\n    doi:10.7554/eLife.12727.031)\n  expected:\n  - quantity: improved single-mutation RCaMP1h variants\n    value: 353\n    tolerance: 35.3\n  - quantity: single-mutation RCaMP1h variants tested\n    value: 934\n    tolerance: 93.4\n  - quantity: improved single-mutation R-GECO1 variants\n    value: 187\n    tolerance: 18.7\n  - quantity: single-mutation R-GECO1 variants tested\n    value: 689\n    tolerance: 68.9\n  criterion: Counted from the supplementary tables, as the Results define it. A single-mutation\n    variant is a row whose \"Mutations added\" column holds one mutation. It counts as improved when\n    its 1 AP dF/F0 relative to the parent is above 1 and its 1 AP p-value is below 0.01 (the\n    paper's Wilcoxon rank-sum threshold, used here to count, as the paper does). Reproduced when\n    all four counts are within tolerance.\n- id: culture-jrgeco1a-sensitivity\n  statement: In cultured neurons jRGECO1a has an 8.5-fold larger 1 AP dF/F0 amplitude than R-GECO1\n    and a faster rise time, with decay time and maximal dF/F0 similar to R-GECO1.\n  source: Results, Protein engineering, paragraph 5; Figure 2\n  quote: jRGECO1a is the most sensitive indicator, with 8.5-fold larger ΔF/F 0 amplitude for 1AP\n    stimuli and faster rise time than R-GECO1 ( Figure 2 ). Decay time and maximal ΔF/F 0 amplitude\n    were similar to R-GECO1.\n  data: elsewhere\n  where: eLife supplementary file 2 of the paper (doi:10.7554/eLife.12727.031), row jRGECO1a; rise\n    time only in Figure 2f, not tabulated\n  expected:\n  - quantity: jRGECO1a 1 AP dF/F0 relative to R-GECO1\n    value: 8.5\n    tolerance: 0.85\n  criterion: From the jRGECO1a row of supplementary file 2. Reproduced when the 1 AP dF/F0 ratio is\n    within tolerance, and the 10 AP half decay time and 160 AP dF/F0 ratios are each within 0.8 to\n    1.25 of R-GECO1 or their p-values are at or above 0.01 (the paper's screen threshold; \"similar\"\n    is not defined, so either reading is accepted). The rise time is not in the table and is not\n    tested.\n- id: culture-jrcamp1-sensitivity\n  statement: jRCaMP1a and jRCaMP1b have 24-fold and 13-fold higher sensitivity than RCaMP1h for 1 AP\n    stimuli in cultured neurons; jRCaMP1a is more sensitive and decays more slowly than jRCaMP1b.\n  source: Results, Protein engineering, paragraph 6; Figure 2\n  quote: jRCaMP1a and jRCaMP1b were also much improved compared to their parent sensors (24-fold and\n    13-fold improved sensitivity for detecting 1 AP stimuli) ( Figure 2 ). jRCaMP1a has higher\n    sensitivity and slower decay kinetics than jRCaMP1b.\n  data: elsewhere\n  where: eLife supplementary file 1 of the paper (doi:10.7554/eLife.12727.030), rows jRCaMP1a and\n    jRCaMP1b\n  expected:\n  - quantity: jRCaMP1a 1 AP dF/F0 relative to RCaMP1h\n    value: 24\n    tolerance: 2.4\n  - quantity: jRCaMP1b 1 AP dF/F0 relative to RCaMP1h\n    value: 13\n    tolerance: 1.3\n  criterion: From the jRCaMP1a and jRCaMP1b rows of supplementary file 1. Reproduced when both\n    ratios are within tolerance and jRCaMP1a has the larger 1 AP ratio and the larger 10 AP half\n    decay time ratio.\n- id: culture-jrcamp1-dynamic-range\n  statement: jRCaMP1b does not saturate between 1 and 160 APs, while jRCaMP1a has a limited dynamic\n    range, 160 +/- 25% in cultured neurons and 320 +/- 10% in solution.\n  source: Results, Protein engineering, paragraph 6; Figure 2c; Figure 2, source data 1\n  quote: jRCaMP1b has a larger dynamic range, without saturation in the range of 1–160 APs ( Figure\n    2c ) ... However, jRCaMP1a has very limited dynamic range in cultured neurons and solution (160 ±\n    25% and 320 ± 10% respectively, mean ± s.d.)\n  expected:\n  - quantity: jRCaMP1a dynamic range in cultured neurons\n    value: 160\n    tolerance: 25\n    unit: '%'\n  - quantity: jRCaMP1a dynamic range in solution\n    value: 320\n    tolerance: 10\n    unit: '%'\n  criterion: Tolerances are the paper's s.d. The absence of saturation in jRCaMP1b is judged as the\n    160 AP dF/F0 exceeding the 80 AP dF/F0 in Figure 2c's data. The paper's culture and purified\n    protein data are not deposited.\n- id: culture-jrcamp1-brighter\n  statement: jRCaMP1a and jRCaMP1b are two-fold brighter than jRGECO1a in the calcium-bound state.\n  source: Results, Protein engineering, paragraph 6; Figure 2, figure supplement 2b\n  quote: jRCaMP1a and jRCaMP1b are two-fold brighter than jRGECO1a in the calcium-bound state\n  expected:\n    quantity: peak two-photon molecular brightness, jRCaMP1a or jRCaMP1b over jRGECO1a\n    value: 2\n    tolerance: 0.2\n- id: photoswitching\n  statement: Like other mApple-based indicators, jRGECO1a photoswitches under blue light, while\n    jRCaMP1a and jRCaMP1b do not, which allows photostimulation of ChR2 and imaging in the same\n    neurons.\n  source: Results, Protein engineering, paragraphs 5 and 6; Figure 2, figure supplements 3 and 4\n  quote: Similar to other mApple-based indicators, jRGECO1a exhibits photoswitching in response to\n    blue light ... Similar to RCaMP1h, jRCaMP1a and jRCaMP1b did not exhibit photoswitching ... This\n    allows independent photostimulation and imaging in neurons that co-express ChR2 and jRCaMP1a/b\n  criterion: As Figure 2, figure supplements 3 and 4 show it. Reproduced when blue pulses give a\n    transient, calcium-independent fluorescence increase in Ca-free jRGECO1a droplets but not in\n    jRCaMP1a, and when in cultured neurons the peak dF/F0 to blue light grows with light power for\n    jRGECO1a alone (without ChR2) but stays near zero for jRCaMP1a alone (5 neurons per group).\n- id: v1-half-decay\n  statement: In mouse V1, mApple-based indicators track the stimulus more faithfully than\n    mRuby-based ones because of faster kinetics; half-decay times after the stimulus end are 300\n    ms (R-GECO1), 390 ms (jRGECO1a), 330 ms (R-CaMP2), 640 ms (jRCaMP1a) and 500 ms (jRCaMP1b).\n  source: Results, Red protein calcium indicators in mouse V1, paragraph 1; Figure 3c and 3d\n  quote: mApple-based indicators tracked more faithfully than mRuby-based indicators because of their\n    faster kinetics (signal half-decay time after end of stimulus was 300 ± 22 ms for R-GECO1, 175\n    cells; 390 ± 20 ms, jRGECO1a, 395 cells; 330 ± 16 ms, R-CaMP2, 310 cells; 640 ± 30 ms, jRCaMP1a,\n    347 cells; 500 ± 45 ms, jRCaMP1b, 95 cells\n  expected:\n  - quantity: R-GECO1 half-decay time\n    value: 300\n    tolerance: 22\n    unit: ms\n  - quantity: jRGECO1a half-decay time\n    value: 390\n    tolerance: 20\n    unit: ms\n  - quantity: R-CaMP2 half-decay time\n    value: 330\n    tolerance: 16\n    unit: ms\n  - quantity: jRCaMP1a half-decay time\n    value: 640\n    tolerance: 30\n    unit: ms\n  - quantity: jRCaMP1b half-decay time\n    value: 500\n    tolerance: 45\n    unit: ms\n  criterion: Tolerances are the paper's s.e.m. Method from Methods, Analysis of V1 functional\n    imaging, paragraph 2 (five-trial mean at the preferred stimulus; cells with a peak above 4 s.d.\n    of the 1 s baseline in the last 1 s of the stimulus; time to half peak by linear\n    interpolation), on mice expressing for 16 to 64 days. The paper's V1 grating data are not in\n    cai-2.\n- id: v1-fraction-responsive-jrcamp1\n  statement: The fraction of V1 neurons detected as responsive is 8-fold higher for jRCaMP1a and\n    6-fold higher for jRCaMP1b than for RCaMP1h, and comparable to GCaMP6f.\n  source: Results, Red protein calcium indicators in mouse V1, paragraph 2; Figure 3e\n  quote: For jRCaMP1a and jRCaMP1b this fraction was 8- and 6-fold higher than for RCaMP1h (p<10 -6\n    , Wilcoxon rank-sum test), and comparable to GCaMP6f.\n  statistics:\n  - test: Wilcoxon rank-sum test\n    p: 0.000001\n    p_relation: <\n    n: 26 fields of view for RCaMP1h, 45 for jRCaMP1a, 31 for jRCaMP1b\n  expected:\n  - quantity: fraction responsive, jRCaMP1a over RCaMP1h\n    value: 8\n    tolerance: 0.8\n  - quantity: fraction responsive, jRCaMP1b over RCaMP1h\n    value: 6\n    tolerance: 0.6\n  criterion: Responsive cells as the Methods define them (dF/F0 above 0.05 in at least one stimulus\n    period and ANOVA across blank and eight directions at p < 0.01), the fraction per field of\n    view, compared by Wilcoxon rank-sum test. Reproduced when both ratios are within tolerance and\n    both tests give p < 1e-6; \"comparable to GCaMP6f\" is judged as no significant difference from\n    GCaMP6f at p < 0.05 by the same test.\n- id: v1-fraction-responsive-jrgeco1a\n  statement: For jRGECO1a the fraction of responsive V1 neurons is 60% higher than R-GECO1, 40%\n    higher than R-CaMP2, 30% higher than GCaMP6f (not significant) and 40% lower than GCaMP6s.\n  source: Results, Red protein calcium indicators in mouse V1, paragraph 2; Figure 3e\n  quote: For jRGECO1a, the fraction was 60% higher than for R-GECO1 (p=0.012), 40% higher than\n    R-CaMP2 (p=0.03), 30% higher than GCaMP6f (p=0.1), but 40% lower than GCaMP6s (p<10 -4 ).\n  statistics:\n  - about: jRGECO1a against R-GECO1\n    test: Wilcoxon rank-sum test\n    p: 0.012\n    n: 40 and 30 fields of view\n  - about: jRGECO1a against R-CaMP2\n    test: Wilcoxon rank-sum test\n    p: 0.03\n    n: 40 and 33 fields of view\n  - about: jRGECO1a against GCaMP6f\n    test: Wilcoxon rank-sum test\n    p: 0.1\n    n: 40 and 29 fields of view\n  - about: jRGECO1a against GCaMP6s\n    test: Wilcoxon rank-sum test\n    p: 0.0001\n    p_relation: <\n    n: 40 and 23 fields of view\n  expected:\n  - quantity: fraction responsive, jRGECO1a over R-GECO1\n    value: 1.6\n    tolerance: 0.06\n  - quantity: fraction responsive, jRGECO1a over R-CaMP2\n    value: 1.4\n    tolerance: 0.04\n  - quantity: fraction responsive, jRGECO1a over GCaMP6f\n    value: 1.3\n    tolerance: 0.03\n  - quantity: fraction responsive, jRGECO1a over GCaMP6s\n    value: 0.6\n    tolerance: 0.04\n  criterion: Tolerances are 10% of each reported percentage difference (60%, 40%, 30%, 40%). Method\n    as in v1-fraction-responsive-jrcamp1. Reproduced when the ratios are within tolerance and the\n    tests give the reported significance (p < 0.05 for R-GECO1 and R-CaMP2, p >= 0.05 for GCaMP6f,\n    p < 1e-4 for GCaMP6s).\n- id: v1-response-amplitude\n  statement: Preferred-stimulus dF/F0 distributions are right-shifted for jRCaMP1a and jRCaMP1b\n    against RCaMP1h (75th percentiles 0.36 and 0.27 against 0.18) and for jRGECO1a against GCaMP6f\n    (0.66 against 0.38); jRGECO1a responses are larger than other red GECIs and GCaMP6f but smaller\n    than GCaMP6s.\n  source: Figure 3f legend; Results, Red protein calcium indicators in mouse V1, paragraph 2\n  quote: 75 percentile values of 0.36 and 0.27 vs. 0.18 for jRCaMP1a and jRCaMP1b vs. RCaMP1h, and\n    0.66 vs. 0.38 for jRGECO1a vs. GCaMP6f, respectively\n  expected:\n  - quantity: 75th percentile dF/F0, jRCaMP1a\n    value: 0.36\n    tolerance: 0.036\n  - quantity: 75th percentile dF/F0, jRCaMP1b\n    value: 0.27\n    tolerance: 0.027\n  - quantity: 75th percentile dF/F0, RCaMP1h\n    value: 0.18\n    tolerance: 0.018\n  - quantity: 75th percentile dF/F0, jRGECO1a\n    value: 0.66\n    tolerance: 0.066\n  - quantity: 75th percentile dF/F0, GCaMP6f\n    value: 0.38\n    tolerance: 0.038\n  criterion: Over all cells of Figure 3f (1981 jRCaMP1a, 971 jRCaMP1b, 861 RCaMP1h, 1605 jRGECO1a,\n    907 GCaMP6f cells), the dF/F0 at the preferred stimulus. Reproduced when the five values are\n    within tolerance and the jRGECO1a 75th percentile is above every other red GECI and GCaMP6f\n    and below GCaMP6s.\n- id: v1-orientation-tuning-similar\n  statement: Orientation tuning (OSI) of responsive V1 neurons is similar for all constructs tested.\n  source: Results, Red protein calcium indicators in mouse V1, paragraph 1; Figure 3, figure\n    supplement 1\n  quote: Orientation tuning was similar for all constructs tested\n  criterion: OSI as in Methods, Analysis of V1 functional imaging, paragraph 3 (two-Gaussian fit).\n    The paper reports no test; reproduced when every construct's mean OSI lies within one s.d. of\n    every other construct's mean (Figure 3, figure supplement 1 bottom panel shows mean +/- s.d.).\n- id: v1-long-term-stable\n  statement: Red GECIs expressed for more than 130 days show no nuclear filling and stable\n    performance, with a small decrease of orientation selectivity for jRCaMP1b after 180 days.\n  source: Results, Red protein calcium indicators in mouse V1, paragraph 3; Figure 3, figure\n    supplement 2\n  quote: Unlike GCaMP indicators, nuclear filling was not observed ( Figure 3—figure supplement 2a ),\n    presumably due to the NES in the red GECI sequences. Red GECIs showed stable performance over\n    time, although a small decrease of orientation selectivity was observed for jRCaMP1b after 180\n    days of expression\n  criterion: The paper reports no test, and each time point is one mouse. Reproduced when, per\n    indicator, the proportion of responsive cells, the median peak dF/F0 and the median half decay\n    time at the longest expression time are within 25% of their values at the shortest, except the\n    jRCaMP1b fraction of orientation-tuned cells at 180 days, which is lower. The 25% bound is a\n    choice made here; the paper gives none.\n- id: lysosome-punctae\n  statement: jRGECO1a, but not jRCaMP1a/b, forms bright punctae that co-localize with the lysosome\n    marker LAMP-1, more often in V1 than in culture; in vivo, ROIs with punctae have 90% higher\n    baseline and 20% lower peak dF/F0 than the surrounding soma.\n  source: Results, Red protein calcium indicators in mouse V1, paragraph 4; Figure 4, figure\n    supplement 1\n  quote: Similar punctae were also found in cultured neurons, but were less numerous (Wilcoxon rank\n    sum test, p<0.001, Figure 4—figure supplement 1b ). When imaged in vivo, ROIs containing punctae\n    had higher baseline fluorescence by 90% but lower peak ΔF/F 0 by 20% compared to their\n    surrounding soma (10 cells and 39 punctae\n  statistics:\n  - about: fraction of somatic area covered by aggregates, V1 against culture\n    test: Wilcoxon rank sum test\n    p: 0.001\n    p_relation: <\n    n: 10 cultured cells, 14 fixed tissue cells\n  expected:\n  - quantity: baseline fluorescence of punctae ROIs over surrounding soma, increase\n    value: 90\n    tolerance: 9\n    unit: '%'\n  - quantity: peak dF/F0 of punctae ROIs over surrounding soma, decrease\n    value: 20\n    tolerance: 2\n    unit: '%'\n- id: red-gecis-900nm\n  statement: Red GECIs also emit green fluorescence under 900 nm excitation, which does not report\n    calcium; jRGECO1a L4 cells respond at 1040 nm but hardly at 900 nm (25 against 1 of 50 cells).\n  source: Results, Red protein calcium indicators in mouse V1, paragraph 5; Figure 4, figure\n    supplement 2\n  quote: Green fluorescence was visible with 900 nm excitation, but not with 1040 nm excitation,\n    suggesting that red GECIs partition into at least two species. The green fluorescence was\n    distributed unevenly across the cytoplasm and does not report calcium\n  expected:\n  - quantity: responsive cells of 50 at 1040 nm\n    value: 25\n    tolerance: 2.5\n  - quantity: responsive cells of 50 at 900 nm\n    value: 1\n    tolerance: 0.1\n- id: green-species-lower-response\n  statement: jRGECO1a neurons with larger relative fluorescence at 900 nm show lower peak dF/F0, and\n    longer expression increases that relative fluorescence.\n  source: Results, Red protein calcium indicators in mouse V1, paragraph 5; Figure 4, figure\n    supplement 3c and 3d\n  quote: Longer expression times for jRGECO1a increased relative intensity at 900 nm and similarly\n    correlated with lower peak ΔF/F 0 ( Figure 4—figure supplement 3c–d , F test, p-value<0.002)\n  statistics:\n  - about: regression of peak dF/F0 on the 900/1040 nm ratio, as in the Results\n    test: F test\n    p: 0.002\n    p_relation: <\n  - about: the same regression, as in the Figure 4, figure supplement 3c legend\n    test: linear regression model, F test\n    statistic: R2 = 0.09, slopes -9.2 and -10\n    p: 0.005\n    p_relation: <\n    n: 98 cells at 16 days, 274 cells at 132 days\n  expected:\n  - quantity: R2, both data sets\n    value: 0.09\n    tolerance: 0.009\n  - quantity: slope at 16 days\n    value: -9.2\n    tolerance: 0.92\n  - quantity: slope at 132 days\n    value: -10\n    tolerance: 1.0\n  criterion: Linear regression of peak somatic dF/F0 to drifting gratings on the ratio of 900 nm\n    somatic signal (red and green channels summed) to 1040 nm baseline, per data set. Reproduced\n    when both slopes are negative with F test p < 0.005 and the median ratio is higher at 132 than\n    at 16 days.\n- id: depth-decay\n  statement: Red GECI fluorescence of L5 apical dendrites decays more slowly with imaging depth (130\n    +/- 30 um) than GCaMP6 fluorescence (75 +/- 15 um).\n  source: Results, Red protein calcium indicators in mouse V1, paragraph 6; Figure 5b\n  quote: Red GECI fluorescence decayed much more slowly (130 ± 30 μm; median ± s.d., 19 dendrites,\n    n=3 mice infected with RCaMP1h, R-GECO1, or jRGECO1a) than GCaMP6 fluorescence (75 ± 15 μm;\n    median ± s.d., 14 dendrites, n=2 mice infected with GCaMP6s or GCaMP6f; p<0.0001, Wilcoxon rank\n    sum test)\n  statistics:\n  - test: Wilcoxon rank sum test\n    p: 0.0001\n    p_relation: <\n    n: 19 red and 14 green GECI dendrites\n  expected:\n  - quantity: median decay length, red GECIs\n    value: 130\n    tolerance: 30\n    unit: um\n  - quantity: median decay length, GCaMP6\n    value: 75\n    tolerance: 15\n    unit: um\n  criterion: Tolerances are the paper's s.d. An exponential fitted per dendrite to fluorescence\n    against depth.\n- id: l6-imaging\n  statement: jRCaMP1a in NTSR1-cre mice allows detection of orientation-tuned somatic transients in\n    L6 cells down to 900 um below the pia.\n  source: Results, Red protein calcium indicators in mouse V1, paragraph 7; Figure 5c and 5d\n  quote: Four weeks after infection we could detect orientation-tuned somatic transients in L6 cells\n    (down to 900 μm below the pia) in response to visual stimuli\n  criterion: Reproduced when L6 cells imaged at 850 um or deeper include cells that are responsive\n    and orientation-tuned by the Methods' definitions.\n- id: dual-color-imaging\n  statement: jRGECO1a in L5 apical dendrites and GCaMP6s in LM axons can be imaged together in L1\n    of V1 with one 1000 nm excitation source; red GECI bleaching is low in large compartments but\n    significant in thin axons.\n  source: Results, Red protein calcium indicators in mouse V1, paragraph 8; Figure 6\n  quote: Imaging was performed in L1 of V1, where signals from overlapping axons and dendrites could\n    be reliably detected ... We note that bleaching of the red GECI was low when imaging relatively\n    large cellular compartments, such as cell bodies or apical dendrites ( Video 1 – 2 ), but\n    significant bleaching was seen for thin axons\n  criterion: A demonstration. Reproduced when the dual-color recording shows activity transients in\n    both channels from distinct dendritic and axonal ROIs. The paper gives no measure of bleaching.\n- id: fig4-recorded-cells\n  statement: Simultaneous imaging and cell-attached recording were made from 11 jRGECO1a cells in 6\n    mice and 10 jRCaMP1a cells in 5 mice.\n  source: Results, Relationship between spikes and fluorescence dynamics, paragraph 1; Figure 4c\n    legend\n  quote: jRGECO1a fluorescence changes in response to 1 AP (top, 199 spikes from 11 cells, n=6\n    mice), and jRCaMP1a fluorescence changes in response to 2 APs (bottom, 65 spikes from 10 cells,\n    n=5 mice)\n  expected:\n  - quantity: jRGECO1a cells\n    value: 11\n    tolerance: 0\n  - quantity: jRGECO1a mice\n    value: 6\n    tolerance: 0\n  - quantity: jRCaMP1a cells\n    value: 10\n    tolerance: 0\n  - quantity: jRCaMP1a mice\n    value: 5\n    tolerance: 0\n  criterion: Counts of distinct cells and animals, so tolerance is zero. Cells are identified by the\n    cell number and date in the file names; a mouse by recording date unless the data set names\n    animals. Partially reproduced when the cell counts match but the mice cannot be identified.\n- id: fig4d-event-counts\n  statement: The Figure 4 analysis rests on 199, 70, 29, 34, 35, 22, 14 and 21 jRGECO1a events and\n    135, 65, 71, 52, 33, 20, 14 and 11 jRCaMP1a events of 1 to 8 APs in their time bins, and on 320\n    (jRGECO1a, 4 s) and 274 (jRCaMP1a, 5 s) no-AP noise events.\n  source: Figure 4d and 4e legends\n  quote: jRGECO1a, blue boxes: 199 1AP events; 2 APs: 70 events within a 100 ms time bin; 3 APs: 29,\n    125 ms; 4 APs: 34, 150 ms; 5 APs: 35, 175 ms; 6 APs: 22, 200 ms; 7 APs:14, 225 ms; 8 APs: 21,\n    250 ms. jRCaMP1a, black boxes: 135 1 AP events; 2 APs: 65, 150 ms; 3 APs: 71, 200 ms; 4 APs: 52,\n    250 ms; 5 APs: 33, 300 ms; 6 APs: 20, 350 ms; 7 APs: 14, 350 ms; 8 APs: 11, 350 ms ... jRGECO1a:\n    320 events of no AP firing within a 4 s bin, jRCaMP1a: 274 events of no AP firing within a 5 s\n    bin\n  expected:\n  - quantity: jRGECO1a 1 AP events\n    value: 199\n    tolerance: 19.9\n  - quantity: jRGECO1a 2 AP events (100 ms)\n    value: 70\n    tolerance: 7\n  - quantity: jRGECO1a 3 AP events (125 ms)\n    value: 29\n    tolerance: 2.9\n  - quantity: jRGECO1a 4 AP events (150 ms)\n    value: 34\n    tolerance: 3.4\n  - quantity: jRGECO1a 5 AP events (175 ms)\n    value: 35\n    tolerance: 3.5\n  - quantity: jRGECO1a 6 AP events (200 ms)\n    value: 22\n    tolerance: 2.2\n  - quantity: jRGECO1a 7 AP events (225 ms)\n    value: 14\n    tolerance: 1.4\n  - quantity: jRGECO1a 8 AP events (250 ms)\n    value: 21\n    tolerance: 2.1\n  - quantity: jRCaMP1a 1 AP events\n    value: 135\n    tolerance: 13.5\n  - quantity: jRCaMP1a 2 AP events (150 ms)\n    value: 65\n    tolerance: 6.5\n  - quantity: jRCaMP1a 3 AP events (200 ms)\n    value: 71\n    tolerance: 7.1\n  - quantity: jRCaMP1a 4 AP events (250 ms)\n    value: 52\n    tolerance: 5.2\n  - quantity: jRCaMP1a 5 AP events (300 ms)\n    value: 33\n    tolerance: 3.3\n  - quantity: jRCaMP1a 6 AP events (350 ms)\n    value: 20\n    tolerance: 2\n  - quantity: jRCaMP1a 7 AP events (350 ms)\n    value: 14\n    tolerance: 1.4\n  - quantity: jRCaMP1a 8 AP events (350 ms)\n    value: 11\n    tolerance: 1.1\n  - quantity: jRGECO1a noise events (4 s)\n    value: 320\n    tolerance: 32\n  - quantity: jRCaMP1a noise events (5 s)\n    value: 274\n    tolerance: 27.4\n  criterion: Spikes are the data set's detected spikes. An n-AP event is n spikes whose span from\n    first to last spike fits within the bin the legend gives (Methods, paragraph 3), with no other\n    spike within 1 s before the first or after the last (the isolation the Methods give for 1 and\n    2 APs; Figure 4f applies \"same parameters\" to all n). A 1 AP event is a spike with no other\n    spike within 1 s. Noise events are bins of 4 s (jRGECO1a) or 5 s (jRCaMP1a) without spikes.\n    Open, with readings (the data set's script, where it settles one, gives the main reading),\n    (a) isolation of more than 1 s before and after the event, or (b) before the first spike\n    only; for the noise bins, (i) non-overlapping consecutive bins, or (ii) bins also separated\n    from spikes by the 1 s isolation. Reproduced when, under one reading, at least 15 of the 18\n    counts are within tolerance; partially reproduced for 10 to 14.\n- id: fig4e-jrgeco1a-1ap-detection\n  statement: With jRGECO1a, single spikes are detected with 82% accuracy at a 5% false-positive\n    rate (11 cells, 6 mice, 199 spikes).\n  source: Results, Relationship between spikes and fluorescence dynamics, paragraph 1; Figure 4e\n    and 4f\n  quote: Single spikes were detected with 82% accuracy (5% false-positive rate, n=11 cells from 6\n    animals, 199 spikes) ( Figure 4e,f ).\n  expected:\n    quantity: jRGECO1a 1 AP detection rate at 5% false-positive rate\n    value: 82\n    tolerance: 8.2\n    unit: '%'\n  depends_on:\n  - fig4d-event-counts\n  criterion: Method from the Methods (Simultaneous electrophysiology and functional imaging in V1,\n    paragraph 2), on the events of fig4d-event-counts. dF/F0 with neuropil subtracted at r = 0.7\n    and F0 the mean of the 10 frames before the first AP; the 1 AP template is the mean of the 1 AP\n    response traces, mean-subtracted and normalized to a unit vector; 1 AP traces and noise traces\n    are projected on it; the detection rate is the fraction of 1 AP projections above the 95th\n    percentile of the noise projections (the threshold giving 5% false positives on the ROC\n    curve). Open, with readings named before the analysis: the trace segment projected is (a) the\n    frames from the first AP to the end of the noise bin length (4 s), (b) the same segment with\n    the 10 baseline frames before it, or (c) the frames from the first AP to 1 s after it (the\n    isolation interval); templates are (i) built from all events, as the Methods describe, or\n    (ii) leave-one-out. \"Accuracy\" is read as the hit rate at 5% false positives, as the\n    parenthesis states; balanced accuracy at that threshold is shown as a variant only.\n    Reproduced when the rate is within tolerance under one reading.\n- id: fig4e-jrgeco1a-2ap-detection\n  statement: With jRGECO1a, two APs within 100 ms are detected with 96% accuracy at a 5%\n    false-positive rate (70 events).\n  source: Results, Relationship between spikes and fluorescence dynamics, paragraph 1; Figure 4e\n  quote: Two APs in a time bin of 100 ms were detected with 96% accuracy (5% false-positive rate, 70\n    events).\n  expected:\n    quantity: jRGECO1a 2 AP detection rate at 5% false-positive rate\n    value: 96\n    tolerance: 4\n    unit: '%'\n  depends_on:\n  - fig4d-event-counts\n  criterion: As fig4e-jrgeco1a-1ap-detection, with the 2 AP template and the 2 AP events in 100 ms\n    bins. The tolerance is 4 points, not 9.6, because a rate cannot exceed 100%; the range is 92\n    to 100%. Reproduced when the rate is within tolerance under one reading.\n- id: fig4e-jrcamp1a-detection\n  statement: jRCaMP1a fluorescence changes are smaller, with 1 AP and 2 AP detection rates of 65% and\n    80% at a 5% false-positive rate (10 cells, 5 mice, 135 and 65 events).\n  source: Results, Relationship between spikes and fluorescence dynamics, paragraph 1; Figure 4e\n  quote: Fluorescence changes of jRCaMP1a were smaller, with a detection rate for 1AP and 2AP events\n    of 65% and 80% respectively (5% false-positive rate, n=10 cells from 5 animals, 135 and 65\n    events respectively).\n  expected:\n  - quantity: jRCaMP1a 1 AP detection rate at 5% false-positive rate\n    value: 65\n    tolerance: 6.5\n    unit: '%'\n  - quantity: jRCaMP1a 2 AP detection rate at 5% false-positive rate\n    value: 80\n    tolerance: 8\n    unit: '%'\n  depends_on:\n  - fig4d-event-counts\n  criterion: As fig4e-jrgeco1a-1ap-detection, for jRCaMP1a (15 Hz frames, 2 AP bin 150 ms, noise\n    bins 5 s; reading (a) uses 5 s segments). Reproduced when both rates are within tolerance under\n    one reading; partially reproduced when one is.\n- id: fig4df-jrgeco1a-better-than-jrcamp1a\n  statement: jRGECO1a shows higher dF/F0 amplitudes and better spike detection (d-prime) than\n    jRCaMP1a over the whole range of AP bursts from 1 to 8 APs.\n  source: Results, Relationship between spikes and fluorescence dynamics, paragraph 1; Figure 4d to\n    4f\n  quote: jRGECO1a showed higher ΔF/F 0 amplitudes and better detection than jRCaMP1a over the entire\n    range of AP bursts ( Figure 4d–f ).\n  depends_on:\n  - fig4d-event-counts\n  criterion: Per n from 1 to 8, the peak dF/F0 of each n-AP event (maximum of the dF/F0 trace after\n    the first spike; F0 the mean of the 10 frames before it) and d-prime between the projections of\n    the n-AP events and the noise traces on the unit n-AP template (difference of means over the\n    root mean of the two variances, the standard d-prime of Chen et al. 2013b, which the Methods\n    cite). Open readings: the window for the peak, (a) to 1 s after the first spike, or (b) the\n    projected segment of fig4e-jrgeco1a-1ap-detection; the segment readings of that claim for\n    d-prime. The paper reports no test. Reproduced when, under one reading, the jRGECO1a median\n    peak dF/F0 and d-prime exceed jRCaMP1a for all 8 values of n; partially reproduced for 6 or 7\n    of them.\n- id: fig4g-jrgeco1a-faster\n  statement: jRGECO1a has faster rise and decay kinetics than jRCaMP1a for 2 AP responses.\n  source: Results, Relationship between spikes and fluorescence dynamics, paragraph 1; Figure 4g\n  quote: jRGECO1a also had faster kinetics ( Figure 4g ).\n  criterion: Method from the Methods, paragraph 3. 2 AP events (bins of 100 ms for jRGECO1a and 150\n    ms for jRCaMP1a) with no spike in the 2 s before; an exponential decay fitted to each trace from\n    its peak; the 16 traces per indicator with the smallest fitting error (root mean square\n    residual) kept, which is how \"only traces with small fitting error were chosen (16 traces for\n    both indicators)\" is read here. Half decay time as (a) the fitted time constant times ln 2, or\n    (b) the time from peak to half peak on the trace. Half rise time, which the paper does not\n    define, as the time from the first spike to half of the peak dF/F0, by linear interpolation\n    (the half-time method of the V1 decay analysis). The paper's spread is s.e.m. and it reports no\n    test. Reproduced when, under one reading, the mean half rise and the mean half decay times are\n    both shorter for jRGECO1a; partially reproduced when one is.\n- id: fig4g-kinetics-like-gcamp6\n  statement: Rise and decay times of jRGECO1a and jRCaMP1a are similar to those of GCaMP6f and\n    GCaMP6s, respectively.\n  source: Results, Relationship between spikes and fluorescence dynamics, paragraph 1; Figure 4g\n  quote: Measured rise and decay time of jRGECO1a and jRCaMP1a were similar to GCaMP6f and GCaMP6s,\n    respectively ( Chen et al., 2013b ).\n  data: elsewhere\n  where: GCaMP6 values from Chen et al. (2013b), Nature 499:295, as published; the paper names no\n    archive for them\n  depends_on:\n  - fig4g-jrgeco1a-faster\n  criterion: The jRGECO1a and jRCaMP1a mean 2 AP half rise and half decay times of\n    fig4g-jrgeco1a-faster, compared with the GCaMP6f and GCaMP6s values Chen et al. (2013b) report.\n    \"Similar\" is not defined; reproduced when each time is within 25% of the matching GCaMP6 value\n    and closer to it than to the other GCaMP6 variant. The 25% bound is a choice made here.\n- id: fly-improved-over-parents\n  statement: At the Drosophila larval NMJ, jRGECO1a, jRCaMP1a and jRCaMP1b have significantly higher\n    single AP sensitivity than their parent indicators.\n  source: Results, Red protein calcium indicators in Drosophila, zebrafish, and C. elegans,\n    paragraph 1; Figure 7c; Figure 7, figure supplements 1 and 2\n  quote: we saw a significant boost of single AP sensitivity in jRGECO1a, jRCaMP1a, and jRCaMP1b\n    variants compared to their parent indicators (p<0.008 for all comparisons; Wilcoxon rank sum\n    test\n  statistics:\n  - test: Wilcoxon rank sum test\n    p: 0.008\n    p_relation: <\n    n: 10 to 13 FOVs per construct, 5 to 7 flies\n- id: fly-single-ap-amplitude\n  statement: At the NMJ, single AP dF/F0 is 11.6% for jRGECO1a and 8.6% for jRCaMP1a, against 4.5%\n    for GCaMP6s, so both outperform GCaMP6s at 1 to 5 Hz.\n  source: Results, Red protein calcium indicators in Drosophila, zebrafish, and C. elegans,\n    paragraph 1; Figure 7c; Figure 7, figure supplement 3\n  quote: Peak response amplitudes of jRGECO1a and jRCaMP1a outperform GCaMP6s in the 1–5 Hz\n    stimulation range (single AP ΔF/F 0 amplitude 11.6 ± 0.9%, 8.6 ± 0.5%, and 4.5 ± 0.3%\n    respectively, mean ± s.e.m\n  expected:\n  - quantity: jRGECO1a single AP dF/F0\n    value: 11.6\n    tolerance: 0.9\n    unit: '%'\n  - quantity: jRCaMP1a single AP dF/F0\n    value: 8.6\n    tolerance: 0.5\n    unit: '%'\n  - quantity: GCaMP6s single AP dF/F0\n    value: 4.5\n    tolerance: 0.3\n    unit: '%'\n  criterion: Tolerances are the paper's s.e.m., over FOVs (12 jRGECO1a, 11 jRCaMP1a, 12 GCaMP6s, 7\n    flies each).\n- id: fly-decay-like-gcamp6f\n  statement: At the NMJ, the half decay time of jRGECO1a at 160 Hz (0.42 s) is similar to GCaMP6f\n    (0.43 s).\n  source: Results, Red protein calcium indicators in Drosophila, zebrafish, and C. elegans,\n    paragraph 1; Figure 7d\n  quote: The decay kinetics of jRGECO1a (half decay time at 160 Hz: 0.42 ± 0.02 s, mean ± s.e.m) was\n    similar to GCaMP6f (0.43 ± 0.01 s\n  expected:\n  - quantity: jRGECO1a half decay time at 160 Hz\n    value: 0.42\n    tolerance: 0.02\n    unit: s\n  - quantity: GCaMP6f half decay time at 160 Hz\n    value: 0.43\n    tolerance: 0.01\n    unit: s\n- id: fig7b-5hz-amplitude\n  statement: To 5 Hz stimulation at the NMJ, jRGECO1a responses are 4-fold higher than GCaMP6f and\n    60% higher than GCaMP6s, and jRCaMP1a responses 3-fold higher than GCaMP6f and similar to\n    GCaMP6s.\n  source: Figure 7b legend\n  quote: Response amplitudes were 4-fold and 60% higher for jRGECO1a than GCaMP6f and GCaMP6s\n    respectively (p<10–4 and p=0.01, Wilcoxon rank sum test), jRCaMP1a response amplitude was 3-fold\n    higher than GCaMP6f (p=10–4) and similar to GCaMP6s\n  statistics:\n  - about: jRGECO1a against GCaMP6f\n    test: Wilcoxon rank sum test\n    p: 0.0001\n    p_relation: <\n    n: 12 and 12 FOVs\n  - about: jRGECO1a against GCaMP6s\n    test: Wilcoxon rank sum test\n    p: 0.01\n    n: 12 and 12 FOVs\n  - about: jRCaMP1a against GCaMP6f\n    test: Wilcoxon rank sum test\n    p: 0.0001\n    n: 11 and 12 FOVs\n  expected:\n  - quantity: 5 Hz amplitude, jRGECO1a over GCaMP6f\n    value: 4\n    tolerance: 0.4\n  - quantity: 5 Hz amplitude, jRGECO1a over GCaMP6s\n    value: 1.6\n    tolerance: 0.06\n  - quantity: 5 Hz amplitude, jRCaMP1a over GCaMP6f\n    value: 3\n    tolerance: 0.3\n  criterion: The 1.6 tolerance is 10% of the 60% difference. \"Similar to GCaMP6s\" is judged as a\n    Wilcoxon rank sum test at p >= 0.05.\n- id: fig7c-frequency-tuning\n  statement: jRGECO1a and jRCaMP1a responses are 2 to 3-fold higher than GCaMP6s and GCaMP6f at 1 Hz\n    stimulation, but lower at 20 Hz and above.\n  source: Figure 7c legend\n  quote: jRGECO1a and jRCaMP1a response amplitudes were 2–3 fold higher than GCaMP6s and GCaMP6f for\n    1 Hz stimulus (p<0.001, Wilcoxon rank sum test), but lower for stimulus frequencies of 20 Hz and\n    higher\n  statistics:\n  - test: Wilcoxon rank sum test\n    p: 0.001\n    p_relation: <\n    n: 12 jRGECO1a, 11 jRCaMP1a, 12 GCaMP6s and 12 GCaMP6f FOVs\n  expected:\n    quantity: 1 Hz amplitude, red over green GECI (four ratios)\n    value: 2.5\n    tolerance: 0.7\n  criterion: The range 2 to 3, widened by 10% of each bound, is 1.8 to 3.3 (written as 2.5 +/- 0.7,\n    slightly wider at the low end). Reproduced when all four 1 Hz ratios fall in 1.8 to 3.3 with p\n    < 0.001, and both red GECIs have lower mean peak dF/F0 than both GCaMP6 variants at 20, 40, 80\n    and 160 Hz.\n- id: zebrafish-jrgeco1a-most-sensitive\n  statement: In zebrafish trigeminal neurons jRGECO1a is the most sensitive red GECI; its response\n    to one and five pulses exceeds all other GECIs including GCaMP6f and GCaMP6s, and is partly\n    saturated for more pulses.\n  source: Results, Red protein calcium indicators in Drosophila, zebrafish, and C. elegans,\n    paragraph 2; Figure 8b and 8c\n  quote: jRGECO1a was the most sensitive red GECI tested in this assay: its response to one and five\n    pulses outperformed all other GECIs, including GCaMP6f and GCaMP6s ( Figure 8b,c ). For higher\n    numbers of stimulus pulses the jRGECO1a response was partially saturated.\n  criterion: Mean peak dF/F0 per fish (n = 5 to 7 fish per GECI). Reproduced when jRGECO1a has the\n    highest mean for 1 and 5 pulses among all eight GECIs, and its 10-pulse to 5-pulse ratio is\n    below 2 (less than proportional to the number of pulses, a reading of \"partially saturated\"\n    made here).\n- id: fig8b-zebrafish-improvement\n  statement: In zebrafish, five-pulse responses are 7- and 8-fold higher for jRCaMP1a and jRCaMP1b\n    than RCaMP1h, and 4-fold higher for jRGECO1a than R-CaMP2; jRCaMP1b has faster kinetics than\n    jRCaMP1a.\n  source: Figure 8b and 8d; Results, Red protein calcium indicators in Drosophila, zebrafish, and C.\n    elegans, paragraph 2\n  quote: Response amplitudes were 7- and 8- fold higher for jRCaMP1a and jRCaMP1b than RCaMP1h,\n    respectively, and 4-fold higher for jRGECO1a than R-CaMP2 (Wilcoxon rank-sum test, p<0.01)\n  statistics:\n  - test: Wilcoxon rank-sum test\n    p: 0.01\n    p_relation: <\n    n: 7 jRCaMP1a, 6 jRCaMP1b, 6 RCaMP1h, 7 jRGECO1a and 6 R-CaMP2 fish\n  expected:\n  - quantity: five-pulse amplitude, jRCaMP1a over RCaMP1h\n    value: 7\n    tolerance: 0.7\n  - quantity: five-pulse amplitude, jRCaMP1b over RCaMP1h\n    value: 8\n    tolerance: 0.8\n  - quantity: five-pulse amplitude, jRGECO1a over R-CaMP2\n    value: 4\n    tolerance: 0.4\n  criterion: Ratios of mean five-pulse peak dF/F0. The kinetics part is judged as a shorter mean\n    10-pulse half decay time for jRCaMP1b than jRCaMP1a (Figure 8d).\n- id: worm-ash\n  statement: In C. elegans ASH neurons, the initial response to glycerol is strongest for jRCaMP1b,\n    jRGECO1a and R-GECO1 (about 250%), and jRGECO1a and jRCaMP1b track the 1 s stimuli best.\n  source: Results, Red protein calcium indicators in Drosophila, zebrafish, and C. elegans,\n    paragraph 3; Figure 9b and 9c\n  quote: All tested GECIs exhibited an initial increase in fluorescence that was strongest for\n    jRCaMP1b, jRCEGO1a, and R-GECO1 (ΔF/F 0 amplitude ~250%, Figure 9b ) ... jRGECO1a and jRCaMP1b\n    showed the best performance in tracking the 1 s stimuli\n  expected:\n    quantity: initial dF/F0 amplitude, jRCaMP1b, jRGECO1a and R-GECO1\n    value: 250\n    tolerance: 25\n    unit: '%'\n  criterion: Signal modulation as the Figure 9c legend defines it (mean peak to trough difference\n    over all 2 s cycles, divided by the mean fluorescence over the first 10 s in buffer). Reproduced\n    when the three initial amplitudes are within tolerance and jRGECO1a and jRCaMP1b have the two\n    highest mean modulations.\n- id: worm-awc\n  statement: In AWC neurons, jRGECO1a and jRCaMP1b detect the odor-induced calcium decrease, the\n    overshoot on odor removal and the return to baseline; R-GECO1 and RCaMP1h detect the decrease\n    poorly; jRCaMP1a truncates the overshoot and has the slowest kinetics. jRCaMP1b is best for\n    graded signals and jRGECO1a for speed.\n  source: Results, Red protein calcium indicators in Drosophila, zebrafish, and C. elegans,\n    paragraph 3; Figure 9d to 9f\n  quote: jRGECO1a and jRCaMP1b robustly detected the three known components of the odor response\n    ... R-GECO1 and RCaMP1h, which have weaker affinity for calcium, did not detect the odor-induced\n    calcium decrease well, whereas jRCaMP1a truncated the overshoot after odor removal ( Figure 9d,e\n    ) and had the slowest kinetics ( Figure 9f ). In summary, jRCaMP1b performed best in detection\n    of graded calcium signals, whereas jRGECO1a had advantages in response speed.\n  criterion: By the epochs of Figure 9e (1 odor addition, 2 odor removal, 3 return to baseline).\n    Reproduced when jRGECO1a and jRCaMP1b show a median decrease in epoch 1, an increase in epoch 2\n    and values near baseline in epoch 3; R-GECO1 and RCaMP1h have smaller epoch 1 decreases than\n    jRGECO1a and jRCaMP1b; jRCaMP1a has a smaller epoch 2 increase than jRGECO1a and jRCaMP1b and\n    the slowest epoch 1 decay rate (Figure 9f).\n"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  python tools/claims_check.py claims/dana-2016.yaml paper/10.7554-elife.12727.txt
```

Result: not kept, because it reads the paper's text.

**Agent**

The YAML broke on two quotes that contain a colon. I'm putting those two in double quotes.

**Agent calls Bash**

```bash
cd  python3 - <<'E'
p='claims/dana-2016.yaml'
s=open(p).read()
old1=s[s.index('  quote: jRGECO1a, blue boxes'):s.index('  expected:\n  - quantity: jRGECO1a 1 AP events')]
body=old1[len('  quote: '):].rstrip('\n')
new1='  quote: "'+body+'"\n'
s=s.replace(old1,new1)
old2=s[s.index('  quote: jRGECO1a was the most sensitive'):s.index('  criterion: Mean peak dF/F0 per fish')]
body=old2[len('  quote: '):].rstrip('\n')
s=s.replace(old2,'  quote: "'+body+'"\n')
open(p,'w').write(s)
E
grep -n '[^"]: [^ ]*: ' claims/dana-2016.yaml | grep -v '^[0-9]*:#' | head; python tools/claims_check.py claims/dana-2016.yaml paper/10.7554-elife.12727.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  python3 - <<'E'
import re
for i,l in enumerate(open('claims/dana-2016.yaml'),1):
    if l.startswith('#'): continue
    m=re.match(r'^\s*(- )?[a-z_]+: ',l)
    rest=l[m.end():] if m else l
    if rest.startswith('"'): continue
    if ': ' in rest or ' #' in rest: print(i,l.rstrip())
E
```

```
465     125 ms; 4 APs: 34, 150 ms; 5 APs: 35, 175 ms; 6 APs: 22, 200 ms; 7 APs:14, 225 ms; 8 APs: 21,
466     250 ms. jRCaMP1a, black boxes: 135 1 AP events; 2 APs: 65, 150 ms; 3 APs: 71, 200 ms; 4 APs: 52,
467     250 ms; 5 APs: 33, 300 ms; 6 APs: 20, 350 ms; 7 APs: 14, 350 ms; 8 APs: 11, 350 ms ... jRGECO1a:
468     320 events of no AP firing within a 4 s bin, jRCaMP1a: 274 events of no AP firing within a 5 s
555     curve). Open, with readings named before the analysis: the trace segment projected is (a) the
612     cite). Open readings: the window for the peak, (a) to 1 s after the first spike, or (b) the
687   quote: The decay kinetics of jRGECO1a (half decay time at 160 Hz: 0.42 ± 0.02 s, mean ± s.e.m) was
```

**Agent calls Bash**

```bash
cd  python3 - <<'E'
p='claims/dana-2016.yaml'
s=open(p).read()
s=s.replace('Open, with readings named before the analysis: the trace segment','Open, with readings named before the analysis, the trace segment')
s=s.replace('cite). Open readings: the window for the peak,','cite). Open readings, the window for the peak')
a='  quote: The decay kinetics of jRGECO1a (half decay time at 160 Hz: 0.42 ± 0.02 s, mean ± s.e.m) was\n    similar to GCaMP6f (0.43 ± 0.01 s\n'
assert a in s
s=s.replace(a,'  quote: "The decay kinetics of jRGECO1a (half decay time at 160 Hz: 0.42 ± 0.02 s, mean ± s.e.m) was\n    similar to GCaMP6f (0.43 ± 0.01 s"\n')
open(p,'w').write(s)
E
python tools/claims_check.py claims/dana-2016.yaml paper/10.7554-elife.12727.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  grep -n -i "rather\|—" claims/dana-2016.yaml | grep -v "quote:" ; git status --short
```

```
327:    sum test, p<0.001, Figure 4—figure supplement 1b ). When imaged in vivo, ROIs containing punctae
366:    correlated with lower peak ΔF/F 0 ( Figure 4—figure supplement 3c–d , F test, p-value<0.002)
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
?? claims/dana-2016.yaml
?? scripts
```

**Agent**

I wrote `claims/dana-2016.yaml` and did not commit it. The quote checker reports 35 claims, 35 quotes, 15 statistical values and 0 problems.

**Text read:** the version of record (PMC4846379), as flattened text: main text, Materials and methods, and all figure, figure-supplement, video and source-data legends. Supplementary files 1 and 2 are the culture screening tables; I read their column headings and the rows for the named sensors. There is no PDF, and no claim needed a figure. The paper links no code. The data set's own Figure 4 script (`data_analysis_for_CRCNS_jRGECO1a.m`, named in the data description) is one of its files, so I did not read it. The criteria say that where it settles an open reading, its choice is the main one, and that the Methods win where the two disagree.

**Claims:**
- **Testable on cai-2 (8):** the Figure 4 claims. They cover the number of cells and mice, the event counts per AP bin, jRGECO1a detection of 1 AP (82%) and 2 APs (96%), jRCaMP1a detection (65% and 80%), jRGECO1a above jRCaMP1a in ΔF/F0 and d′ for 1 to 8 APs, and faster jRGECO1a kinetics.
- **One more Figure 4 claim** (kinetics similar to GCaMP6f and GCaMP6s) is `data: elsewhere`, because the GCaMP6 values come from Chen et al. 2013b.
- **Three claims** are `data: elsewhere` on the supplementary tables: the screen counts (353 of 934 and 187 of 689) and the 8.5-, 24- and 13-fold culture improvements.
- **The other 23** rest on recordings that cai-2 does not hold: culture and protein experiments, V1 grating imaging, lysosomes, 900 nm excitation, imaging depth, L6, dual colour, fly, zebrafish and worm.
- 21 claims have `statistics` (15 p-values checked), 32 have `expected` values, and 32 have a `criterion`.

**Details the paper leaves open, and the readings named:**
1. **Trace segment projected for templates and ROC:** (a) from the first AP to the noise-bin length (4 s for jRGECO1a, 5 s for jRCaMP1a); (b) the same with the 10 baseline frames added; (c) from the first AP to 1 s after it.
2. **Templates:** (i) built from all events, as described; (ii) leave-one-out.
3. **"Accuracy (5% false-positive rate)":** read as the hit rate above the 95th percentile of the noise projections. Balanced accuracy is shown only as a variant.
4. **Event isolation for n APs:** more than 1 s (a) before and after the event, or (b) before only. Noise bins are (i) consecutive, or (ii) also kept 1 s away from spikes.
5. **Window for peak ΔF/F0:** up to 1 s after the first spike, or the projected segment.
6. **Kinetics:** half decay is either the fitted time constant × ln 2 or the time from peak to half peak. Half rise is not defined; I read it as the time from the first spike to half of the peak. "Small fitting error" is read as the 16 traces with the lowest RMS residual.
7. **Thresholds I chose because the paper gives none:** a 25% bound for "stable" (long-term expression) and for "similar to GCaMP6", a 0.8 to 1.25 ratio (or screen p ≥ 0.01) for "similar" decay in culture, and a 10-pulse to 5-pulse ratio below 2 for "partially saturated" in zebrafish. Each one is labelled in its claim as a choice made here.

**Missing from the paper:** the tables of Figure 2 source data 1 (purified-protein properties) and Figure 7 source data 1 to 3 (fly NMJ summaries) are not in the text, only their legends. No claim rests on a number found only there. Figure 4g gives its rise and decay times only in the figure, so that claim is judged by direction alone (jRGECO1a faster on both).

## End of run

24 turns, 6 minutes, $2.07 at API prices, result: success.
