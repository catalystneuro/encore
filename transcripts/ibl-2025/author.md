# 000409 · author · run 39037243249

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

[... 473 more lines not kept]
```

**Agent calls Bash**

```bash
cat README.md docs/design.md; ls -la entries/001453-fouke-2025 claims/001453; cat attempts/001453-fouke-2025-01.yaml
```

```
<persisted-output>
Output too large (58.4KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/f751195b-d081-4c68-9fab-3efdc151580b/tool-results/b90iletlw.txt

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
 "file_path": "/home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/f751195b-d081-4c68-9fab-3efdc151580b/tool-results/b90iletlw.txt"
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
[... 1011 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/001453-fouke-2025; cat entry.yaml requirements.in README.md; head -c 3000 omr.py; cat ../../claims/001453/*.yaml | head -120
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
[... 218 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python - <<'E'
import json
nb=json.load(open('entries/001453-fouke-2025/reproduce_fouke_2025.ipynb'))
for i,c in enumerate(nb['cells'][:8]):
    print(i,c['cell_type'],c.get('metadata'),''.join(c['source'])[:1500]); print('-----')
print(len(nb['cells']))
for c in nb['cells']: print(c['cell_type'],c['metadata'].get('tags'), ''.join(c['source'])[:80].replace('\n',' '))
E
wc -l tools/entry.py; ls schemas
```

```
0 markdown {} # Reproducing Fouke et al. (2025) from dandiset 001453

**Paper.** Fouke KE, He Z, Loring MD, Naumann EA (2025). Neural circuits underlying divergent
visuomotor strategies of zebrafish and *Danionella cerebrum*. *Current Biology*.
[doi:10.1016/j.cub.2025.04.027](https://doi.org/10.1016/j.cub.2025.04.027). This attempt used the
full text of the accepted author manuscript in PubMed Central (PMC12218792); the version of record
is not open access.

**Dandiset.** [DANDI:001453](https://dandiarchive.org/dandiset/001453/0.250518.1950), version
0.250518.1950. The paper cites no DANDI version (its data statement points to a GitLab repository
that holds code only). This is the only published version. The draft holds the same 37 files
(same blobs and sizes); it differs only in metadata added later (authors, keywords, and a
`relatedResource` link to the paper), none of which the analysis uses.

**What the dandiset holds.** Freely swimming tracking of 25 zebrafish (ZF) and 12 *D. cerebrum*
(DC) larvae during the optomotor protocol of Figure 1 and Figure S1. The two-photon imaging and the
head-fixed tail tracking of Figures 2 to 4 are not in it.

**Outside inputs.** The stimulus codes in the files have no names. The names come from the paper's
analysis notebook `Fig1-S1.ipynb` (GitLab `ean26/danionella_omr_neuralcircuits2025`, commit
[... 182 more lines not kept]
```

**Agent calls Bash**

```bash
cat tools/entry.py; cat schemas/attempt.schema.json | head -c 6000
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
[... 586 more lines not kept]
```

**Agent calls Bash**

```bash
python -c "
import json;s=json.load(open('schemas/claims.schema.json'));print(json.dumps(s['properties']['claims']['items'],indent=0)[:3000])"; python -c "import dandi,pynwb,h5py,remfile;print('ok')"; which uv; python --version
```

```
{
"type": "object",
"additionalProperties": false,
"required": [
"id",
"statement",
"source"
],
"properties": {
"id": {
"description": "Stable within the file, e.g. fig2b.",
"type": "string",
"pattern": "^[a-z0-9]+(-[a-z0-9]+)*$"
},
"statement": {
"description": "The finding in one or two sentences, in words. Not a copy of the figure.",
"type": "string",
"minLength": 1
},
"source": {
[... 72 more lines not kept]
```

**Agent**

Setting up a scratch environment for exploration.

**Agent calls Bash**

```bash
cd $TMPDIR && uv venv -q --python 3.13 explore && uv pip install -q --python explore/bin/python dandi pynwb h5py remfile numpy pandas scipy scikit-learn requests 2>&1 | tail -3; explore/bin/python -c "import dandi,pynwb;print(dandi.__version__,pynwb.__version__)"
```

```
0.81.0 4.2.0
Shell cwd was reset to
```

**Agent calls Bash**

```bash
P=$TMPDIR/explore/bin/python; $P - <<'E'
import requests, json
r=requests.get('https://api.dandiarchive.org/api/dandisets/000409/').json()
print(json.dumps(r,indent=1)[:2000])
v=requests.get('https://api.dandiarchive.org/api/dandisets/000409/versions/?page_size=100').json()
for x in v['results']: print(x['version'],x['status'],x['asset_count'],x['size'],x['created'])
E
```

```
{
 "identifier": "000409",
 "created": "2023-01-31T21:47:46.772688Z",
 "modified": "2024-09-29T17:25:36.464925Z",
 "contact_person": "International Brain Laboratory",
 "embargo_status": "OPEN",
 "star_count": 4,
 "is_starred": false,
 "most_recent_published_version": {
  "version": "0.260309.1324",
  "name": "IBL - Brain Wide Map",
  "asset_count": 2048,
  "active_uploads": 0,
  "size": 49700602778159,
  "status": "Valid",
  "created": "2026-03-09T13:24:10.749550Z",
  "modified": "2026-03-09T13:25:26.641016Z",
  "release_notes": ""
 },
 "draft_version": {
[... 13 more lines not kept]
```

**Agent calls Bash**

```bash
P=$TMPDIR/explore/bin/python; mkdir -p paper; $P - <<'E'
import requests, json
m=requests.get('https://api.dandiarchive.org/api/dandisets/000409/versions/0.260309.1324/').json()
for k in ['name','description','citation','relatedResource','assetsSummary','wasGeneratedBy','license','keywords','studyTarget','protocol','ethicsApproval']:
    print(k, json.dumps(m.get(k),indent=0)[:2500])
E
```

```
name "IBL - Brain Wide Map"
description "The International Brain lab (IBL) aims to understand the neural basis of decision-making in the mouse by gathering a whole-brain activity map composed of electrophysiological recordings pooled from multiple laboratories. We have systematically recorded from nearly all major brain areas with Neuropixels probes, using a grid system for unbiased sampling and replicating each recording site in at least two laboratories. These data have been used to construct a brain-wide map of activity at single-spike cellular resolution during a decision-making task. In addition to the map, this data set contains other information gathered during the task: sensory stimuli presented to the mouse; mouse decisions and response times; and mouse pose information from video recordings and DeepLabCut analysis."
citation "International Brain Laboratory; Benson, Brandon; Benson, Julius; Birman, Daniel; Bonacchi, Niccol\u00f2; Carandini, Matteo; Catarino, Joana; Chapuis, Gaelle; Dayan, Peter; DeWitt, Eric; Engel, Tatiana; Fabbri, Michele; Faulkner, Mayo; Fiete, Ila; Findling, Charles; Freitas-Silva, Laura; Ger\u00e7ek, Berk; Harris, Kenneth; Hofer, Sonja; Hu, Fei; Hubert, F\u00e9lix; Huntenburg, Julia; Khanal, Anup; Langdon, Christopher; Lau, Petrina; Meijer, Guido; Miska, Nathaniel; Noel, Jean-Paul; Nylund, Kai; Pan-Vazquez, Alejandro; Pouget, Alexandre; Rossant, Cyrille; Roth, Noam; Schaeffer, Rylan; Schartner, Michael; Shi, Yanliang; Socha, Karolina; Steinmetz, Nicholas; Svoboda, Karel; Urai, Anne; Wells, Miles; West, Steven; Whiteway, Mathew; Winter, Olivier; Witten, Ilana (2026) IBL - Brain Wide Map (Version 0.260309.1324) [Data set]. DANDI Archive. https://doi.org/10.48324/dandi.000409/0.260309.1324"
relatedResource [
{
"url": "https://www.biorxiv.org/content/10.1101/2023.07.04.547681v2",
"name": "A Brain-Wide Map of Neural Activity during Complex Behaviour",
"relation": "dcite:IsDescribedBy",
"schemaKey": "Resource",
"identifier": "https://doi.org
[... 101 more lines not kept]
```

**Agent**

Now the paper. Trying the Nature full text.

**Agent calls Bash**

```bash
P=$TMPDIR/explore/bin/python; $P - <<'E'
import requests
r=requests.get('https://api.crossref.org/works/10.1038/s41586-025-09235-0').json()['message']
print(r['title'], r.get('license'), r.get('published'))
h={'User-Agent':'Mozilla/5.0'}
x=requests.get('https://www.nature.com/articles/s41586-025-09235-0',headers=h)
print(x.status_code,len(x.text))
open('paper/nature.html','w').write(x.text)
E
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
P=$TMPDIR/explore/bin/python; $P - <<'E'
import re,html
t=open('paper/nature.html').read()
# strip
t=re.sub(r'<script.*?</script>|<style.*?</style>','',t,flags=re.S)
t=re.sub(r'<(h[1-4])[^>]*>',r'\n\n## ',t)
t=re.sub(r'<p[^>]*>','\n\n',t)
t=re.sub(r'<[^>]+>','',t)
t=html.unescape(t)
t=re.sub(r'\n\s*\n+','\n\n',t)
open('paper/nature.txt','w').write(t)
print(len(t))
E
grep -n "^## " paper/nature.txt | head -80
```

Result: not kept, because it reads the paper's text.

**Agent**

Full text is open access (CC-BY 4.0). Reading the main text and Methods.

**Agent calls Read**

```json
{
 "file_path": "paper/nature.txt",
 "offset": 80,
 "limit": 200
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/nature.txt",
 "offset": 280,
 "limit": 240
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
P=$TMPDIR/explore/bin/python; $P - <<'E'
import requests, json, collections
url='https://api.dandiarchive.org/api/dandisets/000409/versions/0.260309.1324/assets/?page_size=1000'
assets=[]
while url:
    r=requests.get(url).json(); assets+=r['results']; url=r['next']
print(len(assets))
json.dump(assets,open('/tmp/claude/a409.json','w') if False else open(__import__('os').environ['TMPDIR']+'/a409.json','w'))
c=collections.Counter()
for a in assets:
    p=a['path']; parts=p.split('_'); suf=p.split('/')[-1].split('_',2)[-1]
    import re
    m=re.search(r'_desc-([a-z]+)',p); c[(m.group(1) if m else 'none', p.rsplit('_',1)[-1])]+=1
print(c)
for a in assets[:12]: print(a['path'],a['size'])
subs=set(a['path'].split('/')[0] for a in assets); print(len(subs))
E
```

```
2048
Counter({('raw', 'ecephys.nwb'): 459, ('processed', 'behavior+ecephys.nwb'): 459, ('none', 'VideoLeftCamera.mp4'): 437, ('none', 'VideoRightCamera.mp4'): 433, ('none', 'VideoBodyCamera.mp4'): 260})
sub-NYU-12/sub-NYU-12_ses-b182b754-3c3e-4942-8144-6ee790926b58_ecephys+image/sub-NYU-12_ses-b182b754-3c3e-4942-8144-6ee790926b58_VideoRightCamera.mp4 1668745947
sub-NYU-11/sub-NYU-11_ses-6713a4a7-faed-4df2-acab-ee4e63326f8d_ecephys+image/sub-NYU-11_ses-6713a4a7-faed-4df2-acab-ee4e63326f8d_VideoRightCamera.mp4 2842691249
sub-NYU-11/sub-NYU-11_ses-6713a4a7-faed-4df2-acab-ee4e63326f8d_ecephys+image/sub-NYU-11_ses-6713a4a7-faed-4df2-acab-ee4e63326f8d_VideoLeftCamera.mp4 7913950497
sub-NYU-12/sub-NYU-12_ses-4364a246-f8d7-4ce7-ba23-a098104b96e4_ecephys+image/sub-NYU-12_ses-4364a246-f8d7-4ce7-ba23-a098104b96e4_VideoRightCamera.mp4 1729332149
sub-NYU-12/sub-NYU-12_ses-4364a246-f8d7-4ce7-ba23-a098104b96e4_ecephys+image/sub-NYU-12_ses-4364a246-f8d7-4ce7-ba23-a098104b96e4_VideoLeftCamera.mp4 3316125891
sub-NYU-11/sub-NYU-11_ses-56956777-dca5-468c-87cb-78150432cc57_ecephys+image/sub-NYU-11_ses-56956777-dca5-468c-87cb-78150432cc57_VideoRightCamera.mp4 2183780971
sub-NYU-11/sub-NYU-11_ses-56956777-dca5-468c-87cb-78150432cc57_ecephys+image/sub-NYU-11_ses-56956777-dca5-468c-87cb-78150432cc57_VideoLeftCamera.mp4 5686153372
sub-NYU-39/sub-NYU-39_ses-6ed57216-498d-48a6-b48b-a243a34710ea_ecephys+image/sub-NYU-39_ses-6ed57216-498d-48a6-b48b-a243a34710ea_VideoBodyCamera.mp4 700604839
sub-NYU-39/sub-NYU-39_ses-6ed57216-498d-48a6-b48b-a243a34710ea_ecephys+image/sub-NYU-39_ses-6ed57216-498d-48a6-b48b-a243a34710ea_VideoRightCamera.mp4 4382309228
sub-NYU-39/sub-NYU-39_ses-6ed57216-498d-48a6-b48b-a243a34710ea_ecephys+image/sub-NYU-39_ses-6ed57216-498d-48a6-b48b-a243a34710ea_VideoLeftCamera.mp4 4458632233
sub-NYU-39/sub-NYU-39_ses-35ed605c-1a1a-47b1-86ff-2b56144f55af_ecephys+image/sub-NYU-39_ses-35ed605c-1a1a-47b1-86ff-2b56144f55af_VideoBodyCamera.mp4 685970367
sub-NYU-39/sub-NYU-39_ses-35ed605c
[... 1 more lines not kept]
```

**Agent calls Bash**

```bash
P=$TMPDIR/explore/bin/python; $P - <<'E'
import json,os,numpy as np
a=json.load(open(os.environ['TMPDIR']+'/a409.json'))
pr=[x for x in a if 'desc-processed' in x['path']]
s=np.array([x['size'] for x in pr])/1e9
print(len(pr), s.min(), np.median(s), s.max(), s.sum())
print(pr[0]['path'], pr[0]['asset_id'])
E
```

```
459 0.20890992 0.990334344 2.964499206 485.20328862599996
sub-NYU-11/sub-NYU-11_ses-6713a4a7-faed-4df2-acab-ee4e63326f8d_desc-processed_behavior+ecephys.nwb 388c82a6-94fe-4055-af61-4dfc05035633
```

**Agent calls Bash**

```bash
P=$TMPDIR/explore/bin/python; cd $TMPDIR; time $P - <<'E'
import json,os,h5py,remfile,time
from dandi.dandiapi import DandiAPIClient
a=json.load(open(os.environ['TMPDIR']+'/a409.json'))
pr=[x for x in a if 'desc-processed' in x['path']]
c=DandiAPIClient(); ds=c.get_dandiset('000409','0.260309.1324')
asset=ds.get_asset_by_path(pr[0]['path'])
url=asset.get_content_url(follow_redirects=1, strip_query=True)
print(url)
t=time.time()
f=h5py.File(remfile.File(url),'r')
def walk(g,pre=''):
    for k,v in g.items():
        if isinstance(v,h5py.Dataset):
            print(pre+k, v.shape, v.dtype, dict((kk,str(vv)[:80]) for kk,vv in v.attrs.items() if kk in('unit','description','neurodata_type','conversion','rate','resolution')))
        else:
            print(pre+k+'/', v.attrs.get('neurodata_type',''), str(v.attrs.get('description',''))[:150])
            walk(v,pre+k+'/')
walk(f)
print(time.time()-t)
E
```

```
https://dandiarchive.s3.amazonaws.com/blobs/275/e0a/275e0aae-5c90-4637-afff-3944f319762c
acquisition/  
analysis/  
file_create_date (1,) object {}
general/  
general/devices/  
general/devices/Probe00/ Device A PRB_1_4_0480_1 probe. Additional metadata: {"model_name": "PRB_1_4_0480_1", "manufacturer": "imec", "port": "2", "slot": "2", "part_number": "PRB_1_
general/extracellular_ephys/  
general/extracellular_ephys/Probe00/ ElectrodeGroup Electrode group for probe00
general/extracellular_ephys/Probe00/device/ Device A PRB_1_4_0480_1 probe. Additional metadata: {"model_name": "PRB_1_4_0480_1", "manufacturer": "imec", "port": "2", "slot": "2", "part_number": "PRB_1_
general/extracellular_ephys/electrodes/ ElectrodesTable metadata about extracellular electrodes
general/extracellular_ephys/electrodes/adc_group (384,) int64 {'description': 'ADC group index from SpikeGLX metadata.', 'neurodata_type': 'VectorData'}
general/extracellular_ephys/electrodes/adc_sample_order (384,) int64 {'description': 'ADC sample order from SpikeGLX metadata.', 'neurodata_type': 'VectorData'}
general/extracellular_ephys/electrodes/channel_name (384,) object {'description': 'The name of this channel, showing all recording streams for the electrode (e.g.,', 'neurodata_type': 'VectorData'}
general/extracellular_ephys/electrodes/contact_ids (384,) object {'description': 'Channel IDs as specified by the probe manufacturer.', 'neurodata_type': 'VectorData'}
general/extracellular_ephys/electrodes/contact_shapes (384,) object {'description': 'Contact shape per electrode as defined by the probe.', 'neurodata_type': 'VectorData'}
general/extracellular_ephys/electrodes/electrode_name (384,) object {'description': 'Unique identifier derived from probe contact ids.', 'neurodata_type': 'VectorData'}
general/extracellular_ephys/electrodes/filtering (384,) object {'description': 'Description of hardware filtering.', 'neurodata_type': 'VectorData'}
general/extracellular_ephys/electrodes/group (384,) object {
[... 223 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && git clone -q https://github.com/int-brain-lab/paper-brain-wide-map.git && cd paper-brain-wide-map && git log -1 --format='%H %cd' && ls -R | head -150 && du -sh .
```

```
118fc36cb3602934466ad2c6087c2b3b441f9f1f Tue Jun 2 15:40:12 2026 +0100
.:
LICENSE
MANIFEST.in
README.md
brainwidemap
data_loading_examples.py
pyproject.toml
requirements.txt
requirements_frozen.txt
scripts
setup.py

./brainwidemap:
__init__.py
bwm_loading.py
decoding
encoding
fixtures
manifold
[... 133 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/paper-brain-wide-map; cat README.md | head -80; head -5 brainwidemap/fixtures/*.csv; wc -l brainwidemap/fixtures/*.csv; cat brainwidemap/meta/inclusion_info.csv; head -5 brainwidemap/meta/region_info.csv; wc -l brainwidemap/meta/region_info.csv
```

```
# paper-brain-wide-map
Code related to the brainwide map paper: 

International Brain Laboratory., Angelaki, D., Benson, B. et al. A brain-wide map of neural activity during complex behaviour. Nature 645, 177–191 (2025). https://doi.org/10.1038/s41586-025-09235-0

Find editable figures and latex text here: https://github.com/int-brain-lab/Brainwide-Map-Paper


And companion paper:

Findling, C., Hubert, F., International Brain Laboratory. et al. Brain-wide representations of prior information in mouse decision-making. Nature 645, 192–200 (2025). https://doi.org/10.1038/s41586-025-09226-1

# Contents

- [Installation](#installation)
- [Demo](#minimal-working-example-query-information-about-bwm-data)

# Installation
The installation instructions go through the step of setting up a conda environment, installing dependencies, and linking this repository source code to the environment.
This usually takes a few minutes on a fast internet connection and a consumer laptop.
[... 108 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/paper-brain-wide-map/brainwidemap; sed -n 1,400p bwm_loading.py
```

```
from dateutil import parser
import json
import logging
import numpy as np
import pandas as pd
from pathlib import Path

from brainbox.behavior import training
from brainbox.io.one import SpikeSortingLoader, SessionLoader
from iblatlas.atlas import BrainRegions
from iblutil.numerical import ismember, hash_uuids
from iblutil.io import hashfile
from one.alf import spec
from one.remote import aws

import brainwidemap

_logger = logging.getLogger(__name__)

MODIFIED_BEFORE = '2024-07-10'
[... 381 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/paper-brain-wide-map/brainwidemap; sed -n 400,700p bwm_loading.py; cat meta/mice_info.py meta/probe_type_info.py
```

```
'2024_Q2_IBL_et_al_BWM':
            {'trials':
                 '067fb0e3d242ebeface361c42bdcf8c8',
             'clusters':
                 'b89fac76289f3a3d585910711f1eef41',
             },
        '2026_Q2_IBL_et_al_BWM':
            {'clusters':
                 'ac22196fbd77687d6ee3a0c6b1b1fc15',
             'clusters.waveforms_peak':
                 'db71666e84ae28b6a9051e3fa866d1c9',
             'clusters.acgs_log':
                 '7f1cc617d97b234b307ca9ff16cbf09f',
             'acgs_log.times':
                 'c331a024cedb4ffa30304dc40af5a703',
             },
    }
    if target_path is None:
        target_path = Path(one.cache_dir).joinpath('bwm_tables')
        target_path.mkdir(exist_ok=True, parents=True)
[... 363 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/paper-brain-wide-map; grep -rn "ttest\|0.08\b\|perf_easy\|psychometric\|reversal\|first_movement\|< 0.08\|reaction" --include=*.py brainwidemap/meta | head -40; grep -n "^def " brainwidemap/meta/bwm_figs.py | head -80; wc -l brainwidemap/meta/*.py
```

```
brainwidemap/meta/inclusion_info.py:10:rt_range = (0.08, 0.2)
brainwidemap/meta/inclusion_info.py:40:# Filter trials on "bwm_include" meaning reaction time in range, no NaN in the following trial events
brainwidemap/meta/intro_figure_example_time_series.py:310:    y0_text = y0_top + 0.08 * (y0_rng if y0_rng > 0 else 1.0)
brainwidemap/meta/intro_figure_example_time_series.py:359:    fig.subplots_adjust(left=0.14, right=0.98, bottom=0.08, top=0.96, hspace=0.08)
brainwidemap/meta/meta_bwm.py:6:combine_pvalues, fisher_exact, barnard_exact, boschloo_exact, ttest_ind)
brainwidemap/meta/meta_bwm.py:611:    t, p = ttest_ind(a,b)
brainwidemap/meta/bwm_figs.py:1028:        fig.subplots_adjust(top=0.96, bottom=0.08, left=0.02, right=0.98)
brainwidemap/meta/bwm_figs.py:3758:               'j': fg.place_axes_on_grid(fig, xspan=[xspans3[2][0] - 0.08, xspans3[2][1]], yspan=yspans[2]),
brainwidemap/meta/bwm_figs.py:3923:        x = -0.08
156:def imgs_variable_path(variable):
222:def set_max_ticks(ax, num_ticks=4):
232:def adjust_subplots(fig, adjust=5, extra=2):
242:def plot_vertical_swanson(acronyms, scores, mask=None, ax=None, cmap='viridis', vmin=None, vmax=None, fontsize=7,
268:def plot_horizontal_swanson(acronyms, scores, mask=None, ax=None, cmap='viridis', vmin=None, vmax=None, fontsize=7,
297:def add_sig_legends(ax, mask_label='Not significant'):
315:def add_cbar(cmap, vmin, vmax, ax, label, cbar_kwargs=dict(), associated=True):
336:def get_cmap_for_variable(variable):
364:def adjust_vertical_swansons(positions, ax):
390:def adjust_horizontal_swansons(positions, ax):
422:def beryl_to_cosmos(beryl_acronym, br):
[... 77 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/paper-brain-wide-map/brainwidemap; cat meta/inclusion_info.py; sed -n 2566,2604p meta/bwm_figs.py; cat decoding/settings_for_BWM_figure/settings_stimside.py | grep -v "^#" | grep -v "^$" | head -80
```

```
# https://github.com/int-brain-lab/paper-brain-wide-map/blob/cecac2295f2dd61fad5f5b51326702b566591baa/brainwidemap/meta/inclusion_info.py#L18
import pandas as pd
from pathlib import Path
from one.api import ONE
from iblatlas.regions import BrainRegions
from brainwidemap.bwm_loading import download_aggregate_tables, bwm_query, bwm_units, filter_sessions
import brainwidemap

regions = BrainRegions()
rt_range = (0.08, 0.2)
min_errors = 3
min_qc = 1.
min_units_sessions = (5, 2)

one = ONE(base_url='https://openalyx.internationalbrainlab.org')
one = ONE(base_url='https://alyx.internationalbrainlab.org')

file_trials_table = download_aggregate_tables(one, type='trials')
trials_df = pd.read_parquet(file_trials_table)
clus_df = pd.read_parquet(download_aggregate_tables(one, type='clusters'))
[... 229 more lines not kept]
```

**Agent calls Bash**

```bash
P=$TMPDIR/explore/bin/python; cd $TMPDIR; $P - <<'E'
import json,os,h5py,remfile,time
from dandi.dandiapi import DandiAPIClient
a=json.load(open(os.environ['TMPDIR']+'/a409.json'))
pr=[x for x in a if 'desc-processed' in x['path']]
big=max(pr,key=lambda x:x['size'])
url=f"https://api.dandiarchive.org/api/assets/{big['asset_id']}/download/"
import requests
url=requests.head(url,allow_redirects=True).url.split('?')[0]
t=time.time()
f=h5py.File(remfile.File(url),'r')
print(big['path'], big['size']/1e9)
for k in ['session_description','identifier','session_start_time','general/lab','general/institution','general/protocol','general/session_id','general/subject/date_of_birth','general/subject/sex','general/subject/weight','general/subject/subject_id','general/subject/species','general/ibl_metadata/revision','timestamps_reference_time']:
    print(k, f[k][()])
print(list(f['processing'].keys()))
for m in f['processing']:
    for k in f['processing'][m]: 
        g=f['processing'][m][k]
        print(m,k,g.attrs.get('neurodata_type'), str(g.attrs.get('description',''))[:300])
        if isinstance(g,h5py.Group):
            for kk in g: print('    ',kk, getattr(g[kk],'shape',''), str(g[kk].attrs.get('description',''))[:120] if hasattr(g[kk],'attrs') else '')
print('acq',list(f['acquisition'].keys()), 'analysis', list(f['analysis'].keys()))
d=f['intervals/trials']
for k in d: print(k, d[k].attrs.get('description'))
u=f['units']
print(u.attrs['description'])
for k in ['ibl_quality_score','kilosort2_label','sliding_rp_violation','noise_cutoff','median_spike_amplitude_uV','firing_rate']:
    print(k,u[k].attrs['description'])
print(f['units/spike_times'].chunks, f['units/spike_times'].compression)
print(time.time()-t)
E
```

```
sub-NYU-65/sub-NYU-65_ses-8c025071-c4f3-426c-9aed-f149e8f75b7b_desc-processed_behavior+ecephys.nwb 2.964499206
session_description b''
identifier b'cc5bf455-0207-406f-83db-3f1412bdaff9'
session_start_time b'2022-09-15T12:27:05.370169-04:00'
general/lab b'angelakilab'
general/institution b'New York University / Center for Neural Science'
general/protocol b'_iblrig_tasks_ephysChoiceWorld6.6.4'
general/session_id b'8c025071-c4f3-426c-9aed-f149e8f75b7b'
general/subject/date_of_birth b'2022-05-03T00:00:00-04:00'
general/subject/sex b'M'
general/subject/weight b'0.0247 kg'
general/subject/subject_id b'NYU-65'
general/subject/species b'Mus musculus'
general/ibl_metadata/revision b'2025-05-06'
timestamps_reference_time b'2022-09-15T12:27:05.370169-04:00'
['lick_times', 'motion_energy', 'passive_protocol', 'pose_estimation', 'pupil', 'wheel']
lick_times EventsLickTimes Events Lick event timestamps detected from tongue pose estimation (Lightning Pose). Detection algorithm: frame-to-frame position changes in tongue landmarks (tongue_end_l_x, tongue_end_l_y, tongue_end_r_x, tongue_end_r_y) are computed, and frames where any coordinate changes by more than std(diff)/4 are ma
     timestamps (11808,) 
motion_energy LeftCameraMotionEnergy TimeSeries Motion energy calculated for a region of the left camera video. ROI dimensions: 149 pixels wide, 99 pixels tall, top-left corner at (272, 128).

[... 119 more lines not kept]
```

**Agent calls Bash**

```bash
mkdir -p $TMPDIR/dev; cat > $TMPDIR/dev/scan.py <<'E'
import json,os,h5py,remfile,time,numpy as np,pandas as pd,requests
from concurrent.futures import ThreadPoolExecutor
a=json.load(open(os.environ['TMPDIR']+'/a409.json'))
pr=[x for x in a if 'desc-processed' in x['path']]
def s(x): 
    v=x[()]; return v.decode() if isinstance(v,bytes) else v
def one(asset):
    url=f"https://api.dandiarchive.org/api/assets/{asset['asset_id']}/download/"
    url=requests.head(url,allow_redirects=True).url.split('?')[0]
    t=time.time()
    with h5py.File(remfile.File(url),'r') as f:
        tr={k:f['intervals/trials'][k][:] for k in f['intervals/trials'] if k!='id'}
        u=f['units']
        units={k:u[k][:] for k in ['ibl_quality_score','max_electrode','spike_count','probe_name','firing_rate','median_spike_amplitude_uV','noise_cutoff','sliding_rp_violation','kilosort2_label']}
        loc=f['general/localization/ElectrodesIBLBregma']
        el={k:loc[k][:] for k in ['localized_entity','beryl_location','brain_region','atlas_id','probe_name']}
        dev={k:str(f['general/devices'][k].attrs.get('description',''))[:300] for k in f['general/devices']}
        info=dict(path=asset['path'],start=s(f['session_start_time']),dob=s(f['general/subject/date_of_birth']),sex=s(f['general/subject/sex']),weight=s(f['general/subject/weight']),subject=s(f['general/subject/subject_id']),lab=s(f['general/lab']),protocol=s(f['general/protocol']),rev=s(f['general/ibl_metadata/revision']),proc=list(f['processing'].keys()),
                  passive=[x.decode() for x in f['processing/passive_protocol/passive_intervals/protocol_name'][:]] if 'passive_protocol' in f['processing'] else None)
    return dict(info=info,trials=tr,units=units,el=el,dev=dev,sec=time.time()-t)
t=time.time()
with ThreadPoolExecutor(24) as ex: res=list(ex.map(one,pr[:48]))
print('48 files',time.time()-t, np.median([r['sec'] for r in res]))
import pickle; pickle.dump(res,open(os.environ['TMPDIR']+'/scan48.pkl','wb'))
E
cd $TMPDIR && explore/bin/python dev/scan.py
```

```
48 files 158.26332592964172 71.59875416755676
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cat > $TMPDIR/dev/prof.py <<'E'
import json,os,h5py,remfile,time,requests
a=json.load(open(os.environ['TMPDIR']+'/a409.json'))
pr=[x for x in a if 'desc-processed' in x['path']]
asset=pr[5]
url=f"https://api.dandiarchive.org/api/assets/{asset['asset_id']}/download/"
t=time.time(); url=requests.head(url,allow_redirects=True).url.split('?')[0]; print('url',time.time()-t)
t=time.time(); f=h5py.File(remfile.File(url),'r'); print('open',time.time()-t)
def tm(name,fn):
    t=time.time(); fn(); print(name, round(time.time()-t,2))
tm('trials', lambda: {k:f['intervals/trials'][k][:] for k in f['intervals/trials']})
u=f['units']
for k in ['ibl_quality_score','max_electrode','spike_count','probe_name','firing_rate','kilosort2_label']:
    tm('u.'+k, lambda: u[k][:])
loc=f['general/localization/ElectrodesIBLBregma']
for k in ['localized_entity','beryl_location','brain_region','atlas_id','probe_name']:
    tm('loc.'+k, lambda: loc[k][:])
tm('subject', lambda: [f['general/subject'][k][()] for k in f['general/subject']])
E
cd $TMPDIR && explore/bin/python dev/prof.py
```

```
url 0.5866913795471191
open 1.0859825611114502
trials 0.32
u.ibl_quality_score 0.0
u.max_electrode 0.17
u.spike_count 0.0
u.probe_name 0.18
u.firing_rate 0.0
u.kilosort2_label 0.08
loc.localized_entity 0.0
loc.beryl_location 0.0
loc.brain_region 0.16
loc.atlas_id 0.08
loc.probe_name 0.0
subject 0.0
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && sed -i 's/ThreadPoolExecutor/ProcessPoolExecutor/g; s/ex.map(one,pr\[:48\])/ex.map(one,pr[:48])/; s/ProcessPoolExecutor(24)/ProcessPoolExecutor(16)/' dev/scan.py && sed -i 's/^t=time.time()$/if __name__=="__main__":\n  t=time.time()/; s/^with ProcessPoolExecutor/  with ProcessPoolExecutor/; s/^print(.48 files/  print("48 files"/; s/^import pickle/  import pickle/' dev/scan.py && tail -6 dev/scan.py && explore/bin/python dev/scan.py; nproc
```

```
return dict(info=info,trials=tr,units=units,el=el,dev=dev,sec=time.time()-t)
if __name__=="__main__":
  t=time.time()
  with ProcessPoolExecutor(16) as ex: res=list(ex.map(one,pr[:48]))
  print("48 files"',time.time()-t, np.median([r['sec'] for r in res]))
  import pickle; pickle.dump(res,open(os.environ['TMPDIR']+'/scan48.pkl','wb'))
  File "/tmp/claude-1001/dev/scan.py", line 24
    print("48 files"',time.time()-t, np.median([r['sec'] for r in res]))
                                                      ^
SyntaxError: unterminated string literal (detected at line 24)
4
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && sed -i "s/print(\"48 files\"',/print('48 files',/" dev/scan.py && explore/bin/python dev/scan.py
```

```
48 files 11.319398403167725 2.9161041975021362
Shell cwd was reset to
```

**Agent**

Process-based streaming works: 48 files in 11 s, so a full metadata scan of all 459 sessions takes about 2 minutes. Running it now.

**Agent calls Bash**

```bash
cd $TMPDIR && sed -i "s/pr\[:48\]/pr/; s/scan48/scanall/" dev/scan.py && explore/bin/python dev/scan.py
```

```
48 files 103.6419608592987 3.1710879802703857
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && cat > dev/look.py <<'E'
import pickle,os,numpy as np,pandas as pd,collections
res=pickle.load(open(os.environ['TMPDIR']+'/scanall.pkl','rb'))
info=pd.DataFrame([r['info'] for r in res])
print(len(info), info.subject.nunique(), info.lab.nunique(), info.lab.value_counts().to_dict())
print(info.rev.value_counts().to_dict()); print(info.protocol.value_counts().to_dict())
print(collections.Counter(tuple(sorted(x)) for x in info.proc))
print(collections.Counter(tuple(x) if x else None for x in info.passive))
sub=info.drop_duplicates('subject'); print(sub.sex.value_counts().to_dict())
print(info.weight.head().tolist(), info.dob.head(3).tolist())
# units
nu=sum(len(r['units']['ibl_quality_score']) for r in res); ng=sum((r['units']['ibl_quality_score']==1).sum() for r in res)
print('units',nu,'good',ng)
npb=sum(len(set(r['units']['probe_name'])) for r in res); print('probes from units',npb)
npe=sum(len(set(r['el']['probe_name'])) for r in res); print('probes from electrodes', npe)
ntr=np.array([len(r['trials']['start_time']) for r in res]); print('trials', ntr.mean(), np.median(ntr), ntr.min(), ntr.max())
print(collections.Counter(v for r in res for v in r['dev'].values() for v in [v[:60]]).most_common(10))
print(res[0]['trials'].keys())
print(collections.Counter(np.round(res[0]['trials']['gabor_stimulus_contrast'],3)))
print(collections.Counter(res[0]['trials']['mouse_wheel_choice']))
q=collections.Counter(np.round(np.concatenate([r['units']['ibl_quality_score'] for r in res]),3)); print(q)
E
explore/bin/python dev/look.py
```

```
459 139 12 {'hausserlab': 62, 'danlab': 46, 'mainenlab': 44, 'cortexlab': 42, 'angelakilab': 41, 'churchlandlab_ucla': 41, 'wittenlab': 37, 'zadorlab': 37, 'churchlandlab': 36, 'steinmetzlab': 31, 'mrsicflogellab': 25, 'hoferlab': 17}
{'2025-05-06': 459}
{'_iblrig_tasks_ephysChoiceWorld6.4.2': 182, '_iblrig_tasks_ephysChoiceWorld': 64, '_iblrig_tasks_ephysChoiceWorld6.2.5': 58, '_iblrig_tasks_ephysChoiceWorld6.4.0': 50, '_iblrig_tasks_ephysChoiceWorld6.5.3': 29, '_iblrig_tasks_ephysChoiceWorld6.6.2': 24, '_iblrig_tasks_ephysChoiceWorld6.4.1': 20, '_iblrig_tasks_ephysChoiceWorld6.1.3': 15, '_iblrig_tasks_ephysChoiceWorld6.4.3': 6, '_iblrig_tasks_ephysChoiceWorld6.6.4': 3, '_iblrig_tasks_ephysChoiceWorld6.6.1': 3, '_iblrig_tasks_ephysChoiceWorld6.5.0': 3, '_iblrig_tasks_ephysChoiceWorld6.2.3': 2}
Counter({('lick_times', 'motion_energy', 'passive_protocol', 'pose_estimation', 'pupil', 'wheel'): 378, ('lick_times', 'passive_protocol', 'wheel'): 32, ('lick_times', 'motion_energy', 'pose_estimation', 'pupil', 'wheel'): 24, ('passive_protocol', 'wheel'): 13, ('lick_times', 'motion_energy', 'passive_protocol', 'pose_estimation', 'wheel'): 5, ('lick_times', 'wheel'): 4, ('wheel',): 3})
Counter({('spontaneousActivity', 'taskReplay'): 428, None: 31})
{'M': 94, 'F': 45}
['0.01889 kg', '0.016100000000000003 kg', '0.016100000000000003 kg', '0.024 kg', '0.01838 kg'] ['2019-07-23T00:00:00-04:00', '2020-05-19T00:00:00-04:00', '2020-05-19T00:00:00-04:00']
units 621733 good 75708
probes from units 699
probes from electrodes 699
trials 645.0762527233115 601.0 401 1525
[('A PRB_1_4_0480_1 probe. Additional metadata: {"model_name": ', 403), ('A PRB_1_4_0480_1_C probe. Additional metadata: {"model_name"', 183), ('A NP1010 probe. Additional metadata: {"model_name": "NP1010"', 109), ('A NP2010 probe. Additional metadata: {"model_name": "NP2010"', 4)]
dict_keys(['auditory_cue_time', 'block_index', 'block_type', 'choice_registration_time', 'feedback_time', 'gabor_stimulus_contrast', 'gabor_st
[... 4 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && cat > dev/regions.py <<'E'
import pickle,os,numpy as np,pandas as pd,collections
res=pickle.load(open(os.environ['TMPDIR']+'/scanall.pkl','rb'))
rows=[]
bad=0
for r in res:
    el=r['el']; le=el['localized_entity']
    assert (le==np.arange(len(le))).all() or print('le order', r['info']['path'])
    ber=np.array([x.decode() if isinstance(x,bytes) else x for x in el['beryl_location']])
    me=r['units']['max_electrode']
    up=np.array([x.decode() for x in r['units']['probe_name']]); ep=np.array([x.decode() for x in el['probe_name']])
    bad+= (up!=ep[me]).sum()
    q=r['units']['ibl_quality_score']
    for b,qq in zip(ber[me],q): rows.append((r['info']['path'],b,qq))
print('probe mismatch',bad)
df=pd.DataFrame(rows,columns=['eid','beryl','q'])
print(df.beryl.value_counts().head(5))
g=df[df.q==1]; print('good',len(g), 'regions', g.beryl.nunique())
g=g[~g.beryl.isin(['void','root'])]; print('gray', len(g), g.beryl.nunique(), g.eid.nunique())
c=g.groupby(['beryl','eid']).size(); c=c[c>=5]; print('5/sess', c.sum(), c.index.get_level_values(0).nunique(), c.index.get_level_values(1).nunique())
ns=c.groupby(level=0).size(); keep=ns[ns>=2].index; c2=c[c.index.get_level_values(0).isin(keep)]; print('2 sess', c2.sum(), len(keep), c2.index.get_level_values(1).nunique())
tot=c2.groupby(level=0).sum(); keep2=tot[tot>=20].index; c3=c2[c2.index.get_level_values(0).isin(keep2)]; print('20', c3.sum(), len(keep2), c3.index.get_level_values(1).nunique())
ri=pd.read_csv(os.environ['TMPDIR']+'/paper-brain-wide-map/brainwidemap/meta/region_info.csv')
can=set(ri[ri.canonical].Beryl); print(len(can), len(can&set(keep2)), sorted(can-set(keep2)), sorted(set(keep2)-can))
allr=df[~df.beryl.isin(['void','root'])].beryl.nunique(); print('all regions any unit',allr, df.beryl.nunique())
# per-region counts compare
m=ri.set_index('Beryl')[['# recordings','# neurons','# good neurons']]
mine=pd.DataFrame({'neurons':df.groupby('beryl').size(),'good':df[df.q==1].groupby('beryl').size(),'rec':df.groupby('beryl').eid.nunique()})
j=m.join(mine,how='outer'); print(j.head(10)); print((j['# neurons']==j.neurons).mean(), (j['# good neurons']==j.good).mean(), (j['# recordings']==j.rec).mean())
print(j[(j['# neurons']!=j.neurons)].head(20))
E
explore/bin/python dev/regions.py
```

```
probe mismatch 0
beryl
root    87809
CP      25339
CA1     23169
MRN     23026
DG      18156
Name: count, dtype: int64
good 75708 regions 268
gray 65336 266 459
5/sess 63357 245 455
2 sess 62990 210 454
20 62857 201 454
210 201 ['AD', 'APr', 'CA2', 'ECU', 'FC', 'IA', 'IGL', 'PBG', 'PH'] []
all regions any unit 279 281
       # recordings  # neurons  # good neurons  neurons   good  rec
Beryl                                                              
AAA             3.0      265.0            25.0      265   25.0    3
ACAd           24.0     1960.0           369.0     1960  369.0   23
ACAv           18.0     1388.0           195.0     1388  195.0   18
[... 13 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && cat > dev/spk.py <<'E'
import json,os,h5py,remfile,time,requests,numpy as np
a=json.load(open(os.environ['TMPDIR']+'/a409.json'))
pr=sorted([x for x in a if 'desc-processed' in x['path']],key=lambda x:x['size'])
asset=pr[len(pr)//2]
print(asset['path'],asset['size']/1e9)
url=f"https://api.dandiarchive.org/api/assets/{asset['asset_id']}/download/"
url=requests.head(url,allow_redirects=True).url.split('?')[0]
t=time.time(); f=h5py.File(remfile.File(url),'r')
u=f['units']; idx=u['spike_times_index'][:]; q=u['ibl_quality_score'][:]
print('n units',len(idx),'spikes',idx[-1],'good',(q==1).sum(), time.time()-t)
st=u['spike_times']
good=np.where(q==1)[0]
start=np.r_[0,idx[:-1]]
t=time.time(); tot=0
for i in good:
    x=st[start[i]:idx[i]]; tot+=len(x)
print('good spikes',tot,'read time',time.time()-t, 'chunks', st.chunks)
E
explore/bin/python dev/spk.py
```

```
sub-KS014/sub-KS014_ses-16693458-0801-4d35-a3f1-9115c7e5acfd_desc-processed_behavior+ecephys.nwb 0.990334344
n units 1912 spikes 44345874 good 270 1.4208712577819824
good spikes 12972792 read time 15.294946908950806 chunks (1250000,)
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && cat > dev/bench.py <<'E'
import numpy as np,time
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import KFold
rng=np.random.default_rng(0)
X=rng.poisson(2,(600,30)).astype(float); y=(rng.random(600)<0.5).astype(int); X[y==1,:5]+=1
Cs=[1e-5,1e-4,1e-3,1e-2,1e-1,1,10]
def nested(X,y,seed):
    pred=np.zeros(len(y))
    outer=KFold(5,shuffle=True,random_state=seed)
    for tr,te in outer.split(X):
        inner=KFold(5,shuffle=True,random_state=seed+1)
        sc=np.zeros(len(Cs))
        for itr,ite in inner.split(tr):
            for k,C in enumerate(Cs):
                m=LogisticRegression(penalty='l1',solver='liblinear',C=C,tol=1e-3,max_iter=20000,class_weight='balanced').fit(X[tr][itr],y[tr][itr])
                p=m.predict(X[tr][ite]); yy=y[tr][ite]
                sc[k]+=0.5*((p[yy==1]==1).mean()+(p[yy==0]==0).mean())
        C=Cs[int(np.argmax(sc))]
        m=LogisticRegression(penalty='l1',solver='liblinear',C=C,tol=1e-3,max_iter=20000,class_weight='balanced').fit(X[tr],y[tr])
        pred[te]=m.predict(X[te])
    return 0.5*((pred[y==1]==1).mean()+(pred[y==0]==0).mean())
t=time.time(); 
for s in range(5): b=nested(X,y,s)
print((time.time()-t)/5, b)
E
OPENBLAS_NUM_THREADS=1 explore/bin/python dev/bench.py
```

```
<persisted-output>
Output too large (619.7KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/f751195b-d081-4c68-9fab-3efdc151580b/tool-results/b1k0jqfiu.txt

Preview (first 2KB):
/tmp/claude-1001/explore/lib/python3.13/site-packages/sklearn/linear_model/_logistic.py:1381: FutureWarning: 'penalty' was deprecated in version 1.8 and will be removed in 1.10. To avoid this warning, leave 'penalty' set to its default value and use 'l1_ratio' or 'C' instead. Use l1_ratio=0 instead of penalty='l2', l1_ratio=1 instead of penalty='l1', l1_ratio set to a float between 0 and 1 instead of penalty='elasticnet', and C=np.inf instead of penalty=None.
  warnings.warn(
/tmp/claude-1001/explore/lib/python3.13/site-packages/sklearn/linear_model/_logistic.py:1407: UserWarning: Inconsistent values: penalty=l1 with l1_ratio=0.0. penalty is deprecated. Please use l1_ratio only.
  warnings.warn(
/tmp/claude-1001/explore/lib/python3.13/site-packages/sklearn/linear_model/_logistic.py:1381: FutureWarning: 'penalty' was deprecated in version 1.8 and will be removed in 1.10. To avoid this warning, leave 'penalty' set to its default value and use 'l1_ratio' or 'C' instead. Use l1_ratio=0 instead of penalty='l2', l1_ratio=1 instead of penalty='l1', l1_ratio set to a float between 0 and 1 instead of penalty='elasticnet', and C=np.inf instead of penalty=None.
  warnings.warn(
/tmp/claude-1001/explore/lib/python3.13/site-packages/sklearn/linear_model/_logistic.py:1407: UserWarning: Inconsistent values: penalty=l1 with l1_ratio=0.0. penalty is deprecated. Please use l1_ratio only.
  warnings.warn(
/tmp/claude-1001/explore/lib/python3.13/site-packages/sklearn/linear_model/_logistic.py:1381: FutureWarning: 'penalty' was deprecated in version 1.8 and will be removed in 1.10. To avoid this warning, leave 'penalty' set to its default value and use 'l1_ratio' or 'C' instead. Use l1_ratio=0 instead of penalty='l2', l1_ratio=1 instead of pena
[... 4 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && OPENBLAS_NUM_THREADS=1 explore/bin/python -W ignore dev/bench.py; explore/bin/python -c "import sklearn;print(sklearn.__version__)"
```

```
0.5872751712799072 0.7846541272954181
1.9.1
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && cat >> dev/regions.py <<'E'
print('---')
cc=c3.reset_index(); cc.columns=['beryl','eid','n']
for r in ['VISp','GRN','IRN','LGd','LP','VISpm','VISam','MRN','SCm','PRNr','CA1','CP','PRNc','MOs']:
    x=cc[cc.beryl==r]; print(r, len(x), x.n.sum(), x.n.median())
print(cc.groupby('beryl').size().describe())
for k in ['stim_dec_sig','choice_dec_sig','fback_dec_sig','speed_dec_sig','velocity_dec_sig','stim_euc_sig','choice_euc_sig','fback_euc_sig','stim_man_sig','choice_man_sig','fback_man_sig']:
    v=ri[ri.Beryl.isin(keep2)][k]; print(k, v.sum(), v.notna().sum())
print(ri[ri.Beryl.isin(['VISp','GRN','IRN','LGd','MRN','CA1','CP'])][['Beryl','# recordings','stim_dec','choice_dec','fback_dec','speed_dec','stim_dec_sig','choice_dec_sig','fback_dec_sig']])
E
explore/bin/python dev/regions.py | sed -n '/---/,$p'
```

```
---
VISp 35 844 20.0
GRN 14 555 31.5
IRN 27 739 28.0
LGd 22 551 20.0
LP 58 1780 26.5
VISpm 10 240 13.5
VISam 18 363 16.5
MRN 99 2643 22.0
SCm 54 1645 27.5
PRNr 20 761 39.5
CA1 94 1715 12.0
CP 64 2878 43.5
PRNc 9 276 29.0
MOs 36 1270 31.0
count    201.000000
mean      12.228856
std       14.045190
min        2.000000
25%        5.000000
[... 26 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/paper-brain-wide-map/brainwidemap/decoding/functions; grep -n "def " nulldistributions.py process_targets.py | head -40; sed -n 1,200p nulldistributions.py
```

```
nulldistributions.py:8:def generate_null_distribution_session(trials_df, metadata, **kwargs):
nulldistributions.py:35:def generate_choices(pseudosess, trials_df, subjModel, modeldispatcher, model_parameters=None):
nulldistributions.py:64:def generate_imposter_session(imposterdf,
process_targets.py:14:def optimal_Bayesian(act, side):
process_targets.py:83:def compute_target_mask(target, exclude_trials_within_values):
process_targets.py:113:def compute_beh_target(trials_df, metadata, return_raw=False, **kwargs):
process_targets.py:173:def get_beh_target(trials_df, metadata, remove_old=False, **kwargs):
process_targets.py:242:def get_target_data_per_trial_wrapper(
process_targets.py:362:def load_behavior(target, sess_loader):
process_targets.py:417:def get_target_variable_in_df(
process_targets.py:475:def check_bhv_fit_exists(subject, model, eids, resultpath, modeldispatcher, single_zeta):
process_targets.py:491:def transform_data_for_decoding(ys, Xs):
process_targets.py:510:def logisticreg_criteria(ys, MIN_UNIQUE_COUNTS=3):
import numpy as np
import torch
from behavior_models.models.utils import format_input as mut_format_input
from brainbox.task.closed_loop import generate_pseudo_session
from brainwidemap.decoding.functions.process_targets import optimal_Bayesian, check_bhv_fit_exists


[... 169 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && cat > dev/spkpar.py <<'E'
import json,os,h5py,remfile,time,requests,numpy as np
from concurrent.futures import ProcessPoolExecutor
a=json.load(open(os.environ['TMPDIR']+'/a409.json'))
pr=sorted([x for x in a if 'desc-processed' in x['path']],key=lambda x:x['path'])
def load(asset):
    url=f"https://api.dandiarchive.org/api/assets/{asset['asset_id']}/download/"
    url=requests.head(url,allow_redirects=True).url.split('?')[0]
    t=time.time(); f=h5py.File(remfile.File(url),'r')
    u=f['units']; idx=u['spike_times_index'][:]; q=u['ibl_quality_score'][:]
    st=u['spike_times']; start=np.r_[0,idx[:-1]]
    good=np.where(q==1)[0]; tot=0
    # read contiguous span covering good units chunk-wise
    for i in good:
        tot+=len(st[start[i]:idx[i]])
    return tot, idx[-1], time.time()-t
if __name__=='__main__':
    rng=np.random.default_rng(1); sel=[pr[i] for i in rng.choice(len(pr),16,replace=False)]
    for n in (8,16):
        t=time.time()
        with ProcessPoolExecutor(n) as ex: r=list(ex.map(load,sel))
        print(n, time.time()-t, [round(x[2]) for x in r], sum(x[0] for x in r)/1e6, sum(x[1] for x in r)/1e6)
E
explore/bin/python dev/spkpar.py
```

```
8 48.31363606452942 [12, 16, 13, 19, 20, 4, 18, 16, 7, 20, 18, 19, 18, 31, 27, 14] 161.733594 673.815074
16 45.89869236946106 [21, 24, 21, 30, 33, 5, 31, 31, 9, 31, 31, 31, 33, 45, 40, 25] 161.733594 673.815074
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && sed -i "s/f=h5py.File(remfile.File(url),'r')/f=h5py.File(remfile.File(url),'r',rdcc_nbytes=64*1024**2,rdcc_nslots=10007)/; s/for n in (8,16)/for n in (8,)/" dev/spkpar.py && explore/bin/python dev/spkpar.py
```

```
8 24.439329624176025 [6, 10, 6, 11, 8, 4, 10, 6, 4, 10, 12, 11, 8, 14, 14, 7] 161.733594 673.815074
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/paper-brain-wide-map/brainwidemap/single_cell_stats; wc -l *; sed -n 1,200p single_cell_util.py
```

```
0 __init__.py
  221 single_cell_Working_example_block.py
  170 single_cell_Working_example_choice.py
  189 single_cell_Working_example_feedback.py
  174 single_cell_Working_example_stimulus.py
  214 single_cell_util.py
  968 total
import numpy as np
from scipy.stats import rankdata


def Time_TwoNmannWhitneyUshuf(x, y, bx, by, nShuf):
    # Condition-combined test for indivdiual block, control time drift effect
    nx = len(x)
    ny = len(y)

    ################### x>y #####################
    t1 = np.zeros((nShuf + 1, nx))

    t2 = np.append(x, y, axis=0)
[... 188 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/paper-brain-wide-map/brainwidemap/single_cell_stats; cat single_cell_Working_example_stimulus.py; sed -n 200,214p single_cell_util.py
```

```
from pathlib import Path

import numpy as np
from one.api import ONE
from scipy.stats import rankdata

from brainbox.population.decode import get_spike_counts_in_bins

from brainwidemap import load_good_units, load_trials_and_mask
from brainwidemap.single_cell_stats.single_cell_util import Time_TwoNmannWhitneyUshuf

########### p-value for visual stimulus-side############

def get_stim_time_shuffle(rate, c_L, c_R, block_label, choice_label, nShuf=3000):
    # nShuf=10000;
    # nShuf=5000;

    num_neuron = len(rate[:, 0])

    p = np.zeros(num_neuron)
[... 170 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/paper-brain-wide-map/brainwidemap/manifold; grep -n "def \|sts\|0.0125\|0.002\|stim_restr\|'stim'\|pre_post\|0.7\|sqrt\|lat\b\|latency" state_space_bwm.py | head -120
```

```
35:from statsmodels.stats.multitest import multipletests
51:for split in ['choice', 'stim','fback','block']:
67:blue_left = [0.13850039, 0.41331206, 0.74052025]
68:red_right = [0.66080672, 0.21526712, 0.23069468]
70:b_size = 0.0125  # bin size [sec] for neural binning
71:sts = 0.002  # stride size in [sec] for overlapping bins
75:align = {'stim': 'stim on',
80:exs0 = {'stim_restr': ['NB', 'SOC'],
116:def pre_post(split, can=False):
125:    pre_post0 = {'stim': [0, 0.15],
127:                 'fback': [0, 0.7]}
130:    pre_post_can =  {'stim': [0, 0.1],
134:    pp = pre_post_can if can else pre_post0
142:def grad(c, nobs, fr=1):
154:def eid_probe2pid(eid, probe_name):
162:def fn2_eid_probe_pid(u):
172:def generate_pseudo_blocks(
214:def get_name(brainregion):
222:def get_region_info(reg):
231:def get_eid_info(eid):
[... 92 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/paper-brain-wide-map/brainwidemap/manifold; sed -n 110,140p state_space_bwm.py; sed -n 240,470p state_space_bwm.py; sed -n 840,960p state_space_bwm.py
```

```
# save results here
pth_res = Path(one.cache_dir,'bwm_res', 'manifold', 'res')
pth_res.mkdir(parents=True, exist_ok=True)

sigl = 0.05  # significance level (for stacking, plotting, fdr)

def pre_post(split, can=False):
    '''
    [pre_time, post_time] relative to alignment event
    split could be contr or restr variant, then
    use base window
    
    ca: If true, use canonical time windows
    '''

    pre_post0 = {'stim': [0, 0.15],
                 'choice': [0.15, 0],
                 'fback': [0, 0.7]}

    # canonical windows
[... 363 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/paper-brain-wide-map/brainwidemap/meta/Results; $TMPDIR/explore/bin/python -c "
import pandas as pd
d=pd.read_pickle('stim.pkl'); print(type(d)); 
print(d.columns.tolist() if hasattr(d,'columns') else list(d)[:20]); print(d.head() if hasattr(d,'head') else '')
print(d[d.region.isin(['LGd','VISp','LP','VISpm','VISam','MRN','SCm','PRNr','IRN','GRN'])] if 'region' in getattr(d,'columns',[]) else '')
"
```

```
<class 'pandas.DataFrame'>
['region', 'euclidean_latency', 'euclidean_effect', 'glm_effect', 'mannwhitney_effect', 'decoding_effect', 'decoding_significant', 'mannwhitney_significant', 'euclidean_significant']
  region  euclidean_latency  ...  mannwhitney_significant  euclidean_significant
0   ACAd           0.082979  ...                        0                      1
1   ACAv           0.038298  ...                        0                      0
2    ACB           0.085106  ...                        0                      1
3    AId           0.068085  ...                        0                      0
4    AIp           0.029787  ...                        0                      1

[5 rows x 9 columns]
    region  euclidean_latency  ...  mannwhitney_significant  euclidean_significant
42     GRN           0.089362  ...                        0                      1
46     IRN           0.089362  ...                        0                      1
50     LGd           0.034043  ...                        1                      1
53      LP           0.046809  ...                        1                      1
64     MRN           0.078723  ...                        0                      1
90    PRNr           0.089362  ...                        0                      1
101    SCm           0.078723  ...                        0                      1
128  VISam           0.065957  ...                        1                      1
131   VISp           0.044681  ...                        1                      1
[... 4 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && cat >> dev/regions.py <<'E'
print('=== union')
def union(rs): return cc[cc.beryl.isin(rs)].eid.nunique(), len(cc[cc.beryl.isin(rs)])
base=['VISp','GRN','IRN','LGd','LP','VISpm','VISam']
print(union(base), union(base+['PRNr']), union(base+['PRNr','MRN','SCm']), union(['VISp','GRN','IRN']))
ns=cc.groupby('beryl').size()
rng=np.random.default_rng(409)
pool=sorted(ns[(ns<=12)].index.difference(base)); print(len(pool))
pick=sorted(rng.choice(pool,7,replace=False)); print(pick, ns[pick].to_dict(), union(base+pick), union(['VISp','GRN','IRN']+pick))
E
explore/bin/python dev/regions.py | sed -n '/=== union/,$p'
```

```
=== union
(151, 184) (170, 204) (215, 357) (67, 76)
140
[np.str_('ACAv'), np.str_('CL'), np.str_('HATA'), np.str_('LDT'), np.str_('PA'), np.str_('PVT'), np.str_('TR')] {np.str_('ACAv'): 11, np.str_('CL'): 2, np.str_('HATA'): 5, np.str_('LDT'): 2, np.str_('PA'): 7, np.str_('PVT'): 5, np.str_('TR'): 3} (168, 219) (94, 111)
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/paper-brain-wide-map/brainwidemap/single_cell_stats; grep -n "con1 =\|con2 =\|con3 =\|TimeWindow\|load_trials_and_mask\|_times\|nShuf)" single_cell_Working_example_choice.py single_cell_Working_example_feedback.py | head -60
```

```
single_cell_Working_example_choice.py:9:from brainwidemap.bwm_loading import load_good_units, load_trials_and_mask
single_cell_Working_example_choice.py:37:        con1 = np.logical_and(block_label == 0.8, c_L > 0)
single_cell_Working_example_choice.py:38:        con2 = np.logical_and(choice_label == 1, con1)
single_cell_Working_example_choice.py:39:        con3 = np.logical_and(choice_label == -1, con1)
single_cell_Working_example_choice.py:53:        numer2 = Time_TwoNmannWhitneyUshuf(x2, y2, bx2, by2, nShuf)
single_cell_Working_example_choice.py:56:        con1 = np.logical_and(block_label == 0.8, c_R > 0)
single_cell_Working_example_choice.py:57:        con2 = np.logical_and(choice_label == 1, con1)
single_cell_Working_example_choice.py:58:        con3 = np.logical_and(choice_label == -1, con1)
single_cell_Working_example_choice.py:71:        numer5 = Time_TwoNmannWhitneyUshuf(x5, y5, bx5, by5, nShuf)
single_cell_Working_example_choice.py:74:        con1 = np.logical_and(block_label == 0.2, c_L > 0)
single_cell_Working_example_choice.py:75:        con2 = np.logical_and(choice_label == 1, con1)
single_cell_Working_example_choice.py:76:        con3 = np.logical_and(choice_label == -1, con1)
single_cell_Working_example_choice.py:89:        numer3 = Time_TwoNmannWhitneyUshuf(x3, y3, bx3, by3, nShuf)
single_cell_Working_example_choice.py:92:        con1 = np.logical_and(block_label == 0.2, c_R > 0)
single_cell_Working_example_choice.py:93:        con2 = np.logical_and(choice_label == 1, con1)
single_cell_Working_example_choice.py:94:        con3 = np.logical_and(choice_label == -1, con1)
single_cell_Working_example_choice.py:107:        numer6 = Time_TwoNmannWhitneyUshuf(x6, y6, bx6, by6, nShuf)
single_cell_Working_example_choice.py:116:        p[i_neuron] = t[0] / (1 + nShuf)
single_cell_Working_example_choice.py:121:def BWM_choice_test(one, pid, eid, TimeWindow=np.array([-0.1, 0.0]),):
single_cell_Working_example_choice.py:125:    trials, mask = load_trials_and_mas
[... 28 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && explore/bin/python - <<'E'
import pickle,os,numpy as np,pandas as pd,collections
res=pickle.load(open(os.environ['TMPDIR']+'/scanall.pkl','rb'))
c=collections.Counter()
for r in res:
    t=r['trials']
    for s,ch,rw,con in zip(t['gabor_stimulus_side'],t['mouse_wheel_choice'],t['is_mouse_rewarded'],t['gabor_stimulus_contrast']):
        c[(s.decode(),ch.decode(),bool(rw))]+=1
for k,v in sorted(c.items()): print(k,v)
t=pd.DataFrame({k:(v.astype(str) if v.dtype.kind in 'OS' else v) for k,v in res[0]['trials'].items()})
print(t.head(12).T)
nan=collections.Counter()
for r in res:
    for k,v in r['trials'].items():
        if v.dtype.kind=='f': nan[k]+=np.isnan(v).sum()
print(nan)
rt=np.concatenate([r['trials']['wheel_movement_onset_time']-r['trials']['gabor_stimulus_onset_time'] for r in res])
print(np.nanpercentile(rt,[0,1,5,25,50,75,95,99,100]), np.mean(rt<0.08), np.nanmean(rt<0.08), (rt<0).mean())
E
```

```
('left', 'clockwise', True) 123603
('left', 'counter_clockwise', False) 27097
('left', 'none', False) 626
('right', 'clockwise', False) 25213
('right', 'counter_clockwise', True) 119025
('right', 'none', False) 526
                                           0   ...          11
auditory_cue_time                  268.879856  ...   563.47322
block_index                                 0  ...           0
block_type                           unbiased  ...    unbiased
choice_registration_time           313.593986  ...  564.633785
feedback_time                      313.594909  ...  564.633961
gabor_stimulus_contrast                 100.0  ...        6.25
gabor_stimulus_offset_time         315.645189  ...  565.720301
gabor_stimulus_onset_time          268.974705  ...  563.472356
gabor_stimulus_side                      left  ...        left
is_mouse_rewarded                       False  ...        True
mouse_wheel_choice          counter_clockwise  ...   clockwise
probability_left                          0.5  ...         0.5
quiescence_period                    0.610104  ...    0.573514
[... 11 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n -i "dandi" paper/nature.txt | head; grep -n "^22\.\|^ *22 " paper/nature.txt | head -3; awk 'NR>=521 && NR<=640' paper/nature.txt | grep -n -i "brainwide\|data release" | head
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd $TMPDIR && explore/bin/python - <<'E'
import requests,json,os
def lst(v):
    url=f'https://api.dandiarchive.org/api/dandisets/000409/versions/{v}/assets/?page_size=1000'; out={}
    while url:
        r=requests.get(url).json(); out.update({a['path']:(a['size'],a['blob'] if 'blob' in a else a.get('asset_id')) for a in r['results']}); url=r['next']
    return out
d=lst('draft'); p=lst('0.260309.1324')
print(len(d),len(p), set(d)==set(p), sum(d[k][0]!=p[k][0] for k in p))
a=requests.get('https://api.dandiarchive.org/api/dandisets/000409/versions/0.260309.1324/assets/?page_size=2').json()['results'][0]; print(a)
md=requests.get('https://api.dandiarchive.org/api/dandisets/000409/versions/draft/').json()
mp=requests.get('https://api.dandiarchive.org/api/dandisets/000409/versions/0.260309.1324/').json()
print([k for k in set(md)|set(mp) if md.get(k)!=mp.get(k)])
print(json.dumps(md.get('relatedResource'))[:1500])
E
```

```
2048 2048 True 0
{'asset_id': '9217026b-1002-44f3-a1ab-f3d4de98ff44', 'blob': 'ddf12931-74f6-436b-84e6-d2afb0abc0f9', 'zarr': None, 'path': 'sub-NYU-12/sub-NYU-12_ses-b182b754-3c3e-4942-8144-6ee790926b58_ecephys+image/sub-NYU-12_ses-b182b754-3c3e-4942-8144-6ee790926b58_VideoRightCamera.mp4', 'size': 1668745947, 'created': '2025-12-07T20:35:42.203507Z', 'modified': '2026-03-09T13:24:11.036713Z'}
['doi', 'contributor', 'citation', 'manifestLocation', 'version', 'relatedResource', 'publishedBy', 'about', 'datePublished', 'url', 'id']
[{"url": "https://www.nature.com/articles/s41586-025-09235-0", "name": "A brain-wide map of neural activity during complex behaviour", "relation": "dcite:IsDescribedBy", "schemaKey": "Resource", "identifier": "https://doi.org/10.1038/s41586-025-09235-0", "resourceType": "dcite:JournalArticle"}, {"url": "https://figshare.com/articles/preprint/Data_release_-_Brainwide_map_-_Q4_2022/21400815", "name": "Data release - Brainwide map - Q4 2022", "relation": "dcite:IsDescribedBy", "schemaKey": "Resource"}, {"url": "https://figshare.com/articles/preprint/A_standardized_and_reproducible_method_to_measure_decision-making_in_mice_Appendix_2_IBL_protocol_for_mice_training/11634729", "name": "Behavior: Appendix 2: IBL protocol for mice training", "relation": "dcite:IsDocumentedBy", "schemaKey": "Resource", "identifier": "https://doi.org/10.6084/m9.figshare.11634729.v5"}, {"url": "https://github.com/catalystneuro/IBL-to-nwb", "name": "Conversion Software", "relation": "dcite:IsCompiledBy", "schemaKey": "Resource", "identifier": "", "repository": "https://github.com/catalystneuro/IBL-to-nwb", "resourceType": "dcite:Software"}, {"url": "https://github.com/dandi/example-notebooks/blob/master/000409/IBL/bwm_usage_notebook.ipynb", "name": "IBL - Brain Wide Map Usage Notebook", "relation": "dcite:IsSupplementedBy", "schemaKey": "Resource", "resourceType": "dcite:ComputationalNotebook"}]
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && git clone -q https://github.com/catalystneuro/IBL-to-nwb.git && cd IBL-to-nwb && git log -1 --format='%H %cd' && grep -rn "firstMovement\|wheel_movement_onset\|counter_clockwise\|probabilityLeft\|ibl_quality_score\|rewardVolume" --include=*.py src | head -30
```

```
54030ac4eb40a74978ac1f6ef6e966278b9d3f34 Fri Apr 10 00:20:28 2026 -0600
src/ibl_to_nwb/testing/_consistency_checks.py:199:    deterministically computed from probabilityLeft. If probabilityLeft matches, these
src/ibl_to_nwb/testing/_consistency_checks.py:278:    # computed from probabilityLeft, so checking them is redundant)
src/ibl_to_nwb/datainterfaces/_ibl_sorting_interface.py:54:    "ibl_quality_score": {
src/ibl_to_nwb/datainterfaces/_ibl_sorting_interface.py:65:        "description": "Binary pass/fail (0.0 or 1.0) using sliding refractory period algorithm. Primary metric for ibl_quality_score. Aligns with SpikeInterface's sliding_rp_violations.",
src/ibl_to_nwb/datainterfaces/_brainwide_map_trials_interface.py:20:#   - choice: -1/0/+1 -> "counter_clockwise"/"none"/"clockwise"
src/ibl_to_nwb/datainterfaces/_brainwide_map_trials_interface.py:23:#   - probabilityLeft -> also used to derive "block_index" and "block_type"
src/ibl_to_nwb/datainterfaces/_brainwide_map_trials_interface.py:46:    "wheel_movement_onset_time": {
src/ibl_to_nwb/datainterfaces/_brainwide_map_trials_interface.py:47:        "ibl_name": "firstMovement_times",
src/ibl_to_nwb/datainterfaces/_brainwide_map_trials_interface.py:74:        "description": "Mouse's response: 'counter_clockwise' (counter_clockwise wheel turn moving stimulus leftward), 'clockwise' (clockwise wheel turn moving stimulus rightward), or 'none' (no response within 60s timeout). clockwise and counter_clockwise are wheel movements as seen from the perspective of the mouse",
src/ibl_to_nwb/datainterfaces/_brainwide_map_trials_interface.py:81:        "ibl_name": "rewardVolume",
src/ibl_to_nwb/datainterfaces/_brainwide_map_trials_interface.py:86:        "ibl_name": "probabilityLeft",
src/ibl_to_nwb/datainterfaces/_brainwide_map_trials_interface.py:90:        "ibl_name": "block_type",  # computed from probabilityLeft
src/ibl_to_nwb/datainterfaces/_brainwide_map_trials_interface.py:94:        "ibl_name": "block_index",  # computed
[... 18 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/IBL-to-nwb && grep -rn "revision" --include=*.py src | grep -v "^.*#" | head -20; grep -rn "2024-05-06\|2025-05-06" -r src | head
```

```
src/ibl_to_nwb/utils/electrodes.py:344:    Note: Raw ephys data is NOT revision-dependent (raw recordings never change).
src/ibl_to_nwb/utils/electrodes.py:696:    loader = SpikeSortingLoader(pid=pid, eid=eid, pname=probe_name, one=one, atlas=atlas, revision=BWM_REVISION)
src/ibl_to_nwb/converters/_ibl_spikeglx_converter.py:76:        self.revision = self.REVISION
src/ibl_to_nwb/converters/_ibl_spikeglx_converter.py:225:                ssl.raw_electrophysiology(band=band, stream=False, revision=cls.REVISION)
src/ibl_to_nwb/testing/_consistency_checks.py:75:    revision = nwbfile.lab_meta_data["ibl_metadata"].revision
src/ibl_to_nwb/testing/_consistency_checks.py:76:    load_kwargs = dict(collection="alf", revision=revision)
src/ibl_to_nwb/testing/_consistency_checks.py:107:    revision = nwbfile.lab_meta_data["ibl_metadata"].revision
src/ibl_to_nwb/testing/_consistency_checks.py:108:    load_kwargs = dict(collection="alf", revision=revision)
src/ibl_to_nwb/testing/_consistency_checks.py:123:    revision = nwbfile.lab_meta_data["ibl_metadata"].revision
src/ibl_to_nwb/testing/_consistency_checks.py:124:    load_kwargs = dict(collection="alf", revision=revision)
src/ibl_to_nwb/testing/_consistency_checks.py:149:    revision = nwbfile.lab_meta_data["ibl_metadata"].revision
src/ibl_to_nwb/testing/_consistency_checks.py:150:    load_kwargs = dict(collection="alf", revision=revision)
src/ibl_to_nwb/testing/_consistency_checks.py:152:    session_loader = SessionLoader(one=one, eid=eid, revision=revision)
src/ibl_to_nwb/testing/_consistency_checks.py:264:    revision = nwbfile.lab_meta_data["ibl_metadata"].revision
src/ibl_to_nwb/testing/_consistency_checks.py:267:    session_loader = SessionLoader(one=one, eid=eid, revision=revision)
src/ibl_to_nwb/testing/_consistency_checks.py:294:    revision = nwbfile.lab_meta_data["ibl_metadata"].revision
src/ibl_to_nwb/testing/_consistency_checks.py:295:    load_kwargs = dict(collection="alf", revision=revision)
src/ibl_to_nwb/testing
[... 13 more lines not kept]
```

**Agent calls Bash**

```bash
mkdir -p entries/000409-ibl-2025 claims/000409; ls entries/001453-fouke-2025; cat entries/001453-fouke-2025/requirements.lock.txt | head -5; grep -n "n_jobs\|ProcessPool\|Thread" entries/*/*.py | head
```

```
README.md
entry.yaml
omr.py
reproduce_fouke_2025.ipynb
requirements.in
requirements.lock.txt
# This file was autogenerated by uv via the following command:
#    uv pip compile --python-version 3.13 requirements.in -o requirements.lock.txt
acres==0.5.0
    # via bidsschematools
aiohappyeyeballs==2.7.1
entries/000003-senzai-2017/dg.py:47:from concurrent.futures import ProcessPoolExecutor
entries/000003-senzai-2017/dg.py:458:    with ProcessPoolExecutor(workers) as ex:
entries/000004-chandravadia-2020/recogmem.py:31:from concurrent.futures import ThreadPoolExecutor
entries/000004-chandravadia-2020/recogmem.py:246:    with ThreadPoolExecutor(workers) as pool:
entries/000006-economo-2018/alm.py:34:from concurrent.futures import ThreadPoolExecutor
entries/000006-economo-2018/alm.py:140:    with ThreadPoolExecutor(max_workers=max_workers) as pool:
entries/000035-scala-2021/scala34.py:31:from concurrent.futures import ProcessPoolExecutor
entries/000035-scala-2021/scala34.py:190:    with ProcessPoolExecutor(workers) as ex:
entries/000041-watson-2016/sleepstates.py:336:    from concurrent.futures import ProcessPoolExecutor
[... 1 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && explore/bin/python -W error -c "
from sklearn.linear_model import LogisticRegression
import numpy as np
X=np.random.rand(100,5); y=np.r_[np.zeros(50),np.ones(50)]
m=LogisticRegression(C=1.0,l1_ratio=1.0,solver='liblinear',tol=1e-3,max_iter=20000,class_weight='balanced').fit(X,y); print(m.coef_)
"
```

```
[[0.         0.32233049 0.16676745 0.00108611 0.        ]]
Shell cwd was reset to
```

**Agent calls Write**

```json
{
 "file_path": "entries/000409-ibl-2025/bwm.py",
 "content": "\"\"\"Loading and measures for the IBL brain-wide map, dandiset 000409.\n\nInternational Brain Laboratory et al. (2025), A brain-wide map of neural activity during complex\nbehaviour, Nature 645, 177-191, doi:10.1038/s41586-025-09235-0.\n\nEach session has one processed NWB file (`desc-processed_behavior+ecephys.nwb`) with the trials\ntable, the spike-sorted units of all its probes, the electrode localisation in the Allen CCF (with\nthe Beryl and Cosmos groupings), the wheel, licks and, for most sessions, video pose estimates.\nFiles are streamed from the archive at the pinned version with remfile; nothing is written to disk.\nh5py serialises its calls within a process, so files are read in parallel processes.\n\nWhere the parameters come from. \"Methods\" is the paper's Methods section; \"code\" is the paper's\nrepository https://github.com/int-brain-lab/paper-brain-wide-map at commit\n118fc36cb3602934466ad2c6087c2b3b441f9f1f.\n\n- Unit inclusion: a well-isolated unit passes all three IBL metrics (Methods; code `label == 1`,\n  here `ibl_quality_score == 1`). A unit's region is the Beryl region of its peak channel (code,\n  `atlas_id` of the cluster mapped to Beryl). Regions `void` and `root` are dropped; a region-session\n  needs at least 5 units, a region at least 2 such sessions and 20 units (Methods; code\n  `meta/inclusion_info.py`).\n- Trial inclusion: trials with a missing stimulus onset, choice, block probability, feedback type\n  or time, or first movement time are dropped, as are trials whose first movement time minus\n  stimulus onset is outside 0.08 to 2 s (Methods). A session whose performance on 100% contrast\n  trials is not above 90% is first truncated from the end until it is, keeping at least 400 trials\n  (code `load_trials_and_mask`, `truncate_to_pass`).\n- Windows: stimulus 0 to 0.1 s after stimulus onset, choice 0.1 s before the first movement, feedback\n  0 to 0.2 s after feedback (Methods; code decoding settings).\n- Decoding: L1 logistic regression (liblinear, tol 0.001, up to 20000 iterations, balanced class\n  weights), nested 5 x 5 cross-validation with interleaved random folds, C from\n  1e-5 to 10, balanced accuracy of the pooled test predictions (Methods). The paper repeats the\n  cross-validation 10 times and uses 200 null sessions; here `N_RUNS` and `N_NULL` are smaller to fit\n  the time limit, and each null session reuses the C chosen in each outer fold for the real labels\n  (`decode`); `decode_nested_null` runs the full nested search for a null session, for comparison.\n- Null sessions: stimulus side from pseudo-sessions drawn from the task's generative process\n  (Methods: 90 unbiased trials with a fixed contrast set, then alternating 0.2/0.8 blocks whose\n  lengths follow an exponential of scale 60 truncated to 20 to 100 trials, contrasts 1, 0.25, 0.125,\n  0.0625 and 0 in the ratio 2:2:2:2:1). Choice and feedback from synthetic sessions: an\n  action-kernel model fitted to each session (Methods give the prior update; the choice policy here\n  is a logistic function of the signed contrast and the prior, a common choice, as the companion\n  paper's model package is not used) simulated on pseudo-session stimuli.\n- Single-cell tests: condition-combined Mann-Whitney test with 3000 permutations within individual\n  blocks, combined with a simple Mann-Whitney test; a unit is selective when p < 0.001 (simple) and\n  p < 0.05 (combined) (Methods; code `single_cell_stats`). Strata are the biased blocks crossed with\n  choice (stimulus test) or with stimulus side (choice test); zero-contrast and unbiased-block trials\n  are left out (code).\n- Population trajectories: 12.5 ms bins with a 2 ms stride over 0 to 0.15 s after stimulus onset,\n  trial-averaged per cell for left and right stimuli, distance sqrt(sum over cells of squared\n  differences / number of cells) minus its minimum, null from 1000 permutations of stimulus side\n  within trials of the same block and choice, latency the first time above 70% of the maximum that\n  is also significant point-wise at 0.05, on the code's time axis linspace(0, 0.15, 72) (Methods and\n  code `manifold/state_space_bwm.py`).\n\"\"\"\n\nfrom __future__ import annotations\n\nimport os\nfrom concurrent.futures import ProcessPoolExecutor\n\nimport h5py\nimport numpy as np\nimport pandas as pd\nimport remfile\nimport requests\nfrom dandi.dandiapi import DandiAPIClient\nfrom scipy import stats\nfrom sklearn.linear_model import LogisticRegression\n\nDANDISET_ID = \"000409\"\nDANDISET_VERSION = \"0.260309.1324\"\nAPI = \"https://api.dandiarchive.org/api\"\n\nN_WORKERS = 8                  # processes streaming files at once\nCHUNK_CACHE = 64 * 1024 ** 2   # the spike arrays are stored in 10 MB chunks\n\nMIN_RT, MAX_RT = 0.08, 2.0\nMIN_UNITS_SESSION, MIN_SESSIONS, MIN_UNITS_REGION = 5, 2, 20\nWINDOWS = {  # event column, start, stop (s)\n    \"stim\": (\"stim_on\", 0.0, 0.1),\n    \"choice\": (\"first_move\", -0.1, 0.0),\n    \"feedback\": (\"feedback_time\", 0.0, 0.2),\n}\nCLOCK_OFFSETS = np.round(np.arange(-1.0, 0.41, 0.2), 2)   # 0.2 s windows around feedback\nC_GRID = np.array([1e-5, 1e-4, 1e-3, 1e-2, 1e-1, 1.0, 10.0])\nN_FOLDS = 5\nN_RUNS = 1\nN_NULL = 100\nTRAJ_BIN, TRAJ_STRIDE, TRAJ_POST = 0.0125, 0.002, 0.15\nTRAJ_SHIFTS = int(TRAJ_BIN // TRAJ_STRIDE)                 # 6, as in the code\nTRAJ_NBINS = int(round(TRAJ_POST / TRAJ_BIN))              # 12\nTRAJ_TIMES = np.linspace(0, TRAJ_POST, TRAJ_SHIFTS * TRAJ_NBINS)   # the code's time axis\nN_PERM_TRAJ = 1000\nN_SHUF_CELL = 3000\nALPHA_MW, ALPHA_CCMW = 0.001, 0.05\nPSTH_BIN, PSTH_POST = 0.005, 1.0\n\n\n# --- assets and streaming -------------------------------------------------------------------\n\ndef list_assets() -> pd.DataFrame:\n    \"\"\"Every asset of the pinned version: path, asset id, size, subject, session and kind.\"\"\"\n    client = DandiAPIClient()\n    ds = client.get_dandiset(DANDISET_ID, DANDISET_VERSION)\n    rows = []\n    for a in ds.get_assets():\n        name = a.path.split(\"/\")[-1]\n        rows.append({\"path\": a.path, \"asset_id\": a.identifier, \"size\": a.size,\n                     \"subject\": a.path.split(\"/\")[0][4:],\n                     \"eid\": name.split(\"_ses-\")[1][:36] if \"_ses-\" in name else None,\n                     \"kind\": (\"processed\" if \"desc-processed\" in name else \"raw\" if \"desc-raw\" in name\n                              else name.rsplit(\"_\", 1)[-1].replace(\".mp4\", \"\"))})\n    return pd.DataFrame(rows)\n\n\ndef open_nwb(asset_id: str) -> h5py.File:\n    url = f\"{API}/assets/{asset_id}/download/\"\n    for _ in range(3):\n        try:\n            url = requests.head(url, allow_redirects=True, timeout=60).url.split(\"?\")[0]\n            break\n        except requests.RequestException:\n            continue\n    return h5py.File(remfile.File(url), \"r\", rdcc_nbytes=CHUNK_CACHE, rdcc_nslots=10007)\n\n\ndef _str(x):\n    v = x[()] if hasattr(x, \"shape\") else x\n    return v.decode() if isinstance(v, bytes) else v\n\n\ndef _col(group, name):\n    v = group[name][:]\n    if v.dtype.kind in \"OS\":\n        v = np.array([x.decode() if isinstance(x, bytes) else x for x in v])\n    return v\n\n\ndef run_parallel(fn, items, workers=N_WORKERS):\n    with ProcessPoolExecutor(workers) as ex:\n        return list(ex.map(fn, items))\n\n\n# --- session metadata -----------------------------------------------------------------------\n\ndef scan_session(asset_id: str) -> dict:\n    \"\"\"Everything but the spikes: subject, trials, units with regions, probes and small streams.\"\"\"\n    with open_nwb(asset_id) as f:\n        subj = f[\"general/subject\"]\n        info = {k: _str(subj[k]) for k in (\"subject_id\", \"sex\", \"date_of_birth\", \"weight\", \"species\")}\n        info.update({k: _str(f[f\"general/{k}\"]) for k in (\"lab\", \"institution\", \"protocol\", \"session_id\")})\n        info[\"session_start\"] = _str(f[\"session_start_time\"])\n        info[\"revision\"] = _str(f[\"general/ibl_metadata/revision\"])\n        info[\"processing\"] = sorted(f[\"processing\"].keys())\n        tr = f[\"intervals/trials\"]\n        trials = pd.DataFrame({k: _col(tr, k) for k in tr if k != \"id\"})\n        u = f[\"units\"]\n        units = pd.DataFrame({k: _col(u, k) for k in (\n            \"ibl_quality_score\", \"max_electrode\", \"probe_name\", \"spike_count\", \"firing_rate\",\n            \"median_spike_amplitude_uV\", \"noise_cutoff\", \"sliding_rp_violation\")})\n        idx = u[\"spike_times_index\"][:]\n        units[\"n_spikes_index\"] = np.diff(np.r_[0, idx])\n        loc = f[\"general/localization/ElectrodesIBLBregma\"]\n        entity = loc[\"localized_entity\"][:]\n        beryl = np.empty(len(entity), dtype=object)\n        beryl[entity] = _col(loc, \"beryl_location\")\n        loc_probe = np.empty(len(entity), dtype=object)\n        loc_probe[entity] = _col(loc, \"probe_name\")\n        units[\"region\"] = beryl[units.max_electrode.values]\n        units[\"region_probe\"] = loc_probe[units.max_electrode.values]\n        probes = {k: f[\"general/devices\"][k].attrs.get(\"description\", \"\") for k in f[\"general/devices\"]}\n        epochs = pd.DataFrame({k: _col(f[\"intervals/epochs\"], k)\n                               for k in (\"start_time\", \"stop_time\", \"protocol_type\")})\n        passive = None\n        if \"passive_protocol\" in f[\"processing\"]:\n            pi = f[\"processing/passive_protocol/passive_intervals\"]\n            passive = list(_col(pi, \"protocol_name\"))\n        licks = (f[\"processing/lick_times/EventsLickTimes/timestamps\"][:]\n                 if \"lick_times\" in f[\"processing\"] else np.array([]))\n        wheel_moves = f[\"processing/wheel/WheelMovementIntervals/start_time\"][:]\n    return {\"asset_id\": asset_id, \"info\": info, \"trials\": trials, \"units\": units, \"probes\": probes,\n            \"epochs\": epochs, \"passive\": passive, \"licks\": licks, \"wheel_moves\": wheel_moves}\n\n\ndef task_table(trials: pd.DataFrame) -> pd.DataFrame:\n    \"\"\"The trials table in the paper's terms.\n\n    side: +1 stimulus on the right, -1 on the left. choice: +1 for the response that is rewarded when\n    the stimulus is on the right (counter-clockwise, which the table says moves the stimulus left,\n    towards the centre), -1 for clockwise, 0 for no response. contrast as a fraction.\n    \"\"\"\n    t = pd.DataFrame({\n        \"stim_on\": trials.gabor_stimulus_onset_time.values,\n        \"go_cue\": trials.auditory_cue_time.values,\n        \"first_move\": trials.wheel_movement_onset_time.values,\n        \"feedback_time\": trials.feedback_time.values,\n        \"contrast\": trials.gabor_stimulus_contrast.values / 100.0,\n        \"side\": np.where(trials.gabor_stimulus_side.values == \"right\", 1, -1),\n        \"choice\": trials.mouse_wheel_choice.map({\"counter_clockwise\": 1, \"clockwise\": -1, \"none\": 0}).values,\n        \"correct\": trials.is_mouse_rewarded.values.astype(bool),\n        \"p_left\": trials.probability_left.values,\n        \"block\": trials.block_index.values,\n        \"reward_ul\": trials.reward_volume_uL.values,\n    })\n    t[\"signed_contrast\"] = t.side * t.contrast\n    t[\"rt\"] = t.first_move - t.stim_on\n    return t\n\n\ndef perf_easy(t: pd.DataFrame) -> float:\n    easy = t.contrast >= 0.5\n    return float(t.correct[easy].mean()) if easy.any() else np.nan\n\n\ndef analysis_mask(t: pd.DataFrame) -> tuple[np.ndarray, int]:\n    \"\"\"Trials the paper analyses, and the number of trials kept after truncation.\"\"\"\n    n = len(t)\n    good = lambda k: k >= 400 and perf_easy(t.iloc[:k]) > 0.9\n    while not good(n) and n > 400:\n        n -= 1\n    keep = np.zeros(len(t), bool)\n    keep[:n] = True\n    ok = (keep & t.stim_on.notna() & t.first_move.notna() & t.feedback_time.notna()\n          & t.p_left.notna() & (t.choice != 0) & (t.rt >= MIN_RT) & (t.rt <= MAX_RT))\n    return ok.values, n\n\n\ndef canonical_units(scans: list[dict]) -> pd.DataFrame:\n    \"\"\"Well-isolated units in the canonical regions, with the counts at each inclusion step.\"\"\"\n    rows = []\n    for s in scans:\n        u = s[\"units\"]\n        rows.append(pd.DataFrame({\"eid\": s[\"info\"][\"session_id\"], \"asset_id\": s[\"asset_id\"],\n                                  \"unit\": np.arange(len(u)), \"region\": u.region.values,\n                                  \"good\": u.ibl_quality_score.values == 1}))\n    allu = pd.concat(rows, ignore_index=True)\n    steps = [(\"all units\", allu)]\n    g = allu[allu.good]\n    steps.append((\"well-isolated\", g))\n    g = g[~g.region.isin([\"void\", \"root\"])]\n    steps.append((\"grey matter\", g))\n    n = g.groupby([\"region\", \"eid\"]).unit.transform(\"size\")\n    g = g[n >= MIN_UNITS_SESSION]\n    steps.append((f\">= {MIN_UNITS_SESSION} per session\", g))\n    ns = g.groupby(\"region\").eid.transform(\"nunique\")\n    g = g[ns >= MIN_SESSIONS]\n    steps.append((f\">= {MIN_SESSIONS} sessions\", g))\n    nr = g.groupby(\"region\").unit.transform(\"size\")\n    g = g[nr >= MIN_UNITS_REGION]\n    steps.append((f\">= {MIN_UNITS_REGION} per region\", g))\n    table = pd.DataFrame([{\"step\": k, \"sessions\": v.eid.nunique(), \"units\": len(v),\n                           \"regions\": v.region.nunique()} for k, v in steps])\n    return g.reset_index(drop=True), table\n\n\n# --- spikes -----------------------------------------------------------------------------------\n\ndef window_counts(st: np.ndarray, starts: np.ndarray, width: float) -> np.ndarray:\n    \"\"\"Spikes of a sorted spike train in [start, start + width) for each start (any shape).\"\"\"\n    s = np.asarray(starts, float)\n    out = np.searchsorted(st, s + width) - np.searchsorted(st, s)\n    out[~np.isfinite(s)] = 0\n    return out\n\n\ndef traj_starts(events: np.ndarray) -> np.ndarray:\n    \"\"\"Start of each overlapping trajectory bin, in the code's order (trials x 72).\"\"\"\n    j = np.arange(TRAJ_SHIFTS * TRAJ_NBINS)\n    return events[:, None] + (j // TRAJ_SHIFTS) * TRAJ_BIN + (j % TRAJ_SHIFTS) * TRAJ_STRIDE\n\n\ndef extract_session(job: tuple) -> dict:\n    \"\"\"Stream the spikes of the requested units of one session and reduce them to counts.\n\n    job = (asset_id, unit indices, which of them need trajectory bins, which need feedback PSTHs).\n    Returns the trials table with the analysis mask, counts in the analysis windows (trials x units),\n    counts in 0.2 s windows around feedback for the clock check (trials x units x offsets),\n    trajectory bins (trials x units x 72, uint8), and per unit the mean feedback PSTH on correct and\n    incorrect analysed trials (units x 2 x bins, spikes/s).\n    \"\"\"\n    asset_id, units, traj_units, psth_units = job\n    with open_nwb(asset_id) as f:\n        t = task_table(pd.DataFrame({k: _col(f[\"intervals/trials\"], k)\n                                     for k in f[\"intervals/trials\"] if k != \"id\"}))\n        mask, n_kept = analysis_mask(t)\n        t[\"analysed\"] = mask\n        u = f[\"units\"]\n        idx = u[\"spike_times_index\"][:]\n        start = np.r_[0, idx[:-1]]\n        st_all = u[\"spike_times\"]\n        order = np.argsort(start[units])\n        trains, unsorted = {}, 0\n        for i in np.asarray(units)[order]:\n            st = st_all[start[i]:idx[i]]\n            if np.any(np.diff(st) < 0):\n                unsorted += 1\n                st = np.sort(st)\n            trains[i] = st\n    counts = {}\n    for var, (col, a, b) in WINDOWS.items():\n        ev = t[col].values\n        counts[var] = np.stack([window_counts(trains[i], ev + a, b - a) for i in units], axis=1)\n    fb = t.feedback_time.values\n    clock = np.stack([window_counts(trains[i], fb[:, None] + CLOCK_OFFSETS[None, :], 0.2)\n                      for i in units], axis=1)\n    traj = None\n    if len(traj_units):\n        s = traj_starts(t.stim_on.values)\n        traj = np.stack([window_counts(trains[i], s, TRAJ_BIN) for i in traj_units], axis=1).astype(np.uint8)\n    psth = None\n    if len(psth_units):\n        edges = fb[:, None] + np.arange(0, PSTH_POST, PSTH_BIN)[None, :]\n        sel = {True: mask & t.correct.values, False: mask & ~t.correct.values}\n        psth = np.stack([np.stack([window_counts(trains[i], edges[sel[c]], PSTH_BIN).mean(0) / PSTH_BIN\n                                   for c in (True, False)]) for i in psth_units])\n    return {\"asset_id\": asset_id, \"trials\": t, \"n_kept\": n_kept, \"units\": np.asarray(units),\n            \"counts\": counts, \"clock\": clock, \"traj_units\": np.asarray(traj_units), \"traj\": traj,\n            \"psth_units\": np.asarray(psth_units), \"psth\": psth, \"unsorted_units\": unsorted,\n            \"n_spikes\": int(sum(len(v) for v in trains.values()))}\n\n\n# --- null sessions -----------------------------------------------------------------------------\n\nCONTRASTS = np.array([1.0, 0.25, 0.125, 0.0625, 0.0])\nCONTRAST_P = np.array([2, 2, 2, 2, 1]) / 9\n\n\ndef block_length(rng) -> int:\n    while True:\n        x = int(rng.exponential(60))\n        if 20 <= x <= 100:\n            return x\n\n\ndef pseudo_session(n: int, rng) -> pd.DataFrame:\n    \"\"\"Stimuli of one session drawn from the task's generative process (Methods).\"\"\"\n    first = np.r_[np.repeat(CONTRASTS[:4], 10), -np.repeat(CONTRASTS[:4], 10), np.zeros(10)]\n    first = rng.permutation(first)\n    side = np.sign(first)\n    side[side == 0] = rng.choice([-1, 1], size=(side == 0).sum())\n    contrast = np.abs(first)\n    p_left = np.full(90, 0.5)\n    pl = rng.choice([0.2, 0.8])\n    while len(p_left) < n:\n        p_left = np.r_[p_left, np.full(block_length(rng), pl)]\n        pl = 1 - pl\n    p_left = p_left[:n]\n    k = n - 90\n    if k > 0:\n        s2 = np.where(rng.random(k) < p_left[90:], -1, 1)\n        c2 = rng.choice(CONTRASTS, size=k, p=CONTRAST_P)\n        side = np.r_[side, s2]\n        contrast = np.r_[contrast, c2]\n    side, contrast = side[:n].astype(int), contrast[:n]\n    return pd.DataFrame({\"side\": side, \"contrast\": contrast, \"signed_contrast\": side * contrast,\n                         \"p_left\": p_left})\n\n\ndef _contrast_term(signed_contrast):\n    return np.tanh(5 * signed_contrast) / np.tanh(5)\n\n\ndef _prior(actions, alpha):\n    \"\"\"Action-kernel prior that the next stimulus is on the right (Methods' update rule).\"\"\"\n    pi = np.empty(len(actions))\n    p = 0.5\n    for i, a in enumerate(actions):\n        pi[i] = p\n        if a != 0:\n            p = (1 - alpha) * p + alpha * (a > 0)\n    return pi\n\n\ndef fit_action_kernel(t: pd.DataFrame) -> dict:\n    \"\"\"Learning rate and choice policy of the action-kernel model, by maximum likelihood.\"\"\"\n    best = None\n    resp = t.choice.values != 0\n    for alpha in (0.02, 0.05, 0.1, 0.15, 0.2, 0.3, 0.4, 0.5, 0.7):\n        pi = _prior(t.choice.values, alpha)\n        X = np.c_[_contrast_term(t.signed_contrast.values), pi - 0.5][resp]\n        y = (t.choice.values[resp] > 0).astype(int)\n        m = LogisticRegression(C=1e4, max_iter=1000).fit(X, y)\n        p = np.clip(m.predict_proba(X)[:, 1], 1e-9, 1 - 1e-9)\n        ll = np.sum(y * np.log(p) + (1 - y) * np.log(1 - p))\n        if best is None or ll > best[\"ll\"]:\n            best = {\"alpha\": alpha, \"b0\": m.intercept_[0], \"b\": m.coef_[0].copy(), \"ll\": ll}\n    return best\n\n\ndef synthetic_session(model: dict, n: int, rng) -> pd.DataFrame:\n    \"\"\"Pseudo-session stimuli with choices simulated from the fitted action-kernel model.\"\"\"\n    ps = pseudo_session(n, rng)\n    p, choice = 0.5, np.empty(n, int)\n    x = _contrast_term(ps.signed_contrast.values)\n    for i in range(n):\n        z = model[\"b0\"] + model[\"b\"][0] * x[i] + model[\"b\"][1] * (p - 0.5)\n        a = 1 if rng.random() < 1 / (1 + np.exp(-z)) else -1\n        choice[i] = a\n        p = (1 - model[\"alpha\"]) * p + model[\"alpha\"] * (a > 0)\n    ps[\"choice\"] = choice\n    ps[\"correct\"] = choice == ps.side.values\n    return ps\n\n\n# --- decoding -------------------------------------------------------------------------------\n\ndef _logreg(C):\n    return LogisticRegression(C=C, l1_ratio=1.0, solver=\"liblinear\", tol=1e-3, max_iter=20000,\n                              class_weight=\"balanced\")\n\n\ndef balanced_accuracy(y, p) -> float:\n    return 0.5 * (np.mean(p[y == 1] == 1) + np.mean(p[y == 0] == 0))\n\n\ndef _folds(n, rng, y=None, k=N_FOLDS):\n    \"\"\"Interleaved random folds; redrawn until every training set holds both classes.\"\"\"\n    for _ in range(100):\n        f = rng.permutation(np.arange(n) % k)\n        if y is None or all(len(np.unique(y[f != i])) == 2 for i in range(k)):\n            return f\n    raise RuntimeError(\"could not draw folds with both classes in training\")\n\n\ndef _fit_predict(Xtr, ytr, Xte, C):\n    if len(np.unique(ytr)) < 2:\n        return np.full(len(Xte), ytr[0])\n    return _logreg(C).fit(Xtr, ytr).predict(Xte)\n\n\ndef _choose_C(X, y, rng):\n    inner = _folds(len(y), rng, y)\n    score = np.zeros(len(C_GRID))\n    for i in range(N_FOLDS):\n        tr, va = inner != i, inner == i\n        for k, C in enumerate(C_GRID):\n            score[k] += balanced_accuracy(y[va], _fit_predict(X[tr], y[tr], X[va], C))\n    return C_GRID[int(np.argmax(score))]\n\n\ndef decode(X: np.ndarray, y: np.ndarray, null_ys: list, seed: int) -> dict:\n    \"\"\"Nested cross-validated decoding of y, and of each null target with the outer folds' C.\"\"\"\n    rng = np.random.default_rng(seed)\n    X = np.asarray(X, float)\n    scores, null = [], np.zeros((N_RUNS, len(null_ys)))\n    for run in range(N_RUNS):\n        outer = _folds(len(y), rng, y)\n        pred = np.zeros(len(y))\n        chosen = []\n        for i in range(N_FOLDS):\n            tr, te = outer != i, outer == i\n            C = _choose_C(X[tr], y[tr], rng)\n            chosen.append(C)\n            pred[te] = _fit_predict(X[tr], y[tr], X[te], C)\n        scores.append(balanced_accuracy(y, pred))\n        for j, yn in enumerate(null_ys):\n            outer_n = _folds(len(yn), rng, yn)\n            pn = np.zeros(len(yn))\n            for i in range(N_FOLDS):\n                tr, te = outer_n != i, outer_n == i\n                pn[te] = _fit_predict(X[tr], yn[tr], X[te], chosen[i])\n            null[run, j] = balanced_accuracy(yn, pn)\n    score, null = float(np.mean(scores)), null.mean(0)\n    return {\"score\": score, \"null\": null, \"p\": (1 + np.sum(null >= score)) / (1 + len(null)),\n            \"corrected\": score - float(np.median(null)) if len(null) else np.nan}\n\n\ndef decode_nested_null(X, y, seed) -> float:\n    \"\"\"Balanced accuracy with the full nested search, for one target (a null target, say).\"\"\"\n    rng = np.random.default_rng(seed)\n    X = np.asarray(X, float)\n    outer = _folds(len(y), rng, y)\n    pred = np.zeros(len(y))\n    for i in range(N_FOLDS):\n        tr, te = outer != i, outer == i\n        pred[te] = _fit_predict(X[tr], y[tr], X[te], _choose_C(X[tr], y[tr], rng))\n    return balanced_accuracy(y, pred)\n\n\ndef decoding_targets(t: pd.DataFrame, var: str, sessions: list | None = None):\n    \"\"\"Analysed-trial rows used, the binary target, and the same target in each null session.\"\"\"\n    m = t.analysed.values\n    if var == \"stim\":\n        rows = m & (t.contrast.values > 0)\n        y = (t.side.values[rows] > 0).astype(int)\n        nulls = [(s.side.values[rows] > 0).astype(int) for s in sessions or []]\n    elif var == \"choice\":\n        rows = m\n        y = (t.choice.values[rows] > 0).astype(int)\n        nulls = [(s.choice.values[rows] > 0).astype(int) for s in sessions or []]\n    else:\n        rows = m\n        y = t.correct.values[rows].astype(int)\n        nulls = [s.correct.values[rows].astype(int) for s in sessions or []]\n    return rows, y, nulls\n\n\ndef decode_job(job: tuple) -> dict:\n    \"\"\"One region-session: decode stimulus, choice and feedback against their null sessions.\"\"\"\n    key, t, counts, seed = job\n    rng = np.random.default_rng(seed)\n    n = len(t)\n    model = fit_action_kernel(t[t.analysed])\n    pseudo = [pseudo_session(n, rng) for _ in range(N_NULL)]\n    synth = [synthetic_session(model, n, rng) for _ in range(N_NULL)]\n    out = {\"key\": key, \"alpha\": model[\"alpha\"]}\n    for k, var in enumerate((\"stim\", \"choice\", \"feedback\")):\n        rows, y, nulls = decoding_targets(t, var, pseudo if var == \"stim\" else synth)\n        nulls = [yn for yn in nulls if len(np.unique(yn)) == 2 and min(np.bincount(yn)) >= N_FOLDS]\n        res = decode(counts[var][rows], y, nulls, seed + k + 1)\n        out[var] = {\"n_trials\": int(rows.sum()), \"n_minor\": int(min(np.bincount(y, minlength=2))),\n                    \"n_null\": len(nulls), **res}\n    return out\n\n\ndef fisher_p(p) -> float:\n    p = np.asarray(p, float)\n    return float(stats.chi2.sf(-2 * np.sum(np.log(p)), 2 * len(p)))\n\n\ndef bh(p, q) -> np.ndarray:\n    \"\"\"Benjamini-Hochberg: which p-values are significant at false discovery rate q.\"\"\"\n    p = np.asarray(p, float)\n    order = np.argsort(p)\n    thresh = q * np.arange(1, len(p) + 1) / len(p)\n    passed = p[order] <= thresh\n    k = np.max(np.where(passed)[0]) + 1 if passed.any() else 0\n    sig = np.zeros(len(p), bool)\n    sig[order[:k]] = True\n    return sig\n\n\n# --- single cells -----------------------------------------------------------------------------\n\ndef ccmw_p(counts: np.ndarray, label: np.ndarray, strata: np.ndarray, blocks: np.ndarray,\n           n_shuf: int, rng) -> np.ndarray:\n    \"\"\"Condition-combined Mann-Whitney p-value per unit, permuting within individual blocks.\n\n    counts: trials x units; label: 1 (x), 0 (y) or -1 (left out); strata: condition per trial.\n    Follows Time_TwoNmannWhitneyUshuf and the stimulus, choice and feedback scripts of the code.\n    \"\"\"\n    n_units = counts.shape[1]\n    num = np.zeros((n_shuf + 1, n_units))\n    den = 0.0\n    for s in np.unique(strata[label >= 0]):\n        idx = np.where((strata == s) & (label >= 0))[0]\n        lab = label[idx]\n        nx, ny = int((lab == 1).sum()), int((lab == 0).sum())\n        if nx == 0 or ny == 0:\n            continue\n        ranks = stats.rankdata(counts[idx], axis=0)\n        b = blocks[idx]\n        shared = np.intersect1d(b[lab == 1], b[lab == 0])\n        sx = np.empty((n_shuf + 1, len(idx)))\n        sy = np.empty((n_shuf + 1, len(idx)))\n        sx[0] = sy[0] = lab\n        for tgt in (sx, sy):\n            tgt[1:] = lab\n            for blk in shared:\n                j = np.where(b == blk)[0]\n                tgt[1:, j] = rng.permuted(np.tile(lab[j], (n_shuf, 1)), axis=1)\n        ux = sx @ ranks - nx * (nx + 1) / 2\n        uy = (1 - sy) @ ranks - ny * (ny + 1) / 2\n        num += np.minimum(ux, uy)\n        den += nx * ny\n    if den == 0:\n        return np.full(n_units, np.nan)\n    cp = num / den\n    return np.array([stats.rankdata(cp[:, k])[0] / (1 + n_shuf) for k in range(n_units)])\n\n\ndef simple_mw_p(counts, label) -> np.ndarray:\n    x, y = counts[label == 1], counts[label == 0]\n    out = np.ones(counts.shape[1])\n    for k in range(counts.shape[1]):\n        if np.ptp(np.r_[x[:, k], y[:, k]]) > 0:\n            out[k] = stats.mannwhitneyu(x[:, k], y[:, k], alternative=\"two-sided\").pvalue\n    return out\n\n\ndef single_cell_design(t: pd.DataFrame, var: str, side=None, choice=None, p_left=None):\n    \"\"\"Label, strata and blocks of the code's test for stimulus side or choice.\n\n    Analysed trials of the biased blocks with a visible stimulus. Stimulus: label is left stimulus,\n    strata are block x choice. Choice: label is the code's choice 1 (here -1, clockwise), strata are\n    block x stimulus side. Other side, choice or p_left (a null session) can be passed in.\n    \"\"\"\n    side = t.side.values if side is None else side\n    choice = t.choice.values if choice is None else choice\n    p_left = t.p_left.values if p_left is None else p_left\n    use = t.analysed.values & (t.contrast.values > 0) & (p_left != 0.5)\n    if var == \"stim\":\n        label = np.where(use, (side < 0).astype(int), -1)\n        strata = np.where(p_left == 0.8, 0, 2) + (choice > 0)\n    else:\n        label = np.where(use, (choice < 0).astype(int), -1)\n        strata = np.where(p_left == 0.8, 0, 2) + (side > 0)\n    blocks = np.r_[0, np.cumsum(np.abs(np.diff(p_left)) > 0)]\n    return label, strata, blocks\n\n\ndef single_cell_job(job: tuple) -> dict:\n    \"\"\"Selectivity of each unit of one region-session to stimulus side and choice, with a null run.\"\"\"\n    key, t, counts, seed = job\n    rng = np.random.default_rng(seed)\n    model = fit_action_kernel(t[t.analysed])\n    ps = pseudo_session(len(t), rng)\n    syn = synthetic_session(model, len(t), rng)\n    out = {\"key\": key}\n    for var in (\"stim\", \"choice\"):\n        c = counts[var]\n        for name, kw in ((\"real\", {}),\n                         (\"null\", {\"side\": ps.side.values, \"p_left\": ps.p_left.values} if var == \"stim\"\n                          else {\"choice\": syn.choice.values})):\n            label, strata, blocks = single_cell_design(t, var, **kw)\n            p_cc = ccmw_p(c, label, strata, blocks, N_SHUF_CELL, rng)\n            p_mw = simple_mw_p(c[label >= 0], label[label >= 0])\n            out[f\"{var}_{name}\"] = (p_mw < ALPHA_MW) & (p_cc < ALPHA_CCMW)\n            out[f\"{var}_{name}_mw\"] = p_mw < ALPHA_MW\n            out[f\"{var}_{name}_cc\"] = p_cc < ALPHA_CCMW\n    return out\n\n\n# --- population trajectories ------------------------------------------------------------------\n\ndef trajectory(sessions: list, n_perm: int, rng) -> dict:\n    \"\"\"Stimulus trajectory distance of one region pooled over sessions, with its permutation null.\n\n    sessions: list of (traj bins trials x units x 72, side, p_left, choice) over analysed trials.\n    \"\"\"\n    sq = np.zeros((n_perm + 1, TRAJ_TIMES.size))\n    n_cells = 0\n    for bins, side, p_left, choice in sessions:\n        n, u, nt = bins.shape\n        X = bins.reshape(n, u * nt).astype(np.float32) / TRAJ_BIN\n        labels = np.empty((n_perm + 1, n), np.float32)\n        labels[0] = side < 0\n        groups = [np.where((p_left == pl) & (choice == c))[0] for pl in np.unique(p_left) for c in (-1, 1)]\n        for k in range(1, n_perm + 1):\n            lab = labels[0].copy()\n            for g in groups:\n                lab[g] = lab[rng.permutation(g)]\n            labels[k] = lab\n        nl = labels.sum(1, keepdims=True)\n        mean_l = (labels / nl) @ X\n        mean_r = ((1 - labels) / (n - nl)) @ X\n        d = (mean_l - mean_r).reshape(n_perm + 1, u, nt)\n        sq += np.sum(d.astype(np.float64) ** 2, axis=1)\n        n_cells += u\n    dist = np.sqrt(sq / n_cells)\n    M = dist - dist.min(1, keepdims=True)\n    amp = M.max(1) - M.min(1)\n    ps = np.mean(M >= M[0], axis=0)\n    ups = np.where(M[0] > 0.7 * M[0].max())[0]\n    sig_ups = ups[ps[ups] < 0.05]\n    return {\"n_cells\": n_cells, \"d\": M[0], \"amp\": float(amp[0]), \"p\": float(np.mean(amp >= amp[0])),\n            \"latency\": float(TRAJ_TIMES[sig_ups[0]]) if len(sig_ups) else np.nan,\n            \"latency_70\": float(TRAJ_TIMES[ups[0]]),\n            \"latency_70_bin_start\": float(traj_starts(np.zeros(1))[0, ups[0]])}\n\n\n# --- behaviour --------------------------------------------------------------------------------\n\ndef spectrum_peak(x: np.ndarray, dt: float, fmin=4.0, fmax=20.0, pad=4096):\n    \"\"\"Peak frequency and power of a detrended, Hann-windowed signal within [fmin, fmax].\"\"\"\n    x = np.asarray(x, float)\n    x = x - np.polyval(np.polyfit(np.arange(len(x)), x, 1), np.arange(len(x)))\n    p = np.abs(np.fft.rfft(x * np.hanning(len(x)), n=pad)) ** 2\n    f = np.fft.rfftfreq(pad, dt)\n    band = (f >= fmin) & (f <= fmax)\n    k = np.argmax(p[band])\n    return float(f[band][k]), p, f\n\n\ndef thread_limits():\n    \"\"\"One linear-algebra thread per process: many small fits run in parallel processes.\"\"\"\n    for v in (\"OMP_NUM_THREADS\", \"OPENBLAS_NUM_THREADS\", \"MKL_NUM_THREADS\"):\n        os.environ[v] = \"1\"\n"
}
```

```
File created successfully at: entries/000409-ibl-2025/bwm.py (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd entries/000409-ibl-2025 && cat > $TMPDIR/dev/t1.py <<'E'
import sys,time; sys.path.insert(0,'.')
import bwm, numpy as np, pandas as pd
bwm.thread_limits()
if __name__=='__main__':
    t=time.time(); A=bwm.list_assets(); print('assets',len(A),time.time()-t); print(A.kind.value_counts())
    pr=A[A.kind=='processed'].sort_values('path')
    s=bwm.scan_session(pr.asset_id.iloc[10]); print(s['info'], s['units'].region.value_counts().head())
    t0=bwm.task_table(s['trials']); m,n=bwm.analysis_mask(t0); print(len(t0),m.sum(),n)
    u=s['units']; good=np.where((u.ibl_quality_score==1)&(~u.region.isin(['void','root'])))[0]
    reg=u.region.values[good]; top=pd.Series(reg).value_counts().index[0]; sel=good[reg==top]
    print(top,len(sel))
    t=time.time(); e=bwm.extract_session((s['asset_id'], list(good), list(sel), list(sel))); print('extract',time.time()-t, e['n_spikes'], e['unsorted_units'], e['traj'].shape, e['psth'].shape)
    import pickle; pickle.dump((s,e,sel,good),open('/tmp/claude-1001/t1.pkl','wb'))
    cnt={k:v[:, np.isin(good,sel)] for k,v in e['counts'].items()}
    t=time.time(); r=bwm.decode_job(((top,'x'), e['trials'], cnt, 1)); print('decode',time.time()-t, {k:(v['score'],v['p'],v['corrected'],v['n_null']) for k,v in r.items() if isinstance(v,dict)}, r['alpha'])
    t=time.time(); sc=bwm.single_cell_job(((top,'x'), e['trials'], cnt, 2)); print('sc',time.time()-t, {k:int(v.sum()) for k,v in sc.items() if k!='key'})
    tt=e['trials']; a=tt.analysed.values
    t=time.time(); tr=bwm.trajectory([(e['traj'][a], tt.side.values[a], tt.p_left.values[a], tt.choice.values[a])], 1000, np.random.default_rng(0)); print('traj',time.time()-t, {k:v for k,v in tr.items() if k!='d'})
E
$TMPDIR/explore/bin/python $TMPDIR/dev/t1.py
```

```
assets 2048 1.5213663578033447
kind
raw                 459
processed           459
VideoLeftCamera     437
VideoRightCamera    433
VideoBodyCamera     260
Name: count, dtype: int64
{'subject_id': 'CSH_ZAD_022', 'sex': 'M', 'date_of_birth': '2019-11-12T00:00:00-05:00', 'weight': '0.03209000000000001 kg', 'species': 'Mus musculus', 'lab': 'zadorlab', 'institution': 'Cold Spring Harbor Laboratory', 'protocol': '_iblrig_tasks_ephysChoiceWorld6.4.0', 'session_id': '6a601cc5-7b79-4c75-b0e8-552246532f82', 'session_start': '2020-05-25T14:00:55-04:00', 'revision': '2025-05-06', 'processing': ['passive_protocol', 'wheel']} region
root    597
CS      355
PAG     236
CA1     213
APN     181
Name: count, dtype: int64
827 390 827
CS 46
extract 14.936729669570923 16029956 0 (827, 46, 72) (46, 2, 200)
decode 6.027280569076538 {'stim': (0.6372297866367209, np.float64(0.009900990099009901), 0.10268630831661452, 100), 'choice': (0.7459272048789998, np.float64(0.009900990099009901), 0.22043960627185166, 100), 'feedback': (0.9347613390174017, np.float64(0.009900990099009901), 0.42852127124080774, 100)} 0.2
sc 0.3537750244140625 {'stim_real': 1, 'stim_real_mw': 2, 'stim_real_cc': 5, 'stim_null': 0, 'stim_null_mw': 0, 'stim_null_cc': 5, 'choice_real': 0, 'choice_real_mw': 2, 'choice_real_cc': 6, 'choice_null': 0, 'choice_null_mw': 1, 'choice_null_cc': 0}
[... 1 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && explore/bin/python -c "
import pandas as pd
ri=pd.read_csv('paper-brain-wide-map/brainwidemap/meta/region_info.csv')
r=['VISp','LGd','LP','VISpm','VISam','GRN','IRN','ACAv','CL','HATA','LDT','PA','PVT','TR']
print(ri[ri.Beryl.isin(r)][['Beryl','# good neurons','stim_man','choice_man','fback_man','stim_man_sig','choice_man_sig']])
can=ri[ri.canonical]
print((can['stim_man']*can['# good neurons']).sum()/can['# good neurons'].sum(), (can['choice_man']*can['# good neurons']).sum()/can['# good neurons'].sum(), can.stim_man.max(), can.choice_man.max())
"
```

```
Beryl  # good neurons  stim_man  ...  fback_man  stim_man_sig  choice_man_sig
18   VISam             374      0.02  ...       0.04           1.0             1.0
20    VISp             880      0.03  ...       0.05           1.0             1.0
22   VISpm             241      0.02  ...       0.03           1.0             0.0
26    ACAv             195      0.00  ...       0.04           0.0             0.0
53      TR              37      0.00  ...       0.00           0.0             0.0
67    HATA              59      0.00  ...       0.00           0.0             0.0
75      PA             113      0.00  ...       0.00           0.0             0.0
108    LGd             557      0.03  ...       0.06           1.0             0.0
109     LP            1812      0.01  ...       0.08           1.0             1.0
124    PVT              84      0.00  ...       0.12           0.0             0.0
131     CL              38      0.04  ...       0.43           0.0             1.0
220    LDT              51      0.00  ...       0.20           0.0             0.0
237    GRN             560      0.01  ...       0.39           1.0             1.0
240    IRN             744      0.00  ...       0.32           0.0             1.0

[14 rows x 7 columns]
0.0040781674487527795 0.043813132872314156 0.08 0.3
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && explore/bin/python - <<'E'
import pickle,os,collections
res=pickle.load(open(os.environ['TMPDIR']+'/scanall.pkl','rb'))
seen=set()
for r in res:
    for k,v in r['dev'].items():
        m=v[:40]
        if m not in seen: seen.add(m); print(k, v)
E
```

```
Probe00 A PRB_1_4_0480_1 probe. Additional metadata: {"model_name": "PRB_1_4_0480_1", "manufacturer": "imec", "port": "2", "slot": "2", "part_number": "PRB_1_4_0480_1"}
Probe00 A PRB_1_4_0480_1_C probe. Additional metadata: {"model_name": "PRB_1_4_0480_1_C", "manufacturer": "imec", "port": "3", "slot": "2", "part_number": "PRB_1_4_0480_1_C"}
Probe00 A NP1010 probe. Additional metadata: {"model_name": "NP1010", "manufacturer": "imec"}
Probe00a A NP2010 probe. Additional metadata: {"model_name": "NP2010", "manufacturer": "imec", "port": "1", "slot": "3", "part_number": "NP2010"}
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && explore/bin/python - <<'E'
import json,os,h5py,remfile,requests
a=json.load(open(os.environ['TMPDIR']+'/a409.json'))
raw=[x for x in a if 'desc-raw' in x['path']][0]
url=requests.head(f"https://api.dandiarchive.org/api/assets/{raw['asset_id']}/download/",allow_redirects=True).url.split('?')[0]
f=h5py.File(remfile.File(url),'r')
def walk(g,pre='',d=0):
    for k,v in g.items():
        if k=='specifications': continue
        if isinstance(v,h5py.Dataset): 
            if d<3: print(pre+k, v.shape)
        else:
            print(pre+k+'/', v.attrs.get('neurodata_type',''), str(v.attrs.get('description',''))[:100]); 
            if d<2: walk(v,pre+k+'/',d+1)
walk(f)
E
```

```
acquisition/  
acquisition/ElectricalSeriesProbe01AP/ ElectricalSeries Acquisition traces for the ElectricalSeriesProbe01AP.
acquisition/ElectricalSeriesProbe01AP/data (121012721, 384)
acquisition/ElectricalSeriesProbe01AP/electrodes (384,)
acquisition/ElectricalSeriesProbe01AP/timestamps (121012721,)
acquisition/ElectricalSeriesProbe01LF/ ElectricalSeries Acquisition traces for the ElectricalSeriesProbe01LF.
acquisition/ElectricalSeriesProbe01LF/data (10084394, 384)
acquisition/ElectricalSeriesProbe01LF/electrodes (384,)
acquisition/ElectricalSeriesProbe01LF/timestamps (10084394,)
acquisition/EventsAudio/ LabeledEvents Auditory stimulus presentation events. Marks timing of audio stimulus delivery for auditory tasks or
acquisition/EventsAudio/data (1388,)
acquisition/EventsAudio/timestamps (1388,)
acquisition/EventsBodyCamera/ LabeledEvents Video frame acquisition times for the body camera. Each event marks when a video frame was captured 
acquisition/EventsBodyCamera/data (242050,)
acquisition/EventsBodyCamera/timestamps (242050,)
acquisition/EventsFrame2ttl/ LabeledEvents Monitor refresh events detected by photodiode for visual stimulus timing. The Frame2TTL device uses 
acquisition/EventsFrame2ttl/data (11660,)
acquisition/EventsFrame2ttl/timestamps (11660,)
acquisition/EventsImecSync/ LabeledEvents Multi-probe synchronization signal (1 Hz square wave). This signal is simultaneously recorded on NID
acquisition/EventsImecSync/data (8067,)
[... 80 more lines not kept]
```

**Agent**

Now the claims file, written before running any claim analysis.

**Agent calls Write**

```json
{
 "file_path": "claims/000409/10.1038-s41586-025-09235-0.yaml",
 "content": "# Claims for International Brain Laboratory et al. (2025), A brain-wide map of neural activity\n# during complex behaviour, Nature 645, 177-191, on dandiset 000409.\n# Source: the full text of the version of record (open access, CC BY 4.0), read from the Results,\n# figure legends and Methods. Supplementary information and Extended Data figures were not read\n# beyond their legends.\n#\n# When these criteria were written the author had seen the data check only: the file list, the\n# metadata, and a scan of every processed file (subjects, labs, probe models, trial counts per\n# session, units and their quality scores and regions, the inclusion counts of the canonical set,\n# the processing modules and passive protocols). In checking the trials table the author also saw\n# that 22.75% of first movement times are below 80 ms (claim behav-early-movements), and the mapping\n# of choice to reward. The author had read the paper's per-region table region_info.csv in the\n# paper's repository (commit 118fc36), including its single-cell fractions for the regions the\n# neural claims test, and its results tables meta/Results/*.pkl. No neural analysis had been run on\n# the data, beyond timing one session to plan the run.\n#\n# Tolerances. Counts of released records (sessions, mice, labs, probes, units, regions) have a\n# tolerance of 0: the paper states them for the released data, so any difference is a difference in\n# what was released. Other numbers use the paper's stated spread where it gives one, otherwise 10%.\n#\n# The neural analyses cannot run over all 454 sessions and 201 regions within the time limit, so\n# they test a set of regions fixed here: the paper's three example regions VISp (Fig. 4i), GRN\n# (Fig. 5i) and IRN (Fig. 6i), and seven regions drawn at random (numpy default_rng(409)) from the\n# canonical regions recorded in at most 12 sessions, leaving out the visual regions used for\n# latencies. Each tested region uses all its canonical sessions. Method choices fixed here: one run\n# of the nested cross-validation (paper 10), 100 null sessions per region-session (paper 200), each\n# null decoded with the C chosen for the real labels in each outer fold; per-session p-values are\n# (1 + number of null scores at least the real score) / (1 + number of nulls), combined over sessions\n# with Fisher's method, and the Benjamini-Hochberg correction at q = 0.01 is applied over the tested\n# regions of each variable.\nschema_version: 1\ndandiset: \"000409\"\npaper: doi:10.1038/s41586-025-09235-0\nclaims:\n- id: dataset-sessions-mice-labs\n  statement: The data come from 459 sessions of 139 mice recorded in 12 laboratories.\n  source: Abstract; Methods, Sessions and insertions\n  expected:\n  - quantity: sessions\n    value: 459\n    tolerance: 0\n  - quantity: mice\n    value: 139\n    tolerance: 0\n  - quantity: laboratories\n    value: 12\n    tolerance: 0\n- id: dataset-probes-units\n  statement: 699 Neuropixels insertions yielded 621,733 units, an average of 889 per probe.\n  source: Abstract; Results, Recordings; Methods\n  expected:\n  - quantity: probe insertions\n    value: 699\n    tolerance: 0\n  - quantity: units\n    value: 621733\n    tolerance: 0\n  - quantity: units per probe\n    value: 889\n    tolerance: 1\n- id: well-isolated-neurons\n  statement: Stringent quality metrics identified 75,708 well-isolated neurons, an average of 108 per\n    probe.\n  source: Results, Recordings; Methods, Neurons and brain regions\n  expected:\n  - quantity: well-isolated neurons\n    value: 75708\n    tolerance: 0\n  - quantity: well-isolated neurons per probe\n    value: 108\n    tolerance: 1\n  criterion: A unit is well-isolated when its ibl_quality_score is 1 (all three metrics passed). The\n    data check also tests that the score equals the fraction of the three metrics (median amplitude\n    above 50 uV, noise cutoff below 20, sliding refractory period pass) that each unit passes.\n- id: canonical-regions\n  statement: The main analyses use a canonical dataset of 201 regions with at least 2 sessions of 5\n    well-isolated neurons and at least 20 neurons in total, 62,857 neurons.\n  source: Results, Neural analyses; Methods, Neurons and brain regions\n  expected:\n  - quantity: canonical regions\n    value: 201\n    tolerance: 0\n  - quantity: neurons in canonical regions\n    value: 62857\n    tolerance: 0\n  criterion: Regions are Beryl regions of each unit's peak channel, void and root left out, with the\n    inclusion steps applied in the order of the code's meta/inclusion_info.py. The count at each step\n    is compared with that file's table.\n- id: brain-areas-279\n  statement: The probes covered 279 brain areas.\n  source: Abstract\n  expected:\n    quantity: Beryl regions other than void and root holding at least one unit\n    value: 279\n    tolerance: 0\n- id: mice-sex\n  statement: The 139 mice were 94 male and 45 female.\n  source: Results, Behavioural task; Methods, Animals\n  expected:\n  - quantity: male mice\n    value: 94\n    tolerance: 0\n  - quantity: female mice\n    value: 45\n    tolerance: 0\n- id: mice-age-weight\n  statement: On the day of recording the mice were aged 13 to 178 weeks (mean 44.96, median 27.0)\n    and weighed 16.1 to 35.7 g (mean 23.9, median 23.84).\n  source: Methods, Animals\n  expected:\n  - quantity: minimum age\n    value: 13\n    tolerance: 1.3\n    unit: weeks\n  - quantity: maximum age\n    value: 178\n    tolerance: 17.8\n    unit: weeks\n  - quantity: mean age\n    value: 44.96\n    tolerance: 4.5\n    unit: weeks\n  - quantity: median age\n    value: 27.0\n    tolerance: 2.7\n    unit: weeks\n  - quantity: minimum weight\n    value: 16.1\n    tolerance: 1.61\n    unit: g\n  - quantity: maximum weight\n    value: 35.7\n    tolerance: 3.57\n    unit: g\n  - quantity: mean weight\n    value: 23.9\n    tolerance: 2.39\n    unit: g\n  - quantity: median weight\n    value: 23.84\n    tolerance: 2.38\n    unit: g\n  criterion: Age is session start minus date of birth; weight is the subject weight in each file.\n    Readings, one value per mouse, (a) at its first recording session, (b) at its last, or (c) one\n    value per session. Age and weight are judged separately; each holds when its four values are\n    within tolerance under one reading. Reproduced when both hold, partially reproduced when one\n    does.\n- id: probe-versions\n  statement: The insertions used Neuropixels 1.0 probes of versions 3A (109) and 3B2 (586), and\n    Neuropixels 2.4 probes (4).\n  source: Methods, Materials and apparatus\n  expected:\n  - quantity: 3A insertions\n    value: 109\n    tolerance: 0\n  - quantity: 3B2 insertions\n    value: 586\n    tolerance: 0\n  - quantity: 2.4 insertions\n    value: 4\n    tolerance: 0\n  criterion: The files name probes by imec model; NP1010 (no PXI port or slot, as 3A probes were\n    recorded with an FPGA) is read as 3A, PRB_1_4_0480_1 with or without the _C suffix as 3B2, and\n    NP2010 as the 2.x probes. The counts are of insertions over sessions.\n- id: trials-per-session\n  statement: Recorded sessions lasted on average 645 trials (median 602, range 401 to 1,525).\n  source: Results, Behavioural task\n  expected:\n  - quantity: mean trials per session\n    value: 645\n    tolerance: 64.5\n  - quantity: median trials per session\n    value: 602\n    tolerance: 60.2\n  - quantity: fewest trials\n    value: 401\n    tolerance: 40.1\n  - quantity: most trials\n    value: 1525\n    tolerance: 152.5\n- id: rf-mapping\n  statement: Receptive-field mapping after the task (504 of 699 insertions) found a relatively small\n    fraction of cells with significant receptive fields, with large fractions in VISp, VISl and SCs.\n  source: Results, Representation of visual stimulus; Methods, RF mapping; Supplementary Fig. 5\n- id: behav-performance\n  statement: After training, mice made correct choices on 81.4 +/- 0.4% (mean +/- s.d.) of trials.\n  source: Results, Behavioural task\n  expected:\n    quantity: percent correct\n    value: 81.4\n    tolerance: 0.4\n    unit: '%'\n  criterion: The tolerance is the paper's stated spread. Readings (a) mean over mice of each mouse's\n    percent correct over all its trials; (b) the same over analysed trials (first movement time 0.08\n    to 2 s and complete events); (c) mean over sessions of all trials; (d) all trials pooled.\n    Reproduced when one reading is within tolerance. The spread is reported as s.d. and s.e.m.\n- id: behav-zero-contrast\n  statement: On 0% contrast trials mice were rewarded on 58.7 +/- 0.4% (mean +/- s.e.m. across mice)\n    of trials, better than chance (t138 = 20.18, P = 5.2e-43).\n  source: Results, Behavioural task; Fig. 1d legend\n  expected:\n  - quantity: percent correct at 0% contrast, mean over mice\n    value: 58.7\n    tolerance: 0.4\n    unit: '%'\n  - quantity: t statistic against 50%\n    value: 20.18\n    tolerance: 2.02\n  criterion: One value per mouse, pooled over its sessions; one-sample t-test against 50% with 138\n    degrees of freedom. Readings (a) all 0% contrast trials, (b) analysed 0% contrast trials.\n    Reproduced when both values are within tolerance under one reading.\n- id: behav-early-movements\n  statement: 22.8% of first wheel-movement times occurred under 80 ms after stimulus onset.\n  source: Fig. 1c legend\n  expected:\n    quantity: percent of first movement times below 80 ms\n    value: 22.8\n    tolerance: 2.28\n    unit: '%'\n  criterion: First movement time is the first movement minus stimulus onset. Readings, (a) over all\n    trials of the 459 sessions, a trial without a first movement counting as not early; (b) over\n    trials with both times; (c) mean over sessions of (b).\n- id: fig1d-contrast\n  statement: Mice performed better and faster on trials with high visual contrast.\n  source: Fig. 1d; Results, Behavioural task\n  criterion: Per mouse, pooled over sessions, the percent correct and the median first movement\n    time at each of the five contrasts, over trials with a response. Reproduced when, across mice,\n    percent correct at 100% is higher than at 0% and median first movement time at 100% is shorter\n    than at 0% (Wilcoxon signed-rank p < 0.05 each), and the median over mice of percent correct\n    rises with contrast at every step; partially reproduced when only one of the two measures holds.\n- id: fig1ef-end-of-session\n  statement: Towards the end of the sessions, performance decreased and first wheel-movement times\n    increased.\n  source: Fig. 1e,f; Results, Behavioural task\n  criterion: Per mouse, pooled over sessions, the percent correct on non-zero contrast trials and\n    the median first movement time over the last 50 trials of each session against trials 51 to 300\n    before the end. Reproduced when the end has lower percent correct and longer first movement\n    times (Wilcoxon signed-rank across mice p < 0.05 each); partially reproduced when one holds.\n- id: fig1g-block-switch\n  statement: After a block switch, mice took around 5 to 10 trials to adjust their behaviour, as shown\n    by the fraction of correct choices on 0% contrast trials after the switch.\n  source: Fig. 1g; Results, Behavioural task\n  criterion: Switches between biased blocks; on 0% contrast trials at positions 1 to 40 after the\n    switch, the fraction of choices matching the stimulus side (which follows the new block), per\n    position pooled over each mouse's sessions and averaged over mice. Fit p(n) = a - b exp(-(n - 1) /\n    tau). Readings (a) tau, (b) the trials to cover 90% of the change, 1 + tau ln 10. Reproduced when\n    one reading lies within 4.5 to 11 trials (5 to 10 widened by 10%).\n- id: fig1h-block-bias\n  statement: For all contrast values mice chose the side of the block's likely stimulus more often,\n    responding right more often in right blocks than in left blocks.\n  source: Fig. 1h; Results, Behavioural task\n  criterion: Per mouse, the fraction of right choices at each of the nine signed contrasts in right\n    blocks (p_left 0.2) and left blocks (p_left 0.8), over trials with a response. Reproduced when\n    the right-block fraction is higher at all nine contrasts (median difference above 0 and Wilcoxon\n    signed-rank p < 0.05 across mice); partially reproduced at 6 to 8 contrasts.\n- id: dec-stim-restricted\n  statement: The visual stimulus side, decoded from the first 100 ms after stimulus onset, was\n    represented in a narrower set of regions than choice or feedback, with strong signatures in\n    visual cortex such as VISp.\n  source: Fig. 4a,i; Results, Representation of visual stimulus; Discussion\n  criterion: Decoding of stimulus side on non-zero contrast analysed trials, null from\n    pseudo-sessions, over the tested regions (see the opening comment). Reproduced when VISp is\n    significant and fewer tested regions are significant for stimulus than for choice and than for\n    feedback; partially reproduced when only one of the two holds. The agreement of each region's\n    significance with the paper's table region_info.csv is reported, and does not decide.\n- id: dec-choice-widespread\n  statement: Choice, decoded from the 100 ms before the first wheel movement, was represented in a\n    larger number of regions than the visual stimulus, with strong effects in hindbrain regions such\n    as GRN.\n  source: Fig. 5a,i; Results, Representation of choice\n  criterion: Decoding of choice on analysed trials, null from synthetic sessions of an action-kernel\n    model fitted per session, over the tested regions. Reproduced when GRN is significant and more\n    tested regions are significant for choice than for stimulus; partially reproduced when only one\n    holds.\n- id: dec-feedback-nearly-all\n  statement: Whether the trial was correct could be decoded from the 200 ms after feedback onset in\n    nearly all recorded regions, almost perfectly in many.\n  source: Fig. 6a,i; Results, Representation of feedback\n  criterion: Decoding of feedback on analysed trials, null from synthetic sessions, over the 10\n    tested regions. Reproduced when at least 9 tested regions, including IRN, are significant;\n    partially reproduced for 6 to 8; not reproduced below 6. The number of region-sessions with a\n    balanced accuracy above 0.9 is reported.\n- id: sc-stim-fraction\n  statement: Single-cell tests controlling for choice and block found few stimulus-selective neurons\n    (0.5% of all neurons); even in the regions with the largest fractions, such as visual cortex,\n    the fraction did not exceed about 10%.\n  source: Fig. 4b; Results, Representation of visual stimulus\n  criterion: Over the neurons of the tested and latency regions (14 regions). Reproduced when no\n    region exceeds 11% and at least 10 of the 14 regional fractions are within 0.02 of the paper's\n    region_info.csv value. The 0.5% of all neurons cannot be tested on a set of regions chosen this\n    way, and the pooled fraction is reported. The paper's false-positive rate for the selection,\n    0.001 x 0.05 = 5e-5, is checked with a null run (pseudo-session stimulus sides and blocks); if\n    the 95% interval of the null fraction excludes 1/3 to 3 times 5e-5, the claim is blocked as\n    methods_underspecified.\n- id: sc-choice-fraction\n  statement: More neurons responded to choice than to the visual stimulus (4% of all neurons),\n    with the largest fractions in hindbrain, midbrain and thalamic regions.\n  source: Fig. 5b; Results, Representation of choice\n  depends_on:\n  - sc-stim-fraction\n  criterion: Over the same 14 regions. Reproduced when the pooled choice fraction is higher than the\n    pooled stimulus fraction (binomial test on the neurons selective for exactly one, p < 0.05) and\n    the regional choice fractions correlate with region_info.csv (Spearman, p < 0.05). The same\n    false-positive check applies, with synthetic choices.\n- id: traj-latency-visual\n  statement: The latency of the stimulus trajectory separation ordered the visual regions as LGd <\n    VISp, which is about equal to LP, < VISpm < VISam, at about 34, 42, 42, 57 and 78 ms.\n  source: Fig. 4d,l,m; Results, Representation of visual stimulus\n  expected:\n  - quantity: LGd latency\n    value: 34\n    tolerance: 3.4\n    unit: ms\n  - quantity: VISp latency\n    value: 42\n    tolerance: 4.2\n    unit: ms\n  - quantity: LP latency\n    value: 42\n    tolerance: 4.2\n    unit: ms\n  - quantity: VISpm latency\n    value: 57\n    tolerance: 5.7\n    unit: ms\n  - quantity: VISam latency\n    value: 78\n    tolerance: 7.8\n    unit: ms\n  criterion: Trajectories over all canonical sessions of each region, 0 to 150 ms after stimulus\n    onset. Latency as the Methods define it, the first time the distance reaches 70% of its range;\n    the code's added condition that this time be significant point-wise is a variant. Reproduced\n    when the order holds (LGd below both VISp and LP, both below VISpm, VISpm below VISam, and VISp\n    and LP within 10 ms of each other) and all five values are within tolerance; partially\n    reproduced when only one of the two holds.\n- id: traj-latency-late\n  statement: The early visual wave was followed by later stimulus encoding in the MRN, SCm, PRNr, IRN\n    and GRN, with latencies of about 100 to 120 ms.\n  source: Fig. 4d,l,m; Results, Representation of visual stimulus\n  expected:\n  - quantity: IRN latency\n    value: 110\n    tolerance: 22\n    unit: ms\n  - quantity: GRN latency\n    value: 110\n    tolerance: 22\n    unit: ms\n  criterion: Only IRN and GRN are loaded (MRN, SCm and PRNr would add many sessions). The reported\n    range 100 to 120 ms widened by 10% of each bound is 90 to 132 ms, written as 110 +/- 22 (lower\n    bound 88). Reproduced when both latencies (Methods' definition) are in 90 to 132 ms and both\n    regions' distances are significant; partially reproduced for one region.\n- id: traj-stim-regions\n  statement: The stimulus trajectory distance was significant in 104 regions.\n  source: Results, Representation of visual stimulus; Fig. 4c\n  expected:\n    quantity: regions with significant stimulus trajectory distance\n    value: 104\n    tolerance: 10.4\n- id: fback-oscillation-licking\n  statement: During reward delivery, activity showed coherent oscillations of about 10 Hz that were\n    missing after negative feedback and were closely related to licking.\n  source: Results, Representation of feedback; Fig. 6j-l; Extended Data Fig. 12\n  criterion: In IRN, the paper's example region, the session mean PSTH over units (5 ms bins, 0 to 1\n    s after feedback) on correct and on incorrect trials, and the lick PSTH of the same sessions.\n    Reproduced when (i) the median over sessions of the peak frequency (4 to 20 Hz) of the correct\n    PSTH is within 9 to 11 Hz, (ii) power within 1 Hz of each session's correct peak is higher on\n    correct than incorrect trials (Wilcoxon signed-rank p < 0.05), and (iii) the median lick PSTH\n    peak is within 1 Hz of the neural one. Partially reproduced when (ii) and (iii) hold and (i)\n    does not.\n- id: wheel-speed-decoding\n  statement: Wheel speed was decodable from 163 of the 201 regions.\n  source: Results, Representation of wheel movement; Fig. 7a\n  expected:\n    quantity: regions with significant wheel-speed decoding\n    value: 163\n    tolerance: 16.3\n- id: encoding-feedback-largest\n  statement: In the encoding model the kernel for correct feedback explained the most variance of all\n    kernels (mean delta R2 of 8.6e-3 over all neurons).\n  source: Results, Representation of feedback; Extended Data Fig. 13\n  expected:\n    quantity: mean delta R2 of the correct feedback kernel\n    value: 0.0086\n    tolerance: 0.00086\n- id: video-correlates\n  statement: More than half of the neurons in most brain regions were significantly correlated with\n    at least one behavioural variable from video (nose, paw, pupil, tongue).\n  source: Results, Representation of wheel movement; Extended Data Fig. 15\n- id: granger-interactions\n  statement: High Granger interaction scores were found for region pairs from all major brain\n    regions, weakly correlated with anatomical distance and mostly bidirectional.\n  source: Results, Neural analyses; Extended Data Fig. 4\n"
}
```

```
File created successfully at: claims/000409/10.1038-s41586-025-09235-0.yaml (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd claims/000409 && python - <<'E'
p='10.1038-s41586-025-09235-0.yaml'
s=open(p).read()
s=s.replace("""    value: 110
    tolerance: 22
    unit: ms""","""    value: 111
    tolerance: 21
    unit: ms""")
s=s.replace("""    range 100 to 120 ms widened by 10% of each bound is 90 to 132 ms, written as 110 +/- 22 (lower
    bound 88). Reproduced""","""    range 100 to 120 ms widened by 10% of each bound is 90 to 132 ms, written as 111 +/- 21.
    Reproduced""")
s=s.replace("""  depends_on:
  - sc-stim-fraction
  criterion: Over the same 14""","""  criterion: Over the same 14""")
open(p,'w').write(s)
import yaml; d=yaml.safe_load(open(p)); print(len(d['claims']))
E
```

```
30
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "entries/000409-ibl-2025/bwm.py",
 "old_string": "def fisher_p(p) -> float:",
 "new_string": "def nested_null_job(job: tuple) -> dict:\n    \"\"\"For one region-session, null scores with the full nested search and with the reused C.\"\"\"\n    key, t, counts, seed, n_null = job\n    rng = np.random.default_rng(seed)\n    model = fit_action_kernel(t[t.analysed])\n    pseudo = [pseudo_session(len(t), rng) for _ in range(n_null)]\n    synth = [synthetic_session(model, len(t), rng) for _ in range(n_null)]\n    out = {\"key\": key}\n    for k, var in enumerate((\"stim\", \"choice\", \"feedback\")):\n        rows, y, nulls = decoding_targets(t, var, pseudo if var == \"stim\" else synth)\n        nulls = [yn for yn in nulls if len(np.unique(yn)) == 2 and min(np.bincount(yn)) >= N_FOLDS]\n        X = counts[var][rows]\n        out[var] = {\"nested\": np.array([decode_nested_null(X, yn, seed + 10 * k + j) for j, yn in enumerate(nulls)]),\n                    \"reused\": decode(X, y, nulls, seed + k)[\"null\"]}\n    return out\n\n\ndef clock_job(job: tuple) -> dict:\n    \"\"\"Feedback decoded from 0.2 s windows at offsets around feedback, and with labels one trial off.\"\"\"\n    key, t, clock, seed = job\n    rng = np.random.default_rng(seed)\n    m = t.analysed.values\n    y = t.correct.values[m].astype(int)\n    X = clock[m].astype(float)\n    if min(np.bincount(y, minlength=2)) < N_FOLDS or X.shape[1] == 0:\n        return {\"key\": key, \"acc\": np.full(len(CLOCK_OFFSETS), np.nan), \"shifted\": np.nan}\n\n    def cv(Xk, yk):\n        f = _folds(len(yk), rng, yk)\n        pred = np.zeros(len(yk))\n        for i in range(N_FOLDS):\n            pred[f == i] = _fit_predict(Xk[f != i], yk[f != i], Xk[f == i], 1.0)\n        return balanced_accuracy(yk, pred)\n\n    acc = np.array([cv(X[:, :, j], y) for j in range(len(CLOCK_OFFSETS))])\n    j0 = int(np.where(CLOCK_OFFSETS == 0)[0][0])\n    shifted = cv(X[1:, :, j0], y[:-1])\n    return {\"key\": key, \"acc\": acc, \"shifted\": shifted}\n\n\ndef fisher_p(p) -> float:"
}
```

```
The file entries/000409-ibl-2025/bwm.py has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd entries/000409-ibl-2025 && cat > $TMPDIR/dev/t2.py <<'E'
import sys,time,pickle; sys.path.insert(0,'.')
import bwm, numpy as np
s,e,sel,good=pickle.load(open('/tmp/claude-1001/t1.pkl','rb'))
t=time.time(); r=bwm.clock_job(('x',e['trials'],e['clock'],1)); print(time.time()-t, r)
cnt={k:v[:, np.isin(good,sel)] for k,v in e['counts'].items()}
t=time.time(); r=bwm.nested_null_job(('x',e['trials'],cnt,3,5)); print(time.time()-t, {k:(v['nested'],v['reused']) for k,v in r.items() if k!='key'})
E
OPENBLAS_NUM_THREADS=1 $TMPDIR/explore/bin/python $TMPDIR/dev/t2.py
```

```
2.425022840499878 {'key': 'x', 'acc': array([0.51516528, 0.50370396, 0.5323922 , 0.52592774, 0.56321196,
       0.98780488, 1.        , 0.97417709]), 'shifted': np.float64(0.5852607232968882)}
9.120154619216919 {'stim': (array([0.51212009, 0.54044519, 0.54778192, 0.5742641 , 0.52713782]), array([0.53674691, 0.52917917, 0.49585406, 0.54291045, 0.51649953])), 'choice': (array([0.53394858, 0.53863349, 0.50124788, 0.53274937, 0.47665219]), array([0.59406724, 0.58699769, 0.51887744, 0.57346907, 0.45807251])), 'feedback': (array([0.46434149, 0.54700855, 0.61538462, 0.4724893 , 0.44001613]), array([0.56715252, 0.44301994, 0.53180473, 0.48027418, 0.50592395]))}
```

**Agent**

Helpers work on one session (the clock check shows feedback decoding jump from 0.5 to 0.99 at the feedback window). Now writing the notebook.

**Agent calls Write**

```json
{
 "file_path": "/tmp/claude-1001/dev/make_nb.py",
 "content": "import nbformat as nbf\n\ncells = []\n\n\ndef md(s):\n    cells.append(nbf.v4.new_markdown_cell(s.strip(\"\\n\")))\n\n\ndef code(s, tags=None):\n    c = nbf.v4.new_code_cell(s.strip(\"\\n\"))\n    if tags:\n        c.metadata[\"tags\"] = tags\n    cells.append(c)\n\n\nmd(r\"\"\"\n# Reproducing the IBL brain-wide map (2025) from dandiset 000409\n\n**Paper.** International Brain Laboratory, Angelaki D, Benson B, et al. (2025). A brain-wide map of\nneural activity during complex behaviour. *Nature* 645, 177-191.\n[doi:10.1038/s41586-025-09235-0](https://doi.org/10.1038/s41586-025-09235-0). This attempt used the\nfull text of the version of record, which is open access (CC BY 4.0).\n\n**Dandiset.** [DANDI:000409](https://dandiarchive.org/dandiset/000409/0.260309.1324), version\n0.260309.1324. The paper does not cite a DANDI version (its data statement points to the IBL's own\ndata release). 0.260309.1324 is the only published version. The draft holds the same 2,048 files\nwith the same paths and sizes; its metadata differ (the draft links the Nature paper, the published\nversion the bioRxiv preprint), none of which the analysis uses.\n\n**What the dandiset holds.** For each of 459 sessions a processed file (trials, spike-sorted units of\nall probes with their Allen CCF localisation, wheel, licks, and for most sessions video pose, pupil\nand motion energy), a raw electrophysiology file, and up to three videos. This notebook streams the\nprocessed files only.\n\n**Outside inputs.** The paper's table of per-region results, `brainwidemap/meta/region_info.csv` in\nhttps://github.com/int-brain-lab/paper-brain-wide-map at commit 118fc36, and its table of inclusion\ncounts `meta/inclusion_info.csv`, read only as the paper's reported values. No measurement comes from\noutside the dandiset.\n\n**Scope.** The neural analyses of the paper run over 454 sessions and 201 regions with 10 repeats of\nnested cross-validation and 200 null sessions each; that does not fit the 30-minute limit. The\ndecoding, single-cell and trajectory claims are tested on a set of regions fixed in the claims file,\neach with all its sessions. Claims that need every region are blocked (`not_runnable`), with the\ntiming that shows it at the end.\n\n| Claim | Tested |\n|---|---|\n| dataset-sessions-mice-labs: 459 sessions, 139 mice, 12 labs | yes |\n| dataset-probes-units: 699 insertions, 621,733 units | yes |\n| well-isolated-neurons: 75,708 well-isolated neurons | yes |\n| canonical-regions: 201 regions, 62,857 neurons | yes |\n| brain-areas-279: 279 brain areas | yes |\n| mice-sex: 94 male, 45 female | yes |\n| mice-age-weight: 13 to 178 weeks, 16.1 to 35.7 g | yes |\n| probe-versions: 109 3A, 586 3B2, 4 2.4 | yes |\n| trials-per-session: mean 645, median 602, 401 to 1,525 | yes |\n| rf-mapping: receptive fields (Supplementary Fig. 5) | blocked, data missing |\n| behav-performance: 81.4% correct | yes |\n| behav-zero-contrast: 58.7% at 0% contrast, t138 = 20.18 | yes |\n| behav-early-movements: 22.8% of first movements under 80 ms | yes |\n| fig1d-contrast: better and faster at high contrast | yes |\n| fig1ef-end-of-session: worse and slower at session end | yes |\n| fig1g-block-switch: 5 to 10 trials to adjust | yes |\n| fig1h-block-bias: block biases choices at all contrasts | yes |\n| dec-stim-restricted: stimulus decodable in fewer regions, VISp | yes, 10 regions |\n| dec-choice-widespread: choice in more regions than stimulus, GRN | yes, 10 regions |\n| dec-feedback-nearly-all: feedback in nearly all regions | yes, 10 regions |\n| sc-stim-fraction: few stimulus-selective neurons | yes, 14 regions |\n| sc-choice-fraction: more choice- than stimulus-selective neurons | yes, 14 regions |\n| traj-latency-visual: LGd < VISp = LP < VISpm < VISam | yes |\n| traj-latency-late: IRN, GRN at 100 to 120 ms | yes, 2 of 5 regions |\n| traj-stim-regions: 104 regions with stimulus trajectories | blocked, not runnable |\n| fback-oscillation-licking: about 10 Hz with licking | yes, IRN |\n| wheel-speed-decoding: 163 of 201 regions | blocked, not runnable |\n| encoding-feedback-largest: correct-feedback kernel largest | blocked, not runnable |\n| video-correlates: half of neurons correlate with video | blocked, not runnable |\n| granger-interactions | blocked, not runnable |\n\"\"\")\n\ncode(r\"\"\"\nimport os\nos.environ.update(OMP_NUM_THREADS=\"1\", OPENBLAS_NUM_THREADS=\"1\", MKL_NUM_THREADS=\"1\")\nimport io\nimport time\nimport warnings\n\nimport matplotlib.pyplot as plt\nimport numpy as np\nimport pandas as pd\nimport requests\nfrom scipy import optimize, stats\n\nimport bwm\n\npd.set_option(\"display.width\", 220)\npd.set_option(\"display.max_columns\", 40)\npd.set_option(\"display.max_rows\", 300)\nwarnings.filterwarnings(\"ignore\", category=RuntimeWarning)\n\nREPO = \"https://raw.githubusercontent.com/int-brain-lab/paper-brain-wide-map/118fc36cb3602934466ad2c6087c2b3b441f9f1f\"\nregion_info = pd.read_csv(io.StringIO(requests.get(f\"{REPO}/brainwidemap/meta/region_info.csv\", timeout=60).text))\ninclusion_info = pd.read_csv(io.StringIO(requests.get(f\"{REPO}/brainwidemap/meta/inclusion_info.csv\", timeout=60).text), index_col=0)\n\nstarted = time.time()\nassets = bwm.list_assets()\nprocessed = assets[assets.kind == \"processed\"].sort_values(\"path\").reset_index(drop=True)\nscans = bwm.run_parallel(bwm.scan_session, list(processed.asset_id))\nscan_seconds = time.time() - started\nprint(f\"dandiset {bwm.DANDISET_ID} version {bwm.DANDISET_VERSION}: {len(assets)} assets; \"\n      f\"scanned {len(scans)} processed files in {scan_seconds:.0f} s\")\n\"\"\")\n\ncode(r\"\"\"\n# One row per session, and the trials of all sessions in the paper's terms.\nrows, trial_tables = [], []\nfor s in scans:\n    i, u = s[\"info\"], s[\"units\"]\n    t = bwm.task_table(s[\"trials\"])\n    mask, n_kept = bwm.analysis_mask(t)\n    t[\"analysed\"] = mask\n    t[\"eid\"] = i[\"session_id\"]\n    t[\"subject\"] = i[\"subject_id\"]\n    t[\"trial\"] = np.arange(len(t))\n    t[\"from_end\"] = len(t) - t.trial\n    trial_tables.append(t)\n    rows.append({\"eid\": i[\"session_id\"], \"subject\": i[\"subject_id\"], \"lab\": i[\"lab\"], \"sex\": i[\"sex\"],\n                 \"dob\": pd.Timestamp(i[\"date_of_birth\"]), \"start\": pd.Timestamp(i[\"session_start\"]),\n                 \"weight_g\": float(i[\"weight\"].split()[0]) * 1000 if i[\"weight\"] else np.nan,\n                 \"protocol\": i[\"protocol\"], \"revision\": i[\"revision\"], \"n_trials\": len(t),\n                 \"n_kept\": n_kept, \"n_analysed\": int(mask.sum()), \"n_units\": len(u),\n                 \"n_good\": int((u.ibl_quality_score == 1).sum()), \"n_probes\": u.probe_name.nunique(),\n                 \"modules\": \",\".join(i[\"processing\"]),\n                 \"passive\": \",\".join(s[\"passive\"]) if s[\"passive\"] else \"none\"})\nsessions = pd.DataFrame(rows)\ntrials = pd.concat(trial_tables, ignore_index=True)\nsessions[\"age_weeks\"] = [(st.tz_convert(\"UTC\") - d.tz_convert(\"UTC\")).days / 7 for st, d in zip(sessions.start, sessions.dob)]\nprint(sessions.drop(columns=[\"modules\", \"passive\"]).head().to_string())\n\"\"\")\n\nmd(r\"\"\"\n## Data check\n\nEach check of the metadata against the data is stated under its output.\n\"\"\")\n\ncode(r\"\"\"\nprint(\"Assets by kind:\", assets.kind.value_counts().to_dict())\nper_session = assets.groupby(\"eid\").kind.apply(lambda k: \",\".join(sorted(k)))\nprint(\"Sessions with a processed and a raw file:\", int((per_session.str.contains(\"processed\") & per_session.str.contains(\"raw\")).sum()),\n      \"of\", per_session.size)\nprint(\"Sessions:\", len(sessions), \"; subjects:\", sessions.subject.nunique(), \"; labs:\", sessions.lab.nunique())\nprint(\"Sessions per lab:\", sessions.lab.value_counts().to_dict())\nprint(\"Sessions per subject:\", sessions.subject.value_counts().value_counts().sort_index().to_dict(), \"(sessions: subjects)\")\nprint(\"Spike-sorting revision in the files:\", sessions.revision.value_counts().to_dict())\nprint(\"Task protocols:\", sessions.protocol.str.replace(\"_iblrig_tasks_\", \"\").value_counts().to_dict())\nprint(\"Processing modules:\", sessions.modules.value_counts().to_dict())\nprint(\"Passive protocol phases:\", sessions.passive.value_counts().to_dict())\nepochs = pd.concat([s[\"epochs\"] for s in scans])\nprint(\"Epoch types:\", epochs.protocol_type.value_counts().to_dict())\n\"\"\", [\"sanity\"])\n\nmd(r\"\"\"\nThe counts of sessions, mice and labs are those of the paper. The spike sorting in the files is IBL\nrevision 2025-05-06; the paper's code loads revision 2024-05-06. The unit counts below match the\npaper, so this does not change which units are well-isolated, as far as counts show. No session\nlists receptive-field mapping among its passive phases (only spontaneous activity and task replay),\nand the processed files hold no receptive-field stimulus, so the RF analysis cannot be repeated.\nPose, pupil and motion energy are missing from some sessions (see the module list).\n\"\"\")\n\ncode(r\"\"\"\nsubj = sessions.groupby(\"subject\").agg(sex=(\"sex\", \"first\"), n_sex=(\"sex\", \"nunique\"), dob=(\"dob\", \"nunique\"),\n                                       w_min=(\"weight_g\", \"min\"), w_max=(\"weight_g\", \"max\"), n=(\"eid\", \"size\"))\nprint(\"Sex per mouse:\", subj.sex.value_counts().to_dict(), \"; mice with more than one sex or birth date:\",\n      int((subj.n_sex > 1).sum()), int((subj.dob > 1).sum()))\nprint(\"Weight in the files (g): range\", sessions.weight_g.min(), \"to\", sessions.weight_g.max(),\n      \"; sessions without weight:\", int(sessions.weight_g.isna().sum()))\nprint(\"Mice whose weight differs between their sessions:\", int((subj.w_max > subj.w_min).sum()), \"of\", int((subj.n > 1).sum()),\n      \"with more than one session\")\nprint(\"Age at recording (weeks): range\", round(sessions.age_weeks.min(), 1), \"to\", round(sessions.age_weeks.max(), 1))\n\"\"\", [\"sanity\"])\n\nmd(r\"\"\"\nEvery mouse has one sex and one date of birth. The weight field holds one value per session file.\n\"\"\")\n\ncode(r\"\"\"\nprint(\"Trial columns:\", list(scans[0][\"trials\"].columns))\nprint(\"Trials:\", len(trials), \"; per session\", sessions.n_trials.min(), \"to\", sessions.n_trials.max())\nprint(\"Contrasts (%):\", (trials.contrast * 100).value_counts().sort_index().to_dict())\nc = trials[trials.p_left != 0.5].contrast.value_counts()\nprint(\"Ratio of contrasts 1, 0.25, 0.125, 0.0625, 0 in biased blocks:\", (c.loc[[1, 0.25, 0.125, 0.0625, 0]] / c.loc[0]).round(2).tolist())\nprint(\"p_left values:\", trials.p_left.value_counts().to_dict())\nfirst = trials.groupby(\"eid\").apply(lambda g: int((g.block == 0).sum()), include_groups=False)\nprint(\"Length of the first (unbiased) block:\", first.value_counts().to_dict())\nblen = trials[trials.block > 0].groupby([\"eid\", \"block\"]).size()\nlast = trials.groupby(\"eid\").block.max()\ninner = blen[[b < last[e] for e, b in blen.index]]\nprint(\"Biased block lengths, last block of each session left out: min\", inner.min(), \"max\", inner.max(), \"mean\", round(inner.mean(), 1))\nprint(\"Stimulus side x choice x rewarded:\")\nprint(pd.crosstab([trials.side, trials.choice], trials.correct).to_string())\nprint(\"Reward volume on rewarded trials (uL):\", trials[trials.correct].reward_ul.round(2).value_counts().head(6).to_dict())\nq = pd.concat([s[\"trials\"].quiescence_period for s in scans])\nprint(\"Quiescence period (s): range\", round(q.min(), 3), \"to\", round(q.max(), 3))\nprint(\"Missing values:\", {k: int(trials[k].isna().sum()) for k in [\"stim_on\", \"go_cue\", \"first_move\", \"feedback_time\"]})\nprint(\"Trials without a response:\", int((trials.choice == 0).sum()))\nprint(\"Stimulus onset minus go cue (ms), median and 1st/99th percentiles:\",\n      np.nanpercentile((trials.stim_on - trials.go_cue) * 1000, [50, 1, 99]).round(1).tolist())\nprint(\"First movement before stimulus onset:\", round(float(np.mean(trials.rt < 0)) * 100, 2), \"% of trials; before the go cue:\",\n      round(float(np.mean(trials.first_move < trials.go_cue)) * 100, 2), \"%\")\nprint(\"Trials analysed (complete events, first movement 0.08 to 2 s):\", int(trials.analysed.sum()), \"of\", len(trials))\nprint(\"Sessions truncated to pass the 90% criterion on 100% contrast:\", int((sessions.n_kept < sessions.n_trials).sum()))\n\"\"\", [\"sanity\"])\n\nmd(r\"\"\"\nThe stimulus, choice and reward columns agree: a left stimulus is rewarded after a clockwise turn\nand a right stimulus after a counter-clockwise turn, as the table's description says (clockwise moves\nthe stimulus right, towards the centre). The choice called right here is the counter-clockwise turn.\nThe contrasts and block probabilities are those of the Methods, and the first block is the 90\nunbiased trials. Two descriptions disagree with the data. The first movement time is described as\n\"after the go cue\", but in a part of the trials it precedes both the go cue and the stimulus onset\n(printed above); the paper's 80 ms threshold removes these. The reward is 3 uL in the Methods, while\nthe files record the volumes printed above. Neither is used by an analysis that depends on it,\nother than through the paper's own trial mask.\n\"\"\")\n\ncode(r\"\"\"\nunits = pd.concat([s[\"units\"].assign(eid=s[\"info\"][\"session_id\"]) for s in scans], ignore_index=True)\npasses = ((units.median_spike_amplitude_uV > 50).astype(int) + (units.noise_cutoff < 20).astype(int)\n          + (units.sliding_rp_violation == 1).astype(int)) / 3\nprint(\"Units:\", len(units), \"; quality score values:\", units.ibl_quality_score.round(2).value_counts().sort_index().to_dict())\nprint(\"Units whose score equals the fraction of the three metrics they pass:\",\n      int(np.isclose(passes, units.ibl_quality_score, atol=0.01).sum()), \"of\", len(units))\nprint(\"Units whose spike_count equals the length of their spike train:\", int((units.spike_count == units.n_spikes_index).sum()))\nprint(\"Units whose probe matches the probe of their peak channel:\", int((units.probe_name == units.region_probe).sum()))\nprobe_models = pd.Series([v.split(\" probe.\")[0].replace(\"A \", \"\", 1) for s in scans for v in s[\"probes\"].values()])\nprint(\"Probe devices by model:\", probe_models.value_counts().to_dict())\nprint(\"Units per probe: mean\", round(len(units) / sessions.n_probes.sum(), 1))\n\"\"\", [\"sanity\"])\n\nmd(r\"\"\"\nThe quality score is the fraction of the three metrics (median amplitude above 50 uV, noise cutoff\nbelow 20, sliding refractory-period test) for nearly all units; the exceptions are counted above.\nThe units table's description calls the score a `label` column, which is not in the files, and\ndescribes all units as from Neuropixels 1.0 probes, though four insertions used 2.x probes.\n\"\"\")\n\ncode(r\"\"\"\n# Recordings deposited twice: identical trial timings or identical unit spike counts.\nfp_trials = trials.groupby(\"eid\").apply(lambda g: (len(g), round(float(g.stim_on.iloc[0]), 4), round(float(g.feedback_time.iloc[-1]), 4)), include_groups=False)\ndup_t = fp_trials[fp_trials.duplicated(keep=False)]\nfp_units = units.groupby([\"eid\", \"probe_name\"]).spike_count.apply(lambda c: tuple(np.sort(c.values)[-20:]))\ndup_u = fp_units[fp_units.duplicated(keep=False)]\nprint(\"Sessions sharing trial count, first stimulus time and last feedback time with another:\", len(dup_t))\nprint(\"Probe insertions sharing their 20 largest unit spike counts with another:\", len(dup_u))\nsame_day = sessions.groupby([\"subject\", sessions.start.dt.date]).size()\nprint(\"Mice with more than one session on one day:\", int((same_day > 1).sum()))\n\"\"\", [\"sanity\"])\n\nmd(r\"\"\"\nNo session or insertion repeats another, so each recording is counted once. Units are taken per\nsession; no analysis here treats a unit as the same across sessions.\n\"\"\")\n\ncode(r\"\"\"\n# Clocks of the wheel and lick streams against the trials table.\nnear, lick_ratio = [], []\nfor s in scans:\n    t = bwm.task_table(s[\"trials\"])\n    fm = t.first_move.dropna().values\n    wm = np.sort(s[\"wheel_moves\"])\n    if len(wm) and len(fm):\n        j = np.clip(np.searchsorted(wm, fm), 1, len(wm) - 1)\n        near.append(np.minimum(np.abs(wm[j] - fm), np.abs(wm[j - 1] - fm)))\n    lk = np.sort(s[\"licks\"])\n    fb = t.feedback_time[t.correct].dropna().values\n    if len(lk) > 100:\n        after = (np.searchsorted(lk, fb + 1) - np.searchsorted(lk, fb)).sum()\n        before = (np.searchsorted(lk, fb) - np.searchsorted(lk, fb - 1)).sum()\n        lick_ratio.append(after / max(before, 1))\nnear = np.concatenate(near)\nprint(\"First movement time to the nearest wheel-movement onset (ms): median\", round(np.median(near) * 1000, 2),\n      \"; within 50 ms:\", round(np.mean(near < 0.05) * 100, 1), \"% of\", len(near), \"trials\")\nprint(\"Licks in the 1 s after reward over the 1 s before, per session: median\", round(np.median(lick_ratio), 1),\n      \"; sessions above 2:\", int(np.sum(np.array(lick_ratio) > 2)), \"of\", len(lick_ratio))\n\"\"\", [\"sanity\"])\n\nmd(r\"\"\"\nThe trials' first movement times coincide with onsets in the wheel's movement intervals, and licks\nrise after reward in nearly every session with licks, so the wheel and lick streams share the trials'\nclock. The spikes are checked against the trials' clock after they are loaded, below.\n\"\"\")\n\n# ---------------- dataset claims ----------------\nmd(r\"\"\"\n## dataset-sessions-mice-labs\n\n> The data come from 459 sessions of 139 mice recorded in 12 laboratories.\n\"\"\")\ncode(r\"\"\"\nprint(\"Sessions:\", len(sessions), \"(paper 459); mice:\", sessions.subject.nunique(), \"(139); labs:\", sessions.lab.nunique(), \"(12)\")\n\"\"\", [\"claim:dataset-sessions-mice-labs\"])\nmd(\"**Result: reproduced.** The dandiset holds 459 sessions of 139 mice from 12 labs, as the paper states.\")\n\nmd(r\"\"\"\n## dataset-probes-units\n\n> 699 Neuropixels insertions yielded 621,733 units, an average of 889 per probe.\n\"\"\")\ncode(r\"\"\"\nn_probes = int(sessions.n_probes.sum())\nprint(\"Insertions:\", n_probes, \"(paper 699); units:\", len(units), \"(621,733); per probe:\", round(len(units) / n_probes, 1), \"(889)\")\n\"\"\", [\"claim:dataset-probes-units\"])\nmd(\"**Result: reproduced.** 699 insertions and 621,733 units, 889.5 per probe.\")\n\nmd(r\"\"\"\n## well-isolated-neurons\n\n> Stringent quality metrics identified 75,708 well-isolated neurons, an average of 108 per probe.\n\"\"\")\ncode(r\"\"\"\nn_good = int((units.ibl_quality_score == 1).sum())\nprint(\"Well-isolated units:\", n_good, \"(paper 75,708); per probe:\", round(n_good / n_probes, 1), \"(108)\")\nprint(\"Well-isolated by recomputing the three metrics:\", int((passes == 1).sum()))\n\"\"\", [\"claim:well-isolated-neurons\"])\nmd(\"**Result: reproduced.** 75,708 units have a quality score of 1, 108.3 per probe.\")\n\nmd(r\"\"\"\n## canonical-regions\n\n> The main analyses use a canonical dataset of 201 regions with at least 2 sessions of 5\n> well-isolated neurons and at least 20 neurons in total, 62,857 neurons.\n\"\"\")\ncode(r\"\"\"\ncanon, steps = bwm.canonical_units(scans)\npaper_steps = inclusion_info.iloc[[0, 3, 4, 5, 6, 7]].reset_index(drop=True)\nsteps[\"paper_sessions\"] = paper_steps.n_sessions.values\nsteps[\"paper_units\"] = paper_steps.n_units.values\nsteps[\"paper_regions\"] = paper_steps.n_regions.values\nprint(steps.to_string(index=False))\ncanon_regions = sorted(canon.region.unique())\npaper_canonical = set(region_info[region_info.canonical].Beryl)\nprint(\"\\nCanonical regions:\", len(canon_regions), \"; regions marked canonical in region_info.csv:\", len(paper_canonical),\n      \"; of ours among them:\", len(set(canon_regions) & paper_canonical))\nprint(\"Marked canonical in region_info.csv but with fewer than 20 units:\", sorted(paper_canonical - set(canon_regions)))\n\"\"\", [\"claim:canonical-regions\"])\nmd(r\"\"\"\n**Result: reproduced.** Every inclusion step gives the counts of the paper's inclusion table, ending\nwith 201 regions and 62,857 neurons. The `canonical` column of the paper's region table marks 210\nregions, those left before the 20-neuron step.\n\"\"\")\n\nmd(r\"\"\"\n## brain-areas-279\n\n> The probes covered 279 brain areas.\n\"\"\")\ncode(r\"\"\"\ngrey = units[~units.region.isin([\"void\", \"root\"])]\nprint(\"Beryl regions with at least one unit, void and root left out:\", grey.region.nunique(), \"(paper 279)\")\nprint(\"With at least one well-isolated unit:\", grey[grey.ibl_quality_score == 1].region.nunique())\n\"\"\", [\"claim:brain-areas-279\"])\nmd(\"**Result: reproduced.** Units fall in 279 Beryl regions other than void and root.\")\n\nmd(r\"\"\"\n## mice-sex\n\n> The 139 mice were 94 male and 45 female.\n\"\"\")\ncode(r\"\"\"\nprint(subj.sex.value_counts().to_dict(), \"(paper 94 male, 45 female)\")\n\"\"\", [\"claim:mice-sex\"])\nmd(\"**Result: reproduced.** 94 male and 45 female mice.\")\n\nmd(r\"\"\"\n## mice-age-weight\n\n> On the day of recording the mice were aged 13 to 178 weeks (mean 44.96, median 27.0) and weighed\n> 16.1 to 35.7 g (mean 23.9, median 23.84).\n\"\"\")\ncode(r\"\"\"\ns_sorted = sessions.sort_values(\"start\")\nreadings = {\"a: first session\": s_sorted.groupby(\"subject\").first(), \"b: last session\": s_sorted.groupby(\"subject\").last(),\n            \"c: every session\": s_sorted}\nexpected = {\"age_weeks\": [13, 178, 44.96, 27.0], \"weight_g\": [16.1, 35.7, 23.9, 23.84]}\nfor name, d in readings.items():\n    for var, exp in expected.items():\n        v = d[var].dropna()\n        got = [v.min(), v.max(), v.mean(), v.median()]\n        ok = [abs(g - e) <= 0.1 * e for g, e in zip(got, exp)]\n        print(f\"{name:17s} {var:9s} min {got[0]:6.1f} max {got[1]:6.1f} mean {got[2]:6.2f} median {got[3]:6.2f}  \"\n              f\"within 10%: {ok}  (n = {len(v)})\")\nprint(\"Paper's code (meta/mice_info.py) takes age_weeks and reference_weight from the IBL database, not from the recording day.\")\n\"\"\", [\"claim:mice-age-weight\"])\nmd(\"**Result: see below.**\")\n\nmd(r\"\"\"\n## probe-versions\n\n> The insertions used Neuropixels 1.0 probes of versions 3A (109) and 3B2 (586), and Neuropixels\n> 2.4 probes (4).\n\"\"\")\ncode(r\"\"\"\ngroup = probe_models.map(lambda m: \"3A (NP1010)\" if m == \"NP1010\" else \"3B2 (PRB_1_4_0480_1)\" if m.startswith(\"PRB_1_4_0480_1\")\n                         else \"2.x (NP2010)\" if m == \"NP2010\" else m)\nprint(group.value_counts().to_dict(), \"(paper 3A 109, 3B2 586, 2.4 4)\")\n\"\"\", [\"claim:probe-versions\"])\nmd(\"**Result: reproduced.** The model groups hold 586, 109 and 4 insertions.\")\n\nmd(r\"\"\"\n## trials-per-session\n\n> Recorded sessions lasted on average 645 trials (median 602, range 401 to 1,525).\n\"\"\")\ncode(r\"\"\"\nn = sessions.n_trials\nprint(f\"mean {n.mean():.1f} (645), median {n.median():.0f} (602), range {n.min()} to {n.max()} (401 to 1,525)\")\n\"\"\", [\"claim:trials-per-session\"])\nmd(\"**Result: reproduced.** Mean 645.1, median 601, range 401 to 1,525 trials.\")\n\nmd(r\"\"\"\n## rf-mapping (blocked)\n\n> Receptive-field mapping after the task found a relatively small fraction of cells with significant\n> receptive fields.\n\nBlocked, data missing: no session holds the receptive-field mapping phase or its stimulus (see the\ndata check). The paper used it in 504 of 699 insertions.\n\"\"\")\n\n# ---------------- behaviour ----------------\nmd(r\"\"\"\n## behav-performance\n\n> After training, mice made correct choices on 81.4 +/- 0.4% (mean +/- s.d.) of trials.\n\"\"\")\ncode(r\"\"\"\ndef summary(v):\n    v = np.asarray(v, float)\n    return f\"mean {v.mean():.2f}%, s.d. {v.std(ddof=1):.2f}, s.e.m. {v.std(ddof=1) / np.sqrt(len(v)):.2f} (n = {len(v)})\"\n\nperf = {\n    \"a: mice, all trials\": trials.groupby(\"subject\").correct.mean() * 100,\n    \"b: mice, analysed trials\": trials[trials.analysed].groupby(\"subject\").correct.mean() * 100,\n    \"c: sessions, all trials\": trials.groupby(\"eid\").correct.mean() * 100,\n}\nfor k, v in perf.items():\n    print(f\"{k:26s}\", summary(v), \" within 81.4 +/- 0.4:\", abs(v.mean() - 81.4) <= 0.4)\npooled = trials.correct.mean() * 100\nprint(f\"{'d: all trials pooled':26s} {pooled:.2f}%  within 81.4 +/- 0.4: {abs(pooled - 81.4) <= 0.4}\")\n\"\"\", [\"claim:behav-performance\"])\nmd(\"**Result: see below.**\")\n\nmd(r\"\"\"\n## behav-zero-contrast\n\n> On 0% contrast trials mice were rewarded on 58.7 +/- 0.4% (mean +/- s.e.m. across mice) of trials,\n> better than chance (t138 = 20.18, P = 5.2e-43).\n\"\"\")\ncode(r\"\"\"\nfor name, d in ((\"a: all trials\", trials), (\"b: analysed trials\", trials[trials.analysed])):\n    v = d[d.contrast == 0].groupby(\"subject\").correct.mean() * 100\n    t_, p_ = stats.ttest_1samp(v, 50)\n    print(f\"{name:20s} {summary(v)}; t{len(v) - 1} = {t_:.2f}, P = {p_:.2g}; \"\n          f\"mean within 0.4: {abs(v.mean() - 58.7) <= 0.4}, t within 2.02: {abs(t_ - 20.18) <= 2.02}\")\nprint(\"Paper: t138 = 20.18 gives P =\", f\"{stats.t.sf(20.18, 138) * 2:.2g}\", \"two-sided\")\n\"\"\", [\"claim:behav-zero-contrast\"])\nmd(\"**Result: see below.**\")\n\nmd(r\"\"\"\n## behav-early-movements\n\n> 22.8% of first wheel-movement times occurred under 80 ms after stimulus onset.\n\"\"\")\ncode(r\"\"\"\nearly = trials.rt < 0.08\nhas = trials.rt.notna()\nprint(f\"a: over all trials {early.mean() * 100:.2f}% of {len(trials)}\")\nprint(f\"b: over trials with both times {early[has].mean() * 100:.2f}% of {int(has.sum())}\")\nprint(f\"c: mean over sessions {trials[has].groupby('eid').rt.apply(lambda r: np.mean(r < 0.08)).mean() * 100:.2f}%\")\nprint(f\"Of which before stimulus onset: {np.mean(trials.rt[has] < 0) * 100:.2f}% of trials with both times\")\n\"\"\", [\"claim:behav-early-movements\"])\nmd(\"**Result: see below.**\")\n\nmd(r\"\"\"\n## fig1d-contrast\n\n> Mice performed better and faster on trials with high visual contrast.\n\"\"\")\ncode(r\"\"\"\nresp = trials[trials.choice != 0]\nby_c = resp.groupby([\"subject\", \"contrast\"]).agg(correct=(\"correct\", \"mean\"), rt=(\"rt\", \"median\")).reset_index()\npc = by_c.pivot(index=\"subject\", columns=\"contrast\", values=\"correct\") * 100\nrt = by_c.pivot(index=\"subject\", columns=\"contrast\", values=\"rt\") * 1000\nprint(\"Median over mice, percent correct by contrast:\", pc.median().round(1).to_dict())\nprint(\"Median over mice, median first movement time (ms) by contrast:\", rt.median().round(0).to_dict())\nw1 = stats.wilcoxon(pc[1.0], pc[0.0])\nw2 = stats.wilcoxon(rt[1.0], rt[0.0])\nprint(f\"100% against 0%: correct higher in {(pc[1.0] > pc[0.0]).sum()} of {len(pc)} mice, p = {w1.pvalue:.2g}; \"\n      f\"first movement shorter in {(rt[1.0] < rt[0.0]).sum()} of {len(rt)} mice, p = {w2.pvalue:.2g}\")\nprint(\"Median percent correct rises at every contrast step:\", bool(np.all(np.diff(pc.median().values) > 0)))\nprint(\"Median first movement time falls at every contrast step:\", bool(np.all(np.diff(rt.median().values) < 0)))\n\"\"\", [\"claim:fig1d-contrast\"])\nmd(\"**Result: see below.**\")\n\nmd(r\"\"\"\n## fig1ef-end-of-session\n\n> Towards the end of the sessions, performance decreased and first wheel-movement times increased.\n\"\"\")\ncode(r\"\"\"\nnz = trials[(trials.contrast > 0) & (trials.choice != 0)]\nend = nz[nz.from_end <= 50].groupby(\"subject\").agg(c=(\"correct\", \"mean\"), rt=(\"rt\", \"median\"))\nmid = nz[(nz.from_end > 50) & (nz.from_end <= 300)].groupby(\"subject\").agg(c=(\"correct\", \"mean\"), rt=(\"rt\", \"median\"))\nw1 = stats.wilcoxon(end.c, mid.c)\nw2 = stats.wilcoxon(end.rt, mid.rt)\nprint(f\"Percent correct, last 50 trials: median over mice {end.c.median() * 100:.1f}; trials 51 to 300 from the end {mid.c.median() * 100:.1f}; \"\n      f\"lower at the end in {(end.c < mid.c).sum()} of {len(end)} mice, p = {w1.pvalue:.2g}\")\nprint(f\"Median first movement time (ms), last 50: {end.rt.median() * 1000:.0f}; trials 51 to 300: {mid.rt.median() * 1000:.0f}; \"\n      f\"longer at the end in {(end.rt > mid.rt).sum()} of {len(end)} mice, p = {w2.pvalue:.2g}\")\ncurve = nz[nz.from_end <= 400].assign(bin=lambda d: (d.from_end - 1) // 50).groupby([\"subject\", \"bin\"]).agg(c=(\"correct\", \"mean\"), rt=(\"rt\", \"median\"))\nprint(\"By 50-trial bins from the end (bin 0 is the last 50), median over mice:\")\nprint(curve.groupby(\"bin\").median().assign(c=lambda d: (d.c * 100).round(1), rt=lambda d: (d.rt * 1000).round(0)).T.to_string())\n\"\"\", [\"claim:fig1ef-end-of-session\"])\nmd(\"**Result: see below.**\")\n\nmd(r\"\"\"\n## fig1g-block-switch\n\n> After a block switch, mice took around 5 to 10 trials to adjust their behaviour, as shown by the\n> fraction of correct choices on 0% contrast trials after the switch.\n\"\"\")\ncode(r\"\"\"\nt2 = trials.copy()\nt2[\"pos\"] = t2.groupby([\"eid\", \"block\"]).cumcount() + 1\nsw = t2[(t2.block >= 2) & (t2.pos <= 40) & (t2.contrast == 0) & (t2.choice != 0)]\nmouse_curve = sw.groupby([\"subject\", \"pos\"]).correct.mean().unstack()\nmean_curve = mouse_curve.mean()\nn = mean_curve.index.values.astype(float)\nf = lambda x, a, b, tau: a - b * np.exp(-(x - 1) / tau)\n(a, b, tau), _ = optimize.curve_fit(f, n, mean_curve.values, p0=(0.7, 0.4, 5), maxfev=20000)\nprint(\"Mean over mice of the fraction correct on 0% trials, by position after the switch:\")\nprint(mean_curve.round(3).to_string())\nprint(f\"Fit: a = {a:.3f}, b = {b:.3f}, tau = {tau:.2f} trials; 90% of the change at {1 + tau * np.log(10):.1f} trials\")\nprint(\"Mice with 0% trials at position 1:\", int(mouse_curve[1].notna().sum()), \"; 0% trials in the curve:\", len(sw))\nfits = []\nfor k, row in mouse_curve.iterrows():\n    try:\n        p, _ = optimize.curve_fit(f, n[row.notna()], row.dropna().values, p0=(0.7, 0.4, 5), bounds=([0, -1, 0.1], [1, 1, 100]))\n        fits.append(p[2])\n    except RuntimeError:\n        fits.append(np.nan)\nfits = np.array(fits)\nprint(f\"Per-mouse tau: median {np.nanmedian(fits):.2f}, interquartile {np.nanpercentile(fits, 25):.2f} to {np.nanpercentile(fits, 75):.2f}; \"\n      f\"failed fits {int(np.isnan(fits).sum())} of {len(fits)}\")\nfig, ax = plt.subplots(figsize=(5, 3))\nax.plot(n, mean_curve.values, \"o\", ms=3)\nax.plot(n, f(n, a, b, tau))\nax.set_xlabel(\"trial after block switch (0% contrast)\")\nax.set_ylabel(\"fraction correct\")\nprint(\"Plotted range:\", round(mean_curve.min(), 3), \"to\", round(mean_curve.max(), 3))\n\"\"\", [\"claim:fig1g-block-switch\"])\nmd(\"**Result: see below.**\")\n\nmd(r\"\"\"\n## fig1h-block-bias\n\n> For all contrast values mice chose the side of the block's likely stimulus more often, responding\n> right more often in right blocks than in left blocks.\n\"\"\")\ncode(r\"\"\"\nrb = resp[resp.p_left != 0.5]\npr = rb.assign(right=rb.choice > 0).groupby([\"subject\", \"p_left\", \"signed_contrast\"]).right.mean().unstack([\"p_left\"])\ndiff = (pr[0.2] - pr[0.8]).unstack(\"signed_contrast\")\nrows = []\nfor c in diff.columns:\n    d = diff[c].dropna()\n    rows.append({\"signed_contrast\": c, \"mice\": len(d), \"median_diff\": round(d.median(), 3), \"higher_in\": int((d > 0).sum()),\n                 \"p\": stats.wilcoxon(d).pvalue})\nbias = pd.DataFrame(rows)\nprint(bias.to_string(index=False))\nprint(\"Contrasts with a higher right-block fraction (median > 0 and p < 0.05):\", int(((bias.median_diff > 0) & (bias.p < 0.05)).sum()), \"of 9\")\n\"\"\", [\"claim:fig1h-block-bias\"])\nmd(\"**Result: see below.**\")\n\n# ---------------- neural ----------------\nmd(r\"\"\"\n## Neural data: the regions tested and their spikes\n\nThe regions fixed in the claims file: the example regions VISp, GRN and IRN, seven regions drawn at\nrandom from the canonical regions with at most 12 sessions (leaving out the latency regions), and the\nlatency regions LGd, LP, VISpm and VISam. Each region uses all its canonical sessions and units.\n\"\"\")\ncode(r\"\"\"\nEXAMPLES = [\"VISp\", \"GRN\", \"IRN\"]\nLATENCY = [\"LGd\", \"VISp\", \"LP\", \"VISpm\", \"VISam\"]\nn_sess = canon.groupby(\"region\").eid.nunique()\npool = sorted(n_sess[n_sess <= 12].index.difference(EXAMPLES + LATENCY))\nRANDOM = sorted(np.random.default_rng(409).choice(pool, 7, replace=False).tolist())\nDECODING = EXAMPLES + RANDOM\nTRAJ = LATENCY + [\"IRN\", \"GRN\"]\nTESTED = sorted(set(DECODING) | set(TRAJ))\nprint(\"Random regions:\", RANDOM, \"from\", len(pool), \"candidates\")\nsel = canon[canon.region.isin(TESTED)]\nprint(sel.groupby(\"region\").agg(sessions=(\"eid\", \"nunique\"), units=(\"unit\", \"size\")).T.to_string())\njobs = []\nfor aid, g in sel.groupby(\"asset_id\"):\n    jobs.append((aid, g.unit.tolist(), g[g.region.isin(TRAJ)].unit.tolist(), g[g.region == \"IRN\"].unit.tolist()))\nt0 = time.time()\nextracted = bwm.run_parallel(bwm.extract_session, jobs)\nextract_seconds = time.time() - t0\nby_asset = {e[\"asset_id\"]: e for e in extracted}\nunit_region = {(r.asset_id, r.unit): r.region for r in sel.itertuples()}\nprint(f\"Streamed {len(extracted)} sessions, {sum(e['n_spikes'] for e in extracted) / 1e6:.0f} million spikes of {len(sel)} units, \"\n      f\"in {extract_seconds:.0f} s ({extract_seconds / len(extracted):.2f} s per session with {bwm.N_WORKERS} processes)\")\nprint(\"Units whose spike times were not sorted:\", sum(e[\"unsorted_units\"] for e in extracted))\n\"\"\")\n\ncode(r\"\"\"\n# Spikes against the trials' clock: decode feedback from 0.2 s windows at offsets around feedback,\n# and from the window just after feedback with the labels shifted by one trial.\nclock = bwm.run_parallel(bwm.clock_job, [(e[\"asset_id\"], e[\"trials\"], e[\"clock\"], 7 + k) for k, e in enumerate(extracted)], workers=4)\nacc = np.array([c[\"acc\"] for c in clock])\nshifted = np.array([c[\"shifted\"] for c in clock])\nok = ~np.isnan(acc).any(1)\nprint(\"Balanced accuracy of feedback decoding by window start relative to feedback (s), median over sessions:\")\nprint(dict(zip(bwm.CLOCK_OFFSETS.tolist(), np.nanmedian(acc, 0).round(3).tolist())))\nj0 = int(np.where(bwm.CLOCK_OFFSETS == 0)[0][0])\njump = acc[:, j0] - acc[:, j0 - 1]\nprint(f\"Window 0 to 0.2 s minus window -0.2 to 0 s: median {np.nanmedian(jump):.3f}; above 0.05 in {int(np.sum(jump > 0.05))} of {int(ok.sum())} sessions\")\nprint(f\"Labels shifted by one trial, window 0 to 0.2 s: median {np.nanmedian(shifted):.3f}\")\nbad = [processed.set_index(\"asset_id\").loc[c[\"key\"], \"path\"].split(\"/\")[0] for c, j in zip(clock, jump) if not j > 0.05]\nprint(\"Sessions where the jump is not established:\", bad)\n\"\"\", [\"sanity\"])\n\nmd(r\"\"\"\nIn nearly every session, feedback becomes decodable in the window that starts at feedback and not\nbefore, and shifting the labels by one trial removes it, so the spike times share the clock of the\ntrials table. The sessions where this could not be established are listed above.\n\"\"\")\n\ncode(r\"\"\"\n# Region-session inputs.\ndef region_counts(region, var_keys=(\"stim\", \"choice\", \"feedback\")):\n    out = []\n    for aid, g in sel[sel.region == region].groupby(\"asset_id\"):\n        e = by_asset[aid]\n        cols = np.isin(e[\"units\"], g.unit.values)\n        out.append((aid, e[\"trials\"], {k: e[\"counts\"][k][:, cols] for k in var_keys}))\n    return out\n\nt0 = time.time()\ndec_jobs = []\nfor region in DECODING:\n    for k, (aid, t, c) in enumerate(region_counts(region)):\n        dec_jobs.append(((region, aid), t, c, 1000 * (DECODING.index(region) + 1) + k))\ndec = bwm.run_parallel(bwm.decode_job, dec_jobs, workers=4)\ndecode_seconds = time.time() - t0\nrows = []\nfor d in dec:\n    for var in (\"stim\", \"choice\", \"feedback\"):\n        rows.append({\"region\": d[\"key\"][0], \"asset_id\": d[\"key\"][1], \"var\": var, **{k: d[var][k] for k in (\"n_trials\", \"n_minor\", \"n_null\", \"score\", \"p\", \"corrected\")}})\ndec_df = pd.DataFrame(rows)\nprint(f\"{len(dec_jobs)} region-sessions decoded in {decode_seconds:.0f} s; null sessions per decoding: \"\n      f\"{dec_df.n_null.min()} to {dec_df.n_null.max()}; learning rates of the action-kernel model: \"\n      f\"{pd.Series([d['alpha'] for d in dec]).value_counts().sort_index().to_dict()}\")\nregion_res = []\nfor (region, var), g in dec_df.groupby([\"region\", \"var\"]):\n    region_res.append({\"region\": region, \"var\": var, \"sessions\": len(g), \"p_fisher\": bwm.fisher_p(g.p), \"effect\": g.corrected.median(),\n                       \"median_score\": g.score.median(), \"sessions_p05\": int((g.p < 0.05).sum())})\nregion_res = pd.DataFrame(region_res)\nregion_res[\"significant\"] = False\nfor var, g in region_res.groupby(\"var\"):\n    region_res.loc[g.index, \"significant\"] = bwm.bh(g.p_fisher.values, 0.01)\nri = region_info.set_index(\"Beryl\")\npaper_col = {\"stim\": \"stim_dec\", \"choice\": \"choice_dec\", \"feedback\": \"fback_dec\"}\nregion_res[\"paper_effect\"] = [ri.loc[r, paper_col[v]] for r, v in zip(region_res.region, region_res[\"var\"])]\nregion_res[\"paper_significant\"] = [bool(ri.loc[r, paper_col[v] + \"_sig\"]) for r, v in zip(region_res.region, region_res[\"var\"])]\nprint(region_res.round(4).sort_values([\"var\", \"region\"]).to_string(index=False))\n\"\"\")\n\nmd(r\"\"\"\n## dec-stim-restricted\n\n> The visual stimulus side, decoded from the first 100 ms after stimulus onset, was represented in a\n> narrower set of regions than choice or feedback, with strong signatures in visual cortex such as\n> VISp.\n\"\"\")\ncode(r\"\"\"\nnsig = region_res.groupby(\"var\").significant.sum()\nprint(\"Tested regions significant (BH q = 0.01 over the 10 regions):\", nsig.to_dict())\nvisp = region_res[(region_res.region == \"VISp\") & (region_res[\"var\"] == \"stim\")].iloc[0]\nprint(f\"VISp stimulus: {visp.sessions} sessions, Fisher p = {visp.p_fisher:.2g}, effect {visp.effect:.3f} (paper {visp.paper_effect}), \"\n      f\"sessions with p < 0.05: {visp.sessions_p05}\")\ns = region_res[region_res[\"var\"] == \"stim\"]\nprint(\"Agreement with the paper's significance:\", int((s.significant == s.paper_significant).sum()), \"of\", len(s))\nprint(\"Spearman correlation of effects with the paper's:\", stats.spearmanr(s.effect, s.paper_effect))\nprint(\"Paper over 201 regions: stimulus 40, choice 172, feedback 198 significant\")\npv = dec_df[dec_df[\"var\"] == \"stim\"].groupby(\"region\").p.apply(lambda p: bwm.fisher_p(p))\nprint(\"Variant, Fisher p < 0.01 without the correction:\", int((pv < 0.01).sum()), \"regions\")\n\"\"\", [\"claim:dec-stim-restricted\"])\nmd(\"**Result: see below.**\")\n\nmd(r\"\"\"\n## dec-choice-widespread\n\n> Choice, decoded from the 100 ms before the first wheel movement, was represented in a larger\n> number of regions than the visual stimulus, with strong effects in hindbrain regions such as GRN.\n\"\"\")\ncode(r\"\"\"\ngrn = region_res[(region_res.region == \"GRN\") & (region_res[\"var\"] == \"choice\")].iloc[0]\nprint(f\"GRN choice: {grn.sessions} sessions, Fisher p = {grn.p_fisher:.2g}, effect {grn.effect:.3f} (paper {grn.paper_effect})\")\nc = region_res[region_res[\"var\"] == \"choice\"]\nprint(\"Significant for choice:\", int(c.significant.sum()), \"; for stimulus:\", int(nsig[\"stim\"]))\nprint(\"Agreement with the paper's significance:\", int((c.significant == c.paper_significant).sum()), \"of\", len(c))\nprint(\"Spearman correlation of effects with the paper's:\", stats.spearmanr(c.effect, c.paper_effect))\nprint(c[[\"region\", \"sessions\", \"p_fisher\", \"effect\", \"paper_effect\", \"significant\", \"paper_significant\"]].round(4).to_string(index=False))\n\"\"\", [\"claim:dec-choice-widespread\"])\nmd(\"**Result: see below.**\")\n\nmd(r\"\"\"\n## dec-feedback-nearly-all\n\n> Whether the trial was correct could be decoded from the 200 ms after feedback onset in nearly all\n> recorded regions, almost perfectly in many.\n\"\"\")\ncode(r\"\"\"\nfb = region_res[region_res[\"var\"] == \"feedback\"]\nprint(\"Significant for feedback:\", int(fb.significant.sum()), \"of\", len(fb), \"; IRN significant:\", bool(fb[fb.region == \"IRN\"].significant.iloc[0]))\nprint(fb[[\"region\", \"sessions\", \"p_fisher\", \"effect\", \"median_score\", \"paper_effect\", \"significant\", \"paper_significant\"]].round(4).to_string(index=False))\nf_sess = dec_df[dec_df[\"var\"] == \"feedback\"]\nprint(f\"Region-sessions with balanced accuracy above 0.9: {int((f_sess.score > 0.9).sum())} of {len(f_sess)}; median accuracy {f_sess.score.median():.3f}\")\nprint(\"Spearman correlation of effects with the paper's:\", stats.spearmanr(fb.effect, fb.paper_effect))\n\"\"\", [\"claim:dec-feedback-nearly-all\"])\nmd(\"**Result: see below.**\")\n\ncode(r\"\"\"\n# Variant for the three decoding claims: the null with the full nested search of C, against the\n# null that reuses the real labels' C, on three VISp, GRN and IRN sessions with 20 nulls each.\nnn_jobs = []\nfor k, region in enumerate(EXAMPLES):\n    aid, t, c = region_counts(region)[0]\n    nn_jobs.append(((region, aid), t, c, 5000 + k, 20))\nnn = bwm.run_parallel(bwm.nested_null_job, nn_jobs, workers=3)\nfor r in nn:\n    for var in (\"stim\", \"choice\", \"feedback\"):\n        a, b = r[var][\"nested\"], r[var][\"reused\"]\n        print(f\"{r['key'][0]:5s} {var:8s} nested null: median {np.median(a):.3f}, 95th pct {np.percentile(a, 95):.3f}; \"\n              f\"reused C: median {np.median(b):.3f}, 95th pct {np.percentile(b, 95):.3f}\")\n\"\"\", [\"claim:dec-stim-restricted\", \"claim:dec-choice-widespread\", \"claim:dec-feedback-nearly-all\"])\n\nmd(r\"\"\"\n## Single-cell selectivity (sc-stim-fraction, sc-choice-fraction)\n\nThe code's test on the units of all 14 loaded regions, with a null run on one pseudo-session (stimulus)\nor synthetic session (choice) per region-session to measure the false-positive rate.\n\"\"\")\ncode(r\"\"\"\nt0 = time.time()\nsc_jobs = []\nfor region in TESTED:\n    for k, (aid, t, c) in enumerate(region_counts(region, (\"stim\", \"choice\"))):\n        sc_jobs.append(((region, aid), t, c, 20000 + 100 * TESTED.index(region) + k))\nsc = bwm.run_parallel(bwm.single_cell_job, sc_jobs, workers=4)\nrows = []\nfor r in sc:\n    for i in range(len(r[\"stim_real\"])):\n        rows.append({\"region\": r[\"key\"][0], \"asset_id\": r[\"key\"][1], **{k: bool(r[k][i]) for k in r if k != \"key\"}})\ncells = pd.DataFrame(rows)\nprint(f\"{len(cells)} units in {len(sc_jobs)} region-sessions, in {time.time() - t0:.0f} s\")\nfrac = cells.groupby(\"region\")[[\"stim_real\", \"choice_real\", \"stim_null\", \"choice_null\"]].mean()\nfrac[\"units\"] = cells.groupby(\"region\").size()\nfrac[\"paper_stim\"] = [ri.loc[r, \"stim_man\"] for r in frac.index]\nfrac[\"paper_choice\"] = [ri.loc[r, \"choice_man\"] for r in frac.index]\nprint(frac.round(4).to_string())\n\"\"\")\n\nmd(r\"\"\"\n## sc-stim-fraction\n\n> Single-cell tests controlling for choice and block found few stimulus-selective neurons (0.5% of\n> all neurons); even in the regions with the largest fractions, such as visual cortex, the fraction\n> did not exceed about 10%.\n\"\"\")\ncode(r\"\"\"\ndef ci(k, n):\n    lo = stats.beta.ppf(0.025, k, n - k + 1) if k > 0 else 0.0\n    hi = stats.beta.ppf(0.975, k + 1, n - k)\n    return lo, hi\n\nfor var in (\"stim\", \"choice\"):\n    k, n = int(cells[f\"{var}_null\"].sum()), len(cells)\n    lo, hi = ci(k, n)\n    print(f\"{var}: null run selects {k} of {n} units ({k / n:.2e}), 95% interval {lo:.2e} to {hi:.2e}; \"\n          f\"paper's rate 5e-5, band 1.7e-5 to 1.5e-4; interval excludes the band: {lo > 1.5e-4 or hi < 1.7e-5}\")\n    print(f\"   null units passing the simple test alone: {cells[f'{var}_null_mw'].mean():.2e}; the combined test alone: {cells[f'{var}_null_cc'].mean():.3f}\")\nprint(\"\\nStimulus: largest regional fraction\", round(frac.stim_real.max(), 4), \"in\", frac.stim_real.idxmax(),\n      \"; pooled over the 14 regions\", round(cells.stim_real.mean(), 4))\nagree = (frac.stim_real - frac.paper_stim).abs() <= 0.02\nprint(\"Regions within 0.02 of the paper's fraction:\", int(agree.sum()), \"of\", len(frac))\nprint(\"Paper, pooled over the canonical regions (from region_info.csv):\",\n      round(float((region_info[region_info.canonical].stim_man * region_info[region_info.canonical][\"# good neurons\"]).sum()\n                  / region_info[region_info.canonical][\"# good neurons\"].sum()), 4))\n\"\"\", [\"claim:sc-stim-fraction\"])\nmd(\"**Result: see below.**\")\n\nmd(r\"\"\"\n## sc-choice-fraction\n\n> More neurons responded to choice than to the visual stimulus (4% of all neurons), with the largest\n> fractions in hindbrain, midbrain and thalamic regions.\n\"\"\")\ncode(r\"\"\"\nonly_c = int((cells.choice_real & ~cells.stim_real).sum())\nonly_s = int((cells.stim_real & ~cells.choice_real).sum())\nbt = stats.binomtest(only_c, only_c + only_s, 0.5, alternative=\"greater\") if only_c + only_s else None\nprint(f\"Pooled: choice {cells.choice_real.mean():.4f}, stimulus {cells.stim_real.mean():.4f}; selective for choice only {only_c}, \"\n      f\"stimulus only {only_s}, binomial p = {bt.pvalue if bt else float('nan'):.2g}\")\nprint(\"Spearman correlation of regional choice fractions with the paper's:\", stats.spearmanr(frac.choice_real, frac.paper_choice))\nprint(frac[[\"units\", \"choice_real\", \"paper_choice\"]].sort_values(\"choice_real\", ascending=False).round(4).to_string())\n\"\"\", [\"claim:sc-choice-fraction\"])\nmd(\"**Result: see below.**\")\n\nmd(r\"\"\"\n## Population trajectories (traj-latency-visual, traj-latency-late)\n\"\"\")\ncode(r\"\"\"\nt0 = time.time()\ntraj_res = {}\nfor k, region in enumerate(TRAJ):\n    sess = []\n    for aid, g in sel[sel.region == region].groupby(\"asset_id\"):\n        e = by_asset[aid]\n        cols = np.isin(e[\"traj_units\"], g.unit.values)\n        t = e[\"trials\"]\n        a = t.analysed.values\n        sess.append((e[\"traj\"][a][:, cols], t.side.values[a], t.p_left.values[a], t.choice.values[a]))\n    traj_res[region] = bwm.trajectory(sess, bwm.N_PERM_TRAJ, np.random.default_rng(3000 + k))\ntraj_df = pd.DataFrame({r: {k: v for k, v in d.items() if k != \"d\"} for r, d in traj_res.items()}).T\nfor c in (\"latency\", \"latency_70\", \"latency_70_bin_start\"):\n    traj_df[c] = (traj_df[c].astype(float) * 1000).round(1)\nprint(f\"Trajectories of {len(TRAJ)} regions with {bwm.N_PERM_TRAJ} permutations in {time.time() - t0:.0f} s\")\nprint(\"latency_70: first time above 70% of the range (Methods); latency: also significant point-wise (code); ms on the code's axis\")\nprint(traj_df.to_string())\nfig, ax = plt.subplots(figsize=(6, 3.5))\nfor r, d in traj_res.items():\n    ax.plot(bwm.TRAJ_TIMES * 1000, d[\"d\"], label=r)\nax.set_xlabel(\"time from stimulus onset (ms)\")\nax.set_ylabel(\"distance (spikes/s)\")\nax.legend(fontsize=7)\nprint(\"Plotted distances range from 0 to\", round(max(d[\"d\"].max() for d in traj_res.values()), 2))\n\"\"\")\n\nmd(r\"\"\"\n## traj-latency-visual\n\n> The latency of the stimulus trajectory separation ordered the visual regions as LGd < VISp, which is\n> about equal to LP, < VISpm < VISam, at about 34, 42, 42, 57 and 78 ms.\n\"\"\")\ncode(r\"\"\"\nexp = {\"LGd\": 34, \"VISp\": 42, \"LP\": 42, \"VISpm\": 57, \"VISam\": 78}\nfor col in (\"latency_70\", \"latency\"):\n    L = traj_df[col].astype(float)\n    order = (L[\"LGd\"] < min(L[\"VISp\"], L[\"LP\"]) and max(L[\"VISp\"], L[\"LP\"]) < L[\"VISpm\"] < L[\"VISam\"]\n             and abs(L[\"VISp\"] - L[\"LP\"]) <= 10)\n    within = {r: bool(abs(L[r] - v) <= 0.1 * v) for r, v in exp.items()}\n    print(f\"{col:11s}\", {r: L[r] for r in exp}, \"order holds:\", order, \"within 10%:\", within)\nprint(\"Significance of the distance (permutation p):\", traj_df.loc[list(exp), \"p\"].to_dict())\n\"\"\", [\"claim:traj-latency-visual\"])\nmd(\"**Result: see below.**\")\n\nmd(r\"\"\"\n## traj-latency-late\n\n> The early visual wave was followed by later stimulus encoding in the MRN, SCm, PRNr, IRN and GRN,\n> with latencies of about 100 to 120 ms.\n\"\"\")\ncode(r\"\"\"\nfor r in (\"IRN\", \"GRN\"):\n    d = traj_df.loc[r]\n    print(f\"{r}: latency (Methods) {d.latency_70} ms, with significance (code) {d.latency} ms, distance p = {d.p:.3g}, \"\n          f\"{int(d.n_cells)} cells; in 90 to 132 ms: {90 <= d.latency_70 <= 132}\")\n\"\"\", [\"claim:traj-latency-late\"])\nmd(\"**Result: see below.**\")\n\nmd(r\"\"\"\n## fback-oscillation-licking\n\n> During reward delivery, activity showed coherent oscillations of about 10 Hz that were missing after\n> negative feedback and were closely related to licking.\n\"\"\")\ncode(r\"\"\"\nrows = []\nlick_by_asset = {s[\"asset_id\"]: np.sort(s[\"licks\"]) for s in scans}\nfor aid, g in sel[sel.region == \"IRN\"].groupby(\"asset_id\"):\n    e = by_asset[aid]\n    t = e[\"trials\"]\n    pop = e[\"psth\"].mean(0)          # 2 x bins: correct, incorrect\n    f_c, p_c, freqs = bwm.spectrum_peak(pop[0], bwm.PSTH_BIN)\n    _, p_i, _ = bwm.spectrum_peak(pop[1], bwm.PSTH_BIN)\n    band = np.abs(freqs - f_c) <= 1\n    lk = lick_by_asset[aid]\n    fb = t.feedback_time[t.analysed & t.correct].values\n    edges = fb[:, None] + np.arange(0, bwm.PSTH_POST, bwm.PSTH_BIN)[None, :]\n    lick_psth = bwm.window_counts(lk, edges, bwm.PSTH_BIN).mean(0) / bwm.PSTH_BIN if len(lk) else np.full(edges.shape[1], np.nan)\n    f_l = bwm.spectrum_peak(lick_psth, bwm.PSTH_BIN)[0] if len(lk) else np.nan\n    rows.append({\"session\": aid[:8], \"units\": len(g), \"peak_correct_hz\": f_c, \"power_correct\": p_c[band].sum(),\n                 \"power_incorrect\": p_i[band].sum(), \"licks\": len(lk), \"lick_peak_hz\": f_l,\n                 \"error_trials\": int((t.analysed & ~t.correct).sum())})\nosc = pd.DataFrame(rows)\nprint(osc.round(2).to_string(index=False))\nw = stats.wilcoxon(osc.power_correct, osc.power_incorrect)\nprint(f\"Median peak frequency, correct trials: {osc.peak_correct_hz.median():.2f} Hz; power at the peak higher on correct trials in \"\n      f\"{int((osc.power_correct > osc.power_incorrect).sum())} of {len(osc)} sessions, Wilcoxon p = {w.pvalue:.2g}\")\nprint(f\"Median lick PSTH peak: {osc.lick_peak_hz.median():.2f} Hz over {int(osc.lick_peak_hz.notna().sum())} sessions with licks\")\n\"\"\", [\"claim:fback-oscillation-licking\"])\nmd(\"**Result: see below.**\")\n\nmd(r\"\"\"\n## Claims over all regions (blocked as not runnable)\n\ntraj-stim-regions, wheel-speed-decoding, encoding-feedback-largest, video-correlates and\ngranger-interactions need every canonical region, so every session's spikes. The cost measured\nabove sets the scale.\n\"\"\")\ncode(r\"\"\"\nper_session = extract_seconds / len(extracted)\nper_decode = decode_seconds * 4 / len(dec_jobs) / 3            # CPU seconds per variable per region-session\nn_region_sessions = canon.groupby([\"region\", \"eid\"]).ngroups\nprint(f\"Streaming the spikes of all {canon.eid.nunique()} canonical sessions at {per_session:.2f} s each: about {canon.eid.nunique() * per_session / 60:.0f} min\")\nprint(f\"Decoding one variable for all {n_region_sessions} region-sessions as here (1 run, 100 nulls with reused C): about \"\n      f\"{n_region_sessions * per_decode / 4 / 60:.0f} min on 4 processes; with the paper's 10 runs and 200 nested-search nulls the \"\n      f\"null fits alone grow by more than 10 x 2 x 35 times\")\nprint(f\"Total run time of this notebook so far: {(time.time() - started) / 60:.1f} min of the 30 min limit\")\n\"\"\")\n\nmd(r\"\"\"\n## Summary\n\nFilled in after the run.\n\"\"\")\n\nnb = nbf.v4.new_notebook()\nnb.cells = cells\nnb.metadata[\"kernelspec\"] = {\"name\": \"python3\", \"display_name\": \"Python 3\", \"language\": \"python\"}\nnbf.write(nb, \"entries/000409-ibl-2025/reproduce_ibl_2025.ipynb\")\nprint(len(cells))\n"
}
```

```
File created successfully at: /tmp/claude-1001/dev/make_nb.py (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd  && python -c "import yaml,jsonschema,nbformat;print('ok')" && $TMPDIR/explore/bin/python -c "import nbformat" 2>&1 | tail -1; python $TMPDIR/dev/make_nb.py && printf "dandi\nh5py\nmatplotlib\nnumpy\npandas\nremfile\nrequests\nscikit-learn\nscipy\n" > entries/000409-ibl-2025/requirements.in && python tools/entry.py lock entries/000409-ibl-2025 && grep -E "^(numpy|pandas|scikit-learn|scipy|h5py|dandi|remfile)==" entries/000409-ibl-2025/requirements.lock.txt
```

```
Exit code 2
ok
ModuleNotFoundError: No module named 'nbformat'
102
usage: entry.py [-h] [--output-dir OUTPUT_DIR] [--timeout TIMEOUT]
                [--max-minutes MAX_MINUTES]
                {lock,check,run,all,handover} entry
entry.py: error: entries/000409-ibl-2025 has no entry.yaml
```

**Agent calls Write**

```json
{
 "file_path": "entries/000409-ibl-2025/entry.yaml",
 "content": "schema_version: 1\nname: 000409-ibl-2025\ntype: reproduction\ntitle: The IBL brain-wide map of neural activity (International Brain Laboratory et al. 2025)\ndescription: Tests the findings of the IBL brain-wide map paper (Nature 2025) on dandiset 000409,\n  which holds 459 sessions of Neuropixels recordings from 139 mice performing the IBL\n  decision-making task. It checks the dataset's composition and inclusion counts, the behavioural\n  results of Figure 1, and, on a fixed set of regions, the decoding of stimulus, choice and\n  feedback, single-cell selectivity, the latencies of stimulus trajectories and the feedback\n  oscillations related to licking.\nlicense: Apache-2.0\nnotebooks:\n- path: reproduce_ibl_2025.ipynb\n  title: Reproducing the IBL brain-wide map (2025) from dandiset 000409\n  runtime_minutes: 15\nhelpers:\n- bwm.py\nrelated:\n- id: dandi:000409/0.260309.1324\n  relation: uses_data\n- id: doi:10.1038/s41586-025-09235-0\n  relation: reproduces\n"
}
```

```
File created successfully at: entries/000409-ibl-2025/entry.yaml (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd  && python tools/entry.py lock entries/000409-ibl-2025 && grep -E "^(numpy|pandas|scikit-learn|scipy|h5py|dandi|remfile)==" entries/000409-ibl-2025/requirements.lock.txt && python tools/entry.py check entries/000409-ibl-2025
```

```
wrote entries/000409-ibl-2025/requirements.lock.txt
dandi==0.81.0
h5py==3.16.0
numpy==2.5.4
pandas==3.0.6
remfile==0.1.15
scikit-learn==1.9.1
scipy==1.18.1
0 error(s)
```

**Agent**

Locked and the check passes. Running the notebook from a clean environment (this streams about 170 sessions, so it takes a while).

**Agent calls Bash**

```bash
time python tools/entry.py run entries/000409-ibl-2025 2>&1 | tail -40
```

```
Installed kernelspec registry-000409-ibl-2025 in executed/000409-ibl-2025/.venv/share/jupyter/kernels/registry-000409-ibl-2025
[30;43m        [39;49m[30;43melement[39;49m[30;43m.[39;49m[30;43mreverse[39;49m[30;43m([39;49m[30;43m)[39;49m
[32m    623[39m [30;43m        [39;49m[30;43;01mwhile[39;49;00m[30;43m [39;49m[30;43melement[39;49m[30;43m:[39;49m

[36mFile [39m[32m/opt/hostedtoolcache/Python/3.13.16/x64/lib/python3.13/concurrent/futures/_base.py:625[39m, in [36mExecutor.map.<locals>.result_iterator[39m[34m()[39m
[32m    622[39m [38;5;28;01mwhile[39;00m fs:
[32m    623[39m     [38;5;66;03m# Careful not to keep a reference to the popped future[39;00m
[32m    624[39m     [38;5;28;01mif[39;00m timeout [38;5;129;01mis[39;00m [38;5;28;01mNone[39;00m:
[32m--> [39m[32m625[39m         [38;5;28;01myield[39;00m [30;43m_result_or_cancel[39;49m[30;43m([39;49m[30;43mfs[39;49m[30;43m.[39;49m[30;43mpop[39;49m[30;43m([39;49m[30;43m)[39;49m[30;43m)[39;49m
[32m    626[39m     [38;5;28;01melse[39;00m:
[32m    627[39m         [38;5;28;01myield[39;00m _result_or_cancel(fs.pop(), end_time - time.monotonic())

[36mFile [39m[32m/opt/hostedtoolcache/Python/3.13.16/x64/lib/python3.13/concurrent/futures/_base.py:318[39m, in [36m_result_or_cancel[39m[34m(***failed resolving arguments***)[39m
[32m    316[39m [38;5;28;01mtry[39;00m:
[32m    317[39m     [38;5;28;01mtry[39;00m:
[32m--> [39m[32m318[39m         [38;5;28;01mreturn[39;00m [30;43mfut[39;49m[30;43m.[39;49m[30;43mresult[39;49m[30;43m([39;49m[30;43mtimeout[39;49m[30;43m)[39;49m
[32m    319[39m     [38;5;28;01mfinally[39;00m:
[32m    320[39m         fut.cancel()

[36mFile [39m[32m/opt/hostedtoolcache/Python/3.13.16/x64/lib/python3.13/concurrent/futures/_base.py:460[39m, in [36mFuture.result[39m[34m(self, timeout)[39m
[... 22 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/000409-ibl-2025 && python - <<'E'
p='bwm.py'; s=open(p).read()
s=s.replace('''        epochs = pd.DataFrame({k: _col(f["intervals/epochs"], k)
                               for k in ("start_time", "stop_time", "protocol_type")})''','''        epochs = (pd.DataFrame({k: _col(f["intervals/epochs"], k) for k in ("start_time", "stop_time", "protocol_type")})
                  if "epochs" in f["intervals"] else pd.DataFrame({"protocol_type": ["none"]}))''')
s=s.replace('''        wheel_moves = f["processing/wheel/WheelMovementIntervals/start_time"][:]''','''        wheel_moves = (f["processing/wheel/WheelMovementIntervals/start_time"][:]
                       if "WheelMovementIntervals" in f["processing/wheel"] else np.array([]))''')
open(p,'w').write(s)
E
python - <<'E'
import nbformat
nb=nbformat.read('entries/000409-ibl-2025/reproduce_ibl_2025.ipynb',4)
src="\n\n".join(("# CELL %d\n"%i)+c.source for i,c in enumerate(nb.cells) if c.cell_type=='code')
src=src.replace("import bwm","import bwm\nimport matplotlib; matplotlib.use('Agg')")
open('/tmp/claude-1001/dev/nbscript.py','w').write("if __name__=='__main__':\n"+"\n".join("    "+l for l in src.splitlines()))
E
echo ok
```

```
Traceback (most recent call last):
  File "/opt/hostedtoolcache/Python/3.13.16/x64/lib/python3.13/site-packages/nbformat/__init__.py", line 169, in read
    buf = fp.read()
          ^^^^^^^
AttributeError: 'str' object has no attribute 'read'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
  File "/opt/hostedtoolcache/Python/3.13.16/x64/lib/python3.13/site-packages/nbformat/__init__.py", line 171, in read
    with open(fp, encoding="utf8") as f:  # noqa: PTH123
         ~~~~^^^^^^^^^^^^^^^^^^^^^
FileNotFoundError: [Errno 2] No such file or directory: 'entries/000409-ibl-2025/reproduce_ibl_2025.ipynb'
ok
```

**Agent calls Bash**

```bash
cd  && python - <<'E'
import nbformat
nb=nbformat.read('entries/000409-ibl-2025/reproduce_ibl_2025.ipynb',4)
src="\n\n".join(("# CELL %d\n"%i)+c.source for i,c in enumerate(nb.cells) if c.cell_type=='code')
src=src.replace("import bwm","import bwm\nimport matplotlib; matplotlib.use('Agg')")
open('/tmp/claude-1001/dev/nbscript.py','w').write("if __name__=='__main__':\n"+"\n".join("    "+l for l in src.splitlines()))
E
cd entries/000409-ibl-2025 && time $TMPDIR/explore/bin/python $TMPDIR/dev/nbscript.py > $TMPDIR/run1.log 2>&1; tail -30 $TMPDIR/run1.log
```

```
real	0m0.034s
user	0m0.028s
sys	0m0.006s
Traceback (most recent call last):
  File "/tmp/claude-1001/dev/nbscript.py", line 9, in <module>
    import matplotlib.pyplot as plt
ModuleNotFoundError: No module named 'matplotlib'
```

**Agent calls Bash**

```bash
cd entries/000409-ibl-2025 && uv pip install -q --python $TMPDIR/explore/bin/python matplotlib && time $TMPDIR/explore/bin/python $TMPDIR/dev/nbscript.py > $TMPDIR/run1.log 2>&1; tail -30 $TMPDIR/run1.log
```

```
/bin/bash: line 1: cd: entries/000409-ibl-2025: No such file or directory
Traceback (most recent call last):
  File "/tmp/claude-1001/dev/nbscript.py", line 9, in <module>
    import matplotlib.pyplot as plt
ModuleNotFoundError: No module named 'matplotlib'
```

**Agent calls Bash**

```bash
uv pip install -q --python $TMPDIR/explore/bin/python matplotlib && $TMPDIR/explore/bin/python -c "import matplotlib" && (time $TMPDIR/explore/bin/python $TMPDIR/dev/nbscript.py > $TMPDIR/run1.log 2>&1); tail -30 $TMPDIR/run1.log
```

```
real	0m1.501s
user	0m1.398s
sys	0m0.103s
Traceback (most recent call last):
  File "/tmp/claude-1001/dev/nbscript.py", line 15, in <module>
    import bwm
ModuleNotFoundError: No module named 'bwm'
```

**Agent calls Bash**

```bash
pwd && (time PYTHONPATH=. $TMPDIR/explore/bin/python $TMPDIR/dev/nbscript.py > $TMPDIR/run1.log 2>&1); tail -40 $TMPDIR/run1.log
```

```
entries/000409-ibl-2025

real	3m35.336s
user	0m57.705s
sys	0m4.335s
Length of the first (unbiased) block: {90: 459}
Biased block lengths, last block of each session left out: min 1 max 99 mean 6.9
Stimulus side x choice x rewarded:
correct      False   True 
side choice               
-1   -1          0  123603
      0        626       0
      1      27097       0
 1   -1      25213       0
      0        526       0
      1          0  119025
Reward volume on rewarded trials (uL): {1.5: 242628}
Quiescence period (s): range 0.4 to 0.7
Missing values: {'stim_on': 94, 'go_cue': 954, 'first_move': 3009, 'feedback_time': 199}
Trials without a response: 1152
[... 25 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && explore/bin/python - <<'E'
import pickle,os,numpy as np,pandas as pd,collections
res=pickle.load(open(os.environ['TMPDIR']+'/scanall.pkl','rb'))
t=res[3]['trials']
pl=t['probability_left']; bi=t['block_index']
print(list(zip(pl[85:140],bi[85:140])))
# quality mismatch
u=pd.concat([pd.DataFrame(r['units']) for r in res])
m=((u.median_spike_amplitude_uV>50).astype(int)+(u.noise_cutoff<20).astype(int)+(u.sliding_rp_violation==1).astype(int))/3
bad=~np.isclose(m,u.ibl_quality_score,atol=0.01)
print(bad.sum()); b=u[bad]
print(b[['ibl_quality_score','median_spike_amplitude_uV','noise_cutoff','sliding_rp_violation']].describe())
print(pd.crosstab(np.round(b.ibl_quality_score,2), np.round(m[bad],2)))
print('nan noise', u.noise_cutoff.isna().sum(), 'nan amp', u.median_spike_amplitude_uV.isna().sum())
E
```

```
Exit code 1
[(np.float64(0.5), np.int64(0)), (np.float64(0.5), np.int64(0)), (np.float64(0.5), np.int64(0)), (np.float64(0.5), np.int64(0)), (np.float64(0.5), np.int64(0)), (np.float64(0.8), np.int64(1)), (np.float64(0.8), np.int64(1)), (np.float64(0.8), np.int64(1)), (np.float64(0.8), np.int64(1)), (np.float64(0.8), np.int64(1)), (np.float64(0.8), np.int64(1)), (np.float64(0.8), np.int64(1)), (np.float64(0.8), np.int64(1)), (np.float64(0.8), np.int64(1)), (np.float64(0.8), np.int64(1)), (np.float64(0.8), np.int64(1)), (np.float64(0.8), np.int64(1)), (np.float64(0.8), np.int64(1)), (np.float64(0.8), np.int64(1)), (np.float64(0.8), np.int64(1)), (np.float64(0.8), np.int64(1)), (np.float64(0.8), np.int64(1)), (np.float64(0.8), np.int64(1)), (np.float64(0.8), np.int64(1)), (np.float64(0.8), np.int64(1)), (np.float64(0.8), np.int64(1)), (np.float64(0.8), np.int64(1)), (np.float64(0.8), np.int64(1)), (np.float64(0.8), np.int64(1)), (np.float64(0.8), np.int64(1)), (np.float64(0.8), np.int64(1)), (np.float64(0.8), np.int64(1)), (np.float64(0.8), np.int64(1)), (np.float64(0.8), np.int64(1)), (np.float64(0.8), np.int64(1)), (np.float64(0.8), np.int64(1)), (np.float64(0.8), np.int64(1)), (np.float64(0.8), np.int64(1)), (np.float64(0.8), np.int64(1)), (np.float64(0.8), np.int64(1)), (np.float64(0.8), np.int64(1)), (np.float64(0.8), np.int64(1)), (np.float64(0.8), np.int64(1)), (np.float64(0.8), np.int64(1)), (np.float64(0.8), np.int64(1)), (np.float64(0.8), np.int64(1)), (np.float64(0.8), np.int64(1)), (np.float64(0.8), np.int64(1)), (np.float64(0.8), np.int64(1)), (np.float64(0.8), np.int64(1)), (np.float64(0.8), np.int64(1)), (np.float64(0.8), np.int64(1)), (np.float64(0.8), np.int64(1)), (np.float64(0.8), np.int64(1)), (np.float64(0.8), np.int64(1))]
81334
       ibl_quality_score  ...  sliding_rp_violation
count       81334.000000  ...           81334.00000
mean            0.341887  ...               0.27644
std             0.225746  ...               0.44724
min          
[... 46 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && explore/bin/python - <<'E'
import pickle,os,numpy as np,pandas as pd,collections
res=pickle.load(open(os.environ['TMPDIR']+'/scanall.pkl','rb'))
small=[]
for r in res:
    bi=r['trials']['block_index']; pl=r['trials']['probability_left']
    l=np.bincount(bi)[1:-1]
    small.append(((l<20).sum(), len(l), np.unique(pl).tolist()))
s=pd.DataFrame(small,columns=['n_small','n_blocks','pl'])
print(s.n_small.describe(), (s.n_small>0).sum())
i=int(np.argmax(s.n_small)); r=res[i]; bi=r['trials']['block_index']; pl=r['trials']['probability_left']
print(s.iloc[i], np.bincount(bi)[:60]); print(pl[90:200])
u=pd.concat([pd.DataFrame(r['units']) for r in res],ignore_index=True)
m=((u.median_spike_amplitude_uV>50).astype(int)+(u.noise_cutoff<20).astype(int)+(u.sliding_rp_violation==1).astype(int))/3
bad=~np.isclose(m,u.ibl_quality_score,atol=0.01)
print(pd.crosstab(np.round(u.ibl_quality_score[bad],2), np.round(m[bad],2)))
b=u[bad]
for c in ['median_spike_amplitude_uV','noise_cutoff']: print(c, np.nanpercentile(b[c],[0,5,25,50,75,95,100]))
print('nan noise', u.noise_cutoff.isna().sum(), 'nan amp', u.median_spike_amplitude_uV.isna().sum())
# try amp threshold in different units / noise thresholds
for thr_amp in [50,]: 
  for thr_n in [5,10,20]:
    mm=((u.median_spike_amplitude_uV>thr_amp).astype(int)+(u.noise_cutoff<thr_n).astype(int)+(u.sliding_rp_violation==1).astype(int))/3
    print(thr_amp,thr_n,np.isclose(mm,u.ibl_quality_score,atol=.01).mean())
E
```

```
count    459.000000
mean      67.488017
std      174.841105
min        0.000000
25%        0.000000
50%        0.000000
75%        0.000000
max      805.000000
Name: n_small, dtype: float64 64
n_small                 805
n_blocks                806
pl          [0.2, 0.5, 0.8]
Name: 260, dtype: object [90 33  1  1  1  1  1  1  1  1  1  1  1  1  1  1  1  1  1  1  1  1  1  1
  1  1  1  1  1  1  1  1  1  1  1  1  1  1  1  1  1  1  1  1  1  1  1  1
  1  1  1  1  1  1  1  1  1  1  1  1]
[0.8 0.8 0.8 0.8 0.8 0.8 0.8 0.8 0.8 0.8 0.8 0.8 0.8 0.8 0.8 0.8 0.8 0.8
 0.8 0.8 0.8 0.8 0.8 0.8 0.8 0.8 0.8 0.8 0.8 0.8 0.8 0.8 0.8 0.2 0.8 0.2
 0.8 0.2 0.8 0.2 0.8 0.2 0.8 0.2 0.8 0.2 0.8 0.2 0.8 0.2 0.8 0.2 0.8 0.2
 0.8 0.2 0.8 0.2 0.8 0.2 0.8 0.2 0.8 0.2 0.8 0.2 0.8 0.2 0.8 0.2 0.8 0.2
 0.8 0.2 0.8 0.2 0.8 0.2 0.8 0.2 0.8 0.2 0.8 0.2 0.8 0.2 0.8 0.2 0.8 0.2
[... 16 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && explore/bin/python - <<'E'
import pickle,os,numpy as np,pandas as pd,collections
res=pickle.load(open(os.environ['TMPDIR']+'/scanall.pkl','rb'))
rows=[]
for r in res:
    t=r['trials']; bi=t['block_index']; pl=t['probability_left']; side=np.array([s.decode() for s in t['gabor_stimulus_side']])
    l=np.bincount(bi)[1:-1]
    b=pl!=0.5
    match=np.mean((side[b]=='left')==(pl[b]==0.8))
    # alternative: compare with side of block runs
    rows.append(dict(path=r['info']['path'].split('/')[0],proto=r['info']['protocol'],lab=r['info'].get('lab'),start=r['info']['start'][:10],n_small=int((l<20).sum()),n_blocks=len(l),match=match, frac_one=np.mean(l==1) if len(l) else 0))
d=pd.DataFrame(rows)
print(d[d.n_small>0].sort_values('n_small').to_string())
print(d[d.n_small==0].match.describe())
E
```

```
path                           proto                 lab       start  n_small  n_blocks     match  frac_one
218      sub-PL030  _iblrig_tasks_ephysChoiceWorld          hausserlab  2022-10-08      253       254  0.569182  0.996063
234      sub-PL033  _iblrig_tasks_ephysChoiceWorld          hausserlab  2022-10-12      265       266  0.563636  0.996241
246      sub-PL033  _iblrig_tasks_ephysChoiceWorld          hausserlab  2022-11-02      278       279  0.509091  0.996416
456  sub-ZFM-04308  _iblrig_tasks_ephysChoiceWorld           mainenlab  2022-07-27      279       280  0.517572  0.996429
302  sub-ZFM-04308  _iblrig_tasks_ephysChoiceWorld           mainenlab  2022-07-26      290       291  0.521605  0.996564
148      sub-KS084  _iblrig_tasks_ephysChoiceWorld           cortexlab  2022-01-31      313       314  0.518732  0.996815
212      sub-PL030  _iblrig_tasks_ephysChoiceWorld          hausserlab  2022-10-17      321       322  0.522599  0.996894
228      sub-PL030  _iblrig_tasks_ephysChoiceWorld          hausserlab  2022-09-15      331       332  0.506527  0.996988
210      sub-PL031  _iblrig_tasks_ephysChoiceWorld          hausserlab  2022-11-19      339       340  0.544959  0.997059
248      sub-PL035  _iblrig_tasks_ephysChoiceWorld          hausserlab  2023-04-12      346       347  0.525066  0.997118
245      sub-PL034  _iblrig_tasks_ephysChoiceWorld          hausserlab  2022-10-20      357       358  0.506112  0.997207
222      sub-PL030  _iblrig_tasks_ephysChoiceWorld          hausserlab  2022-09-12      364       365  0.523929  0.997260
227      sub-PL030  _iblrig_tasks_ephysChoiceWorld          hausserlab  2022-10-13      364       365  0.548309  0.997260
225      sub-PL030  _iblrig_tasks_ephysChoiceWorld          hausserlab  2022-09-14      365       366  0.506266  0.997268
244      sub-PL033  _iblrig_tasks_ephysChoiceWorld          hausserlab  2022-11-03      367       368  0.522500  0.997283
247      sub-PL035  _iblrig_tasks_ephysChoiceWorld          ha
[... 58 more lines not kept]
```

**Agent calls Bash**

```bash
python - <<'E'
p='/tmp/claude-1001/dev/make_nb.py'; s=open(p).read()
s=s.replace('''sessions["age_weeks"] = [(st.tz_convert("UTC") - d.tz_convert("UTC")).days / 7 for st, d in zip(sessions.start, sessions.dob)]''',
'''sessions["start"] = pd.to_datetime(sessions.start, utc=True)
sessions["dob"] = pd.to_datetime(sessions.dob, utc=True)
sessions["age_weeks"] = (sessions.start - sessions.dob).dt.days / 7''')
# blocks check
s=s.replace('''blen = trials[trials.block > 0].groupby(["eid", "block"]).size()
last = trials.groupby("eid").block.max()
inner = blen[[b < last[e] for e, b in blen.index]]
print("Biased block lengths, last block of each session left out: min", inner.min(), "max", inner.max(), "mean", round(inner.mean(), 1))''',
'''biased = trials[trials.p_left != 0.5]
match = biased.groupby("eid").apply(lambda g: np.mean((g.side < 0) == (g.p_left == 0.8)), include_groups=False)
sessions["block_match"] = sessions.eid.map(match)
sessions["block_ok"] = sessions.block_match >= 0.7
BLOCK_OK = set(sessions.eid[sessions.block_ok])
print("Fraction of biased-block trials whose stimulus is on the block's likely side, per session:")
print("   sessions at or above 0.7:", len(BLOCK_OK), "range", round(match[match >= 0.7].min(), 3), "to", round(match[match >= 0.7].max(), 3))
print("   sessions below 0.7:", int((~sessions.block_ok).sum()), "range", round(match[match < 0.7].min(), 3), "to", round(match[match < 0.7].max(), 3))
bad_s = sessions[~sessions.block_ok]
print("   their protocols:", bad_s.protocol.value_counts().to_dict(), "; labs:", bad_s.lab.value_counts().to_dict(),
      "; dates", bad_s.start.min().date(), "to", bad_s.start.max().date())
print("   all sessions with that protocol name:", int((sessions.protocol == "_iblrig_tasks_ephysChoiceWorld").sum()))
blen = trials[trials.block > 0].groupby(["eid", "block"]).size()
last = trials.groupby("eid").block.max()
for name, ok in (("block_ok", True), ("other", False)):
    b = blen[[(e in BLOCK_OK) == ok and bl < last[e] for e, bl in blen.index]]
    print(f"Biased block lengths in {name} sessions, last block left out: min {b.min()}, max {b.max()}, mean {b.mean():.1f}, blocks {len(b)}")''')
s=s.replace('''The stimulus, choice and reward columns agree''','''In 64 sessions, every one recorded with the protocol named `_iblrig_tasks_ephysChoiceWorld`
without a version, `probability_left` alternates between 0.2 and 0.8 on every trial after the first
90, and the stimulus falls on the stated block's likely side on about half of the trials, as by
chance; in the other 395 sessions it does so on 80% of trials, with blocks of 20 to 100 trials as
the Methods state. The block column of those 64 sessions does not describe the blocks the mice
experienced. Analyses that need the block (Figure 1g and 1h, the single-cell tests and the
trajectory permutations) leave these sessions out; the decoding nulls are drawn from the generative
process and do not use the recorded blocks.

The stimulus, choice and reward columns agree''')
# quality
s=s.replace('''print("Units whose score equals the fraction of the three metrics they pass:",
      int(np.isclose(passes, units.ibl_quality_score, atol=0.01).sum()), "of", len(units))''','''print("Units whose score equals the fraction of the three metrics they pass, noise cutoff below 20 (Methods):",
      int(np.isclose(passes, units.ibl_quality_score, atol=0.01).sum()), "of", len(units))
passes5 = ((units.median_spike_amplitude_uV > 50).astype(int) + (units.noise_cutoff < 5).astype(int)
           + (units.sliding_rp_violation == 1).astype(int)) / 3
print("The same with a noise cutoff below 5:", int(np.isclose(passes5, units.ibl_quality_score, atol=0.01).sum()))
print("Noise cutoff: units with a value", int(units.noise_cutoff.notna().sum()), "; range", round(units.noise_cutoff.min(), 2), "to",
      round(units.noise_cutoff.max(), 1), "; well-isolated units with a cutoff of 5 or more:",
      int(((units.ibl_quality_score == 1) & (units.noise_cutoff >= 5)).sum()))''')
s=s.replace('''The quality score is the fraction of the three metrics (median amplitude above 50 uV, noise cutoff
below 20, sliding refractory-period test) for nearly all units; the exceptions are counted above.''','''The quality score is the fraction of three metrics passed (median amplitude above 50 uV, the noise
cutoff, the sliding refractory-period test) for every unit when the noise cutoff threshold is 5,
not the 20 uV the Methods give; the column's description gives it in standard deviations, not uV.''')
s=s.replace('''print("Well-isolated by recomputing the three metrics:", int((passes == 1).sum()))''','''print("Well-isolated by recomputing the three metrics: noise cutoff below 20 (Methods)", int((passes == 1).sum()),
      "; below 5", int((passes5 == 1).sum()))''')
# fig1g/h restrict
s=s.replace('''sw = t2[(t2.block >= 2) & (t2.pos <= 40) & (t2.contrast == 0) & (t2.choice != 0)]''','''sw = t2[(t2.block >= 2) & (t2.pos <= 40) & (t2.contrast == 0) & (t2.choice != 0) & t2.eid.isin(BLOCK_OK)]''')
s=s.replace('''print("Mice with 0% trials at position 1:", int(mouse_curve[1].notna().sum()), "; 0% trials in the curve:", len(sw))''','''print("Mice with 0% trials at position 1:", int(mouse_curve[1].notna().sum()), "; 0% trials in the curve:", len(sw),
      "; sessions with valid blocks:", len(BLOCK_OK))''')
s=s.replace('''rb = resp[resp.p_left != 0.5]''','''rb = resp[(resp.p_left != 0.5) & resp.eid.isin(BLOCK_OK)]''')
s=s.replace('''print("Contrasts with a higher right-block fraction (median > 0 and p < 0.05):", int(((bias.median_diff > 0) & (bias.p < 0.05)).sum()), "of 9")''','''print("Contrasts with a higher right-block fraction (median > 0 and p < 0.05):", int(((bias.median_diff > 0) & (bias.p < 0.05)).sum()), "of 9",
      "; mice:", rb.subject.nunique(), "; sessions with valid blocks:", rb.eid.nunique())
allb = resp[resp.p_left != 0.5].assign(right=lambda d: d.choice > 0).groupby(["subject", "p_left", "signed_contrast"]).right.mean().unstack("p_left")
d_all = (allb[0.2] - allb[0.8]).unstack("signed_contrast")
print("Variant with all sessions, median difference by contrast:", d_all.median().round(3).to_dict())''')
# single-cell exclude
s=s.replace('''    for k, (aid, t, c) in enumerate(region_counts(region, ("stim", "choice"))):
        sc_jobs.append''','''    for k, (aid, t, c) in enumerate(region_counts(region, ("stim", "choice"))):
        if t_eid[aid] not in BLOCK_OK:
            continue
        sc_jobs.append''')
s=s.replace('''sc = bwm.run_parallel(bwm.single_cell_job, sc_jobs, workers=4)''','''sc = bwm.run_parallel(bwm.single_cell_job, sc_jobs, workers=4)
left_out = sel[~sel.eid.isin(BLOCK_OK)]
print(f"Left out for invalid blocks: {left_out.groupby(['region', 'eid']).ngroups} region-sessions, {len(left_out)} units")''')
s=s.replace('''by_asset = {e["asset_id"]: e for e in extracted}''','''by_asset = {e["asset_id"]: e for e in extracted}
t_eid = dict(zip(processed.asset_id, sessions.eid))''')
s=s.replace('''    for aid, g in sel[sel.region == region].groupby("asset_id"):
        e = by_asset[aid]
        cols = np.isin(e["traj_units"], g.unit.values)''','''    for aid, g in sel[sel.region == region].groupby("asset_id"):
        if t_eid[aid] not in BLOCK_OK:
            continue
        e = by_asset[aid]
        cols = np.isin(e["traj_units"], g.unit.values)''')
s=s.replace('''print(f"Trajectories of {len(TRAJ)} regions''','''print("Sessions left out for invalid blocks:", {r: int(sel[(sel.region == r) & ~sel.eid.isin(BLOCK_OK)].eid.nunique()) for r in TRAJ})
print(f"Trajectories of {len(TRAJ)} regions''')
open(p,'w').write(s)
E
grep -n "t_eid\|BLOCK_OK" /tmp/claude-1001/dev/make_nb.py | head -20
```

```
203:BLOCK_OK = set(sessions.eid[sessions.block_ok])
205:print("   sessions at or above 0.7:", len(BLOCK_OK), "range", round(match[match >= 0.7].min(), 3), "to", round(match[match >= 0.7].max(), 3))
214:    b = blen[[(e in BLOCK_OK) == ok and bl < last[e] for e, bl in blen.index]]
569:sw = t2[(t2.block >= 2) & (t2.pos <= 40) & (t2.contrast == 0) & (t2.choice != 0) & t2.eid.isin(BLOCK_OK)]
579:      "; sessions with valid blocks:", len(BLOCK_OK))
606:rb = resp[(resp.p_left != 0.5) & resp.eid.isin(BLOCK_OK)]
651:t_eid = dict(zip(processed.asset_id, sessions.eid))
802:        if t_eid[aid] not in BLOCK_OK:
806:left_out = sel[~sel.eid.isin(BLOCK_OK)]
876:        if t_eid[aid] not in BLOCK_OK:
887:print("Sessions left out for invalid blocks:", {r: int(sel[(sel.region == r) & ~sel.eid.isin(BLOCK_OK)].eid.nunique()) for r in TRAJ})
```

**Agent calls Bash**

```bash
python - <<'E'
p='claims/000409/10.1038-s41586-025-09235-0.yaml'; s=open(p).read()
s=s.replace("""# the data, beyond timing one session to plan the run.
#""","""# the data, beyond timing one session to plan the run.
#
# The data check found that in 64 sessions (all with the protocol name _iblrig_tasks_ephysChoiceWorld
# without a version) probability_left alternates between 0.2 and 0.8 on every trial after the first
# 90 and does not follow the stimuli. The claims that use the block (fig1g-block-switch,
# fig1h-block-bias, the single-cell tests and the trajectory permutations) leave these sessions out.
#""")
open(p,'w').write(s)
E
python $TMPDIR/dev/make_nb.py && python - <<'E'
import nbformat
nb=nbformat.read('entries/000409-ibl-2025/reproduce_ibl_2025.ipynb',4)
src="\n\n".join(("# CELL %d\n"%i)+c.source for i,c in enumerate(nb.cells) if c.cell_type=='code')
src=src.replace("import bwm","import bwm, pickle\nimport matplotlib; matplotlib.use('Agg')")
src=src.replace("scans = bwm.run_parallel(bwm.scan_session, list(processed.asset_id))","""import os.path
if os.path.exists('/tmp/claude-1001/scancache.pkl'): scans = pickle.load(open('/tmp/claude-1001/scancache.pkl','rb'))
else:
    scans = bwm.run_parallel(bwm.scan_session, list(processed.asset_id)); pickle.dump(scans, open('/tmp/claude-1001/scancache.pkl','wb'))""")
open('/tmp/claude-1001/dev/nbscript.py','w').write("if __name__=='__main__':\n"+"\n".join("    "+l for l in src.splitlines()))
E
cd entries/000409-ibl-2025 && (time PYTHONPATH=. $TMPDIR/explore/bin/python $TMPDIR/dev/nbscript.py > $TMPDIR/run1.log 2>&1); tail -60 $TMPDIR/run1.log
```

```
102

real	10m4.727s
user	20m19.738s
sys	0m25.533s
VISam     338       0.0385          0.02
PVT        77       0.0260          0.00
ACAv      187       0.0214          0.01
LP       1621       0.0173          0.01
VISp      707       0.0141          0.02
VISpm     225       0.0133          0.00
LGd       533       0.0094          0.01
HATA       58       0.0000          0.00
PA        106       0.0000          0.00
TR         35       0.0000          0.00
Sessions left out for invalid blocks: {'LGd': 2, 'VISp': 6, 'LP': 6, 'VISpm': 1, 'VISam': 1, 'IRN': 2, 'GRN': 0}
Trajectories of 7 regions with 1000 permutations in 10 s
latency_70: first time above 70% of the range (Methods); latency: also significant point-wise (code); ms on the code's axis
       n_cells        amp         p  latency  latency_70  latency_70_bin_start
LGd      533.0   3.561931  0.000999     31.7        31.7                  31.0
[... 45 more lines not kept]
```

**Agent**

The full analysis runs end to end in about 10 minutes, plus about 3 minutes for the scan. Reading the complete output.

**Agent calls Bash**

```bash
sed -n 1,200p $TMPDIR/run1.log
```

```
dandiset 000409 version 0.260309.1324: 2048 assets; scanned 459 processed files in 210 s
                                    eid      subject       lab sex                       dob                            start  weight_g                             protocol    revision  n_trials  n_kept  n_analysed  n_units  n_good  n_probes  age_weeks
0  3e7ae7c0-fe8b-487c-9354-036236fa1010  CSH_ZAD_001  zadorlab   F 2019-04-16 04:00:00+00:00 2020-01-16 20:53:21.500926+00:00     22.37  _iblrig_tasks_ephysChoiceWorld6.2.5  2025-05-06       854     854         406      519      50         1  39.285714
1  03cf52f6-fba6-4743-a42e-dd1ac3072343  CSH_ZAD_011  zadorlab   F 2019-09-17 04:00:00+00:00        2020-03-22 16:56:40+00:00     20.27  _iblrig_tasks_ephysChoiceWorld6.4.0  2025-05-06       415     415         305     1341     119         2  26.714286
2  5b44c40f-80f4-44fb-abfb-c7f19e27a6ca  CSH_ZAD_011  zadorlab   F 2019-09-17 04:00:00+00:00        2020-03-21 18:17:23+00:00     20.27  _iblrig_tasks_ephysChoiceWorld6.4.0  2025-05-06       591     591         437     1927     134         2  26.571429
3  da188f2c-553c-4e04-879b-c9ea2d1b9a93  CSH_ZAD_011  zadorlab   F 2019-09-17 04:00:00+00:00        2020-03-23 16:58:00+00:00     20.27  _iblrig_tasks_ephysChoiceWorld6.4.0  2025-05-06       927     927         676     2019     205         2  26.857143
4  49e0ab27-827a-4c91-bcaa-97eea27a1b8d  CSH_ZAD_019  zadorlab   F 2019-11-12 05:00:00+00:00        2020-08-18 11:41:02+00:00     23.00  _iblrig_tasks_ephysChoiceWorld6.4.1  2025-05-06       884     884         576     1689     141         2  40.000000
Assets by kind: {'raw': 459, 'processed': 459, 'VideoLeftCamera': 437, 'VideoRightCamera': 433, 'VideoBodyCamera': 260}
Sessions with a processed and a raw file: 459 of 459
Sessions: 459 ; subjects: 139 ; labs: 12
Sessions per lab: {'hausserlab': 62, 'danlab': 46, 'mainenlab': 44, 'cortexlab': 42, 'churchlandlab_ucla': 41, 'angelakilab': 41, 'zadorlab': 37, 'wittenlab': 37, 'churchlandlab':
[... 189 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 200,330p $TMPDIR/run1.log | grep -v "ConvergenceWarning\|warnings.warn"
```

```
IRN   choice        27    0.0000  0.1800        0.7182            22         True          0.17               True
   LDT   choice         2    0.0154  0.1300        0.6422             1        False          0.15               True
    PA   choice         7    0.4679 -0.0165        0.4960             1        False         -0.02              False
   PVT   choice         5    0.0413  0.0161        0.5221             1        False          0.03              False
    TR   choice         3    0.4482  0.0072        0.5161             0        False          0.02              False
  VISp   choice        35    0.0000  0.0423        0.5612            15         True          0.06               True
  ACAv feedback        11    0.0000  0.0510        0.5664             6         True          0.09               True
    CL feedback         2    0.0010  0.2672        0.7666             2         True          0.25               True
   GRN feedback        14    0.0000  0.4071        0.9161            14         True          0.42               True
  HATA feedback         5    0.0255  0.0025        0.5048             2        False          0.04               True
   IRN feedback        27    0.0000  0.4066        0.9052            25         True          0.42               True
   LDT feedback         2    0.0010  0.3045        0.8071             2         True          0.32               True
    PA feedback         7    0.1455  0.0000        0.5000             2        False         -0.01              False
   PVT feedback         5    0.0008  0.0888        0.5960             3         True          0.04               True
    TR feedback         3    0.0227  0.0493        0.5473             1        False          0.03              False
  VISp feedback        35    0.0000  0.1133        0.6149            20         True          0.11               True
  ACAv     stim        11    0.5467  0.0079        0.5160             0        False          0.01              Fal
[... 114 more lines not kept]
```

**Agent calls Bash**

```bash
python - <<'E'
p='bwm.py'; s=open(p).read()
s=s.replace('''import os
from concurrent.futures import ProcessPoolExecutor
''','''import os
import warnings
from concurrent.futures import ProcessPoolExecutor
''')
s=s.replace('''from sklearn.linear_model import LogisticRegression
''','''from sklearn.exceptions import ConvergenceWarning
from sklearn.linear_model import LogisticRegression
''')
s=s.replace('''def _fit_predict(Xtr, ytr, Xte, C):
    if len(np.unique(ytr)) < 2:
        return np.full(len(Xte), ytr[0])
    return _logreg(C).fit(Xtr, ytr).predict(Xte)''','''FITS = {"fits": 0, "not_converged": 0}   # per process; reset and reported by each job


def _fit_predict(Xtr, ytr, Xte, C):
    if len(np.unique(ytr)) < 2:
        return np.full(len(Xte), ytr[0])
    with warnings.catch_warnings(record=True) as caught:
        warnings.simplefilter("always", ConvergenceWarning)
        m = _logreg(C).fit(Xtr, ytr)
    FITS["fits"] += 1
    FITS["not_converged"] += any(issubclass(w.category, ConvergenceWarning) for w in caught)
    return m.predict(Xte)''')
s=s.replace('''    key, t, counts, seed = job
    rng = np.random.default_rng(seed)
    n = len(t)
    model = fit_action_kernel(t[t.analysed])''','''    key, t, counts, seed = job
    FITS.update(fits=0, not_converged=0)
    rng = np.random.default_rng(seed)
    n = len(t)
    model = fit_action_kernel(t[t.analysed])''')
s=s.replace('''        out[var] = {"n_trials": int(rows.sum()), "n_minor": int(min(np.bincount(y, minlength=2))),
                    "n_null": len(nulls), **res}
    return out''','''        out[var] = {"n_trials": int(rows.sum()), "n_minor": int(min(np.bincount(y, minlength=2))),
                    "n_null": len(nulls), **res}
    out["fits"], out["not_converged"] = FITS["fits"], FITS["not_converged"]
    return out''')
# trajectory canonical window
s=s.replace('''    sig_ups = ups[ps[ups] < 0.05]
    return {"n_cells": n_cells, "d": M[0], "amp": float(amp[0]), "p": float(np.mean(amp >= amp[0])),
            "latency": float(TRAJ_TIMES[sig_ups[0]]) if len(sig_ups) else np.nan,
            "latency_70": float(TRAJ_TIMES[ups[0]]),
            "latency_70_bin_start": float(traj_starts(np.zeros(1))[0, ups[0]])}''','''    sig_ups = ups[ps[ups] < 0.05]
    # The code's canonical window: the first 48 points, on the axis linspace(0, 0.1, 48).
    Mc = dist[:, :48] - dist[:, :48].min(1, keepdims=True)
    psc = np.mean(Mc >= Mc[0], axis=0)
    upc = np.where(Mc[0] > 0.7 * Mc[0].max())[0]
    sig_c = upc[psc[upc] < 0.05]
    return {"n_cells": n_cells, "d": M[0], "amp": float(amp[0]), "p": float(np.mean(amp >= amp[0])),
            "latency": float(TRAJ_TIMES[sig_ups[0]]) if len(sig_ups) else np.nan,
            "latency_70": float(TRAJ_TIMES[ups[0]]),
            "latency_70_bin_start": float(traj_starts(np.zeros(1))[0, ups[0]]),
            "latency_canonical": float(np.linspace(0, 0.1, 48)[sig_c[0]]) if len(sig_c) else np.nan}''')
open(p,'w').write(s)

p='/tmp/claude-1001/dev/make_nb.py'; s=open(p).read()
s=s.replace('''j0 = int(np.where(bwm.CLOCK_OFFSETS == 0)[0][0])
jump = acc[:, j0] - acc[:, j0 - 1]
print(f"Window 0 to 0.2 s minus window -0.2 to 0 s: median {np.nanmedian(jump):.3f}; above 0.05 in {int(np.sum(jump > 0.05))} of {int(ok.sum())} sessions")''','''post = np.nanmean(acc[:, bwm.CLOCK_OFFSETS >= 0], 1)
pre = np.nanmean(acc[:, bwm.CLOCK_OFFSETS <= -0.4], 1)
jump = post - pre
print(f"Mean accuracy of the windows from feedback on (0, 0.2, 0.4 s) minus those starting 1.0 to 0.4 s before: median {np.nanmedian(jump):.3f}; "
      f"above 0.05 in {int(np.sum(jump > 0.05))} of {int(ok.sum())} sessions")
print("Units per session in these sessions:", int(np.median([len(e["units"]) for e in extracted])), "median")''')
s=s.replace('''In nearly every session, feedback becomes decodable in the window that starts at feedback and not
before, and shifting the labels by one trial removes it, so the spike times share the clock of the
trials table. The sessions where this could not be established are listed above.''','''Feedback becomes decodable in the windows from feedback on and not in the windows before it, and
shifting the labels by one trial removes it, so the spike times share the clock of the trials table
in the sessions where the jump is clear. In the sessions listed above it could not be established
with the units loaded here; for them the shared clock is consistent with the data but not shown.''')
s=s.replace('''dec_df = pd.DataFrame(rows)
print(f"{len(dec_jobs)} region-sessions decoded''','''dec_df = pd.DataFrame(rows)
print(f"Logistic fits: {sum(d['fits'] for d in dec)}; not converged within 20000 iterations: {sum(d['not_converged'] for d in dec)}")
print(f"{len(dec_jobs)} region-sessions decoded''')
s=s.replace('''print(region_res.round(4).sort_values(["var", "region"]).to_string(index=False))''','''print(region_res.round(4).sort_values(["var", "region"]).to_string(index=False))
for q in (0.01, 0.05):
    print(f"Variant, BH at q = {q}:", {v: int(bwm.bh(g.p_fisher.values, q).sum()) for v, g in region_res.groupby("var")},
          "; Fisher p < 0.01 uncorrected:", {v: int((g.p_fisher < 0.01).sum()) for v, g in region_res.groupby("var")})
subj_of = dict(zip(processed.asset_id, sessions.subject))
per = dec_df[dec_df.region.isin(EXAMPLES)].assign(subject=lambda d: d.asset_id.map(subj_of))
print("Per session, example regions (score and p), by mouse:")
print(per.pivot_table(index=["region", "subject", "asset_id"], columns="var", values=["score", "p"]).round(3).droplevel(2).to_string())''')
s=s.replace('''pv = dec_df[dec_df["var"] == "stim"].groupby("region").p.apply(lambda p: bwm.fisher_p(p))
print("Variant, Fisher p < 0.01 without the correction:", int((pv < 0.01).sum()), "regions")''','')
s=s.replace('''for col in ("latency_70", "latency"):''','''for col in ("latency_70", "latency", "latency_canonical"):''')
s=s.replace('''for c in ("latency", "latency_70", "latency_70_bin_start"):''','''for c in ("latency", "latency_70", "latency_70_bin_start", "latency_canonical"):''')
s=s.replace('''print("latency_70: first time above 70% of the range (Methods); latency: also significant point-wise (code); ms on the code's axis")''','''print("latency_70: first time above 70% of the range (Methods); latency: also significant point-wise (code); ms on the code's axis;")
print("latency_canonical: the code's canonical 0 to 100 ms window with significance")''')
s=s.replace('''print("Significance of the distance (permutation p):", traj_df.loc[list(exp), "p"].to_dict())''','''print("Significance of the distance (permutation p):", traj_df.loc[list(exp), "p"].to_dict())
paper_tab = pd.read_pickle(io.BytesIO(requests.get(f"{REPO}/brainwidemap/meta/Results/stim.pkl", timeout=60).content))
print("The paper's results table meta/Results/stim.pkl, euclidean_latency (ms):",
      (paper_tab.set_index("region").loc[list(exp) + ["IRN", "GRN"], "euclidean_latency"] * 1000).round(1).to_dict())''')
open(p,'w').write(s)
E
grep -n "latency_canonical\|stim.pkl\|not_converged" /tmp/claude-1001/dev/make_nb.py | head
```

```
707:print(f"Logistic fits: {sum(d['fits'] for d in dec)}; not converged within 20000 iterations: {sum(d['not_converged'] for d in dec)}")
896:for c in ("latency", "latency_70", "latency_70_bin_start", "latency_canonical"):
901:print("latency_canonical: the code's canonical 0 to 100 ms window with significance")
920:for col in ("latency_70", "latency", "latency_canonical"):
927:paper_tab = pd.read_pickle(io.BytesIO(requests.get(f"{REPO}/brainwidemap/meta/Results/stim.pkl", timeout=60).content))
928:print("The paper's results table meta/Results/stim.pkl, euclidean_latency (ms):",
```

**Agent calls Bash**

```bash
cd  && python $TMPDIR/dev/make_nb.py && python - <<'E'
import nbformat
nb=nbformat.read('entries/000409-ibl-2025/reproduce_ibl_2025.ipynb',4)
src="\n\n".join(("# CELL %d\n"%i)+c.source for i,c in enumerate(nb.cells) if c.cell_type=='code')
src=src.replace("import bwm","import bwm, pickle\nimport matplotlib; matplotlib.use('Agg')")
src=src.replace("scans = bwm.run_parallel(bwm.scan_session, list(processed.asset_id))","""import os.path
if os.path.exists('/tmp/claude-1001/scancache.pkl'): scans = pickle.load(open('/tmp/claude-1001/scancache.pkl','rb'))
else:
    scans = bwm.run_parallel(bwm.scan_session, list(processed.asset_id)); pickle.dump(scans, open('/tmp/claude-1001/scancache.pkl','wb'))""")
open('/tmp/claude-1001/dev/nbscript.py','w').write("if __name__=='__main__':\n"+"\n".join("    "+l for l in src.splitlines()))
E
cd entries/000409-ibl-2025 && (time PYTHONPATH=. $TMPDIR/explore/bin/python $TMPDIR/dev/nbscript.py > $TMPDIR/run2.log 2>&1); grep -v "ConvergenceWarning\|warnings.warn" $TMPDIR/run2.log | sed -n '/Streamed/,$p' | head -150
```

```
102

real	6m41.338s
user	19m36.325s
sys	0m22.656s
Streamed 168 sessions, 222 million spikes of 5609 units, in 104 s (0.62 s per session with 8 processes)
Units whose spike times were not sorted: 0
Balanced accuracy of feedback decoding by window start relative to feedback (s), median over sessions:
{-1.0: 0.518, -0.8: 0.515, -0.6: 0.514, -0.4: 0.536, -0.2: 0.548, -0.0: 0.651, 0.2: 0.716, 0.4: 0.726}
Mean accuracy of the windows from feedback on (0, 0.2, 0.4 s) minus those starting 1.0 to 0.4 s before: median 0.177; above 0.05 in 152 of 168 sessions
Units per session in these sessions: 28 median
Labels shifted by one trial, window 0 to 0.2 s: median 0.536
Sessions where the jump is not established: ['sub-ibl-witten-29', 'sub-NR-0024', 'sub-NR-0024', 'sub-ibl-witten-27', 'sub-SWC-060', 'sub-SWC-052', 'sub-KS023', 'sub-CSH-ZAD-011', 'sub-CSHL049', 'sub-ibl-witten-26', 'sub-MFD-08', 'sub-UCLA037', 'sub-KS046', 'sub-NR-0028', 'sub-UCLA034', 'sub-MFD-05']
Logistic fits: 226440; not converged within 20000 iterations: 6
111 region-sessions decoded in 227 s; null sessions per decoding: 100 to 100; learning rates of the action-kernel model: {0.02: 6, 0.05: 1, 0.1: 3, 0.15: 5, 0.2: 18, 0.3: 33, 0.4: 22, 0.5: 11, 0.7: 12}
region      var  sessions  p_fisher  effect  median_score  sessions_p05  significant  paper_effect  paper_significant
  ACAv   choice        11    0.0000  0.0760        0.5817             7         True          0.07               True
    CL   choice         2    0.0010  0.2467        0.7598             2         True          0.25               True
   GRN   choice        14    0.0000  0.2774        0.8214            14         True          0.28               True
  HATA   choice         5    0.0133  0.0234        0.5316             1        False          0.02              False
[... 135 more lines not kept]
```

**Agent calls Bash**

```bash
grep -v "ConvergenceWarning\|warnings.warn" $TMPDIR/run2.log | sed -n '/Region-sessions with balanced/,$p' | grep -v "^ *[A-Z][A-Za-z]* *[0-9.]* *[0-9.]* *[0-9.]* *[0-9.]*$" | head -80
```

```
Region-sessions with balanced accuracy above 0.9: 23 of 111; median accuracy 0.662
Spearman correlation of effects with the paper's: SignificanceResult(statistic=np.float64(0.9573348703109935), pvalue=np.float64(1.3767647149143998e-05))
VISp  stim     nested null: median 0.518, 95th pct 0.575; reused C: median 0.508, 95th pct 0.531
VISp  choice   nested null: median 0.499, 95th pct 0.574; reused C: median 0.524, 95th pct 0.567
VISp  feedback nested null: median 0.514, 95th pct 0.584; reused C: median 0.512, 95th pct 0.565
GRN   stim     nested null: median 0.554, 95th pct 0.622; reused C: median 0.559, 95th pct 0.598
GRN   choice   nested null: median 0.526, 95th pct 0.577; reused C: median 0.524, 95th pct 0.577
GRN   feedback nested null: median 0.506, 95th pct 0.564; reused C: median 0.509, 95th pct 0.561
IRN   stim     nested null: median 0.529, 95th pct 0.562; reused C: median 0.525, 95th pct 0.564
IRN   choice   nested null: median 0.529, 95th pct 0.555; reused C: median 0.531, 95th pct 0.584
IRN   feedback nested null: median 0.498, 95th pct 0.559; reused C: median 0.517, 95th pct 0.569
Left out for invalid blocks: 19 region-sessions, 381 units
5228 units in 200 region-sessions, in 15 s
        stim_real  choice_real  stim_null  choice_null  units  paper_stim  paper_choice
region                                                                                 
ACAv       0.0000       0.0214     0.0000       0.0053    187        0.00          0.01
CL         0.0588       0.3529     0.0000       0.0000     17        0.04          0.30
GRN        0.0162       0.2198     0.0036       0.0054    555        0.01          0.21
HATA       0.0000       0.0000     0.0000       0.0000     58        0.00          0.00
IRN        0.0056       0.1379     0.0014       0.0000    718        0.00          0.13
[... 60 more lines not kept]
```

**Agent**

Found one reproducibility issue: liblinear shuffles with the global random state, so decoding numbers moved slightly between runs. Fixing the seed, then running in the clean environment.

**Agent calls Bash**

```bash
cd  && sed -i 's/    return LogisticRegression(C=C, l1_ratio=1.0, solver="liblinear", tol=1e-3, max_iter=20000,\n                              class_weight="balanced")/X/' entries/000409-ibl-2025/bwm.py && python - <<'E'
p='entries/000409-ibl-2025/bwm.py'; s=open(p).read()
old='''    return LogisticRegression(C=C, l1_ratio=1.0, solver="liblinear", tol=1e-3, max_iter=20000,
                              class_weight="balanced")'''
assert old in s
s=s.replace(old,'''    return LogisticRegression(C=C, l1_ratio=1.0, solver="liblinear", tol=1e-3, max_iter=20000,
                              class_weight="balanced", random_state=0)''')
open(p,'w').write(s)
E
python $TMPDIR/dev/make_nb.py && python tools/entry.py check entries/000409-ibl-2025 && (time python tools/entry.py run entries/000409-ibl-2025 2>&1 | tail -5)
```

```
102
0 error(s)
Installed kernelspec registry-000409-ibl-2025 in executed/000409-ibl-2025/.venv/share/jupyter/kernels/registry-000409-ibl-2025
pass  reproduce_ibl_2025.ipynb  (628 s)

real	10m35.749s
user	21m41.136s
sys	0m30.497s
```

**Agent**

The notebook passes in a clean environment in 10.5 minutes. Extracting its outputs to write the conclusions.

**Agent calls Bash**

```bash
python - <<'E' > $TMPDIR/exec1.txt
import nbformat
nb=nbformat.read('executed/000409-ibl-2025/reproduce_ibl_2025.ipynb',4)
for i,c in enumerate(nb.cells):
    if c.cell_type!='code': continue
    tags=c.metadata.get('tags',[])
    print(f"=== cell {i} {tags}")
    for o in c.get('outputs',[]):
        if o.get('output_type')=='stream': print(o['text'])
        elif 'data' in o and 'text/plain' in o['data']: print(o['data']['text/plain'][:300])
        elif o.get('output_type')=='error': print('ERROR',o['ename'],o['evalue'])
E
wc -l $TMPDIR/exec1.txt; diff <(grep -v "ConvergenceWarning\|warnings.warn" $TMPDIR/run2.log) $TMPDIR/exec1.txt | grep "^[<>]" | grep -v "=== cell" | head -80
```

```
524 /tmp/claude-1001/exec1.txt
< dandiset 000409 version 0.260309.1324: 2048 assets; scanned 459 processed files in 3 s
> dandiset 000409 version 0.260309.1324: 2048 assets; scanned 459 processed files in 208 s
> 
> 
> 
> 
> 
> 
> 
> 
> 
> 
> 
> 
> 
> 
> 
> 
> 
[... 61 more lines not kept]
```

**Agent calls Bash**

```bash
grep -v "^$" $TMPDIR/exec1.txt | grep -v "^ *\(GRN\|IRN\|VISp\)\? *[A-Za-z_0-9-]* *0\.[0-9]* *0\.[0-9]* *0\.[0-9]* *0\.[0-9]* *0\.[0-9]* *0\.[0-9]*$" | sed -n '/cell 19/,$p' | head -230
```

```
(Bash completed with no output)
```

**Agent calls Bash**

```bash
grep -n "=== cell" $TMPDIR/exec1.txt | head -60
```

```
1:=== cell 1 []
4:=== cell 2 []
12:=== cell 4 ['sanity']
24:=== cell 6 ['sanity']
30:=== cell 8 ['sanity']
64:=== cell 10 ['sanity']
74:=== cell 12 ['sanity']
79:=== cell 14 ['sanity']
83:=== cell 17 ['claim:dataset-sessions-mice-labs']
86:=== cell 20 ['claim:dataset-probes-units']
89:=== cell 23 ['claim:well-isolated-neurons']
93:=== cell 26 ['claim:canonical-regions']
105:=== cell 29 ['claim:brain-areas-279']
109:=== cell 32 ['claim:mice-sex']
112:=== cell 35 ['claim:mice-age-weight']
121:=== cell 38 ['claim:probe-versions']
124:=== cell 41 ['claim:trials-per-session']
127:=== cell 45 ['claim:behav-performance']
133:=== cell 48 ['claim:behav-zero-contrast']
138:=== cell 51 ['claim:behav-early-movements']
[... 19 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 112,240p $TMPDIR/exec1.txt | grep -v "^$" | grep -v "^[0-9][0-9]*  *0\.[0-9]*$"; sed -n 242,260p $TMPDIR/exec1.txt; sed -n 359,524p $TMPDIR/exec1.txt | grep -v "^$" | grep -v "^ *\(GRN\|IRN\|VISp\)\? *[A-Za-z_0-9-]\+ \+0\.[0-9]\+ \+0\.[0-9]\+ \+[0-9.]\+ \+0\.[0-9]\+ \+0\.[0-9]\+ \+0\.[0-9]\+$"
```

```
=== cell 35 ['claim:mice-age-weight']
a: first session  age_weeks min   13.1 max   63.1 mean  28.09 median  26.00  within 10%: [np.True_, np.False_, np.False_, np.True_]  (n = 139)
a: first session  weight_g  min   16.1 max   36.2 mean  24.19 median  24.00  within 10%: [np.True_, np.True_, np.True_, np.True_]  (n = 139)
b: last session   age_weeks min   13.3 max   65.9 mean  28.86 median  26.29  within 10%: [np.True_, np.False_, np.False_, np.True_]  (n = 139)
b: last session   weight_g  min   16.1 max   36.2 mean  24.19 median  24.00  within 10%: [np.True_, np.True_, np.True_, np.True_]  (n = 139)
c: every session  age_weeks min   13.1 max   65.9 mean  28.53 median  26.00  within 10%: [np.True_, np.False_, np.False_, np.True_]  (n = 459)
c: every session  weight_g  min   16.1 max   36.2 mean  24.32 median  24.10  within 10%: [np.True_, np.True_, np.True_, np.True_]  (n = 459)
Paper's code (meta/mice_info.py) takes age_weeks and reference_weight from the IBL database, not from the recording day.
=== cell 38 ['claim:probe-versions']
{'3B2 (PRB_1_4_0480_1)': 586, '3A (NP1010)': 109, '2.x (NP2010)': 4} (paper 3A 109, 3B2 586, 2.4 4)
=== cell 41 ['claim:trials-per-session']
mean 645.1 (645), median 601 (602), range 401 to 1525 (401 to 1,525)
=== cell 45 ['claim:behav-performance']
a: mice, all trials        mean 80.76%, s.d. 5.12, s.e.m. 0.43 (n = 139)  within 81.4 +/- 0.4: False
b: mice, analysed trials   mean 84.62%, s.d. 5.40, s.e.m. 0.46 (n = 139)  within 81.4 +/- 0.4: False
c: sessions, all trials    mean 81.58%, s.d. 5.29, s.e.m. 0.25 (n = 459)  within 81.4 +/- 0.4: True
d: all trials pooled       81.94%  within 81.4 +/- 0.4: False
=== cell 48 ['claim:behav-zero-contrast']
a: all trials        mean 58.26%, s.d. 4.95, s.e.m. 0.42 (n = 139); t138 = 19.68, P = 6.9e-42; mean within 0.4: False, t within 2.02: True
b: analysed trials   mean 59.29%, s.d. 6.76, s.e.m. 0.57 (n = 139); t138 = 16.21, P = 9.3e-34; mean within 0.4: False, t within 2.02: False
[... 225 more lines not kept]
```

**Agent calls Bash**

```bash
grep -c 'md("\*\*Result: see below.\*\*")' $TMPDIR/dev/make_nb.py
```

```
16
```

**Agent calls Write**

```json
{
 "file_path": "/tmp/claude-1001/dev/results.py",
 "content": "RESULTS = [\n# mice-age-weight\nr\"\"\"\n**Result: partially reproduced.** Weight holds under every reading: per mouse at the first session\n16.1 to 36.2 g, mean 24.19 and median 24.00, all within 10% of the paper's values. The files give\neach mouse one weight for all its sessions, so this is not a weight measured on each recording day.\nAge does not hold: at the first session the mice were 13.1 to 63.1 weeks old (mean 28.09, median\n26.00), and no reading comes near the paper's maximum of 178 weeks or mean of 44.96 (at most 65.9\nand 28.86). The paper's code takes age from the IBL database, not from the recording day, which may\nexplain the difference.\n\"\"\",\n# behav-performance\nr\"\"\"\n**Result: reproduced.** Under reading (c), the mean over sessions, 81.58% of trials are correct,\nwithin 81.4 +/- 0.4. The mean over mice is 80.76% over all trials and 84.62% over analysed trials,\nboth outside the tolerance, and all trials pooled give 81.94%. Across mice the s.d. is 5.12 and the\ns.e.m. 0.43, so the paper's +/- 0.4 matches an s.e.m., not the s.d. it states.\n\"\"\",\n# behav-zero-contrast\nr\"\"\"\n**Result: partially reproduced.** Mice are above chance at 0% contrast. Over all trials the mean over\n139 mice is 58.26% (s.e.m. 0.42), t138 = 19.68, P = 6.9e-42, and the t statistic is within its\ntolerance; the mean is 0.44 points below the paper's 58.7, just outside the 0.4 tolerance. Over\nanalysed trials the mean is 59.29% and t138 = 16.21. Neither reading puts both values within\ntolerance.\n\"\"\",\n# behav-early-movements\nr\"\"\"\n**Result: reproduced.** 22.75% of all 296,090 trials have a first movement time under 80 ms\n(reading a), against the paper's 22.8%; reading (b) gives 22.99% and (c) 22.49%. 12.06% of trials\nwith both times have the first movement before the stimulus onset.\n\"\"\",\n# fig1d\nr\"\"\"\n**Result: reproduced.** The median over mice of percent correct rises at every contrast step, from\n59.2% at 0% to 96.8% at 100% (higher at 100% in 139 of 139 mice, p = 1.5e-24), and the median first\nmovement time falls at every step, from 196 to 137 ms (shorter at 100% in 133 of 139 mice,\np = 5.9e-24).\n\"\"\",\n# fig1ef\nr\"\"\"\n**Result: reproduced.** In the last 50 trials of the sessions the median over mice of percent correct\non non-zero contrast trials is 80.0%, against 85.0% in trials 51 to 300 from the end (lower in 105 of\n139 mice, p = 7.9e-13), and the median first movement time is 279 against 165 ms (longer in 131 of\n139 mice, p = 2.6e-22).\n\"\"\",\n# fig1g\nr\"\"\"\n**Result: reproduced.** On 0% contrast trials after a switch between biased blocks (395 sessions\nwith valid blocks, 16,447 trials), the mean fraction correct starts at 0.338 on the first trial after\nthe switch. The fitted time constant is 3.86 trials, below the 4.5 to 11 of reading (a); the fit\ncovers 90% of the change at 9.9 trials, within reading (b). Per-mouse time constants have a median\nof 3.88 trials (interquartile 1.86 to 11.30, 125 mice).\n\"\"\",\n# fig1h\nr\"\"\"\n**Result: reproduced.** In the 395 sessions with valid blocks (125 mice), the fraction of right\nchoices is higher in right blocks than in left blocks at all nine signed contrasts, with median\ndifferences of 0.013 to 0.333 (largest at 0%) and every p below 1e-8. With all sessions included,\nthe median differences are smaller at every contrast (0.012 to 0.314).\n\"\"\",\n# dec-stim-restricted\nr\"\"\"\n**Result: reproduced.** Of the 10 tested regions, 4 are significant for stimulus side (CL, GRN, IRN\nand VISp), against 5 for choice and 7 for feedback. VISp is significant (35 sessions, Fisher p =\n1.3e-08, null-corrected balanced accuracy 0.039, the paper's table 0.02). Each tested region's\nsignificance agrees with the paper's table (10 of 10), and the effects correlate with the paper's\n(Spearman 0.91, p = 0.00025). With BH at q = 0.05 the stimulus count stays 4 while choice rises to 7\nand feedback to 9. In the variant on three example sessions, the null with the full nested search\nhas 95th percentiles of 0.555 to 0.622, against 0.531 to 0.598 with the reused C (VISp stimulus\n0.575 against 0.531), so the reused C can make the null narrower and the per-session p-values\nsmaller.\n\"\"\",\n# dec-choice-widespread\nr\"\"\"\n**Result: reproduced.** GRN is significant for choice (14 sessions, Fisher p = 6e-15, effect 0.277,\nthe paper's table 0.28), and 5 tested regions are significant for choice against 4 for stimulus, a\nmargin of one region. Significance agrees with the paper's table in 9 of 10 regions; LDT (2 sessions,\nFisher p = 0.0154) is significant in the paper and not here. The effects correlate with the paper's\n(Spearman 0.98). Here 5 of 10 regions are significant, while the paper reports 172 of 201.\n\"\"\",\n# dec-feedback-nearly-all\nr\"\"\"\n**Result: partially reproduced.** 7 of the 10 tested regions are significant for feedback, including\nIRN (27 sessions, effect 0.407, the paper's table 0.42); the criterion asks for 9. HATA (Fisher\np = 0.0255), PA (0.1455) and TR (0.0227) are not significant; the paper's table marks HATA\nsignificant and PA and TR not, so 8 of these 10 regions are significant in the paper. With BH at\nq = 0.05, 9 regions are significant. 23 of 111 region-sessions decode feedback with a balanced\naccuracy above 0.9, and the median accuracy is 0.913 in GRN and 0.905 in IRN. The effects correlate\nwith the paper's (Spearman 0.96).\n\"\"\",\n# sc-stim-fraction\nr\"\"\"\n**Result: blocked (methods underspecified).** The test ran, but the null run selects 14 of 5,228 units\n(2.7e-3, 95% interval 1.5e-3 to 4.5e-3), far above the paper's false-positive rate of 5e-5, so by the\ncriterion the procedures differ. Under the null the simple test alone passes 7.1e-3 of units and the\ncombined test 6.9%, so the two tests are not independent, as the paper's rate assumes. The fractions\nthemselves agree with the paper's table: all 14 regions are within 0.02 of it, the largest is 5.9%\n(CL, 17 units), and the visual regions LGd, VISp, VISpm and VISam lie between 2.1% and 3.8%. Pooled\nover the 14 regions the fraction is 1.82%, against 0.41% in the paper's table over all canonical\nregions; the tested regions over-represent visual areas.\n\"\"\",\n# sc-choice-fraction\nr\"\"\"\n**Result: blocked (methods underspecified).** The null run with synthetic choices selects 13 of 5,228\nunits (2.5e-3, 95% interval 1.3e-3 to 4.2e-3), far above 5e-5. Apart from that, the claimed pattern is\npresent: pooled over the 14 regions 5.64% of units are choice-selective against 1.82% for stimulus\n(270 units selective for choice only, 70 for stimulus only, p = 3.8e-29), the largest fractions are\nin CL (35%), GRN (22%) and IRN (14%), and the regional fractions correlate with the paper's (Spearman\n0.84, p = 0.00016).\n\"\"\",\n# traj-latency-visual\nr\"\"\"\n**Result: not reproduced.** The latencies (Methods' definition) are LGd 31.7, VISp 46.5, LP 48.6,\nVISpm 61.3 and VISam 59.2 ms. LGd comes first and VISp and LP are within 10 ms of each other, but\nVISam is not later than VISpm, and VISp, LP and VISam are outside 10% of the paper's 42, 42 and 78 ms.\nThe code's significance condition and its 0 to 100 ms window change the values by less than 1 ms.\nThe paper's own results table gives 34.0, 44.7, 46.8, 59.6 and 66.0 ms; for VISp, LP, VISpm and\nVISam it is closer to the values here than the text is. All five distances are significant\n(p = 0.001). 16 region-sessions with invalid blocks are left out.\n\"\"\",\n# traj-latency-late\nr\"\"\"\n**Result: reproduced.** The IRN distance reaches 70% of its range at 118.3 ms and the GRN distance at\n109.9 ms, both within 90 to 132 ms, and both distances are significant (p = 0.001). MRN, SCm and PRNr\nwere not tested.\n\"\"\",\n# fback-oscillation-licking\nr\"\"\"\n**Result: partially reproduced.** In 27 IRN sessions, the population PSTH after correct feedback has\na median peak frequency of 7.08 Hz, below the 9 to 11 Hz of the criterion. Power at each session's\npeak is higher after correct than after incorrect feedback in 20 of 27 sessions (p = 0.0042), and the\nlick PSTH peaks at a median 7.23 Hz, within 1 Hz of the neural peak. In 4 sessions the neural peak\nlies at the 4 Hz edge of the band searched.\n\"\"\",\n]\n"
}
```

```
File created successfully at: /tmp/claude-1001/dev/results.py (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
python - <<'E'
import re,sys
sys.path.insert(0,'/tmp/claude-1001/dev'); from results import RESULTS
p='/tmp/claude-1001/dev/make_nb.py'; s=open(p).read()
ph='md("**Result: see below.**")'
for r in RESULTS:
    i=s.index(ph); s=s[:i]+'md(r"""'+r+'""")'+s[i+len(ph):]
assert ph not in s
rep = {
'''Every mouse has one sex and one date of birth. The weight field holds one value per session file.''':
'''Every mouse has one sex and one date of birth. The weight field holds one value per mouse, the same
in all its sessions, so it is not the weight on each recording day.''',
'''The trials' first movement times coincide with onsets in the wheel's movement intervals, and licks
rise after reward in nearly every session with licks, so the wheel and lick streams share the trials'
clock.''':
'''The trials' first movement times coincide with onsets in the wheel's movement intervals (96.8%
within 50 ms), and licks rise after reward in 407 of 442 sessions with licks, so the wheel and lick
streams share the trials' clock.''',
'''decoding, single-cell and trajectory claims are tested on a set of regions fixed in the claims file,
each with all its sessions. Claims that need every region are blocked (`not_runnable`), with the
timing that shows it at the end.''':
'''decoding, single-cell and trajectory claims are tested on a set of regions fixed in the claims file,
each with all its sessions. Five claims that need every region were not attempted (blocked, `other`);
the cost measured here is printed at the end.''',
'''| traj-stim-regions: 104 regions with stimulus trajectories | blocked, not runnable |''':'''| traj-stim-regions: 104 regions with stimulus trajectories | blocked, not attempted |''',
'''| wheel-speed-decoding: 163 of 201 regions | blocked, not runnable |''':'''| wheel-speed-decoding: 163 of 201 regions | blocked, not attempted |''',
'''| encoding-feedback-largest: correct-feedback kernel largest | blocked, not runnable |''':'''| encoding-feedback-largest: correct-feedback kernel largest | blocked, not attempted |''',
'''| video-correlates: half of neurons correlate with video | blocked, not runnable |''':'''| video-correlates: half of neurons correlate with video | blocked, not attempted |''',
'''| granger-interactions | blocked, not runnable |''':'''| granger-interactions | blocked, not attempted |''',
'''## Claims over all regions (blocked as not runnable)

traj-stim-regions, wheel-speed-decoding, encoding-feedback-largest, video-correlates and
granger-interactions need every canonical region, so every session's spikes. The cost measured
above sets the scale.''':
'''## Claims over all regions (blocked, not attempted)

traj-stim-regions, wheel-speed-decoding, encoding-feedback-largest, video-correlates and
granger-interactions need every canonical region, so every session's spikes. They were not attempted
in this notebook; the cost measured above sets the scale for a later notebook.''',
'''print(f"Total run time of this notebook so far''':'''n_traj_cells = sum(d["n_cells"] for d in traj_res.values())
print(f"Trajectories here: {n_traj_cells} cells; all {len(canon)} canonical cells would need their spikes streamed and binned in about "
      f"{len(canon) / n_traj_cells:.0f} times the {len(TRAJ)} regions' cost")
print(f"Total run time of this notebook so far''',
'''print("Passive protocol phases:", sessions.passive.value_counts().to_dict())''':'''print("Passive protocol phases:", sessions.passive.value_counts().to_dict())
print("Groups under stimulus/ (presentation, templates) in the processed files:", pd.Series([s["stimulus"] for s in scans]).value_counts().to_dict())''',
}
for a,b in rep.items():
    assert a in s, a[:60]; s=s.replace(a,b)
summary = r'''md(r"""
## Summary

A failure to reproduce here may be a failure of this attempt, not of the paper: see the reasoning and
the differences from the paper's method.

| Claim | Outcome |
|---|---|
| dataset-sessions-mice-labs | reproduced |
| dataset-probes-units | reproduced |
| well-isolated-neurons | reproduced |
| canonical-regions | reproduced |
| brain-areas-279 | reproduced |
| mice-sex | reproduced |
| mice-age-weight | partially reproduced (weight yes, age no) |
| probe-versions | reproduced |
| trials-per-session | reproduced |
| rf-mapping | blocked, data missing |
| behav-performance | reproduced (mean over sessions) |
| behav-zero-contrast | partially reproduced |
| behav-early-movements | reproduced |
| fig1d-contrast | reproduced |
| fig1ef-end-of-session | reproduced |
| fig1g-block-switch | reproduced (reading b) |
| fig1h-block-bias | reproduced |
| dec-stim-restricted | reproduced |
| dec-choice-widespread | reproduced |
| dec-feedback-nearly-all | partially reproduced |
| sc-stim-fraction | blocked, methods underspecified |
| sc-choice-fraction | blocked, methods underspecified |
| traj-latency-visual | not reproduced |
| traj-latency-late | reproduced |
| traj-stim-regions | blocked, not attempted |
| fback-oscillation-licking | partially reproduced |
| wheel-speed-decoding | blocked, not attempted |
| encoding-feedback-largest | blocked, not attempted |
| video-correlates | blocked, not attempted |
| granger-interactions | blocked, not attempted |

**How the analysis differs from the paper's.**

- The neural claims are tested on 14 regions fixed in advance (10 for decoding), each with all its
  canonical sessions, not on all 201 regions; the significance correction runs over the tested
  regions.
- Decoding uses one run of the nested cross-validation (paper 10) and 100 null sessions (paper 200),
  and each null reuses the C chosen for the real labels; on three example sessions this null is
  narrower than the full nested null.
- The synthetic sessions for choice and feedback come from an action-kernel model fitted here, with
  a logistic choice policy, in place of the companion paper's model package.
- The paper's trial mask uses saturation intervals and data revisions that are not in the dandiset;
  the mask here has the Methods' criteria and the code's truncation.
- 64 sessions whose block column does not follow the stimuli are left out of the block analyses.

**What was found about the dandiset.**

- It holds the released dataset completely: 459 sessions, 139 mice, 12 labs, 699 insertions,
  621,733 units, 75,708 well-isolated units, and every count of the paper's inclusion table.
- In 64 sessions (protocol name `_iblrig_tasks_ephysChoiceWorld` without a version)
  `probability_left`, and so `block_index` and `block_type`, alternate on every trial after the first
  90 and do not describe the blocks: the stimulus is on the stated likely side in 48% to 57% of
  trials, against 76% to 83% elsewhere.
- No session holds the receptive-field mapping phase or its stimulus.
- The quality score matches a noise cutoff below 5 for every unit; the Methods give 20 uV.
- The first movement time is described as after the go cue but precedes it in 12% of trials; the
  reward volume is 1.5 uL on every rewarded trial, where the Methods give 3 uL.
- Subject weight is one value per mouse, and the ages at recording (13.1 to 65.9 weeks) do not reach
  the paper's 178 weeks.
""")
'''
i=s.index('md(r"""\n## Summary'); j=s.index('nb = nbf.v4.new_notebook()')
s=s[:i]+summary+"\n"+s[j:]
open(p,'w').write(s)
E
python - <<'E'
p='entries/000409-ibl-2025/bwm.py'; s=open(p).read()
old='''        info["processing"] = sorted(f["processing"].keys())'''
s=s.replace(old, old+'''
        info_stim = [f"{g}/{k}" for g in ("presentation", "templates") for k in f[f"stimulus/{g}"].keys()]''')
s=s.replace('''    return {"asset_id": asset_id, "info": info, "trials": trials, "units": units, "probes": probes,''','''    return {"asset_id": asset_id, "info": info, "stimulus": ",".join(info_stim) or "empty",
            "trials": trials, "units": units, "probes": probes,''')
open(p,'w').write(s)
E
python $TMPDIR/dev/make_nb.py && python tools/entry.py check entries/000409-ibl-2025
```

```
102
0 error(s)
```

**Agent calls Bash**

```bash
sed -i 's/the stimulus is on the stated likely side in 48% to 57% of/the stimulus is on the stated likely side in 47.5% to 57% of/' $TMPDIR/dev/make_nb.py && grep -c "47.5% to 57%" $TMPDIR/dev/make_nb.py && python $TMPDIR/dev/make_nb.py && python tools/entry.py all entries/000409-ibl-2025 2>&1 | tail -4
```

```
1
102
Installed kernelspec registry-000409-ibl-2025 in executed/000409-ibl-2025/.venv/share/jupyter/kernels/registry-000409-ibl-2025
0 error(s)
pass  reproduce_ibl_2025.ipynb  (625 s)
```

**Agent calls Bash**

```bash
python - <<'E' > $TMPDIR/exec2.txt
import nbformat
nb=nbformat.read('executed/000409-ibl-2025/reproduce_ibl_2025.ipynb',4)
for i,c in enumerate(nb.cells):
    if c.cell_type!='code': continue
    print(f"=== cell {i} {c.metadata.get('tags',[])}")
    for o in c.get('outputs',[]):
        if o.get('output_type')=='stream': print(o['text'])
        elif o.get('output_type')=='error': print('ERROR',o['ename'],o['evalue'])
E
diff <(grep -v "^$" $TMPDIR/exec1.txt | grep -v "=== cell") <(grep -v "^$" $TMPDIR/exec2.txt | grep -v "=== cell")
```

```
1c1
< dandiset 000409 version 0.260309.1324: 2048 assets; scanned 459 processed files in 208 s
---
> dandiset 000409 version 0.260309.1324: 2048 assets; scanned 459 processed files in 206 s
16a17
> Groups under stimulus/ (presentation, templates) in the processed files: {'empty': 459}
158d158
< <Figure size 500x300 with 1 Axes>
175c175
< Streamed 168 sessions, 222 million spikes of 5609 units, in 103 s (0.61 s per session with 8 processes)
---
> Streamed 168 sessions, 222 million spikes of 5609 units, in 102 s (0.61 s per session with 8 processes)
184c184
< 111 region-sessions decoded in 241 s; null sessions per decoding: 100 to 100; learning rates of the action-kernel model: {0.02: 6, 0.05: 1, 0.1: 3, 0.15: 5, 0.2: 18, 0.3: 33, 0.4: 22, 0.5: 11, 0.7: 12}
---
> 111 region-sessions decoded in 240 s; null sessions per decoding: 100 to 100; learning rates of the action-kernel model: {0.02: 6, 0.05: 1, 0.1: 3, 0.15: 5, 0.2: 18, 0.3: 33, 0.4: 22, 0.5: 11, 0.7: 12}
397d396
< <Figure size 600x350 with 1 Axes>
436a436
> Trajectories here: 4697 cells; all 62857 canonical cells would need their spikes streamed and binned in about 13 times the 7 regions' cost
```

**Agent**

The final run reproduces every number exactly, and all stimulus groups are empty, which confirms the RF data are missing. Writing the README and the attempt record.

**Agent calls Write**

```json
{
 "file_path": "entries/000409-ibl-2025/README.md",
 "content": "# The IBL brain-wide map (2025) from dandiset 000409\n\nTests the findings of [International Brain Laboratory et al. (2025)](https://doi.org/10.1038/s41586-025-09235-0)\non [DANDI:000409](https://dandiarchive.org/dandiset/000409/0.260309.1324), which holds 459 sessions of\nNeuropixels recordings from 139 mice performing the IBL decision-making task.\n\n| Claim | Outcome |\n|---|---|\n| Dataset composition: sessions, mice, labs, probes, units, well-isolated units, canonical regions, brain areas, sex, probe versions, trials per session (9 claims) | Reproduced |\n| Age and weight of the mice | Partially reproduced (weight yes, age no) |\n| Receptive-field mapping | Blocked: data missing |\n| 81.4% correct; 22.8% of first movements under 80 ms | Reproduced |\n| 58.7% correct at 0% contrast, t138 = 20.18 | Partially reproduced |\n| Figure 1d to 1h: contrast, end of session, block switch, block bias | Reproduced |\n| Stimulus decodable in fewer regions, VISp | Reproduced (10 regions) |\n| Choice decodable in more regions than stimulus, GRN | Reproduced (10 regions) |\n| Feedback decodable in nearly all regions | Partially reproduced (7 of 10) |\n| Single-cell stimulus and choice selectivity | Blocked: methods underspecified (false-positive rate) |\n| Visual latencies LGd < VISp = LP < VISpm < VISam | Not reproduced |\n| Later latencies in IRN and GRN (100 to 120 ms) | Reproduced |\n| About 10 Hz feedback oscillation tied to licking | Partially reproduced (7 Hz) |\n| Whole-brain counts: trajectories, wheel speed, encoding, video, Granger (5 claims) | Blocked: not attempted |\n\nA failure to reproduce here may be a failure of this attempt, not of the paper: see the\nreasoning and the differences from the paper's method.\n\nThe neural claims are tested on a set of 14 regions fixed in advance, each with all its sessions,\nwith fewer cross-validation repeats and null sessions than the paper, to fit the time limit. In 64\nsessions the block column (`probability_left`) alternates on every trial and does not describe the\nblocks; analyses that need blocks leave these sessions out. The attempt record, with the reasons and\nthe differences from the paper's method, is\n[`attempts/000409-ibl-2025-01.yaml`](../../attempts/000409-ibl-2025-01.yaml).\n\n- `reproduce_ibl_2025.ipynb`: the analysis. It takes about 11 minutes: 3.5 to scan the 459 processed\n  files, 2 to stream the spikes of 168 sessions, 4 to decode.\n- `bwm.py`: streaming, the paper's unit and trial inclusion, decoding with pseudo- and synthetic\n  null sessions, the single-cell test and the population trajectories. Other notebooks on this\n  dandiset can import it.\n"
}
```

```
File created successfully at: entries/000409-ibl-2025/README.md (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
sed -i 's/  runtime_minutes: 15/  runtime_minutes: 11/' entries/000409-ibl-2025/entry.yaml && grep runtime entries/000409-ibl-2025/entry.yaml
```

```
runtime_minutes: 11
```

**Agent**

Now the attempt record.

**Agent calls Write**

```json
{
 "file_path": "/tmp/claude-1001/dev/attempt.py",
 "content": "import yaml\n\nNB = \"reproduce_ibl_2025.ipynb\"\nSUB = \"The tested regions are VISp, GRN, IRN and seven drawn at random (ACAv, CL, HATA, LDT, PA, PVT, TR), each with all its canonical sessions, not all 201 regions; the Benjamini-Hochberg correction runs over these 10 regions.\"\nDEC = \"One run of nested cross-validation (paper 10) and 100 null sessions (paper 200); each null reuses the C chosen for the real labels in each outer fold. On three example sessions the full nested null is wider (95th percentiles 0.555 to 0.622 against 0.531 to 0.598), so per-session p-values here can be smaller than the paper's procedure would give.\"\nSYN = \"Synthetic choices and feedback come from an action-kernel model fitted per session with a logistic choice policy, written here; the paper uses the companion paper's model package.\"\nMASK = \"The trial mask follows the Methods and the code's truncation, without the saturation intervals of the IBL aggregate trials table, which are not in the dandiset.\"\nBLOCKS = \"The 64 sessions whose probability_left alternates on every trial are left out.\"\n\n\ndef o(claim, outcome, notes, deviations=None, measured=None, blocked_by=None, output=True):\n    d = {\"claim\": claim, \"outcome\": outcome}\n    if blocked_by:\n        d[\"blocked_by\"] = blocked_by\n    if output:\n        d[\"notebook\"] = NB\n        d[\"output\"] = f\"claim:{claim}\"\n    if measured is not None:\n        d[\"measured\"] = measured\n    d[\"notes\"] = notes\n    if deviations:\n        d[\"deviations\"] = deviations\n    return d\n\n\noutcomes = [\n    o(\"dataset-sessions-mice-labs\", \"reproduced\",\n      \"The pinned version holds 459 sessions of 139 mice from 12 labs, one processed and one raw file per session.\",\n      measured=[459, 139, 12]),\n    o(\"dataset-probes-units\", \"reproduced\",\n      \"699 insertions and 621,733 units, 889.5 per probe.\", measured=[699, 621733, 889.5]),\n    o(\"well-isolated-neurons\", \"reproduced\",\n      \"75,708 units have ibl_quality_score 1, 108.3 per probe. Recomputing the three metrics gives 75,708 with a noise cutoff below 5 and 95,430 with the Methods' 20; the score matches the threshold of 5 for every unit.\",\n      measured=[75708, 108.3],\n      deviations=[\"The files hold spike sorting revision 2025-05-06; the paper's code loads revision 2024-05-06. The counts are identical.\"]),\n    o(\"canonical-regions\", \"reproduced\",\n      \"Every inclusion step gives the counts of the code's inclusion table: 75,708 well-isolated units in 268 regions, 65,336 in grey matter, 63,357 with 5 per session (245 regions), 62,990 with 2 sessions (210), and 62,857 neurons in 201 regions over 454 sessions. The region table region_info.csv marks 210 regions canonical, those left before the 20-neuron step.\",\n      measured=[201, 62857]),\n    o(\"brain-areas-279\", \"reproduced\",\n      \"Units fall in 279 Beryl regions other than void and root (266 with a well-isolated unit).\", measured=279),\n    o(\"mice-sex\", \"reproduced\", \"94 male and 45 female mice; each mouse has one sex in all its files.\", measured=[94, 45]),\n    o(\"mice-age-weight\", \"partially_reproduced\",\n      \"Weight holds under every reading (reading a gives 16.1 to 36.2 g, mean 24.19, median 24.00). Age does not under any reading. At the first session the mice were 13.1 to 63.1 weeks old, mean 28.09, median 26.00; over all sessions at most 65.9 weeks, against the paper's 178 and mean 44.96. The files give each mouse one weight for all its sessions. The paper's code takes age and reference weight from the IBL database, not from the recording day, which may explain the age difference.\",\n      measured=[13.1, 63.1, 28.09, 26.0, 16.1, 36.2, 24.19, 24.0],\n      deviations=[\"Age is session start minus date of birth in the files, which the Methods describe; the paper's code uses the database's age field. Measured values are reading (a).\"]),\n    o(\"probe-versions\", \"reproduced\",\n      \"586 insertions use PRB_1_4_0480_1 (403) or PRB_1_4_0480_1_C (183), 109 NP1010 and 4 NP2010.\",\n      measured=[109, 586, 4],\n      deviations=[\"The files name imec models, not versions; NP1010 is read as 3A (its devices have no PXI port or slot) and NP2010 as the 2.x probes. The counts match under this reading.\"]),\n    o(\"trials-per-session\", \"reproduced\", \"Mean 645.1, median 601, range 401 to 1,525 trials per session.\",\n      measured=[645.1, 601, 401, 1525]),\n    o(\"rf-mapping\", \"blocked\",\n      \"No session lists receptive-field mapping among its passive phases (428 sessions have spontaneous activity and task replay, 31 none), and the stimulus groups of all 459 processed files are empty. The raw files hold photodiode events but not the stimulus sequence. The paper used the mapping in 504 of 699 insertions.\",\n      blocked_by=\"data_missing\", output=False),\n    o(\"behav-performance\", \"reproduced\",\n      \"Reading (c), the mean over 459 sessions, gives 81.58% correct, within 81.4 +/- 0.4. The mean over mice is 80.76% (all trials) and 84.62% (analysed trials); all trials pooled give 81.94%. Across mice the s.d. is 5.12 and the s.e.m. 0.43.\",\n      measured=81.58,\n      deviations=[\"The paper does not say how the mean is taken; four readings are shown and only the mean over sessions is within tolerance.\"]),\n    o(\"behav-zero-contrast\", \"partially_reproduced\",\n      \"Over all trials the mean over 139 mice is 58.26% (s.e.m. 0.42), t138 = 19.68, P = 6.9e-42. The t statistic is within tolerance and the mean is 0.44 points below 58.7, just outside the 0.4 tolerance. Over analysed trials the mean is 59.29% and t138 = 16.21. Mice are clearly above chance; the numbers match in part.\",\n      measured=[58.26, 19.68],\n      deviations=[\"The criterion defines only the reproduced case; the outcome is partially reproduced because the effect is present and one of the two values is within tolerance.\"]),\n    o(\"behav-early-movements\", \"reproduced\",\n      \"22.75% of all 296,090 trials (reading a); 22.99% of trials with both times (b); 22.49% as a mean over sessions (c). 12.06% of trials with both times have the first movement before stimulus onset.\",\n      measured=22.75),\n    o(\"fig1d-contrast\", \"reproduced\",\n      \"Median over mice of percent correct rises at every step, 59.2% at 0% to 96.8% at 100% (higher in 139 of 139 mice, p = 1.5e-24); median first movement time falls at every step, 196 to 137 ms (shorter in 133 of 139 mice, p = 5.9e-24).\"),\n    o(\"fig1ef-end-of-session\", \"reproduced\",\n      \"Last 50 trials against trials 51 to 300 from the end, median over mice of percent correct 80.0 against 85.0 (lower in 105 of 139 mice, p = 7.9e-13), median first movement time 279 against 165 ms (longer in 131 of 139 mice, p = 2.6e-22).\"),\n    o(\"fig1g-block-switch\", \"reproduced\",\n      \"Over 395 sessions with valid blocks and 16,447 zero-contrast trials, the fraction correct starts at 0.338 after the switch. Fitted tau is 3.86 trials, outside reading (a); 90% of the change is covered at 9.9 trials, within reading (b). Per-mouse tau has a median of 3.88 (interquartile 1.86 to 11.30, 125 mice).\",\n      measured=9.9, deviations=[BLOCKS, \"The paper gives no measure of the adjustment time; two readings were fixed before the analysis and the claim holds under reading (b) only.\"]),\n    o(\"fig1h-block-bias\", \"reproduced\",\n      \"In 395 sessions with valid blocks (125 mice) the right-block fraction of right choices is higher at all nine signed contrasts, median differences 0.013 to 0.333, every p below 1e-8. With all sessions the differences are smaller at every contrast (0.012 to 0.314).\",\n      deviations=[BLOCKS]),\n    o(\"dec-stim-restricted\", \"reproduced\",\n      \"4 of 10 tested regions are significant for stimulus (CL, GRN, IRN, VISp), against 5 for choice and 7 for feedback. VISp is significant (35 sessions, Fisher p = 1.3e-08, effect 0.039, paper table 0.02). Significance agrees with region_info.csv in 10 of 10 regions and the effects correlate with the paper's (Spearman 0.91, p = 0.00025). With BH at q = 0.05 the counts are 4, 7 and 9. The paper reports 40 of 201 regions for stimulus.\",\n      deviations=[SUB, DEC, MASK]),\n    o(\"dec-choice-widespread\", \"reproduced\",\n      \"GRN is significant for choice (14 sessions, Fisher p = 6e-15, effect 0.277, paper table 0.28); 5 tested regions are significant for choice against 4 for stimulus, a margin of one region. Significance agrees with region_info.csv in 9 of 10 regions (LDT, 2 sessions, p = 0.0154, is significant in the paper). Effects correlate with the paper's (Spearman 0.98). The paper reports 172 of 201 regions.\",\n      deviations=[SUB, DEC, SYN, MASK]),\n    o(\"dec-feedback-nearly-all\", \"partially_reproduced\",\n      \"7 of 10 tested regions are significant, including IRN (27 sessions, effect 0.407, paper table 0.42); HATA (Fisher p = 0.0255), PA (0.1455) and TR (0.0227) are not. The paper's table marks 8 of these 10 significant (HATA yes, PA and TR no). With BH at q = 0.05, 9 are significant. 23 of 111 region-sessions have a balanced accuracy above 0.9; median accuracy 0.913 in GRN and 0.905 in IRN. Effects correlate with the paper's (Spearman 0.96). The partial outcome comes in part from the correction over 10 regions and the smaller null; the paper's own table has 8 of these 10 regions significant.\",\n      deviations=[SUB, DEC, SYN, MASK]),\n    o(\"sc-stim-fraction\", \"blocked\",\n      \"The test ran on 5,228 units in 200 region-sessions of 14 regions. The null run (pseudo-session sides and blocks) selects 14 units (2.7e-3, 95% interval 1.5e-3 to 4.5e-3), far above the paper's 5e-5, so by the criterion the procedures differ. Under the null the simple test alone passes 7.1e-3 and the combined test 6.9% of units. The regional fractions agree with region_info.csv (14 of 14 within 0.02; largest 5.9% in CL with 17 units; visual regions 2.1% to 3.8%), and the pooled 1.82% is above the paper's 0.41% because the tested regions over-represent visual areas. Were it not for the false-positive check the claim would be reproduced.\",\n      blocked_by=\"methods_underspecified\",\n      deviations=[BLOCKS + \" Here 19 region-sessions and 381 units.\", \"Regions are the 14 loaded for the neural claims, not all canonical regions.\", \"The paper does not state which trials enter the simple Mann-Whitney test; the same trials as the combined test are used.\"]),\n    o(\"sc-choice-fraction\", \"blocked\",\n      \"The null run with synthetic choices selects 13 of 5,228 units (2.5e-3, interval 1.3e-3 to 4.2e-3), far above 5e-5. Otherwise the pattern holds: pooled 5.64% choice-selective against 1.82% for stimulus (270 against 70 units selective for one only, p = 3.8e-29); largest fractions CL 35%, GRN 22%, IRN 14%; regional fractions correlate with the paper's (Spearman 0.84, p = 0.00016).\",\n      blocked_by=\"methods_underspecified\",\n      deviations=[BLOCKS, \"Regions are the 14 loaded for the neural claims.\", SYN]),\n    o(\"traj-latency-visual\", \"not_reproduced\",\n      \"Latencies (Methods' definition) LGd 31.7, VISp 46.5, LP 48.6, VISpm 61.3, VISam 59.2 ms. LGd is first and VISp and LP are within 10 ms, but VISam is not later than VISpm, and VISp, LP and VISam are outside 10% of 42, 42 and 78 ms. The code's significance condition and its 0 to 100 ms window change the values by less than 1 ms. The paper's results table (meta/Results/stim.pkl) gives 34.0, 44.7, 46.8, 59.6 and 66.0 ms, closer to these values than the text is for VISp, LP, VISpm and VISam, and also has VISam later than VISpm. All five distances are significant (p = 0.001).\",\n      measured=[31.7, 46.5, 48.6, 61.3, 59.2],\n      deviations=[BLOCKS + \" Here 16 region-sessions.\", \"Trials follow the mask here, without the saturation intervals the code uses.\", \"The Methods define latency as the first crossing of 70% of the range; the code adds point-wise significance. The Methods' definition decides; the code's is a variant and gives the same values here.\"]),\n    o(\"traj-latency-late\", \"reproduced\",\n      \"IRN 118.3 ms and GRN 109.9 ms, both within 90 to 132 ms, both distances significant (p = 0.001). MRN, SCm and PRNr were not tested; the paper's results table gives 89.4 ms for IRN and GRN in its 0 to 100 ms window.\",\n      measured=[118.3, 109.9],\n      deviations=[\"Only IRN and GRN of the five regions named are tested.\", BLOCKS]),\n    o(\"traj-stim-regions\", \"blocked\",\n      \"Not attempted. It needs the trajectories of all 201 regions, so the spikes of all 62,857 canonical units in 454 sessions; the notebook measures 0.61 s per session to stream the units used here and about 13 times the trajectory cost of the 4,697 cells tested. A separate notebook could test it.\",\n      blocked_by=\"other\", output=False),\n    o(\"fback-oscillation-licking\", \"partially_reproduced\",\n      \"In 27 IRN sessions the population PSTH after correct feedback peaks at a median 7.08 Hz, outside the 9 to 11 Hz of the criterion. Power at the peak is higher after correct than incorrect feedback in 20 of 27 sessions (p = 0.0042), and the lick PSTH peaks at a median 7.23 Hz, within 1 Hz of the neural peak. In 4 sessions the neural peak is at the 4 Hz edge of the band.\",\n      measured=7.08,\n      deviations=[\"Tested in IRN only, the paper's example region; the paper's analysis is a population trajectory over regions.\", \"The spectral measure (Hann-windowed spectrum of the session PSTH, 4 to 20 Hz) is chosen here; the paper describes the oscillation without a measure.\"]),\n    o(\"wheel-speed-decoding\", \"blocked\",\n      \"Not attempted. It needs Lasso decoding in 20 ms bins for all 201 regions with imposter null sessions; the notebook measures about 30 minutes to decode one binary variable for all 2,458 region-sessions with the reduced settings used here, and wheel decoding is heavier.\",\n      blocked_by=\"other\", output=False),\n    o(\"encoding-feedback-largest\", \"blocked\",\n      \"Not attempted. The encoding model would be fitted to each of the 62,857 neurons with its leave-one-out refits, which needs every session's spikes and wheel traces.\",\n      blocked_by=\"other\", output=False),\n    o(\"video-correlates\", \"blocked\",\n      \"Not attempted. It needs video pose and pupil series and every session's spikes; pose is present in 407 of 459 sessions.\",\n      blocked_by=\"other\", output=False),\n    o(\"granger-interactions\", \"blocked\",\n      \"Not attempted. It needs every simultaneously recorded region pair of every session with 1,000 permutations each.\",\n      blocked_by=\"other\", output=False),\n]\n\nattempt = {\n    \"schema_version\": 1,\n    \"id\": \"000409-ibl-2025-01\",\n    \"dandiset\": \"000409\",\n    \"dandiset_version\": \"0.260309.1324\",\n    \"paper\": \"doi:10.1038/s41586-025-09235-0\",\n    \"date\": \"2026-10-17\",\n    \"entry\": \"000409-ibl-2025\",\n    \"provenance\": {\"kind\": \"agent\", \"accountable\": {\"name\": \"CatalystNeuro\"},\n                   \"agent\": {\"harness\": \"Claude Code (GitHub Actions)\", \"model\": \"claude-opus-5-5\", \"protocol\": \"pilot-7\"}},\n    \"inputs\": [\n        {\"what\": \"The paper's per-region results table brainwidemap/meta/region_info.csv (decoding effects and significance, single-cell fractions, canonical flag), used only as the paper's reported values for comparison.\",\n         \"source\": \"https://github.com/int-brain-lab/paper-brain-wide-map at commit 118fc36cb3602934466ad2c6087c2b3b441f9f1f\"},\n        {\"what\": \"The paper's inclusion counts brainwidemap/meta/inclusion_info.csv (Supplementary Table 1), used as reported values for canonical-regions.\",\n         \"source\": \"https://github.com/int-brain-lab/paper-brain-wide-map at commit 118fc36cb3602934466ad2c6087c2b3b441f9f1f\"},\n        {\"what\": \"The paper's results table brainwidemap/meta/Results/stim.pkl (trajectory latencies per region), printed as a variant reference for traj-latency-visual and traj-latency-late.\",\n         \"source\": \"https://github.com/int-brain-lab/paper-brain-wide-map at commit 118fc36cb3602934466ad2c6087c2b3b441f9f1f\"},\n    ],\n    \"outcomes\": outcomes,\n    \"findings\": [\n        {\"kind\": \"metadata_error\",\n         \"statement\": \"In 64 sessions, all with the protocol name _iblrig_tasks_ephysChoiceWorld without a version (hausserlab 48, churchlandlab_ucla 13, mainenlab 2, cortexlab 1, recorded 2022-01-31 to 2023-10-19), probability_left alternates between 0.2 and 0.8 on every trial after the first 90, so block_index and block_type change on every trial. In these sessions the stimulus falls on the stated block's likely side in 47.5% to 57% of biased trials, against 75.9% to 82.8% in the other 395 sessions, so the column does not describe the blocks the mice experienced. Analyses of the block prior cannot use these sessions.\"},\n        {\"kind\": \"data_missing\",\n         \"statement\": \"No session holds the receptive-field mapping phase or its stimulus sequence; passive phases list only spontaneous activity and task replay, and the stimulus groups are empty. The paper ran the mapping in 504 of 699 insertions (Supplementary Fig. 5).\"},\n        {\"kind\": \"paper_inconsistency\",\n         \"statement\": \"The Methods give a noise cutoff below 20 uV for a well-isolated unit, but the quality score in the files, and the paper's count of 75,708 well-isolated units, follow a noise cutoff below 5 for every unit (20 would give 95,430). The files describe the noise cutoff in standard deviations, not uV.\"},\n        {\"kind\": \"metadata_error\",\n         \"statement\": \"wheel_movement_onset_time is described as the first wheel movement after the go cue, but in 11.97% of trials it precedes the go cue (11.93% precede the stimulus onset).\"},\n        {\"kind\": \"other\",\n         \"statement\": \"reward_volume_uL is 1.5 on every one of the 242,628 rewarded trials, while the Methods state a 3 uL reward.\"},\n        {\"kind\": \"metadata_error\",\n         \"statement\": \"The units table's description refers to a 'label' column that the files do not have (the column is ibl_quality_score) and describes all units as from Neuropixels 1.0 probes, though four insertions used NP2010 probes.\"},\n        {\"kind\": \"metadata_insufficient\",\n         \"statement\": \"Subject weight is one value per mouse, identical in all its sessions, and is not described as a reference weight; the Methods give weights on the day of recording.\"},\n        {\"kind\": \"code_mismatch\",\n         \"statement\": \"The Methods give age and weight on the day of recording (13 to 178 weeks), but meta/mice_info.py and print_age_weight in the paper's code take age_weeks and reference_weight from the IBL database. From the files the ages at recording are 13.1 to 65.9 weeks. print_age_weight also prints the median weight under the label mean and the mean under the label median.\"},\n        {\"kind\": \"paper_inconsistency\",\n         \"statement\": \"The Results give 81.4 +/- 0.4% correct as mean +/- s.d.; across mice the s.d. here is 5.12 and the s.e.m. 0.43, so the 0.4 is an s.e.m.\"},\n        {\"kind\": \"other\",\n         \"statement\": \"The single-cell test's false-positive rate, which the paper sets to 0.001 x 0.05 = 5e-5 in its binomial test of regional fractions, is about 2.5e-3 to 2.7e-3 when the test is run with null labels here; the simple Mann-Whitney test alone passes 5e-3 to 7e-3 under the null. The two tests are not independent, so the stated rate understates false positives.\"},\n        {\"kind\": \"code_mismatch\",\n         \"statement\": \"region_info.csv marks 210 regions as canonical; the paper's canonical set, and the code's inclusion table, have 201 (the 9 others have fewer than 20 neurons).\"},\n        {\"kind\": \"paper_inconsistency\",\n         \"statement\": \"The Results give visual trajectory latencies of 34, 42, 42, 57 and 78 ms for LGd, VISp, LP, VISpm and VISam; the paper's own results table (meta/Results/stim.pkl) gives 34.0, 44.7, 46.8, 59.6 and 66.0 ms.\"},\n        {\"kind\": \"other\",\n         \"statement\": \"The files hold IBL spike sorting revision 2025-05-06, while the paper's code loads revision 2024-05-06; the unit and inclusion counts are identical.\"},\n    ],\n}\n\nwith open(\"attempts/000409-ibl-2025-01.yaml\", \"w\") as f:\n    yaml.safe_dump(attempt, f, sort_keys=False, width=100, allow_unicode=True)\nprint(len(outcomes))\n"
}
```

```
File created successfully at: /tmp/claude-1001/dev/attempt.py (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
python - <<'E'
p='entries/000409-ibl-2025/bwm.py'; s=open(p).read()
old='''        info["revision"] = _str(f["general/ibl_metadata/revision"])'''
s=s.replace(old, old+'''
        info["units_description"] = _str(f["units"].attrs.get("description", ""))''')
open(p,'w').write(s)
p='/tmp/claude-1001/dev/make_nb.py'; s=open(p).read()
old='''print("Units per probe: mean", round(len(units) / sessions.n_probes.sum(), 1))'''
s=s.replace(old, old+'''
descs = pd.Series([s["info"]["units_description"] for s in scans])
print("Distinct units-table descriptions:", descs.nunique(), "; first sentence:", descs.iloc[0].split(". ")[0])
print("Descriptions that mention a 'label' column:", int(descs.str.contains("'label' column").sum()), "; columns of the units table include 'label':",
      "label" in scans[0]["units"].columns)''')
open(p,'w').write(s)
p='/tmp/claude-1001/dev/attempt.py'; s=open(p).read()
s=s.replace(" The raw files hold photodiode events but not the stimulus sequence.","")
open(p,'w').write(s)
E
python $TMPDIR/dev/make_nb.py && python $TMPDIR/dev/attempt.py && python tools/entry.py all entries/000409-ibl-2025 2>&1 | tail -3
```

```
102
30
Installed kernelspec registry-000409-ibl-2025 in executed/000409-ibl-2025/.venv/share/jupyter/kernels/registry-000409-ibl-2025
0 error(s)
pass  reproduce_ibl_2025.ipynb  (624 s)
```

**Agent calls Bash**

```bash
python - <<'E' > $TMPDIR/exec3.txt
import nbformat
nb=nbformat.read('executed/000409-ibl-2025/reproduce_ibl_2025.ipynb',4)
for i,c in enumerate(nb.cells):
    if c.cell_type!='code': continue
    print(f"=== cell {i} {c.metadata.get('tags',[])}")
    for o in c.get('outputs',[]):
        if o.get('output_type')=='stream': print(o['text'])
        elif o.get('output_type')=='error': print('ERROR',o['ename'],o['evalue'])
E
diff <(grep -v "^$" $TMPDIR/exec2.txt | grep -v "=== cell") <(grep -v "^$" $TMPDIR/exec3.txt | grep -v "=== cell"); grep -n "label\|units-table" $TMPDIR/exec3.txt | head
```

```
1c1
< dandiset 000409 version 0.260309.1324: 2048 assets; scanned 459 processed files in 206 s
---
> dandiset 000409 version 0.260309.1324: 2048 assets; scanned 459 processed files in 204 s
60a61,62
> Distinct units-table descriptions: 1 ; first sentence: Spike-sorted units from Neuropixels 1.0 probes
> Descriptions that mention a 'label' column: 459 ; columns of the units table include 'label': False
184c186
< 111 region-sessions decoded in 240 s; null sessions per decoding: 100 to 100; learning rates of the action-kernel model: {0.02: 6, 0.05: 1, 0.1: 3, 0.15: 5, 0.2: 18, 0.3: 33, 0.4: 22, 0.5: 11, 0.7: 12}
---
> 111 region-sessions decoded in 239 s; null sessions per decoding: 100 to 100; learning rates of the action-kernel model: {0.02: 6, 0.05: 1, 0.1: 3, 0.15: 5, 0.2: 18, 0.3: 33, 0.4: 22, 0.5: 11, 0.7: 12}
435c437
< Decoding one variable for all 2458 region-sessions as here (1 run, 100 nulls with reused C): about 30 min on 4 processes; with the paper's 10 runs and 200 nested-search nulls the null fits alone grow by more than 10 x 2 x 35 times
---
> Decoding one variable for all 2458 region-sessions as here (1 run, 100 nulls with reused C): about 29 min on 4 processes; with the paper's 10 runs and 200 nested-search nulls the null fits alone grow by more than 10 x 2 x 35 times
74:Distinct units-table descriptions: 1 ; first sentence: Spike-sorted units from Neuropixels 1.0 probes
75:Descriptions that mention a 'label' column: 459 ; columns of the units table include 'label': False
```

**Agent calls Bash**

```bash
sed -i 's/the notebook measures about 30 minutes to decode/the notebook estimates about 29 minutes to decode/' $TMPDIR/dev/attempt.py && python $TMPDIR/dev/attempt.py && python tools/entry.py check entries/000409-ibl-2025 && python tools/entry.py handover entries/000409-ibl-2025 && ls executed/000409-ibl-2025/handover && python - <<'E'
import yaml,re
d=yaml.safe_load(open('attempts/000409-ibl-2025-01.yaml'))
from collections import Counter
print(Counter(o['outcome'] for o in d['outcomes']))
txt=open('attempts/000409-ibl-2025-01.yaml').read()+open('claims/000409/10.1038-s41586-025-09235-0.yaml').read()+open('entries/000409-ibl-2025/README.md').read()
print('emdash', '—' in txt, 'rather', 'rather' in txt.lower())
E
grep -c "rather\|—" entries/000409-ibl-2025/bwm.py entries/000409-ibl-2025/reproduce_ibl_2025.ipynb
```

```
30
0 error(s)
wrote executed/000409-ibl-2025/handover
10.1038-s41586-025-09235-0.yaml
bwm.py
reproduce_ibl_2025.ipynb
Counter({'reproduced': 17, 'blocked': 8, 'partially_reproduced': 4, 'not_reproduced': 1})
emdash False rather False
entries/000409-ibl-2025/bwm.py:0
entries/000409-ibl-2025/reproduce_ibl_2025.ipynb:0
```

**Agent calls Bash**

```bash
git status --short; python -c "
import nbformat
nb=nbformat.read('executed/000409-ibl-2025/handover/reproduce_ibl_2025.ipynb',4)
print(sum(c.source.lstrip().startswith('**Result:') for c in nb.cells), any(c.source.startswith('## Summary') for c in nb.cells), len(nb.cells))"; head -30 attempts/000409-ibl-2025-01.yaml
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
?? attempts/000409-ibl-2025-01.yaml
?? claims/000409/
?? entries/000409-ibl-2025/
?? scripts
0 False 77
schema_version: 1
id: 000409-ibl-2025-01
dandiset: 000409
dandiset_version: 0.260309.1324
paper: doi:10.1038/s41586-025-09235-0
[... 25 more lines not kept]
```

**Agent calls Bash**

```bash
sed -i 's/^dandiset: 000409$/dandiset: "000409"/' attempts/000409-ibl-2025-01.yaml && grep -n '^dandiset' attempts/000409-ibl-2025-01.yaml && python tools/entry.py check entries/000409-ibl-2025 && git check-ignore -v paper executed | head
```

```
3:dandiset: "000409"
4:dandiset_version: 0.260309.1324
0 error(s)
.gitignore:8:paper/	paper
.gitignore:6:executed/	executed
```

**Agent calls Bash**

```bash
sed -i 's/trials per session (9 claims) | Reproduced |/trials per session (8 claims) | Reproduced |/' entries/000409-ibl-2025/README.md && grep -n "8 claims" entries/000409-ibl-2025/README.md && python tools/entry.py check entries/000409-ibl-2025
```

```
9:| Dataset composition: sessions, mice, labs, probes, units, well-isolated units, canonical regions, brain areas, sex, probe versions, trials per session (8 claims) | Reproduced |
0 error(s)
```

**Agent**

I've done protocol steps 1 to 6 for dandiset 000409: the entry is `entries/000409-ibl-2025/`, the attempt record is `attempts/000409-ibl-2025-01.yaml`, and the handover package is in `executed/000409-ibl-2025/handover/`. I used the paper's full text, which is open access (CC BY 4.0); it is saved under `paper/`. I pinned 0.260309.1324, the only published version. The paper cites no DANDI version, and the draft holds the same 2,048 files. Nothing is committed.

## 1. Outcomes

| Claim | Outcome |
|---|---|
| dataset-sessions-mice-labs (459 / 139 / 12) | reproduced |
| dataset-probes-units (699 insertions, 621,733 units) | reproduced |
| well-isolated-neurons (75,708) | reproduced |
| canonical-regions (201 regions, 62,857 neurons; every inclusion step matches) | reproduced |
| brain-areas-279 | reproduced |
| mice-sex (94 male / 45 female) | reproduced |
| mice-age-weight | partially reproduced: weight matches; age at recording is 13 to 66 weeks, the paper says up to 178 |
| probe-versions (109 / 586 / 4) | reproduced |
| trials-per-session | reproduced |
| rf-mapping | blocked, data_missing |
| behav-performance (81.4% correct) | reproduced (mean over sessions, 81.58%) |
| behav-zero-contrast (58.7%, t = 20.18) | partially reproduced (58.26%, t138 = 19.68) |
| behav-early-movements (22.8% under 80 ms) | reproduced (22.75%) |
| fig1d, fig1ef, fig1g, fig1h | reproduced (fig1g only under reading b, 9.9 trials) |
| dec-stim-restricted | reproduced |
| dec-choice-widespread | reproduced (5 regions against 4 for stimulus, a margin of one) |
| dec-feedback-nearly-all | partially reproduced (7 of 10 regions significant) |
| sc-stim-fraction, sc-choice-fraction | blocked, methods_underspecified (false-positive check failed) |
| traj-latency-visual | not reproduced (VISam 59 ms is not later than VISpm 61 ms) |
| traj-latency-late | reproduced (IRN 118 ms, GRN 110 ms) |
| fback-oscillation-licking | partially reproduced (peak at 7.1 Hz, not about 10 Hz; tied to licking) |
| traj-stim-regions, wheel-speed-decoding, encoding-feedback-largest, video-correlates, granger-interactions | blocked, other (not attempted) |

In total: 17 reproduced, 4 partially reproduced, 1 not reproduced, 8 blocked.

For the decoding claims, the per-region effects here track the paper's own region table closely (Spearman 0.91 to 0.98). The two single-cell claims are blocked only by the protocol's false-positive rule. Without that rule, all 14 regional stimulus fractions are within 0.02 of the paper's table.

## 2. What was found about the dandiset

- **Complete release.** It holds every session, mouse, probe and unit the paper reports, and every count of the paper's inclusion table. No recording is deposited twice.
- **Wrong block column in 64 sessions.** These are all the sessions with the protocol name `_iblrig_tasks_ephysChoiceWorld` without a version. In them, `probability_left` (and so `block_index` and `block_type`) flips between 0.2 and 0.8 on every trial after the first 90. The stimulus falls on the stated likely side in only 47.5% to 57% of trials, against 76% to 83% in the other 395 sessions. I left these sessions out of every analysis that uses blocks.
- **No receptive-field mapping.** No session contains the mapping phase or its stimulus.
- **Quality threshold differs from the Methods.** The quality score matches a noise cutoff below 5 for every unit; the Methods say below 20 µV, which would give 95,430 well-isolated units instead of 75,708.
- **Descriptions that disagree with the data:**
  - The first-movement time is described as after the go cue, but it comes before the go cue in 12% of trials.
  - The reward is 1.5 µL on every rewarded trial; the Methods say 3 µL.
  - The units description mentions a `label` column that does not exist and calls all probes Neuropixels 1.0, though four are NP2010.
  - Weight is a single value per mouse, the same in all its sessions.
- **Inconsistencies in the paper and its code:**
  - The "± 0.4 s.d." on 81.4% correct is an s.e.m.; the s.d. across mice is 5.1.
  - The paper's code takes age from the IBL database, not the recording day, and swaps the mean and median labels for weight.
  - The paper's region table marks 210 regions canonical, not 201.
  - The paper's own results table gives different visual latencies from those in the text.
  - The single-cell null rate here is about 2.5e-3, roughly 50 times the paper's stated 5e-5, because the two tests are not independent.

## 3. Where the protocol was unclear, wrong or missing something

1. **Scale.** Nothing covers a dataset where the paper's own analysis (459 sessions, 10 cross-validation runs, 200 null sessions) cannot fit in 30 minutes. I tested a fixed set of regions, chosen in advance in the claims file, and reduced the repeats and nulls. Every reduction is recorded as a deviation.
2. **`not_runnable` versus not attempted.** `not_runnable` asks the notebook to show the analysis does not fit, but some whole-brain analyses could fit in a separate notebook. I used `other`, said "not attempted", and gave the measured cost.
3. **Claims not covered by the criterion.** fig1g had no measure in the paper, so I fixed two readings beforehand. behav-zero-contrast's criterion defined only "reproduced"; I chose partially reproduced and recorded why.
4. **What "far from the paper's rate" means.** The false-positive rule doesn't say. I fixed it in advance as the 95% interval excluding a band of one third to three times the paper's rate. The rule then blocks claims whose regional values match the paper, and the cause looks like the paper's own assumption, not a different procedure. I followed the rule and recorded a finding.
5. **The paper's per-region results tables.** It's unclear whether the tables in its repository count as outside inputs, since they are reported values, not measurements. I listed them under `inputs` and kept the claims as `data: dandiset`.
6. **Bad data found mid-way.** The protocol doesn't say what to do with data found wrong before the analysis but after the criteria were written. I amended the claims file's opening comment before running those analyses and left the 64 sessions out.
7. **Clock check with few units.** Some sessions have too few loaded units to show the shared clock; I listed the 16 such sessions, as the protocol asks.
8. **First author is a consortium.** I named the entry `000409-ibl-2025`.

## 4. Runtime and failures

The notebook runs in about 10.5 minutes (624 s in the last clean run): about 3.5 to scan the 459 processed files, 2 to stream the spikes of 168 sessions, 4 to decode. The last three clean runs gave identical numbers.

Failures during development, all fixed:
- Some files have no `epochs` group, which crashed the first run.
- Mixed time zones broke a date column under pandas 3.
- Decoding was not reproducible until I fixed the liblinear seed.

Six of 226,440 logistic fits did not converge; the notebook reports this. Nothing failed in the final run.

## End of run

101 turns, 92 minutes, result: success.
