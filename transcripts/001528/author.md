# 001528 · author · run 39166587612

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cat docs/protocol.md; ls; ls entries claims attempts tools
```

```
# Protocol for an attempt

Version: `pilot-7`. Record this version in the attempt's provenance.

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

[... 515 more lines not kept]
```

**Agent calls Bash**

```bash
cat README.md | head -150; echo ----; cat docs/design.md
```

```
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

An outcome says what one attempt could recover from the data in a dandiset,
with the methods available to it. **A "not reproduced" or "partially
reproduced" outcome is not a finding that the paper is wrong.** It can come
[... 380 more lines not kept]
```

**Agent calls Bash**

```bash
ls -la entries/001453-fouke-2025 claims/001453; cat entries/001453-fouke-2025/entry.yaml entries/001453-fouke-2025/requirements.in; cat attempts/001453-fouke-2025-01.yaml; cat claims/001453/*.yaml
```

```
<persisted-output>
Output too large (48.6KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/210b92be-775a-4be5-a155-48ed9ac6192b/tool-results/bavbblg2x.txt

Preview (first 2KB):
claims/001453:
total 24
drwxr-xr-x  2 runner runner  4096 Oct 18 21:09 .
drwxr-xr-x 48 runner runner  4096 Oct 18 21:09 ..
-rw-r--r--  1 runner runner 12471 Oct 18 21:09 10.1016-j.cub.2025.04.027.yaml

entries/001453-fouke-2025:
total 124
drwxr-xr-x  2 runner runner  4096 Oct 18 21:09 .
drwxr-xr-x 48 runner runner  4096 Oct 18 21:09 ..
-rw-r--r--  1 runner runner  2158 Oct 18 21:09 README.md
-rw-r--r--  1 runner runner   914 Oct 18 21:09 entry.yaml
-rw-r--r--  1 runner runner 16218 Oct 18 21:09 omr.py
-rw-r--r--  1 runner runner 79403 Oct 18 21:09 reproduce_fouke_2025.ipynb
-rw-r--r--  1 runner runner    61 Oct 18 21:09 requirements.in
-rw-r--r--  1 runner runner  5989 Oct 18 21:09 requirements.lock.txt
[... 44 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/210b92be-775a-4be5-a155-48ed9ac6192b/tool-results/bavbblg2x.txt"
}
```

```
1	claims/001453:
2	total 24
3	drwxr-xr-x  2 runner runner  4096 Oct 18 21:09 .
4	drwxr-xr-x 48 runner runner  4096 Oct 18 21:09 ..
5	-rw-r--r--  1 runner runner 12471 Oct 18 21:09 10.1016-j.cub.2025.04.027.yaml
6	
7	entries/001453-fouke-2025:
8	total 124
9	drwxr-xr-x  2 runner runner  4096 Oct 18 21:09 .
10	drwxr-xr-x 48 runner runner  4096 Oct 18 21:09 ..
11	-rw-r--r--  1 runner runner  2158 Oct 18 21:09 README.md
12	-rw-r--r--  1 runner runner   914 Oct 18 21:09 entry.yaml
13	-rw-r--r--  1 runner runner 16218 Oct 18 21:09 omr.py
14	-rw-r--r--  1 runner runner 79403 Oct 18 21:09 reproduce_fouke_2025.ipynb
15	-rw-r--r--  1 runner runner    61 Oct 18 21:09 requirements.in
16	-rw-r--r--  1 runner runner  5989 Oct 18 21:09 requirements.lock.txt
17	schema_version: 1
18	name: 001453-fouke-2025
19	type: reproduction
20	title: Optomotor swimming of zebrafish and Danionella cerebrum (Fouke et al. 2025)
[... 849 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/001453-fouke-2025; cat README.md; python -c "
import json;nb=json.load(open('reproduce_fouke_2025.ipynb'))
for c in nb['cells'][:8]+nb['cells'][-3:]:
    print('====',c['cell_type'],c['metadata']); print(''.join(c['source'])[:2500])
print(len(nb['cells']))
print(nb['metadata'])
"; head -60 omr.py
```

```
# Fouke, He, Loring & Naumann (2025) from dandiset 001453

Tests the findings of [Fouke et al. (2025)](https://doi.org/10.1016/j.cub.2025.04.027) that can be
tested on [DANDI:001453](https://dandiarchive.org/dandiset/001453/0.250518.1950), which holds the
freely swimming tracking of 25 zebrafish and 12 *Danionella cerebrum* larvae (Figure 1 and Figure
S1). The imaging and head-fixed tail tracking of Figures 2 to 4 are not in it.

| Claim | Outcome |
|---|---|
| The stimulus codes can be linked to the paper's stimuli through its code | Reproduced |
| DC swim faster than ZF, over all stimulus codes | Reproduced |
| Median speed over whole-field stimuli, DC 9.8 and ZF 6.4 mm/s | Reproduced |
| ZF are faster to forward motion than to a static grating (8.8 against 5.0 mm/s) | Reproduced |
| DC do not modulate speed with stimulus direction | Not reproduced |
| DC are faster than ZF for oblique stimuli | Reproduced |
| Both species turn in the direction of motion | Partially reproduced |
| ZF have higher angular acceleration than DC | Not reproduced |
| DC turn less than ZF to monocular stimuli | Reproduced |
| ZF swim in bouts, DC continuously | Reproduced |
| Values from representative trials (Figure 1C, E, F) | Blocked: metadata insufficient |
[... 302 more lines not kept]
```

**Agent calls Bash**

```bash
cd  curl -s https://api.dandiarchive.org/api/dandisets/001528/ | python -m json.tool; curl -s "https://api.dandiarchive.org/api/dandisets/001528/versions/" | python -m json.tool
```

Result: the fetched text is not kept.

**Agent**

No published version of 001528 exists (draft only, 290 assets, 68 GB). Checking how the tooling handles a draft.

**Agent calls Bash**

```bash
grep -n -i "draft\|version" tools/entry.py | head -60; ls schemas; grep -n -i draft schemas/* | head
```

```
10:requirements.lock.txt with every version pinned.
54:from jsonschema import Draft202012Validator
57:PYTHON_VERSION = "3.13"
75:def schema(name: str) -> Draft202012Validator:
76:    return Draft202012Validator(json.loads((ROOT / "schemas" / f"{name}.schema.json").read_text()))
110:    nb = nbformat.read(notebook_path, as_version=4)
152:    versions = {d: v for d, _, v in used}
156:        for d, v in versions.items():
158:                report.error(rel / "entry.yaml", f"pin the version of dandiset {d}, as dandi:{d}/<version>")
163:        nb = nbformat.read(path, as_version=4)
172:            version = versions[dandiset]
173:            if version and version not in code and version not in helper_code:
174:                report.error(rel / name, f"neither the notebook nor a helper names version {version} "
203:        pinned = versions.get(attempt.get("dandiset"))
204:        # The entry streams the version of its latest attempt; earlier attempts keep the version they used.
205:        if pinned and path == mine[-1] and attempt.get("dandiset_version") != pinned:
206:            report.error(where, f"dandiset_version {attempt.get('dandiset_version')!r} differs from "
254:                nb = nbformat.read(entry_dir / notebook, as_version=4)
275:    r = subprocess.run(["uv", "pip", "compile", "--quiet", "--python-version", PYTHON_VERSION,
290:    for cmd in (["uv", "venv", "--quiet", "--clear", "--python", PYTHON_VERSION, str(venv)],
[... 12 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 100,215p tools/entry.py; cat schemas/attempt.schema.json | head -80
```

```
if isinstance(value, dict):
        return {k: _plain(v) for k, v in value.items()}
    if isinstance(value, list):
        return [_plain(v) for v in value]
    if hasattr(value, "isoformat"):
        return value.isoformat()
    return value


def code_of(notebook_path: Path) -> str:
    nb = nbformat.read(notebook_path, as_version=4)
    return "\n".join(c.source for c in nb.cells if c.cell_type == "code")


# --- check --------------------------------------------------------------------

def check(entry_dir: Path) -> Report:
    report = Report()
    rel = entry_dir.relative_to(ROOT)
    entry = validate(report, entry_dir / "entry.yaml", "entry")
[... 176 more lines not kept]
```

**Agent calls Bash**

```bash
mkdir -p paper $TMPDIR/d; curl -s https://api.dandiarchive.org/api/dandisets/001528/versions/draft/ > $TMPDIR/d/meta.json; python -c "
import json;m=json.load(open('$TMPDIR/d/meta.json'))
for k in ['name','description','citation','keywords','relatedResource','assetsSummary','contributor','dateModified','wasGeneratedBy','protocol','studyTarget','ethicsApproval']:
    print('##',k); print(json.dumps(m.get(k),indent=1)[:4000])
"
```

Result: the fetched text is not kept.

**Agent**

Now the asset list and the paper.

**Agent calls Bash**

```bash
cd $TMPDIR/d; python - <<'EOF'
import json,urllib.request
url="https://api.dandiarchive.org/api/dandisets/001528/versions/draft/assets/?page_size=1000"
out=[]
while url:
    r=json.load(urllib.request.urlopen(url)); out+=r['results']; url=r['next']
json.dump(out,open('assets.json','w'))
print(len(out))
import collections
for a in sorted(out,key=lambda a:a['path'])[:400]:
    print(a['path'], round(a['size']/1e6,1), a['modified'][:19])
EOF
```

```
290
sub-B7514/sub-B7514_ses-varying-durations.nwb 295.9 2025-11-04T08:59:58
sub-B7514/sub-B7514_ses-varying-frequencies.nwb 1218.5 2025-11-04T09:00:25
sub-B7515/sub-B7515_ses-varying-durations.nwb 292.1 2025-11-04T08:59:42
sub-B7515/sub-B7515_ses-varying-frequencies.nwb 1210.4 2025-11-04T09:00:33
sub-B7532/sub-B7532_ses-varying-durations.nwb 299.3 2025-11-04T08:59:04
sub-B7532/sub-B7532_ses-varying-frequencies.nwb 1193.5 2025-11-04T09:00:31
sub-B7616/sub-B7616_ses-varying-durations.nwb 310.2 2025-11-04T09:00:07
sub-B7616/sub-B7616_ses-varying-frequencies.nwb 1185.5 2025-11-04T09:01:04
sub-B8364/sub-B8364_ses-varying-durations.nwb 289.8 2025-11-12T17:03:57
sub-B8364/sub-B8364_ses-varying-frequencies.nwb 1253.0 2025-11-12T17:06:26
sub-B8369/sub-B8369_ses-varying-durations.nwb 289.8 2025-11-12T17:04:12
sub-B8369/sub-B8369_ses-varying-frequencies.nwb 1200.5 2025-11-12T17:06:02
sub-B8370/sub-B8370_ses-varying-durations.nwb 289.4 2025-11-12T17:03:39
sub-B8370/sub-B8370_ses-varying-frequencies.nwb 1233.3 2025-11-12T17:05:53
sub-B8427/sub-B8427_ses-varying-durations.nwb 296.7 2025-11-12T17:04:57
sub-B8427/sub-B8427_ses-varying-frequencies.nwb 1309.6 2025-11-12T17:06:08
sub-B8429/sub-B8429_ses-varying-durations.nwb 282.7 2025-11-12T17:05:15
sub-B8429/sub-B8429_ses-varying-frequencies.nwb 1330.1 2025-11-12T17:06:44
sub-B8569/sub-B8569_ses-varying-durations.nwb 297.3 2025-11-04T09:00:31
[... 272 more lines not kept]
```

**Agent**

Now the paper. Trying Europe PMC for the preprint's full text.

**Agent calls Bash**

```bash
cd paper; curl -s "https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.1101/2025.06.03.657460&format=json&resultType=core" | python -c "
import json,sys;r=json.load(sys.stdin)
for x in r['resultList']['result']: print({k:x.get(k) for k in ['id','source','pmcid','title','hasTextMinedTerms','inEPMC','isOpenAccess','fullTextUrlList','license','pubYear']})
"; curl -s -o biorxiv.json "https://api.biorxiv.org/details/biorxiv/10.1101/2025.06.03.657460"; cat biorxiv.json | head -c 3000
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd paper; curl -sL -A "Mozilla/5.0" -o paper.xml "https://www.biorxiv.org/content/early/2025/06/07/2025.06.03.657460.source.xml"; ls -la; head -c 500 paper.xml; curl -sL -A "Mozilla/5.0" -o paper.pdf "https://www.biorxiv.org/content/biorxiv/early/2025/06/07/2025.06.03.657460.full.pdf"; file paper.pdf; ls -la
```

Result: the fetched text is not kept.

**Agent**

Full text available (CC BY). Converting to plain text.

**Agent calls Bash**

```bash
cd paper; python - <<'EOF'
import re
from xml.etree import ElementTree as ET
t=ET.parse('paper.xml'); r=t.getroot()
def txt(e): return re.sub(r'\s+',' ',''.join(e.itertext())).strip()
out=[]
body=r.find('.//body')
def walk(e,depth=0):
    for c in e:
        tag=c.tag.split('}')[-1]
        if tag=='sec':
            ti=c.find('title'); out.append('\n'+'#'*(depth+2)+' '+(txt(ti) if ti is not None else '')); walk(c,depth+1)
        elif tag=='p': out.append(txt(c))
        elif tag=='fig':
            out.append('[FIG] '+txt(c))
for a in r.iter():
    if a.tag.split('}')[-1]=='abstract': out.append('# Abstract\n'+txt(a))
walk(body)
back=r.find('.//back')
if back is not None: walk(back)
# figures may be floats
for f in r.iter():
    if f.tag.split('}')[-1]=='fig' and txt(f) not in '\n'.join(out): out.append('[FIG] '+txt(f))
open('paper.txt','w').write('\n'.join(out))
print(len('\n'.join(out)))
EOF
wc -w paper.txt
```

```
54015
8249 paper.txt
```

**Agent calls Read**

```json
{
 "file_path": "paper/paper.txt"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd paper; grep -o -i '[^.]*\(dandi\|github\|availab\|zenodo\|code \)[^.]*\.' paper.xml | head -20; pdftotext -layout paper.pdf paper_pdf.txt 2>&1 | head -2; grep -n -i "dandi\|github\|availab\|zenodo\|Table S" paper_pdf.txt | head -30
```

```
0/" hwp:id="license-1"><p hwp:id="p-1">This pre-print is available under a Creative Commons License (Attribution 4.
 Additional work that aims to assess the effects of manipulating STN or PPN subtypes or applying technologies for higher resolution temporo-spatial patterning of stimulation may yield results that support or alter present conclusions that are based on currently available data.
</p></sec><sec id="s6f" hwp:id="sec-17"><title hwp:id="title-26">Fiber photometry signal extraction and analysis</title><p hwp:id="p-49">Analysis of recorded signals was performed using custom MATLAB code (Mathworks, RRID: with the signal processing, statstics, and curve fitting toolboxes).
/bin/bash: line 1: pdftotext: command not found
grep: paper_pdf.txt: No such file or directory
```

**Agent**

No data or code statement in the preprint. The dandiset links the conversion repo and an example notebook; cloning both to read.

**Agent calls Bash**

```bash
cd $TMPDIR && git clone -q https://github.com/catalystneuro/hnasko-lab-to-nwb && cd hnasko-lab-to-nwb && git log -1 --format='%H %cd' && find . -path ./.git -prune -o -type f -print | head -80; cd $TMPDIR && git clone -q --depth 1 --filter=blob:none --sparse https://github.com/dandi/example-notebooks && cd example-notebooks && git sparse-checkout set 001528 && git log -1 --format='%H %cd' && find 001528 -type f
```

```
deaefa7b1776a5ffb98fd50c5ff4d7b899bdaf59 Tue Sep 29 10:49:49 2026 +0200
./pyproject.toml
./.github/workflows/test-install.yml
./.github/workflows/auto-publish.yml
./.github/workflows/add-to-dashboard.yml
./LICENSE
./make_env.yml
./.gitignore
./.pre-commit-config.yaml
./src/hnasko_lab_to_nwb/another_conversion/__init__.py
./src/hnasko_lab_to_nwb/embargo_2025/metadata/general_metadata.yaml
./src/hnasko_lab_to_nwb/embargo_2025/metadata/shock_stimulus_metadata.yaml
./src/hnasko_lab_to_nwb/embargo_2025/convert_session.py
./src/hnasko_lab_to_nwb/embargo_2025/utils/add_shock_stimuli.py
./src/hnasko_lab_to_nwb/embargo_2025/utils/__init__.py
./src/hnasko_lab_to_nwb/embargo_2025/tutorials/embrago_2025.ipynb
./src/hnasko_lab_to_nwb/embargo_2025/nwbconverter.py
./src/hnasko_lab_to_nwb/embargo_2025/interfaces/demodulated_tdt_interface.py
./src/hnasko_lab_to_nwb/embargo_2025/interfaces/__init__.py
./src/hnasko_lab_to_nwb/embargo_2025/notes.md
[... 34 more lines not kept]
```

**Agent**

The conversion repo has a `reproduced_analysis` folder. Reading it and the notes.

**Agent calls Bash**

```bash
cd $TMPDIR/hnasko-lab-to-nwb/src/hnasko_lab_to_nwb/lotfi_2025; cat notes.md reproduced_analysis/analysis_notes.md; cat metadata/Cell_type_recordings_Anxa1_metadata.yaml
```

```
<persisted-output>
Output too large (40.6KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/210b92be-775a-4be5-a155-48ed9ac6192b/tool-results/b2b6dcbwi.txt

Preview (first 2KB):
# Notes concerning the lotfi_2025 conversion

Mice were freely moving on a plastic tub.
Simultaneous passive optogenetic stimulations and fiber photometry recordings were conducted during the first two days.
Briefly, excitatory inputs from either the STN or PPN to SN were stimulated and the activity of SN GABAergic neurons were recorded.
Then mice underwent uncued electrical shocks and were recorded using fiber photometry.

Reference paper:  ["Parkinson's Disease-vulnerable and -resilient dopamine neurons display opposite responses to excitatory input"](https://www.biorxiv.org/content/10.1101/2025.06.03.657460v1)


## Sessions description

Each subject --> 3 experimental days:

### Day 1: Varying duration
During day 1, mice were placed in a plastic tub and were recorded for 3.5 minutes.
[... 20 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/210b92be-775a-4be5-a155-48ed9ac6192b/tool-results/b2b6dcbwi.txt"
}
```

```
1	# Notes concerning the lotfi_2025 conversion
2	
3	Mice were freely moving on a plastic tub.
4	Simultaneous passive optogenetic stimulations and fiber photometry recordings were conducted during the first two days.
5	Briefly, excitatory inputs from either the STN or PPN to SN were stimulated and the activity of SN GABAergic neurons were recorded.
6	Then mice underwent uncued electrical shocks and were recorded using fiber photometry.
7	
8	Reference paper:  ["Parkinson's Disease-vulnerable and -resilient dopamine neurons display opposite responses to excitatory input"](https://www.biorxiv.org/content/10.1101/2025.06.03.657460v1)
9	
10	
11	## Sessions description
12	
13	Each subject --> 3 experimental days:
14	
15	### Day 1: Varying duration
16	During day 1, mice were placed in a plastic tub and were recorded for 3.5 minutes.
17	The mice received a 40 Hz stimulation at various durations (i.e. 250ms, 1s and 4s) 5 times for each duration
18	with an inter-stimulus interval (ISI) of 10s.
19	
20	### Day 2: Varying frequencies
[... 964 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/hnasko-lab-to-nwb/src/hnasko_lab_to_nwb/lotfi_2025; wc -l reproduced_analysis/* convert_all_sessions.py convert_session.py interfaces/*; cat reproduced_analysis/analysis_functions.py reproduced_analysis/stream_from_dandi.py
```

```
19 reproduced_analysis/__init__.py
    567 reproduced_analysis/analysis_functions.py
    388 reproduced_analysis/analysis_notes.md
   1555 reproduced_analysis/reproduce_analysis_pipeline.ipynb
     37 reproduced_analysis/stream_from_dandi.py
    178 convert_all_sessions.py
    608 convert_session.py
     17 interfaces/__init__.py
    379 interfaces/concatenated_tdt_fp_interface.py
    728 interfaces/processed_fp_interface.py
    450 interfaces/tdt_optogenetic_stimulus_interface.py
   4926 total
"""
Modular functions for reproducing Lotfi 2025 fiber photometry analysis.

This module provides functions to process fiber photometry data from NWB files,
following the analysis pipeline from the original MATLAB scripts.

Author: Catalyst Neuro
Date: 2025
[... 597 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/hnasko-lab-to-nwb/src/hnasko_lab_to_nwb/lotfi_2025; cat convert_all_sessions.py; python -c "
import json;nb=json.load(open('reproduced_analysis/reproduce_analysis_pipeline.ipynb'))
for c in nb['cells']:
    print('====',c['cell_type']); print(''.join(c['source'])[:1500])
    for o in c.get('outputs',[]):
        if 'text' in o: print('OUT:',''.join(o['text'])[:800])
" | head -300
```

```
"""Script to convert all Water Maze sessions to NWB format, following the structure of auditory_fear_conditioning/convert_all_sessions.py."""

import traceback
from pathlib import Path
from pprint import pformat
from typing import Union
from tqdm import tqdm
import natsort
import pandas as pd
import numpy as np

from hnasko_lab_to_nwb.lotfi_2025.convert_session import (
    varying_durations_session_to_nwb,
    varying_frequencies_session_to_nwb,
)


def dataset_to_nwb(
    *,
    data_dir_path: Union[str, Path],
[... 464 more lines not kept]
```

**Agent**

Now opening an NWB file to list its contents. Setting up a scratch environment first.

**Agent calls Bash**

```bash
cd $TMPDIR && uv venv -q --python 3.13 scratch && . scratch/bin/activate && uv pip install -q h5py remfile dandi pynwb ndx-fiber-photometry ndx-ophys-devices numpy scipy pandas statsmodels matplotlib 2>&1 | tail -3; python -c "import pynwb,h5py,remfile;print(pynwb.__version__)"
```

**Agent calls Bash**

```bash
sed -n 1,200p $TMPDIR/example-notebooks/001528/HnaskoLab/Lotfi_2025/README.md; python -c "
import json;nb=json.load(open('$TMPDIR/example-notebooks/001528/HnaskoLab/Lotfi_2025/001528_demo.ipynb'))
for c in nb['cells']:
    print('====',c['cell_type']); print(''.join(c['source'])[:1200])
" | head -250
```

```
4.2.0
Shell cwd was reset to
```

```
# **Fiber photometry of SNc/SNr dopamine and GABA neuron responses to optogenetic STN and PPN stimulation in Parkinson's disease**

This tutorial shows how to access and process data from [DANDI:001528](https://dandiarchive.org/dandiset/001528/draft) for the study detailed in [*"Parkinson's Disease-vulnerable and -resilient dopamine neurons display opposite responses to excitatory input"*](https://www.biorxiv.org/content/10.1101/2025.06.03.657460v1).

## Running the Notebook

The notebook streams data directly from the DANDI Archive, so nothing needs to be downloaded in advance.

- **Google Colab**: open the notebook with the "Open in Colab" badge at the top and run the install cell, which sets up the exact tested package versions.
- **Locally**: in a Python 3.12 environment, install the direct dependencies with `pip install -r requirements.in` and start Jupyter with `jupyter lab 001528_demo.ipynb`. Running the pinned install cell at the top of the notebook instead reproduces the exact tested versions.
==== markdown
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/dandi/example-notebooks/blob/master/001528/HnaskoLab/Lotfi_2025/001528_demo.ipynb)
==== markdown
## Installing requirements

The cell below installs every Python package needed to run this notebook, at fully pinned versions, using [`uv`](https://github.com/astral-sh/uv) for fast resolution. In Colab the cell is collapsed by default — click the ▶ button to run it.
==== code
#@title Installing requirements (click ▶ to run) { display-mode: "form" }
# Colab provides Python 3.13. We install with `uv --system` because Colab's
# kernel runs outside a virtualenv. All versions (direct + transitive) are
[... 240 more lines not kept]
```

**Agent**

Now dumping the full structure of one small file with h5py over the stream.

**Agent calls Bash**

```bash
cd $TMPDIR && . scratch/bin/activate && cat > dump.py <<'EOF'
import h5py, remfile, sys, json
from dandi.dandiapi import DandiAPIClient
path = sys.argv[1]
c = DandiAPIClient()
ds = c.get_dandiset("001528", "draft")
a = ds.get_asset_by_path(path)
url = a.get_content_url(follow_redirects=1, strip_query=True)
f = h5py.File(remfile.File(url), "r")
def show(name, obj):
    if isinstance(obj, h5py.Dataset):
        v = ""
        if obj.size < 40 and obj.dtype.kind in "OSUifb":
            try: v = obj[()]
            except Exception: pass
        print(f"D {name} {obj.shape} {obj.dtype} {dict((k, obj.attrs[k]) for k in obj.attrs if k in ('unit','conversion','rate','offset','resolution','description','starting_time'))} {v}")
    else:
        at = {k: obj.attrs[k] for k in obj.attrs if k in ('neurodata_type','description','rate','unit')}
        print(f"G {name} {at}")
f.visititems(show)
EOF
python dump.py sub-C4561/sub-C4561_ses-varying-durations_image.nwb 2>&1 | grep -v "^G specifications\|^D specifications" | head -300
```

```
G acquisition {}
G acquisition/BehavioralVideo {'description': "Video recording of the mouse's behavior. Recorded using a camera mounted on the ceiling above the chambers.\n", 'neurodata_type': 'ImageSeries'}
D acquisition/BehavioralVideo/data (0, 0, 0) uint8 {'conversion': np.float64(1.0), 'offset': np.float64(0.0), 'resolution': np.float64(-1.0), 'unit': 'Frames'} 
D acquisition/BehavioralVideo/external_file (1,) object {} [b'sub-C4561_ses-varying-durations_image\\5edc8957-c811-4c13-bc52-491745c3f527_external_file_0.mp4']
D acquisition/BehavioralVideo/format () object {} b'external'
D acquisition/BehavioralVideo/timestamps (2632,) float64 {'unit': 'seconds'} 
G acquisition/raw_signal_SNr {'description': 'The raw modulated fluorescence signal from GCaMP6f calcium indicator in SNr GABAergic neurons, excited at 465nm and 405nm, respectively.', 'neurodata_type': 'FiberPhotometryResponseSeries'}
D acquisition/raw_signal_SNr/data (1580544,) float32 {'conversion': np.float64(1.0), 'offset': np.float64(0.0), 'resolution': np.float64(-1.0), 'unit': 'a.u.'} 
D acquisition/raw_signal_SNr/fiber_photometry_table_region (1,) int64 {'description': 'The region of the FiberPhotometryTable corresponding to the raw signal.'} [0]
D acquisition/raw_signal_SNr/starting_time () float64 {'rate': np.float64(6103.515625), 'unit': 'seconds'} 0.0
G analysis {}
D file_create_date (1,) object {} [b'2025-11-03T22:06:02.915512+01:00']
G general {}
G general/devices {}
G general/devices/BehavioralCamera {'description': 'Camera mounted on ceiling above chambers for behavioral recording', 'neurodata_type': 'Device'}
G general/devices/dichroic_mirror {'description': 'dichroic mirror for GCaMP6f fluorescence signal.', 'neurodata_type': 'DichroicMirror'}
G general/devices/emission_filter {'description': 'emission filter for GCaMP6f fluorescence signal.', 'neurodata_type': 'BandOpticalFilter'}
G general/devices/excitation_filter {'description': 'excitation filter for GCaMP6f fluorescence signal.', 'neu
[... 116 more lines not kept]
```

**Agent**

The stored dF/F (lab's MATLAB output) is in each file, small enough to stream quickly. Next: a metadata scan of every NWB file to map subjects to experimental groups.

**Agent calls Bash**

```bash
cd $TMPDIR && . scratch/bin/activate && cat > scan.py <<'EOF'
import h5py, remfile, json, sys
from concurrent.futures import ThreadPoolExecutor
assets = [a for a in json.load(open('d/assets.json')) if a['path'].endswith('.nwb')]
from dandi.dandiapi import DandiAPIClient
def s(x):
    x = x[()] if hasattr(x, 'shape') else x
    return x.decode() if isinstance(x, bytes) else x
def one(a):
    url = f"https://api.dandiarchive.org/api/assets/{a['asset_id']}/download/"
    import requests
    url = requests.head(url, allow_redirects=True).url.split('?')[0]
    for attempt in range(3):
        try:
            f = h5py.File(remfile.File(url), 'r'); break
        except Exception as e:
            err = e
    else:
        return {'path': a['path'], 'error': repr(err)}
    g = f['general']
    r = {'path': a['path'], 'asset_id': a['asset_id'], 'size': a['size'],
         'subject_id': s(g['subject/subject_id']), 'genotype': s(g['subject/genotype']), 'sex': s(g['subject/sex']),
         'age': s(g['subject/age']), 'session_id': s(g['session_id']), 'start': s(f['session_start_time']),
         'exp': s(g['experiment_description'])[:120], 'sess_desc': s(f['session_description']),
         'effectors': list(g['optogenetic_experiment_metadata/optogenetic_effectors'].keys()),
         'fp_locations': [x.decode() for x in g['fiber_photometry/fiber_photometry_table/location'][:]],
         'indicators': list(g['fiber_photometry/fiber_photometry_indicators'].keys()),
         'acq': {k: f['acquisition'][k]['data'].shape for k in f['acquisition']},
         'ophys': {k: f['processing/ophys'][k]['data'].shape for k in f['processing/ophys']},
         'intervals': list(f['intervals'].keys())}
    ep = f['intervals/optogenetic_epochs_table']
    r['epoch_cols'] = list(ep.keys())
    r['start_time'] = ep['start_time'][:].tolist(); r['stop_time'] = ep['stop_time'][:].tolist()
    r['freq'] = ep['stimulus_frequency'][:].tolist(); r['npulses'] = ep['number_pulses_per_pulse_train'][:].tolist()
    r['period'] = ep['period_in_ms'][:].tolist(); r['pulse_len'] = ep['pulse_length_in_ms'][:].tolist()
    r['iti'] = ep['intertrain_interval_in_ms'][:].tolist(); r['ntrains'] = ep['number_trains'][:].tolist()
    r['sites'] = ep['optogenetic_sites'][:].tolist()
    r['ophys_rates'] = {k: float(f['processing/ophys'][k]['starting_time'].attrs['rate']) for k in f['processing/ophys'] if 'starting_time' in f['processing/ophys'][k]}
    r['ophys_t0'] = {k: float(f['processing/ophys'][k]['starting_time'][()]) for k in f['processing/ophys'] if 'starting_time' in f['processing/ophys'][k]}
    r['ophys_units'] = {k: s(f['processing/ophys'][k]['data'].attrs['unit']) for k in f['processing/ophys']}
    return r
with ThreadPoolExecutor(16) as ex:
    out = list(ex.map(one, assets))
json.dump(out, open('d/scan.json', 'w'), default=str)
print(len(out), sum('error' in r for r in out))
EOF
time python scan.py 2>&1 | tail -5
```

```
258 0

real	7m54.027s
user	0m36.570s
sys	0m2.622s
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && . scratch/bin/activate && python - <<'EOF'
import json, pandas as pd, numpy as np, collections
d = json.load(open('d/scan.json'))
df = pd.DataFrame(d)
df['stim'] = df.effectors.map(lambda e: '+'.join(sorted(x.split('_')[-1] for x in e)))
df['fp'] = df.fp_locations.map(lambda l: '/'.join(sorted(set(l))))
df['ind'] = df.indicators.map(lambda l: '/'.join(l))
df['exp_short'] = df.exp.str[:60]
df['n_ep'] = df.start_time.map(len)
df['dff'] = df.ophys.map(lambda o: '/'.join(sorted(k.replace('deltaF_over_F_','') for k in o if k.startswith('deltaF'))))
pd.set_option('display.width', 250); pd.set_option('display.max_rows', 300); pd.set_option('display.max_colwidth', 70)
print(df.groupby(['exp_short','genotype','stim','fp','dff','session_id']).size().to_string())
print(df.session_id.value_counts())
print(df.sex.value_counts(), df.age.value_counts())
print(df.ophys_units.map(lambda u: tuple(sorted(set(u.values())))).value_counts())
print(df.ophys_rates.map(lambda u: tuple(sorted(set(u.values())))).value_counts())
print(df.ophys_t0.map(lambda u: tuple(sorted(set(u.values())))).value_counts())
print(df.n_ep.value_counts())
print(df.intervals.map(tuple).value_counts())
print(df.start.str[-6:].value_counts())
EOF
```

```
exp_short                                                     genotype                   stim  fp       dff  session_id             
Dopaminergic axon terminals recordings. Mice were freely mov  VGlut2-cre x DAT-flp       STN   DLS/TS   DLS  varying_durations           8
                                                                                                             varying_frequencies         8
                                                                                                        TS   varying_durations           9
                                                                                                             varying_frequencies         9
Parkinson's resilient Vglut2+ dopamine subtypes recordings.   VGlut2-cre X DAT-flp       PPN   SNc      SNc  varying_durations          10
                                                                                                             varying_frequencies        10
                                                                                         STN   SNc      SNc  varying_durations           9
                                                                                                             varying_frequencies         9
Parkinson's-vulnerable Anxa1+ dopamine subtypes recordings.   Vglut2-phiC X Anxa1-cre    PPN   DLS/SNc  DLS  varying_durations_DLS       4
                                                                                                             varying_frequencies_DLS     4
                                                                                                        SNc  varying_durations           6
                                                                                                             varying_durations_SNc       4
                                                                                                             varying_frequencies         6
                                                            
[... 67 more lines not kept]
```

**Agent**

Subject counts per group match the paper's n closely. One striking pattern: for Anxa1 mice the dandiset's DLS and SNc counts are the paper's swapped. Looking closer.

**Agent calls Bash**

```bash
cd $TMPDIR && . scratch/bin/activate && python - <<'EOF'
import json, pandas as pd, numpy as np
d = json.load(open('d/scan.json'))
df = pd.DataFrame(d)
df['stim'] = df.effectors.map(lambda e: '+'.join(sorted(x.split('_')[-1] for x in e)))
pd.set_option('display.width', 250); pd.set_option('display.max_rows', 300); pd.set_option('display.max_colwidth', 120)
a = df[df.genotype.str.contains('Anxa1')]
for _, r in a.sort_values('path').iterrows():
    print(r.path, r.stim, r.fp_locations, r.indicators, r.acq, list(r.ophys), r.size//1e6, r.start)
print()
for _, r in df[df.start_time.map(len).isin([20,40,80,45,63,67])].sort_values('path').iterrows():
    print(r.path, r.exp[:30], len(r.start_time), sorted(set(r.freq)), sorted(set(np.round(np.array(r.stop_time)-np.array(r.start_time),2))))
EOF
```

```
sub-C5903/sub-C5903_ses-varying-durations.nwb STN ['SNc', 'SNc', 'DLS', 'DLS'] ['GCaMP8f_DLS', 'GCaMP8f_SNc'] {'raw_signal_SNc': [1587200]} ['deltaF_over_F_SNc', 'demodulated_calcium_signal_SNc', 'demodulated_isosbestic_control_SNc', 'downsampled_calcium_signal_SNc', 'downsampled_isosbestic_control_SNc'] 0.0 2024-08-27T16:10:23-00:01
sub-C5903/sub-C5903_ses-varying-frequencies.nwb STN ['SNc', 'SNc', 'DLS', 'DLS'] ['GCaMP8f_DLS', 'GCaMP8f_SNc'] {'raw_signal_SNc': [11850133]} ['deltaF_over_F_SNc', 'demodulated_calcium_signal_SNc', 'demodulated_isosbestic_control_SNc', 'downsampled_calcium_signal_SNc', 'downsampled_isosbestic_control_SNc'] 0.0 2024-08-30T14:53:43-00:01
sub-C5904/sub-C5904_ses-varying-durations-DLS.nwb STN ['SNc', 'SNc', 'DLS', 'DLS'] ['GCaMP8f_DLS', 'GCaMP8f_SNc'] {'raw_signal_DLS': [1832448]} ['deltaF_over_F_DLS', 'demodulated_calcium_signal_DLS', 'demodulated_isosbestic_control_DLS', 'downsampled_calcium_signal_DLS', 'downsampled_isosbestic_control_DLS'] 0.0 2024-08-27T14:20:11-00:01
sub-C5904/sub-C5904_ses-varying-durations-SNc.nwb STN ['SNc', 'SNc', 'DLS', 'DLS'] ['GCaMP8f_DLS', 'GCaMP8f_SNc'] {'raw_signal_SNc': [1709056]} ['deltaF_over_F_SNc', 'demodulated_calcium_signal_SNc', 'demodulated_isosbestic_control_SNc', 'downsampled_calcium_signal_SNc', 'downsampled_isosbestic_control_SNc'] 0.0 2024-08-27T15:53:55-00:01
sub-C5904/sub-C5904_ses-varying-frequencies-DLS.nwb STN ['SNc', 'SNc', 'DLS', 'DLS'] ['GCaMP8f_DLS', 'GCaMP8f_SNc'] {'raw_signal_DLS': [9898549]} ['deltaF_over_F_DLS', 'demodulated_calcium_signal_DLS', 'demodulated_isosbestic_control_DLS', 'downsampled_calcium_signal_DLS', 'downsampled_isosbestic_control_DLS'] 0.0 2024-08-29T10:48:44-00:01
sub-C5904/sub-C5904_ses-varying-frequencies-SNc.nwb STN ['SNc', 'SNc', 'DLS', 'DLS'] ['GCaMP8f_DLS', 'GCaMP8f_SNc'] {'raw_signal_SNc': [9714253]} ['deltaF_over_F_SNc', 'demodulated_calcium_signal_SNc', 'demodulated_isosbestic_control_SNc', 'downsampled_calcium_signal_SNc', 'downsampled_isosbestic_contr
[... 100 more lines not kept]
```

**Agent**

Several irregular files (B-series with 16 s "stimuli", 40/80 epochs). Reading the conversion code for how epochs and sites are set.

**Agent calls Bash**

```bash
cd $TMPDIR/hnasko-lab-to-nwb/src/hnasko_lab_to_nwb/lotfi_2025; sed -n 1,608p convert_session.py | grep -v "^\s*#" | head -400
```

```
"""Primary script to run to convert an entire session for of data using the NWBConverter."""

from datetime import datetime
from pathlib import Path
from typing import Union

import pandas as pd
import pytz

from hnasko_lab_to_nwb.lotfi_2025.interfaces.concatenated_tdt_fp_interface import (
    ConcatenatedTDTFiberPhotometryInterface,
)
from hnasko_lab_to_nwb.lotfi_2025.nwbconverter import Lofti2025NWBConverter
from neuroconv.utils import dict_deep_update, load_dict_from_file


def get_target_area_for_subject(file_path: Path, subject_id: str) -> str:
    """Extract available sites for a specific subject.

    Parameters
[... 381 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . scratch/bin/activate && python - <<'EOF'
import json, numpy as np, pandas as pd
d = {r['path']: r for r in json.load(open('d/scan.json'))}
for p in ['sub-B7514/sub-B7514_ses-varying-durations.nwb','sub-B7514/sub-B7514_ses-varying-frequencies.nwb','sub-B8627/sub-B8627_ses-varying-durations.nwb','sub-C2659/sub-C2659_ses-varying-frequencies.nwb','sub-C3412/sub-C3412_ses-varying-frequencies.nwb', 'sub-C4561/sub-C4561_ses-varying-frequencies_image.nwb']:
    r = d[p]
    t = pd.DataFrame({k: r[k] for k in ['start_time','stop_time','freq','npulses','period','pulse_len','iti','ntrains']})
    t['dur'] = (t.stop_time - t.start_time).round(3)
    print(p, r['acq'], r['ophys'], r['ophys_rates'])
    print(t.sort_values('start_time').round(3).to_string())
EOF
```

```
sub-B7514/sub-B7514_ses-varying-durations.nwb {'raw_signal_SNr': [20035584, 1]} {'deltaF_over_F_SNr': [82065], 'demodulated_calcium_signal_SNr': [20035584], 'demodulated_isosbestic_control_SNr': [20035584], 'downsampled_calcium_signal_SNr': [82065], 'downsampled_isosbestic_control_SNr': [82065]} {'deltaF_over_F_SNr': 100.0, 'demodulated_calcium_signal_SNr': 24414.0625, 'demodulated_isosbestic_control_SNr': 24414.0625, 'downsampled_calcium_signal_SNr': 100.0, 'downsampled_isosbestic_control_SNr': 100.0}
    start_time  stop_time  freq  npulses  period  pulse_len  iti  ntrains     dur
30      43.421     43.672  40.0       10    25.0        1.0  0.0        1   0.251
0       54.421     55.422  40.0       40    25.0        1.0  0.0        1   1.001
10      65.471     69.471  40.0      160    25.0        1.0  0.0        1   4.001
20      79.520     95.519  40.0      639    25.0        1.0  0.0        1  15.999
31     115.519    115.770  40.0       10    25.0        1.0  0.0        1   0.251
1      126.569    127.570  40.0       40    25.0        1.0  0.0        1   1.001
11     137.619    141.617  40.0      159    25.0        1.0  0.0        1   3.999
21     151.618    167.618  40.0      640    25.0        1.0  0.0        1  16.000
32     187.617    187.868  40.0       10    25.0        1.0  0.0        1   0.251
2      198.667    199.667  40.0       39    25.0        1.0  0.0        1   1.000
12     209.696    213.697  40.0      160    25.0        1.0  0.0        1   4.000
22     223.696    239.696  40.0      639    25.0        1.0  0.0        1  16.000
33     259.715    259.966  40.0       10    25.0        1.0  0.0        1   0.251
3      270.764    271.764  40.0       39    25.0        1.0  0.0        1   1.000
13     281.765    285.764  40.0      159    25.0        1.0  0.0        1   4.000
23     295.814    311.814  40.0      640    25.0        1.0  0.0        1  16.000
34     331.813    332.064  40.0       10    25.0        1.0  0.0        1   0.251
4      342.862  
[... 305 more lines not kept]
```

**Agent calls Bash**

```bash
mkdir -p entries/001528-hadjas-2025 && cd $TMPDIR && . scratch/bin/activate && python - <<'EOF'
import json, time, h5py, remfile, numpy as np
d = {r['path']: r for r in json.load(open('d/scan.json'))}
import requests
for p in ['sub-C4561/sub-C4561_ses-varying-durations_image.nwb','sub-B7514/sub-B7514_ses-varying-frequencies.nwb','sub-C5904/sub-C5904_ses-varying-durations-DLS.nwb']:
    t=time.time()
    url = requests.head(f"https://api.dandiarchive.org/api/assets/{d[p]['asset_id']}/download/", allow_redirects=True).url.split('?')[0]
    f = h5py.File(remfile.File(url), 'r')
    o = f['processing/ophys']
    k = [x for x in o if x.startswith('deltaF')][0]
    site = k.split('_')[-1]
    dff = o[k]['data'][:]; gc = o['downsampled_calcium_signal_'+site]['data'][:]; af = o['downsampled_isosbestic_control_'+site]['data'][:]
    print(p, time.time()-t, dff.shape, np.nanpercentile(dff,[0.1,50,99.9]).round(2), np.isnan(dff).sum(), np.nanpercentile(gc,[1,50,99]).round(4), np.nanpercentile(af,[1,50,99]).round(4), np.isnan(gc).sum())
    print(o[k]['data'].chunks, o[k]['data'].compression)
EOF
```

```
sub-C4561/sub-C4561_ses-varying-durations_image.nwb 2.257235050201416 (25895,) [-4.42 -0.39 25.18] 0 [0.0882 0.0926 0.1077] [0.0516 0.0533 0.0573] 0
(25895,) gzip
sub-B7514/sub-B7514_ses-varying-frequencies.nwb 3.0498573780059814 (181109,) [-10.69  -0.    44.08] 0 [0.0547 0.0585 0.0669] [0.0377 0.0415 0.0463] 0
(181109,) gzip
sub-C5904/sub-C5904_ses-varying-durations-DLS.nwb 2.281226396560669 (30022,) [-3.38 -0.05  4.7 ] 0 [0.0273 0.0284 0.0304] [0.0246 0.025  0.0258] 0
(30022,) gzip
Shell cwd was reset to
```

**Agent**

Loading is about 2 to 3 s per file, so all 258 files in parallel take roughly a minute. The dF/F values look like percent, but the files say "a.u.". Writing the helper module.

**Agent calls Write**

```json
{
 "file_path": "entries/001528-hadjas-2025/photometry.py",
 "content": "\"\"\"Loading and response measures for the fiber photometry data of dandiset 001528.\n\nHadjas et al. (2025), \"Parkinson's Disease-vulnerable and -resilient dopamine neurons display\nopposite responses to excitatory input\", bioRxiv, doi:10.1101/2025.06.03.657460.\n\nEach NWB file holds one recording of one mouse: the raw modulated photodetector signal, the\ndemodulated and 100 Hz downsampled 465 nm and 405 nm signals, and the dF/F computed by the lab's\nMATLAB pipeline (series `deltaF_over_F_<site>`), with a table of optogenetic stimulation epochs\n(start, stop, frequency). Files are streamed from the archive; nothing is written to disk. Only\nthe 100 Hz series and the epoch table are read.\n\nThe dandiset has no published version. `DANDISET_VERSION` is the draft, and\n`DRAFT_MODIFIED` is the modification time of the draft that this entry was written against;\n`check_version` reports whether the draft has changed since.\n\nWhere the parameters come from:\n\n- The dF/F is the lab's own (stored in the files). Its recomputation in `recompute_dff` follows\n  the Methods (biexponential fit of the 405 nm signal, scaled to the 465 nm signal by robust\n  linear regression) with the details of the lab's MATLAB scripts as described in\n  `reproduced_analysis/analysis_notes.md` of https://github.com/catalystneuro/hnasko-lab-to-nwb\n  at commit deaefa7b1776a5ffb98fd50c5ff4d7b899bdaf59: the first 1 s excluded from the fit, an\n  intercept in the robust fit, dF/F in percent. The MATLAB scripts themselves are not public.\n- Trial windows and the baseline follow the Methods: traces aligned to stimulation onset, the\n  mean dF/F over the 1 s before onset subtracted. The window from 5 s before to 10 s after onset\n  is that of the MATLAB scripts (analysis_notes.md).\n- The response to a train is the mean baseline-subtracted dF/F during the train (the Figure 3C\n  legend, \"mean dF/F during stim train\"); the pre-stimulus comparison window has the length of\n  the train and ends at onset, as in the MATLAB windows `preStm250ms`, `stm_n1_0s` and\n  `stm_n4_0s` (analysis_notes.md). The post-stimulus (rebound) window is the 1 s after offset\n  (the MATLAB windows `stm250_1250ms`, `stm1_2s` and `stm4_5s`). These are choices where the\n  Methods are not explicit.\n- Per mouse, trials of one condition are averaged (\"trials within session and subject were\n  averaged\", Methods).\n\"\"\"\n\nfrom __future__ import annotations\n\nimport hashlib\nfrom concurrent.futures import ThreadPoolExecutor\n\nimport h5py\nimport numpy as np\nimport pandas as pd\nimport remfile\nfrom dandi.dandiapi import DandiAPIClient\n\nDANDISET_ID = \"001528\"\nDANDISET_VERSION = \"draft\"\nDRAFT_MODIFIED = \"2026-09-01T15:27:47.076206Z\"\n\nFS = 100.0                 # Hz, the downsampled series and the stored dF/F\nPRE_S, POST_S = 5.0, 10.0  # trial window around onset, MATLAB scripts\nBASELINE = (-1.0, 0.0)     # s, Methods: 1 s pre-stimulation baseline subtracted\nDURATIONS = (0.25, 1.0, 4.0, 16.0)\nFREQUENCIES = (5.0, 10.0, 20.0, 40.0)\nMIN_TRAIN_S = 0.2          # epochs shorter than this are not trains (zero-length entries exist)\n\nGROUP_PREFIX = {\n    \"SNr GABAergic\": \"GABA\",\n    \"SNc pan-dopaminergic\": \"panDA\",\n    \"Striatal dopamine release\": \"GRABDA\",\n    \"Dopaminergic axon terminals\": \"DAterm\",\n    \"Parkinson's resilient Vglut2+\": \"Vglut2\",\n    \"Parkinson's-vulnerable Anxa1+\": \"Anxa1\",\n}\n\n\ndef check_version() -> dict:\n    \"\"\"Return the draft's modification time, asset count and whether it matches DRAFT_MODIFIED.\"\"\"\n    with DandiAPIClient() as client:\n        ds = client.get_dandiset(DANDISET_ID, DANDISET_VERSION)\n        raw = ds.get_raw_metadata()\n        info = ds.version\n    return {\"modified\": info.modified.isoformat(), \"asset_count\": info.asset_count,\n            \"matches_pinned\": info.modified.isoformat().replace(\"+00:00\", \"Z\") == DRAFT_MODIFIED,\n            \"name\": raw.get(\"name\")}\n\n\ndef nwb_assets() -> list[dict]:\n    with DandiAPIClient() as client:\n        ds = client.get_dandiset(DANDISET_ID, DANDISET_VERSION)\n        return [{\"path\": a.path, \"asset_id\": a.identifier, \"size\": a.size,\n                 \"url\": a.get_content_url(follow_redirects=1, strip_query=True)}\n                for a in ds.get_assets() if a.path.endswith(\".nwb\")]\n\n\ndef _str(x):\n    x = x[()] if hasattr(x, \"shape\") else x\n    return x.decode() if isinstance(x, bytes) else x\n\n\ndef load_file(asset: dict) -> dict:\n    \"\"\"Read the metadata, the 100 Hz series and the epoch table of one file.\"\"\"\n    last = None\n    for _ in range(3):\n        try:\n            f = h5py.File(remfile.File(asset[\"url\"]), \"r\")\n            break\n        except OSError as e:  # transient network errors\n            last = e\n    else:\n        raise last\n    with f:\n        g = f[\"general\"]\n        ophys = f[\"processing/ophys\"]\n        dff_name = [k for k in ophys if k.startswith(\"deltaF_over_F_\")]\n        assert len(dff_name) == 1, (asset[\"path\"], list(ophys))\n        site = dff_name[0].removeprefix(\"deltaF_over_F_\")\n        series = {}\n        for key, name in ((\"dff\", f\"deltaF_over_F_{site}\"), (\"gc\", f\"downsampled_calcium_signal_{site}\"),\n                          (\"af\", f\"downsampled_isosbestic_control_{site}\")):\n            ts = ophys[name]\n            series[key] = ts[\"data\"][:].astype(float)\n            series[key + \"_unit\"] = _str(ts[\"data\"].attrs[\"unit\"])\n            series[key + \"_rate\"] = float(ts[\"starting_time\"].attrs[\"rate\"]) if \"starting_time\" in ts else None\n            series[key + \"_t0\"] = float(ts[\"starting_time\"][()]) if \"starting_time\" in ts else None\n            series[key + \"_has_timestamps\"] = \"timestamps\" in ts\n        ep = f[\"intervals/optogenetic_epochs_table\"]\n        epochs = pd.DataFrame({\n            \"start\": ep[\"start_time\"][:], \"stop\": ep[\"stop_time\"][:],\n            \"frequency\": ep[\"stimulus_frequency\"][:], \"pulses\": ep[\"number_pulses_per_pulse_train\"][:],\n            \"period_ms\": ep[\"period_in_ms\"][:], \"power_mW\": ep[\"power_in_mW\"][:],\n            \"wavelength_nm\": ep[\"wavelength_in_nm\"][:]})\n        effectors = list(g[\"optogenetic_experiment_metadata/optogenetic_effectors\"].keys())\n        exp = _str(g[\"experiment_description\"])\n        group = [v for k, v in GROUP_PREFIX.items() if exp.startswith(k)]\n        assert len(group) == 1, (asset[\"path\"], exp[:80])\n        rec = {\n            \"path\": asset[\"path\"], \"asset_id\": asset[\"asset_id\"],\n            \"subject\": _str(g[\"subject/subject_id\"]).upper(), \"subject_id_raw\": _str(g[\"subject/subject_id\"]),\n            \"genotype\": _str(g[\"subject/genotype\"]), \"sex\": _str(g[\"subject/sex\"]),\n            \"session_id\": _str(g[\"session_id\"]), \"session_start\": _str(f[\"session_start_time\"]),\n            \"experiment_description\": exp, \"group\": group[0], \"site\": site,\n            \"fp_table_locations\": sorted({x.decode() for x in g[\"fiber_photometry/fiber_photometry_table/location\"][:]}),\n            \"input\": \"+\".join(sorted(e.split(\"_\")[-1] for e in effectors)),\n            \"protocol\": \"durations\" if _str(g[\"session_id\"]).startswith(\"varying_durations\") else \"frequencies\",\n            \"raw_rate\": float(f[\"acquisition\"][[k for k in f[\"acquisition\"] if k.startswith(\"raw_signal\")][0]]\n                              [\"starting_time\"].attrs[\"rate\"]),\n            \"epochs\": epochs, **series,\n        }\n    rec[\"dff_md5\"] = hashlib.md5(np.ascontiguousarray(rec[\"dff\"]).tobytes()).hexdigest()\n    return rec\n\n\ndef load_all(workers: int = 24) -> list[dict]:\n    assets = nwb_assets()\n    with ThreadPoolExecutor(workers) as ex:\n        return list(ex.map(load_file, assets))\n\n\ndef label_epochs(rec: dict) -> pd.DataFrame:\n    \"\"\"Epochs with their train duration (rounded to the protocol's values) and whether usable.\n\n    An epoch is dropped when it is shorter than MIN_TRAIN_S, or when its trial window does not\n    lie within the recorded dF/F.\n    \"\"\"\n    ep = rec[\"epochs\"].copy()\n    ep[\"length\"] = ep.stop - ep.start\n    ep[\"duration\"] = [min(DURATIONS, key=lambda d: abs(d - x)) for x in ep.length]\n    n = len(rec[\"dff\"])\n    ep[\"in_signal\"] = (np.floor((ep.start - PRE_S) * FS) >= 0) & (np.floor((ep.start + POST_S) * FS) < n)\n    ep[\"is_train\"] = ep.length >= MIN_TRAIN_S\n    ep[\"usable\"] = ep.in_signal & ep.is_train\n    return ep\n\n\ndef trial_matrix(signal: np.ndarray, onsets: np.ndarray) -> tuple[np.ndarray, np.ndarray]:\n    \"\"\"Trials x samples, from PRE_S before to POST_S after each onset (index = floor(t * FS)),\n    with the mean over BASELINE subtracted from each trial.\"\"\"\n    pre, post = int(PRE_S * FS), int(POST_S * FS)\n    t = np.arange(-pre, post + 1) / FS\n    idx = np.floor(np.asarray(onsets) * FS).astype(int)\n    m = np.stack([signal[i - pre:i + post + 1] for i in idx]) if len(idx) else np.empty((0, len(t)))\n    base = (t >= BASELINE[0]) & (t < BASELINE[1])\n    return m - np.nanmean(m[:, base], axis=1, keepdims=True), t\n\n\ndef window_mean(trace: np.ndarray, t: np.ndarray, a: float, b: float) -> np.ndarray:\n    \"\"\"Mean over the last axis for a <= t < b.\"\"\"\n    w = (t >= a) & (t < b)\n    return np.nanmean(trace[..., w], axis=-1)\n\n\ndef condition_traces(rec: dict, signal: np.ndarray | None = None) -> pd.DataFrame:\n    \"\"\"One row per condition of a recording: the trial-averaged, baseline-subtracted trace.\n\n    Conditions are the train duration for the durations protocol, and duration and frequency for\n    the frequencies protocol (all trains of the durations protocol are at 40 Hz).\n    \"\"\"\n    sig = rec[\"dff\"] if signal is None else signal\n    ep = label_epochs(rec)\n    rows = []\n    for (dur, freq), e in ep[ep.usable].groupby([\"duration\", \"frequency\"]):\n        m, t = trial_matrix(sig, e.start.values)\n        rows.append({\"duration\": dur, \"frequency\": freq, \"n_trials\": len(e),\n                     \"n_dropped\": int(((ep.duration == dur) & (ep.frequency == freq) & ~ep.usable).sum()),\n                     \"trace\": np.nanmean(m, axis=0), \"t\": t})\n    return pd.DataFrame(rows)\n\n\ndef response_measures(trace: np.ndarray, t: np.ndarray, duration: float) -> dict:\n    \"\"\"Mean dF/F during the train, in the pre-stimulus window of the same length, in the 1 s after\n    offset, the area under the curve during the train, and the time of the peak from onset to\n    2.25 s after onset.\"\"\"\n    peak_w = (t >= 0) & (t < 2.25)\n    return {\"during\": window_mean(trace, t, 0.0, duration),\n            \"pre\": window_mean(trace, t, -duration, 0.0),\n            \"post\": window_mean(trace, t, duration, duration + 1.0),\n            \"auc\": np.trapezoid(trace[(t >= 0) & (t <= duration)], dx=1 / FS),\n            \"peak_latency\": t[peak_w][np.nanargmax(trace[peak_w])]}\n\n\ndef recompute_dff(gc: np.ndarray, af: np.ndarray, exclude_s: float = 1.0) -> np.ndarray:\n    \"\"\"dF/F in percent from the 100 Hz 465 nm (gc) and 405 nm (af) signals, as the Methods and the\n    MATLAB scripts describe: a biexponential fit of af over time (first `exclude_s` excluded),\n    scaled to gc by robust (Huber) linear regression with an intercept.\"\"\"\n    from scipy.optimize import curve_fit\n    import statsmodels.api as sm\n\n    x = np.arange(len(af), dtype=float)\n    ok = np.isfinite(af) & np.isfinite(gc) & (x >= exclude_s * FS)\n    xs = x / len(x)\n\n    def biexp(z, a, b, c, d):\n        return a * np.exp(b * z) + c * np.exp(d * z)\n\n    a0 = np.nanmedian(af[ok])\n    p, _ = curve_fit(biexp, xs[ok], af[ok], p0=[a0 * 0.1, -5.0, a0 * 0.9, -0.1], maxfev=20000)\n    fit = biexp(xs, *p)\n    rlm = sm.RLM(gc[ok], sm.add_constant(fit[ok]), M=sm.robust.norms.HuberT()).fit()\n    base = rlm.params[0] + rlm.params[1] * fit\n    return 100.0 * (gc - base) / base\n"
}
```

```
File created successfully at: entries/001528-hadjas-2025/photometry.py (file state is current in your context — no need to Read it back)
```

**Agent**

Loading everything once into a scratch cache for development (the notebook itself will stream).

**Agent calls Bash**

```bash
cd $TMPDIR && . scratch/bin/activate && cat > dev_load.py <<'EOF'
import sys, time, pickle
sys.path.insert(0, 'entries/001528-hadjas-2025')
import photometry as ph
t = time.time()
print(ph.check_version())
recs = ph.load_all()
print(len(recs), time.time() - t)
pickle.dump(recs, open('recs.pkl', 'wb'))
EOF
python dev_load.py
```

```
Exit code 1
{'modified': '2026-09-01T15:27:47.076206+00:00', 'asset_count': 290, 'matches_pinned': True, 'name': "Fiber photometry of SNc/SNr dopamine and GABA neuron responses to optogenetic STN and PPN stimulation in Parkinson's disease"}
Traceback (most recent call last):
  File "/tmp/claude-1001/dev_load.py", line 6, in <module>
    recs = ph.load_all()
  File "entries/001528-hadjas-2025/photometry.py", line 149, in load_all
    return list(ex.map(load_file, assets))
  File "/opt/hostedtoolcache/Python/3.13.16/x64/lib/python3.13/concurrent/futures/_base.py", line 625, in result_iterator
    yield _result_or_cancel(fs.pop())
          ~~~~~~~~~~~~~~~~~^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.13.16/x64/lib/python3.13/concurrent/futures/_base.py", line 318, in _result_or_cancel
    return fut.result(timeout)
           ~~~~~~~~~~^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.13.16/x64/lib/python3.13/concurrent/futures/_base.py", line 453, in result
    return self.__get_result()
           ~~~~~~~~~~~~~~~~~^^
  File "/opt/hostedtoolcache/Python/3.13.16/x64/lib/python3.13/concurrent/futures/_base.py", line 402, in __get_result
    raise self._exception
  File "/opt/hostedtoolcache/Python/3.13.16/x64/lib/python3.13/concurrent/futures/thread.py", line 59, in run
    result = self.fn(*self.args, **self.kwargs)
[... 16 more lines not kept]
```

**Agent**

Some series carry timestamps in place of a rate. Inspecting one.

**Agent calls Bash**

```bash
cd $TMPDIR && . scratch/bin/activate && python - <<'EOF'
import json, h5py, remfile, numpy as np, requests
d = {r['path']: r for r in json.load(open('d/scan.json'))}
import collections
kinds = collections.Counter()
for p, r in d.items():
    kinds[(r['session_id'].split('_')[1][:4], tuple(sorted(set(r['ophys_rates'].values()))), r['exp'][:20])] += 1
for k, v in sorted(kinds.items()): print(k, v)
for p in ['sub-C2659/sub-C2659_ses-varying-frequencies.nwb', 'sub-C4561/sub-C4561_ses-varying-frequencies_image.nwb']:
    url = requests.head(f"https://api.dandiarchive.org/api/assets/{d[p]['asset_id']}/download/", allow_redirects=True).url.split('?')[0]
    f = h5py.File(remfile.File(url), 'r')
    for k in f['processing/ophys']:
        g = f['processing/ophys'][k]
        print(p, k, list(g.keys()))
        if 'timestamps' in g:
            ts = g['timestamps'][:]
            dt = np.diff(ts)
            print('  ts', ts[0], ts[-1], len(ts), np.median(dt), dt.min(), dt.max(), (dt > 0.02).sum(), np.where(dt>0.02)[0][:5], dt[dt>0.02][:5])
    for k in f['acquisition']:
        print(k, list(f['acquisition'][k].keys()))
    dff = f['processing/ophys'][[k for k in f['processing/ophys'] if k.startswith('deltaF')][0]]['data'][:]
    print('nan in dff', np.isnan(dff).sum())
EOF
```

```
('dura', (100.0, 6103.5156), "Parkinson's resilien") 19
('dura', (100.0, 6103.5156), "Parkinson's-vulnerab") 27
('dura', (100.0, 6103.5156), 'SNc pan-dopaminergic') 14
('dura', (100.0, 6103.5156), 'SNr GABAergic neuron') 8
('dura', (100.0, 6103.5156), 'Striatal dopamine re') 31
('dura', (100.0, 24414.0625), 'Dopaminergic axon te') 17
('dura', (100.0, 24414.0625), 'SNc pan-dopaminergic') 6
('dura', (100.0, 24414.0625), 'SNr GABAergic neuron') 7
('freq', (), 'Dopaminergic axon te') 17
('freq', (), "Parkinson's resilien") 3
('freq', (), 'SNc pan-dopaminergic') 6
('freq', (), 'SNr GABAergic neuron') 8
('freq', (100.0, 6103.5156), "Parkinson's resilien") 4
('freq', (100.0, 6103.5156), "Parkinson's-vulnerab") 10
('freq', (100.0, 6103.5156), 'SNc pan-dopaminergic') 4
('freq', (100.0, 6103.5156), 'SNr GABAergic neuron') 7
('freq', (100.0, 6103.5156), 'Striatal dopamine re') 15
('freq', (6103.5156,), "Parkinson's resilien") 12
('freq', (6103.5156,), "Parkinson's-vulnerab") 17
('freq', (6103.5156,), 'SNc pan-dopaminergic') 10
[... 22 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/001528-hadjas-2025 && python - <<'EOF'
import re
s = open('photometry.py').read()
s = s.replace('''            series[key + "_rate"] = float(ts["starting_time"].attrs["rate"]) if "starting_time" in ts else None
            series[key + "_t0"] = float(ts["starting_time"][()]) if "starting_time" in ts else None
            series[key + "_has_timestamps"] = "timestamps" in ts
''', '''            series[key + "_has_timestamps"] = "timestamps" in ts
            if "timestamps" in ts:
                series[key + "_t"] = ts["timestamps"][:]
            else:
                rate, t0 = float(ts["starting_time"].attrs["rate"]), float(ts["starting_time"][()])
                series[key + "_t"] = t0 + np.arange(len(series[key])) / rate
''')
s = s.replace('''            "raw_rate": float(f["acquisition"][[k for k in f["acquisition"] if k.startswith("raw_signal")][0]]
                              ["starting_time"].attrs["rate"]),
''', '''            "raw_rate": _raw_rate(f),
''')
s = s.replace('''def load_file(asset: dict) -> dict:''', '''def _raw_rate(f) -> float:
    raw = f["acquisition"][[k for k in f["acquisition"] if k.startswith("raw_signal")][0]]
    if "starting_time" in raw:
        return float(raw["starting_time"].attrs["rate"])
    return float(1 / np.median(np.diff(raw["timestamps"][:100000])))


def load_file(asset: dict) -> dict:''')
# epochs in-signal check and trial matrix by timestamps
s = s.replace('''    n = len(rec["dff"])
    ep["in_signal"] = (np.floor((ep.start - PRE_S) * FS) >= 0) & (np.floor((ep.start + POST_S) * FS) < n)
''', '''    ts = rec["dff_t"]
    ep["in_signal"] = (ep.start - PRE_S >= ts[0]) & (ep.start + POST_S <= ts[-1])
''')
s = s.replace('''def trial_matrix(signal: np.ndarray, onsets: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    """Trials x samples, from PRE_S before to POST_S after each onset (index = floor(t * FS)),
    with the mean over BASELINE subtracted from each trial."""
    pre, post = int(PRE_S * FS), int(POST_S * FS)
    t = np.arange(-pre, post + 1) / FS
    idx = np.floor(np.asarray(onsets) * FS).astype(int)''', '''def trial_matrix(signal: np.ndarray, times: np.ndarray, onsets: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    """Trials x samples, from PRE_S before to POST_S after each onset, with the mean over BASELINE
    subtracted from each trial. The onset sample is the last one at or before the onset time
    (the MATLAB scripts take floor(t * 100) on a clock starting at 0)."""
    pre, post = int(PRE_S * FS), int(POST_S * FS)
    t = np.arange(-pre, post + 1) / FS
    idx = np.searchsorted(times, np.asarray(onsets), side="right") - 1''')
s = s.replace('''        m, t = trial_matrix(sig, e.start.values)''', '''        m, t = trial_matrix(sig, rec["dff_t"], e.start.values + shift)''')
s = s.replace('''def condition_traces(rec: dict, signal: np.ndarray | None = None) -> pd.DataFrame:''', '''def condition_traces(rec: dict, signal: np.ndarray | None = None, shift: float = 0.0) -> pd.DataFrame:''')
s = s.replace('''    the frequencies protocol (all trains of the durations protocol are at 40 Hz).
    """''', '''    the frequencies protocol (all trains of the durations protocol are at 40 Hz). `shift` moves
    every onset by that many seconds, for the clock check.
    """''')
open('photometry.py','w').write(s)
EOF
grep -n "shift\|_t\"\]\|searchsorted" photometry.py
```

```
125:                series[key + "_t"] = ts["timestamps"][:]
128:                series[key + "_t"] = t0 + np.arange(len(series[key])) / rate
170:    ts = rec["dff_t"]
183:    idx = np.searchsorted(times, np.asarray(onsets), side="right") - 1
195:def condition_traces(rec: dict, signal: np.ndarray | None = None, shift: float = 0.0) -> pd.DataFrame:
199:    the frequencies protocol (all trains of the durations protocol are at 40 Hz). `shift` moves
206:        m, t = trial_matrix(sig, rec["dff_t"], e.start.values + shift)
```

**Agent calls Bash**

```bash
cd $TMPDIR && . scratch/bin/activate && python dev_load.py
```

```
{'modified': '2026-09-01T15:27:47.076206+00:00', 'asset_count': 290, 'matches_pinned': True, 'name': "Fiber photometry of SNc/SNr dopamine and GABA neuron responses to optogenetic STN and PPN stimulation in Parkinson's disease"}
258 581.8216242790222
Shell cwd was reset to
```

**Agent**

Loading took about 10 minutes, far more than expected. Profiling.

**Agent calls Bash**

```bash
cd $TMPDIR && . scratch/bin/activate && python - <<'EOF'
import sys, time
sys.path.insert(0, 'entries/001528-hadjas-2025')
import photometry as ph
t=time.time(); a = ph.nwb_assets(); print('assets', time.time()-t)
import pickle; pickle.dump(a, open('assets_urls.pkl','wb'))
for x in [a[0], a[100], a[200], a[50]]:
    t=time.time(); r = ph.load_file(x); print(x['path'], x['size']//1e6, round(time.time()-t,1), len(r['dff']))
EOF
```

```
assets 35.75767731666565
sub-B7532/sub-B7532_ses-varying-durations.nwb 299.0 2.1 82124
sub-B8370/sub-B8370_ses-varying-durations.nwb 289.0 2.3 82074
sub-C5904/sub-C5904_ses-varying-durations-DLS.nwb 26.0 1.6 30022
sub-C4101/sub-C4101_ses-varying-frequencies.nwb 153.0 2.6 167388
Shell cwd was reset to
```

**Agent**

h5py's global lock serializes the threads. Switching to a process pool.

**Agent calls Bash**

```bash
cd entries/001528-hadjas-2025 && python - <<'EOF'
s = open('photometry.py').read()
s = s.replace("from concurrent.futures import ThreadPoolExecutor", "from concurrent.futures import ProcessPoolExecutor")
s = s.replace('''def load_all(workers: int = 24) -> list[dict]:
    assets = nwb_assets()
    with ThreadPoolExecutor(workers) as ex:
        return list(ex.map(load_file, assets))''', '''def load_all(workers: int = 16) -> list[dict]:
    """Load every NWB file of the dandiset. Processes, not threads: h5py holds a global lock."""
    assets = nwb_assets()
    with ProcessPoolExecutor(workers) as ex:
        return list(ex.map(load_file, assets, chunksize=1))''')
open('photometry.py','w').write(s)
EOF
cd $TMPDIR && . scratch/bin/activate && python dev_load.py
```

```
{'modified': '2026-09-01T15:27:47.076206+00:00', 'asset_count': 290, 'matches_pinned': True, 'name': "Fiber photometry of SNc/SNr dopamine and GABA neuron responses to optogenetic STN and PPN stimulation in Parkinson's disease"}
258 72.55710554122925
Shell cwd was reset to
```

**Agent**

Down to 73 s. Now the data checks.

**Agent calls Bash**

```bash
cd $TMPDIR && . scratch/bin/activate && cat > dev_check.py <<'EOF'
import sys, pickle, numpy as np, pandas as pd, collections
sys.path.insert(0, 'entries/001528-hadjas-2025')
import photometry as ph
pd.set_option('display.width', 250); pd.set_option('display.max_rows', 400)
recs = pickle.load(open('recs.pkl','rb'))
info = pd.DataFrame([{k: r[k] for k in ['path','subject','group','site','input','protocol','session_id','sex','genotype','raw_rate','dff_unit','dff_has_timestamps']} | {
    'n': len(r['dff']), 'nan': int(np.isnan(r['dff']).sum()), 'dt_med': np.median(np.diff(r['dff_t'])), 'dt_max': np.diff(r['dff_t']).max(), 't0': r['dff_t'][0],
    'same_t': np.array_equal(r['dff_t'], r['gc_t']) and np.array_equal(r['dff_t'], r['af_t']), 'md5': r['dff_md5'],
    'p01': np.nanpercentile(r['dff'], 0.1), 'p999': np.nanpercentile(r['dff'], 99.9), 'nep': len(r['epochs']),
    'power': tuple(sorted(set(r['epochs'].power_mW))), 'wl': tuple(sorted(set(r['epochs'].wavelength_nm)))} for r in recs])
print(info.groupby(['group','input','site','protocol']).subject.nunique().unstack())
print(info.dt_med.round(5).value_counts(), info.dt_max.describe(), info.t0.value_counts())
print('same timestamps', info.same_t.all(), 'nan files', (info.nan>0).sum(), info[info.nan>0][['path','nan','n']])
print(info.power.value_counts(), info.wl.value_counts())
print(info.p01.describe(), info.p999.describe())
dup = info[info.md5.duplicated(keep=False)]
print('dups', dup[['path','md5']])
print(info.subject.nunique(), info.groupby('subject').group.nunique().max())
# epochs
rows=[]
for r in recs:
    ep = ph.label_epochs(r)
    for (d,f), e in ep.groupby(['duration','frequency']):
        rows.append({'path': r['path'], 'group': r['group'], 'protocol': r['protocol'], 'duration': d, 'freq': f, 'n': len(e), 'usable': int(e.usable.sum()), 'not_train': int((~e.is_train).sum()), 'out': int((~e.in_signal).sum())})
E = pd.DataFrame(rows)
print(E.groupby(['protocol','duration','freq']).agg(files=('path','nunique'), n=('n','sum'), usable=('usable','sum'), not_train=('not_train','sum'), out=('out','sum')))
print(E.groupby(['protocol','duration','freq','n']).size())
print(E[E.out>0].groupby(['path']).out.sum())
EOF
python dev_check.py
```

```
protocol           durations  frequencies
group  input site                        
Anxa1  PPN   DLS           4            4
             SNc          10           10
       STN   DLS           5            5
             SNc           8            8
DAterm STN   DLS           8            8
             TS            9            9
GABA   PPN   SNr           8            8
       STN   SNr           7            7
GRABDA PPN   DLS           9            9
             TS            9            9
       STN   DLS           7            7
             TS            6            6
Vglut2 PPN   SNc          10           10
       STN   SNc           9            9
panDA  PPN   SNc           9            9
       STN   SNc          11           11
dt_med
0.01    258
[... 188 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/001528-hadjas-2025 && python - <<'EOF'
s = open('photometry.py').read()
old = '''    ts = rec["dff_t"]
    ep["in_signal"] = (ep.start - PRE_S >= ts[0]) & (ep.start + POST_S <= ts[-1])
    ep["is_train"] = ep.length >= MIN_TRAIN_S
    ep["usable"] = ep.in_signal & ep.is_train'''
new = '''    ts = rec["dff_t"]
    ep["in_signal"] = (ep.start - PRE_S >= ts[0]) & (ep.start + POST_S <= ts[-1])
    # the window's samples must be contiguous in time (some files hold segments separated by gaps)
    pre, post = int(PRE_S * FS), int(POST_S * FS)
    idx = np.searchsorted(ts, ep.start.values, side="right") - 1
    lo, hi = np.clip(idx - pre, 0, len(ts) - 1), np.clip(idx + post, 0, len(ts) - 1)
    ep["contiguous"] = np.abs((ts[hi] - ts[lo]) - (pre + post) / FS) < 1.5 / FS
    sig = rec["dff"]
    ep["nan_in_window"] = [bool(np.isnan(sig[a:b + 1]).any()) for a, b in zip(lo, hi)]
    ep["is_train"] = ep.length >= MIN_TRAIN_S
    ep["usable"] = ep.in_signal & ep.contiguous & ep.is_train'''
assert old in s
s = s.replace(old, new)
s = s.replace('''    An epoch is dropped when it is shorter than MIN_TRAIN_S, or when its trial window does not
    lie within the recorded dF/F.''', '''    An epoch is dropped when it is shorter than MIN_TRAIN_S, or when its trial window does not
    lie within the recorded dF/F or is not contiguous in time. Windows holding missing values
    (`nan_in_window`) are kept; means skip the missing samples.''')
open('photometry.py','w').write(s)
EOF
cd $TMPDIR && . scratch/bin/activate && cat > dev_check2.py <<'EOF'
import sys, pickle, numpy as np, pandas as pd, time
sys.path.insert(0, 'entries/001528-hadjas-2025')
import photometry as ph
from scipy import stats
pd.set_option('display.width', 250); pd.set_option('display.max_rows', 400)
recs = pickle.load(open('recs.pkl','rb'))
rows=[]
for r in recs:
    ep = ph.label_epochs(r)
    rows.append({'path': r['path'], 'n': len(ep), 'noncontig': int((~ep.contiguous).sum()), 'nanwin': int((ep.nan_in_window & ep.usable).sum()), 'usable': int(ep.usable.sum())})
E = pd.DataFrame(rows); print(E[(E.noncontig>0)|(E.nanwin>0)])
# clock check: per recording, |during - pre| for true onsets vs shifted by -3 s and +? Use 1 s 40 Hz trains
res=[]
for r in recs:
    for shift in [0.0, -3.0, 3.0]:
        ct = ph.condition_traces(r, shift=shift)
        ct = ct[(ct.duration==1.0)&(ct.frequency==40.0)]
        if not len(ct): continue
        tr, t = ct.trace.iloc[0], ct.t.iloc[0]
        d = ph.window_mean(tr, t, 0, 1) - ph.window_mean(tr, t, -1, 0)
        res.append({'path': r['path'], 'group': r['group'], 'protocol': r['protocol'], 'shift': shift, 'abs_resp': abs(d)})
R = pd.DataFrame(res).pivot_table(index=['path','group','protocol'], columns='shift', values='abs_resp').reset_index()
R['ratio'] = R[0.0] / R[[-3.0, 3.0]].max(axis=1)
print(R.groupby(['group','protocol'])[[0.0,-3.0,3.0,'ratio']].median())
print((R.ratio<1).sum(), R[R.ratio<1.5].sort_values('ratio'))
# dff recompute
t=time.time(); cs=[]
for r in recs[:258:6]:
    try:
        x = ph.recompute_dff(r['gc'], r['af'])
        ok = np.isfinite(x) & np.isfinite(r['dff'])
        cs.append({'path': r['path'], 'r': np.corrcoef(x[ok], r['dff'][ok])[0,1], 'slope': np.polyfit(x[ok], r['dff'][ok], 1)[0], 'maxdiff': np.nanmax(np.abs(x-r['dff']))})
    except Exception as e:
        cs.append({'path': r['path'], 'err': repr(e)})
print(time.time()-t); C = pd.DataFrame(cs); print(C.describe()); print(C.sort_values('r').head(8))
EOF
python dev_check2.py
```

```
Exit code 1
                                             path   n  ...  nanwin  usable
17  sub-C2659/sub-C2659_ses-varying-durations.nwb  15  ...       0      14
37  sub-C3565/sub-C3565_ses-varying-durations.nwb  15  ...       0      14
94  sub-C5007/sub-C5007_ses-varying-durations.nwb  15  ...       0      14
96  sub-C5008/sub-C5008_ses-varying-durations.nwb  15  ...       0      12

[4 rows x 5 columns]
Traceback (most recent call last):
  File "/tmp/claude-1001/dev_check2.py", line 16, in <module>
    ct = ph.condition_traces(r, shift=shift)
  File "entries/001528-hadjas-2025/photometry.py", line 215, in condition_traces
    m, t = trial_matrix(sig, rec["dff_t"], e.start.values + shift)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "entries/001528-hadjas-2025/photometry.py", line 193, in trial_matrix
    m = np.stack([signal[i - pre:i + post + 1] for i in idx]) if len(idx) else np.empty((0, len(t)))
        ~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/tmp/claude-1001/scratch/lib/python3.13/site-packages/numpy/_core/shape_base.py", line 458, in stack
    raise ValueError('all input arrays must have the same shape')
ValueError: all input arrays must have the same shape
```

**Agent calls Bash**

```bash
cd entries/001528-hadjas-2025 && python - <<'EOF'
s = open('photometry.py').read()
old = '''    sig = rec["dff"] if signal is None else signal
    ep = label_epochs(rec)'''
new = '''    sig = rec["dff"] if signal is None else signal
    if shift:
        rec = dict(rec, epochs=rec["epochs"].assign(start=rec["epochs"].start + shift,
                                                    stop=rec["epochs"].stop + shift))
    ep = label_epochs(rec)'''
s = s.replace(old, new)
s = s.replace('''        m, t = trial_matrix(sig, rec["dff_t"], e.start.values + shift)''','''        m, t = trial_matrix(sig, rec["dff_t"], e.start.values)''')
open('photometry.py','w').write(s)
EOF
cd $TMPDIR && . scratch/bin/activate && python dev_check2.py
```

```
path   n  ...  nanwin  usable
17  sub-C2659/sub-C2659_ses-varying-durations.nwb  15  ...       0      14
37  sub-C3565/sub-C3565_ses-varying-durations.nwb  15  ...       0      14
94  sub-C5007/sub-C5007_ses-varying-durations.nwb  15  ...       0      14
96  sub-C5008/sub-C5008_ses-varying-durations.nwb  15  ...       0      12

[4 rows x 5 columns]
shift                    0.0      -3.0       3.0     ratio
group  protocol                                           
Anxa1  durations    0.462668  0.111851  0.171178  2.461187
       frequencies  0.386377  0.161425  0.180681  1.709484
DAterm durations    5.820103  0.709758  0.802127  6.520379
       frequencies  3.426326  0.434167  0.385964  4.944794
GABA   durations    8.794698  0.257894  0.988326  6.956356
       frequencies  7.815445  0.466980  0.711758  7.343486
GRABDA durations    8.009593  0.685417  1.038355  5.724316
       frequencies  7.363526  0.732562  1.113568  4.472579
Vglut2 durations    6.737019  0.559269  0.669870  6.479303
       frequencies  3.213113  0.526745  1.084058  6.336215
panDA  durations    1.136065  0.999431  0.857297  1.455757
[... 83 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/001528-hadjas-2025 && python - <<'EOF'
s = open('photometry.py').read()
old = s[s.index('def recompute_dff'):]
new = '''def recompute_dff(gc: np.ndarray, af: np.ndarray, times: np.ndarray, exclude_s: float = 1.0) -> np.ndarray:
    """dF/F in percent from the 100 Hz 465 nm (gc) and 405 nm (af) signals, as the Methods and the
    MATLAB scripts describe: a biexponential fit of af over time (first `exclude_s` excluded),
    scaled to gc by robust (Huber) linear regression with an intercept. Each contiguous segment
    (separated by missing values or gaps in time) is fitted on its own, as the frequencies
    protocol concatenates separate recordings."""
    from scipy.optimize import curve_fit
    import statsmodels.api as sm

    def biexp(z, a, b, c, d):
        return a * np.exp(b * z) + c * np.exp(d * z)

    out = np.full(len(gc), np.nan)
    good = np.isfinite(gc) & np.isfinite(af)
    breaks = np.flatnonzero(~good[1:] | ~good[:-1] | (np.diff(times) > 1.5 / FS)) + 1
    for seg in np.split(np.arange(len(gc)), breaks):
        seg = seg[good[seg]]
        if len(seg) < 10 * FS:
            continue
        x = (seg - seg[0]) / len(seg)
        fit_on = (seg - seg[0]) >= exclude_s * FS
        a0 = np.median(af[seg])
        p, _ = curve_fit(biexp, x[fit_on], af[seg][fit_on], p0=[a0 * 0.1, -5.0, a0 * 0.9, -0.1], maxfev=20000)
        fit = biexp(x, *p)
        rlm = sm.RLM(gc[seg][fit_on], sm.add_constant(fit[fit_on]), M=sm.robust.norms.HuberT()).fit()
        base = rlm.params[0] + rlm.params[1] * fit
        out[seg] = 100.0 * (gc[seg] - base) / base
    return out
'''
s = s.replace(old, new)
open('photometry.py','w').write(s)
EOF
cd $TMPDIR && . scratch/bin/activate && python - <<'EOF'
import sys, pickle, numpy as np, pandas as pd, time
sys.path.insert(0, 'entries/001528-hadjas-2025')
import photometry as ph
pd.set_option('display.width', 250); pd.set_option('display.max_rows', 400)
recs = pickle.load(open('recs.pkl','rb'))
t=time.time(); cs=[]
for r in recs[::3]:
    try:
        x = ph.recompute_dff(r['gc'], r['af'], r['dff_t'])
        ok = np.isfinite(x) & np.isfinite(r['dff'])
        cs.append({'path': r['path'], 'protocol': r['protocol'], 'r': np.corrcoef(x[ok], r['dff'][ok])[0,1], 'mad': np.median(np.abs(x[ok]-r['dff'][ok]))})
    except Exception as e:
        cs.append({'path': r['path'], 'err': repr(e)})
print(time.time()-t); C = pd.DataFrame(cs); print(C.groupby('protocol').r.describe()); print(C.sort_values('r').head(8))
# Anxa1
rows=[]
for r in recs:
    if r['group']!='Anxa1': continue
    kind = 'single' if r['session_id'] in ('varying_durations','varying_frequencies') else r['site']
    ct = ph.condition_traces(r); c = ct[(ct.duration==1.0)&(ct.frequency==40.0)].iloc[0]
    m = ph.response_measures(c.trace, c.t, 1.0)
    rows.append({'subject': r['subject'], 'input': r['input'], 'protocol': r['protocol'], 'kind': kind, 'gc_med': np.nanmedian(r['gc']), 'af_med': np.nanmedian(r['af']), 'dff_sd': np.nanstd(r['dff']), 'during': m['during'], 'post': m['post'], 'raw_rate': r['raw_rate']})
A = pd.DataFrame(rows)
print(A.groupby(['protocol','kind'])[['gc_med','af_med','dff_sd','during','post']].median())
print(A.groupby(['protocol','kind']).size())
EOF
```

```
58.7018358707428
             count      mean       std  ...       50%       75%       max
protocol                                ...                              
durations     43.0  0.989926  0.032034  ...  0.999953  0.999992  1.000000
frequencies   43.0  0.971072  0.107699  ...  0.998795  0.999815  0.999995

[2 rows x 8 columns]
                                                 path  ...       mad
2     sub-B7532/sub-B7532_ses-varying-frequencies.nwb  ...  1.753699
25  sub-C4562/sub-C4562_ses-varying-durations_imag...  ...  0.272738
58    sub-C2454/sub-C2454_ses-varying-frequencies.nwb  ...  0.297194
41      sub-c4709/sub-c4709_ses-varying-durations.nwb  ...  2.397242
57    sub-C2450/sub-C2450_ses-varying-frequencies.nwb  ...  0.111403
84      sub-C7245/sub-C7245_ses-varying-durations.nwb  ...  0.099280
18    sub-C3710/sub-C3710_ses-varying-frequencies.nwb  ...  1.209900
16    sub-C4100/sub-C4100_ses-varying-frequencies.nwb  ...  0.040670

[8 rows x 4 columns]
                      gc_med    af_med    dff_sd    during      post
protocol    kind                                                    
[... 15 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . scratch/bin/activate && python -c "
from scipy import stats
print('F(1,11)=12.8', stats.f.sf(12.8,1,11))
for x in [21.0,18.2,13.0,4.2,11.5,20.0,24.0,23.2,12.3,15.5,5.9,7.0,18.8,24.8,20.2,18.0,15.3]:
    print(x, 'df3', round(stats.chi2.sf(x,3),5), 'df2', round(stats.chi2.sf(x,2),5))
"
```

```
F(1,11)=12.8 0.004336043536126919
21.0 df3 0.00011 df2 3e-05
18.2 df3 0.0004 df2 0.00011
13.0 df3 0.00464 df2 0.0015
4.2 df3 0.24066 df2 0.12246
11.5 df3 0.00931 df2 0.00318
20.0 df3 0.00017 df2 5e-05
24.0 df3 2e-05 df2 1e-05
23.2 df3 4e-05 df2 1e-05
12.3 df3 0.00642 df2 0.00213
15.5 df3 0.00144 df2 0.00043
5.9 df3 0.11658 df2 0.05234
7.0 df3 0.0719 df2 0.0302
18.8 df3 0.0003 df2 8e-05
24.8 df3 2e-05 df2 0.0
20.2 df3 0.00015 df2 4e-05
18.0 df3 0.00044 df2 0.00012
15.3 df3 0.00158 df2 0.00048
Shell cwd was reset to
```

**Agent calls Write**

```json
{
 "file_path": "claims/001528/10.1101-2025.06.03.657460.yaml",
 "content": "# Claims for Hadjas et al. (2025), bioRxiv preprint version 1, on dandiset 001528.\n# Source: the full text of the preprint (CC BY), read from its JATS XML: Results, figure legends\n# and Methods. The preprint has no data or code availability statement.\n#\n# When these criteria were written, the author had seen the data check only: the file list,\n# the metadata of every file, the number of mice per group, input and recording site, the epoch\n# tables, the units and timestamps of the 100 Hz series, a recomputation of the stored dF/F, and\n# for the clock check the median absolute response to 1 s trains per group (at true and shifted\n# onsets, without its sign). For the Anxa1 mice the author had also seen, per kind of recording\n# (DLS, SNc, and the recordings without a site suffix), the median dF/F during and after 1 s\n# trains (DLS -1.31 and +0.97, SNc -0.40 and +0.07, unsuffixed -0.27 and -0.06, in %, durations\n# protocol). No claim's analysis had been run.\n#\n# Method choices fixed here, where the Methods leave them open:\n# - The dF/F is the lab's own, stored in each file. Traces are aligned to train onset and the\n#   mean over the 1 s before onset is subtracted (Methods). Trials of one condition are averaged\n#   per mouse (Methods); statistics are across mice.\n# - The response to a train is the mean dF/F during the train (Figure 3C legend). The\n#   pre-stimulus comparison window has the length of the train and ends at onset; the rebound\n#   window is the 1 s after offset. Windows of these lengths are among those the lab's MATLAB\n#   scripts compute (analysis_notes.md in catalystneuro/hnasko-lab-to-nwb at commit deaefa7).\n#   The area under the curve during the train gives the same tests within one duration.\n# - Comparisons across train durations use the durations protocol (40 Hz); comparisons across\n#   frequencies use the frequencies protocol at the stated train duration. Where a panel shows\n#   one duration and the text does not say which, the 1 s train is used, as in the insets of\n#   Figures 2 and 4 and in Figure 5C.\n# - Each test is the one the paper reports for that comparison (paired t-test, Wilcoxon\n#   signed-rank, Friedman, repeated-measures ANOVA, two-way ANOVA). Repeated-measures ANOVA\n#   p-values use the Greenhouse-Geisser correction, as the fractional degrees of freedom in the\n#   paper (for example F2,15 for four frequencies in nine mice) imply. Alpha is 0.05.\n# - Mice are grouped by the files' own experiment description, recording site (the name of the\n#   dF/F series) and stimulated input (the opsin's name). For the Anxa1 mice the dandiset's site\n#   labels are used for the outcome; how the recordings without a site suffix affect the result\n#   is shown as a variant (see cohort-sizes).\n#\n# Test statistics (t, W, F) that the paper reports are given in the statements and printed next\n# to the values found, but the outcomes rest on the direction and significance of each test:\n# the statistic depends on the exact window and pre-processing, which the paper does not give,\n# so a tolerance on it would test those choices, not the finding.\nschema_version: 1\ndandiset: \"001528\"\npaper: doi:10.1101/2025.06.03.657460\nclaims:\n- id: cohort-sizes\n  statement: The number of mice per experimental group is as given in the figure legends; SNr\n    GABA neurons STN 7 and PPN 8 (Figure 2); SNc pan-DA neurons STN 11 and PPN 9 (Figure 3);\n    GRAB-DA in TS and DLS, STN 6 and 7, PPN 9 and 9 (Figure 4); DA terminals in TS and DLS with\n    STN stimulation, 9 and 9 (Figure S3); Vglut2+ DA neurons STN 10 and PPN 10, Anxa1+ terminals\n    in DLS STN 8 and PPN 10 (Figure 5); Anxa1+ cell bodies in SNc STN 5 and PPN 4 (Figure S4).\n  source: Legends of Figures 2 to 5, S3 and S4\n  expected:\n  - {quantity: SNr GABA, STN, value: 7, tolerance: 0, unit: mice}\n  - {quantity: SNr GABA, PPN, value: 8, tolerance: 0, unit: mice}\n  - {quantity: SNc pan-DA, STN, value: 11, tolerance: 0, unit: mice}\n  - {quantity: SNc pan-DA, PPN, value: 9, tolerance: 0, unit: mice}\n  - {quantity: GRAB-DA TS, STN, value: 6, tolerance: 0, unit: mice}\n  - {quantity: GRAB-DA DLS, STN, value: 7, tolerance: 0, unit: mice}\n  - {quantity: GRAB-DA TS, PPN, value: 9, tolerance: 0, unit: mice}\n  - {quantity: GRAB-DA DLS, PPN, value: 9, tolerance: 0, unit: mice}\n  - {quantity: DA terminals TS, STN, value: 9, tolerance: 0, unit: mice}\n  - {quantity: DA terminals DLS, STN, value: 9, tolerance: 0, unit: mice}\n  - {quantity: Vglut2 SNc, STN, value: 10, tolerance: 0, unit: mice}\n  - {quantity: Vglut2 SNc, PPN, value: 10, tolerance: 0, unit: mice}\n  - {quantity: Anxa1 DLS, STN, value: 8, tolerance: 0, unit: mice}\n  - {quantity: Anxa1 DLS, PPN, value: 10, tolerance: 0, unit: mice}\n  - {quantity: Anxa1 SNc, STN, value: 5, tolerance: 0, unit: mice}\n  - {quantity: Anxa1 SNc, PPN, value: 4, tolerance: 0, unit: mice}\n  criterion: Mice with a usable durations recording, counted per group, input and site under the\n    dandiset's labels. The tolerance is 0, as these are counts of animals. Reproduced when all 16\n    counts match; partially reproduced when 12 to 15 match; not reproduced below 12. The counts\n    for the frequencies protocol, and the Anxa1 counts if the recordings without a site suffix\n    were DLS recordings, are reported as well.\n- id: fig2-gaba-excited\n  statement: Optogenetic stimulation of STN or PPN inputs increases SNr GABA neuron activity\n    (paired t-test on the 1 s train, STN t = 3.8, p = 0.008; PPN t = 9.2, p < 0.0001).\n  source: Results, second section; Figure 2B and 2E with insets\n  criterion: For 1 s 40 Hz trains, the mean dF/F during the train against the pre-stimulus\n    window, paired t-test across mice, per input. Reproduced when both inputs show a significant\n    increase; partially reproduced when one does; not reproduced otherwise.\n- id: fig2-gaba-frequency\n  statement: The SNr GABA response scales with stimulation frequency from 5 to 40 Hz (Friedman\n    test on 1 s trains, STN F = 21.0, p = 0.0001; PPN F = 18.2, p = 0.0004).\n  source: Results, second section; Figure 2C and 2F\n  criterion: For 1 s trains of the frequencies protocol, the Friedman test across 5, 10, 20 and\n    40 Hz of the mean dF/F during the train, per input. Reproduced when both inputs give p < 0.05\n    with the 40 Hz mean above the 5 Hz mean; partially reproduced when one does.\n- id: fig3b-da-stn-250ms-peak\n  statement: A 250 ms 40 Hz train of STN inputs elicits a net increase in SNc pan-DA neuron\n    activity that peaks after stimulus offset (latency to peak 0.50 +/- 0.03 s, mean +/- SEM).\n  source: Results, third section; Figure 3B\n  expected:\n  - quantity: Mean latency to peak after onset, STN, 250 ms train\n    value: 0.50\n    tolerance: 0.03\n    unit: s\n  criterion: Per mouse, the time of the maximum of the trial-averaged trace from onset to 2.25 s\n    after onset (the 2 s after offset); the mean over mice. The tolerance is the paper's SEM.\n    Reproduced when the mean latency is within tolerance and the mean dF/F over 0 to 1.25 s is\n    above 0 by a one-sample t-test; partially reproduced when the mean latency is after offset\n    (above 0.25 s) and the net response is positive, but outside tolerance; not reproduced\n    otherwise. The latency with a window ending 1.25 s after onset is shown as a variant.\n- id: fig3c-da-stn-duration\n  statement: For SNc pan-DA neurons the STN-evoked response varies with train duration; with 1\n    and 4 s trains an initial increase is followed by inhibition (Friedman test, F = 13.0, p =\n    0.005).\n  source: Results, third section; Figure 3B and 3C\n  criterion: The paper's F = 13.0 with p = 0.005 fits four groups, while three durations were\n    tested. Readings allowed (a) the mean dF/F during 0.25, 1 and 4 s trains (three groups);\n    (b) the same with the pre-stimulus window as a fourth group; (c) the area under the curve\n    during each train (three groups). Reproduced when the Friedman test gives p < 0.05 under one\n    reading and, for 4 s trains, the mean over 0 to 0.5 s is above the mean over the last 1 s of\n    the train (paired t-test p < 0.05); partially reproduced when only one of the two holds.\n- id: fig3d-da-stn-frequency-ns\n  statement: The amplitude of the SNc pan-DA response during STN stimulation does not scale with\n    frequency (Friedman test, F = 4.2, p = 0.24).\n  source: Results, third section; Figure 3D\n  criterion: A claim of absence, judged on the paper's test, the Friedman test across 5, 10, 20\n    and 40 Hz of the mean dF/F during 1 s trains of the frequencies protocol. Reproduced when p\n    >= 0.05; not reproduced when p < 0.05. The 0.25 s and 4 s trains are shown as variants.\n- id: fig3g-da-ppn-duration\n  statement: PPN stimulation also evokes SNc pan-DA responses that vary with train duration\n    (Friedman test, F = 11.5, p = 0.009).\n  source: Results, third section; Figure 3F and 3G\n  criterion: As fig3c-da-stn-duration for the Friedman test, with readings (a) to (c).\n    Reproduced when p < 0.05 under one reading; not reproduced otherwise.\n- id: fig3h-da-ppn-frequency-ns\n  statement: The SNc pan-DA response to PPN stimulation does not vary with frequency\n    (repeated-measures one-way ANOVA, F2,15 = 1.35, p = 0.28).\n  source: Results, third section; Figure 3H\n  criterion: A claim of absence, judged on the paper's test, a repeated-measures ANOVA\n    (Greenhouse-Geisser corrected) across 5, 10, 20 and 40 Hz of the mean dF/F during 1 s\n    trains. Reproduced when p >= 0.05; not reproduced when p < 0.05.\n- id: fig4cf-ts-dls-opposite\n  statement: STN or PPN stimulation evokes opposite DA release in TS (increase) and DLS\n    (decrease) (two-way ANOVA, striatal site, STN F1,11 = 40.9, PPN F1,16 = 36.4, p < 0.0001;\n    site by time interaction of the same size).\n  source: Results, fourth section; Figure 4C and 4F\n  criterion: GRAB-DA recordings, 1 s 40 Hz trains; a two-way mixed ANOVA with site between mice\n    and time (pre-stimulus window, train) within mice. Reproduced when, for both inputs, the\n    mean dF/F during the train is above 0 in TS and below 0 in DLS and the site by time\n    interaction has p < 0.05; partially reproduced when this holds for one input.\n- id: fig4dg-ts-frequency\n  statement: In TS, the DA increase evoked by either input scales with frequency, for all train\n    durations (STN, repeated-measures ANOVA, 0.25 s F2,8 = 7.5, 1 s F2,7 = 13.6, 4 s F2,9 = 16.9;\n    PPN, Friedman, F = 20.0, 24.0, 23.2).\n  source: Results, fourth section; Figure 4D and 4G; Figure S3C, S3D, S3I and S3J\n  criterion: For each input and train duration (six tests), the paper's test across 5, 10, 20\n    and 40 Hz of the mean dF/F during the train in TS. Reproduced when all six give p < 0.05 with\n    the 40 Hz mean above the 5 Hz mean; partially reproduced for three to five; not reproduced\n    below three.\n- id: fig4eh-dls-frequency\n  statement: In DLS, the DA inhibition scales with frequency and is most prominent at higher\n    frequencies (STN, repeated-measures ANOVA, 0.25 s F = 7.5, 1 s F = 12.8, 4 s F = 46.8; PPN,\n    0.25 s Friedman F = 12.3, 1 s and 4 s repeated-measures ANOVA F = 12.8 and 10.2).\n  source: Results, fourth section; Figure 4E and 4H; Figure S3E, S3F, S3K and S3L\n  criterion: For each input and train duration (six tests), the paper's test across 5, 10, 20\n    and 40 Hz of the mean dF/F during the train in DLS. Reproduced when all six give p < 0.05 with\n    the 40 Hz mean below the 5 Hz mean; partially reproduced for three to five; not reproduced\n    below three.\n- id: fig4eh-dls-5hz-increase\n  statement: Low-frequency (5 Hz) stimulation of either STN or PPN increases DLS dopamine.\n  source: Results, fourth section; Figure 4E and 4H; Figure S3F and S3L\n  criterion: For 1 s trains at 5 Hz, the mean dF/F during the train in DLS against 0, one-sample\n    t-test across mice, per input. Reproduced when both inputs give a mean above 0 with p < 0.05;\n    partially reproduced when one does. The 0.25 s and 4 s trains are shown as variants.\n- id: fig4cf-dls-rebound\n  statement: In DLS the DA inhibition is followed by a post-stimulus rebound above baseline.\n  source: Results, fourth section; Figure 4C and 4F\n  criterion: For 1 s 40 Hz trains, the mean dF/F in the 1 s after offset against 0, one-sample\n    t-test across mice, per input. Reproduced when both inputs give a mean above 0 with p < 0.05;\n    partially reproduced when one does.\n- id: figs3-terminals-opposite\n  statement: Calcium in DA terminals in TS and DLS shows opposite responses to STN stimulation,\n    as the GRAB-DA recordings do.\n  source: Results, fourth section; Figure S3N and S3O\n  criterion: DA terminal GCaMP recordings, 1 s 40 Hz trains; the mean dF/F during the train is\n    above 0 in TS and below 0 in DLS, and the two sites differ by a two-way mixed ANOVA site by\n    time interaction at p < 0.05. Reproduced when all hold; partially reproduced when the sites\n    differ but one site's sign is not as stated.\n- id: fig5-vglut2-excited\n  statement: Stimulation of STN or PPN inputs increases the activity of Vglut2+ DA neurons in SNc\n    (STN, Wilcoxon, 0.25 s W = 41, p = 0.012, 1 s W = 43, p = 0.008, 4 s W = -5, p = 0.82; PPN,\n    paired t-test, 0.25 s t = 2.9, p = 0.02, 1 s t = 3.4, p = 0.008, 4 s t = 3.0, p = 0.01).\n  source: Results, fifth section; Figure 5B, 5C, 5G and 5H; Figure S4A and S4D\n  criterion: Durations protocol; the mean dF/F during the train against the pre-stimulus window,\n    with the paper's test (Wilcoxon for STN, paired t-test for PPN). The claim rests on the 0.25\n    and 1 s trains of both inputs (four tests). Reproduced when all four show a significant\n    increase; partially reproduced for two or three; not reproduced otherwise. The 4 s trains\n    are reported.\n- id: fig5-vglut2-frequency\n  statement: The Vglut2+ DA neuron increase scales with frequency for short STN trains and for\n    all PPN durations (Friedman, STN 0.25 s F = 15.5, p = 0.001, 1 s F = 5.9, p = 0.11, 4 s F =\n    7.0, p = 0.07; PPN F = 18.8, 24.8, 20.2, p <= 0.0003).\n  source: Results, fifth section; Figure 5D, 5E, 5I and 5J\n  criterion: Friedman test across 5, 10, 20 and 40 Hz of the mean dF/F during the train. The\n    claim rests on STN 0.25 s and PPN 0.25, 1 and 4 s (four tests). Reproduced when all four\n    give p < 0.05 with the 40 Hz mean above the 5 Hz mean; partially reproduced for two or three;\n    not reproduced otherwise. STN 1 s and 4 s are reported.\n- id: fig5-anxa1-dls-inhibited\n  statement: In DLS terminals of SNc Anxa1+ neurons, STN and PPN stimulation produce inhibition\n    (STN, 0.25 s t = 6.4, p = 0.0004, 1 s W = -36, p = 0.005, 4 s W = -36, p = 0.008; PPN, 0.25 s\n    t = 3.9, p = 0.004, 1 s W = -55, p = 0.002, 4 s t = 3.8, p = 0.004).\n  source: Results, fifth section; Figure 5L, 5M, 5Q and 5R; Figure S4B and S4E\n  criterion: Durations protocol, Anxa1 recordings labeled DLS; the mean dF/F during the train\n    against the pre-stimulus window with the paper's test for each input and duration (six\n    tests). Reproduced when all six show a significant decrease; partially reproduced for three\n    to five; not reproduced below three. The result with the recordings without a site suffix\n    added to DLS is a variant.\n- id: fig5-anxa1-dls-frequency\n  statement: The Anxa1+ terminal inhibition scales with frequency (STN, 0.25 s F = 18.0, 1 s F =\n    15.5, 4 s F = 15.3; PPN, 0.25 s F = 11.5, 1 s F2,15 = 11.0, 4 s F2,18 = 7.2).\n  source: Results, fifth section; Figure 5N, 5O, 5S and 5T\n  criterion: Frequencies protocol, Anxa1 recordings labeled DLS; per input and duration (six\n    tests) the paper's test across 5, 10, 20 and 40 Hz of the mean dF/F during the train\n    (Friedman for STN and for PPN 0.25 s, repeated-measures ANOVA for PPN 1 s and 4 s).\n    Reproduced when all six give p < 0.05 with the 40 Hz mean below the 5 Hz mean; partially\n    reproduced for three to five; not reproduced below three.\n- id: fig5-anxa1-dls-rebound\n  statement: Anxa1+ terminals in DLS show a transient increase in activity at stimulus offset,\n    for both inputs.\n  source: Results, fifth section; Figure 5L and 5Q\n  criterion: Durations protocol, Anxa1 recordings labeled DLS, 1 s 40 Hz trains; the mean dF/F\n    in the 1 s after offset against 0, one-sample t-test. Reproduced when both inputs give a mean\n    above 0 with p < 0.05; partially reproduced when one does.\n- id: figs4-anxa1-soma-inhibited\n  statement: Anxa1+ SNc cell bodies show stimulation-induced inhibition (paired t-test, STN 0.25\n    s t = 3.1, 1 s t = 4.0, 4 s t = 7.2, n = 5; PPN t = 4.8, 8.4, 3.3, n = 4) followed by\n    post-stimulus rebound activation.\n  source: Results, fifth section; Figure S4C and S4F\n  criterion: Durations protocol, Anxa1 recordings labeled SNc; the mean dF/F during the train\n    against the pre-stimulus window, paired t-test, per input and duration (six tests).\n    Reproduced when all six show a significant decrease; partially reproduced for three to five;\n    not reproduced below three. The rebound (mean in the 1 s after offset of 1 s trains above 0)\n    is reported, and the result restricted to the mice with both a DLS and an SNc recording (the\n    paper's n) is a variant.\n- id: fig5-opposite-subtypes\n  statement: Excitatory inputs from STN and PPN activate PD-resilient Vglut2+ DA neurons but\n    inhibit PD-vulnerable Anxa1+ DA neurons.\n  source: Title; Abstract; Results, fifth section; Figure 5\n  criterion: For 1 s 40 Hz trains of the durations protocol, per input, the mean dF/F during the\n    train is above 0 for Vglut2 SNc recordings and below 0 for Anxa1 DLS recordings, and the two\n    groups differ by Welch's t-test at p < 0.05. Reproduced when this holds for both inputs;\n    partially reproduced for one.\n- id: fig1de-th-anxa1-reduced\n  statement: In human SNc, TH+ neurons (Mann-Whitney U = 2.0, p = 0.002) and TH+/ANXA1+ neurons\n    (U = 1.0, p < 0.0001) are fewer in PD cases (n = 7) than in controls (n = 12).\n  source: Results, first section; Figure 1D and 1E\n- id: fig1f-anxa1-de-enriched\n  statement: Among remaining DA neurons in PD, ANXA1+ neurons are de-enriched to 10 +/- 7% of\n    control, ALDH1A1+ to 41 +/- 12%, while CALB1+ neurons trend toward enrichment (301 +/- 103%).\n  source: Results, first section; Figure 1F\n- id: figs1-calb1-aldh1a1-counts\n  statement: TH+/CALB1+ neuron counts are not significantly changed in PD (U = 19.5, p = 0.08)\n    while TH+/ALDH1A1+ counts are reduced (U = 1.0, p < 0.0001).\n  source: Results, first section; Figure S1B to S1F\n- id: figs1-if-aldh1a1\n  statement: Immunofluorescence confirms fewer TH+ and TH+/ALDH1A1+ neurons and a lower fraction\n    of TH+ neurons expressing ALDH1A1 in PD (n = 11) than in controls (n = 15), and counts agree\n    with RNAscope in four cases processed both ways.\n  source: Results, first section; Figure S1G to S1J\n"
}
```

```
File created successfully at: claims/001528/10.1101-2025.06.03.657460.yaml (file state is current in your context — no need to Read it back)
```

**Agent**

Fixing the flow-style mappings (the commas in quantities would split them).

**Agent calls Bash**

```bash
python - <<'EOF'
import re
p='claims/001528/10.1101-2025.06.03.657460.yaml'
s=open(p).read()
s=re.sub(r'\{quantity: ([^,]+), (STN|PPN), value', r'{quantity: "\1, \2", value', s)
open(p,'w').write(s)
import yaml, json, jsonschema
d=yaml.safe_load(open(p))
print(d['claims'][0]['expected'][:2])
jsonschema.validate(d, json.load(open('schemas/claims.schema.json')))
print(len(d['claims']), 'ok')
EOF
```

```
[{'quantity': 'SNr GABA, STN', 'value': 7, 'tolerance': 0, 'unit': 'mice'}, {'quantity': 'SNr GABA, PPN', 'value': 8, 'tolerance': 0, 'unit': 'mice'}]
25 ok
```

**Agent**

Claims file validates (25 claims). Adding statistics helpers and a per-mouse response table to the helper module.

**Agent calls Bash**

```bash
cd entries/001528-hadjas-2025 && cat >> photometry.py <<'EOF'


# --- per-mouse response table ---------------------------------------------------------------

def recording_kind(rec: dict) -> str:
    """For Anxa1 mice: 'dual' for mice with separate DLS and SNc files (site in the session id),
    'single' for the files without a site suffix. Other groups: 'single'."""
    return "dual" if rec["session_id"].endswith(("_DLS", "_SNc")) else "single"


def response_table(recs: list[dict]) -> pd.DataFrame:
    """One row per recording and condition, with the response measures of the trial-averaged trace."""
    rows = []
    for rec in recs:
        for _, c in condition_traces(rec).iterrows():
            rows.append({"subject": rec["subject"], "group": rec["group"], "site": rec["site"],
                         "input": rec["input"], "protocol": rec["protocol"], "kind": recording_kind(rec),
                         "path": rec["path"], "duration": c.duration, "frequency": c.frequency,
                         "n_trials": c.n_trials, "n_dropped": c.n_dropped,
                         **response_measures(c.trace, c.t, c.duration)})
    return pd.DataFrame(rows)


# --- statistics -------------------------------------------------------------------------------

def paired_t(a, b) -> dict:
    from scipy import stats
    a, b = np.asarray(a, float), np.asarray(b, float)
    r = stats.ttest_rel(a, b)
    return {"test": "paired t", "n": len(a), "stat": float(r.statistic), "p": float(r.pvalue),
            "mean_diff": float(np.mean(a - b))}


def wilcoxon_w(a, b) -> dict:
    """Wilcoxon signed-rank test; `stat` is the sum of signed ranks (the W that GraphPad Prism
    reports), positive when a > b."""
    from scipy import stats
    d = np.asarray(a, float) - np.asarray(b, float)
    d = d[d != 0]
    ranks = stats.rankdata(np.abs(d))
    p = stats.wilcoxon(d).pvalue
    return {"test": "Wilcoxon", "n": len(d), "stat": float(np.sum(np.sign(d) * ranks)), "p": float(p),
            "mean_diff": float(np.mean(d))}


def friedman(matrix) -> dict:
    """Friedman test on a mice x conditions matrix (complete rows only)."""
    from scipy import stats
    m = np.asarray(matrix, float)
    m = m[np.isfinite(m).all(axis=1)]
    r = stats.friedmanchisquare(*m.T)
    return {"test": "Friedman", "n": m.shape[0], "stat": float(r.statistic), "p": float(r.pvalue)}


def rm_anova(matrix) -> dict:
    """One-way repeated-measures ANOVA on a mice x conditions matrix (complete rows only), with
    the Greenhouse-Geisser epsilon, corrected degrees of freedom and p-value."""
    from scipy import stats
    m = np.asarray(matrix, float)
    m = m[np.isfinite(m).all(axis=1)]
    n, k = m.shape
    grand = m.mean()
    ss_cond = n * ((m.mean(axis=0) - grand) ** 2).sum()
    ss_subj = k * ((m.mean(axis=1) - grand) ** 2).sum()
    ss_err = ((m - grand) ** 2).sum() - ss_cond - ss_subj
    df1, df2 = k - 1, (k - 1) * (n - 1)
    f = (ss_cond / df1) / (ss_err / df2)
    s = np.cov(m, rowvar=False)
    c = np.eye(k) - 1.0 / k
    sc = c @ s @ c
    eps = np.trace(sc) ** 2 / ((k - 1) * np.trace(sc @ sc))
    return {"test": "RM ANOVA (GG)", "n": n, "stat": float(f), "df1": float(eps * df1), "df2": float(eps * df2),
            "epsilon": float(eps), "p": float(stats.f.sf(f, eps * df1, eps * df2)),
            "p_uncorrected": float(stats.f.sf(f, df1, df2))}


def mixed_2x2(pre_a, during_a, pre_b, during_b) -> dict:
    """Two-way mixed ANOVA with two groups of mice (a, b) and two within-mouse levels (pre,
    during). For a 2 x 2 design the group effect is the pooled two-sample t-test on each mouse's
    mean over the two levels, squared, and the interaction is that on the difference, squared."""
    from scipy import stats
    pa, da, pb, db = (np.asarray(x, float) for x in (pre_a, during_a, pre_b, during_b))
    site = stats.ttest_ind((pa + da) / 2, (pb + db) / 2)
    inter = stats.ttest_ind(da - pa, db - pb)
    df2 = len(pa) + len(pb) - 2
    return {"test": "mixed ANOVA", "df": (1, df2), "F_site": float(site.statistic ** 2), "p_site": float(site.pvalue),
            "F_interaction": float(inter.statistic ** 2), "p_interaction": float(inter.pvalue)}
EOF
cd $TMPDIR && . scratch/bin/activate && python - <<'EOF'
import sys, numpy as np
sys.path.insert(0, 'entries/001528-hadjas-2025')
import photometry as ph
import pingouin
EOF
uv pip install -q pingouin 2>&1 | tail -1; python - <<'EOF'
import sys, numpy as np, pandas as pd
sys.path.insert(0, 'entries/001528-hadjas-2025')
import photometry as ph, pingouin as pg
rng = np.random.default_rng(0)
m = rng.normal(size=(9,4)) + np.array([0,0.3,0.8,1.5]) + rng.normal(size=(9,1))
m[:,3] += rng.normal(scale=2, size=9)
print(ph.rm_anova(m))
df = pd.DataFrame(m).reset_index().melt(id_vars='index')
print(pg.rm_anova(df, dv='value', within='variable', subject='index', correction=True))
a = rng.normal(1,1,7); b = rng.normal(-1,1,6)
print(ph.mixed_2x2(np.zeros(7)+rng.normal(0,.1,7), a, np.zeros(6)+rng.normal(0,.1,6), b))
pre_a = np.zeros(7)+rng.normal(0,.1,7); pre_b=np.zeros(6)+rng.normal(0,.1,6)
L = pd.DataFrame({'s': list(range(7))*2+list(range(7,13))*2, 'g': ['a']*14+['b']*12, 't': ['pre']*7+['d']*7+['pre']*6+['d']*6, 'v': np.r_[pre_a, a, pre_b, b]})
print(ph.mixed_2x2(pre_a, a, pre_b, b)); print(pg.mixed_anova(L, dv='v', within='t', between='g', subject='s'))
print(ph.wilcoxon_w([1,2,3,4,5,6,7,8,9],[0]*9))
EOF
```

```
Traceback (most recent call last):
  File "<stdin>", line 4, in <module>
ModuleNotFoundError: No module named 'pingouin'
{'test': 'RM ANOVA (GG)', 'n': 9, 'stat': 8.681162024634098, 'df1': 1.2601179417142179, 'df2': 10.080943533713743, 'epsilon': 0.42003931390473925, 'p': 0.011257694581584916, 'p_uncorrected': 0.0004451111246121756}
     Source  ddof1  ddof2         F  ...       eps  sphericity  W_spher   p_spher
0  variable      3     24  8.681162  ...  0.420039       False  0.06362  0.002646

[1 rows x 11 columns]
{'test': 'mixed ANOVA', 'df': (1, 11), 'F_site': 6.836171349662812, 'p_site': 0.024058973426341335, 'F_interaction': 6.328863318646241, 'p_interaction': 0.02869294722237323}
{'test': 'mixed ANOVA', 'df': (1, 11), 'F_site': 6.741282895587287, 'p_site': 0.024853103493555975, 'F_interaction': 6.535839066249868, 'p_interaction': 0.026683064244430357}
        Source        SS  DF1  DF2        MS         F     p_unc       np2  eps
0            g  2.898914    1   11  2.898914  6.741283  0.024853  0.379977  NaN
1            t  0.012389    1   11  0.012389  0.022310  0.883969  0.002024  1.0
2  Interaction  3.629516    1   11  3.629516  6.535839  0.026683  0.372713  1.0
{'test': 'Wilcoxon', 'n': 9, 'stat': 45.0, 'p': 0.00390625, 'mean_diff': 5.0}
Shell cwd was reset to
```

**Agent**

The stats helpers agree with pingouin on synthetic data (RM ANOVA F and Greenhouse-Geisser epsilon, mixed ANOVA F). Now writing the notebook.

**Agent calls Bash**

```bash
mkdir -p $TMPDIR/gen && cat > $TMPDIR/gen/build.py <<'PYEOF'
import nbformat as nbf
cells = []
def md(s, tags=None):
    c = nbf.v4.new_markdown_cell(s.strip("\n"))
    if tags: c.metadata["tags"] = tags
    cells.append(c)
def code(s, tags=None):
    c = nbf.v4.new_code_cell(s.strip("\n"))
    if tags: c.metadata["tags"] = tags
    cells.append(c)
exec(open(__file__.replace("build.py", "cells.py")).read())
nb = nbf.v4.new_notebook()
nb.cells = cells
nb.metadata = {"kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"}}
nbf.write(nb, "entries/001528-hadjas-2025/reproduce_hadjas_2025.ipynb")
print(len(cells), "cells")
PYEOF
echo ok
```

```
ok
```

**Agent calls Write**

```json
{
 "file_path": "/tmp/claude-1001/gen/cells.py",
 "content": "md(r'''\n# Reproducing Hadjas et al. (2025) from dandiset 001528\n\n**Paper.** Hadjas LC, Kollman GJ, Linderhof L, Xia M, Mansur S, Saint-Pierre M, Lim B, Lee EB,\nCicchetti F, Awatramani R, Hollon NG, Hnasko TS (2025). Parkinson's Disease-vulnerable and\n-resilient dopamine neurons display opposite responses to excitatory input. bioRxiv,\n[doi:10.1101/2025.06.03.657460](https://doi.org/10.1101/2025.06.03.657460). This attempt used the\nfull text of the preprint (version 1, CC BY), which has no data or code availability statement.\n\n**Dandiset.** [DANDI:001528](https://dandiarchive.org/dandiset/001528/draft), version `draft`.\nThe dandiset has no published version, and the paper cites none, so the draft is the only version\nthere is. The draft read here was last modified on 2026-09-01T15:27:47Z (290 assets); the first\ncell below checks the draft's modification time against that and prints whether it has changed.\nA draft can change, so the numbers below hold for that state of it.\n\n**What the dandiset holds.** Fiber photometry with optogenetic stimulation of STN or PPN inputs\nto the substantia nigra in 120 mice: SNr GABA neurons, SNc pan-DA neurons, GRAB-DA in DLS and TS,\nDA terminals in DLS and TS, Vglut2+ DA neurons and Anxa1+ DA neurons (Figures 2 to 5, S3, S4).\nEach file holds the lab's dF/F, the 465 and 405 nm signals and the stimulation epochs. The human\ntissue counts of Figure 1 and Figure S1 are not in it.\n\n**Code read.** The dandiset links its conversion code,\n[catalystneuro/hnasko-lab-to-nwb](https://github.com/catalystneuro/hnasko-lab-to-nwb) at commit\ndeaefa7b1776a5ffb98fd50c5ff4d7b899bdaf59 (the `lotfi_2025` conversion, its metadata, and a\nPython re-implementation of the lab's MATLAB pipeline with a description of the MATLAB scripts),\nand an example notebook in [dandi/example-notebooks](https://github.com/dandi/example-notebooks)\nat commit 77a123e54e0d185e37768603da1faff79b62421f (`001528/HnaskoLab/Lotfi_2025`), which shows\nhow to load the files. The lab's MATLAB scripts are not public.\n\n**Outside inputs.** None. Groups, inputs and sites come from the files' own metadata.\n\nNo random numbers are drawn anywhere in this notebook.\n\n| Claim | Data | Status |\n|---|---|---|\n| cohort-sizes | dandiset | tested |\n| fig2-gaba-excited | dandiset | tested |\n| fig2-gaba-frequency | dandiset | tested |\n| fig3b-da-stn-250ms-peak | dandiset | tested |\n| fig3c-da-stn-duration | dandiset | tested |\n| fig3d-da-stn-frequency-ns | dandiset | tested |\n| fig3g-da-ppn-duration | dandiset | tested |\n| fig3h-da-ppn-frequency-ns | dandiset | tested |\n| fig4cf-ts-dls-opposite | dandiset | tested |\n| fig4dg-ts-frequency | dandiset | tested |\n| fig4eh-dls-frequency | dandiset | tested |\n| fig4eh-dls-5hz-increase | dandiset | tested |\n| fig4cf-dls-rebound | dandiset | tested |\n| figs3-terminals-opposite | dandiset | tested |\n| fig5-vglut2-excited | dandiset | tested |\n| fig5-vglut2-frequency | dandiset | tested |\n| fig5-anxa1-dls-inhibited | dandiset | tested |\n| fig5-anxa1-dls-frequency | dandiset | tested |\n| fig5-anxa1-dls-rebound | dandiset | tested |\n| figs4-anxa1-soma-inhibited | dandiset | tested |\n| fig5-opposite-subtypes | dandiset | tested |\n| fig1de-th-anxa1-reduced, fig1f-anxa1-de-enriched, figs1-calb1-aldh1a1-counts, figs1-if-aldh1a1 (human tissue) | dandiset | blocked: data missing |\n''')\n\ncode(r'''\nimport time\nimport warnings\n\nimport matplotlib.pyplot as plt\nimport numpy as np\nimport pandas as pd\nfrom scipy import stats\n\nimport photometry as ph\n\npd.set_option(\"display.width\", 220)\npd.set_option(\"display.max_columns\", 40)\npd.set_option(\"display.max_rows\", 300)\nwarnings.filterwarnings(\"ignore\", category=RuntimeWarning)\n\nstarted = time.time()\nversion = ph.check_version()\nprint(\"Dandiset\", ph.DANDISET_ID, \"version\", ph.DANDISET_VERSION, \"| draft modified\", version[\"modified\"],\n      \"| assets\", version[\"asset_count\"], \"| same as the pinned draft (\", ph.DRAFT_MODIFIED, \"):\", version[\"matches_pinned\"])\nrecs = ph.load_all()\nprint(f\"loaded {len(recs)} NWB files in {time.time() - started:.0f} s\")\n''')\n\nmd(r'''\n## Data check\n\nEach check of the metadata against the values is stated under its output.\n''')\n\ncode(r'''\ninfo = pd.DataFrame([{k: r[k] for k in [\"path\", \"subject\", \"subject_id_raw\", \"group\", \"site\", \"input\", \"protocol\",\n                                        \"session_id\", \"sex\", \"genotype\", \"raw_rate\", \"session_start\"]}\n                     | {\"kind\": ph.recording_kind(r), \"fp_table\": \"/\".join(r[\"fp_table_locations\"])} for r in recs])\nprint(\"NWB files:\", len(info), \"| mice:\", info.subject.nunique(), \"| groups per mouse (max):\", info.groupby(\"subject\").group.nunique().max())\nprint(\"\\nMice per group, input, recorded site and protocol:\")\nprint(info.groupby([\"group\", \"input\", \"site\", \"protocol\"]).subject.nunique().unstack().to_string())\nprint(\"\\nGenotype per group:\")\nprint(info.groupby(\"group\").genotype.unique().to_string())\nprint(\"\\nSex per group (mice):\")\nprint(info.drop_duplicates(\"subject\").groupby([\"group\", \"sex\"]).size().unstack(fill_value=0).to_string())\nprint(\"\\nRaw sampling rate (Hz) per group:\")\nprint(info.groupby([\"group\", \"raw_rate\"]).subject.nunique().unstack(fill_value=0).to_string())\nprint(\"\\nSubject ids written in lower case in the files:\", sorted(info[info.subject_id_raw != info.subject].subject_id_raw.unique()))\nprint(\"Session start time zone offsets:\", info.session_start.str[-6:].value_counts().to_dict())\n''', tags=[\"sanity\"])\n\nmd(r'''\nThe files hold 120 mice, each in one group, which fits the dandiset's summary (120 subjects). The\ngroup of each file is read from its experiment description, the site from the name of its dF/F\nseries, and the input from the name of its opsin (ChrimsonR in STN or PPN). For the Anxa1 mice,\nnine have separate DLS and SNc files (session ids ending in `_DLS` and `_SNc`), and nine have one\npair of files without a site suffix, whose dF/F series and raw signal are named SNc; the fiber\nphotometry table of every Anxa1 file lists both an SNc and a DLS fiber. Every session start time\nhas the offset -00:01, the local mean time of London that `pytz` gives when a time zone is\nattached with `replace`; the true offset is lost (a metadata error, it does not affect the\nanalysis). Eight subject ids are written in lower case (`c3015` and others) while the others are\nupper case.\n''')\n\ncode(r'''\nrows = []\nfor r in recs:\n    dt = np.diff(r[\"dff_t\"])\n    rows.append({\"path\": r[\"path\"], \"protocol\": r[\"protocol\"], \"dff_unit\": r[\"dff_unit\"], \"gc_unit\": r[\"gc_unit\"],\n                 \"n\": len(r[\"dff\"]), \"t0\": r[\"dff_t\"][0], \"dt_median_ms\": 1000 * np.median(dt),\n                 \"regular\": bool(np.all(np.abs(dt - 0.01) < 1e-6) or (np.abs(dt[dt < 1] - 0.01) < 1e-6).all()),\n                 \"longest_gap_s\": dt.max(), \"same_times\": np.array_equal(r[\"dff_t\"], r[\"gc_t\"]) and np.array_equal(r[\"dff_t\"], r[\"af_t\"]),\n                 \"timestamps\": r[\"dff_has_timestamps\"], \"nan_frac\": np.isnan(r[\"dff\"]).mean(),\n                 \"dff_p01\": np.nanpercentile(r[\"dff\"], 0.1), \"dff_p999\": np.nanpercentile(r[\"dff\"], 99.9),\n                 \"gc_median\": np.nanmedian(r[\"gc\"]), \"af_median\": np.nanmedian(r[\"af\"])})\nseries = pd.DataFrame(rows)\nprint(\"Stated units of dF/F and of the 465 nm signal:\", series.dff_unit.unique().tolist(), series.gc_unit.unique().tolist())\nprint(\"All 100 Hz series start at 0 s:\", bool((series.t0 == 0).all()), \"| median sample interval (ms):\", series.dt_median_ms.round(4).unique().tolist())\nprint(\"dF/F, 465 and 405 nm series share one time base in every file:\", bool(series.same_times.all()))\nprint(\"Files whose dF/F has explicit timestamps:\", int(series.timestamps.sum()), \"of\", len(series))\nprint(\"Files with a gap in time above 1 s:\", int((series.longest_gap_s > 1).sum()), \"; longest gaps (s):\", series.longest_gap_s.nlargest(3).round(1).tolist())\nprint(\"Files with missing dF/F values:\", int((series.nan_frac > 0).sum()), \"; by protocol:\", series[series.nan_frac > 0].protocol.value_counts().to_dict(),\n      \"; largest fraction:\", round(series.nan_frac.max(), 3))\nprint(\"dF/F 0.1th percentile across files: %.1f to %.1f; 99.9th percentile: %.1f to %.1f\" %\n      (series.dff_p01.min(), series.dff_p01.max(), series.dff_p999.min(), series.dff_p999.max()))\nprint(\"465 nm median across files: %.4f to %.4f; 405 nm: %.4f to %.4f (a.u.)\" %\n      (series.gc_median.min(), series.gc_median.max(), series.af_median.min(), series.af_median.max()))\n''', tags=[\"sanity\"])\n\nmd(r'''\nAll 100 Hz series start at 0 s and are sampled every 10 ms; the dF/F and the two signals share\none time base. Some files of the frequencies protocol join separate recordings: their timestamps\njump (up to about two days, below) and the joins are filled with missing values. The dF/F is\nstated in \"a.u.\", and the series description gives (Gc - fitted_af) / fitted_af; its values (for\nexample 99.9th percentiles of 1.7 to 249) are in percent, as in the MATLAB pipeline (`dF = 100 *\n(Gc - fit) / fit`), and the recomputation below confirms this. The unit is a metadata error; the\nanalysis uses the values as percent.\n''')\n\ncode(r'''\neps = []\nfor r in recs:\n    e = ph.label_epochs(r).assign(path=r[\"path\"], group=r[\"group\"], protocol=r[\"protocol\"])\n    eps.append(e)\neps = pd.concat(eps, ignore_index=True)\nprint(\"Stimulation power (mW) and wavelength (nm) in the epoch tables:\", sorted(eps.power_mW.unique()), sorted(eps.wavelength_nm.unique()))\nprint(\"\\nEpochs per protocol, train duration and frequency (files, epochs, dropped as not a train, outside the signal, not contiguous):\")\ntab = eps.groupby([\"protocol\", \"duration\", \"frequency\"]).agg(\n    files=(\"path\", \"nunique\"), epochs=(\"start\", \"size\"), not_train=(\"is_train\", lambda x: int((~x).sum())),\n    outside=(\"in_signal\", lambda x: int((~x).sum())), not_contiguous=(\"contiguous\", lambda x: int((~x).sum())),\n    usable=(\"usable\", \"sum\"), with_missing=(\"nan_in_window\", \"sum\"))\nprint(tab.to_string())\nper_file = eps[eps.usable].groupby([\"path\", \"protocol\", \"duration\", \"frequency\"]).size().rename(\"trials\").reset_index()\nprint(\"\\nTrials per file and condition:\", per_file.trials.value_counts().sort_index().to_dict())\nten = sorted(per_file[per_file.trials >= 10].path.str.split(\"/\").str[0].unique())\nprint(\"Files with 10 trials per condition belong to\", len(ten), \"mice:\", ten)\nsixteen = eps[eps.duration == 16.0].path.str.split(\"/\").str[0].unique()\nprint(\"Mice with 16 s trains:\", len(sixteen), \"| groups:\", eps[eps.duration == 16.0].group.unique().tolist())\nfour = eps[(eps.protocol == \"frequencies\") & (eps.duration == 4.0)].path.nunique()\nprint(\"Frequencies-protocol files with 4 s trains:\", four, \"of\", eps[eps.protocol == \"frequencies\"].path.nunique())\nprint(\"Number of pulses against frequency x duration (median ratio):\",\n      round(float(np.median(eps[eps.usable].pulses / (eps[eps.usable].frequency * eps[eps.usable].duration))), 3))\nprint(\"Train lengths within 15 ms of the labelled duration:\", round(float((np.abs(eps[eps.usable].length - eps[eps.usable].duration) < 0.015).mean()), 3))\n''', tags=[\"sanity\"])\n\nmd(r'''\nThe epoch tables give 5 mW at 635 nm for every train, as the Methods state. The number of pulses\nin each train fits its frequency and length. Three things differ from the Methods. First, 13 mice\n(the files with the older 24 kHz raw rate) have 10 trials per condition, where the Methods state\n5, and their durations sessions also hold 16 s trains, which the paper does not mention. Second,\nin those mice's frequencies sessions there are no 4 s trains. Third, the Methods give an\ninterval of 20 s between trains in the frequencies sessions, while the conversion code's session\ndescription says 10 s; the epoch starts show about 20 s. A few epochs are dropped: three\nzero-length entries and seven trains whose window runs past the end of the recording. The\nconversion code (`convert_session.py`) names the 1 s block of the STN to SNr GABA frequencies\nsessions `s1s10mW`, which suggests 10 mW, while the epoch table and the Methods give 5 mW; the\ndata cannot settle this.\n''')\n\ncode(r'''\n# Recordings deposited twice: identical dF/F, or near-identical traces of the same length.\nmd5 = pd.Series({r[\"path\"]: r[\"dff_md5\"] for r in recs})\nprint(\"Files sharing an identical dF/F array:\", int(md5.duplicated(keep=False).sum()))\nby_len = {}\nfor r in recs:\n    by_len.setdefault(len(r[\"dff\"]), []).append(r)\npairs = []\nfor n, rs in by_len.items():\n    for i in range(len(rs)):\n        for j in range(i + 1, len(rs)):\n            a, b = rs[i][\"dff\"], rs[j][\"dff\"]\n            ok = np.isfinite(a) & np.isfinite(b)\n            if ok.sum() > 100 and np.corrcoef(a[ok], b[ok])[0, 1] > 0.99:\n                pairs.append((rs[i][\"path\"], rs[j][\"path\"]))\nprint(\"Pairs of same-length files with dF/F correlation above 0.99:\", pairs)\nstarts = info.groupby([\"subject\", \"session_start\"]).size()\nprint(\"Mice with two files starting at the same time:\", starts[starts > 1].index.tolist())\n''', tags=[\"sanity\"])\n\nmd(r'''\nNo recording is deposited twice: no two files share a dF/F array, no two files of the same\nlength have nearly the same trace, and no mouse has two files with the same start time. Each\nrecording is counted once.\n''')\n\ncode(r'''\nt0 = time.time()\nrec_rows = []\nfor r in recs:\n    x = ph.recompute_dff(r[\"gc\"], r[\"af\"], r[\"dff_t\"])\n    ok = np.isfinite(x) & np.isfinite(r[\"dff\"])\n    rec_rows.append({\"path\": r[\"path\"], \"protocol\": r[\"protocol\"], \"r\": np.corrcoef(x[ok], r[\"dff\"][ok])[0, 1],\n                     \"median_abs_diff\": np.median(np.abs(x[ok] - r[\"dff\"][ok])), \"dff_sd\": np.nanstd(r[\"dff\"])})\nrecomp = pd.DataFrame(rec_rows)\nprint(f\"recomputed dF/F for {len(recomp)} files in {time.time() - t0:.0f} s\")\nprint(recomp.groupby(\"protocol\").agg(files=(\"r\", \"size\"), r_median=(\"r\", \"median\"), r_min=(\"r\", \"min\"),\n                                      above_0_99=(\"r\", lambda x: int((x > 0.99).sum())),\n                                      abs_diff_median=(\"median_abs_diff\", \"median\")).round(4).to_string())\nprint(\"\\nLowest correlations:\")\nprint(recomp.nsmallest(6, \"r\").round(3).to_string(index=False))\n''', tags=[\"sanity\"])\n\nmd(r'''\nThe stored dF/F agrees with a recomputation from the stored 465 and 405 nm signals following the\nMethods (biexponential fit of the 405 nm signal, scaled to the 465 nm signal by robust\nregression, in percent): the median correlation and difference are printed above. This is\nconsistent with the stored series being the lab's dF/F in percent. Where they differ most the\nfit of a segment differs (the lab's exact fitting options are not public); the analysis uses the\nstored dF/F.\n''')\n\ncode(r'''\n# Clock check: responses at the true onsets against onsets shifted by -3 s and +3 s (within the\n# 10 to 20 s between trains). Per recording, the mean over conditions of |during - pre|.\ndef abs_response(r, shift):\n    ct = ph.condition_traces(r, shift=shift)\n    vals = [abs(ph.window_mean(c.trace, c.t, 0, c.duration) - ph.window_mean(c.trace, c.t, -c.duration, 0))\n            for _, c in ct.iterrows()]\n    return float(np.mean(vals)) if vals else np.nan\n\nclock = pd.DataFrame([{\"path\": r[\"path\"], \"group\": r[\"group\"], \"site\": r[\"site\"], \"protocol\": r[\"protocol\"],\n                       **{f\"shift_{s:+.0f}\": abs_response(r, s) for s in (0.0, -3.0, 3.0)}} for r in recs])\nclock[\"ratio\"] = clock[\"shift_+0\"] / clock[[\"shift_-3\", \"shift_+3\"]].max(axis=1)\nprint(\"Median |during - pre| (% dF/F) at true and shifted onsets, and the median ratio true / largest shifted:\")\nprint(clock.groupby([\"group\", \"protocol\"])[[\"shift_+0\", \"shift_-3\", \"shift_+3\", \"ratio\"]].median().round(2).to_string())\nprint(\"\\nRecordings whose true-onset response exceeds both shifted ones:\", int((clock.ratio > 1).sum()), \"of\", len(clock))\nprint(\"Recordings where it does not (the clock could not be shown from the response):\")\nprint(clock[clock.ratio <= 1][[\"path\", \"group\", \"site\", \"shift_+0\", \"shift_-3\", \"shift_+3\"]].round(2).to_string(index=False))\n''', tags=[\"sanity\"])\n\nmd(r'''\nFor every group the response at the true onsets is several times that at onsets shifted by 3 s\neither way, so the epoch tables share the clock of the dF/F. The recordings listed last are\nthose where the response at the true onsets does not exceed the shifted ones; there the clock\ncould not be shown from the data, and these recordings are used as they are. The shared time\nbase of the files (above) is consistent with this.\n''')\n\ncode(r'''\n# The Anxa1 recordings: the mice with DLS and SNc files, and those with one unsuffixed file.\nanx = []\nfor r in recs:\n    if r[\"group\"] != \"Anxa1\":\n        continue\n    ct = ph.condition_traces(r)\n    c = ct[(ct.duration == 1.0) & (ct.frequency == 40.0)].iloc[0]\n    m = ph.response_measures(c.trace, c.t, 1.0)\n    anx.append({\"subject\": r[\"subject\"], \"input\": r[\"input\"], \"protocol\": r[\"protocol\"], \"kind\": ph.recording_kind(r),\n                \"site\": r[\"site\"], \"label\": r[\"site\"] if ph.recording_kind(r) == \"dual\" else \"unsuffixed (SNc)\",\n                \"dff_sd\": np.nanstd(r[\"dff\"]), \"during_1s\": m[\"during\"], \"post_1s\": m[\"post\"], \"start\": r[\"session_start\"][:10]})\nanx = pd.DataFrame(anx)\nprint(\"Mice per input and kind of Anxa1 recording:\")\nprint(anx[anx.protocol == \"durations\"].groupby([\"input\", \"label\"]).subject.nunique().unstack().to_string())\nprint(\"\\nMedian over mice (durations protocol, 1 s 40 Hz trains, % dF/F):\")\nprint(anx[anx.protocol == \"durations\"].groupby(\"label\")[[\"dff_sd\", \"during_1s\", \"post_1s\"]].median().round(2).to_string())\n''', tags=[\"sanity\"])\n\nmd(r'''\nThe paper reports Anxa1+ DLS terminals in 8 (STN) and 10 (PPN) mice and SNc cell bodies in 5 and\n4. The dandiset holds DLS recordings for 5 and 4 mice, the mice that also have an SNc file, and\nSNc-labeled recordings for 8 and 10. The paper's DLS counts equal the dandiset's mice with a DLS\nfile plus those with an unsuffixed file (5 + 3 and 4 + 6), and its SNc counts equal the mice with\nboth files. Two explanations fit the counts: the unsuffixed recordings are DLS recordings\nlabelled SNc, or the dandiset lacks the DLS recordings of nine mice and holds SNc recordings the\npaper did not analyse (\"cell body signals were only detected in a subset of mice\"). The signals\nfavour the second: the unsuffixed recordings resemble the SNc recordings of the dual mice (small\ninhibition, no rebound, similar variability), not their DLS recordings (larger inhibition and a\nrebound). This is consistent with, but does not prove, that the labels are right and that DLS\nrecordings of nine mice are missing. The analysis keeps the dandiset's labels and shows the\nother reading as a variant.\n''')\n\ncode(r'''\nR = ph.response_table(recs)\nprint(\"Response table:\", len(R), \"recording x condition rows;\", R.subject.nunique(), \"mice\")\nprint(\"Trials per mouse and condition:\", R.n_trials.value_counts().sort_index().to_dict(), \"| dropped trials:\", int(R.n_dropped.sum()))\nfor col in [\"during\", \"pre\", \"post\"]:\n    print(f\"{col}: {R[col].min():.2f} to {R[col].max():.2f} % dF/F\")\nprint(\"Peak latency range (s):\", R.peak_latency.min(), \"to\", R.peak_latency.max())\n''', tags=[\"sanity\"])\n\nmd(r'''\nThe response measures, per mouse and condition, are computed once here and used by every claim.\n''')\n\ncode(r'''\ndef cohort(group, inp, site=None, protocol=\"durations\", duration=1.0, frequency=40.0, kind=None):\n    \"\"\"One row per mouse: the response measures for one condition.\"\"\"\n    q = (R.group == group) & (R.input == inp) & (R.protocol == protocol) & np.isclose(R.duration, duration) & np.isclose(R.frequency, frequency)\n    if site is not None:\n        q &= R.site == site\n    if kind is not None:\n        q &= R.kind == kind\n    out = R[q]\n    assert not out.subject.duplicated().any(), \"a mouse appears twice\"\n    return out.set_index(\"subject\")\n\ndef freq_matrix(group, inp, duration, site=None, kind=None, measure=\"during\"):\n    \"\"\"Mice x frequency (5, 10, 20, 40 Hz) matrix of one measure, frequencies protocol.\"\"\"\n    q = (R.group == group) & (R.input == inp) & (R.protocol == \"frequencies\") & np.isclose(R.duration, duration)\n    if site is not None:\n        q &= R.site == site\n    if kind is not None:\n        q &= R.kind == kind\n    m = R[q].pivot_table(index=\"subject\", columns=\"frequency\", values=measure)\n    return m.reindex(columns=list(ph.FREQUENCIES))\n\ndef fmt(res):\n    keep = {k: (round(v, 4) if isinstance(v, float) else v) for k, v in res.items()}\n    return \", \".join(f\"{k} {v}\" for k, v in keep.items())\n\ndef plot_traces(ax, group, inp, site=None, protocol=\"durations\", duration=1.0, frequency=40.0, kind=None, label=None):\n    q = (R.group == group) & (R.input == inp) & (R.protocol == protocol) & np.isclose(R.duration, duration) & np.isclose(R.frequency, frequency)\n    if site is not None:\n        q &= R.site == site\n    if kind is not None:\n        q &= R.kind == kind\n    paths = R[q].path.tolist()\n    traces = []\n    for r in recs:\n        if r[\"path\"] in paths:\n            ct = ph.condition_traces(r)\n            c = ct[np.isclose(ct.duration, duration) & np.isclose(ct.frequency, frequency)].iloc[0]\n            traces.append(c.trace)\n            t = c.t\n    m = np.vstack(traces)\n    mean, sem = np.nanmean(m, axis=0), np.nanstd(m, axis=0) / np.sqrt(len(m))\n    ax.plot(t, mean, label=f\"{label or site} (n={len(m)})\")\n    ax.fill_between(t, mean - sem, mean + sem, alpha=0.3)\n    ax.axvspan(0, duration, color=\"red\", alpha=0.08)\n    ax.set_xlim(-3, 8)\n    return float(np.nanmin(mean)), float(np.nanmax(mean))\n''')\n\n# ---------------------------------------------------------------------------------------------\nmd(r'''\n## cohort-sizes\n\n> The number of mice per experimental group is as given in the figure legends.\n''')\n\ncode(r'''\npaper_n = {(\"GABA\", \"STN\", \"SNr\"): 7, (\"GABA\", \"PPN\", \"SNr\"): 8, (\"panDA\", \"STN\", \"SNc\"): 11, (\"panDA\", \"PPN\", \"SNc\"): 9,\n           (\"GRABDA\", \"STN\", \"TS\"): 6, (\"GRABDA\", \"STN\", \"DLS\"): 7, (\"GRABDA\", \"PPN\", \"TS\"): 9, (\"GRABDA\", \"PPN\", \"DLS\"): 9,\n           (\"DAterm\", \"STN\", \"TS\"): 9, (\"DAterm\", \"STN\", \"DLS\"): 9, (\"Vglut2\", \"STN\", \"SNc\"): 10, (\"Vglut2\", \"PPN\", \"SNc\"): 10,\n           (\"Anxa1\", \"STN\", \"DLS\"): 8, (\"Anxa1\", \"PPN\", \"DLS\"): 10, (\"Anxa1\", \"STN\", \"SNc\"): 5, (\"Anxa1\", \"PPN\", \"SNc\"): 4}\ndur_n = R[R.protocol == \"durations\"].groupby([\"group\", \"input\", \"site\"]).subject.nunique()\nfreq_n = R[R.protocol == \"frequencies\"].groupby([\"group\", \"input\", \"site\"]).subject.nunique()\nalt = R[(R.protocol == \"durations\") & (R.group == \"Anxa1\")].assign(\n    site_alt=lambda d: np.where(d.kind == \"single\", \"DLS\", d.site)).groupby([\"input\", \"site_alt\"]).subject.nunique()\nctab = pd.DataFrame([{\"group\": g, \"input\": i, \"site\": s, \"paper\": n, \"dandiset_durations\": int(dur_n.get((g, i, s), 0)),\n                      \"dandiset_frequencies\": int(freq_n.get((g, i, s), 0)),\n                      \"anxa1_unsuffixed_as_DLS\": int(alt.get((i, s), 0)) if g == \"Anxa1\" else np.nan} for (g, i, s), n in paper_n.items()])\nctab[\"match\"] = ctab.paper == ctab.dandiset_durations\nprint(ctab.to_string(index=False))\nprint(\"\\nCounts matching:\", int(ctab.match.sum()), \"of\", len(ctab))\nif True:\n    a = ctab[ctab.group == \"Anxa1\"]\n    print(\"Anxa1 counts matching if the unsuffixed recordings were DLS:\", int((a.paper == a.anxa1_unsuffixed_as_DLS).sum()), \"of\", len(a))\nprint(\"Mice by sex across the dandiset:\", info.drop_duplicates(\"subject\").sex.value_counts().to_dict())\n''', tags=[\"claim:cohort-sizes\"])\n\nmd(r'''\n**Result: TBD**\n''')\n\n# ---------------------------------------------------------------------------------------------\nmd(r'''\n## fig2-gaba-excited\n\n> Optogenetic stimulation of STN or PPN inputs increases SNr GABA neuron activity (paired t-test\n> on the 1 s train, STN t = 3.8, p = 0.008; PPN t = 9.2, p < 0.0001).\n''')\n\ncode(r'''\nfig, axes = plt.subplots(1, 2, figsize=(10, 3), sharey=True)\nfor ax, inp in zip(axes, [\"STN\", \"PPN\"]):\n    lo, hi = plot_traces(ax, \"GABA\", inp, \"SNr\", duration=1.0, label=f\"SNr GABA, {inp}\")\n    ax.set_title(f\"{inp}, 1 s 40 Hz\"); ax.set_xlabel(\"s from onset\"); ax.legend()\n    print(f\"{inp}: plotted group mean ranges {lo:.2f} to {hi:.2f} % dF/F (all within the axes)\")\naxes[0].set_ylabel(\"dF/F (%)\")\nplt.show()\nfor inp, paper in [(\"STN\", \"t = 3.8, p = 0.008\"), (\"PPN\", \"t = 9.2, p < 0.0001\")]:\n    for dur in [0.25, 1.0, 4.0]:\n        c = cohort(\"GABA\", inp, \"SNr\", duration=dur)\n        res = ph.paired_t(c.during, c.pre)\n        tag = f\"(paper, 1 s: {paper})\" if dur == 1.0 else \"\"\n        print(f\"{inp} {dur} s: n {res['n']}, mean during {c.during.mean():.2f}, pre {c.pre.mean():.2f} % ; t {res['stat']:.2f}, p {res['p']:.2g} {tag}\")\nc = cohort(\"GABA\", \"STN\", \"SNr\", duration=1.0)\nprint(\"\\nSTN per mouse, during 1 s train (%):\", c.during.round(2).to_dict())\nprint(\"Variant, mice of the 24 kHz rig (10 trials) vs others, STN 1 s:\", c.groupby(c.n_trials).during.agg([\"size\", \"mean\"]).round(2).to_dict())\n''', tags=[\"claim:fig2-gaba-excited\"])\n\nmd(r'''\n**Result: TBD**\n''')\n\n# ---------------------------------------------------------------------------------------------\nmd(r'''\n## fig2-gaba-frequency\n\n> The SNr GABA response scales with stimulation frequency from 5 to 40 Hz (Friedman test on 1 s\n> trains, STN F = 21.0, p = 0.0001; PPN F = 18.2, p = 0.0004).\n''')\n\ncode(r'''\nfor inp, paper in [(\"STN\", \"F = 21.0, p = 0.0001\"), (\"PPN\", \"F = 18.2, p = 0.0004\")]:\n    m = freq_matrix(\"GABA\", inp, 1.0, \"SNr\")\n    res = ph.friedman(m.values)\n    print(f\"{inp}: mean during (%) by frequency {m.mean().round(2).to_dict()}; mice {len(m)}, complete {res['n']}\")\n    print(f\"   Friedman chi2 {res['stat']:.2f}, p {res['p']:.2g} (paper: {paper}); mice with 40 Hz > 5 Hz: {int((m[40.0] > m[5.0]).sum())} of {len(m)}\")\n    print(f\"   RM ANOVA variant: {fmt(ph.rm_anova(m.values))}\")\n    for dur in [0.25, 4.0]:\n        mv = freq_matrix(\"GABA\", inp, dur, \"SNr\")\n        if mv.dropna().shape[0] >= 3:\n            rv = ph.friedman(mv.values)\n            print(f\"   variant {dur} s trains: mice {rv['n']}, means {mv.mean().round(2).to_dict()}, Friedman {rv['stat']:.2f}, p {rv['p']:.2g}\")\n        else:\n            print(f\"   variant {dur} s trains: {mv.dropna().shape[0]} mice with all four frequencies\")\n''', tags=[\"claim:fig2-gaba-frequency\"])\n\nmd(r'''\n**Result: TBD**\n''')\n\n# ---------------------------------------------------------------------------------------------\nmd(r'''\n## fig3b-da-stn-250ms-peak\n\n> A 250 ms 40 Hz train of STN inputs elicits a net increase in SNc pan-DA neuron activity that\n> peaks after stimulus offset (latency to peak 0.50 +/- 0.03 s, mean +/- SEM).\n''')\n\ncode(r'''\nc = cohort(\"panDA\", \"STN\", \"SNc\", duration=0.25)\nlat = c.peak_latency\nprint(\"Per mouse latency to peak (s, 0 to 2.25 s after onset):\", lat.round(2).to_dict())\nprint(f\"Mean {lat.mean():.3f} s, SEM {lat.sem():.3f} s, n {len(lat)} (paper 0.50 +/- 0.03 s); mice peaking after offset (> 0.25 s): {int((lat > 0.25).sum())}\")\nnet = []\nfor r in recs:\n    if r[\"path\"] in c.path.values:\n        ct = ph.condition_traces(r)\n        cc = ct[np.isclose(ct.duration, 0.25)].iloc[0]\n        net.append(ph.window_mean(cc.trace, cc.t, 0.0, 1.25))\n        w = (cc.t >= 0) & (cc.t < 1.25)\n        cc_lat = cc.t[w][np.nanargmax(cc.trace[w])]\nnet = np.array(net)\nres = stats.ttest_1samp(net, 0)\nprint(f\"Net response over 0 to 1.25 s: mean {net.mean():.2f} % (range {net.min():.2f} to {net.max():.2f}), t {res.statistic:.2f}, p {res.pvalue:.2g}\")\nshort = []\nfor r in recs:\n    if r[\"path\"] in c.path.values:\n        ct = ph.condition_traces(r); cc = ct[np.isclose(ct.duration, 0.25)].iloc[0]\n        w = (cc.t >= 0) & (cc.t < 1.25)\n        short.append(cc.t[w][np.nanargmax(cc.trace[w])])\nshort = np.array(short)\nprint(f\"Variant, peak window 0 to 1.25 s: mean latency {short.mean():.3f} s, SEM {short.std(ddof=1) / np.sqrt(len(short)):.3f}\")\nfig, ax = plt.subplots(figsize=(5, 3))\nlo, hi = plot_traces(ax, \"panDA\", \"STN\", \"SNc\", duration=0.25, label=\"SNc pan-DA, STN 0.25 s\")\nax.set_xlabel(\"s from onset\"); ax.set_ylabel(\"dF/F (%)\"); ax.legend(); plt.show()\nprint(f\"plotted mean ranges {lo:.2f} to {hi:.2f} %\")\n''', tags=[\"claim:fig3b-da-stn-250ms-peak\"])\n\nmd(r'''\n**Result: TBD**\n''')\n\n# ---------------------------------------------------------------------------------------------\nmd(r'''\n## fig3c-da-stn-duration\n\n> For SNc pan-DA neurons the STN-evoked response varies with train duration; with 1 and 4 s\n> trains an initial increase is followed by inhibition (Friedman test, F = 13.0, p = 0.005).\n''')\n\ncode(r'''\ndef duration_tests(group, inp, site):\n    rows = {}\n    for d in [0.25, 1.0, 4.0]:\n        c = cohort(group, inp, site, duration=d)\n        rows[d] = c\n    during = pd.DataFrame({d: rows[d].during for d in rows})\n    auc = pd.DataFrame({d: rows[d].auc for d in rows})\n    print(\"Mean during (%) per duration:\", during.mean().round(2).to_dict(), \"| mice:\", len(during))\n    out = {}\n    out[\"a\"] = ph.friedman(during.values)\n    out[\"b\"] = ph.friedman(np.column_stack([rows[1.0].pre.reindex(during.index).values, during.values]))\n    out[\"c\"] = ph.friedman(auc.values)\n    for k, v in out.items():\n        print(f\"   reading ({k}): Friedman chi2 {v['stat']:.2f}, df {3 if k == 'b' else 2}, p {v['p']:.2g}, n {v['n']}\")\n    return rows, out\n\nrows, out = duration_tests(\"panDA\", \"STN\", \"SNc\")\nearly, late = [], []\nfor r in recs:\n    if r[\"path\"] in rows[4.0].path.values:\n        ct = ph.condition_traces(r); cc = ct[np.isclose(ct.duration, 4.0) & np.isclose(ct.frequency, 40.0)].iloc[0]\n        early.append(ph.window_mean(cc.trace, cc.t, 0.0, 0.5)); late.append(ph.window_mean(cc.trace, cc.t, 3.0, 4.0))\nearly, late = np.array(early), np.array(late)\nres = stats.ttest_rel(early, late)\nprint(f\"4 s trains: mean over 0 to 0.5 s {early.mean():.2f} %, over 3 to 4 s {late.mean():.2f} %; paired t {res.statistic:.2f}, p {res.pvalue:.2g}, n {len(early)}\")\nprint(f\"Mice with late below early: {int((late < early).sum())} of {len(early)}; with late below 0: {int((late < 0).sum())}\")\nfig, ax = plt.subplots(figsize=(6, 3))\nfor d in [0.25, 1.0, 4.0]:\n    lo, hi = plot_traces(ax, \"panDA\", \"STN\", \"SNc\", duration=d, label=f\"{d} s\")\n    print(f\"{d} s: plotted mean ranges {lo:.2f} to {hi:.2f} %\")\nax.set_xlabel(\"s from onset\"); ax.set_ylabel(\"dF/F (%)\"); ax.legend(); plt.show()\n''', tags=[\"claim:fig3c-da-stn-duration\"])\n\nmd(r'''\n**Result: TBD**\n''')\n\n# ---------------------------------------------------------------------------------------------\nmd(r'''\n## fig3d-da-stn-frequency-ns\n\n> The amplitude of the SNc pan-DA response during STN stimulation does not scale with frequency\n> (Friedman test, F = 4.2, p = 0.24).\n''')\n\ncode(r'''\nfor dur in [1.0, 0.25, 4.0]:\n    m = freq_matrix(\"panDA\", \"STN\", dur, \"SNc\")\n    if m.dropna().shape[0] < 3:\n        print(f\"{dur} s: {m.dropna().shape[0]} complete mice\"); continue\n    res = ph.friedman(m.values)\n    tag = \"main (paper F = 4.2, p = 0.24)\" if dur == 1.0 else \"variant\"\n    print(f\"{dur} s [{tag}]: means {m.mean().round(2).to_dict()}, Friedman chi2 {res['stat']:.2f}, p {res['p']:.2g}, n {res['n']}; \"\n          f\"40 minus 5 Hz {np.nanmean(m[40.0] - m[5.0]):.2f} %\")\n''', tags=[\"claim:fig3d-da-stn-frequency-ns\"])\n\nmd(r'''\n**Result: TBD**\n''')\n\n# ---------------------------------------------------------------------------------------------\nmd(r'''\n## fig3g-da-ppn-duration\n\n> PPN stimulation also evokes SNc pan-DA responses that vary with train duration (Friedman test,\n> F = 11.5, p = 0.009).\n''')\n\ncode(r'''\nrows_p, out_p = duration_tests(\"panDA\", \"PPN\", \"SNc\")\nfig, ax = plt.subplots(figsize=(6, 3))\nfor d in [0.25, 1.0, 4.0]:\n    lo, hi = plot_traces(ax, \"panDA\", \"PPN\", \"SNc\", duration=d, label=f\"{d} s\")\n    print(f\"{d} s: plotted mean ranges {lo:.2f} to {hi:.2f} %\")\nax.set_xlabel(\"s from onset\"); ax.set_ylabel(\"dF/F (%)\"); ax.legend(); plt.show()\n''', tags=[\"claim:fig3g-da-ppn-duration\"])\n\nmd(r'''\n**Result: TBD**\n''')\n\n# ---------------------------------------------------------------------------------------------\nmd(r'''\n## fig3h-da-ppn-frequency-ns\n\n> The SNc pan-DA response to PPN stimulation does not vary with frequency (repeated-measures\n> one-way ANOVA, F2,15 = 1.35, p = 0.28).\n''')\n\ncode(r'''\nfor dur in [1.0, 0.25, 4.0]:\n    m = freq_matrix(\"panDA\", \"PPN\", dur, \"SNc\")\n    if m.dropna().shape[0] < 3:\n        print(f\"{dur} s: {m.dropna().shape[0]} complete mice\"); continue\n    res = ph.rm_anova(m.values)\n    tag = \"main (paper F2,15 = 1.35, p = 0.28)\" if dur == 1.0 else \"variant\"\n    print(f\"{dur} s [{tag}]: means {m.mean().round(2).to_dict()}; {fmt(res)}; 40 minus 5 Hz {np.nanmean(m[40.0] - m[5.0]):.2f} %\")\n''', tags=[\"claim:fig3h-da-ppn-frequency-ns\"])\n\nmd(r'''\n**Result: TBD**\n''')\n\n# ---------------------------------------------------------------------------------------------\nmd(r'''\n## fig4cf-ts-dls-opposite\n\n> STN or PPN stimulation evokes opposite DA release in TS (increase) and DLS (decrease)\n> (two-way ANOVA, striatal site, STN F1,11 = 40.9, PPN F1,16 = 36.4, p < 0.0001; site by time\n> interaction of the same size).\n''')\n\ncode(r'''\ndef site_contrast(group, inp, duration=1.0):\n    ts, dls = cohort(group, inp, \"TS\", duration=duration), cohort(group, inp, \"DLS\", duration=duration)\n    res = ph.mixed_2x2(ts.pre, ts.during, dls.pre, dls.during)\n    print(f\"{group} {inp} {duration} s: TS n {len(ts)} mean during {ts.during.mean():.2f} % (mice above 0: {int((ts.during > 0).sum())}); \"\n          f\"DLS n {len(dls)} mean during {dls.during.mean():.2f} % (mice below 0: {int((dls.during < 0).sum())})\")\n    print(f\"   site F{res['df']} {res['F_site']:.1f}, p {res['p_site']:.2g}; interaction F {res['F_interaction']:.1f}, p {res['p_interaction']:.2g}\")\n    return ts, dls, res\n\nfor inp, paper in [(\"STN\", \"F1,11 = 40.9\"), (\"PPN\", \"F1,16 = 36.4\")]:\n    print(f\"paper: {paper}\")\n    site_contrast(\"GRABDA\", inp)\n    for d in [0.25, 4.0]:\n        site_contrast(\"GRABDA\", inp, d)\nfig, axes = plt.subplots(1, 2, figsize=(10, 3), sharey=True)\nfor ax, inp in zip(axes, [\"STN\", \"PPN\"]):\n    for s in [\"TS\", \"DLS\"]:\n        lo, hi = plot_traces(ax, \"GRABDA\", inp, s, duration=1.0)\n        print(f\"{inp} {s}: plotted mean ranges {lo:.2f} to {hi:.2f} %\")\n    ax.set_title(f\"GRAB-DA, {inp}, 1 s 40 Hz\"); ax.set_xlabel(\"s from onset\"); ax.legend()\naxes[0].set_ylabel(\"dF/F (%)\"); plt.show()\n''', tags=[\"claim:fig4cf-ts-dls-opposite\"])\n\nmd(r'''\n**Result: TBD**\n''')\n\n# ---------------------------------------------------------------------------------------------\nmd(r'''\n## fig4dg-ts-frequency\n\n> In TS, the DA increase evoked by either input scales with frequency, for all train durations\n> (STN, repeated-measures ANOVA, 0.25 s F2,8 = 7.5, 1 s F2,7 = 13.6, 4 s F2,9 = 16.9; PPN,\n> Friedman, F = 20.0, 24.0, 23.2).\n''')\n\ncode(r'''\ndef frequency_tests(group, site, plan, direction, kind=None):\n    \"\"\"plan: list of (input, duration, test name, paper text). direction +1: 40 Hz above 5 Hz.\"\"\"\n    out = []\n    for inp, dur, test, paper in plan:\n        m = freq_matrix(group, inp, dur, site, kind=kind)\n        res = ph.friedman(m.values) if test == \"Friedman\" else ph.rm_anova(m.values)\n        other = ph.rm_anova(m.values) if test == \"Friedman\" else ph.friedman(m.values)\n        diff = np.nanmean(m[40.0] - m[5.0])\n        ok = res[\"p\"] < 0.05 and np.sign(diff) == direction\n        out.append({\"input\": inp, \"duration\": dur, \"test\": test, \"n\": res[\"n\"], \"stat\": round(res[\"stat\"], 2),\n                    \"p\": res[\"p\"], \"mean_5\": m[5.0].mean(), \"mean_10\": m[10.0].mean(), \"mean_20\": m[20.0].mean(),\n                    \"mean_40\": m[40.0].mean(), \"holds\": ok, \"paper\": paper, \"other_test_p\": other[\"p\"]})\n    t = pd.DataFrame(out)\n    print(t.round(4).to_string(index=False))\n    print(\"Tests that hold:\", int(t.holds.sum()), \"of\", len(t))\n    return t\n\nplan = [(\"STN\", 0.25, \"RM\", \"F2,8 = 7.5, p = 0.02\"), (\"STN\", 1.0, \"RM\", \"F2,7 = 13.6, p = 0.004\"), (\"STN\", 4.0, \"RM\", \"F2,9 = 16.9, p = 0.001\"),\n        (\"PPN\", 0.25, \"Friedman\", \"F = 20.0, p = 0.0002\"), (\"PPN\", 1.0, \"Friedman\", \"F = 24.0, p < 0.0001\"), (\"PPN\", 4.0, \"Friedman\", \"F = 23.2, p < 0.0001\")]\nts_freq = frequency_tests(\"GRABDA\", \"TS\", plan, +1)\n''', tags=[\"claim:fig4dg-ts-frequency\"])\n\nmd(r'''\n**Result: TBD**\n''')\n\n# ---------------------------------------------------------------------------------------------\nmd(r'''\n## fig4eh-dls-frequency\n\n> In DLS, the DA inhibition scales with frequency and is most prominent at higher frequencies\n> (STN, repeated-measures ANOVA, 0.25 s F = 7.5, 1 s F = 12.8, 4 s F = 46.8; PPN, 0.25 s\n> Friedman F = 12.3, 1 s and 4 s repeated-measures ANOVA F = 12.8 and 10.2).\n''')\n\ncode(r'''\nplan = [(\"STN\", 0.25, \"RM\", \"F2,9 = 7.5, p = 0.015\"), (\"STN\", 1.0, \"RM\", \"F1,11 = 12.8, p = 0.0005\"), (\"STN\", 4.0, \"RM\", \"F2,13 = 46.8, p < 0.0001\"),\n        (\"PPN\", 0.25, \"Friedman\", \"F = 12.3, p = 0.006\"), (\"PPN\", 1.0, \"RM\", \"F1,11 = 12.8, p = 0.002\"), (\"PPN\", 4.0, \"RM\", \"F2,13 = 10.2, p = 0.004\")]\ndls_freq = frequency_tests(\"GRABDA\", \"DLS\", plan, -1)\nprint(\"\\nThe paper gives F1,11 = 12.8 for both STN and PPN 1 s trains, with p = 0.0005 and 0.002; F(1, 11) = 12.8 gives p =\",\n      round(stats.f.sf(12.8, 1, 11), 4))\n''', tags=[\"claim:fig4eh-dls-frequency\"])\n\nmd(r'''\n**Result: TBD**\n''')\n\n# ---------------------------------------------------------------------------------------------\nmd(r'''\n## fig4eh-dls-5hz-increase\n\n> Low-frequency (5 Hz) stimulation of either STN or PPN increases DLS dopamine.\n''')\n\ncode(r'''\nfor inp in [\"STN\", \"PPN\"]:\n    for dur in [1.0, 0.25, 4.0]:\n        c = cohort(\"GRABDA\", inp, \"DLS\", protocol=\"frequencies\", duration=dur, frequency=5.0)\n        if not len(c):\n            continue\n        res = stats.ttest_1samp(c.during, 0)\n        tag = \"main\" if dur == 1.0 else \"variant\"\n        print(f\"{inp} {dur} s 5 Hz [{tag}]: n {len(c)}, mean during {c.during.mean():.2f} % (range {c.during.min():.2f} to {c.during.max():.2f}), \"\n              f\"mice above 0 {int((c.during > 0).sum())}, t {res.statistic:.2f}, p {res.pvalue:.2g}; mean in 1 s after offset {c.post.mean():.2f} %\")\n''', tags=[\"claim:fig4eh-dls-5hz-increase\"])\n\nmd(r'''\n**Result: TBD**\n''')\n\n# ---------------------------------------------------------------------------------------------\nmd(r'''\n## fig4cf-dls-rebound\n\n> In DLS the DA inhibition is followed by a post-stimulus rebound above baseline.\n''')\n\ncode(r'''\nfor inp in [\"STN\", \"PPN\"]:\n    for dur in [1.0, 0.25, 4.0]:\n        c = cohort(\"GRABDA\", inp, \"DLS\", duration=dur)\n        res = stats.ttest_1samp(c.post, 0)\n        tag = \"main\" if dur == 1.0 else \"variant\"\n        print(f\"{inp} {dur} s [{tag}]: n {len(c)}, mean during {c.during.mean():.2f} %, mean in 1 s after offset {c.post.mean():.2f} % \"\n              f\"(range {c.post.min():.2f} to {c.post.max():.2f}), mice above 0 {int((c.post > 0).sum())}, t {res.statistic:.2f}, p {res.pvalue:.2g}\")\n''', tags=[\"claim:fig4cf-dls-rebound\"])\n\nmd(r'''\n**Result: TBD**\n''')\n\n# ---------------------------------------------------------------------------------------------\nmd(r'''\n## figs3-terminals-opposite\n\n> Calcium in DA terminals in TS and DLS shows opposite responses to STN stimulation, as the\n> GRAB-DA recordings do.\n''')\n\ncode(r'''\nts_t, dls_t, res_t = site_contrast(\"DAterm\", \"STN\")\nfor d in [0.25, 4.0]:\n    site_contrast(\"DAterm\", \"STN\", d)\nprint(f\"DLS terminals, mean in 1 s after offset of 1 s trains: {dls_t.post.mean():.2f} % (mice above 0: {int((dls_t.post > 0).sum())} of {len(dls_t)})\")\nfig, ax = plt.subplots(figsize=(5, 3))\nfor s in [\"TS\", \"DLS\"]:\n    lo, hi = plot_traces(ax, \"DAterm\", \"STN\", s, duration=1.0)\n    print(f\"{s}: plotted mean ranges {lo:.2f} to {hi:.2f} %\")\nax.set_title(\"DA terminal GCaMP, STN, 1 s 40 Hz\"); ax.set_xlabel(\"s from onset\"); ax.set_ylabel(\"dF/F (%)\"); ax.legend(); plt.show()\n''', tags=[\"claim:figs3-terminals-opposite\"])\n\nmd(r'''\n**Result: TBD**\n''')\n\n# ---------------------------------------------------------------------------------------------\nmd(r'''\n## fig5-vglut2-excited\n\n> Stimulation of STN or PPN inputs increases the activity of Vglut2+ DA neurons in SNc (STN,\n> Wilcoxon, 0.25 s W = 41, p = 0.012, 1 s W = 43, p = 0.008, 4 s W = -5, p = 0.82; PPN, paired\n> t-test, 0.25 s t = 2.9, p = 0.02, 1 s t = 3.4, p = 0.008, 4 s t = 3.0, p = 0.01).\n''')\n\ncode(r'''\ndef pre_during_tests(group, site, plan, kind=None, label=\"\"):\n    out = []\n    for inp, dur, test, paper in plan:\n        c = cohort(group, inp, site, duration=dur, kind=kind)\n        res = ph.wilcoxon_w(c.during, c.pre) if test == \"Wilcoxon\" else ph.paired_t(c.during, c.pre)\n        other = ph.paired_t(c.during, c.pre) if test == \"Wilcoxon\" else ph.wilcoxon_w(c.during, c.pre)\n        out.append({\"input\": inp, \"duration\": dur, \"test\": res[\"test\"], \"n\": res[\"n\"], \"stat\": round(res[\"stat\"], 2), \"p\": res[\"p\"],\n                    \"mean_during\": c.during.mean(), \"mean_pre\": c.pre.mean(), \"mice_up\": int((c.during > c.pre).sum()),\n                    \"mean_post\": c.post.mean(), \"paper\": paper, \"other_test_p\": other[\"p\"]})\n    t = pd.DataFrame(out)\n    print(label); print(t.round(4).to_string(index=False))\n    return t\n\nplan = [(\"STN\", 0.25, \"Wilcoxon\", \"W = 41, p = 0.012\"), (\"STN\", 1.0, \"Wilcoxon\", \"W = 43, p = 0.008\"), (\"STN\", 4.0, \"Wilcoxon\", \"W = -5, p = 0.82\"),\n        (\"PPN\", 0.25, \"t\", \"t = 2.9, p = 0.02\"), (\"PPN\", 1.0, \"t\", \"t = 3.4, p = 0.008\"), (\"PPN\", 4.0, \"t\", \"t = 3.0, p = 0.01\")]\nvg = pre_during_tests(\"Vglut2\", \"SNc\", plan)\ncore = vg[vg.duration < 4]\nprint(\"\\nTests of 0.25 and 1 s trains with a significant increase:\", int(((core.p < 0.05) & (core.mean_during > core.mean_pre)).sum()), \"of 4\")\nfig, axes = plt.subplots(1, 2, figsize=(10, 3), sharey=True)\nfor ax, inp in zip(axes, [\"STN\", \"PPN\"]):\n    lo, hi = plot_traces(ax, \"Vglut2\", inp, \"SNc\", duration=1.0, label=\"Vglut2 SNc\")\n    ax.set_title(f\"{inp}, 1 s 40 Hz\"); ax.legend(); ax.set_xlabel(\"s from onset\")\n    print(f\"{inp}: plotted mean ranges {lo:.2f} to {hi:.2f} %\")\naxes[0].set_ylabel(\"dF/F (%)\"); plt.show()\n''', tags=[\"claim:fig5-vglut2-excited\"])\n\nmd(r'''\n**Result: TBD**\n''')\n\n# ---------------------------------------------------------------------------------------------\nmd(r'''\n## fig5-vglut2-frequency\n\n> The Vglut2+ DA neuron increase scales with frequency for short STN trains and for all PPN\n> durations (Friedman, STN 0.25 s F = 15.5, p = 0.001, 1 s F = 5.9, p = 0.11, 4 s F = 7.0, p =\n> 0.07; PPN F = 18.8, 24.8, 20.2, p <= 0.0003).\n''')\n\ncode(r'''\nplan = [(\"STN\", 0.25, \"Friedman\", \"F = 15.5, p = 0.001\"), (\"STN\", 1.0, \"Friedman\", \"F = 5.9, p = 0.11\"), (\"STN\", 4.0, \"Friedman\", \"F = 7.0, p = 0.07\"),\n        (\"PPN\", 0.25, \"Friedman\", \"F = 18.8, p = 0.0003\"), (\"PPN\", 1.0, \"Friedman\", \"F = 24.8, p < 0.0001\"), (\"PPN\", 4.0, \"Friedman\", \"F = 20.2, p = 0.0001\")]\nvg_freq = frequency_tests(\"Vglut2\", \"SNc\", plan, +1)\ncore = vg_freq[~((vg_freq.input == \"STN\") & (vg_freq.duration > 0.25))]\nprint(\"Tests the claim rests on (STN 0.25 s, PPN all) that hold:\", int(core.holds.sum()), \"of\", len(core))\n''', tags=[\"claim:fig5-vglut2-frequency\"])\n\nmd(r'''\n**Result: TBD**\n''')\n\n# ---------------------------------------------------------------------------------------------\nmd(r'''\n## fig5-anxa1-dls-inhibited\n\n> In DLS terminals of SNc Anxa1+ neurons, STN and PPN stimulation produce inhibition (STN, 0.25 s\n> t = 6.4, p = 0.0004, 1 s W = -36, p = 0.005, 4 s W = -36, p = 0.008; PPN, 0.25 s t = 3.9, p =\n> 0.004, 1 s W = -55, p = 0.002, 4 s t = 3.8, p = 0.004).\n''')\n\ncode(r'''\nplan = [(\"STN\", 0.25, \"t\", \"t = 6.4, p = 0.0004\"), (\"STN\", 1.0, \"Wilcoxon\", \"W = -36, p = 0.005\"), (\"STN\", 4.0, \"Wilcoxon\", \"W = -36, p = 0.008\"),\n        (\"PPN\", 0.25, \"t\", \"t = 3.9, p = 0.004\"), (\"PPN\", 1.0, \"Wilcoxon\", \"W = -55, p = 0.002\"), (\"PPN\", 4.0, \"t\", \"t = 3.8, p = 0.004\")]\nax_dls = pre_during_tests(\"Anxa1\", \"DLS\", plan, label=\"Recordings labelled DLS (main):\")\nprint(\"Significant decreases:\", int(((ax_dls.p < 0.05) & (ax_dls.mean_during < ax_dls.mean_pre)).sum()), \"of 6\")\n# Variant: the unsuffixed (SNc-labelled) recordings counted as DLS.\nR_alt = R.copy()\nR_alt.loc[(R_alt.group == \"Anxa1\") & (R_alt.kind == \"single\"), \"site\"] = \"DLS\"\nR_main = R\nR = R_alt\nax_alt = pre_during_tests(\"Anxa1\", \"DLS\", plan, label=\"\\nVariant, unsuffixed recordings added to DLS:\")\nR = R_main\nprint(\"Variant significant decreases:\", int(((ax_alt.p < 0.05) & (ax_alt.mean_during < ax_alt.mean_pre)).sum()), \"of 6\")\n''', tags=[\"claim:fig5-anxa1-dls-inhibited\"])\n\nmd(r'''\n**Result: TBD**\n''')\n\n# ---------------------------------------------------------------------------------------------\nmd(r'''\n## fig5-anxa1-dls-frequency\n\n> The Anxa1+ terminal inhibition scales with frequency (STN, 0.25 s F = 18.0, 1 s F = 15.5, 4 s\n> F = 15.3; PPN, 0.25 s F = 11.5, 1 s F2,15 = 11.0, 4 s F2,18 = 7.2).\n''')\n\ncode(r'''\nplan = [(\"STN\", 0.25, \"Friedman\", \"F = 18.0, p = 0.0003\"), (\"STN\", 1.0, \"Friedman\", \"F = 15.5, p = 0.015\"), (\"STN\", 4.0, \"Friedman\", \"F = 15.3, p = 0.001\"),\n        (\"PPN\", 0.25, \"Friedman\", \"F = 11.5, p = 0.0002\"), (\"PPN\", 1.0, \"RM\", \"F2,15 = 11.0, p = 0.006\"), (\"PPN\", 4.0, \"RM\", \"F2,18 = 7.2, p = 0.002\")]\nax_freq = frequency_tests(\"Anxa1\", \"DLS\", plan, -1)\nR = R_alt\nprint(\"\\nVariant, unsuffixed recordings added to DLS:\")\nax_freq_alt = frequency_tests(\"Anxa1\", \"DLS\", plan, -1)\nR = R_main\nprint(\"\\nChi-square p for the paper's Friedman values with 3 df: F = 11.5 ->\", round(stats.chi2.sf(11.5, 3), 4),\n      \"(paper 0.0002); F = 15.5 ->\", round(stats.chi2.sf(15.5, 3), 4), \"(paper 0.015)\")\n''', tags=[\"claim:fig5-anxa1-dls-frequency\"])\n\nmd(r'''\n**Result: TBD**\n''')\n\n# ---------------------------------------------------------------------------------------------\nmd(r'''\n## fig5-anxa1-dls-rebound\n\n> Anxa1+ terminals in DLS show a transient increase in activity at stimulus offset, for both\n> inputs.\n''')\n\ncode(r'''\nfor label, RR in [(\"main, labelled DLS\", R_main), (\"variant, unsuffixed added\", R_alt)]:\n    R = RR\n    for inp in [\"STN\", \"PPN\"]:\n        for dur in [1.0, 0.25, 4.0]:\n            c = cohort(\"Anxa1\", inp, \"DLS\", duration=dur)\n            res = stats.ttest_1samp(c.post, 0)\n            print(f\"[{label}] {inp} {dur} s: n {len(c)}, mean in 1 s after offset {c.post.mean():.2f} % (range {c.post.min():.2f} to {c.post.max():.2f}), \"\n                  f\"mice above 0 {int((c.post > 0).sum())}, t {res.statistic:.2f}, p {res.pvalue:.2g}\")\nR = R_main\nfig, axes = plt.subplots(1, 2, figsize=(10, 3), sharey=True)\nfor ax, inp in zip(axes, [\"STN\", \"PPN\"]):\n    for s, kind, lab in [(\"DLS\", None, \"DLS\"), (\"SNc\", \"dual\", \"SNc, dual mice\"), (\"SNc\", \"single\", \"unsuffixed\")]:\n        lo, hi = plot_traces(ax, \"Anxa1\", inp, s, duration=1.0, kind=kind, label=lab)\n        print(f\"{inp} {lab}: plotted mean ranges {lo:.2f} to {hi:.2f} %\")\n    ax.set_title(f\"Anxa1, {inp}, 1 s 40 Hz\"); ax.legend(); ax.set_xlabel(\"s from onset\")\naxes[0].set_ylabel(\"dF/F (%)\"); plt.show()\n''', tags=[\"claim:fig5-anxa1-dls-rebound\"])\n\nmd(r'''\n**Result: TBD**\n''')\n\n# ---------------------------------------------------------------------------------------------\nmd(r'''\n## figs4-anxa1-soma-inhibited\n\n> Anxa1+ SNc cell bodies show stimulation-induced inhibition (paired t-test, STN 0.25 s t = 3.1,\n> 1 s t = 4.0, 4 s t = 7.2, n = 5; PPN t = 4.8, 8.4, 3.3, n = 4) followed by post-stimulus\n> rebound activation.\n''')\n\ncode(r'''\nplan = [(\"STN\", 0.25, \"t\", \"t = 3.1, p = 0.035\"), (\"STN\", 1.0, \"t\", \"t = 4.0, p = 0.016\"), (\"STN\", 4.0, \"t\", \"t = 7.2, p = 0.002\"),\n        (\"PPN\", 0.25, \"t\", \"t = 4.8, p = 0.018\"), (\"PPN\", 1.0, \"t\", \"t = 8.4, p = 0.004\"), (\"PPN\", 4.0, \"t\", \"t = 3.3, p = 0.044\")]\nsoma = pre_during_tests(\"Anxa1\", \"SNc\", plan, label=\"Recordings labelled SNc (main):\")\nprint(\"Significant decreases:\", int(((soma.p < 0.05) & (soma.mean_during < soma.mean_pre)).sum()), \"of 6\")\nsoma_d = pre_during_tests(\"Anxa1\", \"SNc\", plan, kind=\"dual\", label=\"\\nVariant, mice with both a DLS and an SNc file (the paper's n):\")\nprint(\"Variant significant decreases:\", int(((soma_d.p < 0.05) & (soma_d.mean_during < soma_d.mean_pre)).sum()), \"of 6\")\nfor kind in [None, \"dual\"]:\n    for inp in [\"STN\", \"PPN\"]:\n        c = cohort(\"Anxa1\", inp, \"SNc\", duration=1.0, kind=kind)\n        res = stats.ttest_1samp(c.post, 0)\n        print(f\"Rebound, {kind or 'all SNc'} {inp} 1 s: mean in 1 s after offset {c.post.mean():.2f} %, mice above 0 {int((c.post > 0).sum())} of {len(c)}, t {res.statistic:.2f}, p {res.pvalue:.2g}\")\n''', tags=[\"claim:figs4-anxa1-soma-inhibited\"])\n\nmd(r'''\n**Result: TBD**\n''')\n\n# ---------------------------------------------------------------------------------------------\nmd(r'''\n## fig5-opposite-subtypes\n\n> Excitatory inputs from STN and PPN activate PD-resilient Vglut2+ DA neurons but inhibit\n> PD-vulnerable Anxa1+ DA neurons.\n''')\n\ncode(r'''\nfor label, RR in [(\"main\", R_main), (\"variant, unsuffixed Anxa1 added to DLS\", R_alt)]:\n    R = RR\n    for inp in [\"STN\", \"PPN\"]:\n        v, a = cohort(\"Vglut2\", inp, \"SNc\", duration=1.0), cohort(\"Anxa1\", inp, \"DLS\", duration=1.0)\n        res = stats.ttest_ind(v.during, a.during, equal_var=False)\n        print(f\"[{label}] {inp}: Vglut2 n {len(v)} mean during {v.during.mean():.2f} % ; Anxa1 DLS n {len(a)} mean {a.during.mean():.2f} % ; \"\n              f\"Welch t {res.statistic:.2f}, p {res.pvalue:.2g}\")\nR = R_main\nfor inp in [\"STN\", \"PPN\"]:\n    v, a = cohort(\"Vglut2\", inp, \"SNc\", duration=1.0), cohort(\"Anxa1\", inp, \"SNc\", duration=1.0)\n    res = stats.ttest_ind(v.during, a.during, equal_var=False)\n    print(f\"[variant, Anxa1 SNc] {inp}: Anxa1 SNc n {len(a)} mean {a.during.mean():.2f} % ; Welch t {res.statistic:.2f}, p {res.pvalue:.2g}\")\n''', tags=[\"claim:fig5-opposite-subtypes\"])\n\nmd(r'''\n**Result: TBD**\n''')\n\ncode(r'''\nprint(f\"Notebook ran in {(time.time() - started) / 60:.1f} min\")\n''')\n\nmd(r'''\n## Summary\n\nTBD\n''')\n"
}
```

```
File created successfully at: /tmp/claude-1001/gen/cells.py (file state is current in your context — no need to Read it back)
```

**Agent**

Building the notebook and running it in the scratch environment to check it works.

**Agent calls Bash**

```bash
cd $TMPDIR && . scratch/bin/activate && uv pip install -q nbconvert ipykernel nbformat 2>&1|tail -1; python gen/build.py && cd entries/001528-hadjas-2025 && time jupyter nbconvert --to notebook --execute reproduce_hadjas_2025.ipynb --output $TMPDIR/run1.ipynb --ExecutePreprocessor.timeout=3000 2>&1 | tail -5
```

```
85 cells
[NbConvertApp] Converting notebook reproduce_hadjas_2025.ipynb to notebook
[IPKernelApp] WARNING | Kernel is running over TCP without encryption. All communication (including code and outputs) is sent in plain text and is susceptible to eavesdropping. Use IPC transport or launch with kernel manager-provisioned CurveZMQ keys to enable transport encryption.
[NbConvertApp] Writing 680881 bytes to /tmp/claude-1001/run1.ipynb

real	4m42.323s
user	8m31.591s
sys	0m6.378s
```

**Agent**

Ran in 4.7 min. Reading the outputs.

**Agent calls Bash**

```bash
cd $TMPDIR && python - <<'EOF'
import json
nb = json.load(open('run1.ipynb'))
for i, c in enumerate(nb['cells']):
    if c['cell_type'] != 'code': continue
    tags = c['metadata'].get('tags', [])
    print(f'===== cell {i} {tags}')
    for o in c.get('outputs', []):
        if 'text' in o: print(''.join(o['text']))
        elif o.get('output_type') == 'error': print('ERROR', o['ename'], o['evalue'])
EOF
```

```
<persisted-output>
Output too large (32.8KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/210b92be-775a-4be5-a155-48ed9ac6192b/tool-results/bmb3igonk.txt

Preview (first 2KB):
===== cell 1 []
Dandiset 001528 version draft | draft modified 2026-09-01T15:27:47.076206+00:00 | assets 290 | same as the pinned draft ( 2026-09-01T15:27:47.076206Z ): True

loaded 258 NWB files in 74 s

===== cell 3 ['sanity']
NWB files: 258 | mice: 120 | groups per mouse (max): 1

Mice per group, input, recorded site and protocol:
protocol           durations  frequencies
group  input site                        
Anxa1  PPN   DLS           4            4
             SNc          10           10
       STN   DLS           5            5
             SNc           8            8
DAterm STN   DLS           8            8
[... 44 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/210b92be-775a-4be5-a155-48ed9ac6192b/tool-results/bmb3igonk.txt",
 "offset": 50
}
```

```
50	group                                             
51	Anxa1               18             0             0
52	DAterm               0            17            17
53	GABA                 8             7             7
54	GRABDA              31             0             0
55	Vglut2              16             3             3
56	panDA               14             6             6
57	
58	Subject ids written in lower case in the files: ['c3015', 'c3016', 'c4379', 'c4708', 'c4709', 'c4977', 'c4978', 'c5113']
59	Session start time zone offsets: {'-00:01': 258}
60	
61	===== cell 5 ['sanity']
62	Stated units of dF/F and of the 465 nm signal: ['a.u.'] ['a.u.']
63	All 100 Hz series start at 0 s: True | median sample interval (ms): [10.0]
64	dF/F, 465 and 405 nm series share one time base in every file: True
65	Files whose dF/F has explicit timestamps: 89 of 258
66	Files with a gap in time above 1 s: 34 ; longest gaps (s): [171981.0, 171929.9, 171904.8]
67	Files with missing dF/F values: 88 ; by protocol: {'frequencies': 88} ; largest fraction: 0.548
68	dF/F 0.1th percentile across files: -89.4 to -1.5; 99.9th percentile: 1.7 to 249.4
69	465 nm median across files: 0.0131 to 0.6156; 405 nm: 0.0137 to 0.3375 (a.u.)
[... 409 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/gen && python - <<'EOF'
s = open('cells.py').read()
s = s.replace('''if True:
    a = ctab[ctab.group == "Anxa1"]
    print(''', '''a = ctab[ctab.group == "Anxa1"]
print(''')
old = s[s.index('net = []\nfor r in recs:\n    if r["path"] in c.path.values:'):s.index('fig, ax = plt.subplots(figsize=(5, 3))\nlo, hi = plot_traces(ax, "panDA", "STN", "SNc", duration=0.25')]
new = '''net, short = [], []
for r in recs:
    if r["path"] in c.path.values:
        ct = ph.condition_traces(r)
        cc = ct[np.isclose(ct.duration, 0.25)].iloc[0]
        net.append(ph.window_mean(cc.trace, cc.t, 0.0, 1.25))
        w = (cc.t >= 0) & (cc.t < 1.25)
        short.append(cc.t[w][np.nanargmax(cc.trace[w])])
net, short = np.array(net), np.array(short)
res = stats.ttest_1samp(net, 0)
print(f"Net response over 0 to 1.25 s: mean {net.mean():.2f} % (range {net.min():.2f} to {net.max():.2f}), t {res.statistic:.2f}, p {res.pvalue:.2g}")
print(f"Variant, peak window 0 to 1.25 s: mean latency {short.mean():.3f} s, SEM {short.std(ddof=1) / np.sqrt(len(short)):.3f}")
'''
s = s.replace(old, new)
# epochs cell additions
s = s.replace('''print("Train lengths within 15 ms of the labelled duration:"''', '''no4 = sorted(set(eps[eps.protocol == "frequencies"].path) - set(eps[(eps.protocol == "frequencies") & (eps.duration == 4.0)].path))
print("Frequencies-protocol files without 4 s trains:", [p.split("/")[0] for p in no4])
gaps = []
for r in recs:
    e = ph.label_epochs(r)
    e = e[e.usable].sort_values("start")
    gaps.append(pd.DataFrame({"protocol": r["protocol"], "onset_to_onset": np.diff(e.start.values), "offset_to_onset": e.start.values[1:] - e.stop.values[:-1]}))
gaps = pd.concat(gaps)
gaps = gaps[gaps.onset_to_onset < 100]
print("Median interval between consecutive trains (s), onset to onset and offset to next onset:")
print(gaps.groupby("protocol").median().round(2).to_string())
print("Train lengths within 15 ms of the labelled duration:"''')
open('cells.py','w').write(s)
EOF
grep -n "if True" cells.py; echo done
```

```
done
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && . scratch/bin/activate && python - <<'EOF'
import sys, pickle, numpy as np, pandas as pd
sys.path.insert(0, 'entries/001528-hadjas-2025')
import photometry as ph
recs = pickle.load(open('recs.pkl','rb'))
eps = pd.concat([ph.label_epochs(r).assign(path=r["path"], protocol=r["protocol"]) for r in recs])
no4 = sorted(set(eps[eps.protocol == "frequencies"].path) - set(eps[(eps.protocol == "frequencies") & (eps.duration == 4.0)].path))
print([p.split("/")[0] for p in no4])
gaps=[]
for r in recs:
    e = ph.label_epochs(r); e = e[e.usable].sort_values("start")
    gaps.append(pd.DataFrame({"protocol": r["protocol"], "onset_to_onset": np.diff(e.start.values), "offset_to_onset": e.start.values[1:] - e.stop.values[:-1]}))
g = pd.concat(gaps); g = g[g.onset_to_onset < 100]
print(g.groupby('protocol').median())
print(sorted({r['subject'] for r in recs if r['raw_rate'] > 20000}), len({r['subject'] for r in recs if r['raw_rate'] > 20000}))
EOF
```

```
['sub-B7514', 'sub-B7515', 'sub-B7532', 'sub-B7616', 'sub-B8364', 'sub-B8369', 'sub-B8370', 'sub-B8427', 'sub-B8429', 'sub-B8569', 'sub-B8603', 'sub-B8612', 'sub-B8677', 'sub-C4608']
             onset_to_onset  offset_to_onset
protocol                                    
durations         11.049206        10.048963
frequencies       20.999700        19.999949
['B7514', 'B7515', 'B7532', 'B7616', 'B8364', 'B8369', 'B8370', 'B8427', 'B8429', 'B8569', 'B8603', 'B8612', 'B8627', 'B8630', 'B8677', 'B8821', 'B9071', 'B9262', 'B9266', 'B9962', 'C0176', 'C0177', 'C0178', 'C0180', 'C0679', 'C0680', 'C0683', 'C0925', 'C0926', 'C0932', 'C1496', 'C1498', 'C1499'] 33
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/gen && python - <<'EOF'
s = open('cells.py').read()
def rep(old, new):
    global s
    assert s.count(old) == 1, old[:60]
    s = s.replace(old, new)

rep('''The epoch tables give 5 mW at 635 nm for every train, as the Methods state. The number of pulses
in each train fits its frequency and length. Three things differ from the Methods. First, 13 mice
(the files with the older 24 kHz raw rate) have 10 trials per condition, where the Methods state
5, and their durations sessions also hold 16 s trains, which the paper does not mention. Second,
in those mice's frequencies sessions there are no 4 s trains. Third, the Methods give an
interval of 20 s between trains in the frequencies sessions, while the conversion code's session
description says 10 s; the epoch starts show about 20 s. A few epochs are dropped: three
zero-length entries and seven trains whose window runs past the end of the recording. The
conversion code (`convert_session.py`) names the 1 s block of the STN to SNr GABA frequencies
sessions `s1s10mW`, which suggests 10 mW, while the epoch table and the Methods give 5 mW; the
data cannot settle this.''', '''The epoch tables give 5 mW at 635 nm for every train, as the Methods state, and the number of
pulses in each train fits its frequency and length. The intervals between trains are 10 s in the
durations sessions and 20 s in the frequencies sessions (offset to next onset), as the Methods
state; the files' session description of the frequencies protocol says 10 s, which the data do
not support. Three things differ from the Methods. First, 13 mice (SNr GABA and SNc pan-DA mice
with ids starting with B) have 10 trials per condition, where the Methods state 5. Second, 30
mice (SNr GABA, pan-DA and DA terminal mice recorded on the rig with a 24 kHz raw rate) also have
16 s trains, which the paper does not mention; they are not used. Third, 14 frequencies sessions
have no 4 s trains (the 13 mice above, and C4608, whose 4 s block the conversion notes describe
as a separate recording that is not in the dandiset). Fifteen epochs are dropped: nine
zero-length entries and six trains whose window runs past the end of the recording or across a
gap. The conversion code (`convert_session.py`) names the 1 s block of the STN to SNr GABA
frequencies sessions `s1s10mW`, which suggests 10 mW, while the epoch tables and the Methods give
5 mW; the data cannot settle this.''')

rep('''The stored dF/F agrees with a recomputation from the stored 465 and 405 nm signals following the
Methods (biexponential fit of the 405 nm signal, scaled to the 465 nm signal by robust
regression, in percent): the median correlation and difference are printed above. This is
consistent with the stored series being the lab's dF/F in percent. Where they differ most the
fit of a segment differs (the lab's exact fitting options are not public); the analysis uses the
stored dF/F.''', '''The stored dF/F agrees with a recomputation from the stored 465 and 405 nm signals following the
Methods (biexponential fit of the 405 nm signal, scaled to the 465 nm signal by robust
regression, in percent): median correlation 0.9999 in durations sessions and 0.9988 in
frequencies sessions, above 0.99 in 217 of 258 files, with a median absolute difference below
0.1 % dF/F. This is consistent with the stored series being the lab's dF/F in percent. In a few
files the two differ more (correlation down to 0.31), where the fit of a segment differs; the
lab's exact fitting options are not public. The analysis uses the stored dF/F.''')

rep('''For every group the response at the true onsets is several times that at onsets shifted by 3 s
either way, so the epoch tables share the clock of the dF/F. The recordings listed last are
those where the response at the true onsets does not exceed the shifted ones; there the clock
could not be shown from the data, and these recordings are used as they are. The shared time
base of the files (above) is consistent with this.''', '''In every group the median response at the true onsets is larger than at onsets shifted by 3 s
either way (median ratio 1.2 to 6.3 by group and protocol), and in 235 of 258 recordings the
response at the true onsets exceeds both shifted ones. The epoch tables share the clock of the
dF/F. The 23 recordings listed last, mostly SNc pan-DA recordings with small and variable
responses and unsuffixed Anxa1 recordings, are those where the clock could not be shown from
the response; they are used as they are.''')

rep('''favour the second: the unsuffixed recordings resemble the SNc recordings of the dual mice (small
inhibition, no rebound, similar variability), not their DLS recordings (larger inhibition and a
rebound). This is consistent with, but does not prove, that the labels are right and that DLS
recordings of nine mice are missing. The analysis keeps the dandiset's labels and shows the
other reading as a variant.''', '''favour the second: the unsuffixed recordings resemble the SNc recordings of the dual mice (small
inhibition, no rebound, similar variability), not their DLS recordings (larger inhibition and a
rebound). The tests of figs4-anxa1-soma-inhibited and fig5-anxa1-dls-inhibited below bear on this
too: the paper's cell-body statistics are matched by the dual mice's SNc recordings alone, and
its terminal statistics are not matched by adding the unsuffixed recordings to DLS. This is
consistent with, but does not prove, that the labels are right and that the DLS recordings of
nine mice are missing. The analysis keeps the dandiset's labels and shows the other reading as a
variant.''')
open('cells.py','w').write(s)
EOF
echo ok
```

```
ok
Shell cwd was reset to
```

**Agent**

Now the conclusions, in section order.

**Agent calls Bash**

```bash
cd $TMPDIR/gen && python - <<'EOF'
s = open('cells.py').read()
C = [
# cohort
'''**Result: not reproduced.** 10 of 16 counts match. The SNr GABA, pan-DA and GRAB-DA groups
match exactly, as do DA terminals in TS (9) and Vglut2 PPN (10). DA terminals in DLS have 8 mice
(paper 9) and Vglut2 STN 9 (paper 10). The four Anxa1 counts differ: DLS 5 and 4 against 8 and
10, SNc 8 and 10 against 5 and 4. All four Anxa1 counts would match if the unsuffixed recordings
were DLS recordings; the data check and the Anxa1 claims below favour the reading that the paper's
DLS recordings of those nine mice are not in the dandiset.''',
# fig2 excited
'''**Result: reproduced.** During 1 s 40 Hz trains SNr GABA activity rises above the pre-stimulus
window for STN (mean 18.89 %, t = 3.86, p = 0.0083, n = 7; paper t = 3.8, p = 0.008) and PPN
(6.45 %, t = 9.19, p = 3.7e-05, n = 8; paper t = 9.2). The 0.25 s and 4 s trains also give
significant increases (p from 1.4e-05 to 0.0066). All seven STN mice were recorded with 10
trials per condition.''',
# fig2 frequency
'''**Result: reproduced.** For 1 s trains the response rises from 5 to 40 Hz for STN (4.07 to
32.66 %, Friedman 21.00, p = 0.00011, 40 Hz above 5 Hz in 7 of 7 mice) and PPN (1.57 to 6.10 %,
18.15, p = 0.00041, 8 of 8), the paper's values to the first decimal. The repeated-measures ANOVA
variant gives p = 0.014 and 0.0001, and 0.25 s trains give the same Friedman values.''',
# fig3b
'''**Result: partially reproduced.** With the fixed window (peak from onset to 2.25 s) the mean
latency is 0.786 s (SEM 0.204, n = 11), outside 0.50 +/- 0.03 s, because two mice peak at the
window's end (2.03 and 2.24 s). Ten of 11 mice peak after offset and the net response over 0 to
1.25 s is positive (2.89 %, t = 3.28, p = 0.0083). With a window ending 1.25 s after onset (a
variant, which does not change the outcome) the mean latency is 0.492 s, SEM 0.033, the paper's
value.''',
# fig3c
'''**Result: reproduced.** The STN-evoked pan-DA response differs between train durations (mean
during 0.52, 0.97 and -3.13 % for 0.25, 1 and 4 s): reading (a), three durations, Friedman 13.64,
p = 0.0011; reading (b), with the pre-stimulus window as a fourth group, 12.93, p = 0.0048, which
matches the paper's F = 13.0, p = 0.005; reading (c), area under the curve, p = 0.06. In 4 s
trains the mean over the first 0.5 s (0.71 %) is above that over the last 1 s (-5.05 %) in all 11
mice (paired t = 4.81, p = 0.00071).''',
# fig3d
'''**Result: reproduced.** The paper's test finds no effect of frequency on the STN-evoked pan-DA
response to 1 s trains: Friedman 4.20, p = 0.24 (paper F = 4.2, p = 0.24), 40 minus 5 Hz 0.21 %.
The 0.25 s (p = 0.31) and 4 s (p = 0.18, 5 complete mice) variants also find none.''',
# fig3g
'''**Result: not reproduced.** For PPN stimulation the pan-DA response does not differ between
train durations under any reading (means -0.60, 1.03 and 0.70 %; Friedman p = 0.26, 0.25 and 0.46
for readings (a) to (c), n = 9), where the paper reports F = 11.5, p = 0.009.''',
# fig3h
'''**Result: reproduced.** The paper's test finds no effect of frequency on the PPN-evoked pan-DA
response to 1 s trains: F = 1.35 on Greenhouse-Geisser corrected df 1.85 and 14.8, p = 0.29 (paper
F2,15 = 1.35, p = 0.28); 40 minus 5 Hz is 1.30 %. The 0.25 s and 4 s variants give p = 0.83 and
0.32.''',
# fig4cf opposite
'''**Result: reproduced.** For 1 s 40 Hz trains GRAB-DA rises in TS and falls in DLS with both
inputs: STN, TS 12.45 % (6 of 6 mice above 0), DLS -8.91 % (7 of 7 below 0), site by time
interaction F(1, 11) = 40.9, p = 5.1e-05; PPN, TS 11.39 % (9 of 9), DLS -5.75 % (9 of 9),
F(1, 16) = 36.4, p = 1.7e-05. These are the paper's values. The 0.25 s and 4 s trains give the
same pattern (interaction p from 3.5e-06 to 0.00023).''',
# fig4dg
'''**Result: reproduced.** In TS all six tests find an effect of frequency with the 40 Hz mean
above the 5 Hz mean: STN repeated-measures ANOVA F = 7.62, 13.76 and 17.31 (p = 0.019, 0.0044,
0.0011; paper 7.5, 13.6, 16.9) and PPN Friedman 19.80, 24.33 and 23.27 (p = 0.0002 or below;
paper 20.0, 24.0, 23.2).''',
# fig4eh freq
'''**Result: reproduced.** In DLS all six tests find an effect of frequency with the 40 Hz mean
below the 5 Hz mean (p from below 0.0001 to 0.013). STN 0.25 s and 4 s give F = 7.89 and 47.23
(paper 7.5 and 46.8), PPN 0.25 s Friedman 11.53 (paper 12.3) and PPN 1 s F = 12.98 (paper 12.8).
STN 1 s gives F = 26.17, where the paper reports F1,11 = 12.8 with p = 0.0005, the same F and df
as it reports for PPN 1 s with p = 0.002; F(1, 11) = 12.8 gives p = 0.0043, so one of the two
entries in the paper is likely a copy.''',
# 5hz
'''**Result: not reproduced.** For 1 s trains at 5 Hz the mean GRAB-DA signal in DLS during the
train is positive but not significantly so for either input: STN 1.51 % (4 of 7 mice above 0,
p = 0.22), PPN 1.40 % (6 of 9, p = 0.13). In 4 s trains at 5 Hz it is above 0 for STN (5.41 %,
7 of 7, p = 0.00062) and not significantly for PPN (2.01 %, p = 0.07), and the 1 s after offset
is positive in every condition (0.96 to 6.76 %), as the paper's account of summed rebounds would
predict.''',
# rebound
'''**Result: partially reproduced.** After 1 s 40 Hz trains GRAB-DA in DLS rises above baseline
for PPN (4.53 %, 8 of 9 mice, p = 0.017) but not significantly for STN (0.87 %, 5 of 7, p =
0.29). After 0.25 s and 4 s trains the rebound is significant for both inputs (p from 0.0039 to
0.015).''',
# figs3
'''**Result: reproduced.** STN stimulation raises DA terminal calcium in TS (8.96 %, 9 of 9 mice
above 0) and lowers it in DLS (-4.41 %, 7 of 8 below 0) during 1 s trains; site by time
interaction F(1, 15) = 26.2, p = 0.00013. The 0.25 s and 4 s trains give the same pattern, and
the DLS terminals rebound after offset (6.73 %, 8 of 8 above 0).''',
# vglut2 excited
'''**Result: reproduced.** Vglut2+ DA neurons increase their activity during 0.25 s and 1 s trains
with both inputs: STN Wilcoxon W = 43 and 43 (p = 0.0078 each, n = 9; paper 41 and 43), PPN paired
t = 2.89 and 3.42 (p = 0.018 and 0.0076, n = 10; paper 2.9 and 3.4). For 4 s trains STN gives
W = -5, p = 0.82 (the paper's values) and PPN t = 2.56, p = 0.031 (paper t = 3.0, p = 0.01).''',
# vglut2 freq
'''**Result: reproduced.** The four tests the claim rests on find an effect of frequency with the
40 Hz mean above the 5 Hz mean: STN 0.25 s (Friedman 13.53, p = 0.0036) and PPN 0.25, 1 and 4 s
(11.23, 17.91 and 16.20; p = 0.011, 0.0005 and 0.0010). The PPN tests use 7 of 10 mice, those
with all four frequencies. As in the paper, STN 1 s and 4 s are not significant (p = 0.43 and
0.16; paper 0.11 and 0.07).''',
# anxa1 dls inhibited
'''**Result: blocked (data missing).** Every Anxa1 mouse with a DLS recording shows a lower mean
during the train than before it (0 of 5 STN and at most 1 of 4 PPN mice go up, in all six
conditions), but the dandiset holds DLS recordings for 5 (STN) and 4 (PPN) mice, where the paper
has 8 and 10. At these numbers the Wilcoxon tests the paper uses for three of the six conditions
cannot reach p < 0.05 (smallest p 0.0625 for 5 mice and 0.125 for 4), and 2 of 6 tests are
significant. With the unsuffixed recordings added to DLS (a variant), all 6 tests are significant
(W = -34, -36 and -51 against the paper's -36, -36 and -55; t = 2.65, 2.47 and 2.98 against 6.4,
3.9 and 3.8).''',
# anxa1 freq
'''**Result: partially reproduced.** Among Anxa1 DLS recordings, 5 of 6 tests find an effect of
frequency with the 40 Hz mean below the 5 Hz mean (p from 0.0043 to 0.026, with 5 STN and 4 PPN
mice); PPN 4 s does not (F = 1.95, p = 0.24). With the unsuffixed recordings added, 3 of 6 hold.
Two of the paper's Friedman entries do not fit their p-values (F = 11.5 gives p = 0.0093 against
the stated 0.0002; F = 15.5 gives 0.0014 against 0.015).''',
# anxa1 rebound
'''**Result: partially reproduced.** After 1 s trains Anxa1 DLS terminals rise above baseline for
STN (1.02 %, 5 of 5 mice, p = 0.0044) but not significantly for PPN (0.57 %, 3 of 4, p = 0.14,
n = 4). The same holds for 0.25 s and 4 s trains (STN p = 0.036 and 0.026; PPN p = 0.20 and 0.11).''',
# soma
'''**Result: partially reproduced.** Among the recordings labelled SNc (8 STN and 10 PPN mice), 5
of 6 tests show a significant decrease during the train (p from 0.0003 to 0.014); STN 0.25 s does
not (t = -1.56, p = 0.16). Restricted to the mice with both a DLS and an SNc file (5 and 4, the
paper's n; a variant), all 6 are significant with the paper's statistics (t = 3.13, 3.98, 7.26,
4.72, 8.35, 3.33 against 3.1, 4.0, 7.2, 4.8, 8.4, 3.3). No post-stimulus rebound is seen in the
cell bodies after 1 s trains (all SNc, STN -0.08 % and PPN 0.03 %, p = 0.65 and 0.80; dual mice
-0.15 % and 0.26 %, p = 0.53 and 0.16).''',
# opposite
'''**Result: reproduced.** During 1 s 40 Hz trains Vglut2+ SNc neurons rise and Anxa1+ DLS
terminals fall with both inputs: STN 6.54 % against -1.73 % (Welch t = 3.56, p = 0.0066), PPN
9.35 % against -1.48 % (t = 3.90, p = 0.0032). The difference holds with the unsuffixed Anxa1
recordings added to DLS (p = 0.0097 and 0.005) and against the Anxa1 SNc recordings (p = 0.017
and 0.0065).''',
]
parts = s.split("**Result: TBD**")
assert len(parts) == len(C) + 1, len(parts)
out = parts[0]
for c, p in zip(C, parts[1:]):
    out += c + p
s = out
summary = r"""
## Summary

A failure to reproduce here may be a failure of this attempt, not of the paper: see the reasoning
and the differences from the paper's method.

| Claim | Data | Outcome |
|---|---|---|
| cohort-sizes | dandiset | not reproduced |
| fig2-gaba-excited | dandiset | reproduced |
| fig2-gaba-frequency | dandiset | reproduced |
| fig3b-da-stn-250ms-peak | dandiset | partially reproduced |
| fig3c-da-stn-duration | dandiset | reproduced |
| fig3d-da-stn-frequency-ns | dandiset | reproduced |
| fig3g-da-ppn-duration | dandiset | not reproduced |
| fig3h-da-ppn-frequency-ns | dandiset | reproduced |
| fig4cf-ts-dls-opposite | dandiset | reproduced |
| fig4dg-ts-frequency | dandiset | reproduced |
| fig4eh-dls-frequency | dandiset | reproduced |
| fig4eh-dls-5hz-increase | dandiset | not reproduced |
| fig4cf-dls-rebound | dandiset | partially reproduced |
| figs3-terminals-opposite | dandiset | reproduced |
| fig5-vglut2-excited | dandiset | reproduced |
| fig5-vglut2-frequency | dandiset | reproduced |
| fig5-anxa1-dls-inhibited | dandiset | blocked: data missing |
| fig5-anxa1-dls-frequency | dandiset | partially reproduced |
| fig5-anxa1-dls-rebound | dandiset | partially reproduced |
| figs4-anxa1-soma-inhibited | dandiset | partially reproduced |
| fig5-opposite-subtypes | dandiset | reproduced |
| fig1de, fig1f, figs1 counts, figs1 IF (human tissue) | dandiset | blocked: data missing |

**How the analysis differs from the paper's.** It uses the lab's dF/F stored in the files, the
Methods' 1 s baseline, and windows the Methods do not give: the mean during the train, a
pre-stimulus window of the train's length, and the 1 s after offset. Where a panel shows one
train duration without saying which, the 1 s train is used. The paper chose between parametric
and non-parametric tests by a Shapiro-Wilk test; here each comparison uses the test the paper
reports for it. Repeated-measures ANOVAs are Greenhouse-Geisser corrected, as the paper's
fractional degrees of freedom imply. For many comparisons this reproduces the paper's statistic
to the first decimal, which suggests the windows match the lab's. The Anxa1 groups follow the
dandiset's site labels.

**What was found about the dandiset.**

- It holds the photometry of Figures 2 to 5, S3 and S4 for 120 mice; the human tissue counts of
  Figure 1 and S1 and the histology of Figure S2 are not in it.
- For the Anxa1 mice it holds DLS terminal recordings for 5 (STN) and 4 (PPN) mice where the paper
  has 8 and 10, and SNc recordings for 8 and 10 where the paper has 5 and 4. The nine extra SNc
  recordings carry no site suffix in their file names; their signals resemble the SNc recordings,
  and the paper's cell-body statistics are matched by the other SNc recordings alone. The DLS
  recordings of nine mice appear to be missing.
- DA terminals in DLS have 8 mice (paper 9) and Vglut2+ neurons with STN stimulation 9 (paper 10).
- The dF/F is stated in "a.u." but is in percent.
- Thirteen mice have 10 trials per condition (Methods: 5), 30 mice have 16 s trains the paper does
  not mention, and 14 frequencies sessions have no 4 s trains, one of them (C4608) because a
  separate recording was not converted.
- Every session start time carries the offset -00:01, an artefact of attaching the London time
  zone with `replace`, so the true offset is lost; eight subject ids are lower case.
- The files' description of the frequencies protocol gives an interval of 10 s between trains;
  the epochs and the Methods give 20 s.
- The conversion code names the 1 s block of the STN to SNr GABA frequencies sessions as 10 mW,
  while the files and the Methods give 5 mW.
- The epoch tables share the clock of the dF/F (the responses lock to the true onsets in 235 of
  258 recordings), and no recording is deposited twice.
- The dandiset has no published version, so results hold for the draft as modified on
  2026-09-01.
"""
s = s.replace('''md(r\'\'\'
## Summary

TBD
\'\'\')''', 'md(r"""' + summary + '""")')
assert 'TBD' not in s
open('cells.py','w').write(s)
EOF
grep -c "Result:" $TMPDIR/gen/cells.py
```

```
21
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/gen && python - <<'EOF'
s = open('cells.py').read()
old = '''**Result: blocked (data missing).** Every Anxa1 mouse with a DLS recording shows a lower mean
during the train than before it (0 of 5 STN and at most 1 of 4 PPN mice go up, in all six
conditions), but'''
new = '''**Result: blocked (data missing).** Anxa1 DLS terminals fall during the train: no STN mouse (of
5) goes up in any condition, and no PPN mouse (of 4) except one in 4 s trains. But'''
assert old in s; s = s.replace(old, new); open('cells.py','w').write(s)
EOF
cd $TMPDIR && . scratch/bin/activate && python gen/build.py
```

```
85 cells
Shell cwd was reset to
```

**Agent**

Now entry.yaml, requirements.in and README, then lock and run with the registry tool.

**Agent calls Bash**

```bash
cd entries/001528-hadjas-2025 && cat > entry.yaml <<'EOF'
schema_version: 1
name: 001528-hadjas-2025
type: reproduction
title: Responses of SNr GABA and SNc dopamine neuron subtypes to STN and PPN input (Hadjas et al. 2025)
description: Tests the mouse fiber photometry findings of Hadjas et al. (2025) on dandiset 001528,
  which holds recordings from 120 mice during optogenetic stimulation of STN or PPN inputs to the
  substantia nigra. It compares responses of SNr GABA neurons, SNc pan-DA neurons, striatal
  dopamine release in TS and DLS, DA terminals, and Vglut2+ and Anxa1+ DA neurons across train
  durations and frequencies, using the lab's dF/F stored in the files. The human tissue counts of
  Figure 1 are not in the dandiset.
license: Apache-2.0
notebooks:
- path: reproduce_hadjas_2025.ipynb
  title: Reproducing Hadjas et al. (2025) from dandiset 001528
  runtime_minutes: 5
helpers:
- photometry.py
related:
- id: dandi:001528/draft
  relation: uses_data
- id: doi:10.1101/2025.06.03.657460
  relation: reproduces
EOF
printf "dandi\nh5py\nmatplotlib\nnumpy\npandas\nremfile\nscipy\nstatsmodels\n" > requirements.in
cat ../001453-fouke-2025/requirements.lock.txt | head -5; cat schemas/entry.schema.json | python -c "import json,sys; d=json.load(sys.stdin); print(json.dumps(d['properties']['related'],indent=0)[:600])"
```

```
# This file was autogenerated by uv via the following command:
#    uv pip compile --python-version 3.13 requirements.in -o requirements.lock.txt
acres==0.5.0
    # via bidsschematools
aiohappyeyeballs==2.7.1
{
"type": "array",
"minItems": 1,
"items": {
"type": "object",
"additionalProperties": false,
"required": [
"id",
"relation"
],
"properties": {
"id": {
"description": "dandi:<id>[/<version>], doi:<doi>, or entry:<name>.",
"type": "string",
"pattern": "^(dandi:[0-9]{6}(/.+)?|doi:10\\.[0-9]{4,9}/.+|entry:[a-z0-9]+(-[a-z0-9]+)*)$"
[... 12 more lines not kept]
```

**Agent calls Bash**

```bash
cd  && python tools/entry.py lock entries/001528-hadjas-2025 2>&1 | tail -5 && sed -n 280,360p tools/entry.py
```

```
wrote entries/001528-hadjas-2025/requirements.lock.txt


def run(entry_dir: Path, output_dir: Path, timeout: int, max_minutes: float) -> int:
    entry = yaml.safe_load((entry_dir / "entry.yaml").read_text())
    output_dir.mkdir(parents=True, exist_ok=True)
    venv = (output_dir / ".venv").resolve()
    python = venv / "bin" / "python"
    # A kernel of the entry's own environment, under a name no other kernel on the machine has, so
    # nbconvert cannot pick up some other "python3" kernel (a user's or a conda install's).
    kernel = f"registry-{entry_dir.name}"
    for cmd in (["uv", "venv", "--quiet", "--clear", "--python", PYTHON_VERSION, str(venv)],
                ["uv", "pip", "install", "--quiet", "--python", str(python),
                 "-r", str(entry_dir / "requirements.lock.txt"), *HARNESS],
                [str(python), "-m", "ipykernel", "install", "--prefix", str(venv), "--name", kernel]):
        if subprocess.run(cmd).returncode != 0:
            print(f"error: could not build the environment ({' '.join(cmd[:3])})", file=sys.stderr)
            return 1

    results, failed = [], False
[... 62 more lines not kept]
```

**Agent**

Writing the attempt record before running the full check.

**Agent calls Bash**

```bash
python -c "
import json;d=json.load(open('schemas/attempt.schema.json'))
p=d['properties']
print(json.dumps(p['outcomes']['items'],indent=0)[:2500]); print(json.dumps(p['findings'],indent=0)[:1200]); print(json.dumps(p['inputs'],indent=0)[:600]); print(list(p))
print(json.dumps(p['provenance']['properties']['agent'],indent=0)[:800])"
```

```
{
"type": "object",
"additionalProperties": false,
"required": [
"claim",
"outcome"
],
"properties": {
"claim": {
"description": "Claim id from the target's claims file.",
"type": "string"
},
"outcome": {
"enum": [
"reproduced",
"partially_reproduced",
"not_reproduced",
"blocked"
],
"description": "Describes the result, not the method: whether the effect the claim states was found. Differences in method from the paper go in `deviations`."
[... 180 more lines not kept]
```

**Agent calls Write**

```json
{
 "file_path": "attempts/001528-hadjas-2025-01.yaml",
 "content": "schema_version: 1\nid: 001528-hadjas-2025-01\ndandiset: \"001528\"\ndandiset_version: draft\npaper: doi:10.1101/2025.06.03.657460\ndate: 2026-10-18\nentry: 001528-hadjas-2025\nprovenance:\n  kind: agent\n  accountable:\n    name: CatalystNeuro\n  agent:\n    harness: Claude Code (GitHub Actions)\n    model: claude-opus-5-5\n    protocol: pilot-7\noutcomes:\n- claim: cohort-sizes\n  outcome: not_reproduced\n  notebook: reproduce_hadjas_2025.ipynb\n  output: claim:cohort-sizes\n  measured: [7, 8, 11, 9, 6, 7, 9, 9, 9, 8, 9, 10, 5, 4, 8, 10]\n  notes: 10 of 16 counts match. SNr GABA, pan-DA and GRAB-DA groups match exactly, as do DA\n    terminals in TS and Vglut2 with PPN. DA terminals in DLS have 8 mice (paper 9) and Vglut2 with\n    STN 9 (paper 10). The Anxa1 groups have DLS recordings for 5 (STN) and 4 (PPN) mice against the\n    paper's 8 and 10, and SNc recordings for 8 and 10 against 5 and 4. All four Anxa1 counts would\n    match if the nine recordings without a site suffix were DLS recordings; their signals resemble\n    the SNc recordings, and the paper's cell-body statistics are matched by the dual mice's SNc\n    recordings alone, so the DLS recordings of those nine mice appear to be missing.\n  deviations:\n  - Counted from the durations protocol; the frequencies protocol gives the same counts.\n- claim: fig2-gaba-excited\n  outcome: reproduced\n  notebook: reproduce_hadjas_2025.ipynb\n  output: claim:fig2-gaba-excited\n  notes: 1 s 40 Hz trains, mean during the train against the 1 s before onset. STN mean 18.89 %\n    dF/F, paired t = 3.86, p = 0.0083, n = 7 (paper t = 3.8, p = 0.008); PPN 6.45 %, t = 9.19, p =\n    3.7e-05, n = 8 (paper t = 9.2). The 0.25 and 4 s trains also give significant increases (p\n    1.4e-05 to 0.0066).\n  deviations:\n  - The response window (mean during the train) and pre-stimulus window (same length, before\n    onset) are choices; the paper does not state them.\n  - All seven STN mice have 10 trials per condition, where the Methods state 5.\n- claim: fig2-gaba-frequency\n  outcome: reproduced\n  notebook: reproduce_hadjas_2025.ipynb\n  output: claim:fig2-gaba-frequency\n  notes: 1 s trains of the frequencies protocol. STN means rise from 4.07 to 32.66 % between 5 and\n    40 Hz, Friedman 21.00, p = 0.00011, 7 of 7 mice higher at 40 than 5 Hz; PPN 1.57 to 6.10 %,\n    Friedman 18.15, p = 0.00041, 8 of 8 (paper 21.0 and 18.2). A repeated-measures ANOVA variant\n    gives p = 0.014 and 0.0001.\n  deviations:\n  - The conversion code names the STN 1 s block of these mice as 10 mW, while the files and the\n    Methods give 5 mW; the analysis takes the files as they are.\n- claim: fig3b-da-stn-250ms-peak\n  outcome: partially_reproduced\n  notebook: reproduce_hadjas_2025.ipynb\n  output: claim:fig3b-da-stn-250ms-peak\n  measured: 0.786\n  notes: With the window fixed in the criterion (peak from onset to 2.25 s) the mean latency is\n    0.786 s, SEM 0.204, n = 11, outside 0.50 +/- 0.03 s, because two mice peak at 2.03 and 2.24 s.\n    Ten of 11 mice peak after offset and the net response over 0 to 1.25 s is positive (2.89 %, t\n    = 3.28, p = 0.0083). With a window ending at 1.25 s, a variant, the mean latency is 0.492 s,\n    SEM 0.033, the paper's value.\n  deviations:\n  - The paper does not give the window in which the peak is sought; the criterion fixed 0 to 2.25\n    s, and the variant 0 to 1.25 s matches the paper.\n- claim: fig3c-da-stn-duration\n  outcome: reproduced\n  notebook: reproduce_hadjas_2025.ipynb\n  output: claim:fig3c-da-stn-duration\n  notes: Means during 0.25, 1 and 4 s trains are 0.52, 0.97 and -3.13 %, n = 11. Reading (a),\n    Friedman over three durations, 13.64, p = 0.0011; reading (b), with the pre-stimulus window as a\n    fourth group, 12.93, p = 0.0048, matching the paper's F = 13.0, p = 0.005; reading (c), area\n    under the curve, p = 0.06. In 4 s trains the first 0.5 s (0.71 %) is above the last 1 s (-5.05\n    %) in all 11 mice, paired t = 4.81, p = 0.00071.\n  deviations:\n  - The paper's F and p fit four groups while three durations were tested; readings (a) and (b)\n    match, and (b) gives the paper's value.\n- claim: fig3d-da-stn-frequency-ns\n  outcome: reproduced\n  notebook: reproduce_hadjas_2025.ipynb\n  output: claim:fig3d-da-stn-frequency-ns\n  notes: 1 s trains, Friedman 4.20, p = 0.24, n = 11 (paper F = 4.2, p = 0.24); 40 minus 5 Hz 0.21\n    % dF/F. Variants with 0.25 s (p = 0.31) and 4 s trains (p = 0.18, 5 mice with all four\n    frequencies) also find no effect.\n  deviations:\n  - The paper does not say which train duration Figure 3D shows; the 1 s train was fixed in the\n    criterion.\n- claim: fig3g-da-ppn-duration\n  outcome: not_reproduced\n  notebook: reproduce_hadjas_2025.ipynb\n  output: claim:fig3g-da-ppn-duration\n  notes: Means during 0.25, 1 and 4 s PPN trains are -0.60, 1.03 and 0.70 %, n = 9. Friedman p =\n    0.26, 0.25 and 0.46 under readings (a) to (c), where the paper reports F = 11.5, p = 0.009.\n  deviations:\n  - The paper's measure for this comparison is not stated; the mean during the train (and the area\n    under the curve) were used, as for the STN comparison, which matches the paper there.\n- claim: fig3h-da-ppn-frequency-ns\n  outcome: reproduced\n  notebook: reproduce_hadjas_2025.ipynb\n  output: claim:fig3h-da-ppn-frequency-ns\n  notes: 1 s trains, repeated-measures ANOVA F = 1.35 on Greenhouse-Geisser corrected df 1.85 and\n    14.8, p = 0.29, n = 9 (paper F2,15 = 1.35, p = 0.28); 40 minus 5 Hz 1.30 %. Variants with 0.25\n    and 4 s trains give p = 0.83 and 0.32.\n  deviations:\n  - The 1 s train was fixed in the criterion, as the paper does not name the duration.\n- claim: fig4cf-ts-dls-opposite\n  outcome: reproduced\n  notebook: reproduce_hadjas_2025.ipynb\n  output: claim:fig4cf-ts-dls-opposite\n  notes: GRAB-DA, 1 s 40 Hz trains. STN, TS 12.45 % (6 of 6 above 0), DLS -8.91 % (7 of 7 below\n    0), site by time interaction F(1, 11) = 40.9, p = 5.1e-05; PPN, TS 11.39 % (9 of 9), DLS -5.75\n    % (9 of 9), F(1, 16) = 36.4, p = 1.7e-05, the paper's values. The 0.25 and 4 s trains give the\n    same pattern.\n- claim: fig4dg-ts-frequency\n  outcome: reproduced\n  notebook: reproduce_hadjas_2025.ipynb\n  output: claim:fig4dg-ts-frequency\n  notes: All six tests hold, with the 40 Hz mean above the 5 Hz mean. STN repeated-measures ANOVA F\n    = 7.62, 13.76, 17.31 for 0.25, 1 and 4 s (p = 0.019, 0.0044, 0.0011; paper 7.5, 13.6, 16.9);\n    PPN Friedman 19.80, 24.33, 23.27 (p at most 0.0002; paper 20.0, 24.0, 23.2).\n- claim: fig4eh-dls-frequency\n  outcome: reproduced\n  notebook: reproduce_hadjas_2025.ipynb\n  output: claim:fig4eh-dls-frequency\n  notes: All six tests hold, with the 40 Hz mean below the 5 Hz mean (p below 0.0001 to 0.013). STN\n    0.25 and 4 s F = 7.89 and 47.23 (paper 7.5, 46.8); PPN 0.25 s Friedman 11.53 (paper 12.3), PPN\n    1 and 4 s F = 12.98 and 15.92 (paper 12.8, 10.2). STN 1 s gives F = 26.17 where the paper gives\n    F1,11 = 12.8, p = 0.0005, the same F and df it gives for PPN 1 s.\n- claim: fig4eh-dls-5hz-increase\n  outcome: not_reproduced\n  notebook: reproduce_hadjas_2025.ipynb\n  output: claim:fig4eh-dls-5hz-increase\n  notes: 1 s trains at 5 Hz, mean GRAB-DA in DLS during the train, STN 1.51 % (4 of 7 above 0, p =\n    0.22), PPN 1.40 % (6 of 9, p = 0.13). For 4 s trains, a variant, STN 5.41 % (7 of 7, p =\n    0.00062) and PPN 2.01 % (p = 0.07). The 1 s after offset is positive in all six conditions\n    (0.96 to 6.76 %).\n  deviations:\n  - The paper does not state the window or test for this observation; the mean during 1 s trains\n    against 0 was fixed in the criterion. The effect is present for STN 4 s trains, which the paper\n    also cites (Figure S3F).\n- claim: fig4cf-dls-rebound\n  outcome: partially_reproduced\n  notebook: reproduce_hadjas_2025.ipynb\n  output: claim:fig4cf-dls-rebound\n  notes: After 1 s 40 Hz trains, PPN 4.53 % (8 of 9 above 0, p = 0.017), STN 0.87 % (5 of 7, p =\n    0.29). After 0.25 and 4 s trains the rebound is significant for both inputs (p 0.0039 to\n    0.015).\n  deviations:\n  - The rebound window (1 s after offset) and test are choices; the paper gives no statistic.\n- claim: figs3-terminals-opposite\n  outcome: reproduced\n  notebook: reproduce_hadjas_2025.ipynb\n  output: claim:figs3-terminals-opposite\n  notes: DA terminal GCaMP, 1 s trains, TS 8.96 % (9 of 9 above 0), DLS -4.41 % (7 of 8 below 0),\n    site by time interaction F(1, 15) = 26.2, p = 0.00013. The DLS terminals rebound after offset\n    (6.73 %, 8 of 8 above 0).\n  deviations:\n  - 8 DLS mice, where the paper has 9.\n- claim: fig5-vglut2-excited\n  outcome: reproduced\n  notebook: reproduce_hadjas_2025.ipynb\n  output: claim:fig5-vglut2-excited\n  notes: STN Wilcoxon W = 43 and 43 for 0.25 and 1 s (p = 0.0078 each, n = 9; paper 41 and 43);\n    PPN paired t = 2.89 and 3.42 (p = 0.018 and 0.0076, n = 10; paper 2.9 and 3.4). For 4 s trains\n    STN W = -5, p = 0.82 as in the paper, and PPN t = 2.56, p = 0.031 (paper 3.0, p = 0.01).\n  deviations:\n  - 9 STN mice, where the paper has 10.\n- claim: fig5-vglut2-frequency\n  outcome: reproduced\n  notebook: reproduce_hadjas_2025.ipynb\n  output: claim:fig5-vglut2-frequency\n  notes: STN 0.25 s Friedman 13.53, p = 0.0036; PPN 0.25, 1 and 4 s 11.23, 17.91, 16.20 (p = 0.011,\n    0.0005, 0.0010), all with the 40 Hz mean above the 5 Hz mean. STN 1 and 4 s are not significant\n    (p = 0.43 and 0.16), as in the paper (0.11 and 0.07).\n  deviations:\n  - The PPN tests use the 7 of 10 mice that have all four frequencies (three frequencies sessions\n    lack 5 Hz trains).\n- claim: fig5-anxa1-dls-inhibited\n  outcome: blocked\n  blocked_by: data_missing\n  notebook: reproduce_hadjas_2025.ipynb\n  output: claim:fig5-anxa1-dls-inhibited\n  notes: The dandiset holds Anxa1 DLS recordings for 5 (STN) and 4 (PPN) mice where the paper has 8\n    and 10. At these numbers the Wilcoxon tests the paper uses for three of the six conditions cannot\n    reach p < 0.05 (smallest p 0.0625 and 0.125), so the claim cannot be tested by its criterion; 2\n    of 6 tests are significant. No STN mouse goes up in any condition, and one PPN mouse in 4 s\n    trains. With the nine recordings without a site suffix added to DLS, a variant, all 6 tests are\n    significant, but the statistics differ from the paper's (W = -34, -36, -51 against -36, -36,\n    -55; t = 2.65, 2.47, 2.98 against 6.4, 3.9, 3.8), where the cell-body statistics match exactly\n    with the dual mice. The DLS recordings of the nine mice appear not to be in the dandiset.\n- claim: fig5-anxa1-dls-frequency\n  outcome: partially_reproduced\n  notebook: reproduce_hadjas_2025.ipynb\n  output: claim:fig5-anxa1-dls-frequency\n  notes: With the dandiset's DLS recordings (5 STN, 4 PPN mice) 5 of 6 tests hold (p 0.0043 to\n    0.026, 40 Hz below 5 Hz); PPN 4 s does not (F = 1.95, p = 0.24). With the unsuffixed recordings\n    added, 3 of 6 hold.\n  deviations:\n  - 5 and 4 mice, where the paper has 8 and 10 (see fig5-anxa1-dls-inhibited).\n- claim: fig5-anxa1-dls-rebound\n  outcome: partially_reproduced\n  notebook: reproduce_hadjas_2025.ipynb\n  output: claim:fig5-anxa1-dls-rebound\n  notes: After 1 s trains, STN 1.02 % (5 of 5 above 0, p = 0.0044), PPN 0.57 % (3 of 4, p = 0.14).\n    The 0.25 and 4 s trains give the same picture (STN p = 0.036 and 0.026, PPN p = 0.20 and\n    0.11).\n  deviations:\n  - 5 and 4 mice, where the paper has 8 and 10.\n  - The rebound window (1 s after offset) and test are choices; the paper gives no statistic.\n- claim: figs4-anxa1-soma-inhibited\n  outcome: partially_reproduced\n  notebook: reproduce_hadjas_2025.ipynb\n  output: claim:figs4-anxa1-soma-inhibited\n  notes: With all SNc-labelled recordings (8 STN, 10 PPN mice) 5 of 6 tests show a significant\n    decrease (p 0.0003 to 0.014); STN 0.25 s does not (t = -1.56, p = 0.16). Restricted to the mice\n    with both a DLS and an SNc file (5 and 4, the paper's n), a variant, all 6 are significant with\n    the paper's statistics (t = 3.13, 3.98, 7.26, 4.72, 8.35, 3.33 against 3.1, 4.0, 7.2, 4.8, 8.4,\n    3.3). The statement's post-stimulus rebound is not seen in the cell bodies after 1 s trains (STN\n    -0.08 %, PPN 0.03 %, p = 0.65 and 0.80; dual mice p = 0.53 and 0.16).\n  deviations:\n  - The dandiset labels 8 and 10 mice as SNc where the paper analysed 5 and 4; the outcome uses the\n    dandiset's labels as fixed in the criterion.\n- claim: fig5-opposite-subtypes\n  outcome: reproduced\n  notebook: reproduce_hadjas_2025.ipynb\n  output: claim:fig5-opposite-subtypes\n  notes: 1 s 40 Hz trains. STN, Vglut2 6.54 % against Anxa1 DLS -1.73 % (Welch t = 3.56, p =\n    0.0066); PPN 9.35 % against -1.48 % (t = 3.90, p = 0.0032). It holds with the unsuffixed Anxa1\n    recordings added to DLS (p = 0.0097 and 0.005) and against the Anxa1 SNc recordings (p = 0.017\n    and 0.0065).\n  deviations:\n  - Anxa1 DLS recordings of 5 and 4 mice, where the paper has 8 and 10.\n- claim: fig1de-th-anxa1-reduced\n  outcome: blocked\n  blocked_by: data_missing\n  notes: The human RNAscope counts are not in the dandiset, which holds mouse photometry only. The\n    preprint has no data availability statement, and the dandiset metadata and the conversion\n    repository link no other deposit.\n- claim: fig1f-anxa1-de-enriched\n  outcome: blocked\n  blocked_by: data_missing\n  notes: Human tissue counts are not in the dandiset nor in any deposit the paper or the dandiset\n    names (see fig1de-th-anxa1-reduced).\n- claim: figs1-calb1-aldh1a1-counts\n  outcome: blocked\n  blocked_by: data_missing\n  notes: Human tissue counts are not in the dandiset nor in any deposit the paper or the dandiset\n    names (see fig1de-th-anxa1-reduced).\n- claim: figs1-if-aldh1a1\n  outcome: blocked\n  blocked_by: data_missing\n  notes: Human immunofluorescence counts are not in the dandiset nor in any deposit the paper or\n    the dandiset names (see fig1de-th-anxa1-reduced).\ninputs: []\nfindings:\n- kind: data_missing\n  statement: For the Anxa1 mice the dandiset holds DLS terminal recordings for 5 (STN) and 4 (PPN)\n    mice where the paper analyses 8 and 10. Nine mice (C5903, C5906, C5992, C6900, C6902, C7244,\n    C7245, C7248, C7249) have only recordings labelled SNc, without a site suffix in the file\n    name. Their signals resemble SNc recordings, and the paper's cell-body statistics are\n    reproduced exactly by the other nine mice's SNc recordings, so the DLS recordings of these nine\n    mice appear not to be deposited, and the nine SNc recordings were not used in the paper.\n- kind: selection_undocumented\n  statement: The dandiset includes Anxa1 SNc recordings from nine mice that the paper's cell-body\n    analysis (n = 5 and 4) leaves out, and it does not say which recordings the paper used.\n- kind: data_missing\n  statement: The human RNAscope and immunofluorescence counts of Figure 1 and Figure S1 and the\n    histology of Figure S2 are not in the dandiset, and the preprint has no data availability\n    statement.\n- kind: data_missing\n  statement: DA terminals in DLS have 8 mice where Figure S3 gives 9, and Vglut2+ neurons with STN\n    stimulation 9 where Figure 5 gives 10.\n- kind: data_missing\n  statement: Subject C4608 (SNr GABA, PPN) has no 4 s trains in its frequencies session; the\n    conversion notes say they were recorded in a separate session, which is not in the dandiset.\n- kind: metadata_error\n  statement: The dF/F series are stated in a.u. but hold percent (100 times (Gc - fit) / fit); a\n    recomputation from the stored signals agrees with a median correlation of 0.9999 (durations)\n    and 0.9988 (frequencies).\n- kind: metadata_error\n  statement: Every session start time carries the offset -00:01, the local mean time of London that\n    pytz gives when a time zone is attached with replace; the true offset is lost.\n- kind: metadata_error\n  statement: The session description of the frequencies protocol gives an interval of 10 s between\n    trains; the epochs and the Methods give 20 s.\n- kind: other\n  statement: Thirteen mice (SNr GABA and pan-DA, ids starting with B) have 10 trials per condition\n    where the Methods state 5, and 30 mice have 16 s trains that the paper does not mention.\n- kind: code_mismatch\n  statement: The conversion code names the 1 s block of the STN to SNr GABA frequencies sessions\n    s1s10mW, suggesting 10 mW, while the epoch tables and the Methods give 5 mW.\n- kind: code_mismatch\n  statement: The conversion repository's Python re-implementation of the dF/F forces the robust fit\n    through the origin, saying the MATLAB version does so, while its own description of the MATLAB\n    scripts includes an intercept; it also gives the calcium channel as demodulated at 330 Hz and\n    the isosbestic at 210 Hz, while the Methods and the files' device descriptions give 465 nm at\n    210 Hz and 405 nm at 330 Hz.\n- kind: metadata_insufficient\n  statement: The file names and session ids of nine Anxa1 mice carry no recording site, and every\n    Anxa1 file lists both an SNc and a DLS fiber in its fiber photometry table, so the site rests\n    on the name of the dF/F series alone.\n- kind: other\n  statement: Eight subject ids are written in lower case (c3015, c3016, c4379, c4708, c4709, c4977,\n    c4978, c5113) while the others are upper case.\n- kind: paper_inconsistency\n  statement: The Results give F1,11 = 12.8 for the DLS frequency effect with 1 s trains for both STN\n    (p = 0.0005) and PPN (p = 0.002); F(1, 11) = 12.8 gives p = 0.0043, and the data give F = 26.2\n    for STN. Two Friedman entries for Anxa1 terminals also do not fit their p-values (F = 11.5 with\n    p = 0.0002, F = 15.5 with p = 0.015; with 3 df these give 0.0093 and 0.0014).\n- kind: methods_unavailable\n  statement: The lab's MATLAB analysis scripts are not public; the preprint names custom MATLAB code\n    and has no code availability statement. The conversion repository describes them.\n- kind: other\n  statement: The dandiset has no published version; this attempt used the draft as modified on\n    2026-09-01T15:27:47Z.\n"
}
```

```
File created successfully at: attempts/001528-hadjas-2025-01.yaml (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd $TMPDIR && . scratch/bin/activate && python -c "
import pickle; recs=pickle.load(open('recs.pkl','rb'))
for r in recs:
    if r['protocol']=='frequencies' and 5.0 not in set(r['epochs'].frequency): print(r['path'], r['group'], r['input'])
"
```

```
sub-C3412/sub-C3412_ses-varying-frequencies.nwb Vglut2 PPN
sub-C3798/sub-C3798_ses-varying-frequencies.nwb Vglut2 PPN
sub-C4707/sub-C4707_ses-varying-frequencies.nwb Vglut2 PPN
Shell cwd was reset to
```

**Agent calls Bash**

```bash
python - <<'EOF'
p='attempts/001528-hadjas-2025-01.yaml'
s=open(p).read()
old = s[s.index("- kind: code_mismatch\n  statement: The conversion repository's Python"):s.index("- kind: metadata_insufficient")]
new = """- kind: code_mismatch
  statement: The conversion repository's Python re-implementation of the dF/F forces the robust fit
    through the origin, saying the MATLAB version does so, while its own description of the MATLAB
    scripts includes an intercept.
- kind: metadata_error
  statement: The files describe the modulation inconsistently. The excitation source descriptions
    give 465 nm modulated at 210 Hz and 405 nm at 330 Hz, as the Methods do, while the processed
    series descriptions give the calcium signal as demodulated at 330 Hz and the isosbestic signal at
    210 Hz, as the conversion repository's description of the MATLAB scripts does. This attempt did
    not check which is right against the raw signal.
"""
s = s.replace(old, new)
open(p,'w').write(s)
import yaml, json, jsonschema
d = yaml.safe_load(open(p))
jsonschema.validate(d, json.load(open('schemas/attempt.schema.json')))
# check for ': ' in plain scalars: scan raw lines that are continuation or values
import re
for i,l in enumerate(open(p).read().splitlines()):
    body = re.sub(r'^\s*-?\s*[a-z_]+: ', '', l, count=1) if re.match(r'^\s*-?\s*[a-z_]+: ', l) else l
    if ': ' in body or ' #' in body: print(i+1, l)
print('ok', len(d['outcomes']))
EOF
python - <<'EOF'
import re
for p in ['claims/001528/10.1101-2025.06.03.657460.yaml']:
    for i,l in enumerate(open(p).read().splitlines()):
        if l.lstrip().startswith('#'): continue
        body = re.sub(r'^\s*-?\s*[a-z_]+: ', '', l, count=1) if re.match(r'^\s*-?\s*[a-z_]+: ', l) else l
        if (': ' in body and not body.strip().startswith('{')) or ' #' in body: print(i+1, l)
EOF
```

```
Traceback (most recent call last):
  File "<stdin>", line 19, in <module>
  File "/opt/hostedtoolcache/Python/3.13.16/x64/lib/python3.13/site-packages/jsonschema/validators.py", line 1332, in validate
    raise error
jsonschema.exceptions.ValidationError: datetime.date(2026, 10, 18) is not of type 'string'

Failed validating 'type' in schema['properties']['date']:
    {'type': 'string', 'format': 'date'}

On instance['date']:
    datetime.date(2026, 10, 18)
52   - {quantity: "SNr GABA, STN", value: 7, tolerance: 0, unit: mice}
53   - {quantity: "SNr GABA, PPN", value: 8, tolerance: 0, unit: mice}
54   - {quantity: "SNc pan-DA, STN", value: 11, tolerance: 0, unit: mice}
55   - {quantity: "SNc pan-DA, PPN", value: 9, tolerance: 0, unit: mice}
56   - {quantity: "GRAB-DA TS, STN", value: 6, tolerance: 0, unit: mice}
57   - {quantity: "GRAB-DA DLS, STN", value: 7, tolerance: 0, unit: mice}
58   - {quantity: "GRAB-DA TS, PPN", value: 9, tolerance: 0, unit: mice}
59   - {quantity: "GRAB-DA DLS, PPN", value: 9, tolerance: 0, unit: mice}
60   - {quantity: "DA terminals TS, STN", value: 9, tolerance: 0, unit: mice}
[... 7 more lines not kept]
```

**Agent**

Schema date issue is only my ad-hoc validator (the tool converts dates; the example uses the same form). Writing the entry README and running `lock` + `all`.

**Agent calls Write**

```json
{
 "file_path": "entries/001528-hadjas-2025/README.md",
 "content": "# Hadjas et al. (2025) from dandiset 001528\n\nTests the mouse findings of [Hadjas et al. (2025)](https://doi.org/10.1101/2025.06.03.657460) on\n[DANDI:001528](https://dandiarchive.org/dandiset/001528/draft), which holds fiber photometry from\n120 mice during optogenetic stimulation of STN or PPN inputs to the substantia nigra (Figures 2\nto 5, S3 and S4). The dandiset has no published version; the draft as modified on 2026-09-01 was\nused. The human tissue counts of Figure 1 are not in it.\n\n| Claim | Outcome |\n|---|---|\n| Mice per group as in the figure legends | Not reproduced |\n| SNr GABA neurons are excited by STN and PPN input | Reproduced |\n| The SNr GABA response scales with frequency | Reproduced |\n| Pan-DA response to a 250 ms STN train peaks 0.50 s after onset | Partially reproduced |\n| Pan-DA response to STN input varies with train duration | Reproduced |\n| Pan-DA response to STN input does not scale with frequency | Reproduced |\n| Pan-DA response to PPN input varies with train duration | Not reproduced |\n| Pan-DA response to PPN input does not vary with frequency | Reproduced |\n| Opposite DA release in TS and DLS | Reproduced |\n| TS DA release scales with frequency | Reproduced |\n| DLS DA inhibition scales with frequency | Reproduced |\n| 5 Hz stimulation increases DLS DA | Not reproduced |\n| DLS DA rebounds after the train | Partially reproduced |\n| DA terminals in TS and DLS respond oppositely | Reproduced |\n| Vglut2+ DA neurons are excited | Reproduced |\n| The Vglut2+ response scales with frequency | Reproduced |\n| Anxa1+ DLS terminals are inhibited | Blocked: data missing |\n| The Anxa1+ terminal inhibition scales with frequency | Partially reproduced |\n| Anxa1+ terminals rebound after the train | Partially reproduced |\n| Anxa1+ cell bodies are inhibited | Partially reproduced |\n| Vglut2+ excited and Anxa1+ inhibited | Reproduced |\n| Human tissue counts (Figure 1, S1; four claims) | Blocked: data missing |\n\nA failure to reproduce here may be a failure of this attempt, not of the paper: see the\nreasoning and the differences from the paper's method.\n\nThe analysis uses the lab's dF/F stored in the files. Many of the paper's statistics come out to\nthe first decimal. The dandiset holds Anxa1 DLS recordings for 9 of the 18 mice the paper\nanalyses; for the other nine mice it holds SNc recordings only. The attempt record, with the\nreasons and the differences from the paper's method, is\n[`attempts/001528-hadjas-2025-01.yaml`](../../attempts/001528-hadjas-2025-01.yaml).\n\n- `reproduce_hadjas_2025.ipynb`: the analysis. It takes about five minutes, most of it streaming\n  the files and recomputing the dF/F for the data check.\n- `photometry.py`: loading the files, trial alignment, response measures, a recomputation of the\n  dF/F, and the statistical tests. Other notebooks on this dandiset can import it.\n"
}
```

```
File created successfully at: entries/001528-hadjas-2025/README.md (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
python tools/entry.py lock entries/001528-hadjas-2025 2>&1 | tail -2 && time python tools/entry.py all entries/001528-hadjas-2025 2>&1 | tail -30
```

```
wrote entries/001528-hadjas-2025/requirements.lock.txt
Installed kernelspec registry-001528-hadjas-2025 in executed/001528-hadjas-2025/.venv/share/jupyter/kernels/registry-001528-hadjas-2025
0 error(s)
pass  reproduce_hadjas_2025.ipynb  (290 s)

real	5m1.110s
user	8m52.571s
sys	0m8.531s
```

**Agent**

Check passed with 0 errors and the notebook ran in 290 s. Comparing the executed outputs with my dev run to confirm the conclusions still match.

**Agent calls Bash**

```bash
cd $TMPDIR && python - <<'EOF'
import json
def outs(p):
    nb = json.load(open(p)); res = {}
    for c in nb['cells']:
        if c['cell_type'] != 'code': continue
        t = c['metadata'].get('tags', ['untagged'])
        txt = ''.join(''.join(o.get('text', '')) for o in c.get('outputs', []))
        res.setdefault(str(t), []).append(txt)
    return res
a = outs('run1.ipynb'); b = outs('executed/001528-hadjas-2025/reproduce_hadjas_2025.ipynb')
import difflib
for k in b:
    for x, y in zip(a.get(k, []), b[k]):
        if x != y:
            d = [l for l in difflib.unified_diff(x.splitlines(), y.splitlines(), lineterm='', n=0) if not l.startswith(('---','+++','@@'))]
            print(k, '\n'.join(d[:30]))
EOF
```

```
['untagged'] -loaded 258 NWB files in 74 s
+loaded 258 NWB files in 73 s
['untagged'] -Notebook ran in 4.6 min
+Notebook ran in 4.7 min
['sanity'] +Frequencies-protocol files without 4 s trains: ['sub-B7514', 'sub-B7515', 'sub-B7532', 'sub-B7616', 'sub-B8364', 'sub-B8369', 'sub-B8370', 'sub-B8427', 'sub-B8429', 'sub-B8569', 'sub-B8603', 'sub-B8612', 'sub-B8677', 'sub-C4608']
+Median interval between consecutive trains (s), onset to onset and offset to next onset:
+             onset_to_onset  offset_to_onset
+protocol                                    
+durations             11.05            10.05
+frequencies           21.00            20.00
['sanity'] -recomputed dF/F for 258 files in 193 s
+recomputed dF/F for 258 files in 197 s
Shell cwd was reset to
```

**Agent**

Outputs are identical apart from timings and the two new data-check prints. Running the handover.

**Agent calls Bash**

```bash
python tools/entry.py handover entries/001528-hadjas-2025 2>&1 | tail -5; ls executed/001528-hadjas-2025/handover; git status --short; cat .gitignore | head -20
```

```
wrote executed/001528-hadjas-2025/handover
10.1101-2025.06.03.657460.yaml
photometry.py
reproduce_hadjas_2025.ipynb
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
?? attempts/001528-hadjas-2025-01.yaml
?? claims/001528/
?? entries/001528-hadjas-2025/
?? scripts
__pycache__/
*.pyc
[... 6 more lines not kept]
```

**Agent calls Bash**

```bash
python -c "
import json;nb=json.load(open('executed/001528-hadjas-2025/handover/reproduce_hadjas_2025.ipynb'))
print(len(nb['cells']), sum('**Result' in ''.join(c['source']) for c in nb['cells']), any('## Summary' in ''.join(c['source']) for c in nb['cells']))"; ls entries/001528-hadjas-2025
```

```
63 0 False
README.md
__pycache__
entry.yaml
photometry.py
reproduce_hadjas_2025.ipynb
requirements.in
requirements.lock.txt
```

**Agent**

I did steps 1 to 5 of the protocol and ran the handover (step 6). The entry checks with 0 errors and the notebook runs from a clean environment in 290 s. Nothing is committed. I used the preprint's full text (bioRxiv v1, CC BY), saved under `paper/`.

**1. Outcome per claim** (25 claims; counts taken from the attempt record)

| Claim | Outcome |
|---|---|
| cohort-sizes | not reproduced (10 of 16 group counts match) |
| fig2-gaba-excited | reproduced (t = 3.86 and 9.19; paper 3.8 and 9.2) |
| fig2-gaba-frequency | reproduced (Friedman 21.00 and 18.15) |
| fig3b-da-stn-250ms-peak | partially reproduced (0.786 s in the window I fixed beforehand; a narrower window gives the paper's 0.492 ± 0.033 s) |
| fig3c-da-stn-duration | reproduced (12.93, p = 0.0048; paper 13.0, p = 0.005) |
| fig3d-da-stn-frequency-ns | reproduced (4.20, p = 0.24, as in the paper) |
| fig3g-da-ppn-duration | not reproduced (p ≥ 0.25 under every reading) |
| fig3h-da-ppn-frequency-ns | reproduced (F = 1.35, p = 0.29) |
| fig4cf-ts-dls-opposite | reproduced (F = 40.9 and 36.4, the paper's values) |
| fig4dg-ts-frequency | reproduced (6 of 6 tests) |
| fig4eh-dls-frequency | reproduced (6 of 6 tests) |
| fig4eh-dls-5hz-increase | not reproduced |
| fig4cf-dls-rebound | partially reproduced |
| figs3-terminals-opposite | reproduced |
| fig5-vglut2-excited | reproduced |
| fig5-vglut2-frequency | reproduced |
| fig5-anxa1-dls-inhibited | blocked, data missing |
| fig5-anxa1-dls-frequency | partially reproduced |
| fig5-anxa1-dls-rebound | partially reproduced |
| figs4-anxa1-soma-inhibited | partially reproduced |
| fig5-opposite-subtypes | reproduced |
| 4 human tissue claims (Fig 1, S1) | blocked, data missing |

Totals: 12 reproduced, 6 partially reproduced, 3 not reproduced, 4 blocked. All claims are `data: dandiset`; no outside inputs were used.

**2. What was found about the dandiset**
- **No published version.** Only the draft exists; I pinned the draft as modified 2026-09-01T15:27:47Z (290 assets).
- **Contents.** 258 NWB files from 120 mice. Each file holds the lab's dF/F, the 465 and 405 nm signals and the stimulation epochs. Recomputing the dF/F from the stored signals agrees (median r 0.9999 in duration sessions, 0.9988 in frequency sessions). No recording is deposited twice. The stimulus responses lock to the true onsets in 235 of 258 recordings, so the epoch tables share the dF/F clock.
- **Anxa1 DLS recordings appear to be missing for 9 of the 18 mice.** The dandiset has DLS recordings for 5 (STN) and 4 (PPN) mice where the paper has 8 and 10, and SNc recordings for 8 and 10 where the paper has 5 and 4.
  - The paper's cell-body t-values are matched exactly by the SNc recordings of the 9 mice that have both a DLS and an SNc file.
  - The 9 extra recordings, which have no site in their file names, look like SNc signals. Adding them to DLS does not reproduce the paper's terminal statistics.
- **Smaller gaps.**
  - DA terminals in DLS have 8 mice (paper 9) and Vglut2 with STN stimulation has 9 (paper 10).
  - C4608 has no 4 s frequency block.
  - The human tissue counts and histology are not in the dandiset.
- **Metadata errors.**
  - The dF/F is labelled "a.u." but is in percent.
  - Every session start time has a -00:01 offset, so the true time zone is lost.
  - The files' description of the frequency sessions gives a 10 s interval between trains; the data and the Methods give 20 s.
  - The modulation frequencies are described inconsistently within each file.
  - Eight subject ids are lower case.
- **Differences from the Methods.** 13 mice have 10 trials per condition (Methods: 5), and 30 mice have 16 s trains the paper does not mention.
- **Code and paper.**
  - The conversion code labels one block as 10 mW where the files say 5 mW.
  - The conversion repo's Python dF/F code drops the intercept that its own description of the lab's MATLAB scripts includes. Those MATLAB scripts are not public.
  - The paper has a likely copied statistic (F1,11 = 12.8 given twice with different p-values) and two Friedman values that do not fit their p-values.

**3. Where the protocol was unclear, wrong or missing something**
1. **No published version exists.** The protocol only allows drafts for repeat attempts. I pinned `draft`, recorded its modification time, and the notebook checks whether the draft has changed since.
2. **Expected values with a 10% tolerance don't suit test statistics** (t, W, F), which depend on analysis windows the paper does not state. Outcomes rest on direction and significance; the paper's statistics are printed next to mine. Recorded in the claims file's opening comment.
3. **The 10% tolerance doesn't fit counts of animals.** I used 0 and gave the reason.
4. **A selection-dependent block where data are missing.** At the dandiset's n of 5 and 4, the paper's Wilcoxon tests cannot reach p < 0.05. The protocol's "too few units" category is `other`, but the cause is missing recordings, so I used `data_missing`.
5. **Labels against counts.** The paper's counts suggest the Anxa1 site labels are wrong, but the signals suggest they are right. The protocol says to trust the data. I kept the dandiset's labels for outcomes and showed the other reading as a variant.
6. **The data check ran into claim territory.** To examine the label question I looked at Anxa1 response medians before writing criteria. I disclosed this in the claims file.
7. **The clock check has no recipe for evoked photometry.** I compared responses at true onsets with onsets shifted by ±3 s, and named the 23 recordings where this could not be shown.
8. **The source hierarchy didn't fit.** The lab's analysis code is not public; the dandiset links only the conversion repo, which describes the lab's MATLAB scripts and re-implements them in Python. I treated it as "other software" and used its description only to fill gaps the Methods leave. Where it disagrees with the Methods, I followed the Methods.
9. **Test choice.** The paper picked parametric or non-parametric tests after a Shapiro-Wilk test. I used the test the paper reports for each comparison.
10. **Independence of the work.** CatalystNeuro curated this dandiset and wrote the conversion code, and is also the accountable party for this attempt. The protocol does not address this.

**4. Runtime and failures**
- The notebook takes about 5 minutes: 73 s streaming, about 195 s recomputing the dF/F for the data check.
- Loading first took about 10 minutes because h5py serializes threads. I switched to a process pool.
- Two bugs found while preparing, both fixed before the final run:
  - Some files store timestamps instead of a sampling rate, which crashed the first load.
  - Shifted onsets for the clock check could fall outside the recording.
- The final lock, check, run and handover all passed with no errors.

## End of run

66 turns, 53 minutes, result: success.
