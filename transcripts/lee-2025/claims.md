# 001195 · claims · run 39817923469

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cat docs/protocol.md; ls claims/001453/ paper/ claims/001195 2>&1; ls tools
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cat claims/001453/*.yaml | head -150; ls paper; for f in paper/*.txt; do echo "== $f"; head -30 "$f"; wc "$f"; done
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.7554-elife.105955.txt",
 "limit": 700
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -n 150,400p claims/001453/*.yaml
```

```
data: with_labels
  depends_on:
  - stimulus-code-link
  criterion: For each fish, the mean of its median angular velocities for the rightward
    stimuli (right, forward right, backward right) minus the mean for the leftward stimuli
    (left, forward left, backward left). Reproduced when this difference is greater than zero
    in each species by a one-sided Wilcoxon signed-rank test at p < 0.05; partially reproduced
    when it holds in one species only. The per-stimulus species medians are reported as well.
- id: fig1h-zf-higher-angular-acceleration
  statement: Across directional stimuli ZF have higher angular acceleration than DC, and the
    distributions of the two species differ for every stimulus.
  source: Results, Optic flow induces angular matching and turns in DC, paragraph 2; Figure 1H
    (Kruskal-Wallis test with Bonferroni correction)
  quote: Across directional stimuli, ZF maintained higher angular acceleration than DC
  statistics:
  - test: Kruskal-Wallis test
    p: 0.05
    p_relation: "<"
    corrected: Bonferroni
  data: with_labels
[... 152 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "paper/10.7554-elife.105955.txt",
 "offset": 700,
 "limit": 750
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.7554-elife.105955.txt",
 "offset": 1450,
 "limit": 400
}
```

Result: not kept, because it reads the paper's text.

**Agent**

I've read the main text, Methods and figure supplements of the eLife reviewed preprint v2. Now checking the rest for the Figure 7 legend continuation, data and code availability.

**Agent calls Bash**

```bash
cd paper; grep -n -i -E "github|gitlab|zenodo|dandi|code avail|data avail|figshare|(J\) |\(K\)|\(M\) " 10.7554-elife.105955.txt | head -60; grep -n "with 2 cells having" -A 20 10.7554-elife.105955.txt | head -60
```

```
grep: Unmatched ( or \(
675:16 co-registered GH off cells and 18 GH on cells exhibited an excitatory response to social stimulus with 2 cells having the
676-
677-=== page 15 ===
678-Christopher R Lee et al., 2025 eLife. https://doi.org/10.7554/eLife.105955.2
679-15 of 52
680-did find a trend indicating stronger responses toward social stimuli compared to object stimuli in
681-the GH on condition compared to the GH off condition in mice expressing ChrimsonR (Figure
682-7J     ), but not TdTomato (Figure 7—figure supplement 1L     ) in DRNDAT neurons. Importantly, in
683-co-registered neurons, we found little overlap between CeA neurons excited by the social stimulus
684-in both GH on and GH off conditions (Figure 7I     ), suggesting that DRNDAT terminal stimulation
685-may recruit separate ensembles of CeA neurons to represent social stimuli. Considering the
686-variability in social preference behavior across mice and the diverse effects of photostimulation
687-depending on the mouse’s social history, we next considered the responses of CeA neurons to
688-social and object stimuli on an animal-by-animal basis. While we did not observe significant
689-changes in the proportion of excitatory or inhibitory responses to social or object stimuli across
690-the three conditions (Figure 7K-L     ), we did find a significant positive correlation between the
691-proportion of socially-excited CeA neurons and social preference in the GH on condition, but not
692-in the GH off or SI off conditions (Figure 7M     ). Importantly, we do not observe a correlation
693-between social preference and object-excited CeA neurons (Figure 7—figure supplement 1N     )
[... 2 more lines not kept]
```

**Agent calls Bash**

```bash
cd paper; grep -n -i -E "github|gitlab|zenodo|dandi|availab|figshare|co-registered|Figure 7|=== page" 10.7554-elife.105955.txt | sed -n '1,400p' | awk -F: '$1>1840'
```

```
1863:=== page 46 ===
1912:=== page 47 ===
1951:=== page 48 ===
1978:=== page 49 ===
2033:=== page 50 ===
2084:=== page 51 ===
2139:=== page 52 ===
```

**Agent calls Read**

```json
{
 "file_path": "paper/10.7554-elife.105955.txt",
 "offset": 1850,
 "limit": 340
}
```

Result: not kept, because it reads the paper's text.

**Agent**

The text file cuts off the Figure 7 legend after panel I, and it has no data or code availability section. I'll check the PDF for both.

**Agent calls Bash**

```bash
cd paper; python -c "
import fitz
d=fitz.open('10.7554-elife.105955.pdf'); print(d.page_count)
for i,p in enumerate(d):
    t=p.get_text()
    for k in ['github','GitHub','zenodo','Zenodo','DANDI','dandi','availab','Data avail','Code']:
        if k in t: print(i+1,k)
print(d[13].get_text()[-3000:])
"
```

```
Exit code 1
Traceback (most recent call last):
  File "<string>", line 2, in <module>
    import fitz
ModuleNotFoundError: No module named 'fitz'
```

**Agent calls Bash**

```bash
cd paper; which pdftotext pdftoppm; python -c "import pypdf" 2>&1; pdftotext -layout -f 14 -l 14 10.7554-elife.105955.pdf - | tail -40; pdftotext 10.7554-elife.105955.pdf - | grep -n -i -E "github|zenodo|dandi|availab|osf.io"
```

```
Traceback (most recent call last):
  File "<string>", line 1, in <module>
    import pypdf
ModuleNotFoundError: No module named 'pypdf'
/bin/bash: line 1: pdftotext: command not found
/bin/bash: line 1: pdftotext: command not found
```

**Agent calls Read**

```json
{
 "file_path": "paper/10.7554-elife.105955.pdf",
 "pages": "14"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd paper; pip list 2>/dev/null | grep -i -E "pdf|mupdf|poppler|pillow"; ls -la; python - <<'E'
import re,zlib
data=open('10.7554-elife.105955.pdf','rb').read()
print(len(data))
for m in re.finditer(rb'/URI\s*\(([^)]*)\)',data):
    print(m.group(1)[:150])
E
```

```
total 12336
drwxr-xr-x  3 runner runner     4096 Oct 22 16:56 .
drwxr-xr-x 19 runner runner     4096 Oct 22 16:56 ..
drwxr-xr-x  3 runner runner     4096 Oct 22 16:56 .claude
-rw-r--r--  1 runner runner  1105343 Oct 22 16:55 10.21203-rs.3.rs-1025403-v1.pdf
-rw-r--r--  1 runner runner   133304 Oct 22 16:55 10.21203-rs.3.rs-1025403-v1.txt
-rw-r--r--  1 runner runner 11189164 Oct 22 16:55 10.7554-elife.105955.pdf
-rw-r--r--  1 runner runner   184563 Oct 22 16:55 10.7554-elife.105955.txt
11189164
```

**Agent calls Bash**

```bash
cd $TMPDIR && pip install --quiet pymupdf 2>&1 | tail -2; python -c "import fitz; print(fitz.__doc__)"
```

```
Exit code 1
[notice] A new release of pip is available: 26.2.1 -> 26.2.2
[notice] To update, run: pip install --upgrade pip
Traceback (most recent call last):
  File "<string>", line 1, in <module>
    import fitz; print(fitz.__doc__)
    ^^^^^^^^^^^
ModuleNotFoundError: No module named 'fitz'
```

**Agent calls Bash**

```bash
cd $TMPDIR && pip install pymupdf 2>&1 | tail -3; python -m pip show pymupdf | head -3; which python
```

```
[notice] A new release of pip is available: 26.2.1 -> 26.2.2
[notice] To update, run: pip install --upgrade pip
WARNING: Package(s) not found: pymupdf
/opt/hostedtoolcache/Python/3.13.16/x64/bin/python
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && pip install --target $TMPDIR/pylib pymupdf 2>&1 | grep -v notice | tail -3; PYTHONPATH=$TMPDIR/pylib python -c "import fitz; print('ok')"
```

```
Successfully installed flatbuffers-25.12.19 networkx-3.7 numpy-2.5.4 onnxruntime-1.31.0 packaging-26.3 protobuf-7.36.2 psutil-7.2.2 pymupdf-2.0 pymupdf-layout-2.0 pymupdf4llm-2.0 pyyaml-6.0.3 tabulate-0.10.0

[0;93m2026-10-22 16:56:52.628900616 [W:onnxruntime:Default, device_discovery.cc:95 GetPciBusId] Skipping pci_bus_id for PCI path at "/sys/devices/LNXSYSTM:00/LNXSYBUS:00/ACPI0004:00/MSFT1000:00/5620e0c7-8062-4dce-aeb7-520c7ef76171" because filename "5620e0c7-8062-4dce-aeb7-520c7ef76171" did not match expected pattern of [0-9a-f]+:[0-9a-f]+:[0-9a-f]+[.][0-9a-f]+[m
/tmp/claude-1001/pylib/fitz/__init__.py:17: FutureWarning: The `fitz` API is deprecated and will be removed in future. Use `import pymupdf` instead.
  warnings.warn(
ok
Shell cwd was reset to
```

**Agent calls Bash**

```bash
PYTHONPATH=$TMPDIR/pylib python - 2>/dev/null <<'E'
import pymupdf
d=pymupdf.open('paper/10.7554-elife.105955.pdf'); print(d.page_count)
links=set()
for i,p in enumerate(d):
    for l in p.get_links():
        u=l.get('uri')
        if u and not 'doi.org/10' in u and 'scholar' not in u and 'pubmed' not in u.lower() and 'ncbi' not in u: links.add((i+1,u))
for x in sorted(links): print(x)
t=d[13].get_text()
print(t[-2500:])
E
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
PYTHONPATH=$TMPDIR/pylib python - 2>/dev/null <<'E'
import pymupdf,os
d=pymupdf.open('paper/10.7554-elife.105955.pdf')
for n in [12,14]:
    p=d[n-1]; print(n,p.rect)
    p.get_pixmap(dpi=110).save(os.environ['TMPDIR']+f'/p{n}.png')
E
ls $TMPDIR/*.png
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/p14.png"
}
```

Result: no output.

**Agent calls Bash**

```bash
curl -s https://api.dandiarchive.org/api/dandisets/001195/ | python -c "import json,sys; d=json.load(sys.stdin); print(json.dumps(d,indent=1)[:1500])"; curl -s https://api.dandiarchive.org/api/dandisets/001195/versions/draft/info/ | python -c "
import json,sys; d=json.load(sys.stdin); m=d['metadata']; print(m['name']); print(m.get('description')); print(m.get('relatedResource')); print(m.get('assetsSummary',{}).get('variableMeasured'), m.get('assetsSummary',{}).get('approach'), m.get('assetsSummary',{}).get('numberOfSubjects'))"
```

Result: the fetched text is not kept.

**Agent**

The dandiset holds the Figure 6 ex vivo patch-clamp recordings and the Figure 7 CeA calcium imaging with behaviour videos. Next I'll read the checker and the schema.

**Agent calls Bash**

```bash
sed -n 1,80p tools/claims_check.py; ls docs; grep -rn "schema_version\|data:\|kind:" docs/*.md | head -30
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

[... 83 more lines not kept]
```

**Agent calls Bash**

```bash
cat schemas/claims.schema.json | head -200; ls docs/agents; ls claims | head; ls claims/*/ | head -40
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
[... 242 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 200,320p schemas/claims.schema.json; cat docs/agents/claims.md
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
[... 116 more lines not kept]
```

**Agent calls Bash**

```bash
grep -n -i -E "cluster|93%|62%|n ?= ?(19|36|48|20|17|5)\b|late-firing|EPSP|IEI|inter-?event|github|code avail|data avail" paper/10.21203-rs.3.rs-1025403-v1.txt | head -80
```

Result: not kept, because it reads the paper's text.

**Agent**

The preprint's ephys Methods match the eLife text. It adds one detail: the resting-potential cells came from 19 mice. Now I'll read the Figure 6 panels for the response proportions.

**Agent calls Bash**

```bash
PYTHONPATH=$TMPDIR/pylib python - 2>/dev/null <<'E'
import pymupdf,os
d=pymupdf.open('paper/10.7554-elife.105955.pdf')
p=d[11]
r=p.rect
p.get_pixmap(dpi=200,clip=pymupdf.Rect(0,0,r.width,r.height*0.55)).save(os.environ['TMPDIR']+'/p12a.png')
p=d[13]
p.get_pixmap(dpi=200,clip=pymupdf.Rect(0,r.height*0.28,r.width,r.height*0.62)).save(os.environ['TMPDIR']+'/p14b.png')
E
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/p12a.png"
}
```

Result: not kept, because it reads the paper's text.

Result: no output.

**Agent calls Bash**

```bash
PYTHONPATH=$TMPDIR/pylib python - 2>/dev/null <<'E'
import pymupdf,os
d=pymupdf.open('paper/10.7554-elife.105955.pdf')
for pn in [12,14]:
    for img in d[pn-1].get_images(full=True):
        x=img[0]; pix=pymupdf.Pixmap(d,x); print(pn,x,pix.width,pix.height)
        if pix.n>4: pix=pymupdf.Pixmap(pymupdf.csRGB,pix)
        pix.save(os.environ['TMPDIR']+f'/img{pn}_{x}.png')
