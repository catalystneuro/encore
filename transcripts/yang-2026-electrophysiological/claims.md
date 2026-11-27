# yang-2026-electrophysiological · claims · run 45915597306

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
grep -n "^#" docs/protocol.md | head -50; ls paper/ claims/ | head -50
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -n 1,200p docs/protocol.md; ls -la paper/
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cat paper/10.64898-2026.01.08.698522.txt | head -c 70000
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-registry-encore-registry/1063968d-a60a-49f8-923c-464a36a6e0f3/tool-results/bec7vnufg.txt"
}
```

```
1	DOI: 10.64898/2026.01.08.698522
2	Version: bioRxiv preprint, version 2 (2026-08-20)
3	Source: PDF supplied by a person
4	Stored: 2026-11-25
5	Extracted: PyMuPDF, dehyphenated, NFKC; with 1 supplement PDF(s)
6	------------------------------------------------------------------------
7	
8	=== page 1 ===
9	Title:  
10	Electrophysiological response geometries reveal shared and protocol-specific cell-type organization 
11	 
12	Author: 
13	Zihan Yang1, Yuchen Xiao2* 
14	 
15	Affiliations: 
16	1Department of Biosciences, Durham University, Durham, United Kingdom 
17	2School of Life Sciences, Westlake University, Hangzhou, China 
18	 
19	*Correspondence: [removed: an e-mail address] 
20	 
[... 841 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-registry-encore-registry/1063968d-a60a-49f8-923c-464a36a6e0f3/tool-results/bec7vnufg.txt",
 "offset": 862
}
```

```
862	interneurons that specialize in disinhibitory control. Nature 503, 521–524. 
863	https://doi.org/10.1038/nature12676. 
864	22. Lee, B.R., Dalley, R., Miller, J.A., Chartrand, T., Close, J., Mann, R., Mukora, A., Ng, L., Alfiler, 
865	L., Baker, K., et al. (2023). Signature morphoelectric properties of diverse GABAergic 
866	interneurons in the human neocortex. Science 382, eadf6484. 
867	https://doi.org/10.1126/science.adf6484. 
868	23. Fu, Y., Tucciarone, J.M., Espinosa, J.S., Sheng, N., Darcy, D.P., Nicoll, R.A., Huang, Z.J., and 
869	Stryker, M.P. (2014). A cortical circuit for gain control by behavioral state. Cell 156, 1139–1152. 
870	https://doi.org/10.1016/j.cell.2014.01.050. 
871	24. Reimer, J., Froudarakis, E., Cadwell, C.R., Yatsenko, D., Denfield, G.H., and Tolias, A.S. (2014). 
872	Pupil fluctuations track fast switching of cortical states during quiet wakefulness. Neuron 84, 
873	355–362. https://doi.org/10.1016/j.neuron.2014.09.033. 
874	25. Keller, A.J., Dipoppa, M., Roth, M.M., Caudill, M.S., Ingrosso, A., Miller, K.D., and Scanziani, 
875	M. (2020). A disinhibitory circuit for contextual modulation in primary visual cortex. Neuron 
876	108, 1181-1193.e8. https://doi.org/10.1016/j.neuron.2020.11.013. 
877	26. Schuman, B., Machold, R.P., Hashikawa, Y., Fuzik, J., Fishell, G.J., and Rudy, B. (2019). Four 
878	unique interneuron populations reside in neocortical layer 1. J. Neurosci. Off. J. Soc. Neurosci. 
879	39, 125–139. https://doi.org/10.1523/JNEUROSCI.1613-18.2018. 
880	27. Cohen-Kashi Malina, K., Tsivourakis, E., Kushinsky, D., Apelblat, D., Shtiglitz, S., Zohar, E., 
881	Sokoletsky, M., Tasaka, G.-I., Mizrahi, A., Lampl, I., et al. (2021). NDNF interneurons in layer 1 
[... 135 more lines not kept]
```

**Agent**

The text is read: a bioRxiv v2 preprint with Methods and a one-table supplement. It gives no numbers, so I'll read the figures, Table 1 and Supplementary Table 1 from the PDFs.

**Agent calls Bash**

```bash
cd $TMPDIR && which pdftoppm; python -c "import fitz; print(fitz.__doc__)"; sed -n 1,80p claims/fouke-2025.yaml
```

```
Traceback (most recent call last):
  File "<string>", line 1, in <module>
    import fitz; print(fitz.__doc__)
    ^^^^^^^^^^^
ModuleNotFoundError: No module named 'fitz'
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
[... 66 more lines not kept]
```

**Agent calls Bash**

```bash
cd  mkdir -p $TMPDIR/pg && pdftoppm -r 110 -png paper/10.64898-2026.01.08.698522.pdf $TMPDIR/pg/p && pdftoppm -r 130 -png paper/10.64898-2026.01.08.698522.supp.pdf $TMPDIR/pg/s && ls $TMPDIR/pg; cat papers/datasets/yang-2026-electrophysiological.yaml 2>/dev/null; ls claims | grep -i -E "gouwens|000020"
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
python -c "import pypdfium2" 2>&1; python -c "import pdfplumber" 2>&1; python -c "import pypdf" 2>&1; which mutool magick convert gs qpdf 2>&1 | head
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
Traceback (most recent call last):
  File "<string>", line 1, in <module>
    import pypdf
ModuleNotFoundError: No module named 'pypdf'
```

**Agent calls Read**

```json
{
 "file_path": "paper/10.64898-2026.01.08.698522.pdf",
 "pages": "3-5"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.64898-2026.01.08.698522.supp.pdf",
 "pages": "1-3"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd $TMPDIR && timeout 120 pip install --target $TMPDIR/pylib pymupdf 2>&1 | tail -2
```

```
Successfully installed flatbuffers-25.12.19 networkx-3.7 numpy-2.5.5 onnxruntime-1.32.0 packaging-26.4 protobuf-7.36.2 psutil-7.2.2 pymupdf-2.2 pymupdf-layout-2.2 pymupdf4llm-2.2 pyyaml-6.0.4 tabulate-0.10.0
Shell cwd was reset to
```

**Agent calls Bash**

```bash
mkdir -p $TMPDIR/pg; PYTHONPATH=$TMPDIR/pylib python -c "
import fitz,os
d=os.environ['TMPDIR']+'/pg/'
for f,pre,z in [('paper/10.64898-2026.01.08.698522.pdf','p',1.6),('paper/10.64898-2026.01.08.698522.supp.pdf','s',2.0)]:
    doc=fitz.open(f)
    for i,pg in enumerate(doc):
        if pre=='p' and i+1 not in (3,4,5,7,9,10): continue
        pg.get_pixmap(matrix=fitz.Matrix(z,z)).save(d+f'{pre}{i+1}.png')
print(os.listdir(d))
"
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/pg/p3.png"
}
```

Result: no output.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/pg/p4.png"
}
```

