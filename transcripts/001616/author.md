# 001616 · author · run 38628885035

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cat docs/protocol.md; ls; ls entries claims attempts tools
```

```
# Protocol for an attempt

Version: `pilot-6`. Record this version in the attempt's provenance.

This is what an agent, or a person, does to attempt a target and deposit the
result. It is written from the eight pilot attempts
([pilot notes](pilot-notes.md)); the reasons for the rules are there.

There are two roles. The **author** makes the attempt. The **verifier** checks
it and must not be the author: for agents, a separate run with a separate
context that has not seen the author's reasoning.

Agent runs are made with the [Agent run](../.github/workflows/attempt.yml)
workflow, one role at a time: `author`, `verifier-1`, `author-revise-1`,
`verifier-2`, `author-revise-2`, and, when the last of these proposes changes
of outcome, `verifier-3` and `author-revise-3`. Each run's transcript and final report are
kept in [`transcripts/<dandiset>/`](../transcripts).

## Author

[... 369 more lines not kept]
```

**Agent calls Bash**

```bash
cat README.md docs/design.md; ls -R entries/001453-fouke-2025 claims/001453; cat attempts/001453-fouke-2025-01.yaml
```

```
<persisted-output>
Output too large (52.7KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/3a2bc7d8-533c-480a-983e-8dfeabc62c0c/tool-results/bl0slj9ia.txt

Preview (first 2KB):
# Reproduction registry (working name)

Agents, and people, try to reproduce the key findings of papers from the open
data on the [DANDI Archive](https://dandiarchive.org), and register the result
here: the notebooks when it works, and the reason when it does not.

- **For the archive:** evidence of whether each dandiset is complete and
  accurate enough to support the findings of its paper.
- **For analysts:** working notebooks to build new analyses on.

Status: pilot. All eight pilot targets have been attempted and checked by an
independent agent.

**Dashboard:** <https://catalystneuro.github.io/reproduction-registry/>

## Reading the outcomes
[... 24 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/3a2bc7d8-533c-480a-983e-8dfeabc62c0c/tool-results/bl0slj9ia.txt"
}
```

```
1	# Reproduction registry (working name)
2	
3	Agents, and people, try to reproduce the key findings of papers from the open
4	data on the [DANDI Archive](https://dandiarchive.org), and register the result
5	here: the notebooks when it works, and the reason when it does not.
6	
7	- **For the archive:** evidence of whether each dandiset is complete and
8	  accurate enough to support the findings of its paper.
9	- **For analysts:** working notebooks to build new analyses on.
10	
11	Status: pilot. All eight pilot targets have been attempted and checked by an
12	independent agent.
13	
14	**Dashboard:** <https://catalystneuro.github.io/reproduction-registry/>
15	
16	## Reading the outcomes
17	
18	An outcome says what one attempt could recover from the data in a dandiset,
19	with the methods available to it. **A "not reproduced" or "partially
20	reproduced" outcome is not a finding that the paper is wrong.** It can come
[... 971 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/001453-fouke-2025; cat entry.yaml requirements.in README.md; head -c 6000 ../../claims/001453/*.yaml; echo; python -c "
import json;nb=json.load(open('reproduce_fouke_2025.ipynb'))
for c in nb['cells'][:12]: print('----',c['cell_type'],c.get('metadata'));print(''.join(c['source'])[:2500])
"
```

```
schema_version: 1
name: 001453-fouke-2025
type: reproduction
title: Optomotor swimming of zebrafish and Danionella cerebrum (Fouke et al. 2025)
description: Tests the freely swimming findings of Fouke, He, Loring and Naumann (2025) on dandiset
  001453, which holds the tracking data of 25 zebrafish and 12 Danionella cerebrum larvae during the
  optomotor protocol. It compares swimming speed, turning and angular acceleration between species
  and stimuli, the response to monocular stimuli, and how steady the swimming is. The imaging and
  head-fixed tail tracking of the paper's Figures 2 to 4 are not in the dandiset.
license: Apache-2.0
notebooks:
- path: reproduce_fouke_2025.ipynb
  title: Reproducing Fouke et al. (2025) from dandiset 001453
  runtime_minutes: 6
helpers:
- omr.py
related:
- id: dandi:001453/0.250518.1950
  relation: uses_data
- id: doi:10.1016/j.cub.2025.04.027
[... 372 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python -c "
import json;nb=json.load(open('entries/001453-fouke-2025/reproduce_fouke_2025.ipynb'))
for c in nb['cells'][12:]: print('----',c['cell_type'],c.get('metadata'));print(''.join(c['source'])[:800])
" | tail -150; head -80 entries/001453-fouke-2025/omr.py; ls schemas; wc -l tools/entry.py
```

```
print(rate_aw.groupby(["species", "rate"]).right_minus_left.agg(["median", "size"]).round(2).to_string())
pair = (aw[3] - aw[2]).rename("right_minus_left_binocular")
for sp in ("ZF", "DC"):
    v = pair.loc[sp].dropna()
    print(f"{sp}, codes 3 minus 2 only: median {v.median():.2f} deg/s over {len(v)} fish, p = {stats.wilcoxon(v, alternative='greater').pvalue:.3g}")
---- markdown {}
**Result: partially reproduced.** ZF follow the direction of motion: the rightward minus leftward
difference is positive in 23 of 25 fish (median 29.51 deg/s, one-sided Wilcoxon p = 9.8e-07). DC do
not by this test: 7 of 12 fish are positive, median 0.88 deg/s, p = 0.151, and the DC median for
left motion is +0.25 deg/s. Codes 3 minus 2 alone give the same (ZF 45.08 deg/s, p = 2.6e-06; DC
3.10 deg/s, p = 0.133). DC turn right to right motion (median 8.67 deg/s), and four DC fish have
differences above 12 deg/s.
---- markdown {}
## fig1h-zf-higher-angular-acceleration

> Across directional stimuli ZF have higher angular acceleration than DC, and the distributions
> of the two species differ for every stimulus.
---- code {'tags': ['claim:fig1h-zf-higher-angular-acceleration']}
started = time.time()
passing = set(zip(measures[measures.passes].path, measures[measures.passes].trial))
[... 214 more lines not kept]
```

**Agent**

I've read the protocol and the example entry. Now the target: metadata of dandiset 001616 and the paper.

**Agent calls Bash**

```bash
cd $TMPDIR; curl -s https://api.dandiarchive.org/api/dandisets/001616/ | python -m json.tool | head -40; curl -s "https://api.dandiarchive.org/api/dandisets/001616/versions/" | python -m json.tool
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR; for v in 0.260702.0824 0.260519.1133; do curl -s "https://api.dandiarchive.org/api/dandisets/001616/versions/$v/assets/?page_size=200" | python -c "
import json,sys;d=json.load(sys.stdin)
for a in d['results']: print(a['path'],a['size'],a['blob'] if 'blob' in a else '',a['asset_id'])
"; echo; done; curl -s "https://api.dandiarchive.org/api/dandisets/001616/versions/0.260702.0824/" > meta.json; python -m json.tool meta.json | head -300
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR; python -c "
import json;m=json.load(open('meta.json'))
for k in ['description','relatedResource','assetsSummary','studyTarget','protocol','ethicsApproval','wasGeneratedBy','dateCreated','datePublished']: print(k, json.dumps(m.get(k),indent=1)[:3000])
"; curl -s "https://api.dandiarchive.org/api/dandisets/001616/versions/0.260519.1133/" | python -c "
import json,sys;m=json.load(sys.stdin); print(m['description']); print(json.dumps(m.get('relatedResource'),indent=1))"
```

Result: the fetched text is not kept.

**Agent**

Now the paper. eLife is open access; I'll fetch the reviewed preprint text.

**Agent calls Bash**

```bash
mkdir -p paper; cd paper; curl -sL "https://api.crossref.org/works/10.7554/elife.106758.1" | python -c "import json,sys;m=json.load(sys.stdin)['message'];print(m.get('title'),m.get('author')[:3],m.get('published'),m.get('URL'),m.get('relation'))" ; curl -sL -o rp.html "https://elifesciences.org/reviewed-preprints/106758v1"; ls -la; curl -sL "https://elifesciences.org/reviewed-preprints/106758" -o rp_latest.html; ls -la
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd paper; cat rp.html | head -30; curl -sL "https://prod--gateway.elifesciences.org/reviewed-preprints/106758v1" -o gw.json; head -c 500 gw.json; echo; curl -sL "https://api.biorxiv.org/details/biorxiv/10.1101/2024.06.13.598791" | head -c 2000
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd paper; for u in "https://prod--epp.elifesciences.org/api/preprints/106758v1" "https://api.elifesciences.org/reviewed-preprints/106758" "https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.7554/eLife.106758.1&format=json&resultType=core"; do echo "== $u"; curl -sL "$u" | head -c 800; echo; done
```

```
== https://prod--epp.elifesciences.org/api/preprints/106758v1
{"article":{"msid":"106758","doi":"10.7554/eLife.106758.1","id":"106758v1","versionIdentifier":"1","versionDoi":"10.7554/eLife.106758.1","umbrellaDoi":"10.7554/eLife.106758","article":{"title":"Decoding movie content from neuronal population activity in the human medial temporal lobe","authors":[{"type":"Person","affiliations":[{"type":"Organization","name":"Dynamic Vision and Learning Group, Technical University of Munich, Munich, Germany"}],"familyNames":["Gerken"],"givenNames":["Franziska"],"identifiers":[{"type":"PropertyValue","propertyID":"https://registry.identifiers.org/registry/orcid","value":"http://orcid.org/0009-0004-9668-719X"}],"meta":{"notes":[{"type":"fn","label":"*","rid":"n1"}]}},{"type":"Person","affiliations":[{"type":"Organization","name":"Department of Epileptology, U
== https://api.elifesciences.org/reviewed-preprints/106758
{"id":"106758","doi":"10.1101/2024.06.13.598791","version":1,"status":"reviewed","authorLine":"Franziska Gerken, Alana Darcher ... Laura Leal-Taixé","title":"Decoding movie content from neuronal population activity in the human medial temporal lobe","published":"2025-08-13T14:00:00Z","reviewedDate":"2025-08-13T14:00:00Z","versionDate":"2025-08-13T14:00:00Z","statusDate":"2025-08-13T14:00:00Z","stage":"published","subjects":[{"id":"neuroscience","name":"Neuroscience"}],"elifeAssessment":{"title":"eLife Assessment","content":[{"type":"paragraph","text":"This valuable study demonstrates that it is possible to decode information about characters and locations from single-unit responses in the human brain to a narrative movie, using a convincing technical approach to capture information in pop
== https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.7554/eLife.106758.1&format=json&resultType=core
{"version":"6.9","hitCount":0,"request":{"queryString":"DOI:10.7554/eLife.106758.1","resultType":"core","cursorMark":"*","pageSize":25,"sort":"","synonym":fal
[... 1 more lines not kept]
```

**Agent calls Bash**

```bash
cd paper; curl -sL "https://prod--epp.elifesciences.org/api/preprints/106758v1" -o epp_106758v1.json; python - <<'EOF'
import json
d=json.load(open('epp_106758v1.json'))
print(d.keys()); a=d['article']; print(a.keys()); print(a['article'].keys())
out=[]
def walk(n,depth=0):
    if isinstance(n,str): out.append(n); return
    if isinstance(n,list):
        for x in n: walk(x,depth); return
    if isinstance(n,dict):
        t=n.get('type')
        if t=='Heading': out.append('\n\n'+'#'*n.get('depth',1)+' ')
        if t in('Paragraph','Figure','Table','ListItem'): out.append('\n\n')
        if t=='Figure' or t=='Table':
            out.append('[%s %s] '%(t,n.get('label','')))
        for k in ('content','caption','items','rows','cells'):
            if k in n: walk(n[k],depth)
        if t=='Math' or t=='MathFragment': out.append(n.get('text','') or n.get('mathml','')[:0])
art=a['article']
walk(art.get('abstract'))
walk(art['content'])
txt=''.join(out)
open('paper.txt','w').write(txt); print(len(txt))
EOF
grep -n "^#" paper.txt | head -80
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd paper; python - <<'EOF'
import json
d=json.load(open('epp_106758v1.json'))
c=d['article']['article']['content']
print(type(c), len(c))
print(json.dumps(c[:3],indent=0)[:2000])
EOF
```

```
<class 'list'> 166
[
{
"type": "Heading",
"id": "s1",
"depth": 1,
"content": [
"Introduction"
]
},
{
"type": "Paragraph",
"content": [
"The human medial temporal lobe (MTL) plays an integral role in the representation of semantic information. Single neurons in the MTL exhibit strong and highly selective tunings to categories, such as faces or locations ",
{
"type": "Superscript",
"content": [
{
"type": "Cite",
"target": "c1",
[... 110 more lines not kept]
```

**Agent calls Bash**

```bash
cd paper; python - <<'EOF'
import json
d=json.load(open('epp_106758v1.json'))
out=[]
def walk(n):
    if isinstance(n,str): out.append(n); return
    if isinstance(n,list):
        for x in n: walk(x)
        return
    if isinstance(n,dict):
        t=n.get('type')
        if t=='Heading': out.append('\n\n'+'#'*n.get('depth',1)+' ')
        if t in('Paragraph','ListItem'): out.append('\n\n')
        if t in('Figure','Table'): out.append('\n\n[%s %s] '%(t,n.get('label','')))
        if t=='TableRow': out.append('\n| ')
        if t=='TableCell': out.append(' | ')
        for k in ('content','caption','items','rows','cells','label'):
            if k in n and k!='label': walk(n[k])
art=d['article']['article']
out.append('# Abstract\n'); walk(art.get('abstract'))
walk(art['content'])
txt=''.join(out)
open('paper.txt','w').write(txt); print(len(txt))
EOF
grep -n "^#" paper.txt
```

```
87170
1:# Abstract
6:# Introduction
16:# Results
22:# Overview of dataset, features, and decoding approach.
30:## Stimulus-aligned responsive neurons found primarily in parahippocampal cortex
36:# Responsive single-neurons in the parahippocampal cortex.
42:## Decoding of semantic content from population responses
46:### Decoding from neuronal activity
52:# Categories of labels can be decoded from the neuronal population activity.
60:## Choice of architecture
66:## Avoiding spurious decoding performance by introducing temporal gaps
70:### Patient-wise decoding performance
78:# Patient-specific decoding performance.
84:## Parahippocampal cortex drives decoding of visual transitions and location
92:## Amygdala drives decoding of character presence
96:## Distribution of information across MTL regions
102:# Semantic information is distributed differently across MTL regions based on category.
108:## Differences in character’s visual appearances
114:## Responsive neurons drive decoding of visual transitions but not decoding of characters
[... 46 more lines not kept]
```

**Agent**

Full text of the eLife reviewed preprint (v1) is available and saved under `paper/`. Reading it now.

**Agent calls Read**

```json
{
 "file_path": "paper/paper.txt"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/paper.txt",
 "offset": 232
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd paper; python -c "
import json;d=json.load(open('epp_106758v1.json'))
print(json.dumps(d['versions'],indent=0)[:1500]); print(d['article']['article']['meta'] if 'meta' in d['article']['article'] else '')
" | head -60; grep -o '"[^"]*supp[^"]*"' epp_106758v1.json | sort -u | head; grep -o 'https://[^"]*\.pdf' epp_106758v1.json | sort -u | head
```

```
{
"106758v1": {
"msid": "106758",
"doi": "10.7554/eLife.106758.1",
"id": "106758v1",
"versionIdentifier": "1",
"versionDoi": "10.7554/eLife.106758.1",
"umbrellaDoi": "10.7554/eLife.106758",
"preprintDoi": "10.1101/2024.06.13.598791",
"preprintUrl": "https://www.biorxiv.org/content/10.1101/2024.06.13.598791v2",
"preprintPosted": "2025-03-11T00:00:00.000Z",
"sentForReview": "2025-05-06T10:34:43.000Z",
"peerReview": {
"evaluationSummary": {
"date": "2025-08-12T09:15:07.591Z",
"doi": "10.7554/eLife.106758.1.sa4",
"participants": [
{
"name": "Iris Groen",
"role": "editor",
[... 20 more lines not kept]
```

**Agent calls Bash**

```bash
cd paper; for u in "https://prod--epp.elifesciences.org/api/files/106758/v1/content/supplements/598791_file03.pdf" "https://prod--epp.elifesciences.org/api/files/106758/v1/content/supplements/598791_file03.pdf/" ; do curl -sL -o supp.pdf "$u"; file supp.pdf; done; ls -la; pip list 2>/dev/null | grep -i -E "pdf|pymupdf|fitz"; which pdftotext
```

```
Exit code 1
supp.pdf: PDF document, version 1.3
supp.pdf: XML 1.0 document, ASCII text
total 320
drwxr-xr-x  3 runner runner   4096 Oct 14 20:20 .
drwxr-xr-x 16 runner runner   4096 Oct 14 20:20 ..
drwxr-xr-x  3 runner runner   4096 Oct 14 20:17 .claude
-rw-r--r--  1 runner runner 211400 Oct 14 20:20 epp_106758v1.json
-rw-r--r--  1 runner runner  87392 Oct 14 20:20 paper.txt
-rw-r--r--  1 runner runner   3038 Oct 14 20:17 rp.html
-rw-r--r--  1 runner runner   3038 Oct 14 20:17 rp_latest.html
-rw-r--r--  1 runner runner    330 Oct 14 20:20 supp.pdf
```

**Agent calls Bash**

```bash
cd paper; curl -sL -o supp.pdf "https://prod--epp.elifesciences.org/api/files/106758/v1/content/supplements/598791_file03.pdf"; ls -la supp.pdf; python -c "import fitz" 2>&1; python -c "import pypdf" 2>&1; uv --version
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd paper; uv run --with pypdf python -c "
import pypdf;r=pypdf.PdfReader('supp.pdf');print(len(r.pages))
open('supp.txt','w').write('\n\n=== PAGE ===\n'.join(p.extract_text() for p in r.pages))
" && wc -c supp.txt
```

```
Installed 1 package in 2ms
Ignoring wrong pointing object 24 0 (offset 0)
Ignoring wrong pointing object 40 0 (offset 0)
Ignoring wrong pointing object 115 0 (offset 0)
Ignoring wrong pointing object 174 0 (offset 0)
16
21977 supp.txt
```

**Agent calls Read**

```json
{
 "file_path": "paper/supp.txt"
}
```

Result: not kept, because it reads the paper's text.

**Agent**

Paper and supplement read. Now the code the dandiset links to (GitHub mormannlab/SUMMER, Zenodo 18790255).

**Agent calls Bash**

```bash
cd $TMPDIR && git clone -q https://github.com/mormannlab/SUMMER && cd SUMMER && git log --oneline | head -5 && git rev-parse HEAD && find . -path ./.git -prune -o -type f -print | head -100; curl -s https://zenodo.org/api/records/18790255 | python -c "import json,sys;m=json.load(sys.stdin);print(m['metadata']['title'],m['metadata'].get('version'),m['metadata'].get('related_identifiers'));print([f['key'] for f in m['files']])"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR/SUMMER; git tag; git log -1 --format='%H %cd' v1.0.0 2>/dev/null; wc -l README.md ML_framework/*.py ML_framework/nwb_loading/*.py visualization/plot_code/responsive_units/utils/*.py visualization/plot_code/nwb_io.py nwb_generation/utils/process_labels.py nwb_generation/write_nwb.py; cat README.md ML_framework/README.md
```

```
v1.0.0
v1.1.0
v1.2.0
4d46ff2234d4af78c8f0e5992afa500d543ab63f Thu Feb 26 12:21:46 2026 +0000
   203 README.md
     1 ML_framework/__init__.py
   647 ML_framework/dataloader.py
   108 ML_framework/model.py
   187 ML_framework/train.py
     1 ML_framework/nwb_loading/__init__.py
   275 ML_framework/nwb_loading/binning.py
   250 ML_framework/nwb_loading/nwb_loading.py
     0 visualization/plot_code/responsive_units/utils/__init__.py
   275 visualization/plot_code/responsive_units/utils/calc_cluster_permutation.py
   274 visualization/plot_code/responsive_units/utils/calc_responsive_units.py
   295 visualization/plot_code/nwb_io.py
    37 nwb_generation/utils/process_labels.py
  1053 nwb_generation/write_nwb.py
  3606 total
# SUMMER
[... 369 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/SUMMER; cat ML_framework/nwb_loading/nwb_loading.py ML_framework/nwb_loading/binning.py
```

```
from pathlib import Path
import numpy as np
from pynwb import NWBHDF5IO

from .binning import *

DEFAULT_DATA_DIR = "/data"

def load_nwb(patient, data_dir=None):
    """
    Load NWB data for a given patient.

    Parameters:
        patient (str): The patient ID.
        data_dir (str, optional): Directory containing NWB files. Defaults to "/data".

    Returns:
        tuple: A tuple containing the loaded NWB file and the path to the NWB file.
    """
    base = Path(data_dir) if data_dir is not None else Path(DEFAULT_DATA_DIR)
[... 507 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/SUMMER; cat ML_framework/dataloader.py | sed -n 1,400p
```

```
"""
PyTorch Dataset and Lightning DataModule for SUMMER NWB data.
Supports single or multiple patients; multi-patient data is concatenated along the units dimension.
Optional buffer/fold split for train/val/test with temporal separation.
"""

from pathlib import Path
import logging
import math
import numpy as np
import torch
from torch.utils.data import Dataset, DataLoader, Subset
import pytorch_lightning as pl

logger = logging.getLogger(__name__)

# Buffer size (seconds) -> number of repeated parts in the session (for split layout)
"""BUFFER_NUMBER_REPEATED_PARTS = {
    5: 59, 10: 36, 15: 26, 20: 21, 25: 17, 30: 14, 35: 12, 40: 11, 45: 10, 50: 9, 55: 8,
}"""
[... 381 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/SUMMER; cat visualization/plot_code/responsive_units/utils/calc_responsive_units.py; sed -n 1,120p visualization/plot_code/responsive_units/utils/calc_cluster_permutation.py
```

```
"""
calc_responsive_units.py

Module for calculating responsive units in neural spike data, including
functions for extracting spike times around events, binning spike trains,
computing baseline and stimulus activity, and applying a ZETA test to each
unit.

Author: Alana Darcher
Date: 2025-09-16

Dependencies:
    numpy
    pandas
    zetapy
    tqdm

Usage:
    Import and use the provided functions to process spike/event data and
    assess responsiveness of neural units.
[... 375 more lines not kept]
```

**Agent calls Bash**

```bash
mkdir -p $TMPDIR/scratch && cd $TMPDIR/scratch && uv venv -q -p 3.12 .venv && . .venv/bin/activate && uv pip install -q dandi h5py remfile pynwb numpy pandas scipy scikit-learn statsmodels matplotlib 2>&1 | tail -2; python -c "import pynwb,dandi;print(pynwb.__version__,dandi.__version__)"
```

```
4.2.0 0.81.0
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/scratch && . .venv/bin/activate && cat > inspect1.py <<'EOF'
import h5py, remfile, numpy as np
from dandi.dandiapi import DandiAPIClient
with DandiAPIClient() as c:
    ds=c.get_dandiset("001616","0.260702.0824")
    a=ds.get_asset_by_path("sub-1/sub-1_ses-sub1_ecephys.nwb")
    url=a.get_content_url(follow_redirects=1, strip_query=True)
f=h5py.File(remfile.File(url),'r')
def show(name,obj):
    if isinstance(obj,h5py.Dataset):
        s=f"{name} {obj.shape} {obj.dtype}"
        at={k:(v.decode() if isinstance(v,bytes) else v) for k,v in obj.attrs.items() if k not in('namespace','object_id')}
        print(s, {k:str(v)[:80] for k,v in at.items()})
    else:
        at={k:(v.decode() if isinstance(v,bytes) else v) for k,v in obj.attrs.items() if k not in('namespace','object_id')}
        print(name+'/', {k:str(v)[:120] for k,v in at.items()})
f.visititems(show)
EOF
python inspect1.py 2>&1 | grep -v "^specifications" | head -250
```

```
acquisition/ {}
analysis/ {}
file_create_date (1,) object {}
general/ {}
general/devices/ {}
general/devices/NeuraLynx ATLAS/ {'description': 'Acquisition amplifier', 'manufacturer': 'NeuraLynx', 'neurodata_type': 'Device'}
general/experiment_description () object {}
general/extracellular_ephys/ {}
general/extracellular_ephys/LA/ {'description': 'depth electrode AL (macro contact), AL manual review', 'location': 'left amygdala', 'neurodata_type': 'ElectrodeGroup'}
general/extracellular_ephys/LAH/ {'description': 'depth electrode AHL (macro contact), AHL manual review', 'location': 'left anterior hippocampus', 'neurodata_type': 'ElectrodeGroup'}
general/extracellular_ephys/LEC/ {'description': 'depth electrode ECL (macro contact), ECL manual review', 'location': 'left entorhinal cortex', 'neurodata_type': 'ElectrodeGroup'}
general/extracellular_ephys/LPHC/ {'description': 'depth electrode PHCL (macro contact), PHCL manual review', 'location': 'left parahippocampal cortex', 'neurodata_type': 'ElectrodeGroup'}
general/extracellular_ephys/RA/ {'description': 'depth electrode AR (macro contact), AR manual review', 'location': 'right amygdala', 'neurodata_type': 'ElectrodeGroup'}
general/extracellular_ephys/RAH/ {'description': 'depth electrode AHR (macro contact), AHR manual review', 'location': 'right anterior hippocampus', 'neurodata_type': 'ElectrodeGroup'}
general/extracellular_ephys/REC/ {'description': 'depth electrode ECR (macro contact), ECR manual review', 'location': 'right entorhinal cortex', 'neurodata_type': 'ElectrodeGroup'}
general/extracellular_ephys/RPHC/ {'description': 'depth electrode PHCR (macro contact), PHCR manual review', 'location': 'right parahippocampal cortex', 'neurodata_type': 'ElectrodeGroup'}
general/extracellular_ephys/electrodes/ {'colnames': "['location' 'group' 'group_name' 'hemisphere' 'brain_region'\n 'bundle_index' 'csc_nr' 'x' 'y' 'z']", 'description': 'metadata about extracellular electrodes', 'neurodata_type': 'DynamicTable'}
ge
[... 87 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/scratch && . .venv/bin/activate && cat > inspect2.py <<'EOF'
import h5py, remfile, numpy as np
from dandi.dandiapi import DandiAPIClient
with DandiAPIClient() as c:
    ds=c.get_dandiset("001616","0.260702.0824")
    a=ds.get_asset_by_path("sub-1/sub-1_ses-sub1_ecephys.nwb")
    url=a.get_content_url(follow_redirects=1, strip_query=True)
f=h5py.File(remfile.File(url),'r')
d=lambda x: x.decode() if isinstance(x,bytes) else x
for k in ['session_description','identifier','session_start_time','timestamps_reference_time','general/experiment_description','general/institution','general/lab','general/session_id','general/related_publications','general/keywords','general/subject/age','general/subject/description','general/subject/sex','general/subject/species','general/subject/subject_id']:
    v=f[k][()]; print(k,'=',[d(x) for x in v] if hasattr(v,'__len__') and not isinstance(v,(bytes,str)) else d(v))
for p in ['units','processing/machine_learning/movie_annotations_indicator_functions','processing/machine_learning/movie_binning_info','stimulus/presentation/annotations_base','stimulus/presentation/annotations_patient_aligned','stimulus/presentation/cleaned_watchlogs','stimulus/presentation/raw_watchlogs','stimulus/presentation/movie_frame_times_analysis','stimulus/presentation/movie_frame_times_base']:
    print('\n##',p,':',d(f[p].attrs['description']))
    for k in f[p]:
        if isinstance(f[p][k],h5py.Dataset) and 'description' in f[p][k].attrs: print('  ',k,':',d(f[p][k].attrs['description']))
names=[d(x) for x in f['processing/machine_learning/movie_annotations_indicator_functions/label_name'][:]]
print('\nlabels:',names)
idx=f['processing/machine_learning/movie_annotations_indicator_functions/indicator_function_index'][:]
ind=f['processing/machine_learning/movie_annotations_indicator_functions/indicator_function'][:]
st=np.r_[0,idx]
for i,n in enumerate(names):
    v=ind[st[i]:st[i+1]]; print(f'{n:30s} len={len(v)} uniq={np.unique(v)} mean1={np.mean(v==1):.3f}')
EOF
python inspect2.py
```

```
session_description = Single unit activity and associated stimulus labels for movie viewing session of participant 1
identifier = 29be34f0-bff2-4bd1-abee-2dd6ed497a72
session_start_time = 2012-01-01T12:00:00+01:00
timestamps_reference_time = 2012-01-01T12:00:00+01:00
general/experiment_description = Single-neuron data recorded from Behnke-Fried microwires implanted in the human medial temporal lobe during the German-language presentation of a full-length movie (500 Days of Summer). This file also includes over 50 annotations of movie content.
general/institution = Universitätsklinikum Bonn (University Hospital Bonn)
general/lab = Mormann Lab at Universitätsklinikum Bonn (University Hospital Bonn)
general/session_id = sub1
general/related_publications = ['https://doi.org/10.7554/eLife.106758.1']
general/keywords = ['cognitive neuroscience', 'single units', 'human single neuron', 'human electrophysiology', 'amygdala', 'parahippocampal cortex', 'entorhinal cortex', 'hippocampus', 'movie', '500 Days of Summer', 'summer', 'open source', 'NWB']
general/subject/age = P54Y
general/subject/description = BF-implanted epilepsy patient
general/subject/sex = M
general/subject/species = Homo sapiens
general/subject/subject_id = 1

## units : Spike times (milliseconds), waveforms (uV), and associated spike sorting metrics for 1's movie session. Spike times are reference to the start of the movie, such that a spike time == 0 would indicate a spike at the exact onset of the movie.
   brain_region : brain region from which unit was recorded.
   cell_type : indicates if a given unit is a putative pyramidal cell or interneuron
   csc_nr : id for the electrode channel from which the unit was sorted, links to electrodes table
[... 105 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/scratch && . .venv/bin/activate && cat > load_all.py <<'EOF'
import h5py, remfile, numpy as np, pandas as pd, pickle, time
from concurrent.futures import ThreadPoolExecutor
from dandi.dandiapi import DandiAPIClient
d=lambda x: x.decode() if isinstance(x,bytes) else x
def ragged(g,name):
    data=g[name][:]; idx=g[name+'_index'][:]; st=np.r_[0,idx]; return [data[st[i]:st[i+1]] for i in range(len(idx))]
def load(path_url):
    path,url=path_url
    f=h5py.File(remfile.File(url),'r')
    u=f['units']
    out={'path':path}
    out['units']=pd.DataFrame({k:[d(x) for x in u[k][:]] for k in ['unit_id','csc_nr','brain_region','hemisphere','is_single_unit','peak_SNR','isi_violations','cv2','iso_dist','cell_type']})
    out['spikes']=ragged(u,'spike_times')
    out['subject']={k:d(f['general/subject/'+k][()]) for k in ['age','sex','subject_id','species']}
    out['session_id']=d(f['general/session_id'][()])
    out['session_start']=d(f['session_start_time'][()])
    for w in ['cleaned_watchlogs','raw_watchlogs']:
        g=f['stimulus/presentation/'+w]; out[w]=pd.DataFrame({'pts':g['pts'][:],'rec':g['neural_recording_time'][:]})
    for a in ['annotations_base','annotations_patient_aligned']:
        g=f['stimulus/presentation/'+a]; out[a]=pd.DataFrame({k:[d(x) for x in g[k][:]] if k=='label_name' else g[k][:] for k in ['start_time','stop_time','label_name','entry_index','value']})
    g=f['processing/machine_learning/movie_annotations_indicator_functions']
    names=[d(x) for x in g['label_name'][:]]; out['indicator']=dict(zip(names,ragged(g,'indicator_function')))
    g=f['processing/machine_learning/movie_binning_info']
    out['binning']={'bin_length':g['bin_length'][:],'edges':ragged(g,'edges'),'frames':[np.array([d(x) for x in r]) for r in ragged(g,'frames')]}
    out['frames_base']=f['stimulus/presentation/movie_frame_times_base/data'][:]
    out['frames_analysis']=f['stimulus/presentation/movie_frame_times_analysis/data'][:]
    out['electrodes']=pd.DataFrame({k:[d(x) for x in f['general/extracellular_ephys/electrodes/'+k][:]] for k in ['location','group_name','hemisphere','brain_region','csc_nr','x','y','z']})
    return out
t=time.time()
import sys
version=sys.argv[1]
with DandiAPIClient() as c:
    ds=c.get_dandiset("001616",version)
    assets=sorted((a.path,a.get_content_url(follow_redirects=1,strip_query=True)) for a in ds.get_assets())
with ThreadPoolExecutor(8) as ex: res=list(ex.map(load,assets))
print(time.time()-t)
pickle.dump(res,open(f'all_{version}.pkl','wb'))
EOF
python load_all.py 0.260702.0824
```

```
125.19934058189392
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/scratch && . .venv/bin/activate && cat > explore1.py <<'EOF'
import pickle, numpy as np, pandas as pd
res=pickle.load(open('all_0.260702.0824.pkl','rb'))
rows=[]
for r in res:
    u=r['units']; s=r['subject']
    rows.append({'path':r['path'],'sid':s['subject_id'],'age':s['age'],'sex':s['sex'],'n':len(u),**u.brain_region.value_counts().to_dict(),'single':int(u.is_single_unit.sum()),
                 'n_spk':sum(len(x) for x in r['spikes']),'spk_min':min(x.min() for x in r['spikes'] if len(x)),'spk_max':max(x.max() for x in r['spikes'] if len(x)),
                 'cw_n':len(r['cleaned_watchlogs']),'rw_n':len(r['raw_watchlogs']),'rec0':r['cleaned_watchlogs'].rec.iloc[0],'rec1':r['cleaned_watchlogs'].rec.iloc[-1],'pts0':r['cleaned_watchlogs'].pts.iloc[0],'pts1':r['cleaned_watchlogs'].pts.iloc[-1]})
df=pd.DataFrame(rows).fillna(0)
pd.set_option('display.width',250); pd.set_option('display.max_columns',40)
print(df.to_string())
print(df.n.sum(), df[[c for c in df.columns if c in ('A','H','EC','PHC','PIC','AH','MH','PH')]].sum().to_dict())
print('sex',df.sex.value_counts().to_dict(),'ages',sorted(df.age))
print(set(x for r in res for x in r['units'].brain_region))
print(res[0]['units'].head(10).to_string())
print(res[0]['electrodes'].to_string())
# same labels in all files?
ref=res[0]['indicator']
print('indicator identical across files:', all(all(np.array_equal(ref[k],r['indicator'][k]) for k in ref) and set(ref)==set(r['indicator']) for r in res))
print('annotations_base identical:', all(r['annotations_base'].equals(res[0]['annotations_base']) for r in res))
print('frames_base identical:', all(np.array_equal(r['frames_base'],res[0]['frames_base']) for r in res), res[0]['frames_base'][:3], res[0]['frames_base'][-1], len(res[0]['frames_analysis']), res[0]['frames_analysis'][[0,-1]])
b=res[0]['binning']; print(b['bin_length'], [len(e) for e in b['edges']], [len(f) for f in b['frames']], b['frames'][1][:3], b['edges'][1][:5])
EOF
python explore1.py
```

```
path sid   age sex    n    EC    AH     A   PHC  single    n_spk       spk_min       spk_max    cw_n    rw_n           rec0          rec1   pts0     pts1    PH   FF    LG   PIC  PRC    MH
0      sub-1/sub-1_ses-sub1_ecephys.nwb   1  P54Y   M   40  16.0  10.0   8.0   6.0      25   397655  4.462854e+00  8.244127e+06  120102  121266       0.000000  8.244131e+06   0.04  4803.84   0.0  0.0   0.0   0.0  0.0   0.0
1   sub-10/sub-10_ses-sub10_ecephys.nwb  10  P44Y   F  108  15.0  20.0  19.0  15.0      70  1809222  3.036416e+00  5.952549e+06  122996  122396       0.000000  5.952553e+06   0.04  4919.44  39.0  0.0   0.0   0.0  0.0   0.0
2   sub-11/sub-11_ses-sub11_ecephys.nwb  11  P62Y   M   31   0.0  14.0   2.0   4.0      12   362082  5.392670e+00  4.997858e+06  122820  122904   84731.238250  4.997893e+06  18.16  4930.88  11.0  0.0   0.0   0.0  0.0   0.0
3   sub-12/sub-12_ses-sub12_ecephys.nwb  12  P36Y   M   52  29.0  17.0   0.0   4.0      22   409441  3.276744e+00  5.015300e+06  121184  122650   19276.191000  5.015306e+06   0.04  4847.12   2.0  0.0   0.0   0.0  0.0   0.0
4   sub-13/sub-13_ses-sub13_ecephys.nwb  13  P41Y   M  137  26.0   8.0  34.0  19.0      86  1451503  1.515963e+00  4.887761e+06  121178  119681       0.000000  4.887761e+06   0.04  4847.08  44.0  6.0   0.0   0.0  0.0   0.0
5   sub-14/sub-14_ses-sub14_ecephys.nwb  14  P26Y   F   30   4.0   9.0   5.0  11.0       6   148301  5.713573e+01  4.957027e+06  120107  121898  139385.575500  4.957072e+06   0.04  4804.24   1.0  0.0   0.0   0.0  0.0   0.0
6   sub-15/sub-15_ses-sub15_ecephys.nwb  15  P35Y   F   97  23.0  13.0  35.0  19.0      46   674127  1.456136e+01  4.805150e+06  119518  119516       0.000000  4.805154e+06   0.04  4780.60   7.0  0.0   0.0   0.0  0.0   0.0
7   sub-16/sub-16_ses-sub16_ecephys.nwb  16  P31Y   F   67  17.0  25.0  14.0   0.0      25   528123  5.937316e+00  4.879582e+06  119679  119676       0.000000  4.879582e+06   0.04  4787.04  11.0  0.0   0.0   0.0  0.0   0.0
8   sub-17/sub-17_ses-sub17_
[... 54 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/scratch && . .venv/bin/activate && cat > explore2.py <<'EOF'
import pickle, numpy as np, pandas as pd, collections
res=pickle.load(open('all_0.260702.0824.pkl','rb'))
grp=collections.Counter(); reg=collections.Counter(); cross=collections.Counter()
for r in res:
    e=r['electrodes'].set_index('csc_nr'); u=r['units']
    g=u.csc_nr.map(e.group_name); el=u.csc_nr.map(e.brain_region)
    for a,b,c in zip(g,u.brain_region,el): cross[(a[1:] if a[0] in 'LR' else a, b)]+=1; 
    assert (el==u.brain_region).all() or print(r['path'],'unit region != electrode region', (el!=u.brain_region).sum())
print(sorted(cross.items()))
fa=res[0]['frames_analysis']
for r in res:
    cw=r['cleaned_watchlogs']; rw=r['raw_watchlogs']
    pts=cw.pts.values; rec=cw.rec.values
    d=np.diff(pts); dr=np.diff(rec)
    cover=np.isin(np.round(fa,2),np.round(pts,2)).mean()
    rd=np.diff(rw.pts.values)
    print(r['path'].split('/')[0], f"cover={cover:.4f} pts_rep={np.sum(d==0)} pts_back={np.sum(d<0)} jumps>0.05={np.sum(d>0.05)} rec_dt_med={np.median(dr):.2f} rec_dt_max={dr.max():.0f} raw_rep={np.sum(rd==0)} raw_back={np.sum(rd<0)} raw_jump={np.sum(rd>0.05)} rec_back={np.sum(dr<0)}")
EOF
python explore2.py
```

```
[(('A', 'A'), 464), (('AH', 'AH'), 359), (('AHa', 'AH'), 32), (('AHb', 'AH'), 27), (('Aa', 'A'), 49), (('Ab', 'A'), 46), (('EC', 'EC'), 391), (('ECa', 'EC'), 71), (('ECb', 'EC'), 20), (('ECc', 'EC'), 11), (('FF', 'FF'), 6), (('LG', 'LG'), 15), (('MH', 'MH'), 16), (('PH', 'PH'), 328), (('PHC', 'PHC'), 273), (('PHCa', 'PHC'), 11), (('PHCb', 'PHC'), 9), (('PHa', 'PH'), 46), (('PHb', 'PH'), 38), (('PIC', 'PIC'), 68), (('PRC', 'PRC'), 6)]
sub-1 cover=1.0000 pts_rep=6 pts_back=0 jumps>0.05=0 rec_dt_med=41.00 rec_dt_max=2438262 raw_rep=4 raw_back=39 raw_jump=7 rec_back=0
sub-10 cover=1.0000 pts_rep=11 pts_back=0 jumps>0.05=1 rec_dt_med=41.02 rec_dt_max=615504 raw_rep=6 raw_back=0 raw_jump=23 rec_back=0
sub-11 cover=1.0000 pts_rep=1 pts_back=0 jumps>0.05=0 rec_dt_med=41.01 rec_dt_max=425 raw_rep=0 raw_back=0 raw_jump=20 rec_back=0
sub-12 cover=1.0000 pts_rep=6 pts_back=0 jumps>0.05=0 rec_dt_med=41.01 rec_dt_max=69008 raw_rep=2 raw_back=17 raw_jump=43 rec_back=0
sub-13 cover=1.0000 pts_rep=2 pts_back=0 jumps>0.05=1 rec_dt_med=41.02 rec_dt_max=36275 raw_rep=0 raw_back=0 raw_jump=66 rec_back=0
sub-14 cover=1.0000 pts_rep=1 pts_back=0 jumps>0.05=0 rec_dt_med=41.02 rec_dt_max=13445 raw_rep=1 raw_back=2 raw_jump=21 rec_back=0
sub-15 cover=1.0000 pts_rep=3 pts_back=0 jumps>0.05=0 rec_dt_med=40.69 rec_dt_max=14243 raw_rep=2 raw_back=0 raw_jump=1 rec_back=0
sub-16 cover=1.0000 pts_rep=3 pts_back=0 jumps>0.05=0 rec_dt_med=40.69 rec_dt_max=41669 raw_rep=1 raw_back=0 raw_jump=1 rec_back=0
sub-17 cover=1.0000 pts_rep=1 pts_back=0 jumps>0.05=0 rec_dt_med=40.68 rec_dt_max=26893 raw_rep=1 raw_back=0 raw_jump=1 rec_back=0
sub-18 cover=1.0000 pts_rep=4 pts_back=0 jumps>0.05=0 rec_dt_med=40.68 rec_dt_max=134676 raw_rep=1 raw_back=0 raw_jump=0 rec_back=0
sub-19 cover=1.0000 pts_rep=5 pts_back=0 jumps>0.05=0 rec_dt_med=40.68 rec_dt_max=131290 raw_rep=5 raw_back=0 raw_jump=0 rec_back=0
sub-2 cover=1.0000 pts_rep=3 pts_back=0 jumps>0.05=0 rec_dt_med=41.04 rec_dt_max=794009 raw_rep=4 raw_back=29 r
[... 18 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/scratch && . .venv/bin/activate && cat > oldver.py <<'EOF'
import h5py, remfile, numpy as np, pandas as pd, collections
from concurrent.futures import ThreadPoolExecutor
from dandi.dandiapi import DandiAPIClient
d=lambda x: x.decode() if isinstance(x,bytes) else x
with DandiAPIClient() as c:
    ds=c.get_dandiset("001616","0.260519.1133")
    assets=sorted((a.path,a.get_content_url(follow_redirects=1,strip_query=True)) for a in ds.get_assets() if 'behavior+ecephys' in a.path)
def top(pu):
    p,u=pu; f=h5py.File(remfile.File(u),'r')
    keys=[]; f.visit(keys.append)
    un=f['units']; cols=list(un.keys())
    br=[d(x) for x in un['brain_region'][:]] if 'brain_region' in un else None
    loc=None
    sp=un['spike_times'][:]; idx=un['spike_times_index'][:]
    return p, keys, cols, br, len(idx), sp[:idx[0]][:5], d(f['general/subject/subject_id'][()])
with ThreadPoolExecutor(8) as ex: out=list(ex.map(top,assets))
print(len(out)); print('\n'.join(k for k in out[0][1] if not k.startswith('specifications')))
cnt=collections.Counter(); tot=0
for p,keys,cols,br,n,s,sid in out:
    tot+=n; cnt.update(br)
    print(p,n,sid,s)
print(tot,cnt)
EOF
python oldver.py 2>&1 | tail -80
```

```
stimulus/presentation/annotations_base/value
stimulus/presentation/annotations_patient_aligned
stimulus/presentation/annotations_patient_aligned/entry_index
stimulus/presentation/annotations_patient_aligned/id
stimulus/presentation/annotations_patient_aligned/label_name
stimulus/presentation/annotations_patient_aligned/start_time
stimulus/presentation/annotations_patient_aligned/stop_time
stimulus/presentation/annotations_patient_aligned/value
stimulus/presentation/cleaned_watchlogs
stimulus/presentation/cleaned_watchlogs/id
stimulus/presentation/cleaned_watchlogs/neural_recording_time
stimulus/presentation/cleaned_watchlogs/pts
stimulus/presentation/movie_frame_times_analysis
stimulus/presentation/movie_frame_times_analysis/data
stimulus/presentation/movie_frame_times_analysis/starting_time
stimulus/presentation/movie_frame_times_base
stimulus/presentation/movie_frame_times_base/data
stimulus/presentation/movie_frame_times_base/starting_time
stimulus/presentation/raw_watchlogs
stimulus/presentation/raw_watchlogs/id
[... 61 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/scratch && . .venv/bin/activate && cat > bin_test.py <<'EOF'
import pickle, numpy as np, pandas as pd, time
res=pickle.load(open('all_0.260702.0824.pkl','rb'))
b=res[0]['binning']; i80=list(b['bin_length']).index(80)
edges=b['edges'][i80]; frames=b['frames'][i80]
print(len(edges), edges[:3], edges[-3:], frames[:2], frames[-2:])
def to_movie_time(spk, cw):
    pts=cw.pts.values; rec=cw.rec.values
    pause=np.where(np.diff(pts)==0)[0]
    keep=np.ones(len(spk),bool)
    for i in pause: keep &= ~((spk>rec[i])&(spk<rec[i+1]))
    keep &= (spk>=rec[0])&(spk<=rec[-1])
    return np.interp(spk[keep],rec,pts)
t=time.time()
X=[]; meta=[]
for r in res:
    cw=r['cleaned_watchlogs']; pts=cw.pts.values
    j=np.where(np.diff(pts)>0.05)[0]
    if len(j): print(r['path'].split('/')[0],'jumps',[(pts[k],pts[k+1]) for k in j])
    for k,s in enumerate(r['spikes']):
        X.append(np.histogram(to_movie_time(s,cw),edges)[0])
        meta.append((r['subject']['subject_id'],k,r['units'].brain_region[k]))
X=np.array(X,dtype=np.int16); print(X.shape, time.time()-t, X.sum(1).min(), np.median(X.sum(1)/ (edges[-1]-edges[0])))
np.save('X80.npy',X); pd.DataFrame(meta,columns=['sid','k','region']).to_csv('meta.csv',index=False)
EOF
python bin_test.py
```

```
59081 [36.72 36.8  36.88] [4762.96 4763.04 4763.12] ['frame_000919.jpg' 'frame_000921.jpg'] ['frame_119075.jpg' 'frame_119077.jpg']
sub-10 jumps [(np.float64(0.04), np.float64(0.12))]
sub-13 jumps [(np.float64(0.04), np.float64(0.12))]
sub-25 jumps [(np.float64(0.04), np.float64(0.16))]
sub-27 jumps [(np.float64(0.04), np.float64(0.12))]
sub-28 jumps [(np.float64(0.04), np.float64(0.12))]
sub-3 jumps [(np.float64(0.04), np.float64(0.12))]
sub-9 jumps [(np.float64(0.04), np.float64(0.12))]
(2286, 59080) 5.0937278270721436 0 0.916976980365606
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/scratch && . .venv/bin/activate && cat > lr_test.py <<'EOF'
import pickle, numpy as np, pandas as pd, time, math
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import cohen_kappa_score
X=np.load('X80.npy').astype(np.float32); n=X.shape[1]
cs=np.cumsum(np.pad(X,((0,0),(1,0))),axis=1)
k=np.arange(n); lo=np.clip(k-10,0,n); hi=np.clip(k+10,0,n)
S=(cs[:,hi]-cs[:,lo]).T  # samples x units
res=pickle.load(open('all_0.260702.0824.pkl','rb'))
fr=np.array([int(f.split('_')[1][:-4]) for f in res[0]['binning']['frames'][1]])
ind=res[0]['indicator']['summer']; y=ind[fr-1]
def split(n,fold,parts=11,buf_bins=420):
    base=int(n/parts); fl=int((base-5*buf_bins)/5); tr=[];va=[];te=[]
    for p in range(parts):
        i=p*base; F=[np.arange(i+j*(fl+buf_bins), i+j*(fl+buf_bins)+fl) for j in range(5)]; B=[np.arange(i+j*(fl+buf_bins)+fl, i+(j+1)*(fl+buf_bins)) for j in range(5)]
        f=fold-1; t,v=F[f],F[(f+1)%5]
        rest=[(f+2)%5,(f+3)%5,(f+4)%5]
        trn=np.concatenate([F[rest[0]],B[rest[0]],F[rest[1]],B[rest[1]],F[rest[2]]]) 
        tr.append(trn);va.append(v);te.append(t)
    return np.concatenate(tr),np.concatenate(va),np.concatenate(te)
tr,va,te=split(n,1); print(len(tr),len(va),len(te))
mu=S[tr].mean(0); sd=S[tr].std(0); sd[sd==0]=1
Z=(S-mu)/sd
for C in [0.001,0.003,0.01,0.03]:
    t=time.time(); m=LogisticRegression(penalty='l1',solver='liblinear',C=C,class_weight='balanced').fit(Z[tr],y[tr])
    print(C, f"{time.time()-t:.1f}s", 'nz',(m.coef_!=0).sum(), 'val',round(cohen_kappa_score(y[va],m.predict(Z[va])),3),'test',round(cohen_kappa_score(y[te],m.predict(Z[te])),3))
EOF
python lr_test.py
```

```
/tmp/claude-1001/scratch/.venv/lib/python3.12/site-packages/sklearn/linear_model/_logistic.py:1381: FutureWarning: 'penalty' was deprecated in version 1.8 and will be removed in 1.10. To avoid this warning, leave 'penalty' set to its default value and use 'l1_ratio' or 'C' instead. Use l1_ratio=0 instead of penalty='l2', l1_ratio=1 instead of penalty='l1', l1_ratio set to a float between 0 and 1 instead of penalty='elasticnet', and C=np.inf instead of penalty=None.
  warnings.warn(
/tmp/claude-1001/scratch/.venv/lib/python3.12/site-packages/sklearn/linear_model/_logistic.py:1407: UserWarning: Inconsistent values: penalty=l1 with l1_ratio=0.0. penalty is deprecated. Please use l1_ratio only.
  warnings.warn(
/tmp/claude-1001/scratch/.venv/lib/python3.12/site-packages/sklearn/linear_model/_logistic.py:1381: FutureWarning: 'penalty' was deprecated in version 1.8 and will be removed in 1.10. To avoid this warning, leave 'penalty' set to its default value and use 'l1_ratio' or 'C' instead. Use l1_ratio=0 instead of penalty='l2', l1_ratio=1 instead of penalty='l1', l1_ratio set to a float between 0 and 1 instead of penalty='elasticnet', and C=np.inf instead of penalty=None.
  warnings.warn(
/tmp/claude-1001/scratch/.venv/lib/python3.12/site-packages/sklearn/linear_model/_logistic.py:1407: UserWarning: Inconsistent values: penalty=l1 with l1_ratio=0.0. penalty is deprecated. Please use l1_ratio only.
  warnings.warn(
/tmp/claude-1001/scratch/.venv/lib/python3.12/site-packages/sklearn/linear_model/_logistic.py:1381: FutureWarning: 'penalty' was deprecated in version 1.8 and will be removed in 1.10. To avoid this warning, leave 'penalty' set to its default value and use 'l1_ratio' or 'C' instead. Use l1_ratio=0 instead of penalty='l2', l1_ratio=1 instead of penalty='l1', l1_ratio set to a float between 0 and 1 instead of penalty='elasticnet', and C=np.inf instead of penalty=None.
  warnings.warn(
/tmp/claude-1001/scratch/.venv/lib/python3.12/site-packages/sklearn/linear_mode
[... 11 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/scratch && . .venv/bin/activate && python -c "
import pickle,numpy as np,pandas as pd
res=pickle.load(open('all_0.260702.0824.pkl','rb'))
a=res[0]['annotations_base']; pa=res[0]['annotations_patient_aligned']
for l in ['indoor-setting','camera-cuts','scenes','summer','persons','mckenzie','summer-presence','tom-faces']:
    s=a[a.label_name==l]; print(l, len(s), s.value.value_counts().to_dict(), (s.stop_time-s.start_time).describe()[['min','50%','max']].round(3).to_dict()); print(s.head(4).to_string())
print(pa[pa.label_name=='summer'].head(4).to_string())
ind=res[0]['indicator']
print('indoor vals', pd.Series(ind['indoor-setting']).value_counts().to_dict())
cc=ind['camera-cuts']; print('cc onsets', np.sum(np.diff(cc)==1), 'scene onsets', np.sum(np.diff(ind['scenes'])==1))
# is scenes subset of camera cuts?
print('scenes&cc', np.sum((ind['scenes']==1)&(cc==1)), np.sum(ind['scenes']==1))
print('faces subset of char', np.sum((ind['summer-faces']==1)&(ind['summer']==0)), np.sum((ind['tom-faces']==1)&(ind['tom']==0)))
"
```

```
indoor-setting 100 {0: 50, 1: 44, 99: 6} {'min': 1.056, '50%': 18.081, 'max': 424.862}
      start_time   stop_time      label_name  entry_index  value
2092    0.000000   21.941999  indoor-setting            1      0
2093   21.982000   36.606998  indoor-setting            2     99
2094   36.646999   69.267998  indoor-setting            3      0
2095   69.307999  121.018997  indoor-setting            4      1
camera-cuts 1917 {0: 959, 1: 958} {'min': 0.039, '50%': 0.559, 'max': 266.52}
    start_time  stop_time   label_name  entry_index  value
62        0.00      1.119  camera-cuts            1      0
63        1.12      1.159  camera-cuts            2      1
64        1.16      1.719  camera-cuts            3      0
65        1.72      1.759  camera-cuts            4      1
scenes 267 {0: 134, 1: 133} {'min': 0.039, '50%': 1.079, 'max': 396.599}
      start_time  stop_time label_name  entry_index  value
3495    0.000000  23.358999     scenes            1      0
3496   23.360001  23.399000     scenes            2      1
3497   23.400000  36.639000     scenes            3      0
3498   36.639999  36.679001     scenes            4      1
summer 283 {0: 142, 1: 141} {'min': 0.039, '50%': 4.959, 'max': 466.84}
      start_time   stop_time label_name  entry_index  value
[... 38 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/SUMMER; sed -n 120,275p visualization/plot_code/responsive_units/utils/calc_cluster_permutation.py; grep -n "alpha\|identify_responses\|cluster\|zeta\|onset\|key=" visualization/plot_code/responsive_units/plot_responsive_units.ipynb | head -60
```

```
if len(clus_collection.keys()) == 0:
        cluster_sum = 0
        cluster_inds = []
        
        if mode == "maxsum":
            return cluster_sum, cluster_inds
        elif mode == "all":
            return [], [], []
        
    else:
        
        if mode == "maxsum":
            ## continuing with algo as specified in the original paper
            
            #step 4: Calculate cluster-level statistics by taking the sum of the t-values within a cluster
            sums = []
            for clus_id in clus_collection.keys():
                if verbose:
                    print(clus_id)
                    print(sum(gt_stats[clus_collection[clus_id]]))
[... 160 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/SUMMER; python - <<'EOF'
import json
nb=json.load(open('visualization/plot_code/responsive_units/plot_responsive_units.ipynb'))
for c in nb['cells'][:25]:
    if c['cell_type']=='code': print('----\n'+''.join(c['source'])[:1500])
EOF
grep -n "def \|annotation\|patient_aligned\|spike_times" visualization/plot_code/nwb_io.py | head -40
```

```
----
import sys
import os
from collections import Counter
from pathlib import Path

import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
from matplotlib import rc
import matplotlib.gridspec as gridspec
import seaborn as sns
from tabulate import tabulate
from nilearn.plotting import plot_markers

PROJECT_ROOT = Path(os.getcwd()).resolve().parents[2]
sys.path.insert(0, str(PROJECT_ROOT))

from visualization.plot_code.config_plot_params import *
[... 375 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/SUMMER; grep -rn "REGION_ALTERNATIVE_NAMES\s*=" -A8 --include=*.py . ; sed -n 118,160p visualization/plot_code/nwb_io.py; grep -rn "373\|580\|794\|440\b" --include=*.ipynb --include=*.py . | head
```

```
./visualization/plot_code/nwb_io.py:19:REGION_ALTERNATIVE_NAMES = {"PHC": ["PHC", "APH", "PPH", "MPH"],
./visualization/plot_code/nwb_io.py-20-                            "A": ["A"],
./visualization/plot_code/nwb_io.py-21-                            "EC": ["EC"],
./visualization/plot_code/nwb_io.py-22-                            "PIC": ["PIC"],
./visualization/plot_code/nwb_io.py-23-                            "H": ["H", "AH", "MH", "PH"]} 
./visualization/plot_code/nwb_io.py-24-
./visualization/plot_code/nwb_io.py-25-#####
./visualization/plot_code/nwb_io.py-26-# Collection within patients
./visualization/plot_code/nwb_io.py-27-#####
def collect_all_spike_data_in_region(data_dir, region, region_name_dict=REGION_ALTERNATIVE_NAMES, drop_waveforms=True):
    """
    Collect unitwise data from NWB files for a given region.

    Args:
        data_dir (pathlib object, string-like): path to the parent directory containing nwb files
        region (string): region abbreviation (e.g., 'PHC' for parahippocampal cortex)
        region_name_dict (dict, optional): Defaults to REGION_ALTERNATIVE_NAMES.

    Returns:
        pandas DataFrames: DataFrame containing collected unit data
[... 41 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/SUMMER; python - <<'EOF'
import json
for p in ['visualization/plot_code/decoding_results/decoding_results/notebooks/decoding_performance.ipynb','visualization/plot_code/decoding_results/subregions/notebooks/performance.ipynb','visualization/plot_code/decoding_results/buffer_lengths/notebooks/comparison_performance.ipynb']:
    nb=json.load(open(p)); print('=====',p)
    for c in nb['cells']:
        if c['cell_type']=='code':
            s=''.join(c['source'])
            if any(ch.isdigit() for ch in s) and ('=' in s) and ('[' in s): print('----\n'+s[:3500])
EOF
cat visualization/plot_code/decoding_results/subregions/config_characters.py visualization/plot_code/decoding_results/decoding_results/config_decoding.py | head -80
```

```
===== visualization/plot_code/decoding_results/decoding_results/notebooks/decoding_performance.ipynb
----
import sys
import os
import numpy as np
from pathlib import Path

PROJECT_ROOT = Path(os.getcwd()).resolve().parents[4]
sys.path.insert(0, str(PROJECT_ROOT))
from visualization.plot_code.config_colors import *
import visualization.plot_code.decoding_results.decoding_results.notebooks.utils as utils
----
# Structure: (Kappa, f1, pr_auc, auroc)
labels = ["Summer", "Tom", "McKenzie", "Persons", "Scene Cuts", "Camera Cuts", "Days of Summer", "Indoor"]

summer = [0.3086222559, 0.6510404478, 0.6955660462, 0.7089385748]
#summer_std = [0.1101072593, 0.0421847961, 0.0886701569, 0.0785379818]
summer_err = [0.05505363, 0.021092398, 0.044335078, 0.039268991]
summer_baseline = [0, 0, 0, 0.5]

[... 230 more lines not kept]
```

**Agent**

Now I have what I need to write the claims. Before that, a quick check of whether the code's ZETA test is fast enough to run as a variant.

**Agent calls Bash**

```bash
cd $TMPDIR/scratch && . .venv/bin/activate && uv pip install -q zetapy 2>&1 | tail -1; python - <<'EOF'
import pickle, numpy as np, time
from zetapy import zetatest
res=pickle.load(open('all_0.260702.0824.pkl','rb'))
r=res[0]; a=r['annotations_patient_aligned']; c=a[(a.label_name=='camera-cuts')&(a.value==1)]
st=c.start_time.values; sp=c.stop_time.values
on=[st[i] for i in range(1,len(st)) if st[i]-1000>sp[i-1]]
print(len(on))
s=r['spikes'][3]
t=time.time(); z=zetatest(s/1000,np.array(on)/1000,1,resampling_number=1000); print(time.time()-t, z[0])
t=time.time(); z=zetatest(s/1000,np.array(on)/1000,1,resampling_number=100); print(time.time()-t, z[0])
EOF
```

```
900
5.043921709060669 0.25327528874017546
0.5164828300476074 0.2206296157464045
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd  cat schemas/claims.schema.json | head -120; python -c "
import json;s=json.load(open('schemas/attempt.schema.json'));print(json.dumps(s,indent=1)[:5000])"
```

```
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "Claims proposed for one target (a dandiset and one of its papers)",
  "description": "Draft. To be revised after the pilot.",
  "type": "object",
  "additionalProperties": false,
  "required": [
    "schema_version",
    "dandiset",
    "paper",
    "claims"
  ],
  "properties": {
    "schema_version": {
      "const": 1
    },
    "dandiset": {
      "type": "string",
      "pattern": "^[0-9]{6}$"
    },
[... 309 more lines not kept]
```

**Agent**

Writing the claims file now, before running any claim's analysis.

**Agent calls Write**

```json
{
 "file_path": "claims/001616/10.7554-elife.106758.1.yaml",
 "content": "# Claims for Gerken, Darcher et al., \"Decoding movie content from neuronal population activity in\n# the human medial temporal lobe\", eLife reviewed preprint 106758 version 1, on dandiset 001616.\n# Source: the full text of the reviewed preprint (open access, from the eLife API) and its\n# supplementary file 598791_file03.pdf (Tables S1 and S2).\n#\n# When these criteria were written, the author had seen the data check only: the file list and\n# metadata of both published versions, the contents of every file, the units per patient and per\n# brain region, the subjects' sex and age, the annotations and watchlogs, and the label counts.\n# While timing the logistic regression on one fold for the label Summer, the author also saw that\n# fold's validation and test kappa (validation 0.26 to 0.30, test 0.42 to 0.48 over four values\n# of C). No other claim's analysis had been run. The author had read the dataset's code (GitHub\n# mormannlab/SUMMER at commit 59fc242), including the values its plotting notebooks hold for the\n# LSTM results by region and by gap size.\n#\n# Method choices fixed here, where the Methods leave them open:\n# - Time base. Spikes (milliseconds, recording clock) are mapped to movie time through the cleaned\n#   watchlog of each patient; spikes during pauses (repeated presentation timestamps) are dropped.\n# - Responsive neurons (Methods, after Mormann et al. 2008). Pseudo-trials are label onsets in the\n#   movie annotations preceded by at least 1000 ms without the label; for labels with a duration\n#   (not camera or scene cuts) the label must also last at least 1000 ms (Results). Baseline is\n#   the spike count from -1000 to 0 ms divided by 10; the stimulus period is 19 overlapping 100 ms\n#   bins starting every 50 ms from 0 to 900 ms. Each bin is compared with the baseline across\n#   pseudo-trials by a two-sided Wilcoxon signed-rank test, and the 19 p-values are combined by\n#   Simes' procedure. A neuron that spikes in fewer than a third of the pseudo-trials gets p = 1.\n#   The paper states two thresholds (Methods alpha 0.01; Results, Figure 2 and Table S1 0.001);\n#   both are readings. The dataset's code uses the ZETA test instead; it is shown as a variant.\n# - Regions are the dandiset's `brain_region` per unit. H is AH, MH and PH together, as in the\n#   dataset's code (REGION_ALTERNATIVE_NAMES). FF, LG and PRC are outside the paper's regions.\n# - Decoding samples are the 80 ms bins of the analysis portion of the film given in\n#   `movie_binning_info` (credits excluded), each labelled by its first frame. Camera and scene\n#   cut labels are set to 1 for frames within 520 ms after a cut onset (Methods, for camera cuts;\n#   applied to scene cuts too). For Indoor/Outdoor, indoor is 1, outdoor 0, and frames marked 99\n#   are left out. Splits follow the dataset's code (ML_framework/dataloader.py) with a 32 s gap\n#   plus the 1.6 s window, which gives 30822, 7194 and 7194 samples, as the paper's 30800, 7200 and\n#   7200; fold f is the test set and fold f+1 the validation set.\n# - Logistic regression (Methods): the summed spike count of each neuron from 800 ms before to\n#   800 ms after the bin, z-scored with training statistics, L1 penalty, liblinear solver,\n#   class weights balanced (the paper oversamples the minority class), C chosen on the validation\n#   kappa from 0.001, 0.003, 0.01 and 0.03, prediction at probability 0.5. Performance is\n#   Cohen's kappa on the test set, mean and SEM over the five folds. Chance is tested by shuffling\n#   the test labels 1000 times (Methods).\nschema_version: 1\ndandiset: \"001616\"\npaper: doi:10.7554/elife.106758.1\nclaims:\n- id: dataset-composition\n  statement: The data are 2286 single and multi-units from 29 patients (17 female), 30 to 137 units\n    per patient, in the amygdala (580), hippocampus (794), entorhinal cortex (440), parahippocampal\n    cortex (373) and piriform cortex (99).\n  source: Results, first paragraph; Figure 1d; Patient-wise decoding performance\n  expected:\n  - quantity: patients\n    value: 29\n    tolerance: 0\n  - quantity: units\n    value: 2286\n    tolerance: 0\n  - quantity: female patients\n    value: 17\n    tolerance: 0\n  - quantity: units in the amygdala\n    value: 580\n    tolerance: 58\n  - quantity: units in the hippocampus\n    value: 794\n    tolerance: 79.4\n  - quantity: units in the entorhinal cortex\n    value: 440\n    tolerance: 44\n  - quantity: units in the parahippocampal cortex\n    value: 373\n    tolerance: 37.3\n  - quantity: units in the piriform cortex\n    value: 99\n    tolerance: 9.9\n  criterion: Counts of patients, units and female patients are exact, as the dandiset should hold\n    the recordings the paper analysed. Regions as fixed in the opening comment. Reproduced when\n    every value is within tolerance and units per patient range from 30 to 137; partially\n    reproduced when the patient, unit and sex counts match but a region count does not; not\n    reproduced when the patient or unit count differs.\n- id: fig2b-phc-camera-cuts\n  statement: Over half of the parahippocampal neurons responded to camera cuts (193 of 373, 51.74%).\n  source: Results, Stimulus-aligned responsive neurons; Figure 2b; Table S1\n  expected:\n    quantity: fraction of PHC units responsive to camera cuts\n    value: 51.74\n    tolerance: 5.17\n    unit: percent\n  criterion: Responsive neurons by the Methods' test as fixed in the opening comment. The fraction\n    is compared, as the dandiset's PHC count differs from the paper's; the count is reported\n    against 193. Readings are alpha 0.001 and alpha 0.01; reproduced when the fraction is within\n    tolerance under either; partially reproduced when it is outside tolerance but above 25% under\n    either; not reproduced otherwise.\n- id: tables1-camera-cuts-regions\n  statement: Camera cuts evoked responses in a large share of neurons in every region (amygdala\n    46.90%, entorhinal cortex 45.68%, hippocampus 38.92%).\n  source: Table S1; Results, Stimulus-aligned responsive neurons\n  depends_on:\n  - fig2b-phc-camera-cuts\n  expected:\n  - quantity: fraction of A units responsive to camera cuts\n    value: 46.90\n    tolerance: 4.69\n    unit: percent\n  - quantity: fraction of EC units responsive to camera cuts\n    value: 45.68\n    tolerance: 4.57\n    unit: percent\n  - quantity: fraction of H units responsive to camera cuts\n    value: 38.92\n    tolerance: 3.89\n    unit: percent\n  criterion: Same test and readings as fig2b-phc-camera-cuts. Reproduced when all three fractions\n    are within tolerance under one reading; partially reproduced when not, but every region has\n    more than 25% responsive units under one reading; not reproduced otherwise.\n- id: fig2b-phc-scene-cuts\n  statement: Few parahippocampal neurons responded to scene cuts (25 of 373, 6.70%), but the\n    modulation was consistent across the responsive neurons (cluster permutation test, p = 0.018).\n  source: Results, Stimulus-aligned responsive neurons; Figure 2b; Table S1\n  expected:\n    quantity: fraction of PHC units responsive to scene cuts\n    value: 6.70\n    tolerance: 2.54\n    unit: percent\n  criterion: The tolerance is the 95% binomial interval of a proportion of 6.70% among the paper's\n    373 units (1.96 times the standard error); 10% of the value (0.67 points) is smaller than the\n    sampling error of a count of 25. Readings alpha 0.001 and 0.01. The cluster permutation test\n    as in the Methods (z-scored trial-averaged rate per unit in 100 ms bins from -1000 to 1000 ms,\n    two-sided independent t-test per bin between responsive and non-responsive units, clusters of\n    adjacent bins with p < 0.005, summed absolute t, 1000 permutations of the unit labels,\n    p of a cluster the fraction of permutations whose largest cluster sum exceeds it).\n    Reproduced when, under one reading, the fraction is within tolerance and the largest cluster\n    has p < 0.05; partially reproduced when one of the two holds; not reproduced otherwise.\n- id: tables1-few-semantic-responses\n  statement: Only a few neurons responded to the onset of semantic features (Summer 46, Tom 216,\n    Persons 6 and Outdoor 4 of 2286 neurons), in contrast to camera cuts (1025).\n  source: Abstract; Results, Stimulus-aligned responsive neurons; Table S1\n  expected:\n  - quantity: units responsive to Summer\n    value: 46\n    tolerance: 13.2\n  - quantity: units responsive to Tom\n    value: 216\n    tolerance: 21.6\n  criterion: The tolerance for Summer is the 95% binomial interval of 46 among 2286 units (10% of\n    46 is smaller than its sampling error); for Tom 10%. Readings alpha 0.001 and 0.01. Reproduced\n    when, under one reading, both counts are within tolerance and every semantic label tested\n    (Summer, Tom, McKenzie, Persons, Indoor, Outdoor, Summer Presence) has fewer than 10% of all\n    units responsive while camera cuts have more than 25%; partially reproduced when that contrast\n    holds but a count is outside tolerance; not reproduced otherwise.\n- id: tables1-no-indoor-response\n  statement: No neuron responded to the onset of indoor scenes.\n  source: Results, Stimulus-aligned responsive neurons; Table S1\n  criterion: A claim of absence, judged on the paper's test at alpha 0.001, the threshold stated in\n    the same Results paragraph. Reproduced when no unit is responsive to Indoor onsets; not\n    reproduced when any is. The count at alpha 0.01 and the counts for McKenzie and Summer\n    Presence (also 0 in Table S1) are reported as variants.\n- id: results-cluster-regions\n  statement: By the cluster permutation test, parahippocampal neurons responded to the largest set\n    of features (Summer, Persons, Camera Cuts, Scene Cuts, Outdoor), compared with the hippocampus\n    (Tom, Camera Cuts, Outdoor), the amygdala (Camera Cuts) and the entorhinal cortex (none).\n  source: Results, Stimulus-aligned responsive neurons\n  depends_on:\n  - fig2b-phc-camera-cuts\n  criterion: The cluster test of fig2b-phc-scene-cuts is run for 8 labels (Summer, Tom, McKenzie,\n    Persons, Camera Cuts, Scene Cuts, Indoor, Outdoor) in 4 regions (A, H, EC, PHC); a cell is\n    significant when its largest cluster has p < 0.05; with fewer than 2 responsive units a cell\n    is not significant. Readings alpha 0.001 and 0.01 for the responsive split. Reproduced when,\n    under one reading, at least 28 of the 32 cells agree with the paper's list and PHC has the\n    most significant labels; partially reproduced when one of the two holds or at least 24 cells\n    agree; not reproduced otherwise.\n- id: fig3b-single-neuron-threshold\n  statement: Thresholding the activity of single neurons does not reliably predict whether Summer\n    is on screen; most neurons perform near chance, below the population decoder.\n  source: Results, Decoding from neuronal activity; Figure 3b; Methods, Single-neuron decoding\n    performance\n  criterion: For each unit, the summed spike count from 800 ms before to 800 ms after each sample;\n    on each fold's validation set the threshold and its direction (above or below) that maximise\n    kappa among up to 50 quantiles of the counts; kappa of that rule on the test set, averaged\n    over the five folds. Reproduced when the median unit's kappa is below 0.05 and no unit reaches\n    the paper's population kappa for Summer (0.31); partially reproduced when one of the two holds;\n    not reproduced otherwise.\n- id: fig3c-logreg-characters-location\n  statement: A logistic regression on spike counts decodes characters and location about as well as\n    the LSTM; pooled over patients it reaches kappa 0.28 for Summer and 0.31 for Indoor/Outdoor.\n  source: Results, Choice of architecture and Patient-wise decoding performance; Figure 3c; Figure 4a\n  expected:\n  - quantity: kappa for Summer, logistic regression, pooled\n    value: 0.28\n    tolerance: 0.055\n  - quantity: kappa for Indoor/Outdoor, logistic regression, pooled\n    value: 0.31\n    tolerance: 0.060\n  criterion: The tolerances are the SEMs over folds the paper gives for these labels (Table S2,\n    LSTM), the nearest stated spread, as the paper gives none for the logistic regression. The\n    logistic regression as fixed in the opening comment. Reproduced when both values are within\n    tolerance and Tom, McKenzie and Persons each reach at least the LSTM value less its SEM (0.17,\n    0.235, 0.312); partially reproduced when 3 or 4 of these 5 conditions hold; not reproduced\n    otherwise. Permutation p-values per fold are reported.\n- id: fig3c-logreg-cuts-lower\n  statement: For scene and camera cuts the logistic regression performs below the LSTM, by 0.1 and\n    0.07, that is about kappa 0.10 and 0.11.\n  source: Results, Choice of architecture; Figure 3c; Table S2\n  expected:\n  - quantity: kappa for Scene Cuts, logistic regression\n    value: 0.10\n    tolerance: 0.032\n  - quantity: kappa for Camera Cuts, logistic regression\n    value: 0.11\n    tolerance: 0.015\n  criterion: The values are the LSTM's (Table S2, 0.20 and 0.18) less the stated drops, and the\n    tolerances the LSTM's SEMs, the nearest stated spread. Reproduced when both values are within\n    tolerance; partially reproduced when both are below the LSTM values and above chance\n    (permutation p < 0.001 in every fold) but one or both are outside tolerance; not reproduced\n    otherwise.\n- id: fig3e-temporal-gap\n  statement: Without temporal gaps between training, validation and test samples, decoding of Summer\n    is almost perfect (kappa 0.99), and it falls to 0.31 as the gap grows to 32 s.\n  source: Results, Avoiding spurious decoding performance; Figure 3e; Figure S9\n  criterion: Tested with the logistic regression in place of the LSTM. A random split assigns each\n    sample at random to training, validation and test in the proportions of the 32 s split, five\n    times; gaps of 4, 8, 16 and 32 s use the dataset's code layout. Reproduced when the random-split\n    kappa is at least 0.9 and above the 32 s value; partially reproduced when it exceeds the 32 s\n    value by at least 0.2 but is below 0.9; not reproduced otherwise.\n- id: fig4-patients-below-pooled\n  statement: Decoding from a single patient's neurons is lower than from the pooled population; no\n    patient matches the pooled performance, for Summer, Scene Cuts or Indoor/Outdoor.\n  source: Results, Patient-wise decoding performance; Figure 4\n  depends_on:\n  - fig3c-logreg-characters-location\n  criterion: The logistic regression per patient, same folds and procedure as the pooled model.\n    Reproduced when, for all three labels, every patient's mean kappa is below the pooled mean\n    kappa; partially reproduced when this holds for two labels; not reproduced otherwise.\n- id: fig4-named-patients\n  statement: For Summer, patients 7, 10, 15 and 22 exceed kappa 0.2; for Indoor/Outdoor, patients 2,\n    13, 20 and 25 exceed 0.2.\n  source: Results, Patient-wise decoding performance; Figure 4b and 4d\n  depends_on:\n  - fig4-patients-below-pooled\n  criterion: Assumes the dandiset's subject ids are the paper's patient numbers; the dandiset and\n    paper give no mapping. Of the 8 named patient and label pairs, reproduced when at least 7 have\n    mean kappa above 0.2; partially reproduced for 4 to 6; not reproduced below 4. The patients\n    above 0.2 here are listed either way.\n- id: fig5-region-decoding\n  statement: Decoding from single regions depends on the feature; the amygdala is best and the\n    hippocampus worst for Summer, and the parahippocampal cortex is best and the amygdala worst\n    for Indoor/Outdoor.\n  source: Results, Parahippocampal cortex drives decoding; Amygdala drives decoding; Figure 5\n  criterion: Tested with the logistic regression in place of the LSTM, restricted to the units of\n    one region (A, H, EC, PHC as fixed in the opening comment). The four orderings are A highest\n    and H lowest for Summer, PHC highest and A lowest for Indoor/Outdoor, by mean kappa.\n    Reproduced when all four hold; partially reproduced when 2 or 3 hold; not reproduced otherwise.\n- id: fig6-responsive-subsets\n  statement: Responsive neurons drive decoding of camera cuts but not of Summer; without them,\n    Summer is decoded about as well as from all neurons while camera cuts drop the most, and\n    responsive neurons alone decode camera cuts about as well as all neurons but Summer less well.\n  source: Results, Decoding with non-responsive versus responsive neurons; Figure 6\n  depends_on:\n  - fig2b-phc-camera-cuts\n  - tables1-few-semantic-responses\n  criterion: Tested with the logistic regression in place of the LSTM, over all regions together.\n    Responsive units at alpha 0.001. Conditions (a) Summer without responsive units is at least\n    the complete kappa less 0.05; (b) Summer with responsive units only is below the complete\n    kappa less 0.05; (c) the drop without responsive units is larger for camera cuts than for\n    Summer; (d) camera cuts with responsive units only is at least the complete kappa less 0.05.\n    Reproduced when all four hold; partially reproduced when 2 or 3 hold; not reproduced\n    otherwise. Size-matched non-responsive sets (three draws) are shown as a variant.\n- id: fig7b-top500-overlap\n  statement: Across the five rankings of neurons by logistic regression weights for Summer, the top\n    500 neurons share 78 neurons, against about 1 expected by chance.\n  source: Results, Top-ranked neurons; Figure 7b; Methods, Intersection of top-performing neurons\n  expected:\n    quantity: units common to the top 500 of all five rankings\n    value: 78\n    tolerance: 7.8\n  criterion: Twenty sub-splits, four per test fold, each taking one of the other four folds as\n    validation and the remaining three as training; each fit as the pooled logistic regression.\n    Ranking per test fold as in the Methods (units grouped by the number of the four models with a\n    non-zero coefficient, then by mean absolute coefficient); units tied at zero are ordered by a\n    seeded random draw. Chance is computed for 2286 units and five sets of 500. Reproduced when the\n    overlap is within tolerance; partially reproduced when it is outside tolerance but at least ten\n    times chance; not reproduced otherwise.\n- id: fig3c-lstm-decoding\n  statement: An LSTM decodes every label above chance from the pooled population, with kappa 0.36\n    for Persons, 0.31 for Indoor/Outdoor, 0.31 for Summer, 0.32 for McKenzie, 0.23 for Tom, 0.20\n    for Scene Cuts and 0.18 for Camera Cuts.\n  source: Results, Decoding from neuronal activity; Figure 3c; Table S2\n  expected:\n  - quantity: kappa for Persons\n    value: 0.36\n    tolerance: 0.048\n  - quantity: kappa for Summer\n    value: 0.31\n    tolerance: 0.055\n  - quantity: kappa for Camera Cuts\n    value: 0.18\n    tolerance: 0.015\n- id: fig3d-temporal-shuffle\n  statement: Shuffling the order of time bins in the test data lowers the LSTM's performance, most\n    for visual transitions.\n  source: Results, Choice of architecture; Figure 3d\n- id: fig5-faces-presence\n  statement: Face labels decode slightly better than character labels (Summer 0.33, Tom 0.27), and\n    Summer Presence (0.27) is decoded best from the amygdala (0.26).\n  source: Results, Differences in character's visual appearances; Figure 5b and 5c\n- id: fig7a-500-neurons\n  statement: Decoding Summer from the 500 top-ranked neurons gives the peak performance (kappa 0.38),\n    above that of the full population.\n  source: Results, Training on pre-selections of top-ranked neurons; Figure 7a\n"
}
```

```
File created successfully at: claims/001616/10.7554-elife.106758.1.yaml (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd  sed -n 1,378p tools/entry.py | grep -v "^\s*$" | head -330
```

```
"""Lock, check and run one entry. This is the whole local workflow for a deposit.
    python tools/entry.py lock  entries/<name>   # pin the environment
    python tools/entry.py check entries/<name>   # validate metadata and conventions
    python tools/entry.py run   entries/<name>   # execute every notebook from a clean environment
    python tools/entry.py all   entries/<name>   # check, then run
    python tools/entry.py handover entries/<name> # the verifier's package, from the executed copies
`lock` compiles the entry's requirements.in (direct dependencies only) into
requirements.lock.txt with every version pinned.
`check` validates entry.yaml, and the claims and attempt files that mention
the entry, against the schemas, and applies the conventions that keep a result
tied to the data:
- every notebook in the directory is listed in entry.yaml, and exists;
- notebooks are committed without outputs;
- the lock file is present and newer requirements are not left unlocked;
- each notebook, or a helper it imports, names the dandiset the entry uses;
- each notebook has a cell tagged `sanity` that prints what was loaded;
- no notebook or helper embeds a large literal array or an encoded image, or
  reads a figure from somewhere else.
`run` builds a fresh virtual environment from the lock file and executes each
notebook through a Jupyter kernel installed in that environment, in the entry
[... 306 more lines not kept]
```

**Agent calls Bash**

```bash
free -g; nproc; cd $TMPDIR/scratch && . .venv/bin/activate && python -c "import sklearn,joblib,scipy;print(sklearn.__version__,joblib.__version__,scipy.__version__)"
```

```
total        used        free      shared  buff/cache   available
Mem:              15           1           7           0           7          14
Swap:              2           0           2
4
1.9.1 1.6.0 1.18.1
Shell cwd was reset to
```

**Agent**

Claims written. Now the helper module.

**Agent calls Write**

```json
{
 "file_path": "entries/001616-gerken-2025/summer.py",
 "content": "\"\"\"Loading and measures for dandiset 001616 (SUMMER), human MTL single units during the film\n\"500 Days of Summer\".\n\nGerken, Darcher et al., eLife reviewed preprint 106758 v1, doi:10.7554/eLife.106758.1.\n\nEach NWB file holds one patient: spike times of every unit (milliseconds, recording clock, with\n0 at the movie start), the unit's brain region, the movie annotations (53 labels, per frame and as\nsegments in movie time), and the watchlogs that map each presented frame (presentation time\nstamp, seconds) to the recording clock (milliseconds). Files are streamed from the archive at the\npinned version; nothing is written to disk.\n\nWhere the parameters come from:\n\n- The Methods of the paper: 80 ms bins (two frames), a window of 800 ms before and after each\n  sample, labels of a bin taken from its first frame, camera cut labels extended to frames within\n  520 ms of the cut, a gap of 32 s between training, validation and test samples, logistic\n  regression with an L1 penalty (liblinear), z-scored with training statistics, Cohen's kappa,\n  1000 test-label shuffles for chance. The responsive-unit test (baseline -1000 to 0 ms,\n  19 overlapping 100 ms bins from 0 to 1000 ms, Wilcoxon signed-rank, Simes correction, spikes in\n  at least a third of the pseudo-trials) and the cluster permutation test (p < 0.005 per bin,\n  1000 permutations).\n- The dataset's code (https://github.com/mormannlab/SUMMER at commit\n  59fc2424615150481494edf3e31d707729d395ea): the bin edges and frames of `movie_binning_info`,\n  the fold layout of ML_framework/dataloader.py (`BUFFER_NUMBER_REPEATED_PARTS`, five folds per\n  part, test fold f, validation fold f+1), the grouping of hippocampal subregions\n  (`REGION_ALTERNATIVE_NAMES`), the onset rule of calc_responsive_units.py, and the ZETA test it\n  uses for responsive units (shown as a variant).\n- Common choices where neither says: class weights balanced in the logistic regression (the paper\n  oversamples the minority class for its LSTM), the grid of C values, the threshold search for\n  single units, and dropping spikes that fall in playback pauses.\n\"\"\"\n\nfrom __future__ import annotations\n\nfrom concurrent.futures import ThreadPoolExecutor\n\nimport h5py\nimport numpy as np\nimport pandas as pd\nimport remfile\nfrom dandi.dandiapi import DandiAPIClient\nfrom scipy import stats\n\nDANDISET_ID = \"001616\"\nDANDISET_VERSION = \"0.260702.0824\"\n\nBIN_MS = 80                 # Methods: 80 ms bins, two frames of 40 ms\nWINDOW_BINS = 10            # Methods: 800 ms before and 800 ms after a sample\nCUT_SPREAD_S = 0.52         # Methods: cut labels cover frames within 520 ms of the cut onset\nGAP_S = 32                  # Methods: 32 s between training, validation and test samples\n# dataset code, ML_framework/dataloader.py: number of repeated parts for each gap size\nPARTS_FOR_GAP = {4: 59, 8: 36, 12: 26, 16: 21, 20: 17, 24: 14, 28: 12, 32: 11, 36: 10, 40: 9, 44: 8}\nC_GRID = (0.001, 0.003, 0.01, 0.03)   # common choice; chosen per split on the validation kappa\nN_PERMUTATIONS = 1000       # Methods\nALPHAS = (0.001, 0.01)      # Results and Figure 2 give 0.001, the Methods 0.01\nCLUSTER_ALPHA = 0.005       # Methods\n\n# Paper label name -> (dandiset label, value that marks the feature)\nLABELS = {\n    \"Summer\": (\"summer\", 1), \"Tom\": (\"tom\", 1), \"McKenzie\": (\"mckenzie\", 1),\n    \"Persons\": (\"persons\", 1), \"Summer Faces\": (\"summer-faces\", 1), \"Tom Faces\": (\"tom-faces\", 1),\n    \"Summer Presence\": (\"summer-presence\", 1), \"Camera Cuts\": (\"camera-cuts\", 1),\n    \"Scene Cuts\": (\"scenes\", 1), \"Indoor\": (\"indoor-setting\", 1), \"Outdoor\": (\"indoor-setting\", 0),\n}\nCUT_LABELS = (\"camera-cuts\", \"scenes\")\n# dataset code, visualization/plot_code/nwb_io.py\nREGIONS = {\"A\": [\"A\"], \"H\": [\"H\", \"AH\", \"MH\", \"PH\"], \"EC\": [\"EC\"], \"PHC\": [\"PHC\", \"APH\", \"PPH\", \"MPH\"],\n           \"PIC\": [\"PIC\"]}\n\n\ndef _text(value):\n    return value.decode() if isinstance(value, bytes) else value\n\n\ndef _ragged(group, name):\n    data, index = group[name][:], group[name + \"_index\"][:]\n    starts = np.r_[0, index[:-1]]\n    return [data[a:b] for a, b in zip(starts, index)]\n\n\ndef asset_urls(version: str = DANDISET_VERSION) -> list[tuple[str, str, str]]:\n    \"\"\"(path, blob id, streaming URL) of every NWB file at a version.\"\"\"\n    with DandiAPIClient() as client:\n        dandiset = client.get_dandiset(DANDISET_ID, version)\n        return sorted((a.path, a.blob, a.get_content_url(follow_redirects=1, strip_query=True))\n                      for a in dandiset.get_assets() if a.path.endswith(\".nwb\"))\n\n\ndef load_session(path: str, url: str) -> dict:\n    \"\"\"Everything the analysis uses from one file, without the waveforms.\"\"\"\n    f = h5py.File(remfile.File(url), \"r\")\n    u = f[\"units\"]\n    units = pd.DataFrame({k: [_text(x) for x in u[k][:]] for k in\n                          (\"unit_id\", \"csc_nr\", \"brain_region\", \"hemisphere\", \"is_single_unit\")})\n    s = {\"path\": path,\n         \"subject_id\": _text(f[\"general/subject/subject_id\"][()]),\n         \"sex\": _text(f[\"general/subject/sex\"][()]),\n         \"age\": _text(f[\"general/subject/age\"][()]),\n         \"units\": units,\n         \"units_description\": _text(u.attrs[\"description\"]),\n         \"spikes_ms\": _ragged(u, \"spike_times\")}\n    e = f[\"general/extracellular_ephys/electrodes\"]\n    s[\"electrodes\"] = pd.DataFrame({k: [_text(x) for x in e[k][:]] for k in (\"csc_nr\", \"group_name\", \"brain_region\")})\n    for name in (\"cleaned_watchlogs\", \"raw_watchlogs\"):\n        g = f[\"stimulus/presentation/\" + name]\n        s[name] = pd.DataFrame({\"pts\": g[\"pts\"][:], \"rec_ms\": g[\"neural_recording_time\"][:]})\n    for name in (\"annotations_base\", \"annotations_patient_aligned\"):\n        g = f[\"stimulus/presentation/\" + name]\n        s[name] = pd.DataFrame({\"start\": g[\"start_time\"][:], \"stop\": g[\"stop_time\"][:],\n                                \"label\": [_text(x) for x in g[\"label_name\"][:]], \"value\": g[\"value\"][:]})\n        s[name + \"_unit\"] = _text(g[\"start_time\"].attrs[\"description\"])\n    g = f[\"processing/machine_learning/movie_annotations_indicator_functions\"]\n    s[\"indicator\"] = dict(zip([_text(x) for x in g[\"label_name\"][:]], _ragged(g, \"indicator_function\")))\n    g = f[\"processing/machine_learning/movie_binning_info\"]\n    lengths = list(g[\"bin_length\"][:])\n    i = lengths.index(BIN_MS)\n    s[\"edges_s\"] = _ragged(g, \"edges\")[i]\n    s[\"bin_frames\"] = np.array([int(_text(x).split(\"_\")[1].split(\".\")[0]) for x in _ragged(g, \"frames\")[i]])\n    s[\"frame_times_base\"] = f[\"stimulus/presentation/movie_frame_times_base/data\"][:]\n    s[\"frame_times_analysis\"] = f[\"stimulus/presentation/movie_frame_times_analysis/data\"][:]\n    f.close()\n    return s\n\n\ndef load_all(version: str = DANDISET_VERSION, workers: int = 8) -> list[dict]:\n    assets = asset_urls(version)\n    with ThreadPoolExecutor(workers) as pool:\n        sessions = list(pool.map(lambda a: load_session(a[0], a[2]), assets))\n    for s, a in zip(sessions, assets):\n        s[\"blob\"] = a[1]\n    return sorted(sessions, key=lambda s: int(s[\"subject_id\"]))\n\n\n# --- time base ------------------------------------------------------------------------------\n\ndef pauses(watchlog: pd.DataFrame) -> np.ndarray:\n    \"\"\"(start, stop) on the recording clock (ms) of each playback pause: consecutive entries with\n    the same presentation time stamp.\"\"\"\n    pts, rec = watchlog.pts.to_numpy(), watchlog.rec_ms.to_numpy()\n    i = np.where(np.diff(pts) == 0)[0]\n    return np.c_[rec[i], rec[i + 1]]\n\n\ndef movie_time(spikes_ms: np.ndarray, watchlog: pd.DataFrame) -> np.ndarray:\n    \"\"\"Spike times in movie seconds, through the cleaned watchlog. Spikes in pauses and outside\n    the logged playback are dropped.\"\"\"\n    pts, rec = watchlog.pts.to_numpy(), watchlog.rec_ms.to_numpy()\n    keep = (spikes_ms >= rec[0]) & (spikes_ms <= rec[-1])\n    for a, b in pauses(watchlog):\n        keep &= ~((spikes_ms > a) & (spikes_ms < b))\n    return np.interp(spikes_ms[keep], rec, pts)\n\n\ndef movie_to_rec(t_s: np.ndarray, watchlog: pd.DataFrame) -> np.ndarray:\n    \"\"\"Movie seconds to recording milliseconds (first presentation of each time stamp).\"\"\"\n    pts, rec = watchlog.pts.to_numpy(), watchlog.rec_ms.to_numpy()\n    first = np.r_[True, np.diff(pts) != 0]\n    return np.interp(t_s, pts[first], rec[first])\n\n\ndef unit_table(sessions: list[dict]) -> pd.DataFrame:\n    rows = []\n    for s in sessions:\n        for k, r in s[\"units\"].iterrows():\n            region = next((name for name, members in REGIONS.items() if r.brain_region in members), \"other\")\n            rows.append({\"patient\": int(s[\"subject_id\"]), \"index\": k, \"unit_id\": r.unit_id,\n                         \"brain_region\": r.brain_region, \"region\": region,\n                         \"single\": bool(r.is_single_unit), \"n_spikes\": len(s[\"spikes_ms\"][k])})\n    return pd.DataFrame(rows)\n\n\ndef movie_spikes(sessions: list[dict]) -> list[np.ndarray]:\n    \"\"\"Spike times in movie seconds, one array per unit, in the order of `unit_table`.\"\"\"\n    return [movie_time(sp, s[\"cleaned_watchlogs\"]) for s in sessions for sp in s[\"spikes_ms\"]]\n\n\ndef binned_counts(spikes_s: list[np.ndarray], edges_s: np.ndarray) -> np.ndarray:\n    \"\"\"Units x bins spike counts on the 80 ms bin edges.\"\"\"\n    return np.array([np.histogram(t, edges_s)[0] for t in spikes_s], dtype=np.int16)\n\n\ndef window_sums(counts: np.ndarray, half: int = WINDOW_BINS) -> np.ndarray:\n    \"\"\"Samples x units: spikes from `half` bins before to `half` bins after each bin (the bin\n    itself included in the after part), truncated at the ends.\"\"\"\n    n = counts.shape[1]\n    c = np.cumsum(np.pad(counts.astype(np.int32), ((0, 0), (1, 0))), axis=1)\n    k = np.arange(n)\n    return (c[:, np.clip(k + half, 0, n)] - c[:, np.clip(k - half, 0, n)]).T.astype(np.float32)\n\n\n# --- labels -----------------------------------------------------------------------------------\n\ndef frame_labels(session: dict, label: str) -> np.ndarray:\n    \"\"\"Per-frame label (frames 1..125743, index = frame - 1). Cut labels are extended to the\n    frames within 520 ms after each cut onset.\"\"\"\n    v = session[\"indicator\"][label].copy()\n    if label in CUT_LABELS:\n        onsets = np.where(v == 1)[0]\n        spread = int(round(CUT_SPREAD_S / 0.04))\n        out = np.zeros_like(v)\n        for i in onsets:\n            out[i:i + spread] = 1\n        v = out\n    return v\n\n\ndef bin_labels(session: dict, label: str) -> np.ndarray:\n    \"\"\"Label of each 80 ms bin, from its first frame; values other than 0 and 1 (99, excluded)\n    are kept as they are.\"\"\"\n    return frame_labels(session, label)[session[\"bin_frames\"][:-1] - 1]\n\n\ndef onsets(annotations: pd.DataFrame, label: str, value: int, min_absence: float = 1.0,\n           min_presence: float | None = 1.0) -> np.ndarray:\n    \"\"\"Onsets of a feature preceded by at least `min_absence` (s) without it and, if\n    `min_presence` is given, lasting at least that long. Times as in `annotations`.\"\"\"\n    a = annotations[(annotations.label == label) & (annotations.value == value)].sort_values(\"start\")\n    start, stop = a.start.to_numpy(), a.stop.to_numpy()\n    keep = np.r_[False, start[1:] - min_absence > stop[:-1]]\n    if min_presence is not None:\n        keep &= (stop - start) >= min_presence\n    return start[keep]\n\n\n# --- responsive units (Methods) ----------------------------------------------------------------\n\ndef _counts_in(t: np.ndarray, starts: np.ndarray, width: float) -> np.ndarray:\n    return np.searchsorted(t, starts + width, side=\"left\") - np.searchsorted(t, starts, side=\"left\")\n\n\ndef wilcoxon_simes(spikes_s: np.ndarray, events_s: np.ndarray) -> tuple[float, float]:\n    \"\"\"Simes-combined p of 19 overlapping 100 ms bins (0 to 1000 ms) against the baseline rate\n    (-1000 to 0 ms, per 100 ms), two-sided Wilcoxon signed-rank across pseudo-trials, and the\n    fraction of pseudo-trials with a spike from -1000 to 1000 ms. p = 1 below a third.\"\"\"\n    t = np.sort(spikes_s)\n    base = _counts_in(t, events_s - 1.0, 1.0) / 10.0\n    active = np.mean(_counts_in(t, events_s - 1.0, 2.0) > 0) if len(events_s) else 0.0\n    if active < 1 / 3 or len(events_s) < 2:\n        return 1.0, active\n    starts = events_s[:, None] + 0.05 * np.arange(19)[None, :]\n    bins = _counts_in(t, starts.ravel(), 0.1).reshape(starts.shape)\n    diff = bins - base[:, None]\n    p = np.ones(19)\n    for j in range(19):\n        if np.any(diff[:, j] != 0):\n            p[j] = stats.wilcoxon(diff[:, j]).pvalue\n    ps = np.sort(p)\n    return float(min(1.0, np.min(19 * ps / np.arange(1, 20)))), active\n\n\ndef mean_psth(spikes_s: np.ndarray, events_s: np.ndarray, per_trial_z: bool = False) -> np.ndarray:\n    \"\"\"Trial-averaged spike counts in 20 bins of 100 ms from -1000 to 1000 ms, z-scored over the\n    20 bins (Methods). With `per_trial_z`, each trial is z-scored first and then averaged, as in\n    the dataset's code; trials without spikes stay at 0.\"\"\"\n    t = np.sort(spikes_s)\n    starts = events_s[:, None] - 1.0 + 0.1 * np.arange(20)[None, :]\n    m = _counts_in(t, starts.ravel(), 0.1).reshape(starts.shape).astype(float)\n    if per_trial_z:\n        sd = m.std(1, keepdims=True)\n        z = np.where(sd > 0, (m - m.mean(1, keepdims=True)) / np.where(sd > 0, sd, 1), 0.0)\n        return z.mean(0)\n    v = m.mean(0)\n    return (v - v.mean()) / v.std() if v.std() > 0 else np.zeros_like(v)\n\n\ndef _clusters(t: np.ndarray, p: np.ndarray) -> list[float]:\n    sums, current = [], 0.0\n    for tv, pv in zip(t, p):\n        if pv < CLUSTER_ALPHA:\n            current += abs(tv)\n        elif current:\n            sums.append(current)\n            current = 0.0\n    if current:\n        sums.append(current)\n    return sums\n\n\ndef cluster_test(psth: np.ndarray, responsive: np.ndarray, rng: np.random.Generator,\n                 n_perm: int = N_PERMUTATIONS) -> tuple[float, float]:\n    \"\"\"Largest cluster sum of |t| between responsive and non-responsive units, and its\n    permutation p (fraction of label permutations whose largest cluster sum is at least it).\"\"\"\n    if responsive.sum() < 2 or (~responsive).sum() < 2:\n        return 0.0, 1.0\n\n    def largest(mask):\n        t, p = stats.ttest_ind(psth[mask], psth[~mask], axis=0)\n        c = _clusters(np.nan_to_num(t), np.nan_to_num(p, nan=1.0))\n        return max(c) if c else 0.0\n\n    observed = largest(responsive)\n    if observed == 0:\n        return 0.0, 1.0\n    null = np.array([largest(rng.permutation(responsive)) for _ in range(n_perm)])\n    return observed, float(np.mean(null >= observed))\n\n\n# --- splits and decoding -------------------------------------------------------------------------\n\ndef fold_blocks(n: int, gap_s: int = GAP_S, window_s: float = 2 * WINDOW_BINS * BIN_MS / 1000):\n    \"\"\"Per repeated part, the five folds and the gaps after them (sample indices), as in the\n    dataset's code with sequence = the 1.6 s window.\"\"\"\n    parts = PARTS_FOR_GAP[gap_s]\n    base = int(n / parts)\n    gap = int(np.ceil((gap_s + window_s) * 1000 / BIN_MS))\n    length = int((base - 5 * gap) / 5)\n    blocks = []\n    for p in range(parts):\n        i = p * base\n        folds = [np.arange(i + j * (length + gap), i + j * (length + gap) + length) for j in range(5)]\n        gaps = [np.arange(i + j * (length + gap) + length, i + (j + 1) * (length + gap)) for j in range(5)]\n        blocks.append((folds, gaps))\n    return blocks\n\n\ndef split(n: int, test_fold: int, val_fold: int | None = None, gap_s: int = GAP_S):\n    \"\"\"Train, validation and test indices. Test is fold `test_fold` (0-4), validation fold\n    `val_fold` (default the next one); training is the other three folds with the gaps between\n    adjacent training folds, as in the dataset's code.\"\"\"\n    val_fold = (test_fold + 1) % 5 if val_fold is None else val_fold\n    train_folds = [j for j in range(5) if j not in (test_fold, val_fold)]\n    tr, va, te = [], [], []\n    for folds, gaps in fold_blocks(n, gap_s):\n        te.append(folds[test_fold])\n        va.append(folds[val_fold])\n        for j in train_folds:\n            tr.append(folds[j])\n            if (j + 1) % 5 in train_folds and j < 4:\n                tr.append(gaps[j])\n    return np.concatenate(tr), np.concatenate(va), np.concatenate(te)\n\n\ndef random_split(n: int, sizes: tuple[int, int, int], rng: np.random.Generator):\n    order = rng.permutation(n)\n    a, b, c = sizes\n    return np.sort(order[:a]), np.sort(order[a:a + b]), np.sort(order[a + b:a + b + c])\n\n\ndef kappa(y: np.ndarray, p: np.ndarray) -> float:\n    \"\"\"Cohen's kappa for binary labels.\"\"\"\n    y, p = np.asarray(y, bool), np.asarray(p, bool)\n    po = np.mean(y == p)\n    pe = y.mean() * p.mean() + (1 - y.mean()) * (1 - p.mean())\n    return float((po - pe) / (1 - pe)) if pe < 1 else 0.0\n\n\ndef shuffled_kappas(y: np.ndarray, p: np.ndarray, rng: np.random.Generator, n: int = N_PERMUTATIONS):\n    \"\"\"Kappa of the fixed predictions against shuffled test labels (Methods, test-set shuffle).\"\"\"\n    y = np.asarray(y, bool)\n    p = np.asarray(p, bool)\n    ys = np.array([rng.permutation(y) for _ in range(n)])\n    po = np.mean(ys == p[None, :], axis=1)\n    pe = y.mean() * p.mean() + (1 - y.mean()) * (1 - p.mean())\n    return (po - pe) / (1 - pe) if pe < 1 else np.zeros(n)\n\n\ndef fit_logreg(S: np.ndarray, y: np.ndarray, tr: np.ndarray, va: np.ndarray, te: np.ndarray,\n               columns=None, c_grid=C_GRID) -> dict:\n    \"\"\"L1 logistic regression on window sums, z-scored with training statistics; C chosen on the\n    validation kappa. Samples whose label is not 0 or 1 are left out.\"\"\"\n    from sklearn.linear_model import LogisticRegression\n    ok = (y == 0) | (y == 1)\n    tr, va, te = tr[ok[tr]], va[ok[va]], te[ok[te]]\n    X = S if columns is None else S[:, columns]\n    mu = X[tr].mean(0)\n    sd = X[tr].std(0)\n    sd[sd == 0] = 1\n    Ztr, Zva, Zte = ((X[i] - mu) / sd for i in (tr, va, te))\n    best = None\n    for c in c_grid:\n        model = LogisticRegression(l1_ratio=1.0, solver=\"liblinear\", C=c, class_weight=\"balanced\")\n        model.fit(Ztr, y[tr])\n        k = kappa(y[va], model.predict(Zva))\n        if best is None or k > best[0]:\n            best = (k, c, model)\n    k_val, c, model = best\n    pred = model.predict(Zte)\n    return {\"kappa\": kappa(y[te], pred), \"kappa_val\": k_val, \"C\": c, \"coef\": model.coef_.ravel(),\n            \"y_test\": y[te], \"pred\": pred, \"n\": (len(tr), len(va), len(te))}\n\n\ndef run_jobs(jobs, n_jobs: int = -1):\n    \"\"\"Run (function, args) pairs in parallel processes.\"\"\"\n    from joblib import Parallel, delayed\n    return Parallel(n_jobs=n_jobs)(delayed(f)(*a) for f, a in jobs)\n\n\ndef threshold_unit(x: np.ndarray, y: np.ndarray, va: np.ndarray, te: np.ndarray, n_q: int = 50) -> float:\n    \"\"\"Single-unit decoding: the threshold and direction with the best validation kappa, among up\n    to `n_q` quantiles of the unit's counts, applied to the test set.\"\"\"\n    candidates = np.unique(np.quantile(x[va], np.linspace(0, 1, n_q)))\n    best, rule = -np.inf, (np.inf, 1)\n    for t in candidates:\n        for sign in (1, -1):\n            k = kappa(y[va], sign * x[va] > sign * t)\n            if k > best:\n                best, rule = k, (t, sign)\n    t, sign = rule\n    return kappa(y[te], sign * x[te] > sign * t)\n\n\ndef ranking(coefs: list[np.ndarray], rng: np.random.Generator) -> np.ndarray:\n    \"\"\"Methods: units grouped by the number of models with a non-zero coefficient (most first),\n    then by mean absolute coefficient; ties (all zero) in a random order.\"\"\"\n    C = np.abs(np.array(coefs))\n    nonzero = (C > 0).sum(0)\n    mean_abs = C.mean(0)\n    tiebreak = rng.permutation(C.shape[1])\n    return np.lexsort((tiebreak, -mean_abs, -nonzero))\n"
}
```

```
File created successfully at: entries/001616-gerken-2025/summer.py (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "entries/001616-gerken-2025/summer.py",
 "old_string": "    adjacent training folds, as in the dataset's code.\"\"\"",
 "new_string": "    adjacent training folds (the gap after fold 5 leads to fold 1 of the next part), as in the\n    dataset's code.\"\"\""
}
```

```
The file entries/001616-gerken-2025/summer.py has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "entries/001616-gerken-2025/summer.py",
 "old_string": "            if (j + 1) % 5 in train_folds and j < 4:",
 "new_string": "            if (j + 1) % 5 in train_folds:"
}
```

```
The file entries/001616-gerken-2025/summer.py has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd $TMPDIR/scratch && . .venv/bin/activate && cp entries/001616-gerken-2025/summer.py . && python - <<'EOF'
import time, pickle, summer, numpy as np
t=time.time(); S=summer.load_all(); print('load',time.time()-t)
pickle.dump(S,open('sessions.pkl','wb'))
n=59080
for f in range(5):
    tr,va,te=summer.split(n,f); print(f,len(tr),len(va),len(te), len(set(tr)&set(te)), len(set(tr)&set(va)))
from sklearn.linear_model import LogisticRegression
m=LogisticRegression(l1_ratio=1.0, solver="liblinear", C=0.01); m.fit(np.random.randn(100,5), np.random.rand(100)>0.5); print((m.coef_!=0).sum())
EOF
```

```
load 127.47386980056763
0 30822 7194 7194 0 0
1 30822 7194 7194 0 0
2 30822 7194 7194 0 0
3 30822 7194 7194 0 0
4 30822 7194 7194 0 0
0
Shell cwd was reset to
```

**Agent**

Splits reproduce the paper's sample counts exactly (30822/7194/7194). Now timing the responsive-unit test across all units and labels.

**Agent calls Bash**

```bash
cd $TMPDIR/scratch && . .venv/bin/activate && cp entries/001616-gerken-2025/summer.py . && python - <<'EOF'
import time, pickle, summer, numpy as np, pandas as pd
S=pickle.load(open('sessions.pkl','rb'))
units=summer.unit_table(S); t=time.time(); spk=summer.movie_spikes(S); print('mt',time.time()-t)
ann=S[0]['annotations_base']
ev=summer.onsets(ann,'camera-cuts',1,min_presence=None); print(len(ev))
t=time.time()
ps=[summer.wilcoxon_simes(x,ev) for x in spk[:200]]
print('200 units',time.time()-t)
EOF
```

```
mt 1.5730197429656982
883
200 units 1.6638069152832031
Shell cwd was reset to
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "entries/001616-gerken-2025/summer.py",
 "old_string": "def mean_psth(",
 "new_string": "def responsive_table(spikes_s: list[np.ndarray], t_range: tuple[float, float],\n                     events: dict[str, np.ndarray]) -> pd.DataFrame:\n    \"\"\"For one patient's units: the Wilcoxon-Simes p, the fraction of active pseudo-trials, the\n    number of pseudo-trials and the trial-averaged PSTH (Methods z-scoring, and the code's\n    per-trial z-scoring) for each label. Events whose window leaves the patient's logged\n    playback are left out.\"\"\"\n    rows = []\n    for name, ev in events.items():\n        ev = ev[(ev - 1.0 >= t_range[0]) & (ev + 1.0 <= t_range[1])]\n        for i, t in enumerate(spikes_s):\n            p, active = wilcoxon_simes(t, ev)\n            rows.append({\"unit\": i, \"label\": name, \"p\": p, \"active\": active, \"trials\": len(ev),\n                         \"psth\": mean_psth(t, ev), \"psth_trial_z\": mean_psth(t, ev, per_trial_z=True)})\n    return pd.DataFrame(rows)\n\n\ndef mean_psth("
}
```

```
The file entries/001616-gerken-2025/summer.py has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "entries/001616-gerken-2025/summer.py",
 "old_string": "def threshold_unit(x: np.ndarray, y: np.ndarray, va: np.ndarray, te: np.ndarray, n_q: int = 50) -> float:\n    \"\"\"Single-unit decoding: the threshold and direction with the best validation kappa, among up\n    to `n_q` quantiles of the unit's counts, applied to the test set.\"\"\"\n    candidates = np.unique(np.quantile(x[va], np.linspace(0, 1, n_q)))\n    best, rule = -np.inf, (np.inf, 1)\n    for t in candidates:\n        for sign in (1, -1):\n            k = kappa(y[va], sign * x[va] > sign * t)\n            if k > best:\n                best, rule = k, (t, sign)\n    t, sign = rule\n    return kappa(y[te], sign * x[te] > sign * t)",
 "new_string": "def kappa_rows(y: np.ndarray, P: np.ndarray) -> np.ndarray:\n    \"\"\"Cohen's kappa of each row of a boolean prediction matrix against labels y.\"\"\"\n    y = np.asarray(y, bool)\n    P = np.asarray(P, bool)\n    po = (P == y[None, :]).mean(1)\n    q = P.mean(1)\n    pe = y.mean() * q + (1 - y.mean()) * (1 - q)\n    with np.errstate(invalid=\"ignore\", divide=\"ignore\"):\n        k = (po - pe) / (1 - pe)\n    return np.where(pe < 1, k, 0.0)\n\n\ndef threshold_unit(x: np.ndarray, y: np.ndarray, va: np.ndarray, te: np.ndarray, n_q: int = 50) -> float:\n    \"\"\"Single-unit decoding (Methods, Figure 3b): the threshold and direction with the best\n    validation kappa, among up to `n_q` quantiles of the unit's window counts, applied to the\n    test set.\"\"\"\n    t = np.unique(np.quantile(x[va], np.linspace(0, 1, n_q)))\n    above = x[va][None, :] > t[:, None]\n    k = np.r_[kappa_rows(y[va], above), kappa_rows(y[va], ~above)]\n    best = int(np.argmax(k))\n    threshold, sign = t[best % len(t)], (1 if best < len(t) else -1)\n    pred = x[te] > threshold if sign == 1 else ~(x[te] > threshold)\n    return kappa(y[te], pred)\n\n\ndef unit_summary(url: str) -> dict:\n    \"\"\"Units, spike counts and the sorted spike times of a file, to compare deposits.\"\"\"\n    f = h5py.File(remfile.File(url), \"r\")\n    u = f[\"units\"]\n    out = {\"subject_id\": _text(f[\"general/subject/subject_id\"][()]),\n           \"regions\": [_text(x) for x in u[\"brain_region\"][:]],\n           \"spikes_ms\": np.sort(u[\"spike_times\"][:]),\n           \"n_units\": len(u[\"spike_times_index\"])}\n    f.close()\n    return out"
}
```

```
The file entries/001616-gerken-2025/summer.py has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "entries/001616-gerken-2025/summer.py",
 "old_string": "    best = None\n    for c in c_grid:\n        model = LogisticRegression(l1_ratio=1.0, solver=\"liblinear\", C=c, class_weight=\"balanced\")\n        model.fit(Ztr, y[tr])\n        k = kappa(y[va], model.predict(Zva))\n        if best is None or k > best[0]:\n            best = (k, c, model)\n    k_val, c, model = best\n    pred = model.predict(Zte)\n    return {\"kappa\": kappa(y[te], pred), \"kappa_val\": k_val, \"C\": c, \"coef\": model.coef_.ravel(),\n            \"y_test\": y[te], \"pred\": pred, \"n\": (len(tr), len(va), len(te))}",
 "new_string": "    best, test_by_c = None, {}\n    for c in c_grid:\n        model = LogisticRegression(l1_ratio=1.0, solver=\"liblinear\", C=c, class_weight=\"balanced\")\n        model.fit(Ztr, y[tr])\n        k = kappa(y[va], model.predict(Zva))\n        test_by_c[c] = kappa(y[te], model.predict(Zte))\n        if best is None or k > best[0]:\n            best = (k, c, model)\n    k_val, c, model = best\n    pred = model.predict(Zte)\n    return {\"kappa\": kappa(y[te], pred), \"kappa_val\": k_val, \"C\": c, \"coef\": model.coef_.ravel(),\n            \"y_test\": y[te], \"pred\": pred, \"n\": (len(tr), len(va), len(te)), \"kappa_by_C\": test_by_c}"
}
```

```
The file entries/001616-gerken-2025/summer.py has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent**

Helper done. Now writing the notebook (analysis cells first; conclusions after I see outputs).

**Agent calls Write**

```json
{
 "file_path": "/tmp/claude-1001/scratch/build_nb.py",
 "content": "\"\"\"Builds the notebook from cell sources. Conclusions are in results.py (filled after the run).\"\"\"\nimport json\nimport sys\nfrom pathlib import Path\n\nimport nbformat as nbf\n\nENTRY = Path(\"entries/001616-gerken-2025\")\nresults = json.loads(Path(\"/tmp/claude-1001/scratch/results.json\").read_text()) if Path(\"/tmp/claude-1001/scratch/results.json\").exists() else {}\n\ncells = []\n\n\ndef md(text):\n    cells.append(nbf.v4.new_markdown_cell(text.strip(\"\\n\")))\n\n\ndef code(text, tags=None):\n    c = nbf.v4.new_code_cell(text.strip(\"\\n\"))\n    if tags:\n        c.metadata[\"tags\"] = tags\n    cells.append(c)\n\n\ndef result(key):\n    md(results.get(key, f\"**Result: pending ({key}).**\"))\n\n\nmd(results[\"header\"] if \"header\" in results else \"# header pending\")\n\ncode(r'''\nimport os\nfor var in (\"OMP_NUM_THREADS\", \"OPENBLAS_NUM_THREADS\", \"MKL_NUM_THREADS\"):\n    os.environ.setdefault(var, \"1\")\nimport time\nimport warnings\n\nimport matplotlib.pyplot as plt\nimport numpy as np\nimport pandas as pd\nfrom scipy import stats\n\nimport summer\n\npd.set_option(\"display.width\", 220)\npd.set_option(\"display.max_columns\", 40)\npd.set_option(\"display.max_rows\", 200)\nwarnings.filterwarnings(\"ignore\", category=RuntimeWarning)\n\nstarted = time.time()\nsessions = summer.load_all()\nunits = summer.unit_table(sessions)\nspikes = summer.movie_spikes(sessions)\nprint(f\"loaded {len(sessions)} files, {len(units)} units, from dandiset {summer.DANDISET_ID} \"\n      f\"version {summer.DANDISET_VERSION} in {time.time() - started:.0f} s\")\n''')\n\nmd(\"\"\"\n## Data check\n\nEach check of the metadata against the values is stated under its output.\n\"\"\")\n\ncode(r'''\n# Versions: what the pinned version holds against the earlier published version.\npinned = summer.asset_urls(summer.DANDISET_VERSION)\nearlier = summer.asset_urls(\"0.260519.1133\")\nblob = {p: b for p, b, _ in pinned}\nsame = [p for p, b, _ in earlier if blob.get(p) == b]\nextra = [(p, u) for p, b, u in earlier if p not in blob]\nprint(f\"version {summer.DANDISET_VERSION}: {len(pinned)} NWB files; version 0.260519.1133: {len(earlier)} NWB files\")\nprint(f\"files of 0.260519.1133 also in the pinned version, same path and blob: {len(same)} of {len(pinned)}\")\nprint(f\"files only in 0.260519.1133: {len(extra)}, named like {extra[0][0]}\")\n\nfrom concurrent.futures import ThreadPoolExecutor\nwith ThreadPoolExecutor(8) as pool:\n    old = list(pool.map(lambda a: summer.unit_summary(a[1]), extra))\nrows = []\nfor o in old:\n    s = next(s for s in sessions if s[\"subject_id\"] == o[\"subject_id\"])\n    new_spikes = np.sort(np.concatenate(s[\"spikes_ms\"]))\n    same_n = len(new_spikes) == len(o[\"spikes_ms\"])\n    rows.append({\"patient\": int(o[\"subject_id\"]), \"units_old\": o[\"n_units\"], \"units_pinned\": len(s[\"units\"]),\n                 \"spikes_old\": len(o[\"spikes_ms\"]), \"spikes_pinned\": len(new_spikes),\n                 \"same_spike_times\": bool(same_n and np.allclose(new_spikes, o[\"spikes_ms\"], atol=1e-3)),\n                 \"same_regions\": sorted(o[\"regions\"]) == sorted(s[\"units\"].brain_region)})\nold_cmp = pd.DataFrame(rows).sort_values(\"patient\")\nprint(old_cmp.to_string(index=False))\nprint(\"patients of the pinned version without an older copy:\",\n      sorted(set(int(s[\"subject_id\"]) for s in sessions) - set(old_cmp.patient)))\nprint(\"older copies with the same spike times as the pinned file:\", int(old_cmp.same_spike_times.sum()), \"of\", len(old_cmp))\n''', [\"sanity\"])\n\nresult(\"md_versions\")\n\ncode(r'''\npat = pd.DataFrame([{\"patient\": int(s[\"subject_id\"]), \"sex\": s[\"sex\"], \"age\": s[\"age\"], \"units\": len(s[\"units\"]),\n                     \"single_units\": int(s[\"units\"].is_single_unit.sum())} for s in sessions])\nages = pat.age.str.extract(r\"P(\\d+)Y\")[0].astype(int)\nprint(f\"patients {len(pat)}; female {int((pat.sex == 'F').sum())}, male {int((pat.sex == 'M').sum())}; \"\n      f\"ages {ages.min()} to {ages.max()} years (median {ages.median():.0f})\")\nprint(f\"units {pat.units.sum()} ({pat.single_units.sum()} marked single units); per patient {pat.units.min()} to {pat.units.max()}\")\nprint(\"\\nUnits by `brain_region` as stored:\")\nprint(units.brain_region.value_counts().to_string())\nprint(\"\\nUnits by region as grouped here (H = AH, MH, PH; FF, LG and PRC are 'other'):\")\nprint(units.region.value_counts().to_string())\nprint(\"\\nUnits per patient and region:\")\nprint(pd.crosstab(units.patient, units.region, margins=True).to_string())\nmismatch = 0\nfor s in sessions:\n    region_of = dict(zip(s[\"electrodes\"].csc_nr, s[\"electrodes\"].brain_region))\n    mismatch += int((s[\"units\"].csc_nr.map(region_of) != s[\"units\"].brain_region).sum())\nprint(\"\\nunits whose region differs from that of their electrode:\", mismatch)\nprint(\"units table description:\", sessions[0][\"units_description\"])\n''', [\"sanity\"])\n\nresult(\"md_units\")\n\ncode(r'''\nrows = []\nfor s in sessions:\n    w = s[\"cleaned_watchlogs\"]\n    raw = s[\"raw_watchlogs\"]\n    pa = summer.pauses(w)\n    sp = np.concatenate(s[\"spikes_ms\"])\n    in_pause = sum(int(((sp > a) & (sp < b)).sum()) for a, b in pa)\n    rows.append({\"patient\": int(s[\"subject_id\"]), \"frames_logged\": len(w),\n                 \"analysis_frames_covered\": float(np.isin(np.round(s[\"frame_times_analysis\"], 2), np.round(w.pts, 2)).mean()),\n                 \"pts_first_s\": w.pts.iloc[0], \"pts_last_s\": w.pts.iloc[-1],\n                 \"pauses\": len(pa), \"pause_min\": (pa[:, 1] - pa[:, 0]).sum() / 60000 if len(pa) else 0.0,\n                 \"frame_interval_ms\": float(np.median(np.diff(w.rec_ms[np.r_[True, np.diff(w.pts) != 0]]))),\n                 \"raw_backward_steps\": int((np.diff(raw.pts) < 0).sum()),\n                 \"spike_min_ms\": sp.min(), \"spike_max_ms\": sp.max(), \"rec_last_ms\": w.rec_ms.iloc[-1],\n                 \"spikes_in_pauses\": in_pause, \"spikes_outside_log\": int(((sp < w.rec_ms.iloc[0]) | (sp > w.rec_ms.iloc[-1])).sum())})\ntb = pd.DataFrame(rows)\nprint(tb.round(3).to_string(index=False))\nprint(\"\\nmedian frame interval on the recording clock, ms:\", tb.frame_interval_ms.min().round(2), \"to\", tb.frame_interval_ms.max().round(2))\nprint(\"analysis frames (credits excluded):\", len(sessions[0][\"frame_times_analysis\"]), \"from\",\n      sessions[0][\"frame_times_analysis\"][0], \"to\", sessions[0][\"frame_times_analysis\"][-1], \"s; all frames:\",\n      len(sessions[0][\"frame_times_base\"]))\nprint(\"80 ms bin edges identical in all files:\", all(np.array_equal(s[\"edges_s\"], sessions[0][\"edges_s\"]) for s in sessions),\n      \"; bins:\", len(sessions[0][\"edges_s\"]) - 1)\nprint(\"annotation and indicator tables identical in all files:\",\n      all(s[\"annotations_base\"].equals(sessions[0][\"annotations_base\"]) for s in sessions),\n      all(all(np.array_equal(s[\"indicator\"][k], sessions[0][\"indicator\"][k]) for k in sessions[0][\"indicator\"]) for s in sessions))\n\n# Do the patient-aligned annotations (stated in seconds in the column, ms in the table description)\n# follow from the movie-time annotations through the watchlog?\ndev = []\nfor s in sessions:\n    b = s[\"annotations_base\"]\n    a = s[\"annotations_patient_aligned\"]\n    for lab in (\"summer\", \"camera-cuts\"):\n        bs = b[(b.label == lab) & (b.value == 1)].start.to_numpy()\n        as_ = a[(a.label == lab) & (a.value == 1)].start.to_numpy()\n        w = s[\"cleaned_watchlogs\"]\n        inside = (bs >= w.pts.iloc[0]) & (bs <= w.pts.iloc[-1])\n        mapped = summer.movie_to_rec(bs[inside], w)\n        nearest = np.abs(as_[None, :] - mapped[:, None]).min(1) if len(as_) else np.array([np.nan])\n        dev.append({\"patient\": int(s[\"subject_id\"]), \"label\": lab, \"base_onsets\": int(inside.sum()),\n                    \"aligned_onsets\": len(as_), \"median_abs_diff_ms\": float(np.median(nearest))})\ndev = pd.DataFrame(dev)\nprint(\"\\nmovie-time onsets mapped through the watchlog against `annotations_patient_aligned` (ms):\")\nprint(dev.groupby(\"label\")[[\"base_onsets\", \"aligned_onsets\", \"median_abs_diff_ms\"]].describe().round(1).T.to_string())\nprint(\"column description:\", repr(sessions[0][\"annotations_patient_aligned_unit\"]))\n''', [\"sanity\"])\n\nresult(\"md_timebase\")\n\ncode(r'''\ns0 = sessions[0]\nfa = s0[\"frame_times_analysis\"]\nanalysis = (s0[\"frame_times_base\"] >= fa[0]) & (s0[\"frame_times_base\"] <= fa[-1])\nrows = []\nfor name, (label, value) in summer.LABELS.items():\n    v = s0[\"indicator\"][label]\n    rows.append({\"label\": name, \"dandiset_label\": label, \"values\": str(sorted(np.unique(v).tolist())),\n                 \"fraction_of_analysis_frames\": float(np.mean(v[analysis] == value)),\n                 \"segments\": int(((s0[\"annotations_base\"].label == label) & (s0[\"annotations_base\"].value == value)).sum())})\nlab = pd.DataFrame(rows)\nprint(lab.round(3).to_string(index=False))\nprint(\"Paper (Results): Summer 50/50, Tom 80/20, Persons 95/5, McKenzie 10/90 of frames.\")\ncc = s0[\"indicator\"][\"camera-cuts\"]\nsc = s0[\"indicator\"][\"scenes\"]\nmovie_s = s0[\"frame_times_base\"][-1]\nprint(f\"\\ncamera cuts: {int(cc.sum())} single-frame events, one every {movie_s / cc.sum():.2f} s (supplement: one every 3 s)\")\nprint(f\"scene cuts: {int(sc.sum())}, mean scene length {movie_s / sc.sum():.1f} s (supplement: 36.15 s); \"\n      f\"scene cut frames that are also camera cut frames: {int(((sc == 1) & (cc == 1)).sum())}\")\nprint(\"frames of indoor-setting by value (1 indoor, 0 outdoor, 99 neither):\",\n      pd.Series(s0[\"indicator\"][\"indoor-setting\"][analysis]).value_counts().to_dict())\nprint(\"face labels hold only 0 and 1 (the Methods also exclude frames):\",\n      [sorted(np.unique(s0[\"indicator\"][k]).tolist()) for k in (\"summer-faces\", \"tom-faces\")])\nprint(\"all 53 labels:\", \", \".join(sorted(s0[\"indicator\"])))\n''', [\"sanity\"])\n\nresult(\"md_labels\")\n\ncode(r'''\n# Duplicates within the pinned version: identical spike trains across units, identical watchlogs.\nkeys = {}\ndupes = []\nfor i, t in enumerate(spikes):\n    if len(t) < 20:\n        continue\n    k = tuple(np.round(t[:20], 4))\n    if k in keys:\n        dupes.append((keys[k], i))\n    keys.setdefault(k, i)\nprint(\"pairs of units with the same first 20 spike times:\", len(dupes))\nfor a, b in dupes:\n    print(\"  \", units.iloc[a][[\"patient\", \"unit_id\", \"brain_region\", \"n_spikes\"]].to_dict(),\n          units.iloc[b][[\"patient\", \"unit_id\", \"brain_region\", \"n_spikes\"]].to_dict())\nw0 = {int(s[\"subject_id\"]): tuple(np.round(s[\"cleaned_watchlogs\"].rec_ms.to_numpy()[100:110], 3)) for s in sessions}\nprint(\"patients sharing a watchlog:\", len(w0) - len(set(w0.values())))\nprint(\"units with no spike during playback:\", int(sum(len(t) == 0 for t in spikes)))\n''', [\"sanity\"])\n\nresult(\"md_dupes\")\n\ncode(r'''\n# Clock check: does each patient's population respond to camera cuts at the annotated times, and\n# not at the same number of random times? Index = mean over units of (rate 0-500 ms after minus\n# rate 500-0 ms before) / unit's mean rate.\nrng_clock = np.random.default_rng(1)\nann = sessions[0][\"annotations_base\"]\ncuts = summer.onsets(ann, \"camera-cuts\", 1, min_presence=None)\n\n\ndef cut_index(ts, ev):\n    vals = []\n    for t in ts:\n        if len(t) < 100:\n            continue\n        rate = len(t) / (t[-1] - t[0])\n        after = summer._counts_in(np.sort(t), ev, 0.5).mean() / 0.5\n        before = summer._counts_in(np.sort(t), ev - 0.5, 0.5).mean() / 0.5\n        vals.append((after - before) / rate)\n    return np.mean(vals)\n\n\nrows = []\nfor s in sessions:\n    p = int(s[\"subject_id\"])\n    ts = [spikes[i] for i in units.index[units.patient == p]]\n    lo, hi = s[\"cleaned_watchlogs\"].pts.iloc[0] + 1, s[\"cleaned_watchlogs\"].pts.iloc[-1] - 1\n    ev = cuts[(cuts > lo) & (cuts < hi)]\n    true = cut_index(ts, ev)\n    null = np.array([cut_index(ts, np.sort(rng_clock.uniform(lo, hi, len(ev)))) for _ in range(20)])\n    shifted = cut_index(ts, ev + 2.0)\n    rows.append({\"patient\": p, \"cuts\": len(ev), \"index_true\": true, \"index_shift_2s\": shifted,\n                 \"null_mean\": null.mean(), \"null_sd\": null.std(), \"z\": (true - null.mean()) / null.std()})\nclock = pd.DataFrame(rows)\nprint(clock.round(3).to_string(index=False))\nprint(\"patients with z above 3:\", int((clock.z > 3).sum()), \"of\", len(clock),\n      \"; below 3:\", clock.patient[clock.z <= 3].tolist())\n''', [\"sanity\"])\n\nresult(\"md_clock\")\n\nmd(\"\"\"\n## Responsive units\n\nShared by the next six claims. For every unit and the 11 labels of Table S1, the Methods' test as\nfixed in the claims file: onsets preceded by at least 1 s without the label and, for labels with a\nduration, lasting at least 1 s; the code's onset rule (no minimum duration) is computed as a\nvariant. Indoor and Outdoor are the values 1 and 0 of `indoor-setting`.\n\"\"\")\n\ncode(r'''\nLABEL_ORDER = [\"Tom\", \"Summer\", \"McKenzie\", \"Persons\", \"Tom Faces\", \"Summer Faces\", \"Summer Presence\",\n               \"Camera Cuts\", \"Scene Cuts\", \"Indoor\", \"Outdoor\"]\nevents, events_code = {}, {}\nfor name in LABEL_ORDER:\n    label, value = summer.LABELS[name]\n    events[name] = summer.onsets(ann, label, value, min_presence=None if label in summer.CUT_LABELS else 1.0)\n    events_code[name] = summer.onsets(ann, label, value, min_presence=None)\nprint(pd.DataFrame({\"onsets (Methods rule)\": {k: len(v) for k, v in events.items()},\n                    \"onsets (code rule)\": {k: len(v) for k, v in events_code.items()}}).to_string())\n\nstarted = time.time()\njobs = []\nfor s in sessions:\n    p = int(s[\"subject_id\"])\n    idx = units.index[units.patient == p].to_numpy()\n    rng_ = (s[\"cleaned_watchlogs\"].pts.iloc[0], s[\"cleaned_watchlogs\"].pts.iloc[-1])\n    jobs.append((summer.responsive_table, ([spikes[i] for i in idx], rng_, events)))\n    jobs.append((summer.responsive_table, ([spikes[i] for i in idx], rng_,\n                                            {k: v for k, v in events_code.items() if summer.LABELS[k][0] not in summer.CUT_LABELS})))\nout = summer.run_jobs(jobs)\nparts = []\nfor (f, (ts, r, ev)), df, in zip(jobs, out):\n    pass\nresp_tables = []\nfor j, s in enumerate(sessions):\n    idx = units.index[units.patient == int(s[\"subject_id\"])].to_numpy()\n    for k, rule in ((2 * j, \"methods\"), (2 * j + 1, \"code\")):\n        df = out[k].copy()\n        df[\"unit\"] = idx[df.unit.to_numpy()]\n        df[\"rule\"] = rule\n        resp_tables.append(df)\nresp = pd.concat(resp_tables, ignore_index=True)\nresp = resp.merge(units[[\"patient\", \"region\", \"brain_region\"]], left_on=\"unit\", right_index=True)\nprint(f\"responsive tests done in {time.time() - started:.0f} s; rows {len(resp)}\")\nP = resp[resp.rule == \"methods\"].pivot(index=\"unit\", columns=\"label\", values=\"p\")\nprint(\"units with p = 1 because they spike in fewer than a third of the pseudo-trials, by label:\")\nprint((resp[resp.rule == \"methods\"].assign(low=lambda d: d.active < 1 / 3).groupby(\"label\").low.sum()).to_string())\n\n\ndef responsive_counts(pv, alpha):\n    r = pv <= alpha\n    by_region = r.groupby(units.region).sum()\n    return r.sum(), by_region\n''')\n\nmd(\"\"\"\n## fig2b-phc-camera-cuts\n\n> Over half of the parahippocampal neurons responded to camera cuts (193 of 373, 51.74%).\n\"\"\")\n\ncode(r'''\nrng_fig2b = np.random.default_rng(22)\nphc = units.index[units.region == \"PHC\"]\ncc_p = P.loc[phc, \"Camera Cuts\"]\nprint(f\"PHC units: {len(phc)} (paper: 373)\")\nfor alpha in summer.ALPHAS:\n    n = int((cc_p <= alpha).sum())\n    print(f\"alpha {alpha}: {n} of {len(phc)} responsive, {100 * n / len(phc):.2f}% (paper: 193 of 373, 51.74%; tolerance 46.57 to 56.91%)\")\nprint(\"\\nThreshold sweep (fraction of PHC units, %):\",\n      {a: round(100 * float((cc_p <= a).mean()), 2) for a in (1e-4, 1e-3, 1e-2, 5e-2)})\n\n# Reference: the same test at random event times (same number of events, within each patient's playback).\nnull_rows = []\nfor s in sessions:\n    p = int(s[\"subject_id\"])\n    idx = [i for i in phc if units.patient[i] == p]\n    if not idx:\n        continue\n    lo, hi = s[\"cleaned_watchlogs\"].pts.iloc[0] + 1, s[\"cleaned_watchlogs\"].pts.iloc[-1] - 1\n    ev = np.sort(rng_fig2b.uniform(lo, hi, len(events[\"Camera Cuts\"])))\n    for i in idx:\n        null_rows.append(summer.wilcoxon_simes(spikes[i], ev)[0])\nnull_p = np.array(null_rows)\nprint(\"random event times, PHC units responsive (%):\", {a: round(100 * float((null_p <= a).mean()), 2) for a in summer.ALPHAS})\n\nprint(\"\\nPer patient, PHC units responsive to camera cuts at alpha 0.001 and 0.01:\")\nper = pd.DataFrame({\"units\": cc_p.groupby(units.patient).size(),\n                    \"resp_0.001\": (cc_p <= 0.001).groupby(units.patient).sum(),\n                    \"resp_0.01\": (cc_p <= 0.01).groupby(units.patient).sum()})\nper[\"pct_0.001\"] = 100 * per[\"resp_0.001\"] / per.units\nprint(per.round(1).to_string())\n''', [\"claim:fig2b-phc-camera-cuts\"])\n\ncode(r'''\n# Variant: the ZETA test of the dataset's code (zetapy), on the recording clock with the\n# patient-aligned onsets of the code; 100 resamplings in place of the code's 1000, for time.\nfrom zetapy import zetatest\nfrom joblib import Parallel, delayed\n\n\ndef zeta_p(spikes_ms, events_ms, seed):\n    np.random.seed(seed)\n    return zetatest(spikes_ms / 1000, events_ms / 1000, 1, resampling_number=100)[0]\n\n\nzeta_rows = []\nstarted = time.time()\nfor name in (\"Camera Cuts\", \"Scene Cuts\"):\n    label, value = summer.LABELS[name]\n    tasks = []\n    for s in sessions:\n        p = int(s[\"subject_id\"])\n        a = s[\"annotations_patient_aligned\"]\n        st = a[(a.label == label) & (a.value == value)].sort_values(\"start\")\n        on = st.start.to_numpy()[1:][st.start.to_numpy()[1:] - 1000 > st.stop.to_numpy()[:-1]]\n        for k, i in enumerate(units.index[(units.patient == p) & (units.region == \"PHC\")]):\n            tasks.append((i, s[\"spikes_ms\"][units[\"index\"][i]], on))\n    ps = Parallel(n_jobs=-1)(delayed(zeta_p)(sp, on, 73 + j) for j, (i, sp, on) in enumerate(tasks))\n    zeta_rows += [{\"unit\": i, \"label\": name, \"p_zeta\": pz} for (i, _, _), pz in zip(tasks, ps)]\nzeta = pd.DataFrame(zeta_rows)\nprint(f\"ZETA on {zeta.unit.nunique()} PHC units in {time.time() - started:.0f} s\")\nfor name in (\"Camera Cuts\", \"Scene Cuts\"):\n    z = zeta[zeta.label == name].p_zeta\n    print(name, {a: f\"{int((z <= a).sum())} of {len(z)} ({100 * float((z <= a).mean()):.2f}%)\" for a in summer.ALPHAS})\n''', [\"claim:fig2b-phc-camera-cuts\"])\n\nresult(\"fig2b-phc-camera-cuts\")\n\nmd(\"\"\"\n## tables1-camera-cuts-regions\n\n> Camera cuts evoked responses in a large share of neurons in every region (amygdala 46.90%,\n> entorhinal cortex 45.68%, hippocampus 38.92%).\n\"\"\")\n\ncode(r'''\npaper_cc = {\"A\": 46.90, \"EC\": 45.68, \"H\": 38.92, \"PHC\": 51.74}\nrows = []\nfor region in (\"A\", \"EC\", \"H\", \"PHC\", \"PIC\", \"other\"):\n    idx = units.index[units.region == region]\n    for alpha in summer.ALPHAS:\n        n = int((P.loc[idx, \"Camera Cuts\"] <= alpha).sum())\n        rows.append({\"region\": region, \"alpha\": alpha, \"units\": len(idx), \"responsive\": n,\n                     \"pct\": 100 * n / len(idx), \"paper_pct\": paper_cc.get(region, np.nan)})\ncc_reg = pd.DataFrame(rows)\ncc_reg[\"within_10pct\"] = (cc_reg.pct - cc_reg.paper_pct).abs() <= 0.1 * cc_reg.paper_pct\nprint(cc_reg.round(2).to_string(index=False))\ntot = {a: int((P[\"Camera Cuts\"] <= a).sum()) for a in summer.ALPHAS}\nprint(\"all units:\", {a: f\"{n} of {len(P)} ({100 * n / len(P):.2f}%)\" for a, n in tot.items()}, \"(paper: 1025, 44.84%)\")\nprint(\"\\nPer patient fraction responsive at alpha 0.001 (%), by region (median and range over patients with 5 or more units):\")\nfr = (P[\"Camera Cuts\"] <= 0.001).groupby([units.region, units.patient]).agg([\"mean\", \"size\"])\nfr = fr[fr[\"size\"] >= 5]\nprint((100 * fr[\"mean\"]).groupby(level=0).describe()[[\"count\", \"min\", \"50%\", \"max\"]].round(1).to_string())\n''', [\"claim:tables1-camera-cuts-regions\"])\n\nresult(\"tables1-camera-cuts-regions\")\n\nmd(\"\"\"\n## fig2b-phc-scene-cuts\n\n> Few parahippocampal neurons responded to scene cuts (25 of 373, 6.70%), but the modulation was\n> consistent across the responsive neurons (cluster permutation test, p = 0.018).\n\"\"\")\n\ncode(r'''\nrng_scene = np.random.default_rng(23)\npsth = {rule: {name: np.vstack(resp[(resp.rule == rule) & (resp.label == name)].set_index(\"unit\").loc[units.index, \"psth\"])\n               for name in resp[resp.rule == rule].label.unique()} for rule in (\"methods\",)}\npsth_trial = {name: np.vstack(resp[(resp.rule == \"methods\") & (resp.label == name)].set_index(\"unit\").loc[units.index, \"psth_trial_z\"])\n              for name in LABEL_ORDER}\nphc_mask = (units.region == \"PHC\").to_numpy()\nsc_p = P.loc[phc, \"Scene Cuts\"]\nfor alpha in summer.ALPHAS:\n    r = (sc_p <= alpha).to_numpy()\n    obs, pc = summer.cluster_test(psth[\"methods\"][\"Scene Cuts\"][phc_mask], r, rng_scene)\n    obs2, pc2 = summer.cluster_test(psth_trial[\"Scene Cuts\"][phc_mask], r, rng_scene)\n    print(f\"alpha {alpha}: {int(r.sum())} of {len(r)} PHC units responsive ({100 * r.mean():.2f}%; paper 25 of 373, 6.70%, \"\n          f\"tolerance 4.16 to 9.24%); largest cluster sum |t| {obs:.1f}, p = {pc:.3f}; \"\n          f\"with the code's per-trial z-scoring {obs2:.1f}, p = {pc2:.3f}\")\nprint(\"threshold sweep (%):\", {a: round(100 * float((sc_p <= a).mean()), 2) for a in (1e-4, 1e-3, 1e-2, 5e-2)})\nprint(\"onsets used:\", len(events[\"Scene Cuts\"]))\n''', [\"claim:fig2b-phc-scene-cuts\"])\n\nresult(\"fig2b-phc-scene-cuts\")\n\nmd(\"\"\"\n## tables1-few-semantic-responses\n\n> Only a few neurons responded to the onset of semantic features (Summer 46, Tom 216, Persons 6 and\n> Outdoor 4 of 2286 neurons), in contrast to camera cuts (1025).\n\"\"\")\n\ncode(r'''\ntable_s1 = {\"Tom\": 216, \"Summer\": 46, \"McKenzie\": 0, \"Persons\": 6, \"Tom Faces\": 843, \"Summer Faces\": 634,\n            \"Summer Presence\": 0, \"Camera Cuts\": 1025, \"Scene Cuts\": 106, \"Indoor\": 0, \"Outdoor\": 4}\nPc = resp[resp.rule == \"code\"].pivot(index=\"unit\", columns=\"label\", values=\"p\")\nrows = []\nfor name in LABEL_ORDER:\n    row = {\"label\": name, \"onsets\": len(events[name]), \"paper_total\": table_s1[name]}\n    for alpha in summer.ALPHAS:\n        r = P[name] <= alpha\n        row[f\"total_{alpha}\"] = int(r.sum())\n        row[f\"pct_{alpha}\"] = round(100 * float(r.mean()), 2)\n        for region in (\"A\", \"EC\", \"H\", \"PHC\"):\n            row[f\"{region}_{alpha}\"] = int(r[units.region == region].sum())\n        if name in Pc:\n            row[f\"code_rule_total_{alpha}\"] = int((Pc[name] <= alpha).sum())\n    rows.append(row)\ns1 = pd.DataFrame(rows)\nprint(s1.to_string(index=False))\nprint(\"\\nTolerance: Summer 46 +- 13.2 (32.8 to 59.2), Tom 216 +- 21.6 (194.4 to 237.6).\")\nsemantic = [\"Summer\", \"Tom\", \"McKenzie\", \"Persons\", \"Indoor\", \"Outdoor\", \"Summer Presence\"]\nfor alpha in summer.ALPHAS:\n    print(f\"alpha {alpha}: largest semantic fraction {s1.set_index('label').loc[semantic, f'pct_{alpha}'].max():.2f}% \"\n          f\"({s1.set_index('label').loc[semantic, f'pct_{alpha}'].idxmax()}); camera cuts {s1.set_index('label').loc['Camera Cuts', f'pct_{alpha}']:.2f}%\")\nprint(\"\\nPer patient, units responsive to Summer and Tom at alpha 0.001:\")\nprint(pd.DataFrame({\"units\": units.groupby(\"patient\").size(),\n                    \"Summer\": (P[\"Summer\"] <= 0.001).groupby(units.patient).sum(),\n                    \"Tom\": (P[\"Tom\"] <= 0.001).groupby(units.patient).sum()}).T.to_string())\n''', [\"claim:tables1-few-semantic-responses\"])\n\nresult(\"tables1-few-semantic-responses\")\n\nmd(\"\"\"\n## tables1-no-indoor-response\n\n> No neuron responded to the onset of indoor scenes.\n\"\"\")\n\ncode(r'''\nfor name in (\"Indoor\", \"McKenzie\", \"Summer Presence\"):\n    print(name, f\"({len(events[name])} onsets):\", {a: int((P[name] <= a).sum()) for a in summer.ALPHAS},\n          \"| code onset rule:\", {a: int((Pc[name] <= a).sum()) for a in summer.ALPHAS})\nprint(\"smallest Indoor p:\", f\"{P['Indoor'].min():.2g}\", \"; units testable for Indoor (spiking in a third of the pseudo-trials):\",\n      int((resp[(resp.rule == 'methods') & (resp.label == 'Indoor')].active >= 1 / 3).sum()))\nprint(\"reference, PHC units at random times (fig2b section), responsive at 0.001:\", f\"{100 * float((null_p <= 0.001).mean()):.2f}%\")\n''', [\"claim:tables1-no-indoor-response\"])\n\nresult(\"tables1-no-indoor-response\")\n\nmd(\"\"\"\n## results-cluster-regions\n\n> By the cluster permutation test, parahippocampal neurons responded to the largest set of features\n> (Summer, Persons, Camera Cuts, Scene Cuts, Outdoor), compared with the hippocampus (Tom, Camera\n> Cuts, Outdoor), the amygdala (Camera Cuts) and the entorhinal cortex (none).\n\"\"\")\n\ncode(r'''\nrng_cluster = np.random.default_rng(24)\npaper_sig = {\"PHC\": {\"Summer\", \"Persons\", \"Camera Cuts\", \"Scene Cuts\", \"Outdoor\"},\n             \"H\": {\"Tom\", \"Camera Cuts\", \"Outdoor\"}, \"A\": {\"Camera Cuts\"}, \"EC\": set()}\nCL = [\"Summer\", \"Tom\", \"McKenzie\", \"Persons\", \"Camera Cuts\", \"Scene Cuts\", \"Indoor\", \"Outdoor\"]\nrows = []\nstarted = time.time()\nfor alpha in summer.ALPHAS:\n    for region in (\"A\", \"H\", \"EC\", \"PHC\"):\n        m = (units.region == region).to_numpy()\n        for name in CL:\n            r = (P.loc[units.index[m], name] <= alpha).to_numpy()\n            obs, pc = summer.cluster_test(psth[\"methods\"][name][m], r, rng_cluster)\n            rows.append({\"alpha\": alpha, \"region\": region, \"label\": name, \"responsive\": int(r.sum()),\n                         \"cluster_sum\": obs, \"p\": pc, \"significant\": pc < 0.05, \"paper\": name in paper_sig[region]})\ncl = pd.DataFrame(rows)\ncl[\"agree\"] = cl.significant == cl.paper\nprint(f\"cluster tests in {time.time() - started:.0f} s\")\nfor alpha in summer.ALPHAS:\n    t = cl[cl.alpha == alpha]\n    print(f\"\\nalpha {alpha}: cells agreeing with the paper {int(t.agree.sum())} of {len(t)}\")\n    print(t.pivot(index=\"label\", columns=\"region\", values=\"p\").round(3).to_string())\n    print(\"significant labels per region:\", t[t.significant].groupby(\"region\").label.apply(list).to_dict())\n    print(\"responsive units per cell:\")\n    print(t.pivot(index=\"label\", columns=\"region\", values=\"responsive\").to_string())\n''', [\"claim:results-cluster-regions\"])\n\nresult(\"results-cluster-regions\")\n\nmd(\"\"\"\n## Decoding data\n\nSamples are the 59080 bins of 80 ms of the analysis portion; each unit's feature is its spike count\nfrom 800 ms before to 800 ms after the bin. The labels are those of the decoding claims.\n\"\"\")\n\ncode(r'''\nedges = sessions[0][\"edges_s\"]\ncounts = summer.binned_counts(spikes, edges)\nS = summer.window_sums(counts)\nn = S.shape[0]\nDEC = {\"Summer\": \"summer\", \"Tom\": \"tom\", \"McKenzie\": \"mckenzie\", \"Persons\": \"persons\",\n       \"Indoor/Outdoor\": \"indoor-setting\", \"Scene Cuts\": \"scenes\", \"Camera Cuts\": \"camera-cuts\"}\nY = {name: summer.bin_labels(sessions[0], label) for name, label in DEC.items()}\nprint(\"samples x units:\", S.shape, \"; spikes per unit per bin, median:\", float(np.median(counts.mean(1))))\nprint(pd.DataFrame({name: {\"positive\": float(np.mean(y == 1)), \"negative\": float(np.mean(y == 0)),\n                           \"excluded\": float(np.mean((y != 0) & (y != 1)))} for name, y in Y.items()}).round(3).to_string())\nfor f in range(5):\n    tr, va, te = summer.split(n, f)\n    gap_tr_te = np.min(np.abs(edges[tr][:, None] - edges[te][None, ::50])) if f == 0 else None\n    print(f\"fold {f + 1}: train {len(tr)}, validation {len(va)}, test {len(te)}\"\n          + (f\"; smallest distance from a training to a test sample, every 50th test sample checked: {gap_tr_te:.1f} s\" if f == 0 else \"\"))\n''')\n\nmd(\"\"\"\n## fig3b-single-neuron-threshold\n\n> Thresholding the activity of single neurons does not reliably predict whether Summer is on\n> screen; most neurons perform near chance, below the population decoder.\n\"\"\")\n\ncode(r'''\ny = Y[\"Summer\"]\nfolds = [summer.split(n, f) for f in range(5)]\nstarted = time.time()\nsingle = np.array([[summer.threshold_unit(S[:, i], y, va, te) for (tr, va, te) in folds] for i in range(S.shape[1])])\nmean_k = single.mean(1)\nprint(f\"single-unit thresholds in {time.time() - started:.0f} s\")\nprint(f\"median unit kappa {np.median(mean_k):.4f}; fraction of units below 0.05: {np.mean(mean_k < 0.05):.3f}; \"\n      f\"best unit {mean_k.max():.3f} (patient {units.patient[mean_k.argmax()]}, {units.region[mean_k.argmax()]}); \"\n      f\"units at or above 0.31: {int((mean_k >= 0.31).sum())}\")\nprint(\"quantiles of unit kappa (5, 25, 50, 75, 95, 99%):\", np.round(np.quantile(mean_k, [.05, .25, .5, .75, .95, .99]), 3))\nprint(\"by region, median and max:\")\nprint(pd.Series(mean_k).groupby(units.region).agg([\"median\", \"max\", \"size\"]).round(3).to_string())\nfig, ax = plt.subplots(figsize=(5, 3))\nax.hist(mean_k, bins=60)\nax.axvline(0.31, color=\"k\", ls=\"--\", label=\"paper LSTM, all units\")\nax.set_xlabel(\"single-unit kappa, Summer (mean of 5 folds)\")\nax.set_ylabel(\"units\")\nax.legend()\nplt.show()\nprint(f\"plotted range {mean_k.min():.3f} to {mean_k.max():.3f}; all points shown\")\n''', [\"claim:fig3b-single-neuron-threshold\"])\n\nresult(\"fig3b-single-neuron-threshold\")\n\nmd(\"\"\"\n## fig3c-logreg-characters-location and fig3c-logreg-cuts-lower\n\n> A logistic regression on spike counts decodes characters and location about as well as the LSTM;\n> pooled over patients it reaches kappa 0.28 for Summer and 0.31 for Indoor/Outdoor.\n\n> For scene and camera cuts the logistic regression performs below the LSTM, by 0.1 and 0.07, that\n> is about kappa 0.10 and 0.11.\n\"\"\")\n\ncode(r'''\nrng_lr = np.random.default_rng(31)\nstarted = time.time()\njobs = [(summer.fit_logreg, (S, Y[name], *folds[f])) for name in DEC for f in range(5)]\nfits = dict(zip([(name, f) for name in DEC for f in range(5)], summer.run_jobs(jobs)))\nprint(f\"{len(jobs)} pooled fits in {time.time() - started:.0f} s\")\nlstm = {\"Summer\": (0.3086, 0.0551), \"Tom\": (0.2300, 0.0604), \"McKenzie\": (0.3162, 0.0815), \"Persons\": (0.3599, 0.0477),\n        \"Indoor/Outdoor\": (0.3115, 0.0597), \"Scene Cuts\": (0.2007, 0.0321), \"Camera Cuts\": (0.1833, 0.0149)}\nrows = []\nfor name in DEC:\n    ks = np.array([fits[(name, f)][\"kappa\"] for f in range(5)])\n    perm_p = []\n    for f in range(5):\n        r = fits[(name, f)]\n        null = summer.shuffled_kappas(r[\"y_test\"], r[\"pred\"], rng_lr)\n        perm_p.append((1 + np.sum(null >= r[\"kappa\"])) / (1 + len(null)))\n    rows.append({\"label\": name, \"kappa_mean\": ks.mean(), \"kappa_sem\": ks.std(ddof=1) / np.sqrt(5),\n                 \"folds\": np.round(ks, 3).tolist(), \"C\": [fits[(name, f)][\"C\"] for f in range(5)],\n                 \"nonzero_units\": [int((fits[(name, f)][\"coef\"] != 0).sum()) for f in range(5)],\n                 \"max_perm_p\": max(perm_p), \"lstm_paper\": lstm[name][0], \"lstm_sem\": lstm[name][1]})\nlr = pd.DataFrame(rows).set_index(\"label\")\nprint(lr.round(4).to_string())\nprint(\"\\npaper, logistic regression: Summer 0.28 (tolerance 0.225 to 0.335), Indoor/Outdoor 0.31 (0.25 to 0.37); \"\n      \"Scene Cuts 0.10 (0.068 to 0.132), Camera Cuts 0.11 (0.095 to 0.125)\")\nprint(\"thresholds, LSTM less SEM: Tom 0.17, McKenzie 0.235, Persons 0.312\")\nprint(\"\\ntest kappa at each C, mean over folds:\")\nprint(pd.DataFrame({name: {c: np.mean([fits[(name, f)][\"kappa_by_C\"][c] for f in range(5)]) for c in summer.C_GRID} for name in DEC}).round(3).to_string())\n''', [\"claim:fig3c-logreg-characters-location\", \"claim:fig3c-logreg-cuts-lower\"])\n\ncode(r'''\n# Clock check by decoding: the same fits for Summer with the labels shifted by 300 s (circularly).\nstarted = time.time()\nshifted = np.roll(Y[\"Summer\"], int(300 / 0.08))\nsh = summer.run_jobs([(summer.fit_logreg, (S, shifted, *folds[f])) for f in range(5)])\nprint(f\"Summer, labels shifted by 300 s: kappa {np.mean([r['kappa'] for r in sh]):.3f} \"\n      f\"(folds {np.round([r['kappa'] for r in sh], 3).tolist()}); true labels {lr.loc['Summer', 'kappa_mean']:.3f}; \"\n      f\"{time.time() - started:.0f} s\")\n''', [\"claim:fig3c-logreg-characters-location\"])\n\nresult(\"fig3c-logreg-characters-location\")\nresult(\"fig3c-logreg-cuts-lower\")\n\nmd(\"\"\"\n## fig3e-temporal-gap\n\n> Without temporal gaps between training, validation and test samples, decoding of Summer is\n> almost perfect (kappa 0.99), and it falls to 0.31 as the gap grows to 32 s.\n\"\"\")\n\ncode(r'''\nrng_gap = np.random.default_rng(35)\ny = Y[\"Summer\"]\nsizes = tuple(len(i) for i in folds[0])\nstarted = time.time()\njobs = [(summer.fit_logreg, (S, y, *summer.random_split(n, sizes, rng_gap))) for _ in range(5)]\nfor gap in (4, 8, 16):\n    jobs += [(summer.fit_logreg, (S, y, *summer.split(n, f, gap_s=gap))) for f in range(5)]\nout = summer.run_jobs(jobs)\ngap_rows = {\"random\": [r[\"kappa\"] for r in out[:5]]}\nfor j, gap in enumerate((4, 8, 16)):\n    gap_rows[f\"{gap} s\"] = [r[\"kappa\"] for r in out[5 + 5 * j: 10 + 5 * j]]\ngap_rows[\"32 s\"] = [fits[(\"Summer\", f)][\"kappa\"] for f in range(5)]\npaper_gap = {\"random\": 0.987, \"4 s\": 0.584, \"8 s\": 0.539, \"16 s\": 0.429, \"32 s\": 0.309}\ngt = pd.DataFrame({k: {\"kappa_mean\": np.mean(v), \"sem\": np.std(v, ddof=1) / np.sqrt(5), \"min\": np.min(v), \"max\": np.max(v),\n                       \"paper_lstm\": paper_gap[k]} for k, v in gap_rows.items()}).T\nprint(f\"{len(jobs)} fits in {time.time() - started:.0f} s\")\nprint(gt.round(3).to_string())\nprint(\"(paper LSTM values from the dataset's code, buffer_lengths/comparison_performance.ipynb)\")\n''', [\"claim:fig3e-temporal-gap\"])\n\nresult(\"fig3e-temporal-gap\")\n\nmd(\"\"\"\n## fig4-patients-below-pooled\n\n> Decoding from a single patient's neurons is lower than from the pooled population; no patient\n> matches the pooled performance, for Summer, Scene Cuts or Indoor/Outdoor.\n\"\"\")\n\ncode(r'''\nstarted = time.time()\nPAT_LABELS = (\"Summer\", \"Scene Cuts\", \"Indoor/Outdoor\")\nkeys, jobs = [], []\nfor p in sorted(units.patient.unique()):\n    cols = units.index[units.patient == p].to_numpy()\n    for name in PAT_LABELS:\n        for f in range(5):\n            keys.append((p, name, f))\n            jobs.append((summer.fit_logreg, (S, Y[name], *folds[f], cols)))\npfits = dict(zip(keys, summer.run_jobs(jobs)))\nprint(f\"{len(jobs)} per-patient fits in {time.time() - started:.0f} s\")\npt = pd.DataFrame({name: {p: np.mean([pfits[(p, name, f)][\"kappa\"] for f in range(5)]) for p in sorted(units.patient.unique())}\n                   for name in PAT_LABELS})\npt.insert(0, \"units\", units.groupby(\"patient\").size())\nprint(pt.round(3).to_string())\nfor name in PAT_LABELS:\n    pooled = lr.loc[name, \"kappa_mean\"]\n    print(f\"{name}: pooled {pooled:.3f}; best patient {pt[name].idxmax()} at {pt[name].max():.3f}; \"\n          f\"patients at or above pooled: {int((pt[name] >= pooled).sum())}; median patient {pt[name].median():.3f}\")\n''', [\"claim:fig4-patients-below-pooled\"])\n\nresult(\"fig4-patients-below-pooled\")\n\nmd(\"\"\"\n## fig4-named-patients\n\n> For Summer, patients 7, 10, 15 and 22 exceed kappa 0.2; for Indoor/Outdoor, patients 2, 13, 20\n> and 25 exceed 0.2.\n\"\"\")\n\ncode(r'''\nnamed = {\"Summer\": [7, 10, 15, 22], \"Indoor/Outdoor\": [2, 13, 20, 25], \"Scene Cuts\": [2, 10, 19, 20]}\nhits = 0\nfor name, ps in named.items():\n    vals = pt.loc[ps, name]\n    above = pt.index[pt[name] > 0.2].tolist()\n    if name != \"Scene Cuts\":\n        hits += int((vals > 0.2).sum())\n    print(f\"{name}: named patients {dict(zip(ps, vals.round(3)))}; all patients above 0.2: {above}; \"\n          f\"top 4 here: {pt[name].nlargest(4).index.tolist()}\")\nprint(\"named Summer and Indoor/Outdoor pairs above 0.2:\", hits, \"of 8\")\nprint(\"(Scene Cuts: the paper says only that these patients show slightly better results)\")\n''', [\"claim:fig4-named-patients\"])\n\nresult(\"fig4-named-patients\")\n\nmd(\"\"\"\n## fig5-region-decoding\n\n> Decoding from single regions depends on the feature; the amygdala is best and the hippocampus\n> worst for Summer, and the parahippocampal cortex is best and the amygdala worst for\n> Indoor/Outdoor.\n\"\"\")\n\ncode(r'''\nstarted = time.time()\nREG_LABELS = (\"Summer\", \"Indoor/Outdoor\")\nkeys, jobs = [], []\nfor region in (\"A\", \"H\", \"EC\", \"PHC\"):\n    cols = units.index[units.region == region].to_numpy()\n    for name in REG_LABELS:\n        for f in range(5):\n            keys.append((region, name, f))\n            jobs.append((summer.fit_logreg, (S, Y[name], *folds[f], cols)))\nrfits = dict(zip(keys, summer.run_jobs(jobs)))\nprint(f\"{len(jobs)} region fits in {time.time() - started:.0f} s\")\nrt = pd.DataFrame({name: {region: np.mean([rfits[(region, name, f)][\"kappa\"] for f in range(5)]) for region in (\"A\", \"H\", \"EC\", \"PHC\")}\n                   for name in REG_LABELS})\nrs = pd.DataFrame({name: {region: np.std([rfits[(region, name, f)][\"kappa\"] for f in range(5)], ddof=1) / np.sqrt(5)\n                          for region in (\"A\", \"H\", \"EC\", \"PHC\")} for name in REG_LABELS})\nprint(\"mean kappa:\")\nprint(rt.round(3).to_string())\nprint(\"SEM:\")\nprint(rs.round(3).to_string())\nprint(\"units:\", units.region.value_counts()[[\"A\", \"H\", \"EC\", \"PHC\"]].to_dict())\nprint(\"paper (LSTM): Summer A 0.285, H 0.091, EC 0.191, PHC 0.171 (dataset code); Indoor/Outdoor PHC 0.30, H 0.26, EC 0.15, A 0.10 (Results)\")\ncond = {\"Summer, A highest\": rt.Summer.idxmax() == \"A\", \"Summer, H lowest\": rt.Summer.idxmin() == \"H\",\n        \"Indoor/Outdoor, PHC highest\": rt[\"Indoor/Outdoor\"].idxmax() == \"PHC\", \"Indoor/Outdoor, A lowest\": rt[\"Indoor/Outdoor\"].idxmin() == \"A\"}\nprint(cond, \"; holding:\", sum(cond.values()), \"of 4\")\n''', [\"claim:fig5-region-decoding\"])\n\nresult(\"fig5-region-decoding\")\n\nmd(\"\"\"\n## fig6-responsive-subsets\n\n> Responsive neurons drive decoding of camera cuts but not of Summer; without them, Summer is\n> decoded about as well as from all neurons while camera cuts drop the most, and responsive\n> neurons alone decode camera cuts about as well as all neurons but Summer less well.\n\"\"\")\n\ncode(r'''\nrng_sub = np.random.default_rng(36)\nstarted = time.time()\nkeys, jobs = [], []\nsets = {}\nfor name in (\"Summer\", \"Camera Cuts\"):\n    r = (P[name] <= 0.001).to_numpy()\n    sets[(name, \"responsive only\")] = np.where(r)[0]\n    sets[(name, \"non-responsive only\")] = np.where(~r)[0]\n    for d in range(3):\n        sets[(name, f\"non-responsive, size-matched {d + 1}\")] = np.sort(rng_sub.choice(np.where(~r)[0], r.sum(), replace=False))\nfor (name, kind), cols in sets.items():\n    for f in range(5):\n        keys.append((name, kind, f))\n        jobs.append((summer.fit_logreg, (S, Y[name], *folds[f], cols)))\nsfits = dict(zip(keys, summer.run_jobs(jobs)))\nprint(f\"{len(jobs)} subset fits in {time.time() - started:.0f} s\")\nrows = []\nfor name in (\"Summer\", \"Camera Cuts\"):\n    rows.append({\"label\": name, \"set\": \"complete\", \"units\": S.shape[1], \"kappa\": lr.loc[name, \"kappa_mean\"], \"sem\": lr.loc[name, \"kappa_sem\"]})\n    for (nm, kind), cols in sets.items():\n        if nm == name:\n            ks = [sfits[(name, kind, f)][\"kappa\"] for f in range(5)]\n            rows.append({\"label\": name, \"set\": kind, \"units\": len(cols), \"kappa\": np.mean(ks), \"sem\": np.std(ks, ddof=1) / np.sqrt(5)})\nsub = pd.DataFrame(rows)\nprint(sub.round(3).to_string(index=False))\nk = sub.set_index([\"label\", \"set\"]).kappa\ndrop_s = k[\"Summer\", \"complete\"] - k[\"Summer\", \"non-responsive only\"]\ndrop_c = k[\"Camera Cuts\", \"complete\"] - k[\"Camera Cuts\", \"non-responsive only\"]\ncond = {\"a: Summer without responsive >= complete - 0.05\": k[\"Summer\", \"non-responsive only\"] >= k[\"Summer\", \"complete\"] - 0.05,\n        \"b: Summer responsive only < complete - 0.05\": k[\"Summer\", \"responsive only\"] < k[\"Summer\", \"complete\"] - 0.05,\n        \"c: drop without responsive larger for camera cuts\": drop_c > drop_s,\n        \"d: camera cuts responsive only >= complete - 0.05\": k[\"Camera Cuts\", \"responsive only\"] >= k[\"Camera Cuts\", \"complete\"] - 0.05}\nprint(f\"drop without responsive units: Summer {drop_s:.3f}, Camera Cuts {drop_c:.3f}\")\nprint(cond, \"; holding:\", sum(bool(v) for v in cond.values()), \"of 4\")\n''', [\"claim:fig6-responsive-subsets\"])\n\nresult(\"fig6-responsive-subsets\")\n\nmd(\"\"\"\n## fig7b-top500-overlap\n\n> Across the five rankings of neurons by logistic regression weights for Summer, the top 500\n> neurons share 78 neurons, against about 1 expected by chance.\n\"\"\")\n\ncode(r'''\nrng_rank = np.random.default_rng(37)\nstarted = time.time()\ny = Y[\"Summer\"]\nkeys, jobs = [], []\nfor f in range(5):\n    for v in [j for j in range(5) if j != f]:\n        keys.append((f, v))\n        jobs.append((summer.fit_logreg, (S, y, *summer.split(n, f, val_fold=v))))\nkfits = dict(zip(keys, summer.run_jobs(jobs)))\nprint(f\"{len(jobs)} sub-split fits in {time.time() - started:.0f} s\")\nrankings, zero_in_top = [], []\nfor f in range(5):\n    coefs = [kfits[(f, v)][\"coef\"] for v in range(5) if v != f]\n    order = summer.ranking(coefs, rng_rank)\n    rankings.append(order)\n    nz = (np.abs(np.array(coefs)) > 0).any(0)\n    zero_in_top.append(int((~nz[order[:500]]).sum()))\n    print(f\"test fold {f + 1}: C {[kfits[(f, v)]['C'] for v in range(5) if v != f]}, units with a non-zero coefficient in any of the 4 models \"\n          f\"{int(nz.sum())}, in all 4 {int((np.abs(np.array(coefs)) > 0).all(0).sum())}; top 500 tied at zero {zero_in_top[-1]}; \"\n          f\"sub-split test kappa {np.round([kfits[(f, v)]['kappa'] for v in range(5) if v != f], 3).tolist()}\")\nN = S.shape[1]\nrows = []\nfor k_ in (100, 350, 500, 750, 1000):\n    common = set(rankings[0][:k_])\n    for o in rankings[1:]:\n        common &= set(o[:k_])\n    sims = [len(set.intersection(*[set(rng_rank.choice(N, k_, replace=False)) for _ in range(5)])) for _ in range(200)]\n    rows.append({\"top\": k_, \"common\": len(common), \"chance_formula\": N * (k_ / N) ** 5, \"chance_simulated\": np.mean(sims),\n                 \"paper_chance\": {100: 0, 350: 0, 500: 1, 750: 9, 1000: 37}[k_],\n                 \"common_responsive_to_summer\": int(np.sum(P[\"Summer\"].to_numpy()[list(common)] <= 0.001))})\nov = pd.DataFrame(rows)\nprint(ov.round(2).to_string(index=False))\ncommon500 = set(rankings[0][:500]).intersection(*[set(o[:500]) for o in rankings[1:]])\nprint(\"common 500 by region:\", units.loc[sorted(common500)].region.value_counts().to_dict(),\n      \"; patients:\", units.loc[sorted(common500)].patient.nunique())\n# Variant: zero-tied units ordered by unit index instead of a random draw (same order in every ranking).\norder_idx = [np.lexsort((np.arange(N), -np.abs(np.array([kfits[(f, v)][\"coef\"] for v in range(5) if v != f])).mean(0),\n                         -(np.abs(np.array([kfits[(f, v)][\"coef\"] for v in range(5) if v != f])) > 0).sum(0))) for f in range(5)]\nprint(\"variant, ties by unit index: common in top 500:\", len(set(order_idx[0][:500]).intersection(*[set(o[:500]) for o in order_idx[1:]])))\n''', [\"claim:fig7b-top500-overlap\"])\n\nresult(\"fig7b-top500-overlap\")\n\nmd(results.get(\"blocked\", \"## Blocked claims\\n\\npending\"))\nmd(results.get(\"summary\", \"## Summary\\n\\npending\"))\n\ncode(r'''\nprint(f\"total run time {(time.time() - started_all if 'started_all' in globals() else time.time() - started) / 60:.1f} min\")\n''')\n\nnb = nbf.v4.new_notebook()\nnb.cells = cells\nnb.metadata[\"kernelspec\"] = {\"display_name\": \"Python 3\", \"language\": \"python\", \"name\": \"python3\"}\nnbf.write(nb, ENTRY / \"reproduce_gerken_2025.ipynb\")\nprint(\"wrote\", len(cells), \"cells\")\n"
}
```

```
File created successfully at: /tmp/claude-1001/scratch/build_nb.py (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "entries/001616-gerken-2025/summer.py",
 "old_string": "def run_jobs(jobs, n_jobs: int = -1):",
 "new_string": "def fit_folds(S: np.ndarray, columns, labels: dict, splits: list) -> dict:\n    \"\"\"`fit_logreg` for each label and split on one subset of units, sliced once.\"\"\"\n    X = np.ascontiguousarray(S[:, columns])\n    return {(name, f): fit_logreg(X, y, *sp) for name, y in labels.items() for f, sp in enumerate(splits)}\n\n\ndef run_jobs(jobs, n_jobs: int = -1):"
}
```

```
The file entries/001616-gerken-2025/summer.py has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd /tmp/claude-1001/scratch && python - <<'EOF'
p='build_nb.py'; s=open(p).read()
s=s.replace('''started = time.time()
sessions = summer.load_all()''','''started_all = started = time.time()
sessions = summer.load_all()''')
s=s.replace('''parts = []
for (f, (ts, r, ev)), df, in zip(jobs, out):
    pass
''','')
s=s.replace('''print(f"total run time {(time.time() - started_all if 'started_all' in globals() else time.time() - started) / 60:.1f} min")''','''print(f"total run time {(time.time() - started_all) / 60:.1f} min")''')
# patients
s=s.replace('''keys, jobs = [], []
for p in sorted(units.patient.unique()):
    cols = units.index[units.patient == p].to_numpy()
    for name in PAT_LABELS:
        for f in range(5):
            keys.append((p, name, f))
            jobs.append((summer.fit_logreg, (S, Y[name], *folds[f], cols)))
pfits = dict(zip(keys, summer.run_jobs(jobs)))
print(f"{len(jobs)} per-patient fits in {time.time() - started:.0f} s")''','''pats = sorted(units.patient.unique())
out = summer.run_jobs([(summer.fit_folds, (S, units.index[units.patient == p].to_numpy(), {k: Y[k] for k in PAT_LABELS}, folds))
                       for p in pats])
pfits = {(p, name, f): r for p, o in zip(pats, out) for (name, f), r in o.items()}
print(f"{len(pfits)} per-patient fits in {time.time() - started:.0f} s")''')
s=s.replace('''keys, jobs = [], []
for region in ("A", "H", "EC", "PHC"):
    cols = units.index[units.region == region].to_numpy()
    for name in REG_LABELS:
        for f in range(5):
            keys.append((region, name, f))
            jobs.append((summer.fit_logreg, (S, Y[name], *folds[f], cols)))
rfits = dict(zip(keys, summer.run_jobs(jobs)))
print(f"{len(jobs)} region fits in {time.time() - started:.0f} s")''','''REGS = ("A", "H", "EC", "PHC")
out = summer.run_jobs([(summer.fit_folds, (S, units.index[units.region == region].to_numpy(), {k: Y[k]}, folds))
                       for region in REGS for k in REG_LABELS])
rfits = {(region, name, f): r for (region, k), o in zip([(g, k) for g in REGS for k in REG_LABELS], out) for (name, f), r in o.items()}
print(f"{len(rfits)} region fits in {time.time() - started:.0f} s")''')
s=s.replace('''for (name, kind), cols in sets.items():
    for f in range(5):
        keys.append((name, kind, f))
        jobs.append((summer.fit_logreg, (S, Y[name], *folds[f], cols)))
sfits = dict(zip(keys, summer.run_jobs(jobs)))
print(f"{len(jobs)} subset fits in {time.time() - started:.0f} s")''','''out = summer.run_jobs([(summer.fit_folds, (S, cols, {name: Y[name]}, folds)) for (name, kind), cols in sets.items()])
sfits = {(name, kind, f): o[(name, f)] for ((name, kind), cols), o in zip(sets.items(), out) for f in range(5)}
print(f"{len(sfits)} subset fits in {time.time() - started:.0f} s")''')
open(p,'w').write(s)
EOF
grep -n "keys, jobs = \[\], \[\]" build_nb.py
```

```
768:keys, jobs = [], []
812:keys, jobs = [], []
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd entries/001616-gerken-2025 && cat > requirements.in <<'EOF'
dandi
h5py
joblib
matplotlib
numpy
pandas
remfile
scikit-learn
scipy
zetapy
EOF
cat > entry.yaml <<'EOF'
schema_version: 1
name: 001616-gerken-2025
type: reproduction
title: Single units of the human medial temporal lobe during a full-length movie (Gerken, Darcher et al. 2025)
description: Tests the findings of Gerken, Darcher et al. (eLife reviewed preprint 106758, 2025) on dandiset
  001616 (SUMMER), which holds 2286 units from 29 patients watching "500 Days of Summer" with 53 frame-wise
  annotations. It counts units responsive to the onsets of movie features, runs the cluster permutation
  test by region, and decodes characters, location and cuts with the paper's logistic regression, pooled,
  per patient, per region and on subsets of units. The paper's LSTM is not run.
license: Apache-2.0
notebooks:
- path: reproduce_gerken_2025.ipynb
  title: Reproducing Gerken, Darcher et al. (2025) from dandiset 001616
  runtime_minutes: 20
helpers:
- summer.py
related:
- id: dandi:001616/0.260702.0824
  relation: uses_data
- id: doi:10.7554/elife.106758.1
  relation: reproduces
EOF
cat ../../schemas/entry.schema.json | python -c "import json,sys;s=json.load(sys.stdin);print(json.dumps(s['properties'],indent=0)[:1500])"; cd /tmp/claude-1001/scratch && . .venv/bin/activate && uv pip install -q ipykernel nbconvert nbformat joblib zetapy && python build_nb.py
```

```
{
"schema_version": {
"const": 1
},
"name": {
"description": "Unique across the registry, and the name of the entry's directory.",
"type": "string",
"pattern": "^[a-z0-9]+(-[a-z0-9]+)*$",
"maxLength": 100
},
"type": {
"enum": [
"orientation",
"reproduction",
"analysis"
]
},
"title": {
"type": "string",
"minLength": 1,
[... 73 more lines not kept]
```

**Agent**

Now a development run of the full notebook (streams the data; may take ~20 minutes).

**Agent calls Bash**

```bash
cd /tmp/claude-1001/scratch && . .venv/bin/activate && mkdir -p run && cp entries/001616-gerken-2025/{summer.py,reproduce_gerken_2025.ipynb} run/ && python -m ipykernel install --prefix .venv --name scratchk >/dev/null 2>&1; cd run && time JUPYTER_PATH=/tmp/claude-1001/scratch/.venv/share/jupyter python -m jupyter nbconvert --to notebook --execute --ExecutePreprocessor.timeout=7200 --ExecutePreprocessor.kernel_name=scratchk --output executed.ipynb reproduce_gerken_2025.ipynb 2>&1 | tail -30
```

```
[32m-> [39m[32m1806[39m         [30;43mself[39;49m[30;43m.[39;49m[30;43m_raise_error_fast[39;49m[30;43m([39;49m[30;43m)[39;49m
[32m   1807[39m         [38;5;28;01mbreak[39;00m
[32m   1809[39m     nb_jobs = [38;5;28mlen[39m([38;5;28mself[39m._jobs)

[36mFile [39m[32m/tmp/claude-1001/scratch/.venv/lib/python3.12/site-packages/joblib/parallel.py:1885[39m, in [36mParallel._raise_error_fast[39m[34m(self)[39m
[32m   1881[39m [38;5;66;03m# If this error job exists, immediately raise the error by[39;00m
[32m   1882[39m [38;5;66;03m# calling get_result. This job might not exists if abort has been[39;00m
[32m   1883[39m [38;5;66;03m# called directly or if the generator is gc'ed.[39;00m
[32m   1884[39m [38;5;28;01mif[39;00m error_job [38;5;129;01mis[39;00m [38;5;129;01mnot[39;00m [38;5;28;01mNone[39;00m:
[32m-> [39m[32m1885[39m     [30;43merror_job[39;49m[30;43m.[39;49m[30;43mget_result[39;49m[30;43m([39;49m[30;43mself[39;49m[30;43m.[39;49m[30;43mtimeout[39;49m[30;43m)[39;49m

[36mFile [39m[32m/tmp/claude-1001/scratch/.venv/lib/python3.12/site-packages/joblib/parallel.py:780[39m, in [36mBatchCompletionCallBack.get_result[39m[34m(self, timeout)[39m
[32m    774[39m backend = [38;5;28mself[39m.parallel._backend
[32m    776[39m [38;5;28;01mif[39;00m backend.supports_retrieve_callback:
[32m    777[39m     [38;5;66;03m# We assume that the result has already been retrieved by the[39;00m
[32m    778[39m     [38;5;66;03m# callback thread, and is stored internally. It's just waiting to[39;00m
[32m    779[39m     [38;5;66;03m# be returned.[39;00m
[32m--> [39m[32m780[39m     [38;5;28;01mreturn[39;00m [30;43mself[39;49m[30;43m.[39;49m[30;43m_return_or_raise[39;49m[30;43m([39;49m[30;43m)[39;49m
[32m    782[39m [38;5;66;03m# For other backends, the main thread needs to run the retrieval step.[39;00m
[32m    783[39m [38;5;28;01mtry[39;00m:
[... 15 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/001616-gerken-2025 && python - <<'EOF'
p='summer.py'; s=open(p).read()
s=s.replace('''    """Label of each 80 ms bin, from its first frame; values other than 0 and 1 (99, excluded)
    are kept as they are."""
    return frame_labels(session, label)[session["bin_frames"][:-1] - 1]''','''    """Label of each 80 ms bin, from its first frame (`movie_binning_info` gives one frame per
    bin); values other than 0 and 1 (99, excluded) are kept as they are."""
    return frame_labels(session, label)[session["bin_frames"] - 1]''')
open(p,'w').write(s)
EOF
cd /tmp/claude-1001/scratch && . .venv/bin/activate && cp entries/001616-gerken-2025/summer.py run/ && cd run && time JUPYTER_PATH=/tmp/claude-1001/scratch/.venv/share/jupyter python -m jupyter nbconvert --to notebook --execute --allow-errors --ExecutePreprocessor.timeout=7200 --ExecutePreprocessor.kernel_name=scratchk --output executed.ipynb reproduce_gerken_2025.ipynb 2>&1 | tail -3
```

```
[NbConvertApp] Converting notebook reproduce_gerken_2025.ipynb to notebook
[IPKernelApp] WARNING | Kernel is running over TCP without encryption. All communication (including code and outputs) is sent in plain text and is susceptible to eavesdropping. Use IPC transport or launch with kernel manager-provisioned CurveZMQ keys to enable transport encryption.
[NbConvertApp] Writing 130789 bytes to executed.ipynb

real	16m52.628s
user	47m23.785s
sys	2m46.980s
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd /tmp/claude-1001/scratch/run && python - <<'EOF'
import json
nb=json.load(open('executed.ipynb'))
for i,c in enumerate(nb['cells']):
    if c['cell_type']!='code': 
        print(f'[{i} MD]', ''.join(c['source'])[:80].replace('\n',' ')); continue
    print(f'----- [{i}] tags={c["metadata"].get("tags")}')
    for o in c.get('outputs',[]):
        if o['output_type']=='stream': print(''.join(o['text'])[:6000])
        elif o['output_type']=='error': print('ERROR', o['ename'], o['evalue'])
        elif 'text/plain' in o.get('data',{}): print(''.join(o['data']['text/plain'])[:300])
EOF
```

```
<persisted-output>
Output too large (39.5KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/3a2bc7d8-533c-480a-983e-8dfeabc62c0c/tool-results/b1p8dm77r.txt

Preview (first 2KB):
[0 MD] # header pending
----- [1] tags=None
loaded 29 files, 2286 units, from dandiset 001616 version 0.260702.0824 in 124 s

[2 MD] ## Data check  Each check of the metadata against the values is stated under its
----- [3] tags=['sanity']
version 0.260702.0824: 29 NWB files; version 0.260519.1133: 57 NWB files
files of 0.260519.1133 also in the pinned version, same path and blob: 29 of 29
files only in 0.260519.1133: 28, named like sub-1/sub-1_ses-1_behavior+ecephys.nwb

 patient  units_old  units_pinned  spikes_old  spikes_pinned  same_spike_times  same_regions
       1         40            40      397655         397655              True          True
       2         83            83      535482         535482              True          True
       4        120           120     2087660        2087660              True          True
       5         79            79      948767         948767              True          True
       6         99            99     1271620        1271620              True          True
[... 13 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/3a2bc7d8-533c-480a-983e-8dfeabc62c0c/tool-results/b1p8dm77r.txt",
 "offset": 30
}
```

```
30	      20         88            88     1159216        1159216              True          True
31	      21        109           109     1291303        1291303              True          True
32	      22         79            79     1258690        1258690              True          True
33	      23         50            50      303595         303595              True          True
34	      24         88            88      403093         403093              True          True
35	      25        110           110      515371         515371              True          True
36	      26         85            85      420460         420460              True          True
37	      27         90            90      910449         910449              True          True
38	      28        111           111     1559006        1559006              True          True
39	      29         66            66      229656         229656              True          True
40	patients of the pinned version without an older copy: [3]
41	older copies with the same spike times as the pinned file: 28 of 28
42	
43	[4 MD] **Result: pending (md_versions).**
44	----- [5] tags=['sanity']
45	patients 29; female 17, male 12; ages 19 to 62 years (median 40)
46	units 2286 (1190 marked single units); per patient 30 to 137
47	
48	Units by `brain_region` as stored:
49	brain_region
[... 547 more lines not kept]
```

**Agent calls Bash**

```bash
cd /tmp/claude-1001/scratch && . .venv/bin/activate && cp entries/001616-gerken-2025/summer.py . && python - <<'EOF'
import pickle, numpy as np, summer
S=pickle.load(open('sessions.pkl','rb'))
units=summer.unit_table(S); spk=summer.movie_spikes(S)
ann=S[0]['annotations_base']
cuts=summer.onsets(ann,'camera-cuts',1,min_presence=None)
edges=np.arange(-2,2.0001,0.05)
def psth(ev, idx):
    out=[]
    for i in idx:
        t=spk[i]
        if len(t)<500: continue
        h=np.zeros(len(edges)-1)
        rel=np.concatenate([t[(t>e-2)&(t<e+2)]-e for e in ev])
        h=np.histogram(rel,edges)[0]/len(ev)/0.05
        out.append(h/ (len(t)/(t[-1]-t[0])))
    return np.mean(out,0)
for reg in ['PHC','A','H','EC']:
    idx=units.index[units.region==reg]
    p=psth(cuts, idx)
    print(reg, ' '.join(f'{x:.2f}' for x in p))
rng=np.random.default_rng(0); rnd=np.sort(rng.uniform(40,4700,len(cuts)))
print('rnd', ' '.join(f'{x:.2f}' for x in psth(rnd, units.index[units.region=="PHC"])))
print(edges[:-1][::4])
EOF
```

```
PHC 1.02 1.00 0.99 0.99 1.02 0.99 1.01 1.00 0.99 1.01 1.00 0.99 1.01 0.99 0.99 0.99 0.98 1.00 1.01 0.98 1.00 1.00 0.99 0.99 1.01 0.98 0.99 1.00 1.00 1.00 0.98 1.00 0.96 0.99 0.99 0.98 0.99 0.99 0.98 0.99 0.97 0.98 0.99 1.01 1.13 1.10 1.10 1.06 1.05 1.06 1.05 1.04 1.02 1.04 1.01 1.03 1.04 1.02 1.00 1.00 1.01 1.01 1.00 1.02 1.02 1.01 1.00 1.00 0.99 1.01 1.00 1.01 0.97 1.00 0.99 1.01 0.98 0.98 0.99 0.99
A 1.01 0.99 1.02 1.00 1.00 1.01 0.99 1.02 0.99 0.97 1.00 1.00 1.01 1.03 1.01 1.01 1.00 0.99 1.01 1.01 0.99 1.01 0.99 1.03 1.03 1.00 0.99 1.01 1.01 1.00 1.01 1.02 1.02 1.01 1.02 1.02 1.02 1.01 1.01 1.01 1.01 1.01 0.99 0.99 0.97 0.98 0.97 0.95 0.96 0.97 0.96 0.96 0.99 0.99 1.01 1.03 1.00 1.03 1.05 1.01 1.02 1.02 1.02 1.01 1.03 1.01 1.03 1.01 1.02 1.01 1.01 1.01 1.02 1.00 1.00 1.01 1.00 1.03 1.01 1.00
H 1.00 1.00 0.99 0.99 1.00 1.00 0.98 0.99 0.99 0.99 0.99 0.99 0.99 0.99 1.00 1.00 0.99 1.00 0.99 1.01 1.00 1.00 0.99 0.99 1.01 1.02 1.01 1.00 0.99 1.01 0.99 0.99 1.01 1.00 1.00 1.00 0.99 0.99 0.99 0.99 0.99 1.01 0.98 0.99 0.98 0.99 0.97 0.97 0.99 0.99 0.99 1.00 1.00 0.99 0.99 1.00 1.00 1.00 1.00 0.99 0.99 1.00 1.00 0.99 1.00 0.98 0.99 0.99 1.00 1.00 0.99 0.99 1.01 0.99 0.99 1.00 0.98 0.99 1.00 0.99
EC 1.00 1.00 0.99 0.99 0.98 0.98 1.00 1.01 1.01 1.00 0.98 1.01 1.00 0.99 0.99 0.99 1.01 1.00 0.98 1.00 0.99 0.97 0.99 0.99 0.99 0.97 0.99 0.99 0.99 1.00 1.01 1.00 0.99 0.98 0.99 1.00 1.02 1.01 0.99 1.00 0.98 1.00 0.99 0.99 0.99 0.96 0.96 0.98 0.97 0.98 0.98 0.97 0.99 1.00 1.02 1.01 1.01 1.01 1.02 1.02 1.01 1.00 1.00 1.00 1.01 1.01 1.00 0.99 1.02 0.98 0.99 0.98 1.00 1.01 0.99 1.00 0.99 0.98 0.98 0.99
rnd 1.00 0.99 1.01 0.99 1.00 0.99 1.00 1.00 0.98 1.00 1.00 1.00 1.01 1.01 0.99 1.02 0.99 0.98 1.00 1.00 0.98 1.01 0.99 0.99 0.98 0.99 0.97 0.99 0.99 0.97 0.98 1.01 0.99 0.98 1.00 0.97 1.01 1.00 1.00 0.99 0.99 0.99 1.00 1.01 1.00 1.02 1.00 0.98 0.99 1.01 1.01 1.02 0.98 1.00 1.00 1.02 1.02 1.00 0.98 0.99 1.02 1.00 1.00 1.01 0.98 1.01 0.98 1.00 1.01 0.98 1.01 0.99 1.02 1.00 0.97 0.98 1.00 
[... 6 more lines not kept]
```

**Agent calls Bash**

```bash
cd /tmp/claude-1001/scratch && . .venv/bin/activate && python - <<'EOF'
import numpy as np, summer
rng=np.random.default_rng(0)
for rate in (0.5,2,10):
    ps=[]
    for k in range(200):
        t=np.sort(rng.uniform(0,5000,rng.poisson(rate*5000)))
        ev=np.sort(rng.uniform(10,4990,883))
        ps.append(summer.wilcoxon_simes(t,ev)[0])
    ps=np.array(ps); print(rate,'Hz: frac p<=0.001',np.mean(ps<=0.001),'p<=0.01',np.mean(ps<=0.01))
for rate in (2,):
    ps=[]
    for k in range(200):
        t=np.sort(rng.uniform(0,5000,rng.poisson(rate*5000)))
        ev=np.sort(rng.uniform(10,4990,40))
        ps.append(summer.wilcoxon_simes(t,ev)[0])
    ps=np.array(ps); print('40 events',rate,'Hz: frac p<=0.001',np.mean(ps<=0.001),'p<=0.01',np.mean(ps<=0.01))
EOF
```

```
0.5 Hz: frac p<=0.001 1.0 p<=0.01 1.0
2 Hz: frac p<=0.001 1.0 p<=0.01 1.0
10 Hz: frac p<=0.001 0.27 p<=0.01 0.61
40 events 2 Hz: frac p<=0.001 0.165 p<=0.01 0.485
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd /tmp/claude-1001/scratch && python - <<'EOF'
p='build_nb.py'; s=open(p).read()
old_clock_start = s.index("code(r'''\n# Clock check: does each patient's population respond")
old_clock_end = s.index("result(\"md_clock\")")
new_clock = r'''code(r"""
# Clock check: does each patient's population change its rate after camera cuts at the annotated
# times, and not at the same number of random times? Index = mean over units with 100 or more
# spikes of |rate 200-600 ms after - rate 400-0 ms before| / unit's mean rate; increases and
# decreases both count, as regions differ in sign (pooled PSTH below).
rng_clock = np.random.default_rng(1)
ann = sessions[0]["annotations_base"]
cuts = summer.onsets(ann, "camera-cuts", 1, min_presence=None)


def cut_index(ts, ev):
    vals = []
    for t in ts:
        if len(t) < 100:
            continue
        rate = len(t) / (t[-1] - t[0])
        after = summer._counts_in(t, ev + 0.2, 0.4).mean() / 0.4
        before = summer._counts_in(t, ev - 0.4, 0.4).mean() / 0.4
        vals.append(abs(after - before) / rate)
    return np.mean(vals)


rows = []
for s in sessions:
    p = int(s["subject_id"])
    ts = [np.sort(spikes[i]) for i in units.index[units.patient == p]]
    lo, hi = s["cleaned_watchlogs"].pts.iloc[0] + 1, s["cleaned_watchlogs"].pts.iloc[-1] - 1
    ev = cuts[(cuts > lo) & (cuts < hi)]
    true = cut_index(ts, ev)
    null = np.array([cut_index(ts, np.sort(rng_clock.uniform(lo, hi, len(ev)))) for _ in range(20)])
    rows.append({"patient": p, "cuts": len(ev), "index_true": true, "index_shift_2s": cut_index(ts, ev + 2.0),
                 "null_mean": null.mean(), "null_sd": null.std(), "z": (true - null.mean()) / null.std()})
clock = pd.DataFrame(rows)
print(clock.round(3).to_string(index=False))
print("patients with z above 3:", int((clock.z > 3).sum()), "of", len(clock), "; not above 3:", clock.patient[clock.z <= 3].tolist())

# Pooled PSTH around camera cuts, by region (rate / unit's mean rate, 100 ms bins from -1 to 1 s).
bins = np.arange(-1.0, 1.0001, 0.1)
ps = {}
for region in ("A", "H", "EC", "PHC"):
    vals = []
    for i in units.index[units.region == region]:
        t = np.sort(spikes[i])
        if len(t) < 100:
            continue
        rate = len(t) / (t[-1] - t[0])
        vals.append(summer._counts_in(t, (cuts[:, None] + bins[None, :-1]).ravel(), 0.1).reshape(len(cuts), -1).mean(0) / 0.1 / rate)
    ps[region] = np.mean(vals, 0)
print("\npooled rate around camera cuts / mean rate, bins starting at (s):")
print(pd.DataFrame(ps, index=np.round(bins[:-1], 1)).T.round(3).to_string())
""", ["sanity"])

'''
s = s[:old_clock_start] + new_clock + s[old_clock_end:]
s = s.replace('code(r"""', "code(r'''").replace('""", ["sanity"])\n\n', "''', [\"sanity\"])\n\n")
# calibration cell after responsive_counts definition
anchor = '''def responsive_counts(pv, alpha):
    r = pv <= alpha
    by_region = r.groupby(units.region).sum()
    return r.sum(), by_region
\'\'\')
'''
calib = anchor + r'''
md("""
The Methods' test is checked against chance: the same test with random event times (as many as
there are camera cut onsets, within each patient's playback), for every unit, and on synthetic
units firing as stationary Poisson processes with random events.
""")

code(r"""
rng_calib = np.random.default_rng(21)
null_rows = []
for s in sessions:
    p = int(s["subject_id"])
    lo, hi = s["cleaned_watchlogs"].pts.iloc[0] + 1, s["cleaned_watchlogs"].pts.iloc[-1] - 1
    ev = np.sort(rng_calib.uniform(lo, hi, len(events["Camera Cuts"])))
    for i in units.index[units.patient == p]:
        null_rows.append({"unit": i, "region": units.region[i], "p": summer.wilcoxon_simes(spikes[i], ev)[0]})
null = pd.DataFrame(null_rows)
print("Methods' test at random times, fraction of units 'responsive':")
print(null.groupby("region").p.agg(**{"alpha_0.001": lambda v: np.mean(v <= 0.001), "alpha_0.01": lambda v: np.mean(v <= 0.01),
                                       "units": "size"}).round(3).to_string())
print("all units:", {a: round(float(np.mean(null.p <= a)), 3) for a in summer.ALPHAS})
null_p = null.set_index("unit").p
synth = []
for rate in (2.0, 10.0):
    for n_ev in (40, 883):
        ps_ = []
        for _ in range(100):
            t = np.sort(rng_calib.uniform(0, 5000, rng_calib.poisson(rate * 5000)))
            ps_.append(summer.wilcoxon_simes(t, np.sort(rng_calib.uniform(10, 4990, n_ev)))[0])
        synth.append({"rate_hz": rate, "events": n_ev, "alpha_0.001": np.mean(np.array(ps_) <= 0.001),
                      "alpha_0.01": np.mean(np.array(ps_) <= 0.01)})
print("\nsynthetic Poisson units, 100 each, fraction 'responsive':")
print(pd.DataFrame(synth).to_string(index=False))
""")
'''
assert anchor in s
s = s.replace(anchor, calib)
s = s.replace('code(r"""\nrng_calib', "code(r'''\nrng_calib").replace('print(pd.DataFrame(synth).to_string(index=False))\n""")', "print(pd.DataFrame(synth).to_string(index=False))\n''')")
# fig2b: remove PHC-only null, use null_p
old_null_start = s.index("# Reference: the same test at random event times (same number of events, within each patient's playback).")
old_null_end = s.index('print("\\nPer patient, PHC units responsive to camera cuts')
s = s[:old_null_start] + '''print("random event times (calibration above), PHC units responsive (%):",
      {a: round(100 * float((null_p[phc] <= a).mean()), 2) for a in summer.ALPHAS})
''' + s[old_null_end:]
s = s.replace("rng_fig2b = np.random.default_rng(22)\n", "")
# ZETA null
s = s.replace('''zeta = pd.DataFrame(zeta_rows)''','''zeta = pd.DataFrame(zeta_rows)
rng_zeta = np.random.default_rng(25)
tasks = []
for s in sessions:
    p = int(s["subject_id"])
    w = s["cleaned_watchlogs"]
    lo, hi = w.rec_ms.iloc[0] + 1000, w.rec_ms.iloc[-1] - 1000
    ev = np.sort(rng_zeta.uniform(lo, hi, len(events["Camera Cuts"])))
    for i in units.index[(units.patient == p) & (units.region == "PHC")]:
        tasks.append((i, s["spikes_ms"][units["index"][i]], ev))
zeta_null = np.array(Parallel(n_jobs=-1)(delayed(zeta_p)(sp, on, 1000 + j) for j, (i, sp, on) in enumerate(tasks)))''')
s = s.replace('''    print(name, {a: f"{int((z <= a).sum())} of {len(z)} ({100 * float((z <= a).mean()):.2f}%)" for a in summer.ALPHAS})
''','''    print(name, {a: f"{int((z <= a).sum())} of {len(z)} ({100 * float((z <= a).mean()):.2f}%)" for a in summer.ALPHAS})
print("ZETA at random times (as many as camera cut onsets), PHC units:",
      {a: f"{int((zeta_null <= a).sum())} of {len(zeta_null)} ({100 * float((zeta_null <= a).mean()):.2f}%)" for a in summer.ALPHAS})
''')
s = s.replace('''print("reference, PHC units at random times (fig2b section), responsive at 0.001:", f"{100 * float((null_p <= 0.001).mean()):.2f}%")''','''print("reference, all units at random times (calibration above), responsive:", {a: f"{100 * float((null_p <= a).mean()):.2f}%" for a in summer.ALPHAS})''')
# fig6 size matched
s = s.replace('''    for d in range(3):
        sets[(name, f"non-responsive, size-matched {d + 1}")] = np.sort(rng_sub.choice(np.where(~r)[0], r.sum(), replace=False))''','''    if r.sum() <= (~r).sum():
        for d in range(3):
            sets[(name, f"non-responsive, size-matched {d + 1}")] = np.sort(rng_sub.choice(np.where(~r)[0], r.sum(), replace=False))
    else:
        print(f"{name}: {int(r.sum())} responsive and {int((~r).sum())} non-responsive units; no size-matched non-responsive set")''')
open(p,'w').write(s)
EOF
grep -n '"""' /tmp/claude-1001/scratch/build_nb.py | head; cd /tmp/claude-1001/scratch && . .venv/bin/activate && python build_nb.py
```

```
1:"""Builds the notebook from cell sources. Conclusions are in results.py (filled after the run)."""
58:md("""
62:""")
274:md("""
281:""")
326:md("""
330:""")
360:md("""
364:""")
433:md("""
wrote 69 cells
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd entries/001616-gerken-2025 && python -c "
import json;nb=json.load(open('reproduce_gerken_2025.ipynb'))
for i,c in enumerate(nb['cells']):
    src=''.join(c['source'])
    if 'Clock check' in src or 'rng_calib' in src or 'checked against chance' in src: print(i,c['cell_type'],c['metadata']);print(src[:600]);print('...')
"
```

```
13 code {'tags': ['sanity']}
# Clock check: does each patient's population change its rate after camera cuts at the annotated
# times, and not at the same number of random times? Index = mean over units with 100 or more
# spikes of |rate 200-600 ms after - rate 400-0 ms before| / unit's mean rate; increases and
# decreases both count, as regions differ in sign (pooled PSTH below).
rng_clock = np.random.default_rng(1)
ann = sessions[0]["annotations_base"]
cuts = summer.onsets(ann, "camera-cuts", 1, min_presence=None)


def cut_index(ts, ev):
    vals = []
    for t in ts:
        if len(t) < 100:
            continue
     
...
17 markdown {}
The Methods' test is checked against chance: the same test with random event times (as many as
there are camera cut onsets, within each patient's playback), for every unit, and on synthetic
[... 24 more lines not kept]
```

**Agent calls Bash**

```bash
cd  && sed -i 's/model = LogisticRegression(l1_ratio=1.0, solver="liblinear", C=c, class_weight="balanced")/model = LogisticRegression(l1_ratio=1.0, solver="liblinear", C=c, class_weight="balanced", random_state=0)/' entries/001616-gerken-2025/summer.py && grep -n "random_state" entries/001616-gerken-2025/summer.py && python -c "import yaml,jsonschema,nbformat" && python tools/entry.py lock entries/001616-gerken-2025 && grep -E "^(zetapy|scikit-learn|numpy|scipy|dandi|joblib)==" entries/001616-gerken-2025/requirements.lock.txt
```

```
388:        model = LogisticRegression(l1_ratio=1.0, solver="liblinear", C=c, class_weight="balanced", random_state=0)
wrote entries/001616-gerken-2025/requirements.lock.txt
dandi==0.81.0
joblib==1.6.0
numpy==2.5.4
scikit-learn==1.9.1
scipy==1.18.1
zetapy==4.1
```

**Agent**

Locked. Running check and the clean-environment execution now (about 20 minutes).

**Agent calls Bash**

```bash
time python tools/entry.py all entries/001616-gerken-2025 2>&1 | tail -40
```

```
Installed kernelspec registry-001616-gerken-2025 in executed/001616-gerken-2025/.venv/share/jupyter/kernels/registry-001616-gerken-2025
0 error(s)
pass  reproduce_gerken_2025.ipynb  (1328 s)

real	22m13.874s
user	62m29.302s
sys	3m43.977s
```

**Agent calls Bash**

```bash
python - <<'EOF' > /tmp/claude-1001/scratch/out1.txt
import json
nb=json.load(open('executed/001616-gerken-2025/reproduce_gerken_2025.ipynb'))
for i,c in enumerate(nb['cells']):
    if c['cell_type']!='code': continue
    print(f'----- [{i}] tags={c["metadata"].get("tags")}')
    for o in c.get('outputs',[]):
        if o['output_type']=='stream': print(''.join(o['text']))
        elif o['output_type']=='error': print('ERROR', o['ename'], o['evalue'])
EOF
sed -n '/----- \[13\]/,/----- \[22\]/p' /tmp/claude-1001/scratch/out1.txt; grep -n "ZETA\|random event times\|ERROR\|total run\|subset fits\|size-matched\|holding\|drop without" /tmp/claude-1001/scratch/out1.txt
```

```
----- [13] tags=['sanity']
 patient  cuts  index_true  index_shift_2s  null_mean  null_sd      z
       1   883       0.125           0.124      0.113    0.021  0.560
       2   883       0.114           0.091      0.086    0.009  3.027
       3   883       0.161           0.087      0.086    0.013  5.869
       4   883       0.073           0.068      0.067    0.007  0.992
       5   883       0.122           0.079      0.092    0.010  3.125
       6   883       0.118           0.110      0.099    0.011  1.672
       7   883       0.112           0.095      0.091    0.009  2.284
       8   883       0.087           0.107      0.104    0.011 -1.539
       9   883       0.098           0.088      0.113    0.014 -1.024
      10   883       0.111           0.064      0.073    0.008  4.993
      11   883       0.097           0.112      0.090    0.015  0.428
      12   883       0.113           0.105      0.091    0.011  1.906
      13   883       0.127           0.086      0.088    0.009  4.449
      14   883       0.148           0.146      0.126    0.017  1.289
      15   883       0.152           0.102      0.116    0.010  3.766
      16   883       0.145           0.088      0.105    0.009  4.312
      17   883       0.125           0.087      0.094    0.012  2.478
      18   883       0.193           0.143      0.153    0.020  1.949
[... 400 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n '/----- \[3\]/,/----- \[13\]/p' /tmp/claude-1001/scratch/out1.txt | sed -n '1,12p;40,60p;95,175p'
```

```
----- [3] tags=['sanity']
version 0.260702.0824: 29 NWB files; version 0.260519.1133: 57 NWB files
files of 0.260519.1133 also in the pinned version, same path and blob: 29 of 29
files only in 0.260519.1133: 28, named like sub-1/sub-1_ses-1_behavior+ecephys.nwb

 patient  units_old  units_pinned  spikes_old  spikes_pinned  same_spike_times  same_regions
       1         40            40      397655         397655              True          True
       2         83            83      535482         535482              True          True
       4        120           120     2087660        2087660              True          True
       5         79            79      948767         948767              True          True
       6         99            99     1271620        1271620              True          True
       7         84            84     1577631        1577631              True          True
units 2286 (1190 marked single units); per patient 30 to 137

Units by `brain_region` as stored:
brain_region
A      559
EC     493
AH     418
PH     412
[... 94 more lines not kept]
```

**Agent**

The executed outputs are in. Writing the conclusions, blocked-claims section and summary into the notebook now.

**Agent calls Bash**

```bash
cat > /tmp/claude-1001/scratch/results.py <<'PYEOF'
import json
R = {}
R["header"] = """# Reproducing Gerken, Darcher et al. (2025) from dandiset 001616

Paper: Gerken F, Darcher A, Gonçalves PJ, Rapp R, Elezi I, Niediek J, Kehl MS, Reber TP, Liebe S,
Macke JH, Mormann F, Leal-Taixé L (2025). Decoding movie content from neuronal population activity in
the human medial temporal lobe. eLife reviewed preprint 106758, version 1.
[doi:10.7554/eLife.106758.1](https://doi.org/10.7554/eLife.106758.1). This attempt used the full
text, which is open access, and the supplementary file with Tables S1 and S2.

Dandiset: [DANDI:001616](https://dandiarchive.org/dandiset/001616/0.260702.0824), version
0.260702.0824 (SUMMER). The paper cites no DANDI version; its data statement says the data will be
published separately. This is the most recent published version. The earlier published version,
0.260519.1133, holds the same 29 files (same blobs) and 28 older copies of the same recordings with
identical spike times (shown in the data check), so the analysis would read the same data from
either; the pinned version holds each recording once.

Code read: the dataset's repository [mormannlab/SUMMER](https://github.com/mormannlab/SUMMER) at
commit 59fc242 (Zenodo 10.5281/zenodo.21165561 archives it). It holds the NWB conversion, the
responsive-unit and cluster code behind Figure 2, plotting notebooks that hold the paper's LSTM
results as numbers, and a simple linear training baseline. It does not hold the paper's LSTM or its
hyperparameters. The fold layout, the grouping of hippocampal subregions and the onset rule here
follow it, as stated in `summer.py`.

No data from outside the dandiset is used. Each claim's section has its own random generator; the
logistic regression is seeded, and each ZETA test is seeded. The notebook takes about 22 minutes,
most of it in the logistic regression fits and the ZETA variant.

| Claim | Status |
|---|---|
| dataset-composition | tested |
| fig2b-phc-camera-cuts | tested; blocked, the responsive test is not calibrated |
| tables1-camera-cuts-regions | tested; blocked, depends on the responsive test |
| fig2b-phc-scene-cuts | tested; blocked, the responsive test is not calibrated |
| tables1-few-semantic-responses | tested; blocked, the responsive test is not calibrated |
| tables1-no-indoor-response | tested; blocked, the responsive test is not calibrated |
| results-cluster-regions | tested; blocked, depends on the responsive test |
| fig3b-single-neuron-threshold | tested |
| fig3c-logreg-characters-location | tested |
| fig3c-logreg-cuts-lower | tested |
| fig3e-temporal-gap | tested, with the logistic regression in place of the LSTM |
| fig4-patients-below-pooled | tested |
| fig4-named-patients | tested, assuming subject ids are the paper's patient numbers |
| fig5-region-decoding | tested, with the logistic regression in place of the LSTM |
| fig6-responsive-subsets | tested, with the logistic regression; blocked, depends on the responsive test |
| fig7b-top500-overlap | tested |
| fig3c-lstm-decoding | blocked: the LSTM's code and hyperparameters are not published |
| fig3d-temporal-shuffle | blocked: as above |
| fig5-faces-presence | blocked: as above; face labels also lack the excluded frames |
| fig7a-500-neurons | blocked: as above |"""

R["md_versions"] = """The earlier published version holds the 29 files of the pinned version unchanged and 28 more,
named `ses-1_behavior+ecephys`, one per patient except patient 3. Each of these holds the same
units, regions and spike times as the pinned file of its patient, so that version deposits 28
recordings twice. The pinned version holds each recording once."""

R["md_units"] = """29 patients, 17 of them female, and 2286 units, 30 to 137 per patient, as the paper states. The
paper's Results give ages 22 to 63 for these 29 patients; the files give 19 to 62, the range the
Methods give for all 46 patients recorded. The region counts differ from the paper's (A 580, H 794,
EC 440, PHC 373, PIC 99): grouping AH, MH and PH as hippocampus, as the dataset's code does, gives
A 559, H 846, EC 493, PHC 293 and PIC 68, and 27 units lie in regions the paper does not name (FF,
LG, PRC). The totals agree, so the units were assigned to regions differently. Every unit's region
matches that of its electrode. No unit is labelled `H`; the dataset's training code
(`ML_framework/nwb_loading/nwb_loading.py`) compares `brain_region` with `H` when asked for the
hippocampus, so it would select no unit. The units table states its spike times in milliseconds,
where NWB expects seconds."""

R["md_timebase"] = """Every frame of the analysis portion (36.72 to 4763.16 s, credits excluded) is in every patient's
cleaned watchlog. Playback was paused in 24 patients, for up to 57 minutes in all (patient 1);
spikes in pauses are dropped (up to 298658 in patient 10). Frames advance every 40.68 to 41.79 ms
of the recording clock while the film has 40 ms frames, so the recording clock is in milliseconds
and playback ran 2 to 4% slower than 25 frames per second; spikes are mapped to movie time through
the watchlog, which absorbs this. Spikes span the logged playback in every file, and 15 files also
hold spikes outside it. The patient-aligned annotations agree with the movie-time annotations
mapped through the watchlog to a median of one frame (40.7 to 41.8 ms). Their start and stop
columns are described as seconds but hold milliseconds, as the table description says. In some
patients that table holds more onsets than the film has (up to 1181 camera cuts against 958),
apparently from replayed portions; the analysis uses the movie-time annotations. All files carry
the same annotations, indicator functions and 80 ms bin edges (59080 bins)."""

R["md_labels"] = """The fractions of frames match the paper's descriptions (Summer 0.53, Tom 0.79, Persons 0.95,
McKenzie 0.09 of the analysis frames). The dandiset has 958 camera cuts, one every 5.25 s, where
the supplement says one every 3 s. Its 133 scene cuts give a mean scene of 37.8 s (supplement
36.15 s), and 121 of them fall on a camera cut frame. Indoor/Outdoor is `indoor-setting`: 1 indoor,
0 outdoor, and 99 for 839 analysis frames that are neither. The face labels hold only 0 and 1,
while the Methods define face labels with a third state for excluded frames; those frames cannot be
identified from the dandiset."""

R["md_dupes"] = """No two units share their first 20 spike times and no two patients share a watchlog, so no
recording appears twice in the pinned version. Two units have no spike during playback."""

R["md_clock"] = """In 12 of 29 patients the population changes its rate after camera cuts more than after random
times (z above 3). In the other 17 (patients 1, 4, 6, 7, 8, 9, 11, 12, 14, 17, 18, 21, 24, 25, 26, 27
and 28) this check does not establish the alignment, though it does not contradict it. Pooled over
patients, the PHC rate rises to 1.09 times its mean 200 to 300 ms after a cut, and the A and EC rates
fall to 0.95 at 300 to 400 ms. Decoding Summer with its labels shifted by 300 s gives kappa 0.016
against 0.302 with the true labels (fig3c section). The spikes and annotations are consistent with
one clock: shown for the pooled data and for 12 patients one by one."""

R["fig2b-phc-camera-cuts"] = """**Result: blocked (methods_underspecified).** The Methods' test, as fixed in the claims file,
counts 222 of 293 PHC units (75.77%) responsive to camera cuts at alpha 0.001 and 228 (77.82%) at
0.01, against 51.74% in the paper. The same test counts 72.35% of PHC units, and 68.3% of all
units, responsive at random event times, and every synthetic Poisson unit with 883 random events.
Its false-positive rate is far from its alpha, so the procedure here is not the one that produced
the paper's counts, and the claim cannot be judged. The ZETA test of the dataset's code is
calibrated here (0 of 293 PHC units at random times at alpha 0.001, 4 at 0.01); it finds 37 of 293
(12.63%) responsive at 0.001 and 65 (22.18%) at 0.01, below the paper's 51.74%."""

R["tables1-camera-cuts-regions"] = """**Result: blocked (methods_underspecified)**, as it rests on the selection of
fig2b-phc-camera-cuts. The miscalibrated test counts 64 to 76% of the units of every region
responsive (A 73.70%, EC 74.04%, H 64.42%, PHC 75.77% at alpha 0.001), against 39 to 52% in the
paper, and 62 to 73% of the units of each region at random times."""

R["fig2b-phc-scene-cuts"] = """**Result: blocked (methods_underspecified).** The Methods' test counts 139 of 293 PHC units
(47.44%) responsive to scene cuts at alpha 0.001 and 179 (61.09%) at 0.01, against 6.70%; the test is
not calibrated (see fig2b-phc-camera-cuts). With this split, the cluster test finds no cluster with
the Methods' z-scoring (p = 1.000 at either alpha); with the code's per-trial z-scoring the largest
cluster has p = 0.048 at alpha 0.001 and there is none at 0.01. The ZETA test finds 8 of 293 PHC
units (2.73%) at alpha 0.001 and 30 (10.24%) at 0.01, either side of the tolerance of 4.16 to
9.24%."""

R["tables1-few-semantic-responses"] = """**Result: blocked (methods_underspecified).** The test counts 1017 units responsive to Summer and
1168 to Tom at alpha 0.001 (paper 46 and 216), and 9.80 to 51.09% of all units for each semantic
label, while it counts 68.3% at random times. The counts are dominated by the test's false
positives, so neither the counts nor the contrast with camera cuts (70.73%) can be judged."""

R["tables1-no-indoor-response"] = """**Result: blocked (methods_underspecified).** The test as fixed counts 279 units responsive to
Indoor onsets at alpha 0.001 (790 at 0.01), and 422 for McKenzie and 224 for Summer Presence, where
Table S1 has 0 for each; at random times it counts 68.33% of units. An absence cannot be judged with
a test whose false-positive rate is this far from its alpha."""

R["results-cluster-regions"] = """**Result: blocked (methods_underspecified)**, as the split into responsive and non-responsive
units comes from the miscalibrated test. With that split, 9 of 32 cells agree with the paper at
alpha 0.001 and 13 at 0.01. Camera cuts give no cluster in any region (p = 1.000), and PHC has 5
significant labels at alpha 0.001 against 7 in H."""

R["fig3b-single-neuron-threshold"] = """**Result: reproduced.** The median unit's kappa for Summer is 0.0077, 89.8% of units are below
0.05, and the best unit reaches 0.276 (patient 7, amygdala). No unit reaches the paper's population
value of 0.31, nor the pooled logistic regression here (0.302)."""

R["fig3c-logreg-characters-location"] = """**Result: reproduced.** Pooled over patients, the logistic regression gives kappa 0.302 for
Summer (SEM 0.056; paper 0.28) and 0.360 for Indoor/Outdoor (SEM 0.049; paper 0.31), both within
tolerance. Tom (0.217), McKenzie (0.317) and Persons (0.418) reach the LSTM values less their SEM
(0.17, 0.235, 0.312). Every fold is above chance by the test-label shuffle (p = 0.001, the smallest
possible with 1000 shuffles) for Summer, McKenzie, Persons and Indoor/Outdoor; for Tom one fold has
kappa 0 (p = 0.52). The value of C chosen on validation varies across folds (0.001 to 0.03); over
the grid, the test kappa ranges from 0.266 to 0.311 for Summer and from 0.349 to 0.392 for
Indoor/Outdoor. With the Summer labels shifted by 300 s the kappa is 0.016."""

R["fig3c-logreg-cuts-lower"] = """**Result: reproduced.** The logistic regression gives kappa 0.0745 for Scene Cuts (SEM 0.027) and
0.0967 for Camera Cuts (SEM 0.020), within the tolerances around 0.10 and 0.11 and below the LSTM
values of 0.20 and 0.18. Camera Cuts are above chance in every fold (p = 0.001); Scene Cuts are not
in one fold (kappa -0.014, p = 1.0)."""

R["fig3e-temporal-gap"] = """**Result: reproduced.** With samples assigned to training, validation and test at random, the
logistic regression decodes Summer with kappa 0.947 (5 draws, 0.942 to 0.952). With gaps of 4, 8, 16
and 32 s it gives 0.555, 0.524, 0.450 and 0.302, close to the LSTM values the dataset's code holds
for the same gaps (0.987 random, then 0.584, 0.539, 0.429 and 0.309)."""

R["fig4-patients-below-pooled"] = """**Result: reproduced.** No patient reaches the pooled kappa for any of the three labels. For
Summer the best patient is 7 at 0.268 against 0.302 pooled (median patient 0.060); for Scene Cuts
patient 20 at 0.044 against 0.075 (median 0.011); for Indoor/Outdoor patient 2 at 0.257 against
0.360 (median 0.099)."""

R["fig4-named-patients"] = """**Result: reproduced.** Taking subject ids as the paper's patient numbers, 7 of the 8 named pairs
exceed 0.2: for Summer patients 7 (0.268), 10 (0.227) and 22 (0.241), with 15 at 0.197; for
Indoor/Outdoor patients 2 (0.257), 13 (0.209), 20 (0.217) and 25 (0.202). The four best patients
here are 7, 22, 10 and 15 for Summer and 2, 20, 13 and 19 for Indoor/Outdoor. For Scene Cuts, the
patients the paper names (2, 10, 19, 20) are the four best here (0.027 to 0.044). That the named
patients come out on top supports the identity of the numbering, without proving it."""

R["fig5-region-decoding"] = """**Result: partially reproduced.** With the logistic regression, Summer is decoded best from the
amygdala (0.291) and worst from the hippocampus (0.066; EC 0.148, PHC 0.097), and Indoor/Outdoor
best from PHC (0.357), then H (0.301). The amygdala is not the lowest for Indoor/Outdoor: A (0.122)
and EC (0.117) differ by less than their SEMs (0.041, 0.052). Three of the four orderings hold. The
regions here hold different units from the paper's (PHC 293 against 373)."""

R["fig6-responsive-subsets"] = """**Result: blocked (methods_underspecified)**, as the responsive sets come from the miscalibrated
test (1017 of 2286 units for Summer and 1617 for Camera Cuts at alpha 0.001). With these sets, all
four conditions of the criterion hold: for Summer, 0.311 without responsive units against 0.302 for
all units, and 0.245 with responsive units only; for Camera Cuts, 0.097 with responsive units only,
the same as with all units, and 0.013 without them. Size-matched non-responsive sets give 0.243 to
0.281 for Summer; none can be drawn for Camera Cuts, which has 669 non-responsive units."""

R["fig7b-top500-overlap"] = """**Result: partially reproduced.** The five rankings share 97 units in their top 500, against 78 in
the paper (tolerance 70.2 to 85.8) and 1.14 expected by chance (1.12 simulated), 85 times chance.
No unit in a top 500 was tied at zero, so the tie-break does not matter (97 with ties by unit
index). The overlaps for the top 100, 350, 750 and 1000 are 20, 66, 157 and 254, against chance
values of 0.00, 0.19, 8.69 and 36.6 that match the paper's (0, 0, 9, 37). The 97 units come from 26
patients and every region."""

R["blocked"] = """## Blocked claims

fig3c-lstm-decoding, fig3d-temporal-shuffle, fig5-faces-presence and fig7a-500-neurons rest on the
paper's LSTM. Its code is not in the paper's materials, the dataset's GitHub repository or its
Zenodo archive (which hold a two-layer linear baseline), and the Methods say that the number of
linear layers, hidden sizes, batch size, learning rate, weight decay and dropout were chosen for
each label without giving them. These claims are blocked with `methods_underspecified`. Training an
LSTM for 700 epochs on 2286 inputs for each label and fold would also not fit the time limit on a
CPU; this was not tried. For fig5-faces-presence the face labels in the dandiset also lack the
excluded state the Methods describe."""

R["summary"] = """## Summary

A failure to reproduce here may be a failure of this attempt, not of the paper: see the reasoning
and the differences from the paper's method.

| Claim | Outcome |
|---|---|
| dataset-composition | partially reproduced |
| fig2b-phc-camera-cuts | blocked (methods underspecified) |
| tables1-camera-cuts-regions | blocked (methods underspecified) |
| fig2b-phc-scene-cuts | blocked (methods underspecified) |
| tables1-few-semantic-responses | blocked (methods underspecified) |
| tables1-no-indoor-response | blocked (methods underspecified) |
| results-cluster-regions | blocked (methods underspecified) |
| fig3b-single-neuron-threshold | reproduced |
| fig3c-logreg-characters-location | reproduced |
| fig3c-logreg-cuts-lower | reproduced |
| fig3e-temporal-gap | reproduced |
| fig4-patients-below-pooled | reproduced |
| fig4-named-patients | reproduced |
| fig5-region-decoding | partially reproduced |
| fig6-responsive-subsets | blocked (methods underspecified) |
| fig7b-top500-overlap | partially reproduced |
| fig3c-lstm-decoding | blocked (methods underspecified) |
| fig3d-temporal-shuffle | blocked (methods underspecified) |
| fig5-faces-presence | blocked (methods underspecified) |
| fig7a-500-neurons | blocked (methods underspecified) |

How the analysis differs from the paper's:

- The paper's LSTM is not run. Its logistic regression, which the paper reports for the
  patient-wise analysis and Figure 3c, is run as the Methods describe, with class weights in place
  of oversampling and C chosen from four values. It stands in for the LSTM in fig3e, fig5 and fig6.
- The responsive-unit test follows the Methods as written. On this data it is not calibrated
  (68.3% of units responsive at random times at alpha 0.001), so the claims that rest on it are
  blocked. The dataset code's ZETA test is calibrated here and gives 12.63% of PHC units for camera
  cuts at alpha 0.001, against the paper's 51.74%.
- Regions are the dandiset's `brain_region`, grouped as in the dataset's code; their counts differ
  from the paper's.
- Cut labels are extended to 520 ms after the cut for scene cuts too; the Methods state it for
  camera cuts.

What was found about the dandiset:

- It holds the 2286 units of the 29 patients, the movie annotations and the watchlogs needed for
  the analyses, and the logistic regression results of the paper are recovered from it.
- The units' regions give counts that differ from the paper's (PHC 293 against 373, EC 493 against
  440, PIC 68 against 99, 27 units in other regions), with no mapping between the two.
- Spike times are stored in milliseconds; the patient-aligned annotation columns are described as
  seconds but hold milliseconds.
- The face labels lack the excluded state the Methods use.
- The earlier published version 0.260519.1133 holds 28 of the recordings twice.
- The dataset's code identifies responsive units with the ZETA test, not the test of the Methods,
  and its training code selects no hippocampal unit."""
json.dump(R, open("/tmp/claude-1001/scratch/results.json", "w"), indent=1, ensure_ascii=False)
PYEOF
cd /tmp/claude-1001/scratch && . .venv/bin/activate && python results.py && python build_nb.py && grep -c "—" entries/001616-gerken-2025/reproduce_gerken_2025.ipynb; grep -ci "rather" entries/001616-gerken-2025/reproduce_gerken_2025.ipynb
```

```
Exit code 1
wrote 69 cells
0
0
```

**Agent**

Now the entry README and the attempt record.

**Agent calls Write**

```json
{
 "file_path": "entries/001616-gerken-2025/README.md",
 "content": "# Gerken, Darcher et al. (2025) from dandiset 001616\n\nTests the findings of [Gerken, Darcher et al. (2025)](https://doi.org/10.7554/eLife.106758.1), eLife\nreviewed preprint 106758, on [DANDI:001616](https://dandiarchive.org/dandiset/001616/0.260702.0824)\n(SUMMER), which holds 2286 units recorded in the medial temporal lobe of 29 patients while they\nwatched \"500 Days of Summer\", with 53 frame-wise annotations of the film.\n\n| Claim | Outcome |\n|---|---|\n| 2286 units from 29 patients, with the paper's counts per region | Partially reproduced |\n| Units responsive to feature onsets (Figure 2, Table S1; six claims) | Blocked: methods underspecified |\n| Single units thresholded do not decode Summer | Reproduced |\n| Logistic regression decodes characters and location (Summer 0.28, Indoor/Outdoor 0.31) | Reproduced |\n| Logistic regression is weaker for scene and camera cuts | Reproduced |\n| Without temporal gaps decoding is almost perfect | Reproduced |\n| No single patient matches the pooled decoder | Reproduced |\n| The patients the paper names decode above 0.2 | Reproduced |\n| Decoding by region (amygdala for Summer, PHC for Indoor/Outdoor) | Partially reproduced |\n| Responsive units drive decoding of cuts, not of Summer | Blocked: methods underspecified |\n| 78 units shared by the top 500 of five rankings | Partially reproduced |\n| LSTM results (Figures 3c, 3d, 5b, 7a; four claims) | Blocked: methods underspecified |\n\nA failure to reproduce here may be a failure of this attempt, not of the paper: see the reasoning\nand the differences from the paper's method.\n\nThe responsive-unit test of the Methods, as written, counts about 70% of units responsive even at\nrandom event times on this data, so the claims that rest on it could not be judged. The paper's\nLSTM is not published; its logistic regression is run instead where the paper uses it, and as a\nstand-in in three claims. The attempt record, with the reasons and the differences from the paper's\nmethod, is [`attempts/001616-gerken-2025-01.yaml`](../../attempts/001616-gerken-2025-01.yaml).\n\n- `reproduce_gerken_2025.ipynb`: the analysis. It takes about 22 minutes on four cores.\n- `summer.py`: loading the files, the time base through the watchlogs, the responsive-unit and\n  cluster tests, the fold layout of the dataset's code and the logistic regression. Other notebooks\n  on this dandiset can import it.\n"
}
```

```
File created successfully at: entries/001616-gerken-2025/README.md (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
sed -i 's/runtime_minutes: 20/runtime_minutes: 22/' entries/001616-gerken-2025/entry.yaml && cat > /tmp/claude-1001/scratch/attempt.py <<'PYEOF'
import yaml
NB = "reproduce_gerken_2025.ipynb"
RESP_DEV = ("The responsive-unit test follows the Methods as fixed in the claims file (baseline count over "
            "-1000 to 0 ms divided by 10, 19 overlapping 100 ms bins, two-sided Wilcoxon signed-rank, Simes); "
            "the Methods do not say more.")
def o(claim, outcome, notes, deviations=None, measured=None, blocked_by=None, output=True):
    d = {"claim": claim, "outcome": outcome}
    if blocked_by:
        d["blocked_by"] = blocked_by
    if output:
        d["notebook"] = NB
        d["output"] = f"claim:{claim}"
    if measured is not None:
        d["measured"] = measured
    d["notes"] = notes
    if deviations:
        d["deviations"] = deviations
    return d

outcomes = [
 o("dataset-composition", "partially_reproduced",
   "29 patients, 2286 units and 17 female patients, as stated, with 30 to 137 units per patient. With AH, MH "
   "and PH grouped as hippocampus (the dataset's code), the regions hold A 559 (paper 580), H 846 (794), EC 493 "
   "(440), PHC 293 (373) and PIC 68 (99), and 27 units lie in FF, LG and PRC. A and H are within 10%; EC, PHC "
   "and PIC are not. Every unit's region matches that of its electrode.",
   ["Regions are read from the dandiset's `brain_region` and grouped as in the dataset's code; the paper "
    "gives no mapping."],
   measured=[29, 2286, 17, 559, 846, 493, 293, 68], output=False),
 o("fig2b-phc-camera-cuts", "blocked",
   "The Methods' test counts 222 of 293 PHC units (75.77%) responsive at alpha 0.001 and 228 (77.82%) at 0.01 "
   "(paper 193 of 373, 51.74%). The same test counts 72.35% of PHC units and 68.3% of all units responsive at "
   "random event times, and all synthetic Poisson units (2 Hz) with 883 random events, so its false-positive "
   "rate is far from its alpha and the procedure differs from the paper's. The test compares integer counts in "
   "100 ms bins with the baseline mean per 100 ms across hundreds of trials, which a signed-rank test finds "
   "different even without a response. The dataset code's ZETA test (100 resamplings) is calibrated here (0 "
   "and 4 of 293 PHC units at random times at alpha 0.001 and 0.01) and finds 37 (12.63%) and 65 (22.18%), "
   "below the paper's fraction.",
   [RESP_DEV, "The ZETA variant uses 100 resamplings in place of the code's 1000, for time.",
    "The fraction is compared, as the dandiset's PHC holds 293 units against the paper's 373."],
   blocked_by="methods_underspecified"),
 o("tables1-camera-cuts-regions", "blocked",
   "Depends on fig2b-phc-camera-cuts. The miscalibrated test counts A 73.70%, EC 74.04%, H 64.42% and PHC "
   "75.77% at alpha 0.001 (paper 46.90, 45.68, 38.92, 51.74%), and 62 to 73% of each region at random times.",
   [RESP_DEV], blocked_by="methods_underspecified"),
 o("fig2b-phc-scene-cuts", "blocked",
   "The Methods' test counts 139 of 293 PHC units (47.44%) at alpha 0.001 and 179 (61.09%) at 0.01 (paper "
   "6.70%); it is miscalibrated (see fig2b-phc-camera-cuts). With this split the cluster test finds no cluster "
   "with the Methods' z-scoring (p = 1.000); with the code's per-trial z-scoring p = 0.048 at alpha 0.001 and "
   "no cluster at 0.01. The ZETA test finds 8 of 293 (2.73%) at 0.001 and 30 (10.24%) at 0.01, either side of "
   "the tolerance of 4.16 to 9.24%.",
   [RESP_DEV, "Cluster p is the fraction of 1000 label permutations whose largest cluster is at least the "
    "observed largest cluster; the Methods compare each cluster with the permuted histogram."],
   blocked_by="methods_underspecified"),
 o("tables1-few-semantic-responses", "blocked",
   "The test counts 1017 units responsive to Summer and 1168 to Tom at alpha 0.001 (paper 46 and 216), and "
   "9.80 to 51.09% of units for each semantic label, while it counts 68.3% at random times; the counts are "
   "dominated by false positives. The code's onset rule (no minimum duration) changes them little (1030 and "
   "1194).",
   [RESP_DEV, "Onsets for labels with a duration also last at least 1 s (Results); the code does not "
    "require this, shown as a variant."],
   blocked_by="methods_underspecified"),
 o("tables1-no-indoor-response", "blocked",
   "The test counts 279 units responsive to Indoor onsets at alpha 0.001 and 790 at 0.01, and 422 for McKenzie "
   "and 224 for Summer Presence at 0.001, where Table S1 has 0; at random times it counts 68.33% of units. An "
   "absence cannot be judged with this test. The paper's test as written is the one run here; the alpha of "
   "0.001 is that of the Results paragraph making the claim.",
   [RESP_DEV], blocked_by="methods_underspecified"),
 o("results-cluster-regions", "blocked",
   "The responsive and non-responsive split comes from the miscalibrated test. With it, 9 of 32 cells agree "
   "with the paper at alpha 0.001 and 13 at 0.01; camera cuts give no cluster in any region (p = 1.000), and "
   "PHC has 5 significant labels at 0.001 against 7 in H.",
   [RESP_DEV], blocked_by="methods_underspecified"),
 o("fig3b-single-neuron-threshold", "reproduced",
   "Median unit kappa for Summer 0.0077 over 2286 units; 89.8% below 0.05; best unit 0.276 (patient 7, "
   "amygdala); no unit reaches 0.31 or the pooled logistic regression (0.302).",
   ["The threshold and its direction are searched over 50 quantiles of each unit's window counts on the "
    "validation set; the Methods say only that the best threshold was chosen on the validation set."]),
 o("fig3c-logreg-characters-location", "reproduced",
   "Pooled logistic regression, mean over 5 folds: Summer 0.302 (SEM 0.056), Indoor/Outdoor 0.360 (SEM "
   "0.049), both within tolerance of 0.28 and 0.31; Tom 0.217, McKenzie 0.317 and Persons 0.418 reach the LSTM "
   "values less their SEM. Test-label shuffles give p = 0.001 in every fold for Summer, McKenzie, Persons and "
   "Indoor/Outdoor; one Tom fold has kappa 0 (p = 0.52). Over the C grid the test kappa ranges from 0.266 to "
   "0.311 (Summer) and from 0.349 to 0.392 (Indoor/Outdoor). With Summer labels shifted by 300 s the kappa "
   "is 0.016.",
   ["Class weights balanced in place of oversampling the minority class.",
    "C chosen on the validation kappa from 0.001, 0.003, 0.01 and 0.03; the Methods do not give the range.",
    "The fold layout is that of the dataset's code with the 1.6 s window added to the 32 s gap, which gives "
    "the paper's sample counts (30822, 7194, 7194 against 30800, 7200, 7200).",
    "The 0.28 for Summer is the pooled value of Figure 4; the paper does not state the Figure 3c logistic "
    "regression values in numbers."],
   measured=[0.302, 0.36]),
 o("fig3c-logreg-cuts-lower", "reproduced",
   "Scene Cuts 0.0745 (SEM 0.027) and Camera Cuts 0.0967 (SEM 0.020), within tolerance of 0.10 and 0.11 and "
   "below the LSTM's 0.20 and 0.18. Camera Cuts are above chance in every fold (p = 0.001); one Scene Cuts "
   "fold is not (kappa -0.014, p = 1.0).",
   ["Scene cut labels are extended to 520 ms after the cut, as the Methods state for camera cuts.",
    "The expected values are derived from the stated drops (0.1, 0.07) and the LSTM values of Table S2."],
   measured=[0.0745, 0.0967]),
 o("fig3e-temporal-gap", "reproduced",
   "Summer with a random split 0.947 (5 draws, 0.942 to 0.952); with gaps of 4, 8, 16 and 32 s 0.555, 0.524, "
   "0.450 and 0.302. The LSTM values held in the dataset's code are 0.987, 0.584, 0.539, 0.429 and 0.309.",
   ["Logistic regression in place of the LSTM.",
    "Gaps other than 32 s use the dataset's code table of repeated parts per gap."]),
 o("fig4-patients-below-pooled", "reproduced",
   "No patient reaches the pooled kappa: Summer best patient 7 at 0.268 against 0.302 (median 0.060); Scene "
   "Cuts patient 20 at 0.044 against 0.075 (median 0.011); Indoor/Outdoor patient 2 at 0.257 against 0.360 "
   "(median 0.099)."),
 o("fig4-named-patients", "reproduced",
   "7 of 8 named pairs exceed 0.2: Summer patients 7 (0.268), 10 (0.227), 22 (0.241), and 15 at 0.197; "
   "Indoor/Outdoor patients 2 (0.257), 13 (0.209), 20 (0.217), 25 (0.202). For Scene Cuts the paper's "
   "patients 2, 10, 19 and 20 are the four best here (0.027 to 0.044).",
   ["Assumes the dandiset's subject ids are the paper's patient numbers; neither gives a mapping. The "
    "agreement of the named patients supports this."]),
 o("fig5-region-decoding", "partially_reproduced",
   "Summer A 0.291, EC 0.148, PHC 0.097, H 0.066: A highest and H lowest hold. Indoor/Outdoor PHC 0.357, H "
   "0.301, A 0.122, EC 0.117: PHC highest holds; A is not lowest, though A and EC differ by less than their "
   "SEMs (0.041, 0.052). 3 of 4 orderings hold.",
   ["Logistic regression in place of the LSTM.",
    "Regions as stored in the dandiset, which hold different units from the paper's (PHC 293 against 373)."]),
 o("fig6-responsive-subsets", "blocked",
   "Depends on the responsive sets of the miscalibrated test (1017 units for Summer, 1617 for Camera Cuts at "
   "alpha 0.001). With them all four conditions hold: Summer 0.311 without responsive units, 0.245 with them "
   "only, 0.302 complete; Camera Cuts 0.097 with responsive units only, 0.013 without, 0.097 complete. "
   "Size-matched non-responsive sets give 0.243 to 0.281 for Summer; none can be drawn for Camera Cuts (669 "
   "non-responsive units).",
   ["Logistic regression in place of the LSTM, over all regions together."],
   blocked_by="methods_underspecified"),
 o("fig7b-top500-overlap", "partially_reproduced",
   "97 units are common to the top 500 of the five rankings, against 78 (tolerance 70.2 to 85.8) and a chance "
   "level of 1.14 by the paper's formula (1.12 simulated), 85 times chance. No unit in a top 500 was tied at "
   "zero; ties by unit index give the same 97. Chance values for 100, 350, 750 and 1000 (0.00, 0.19, 8.69, "
   "36.6) match the paper's (0, 0, 9, 37), so the chance computation agrees; observed overlaps are 20, 66, "
   "157 and 254.",
   ["The four sub-splits of a test fold take each of the other four folds once as validation; the Methods "
    "say only that they alternate training and validation data.",
    "The Methods average the absolute coefficients 'across the five splits' within a set of four models; the "
    "mean over the four models is used."],
   measured=97),
 o("fig3c-lstm-decoding", "blocked",
   "The LSTM's code is not in the paper's materials, the dataset's GitHub repository (commit 59fc242) or its "
   "Zenodo archive, which hold a two-layer linear baseline; the Methods choose layers, hidden sizes, batch "
   "size, learning rate, weight decay and dropout per label without stating them. Training 700 epochs per "
   "label and fold on a CPU would also exceed the time limit; this was not tried. The logistic regression "
   "results are under fig3c-logreg-characters-location and fig3c-logreg-cuts-lower.",
   blocked_by="methods_underspecified", output=False),
 o("fig3d-temporal-shuffle", "blocked",
   "Needs the trained LSTM; see fig3c-lstm-decoding.", blocked_by="methods_underspecified", output=False),
 o("fig5-faces-presence", "blocked",
   "Needs the LSTM; see fig3c-lstm-decoding. The face labels in the dandiset also hold only 0 and 1, while "
   "the Methods exclude frames where a face is neither shown nor absent; those frames cannot be identified.",
   blocked_by="methods_underspecified", output=False),
 o("fig7a-500-neurons", "blocked",
   "Needs the LSTM; see fig3c-lstm-decoding. The ranking itself is tested under fig7b-top500-overlap.",
   blocked_by="methods_underspecified", output=False),
]
# dataset-composition output tag: data check cells are tagged sanity, not claim; point to sanity
for d in outcomes:
    if d["claim"] == "dataset-composition":
        d["notebook"] = NB
        d["output"] = "sanity"
attempt = {
 "schema_version": 1,
 "id": "001616-gerken-2025-01",
 "dandiset": "001616",
 "dandiset_version": "0.260702.0824",
 "paper": "doi:10.7554/elife.106758.1",
 "date": "2026-10-14",
 "entry": "001616-gerken-2025",
 "provenance": {"kind": "agent", "accountable": {"name": "CatalystNeuro"},
                "agent": {"harness": "Claude Code (GitHub Actions)", "model": "claude-opus-5-5", "protocol": "pilot-6"}},
 "inputs": [{"what": "Method choices read from the dataset's code (the fold layout and table of repeated parts per gap, the "
                     "grouping of hippocampal subregions, the onset rule and the ZETA test for responsive units), and the "
                     "LSTM results per gap and per region its plotting notebooks hold, printed for comparison only.",
             "source": "https://github.com/mormannlab/SUMMER at commit 59fc2424615150481494edf3e31d707729d395ea"}],
 "outcomes": outcomes,
 "findings": [
  {"kind": "other", "statement": "The units' `brain_region` gives A 559, hippocampus 846 (AH 418, MH 16, PH 412), EC 493, "
   "PHC 293 and PIC 68 units, and 27 in FF, LG and PRC, where the paper reports A 580, H 794, EC 440, PHC 373 and PIC 99 "
   "for the same 2286 units. Neither the dandiset nor the paper maps one assignment to the other, so the paper's region "
   "analyses cannot be repeated on the paper's regions."},
  {"kind": "format_error", "statement": "Spike times in the units table are in milliseconds (its description says so), "
   "where NWB requires seconds; the watchlogs' recording times are also in milliseconds."},
  {"kind": "metadata_error", "statement": "The start and stop columns of `annotations_patient_aligned` are described as "
   "seconds but hold milliseconds of the recording clock, as the table's own description says."},
  {"kind": "metadata_insufficient", "statement": "The face labels (summer-faces, tom-faces and others) hold only 0 and 1. "
   "The Methods define face labels with frames excluded when a face is neither shown nor clearly absent; those frames "
   "cannot be identified."},
  {"kind": "other", "statement": "Published version 0.260519.1133 holds 57 files: the 29 of the later version and 28 "
   "older copies (`ses-1_behavior+ecephys`) with the same units and spike times, one per patient except patient 3. "
   "Version 0.260702.0824 holds each recording once."},
  {"kind": "code_mismatch", "statement": "The dataset's code identifies responsive units with the ZETA test (zetapy; "
   "alpha 0.01 in its notebook), where the Methods describe a bin-wise Wilcoxon signed-rank test with Simes correction. "
   "With ZETA, 12.63% of PHC units respond to camera cuts at alpha 0.001 and 22.18% at 0.01, against the paper's "
   "51.74%."},
  {"kind": "methods_unavailable", "statement": "The responsive-unit test as the Methods describe it (spike counts in 19 "
   "bins of 100 ms against the baseline count per 100 ms, signed-rank across pseudo-trials, Simes) counts 68% of units "
   "responsive at random event times on this data and every synthetic Poisson unit with 883 events, so the procedure "
   "behind Figure 2 and Table S1 cannot be recovered from the text. The paper's LSTM code and its per-label "
   "hyperparameters are not published either."},
  {"kind": "paper_inconsistency", "statement": "The threshold for responsive units is alpha 0.01 in the Methods and "
   "0.001 in the Results, the Figure 2 legend and Table S1; the cluster test section splits units at p 0.01."},
  {"kind": "paper_inconsistency", "statement": "The Results give the 29 patients' ages as 22 to 63; the Methods give 19 "
   "to 62 for all 46 patients recorded. The dandiset's 29 patients are 19 to 62."},
  {"kind": "other", "statement": "The dandiset has 958 camera cuts in the 83-minute film, one every 5.25 s; the "
   "supplement says one every 3 s."},
  {"kind": "code_mismatch", "statement": "The training code of the dataset's repository "
   "(ML_framework/nwb_loading/nwb_loading.py, get_unit_ids_for_patient_nwb) compares `brain_region` with the region "
   "group name in place of its subregions; no unit is labelled `H`, so asking for the hippocampus selects no unit."},
  {"kind": "identifier_missing", "statement": "Neither the dandiset nor the paper states that subject ids are the "
   "paper's patient numbers. Taking them as such, the patients the paper names in Figure 4 are among the best here (7 "
   "of 8 above kappa 0.2)."},
 ],
}
class D(yaml.SafeDumper):
    pass
open("attempts/001616-gerken-2025-01.yaml", "w").write(
    yaml.dump(attempt, Dumper=D, sort_keys=False, allow_unicode=True, width=100))
PYEOF
python /tmp/claude-1001/scratch/attempt.py && grep -n "^- claim\|outcome:" attempts/001616-gerken-2025-01.yaml | head -5; grep -c "'" attempts/001616-gerken-2025-01.yaml
```

```
22:- claim: dataset-composition
23:  outcome: partially_reproduced
42:- claim: fig2b-phc-camera-cuts
43:  outcome: blocked
61:- claim: tables1-camera-cuts-regions
52
```

**Agent calls Bash**

```bash
grep -n "'" attempts/001616-gerken-2025-01.yaml | head -30
```

```
3:dandiset: '001616'
6:date: '2026-10-14'
17:- what: Method choices read from the dataset's code (the fold layout and table of repeated parts per gap,
34:    With AH, MH and PH grouped as hippocampus (the dataset's code), the regions hold A 559 (paper 580),
36:    H are within 10%; EC, PHC and PIC are not. Every unit's region matches that of its electrode.
38:  - Regions are read from the dandiset's `brain_region` and grouped as in the dataset's code; the paper
47:  notes: The Methods' test counts 222 of 293 PHC units (75.77%) responsive at alpha 0.001 and 228 (77.82%)
50:    its false-positive rate is far from its alpha and the procedure differs from the paper's. The test
52:    which a signed-rank test finds different even without a response. The dataset code's ZETA test (100
54:    and finds 37 (12.63%) and 65 (22.18%), below the paper's fraction.
59:  - The ZETA variant uses 100 resamplings in place of the code's 1000, for time.
60:  - The fraction is compared, as the dandiset's PHC holds 293 units against the paper's 373.
78:  notes: The Methods' test counts 139 of 293 PHC units (47.44%) at alpha 0.001 and 179 (61.09%) at 0.01
80:    no cluster with the Methods' z-scoring (p = 1.000); with the code's per-trial z-scoring p = 0.048
96:    the counts are dominated by false positives. The code's onset rule (no minimum duration) changes them
111:    68.33% of units. An absence cannot be judged with this test. The paper's test as written is the one
136:  - The threshold and its direction are searched over 50 quantiles of each unit's window counts on the
145:  notes: 'Pooled logistic regression, mean over 5 folds: Summer 0.302 (SEM 0.056), Indoor/Outdoor 0.360
150:    by 300 s the kappa is 0.016.'
154:  - The fold layout is that of the dataset's code with the 1.6 s window added to the 32 s gap, which gives
[... 10 more lines not kept]
```

**Agent calls Bash**

```bash
cd /tmp/claude-1001/scratch && python - <<'EOF'
p='attempt.py'; s=open(p).read()
for a,b in [("mean over 5 folds: Summer","mean over 5 folds, Summer"),("No patient reaches the pooled kappa: Summer","No patient reaches the pooled kappa. Summer"),
            ("7 of 8 named pairs exceed 0.2: Summer","7 of 8 named pairs exceed 0.2; Summer"),("Summer A 0.291, EC 0.148, PHC 0.097, H 0.066: A highest","Summer A 0.291, EC 0.148, PHC 0.097, H 0.066, so A highest"),
            ("H 0.301, A 0.122, EC 0.117: PHC highest","H 0.301, A 0.122, EC 0.117, so PHC highest"),("With them all four conditions hold: Summer","With them all four conditions hold. Summer")]:
    assert a in s or a.replace(' ','\n') in s, a
    s=s.replace(a,b)
open(p,'w').write(s)
EOF
grep -n '"[^"]*: [^"]*"' /tmp/claude-1001/scratch/attempt.py | grep -v '^\s*#' | grep -v '"kind"\|"statement"\|"what"\|"source"\|{"' | head; python /tmp/claude-1001/scratch/attempt.py && grep -n "^\s*[a-z_]*: '" attempts/001616-gerken-2025-01.yaml
```

```
Traceback (most recent call last):
  File "<stdin>", line 5, in <module>
AssertionError: H 0.301, A 0.122, EC 0.117: PHC highest
79:   "Pooled logistic regression, mean over 5 folds: Summer 0.302 (SEM 0.056), Indoor/Outdoor 0.360 (SEM "
105:   "No patient reaches the pooled kappa: Summer best patient 7 at 0.268 against 0.302 (median 0.060); Scene "
109:   "7 of 8 named pairs exceed 0.2: Summer patients 7 (0.268), 10 (0.227), 22 (0.241), and 15 at 0.197; "
115:   "Summer A 0.291, EC 0.148, PHC 0.097, H 0.066: A highest and H lowest hold. Indoor/Outdoor PHC 0.357, H "
116:   "0.301, A 0.122, EC 0.117: PHC highest holds; A is not lowest, though A and EC differ by less than their "
122:   "alpha 0.001). With them all four conditions hold: Summer 0.311 without responsive units, 0.245 with them "
163: "id": "001616-gerken-2025-01",
164: "dandiset": "001616",
165: "dandiset_version": "0.260702.0824",
166: "paper": "doi:10.7554/elife.106758.1",
3:dandiset: '001616'
6:date: '2026-10-14'
145:  notes: 'Pooled logistic regression, mean over 5 folds: Summer 0.302 (SEM 0.056), Indoor/Outdoor 0.360
185:  notes: 'No patient reaches the pooled kappa: Summer best patient 7 at 0.268 against 0.302 (median 0.060);
192:  notes: '7 of 8 named pairs exceed 0.2: Summer patients 7 (0.268), 10 (0.227), 22 (0.241), and 15 at
202:  notes: 'Summer A 0.291, EC 0.148, PHC 0.097, H 0.066: A highest and H lowest hold. Indoor/Outdoor PHC
213:  notes: 'Depends on the responsive sets of the miscalibrated test (1017 units for Summer, 1617 for Camera
[... 2 more lines not kept]
```

**Agent calls Bash**

```bash
cd /tmp/claude-1001/scratch && python - <<'EOF'
p='attempt.py'; s=open(p).read()
for a,b in [("mean over 5 folds: Summer","mean over 5 folds, Summer"),("pooled kappa: Summer","pooled kappa. Summer"),
            ("exceed 0.2: Summer","exceed 0.2; Summer"),("H 0.066: A highest","H 0.066, so A highest"),
            ("EC 0.117: PHC highest","EC 0.117, so PHC highest"),("conditions hold: Summer","conditions hold. Summer"),
            ("holds 57 files: the 29","holds 57 files, the 29")]:
    assert a in s, a
    s=s.replace(a,b)
open(p,'w').write(s)
EOF
python /tmp/claude-1001/scratch/attempt.py && grep -n "^\s*[a-z_-]*: '\|^\s*- '" attempts/001616-gerken-2025-01.yaml
```

```
Exit code 2
grep: attempts/001616-gerken-2025-01.yaml: No such file or directory
```

**Agent calls Bash**

```bash
grep -n "^\s*[a-z_-]*: '\|^\s*- '" attempts/001616-gerken-2025-01.yaml
```

```
3:dandiset: '001616'
6:date: '2026-10-14'
```

**Agent**

Attempt record written. Final check and clean run (~22 minutes).

**Agent calls Bash**

```bash
time python tools/entry.py all entries/001616-gerken-2025 2>&1 | tail -5
```

```
Installed kernelspec registry-001616-gerken-2025 in executed/001616-gerken-2025/.venv/share/jupyter/kernels/registry-001616-gerken-2025
0 error(s)
pass  reproduce_gerken_2025.ipynb  (1332 s)

real	22m19.858s
user	63m43.716s
sys	3m9.694s
```

**Agent calls Bash**

```bash
python - <<'EOF' > /tmp/claude-1001/scratch/out2.txt
import json
nb=json.load(open('executed/001616-gerken-2025/reproduce_gerken_2025.ipynb'))
for i,c in enumerate(nb['cells']):
    if c['cell_type']!='code': continue
    print(f'----- tags={c["metadata"].get("tags")}')
    for o in c.get('outputs',[]):
        if o['output_type']=='stream': print(''.join(o['text']))
        elif o['output_type']=='error': print('ERROR', o['ename'], o['evalue'])
EOF
sed 's/^----- \[[0-9]*\] /----- /' /tmp/claude-1001/scratch/out1.txt > /tmp/claude-1001/scratch/out1n.txt; diff <(grep -v " in [0-9]* s\|total run time\|loaded 29" /tmp/claude-1001/scratch/out1n.txt) <(grep -v " in [0-9]* s\|total run time\|loaded 29" /tmp/claude-1001/scratch/out2.txt) | head -40; grep "total run" /tmp/claude-1001/scratch/out2.txt
```

```
488c488
< Summer, labels shifted by 300 s: kappa 0.016 (folds [0.009, 0.044, -0.11, 0.058, 0.081]); true labels 0.302; 30 s
---
> Summer, labels shifted by 300 s: kappa 0.016 (folds [0.009, 0.044, -0.11, 0.058, 0.081]); true labels 0.302; 32 s
total run time 22.0 min
```

**Agent**

Both runs give identical numbers. Running the handover step.

**Agent calls Bash**

```bash
python tools/entry.py handover entries/001616-gerken-2025 && ls executed/001616-gerken-2025/handover/ && python -c "
import json;nb=json.load(open('executed/001616-gerken-2025/handover/reproduce_gerken_2025.ipynb'))
print(sum(1 for c in nb['cells'] if c['cell_type']=='markdown' and ''.join(c['source']).lstrip().startswith('**Result')), [''.join(c['source'])[:30] for c in nb['cells'][-3:]])"; git status --short; ls paper
```

```
wrote executed/001616-gerken-2025/handover
10.7554-elife.106758.1.yaml
reproduce_gerken_2025.ipynb
summer.py
0 ['## fig7b-top500-overlap\n\n> Acr', 'rng_rank = np.random.default_r', '## Blocked claims\n\nfig3c-lstm-']
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
?? attempts/001616-gerken-2025-01.yaml
?? claims/001616/
?? entries/001616-gerken-2025/
?? scripts
epp_106758v1.json
[... 5 more lines not kept]
```

**Agent calls Bash**

```bash
ls -la --time-style=full-iso .bash_profile .bashrc .gitconfig .mcp.json .profile .ripgreprc .zprofile .zshrc scripts .idea .vscode 2>&1 | head -20; cat .gitignore 2>/dev/null | head
```

```
crw-rw-rw- 1 nobody nogroup 1, 3 2026-10-14 20:16:15.489234983 +0000 .bash_profile
crw-rw-rw- 1 nobody nogroup 1, 3 2026-10-14 20:16:15.489234983 +0000 .bashrc
crw-rw-rw- 1 nobody nogroup 1, 3 2026-10-14 20:16:15.489234983 +0000 .gitconfig
crw-rw-rw- 1 nobody nogroup 1, 3 2026-10-14 20:16:15.489234983 +0000 .idea
crw-rw-rw- 1 nobody nogroup 1, 3 2026-10-14 20:16:15.489234983 +0000 .mcp.json
crw-rw-rw- 1 nobody nogroup 1, 3 2026-10-14 20:16:15.489234983 +0000 .profile
crw-rw-rw- 1 nobody nogroup 1, 3 2026-10-14 20:16:15.489234983 +0000 .ripgreprc
crw-rw-rw- 1 nobody nogroup 1, 3 2026-10-14 20:16:15.489234983 +0000 .vscode
crw-rw-rw- 1 nobody nogroup 1, 3 2026-10-14 20:16:15.489234983 +0000 .zprofile
crw-rw-rw- 1 nobody nogroup 1, 3 2026-10-14 20:16:15.489234983 +0000 .zshrc
crw-rw-rw- 1 nobody nogroup 1, 3 2026-10-14 20:16:15.489234983 +0000 scripts
__pycache__/
*.pyc
.ipynb_checkpoints/
.venv/
.DS_Store
executed/
site/
paper/
```

**Agent calls Bash**

```bash
grep -n "—\|rather" claims/001616/*.yaml attempts/001616-gerken-2025-01.yaml entries/001616-gerken-2025/README.md entries/001616-gerken-2025/summer.py entries/001616-gerken-2025/entry.yaml; grep -c "\*\*" entries/001616-gerken-2025/README.md; python tools/entry.py check entries/001616-gerken-2025 | tail -1
```

```
0
0 error(s)
```

**Agent**

I've finished steps 1 to 5 and run the handover (step 6). The entry is `entries/001616-gerken-2025/`, with `claims/001616/10.7554-elife.106758.1.yaml` and `attempts/001616-gerken-2025-01.yaml`. It is locked, `check` reports 0 errors, and two clean runs gave identical numbers. I used the full text of the eLife reviewed preprint v1, which is open access, plus its supplement. The pinned version is 0.260702.0824: the paper cites no DANDI version, this is the newest published one, and it holds each recording once.

## 1. Outcomes

| Claim | Outcome |
|---|---|
| dataset-composition | partially reproduced (totals match; EC, PHC and PIC unit counts differ) |
| fig2b-phc-camera-cuts | blocked: methods_underspecified |
| tables1-camera-cuts-regions | blocked: methods_underspecified |
| fig2b-phc-scene-cuts | blocked: methods_underspecified |
| tables1-few-semantic-responses | blocked: methods_underspecified |
| tables1-no-indoor-response | blocked: methods_underspecified |
| results-cluster-regions | blocked: methods_underspecified |
| fig3b-single-neuron-threshold | reproduced |
| fig3c-logreg-characters-location | reproduced (Summer 0.302, Indoor/Outdoor 0.360) |
| fig3c-logreg-cuts-lower | reproduced (scene cuts 0.0745, camera cuts 0.0967) |
| fig3e-temporal-gap | reproduced (logistic regression in place of the LSTM; random split 0.947) |
| fig4-patients-below-pooled | reproduced |
| fig4-named-patients | reproduced (7 of 8 named patients above 0.2) |
| fig5-region-decoding | partially reproduced (3 of 4 orderings hold) |
| fig6-responsive-subsets | blocked: methods_underspecified (all 4 conditions hold, but it depends on the responsive test) |
| fig7b-top500-overlap | partially reproduced (97 shared units against the paper's 78; chance is 1.14) |
| fig3c-lstm-decoding, fig3d-temporal-shuffle, fig5-faces-presence, fig7a-500-neurons | blocked: methods_underspecified (the LSTM is not published) |

The six responsive-unit claims are blocked because the Methods' test, as written, is badly miscalibrated here. It flags 68% of units as responsive at random event times, and 100% of synthetic Poisson units when there are 883 events.

## 2. What was found about the dandiset

- **Totals match:** 29 patients, 17 female, 2286 units, 30 to 137 per patient.
- **Region counts differ from the paper**, and there is no mapping between them:

  | Region | Dandiset | Paper |
  |---|---|---|
  | A | 559 | 580 |
  | H | 846 | 794 |
  | EC | 493 | 440 |
  | PHC | 293 | 373 |
  | PIC | 68 | 99 |
  | Other (FF, LG, PRC) | 27 | not named |

- **Units:** spike times are stored in milliseconds, not the seconds NWB requires. The patient-aligned annotation columns say seconds but hold milliseconds.
- **Labels:**
  - The face labels lack the "excluded" state the Methods use.
  - There are 958 camera cuts (one every 5.25 s); the supplement says one every 3 s.
- **Versions:** the earlier version 0.260519.1133 holds 28 recordings twice, as older copies with identical spike times.
- **Dataset code (GitHub mormannlab/SUMMER @59fc242):**
  - It selects responsive units with the ZETA test, not the Methods' test. ZETA is calibrated here and gives 12.6% of PHC units responsive to camera cuts, against the paper's 51.7%.
  - Its training loader selects no hippocampal units, because no unit is labelled `H`.
- **Paper inconsistencies:** the responsive threshold is alpha 0.01 in the Methods and 0.001 in the Results. The patients' ages are 22–63 in the Results; the files have 19–62.
- **Clock check:** spikes and annotations look aligned. PHC firing rises 200–300 ms after cuts, and decoding with labels shifted by 300 s falls to kappa 0.016. Per patient, the alignment is shown for 12 of 29.

## 3. Points where the protocol was unclear or did not fit

1. **Chance-level rule.** It covers "a chance level or false-positive rate the paper states". The paper gives only the alpha, and I treated that as the stated false-positive rate. The responsive claims ran but are blocked. This includes an absence claim, which the protocol otherwise says to judge on the paper's test as written.
2. **Blocked claims that depend on blocked claims.** The rule blocks fig6 and the cluster claim even though their analyses ran. I blocked them and kept the numbers in the notes.
3. **Several readings vs one main choice.** The paper gives two alphas. I treated both as readings, and used 0.001 alone for the absence claim, since it is the threshold in the same Results paragraph.
4. **Data check vs claim analyses.** I saw one fold's Summer kappa while timing the model, before writing the criteria. I disclosed it in the claims file's opening comment.
5. **Reference values from code.** The protocol has no slot for these. The code's printed LSTM values per gap and region are listed under `inputs` and used only for comparison; all claims are `data: dandiset`.
6. **Tolerances.** For small proportions I used the 95% binomial interval instead of 10%. For the logistic regression I used the paper's LSTM SEM, since none is given for the regression. Both are stated in the claims file.
7. **Substitute model.** For claims stated about the LSTM, the protocol does not say whether a substitute counts as tested. I tested three with the paper's own logistic regression and recorded it as a deviation.
8. **Region claim (fig5).** The regions themselves differ from the paper's. I judged on the dandiset's regions and recorded it as a deviation.
9. **Data-check claim tag.** The protocol gives no claim tag for a data-check claim, so I pointed dataset-composition's `output` at the `sanity` cells.

## 4. Runtime and failures

- The notebook takes 22 minutes on 4 cores, over the 10-minute aim but under the 30-minute CI limit. Most of the time is about 285 logistic-regression fits and the ZETA variant.
- The ZETA variant uses 100 resamplings instead of the code's 1000, for time, and covers PHC units only.
- During development, an off-by-one in the bin labels and an impossible size-matched draw broke the run; both are fixed. A first version of the per-patient clock check cancelled out across regions and was replaced.
- `git status` shows dotfile names (`.bashrc`, `scripts`, and others) at the repo root. They are sandbox device mounts, not files I created.

Nothing was committed or pushed.

## End of run

82 turns, 107 minutes, result: success.