E
ls -la $TMPDIR/img*
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
PYTHONPATH=$TMPDIR/pylib python - 2>/dev/null <<'E'
import pymupdf,os
T=os.environ['TMPDIR']
pix=pymupdf.Pixmap(T+'/img12_157.png')
W,H=pix.width,pix.height
def crop(x0,y0,x1,y1,name):
    doc=pymupdf.open(); 
    src=pymupdf.open(T+'/img12_157.png')
    page=src[0]; r=page.rect
    p=page.get_pixmap(clip=pymupdf.Rect(r.width*x0,r.height*y0,r.width*x1,r.height*y1),matrix=pymupdf.Matrix(1,1))
    p.save(T+'/'+name)
crop(0,0.15,1,0.36,'f6dgi.png')
crop(0,0.70,1,1,'f6nq.png')
E
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/f6dgi.png"
}
```

```
(Bash completed with no output)
```

Result: no output.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/f6nq.png"
}
```

Result: no output.

**Agent calls Bash**

```bash
PYTHONPATH=$TMPDIR/pylib python - 2>/dev/null <<'E'
import pymupdf,os
T=os.environ['TMPDIR']
src=pymupdf.open(T+'/img12_157.png'); page=src[0]; r=page.rect
page.get_pixmap(clip=pymupdf.Rect(0,r.height*0.36,r.width,r.height*0.56)).save(T+'/f6jk.png')
src=pymupdf.open(T+'/img14_194.png'); page=src[0]; r=page.rect
page.get_pixmap(clip=pymupdf.Rect(0,r.height*0.55,r.width,r.height*1)).save(T+'/f7gm.png')
E
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/f6jk.png"
}
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/f7gm.png"
}
```

```
(Bash completed with no output)
```

Result: no output.

Result: no output.

**Agent calls Write**

