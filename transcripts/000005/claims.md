# 000005 · claims · run 39469618243

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
grep -n "^#" docs/protocol.md | head -50; ls paper/ claims/000005/ claims/001453/
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "docs/protocol.md",
 "limit": 170
}
```

```
1	# Protocol for an attempt
2	
3	Version: `pilot-10`. Record this version in the attempt's provenance.
4	
5	This is what agents, or people, do to attempt a target and deposit the
6	result. It is written from the pilot attempts
7	([pilot notes](pilot-notes.md)); the reasons for the rules are there.
8	
9	An attempt has three roles, each a separate run with a separate context:
10	
11	- The **reader** reads the paper and writes the claims file: every finding,
12	  and how each is to be tested, taken from the paper. A second reader checks
13	  it against the paper. Readers never see the dandiset's data.
14	- The **author** tests the claims on the dandiset. It reads the paper to
15	  understand the claims, but the claims file binds it: it cannot change a
16	  claim, and it asks a reader for any method detail the file lacks.
17	- The **verifier** checks the author's work and must not be the author.
18	
19	So every claim and its method are fixed from the paper before anyone analyses
20	the data, and no method is chosen by the agent that runs the analysis.
[... 150 more lines not kept]
```

**Agent calls Bash**

```bash
cat claims/000005/10.1038-nn.4412.yaml; wc -l paper/10.1038-nn.4412.txt; head -30 paper/10.1038-nn.4412.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
tail -40 claims/000005/10.1038-nn.4412.yaml; echo ----; cat claims/001453/*.yaml | head -150
```

```
depends_on:
  - fs-suppress-movement-spiking
  criterion: For the same excitatory cells, touch selectivity computed inside the light epochs of
    light trials and inside the same span of trials without light. Reproduced when selectivity is
    lower with light in most cells and a one-sided Wilcoxon signed-rank test gives p < 0.05;
    partially reproduced when lower in most cells without significance; not reproduced otherwise.
- id: thalamus-drives-fs
  statement: Thalamic activity drives L4 FS interneurons.
  source: Results, Inhibition is driven by thalamus, paragraph 2; Figure 6d,e
  quote: Photoinhibition reduced spike rates in FS interneurons during nonwhisking (to 4% of control
    ... and whisking epochs (to 13% of control ... as well as in response to touch (to 32% of control
    ... FS interneurons were thus driven by input from the thalamus.
  statistics:
  - about: Nonwhisking spike rate with and without thalamic photoinhibition
    p: 5.0e-4
    n: 13 neurons
  - about: Whisking spike rate with and without thalamic photoinhibition
    p: 6.0e-5
    n: 15 neurons
  - about: Touch response with and without thalamic photoinhibition
[... 171 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "paper/10.1038-nn.4412.txt",
 "offset": 30,
 "limit": 700
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
awk 'NR>=730 && (length($0)>45 || /^=== page/)' paper/10.1038-nn.4412.txt | head -400
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/2e2d51b6-46f0-49e4-9a2e-f9e127d273bf/tool-results/bfidfj3wa.txt"
}
```

```
1	Figure 4  Membrane potential of L4 FS interneurons. (a) Top, labeled nonspiny FS interneuron (FS No. 1). Bottom, recording configuration. 
2	Right, spike waveform. (b) Membrane potential of example L4 FS interneuron. (c) Same as b but for a trial without touches, in which the pole was 
3	in a distal location. (d) Touch-aligned membrane potential for 3 neurons. Top, example curvature changes; middle, Vm traces, spikes of 10 example 
4	trials and Vm average of all touches; bottom, PSTH. (e) Membrane potential aligned to whisking onset. Top, example whisker trajectories; middle, 
5	Vm traces, spikes of 10 example trials and Vm average of all whisking transitions; bottom, PSTH. (f) Average touch- and whisking-aligned 
6	Vm (7 L4 FS interneurons), ordered by resting Vm. (g) Distribution of the distance from membrane potential to spike threshold (distance to threshold) 
7	in three example neurons for different behavioral periods (nonwhisking, whisking and touch). The 10th, 50th and 90th percentiles are marked. 
8	Spike threshold is at 0 mV. Dashed lines denote the s.d. of spike threshold across individual spikes. (h) Comparison of the 10th percentile in 
9	distance-to-threshold distribution for different behavioral periods. Colors correspond to those in f.
10	© 2016 Nature America, Inc., part of Springer Nature. All rights reserved.
11	=== page 7 ===
12	nature NEUROSCIENCE  VOLUME 19 | NUMBER 12 | DECEMBER 2016	
13	To remove sensory input, we transected the infraorbital nerve 
14	(ION)22, which carries all mechanosensory information from the 
15	whisker pad to the brain (Fig. 7a). Mice still searched for the pole 
16	during the sample epoch (Supplementary Video 3), with similar 
17	whisking amplitudes and time courses as under control conditions 
18	(data not shown); however, as they were unable to sense the object, 
19	Figure 5  Spiking of VPM neurons, L4 excitatory neurons and L4 FS interneurons. (a) VPM→L4 circuit schematic. Cell types are color-coded: 
20	VPM, black
[... 381 more lines not kept]
```

**Agent calls Bash**

```bash
grep -n "=== page\|Supplementary Figure 1\b\|Supplementary Table" paper/10.1038-nn.4412.txt | head -60
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1038-nn.4412.txt",
 "offset": 1539,
 "limit": 600
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -n 2139,2541p paper/10.1038-nn.4412.txt | awk 'length($0)>25' | head -150
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -n 2124,2541p paper/10.1038-nn.4412.txt | tr '\n' '|' | fold -w 250
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1038-nn.4412.supp.pdf",
 "pages": "25"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
python3 -c "
import fitz
d=fitz.open('paper/10.1038-nn.4412.supp.pdf'); p=d[24]
for b in p.get_text('words'): pass
rows={}
for w in p.get_text('words'):
    rows.setdefault(round(w[1]/4),[]).append((w[0],w[4]))
for k in sorted(rows): print(' '.join(t for _,t in sorted(rows[k])))
"
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
python3 -c "import pypdf" 2>&1; python3 -c "import pdfplumber" 2>&1; which pdftotext mutool
```

```
Exit code 1
Traceback (most recent call last):
  File "<string>", line 1, in <module>
    import pypdf
ModuleNotFoundError: No module named 'pypdf'
Traceback (most recent call last):
  File "<string>", line 1, in <module>
    import pdfplumber
ModuleNotFoundError: No module named 'pdfplumber'
```

**Agent calls Bash**

```bash
ls; grep -rl "000005" --include=*.yaml --include=*.md --include=*.json . 2>/dev/null | grep -v "^./paper" | head -20
```

```
LICENSE
README.md
attempts
bunfig.toml
claims
docs
entries
node_modules
package-lock.json
package.json
paper
papers
pnpm-lock.yaml
questions
schemas
scripts
targets
tests
tools
transcripts
[... 21 more lines not kept]
```

**Agent calls Bash**

```bash
ls targets papers | head; grep -rl '"000005"\|000005' targets papers 2>/dev/null | head
```

```
papers:
manifest.yaml
triage.yaml

targets:
dandisets.json
pilot.yaml
targets/dandisets.json
papers/manifest.yaml
```

**Agent calls Bash**

```bash
python3 -c "
import json;d=json.load(open('targets/dandisets.json'))
items=d if isinstance(d,list) else d.get('dandisets',d)
for x in (items if isinstance(items,list) else items.values()):
    if '000005' in json.dumps(x)[:200]: print(json.dumps(x,indent=1)[:3000])
" ; grep -n -A12 "000005" papers/manifest.yaml | head -30
```

```
18:  '000005':
19-  - doi: 10.1038/nn.4412
20-    status: stored
21-    version: version of record
22-    source: PDF supplied by a person
23-    pdf: true
24-    supplements: 1
25-  '000006':
26-  - doi: 10.1038/s41586-018-0642-9
27-    status: stored
28-    version: version of record
29-    source: PDF supplied by a person
30-    pdf: true
```

**Agent calls Bash**

```bash
grep -n -B2 -A25 '"000005"' targets/dandisets.json | head -60
```

```
69-  },
70-  {
71:   "dandiset": "000005",
72-   "name": "Electrophysiology data from thalamic and cortical neurons during somatosensation",
73-   "published_version": "0.220126.1853",
74-   "asset_count": 148,
75-   "size_gb": 46.44,
76-   "data_standards": [
77-    "Neurodata Without Borders (NWB)"
78-   ],
79-   "species": [
80-    "House mouse"
81-   ],
82-   "approaches": [
83-    "electrophysiological approach",
84-    "optogenetic approach"
85-   ],
86-   "papers": [
87-    {
88-     "doi": "10.1038/nn.4412",
[... 8 more lines not kept]
```

**Agent calls Bash**

```bash
grep -n -A3 "Data and code availability\|github\|crcns" paper/10.1038-nn.4412.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
curl -sL -m 30 https://doi.org/10.6080/K0T43R01 | sed 's/<[^>]*>//g' | grep -v '^\s*$' | head -120
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
curl -sL -m 30 https://crcns.org/data-sets/ssc/ssc-7 | sed 's/<[^>]*>//g' | grep -v '^\s*$' | sed -n '/About ssc-7\|ssc-7 (Somatosensory/,$p' | sed -n '120,260p'; curl -sL -m 30 https://crcns.org/data-sets/ssc/ssc-7/about-ssc-7 | sed 's/<[^>]*>//g' | grep -v '^\s*$' | tail -100
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
sed -n 943,1300p paper/10.1038-nn.4412.txt | grep -v -E '^\s*[-−–0-9.,%°οo]*\s*$' | grep -E '.{30,}' | sed -n '1,400p' | grep -n -i -E 'AUC|strong responses|nonwhisking|Kruskal|reafference|ION|touch' | head -60
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
grep -n -A2 "including modulation correlated with self-movement\|did not depend on a\|P = 0.80" paper/10.1038-nn.4412.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
ls schemas tools; sed -n 1,200p schemas/claims*.json 2>/dev/null | head -200
```

```
schemas:
attempt.schema.json
claims.schema.json
entry.schema.json

tools:
agent_run.py
archive_transcripts.sh
build_site.py
build_targets.py
claims_check.py
conversion_issue.py
entry.py
flagged.py
get_papers.sh
papers_manifest.py
progress.py
readme_row.py
runner
site_assets
[... 203 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 200,400p schemas/claims.schema.json
```

```
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
            "enum": [
[... 127 more lines not kept]
```

**Agent calls Bash**

```bash
pip install --quiet --target "$TMPDIR/pylib" pymupdf 2>&1 | tail -2; PYTHONPATH="$TMPDIR/pylib" python3 -c "import fitz;print(fitz.__doc__)"
```

```
[notice] A new release of pip is available: 26.2.1 -> 26.2.2
[notice] To update, run: pip install --upgrade pip
[0;93m2026-10-20 17:54:41.209751539 [W:onnxruntime:Default, device_discovery.cc:95 GetPciBusId] Skipping pci_bus_id for PCI path at "/sys/devices/LNXSYSTM:00/LNXSYBUS:00/ACPI0004:00/MSFT1000:00/5620e0c7-8062-4dce-aeb7-520c7ef76171" because filename "5620e0c7-8062-4dce-aeb7-520c7ef76171" did not match expected pattern of [0-9a-f]+:[0-9a-f]+:[0-9a-f]+[.][0-9a-f]+[m
/tmp/claude-1001/pylib/fitz/__init__.py:17: FutureWarning: The `fitz` API is deprecated and will be removed in future. Use `import pymupdf` instead.
  warnings.warn(
PyMuPDF 2.0: Python bindings for the MuPDF 1.28.5 library.
Python 3.13 running on linux (64-bit).
```

**Agent calls Bash**

```bash
cd $TMPDIR && PYTHONPATH="$TMPDIR/pylib" python3 -c "
import pymupdf
d=pymupdf.open('$PWD/paper/10.1038-nn.4412.supp.pdf'.replace('$TMPDIR','')) if False else pymupdf.open('paper/10.1038-nn.4412.supp.pdf')
for i in [9,24]:
    d[i].get_pixmap(dpi=110).save(f'supp{i+1}.png')
" 2>&1 | grep -v Warn; ls $TMPDIR/*.png
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/supp10.png"
}
```

Result: no output.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/supp25.png"
}
```

Result: no output.

**Agent calls Bash**

```bash
sed -n 768,943p paper/10.1038-nn.4412.txt | grep -n -i "spikes\|touch\|NW\|whisk\|AUC\|%" | head -40; echo ---; sed -n 1123,1269p paper/10.1038-nn.4412.txt | grep -v -E '^\s*[-−–0-9.,%°οo]*\s*$' | awk 'length($0)<45' | head -60
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd $TMPDIR && PYTHONPATH="$TMPDIR/pylib" python3 -c "
import pymupdf
d=pymupdf.open('paper/10.1038-nn.4412.pdf')
print(len(d))
for i in [6,8]:
    d[i].get_pixmap(dpi=130).save(f'main{i+1}.png')
" 2>&1 | grep -v -i "warn\|onnx"
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/main9.png"
}
```

Result: not kept, because it reads the paper's text.

Result: no output.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/main7.png"
}
```

Result: no output.

**Agent calls Bash**

```bash
sed -n 1,60p tools/claims_check.py
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
cd $TMPDIR && PYTHONPATH="$TMPDIR/pylib" python3 -c "
import pymupdf
d=pymupdf.open('paper/10.1038-nn.4412.supp.pdf')
for i in [2,11]:
    d[i].get_pixmap(dpi=150).save(f'supp{i+1}.png')
" 2>&1 | grep -v -i "warn\|onnx"
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/supp3.png"
}
```

Result: not kept, because it reads the paper's text.

Result: no output.

**Agent calls Bash**

```bash
cd $TMPDIR && PYTHONPATH="$TMPDIR/pylib" python3 -c "
import pymupdf
d=pymupdf.open('paper/10.1038-nn.4412.supp.pdf')
p=d[2]; r=p.rect
clip=pymupdf.Rect(r.width*0.73,r.height*0.19,r.width*0.84,r.height*0.36)
p.get_pixmap(dpi=500,clip=clip).save('phasezoom.png')
" 2>&1 | grep -v -i "warn\|onnx"
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/phasezoom.png"
}
```

Result: not kept, because it reads the paper's text.

Result: no output.

**Agent calls Write**

```json
{
 "file_path": "claims/000005/10.1038-nn.4412.yaml",
 "content": "# Claims for Yu, Gutnisky, Hires & Svoboda (2016), Nat. Neurosci. 19, 1647-1657, on dandiset\n# 000005 (\"Electrophysiology data from thalamic and cortical neurons during somatosensation\").\n#\n# Provenance. Written by an agent (model \"claude-opus-5-5\", Claude Code in GitHub Actions),\n# 2026-10-20, protocol as stated in docs/protocol.md (version pilot-10), Reader steps 1 to 4.\n#\n# What changed. This file replaces a deprecated version whose claims were written from the\n# abstract only, with cell types and every measure chosen by the earlier author (proxy FS and\n# excitatory classes, a 6 to 30 Hz whisking band, a touch-selectivity index, Rayleigh and\n# harmonic phase tests). Read against the full text on 2026-10-20, the criteria of\n# exc-mainly-touch and fs-enhance-touch-selectivity tested measures the paper does not use, and\n# seven or more of the paper's findings on these data had no claim. Every claim is written again\n# here from the full text: statements, sources, quotes, statistics, expected values and criteria\n# all come from the paper. The ids of the eight earlier claims are kept where the finding is the\n# same (vpm-touch, vpm-whisking, fs-touch-and-whisking, exc-mainly-touch,\n# fs-suppress-movement-spiking, fs-enhance-touch-selectivity, thalamus-drives-fs,\n# sensory-input-drives-fs), so the outcomes can be compared; their criteria are new. The\n# earlier file's amendments and its proxy cell classes no longer apply. The new claims are\n# vpm-whisking-phase, exc-vm-touch-whisking, exc-threshold-touch-vs-whisking,\n# exc-effective-reversal, exc-inhibition-timing, fs-touch-response, fs-vm-touch-whisking,\n# fs-whisking-rate, fs-whisking-phase, vpm-photoinhibition, exc-thalamus-photoinhibition,\n# rabies-vpm-input, ion-cut-exc-no-touch, ion-cut-exc-whisking, ion-cut-exc-phase,\n# ion-cut-fs-no-touch, ion-cut-fs-phase, pv-enphr-suppression, exc-touch-spikes-enphr,\n# auc-weak-strong, auc-groups, behavior-false-alarms and behavior-touches.\n# This reader did not see the dandiset's data. It did read the deprecated file, whose opening\n# comment reports some outputs of the earlier attempt's first run under its own proxy measures;\n# no criterion below was set from them.\n#\n# Text read. The version of record (PDF supplied by a person, text extracted 2026-10-20, under\n# paper/), with its Online Methods and its one supplement PDF (Supplementary Figures 1 to 14 and\n# Supplementary Tables 1 and 2). PDF pages were opened only to read Supplementary Table 2, the\n# boundary drawn in Supplementary Figure 6, the number of phase bins in Supplementary Figure 2d,\n# and the P values printed in Figure 8d, which the text garbles or does not give.\n#\n# Code. The paper's data and code statement points to CRCNS ssc-7 (doi:10.6080/K0T43R01). Its\n# public pages (read 2026-10-20) describe NWB 1.0.6 data files and a data-description document;\n# no analysis code is listed and the download needs an account, so no code was read. Every\n# method below comes from the Online Methods, the figure legends or the supplement.\n#\n# The data the paper used (Online Methods; Supplementary Table 2).\n# - Head-fixed mice performing a lick/no-lick object localization task with 1 to 3 spared\n#   whiskers of one row; a pole in an anterior (no-lick) or one of several posterior (lick)\n#   locations; whisker angle and curvature from 1,000 fps video (Janelia Whisker Tracker); touch\n#   onsets and offsets of the principal whisker; licks; trial outcome. Videos are 5 s per trial.\n# - VPM: 29 single units from chronic silicon probes (4 x 8 sites, 19,531.25 Hz) in 6\n#   VGAT-ChR2-EYFP mice, each with a mapped principal whisker (Figs. 1, 5).\n# - L4 excitatory (E) neurons, 85 in control mice (Fig. 5): 37 whole-cell (Vm, 10 or 20 kHz)\n#   and 48 loose-seal cell-attached recordings, in VGAT-ChR2-EYFP, PV-IRES-Cre (eNpHR3.0),\n#   PV-IRES-Cre x Ai32, C57BL/6 and SOM-IRES-Cre x Ai32 mice (Supplementary Table 2).\n# - L4 FS interneurons, 26 in control mice per the Results and Methods (19 ChR2-tagged in\n#   VGAT-ChR2-EYFP mice, 5 whole-cell and 14 cell-attached; 4 eNpHR-inactivated in PV-IRES-Cre\n#   mice; 3 by waveform); Supplementary Figure 7 and Table 2 list 25. 7 were whole-cell.\n# - Thalamic photoinhibition: optic fiber in VPM of VGAT-ChR2-EYFP mice (10 mice), 5 ms pulses at\n#   100 Hz (Supplementary Fig. 9i), light in 25 to 50% of trials; 17 VPM multiunits recorded by\n#   pipette; L4 FS (13 to 15) and E neurons (12 whole-cell) recorded with and without light.\n# - ION transection (9 mice): 9 or 10 L4 E neurons whole-cell and 10 L4 FS neurons cell-attached.\n# - PV suppression: eNpHR3.0 in PV neurons of PV-IRES-Cre mice (9 injected), constant 594 nm\n#   light at the cortex on a subset of trials; 40 L4 E neurons and 4 L4 PV neurons; behavior of\n#   8 mice (Supplementary Fig. 14).\n# - Rabies tracing from L4 PV neurons (PV-IRES-Cre x Ai9; histology, Supplementary Fig. 10).\n#\n# Cell types. Recordings at manipulator depth 420 to 620 um count as L4 when unlabeled (Online\n# Methods, Barrel cortex recordings). FS interneurons are cells driven by 5 ms light pulses within\n# 5 ms of onset in VGAT-ChR2-EYFP mice and inside the waveform boundary of Supplementary Figure 6,\n# or PV cells inactivated by eNpHR, or the few identified by waveform and rate (Online Methods).\n# The boundary of Supplementary Figure 6 is drawn, not given in numbers; read from the figure it\n# lies near spike duration 0.27 ms and peak-to-trough ratio 2.8 (an approximate reading). Other\n# L4 cells are excitatory (Fig. 8e legend, \"putative excitatory neurons\"). Where the dandiset\n# labels cell types, the author uses its labels and reports how they map onto these rules.\n#\n# Measures used by the criteria, each from the paper.\n# - Touch. Touches of the principal whisker only; onsets pooled across pole locations;\n#   intertouch interval (offset of the previous touch to onset of the next) at least 25 ms for\n#   Figs. 1 to 7 and at least 10 ms for Fig. 8e (Online Methods, Data analysis; Behavior).\n# - Spikes per touch. Cortical neurons (Fig. 5) spikes 0 to 50 ms after touch onset minus 2 x the\n#   spikes 0 to 25 ms before; cortical neurons (Fig. 8e) spikes 4 to 20 ms after minus spikes 0\n#   to 16 ms before; VPM spikes 0 to 25 ms after minus 0 to 25 ms before; averaged over touches\n#   (Online Methods, Data analysis). 95% confidence interval by bootstrap (Fig. 5b legend), 1,000\n#   iterations (the number the Methods give for rate intervals).\n# - Spike latency. Touch PSTH in 1 ms bins; latency is the time from touch onset to the crossing\n#   by dPSTH/dt of 3 x the s.d. of dPSTH/dt 0 to 25 ms before onset; cells with no 1 ms bin of\n#   at least 10 spikes/s within 0 to 100 ms, or with no crossing, are left out (Online Methods).\n# - Whisking. Whisker angle band-passed 6 to 60 Hz (4th-order Butterworth), Hilbert transform\n#   for amplitude and phase (phase 0 most protracted, +-pi most retracted). Whisking epochs are\n#   whisking cycles whose amplitude at phase 0 exceeds 2.5 degrees, leaving out +-100 ms around\n#   licks and -10 to 100 ms around touches. Nonwhisking periods are periods of at least 100 ms\n#   with amplitude below 1.25 degrees and no touch or lick. Whisking onsets (transitions) are ends\n#   of nonwhisking periods followed by a rise of mean amplitude of at least 2 degrees with no touch\n#   within 250 ms (Online Methods, Data analysis).\n# - Rates. Spike rate in nonwhisking and in whisking periods from the extracted epochs, with a\n#   1,000-iteration bootstrap interval (Online Methods; Fig. 5d legend).\n# - Phase coupling. Spike rate (or Vm) in phase bins during whisking epochs, fitted by a sinusoid;\n#   r2 > 0.25 marks coupling (Supplementary Figs. 2e,f, 3f,g and 12a); coupling strength is half\n#   the peak-to-trough of the fit (Online Methods). For FS cells a sum of a sinusoid and one of\n#   twice the frequency is used when its r2 is 50% higher (Supplementary Fig. 7g). Supplementary\n#   Figure 2d shows 12 phase bins over -pi to pi (read from the figure; the text gives none).\n# - Vm. Spikes removed by interpolating Vm from 1 ms before to 4 ms after each spike; spike\n#   threshold where dVm/dt exceeds 3 s.d. of the trial's dVm/dt; each trial's threshold from a\n#   linear fit of threshold against trial number; -42 mV for silent neurons. Distance to\n#   threshold is threshold minus Vm over all time, its 10th percentile taken separately in\n#   nonwhisking, whisking and touch epochs (4 to 50 ms after touch onset). Touch PSP latency is\n#   where dVm/dt of the touch-aligned average crosses 3 x the s.d. of dVm/dt 0 to 25 ms before\n#   onset (Online Methods, Data analysis). Pre-touch Vm is the mean 0 to 5 ms before onset and the\n#   post-touch Vm is at the peak of the average PSP; pre-whisking Vm is the mean 0 to 200 ms\n#   before whisking onset and post-whisking Vm the mean 100 to 300 ms after (Supplementary Fig.\n#   4 legend).\n# - Tests. Wilcoxon rank-sum (unpaired), Wilcoxon signed-rank (paired), Kruskal-Wallis (Online\n#   Methods, Statistical analysis). Where a P is printed without a test, the test is the one the\n#   Methods give for that design. The paper states no significance level; it calls P = 0.046\n#   significant and P = 0.09 and 0.20 not significant, so 0.05 is used.\n#\n# Tolerances. Where the paper gives mean +- s.e.m., the s.e.m. Where it gives mean +- s.d. over n\n# cells, the larger of 10% of the value and s.d./sqrt(n): the s.d. is the spread across cells,\n# not the uncertainty of the mean, and s.d./sqrt(n) is the standard error those numbers imply.\n# Otherwise 10% of the value; counts get 10% of the count.\n#\n# Details the paper leaves open, with the readings each criterion runs (all are run; the outcome\n# is the one they all give, or the claim is methods_underspecified).\n# - O1 Filter direction of the 6 to 60 Hz band-pass. (a) zero-phase (forward and backward);\n#   (b) single forward pass.\n# - O2 Samples of the per-neuron rank-sum test of whisking against nonwhisking rate. (a) the rate\n#   in each whisking epoch against the rate in each nonwhisking period; (b) per trial, the rate\n#   in whisking epochs against that in nonwhisking periods.\n# - O3 The spike-threshold rule \"exceeded 3x s.d. of mean dVm/dt\". (a) dVm/dt above its trial\n#   mean by 3 s.d.; (b) dVm/dt above 3 s.d.\n# - O4 Resting Vm. (a) mean Vm in nonwhisking periods, spikes removed; (b) median of the same.\n# - O5 Light comparison windows. (a) epochs of light trials inside the light, against epochs of\n#   control trials inside the same span of trial time; (b) against epochs anywhere in control\n#   trials.\n# - O6 \"% of control\". (a) the population mean with light over the population mean without;\n#   (b) the median over cells of each cell's ratio.\n# - O7 Laser powers of the thalamic photoinhibition (dose-dependent, Supplementary Fig. 9i,j).\n#   (a) all powers pooled; (b) the highest power only.\n# - O8 Phase of the derivative-based latencies. The text fixes the 1 ms bins and gives no\n#   smoothing; read as the first difference of the unsmoothed PSTH (or Vm average).\n# Which cells enter each n (40 of the 43 E cells in PV-IRES-Cre mice; 13 to 15 FS cells in the\n# thalamic experiment) the paper does not say beyond the counts; cells enter a comparison when\n# they have epochs of each kind compared, and the counts are reported against the paper's.\nschema_version: 2\ndataset:\n  archive: dandi\n  id: \"000005\"\npaper: doi:10.1038/nn.4412\nclaims:\n- id: behavior-touches\n  statement: Mice touched the pole often when it was within reach (lick trials, 5.7 +- 5.3\n    touches per trial over 4,147 trials) and rarely when it was distal (0.9 +- 3.4 over 4,173\n    trials); performance was 0.72 +- 0.11 in cortical and 0.71 +- 0.07 in VPM recordings.\n  source: Online Methods, Behavior, paragraph 2\n  quote: Mice touched the pole at a proximal location multiple times (number of touches ... Mice\n    touched the pole at a distal location less often (number of touches, 0.9 ± 3.4, mean ± s.d.,\n    4,173 trials) and withheld licking. Average performance (proportion of correct trials) was 0.72\n    ± 0.11 (mean ± s.d., during the recordings of 111 cells) for cortical recordings and 0.71 ±\n    0.07 for VPM recordings (during the recordings of 29 cells).\n  expected:\n  - quantity: touches per trial, pole within reach (posterior, lick trials)\n    value: 5.7\n    tolerance: 0.57\n  - quantity: touches per trial, pole distal (anterior, no-lick trials)\n    value: 0.9\n    tolerance: 0.09\n  - quantity: proportion correct during cortical recordings (111 cells)\n    value: 0.72\n    tolerance: 0.072\n  - quantity: proportion correct during VPM recordings (29 cells)\n    value: 0.71\n    tolerance: 0.071\n  criterion: >-\n    Touches of the principal whisker counted per trial (Online Methods, Behavior), over the\n    trials of the 111 control cortical cells (85 E and 26 FS, Fig. 5) and, separately for\n    performance, the 29 VPM sessions; the touch counts pool the cortical recordings, which is\n    where the trial counts (4,147 and 4,173) come from, with the VPM sessions as a variant.\n    Reproduced when every expected value is within tolerance; partially reproduced when the\n    touch counts are and a performance value is not, or the reverse.\n- id: vpm-touch\n  statement: VPM neurons respond to active touch with a sharp, short-latency increase in spike\n    rate (0.6 +- 0.5 spikes per touch, median 0.4; latency 3.2 +- 1.0 ms, median 2.5 ms).\n  source: Results, Chronic extracellular recordings from somatosensory thalamus, paragraph 1;\n    Figure 1b,d; Figure 5b,c\n  quote: Neurons responded to active touch during behavior with an increase in spike rate (Fig. 1b).\n    The peristimulus time ... histogram aligned to touch onset showed a sharp peak in spike rate\n    (mean ± s.d., 0.6 ± 0.5 spikes per touch; median, 0.4 spikes per touch), with short latency\n    after touch onset (mean ± s.d., 3.2 ± 1.0 ms; median, 2.5 ms)\n  expected:\n  - quantity: mean VPM spikes per touch (29 neurons)\n    value: 0.6\n    tolerance: 0.093\n  - quantity: median VPM spikes per touch\n    value: 0.4\n    tolerance: 0.04\n  - quantity: mean VPM touch latency\n    value: 3.2\n    tolerance: 0.32\n    unit: ms\n  - quantity: median VPM touch latency\n    value: 2.5\n    tolerance: 0.25\n    unit: ms\n  criterion: >-\n    Over the 29 VPM units, spikes per touch by the VPM definition (0 to 25 ms after minus 0 to\n    25 ms before onset) and spike latency by the dPSTH/dt rule, on principal-whisker touches with\n    intertouch interval at least 25 ms (Online Methods, Data analysis; header, Measures). The\n    latency n is the units that pass the Methods' exclusion; the paper does not print it. Filter\n    readings O1 do not enter (no whisking measure); latency reading O8. Reproduced when all four\n    values are within tolerance; partially reproduced when the spikes-per-touch values are and a\n    latency value is not.\n- id: vpm-whisking\n  statement: VPM neurons fire at 5.1 +- 5.5 spikes/s without whisker movement or touch; most\n    (25 of 29) increase their rate during whisking without touch, and the mean rate rises from\n    5.1 to 13.5 spikes/s. Three of 29 do not increase with whisking but still respond to touch.\n  source: Results, Chronic extracellular recordings from somatosensory thalamus, paragraphs 1 and\n    2; Figure 1c,e; Figure 5d,e; Supplementary Figure 2b,c\n  quote: Typical VPM neurons showed significant spike rates (mean ± s.d., 5.1 ± 5.5 spikes per s;\n    median, 3.3 spikes per s; n = 29 neurons), even in the absence of whisker movement and touch.\n    ... Most VPM neurons increased their spike rate during whisking in the absence of touch (25 out\n    of 29 neurons ... The average spike rate increased severalfold after onset of whisker movement\n    (from 5.1 ± 5.5 spikes per s to 13.5 ± 12.7 spikes per s; P = 4 × 10−6; n = 29 neurons,\n    Wilcoxon signed-rank test\n  statistics:\n  - about: nonwhisking against whisking spike rate over VPM neurons\n    test: Wilcoxon signed-rank test\n    p: 4.0e-6\n    n: 29 neurons\n  expected:\n  - quantity: VPM neurons with a significant increase of rate during whisking\n    value: 25\n    tolerance: 2.5\n    unit: of 29 neurons\n  - quantity: mean nonwhisking rate\n    value: 5.1\n    tolerance: 1.02\n    unit: spikes/s\n  - quantity: median nonwhisking rate\n    value: 3.3\n    tolerance: 0.33\n    unit: spikes/s\n  - quantity: mean whisking rate\n    value: 13.5\n    tolerance: 2.36\n    unit: spikes/s\n  criterion: >-\n    Over the 29 VPM units, the rate in nonwhisking periods and in whisking epochs (Online\n    Methods; header, Measures). A unit increases when a Wilcoxon rank-sum test of whisking\n    against nonwhisking rate gives p < 0.05 with the whisking rate higher (Results, the test\n    named for the 25 of 29), under samples O2 (a) and (b) and filters O1 (a) and (b). The\n    population test is a Wilcoxon signed-rank test of per-unit nonwhisking against whisking rate.\n    Reproduced when the signed-rank test gives p < 0.05 with whisking higher and the expected\n    values are within tolerance; partially reproduced when the test holds and a value is not\n    within tolerance; not reproduced when the test fails.\n- id: vpm-whisking-phase\n  statement: The spike rate of VPM neurons is modulated by the phase of whisker movement.\n  source: Results, Chronic extracellular recordings from somatosensory thalamus, paragraph 2;\n    Supplementary Figure 2d-f\n  quote: The spike rate was modulated by the phase of the movement (Supplementary Fig. 2d).\n  depends_on:\n  - vpm-whisking\n  criterion: >-\n    For each VPM unit, spike rate in 12 phase bins during whisking epochs (Supplementary Fig.\n    2d, bins read from the figure), fitted with a sinusoid; a unit is phase modulated when r2 >\n    0.25 (Supplementary Fig. 2e,f). The paper gives no count; its histogram (Supplementary Fig.\n    2e) has most of the 29 units above 0.25 (about 23 to 26, read from the bars). Reproduced\n    when more than half of the 29 units have r2 > 0.25 under both filter readings O1; not\n    reproduced otherwise. The number above 0.25 and the coupling strengths are reported.\n- id: exc-vm-touch-whisking\n  statement: In L4 excitatory neurons (37 whole-cell), resting Vm spans -76 to -45 mV (-63 +- 8\n    mV); every neuron depolarizes after touch (latency 4.8 +- 0.8 ms, amplitude 6.0 +- 2.9 mV),\n    while whisking causes only a small depolarization or hyperpolarization (1.2 +- 2.1 mV).\n  source: Results, Membrane-potential dynamics of L4 excitatory neurons, paragraph 2; Figure 2f\n  quote: >-\n    Across the excitatory population, the resting membrane potential (Vm) spanned a large range\n    (−76 to −45 mV, mean ± s.d., −63 ± 8 mV; median, −64 mV, n = 37 neurons ... Touches evoked\n    short-latency depolarizations (latency: mean ± s.d., 4.8 ± 0.8 ms; median, 4.7 ms; amplitude:\n    mean ± s.d., 6.0 ± 2.9 mV; median, 5.7 mV; n = 37 neurons) for all neurons (Fig. 2f) ...\n    Whisking induced small depolarization or hyperpolarization (mean ± s.d., 1.2 ± 2.1 mV; median,\n    1.2 mV; Fig. 2f)\n  expected:\n  - quantity: mean resting Vm\n    value: -63\n    tolerance: 6.3\n    unit: mV\n  - quantity: mean touch PSP latency\n    value: 4.8\n    tolerance: 0.48\n    unit: ms\n  - quantity: mean touch PSP amplitude\n    value: 6.0\n    tolerance: 0.6\n    unit: mV\n  - quantity: mean whisking-evoked Vm change\n    value: 1.2\n    tolerance: 0.35\n    unit: mV\n  criterion: >-\n    The 37 whole-cell L4 E neurons of control mice. Touch-aligned average Vm (spikes removed)\n    over principal-whisker touches with intertouch interval at least 25 ms; latency by the\n    dVm/dt rule (reading O8); amplitude is the peak of the average minus the mean 0 to 5 ms\n    before onset (Supplementary Fig. 4 legend). Whisking change is the mean Vm 100 to 300 ms\n    after whisking onset minus the mean 0 to 200 ms before, averaged over onsets (Supplementary\n    Fig. 4 legend). Resting Vm by O4 (a) and (b). Reproduced when a touch latency is found in\n    every neuron with a positive amplitude and the four values are within tolerance; partially\n    reproduced when every neuron depolarizes and a value is out of tolerance.\n- id: exc-threshold-touch-vs-whisking\n  statement: Touch moves the membrane potential of L4 excitatory neurons much closer to spike\n    threshold than whisking does (shift 6.1 +- 3.2 mV against 1.1 +- 2.0 mV).\n  source: Results, Membrane-potential dynamics of L4 excitatory neurons, paragraph 2; Figure 2g,h\n  quote: Compared to whisking, touch caused a larger shift of membrane potential toward spike\n    threshold (whisking, 1.1 ± 2.0 mV; touch, 6.1 ± 3.2 mV; P = 1 × 10−7, Wilcoxon signed-rank test;\n    Fig. 2g,h)\n  statistics:\n  - about: touch against whisking shift toward threshold\n    test: Wilcoxon signed-rank test\n    p: 1.0e-7\n    n: 37 neurons\n  expected:\n  - quantity: mean whisking shift toward threshold\n    value: 1.1\n    tolerance: 0.33\n    unit: mV\n  - quantity: mean touch shift toward threshold\n    value: 6.1\n    tolerance: 0.61\n    unit: mV\n  criterion: >-\n    For each of the 37 whole-cell L4 E neurons, the 10th percentile of distance to threshold in\n    nonwhisking, whisking and touch epochs (Online Methods; header, Measures), with threshold\n    readings O3 (a) and (b) and filters O1. The shift is the nonwhisking value minus the\n    whisking (or touch) value (Fig. 2h compares these percentiles across periods; the baseline\n    period is the paper's nonwhisking period). Reproduced when the touch shift exceeds the\n    whisking shift by a Wilcoxon signed-rank test at p < 0.05 and both means are within\n    tolerance; partially reproduced when only the test holds.\n- id: exc-effective-reversal\n  statement: The effective reversal potential of the touch response of L4 excitatory neurons is\n    more depolarized than resting Vm, while that of whisking is close to rest and more\n    hyperpolarized than that of touch.\n  source: Results, Membrane-potential dynamics of L4 excitatory neurons, paragraph 2;\n    Supplementary Figure 4\n  quote: of the touch response was more depolarized than the resting Vm and sometimes crossed the\n    spike threshold ... In contrast, the effective reversal potential for whisker movement was\n    close to the resting Vm, below the spike threshold and more hyperpolarized than that for touch\n  criterion: >-\n    Per Supplementary Fig. 4 legend. For each touch, pre-Vm is the mean 0 to 5 ms before onset\n    and post-Vm the Vm at the peak time of the neuron's average PSP; for each whisking onset,\n    pre-Vm the mean 0 to 200 ms before and post-Vm the mean 100 to 300 ms after. dVm = post minus\n    pre, fitted linearly against pre-Vm; the reversal is where the line crosses zero. The legend\n    leaves open whether one line is fitted per neuron or over all neurons (panel b shows all\n    neurons, panel c compares reversals). Readings (a) per neuron, compared across the 37\n    neurons; (b) one pooled fit per event type. The paper reports no test. Reproduced when, under\n    the reading, the touch reversal lies above the whisking reversal (in more than half of the\n    neurons and in the medians for a) and above the median resting Vm; not reproduced otherwise.\n- id: exc-inhibition-timing\n  statement: With L4 excitatory neurons depolarized near 0 mV to reveal inhibition, touch evokes\n    strong, transient inhibition that follows excitation by 0.4 +- 0.8 ms at half maximum.\n  source: Results, Membrane-potential dynamics of L4 excitatory neurons, paragraph 3; Figure\n    3b-d\n  quote: Touch elicited strong and transient inhibitory input (Fig. 3b,c), which followed excitation\n    with a short delay (mean ± s.d., 0.4 ± 0.8 ms at half max; n = 6 neurons; Fig. 3d).\n  expected:\n    quantity: mean delay of inhibition after excitation at half maximum\n    value: 0.4\n    tolerance: 0.33\n    unit: ms\n  criterion: >-\n    The 6 L4 E neurons recorded both at rest and with steady depolarizing current (about 1 nA,\n    baseline near 0 mV; Online Methods, Barrel cortex recordings). For each, the touch-aligned\n    average Vm at rest (excitation) and with current (inhibition, sign inverted), each\n    normalized to its peak (Fig. 3d); the time at which each first reaches half its peak after\n    onset; the delay is inhibition minus excitation. Trials at depolarized potential are those\n    with injected current (or a Vm baseline near 0 mV, as the dandiset marks them). Reproduced\n    when the mean delay is within tolerance and positive in most of the neurons; not reproduced\n    otherwise.\n- id: fs-touch-response\n  statement: L4 FS interneurons fire at 9.3 +- 8.5 spikes/s without whisker movement and fire\n    1.9 +- 1.0 spikes per touch, with a spike latency of 5.3 +- 2.1 ms.\n  source: Results, Dynamics of L4 fast-spiking interneurons, paragraph 1; Figure 5b,c\n  quote: FS interneurons were active during baseline conditions, even in the absence of whisker\n    movements (mean ± s.d., 9.3 ± 8.5 spikes per s; median, 6.4 spikes per s; n = 26 neurons ...\n    and spike rates increased after touch (mean ± s.d., 1.9 ± 1.0 spikes per touch; median, 1.9\n    spikes per touch; n = 26 neurons ... and spiking (mean ± s.d., 5.3 ± 2.1 ms; median, 4.5 ms, n\n    = 24 neurons; Fig. 5c)\n  expected:\n  - quantity: mean FS nonwhisking rate\n    value: 9.3\n    tolerance: 1.67\n    unit: spikes/s\n  - quantity: mean FS spikes per touch\n    value: 1.9\n    tolerance: 0.2\n  - quantity: mean FS touch spike latency (24 neurons)\n    value: 5.3\n    tolerance: 0.53\n    unit: ms\n  criterion: >-\n    Over the control L4 FS cells (26 in the text, 25 in Supplementary Fig. 7; both sets\n    reported), the nonwhisking rate, spikes per touch by the cortical Fig. 5 definition and\n    spike latency by the dPSTH/dt rule with its exclusion (header, Measures; reading O8).\n    Reproduced when the three values are within tolerance; partially reproduced when two are.\n- id: fs-vm-touch-whisking\n  statement: In whole-cell L4 FS interneurons (n = 7), touch depolarizes the membrane by 7.0 +-\n    5.2 mV with onset 4.0 +- 0.6 ms, and whisking depolarizes it by 2.7 +- 2.1 mV toward\n    threshold.\n  source: Results, Dynamics of L4 fast-spiking interneurons, paragraphs 1 and 2; Figure 4d-h\n  quote: Membrane potential depolarized (mean ± s.d., 7.0 ± 5.2 mV; median, 6.7 mV; n = 7 neurons,\n    Fig. 4d,f) ... Response latencies were short for membrane potential depolarization (onset ...\n    4.0 ± 0.6 ms; median, 4.2 ms, n = 7 neurons; Fig. 4d,f) ... after onset of whisking, the\n    membrane potential of FS neurons depolarized closer to spike threshold (mean ± s.d., 2.7 ± 2.1\n    mV; median, 2.4 mV, n = 7 neurons; Fig. 4e–h)\n  expected:\n  - quantity: mean touch depolarization\n    value: 7.0\n    tolerance: 1.97\n    unit: mV\n  - quantity: mean touch Vm onset latency\n    value: 4.0\n    tolerance: 0.4\n    unit: ms\n  - quantity: mean whisking depolarization\n    value: 2.7\n    tolerance: 0.79\n    unit: mV\n  criterion: >-\n    The 7 whole-cell L4 FS cells. Touch amplitude and latency as in exc-vm-touch-whisking;\n    whisking depolarization as the post-onset (100 to 300 ms) minus pre-onset (0 to 200 ms) mean\n    Vm (Supplementary Fig. 4 legend, the paper's whisking-onset measure), with the nonwhisking\n    minus whisking 10th percentile of distance to threshold (Fig. 4h) as reading (b). Reproduced\n    when all three values are within tolerance under a reading; partially reproduced when the\n    touch values are and the whisking value is not.\n- id: fs-whisking-rate\n  statement: Most L4 FS interneurons (23 of 26) increase their spike rate during whisking without\n    touch and 3 of 26 decrease it; over the population the rate roughly doubles (to 21.1 +- 15.8\n    spikes/s).\n  source: Results, Dynamics of L4 fast-spiking interneurons, paragraph 2; Figure 5d,e\n  quote: most L4 FS neurons significantly increased their spike rate during whisker movement without\n    touch (23 of 26 neurons ... and a small subset (3 of 26 neurons ... decreased spike rate.\n    Overall, after onset of whisking ... and the spike rate doubled (mean ± s.d., 21.1 ± 15.8 spikes\n    per s; median, 14.6 spikes per s, n = 26 neurons, P = 2.7 × 10−5; Fig. 5d)\n  statistics:\n  - about: nonwhisking against whisking spike rate over FS neurons\n    p: 2.7e-5\n    n: 26 neurons\n  expected:\n  - quantity: FS neurons with a significant increase during whisking\n    value: 23\n    tolerance: 2.3\n    unit: of 26 neurons\n  - quantity: FS neurons with a significant decrease during whisking\n    value: 3\n    tolerance: 0.3\n    unit: of 26 neurons\n  - quantity: mean FS whisking rate\n    value: 21.1\n    tolerance: 3.1\n    unit: spikes/s\n  depends_on:\n  - fs-touch-response\n  criterion: >-\n    Over the control L4 FS cells, per-cell Wilcoxon rank-sum tests of whisking against\n    nonwhisking rate at p < 0.05 (Results), samples O2 (a) and (b), filters O1 (a) and (b). The\n    population test is not named; it is paired, so a Wilcoxon signed-rank test (Online Methods,\n    Statistical analysis). Reproduced when the signed-rank test gives p < 0.05 with whisking\n    higher and the counts and mean are within tolerance; partially reproduced when the test\n    holds and a value is not within tolerance; not reproduced when the test fails.\n- id: fs-whisking-phase\n  statement: Spikes of L4 FS interneurons are coupled to whisking phase.\n  source: Results, Dynamics of L4 fast-spiking interneurons, paragraph 2; Supplementary Figure\n    7d,g\n  quote: Spikes of L4 FS neurons were also coupled to whisking phase (Supplementary Fig. 7).\n  criterion: >-\n    For each control L4 FS cell, spike rate in 12 phase bins during whisking epochs, fitted with\n    a sinusoid, or a sinusoid plus one of twice the frequency when that raises r2 by 50%\n    (Supplementary Fig. 7g); coupled when r2 > 0.25 (the threshold of Supplementary Figs. 2e and\n    12a). Supplementary Fig. 7g shows fits for all 25 cells (18 single, 7 double). Reproduced\n    when more than half of the cells are coupled under both filter readings O1; not reproduced\n    otherwise.\n- id: fs-touch-and-whisking\n  statement: Touch- and whisking-evoked spikes are typically multiplexed in individual L4 FS\n    neurons, as in VPM neurons.\n  source: Results, Dynamics of L4 fast-spiking interneurons, paragraph 3; Figure 5b,d;\n    Supplementary Figure 7\n  quote: Touch- and whisking-evoked spikes were typically multiplexed in individual L4 FS neurons\n    (Fig. 5b,d and Supplementary Fig. 7), as in VPM neurons.\n  depends_on:\n  - fs-touch-response\n  - fs-whisking-rate\n  criterion: >-\n    A control L4 FS cell multiplexes when its spikes per touch (Fig. 5 definition) has a 95%\n    bootstrap interval above zero (Fig. 5b legend) and its whisking rate is significantly\n    different from its nonwhisking rate by the per-cell rank-sum test of fs-whisking-rate (Fig.\n    5d; the 23 increases and 3 decreases), readings O1 and O2. \"Typically\" is read as more than\n    half of the cells. Reproduced when more than half multiplex under every reading; not\n    reproduced otherwise. The same count for the 29 VPM units is reported.\n- id: exc-mainly-touch\n  statement: L4 excitatory neurons respond mostly to touch (0.3 +- 0.4 spikes per touch, n = 85)\n    and only weakly to whisker movement; their rate does not change significantly between\n    nonwhisking and whisking (0.4 to 0.6 spikes/s, P = 0.20).\n  source: Results, Dynamics of L4 fast-spiking interneurons, paragraph 3; Figure 5b,d,e\n  quote: Excitatory neurons responded mostly to touch (mean ± s.d., 0.3 ± 0.4 spikes per touch;\n    median, 0.1 spikes per touch; n = 85 neurons; Fig. 5b,d) and showed weak response to whisker\n    movement ... (nonwhisking ... 0.4 ± 0.6 spikes per s; median, 0.1 spikes per s; whisking ...\n    0.6 ± 0.9 spikes per s; median, 0.2 spikes per s; n = 85, P = 0.20; Fig. 5d,e). In contrast to\n    VPM and L4 FS neurons, L4 excitatory neurons responded selectively to touch\n  statistics:\n  - about: nonwhisking against whisking spike rate over L4 excitatory neurons\n    p: 0.2\n    n: 85 neurons\n  expected:\n  - quantity: mean L4 E spikes per touch\n    value: 0.3\n    tolerance: 0.043\n  - quantity: mean L4 E nonwhisking rate\n    value: 0.4\n    tolerance: 0.065\n    unit: spikes/s\n  - quantity: mean L4 E whisking rate\n    value: 0.6\n    tolerance: 0.098\n    unit: spikes/s\n  criterion: >-\n    The 85 control L4 E neurons (37 whole-cell, 48 cell-attached; control trials only for cells\n    in eNpHR mice). Spikes per touch by the cortical Fig. 5 definition; rates in nonwhisking\n    and whisking periods (header, Measures). The absence part is judged on the paper's test, a\n    paired test of per-neuron nonwhisking against whisking rate; the test is not named, and the\n    Methods' paired test is the Wilcoxon signed-rank test, at 0.05. Reproduced when that test\n    gives p >= 0.05 and the three values are within tolerance; partially reproduced when the\n    test gives p >= 0.05 and a value is not within tolerance; not reproduced when the test finds\n    a difference. The size of the whisking change is reported either way, with filter readings\n    O1 shown (the absence test is judged on each; a split is reported as a deviation).\n- id: vpm-photoinhibition\n  statement: Photoactivating TRN axons in VPM of VGAT-ChR2-EYFP mice reduces thalamic activity\n    to 17% of control.\n  source: Results, Inhibition is driven by thalamus, paragraph 1; Figure 6b,c\n  quote: Photoactivation of TRN axons reduced activity in the thalamus (to 17% of control, P = 3 ×\n    10−4, n = 17 multiunit recordings; Fig. 6b,c).\n  statistics:\n  - test: Wilcoxon signed-rank test (paired design; the paper does not name the test)\n    p: 3.0e-4\n    n: 17 multiunit recordings\n  expected:\n    quantity: VPM multiunit rate with light as a fraction of control\n    value: 0.17\n    tolerance: 0.017\n  criterion: >-\n    The 17 VPM multiunit recordings made by pipette during behavior. Rate over all time inside\n    the light (Supplementary Fig. 9i, no behavioral epochs for multiunits) against control,\n    windows O5 (a) and (b), fractions O6 (a) and (b), laser powers O7 (a) and (b). Reproduced\n    when a Wilcoxon signed-rank test of per-recording rates gives p < 0.05 with light lower and\n    the fraction is within tolerance under a reading; partially reproduced when only the test\n    holds.\n- id: exc-thalamus-photoinhibition\n  statement: Thalamic photoinhibition hyperpolarizes L4 excitatory neurons and reduces their Vm\n    fluctuations, with an onset latency of 4.2 ms, longer than the 2.8 ms latency of direct\n    cortical GABAergic activation.\n  source: Results, Inhibition is driven by thalamus, paragraph 1; Supplementary Figure 9a-f\n  quote: photoinhibition of thalamus hyperpolarized excitatory neurons and reduced the amplitudes of\n    their membrane voltage fluctuations (Supplementary Fig. 9a–e). Onset latency of Vm\n    hyperpolarization induced by thalamus inactivation was 4.2 ms. This was longer than the 2.8-ms\n    latency measured with direct cortical GABAergic activation (Supplementary Fig. 9f)\n  expected:\n  - quantity: onset latency of Vm hyperpolarization with thalamic photoinhibition\n    value: 4.2\n    tolerance: 0.42\n    unit: ms\n  - quantity: onset latency of Vm hyperpolarization with direct cortical light\n    value: 2.8\n    tolerance: 0.28\n    unit: ms\n  criterion: >-\n    The 12 whole-cell L4 E neurons with VPM light (Supplementary Fig. 9c) and the 7 with direct\n    cortical light in VGAT-ChR2 mice (Supplementary Fig. 9f). Resting Vm and Vm variance\n    (high-pass 10 Hz) from Vm outside touch, light against control (Supplementary Fig. 9d,e),\n    windows O5. The latency rule is not given; readings (a) the dVm/dt rule of the touch latency\n    applied to the laser-onset-aligned average (3 x s.d. of dVm/dt before onset; Online\n    Methods); (b) the first time the grand average Vm falls 3 s.d. below its pre-onset mean.\n    The paper reports no test for 9d,e. Reproduced when Vm is lower and variance lower with\n    light in most of the 12 neurons and both latencies are within tolerance with the thalamic\n    one longer; partially reproduced when the Vm and variance parts hold and a latency does not.\n- id: thalamus-drives-fs\n  statement: Photoinhibiting the thalamus reduces the spike rates of L4 FS interneurons during\n    nonwhisking (to 4% of control), whisking (to 13%) and touch (to 32%), so FS interneurons are\n    driven by thalamic input.\n  source: Results, Inhibition is driven by thalamus, paragraph 2; Figure 6d,e; Supplementary\n    Figure 9j\n  quote: Photoinhibition reduced spike rates in FS interneurons during nonwhisking (to 4% of control\n    ... and whisking epochs (to 13% of control ... as well as in response to touch (to 32% of\n    control ... FS interneurons were thus driven by input from the thalamus.\n  statistics:\n  - about: nonwhisking spike rate with and without thalamic photoinhibition\n    p: 5.0e-4\n    n: 13 neurons\n  - about: whisking spike rate with and without thalamic photoinhibition\n    p: 6.0e-5\n    n: 15 neurons\n  - about: touch response with and without thalamic photoinhibition\n    p: 1.0e-4\n    n: 14 neurons\n  expected:\n  - quantity: FS nonwhisking rate with light as a fraction of control\n    value: 0.04\n    tolerance: 0.004\n  - quantity: FS whisking rate with light as a fraction of control\n    value: 0.13\n    tolerance: 0.013\n  - quantity: FS spikes per touch with light as a fraction of control\n    value: 0.32\n    tolerance: 0.032\n  criterion: >-\n    The L4 FS cells (ChR2-tagged, thin spikes; Fig. 6e legend) recorded with VPM light.\n    Nonwhisking and whisking rates, and spikes per touch (Fig. 6e axis; Fig. 5 definition), in\n    light trials inside the light against control, windows O5, fractions O6 (Fig. 6e plots\n    population means, which favours O6 a), laser powers O7. Tests are Wilcoxon signed-rank\n    (paired; not named in the Results). Reproduced when all three tests give p < 0.05 with\n    light lower and the fractions are within tolerance under a reading; partially reproduced\n    when the three tests hold and a fraction is not within tolerance; not reproduced when a\n    test fails.\n- id: rabies-vpm-input\n  statement: Monosynaptic rabies tracing from L4 PV interneurons labels thalamic neurons mostly in\n    VPM (>90%) and few in POM (<10%).\n  source: Results, Inhibition is driven by thalamus, paragraph 3; Supplementary Figure 10\n  quote: The vast majority of trans-synaptically labeled thalamic neurons were in VPM (>90%), with\n    only a small minority in POM (<10%; Supplementary Fig. 10).\n  criterion: >-\n    Counts of GFP-labeled neurons in VPM and POM from the tracing sections (Online Methods,\n    Virus injection). Reproduced when VPM holds more than 90% of the labeled thalamic neurons.\n    The paper's histology is not described as part of the recordings; the author reports\n    whether the dandiset holds it.\n- id: ion-cut-exc-no-touch\n  statement: After infraorbital nerve transection, L4 excitatory neurons do not depolarize after\n    touch.\n  source: Results, Inhibition is driven by sensory input, paragraph 2; Figure 7b\n  quote: As expected, L4 excitatory neurons did not depolarize after touch (Fig. 7b).\n  criterion: >-\n    The L4 E neurons recorded whole-cell in ION-cut mice (8 in Fig. 7b). The paper reports no\n    test; the claim is one of absence. Touch PSP amplitude as in exc-vm-touch-whisking, per\n    neuron, tested against zero by the Methods' paired test (Wilcoxon signed-rank on per-neuron\n    mean post-touch against pre-touch Vm) at 0.05. Reproduced when the test finds no\n    depolarization; not reproduced when it finds one. Touch counts per neuron and the mean\n    amplitude are reported, with the 15 matched control neurons as comparison.\n- id: ion-cut-exc-whisking\n  statement: After ION transection, whisking-evoked depolarization of L4 excitatory neurons is\n    reduced (0.62 +- 0.50 mV, n = 9) relative to control neurons with matched resting potential\n    (1.54 +- 0.79 mV, n = 15).\n  source: Results, Inhibition is driven by sensory input, paragraph 2; Figure 7c,d\n  quote: >-\n    Depolarizations in response to whisker movement were reduced (ION cut: mean ± s.d., 0.62 ± 0.50\n    mV, n = 9 neurons versus Control with matched resting potential: mean ± s.d., 1.54 ± 0.79 mV,\n    n = 15 neurons; P = 0.005, Wilcoxon rank-sum test; Fig. 7c,d)\n  statistics:\n  - test: Wilcoxon rank-sum test\n    p: 0.005\n    n: 9 ION-cut and 15 control neurons\n  expected:\n  - quantity: mean whisking depolarization, ION cut\n    value: 0.62\n    tolerance: 0.167\n    unit: mV\n  - quantity: mean whisking depolarization, matched controls\n    value: 1.54\n    tolerance: 0.204\n    unit: mV\n  depends_on:\n  - exc-vm-touch-whisking\n  criterion: >-\n    Whisking depolarization as in exc-vm-touch-whisking (Supplementary Fig. 4 windows). The\n    matching rule for the 15 controls is not given; readings (a) the control whole-cell E neurons\n    whose resting Vm (O4) lies within the range of the 9 ION-cut neurons; (b) the 15 control\n    neurons nearest in resting Vm to the ION-cut median. Reproduced when a Wilcoxon rank-sum\n    test gives p < 0.05 with ION-cut lower and both means are within tolerance under a reading;\n    partially reproduced when only the test holds.\n- id: ion-cut-exc-phase\n  statement: After ION transection, phase-locking of L4 excitatory Vm to whisker movement is\n    abolished (coupling 0.12 +- 0.04 mV against 0.38 +- 0.31 mV in controls).\n  source: Results, Inhibition is driven by sensory input, paragraph 2; Figure 7e\n  quote: phase-locking of membrane potential to whisker movement was abolished (ION cut, 0.12 ± 0.04\n    mV versus Control, 0.38 ± 0.31 mV; P = 0.005; Fig. 7e)\n  statistics:\n  - p: 0.005\n    n: 9 ION-cut and 15 control neurons (the n of the same sentence)\n  expected:\n  - quantity: mean Vm phase coupling, ION cut\n    value: 0.12\n    tolerance: 0.013\n    unit: mV\n  - quantity: mean Vm phase coupling, controls\n    value: 0.38\n    tolerance: 0.08\n    unit: mV\n  depends_on:\n  - ion-cut-exc-whisking\n  criterion: >-\n    Vm (spikes removed) in 12 phase bins during whisking epochs, fitted with a sinusoid;\n    coupling strength is half its peak-to-trough (Online Methods), filters O1. Same ION-cut and\n    matched control neurons as ion-cut-exc-whisking, both readings; unpaired, so a Wilcoxon\n    rank-sum test (Online Methods). Reproduced when the test gives p < 0.05 with ION-cut lower\n    and both means are within tolerance; partially reproduced when only the test holds.\n- id: ion-cut-fs-no-touch\n  statement: After ION transection, touch does not evoke spikes in L4 FS interneurons.\n  source: Results, Inhibition is driven by sensory input, paragraph 3; Figure 7g\n  quote: Touch did not evoke spikes in FS interneurons (Fig. 7g).\n  criterion: >-\n    The 10 L4 FS cells (ChR2-tagged, thin spikes) recorded in ION-cut mice. A claim of absence\n    with no test in the paper; judged by the Methods' paired test (Wilcoxon signed-rank) of\n    per-cell spikes 0 to 50 ms after against 2 x spikes 0 to 25 ms before touch (the Fig. 5\n    spikes-per-touch terms) at 0.05. Reproduced when no increase is found; not reproduced when\n    one is. The mean spikes per touch is reported against the control FS value (1.9).\n- id: sensory-input-drives-fs\n  statement: After ION transection, the whisking-related activation of L4 FS interneurons is\n    absent in most cells (P = 0.80, n = 10), so their movement-related modulation is reafference\n    driven by sensory input.\n  source: Results, Inhibition is driven by sensory input, paragraph 3; Figure 7h,i\n  quote: In addition, whisking-related activation of FS interneurons was also absent in most cells\n    (P = 0.80, n = 10 neurons; Fig. 7h,i). ... These data show that excitation of L4 excitatory\n    neurons and L4 FS neurons is dominated by sensory input. Modulation correlated with whisker\n    movement in L4 FS neurons constitutes reafference.\n  statistics:\n  - about: nonwhisking against whisking spike rate of FS cells after ION cut\n    p: 0.8\n    n: 10 neurons\n  depends_on:\n  - fs-whisking-rate\n  criterion: >-\n    The 10 L4 FS cells in ION-cut mice; nonwhisking and whisking rates as in fs-whisking-rate.\n    A claim of absence judged on the paper's test, a paired test (not named; Wilcoxon\n    signed-rank per the Methods) of per-cell nonwhisking against whisking rate at 0.05.\n    Reproduced when it finds no difference; not reproduced when it finds one. The per-cell\n    rank-sum results (how many cells still increase, readings O2) and the size of the change\n    are reported.\n- id: ion-cut-fs-phase\n  statement: After ION transection, phase-locking of L4 FS spikes to whisker movement is reduced\n    but not entirely abolished.\n  source: Results, Inhibition is driven by sensory input, paragraph 3; Supplementary Figure 12\n  quote: Phase-locking of spikes to whisker movement was reduced but not entirely abolished\n    (Supplementary Fig. 12).\n  depends_on:\n  - fs-whisking-phase\n  criterion: >-\n    r2 of the phase fit (sinusoid, or sinusoid plus double frequency as in Supplementary Fig.\n    7g; 12 bins; filters O1) for the 10 ION-cut FS cells and the control FS cells; Supplementary\n    Fig. 12b compares the two distributions by their medians. The paper reports no test.\n    Reproduced when the ION-cut median r2 is below the control median and at least one ION-cut\n    cell has r2 > 0.25 (Supplementary Fig. 12a); not reproduced otherwise.\n- id: pv-enphr-suppression\n  statement: Yellow light in PV-IRES-Cre mice expressing eNpHR3.0 strongly inhibits most L4 PV\n    interneurons (3 of 4); their rate falls 3 ms after laser onset and L4 excitatory activity\n    rises 2 ms later.\n  source: Results, Layer 4 FS interneurons suppress reafference in L4, paragraph 5; Supplementary\n    Figure 13a,c\n  quote: First, the spike rate of L4 PV interneurons decreased 3 ms after laser onset, and activity\n    in L4 neurons increased only 2 ms later (Supplementary Fig. 13c) ... Four L4 PV interneurons\n    recorded. 3 out of 4 are strongly inhibited by eNpHR stimulation.\n  expected:\n  - quantity: L4 PV interneurons strongly inhibited by light\n    value: 3\n    unit: of 4\n  - quantity: latency of PV rate decrease after laser onset\n    value: 3\n    tolerance: 0.3\n    unit: ms\n  - quantity: further delay to the rise of L4 excitatory activity\n    value: 2\n    tolerance: 0.2\n    unit: ms\n  criterion: >-\n    The 4 L4 PV cells and the excitatory cells of PV-IRES-Cre mice; rates in nonwhisking and\n    whisking periods with and without light (Supplementary Fig. 13a, 95% intervals). \"Strongly\n    inhibited\" is not defined; read as the light-trial rate below the lower bound of the\n    control 95% bootstrap interval in both periods. Grand averages aligned to laser onset\n    (Supplementary Fig. 13c); the latency rule is not given, readings as in\n    exc-thalamus-photoinhibition, applied to the PSTH (1 ms bins). Reproduced when 3 of 4 PV\n    cells are inhibited and the latencies are within tolerance (1 ms bins limit them to whole\n    ms); partially reproduced when only the PV count holds.\n- id: fs-suppress-movement-spiking\n  statement: Partially suppressing PV (FS) interneurons increases the spike rate of L4 excitatory\n    neurons during nonwhisking (0.6 to 1.6 spikes/s) and whisking (0.8 to 2.7 spikes/s).\n  source: Results, Layer 4 FS interneurons suppress reafference in L4, paragraph 1; Figure 8b-d;\n    Supplementary Figure 13b\n  quote: Partially suppressing PV (FS) interneurons changed the responses of excitatory neurons\n    (Fig. 8b–e; P = 1 × 10−6, Kruskal-Wallis test). L4 excitatory neurons increased their spike rate\n    during both nonwhisking periods (from 0.6 ± 0.1 spikes per s to 1.6 ± 0.3 spikes per s; mean ±\n    s.e.m., n = 40 neurons, P = 6 × 10−5) and whisking periods(from 0.8 ± 0.2 spikes per s to 2.7 ±\n    0.5 spikes per s, P = 2 × 10−6\n  statistics:\n  - about: rates of excitatory neurons across conditions\n    test: Kruskal-Wallis test\n    p: 1.0e-6\n    n: 40 neurons\n  - about: nonwhisking rate, control against eNpHR\n    p: 6.0e-5\n    n: 40 neurons\n  - about: whisking rate, control against eNpHR\n    p: 2.0e-6\n    n: 40 neurons\n  expected:\n  - quantity: nonwhisking rate, control\n    value: 0.6\n    tolerance: 0.1\n    unit: spikes/s\n  - quantity: nonwhisking rate, eNpHR\n    value: 1.6\n    tolerance: 0.3\n    unit: spikes/s\n  - quantity: whisking rate, control\n    value: 0.8\n    tolerance: 0.2\n    unit: spikes/s\n  - quantity: whisking rate, eNpHR\n    value: 2.7\n    tolerance: 0.5\n    unit: spikes/s\n  criterion: >-\n    The putative excitatory L4 neurons of PV-IRES-Cre eNpHR mice with light trials (40 in the\n    paper; the selection beyond the count is not given). Nonwhisking and whisking rates in light\n    trials inside the light against control, windows O5, filters O1. Kruskal-Wallis over the\n    four groups (nonwhisking and whisking, control and light; Fig. 8b-e), and Wilcoxon\n    signed-rank tests per period (paired; not named in the Results). Reproduced when both\n    paired tests give p < 0.05 with light higher and the four rates are within tolerance;\n    partially reproduced when the tests hold and a rate is not within tolerance; not reproduced\n    when a paired test fails.\n- id: fs-enhance-touch-selectivity\n  statement: With PV interneurons suppressed, L4 excitatory neurons become driven by whisker\n    movement (whisking rate above nonwhisking, P = 0.02), while in control trials they are not\n    (P = 0.55); their selectivity for touch is normally maintained in part by FS interneurons.\n  source: Results, Layer 4 FS interneurons suppress reafference in L4, paragraph 1; Figure 8d\n  quote: L4 excitatory neurons were instead driven by whisker movements (P = 0.02, Fig. 8d),\n    implying that their selectivity for touch was normally maintained in part by FS interneurons.\n  statistics:\n  - about: nonwhisking against whisking rate in eNpHR trials (Fig. 8d)\n    p: 0.02\n    n: 40 neurons\n  - about: nonwhisking against whisking rate in control trials (Fig. 8d, printed in the figure)\n    p: 0.55\n    n: 40 neurons\n  depends_on:\n  - fs-suppress-movement-spiking\n  criterion: >-\n    Same neurons, windows and rates as fs-suppress-movement-spiking. Fig. 8d prints P = 0.55\n    for nonwhisking against whisking in control and P = 0.02 with eNpHR; the paired test is the\n    Wilcoxon signed-rank test (Online Methods). Readings O5 and O1. Reproduced when the test in\n    light trials gives p < 0.05 with whisking higher and the test in control trials gives p >=\n    0.05; partially reproduced when the light test holds and the control test also finds a\n    difference; not reproduced when the light test fails.\n- id: exc-touch-spikes-enphr\n  statement: PV interneuron suppression does not change mean touch-evoked spiking of L4\n    excitatory neurons significantly (0.27 to 0.32 spikes per touch, P = 0.09); its effect is\n    heterogeneous, with weakly responding neurons responding more and strongly responding\n    neurons unchanged or less.\n  source: Results, Layer 4 FS interneurons suppress reafference in L4, paragraph 2; Figure 8e;\n    Supplementary Figure 13b\n  quote: PV interneuron suppression also modulated touch-evoked spiking in L4 excitatory neurons,\n    but they did so in a heterogeneous manner (mean ± s.e.m., from 0.27 ± 0.06 spikes per touch to\n    0.32 ± 0.06 spikes per touch, n = 40 neurons, P = 0.09, Wilcoxon signed-rank test; Fig. 8e and\n    Supplementary Fig. 13). Neurons that responded weakly to touch tended to respond more strongly\n    with PV interneuron suppression.\n  statistics:\n  - test: Wilcoxon signed-rank test\n    p: 0.09\n    n: 40 neurons\n  expected:\n  - quantity: spikes per touch, control\n    value: 0.27\n    tolerance: 0.06\n  - quantity: spikes per touch, eNpHR\n    value: 0.32\n    tolerance: 0.06\n  depends_on:\n  - fs-suppress-movement-spiking\n  criterion: >-\n    Same 40 neurons. Spikes per touch by the Fig. 8e definition (4 to 20 ms after minus 0 to 16\n    ms before onset; intertouch interval at least 10 ms), light against control trials. The\n    absence of a mean change is judged on the paper's test, a Wilcoxon signed-rank test at\n    0.05. Reproduced when it gives p >= 0.05 and both means are within tolerance; partially\n    reproduced when p >= 0.05 and a mean is not within tolerance; not reproduced when it finds\n    a change. The heterogeneity is described, not tested, in the paper; the change against the\n    control value is shown per neuron (Fig. 8e) and reported.\n- id: auc-weak-strong\n  statement: Suppressing PV interneurons improves touch detection (AUC) for L4 excitatory neurons\n    with weak touch responses and diminishes it for neurons with robust touch responses.\n  source: Results, Layer 4 FS interneurons suppress reafference in L4, paragraph 3; Figure 8f,g\n  quote: Consistent with the heterogeneous changes in spikes per touch, suppression of PV\n    interneurons improved AUC for neurons with weak responses to touch and diminished AUC for\n    neurons with robust responses to touch (Fig. 8f,g).\n  depends_on:\n  - fs-suppress-movement-spiking\n  criterion: >-\n    Same 40 neurons. ROC per neuron and condition (Online Methods): per trial, spike counts in\n    250 ms before and after the first touch, or in the sample epoch for trials without touch;\n    touch and no-touch periods resampled 5,000 times; AUC from the threshold sweep of the count\n    difference. Which 250 ms windows of the sample epoch serve in no-touch trials is not given;\n    readings (a) two adjacent 250 ms windows at a random time in the sample epoch; (b) the 250\n    ms before and after the median first-touch time of touch trials. The touch-evoked rate is\n    the mean rate 0 to 250 ms after minus 0 to 250 ms before touch, control trials (Fig. 8g\n    legend). The paper gives no test; it groups neurons by the sign of the AUC change (Fig. 8h,\n    19 increased, 21 reduced). Reproduced when the neurons whose AUC rises have a lower mean\n    control touch-evoked rate than those whose AUC falls (as Fig. 8h, 3.4 against 7.3\n    spikes/s) under both readings; not reproduced otherwise.\n- id: auc-groups\n  statement: Neurons whose AUC rose with PV suppression gained touch-evoked spiking (3.4 to 8.7\n    spikes/s); neurons whose AUC fell kept their touch-evoked response (7.3 to 7.0 spikes/s) but\n    had higher baseline rates (0.9 to 2.6 spikes/s).\n  source: Results, Layer 4 FS interneurons suppress reafference in L4, paragraph 4; Figure 8h\n  quote: L4 excitatory neurons with increased AUCs showed a population increase in touch-evoked\n    responses on average (from 3.4 ± 0.8 spikes per s to 8.7 ± 1.9 spikes per s, P = 0.0001).\n    Neurons with reduced AUC showed unchanged touchevoked responses as a population (from 7.3 ±\n    1.5 spikes per s to 7.0 ± 1.4 spikes per s, P = 0.98, average 0–250 ms after touch onset) ...\n    but elevated baseline spike rates (from 0.9 ± 0.2 spikes per s to 2.6 ± 0.6 spikes per s, mean\n    ± s.e.m., P = 0.0002; Fig. 8f–h).\n  statistics:\n  - about: touch-evoked rate, control against eNpHR, neurons with increased AUC\n    p: 0.0001\n    n: 19 neurons (Fig. 8h)\n  - about: touch-evoked rate, control against eNpHR, neurons with reduced AUC\n    p: 0.98\n    n: 21 neurons (Fig. 8h)\n  - about: baseline rate, control against eNpHR, neurons with reduced AUC\n    p: 0.0002\n    n: 21 neurons (Fig. 8h)\n  expected:\n  - quantity: touch-evoked rate, increased-AUC group, control\n    value: 3.4\n    tolerance: 0.8\n    unit: spikes/s\n  - quantity: touch-evoked rate, increased-AUC group, eNpHR\n    value: 8.7\n    tolerance: 1.9\n    unit: spikes/s\n  - quantity: touch-evoked rate, reduced-AUC group, control\n    value: 7.3\n    tolerance: 1.5\n    unit: spikes/s\n  - quantity: touch-evoked rate, reduced-AUC group, eNpHR\n    value: 7.0\n    tolerance: 1.4\n    unit: spikes/s\n  - quantity: baseline rate, reduced-AUC group, control\n    value: 0.9\n    tolerance: 0.2\n    unit: spikes/s\n  - quantity: baseline rate, reduced-AUC group, eNpHR\n    value: 2.6\n    tolerance: 0.6\n    unit: spikes/s\n  depends_on:\n  - auc-weak-strong\n  criterion: >-\n    Groups by the sign of the AUC change (auc-weak-strong, both readings). The touch-evoked\n    response is the mean rate 0 to 250 ms after touch onset (as the sentence says); the baseline\n    is the mean rate 0 to 250 ms before onset (Fig. 8g legend). Paired tests are Wilcoxon\n    signed-rank (Online Methods). Reproduced when the increased-AUC group's rise and the\n    reduced-AUC group's baseline rise give p < 0.05, the reduced-AUC group's touch response\n    shows no change at 0.05, and the means are within tolerance; partially reproduced when the\n    three tests hold and a mean is not within tolerance; not reproduced otherwise.\n- id: behavior-false-alarms\n  statement: With PV interneurons suppressed, most mice (6 of 8) are more likely to report touch\n    with the pole out of reach (false alarms on no-lick trials).\n  source: Results, Layer 4 FS interneurons suppress reafference in L4, paragraph 4;\n    Supplementary Figure 14b,c\n  quote: with PV interneuron suppressed, most mice (6 of 8) were more likely to report touches with\n    the pole out of reach (Supplementary Fig. 14). ... In 8 mice tested, 6 showed a significant\n    decrease of performance during Nolick trials with PV interneuron inactivation\n  expected:\n    quantity: mice with a significant decrease of no-lick performance with light\n    value: 6\n    unit: of 8 mice\n  criterion: >-\n    For each of the 8 PV-IRES-Cre eNpHR mice, correct responses on no-lick (anterior pole)\n    trials with and without light, compared by a chi-squared test at p < 0.05 (Supplementary\n    Fig. 14c). Whether sessions of a mouse are pooled is not stated; readings (a) all of a\n    mouse's trials pooled; (b) per session, a mouse counting when any session is significant.\n    Reproduced when 6 of 8 mice show a significant decrease under a reading (5 to 7 partially\n    reproduced); not reproduced when fewer than 5 do.\n"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -i 's/Results, Layer 4 FS interneurons suppress reafference in L4, paragraph 5; Supplementary/Results, Layer 4 FS interneurons suppress reafference in L4, paragraph 7; Supplementary/; s/  source: Results, Layer 4 FS interneurons suppress reafference in L4, paragraph 4;$/  source: Results, Layer 4 FS interneurons suppress reafference in L4, paragraph 6;/' claims/000005/10.1038-nn.4412.yaml && grep -n "paragraph [467]" claims/000005/10.1038-nn.4412.yaml; python tools/claims_check.py claims/000005/10.1038-nn.4412.yaml paper/10.1038-nn.4412.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
f=claims/000005/10.1038-nn.4412.yaml; grep -n "—\|rather" $f; python3 - <<'EOF'
import re
lines=open('claims/000005/10.1038-nn.4412.yaml').read().split('\n')
blk=False
for i,l in enumerate(lines,1):
    if l.lstrip().startswith('#'): continue
    m=re.match(r'^(\s*)(- )?([a-z_]+): (.*)$',l)
    if m:
        blk = m.group(4).strip() in ('>-','|','>')
        rest=m.group(4)
        if not blk and ': ' in rest: print('key-line',i,l)
        continue
    if not blk and ': ' in l: print('cont',i,l)
EOF
```

```
(Bash completed with no output)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/000005/10.1038-nn.4412.yaml",
 "old_string": "  - test: Wilcoxon signed-rank test (paired design; the paper does not name the test)\n    p: 3.0e-4",
 "new_string": "  - p: 3.0e-4"
}
```

```
The file claims/000005/10.1038-nn.4412.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/000005/10.1038-nn.4412.yaml",
 "old_string": "    when a Wilcoxon signed-rank test of per-recording rates gives",
 "new_string": "    when a Wilcoxon signed-rank test of per-recording rates (paired; the paper does not name\n    the test, the Methods give this one for paired data) gives"
}
```

```
The file claims/000005/10.1038-nn.4412.yaml has been updated successfully.
```

**Agent calls Bash**

```bash
python tools/claims_check.py claims/000005/10.1038-nn.4412.yaml paper/10.1038-nn.4412.txt; git status --short
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
python3 -c "
import yaml;c=yaml.safe_load(open('claims/000005/10.1038-nn.4412.yaml'))['claims']
print(len(c),sum('quote' in x for x in c),sum('statistics' in x for x in c),sum(len(x.get('statistics',[])) for x in c),sum('criterion' in x for x in c),sum('expected' in x for x in c))"
```

```
31 31 13 20 31 20
```

**Agent**

I rewrote `claims/000005/10.1038-nn.4412.yaml` from the full text. The quote checker reports 0 problems: 31 claims, 31 quotes, 20 statistical values. Nothing is committed.

**Text read:** the version of record, with its Online Methods and its one supplement (Supplementary Figures 1–14 and Tables 1–2). The extracted text garbled a few things, so I rendered PDF pages for four of them: Supplementary Table 2, the FS waveform boundary in Supp. Fig. 6, the number of phase bins in Supp. Fig. 2d (12), and the P values printed in Fig. 8d (0.55 and 0.02).

**Code:** the paper's data and code link is CRCNS ssc-7 (doi:10.6080/K0T43R01). Its public pages list NWB data files and a data-description document. No analysis code is listed, and downloading needs an account, so I read no code. Every method in the criteria comes from the Methods, the figure legends or the supplement.

**Claims:**
- 31 claims, all with quotes and criteria; 20 have expected values; 13 have statistics (20 entries).
- The eight earlier ids are kept, each with a new criterion. The new criteria for exc-mainly-touch and fs-enhance-touch-selectivity use the paper's own tests: P = 0.20, and P = 0.02 against 0.55. The proxy cell types and the touch-selectivity index from the deprecated file are gone.
- 23 claims are new: VPM phase coupling, excitatory-neuron Vm, distance to threshold, effective reversal, inhibition timing, FS touch, FS Vm, FS whisking rate and FS phase, VPM photoinhibition, excitatory Vm under thalamic photoinhibition, rabies tracing, five nerve-cut claims, PV suppression, touch spikes under eNpHR, two AUC claims, and two behavior claims.
- The opening comment says what changed and why. It also notes that I read the deprecated file's comment, which reports some outcomes of the earlier attempt; no criterion was set from them.

**Details the paper leaves open, and the readings named for each:**
- **O1, band-pass filter direction:** zero-phase, or a single forward pass.
- **O2, samples for the per-cell rank-sum test:** rates per epoch, or per trial.
- **O3, spike threshold:** dV/dt more than 3 s.d. above its mean, or above 3 s.d.
- **O4, resting Vm:** mean or median of nonwhisking Vm.
- **O5, light comparison window:** control trials over the same span of trial time, or all control-trial time.
- **O6, "% of control":** ratio of population means, or median of per-cell ratios.
- **O7, laser powers:** all powers pooled, or the highest power only.
- **O8, latency derivative:** read as the unsmoothed 1-ms PSTH, since the text names no smoothing.
- **Claim-specific:**
  - Effective reversal: one fit per neuron, or one pooled fit.
  - Nerve-cut controls "with matched resting potential": controls within the nerve-cut cells' Vm range, or the 15 nearest in Vm.
  - Latency of the light effects: the dV/dt rule, or a 3 s.d. drop of the average.
  - "Strongly inhibited" PV cells: rate below the control 95% interval.
  - AUC windows on no-touch trials: random windows in the sample epoch, or windows at the median touch time.
  - Pooling for the per-mouse chi-squared test: per mouse, or per session.
- **Other gaps:**
  - The paper states no significance level. I used 0.05, since it calls P = 0.046 significant and P = 0.09 and 0.20 not.
  - Several P values are printed without a test named; I used the Wilcoxon test the Methods give for that design.
  - Which cells make up some counts is not stated: 40 of the 43 excitatory cells in PV-Cre mice, and 13 to 15 FS cells in the thalamic experiment.

**Missing or inconsistent in the paper:**
- The FS count is 26 in the Results and Methods but 25 in Supp. Fig. 7 and Table 2; both sets are to be reported.
- The FS waveform boundary is only drawn in Supp. Fig. 6, near 0.27 ms and a peak-to-trough ratio of 2.8; that is an approximate reading.
- No sentence gives the number of VPM cells with phase coupling. I read about 23 to 26 above r² = 0.25 from the Supp. Fig. 2e histogram.
- Whether the dandiset holds the rabies histology (rabies-vpm-input) is for the author to find.

## End of run

46 turns, 10 minutes, result: success.