Result: no output.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/pg/p5.png"
}
```

Result: no output.

**Agent calls Bash**

```bash
PYTHONPATH=$TMPDIR/pylib python -W ignore -c "
import pymupdf as fitz,os
d=os.environ['TMPDIR']+'/pg/'
doc=fitz.open('paper/10.64898-2026.01.08.698522.pdf')
def clip(p,x0,y0,x1,y1,name,z=4):
    pg=doc[p-1]; r=pg.rect; W,H=r.width,r.height
    pg.get_pixmap(matrix=fitz.Matrix(z,z),clip=fitz.Rect(x0*W,y0*H,x1*W,y1*H)).save(d+name)
clip(3,0.12,0.31,0.35,0.73,'f1cd.png')
clip(5,0.12,0.42,0.9,0.74,'f2.png',3)
"
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/pg/f1cd.png"
}
```

Result: no output.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/pg/f2.png"
}
```

Result: no output.

**Agent calls Bash**

```bash
PYTHONPATH=$TMPDIR/pylib python -W ignore -c "
import pymupdf as fitz,os
d=os.environ['TMPDIR']+'/pg/'
doc=fitz.open('paper/10.64898-2026.01.08.698522.pdf')
for p in (7,8,9,10):
    pg=doc[p-1]
    pg.get_pixmap(matrix=fitz.Matrix(3,3),clip=fitz.Rect(0,0.08*pg.rect.height,pg.rect.width,0.8*pg.rect.height)).save(d+f'z{p}.png')
"
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/pg/z7.png"
}
```

Result: not kept, because it reads the paper's text.

Result: no output.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/pg/z9.png"
}
```

Result: no output.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/pg/z8.png"
}
```

Result: no output.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/pg/z10.png"
}
```

Result: no output.

**Agent calls Bash**

```bash
PYTHONPATH=$TMPDIR/pylib python -W ignore -c "
import pymupdf as fitz,os
d=os.environ['TMPDIR']+'/pg/'
doc=fitz.open('paper/10.64898-2026.01.08.698522.pdf')
pg=doc[7]; W,H=pg.rect.width,pg.rect.height
pg.get_pixmap(matrix=fitz.Matrix(4,4),clip=fitz.Rect(0.1*W,0.65*H,0.9*W,H)).save(d+'f4a.png')
pg=doc[8]
pg.get_pixmap(matrix=fitz.Matrix(4,4),clip=fitz.Rect(0.1*W,0.0*H,0.9*W,0.3*H)).save(d+'f4b.png')
for i,p in enumerate(doc[8:10]):
  print(i, [ (round(b[1]/H,2), b[4][:60]) for b in p.get_text('blocks')][:4])
"
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/pg/f4a.png"
}
```

Result: not kept, because it reads the paper's text.

Result: no output.

**Agent**

Figures read (Fig 4E gives n = 2154 brief cells; Fig 5A/B give Spearman 0.883 and 0.707). Now the supplementary feature table.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/pg/s1.png"
}
```

Result: no output.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/pg/s2.png"
}
```

Result: no output.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/pg/s3.png"
}
```

Result: no output.

**Agent calls Bash**

```bash
ls tools/ | grep -i -E "claim|schema"; ls docs | head -40; grep -l "read from the figure\|read off" claims/*.yaml | head -5
```

```
claims_check.py
agents
archives.md
author-responses.md
badges.md
conversion-tracker.md
design.md
encore.md
fixing-conversions.md
outside-runs.md
paper-first.md
pilot-notes
pilot-notes.md
pipeline.md
protocol.md
queue.md
replicates.md
claims/churchland-2012.yaml
claims/funamizu-2016.yaml
claims/henry-2022.yaml
[... 2 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 1,80p tools/claims_check.py; grep -n "read off\|read from the figure" claims/henry-2022.yaml | head -5; ls claims | grep -E "^(gouwens|scala|lee)"; grep -rl "000020" claims papers/datasets | head
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

[... 70 more lines not kept]
```

**Agent calls Bash**

```bash
python -c "
import json;s=json.load(open('schemas/claims.schema.json'))
print(json.dumps(s,indent=1)[:9000])"; sed -n 80,200p tools/claims_check.py
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
[... 357 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 1,40p claims/lee-2023.yaml; grep -rn "000020" papers/ docs/*.md 2>/dev/null | head
```

```
# Claims for Lee, Dalley et al. (2023), Science 382, eadf6484, on dandiset 000636.
# Written by an agent (model "claude-opus-5-5", Claude Code in GitHub Actions), 2026-10-23,
# protocol pilot-10 as stated in docs/protocol.md (Reader).
#
# Text read. The author manuscript of the version of record in PubMed Central (PMC12229143,
# NIHMS2006139), as text (paper/10.1126-science.adf6484.txt). It has the structured summary,
# the Results, the Discussion, the Materials and Methods and the legends of Figures 1 to 6. It
# does not have the supplementary materials: the legends of figs. S1 to S9 and Data S1 and S2
# are missing, and no PDF was supplied, so no figure could be read. The bioRxiv preprint
# (doi:10.1101/2022.11.08.515739, paper/10.1101-2022.11.08.515739.txt) was read as well. Its
# Results and legends of Supplementary Figures 1 to 5 (an earlier numbering) give some test
# names that the version of record moves to its supplement; where a quote or a method is taken
# from the preprint the claim says so. The preprint has no human versus mouse section. Claims
# that cite figs. S1 to S9 of the version of record rest on the main text sentence that cites
# them, and the features shown in Figure 2H and fig. S8B are not named in any text read.
#
# Code read. github.com/AllenInstitute/human_patchseq_gaba at commit 5eb357a (2023-11-28),
# linked under Data and materials availability. It holds one R notebook
# (scripts_gene_expression/acute_vs_culture_comparisons_update.Rmd; gene-expression analyses,
# the microglial ("immune") signature, the ion-channel gene test, DBC gene tests and the SST
[... 23 more lines not kept]
```