```json
{
 "file_path": "claims/001195/10.7554-elife.105955.yaml",
 "content": "# Claims for Lee, Matthews, Lemieux et al. (2025), \"Separable Dorsal Raphe Dopamine Projections\n# Mimic the Facets of a Loneliness-like State\", eLife doi:10.7554/eLife.105955, on dandiset 001195.\n# Written by an agent (model \"claude-opus-5-5\", Claude Code in GitHub Actions), 2026-10-22, protocol\n# as stated in docs/protocol.md (version pilot-10).\n#\n# Text read: the eLife reviewed preprint, version 2 (8 July 2025), from paper/10.7554-elife.105955.txt\n# (a PDF supplied by a person, extracted with PyMuPDF), with its Methods, figure legends and all figure\n# supplements. The PDF was opened for Figures 6 and 7 only. The legend of Figure 7 runs off the page in\n# the PDF itself and stops inside panel I; panels J to M have no legend, so their numbers (the\n# percentages of Figure 7J and r = 0.679, p = 0.045 in Figure 7M) were read from the figure image. The\n# eLife source data files listed under each figure are not in paper/, and the supplied text has no\n# data or code availability statement. The paper links no analysis code, so no code was read and\n# every method detail below comes from the Methods, the legends and the figure supplements. The\n# earlier Research Square preprint (doi:10.21203/rs.3.rs-1025403/v1), which the dandiset says used\n# the same patch-clamp data, was checked for the ex vivo Methods only: they match the eLife text, and\n# it adds that the cells recorded at rest came from 19 mice.\n#\n# The dandiset (title and description on DANDI) holds in vivo calcium imaging with behaviour videos\n# and ex vivo patch-clamp recordings, the data of Figure 6, Figure 6 supplement 1, Figure 7 and\n# Figure 7 supplements 1 and 2. The behavioural optogenetics (Figures 2 to 4 and 8), the tracing\n# (Figure 1) and the RNAscope (Figure 5) are covered below because they are the paper's main findings.\n#\n# Data the paper used, as it reports them:\n# - Ex vivo patch clamp (Figure 6). Male DAT::Cre mice with ChR2 (AAV5-DIO-ChR2-eYFP) in the DRN,\n#   at least 8 weeks of expression; whole-cell current clamp in coronal slices of the BNST, CeA and\n#   BLP, in the region with eYFP terminals; 3 kHz filter, 10 kHz sampling. Light, 470 nm, 8 pulses of\n#   5 ms at 30 Hz every 30 s. At rest, BNST n = 19, CeA n = 36, BLP n = 48 cells; with current\n#   injected to make the cell fire, BNST n = 5, CeA n = 20, BLP n = 17. Baseline properties came from\n#   a 5 mV, 250 ms hyperpolarizing step in voltage clamp at -70 mV (capacitance, membrane resistance)\n#   and from 1 s current steps from -120 to 260 pA in 20 pA increments. Clustered cells: CeA 26 and\n#   BLP 27 (from the t-test degrees of freedom, t24 and t25, in Figure 6 supplement 1H-I). A few cells\n#   were recorded with TTX/4AP (EPSP n = 8, IPSP n = 3).\n# - Ex vivo ChrimsonR validation (Figure 7 supplement 1B-I). DAT::Cre mice with ChrimsonR in the\n#   DRN; CeA cells stimulated with 635 nm (10 mW) or 470 nm (0.3 and 0.2 mW) light, and with 635 nm\n#   light during constant 470 nm light; 9 and 12 cells (from F2,16 and t11).\n# - In vivo imaging (Figure 7). DAT::Cre mice, GCaMP7f in the CeA, ChrimsonR (or TdTomato in\n#   controls) in the DRN, GRIN lens over the CeA, nVoke microscope at 20 frames/s. Three-chamber\n#   sessions of 5 min habituation and 10 min test with a juvenile mouse under one cup and an object\n#   under the other, in three conditions per mouse: group-housed without light (GH off), group-housed\n#   with 620 nm light (8 pulses of 5 ms at 30 Hz every 1 s, 10 mW; GH on), order counterbalanced,\n#   and 2-3 weeks later after 24 h of isolation without light (SI off). ChrimsonR cells: GH off 429,\n#   GH on 441, SI off 484; the legend says N = 15 mice per condition, Figure 7E says N = 12 ChrimsonR\n#   mice, and TdTomato controls are N = 2 (39, 61 and 76 cells). 202 cells were co-registered\n#   between GH off and GH on. Measured variables: CNMF-E traces per cell, SLEAP pose (15 keypoints)\n#   from the behaviour video, cup interactions derived from it, time in the social and object sides.\n# - Behaviour with optogenetics (Figures 2-4, 8, supplements). Male DAT::Cre mice, ChR2, NpHR or\n#   eYFP in the DRN, fibres over the BNST, CeA or BLP; tube test, RTPP, OFT, EPM, three-chamber,\n#   juvenile intruder, ICSS. Group sizes are given in each claim.\n#\n# Method details the paper leaves open are named in the criteria with the readings its text allows.\n# The SLEAP model (774 labelled frames) and the custom MATLAB code for passive properties (Q-method,\n# by P. Namburi) are described but not published with the paper.\nschema_version: 2\ndataset:\n  archive: dandi\n  id: \"001195\"\npaper: doi:10.7554/elife.105955\nclaims:\n\n# ---------------------------------------------------------------- Figure 6, ex vivo patch clamp\n- id: fig6df-epsp-ipsp-at-rest\n  statement: At the resting membrane potential, photostimulation of DRN-DAT terminals evoked both\n    excitatory and inhibitory post-synaptic potentials in downstream cells of the BNST, CeA and BLP\n    (19, 36 and 48 cells recorded).\n  source: Results, DRNDAT input has divergent effects on downstream cellular excitability, paragraph\n    2; Figure 6D-F\n  quote: Optical stimulation at the resting membrane potential evoked both excitatory and inhibitory\n    post-synaptic potentials (EPSPs and IPSPs) in downstream cells\n  expected:\n  - quantity: BNST cells recorded at rest\n    value: 19\n    tolerance: 0\n    unit: cells\n  - quantity: CeA cells recorded at rest\n    value: 36\n    tolerance: 0\n    unit: cells\n  - quantity: BLP cells recorded at rest\n    value: 48\n    tolerance: 0\n    unit: cells\n  criterion: Counts are compared exactly (tolerance 0) because they are cell counts the dataset\n    either holds or not; a count that differs is reported, and the claim is then judged on the\n    cells present. Per cell, the average of the light sweeps at rest (Methods, Ex vivo\n    electrophysiology); the EPSP peak and IPSP trough are measured against the 5 s before\n    stimulation (Methods). A cell is 'excitation' with an EPSP only, 'inhibition' with an IPSP only,\n    'mix' with both, 'none' otherwise (Methods; Figure 6D-F legend). The paper gives no threshold\n    for calling a deflection an EPSP or an IPSP; the readings run are a peak (EPSP) or trough (IPSP)\n    of the average trace within 0-5.5 s of light onset (the window the Methods use for total\n    voltage area) beyond (a) 2 or (b) 3 standard deviations of the 5 s baseline of the average\n    trace. Reproduced when, under the readings, each of the three regions has at least one cell with\n    an EPSP and the pooled cells include cells with an IPSP; the proportions of the four classes\n    per region are reported. If the readings disagree the claim is blocked as\n    methods_underspecified.\n\n- id: fig6gi-firing-responses\n  statement: In cells made to fire by constant current, photostimulation increased firing in all\n    BNST cells (5 of 5), while CeA (20 cells) and BLP (17 cells) cells showed either an increase or\n    a decrease in firing.\n  source: Results, DRNDAT input has divergent effects on downstream cellular excitability, paragraph\n    2; Figure 6G-I\n  quote: During spontaneous firing, BNST cells were universally excited whereas more diverse\n    responses were observed with the BLP and CeA\n  expected:\n  - quantity: BNST firing cells\n    value: 5\n    tolerance: 0\n    unit: cells\n  - quantity: CeA firing cells\n    value: 20\n    tolerance: 0\n    unit: cells\n  - quantity: BLP firing cells\n    value: 17\n    tolerance: 0\n    unit: cells\n  criterion: Per cell, the action potential inter-event interval (IEI) in the 5 s before and the 5 s\n    after the first light pulse; a decrease is 'excitation', an increase 'inhibition' (Methods, Ex\n    vivo electrophysiology). The paper does not say how sweeps are combined or which summary of the\n    IEIs is compared; readings (a) mean IEI over all intervals pooled across sweeps, (b) mean over\n    sweeps of each sweep's mean IEI. The Figure 6 supplement 1G legend plots 5.5 s before the light,\n    so a 5.5 s baseline is shown as a variant. Action potentials are detected as upward crossings of\n    0 mV, a standard choice. Reproduced when every BNST cell is excited and both classes occur among\n    CeA cells and among BLP cells, under each reading.\n\n- id: fig6j-epsp-amplitude-region\n  statement: The peak amplitude of the optically evoked EPSP differed between regions, larger in\n    the CeA than in the BLP.\n  source: Figure 6J, left\n  quote: \"peak amplitude (Kruskal-Wallis statistic = 6.790, p=0.0335; Dunn’s posts-hoc tests: CeA vs BLP\n    p=0.0378)\"\n  statistics:\n  - about: EPSP peak amplitude across BNST, CeA and BLP\n    test: Kruskal-Wallis\n    statistic: Kruskal-Wallis statistic = 6.790\n    p: 0.0335\n  - about: CeA against BLP\n    test: Dunn's post hoc test\n    p: 0.0378\n    corrected: Dunn's multiple comparisons\n  depends_on:\n  - fig6df-epsp-ipsp-at-rest\n  criterion: EPSP peak of the average trace at rest against the 5 s baseline (Methods), one value per\n    cell with an EPSP. Which cells enter is open; readings (a) cells with an EPSP (excitation and\n    mix), (b) excitation-only cells. Reproduced when, under the readings, a Kruskal-Wallis test across\n    the three regions gives p < 0.05, Dunn's test gives CeA against BLP p < 0.05, and the CeA median\n    exceeds the BLP median.\n\n- id: fig6k-ipsp-amplitude-region\n  statement: The trough amplitude of the optically evoked IPSP differed between regions, deeper in\n    the CeA than in the BLP.\n  source: Figure 6K, left\n  quote: \"trough amplitude (one-way ANOVA, F2,31=8.150, p=0.0014, CeA vs BLP: **p=0.0014)\"\n  statistics:\n  - about: IPSP trough amplitude across BNST, CeA and BLP\n    test: one-way ANOVA\n    statistic: F(2,31) = 8.150\n    p: 0.0014\n    n: 34 cells with an IPSP (from the degrees of freedom)\n  - about: CeA against BLP\n    test: post hoc comparison (test not named)\n    p: 0.0014\n  depends_on:\n  - fig6df-epsp-ipsp-at-rest\n  expected:\n  - quantity: cells with an IPSP in the test\n    value: 34\n    tolerance: 3.4\n    unit: cells\n  criterion: IPSP trough of the average trace at rest against the 5 s baseline (Methods), one value\n    per cell. Readings for the cells (a) inhibition and mix cells, (b) inhibition-only cells; the\n    single BNST point in Figure 6K beside the absence of BNST inhibition-only cells in Figure 6D\n    favours (a), but both are run. The post hoc test is not named; Tukey's test (the Prism default\n    after a one-way ANOVA) and Holm-Sidak are the readings. Reproduced when the one-way ANOVA gives\n    p < 0.05, CeA against BLP p < 0.05 and the CeA mean trough is more negative than the BLP mean.\n\n- id: fig6-s1de-monosynaptic\n  statement: The optically evoked EPSP and the slow component of the IPSP persisted after TTX/4AP,\n    so the responses were typically monosynaptic.\n  source: Figure 6 supplement 1D-E; Results, DRNDAT input has divergent effects on downstream\n    cellular excitability, paragraph 2\n  quote: the optically-evoked EPSP (upper panels) and slow component of the IPSP (lower panels) was\n    maintained following application of TTX/4AP\n  expected:\n  - quantity: EPSP cells tested with TTX/4AP\n    value: 8\n    tolerance: 0\n    unit: cells\n  - quantity: IPSP cells tested with TTX/4AP\n    value: 3\n    tolerance: 0\n    unit: cells\n  criterion: Per cell, the EPSP peak or IPSP trough after TTX/4AP divided by that before (normalized\n    amplitude, Figure 6 supplement 1E). The paper gives no threshold for 'maintained'; the response\n    is counted as maintained when it is still detected under the readings of fig6df-epsp-ipsp-at-rest.\n    Reproduced when it is maintained in most cells of each group. The normalized amplitudes are\n    reported.\n\n- id: fig6no-cea-clusters\n  statement: Hierarchical clustering of CeA cells on four baseline properties gave two clusters,\n    late-firing cells (cluster 1) that were excited by DRN-DAT input and regular-firing cells\n    (cluster 2) that were mostly inhibited.\n  source: Results, DRNDAT input has divergent effects on downstream cellular excitability, paragraph\n    3; Figure 6L, 6N-O\n  quote: CeA cells in cluster 1 represented ‘late-firing’ neurons, whereas cluster 2 were typical of\n    ‘regularfiring’ neurons ... with cluster 1 ‘late-firing’ neurons excited and cluster 2\n    ‘regular-firing’ neurons mostly inhibited\n  expected:\n  - quantity: CeA cells clustered\n    value: 26\n    tolerance: 0\n    unit: cells\n  depends_on:\n  - fig6df-epsp-ipsp-at-rest\n  - fig6gi-firing-responses\n  criterion: Features from the Methods (Ex vivo electrophysiology). Ramp ratio, mean Vm 900-1000 ms\n    over mean Vm 100-200 ms after step onset at the largest subthreshold step; max instantaneous\n    frequency, the highest firing frequency in the first 100 ms of the depolarizing steps; firing\n    delay, step onset to first spike at rheobase; voltage sag, peak minus steady-state Vm in the\n    -120 pA step. Each feature max-min normalized, Ward linkage on Euclidean distance (scipy\n    linkage), two clusters at the top split. Response label per cell (Methods), from IEI when firing\n    data exist, else EPSP only = excitation, IPSP only = inhibition, mix by the sign of the voltage\n    area 0-5.5 s after light onset. Open details and their readings, all run. (1) Ramp ratio from\n    absolute Vm (as written) or from the deflections from the pre-step baseline. (2) Steady state\n    for the sag, the mean of the last 100 ms or of the last 200 ms of the step. (3) Normalization,\n    max-min as the Methods and legend say, or none, because the dendrogram's axis (to 200) is far\n    above what four features in [0, 1] can give. (4) Cells, those with all four features (26 from\n    t24). The cluster with the longer firing delay is the late-firing cluster. Reproduced when,\n    under the readings, every response-labelled cell of the late-firing cluster is excited and more\n    than half of those of the other cluster are inhibited; blocked as methods_underspecified if the\n    readings disagree.\n\n- id: fig6-s1h-cea-cluster-properties\n  statement: The two CeA clusters differed in all four input properties (ramp ratio, maximum\n    instantaneous frequency, firing delay and voltage sag).\n  source: Figure 6 supplement 1H\n  quote: \"Unpaired t-tests for CeA – ramp ratio: t24=3.502, p=0.0018; max instantaneous firing\n    frequency (max freqinst.): t24=4.698, p<0.0001, firing delay: t24=5.050, p<0.0001, voltage sag:\n    t24=3.983, p=0.0006\"\n  statistics:\n  - about: ramp ratio\n    test: unpaired t-test\n    statistic: t(24) = 3.502\n    p: 0.0018\n  - about: max instantaneous firing frequency\n    test: unpaired t-test\n    statistic: t(24) = 4.698\n    p: 0.0001\n    p_relation: \"<\"\n  - about: firing delay\n    test: unpaired t-test\n    statistic: t(24) = 5.050\n    p: 0.0001\n    p_relation: \"<\"\n  - about: voltage sag\n    test: unpaired t-test\n    statistic: t(24) = 3.983\n    p: 0.0006\n  depends_on:\n  - fig6no-cea-clusters\n  criterion: Unpaired two-sided t-tests (Statistical analyses) between the clusters of\n    fig6no-cea-clusters on the raw feature values. Reproduced when all four give p < 0.05 under the\n    readings of that claim.\n\n- id: fig6pq-blp-clusters\n  statement: BLP cells clustered into putative pyramidal neurons (cluster 1) and putative GABAergic\n    interneurons (cluster 2); 93% of the putative pyramidal neurons were inhibited by DRN-DAT input\n    and 62% of the putative interneurons were excited.\n  source: Results, DRNDAT input has divergent effects on downstream cellular excitability, paragraph\n    3; Figure 6M, 6P-Q\n  quote: with 93% of putative pyramidal neurons showing an inhibitory response, and 62% of putative\n    GABAergic interneurons showing an excitatory response\n  expected:\n  - quantity: putative pyramidal BLP cells inhibited\n    value: 93\n    tolerance: 9.3\n    unit: percent\n  - quantity: putative GABAergic BLP cells excited\n    value: 62\n    tolerance: 6.2\n    unit: percent\n  - quantity: BLP cells clustered\n    value: 27\n    tolerance: 0\n    unit: cells\n  depends_on:\n  - fig6df-epsp-ipsp-at-rest\n  - fig6gi-firing-responses\n  criterion: As fig6no-cea-clusters, with capacitance in place of ramp ratio (Methods). Capacitance\n    from the 5 mV, 250 ms hyperpolarizing step in voltage clamp at -70 mV by the Q-method (charge\n    of the transient over 5 mV; Methods cite the Q-method, the paper's MATLAB code is not\n    published). Cells, those with all four features (27 from t25). The cluster with the larger\n    capacitance and lower maximum frequency is the pyramidal cluster. The same open readings\n    (steady state for the sag, normalization) are run. Denominators are the response-labelled\n    cells of each cluster. Reproduced when both percentages are within tolerance under the\n    readings; partially reproduced when the direction holds (most pyramidal cells inhibited, most\n    interneurons excited) but a percentage is outside tolerance.\n\n- id: fig6-s1i-blp-cluster-properties\n  statement: The two BLP clusters differed in capacitance, maximum instantaneous frequency, firing\n    delay and voltage sag.\n  source: Figure 6 supplement 1I\n  quote: \"unpaired t-tests for BLP – capacitance: t25=4.803, p<0.0001, max freqinst.: t25=15.48,\n    p<0.0001, firing delay: t25=2.743, p=0.0111, voltage sag: t25=2.705, p=0.0121\"\n  statistics:\n  - about: capacitance\n    test: unpaired t-test\n    statistic: t(25) = 4.803\n    p: 0.0001\n    p_relation: \"<\"\n  - about: max instantaneous firing frequency\n    test: unpaired t-test\n    statistic: t(25) = 15.48\n    p: 0.0001\n    p_relation: \"<\"\n  - about: firing delay\n    test: unpaired t-test\n    statistic: t(25) = 2.743\n    p: 0.0111\n  - about: voltage sag\n    test: unpaired t-test\n    statistic: t(25) = 2.705\n    p: 0.0121\n  depends_on:\n  - fig6pq-blp-clusters\n  criterion: Unpaired two-sided t-tests between the clusters of fig6pq-blp-clusters on the raw\n    feature values. Reproduced when all four give p < 0.05 under the readings of that claim.\n\n- id: fig6-s1jk-cluster-voltage-area\n  statement: The total voltage area evoked by DRN-DAT stimulation differed between the two clusters\n    in both the CeA and the BLP, and the EPSP peak amplitude differed between the BLP clusters but not\n    between the CeA clusters.\n  source: Figure 6 supplement 1J-K\n  quote: \"EPSP peak amplitude, CeA: unpaired t-test, t17=1.40, p=0.180; BLP: unpaired t-test t22=2.34,\n    p=0.029. ... Total voltage area, CeA: Mann-Whitney U = 22, p=0.0023; BLP: Mann-Whitney U = 29,\n    p=0.0019\"\n  statistics:\n  - about: CeA clusters, total voltage area\n    test: Mann-Whitney U\n    statistic: U = 22\n    p: 0.0023\n  - about: BLP clusters, total voltage area\n    test: Mann-Whitney U\n    statistic: U = 29\n    p: 0.0019\n  - about: BLP clusters, EPSP peak amplitude\n    test: unpaired t-test\n    statistic: t(22) = 2.34\n    p: 0.029\n  - about: CeA clusters, EPSP peak amplitude\n    test: unpaired t-test\n    statistic: t(17) = 1.40\n    p: 0.18\n  depends_on:\n  - fig6no-cea-clusters\n  - fig6pq-blp-clusters\n  criterion: Total voltage area, the integral of Vm against the 5 s pre-light baseline from 0 to 5.5\n    s after the first pulse, on the average trace at rest (Methods). Mann-Whitney U for the area and\n    unpaired t-test for the EPSP peak between clusters, as the legend names them. Reproduced when\n    the area tests give p < 0.05 in both regions, the BLP EPSP test gives p < 0.05, and the CeA EPSP\n    test gives p >= 0.05 (a claim of absence, judged on the paper's t-test).\n\n- id: fig6-s1ln-combined-clusters\n  statement: Clustering CeA and BLP cells together gave two clusters with a response pattern very\n    similar to that of the separate clusterings.\n  source: Figure 6 supplement 1L-N; Results, DRNDAT input has divergent effects on downstream\n    cellular excitability, paragraph 3\n  quote: In addition, clustering CeA and BLP cells together yielded a very similar result\n  depends_on:\n  - fig6no-cea-clusters\n  - fig6pq-blp-clusters\n  criterion: The five features used in the separate clusterings (ramp ratio, capacitance, maximum\n    instantaneous frequency, firing delay, voltage sag; Figure 6 supplement 1L), max-min normalized,\n    Ward linkage, two clusters, on the cells with all five. Reproduced when, under the readings of\n    the two claims it depends on, at least 80% of the cells fall in the cluster that matches their\n    separate cluster (late-firing CeA and putative interneurons on one side, regular-firing CeA and\n    putative pyramidal on the other, or the reverse, whichever matches better); the paper gives no\n    number for 'very similar', so the agreement is reported in full and the 80% bound is a stated\n    choice.\n\n# ---------------------------------------------------------------- Figure 7, in vivo imaging\n- id: fig7e-no-behavioural-change\n  statement: In ChrimsonR mice the stimulation parameters were tuned so that social preference did\n    not change across GH off, GH on and SI off.\n  source: Figure 7E; Results, DRNDAT input enables a functional shift in CeA dynamics, paragraph 4\n  quote: We successfully optimized viral expression and illumination parameters to minimize changes\n    in social preference with DRNDAT-CeA with ChrimsonR\n  statistics:\n  - test: mixed-effects model\n    statistic: F(1.897, 30.36) = 0.5767\n    p: 0.5591\n    n: 12 mice\n  criterion: A claim of absence, judged on the paper's test. Social:object ratio per session, time\n    in the social side over time in the object side during the 10 min test (Methods, Three chamber\n    sociability assay; the imaging chamber has the same dimensions). Sides are the left and right\n    compartments (23 cm each) of the 57.5 cm chamber, the 11.5 cm centre excluded. A mixed-effects\n    model with condition as the repeated factor (Prism's mixed-effects analysis, restricted maximum\n    likelihood) on the ChrimsonR mice. Reproduced when p >= 0.05; the condition means are reported\n    either way. Total social time (Figure 7E right) is shown as a variant, under both readings the\n    paper allows (social side time, as the axis label says, and social cup interaction time, as\n    the legend says).\n\n- id: fig7gh-delta-auroc-trend\n  statement: CeA response strength to the social cup relative to the object cup (social minus object\n    auROC) tended to be larger with DRN-DAT stimulation (GH on) than without (GH off), a trend with\n    a significant Kruskal-Wallis test across conditions but a non-significant pairwise test.\n  source: Figure 7G-H; Results, DRNDAT input enables a functional shift in CeA dynamics, paragraph 5\n  quote: we did find a trend indicating stronger responses toward social stimuli compared to object\n    stimuli in the GH on condition compared to the GH off condition in mice expressing ChrimsonR\n  statistics:\n  - about: social minus object auROC across GH off, GH on, SI off\n    test: Kruskal-Wallis\n    statistic: K-W statistic = 6.172\n    p: 0.0457\n    n: 429, 441 and 484 cells\n  - about: GH off against GH on\n    test: Dunn's multiple comparisons\n    p: 0.058\n  - about: GH off against SI off\n    test: Dunn's multiple comparisons\n    p: 0.9999\n    p_relation: \">\"\n  expected:\n  - quantity: GH off cells\n    value: 429\n    tolerance: 42.9\n    unit: cells\n  - quantity: GH on cells\n    value: 441\n    tolerance: 44.1\n    unit: cells\n  - quantity: SI off cells\n    value: 484\n    tolerance: 48.4\n    unit: cells\n  criterion: auROC per cell and stimulus as in the Methods (In vivo microendoscopic calcium imaging).\n    A binary vector of social (or object) cup interaction in 40 ms bins against the cell's raw CNMF-E\n    trace z-scored and thresholded at 100 steps from its minimum to its maximum; area under the\n    ROC curve. Interaction, from pose, when the nose is within 1.3 times the cup diameter and the\n    cup lies in a 90 degree cone in front of the head (Methods). Open details, readings all run.\n    (1) Distance, nose to cup centre below 0.65 cup diameters (inside a circle 1.3 times the cup)\n    or below 1.3 cup diameters. (2) Head direction, from the neck or the head keypoint to the nose;\n    the cone is 45 degrees either side. (3) Time base, traces and behaviour resampled to 40 ms bins\n    as written, or the 50 ms imaging frames. (4) Period, the 10 min test only, or the whole session\n    with habituation counted as no interaction. (5) Mice, ChrimsonR mice only (the panel is\n    labelled DRNDAT-CeA:ChrimsonR) or all mice imaged. Kruskal-Wallis on social minus object auROC\n    across the three conditions with cells as samples, then Dunn's test. Reproduced when, under the\n    readings, Kruskal-Wallis gives p < 0.05 and the GH on median or mean exceeds that of GH off;\n    the Dunn p-values are reported. If the readings disagree the claim is blocked as\n    methods_underspecified.\n\n- id: fig7j-proportions-unchanged\n  statement: Single cells did not change significantly in response strength or in the proportion of\n    neurons significantly excited or inhibited by the social or object cup across the three\n    conditions (social cup excited 6.0%, 7.2% and 5.9%, inhibited 4.8%, 4.0% and 6.0%; object cup\n    excited 4.1%, 2.4% and 3.6%, inhibited 5.0%, 3.6% and 5.1%, for GH off, GH on and SI off).\n  source: Figure 7J (percentages read from the figure); Results, DRNDAT input enables a functional\n    shift in CeA dynamics, paragraph 5\n  quote: At a single-cell level, we did not observe significant changes in CeA response strength or\n    proportion of neurons significantly responding to social or object stimuli across the three\n    conditions\n  expected:\n  - quantity: social-excited, GH off\n    value: 6.0\n    tolerance: 0.6\n    unit: percent of cells\n  - quantity: social-excited, GH on\n    value: 7.2\n    tolerance: 0.72\n    unit: percent of cells\n  - quantity: social-excited, SI off\n    value: 5.9\n    tolerance: 0.59\n    unit: percent of cells\n  - quantity: social-inhibited, GH off\n    value: 4.8\n    tolerance: 0.48\n    unit: percent of cells\n  - quantity: social-inhibited, GH on\n    value: 4.0\n    tolerance: 0.4\n    unit: percent of cells\n  - quantity: social-inhibited, SI off\n    value: 6.0\n    tolerance: 0.6\n    unit: percent of cells\n  - quantity: object-excited, GH off\n    value: 4.1\n    tolerance: 0.41\n    unit: percent of cells\n  - quantity: object-excited, GH on\n    value: 2.4\n    tolerance: 0.24\n    unit: percent of cells\n  - quantity: object-excited, SI off\n    value: 3.6\n    tolerance: 0.36\n    unit: percent of cells\n  - quantity: object-inhibited, GH off\n    value: 5.0\n    tolerance: 0.5\n    unit: percent of cells\n  - quantity: object-inhibited, GH on\n    value: 3.6\n    tolerance: 0.36\n    unit: percent of cells\n  - quantity: object-inhibited, SI off\n    value: 5.1\n    tolerance: 0.51\n    unit: percent of cells\n  depends_on:\n  - fig7gh-delta-auroc-trend\n  criterion: A cell is significantly excited when its auROC exceeds the 97.5th percentile of 1,000\n    auROCs from random circular shifts of the behaviour vector, inhibited when below the 2.5th\n    (Methods); shifts drawn uniformly over the session length and the seed are standard choices.\n    The auROC readings of fig7gh-delta-auroc-trend are all run. The expected percentages hold when\n    within tolerance under one reading. The paper names no test for the proportions (the legend of\n    7J is missing); readings for the absence part, a chi-square test of the 3 by 2 table of\n    responsive against other cells per stimulus and sign, and a Kruskal-Wallis test of the\n    per-mouse percentages (Figure 7K-L). Reproduced when the percentages are within tolerance and\n    no test finds p < 0.05; partially reproduced when the tests find no difference but percentages\n    fall outside tolerance.\n\n- id: fig7i-little-overlap\n  statement: Among 202 cells co-registered between GH off and GH on, 16 GH off and 18 GH on cells\n    were excited by the social cup, and only 2 in both sessions, suggesting that stimulation recruits\n    separate CeA ensembles for social stimuli.\n  source: Figure 7I; Results, DRNDAT input enables a functional shift in CeA dynamics, paragraph 5\n  quote: in co-registered neurons, we found little overlap between CeA neurons excited by the social\n    stimulus in both GH on and GH off conditions\n  expected:\n  - quantity: co-registered cells, GH off and GH on\n    value: 202\n    tolerance: 20.2\n    unit: cells\n  - quantity: co-registered cells social-excited in GH off\n    value: 16\n    tolerance: 1.6\n    unit: cells\n  - quantity: co-registered cells social-excited in GH on\n    value: 18\n    tolerance: 1.8\n    unit: cells\n  - quantity: co-registered cells social-excited in both\n    value: 2\n    tolerance: 1\n    unit: cells\n  depends_on:\n  - fig7j-proportions-unchanged\n  criterion: Co-registration with CellReg on the CNMF-E spatial footprints, with translation and\n    rotation and its probabilistic model on spatial correlation and centroid distance (Methods);\n    the paper gives no CellReg parameters, so its defaults are used, a stated choice. The tolerance\n    on the 'both' count is one cell, since 10% of 2 is below a cell. Reproduced when the counts are\n    within tolerance under one auROC reading. Whatever the counts, the overlap is reported against\n    the number expected if the two sets were independent (16 x 18 / 202, about 1.4 in the paper).\n    The figure's inhibitory overlap (12 GH off, 11 GH on, 2 both) is reported as well.\n\n- id: fig7m-social-excited-predicts-preference\n  statement: Across mice, the proportion of socially excited CeA neurons correlated positively with\n    social preference in the GH on condition (r = 0.679, p = 0.045), but not in GH off or SI off.\n  source: Figure 7M (r and p read from the figure); Results, DRNDAT input enables a functional shift\n    in CeA dynamics, paragraph 5\n  quote: we did find a significant positive correlation between the proportion of socially-excited\n    CeA neurons and social preference in the GH on condition, but not in the GH off or SI off\n    conditions\n  statistics:\n  - about: GH on\n    test: Pearson's correlation\n    statistic: r = 0.679\n    p: 0.045\n  expected:\n  - quantity: Pearson r, GH on\n    value: 0.679\n    tolerance: 0.0679\n  depends_on:\n  - fig7j-proportions-unchanged\n  - fig7e-no-behavioural-change\n  criterion: Per mouse and condition, the fraction of its cells significantly excited by the social\n    cup (fig7j-proportions-unchanged) against its social:object ratio (fig7e-no-behavioural-change,\n    labelled soc:obj zone ratio in the figure); Pearson correlation per condition (Statistical\n    analyses). Which mice enter is not stated and the counts disagree (the Figure 7G legend says 15\n    mice, Figure 7E 12 ChrimsonR mice, Figure 7 supplement 1N-O 9, 8 and 9 mice); readings (a)\n    ChrimsonR mice with that session, (b) all mice imaged in that session. Reproduced when, under\n    one reading together with each auROC reading, GH on gives r > 0 with p < 0.05 and GH off and SI\n    off give p >= 0.05; r is within tolerance for full agreement, else partially reproduced. If\n    the readings disagree on the sign or significance, the claim is blocked as\n    methods_underspecified with every result shown.\n\n- id: fig7-s1no-no-other-correlations\n  statement: Social preference did not correlate with the proportion of object-excited CeA neurons\n    or of socially inhibited CeA neurons in any condition.\n  source: Figure 7 supplement 1N-O; Results, DRNDAT input enables a functional shift in CeA\n    dynamics, paragraph 5\n  quote: Importantly, we do not observe a correlation between social preference and object-excited\n    CeA neurons\n  statistics:\n  - about: object-excited, GH off\n    test: Pearson's correlation\n    statistic: r = -0.3231\n    p: 0.6328\n    n: 9 mice\n  - about: object-excited, GH on\n    test: Pearson's correlation\n    statistic: r = -0.1152\n    p: 0.7679\n    n: 8 mice\n  - about: object-excited, SI off\n    test: Pearson's correlation\n    statistic: r = 0.3438\n    p: 0.3307\n    n: 9 mice\n  - about: social-inhibited, GH off\n    test: Pearson's correlation\n    statistic: r = 0.1729\n    p: 0.3625\n    n: 9 mice\n  - about: social-inhibited, GH on\n    test: Pearson's correlation\n    statistic: r = -0.3941\n    p: 0.2939\n    n: 8 mice\n  - about: social-inhibited, SI off\n    test: Pearson's correlation\n    statistic: r = 0.0116\n    p: 0.9745\n    n: 9 mice\n  depends_on:\n  - fig7m-social-excited-predicts-preference\n  criterion: A claim of absence, judged on the paper's Pearson correlations, as in\n    fig7m-social-excited-predicts-preference with object-excited and social-inhibited fractions.\n    Reproduced when all six give p >= 0.05; r is reported either way. The printed GH off pair (r =\n    -0.3231 with p = 0.6328 for N = 9) is not self-consistent, which is noted.\n\n- id: fig7-s1l-tdtomato-no-change\n  statement: In TdTomato control mice, the social minus object auROC did not differ across GH off,\n    GH on and SI off.\n  source: Figure 7 supplement 1L\n  quote: Difference in response strength (Δ auROC) of CeA neurons to social and object cups in\n    DRNDAT-CeA:TdTomato control mice\n  statistics:\n  - test: one-way ANOVA\n    statistic: F(2,173) = 0.4183\n    p: 0.6588\n    n: 39, 61 and 76 cells from 2 mice\n  expected:\n  - quantity: TdTomato cells, GH off\n    value: 39\n    tolerance: 3.9\n    unit: cells\n  - quantity: TdTomato cells, GH on\n    value: 61\n    tolerance: 6.1\n    unit: cells\n  - quantity: TdTomato cells, SI off\n    value: 76\n    tolerance: 7.6\n    unit: cells\n  depends_on:\n  - fig7gh-delta-auroc-trend\n  criterion: A claim of absence, judged on the paper's one-way ANOVA across conditions with cells as\n    samples, on the auROC readings of fig7gh-delta-auroc-trend. Reproduced when p >= 0.05.\n\n- id: fig7-s2-functional-clusters\n  statement: Hierarchical clustering of trial-averaged CeA responses to social and object cup\n    interactions gave 12 functional clusters.\n  source: Figure 7 supplement 2A-B; Methods, In vivo microendoscopic calcium imaging, last paragraph\n  quote: The dendrogram (left) reveals 12 functional clusters of neurons\n  expected:\n  - quantity: functional clusters\n    value: 12\n    tolerance: 1.2\n    unit: clusters\n  depends_on:\n  - fig7gh-delta-auroc-trend\n  criterion: Trials are interactions lasting at least 1 s, at least 5 s after the previous\n    interaction, merging pauses under 1.5 s (Methods). Per neuron, the z-scored average trace from\n    5 s before to 5 s after onset for the social and the object cup, concatenated; MATLAB-style\n    agglomerative clustering cut at 0.770 times the largest linkage distance (Methods). Open\n    details, readings all run. (1) Linkage, MATLAB's default (single) or Ward or average, since the\n    Methods name the 'cluster' function but no method. (2) Z-scoring of the whole trace before\n    averaging, or of the averaged trace. (3) Neurons, pooled across the three conditions (the\n    figure gives percentages per condition from one dendrogram). Reproduced when one reading\n    gives 11 to 13 clusters; the counts under all readings are reported.\n\n- id: fig7-s1ef-red-vs-blue\n  statement: Ex vivo, red light evoked ChrimsonR-mediated potentials in CeA cells with much larger\n    peak amplitude and area than the blue light (0.3 or 0.2 mW) used for imaging.\n  source: Figure 7 supplement 1D-F; Results, DRNDAT input enables a functional shift in CeA dynamics,\n    paragraph 2\n  quote: Red light evoked a PSP with a significantly greater peak amplitude\n  statistics:\n  - about: peak amplitude, 635 nm against 470 nm at 0.3 and 0.2 mW\n    test: repeated measures ANOVA\n    statistic: F(2,16) = 200.1\n    p: 0.0001\n    p_relation: \"<\"\n  - about: area\n    test: repeated measures ANOVA\n    statistic: F(2,16) = 404.2\n    p: 0.0001\n    p_relation: \"<\"\n  criterion: Per cell, the PSP peak amplitude (absolute largest deflection from the 5 s baseline,\n    whichever sign) and the area 0-5.5 s after light onset, for each light condition (Methods, Ex\n    vivo electrophysiology). Repeated measures one-way ANOVA across the three lights. Reproduced\n    when both ANOVAs give p < 0.05 and red exceeds each blue power in most cells.\n\n- id: fig7-s1hi-red-during-blue\n  statement: Red light still evoked PSPs during constant blue light, though they were significantly\n    smaller than with red light alone.\n  source: Figure 7 supplement 1G-I\n  quote: Red light evoked a significantly smaller PSP in the presence of continuous blue light\n  statistics:\n  - about: peak amplitude\n    test: paired t-test\n    statistic: t(11) = 5.172\n    p: 0.0003\n  - about: potential area\n    test: paired t-test\n    statistic: t(11) = 6.431\n    p: 0.0001\n    p_relation: \"<\"\n  criterion: As fig7-s1ef-red-vs-blue, red alone against red during constant 0.3 mW blue light,\n    paired two-sided t-tests. Reproduced when both give p < 0.05 with smaller PSPs during blue\n    light, and a PSP is still detected during blue light in most cells.\n\n# ---------------------------------------------------------------- Figure 1, anatomy\n- id: fig1c-drn-vta-projections\n  statement: DRN-DAT and VTA-DAT neurons innervate distinct targets; VTA-DAT fluorescence is greater\n    in striatal subregions, DRN-DAT fluorescence is greater in the oval BNST and the lateral CeA.\n  source: Figure 1C; Results, DRNDAT neurons project to and exhibit dense collateralization,\n    paragraph 1\n  quote: and significantly greater following DRN injection in the BNST oval nucleus (unpaired ttest\n    t22=3.95, p=0.0007) and CeA lateral division\n  statistics:\n  - about: BNST oval nucleus, DRN against VTA\n    test: unpaired t-test\n    statistic: t(22) = 3.95\n    p: 0.0007\n  - about: CeA lateral division, DRN against VTA\n    test: unpaired t-test\n    statistic: t(34) = 3.18\n    p: 0.0031\n  - about: CPu, VTA against DRN\n    test: unpaired t-test\n    statistic: t(39) = 13.23\n    p: 0.0001\n    p_relation: \"<\"\n\n- id: fig1h-collateralization\n  statement: Dual retrograde tracing shows that many TH+ DRN neurons project to both the BNST and\n    the CeA (46% of BNST projectors, 55% of CeA projectors), while few project to both the BLP and\n    the BNST or CeA (7.6% and 9.7%).\n  source: Figure 1H\n  quote: dual CTB-labelled TH+ cells constituted 46% of all BNST projectors and 55% of all CeA\n    projectors ... (7.6% of BNST projectors and 9.7% of CeA projectors)\n  expected:\n  - quantity: dual-labelled among BNST projectors, BNST and CeA injections\n    value: 46\n    tolerance: 4.6\n    unit: percent\n  - quantity: dual-labelled among CeA projectors, BNST and CeA injections\n    value: 55\n    tolerance: 5.5\n    unit: percent\n  - quantity: dual-labelled among BNST projectors, BNST and BLP injections\n    value: 7.6\n    tolerance: 0.76\n    unit: percent\n  - quantity: dual-labelled among CeA projectors, CeA and BLP injections\n    value: 9.7\n    tolerance: 0.97\n    unit: percent\n\n- id: fig1-s2d-fewer-blp-projectors\n  statement: TH+ BNST and CeA projectors per slice were similar in number, while BLP projectors were\n    significantly fewer.\n  source: Figure 1 supplement 2D\n  quote: The total number of TH+ BNST and CeA projectors per slice was similar (n=27.9 BNST projectors\n    and n=27.2 CeA projectors per slice), whereas TH+ BLP projectors were significantly fewer\n  statistics:\n  - test: Kruskal-Wallis\n    statistic: Kruskal-Wallis statistic = 83.5\n    p: 0.0001\n    p_relation: \"<\"\n  expected:\n  - quantity: BNST projectors per slice\n    value: 27.9\n    tolerance: 2.79\n  - quantity: CeA projectors per slice\n    value: 27.2\n    tolerance: 2.72\n  - quantity: BLP projectors per slice\n    value: 6.4\n    tolerance: 0.64\n\n# ---------------------------------------------------------------- Figures 2 to 4, behaviour\n- id: fig2d-blp-place-avoidance\n  statement: Photostimulation of the DRN-DAT to BLP projection, but not the projections to the BNST\n    or CeA, produced avoidance of the stimulation zone in real-time place preference relative to\n    eYFP controls.\n  source: Figure 2B-G; Results, DRNDAT-BLP photostimulation promotes place avoidance, paragraph 2\n  quote: we found that photostimulation of the DRNDAT-BLP projection, but not the projection to the\n    BNST or CeA, produced avoidance of the stimulation zone, relative to eYFP controls\n  statistics:\n  - about: BLP, ChR2 against eYFP, ON minus OFF zone time\n    test: unpaired t-test\n    statistic: t(20) = 2.13\n    p: 0.0455\n    n: 14 ChR2 and 8 eYFP mice\n  - about: BLP, time in ON zone across the session\n    test: repeated measures two-way ANOVA, main effect of opsin\n    statistic: F(1,20) = 4.53\n    p: 0.046\n  - about: BNST\n    test: unpaired t-test\n    statistic: t(41) = 1.44\n    p: 0.156\n    n: 29 ChR2 and 14 eYFP mice\n  - about: CeA\n    test: unpaired t-test\n    statistic: t(39) = 0.828\n    p: 0.413\n    n: 28 ChR2 and 13 eYFP mice\n  criterion: As the paper tests it, ON minus OFF percent zone time in ChR2 against eYFP mice per\n    projection, unpaired two-sided t-test. Reproduced when BLP gives p < 0.05 with ChR2 lower and\n    BNST and CeA give p >= 0.05.\n\n- id: fig2-s2-no-icss\n  statement: Photostimulation of none of the three projections supported intracranial\n    self-stimulation.\n  source: Figure 2 supplement 2A-C\n  quote: did not support intra-cranial self-stimulation (ICSS) as shown by a lack of preference for\n    the active nosepoke\n  statistics:\n  - about: BNST\n    test: unpaired t-test\n    statistic: t(42) = 0.225\n    p: 0.823\n  - about: CeA\n    test: unpaired t-test\n    statistic: t(41) = 0.225\n    p: 0.823\n  - about: BLP\n    test: unpaired t-test\n    statistic: t(20) = 0.152\n    p: 0.881\n\n- id: fig3a-c-epm-no-effect\n  statement: Photostimulation of the projections had no significant effect on open arm time in the\n    elevated plus maze; BNST stimulation gave only a weak trend toward more open arm time.\n  source: Figure 3A-C; Results, DRNDAT-BNST photostimulation promotes non-social exploration\n  quote: resulted in a weak trend toward increased time spent in the open arm of the EPM\n  statistics:\n  - about: BNST, ON minus first OFF epoch, ChR2 against eYFP\n    test: unpaired t-test\n    statistic: t(27) = 1.39\n    p: 0.177\n  - about: CeA\n    test: unpaired t-test\n    statistic: t(35) = 0.639\n    p: 0.527\n  - about: BLP\n    test: unpaired t-test\n    statistic: t(20) = 0.759\n    p: 0.457\n  - about: BNST, light by group across epochs\n    test: two-way ANOVA, interaction\n    statistic: F(2,50) = 2.008\n    p: 0.145\n\n- id: fig3-s1-oft-no-effect\n  statement: Photostimulation did not change time in the centre or distance travelled in the open\n    field for any projection.\n  source: Figure 3 supplement 1\n  quote: Photostimulation had no significant effect on time spent in the center of the open field\n  statistics:\n  - about: centre time, BNST\n    test: two-way ANOVA, light by group interaction\n    statistic: F(2,90) = 0.2105\n    p: 0.811\n  - about: centre time, CeA\n    test: two-way ANOVA, light by group interaction\n    statistic: F(2,92) = 0.528\n    p: 0.592\n  - about: centre time, BLP\n    test: two-way ANOVA, light by group interaction\n    statistic: F(2,40) = 0.181\n    p: 0.835\n\n- id: fig3g-bnst-rearing\n  statement: Photostimulation of the DRN-DAT to BNST projection increased rearing during the\n    juvenile intruder assay; CeA and BLP stimulation did not.\n  source: Figure 3G-I; Results, DRNDAT-BNST photostimulation promotes non-social exploration\n  quote: photoactivation of the DRNDAT-BNST projection increased rearing behavior\n  statistics:\n  - test: paired t-test\n    statistic: t(23) = 2.32\n    p: 0.0298\n    n: 24 ChR2 mice\n\n- id: fig4e-cea-social-preference\n  statement: Photostimulation of the DRN-DAT to CeA projection increased the social:object ratio in\n    the three-chamber assay; BNST and BLP stimulation had no significant effect.\n  source: Figure 4D-F; Results, DRNDAT-CeA photostimulation promotes sociability, paragraph 1\n  quote: This revealed that optical stimulation of the DRNDAT-CeA projection increased social\n    preference, but no significant effect was observed\n  statistics:\n  - about: CeA ChR2, ON against OFF\n    test: paired t-test\n    statistic: t(28) = 2.91\n    p: 0.021\n    corrected: corrected for multiple comparisons (method not named)\n    n: 29 mice\n  - about: BNST ChR2\n    test: paired t-test\n    statistic: t(26) = 0.552\n    p: 0.586\n    n: 27 mice\n  - about: BLP ChR2\n    test: paired t-test\n    statistic: t(13) = 1.62\n    p: 0.13\n    n: 14 mice\n  - about: CeA ChR2, social zone time\n    test: paired t-test\n    statistic: t(28) = 2.88\n    p: 0.015\n    corrected: corrected for multiple comparisons\n\n- id: fig4h-cea-rank-correlation\n  statement: In DRN-DAT to CeA ChR2 mice the light-induced change in social zone time correlated\n    positively with social dominance.\n  source: Figure 4H; Results, DRNDAT-CeA photostimulation promotes sociability, paragraph 1\n  quote: we found that the optically-induced change in social preference in DRNDAT-CeA mice was\n    positively correlated with social dominance\n  statistics:\n  - test: Pearson's correlation\n    statistic: r = 0.549\n    p: 0.002\n    n: 29 mice\n  expected:\n    quantity: Pearson r\n    value: 0.549\n    tolerance: 0.0549\n\n- id: fig4k-cea-face-investigation\n  statement: Photostimulation of the DRN-DAT to CeA projection modestly increased face investigation\n    of a juvenile in the home cage.\n  source: Figure 4J-L; Results, DRNDAT-CeA photostimulation promotes sociability, paragraph 2\n  quote: photoactivation of the DRNDAT-CeA projection modestly increased face sniffing of the\n    juvenile mouse\n  statistics:\n  - test: paired t-test\n    statistic: t(22) = 2.36\n    p: 0.027\n    n: 22 ChR2 mice\n\n- id: fig4r-markov-transitions\n  statement: In a two-state Markov model of juvenile intruder behaviour, CeA photostimulation changed\n    the probability of transitions between social and nonsocial states but not of transitions within\n    a state.\n  source: Figure 4P-R; Results, DRNDAT-CeA photostimulation promotes sociability, paragraph 4\n  quote: did not significantly change the probability of transitioning within social and nonsocial\n    state (Figure 4Q ), but did significantly change the probability of transitioning between social\n    and nonsocial states\n  statistics:\n  - about: across-state transitions, opsin by transition\n    test: two-way ANOVA, interaction\n    statistic: F(1,68) = 4.452\n    p: 0.0385\n  - about: within-state transitions\n    test: two-way ANOVA, interaction\n    statistic: F(1,68) = 3.385\n    p: 0.0702\n\n- id: fig4-s2d-baseline-correlations\n  statement: Across baseline behaviour, social dominance correlated weakly and negatively with open\n    arm time, and social sniffing correlated robustly and negatively with rearing.\n  source: Figure 4 supplement 2D; Results, DRNDAT-CeA photostimulation promotes sociability,\n    paragraph 3\n  quote: This showed a weak, negative correlation between social dominance and open arm time in the\n    elevated plus maze ... revealed a robust negative correlation between the time spent engaged in\n    social sniffing and time spent rearing\n\n# ---------------------------------------------------------------- Figure 5, receptor expression\n- id: fig5-receptor-segregation\n  statement: In the BNST and CeA terminal fields neuropeptide receptors (Vipr2, Npbwr1) were densely\n    and co-expressed, with Drd2 more abundant than Drd1, while the BLP terminal field was dominated\n    by Drd1.\n  source: Figure 5; Results, DRNDAT terminal fields contain spatially-segregated dopamine and\n    neuropeptide receptor populations, paragraph 2\n  quote: dopamine receptor expression was relatively more sparse, with Drd2 more abundant than Drd1\n    ... The DRNDAT terminal field of the BLP displayed a markedly different receptor expression\n    pattern, dominated by Drd1\n  statistics:\n  - about: oval BNST, probe by AP position\n    test: two-way ANOVA, interaction\n    statistic: F(9,160) = 6.194\n    p: 0.0001\n    p_relation: \"<\"\n  - about: CeL, probe by AP position\n    test: two-way ANOVA, interaction\n    statistic: F(12,220) = 8.664\n    p: 0.0001\n    p_relation: \"<\"\n  - about: BLP, probe by AP position\n    test: two-way ANOVA, interaction\n    statistic: F(15,176) = 2.165\n    p: 0.0091\n\n# ---------------------------------------------------------------- Figure 8, photoinhibition\n- id: fig8c-cea-inhibition-blocks-rebound\n  statement: Photoinhibition of DRN-DAT terminals in the CeA, but not the BNST or BLP, blocked the\n    increase in social preference after 24 h of isolation.\n  source: Figure 8C; Results, DRNDAT-CeA photoinhibition blocks isolation-induced sociability\n  quote: However, inhibition of DRNDAT terminals in CeA, but not BNST or BLP, blocked the rebound in\n    sociability associated with acute social isolation\n  statistics:\n  - about: CeA, light by group\n    test: two-way RM ANOVA, interaction\n    statistic: F(1,30) = 4.909\n    p: 0.0344\n    n: 20 NpHR and 12 eYFP mice\n  - about: CeA NpHR against eYFP after isolation\n    test: multiple comparisons test\n    p: 0.0017\n    corrected: adjusted\n  - about: CeA, isolated minus grouped, NpHR against eYFP\n    test: unpaired t-test\n    statistic: t(29) = 2.177\n    p: 0.0377\n  - about: BNST, light by group\n    test: two-way RM ANOVA, interaction\n    statistic: F(1,10) = 1.005\n    p: 0.3397\n  - about: BLP, light by group\n    test: two-way RM ANOVA, interaction\n    statistic: F(1,12) = 3.346\n    p: 0.0923\n\n- id: fig8d-cea-inhibition-rank\n  statement: In CeA NpHR mice the change in social zone time after isolation correlated negatively\n    with social dominance.\n  source: Figure 8D\n  quote: showing significant negative correlation in NpHRCeA mice\n  statistics:\n  - test: Pearson's correlation\n    statistic: r = -0.500\n    p: 0.0414\n    n: 20 mice\n  expected:\n    quantity: Pearson r\n    value: -0.5\n    tolerance: 0.05\n\n- id: fig8-s1-no-effect-group-housed\n  statement: Photoinhibition of the terminals in group-housed mice did not change social preference\n    in any region.\n  source: Figure 8 supplement 1B\n  quote: Photoinhibition had no significant effect on social:object ratio in group-housed mice\n  statistics:\n  - about: CeA\n    test: two-way ANOVA, light by group interaction\n    statistic: F(1,31) = 0.1353\n    p: 0.7154\n  - about: BNST\n    test: two-way ANOVA, light by group interaction\n    p: 0.4571\n  - about: BLP\n    test: two-way ANOVA, light by group interaction\n    statistic: F(1,14) = 2.517\n    p: 0.1349\n"
}
```

