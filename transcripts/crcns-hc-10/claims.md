# crcns-hc-10 · claims · run 42155400944

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  grep -n "^#" docs/protocol.md | head -50; ls claims/001453/ claims/crcns-hc-10/ paper/ 2>&1
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  sed -n 1,185p docs/protocol.md
```

```
# Protocol for an attempt

Version: `pilot-13`. Record this version in the attempt's provenance.

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
[... 165 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat claims/001453/*.yaml
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
[... 301 more lines not kept]
```

**Agent calls Bash**

```bash
cd  wc -l paper/*.txt; head -30 paper/10.1016-j.neuron.2014.03.034.txt; cat paper/hc-10.data-description.txt | head -80
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  sed -n 80,372p paper/hc-10.data-description.txt
```

Result: not kept, because it reads the paper's text.

**Agent**

So the dataset holds current-injection sweeps of PVBCs and deep/superficial PCs. Now the paper.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1016-j.neuron.2014.03.034.txt",
 "limit": 700
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1016-j.neuron.2014.03.034.txt",
 "offset": 700,
 "limit": 700
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1016-j.neuron.2014.03.034.txt",
 "offset": 1400,
 "limit": 520
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1016-j.neuron.2014.03.034.pdf",
 "pages": "18-22"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  python -c "
import fitz,os
d=fitz.open('paper/10.1016-j.neuron.2014.03.034.pdf')
print(len(d))
for i in [17,18,19,20,21,23]:
    d[i].get_pixmap(dpi=110).save(os.environ['TMPDIR']+f'/p{i+1}.png')
"; ls $TMPDIR
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  ls; cat requirements*.txt pyproject.toml 2>/dev/null | head -30; which python; python -c "import pypdfium2" 2>&1; pip list 2>/dev/null | grep -i -E "pdf|mupdf|pillow"
```

```
LICENSE
LICENSE-data
README.md
attempts
bunfig.toml
claims
docs
encore_science
entries
node_modules
package-lock.json
package.json
paper
papers
pnpm-lock.yaml
pyproject.toml
questions
queue
schemas
scripts
[... 40 more lines not kept]
```

**Agent calls Bash**

```bash
cd  uv run --with pymupdf python -c "
import fitz,os
d=fitz.open('paper/10.1016-j.neuron.2014.03.034.pdf')
print(len(d))
for i in [17,18,19,20,21]:
    d[i].get_pixmap(dpi=120).save(os.environ['TMPDIR']+f'/p{i+1}.png')
" 2>&1 | tail -3; ls $TMPDIR
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
echo $TMPDIR
```

```
/tmp/claude-1001
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/p18.png"
}
```

Result: no output.

**Agent calls Bash**

```bash
cd  uv run --with pymupdf python -c "
import pymupdf,os
d=pymupdf.open('paper/10.1016-j.neuron.2014.03.034.pdf')
p=d[17]; r=p.rect
clip=pymupdf.Rect(r.x0+r.width*0.12,r.y0+r.height*0.28,r.x0+r.width*0.68,r.y0+r.height*0.47)
p.get_pixmap(dpi=300,clip=clip).save(os.environ['TMPDIR']+'/s1eh.png')
p=d[21]
p.get_pixmap(dpi=110).save(os.environ['TMPDIR']+'/p22b.png')
" 2>&1 | grep -v Warn
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/s1eh.png"
}
```

Result: no output.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/p20.png"
}
```

Result: no output.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/p22b.png"
}
```

Result: no output.

**Agent calls Bash**

```bash
cd  uv run --with pymupdf python -c "
import pymupdf,os
d=pymupdf.open('paper/10.1016-j.neuron.2014.03.034.pdf')
p=d[19]; r=p.rect
clip=pymupdf.Rect(r.x0+r.width*0.38,r.y0+r.height*0.33,r.x0+r.width*0.53,r.y0+r.height*0.52)
p.get_pixmap(dpi=400,clip=clip).save(os.environ['TMPDIR']+'/s3f.png')
" 2>&1 | grep -v Warn
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/s3f.png"
}
```

Result: no output.

**Agent calls Bash**

```bash
cd $TMPDIR; curl -sL -m 30 -o mdb.html -w "%{http_code}\n" "https://modeldb.science/153280"; curl -sL -m 30 -o mdbzip.zip -w "%{http_code}\n" "https://modeldb.science/download/153280"; ls -la mdb*; file mdbzip.zip
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR && mkdir -p mdb && cd mdb && unzip -oq ../mdbzip.zip && find . -type f | head -100; find . -type f | wc -l; grep -o 'Model Information.\{0,300\}' ../mdb.html | head -2
```

```
./__MACOSX/superdeep/._ch_KCaS.mod
./__MACOSX/superdeep/._ch_CavL.mod
./__MACOSX/superdeep/._MyExp2Sidnw.mod
./__MACOSX/superdeep/._ModelDB Quick Start Guide.pdf
./__MACOSX/superdeep/._modelview.hoc
./__MACOSX/superdeep/._stimulation
./__MACOSX/superdeep/._README.txt
./__MACOSX/superdeep/._connectivity
./__MACOSX/superdeep/._mynetstim.mod
./__MACOSX/superdeep/._iconc_Ca.mod
./__MACOSX/superdeep/._setupfiles
./__MACOSX/superdeep/._ch_CavLZ.mod
./__MACOSX/superdeep/._ch_Kdrslow.mod
./__MACOSX/superdeep/setupfiles/._custom_init.hoc
./__MACOSX/superdeep/setupfiles/._save_run_info.hoc
./__MACOSX/superdeep/setupfiles/._write_results_functions.hoc
./__MACOSX/superdeep/setupfiles/._sim_execution_functions.hoc
./__MACOSX/superdeep/setupfiles/._nc_append_functions.hoc
./__MACOSX/superdeep/setupfiles/._set_other_parameters.hoc
./__MACOSX/superdeep/setupfiles/._CellCategoryInfo.hoc
[... 82 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/mdb/superdeep && ls; cat README.txt | head -60; cat version.txt hg_status.out 2>/dev/null | head; grep -rli "sag\|rheobase\|input resist" --include=*.hoc --include=*.m --include=*.txt . | head
```

```
ModelDB Quick Start Guide.pdf
MyExp2Sid.mod
MyExp2Sidnw.mod
README.txt
cells
ch_CavL.mod
ch_CavLZ.mod
ch_CavN.mod
ch_CavT.mod
ch_HCNp.mod
ch_KCaS.mod
ch_Kdrfast.mod
ch_Kdrp.mod
ch_Kdrslow.mod
ch_KvA.mod
ch_KvAdistp.mod
ch_KvAproxp.mod
ch_KvCaB.mod
ch_NavPVBC.mod
ch_Navp.mod
[... 83 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/mdb/superdeep && grep -n -i "sag\|rheobase\|input resist\|rinput" superdeep.hoc setupfiles/sim_execution_functions.hoc cells/class_pyramidaldeepcell.hoc cells/class_pyramidalsupercell.hoc | head -20; cat version.txt vercomment.txt | head
```

```
superdeep.hoc:134:III.SET UP PARALLEL CAPABILITY AND MEMORY USAGE RECORDER, AND WRITE OUT RUN RECEIPT
superdeep.hoc:156:												//  usage:
superdeep.hoc:244:{zzz=0} // zzz contains the last memory usage from the previous call to mallinfo
superdeep.hoc:259:									//  $1 is the previous memory usage (from previous call to mallinfo)
superdeep.hoc:266:																						//  current memory usage,
superdeep.hoc:268:																						//  memory usage since 
superdeep.hoc:284:        return m // Return the current memory usage (to be passed into this function at the next call)
superdeep.hoc:287:{zzz = mallinfo(zzz, "Prior to creating cells")}	// Memory usage prior to creating the cells
superdeep.hoc:328:zzz = mallinfo(zzz, "After creating cells") // Record the memory usage after cells are created
superdeep.hoc:358:zzz = mallinfo(zzz, "After connecting cells")	// Record the memory usage after creating the connections
superdeep.hoc:367:zzz = mallinfo(zzz, "After defining stimulation")	// Record the memory usage after defining stimulation
superdeep.hoc:453:zzz = mallinfo(zzz, "Before running simulation")	// Get memory usage before running simulation
superdeep.hoc:457:zzz = mallinfo(zzz, "After running simulation")		// Get memory usage after running simulation
superdeep.hoc:459:if (pc.id==0) {			// Close the files used to record the memory usage as no more data points will be written
superdeep.hoc:481:{pc.done()}			// Sends the quit message to the worker processors, which then quit NEURON
superdeep.hoc:483:quit()	// Sends the quit message to the host processor, which then quits NEURON
setupfiles/sim_execution_functions.hoc:27:	if (maxcomp>0) {							// Print a summary message to screen
setupfiles/sim_execution_functions.hoc:50:	// Print a summary message of the time taken for each part of the code, as well as the name of the run
cells/class_pyramidaldeepcell.hoc:3332:	distance() // calculates the distance between location 0 of the currently accessed section (as the
[... 4 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR; curl -sL -m 30 -o sd.html -w "%{http_code}\n" "http://www.ivansolteszlab.org/models/superdeep.html"; wc -c sd.html; sed 's/<[^>]*>/ /g' sd.html | tr -s ' \n' | head -c 3000; curl -sL -m 30 -o osb.html -w "%{http_code}\n" "http://www.opensourcebrain.org/projects/nc_superdeep"; wc -c osb.html
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd  ls schemas; python -c "
import json;s=json.load(open('schemas/claims.schema.json'));print(json.dumps(s,indent=1)[:6000])" 2>/dev/null || ls schemas
```

```
attempt.schema.json
claims.schema.json
entry.schema.json
paper-match.schema.json
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
[... 189 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python -c "
import json;s=json.load(open('schemas/claims.schema.json'));print(json.dumps(s['\$defs'],indent=1))"; grep -n "crcns\|CRCNS" docs/archives.md | head -20; ls claims | grep -i crcns | head
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
[... 98 more lines not kept]
```

**Agent calls Bash**

```bash
cd  ls claims/crcns-hc-9; head -40 claims/crcns-hc-9/*.yaml
```

```
10.1523-jneurosci.5680-12.2013.yaml
# Claims for Quattrocolo & Maccaferri (2013), J Neurosci 33:5486-5498, on CRCNS data set hc-9
# (doi:10.6080/K0HQ3WTH).
# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"), 2026-11-04,
# protocol as stated in docs/protocol.md (Reader).
#
# Text read: the version of record, as supplied under paper/ (PyMuPDF text of the journal PDF),
# with its Materials and Methods, Results, Discussion and the legends of Figures 1 to 13. The
# paper has no supplement. It links no analysis code, so none was read. The PDF could not be
# rendered here, and the extracted text prints the signs =, < and > (and minus, plus/minus,
# mu, Omega) as a replacement character. Each p_relation below is read from the sentence it
# sits in: a difference the text calls significant, or a change it reports, is p < 0.05; one
# it calls absent ("did not change significantly", "similar", "ineffective", "returned to
# baseline") is p > 0.05. Values printed with that character between them are read as mean
# plus/minus SE, as the Methods state ("Data are presented as mean ±SE").
#
# Data the paper used. Acute hippocampal slices (350 um) from mice of either sex, P10 to P19:
# CXCR4-EGFP mice (Cajal-Retzius cells labelled by EGFP; 56 animals) and Sst-IRES-Cre;
# ChR2(H134R)-EYFP mice (8 animals) for the optogenetic experiments. Recordings at 30-32 C,
# filtered at 3 kHz and digitized at 10-20 kHz (Multiclamp 700, Clampex 9). Experiments:
[... 21 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 1,60p tools/claims_check.py
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

[... 41 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 40,80p claims/crcns-hc-9/*.yaml; grep -n -A12 "fig7a-olm-sag" claims/crcns-hc-9/*.yaml | head -60
```

```
# biexponential fit, or the time to 63% decay when neither fits; stratum oriens-evoked PSCs
# averaged first, then analyzed alike. Figure 10 windows 0-5 min (control) and 7-12 min
# (drug). Figure 11 firing rates per Abeles (1982), prestimulus 40-60 ms, early 90-110 ms,
# late 400-420 ms; Figure 11D baseline over 0-60 ms, and the effect as the peak of a 5 ms
# binned time course divided by baseline. Figure 12 slow conductance windows 40-60 ms against
# 60-80 and 100-120 ms; fast conductance 50-60 ms against 60-70 and 100-110 ms. Significance
# level 0.05; tests named in the text.
schema_version: 2
dataset:
  archive: crcns
  id: hc-9
  doi: 10.6080/K0HQ3WTH
paper: doi:10.1523/jneurosci.5680-12.2013
claims:
- id: fig7a-olm-sag
  statement: O-LM interneurons recorded in CXCR4-EGFP slices show a sag in their voltage
    response to hyperpolarizing current pulses (pulses of -100 and +50 pA in Figure 7A), and the
    ChR2-expressing O-LM cell of Figure 7D has a similar firing pattern.
  source: Figure 7A and 7D legends
  quote: Firingpatternsoftheaboveshowncells.Noticethepresenceofasaginthehyperpolarizingresponse.
[... 62 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/mdb/superdeep && head -5 hg_status.out hg_diff.out vercomment.txt 2>/dev/null; unzip -l ../../mdbzip.zip | head -5; sha256sum ../../mdbzip.zip
```

```
==> hg_status.out <==
ModelDB

==> hg_diff.out <==
ModelDB

==> vercomment.txt <==
ModelDB
Archive:  ../../mdbzip.zip
  Length      Date    Time    Name
---------  ---------- -----   ----
        0  2022-05-27 15:11   superdeep/
      212  2022-05-27 15:11   __MACOSX/._superdeep
333fd2210822a122e0cf57a3d16d6a8159f6765064de39b0051d03e1600fe405  ../../mdbzip.zip
Shell cwd was reset to
```

**Agent calls Write**

```json
{
 "file_path": "claims/crcns-hc-10/10.1016-j.neuron.2014.03.034.yaml",
 "content": "# Claims for Lee, Marchionni, Bezaire, Varga, Danielson, Lovett-Barron, Losonczy & Soltesz (2014),\n# Neuron 82:1129-1144, on CRCNS data set hc-10 (doi:10.6080/K00P0WXQ).\n# Written by an agent (model \"claude-opus-5-5\", Claude Code, runner \"GitHub Actions\"), 2026-11-06,\n# protocol as stated in docs/protocol.md (Reader).\n#\n# Text read: the version of record with its Supplemental Information, as supplied under paper/\n# (PyMuPDF text of the journal PDF): Results, Discussion, Experimental Procedures, the legends\n# of Figures 1 to 6 and S1 to S5, Table S1 and the Supplemental Experimental Procedures. The\n# extracted text prints micrometres as \"mm\" and some minus signs as a replacement character.\n# Values shown only in Figures S1E to S1H and S3F were read from the PDF pages (rendered here)\n# and are marked as read from a figure.\n#\n# Code read: the model code the paper links, ModelDB accession 153280 (\"superdeep\", NEURON),\n# downloaded from modeldb.science/download/153280 on 2026-11-06 (zip sha256 333fd221...fe405,\n# README \"Last updated on May 15, 2014\"). It holds the cell templates, connectivity, stimulation\n# and job scripts of the network model of Figures 4C to 4F and S3. It holds no analysis of the\n# experimental recordings, so it fixes none of the criteria for the intrinsic properties. The\n# lab page the paper also links (ivansolteszlab.org/models/superdeep.html, said to hold the\n# simulation results and analysis procedures) is now a parked domain, and the Open Source\n# Brain project page returns 404; neither was read.\n#\n# Data the paper used. Coronal hippocampal slices (300 um) from 2- to 3-month-old PV-TOM,\n# PV-ChR2 and C57BL/6J mice of either sex, septal (AP -1.9 to -2.5 mm) and temporal (AP -3.1\n# to -3.7 mm) CA1; recordings at 33 C, filtered at 3 kHz, digitized at 10 kHz (MultiClamp\n# 700B, Digidata 1440A). PCs are superficial (sPC) or deep (dPC) by soma distance from the\n# Pyr/Rad border (septal 0-20 and 20-40 um; temporal 0-50 and 50-200 um). Experiments: paired\n# recordings PVBC to PC (euIPSC, uIPSC, CV, release probability, paired-pulse ratio, connection\n# probability; Figure 1), PC to PVBC (euEPSC, connection probability; Figure 3), PVBC trains\n# against PC firing in current clamp (Figure 4A, 4B), CCKBC to PC (Figure 5), PVBC to\n# retrogradely labelled mPFC-, AMG- and MEC-projecting dPCs (Figure 6); bouton counts and\n# morphology (Figures 1J to 1L, 2G to 2I, 5G, S1, S4, S5); optogenetic IPSCs (Figure 1N); in\n# vivo two-photon GCaMP5 imaging of PV+ axons in 5 head-fixed running mice (Figure 2B to 2F);\n# a NEURON network model of 1,000 sPCs, 1,000 dPCs and 36 PVBCs (Figure 4C to 4F, S3).\n# Intrinsic properties (Figure S1E to S1H): sPC n = 8, dPC n = 9, held at -70 mV, 1 s steps\n# (0 to +550 pA in 50 pA steps for firing; -100 to +100 pA for input resistance, steady state\n# 0.8 to 1.0 s after step onset); voltages uncorrected for the +14.6 mV junction potential,\n# which Table S1 subtracts.\n#\n# The CRCNS data set, by its description, holds ATF files of current-injection sweeps: for\n# this paper 8 superficial and 9 deep PCs (steps -400 to +550 pA in 50 pA increments, the\n# protocol of Supplemental Experimental Procedures 8A) and 6 PV+ basket cells; its other cells\n# belong to other papers. Only the claims figs1e-if-curves, figs1f-input-resistance,\n# figs1g-resting-potential, figs1h-sag, tables1-rheobase and figs3f-pvbc-firing concern those\n# recordings. The other claims cover the paper's main findings, whose data the data set does\n# not hold. The model claims need simulations of the ModelDB code (data with_inputs).\n#\n# Statistics, from Experimental Procedures, Statistical Analysis: two-tailed Student's t tests,\n# paired or unpaired as appropriate, replaced by Wilcoxon signed-rank (paired) or Mann-Whitney\n# (unpaired) when a group fails the Shapiro-Wilk test; Pearson's chi-square for connection\n# probabilities, with Bonferroni-Holm correction for three groups (Figure 6G); ANOVA with\n# Tukey-Kramer for Figures 6E, S5D and 4D to 4F; mean and SEM; significance at p < 0.05. The\n# text does not say which test each comparison used, so `test` below names the rule. Where a\n# mean is given with its SEM, the SEM is the tolerance.\nschema_version: 2\ndataset:\n  archive: crcns\n  id: hc-10\n  doi: 10.6080/K00P0WXQ\npaper: doi:10.1016/j.neuron.2014.03.034\nclaims:\n- id: figs1e-if-curves\n  statement: Superficial and deep CA1 PCs do not differ in firing frequency as a function of\n    injected current (two-way ANOVA, p > 0.4; 8 sPCs, 9 dPCs).\n  source: Results, PVBCs Preferentially Innervate Subpopulations of CA1 PCs, paragraph 2;\n    Figure S1E and legend\n  quote: There were no differences between dPCs and sPCs in terms of their firing frequency as a\n    function of intracellularly injected current (Figure S1E)\n  statistics:\n  - test: two-way ANOVA\n    p: 0.4\n    p_relation: \">\"\n    n: 8 sPCs and 9 dPCs\n  expected:\n  - quantity: sPC firing frequency at +550 pA (read from Figure S1E)\n    value: 31.5\n    tolerance: 3.15\n    unit: Hz\n  - quantity: dPC firing frequency at +550 pA (read from Figure S1E)\n    value: 30.5\n    tolerance: 3.05\n    unit: Hz\n  criterion: 'From the Supplemental Experimental Procedures 2B, steps of 1 s from 0 to +550 pA\n    in 50 pA increments, cells held at -70 mV; the data set''s steps from 0 to +550 pA are used.\n    How firing frequency is computed is not stated. Readings: (a) spikes during the 1 s step\n    divided by 1 s; (b) (spikes - 1) over the time from first to last spike, the form the\n    Figure S3E legend implies for the model (31.06 Hz for 30 spikes). Spike detection is a\n    standard choice (upward crossing of 0 mV) that cannot change the outcome. A claim of\n    absence, judged on the paper''s test as written, a two-way ANOVA of firing frequency on\n    group (sPC, dPC) and current step: reproduced when the group effect is not significant\n    (p >= 0.05), not reproduced when it is; the effect size is reported either way, and a\n    repeated-measures ANOVA is shown as a variant. The expected values, read from the figure,\n    are checked as well under either reading.'\n- id: figs1f-input-resistance\n  statement: Superficial and deep PCs do not differ in input resistance (117 against 124 MOhm).\n  source: Results, PVBCs Preferentially Innervate Subpopulations of CA1 PCs, paragraph 2;\n    Figure S1F; Table S1\n  quote: There were no differences between dPCs and sPCs in terms of their firing frequency as a\n    function of intracellularly injected current (Figure S1E) and in input resistance (Figure\n    S1F)\n  expected:\n  - quantity: sPC input resistance (Table S1, experimental)\n    value: 117\n    tolerance: 11.7\n    unit: MOhm\n  - quantity: dPC input resistance (Table S1, experimental)\n    value: 124\n    tolerance: 12.4\n    unit: MOhm\n  criterion: 'From the Supplemental Experimental Procedures 2B, voltage responses to 1 s steps\n    from -100 to +100 pA in 50 pA increments, cells held at -70 mV, measured at steady state\n    0.8 to 1.0 s after step onset. How resistance is computed from these responses is not\n    stated. Readings: (a) the slope of a linear fit of steady-state voltage against current\n    over the five steps; (b) the mean of the change from the pre-step baseline divided by the\n    current, over the four non-zero steps. Per cell, then mean per group. Reproduced when, under\n    one reading, both group means are within tolerance and the groups do not differ by the\n    paper''s rule (two-tailed unpaired t test, Mann-Whitney if Shapiro-Wilk fails, p >= 0.05).\n    Partially reproduced when the groups do not differ but a mean falls outside tolerance.'\n- id: figs1g-resting-potential\n  statement: Superficial PCs have more depolarized resting membrane potentials than deep PCs\n    (about -66 against -72 mV uncorrected; -80.9 against -86.6 mV corrected for the junction\n    potential).\n  source: Results, PVBCs Preferentially Innervate Subpopulations of CA1 PCs, paragraph 2;\n    Figure S1G; Table S1\n  quote: However, sPCs showed more depolarized resting membrane potentials (Figure S1G)\n  statistics:\n  - test: two-tailed unpaired t test, or Mann-Whitney test when Shapiro-Wilk fails\n    p: 0.05\n    p_relation: <\n    n: 8 sPCs and 9 dPCs\n  expected:\n  - quantity: sPC resting potential, uncorrected (Table S1 -80.9 mV plus the 14.6 mV junction\n      potential; Figure S1G shows about -66 mV)\n    value: -66.3\n    tolerance: 6.63\n    unit: mV\n  - quantity: dPC resting potential, uncorrected (Table S1 -86.6 mV plus 14.6 mV; Figure S1G\n      shows about -72 mV)\n    value: -72.0\n    tolerance: 7.2\n    unit: mV\n  criterion: 'The paper does not say how the resting potential was measured. It is read as the\n    membrane potential with no injected current: the pre-step baseline of sweeps whose current\n    channel shows zero holding current. Table S1''s footnote says the biological PCs were given\n    an unrecorded tonic current during the sweeps to rest at -84.6 mV (corrected), and the\n    Methods say cells were held at -70 mV; if the files show a holding current, or no current\n    channel and a baseline at the holding level, the sweeps do not hold the resting potential\n    and the claim cannot be tested on them. Otherwise reproduced when sPCs are more depolarized\n    than dPCs by the paper''s rule (two-tailed unpaired t test, Mann-Whitney if Shapiro-Wilk\n    fails, p < 0.05) and both means are within tolerance; partially reproduced when the\n    difference holds but a mean falls outside.'\n- id: figs1h-sag\n  statement: Superficial PCs show larger sag potentials than deep PCs in response to large\n    hyperpolarizing current pulses (about 8.7 against 5.6 mV).\n  source: Results, PVBCs Preferentially Innervate Subpopulations of CA1 PCs, paragraph 2;\n    Figure S1H\n  quote: as reported before (Jarsky et al., 2008), larger sag potentials in response to large\n    hyperpolarizing current pulses (Figure S1H)\n  statistics:\n  - test: two-tailed unpaired t test, or Mann-Whitney test when Shapiro-Wilk fails\n    p: 0.05\n    p_relation: <\n    n: 8 sPCs and 9 dPCs\n  expected:\n  - quantity: sPC sag amplitude (read from Figure S1H)\n    value: 8.7\n    tolerance: 0.87\n    unit: mV\n  - quantity: dPC sag amplitude (read from Figure S1H)\n    value: 5.6\n    tolerance: 0.56\n    unit: mV\n  criterion: 'Sag amplitude is the difference between the peak hyperpolarization during the\n    step and the steady state; the paper does not define the windows or the step. Steady state\n    is taken as the mean at 0.8 to 1.0 s, the window the Supplemental Experimental Procedures 2B\n    use for input resistance, and the peak as the most negative voltage in the step (a standard\n    choice). The step is open; readings (a) -400 pA, the largest step of the protocol (Figure\n    S3C plots sag against current down to -400 pA, and its biological values there are of the\n    size of Figure S1H), (b) -300 pA, (c) -200 pA. Reproduced when, under one reading, sPC sag\n    exceeds dPC sag by the paper''s rule (two-tailed unpaired t test, Mann-Whitney if\n    Shapiro-Wilk fails, p < 0.05) and both means are within tolerance; partially reproduced when\n    the difference holds under a reading but no reading puts both means within tolerance.'\n- id: tables1-rheobase\n  statement: The experimental superficial and deep PCs have the same rheobase, +150 pA, at the\n    50 pA resolution of the step protocol.\n  source: Table S1 and its footnote\n  inferred: Values from Table S1 (Experimental Rheobase, dPC +150, sPC +150 pA); no sentence of\n    the text states them.\n  expected:\n  - quantity: sPC rheobase\n    value: 150\n    tolerance: 0\n    unit: pA\n  - quantity: dPC rheobase\n    value: 150\n    tolerance: 0\n    unit: pA\n  criterion: 'Rheobase is the smallest step that evokes firing, excluding the tonic current\n    (Table S1 footnote); steps are on a 50 pA grid, so a 10% tolerance admits only the reported\n    step and the tolerance is set to 0. How a group value is formed is not stated. Readings: (a)\n    the median of per-cell rheobases; (b) the mean of per-cell rheobases rounded to the nearest\n    50 pA step; (c) the first step at which the group-mean firing frequency of Figure S1E is\n    above zero. Reproduced when, under one reading, both groups give +150 pA; partially\n    reproduced when they give the same step but not +150 pA.'\n- id: figs3f-pvbc-firing\n  statement: A biological PV+ basket cell does not fire up to +300 pA and its firing rises\n    steeply above that, to about 17 Hz at +400, 36 Hz at +450 and 52 Hz at +500 pA, matched by\n    the PVBC model.\n  source: Figure S3F and legend\n  inferred: Values read from Figure S3F (open triangles); the legend says only \"Firing frequency\n    of model and biological PVBCs in response to suprathreshold current injections\".\n  expected:\n  - quantity: PVBC firing at +400 pA\n    value: 17\n    tolerance: 1.7\n    unit: Hz\n  - quantity: PVBC firing at +450 pA\n    value: 36\n    tolerance: 3.6\n    unit: Hz\n  - quantity: PVBC firing at +500 pA\n    value: 52\n    tolerance: 5.2\n    unit: Hz\n  criterion: 'Firing frequency per step as in figs1e-if-curves, under either of its readings.\n    The figure shows one biological PVBC and does not name it, nor whether it is one cell or a\n    mean. Readings: (a) any one of the data set''s PV+ basket cells; (b) the mean over them,\n    using the steps every cell has. Reproduced when, under one reading, there is no firing from\n    0 to +300 pA and the three values are within tolerance; partially reproduced when the onset\n    is between +300 and +400 pA but the values are outside tolerance.'\n- id: fig1e-euipsc-dpc-larger\n  statement: PVBCs evoke effective unitary IPSCs about three times larger in dPCs than in sPCs,\n    in septal CA1 (65.2 against 19.6 pA) and temporal CA1 (65.0 against 24.9 pA).\n  source: Results, PVBCs Preferentially Innervate Subpopulations of CA1 PCs, paragraph 3;\n    Figure 1C to 1E\n  quote: 'septal: dPC: 65.2 ± 17.2 pA, n = 7; sPC: 19.6 ± 5.4 pA, n = 7; p < 0.05; temporal: dPC:\n    65.0 ± 8.3 pA, n = 17; sPC: 24.9 ± 3.9 pA, n = 22; p < 0.005'\n  statistics:\n  - about: septal dPC against sPC\n    test: two-tailed unpaired t test, or Mann-Whitney test when Shapiro-Wilk fails\n    p: 0.05\n    p_relation: <\n    n: 7 dPCs and 7 sPCs\n  - about: temporal dPC against sPC\n    test: two-tailed unpaired t test, or Mann-Whitney test when Shapiro-Wilk fails\n    p: 0.005\n    p_relation: <\n    n: 17 dPCs and 22 sPCs\n  expected:\n  - quantity: septal dPC euIPSC\n    value: 65.2\n    tolerance: 17.2\n    unit: pA\n  - quantity: septal sPC euIPSC\n    value: 19.6\n    tolerance: 5.4\n    unit: pA\n  - quantity: temporal dPC euIPSC\n    value: 65.0\n    tolerance: 8.3\n    unit: pA\n  - quantity: temporal sPC euIPSC\n    value: 24.9\n    tolerance: 3.9\n    unit: pA\n- id: fig1-uipsc-successes\n  statement: Counting successful events only, unitary IPSCs are also larger in dPCs than in sPCs\n    (68.4 against 32.4 pA, septal and temporal pooled).\n  source: Results, PVBCs Preferentially Innervate Subpopulations of CA1 PCs, paragraph 3\n  quote: 'Note that the difference in IPSC amplitudes was significant also when only the\n    successful events were considered ... dPC: 68.4 ± 6.9 pA, n = 24; sPC: 32.4 ± 3.5 pA, n =\n    29; data pooled from septal and temporal CA1, p < 0.005'\n  statistics:\n  - test: two-tailed unpaired t test, or Mann-Whitney test when Shapiro-Wilk fails\n    p: 0.005\n    p_relation: <\n    n: 24 dPCs and 29 sPCs\n  expected:\n  - quantity: dPC uIPSC\n    value: 68.4\n    tolerance: 6.9\n    unit: pA\n  - quantity: sPC uIPSC\n    value: 32.4\n    tolerance: 3.5\n    unit: pA\n- id: fig1f-connection-probability\n  statement: The PVBC to PC connection probability does not differ between sPCs and dPCs\n    (septal 50% and 50%; temporal 48.9% and 43.6%).\n  source: Results, PVBCs Preferentially Innervate Subpopulations of CA1 PCs, paragraph 3;\n    Figure 1F\n  quote: 'the robust difference in IPSC amplitudes was present without a difference in\n    connection probability ... (Figure 1F; septal: sPCs: 50%; dPCs: 50%; temporal: sPCs:\n    48.9%; dPCs: 43.6%)'\n  expected:\n  - quantity: septal sPC connection probability\n    value: 50\n    tolerance: 5\n    unit: '%'\n  - quantity: septal dPC connection probability\n    value: 50\n    tolerance: 5\n    unit: '%'\n  - quantity: temporal sPC connection probability\n    value: 48.9\n    tolerance: 4.89\n    unit: '%'\n  - quantity: temporal dPC connection probability\n    value: 43.6\n    tolerance: 4.36\n    unit: '%'\n  criterion: A claim of absence, judged by Pearson's chi-square test on connected and tested\n    pairs (Statistical Analysis, Figure 1F), per region, at p < 0.05. Reproduced when neither\n    region shows a significant difference.\n- id: fig1g-somatic-distance\n  statement: Somatic distances of PVBC-sPC pairs (76.2 um) and PVBC-dPC pairs (70.4 um) do not\n    differ, so the larger dPC IPSCs are not due to pair geometry.\n  source: Results, PVBCs Preferentially Innervate Subpopulations of CA1 PCs, paragraph 3;\n    Figure 1G\n  quote: since the somatic distances of the PVBC-sPC pairs (76.2 ± 4.7 mm; n = 38) and the\n    PVBC-dPC pairs (70.4 ± 6.3 mm; n = 30) were not different (p > 0.5; Figure 1G\n  statistics:\n  - test: two-tailed unpaired t test, or Mann-Whitney test when Shapiro-Wilk fails\n    p: 0.5\n    p_relation: \">\"\n    n: 38 PVBC-sPC and 30 PVBC-dPC pairs\n  expected:\n  - quantity: PVBC-sPC somatic distance\n    value: 76.2\n    tolerance: 4.7\n    unit: um\n  - quantity: PVBC-dPC somatic distance\n    value: 70.4\n    tolerance: 6.3\n    unit: um\n- id: fig1-common-pvbc\n  statement: When an sPC and a dPC share a presynaptic PVBC, the dPC euIPSC is still larger\n    (63.8 against 22.1 pA, 8 sequential paired recordings).\n  source: Results, PVBCs Preferentially Innervate Subpopulations of CA1 PCs, paragraph 3\n  quote: 'the larger euIPSCs in dPCs compared to sPCs were also observed when the postsynaptic\n    cells shared a common presynaptic PVBC (n = 8 sequential paired recordings; dPC: 63.8 ±\n    15.9 pA; sPC: 22.1 ± 5.5 pA; p < 0.001)'\n  statistics:\n  - test: two-tailed paired t test, or Wilcoxon signed-rank test when Shapiro-Wilk fails\n    p: 0.001\n    p_relation: <\n    n: 8 sequential paired recordings\n  expected:\n  - quantity: dPC euIPSC, common PVBC\n    value: 63.8\n    tolerance: 15.9\n    unit: pA\n  - quantity: sPC euIPSC, common PVBC\n    value: 22.1\n    tolerance: 5.5\n    unit: pA\n- id: fig1i-distance-correlation\n  statement: euIPSC amplitude correlates with PC distance from stratum radiatum (septal R2 =\n    0.389, temporal R2 = 0.356), but not within either group alone (temporal sPC R2 = 0.027,\n    dPC R2 = 0.045).\n  source: Results, PVBCs Preferentially Innervate Subpopulations of CA1 PCs, paragraph 4;\n    Figure 1I\n  quote: 'While there was a correlation between distance of the postsynaptic PCs from the\n    stratum radiatum and the euIPSC amplitude (Figure 1I; R2 = 0.389, p < 0.05, septal CA1; R2 =\n    0.356, p < 0.005, temporal CA1), this was driven by the overall difference between sPCs and\n    dPCs, as no correlation remained when examining either group individually (R2 = 0.027, p =\n    0.22, sPC; R2 = 0.045, p = 0.20, dPC'\n  statistics:\n  - about: septal, all PCs\n    test: linear fit\n    statistic: R2 = 0.389\n    p: 0.05\n    p_relation: <\n  - about: temporal, all PCs\n    test: linear fit\n    statistic: R2 = 0.356\n    p: 0.005\n    p_relation: <\n  - about: temporal sPCs\n    test: linear fit\n    statistic: R2 = 0.027\n    p: 0.22\n  - about: temporal dPCs\n    test: linear fit\n    statistic: R2 = 0.045\n    p: 0.2\n  expected:\n  - quantity: R2, septal\n    value: 0.389\n    tolerance: 0.0389\n  - quantity: R2, temporal\n    value: 0.356\n    tolerance: 0.0356\n- id: fig1-kmeans-large-small\n  statement: K-means with two clusters splits euIPSCs into small (mean 22.5 pA) and large (82.1\n    pA) amplitudes, and large ones are more frequent in dPCs (10 of 17) than in sPCs (3 of 22).\n  source: Results, PVBCs Preferentially Innervate Subpopulations of CA1 PCs, paragraph 4\n  quote: we performed a K-means test for two-clusters, which indicated a ''small''-amplitude\n    euIPSC cluster with a mean of 22.5 pA, and a ''large''-amplitude cluster with a mean of 82.1\n    pA ... (3 of 22 average euIPSCs recorded from sPCs were ''large'' amplitude versus 10 of 17\n    from dPCs, p < 0.01, Pearson's chi-square test)\n  statistics:\n  - test: Pearson's chi-square test\n    p: 0.01\n    p_relation: <\n    n: 22 sPCs and 17 dPCs\n  expected:\n  - quantity: small cluster mean\n    value: 22.5\n    tolerance: 2.25\n    unit: pA\n  - quantity: large cluster mean\n    value: 82.1\n    tolerance: 8.21\n    unit: pA\n  - quantity: large euIPSCs among sPCs\n    value: 3\n    tolerance: 0\n  - quantity: large euIPSCs among dPCs\n    value: 10\n    tolerance: 1\n- id: fig1j-axon-terminals\n  statement: Single PVBCs form about twice as many putative perisomatic axon terminals on dPCs\n    as on sPCs (8.7 against 4.0).\n  source: Results, PVBCs Preferentially Innervate Subpopulations of CA1 PCs, paragraph 5;\n    Figure 1J\n  quote: 'PVBCs formed significantly more perisomatic axon terminals on dPCs compared to sPCs\n    (Figures 1J and S1I; dPC: 8.7 ± 0.9, n = 10; sPC: 4.0 ± 0.6, n = 10; p < 0.005)'\n  statistics:\n  - test: two-tailed unpaired t test, or Mann-Whitney test when Shapiro-Wilk fails\n    p: 0.005\n    p_relation: <\n    n: 10 dPCs and 10 sPCs\n  expected:\n  - quantity: terminals per dPC\n    value: 8.7\n    tolerance: 0.9\n  - quantity: terminals per sPC\n    value: 4.0\n    tolerance: 0.6\n- id: fig1-release-properties\n  statement: PVBC to dPC inputs have a smaller coefficient of variation (0.61 against 1.00) and\n    a higher probability of release (0.92 against 0.66) than PVBC to sPC inputs, with no\n    difference in paired-pulse ratio (71.6% against 88.9%).\n  source: Results, PVBCs Preferentially Innervate Subpopulations of CA1 PCs, paragraph 5\n  quote: 'the PVBC-to-dPC unitary inputs were accompanied by smaller coefficient of variation\n    (dPC: 0.61 ± 0.06, n = 17; sPC: 1.00 ± 0.06, n = 22; p < 0.001) and larger probability of\n    success in GABA release (dPC: 0.92 ± 0.03, n = 17; sPC: 0.66 ± 0.04, n = 22; p < 0.001),\n    without differences in short-term plasticity properties'\n  statistics:\n  - about: coefficient of variation\n    test: two-tailed unpaired t test, or Mann-Whitney test when Shapiro-Wilk fails\n    p: 0.001\n    p_relation: <\n    n: 17 dPCs and 22 sPCs\n  - about: probability of success\n    test: two-tailed unpaired t test, or Mann-Whitney test when Shapiro-Wilk fails\n    p: 0.001\n    p_relation: <\n    n: 17 dPCs and 22 sPCs\n  - about: paired-pulse ratio\n    test: two-tailed unpaired t test, or Mann-Whitney test when Shapiro-Wilk fails\n    p: 0.3\n    p_relation: \">\"\n    n: 17 dPCs and 22 sPCs\n  expected:\n  - quantity: dPC CV\n    value: 0.61\n    tolerance: 0.06\n  - quantity: sPC CV\n    value: 1.0\n    tolerance: 0.06\n  - quantity: dPC probability of success\n    value: 0.92\n    tolerance: 0.03\n  - quantity: sPC probability of success\n    value: 0.66\n    tolerance: 0.04\n  - quantity: dPC paired-pulse ratio\n    value: 71.6\n    tolerance: 7.6\n    unit: '%'\n  - quantity: sPC paired-pulse ratio\n    value: 88.9\n    tolerance: 9.9\n    unit: '%'\n  criterion: CV from 50 events per pair including failures; paired-pulse ratio as the second\n    over the first response to 10 Hz presynaptic stimulation (Supplemental Experimental\n    Procedures 2A). The paired-pulse part is a claim of absence, judged by the paper's rule at\n    p < 0.05.\n- id: fig1k-somatic-dendritic-ratio\n  statement: The ratio of somatic to proximal dendritic PVBC boutons is similar on sPCs and dPCs.\n  source: Results, PVBCs Preferentially Innervate Subpopulations of CA1 PCs, paragraph 5;\n    Figure 1K\n  quote: the ratio of the number of somatic versus proximal dendritic PVBC boutons was similar\n    between PVBC-sPC and PVBC-dPC pairs (Figure 1K; p > 0.38)\n  statistics:\n  - test: two-tailed unpaired t test, or Mann-Whitney test when Shapiro-Wilk fails\n    p: 0.38\n    p_relation: \">\"\n    n: 10 sPCs and 10 dPCs\n- id: fig1l-pv-boutons\n  statement: dPC somata are surrounded by about twice as many PV+ boutons as sPC somata (107.3\n    against 55.0).\n  source: Results, PVBCs Preferentially Innervate Subpopulations of CA1 PCs, paragraph 6;\n    Figure 1L\n  quote: 'the number of PV+ boutons around the somata of single dPCs were approximately 2-fold\n    higher than in the case of sPCs (dPC: 107.3 ± 7.8, n = 7; sPC: 55.0 ± 2.8, n = 5; p <\n    0.005)'\n  statistics:\n  - test: two-tailed unpaired t test, or Mann-Whitney test when Shapiro-Wilk fails\n    p: 0.005\n    p_relation: <\n    n: 7 dPCs and 5 sPCs\n  expected:\n  - quantity: PV+ boutons per dPC soma\n    value: 107.3\n    tolerance: 7.8\n  - quantity: PV+ boutons per sPC soma\n    value: 55.0\n    tolerance: 2.8\n- id: fig1n-optogenetic-ipsc\n  statement: Light activation of PV+ cells in PV-ChR2 slices evokes larger IPSCs in dPCs than in\n    simultaneously recorded sPCs (382.3 against 141.6 pA).\n  source: Results, PVBCs Preferentially Innervate Subpopulations of CA1 PCs, paragraph 7;\n    Figure 1M and 1N\n  quote: 'resulted in significantly larger optogentically evoked IPSCs in dPCs compared to sPCs\n    (dPC: 382.3 ± 47.8 pA, n = 8; sPC: 141.6 ± 26.3 pA, n = 8; p < 0.005'\n  statistics:\n  - test: two-tailed paired t test, or Wilcoxon signed-rank test when Shapiro-Wilk fails\n    p: 0.005\n    p_relation: <\n    n: 8 dPC-sPC dual recordings\n  expected:\n  - quantity: dPC light-evoked IPSC\n    value: 382.3\n    tolerance: 47.8\n    unit: pA\n  - quantity: sPC light-evoked IPSC\n    value: 141.6\n    tolerance: 26.3\n    unit: pA\n- id: fig2c-fullfield-running\n  statement: In running mice, full-field PV+ axonal GCaMP5 fluorescence rises more in the deep\n    than in the superficial sublayer (dF/F 43.4% against 30.3%).\n  source: Results, Running Evokes Preferential Activation of PVBC Axon Terminals around the\n    Somata of dPCs, paragraph 1; Figure 2B and 2C\n  quote: 'the running-associated increases in full-field axonal fluorescence were significantly\n    larger in the deep compared to the superficial sublayer (Figures 2B and 2C; deep: DF/F =\n    43.4% ± 3.7%; superficial: 30.3% ± 2.4%; n = 10 superficial-deep FOV pairs in 5 mice; p <\n    0.05)'\n  statistics:\n  - test: two-tailed paired t test, or Wilcoxon signed-rank test when Shapiro-Wilk fails\n    p: 0.05\n    p_relation: <\n    n: 10 superficial-deep FOV pairs in 5 mice\n  expected:\n  - quantity: deep full-field dF/F during running\n    value: 43.4\n    tolerance: 3.7\n    unit: '%'\n  - quantity: superficial full-field dF/F during running\n    value: 30.3\n    tolerance: 2.4\n    unit: '%'\n- id: fig2e-bouton-roi-running\n  statement: Running-evoked fluorescence of single PV+ bouton ROIs does not differ between the\n    sublayers (60.4% against 59.3%).\n  source: Results, Running Evokes Preferential Activation of PVBC Axon Terminals around the\n    Somata of dPCs, paragraph 2; Figure 2D and 2E\n  quote: 'there was no difference in the enhancement in PV+ bouton ROI fluorescence between the\n    sublayers (Figure 2E; deep: DF/F = 60.4% ± 6.2%, n = 5; superficial: 59.3% ± 7.2%, n = 5; p\n    > 0.5)'\n  statistics:\n  - test: two-tailed paired t test, or Wilcoxon signed-rank test when Shapiro-Wilk fails\n    p: 0.5\n    p_relation: \">\"\n    n: 5 deep and 5 superficial\n  expected:\n  - quantity: deep bouton dF/F during running\n    value: 60.4\n    tolerance: 6.2\n    unit: '%'\n  - quantity: superficial bouton dF/F during running\n    value: 59.3\n    tolerance: 7.2\n    unit: '%'\n- id: fig2f-bouton-density\n  statement: In anesthetized mice, two-photon imaging shows more PV+ boutons in the deep than in\n    the superficial sublayer.\n  source: Results, Running Evokes Preferential Activation of PVBC Axon Terminals around the\n    Somata of dPCs, paragraph 2; Figure 2F\n  quote: found significantly higher numbers of PV+ boutons in the deep compared to the\n    superficial sublayer (Figure 2F)\n  statistics:\n  - test: two-tailed t test, or its rank equivalent when Shapiro-Wilk fails\n    p: 0.05\n    p_relation: <\n- id: figs2-ais-correction\n  statement: Axon initial segment-targeting boutons are 12.7% of PV+ boutons in the deep and\n    4.2% in the superficial sublayer, and after correcting for them the running-evoked rise\n    remains larger in the deep sublayer (37.9% against 29.0%).\n  source: Results, Running Evokes Preferential Activation of PVBC Axon Terminals around the\n    Somata of dPCs, paragraph 3; Figure S2\n  quote: 'The results showed that 12.7% (229 out of 1,803) of the PV+ boutons in the deep\n    sublayer and 4.2% (49 out of 1,161) of the PV+ boutons in the superficial sublayer were axon\n    initial segment-targeting boutons ... (corrected DF/F, deep: 37.9% ± 3.3%; superficial:\n    29.0% ± 2.2%; p < 0.05)'\n  statistics:\n  - test: two-tailed paired t test, or Wilcoxon signed-rank test when Shapiro-Wilk fails\n    p: 0.05\n    p_relation: <\n    n: 10 superficial-deep FOV pairs\n  expected:\n  - quantity: AIS-targeting share, deep\n    value: 12.7\n    tolerance: 1.27\n    unit: '%'\n  - quantity: AIS-targeting share, superficial\n    value: 4.2\n    tolerance: 0.42\n    unit: '%'\n  - quantity: corrected deep dF/F\n    value: 37.9\n    tolerance: 3.3\n    unit: '%'\n  - quantity: corrected superficial dF/F\n    value: 29.0\n    tolerance: 2.2\n    unit: '%'\n- id: fig2gi-pvbc-axon-sublayers\n  statement: Single PVBCs, filled in vitro (7) or in vivo (4), have longer axons and more\n    boutons in the deep than in the superficial sublayer, with no difference in interbouton\n    distance.\n  source: Results, Running Evokes Preferential Activation of PVBC Axon Terminals around the\n    Somata of dPCs, paragraph 4; Figure 2G to 2I\n  quote: analysis showed significantly longer axons (Figure 2G) and more boutons (Figure 2H)\n    belonging to single PVBCs in the deep compared to the superficial sublayer ... the\n    interbouton distance was not different (Figure 2I)\n- id: fig3c-spc-excite-pvbc\n  statement: sPCs connect to PVBCs three times as often as dPCs do (48.2%, 27 of 56, against\n    16%, 8 of 50), with no difference in euEPSC amplitude (46.7 against 33.3 pA).\n  source: Results, CA1 sPCs Are More Likely to Provide Excitatory Inputs to PVBCs, paragraph 1;\n    Figure 3A to 3C\n  quote: 'the connection probability between sPCs to PVBCs was three times higher compared to\n    dPCs to PVBCs (Figures 3A and 3C; dPC: 16%, 8/50 pairs connected; sPC: 48.2%, 27/56; p <\n    0.001), with no difference in the euEPSC amplitudes (Figure 3B; dPC: 33.3 ± 5.1 pA, n = 8;\n    sPC: 46.7 ± 10.7 pA, n = 27; p > 0.1)'\n  statistics:\n  - about: connection probability\n    test: Pearson's chi-square test\n    p: 0.001\n    p_relation: <\n    n: 50 dPC and 56 sPC pairs\n  - about: euEPSC amplitude\n    test: two-tailed unpaired t test, or Mann-Whitney test when Shapiro-Wilk fails\n    p: 0.1\n    p_relation: \">\"\n    n: 8 dPC and 27 sPC connections\n  expected:\n  - quantity: sPC to PVBC connected pairs\n    value: 27\n    tolerance: 2.7\n  - quantity: dPC to PVBC connected pairs\n    value: 8\n    tolerance: 0.8\n  - quantity: dPC euEPSC\n    value: 33.3\n    tolerance: 5.1\n    unit: pA\n  - quantity: sPC euEPSC\n    value: 46.7\n    tolerance: 10.7\n    unit: pA\n- id: fig3-epsc-release-properties\n  statement: Release probability (0.74 against 0.70) and short-term plasticity (89.1% against\n    82.3%) of PC to PVBC synapses do not differ between dPCs and sPCs.\n  source: Results, CA1 sPCs Are More Likely to Provide Excitatory Inputs to PVBCs, paragraph 1\n  quote: there was no difference in the probability of success in glutamate release from dPCs\n    (0.74 ± 0.06, n = 8) versus sPCs (0.70 ± 0.05, n = 27; p < 0.05), and the short-term\n    plasticity properties were also similar between the two groups (dPC: 89.1% ± 16.7%, n = 8;\n    sPC: 82.3% ± 9.8%, n = 18; p > 0.5)\n  statistics:\n  - about: release probability (printed p < 0.05 in a sentence that reports no difference)\n    test: two-tailed unpaired t test, or Mann-Whitney test when Shapiro-Wilk fails\n    p: 0.05\n    p_relation: <\n    n: 8 dPCs and 27 sPCs\n  - about: paired-pulse ratio\n    test: two-tailed unpaired t test, or Mann-Whitney test when Shapiro-Wilk fails\n    p: 0.5\n    p_relation: \">\"\n    n: 8 dPCs and 18 sPCs\n  expected:\n  - quantity: dPC release probability\n    value: 0.74\n    tolerance: 0.06\n  - quantity: sPC release probability\n    value: 0.70\n    tolerance: 0.05\n  - quantity: dPC paired-pulse ratio\n    value: 89.1\n    tolerance: 16.7\n    unit: '%'\n  - quantity: sPC paired-pulse ratio\n    value: 82.3\n    tolerance: 9.8\n    unit: '%'\n  criterion: A claim of absence. The sentence reports no difference in release probability but\n    prints p < 0.05, which contradicts it; the sentence's words are taken, and the claim is\n    judged by the paper's rule at p < 0.05 for both measures.\n- id: fig3ef-reciprocal-motifs\n  statement: PVBCs connect to sPCs, and to dPCs, with similar probability and euIPSC amplitude\n    whether or not the PC excites the PVBC.\n  source: Results, CA1 sPCs Are More Likely to Provide Excitatory Inputs to PVBCs, paragraph 3;\n    Figure 3E and 3F\n  quote: PVBCs formed unitary connections with similar probability and strength with sPCs\n    regardless of whether the sPCs provided excitatory input to the PVBC (Figure 3E). A similar\n    scenario was observed for dPCs (Figure 3F)\n  criterion: A claim of absence, judged by Pearson's chi-square test for connection probability\n    and the paper's unpaired rule for euIPSC amplitude, at p < 0.05, for sPCs and dPCs apart.\n- id: fig4b-pvbc-inhibit-firing\n  statement: Theta-nested gamma bursts of PVBCs reduce dPC firing (2.1 to 0.6 Hz) more than sPC\n    firing (2.2 to 1.6 Hz), from similar baseline rates.\n  source: Results, PVBCs Nonuniformly Inhibit the Action Potential Discharges of PCs, paragraph\n    1; Figure 4A and 4B\n  quote: 'change in dPCs firing during theta-nested gamma-frequency discharges of PVBCs: 2.1 ±\n    0.2 Hz to 0.6 ± 0.2 Hz, n = 7; in sPC: from 2.2 ± 0.1 Hz to 1.6 ± 0.3 Hz, n = 8; p < 0.05'\n  statistics:\n  - about: inhibition of firing, dPC against sPC\n    test: two-tailed unpaired t test, or Mann-Whitney test when Shapiro-Wilk fails\n    p: 0.05\n    p_relation: <\n    n: 7 dPC and 8 sPC pairs\n  - about: baseline firing, sPC against dPC\n    test: two-tailed unpaired t test, or Mann-Whitney test when Shapiro-Wilk fails\n    p: 0.5\n    p_relation: \">\"\n    n: 8 sPCs and 7 dPCs\n  expected:\n  - quantity: dPC firing before\n    value: 2.1\n    tolerance: 0.2\n    unit: Hz\n  - quantity: dPC firing during PVBC bursts\n    value: 0.6\n    tolerance: 0.2\n    unit: Hz\n  - quantity: sPC firing before\n    value: 2.2\n    tolerance: 0.1\n    unit: Hz\n  - quantity: sPC firing during PVBC bursts\n    value: 1.6\n    tolerance: 0.3\n    unit: Hz\n- id: fig4d-model-feedforward\n  statement: In the network model, extra excitation to sPCs lowers dPC firing more than extra\n    excitation to dPCs lowers sPC firing, and sPCs are more sensitive to their own extra\n    excitation than dPCs.\n  source: Results, Computational Simulations Indicate Preferential Feedforward Inhibition from\n    the Superficial to Deep PC Sublayer, paragraphs 1 and 2; Figure 4C to 4E\n  quote: increasing excitation selectively to sPCs in the model caused a larger decrease in dPC\n    firing than the decrease in sPC firing that occurred after increasing excitation selectively\n    to dPCs (Figure 4D; p < 0.001), and the sPCs in the network (subject to less PVBC\n    inhibition) were more sensitive to increasing levels of excitation than the dPCs\n  statistics:\n  - test: Tukey-Kramer test\n    p: 0.001\n    p_relation: <\n    n: three statistically independent simulations\n  data: with_inputs\n  criterion: Needs the network model of ModelDB 153280, run as the Supplemental Experimental\n    Procedures 8 describe (control, and +5, 10, 15, 20, 30 and 40% afferents to sPCs or to dPCs;\n    three independent networks; 5,000 ms at 0.05 ms steps), rates normalized to control.\n    Reproduced when the decrease in dPC rate with excitation to sPCs exceeds the decrease in sPC\n    rate with excitation to dPCs by Tukey-Kramer at p < 0.05, and sPC rates rise more with\n    their own extra excitation than dPC rates.\n- id: fig4ef-model-pvbc-rates\n  statement: In the model, control PC rates are about 2.4 Hz; adding 5% excitation to sPCs\n    raises sPC firing 34% and PVBC firing 65%, while adding 10% to dPCs raises dPC firing 38%\n    but PVBC firing only 15%.\n  source: Results, Computational Simulations Indicate Preferential Feedforward Inhibition from\n    the Superficial to Deep PC Sublayer, paragraphs 1 and 2; Figure 4C, 4E and 4F\n  quote: While a 34% increase in sPC firing rate resulted in a 65% increase in PVBC firing, a 38%\n    increase in dPC firing rate only resulted in a 15% increase in PVBC firing (Figure 4F)\n  data: with_inputs\n  depends_on:\n  - fig4d-model-feedforward\n  expected:\n  - quantity: control PC firing rate\n    value: 2.4\n    tolerance: 0.24\n    unit: Hz\n  - quantity: sPC rate increase, +5% to sPCs\n    value: 34\n    tolerance: 3.4\n    unit: '%'\n  - quantity: PVBC rate increase, +5% to sPCs\n    value: 65\n    tolerance: 6.5\n    unit: '%'\n  - quantity: dPC rate increase, +10% to dPCs\n    value: 38\n    tolerance: 3.8\n    unit: '%'\n  - quantity: PVBC rate increase, +10% to dPCs\n    value: 15\n    tolerance: 1.5\n    unit: '%'\n  criterion: From simulations of ModelDB 153280 as in fig4d-model-feedforward; each value is the\n    mean over the three networks. Reproduced when all are within tolerance; partially\n    reproduced when the PVBC increase is larger for the sPC condition but some value is outside.\n- id: fig5-cckbc-nonselective\n  statement: CCKBCs evoke similar euIPSCs in dPCs and sPCs (42.2 against 42.9 pA) with similar\n    connection probability (44% against 40%), similar pair distances and bouton numbers, and no\n    PC to CCKBC excitatory connections were found (0 of 28 deep, 0 of 23 superficial).\n  source: Results, Cholecystokinin-Expressing Basket Cells Do Not Preferentially Innervate CA1\n    sPCs versus dPCs, paragraph 1; Figure 5C to 5H, S4\n  quote: 'the IPSCs generated by the CCKBCs were similar between sPCs and dPCs (Figures 5B and\n    5C; euIPSCs amplitude; dPC: 42.2 ± 8.5 pA, n = 20; sPC: 42.9 ± 8.8 pA, n = 21; p > 0.5; data\n    from the temporal hippocampus). In addition, there was also no difference in connection\n    probability (Figure 5D; dPC: 44%; sPC: 40%; p > 0.62)'\n  statistics:\n  - about: euIPSC amplitude\n    test: two-tailed unpaired t test, or Mann-Whitney test when Shapiro-Wilk fails\n    p: 0.5\n    p_relation: \">\"\n    n: 20 dPCs and 21 sPCs\n  - about: connection probability\n    test: Pearson's chi-square test\n    p: 0.62\n    p_relation: \">\"\n  - about: somatic distance\n    test: two-tailed unpaired t test, or Mann-Whitney test when Shapiro-Wilk fails\n    p: 0.5\n    p_relation: \">\"\n    n: 25 CCKBC-sPC and 22 CCKBC-dPC pairs\n  - about: CCKBC boutons per PC\n    test: two-tailed unpaired t test, or Mann-Whitney test when Shapiro-Wilk fails\n    p: 0.5\n    p_relation: \">\"\n    n: 9 sPCs and 9 dPCs\n  - about: CB1R+ boutons per PC soma\n    test: two-tailed unpaired t test, or Mann-Whitney test when Shapiro-Wilk fails\n    p: 0.5\n    p_relation: \">\"\n  expected:\n  - quantity: dPC euIPSC from CCKBCs\n    value: 42.2\n    tolerance: 8.5\n    unit: pA\n  - quantity: sPC euIPSC from CCKBCs\n    value: 42.9\n    tolerance: 8.8\n    unit: pA\n  - quantity: dPC connection probability\n    value: 44\n    tolerance: 4.4\n    unit: '%'\n  - quantity: sPC connection probability\n    value: 40\n    tolerance: 4\n    unit: '%'\n  criterion: Claims of absence, each judged by the paper's test (unpaired rule for amplitudes,\n    distances and bouton counts; Pearson's chi-square for connection probability) at p < 0.05.\n    Reproduced when none differs and no PC to CCKBC connection is found.\n- id: fig6c-parallel-projections\n  statement: mPFC- and AMG-projecting dPCs of temporal CA1 are largely separate populations\n    (17% of mPFC-projecting and 14% of AMG-projecting cells double-labelled), and mPFC- and\n    AMG-projecting PCs lie mostly in the deep sublayer.\n  source: Results, Heterogeneous PVBC Microcircuits as a Function of Long-Distance Targets of\n    CA1 PCs, paragraphs 2 and 3; Figure 6B and 6C, S5C\n  quote: 'mPFCPCs also labeled from AMG: 17%, 54 colabeled cells out of 314 cells; AMGPCs also\n    labeled from mPFC: 14%, 54/385 colabeled cells; n = 3 animals), indicating that the mPFCPCs\n    and AMGPCs form a largely segregated, parallel projection pathway from the CA1'\n  expected:\n  - quantity: mPFC-projecting cells also labelled from AMG\n    value: 17\n    tolerance: 1.7\n    unit: '%'\n  - quantity: AMG-projecting cells also labelled from mPFC\n    value: 14\n    tolerance: 1.4\n    unit: '%'\n- id: fig6e-amg-larger-ipsc\n  statement: PVBCs evoke euIPSCs three times larger in AMG-projecting than in mPFC-projecting\n    dPCs (64.0 against 21.0 pA), with similar connection probability (36% against 32.1%) and\n    twice as many perisomatic terminals (6.0 against 3.0).\n  source: Results, Heterogeneous PVBC Microcircuits as a Function of Long-Distance Targets of\n    CA1 PCs, paragraph 4; Figure 6D and 6E, S5D\n  quote: 'PVBCs evoked significantly larger euIPSCs in postsynaptic AMGPCs compared to mPFCPCs\n    (Figures 6D and 6E; AMG: 64.0 ± 12.6 pA, n = 9; mPFC: 21.0 ± 3.5 pA, n = 9; p < 0.05 ...\n    PVBCs formed significantly more perisomatic axon terminals on AMGPCs compared to mPFCPCs\n    (AMG: 6.0 ± 0.4, n = 4; mPFC: 3.0 ± 0.4, n = 4; p < 0.005)'\n  statistics:\n  - about: euIPSC amplitude\n    test: ANOVA followed by Tukey-Kramer test\n    p: 0.05\n    p_relation: <\n    n: 9 AMG and 9 mPFC dPCs\n  - about: perisomatic terminals\n    test: two-tailed unpaired t test, or Mann-Whitney test when Shapiro-Wilk fails\n    p: 0.005\n    p_relation: <\n    n: 4 AMG and 4 mPFC dPCs\n  expected:\n  - quantity: AMG dPC euIPSC\n    value: 64.0\n    tolerance: 12.6\n    unit: pA\n  - quantity: mPFC dPC euIPSC\n    value: 21.0\n    tolerance: 3.5\n    unit: pA\n  - quantity: PVBC-mPFC connected pairs (of 28)\n    value: 9\n    tolerance: 0.9\n  - quantity: PVBC-AMG connected pairs (of 24)\n    value: 9\n    tolerance: 0.9\n  - quantity: terminals per AMG dPC\n    value: 6.0\n    tolerance: 0.4\n  - quantity: terminals per mPFC dPC\n    value: 3.0\n    tolerance: 0.4\n- id: fig6g-mpfc-excite-pvbc\n  statement: mPFC-projecting dPCs excite PVBCs far more often (33.3%) than AMG- (4.2%) or\n    MEC-projecting (5%) dPCs.\n  source: Results, Heterogeneous PVBC Microcircuits as a Function of Long-Distance Targets of\n    CA1 PCs, paragraph 5; Figure 6F and 6G\n  quote: 'mPFCPCs were significantly more likely than AMGPCs or MECPCs to display excitatory\n    connections with PVBCs (Figures 6F and 6G; mPFC: 33.3%; AMG: 4.2%; MEC: 5%; p < 0.025'\n  statistics:\n  - test: Pearson's chi-square test\n    corrected: Bonferroni-Holm\n    p: 0.025\n    p_relation: <\n  expected:\n  - quantity: mPFC dPC to PVBC connection probability\n    value: 33.3\n    tolerance: 3.33\n    unit: '%'\n  - quantity: AMG dPC to PVBC connection probability\n    value: 4.2\n    tolerance: 0.42\n    unit: '%'\n  - quantity: MEC dPC to PVBC connection probability\n    value: 5\n    tolerance: 0.5\n    unit: '%'\n- id: figs1-pc-morphology\n  statement: dPCs have larger somata and longer basal dendrites than sPCs, with similar apical\n    dendritic length.\n  source: Results, PVBCs Preferentially Innervate Subpopulations of CA1 PCs, paragraph 2;\n    Figure S1A to S1D; Figure S3A legend\n  quote: there were some morphological differences between the dPCs and sPCs, with the dPCs\n    having larger basal dendritic trees and somata (Figures S1A-S1D)\n  expected:\n  - quantity: dPC soma surface area (Figure S3A legend)\n    value: 822\n    tolerance: 82.2\n    unit: um2\n  - quantity: sPC soma surface area (Figure S3A legend)\n    value: 636\n    tolerance: 63.6\n    unit: um2\n"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  python tools/claims_check.py claims/crcns-hc-10/10.1016-j.neuron.2014.03.034.yaml paper/10.1016-j.neuron.2014.03.034.txt 2>&1 | tail -40
```

Result: not kept, because it reads the paper's text.

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/crcns-hc-10/10.1016-j.neuron.2014.03.034.yaml",
 "old_string": "  quote: there was no difference in the probability of success in glutamate release from dPCs\n    (0.74 ± 0.06, n = 8) versus sPCs (0.70 ± 0.05, n = 27; p < 0.05), and the short-term\n    plasticity properties were also similar between the two groups (dPC: 89.1% ± 16.7%, n = 8;\n    sPC: 82.3% ± 9.8%, n = 18; p > 0.5)",
 "new_string": "  quote: 'there was no difference in the probability of success in glutamate release from dPCs\n    (0.74 ± 0.06, n = 8) versus sPCs (0.70 ± 0.05, n = 27; p < 0.05), and the short-term\n    plasticity properties were also similar between the two groups (dPC: 89.1% ± 16.7%, n = 8;\n    sPC: 82.3% ± 9.8%, n = 18; p > 0.5)'"
}
```

```
The file claims/crcns-hc-10/10.1016-j.neuron.2014.03.034.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd  python tools/claims_check.py claims/crcns-hc-10/10.1016-j.neuron.2014.03.034.yaml paper/10.1016-j.neuron.2014.03.034.txt 2>&1 | tail -30
```

Result: not kept, because it reads the paper's text.

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/crcns-hc-10/10.1016-j.neuron.2014.03.034.yaml",
 "old_string": "  quote: increasing excitation selectively to sPCs in the model caused a larger decrease in dPC",
 "new_string": "  quote: increasing excitation selectively to sPCs in the model caused a ... larger decrease in dPC"
}
```

```
The file claims/crcns-hc-10/10.1016-j.neuron.2014.03.034.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd  python tools/claims_check.py claims/crcns-hc-10/10.1016-j.neuron.2014.03.034.yaml paper/10.1016-j.neuron.2014.03.034.txt 2>&1 | tail -30; grep -c "—\|rather" claims/crcns-hc-10/*.yaml
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  python -c "
import yaml;c=yaml.safe_load(open('claims/crcns-hc-10/10.1016-j.neuron.2014.03.034.yaml'))['claims']
print(len(c),sum('quote' in x for x in c),sum('statistics' in x for x in c),sum('criterion' in x for x in c),sum('expected' in x for x in c))"; git status --short
```

```
34 32 25 13 29
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
?? claims/crcns-hc-10/
?? scripts
?? uv.lock
```

**Agent calls Bash**

```bash
cd  ls -la --time-style=full-iso uv.lock; head -5 uv.lock
```

```
-rw-r--r-- 1 runner runner 185534 2026-11-06 03:19:35.565423537 +0000 uv.lock
version = 1
revision = 5
requires-python = ">=3.10"
resolution-markers = [
    "python_full_version >= '3.12'",
```

**Agent calls Bash**

```bash
cd  rm uv.lock
```

```
(Bash completed with no output)
```

**Agent**

I wrote `claims/crcns-hc-10/10.1016-j.neuron.2014.03.034.yaml`, and the quote checker passes it with 0 problems.

**Text read.** The version of record with its Supplemental Information, from `paper/`. That covers the main text, Experimental Procedures, the legends for Figures 1–6 and S1–S5, Table S1 and the Supplemental Experimental Procedures. Values that appear only in figures (S1E–H and S3F) were read from rendered PDF pages, and the file marks them as read from a figure.

**Code read.** The model code the paper links, ModelDB 153280 ("superdeep", README dated May 15, 2014, zip sha256 recorded in the file). It holds only the network model. It has no analysis of the experimental cells, so it settles none of the intrinsic-property criteria. Two other links in the paper are dead: the lab page is a parked domain and the Open Source Brain page returns 404.

**What the dataset holds.** Current-step sweeps from 8 superficial and 9 deep pyramidal cells (PCs) and 6 PV+ basket cells (PVBCs). These match the n of Figure S1E–H and the step protocol in Supplemental Experimental Procedures 8A. Six claims concern these recordings: I-F curves, input resistance, resting potential, sag, rheobase, and PVBC firing (Figure S3F). The other claims cover the paper's main findings, whose data the dataset does not hold. The two model claims need runs of the ModelDB code, so they are marked `with_inputs`.

**Counts.**
- 34 claims.
- 32 have quotes. The other 2 have `inferred` notes: the Table S1 rheobase and the Figure S3F values.
- 25 have statistics, 29 have expected values, and 13 have criteria.

**Details the paper leaves open, with the readings named:**
- **Firing frequency:** spikes per 1 s step, or (n−1) over the time from first to last spike (the form the Figure S3E model legend implies). The I-F claim is a claim of absence judged on the paper's two-way ANOVA; a repeated-measures ANOVA is shown as a variant.
- **Input resistance:** slope of a linear V–I fit, or the mean of ΔV/I. The 0.8–1.0 s window and the ±100 pA steps come from the Methods.
- **Sag:** which step to use: −400, −300 or −200 pA. Steady state is taken at 0.8–1.0 s, borrowed from the input-resistance method.
- **Resting potential:** how it was measured is not stated. Table S1 says an unrecorded tonic current was applied during the sweeps. If the files show a holding current, the claim cannot be tested on them.
- **Rheobase group value:** median of per-cell values, mean rounded to the 50 pA step, or the first step where the group-mean I-F curve is above zero.
- **Figure S3F PVBC:** the cell is not named. Readings: any one of the dataset's 6 PVBCs, or their mean.
- **Tests:** the text never says which test each comparison used. Each claim records the Methods rule: two-tailed t test, switching to Mann-Whitney or Wilcoxon when Shapiro-Wilk fails.

**Gaps and inconsistencies in the paper:**
- Sag amplitude and the I-F values exist only in figures, as noted above.
- The release-probability comparison in Figure 3 prints "p < 0.05" in a sentence that reports no difference. The statistic is recorded as printed, and the criterion follows the sentence's words.
- The Figure 6G connection probabilities give no denominators.
- The simulation results are not deposited anywhere: the README offers them on request.

Nothing the claims need is missing from the text.

## End of run

41 turns, 6 minutes, $2.64 at API prices, result: success.