**Agent calls Write**

```json
{
 "file_path": "claims/yang-2026-electrophysiological.yaml",
 "content": "# Claims for Yang & Xiao (2026), \"Electrophysiological response geometries reveal shared and\n# protocol-specific cell-type organization\", on dandiset 000020.\n# Written by an agent (model \"claude-opus-5-5\", Claude Code, runner \"GitHub Actions\"),\n# 2026-11-27, protocol pilot-18 as stated in docs/protocol.md (Reader).\n#\n# Text read. The bioRxiv preprint, version 2 (posted 2026-08-20), as text\n# (paper/10.64898-2026.01.08.698522.txt): Abstract, Introduction, Results, Discussion, Methods\n# (sections 1 to 7), the legends of Figures 1 to 5 and the Data and Code Availability\n# statement. The supplement (one PDF, paper/10.64898-2026.01.08.698522.supp.pdf) holds only\n# Supplementary Table 1, the list of derived features per protocol; its table body is an image\n# and was read from the PDF. Table 1 (feature classes) was read from the main PDF. The text\n# reports no number: every value below (cell counts, variance explained, correlations, n) was\n# read from the figures in the PDF, and the statistics come from the text printed inside\n# Figure 5A, 5B and 4E. Values read off bars or box plots are approximate, and the claims say\n# so.\n#\n# Code read. None. The paper links no code: \"The analysis code used in this study will be made\n# publicly available upon publication\" (Data and Code Availability). No detail below is settled\n# by code.\n#\n# Data the paper used. Intracellular current-clamp recordings from genetically targeted\n# (Cre-line labelled) neurons of mouse visual cortex in the Allen Institute Patch-seq resource,\n# DANDI 000020, version 0.210913.1639 (Data and Code Availability; Methods 1). Raw NWB files were\n# converted to HDF5 holding per sweep the voltage response, the current command, the time\n# vector and cell metadata including the Cre line. Cre-line labels are the groups throughout\n# (\"driver lines\", abbreviated in the figures by marker gene). Sweeps were assigned to three\n# stimulus families from the stimulus description, the command waveform and the recording\n# mode: long pulse (sustained current steps), ramp, and brief pulse; for the brief pulse the\n# protocol X5SP_Search_DA_0 was used (Methods 1). Sweeps passed common and protocol-specific\n# quality control (Methods 2), and were aggregated to one feature vector per cell and protocol\n# (Methods 3; features in Supplementary Table 1). Cells in the PCA geometries (Figure 1C, read\n# off the bars): about 2270 long pulse, about 3220 ramp, 2154 brief pulse (the n printed in\n# Figure 4E). Driver lines: 9 in the long-pulse and ramp geometries (Sncg, Oxtr, Ndnf, Htr3a,\n# Gad2, Slc32a1, Pvalb, Sst, Vip; Figures 2 and 3) and 11 in the brief-pulse geometry (Gad2,\n# Htr3a, Ndnf, Oxtr, Pvalb, Sst, Vip, Sncg, Cck, Calb2, Crh; Figure 4). Measured variables: the\n# derived features of Supplementary Table 1 (firing rates, spike counts, response fractions,\n# first-spiking command, recruitment current, first-spike latency, peak and mean response\n# amplitudes, fast-response amplitudes, gain in mV/pA, baseline potential and noise).\n#\n# Method details the paper fixes. Features standardized and PCA run separately per protocol\n# and feature set with scikit-learn (Methods 4, 7); driver-line centroid is the mean PC score\n# vector of the line's cells; pairwise Euclidean distances between centroids; the upper\n# triangle of each distance matrix over shared driver lines correlated across geometries with\n# Pearson and Spearman (Methods 5); balanced resampling draws the same number of cells from\n# each retained line within each geometry and recomputes centroids, distances and correlations\n# from the PC scores; the null permutes driver labels within each balanced sample; empirical\n# p-values compare balanced true correlations against the shuffled-label null (Methods 6).\n# PC signs are arbitrary and interpretation is by feature composition (Methods 4).\n#\n# Method details the paper leaves open (no code to settle them). Each is named in the claims\n# that need it, with the readings the text allows:\n# - Quality-control thresholds (baseline stability and noise, trace length, ramp linearity,\n#   pulse detection); none are given (Methods 2).\n# - Spike detection (threshold or dV/dt criterion) and so every spike-based feature,\n#   recruitment current and first-spike latency.\n# - Which stimulus descriptions define long-pulse and ramp sweeps (only X5SP_Search_DA_0 is\n#   named), and the command-amplitude bins of the long-pulse command-binned features.\n# - The definitions of fast response, response windows and gain (gain is in mV/pA, Figure 4F).\n# - The missingness threshold for dropping features and the imputation statistic (mean or\n#   median).\n# - The exact membership of each feature set: the sustained-response long-pulse set, the\n#   recruitment-focused ramp set, the brief-pulse response-focused, gain-focused and base sets.\n# - How many PCs form the space where centroids and distances are computed (all PCs, the five\n#   shown in the figures, or PC1 and PC2).\n# - Minimum cells for a driver line to be included; how Cre lines sharing a marker gene are\n#   pooled; Figure 1D gives 7 lines shared by all three protocols where the figures' labels give\n#   8 (the nine long-pulse and ramp lines less Slc32a1).\n# - Balanced resampling: cells per line per draw, number of iterations, the exclusion rule for\n#   \"insufficient representation\", and how the empirical p-value is formed; the meaning of the\n#   stars in Figure 5C is not given.\nschema_version: 2\npaper: doi:10.64898/2026.01.08.698522\nclaims:\n- id: fig1c-cells-per-protocol\n  statement: About 2270 cells entered the long-pulse geometry, about 3220 the ramp geometry and\n    2154 the brief-pulse geometry.\n  source: Figure 1C; Figure 4E (n printed in the panel)\n  quote: (C) Number of cells included in PCA-based response geometry construction for each\n    stimulation protocol.\n  expected:\n  - quantity: cells in the long-pulse PCA geometry (read off the Figure 1C bar)\n    value: 2270\n    tolerance: 227\n  - quantity: cells in the ramp PCA geometry (read off the Figure 1C bar)\n    value: 3220\n    tolerance: 322\n  - quantity: cells in the brief-pulse PCA geometry (n printed in Figure 4E)\n    value: 2154\n    tolerance: 215\n  criterion: Cells are counted after the common and protocol-specific quality control of\n    Methods 2 and aggregation to one vector per cell (Methods 3), with brief-pulse sweeps from\n    X5SP_Search_DA_0 (Methods 1). The quality-control thresholds and the stimulus descriptions\n    for long-pulse and ramp sweeps are not given (open). Readings for the long-pulse sweeps, all\n    long square current steps of the dataset or only the suprathreshold step family; for the\n    ramp, the ramp stimulus family. The claim is reproduced when each count is within its\n    tolerance under a reading; tolerance is 10% of the value, and the long-pulse and ramp values\n    are read off bars to about 50 cells.\n- id: fig1d-driver-line-coverage\n  statement: The long-pulse and ramp geometries each hold 9 driver lines and the brief-pulse\n    geometry 11, with a subset of lines shared across protocols used for cross-protocol\n    validation.\n  source: Figure 1D; driver lines named in Figures 2B, 3B and 4D\n  quote: (D) Driver-line coverage across protocol-specific geometries, including the\n    driver-defined groups shared across protocols and used for balanced cross-protocol\n    validation.\n  expected:\n  - quantity: driver lines in the long-pulse geometry\n    value: 9\n    tolerance: 0\n  - quantity: driver lines in the ramp geometry (labelled \"Short pulse\" in the Figure 1D diagram;\n      Figure 3 shows the same 9 lines)\n    value: 9\n    tolerance: 0\n  - quantity: driver lines in the brief-pulse geometry\n    value: 11\n    tolerance: 0\n  - quantity: driver lines shared by all three geometries (Figure 1D)\n    value: 7\n    tolerance: 1\n  criterion: Lines are Cre-line labels abbreviated by marker gene (Methods 1; Figure 2 legend).\n    The minimum number of cells for a line to be kept and how Cre lines with the same marker\n    are pooled are not given (open). The three per-protocol counts are exact. The shared count\n    has tolerance 1 because the paper is inconsistent; Figure 1D prints 7, while the lines named\n    in Figures 2 to 4 give 8 shared (all long-pulse lines but Slc32a1). Reproduced when the\n    per-protocol lines are those named in Figures 2B, 3B and 4D and the shared count is 7 or 8.\n- id: fig2a-longpulse-low-dimensional\n  statement: A few principal components capture most of the variance of the long-pulse\n    features; PC1 explains about 39%, PC2 about 15%, and the first five about 76%.\n  source: Results, Long-pulse stimulation defines a sustained-output response geometry,\n    paragraph 2; Figure 2A\n  quote: A small number of principal components captured most of the variance in long-pulse\n    responses (Fig. 2A)\n  expected:\n  - quantity: variance explained by long-pulse PC1 (read off Figure 2A)\n    value: 39\n    tolerance: 3.9\n    unit: percent\n  - quantity: variance explained by long-pulse PC2 (read off Figure 2A)\n    value: 15\n    tolerance: 1.5\n    unit: percent\n  - quantity: cumulative variance explained by long-pulse PC1 to PC5 (read off Figure 2A)\n    value: 76\n    tolerance: 7.6\n    unit: percent\n  criterion: PCA on the standardized long-pulse sustained-response feature set (Methods 3, 4),\n    after dropping features with excessive missingness and imputing the rest. Open, and named\n    as readings. The feature set, either all long-pulse features of Supplementary Table 1 or\n    those shown in Figure 2D plus the rest of Supplementary Table 1 without the command-binned\n    features. The imputation statistic, mean or median. The missingness threshold, a standard\n    choice (features with more than 50% missing dropped), recorded as an assumption.\n    Reproduced when the three values are within tolerance under a reading.\n- id: fig2b-longpulse-continuous-biased\n  statement: In the long-pulse PC1 to PC2 embedding cells form a continuum, not discrete\n    clusters, and driver lines occupy biased regions of it.\n  source: Results, Long-pulse stimulation defines a sustained-output response geometry,\n    paragraph 2; Figure 2B\n  quote: the PC1–PC2 embedding revealed a continuous response geometry rather than discrete\n    isolated clusters (Fig. 2B). Driver-defined groups were not randomly distributed within this\n    continuum.\n  criterion: The paper reports no test for either part. Continuity is judged as the paper does,\n    by inspecting the PC1 to PC2 scatter coloured by line (Figure 2B). For the bias, the only\n    test of driver-line structure the paper uses is the driver-label shuffle (Methods 6);\n    applied here, the mean pairwise centroid distance among the 9 lines (Methods 5) is compared\n    with its distribution over label permutations of the same cells, and the bias holds when\n    fewer than 5% of permutations reach it. The number of PCs in the centroid space is open;\n    readings all PCs, the first five, and PC1 and PC2.\n  depends_on:\n  - fig2a-longpulse-low-dimensional\n- id: fig2d-longpulse-loadings\n  statement: Long-pulse PC1 is dominated by sustained firing features (firing rates, spike\n    counts, high-spiking and spiking fraction) with subthreshold fraction of opposite sign; PC2\n    has positive loadings from first-spiking current, maximum firing rate, maximum spike count,\n    subthreshold fraction and firing-rate slope, and negative ones from spiking fraction and\n    baseline variability.\n  source: Results, Long-pulse stimulation defines a sustained-output response geometry,\n    paragraph 3; Figure 2D1, 2D2\n  quote: PC1 was dominated by sustained spiking-output features, including firing-rate\n    measures, spike-count measures, high-spiking fraction, and spiking fraction, with\n    subthreshold fraction loading in the opposite direction (Fig. 2D1). ... PC2 captured a\n    complementary output-recruitment dimension, with positive loadings from first-spiking\n    current, maximum firing rate, maximum spike count, subthreshold fraction, and firing-rate\n    slope, and negative loadings from features including spiking fraction and baseline\n    variability (Fig. 2D2).\n  criterion: Loadings of the PCA of fig2a-longpulse-low-dimensional, under the same readings.\n    Signs are judged relative to each other, as PC signs are arbitrary (Methods 4). Figure 2D\n    shows the top 8 features by absolute loading of each PC. Reproduced when, for each PC, at\n    least 6 of the 8 features Figure 2D shows are among its 8 largest absolute loadings and\n    every feature the quote names has the stated sign relative to the others; partially\n    reproduced when this holds for one PC only.\n  depends_on:\n  - fig2a-longpulse-low-dimensional\n- id: fig2c-longpulse-centroid-distances\n  statement: Driver-line centroids are separated in long-pulse PC space; the Pvalb centroid is\n    farthest from Vip and Sncg.\n  source: Results, Long-pulse stimulation defines a sustained-output response geometry,\n    paragraph 4; Figure 2C\n  quote: Driver-line centroids were separated in PC space (Fig. 2C)\n  criterion: Centroids are the mean PC score vector of each line's cells and distances are\n    Euclidean (Methods 5). Which pairs are farthest is read off the Figure 2C heatmap (Pvalb to\n    Vip and Pvalb to Sncg darkest, about 3.4 and 3.2); no sentence states it. The number of PCs\n    in the space is open; readings all PCs, the first five, and PC1 and PC2. Reproduced when the\n    two largest of the 36 distances are Pvalb to Vip and Pvalb to Sncg under a reading.\n  depends_on:\n  - fig2a-longpulse-low-dimensional\n- id: fig2e-longpulse-pc2-pvalb-high-vip-low\n  statement: Along long-pulse PC2, Pvalb cells sit at the high end and Vip cells at the low end,\n    with the other lines between.\n  source: Results, Long-pulse stimulation defines a sustained-output response geometry,\n    paragraph 4; Figure 2E\n  quote: Pvalb-targeted cells were shifted toward the higher end of PC2 ... whereas Vip-targeted\n    cells occupied the lower end of the distribution. Other driverdefined groups occupied\n    intermediate positions\n  criterion: PC2 of fig2a-longpulse-low-dimensional, oriented so that first-spiking current\n    loads positively, as in Figure 2D2. The per-line summary is open; readings the median (the\n    box plots of Figure 2E) and the mean (the centroid, Figure 5A). Reproduced when Pvalb has the\n    highest and Vip the lowest value of the 9 lines under a reading.\n  depends_on:\n  - fig2d-longpulse-loadings\n- id: fig3a-ramp-variance\n  statement: The ramp feature space is low-dimensional; PC1 explains about 33%, PC2 about 21%,\n    and the first five about 87% of the variance.\n  source: Results, Ramp stimulation reveals a recruitment-threshold response geometry,\n    paragraph 2; Figure 3A\n  quote: The ramp feature space formed a structured response geometry with\n    driver-line-dependent occupancy (Fig. 3A-B).\n  expected:\n  - quantity: variance explained by ramp PC1 (read off Figure 3A)\n    value: 33\n    tolerance: 3.3\n    unit: percent\n  - quantity: variance explained by ramp PC2 (read off Figure 3A)\n    value: 21\n    tolerance: 2.1\n    unit: percent\n  - quantity: cumulative variance explained by ramp PC1 to PC5 (read off Figure 3A)\n    value: 87\n    tolerance: 8.7\n    unit: percent\n  criterion: PCA of the standardized ramp features (Methods 4). The recruitment-focused set is\n    the main ramp geometry (Methods 3, 4), but its members are not listed, and the Figure 3\n    legend says only \"ramp-response features\" (open). Readings. (a) The 8 features in Figure 3D\n    (minimum and median recruitment current, minimum and median first-spike latency, median and\n    maximum spike count, median and maximum firing rate). (b) All ramp features of\n    Supplementary Table 1. Imputation and missingness as in fig2a-longpulse-low-dimensional.\n    Reproduced when the three values are within tolerance under a reading.\n- id: fig3b-ramp-continuous-biased\n  statement: In the ramp PC1 to PC2 embedding cells form a continuum without isolated\n    driver-line clusters, and driver lines occupy biased regions of it.\n  source: Results, Ramp stimulation reveals a recruitment-threshold response geometry,\n    paragraph 2; Figure 3B\n  quote: As in the long-pulse geometry, cells did not form isolated driver-line clusters.\n    Instead, driver-defined groups occupied biased regions within a shared response continuum.\n  criterion: As in fig2b-longpulse-continuous-biased, on the ramp geometry of\n    fig3a-ramp-variance under its readings.\n  depends_on:\n  - fig3a-ramp-variance\n- id: fig3d-ramp-loadings\n  statement: Ramp PC1 is dominated by recruitment-current and first-spike-latency features\n    (minimum and median recruitment current, first-spike latency); PC2 by firing-rate and\n    spike-count output, with recruitment and latency features of opposite sign.\n  source: Results, Ramp stimulation reveals a recruitment-threshold response geometry,\n    paragraphs 3 and 4; Figure 3D1, 3D2\n  quote: PC1 was strongly defined by recruitment-current and first-spike-latency features,\n    including minimum recruitment current, median recruitment current, and latency to first\n    spike ... PC2 captured complementary outputrelated variation, with prominent contributions\n    from firing-rate and spike-count features once spiking had been recruited (Fig. 3D2).\n  criterion: Loadings of the PCA of fig3a-ramp-variance, under its readings, with signs judged\n    relative to each other (Methods 4). Reproduced when the 4 recruitment-current and latency\n    features are the 4 largest absolute loadings of PC1, and the 4 firing-rate and spike-count\n    features are the largest absolute loadings of PC2 with the recruitment and latency features\n    of opposite sign, as in Figure 3D2; partially reproduced when only one PC matches. Spike\n    detection, which defines recruitment current and latency, is not given (open); readings\n    the upward crossing of 0 mV, and a dV/dt threshold of 20 V/s.\n  depends_on:\n  - fig3a-ramp-variance\n- id: fig3e-ramp-recruitment-current-order\n  statement: Pvalb cells need the highest ramp recruitment current, Vip and Sncg cells the\n    lowest, and the other lines lie between.\n  source: Results, Ramp stimulation reveals a recruitment-threshold response geometry,\n    paragraph 4; Figure 3E\n  quote: Pvalb-targeted cells were shifted toward higher recruitment currents2,3, whereas Vip-\n    and Sncg-targeted cells occupied the lower-current end of the distribution, with other\n    driver-defined groups positioned between these extremes.\n  criterion: The per-cell value is the median recruitment current over the cell's ramp sweeps\n    (Supplementary Table 1; Figure 3E axis \"Ramp median recruitment current (pA)\"); recruitment\n    current is the command current at the first spike. Spike detection is open (readings as in\n    fig3d-ramp-loadings). The per-line summary is the median of cells, as the box plots of\n    Figure 3E show. Reproduced when Pvalb has the highest line median and Vip and Sncg the two\n    lowest of the 9 lines. For scale only, Figure 3E shows a Pvalb median near 270 pA and Vip and\n    Sncg medians below 100 pA; these are read off the plot and are not tested.\n- id: fig4a-brief-response-variance\n  statement: The brief-pulse response-focused feature space is low-dimensional; PC1 explains\n    about 47%, PC2 about 19%, and the first five about 95% of the variance.\n  source: Results, Brief-pulse stimulation reveals a transient-gain response geometry,\n    paragraphs 1 and 2; Figure 4A\n  quote: The resulting brief-pulse response space formed a structured and low-dimensional\n    geometry\n  expected:\n  - quantity: variance explained by brief response PC1 (read off Figure 4A)\n    value: 47\n    tolerance: 4.7\n    unit: percent\n  - quantity: variance explained by brief response PC2 (read off Figure 4A)\n    value: 19\n    tolerance: 1.9\n    unit: percent\n  - quantity: cumulative variance explained by brief response PC1 to PC5 (read off Figure 4A)\n    value: 95\n    tolerance: 9.5\n    unit: percent\n  criterion: PCA of the standardized response-focused brief-pulse features from\n    X5SP_Search_DA_0 sweeps (Methods 1, 3, 4). The Results name its features (peak response\n    amplitude, mean response amplitude, fast response magnitude, input-normalized gain), and\n    Figure 4C shows 10 amplitude features, but the set is not listed (open). Readings. (a) The\n    peak, mean and fast voltage-response features of Supplementary Table 1 (median and maximum\n    peak response amplitude, median mean response amplitude, median and maximum fast-response\n    peak, median fast-response mean), with or without the two gain features. (b) Those plus the\n    peak-response quantiles Figure 4C shows (lower-quartile peak response), which Supplementary\n    Table 1 does not list. The fast-response window is not given (open). Reproduced when the\n    three values are within tolerance under a reading.\n- id: fig4b-brief-continuous-biased\n  statement: In the brief-pulse response embedding cells occupy a continuous space with biased\n    driver-line occupancy, and driver-line centroids are separated.\n  source: Results, Brief-pulse stimulation reveals a transient-gain response geometry,\n    paragraphs 2 and 3; Figure 4B, 4D\n  quote: Cells occupied a continuous response space with biased driver-line occupancy,\n    indicating that transient voltage responses were not distributed randomly across\n    genetically targeted cells.\n  criterion: As in fig2b-longpulse-continuous-biased, on the geometry of\n    fig4a-brief-response-variance under its readings, with the 11 brief-pulse lines.\n  depends_on:\n  - fig4a-brief-response-variance\n- id: fig4c-brief-response-pc1-loadings\n  statement: Brief response PC1 is dominated by fast and total voltage-response amplitude\n    features (fast response mean, response mean, response peak, response quantiles, fast peak\n    response), all loading with the same sign.\n  source: Results, Brief-pulse stimulation reveals a transient-gain response geometry,\n    paragraph 2; Figure 4C\n  quote: response PC1 was dominated by fast and total voltage-response amplitude features,\n    including fast response mean, response mean, response peak, response quantiles, and fast\n    peak response measures (Fig. 4C).\n  criterion: Loadings of PC1 of fig4a-brief-response-variance, under its readings. Reproduced\n    when the largest absolute PC1 loadings are amplitude features (peak, mean or fast response)\n    and these share one sign; not reproduced when a gain, timing or baseline feature is among\n    the top three.\n  depends_on:\n  - fig4a-brief-response-variance\n- id: fig4e-brief-response-base-alignment\n  statement: Across 2154 cells, brief response PC1 scores correlate strongly with PC2 of the\n    broader brief-pulse base geometry (Pearson r = 0.875, Spearman r = 0.900).\n  source: Results, Brief-pulse stimulation reveals a transient-gain response geometry,\n    paragraph 3; Figure 4E\n  quote: response PC1 aligned strongly with the corresponding response-related axis from the\n    broader brief-pulse base geometry (Fig. 4E).\n  expected:\n  - quantity: Pearson r between response PC1 and base PC2 (printed in Figure 4E)\n    value: 0.875\n    tolerance: 0.0875\n  - quantity: Spearman r between response PC1 and base PC2 (printed in Figure 4E)\n    value: 0.9\n    tolerance: 0.09\n  - quantity: cells (printed in Figure 4E)\n    value: 2154\n    tolerance: 215\n  criterion: The base geometry is a PCA of the broader brief-pulse feature set, which the\n    Methods do not define (open); reading, all brief-pulse features of Supplementary Table 1,\n    standardized and imputed as for the response set. PC signs are arbitrary (Methods 4), so\n    the absolute value of r is compared. The base axis is the one the paper names, PC2; if the\n    response-related base axis is another PC under a reading, that is reported as a deviation\n    and the correlation with the best-matching base PC is shown. Reproduced when both |r| are\n    within tolerance (capped at 1).\n  depends_on:\n  - fig4a-brief-response-variance\n- id: fig4f-brief-gain-vip-cck-high\n  statement: On peak response gain the driver-line order differs from long-pulse and ramp; Vip\n    and Cck cells have the highest gain, and Pvalb cells are not at the upper extreme.\n  source: Results, Brief-pulse stimulation reveals a transient-gain response geometry,\n    paragraph 4; Figure 4F\n  quote: Vip- and Cck-targeted cells occupied the higher-gain end of the distribution, whereas\n    Pvalb-targeted cells no longer defined the upper extreme observed in the sustained-output\n    and ramprecruitment geometries.\n  criterion: Per cell, the median peak-response gain over X5SP_Search_DA_0 sweeps (Supplementary\n    Table 1, \"median peak-response gain\"; Figure 4F, mV/pA), gain being peak voltage response\n    divided by command amplitude. The response window and baseline are not given (open);\n    readings the peak within the pulse plus 10 ms and the peak within the pulse plus 50 ms,\n    from the pre-pulse baseline. Line summary is the median of cells (box plots of Figure 4F).\n    Reproduced when Vip and Cck have the two highest line medians of the 11 lines and Pvalb's\n    median is below the median of the 11 line medians (Figure 4F shows Pvalb near 0.045 mV/pA,\n    among the lowest, and Vip and Cck near 0.08 mV/pA).\n- id: disc-brief-gain-sncg-cck-non-pvalb\n  statement: Cck and Sncg cells also lie toward the high-gain end of the brief-pulse\n    distribution, so high transient sensitivity is spread over several non-Pvalb inhibitory\n    groups.\n  source: Discussion, paragraph 4; Figure 4F\n  quote: Cck- and Sncg-targeted cells also contributed to the higher-gain end of the brief-pulse\n    distribution, indicating that transient-response sensitivity is distributed across multiple\n    non-Pvalb inhibitory groups.\n  criterion: Gain and line medians as in fig4f-brief-gain-vip-cck-high, under its readings.\n    Reproduced when Cck and Sncg line medians both exceed Pvalb's and lie in the upper half of\n    the 11 line medians (Figure 4F shows Sncg third, near 0.06 mV/pA).\n  depends_on:\n  - fig4f-brief-gain-vip-cck-high\n- id: fig5a-longpc2-ramppc1-centroids\n  statement: Across the 9 driver lines, centroids on long-pulse PC2 and ramp recruitment PC1 are\n    closely aligned (Spearman r = 0.883, p = 0.002), with Pvalb high and Vip low on both.\n  source: Results, Protocol-specific response geometries preserve shared cell-group structure,\n    paragraph 2; Figure 5A\n  quote: Driver-line centroids along the long-pulse PC2 output-recruitment axis were closely\n    aligned with centroids along the ramp recruitment PC1 axis (Fig. 5A).\n  statistics:\n  - test: Spearman correlation (printed in Figure 5A)\n    statistic: r = 0.883\n    p: 0.002\n    n: 9 driver lines\n  expected:\n    quantity: Spearman r between long-pulse PC2 and ramp recruitment PC1 centroids\n    value: 0.883\n    tolerance: 0.088\n  criterion: Centroid on an axis is the mean PC score of the line's cells (Methods 5), on PC2\n    of fig2a-longpulse-low-dimensional and PC1 of fig3a-ramp-variance (recruitment-focused set,\n    the main ramp representation, Methods 3), each under its readings. Axes are oriented so\n    that first-spiking current loads positively on long-pulse PC2 and recruitment current on\n    ramp PC1, as Figures 2D2 and 3D1 show. Reproduced when r is within tolerance (capped at 1)\n    and p < 0.05 by the Spearman test's own p-value.\n  depends_on:\n  - fig2e-longpulse-pc2-pvalb-high-vip-low\n  - fig3d-ramp-loadings\n- id: fig5b-long-ramp-distance-alignment\n  statement: Pairwise driver-line centroid distances in the long-pulse and ramp recruitment\n    geometries are positively correlated over 36 line pairs (Spearman r = 0.707, p < 0.001).\n  source: Results, Protocol-specific response geometries preserve shared cell-group structure,\n    paragraph 3; Figure 5B\n  quote: Long-pulse and ramp recruitment geometries showed a positive distance-matrix alignment,\n    demonstrating that their relationship was not limited to a single principal component\n    comparison.\n  statistics:\n  - test: Spearman correlation (printed in Figure 5B)\n    statistic: r = 0.707\n    p: 0.001\n    p_relation: \"<\"\n    n: 36 driver-line pairs\n  expected:\n  - quantity: Spearman r between long-pulse and ramp recruitment centroid distance vectors\n    value: 0.707\n    tolerance: 0.071\n  - quantity: driver-line pairs\n    value: 36\n    tolerance: 0\n  criterion: Euclidean distances between centroids in each PC space, upper triangles over the\n    shared lines vectorized and correlated (Methods 5), on the geometries of\n    fig2a-longpulse-low-dimensional and fig3a-ramp-variance. The number of PCs in each space is\n    open; readings all PCs, the first five, and PC1 and PC2. Methods 5 also names Pearson; it is\n    shown as a variant. Reproduced when Spearman r is within tolerance and p < 0.001 under a\n    reading.\n  depends_on:\n  - fig2c-longpulse-centroid-distances\n  - fig3a-ramp-variance\n- id: fig5c-balanced-correlations-positive\n  statement: Under balanced resampling, distance-matrix correlations are positive for every\n    protocol pair, with medians near 0.79 (long pulse against ramp recruitment) and 0.6 to 0.65\n    for the pairs involving brief response or brief gain.\n  source: Results, Protocol-specific response geometries preserve shared cell-group structure,\n    paragraph 4; Figure 5C\n  quote: Across comparisons, balanced distance-matrix correlations remained consistently\n    positive, including long-pulse versus brief-response, ramp recruitment versus\n    brief-response, ramp recruitment versus brief-gain, long-pulse versus brief-gain, and\n    brief-response versus brief-gain geometries.\n  expected:\n  - quantity: median balanced Spearman r, long pulse against ramp recruitment (read off Figure\n      5C)\n    value: 0.79\n    tolerance: 0.079\n  - quantity: median balanced Spearman r, ramp recruitment against brief response (read off\n      Figure 5C)\n    value: 0.65\n    tolerance: 0.065\n  - quantity: median balanced Spearman r, ramp recruitment against brief gain (read off Figure\n      5C)\n    value: 0.65\n    tolerance: 0.065\n  - quantity: median balanced Spearman r, long pulse against brief gain (read off Figure 5C)\n    value: 0.62\n    tolerance: 0.062\n  - quantity: median balanced Spearman r, brief response against brief gain (read off Figure 5C)\n    value: 0.62\n    tolerance: 0.062\n  - quantity: median balanced Spearman r, long pulse against brief response (read off Figure 5C)\n    value: 0.61\n    tolerance: 0.061\n  criterion: For each pair of geometries, lines with insufficient representation are dropped,\n    the same number of cells is drawn from each retained line within each geometry, centroids\n    and distance matrices are recomputed from the PC scores, and the Spearman correlation of\n    the distance vectors over shared lines is taken; repeated over iterations (Methods 6). The\n    brief gain geometry is PCA of the gain-focused brief-pulse set (Methods 3, 4), whose members\n    are not listed (open; reading, the two gain features and the peak-response command slopes of\n    Supplementary Table 1). Open, named as readings. Cells per line per draw, the smallest\n    retained line's count, or a fixed 20. The exclusion rule, lines with fewer cells than\n    that number in either geometry. Iterations, 1000 (a standard choice that cannot change the\n    outcome beyond resampling noise). PCs in the space, as in fig5b-long-ramp-distance-alignment.\n    Sampling with or without replacement, without (the Methods say \"randomly sampled\"),\n    recorded as a standard choice. Reproduced when every median is positive and within\n    tolerance under a reading; partially reproduced when all are positive but some fall outside\n    tolerance.\n  depends_on:\n  - fig5b-long-ramp-distance-alignment\n  - fig4a-brief-response-variance\n- id: fig5d-f-true-above-shuffle-null\n  statement: For every protocol pair, the balanced true distance-matrix correlations lie above\n    the driver-label shuffle null distribution, which centres near zero.\n  source: Results, Protocol-specific response geometries preserve shared cell-group structure,\n    paragraph 4; Figure 5C to 5F\n  quote: In each case, the true balanced alignments were shifted above driver-label shuffle null\n    distributions, showing that the preserved geometry could not be explained by unequal\n    sampling or random driver-line assignment.\n  criterion: The null permutes driver labels within each balanced sample, keeping the PC scores\n    and sample sizes, and recomputes centroids, distances and correlations; empirical p-values\n    compare the balanced true correlations with the null (Methods 6). How the p-value is formed\n    is not given (open); readings, the fraction of null correlations at or above the median true\n    correlation, and that fraction with one added to numerator and denominator. Whether the\n    labels are shuffled in one geometry or both is open; both readings are run. Figure 5C marks\n    each pair with one or two stars without saying what they mean. Reproduced when, for all six\n    pairs, the empirical p is below 0.05 under a reading and the null median is within 0.15 of\n    zero (Figures 5D to 5F show null modes near 0).\n  depends_on:\n  - fig5c-balanced-correlations-positive\n"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
python tools/claims_check.py claims/yang-2026-electrophysiological.yaml paper/10.64898-2026.01.08.698522.txt; grep -n " — \|rather\|—" claims/yang-2026-electrophysiological.yaml
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
f=claims/yang-2026-electrophysiological.yaml; python - <<'EOF'
p='claims/yang-2026-electrophysiological.yaml'
s=open(p).read()
s=s.replace("""  quote: the PC1–PC2 embedding revealed a continuous response geometry rather than discrete
    isolated clusters (Fig. 2B). Driver-defined""","""  quote: the PC1–PC2 embedding revealed a continuous response geometry ... (Fig. 2B).
    Driver-defined""")
open(p,'w').write(s)
EOF
grep -v "^#" $f | grep -nE "^\s+(- )?[a-z_]+: .*: " ; grep -c rather $f; python tools/claims_check.py $f paper/10.64898-2026.01.08.698522.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
grep -v "^#" claims/yang-2026-electrophysiological.yaml | grep -nE "^\s{4,}[^-].*: " | grep -vE "^\S*\s+[a-z_]+: " | head
```