Result: not kept, because it reads the paper's text.

**Agent**

The draft is written. Fixing one quote where I dropped a colon, then running the quote checker.

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001195/10.7554-elife.105955.yaml",
 "old_string": "  quote: and significantly greater following DRN injection in the BNST oval nucleus (unpaired ttest\n    t22=3.95, p=0.0007) and CeA lateral division",
 "new_string": "  quote: \"and significantly greater following DRN injection in the BNST oval nucleus (unpaired ttest:\n    t22=3.95, p=0.0007) and CeA lateral division\""
}
```

```
The file claims/001195/10.7554-elife.105955.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
python tools/claims_check.py claims/001195/10.7554-elife.105955.yaml paper/10.7554-elife.105955.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001195/10.7554-elife.105955.yaml",
 "old_string": "  quote: we did find a trend indicating",
 "new_string": "  quote: did find a trend indicating"
}
```

```
The file claims/001195/10.7554-elife.105955.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
python tools/claims_check.py claims/001195/10.7554-elife.105955.yaml paper/10.7554-elife.105955.txt; grep -n -E "—| rather |^[^#\"]*[a-z]: [^\"]*: " claims/001195/10.7554-elife.105955.yaml | grep -v -E "^\s*[0-9]+:\s*(- )?[a-z_]+: " | head
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
python -c "
import yaml;d=yaml.safe_load(open('claims/001195/10.7554-elife.105955.yaml'))
c=d['claims'];print(len(c),sum('quote' in x for x in c),sum('statistics' in x for x in c),sum('criterion' in x for x in c),sum('expected' in x for x in c))"; grep -c "rather" claims/001195/10.7554-elife.105955.yaml
```

```
38 38 27 22 16
0
```

**Agent**

I've written `claims/001195/10.7554-elife.105955.yaml`. The quote checker reports 0 problems: 38 claims, 38 quotes, 71 statistical values.

**Text read.** The eLife reviewed preprint, version 2 (8 July 2025): main text, Methods, figure legends and all figure supplements. I opened the PDF only for Figures 6 and 7.
- The paper links no analysis code, so every method detail comes from the Methods, legends and supplements.
- The earlier Research Square preprint uses the same patch-clamp data. I checked only its ex vivo Methods: they match the eLife text, and it adds that the cells recorded at rest came from 19 mice.
- The dandiset holds the ex vivo patch-clamp data (Figure 6) and the CeA imaging with behaviour videos (Figure 7). Those claims have full criteria.

**Counts.** 38 claims: all 38 have quotes, 27 have statistics, 22 have criteria and 16 have expected values. Of these, 20 cover Figures 6 and 7 with their supplements. The other 18 cover tracing, behaviour, RNAscope and photoinhibition, and most of them record only the paper's tests.

**Details the paper leaves open, with the readings named:**
- **EPSP/IPSP detection (6D-F, also used by 6J-K, the clusters and TTX/4AP):** no threshold is given. Readings: a deflection beyond 2 or 3 SD of the 5 s baseline.
- **Firing responses (6G-I):** how sweeps are combined is not stated. Readings: pooled intervals, or the mean over sweeps. A 5.5 s baseline (the supplement legend) is a variant of the Methods' 5 s.
- **Which cells enter 6J-K:** cells with any EPSP (or IPSP), or single-type cells only. The post hoc test in 6K is not named: Tukey or Holm-Sidak.
- **Clustering (6N-Q):**
  - Ramp ratio: absolute membrane potential, or deflection from baseline.
  - Sag steady state: last 100 ms or last 200 ms of the step.
  - Max-min normalisation, or none. The dendrogram axes (up to 200 and 350) are far above what four features scaled to 0–1 can give.
  - For capacitance the paper cites the Q-method, but its MATLAB code is not published.
- **auROC (7G-H, J, I, M):**
  - Interaction distance: nose within 0.65 or 1.3 cup diameters.
  - Head direction: from the neck or the head keypoint.
  - Time bins: 40 ms as written, or the 50 ms imaging frames.
  - Period: test only, or the whole session.
  - Mice: ChrimsonR only, or all imaged.
- **Proportion test (7J):** none is named. Readings: chi-square, or Kruskal-Wallis on per-mouse percentages.
- **Which mice enter 7M:** the counts disagree (15, 12, and 9/8/9 in different places).
- **Social time in 7E (variant):** time on the social side, or cup interaction time.
- **Functional clusters (7-S2):**
  - Linkage: MATLAB default (single), Ward or average.
  - Z-scoring: before or after averaging.
- **Combined clustering (6-S1L-N):** "very similar" is judged by my own choice of at least 80% agreement, which the criterion states as a choice.

**Missing from the paper:**
- The Figure 7 legend runs off the page in the PDF itself, so panels J to M have none. I read the 7J percentages and 7M's r = 0.679, p = 0.045 from the figure image.
- Figure 6 gives the response proportions only as unlabelled pie charts.
- The supplied text has no data or code availability statement, and the source data files are not included.
- The SLEAP model and CellReg parameters are not given; the criteria use CellReg defaults.
- 7-S1N prints r = -0.3231 with p = 0.6328 for N = 9, which do not match each other.

## End of run

40 turns, 7 minutes, result: success.
