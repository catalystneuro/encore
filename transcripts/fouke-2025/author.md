# 001453 · author · run 38574152687

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cat docs/protocol.md; ls; ls entries claims attempts tools
```

```
# Protocol for an attempt

Version: `pilot-5`. Record this version in the attempt's provenance.

This is what an agent, or a person, does to attempt a target and deposit the
result. It is written from the first five pilot attempts
([pilot notes](pilot-notes.md)); the reasons for the rules are there.

There are two roles. The **author** makes the attempt. The **verifier** checks
it and must not be the author: for agents, a separate run with a separate
context that has not seen the author's reasoning.

Agent runs are made with the [Agent run](../.github/workflows/attempt.yml)
workflow, one role at a time: `author`, `verifier-1`, `author-revise-1`,
`verifier-2`, `author-revise-2`. Each run's transcript and final report are
kept in [`transcripts/<dandiset>/`](../transcripts).

## Author

### 1. Establish what can be tested
[... 331 more lines not kept]
```

**Agent calls Bash**

```bash
cat README.md docs/design.md; ls entries/000127-chowdhury-2020 claims/000127; cat entries/000127-chowdhury-2020/entry.yaml entries/000127-chowdhury-2020/requirements.in claims/000127/*.yaml attempts/000127-chowdhury-2020-01.yaml
```

```
# Reproduction registry (working name)

Agents, and people, try to reproduce the key findings of papers from the open
data on the [DANDI Archive](https://dandiarchive.org), and register the result
here: the notebooks when it works, and the reason when it does not.

- **For the archive:** evidence of whether each dandiset is complete and
  accurate enough to support the findings of its paper.
- **For analysts:** working notebooks to build new analyses on.

Status: pilot. Seven of the eight pilot targets have been attempted and checked by an
independent agent.

**Dashboard:** <https://catalystneuro.github.io/reproduction-registry/>

## Reading the outcomes

An outcome says what one attempt could recover from the data in a dandiset,
with the methods available to it. **A "not reproduced" or "partially
reproduced" outcome is not a finding that the paper is wrong.** It can come
[... 609 more lines not kept]
```

**Agent calls Bash**

```bash
ls schemas; cat schemas/*.json | head -400; cat entries/000127-chowdhury-2020/README.md
```

```
attempt.schema.json
claims.schema.json
entry.schema.json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "One attempt at reproducing the claims of a target",
  "description": "Draft. To be revised after the pilot. An attempt is recorded whether or not it produced a working notebook.",
  "type": "object",
  "additionalProperties": false,
  "required": [
    "schema_version",
    "id",
    "dandiset",
    "paper",
    "date",
    "provenance",
    "outcomes"
  ],
  "properties": {
    "schema_version": {
[... 409 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 400,600p schemas/claims.schema.json; cat schemas/entry.schema.json | head -50; wc -l tools/entry.py
```

```
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "An entry: a directory of notebooks with its metadata (entry.yaml)",
  "description": "Draft. To be revised after the pilot.",
  "type": "object",
  "additionalProperties": false,
  "required": ["schema_version", "name", "type", "title", "description", "license", "notebooks", "related"],
  "properties": {
    "schema_version": {"const": 1},
    "name": {
      "description": "Unique across the registry, and the name of the entry's directory.",
      "type": "string",
      "pattern": "^[a-z0-9]+(-[a-z0-9]+)*$",
      "maxLength": 100
    },
    "type": {"enum": ["orientation", "reproduction", "analysis"]},
    "title": {"type": "string", "minLength": 1, "maxLength": 300},
    "description": {"type": "string", "minLength": 1},
    "license": {"description": "SPDX identifier.", "type": "string"},
    "notebooks": {
[... 31 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 60,400p schemas/claims.schema.json; cat tools/entry.py
```

```
"items": {
                  "$ref": "#/$defs/expected"
                }
              }
            ]
          },
          "criterion": {
            "description": "For a claim without a number, how it will be judged. Written before the analysis is run.",
            "type": "string"
          },
          "depends_on": {
            "description": "Ids of claims in this file whose result this one uses.",
            "type": "array",
            "items": {
              "type": "string",
              "pattern": "^[a-z0-9]+(-[a-z0-9]+)*$"
            }
          },
          "data": {
            "description": "What the claim's test uses: the dandiset alone (the default), or the dandiset with data from elsewhere, listed under `inputs` in the attempt. The two are counted apart.",
[... 403 more lines not kept]
```

**Agent**

Now the dandiset metadata.

**Agent calls Bash**

```bash
cd $TMPDIR; curl -s https://api.dandiarchive.org/api/dandisets/001453/ | python -m json.tool; curl -s "https://api.dandiarchive.org/api/dandisets/001453/versions/" | python -m json.tool
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
curl -s https://api.dandiarchive.org/api/dandisets/001453/versions/0.250518.1950/ | python -m json.tool; curl -s "https://api.dandiarchive.org/api/dandisets/001453/versions/0.250518.1950/assets/?page_size=100" | python -c "
import json,sys; d=json.load(sys.stdin)
for a in d['results']: print(a['asset_id'], a['size'], a['path'])"
```

Result: the fetched text is not kept.

**Agent**

Only behavior NWB files (37, 3.8 GB). Now the paper.

**Agent calls Bash**

```bash
mkdir -p paper; curl -s "https://api.crossref.org/works/10.1016/j.cub.2025.04.027" | python -c "
import json,sys; d=json.load(sys.stdin)['message']; print(d.get('title'), d.get('license'), [l.get('URL') for l in d.get('link',[])]); print([a.get('family') for a in d['author']])"; curl -s "https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.1016/j.cub.2025.04.027&format=json&resultType=core" | python -c "
import json,sys; d=json.load(sys.stdin); r=d['resultList']['result']; [print(x.get('pmid'),x.get('pmcid'),x.get('isOpenAccess'),x.get('inEPMC')) for x in r]"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
curl -s "https://www.ebi.ac.uk/europepmc/webservices/rest/PMC12218792/fullTextXML" -o paper/fulltext.xml; ls -la paper; head -c 1500 paper/fulltext.xml
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
curl -sL "https://www.ncbi.nlm.nih.gov/research/bionlp/RESTful/pmcoa.cgi/BioC_xml/PMC12218792/unicode" -o paper/bioc.xml; ls -la paper; head -c 600 paper/bioc.xml; echo; curl -sL -A "Mozilla/5.0" "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pmc&id=12218792&rettype=xml" -o paper/pmc.xml; ls -la paper; head -c 800 paper/pmc.xml
```

Result: the fetched text is not kept.

**Agent**

Got the PMC author manuscript (NIH public access). Converting to text.

**Agent calls Bash**

```bash
rm paper/bioc.xml paper/fulltext.xml; python - <<'EOF'
import re
x=open('paper/pmc.xml').read()
x=re.sub(r'<title>',r'\n\n## ',x); x=re.sub(r'</title>',r'\n',x)
x=re.sub(r'<p>|<p [^>]*>',r'\n',x)
x=re.sub(r'<caption>',r'\n[CAPTION] ',x)
t=re.sub(r'<[^>]+>','',x)
import html; t=html.unescape(t)
open('paper/fulltext.txt','w').write(t)
print(len(t))
EOF
grep -n "restricted\|license\|manuscript" paper/pmc.xml | head -5
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/fulltext.txt"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
wc -c paper/fulltext.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/fulltext.txt",
 "offset": 266
}
```

Result: not kept, because it reads the paper's text.

**Agent**

Full text is the PMC author manuscript. Now set up an exploration environment and check the linked code.

**Agent calls Bash**

```bash
cd $TMPDIR && uv venv -q --python 3.13 explore && uv pip install -q --python explore/bin/python pynwb remfile h5py dandi numpy pandas scipy matplotlib statsmodels 2>&1 | tail -3; echo done; curl -sI https://gitlab.oit.duke.edu/ean26/danionella_omr_neuralcircuits2025 | head -5; curl -s https://api.github.com/users/naumannlab/repos | python -c "import json,sys; [print(r['name'], r['pushed_at']) for r in json.load(sys.stdin)]"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
curl -s "https://gitlab.oit.duke.edu/api/v4/projects/ean26%2Fdanionella_omr_neuralcircuits2025" | head -c 1500; echo; curl -s "https://gitlab.oit.duke.edu/api/v4/projects/ean26%2Fdanionella_omr_neuralcircuits2025/repository/tree?per_page=100&recursive=true" | head -c 3000; echo; curl -s -o /dev/null -w "%{http_code}\n" https://api.github.com/users/naumannlab/repos; curl -s https://api.github.com/orgs/naumannlab/repos | head -c 500
```

Result: the fetched text is not kept.

**Agent**

The code repository is public. Cloning it (outside the repo) and opening one NWB file in parallel.

**Agent calls Bash**

```bash
cd $TMPDIR && git clone -q https://gitlab.oit.duke.edu/ean26/danionella_omr_neuralcircuits2025.git code && cd code && git log --format="%H %ad %s" | head; cat README.md; ls -la
```

**Agent calls Bash**

```bash
cd $TMPDIR && cat > inspect1.py <<'EOF'
import sys, h5py, remfile
from dandi.dandiapi import DandiAPIClient
path = sys.argv[1]
with DandiAPIClient() as c:
    a = c.get_dandiset("001453","0.250518.1950").get_asset_by_path(path)
    url = a.get_content_url(follow_redirects=1, strip_query=True)
f = h5py.File(remfile.File(url),'r')
def show(name, obj):
    if isinstance(obj, h5py.Dataset):
        print(name, obj.shape, obj.dtype, dict((k, (v if not hasattr(v,'shape') or v.size<5 else '...')) for k,v in obj.attrs.items() if k not in ('object_id','namespace')))
    else:
        print(name+'/', {k:v for k,v in obj.attrs.items() if k not in ('object_id','namespace')})
f.visititems(show)
EOF
explore/bin/python inspect1.py sub-0/sub-0_ses-20231031T135510_behavior.nwb 2>&1 | head -150
```

```
33a5c297ff4ab6ff49f6bdd96139e9fdd867025c Thu Apr 10 09:14:08 2025 -0400 Merge branch 'main' into 'main'
375a46e01117a4fadbe9092bbe82aede63ee65ac Mon Apr 7 14:54:48 2025 -0400 Upload New File
cd51e4cd9e6b31a3e9e398a4cdde42720c545130 Mon Apr 7 14:54:40 2025 -0400 Upload New File
6ce158d5590354762ee9b74ebefd86bb5488289e Mon Apr 7 14:54:30 2025 -0400 Upload New File
bc6deaf1b0b759004f0d980318ff139f168367ed Mon Apr 7 14:54:21 2025 -0400 Upload New File
770c075455d696a232397f3eec7b9841b44cd380 Mon Apr 7 14:54:06 2025 -0400 Upload New File
72d853b6ab810434061abb467f815c8de34687f1 Mon Apr 7 14:53:51 2025 -0400 Upload New File
c66881a77f41bbee178e700dbec784e4d994256a Mon Apr 7 14:53:36 2025 -0400 Upload New File
308bcaed591f0c36434a48ff97397f4cb533d254 Mon Apr 7 14:53:25 2025 -0400 Upload New File
824367ebd394fa3a6d16112d591810a03d8fdd2b Mon Apr 7 14:52:56 2025 -0400 Upload New File
# Danionella_OMR_NeuralCircuits2025



#Gitlab repository for Fouke et al., Current Biology, 2025

This repository contains data and code associated with: " Neural Circuits Underlying Divergent Visuomotor Strategies of Zebrafish and Danionella cerebrum." 
Kaitlyn E. Fouke1, Zichen He1, 2, Matthew D. Loring1, Eva A. Naumann1, 2 ,3

Affiliations :
[... 39 more lines not kept]
```

```
acquisition/ {}
analysis/ {}
file_create_date (1,) object {}
general/ {}
general/experiment_description () object {}
general/experimenter (1,) object {}
general/institution () object {}
general/keywords (4,) object {}
general/lab () object {}
general/related_publications (1,) object {}
general/subject/ {'neurodata_type': 'Subject'}
general/subject/age () object {'reference': 'birth'}
general/subject/sex () object {}
general/subject/species () object {}
general/subject/subject_id () object {}
identifier () object {}
processing/ {}
processing/behavior/ {'description': 'freely swimming tracking data', 'neurodata_type': 'ProcessingModule'}
processing/behavior/BehavioralTimeSeries/ {'neurodata_type': 'BehavioralTimeSeries'}
processing/behavior/BehavioralTimeSeries/dist/ {'comments': 'no comments', 'description': 'distance since last frame', 'neurodata_type': 'TimeSeries'}
[... 60 more lines not kept]
```

**Agent**

Freely swimming tracking only, no imaging or tail data. Surveying metadata of all 37 files.

**Agent calls Bash**

```bash
cd $TMPDIR && cat > survey.py <<'EOF'
import h5py, remfile, json
from dandi.dandiapi import DandiAPIClient
from concurrent.futures import ThreadPoolExecutor
with DandiAPIClient() as c:
    ds = c.get_dandiset("001453","0.250518.1950")
    assets = [(a.path, a.get_content_url(follow_redirects=1, strip_query=True)) for a in ds.get_assets()]
def s(x):
    x = x[()]
    if hasattr(x,'decode'): return x.decode()
    if hasattr(x,'tolist'): x = x.tolist()
    return [v.decode() if hasattr(v,'decode') else v for v in x] if isinstance(x,list) else x
def one(pa):
    p,u = pa
    f = h5py.File(remfile.File(u),'r')
    g = f['general']; sub = g['subject']
    bts = f['processing/behavior/BehavioralTimeSeries']
    ts = bts['f0_x/timestamps']
    n = ts.shape[0]
    out = dict(path=p, species=s(sub['species']), age=s(sub['age']), sex=s(sub['sex']), sid=s(sub['subject_id']),
      desc=s(f['session_description']), start=s(f['session_start_time']), ident=s(f['identifier']),
      exp=s(g['experiment_description']) if 'experiment_description' in g else None,
      n=n, t0=float(ts[0]), t1=float(ts[-1]), series=sorted(bts.keys()),
      other=[k for k in g.keys()], acq=list(f['acquisition'].keys()), stim=list(f['stimulus/presentation'].keys()),
      intervals=list(f['intervals'].keys()) if 'intervals' in f else None,
      sub_keys=list(sub.keys()))
    return out
with ThreadPoolExecutor(8) as ex:
    res = list(ex.map(one, assets))
json.dump(res, open('survey.json','w'), indent=1, default=str)
for r in sorted(res, key=lambda r: r['path']):
    print(r['path'], r['species'], r['age'], r['sex'], r['n'], round(r['t0'],2), round(r['t1'],1), r['ident'])
print(res[0])
EOF
explore/bin/python survey.py 2>&1 | tail -45
```

```
sub-0/sub-0_ses-20230620T110854_behavior.nwb Danio rerio P5D/P9D U 9842588 13.92 60481.6 1b6813d0-d0a1-415d-8a0b-e3caddde9d52
sub-0/sub-0_ses-20231031T135510_behavior.nwb Danionella cerebrum P5D/P9D U 85373 155.27 8083.6 e960b7d5-c2be-485a-bf7a-cad56686f8fd
sub-1/sub-1_ses-20230614T163157_behavior.nwb Danio rerio P5D/P9D U 642085 -0.02 3944.6 72e62945-c442-472c-991d-b1eb3c138b12
sub-1/sub-1_ses-20231031T135558_behavior.nwb Danionella cerebrum P5D/P9D U 254638 415.18 19412.9 9af04c95-23ea-42c4-a7b8-1313f1ed5a18
sub-10/sub-10_ses-20230620T111637_behavior.nwb Danio rerio P5D/P9D U 219788 5.75 6358.0 45bb6cce-e406-459c-9c7a-8e9818929542
sub-10/sub-10_ses-20240503T190631_behavior.nwb Danionella cerebrum P5D/P9D U 532103 45.69 23783.5 6db0751b-b8aa-4714-8f99-0e636b1c9f16
sub-11/sub-11_ses-20230620T111855_behavior.nwb Danio rerio P5D/P9D U 2106421 -0.01 60917.2 6793c73f-81c0-4e4e-94ad-cb6dc9c7a73e
sub-11/sub-11_ses-20240522T002407_behavior.nwb Danionella cerebrum P5D/P9D U 633139 363.5 67717.0 e4de6ee2-5996-48b0-a54f-52ce486d25ee
sub-12/sub-12_ses-20230614T171042_behavior.nwb Danio rerio P5D/P9D U 261221 0.01 8023.8 96b50ae7-b7b0-4f7e-a23d-72670cc85444
sub-13/sub-13_ses-20230615T105805_behavior.nwb Danio rerio P5D/P9D U 336304 0.0 10330.2 e146c70b-c6e5-466c-826c-b9152720a576
sub-14/sub-14_ses-20230614T161558_behavior.nwb Danio rerio P5D/P9D U 377090 0.01 11583.0 e97658e2-bab2-42d8-b08e-f5382e7d2706
sub-15/sub-15_ses-20230620T111927_behavior.nwb Danio rerio P5D/P9D U 499605 0.0 14487.1 39b981d5-6b61-4315-b33b-74232e3ae524
sub-16/sub-16_ses-20230725T175146_behavior.nwb Danio rerio P5D/P9D U 335384 0.0 10306.0 29e6c415-6373-48be-8e05-2ea418c016bd
sub-17/sub-17_ses-20230725T175210_behavior.nwb Danio rerio P5D/P9D U 257365 0.0 7905.4 4a9987e0-f82d-4a93-83d7-3232f4b53bf5
sub-18/sub-18_ses-20230725T175221_behavior.nwb Danio rerio P5D/P9D U 336498 -0.01 10340.1 49d19fd2-b04d-4aa9-b7ec-810a56855674
sub-19/sub-19_ses-20230725T175242_behavior.nwb Danio rerio P5D/P9D U 257126 -0.02 79
[... 23 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/code && python3 - <<'EOF'
import json
for fn in ['Fig1-S1.ipynb']:
    nb=json.load(open(fn))
    print('=====',fn, len(nb['cells']))
    for i,c in enumerate(nb['cells']):
        src=''.join(c['source'])
        if c['cell_type']=='code':
            print(f'--- [{i}] code'); print(src)
            for o in c.get('outputs',[]):
                if o.get('output_type')=='stream': print('>>', ''.join(o['text'])[:800])
                elif 'data' in o and 'text/plain' in o['data']: print('>>', ''.join(o['data']['text/plain'])[:500])
        else:
            print(f'--- [{i}] md'); print(src)
EOF
```

```
<persisted-output>
Output too large (127.5KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/b42a26e6-9b50-422d-b272-9770a97e7467/tool-results/bf37t13ju.txt

Preview (first 2KB):
===== Fig1-S1.ipynb 113
--- [0] md
# FIGURE 1 & S1 ZF VS DC FREELY SWIMMING BEHAVIOR
--- [1] md
# load imports
--- [2] code
import pandas as pd
import numpy as np
import os
from os import path 
from pathlib import Path

from matplotlib import pyplot as plt
import scipy
from math import radians, degrees
from matplotlib.lines import Line2D
[... 58 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/b42a26e6-9b50-422d-b272-9770a97e7467/tool-results/bf37t13ju.txt"
}
```

```
1	===== Fig1-S1.ipynb 113
2	--- [0] md
3	# FIGURE 1 & S1 ZF VS DC FREELY SWIMMING BEHAVIOR
4	--- [1] md
5	# load imports
6	--- [2] code
7	import pandas as pd
8	import numpy as np
9	import os
10	from os import path 
11	from pathlib import Path
12	
13	from matplotlib import pyplot as plt
14	import scipy
15	from math import radians, degrees
16	from matplotlib.lines import Line2D
17	import matplotlib.patches as mpatches
18	
19	from ipywidgets import interact
20	
[... 1004 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/code && grep -n "stimToNum\|'forward'\|monocular\|kruskal\|anova\|ols(\|f_oneway\|tukey" -i ../../bf37t13ju.txt 2>/dev/null | head; F=/home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/b42a26e6-9b50-422d-b272-9770a97e7467/tool-results/bf37t13ju.txt; grep -n "^--- \[\|ols(\|anova_lm\|kruskal\|pairwise_tukey\|>> " $F | sed -n 1,400p | awk -F: '$1>1024' | head -150
```

```
1034:>> <Figure size 1000x1000 with 9 Axes>
1035:--- [42] md
1037:--- [43] code
1040:--- [44] code
1117:>> <Figure size 600x600 with 2 Axes>
1118:>> <Figure size 600x600 with 2 Axes>
1119:>> <Figure size 600x600 with 2 Axes>
1120:>> <Figure size 600x600 with 2 Axes>
1121:>> <Figure size 600x600 with 2 Axes>
1122:>> <Figure size 600x600 with 2 Axes>
1123:>> <Figure size 600x600 with 2 Axes>
1124:>> <Figure size 600x600 with 2 Axes>
1125:>> <Figure size 600x600 with 2 Axes>
1126:>> <Figure size 600x600 with 2 Axes>
1127:>> <Figure size 600x600 with 2 Axes>
1128:>> <Figure size 600x600 with 2 Axes>
1129:>> <Figure size 600x600 with 2 Axes>
1130:>> <Figure size 600x600 with 2 Axes>
1131:>> <Figure size 600x600 with 2 Axes>
1132:>> <Figure size 600x600 with 2 Axes>
[... 131 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/b42a26e6-9b50-422d-b272-9770a97e7467/tool-results/bf37t13ju.txt",
 "offset": 1035,
 "limit": 450
}
```

```
1035	--- [42] md
1036	# Fig 1C - velocity and distance representative plots 
1037	--- [43] code
1038	best_dc = dc_parent_folders[29]
1039	best_zf = zf_parent_folders[0]
1040	--- [44] code
1041	# FIG 1C
1042	rep_zf_velocities = []
1043	rep_zf_times = []
1044	rep_dc_velocities = []
1045	rep_dc_times = []
1046	
1047	filtering = True
1048	with warnings.catch_warnings(record=True):  
1049	    for b, best_fish in enumerate([best_zf, best_dc]):
1050	        for entry in os.listdir(best_fish):
1051	            fig, ((ax0, ax1)) = plt.subplots(2, 1, figsize=(6,6))
1052	            if 'dataframe' in entry or 'dataframe_continuous' in entry:
1053	                if b == 1 and entry == 'dataframe_continuous.h5': # DANIONELLA 
1054	                    fig, ((ax0, ax1)) = plt.subplots(2, 1, figsize=(6,6))
[... 430 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/b42a26e6-9b50-422d-b272-9770a97e7467/tool-results/bf37t13ju.txt",
 "offset": 1727,
 "limit": 1085
}
```

```
1727	--- [70] md
1728	# Fig S1E - monocular behavior analysis
1729	--- [71] code
1730	# angular velocity
1731	
1732	# static, medial right, lateral right, medial left, lateral left, binocular right, binocular left
1733	monocular_stim_order = [20, 11, 10, 9, 13, 3, 2]
1734	trimmed = True # first 35 seconds of each trial
1735	
1736	with warnings.catch_warnings(record=True): 
1737	    stim_choice = monocular_stim_order
1738	    monocular_medanglvel_data_dict = BCDict()
1739	
1740	    for s in stim_choice:
1741	        if s not in monocular_medanglvel_data_dict.keys():
1742	            monocular_medanglvel_data_dict[s] = BCDict()
1743	        # first zebrafish
1744	        avg_fish_arr = np.zeros(shape = (len(zf_parent_folders)))
1745	        arr_lst = []
1746	        color_lst= []
[... 1063 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && cat > look.py <<'EOF'
import h5py, remfile, numpy as np, sys
from dandi.dandiapi import DandiAPIClient
with DandiAPIClient() as c:
    ds = c.get_dandiset("001453","0.250518.1950")
    for path in sys.argv[1:]:
        u = ds.get_asset_by_path(path).get_content_url(follow_redirects=1, strip_query=True)
        f = h5py.File(remfile.File(u),'r')
        g = f['processing/behavior/BehavioralTimeSeries']
        d = {k: g[k+'/data'][:] for k in g}
        t = g['f0_x/timestamps'][:]
        same = all(np.array_equal(t, g[k+'/timestamps'][:], equal_nan=True) for k in g)
        print('====', path, 'n', len(t), 'same ts', same)
        dt = np.diff(t); print('dt pct', np.nanpercentile(dt,[0,1,50,99,100]).round(4), 'n dt>0.5s', (dt>0.5).sum(), 'neg', (dt<0).sum())
        for k,v in d.items(): print(k, 'nan', np.isnan(v).sum(), 'pct', np.nanpercentile(v,[0,1,50,99,100]).round(3))
        st = d['stimulus']; si = d['stim_index']
        print('stim values', np.unique(st[~np.isnan(st)]).astype(int))
        print('n trials', len(np.unique(si[~np.isnan(si)])))
        x,y,th = d['f0_x'],d['f0_y'],d['f0_theta']
        dx, dy = np.diff(x), np.diff(y)
        ok = ~np.isnan(dx)
        print('corr vx vs dx', np.corrcoef(d['f0_vx'][1:][ok], dx[ok])[0,1], 'ratio med', np.nanmedian(np.abs(d['f0_vx'][1:][ok])/np.maximum(np.abs(dx[ok]),1e-9)))
        print('corr vx[:-1] vs dx', np.corrcoef(d['f0_vx'][:-1][ok], dx[ok])[0,1])
        dth = np.diff(th); okt = ~np.isnan(dth)
        print('corr vth vs dth', np.corrcoef(d['f0_vtheta'][1:][okt], dth[okt])[0,1], np.corrcoef(d['f0_vtheta'][:-1][okt], dth[okt])[0,1])
        step = np.hypot(dx,dy)
        print('corr dist vs step', np.corrcoef(d['dist'][1:][ok], step[ok])[0,1], 'ratio', np.nanmedian(d['dist'][1:][ok]/np.maximum(step[ok],1e-9)))
        # trial structure
        idx = np.unique(si[~np.isnan(si)])[:5]
        for i in idx:
            m = si==i
            print(' trial', int(i), 'stim', np.unique(st[m]), 'dur', round(t[m][-1]-t[m][0],2), 'n', m.sum())
        print('frames outside trials', np.isnan(si).sum())
EOF
explore/bin/python look.py sub-0/sub-0_ses-20231031T135510_behavior.nwb sub-12/sub-12_ses-20230614T171042_behavior.nwb 2>&1
```

```
Exit code 1
==== sub-0/sub-0_ses-20231031T135510_behavior.nwb n 85373 same ts True
dt pct [2.00000e-03 5.10000e-03 6.80000e-03 2.00000e-02 1.41277e+03] n dt>0.5s 92 neg 0
dist nan 177 pct [0.00000e+00 1.80000e-02 6.31000e-01 2.24200e+00 4.34995e+02]
f0_theta nan 0 pct [-27.002 -21.98   -1.159  11.575  14.151]
f0_vtheta nan 0 pct [-0.22  -0.103  0.     0.1    0.206]
f0_vx nan 0 pct [-6.079 -1.365  0.023  1.393  4.594]
f0_vy nan 0 pct [-8.801 -1.446  0.009  1.351  7.854]
f0_x nan 0 pct [  12.8    138.41   480.994 1017.727 1105.583]
f0_y nan 0 pct [  10.252   47.567  548.776 1072.94  1108.77 ]
stim_index nan 0 pct [ 0.  0. 25. 52. 52.]
stimulus nan 0 pct [ 0.  0.  9. 19. 19.]
stim values [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19]
n trials 46
corr vx vs dx 0.0624528895546782 ratio med 0.8481903
corr vx[:-1] vs dx 0.04406678029932133
corr vth vs dth 0.29523654871631544 0.08698115979870848
corr dist vs step nan ratio 1.0
 trial 0 stim [10.] dur 18.39 n 2714
 trial 1 stim [3.] dur 19.86 n 2850
[... 24 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && cat > look2.py <<'EOF'
import h5py, remfile, numpy as np, json, time
from dandi.dandiapi import DandiAPIClient
from concurrent.futures import ThreadPoolExecutor
with DandiAPIClient() as c:
    ds = c.get_dandiset("001453","0.250518.1950")
    assets = [(a.path, a.get_content_url(follow_redirects=1, strip_query=True)) for a in ds.get_assets()]
def one(pa):
    p,u = pa; t0=time.time()
    f = h5py.File(remfile.File(u),'r')
    g = f['processing/behavior/BehavioralTimeSeries']
    sp = f['general/subject/species'][()].decode()
    t = g['f0_x/timestamps'][:]
    d = {k: g[k+'/data'][:] for k in ['f0_x','f0_y','f0_theta','f0_vtheta','f0_vx','stimulus','stim_index']}
    si, st = d['stim_index'], d['stimulus']
    dt = np.diff(t)
    res = dict(path=p, sp=sp[:6], n=len(t), hz=float(1/np.median(dt)), secs=time.time()-t0,
               chunks=str(g['f0_x/data'].chunks), comp=str(g['f0_x/data'].compression))
    # per trial: sum(vtheta) vs delta theta; trial duration
    rat, rat2, durs, codes = [], [], [], {}
    for i in np.unique(si[~np.isnan(si)]):
        m = (si==i) & ~np.isnan(d['f0_theta'])
        if m.sum() < 50: continue
        th = d['f0_theta'][m]; vt = d['f0_vtheta'][m]; tt = t[m]
        dth = th[-1]-th[0]
        if abs(dth) > 0.5:
            rat.append(vt.sum()/dth); rat2.append(np.trapezoid(vt, tt)/dth)
        durs.append(tt[-1]-tt[0])
        c = int(np.unique(st[si==i])[0]); codes[c] = codes.get(c,0)+1
        # stim unique per trial?
        if len(np.unique(st[si==i]))>1: res['multi_stim_trial']=True
    res.update(sum_vt_over_dth=float(np.median(rat)) if rat else None, int_vt_over_dth=float(np.median(rat2)) if rat2 else None,
               dur_med=float(np.median(durs)), dur_max=float(np.max(durs)), ntr=len(durs), codes=codes,
               xr=[float(np.nanmin(d['f0_x'])), float(np.nanmax(d['f0_x']))], yr=[float(np.nanmin(d['f0_y'])), float(np.nanmax(d['f0_y']))],
               nan_x=int(np.isnan(d['f0_x']).sum()), nan_si=int(np.isnan(si).sum()), first=d['f0_x'][~np.isnan(d['f0_x'])][:3].tolist(),
               ts_mono=bool((dt>0).all()), t_start=float(t[0]))
    # stim_index monotone?
    s2 = si[~np.isnan(si)]
    res['si_monotone'] = bool((np.diff(s2)>=0).all())
    return res
t0=time.time()
with ThreadPoolExecutor(8) as ex: res = list(ex.map(one, assets))
print('total', time.time()-t0)
json.dump(res, open('look2.json','w'), indent=1)
for r in sorted(res, key=lambda r:(r['sp'], r['path'])):
    print(r['sp'], r['path'].split('/')[1][:28], r['n'], round(r['hz'],1), round(r['secs']), r['ntr'], round(r['dur_med'],1), round(r['dur_max'],1),
          r['sum_vt_over_dth'] and round(r['sum_vt_over_dth'],3), r['int_vt_over_dth'] and round(r['int_vt_over_dth'],3), [round(v) for v in r['xr']+r['yr']], r['nan_x'], r['nan_si'], r['si_monotone'], r.get('multi_stim_trial'), r['chunks'], r['comp'])
    print('    codes', dict(sorted(r['codes'].items())))
EOF
explore/bin/python look2.py 2>&1 | tail -80
```

```
total 125.40443730354309
Danio  sub-0_ses-20230620T110854_be 9842588 170.7 44 184 35.0 14400.0 0.987 0.006 [7, 1123, 11, 1114] 4076729 6702029 True None None None
    codes {0: 9, 1: 9, 2: 9, 3: 10, 4: 9, 5: 9, 6: 8, 7: 9, 8: 9, 9: 9, 10: 9, 11: 9, 12: 10, 13: 9, 14: 9, 15: 9, 16: 10, 17: 9, 18: 9, 19: 10, 20: 1}
Danio  sub-1_ses-20230614T163157_be 642085 167.2 21 72 13.8 35.0 0.933 0.006 [1, 1113, 14, 1106] 217359 430213 True None None None
    codes {0: 4, 1: 1, 2: 3, 3: 2, 4: 6, 5: 4, 6: 5, 7: 4, 8: 5, 9: 4, 10: 3, 11: 3, 12: 4, 13: 4, 14: 3, 15: 3, 16: 3, 17: 4, 18: 5, 19: 2}
Danio  sub-10_ses-20230620T111637_b 219788 34.6 20 141 35.0 73.5 0.988 0.029 [6, 1116, 7, 1110] 28171 80334 True None None None
    codes {0: 7, 1: 7, 2: 7, 3: 7, 4: 7, 5: 7, 6: 7, 7: 7, 8: 7, 9: 7, 10: 7, 11: 7, 12: 7, 13: 7, 14: 7, 15: 7, 16: 7, 17: 7, 18: 7, 19: 7, 20: 1}
Danio  sub-11_ses-20230620T111855_b 2106421 34.4 24 395 35.0 14400.9 0.91 0.026 [6, 1117, -2, 1119] 582797 763367 True None None None
    codes {0: 20, 1: 21, 2: 20, 3: 19, 4: 19, 5: 19, 6: 20, 7: 20, 8: 18, 9: 20, 10: 19, 11: 21, 12: 20, 13: 17, 14: 19, 15: 21, 16: 19, 17: 19, 18: 21, 19: 21, 20: 2}
Danio  sub-12_ses-20230614T171042_b 261221 32.5 19 140 35.0 2281.5 0.953 0.029 [12, 1120, 9, 1112] 35988 58789 True None None None
    codes {0: 7, 1: 7, 2: 7, 3: 6, 4: 7, 5: 7, 6: 7, 7: 7, 8: 7, 9: 7, 10: 7, 11: 7, 12: 7, 13: 7, 14: 7, 15: 7, 16: 7, 17: 7, 18: 7, 19: 7, 20: 1}
Danio  sub-13_ses-20230615T105805_b 336304 32.5 21 116 35.0 35.0 0.998 0.031 [9, 1114, 5, 1108] 158733 213628 True None None None
    codes {0: 5, 1: 5, 2: 5, 3: 6, 4: 6, 5: 6, 6: 6, 7: 6, 8: 6, 9: 6, 10: 6, 11: 6, 12: 6, 13: 6, 14: 6, 15: 6, 16: 6, 17: 5, 18: 6, 19: 6}
Danio  sub-14_ses-20230614T161558_b 377090 32.5 26 136 34.6 4312.6 0.997 0.031 [5, 1117, 3, 1109] 91804 108554 True None None None
    codes {0: 7, 1: 6, 2: 7, 3: 7, 4: 7, 5: 7, 6: 6, 7: 6, 8: 7, 9: 6, 10: 7, 11: 7, 12: 7, 13: 7, 14: 7, 15: 7, 16: 7, 17: 7, 18: 7, 19: 6, 20: 1}
Danio 
[... 60 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && cat > ver.py <<'EOF'
import requests
def assets(v):
    r = requests.get(f"https://api.dandiarchive.org/api/dandisets/001453/versions/{v}/assets/?page_size=200").json()['results']
    return {a['path']:(a['blob'] if 'blob' in a else a['asset_id'], a['size']) for a in r}
a, b = assets('0.250518.1950'), assets('draft')
print(len(a), len(b), a==b)
for p in set(a)|set(b):
    if a.get(p)!=b.get(p): print(p, a.get(p), b.get(p))
m1 = requests.get("https://api.dandiarchive.org/api/dandisets/001453/versions/0.250518.1950/").json()
m2 = requests.get("https://api.dandiarchive.org/api/dandisets/001453/versions/draft/").json()
for k in sorted(set(m1)|set(m2)):
    if m1.get(k)!=m2.get(k): print('META DIFF', k, str(m1.get(k))[:300], '|||', str(m2.get(k))[:300])
EOF
explore/bin/python ver.py
```

```
37 37 True
META DIFF about None ||| [{'name': 'hindbrain', 'schemaKey': 'Anatomy', 'identifier': 'http://purl.obolibrary.org/obo/UBERON_0002028'}, {'name': 'locomotion', 'schemaKey': 'GenericType', 'identifier': 'https://www.cognitiveatlas.org/concept/id/trm_50eb692db57eb'}]
META DIFF citation Fouke, Kaitlyn (2025) Neural circuits underlying divergent visuomotor strategies of zebrafish and Danionella cerebrum (Version 0.250518.1950) [Data set]. DANDI Archive. https://doi.org/10.48324/dandi.001453/0.250518.1950 ||| Fouke, Kaitlyn; He, Zichen; Loring, Matthew D.; Naumann, Eva A. (2026) Neural circuits underlying divergent visuomotor strategies of zebrafish and Danionella cerebrum (Version draft) [Data set]. DANDI Archive. https://dandiarchive.org/dandiset/001453/draft
META DIFF contributor [{'name': 'Fouke, Kaitlyn', 'email': '[removed: an e-mail address]', 'roleName': ['dcite:ContactPerson'], 'schemaKey': 'Person', 'affiliation': [], 'includeInCitation': True}] ||| [{'name': 'Fouke, Kaitlyn', 'email': '[removed: an e-mail address]', 'roleName': ['dcite:ContactPerson', 'dcite:Author'], 'schemaKey': 'Person', 'identifier': '0000-0001-7341-0340', 'affiliation': [{'name': 'Duke University', 'schemaKey': 'Affiliation', 'identifier': 'https://ror.org/00py81415'}], 'includ
META DIFF datePublished 2025-05-18T19:50:10.255848+00:00 ||| None
META DIFF doi 10.48324/dandi.001453/0.250518.1950 ||| None
META DIFF id DANDI:001453/0.250518.1950 ||| DANDI:001453/draft
META DIFF keywords None ||| ['optomotor response', 'Danionella cerebrum', 'visuomotor behavior', 'two-photon calcium imaging', 'direction selectivity', 'closed-loop behavioral tracking', 'comparative neuroscience']
META DIFF manifestLocation ['https://dandiarchive.s3.amazonaws.com/dandisets/001453/0.250518.1950/assets.yaml'] ||| ['https://api.dandiarchive.org/api/dandisets/001453/versions/draft/assets/']
META DIFF publishedBy {'id': 'urn:uuid:5dade24c-f7aa-4d58-83ed-71a7079f72c7', 'name': 'DANDI publish', 'endDate': '2025-05-18T19:5
[... 4 more lines not kept]
```

**Agent calls Bash**

```bash
for r in Naumann-Lab/caImageAnalysis Naumann-Lab/fishFlux Naumann-Lab/behavior_rigs Naumann-Lab/pandastim; do echo "$r $(curl -s -o /dev/null -w '%{http_code}' https://api.github.com/repos/$r)"; done; curl -s "https://api.github.com/orgs/Naumann-Lab/repos?per_page=100" | python3 -c "import json,sys; [print(r['name'], r['pushed_at']) for r in json.load(sys.stdin)]"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR && for b in kaitlyn; do curl -s "https://api.github.com/repos/Naumann-Lab/caImageAnalysis/branches/$b" | python3 -c "import json,sys; d=json.load(sys.stdin); print(d.get('name'), d.get('commit',{}).get('sha'))"; done; git clone -q --depth 50 -b kaitlyn https://github.com/Naumann-Lab/caImageAnalysis.git cai 2>&1 | tail -2; cd cai && git log -1 --format="%H %ad" && grep -rn "stimToNum" --include=*.py . | head; grep -rln "fishFlux\|forward_left" --include=*.py . | head
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR/cai && grep -n "forward_left\|\"static\"\|'static'\|medial\|lateral" constants.py stimuli.py | head -40
```

```
constants.py:2:    "medial_right": "medial_left",
constants.py:3:    "medial_left": "medial_right",
constants.py:8:    "lateral_left": "lateral_right",
constants.py:9:    "lateral_right": "lateral_left",
constants.py:12:    "forward_left": "backward_right",
constants.py:14:    "backward_right": "forward_left",
constants.py:26:    "medial_right": "lateral_right",
constants.py:27:    "medial_left": "lateral_left",
constants.py:32:    "lateral_left": "medial_left",
constants.py:33:    "lateral_right": "medial_right",
constants.py:36:    "forward_left": "backward_right",
constants.py:38:    "backward_right": "forward_left",
constants.py:55:    "forward_left": [0, 0.75, 1],
constants.py:62:    "medial_left" : [0, 1, 0],
constants.py:63:    "medial_right" : [0, 1, 0],
constants.py:64:    "lateral_left" : [1, 0, 1],
constants.py:65:    "lateral_right" : [1, 0, 1]
constants.py:69:    "medial" : [0, 1, 0],
constants.py:70:    "lateral" : [1, 0, 1],
constants.py:92:    "forward_left": "backward_right",
[... 21 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && git clone -q https://github.com/Naumann-Lab/pandastim.git pstim 2>&1|tail -1; cd pstim && git log -1 --format="%H %ad"; find . -iname "*twentyone*" -o -iname "*.hdf" | head; grep -rn "stimToNum\|forward_left" --include=*.py . | head
```

```
7d9d1610be442c5a933e2575c071c64577e6312f Wed Jul 10 11:37:14 2024 -0400
./resources/sevenrep_17stim.hdf
./resources/protocols/stubby_8dir.hdf
./resources/protocols/bhvr_fourstim_speed.hdf
./resources/protocols/sevenrep_17stim.hdf
./resources/protocols/sevenrep_twentyonestim.hdf
./resources/protocols/sevenrep_17stim_04vel.hdf
./resources/protocols/fourstim_speed.hdf
./resources/protocols/bhvr_fourstim_speed_3.7py.hdf
./experiments/twentyonestim.py
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && explore/bin/python -m pip --version >/dev/null 2>&1; uv pip install -q --python explore/bin/python tables 2>&1 | tail -1; explore/bin/python -c "
import pandas as pd
s = pd.read_hdf('pstim/resources/protocols/sevenrep_twentyonestim.hdf')
print(s.columns.tolist()); print(s.head(25).to_string()); print(len(s)); print(list(s.stim_name.unique()))
"; head -60 pstim/experiments/twentyonestim.py
```

```
['stim_name', 'angle', 'velocity', 'stim_type', 'stationary_time', 'duration']
           stim_name       angle      velocity stim_type  stationary_time  duration
0       medial_right   (90, 270)     (0.02, 0)         b                3        35
1              right          90          0.02         s                3        35
2   forward_backward    (0, 180)  (0.02, 0.02)         b                3        35
3         x_backward  (180, 180)     (0, 0.02)         b                3        35
4         converging   (90, 270)  (0.02, 0.02)         b                3        35
5      lateral_right   (270, 90)     (0, 0.02)         b                3        35
6          x_forward      (0, 0)     (0, 0.02)         b                3        35
7           backward         180          0.02         s                3        35
8          forward_x      (0, 0)     (0.02, 0)         b                3        35
9     backward_right         135          0.02         s                3        35
10      forward_left         315          0.02         s                3        35
11      lateral_left   (270, 90)     (0.02, 0)         b                3        35
12        backward_x  (180, 180)     (0.02, 0)         b                3        35
13         diverging   (270, 90)  (0.02, 0.02)         b                3        35
14     forward_right          45          0.02         s                3        35
15       medial_left   (90, 270)     (0, 0.02)         b                3        35
16     backward_left         225          0.02         s                3        35
17              left         270          0.02         s                3        35
[... 70 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && explore/bin/python -c "
import pandas as pd
s = pd.read_hdf('pstim/resources/protocols/sevenrep_twentyonestim.hdf')
print(s.stim_name.value_counts().to_string()); import numpy as np
print(np.where(s.stim_name=='blank')[0][:20]); print(s[s.stim_name=='blank'].head(3).to_string())
print(s.iloc[140:150].to_string())
"
```

```
stim_name
medial_right        70
right               70
forward_backward    70
x_backward          70
converging          70
lateral_right       70
x_forward           70
backward            70
forward_x           70
backward_right      70
forward_left        70
lateral_left        70
backward_x          70
diverging           70
forward_right       70
medial_left         70
backward_left       70
left                70
backward_forward    70
[... 19 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && cat > scale.py <<'EOF'
import h5py, remfile, numpy as np
from dandi.dandiapi import DandiAPIClient
from concurrent.futures import ThreadPoolExecutor
with DandiAPIClient() as c:
    ds = c.get_dandiset("001453","0.250518.1950")
    assets = [(a.path, a.get_content_url(follow_redirects=1, strip_query=True)) for a in ds.get_assets() if a.size < 2e8]
def one(pa):
    p,u = pa
    f = h5py.File(remfile.File(u),'r'); g = f['processing/behavior/BehavioralTimeSeries']
    x = g['f0_x/data'][:]; y = g['f0_y/data'][:]; si = g['stim_index/data'][:]; st = g['stimulus/data'][:]
    m = ~np.isnan(si) & (st != 20) & ~np.isnan(x)
    starts = [np.where((si==i)&~np.isnan(x))[0][0] for i in np.unique(si[m])]
    xs, ys = x[starts], y[starts]
    return p, f['general/subject/species'][()].decode()[:6], np.percentile(x[m],[1,99]).round(), np.percentile(y[m],[1,99]).round(), np.percentile(xs,[5,95]).round(), np.percentile(ys,[5,95]).round()
with ThreadPoolExecutor(8) as ex:
    for r in ex.map(one, assets): print(r[1], r[0].split('/')[1][:24], 'trial x', r[2], 'y', r[3], 'start x', r[4], 'y', r[5])
EOF
explore/bin/python scale.py
```

```
Danion sub-0_ses-20231031T13551 trial x [ 138. 1018.] y [  48. 1073.] start x [240. 694.] y [203. 718.]
Danio  sub-10_ses-20230620T1116 trial x [ 102. 1021.] y [ 52. 952.] start x [208. 734.] y [ 91. 608.]
Danion sub-1_ses-20231031T13555 trial x [  49. 1007.] y [ 49. 984.] start x [252. 769.] y [207. 731.]
Danio  sub-1_ses-20230614T16315 trial x [  37. 1018.] y [ 146. 1026.] start x [216. 733.] y [130. 611.]
Danion sub-10_ses-20240503T1906 trial x [ 21. 972.] y [ 33. 977.] start x [194. 727.] y [232. 751.]
Danio  sub-12_ses-20230614T1710 trial x [160. 993.] y [ 60. 900.] start x [ 205. 1052.] y [ 50. 900.]
Danion sub-11_ses-20240522T0024 trial x [ 29. 981.] y [ 43. 999.] start x [191. 718.] y [214. 750.]
Danio  sub-13_ses-20230615T1058 trial x [ 116. 1034.] y [ 59. 903.] start x [213. 727.] y [ 80. 613.]
Danio  sub-14_ses-20230614T1615 trial x [  81. 1075.] y [ 32. 998.] start x [ 139. 1060.] y [ 49. 830.]
Danio  sub-15_ses-20230620T1119 trial x [ 51. 996.] y [  66. 1038.] start x [123. 907.] y [ 234. 1003.]
Danio  sub-16_ses-20230725T1751 trial x [  77. 1051.] y [131. 957.] start x [261. 788.] y [215. 685.]
Danio  sub-17_ses-20230725T1752 trial x [ 148. 1066.] y [  74. 1077.] start x [260. 797.] y [204. 708.]
Danio  sub-19_ses-20230725T1752 trial x [ 67. 977.] y [119. 831.] start x [280. 809.] y [187. 723.]
Danio  sub-18_ses-20230725T1752 trial x [294. 957.] y [154. 973.] start x [338. 817.] y [241. 711.]
Danion sub-2_ses-20231031T15475 trial x [269. 910.] y [248. 891.] start x [307. 781.] y [310. 801.]
Danio  sub-20_ses-20230725T1755 trial x [  89. 1052.] y [  95. 1077.] start x [191. 732.] y [163. 612.]
Danio  sub-22_ses-20230725T1755 trial x [  52. 1072.] y [  44. 1014.] start x [  82. 1026.] y [ 78. 858.]
Danio  sub-23_ses-20230725T1756 trial x [ 118. 1007.] y [140. 909.] start x [264. 782.] y [203. 727.]
Danio  sub-21_ses-20230725T1755 trial x [ 83. 968.] y [ 206. 1080.] start x [253. 798.] y [222. 737.]
Danio  sub-24_ses-20230725T1756 trial x [123. 909.] y [ 
[... 14 more lines not kept]
```

**Agent calls Write**

```json
{
 "file_path": "claims/001453/10.1016-j.cub.2025.04.027.yaml",
 "content": "# Claims for Fouke, He, Loring & Naumann (2025) on dandiset 001453.\n# Source: the accepted author manuscript in PubMed Central (PMC12218792), full text, read\n# from its Results, figure legends and STAR Methods. The version of record is not open access.\n#\n# When these criteria were written, the author had seen the data check only: the file list,\n# subject metadata, frame rates, units, trial structure and stimulus codes of every file, and\n# the extent of positions. No claim's analysis had been run. The author had also read the\n# outputs printed in the paper's own analysis notebook (Fig1-S1.ipynb, GitLab commit 33a5c29),\n# which include per-stimulus median speeds and angular velocities and its statistics.\n#\n# The dandiset holds only the freely swimming tracking data of Figure 1 and Figure S1. Its\n# stimulus codes 0 to 20 carry no names. The names come from the paper's code and from the\n# stimulus software's protocol file (see stimulus-code-link), so the claims that need them\n# use outside data and depend on that claim.\n#\n# Method choices fixed here, from the paper's Fig1-S1.ipynb where the Methods are silent: a\n# trial is one stim_index; tracked frames only; positions smoothed with a Savitzky-Golay filter\n# (21 frames, order 2); trials rejected when the absolute cumulative heading change exceeds\n# 1000 degrees in the first 10 s or 2000 degrees in the first 35 s, or the mean speed exceeds\n# 100 mm/s; measures taken from 3 s to 35 s after the first frame (the 3 s stationary phase is\n# left out); speed is path length over time, at 10 pixels per mm; angular velocity is the\n# summed heading change over time; each fish's value for a stimulus is the median over its\n# trials, and a species' value is the median over fish.\nschema_version: 1\ndandiset: \"001453\"\npaper: doi:10.1016/j.cub.2025.04.027\nclaims:\n- id: stimulus-code-link\n  statement: The dandiset's stimulus codes can be linked to the stimuli the paper names, using\n    the paper's analysis code and the protocol file of its stimulus software, and the values\n    computed through that link agree with those the paper's code printed.\n  source: Data and Code Availability; the paper's Fig1-S1.ipynb at GitLab commit 33a5c29\n  data: with_inputs\n  criterion: Records are matched by the integer stimulus code. The link holds (reproduced) when\n    every code the analysis uses (0 to 7, 9, 10, 11, 13 and 20) occurs in the dandiset, and the\n    species' median speeds for the nine whole-field stimuli computed here are within 10% of the\n    values printed in Fig1-S1.ipynb for at least 14 of the 18 species and stimulus pairs. It is\n    partially reproduced for 9 to 13 pairs and not reproduced below 9. The fish cannot be\n    matched one to one, as no identifier links the dandiset's subjects to the code's folders;\n    the counts per species are compared instead. The sign of the zebrafish turning response\n    to codes 9 and 11 is reported, as the code and the protocol file disagree on which of them\n    is lateral right.\n- id: fig1d-dc-faster-all-codes\n  statement: Danionella cerebrum (DC) swim at a higher median velocity than zebrafish (ZF)\n    across the visual stimuli.\n  source: Results, first section; Figure 1D\n  criterion: Tested without stimulus names, over all 21 stimulus codes. For each fish and code\n    the median over trials of the trial speed in pixels per second; a two-way ANOVA (type II)\n    of these values on species, code and their interaction. Reproduced when the species effect\n    has p < 0.05 and the DC median over all fish and code values exceeds the ZF median.\n- id: fig1d-median-velocity\n  statement: Across the whole-field stimuli DC have a higher median velocity than ZF (9.8\n    against 6.4 mm/s), with a significant main effect of species in a two-way ANOVA.\n  source: Results, first section; Figure 1D\n  data: with_inputs\n  depends_on:\n  - stimulus-code-link\n  expected:\n  - quantity: DC median velocity over whole-field stimuli\n    value: 9.8\n    tolerance: 0.98\n    unit: mm/s\n  - quantity: ZF median velocity over whole-field stimuli\n    value: 6.4\n    tolerance: 0.64\n    unit: mm/s\n  criterion: Over the nine whole-field stimuli (static, and the eight directions), the paper\n    does not say how the overall median is taken. The readings are (a) the median of the nine\n    per-stimulus species medians; (b) the median over all fish and stimulus values pooled;\n    (c) the median over fish of each fish's median across stimuli; (d) the median over all\n    passing trials pooled. Reproduced when, under one reading, both values are within\n    tolerance and the species effect of a two-way ANOVA (type II) on fish-by-stimulus values\n    has p < 0.05 with DC higher. Partially reproduced when the ANOVA holds but no reading\n    puts both values within tolerance.\n- id: fig1d-zf-forward-faster-than-static\n  statement: ZF modulate their velocity with the direction of motion; forward motion\n    increases their median velocity (static 5.0 mm/s, forward 8.8 mm/s).\n  source: Results, first section; Figure 1D\n  data: with_inputs\n  depends_on:\n  - stimulus-code-link\n  expected:\n  - quantity: ZF median velocity, static\n    value: 5.0\n    tolerance: 0.5\n    unit: mm/s\n  - quantity: ZF median velocity, forward\n    value: 8.8\n    tolerance: 0.88\n    unit: mm/s\n- id: fig1d-dc-no-modulation\n  statement: DC lack the direction-dependent velocity modulation seen in ZF.\n  source: Results, first section; Figure 1D legend\n  data: with_inputs\n  depends_on:\n  - stimulus-code-link\n  criterion: A claim of absence, judged on the paper's test, a two-way ANOVA followed by\n    Tukey's HSD (family-wise alpha 0.05) over all 18 species and stimulus groups of\n    fish-by-stimulus median speeds, as in Fig1-S1.ipynb. Reproduced when no pair of DC\n    stimuli differs significantly; not reproduced when any does. The range of DC\n    per-stimulus medians and the ZF pairs that differ are reported either way.\n- id: fig1d-dc-faster-oblique\n  statement: DC swim at a significantly higher velocity than ZF for oblique stimuli.\n  source: Figure 1D legend\n  criterion: Per stimulus, ZF against DC fish-by-stimulus median speeds with Tukey's HSD on the\n    two groups, at the Bonferroni level 0.05/9, as in Fig1-S1.ipynb. \"Oblique\" can be read as\n    (a) the intercardinal directions forward right, forward left, backward right and backward\n    left, or (b) the motion of 90 degrees or more used for turning in the Results (right,\n    left, backward right, backward left). Reproduced when, under one reading, at least two of\n    its four stimuli show DC significantly faster than ZF.\n  data: with_inputs\n  depends_on:\n  - stimulus-code-link\n- id: fig1g-follow-direction\n  statement: Both species follow the direction of optic flow, turning right (positive angular\n    velocity) to rightward motion and left to leftward motion.\n  source: Figure 1G; Results, second section\n  data: with_inputs\n  depends_on:\n  - stimulus-code-link\n  criterion: For each fish, the mean of its median angular velocities for the rightward\n    stimuli (right, forward right, backward right) minus the mean for the leftward stimuli\n    (left, forward left, backward left). Reproduced when this difference is greater than zero\n    in each species by a one-sided Wilcoxon signed-rank test at p < 0.05; partially reproduced\n    when it holds in one species only. The per-stimulus species medians are reported as well.\n- id: fig1h-zf-higher-angular-acceleration\n  statement: Across directional stimuli ZF have higher angular acceleration than DC, and the\n    distributions of the two species differ for every stimulus.\n  source: Results, second section; Figure 1H (Kruskal-Wallis test with Bonferroni correction)\n  data: with_inputs\n  depends_on:\n  - stimulus-code-link\n  criterion: Angular acceleration as the Methods define it (degrees per second squared), from\n    the heading resampled to 30 Hz so that files with different frame rates are treated alike,\n    smoothed with a 7-sample rolling median before and after each derivative as the code does;\n    absolute values between 10 and 1000 degrees per second squared kept, frames 0 to 35 s\n    into each passing trial, as in Fig1-S1.ipynb. Per stimulus, a Kruskal-Wallis test of ZF\n    against DC frames at p < 0.05/9. Reproduced when, for all nine whole-field stimuli, the\n    test is significant and the ZF median is higher; partially reproduced when that holds for\n    five to eight; not reproduced otherwise. The quantity Fig1-S1.ipynb computes under this\n    name (heading change per frame divided by the file's mean frame interval) is shown as a\n    variant, as is a test on per-fish medians.\n- id: figs1e-dc-respond-less-monocular\n  statement: DC generally respond less than ZF to monocular stimuli, suggesting that they need\n    more visual motion input to drive the optomotor response.\n  source: Results, second section; Figure S1E\n  data: with_inputs\n  depends_on:\n  - stimulus-code-link\n  criterion: As in Fig1-S1.ipynb, the angular velocity toward the stimulated direction (left\n    stimuli sign-flipped), per fish, pooled into static, medial (codes 10 and 13), lateral\n    (9 and 11, with 9 as lateral right, as the figure code has it) and binocular (3 and 2).\n    Reproduced when a two-way ANOVA (type II) on species and category has a species effect at\n    p < 0.05 and the DC median is below the ZF median for both medial and lateral; partially\n    reproduced when the species effect holds and DC is lower for one of the two. The\n    protocol file's assignment of 9 and 11 is shown as a variant.\n- id: fig1c-continuous-vs-bouts\n  statement: ZF swim in discrete bouts separated by glides, while DC swim continuously at a\n    relatively constant velocity.\n  source: Results, first section; Figure 1C and Figure S1D\n  criterion: The paper shows this with representative traces and a bout analysis whose bout\n    files are not in the dandiset, so a measure is fixed here. Per trial, positions resampled\n    to 30 Hz between 3 and 35 s, instantaneous speed, and the ratio of its median to its mean\n    (near 1 for steady swimming, low for bursts); per fish, the median over all trials of all\n    stimulus codes. Reproduced when the ZF fish have lower ratios than the DC fish by a\n    two-sided Mann-Whitney test at p < 0.05.\n- id: fig1cef-representative-values\n  statement: In representative trials ZF bouts reach a peak velocity of 44.7 mm/s with a median\n    of 1.8 mm/s, DC swim at a median of 13.7 mm/s to forward motion; to oblique motion ZF show\n    a median angular velocity of 12.0 degrees/s and median peak angular acceleration of 174\n    degrees/s2, and DC an average peak of 103 degrees/s2 to rightward motion.\n  source: Results, first and second sections; Figure 1C, 1E and 1F\n- id: fig2d-shared-architecture\n  statement: Both species have spatially intermixed, direction-selective neurons enriched in the\n    pretectum and anterior hindbrain, and share the major functional response types.\n  source: Figure 2B to 2F\n- id: fig2g-dsi-similar\n  statement: The average direction selectivity index is similar in ZF and DC (0.62 against 0.66,\n    p > 0.05, Student's t-test, 5 fish each).\n  source: Figure 2G\n- id: fig2h-fewer-motion-responsive\n  statement: ZF tend to have a higher proportion of motion-responsive neurons than DC (0.13\n    against 0.06, p = 0.059).\n  source: Figure 2H\n- id: fig2k-more-monocular\n  statement: DC have a higher proportion of purely monocular neurons than ZF (0.37 against 0.16,\n    p < 0.05).\n  source: Figure 2K\n- id: fig2l-bi-ratio\n  statement: The binocularity index ratio is higher in ZF than in DC (0.72 against 0.24, p =\n    0.010).\n  source: Figure 2L\n- id: fig3e-longer-swims\n  statement: Head-fixed DC perform longer swims than ZF (median 0.75 s against 0.29 s, p <\n    0.0001).\n  source: Figure 3E and 3F\n- id: fig3cd-zf-turn-more\n  statement: Head-fixed ZF show larger directional tail angles than DC to turn-inducing stimuli,\n    and shorten their swims for oblique stimuli while DC do not.\n  source: Figure 3C and 3D\n- id: fig4f-longer-on-duration\n  statement: Swim-onset-associated neurons in DC have a longer active (ON) phase than in ZF,\n    while non-motor-associated neurons have similar ON durations.\n  source: Figure 4E and 4F\n- id: fig4hi-vspn-lateralized\n  statement: Motor-associated neurons in the putative ventromedial spinal projection neurons of\n    both species encode turn direction in a lateralized way, correlating more with ipsilateral\n    turns.\n  source: Figure 4H and 4I\n"
}
```

```
File created successfully at: claims/001453/10.1016-j.cub.2025.04.027.yaml (file state is current in your context — no need to Read it back)
```

**Agent**

Claims file written (20 claims: 9 testable, 11 blocked). Now the helper module.

**Agent calls Write**

```json
{
 "file_path": "entries/001453-fouke-2025/omr.py",
 "content": "\"\"\"Loading and measures for the freely swimming optomotor data of dandiset 001453.\n\nFouke, He, Loring & Naumann (2025), Current Biology, doi:10.1016/j.cub.2025.04.027.\n\nEach NWB file holds one fish: x and y position (pixels), heading (`f0_theta`, radians), its\nchange per frame (`f0_vtheta`; the file says radians/s, the data show radians per frame),\nvelocity estimates, and per frame the stimulus code and trial number (`stim_index`). Files are\nstreamed from the archive at the pinned version; nothing is written to disk.\n\nWhere the parameters come from:\n\n- Trial processing follows the paper's analysis notebook, Fig1-S1.ipynb, in\n  https://gitlab.oit.duke.edu/ean26/danionella_omr_neuralcircuits2025 at commit\n  33a5c297ff4ab6ff49f6bdd96139e9fdd867025c (the Methods give none of these): Savitzky-Golay\n  smoothing of positions (21 frames, order 2); rejection of trials whose absolute cumulative\n  heading change exceeds 1000 degrees in the first 10 s or 2000 degrees in the first 35 s, or\n  whose mean speed exceeds 100 mm/s; measures from 3 s to 35 s after the first tracked frame;\n  10 pixels per mm (the code divides pixels per second by 10 to give mm/s); per fish the median\n  over trials. The 3 s stationary phase and the 32 s of motion are in the Methods.\n- The names of the stimulus codes combine the protocol file sevenrep_twentyonestim.hdf of the\n  stimulus software pandastim (https://github.com/Naumann-Lab/pandastim at commit\n  7d9d1610be442c5a933e2575c071c64577e6312f), whose stimulus names, in order of first\n  appearance, Fig1-S1.ipynb converts to the codes [10, 3, 16, 19, 12, 11, 15, 1, 14, 4, 6, 9,\n  18, 8, 5, 13, 7, 2, 17, 0, 20]. Fig1-S1.ipynb itself labels code 9 as lateral right and 11\n  as lateral left, the reverse of that conversion (its `remapDict` swaps them);\n  `LATERAL_FROM_FIGURE_CODE` keeps the figure code's reading.\n- Angular acceleration as the Methods define it (degrees per second squared) uses the heading\n  resampled to `COMMON_HZ` (a common choice here, as the files' frame rates differ from 32 to\n  171 Hz) and the code's 7-sample rolling medians. `code_angular_acceleration` reproduces what\n  Fig1-S1.ipynb computes under that name.\n\"\"\"\n\nfrom __future__ import annotations\n\nfrom concurrent.futures import ThreadPoolExecutor\n\nimport h5py\nimport numpy as np\nimport pandas as pd\nimport remfile\nfrom dandi.dandiapi import DandiAPIClient\nfrom scipy.signal import savgol_filter\n\nDANDISET_ID = \"001453\"\nDANDISET_VERSION = \"0.250518.1950\"\n\nPX_PER_MM = 10.0          # Fig1-S1.ipynb: pixels per second / 10 = mm/s\nSAVGOL_WINDOW, SAVGOL_ORDER = 21, 2\nMAX_CUM_ANGLE_10S = 1000.0   # degrees, first 10 s of a trial\nMAX_CUM_ANGLE_35S = 2000.0   # degrees, first 35 s\nMAX_SPEED_MM_S = 100.0\nTRIAL_LIMIT_S = 35.0\nMOTION_START_S = 3.0      # the stationary phase before the grating moves\nCOMMON_HZ = 30.0\nROLLING = 7               # Fig1-S1.ipynb, rolling medians of angular velocity and acceleration\nACCEL_RANGE = (10.0, 1000.0)  # Fig1-S1.ipynb keeps absolute values in this range, deg/s^2\n\n# Stimulus codes and names: pandastim's protocol order mapped to codes by Fig1-S1.ipynb.\n_PROTOCOL_NAMES = [\"medial_right\", \"right\", \"forward_backward\", \"x_backward\", \"converging\",\n                   \"lateral_right\", \"x_forward\", \"backward\", \"forward_x\", \"backward_right\",\n                   \"forward_left\", \"lateral_left\", \"backward_x\", \"diverging\", \"forward_right\",\n                   \"medial_left\", \"backward_left\", \"left\", \"backward_forward\", \"forward\", \"blank\"]\n_CODE_ORDER = [10, 3, 16, 19, 12, 11, 15, 1, 14, 4, 6, 9, 18, 8, 5, 13, 7, 2, 17, 0, 20]\nSTIMULUS_NAMES = dict(zip(_CODE_ORDER, _PROTOCOL_NAMES))\nSTIMULUS_NAMES[20] = \"static\"    # the protocol's \"blank\": 4 h without motion after the trials\nLATERAL_FROM_FIGURE_CODE = {9: \"lateral_right\", 11: \"lateral_left\"}\n\nWHOLE_FIELD = [20, 0, 5, 3, 4, 1, 7, 2, 6]     # Fig1-S1.ipynb's order for Figure 1D, G and H\nRIGHTWARD, LEFTWARD = [3, 5, 4], [2, 6, 7]\n\n\ndef asset_urls() -> list[tuple[str, str]]:\n    \"\"\"(path, streaming URL) of every NWB file at the pinned version.\"\"\"\n    with DandiAPIClient() as client:\n        dandiset = client.get_dandiset(DANDISET_ID, DANDISET_VERSION)\n        return sorted((a.path, a.get_content_url(follow_redirects=1, strip_query=True))\n                      for a in dandiset.get_assets() if a.path.endswith(\".nwb\"))\n\n\ndef _text(value) -> str:\n    value = value[()]\n    return value.decode() if isinstance(value, bytes) else str(value)\n\n\ndef load_session(path: str, url: str) -> dict:\n    \"\"\"One fish: its metadata, and the frames that belong to a trial.\n\n    Frames outside a trial (no stim_index) are dropped, and the static block (code 20, hours\n    long) is cut to its first 60 s. Before that, the file's mean frame interval over tracked\n    frames is kept as `code_dt`, which Fig1-S1.ipynb uses for its angular acceleration.\n    \"\"\"\n    with h5py.File(remfile.File(url), \"r\") as f:\n        subject = f[\"general/subject\"]\n        series = f[\"processing/behavior/BehavioralTimeSeries\"]\n        t = series[\"f0_x/timestamps\"][:]\n        data = {k: series[f\"{k}/data\"][:] for k in\n                (\"f0_x\", \"f0_y\", \"f0_theta\", \"f0_vtheta\", \"f0_vx\", \"f0_vy\", \"stimulus\", \"stim_index\")}\n        has_dist = \"dist\" in series\n        if has_dist:\n            data[\"dist\"] = series[\"dist/data\"][:]\n        session = {\n            \"path\": path,\n            \"subject_id\": _text(subject[\"subject_id\"]),\n            \"species\": _text(subject[\"species\"]),\n            \"age\": _text(subject[\"age\"]),\n            \"session_start\": _text(f[\"session_start_time\"]),\n            \"units\": {k: series[f\"{k}/data\"].attrs.get(\"unit\") for k in series},\n            \"descriptions\": {k: series[k].attrs.get(\"description\") for k in series},\n            \"same_timestamps\": all(np.array_equal(series[f\"{k}/timestamps\"][:], t) for k in series),\n            \"has_dist\": has_dist,\n        }\n    tracked = ~np.isnan(data[\"f0_x\"])\n    session[\"n_frames\"] = len(t)\n    session[\"n_tracked\"] = int(tracked.sum())\n    session[\"frame_hz\"] = float(1 / np.median(np.diff(t)))\n    session[\"code_dt\"] = float(np.mean(np.diff(t[tracked])))\n    session[\"x_range\"] = (float(np.nanmin(data[\"f0_x\"])), float(np.nanmax(data[\"f0_x\"])))\n    session[\"y_range\"] = (float(np.nanmin(data[\"f0_y\"])), float(np.nanmax(data[\"f0_y\"])))\n    in_trial = ~np.isnan(data[\"stim_index\"])\n    static = in_trial & (data[\"stimulus\"] == 20)\n    if static.any():\n        start = t[static][0]\n        in_trial &= ~(static & (t > start + 60))\n    session[\"t\"] = t[in_trial]\n    for k, v in data.items():\n        session[k] = v[in_trial]\n    return session\n\n\ndef load_all(workers: int = 8) -> list[dict]:\n    \"\"\"Every fish in the dandiset, loaded in parallel.\"\"\"\n    urls = asset_urls()\n    with ThreadPoolExecutor(workers) as pool:\n        return list(pool.map(lambda pu: load_session(*pu), urls))\n\n\ndef fish_key(session: dict) -> str:\n    \"\"\"Subject ids are reused across species, so a fish is named by species and subject.\"\"\"\n    return f\"{'ZF' if session['species'] == 'Danio rerio' else 'DC'}-sub-{session['subject_id']}\"\n\n\ndef trials(session: dict):\n    \"\"\"(trial number, stimulus code, indices of its tracked frames), in recorded order.\"\"\"\n    tracked = ~np.isnan(session[\"f0_x\"])\n    index = session[\"stim_index\"]\n    for number in np.unique(index):\n        rows = np.flatnonzero((index == number) & tracked)\n        if len(rows):\n            yield int(number), int(session[\"stimulus\"][rows[0]]), rows\n\n\ndef _path_length(x: np.ndarray, y: np.ndarray) -> float:\n    return float(np.hypot(np.diff(x), np.diff(y)).sum())\n\n\ndef _resample(t: np.ndarray, values: list[np.ndarray], hz: float = COMMON_HZ):\n    grid = np.arange(t[0], t[-1], 1 / hz)\n    return grid, [np.interp(grid, t, v) for v in values]\n\n\ndef trial_measures(session: dict) -> pd.DataFrame:\n    \"\"\"One row per trial: whether it passes the code's criteria, and its measures.\n\n    speed_mm_s: path length of the smoothed positions from 3 to 35 s over that time (Fig1-S1).\n    speed30_mm_s: the same from raw positions resampled to 30 Hz (variant).\n    angvel_deg_s: summed heading change from 3 to 35 s over that time (Fig1-S1).\n    steadiness: median over mean of the 30 Hz instantaneous speed, 3 to 35 s.\n    \"\"\"\n    rows = []\n    for number, code, idx in trials(session):\n        t = session[\"t\"][idx]\n        x, y, vth = session[\"f0_x\"][idx], session[\"f0_y\"][idx], session[\"f0_vtheta\"][idx]\n        row = {\"fish\": fish_key(session), \"species\": fish_key(session)[:2], \"path\": session[\"path\"],\n               \"trial\": number, \"code\": code, \"n_frames\": len(idx), \"passes\": False}\n        rows.append(row)\n        if len(idx) < SAVGOL_WINDOW:\n            row[\"reason\"] = \"too short\"\n            continue\n        xs = savgol_filter(x, SAVGOL_WINDOW, SAVGOL_ORDER, mode=\"nearest\")\n        ys = savgol_filter(y, SAVGOL_WINDOW, SAVGOL_ORDER, mode=\"nearest\")\n        if session[\"has_dist\"]:      # DC files carry `dist`, which the code uses in its check\n            step = session[\"dist\"][idx].copy()\n            step[0] = 0\n        else:\n            step = np.concatenate([[0], np.hypot(np.diff(xs), np.diff(ys))])\n        w35 = t < t[0] + TRIAL_LIMIT_S\n        w10 = t < t[0] + 10\n        cum10 = abs(np.sum(vth[w10]) * 180 / np.pi)\n        cum35 = abs(np.sum(vth[w35]) * 180 / np.pi)\n        span = t[w35][-1] - t[0]\n        speed_check = (np.nansum(step[w35]) / PX_PER_MM) / span if span > 0 else np.inf\n        if cum10 > MAX_CUM_ANGLE_10S or cum35 > MAX_CUM_ANGLE_35S or speed_check > MAX_SPEED_MM_S:\n            row[\"reason\"] = \"criteria\"\n            continue\n        keep = w35 & (t > 0)\n        t, xs, ys, vth, xr, yr = t[keep], xs[keep], ys[keep], vth[keep], x[keep], y[keep]\n        if len(t) < 2:\n            row[\"reason\"] = \"empty\"\n            continue\n        motion = (t > t[0] + MOTION_START_S) & (t < t[0] + TRIAL_LIMIT_S)\n        if motion.sum() < 2:\n            row[\"reason\"] = \"no motion phase\"\n            continue\n        tm = t[motion]\n        duration = tm[-1] - tm[0]\n        row.update(passes=True, reason=\"\", duration_s=duration,\n                   speed_mm_s=_path_length(xs[motion], ys[motion]) / duration / PX_PER_MM,\n                   angvel_deg_s=np.sum(vth[motion]) / duration * 180 / np.pi)\n        if duration > 2 / COMMON_HZ:\n            _, (gx, gy) = _resample(tm, [xr[motion], yr[motion]])\n            inst = np.hypot(np.diff(gx), np.diff(gy)) * COMMON_HZ / PX_PER_MM\n            row[\"speed30_mm_s\"] = float(inst.mean()) if len(inst) else np.nan\n            row[\"steadiness\"] = float(np.median(inst) / inst.mean()) if len(inst) and inst.mean() > 0 else np.nan\n    return pd.DataFrame(rows)\n\n\ndef _rolling_median(values: np.ndarray, window: int = ROLLING) -> np.ndarray:\n    return pd.Series(values).rolling(window, min_periods=1).median().to_numpy()\n\n\ndef angular_acceleration(t: np.ndarray, vtheta: np.ndarray) -> np.ndarray:\n    \"\"\"Absolute angular acceleration (deg/s^2) as the Methods define it, at 30 Hz.\n\n    Heading is the cumulative sum of the per-frame change, resampled to 30 Hz; angular velocity\n    and acceleration are its first and second differences over time, each smoothed with the\n    code's 7-sample rolling median.\n    \"\"\"\n    if len(t) < 3 or t[-1] - t[0] < 3 / COMMON_HZ:\n        return np.array([])\n    _, (heading,) = _resample(t, [np.cumsum(vtheta)])\n    omega = _rolling_median(np.diff(heading) * COMMON_HZ)\n    alpha = _rolling_median(np.diff(omega) * COMMON_HZ)\n    return np.abs(alpha) * 180 / np.pi\n\n\ndef code_angular_acceleration(vtheta: np.ndarray, code_dt: float) -> np.ndarray:\n    \"\"\"What Fig1-S1.ipynb computes as angular acceleration (deg/s^2 in its labels).\n\n    Rolling median of the per-frame heading change, divided by the file's mean frame interval,\n    rolling median again. This is an angular velocity, and the mean interval includes the gaps\n    between trials in files that hold only trial frames.\n    \"\"\"\n    return np.abs(_rolling_median(_rolling_median(vtheta) / code_dt)) * 180 / np.pi\n\n\ndef acceleration_frames(session: dict, passing: set) -> pd.DataFrame:\n    \"\"\"Per-frame absolute angular acceleration, 0 to 35 s into each passing trial, both ways.\"\"\"\n    out = []\n    for number, code, idx in trials(session):\n        if (session[\"path\"], number) not in passing:\n            continue\n        t, vth = session[\"t\"][idx], session[\"f0_vtheta\"][idx]\n        keep = (t < t[0] + TRIAL_LIMIT_S) & (t > 0)\n        t, vth = t[keep], vth[keep]\n        if len(t) < 3:\n            continue\n        window = (t > t[0]) & (t < t[0] + TRIAL_LIMIT_S)\n        methods = angular_acceleration(t[window], vth[window])\n        coded = code_angular_acceleration(vth, session[\"code_dt\"])[window]\n        for kind, values in ((\"methods\", methods), (\"code\", coded)):\n            values = values[(values > ACCEL_RANGE[0]) & (values < ACCEL_RANGE[1])]\n            out.append(pd.DataFrame({\"fish\": fish_key(session), \"species\": fish_key(session)[:2],\n                                     \"code\": code, \"kind\": kind, \"accel\": values.astype(np.float32)}))\n    return pd.concat(out, ignore_index=True) if out else pd.DataFrame()\n\n\ndef fish_medians(measures: pd.DataFrame, column: str) -> pd.DataFrame:\n    \"\"\"Per fish and stimulus code, the median over passing trials (failing trials are NaN).\"\"\"\n    m = measures.copy()\n    m.loc[~m[\"passes\"], column] = np.nan\n    out = m.groupby([\"species\", \"fish\", \"code\"])[column].median().reset_index()\n    return out.dropna(subset=[column])\n"
}
```

```
File created successfully at: entries/001453-fouke-2025/omr.py (file state is current in your context — no need to Read it back)
```

**Agent**

Helper written. Now the notebook, generated from a script so I can debug the cells as plain Python first.

**Agent calls Write**

```json
{
 "file_path": "/tmp/claude-1001/make_nb.py",
 "content": "import nbformat as nbf\nimport sys\n\ncells = []\n\n\ndef md(text):\n    cells.append(nbf.v4.new_markdown_cell(text.strip(\"\\n\")))\n\n\ndef code(text, tags=None):\n    c = nbf.v4.new_code_cell(text.strip(\"\\n\"))\n    if tags:\n        c.metadata[\"tags\"] = tags\n    cells.append(c)\n\n\nmd(r\"\"\"\n# Reproducing Fouke et al. (2025) from dandiset 001453\n\n**Paper.** Fouke KE, He Z, Loring MD, Naumann EA (2025). Neural circuits underlying divergent\nvisuomotor strategies of zebrafish and *Danionella cerebrum*. *Current Biology*.\n[doi:10.1016/j.cub.2025.04.027](https://doi.org/10.1016/j.cub.2025.04.027). This attempt used the\nfull text of the accepted author manuscript in PubMed Central (PMC12218792); the version of record\nis not open access.\n\n**Dandiset.** [DANDI:001453](https://dandiarchive.org/dandiset/001453/0.250518.1950), version\n0.250518.1950. The paper cites no DANDI version (its data statement points to a GitLab repository\nthat holds code only). This is the only published version. The draft holds the same 37 files\n(same blobs and sizes); it differs only in metadata added later (authors, keywords, and a\n`relatedResource` link to the paper), none of which the analysis uses.\n\n**What the dandiset holds.** Freely swimming tracking of 25 zebrafish (ZF) and 12 *D. cerebrum*\n(DC) larvae during the optomotor protocol of Figure 1 and Figure S1. The two-photon imaging and the\nhead-fixed tail tracking of Figures 2 to 4 are not in it.\n\n**Outside inputs.** The stimulus codes in the files have no names. The names come from the paper's\nanalysis notebook `Fig1-S1.ipynb` (GitLab `ean26/danionella_omr_neuralcircuits2025`, commit\n33a5c29) and the protocol file of the stimulus software pandastim (GitHub\n`Naumann-Lab/pandastim`, commit 7d9d161). The spatial scale (10 pixels per mm) is the factor in\n`Fig1-S1.ipynb`. Claims marked \"with inputs\" use these and depend on the link claim.\n\nNo random numbers are drawn anywhere in this notebook.\n\n| Claim | Data | Status |\n|---|---|---|\n| stimulus-code-link | with inputs | tested |\n| fig1d-dc-faster-all-codes | dandiset | tested |\n| fig1d-median-velocity | with inputs | tested |\n| fig1d-zf-forward-faster-than-static | with inputs | tested |\n| fig1d-dc-no-modulation | with inputs | tested |\n| fig1d-dc-faster-oblique | with inputs | tested |\n| fig1g-follow-direction | with inputs | tested |\n| fig1h-zf-higher-angular-acceleration | with inputs | tested |\n| figs1e-dc-respond-less-monocular | with inputs | tested |\n| fig1c-continuous-vs-bouts | dandiset | tested |\n| fig1cef-representative-values | dandiset | blocked: the representative fish and trials cannot be identified |\n| fig2d, fig2g, fig2h, fig2k, fig2l (imaging) | dandiset | blocked: data missing |\n| fig3e, fig3cd (head-fixed tail tracking) | dandiset | blocked: data missing |\n| fig4f, fig4hi (imaging with tail tracking) | dandiset | blocked: data missing |\n\"\"\")\n\ncode(r\"\"\"\nimport time\nimport warnings\n\nimport matplotlib.pyplot as plt\nimport numpy as np\nimport pandas as pd\nimport statsmodels.api as sm\nfrom scipy import stats\nfrom statsmodels.formula.api import ols\nfrom statsmodels.stats.multicomp import pairwise_tukeyhsd\n\nimport omr\n\npd.set_option(\"display.width\", 200)\npd.set_option(\"display.max_columns\", 40)\npd.set_option(\"display.max_rows\", 200)\nwarnings.filterwarnings(\"ignore\", category=RuntimeWarning)\n\nstarted = time.time()\nsessions = omr.load_all()\nprint(f\"loaded {len(sessions)} files from dandiset {omr.DANDISET_ID} version {omr.DANDISET_VERSION} \"\n      f\"in {time.time() - started:.0f} s\")\n\"\"\")\n\nmd(r\"\"\"\n## Data check\n\nEach check of the metadata against the values is stated under its output.\n\"\"\")\n\ncode(r\"\"\"\ninfo = pd.DataFrame([{\n    \"fish\": omr.fish_key(s), \"species\": s[\"species\"], \"subject_id\": s[\"subject_id\"], \"age\": s[\"age\"],\n    \"session_start\": s[\"session_start\"][:19], \"frames\": s[\"n_frames\"], \"tracked\": s[\"n_tracked\"],\n    \"frame_hz\": round(s[\"frame_hz\"], 1), \"x_max\": round(s[\"x_range\"][1]), \"y_max\": round(s[\"y_range\"][1]),\n    \"has_dist\": s[\"has_dist\"], \"same_timestamps\": s[\"same_timestamps\"]} for s in sessions])\nprint(\"Files per species:\")\nprint(info.species.value_counts().to_string())\nprint(\"\\nSubject ids used by both species:\",\n      sorted(set(info[info.species == \"Danio rerio\"].subject_id) & set(info[info.species != \"Danio rerio\"].subject_id), key=int))\nprint(\"Distinct subject ids:\", info.subject_id.nunique(), \"; distinct fish (species and id):\", info.fish.nunique())\nprint(\"Age field values:\", info.age.unique().tolist())\nprint(\"Paper, Figure 1D legend: N = ZF 26, DC 12 fish.\")\nprint(\"\\nEvery series in a file shares one timestamp array:\", bool(info.same_timestamps.all()))\nprint(\"\\nStated units:\", sessions[0][\"units\"])\nprint(\"\\n\", info.sort_values([\"species\", \"frame_hz\"]).to_string(index=False))\n\"\"\", tags=[\"sanity\"])\n\nmd(r\"\"\"\nThe archive's summary says 25 subjects and lists only *Danio rerio*. The files hold 37 fish:\nsubject ids 0 to 11 are each used for one zebrafish and one *D. cerebrum*, so `subject_id` alone\ndoes not identify an animal. Fish are named here by species and subject id. The 25 ZF are one fewer\nthan the 26 of the Figure 1D legend; the paper's notebook (`healthy_zf_fish`) lists 25 ZF and 12 DC,\nand its ANOVA has 305 residual degrees of freedom, which fits 25 and 12 fish over nine stimuli\nless ten empty cells. The age is given as a range (P5D/P9D) for every fish.\n\"\"\")\n\ncode(r\"\"\"\nfast = info.frame_hz > 100\nprint(\"Files by frame rate (Methods: tracking at more than 150 Hz):\")\nprint(pd.crosstab(info.species, np.where(fast, \"128-171 Hz\", \"32-35 Hz\")).to_string())\n\n# What f0_vtheta is: compare its sum over a trial with the trial's change of f0_theta.\nrows = []\nfor s in sessions:\n    ratio_sum, ratio_int, vx_frame, vx_sec = [], [], [], []\n    for number, c, idx in omr.trials(s):\n        if len(idx) < 50:\n            continue\n        th, vth, t = s[\"f0_theta\"][idx], s[\"f0_vtheta\"][idx], s[\"t\"][idx]\n        if abs(th[-1] - th[0]) > 0.5:\n            ratio_sum.append(vth.sum() / (th[-1] - th[0]))\n            ratio_int.append(np.trapezoid(vth, t) / (th[-1] - th[0]))\n        dx = np.diff(s[\"f0_x\"][idx])\n        vx = s[\"f0_vx\"][idx][1:]\n        ok = np.abs(dx) > 0.5\n        if ok.sum() > 10:\n            vx_frame.append(np.median(vx[ok] / dx[ok]))\n            vx_sec.append(np.median(vx[ok] / (dx[ok] / np.diff(t)[ok])))\n    rows.append({\"fish\": omr.fish_key(s), \"frame_hz\": round(s[\"frame_hz\"]),\n                 \"sum_vtheta/dtheta\": np.median(ratio_sum), \"integral_vtheta_dt/dtheta\": np.median(ratio_int),\n                 \"vx/(dx per frame)\": np.median(vx_frame), \"vx/(dx per s)\": np.median(vx_sec)})\nunits = pd.DataFrame(rows)\nprint(\"\\nMedian over trials, per file:\")\nprint(units.round(3).to_string(index=False))\nprint(\"\\nAcross files, median of sum(vtheta)/dtheta:\", round(units[\"sum_vtheta/dtheta\"].median(), 3),\n      \"; of integral(vtheta dt)/dtheta:\", round(units[\"integral_vtheta_dt/dtheta\"].median(), 4))\n\"\"\", tags=[\"sanity\"])\n\nmd(r\"\"\"\n`f0_vtheta` is stated in radians/s. Summed over a trial's frames it gives the trial's change of\n`f0_theta` (median ratio near 1 in most files), while its time integral gives about 1/frame rate\nof it. It is the heading change per frame, in radians. The paper's code uses it that way (it sums\nit to get the cumulative angle), so the analysis is unaffected, but the stated unit is wrong.\n`f0_vx` and `f0_vy` are stated in pixels/s; the ratio to the per-frame displacement, printed above,\nis the check (a ratio near 1 per frame means pixels per frame). The paper's code converts them\nwith the frame interval, which treats them as per frame. They are not used below.\n\n16 of 25 ZF files and 1 of 12 DC files are sampled at 32 to 35 Hz, against the Methods' \"more than\n150 Hz\". The measures below are reported by frame-rate group where it could matter.\n\"\"\")\n\ncode(r\"\"\"\n# Spatial scale: trials start when the fish is in the central area, and end when it leaves the\n# 45 mm active area. Positions are in pixels; no scale is given in the files.\nrows = []\nfor s in sessions:\n    starts = np.array([idx[0] for _, c, idx in omr.trials(s) if c != 20])\n    inside = np.concatenate([idx for _, c, idx in omr.trials(s) if c != 20])\n    x, y = s[\"f0_x\"], s[\"f0_y\"]\n    rows.append({\"fish\": omr.fish_key(s),\n                 \"start_x_5_95\": np.ptp(np.percentile(x[starts], [5, 95])),\n                 \"start_y_5_95\": np.ptp(np.percentile(y[starts], [5, 95])),\n                 \"trial_x_1_99\": np.ptp(np.percentile(x[inside], [1, 99])),\n                 \"trial_y_1_99\": np.ptp(np.percentile(y[inside], [1, 99])),\n                 \"x_max\": s[\"x_range\"][1], \"y_max\": s[\"y_range\"][1]})\nextent = pd.DataFrame(rows).round(0)\nprint(extent.to_string(index=False))\nprint(\"\\nMedian extent of trial start positions (px):\", extent[[\"start_x_5_95\", \"start_y_5_95\"]].median().to_dict())\nprint(\"Median extent of positions in trials (px):\", extent[[\"trial_x_1_99\", \"trial_y_1_99\"]].median().to_dict())\nprint(\"Files with any position beyond 1200 px:\", extent[(extent.x_max > 1200) | (extent.y_max > 1200)].fish.tolist())\n\"\"\", tags=[\"sanity\"])\n\nmd(r\"\"\"\nTrial start positions spread over about 500 pixels, and positions in trials over about 900 pixels,\nwith a maximum near 1100 in almost every file. At the code's 10 pixels per mm this is a start area\nof about 50 mm and a field of about 110 mm, close to the 45 mm active area and the 100 mm dish of\nthe Methods. The scale is consistent with the data, not shown by it. One DC file has positions up\nto about 1490 pixels, so its camera field, and possibly its scale, differs from the others.\n\"\"\")\n\ncode(r\"\"\"\ntrial_rows = []\nfor s in sessions:\n    for number, c, idx in omr.trials(s):\n        t = s[\"t\"][idx]\n        trial_rows.append({\"fish\": omr.fish_key(s), \"species\": omr.fish_key(s)[:2], \"code\": c,\n                           \"trial\": number, \"duration_s\": t[-1] - t[0]})\ntrial_table = pd.DataFrame(trial_rows)\nprint(\"Stimulus codes present:\", sorted(trial_table.code.unique()))\ncounts = trial_table.pivot_table(index=\"fish\", columns=\"code\", values=\"trial\", aggfunc=\"count\", fill_value=0)\nprint(\"\\nTrials per fish and stimulus code:\")\nprint(counts.to_string())\nprint(\"\\nFish without code 20 (static):\", counts.index[counts[20] == 0].tolist())\nprint(\"\\nTrial duration (s) by species, codes 0-19 (code 20 is cut to its first 60 s on loading):\")\nprint(trial_table[trial_table.code != 20].groupby(\"species\").duration_s.describe().round(1).to_string())\nprint(\"\\nFraction of trial frames tracked (positions present), by species:\")\nprint(info.assign(sp=info.fish.str[:2], frac=info.tracked / info.frames).groupby(\"sp\").frac.describe().round(3).to_string())\nprint(\"\\nFiles with a `dist` series:\", info.groupby(info.fish.str[:2]).has_dist.sum().to_dict())\n\"\"\", tags=[\"sanity\"])\n\nmd(r\"\"\"\nAll files use codes 0 to 19, and 26 of 37 also code 20. The protocol file of the stimulus software\nhas 140 motion trials (20 stimuli, 7 repeats, each with a 3 s stationary phase and 35 s in all)\nfollowed by a 4-hour \"blank\" block, which is code 20: the \"static\" condition of Figure 1D is the\nstart of that block, one period per fish, after all motion trials. 11 fish have no code 20. The\ntrials of DC are shorter than those of ZF (DC more often leave the active area, which ends a\ntrial). ZF files hold every frame, with untracked frames as NaN and frames between trials; DC files\nhold only tracked trial frames, and carry an extra `dist` series. The two species were evidently\nexported differently.\n\"\"\")\n\ncode(r\"\"\"\n# Recordings deposited twice: compare frame counts, the sequence of stimulus codes, and the first\n# tracked positions of every pair of files.\nsig = []\nfor s in sessions:\n    seq = tuple(c for _, c, _ in omr.trials(s))\n    xs = s[\"f0_x\"][~np.isnan(s[\"f0_x\"])][:500]\n    sig.append((omr.fish_key(s), s[\"n_frames\"], seq, xs))\npairs = []\nfor i in range(len(sig)):\n    for j in range(i + 1, len(sig)):\n        same_n = sig[i][1] == sig[j][1]\n        same_seq = sig[i][2] == sig[j][2]\n        n = min(len(sig[i][3]), len(sig[j][3]))\n        same_x = n > 0 and np.allclose(sig[i][3][:n], sig[j][3][:n])\n        if same_n or same_x or (same_seq and len(sig[i][2]) > 20):\n            pairs.append((sig[i][0], sig[j][0], same_n, same_seq, same_x))\nprint(\"Pairs sharing frame count, stimulus sequence or first positions:\", pairs if pairs else \"none\")\nprint(\"Distinct stimulus sequences:\", len({s[2] for s in sig}), \"of\", len(sig))\n\"\"\", tags=[\"sanity\"])\n\nmd(r\"\"\"\nNo two files share a frame count, a sequence of stimulus codes or their first positions, so no\nrecording appears to be deposited twice.\n\n**Clock of the stimulus labels.** The stimulus code and trial number are series on the same\ntimestamps as the positions, so they share one clock by construction. Whether the labels are\naligned with what the fish saw is checked with a contrast: turning to code 3 minus turning to code 2\n(right and left motion, by the outside mapping; the check itself does not need the names), in\n0.5 s bins from the trial start. If the labels are aligned, the difference should be near zero in\nthe 3 s stationary phase and grow once the grating moves. With each trial given the code of the\ntrial before it, the difference should vanish.\n\"\"\")\n\ncode(r\"\"\"\nbins = np.arange(0, 20.5, 0.5)\n\n\ndef turning_course(shift):\n    out = {}\n    for s in sessions:\n        tr = list(omr.trials(s))\n        for k, (number, c, idx) in enumerate(tr):\n            label = tr[k - shift][1] if k - shift >= 0 else None\n            if label not in (2, 3):\n                continue\n            t = s[\"t\"][idx] - s[\"t\"][idx][0]\n            deg = np.degrees(s[\"f0_vtheta\"][idx])\n            h = np.histogram(t, bins, weights=deg)[0] / 0.5\n            out.setdefault((omr.fish_key(s)[:2], label), []).append(h)\n    return out\n\n\nrows = []\nfig, axes = plt.subplots(1, 2, figsize=(10, 3.5), sharey=True)\nfor ax, shift in zip(axes, (0, 1)):\n    course = turning_course(shift)\n    for sp, colour in ((\"ZF\", \"0.4\"), (\"DC\", \"k\")):\n        diff = np.mean(course[(sp, 3)], axis=0) - np.mean(course[(sp, 2)], axis=0)\n        ax.plot(bins[:-1] + 0.25, diff, color=colour, label=sp)\n        rows.append({\"labels\": \"true\" if shift == 0 else \"previous trial\", \"species\": sp,\n                     \"0-3 s\": diff[bins[:-1] < 3].mean(), \"3-20 s\": diff[bins[:-1] >= 3].mean(),\n                     \"min\": diff.min(), \"max\": diff.max()})\n    ax.axvline(3, ls=\"--\", color=\"0.6\")\n    ax.axhline(0, color=\"0.8\")\n    ax.set_title(\"true labels\" if shift == 0 else \"labels of the previous trial\")\n    ax.set_xlabel(\"time from trial start (s)\")\naxes[0].set_ylabel(\"turning, code 3 minus code 2 (deg/s)\")\naxes[0].legend()\nplt.tight_layout()\nplt.show()\nprint(\"Mean difference in turning (deg/s), code 3 minus code 2; axes autoscaled, all points shown:\")\nprint(pd.DataFrame(rows).round(2).to_string(index=False))\n\"\"\", tags=[\"sanity\"])\n\nmd(r\"\"\"\nThe printed means above give the size of the contrast before and after the grating starts to\nmove, with the true labels and with the labels of the previous trial.\n\"\"\")\n\nmd(r\"\"\"\n## Trial measures\n\nEvery trial is processed as in `Fig1-S1.ipynb` (see the helper's docstring). The counts of trials\ndropped, by reason, follow.\n\"\"\")\n\ncode(r\"\"\"\nstarted = time.time()\nmeasures = pd.concat([omr.trial_measures(s) for s in sessions], ignore_index=True)\nmeasures[\"name\"] = measures.code.map(omr.STIMULUS_NAMES)\nhz = {omr.fish_key(s): s[\"frame_hz\"] for s in sessions}\nmeasures[\"rate\"] = np.where(measures.fish.map(hz) > 100, \"fast\", \"slow\")\nprint(f\"{len(measures)} trials measured in {time.time() - started:.0f} s\")\nprint(\"\\nTrials kept and dropped, by species and reason:\")\nprint(measures.assign(reason=measures.reason.fillna(\"\").replace(\"\", \"kept\")).groupby([\"species\", \"reason\"]).size().to_string())\nprint(\"\\nPassing trials per species:\", measures[measures.passes].groupby(\"species\").size().to_dict())\nprint(\"Range of trial speed (mm/s) in passing trials:\", measures.speed_mm_s.min().round(2), \"to\", measures.speed_mm_s.max().round(2))\nprint(\"Range of trial angular velocity (deg/s):\", measures.angvel_deg_s.min().round(1), \"to\", measures.angvel_deg_s.max().round(1))\n\"\"\")\n\nmd(r\"\"\"\n## stimulus-code-link\n\n> The dandiset's stimulus codes can be linked to the stimuli the paper names, using the paper's\n> analysis code and the protocol file of its stimulus software, and the values computed through\n> that link agree with those the paper's code printed.\n\nReference values: the per-stimulus medians printed by `Fig1-S1.ipynb` (commit 33a5c29), cells\nfor Figure 1D (speed) and Figure 1G (angular velocity).\n\"\"\")\n\ncode(r\"\"\"\nCODE_PRINTED_SPEED = {  # mm/s, Fig1-S1.ipynb output, codes in WHOLE_FIELD order\n    \"DC\": [11.9, 9.7, 10.0, 10.5, 10.5, 10.4, 8.8, 9.4, 9.0],\n    \"ZF\": [5.1, 8.8, 8.4, 6.7, 4.9, 4.3, 5.2, 6.4, 8.3]}\nCODE_PRINTED_ANGVEL = {  # deg/s\n    \"DC\": [-1.8, -2.0, 1.8, 8.7, 3.4, 5.0, -2.3, 0.3, 1.5],\n    \"ZF\": [2.3, 0.6, 6.6, 17.2, 7.7, 0.0, -21.5, -22.3, -1.4]}\n\nused = [0, 1, 2, 3, 4, 5, 6, 7, 9, 10, 11, 13, 20]\npresent = set(trial_table.code.unique())\nprint(\"Codes the analysis uses that are missing from the dandiset:\", sorted(set(used) - present) or \"none\")\nprint(\"Fish per species here:\", info.fish.str[:2].value_counts().to_dict(),\n      \"; in Fig1-S1.ipynb's lists: ZF 25, DC 12; in the paper: ZF 26, DC 12\")\n\nspeed_fish = omr.fish_medians(measures, \"speed_mm_s\")\nangvel_fish = omr.fish_medians(measures, \"angvel_deg_s\")\nrows = []\nfor sp in (\"ZF\", \"DC\"):\n    for k, c in enumerate(omr.WHOLE_FIELD):\n        sv = speed_fish[(speed_fish.species == sp) & (speed_fish.code == c)].speed_mm_s\n        av = angvel_fish[(angvel_fish.species == sp) & (angvel_fish.code == c)].angvel_deg_s\n        rows.append({\"species\": sp, \"code\": c, \"name\": omr.STIMULUS_NAMES[c], \"n_fish\": len(sv),\n                     \"speed_here\": sv.median(), \"speed_code\": CODE_PRINTED_SPEED[sp][k],\n                     \"angvel_here\": av.median(), \"angvel_code\": CODE_PRINTED_ANGVEL[sp][k]})\nlink = pd.DataFrame(rows)\nlink[\"speed_ratio\"] = link.speed_here / link.speed_code\nlink[\"within_10pct\"] = (link.speed_ratio - 1).abs() <= 0.10\nprint(link.round(2).to_string(index=False))\nn_within = int(link.within_10pct.sum())\nprint(f\"\\nSpeed medians within 10% of the code's printed values: {n_within} of {len(link)}\")\nprint(\"Median absolute difference in angular velocity (deg/s):\",\n      round((link.angvel_here - link.angvel_code).abs().median(), 2))\n\"\"\", tags=[\"claim:stimulus-code-link\"])\n\ncode(r\"\"\"\n# Codes 9 and 11: the figure code calls 9 lateral right, the protocol conversion calls 11 lateral right.\nrows = []\nfor c in (10, 13, 9, 11, 3, 2):\n    for sp in (\"ZF\", \"DC\"):\n        v = angvel_fish[(angvel_fish.species == sp) & (angvel_fish.code == c)].angvel_deg_s\n        rows.append({\"code\": c, \"protocol name\": omr.STIMULUS_NAMES[c],\n                     \"figure-code name\": omr.LATERAL_FROM_FIGURE_CODE.get(c, omr.STIMULUS_NAMES[c]),\n                     \"species\": sp, \"n_fish\": len(v), \"median_deg_s\": v.median(),\n                     \"fish_turning_right\": int((v > 0).sum())})\nprint(pd.DataFrame(rows).round(2).to_string(index=False))\n\"\"\", tags=[\"claim:stimulus-code-link\"])\n\nmd(r\"\"\"\n**Result: ...**\n\"\"\")\n\nmd(r\"\"\"\n## fig1d-dc-faster-all-codes\n\n> *D. cerebrum* (DC) swim at a higher median velocity than zebrafish (ZF) across the visual\n> stimuli.\n\nTested without the stimulus names, over all 21 codes, in pixels per second (no scale needed).\n\"\"\")\n\ncode(r\"\"\"\ndef two_way(df, value, factor=\"code\"):\n    model = ols(f\"{value} ~ C(species) + C({factor}) + C(species):C({factor})\", data=df).fit()\n    return sm.stats.anova_lm(model, typ=2)\n\n\nall_codes = speed_fish.assign(speed_px_s=speed_fish.speed_mm_s * omr.PX_PER_MM)\ntable = two_way(all_codes, \"speed_px_s\")\nprint(table.round(4).to_string())\nmed = all_codes.groupby(\"species\").speed_px_s.median()\nprint(\"\\nMedian over fish and code values (px/s):\", med.round(1).to_dict(),\n      \"; n values:\", all_codes.groupby(\"species\").size().to_dict())\nper_fish = all_codes.groupby([\"species\", \"fish\"]).speed_px_s.median()\nprint(\"\\nPer fish, median over codes (px/s):\")\nprint(per_fish.round(1).to_string())\n\"\"\", tags=[\"claim:fig1d-dc-faster-all-codes\"])\n\ncode(r\"\"\"\n# Variants: speed from positions resampled to 30 Hz; ZF split by frame rate.\ns30 = omr.fish_medians(measures, \"speed30_mm_s\").assign(speed_px_s=lambda d: d.speed30_mm_s * omr.PX_PER_MM)\nt30 = two_way(s30, \"speed_px_s\")\nprint(\"30 Hz variant, species effect: F =\", round(t30.loc[\"C(species)\", \"F\"], 2), \"p =\", f\"{t30.loc['C(species)', 'PR(>F)']:.2g}\",\n      \"; medians (px/s):\", s30.groupby(\"species\").speed_px_s.median().round(1).to_dict())\nrate = all_codes.fish.map(lambda f: \"fast\" if hz[f] > 100 else \"slow\")\nprint(\"\\nMedian over fish and code values (px/s) by species and frame rate:\")\nprint(all_codes.assign(rate=rate).groupby([\"species\", \"rate\"]).speed_px_s.agg([\"median\", \"size\"]).round(1).to_string())\nprint(\"\\nThe same with 30 Hz resampled positions:\")\nprint(s30.assign(rate=s30.fish.map(lambda f: \"fast\" if hz[f] > 100 else \"slow\")).groupby([\"species\", \"rate\"]).speed_px_s.agg([\"median\", \"size\"]).round(1).to_string())\n\"\"\", tags=[\"claim:fig1d-dc-faster-all-codes\"])\n\nmd(r\"\"\"\n**Result: ...**\n\"\"\")\n\nmd(r\"\"\"\n## fig1d-median-velocity\n\n> Across the whole-field stimuli DC have a higher median velocity than ZF (9.8 against 6.4 mm/s),\n> with a significant main effect of species in a two-way ANOVA.\n\"\"\")\n\ncode(r\"\"\"\nwf = speed_fish[speed_fish.code.isin(omr.WHOLE_FIELD)].copy()\nwf[\"name\"] = wf.code.map(omr.STIMULUS_NAMES)\nwide = wf.pivot_table(index=[\"species\", \"fish\"], columns=\"name\", values=\"speed_mm_s\")\nprint(\"Per fish median speed (mm/s), whole-field stimuli:\")\nprint(wide.round(1).to_string())\n\n\ndef readings(fish_values, trials_values, column):\n    out = {}\n    for sp in (\"DC\", \"ZF\"):\n        f = fish_values[fish_values.species == sp]\n        out[sp] = {\n            \"a: median of stimulus medians\": f.groupby(\"code\")[column].median().median(),\n            \"b: median of fish x stimulus values\": f[column].median(),\n            \"c: median over fish of fish medians\": f.groupby(\"fish\")[column].median().median(),\n            \"d: median of passing trials\": trials_values[trials_values.species == sp][column].median()}\n    return pd.DataFrame(out)\n\n\nwf_trials = measures[measures.passes & measures.code.isin(omr.WHOLE_FIELD)]\nread = readings(wf, wf_trials, \"speed_mm_s\")\nread[\"DC within 9.8 +/- 0.98\"] = (read.DC - 9.8).abs() <= 0.98\nread[\"ZF within 6.4 +/- 0.64\"] = (read.ZF - 6.4).abs() <= 0.64\nprint(\"\\nOverall medians (mm/s) under each reading:\")\nprint(read.round(2).to_string())\nanova_wf = two_way(wf, \"speed_mm_s\")\nprint(\"\\nTwo-way ANOVA (type II) on fish x stimulus medians:\")\nprint(anova_wf.round(4).to_string())\n\"\"\", tags=[\"claim:fig1d-median-velocity\"])\n\ncode(r\"\"\"\n# Variants: 30 Hz speeds; no trial rejection; by ZF frame-rate group.\nwf30 = s30[s30.code.isin(omr.WHOLE_FIELD)]\nr30 = readings(wf30, measures[measures.passes & measures.code.isin(omr.WHOLE_FIELD)], \"speed30_mm_s\")\na30 = two_way(wf30, \"speed30_mm_s\")\nprint(\"30 Hz positions: overall medians (mm/s)\")\nprint(r30.round(2).to_string())\nprint(\"species effect p =\", f\"{a30.loc['C(species)', 'PR(>F)']:.2g}\")\n\nno_reject = measures.copy()\nno_reject[\"passes\"] = no_reject.speed_mm_s.notna()\nnr = omr.fish_medians(no_reject, \"speed_mm_s\")\nnr = nr[nr.code.isin(omr.WHOLE_FIELD)]\nprint(\"\\nWithout the code's trial rejection (trials with a measure:\", int(no_reject.passes.sum()), \"):\")\nprint(readings(nr, no_reject[no_reject.passes & no_reject.code.isin(omr.WHOLE_FIELD)], \"speed_mm_s\").round(2).to_string())\nprint(\"species effect p =\", f\"{two_way(nr, 'speed_mm_s').loc['C(species)', 'PR(>F)']:.2g}\")\n\nwf_rate = wf.assign(rate=wf.fish.map(lambda f: \"fast\" if hz[f] > 100 else \"slow\"))\nprint(\"\\nReading (b) by species and frame rate (mm/s):\")\nprint(wf_rate.groupby([\"species\", \"rate\"]).speed_mm_s.agg([\"median\", \"size\"]).round(2).to_string())\n\"\"\", tags=[\"claim:fig1d-median-velocity\"])\n\ncode(r\"\"\"\nfig, ax = plt.subplots(figsize=(10, 3.5))\nfor k, c in enumerate(omr.WHOLE_FIELD):\n    for dx, sp, colour in ((-0.15, \"ZF\", \"0.5\"), (0.15, \"DC\", \"k\")):\n        v = wf[(wf.species == sp) & (wf.code == c)].speed_mm_s\n        ax.scatter(np.full(len(v), k + dx), v, s=10, color=colour, label=sp if k == 0 else None)\n        ax.hlines(v.median(), k + dx - 0.1, k + dx + 0.1, color=\"r\")\nax.set_xticks(range(len(omr.WHOLE_FIELD)), [omr.STIMULUS_NAMES[c] for c in omr.WHOLE_FIELD], rotation=30)\nax.set_ylabel(\"fish median speed (mm/s)\")\nax.legend()\nplt.tight_layout()\nplt.show()\nprint(\"Plotted range (mm/s):\", wf.speed_mm_s.min().round(2), \"to\", wf.speed_mm_s.max().round(2), \"; axes autoscaled, all points shown\")\n\"\"\", tags=[\"claim:fig1d-median-velocity\"])\n\nmd(r\"\"\"\n**Result: ...**\n\"\"\")\n\nmd(r\"\"\"\n## fig1d-zf-forward-faster-than-static\n\n> ZF modulate their velocity with the direction of motion; forward motion increases their median\n> velocity (static 5.0 mm/s, forward 8.8 mm/s).\n\"\"\")\n\ncode(r\"\"\"\nfor c in (20, 0):\n    v = wf[(wf.species == \"ZF\") & (wf.code == c)].speed_mm_s\n    print(f\"ZF {omr.STIMULUS_NAMES[c]:8s} median {v.median():.2f} mm/s over {len(v)} fish \"\n          f\"(interquartile {v.quantile(0.25):.2f} to {v.quantile(0.75):.2f})\")\npaired = wide.loc[\"ZF\"][[\"static\", \"forward\"]].dropna()\nprint(f\"\\nZF fish with both: {len(paired)}; forward faster in {(paired.forward > paired.static).sum()}; \"\n      f\"median of forward minus static {np.median(paired.forward - paired.static):.2f} mm/s; \"\n      f\"Wilcoxon p = {stats.wilcoxon(paired.forward, paired.static).pvalue:.3g}\")\nprint(\"\\nBy ZF frame-rate group (median mm/s, n fish):\")\nprint(wf_rate[(wf_rate.species == \"ZF\") & wf_rate.code.isin([20, 0])].groupby([\"rate\", \"code\"]).speed_mm_s.agg([\"median\", \"size\"]).round(2).to_string())\nv30 = wf30[(wf30.species == \"ZF\")].groupby(\"code\").speed30_mm_s.median()\nprint(\"\\n30 Hz variant, ZF static and forward (mm/s):\", round(v30[20], 2), round(v30[0], 2))\n\"\"\", tags=[\"claim:fig1d-zf-forward-faster-than-static\"])\n\nmd(r\"\"\"\n**Result: ...**\n\"\"\")\n\nmd(r\"\"\"\n## fig1d-dc-no-modulation\n\n> DC lack the direction-dependent velocity modulation seen in ZF.\n\nThe paper's test: Tukey's HSD over all 18 species and stimulus groups of fish medians.\n\"\"\")\n\ncode(r\"\"\"\ngroups = wf.species + \"_\" + wf.name\ntukey = pairwise_tukeyhsd(wf.speed_mm_s, groups, alpha=0.05)\nres = pd.DataFrame(tukey.summary().data[1:], columns=tukey.summary().data[0])\ndc_pairs = res[res.group1.str.startswith(\"DC\") & res.group2.str.startswith(\"DC\")]\nzf_pairs = res[res.group1.str.startswith(\"ZF\") & res.group2.str.startswith(\"ZF\")]\nprint(f\"DC pairs: {len(dc_pairs)}, significant: {int(dc_pairs.reject.sum())}; smallest adjusted p {dc_pairs['p-adj'].min():.3f}\")\nprint(f\"ZF pairs: {len(zf_pairs)}, significant: {int(zf_pairs.reject.sum())}; smallest adjusted p {zf_pairs['p-adj'].min():.3f}\")\nprint(res[res.reject].to_string(index=False) if res.reject.any() else \"no significant pair\")\ndc_med = wf[wf.species == \"DC\"].groupby(\"name\").speed_mm_s.median()\nzf_med = wf[wf.species == \"ZF\"].groupby(\"name\").speed_mm_s.median()\nprint(f\"\\nRange of DC per-stimulus medians: {dc_med.min():.2f} to {dc_med.max():.2f} mm/s (ratio {dc_med.max() / dc_med.min():.2f})\")\nprint(f\"Range of ZF per-stimulus medians: {zf_med.min():.2f} to {zf_med.max():.2f} mm/s (ratio {zf_med.max() / zf_med.min():.2f})\")\nfor sp in (\"DC\", \"ZF\"):\n    sub = wf[wf.species == sp]\n    print(f\"{sp}: one-way ANOVA across the nine stimuli, p = {stats.f_oneway(*[g.speed_mm_s for _, g in sub.groupby('code')]).pvalue:.3g}; \"\n          f\"Friedman over fish with all nine: \", end=\"\")\n    w = sub.pivot_table(index=\"fish\", columns=\"code\", values=\"speed_mm_s\").dropna()\n    print(f\"{len(w)} fish, p = {stats.friedmanchisquare(*[w[c] for c in w.columns]).pvalue:.3g}\" if len(w) > 2 else \"too few\")\n\"\"\", tags=[\"claim:fig1d-dc-no-modulation\"])\n\nmd(r\"\"\"\n**Result: ...**\n\"\"\")\n\nmd(r\"\"\"\n## fig1d-dc-faster-oblique\n\n> DC swim at a significantly higher velocity than ZF for oblique stimuli.\n\"\"\")\n\ncode(r\"\"\"\nrows = []\nfor c in omr.WHOLE_FIELD:\n    sub = wf[wf.code == c]\n    t = pairwise_tukeyhsd(sub.speed_mm_s, sub.species)\n    rows.append({\"code\": c, \"name\": omr.STIMULUS_NAMES[c],\n                 \"DC_median\": sub[sub.species == \"DC\"].speed_mm_s.median(),\n                 \"ZF_median\": sub[sub.species == \"ZF\"].speed_mm_s.median(),\n                 \"mean_DC_minus_ZF\": sub[sub.species == \"DC\"].speed_mm_s.mean() - sub[sub.species == \"ZF\"].speed_mm_s.mean(),\n                 \"p\": t.pvalues[0], \"n_DC\": int((sub.species == \"DC\").sum()), \"n_ZF\": int((sub.species == \"ZF\").sum())})\nper_stim = pd.DataFrame(rows)\nper_stim[\"significant_at_0.05/9\"] = per_stim.p < 0.05 / 9\nprint(per_stim.round(4).to_string(index=False))\nreading_a = [\"forward_right\", \"forward_left\", \"backward_right\", \"backward_left\"]\nreading_b = [\"right\", \"left\", \"backward_right\", \"backward_left\"]\nfor label, names in ((\"a, intercardinal\", reading_a), (\"b, 90 degrees or more\", reading_b)):\n    sel = per_stim[per_stim.name.isin(names)]\n    n = int((sel[\"significant_at_0.05/9\"] & (sel.mean_DC_minus_ZF > 0)).sum())\n    print(f\"Reading {label}: {n} of 4 stimuli with DC significantly faster\")\n\"\"\", tags=[\"claim:fig1d-dc-faster-oblique\"])\n\nmd(r\"\"\"\n**Result: ...**\n\"\"\")\n\nmd(r\"\"\"\n## fig1g-follow-direction\n\n> Both species follow the direction of optic flow, turning right (positive angular velocity) to\n> rightward motion and left to leftward motion.\n\"\"\")\n\ncode(r\"\"\"\nawf = angvel_fish[angvel_fish.code.isin(omr.WHOLE_FIELD)].copy()\nawf[\"name\"] = awf.code.map(omr.STIMULUS_NAMES)\nprint(\"Species medians of fish median angular velocity (deg/s), and fish turning right:\")\nsummary = awf.groupby([\"name\", \"species\"]).angvel_deg_s.agg([\"median\", \"size\", lambda v: int((v > 0).sum())])\nsummary.columns = [\"median\", \"n_fish\", \"n_positive\"]\nprint(summary.round(2).unstack(\"species\").to_string())\n\naw = awf.pivot_table(index=[\"species\", \"fish\"], columns=\"code\", values=\"angvel_deg_s\")\nscore = (aw[omr.RIGHTWARD].mean(axis=1) - aw[omr.LEFTWARD].mean(axis=1)).rename(\"right_minus_left\")\nprint(\"\\nPer fish, mean over rightward minus mean over leftward stimuli (deg/s):\")\nprint(score.round(2).to_string())\nfor sp in (\"ZF\", \"DC\"):\n    v = score.loc[sp].dropna()\n    p = stats.wilcoxon(v, alternative=\"greater\").pvalue\n    print(f\"{sp}: {len(v)} fish, median {v.median():.2f} deg/s, {int((v > 0).sum())} positive, one-sided Wilcoxon p = {p:.3g}\")\n\"\"\", tags=[\"claim:fig1g-follow-direction\"])\n\ncode(r\"\"\"\n# Variant: by frame-rate group, and the binocular pair alone (right minus left).\nrate_aw = score.reset_index().assign(rate=lambda d: d.fish.map(lambda f: \"fast\" if hz[f] > 100 else \"slow\"))\nprint(rate_aw.groupby([\"species\", \"rate\"]).right_minus_left.agg([\"median\", \"size\"]).round(2).to_string())\npair = (aw[3] - aw[2]).rename(\"right_minus_left_binocular\")\nfor sp in (\"ZF\", \"DC\"):\n    v = pair.loc[sp].dropna()\n    print(f\"{sp}, codes 3 minus 2 only: median {v.median():.2f} deg/s over {len(v)} fish, p = {stats.wilcoxon(v, alternative='greater').pvalue:.3g}\")\n\"\"\", tags=[\"claim:fig1g-follow-direction\"])\n\nmd(r\"\"\"\n**Result: ...**\n\"\"\")\n\nmd(r\"\"\"\n## fig1h-zf-higher-angular-acceleration\n\n> Across directional stimuli ZF have higher angular acceleration than DC, and the distributions\n> of the two species differ for every stimulus.\n\"\"\")\n\ncode(r\"\"\"\nstarted = time.time()\npassing = set(zip(measures[measures.passes].path, measures[measures.passes].trial))\naccel = pd.concat([omr.acceleration_frames(s, passing) for s in sessions], ignore_index=True)\naccel = accel[accel.code.isin(omr.WHOLE_FIELD)]\nprint(f\"angular acceleration frames computed in {time.time() - started:.0f} s; frames kept:\")\nprint(accel.groupby([\"kind\", \"species\"]).size().to_string())\n\n\ndef accel_tests(kind):\n    rows = []\n    for c in omr.WHOLE_FIELD:\n        sub = accel[(accel.kind == kind) & (accel.code == c)]\n        z, d = sub[sub.species == \"ZF\"].accel, sub[sub.species == \"DC\"].accel\n        fz = sub[sub.species == \"ZF\"].groupby(\"fish\").accel.median()\n        fd = sub[sub.species == \"DC\"].groupby(\"fish\").accel.median()\n        rows.append({\"name\": omr.STIMULUS_NAMES[c], \"ZF_median\": z.median(), \"DC_median\": d.median(),\n                     \"n_ZF\": len(z), \"n_DC\": len(d), \"kruskal_p\": stats.kruskal(z, d).pvalue,\n                     \"ZF_fish_median\": fz.median(), \"DC_fish_median\": fd.median(),\n                     \"fish_mannwhitney_p\": stats.mannwhitneyu(fz, fd).pvalue})\n    out = pd.DataFrame(rows)\n    out[\"zf_higher_and_sig\"] = (out.ZF_median > out.DC_median) & (out.kruskal_p < 0.05 / 9)\n    return out\n\n\nmain = accel_tests(\"methods\")\nprint(\"\\nMethods definition (deg/s^2, heading at 30 Hz), frames 10 to 1000:\")\nprint(main.to_string(index=False, float_format=lambda v: f\"{v:.3g}\"))\nprint(f\"\\nStimuli with ZF higher and Kruskal-Wallis p < 0.05/9: {int(main.zf_higher_and_sig.sum())} of 9\")\nprint(f\"Per-fish variant, ZF fish median higher and Mann-Whitney p < 0.05/9: \"\n      f\"{int(((main.ZF_fish_median > main.DC_fish_median) & (main.fish_mannwhitney_p < 0.05 / 9)).sum())} of 9\")\n\"\"\", tags=[\"claim:fig1h-zf-higher-angular-acceleration\"])\n\ncode(r\"\"\"\ncoded = accel_tests(\"code\")\nprint(\"Variant: Fig1-S1.ipynb's quantity (per-frame heading change / file mean frame interval):\")\nprint(coded.to_string(index=False, float_format=lambda v: f\"{v:.3g}\"))\nprint(f\"\\nStimuli with ZF higher and p < 0.05/9: {int(coded.zf_higher_and_sig.sum())} of 9\")\nratio = pd.DataFrame([{\"fish\": omr.fish_key(s), \"frame_interval_median_ms\": 1000 / s[\"frame_hz\"], \"code_dt_ms\": 1000 * s[\"code_dt\"]} for s in sessions])\nratio[\"code_dt_over_frame_interval\"] = ratio.code_dt_ms / ratio.frame_interval_median_ms\nprint(\"\\nThe code's mean interval against the median frame interval, by species:\")\nprint(ratio.groupby(ratio.fish.str[:2]).code_dt_over_frame_interval.describe().round(2).to_string())\n\"\"\", tags=[\"claim:fig1h-zf-higher-angular-acceleration\"])\n\nmd(r\"\"\"\n**Result: ...**\n\"\"\")\n\nmd(r\"\"\"\n## figs1e-dc-respond-less-monocular\n\n> DC generally respond less than ZF to monocular stimuli, suggesting that they need more visual\n> motion input to drive the optomotor response.\n\"\"\")\n\ncode(r\"\"\"\ndef monocular_table(lateral_right, lateral_left):\n    cats = {\"static\": [(20, 1)], \"medial\": [(10, 1), (13, -1)],\n            \"lateral\": [(lateral_right, 1), (lateral_left, -1)], \"binocular\": [(3, 1), (2, -1)]}\n    rows = []\n    for cat, members in cats.items():\n        for c, sign in members:\n            sub = angvel_fish[angvel_fish.code == c]\n            for _, r in sub.iterrows():\n                rows.append({\"category\": cat, \"species\": r.species, \"fish\": r.fish, \"code\": c,\n                             \"toward_deg_s\": sign * r.angvel_deg_s})\n    return pd.DataFrame(rows)\n\n\ndef monocular_tests(df):\n    model = ols(\"toward_deg_s ~ C(species) + C(category) + C(species):C(category)\", data=df).fit()\n    table = sm.stats.anova_lm(model, typ=2)\n    rows = []\n    for cat in (\"static\", \"medial\", \"lateral\", \"binocular\"):\n        sub = df[df.category == cat]\n        t = pairwise_tukeyhsd(sub.toward_deg_s, sub.species)\n        rows.append({\"category\": cat, \"ZF_median\": sub[sub.species == \"ZF\"].toward_deg_s.median(),\n                     \"DC_median\": sub[sub.species == \"DC\"].toward_deg_s.median(),\n                     \"n_ZF\": int((sub.species == \"ZF\").sum()), \"n_DC\": int((sub.species == \"DC\").sum()),\n                     \"p\": t.pvalues[0], \"significant_at_0.05/4\": t.pvalues[0] < 0.05 / 4})\n    return table, pd.DataFrame(rows)\n\n\nmono = monocular_table(9, 11)\ntable, per_cat = monocular_tests(mono)\nprint(\"Figure-code assignment (9 lateral right, 11 lateral left). Two-way ANOVA (type II):\")\nprint(table.round(4).to_string())\nprint()\nprint(per_cat.round(4).to_string(index=False))\nprint(\"\\nPer fish, angular velocity toward the stimulus (deg/s), mean of the two sides:\")\nprint(mono.groupby([\"species\", \"fish\", \"category\"]).toward_deg_s.mean().unstack().round(1).to_string())\n\"\"\", tags=[\"claim:figs1e-dc-respond-less-monocular\"])\n\ncode(r\"\"\"\nswapped = monocular_table(11, 9)\nt2, p2 = monocular_tests(swapped)\nprint(\"Variant, protocol-file assignment (11 lateral right, 9 lateral left):\")\nprint(\"species effect p =\", f\"{t2.loc['C(species)', 'PR(>F)']:.3g}\")\nprint(p2.round(4).to_string(index=False))\n\"\"\", tags=[\"claim:figs1e-dc-respond-less-monocular\"])\n\nmd(r\"\"\"\n**Result: ...**\n\"\"\")\n\nmd(r\"\"\"\n## fig1c-continuous-vs-bouts\n\n> ZF swim in discrete bouts separated by glides, while DC swim continuously at a relatively\n> constant velocity.\n\nMeasure fixed in the claims file: the ratio of median to mean instantaneous speed (positions at\n30 Hz, 3 to 35 s), per fish the median over all trials of all codes.\n\"\"\")\n\ncode(r\"\"\"\nsteady = measures[measures.passes].groupby([\"species\", \"fish\"]).steadiness.median()\nprint(\"Per fish median steadiness (median / mean instantaneous speed):\")\nprint(steady.round(3).to_string())\nz, d = steady.loc[\"ZF\"].dropna(), steady.loc[\"DC\"].dropna()\np = stats.mannwhitneyu(z, d, alternative=\"two-sided\").pvalue\nprint(f\"\\nZF median {z.median():.3f} over {len(z)} fish; DC median {d.median():.3f} over {len(d)} fish; Mann-Whitney p = {p:.3g}\")\nby_rate = steady.reset_index().assign(rate=lambda df: df.fish.map(lambda f: \"fast\" if hz[f] > 100 else \"slow\"))\nprint(\"\\nBy frame rate of the file:\")\nprint(by_rate.groupby([\"species\", \"rate\"]).steadiness.agg([\"median\", \"size\"]).round(3).to_string())\nzs = by_rate[(by_rate.species == \"ZF\") & (by_rate.rate == \"fast\")].steadiness\nds = by_rate[(by_rate.species == \"DC\") & (by_rate.rate == \"fast\")].steadiness\nprint(f\"Fast files only: ZF {zs.median():.3f} (n {len(zs)}) against DC {ds.median():.3f} (n {len(ds)}), p = {stats.mannwhitneyu(zs, ds).pvalue:.3g}\")\nfwd = measures[measures.passes & (measures.code == 0)].groupby([\"species\", \"fish\"]).steadiness.median()\nprint(f\"Forward trials only (code 0): ZF {fwd.loc['ZF'].median():.3f}, DC {fwd.loc['DC'].median():.3f}, p = {stats.mannwhitneyu(fwd.loc['ZF'].dropna(), fwd.loc['DC'].dropna()).pvalue:.3g}\")\n\"\"\", tags=[\"claim:fig1c-continuous-vs-bouts\"])\n\nmd(r\"\"\"\n**Result: ...**\n\"\"\")\n\nmd(r\"\"\"\n## Summary\n\n...\n\"\"\")\n\nnb = nbf.v4.new_notebook()\nnb.cells = cells\nnb.metadata[\"kernelspec\"] = {\"name\": \"python3\", \"display_name\": \"Python 3\", \"language\": \"python\"}\nnbf.write(nb, sys.argv[1])\nprint(\"cells\", len(cells))\n"
}
```

```
File created successfully at: /tmp/claude-1001/make_nb.py (file state is current in your context — no need to Read it back)
```

**Agent**

Now the entry metadata, then a debug run of the notebook in the exploration environment.

**Agent calls Bash**

```bash
cd entries/001453-fouke-2025 && cat > requirements.in <<'EOF'
dandi
h5py
matplotlib
numpy
pandas
remfile
scipy
statsmodels
EOF
cat > entry.yaml <<'EOF'
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
  relation: reproduces
EOF
cd $TMPDIR && explore/bin/python make_nb.py entries/001453-fouke-2025/reproduce_fouke_2025.ipynb && uv pip install -q --python explore/bin/python ipykernel nbconvert 2>&1 | tail -1; echo ok
```

```
Traceback (most recent call last):
  File "/tmp/claude-1001/make_nb.py", line 1, in <module>
    import nbformat as nbf
ModuleNotFoundError: No module named 'nbformat'
ok
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && explore/bin/python make_nb.py entries/001453-fouke-2025/reproduce_fouke_2025.ipynb && explore/bin/python -m ipykernel install --prefix $TMPDIR/explore --name explore-k >/dev/null && cd entries/001453-fouke-2025 && time JUPYTER_PATH=$TMPDIR/explore/share/jupyter $TMPDIR/explore/bin/python -m jupyter nbconvert --to notebook --execute --ExecutePreprocessor.timeout=3600 --ExecutePreprocessor.kernel_name=explore-k --output-dir $TMPDIR/dbg --output dbg.ipynb reproduce_fouke_2025.ipynb 2>&1 | tail -30
```

```
Exit code 1
Traceback (most recent call last):
  File "/tmp/claude-1001/make_nb.py", line 1, in <module>
    import nbformat as nbf
ModuleNotFoundError: No module named 'nbformat'
```

**Agent calls Bash**

```bash
cd $TMPDIR && uv pip install --python explore/bin/python ipykernel nbconvert nbformat 2>&1 | tail -2; explore/bin/python -c "import nbformat; print(nbformat.__version__)"
```

```
+ traitlets==5.16.1
 + webencodings==0.6.1
5.11.1
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && explore/bin/python make_nb.py entries/001453-fouke-2025/reproduce_fouke_2025.ipynb && explore/bin/python -m ipykernel install --prefix $TMPDIR/explore --name explore-k >/dev/null && cd entries/001453-fouke-2025 && time JUPYTER_PATH=$TMPDIR/explore/share/jupyter $TMPDIR/explore/bin/python -m jupyter nbconvert --to notebook --execute --ExecutePreprocessor.timeout=3600 --ExecutePreprocessor.kernel_name=explore-k --output-dir $TMPDIR/dbg --output dbg.ipynb reproduce_fouke_2025.ipynb 2>&1 | tail -30
```

```
cells 55
[NbConvertApp] Making directory /tmp/claude-1001/dbg
[NbConvertApp] Converting notebook reproduce_fouke_2025.ipynb to notebook
[IPKernelApp] WARNING | Kernel is running over TCP without encryption. All communication (including code and outputs) is sent in plain text and is susceptible to eavesdropping. Use IPC transport or launch with kernel manager-provisioned CurveZMQ keys to enable transport encryption.
[NbConvertApp] Writing 254734 bytes to /tmp/claude-1001/dbg/dbg.ipynb

real	3m57.151s
user	0m41.699s
sys	0m4.951s
```

**Agent**

It ran end to end in 4 minutes. Reading the outputs.

**Agent calls Bash**

```bash
cd $TMPDIR && cat > dump.py <<'EOF'
import nbformat, sys
nb = nbformat.read(sys.argv[1], as_version=4)
for i, c in enumerate(nb.cells):
    if c.cell_type != 'code': continue
    print(f'===== [{i}] {c.metadata.get("tags")}')
    for o in c.outputs:
        if o.output_type == 'stream': print(o.text)
        elif o.output_type == 'error': print('ERROR', o.ename, o.evalue)
        elif 'text/plain' in o.get('data', {}) and 'image/png' not in o['data']: print(o['data']['text/plain'])
EOF
explore/bin/python dump.py dbg/dbg.ipynb | head -330
```

```
===== [1] None
loaded 37 files from dandiset 001453 version 0.250518.1950 in 205 s

===== [3] ['sanity']
Files per species:
species
Danio rerio            25
Danionella cerebrum    12

Subject ids used by both species: ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11']
Distinct subject ids: 25 ; distinct fish (species and id): 37
Age field values: ['P5D/P9D']
Paper, Figure 1D legend: N = ZF 26, DC 12 fish.

Every series in a file shares one timestamp array: True

Stated units: {'f0_theta': 'radians', 'f0_vtheta': 'radians/s', 'f0_vx': 'pixels/s', 'f0_vy': 'pixels/s', 'f0_x': 'pixels', 'f0_y': 'pixels', 'stim_index': 'a.u.', 'stimulus': 'a.u.'}

      fish             species subject_id     age       session_start  frames  tracked  frame_hz  x_max  y_max  has_dist  same_timestamps
ZF-sub-12         Danio rerio         12 P5D/P9D 2023-06-14T17:10:42  261221   225233      32.5   1120   1112     False             True
[... 316 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && explore/bin/python dump.py dbg/dbg.ipynb 2>/dev/null | sed -n 330,700p
```

```
===== [23] ['claim:fig1d-dc-faster-all-codes']
30 Hz variant, species effect: F = 33.13 p = 1.3e-08 ; medians (px/s): {'DC': 95.2, 'ZF': 53.8}

Median over fish and code values (px/s) by species and frame rate:
              median  size
species rate              
DC      fast    86.4   228
        slow   106.6    21
ZF      fast    59.9   145
        slow    52.9   373

The same with 30 Hz resampled positions:
              median  size
species rate              
DC      fast    89.4   228
        slow   112.4    21
ZF      fast    59.3   145
        slow    51.6   373

===== [26] ['claim:fig1d-median-velocity']
[... 351 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && explore/bin/python dump.py dbg/dbg.ipynb 2>/dev/null | sed -n 700,760p
```

```
ZF-sub-6     0.283
         ZF-sub-7     0.281
         ZF-sub-8     0.342
         ZF-sub-9     0.302

ZF median 0.306 over 25 fish; DC median 0.908 over 12 fish; Mann-Whitney p = 5.36e-05

By frame rate of the file:
              median  size
species rate              
DC      fast   0.898    11
        slow   0.999     1
ZF      fast   0.298     7
        slow   0.313    18
Fast files only: ZF 0.298 (n 7) against DC 0.898 (n 11), p = 0.00283
Forward trials only (code 0): ZF 0.376, DC 0.956, p = 1.23e-06
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && python3 - <<'EOF'
p='make_nb.py'; s=open(p).read()
def rep(a,b):
    global s
    assert s.count(a)==1, a[:60]
    s=s.replace(a,b)
rep("""16 of 25 ZF files and 1 of 12 DC files are sampled at 32 to 35 Hz, against the Methods' "more than
150 Hz".""", """18 of 25 ZF files and 1 of 12 DC files are sampled at 32 to 35 Hz, against the Methods' "more than
150 Hz". The ratio of `f0_vtheta`'s sum to the change of `f0_theta` is lower in most DC files
(0.09 to 0.89) than in ZF files, so in DC files the two series do not agree over a trial; the
analysis uses `f0_vtheta`, as the paper's code does.""")
rep("""No two files share a frame count, a sequence of stimulus codes or their first positions, so no
recording appears to be deposited twice.""", """No two files share a frame count or their first positions. The pairs listed share only the
sequence of stimulus codes: six ZF files ran the full fixed protocol of the stimulus software in
the same order. No recording appears to be deposited twice.""")
rep("""print("Mean difference in turning (deg/s), code 3 minus code 2; axes autoscaled, all points shown:")
print(pd.DataFrame(rows).round(2).to_string(index=False))""", """print("Mean difference in turning (deg/s), code 3 minus code 2; axes autoscaled, all points shown:")
print(pd.DataFrame(rows).round(2).to_string(index=False))
course = turning_course(0)
zf_diff = np.mean(course[("ZF", 3)], axis=0) - np.mean(course[("ZF", 2)], axis=0)
print("\\nZF, true labels, by 0.5 s bin from 0 to 6 s:", np.round(zf_diff[:12], 1).tolist())""")
rep("""The printed means above give the size of the contrast before and after the grating starts to
move, with the true labels and with the labels of the previous trial.""", """For ZF the contrast with the true labels is 13.2 deg/s in the stationary phase and 34.8 deg/s from
3 to 20 s, and the binned values rise after 3 s; with the labels of the previous trial it is 7.9
and 6.7 deg/s. The offset before 3 s is consistent with turning carried over from the previous
trial (in the fixed protocol, right motion follows medial-right motion, and the trials after a
code 3 trial start with a positive offset too). For ZF the stimulus labels are consistent with the
timing of the response. For DC the contrast is small (4.6 deg/s from 3 to 20 s with true labels,
0.1 with shifted labels) and noisier in the stationary phase (9.8 and 15.0 deg/s); the timing of
the DC labels could not be established by this check beyond that difference.""")
rep("""print("Range of trial angular velocity (deg/s):", measures.angvel_deg_s.min().round(1), "to", measures.angvel_deg_s.max().round(1))""",
"""print("Range of trial angular velocity (deg/s):", measures.angvel_deg_s.min().round(1), "to", measures.angvel_deg_s.max().round(1))
fast_trials = measures[measures.passes & (measures.speed_mm_s > omr.MAX_SPEED_MM_S)]
print("Passing trials whose measured speed exceeds 100 mm/s (the code's check uses a different "
      "window and, for DC, the stored `dist`):", fast_trials.groupby("species").size().to_dict())""")
# p-value formatting
rep("""table = two_way(all_codes, "speed_px_s")
print(table.round(4).to_string())""", """table = two_way(all_codes, "speed_px_s")
print(table.to_string(float_format=lambda v: f"{v:.4g}"))""")
rep("""print("\\nTwo-way ANOVA (type II) on fish x stimulus medians:")
print(anova_wf.round(4).to_string())""", """print("\\nTwo-way ANOVA (type II) on fish x stimulus medians:")
print(anova_wf.to_string(float_format=lambda v: f"{v:.4g}"))""")
rep("""print("Figure-code assignment (9 lateral right, 11 lateral left). Two-way ANOVA (type II):")
print(table.round(4).to_string())""", """print("Figure-code assignment (9 lateral right, 11 lateral left). Two-way ANOVA (type II):")
print(table.to_string(float_format=lambda v: f"{v:.4g}"))""")
# no-modulation variants
rep("""    print(f"{len(w)} fish, p = {stats.friedmanchisquare(*[w[c] for c in w.columns]).pvalue:.3g}" if len(w) > 2 else "too few")
""", """    print(f"{len(w)} fish, p = {stats.friedmanchisquare(*[w[c] for c in w.columns]).pvalue:.3g}" if len(w) > 2 else "too few")
print("\\nDC static, per fish (mm/s):", wf[(wf.species == 'DC') & (wf.code == 20)].set_index('fish').speed_mm_s.round(1).to_dict())
""")
rep("""## fig1d-dc-faster-oblique
""", """## fig1d-dc-faster-oblique
""")
s = s.replace("""md(r\"\"\"
## fig1d-dc-faster-oblique""", """code(r\"\"\"
# Variants: the eight motion directions only; fish-stimulus values above 100 mm/s left out.
for label, sub in (("directions only", wf[wf.code != 20]), ("values above 100 mm/s left out", wf[wf.speed_mm_s <= 100])):
    t = pairwise_tukeyhsd(sub.speed_mm_s, sub.species + "_" + sub.name)
    r = pd.DataFrame(t.summary().data[1:], columns=t.summary().data[0])
    dcp = r[r.group1.str.startswith("DC") & r.group2.str.startswith("DC")]
    zfp = r[r.group1.str.startswith("ZF") & r.group2.str.startswith("ZF")]
    print(f"{label}: DC pairs significant {int(dcp.reject.sum())} of {len(dcp)} (smallest p {dcp['p-adj'].min():.3f}); "
          f"ZF pairs significant {int(zfp.reject.sum())} of {len(zfp)} (smallest p {zfp['p-adj'].min():.3f})")
\"\"\", tags=["claim:fig1d-dc-no-modulation"])

md(r\"\"\"
**Result: ...**
\"\"\")

md(r\"\"\"
## fig1d-dc-faster-oblique""", 1)
# remove the original Result placeholder that preceded oblique header (now duplicated) - handled by checking below
# fig1h fast-only variant
rep("""print("\\nThe code's mean interval against the median frame interval, by species:")""", """fast_fish = {f for f, v in hz.items() if v > 100}
sub = accel[(accel.kind == "methods") & accel.fish.isin(fast_fish)]
fm = sub.groupby(["species", "fish"]).accel.median()
print("\\nMethods definition, files at 128-171 Hz only: per-fish median over all whole-field frames (deg/s^2):",
      f"ZF {fm.loc['ZF'].median():.1f} (n {len(fm.loc['ZF'])}), DC {fm.loc['DC'].median():.1f} (n {len(fm.loc['DC'])}),",
      f"Mann-Whitney p = {stats.mannwhitneyu(fm.loc['ZF'], fm.loc['DC']).pvalue:.3g}")
print("\\nThe code's mean interval against the median frame interval, by species:")""")
open(p,'w').write(s)
EOF
grep -n "Result: \.\.\." make_nb.py | head -30; grep -n "^## fig1d-dc-faster-oblique\|## fig1d-dc-no-modulation" make_nb.py
```

```
401:**Result: ...**
444:**Result: ...**
523:**Result: ...**
549:**Result: ...**
583:**Result: ...**
598:**Result: ...**
629:**Result: ...**
668:**Result: ...**
729:**Result: ...**
786:**Result: ...**
817:**Result: ...**
553:## fig1d-dc-no-modulation
602:## fig1d-dc-faster-oblique
Shell cwd was reset to
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/make_nb.py",
 "offset": 575,
 "limit": 30
}
```

```
575	    print(f"{sp}: one-way ANOVA across the nine stimuli, p = {stats.f_oneway(*[g.speed_mm_s for _, g in sub.groupby('code')]).pvalue:.3g}; "
576	          f"Friedman over fish with all nine: ", end="")
577	    w = sub.pivot_table(index="fish", columns="code", values="speed_mm_s").dropna()
578	    print(f"{len(w)} fish, p = {stats.friedmanchisquare(*[w[c] for c in w.columns]).pvalue:.3g}" if len(w) > 2 else "too few")
579	print("\nDC static, per fish (mm/s):", wf[(wf.species == 'DC') & (wf.code == 20)].set_index('fish').speed_mm_s.round(1).to_dict())
580	""", tags=["claim:fig1d-dc-no-modulation"])
581	
582	md(r"""
583	**Result: ...**
584	""")
585	
586	code(r"""
587	# Variants: the eight motion directions only; fish-stimulus values above 100 mm/s left out.
588	for label, sub in (("directions only", wf[wf.code != 20]), ("values above 100 mm/s left out", wf[wf.speed_mm_s <= 100])):
589	    t = pairwise_tukeyhsd(sub.speed_mm_s, sub.species + "_" + sub.name)
590	    r = pd.DataFrame(t.summary().data[1:], columns=t.summary().data[0])
591	    dcp = r[r.group1.str.startswith("DC") & r.group2.str.startswith("DC")]
592	    zfp = r[r.group1.str.startswith("ZF") & r.group2.str.startswith("ZF")]
593	    print(f"{label}: DC pairs significant {int(dcp.reject.sum())} of {len(dcp)} (smallest p {dcp['p-adj'].min():.3f}); "
594	          f"ZF pairs significant {int(zfp.reject.sum())} of {len(zfp)} (smallest p {zfp['p-adj'].min():.3f})")
[... 10 more lines not kept]
```

**Agent**

Removing the duplicated placeholder, then re-running to get final numbers before writing conclusions.

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "/tmp/claude-1001/make_nb.py",
 "old_string": "    print(f\"{len(w)} fish, p = {stats.friedmanchisquare(*[w[c] for c in w.columns]).pvalue:.3g}\" if len(w) > 2 else \"too few\")\nprint(\"\\nDC static, per fish (mm/s):\", wf[(wf.species == 'DC') & (wf.code == 20)].set_index('fish').speed_mm_s.round(1).to_dict())\n\"\"\", tags=[\"claim:fig1d-dc-no-modulation\"])\n\nmd(r\"\"\"\n**Result: ...**\n\"\"\")\n\ncode(r\"\"\"",
 "new_string": "    print(f\"{len(w)} fish, p = {stats.friedmanchisquare(*[w[c] for c in w.columns]).pvalue:.3g}\" if len(w) > 2 else \"too few\")\nprint(\"\\nDC static, per fish (mm/s):\", wf[(wf.species == 'DC') & (wf.code == 20)].set_index('fish').speed_mm_s.round(1).to_dict())\n\"\"\", tags=[\"claim:fig1d-dc-no-modulation\"])\n\ncode(r\"\"\""
}
```

```
The file /tmp/claude-1001/make_nb.py has been updated successfully.
```

**Agent calls Bash**

```bash
cd $TMPDIR && explore/bin/python make_nb.py entries/001453-fouke-2025/reproduce_fouke_2025.ipynb && cd entries/001453-fouke-2025 && JUPYTER_PATH=$TMPDIR/explore/share/jupyter $TMPDIR/explore/bin/python -m jupyter nbconvert --to notebook --execute --ExecutePreprocessor.timeout=3600 --ExecutePreprocessor.kernel_name=explore-k --output-dir $TMPDIR/dbg --output dbg.ipynb reproduce_fouke_2025.ipynb 2>&1 | tail -2 && cd $TMPDIR && explore/bin/python dump.py dbg/dbg.ipynb 2>/dev/null | grep -A12 "Mean difference in turning\|Passing trials whose\|C(species) \|DC pairs:\|directions only\|DC static, per\|files at 128\|species effect p" | head -90
```

```
cells 56
[IPKernelApp] WARNING | Kernel is running over TCP without encryption. All communication (including code and outputs) is sent in plain text and is susceptible to eavesdropping. Use IPC transport or launch with kernel manager-provisioned CurveZMQ keys to enable transport encryption.
[NbConvertApp] Writing 259607 bytes to /tmp/claude-1001/dbg/dbg.ipynb
Mean difference in turning (deg/s), code 3 minus code 2; axes autoscaled, all points shown:
        labels species  0-3 s    3-20 s        min       max
          true      ZF  13.16 34.810001   2.580000 49.560001
          true      DC   9.81  4.560000 -15.790000 29.840000
previous trial      ZF   7.85  6.730000   0.220000 16.700001
previous trial      DC  14.98  0.120000 -17.889999 43.450001


ZF, true labels, by 0.5 s bin from 0 to 6 s: [16.799999237060547, 18.0, 16.5, 19.100000381469727, 2.5999999046325684, 5.900000095367432, 14.899999618530273, 19.0, 19.700000762939453, 40.20000076293945, 32.79999923706055, 36.29999923706055]

===== [16] None
4522 trials measured in 3 s

--
Passing trials whose measured speed exceeds 100 mm/s (the code's check uses a different window and, for DC, the stored `dist`): {'DC': 11, 'ZF': 1}

===== [18] ['claim:stimulus-code-link']
[... 74 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && explore/bin/python dump.py dbg/dbg.ipynb 2>/dev/null | grep -B2 -A3 "directions only\|DC static, per\|files at 128\|Friedman" | head -40
```

```
Range of DC per-stimulus medians: 8.81 to 10.52 mm/s (ratio 1.19)
Range of ZF per-stimulus medians: 4.33 to 8.78 mm/s (ratio 2.03)
DC: one-way ANOVA across the nine stimuli, p = 0.479; Friedman over fish with all nine: 9 fish, p = 0.622
ZF: one-way ANOVA across the nine stimuli, p = 0.00082; Friedman over fish with all nine: 18 fish, p = 3.76e-10

DC static, per fish (mm/s): {'DC-sub-10': 19.8, 'DC-sub-11': 0.0, 'DC-sub-2': 106.5, 'DC-sub-4': 10.5, 'DC-sub-5': 11.9, 'DC-sub-6': 0.0, 'DC-sub-7': 13.9, 'DC-sub-8': 4.8, 'DC-sub-9': 9.5}

===== [35] ['claim:fig1d-dc-no-modulation']
directions only: DC pairs significant 0 of 28 (smallest p 0.999); ZF pairs significant 3 of 28 (smallest p 0.009)

values above 100 mm/s left out: DC pairs significant 0 of 36 (smallest p 1.000); ZF pairs significant 0 of 36 (smallest p 0.110)

--
Stimuli with ZF higher and p < 0.05/9: 7 of 9

Methods definition, files at 128-171 Hz only: per-fish median over all whole-field frames (deg/s^2): ZF 84.9 (n 7), DC 178.6 (n 11), Mann-Whitney p = 6.28e-05

The code's mean interval against the median frame interval, by species:
      count  mean   std   min   25%   50%    75%    max
Shell cwd was reset to
```

**Agent**

All numbers are in. Writing the conclusions and summary into the notebook generator.

**Agent calls Bash**

```bash
cd $TMPDIR && cat > results.py <<'PYEOF'
p='make_nb.py'; s=open(p).read()
s = s.replace("""All files use codes 0 to 19, and 26 of 37 also code 20.""", """All files use codes 0 to 19, and 27 of 37 also code 20.""")
s = s.replace("""after all motion trials. 11 fish have no code 20.""", """after all motion trials. 10 fish have no code 20.""")
s = s.replace("""For ZF the contrast with the true labels is 13.2 deg/s in the stationary phase and 34.8 deg/s from
3 to 20 s, and the binned values rise after 3 s;""", """For ZF the contrast with the true labels is 13.2 deg/s in the stationary phase and 34.8 deg/s from
3 to 20 s; in 0.5 s bins it falls to 2.6 and 5.9 deg/s between 2 and 3 s and rises from 3 s on,
to 40.2 deg/s at 4.5 to 5 s;""")
R = [
"""**Result: reproduced.** Every code the analysis uses is in the dandiset. Through the link, 17 of
18 species and stimulus speed medians are within 10% of the values printed by the paper's code (the
exception is DC static, 10.52 against 11.9 mm/s), and the angular velocities differ from the
printed ones by a median of 0.02 deg/s. The fish counts (25 ZF, 12 DC) match the code's lists, not
the paper's 26 ZF. Fish cannot be matched one by one. The data do not settle whether code 9 or 11
is lateral right: the ZF medians for both are near zero (0.02 and 1.59 deg/s), while the medial
codes 10 and 13 give 17.94 and -11.18 deg/s.""",
"""**Result: reproduced.** Over all 21 codes DC swim faster than ZF: median 94.0 against 55.2
pixels/s over fish and code values, species effect F = 78.4, p = 6.3e-18. With positions resampled
to 30 Hz the result is the same (95.2 against 53.8 pixels/s, p = 1.3e-08), and DC are faster within
each frame-rate group (fast files 86.4 against 59.9, slow files 106.6 against 52.9).""",
"""**Result: reproduced.** Under every reading both overall medians are within tolerance of 9.8
and 6.4 mm/s: reading (a) gives DC 10.02 and ZF 6.39, (b) 9.87 and 6.41, (c) 9.36 and 6.33, (d)
9.88 and 6.28. The species effect of the two-way ANOVA is F = 20.8, p = 7.5e-06. With positions
resampled to 30 Hz, DC give 9.43 to 10.15 and ZF 6.07 to 6.30, still within tolerance (p = 0.0011);
without the code's trial rejection the values are unchanged. ZF from 32 to 35 Hz files are slower
(5.88 mm/s, reading b) than ZF from 167 to 171 Hz files (6.98).""",
"""**Result: reproduced.** ZF median speed is 4.84 mm/s for static (18 fish) and 8.78 mm/s for
forward (25 fish), against 5.0 and 8.8. Of 18 fish with both, 14 are faster to forward motion
(median difference 3.67 mm/s, Wilcoxon p = 0.0077). The static value depends on frame rate: 8.31
mm/s in the 5 fish from fast files, 4.50 in the 13 from slow files; forward does not (8.94 and
8.69).""",
"""**Result: not reproduced.** By the paper's test, Tukey's HSD over the 18 groups, 3 of 36 DC
pairs differ (static against backward left, backward right and forward left, adjusted p 0.030 to
0.049), so the test finds a difference within DC. All three involve static, whose DC values come
from 9 fish and include one at 106.5 mm/s and two at 0.0. Among the eight motion directions no DC
pair differs (smallest adjusted p 0.999); the DC per-stimulus medians span 8.81 to 10.52 mm/s
(ratio 1.19, against 2.03 in ZF), and a one-way ANOVA across the nine DC stimuli gives p = 0.479
(ZF p = 0.00082). With values above 100 mm/s left out, no DC pair differs. The same Tukey test
finds no ZF pair over the 18 groups (smallest adjusted p 0.835), and 3 of 28 among the directions
alone.""",
"""**Result: reproduced.** Under reading (b) DC are significantly faster than ZF for right
(p = 0.0002) and backward right (p = 0.0047), 2 of 4; under reading (a) for 1 of 4 (backward
right). Backward motion, which is not oblique, also differs (p = 0.0002).""",
"""**Result: partially reproduced.** ZF follow the direction of motion: the rightward minus leftward
difference is positive in 23 of 25 fish (median 29.51 deg/s, one-sided Wilcoxon p = 9.8e-07). DC do
not by this test: 7 of 12 fish are positive, median 0.88 deg/s, p = 0.151, and the DC median for
left motion is +0.25 deg/s. Codes 3 minus 2 alone give the same (ZF 45.08 deg/s, p = 2.6e-06; DC
3.10 deg/s, p = 0.133). DC turn right to right motion (median 8.67 deg/s), and four DC fish have
differences above 12 deg/s.""",
"""**Result: not reproduced.** With angular acceleration as the Methods define it, DC are higher
than ZF for all nine stimuli (medians 143 to 191 against 55.4 to 66.4 deg/s², Kruskal-Wallis p
below 0.05/9 for each), the reverse of the claim, so 0 of 9 stimuli meet the criterion. Per-fish
medians give the same, and so do the files at 128 to 171 Hz alone (ZF 84.9, DC 178.6 deg/s²,
p = 6.3e-05). The quantity Fig1-S1.ipynb computes gives ZF higher with p below 0.05/9 for 7 of 9
stimuli. That quantity divides each frame's heading change by the file's mean frame interval, which
in DC files is a median 8.73 times the frame interval (ZF 1.37), because DC files hold only trial
frames and the gaps between trials enter the mean.""",
"""**Result: reproduced.** The species effect is significant (F = 23.3, p in the table above), and
DC turn less toward the stimulus than ZF for medial stimuli (median 3.26 against 13.48 deg/s,
p = 0.0003) and binocular ones (2.87 against 21.87 deg/s, p = 0.0002). For lateral stimuli DC are
below ZF only nominally (-1.07 against -0.13 deg/s, p = 0.96): neither species turns toward lateral
motion, and the criterion's lateral part holds by 0.95 deg/s. With the protocol file's assignment
of codes 9 and 11 the lateral medians change sign (ZF 0.13, DC 1.07 deg/s), DC are no longer below
ZF there, and that variant would be partially reproduced.""",
"""**Result: reproduced.** The median-to-mean ratio of instantaneous speed is 0.306 in ZF (25 fish,
0.244 to 0.580) and 0.908 in DC (12 fish, 11 of them above 0.74 and one at 0.140), Mann-Whitney
p = 5.4e-05. The difference holds in the files at 128 to 171 Hz alone (0.298 against 0.898,
p = 0.0028) and in forward trials alone (0.376 against 0.956, p = 1.2e-06).""",
]
for r in R:
    assert "**Result: ...**" in s
    s = s.replace("**Result: ...**", r, 1)
assert "**Result: ...**" not in s
summary = r'''## Summary

A failure to reproduce here may be a failure of this attempt, not of the paper: see the reasoning
and the differences from the paper's method.

| Claim | Data | Outcome |
|---|---|---|
| stimulus-code-link | with inputs | reproduced |
| fig1d-dc-faster-all-codes | dandiset | reproduced |
| fig1d-median-velocity | with inputs | reproduced |
| fig1d-zf-forward-faster-than-static | with inputs | reproduced |
| fig1d-dc-no-modulation | with inputs | not reproduced |
| fig1d-dc-faster-oblique | with inputs | reproduced |
| fig1g-follow-direction | with inputs | partially reproduced |
| fig1h-zf-higher-angular-acceleration | with inputs | not reproduced |
| figs1e-dc-respond-less-monocular | with inputs | reproduced |
| fig1c-continuous-vs-bouts | dandiset | reproduced |
| fig1cef-representative-values | dandiset | blocked: metadata insufficient |
| fig2d, fig2g, fig2h, fig2k, fig2l, fig3e, fig3cd, fig4f, fig4hi | dandiset | blocked: data missing |

**How the analysis differs from the paper's.** The stimulus names come from the paper's code and
the stimulus software, not from the dandiset. The trial processing follows the paper's notebook
`Fig1-S1.ipynb`, except that DC files have no `vel` column, so the code's filter on it is not
applied. The dandiset has 25 ZF, not 26. Angular acceleration follows the Methods' definition, on
heading resampled to 30 Hz; the code's quantity is a variant. The test of "following the direction"
and the measure of continuous swimming are choices made here, as the paper gives no test for the
first and bases the second on bout files that are not in the dandiset.

**What was found about the dandiset.**

- It holds only the freely swimming behaviour of Figure 1 and Figure S1. The imaging and head-fixed
  tail tracking of Figures 2 to 4 are not in it, and the GitLab repository the paper names for
  "all behavioral and imaging data" holds notebooks only.
- The stimulus codes 0 to 20 have no names or description in the files or the metadata. The paper's
  code and the stimulus software disagree on which of codes 9 and 11 is lateral right.
- Subject ids 0 to 11 are each used for one ZF and one DC; the archive's summary counts 25 subjects
  and lists only *Danio rerio*.
- `f0_vtheta` is a heading change per frame, not radians/s as stated; in most DC files its sum does
  not match the change of `f0_theta`.
- 18 of 25 ZF files and 1 DC file are at 32 to 35 Hz, not above 150 Hz as the Methods say.
- No spatial scale is given; positions in pixels are consistent with the code's 10 pixels per mm,
  except one DC file whose positions reach 1490 pixels.
- ZF and DC files were exported differently: ZF files keep untracked and between-trial frames,
  DC files hold only tracked trial frames and an extra `dist` series.
- The paper's code computes "angular acceleration" as heading change per frame divided by the
  file's mean frame interval, which the gaps between trials inflate in DC files; the Figure 1H
  result depends on it.
'''
s = s.replace('''md(r"""
## Summary

...
""")''', 'md(r"""\n' + summary + '""")')
assert "## Summary\n\n..." not in s
open(p,'w').write(s)
PYEOF
explore/bin/python results.py && explore/bin/python make_nb.py entries/001453-fouke-2025/reproduce_fouke_2025.ipynb
```

```
cells 56
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && python3 - <<'EOF'
p='make_nb.py'; s=open(p).read()
a="""lower in most DC files
(0.09 to 0.89) than in ZF files,"""
assert a in s; s=s.replace(a, """lower in most DC files
(0.09 to 0.89) than in most ZF files,""")
a="""is the check (a ratio near 1 per frame means pixels per frame). The paper's code converts them
with the frame interval, which treats them as per frame. They are not used below."""
assert a in s; s=s.replace(a, """is the check: per frame it is 0.63 to 1.11, per second about the frame interval, so these are
pixels per frame. The paper's code converts them with the frame interval, which treats them as per
frame. They are not used below.""")
open(p,'w').write(s)
EOF
explore/bin/python make_nb.py entries/001453-fouke-2025/reproduce_fouke_2025.ipynb
```

```
cells 56
Shell cwd was reset to
```

**Agent**

Now the entry README and the attempt record.

**Agent calls Write**

```json
{
 "file_path": "entries/001453-fouke-2025/README.md",
 "content": "# Fouke, He, Loring & Naumann (2025) from dandiset 001453\n\nTests the findings of [Fouke et al. (2025)](https://doi.org/10.1016/j.cub.2025.04.027) that can be\ntested on [DANDI:001453](https://dandiarchive.org/dandiset/001453/0.250518.1950), which holds the\nfreely swimming tracking of 25 zebrafish and 12 *Danionella cerebrum* larvae (Figure 1 and Figure\nS1). The imaging and head-fixed tail tracking of Figures 2 to 4 are not in it.\n\n| Claim | Outcome |\n|---|---|\n| The stimulus codes can be linked to the paper's stimuli through its code | Reproduced |\n| DC swim faster than ZF, over all stimulus codes | Reproduced |\n| Median speed over whole-field stimuli, DC 9.8 and ZF 6.4 mm/s | Reproduced |\n| ZF are faster to forward motion than to a static grating (8.8 against 5.0 mm/s) | Reproduced |\n| DC do not modulate speed with stimulus direction | Not reproduced |\n| DC are faster than ZF for oblique stimuli | Reproduced |\n| Both species turn in the direction of motion | Partially reproduced |\n| ZF have higher angular acceleration than DC | Not reproduced |\n| DC turn less than ZF to monocular stimuli | Reproduced |\n| ZF swim in bouts, DC continuously | Reproduced |\n| Values from representative trials (Figure 1C, E, F) | Blocked: metadata insufficient |\n| Figures 2 to 4: imaging and head-fixed tail tracking (nine claims) | Blocked: data missing |\n\nA failure to reproduce here may be a failure of this attempt, not of the paper: see the\nreasoning and the differences from the paper's method.\n\nThe files carry no names for their stimulus codes. The names come from the paper's analysis\nnotebook and the protocol file of its stimulus software, so most claims use these outside inputs.\nThe attempt record, with the reasons and the differences from the paper's method, is\n[`attempts/001453-fouke-2025-01.yaml`](../../attempts/001453-fouke-2025-01.yaml).\n\n- `reproduce_fouke_2025.ipynb`: the analysis. It takes about five minutes, most of it streaming the\n  files.\n- `omr.py`: loading the files, the stimulus names, and the trial measures of the paper's code, with\n  the angular acceleration of the Methods. Other notebooks on this dandiset can import it.\n"
}
```

```
File created successfully at: entries/001453-fouke-2025/README.md (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
python tools/entry.py lock entries/001453-fouke-2025 && time python tools/entry.py all entries/001453-fouke-2025 2>&1 | tail -15
```

```
wrote entries/001453-fouke-2025/requirements.lock.txt
Installed kernelspec registry-001453-fouke-2025 in executed/001453-fouke-2025/.venv/share/jupyter/kernels/registry-001453-fouke-2025
0 error(s)
pass  reproduce_fouke_2025.ipynb  (226 s)

real	3m52.327s
user	0m45.914s
sys	0m6.103s
```

**Agent**

Passed in 226 s. Checking that the executed copy's numbers match the conclusions (locked versions may differ from my exploration env).

**Agent calls Bash**

```bash
cd $TMPDIR && explore/bin/python - <<'EOF'
import nbformat
def outs(path):
    nb = nbformat.read(path, as_version=4)
    r=[]
    for c in nb.cells:
        if c.cell_type!='code': continue
        t=''
        for o in c.outputs:
            if o.output_type=='stream': t+=o.text
            elif o.output_type=='error': t+='ERROR '+o.evalue
            elif 'text/plain' in o.get('data',{}) and 'image/png' not in o['data']: t+=o['data']['text/plain']
        r.append(t)
    return r
a = outs('dbg/dbg.ipynb'); b = outs('executed/001453-fouke-2025/reproduce_fouke_2025.ipynb')
import difflib
for i,(x,y) in enumerate(zip(a,b)):
    if x!=y:
        d=[l for l in difflib.unified_diff(x.splitlines(), y.splitlines(), lineterm='', n=0) if not l.startswith(('---','+++','@@'))]
        print(i, d[:10])
EOF
grep -o '"F = [^"]*\|C(species)  [^\\]*' executed/001453-fouke-2025/reproduce_fouke_2025.ipynb | head
```

```
0 ['-loaded 37 files from dandiset 001453 version 0.250518.1950 in 191 s', '+loaded 37 files from dandiset 001453 version 0.250518.1950 in 192 s']
C(species)         2.694e+05   1 78.44 6.272e-18
C(species)               966   1 20.78 7.477e-06
C(species)                  3411   1 23.26 2.508e-06
Shell cwd was reset to
```

**Agent calls Bash**

```bash
for q in Danionella Naumann Fouke; do curl -s "https://api.dandiarchive.org/api/dandisets/?search=$q&page_size=50" | python3 -c "import json,sys; [print('$q', d['identifier'], (d.get('most_recent_published_version') or d['draft_version'])['name'][:90]) for d in json.load(sys.stdin)['results']]"; done
```

Result: the fetched text is not kept.

**Agent calls Write**

```json
{
 "file_path": "attempts/001453-fouke-2025-01.yaml",
 "content": "schema_version: 1\nid: 001453-fouke-2025-01\ndandiset: \"001453\"\ndandiset_version: 0.250518.1950\npaper: doi:10.1016/j.cub.2025.04.027\ndate: 2026-10-14\nentry: 001453-fouke-2025\nprovenance:\n  kind: agent\n  accountable:\n    name: CatalystNeuro\n  agent:\n    harness: Claude Code (GitHub Actions)\n    model: claude-opus-5-5\n    protocol: pilot-5\ninputs:\n- what: Names of the stimulus codes (the conversion of stimulus names to codes, its printed list of\n    codes, and its own labels for codes 9 to 13), the trial processing parameters, the spatial\n    scale of 10 pixels per mm, and the per-stimulus medians it printed, used as reference values\n    for the link claim. From the paper's analysis notebook Fig1-S1.ipynb.\n  source: https://gitlab.oit.duke.edu/ean26/danionella_omr_neuralcircuits2025 at commit\n    33a5c297ff4ab6ff49f6bdd96139e9fdd867025c\n- what: Stimulus names in protocol order, from the protocol file\n    resources/protocols/sevenrep_twentyonestim.hdf of the stimulus software pandastim.\n  source: https://github.com/Naumann-Lab/pandastim at commit 7d9d1610be442c5a933e2575c071c64577e6312f\noutcomes:\n- claim: stimulus-code-link\n  outcome: reproduced\n  notebook: reproduce_fouke_2025.ipynb\n  output: claim:stimulus-code-link\n  notes: Codes are matched by their integer value. All 21 codes are in the dandiset, including\n    every code the analysis uses. Through the link, 17 of 18 species and stimulus speed medians\n    are within 10% of the values printed by Fig1-S1.ipynb (DC static is 10.52 against 11.9\n    mm/s), and the angular velocities differ from the printed ones by a median of 0.02 deg/s.\n    The fish counts (25 ZF, 12 DC) match the code's lists; fish cannot be matched one by one, as\n    no identifier links the dandiset's subjects to the code's folders. The data do not settle\n    which of codes 9 and 11 is lateral right; the ZF medians are 0.02 and 1.59 deg/s.\n  deviations:\n  - The code's filter on a `vel` column is not applied to DC trials, as the DC files have no such\n    series; this may explain the one DC static value outside 10%.\n- claim: fig1d-dc-faster-all-codes\n  outcome: reproduced\n  notebook: reproduce_fouke_2025.ipynb\n  output: claim:fig1d-dc-faster-all-codes\n  notes: Over all 21 codes, the median over fish and code values is 94.0 pixels/s for DC and 55.2\n    for ZF; species effect F = 78.4, p = 6.3e-18. With positions resampled to 30 Hz, 95.2\n    against 53.8 (p = 1.3e-08). DC are faster within each frame-rate group.\n  deviations:\n  - Tested over all stimulus codes without their names; the paper's figure uses nine whole-field\n    stimuli.\n  - The comparison assumes one spatial scale for all rigs, which the files do not state.\n- claim: fig1d-median-velocity\n  outcome: reproduced\n  notebook: reproduce_fouke_2025.ipynb\n  output: claim:fig1d-median-velocity\n  measured:\n  - 9.87\n  - 6.41\n  notes: All four readings put both values within tolerance; (a) median of stimulus medians DC\n    10.02 and ZF 6.39 mm/s, (b) median of fish and stimulus values 9.87 and 6.41 (given as\n    measured), (c) median of fish medians 9.36 and 6.33, (d) median of trials 9.88 and 6.28.\n    Species effect F = 20.8, p = 7.5e-06. With 30 Hz positions DC 9.43 to 10.15 and ZF 6.07 to\n    6.30 (p = 0.0011); without trial rejection the values are unchanged.\n  deviations:\n  - The paper does not say how the overall median is taken; four readings are shown, and all\n    match.\n  - 25 ZF, where the paper states 26.\n  - Speeds rely on the code's scale of 10 pixels per mm, which the dandiset does not state.\n- claim: fig1d-zf-forward-faster-than-static\n  outcome: reproduced\n  notebook: reproduce_fouke_2025.ipynb\n  output: claim:fig1d-zf-forward-faster-than-static\n  measured:\n  - 4.84\n  - 8.78\n  notes: ZF static 4.84 mm/s over 18 fish and forward 8.78 mm/s over 25 fish. Of 18 fish with\n    both, 14 are faster to forward motion (median difference 3.67 mm/s, Wilcoxon p = 0.0077).\n    The static value is 8.31 mm/s in the 5 fish from 167 to 171 Hz files and 4.50 in the 13\n    from 32 to 35 Hz files. Static is the start of a 4-hour blank block after all motion trials,\n    one period per fish, and 7 ZF have none.\n  deviations:\n  - 25 ZF, where the paper states 26.\n- claim: fig1d-dc-no-modulation\n  outcome: not_reproduced\n  notebook: reproduce_fouke_2025.ipynb\n  output: claim:fig1d-dc-no-modulation\n  notes: By the paper's test (Tukey's HSD over the 18 species and stimulus groups) 3 of 36 DC\n    pairs differ, all static against a motion direction (backward left, backward right, forward\n    left; adjusted p 0.030 to 0.049). The DC static values come from 9 fish and include one at\n    106.5 mm/s and two at 0.0. Among the eight directions no DC pair differs (smallest adjusted\n    p 0.999), DC per-stimulus medians span 8.81 to 10.52 mm/s (ratio 1.19, ZF 2.03), and a\n    one-way ANOVA across the nine DC stimuli gives p = 0.479 (ZF p = 0.00082). With values above\n    100 mm/s left out, no DC pair differs. The same Tukey test finds no ZF pair over the 18\n    groups (smallest p 0.835).\n  deviations:\n  - The DC static block may hold different frames from the paper's, as the code's filter on DC\n    `vel` cannot be applied (DC static 10.52 against the code's printed 11.9 mm/s).\n- claim: fig1d-dc-faster-oblique\n  outcome: reproduced\n  notebook: reproduce_fouke_2025.ipynb\n  output: claim:fig1d-dc-faster-oblique\n  notes: Under reading (b), motion at 90 degrees or more, DC are significantly faster than ZF for\n    right (p = 0.0002) and backward right (p = 0.0047), 2 of 4; under reading (a), the\n    intercardinal directions, for 1 of 4 (backward right). Backward motion also differs\n    (p = 0.0002).\n  deviations:\n  - The legend's \"oblique\" can be read two ways; the claim is reproduced under one of them (b)\n    and not under the other (a).\n- claim: fig1g-follow-direction\n  outcome: partially_reproduced\n  notebook: reproduce_fouke_2025.ipynb\n  output: claim:fig1g-follow-direction\n  notes: ZF turn with the motion; the rightward minus leftward difference is positive in 23 of 25\n    fish (median 29.51 deg/s, one-sided Wilcoxon p = 9.8e-07). DC do not by this test; 7 of 12\n    positive, median 0.88 deg/s, p = 0.151, and the DC median for left motion is +0.25 deg/s,\n    the same sign as the paper's code printed (+0.3). DC turn right to right motion (8.67 deg/s).\n  deviations:\n  - The paper gives no test for following the direction; the per-fish rightward minus leftward\n    difference and its test were chosen here before the analysis.\n- claim: fig1h-zf-higher-angular-acceleration\n  outcome: not_reproduced\n  notebook: reproduce_fouke_2025.ipynb\n  output: claim:fig1h-zf-higher-angular-acceleration\n  notes: With angular acceleration as the Methods define it, DC are higher than ZF for all nine\n    stimuli (medians 143 to 191 against 55.4 to 66.4 deg/s2, Kruskal-Wallis p below 0.05/9 for\n    each), the reverse of the claim. Per-fish medians, and the files at 128 to 171 Hz alone\n    (ZF 84.9, DC 178.6 deg/s2, p = 6.3e-05), give the same. The quantity Fig1-S1.ipynb computes\n    gives ZF higher with p below 0.05/9 for 7 of 9 stimuli; it divides the heading change per\n    frame by the file's mean frame interval, which in DC files is a median 8.73 times the frame\n    interval (ZF 1.37), as DC files hold only trial frames.\n  deviations:\n  - Follows the Methods' definition (degrees per second squared) on heading resampled to 30 Hz;\n    the code's quantity, which disagrees with the Methods, is shown as a variant.\n  - Heading is taken from the cumulative sum of `f0_vtheta`, as the code does; in DC files it does\n    not match `f0_theta`.\n- claim: figs1e-dc-respond-less-monocular\n  outcome: reproduced\n  notebook: reproduce_fouke_2025.ipynb\n  output: claim:figs1e-dc-respond-less-monocular\n  notes: Species effect F = 23.3, p = 2.5e-06. DC turn less toward the stimulus than ZF for\n    medial stimuli (3.26 against 13.48 deg/s, p = 0.0003) and binocular ones (2.87 against 21.87,\n    p = 0.0002). For lateral stimuli DC are below ZF only nominally (-1.07 against -0.13 deg/s,\n    p = 0.96); neither species turns toward lateral motion. With the protocol file's assignment of\n    codes 9 and 11, the lateral medians change sign and DC are no longer below ZF there, which\n    would make the claim partially reproduced.\n  deviations:\n  - Codes 9 and 11 are assigned as the figure code has them; the stimulus software's conversion\n    has them the other way, and the data do not settle it.\n- claim: fig1c-continuous-vs-bouts\n  outcome: reproduced\n  notebook: reproduce_fouke_2025.ipynb\n  output: claim:fig1c-continuous-vs-bouts\n  notes: The median-to-mean ratio of instantaneous speed is 0.306 in ZF (25 fish, 0.244 to 0.580)\n    and 0.908 in DC (12 fish, 11 above 0.74, one at 0.140), Mann-Whitney p = 5.4e-05. It holds in\n    files at 128 to 171 Hz alone (0.298 against 0.898, p = 0.0028) and in forward trials alone.\n  deviations:\n  - The paper shows this with representative traces and a bout analysis whose bout files are not\n    in the dandiset; the measure was chosen here before the analysis.\n- claim: fig1cef-representative-values\n  outcome: blocked\n  blocked_by: metadata_insufficient\n  notes: The numbers come from single representative fish and trials. Fig1-S1.ipynb selects them\n    by the index of a data folder and a trial number (for example DC folder 29, trial 79), and the\n    dandiset gives no mapping from those folders to its subjects, nor the original file names.\n- claim: fig2d-shared-architecture\n  outcome: blocked\n  blocked_by: data_missing\n  notes: The two-photon imaging data are not in the dandiset, which holds only freely swimming\n    tracking. The GitLab repository the paper names for \"all behavioral and imaging data\" holds\n    notebooks only, and no other dandiset of this lab or paper was found on the archive.\n- claim: fig2g-dsi-similar\n  outcome: blocked\n  blocked_by: data_missing\n  notes: Imaging data not in the dandiset, nor found elsewhere (see fig2d-shared-architecture).\n- claim: fig2h-fewer-motion-responsive\n  outcome: blocked\n  blocked_by: data_missing\n  notes: Imaging data not in the dandiset, nor found elsewhere (see fig2d-shared-architecture).\n- claim: fig2k-more-monocular\n  outcome: blocked\n  blocked_by: data_missing\n  notes: Imaging data not in the dandiset, nor found elsewhere (see fig2d-shared-architecture).\n- claim: fig2l-bi-ratio\n  outcome: blocked\n  blocked_by: data_missing\n  notes: Imaging data not in the dandiset, nor found elsewhere (see fig2d-shared-architecture).\n- claim: fig3e-longer-swims\n  outcome: blocked\n  blocked_by: data_missing\n  notes: The head-fixed tail tracking recorded during imaging is not in the dandiset, nor in the\n    paper's GitLab repository.\n- claim: fig3cd-zf-turn-more\n  outcome: blocked\n  blocked_by: data_missing\n  notes: The head-fixed tail tracking is not in the dandiset, nor in the paper's GitLab repository.\n- claim: fig4f-longer-on-duration\n  outcome: blocked\n  blocked_by: data_missing\n  notes: Needs the imaging and the head-fixed tail tracking, neither of which is in the dandiset.\n- claim: fig4hi-vspn-lateralized\n  outcome: blocked\n  blocked_by: data_missing\n  notes: Needs the imaging, the tail tracking and the registration to the mapzebrain atlas, none\n    of which is in the dandiset.\nfindings:\n- kind: data_missing\n  statement: The dandiset holds only the freely swimming tracking of Figure 1 and Figure S1. The\n    two-photon imaging and the head-fixed tail tracking behind Figures 2 to 4 are not in it, and\n    the GitLab repository the paper names for all behavioural and imaging data holds analysis\n    notebooks only. Nine of the paper's main findings cannot be tested.\n- kind: metadata_insufficient\n  statement: The stimulus codes 0 to 20 have no names or description in the files or the\n    dandiset metadata. They can be named only from the paper's analysis notebook and the protocol\n    file of its stimulus software.\n- kind: code_mismatch\n  statement: The paper's analysis notebook labels code 9 as lateral right and 11 as lateral left,\n    while its conversion of the stimulus software's names gives the reverse (it carries a remap\n    that swaps them). The data do not settle which is right, as zebrafish barely turn to either.\n- kind: metadata_error\n  statement: Subject ids 0 to 11 are each used for one zebrafish and one Danionella cerebrum, so\n    subject_id does not identify an animal. The archive's summary counts 25 subjects and lists\n    only Danio rerio; the files hold 37 fish of two species.\n- kind: metadata_error\n  statement: f0_vtheta is stated in radians/s but holds the heading change per frame in radians,\n    and f0_vx and f0_vy are stated in pixels/s but are per frame. In most Danionella files the sum\n    of f0_vtheta over a trial does not match the change of f0_theta (median ratios 0.09 to 0.89).\n- kind: other\n  statement: 18 of 25 zebrafish files and 1 of 12 Danionella files are sampled at 32 to 35 Hz,\n    where the Methods state tracking at more than 150 Hz. Some measures differ with frame rate,\n    such as the zebrafish static speed (8.31 against 4.50 mm/s).\n- kind: metadata_insufficient\n  statement: No spatial scale is given; positions are in pixels. They are consistent with the 10\n    pixels per mm in the paper's code, except one Danionella file (sub-5) whose positions reach\n    1490 pixels against about 1120 in the others.\n- kind: other\n  statement: Zebrafish and Danionella files were exported differently. Zebrafish files keep\n    untracked frames and frames between trials; Danionella files hold only tracked trial frames\n    and add a `dist` series. The paper's code filters Danionella frames on a `vel` column that is\n    not in the files.\n- kind: code_mismatch\n  statement: The paper's code computes the angular acceleration of Figure 1H as the heading change\n    per frame divided by the file's mean frame interval, an angular velocity. In Danionella files\n    the mean interval includes the gaps between trials (a median 8.73 times the frame interval),\n    which scales their values down. With the Methods' definition Danionella have the higher\n    angular acceleration.\n- kind: code_mismatch\n  statement: Figure 1H and its legend state a Kruskal-Wallis test with Bonferroni correction; the\n    code runs two-sample Kolmogorov-Smirnov tests, and its loop selects the stimulus with a\n    variable left from an earlier loop, so the nine tests compare the same stimulus.\n- kind: code_mismatch\n  statement: The Figure 1D legend gives 26 zebrafish; the paper's code lists 25, its ANOVA\n    degrees of freedom fit 25, and the dandiset holds 25.\n- kind: selection_undocumented\n  statement: The dandiset holds the 25 zebrafish and 12 Danionella the code keeps after exclusion\n    (its comments give 28 and 40 recorded). The dandiset does not say that the excluded fish were\n    left out or why.\n"
}
```

```
File created successfully at: attempts/001453-fouke-2025-01.yaml (file state is current in your context — no need to Read it back)
```

**Agent**

Updating the monocular conclusion with the printed p-value, then the final check, run and handover.

**Agent calls Bash**

```bash
cd $TMPDIR && python3 - <<'EOF'
p='make_nb.py'; s=open(p).read()
a="(F = 23.3, p in the table above)"
assert a in s; s=s.replace(a,"(F = 23.3, p = 2.5e-06)")
open(p,'w').write(s)
EOF
explore/bin/python make_nb.py entries/001453-fouke-2025/reproduce_fouke_2025.ipynb
cd  && python3 - <<'EOF'
import yaml, re
for f in ['attempts/001453-fouke-2025-01.yaml','claims/001453/10.1016-j.cub.2025.04.027.yaml','entries/001453-fouke-2025/entry.yaml']:
    yaml.safe_load(open(f))
    for i,l in enumerate(open(f),1):
        body = re.sub(r'^\s*(- )?[a-z_]+: ', '', l.rstrip('\n'))
        if ': ' in body and not l.strip().startswith('#'): print(f, i, l.rstrip())
    t=open(f).read()
    for w in ['—',' rather','**']:
        if w in t: print(f,'contains',w)
EOF
grep -n "—\| rather" entries/001453-fouke-2025/*.md entries/001453-fouke-2025/omr.py; grep -c "—\| rather" entries/001453-fouke-2025/reproduce_fouke_2025.ipynb
```

```
cells 56
0
```

**Agent calls Bash**

```bash
python tools/entry.py all entries/001453-fouke-2025 2>&1 | tail -5 && python tools/entry.py handover entries/001453-fouke-2025 && ls executed/001453-fouke-2025/handover && python3 -c "
import nbformat
nb=nbformat.read('executed/001453-fouke-2025/handover/reproduce_fouke_2025.ipynb',as_version=4)
print(sum('**Result' in c.source for c in nb.cells), any('## Summary' in c.source for c in nb.cells), len(nb.cells))
nb=nbformat.read('executed/001453-fouke-2025/reproduce_fouke_2025.ipynb',as_version=4)
print([o.get('ename') for c in nb.cells if c.cell_type=='code' for o in c.outputs if o.output_type=='error'])
"; git status --short
```

```
Installed kernelspec registry-001453-fouke-2025 in executed/001453-fouke-2025/.venv/share/jupyter/kernels/registry-001453-fouke-2025
0 error(s)
pass  reproduce_fouke_2025.ipynb  (225 s)
wrote executed/001453-fouke-2025/handover
10.1016-j.cub.2025.04.027.yaml
omr.py
reproduce_fouke_2025.ipynb
0 False 45
[]
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
?? attempts/001453-fouke-2025-01.yaml
[... 3 more lines not kept]
```

**Agent calls Bash**

```bash
ls -la .bash_profile .bashrc .gitconfig .mcp.json .profile .ripgreprc .zprofile .zshrc .idea .vscode scripts 2>&1 | head -20; cat .gitignore 2>/dev/null | head
```

```
crw-rw-rw- 1 nobody nogroup 1, 3 Oct 14 13:46 .bash_profile
crw-rw-rw- 1 nobody nogroup 1, 3 Oct 14 13:46 .bashrc
crw-rw-rw- 1 nobody nogroup 1, 3 Oct 14 13:46 .gitconfig
crw-rw-rw- 1 nobody nogroup 1, 3 Oct 14 13:46 .idea
crw-rw-rw- 1 nobody nogroup 1, 3 Oct 14 13:46 .mcp.json
crw-rw-rw- 1 nobody nogroup 1, 3 Oct 14 13:46 .profile
crw-rw-rw- 1 nobody nogroup 1, 3 Oct 14 13:46 .ripgreprc
crw-rw-rw- 1 nobody nogroup 1, 3 Oct 14 13:46 .vscode
crw-rw-rw- 1 nobody nogroup 1, 3 Oct 14 13:46 .zprofile
crw-rw-rw- 1 nobody nogroup 1, 3 Oct 14 13:46 .zshrc
crw-rw-rw- 1 nobody nogroup 1, 3 Oct 14 13:46 scripts
__pycache__/
*.pyc
.ipynb_checkpoints/
.venv/
.DS_Store
executed/
site/
paper/
```

**Agent**

I did steps 1 to 6 of the protocol for dandiset 001453. The entry passes `entry.py all` with 0 errors and runs in 225 s, and the handover package is built. Of 20 claims, 6 were reproduced, 1 partially and 2 not, with 1 more reproduced (the link) and 10 blocked. Nothing was committed or pushed.

**Paper text:** I used the full text of the accepted author manuscript in PubMed Central (PMC12218792), saved under `paper/`. The published version itself is not open access.

**Version:** pinned 0.250518.1950, the only published version. The paper cites no DANDI version. The draft has the same 37 files and only adds metadata, as the notebook header explains.

**Outside inputs:** the stimulus codes have no names in the dandiset. The names come from the paper's analysis notebook on GitLab (commit 33a5c29) and the protocol file of its stimulus software, pandastim (commit 7d9d161). Claims that rely on them are marked "with inputs" and depend on a link claim.

### 1. Outcomes

| Claim | Data | Outcome |
|---|---|---|
| stimulus-code-link | with inputs | reproduced (17 of 18 speed medians within 10% of the values the paper's code printed) |
| fig1d-dc-faster-all-codes | dandiset | reproduced (94.0 vs 55.2 px/s, p = 6e-18) |
| fig1d-median-velocity | with inputs | reproduced (9.87 and 6.41 vs 9.8 and 6.4 mm/s) |
| fig1d-zf-forward-faster-than-static | with inputs | reproduced (4.84 and 8.78 vs 5.0 and 8.8) |
| fig1d-dc-no-modulation | with inputs | not reproduced (3 DC pairs differ in the Tukey test, all involving "static") |
| fig1d-dc-faster-oblique | with inputs | reproduced under one of the two readings of "oblique" |
| fig1g-follow-direction | with inputs | partially reproduced (holds for zebrafish, p = 1e-6; not for Danionella, p = 0.15) |
| fig1h-zf-higher-angular-acceleration | with inputs | not reproduced (by the Methods' definition Danionella are higher for all 9 stimuli) |
| figs1e-dc-respond-less-monocular | with inputs | reproduced (the lateral part only nominally) |
| fig1c-continuous-vs-bouts | dandiset | reproduced (0.31 vs 0.91, p = 5e-5) |
| fig1cef-representative-values | dandiset | blocked: metadata_insufficient |
| 9 claims on imaging and head-fixed tail tracking (Figures 2 to 4) | dandiset | blocked: data_missing |

### 2. What was found about the dandiset

- **Missing data:** it holds only the freely swimming tracking behind Figure 1 and Figure S1. The paper's GitLab "data" repository holds notebooks only.
- **Fish count:** 25 zebrafish (the paper says 26; the paper's code and the dandiset both have 25) and 12 Danionella.
- **Subject IDs:** IDs 0 to 11 are each reused for one fish of each species. The archive summary says 25 subjects and lists only zebrafish.
- **Stimulus codes:** codes 0 to 20 have no names. The paper's code and the stimulus software swap codes 9 and 11 (lateral right and left).
- **Wrong units:** `f0_vtheta` is per frame, not radians/s, and `f0_vx`/`f0_vy` are per frame, not pixels/s.
- **Frame rates:** 18 of 25 zebrafish files and 1 Danionella file are sampled at 32 to 35 Hz. The Methods say above 150 Hz.
- **Spatial scale:** none is given. Positions fit the code's 10 px per mm, except one Danionella file (sub-5) whose positions reach 1490 px.
- **Export differences:** the two species were exported differently. Danionella files hold only trial frames plus an extra `dist` series.
- **Code bug behind Figure 1H:** the code divides each frame's heading change by the file's mean frame interval. In Danionella files that interval includes the gaps between trials (8.7 times the frame interval), so only this quantity shows zebrafish higher.
- **Code test mismatch:** the code runs a Kolmogorov-Smirnov test where the paper states Kruskal-Wallis, and its loop tests the same stimulus nine times.
- **Selection:** the dandiset holds only the fish kept after exclusion, without saying so.
- **No duplicate recordings.**

### 3. Where the protocol was unclear, wrong or missing something

1. **Labels as outside data.** The code-to-name table is a label, not data, yet without it nearly every claim needs outside input. I treated it as an outside input, marked 7 claims "with inputs", and made a link claim.
2. **No identifier for a link claim.** The protocol expects records to be matched by an identifier, but fish can't be matched here. I matched stimulus codes by integer and compared the per-stimulus medians with the paper's printed code outputs.
3. **Clock check doesn't fit.** Labels sit on the same timestamps as positions, so they share a clock by construction. I used a turning contrast over time with true and shifted labels. It supports zebrafish; for Danionella it could not establish the timing, and I said so.
4. **Several conflicting sources.** The Methods, the analysis code and the stimulus software disagree with each other (Figure 1H quantity, codes 9 and 11, the test used). The protocol's rule covers only Methods versus code. I followed the Methods for the main result where it is explicit and the figure code otherwise, and showed the others as variants.
5. **Absence claim that mixes conditions.** The paper's test for "DC lack modulation" includes the static condition, which is not a direction. I judged it as written (not reproduced) and showed directions-only as a variant, where no DC pair differs.
6. **Representative-trial numbers.** The protocol has no category for these. I blocked them as metadata_insufficient.
7. **Choosing the `measured` value.** When every reading matches, the protocol doesn't say which to record. I recorded reading (b) and listed all four in the notes.
8. **Stale example entry.** The example entry is from protocol pilot-0 (no `data`, `inputs` or provenance fields), so I took field names from `schemas/` instead.

### 4. Runtime and failures

- **Runtime:** the notebook takes 225 s, about 190 s of it streaming the files. The whole session took about 1.5 hours.
- **Failures:** Europe PMC returned HTTP 500 and the NCBI BioC API returned 429, so I fetched the paper through NCBI efetch.
- **Odd files in `git status`:** it lists `.bashrc`, `.mcp.json`, `scripts` and similar at the repo root. These are `/dev/null` placeholders the sandbox mounts, not files I created; the workflow should not commit them.

## End of run

60 turns, 37 minutes, result: success.