```
(Bash completed with no output)
```

**Agent**

I wrote `claims/yang-2026-electrophysiological.yaml` with 21 claims, and all 21 quotes match the text. The quote checker still reports one problem: p = 0.002 for Figure 5A is not in the text because it is printed only inside the figure. I confirmed it by reading the figure in the PDF.

**Text read:** the bioRxiv preprint, version 2 (2026-08-20), with Results, Methods sections 1 to 7, the legends of Figures 1 to 5 and the Data and Code Availability statement. The supplement is only Supplementary Table 1, the list of derived features for each protocol. Its body and Table 1 are images, so I read them from the PDFs.

The text gives no numbers at all. Cell counts, variance explained, correlations and n all come from the figures. Figures 4E, 5A and 5B print their statistics inside the panel; everything else was read off bars or box plots, and the claims mark those values as approximate. The paper links no code: it says the code "will be made publicly available upon publication". So none of the open details below could be settled by code.

**Claims:**
- **Quotes:** 21 of 21.
- **Statistics:** 2 claims.
  - Fig 5A: Spearman r = 0.883, p = 0.002, n = 9 driver lines.
  - Fig 5B: Spearman r = 0.707, p < 0.001, 36 driver-line pairs.
- **Expected values:** 9 claims.
- **Criteria:** all 21. All claims use the dataset itself.

**Details the paper leaves open, with the readings named:**
- **Quality control thresholds:** none are given.
- **Which stimulus descriptions count as long pulse and ramp:** only the brief-pulse protocol, X5SP_Search_DA_0, is named. Readings: all long square steps, or only the suprathreshold family.
- **Spike detection,** which sets recruitment current and latency: a 0 mV crossing, or dV/dt of 20 V/s.
- **Response window for gain:** pulse plus 10 ms, or pulse plus 50 ms.
- **Imputation and missingness:** mean or median imputation. Dropping features over 50% missing is my assumption.
- **Feature-set membership:**
  - Ramp, recruitment-focused: the 8 features shown in Fig 3D, or all ramp features.
  - Brief response: two variants of the listed amplitude features.
  - Brief base set: all brief-pulse features.
  - Brief gain set: gain plus the command-slope features.
- **How many PCs form the space for centroids and distances:** all, the first five, or PC1 and PC2.
- **Per-group summary for orderings:** median or mean.
- **Balanced resampling:** cells per line per draw (the smallest line's count, or 20). The exclusion rule follows from that number. I used 1000 iterations and sampling without replacement as standard choices.
- **Empirical p-value:** a plain fraction, or a fraction with one added to each count. The shuffle can be applied in one geometry or both.
- **Stars in Fig 5C:** their meaning is not given.
- **Shared driver lines:** the paper is inconsistent. Fig 1D prints 7 lines shared by all three protocols, but the line names in Figs 2 to 4 give 8, so the claim accepts 7 or 8. The Fig 1D diagram also labels the ramp set "Short pulse".

**Missing that a claim needed:** no exact numbers in the text, no code, and no definitions of the feature sets or resampling parameters. Nothing missing stops a claim from being written, so I did not stop the run.

## End of run

37 turns, 5 minutes, $1.81 at API prices, result: success.
