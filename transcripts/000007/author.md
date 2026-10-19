# 000007 · author · run 39247064898

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

[... 542 more lines not kept]
```

**Agent calls Bash**

```bash
cat README.md docs/design.md; ls -la entries/001453-fouke-2025 claims/001453; cat attempts/001453-fouke-2025-01.yaml
```

```
<persisted-output>
Output too large (62.7KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/88b7bb88-935b-4feb-9f84-9ce0ac17f754/tool-results/bhr8d3747.txt

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
 "file_path": "/home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/88b7bb88-935b-4feb-9f84-9ce0ac17f754/tool-results/bhr8d3747.txt"
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
[... 826 more lines not kept]
```

**Agent calls Bash**

```bash
cat claims/001453/*.yaml | head -120; cat entries/001453-fouke-2025/{entry.yaml,requirements.in,README.md}; head -60 entries/001453-fouke-2025/omr.py; ls schemas
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
[... 226 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 847,1054p /home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/88b7bb88-935b-4feb-9f84-9ce0ac17f754/tool-results/bhr8d3747.txt | grep -n "" | sed -n 1,5p; python3 -c "import yaml;d=yaml.safe_load(open('attempts/001453-fouke-2025-01.yaml'));print(d.keys())"
```

```
1:      protocol file's assignment, under which the result would be partially reproduced.
2:  - claim: fig1c-continuous-vs-bouts
3:    agrees: true
4:    outcome: reproduced
5:    reason: Steadiness ZF 0.306 against DC 0.908, p=5e-5. It holds in the 128 to 171 Hz files only
dict_keys(['schema_version', 'id', 'dandiset', 'dandiset_version', 'paper', 'date', 'entry', 'provenance', 'inputs', 'outcomes', 'findings', 'verifications'])
```

**Agent calls Bash**

```bash
python3 - <<'E'
import json
nb=json.load(open('entries/001453-fouke-2025/reproduce_fouke_2025.ipynb'))
print(nb['metadata'])
for i,c in enumerate(nb['cells'][:8]):
    print('---',i,c['cell_type'],c['metadata'].get('tags'));print(''.join(c['source'])[:1500])
for i,c in enumerate(nb['cells']):
    print(i,c['cell_type'],c['metadata'].get('tags'), ''.join(c['source'])[:80].replace('\n',' '))
E
```

```
{'kernelspec': {'display_name': 'Python 3', 'language': 'python', 'name': 'python3'}}
--- 0 markdown None
# Reproducing Fouke et al. (2025) from dandiset 001453

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

[... 179 more lines not kept]
```

**Agent calls Bash**

```bash
wc -l tools/entry.py; grep -n "def \|fail\|error(" tools/entry.py | head -120
```

```
396 tools/entry.py
28:that takes longer than --max-minutes fails, even if it ran without error.
68:    def __init__(self):
71:    def error(self, where, message: str) -> None:
75:def schema(name: str) -> Draft202012Validator:
79:def load(report: Report, path: Path):
84:        report.error(path.relative_to(ROOT), f"not valid YAML: {e}")
88:def validate(report: Report, path: Path, schema_name: str) -> dict | None:
94:        report.error(path.relative_to(ROOT), f"{where}: {err.message}")
98:def _plain(value):
109:def code_of(notebook_path: Path) -> str:
116:def check(entry_dir: Path) -> Report:
123:        report.error(rel / "entry.yaml", f"name {entry.get('name')!r} must match the directory name")
128:        report.error(rel / name, "notebook is not listed in entry.yaml")
130:        report.error(rel / "entry.yaml", f"listed notebook {name!r} does not exist")
134:            report.error(rel / "entry.yaml", f"listed helper {name!r} does not exist")
138:        report.error(rel, "no requirements.in")
140:        report.error(rel, "no requirements.lock.txt; run `tools/entry.py lock`")
147:                report.error(rel / "requirements.lock.txt", f"{name} is required but not locked; re-run lock")
155:            report.error(rel / "entry.yaml", "an orientation or reproduction entry must relate to a dandiset")
[... 33 more lines not kept]
```

**Agent**

Now the paper. Nature 2018 (Gao et al.); likely PMC author manuscript available.

**Agent calls Bash**

```bash
mkdir -p paper; curl -s "https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.1038/s41586-018-0633-x&format=json&resultType=core" | python3 -c "import json,sys;d=json.load(sys.stdin);r=d['resultList']['result'][0];print(r.get('pmcid'),r.get('isOpenAccess'),r.get('title'),r.get('authorString'), r.get('inEPMC'))"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd paper; curl -s "https://www.ebi.ac.uk/europepmc/webservices/rest/PMC6212318/fullTextXML" -o gao2018.xml; ls -la; python3 - <<'E'
import re,html
x=open('gao2018.xml').read()
t=re.sub(r'<xref[^>]*>(.*?)</xref>',r'\1',x)
t=re.sub(r'</(p|title|caption|sec|label)>','\n',t)
t=re.sub(r'<[^>]+>','',t); t=html.unescape(t)
t=re.sub(r'\n\s*\n+','\n\n',t)
open('gao2018.txt','w').write(t); print(len(t))
E
```

Result: the fetched text is not kept.

**Agent calls Read**

```json
{
 "file_path": "paper/gao2018.txt"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/gao2018.txt",
 "offset": 133,
 "limit": 300
}
```

Result: not kept, because it reads the paper's text.

**Agent**

Full text is available (PMC6212318 author manuscript). Now the dandiset.

**Agent calls Bash**

```bash
cd  curl -s https://api.dandiarchive.org/api/dandisets/000007/versions/ | python3 -m json.tool | head -60
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
V=0.220126.1903; curl -s "https://api.dandiarchive.org/api/dandisets/000007/versions/$V/" > $TMPDIR/meta.json; python3 -c "
import json;d=json.load(open('$TMPDIR/meta.json'))
for k in ['description','assetsSummary','relatedResource','citation','wasGeneratedBy','about','keywords','license','contributor']:
  print(k, json.dumps(d.get(k),indent=0)[:2500])"; curl -s "https://api.dandiarchive.org/api/dandisets/000007/versions/$V/assets/?page_size=200" | python3 -c "
import json,sys;d=json.load(sys.stdin);print(d['count'])
for a in d['results']: print(a['asset_id'],a['path'],a['size'])"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR && uv venv -q explore && . explore/bin/activate && uv pip install -q dandi pynwb remfile h5py numpy pandas scipy 2>&1 | tail -2; python -c "import pynwb,dandi;print(pynwb.__version__,dandi.__version__)"
```

```
4.2.0 0.81.0
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cat > $TMPDIR/open1.py <<'E'
import sys, remfile, h5py, pynwb
from dandi.dandiapi import DandiAPIClient
path=sys.argv[1]
with DandiAPIClient() as c:
    a=c.get_dandiset("000007","0.220126.1903").get_asset_by_path(path)
    url=a.get_content_url(follow_redirects=1, strip_query=True)
f=h5py.File(remfile.File(url),'r')
def show(name,obj):
    if isinstance(obj,h5py.Dataset): print(name, obj.shape, obj.dtype, dict(obj.attrs).get('unit',''), dict(obj.attrs).get('description','')[:100] if isinstance(dict(obj.attrs).get('description',''),str) else '')
    else:
        at={k:v for k,v in obj.attrs.items() if k not in('namespace','object_id')}
        print(name+'/', at)
f.visititems(show)
E
. $TMPDIR/explore/bin/activate; python $TMPDIR/open1.py sub-BAYLORCD12/sub-BAYLORCD12_ses-20180125T191601.nwb
```

```
acquisition/ {}
analysis/ {}
file_create_date (1,) object  
general/ {}
general/devices/ {}
general/devices/Cambridge NeuroTech 64ch H2 probe/ {'neurodata_type': 'Device'}
general/devices/fiber/ {'neurodata_type': 'Device'}
general/experiment_description () object  
general/experimenter (1,) object  
general/extracellular_ephys/ {}
general/extracellular_ephys/Cambridge NeuroTech 64ch H2 probe_g1/ {'description': 'N/A', 'location': '{"probe_type": "Cambridge NeuroTech 64ch H2 probe", "rec_coordinate_ap": "2.5", "rec_coordinate_ml": "-1.5", "rec_coordinate_dv": "None", "ground_coordinate_ap": "-3.0", "ground_coordinate_ml": "-1.0", "ground_coordinate_dv": "1.0", "rec_marker": "stereotaxic", "spike_sorting_method": "manual", "ad_unit": "14 bits", "coordinate_ref": "lambda", "penetration_num": "1"}', 'neurodata_type': 'ElectrodeGroup'}
general/extracellular_ephys/electrodes/ {'colnames': array(['x', 'y', 'z', 'imp', 'location', 'filtering', 'group',
       'group_name'], dtype=object), 'description': 'metadata about extracellular electrodes', 'neurodata_type': 'DynamicTable'}
general/extracellular_ephys/electrodes/filtering (64,) object  description of hardware filtering
general/extracellular_ephys/electrodes/group (64,) object  a reference to the ElectrodeGroup this electrode is a part of
general/extracellular_ephys/electrodes/group_name (64,) object  the name of the ElectrodeGroup this electrode is a part of
general/extracellular_ephys/electrodes/id (64,) int64  
general/extracellular_ephys/electrodes/imp (64,) float64  the impedance of the channel
general/extracellular_ephys/electrodes/location (64,) object  the location of channel within the subject e.g. brain region
general/extracellular_ephys/electrodes/x (64,) float64  the x coordinate of the channel location
[... 75 more lines not kept]
```

**Agent calls Bash**

```bash
cat > $TMPDIR/dump.py <<'E'
import sys, remfile, h5py, numpy as np, pandas as pd, collections
from dandi.dandiapi import DandiAPIClient
V="0.220126.1903"
with DandiAPIClient() as c:
    ds=c.get_dandiset("000007",V)
    urls={a.path:a.get_content_url(follow_redirects=1, strip_query=True) for a in ds.get_assets() if a.path in sys.argv[1:]}
def s(x):
    x=x[()]; return x.decode() if isinstance(x,bytes) else x
for p,u in urls.items():
    f=h5py.File(remfile.File(u),'r'); print("=====",p)
    for k in ['session_description','identifier','session_start_time','general/experiment_description','general/institution','general/virus','general/subject/subject_id','general/subject/genotype','general/subject/sex','general/subject/species','general/subject/date_of_birth','general/experimenter','general/keywords','general/related_publications']:
        if k in f: print(k,'=',s(f[k]))
    for g in f['general/optogenetics']:
        print('opto',g,{k:s(f['general/optogenetics'][g][k]) for k in f['general/optogenetics'][g]})
    for g in f['general/extracellular_ephys']:
        if g!='electrodes': print('group',g,dict(f['general/extracellular_ephys'][g].attrs)['location'])
    e=f['general/extracellular_ephys/electrodes']
    print('electrode location', collections.Counter([x.decode() if isinstance(x,bytes) else x for x in e['location'][:]]), 'xyz', e['x'][:3],e['y'][:3],e['z'][:3], 'imp', e['imp'][:3], 'filt', e['filtering'][0])
    t=f['intervals/trials']
    df=pd.DataFrame({k:[x.decode() if isinstance(x,bytes) else x for x in t[k][:]] for k in t.attrs['colnames']})
    print(df.head(3).to_string()); print(df.describe().to_string())
    print(df.response.value_counts().to_dict(), df.photo_stim_id.value_counts().to_dict(), df.lick_early.value_counts().to_dict(), df.session_directory.unique()[:3])
    u=f['units']
    print('cell_type',collections.Counter([x.decode() if isinstance(x,bytes) else x for x in u['cell_type'][:]]),'sr',np.unique(u['sampling_rate'][:]),'n units',len(u['id']))
    st=u['spike_times'][:]; print('spike range',st.min(),st.max(), 'trial range', df.start_time.min(), df.stop_time.max(), 'obs', u['obs_intervals'][:3])
    for gp in ['acquisition','processing','stimulus/presentation','analysis']:
        print(gp, list(f[gp].keys()))
E
. $TMPDIR/explore/bin/activate; python $TMPDIR/dump.py sub-BAYLORCD12/sub-BAYLORCD12_ses-20180125T191601.nwb sub-anm00314756/sub-anm00314756_ses-20151020T194211.nwb sub-BAYLORNL14/sub-BAYLORNL14_ses-20170602T114550.nwb 2>&1 | grep -v Warn
```

```
===== sub-anm00314756/sub-anm00314756_ses-20151020T194211.nwb
session_description = 
identifier = anm00314756_2015-10-20 19:42:11
session_start_time = 2015-10-20T19:42:11+00:00
general/experiment_description = Extracelluar recording in ALM
general/institution = Janelia Research Campus
general/virus = [{"virus": "AAV2-hSyn-hChR2(H134R)-EYFP", "brain_location": "Dentate", "hemisphere": "right", "injection_date": "2015-08-25", "injection_volume": "150.0", "injection_coordinate_ap": "-2.3", "injection_coordinate_ml": "2.5", "injection_coordinate_dv": "2.4", "coordinate_ref": "lambda", "virus_source": "UNC", "virus_lot_number": ""}]
general/subject/subject_id = anm00314756
general/subject/genotype = unknown
general/subject/sex = M
general/subject/species = Mus musculus
general/subject/date_of_birth = 2015-06-30T00:00:00+00:00
general/experimenter = [b'Nuo Li']
general/keywords = [b'motor planning' b'anterior lateral cortex' b'ALM'
 b'Extracellular recording' b'optogenetics']
general/related_publications = [b'https://www.nature.com/articles/s41586-018-0633-x']
Traceback (most recent call last):
  File "/tmp/claude-1001/dump.py", line 14, in <module>
    print('opto',g,{k:s(f['general/optogenetics'][g][k]) for k in f['general/optogenetics'][g]})
                      ~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[... 12 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR; sed -i "s/print('opto',g,{k:s(f\['general\/optogenetics'\]\[g\]\[k\]) for k in f\['general\/optogenetics'\]\[g\]})/og=f['general\/optogenetics'][g]; print('opto',g,{k:s(og[k]) for k in og if isinstance(og[k],h5py.Dataset)}, list(og.keys()))/" dump.py; . explore/bin/activate; python dump.py sub-BAYLORCD12/sub-BAYLORCD12_ses-20180125T191601.nwb sub-anm00314756/sub-anm00314756_ses-20151020T194211.nwb sub-BAYLORNL14/sub-BAYLORNL14_ses-20170602T114550.nwb 2>&1 | grep -v Warn
```

```
===== sub-anm00314756/sub-anm00314756_ses-20151020T194211.nwb
session_description = 
identifier = anm00314756_2015-10-20 19:42:11
session_start_time = 2015-10-20T19:42:11+00:00
general/experiment_description = Extracelluar recording in ALM
general/institution = Janelia Research Campus
general/virus = [{"virus": "AAV2-hSyn-hChR2(H134R)-EYFP", "brain_location": "Dentate", "hemisphere": "right", "injection_date": "2015-08-25", "injection_volume": "150.0", "injection_coordinate_ap": "-2.3", "injection_coordinate_ml": "2.5", "injection_coordinate_dv": "2.4", "coordinate_ref": "lambda", "virus_source": "UNC", "virus_lot_number": ""}]
general/subject/subject_id = anm00314756
general/subject/genotype = unknown
general/subject/sex = M
general/subject/species = Mus musculus
general/subject/date_of_birth = 2015-06-30T00:00:00+00:00
general/experimenter = [b'Nuo Li']
general/keywords = [b'motor planning' b'anterior lateral cortex' b'ALM'
 b'Extracellular recording' b'optogenetics']
general/related_publications = [b'https://www.nature.com/articles/s41586-018-0633-x']
opto Dentate {'description': '', 'excitation_lambda': np.float64(473.0), 'location': '{"brain_location": "Dentate", "hemisphere": "right", "coordinate_ref": "lambda", "photo_stim_coordinate_ap": "-2.3", "photo_stim_coordinate_ml": "2.5", "photo_stim_coordinate_dv": "2.4"}'} ['description', 'device', 'excitation_lambda', 'location']
group NN 32ch A4x8-5mm-100-200-177_g1 {"probe_type": "NN 32ch A4x8-5mm-100-200-177", "rec_coordinate_ap": "2.5", "rec_coordinate_ml": "-1.5", "rec_coordinate_dv": "None", "ground_coordinate_ap": "-3.0", "ground_coordinate_ml": "-1.0", "ground_coordinate_dv": "1.0", "rec_marker": "stereotaxic", "spike_sorting_method": "manual", "ad_unit": "14 bits", "coordinate_ref": "lambda", "penetration_num": "1"}
electrode location Counter({'ALM': 64}) xyz [nan nan nan] [nan nan nan] [nan nan nan] imp [-1. -1. -1.] filt b'Bandpass filtered 300-6K Hz'
   start_time  stop_time                            
[... 110 more lines not kept]
```

**Agent**

Files are small (54 files, 199 MB). Trial tables carry `photo_stim_id` codes without a description. Next I summarise all files.

**Agent calls Bash**

```bash
cat > $TMPDIR/summ.py <<'E'
import remfile, h5py, numpy as np, pandas as pd, collections, json
from concurrent.futures import ThreadPoolExecutor
from dandi.dandiapi import DandiAPIClient
V="0.220126.1903"
with DandiAPIClient() as c:
    ds=c.get_dandiset("000007",V)
    assets=[(a.path,a.get_content_url(follow_redirects=1, strip_query=True)) for a in ds.get_assets()]
def dec(x): return x.decode() if isinstance(x,bytes) else x
def one(pu):
    p,u=pu; f=h5py.File(remfile.File(u),'r')
    t=f['intervals/trials']; df=pd.DataFrame({k:[dec(x) for x in t[k][:]] for k in t.attrs['colnames']})
    og=f['general/optogenetics']; opto=[(g,json.loads(dec(og[g]['location'][()]))) for g in og]
    u_=f['units']; st=u_['spike_times'][:]; idx=u_['spike_times_index'][:]
    segs=np.split(st,idx[:-1]); sorted_ok=all(np.all(np.diff(s)>=0) for s in segs)
    groups=[g for g in f['general/extracellular_ephys'] if g!='electrodes']
    return dict(path=p, subj=dec(f['general/subject/subject_id'][()]), geno=dec(f['general/subject/genotype'][()]),
        virus=[(v['brain_location'],v['hemisphere']) for v in json.loads(dec(f['general/virus'][()]) or '[]')],
        opto=[(g,o['hemisphere'],o['photo_stim_coordinate_ml']) for g,o in opto],
        probe=[json.loads(dec(f['general/extracellular_ephys'][g].attrs['location']))['probe_type'][:8]+"/"+json.loads(dec(f['general/extracellular_ephys'][g].attrs['location']))['rec_coordinate_ml'] for g in groups],
        ntr=len(df), resp=dict(collections.Counter(df.response)), stim=dict(sorted(collections.Counter(df.photo_stim_id).items())),
        nunits=len(u_['id']), ctype=dict(collections.Counter(dec(x) for x in u_['cell_type'][:])), sorted=sorted_ok, nspk=len(st),
        delay=np.round(np.median(df.cue_time-df.pole_out_time),3), sample=np.round(np.median(df.pole_out_time-df.pole_in_time),3),
        dur=np.round(np.median(df.stop_time-df.start_time),2), poleoff=np.round(np.median(df.pole_in_time-df.start_time),3),
        first_spk=st[:20].tolist()[:2], wf=u_['waveform_mean'].shape)
with ThreadPoolExecutor(8) as ex: rows=list(ex.map(one,assets))
df=pd.DataFrame(rows).sort_values('path'); df.to_pickle('/tmp/claude-1001/summ.pkl')
pd.set_option('display.width',400); pd.set_option('display.max_colwidth',80); pd.set_option('display.max_rows',100)
print(df.drop(columns=['first_spk','wf']).to_string())
E
cd $TMPDIR; . explore/bin/activate; time python summ.py 2>&1 | grep -v Warn
```

```
path         subj                           geno                 virus                       opto            probe  ntr                                                                              resp                          stim  nunits                                     ctype  sorted     nspk  delay  sample  dur  poleoff
14    sub-BAYLORCD12/sub-BAYLORCD12_ses-20180125T191601.nwb   BAYLORCD12  L7-cre x rosa26-lsl-ChR2-EYFP                    []  [(Fastigial, left, -0.8)]  [Cambridg/-1.5]  273                    {'HitR': 72, 'HitL': 89, 'ErrL': 28, 'ErrR': 9, 'NoLickR': 75}  {'0': 226, '5': 29, '6': 18}      20                {'pyramidal': 19, 'FS': 1}    True   148525    1.3     1.3  5.0    0.570
15    sub-BAYLORCD12/sub-BAYLORCD12_ses-20180126T122506.nwb   BAYLORCD12  L7-cre x rosa26-lsl-ChR2-EYFP                    []  [(Fastigial, left, -0.8)]  [Cambridg/-1.5]  256     {'HitR': 79, 'HitL': 83, 'ErrR': 15, 'ErrL': 35, 'NoLickL': 43, 'NoLickR': 1}  {'0': 220, '5': 16, '6': 20}      22                         {'pyramidal': 22}    True   202946    1.3     1.3  5.0    0.570
16    sub-BAYLORCD12/sub-BAYLORCD12_ses-20180128T220037.nwb   BAYLORCD12  L7-cre x rosa26-lsl-ChR2-EYFP                    []  [(Fastigial, left, -0.8)]  [Cambridg/-1.5]  318                                  {'HitR': 98, 'HitL': 133, 'ErrL': 80, 'ErrR': 7}  {'0': 270, '5': 23, '6': 25}      22                         {'pyramidal': 22}    True   196196    1.3     1.3  5.0    0.570
17    sub-BAYLORCD12/sub-BAYLORCD12_ses-20180129T160551.nwb   BAYLORCD12  L7-cre x rosa26-lsl-ChR2-EYFP                    []  [(Fastigial, left, -0.8)]  [Cambridg/-1.5]  196                    {'ErrL': 21, 'HitL': 77, 'HitR': 72, 'ErrR': 18, 'NoLickR': 8}   {'0': 177, '5': 11, '6': 8}      44  {'unknown': 1, 'pyramidal': 41, 'FS': 2}    True   562665    1.3     1.3  5.0    0.570
18    sub-BAYLORCD12/sub-BAYLORCD12_ses-20180130T153224.nwb   BAYLORCD12  L7-cre x rosa26-lsl-ChR2-EYFP                    []  [(Fastigial, 
[... 54 more lines not kept]
```

**Agent calls Bash**

```bash
cd paper; grep -o '<supplementary-material[^>]*>.\{0,600\}' gao2018.xml | head; grep -o 'xlink:href="[^"]*"' gao2018.xml | grep -iv "jpg\|gif" | head -20
```

```
<supplementary-material content-type="local-data" id="SD1" position="float" orientation="portrait"><label>1</label><media xmlns:xlink="http://www.w3.org/1999/xlink" xlink:href="NIHMS1504009-supplement-1.pdf" orientation="portrait" id="d36e1905" position="anchor"><?suppdata-name NIHMS1504009-supplement-1.pdf?><?suppdata-size 151871?><?suppdata-md5 b5e0e044586f4372c9ee9ea48c67a21a?><?suppdata-image-server-status NEVER_LOAD?><?suppdata-mime-type application?><?suppdata-mime-sub-type pdf?><?suppdata-cloudpmc-urn urn:app:20cb/6212318/b5e0e044586f/NIHMS1504009-supplement-1.pdf?></media></supplementary-material><supplementary-material content-type="local-data" id="SD2" position="float" orientation
xlink:href="http://www.nature.com/authors/editorial_policies/license.html#terms"
xlink:href="nihms-1504009.pdf"
xlink:href="https://imagej.net/Fiji"
xlink:href="https://www.mathworks.com/matlabcentral/fileexchange/20057-b-spline-grid--image-and-point-based-registration"
xlink:href="NIHMS1504009-supplement-1.pdf"
xlink:href="NIHMS1504009-supplement-2.pdf"
xlink:href="http://www.nature.com/reprints"
```

**Agent calls Bash**

```bash
cd paper; for n in 1 2; do curl -sL -A "Mozilla/5.0" -o supp$n.pdf "https://pmc.ncbi.nlm.nih.gov/articles/instance/6212318/bin/NIHMS1504009-supplement-$n.pdf"; file supp$n.pdf; done; ls -la
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd paper; rm supp1.pdf supp2.pdf; curl -sL -o supp.zip "https://www.ebi.ac.uk/europepmc/webservices/rest/PMC6212318/supplementaryFiles"; file supp.zip; unzip -o -q supp.zip -d supp && ls -la supp; ls -la .claude
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd paper; rm -rf supp supp.zip; for n in 1 2 3; do curl -sL -A "Mozilla/5.0" -o esm$n "https://static-content.springer.com/esm/art%3A10.1038%2Fs41586-018-0633-x/MediaObjects/41586_2018_633_MOESM${n}_ESM.pdf"; file esm$n; done
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd paper; rm esm3; mv esm1 esm1.pdf; mv esm2 esm2.pdf; which pdftotext; pdftotext -layout esm1.pdf - | head -50; pdftotext -layout esm2.pdf - | head -150
```

```
/bin/bash: line 1: pdftotext: command not found
/bin/bash: line 1: pdftotext: command not found
```

**Agent calls Bash**

```bash
cd $TMPDIR; . explore/bin/activate; uv pip install -q pypdf; cd paper; python -c "
import pypdf
for n in (1,2):
    r=pypdf.PdfReader(f'esm{n}.pdf'); t='\n'.join(p.extract_text() for p in r.pages); open(f'esm{n}.txt','w').write(t); print(n,len(r.pages),len(t))
"; head -c 3000 esm1.txt; echo; head -c 6000 esm2.txt
```

```
1 6 14852
2 3 8463
Letter
https://doi.org/10.1038/s41586-018-0633-x
A cortico-cerebellar loop for motor planning
Zhenyu Gao1, Courtney Davis2, Alyse M. thomas2, Michael N. economo3, Amada M. Abrego2, Karel Svoboda3,  
Chris I. De Zeeuw1,4 & Nuo Li2,3*
1Department of Neuroscience, Erasmus MC, Rotterdam, The Netherlands. 2Department of Neuroscience, Baylor College of Medicine, Houston, TX, USA. 3Janelia Research Campus, Ashburn, VA, 
USA. 4Netherlands Institute for Neuroscience, Amsterdam, The Netherlands. *e-mail: [removed: an e-mail address]
NATURE|  www.nature.com/nature
SUPPLEMENTARY INFORMATION
https:/ / doi.org/10.1038/s41586-018-0633-x
In the format provided by the authors and unedited.
© 2018 Springer Nature Limited. All rights reserved.
1 
 
Fastigial perturbation destroys the relationship between ALM activity trajectories 
and specific future movements 
 
We examined the relationship of ALM activity trajectories to upcoming movements and 
[... 108 more lines not kept]
```

**Agent calls Bash**

```bash
cd paper; sed -n '/Supplementary Table\|Supplemental Table/,$p' esm1.txt | head -150
```

```
Supplemental Table 1. List of mice and manipulated hemispheres in individual 
experiments. 
  
4 
 
References 
1 Li, N., Daie, K., Svoboda, K. & Druckmann, S. Robust neuronal dynamics in premotor cortex 
during motor planning. Nature, doi:10.1038/nature17643 (2016). 
2 Inagaki, H. K., Fontolan, L., Romani, S. & Svoboda, K. Discrete attractor dynamics underlying 
selective persistent activity in frontal cortex. bioRxiv, doi:https://doi.org/10.1101/203448 
(2017). 
3 Wolpert, D. M., Miall, R. C. & Kawato, M. Internal models in the cerebellum. Trends Cogn Sci 2, 
338-347 (1998). 
4 Kawato, M. Internal models for motor control and trajectory planning. Current opinion in 
neurobiology 9, 718-727 (1999). 
5 Heiney, S. A., Kim, J., Augustine, G. J. & Medina, J. F. Precise control of movement kinematics by 
optogenetic inhibition of Purkinje cell activity. The Journal of neuroscience : the official journal of 
the Society for Neuroscience 34, 2321-2330, doi:10.1523/JNEUROSCI.4547-13.2014 (2014). 
6 Herzfeld, D. J., Kojima, Y., Soetedjo, R. & Shadmehr, R. Encoding of action by the Purkinje cells of 
the cerebellum. Nature 526, 439-442, doi:10.1038/nature15693 (2015). 
[... 48 more lines not kept]
```

**Agent**

Supplemental Table 1 is an image; I'll render that page to read the mouse list (kept under `paper/`, not committed).

**Agent calls Bash**

```bash
cd paper; . $TMPDIR/explore/bin/activate; python -c "
import pypdf
r=pypdf.PdfReader('esm1.pdf')
for i,p in enumerate(r.pages):
    for im in p.images:
        fn=f'esm1_p{i}_{im.name}'; open(fn,'wb').write(im.data); print(fn, len(im.data))
"
```

```
(Bash completed with no output)
```

**Agent calls Bash**

```bash
cd $TMPDIR; . explore/bin/activate; uv pip install -q pymupdf 2>&1|tail -1; cd paper; python -c "
import fitz
d=fitz.open('esm1.pdf')
for i,p in enumerate(d):
    if 'Supplemental Table' in p.get_text(): p.get_pixmap(dpi=150).save(f'table_p{i}.png'); print(i)
"
```

```
[0;93m2026-10-19 11:51:37.680070664 [W:onnxruntime:Default, device_discovery.cc:95 GetPciBusId] Skipping pci_bus_id for PCI path at "/sys/devices/LNXSYSTM:00/LNXSYBUS:00/ACPI0004:00/MSFT1000:00/5620e0c7-8062-4dce-aeb7-520c7ef76171" because filename "5620e0c7-8062-4dce-aeb7-520c7ef76171" did not match expected pattern of [0-9a-f]+:[0-9a-f]+:[0-9a-f]+[.][0-9a-f]+[m
/tmp/claude-1001/explore/lib/python3.13/site-packages/fitz/__init__.py:17: FutureWarning: The `fitz` API is deprecated and will be removed in future. Use `import pymupdf` instead.
  warnings.warn(
3
```

**Agent calls Read**

```json
{
 "file_path": "paper/table_p3.png"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cat > $TMPDIR/stimtime.py <<'E'
import remfile, h5py, numpy as np, pandas as pd
from concurrent.futures import ThreadPoolExecutor
from dandi.dandiapi import DandiAPIClient
V="0.220126.1903"
with DandiAPIClient() as c:
    assets=[(a.path,a.get_content_url(follow_redirects=1, strip_query=True)) for a in c.get_dandiset("000007",V).get_assets()]
def dec(x): return x.decode() if isinstance(x,bytes) else x
edges=np.arange(-0.6,3.6,0.01)  # relative to pole_in
def one(pu):
    p,u=pu; f=h5py.File(remfile.File(u),'r')
    t=f['intervals/trials']; df=pd.DataFrame({k:[dec(x) for x in t[k][:]] for k in ['pole_in_time','pole_out_time','cue_time','photo_stim_id','response','lick_early']})
    st=f['units/spike_times'][:]; idx=f['units/spike_times_index'][:]; segs=np.split(st,idx[:-1])
    out={}
    for code in sorted(df.photo_stim_id.unique()):
        tr=df[(df.photo_stim_id==code)&(df.lick_early==0)]
        H=np.zeros((len(segs),len(edges)-1))
        for i,s in enumerate(segs):
            for t0 in tr.pole_in_time: 
                H[i]+=np.histogram(s-t0,edges)[0]
        out[code]=H/len(tr)/0.01
    return p,out
with ThreadPoolExecutor(8) as ex: res=list(ex.map(one,assets))
import pickle; pickle.dump(res,open('/tmp/claude-1001/stimtime.pkl','wb'))
E
cd $TMPDIR; . explore/bin/activate; python stimtime.py 2>&1 | grep -v Warn; python - <<'E'
import pickle,numpy as np
res=pickle.load(open('/tmp/claude-1001/stimtime.pkl','rb'))
edges=np.arange(-0.6,3.6,0.01); c=edges[:-1]+0.005
for grp,codes in [('FN',('1','2')),('DN',('3','4')),('PI',('5','6'))]:
    for code in codes:
        diffs=[]
        for p,o in res:
            if code in o: diffs.append(np.abs(o[code]-o['0']))
        D=np.concatenate(diffs).mean(0)
        base=D[c<0].mean(); sd=D[c<0].std()
        above=c[D>base+4*sd]
        # print profile in 100ms bins
        prof=[round(D[(c>=a)&(c<a+0.1)].mean()-base,2) for a in np.arange(-0.2,3.4,0.1)]
        print(grp,code,'first>4sd',above[:5], '\n  ', prof)
E
```

```
FN 1 first>4sd [0.015 0.025 0.035 0.045 0.055] 
   [np.float64(0.06), np.float64(0.02), np.float64(2.45), np.float64(1.73), np.float64(1.44), np.float64(1.36), np.float64(1.51), np.float64(1.69), np.float64(1.55), np.float64(1.49), np.float64(1.43), np.float64(1.42), np.float64(1.31), np.float64(1.22), np.float64(1.46), np.float64(1.22), np.float64(1.0), np.float64(0.89), np.float64(0.86), np.float64(0.85), np.float64(0.7), np.float64(0.65), np.float64(0.61), np.float64(0.71), np.float64(0.57), np.float64(0.55), np.float64(0.51), np.float64(0.39), np.float64(0.58), np.float64(0.25), np.float64(0.12), np.float64(0.12), np.float64(0.09), np.float64(0.09), np.float64(0.11), np.float64(0.16)]
FN 2 first>4sd [1.315 1.325 1.335 1.345 1.355] 
   [np.float64(-0.08), np.float64(0.03), np.float64(-0.01), np.float64(0.05), np.float64(-0.05), np.float64(-0.04), np.float64(-0.1), np.float64(-0.06), np.float64(-0.11), np.float64(-0.11), np.float64(0.0), np.float64(-0.09), np.float64(-0.04), np.float64(-0.03), np.float64(-0.08), np.float64(1.86), np.float64(1.77), np.float64(1.71), np.float64(1.75), np.float64(1.87), np.float64(1.95), np.float64(1.72), np.float64(1.73), np.float64(1.58), np.float64(1.49), np.float64(1.46), np.float64(1.18), np.float64(1.12), np.float64(1.23), np.float64(0.81), np.float64(0.57), np.float64(0.47), np.float64(0.34), np.float64(0.56), np.float64(0.47), np.float64(0.34)]
DN 3 first>4sd [0.005 0.015 0.025 0.035 0.045] 
   [np.float64(-0.02), np.float64(0.06), np.float64(1.08), np.float64(1.16), np.float64(1.15), np.float64(0.82), np.float64(0.87), np.float64(0.53), np.float64(0.41), np.float64(0.31), np.float64(0.31), np.float64(0.3), np.float64(0.23), np.float64(0.18), np.float64(0.08), np.float64(-0.08), np.float64(-0.14), np.float64(-0.17), np.float64(-0.18), np.float64(-0.12), np.float64(-0.12), np.float64(-0.16), np.float64(-0.08), np.float64(-0.13), np.float64(-0.11), np.float64(-0.12), np.float64(-0.15), np.float64(-0.22), np.float64(-0.22), np.f
[... 7 more lines not kept]
```

**Agent calls Bash**

```bash
for v in draft 0.220126.1903; do curl -s "https://api.dandiarchive.org/api/dandisets/000007/versions/$v/assets/?page_size=200" | python3 -c "
import json,sys;d=json.load(sys.stdin);print(sorted((a['path'],a['size'],a.get('blob')) for a in d['results'])[:2], len(d['results']))" ; done
curl -s "https://api.dandiarchive.org/api/dandisets/000007/versions/$v/assets/?page_size=200" | python3 -c "
import json,sys;d=json.load(sys.stdin);print(json.dumps(d['results'][0]))"
python3 - <<'E'
import json,urllib.request
a=json.load(urllib.request.urlopen("https://api.dandiarchive.org/api/dandisets/000007/versions/draft/"))
b=json.load(urllib.request.urlopen("https://api.dandiarchive.org/api/dandisets/000007/versions/0.220126.1903/"))
for k in sorted(set(a)|set(b)):
    if a.get(k)!=b.get(k): print('DIFF',k, str(a.get(k))[:300],'|||', str(b.get(k))[:300])
E
for q in "cerebellar" "Nuo Li" "fastigial" "cortico-cerebellar"; do curl -s "https://api.dandiarchive.org/api/dandisets/?search=$(python3 -c "import urllib.parse;print(urllib.parse.quote('$q'))")&page_size=50" | python3 -c "
import json,sys;d=json.load(sys.stdin);print('$q',[(r['identifier'],(r.get('most_recent_published_version') or r['draft_version'])['name'][:60]) for r in d['results']])"; done
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
curl -s "https://api.dandiarchive.org/api/dandisets/000572/versions/draft/" | python3 -c "
import json,sys;d=json.load(sys.stdin);print(d['name']);print(d.get('description','')[:600]);print(d.get('relatedResource'));print(d['assetsSummary'].get('numberOfSubjects'))"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
curl -sL "https://crcns.org/data-sets/motor-cortex" | grep -io '<a href="[^"]*alm[^"]*"[^<]*<[^<]*' | head -20; curl -sL "https://crcns.org/data-sets/cb" | grep -io 'href="/data-sets/[^"]*"' | sort -u | head; curl -sL "https://crcns.org/search?SearchableText=cerebellar+nuclei+motor+planning" | grep -io 'href="https://crcns.org/data-sets/[^"]*"' | sort -u | head
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
curl -sL -o $TMPDIR/crcns.html -w "%{http_code}\n" "https://crcns.org/data-sets/motor-cortex"; wc -c $TMPDIR/crcns.html; grep -o 'alm-[0-9][^<"]*' $TMPDIR/crcns.html | sort -u | head; grep -io 'cerebell[^<]*' $TMPDIR/crcns.html | head
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
grep -o '.\{1500\}cerebellar nucleus neurons of adult mice.\{600\}' $TMPDIR/crcns.html | sed 's/<[^>]*>/ /g' | tr -s ' ' | head -c 3000; echo; grep -o 'href="[^"]*alm-6[^"]*"' $TMPDIR/crcns.html | sort -u
```

```
href="https://crcns.org/data-sets/motor-cortex/alm-6"
```

**Agent calls Bash**

```bash
curl -sL "https://crcns.org/data-sets/motor-cortex/alm-6" | sed 's/<[^>]*>/ /g' | tr -s ' \n' | grep -i -A3 -B3 "zenodo\|cerebell\|doi" | head -60
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
curl -sL "https://crcns.org/data-sets/motor-cortex/alm-6" > $TMPDIR/alm6.html; grep -o 'href="[^"]*zenodo[^"]*"' $TMPDIR/alm6.html | sort -u; sed 's/<[^>]*>/ /g' $TMPDIR/alm6.html | tr -s ' \n' | sed -n '/alm-6 (anterior lateral motor cortex 6) *$/,$p' | grep -v "^ *$" | tail -60 | head -60
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
sed 's/<[^>]*>/ /g' $TMPDIR/alm6.html | tr -s ' \n' | grep -n -i "zenodo\|doi\|10\.\|about\|data set\|summary" | head -30; grep -o 'https\?://[^"<> ]*\(zenodo\|doi\)[^"<> ]*' $TMPDIR/alm6.html | sort -u
```

```
120: <meta content="Datasets from Gao et al (2018) A cortico-cerebellar loop for motor planning. Nature, Nov;563(7729):113-116. Data is hosted at zenodo.com."
213: title="The following folders contain data sets of the specified type. Click on the folders to view.">Data Sets 
222: title="Discussions about using data or crcns.org.">Forum 
224: href="https://crcns.org/about"
225: title="Information about this website and the CRCNS funding program.">About 
228: title="Publications and online resources (since 2009) based on data sets shared on CRCNS.org. ">Publications 
234: title="Data sharing projects that encompass much more than data sets. ">Hosted Projects 
237: title="Information about Neurodata Without Borders project.">NWB project 
270: Data Sets 
409: title="Extracellular recordings from anterior lateral motor cortex (ALM) neurons of adult mice performing a tactile decision behavior. Data contributed by Nuo Li in the lab of Karel Svoboda at Janelia Farm. This is the extracellular neurophysiology data set and behavior data set described in Li, N., Chen, T.W. et al Nature 2015.">
422: title="Calcium imaging recordings from mouse anterior lateral motor cortex (ALM) during performance of a tactile decision task. Data contributed by Tsai-Wen Chen in the lab of Karel Svoboda at Janelia Farm. This is the calcium imaging data set described in Li, N., Chen, T.W. et al Nature 2015.">
488: title="Datasets from Gao et al (2018) A cortico-cerebellar loop for motor planning. Nature, Nov;563(7729):113-116. Data is hosted at zenodo.com.">
498: <a href="https://crcns.org/data-sets/motor-cortex/alm-6/about-alm-6"
502: About alm-6 
517:Chen et al (2021) Cell, 184(14):3717-3730. Data is hosted at zenodo.com.">
530: title="Data and simulations related to: Thalamus-driven functional populations in frontal cortex activity supports decision-making. Yang et al (2022) Nat Neurosci. Data is hosted at zenodo.com.">
717: title="Data sets designed for challenges (predicting neuron responses)
[... 7 more lines not kept]
```

**Agent calls Bash**

```bash
curl -s "https://zenodo.org/api/records?q=%22cortico-cerebellar%20loop%20for%20motor%20planning%22&size=20" | python3 -c "
import json,sys;d=json.load(sys.stdin)
for h in d['hits']['hits']: print(h['id'],h['doi'],h['metadata']['title'][:90],h['metadata'].get('publication_date'), [ (f['key'],f['size']) for f in h.get('files',[])][:10])"
```

Result: the fetched text is not kept.

**Agent**

The paper's full data are on Zenodo via CRCNS alm-6 (NWB 11.9 GB zip, MATLAB 38 GB, plus analysis scripts). Reading the data description and listing the archives.

**Agent calls Bash**

```bash
cd paper; curl -sL -o zenodo_desc.pdf "https://zenodo.org/records/6647629/files/data%20description_ALM4_ver2022.pdf?download=1"; file zenodo_desc.pdf; . $TMPDIR/explore/bin/activate; python -c "
import pypdf;r=pypdf.PdfReader('zenodo_desc.pdf');t='\n'.join(p.extract_text() for p in r.pages);open('zenodo_desc.txt','w').write(t);print(t)"; curl -s https://zenodo.org/api/records/6647629 | python3 -c "import json,sys;d=json.load(sys.stdin);print(d['metadata'].get('description'));print(d['metadata'].get('version'), d['metadata'].get('license'), d['files'])"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
U="https://zenodo.org/api/records/6647629/files/datafiles_NWB.zip/content"; curl -sIL -r 0-99 "$U" | grep -i "HTTP/\|content-range\|accept-ranges\|content-length\|location" ; cd $TMPDIR; . explore/bin/activate; python - <<'E'
import requests, struct, io, zipfile, time
U="https://zenodo.org/api/records/6647629/files/datafiles_NWB.zip/content"
s=requests.Session()
r=s.get(U,headers={'Range':'bytes=-200000'},allow_redirects=True); print(r.status_code,len(r.content), r.url[:80])
class RangeFile(io.RawIOBase):
    def __init__(self,url,size): self.url=url; self.size=size; self.pos=0
    def seekable(self): return True
    def readable(self): return True
    def seek(self,o,w=0):
        self.pos = o if w==0 else (self.pos+o if w==1 else self.size+o); return self.pos
    def tell(self): return self.pos
    def readinto(self,b):
        n=len(b); 
        if self.pos>=self.size: return 0
        end=min(self.pos+n,self.size)-1
        d=s.get(self.url,headers={'Range':f'bytes={self.pos}-{end}'}).content
        b[:len(d)]=d; self.pos+=len(d); return len(d)
t=time.time()
z=zipfile.ZipFile(io.BufferedReader(RangeFile(r.url if r.status_code==206 else U,11886183325),buffer_size=1<<20))
infos=z.infolist(); print(len(infos), time.time()-t)
import collections
print(collections.Counter(i.compress_type for i in infos))
for i in infos[:15]: print(i.filename,i.file_size,i.compress_size)
print(sum(i.file_size for i in infos)/1e9)
import pickle; pickle.dump([(i.filename,i.file_size,i.compress_size,i.compress_type,i.header_offset) for i in infos],open('ziplist.pkl','wb'))
E
```

```
HTTP/1.1 200 OK
content-length: 11886183325
206 200000 https://zenodo.org/api/records/6647629/files/datafiles_NWB.zip/content
185 0.9637937545776367
Counter({8: 185})
datafiles_NWB/ANM344651_20160729.nwb 24783660 12934590
datafiles_NWB/ANM344651_20160730.nwb 18614040 9667609
datafiles_NWB/ANM344651_20160731.nwb 19820280 10215762
datafiles_NWB/ANM344651_20160801.nwb 60951892 31396452
datafiles_NWB/ANM344651_20160802.nwb 37800760 19489027
datafiles_NWB/ANM344651_20160803.nwb 19635392 10184927
datafiles_NWB/ANM344652_20160725.nwb 30806404 16005637
datafiles_NWB/ANM344652_20160726.nwb 85894948 44586348
datafiles_NWB/ANM344652_20160727.nwb 1962940 987337
datafiles_NWB/ANM344652_20160728.nwb 18067332 9370563
datafiles_NWB/ANM344652_20160729.nwb 130871468 67960235
datafiles_NWB/ANM344652_20160730_pene1.nwb 48271864 25062510
datafiles_NWB/ANM344652_20160730_pene2.nwb 103035628 53415530
datafiles_NWB/ANM344652_20160731.nwb 12298844 6325653
datafiles_NWB/ANM344652_20160801.nwb 50157104 26025079
[... 2 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR; . explore/bin/activate; cat > zread.py <<'E'
import requests, zlib, struct, io, time, pickle, h5py, sys
U="https://zenodo.org/api/records/6647629/files/datafiles_NWB.zip/content"
s=requests.Session()
infos=pickle.load(open('/tmp/claude-1001/ziplist.pkl','rb'))
def read_entry(name):
    fn,size,csize,ct,off=[i for i in infos if i[0]==name][0]
    h=s.get(U,headers={'Range':f'bytes={off}-{off+29}'}).content
    nl,el=struct.unpack('<HH',h[26:30]); start=off+30+nl+el
    r=s.get(U,headers={'Range':f'bytes={start}-{start+csize-1}'},stream=True)
    d=zlib.decompressobj(-15); out=[]
    for chunk in r.iter_content(1<<20): out.append(d.decompress(chunk))
    out.append(d.flush()); b=b''.join(out); assert len(b)==size; return b
t=time.time(); b=read_entry(sys.argv[1]); dt=time.time()-t; print(len(b)/1e6,'MB in',round(dt,1),'s')
f=h5py.File(io.BytesIO(b),'r')
def show(name,obj):
    if isinstance(obj,h5py.Dataset): print(' ',name, obj.shape, obj.dtype, str(dict(obj.attrs).get('description',''))[:90])
f.visititems(show)
for k in ['general/subject/subject_id','general/subject/genotype','general/experiment_description','session_description']:
    if k in f: print(k, f[k][()])
for g in f['general/extracellular_ephys']:
    if g!='electrodes': print('group', g, dict(f['general/extracellular_ephys'][g].attrs).get('location'))
E
python zread.py datafiles_NWB/ANM344652_20160801.nwb 2>&1 | grep -v Warn | head -80
```

```
50.157104 MB in 40.6 s
  analysis/unit2/control (1,) uint8 
  analysis/unit2/control_description (1,) object 
  analysis/unit2/data (78545, 37) float64 
  analysis/unit2/electrodes (78545,) int32 Electrodes involved with these spike events
  analysis/unit2/timestamps (78545,) float64 
  analysis/unit3/control (1,) uint8 
  analysis/unit3/control_description (1,) object 
  analysis/unit3/data (43341, 37) float64 
  analysis/unit3/electrodes (43341,) int32 Electrodes involved with these spike events
  analysis/unit3/timestamps (43341,) float64 
  analysis/unit4/control (1,) uint8 
  analysis/unit4/control_description (1,) object 
  analysis/unit4/data (32551, 37) float64 
  analysis/unit4/electrodes (32551,) int32 Electrodes involved with these spike events
  analysis/unit4/timestamps (32551,) float64 
  file_create_date (1,) object 
  general/data_collection () object 
  general/experiment_description () object 
  general/experimenter () object 
[... 55 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR; . explore/bin/activate; python - <<'E'
import requests,time
from concurrent.futures import ThreadPoolExecutor
U="https://zenodo.org/api/records/6647629/files/datafiles_NWB.zip/content"
def get(a):
    s=requests.Session(); t=time.time(); n=len(s.get(U,headers={'Range':f'bytes={a}-{a+8_000_000-1}'}).content); return n,time.time()-t
n,dt=get(1_000_000_000); print('single',n/dt/1e6,'MB/s')
t=time.time()
with ThreadPoolExecutor(8) as ex: r=list(ex.map(get,[2_000_000_000+i*10**8 for i in range(8)]))
print('8 parallel',sum(x[0] for x in r)/(time.time()-t)/1e6,'MB/s')
E
```

```
single 0.6423412237895746 MB/s
8 parallel 4.170164740762798 MB/s
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR; . explore/bin/activate; python - <<'E'
import pickle,collections,re
infos=pickle.load(open('ziplist.pkl','rb'))
by=collections.defaultdict(lambda:[0,0])
for fn,size,cs,ct,off in infos:
    m=re.search(r'/([A-Za-z]+\d+)_',fn); k=m.group(1) if m else fn
    by[k][0]+=1; by[k][1]+=cs
for k,v in sorted(by.items()): print(k,v[0],round(v[1]/1e9,2))
nl=[i for i in infos if '/NL' in i[0]]; print('NL total GB',sum(i[2] for i in nl)/1e9, len(nl))
print(sorted(nl,key=lambda i:i[2])[:3])
E
```

```
ANM344651 6 0.09
ANM344652 10 0.28
ANM344653 2 0.09
ANM350830 3 0.07
ANM350831 3 0.05
BAYLORCD1 12 0.65
BAYLORCD2 8 0.32
BAYLORDJ1 5 0.24
BAYLORNL1 11 0.52
BAYLORNL10 13 1.57
BAYLORNL11 13 1.27
BAYLORNL2 11 0.46
BAYLORNL3 13 0.88
BAYLORNL4 14 1.07
BAYLORNL6 16 0.82
BAYLORNL7 14 0.94
BAYLORNL8 17 1.16
BAYLORNL9 14 1.4
NL total GB 0.0 0
[]
[... 1 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR; . explore/bin/activate; python - <<'E'
import requests,time
from concurrent.futures import ThreadPoolExecutor
U="https://zenodo.org/api/records/6647629/files/datafiles_NWB.zip/content"
def get(a):
    s=requests.Session(); n=len(s.get(U,headers={'Range':f'bytes={a}-{a+4_000_000-1}'}).content); return n
for k in (16,32):
    t=time.time()
    with ThreadPoolExecutor(k) as ex: r=list(ex.map(get,[3_000_000_000+i*10**8+k for i in range(k)]))
    print(k,'parallel',sum(r)/(time.time()-t)/1e6,'MB/s', set(r))
E
```

```
16 parallel 7.4266603081751 MB/s {4000000}
32 parallel 12.796056818142544 MB/s {4000000}
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR; . explore/bin/activate; python - <<'E' 2>&1 | grep -v Warn
import pickle; infos=pickle.load(open('ziplist.pkl','rb'))
nl=sorted([i for i in infos if 'BAYLORNL3_' in i[0] or 'BAYLORNL4_' in i[0]],key=lambda i:i[2]); print([(i[0],i[2]) for i in nl[:3]])
exec(open('zread.py').read().split("t=time.time()")[0])
b=read_entry(nl[0][0]); f=h5py.File(io.BytesIO(b),'r')
def dec(x): return x.decode() if isinstance(x,bytes) else x
print(list(f['units'].keys()), dict(f['units'].attrs))
print(list(f['analysis'].keys())[:5])
a=f['analysis'][list(f['analysis'].keys())[0]]; print({k:a[k][()] if a[k].shape==() or a[k].size<3 else a[k].shape for k in a}, dict(a.attrs))
print(list(f['intervals/trials'].keys()))
import numpy as np
print('stim', np.unique(f['intervals/trials/StimTrials'][:],return_counts=True))
for k in f['general']:
    o=f['general'][k]
    if isinstance(o,h5py.Dataset): print(k, str(dec(o[()]))[:400])
print(list(f['acquisition'].keys()) if 'acquisition' in f else None, list(f['stimulus'].keys()) if 'stimulus' in f else None)
print(f['general/extracellular_ephys/electrodes/location'][:], [ (g,dict(f['general/extracellular_ephys'][g].attrs)) for g in f['general/extracellular_ephys'] if g!='electrodes'])
print(f['units/waveforms'][0])
E
```

```
[('datafiles_NWB/BAYLORNL3_20170120.nwb', 1092707), ('datafiles_NWB/BAYLORNL3_20170208.nwb', 4762433), ('datafiles_NWB/BAYLORNL3_20170203.nwb', 20590910)]
['id', 'spike_times', 'spike_times_index', 'trials', 'trials_index', 'waveforms'] {'colnames': array(['spike_times', 'trials', 'waveforms'], dtype=object), 'description': 'Analysed Spike Events', 'help': 'Data about spiking units', 'namespace': 'core', 'neurodata_type': 'Units'}
['unit1', 'unit3']
{'control': array([1], dtype=uint8), 'control_description': array([b'Units Table ID'], dtype=object), 'data': (2544, 30), 'electrodes': (2544,), 'timestamps': (2544,)} {'comments': 'cellType: Outside DCN unit', 'description': 'single unit 1 with unit location information', 'help': 'Snapshots of spike events from data.', 'namespace': 'core', 'neurodata_type': 'SpikeEventSeries'}
['CueTime', 'ErrL', 'ErrR', 'GoodTrials', 'HitL', 'HitR', 'LickEarly', 'NoLickL', 'NoLickR', 'PhotostimulationType', 'PoleInTime', 'PoleOutTime', 'StimTrials', 'id', 'start_time', 'stop_time', 'timeseries', 'timeseries_index']
stim (array([0., 1.]), array([281, 130]))
data_collection extracellularDataType: sorted spike times, spike waveform snipets, spike band voltage traces
cellType: Fastigial unit, Interposed unit, Dentate unit, Outside DCN unit
identificationMethod: recording location recovered from histology
amplifierRolloff: 
spikeSorting: manual
ADunit: 14 bits, 16 bits
experiment_description experimentType: behavior, extracellular, photostim
referenceAtlas: Allen Reference Atlas
task_keyword: detection, discrimination, lick Left lick Right, delay, somatosensory, motor, response, reward
experimenter Nuo Li
institution Baylor College of Medicine, Houston TX77030, USA
keywords [b'Network models' b'Deep cerebellar nucleus cortex' b'Short-term memory']
lab Svoboda
protocol IACUC
[... 9 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR; . explore/bin/activate; python - <<'E'
import requests, io, zipfile, json
rec=requests.get("https://zenodo.org/api/records/6653158").json()
print(rec['metadata']['title'], rec['metadata'].get('version'), rec['created'], rec['metadata'].get('description','')[:300])
U=[f['links']['self'] for f in rec['files'] if f['key']=='analyses_scripts.zip'][0]; size=[f['size'] for f in rec['files'] if f['key']=='analyses_scripts.zip'][0]
s=requests.Session()
class RF(io.RawIOBase):
    def __init__(s_,u,n): s_.u=u; s_.n=n; s_.p=0
    def seekable(s_): return True
    def readable(s_): return True
    def seek(s_,o,w=0): s_.p = o if w==0 else (s_.p+o if w==1 else s_.n+o); return s_.p
    def tell(s_): return s_.p
    def readinto(s_,b):
        if s_.p>=s_.n: return 0
        e=min(s_.p+len(b),s_.n)-1; d=s.get(s_.u,headers={'Range':f'bytes={s_.p}-{e}'}).content; b[:len(d)]=d; s_.p+=len(d); return len(d)
z=zipfile.ZipFile(io.BufferedReader(RF(U,size),buffer_size=1<<20))
inf=z.infolist(); print(len(inf))
for i in inf:
    if not i.filename.endswith('.mat') or i.file_size<2e5: print(i.filename,i.file_size,i.compress_size)
import os; os.makedirs('scripts',exist_ok=True)
for i in inf:
    if i.filename.endswith('.m'): z.extract(i,'scripts')
print(sum(i.file_size for i in inf if i.filename.endswith('.mat'))/1e6,'MB of .mat')
E
find $TMPDIR/scripts -name "*.m" | head -100
```

```
Dataset (MATLAB format) from Gao et al (2018) A cortico-cerebellar loop for motor planning. Nature, Nov;563(7729):113-116. None 2022-06-22T19:51:21.266304+00:00 <p><strong>Summary</strong></p>

<p>These experiments measure neuronal responses from anterior lateral motor cortex (ALM) and deep cerebellar nucleus (CN) of adult mice performing pole location discrimination with a short-term memory. In some cases, we manipulate activity of one brain region while r
12
analyses_scripts/analysis_compile_all_DCN_data.m 14678 2575
analyses_scripts/analysis_compiled_all_DCN_ALMsilencing_selectivity.m 19003 3087
analyses_scripts/analysis_DCN_ALM_photoinhibition_selectivity.m 2696 788
analyses_scripts/analysis_DCN_population_selectivity.m 1125 513
analyses_scripts/analysis_DCN_view_individual_neurons.m 10588 2193
analyses_scripts/helper_functions/ 0 0
analyses_scripts/helper_functions/func_getPSTH.m 866 374
analyses_scripts/helper_functions/func_getPSTH_smallBin.m 527 263
analyses_scripts/helper_functions/func_getPSTHsmallBin.m 538 266
analyses_scripts/helper_functions/func_plot_mean_and_sem.m 961 407
340.204902 MB of .mat
/tmp/claude-1001/scripts/analyses_scripts/analysis_compile_all_DCN_data.m
/tmp/claude-1001/scripts/analyses_scripts/analysis_DCN_ALM_photoinhibition_selectivity.m
/tmp/claude-1001/scripts/analyses_scripts/analysis_DCN_view_individual_neurons.m
/tmp/claude-1001/scripts/analyses_scripts/helper_functions/func_getPSTH_smallBin.m
/tmp/claude-1001/scripts/analyses_scripts/helper_functions/func_getPSTHsmallBin.m
[... 5 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/scripts/analyses_scripts; for f in *.m helper_functions/*.m; do echo "=================== $f"; cat "$f"; done | head -700
```

```
=================== analysis_DCN_ALM_photoinhibition_selectivity.m
clear all
% close all

addpath('.\helper_functions\')

% 
% % check to see if the data has been compiled
% if ~exist('analysis_compiled_all_DCN_ALMsilencing_selectivity.mat')
%     
%     % if not, compile all data first
%     analysis_compiled_all_DCN_ALMsilencing_selectivity
%     
% end


load analysis_compiled_all_DCN_ALMsilencing_selectivity

sig_selective(isnan(sig_selective))=0;

[... 682 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/scripts/analyses_scripts; sed -n 330,420p analysis_compile_all_DCN_data.m; echo =========; grep -n "Photostim_type\|ttest\|stim1\|stim2\|stim3\|N_trials_all\|_screen\|randsample\|>=\|cellType" analysis_compiled_all_DCN_ALMsilencing_selectivity.m | head -80; cat helper_functions/func_getPSTH.m
```

```
if mean(spk_count_yes)>mean(spk_count_no)
            PSTH_prefer_cue_aligned(n_unit,:) = psth1;
            PSTH_nonprefer_cue_aligned(n_unit,:) = psth2;
        else
            PSTH_prefer_cue_aligned(n_unit,:) = psth2;
            PSTH_nonprefer_cue_aligned(n_unit,:) = psth1;
        end
        
        
        
        
        
        % ============ other  information ==============
        Probe_type_all{n_unit,1} = meta_data.extracellular.probeType;
        Channel_all(n_unit,1) = median(unit.channel);
        if sum(strcmp(unit.cellType,'Fastigial unit'))>0
            cellType_all(n_unit,1) = 1;
        elseif sum(strcmp(unit.cellType,'Interposed unit'))>0
            cellType_all(n_unit,1) = 2;
        elseif sum(strcmp(unit.cellType,'Dentate unit'))>0
[... 142 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR; . explore/bin/activate; python - <<'E'
import requests, io, zipfile
rec=requests.get("https://zenodo.org/api/records/6653158").json()
for f in rec['files']: print(f['key'],f['size'],f['checksum'])
f=[f for f in rec['files'] if f['key']=='analyses_scripts.zip'][0]; U=f['links']['self']; size=f['size']
s=requests.Session()
class RF(io.RawIOBase):
    def __init__(s_,u,n): s_.u=u; s_.n=n; s_.p=0
    def seekable(s_): return True
    def readable(s_): return True
    def seek(s_,o,w=0): s_.p = o if w==0 else (s_.p+o if w==1 else s_.n+o); return s_.p
    def tell(s_): return s_.p
    def readinto(s_,b):
        if s_.p>=s_.n: return 0
        e=min(s_.p+len(b),s_.n)-1; d=s.get(s_.u,headers={'Range':f'bytes={s_.p}-{e}'}).content; b[:len(d)]=d; s_.p+=len(d); return len(d)
z=zipfile.ZipFile(io.BufferedReader(RF(U,size),buffer_size=1<<20))
for i in z.infolist(): print(i.filename,i.file_size,i.compress_size,i.compress_type)
E
```

```
datafiles_4_of_4.zip 9268156363 md5:3e56f5313fd4cd413ac0460f6b7cd7ad
data description_ALM4_ver2022.pdf 322524 md5:52d47c36989db22c6593c962704f572e
analyses_scripts.zip 339877520 md5:c37151c75a1e440ba7f07b21f304d360
datafiles_1_of_4.zip 11443344530 md5:f117488258ea3cb46584ce22c5672c05
datafiles_2_of_4.zip 8591181273 md5:5f2fa68cdb646fd626d978c5fbb06c61
datafiles_3_of_4.zip 9260149333 md5:87bfa3109b5910432b5cff607c27b3f9
analyses_scripts/analysis_compile_all_DCN_data.m 14678 2575 8
analyses_scripts/analysis_compile_all_DCN_data.mat 203627100 203566041 8
analyses_scripts/analysis_compiled_all_DCN_ALMsilencing_selectivity.m 19003 3087 8
analyses_scripts/analysis_compiled_all_DCN_ALMsilencing_selectivity.mat 136577802 136298753 8
analyses_scripts/analysis_DCN_ALM_photoinhibition_selectivity.m 2696 788 8
analyses_scripts/analysis_DCN_population_selectivity.m 1125 513 8
analyses_scripts/analysis_DCN_view_individual_neurons.m 10588 2193 8
analyses_scripts/helper_functions/ 0 0 0
analyses_scripts/helper_functions/func_getPSTH.m 866 374 8
analyses_scripts/helper_functions/func_getPSTH_smallBin.m 527 263 8
analyses_scripts/helper_functions/func_getPSTHsmallBin.m 538 266 8
analyses_scripts/helper_functions/func_plot_mean_and_sem.m 961 407 8
Shell cwd was reset to
```

**Agent calls Bash**

```bash
free -g; nproc; df -h $TMPDIR | tail -1; python3 --version; cat entries/001453-fouke-2025/requirements.lock.txt | head -20; sed -n 1,60p tools/entry.py
```

```
total        used        free      shared  buff/cache   available
Mem:              15           1           9           0           4          14
Swap:              2           0           2
4
/dev/root       145G   61G   84G  42% /tmp/claude-1001
Python 3.13.16
# This file was autogenerated by uv via the following command:
#    uv pip compile --python-version 3.13 requirements.in -o requirements.lock.txt
acres==0.5.0
    # via bidsschematools
aiohappyeyeballs==2.7.1
    # via aiohttp
aiohttp==3.14.5
    # via nwbinspector
aiosignal==1.4.0
    # via aiohttp
annotated-types==0.8.0
    # via pydantic
arrow==1.4.0
    # via isoduration
[... 65 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 98,115p tools/entry.py; sed -n 160,180p tools/entry.py; sed -n 196,330p tools/entry.py
```

```
def _plain(value):
    """YAML dates as strings, so JSON Schema's string formats apply."""
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


    for name in [n for n in listed if n in present]:
[... 154 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 60,68p tools/entry.py; python3 -c "
import json;s=json.load(open('schemas/claims.schema.json'));print(json.dumps(s,indent=1)[:5000])"
```

```
EMBEDDED_IMAGE = re.compile(r"data:image/|iVBORw0KGgo|/9j/4AAQ")
READS_A_FIGURE = re.compile(r"""(imread|Image\.open|IPython\.display\.Image|display\.Image)\s*\(""")
LOCAL_PATH = re.compile(r"""["'](?:~/|/(?:Users|home|tmp|mnt|media|Volumes|data|scratch)/|[A-Za-z]:[\\/])""")
LONG_LITERAL = re.compile(r"[\[(]\s*(?:-?\d+\.?\d*(?:e-?\d+)?\s*,\s*){%d,}" % MAX_LITERAL_NUMBERS)


class Report:
    def __init__(self):
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
[... 128 more lines not kept]
```

**Agent calls Bash**

```bash
mkdir -p entries/000007-gao-2018; cat $TMPDIR/scripts/analyses_scripts/helper_functions/func_getPSTH_smallBin.m; sed -n 280,300p $TMPDIR/scripts/analyses_scripts/analysis_compiled_all_DCN_ALMsilencing_selectivity.m; sed -n 160,175p $TMPDIR/scripts/analyses_scripts/analysis_compiled_all_DCN_ALMsilencing_selectivity.m
```

```
function [PSTH time] = func_getPSTH_smallBin(SpikeTimes, PSTH_StartTime, PSTH_EndTime)

% 
% SpikeTimes -- {n_rep,1}
% 

if nargin == 1
    PSTH_StartTime = -.52;
    PSTH_EndTime = 5.020;
end

time = PSTH_StartTime-.01:.01:PSTH_EndTime+.01;


n_rep = size(SpikeTimes,1);
total_counts = 0;
for i_rep = 1:n_rep
    
    [counts] = hist(SpikeTimes{i_rep,1},time);
    total_counts = total_counts+counts/n_rep;
[... 47 more lines not kept]
```

**Agent calls Write**

```json
{
 "file_path": "entries/000007-gao-2018/gao2018.py",
 "content": "\"\"\"Loading and measures for the ALM recordings of dandiset 000007.\n\nGao, Davis, Thomas, Economo, Abrego, Svoboda, De Zeeuw & Li (2018), Nature,\ndoi:10.1038/s41586-018-0633-x.\n\nEach NWB file holds one session of ALM recording in a head-fixed mouse doing the delayed\nresponse task: the sorted units (spike times, a cell type label, the mean waveform) and a trial\ntable with the times of pole in (sample start), pole out (delay start) and the go cue (delay\nend), the outcome (`response`), early licks, and a photostimulation code (`photo_stim_id`).\nThe trial times are on the session clock, as are the spike times. Files are streamed from the\narchive at the pinned version; nothing is written to disk.\n\nWhere the parameters come from:\n\n- Epochs, from the Methods and the paper's CN analysis scripts (`analyses_scripts.zip` of Zenodo\n  record doi:10.5281/zenodo.6653158, `analysis_compile_all_DCN_data.m`): sample is pole in to\n  pole out, delay is pole out to the cue, response is the cue to 1.3 s after it.\n- Trial selection, from the same scripts: trials with an early lick are left out, and for each\n  unit only the trials from the first to the last trial in which it fired (\"stable trials\").\n  The scripts also drop trials marked as not performing (`GoodTrials`); the dandiset has no such\n  column (see the data check).\n- Trial type: the R or L in `response` (HitR, ErrR, NoLickR) is the instructed side, as in the\n  scripts, where \"yes\" trials are HitR or ErrR and the analysis of photostimulation groups\n  correct and error trials by instructed type (Methods).\n- Selectivity test: two-tailed t-test on spike rates of correct trials, lick right against lick\n  left, in each epoch, p < 0.05 in any epoch (Methods and scripts). Preferred trial type from a\n  random subset of trials (10 per type for ALM, Methods; the scripts use 20 for CN and require 30\n  correct trials of each type), selectivity on the rest.\n- Cell types: trough-to-peak width of the mean waveform, below 0.35 ms fast spiking, above\n  0.45 ms putative pyramidal, in between left out (Methods).\n- Photostimulation effect on a unit: two-tailed t-test of spike counts, control against\n  photostimulation trials, trial types pooled (Methods); p < 0.01.\n- Onset latency (Extended Data Fig. 9a): rate change in 10 ms bins stepped by 1 ms, the sign of\n  suppressed units flipped, onset as the first bin where the population change differs from 0\n  (t-test p < 0.01), resampled over units 10,000 times. The window searched (from photostimulus\n  onset to 100 ms after it) is a choice made here; the Methods do not give one.\n- Coding direction (Methods): mean spike counts in 400 ms windows stepped by 10 ms, the\n  difference of the lick right and lick left means, averaged over the delay epoch, from correct\n  control trials; projections on held-out trials.\n- Behavioural performance: fraction correct, without early-lick and no-lick trials; the\n  hierarchical bootstrap over mice, sessions and trials (Methods), one-tailed.\n- Names of the photostimulation codes: from the data description of the paper's Zenodo records\n  (`data description_ALM4_ver2022.pdf` in doi:10.5281/zenodo.6647629 and 6653158), not from the\n  dandiset, which leaves them undescribed.\n\"\"\"\n\nfrom __future__ import annotations\n\nimport json\nfrom concurrent.futures import ThreadPoolExecutor\n\nimport h5py\nimport numpy as np\nimport pandas as pd\nimport remfile\nfrom dandi.dandiapi import DandiAPIClient\nfrom scipy import stats\n\nDANDISET_ID = \"000007\"\nDANDISET_VERSION = \"0.220126.1903\"\n\nRESPONSE_S = 1.3            # length of the response epoch after the cue (scripts)\nSELECTIVE_P = 0.05\nPHOTOSTIM_P = 0.01\nALM_SCREEN_TRIALS = 10      # Methods: trials per type used to pick the preferred type in ALM\nNARROW_MS, WIDE_MS = 0.35, 0.45\n\n# Photostimulation codes, from the data description of the paper's Zenodo records.\nSTIM_CODES = {\n    0: (\"control\", None, None, None),\n    1: (\"fastigial photo-activation\", \"fastigial\", \"sample\", 0.5),\n    2: (\"fastigial photo-activation\", \"fastigial\", \"delay\", 0.5),\n    3: (\"dentate photo-activation\", \"dentate\", \"sample\", 0.5),\n    4: (\"dentate photo-activation\", \"dentate\", \"delay\", 0.5),\n    5: (\"CN photo-inhibition\", \"CN\", \"delay\", 0.5),\n    6: (\"CN photo-inhibition\", \"CN\", \"delay\", 1.3),\n}\n\n\ndef _text(x):\n    x = x[()] if hasattr(x, \"shape\") else x\n    if isinstance(x, bytes):\n        x = x.decode()\n    return x\n\n\ndef asset_urls() -> dict[str, str]:\n    with DandiAPIClient() as client:\n        ds = client.get_dandiset(DANDISET_ID, DANDISET_VERSION)\n        return {a.path: a.get_content_url(follow_redirects=1, strip_query=True) for a in ds.get_assets()}\n\n\ndef load_session(path: str, url: str) -> dict:\n    \"\"\"Everything the analyses use from one file, read once.\"\"\"\n    f = h5py.File(remfile.File(url), \"r\")\n    t = f[\"intervals/trials\"]\n    cols = [c.decode() if isinstance(c, bytes) else c for c in t.attrs[\"colnames\"]]\n    trials = pd.DataFrame({c: [_text(v) if isinstance(v, bytes) else v for v in t[c][:]] for c in cols\n                           if c != \"session_directory\"})\n    trials[\"stim\"] = trials.pop(\"photo_stim_id\").astype(int)\n    trials[\"trial_type\"] = trials.response.str[-1].map({\"R\": \"R\", \"L\": \"L\"})\n    trials.loc[trials.response == \"NoLickNoResponse\", \"trial_type\"] = None\n    trials[\"outcome\"] = np.select([trials.response.str.startswith(\"Hit\"), trials.response.str.startswith(\"Err\")],\n                                  [\"hit\", \"error\"], \"nolick\")\n    u = f[\"units\"]\n    st = u[\"spike_times\"][:]\n    idx = u[\"spike_times_index\"][:]\n    spikes = np.split(st, idx[:-1])\n    groups = [g for g in f[\"general/extracellular_ephys\"] if g != \"electrodes\"]\n    rec = json.loads(f[\"general/extracellular_ephys\"][groups[0]].attrs[\"location\"])\n    opto = {g: json.loads(_text(f[\"general/optogenetics\"][g][\"location\"])) for g in f[\"general/optogenetics\"]}\n    subject = path.split(\"/\")[0].removeprefix(\"sub-\")\n    s = dict(\n        path=path, subject=subject, session=path.split(\"_ses-\")[1].removesuffix(\".nwb\"),\n        genotype=_text(f[\"general/subject/genotype\"]),\n        virus=json.loads(_text(f[\"general/virus\"]) or \"[]\"),\n        opto=opto, probe=rec[\"probe_type\"], rec_ml=float(rec[\"rec_coordinate_ml\"]),\n        trials=trials, spikes=spikes,\n        cell_type=np.array([_text(x) for x in u[\"cell_type\"][:]]),\n        unit_rate_hz=u[\"sampling_rate\"][:],\n        waveform=u[\"waveform_mean\"][:],\n        obs=u[\"obs_intervals\"][:],\n        trial_descriptions={c: _text(t[c].attrs.get(\"description\", \"\")) for c in cols},\n        units_colnames=[c.decode() if isinstance(c, bytes) else c for c in u.attrs[\"colnames\"]],\n    )\n    s[\"site\"] = next(iter(opto)) if opto else None\n    s[\"site_hemisphere\"] = next(iter(opto.values()))[\"hemisphere\"] if opto else None\n    s[\"group\"] = {\"Fastigial\": \"FN\", \"Dentate\": \"DN\"}.get(s[\"site\"]) if s[\"genotype\"] == \"unknown\" else \"PI\"\n    f.close()\n    return s\n\n\ndef load_all(workers: int = 8) -> list[dict]:\n    urls = asset_urls()\n    with ThreadPoolExecutor(workers) as ex:\n        sessions = list(ex.map(lambda kv: load_session(*kv), sorted(urls.items())))\n    return sessions\n\n\ndef spike_width_ms(waveform: np.ndarray, rate_hz: float) -> float:\n    \"\"\"Trough-to-peak interval of a mean waveform (Methods).\"\"\"\n    trough = int(np.argmin(waveform))\n    peak = trough + int(np.argmax(waveform[trough:]))\n    return (peak - trough) / rate_hz * 1000.0\n\n\ndef counts(spikes: np.ndarray, starts, stops) -> np.ndarray:\n    \"\"\"Spike counts in [start, stop) for each pair, on the session clock.\"\"\"\n    starts, stops = np.asarray(starts, float), np.asarray(stops, float)\n    return np.searchsorted(spikes, stops) - np.searchsorted(spikes, starts)\n\n\ndef stable_trials(spikes: np.ndarray, trials: pd.DataFrame) -> np.ndarray:\n    \"\"\"Trials from the first to the last one in which the unit fired (the scripts' rule).\"\"\"\n    n = counts(spikes, trials.start_time, trials.stop_time)\n    fired = np.flatnonzero(n > 0)\n    keep = np.zeros(len(trials), bool)\n    if len(fired):\n        keep[fired[0]:fired[-1] + 1] = True\n    return keep\n\n\ndef epoch_bounds(trials: pd.DataFrame) -> dict[str, tuple[np.ndarray, np.ndarray]]:\n    return {\"sample\": (trials.pole_in_time.values, trials.pole_out_time.values),\n            \"delay\": (trials.pole_out_time.values, trials.cue_time.values),\n            \"response\": (trials.cue_time.values, trials.cue_time.values + RESPONSE_S)}\n\n\ndef epoch_rates(spikes, trials) -> pd.DataFrame:\n    out = {}\n    for name, (a, b) in epoch_bounds(trials).items():\n        out[name] = counts(spikes, a, b) / (b - a)\n    return pd.DataFrame(out, index=trials.index)\n\n\ndef selectivity_tests(s: dict, unit_mask=None) -> pd.DataFrame:\n    \"\"\"Per unit, t-test p of lick right against lick left (correct control trials) in each epoch.\"\"\"\n    tr = s[\"trials\"]\n    rows = []\n    for i, sp in enumerate(s[\"spikes\"]):\n        if unit_mask is not None and not unit_mask[i]:\n            continue\n        ok = stable_trials(sp, tr) & (tr.lick_early == 0).values & (tr.stim == 0).values & (tr.outcome == \"hit\").values\n        r = epoch_rates(sp, tr)\n        right, left = ok & (tr.trial_type == \"R\").values, ok & (tr.trial_type == \"L\").values\n        row = {\"unit\": i, \"n_right\": int(right.sum()), \"n_left\": int(left.sum())}\n        for e in (\"sample\", \"delay\", \"response\"):\n            if right.sum() >= 2 and left.sum() >= 2:\n                row[f\"p_{e}\"] = stats.ttest_ind(r[e].values[right], r[e].values[left]).pvalue\n                row[f\"d_{e}\"] = r[e].values[right].mean() - r[e].values[left].mean()\n            else:\n                row[f\"p_{e}\"], row[f\"d_{e}\"] = np.nan, np.nan\n        rows.append(row)\n    return pd.DataFrame(rows)\n\n\ndef psth(spikes, align, t_from, t_to, step=0.001, smooth=0.2):\n    \"\"\"Mean rate (spikes/s) around each alignment time, box-car of `smooth` s (the scripts' 200 ms).\"\"\"\n    edges = np.arange(t_from - smooth, t_to + smooth + step / 2, step)\n    h = np.zeros(len(edges) - 1)\n    for t0 in align:\n        lo, hi = np.searchsorted(spikes, [t0 + edges[0], t0 + edges[-1]])\n        h += np.histogram(spikes[lo:hi] - t0, edges)[0]\n    h = h / max(len(align), 1) / step\n    k = int(round(smooth / step))\n    sm = np.convolve(h, np.ones(k) / k, mode=\"same\")\n    centres = edges[:-1] + step / 2\n    keep = (centres >= t_from) & (centres <= t_to)\n    return centres[keep], sm[keep]\n\n\ndef binned_counts(spikes, align, centres, width):\n    \"\"\"Spike counts in windows of `width` s centred on `centres`, for each alignment time.\"\"\"\n    align = np.asarray(align, float)[:, None]\n    a = align + np.asarray(centres)[None, :] - width / 2\n    return (np.searchsorted(spikes, a + width) - np.searchsorted(spikes, a)).astype(float)\n\n\ndef performance(trials: pd.DataFrame) -> pd.DataFrame:\n    \"\"\"Trials that count for performance: no early lick, a lick after the cue.\"\"\"\n    t = trials[(trials.lick_early == 0) & (trials.outcome != \"nolick\") & trials.trial_type.notna()]\n    return t.assign(correct=(t.outcome == \"hit\").astype(float))\n\n\ndef hierarchical_bootstrap(df: pd.DataFrame, stat, n: int, rng: np.random.Generator) -> np.ndarray:\n    \"\"\"Resample mice, then sessions within mouse, then trials within session (Methods).\"\"\"\n    by_mouse = {m: {s: g for s, g in d.groupby(\"session\")} for m, d in df.groupby(\"subject\")}\n    mice = list(by_mouse)\n    out = np.empty(n)\n    for k in range(n):\n        parts = []\n        for m in rng.choice(mice, len(mice)):\n            sess = list(by_mouse[m])\n            for s in rng.choice(len(sess), len(sess)):\n                g = by_mouse[m][sess[s]]\n                parts.append(g.iloc[rng.integers(0, len(g), len(g))])\n        out[k] = stat(pd.concat(parts))\n    return out\n\n\ndef onset_latency(change: np.ndarray, centres: np.ndarray, rng: np.random.Generator, n_boot: int = 10000,\n                  p: float = 0.01) -> tuple[float, float, np.ndarray]:\n    \"\"\"Onset of a population rate change (units x bins), as in Extended Data Fig. 9a.\n\n    The onset is the first bin centre at which the change across units differs from 0 (one-sample\n    t-test, p < 0.01). Units are resampled with replacement `n_boot` times; returns the mean and\n    standard deviation of the resampled onsets (the bootstrap standard error) and the onsets.\n    \"\"\"\n    def first(x):\n        t, pv = stats.ttest_1samp(x, 0.0, axis=0)\n        hit = np.flatnonzero((pv < p) & (t > 0))\n        return centres[hit[0]] if len(hit) else np.nan\n    onsets = np.array([first(change[rng.integers(0, len(change), len(change))]) for _ in range(n_boot)])\n    return float(np.nanmean(onsets)), float(np.nanstd(onsets)), onsets\n"
}
```

```
File created successfully at: entries/000007-gao-2018/gao2018.py (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd entries/000007-gao-2018; . $TMPDIR/explore/bin/activate; python - <<'E' 2>&1 | grep -v Warn
import time,pickle, gao2018 as g, numpy as np, pandas as pd, collections
t=time.time(); S=g.load_all(); print('load',time.time()-t)
pickle.dump(S,open('/tmp/claude-1001/S.pkl','wb'))
rows=[]
for s in S:
    w=[g.spike_width_ms(wf,r) for wf,r in zip(s['waveform'],s['unit_rate_hz'])]
    for ct,ww in zip(s['cell_type'],w): rows.append(dict(group=s['group'],subject=s['subject'],probe=s['probe'][:8],ct=ct,w=ww))
d=pd.DataFrame(rows)
print(d.groupby(['group','ct']).size().unstack())
print(d.groupby(['probe','ct']).w.describe())
print(pd.crosstab([d.probe,d.ct],pd.cut(d.w,[0,0.2,0.3,0.35,0.4,0.45,0.5,0.6,0.8,2])))
print(S[0]['trial_descriptions']); print(S[0]['units_colnames'])
E
```

```
load 72.16100597381592
ct       FS  pyramidal  unknown
group                          
DN     33.0      545.0      NaN
FN     40.0      567.0      1.0
PI     29.0      706.0      2.0
                     count      mean       std   min   25%   50%   75%   max
probe    ct                                                                 
Cambridg FS           29.0  0.229310  0.036638  0.15  0.20  0.25  0.25  0.25
         pyramidal   706.0  0.652620  0.079917  0.30  0.60  0.70  0.70  0.70
         unknown       2.0  0.300000  0.000000  0.30  0.30  0.30  0.30  0.30
NN 32ch  FS           73.0  0.221233  0.064505  0.15  0.15  0.20  0.25  0.35
         pyramidal  1112.0  0.686556  0.103131  0.30  0.60  0.70  0.70  0.90
         unknown       1.0  0.300000       NaN  0.30  0.30  0.30  0.30  0.30
w                   (0.0, 0.2]  (0.2, 0.3]  ...  (0.6, 0.8]  (0.8, 2.0]
probe    ct                                 ...                        
Cambridg FS                  8          21  ...           0           0
         pyramidal           0          16  ...         491           0
         unknown             0           2  ...           0           0
NN 32ch  FS                 37          28  ...           0           0
[... 6 more lines not kept]
```

**Agent calls Bash**

```bash
. $TMPDIR/explore/bin/activate; python - <<'E' 2>&1 | grep -v Warn
import pickle, numpy as np, pandas as pd, hashlib, collections, gao2018 as g
S=pickle.load(open('/tmp/claude-1001/S.pkl','rb'))
H=collections.defaultdict(list); near=[]
for s in S:
    for i,sp in enumerate(s['spikes']):
        H[hashlib.md5(np.round(sp,5).tobytes()).hexdigest()].append((s['path'].split('/')[1][:40],i,len(sp)))
d=[v for v in H.values() if len(v)>1]; print('identical spike trains groups',len(d), d[:10])
# within session near duplicates: fraction of coincident spikes within 0.5 ms
cnt=0; ex=[]
for s in S:
    sp=s['spikes']
    for i in range(len(sp)):
        for j in range(i+1,len(sp)):
            a,b=sp[i],sp[j]
            if len(a)<100 or len(b)<100: continue
            k=np.searchsorted(b,a); k=np.clip(k,1,len(b)-1)
            dmin=np.minimum(np.abs(b[k]-a),np.abs(b[k-1]-a))
            f=(dmin<0.0005).mean()
            if f>0.5: cnt+=1; ex.append((s['path'][-30:],i,j,len(a),len(b),round(f,2)))
print('near-duplicate unit pairs within sessions (>50% spikes within 0.5 ms):',cnt, ex[:20])
# session-level duplicates: trial tables
T={}
for s in S:
    k=hashlib.md5(np.round(s['trials'][['pole_in_time','cue_time']].values,3).tobytes()).hexdigest(); T.setdefault(k,[]).append(s['path'])
print('dup trial tables',[v for v in T.values() if len(v)>1])
print('same start count', collections.Counter(len(s['trials']) for s in S).most_common(3))
E
```

```
identical spike trains groups 0 []
near-duplicate unit pairs within sessions (>50% spikes within 0.5 ms): 2 [('LORCD6_ses-20170611T140007.nwb', 48, 57, 10030, 11008, np.float64(0.96)), ('314760_ses-20151021T164427.nwb', 5, 37, 4332, 9786, np.float64(0.83))]
dup trial tables []
same start count [(246, 3), (343, 2), (220, 2)]
```

**Agent calls Bash**

```bash
. $TMPDIR/explore/bin/activate; python - <<'E' 2>&1 | grep -v Warn
import pickle, numpy as np, pandas as pd, gao2018 as g
S=pickle.load(open('/tmp/claude-1001/S.pkl','rb'))
rows=[]
for s in S:
    tr=s['trials']
    for i,sp in enumerate(s['spikes']):
        st=g.stable_trials(sp,tr); ok=st&(tr.lick_early==0).values
        dur=sp[-1]-sp[0]; inside=(g.counts(sp,tr.start_time,tr.stop_time).sum())/len(sp)
        rows.append(dict(group=s['group'],subj=s['subject'],sess=s['session'],ct=s['cell_type'][i],nst=st.sum(),ntr=len(tr),
            stim=[int((ok&(tr.stim==c).values).sum()) for c in sorted(tr.stim.unique()) if c>0],
            hitR=int((ok&(tr.stim==0).values&(tr.response=='HitR').values).sum()),hitL=int((ok&(tr.stim==0).values&(tr.response=='HitL').values).sum()),
            rate=len(sp)/dur, frac_in_trials=inside))
d=pd.DataFrame(rows); d['minstim']=d.stim.apply(min)
p=d[d.ct=='pyramidal']
for grp in ['FN','DN','PI']:
    q=p[p.group==grp]
    print(grp,len(q),'stable frac median',(q.nst/q.ntr).median(),'n hitR>=30&hitL>=30',((q.hitR>=30)&(q.hitL>=30)).sum(),
          '>=10 each',((q.hitR>=10)&(q.hitL>=10)).sum(), 'minstim>3', (q.minstim>3).sum(),'minstim>=10',(q.minstim>=10).sum(), 'rate>0.5', (q.rate>0.5).sum(),'rate>1',(q.rate>1).sum())
print(d.groupby(['group','subj','sess']).size().groupby(['group','subj']).agg(['count','sum']))
E
```

```
FN 567 stable frac median 0.8148148148148148 n hitR>=30&hitL>=30 431 >=10 each 514 minstim>3 476 minstim>=10 428 rate>0.5 500 rate>1 435
DN 545 stable frac median 0.9031531531531531 n hitR>=30&hitL>=30 530 >=10 each 544 minstim>3 545 minstim>=10 535 rate>0.5 465 rate>1 401
PI 706 stable frac median 0.8336124127314222 n hitR>=30&hitL>=30 540 >=10 each 649 minstim>3 666 minstim>=10 501 rate>0.5 607 rate>1 528
                   count  sum
group subj                   
DN    BAYLORNL12       5  244
      BAYLORNL14       6  308
      anm00314756      2   26
FN    BAYLORCD6        4  196
      BAYLORNL15       5  177
      anm00314746      3   63
      anm00314757      2   38
      anm00314758      4   62
      anm00314760      3   72
PI    BAYLORCD12       5  160
      BAYLORCD13       5  100
      BAYLORCD14       5  195
      BAYLORCD8        5  282
```

**Agent calls Write**

```json
{
 "file_path": "claims/000007/10.1038-s41586-018-0633-x.yaml",
 "content": "# Claims for Gao, Davis, Thomas, Economo, Abrego, Svoboda, De Zeeuw & Li (2018), Nature, on\n# dandiset 000007. Source, the author manuscript in PubMed Central (PMC6212318), full text, with\n# its Methods, figure legends and Extended Data legends, and the Supplementary Information from\n# the publisher (Supplemental Table 1 lists the mice of each experiment).\n#\n# The dandiset holds the ALM recordings only, 54 sessions from 13 mice (9 with ChR2 in the\n# fastigial or dentate nucleus, 4 L7-cre x Ai32 for CN photo-inhibition), with spike times, a\n# trial table and an undescribed photostimulation code. The CN recordings, the lesion and\n# behaviour-only sessions, the anatomy and the lick times are not in it. The paper's data\n# description and the CN recordings are on Zenodo (NWB, doi:10.5281/zenodo.6647629; MATLAB with\n# the paper's CN analysis scripts, doi:10.5281/zenodo.6653158), found through CRCNS alm-6, which\n# the paper's reporting summary names. Claims on the CN recordings are `elsewhere`; claims that\n# need the names of the photostimulation codes take them from the Zenodo data description\n# (`with_labels`) and depend on stim-code-link.\n#\n# When these criteria were written the author had seen the data check only: the file list and\n# metadata, counts of sessions, trials, outcomes, codes and units per file, the cell type labels\n# and spike widths, a search for duplicated units and sessions, and, to see what the codes are,\n# the mean absolute difference in ALM firing between each code's trials and control trials in\n# 10 ms and 100 ms bins from 0.6 s before to 3.6 s after pole in, pooled over all units. That\n# last check showed the change starting 5 to 15 ms after sample onset for codes 1 and 3 and\n# after delay onset for codes 2, 4, 5 and 6, lasting longer after code 1 and 2 (fastigial) than\n# after 3 and 4 (dentate), and longer after 6 than after 5. It bears on stim-code-link,\n# ed9a-fn-latency, ed9a-dn-latency, fig4f-fn-persistent and fig4g-dn-recovery. No unit-level\n# test, selectivity, performance or coding direction had been computed. The author had also\n# read the paper's CN analysis scripts.\n#\n# Method choices fixed here, from the Methods and the paper's CN scripts where the Methods are\n# silent (see the helper module). Epochs are sample (pole in to pole out), delay (pole out to\n# cue) and response (cue to 1.3 s after). Trials with early licks are dropped, and each unit\n# uses its stable trials (first to last trial with a spike). The trial type is the R or L of\n# `response`. Units are the putative pyramidal neurons as labelled in the files, unless a claim\n# says otherwise. A unit is selective when a two-tailed t-test on spike rates of correct\n# control trials, lick right against lick left, has p < 0.05 in the sample, delay or response\n# epoch. Photostimulation effects use control (code 0) against photostimulation trials, correct\n# and error trials together, grouped by instructed type where selectivity is computed.\nschema_version: 1\ndandiset: \"000007\"\npaper: doi:10.1038/s41586-018-0633-x\nclaims:\n- id: stim-code-link\n  statement: The dandiset's photostimulation codes 1 to 6 can be named from the paper's Zenodo\n    data description (1 and 2 fastigial photo-activation in the sample and delay epochs, 3 and 4\n    dentate photo-activation in the sample and delay, 5 and 6 CN photo-inhibition in the delay\n    for 0.5 and 1.3 s), and the ALM responses agree with those names.\n  source: Data description of Zenodo records 6647629 and 6653158; Methods\n  data: with_labels\n  criterion: Codes are matched by their integer value. Reproduced when (1) codes 1 and 2 occur\n    only in the mice with ChR2 in the fastigial nucleus, 3 and 4 only in the dentate mice and 5\n    and 6 only in the L7-cre mice; (2) for each code the population change in ALM firing\n    (mean over units of the absolute difference from control trials, 10 ms bins) first exceeds\n    the pre-trial level by 4 standard deviations within 50 ms after the stated onset (pole in\n    for the sample codes, pole out for the delay codes), and not before it; and (3) the change\n    after code 5 ends earlier than after code 6 (smaller mean change 0.7 to 1.2 s after onset).\n    Partially reproduced when (1) and (2) hold and (3) does not.\n- id: methods-alm-unit-counts\n  statement: The ALM recordings comprise 912 putative pyramidal neurons in the 9 mice tested\n    with CN photo-activation (446 with fastigial and 466 with dentate photo-activation), and\n    490 single units (454 putative pyramidal) in 4 mice across 19 sessions during CN\n    photo-inhibition.\n  source: Methods, Electrophysiology data analysis; Figure 4f and 4g legends\n  expected:\n  - quantity: putative pyramidal neurons, photo-activation mice\n    value: 912\n    tolerance: 91.2\n  - quantity: putative pyramidal neurons, fastigial photo-activation mice\n    value: 446\n    tolerance: 44.6\n  - quantity: putative pyramidal neurons, dentate photo-activation mice\n    value: 466\n    tolerance: 46.6\n  - quantity: single units, photo-inhibition mice\n    value: 490\n    tolerance: 49\n  - quantity: putative pyramidal neurons, photo-inhibition mice\n    value: 454\n    tolerance: 45.4\n  - quantity: sessions, photo-inhibition mice\n    value: 19\n    tolerance: 1.9\n  criterion: Pyramidal neurons are counted under two readings, (a) the files' cell type label\n    and (b) the Methods' width rule (trough to peak above 0.45 ms). Reproduced when every count\n    is within tolerance under one reading, partially reproduced when at least half are, not\n    reproduced otherwise.\n- id: fig1g-fn-delay-performance\n  statement: Fastigial photo-activation during the early delay epoch reduced behavioural\n    performance (incorrect choices).\n  source: Results, paragraph 4; Figure 1g; Extended Data Figure 10b\n  data: with_labels\n  depends_on:\n  - stim-code-link\n  criterion: Performance (fraction correct, without early-lick and no-lick trials) on code 2\n    trials against control trials in the fastigial mice, trial types pooled. Reproduced when\n    performance is lower with photostimulation and the one-tailed hierarchical bootstrap\n    (mice, sessions, trials; 10,000 resamples) gives p < 0.05.\n- id: fig1-fn-sample-no-effect\n  statement: Fastigial photo-activation during the early sample epoch had no effect on\n    behavioural choice (p > 0.05 for either trial type, bootstrap).\n  source: Results, paragraph 4\n  data: with_labels\n  depends_on:\n  - stim-code-link\n  criterion: A claim of absence, judged on the paper's test, the one-tailed hierarchical\n    bootstrap of the performance change on code 1 trials, for lick right and lick left trials\n    separately. Reproduced when neither trial type shows a decrease with p < 0.05; not\n    reproduced when either does.\n- id: fig1g-dn-little-effect\n  statement: Dentate photo-activation produced little effect on behavioural choice (p = 0.06,\n    bootstrap).\n  source: Results, paragraph 5; Figure 1g\n  data: with_labels\n  depends_on:\n  - stim-code-link\n  criterion: A claim of absence, judged on the paper's test, the one-tailed hierarchical\n    bootstrap of the performance change with delay-epoch dentate photo-activation (code 4),\n    trial types pooled. Reproduced when the decrease has p >= 0.05; not reproduced when p <\n    0.05. The size of the change is reported either way.\n- id: fig1h-fn-delay-bias-either-direction\n  statement: Fastigial photo-activation during the delay epoch biased future movements to\n    either the contralateral or the ipsilateral direction in individual mice.\n  source: Results, paragraph 4; Figure 1h; Extended Data Figure 1e\n  data: with_labels\n  depends_on:\n  - stim-code-link\n  criterion: For each fastigial mouse, the bias is the performance change on ipsilateral\n    trials minus that on contralateral trials (trial types relative to the manipulated\n    hemisphere; a contralateral trial instructs licking to the side opposite the stimulated\n    nucleus), on code 2 trials, with a bootstrap over that mouse's sessions and trials (10,000\n    resamples, two-tailed p < 0.05). Reproduced when at least one mouse is significantly biased\n    in each direction; partially reproduced when mice are biased in one direction only.\n- id: ed1f-fn-no-early-licks\n  statement: Fastigial photo-activation during the delay epoch did not evoke early licks.\n  source: Results, paragraph 5; Extended Data Figure 1f\n  data: with_labels\n  depends_on:\n  - stim-code-link\n  criterion: A claim of absence. The paper gives no test; the test fixed here is the one-tailed\n    hierarchical bootstrap of the increase in the early-lick rate on code 2 trials against\n    control trials. Reproduced when p >= 0.05; not reproduced when the increase has p < 0.05.\n- id: fig1k-pi-delay-performance\n  statement: CN photo-inhibition during the delay epoch resulted in incorrect behavioural\n    choices.\n  source: Results, paragraph 6; Figure 1k; Extended Data Figure 2g and 2h\n  data: with_labels\n  depends_on:\n  - stim-code-link\n  criterion: Performance on photo-inhibition trials (codes 5 and 6 pooled) against control\n    trials in the L7-cre mice, trial types pooled. Reproduced when performance is lower and the\n    one-tailed hierarchical bootstrap gives p < 0.05. Codes 5 and 6 are also shown apart.\n- id: fig1d-fn-lesion\n  statement: Fastigial lesions impaired initiation of contralesional licking, while dentate\n    lesions did not change behavioural choice or movement execution.\n  source: Results, paragraph 3; Figure 1d\n- id: fig1e-lesion-lick-timing\n  statement: Fastigial lesions slowed initiation of contralesional licking after the go cue,\n    and licking after initiation was unaffected.\n  source: Results, paragraph 3; Figure 1e; Extended Data Figure 1b and 1c\n- id: fig1h-response-contra-bias\n  statement: Fastigial photo-activation immediately before movement onset (response epoch)\n    produced a contralateral bias.\n  source: Results, paragraph 4; Figure 1h\n- id: fig1i-licking-unaffected\n  statement: Fastigial photo-activation did not block or perturb the frequency and duration of\n    licking after initiation of lick bouts, and CN photo-inhibition minimally affected movement\n    execution.\n  source: Results, paragraphs 5 and 6; Figure 1i and 1l\n- id: fig1k-response-ipsi-bias\n  statement: CN photo-inhibition during the response epoch produced an ipsilateral bias, and\n    photo-inhibition during the early sample epoch did not affect choice.\n  source: Results, paragraph 6; Figure 1k; Extended Data Figure 2g\n- id: ed2-pi-silences-fastigial\n  statement: Photostimulation of Purkinje cells in L7-cre x Ai32 mice silenced fastigial\n    neurons, and at the intensities used in the task evoked no consistent movement.\n  source: Figure 1j; Extended Data Figure 2b to 2f\n- id: fig2-alm-selective-fraction\n  statement: Most ALM pyramidal neurons distinguished lick left and lick right trials\n    (980/1194, p < 0.05, two-tailed t-test).\n  source: Results, paragraph 7\n  expected:\n    quantity: fraction of ALM putative pyramidal neurons that are selective\n    value: 0.821\n    tolerance: 0.082\n  criterion: The paper's 1194 neurons come from the 10 mice recorded during behaviour (Figure 2;\n    Supplemental Table 1), the 9 photo-activation mice of the dandiset and one excluded mouse.\n    The readings are (a) the pyramidal neurons of the 9 photo-activation mice and (b) those of\n    all 13 mice. Reproduced when the fraction is within tolerance under one reading.\n- id: fig2-alm-preparatory-fraction\n  statement: Preparatory activity (selectivity before the response epoch) was present in 59% of\n    ALM neurons.\n  source: Results, paragraph 7\n  expected:\n    quantity: fraction of ALM neurons selective in the sample or delay epoch\n    value: 0.59\n    tolerance: 0.059\n  criterion: Readings (a) and (b) as in fig2-alm-selective-fraction; the denominator is all\n    pyramidal neurons, as \"59% of neurons\" reads. Reproduced when the fraction is within\n    tolerance under one reading.\n- id: fig2-alm-perimovement-fraction\n  statement: Peri-movement activity (selectivity in the response epoch) was present in 67% of\n    ALM neurons.\n  source: Results, paragraph 7\n  expected:\n    quantity: fraction of ALM neurons selective in the response epoch\n    value: 0.67\n    tolerance: 0.067\n  criterion: Readings (a) and (b) as in fig2-alm-selective-fraction. Reproduced when the fraction\n    is within tolerance under one reading.\n- id: fig2c-alm-selectivity-time-course\n  statement: Selectivity for lick left and lick right trials emerged gradually in the ALM\n    population average, starting during the sample epoch and reaching a maximum in the\n    response epoch.\n  source: Results, paragraph 8; Figure 2c\n  depends_on:\n  - fig2-alm-selective-fraction\n  criterion: Selective pyramidal neurons of the 9 photo-activation mice with at least 15\n    correct control trials of each type; the preferred type from 10 random trials of each type\n    (delay epoch counts), selectivity (preferred minus non-preferred rate, 200 ms box-car) on\n    the rest. Reproduced when (1) the mean selectivity over the last 300 ms of the sample epoch\n    is above 0 (bootstrap over neurons, 95% interval above 0) and (2) the maximum of the mean\n    selectivity between pole in and 1.3 s after the cue lies in the response epoch.\n- id: fig2-cn-unit-counts\n  statement: 878 CN-region single units were recorded in 18 mice across 169 sessions, 314 from\n    outside the CN, 268 in the fastigial, 139 in the interposed and 157 in the dentate nucleus.\n  source: Methods, Electrophysiology data analysis\n  data: elsewhere\n  where: Zenodo doi:10.5281/zenodo.6647629 (datafiles_NWB.zip)\n  expected:\n  - quantity: single units\n    value: 878\n    tolerance: 87.8\n  - quantity: units outside the CN\n    value: 314\n    tolerance: 31.4\n  - quantity: fastigial units\n    value: 268\n    tolerance: 26.8\n  - quantity: interposed units\n    value: 139\n    tolerance: 13.9\n  - quantity: dentate units\n    value: 157\n    tolerance: 15.7\n  - quantity: sessions\n    value: 169\n    tolerance: 16.9\n  criterion: Unit locations from each unit's cell type comment in the files. Reproduced when all\n    six counts are within tolerance, partially reproduced when at least three are.\n- id: fig2-cn-selective-fraction\n  statement: A similar proportion of CN neurons as of ALM neurons showed trial-type selectivity\n    (416/564).\n  source: Results, paragraph 7\n  data: elsewhere\n  where: Zenodo doi:10.5281/zenodo.6647629 (datafiles_NWB.zip)\n  expected:\n    quantity: fraction of CN neurons that are selective\n    value: 0.738\n    tolerance: 0.074\n  criterion: CN units are those located in the fastigial, interposed or dentate nucleus, with\n    the test of the paper's script analysis_compile_all_DCN_data.m (correct, control,\n    non-early-lick, performing trials; any epoch p < 0.05). Reproduced when within tolerance.\n- id: fig2-cn-preparatory-fraction\n  statement: Preparatory activity was more prevalent in ALM than in CN (59% against 35% of\n    neurons, p < 0.001, chi-square test).\n  source: Results, paragraph 7\n  data: elsewhere\n  where: Zenodo doi:10.5281/zenodo.6647629 (datafiles_NWB.zip), with the ALM neurons of the\n    dandiset\n  expected:\n    quantity: fraction of CN neurons selective in the sample or delay epoch\n    value: 0.35\n    tolerance: 0.035\n  criterion: Reproduced when the CN fraction is within tolerance and a chi-square test of the\n    ALM fraction (reading (a) of fig2-alm-preparatory-fraction) against the CN fraction gives\n    p < 0.001 with ALM higher. Partially reproduced when the test holds and the CN fraction is\n    outside tolerance.\n- id: fig2-cn-perimovement-fraction\n  statement: Peri-movement activity was equally prevalent in ALM and CN (67% against 66%).\n  source: Results, paragraph 7\n  data: elsewhere\n  where: Zenodo doi:10.5281/zenodo.6647629 (datafiles_NWB.zip)\n  expected:\n    quantity: fraction of CN neurons selective in the response epoch\n    value: 0.66\n    tolerance: 0.066\n- id: ed4e-cn-predict-movement\n  statement: Most CN neurons with delay selectivity predicted the upcoming licking direction,\n    switching their trial-type preference on error trials (67%, n = 73 neurons tested on more\n    than 3 error trials).\n  source: Results, paragraph 8; Extended Data Figure 4e\n  data: elsewhere\n  where: Zenodo doi:10.5281/zenodo.6647629 (datafiles_NWB.zip)\n  expected:\n  - quantity: fraction of neurons with a negative error to correct selectivity ratio\n    value: 0.67\n    tolerance: 0.067\n  - quantity: neurons tested\n    value: 73\n    tolerance: 7.3\n  criterion: CN neurons with significant delay selectivity and more than 3 error trials of each\n    type; the ratio is the delay selectivity (lick right minus lick left by instructed type) on\n    error trials over that on correct trials. Reproduced when the fraction is within tolerance;\n    the count is reported.\n- id: ed4g-fn-contra-late-delay\n  statement: In the fastigial nucleus, equal numbers of neurons preferred contralateral or\n    ipsilateral movement in the early delay, and a population preference for contralateral\n    movement developed right before movement initiation.\n  source: Results, paragraph 9; Extended Data Figure 4g\n  data: elsewhere\n  where: Zenodo doi:10.5281/zenodo.6647629 (datafiles_NWB.zip)\n  criterion: Fastigial units (all recorded in the left CN, so contralateral is lick right)\n    significant (t-test p < 0.05, correct control trials) in the first or in the last 500 ms of\n    the delay; per mouse the fraction of those preferring contralateral in each window. One-\n    tailed bootstrap over mice (10,000). Reproduced when the late fraction exceeds 0.5 with p <\n    0.05 and the early fraction does not differ from 0.5 (two-tailed p >= 0.05); partially\n    reproduced when only the late part holds.\n- id: ed4c-lick-modulation\n  statement: In ALM and CN a similar small proportion (below 10%) of neurons modulated their\n    spike rates during individual licks.\n  source: Results, paragraph 7; Extended Data Figure 4a to 4c\n  data: elsewhere\n  where: Zenodo doi:10.5281/zenodo.6653158 (MATLAB datafiles, with the lick traces of the ALM\n    sessions)\n- id: fig3b-cn-modulated-fraction\n  statement: Activity of many CN neurons was rapidly altered by bilateral ALM photo-inhibition\n    (185/389, p < 0.01, two-tailed t-test).\n  source: Results, paragraph 10; Figure 3b\n  data: elsewhere\n  where: Zenodo doi:10.5281/zenodo.6647629 (datafiles_NWB.zip)\n  expected:\n    quantity: fraction of CN neurons modulated by ALM photo-inhibition\n    value: 0.476\n    tolerance: 0.048\n  criterion: CN units (fastigial, interposed or dentate) of sessions with bilateral ALM\n    photo-inhibition (code 9); delay-epoch spike counts, control against code 9 trials, trial\n    types pooled, p < 0.01. Reproduced when within tolerance; the count is reported.\n- id: fig3b-cn-net-increase\n  statement: ALM photo-inhibition caused more CN neurons to increase than to decrease their\n    activity (123/185 increase, p < 0.001, binomial test).\n  source: Results, paragraph 10; Figure 3b\n  data: elsewhere\n  where: Zenodo doi:10.5281/zenodo.6647629 (datafiles_NWB.zip)\n  depends_on:\n  - fig3b-cn-modulated-fraction\n  expected:\n    quantity: fraction of modulated CN neurons that increased\n    value: 0.665\n    tolerance: 0.066\n  criterion: Reproduced when the fraction is within tolerance and a two-tailed binomial test\n    against 0.5 gives p < 0.001.\n- id: fig3-cn-latency\n  statement: The CN response to ALM photo-inhibition had a latency of 10.7 +/- 4.0 ms (mean +/-\n    s.e.m.).\n  source: Results, paragraph 10\n  data: elsewhere\n  where: Zenodo doi:10.5281/zenodo.6647629 (datafiles_NWB.zip)\n  depends_on:\n  - fig3b-cn-modulated-fraction\n  expected:\n    quantity: onset latency\n    value: 10.7\n    tolerance: 4.0\n    unit: ms\n  criterion: The latency method of Extended Data Figure 9a, on the modulated CN neurons,\n    aligned to delay onset.\n- id: fig3c-cn-selectivity-abolished\n  statement: CN selectivity for lick left and lick right trials was abolished by bilateral ALM\n    photo-inhibition.\n  source: Results, paragraph 10; Figure 3c; Extended Data Figure 5b to 5d\n  data: elsewhere\n  where: Zenodo doi:10.5281/zenodo.6647629 (datafiles_NWB.zip)\n  criterion: As in the paper's script analysis_compiled_all_DCN_ALMsilencing_selectivity.m, CN\n    units selective in the sample or delay epoch (correct and error trials by instructed type),\n    with at least 30 control trials of each type and more than 2 code 9 trials of each type;\n    preferred type from the delay rate of 20 random control trials of each type; selectivity\n    is the preferred minus non-preferred rate in the delay epoch on the remaining control\n    trials and on code 9 trials. Reproduced when the photo-inhibition selectivity is at most\n    25% of control; partially reproduced when it is lower than control (bootstrap over neurons,\n    one-tailed p < 0.05) but above 25%; not reproduced otherwise.\n- id: ed6-cn-either-hemisphere\n  statement: Photo-inhibiting either side of ALM reduced CN preparatory activity.\n  source: Results, paragraph 11; Extended Data Figure 6a to 6d\n  data: elsewhere\n  where: Zenodo doi:10.5281/zenodo.6647629 (datafiles_NWB.zip)\n  criterion: As fig3c-cn-selectivity-abolished, for left (code 7) and right (code 8) ALM\n    photo-inhibition. Reproduced when selectivity is lower than control for both (one-tailed\n    bootstrap p < 0.05 each); partially reproduced when for one.\n- id: fig3e-alm-modulated-fraction\n  statement: Activity of many ALM neurons was rapidly altered by CN photo-inhibition (197/454,\n    p < 0.01, two-tailed t-test).\n  source: Results, paragraph 12; Figure 3e; Extended Data Figure 5e\n  data: with_labels\n  depends_on:\n  - stim-code-link\n  expected:\n    quantity: fraction of ALM pyramidal neurons modulated by CN photo-inhibition\n    value: 0.434\n    tolerance: 0.043\n  criterion: Pyramidal neurons of the L7-cre mice; delay-epoch spike counts of control against\n    photo-inhibition trials, trial types pooled, p < 0.01. The Methods state a 1.3 s\n    photostimulus, and the files hold 0.5 s (code 5) and 1.3 s (code 6) trials. Readings (a)\n    code 6 trials and (b) codes 5 and 6 pooled. Reproduced when within tolerance under one\n    reading.\n- id: fig3e-alm-mean-rate-unchanged\n  statement: CN photo-inhibition left the average ALM spike rate nearly unchanged (control 4.15,\n    photo-inhibition 4.39 spikes/s, p = 0.58, two-tailed t-test).\n  source: Results, paragraph 12\n  data: with_labels\n  depends_on:\n  - stim-code-link\n  expected:\n  - quantity: mean delay-epoch rate, control\n    value: 4.15\n    tolerance: 0.415\n    unit: spikes/s\n  - quantity: mean delay-epoch rate, photo-inhibition\n    value: 4.39\n    tolerance: 0.439\n    unit: spikes/s\n  criterion: Per-neuron mean delay-epoch rates on control and on code 6 trials, over the\n    pyramidal neurons of the L7-cre mice. The absence is judged on a two-sample two-tailed\n    t-test across neurons (the paper's form is not stated; the paired test is shown as a\n    variant). Reproduced when both rates are within tolerance and the test gives p >= 0.05;\n    partially reproduced when the test gives p >= 0.05 and a rate is outside tolerance; not\n    reproduced when p < 0.05.\n- id: fig3e-alm-up-down\n  statement: Individual ALM neurons increased (108/197) or decreased (89/197) their responses\n    during CN photo-inhibition.\n  source: Results, paragraph 12; Figure 3e\n  data: with_labels\n  depends_on:\n  - fig3e-alm-modulated-fraction\n  expected:\n    quantity: fraction of modulated ALM neurons that increased\n    value: 0.548\n    tolerance: 0.055\n  criterion: Under the reading of fig3e-alm-modulated-fraction that matched (the first listed\n    if both or neither did). Reproduced when within tolerance.\n- id: fig3-alm-latency-pi\n  statement: The ALM response to CN photo-inhibition had a latency of 7.1 +/- 3.8 ms (mean +/-\n    s.e.m.).\n  source: Results, paragraph 12\n  data: with_labels\n  depends_on:\n  - fig3e-alm-modulated-fraction\n  expected:\n    quantity: onset latency\n    value: 7.1\n    tolerance: 3.8\n    unit: ms\n  criterion: The method of Extended Data Figure 9a on the modulated neurons of\n    fig3e-alm-modulated-fraction (same reading), rate change in 10 ms bins stepped by 1 ms from\n    20 ms before to 100 ms after delay onset, with the sign of suppressed neurons flipped; the\n    onset is the centre of the first bin whose change across neurons is above 0 (one-sample\n    t-test p < 0.01); mean and standard deviation over 10,000 resamples of neurons. Reproduced\n    when the mean is within tolerance.\n- id: fig3f-alm-selectivity-abolished\n  statement: ALM trial-type selectivity was abolished by CN photo-inhibition.\n  source: Results, paragraph 12; Figure 3f\n  data: with_labels\n  depends_on:\n  - stim-code-link\n  criterion: Pyramidal neurons of the L7-cre mice selective in the sample or delay epoch (correct\n    and error trials by instructed type, control trials) with more than 3 photo-inhibition\n    trials of each type and at least 15 control trials of each type; preferred type from the\n    delay rate of 10 random control trials of each type; selectivity is the preferred minus\n    non-preferred delay-epoch rate on the remaining control trials and on code 6 trials.\n    Reproduced when the photo-inhibition selectivity is at most 25% of control; partially\n    reproduced when it is lower than control (bootstrap over neurons, one-tailed p < 0.05) but\n    above 25%; not reproduced otherwise. Codes 5 and 6 pooled are shown as a variant.\n- id: ed9a-fn-latency\n  statement: Fastigial photo-activation induced rapid changes in ALM activity, with a latency\n    of 4.5 +/- 2.6 ms, in 227 significantly modulated neurons.\n  source: Results, paragraph 14; Extended Data Figure 9a\n  data: with_labels\n  depends_on:\n  - stim-code-link\n  expected:\n  - quantity: onset latency\n    value: 4.5\n    tolerance: 2.6\n    unit: ms\n  - quantity: neurons significantly modulated\n    value: 227\n    tolerance: 22.7\n  criterion: Pyramidal neurons of the fastigial mice; modulated when the spike count in the 0.5 s\n    after photostimulus onset differs between control and photostimulation trials (p < 0.01);\n    latency as in fig3-alm-latency-pi aligned to photostimulus onset. Readings (a) delay\n    photostimulation (code 2) and (b) codes 1 and 2 pooled, each aligned to its own onset.\n    Reproduced when both values are within tolerance under one reading; partially reproduced\n    when the latency is and the count is not.\n- id: ed9a-dn-latency\n  statement: Dentate photo-activation also induced ALM response changes, with a latency of 8.3\n    +/- 5.0 ms, in 163 significantly modulated neurons.\n  source: Results, paragraph 14; Extended Data Figure 9a\n  data: with_labels\n  depends_on:\n  - stim-code-link\n  expected:\n  - quantity: onset latency\n    value: 8.3\n    tolerance: 5.0\n    unit: ms\n  - quantity: neurons significantly modulated\n    value: 163\n    tolerance: 16.3\n  criterion: As ed9a-fn-latency, for the dentate mice and codes 4 (reading a) and 3 and 4\n    (reading b).\n- id: fig4f-fn-persistent\n  statement: Transient photo-activation of the fastigial nucleus altered ALM preparatory activity\n    long (more than 1 s) after the photostimulus ended.\n  source: Results, paragraph 14; Figure 4f; Extended Data Figure 9b\n  data: with_labels\n  depends_on:\n  - stim-code-link\n  criterion: Pyramidal neurons of the fastigial mice, delay photostimulation (code 2). For each\n    400 ms bin (50 ms steps) the fraction of neurons whose spike counts differ between control\n    and code 2 trials (two-tailed t-test, p < 0.01). Reproduced when the fraction in the bin\n    from 1.0 to 1.4 s after photostimulus offset is more than twice the fraction in the bin\n    ending at photostimulus onset and higher than it by a one-tailed Fisher exact test (p <\n    0.05).\n- id: fig4g-dn-recovery\n  statement: ALM activity quickly recovered after dentate photo-activation.\n  source: Results, paragraph 14; Figure 4g\n  data: with_labels\n  depends_on:\n  - stim-code-link\n  criterion: As fig4f-fn-persistent, for the dentate mice and code 4. Reproduced when, in the\n    bin from 1.0 to 1.4 s after offset, the dentate fraction is less than twice its own fraction\n    in the bin ending at onset and lower than the fastigial fraction in the same bin (two-tailed\n    Fisher exact test, p < 0.05).\n- id: fig4i-fn-cd-collapse\n  statement: Fastigial photo-activation resulted in a collapse of ALM activity trajectories\n    along the coding direction, destroying the coding of future movement.\n  source: Results, paragraph 15; Figure 4i\n  data: with_labels\n  depends_on:\n  - stim-code-link\n  criterion: Sessions of the fastigial mice with more than 5 pyramidal neurons and more than 5\n    trials of each type in each condition. The coding direction from a random half of the\n    correct control trials (400 ms windows stepped by 10 ms, the lick right minus lick left\n    mean, averaged over the delay epoch); projections of the other control trials and of all\n    code 2 trials (correct and error, by instructed type), offset by the mean projection of\n    the training trials. Separation is the lick right minus lick left projection in the last\n    400 ms of the delay; the ratio is its mean over sessions for code 2 over that for control,\n    with a bootstrap over sessions (10,000). Reproduced when the ratio is below 0.5 and its\n    upper 95% bound below 1; partially reproduced when the upper bound is below 1 and the ratio\n    is 0.5 or more.\n- id: fig4i-dn-cd-minimal\n  statement: Dentate photo-activation minimally impacted ALM activity trajectories along the\n    coding direction, despite having an impact on ALM neuron responses.\n  source: Results, paragraph 15; Figure 4i; Extended Data Figure 9c\n  data: with_labels\n  depends_on:\n  - stim-code-link\n  criterion: As fig4i-fn-cd-collapse, for the dentate mice and code 4. Reproduced when the ratio\n    is above 0.75 and lower for the fastigial than for the dentate photo-activation in at least\n    95% of paired bootstrap resamples; partially reproduced when the ratio is between 0.5 and\n    0.75.\n- id: ed10d-fn-no-prediction\n  statement: After fastigial photo-activation, ALM activity along the coding direction no longer\n    predicted the future movement direction (n = 337 trials).\n  source: Supplementary Information; Extended Data Figure 10d\n  data: with_labels\n  depends_on:\n  - stim-code-link\n  expected:\n    quantity: fastigial photo-activation trials analysed\n    value: 337\n    tolerance: 33.7\n  criterion: Sessions and coding direction as in fig4i-fn-cd-collapse; the projection in the\n    last 400 ms of the delay, minus the midpoint of the two training-trial endpoints. A\n    claim of absence; the paper gives no test, the test fixed here is a logistic regression of\n    licking right on the projection, pooled over sessions. Reproduced when the slope on code 2\n    trials has p >= 0.05 while the slope on held-out control trials has p < 0.05; not\n    reproduced when the code 2 slope has p < 0.05. The trial count is reported.\n- id: ed10c-alm-pi-endpoints\n  statement: After bilateral ALM photo-inhibition the distance of ALM trajectories to the\n    endpoints along the coding direction still predicted future movements (n = 690 trials).\n  source: Supplementary Information; Extended Data Figure 10c\n- id: ed10efg-alm-needed-after-fn\n  statement: ALM activity remained necessary for directional licking after a fastigial\n    perturbation, as unilateral and bilateral ALM photo-inhibition affected licking with or\n    without a preceding fastigial perturbation.\n  source: Supplementary Information; Extended Data Figure 10e to 10g\n- id: fig4bc-fastigial-thalamus\n  statement: Fastigial projections mostly overlapped with the parts of the thalamus that project\n    to ALM (VM and parts of VAL), while dentate projections targeted an adjacent region.\n  source: Results, paragraph 13; Figure 4a to 4c; Extended Data Figures 7 and 8\n"
}
```

```
File created successfully at: claims/000007/10.1038-s41586-018-0633-x.yaml (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd  python3 - <<'E'
import yaml,json,jsonschema
d=yaml.safe_load(open('claims/000007/10.1038-s41586-018-0633-x.yaml'))
jsonschema.validate(d,json.load(open('schemas/claims.schema.json')))
print(len(d['claims']))
import collections; print(collections.Counter(c.get('data','dandiset') for c in d['claims']))
for c in d['claims']:
    for k,v in c.items():
        if isinstance(v,str) and ': ' in v: print('COLON',c['id'],k)
E
grep -n "—\|rather" claims/000007/*.yaml
```

```
45
Counter({'with_labels': 19, 'dandiset': 14, 'elsewhere': 12})
```

**Agent**

Claims file written (45 claims: 14 dandiset, 19 with labels, 12 elsewhere). Now developing the main notebook's analyses against a local cache of the loaded sessions (the notebook itself streams).

**Agent calls Bash**

```bash
mkdir -p $TMPDIR/dev; cat > $TMPDIR/dev/c01_sanity.py <<'E'
import pickle, numpy as np, pandas as pd, gao2018 as g
from scipy import stats
pd.set_option("display.width", 220); pd.set_option("display.max_columns", 40); pd.set_option("display.max_rows", 200)
sessions=pickle.load(open('/tmp/claude-1001/S.pkl','rb'))
#--- cell
inv = pd.DataFrame([{
    "group": s["group"], "subject": s["subject"], "session": s["session"], "genotype": s["genotype"],
    "site": f'{s["site"]} {s["site_hemisphere"]}', "virus": ";".join(f'{v["brain_location"]} {v["hemisphere"]}' for v in s["virus"]),
    "probe": s["probe"], "rec_ml": s["rec_ml"], "trials": len(s["trials"]), "units": len(s["spikes"]),
    "pyramidal": int((s["cell_type"] == "pyramidal").sum()), "FS": int((s["cell_type"] == "FS").sum()),
    "other_label": int((~np.isin(s["cell_type"], ["pyramidal", "FS"])).sum()),
    "codes": " ".join(f"{c}:{n}" for c, n in s["trials"].stim.value_counts().sort_index().items())} for s in sessions])
print("Groups: FN = ChR2 virus in the fastigial nucleus, DN = in the dentate nucleus, PI = L7-cre x Ai32 (CN photo-inhibition)")
print(inv.groupby(["group", "subject"]).agg(sessions=("session", "size"), trials=("trials", "sum"), units=("units", "sum"),
      pyramidal=("pyramidal", "sum"), FS=("FS", "sum"), other=("other_label", "sum")).to_string())
print("\nTotals by group:"); print(inv.groupby("group")[["trials", "units", "pyramidal", "FS", "other_label"]].sum().assign(sessions=inv.groupby("group").size()).to_string())
print("\nSubjects:", inv.subject.nunique(), " sessions:", len(inv))
print("\nPer subject: genotype, stimulation site, virus, probe, recording ML (mm):")
print(inv.drop_duplicates("subject")[["group", "subject", "genotype", "site", "virus", "probe", "rec_ml"]].to_string(index=False))
alltr = pd.concat([s["trials"].assign(group=s["group"], subject=s["subject"]) for s in sessions])
print("\nTrials by group and photostimulation code:"); print(pd.crosstab(alltr.group, alltr.stim).to_string())
print("\nTrials by response:"); print(alltr.response.value_counts().to_string())
print("early-lick trials:", int(alltr.lick_early.sum()), "of", len(alltr))
E
cd entries/000007-gao-2018; . $TMPDIR/explore/bin/activate; python $TMPDIR/dev/c01_sanity.py
```

```
Exit code 1
Traceback (most recent call last):
  File "/tmp/claude-1001/dev/c01_sanity.py", line 1, in <module>
    import pickle, numpy as np, pandas as pd, gao2018 as g
ModuleNotFoundError: No module named 'gao2018'
```

**Agent calls Bash**

```bash
cd entries/000007-gao-2018; . $TMPDIR/explore/bin/activate; PYTHONPATH=. python $TMPDIR/dev/c01_sanity.py
```

```
Exit code 1
Groups: FN = ChR2 virus in the fastigial nucleus, DN = in the dentate nucleus, PI = L7-cre x Ai32 (CN photo-inhibition)
                   sessions  trials  units  pyramidal  FS  other
group subject                                                   
DN    BAYLORNL12          5    1910    244        231  13      0
      BAYLORNL14          6    2283    308        288  20      0
      anm00314756         2     457     26         26   0      0
FN    BAYLORCD6           4     941    196        187   8      1
      BAYLORNL15          5    1547    177        160  17      0
      anm00314746         3     780     63         60   3      0
      anm00314757         2     280     38         35   3      0
      anm00314758         4    1005     62         61   1      0
      anm00314760         3     745     72         64   8      0
PI    BAYLORCD12          5    1205    160        153   6      1
      BAYLORCD13          5     967    100         96   4      0
      BAYLORCD14          5    1719    195        185   9      1
      BAYLORCD8           5    1795    282        272  10      0

Totals by group:
       trials  units  pyramidal  FS  other_label  sessions
[... 66 more lines not kept]
```

**Agent calls Bash**

```bash
cat > $TMPDIR/dev/build.py <<'E'
"""Build notebook from a percent-format source; or emit a dev script that uses the cache."""
import sys, re, nbformat
src, out = sys.argv[1], sys.argv[2]
text = open(src).read()
cells = []
for block in re.split(r"^# %%", text, flags=re.M)[1:]:
    header, _, body = block.partition("\n")
    body = body.strip("\n")
    tags = re.findall(r'tags=\[([^\]]*)\]', header)
    tags = [t.strip().strip('"\'') for t in tags[0].split(",")] if tags else []
    if "[markdown]" in header:
        body = "\n".join(l[2:] if l.startswith("# ") else l[1:] if l.startswith("#") else l for l in body.split("\n"))
        c = nbformat.v4.new_markdown_cell(body)
    else:
        c = nbformat.v4.new_code_cell(body)
    if tags: c.metadata["tags"] = tags
    cells.append(c)
if out.endswith(".ipynb"):
    nb = nbformat.v4.new_notebook(); nb.cells = cells
    nb.metadata["kernelspec"] = {"display_name": "Python 3", "language": "python", "name": "python3"}
    nbformat.write(nb, out)
else:
    upto = sys.argv[3] if len(sys.argv) > 3 else None
    code = []
    for c in cells:
        if c.cell_type == "code":
            s = c.source.replace("sessions = gao2018.load_all()", "import pickle; sessions = pickle.load(open('/tmp/claude-1001/S.pkl','rb'))")
            code.append(f"print('\\n######## CELL {c.metadata.get('tags', [])}')\n" + s)
    open(out, "w").write("\n\n".join(code))
E
echo ok
```

```
ok
```

**Agent calls Write**

```json
{
 "file_path": "/tmp/claude-1001/dev/nb_main.py",
 "content": "# %% [markdown]\n# HEADER\n\n# %%\nimport time\nimport warnings\n\nimport matplotlib.pyplot as plt\nimport numpy as np\nimport pandas as pd\nfrom scipy import stats\nfrom sklearn.linear_model import LogisticRegression\nfrom sklearn.model_selection import cross_val_score, StratifiedKFold\n\nimport gao2018\n\npd.set_option(\"display.width\", 220)\npd.set_option(\"display.max_columns\", 40)\npd.set_option(\"display.max_rows\", 200)\nwarnings.filterwarnings(\"ignore\", category=RuntimeWarning)\n\nstarted = time.time()\nsessions = gao2018.load_all()\nprint(f\"loaded {len(sessions)} files from dandiset {gao2018.DANDISET_ID} version {gao2018.DANDISET_VERSION} \"\n      f\"in {time.time() - started:.0f} s\")\n\n# %% [markdown]\n# ## Data check\n#\n# Each check of the metadata against the values is stated under its output.\n\n# %% tags=[\"sanity\"]\ninv = pd.DataFrame([{\n    \"group\": s[\"group\"], \"subject\": s[\"subject\"], \"session\": s[\"session\"], \"genotype\": s[\"genotype\"],\n    \"site\": f'{s[\"site\"]} {s[\"site_hemisphere\"]}',\n    \"virus\": \";\".join(f'{v[\"brain_location\"]} {v[\"hemisphere\"]}' for v in s[\"virus\"]),\n    \"probe\": s[\"probe\"], \"rec_ml\": s[\"rec_ml\"], \"trials\": len(s[\"trials\"]), \"units\": len(s[\"spikes\"]),\n    \"pyramidal\": int((s[\"cell_type\"] == \"pyramidal\").sum()), \"FS\": int((s[\"cell_type\"] == \"FS\").sum()),\n    \"other_label\": int((~np.isin(s[\"cell_type\"], [\"pyramidal\", \"FS\"])).sum())} for s in sessions])\nprint(\"Groups: FN = ChR2 virus in the fastigial nucleus, DN = in the dentate nucleus, PI = L7-cre x Ai32 (CN photo-inhibition)\")\nprint(inv.groupby([\"group\", \"subject\"]).agg(sessions=(\"session\", \"size\"), trials=(\"trials\", \"sum\"), units=(\"units\", \"sum\"),\n      pyramidal=(\"pyramidal\", \"sum\"), FS=(\"FS\", \"sum\"), other=(\"other_label\", \"sum\")).to_string())\nprint(\"\\nTotals by group:\")\nprint(inv.groupby(\"group\")[[\"trials\", \"units\", \"pyramidal\", \"FS\", \"other_label\"]].sum()\n      .assign(sessions=inv.groupby(\"group\").size()).to_string())\nprint(\"\\nSubjects:\", inv.subject.nunique(), \"; sessions:\", len(inv), \"; cell type labels:\",\n      sorted(set(np.concatenate([s[\"cell_type\"] for s in sessions]))))\nprint(\"\\nPer subject: genotype, stimulation site, virus, probe, recording ML (mm from midline):\")\nprint(inv.drop_duplicates(\"subject\")[[\"group\", \"subject\", \"genotype\", \"site\", \"virus\", \"probe\", \"rec_ml\"]].to_string(index=False))\nalltr = pd.concat([s[\"trials\"].assign(group=s[\"group\"], subject=s[\"subject\"]) for s in sessions], ignore_index=True)\nprint(\"\\nTrials by group and photo_stim_id:\")\nprint(pd.crosstab(alltr.group, alltr.stim).to_string())\nprint(\"\\nTrials by response:\", alltr.response.value_counts().to_dict())\nprint(\"Early-lick trials:\", int(alltr.lick_early.sum()), \"of\", len(alltr))\nprint(\"Trial table columns:\", list(sessions[0][\"trials_columns\"]) if \"trials_columns\" in sessions[0] else\n      list(sessions[0][\"trial_descriptions\"]))\nprint(\"Units table columns:\", sessions[0][\"units_colnames\"])\n\n# %% [markdown]\n# The archive lists 13 subjects and 54 files, and the files hold 13 mice: 6 with ChR2 virus in the\n# fastigial nucleus (FN), 3 in the dentate nucleus (DN) and 4 L7-cre x Ai32 mice for CN\n# photo-inhibition (PI). This matches the ALM recordings of Supplemental Table 1 (6, 3 and 4 mice).\n# The FN and DN groups hold 34 sessions and the PI group 20, as the Zenodo data description says;\n# the Methods give 19 sessions for the PI group. The dandiset holds no CN recordings, no lick\n# times, no lesion or behaviour-only sessions, and no anatomy. The `photo_stim_id` codes (0 to 6)\n# have no description in the files or the dandiset metadata. Codes 1 and 2 occur only in FN mice,\n# 3 and 4 only in DN mice, and 5 and 6 only in PI mice. The trial table has no column marking the\n# periods when the mouse was not performing (`GoodTrials` in the paper's scripts); the many\n# `NoLick` trials at the ends of some sessions are such periods, and they drop out of performance\n# and of the correct-trial analyses here.\n\n# %% tags=[\"sanity\"]\n# Units and spike widths. The Methods classify units by trough-to-peak width: below 0.35 ms fast\n# spiking, above 0.45 ms putative pyramidal. The files give a cell type label, a sampling rate for\n# the waveform and a 30-sample mean waveform.\nrows = []\nfor s in sessions:\n    for ct, wf, hz in zip(s[\"cell_type\"], s[\"waveform\"], s[\"unit_rate_hz\"]):\n        rows.append({\"group\": s[\"group\"], \"probe\": s[\"probe\"][:12], \"label\": ct, \"rate_hz\": int(hz),\n                     \"width_ms\": round(gao2018.spike_width_ms(wf, hz), 3)})\nunits = pd.DataFrame(rows)\nprint(\"Waveform sampling rate stated, by probe:\", units.groupby(\"probe\").rate_hz.unique().to_dict())\nprint(\"Methods: 32-channel NeuroNexus recordings were sampled at 25,000 Hz, 64-channel at 20,000 Hz.\")\nprint(\"\\nWidth (ms) by label, at the stated rate:\")\nprint(units.groupby([\"probe\", \"label\"]).width_ms.describe()[[\"count\", \"min\", \"25%\", \"50%\", \"75%\", \"max\"]].to_string())\nunits[\"width_class\"] = pd.cut(units.width_ms, [0, gao2018.NARROW_MS - 1e-9, gao2018.WIDE_MS + 1e-9, 9],\n                              labels=[\"narrow (<0.35)\", \"intermediate\", \"wide (>0.45)\"])\nprint(\"\\nLabel against width class, at the stated rate:\")\nprint(pd.crosstab([units.probe, units.label], units.width_class).to_string())\nscaled = units.width_ms * np.where(units.probe.str.startswith(\"NN\"), 20000 / 25000, 1.0)\nunits[\"width_class_25k\"] = pd.cut(scaled, [0, gao2018.NARROW_MS - 1e-9, gao2018.WIDE_MS + 1e-9, 9],\n                                  labels=[\"narrow (<0.35)\", \"intermediate\", \"wide (>0.45)\"])\nprint(\"\\nThe same if the NeuroNexus waveforms were sampled at 25 kHz:\")\nprint(pd.crosstab([units.probe, units.label], units.width_class_25k).to_string())\ne = sessions[0]\nprint(\"\\nUnit observation intervals, first unit of each of 3 files:\", [s[\"obs\"][0].round(1).tolist() for s in sessions[:3]])\n\n# %% [markdown]\n# The files' labels follow the width rule closely but not exactly: a few units labelled pyramidal\n# have widths of 0.30 ms or less at the stated rate. The stated waveform rate is 20 kHz for every\n# unit, including the NeuroNexus recordings that the Methods say were sampled at 25 kHz; with 25\n# kHz the labels agree with the width classes in the same way (printed above), so the rate cannot\n# be settled from the widths. The analyses below use the files' labels; the width rule is a\n# variant in methods-alm-unit-counts. The electrode table gives no positions (x, y and z are NaN)\n# and no impedances (-1), so unit depth is not available.\n\n# %% tags=[\"sanity\"]\n# Trial times. The table's descriptions say pole_in_time, pole_out_time and cue_time are relative\n# to the trial start; the values are compared with start_time here.\nd = sessions[0][\"trial_descriptions\"]\nfor c in (\"start_time\", \"pole_in_time\", \"pole_out_time\", \"cue_time\"):\n    print(f\"{c}: {d[c]!r}\")\nlag = pd.DataFrame({\n    \"pole_in - start\": alltr.pole_in_time - alltr.start_time,\n    \"sample (pole_out - pole_in)\": alltr.pole_out_time - alltr.pole_in_time,\n    \"delay (cue - pole_out)\": alltr.cue_time - alltr.pole_out_time,\n    \"trial (stop - start)\": alltr.stop_time - alltr.start_time})\nprint(\"\\n\", lag.describe().round(3).to_string())\nprint(\"\\npole_in_time range over all trials:\", alltr.pole_in_time.min().round(1), \"to\", alltr.pole_in_time.max().round(1), \"s\")\nin_trials = []\nfor s in sessions:\n    sp = np.concatenate(s[\"spikes\"])\n    n_in = gao2018.counts(np.sort(sp), s[\"trials\"].start_time, s[\"trials\"].stop_time).sum()\n    in_trials.append(n_in / len(sp))\nprint(\"Fraction of spikes inside the 5 s trial windows, per file: median\", np.round(np.median(in_trials), 3),\n      \"range\", np.round(min(in_trials), 3), \"to\", np.round(max(in_trials), 3))\nprint(\"Spike times sorted within every unit:\", all(np.all(np.diff(sp) >= 0) for s in sessions for sp in s[\"spikes\"]))\n\n# %% [markdown]\n# The trial times are not relative to the trial start: pole in follows `start_time` by 0.57 s in\n# every trial, and all the times run over the session (up to thousands of seconds), on the clock of\n# the spike times. The descriptions are wrong; the analyses use the times as session times. The\n# sample and delay epochs are 1.3 s in every trial, as the Methods state. Each trial row covers a\n# fixed 5 s window from 0.57 s before pole in, so `stop_time` is a window end, not the end of the\n# trial. Spike times are sorted.\n\n# %% tags=[\"sanity\"]\n# Supplemental Table 1 lists the mice and hemispheres of each experiment. Its ALM recording rows,\n# set against the files (ML coordinates are negative on the left; the 2015 mice have numeric ids,\n# and only anm00314757, the one with a left fastigial site and right ALM, can be matched to the\n# table's AN107, and anm00314756, the one dentate mouse with a numeric id, to AN106).\ntable = pd.DataFrame([\n    (\"BAYLORCD8\", \"left\", \"right\"), (\"BAYLORCD12\", \"left\", \"right\"), (\"BAYLORCD13\", \"left\", \"right\"),\n    (\"BAYLORCD14\", \"right\", \"left\"), (\"BAYLORCD6\", \"left\", \"right\"), (\"BAYLORNL15\", \"left\", \"right\"),\n    (\"anm00314757\", \"right\", \"left\"), (\"BAYLORNL12\", \"left\", \"right\"), (\"BAYLORNL14\", \"left\", \"right\"),\n    (\"anm00314756\", \"left\", \"right\")], columns=[\"subject\", \"table_ALM\", \"table_CN\"])\nfiles = inv.drop_duplicates(\"subject\").set_index(\"subject\")\ntable[\"file_ALM\"] = table.subject.map(lambda m: \"left\" if files.loc[m, \"rec_ml\"] < 0 else \"right\")\ntable[\"file_CN\"] = table.subject.map(lambda m: files.loc[m, \"site\"].split()[1])\ntable[\"agrees\"] = (table.table_ALM == table.file_ALM) & (table.table_CN == table.file_CN)\nprint(table.to_string(index=False))\nprint(\"\\nThe Methods: 'ALM recordings were always contralateral to the side of CN manipulations'.\")\nprint(\"Files with ALM and CN site on the same side:\",\n      [m for m, r in files.iterrows() if (r.rec_ml < 0) == (r.site.split()[1] == \"left\")])\npi = files[files.group == \"PI\"]\nprint(\"\\nPI mice, stimulation site coordinates as given in the files:\")\nfor s in sessions:\n    if s[\"group\"] == \"PI\" and s[\"session\"] == min(x[\"session\"] for x in sessions if x[\"subject\"] == s[\"subject\"]):\n        print(\" \", s[\"subject\"], s[\"opto\"])\n\n# %% [markdown]\n# For the ALM recordings during CN photo-inhibition the files disagree with Supplemental Table 1 in\n# three of four mice: BAYLORCD12 and BAYLORCD13 are given a left fastigial site where the table\n# has the right CN, and BAYLORCD14 is given left ALM where the table has right ALM. In those three\n# files ALM and the stimulation site are on the same side, against the Methods' statement that ALM\n# recordings were always contralateral to the CN manipulation. The PI files also describe the\n# photostimulation site as the fastigial nucleus at 2.4 mm depth, while the Methods photostimulate\n# the cerebellar cortex through a cranial window at the brain surface. For the FN and DN mice the\n# files agree with the table where the mice can be matched. No analysis below uses the side of\n# photo-inhibition; fig1h-fn-delay-bias-either-direction uses the FN side, which agrees.\n\n# %% tags=[\"sanity\"]\n# Recordings deposited twice: identical or near-identical spike trains across all units, and\n# repeated trial tables.\nimport hashlib\nfrom collections import defaultdict\ndigests = defaultdict(list)\nfor s in sessions:\n    for i, sp in enumerate(s[\"spikes\"]):\n        digests[hashlib.md5(np.round(sp, 5).tobytes()).hexdigest()].append((s[\"subject\"], s[\"session\"], i))\nprint(\"Groups of identical spike trains:\", [v for v in digests.values() if len(v) > 1])\ntables = defaultdict(list)\nfor s in sessions:\n    tables[hashlib.md5(np.round(s[\"trials\"][[\"pole_in_time\", \"cue_time\"]].values, 3).tobytes()).hexdigest()].append(s[\"session\"])\nprint(\"Repeated trial tables:\", [v for v in tables.values() if len(v) > 1])\nnear = []\nfor s in sessions:\n    sp = s[\"spikes\"]\n    for i in range(len(sp)):\n        for j in range(i + 1, len(sp)):\n            a, b = (sp[i], sp[j]) if len(sp[i]) <= len(sp[j]) else (sp[j], sp[i])\n            if len(a) < 100:\n                continue\n            k = np.clip(np.searchsorted(b, a), 1, len(b) - 1)\n            frac = (np.minimum(np.abs(b[k] - a), np.abs(b[k - 1] - a)) < 0.0005).mean()\n            if frac > 0.5:\n                near.append((s[\"subject\"], s[\"session\"], i, j, len(sp[i]), len(sp[j]), round(frac, 2)))\nprint(\"Unit pairs in one session sharing more than half of the smaller unit's spikes within 0.5 ms:\")\nprint(pd.DataFrame(near, columns=[\"subject\", \"session\", \"unit_a\", \"unit_b\", \"spikes_a\", \"spikes_b\", \"shared\"]).to_string(index=False))\n\n# %% [markdown]\n# No recording is deposited twice: no two files share a trial table and no two units share a spike\n# train. Within two sessions a pair of units shares most spikes (83% and 96% of the smaller unit's\n# spikes within 0.5 ms), so each pair is likely one neuron sorted twice or a unit and part of it.\n# These four units are kept, as the paper's counts give no way to tell which were used; they are 4\n# of 1923 units. Units are not matched across sessions; each session's units are treated as\n# distinct neurons, as the paper's counts do.\n\n# %% tags=[\"sanity\"]\n# Clock check 1: the trial table and the spikes share a clock. Decoding the instructed trial type\n# from population spike counts (200 ms windows) in each session, with 5-fold cross-validated\n# logistic regression on control trials, should be at chance before pole in and rise after it.\ncentres = np.arange(-0.4, 3.5, 0.2)\nrng_clock = np.random.default_rng(1)\nacc = []\nfor s in sessions:\n    tr = s[\"trials\"]\n    ok = (tr.stim == 0) & (tr.lick_early == 0) & tr.outcome.isin([\"hit\", \"error\"])\n    t0, y = tr.pole_in_time.values[ok], (tr.trial_type.values[ok] == \"R\").astype(int)\n    if min(y.sum(), (1 - y).sum()) < 10:\n        continue\n    X = np.stack([gao2018.binned_counts(sp, t0, centres + 0.1, 0.2) for sp in s[\"spikes\"]], axis=2)\n    cv = StratifiedKFold(5, shuffle=True, random_state=0)\n    row = {\"session\": f'{s[\"subject\"]} {s[\"session\"]}', \"group\": s[\"group\"]}\n    for k, c in enumerate(centres):\n        row[round(c, 1)] = cross_val_score(LogisticRegression(C=0.1, max_iter=2000), X[:, k, :], y, cv=cv,\n                                           scoring=\"balanced_accuracy\").mean()\n    acc.append(row)\nacc = pd.DataFrame(acc)\ncols = [c for c in acc.columns if isinstance(c, float)]\nprint(\"Balanced accuracy, median over sessions, by window start relative to pole in (s):\")\nprint(acc[cols].median().round(2).to_string())\npre = acc[[c for c in cols if c < 0]].mean(axis=1)\nlate_delay = acc[[c for c in cols if 2.0 <= c < 2.6]].mean(axis=1)\nprint(f\"\\nSessions decoded: {len(acc)} of {len(sessions)}\")\nprint(\"Mean accuracy before pole in: median\", pre.median().round(3), \"; in the last 600 ms of the delay: median\",\n      late_delay.median().round(3))\nprint(\"Sessions whose late-delay accuracy exceeds the pre-trial accuracy by 0.1 or more:\",\n      int((late_delay - pre >= 0.1).sum()), \"of\", len(acc))\nprint(\"Sessions where it does not:\", acc.session[(late_delay - pre < 0.1)].tolist())\n\n# %% [markdown]\n# Before pole in the trial type cannot be decoded (median balanced accuracy near 0.5), and it rises\n# during the sample and delay epochs, so the trial table and the spikes share a clock at the scale\n# of the epochs. The sessions listed above, where the delay is not decoded better than the\n# pre-trial period, have few units or trials; for them the shared clock is not shown by this\n# check. The photostimulation responses below (stim-code-link) start within milliseconds of the\n# stimulus onset taken from the trial table, which shows the alignment at a finer scale for every\n# group of mice.\n\n# %% tags=[\"sanity\"]\n# The R and L of `response`. In the paper's scripts \"yes\" trials are HitR or ErrR, so R is the\n# instructed side. NoLickR and NoLickL also carry a side, which can only be the instructed one. A\n# check from the data: ALM late-delay activity follows the upcoming lick on error trials (Extended\n# Data Fig. 4e, and earlier work of the lab), so if R is the instructed side, ErrR trials (licked\n# left) should resemble HitL trials.\nrows = []\nfor s in sessions:\n    tr = s[\"trials\"]\n    ok = (tr.stim == 0) & (tr.lick_early == 0)\n    a, b = tr.cue_time.values - 0.6, tr.cue_time.values\n    X = np.stack([gao2018.counts(sp, a, b) / 0.6 for sp in s[\"spikes\"]], axis=1)\n    hr, hl = ok & (tr.response == \"HitR\"), ok & (tr.response == \"HitL\")\n    er, el = ok & (tr.response == \"ErrR\"), ok & (tr.response == \"ErrL\")\n    if min(er.sum(), el.sum()) < 3:\n        continue\n    w = X[hr].mean(0) - X[hl].mean(0)\n    mid = (X[hr].mean(0) + X[hl].mean(0)) @ w / 2\n    rows.append({\"session\": s[\"session\"], \"ErrR_like_HitR\": float(((X[er] @ w) > mid).mean()),\n                 \"ErrL_like_HitR\": float(((X[el] @ w) > mid).mean()), \"n_ErrR\": int(er.sum()), \"n_ErrL\": int(el.sum())})\nerr = pd.DataFrame(rows)\nprint(\"Fraction of error trials whose last-600-ms delay activity falls on the HitR side of the HitR/HitL midpoint, per session:\")\nprint(err[[\"ErrR_like_HitR\", \"ErrL_like_HitR\"]].describe().round(3).to_string())\nprint(\"Sessions where ErrR trials fall on the HitR side less often than ErrL trials:\",\n      int((err.ErrR_like_HitR < err.ErrL_like_HitR).sum()), \"of\", len(err))\n"
}
```

```
File created successfully at: /tmp/claude-1001/dev/nb_main.py (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd entries/000007-gao-2018; . $TMPDIR/explore/bin/activate; uv pip install -q scikit-learn matplotlib statsmodels 2>&1 | tail -1; python $TMPDIR/dev/build.py $TMPDIR/dev/nb_main.py $TMPDIR/dev/run.py && time PYTHONPATH=. python $TMPDIR/dev/run.py 2>&1 | grep -v Warn
```

```
Traceback (most recent call last):
  File "/tmp/claude-1001/dev/build.py", line 2, in <module>
    import sys, re, nbformat
ModuleNotFoundError: No module named 'nbformat'
```

**Agent calls Bash**

```bash
cd entries/000007-gao-2018; . $TMPDIR/explore/bin/activate; uv pip install -q nbformat; python $TMPDIR/dev/build.py $TMPDIR/dev/nb_main.py $TMPDIR/dev/run.py && time PYTHONPATH=. python $TMPDIR/dev/run.py 2>&1 | grep -v Warn
```

```
File "/tmp/claude-1001/dev/run.py", line 24
    print('\n######## CELL ['sanity']')
          ^^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: invalid syntax. Perhaps you forgot a comma?

real	0m0.025s
user	0m0.019s
sys	0m0.008s
```

**Agent calls Bash**

```bash
cd entries/000007-gao-2018; . $TMPDIR/explore/bin/activate; sed -i "s|print('\\\\n######## CELL {c.metadata.get('tags', \[\])}')|print(\"\\\\n######## CELL {c.metadata.get('tags', [])}\")|" $TMPDIR/dev/build.py; grep -n "CELL" $TMPDIR/dev/build.py; python $TMPDIR/dev/build.py $TMPDIR/dev/nb_main.py $TMPDIR/dev/run.py && time PYTHONPATH=. python $TMPDIR/dev/run.py 2>&1 | grep -v Warn
```

```
28:            code.append(f"print('\\n######## CELL {c.metadata.get('tags', [])}')\n" + s)
  File "/tmp/claude-1001/dev/run.py", line 24
    print('\n######## CELL ['sanity']')
          ^^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: invalid syntax. Perhaps you forgot a comma?

real	0m0.025s
user	0m0.018s
sys	0m0.008s
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "/tmp/claude-1001/dev/build.py",
 "old_string": "            code.append(f\"print('\\\\n######## CELL {c.metadata.get('tags', [])}')\\n\" + s)",
 "new_string": "            code.append(\"print(\" + repr(\"\\n######## CELL \" + str(c.metadata.get(\"tags\", []))) + \")\\n\" + s)"
}
```

```
<tool_use_error>File has not been read yet. Read it first before writing to it.</tool_use_error>
```

**Agent calls Bash**

```bash
cd entries/000007-gao-2018; . $TMPDIR/explore/bin/activate; python $TMPDIR/dev/build.py $TMPDIR/dev/nb_main.py $TMPDIR/dev/run.py && time PYTHONPATH=. python $TMPDIR/dev/run.py 2>&1 | grep -v Warn
```

```
File "/tmp/claude-1001/dev/run.py", line 24
    print('\n######## CELL ['sanity']')
          ^^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: invalid syntax. Perhaps you forgot a comma?

real	0m0.025s
user	0m0.017s
sys	0m0.010s
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/dev/build.py",
 "offset": 25,
 "limit": 5
}
```

```
25	    for c in cells:
26	        if c.cell_type == "code":
27	            s = c.source.replace("sessions = gao2018.load_all()", "import pickle; sessions = pickle.load(open('/tmp/claude-1001/S.pkl','rb'))")
28	            code.append(f"print('\\n######## CELL {c.metadata.get('tags', [])}')\n" + s)
29	    open(out, "w").write("\n\n".join(code))
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "/tmp/claude-1001/dev/build.py",
 "old_string": "            code.append(f\"print('\\\\n######## CELL {c.metadata.get('tags', [])}')\\n\" + s)",
 "new_string": "            code.append(\"print(\" + repr(\"\\n######## CELL \" + str(c.metadata.get(\"tags\", []))) + \")\\n\" + s)"
}
```

```
The file /tmp/claude-1001/dev/build.py has been updated successfully.
```

**Agent calls Bash**

```bash
cd entries/000007-gao-2018; . $TMPDIR/explore/bin/activate; python $TMPDIR/dev/build.py $TMPDIR/dev/nb_main.py $TMPDIR/dev/run.py && time PYTHONPATH=. python $TMPDIR/dev/run.py 2>&1 | grep -v Warn
```

```
######## CELL []
loaded 54 files from dandiset 000007 version 0.220126.1903 in 0 s

######## CELL ['sanity']
Groups: FN = ChR2 virus in the fastigial nucleus, DN = in the dentate nucleus, PI = L7-cre x Ai32 (CN photo-inhibition)
                   sessions  trials  units  pyramidal  FS  other
group subject                                                   
DN    BAYLORNL12          5    1910    244        231  13      0
      BAYLORNL14          6    2283    308        288  20      0
      anm00314756         2     457     26         26   0      0
FN    BAYLORCD6           4     941    196        187   8      1
      BAYLORNL15          5    1547    177        160  17      0
      anm00314746         3     780     63         60   3      0
      anm00314757         2     280     38         35   3      0
      anm00314758         4    1005     62         61   1      0
      anm00314760         3     745     72         64   8      0
PI    BAYLORCD12          5    1205    160        153   6      1
      BAYLORCD13          5     967    100         96   4      0
      BAYLORCD14          5    1719    195        185   9      1
      BAYLORCD8           5    1795    282        272  10      0
[... 168 more lines not kept]
```

**Agent**

Data check works. Some trials have sample or delay durations far from 1.3 s; I'll count them and exclude them as a stated choice. Next, the stim-code-link and count claims.

**Agent calls Bash**

```bash
cd entries/000007-gao-2018; . $TMPDIR/explore/bin/activate; python - <<'E'
import pickle,numpy as np,pandas as pd
S=pickle.load(open('/tmp/claude-1001/S.pkl','rb'))
a=pd.concat([s['trials'].assign(sess=s['session'],grp=s['group']) for s in S],ignore_index=True)
smp=a.pole_out_time-a.pole_in_time; dl=a.cue_time-a.pole_out_time; lag=a.pole_in_time-a.start_time
odd=(abs(smp-1.3)>0.05)|(abs(dl-1.3)>0.05)
print(odd.sum(), (abs(smp-1.3)>0.05).sum(), (abs(dl-1.3)>0.05).sum(), (abs(lag-0.57)>0.01).sum())
print(a[odd].groupby(['grp']).size(), a[odd].response.value_counts(), a[odd].stim.value_counts(), a[odd].lick_early.value_counts())
print(pd.DataFrame({'smp':smp[odd],'dl':dl[odd],'lag':lag[odd]}).describe())
print(a[odd].groupby('sess').size().sort_values().tail(10))
E
```

```
1244 700 605 12
grp
DN    156
FN    457
PI    631
dtype: int64 response
HitR       533
HitL       464
ErrL       131
ErrR       110
NoLickL      4
NoLickR      2
Name: count, dtype: int64 stim
0    899
5    127
2     73
1     61
6     51
3     17
4     16
[... 25 more lines not kept]
```

**Agent calls Bash**

```bash
cat >> $TMPDIR/dev/nb_main.py <<'E'

# %% [markdown]
# Of the trials, 1244 have a sample or delay epoch that differs from 1.3 s by more than 50 ms; all
# but one of them are early-lick trials, in which the task restarts the epoch, and they are left
# out with the early-lick trials. 

# %% tags=["sanity"]
smp = alltr.pole_out_time - alltr.pole_in_time
dly = alltr.cue_time - alltr.pole_out_time
odd = (abs(smp - 1.3) > 0.05) | (abs(dly - 1.3) > 0.05)
print("Trials with a sample or delay epoch more than 50 ms from 1.3 s:", int(odd.sum()),
      "; of them early-lick trials:", int(alltr.lick_early[odd].sum()))
print("Among trials without early licks, sample epoch", smp[alltr.lick_early == 0].round(3).agg(["min", "max"]).tolist(),
      "s, delay epoch", dly[alltr.lick_early == 0].round(3).agg(["min", "max"]).tolist(), "s")

# %% [markdown]
# ## stim-code-link
#
# > The dandiset's photostimulation codes 1 to 6 can be named from the paper's Zenodo data
# > description (1 and 2 fastigial photo-activation in the sample and delay epochs, 3 and 4 dentate
# > photo-activation in the sample and delay, 5 and 6 CN photo-inhibition in the delay for 0.5 and
# > 1.3 s), and the ALM responses agree with those names.
#
# The names are in `gao2018.STIM_CODES`, from the data description of the Zenodo records. The ALM
# response to each code is the mean over all units of the group of the absolute difference in
# firing rate between that code's trials and control trials (no early licks), in 10 ms bins
# aligned to pole in.

# %% tags=["claim:stim-code-link"]
BIN = 0.01
link_edges = np.arange(-0.5, 3.6 + BIN / 2, BIN)
link_t = link_edges[:-1] + BIN / 2
group_codes = {"FN": (1, 2), "DN": (3, 4), "PI": (5, 6)}
change = {}
for grp, codes in group_codes.items():
    per_unit = {c: [] for c in codes}
    for s in sessions:
        if s["group"] != grp:
            continue
        tr = s["trials"][s["trials"].lick_early == 0]
        for sp in s["spikes"]:
            rate = {}
            for c in (0,) + codes:
                t0 = tr.pole_in_time.values[tr.stim.values == c]
                rate[c] = np.mean([np.histogram(sp[(sp > t + link_edges[0]) & (sp < t + link_edges[-1])] - t, link_edges)[0]
                                   for t in t0], axis=0) / BIN
            for c in codes:
                per_unit[c].append(np.abs(rate[c] - rate[0]))
    for c in codes:
        change[c] = np.mean(per_unit[c], axis=0)
        change[(c, "n_units")] = len(per_unit[c])

onset_expected = {1: 0.0, 2: 1.3, 3: 0.0, 4: 1.3, 5: 1.3, 6: 1.3}
rows = []
for c, ref in onset_expected.items():
    x = change[c]
    base = x[link_t < 0]
    thr = base.mean() + 4 * base.std()
    above = link_t[(x > thr) & (link_t >= 0)]
    first = above[0] if len(above) else np.nan
    rows.append({"code": c, "name": " ".join(str(v) for v in gao2018.STIM_CODES[c][1:3]), "units": change[(c, "n_units")],
                 "stated_onset_s": ref, "first_bin_above_s": round(first, 3),
                 "first_minus_onset_ms": round((first - ref) * 1000, 1),
                 "bins_above_before_onset": int(((x > thr) & (link_t >= 0) & (link_t < ref)).sum()),
                 "change_0.7_1.2s_after_onset": round(x[(link_t >= ref + 0.7) & (link_t < ref + 1.2)].mean() - base.mean(), 3)})
link = pd.DataFrame(rows)
print("Time from pole in of the first 10 ms bin (centre) whose change exceeds the pre-trial mean by 4 SD:")
print(link.to_string(index=False))
codes_by_group = alltr.groupby("group").stim.unique().map(sorted)
print("\nCodes present in each group:", codes_by_group.to_dict())
c1 = all(set(codes_by_group[g]) == {0, *group_codes[g]} for g in group_codes)
c2 = bool(((link.first_minus_onset_ms >= 0) & (link.first_minus_onset_ms <= 50) & (link.bins_above_before_onset == 0)).all())
c3 = bool(link.set_index("code").loc[5, "change_0.7_1.2s_after_onset"] < link.set_index("code").loc[6, "change_0.7_1.2s_after_onset"])
print(f"\n(1) codes only in their groups: {c1}; (2) onsets within 50 ms after the stated onset and none before: {c2}; "
      f"(3) code 5 ends before code 6: {c3}")

fig, axes = plt.subplots(1, 3, figsize=(13, 3), sharey=True)
for ax, (grp, codes) in zip(axes, group_codes.items()):
    for c in codes:
        ax.plot(link_t, change[c], label=f"code {c}")
    for x in (0, 1.3, 2.6):
        ax.axvline(x, color="k", lw=0.5)
    ax.set_title(grp); ax.set_xlabel("time from pole in (s)"); ax.legend()
axes[0].set_ylabel("mean |rate change| (spikes/s)")
plt.tight_layout(); plt.show()
print("Plotted range:", round(min(change[c].min() for c in onset_expected), 2), "to",
      round(max(change[c].max() for c in onset_expected), 2), "spikes/s; all points inside the axes")

# %% [markdown]
# RESULT stim-code-link

# %% [markdown]
# ## methods-alm-unit-counts
#
# > The ALM recordings comprise 912 putative pyramidal neurons in the 9 mice tested with CN
# > photo-activation (446 with fastigial and 466 with dentate photo-activation), and 490 single
# > units (454 putative pyramidal) in 4 mice across 19 sessions during CN photo-inhibition.

# %% tags=["claim:methods-alm-unit-counts"]
units["subject"] = np.concatenate([[s["subject"]] * len(s["spikes"]) for s in sessions])
wide = units.width_ms > gao2018.WIDE_MS
counts_tbl = pd.DataFrame({
    "expected": [912, 446, 466, 490, 454, 19],
    "(a) labels": [int((units.label == "pyramidal")[units.group.isin(["FN", "DN"])].sum()),
                   int((units.label == "pyramidal")[units.group == "FN"].sum()),
                   int((units.label == "pyramidal")[units.group == "DN"].sum()),
                   int((units.group == "PI").sum()), int((units.label == "pyramidal")[units.group == "PI"].sum()),
                   int((inv.group == "PI").sum())],
    "(b) width rule": [int(wide[units.group.isin(["FN", "DN"])].sum()), int(wide[units.group == "FN"].sum()),
                       int(wide[units.group == "DN"].sum()), int((units.group == "PI").sum()),
                       int(wide[units.group == "PI"].sum()), int((inv.group == "PI").sum())]},
    index=["pyramidal, photo-activation mice", "pyramidal, fastigial mice", "pyramidal, dentate mice",
           "units, photo-inhibition mice", "pyramidal, photo-inhibition mice", "sessions, photo-inhibition mice"])
counts_tbl["tolerance"] = (counts_tbl.expected * 0.1).round(1)
for r in ("(a) labels", "(b) width rule"):
    counts_tbl[f"within {r[:3]}"] = (counts_tbl[r] - counts_tbl.expected).abs() <= counts_tbl.tolerance
print(counts_tbl.to_string())
print("\nPyramidal units (labels) per mouse:")
print(units[units.label == "pyramidal"].groupby(["group", "subject"]).size().to_string())
print("\nPaper: 1309 ALM units in 10 mice during behaviour (1194 pyramidal, 82 FS, 33 intermediate);"
      " dandiset, 9 photo-activation mice:", int(units.group.isin(["FN", "DN"]).sum()), "units,",
      int(((units.label == "FS") & units.group.isin(["FN", "DN"])).sum()), "FS")

# %% [markdown]
# RESULT methods-alm-unit-counts
E
cd entries/000007-gao-2018; . $TMPDIR/explore/bin/activate; python $TMPDIR/dev/build.py $TMPDIR/dev/nb_main.py $TMPDIR/dev/run.py && time PYTHONPATH=. MPLBACKEND=Agg python $TMPDIR/dev/run.py 2>&1 | grep -v Warn | sed -n '/sample or delay epoch more/,$p'
```

```
Trials with a sample or delay epoch more than 50 ms from 1.3 s: 1244 ; of them early-lick trials: 1243
Among trials without early licks, sample epoch [1.11, 1.3] s, delay epoch [1.3, 1.301] s

######## CELL ['claim:stim-code-link']
Time from pole in of the first 10 ms bin (centre) whose change exceeds the pre-trial mean by 4 SD:
 code             name  units  stated_onset_s  first_bin_above_s  first_minus_onset_ms  bins_above_before_onset  change_0.7_1.2s_after_onset
    1 fastigial sample    608             0.0              0.015                  15.0                        0                        1.349
    2  fastigial delay    608             1.3              1.315                  15.0                        0                        1.483
    3   dentate sample    578             0.0              0.005                   5.0                        0                        0.261
    4    dentate delay    578             1.3              1.305                   5.0                        0                        0.235
    5         CN delay    737             1.3              1.335                  35.0                        0                        0.950
    6         CN delay    737             1.3                NaN                   NaN                        0                          NaN

Codes present in each group: {'DN': [np.int64(0), np.int64(3), np.int64(4)], 'FN': [np.int64(0), np.int64(1), np.int64(2)], 'PI': [np.int64(0), np.int64(5), np.int64(6)]}

(1) codes only in their groups: True; (2) onsets within 50 ms after the stated onset and none before: False; (3) code 5 ends before code 6: False
Plotted range: 1.64 to 6.09 spikes/s; all points inside the axes

######## CELL ['claim:methods-alm-unit-counts']
                                  expected  (a) labels  (b) width rule  tolerance  within (a)  within (b)
[... 28 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/000007-gao-2018; . $TMPDIR/explore/bin/activate; cat > $TMPDIR/dev/dbg.py <<'E'
exec(open('/tmp/claude-1001/dev/run.py').read().split("print('\\n######## CELL [\\'claim:methods-alm-unit-counts\\']')")[0].split("fig, axes")[0])
for c in (5,6):
    x=change[c]; base=x[link_t<0]; print(c, base.mean(), base.std(), x[(link_t>1.3)&(link_t<1.5)].round(2))
E
PYTHONPATH=. MPLBACKEND=Agg python $TMPDIR/dev/dbg.py 2>&1 | tail -4
```

```
5 2.6210550102293304 0.12844332466329253 [2.82 2.68 2.87 3.35 4.02 4.34 4.19 4.4  4.27 3.91 4.66 4.28 4.45 4.69
 4.35 4.5  4.45 4.37 4.36 4.32]
6 nan nan [nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan
 nan nan]
```

**Agent calls Bash**

```bash
cd $TMPDIR/dev; python3 - <<'E'
p='/tmp/claude-1001/dev/nb_main.py'; s=open(p).read()
old="""            for c in codes:
                per_unit[c].append(np.abs(rate[c] - rate[0]))"""
new="""            for c in codes:
                if (tr.stim.values == c).sum() > 0:
                    per_unit[c].append(np.abs(rate[c] - rate[0]))"""
assert old in s; s=s.replace(old,new)
old2="""            for c in (0,) + codes:
                t0 = tr.pole_in_time.values[tr.stim.values == c]
                rate[c] = np.mean("""
new2="""            for c in (0,) + codes:
                t0 = tr.pole_in_time.values[tr.stim.values == c]
                if len(t0) == 0:
                    continue
                rate[c] = np.mean("""
assert old2 in s; s=s.replace(old2,new2); open(p,'w').write(s)
E
cd entries/000007-gao-2018; . $TMPDIR/explore/bin/activate; python $TMPDIR/dev/build.py $TMPDIR/dev/nb_main.py $TMPDIR/dev/run.py && PYTHONPATH=. MPLBACKEND=Agg python $TMPDIR/dev/run.py 2>&1 | grep -v Warn | sed -n '/claim:stim-code-link/,/Plotted/p'
```

```
######## CELL ['claim:stim-code-link']
Time from pole in of the first 10 ms bin (centre) whose change exceeds the pre-trial mean by 4 SD:
 code             name  units  stated_onset_s  first_bin_above_s  first_minus_onset_ms  bins_above_before_onset  change_0.7_1.2s_after_onset
    1 fastigial sample    608             0.0              0.015                  15.0                        0                        1.349
    2  fastigial delay    608             1.3              1.315                  15.0                        0                        1.483
    3   dentate sample    578             0.0              0.005                   5.0                        0                        0.261
    4    dentate delay    578             1.3              1.305                   5.0                        0                        0.235
    5         CN delay    737             1.3              1.335                  35.0                        0                        0.950
    6         CN delay    700             1.3              1.335                  35.0                        0                        1.639

Codes present in each group: {'DN': [np.int64(0), np.int64(3), np.int64(4)], 'FN': [np.int64(0), np.int64(1), np.int64(2)], 'PI': [np.int64(0), np.int64(5), np.int64(6)]}

(1) codes only in their groups: True; (2) onsets within 50 ms after the stated onset and none before: True; (3) code 5 ends before code 6: True
Plotted range: 1.64 to 6.09 spikes/s; all points inside the axes
```

**Agent**

stim-code-link holds on all three parts. Now the behaviour claims; I'm replacing the pandas bootstrap with a faster array version.

**Agent calls Bash**

```bash
cd entries/000007-gao-2018; python3 - <<'E'
p='gao2018.py'; s=open(p).read()
start=s.index("def hierarchical_bootstrap"); end=s.index("def onset_latency")
new='''def hierarchical_bootstrap(data: dict, n_conditions: int, n: int, rng: np.random.Generator) -> np.ndarray:
    """Resample mice, then sessions within mouse, then trials within session (Methods).

    `data` maps each mouse to a list of sessions, each a pair of arrays (y, k): a 0/1 outcome per
    trial and its condition (0 to n_conditions - 1). Returns, for each of the `n` resamples, the
    sum of y and the number of trials in each condition, shape (n, n_conditions, 2).
    """
    mice = list(data)
    out = np.zeros((n, n_conditions, 2))
    for b in range(n):
        for m in rng.choice(len(mice), len(mice)):
            sess = data[mice[m]]
            for j in rng.choice(len(sess), len(sess)):
                y, k = sess[j]
                pick = rng.integers(0, len(y), len(y))
                out[b, :, 0] += np.bincount(k[pick], weights=y[pick], minlength=n_conditions)
                out[b, :, 1] += np.bincount(k[pick], minlength=n_conditions)
    return out


def one_tailed_p(observed: float, resampled: np.ndarray) -> float:
    """Fraction of resamples whose change has the opposite sign to the observed one (Methods)."""
    resampled = resampled[np.isfinite(resampled)]
    return float((resampled >= 0).mean() if observed < 0 else (resampled <= 0).mean())


'''
s=s[:start]+new+s[end:]; open(p,'w').write(s)
E
grep -n "def " gao2018.py
```

```
80:def _text(x):
87:def asset_urls() -> dict[str, str]:
93:def load_session(path: str, url: str) -> dict:
133:def load_all(workers: int = 8) -> list[dict]:
140:def spike_width_ms(waveform: np.ndarray, rate_hz: float) -> float:
147:def counts(spikes: np.ndarray, starts, stops) -> np.ndarray:
153:def stable_trials(spikes: np.ndarray, trials: pd.DataFrame) -> np.ndarray:
163:def epoch_bounds(trials: pd.DataFrame) -> dict[str, tuple[np.ndarray, np.ndarray]]:
169:def epoch_rates(spikes, trials) -> pd.DataFrame:
176:def selectivity_tests(s: dict, unit_mask=None) -> pd.DataFrame:
197:def psth(spikes, align, t_from, t_to, step=0.001, smooth=0.2):
212:def binned_counts(spikes, align, centres, width):
219:def performance(trials: pd.DataFrame) -> pd.DataFrame:
225:def hierarchical_bootstrap(data: dict, n_conditions: int, n: int, rng: np.random.Generator) -> np.ndarray:
245:def one_tailed_p(observed: float, resampled: np.ndarray) -> float:
251:def onset_latency(change: np.ndarray, centres: np.ndarray, rng: np.random.Generator, n_boot: int = 10000,
259:    def first(x):
```

**Agent calls Bash**

```bash
cat >> $TMPDIR/dev/nb_main.py <<'E'

# %% [markdown]
# ## Behaviour during the recordings
#
# The behavioural claims are tested on the trials of the recording sessions, the only behaviour in
# the dandiset. Performance is the fraction correct without early-lick and no-lick trials. A
# contralateral trial is one whose instructed lick is toward the side opposite the stimulated
# nucleus. `perf_data` gathers, per mouse and session, each trial's outcome and condition for the
# hierarchical bootstrap of the Methods.

# %% 
def perf_table(group):
    rows = []
    for s in sessions:
        if s["group"] != group:
            continue
        t = gao2018.performance(s["trials"])
        contra_side = "L" if s["site_hemisphere"] == "right" else "R"
        rows.append(t.assign(subject=s["subject"], session=s["session"],
                             side=np.where(t.trial_type == contra_side, "contra", "ipsi")))
    return pd.concat(rows, ignore_index=True)


def perf_data(tbl, condition):
    """{mouse: [(correct, condition index), ...]} for trials whose condition is not None."""
    data = {}
    for (m, sess), g in tbl.groupby(["subject", "session"]):
        k = condition(g)
        ok = k >= 0
        if ok.sum():
            data.setdefault(m, []).append((g.correct.values[ok], k[ok].astype(int)))
    return data


def perf_change(boot, stim=1, ctrl=0):
    return boot[:, stim, 0] / boot[:, stim, 1] - boot[:, ctrl, 0] / boot[:, ctrl, 1]


perf_fn, perf_dn, perf_pi = perf_table("FN"), perf_table("DN"), perf_table("PI")
for name, t in (("FN", perf_fn), ("DN", perf_dn), ("PI", perf_pi)):
    print(name, "performance by mouse and code (fraction correct, trials):")
    print(t.groupby(["subject", "stim"]).correct.agg(["mean", "size"]).unstack("stim").round(3).to_string(), "\n")

# %% [markdown]
# ## fig1g-fn-delay-performance
#
# > Fastigial photo-activation during the early delay epoch reduced behavioural performance
# > (incorrect choices).

# %% tags=["claim:fig1g-fn-delay-performance"]
rng = np.random.default_rng(101)
obs = perf_fn[perf_fn.stim == 2].correct.mean() - perf_fn[perf_fn.stim == 0].correct.mean()
boot = gao2018.hierarchical_bootstrap(perf_data(perf_fn, lambda g: np.select([g.stim == 0, g.stim == 2], [0, 1], -1)),
                                      2, 10000, rng)
d = perf_change(boot)
print(f"FN mice ({perf_fn.subject.nunique()}), code 2 against control: control {perf_fn[perf_fn.stim == 0].correct.mean():.3f}"
      f" ({(perf_fn.stim == 0).sum()} trials), photostim {perf_fn[perf_fn.stim == 2].correct.mean():.3f} ({(perf_fn.stim == 2).sum()} trials)")
print(f"change {obs:+.3f}; bootstrap 95% interval {np.percentile(d, 2.5):+.3f} to {np.percentile(d, 97.5):+.3f}; "
      f"one-tailed p = {gao2018.one_tailed_p(obs, d):.4f}")
per_mouse = perf_fn[perf_fn.stim.isin([0, 2])].groupby(["subject", "stim"]).correct.mean().unstack()
per_mouse["change"] = per_mouse[2] - per_mouse[0]
print("\nPer mouse:"); print(per_mouse.round(3).to_string())
print("Mice with lower performance on code 2 trials:", int((per_mouse.change < 0).sum()), "of", len(per_mouse))

# %% [markdown]
# RESULT fig1g-fn-delay-performance

# %% [markdown]
# ## fig1-fn-sample-no-effect
#
# > Fastigial photo-activation during the early sample epoch had no effect on behavioural choice
# > (p > 0.05 for either trial type, bootstrap).

# %% tags=["claim:fig1-fn-sample-no-effect"]
rng = np.random.default_rng(102)
rows = []
for side in ("contra", "ipsi"):
    sub = perf_fn[perf_fn.side == side]
    obs = sub[sub.stim == 1].correct.mean() - sub[sub.stim == 0].correct.mean()
    boot = gao2018.hierarchical_bootstrap(perf_data(sub, lambda g: np.select([g.stim == 0, g.stim == 1], [0, 1], -1)),
                                          2, 10000, rng)
    d = perf_change(boot)
    rows.append({"trial type": side, "control": sub[sub.stim == 0].correct.mean(), "code 1": sub[sub.stim == 1].correct.mean(),
                 "change": obs, "ci_low": np.percentile(d, 2.5), "ci_high": np.percentile(d, 97.5),
                 "one_tailed_p": gao2018.one_tailed_p(obs, d), "n_code1": int((sub.stim == 1).sum())})
print(pd.DataFrame(rows).round(4).to_string(index=False))
print("By lick direction, the same test:")
for side in ("R", "L"):
    sub = perf_fn[perf_fn.trial_type == side]
    print(f"  lick {side}: control {sub[sub.stim == 0].correct.mean():.3f}, code 1 {sub[sub.stim == 1].correct.mean():.3f}")

# %% [markdown]
# RESULT fig1-fn-sample-no-effect

# %% [markdown]
# ## fig1g-dn-little-effect
#
# > Dentate photo-activation produced little effect on behavioural choice (p = 0.06, bootstrap).

# %% tags=["claim:fig1g-dn-little-effect"]
rng = np.random.default_rng(103)
for code in (4, 3):
    obs = perf_dn[perf_dn.stim == code].correct.mean() - perf_dn[perf_dn.stim == 0].correct.mean()
    boot = gao2018.hierarchical_bootstrap(perf_data(perf_dn, lambda g: np.select([g.stim == 0, g.stim == code], [0, 1], -1)),
                                          2, 10000, rng)
    d = perf_change(boot)
    print(f"DN mice ({perf_dn.subject.nunique()}), code {code}: control {perf_dn[perf_dn.stim == 0].correct.mean():.3f}, "
          f"photostim {perf_dn[perf_dn.stim == code].correct.mean():.3f}; change {obs:+.3f}; 95% interval "
          f"{np.percentile(d, 2.5):+.3f} to {np.percentile(d, 97.5):+.3f}; one-tailed p = {gao2018.one_tailed_p(obs, d):.4f}")
print("(code 4 is the test; code 3, sample-epoch dentate photo-activation, is shown for reference)")
pm = perf_dn[perf_dn.stim.isin([0, 4])].groupby(["subject", "stim"]).correct.mean().unstack()
print("Per mouse:"); print((pm[4] - pm[0]).round(3).to_string())

# %% [markdown]
# RESULT fig1g-dn-little-effect

# %% [markdown]
# ## fig1h-fn-delay-bias-either-direction
#
# > Fastigial photo-activation during the delay epoch biased future movements to either the
# > contralateral or the ipsilateral direction in individual mice.

# %% tags=["claim:fig1h-fn-delay-bias-either-direction"]
rng = np.random.default_rng(104)
rows = []
for m, sub in perf_fn.groupby("subject"):
    cond = lambda g: np.select([(g.stim == 0) & (g.side == "contra"), (g.stim == 0) & (g.side == "ipsi"),
                                (g.stim == 2) & (g.side == "contra"), (g.stim == 2) & (g.side == "ipsi")], [0, 1, 2, 3], -1)
    boot = gao2018.hierarchical_bootstrap({m: perf_data(sub, cond)[m]}, 4, 10000, rng)
    bias = (boot[:, 3, 0] / boot[:, 3, 1] - boot[:, 1, 0] / boot[:, 1, 1]) - (boot[:, 2, 0] / boot[:, 2, 1] - boot[:, 0, 0] / boot[:, 0, 1])
    pc = sub[(sub.stim == 0)].groupby("side").correct.mean()
    ps = sub[(sub.stim == 2)].groupby("side").correct.mean()
    b = (ps["ipsi"] - pc["ipsi"]) - (ps["contra"] - pc["contra"])
    p2 = 2 * gao2018.one_tailed_p(b, bias)
    rows.append({"mouse": m, "site": sub_site if (sub_site := None) else
                 next(s["site_hemisphere"] for s in sessions if s["subject"] == m),
                 "sessions": sub.session.nunique(), "contra change": ps["contra"] - pc["contra"],
                 "ipsi change": ps["ipsi"] - pc["ipsi"], "bias (ipsi - contra)": b, "two_tailed_p": min(p2, 1.0),
                 "n_code2": int((sub.stim == 2).sum())})
bias_tbl = pd.DataFrame(rows)
bias_tbl["direction"] = np.where(bias_tbl.two_tailed_p >= 0.05, "none",
                                 np.where(bias_tbl["bias (ipsi - contra)"] > 0, "contralateral", "ipsilateral"))
print("A positive bias means contralateral trials lost more than ipsilateral ones, a bias toward ipsilateral licking...")
print(bias_tbl.round(4).to_string(index=False))

# %% [markdown]
# The bias is signed so that a positive value is a larger drop on contralateral trials, that is,
# mice licking ipsilaterally more; the direction column names the direction of licking the
# photostimulation favours.

# %% [markdown]
# RESULT fig1h-fn-delay-bias-either-direction

# %% [markdown]
# ## ed1f-fn-no-early-licks
#
# > Fastigial photo-activation during the delay epoch did not evoke early licks.

# %% tags=["claim:ed1f-fn-no-early-licks"]
rng = np.random.default_rng(105)
early = pd.concat([s["trials"].assign(subject=s["subject"], session=s["session"]) for s in sessions if s["group"] == "FN"],
                  ignore_index=True)
early = early[early.stim.isin([0, 2])].assign(correct=lambda t: t.lick_early.astype(float))
obs = early[early.stim == 2].correct.mean() - early[early.stim == 0].correct.mean()
boot = gao2018.hierarchical_bootstrap(perf_data(early, lambda g: np.where(g.stim == 2, 1, 0)), 2, 10000, rng)
d = perf_change(boot)
print(f"Early-lick rate, FN mice: control {early[early.stim == 0].correct.mean():.3f} ({(early.stim == 0).sum()} trials), "
      f"code 2 {early[early.stim == 2].correct.mean():.3f} ({(early.stim == 2).sum()} trials)")
print(f"increase {obs:+.3f}; 95% interval {np.percentile(d, 2.5):+.3f} to {np.percentile(d, 97.5):+.3f}; "
      f"one-tailed p for an increase = {float((d <= 0).mean()):.4f}")
pm = early.groupby(["subject", "stim"]).correct.mean().unstack()
print("Per mouse:"); print(pm.round(3).to_string())
print("Variant, no-lick rate (trials without early licks): control",
      round(float((early[(early.stim == 0) & (early.lick_early == 0)].outcome == "nolick").mean()), 3), "code 2",
      round(float((early[(early.stim == 2) & (early.lick_early == 0)].outcome == "nolick").mean()), 3))

# %% [markdown]
# RESULT ed1f-fn-no-early-licks

# %% [markdown]
# ## fig1k-pi-delay-performance
#
# > CN photo-inhibition during the delay epoch resulted in incorrect behavioural choices.

# %% tags=["claim:fig1k-pi-delay-performance"]
rng = np.random.default_rng(106)
for label, codes in (("codes 5 and 6", (5, 6)), ("code 5 (0.5 s)", (5,)), ("code 6 (1.3 s)", (6,))):
    sub = perf_pi[perf_pi.stim.isin((0,) + codes)]
    obs = sub[sub.stim != 0].correct.mean() - sub[sub.stim == 0].correct.mean()
    boot = gao2018.hierarchical_bootstrap(perf_data(sub, lambda g: np.where(g.stim == 0, 0, 1)), 2, 10000, rng)
    d = perf_change(boot)
    print(f"PI mice, {label}: control {sub[sub.stim == 0].correct.mean():.3f}, photo-inhibition {sub[sub.stim != 0].correct.mean():.3f} "
          f"({(sub.stim != 0).sum()} trials); change {obs:+.3f}; 95% interval {np.percentile(d, 2.5):+.3f} to "
          f"{np.percentile(d, 97.5):+.3f}; one-tailed p = {gao2018.one_tailed_p(obs, d):.4f}")
pm = perf_pi.groupby(["subject", "stim"]).correct.mean().unstack()
print("\nPer mouse:"); print(pm.round(3).to_string())

# %% [markdown]
# RESULT fig1k-pi-delay-performance
E
cd entries/000007-gao-2018; . $TMPDIR/explore/bin/activate; python $TMPDIR/dev/build.py $TMPDIR/dev/nb_main.py $TMPDIR/dev/run.py && time PYTHONPATH=. MPLBACKEND=Agg python $TMPDIR/dev/run.py 2>&1 | grep -v Warn | sed -n '/FN performance by mouse/,$p'
```

```
FN performance by mouse and code (fraction correct, trials):
              mean                size          
stim             0      1      2     0    1    2
subject                                         
BAYLORCD6    0.745  0.803  0.662   666   71   74
BAYLORNL15   0.896  0.795  0.447  1079  132  103
anm00314746  0.921  0.950  0.782   572   80   78
anm00314757  0.906  0.852  0.727   160   27   22
anm00314758  0.912  0.930  0.765   704  114   98
anm00314760  0.875  0.877  0.479   534   81   71 

DN performance by mouse and code (fraction correct, trials):
              mean                size          
stim             0      3      4     0    3    4
subject                                         
BAYLORNL12   0.862  0.823  0.832  1392  215  214
BAYLORNL14   0.885  0.920  0.832  1700  264  285
anm00314756  0.862  0.900  0.870   318   50   46 

PI performance by mouse and code (fraction correct, trials):
[... 82 more lines not kept]
```

**Agent calls Bash**

```bash
python3 - <<'E'
p='/tmp/claude-1001/dev/nb_main.py'; s=open(p).read()
old='''    rows.append({"mouse": m, "site": sub_site if (sub_site := None) else
                 next(s["site_hemisphere"] for s in sessions if s["subject"] == m),'''
new='''    rows.append({"mouse": m, "site": next(s["site_hemisphere"] for s in sessions if s["subject"] == m),'''
assert old in s; s=s.replace(old,new)
old='''                                 np.where(bias_tbl["bias (ipsi - contra)"] > 0, "contralateral", "ipsilateral"))
print("A positive bias means contralateral trials lost more than ipsilateral ones, a bias toward ipsilateral licking...")'''
new='''                                 np.where(bias_tbl["bias (ipsi - contra)"] > 0, "ipsilateral", "contralateral"))
print("Bias = change on ipsilateral trials minus change on contralateral trials; positive when contralateral trials lose")
print("more, that is, when photostimulation pushes licking to the ipsilateral side.")'''
assert old in s; s=s.replace(old,new)
old='''# The bias is signed so that a positive value is a larger drop on contralateral trials, that is,
# mice licking ipsilaterally more; the direction column names the direction of licking the
# photostimulation favours.'''
new='''# The direction column names the side toward which photostimulation pushes licking (relative to
# the stimulated nucleus), for mice with a two-tailed p below 0.05.'''
assert old in s; s=s.replace(old,new); open(p,'w').write(s)
E
echo done
```

```
done
```

**Agent calls Bash**

```bash
cat >> $TMPDIR/dev/nb_main.py <<'E'

# %% [markdown]
# ## ALM selectivity (Figure 2)
#
# Every pyramidal neuron is tested for selectivity in the sample, delay and response epochs
# (two-tailed t-test on spike rates of correct control trials without early licks, in the unit's
# stable trials, lick right against lick left).

# %%
sel = []
for s in sessions:
    t = gao2018.selectivity_tests(s, unit_mask=s["cell_type"] == "pyramidal")
    sel.append(t.assign(group=s["group"], subject=s["subject"], session=s["session"]))
sel = pd.concat(sel, ignore_index=True)
for e in ("sample", "delay", "response"):
    sel[f"sig_{e}"] = sel[f"p_{e}"] < gao2018.SELECTIVE_P
sel["selective"] = sel[["sig_sample", "sig_delay", "sig_response"]].any(axis=1)
sel["preparatory"] = sel[["sig_sample", "sig_delay"]].any(axis=1)
untested = sel[["p_sample", "p_delay", "p_response"]].isna().any(axis=1)
print("Pyramidal neurons tested:", len(sel), "; without a test in some epoch (fewer than 2 trials of a type):", int(untested.sum()))
print("Correct control trials per neuron, median (lick right, lick left):", int(sel.n_right.median()), int(sel.n_left.median()))
readings = {"(a) photo-activation mice": sel.group.isin(["FN", "DN"]), "(b) all 13 mice": sel.group.notna()}
frac_rows = []
for r, m in readings.items():
    frac_rows.append({"reading": r, "neurons": int(m.sum()), "selective": sel.selective[m].mean(),
                      "preparatory": sel.preparatory[m].mean(), "peri-movement": sel.sig_response[m].mean()})
fractions = pd.DataFrame(frac_rows).set_index("reading")
print(fractions.round(3).to_string())
print("\nBy mouse (fractions):")
print(sel.groupby(["group", "subject"])[["selective", "preparatory", "sig_response"]].mean().round(3)
      .assign(neurons=sel.groupby(["group", "subject"]).size()).to_string())

# %% [markdown]
# ## fig2-alm-selective-fraction
#
# > Most ALM pyramidal neurons distinguished lick left and lick right trials (980/1194, p < 0.05,
# > two-tailed t-test).

# %% tags=["claim:fig2-alm-selective-fraction"]
print("Expected 0.821 +/- 0.082")
for r in readings:
    v = fractions.loc[r, "selective"]
    print(f"{r}: {v:.3f} ({int(round(v * fractions.loc[r, 'neurons']))}/{fractions.loc[r, 'neurons']}); within tolerance: {abs(v - 0.821) <= 0.082}")
# The test at p < 0.05 in three epochs gives a false-positive rate per neuron of up to about 14%;
# with trial labels shuffled within each session the fraction is:
rng = np.random.default_rng(201)
null = []
for s in sessions:
    if s["group"] not in ("FN", "DN"):
        continue
    sh = dict(s, trials=s["trials"].assign(trial_type=rng.permutation(s["trials"].trial_type.values)))
    t = gao2018.selectivity_tests(sh, unit_mask=s["cell_type"] == "pyramidal")
    null.append((t[["p_sample", "p_delay", "p_response"]] < 0.05).any(axis=1))
print(f"Shuffled labels, reading (a): {pd.concat(null).mean():.3f} selective")
print("Threshold variants, reading (a):", {p: round(float((sel[readings['(a) photo-activation mice']][['p_sample', 'p_delay', 'p_response']] < p).any(axis=1).mean()), 3)
                                           for p in (0.01, 0.05)})

# %% [markdown]
# RESULT fig2-alm-selective-fraction

# %% [markdown]
# ## fig2-alm-preparatory-fraction
#
# > Preparatory activity (selectivity before the response epoch) was present in 59% of ALM
# > neurons.

# %% tags=["claim:fig2-alm-preparatory-fraction"]
print("Expected 0.59 +/- 0.059")
for r in readings:
    v = fractions.loc[r, "preparatory"]
    print(f"{r}: {v:.3f} ({int(round(v * fractions.loc[r, 'neurons']))}/{fractions.loc[r, 'neurons']}); within tolerance: {abs(v - 0.59) <= 0.059}")
ma = readings["(a) photo-activation mice"]
print("Variant, as a fraction of selective neurons, reading (a):", round(sel.preparatory[ma].sum() / sel.selective[ma].sum(), 3))
print("Delay epoch alone, reading (a):", round(sel.sig_delay[ma].mean(), 3), "; sample alone:", round(sel.sig_sample[ma].mean(), 3))

# %% [markdown]
# RESULT fig2-alm-preparatory-fraction

# %% [markdown]
# ## fig2-alm-perimovement-fraction
#
# > Peri-movement activity (selectivity in the response epoch) was present in 67% of ALM neurons.

# %% tags=["claim:fig2-alm-perimovement-fraction"]
print("Expected 0.67 +/- 0.067")
for r in readings:
    v = fractions.loc[r, "peri-movement"]
    print(f"{r}: {v:.3f}; within tolerance: {abs(v - 0.67) <= 0.067}")

# %% [markdown]
# RESULT fig2-alm-perimovement-fraction

# %% [markdown]
# ## fig2c-alm-selectivity-time-course
#
# > Selectivity for lick left and lick right trials emerged gradually in the ALM population
# > average, starting during the sample epoch and reaching a maximum in the response epoch.

# %% tags=["claim:fig2c-alm-selectivity-time-course"]
rng = np.random.default_rng(202)
tc_centres = np.round(np.arange(-0.4, 3.9 + 1e-9, 0.01), 3)   # from pole in; cue at 2.6 s
curves, dropped = [], 0
for s in sessions:
    if s["group"] not in ("FN", "DN"):
        continue
    tr = s["trials"]
    tested = sel[(sel.session == s["session"]) & (sel.subject == s["subject"])].set_index("unit")
    for i, sp in enumerate(s["spikes"]):
        if i not in tested.index or not tested.loc[i, "selective"]:
            continue
        ok = gao2018.stable_trials(sp, tr) & (tr.lick_early == 0).values & (tr.stim == 0).values & (tr.outcome == "hit").values
        r_idx = np.flatnonzero(ok & (tr.trial_type == "R").values)
        l_idx = np.flatnonzero(ok & (tr.trial_type == "L").values)
        if min(len(r_idx), len(l_idx)) < 15:
            dropped += 1
            continue
        r_idx, l_idx = rng.permutation(r_idx), rng.permutation(l_idx)
        k = gao2018.ALM_SCREEN_TRIALS
        dr = gao2018.epoch_rates(sp, tr)["delay"].values
        pref_r = dr[r_idx[:k]].mean() >= dr[l_idx[:k]].mean()
        rate_r = gao2018.binned_counts(sp, tr.pole_in_time.values[r_idx[k:]], tc_centres, 0.2).mean(0) / 0.2
        rate_l = gao2018.binned_counts(sp, tr.pole_in_time.values[l_idx[k:]], tc_centres, 0.2).mean(0) / 0.2
        curves.append((rate_r - rate_l) if pref_r else (rate_l - rate_r))
curves = np.array(curves)
mean_sel = curves.mean(0)
print(f"Selective neurons used: {len(curves)}; dropped for fewer than 15 correct control trials of a type: {dropped}")
late_sample = (tc_centres >= 1.0) & (tc_centres < 1.3)
boot = np.array([curves[rng.integers(0, len(curves), len(curves))][:, late_sample].mean() for _ in range(2000)])
print(f"(1) mean selectivity, last 300 ms of the sample epoch: {curves[:, late_sample].mean():.2f} spikes/s, "
      f"bootstrap 95% interval {np.percentile(boot, 2.5):.2f} to {np.percentile(boot, 97.5):.2f}")
win = (tc_centres >= 0) & (tc_centres <= 3.9)
t_max = tc_centres[win][np.argmax(mean_sel[win])]
print(f"(2) maximum of the mean selectivity at {t_max:.2f} s from pole in ({mean_sel[win].max():.2f} spikes/s); "
      f"response epoch is 2.6 to 3.9 s: {2.6 <= t_max <= 3.9}")
for lab, (a, b) in {"pre-sample": (-0.4, 0), "sample": (0, 1.3), "delay": (1.3, 2.6), "response": (2.6, 3.9)}.items():
    m = (tc_centres >= a) & (tc_centres < b)
    print(f"  mean selectivity, {lab}: {mean_sel[m].mean():.2f} spikes/s")
print("By group:", {g: round(float(c), 2) for g, c in zip(["(curves are pooled)"], [mean_sel.max()])})
fig, ax = plt.subplots(figsize=(6, 3))
sem = curves.std(0) / np.sqrt(len(curves))
ax.fill_between(tc_centres, mean_sel - sem, mean_sel + sem, color="0.8"); ax.plot(tc_centres, mean_sel, "k")
for x in (0, 1.3, 2.6):
    ax.axvline(x, color="k", lw=0.5, ls=":")
ax.axhline(0, color="k", lw=0.5); ax.set_xlabel("time from pole in (s)"); ax.set_ylabel("selectivity (spikes/s)")
plt.tight_layout(); plt.show()
print("Plotted range:", round(float((mean_sel - sem).min()), 2), "to", round(float((mean_sel + sem).max()), 2), "spikes/s")

# %% [markdown]
# RESULT fig2c-alm-selectivity-time-course
E
cd entries/000007-gao-2018; . $TMPDIR/explore/bin/activate; python $TMPDIR/dev/build.py $TMPDIR/dev/nb_main.py $TMPDIR/dev/run.py && time PYTHONPATH=. MPLBACKEND=Agg python $TMPDIR/dev/run.py 2>&1 | grep -v Warn | sed -n '/fig1h-fn-delay-bias/,/ed1f/p;/Pyramidal neurons tested/,$p'
```

```
######## CELL ['claim:fig1h-fn-delay-bias-either-direction']
Bias = change on ipsilateral trials minus change on contralateral trials; positive when contralateral trials lose
more, that is, when photostimulation pushes licking to the ipsilateral side.
      mouse  site  sessions  contra change  ipsi change  bias (ipsi - contra)  two_tailed_p  n_code2     direction
  BAYLORCD6 right         4        -0.0225      -0.1861               -0.1636        0.6056       74          none
 BAYLORNL15 right         5        -0.7188      -0.0420                0.6768        0.0000      103   ipsilateral
anm00314746 right         3         0.0807      -0.4127               -0.4934        0.0006       78 contralateral
anm00314757  left         2         0.0247      -0.3340               -0.3587        0.4776       22          none
anm00314758 right         4        -0.2125      -0.0884                0.1241        0.6342       98          none
anm00314760 right         3        -0.7260       0.0303                0.7563        0.0000       71   ipsilateral

######## CELL ['claim:ed1f-fn-no-early-licks']
Pyramidal neurons tested: 1818 ; without a test in some epoch (fewer than 2 trials of a type): 91
Correct control trials per neuron, median (lick right, lick left): 68 68
                           neurons  selective  preparatory  peri-movement
reading                                                                  
(a) photo-activation mice     1112      0.779        0.558          0.629
(b) all 13 mice               1818      0.751        0.525          0.596

By mouse (fractions):
[... 49 more lines not kept]
```

**Agent calls Bash**

```bash
python3 - <<'E'
p='/tmp/claude-1001/dev/nb_main.py'; s=open(p).read()
old='''print("By group:", {g: round(float(c), 2) for g, c in zip(["(curves are pooled)"], [mean_sel.max()])})
'''
new='''# Variant: preferred type from the response epoch of the screening trials.
curves_resp = []
rng_v = np.random.default_rng(203)
for s in sessions:
    if s["group"] not in ("FN", "DN"):
        continue
    tr = s["trials"]
    tested = sel[(sel.session == s["session"]) & (sel.subject == s["subject"])].set_index("unit")
    for i, sp in enumerate(s["spikes"]):
        if i not in tested.index or not tested.loc[i, "selective"]:
            continue
        ok = gao2018.stable_trials(sp, tr) & (tr.lick_early == 0).values & (tr.stim == 0).values & (tr.outcome == "hit").values
        r_idx = rng_v.permutation(np.flatnonzero(ok & (tr.trial_type == "R").values))
        l_idx = rng_v.permutation(np.flatnonzero(ok & (tr.trial_type == "L").values))
        if min(len(r_idx), len(l_idx)) < 15:
            continue
        k = gao2018.ALM_SCREEN_TRIALS
        rr = gao2018.epoch_rates(sp, tr)["response"].values
        pref_r = rr[r_idx[:k]].mean() >= rr[l_idx[:k]].mean()
        rate_r = gao2018.binned_counts(sp, tr.pole_in_time.values[r_idx[k:]], tc_centres, 0.2).mean(0) / 0.2
        rate_l = gao2018.binned_counts(sp, tr.pole_in_time.values[l_idx[k:]], tc_centres, 0.2).mean(0) / 0.2
        curves_resp.append((rate_r - rate_l) if pref_r else (rate_l - rate_r))
mean_resp = np.mean(curves_resp, axis=0)
print(f"Variant, preferred type from the response epoch: maximum at {tc_centres[win][np.argmax(mean_resp[win])]:.2f} s "
      f"({mean_resp[win].max():.2f} spikes/s); late-sample mean {mean_resp[late_sample].mean():.2f}, response-epoch mean "
      f"{mean_resp[(tc_centres >= 2.6) & (tc_centres < 3.9)].mean():.2f} spikes/s")
'''
assert old in s; s=s.replace(old,new); open(p,'w').write(s)
E
cat >> $TMPDIR/dev/nb_main.py <<'E'

# %% [markdown]
# ## Photostimulation effects on single ALM neurons
#
# For each pyramidal neuron, spike counts on control and photostimulation trials (correct and
# error, lick right and lick left pooled, no early licks, stable trials) are compared with a
# two-tailed t-test. `unit_trials` gathers what the following claims need.

# %%
def unit_trials(group):
    """Per pyramidal neuron of the group, its usable trials (correct or error, no early lick, stable)."""
    out = []
    for s in sessions:
        if s["group"] != group:
            continue
        tr = s["trials"]
        base = (tr.lick_early == 0).values & tr.outcome.isin(["hit", "error"]).values
        for i, sp in enumerate(s["spikes"]):
            if s["cell_type"][i] != "pyramidal":
                continue
            out.append({"subject": s["subject"], "session": s["session"], "unit": i, "spikes": sp,
                        "trials": tr[base & gao2018.stable_trials(sp, tr)]})
    return out


def modulation(units_, codes, onset_col, window):
    """t-test of spike counts in `window` (s from onset_col) between control and the given codes."""
    rows = []
    for u in units_:
        tr = u["trials"]
        a = tr[onset_col].values + window[0]
        n = gao2018.counts(u["spikes"], a, tr[onset_col].values + window[1]).astype(float)
        c, st = n[tr.stim.values == 0], n[np.isin(tr.stim.values, codes)]
        if len(st) < 2 or len(c) < 2:
            rows.append({"p": np.nan, "diff": np.nan, "ctrl_rate": np.nan, "stim_rate": np.nan, "n_stim": len(st)})
            continue
        w = window[1] - window[0]
        rows.append({"p": stats.ttest_ind(c, st).pvalue, "diff": (st.mean() - c.mean()) / w,
                     "ctrl_rate": c.mean() / w, "stim_rate": st.mean() / w, "n_stim": len(st)})
    return pd.DataFrame(rows)


def change_curves(units_, codes, onset_col, signs, centres, width=0.01):
    """Per neuron, photostimulation minus control rate in bins of `width` around the onset, times `signs`."""
    out = []
    for u, sg in zip(units_, signs):
        tr = u["trials"]
        t0 = tr[onset_col].values
        x = gao2018.binned_counts(u["spikes"], t0, centres, width) / width
        out.append(sg * (x[np.isin(tr.stim.values, codes)].mean(0) - x[tr.stim.values == 0].mean(0)))
    return np.array(out)


ut_pi, ut_fn, ut_dn = unit_trials("PI"), unit_trials("FN"), unit_trials("DN")
lat_centres = np.round(np.arange(-0.015, 0.1 + 1e-9, 0.001), 4)
print("Pyramidal neurons: PI", len(ut_pi), "FN", len(ut_fn), "DN", len(ut_dn))

# %% [markdown]
# ## fig3e-alm-modulated-fraction
#
# > Activity of many ALM neurons was rapidly altered by CN photo-inhibition (197/454, p < 0.01,
# > two-tailed t-test).

# %% tags=["claim:fig3e-alm-modulated-fraction"]
pi_mod = {}
for r, codes in (("(a) code 6", (6,)), ("(b) codes 5 and 6", (5, 6))):
    m = modulation(ut_pi, codes, "pole_out_time", (0.0, 1.3))
    pi_mod[r] = m
    sig = m.p < gao2018.PHOTOSTIM_P
    tested = m.p.notna()
    print(f"{r}: {int(sig.sum())}/{int(tested.sum())} neurons modulated = {sig.sum() / tested.sum():.3f} "
          f"(expected 0.434 +/- 0.043; within: {abs(sig.sum() / tested.sum() - 0.434) <= 0.043}); not tested: {int((~tested).sum())}")
m = pi_mod["(a) code 6"]
m["subject"] = [u["subject"] for u in ut_pi]
print("\nBy mouse, reading (a):")
print(m.groupby("subject").apply(lambda g: pd.Series({"neurons": int(g.p.notna().sum()), "modulated": float((g.p < 0.01).mean())}),
                                 include_groups=False).round(3).to_string())
print("Threshold variant, reading (a), p < 0.05:", round(float((m.p < 0.05).sum() / m.p.notna().sum()), 3))
# A control-against-control check of the false-positive rate: control trials split at random in two.
rng = np.random.default_rng(301)
fp = []
for u in ut_pi:
    tr = u["trials"]
    n = gao2018.counts(u["spikes"], tr.pole_out_time.values, tr.cue_time.values)[tr.stim.values == 0]
    k = rng.permutation(len(n))
    fp.append(stats.ttest_ind(n[k[: len(k) // 2]], n[k[len(k) // 2:]]).pvalue < 0.01 if len(n) > 4 else np.nan)
print("Control trials split in two halves, fraction 'modulated':", round(float(np.nanmean(fp)), 3), "(expected 0.01)")

# %% [markdown]
# RESULT fig3e-alm-modulated-fraction

# %% [markdown]
# ## fig3e-alm-mean-rate-unchanged
#
# > CN photo-inhibition left the average ALM spike rate nearly unchanged (control 4.15,
# > photo-inhibition 4.39 spikes/s, p = 0.58, two-tailed t-test).

# %% tags=["claim:fig3e-alm-mean-rate-unchanged"]
m = pi_mod["(a) code 6"].dropna(subset=["p"])
print(f"Neurons: {len(m)}; mean delay-epoch rate control {m.ctrl_rate.mean():.2f}, code 6 {m.stim_rate.mean():.2f} spikes/s "
      "(expected 4.15 +/- 0.415 and 4.39 +/- 0.439)")
print(f"Two-sample t-test across neurons: p = {stats.ttest_ind(m.ctrl_rate, m.stim_rate).pvalue:.3f}")
print(f"Variant, paired t-test: p = {stats.ttest_rel(m.ctrl_rate, m.stim_rate).pvalue:.3g}; median change "
      f"{(m.stim_rate - m.ctrl_rate).median():+.3f} spikes/s")
mb = pi_mod["(b) codes 5 and 6"].dropna(subset=["p"])
print(f"Variant, codes 5 and 6: control {mb.ctrl_rate.mean():.2f}, photo-inhibition {mb.stim_rate.mean():.2f} spikes/s, "
      f"two-sample p = {stats.ttest_ind(mb.ctrl_rate, mb.stim_rate).pvalue:.3f}")

# %% [markdown]
# RESULT fig3e-alm-mean-rate-unchanged

# %% [markdown]
# ## fig3e-alm-up-down
#
# > Individual ALM neurons increased (108/197) or decreased (89/197) their responses during CN
# > photo-inhibition.

# %% tags=["claim:fig3e-alm-up-down"]
for r, m in pi_mod.items():
    sig = m[m.p < 0.01]
    up = int((sig["diff"] > 0).sum())
    print(f"{r}: {up} increased, {len(sig) - up} decreased; fraction increased {up / len(sig):.3f} "
          f"(expected 0.548 +/- 0.055); binomial p = {stats.binomtest(up, len(sig)).pvalue:.3g}")

# %% [markdown]
# RESULT fig3e-alm-up-down

# %% [markdown]
# ## fig3-alm-latency-pi
#
# > The ALM response to CN photo-inhibition had a latency of 7.1 +/- 3.8 ms (mean +/- s.e.m.).

# %% tags=["claim:fig3-alm-latency-pi"]
rng = np.random.default_rng(302)
lat_results = {}
for r, codes in (("(a) code 6", (6,)), ("(b) codes 5 and 6", (5, 6))):
    m = pi_mod[r]
    sig = (m.p < 0.01).values
    units_sig = [u for u, k in zip(ut_pi, sig) if k]
    ch = change_curves(units_sig, codes, "pole_out_time", np.sign(m["diff"].values[sig]), lat_centres)
    mean, sd, onsets = gao2018.onset_latency(ch, lat_centres, rng)
    lat_results[r] = (mean, sd)
    print(f"{r}: {len(units_sig)} neurons; onset {mean * 1000:.1f} +/- {sd * 1000:.1f} ms (bootstrap s.d. over neurons); "
          f"resamples without an onset in the window: {int(np.isnan(onsets).sum())}")
    print(f"   expected 7.1 +/- 3.8 ms; within: {abs(mean * 1000 - 7.1) <= 3.8}")
    print("   population change (spikes/s) at bin centres -10, 0, 5, 10, 15, 20, 30 ms:",
          [round(float(ch.mean(0)[np.argmin(np.abs(lat_centres - x / 1000))]), 2) for x in (-10, 0, 5, 10, 15, 20, 30)])
print("Variant, 20 ms bins, reading (a):")
m = pi_mod["(a) code 6"]; sig = (m.p < 0.01).values
ch20 = change_curves([u for u, k in zip(ut_pi, sig) if k], (6,), "pole_out_time", np.sign(m["diff"].values[sig]), lat_centres, 0.02)
mean20, sd20, _ = gao2018.onset_latency(ch20, lat_centres, rng, n_boot=2000)
print(f"   onset {mean20 * 1000:.1f} +/- {sd20 * 1000:.1f} ms")

# %% [markdown]
# RESULT fig3-alm-latency-pi

# %% [markdown]
# ## fig3f-alm-selectivity-abolished
#
# > ALM trial-type selectivity was abolished by CN photo-inhibition.

# %% tags=["claim:fig3f-alm-selectivity-abolished"]
def photostim_selectivity(units_, codes, rng, onset_col="pole_out_time", min_stim=4, centres=None):
    """Selectivity (preferred minus non-preferred) on held-out control and on photostimulation trials.

    Neurons selective in the sample or delay epoch (t-test p < 0.05, correct and error trials by
    instructed type, control trials), with at least `min_stim` photostimulation trials of each
    type and 15 control trials of each type; preferred type from the delay rate of 10 random
    control trials of each type.
    """
    rows, curves_c, curves_s = [], [], []
    for u in units_:
        tr, sp = u["trials"], u["spikes"]
        r = gao2018.epoch_rates(sp, tr)
        ctrl, stim = tr.stim.values == 0, np.isin(tr.stim.values, codes)
        R, L = (tr.trial_type == "R").values, (tr.trial_type == "L").values
        if min((ctrl & R).sum(), (ctrl & L).sum()) < 15 or min((stim & R).sum(), (stim & L).sum()) < min_stim:
            continue
        p_s = stats.ttest_ind(r["sample"].values[ctrl & R], r["sample"].values[ctrl & L]).pvalue
        p_d = stats.ttest_ind(r["delay"].values[ctrl & R], r["delay"].values[ctrl & L]).pvalue
        if not (p_s < 0.05 or p_d < 0.05):
            continue
        ri, li = rng.permutation(np.flatnonzero(ctrl & R)), rng.permutation(np.flatnonzero(ctrl & L))
        k = gao2018.ALM_SCREEN_TRIALS
        d = r["delay"].values
        sgn = 1.0 if d[ri[:k]].mean() >= d[li[:k]].mean() else -1.0
        ctrl_sel = sgn * (d[ri[k:]].mean() - d[li[k:]].mean())
        stim_sel = sgn * (d[stim & R].mean() - d[stim & L].mean())
        rows.append({"subject": u["subject"], "ctrl": ctrl_sel, "stim": stim_sel})
        if centres is not None:
            x = gao2018.binned_counts(sp, tr[onset_col].values, centres, 0.2) / 0.2
            curves_c.append(sgn * (x[ri[k:]].mean(0) - x[li[k:]].mean(0)))
            curves_s.append(sgn * (x[stim & R].mean(0) - x[stim & L].mean(0)))
    return pd.DataFrame(rows), np.array(curves_c), np.array(curves_s)


def judge_abolished(tbl, rng, label):
    ratio = tbl.stim.mean() / tbl.ctrl.mean()
    boot = np.array([tbl.iloc[rng.integers(0, len(tbl), len(tbl))].pipe(lambda t: t.stim.mean() - t.ctrl.mean())
                     for _ in range(10000)])
    p = float((boot >= 0).mean())
    print(f"{label}: {len(tbl)} neurons; delay selectivity control {tbl.ctrl.mean():.2f}, photostim {tbl.stim.mean():.2f} "
          f"spikes/s; ratio {ratio:.2f}; one-tailed bootstrap p (photostim not lower) = {p:.4f}; "
          f"95% interval of photostim selectivity {np.percentile([tbl.stim.iloc[rng.integers(0, len(tbl), len(tbl))].mean() for _ in range(2000)], [2.5, 97.5]).round(2).tolist()}")
    return ratio, p


rng = np.random.default_rng(303)
sel_centres = np.round(np.arange(-1.3, 2.6 + 1e-9, 0.02), 3)
pi_sel, pc, ps = photostim_selectivity(ut_pi, (6,), rng, centres=sel_centres)
judge_abolished(pi_sel, rng, "Code 6 (1.3 s)")
print("By mouse:"); print(pi_sel.groupby("subject")[["ctrl", "stim"]].agg(["mean", "size"]).round(2).to_string())
pi_sel_b, _, _ = photostim_selectivity(ut_pi, (5, 6), rng)
judge_abolished(pi_sel_b, rng, "Variant, codes 5 and 6")
fig, ax = plt.subplots(figsize=(6, 3))
ax.plot(sel_centres, pc.mean(0), "k", label="control"); ax.plot(sel_centres, ps.mean(0), "c", label="CN photo-inhibition (code 6)")
for x in (-1.3, 0, 1.3):
    ax.axvline(x, color="k", lw=0.5, ls=":")
ax.axhline(0, color="k", lw=0.5); ax.set_xlabel("time from delay onset (s)"); ax.set_ylabel("selectivity (spikes/s)"); ax.legend()
plt.tight_layout(); plt.show()
print("Plotted range:", round(float(min(pc.mean(0).min(), ps.mean(0).min())), 2), "to",
      round(float(max(pc.mean(0).max(), ps.mean(0).max())), 2), "spikes/s")

# %% [markdown]
# RESULT fig3f-alm-selectivity-abolished
E
cd entries/000007-gao-2018; . $TMPDIR/explore/bin/activate; python $TMPDIR/dev/build.py $TMPDIR/dev/nb_main.py $TMPDIR/dev/run.py && time PYTHONPATH=. MPLBACKEND=Agg python $TMPDIR/dev/run.py 2>&1 | grep -v Warn | sed -n '/Variant, preferred type from the response/,$p'
```

```
Variant, preferred type from the response epoch: maximum at 3.09 s (2.66 spikes/s); late-sample mean 0.55, response-epoch mean 2.31 spikes/s
Plotted range: -0.04 to 2.72 spikes/s

######## CELL []
Pyramidal neurons: PI 706 FN 567 DN 545

######## CELL ['claim:fig3e-alm-modulated-fraction']
(a) code 6: 234/643 neurons modulated = 0.364 (expected 0.434 +/- 0.043; within: False); not tested: 63
(b) codes 5 and 6: 298/695 neurons modulated = 0.429 (expected 0.434 +/- 0.043; within: True); not tested: 11

By mouse, reading (a):
            neurons  modulated
subject                       
BAYLORCD12    145.0      0.183
BAYLORCD13     93.0      0.177
BAYLORCD14    183.0      0.443
BAYLORCD8     222.0      0.393
Threshold variant, reading (a), p < 0.05: 0.446
Control trials split in two halves, fraction 'modulated': 0.01 (expected 0.01)

[... 37 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/000007-gao-2018; . $TMPDIR/explore/bin/activate; cat > $TMPDIR/dev/dbg2.py <<'E'
src=open('/tmp/claude-1001/dev/run.py').read()
cut=src.index("print('\\n######## CELL [\\'claim:fig3e-alm-mean-rate-unchanged\\']')")
exec(src[:cut])
rng=np.random.default_rng(0)
cen=np.round(np.arange(-0.2,0.1+1e-9,0.005),4)
for codes in [(6,),(5,),(5,6)]:
    m=modulation(ut_pi, codes, "pole_out_time", (0.0, 1.3)); sig=(m.p<0.01).values
    ch=change_curves([u for u,k in zip(ut_pi,sig) if k], codes, "pole_out_time", np.sign(m['diff'].values[sig]), cen)
    print(codes, sig.sum(), np.round(ch.mean(0),2)[::2])
    pre=ch[:, cen<-0.01].mean(1,keepdims=True)
    print(' baseline-subtracted', np.round((ch-pre).mean(0),2)[::2])
E
PYTHONPATH=. MPLBACKEND=Agg python $TMPDIR/dev/dbg2.py 2>&1 | tail -6
```

```
Traceback (most recent call last):
  File "/tmp/claude-1001/dev/dbg2.py", line 2, in <module>
    cut=src.index("print('\\n######## CELL [\\'claim:fig3e-alm-mean-rate-unchanged\\']')")
ValueError: substring not found
```

**Agent calls Bash**

```bash
cd entries/000007-gao-2018; . $TMPDIR/explore/bin/activate; grep -n "CELL" $TMPDIR/dev/run.py | head -3; sed -i 's|^cut=.*|cut=src.index("claim:fig3e-alm-mean-rate-unchanged"); cut=src.rindex("\\n",0,cut)|' $TMPDIR/dev/dbg2.py; PYTHONPATH=. MPLBACKEND=Agg python $TMPDIR/dev/dbg2.py 2>&1 | tail -6
```

```
1:print('\n######## CELL []')
24:print("\n######## CELL ['sanity']")
51:print("\n######## CELL ['sanity']")
(5, 6) 298 [-0.12 -0.08  0.03 -0.12  0.02 -0.16 -0.44 -0.05  0.08 -0.01  0.53  0.12
  0.18 -0.1   0.05 -0.11  0.7   0.2  -0.22 -0.08  0.24  0.36 -0.01  1.06
  2.46  3.85  4.05  3.82  4.24  4.16  4.24]
 baseline-subtracted [-0.16 -0.11 -0.01 -0.15 -0.01 -0.19 -0.47 -0.09  0.04 -0.04  0.5   0.09
  0.15 -0.13  0.02 -0.14  0.67  0.16 -0.26 -0.12  0.2   0.33 -0.04  1.02
  2.43  3.82  4.02  3.79  4.21  4.12  4.21]
```

**Agent calls Bash**

```bash
cd entries/000007-gao-2018; . $TMPDIR/explore/bin/activate; PYTHONPATH=. MPLBACKEND=Agg python $TMPDIR/dev/dbg2.py 2>&1 | grep -v Warn | tail -18 | head -12
```

```
(6,) 234 [-0.62  0.15  0.85 -0.42 -0.07  0.88  0.23 -0.42  0.46  0.13  0.26  0.21
  0.16 -0.14  0.6   0.17  0.92  0.23 -0.1   0.21  0.75  0.8   0.08  0.39
  2.23  3.95  4.37  3.39  4.41  4.12  4.56]
 baseline-subtracted [-0.81 -0.05  0.65 -0.62 -0.26  0.68  0.03 -0.62  0.26 -0.07  0.07  0.02
 -0.04 -0.34  0.4  -0.02  0.72  0.03 -0.3   0.01  0.55  0.61 -0.11  0.2
  2.04  3.75  4.17  3.19  4.21  3.93  4.37]
(5,) 229 [ 0.17 -0.13  0.35 -0.33 -0.1  -0.67  0.03  0.08  0.07 -0.04  0.56  0.54
 -0.2  -0.07 -0.09 -0.28  0.81  0.21 -0.08 -0.12  0.49  0.02  0.06  0.91
  3.34  4.67  3.87  4.37  4.    4.14  4.44]
 baseline-subtracted [ 0.13 -0.17  0.3  -0.38 -0.15 -0.71 -0.02  0.03  0.03 -0.09  0.52  0.5
 -0.24 -0.12 -0.13 -0.33  0.76  0.17 -0.13 -0.16  0.44 -0.03  0.01  0.86
  3.29  4.62  3.82  4.33  3.96  4.1   4.4 ]
```

**Agent**

The CN photo-inhibition latency in ALM is clearly about 30 to 35 ms in the data; the paper's first-crossing method picks up noise before that. I'll add a sustained-onset variant to show this.

**Agent calls Bash**

```bash
cd entries/000007-gao-2018; python3 - <<'E'
p='gao2018.py'; s=open(p).read()
start=s.index("def onset_latency")
new='''def onset_latency(change: np.ndarray, centres: np.ndarray, rng: np.random.Generator, n_boot: int = 10000,
                  p: float = 0.01, run: int = 1) -> tuple[float, float, np.ndarray]:
    """Onset of a population rate change (units x bins), as in Extended Data Fig. 9a.

    The onset is the first bin centre at which the change across units is above 0 (one-sample
    t-test, p < 0.01). With `run` > 1 (a variant here, not the paper's), the first of `run`
    consecutive such bins. Units are resampled with replacement `n_boot` times; returns the mean
    and standard deviation of the resampled onsets (the bootstrap standard error) and the onsets.
    """
    def first(x):
        t, pv = stats.ttest_1samp(x, 0.0, axis=0)
        ok = ((pv < p) & (t > 0)).astype(int)
        if run > 1:
            ok = (np.convolve(ok, np.ones(run, int), mode="full")[run - 1:] == run).astype(int)
        hit = np.flatnonzero(ok)
        return centres[hit[0]] if len(hit) else np.nan
    onsets = np.array([first(change[rng.integers(0, len(change), len(change))]) for _ in range(n_boot)])
    return float(np.nanmean(onsets)), float(np.nanstd(onsets)), onsets
'''
s=s[:start]+new; open(p,'w').write(s)
p='/tmp/claude-1001/dev/nb_main.py'; s=open(p).read()
old='''print("Variant, 20 ms bins, reading (a):")
m = pi_mod["(a) code 6"]; sig = (m.p < 0.01).values
ch20 = change_curves([u for u, k in zip(ut_pi, sig) if k], (6,), "pole_out_time", np.sign(m["diff"].values[sig]), lat_centres, 0.02)
mean20, sd20, _ = gao2018.onset_latency(ch20, lat_centres, rng, n_boot=2000)
print(f"   onset {mean20 * 1000:.1f} +/- {sd20 * 1000:.1f} ms")'''
new='''# Variants: the first of 10 consecutive significant bins (a sustained change), and the change in 5 ms
# steps from 50 ms before onset, to show where the rise is.
wide_centres = np.round(np.arange(-0.05, 0.1 + 1e-9, 0.005), 3)
for r, codes in (("(a) code 6", (6,)), ("(b) codes 5 and 6", (5, 6)), ("code 5 alone", (5,))):
    m = pi_mod[r] if r in pi_mod else modulation(ut_pi, codes, "pole_out_time", (0.0, 1.3))
    sig = (m.p < 0.01).values
    units_sig = [u for u, k in zip(ut_pi, sig) if k]
    ch = change_curves(units_sig, codes, "pole_out_time", np.sign(m["diff"].values[sig]), lat_centres)
    mean10, sd10, _ = gao2018.onset_latency(ch, lat_centres, rng, n_boot=2000, run=10)
    chw = change_curves(units_sig, codes, "pole_out_time", np.sign(m["diff"].values[sig]), wide_centres).mean(0)
    print(f"{r}: sustained onset {mean10 * 1000:.1f} +/- {sd10 * 1000:.1f} ms; change in 10 ms bins at -50 to +100 ms (5 ms steps):")
    print("   ", np.round(chw, 1).tolist())'''
assert old in s; s=s.replace(old,new); open(p,'w').write(s)
E
echo ok
```

```
ok
```

**Agent calls Bash**

```bash
cat >> $TMPDIR/dev/nb_main.py <<'E'

# %% [markdown]
# ## ed9a-fn-latency
#
# > Fastigial photo-activation induced rapid changes in ALM activity, with a latency of 4.5 +/- 2.6
# > ms, in 227 significantly modulated neurons.
#
# For reading (b) the sample (code 1) and delay (code 2) photostimulation trials are pooled, each
# aligned to its own onset: the counts in the 0.5 s after onset are taken as deviations from the
# control mean in the same task window, and the change curves are the trial-weighted mean of the
# two codes' curves.

# %%
def act_modulation_and_change(units_, codes_onsets, centres):
    """Modulation (0.5 s after onset) and change curves for photo-activation codes, pooled over codes."""
    rows, curves = [], []
    for u in units_:
        tr, sp = u["trials"], u["spikes"]
        ctrl_dev, stim_dev, curve, n_tot = [], [], 0.0, 0
        ok = True
        for code, col in codes_onsets:
            t0 = tr[col].values
            n = gao2018.counts(sp, t0, t0 + 0.5).astype(float)
            c, st = tr.stim.values == 0, tr.stim.values == code
            if st.sum() < 2 or c.sum() < 2:
                ok = False
                break
            mu = n[c].mean()
            ctrl_dev.append(n[c] - mu); stim_dev.append(n[st] - mu)
            x = gao2018.binned_counts(sp, t0, centres, 0.01) / 0.01
            curve = curve + st.sum() * (x[st].mean(0) - x[c].mean(0)); n_tot += st.sum()
        if not ok:
            rows.append({"p": np.nan, "diff": np.nan}); curves.append(np.full(len(centres), np.nan))
            continue
        cd_, sd_ = np.concatenate(ctrl_dev), np.concatenate(stim_dev)
        rows.append({"p": stats.ttest_ind(cd_, sd_).pvalue, "diff": sd_.mean() / 0.5})
        curves.append(curve / n_tot)
    return pd.DataFrame(rows), np.array(curves)


def latency_claim(units_, readings_, rng, label):
    out = {}
    for r, codes_onsets in readings_.items():
        m, curves_ = act_modulation_and_change(units_, codes_onsets, lat_centres)
        sig = (m.p < 0.01).values
        ch = curves_[sig] * np.sign(m["diff"].values[sig])[:, None]
        mean, sd, onsets = gao2018.onset_latency(ch, lat_centres, rng)
        mean10, sd10, _ = gao2018.onset_latency(ch, lat_centres, rng, n_boot=2000, run=10)
        out[r] = (int(sig.sum()), mean, sd)
        print(f"{label} {r}: {int(sig.sum())} of {int(m.p.notna().sum())} neurons modulated; onset {mean * 1000:.1f} +/- "
              f"{sd * 1000:.1f} ms; resampled onsets before 0 ms: {float((onsets < 0).mean()):.3f}; "
              f"variant, sustained onset {mean10 * 1000:.1f} +/- {sd10 * 1000:.1f} ms")
        print("    population change (spikes/s) at bin centres -10, 0, 5, 10, 15, 20, 30 ms:",
              [round(float(ch.mean(0)[np.argmin(np.abs(lat_centres - x / 1000))]), 2) for x in (-10, 0, 5, 10, 15, 20, 30)])
    return out

# %% tags=["claim:ed9a-fn-latency"]
rng = np.random.default_rng(401)
fn_lat = latency_claim(ut_fn, {"(a) code 2": [(2, "pole_out_time")],
                               "(b) codes 1 and 2": [(1, "pole_in_time"), (2, "pole_out_time")]}, rng, "FN")
for r, (n, mean, sd) in fn_lat.items():
    print(f"{r}: latency within 4.5 +/- 2.6 ms: {abs(mean * 1000 - 4.5) <= 2.6}; count within 227 +/- 22.7: {abs(n - 227) <= 22.7}")

# %% [markdown]
# RESULT ed9a-fn-latency

# %% [markdown]
# ## ed9a-dn-latency
#
# > Dentate photo-activation also induced ALM response changes, with a latency of 8.3 +/- 5.0 ms,
# > in 163 significantly modulated neurons.

# %% tags=["claim:ed9a-dn-latency"]
rng = np.random.default_rng(402)
dn_lat = latency_claim(ut_dn, {"(a) code 4": [(4, "pole_out_time")],
                               "(b) codes 3 and 4": [(3, "pole_in_time"), (4, "pole_out_time")]}, rng, "DN")
for r, (n, mean, sd) in dn_lat.items():
    print(f"{r}: latency within 8.3 +/- 5.0 ms: {abs(mean * 1000 - 8.3) <= 5.0}; count within 163 +/- 16.3: {abs(n - 163) <= 16.3}")

# %% [markdown]
# RESULT ed9a-dn-latency

# %% [markdown]
# ## fig4f-fn-persistent
#
# > Transient photo-activation of the fastigial nucleus altered ALM preparatory activity long (more
# > than 1 s) after the photostimulus ended.

# %%
fr_centres = np.round(np.arange(-1.1, 2.6 + 1e-9, 0.05), 3)   # 400 ms bins, centres from delay onset


def fraction_modulated(units_, code):
    sig = []
    for u in units_:
        tr = u["trials"]
        x = gao2018.binned_counts(u["spikes"], tr.pole_out_time.values, fr_centres, 0.4)
        c, st = x[tr.stim.values == 0], x[tr.stim.values == code]
        if len(st) < 2:
            continue
        with np.errstate(all="ignore"):
            p = stats.ttest_ind(c, st, axis=0).pvalue
        sig.append(np.nan_to_num(p, nan=1.0) < 0.01)
    return np.array(sig)


sig_fn, sig_dn = fraction_modulated(ut_fn, 2), fraction_modulated(ut_dn, 4)
pre_bin = np.argmin(np.abs(fr_centres - (-0.2)))    # 400 ms ending at photostimulus onset
post_bin = np.argmin(np.abs(fr_centres - 1.7))      # 1.0 to 1.4 s after offset (offset at 0.5 s)
frac_tbl = pd.DataFrame({"centre_s": fr_centres, "FN": sig_fn.mean(0), "DN": sig_dn.mean(0)})
print("Neurons: FN", len(sig_fn), "DN", len(sig_dn))
print("Fraction modulated (p < 0.01) per 400 ms bin, every fourth bin; centres from delay onset (cue at 1.3 s):")
print(frac_tbl.iloc[::4].round(3).to_string(index=False))

# %% tags=["claim:fig4f-fn-persistent"]
a, b = int(sig_fn[:, post_bin].sum()), int(sig_fn[:, pre_bin].sum())
n = len(sig_fn)
p = stats.fisher_exact([[a, n - a], [b, n - b]], alternative="greater").pvalue
print(f"FN, bin ending at photostimulus onset ({fr_centres[pre_bin] - 0.2:.1f} to {fr_centres[pre_bin] + 0.2:.1f} s): {b}/{n} = {b / n:.3f}")
print(f"FN, bin 1.0 to 1.4 s after offset ({fr_centres[post_bin] - 0.2:.1f} to {fr_centres[post_bin] + 0.2:.1f} s): {a}/{n} = {a / n:.3f}")
print(f"ratio {a / max(b, 1):.1f}; one-tailed Fisher exact p = {p:.2g}")
for lag_s in (0.5, 0.8, 1.2):
    k = np.argmin(np.abs(fr_centres - (0.5 + lag_s + 0.2)))
    print(f"  variant, bin starting {lag_s} s after offset: {sig_fn[:, k].mean():.3f}")
fig, ax = plt.subplots(figsize=(6, 3))
ax.plot(fr_centres, frac_tbl.FN, "b", label="fastigial (code 2)"); ax.plot(fr_centres, frac_tbl.DN, "r", label="dentate (code 4)")
ax.axvspan(0, 0.5, color="c", alpha=0.3); ax.axvline(1.3, color="k", lw=0.5, ls=":")
ax.set_xlabel("400 ms bin centre from delay onset (s)"); ax.set_ylabel("fraction modulated"); ax.legend()
plt.tight_layout(); plt.show()
print("Plotted range:", round(float(frac_tbl[["FN", "DN"]].min().min()), 3), "to", round(float(frac_tbl[["FN", "DN"]].max().max()), 3))

# %% [markdown]
# RESULT fig4f-fn-persistent

# %% [markdown]
# ## fig4g-dn-recovery
#
# > ALM activity quickly recovered after dentate photo-activation.

# %% tags=["claim:fig4g-dn-recovery"]
a_d, b_d = int(sig_dn[:, post_bin].sum()), int(sig_dn[:, pre_bin].sum())
n_d = len(sig_dn)
p_vs_fn = stats.fisher_exact([[a_d, n_d - a_d], [a, n - a]]).pvalue
print(f"DN, bin ending at onset: {b_d}/{n_d} = {b_d / n_d:.3f}; bin 1.0 to 1.4 s after offset: {a_d}/{n_d} = {a_d / n_d:.3f} "
      f"(ratio {a_d / max(b_d, 1):.1f})")
print(f"FN in the same bin: {a / n:.3f}; two-tailed Fisher exact p (DN against FN) = {p_vs_fn:.2g}")
during = np.argmin(np.abs(fr_centres - 0.25))
print(f"During photostimulation (bin centred 0.25 s): FN {sig_fn[:, during].mean():.3f}, DN {sig_dn[:, during].mean():.3f}")
print("By mouse, DN, post-offset bin:", {m: round(float(sig_dn[[u['subject'] == m for u in ut_dn]][:, post_bin].mean()), 3)
                                         for m in sorted({u['subject'] for u in ut_dn})})

# %% [markdown]
# RESULT fig4g-dn-recovery

# %% [markdown]
# ## Coding direction (Figure 4i, Extended Data Figure 10d)
#
# `cd_sessions` computes, for each session, the coding direction from a random half of the correct
# control trials and the projections of the other control trials and the photostimulation trials.
# Neurons are those whose stable trials cover at least half of the session's usable trials, and
# trials are those stable for all of them (a choice made here).

# %%
cd_centres = np.round(np.arange(0.2, 1.1 + 1e-9, 0.01), 3)    # 400 ms windows inside the delay, from delay onset
traj_centres = np.round(np.arange(-1.1, 1.3 + 1e-9, 0.05), 3)


def cd_sessions(group, code, rng):
    out = []
    for s in sessions:
        if s["group"] != group:
            continue
        tr = s["trials"]
        base = (tr.lick_early == 0).values & tr.outcome.isin(["hit", "error"]).values
        pyr = [i for i in range(len(s["spikes"])) if s["cell_type"][i] == "pyramidal"]
        stab = {i: gao2018.stable_trials(s["spikes"][i], tr) & base for i in pyr}
        keep_u = [i for i in pyr if stab[i].sum() >= 0.5 * base.sum()]
        if not keep_u:
            continue
        ok = np.logical_and.reduce([stab[i] for i in keep_u])
        t = tr[ok]
        ctrl_hit = np.flatnonzero((t.stim.values == 0) & (t.outcome.values == "hit"))
        R, L = t.trial_type.values == "R", t.trial_type.values == "L"
        n_ok = min(((t.stim.values == code) & R).sum(), ((t.stim.values == code) & L).sum(),
                   ((t.stim.values == 0) & R).sum(), ((t.stim.values == 0) & L).sum())
        if len(keep_u) <= 5 or n_ok <= 5:
            continue
        train = np.zeros(len(t), bool)
        for side in (R, L):
            idx = rng.permutation(np.intersect1d(ctrl_hit, np.flatnonzero(side)))
            train[idx[: len(idx) // 2]] = True
        X = np.stack([gao2018.binned_counts(s["spikes"][i], t.pole_out_time.values, cd_centres, 0.4) for i in keep_u], axis=2)
        cd = (X[train & R].mean(0) - X[train & L].mean(0)).mean(0)
        last = np.stack([gao2018.binned_counts(s["spikes"][i], t.cue_time.values, [-0.2], 0.4)[:, 0] for i in keep_u], axis=1)
        traj = np.stack([gao2018.binned_counts(s["spikes"][i], t.pole_out_time.values, traj_centres, 0.4) for i in keep_u], axis=2)
        proj_last, proj_traj = last @ cd, traj @ cd
        offset = proj_traj[train].mean()
        ep_r, ep_l = proj_last[train & R].mean(), proj_last[train & L].mean()
        test_ctrl, stim = (~train) & (t.stim.values == 0), t.stim.values == code
        licked_r = ((t.outcome.values == "hit") & R) | ((t.outcome.values == "error") & L)
        out.append({"subject": s["subject"], "session": s["session"], "neurons": len(keep_u),
                    "sep_ctrl": proj_last[test_ctrl & R].mean() - proj_last[test_ctrl & L].mean(),
                    "sep_stim": proj_last[stim & R].mean() - proj_last[stim & L].mean(),
                    "traj": {k: (proj_traj[m & R].mean(0) - offset, proj_traj[m & L].mean(0) - offset)
                             for k, m in (("ctrl", test_ctrl), ("stim", stim))},
                    "x_ctrl": (proj_last[test_ctrl] - (ep_r + ep_l) / 2) / (ep_r - ep_l), "y_ctrl": licked_r[test_ctrl],
                    "x_stim": (proj_last[stim] - (ep_r + ep_l) / 2) / (ep_r - ep_l), "y_stim": licked_r[stim],
                    "n_stim": int(stim.sum()), "n_test_ctrl": int(test_ctrl.sum())})
    return pd.DataFrame(out)


rng = np.random.default_rng(501)
cd_fn, cd_dn = cd_sessions("FN", 2, rng), cd_sessions("DN", 4, rng)
n_fn_sessions = len({(s["subject"], s["session"]) for s in sessions if s["group"] == "FN"})
n_dn_sessions = len({(s["subject"], s["session"]) for s in sessions if s["group"] == "DN"})
print(f"Sessions used: FN {len(cd_fn)} of {n_fn_sessions}, DN {len(cd_dn)} of {n_dn_sessions} "
      "(paper, 28 of 39 sessions over both groups and the excluded mouse)")
print("Neurons per session: FN", cd_fn.neurons.tolist(), "; DN", cd_dn.neurons.tolist())
print(cd_fn[["subject", "session", "neurons", "sep_ctrl", "sep_stim", "n_stim"]].round(2).to_string(index=False))
print(cd_dn[["subject", "session", "neurons", "sep_ctrl", "sep_stim", "n_stim"]].round(2).to_string(index=False))


def sep_ratio(tbl, idx):
    t = tbl.iloc[idx]
    return t.sep_stim.mean() / t.sep_ctrl.mean()


rng = np.random.default_rng(502)
boot_fn = np.array([sep_ratio(cd_fn, rng.integers(0, len(cd_fn), len(cd_fn))) for _ in range(10000)])
boot_dn = np.array([sep_ratio(cd_dn, rng.integers(0, len(cd_dn), len(cd_dn))) for _ in range(10000)])
ratio_fn, ratio_dn = sep_ratio(cd_fn, np.arange(len(cd_fn))), sep_ratio(cd_dn, np.arange(len(cd_dn)))

# %% [markdown]
# ## fig4i-fn-cd-collapse
#
# > Fastigial photo-activation resulted in a collapse of ALM activity trajectories along the coding
# > direction, destroying the coding of future movement.

# %% tags=["claim:fig4i-fn-cd-collapse"]
print(f"FN: separation in the last 400 ms of the delay, control {cd_fn.sep_ctrl.mean():.2f}, code 2 {cd_fn.sep_stim.mean():.2f} "
      f"(spike-count units); ratio {ratio_fn:.2f}, bootstrap 95% interval {np.percentile(boot_fn, 2.5):.2f} to {np.percentile(boot_fn, 97.5):.2f}")
print("Sessions with a smaller separation on code 2 trials:", int((cd_fn.sep_stim < cd_fn.sep_ctrl).sum()), "of", len(cd_fn))
print("By mouse, ratio:", cd_fn.groupby("subject").apply(lambda t: round(t.sep_stim.mean() / t.sep_ctrl.mean(), 2), include_groups=False).to_dict())
fig, axes = plt.subplots(1, 2, figsize=(10, 3), sharey=True)
rng_lo, rng_hi = np.inf, -np.inf
for ax, (lab, tbl) in zip(axes, (("fastigial (code 2)", cd_fn), ("dentate (code 4)", cd_dn))):
    for cond, ls in (("ctrl", "-"), ("stim", "--")):
        r_ = np.mean([t[cond][0] for t in tbl.traj], axis=0); l_ = np.mean([t[cond][1] for t in tbl.traj], axis=0)
        ax.plot(traj_centres, r_, "b" + ls, label=f"lick right, {cond}"); ax.plot(traj_centres, l_, "r" + ls, label=f"lick left, {cond}")
        rng_lo, rng_hi = min(rng_lo, r_.min(), l_.min()), max(rng_hi, r_.max(), l_.max())
    ax.axvspan(0, 0.5, color="c", alpha=0.2); ax.set_title(lab); ax.set_xlabel("400 ms window centre from delay onset (s)")
axes[0].set_ylabel("projection on cd (offset removed)"); axes[1].legend(fontsize=7)
plt.tight_layout(); plt.show()
print("Plotted range:", round(float(rng_lo), 2), "to", round(float(rng_hi), 2))

# %% [markdown]
# RESULT fig4i-fn-cd-collapse

# %% [markdown]
# ## fig4i-dn-cd-minimal
#
# > Dentate photo-activation minimally impacted ALM activity trajectories along the coding
# > direction, despite having an impact on ALM neuron responses.

# %% tags=["claim:fig4i-dn-cd-minimal"]
print(f"DN: separation control {cd_dn.sep_ctrl.mean():.2f}, code 4 {cd_dn.sep_stim.mean():.2f}; ratio {ratio_dn:.2f}, "
      f"bootstrap 95% interval {np.percentile(boot_dn, 2.5):.2f} to {np.percentile(boot_dn, 97.5):.2f}")
print(f"Fraction of paired resamples with the FN ratio below the DN ratio: {float((boot_fn < boot_dn).mean()):.4f}")
print("By mouse, ratio:", cd_dn.groupby("subject").apply(lambda t: round(t.sep_stim.mean() / t.sep_ctrl.mean(), 2), include_groups=False).to_dict())
print("Sessions with a smaller separation on code 4 trials:", int((cd_dn.sep_stim < cd_dn.sep_ctrl).sum()), "of", len(cd_dn))

# %% [markdown]
# RESULT fig4i-dn-cd-minimal

# %% [markdown]
# ## ed10d-fn-no-prediction
#
# > After fastigial photo-activation, ALM activity along the coding direction no longer predicted
# > the future movement direction (n = 337 trials).

# %% tags=["claim:ed10d-fn-no-prediction"]
import statsmodels.api as sm


def logit(x, y):
    fit = sm.Logit(y.astype(float), sm.add_constant(x)).fit(disp=0)
    return fit.params[1], fit.pvalues[1], len(y)


for lab, tbl in (("FN", cd_fn), ("DN", cd_dn)):
    xc, yc = np.concatenate(tbl.x_ctrl.values), np.concatenate(tbl.y_ctrl.values)
    xs, ys = np.concatenate(tbl.x_stim.values), np.concatenate(tbl.y_stim.values)
    bc, pc_, nc = logit(xc, yc)
    bs, ps_, ns = logit(xs, ys)
    print(f"{lab}: held-out control trials, slope {bc:.2f} (p = {pc_:.2g}, {nc} trials); photostimulation trials, slope {bs:.2f} "
          f"(p = {ps_:.2g}, {ns} trials)")
    bins = np.array([-np.inf, -0.5, 0, 0.5, np.inf])
    print("   P(lick right) by projection bin (<-0.5, -0.5..0, 0..0.5, >0.5): control",
          [round(float(yc[(xc >= a) & (xc < b)].mean()), 2) if ((xc >= a) & (xc < b)).sum() else None for a, b in zip(bins[:-1], bins[1:])],
          "photostim", [round(float(ys[(xs >= a) & (xs < b)].mean()), 2) if ((xs >= a) & (xs < b)).sum() else None for a, b in zip(bins[:-1], bins[1:])])
print("Expected FN trial count 337 +/- 33.7")

# %% [markdown]
# RESULT ed10d-fn-no-prediction
E
cd entries/000007-gao-2018; . $TMPDIR/explore/bin/activate; python $TMPDIR/dev/build.py $TMPDIR/dev/nb_main.py $TMPDIR/dev/run.py && time PYTHONPATH=. MPLBACKEND=Agg python $TMPDIR/dev/run.py 2>&1 | grep -v Warn | sed -n '/claim:fig3-alm-latency-pi/,$p'
```

```
######## CELL ['claim:fig3-alm-latency-pi']
(a) code 6: 234 neurons; onset 7.8 +/- 14.3 ms (bootstrap s.d. over neurons); resamples without an onset in the window: 0
   expected 7.1 +/- 3.8 ms; within: True
   population change (spikes/s) at bin centres -10, 0, 5, 10, 15, 20, 30 ms: [0.21, 0.75, 0.7, 0.8, 0.7, 0.08, 0.39]
(b) codes 5 and 6: 298 neurons; onset 16.7 +/- 12.9 ms (bootstrap s.d. over neurons); resamples without an onset in the window: 0
   expected 7.1 +/- 3.8 ms; within: False
   population change (spikes/s) at bin centres -10, 0, 5, 10, 15, 20, 30 ms: [-0.08, 0.24, 0.48, 0.36, 0.16, -0.01, 1.06]
(a) code 6: sustained onset 30.6 +/- 14.2 ms; change in 10 ms bins at -50 to +100 ms (5 ms steps):
    [0.2, 0.5, 0.9, 0.8, 0.2, -0.2, -0.1, 0.2, 0.2, 0.4, 0.7, 0.7, 0.8, 0.7, 0.1, 0.1, 0.4, 0.9, 2.2, 3.3, 3.9, 4.8, 4.4, 3.1, 3.4, 3.8, 4.4, 4.8, 4.1, 4.1, 4.6]
(b) codes 5 and 6: sustained onset 29.2 +/- 4.9 ms; change in 10 ms bins at -50 to +100 ms (5 ms steps):
    [-0.1, 0.5, 0.7, 0.3, 0.2, -0.0, -0.2, -0.0, -0.1, -0.2, 0.2, 0.5, 0.4, 0.2, -0.0, 0.2, 1.1, 1.6, 2.5, 3.4, 3.9, 4.3, 4.1, 3.5, 3.8, 4.2, 4.2, 4.2, 4.2, 4.2, 4.2]
code 5 alone: sustained onset 32.4 +/- 4.8 ms; change in 10 ms bins at -50 to +100 ms (5 ms steps):
    [-0.3, 0.4, 0.8, 0.3, 0.2, 0.1, -0.1, 0.0, -0.1, -0.2, 0.5, 0.9, 0.0, -0.4, 0.1, 0.3, 0.9, 2.0, 3.3, 4.1, 4.7, 4.6, 3.9, 3.5, 4.4, 4.7, 4.0, 4.0, 4.1, 3.8, 4.4]

######## CELL ['claim:fig3f-alm-selectivity-abolished']
Code 6 (1.3 s): 252 neurons; delay selectivity control 2.04, photostim 0.48 spikes/s; ratio 0.23; one-tailed bootstrap p (photostim not lower) = 0.0000; 95% interval of photostim selectivity [0.21, 0.76]
By mouse:
            ctrl       stim     
            mean size  mean size
subject                         
[... 96 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/000007-gao-2018; . $TMPDIR/explore/bin/activate; python - <<'E' 2>&1 | grep -v Warn
import pickle,numpy as np,pandas as pd,gao2018
sessions=pickle.load(open('/tmp/claude-1001/S.pkl','rb'))
for s in sessions:
    if s['group'] not in ('FN','DN'): continue
    tr=s['trials']; base=(tr.lick_early==0).values & tr.outcome.isin(['hit','error']).values
    code=2 if s['group']=='FN' else 4
    pyr=[i for i in range(len(s['spikes'])) if s['cell_type'][i]=='pyramidal']
    stab={i: gao2018.stable_trials(s['spikes'][i],tr)&base for i in pyr}
    fr=[stab[i].sum()/base.sum() for i in pyr]
    keep=[i for i in pyr if stab[i].sum()>=0.5*base.sum()]
    ok=np.logical_and.reduce([stab[i] for i in keep]) if keep else base
    t=tr[ok]; R=t.trial_type.values=='R'; L=~R
    n=[((t.stim.values==code)&R).sum(),((t.stim.values==code)&L).sum()]
    nb=[((tr.stim.values==code)&(tr.trial_type.values=='R')&base).sum(),((tr.stim.values==code)&(tr.trial_type.values=='L')&base).sum()]
    print(s['subject'],s['session'],len(pyr),len(keep),base.sum(),ok.sum(),n,nb, np.round(np.percentile(fr,[10,50,90]),2))
E
```

```
BAYLORCD6 20170610T135720 62 54 271 32 [np.int64(4), np.int64(1)] [np.int64(13), np.int64(16)] [0.33 0.86 1.  ]
BAYLORCD6 20170611T140007 59 42 50 28 [np.int64(0), np.int64(2)] [np.int64(1), np.int64(2)] [0.   0.98 1.  ]
BAYLORCD6 20170612T125622 30 30 206 29 [np.int64(2), np.int64(3)] [np.int64(5), np.int64(14)] [0.72 1.   1.  ]
BAYLORCD6 20170614T111143 36 20 284 21 [np.int64(1), np.int64(1)] [np.int64(7), np.int64(16)] [0.29 0.52 0.85]
BAYLORNL12 20170610T122530 59 57 357 47 [np.int64(0), np.int64(4)] [np.int64(15), np.int64(26)] [0.62 0.98 1.  ]
BAYLORNL12 20170611T124136 57 40 347 29 [np.int64(3), np.int64(1)] [np.int64(25), np.int64(13)] [0.34 0.63 1.  ]
BAYLORNL12 20170612T115219 44 39 388 103 [np.int64(5), np.int64(5)] [np.int64(20), np.int64(29)] [0.5  0.97 1.  ]
BAYLORNL12 20170613T123812 38 28 407 29 [np.int64(0), np.int64(0)] [np.int64(26), np.int64(22)] [0.45 0.66 1.  ]
BAYLORNL12 20170614T094441 33 29 322 67 [np.int64(5), np.int64(2)] [np.int64(15), np.int64(23)] [0.45 0.9  1.  ]
BAYLORNL14 20170602T114550 47 41 472 93 [np.int64(7), np.int64(2)] [np.int64(33), np.int64(23)] [0.48 0.9  1.  ]
BAYLORNL14 20170603T153540 66 59 423 13 [np.int64(0), np.int64(0)] [np.int64(15), np.int64(31)] [0.49 0.8  1.  ]
BAYLORNL14 20170604T150059 60 55 398 82 [np.int64(4), np.int64(3)] [np.int64(23), np.int64(29)] [0.62 1.   1.  ]
BAYLORNL14 20170605T123139 54 49 314 56 [np.int64(4), np.int64(2)] [np.int64(15), np.int64(23)] [0.54 0.94 1.  ]
BAYLORNL14 20170606T094050 35 31 336 110 [np.int64(10), np.int64(6)] [np.int64(25), np.int64(25)] [0.49 0.87 1.  ]
BAYLORNL14 20170607T130355 26 22 306 34 [np.int64(4), np.int64(3)] [np.int64(20), np.int64(23)] [0.48 0.83 1.  ]
BAYLORNL15 20170602T095359 28 2 257 173 [np.int64(6), np.int64(10)] [np.int64(8), np.int64(19)] [0.24 0.34 0.4 ]
BAYLORNL15 20170603T122807 45 38 372 35 [np.int64(0), np.int64(0)] [np.int64(12), np.int64(19)] [0.46 0.84 1.  ]
BAYLORNL15 20170604T121032 25 22 248 31 [np.int64(1), np.int64(1)] [np.int64(4), np.i
[... 16 more lines not kept]
```

**Agent calls Bash**

```bash
python3 - <<'E'
p='/tmp/claude-1001/dev/nb_main.py'; s=open(p).read()
# cd: drop stability
old='''# Neurons are those whose stable trials cover at least half of the session's usable trials, and
# trials are those stable for all of them (a choice made here).'''
new='''# All pyramidal neurons of a session and all its usable trials (correct or error, no early lick)
# are used; the stable-trial rule is not applied here, since requiring every trial to be stable
# for every neuron leaves too few trials (a choice made here).'''
assert old in s; s=s.replace(old,new)
old='''        pyr = [i for i in range(len(s["spikes"])) if s["cell_type"][i] == "pyramidal"]
        stab = {i: gao2018.stable_trials(s["spikes"][i], tr) & base for i in pyr}
        keep_u = [i for i in pyr if stab[i].sum() >= 0.5 * base.sum()]
        if not keep_u:
            continue
        ok = np.logical_and.reduce([stab[i] for i in keep_u])
        t = tr[ok]'''
new='''        keep_u = [i for i in range(len(s["spikes"])) if s["cell_type"][i] == "pyramidal"]
        t = tr[base]'''
assert old in s; s=s.replace(old,new)
# latency: extended centres and baseline-subtracted variant
old='''lat_centres = np.round(np.arange(-0.015, 0.1 + 1e-9, 0.001), 4)'''
new='''lat_centres = np.round(np.arange(-0.015, 0.1 + 1e-9, 0.001), 4)      # bins from 20 ms before onset
pre_centres = np.round(np.arange(-0.2, -0.02 + 1e-9, 0.001), 4)       # for the baseline-subtracted variant'''
assert old in s; s=s.replace(old,new)
old='''        mean10, sd10, _ = gao2018.onset_latency(ch, lat_centres, rng, n_boot=2000, run=10)
        out[r] = (int(sig.sum()), mean, sd)
        print(f"{label} {r}: {int(sig.sum())} of {int(m.p.notna().sum())} neurons modulated; onset {mean * 1000:.1f} +/- "
              f"{sd * 1000:.1f} ms; resampled onsets before 0 ms: {float((onsets < 0).mean()):.3f}; "
              f"variant, sustained onset {mean10 * 1000:.1f} +/- {sd10 * 1000:.1f} ms")'''
new='''        mean10, sd10, _ = gao2018.onset_latency(ch, lat_centres, rng, n_boot=2000, run=10)
        _, pre_curves = act_modulation_and_change([u for u, k in zip(units_, sig) if k], codes_onsets, pre_centres)
        pre = (pre_curves * np.sign(m["diff"].values[sig])[:, None]).mean(1, keepdims=True)
        mean_b, sd_b, _ = gao2018.onset_latency(ch - pre, lat_centres, rng, n_boot=2000)
        out[r] = (int(sig.sum()), mean, sd)
        print(f"{label} {r}: {int(sig.sum())} of {int(m.p.notna().sum())} neurons modulated; onset {mean * 1000:.1f} +/- "
              f"{sd * 1000:.1f} ms; resampled onsets before 0 ms: {float((onsets < 0).mean()):.3f}")
        print(f"    variants: sustained onset {mean10 * 1000:.1f} +/- {sd10 * 1000:.1f} ms; with each neuron's change in the 200 to "
              f"20 ms before onset subtracted, onset {mean_b * 1000:.1f} +/- {sd_b * 1000:.1f} ms (pre-onset change "
              f"{float(pre.mean()):.2f} spikes/s)")'''
assert old in s; s=s.replace(old,new)
old='''    mean, sd, onsets = gao2018.onset_latency(ch, lat_centres, rng)
    lat_results[r] = (mean, sd)
    print(f"{r}: {len(units_sig)} neurons; onset {mean * 1000:.1f} +/- {sd * 1000:.1f} ms (bootstrap s.d. over neurons); "
          f"resamples without an onset in the window: {int(np.isnan(onsets).sum())}")'''
new='''    mean, sd, onsets = gao2018.onset_latency(ch, lat_centres, rng)
    lat_results[r] = (mean, sd)
    pre = change_curves(units_sig, codes, "pole_out_time", np.sign(m["diff"].values[sig]), pre_centres).mean(1, keepdims=True)
    mean_b, sd_b, _ = gao2018.onset_latency(ch - pre, lat_centres, rng, n_boot=2000)
    print(f"{r}: {len(units_sig)} neurons; onset {mean * 1000:.1f} +/- {sd * 1000:.1f} ms (bootstrap s.d. over neurons); "
          f"resamples without an onset in the window: {int(np.isnan(onsets).sum())}; before 0 ms: {float((onsets < 0).mean()):.3f}")
    print(f"   variant, pre-onset change subtracted ({float(pre.mean()):.2f} spikes/s): onset {mean_b * 1000:.1f} +/- {sd_b * 1000:.1f} ms")'''
assert old in s; s=s.replace(old,new)
open(p,'w').write(s)
E
cd entries/000007-gao-2018; . $TMPDIR/explore/bin/activate; python $TMPDIR/dev/build.py $TMPDIR/dev/nb_main.py $TMPDIR/dev/run.py && time PYTHONPATH=. MPLBACKEND=Agg python $TMPDIR/dev/run.py 2>&1 | grep -v Warn | sed -n '/claim:fig3-alm-latency-pi/,/sustained onset 30/p;/claim:ed9a-fn-latency/,/fig4f/p;/Sessions used/,$p'
```

```
######## CELL ['claim:fig3-alm-latency-pi']
(a) code 6: 234 neurons; onset 7.8 +/- 14.3 ms (bootstrap s.d. over neurons); resamples without an onset in the window: 0; before 0 ms: 0.293
   variant, pre-onset change subtracted (0.21 spikes/s): onset 16.3 +/- 16.6 ms
   expected 7.1 +/- 3.8 ms; within: True
   population change (spikes/s) at bin centres -10, 0, 5, 10, 15, 20, 30 ms: [0.21, 0.75, 0.7, 0.8, 0.7, 0.08, 0.39]
(b) codes 5 and 6: 298 neurons; onset 16.6 +/- 12.9 ms (bootstrap s.d. over neurons); resamples without an onset in the window: 0; before 0 ms: 0.105
   variant, pre-onset change subtracted (0.04 spikes/s): onset 19.0 +/- 12.7 ms
   expected 7.1 +/- 3.8 ms; within: False
   population change (spikes/s) at bin centres -10, 0, 5, 10, 15, 20, 30 ms: [-0.08, 0.24, 0.48, 0.36, 0.16, -0.01, 1.06]
(a) code 6: sustained onset 31.1 +/- 13.7 ms; change in 10 ms bins at -50 to +100 ms (5 ms steps):
    [0.2, 0.5, 0.9, 0.8, 0.2, -0.2, -0.1, 0.2, 0.2, 0.4, 0.7, 0.7, 0.8, 0.7, 0.1, 0.1, 0.4, 0.9, 2.2, 3.3, 3.9, 4.8, 4.4, 3.1, 3.4, 3.8, 4.4, 4.8, 4.1, 4.1, 4.6]
(b) codes 5 and 6: sustained onset 29.1 +/- 5.3 ms; change in 10 ms bins at -50 to +100 ms (5 ms steps):
    [-0.1, 0.5, 0.7, 0.3, 0.2, -0.0, -0.2, -0.0, -0.1, -0.2, 0.2, 0.5, 0.4, 0.2, -0.0, 0.2, 1.1, 1.6, 2.5, 3.4, 3.9, 4.3, 4.1, 3.5, 3.8, 4.2, 4.2, 4.2, 4.2, 4.2, 4.2]
code 5 alone: sustained onset 32.4 +/- 4.6 ms; change in 10 ms bins at -50 to +100 ms (5 ms steps):
    [-0.3, 0.4, 0.8, 0.3, 0.2, 0.1, -0.1, 0.0, -0.1, -0.2, 0.5, 0.9, 0.0, -0.4, 0.1, 0.3, 0.9, 2.0, 3.3, 4.1, 4.7, 4.6, 3.9, 3.5, 4.4, 4.7, 4.0, 4.0, 4.1, 3.8, 4.4]

######## CELL ['claim:fig3f-alm-selectivity-abolished']
Code 6 (1.3 s): 252 neurons; delay selectivity control 2.04, photostim 0.48 spikes/s; ratio 0.23; one-tailed bootstrap p (photostim not lower) = 0.0000; 95% interval of photostim selectivity [0.21, 0.76]
By mouse:
            ctrl       stim     
[... 222 more lines not kept]
```

**Agent**

The 2017 and 2018 files give pole times with only two decimals. If they are rounded to 10 ms, that limits any millisecond latency claim. Checking the precision per file.

**Agent calls Bash**

```bash
cd entries/000007-gao-2018; . $TMPDIR/explore/bin/activate; python - <<'E'
import pickle,numpy as np,pandas as pd
S=pickle.load(open('/tmp/claude-1001/S.pkl','rb'))
rows=[]
for s in S:
    t=s['trials']
    for c in ['start_time','pole_in_time','pole_out_time','cue_time']:
        v=t[c].values; r=np.abs(v*100-np.round(v*100))<1e-6
        rows.append(dict(grp=s['group'],subj=s['subject'],col=c,frac10ms=r.mean()))
d=pd.DataFrame(rows); print(d.pivot_table(index=['grp','subj'],columns='col',values='frac10ms').round(2))
E
```

```
col              cue_time  pole_in_time  pole_out_time  start_time
grp subj                                                          
DN  BAYLORNL12       0.96          1.00           0.98        1.00
    BAYLORNL14       0.99          1.00           0.99        1.00
    anm00314756      0.00          0.00           0.00        1.00
FN  BAYLORCD6        0.86          1.00           0.97        1.00
    BAYLORNL15       0.94          1.00           0.99        1.00
    anm00314746      0.00          0.00           0.00        1.00
    anm00314757      0.00          0.00           0.00        0.96
    anm00314758      0.00          0.00           0.00        1.00
    anm00314760      0.00          0.00           0.00        1.00
PI  BAYLORCD12       0.90          1.00           0.95        1.00
    BAYLORCD13       0.59          0.83           0.61        0.83
    BAYLORCD14       0.97          1.00           0.99        1.00
    BAYLORCD8        0.90          1.00           0.99        1.00
```

**Agent**

The 40 sessions from the 2017 and 2018 mice give event times on a 10 ms grid; the 2015 files are precise. I'll record this as a finding and add a 2015-files-only latency variant.

**Agent calls Bash**

```bash
python3 - <<'E'
p='/tmp/claude-1001/dev/nb_main.py'; s=open(p).read()
old='''# %% [markdown]
# ## stim-code-link
'''
new='''# %% tags=["sanity"]
# Precision of the trial event times: the fraction of values that fall on a 10 ms grid, per mouse.
prec = []
for s in sessions:
    t = s["trials"]
    row = {"group": s["group"], "subject": s["subject"]}
    for c in ("pole_in_time", "pole_out_time", "cue_time"):
        v = t[c].values
        row[c] = float((np.abs(v * 100 - np.round(v * 100)) < 1e-6).mean())
    prec.append(row)
prec = pd.DataFrame(prec).groupby(["group", "subject"]).mean().round(2)
print("Fraction of event times on a 10 ms grid:")
print(prec.to_string())

# %% [markdown]
# In the files of the 2017 and 2018 mice (BAYLOR ids, 40 of 54 sessions, all four PI mice) the pole
# and cue times lie on a 10 ms grid, while in the 2015 files (anm ids) they are given to a
# microsecond. Times of the photostimulus are known only through these event times, so in the
# BAYLOR files an onset latency of a few milliseconds cannot be measured to better than about 10
# ms. The latency claims show the 2015 files apart as a variant.

# %% [markdown]
# ## stim-code-link
'''
assert old in s; s=s.replace(old,new,1)
old='''        out[r] = (int(sig.sum()), mean, sd)
        print(f"{label} {r}: {int(sig.sum())} of'''
new='''        early = np.array([u["subject"].startswith("anm") for u in units_])[sig]
        if early.sum() >= 5:
            mean_e, sd_e, _ = gao2018.onset_latency(ch[early], lat_centres, rng, n_boot=2000)
            early_txt = f"2015 files only ({int(early.sum())} neurons), onset {mean_e * 1000:.1f} +/- {sd_e * 1000:.1f} ms"
        else:
            early_txt = f"2015 files only: {int(early.sum())} modulated neurons, too few"
        out[r] = (int(sig.sum()), mean, sd)
        print(f"{label} {r}: {int(sig.sum())} of'''
assert old in s; s=s.replace(old,new)
old='''              f"{float(pre.mean()):.2f} spikes/s)")'''
new='''              f"{float(pre.mean()):.2f} spikes/s); {early_txt}")'''
assert old in s; s=s.replace(old,new)
old='''print(f"FN: separation in the last 400 ms of the delay, control {cd_fn.sep_ctrl.mean():.2f}, code 2 {cd_fn.sep_stim.mean():.2f} "
      f"(spike-count units); ratio {ratio_fn:.2f}, bootstrap 95% interval {np.percentile(boot_fn, 2.5):.2f} to {np.percentile(boot_fn, 97.5):.2f}")'''
new='''print(f"FN: separation in the last 400 ms of the delay, control {cd_fn.sep_ctrl.mean():.2f}, code 2 {cd_fn.sep_stim.mean():.2f} "
      f"(spike-count units); ratio {ratio_fn:.3f}, bootstrap 95% interval {np.percentile(boot_fn, 2.5):.3f} to {np.percentile(boot_fn, 97.5):.3f}")
print(f"Variant, the median over sessions of each session's ratio: {np.median(cd_fn.sep_stim / cd_fn.sep_ctrl):.3f}; "
      f"each session's separation scaled by its control separation, mean ratio {np.mean(cd_fn.sep_stim / cd_fn.sep_ctrl):.3f}")'''
assert old in s; s=s.replace(old,new)
old='''print(f"Fraction of paired resamples with the FN ratio below the DN ratio: {float((boot_fn < boot_dn).mean()):.4f}")'''
new='''print(f"Fraction of paired resamples with the FN ratio below the DN ratio: {float((boot_fn < boot_dn).mean()):.4f}")
print(f"Variant, the median over sessions of each session's ratio: {np.median(cd_dn.sep_stim / cd_dn.sep_ctrl):.3f}")'''
assert old in s; s=s.replace(old,new)
open(p,'w').write(s)
E
echo ok
```

```
ok
```

**Agent**

Main notebook analyses are drafted. Now prototyping the CN loader for the Zenodo NWB zip, to see whether a full fetch fits the time limit.

**Agent calls Bash**

```bash
cd $TMPDIR; . explore/bin/activate; python - <<'E' 2>&1 | grep -v Warn
exec(open('zread.py').read().split("t=time.time()")[0])
import numpy as np, pandas as pd
nl=[i for i in infos if 'BAYLORNL3_20170120' in i[0]][0]
b=read_entry(nl[0]); f=h5py.File(io.BytesIO(b),'r')
t=f['intervals/trials']
for k in t: 
    if k not in ('timeseries',): print(k, t[k].shape, t[k][:5], dict(t[k].attrs).get('description'))
ts=t['timeseries'][:5]; print(ts)
print(t['timeseries'].attrs.keys())
u=f['units']; print(u['id'][:], u['spike_times_index'][:], u['trials'][:10], u['spike_times'][:10])
for k in f['analysis']: a=f['analysis'][k]; print(k, a['control'][:], dict(a.attrs)['comments'], a['timestamps'][:3])
print(list(f['acquisition'].keys()) if 'acquisition' in f else '', list(f['stimulus/presentation'].keys()))
for k in f['stimulus/presentation']:
    o=f['stimulus/presentation'][k]; print(k, list(o.keys()), dict(o.attrs).get('description'))
    for kk in o:
        if isinstance(o[kk],h5py.Dataset): print('  ',kk,o[kk].shape)
print(f['session_start_time'][()], f['timestamps_reference_time'][()])
E
```

```
CueTime (2, 411) [[   nan    nan    nan    nan    nan    nan    nan    nan    nan    nan
     nan 3.17   3.17   3.17   3.17   3.17   3.17   3.17   3.17   3.17
  3.17   3.17   3.17   3.17   3.17   3.17   3.17   3.17   3.17   3.17
  3.17   4.5942 3.17   3.17   3.17   3.17   3.17   3.3513 3.17   3.17
  3.9626 3.17   3.17   3.17   3.17   3.17   3.17   3.17   3.17   3.17
  3.17   3.17   3.17   3.17   3.17   3.17   3.17   3.17   3.17   3.17
  3.17   3.17   3.17   4.4925 4.6789 3.17   3.17   3.17   3.17   3.17
  3.17   3.17   3.17   3.17   3.17   3.17   3.17   3.17   3.17   3.17
  3.17   3.17   3.17   3.17   3.17   4.3682 3.17   4.4534 3.17   3.17
  3.17   3.17   3.17   3.17   3.17   3.17   3.17   3.17   3.17   3.17
  3.17   3.17   3.17   3.17   3.17   3.17   3.17   3.17   3.17   3.17
  3.17   3.17   4.422  3.17   3.17   3.17   3.17   3.17   3.17   3.17
  3.17   3.17   3.17   3.17   3.17   3.17   3.17   3.17   3.17   3.17
  3.17   3.17   3.17   3.17   3.17   4.3299 3.17   3.17   3.17   3.17
  3.17   3.17   3.17   3.17   3.17   3.17   4.5107 3.17   3.17   3.17
  3.17   3.17   3.17   3.17   3.17   3.17   3.17   3.17   3.17   3.17
  3.17   3.17   3.17   3.17   3.17   3.17   3.17   3.17   3.17   3.17
  3.17   3.17   3.17   3.17   3.17   3.17   4.4391 3.17   3.17   3.17
  3.17   3.17   3.17   3.17   3.17   3.17   3.17   3.17   3.17   3.17
  3.17   3.17   3.17   3.17   3.17   3.17   3.17   3.17   3.17   3.17
[... 96 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR; . explore/bin/activate; cat > fetchtest.py <<'E'
import requests, zlib, struct, time, pickle, threading
from concurrent.futures import ThreadPoolExecutor
U="https://zenodo.org/api/records/6647629/files/datafiles_NWB.zip/content"
infos=pickle.load(open('/tmp/claude-1001/ziplist.pkl','rb'))
local=threading.local()
def sess():
    if not hasattr(local,'s'): local.s=requests.Session()
    return local.s
def get(a,b):
    for k in range(5):
        try:
            r=sess().get(U,headers={'Range':f'bytes={a}-{b}'},timeout=120); r.raise_for_status()
            if len(r.content)==b-a+1: return r.content
        except Exception as e: err=e
        time.sleep(2*(k+1))
    raise RuntimeError(f'range {a}-{b} failed')
pool=ThreadPoolExecutor(32)
CH=4<<20
def entry(info):
    fn,size,csize,ct,off=info
    h=get(off,off+29); nl,el=struct.unpack('<HH',h[26:30]); start=off+30+nl+el
    futs=[pool.submit(get,a,min(a+CH,start+csize)-1) for a in range(start,start+csize,CH)]
    d=zlib.decompressobj(-15); n=0
    for f in futs: n+=len(d.decompress(f.result()))
    n+=len(d.flush()); assert n==size; return n
t=time.time(); tot=0
with ThreadPoolExecutor(4) as files:
    for i,n in enumerate(files.map(entry, sorted(infos,key=lambda i:-i[2]))):
        tot+=n
        if i%20==0: print(i, round(time.time()-t), 's', round(tot/1e9,2),'GB uncompressed', flush=True)
print('done',round(time.time()-t),'s')
E
timeout 3000 python fetchtest.py
```

```
Exit code 1
Traceback (most recent call last):
  File "/tmp/claude-1001/fetchtest.py", line 28, in <module>
    for i,n in enumerate(files.map(entry, sorted(infos,key=lambda i:-i[2]))):
               ~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.13.16/x64/lib/python3.13/concurrent/futures/_base.py", line 625, in result_iterator
    yield _result_or_cancel(fs.pop())
          ~~~~~~~~~~~~~~~~~^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.13.16/x64/lib/python3.13/concurrent/futures/_base.py", line 318, in _result_or_cancel
    return fut.result(timeout)
           ~~~~~~~~~~^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.13.16/x64/lib/python3.13/concurrent/futures/_base.py", line 460, in result
    return self.__get_result()
           ~~~~~~~~~~~~~~~~~^^
  File "/opt/hostedtoolcache/Python/3.13.16/x64/lib/python3.13/concurrent/futures/_base.py", line 402, in __get_result
    raise self._exception
  File "/opt/hostedtoolcache/Python/3.13.16/x64/lib/python3.13/concurrent/futures/thread.py", line 59, in run
    result = self.fn(*self.args, **self.kwargs)
  File "/tmp/claude-1001/fetchtest.py", line 24, in entry
    for f in futs: n+=len(d.decompress(f.result()))
[... 11 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR; . explore/bin/activate; python - <<'E'
import requests
U="https://zenodo.org/api/records/6647629/files/datafiles_NWB.zip/content"
r=requests.get(U,headers={'Range':'bytes=2707650452-2707650999'},timeout=60); print(r.status_code, r.headers.get('Retry-After'), r.headers.get('X-RateLimit-Limit'), r.headers.get('X-RateLimit-Remaining'), r.headers.get('X-RateLimit-Reset'), r.text[:300] if r.status_code!=206 else len(r.content))
E
```

```
206 0 133 91 1792414042 548
Shell cwd was reset to
```

**Agent**

Zenodo limits clients to 133 requests per minute, so 4 MB chunks hit the limit. Retrying with 32 MB chunks and rate-limit handling.

**Agent calls Bash**

```bash
cd $TMPDIR; . explore/bin/activate; python - <<'E'
s=open('fetchtest.py').read()
s=s.replace("""            r=sess().get(U,headers={'Range':f'bytes={a}-{b}'},timeout=120); r.raise_for_status()""","""            r=sess().get(U,headers={'Range':f'bytes={a}-{b}'},timeout=600)
            if r.status_code==429:
                time.sleep(max(5,float(r.headers.get('Retry-After') or 30))); continue
            r.raise_for_status()""")
s=s.replace("CH=4<<20","CH=32<<20").replace("for k in range(5)","for k in range(8)")
open('fetchtest.py','w').write(s)
E
timeout 3300 python fetchtest.py
```

```
0 60 s 0.52 GB uncompressed
20 206 s 7.57 GB uncompressed
40 339 s 12.25 GB uncompressed
60 420 s 15.44 GB uncompressed
80 505 s 17.96 GB uncompressed
100 575 s 19.88 GB uncompressed
120 658 s 21.23 GB uncompressed
140 715 s 22.24 GB uncompressed
160 755 s 22.82 GB uncompressed
180 773 s 23.05 GB uncompressed
done 775 s
Shell cwd was reset to
```

**Agent**

A full fetch of the CN zip takes 13 min here, so the CN claims can be tested within the 30 min limit. Writing the CN helper.

**Agent calls Write**

```json
{
 "file_path": "entries/000007-gao-2018/gao2018_cn.py",
 "content": "\"\"\"The CN recordings of Gao et al. (2018), streamed from Zenodo, for the claims the dandiset cannot test.\n\nDandiset 000007 holds only the ALM recordings. The paper's CN recordings (185 sessions, 18 mice,\nby the record's description) are deposited as NWB files in one zip archive on Zenodo,\ndoi:10.5281/zenodo.6647629 (`datafiles_NWB.zip`, 11.9 GB). Zenodo answers HTTP range requests,\nso each file is read from the archive's central directory, its compressed bytes are fetched in\n32 MB ranges over parallel connections, inflated in memory, and opened with h5py from memory.\nNothing is written to disk. Zenodo allows 133 requests a minute; the large ranges keep the run\nto a few hundred requests.\n\nWhat is read from each file, and how, follows the paper's CN scripts (`analyses_scripts.zip` in\nthe MATLAB record doi:10.5281/zenodo.6653158, `analysis_compile_all_DCN_data.m` and\n`analysis_compiled_all_DCN_ALMsilencing_selectivity.m`):\n\n- trials: start time (session clock), pole in, pole out and cue times relative to the trial\n  start, the outcome flags (HitR, HitL, ErrR, ErrL, NoLickR, NoLickL, LickEarly), `GoodTrials`\n  and `PhotostimulationType` (0 control; 7, 8, 9, 10 left, right, bilateral ALM and bilateral M1\n  photo-inhibition in the delay, by the column's description);\n- units: spike times (session clock), and each unit's location from the `cellType` comment of\n  its SpikeEventSeries (fastigial, interposed, dentate or outside the CN);\n- the scripts' trial selection (correct or error by instructed type, no early lick, performing\n  trials, the unit's stable trials) and epochs (sample, delay, response of 1.3 s after the cue).\n\"\"\"\n\nfrom __future__ import annotations\n\nimport io\nimport re\nimport struct\nimport threading\nimport time\nimport zipfile\nimport zlib\nfrom concurrent.futures import ThreadPoolExecutor\n\nimport h5py\nimport numpy as np\nimport pandas as pd\nimport requests\n\nZENODO_RECORD = \"6647629\"\nZENODO_DOI = \"10.5281/zenodo.6647629\"\nZIP_URL = f\"https://zenodo.org/api/records/{ZENODO_RECORD}/files/datafiles_NWB.zip/content\"\nCHUNK = 32 << 20\nCONNECTIONS = 32\nRESPONSE_S = 1.3\nLOCATIONS = {\"Fastigial unit\": \"FN\", \"Interposed unit\": \"IP\", \"Dentate unit\": \"DN\", \"Outside DCN unit\": \"outside\"}\n\n_local = threading.local()\n\n\ndef _session():\n    if not hasattr(_local, \"s\"):\n        _local.s = requests.Session()\n    return _local.s\n\n\ndef get_range(a: int, b: int, attempts: int = 8) -> bytes:\n    \"\"\"Bytes a to b (inclusive) of the archive, waiting out the rate limit.\"\"\"\n    for k in range(attempts):\n        try:\n            r = _session().get(ZIP_URL, headers={\"Range\": f\"bytes={a}-{b}\"}, timeout=600)\n            if r.status_code == 429:\n                time.sleep(max(5.0, float(r.headers.get(\"Retry-After\") or 30)))\n                continue\n            r.raise_for_status()\n            if len(r.content) == b - a + 1:\n                return r.content\n        except requests.RequestException:\n            pass\n        time.sleep(2 * (k + 1))\n    raise RuntimeError(f\"could not fetch bytes {a}-{b} of {ZIP_URL}\")\n\n\nclass _RangeFile(io.RawIOBase):\n    def __init__(self, size):\n        self.size, self.pos = size, 0\n\n    def seekable(self):\n        return True\n\n    def readable(self):\n        return True\n\n    def seek(self, offset, whence=0):\n        self.pos = offset if whence == 0 else (self.pos + offset if whence == 1 else self.size + offset)\n        return self.pos\n\n    def tell(self):\n        return self.pos\n\n    def readinto(self, b):\n        if self.pos >= self.size:\n            return 0\n        end = min(self.pos + len(b), self.size) - 1\n        d = get_range(self.pos, end)\n        b[:len(d)] = d\n        self.pos += len(d)\n        return len(d)\n\n\ndef archive_entries() -> list[zipfile.ZipInfo]:\n    size = int(requests.head(ZIP_URL, allow_redirects=True, timeout=60).headers[\"Content-Length\"])\n    z = zipfile.ZipFile(io.BufferedReader(_RangeFile(size), buffer_size=1 << 20))\n    return [i for i in z.infolist() if i.filename.endswith(\".nwb\")]\n\n\ndef read_entry(info: zipfile.ZipInfo, pool: ThreadPoolExecutor) -> bytes:\n    head = get_range(info.header_offset, info.header_offset + 29)\n    name_len, extra_len = struct.unpack(\"<HH\", head[26:30])\n    start = info.header_offset + 30 + name_len + extra_len\n    parts = [pool.submit(get_range, a, min(a + CHUNK, start + info.compress_size) - 1)\n             for a in range(start, start + info.compress_size, CHUNK)]\n    inflate = zlib.decompressobj(-15)\n    out = [inflate.decompress(p.result()) for p in parts]\n    out.append(inflate.flush())\n    data = b\"\".join(out)\n    if len(data) != info.file_size or zlib.crc32(data) != info.CRC:\n        raise RuntimeError(f\"{info.filename} did not inflate to its stated size and checksum\")\n    return data\n\n\ndef _vec(t, name):\n    x = t[name][:]\n    if x.ndim == 2:          # CueTime is stored as two rows; the second has a value for every trial\n        x = x[-1]\n    return x\n\n\ndef parse_session(name: str, data: bytes) -> dict:\n    f = h5py.File(io.BytesIO(data), \"r\")\n    t = f[\"intervals/trials\"]\n    cols = [\"HitR\", \"HitL\", \"ErrR\", \"ErrL\", \"NoLickR\", \"NoLickL\", \"LickEarly\"]\n    trials = pd.DataFrame({c: _vec(t, c) for c in cols})\n    trials[\"start\"] = t[\"start_time\"][:]\n    trials[\"pole_in\"] = _vec(t, \"PoleInTime\")\n    trials[\"pole_out\"] = _vec(t, \"PoleOutTime\")\n    trials[\"cue\"] = _vec(t, \"CueTime\")\n    trials[\"good\"] = t[\"GoodTrials\"][:] if \"GoodTrials\" in t else 1\n    trials[\"stim\"] = _vec(t, \"PhotostimulationType\") if \"PhotostimulationType\" in t else 0.0\n    trials[\"trial_id\"] = t[\"id\"][:]\n    trials[\"trial_type\"] = np.select([(trials.HitR + trials.ErrR + trials.NoLickR) > 0,\n                                      (trials.HitL + trials.ErrL + trials.NoLickL) > 0], [\"R\", \"L\"], None)\n    trials[\"outcome\"] = np.select([(trials.HitR + trials.HitL) > 0, (trials.ErrR + trials.ErrL) > 0], [\"hit\", \"error\"], \"nolick\")\n    u = f[\"units\"]\n    st, idx = u[\"spike_times\"][:], u[\"spike_times_index\"][:].astype(int)\n    ids = u[\"id\"][:]\n    loc = {}\n    for k in f[\"analysis\"]:\n        a = f[\"analysis\"][k]\n        m = re.search(r\"cellType:\\s*(.+)\", str(a.attrs.get(\"comments\", \"\")))\n        loc[int(a[\"control\"][0])] = LOCATIONS.get(m.group(1).strip(), m.group(1).strip()) if m else None\n    tr_of_spike = u[\"trials\"][:]\n    spikes, spike_trials = np.split(st, idx[:-1]), np.split(tr_of_spike, idx[:-1])\n    order = [np.argsort(s, kind=\"stable\") for s in spikes]\n    mouse = re.search(r\"/([A-Za-z]+\\d+)_\", name).group(1)\n    f.close()\n    return {\"file\": name.split(\"/\")[-1], \"mouse\": mouse, \"trials\": trials,\n            \"spikes\": [s[o] for s, o in zip(spikes, order)],\n            \"spike_trials\": [s[o] for s, o in zip(spike_trials, order)],\n            \"location\": [loc.get(int(i)) for i in ids], \"unit_ids\": ids.tolist(),\n            \"nbytes\": len(data)}\n\n\ndef load_all(entries=None, files_in_parallel: int = 4) -> tuple[list[dict], dict]:\n    \"\"\"Every CN session of the archive, and timing of the fetch.\"\"\"\n    started = time.time()\n    entries = entries if entries is not None else archive_entries()\n    pool = ThreadPoolExecutor(CONNECTIONS)\n\n    def one(info):\n        return parse_session(info.filename, read_entry(info, pool))\n\n    with ThreadPoolExecutor(files_in_parallel) as ex:\n        out = list(ex.map(one, sorted(entries, key=lambda i: -i.compress_size)))\n    pool.shutdown()\n    timing = {\"seconds\": time.time() - started, \"compressed_bytes\": sum(i.compress_size for i in entries),\n              \"files\": len(entries)}\n    return sorted(out, key=lambda s: s[\"file\"]), timing\n\n\n# --- trial selection and measures, as in the paper's CN scripts ---------------------------------\n\ndef usable(s: dict) -> pd.Series:\n    t = s[\"trials\"]\n    return (t.good == 1) & (t.LickEarly == 0) & t.pole_in.notna() & t.cue.notna()\n\n\ndef stable(s: dict, i: int) -> np.ndarray:\n    \"\"\"Trials from the first to the last trial in which unit i fired (the scripts' rule).\"\"\"\n    tr = s[\"spike_trials\"][i]\n    ids = s[\"trials\"].trial_id.values\n    if len(tr) == 0:\n        return np.zeros(len(ids), bool)\n    return (ids >= np.nanmin(tr)) & (ids <= min(np.nanmax(tr), ids.max()))\n\n\ndef epoch_rates(s: dict, i: int) -> pd.DataFrame:\n    \"\"\"Spike rates in the sample, delay and response epochs of every trial.\"\"\"\n    t, sp = s[\"trials\"], s[\"spikes\"][i]\n    bounds = {\"sample\": (t.pole_in, t.pole_out), \"delay\": (t.pole_out, t.cue), \"response\": (t.cue, t.cue + RESPONSE_S)}\n    out = {}\n    for k, (a, b) in bounds.items():\n        a_abs, b_abs = (t.start + a).values, (t.start + b).values\n        n = np.searchsorted(sp, b_abs) - np.searchsorted(sp, a_abs)\n        out[k] = n / (b - a).values\n    return pd.DataFrame(out, index=t.index)\n\n\ndef window_counts(s: dict, i: int, col: str, offsets, width: float) -> np.ndarray:\n    \"\"\"Counts in windows of `width` centred at `offsets` from trial event `col`, trials x windows.\"\"\"\n    t, sp = s[\"trials\"], s[\"spikes\"][i]\n    t0 = (t.start + t[col]).values[:, None] + np.asarray(offsets)[None, :] - width / 2\n    return (np.searchsorted(sp, t0 + width) - np.searchsorted(sp, t0)).astype(float)\n"
}
```

```
File created successfully at: entries/000007-gao-2018/gao2018_cn.py (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd entries/000007-gao-2018; . $TMPDIR/explore/bin/activate; python - <<'E' 2>&1 | grep -v Warn
import gao2018_cn as cn, time, numpy as np, pandas as pd, collections
t=time.time(); E=cn.archive_entries(); print(len(E), time.time()-t)
small=sorted(E,key=lambda i:i.compress_size)
pick=[small[0], small[1]]+[i for i in small if 'BAYLORNL4_' in i.filename][:1]+[i for i in small if 'ANM344652' in i.filename][:1]
S,tm=cn.load_all(pick); print(tm)
for s in S:
    t=s['trials']; print(s['file'], s['mouse'], len(t), collections.Counter(s['location']), t.stim.value_counts(dropna=False).to_dict(), t.good.sum(), t.trial_type.value_counts().to_dict(), t.outcome.value_counts().to_dict())
    print(t[['start','pole_in','pole_out','cue']].describe().round(3).loc[['min','50%','max']])
    print([ (len(sp), sp[:2].round(2).tolist(), np.all(np.diff(sp)>=0)) for sp in s['spikes']][:3], s['trials'].start.iloc[[0,-1]].tolist())
E
```

```
185 2.04702091217041
{'seconds': 11.9307541847229, 'compressed_bytes': 24564027, 'files': 4}
ANM344652_20160727.nwb ANM344652 106 Counter({'outside': 2}) {0.0: 106} 66 {'L': 40, 'R': 26} {'hit': 59, 'nolick': 40, 'error': 7}
        start  pole_in  pole_out    cue
min     2.402    0.572     1.872  3.572
50%  2828.709    0.572     1.872  3.573
max  3355.027    0.573     1.873  3.574
[(3894, [2480.41, 2480.47], np.True_), (1909, [2353.69, 2353.69], np.True_)] [2.401766, 3355.027022]
BAYLORNL1_20161121.nwb BAYLORNL1 304 Counter({'outside': 1}) {0.0: 304} 40 {'L': 160, 'R': 144} {'hit': 213, 'error': 91}
        start  pole_in  pole_out   cue
min  1379.100     0.57     1.870  3.17
50%  2927.074     0.57     1.870  3.17
max  4436.207     0.57     2.238  9.40
[(1334, [1397.89, 1397.97], np.True_)] [1379.1, 4436.207]
BAYLORNL2_20161115.nwb BAYLORNL2 96 Counter({'outside': 1}) {0.0: 96} 40 {'R': 66, 'L': 30} {'hit': 52, 'error': 44}
        start  pole_in  pole_out    cue
min  5427.575     0.57     1.870  3.170
50%  5916.093     0.57     1.870  3.170
max  6408.231     0.57     2.194  6.127
[(3941, [5440.34, 5441.83], np.True_)] [5427.575, 6408.231]
[... 6 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/000007-gao-2018; . $TMPDIR/explore/bin/activate; python - <<'E' 2>&1 | grep -v Warn
import gao2018_cn as cn, pickle
S,tm=cn.load_all(); print(tm, len(S))
pickle.dump((S,tm),open('/tmp/claude-1001/CN.pkl','wb'))
E
ls -la $TMPDIR/CN.pkl
```

```
{'seconds': 732.6675255298615, 'compressed_bytes': 11886154511, 'files': 185} 185
-rw-r--r-- 1 runner runner 1369915477 Oct 19 13:13 /tmp/claude-1001/CN.pkl
```

**Agent**

All 185 CN sessions streamed in 12 min. Writing the CN notebook.

**Agent calls Write**

```json
{
 "file_path": "/tmp/claude-1001/dev/nb_cn.py",
 "content": "# %% [markdown]\n# HEADER_CN\n\n# %%\nimport time\nimport warnings\n\nimport matplotlib.pyplot as plt\nimport numpy as np\nimport pandas as pd\nfrom scipy import stats\n\nimport gao2018\nimport gao2018_cn as cn\n\npd.set_option(\"display.width\", 220)\npd.set_option(\"display.max_columns\", 40)\npd.set_option(\"display.max_rows\", 200)\nwarnings.filterwarnings(\"ignore\", category=RuntimeWarning)\n\nstarted = time.time()\nentries = cn.archive_entries()\nprint(f\"Zenodo record {cn.ZENODO_DOI}: {len(entries)} NWB files, {sum(e.compress_size for e in entries) / 1e9:.2f} GB \"\n      f\"compressed, {sum(e.file_size for e in entries) / 1e9:.2f} GB inflated\")\ncn_sessions, timing = cn.load_all(entries)\nprint(f\"streamed and parsed {timing['files']} files in {timing['seconds'] / 60:.1f} min \"\n      f\"({timing['compressed_bytes'] / timing['seconds'] / 1e6:.1f} MB/s over {cn.CONNECTIONS} connections)\")\n\n# %% [markdown]\n# ## Data check\n#\n# Each check of the record's description against the values is stated under its output.\n\n# %% tags=[\"sanity\"]\nunits = pd.DataFrame([{\"file\": s[\"file\"], \"mouse\": s[\"mouse\"], \"unit\": i, \"location\": loc, \"spikes\": len(sp)}\n                      for s in cn_sessions for i, (loc, sp) in enumerate(zip(s[\"location\"], s[\"spikes\"]))])\nsess = pd.DataFrame([{\"file\": s[\"file\"], \"mouse\": s[\"mouse\"], \"trials\": len(s[\"trials\"]), \"good\": int(s[\"trials\"].good.sum()),\n                      \"units\": len(s[\"spikes\"]), \"codes\": \" \".join(f\"{int(c)}:{n}\" for c, n in\n                                                                   s[\"trials\"].stim.value_counts(dropna=False).sort_index().items())}\n                     for s in cn_sessions])\nprint(\"Mice:\", sess.mouse.nunique(), \"; sessions:\", len(sess), \"; units:\", len(units))\nprint(\"\\nUnits by location:\", units.location.value_counts(dropna=False).to_dict())\nprint(\"\\nBy mouse:\")\nprint(units.groupby([\"mouse\", \"location\"]).size().unstack(fill_value=0).assign(sessions=sess.groupby(\"mouse\").size()).to_string())\nalltr = pd.concat([s[\"trials\"].assign(mouse=s[\"mouse\"]) for s in cn_sessions], ignore_index=True)\nprint(\"\\nTrials:\", len(alltr), \"; performing (GoodTrials = 1):\", int(alltr.good.sum()))\nprint(\"PhotostimulationType values:\", alltr.stim.value_counts(dropna=False).sort_index().to_dict())\nprint(\"Mice with ALM photo-inhibition trials (codes 7 to 10):\", sorted(alltr[alltr.stim.isin([7, 8, 9, 10])].mouse.unique()))\nprint(\"Spike times sorted after ordering:\", all(np.all(np.diff(sp) >= 0) for s in cn_sessions for sp in s[\"spikes\"]))\ng = alltr[alltr.good == 1]\nprint(\"\\nPerforming trials, epoch lengths (s): sample\", (g.pole_out - g.pole_in)[g.LickEarly == 0].round(3).agg([\"min\", \"median\", \"max\"]).tolist(),\n      \"; delay\", (g.cue - g.pole_out)[g.LickEarly == 0].round(3).agg([\"min\", \"median\", \"max\"]).tolist(),\n      \"; pole in after trial start\", g.pole_in.round(3).agg([\"min\", \"median\", \"max\"]).tolist())\n\n# %% [markdown]\n# The record holds 185 sessions from 18 mice, as its description says; the Methods give 169\n# sessions. The unit counts by location are set against the paper in fig2-cn-unit-counts. Pole in,\n# pole out and cue are relative to each trial's start, as the column descriptions say, and the\n# sample and delay epochs are 1.3 s in performing trials without early licks. ALM photo-inhibition\n# codes occur only in the 8 VGAT-ChR2 mice (BAYLORNL3 to NL11 in Supplemental Table 1).\n\n# %% tags=[\"sanity\"]\n# Duplicated recordings: identical spike trains across all units, and the two penetrations of one day.\nimport hashlib\nfrom collections import defaultdict\ndigests = defaultdict(list)\nfor s in cn_sessions:\n    for i, sp in enumerate(s[\"spikes\"]):\n        if len(sp):\n            digests[hashlib.md5(np.round(sp, 5).tobytes()).hexdigest()].append((s[\"file\"], i))\ndups = [v for v in digests.values() if len(v) > 1]\nprint(\"Groups of identical spike trains:\", len(dups), dups[:10])\nsame_day = sess[sess.file.str.contains(\"pene\")]\nprint(\"Files with several penetrations on one day:\", same_day.file.tolist())\nstarts = defaultdict(list)\nfor s in cn_sessions:\n    starts[(s[\"mouse\"], round(float(s[\"trials\"].start.iloc[0]), 2), len(s[\"trials\"]))].append(s[\"file\"])\nprint(\"Files sharing a mouse, first trial start and trial count:\", [v for v in starts.values() if len(v) > 1])\n\n# %% tags=[\"sanity\"]\n# Clock check: CN firing around pole in, lick right against lick left (correct control trials), in\n# 200 ms windows; the population difference should be near 0 before pole in and grow after it.\noffs = np.round(np.arange(-0.5, 3.9, 0.2), 2)\ndiffs = []\nfor s in cn_sessions:\n    t = s[\"trials\"]\n    ok = cn.usable(s) & (t.stim == 0) & (t.outcome == \"hit\")\n    for i, loc in enumerate(s[\"location\"]):\n        if loc in (None, \"outside\"):\n            continue\n        st = cn.stable(s, i)\n        r, l = (ok & st & (t.trial_type == \"R\")).values, (ok & st & (t.trial_type == \"L\")).values\n        if min(r.sum(), l.sum()) < 10:\n            continue\n        x = cn.window_counts(s, i, \"pole_in\", offs + 0.1, 0.2) / 0.2\n        tt = stats.ttest_ind(x[r], x[l], axis=0)\n        diffs.append(np.nan_to_num(tt.pvalue, nan=1.0) < 0.05)\ndiffs = np.array(diffs)\nprint(f\"CN units tested: {len(diffs)}; fraction with lick right and lick left differing (p < 0.05) per window, by window start:\")\nprint(pd.Series(diffs.mean(0), index=offs).round(3).to_string())\n\n# %% [markdown]\n# Before pole in the fraction of CN units distinguishing the trial types is near the 5% expected by\n# chance, and it rises through the sample and delay epochs, so the trial times and the spikes are\n# on one clock at the scale of the epochs. ALM photo-inhibition onset is checked at a finer scale in\n# fig3-cn-latency.\n\n# %% [markdown]\n# ## Selectivity of CN neurons\n#\n# The test of `analysis_compile_all_DCN_data.m`: correct control trials without early licks, in\n# performing trials and the unit's stable trials, a two-tailed t-test of lick right against lick\n# left rates in the sample, delay and response epochs.\n\n# %%\nrows = []\nfor s in cn_sessions:\n    t = s[\"trials\"]\n    base = cn.usable(s) & (t.stim == 0)\n    for i, loc in enumerate(s[\"location\"]):\n        st = cn.stable(s, i)\n        r_ = epoch_r = cn.epoch_rates(s, i)\n        R = (base & st & (t.outcome == \"hit\") & (t.trial_type == \"R\")).values\n        L = (base & st & (t.outcome == \"hit\") & (t.trial_type == \"L\")).values\n        row = {\"file\": s[\"file\"], \"mouse\": s[\"mouse\"], \"unit\": i, \"location\": loc, \"n_R\": int(R.sum()), \"n_L\": int(L.sum())}\n        for e in (\"sample\", \"delay\", \"response\"):\n            row[f\"p_{e}\"] = stats.ttest_ind(r_[e].values[R], r_[e].values[L]).pvalue if min(R.sum(), L.sum()) >= 2 else np.nan\n        rows.append(row)\ncn_sel = pd.DataFrame(rows)\nfor e in (\"sample\", \"delay\", \"response\"):\n    cn_sel[f\"sig_{e}\"] = cn_sel[f\"p_{e}\"] < 0.05\ncn_sel[\"selective\"] = cn_sel[[\"sig_sample\", \"sig_delay\", \"sig_response\"]].any(axis=1)\ncn_sel[\"preparatory\"] = cn_sel[[\"sig_sample\", \"sig_delay\"]].any(axis=1)\nin_cn = cn_sel.location.isin([\"FN\", \"IP\", \"DN\"])\nprint(\"CN units:\", int(in_cn.sum()), \"; untested in some epoch:\", int(cn_sel[in_cn][[\"p_sample\", \"p_delay\", \"p_response\"]].isna().any(axis=1).sum()))\nprint(cn_sel[in_cn].groupby(\"location\")[[\"selective\", \"preparatory\", \"sig_response\"]].mean().round(3)\n      .assign(units=cn_sel[in_cn].groupby(\"location\").size()).to_string())\n\n# %% [markdown]\n# ## fig2-cn-unit-counts\n#\n# > 878 CN-region single units were recorded in 18 mice across 169 sessions, 314 from outside the\n# > CN, 268 in the fastigial, 139 in the interposed and 157 in the dentate nucleus.\n\n# %% tags=[\"claim:fig2-cn-unit-counts\"]\ncnt = pd.DataFrame({\"expected\": [878, 314, 268, 139, 157, 169],\n                    \"measured\": [len(units), int((units.location == \"outside\").sum()), int((units.location == \"FN\").sum()),\n                                 int((units.location == \"IP\").sum()), int((units.location == \"DN\").sum()), len(sess)]},\n                   index=[\"single units\", \"outside the CN\", \"fastigial\", \"interposed\", \"dentate\", \"sessions\"])\ncnt[\"tolerance\"] = (cnt.expected * 0.1).round(1)\ncnt[\"within\"] = (cnt.measured - cnt.expected).abs() <= cnt.tolerance\nprint(cnt.to_string())\nprint(\"Within tolerance:\", int(cnt.within.sum()), \"of\", len(cnt), \"; units in the CN:\", int(in_cn.sum()), \"(Results: 564)\")\nprint(\"Sessions with no units:\", int((sess.units == 0).sum()), \"; with only units outside the CN:\",\n      int(sum(all(l == \"outside\" for l in s[\"location\"]) for s in cn_sessions if s[\"location\"])))\n\n# %% [markdown]\n# RESULT fig2-cn-unit-counts\n\n# %% [markdown]\n# ## fig2-cn-selective-fraction\n#\n# > A similar proportion of CN neurons as of ALM neurons showed trial-type selectivity (416/564).\n\n# %% tags=[\"claim:fig2-cn-selective-fraction\"]\nv = cn_sel.selective[in_cn].mean()\nprint(f\"CN units selective: {int(cn_sel.selective[in_cn].sum())}/{int(in_cn.sum())} = {v:.3f} (expected 0.738 +/- 0.074; within: {abs(v - 0.738) <= 0.074})\")\nprint(\"By mouse:\", cn_sel[in_cn].groupby(\"mouse\").selective.mean().round(2).to_dict())\nrng = np.random.default_rng(601)\nnull = []\nfor s in cn_sessions:\n    t = s[\"trials\"].copy()\n    t[\"trial_type\"] = rng.permutation(t.trial_type.values)\n    sh = dict(s, trials=t)\n    base = cn.usable(sh) & (t.stim == 0)\n    for i, loc in enumerate(s[\"location\"]):\n        if loc not in (\"FN\", \"IP\", \"DN\"):\n            continue\n        st = cn.stable(sh, i)\n        r_ = cn.epoch_rates(sh, i)\n        R = (base & st & (t.outcome == \"hit\") & (t.trial_type == \"R\")).values\n        L = (base & st & (t.outcome == \"hit\") & (t.trial_type == \"L\")).values\n        if min(R.sum(), L.sum()) < 2:\n            continue\n        null.append(any(stats.ttest_ind(r_[e].values[R], r_[e].values[L]).pvalue < 0.05 for e in (\"sample\", \"delay\", \"response\")))\nprint(f\"Shuffled trial types: {np.mean(null):.3f} of CN units 'selective' (the chance level of this test)\")\n\n# %% [markdown]\n# RESULT fig2-cn-selective-fraction\n\n# %% [markdown]\n# ## fig2-cn-preparatory-fraction\n#\n# > Preparatory activity was more prevalent in ALM than in CN (59% against 35% of neurons, p <\n# > 0.001, chi-square test).\n#\n# The ALM fraction is computed here from the dandiset, as reading (a) of the main notebook (the\n# pyramidal neurons of the 9 photo-activation mice).\n\n# %% tags=[\"claim:fig2-cn-preparatory-fraction\"]\nalm_sessions = gao2018.load_all()\nalm = pd.concat([gao2018.selectivity_tests(s, unit_mask=s[\"cell_type\"] == \"pyramidal\") for s in alm_sessions\n                 if s[\"group\"] in (\"FN\", \"DN\")], ignore_index=True)\nalm_prep = int(((alm.p_sample < 0.05) | (alm.p_delay < 0.05)).sum())\ncn_prep = int(cn_sel.preparatory[in_cn].sum())\nv = cn_prep / in_cn.sum()\ntable = np.array([[alm_prep, len(alm) - alm_prep], [cn_prep, int(in_cn.sum()) - cn_prep]])\nchi2, p, _, _ = stats.chi2_contingency(table)\nprint(f\"ALM (dandiset, {gao2018.DANDISET_ID} version {gao2018.DANDISET_VERSION}): {alm_prep}/{len(alm)} = {alm_prep / len(alm):.3f}\")\nprint(f\"CN: {cn_prep}/{int(in_cn.sum())} = {v:.3f} (expected 0.35 +/- 0.035; within: {abs(v - 0.35) <= 0.035})\")\nprint(f\"chi-square = {chi2:.1f}, p = {p:.2g}; ALM higher: {alm_prep / len(alm) > v}\")\nprint(\"CN by nucleus:\", cn_sel[in_cn].groupby(\"location\").preparatory.mean().round(3).to_dict())\n\n# %% [markdown]\n# RESULT fig2-cn-preparatory-fraction\n\n# %% [markdown]\n# ## fig2-cn-perimovement-fraction\n#\n# > Peri-movement activity was equally prevalent in ALM and CN (67% against 66%).\n\n# %% tags=[\"claim:fig2-cn-perimovement-fraction\"]\nv = cn_sel.sig_response[in_cn].mean()\nalm_resp = float((alm.p_response < 0.05).mean())\nprint(f\"CN response-epoch selective: {v:.3f} (expected 0.66 +/- 0.066; within: {abs(v - 0.66) <= 0.066}); ALM (dandiset) {alm_resp:.3f}\")\nt2 = np.array([[int((alm.p_response < 0.05).sum()), int((alm.p_response >= 0.05).sum() + alm.p_response.isna().sum())],\n               [int(cn_sel.sig_response[in_cn].sum()), int((~cn_sel.sig_response[in_cn]).sum())]])\nprint(f\"chi-square ALM against CN: p = {stats.chi2_contingency(t2)[1]:.2g}\")\n\n# %% [markdown]\n# RESULT fig2-cn-perimovement-fraction\n\n# %% [markdown]\n# ## ed4e-cn-predict-movement\n#\n# > Most CN neurons with delay selectivity predicted the upcoming licking direction, switching\n# > their trial-type preference on error trials (67%, n = 73 neurons tested on more than 3 error\n# > trials).\n\n# %% tags=[\"claim:ed4e-cn-predict-movement\"]\nrows = []\nfor s in cn_sessions:\n    t = s[\"trials\"]\n    base = cn.usable(s) & (t.stim == 0)\n    sel_s = cn_sel[cn_sel.file == s[\"file\"]].set_index(\"unit\")\n    for i, loc in enumerate(s[\"location\"]):\n        if loc not in (\"FN\", \"IP\", \"DN\") or not sel_s.loc[i, \"sig_delay\"]:\n            continue\n        st = cn.stable(s, i)\n        d = cn.epoch_rates(s, i)[\"delay\"].values\n        m = lambda o, side: (base & st & (t.outcome == o) & (t.trial_type == side)).values\n        if min(m(\"error\", \"R\").sum(), m(\"error\", \"L\").sum()) <= 3:\n            continue\n        c_sel = d[m(\"hit\", \"R\")].mean() - d[m(\"hit\", \"L\")].mean()\n        e_sel = d[m(\"error\", \"R\")].mean() - d[m(\"error\", \"L\")].mean()\n        rows.append({\"mouse\": s[\"mouse\"], \"location\": loc, \"ratio\": e_sel / c_sel})\ned4e = pd.DataFrame(rows)\nv = float((ed4e.ratio < 0).mean())\nprint(f\"Delay-selective CN neurons with more than 3 error trials of each type: {len(ed4e)} (expected 73 +/- 7.3)\")\nprint(f\"Fraction with a negative error/correct ratio (predicting movement): {v:.3f} (expected 0.67 +/- 0.067; within: {abs(v - 0.67) <= 0.067})\")\nprint(\"Median ratio:\", round(float(ed4e.ratio.median()), 2), \"; by nucleus:\", ed4e.groupby(\"location\").ratio.apply(lambda r: round(float((r < 0).mean()), 2)).to_dict())\nprint(\"Variant, at least 3 error trials of each type:\")\n# (recomputed with >= 3)\n\n# %% [markdown]\n# RESULT ed4e-cn-predict-movement\n\n# %% [markdown]\n# ## ed4g-fn-contra-late-delay\n#\n# > In the fastigial nucleus, equal numbers of neurons preferred contralateral or ipsilateral\n# > movement in the early delay, and a population preference for contralateral movement developed\n# > right before movement initiation.\n\n# %% tags=[\"claim:ed4g-fn-contra-late-delay\"]\nrng = np.random.default_rng(602)\nrows = []\nfor s in cn_sessions:\n    t = s[\"trials\"]\n    base = cn.usable(s) & (t.stim == 0) & (t.outcome == \"hit\")\n    for i, loc in enumerate(s[\"location\"]):\n        if loc != \"FN\":\n            continue\n        st = cn.stable(s, i)\n        R, L = (base & st & (t.trial_type == \"R\")).values, (base & st & (t.trial_type == \"L\")).values\n        if min(R.sum(), L.sum()) < 2:\n            continue\n        early = cn.window_counts(s, i, \"pole_out\", [0.25], 0.5)[:, 0]\n        late = cn.window_counts(s, i, \"cue\", [-0.25], 0.5)[:, 0]\n        for w, x in ((\"early\", early), (\"late\", late)):\n            p = stats.ttest_ind(x[R], x[L]).pvalue\n            if p < 0.05:\n                rows.append({\"mouse\": s[\"mouse\"], \"window\": w, \"contra\": x[R].mean() > x[L].mean()})\nfn_pref = pd.DataFrame(rows)\nper_mouse = fn_pref.groupby([\"window\", \"mouse\"]).contra.mean().unstack(\"window\")\nprint(\"Significant FN neurons per window:\", fn_pref.groupby(\"window\").size().to_dict(), \"; mice:\", per_mouse.index.nunique(), \"(paper, 15)\")\nprint(\"Fraction contralateral (lick right) per mouse:\"); print(per_mouse.round(2).to_string())\nres = {}\nfor w in (\"early\", \"late\"):\n    x = per_mouse[w].dropna().values\n    boot = np.array([x[rng.integers(0, len(x), len(x))].mean() for _ in range(10000)])\n    res[w] = (x.mean(), float((boot <= 0.5).mean()), float(2 * min((boot <= 0.5).mean(), (boot >= 0.5).mean())))\n    print(f\"{w}: mean over {len(x)} mice {x.mean():.3f}; one-tailed p (not above 0.5) {res[w][1]:.4f}; two-tailed p {min(res[w][2], 1):.4f}; \"\n          f\"pooled over neurons {fn_pref[fn_pref.window == w].contra.mean():.3f}\")\n\n# %% [markdown]\n# RESULT ed4g-fn-contra-late-delay\n\n# %% [markdown]\n# ## CN during ALM photo-inhibition (Figure 3a to 3c)\n\n# %%\ndef cn_units_with(code_set):\n    out = []\n    for s in cn_sessions:\n        t = s[\"trials\"]\n        if not t.stim.isin(code_set).any():\n            continue\n        base = (cn.usable(s) & t.outcome.isin([\"hit\", \"error\"])).values\n        for i, loc in enumerate(s[\"location\"]):\n            if loc in (\"FN\", \"IP\", \"DN\"):\n                out.append({\"s\": s, \"i\": i, \"mouse\": s[\"mouse\"], \"location\": loc, \"use\": base & cn.stable(s, i)})\n    return out\n\n\nvgat_units = cn_units_with({9})\nmod = []\nfor u in vgat_units:\n    s, i, use = u[\"s\"], u[\"i\"], u[\"use\"]\n    t = s[\"trials\"]\n    d = cn.epoch_rates(s, i)[\"delay\"].values * (t.cue - t.pole_out).values\n    c, st = d[use & (t.stim.values == 0)], d[use & (t.stim.values == 9)]\n    mod.append({\"p\": stats.ttest_ind(c, st).pvalue if min(len(c), len(st)) >= 2 else np.nan,\n                \"diff\": (st.mean() - c.mean()) / 1.3 if len(st) else np.nan, \"n9\": len(st)})\nmod = pd.DataFrame(mod)\nprint(\"CN units in sessions with bilateral ALM photo-inhibition (code 9):\", len(vgat_units), \"(paper, 389)\")\nprint(\"Tested (2 or more trials in each condition):\", int(mod.p.notna().sum()))\n\n# %% [markdown]\n# ## fig3b-cn-modulated-fraction\n#\n# > Activity of many CN neurons was rapidly altered by bilateral ALM photo-inhibition (185/389, p\n# > < 0.01, two-tailed t-test).\n\n# %% tags=[\"claim:fig3b-cn-modulated-fraction\"]\nsig = mod.p < 0.01\nv = sig.sum() / mod.p.notna().sum()\nprint(f\"Modulated: {int(sig.sum())}/{int(mod.p.notna().sum())} = {v:.3f} (expected 0.476 +/- 0.048; within: {abs(v - 0.476) <= 0.048})\")\nprint(\"By nucleus:\", pd.Series(sig.values, index=[u[\"location\"] for u in vgat_units]).groupby(level=0).mean().round(3).to_dict())\nprint(\"By mouse:\", pd.Series(sig.values, index=[u[\"mouse\"] for u in vgat_units]).groupby(level=0).mean().round(3).to_dict())\nprint(\"Variant, p < 0.05:\", round(float((mod.p < 0.05).sum() / mod.p.notna().sum()), 3))\n\n# %% [markdown]\n# RESULT fig3b-cn-modulated-fraction\n\n# %% [markdown]\n# ## fig3b-cn-net-increase\n#\n# > ALM photo-inhibition caused more CN neurons to increase than to decrease their activity\n# > (123/185 increase, p < 0.001, binomial test).\n\n# %% tags=[\"claim:fig3b-cn-net-increase\"]\nup = int((mod[\"diff\"][sig] > 0).sum())\nv = up / sig.sum()\nprint(f\"Increased {up}, decreased {int(sig.sum()) - up}; fraction increased {v:.3f} (expected 0.665 +/- 0.066; within: \"\n      f\"{abs(v - 0.665) <= 0.066}); binomial p = {stats.binomtest(up, int(sig.sum())).pvalue:.2g}\")\n\n# %% [markdown]\n# RESULT fig3b-cn-net-increase\n\n# %% [markdown]\n# ## fig3-cn-latency\n#\n# > The CN response to ALM photo-inhibition had a latency of 10.7 +/- 4.0 ms (mean +/- s.e.m.).\n\n# %% tags=[\"claim:fig3-cn-latency\"]\nrng = np.random.default_rng(603)\nlat_centres = np.round(np.arange(-0.015, 0.1 + 1e-9, 0.001), 4)\ncurves = []\nfor u, k, dsign in zip(vgat_units, sig.values, np.sign(mod[\"diff\"].values)):\n    if not k:\n        continue\n    s, i, use = u[\"s\"], u[\"i\"], u[\"use\"]\n    t = s[\"trials\"]\n    x = cn.window_counts(s, i, \"pole_out\", lat_centres, 0.01) / 0.01\n    curves.append(dsign * (x[use & (t.stim.values == 9)].mean(0) - x[use & (t.stim.values == 0)].mean(0)))\ncurves = np.array(curves)\nmean, sd, onsets = gao2018.onset_latency(curves, lat_centres, rng)\nmean10, sd10, _ = gao2018.onset_latency(curves, lat_centres, rng, n_boot=2000, run=10)\nprint(f\"{len(curves)} modulated CN neurons; onset {mean * 1000:.1f} +/- {sd * 1000:.1f} ms (expected 10.7 +/- 4.0; within: \"\n      f\"{abs(mean * 1000 - 10.7) <= 4.0}); resampled onsets before 0 ms: {float((onsets < 0).mean()):.3f}\")\nprint(f\"Variant, sustained onset (10 consecutive bins): {mean10 * 1000:.1f} +/- {sd10 * 1000:.1f} ms\")\nprint(\"Population change (spikes/s) at bin centres -10, 0, 5, 10, 15, 20, 30 ms:\",\n      [round(float(curves.mean(0)[np.argmin(np.abs(lat_centres - x / 1000))]), 2) for x in (-10, 0, 5, 10, 15, 20, 30)])\nprec = float(np.mean([np.mean(np.abs(s[\"trials\"].pole_out.dropna().values * 100 - np.round(s[\"trials\"].pole_out.dropna().values * 100)) < 1e-6)\n                      for s in cn_sessions if s[\"trials\"].stim.isin([9]).any()]))\nprint(f\"Fraction of pole-out times on a 10 ms grid in these sessions: {prec:.2f}\")\n\n# %% [markdown]\n# RESULT fig3-cn-latency\n\n# %% [markdown]\n# ## fig3c-cn-selectivity-abolished\n#\n# > CN selectivity for lick left and lick right trials was abolished by bilateral ALM\n# > photo-inhibition.\n\n# %%\ndef cn_photostim_selectivity(units_, code, rng):\n    \"\"\"As analysis_compiled_all_DCN_ALMsilencing_selectivity.m and analysis_DCN_ALM_photoinhibition_selectivity.m.\"\"\"\n    rows = []\n    for u in units_:\n        s, i, use = u[\"s\"], u[\"i\"], u[\"use\"]\n        t = s[\"trials\"]\n        r = cn.epoch_rates(s, i)\n        ctrl, stim = use & (t.stim.values == 0), use & (t.stim.values == code)\n        R, L = (t.trial_type == \"R\").values, (t.trial_type == \"L\").values\n        if (ctrl & R).sum() < 30 or (ctrl & L).sum() < 30 or (stim & R).sum() <= 2 or (stim & L).sum() <= 2:\n            continue\n        ps = stats.ttest_ind(r[\"sample\"].values[ctrl & R], r[\"sample\"].values[ctrl & L]).pvalue\n        pd_ = stats.ttest_ind(r[\"delay\"].values[ctrl & R], r[\"delay\"].values[ctrl & L]).pvalue\n        if not (ps < 0.05 or pd_ < 0.05):\n            continue\n        ri, li = rng.permutation(np.flatnonzero(ctrl & R)), rng.permutation(np.flatnonzero(ctrl & L))\n        d = r[\"delay\"].values\n        sgn = 1.0 if d[ri[:20]].mean() > d[li[:20]].mean() else (-1.0 if d[ri[:20]].mean() < d[li[:20]].mean() else 0.0)\n        if sgn == 0:\n            continue\n        rows.append({\"mouse\": u[\"mouse\"], \"location\": u[\"location\"],\n                     \"ctrl\": sgn * (d[ri[20:]].mean() - d[li[20:]].mean()), \"stim\": sgn * (d[stim & R].mean() - d[stim & L].mean())})\n    return pd.DataFrame(rows)\n\n\ndef judge(tbl, rng, label):\n    ratio = tbl.stim.mean() / tbl.ctrl.mean()\n    boot = np.array([tbl.iloc[rng.integers(0, len(tbl), len(tbl))].pipe(lambda x: x.stim.mean() - x.ctrl.mean()) for _ in range(10000)])\n    p = float((boot >= 0).mean())\n    print(f\"{label}: {len(tbl)} neurons; delay selectivity control {tbl.ctrl.mean():.2f}, photo-inhibition {tbl.stim.mean():.2f} \"\n          f\"spikes/s; ratio {ratio:.2f}; one-tailed bootstrap p (not lower) = {p:.4f}\")\n    return ratio, p\n\n# %% tags=[\"claim:fig3c-cn-selectivity-abolished\"]\nrng = np.random.default_rng(604)\nsel9 = cn_photostim_selectivity(vgat_units, 9, rng)\njudge(sel9, rng, \"Bilateral ALM photo-inhibition (code 9)\")\nprint(\"Expected n = 157\")\nprint(\"By nucleus:\"); print(sel9.groupby(\"location\")[[\"ctrl\", \"stim\"]].agg([\"mean\", \"size\"]).round(2).to_string())\nprint(\"By mouse, ratio:\", sel9.groupby(\"mouse\").apply(lambda x: round(x.stim.mean() / x.ctrl.mean(), 2), include_groups=False).to_dict())\n\n# %% [markdown]\n# RESULT fig3c-cn-selectivity-abolished\n\n# %% [markdown]\n# ## ed6-cn-either-hemisphere\n#\n# > Photo-inhibiting either side of ALM reduced CN preparatory activity.\n\n# %% tags=[\"claim:ed6-cn-either-hemisphere\"]\nrng = np.random.default_rng(605)\nfor code, lab in ((7, \"left ALM (ipsilateral to the CN recording, code 7)\"), (8, \"right ALM (contralateral, code 8)\"),\n                  (10, \"variant, bilateral M1 (code 10)\")):\n    us = cn_units_with({code})\n    tbl = cn_photostim_selectivity(us, code, rng)\n    if len(tbl):\n        judge(tbl, rng, lab)\n    else:\n        print(lab, \": no neurons meet the trial criteria\")\n"
}
```

```
File created successfully at: /tmp/claude-1001/dev/nb_cn.py (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
python3 - <<'E'
p='/tmp/claude-1001/dev/nb_cn.py'; s=open(p).read()
s=s.replace('''print("Variant, at least 3 error trials of each type:")
# (recomputed with >= 3)
''','')
s=s.replace("r_ = epoch_r = cn.epoch_rates(s, i)","r_ = cn.epoch_rates(s, i)")
open(p,'w').write(s)
p='/tmp/claude-1001/dev/build.py'; s=open(p).read()
s=s.replace('''            s = c.source.replace("sessions = gao2018.load_all()", "import pickle; sessions = pickle.load(open('/tmp/claude-1001/S.pkl','rb'))")''',
'''            s = c.source.replace("alm_sessions = gao2018.load_all()", "import pickle; alm_sessions = pickle.load(open('/tmp/claude-1001/S.pkl','rb'))")
            s = s.replace("sessions = gao2018.load_all()", "import pickle; sessions = pickle.load(open('/tmp/claude-1001/S.pkl','rb'))")
            s = s.replace("cn_sessions, timing = cn.load_all(entries)", "import pickle; cn_sessions, timing = pickle.load(open('/tmp/claude-1001/CN.pkl','rb'))")''')
open(p,'w').write(s)
E
cd entries/000007-gao-2018; . $TMPDIR/explore/bin/activate; python $TMPDIR/dev/build.py $TMPDIR/dev/nb_cn.py $TMPDIR/dev/run_cn.py && time PYTHONPATH=. MPLBACKEND=Agg python $TMPDIR/dev/run_cn.py 2>&1 | grep -v Warn
```

```
######## CELL []
Zenodo record 10.5281/zenodo.6647629: 185 NWB files, 11.89 GB compressed, 23.05 GB inflated
streamed and parsed 185 files in 12.2 min (16.2 MB/s over 32 connections)

######## CELL ['sanity']
Traceback (most recent call last):
  File "/tmp/claude-1001/dev/run_cn.py", line 30, in <module>
    "units": len(s["spikes"]), "codes": " ".join(f"{int(c)}:{n}" for c, n in
                                        ~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^
                                                 s["trials"].stim.value_counts(dropna=False).sort_index().items())}
                                                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/tmp/claude-1001/dev/run_cn.py", line 30, in <genexpr>
    "units": len(s["spikes"]), "codes": " ".join(f"{int(c)}:{n}" for c, n in
                                                    ~~~^^^
ValueError: cannot convert float NaN to integer

real	0m4.989s
user	0m2.788s
sys	0m0.860s
```

**Agent calls Bash**

```bash
python3 - <<'E'
p='/tmp/claude-1001/dev/nb_cn.py'; s=open(p).read()
s=s.replace('''"codes": " ".join(f"{int(c)}:{n}" for c, n in''','''"codes": " ".join(f"{c:g}:{n}" for c, n in''')
open(p,'w').write(s)
E
cd entries/000007-gao-2018; . $TMPDIR/explore/bin/activate; python $TMPDIR/dev/build.py $TMPDIR/dev/nb_cn.py $TMPDIR/dev/run_cn.py && time PYTHONPATH=. MPLBACKEND=Agg python $TMPDIR/dev/run_cn.py 2>&1 | grep -v Warn
```

```
######## CELL []
Zenodo record 10.5281/zenodo.6647629: 185 NWB files, 11.89 GB compressed, 23.05 GB inflated
streamed and parsed 185 files in 12.2 min (16.2 MB/s over 32 connections)

######## CELL ['sanity']
Mice: 18 ; sessions: 185 ; units: 1212

Units by location: {'outside': 455, 'FN': 377, 'DN': 202, 'IP': 178}

By mouse:
location    DN  FN  IP  outside  sessions
mouse                                    
ANM344651    0   3   0       19         6
ANM344652    7  25   0       27        10
ANM344653    0   0   0       20         2
ANM350830    0   0   0       13         3
ANM350831    0   0   0       13         3
BAYLORCD1    7  34   8       57        12
BAYLORCD2    0   8   6       19         8
BAYLORDJ1    0   9   0        9         5
[... 149 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/000007-gao-2018; . $TMPDIR/explore/bin/activate; cat > $TMPDIR/dev/dbg3.py <<'E'
src=open('/tmp/claude-1001/dev/run_cn.py').read()
cut=src.index("claim:fig2-cn-unit-counts"); cut=src.rindex("\n",0,cut)
exec(src[:cut])
g=alltr[(alltr.good==1)&(alltr.LickEarly==0)]
bad=(abs(g.cue-g.pole_out-1.3)>0.05)|(abs(g.pole_out-g.pole_in-1.3)>0.05)
print('performing non-early trials with odd epochs', int(bad.sum()), 'of', len(g)); print(g[bad][['pole_in','pole_out','cue','outcome','stim']].head(10))
c=cn_sel[in_cn]; m30=(c.n_R>=30)&(c.n_L>=30)
print('CN units with >=30 correct ctrl trials each:', int(m30.sum()), 'selective', round(c.selective[m30].mean(),3), 'prep', round(c.preparatory[m30].mean(),3), 'resp', round(c.sig_response[m30].mean(),3))
print('selective (sample or delay) & >30:', int((c.preparatory & (c.n_R>30)&(c.n_L>30)).sum()))
print('trial counts per CN unit', c.n_R.describe().round(1).to_dict())
E
PYTHONPATH=. MPLBACKEND=Agg python $TMPDIR/dev/dbg3.py 2>&1 | grep -v Warn | tail -18
```

```
DN            0.614        0.327         0.505    202
FN            0.565        0.236         0.499    377
IP            0.624        0.275         0.545    178
performing non-early trials with odd epochs 4640 of 40041
     pole_in  pole_out       cue outcome  stim
20  0.572165  1.872493  3.572986   error   0.0
21  0.572164  1.872492  3.572985     hit   0.0
22  0.572331  1.872659  3.572986     hit   0.0
23  0.571998  1.872168  3.572653     hit   0.0
24  0.572831  1.873160  3.573486     hit   0.0
25  0.572331  1.872660  3.573153     hit   0.0
26  0.571998  1.872327  3.572653     hit   0.0
28  0.571998  1.872326  3.572819     hit   0.0
30  0.572998  1.873327  3.573653     hit   0.0
31  0.571664  1.871993  3.572486     hit   0.0
CN units with >=30 correct ctrl trials each: 457 selective 0.757 prep 0.372 resp 0.67
selective (sample or delay) & >30: 170
trial counts per CN unit {'count': 757.0, 'mean': 46.3, 'std': 32.8, 'min': 0.0, '25%': 12.0, '50%': 48.0, '75%': 70.0, 'max': 137.0}
```

**Agent**

The scripts' 30-trial rule brings the CN fractions into line with the paper (0.757, 0.372, 0.67), though it is not the criterion I fixed. I'll show it as a variant in both notebooks.

**Agent calls Bash**

```bash
python3 - <<'E'
p='/tmp/claude-1001/dev/nb_cn.py'; s=open(p).read()
old='''print("\\nPerforming trials, epoch lengths (s): sample",'''
new='''print("\\nDelay epoch (cue - pole out) of performing trials without early licks, median per mouse (s):",
      alltr[(alltr.good == 1) & (alltr.LickEarly == 0)].assign(d=lambda t: t.cue - t.pole_out).groupby("mouse").d.median().round(2).to_dict())
print("Performing trials, epoch lengths (s): sample",'''
assert old in s; s=s.replace(old,new)
old='''# %% [markdown]
# The record holds 185 sessions from 18 mice, as its description says; the Methods give 169
# sessions.'''
new='''# %% [markdown]
# The record holds 185 sessions from 18 mice, as its description says; the Methods give 169
# sessions. In the sessions of the 2016 mice (ANM ids) the delay epoch is 1.7 s, not the 1.3 s of
# the Methods; the epochs are taken from each trial's own times.'''
assert old in s; s=s.replace(old,new)
old='''print("By mouse:", cn_sel[in_cn].groupby("mouse").selective.mean().round(2).to_dict())'''
new='''print("By mouse:", cn_sel[in_cn].groupby("mouse").selective.mean().round(2).to_dict())
m30 = in_cn & (cn_sel.n_R >= 30) & (cn_sel.n_L >= 30)
print(f"Variant, CN units with at least 30 correct control trials of each type (the scripts' rule for their population "
      f"analyses): {int(m30.sum())} units, selective {cn_sel.selective[m30].mean():.3f}, preparatory {cn_sel.preparatory[m30].mean():.3f}, "
      f"peri-movement {cn_sel.sig_response[m30].mean():.3f}")
print("Correct control trials of each type per CN unit, quartiles (lick right):", cn_sel.n_R[in_cn].quantile([0.25, 0.5, 0.75]).tolist())'''
assert old in s; s=s.replace(old,new)
old='''print("Within tolerance:", int(cnt.within.sum()), "of", len(cnt), "; units in the CN:", int(in_cn.sum()), "(Results: 564)")'''
new='''print("Within tolerance:", int(cnt.within.sum()), "of", len(cnt), "; units in the CN:", int(in_cn.sum()), "(Results: 564)")
m30 = in_cn & (cn_sel.n_R >= 30) & (cn_sel.n_L >= 30)
print("Variant, CN units with at least 30 correct control trials of each type:", int(m30.sum()))'''
assert old in s; s=s.replace(old,new)
old='''print("CN by nucleus:", cn_sel[in_cn].groupby("location").preparatory.mean().round(3).to_dict())'''
new='''print("CN by nucleus:", cn_sel[in_cn].groupby("location").preparatory.mean().round(3).to_dict())
m30 = in_cn & (cn_sel.n_R >= 30) & (cn_sel.n_L >= 30)
print(f"Variant, CN units with at least 30 correct control trials of each type: {cn_sel.preparatory[m30].mean():.3f}")'''
assert old in s; s=s.replace(old,new)
old='''print(f"chi-square ALM against CN: p = {stats.chi2_contingency(t2)[1]:.2g}")'''
new='''print(f"chi-square ALM against CN: p = {stats.chi2_contingency(t2)[1]:.2g}")
m30 = in_cn & (cn_sel.n_R >= 30) & (cn_sel.n_L >= 30)
print(f"Variant, CN units with at least 30 correct control trials of each type: {cn_sel.sig_response[m30].mean():.3f}")'''
assert old in s; s=s.replace(old,new)
open(p,'w').write(s)
p='/tmp/claude-1001/dev/nb_main.py'; s=open(p).read()
old='''print("\\nBy mouse (fractions):")'''
new='''m30 = (sel.n_right >= 30) & (sel.n_left >= 30)
for r, m in readings.items():
    print(f"Variant, {r}, neurons with at least 30 correct control trials of each type: {int((m & m30).sum())} neurons, "
          f"selective {sel.selective[m & m30].mean():.3f}, preparatory {sel.preparatory[m & m30].mean():.3f}, "
          f"peri-movement {sel.sig_response[m & m30].mean():.3f}")
print("\\nBy mouse (fractions):")'''
assert old in s; s=s.replace(old,new)
open(p,'w').write(s)
E
echo ok
```

```
ok
```

**Agent calls Bash**

```bash
cd entries/000007-gao-2018; . $TMPDIR/explore/bin/activate; python $TMPDIR/dev/build.py $TMPDIR/dev/nb_main.py $TMPDIR/dev/run.py && PYTHONPATH=. MPLBACKEND=Agg python $TMPDIR/dev/run.py 2>&1 | grep -v Warn > $TMPDIR/dev/out_main.txt; python $TMPDIR/dev/build.py $TMPDIR/dev/nb_cn.py $TMPDIR/dev/run_cn.py && PYTHONPATH=. MPLBACKEND=Agg python $TMPDIR/dev/run_cn.py 2>&1 | grep -v Warn > $TMPDIR/dev/out_cn.txt; grep -n "Variant, (a)\|Variant, (b)\|precision\|10 ms grid" -A0 $TMPDIR/dev/out_main.txt | head; sed -n '/claim:ed9a-fn-latency/,/fig4f/p' $TMPDIR/dev/out_main.txt; sed -n '/Fraction of event times/,/stim-code/p' $TMPDIR/dev/out_main.txt; grep -n "Variant" $TMPDIR/dev/out_cn.txt
```

```
192:Fraction of event times on a 10 ms grid:
--
359:Variant, (a) photo-activation mice, neurons with at least 30 correct control trials of each type: 961 neurons, selective 0.834, preparatory 0.608, peri-movement 0.680
360:Variant, (b) all 13 mice, neurons with at least 30 correct control trials of each type: 1501 neurons, selective 0.821, preparatory 0.589, peri-movement 0.658
######## CELL ['claim:ed9a-fn-latency']
FN (a) code 2: 187 of 532 neurons modulated; onset 2.0 +/- 8.1 ms; resampled onsets before 0 ms: 0.238
    variants: sustained onset 6.7 +/- 2.3 ms; with each neuron's change in the 200 to 20 ms before onset subtracted, onset -0.1 +/- 8.8 ms (pre-onset change -0.05 spikes/s); 2015 files only (73 neurons), onset 9.5 +/- 6.0 ms
    population change (spikes/s) at bin centres -10, 0, 5, 10, 15, 20, 30 ms: [0.84, -0.14, 1.65, 4.6, 6.4, 7.51, 7.79]
FN (b) codes 1 and 2: 248 of 520 neurons modulated; onset -0.9 +/- 11.9 ms; resampled onsets before 0 ms: 0.443
    variants: sustained onset 9.3 +/- 3.3 ms; with each neuron's change in the 200 to 20 ms before onset subtracted, onset -4.8 +/- 11.7 ms (pre-onset change -0.05 spikes/s); 2015 files only (90 neurons), onset 12.0 +/- 5.1 ms
    population change (spikes/s) at bin centres -10, 0, 5, 10, 15, 20, 30 ms: [0.84, -0.32, 0.47, 2.29, 4.18, 5.92, 6.41]
(a) code 2: latency within 4.5 +/- 2.6 ms: True; count within 227 +/- 22.7: False
(b) codes 1 and 2: latency within 4.5 +/- 2.6 ms: False; count within 227 +/- 22.7: True

######## CELL ['claim:ed9a-dn-latency']
DN (a) code 4: 183 of 539 neurons modulated; onset -9.0 +/- 5.7 ms; resampled onsets before 0 ms: 0.981
    variants: sustained onset -3.3 +/- 5.5 ms; with each neuron's change in the 200 to 20 ms before onset subtracted, onset -5.0 +/- 5.8 ms (pre-onset change 0.23 spikes/s); 2015 files only: 1 modulated neurons, too few
    population change (spikes/s) at bin centres -10, 0, 5, 10, 15, 20, 30 ms: [0.79, 1.31, 1.85, 2.35, 2.69, 2.9, 4.37]
DN (b) codes 3
[... 54 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n '/claim:fig1g-fn-delay/,/claim:fig2-alm-selective/p' $TMPDIR/dev/out_main.txt | head -80; sed -n '/claim:fig2c/,/claim:fig3e-alm-mean/p' $TMPDIR/dev/out_main.txt
```

```
######## CELL ['claim:fig1g-fn-delay-performance']
FN mice (6), code 2 against control: control 0.873 (3715 trials), photostim 0.630 (446 trials)
change -0.243; bootstrap 95% interval -0.388 to -0.101; one-tailed p = 0.0001

Per mouse:
stim             0      2  change
subject                          
BAYLORCD6    0.745  0.662  -0.083
BAYLORNL15   0.896  0.447  -0.450
anm00314746  0.921  0.782  -0.139
anm00314757  0.906  0.727  -0.179
anm00314758  0.912  0.765  -0.147
anm00314760  0.875  0.479  -0.396
Mice with lower performance on code 2 trials: 6 of 6

######## CELL ['claim:fig1-fn-sample-no-effect']
trial type  control  code 1  change  ci_low  ci_high  one_tailed_p  n_code1
    contra   0.8563  0.8226 -0.0336 -0.1815   0.1032        0.3648      265
      ipsi   0.8929  0.9167  0.0238 -0.0609   0.0889        0.2526      240
By lick direction, the same test:
[... 89 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n '/claim:fig3e-alm-mean/,/claim:fig3f/p;/claim:fig4i-fn-cd-collapse/,$p' $TMPDIR/dev/out_main.txt | grep -v "^ \+[A-Za-z0-9]* \+20[0-9]*T" | head -60
```

```
######## CELL ['claim:fig3e-alm-mean-rate-unchanged']
Neurons: 643; mean delay-epoch rate control 4.46, code 6 4.80 spikes/s (expected 4.15 +/- 0.415 and 4.39 +/- 0.439)
Two-sample t-test across neurons: p = 0.379
Variant, paired t-test: p = 0.151; median change -0.071 spikes/s
Variant, codes 5 and 6: control 4.45, photo-inhibition 4.94 spikes/s, two-sample p = 0.187

######## CELL ['claim:fig3e-alm-up-down']
(a) code 6: 137 increased, 97 decreased; fraction increased 0.585 (expected 0.548 +/- 0.055); binomial p = 0.0106
(b) codes 5 and 6: 172 increased, 126 decreased; fraction increased 0.577 (expected 0.548 +/- 0.055); binomial p = 0.00903

######## CELL ['claim:fig3-alm-latency-pi']
(a) code 6: 234 neurons; onset 7.8 +/- 14.3 ms (bootstrap s.d. over neurons); resamples without an onset in the window: 0; before 0 ms: 0.293
   variant, pre-onset change subtracted (0.21 spikes/s): onset 16.3 +/- 16.6 ms
   expected 7.1 +/- 3.8 ms; within: True
   population change (spikes/s) at bin centres -10, 0, 5, 10, 15, 20, 30 ms: [0.21, 0.75, 0.7, 0.8, 0.7, 0.08, 0.39]
(b) codes 5 and 6: 298 neurons; onset 16.6 +/- 12.9 ms (bootstrap s.d. over neurons); resamples without an onset in the window: 0; before 0 ms: 0.105
   variant, pre-onset change subtracted (0.04 spikes/s): onset 19.0 +/- 12.7 ms
   expected 7.1 +/- 3.8 ms; within: False
   population change (spikes/s) at bin centres -10, 0, 5, 10, 15, 20, 30 ms: [-0.08, 0.24, 0.48, 0.36, 0.16, -0.01, 1.06]
(a) code 6: sustained onset 31.1 +/- 13.7 ms; change in 10 ms bins at -50 to +100 ms (5 ms steps):
[... 27 more lines not kept]
```

**Agent**

All numbers are in. Writing the conclusions, headers and summaries now.

**Agent calls Bash**

```bash
cat > $TMPDIR/dev/results_main.py <<'E'
R = {}
R["stim-code-link"] = """**Result: reproduced.** Codes 1 and 2 occur only in the six fastigial mice, 3 and 4 only in the
three dentate mice and 5 and 6 only in the four L7-cre mice. For every code the ALM change first
exceeds the pre-trial level by 4 SD 5 to 35 ms after the onset the name implies (pole in for codes
1 and 3, pole out for 2, 4, 5 and 6), with no bin above it between pole in and that onset. The
change 0.7 to 1.2 s after onset is 0.95 spikes/s after code 5 and 1.64 after code 6, so code 5
ends earlier, as a 0.5 s photostimulus against a 1.3 s one would. The names from the Zenodo data
description are used below."""
R["methods-alm-unit-counts"] = """**Result: not reproduced.** Only the session count of the photo-inhibition mice (20 against 19)
is within tolerance, under both readings. The dandiset holds more units than the paper reports:
1112 pyramidal neurons in the 9 photo-activation mice against 912 (567 against 446 in the
fastigial mice, 545 against 466 in the dentate mice), and 737 units (706 pyramidal) in the
photo-inhibition mice against 490 (454). The width rule gives similar counts (1082, 557, 525,
676). With the 9 mice the dandiset already has 1186 units, against the paper's 1309 for 10 mice.
The paper's unit selection is not described and the dandiset does not mark which units the paper
used."""
R["fig1g-fn-delay-performance"] = """**Result: reproduced.** In the six fastigial mice, delay-epoch photo-activation lowers
performance from 0.873 to 0.630 (change -0.243, 95% interval -0.388 to -0.101, one-tailed
bootstrap p = 0.0001), and performance is lower on code 2 trials in all six mice."""
R["fig1-fn-sample-no-effect"] = """**Result: reproduced.** Sample-epoch fastigial photo-activation changes performance by -0.034
on contralateral trials (one-tailed p = 0.365) and +0.024 on ipsilateral trials (p = 0.253), so
neither trial type shows a decrease with p < 0.05."""
R["fig1g-dn-little-effect"] = """**Result: reproduced.** Delay-epoch dentate photo-activation (0.5 s, three mice) changes
performance by -0.038 (95% interval -0.091 to +0.027, one-tailed p = 0.108), so the test does not
find an effect. The paper's dentate result is from 1.3 s photostimulation in eight mice."""
R["fig1h-fn-delay-bias-either-direction"] = """**Result: reproduced.** Of the six fastigial mice, two (BAYLORNL15 and anm00314760) are pushed
toward ipsilateral licking (bias +0.68 and +0.76, p < 0.0001) and one (anm00314746) toward
contralateral licking (bias -0.49, p = 0.0006); the other three show no significant bias (p 0.48
to 0.63)."""
R["ed1f-fn-no-early-licks"] = """**Result: reproduced.** The early-lick rate is 0.079 on control and 0.127 on code 2 trials
(increase +0.049, 95% interval -0.026 to +0.163, one-tailed p = 0.174), so the test does not find
an increase. One mouse (BAYLORCD6) rises from 0.081 to 0.324. The no-lick rate rises from 0.018 to
0.11 on code 2 trials (a variant, not tested)."""
R["fig1k-pi-delay-performance"] = """**Result: reproduced.** In the four L7-cre mice, CN photo-inhibition in the delay epoch lowers
performance from 0.848 to 0.693 (change -0.155, 95% interval -0.245 to -0.067, one-tailed p <
0.0001); the 0.5 s (code 5) and 1.3 s (code 6) photostimuli each lower it (-0.142, p = 0.012;
-0.171, p < 0.0001), in every mouse."""
R["fig2-alm-selective-fraction"] = """**Result: reproduced.** 866 of 1112 pyramidal neurons of the photo-activation mice (0.779) are
selective, within 0.821 +/- 0.082, as are 1365 of 1818 over all 13 mice (0.751). With trial types
shuffled the same test calls 0.121 of neurons selective. With the scripts' rule of at least 30
correct trials of each type the fraction is 0.834 (961 neurons)."""
R["fig2-alm-preparatory-fraction"] = """**Result: reproduced.** Under reading (a), 621 of 1112 pyramidal neurons (0.558) are selective
in the sample or delay epoch, within 0.59 +/- 0.059; over all 13 mice (reading b) the fraction is
0.525, outside it. With at least 30 correct trials of each type, reading (a) gives 0.608."""
R["fig2-alm-perimovement-fraction"] = """**Result: reproduced.** Under reading (a), 0.629 of pyramidal neurons are selective in the
response epoch, within 0.67 +/- 0.067; reading (b) gives 0.596, outside it. With at least 30
correct trials of each type, reading (a) gives 0.680."""
R["fig2c-alm-selectivity-time-course"] = """**Result: partially reproduced.** Selectivity emerges in the sample epoch (1.19 spikes/s in its
last 300 ms, 95% interval 0.99 to 1.42, against 0.02 before pole in) and grows through the delay
(mean 2.09 spikes/s), but its maximum (2.53 spikes/s) falls at 2.54 s, just before the cue, and
the response-epoch mean (0.96) is lower than the delay mean, so the second part of the criterion
fails. When the preferred type is picked from the response epoch, the maximum is at 3.09 s, in
the response epoch (2.66 spikes/s), and the late-sample selectivity is 0.55 spikes/s; the paper
says the choice of epoch made little difference, which these data do not bear out for the
response epoch. The criterion gave no partial level; the effect holds in part."""
R["fig3e-alm-modulated-fraction"] = """**Result: reproduced.** Under reading (b), codes 5 and 6 pooled, 298 of 695 pyramidal neurons
(0.429) are modulated, within 0.434 +/- 0.043; under reading (a), code 6 alone, 234 of 643 (0.364)
are, outside it. Splitting control trials in two gives 0.01, the false-positive rate of the test.
The fraction differs by mouse (0.18 in BAYLORCD12 and CD13, 0.39 and 0.44 in CD8 and CD14)."""
R["fig3e-alm-mean-rate-unchanged"] = """**Result: reproduced.** The mean delay-epoch rate is 4.46 spikes/s on control and 4.80 on code
6 trials (both within tolerance of 4.15 and 4.39), and the two-sample t-test gives p = 0.379. The
paired test also finds no change (p = 0.151)."""
R["fig3e-alm-up-down"] = """**Result: reproduced.** Under reading (b), the one that matched, 172 of 298 modulated neurons
increase (0.577), within 0.548 +/- 0.055; under reading (a), 0.585. More neurons increase than
decrease (binomial p = 0.009), which the paper does not state."""
R["fig3-alm-latency-pi"] = """**Result: not reproduced.** Under reading (b), the one that matched in
fig3e-alm-modulated-fraction, the onset is 16.6 +/- 12.9 ms, outside 7.1 +/- 3.8 ms. Under reading
(a) it is 7.8 +/- 14.3 ms, within tolerance, but 29% of the resampled onsets fall before the
photostimulus, so this value reflects noise crossings of the threshold before the rise. The
population change stays below 1 spikes/s up to 25 ms after delay onset and rises to 2 to 3
spikes/s between 30 and 40 ms; the sustained onset is 29 to 32 ms for codes 5, 6 and both. The event
times of these sessions lie on a 10 ms grid (data check), which limits any latency to that
precision."""
R["fig3f-alm-selectivity-abolished"] = """**Result: reproduced.** In 252 selective neurons, delay selectivity falls from 2.04 spikes/s on
control trials to 0.48 on code 6 trials, a ratio of 0.23, within the 25% the criterion allows;
the remaining selectivity is above 0 (95% interval 0.21 to 0.76). In two of four mice it falls to
near zero (0.08 and -0.02 spikes/s), in the other two to 0.71 and 0.73. With codes 5 and 6 pooled
the ratio is 0.36."""
R["ed9a-fn-latency"] = """**Result: partially reproduced.** Under reading (a), delay photostimulation, the onset is 2.0
+/- 8.1 ms, within 4.5 +/- 2.6 ms, but 187 neurons are modulated, outside 227 +/- 22.7; under
reading (b) 248 neurons are modulated, within tolerance, and the onset is -0.9 +/- 11.9 ms,
outside it. The first-crossing onset is fragile here: under reading (a), 24% of resampled onsets
fall before the photostimulus. The population change rises from -0.14 spikes/s at 0 ms to 1.65 at
5 ms and 4.6 at 10 ms; the sustained onset is 6.7 +/- 2.3 ms, and in the 2015 files, whose event
times are precise, the first-crossing onset is 9.5 +/- 6.0 ms."""
R["ed9a-dn-latency"] = """**Result: not reproduced.** Neither reading gives a latency or count within tolerance: the
onsets are -9.0 +/- 5.7 ms (code 4) and -12.2 +/- 4.5 ms (codes 3 and 4), against 8.3 +/- 5.0,
and 183 and 230 neurons are modulated, against 163 +/- 16.3. In over 96% of resamples the onset
falls before the photostimulus: the population change is already 0.79 spikes/s 10 ms before onset
and 1.31 at onset, and subtracting each neuron's change in the 200 ms before onset still gives
-5.0 ms. The dentate sessions are almost all from 2017 files with event times on a 10 ms grid, and
the 2015 files have too few modulated neurons (1 and 4) to measure an onset, so the data cannot
place this onset to within the few milliseconds the claim needs."""
R["fig4f-fn-persistent"] = """**Result: reproduced.** In the bin 1.0 to 1.4 s after the fastigial photostimulus ended, 78 of
538 neurons (0.145) differ from control, against 5 of 538 (0.009) in the bin ending at onset (one-
tailed Fisher p = 2.3e-19). The fraction declines from 0.361 during photostimulation to 0.119 at
1.2 s after offset."""
R["fig4g-dn-recovery"] = """**Result: partially reproduced.** In the bin 1.0 to 1.4 s after offset, 0.051 of dentate-mouse
neurons differ from control, lower than the fastigial 0.145 (Fisher p = 2e-07) and down from
0.328 during photostimulation, but 2.3 times the 0.022 before onset, above the factor of 2 the
criterion allows. ALM recovers faster after dentate than after fastigial photo-activation, and
not fully within 1.4 s. The criterion gave no partial level; the effect holds in part."""
R["fig4i-fn-cd-collapse"] = """**Result: reproduced.** Over 15 sessions, the separation of lick right and lick left trajectories
in the last 400 ms of the delay is 62.97 on control and 31.42 on code 2 trials, a ratio of 0.499
(95% interval 0.204 to 0.955), just under the 0.5 of the criterion. The result is near that
threshold: the median of the per-session ratios is 0.602, the mean of them 0.854, and two of six
mice (BAYLORCD6, 2.45; anm00314746, 1.27) show no collapse. Separation is smaller with
photostimulation in 11 of 15 sessions. With the dentate sessions the analysis uses 28 sessions,
the number the Methods give."""
R["fig4i-dn-cd-minimal"] = """**Result: reproduced.** Over 13 sessions the separation is 55.79 on control and 58.21 on code 4
trials, a ratio of 1.04 (95% interval 0.87 to 1.20), and the fastigial ratio is lower in 98.5% of
paired resamples."""
R["ed10d-fn-no-prediction"] = """**Result: not reproduced.** On fastigial photostimulation trials the projection on the coding
direction still predicts licking right (slope 0.40, p = 0.00015, 386 trials), though less than on
control trials (slope 1.44, p = 3e-63). The probability of licking right goes from 0.51 to 0.77
across projection bins on photostimulation trials, against 0.27 to 0.85 on control trials. The
trial count (386) is outside 337 +/- 33.7."""
E
cat > $TMPDIR/dev/results_cn.py <<'E'
R = {}
R["fig2-cn-unit-counts"] = """**Result: not reproduced.** Only the session count is within tolerance (185 against 169). The
record holds 1212 units against 878: 455 outside the CN (314), 377 fastigial (268), 178
interposed (139) and 202 dentate (157), 757 in the CN against the Results' 564. 457 CN units
have at least 30 correct control trials of each type. The paper's unit selection is not
described."""
R["fig2-cn-selective-fraction"] = """**Result: not reproduced.** 448 of 757 CN units (0.592) are selective, outside 0.738 +/- 0.074;
the chance level of the test is 0.127. Restricted to the 457 units with at least 30 correct
control trials of each type, the scripts' rule for their population analyses, the fraction is
0.757, within tolerance, which suggests the paper's 564 neurons were selected by trial count or
a similar rule that the Methods do not state. The fraction ranges from 0.07 to 0.93 across mice."""
R["fig2-cn-preparatory-fraction"] = """**Result: partially reproduced.** Preparatory activity is more prevalent in ALM (621 of 1112,
0.558) than in CN (204 of 757, 0.269), chi-square p = 8.7e-35, but the CN fraction is outside
0.35 +/- 0.035. With at least 30 correct trials of each type the CN fraction is 0.372, within
tolerance."""
R["fig2-cn-perimovement-fraction"] = """**Result: not reproduced.** 0.511 of CN units are selective in the response epoch, outside 0.66
+/- 0.066, and lower than ALM's 0.629 (chi-square p = 5.7e-07), where the paper finds them equal.
With at least 30 correct trials of each type the CN fraction is 0.670, within tolerance."""
R["ed4e-cn-predict-movement"] = """**Result: not reproduced.** Of 117 delay-selective CN neurons with more than 3 error trials of
each type (against 73), 0.496 have a negative error to correct ratio, outside 0.67 +/- 0.067; the
median ratio is 0.02."""
R["ed4g-fn-contra-late-delay"] = """**Result: reproduced.** In the last 500 ms of the delay a mean of 0.650 of significant fastigial
neurons per mouse prefer contralateral licking (13 mice, one-tailed p = 0.033), and in the first
500 ms 0.639 do (11 mice), not different from 0.5 (two-tailed p = 0.219). The paper's p = 0.0001
for the late window is not matched; the early fraction is above one half without significance."""
R["fig3b-cn-modulated-fraction"] = """**Result: not reproduced.** 145 of 517 CN units (0.280) in sessions with bilateral ALM photo-
inhibition are modulated at p < 0.01, outside 0.476 +/- 0.048; at p < 0.05 the fraction is 0.412.
The record has 563 CN units in these sessions, against the paper's 389. The fraction is 0.435 in
the dentate, 0.178 in the fastigial and 0.186 in the interposed nucleus."""
R["fig3b-cn-net-increase"] = """**Result: reproduced.** Of the 145 modulated CN units, 100 increase their delay-epoch rate
(0.690, within 0.665 +/- 0.066; binomial p = 5.7e-06)."""
R["fig3-cn-latency"] = """**Result: not reproduced.** The first-crossing onset is 0.2 +/- 13.7 ms, outside 10.7 +/- 4.0
ms, and 47% of resampled onsets fall before the photostimulus; the population change is 1.14
spikes/s at -10 ms and 0.29 at 5 ms, and rises to 3.16 at 15 ms. The sustained onset is 14.3 +/-
2.0 ms. In these sessions 96% of pole-out times lie on a 10 ms grid."""
R["fig3c-cn-selectivity-abolished"] = """**Result: reproduced.** In 137 selective CN units (against 157), delay selectivity falls from
3.73 spikes/s on control to 0.68 on bilateral ALM photo-inhibition trials, a ratio of 0.18 (one-
tailed p < 0.0001). It falls to 0.01 in fastigial units and to 0.96 and 1.15 in dentate and
interposed units."""
R["ed6-cn-either-hemisphere"] = """**Result: reproduced.** Photo-inhibiting the left ALM lowers CN delay selectivity from 3.48 to
1.29 spikes/s (154 units, p < 0.0001) and the right ALM from 3.37 to 1.56 (152 units, p =
0.0002). Bilateral M1 photo-inhibition, a variant, lowers it from 3.62 to 1.84 (75 units, p =
0.019), so the reduction is not specific to ALM in these data."""
E
echo ok
```

```
ok
```

**Agent calls Bash**

```bash
python3 - <<'E'
p='/tmp/claude-1001/dev/results_main.py'; s=open(p).read()
s=s.replace("""-5.0 ms. The dentate sessions are almost all from 2017 files with event times on a 10 ms grid, and
the 2015 files have too few modulated neurons (1 and 4) to measure an onset, so the data cannot
place this onset to within the few milliseconds the claim needs.""","""-5.0 ms. Eleven of the 13 dentate sessions are from 2017 files with event times on a 10 ms grid,
and the 2015 files have too few modulated neurons (1 and 4) to measure an onset, so the data
cannot place this onset to within the few milliseconds the claim needs.""")
open(p,'w').write(s)
p='/tmp/claude-1001/dev/results_cn.py'; s=open(p).read()
s=s.replace("""0.019), so the reduction is not specific to ALM in these data.""","""0.019), a smaller reduction than bilateral ALM photo-inhibition (ratio 0.51 against 0.18 in
fig3c-cn-selectivity-abolished).""")
open(p,'w').write(s)
E
cat >> $TMPDIR/dev/nb_cn.py <<'E'

# %% [markdown]
# ## ed4c-lick-modulation (blocked)
#
# > In ALM and CN a similar small proportion (below 10%) of neurons modulated their spike rates
# > during individual licks.
#
# The dandiset has no lick times. For the ALM sessions they are in the MATLAB record of the paper
# on Zenodo, whose data files also hold the raw voltage traces. The time to fetch them at the rate
# measured above:

# %% tags=["claim:ed4c-lick-modulation"]
import requests
rec = requests.get("https://zenodo.org/api/records/6653158", timeout=60).json()
mat = [(f["key"], f["size"]) for f in rec["files"] if f["key"].startswith("datafiles_")]
total = sum(size for _, size in mat)
rate = timing["compressed_bytes"] / timing["seconds"]
print("MATLAB data files of doi:10.5281/zenodo.6653158:", [(k, round(v / 1e9, 2)) for k, v in mat])
print(f"total {total / 1e9:.1f} GB; at the {rate / 1e6:.1f} MB/s measured here, {total / rate / 60:.0f} min to fetch, "
      "against the 30 min limit for a notebook")
E
python3 - <<'E'
import re
for nbp, rp in (('/tmp/claude-1001/dev/nb_main.py','/tmp/claude-1001/dev/results_main.py'),('/tmp/claude-1001/dev/nb_cn.py','/tmp/claude-1001/dev/results_cn.py')):
    ns={}; exec(open(rp).read(),ns); R=ns['R']
    s=open(nbp).read()
    for k,v in R.items():
        marker=f"# %% [markdown]\n# RESULT {k}\n"
        assert marker in s, k
        s=s.replace(marker, "# %% [markdown]\n" + "\n".join("# "+l for l in v.split("\n")) + "\n")
    left=re.findall(r"# RESULT .*", s); print(nbp, 'unfilled', left)
    open(nbp,'w').write(s)
E
```

```
Exit code 1
/tmp/claude-1001/dev/nb_main.py unfilled []
Traceback (most recent call last):
  File "<stdin>", line 7, in <module>
AssertionError: ed6-cn-either-hemisphere
```

**Agent calls Bash**

```bash
python3 - <<'E'
p='/tmp/claude-1001/dev/nb_cn.py'; s=open(p).read()
old='''# %% [markdown]
# ## ed4c-lick-modulation (blocked)'''
s=s.replace(old, "# %% [markdown]\n# RESULT ed6-cn-either-hemisphere\n\n"+old)
ns={}; exec(open('/tmp/claude-1001/dev/results_cn.py').read(),ns); R=ns['R']
for k,v in R.items():
    marker=f"# %% [markdown]\n# RESULT {k}\n"
    assert marker in s, k
    s=s.replace(marker, "# %% [markdown]\n" + "\n".join("# "+l for l in v.split("\n")) + "\n")
import re; print(re.findall(r"# RESULT .*", s))
open(p,'w').write(s)
E
grep -c "Result:" $TMPDIR/dev/nb_main.py $TMPDIR/dev/nb_cn.py
```

```
[]
/tmp/claude-1001/dev/nb_main.py:24
/tmp/claude-1001/dev/nb_cn.py:11
```

**Agent**

Conclusions inserted (24 tested claims in the main notebook, 11 in the CN notebook). Now the headers and summaries.

**Agent calls Bash**

```bash
cat > $TMPDIR/dev/header_main.md <<'E'
# Reproducing Gao et al. (2018) from dandiset 000007

**Paper.** Gao Z, Davis C, Thomas AM, Economo MN, Abrego AM, Svoboda K, De Zeeuw CI, Li N (2018). A
cortico-cerebellar loop for motor planning. *Nature* 563, 113-116.
[doi:10.1038/s41586-018-0633-x](https://doi.org/10.1038/s41586-018-0633-x). This attempt used the full
text of the author manuscript in PubMed Central (PMC6212318), and the publisher's Supplementary
Information for Supplemental Table 1 (the mice of each experiment).

**Dandiset.** [DANDI:000007](https://dandiarchive.org/dandiset/000007/0.220126.1903), version
0.220126.1903. The paper (2018) cites no DANDI version, as the dandiset was created later. This is the
only published version. The draft holds the same 54 assets (same blobs and sizes) and differs only
in metadata added later (a longer description, keywords, anatomy terms, affiliations), none of which
the analysis uses.

**What the dandiset holds.** ALM recordings in 13 mice, 54 sessions: 6 mice with ChR2 in the
fastigial nucleus and 3 in the dentate nucleus (photo-activation, 34 sessions) and 4 L7-cre x Ai32
mice (CN photo-inhibition, 20 sessions). Spike times, cell type labels and mean waveforms of the
units, and a trial table with the task times, the outcome and a photostimulation code. It does not
hold the CN recordings, the lick times, the lesion and behaviour-only sessions, or the anatomy.

**Outside inputs.** The names of the photostimulation codes come from the data description of the
paper's Zenodo records (doi:10.5281/zenodo.6647629 and 10.5281/zenodo.6653158, found through CRCNS
alm-6, which the paper's reporting summary names); stim-code-link tests them. Method choices the
Methods leave open follow the paper's CN analysis scripts in the MATLAB record. The CN recordings,
also on Zenodo, are analysed in the second notebook, `reproduce_gao_2018_cn.ipynb`.

| Claim | Data | Status | Notebook |
|---|---|---|---|
| stim-code-link | with labels | tested | this |
| methods-alm-unit-counts | dandiset | tested | this |
| fig1g-fn-delay-performance | with labels | tested | this |
| fig1-fn-sample-no-effect | with labels | tested | this |
| fig1g-dn-little-effect | with labels | tested | this |
| fig1h-fn-delay-bias-either-direction | with labels | tested | this |
| ed1f-fn-no-early-licks | with labels | tested | this |
| fig1k-pi-delay-performance | with labels | tested | this |
| fig1d-fn-lesion | dandiset | blocked, data missing | |
| fig1e-lesion-lick-timing | dandiset | blocked, data missing | |
| fig1h-response-contra-bias | dandiset | blocked, data missing | |
| fig1i-licking-unaffected | dandiset | blocked, data missing | |
| fig1k-response-ipsi-bias | dandiset | blocked, data missing | |
| ed2-pi-silences-fastigial | dandiset | blocked, data missing | |
| fig2-alm-selective-fraction | dandiset | tested | this |
| fig2-alm-preparatory-fraction | dandiset | tested | this |
| fig2-alm-perimovement-fraction | dandiset | tested | this |
| fig2c-alm-selectivity-time-course | dandiset | tested | this |
| fig2-cn-unit-counts | elsewhere (Zenodo) | tested | CN |
| fig2-cn-selective-fraction | elsewhere (Zenodo) | tested | CN |
| fig2-cn-preparatory-fraction | elsewhere (Zenodo) | tested | CN |
| fig2-cn-perimovement-fraction | elsewhere (Zenodo) | tested | CN |
| ed4e-cn-predict-movement | elsewhere (Zenodo) | tested | CN |
| ed4g-fn-contra-late-delay | elsewhere (Zenodo) | tested | CN |
| ed4c-lick-modulation | elsewhere (Zenodo) | blocked, too large | CN |
| fig3b-cn-modulated-fraction | elsewhere (Zenodo) | tested | CN |
| fig3b-cn-net-increase | elsewhere (Zenodo) | tested | CN |
| fig3-cn-latency | elsewhere (Zenodo) | tested | CN |
| fig3c-cn-selectivity-abolished | elsewhere (Zenodo) | tested | CN |
| ed6-cn-either-hemisphere | elsewhere (Zenodo) | tested | CN |
| fig3e-alm-modulated-fraction | with labels | tested | this |
| fig3e-alm-mean-rate-unchanged | with labels | tested | this |
| fig3e-alm-up-down | with labels | tested | this |
| fig3-alm-latency-pi | with labels | tested | this |
| fig3f-alm-selectivity-abolished | with labels | tested | this |
| ed9a-fn-latency | with labels | tested | this |
| ed9a-dn-latency | with labels | tested | this |
| fig4f-fn-persistent | with labels | tested | this |
| fig4g-dn-recovery | with labels | tested | this |
| fig4i-fn-cd-collapse | with labels | tested | this |
| fig4i-dn-cd-minimal | with labels | tested | this |
| ed10d-fn-no-prediction | with labels | tested | this |
| ed10c-alm-pi-endpoints | dandiset | blocked, data missing | |
| ed10efg-alm-needed-after-fn | dandiset | blocked, data missing | |
| fig4bc-fastigial-thalamus | dandiset | blocked, data missing | |

Seeds are fixed per section. The notebook streams about 200 MB and takes about five minutes.
E
cat > $TMPDIR/dev/summary_main.md <<'E'
## Summary

A failure to reproduce here may be a failure of this attempt, not of the paper: see the reasoning
and the differences from the paper's method.

| Claim | Outcome |
|---|---|
| stim-code-link | reproduced |
| methods-alm-unit-counts | not reproduced |
| fig1g-fn-delay-performance | reproduced |
| fig1-fn-sample-no-effect | reproduced |
| fig1g-dn-little-effect | reproduced |
| fig1h-fn-delay-bias-either-direction | reproduced |
| ed1f-fn-no-early-licks | reproduced |
| fig1k-pi-delay-performance | reproduced |
| fig2-alm-selective-fraction | reproduced |
| fig2-alm-preparatory-fraction | reproduced |
| fig2-alm-perimovement-fraction | reproduced |
| fig2c-alm-selectivity-time-course | partially reproduced |
| fig3e-alm-modulated-fraction | reproduced |
| fig3e-alm-mean-rate-unchanged | reproduced |
| fig3e-alm-up-down | reproduced |
| fig3-alm-latency-pi | not reproduced |
| fig3f-alm-selectivity-abolished | reproduced |
| ed9a-fn-latency | partially reproduced |
| ed9a-dn-latency | not reproduced |
| fig4f-fn-persistent | reproduced |
| fig4g-dn-recovery | partially reproduced |
| fig4i-fn-cd-collapse | reproduced |
| fig4i-dn-cd-minimal | reproduced |
| ed10d-fn-no-prediction | not reproduced |
| fig1d-fn-lesion, fig1e-lesion-lick-timing, fig1h-response-contra-bias, fig1i-licking-unaffected, fig1k-response-ipsi-bias, ed2-pi-silences-fastigial, ed10c-alm-pi-endpoints, ed10efg-alm-needed-after-fn, fig4bc-fastigial-thalamus | blocked, data missing |

The CN claims are summarised in the second notebook.

**How the analysis differs from the paper's.** Behaviour is tested on the trials of the recording
sessions only, the only behaviour in the dandiset: delay dentate photo-activation is 0.5 s in 3 mice
here against 1.3 s in 8 in Figure 1g, and CN photo-inhibition covers 4 of the 7 mice of Figure 1k.
The dandiset holds more units than the paper counts and does not say which the paper used, so all
units labelled pyramidal are used. The trial table has no column for periods when the mouse was not
performing. The scripts' stable-trial rule, written for the CN data, is applied to ALM, except in
the coding-direction analysis. Ambiguous numbers are tested under the readings listed in the claims
file: reading (b) matched for the photo-inhibition fraction, and the latency and up-down claims are
judged under it. Latencies use a search window and bin centre chosen here.

**What was found about the dandiset.** The photostimulation codes have no description; their names
come from the Zenodo data description and match the ALM responses. The trial time columns are
described as relative to the trial start and hold session times. In three of four photo-inhibition
mice the stimulated or recorded hemisphere disagrees with Supplemental Table 1. The dandiset holds
more units than the paper reports, with no record of which were analysed. In the 40 sessions of the
2017 and 2018 mice the event times lie on a 10 ms grid, too coarse for the paper's millisecond
latencies. The CN recordings, lick times, lesion and behaviour-only sessions and anatomy are not in
the dandiset; the CN recordings are on Zenodo.
E
cat > $TMPDIR/dev/header_cn.md <<'E'
# Gao et al. (2018): the CN recordings, from Zenodo

**Paper.** Gao Z, Davis C, Thomas AM, Economo MN, Abrego AM, Svoboda K, De Zeeuw CI, Li N (2018). A
cortico-cerebellar loop for motor planning. *Nature* 563, 113-116.
[doi:10.1038/s41586-018-0633-x](https://doi.org/10.1038/s41586-018-0633-x). Full text of the author
manuscript (PMC6212318) and the publisher's Supplementary Information.

**Data.** Dandiset 000007 (version 0.220126.1903, see `reproduce_gao_2018.ipynb`) holds only the ALM
recordings. The CN recordings of Figures 2 and 3 and Extended Data Figures 3 to 6 are deposited on
Zenodo as NWB files in one zip archive, [doi:10.5281/zenodo.6647629](https://doi.org/10.5281/zenodo.6647629)
(`datafiles_NWB.zip`, 11.9 GB), found through CRCNS alm-6, which the paper's reporting summary names.
The archive is streamed with HTTP range requests and inflated in memory (`gao2018_cn.py`); the ALM
fraction of fig2-cn-preparatory-fraction is computed from the dandiset. The claims here are counted
apart from those on the dandiset.

**Method.** Trial selection, epochs and the selectivity and photo-inhibition analyses follow the
paper's CN scripts (`analyses_scripts.zip` in the MATLAB record doi:10.5281/zenodo.6653158).

| Claim | Status |
|---|---|
| fig2-cn-unit-counts | tested |
| fig2-cn-selective-fraction | tested |
| fig2-cn-preparatory-fraction | tested |
| fig2-cn-perimovement-fraction | tested |
| ed4e-cn-predict-movement | tested |
| ed4g-fn-contra-late-delay | tested |
| fig3b-cn-modulated-fraction | tested |
| fig3b-cn-net-increase | tested |
| fig3-cn-latency | tested |
| fig3c-cn-selectivity-abolished | tested |
| ed6-cn-either-hemisphere | tested |
| ed4c-lick-modulation | blocked, too large |

Streaming the archive takes most of the run, about 12 to 15 minutes.
E
cat > $TMPDIR/dev/summary_cn.md <<'E'
## Summary

A failure to reproduce here may be a failure of this attempt, not of the paper: see the reasoning
and the differences from the paper's method.

| Claim | Outcome |
|---|---|
| fig2-cn-unit-counts | not reproduced |
| fig2-cn-selective-fraction | not reproduced |
| fig2-cn-preparatory-fraction | partially reproduced |
| fig2-cn-perimovement-fraction | not reproduced |
| ed4e-cn-predict-movement | not reproduced |
| ed4g-fn-contra-late-delay | reproduced |
| fig3b-cn-modulated-fraction | not reproduced |
| fig3b-cn-net-increase | reproduced |
| fig3-cn-latency | not reproduced |
| fig3c-cn-selectivity-abolished | reproduced |
| ed6-cn-either-hemisphere | reproduced |
| ed4c-lick-modulation | blocked, too large |

**How the analysis differs from the paper's.** The Zenodo record holds more sessions (185 against
169) and more units (757 in the CN against 564) than the paper reports, and all of them are used.
With the scripts' rule of at least 30 correct trials of each type, used there for the population
analyses, the selective, preparatory and peri-movement fractions match the paper (0.757, 0.372 and
0.670), so the paper's counts likely rest on a trial-count selection the Methods do not state; the
outcomes are judged on all units, as the criteria fixed. The sessions of the 2016 mice have a 1.7 s
delay epoch.

**What was found.** The paper's direction results hold in these data: bilateral ALM photo-inhibition
removes most CN delay selectivity and increases more CN neurons than it decreases, and either ALM
hemisphere reduces it. The fractions of selective and modulated neurons are lower than the paper's
on the full set of units. One pair of units in one session (BAYLORNL10, 2017-05-03) has identical
spike trains.
E
python3 - <<'E'
for nbp, h, sm in (('/tmp/claude-1001/dev/nb_main.py','header_main.md','summary_main.md'),('/tmp/claude-1001/dev/nb_cn.py','header_cn.md','summary_cn.md')):
    s=open(nbp).read()
    hd=open('/tmp/claude-1001/dev/'+h).read().rstrip("\n"); su=open('/tmp/claude-1001/dev/'+sm).read().rstrip("\n")
    md=lambda t: "\n".join(("# "+l) if l else "#" for l in t.split("\n"))
    key = "# HEADER_CN" if "HEADER_CN" in s else "# HEADER"
    s=s.replace(key, md(hd), 1)
    s=s.rstrip("\n")+"\n\n# %% [markdown]\n"+md(su)+"\n"
    open(nbp,'w').write(s)
E
grep -n "HEADER" $TMPDIR/dev/nb_main.py $TMPDIR/dev/nb_cn.py; grep -n "—\|rather" $TMPDIR/dev/nb_main.py $TMPDIR/dev/nb_cn.py entries/000007-gao-2018/*.py | head
```

```
grep: entries/000007-gao-2018/*.py: No such file or directory
```

**Agent calls Bash**

```bash
cd  sed -i 's/takes about five minutes./takes about six minutes./' $TMPDIR/dev/nb_main.py; cat schemas/entry.schema.json | python3 -c "import json,sys;d=json.load(sys.stdin);print(json.dumps(d['properties'],indent=0)[:2500])"
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
[... 71 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/000007-gao-2018; cat > entry.yaml <<'E'
schema_version: 1
name: 000007-gao-2018
type: reproduction
title: ALM and cerebellar nuclei during motor planning (Gao et al. 2018)
description: Tests the findings of Gao, Davis, Thomas, Economo, Abrego, Svoboda, De Zeeuw and Li (2018)
  on dandiset 000007, which holds ALM recordings in 13 mice during the delayed response task, with
  photo-activation of the fastigial or dentate nucleus or photo-inhibition of the CN. It tests the
  behavioural effects of the photostimulation in the recording sessions, ALM selectivity, the ALM
  response to CN photo-inhibition and photo-activation, and the coding direction. A second notebook
  tests the CN findings on the paper's CN recordings, streamed from Zenodo. Lesions, licking, the
  anatomy and the other behaviour sessions are not deposited.
license: Apache-2.0
notebooks:
- path: reproduce_gao_2018.ipynb
  title: Reproducing Gao et al. (2018) from dandiset 000007
  runtime_minutes: 6
- path: reproduce_gao_2018_cn.ipynb
  title: Gao et al. (2018), the CN recordings from Zenodo
  runtime_minutes: 15
helpers:
- gao2018.py
- gao2018_cn.py
related:
- id: dandi:000007/0.220126.1903
  relation: uses_data
- id: doi:10.1038/s41586-018-0633-x
  relation: reproduces
- id: doi:10.5281/zenodo.6647629
  relation: uses_data
E
cat > requirements.in <<'E'
dandi
h5py
matplotlib
numpy
pandas
remfile
requests
scikit-learn
scipy
statsmodels
E
. $TMPDIR/explore/bin/activate; python $TMPDIR/dev/build.py $TMPDIR/dev/nb_main.py reproduce_gao_2018.ipynb; python $TMPDIR/dev/build.py $TMPDIR/dev/nb_cn.py reproduce_gao_2018_cn.ipynb; ls; cd ../..; pip list 2>/dev/null | grep -i "jsonschema\|nbformat\|pyyaml" ; python3 tools/entry.py lock entries/000007-gao-2018 && python3 tools/entry.py check entries/000007-gao-2018
```

```
__pycache__
entry.yaml
gao2018.py
gao2018_cn.py
reproduce_gao_2018.ipynb
reproduce_gao_2018_cn.ipynb
requirements.in
fastjsonschema            2.22.2
jsonschema                4.26.0
jsonschema-specifications 2025.9.1
nbformat                  5.11.1
PyYAML                    6.0.3
wrote entries/000007-gao-2018/requirements.lock.txt
0 error(s)
```

**Agent**

Check passes. Running the entry from a clean environment (both notebooks, about 20 to 25 min).

**Agent calls Bash**

```bash
cd  rm -rf entries/000007-gao-2018/__pycache__; time python3 tools/entry.py all entries/000007-gao-2018 2>&1 | tail -30
```

```
Installed kernelspec registry-000007-gao-2018 in executed/000007-gao-2018/.venv/share/jupyter/kernels/registry-000007-gao-2018
0 error(s)
pass  reproduce_gao_2018.ipynb  (349 s)
pass  reproduce_gao_2018_cn.ipynb  (706 s)

real	17m47.978s
user	10m21.700s
sys	0m26.226s
```

**Agent**

Both notebooks pass (349 s and 706 s). Checking that the executed outputs match the numbers in the conclusions.

**Agent calls Bash**

```bash
cd  python3 - <<'E'
import nbformat
for name in ("reproduce_gao_2018.ipynb","reproduce_gao_2018_cn.ipynb"):
    nb=nbformat.read(f"executed/000007-gao-2018/{name}",4)
    out=[]
    for c in nb.cells:
        if c.cell_type!="code": continue
        out.append("######## CELL "+str(c.metadata.get("tags",[])))
        for o in c.get("outputs",[]):
            if o.get("output_type")=="stream" and o.get("name")=="stdout": out.append(o["text"].rstrip("\n"))
            elif o.get("output_type")=="error": out.append("ERROR "+o["ename"])
    open(f"/tmp/claude-1001/dev/exec_{name}.txt","w").write("\n".join(out)+"\n")
E
cd $TMPDIR/dev; diff <(grep -v "^loaded\|in [0-9.]* s$" out_main.txt) <(grep -v "^loaded" exec_reproduce_gao_2018.ipynb.txt) | head -40; echo ====; diff out_cn.txt exec_reproduce_gao_2018_cn.ipynb.txt | head -40
```

```
1d0
< 
3d1
< 
58d55
< 
94d90
< 
114d109
< 
136d130
< 
144d137
< 
172d164
< 
185d176
< 
189d179
< 
[... 62 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/dev; diff <(grep -v "^loaded\|^$" out_main.txt) <(grep -v "^loaded\|^$" exec_reproduce_gao_2018.ipynb.txt); echo ====; diff <(grep -v "^$" out_cn.txt) <(grep -v "^$" exec_reproduce_gao_2018_cn.ipynb.txt)
```

```
====
3c3
< streamed and parsed 185 files in 12.2 min (16.2 MB/s over 32 connections)
---
> streamed and parsed 185 files in 9.6 min (20.6 MB/s over 32 connections)
150a151,153
> ######## CELL ['claim:ed4c-lick-modulation']
> MATLAB data files of doi:10.5281/zenodo.6653158: [('datafiles_4_of_4.zip', 9.27), ('datafiles_1_of_4.zip', 11.44), ('datafiles_2_of_4.zip', 8.59), ('datafiles_3_of_4.zip', 9.26)]
> total 38.6 GB; at the 20.6 MB/s measured here, 31 min to fetch, against the 30 min limit for a notebook
```

**Agent**

The lick-trace record is borderline (31 min at the measured rate). The zips may separate processed files from raw voltage, so I'll list their contents before blocking the claim.

**Agent calls Bash**

```bash
cd $TMPDIR; . explore/bin/activate; python - <<'E'
import requests, io, zipfile, collections, re
rec=requests.get("https://zenodo.org/api/records/6653158").json()
s=requests.Session()
class RF(io.RawIOBase):
    def __init__(s_,u,n): s_.u=u; s_.n=n; s_.p=0
    def seekable(s_): return True
    def readable(s_): return True
    def seek(s_,o,w=0): s_.p = o if w==0 else (s_.p+o if w==1 else s_.n+o); return s_.p
    def tell(s_): return s_.p
    def readinto(s_,b):
        if s_.p>=s_.n: return 0
        e=min(s_.p+len(b),s_.n)-1; d=s.get(s_.u,headers={'Range':f'bytes={s_.p}-{e}'}).content; b[:len(d)]=d; s_.p+=len(d); return len(d)
for f in rec['files']:
    if not f['key'].startswith('datafiles_'): continue
    z=zipfile.ZipFile(io.BufferedReader(RF(f['links']['self'],f['size']),buffer_size=1<<20))
    inf=z.infolist(); kinds=collections.defaultdict(lambda:[0,0])
    for i in inf:
        k=re.sub(r'[0-9_]+','#',i.filename)[:70]; kinds[k][0]+=1; kinds[k][1]+=i.compress_size
    print(f['key'], len(inf)); 
    for k,v in sorted(kinds.items(), key=lambda kv:-kv[1][1])[:8]: print('   ',k,v[0],round(v[1]/1e9,2),'GB')
E
```

```
datafiles_4_of_4.zip 52
    datafiles#of#/data#structure#BAYLORNL#.mat 26 9.27 GB
    datafiles#of#/meta#data#BAYLORNL#.mat 26 0.0 GB
datafiles_1_of_4.zip 196
    datafiles#of#/data#structure#BAYLORNL#.mat 49 9.65 GB
    datafiles#of#/data#structure#BAYLORCD#.mat 20 0.97 GB
    datafiles#of#/data#structure#ANM#.mat 22 0.51 GB
    datafiles#of#/data#structure#BAYLORDJ#.mat 5 0.24 GB
    datafiles#of#/data#structure#ANM#pene#.mat 2 0.08 GB
    datafiles#of#/meta#data#BAYLORNL#.mat 49 0.0 GB
    datafiles#of#/meta#data#ANM#.mat 22 0.0 GB
    datafiles#of#/meta#data#BAYLORCD#.mat 20 0.0 GB
datafiles_2_of_4.zip 60
    datafiles#of#/data#structure#BAYLORNL#.mat 30 8.59 GB
    datafiles#of#/meta#data#BAYLORNL#.mat 30 0.0 GB
datafiles_3_of_4.zip 62
    datafiles#of#/data#structure#BAYLORNL#.mat 31 9.26 GB
    datafiles#of#/meta#data#BAYLORNL#.mat 31 0.0 GB
Shell cwd was reset to
```

**Agent calls Bash**

```bash
curl -sL "https://crcns.org/news" | sed 's/<[^>]*>/ /g' | tr -s ' \n' | grep -i -A8 "AWS" | head -30; curl -sL "https://crcns.org/data-sets/motor-cortex/alm-4" | sed 's/<[^>]*>/ /g' | tr -s ' \n' | grep -i -B2 -A6 "download\|aws\|s3" | head -40
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
curl -sL "https://crcns.org/news/data-now-downloaded-through-aws" | sed 's/<[^>]*>/ /g' | tr -s ' \n' | grep -i -A25 "Data now downloaded through AWS" | sed -n '20,80p'; curl -sL "https://crcns.org/download" | sed 's/<[^>]*>/ /g' | tr -s ' \n' | grep -i -A20 "account\|login\|aws\|s3" | head -40
```

Result: the fetched text is not kept.

**Agent**

CRCNS requires an account, so the ALM lick traces cannot be fetched by a notebook; ed4c will be blocked as not runnable, with a cell showing the Zenodo MATLAB zips hold only CN mice.

**Agent calls Bash**

```bash
cd entries/000007-gao-2018; python3 - <<'E'
p='gao2018_cn.py'; s=open(p).read()
rep=[('''def get_range(a: int, b: int, attempts: int = 8) -> bytes:
    """Bytes a to b (inclusive) of the archive, waiting out the rate limit."""
    for k in range(attempts):
        try:
            r = _session().get(ZIP_URL, headers={"Range": f"bytes={a}-{b}"}, timeout=600)''','''def get_range(a: int, b: int, attempts: int = 8, url: str = ZIP_URL) -> bytes:
    """Bytes a to b (inclusive) of the archive, waiting out the rate limit."""
    for k in range(attempts):
        try:
            r = _session().get(url, headers={"Range": f"bytes={a}-{b}"}, timeout=600)'''),
('''    raise RuntimeError(f"could not fetch bytes {a}-{b} of {ZIP_URL}")''','''    raise RuntimeError(f"could not fetch bytes {a}-{b} of {url}")'''),
('''    def __init__(self, size):
        self.size, self.pos = size, 0''','''    def __init__(self, size, url):
        self.size, self.pos, self.url = size, 0, url'''),
('''        d = get_range(self.pos, end)''','''        d = get_range(self.pos, end, url=self.url)'''),
('''def archive_entries() -> list[zipfile.ZipInfo]:
    size = int(requests.head(ZIP_URL, allow_redirects=True, timeout=60).headers["Content-Length"])
    z = zipfile.ZipFile(io.BufferedReader(_RangeFile(size), buffer_size=1 << 20))
    return [i for i in z.infolist() if i.filename.endswith(".nwb")]''','''def archive_entries(url: str = ZIP_URL, suffix: str = ".nwb") -> list[zipfile.ZipInfo]:
    """The files of a zip archive on Zenodo, read from its central directory with range requests."""
    size = int(requests.head(url, allow_redirects=True, timeout=60).headers["Content-Length"])
    z = zipfile.ZipFile(io.BufferedReader(_RangeFile(size, url), buffer_size=1 << 20))
    return [i for i in z.infolist() if i.filename.endswith(suffix)]''')]
for a,b in rep:
    assert a in s, a[:50]; s=s.replace(a,b)
open(p,'w').write(s)
p='/tmp/claude-1001/dev/nb_cn.py'; s=open(p).read()
start=s.index("# %% [markdown]\n# ## ed4c-lick-modulation (blocked)"); end=s.index("# %% [markdown]\n# ## Summary")
new='''# %% [markdown]
# ## ed4c-lick-modulation (blocked)
#
# > In ALM and CN a similar small proportion (below 10%) of neurons modulated their spike rates
# > during individual licks.
#
# The dandiset has no lick times. The data description of the Zenodo records says the MATLAB format
# holds tongue movement traces, and that the ALM sessions are on CRCNS (alm-4,
# doi:10.6080/K0NS0S26), not in this release. The MATLAB record's data files, listed here from
# their zip directories, hold only the mice of the CN recordings:

# %% tags=["claim:ed4c-lick-modulation"]
import re
import requests
rec = requests.get("https://zenodo.org/api/records/6653158", timeout=60).json()
alm_mice = sorted({s["subject"].upper().replace("ANM00", "ANM") for s in alm_sessions})
for f in sorted(rec["files"], key=lambda f: f["key"]):
    if not f["key"].startswith("datafiles_"):
        continue
    names = [i.filename for i in cn.archive_entries(f["links"]["self"], ".mat")]
    mice = sorted({m.group(1).upper() for n in names if (m := re.search(r"data_structure_([A-Za-z]+\\d+)_", n))})
    print(f"{f['key']} ({f['size'] / 1e9:.1f} GB): {len(names)} .mat files; mice {mice}")
    print("   ALM mice of the dandiset among them:", sorted(set(mice) & set(alm_mice)))
print("\\nALM mice of the dandiset:", alm_mice)

# %% [markdown]
# None of the dandiset's ALM mice is in the MATLAB record, so the ALM lick traces are only on CRCNS
# alm-4. CRCNS requires an account to download, which a notebook run by the registry cannot use. The
# claim, which compares ALM and CN, is blocked as not runnable here.

'''
s=s[:start]+new+s[end:]
open(p,'w').write(s)
E
grep -n "6653158\|datafiles_" $TMPDIR/dev/nb_cn.py | head
```

```
12:# (`datafiles_NWB.zip`, 11.9 GB), found through CRCNS alm-6, which the paper's reporting summary names.
18:# paper's CN scripts (`analyses_scripts.zip` in the MATLAB record doi:10.5281/zenodo.6653158).
563:rec = requests.get("https://zenodo.org/api/records/6653158", timeout=60).json()
566:    if not f["key"].startswith("datafiles_"):
```

**Agent calls Bash**

```bash
cd entries/000007-gao-2018; sed -i 's/| ed4c-lick-modulation | elsewhere (Zenodo) | blocked, too large | CN |/| ed4c-lick-modulation | elsewhere (CRCNS) | blocked, not runnable | CN |/' $TMPDIR/dev/nb_main.py; sed -i 's/| ed4c-lick-modulation | blocked, too large |/| ed4c-lick-modulation | blocked, not runnable |/' $TMPDIR/dev/nb_cn.py; grep -n "ed4c" $TMPDIR/dev/nb_main.py $TMPDIR/dev/nb_cn.py | head; . $TMPDIR/explore/bin/activate; python - <<'E' 2>&1 | grep -v Warn
import pickle, gao2018_cn as cn
alm_sessions=pickle.load(open('/tmp/claude-1001/S.pkl','rb'))
src=open('/tmp/claude-1001/dev/nb_cn.py').read()
cell=src.split('# %% tags=["claim:ed4c-lick-modulation"]')[1].split("# %% [markdown]")[0]
exec(cell)
E
```

```
/tmp/claude-1001/dev/nb_main.py:54:# | ed4c-lick-modulation | elsewhere (CRCNS) | blocked, not runnable | CN |
/tmp/claude-1001/dev/nb_cn.py:33:# | ed4c-lick-modulation | blocked, not runnable |
/tmp/claude-1001/dev/nb_cn.py:550:# ## ed4c-lick-modulation (blocked)
/tmp/claude-1001/dev/nb_cn.py:560:# %% tags=["claim:ed4c-lick-modulation"]
/tmp/claude-1001/dev/nb_cn.py:598:# | ed4c-lick-modulation | blocked, not runnable |
datafiles_1_of_4.zip (11.4 GB): 196 .mat files; mice ['ANM344651', 'ANM344652', 'ANM344653', 'ANM350830', 'ANM350831', 'BAYLORCD1', 'BAYLORCD2', 'BAYLORDJ1', 'BAYLORNL1', 'BAYLORNL2', 'BAYLORNL3', 'BAYLORNL4']
   ALM mice of the dandiset among them: []
datafiles_2_of_4.zip (8.6 GB): 60 .mat files; mice ['BAYLORNL6', 'BAYLORNL7']
   ALM mice of the dandiset among them: []
datafiles_3_of_4.zip (9.3 GB): 62 .mat files; mice ['BAYLORNL8', 'BAYLORNL9']
   ALM mice of the dandiset among them: []
datafiles_4_of_4.zip (9.3 GB): 52 .mat files; mice ['BAYLORNL10', 'BAYLORNL11']
   ALM mice of the dandiset among them: []

ALM mice of the dandiset: ['ANM314746', 'ANM314756', 'ANM314757', 'ANM314758', 'ANM314760', 'BAYLORCD12', 'BAYLORCD13', 'BAYLORCD14', 'BAYLORCD6', 'BAYLORCD8', 'BAYLORNL12', 'BAYLORNL14', 'BAYLORNL15']
```

**Agent**

Now the attempt record. Checking the attempt schema first.

**Agent calls Bash**

```bash
cd  python3 -c "
import json;d=json.load(open('schemas/attempt.schema.json'));p=d['properties']
print(list(p)); print(json.dumps(p['outcomes']['items'],indent=0)[:3000]); print(json.dumps(p['findings'],indent=0)[:1500]); print(json.dumps(p['inputs'],indent=0)[:800]); print(d.get('required'))"
```

```
['schema_version', 'id', 'dandiset', 'dandiset_version', 'paper', 'date', 'entry', 'provenance', 'outcomes', 'verifications', 'findings', 'inputs']
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
[... 159 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python3 - <<'E'
p='claims/000007/10.1038-s41586-018-0633-x.yaml'; s=open(p).read()
old='''  where: Zenodo doi:10.5281/zenodo.6653158 (MATLAB datafiles, with the lick traces of the ALM
    sessions)'''
new='''  where: CRCNS alm-4 doi:10.6080/K0NS0S26 (the ALM sessions in MATLAB format, with tongue
    movement traces by the Zenodo data description), and Zenodo doi:10.5281/zenodo.6647629 for the
    CN sessions'''
assert old in s; s=s.replace(old,new); open(p,'w').write(s)
E
echo ok
```

```
ok
```

**Agent calls Write**

```json
{
 "file_path": "attempts/000007-gao-2018-01.yaml",
 "content": "schema_version: 1\nid: 000007-gao-2018-01\ndandiset: \"000007\"\ndandiset_version: 0.220126.1903\npaper: doi:10.1038/s41586-018-0633-x\ndate: 2026-10-19\nentry: 000007-gao-2018\nprovenance:\n  kind: agent\n  accountable:\n    name: CatalystNeuro\n  agent:\n    harness: Claude Code (GitHub Actions)\n    model: claude-opus-5-5\n    protocol: pilot-7\ninputs:\n- what: Names of the photostimulation codes 1 to 6 (and 7 to 10 of the CN files), from the data\n    description `data description_ALM4_ver2022.pdf` of the paper's Zenodo records.\n  source: doi:10.5281/zenodo.6647629 (also in doi:10.5281/zenodo.6653158)\n- what: The CN recordings, 185 NWB files in `datafiles_NWB.zip` (md5 fb41644843d71b3d0c078f76b1e6c227),\n    streamed with range requests for the claims on data elsewhere.\n  source: doi:10.5281/zenodo.6647629\n- what: The paper's CN analysis scripts (`analyses_scripts.zip`, md5 c37151c75a1e440ba7f07b21f304d360,\n    read and followed for trial selection, epochs and the selectivity and photo-inhibition analyses),\n    and the list of the record's MATLAB data files, read from their zip directories.\n  source: doi:10.5281/zenodo.6653158\n- what: Supplemental Table 1 of the paper's Supplementary Information (mice and hemispheres of each\n    experiment), compared with the files' metadata.\n  source: doi:10.1038/s41586-018-0633-x\noutcomes:\n- claim: stim-code-link\n  outcome: reproduced\n  notebook: reproduce_gao_2018.ipynb\n  output: claim:stim-code-link\n  notes: Codes are matched by integer value. Codes 1 and 2 occur only in the 6 fastigial mice, 3 and\n    4 only in the 3 dentate mice, 5 and 6 only in the 4 L7-cre mice. The ALM change first exceeds the\n    pre-trial level by 4 SD 15 ms (codes 1, 2), 5 ms (3, 4) and 35 ms (5, 6) after the onset the\n    names imply, with no bin above it before. The change 0.7 to 1.2 s after onset is 0.95 spikes/s\n    for code 5 and 1.64 for code 6.\n- claim: methods-alm-unit-counts\n  outcome: not_reproduced\n  notebook: reproduce_gao_2018.ipynb\n  output: claim:methods-alm-unit-counts\n  measured:\n  - 1112\n  - 567\n  - 545\n  - 737\n  - 706\n  - 20\n  notes: Under the files' labels (reading a) only the session count is within tolerance; the width\n    rule (reading b) gives 1082, 557, 525, 737, 676 and 20, also one of six. The 9 photo-activation\n    mice hold 1186 units, against the paper's 1309 for 10 mice. With at least 30 correct control\n    trials of each type, 961 pyramidal neurons of the photo-activation mice remain.\n  deviations:\n  - The dandiset lacks the tenth ALM mouse (excluded from Figure 4 for a missed injection) that the\n    paper's totals of 1309 and 1194 include.\n- claim: fig1g-fn-delay-performance\n  outcome: reproduced\n  notebook: reproduce_gao_2018.ipynb\n  output: claim:fig1g-fn-delay-performance\n  notes: Six fastigial mice, performance 0.873 on control and 0.630 on code 2 trials (change -0.243,\n    95% interval -0.388 to -0.101, one-tailed hierarchical bootstrap p = 0.0001); lower in all six\n    mice (-0.083 to -0.450).\n  deviations:\n  - Trials of the recording sessions only; the paper's Figure 1g may include behaviour-only sessions,\n    which are not deposited.\n- claim: fig1-fn-sample-no-effect\n  outcome: reproduced\n  notebook: reproduce_gao_2018.ipynb\n  output: claim:fig1-fn-sample-no-effect\n  notes: Code 1 changes performance by -0.034 on contralateral (p = 0.365) and +0.024 on\n    ipsilateral trials (p = 0.253).\n  deviations:\n  - Recording sessions only.\n- claim: fig1g-dn-little-effect\n  outcome: reproduced\n  notebook: reproduce_gao_2018.ipynb\n  output: claim:fig1g-dn-little-effect\n  notes: Code 4 changes performance from 0.873 to 0.835 (-0.038, 95% interval -0.091 to +0.027,\n    one-tailed p = 0.108) in three dentate mice.\n  deviations:\n  - The dandiset holds 0.5 s delay photostimulation in 3 dentate mice; Figure 1g uses 1.3 s\n    photostimulation in 8 mice (Supplemental Table 1).\n- claim: fig1h-fn-delay-bias-either-direction\n  outcome: reproduced\n  notebook: reproduce_gao_2018.ipynb\n  output: claim:fig1h-fn-delay-bias-either-direction\n  notes: Two mice are pushed to ipsilateral licking (BAYLORNL15 bias +0.68, anm00314760 +0.76, both\n    p < 0.0001) and one to contralateral licking (anm00314746, -0.49, p = 0.0006); three show no\n    significant bias (p 0.48 to 0.63).\n  deviations:\n  - 0.5 s delay photostimulation in the recording sessions; Figure 1h shows these and 1.3 s\n    photostimulation in other mice.\n- claim: ed1f-fn-no-early-licks\n  outcome: reproduced\n  notebook: reproduce_gao_2018.ipynb\n  output: claim:ed1f-fn-no-early-licks\n  notes: Early-lick rate 0.079 on control and 0.127 on code 2 trials (increase +0.049, 95% interval\n    -0.026 to +0.163, one-tailed p = 0.174). In one mouse (BAYLORCD6) it rises from 0.081 to 0.324.\n    The no-lick rate rises from 0.018 to 0.11, a variant not tested.\n  deviations:\n  - The paper gives no test; the hierarchical bootstrap was fixed before the analysis.\n  - Recording sessions with 0.5 s photostimulation; Extended Data Figure 1f is from 1.3 s\n    photostimulation in other mice.\n- claim: fig1k-pi-delay-performance\n  outcome: reproduced\n  notebook: reproduce_gao_2018.ipynb\n  output: claim:fig1k-pi-delay-performance\n  notes: Codes 5 and 6 lower performance from 0.848 to 0.693 (change -0.155, 95% interval -0.245 to\n    -0.067, p < 0.0001); code 5 alone -0.142 (p = 0.012), code 6 alone -0.171 (p < 0.0001); lower in\n    all four mice for both codes.\n  deviations:\n  - 4 of the 7 mice of Figure 1k, recording sessions only.\n- claim: fig1d-fn-lesion\n  outcome: blocked\n  blocked_by: data_missing\n  notes: The lesion sessions are not in the dandiset, nor in the Zenodo records, which hold only ALM\n    and CN recordings by their data description; CRCNS alm-6 points to the same records.\n- claim: fig1e-lesion-lick-timing\n  outcome: blocked\n  blocked_by: data_missing\n  notes: Needs the lesion sessions and lick times, neither in the dandiset nor in the Zenodo\n    records.\n- claim: fig1h-response-contra-bias\n  outcome: blocked\n  blocked_by: data_missing\n  notes: The dandiset has no response-epoch photostimulation (codes 1 to 4 are sample and delay);\n    the 1.3 s photo-activation sessions of Supplemental Table 1 are not deposited.\n- claim: fig1i-licking-unaffected\n  outcome: blocked\n  blocked_by: data_missing\n  notes: The dandiset has no lick times, and the behaviour sessions of Figure 1i and 1l are not\n    deposited in the dandiset or the Zenodo records.\n- claim: fig1k-response-ipsi-bias\n  outcome: blocked\n  blocked_by: data_missing\n  notes: The dandiset has only delay photo-inhibition (codes 5 and 6); the sample and response\n    epoch sessions of Figure 1k are not deposited.\n- claim: ed2-pi-silences-fastigial\n  outcome: blocked\n  blocked_by: data_missing\n  notes: The fastigial recordings in L7-cre x Ai32 mice (60 units, 2 mice) and the movement videos\n    are not in the dandiset; the Zenodo CN record holds the 18 mice of the CN recordings during the\n    task, none of them L7-cre.\n- claim: fig2-alm-selective-fraction\n  outcome: reproduced\n  notebook: reproduce_gao_2018.ipynb\n  output: claim:fig2-alm-selective-fraction\n  measured: 0.779\n  notes: Both readings match; (a) 866 of 1112 (0.779), given as measured, (b) 1365 of 1818 (0.751).\n    The chance level of the test with shuffled trial types is 0.121. With at least 30 correct\n    control trials of each type, 0.834 under reading (a).\n  deviations:\n  - The dandiset holds more units than the paper reports and does not mark the paper's; all units\n    labelled pyramidal are used.\n  - The selection of trials marked as not performing in the paper's scripts (GoodTrials) cannot be\n    applied; the dandiset has no such column.\n- claim: fig2-alm-preparatory-fraction\n  outcome: reproduced\n  notebook: reproduce_gao_2018.ipynb\n  output: claim:fig2-alm-preparatory-fraction\n  measured: 0.558\n  notes: Reading (a) matches (621 of 1112, 0.558); reading (b) does not (0.525). As a fraction of\n    selective neurons, 0.717. With at least 30 correct trials of each type, 0.608.\n  deviations:\n  - As for fig2-alm-selective-fraction.\n- claim: fig2-alm-perimovement-fraction\n  outcome: reproduced\n  notebook: reproduce_gao_2018.ipynb\n  output: claim:fig2-alm-perimovement-fraction\n  measured: 0.629\n  notes: Reading (a) matches (0.629); reading (b) does not (0.596). With at least 30 correct trials\n    of each type, 0.680.\n  deviations:\n  - As for fig2-alm-selective-fraction.\n- claim: fig2c-alm-selectivity-time-course\n  outcome: partially_reproduced\n  notebook: reproduce_gao_2018.ipynb\n  output: claim:fig2c-alm-selectivity-time-course\n  notes: 838 selective neurons. Selectivity in the last 300 ms of the sample is 1.19 spikes/s (95%\n    interval 0.99 to 1.42), so part (1) holds; the maximum (2.53 spikes/s) is at 2.54 s after pole in,\n    just before the cue, and the response-epoch mean (0.96) is below the delay mean (2.09), so part\n    (2) fails. With the preferred type from the response epoch the maximum is at 3.09 s, in the\n    response epoch.\n  deviations:\n  - The criterion defined only the reproduced level; with one of its two parts holding, the outcome\n    is partially reproduced by the protocol's definition.\n  - The preferred type is chosen from the delay epoch, a choice the Methods leave open.\n- claim: fig2-cn-unit-counts\n  outcome: not_reproduced\n  notebook: reproduce_gao_2018_cn.ipynb\n  output: claim:fig2-cn-unit-counts\n  measured:\n  - 1212\n  - 455\n  - 377\n  - 178\n  - 202\n  - 185\n  notes: Only the session count is within tolerance. The record has 757 CN units against the\n    Results' 564; 457 CN units have at least 30 correct control trials of each type.\n- claim: fig2-cn-selective-fraction\n  outcome: not_reproduced\n  notebook: reproduce_gao_2018_cn.ipynb\n  output: claim:fig2-cn-selective-fraction\n  measured: 0.592\n  notes: 448 of 757 CN units are selective (chance level of the test 0.127). With the scripts' rule of\n    at least 30 correct control trials of each type, 457 units and a fraction of 0.757, within\n    tolerance, so the difference likely comes from a unit selection the Methods do not state.\n  deviations:\n  - All units of the record are used; it holds more units and sessions than the paper reports.\n- claim: fig2-cn-preparatory-fraction\n  outcome: partially_reproduced\n  notebook: reproduce_gao_2018_cn.ipynb\n  output: claim:fig2-cn-preparatory-fraction\n  measured: 0.269\n  notes: ALM 0.558 (dandiset, reading a) against CN 0.269 (204 of 757), chi-square p = 8.7e-35, so the\n    comparison holds; the CN fraction is outside 0.35 +/- 0.035. With at least 30 correct trials of\n    each type, 0.372.\n  deviations:\n  - As for fig2-cn-selective-fraction.\n- claim: fig2-cn-perimovement-fraction\n  outcome: not_reproduced\n  notebook: reproduce_gao_2018_cn.ipynb\n  output: claim:fig2-cn-perimovement-fraction\n  measured: 0.511\n  notes: CN 0.511 against ALM 0.629 (chi-square p = 5.7e-07), where the paper finds them equal. With\n    at least 30 correct trials of each type, 0.670, within tolerance.\n  deviations:\n  - As for fig2-cn-selective-fraction.\n- claim: ed4e-cn-predict-movement\n  outcome: not_reproduced\n  notebook: reproduce_gao_2018_cn.ipynb\n  output: claim:ed4e-cn-predict-movement\n  measured:\n  - 0.496\n  - 117\n  notes: 117 delay-selective CN neurons with more than 3 error trials of each type; 0.496 have a\n    negative error to correct selectivity ratio (median ratio 0.02).\n  deviations:\n  - All units of the record are used.\n- claim: ed4g-fn-contra-late-delay\n  outcome: reproduced\n  notebook: reproduce_gao_2018_cn.ipynb\n  output: claim:ed4g-fn-contra-late-delay\n  notes: Late delay, mean contralateral fraction per mouse 0.650 (13 mice, one-tailed p = 0.033);\n    early delay 0.639 (11 mice, two-tailed p = 0.219). The paper's p = 0.0001 is not matched.\n  deviations:\n  - The paper does not say which fastigial neurons enter the proportions; neurons significant in each\n    window were used, as fixed in the criterion. 13 mice have such neurons, against 15 in the figure.\n- claim: ed4c-lick-modulation\n  outcome: blocked\n  blocked_by: not_runnable\n  notes: The dandiset has no lick times. The Zenodo MATLAB record holds only the 18 CN mice (its zip\n    directories, listed in the CN notebook, contain none of the 13 ALM mice); the ALM sessions with\n    their tongue traces are on CRCNS alm-4 (doi:10.6080/K0NS0S26), which requires an account to\n    download, so a notebook run by the registry cannot fetch them.\n- claim: fig3b-cn-modulated-fraction\n  outcome: not_reproduced\n  notebook: reproduce_gao_2018_cn.ipynb\n  output: claim:fig3b-cn-modulated-fraction\n  measured: 0.28\n  notes: 145 of 517 tested CN units (563 in sessions with code 9, against 389) are modulated at p <\n    0.01; 0.412 at p < 0.05. By nucleus 0.435 dentate, 0.178 fastigial, 0.186 interposed.\n  deviations:\n  - All units of the record are used.\n- claim: fig3b-cn-net-increase\n  outcome: reproduced\n  notebook: reproduce_gao_2018_cn.ipynb\n  output: claim:fig3b-cn-net-increase\n  measured: 0.69\n  notes: 100 of 145 modulated units increase (binomial p = 5.7e-06). The modulated set itself differs\n    from the paper's (fig3b-cn-modulated-fraction).\n- claim: fig3-cn-latency\n  outcome: not_reproduced\n  notebook: reproduce_gao_2018_cn.ipynb\n  output: claim:fig3-cn-latency\n  measured: 0.2\n  notes: First-crossing onset 0.2 +/- 13.7 ms, with 47% of resampled onsets before the photostimulus;\n    the population change is 1.14 spikes/s at -10 ms, 0.29 at 5 ms and 3.16 at 15 ms. The sustained\n    onset (10 consecutive bins) is 14.3 +/- 2.0 ms. 96% of pole-out times in these sessions lie on a\n    10 ms grid.\n  deviations:\n  - The search window (20 ms before to 100 ms after onset) and bin centre are choices made here.\n- claim: fig3c-cn-selectivity-abolished\n  outcome: reproduced\n  notebook: reproduce_gao_2018_cn.ipynb\n  output: claim:fig3c-cn-selectivity-abolished\n  notes: 137 neurons (against 157); delay selectivity 3.73 spikes/s on control and 0.68 on code 9\n    trials, ratio 0.18 (p < 0.0001). Fastigial 0.01, dentate 0.96, interposed 1.15 spikes/s on\n    photo-inhibition trials.\n- claim: ed6-cn-either-hemisphere\n  outcome: reproduced\n  notebook: reproduce_gao_2018_cn.ipynb\n  output: claim:ed6-cn-either-hemisphere\n  notes: Left ALM 3.48 to 1.29 spikes/s (154 units, p < 0.0001), right ALM 3.37 to 1.56 (152 units,\n    p = 0.0002). Bilateral M1, a variant, 3.62 to 1.84 (ratio 0.51, p = 0.019).\n- claim: fig3e-alm-modulated-fraction\n  outcome: reproduced\n  notebook: reproduce_gao_2018.ipynb\n  output: claim:fig3e-alm-modulated-fraction\n  measured: 0.429\n  notes: Reading (b), codes 5 and 6, matches (298 of 695, 0.429); reading (a), code 6, does not (234\n    of 643, 0.364). The test's false-positive rate on split control trials is 0.01. By mouse 0.18 to\n    0.44.\n  deviations:\n  - The Methods state a 1.3 s photostimulus; the files hold 0.5 s and 1.3 s trials, and the\n    readings fixed in the criterion cover both.\n  - All units labelled pyramidal are used; the dandiset holds 706 in these mice against 454.\n- claim: fig3e-alm-mean-rate-unchanged\n  outcome: reproduced\n  notebook: reproduce_gao_2018.ipynb\n  output: claim:fig3e-alm-mean-rate-unchanged\n  measured:\n  - 4.46\n  - 4.8\n  notes: Two-sample t-test p = 0.379 over 643 neurons; paired test p = 0.151; codes 5 and 6 pooled\n    4.45 against 4.94 (p = 0.187).\n  deviations:\n  - The paper does not say whether its t-test is paired; the two-sample test was fixed before the\n    analysis and the paired one shown.\n- claim: fig3e-alm-up-down\n  outcome: reproduced\n  notebook: reproduce_gao_2018.ipynb\n  output: claim:fig3e-alm-up-down\n  measured: 0.577\n  notes: Reading (b), 172 of 298 increase; reading (a) 0.585. More increase than decrease (binomial p\n    = 0.009).\n- claim: fig3-alm-latency-pi\n  outcome: not_reproduced\n  notebook: reproduce_gao_2018.ipynb\n  output: claim:fig3-alm-latency-pi\n  measured: 16.6\n  notes: Under reading (b), the matching one, 16.6 +/- 12.9 ms. Under reading (a) 7.8 +/- 14.3 ms,\n    within tolerance, but 29% of its resampled onsets fall before the photostimulus. The population\n    change stays below 1 spikes/s until 25 ms after onset and rises between 30 and 40 ms; the\n    sustained onset is 29 to 32 ms for codes 5, 6 and both. All four mice's event times lie on a 10\n    ms grid.\n  deviations:\n  - The search window and bin centre are choices made here; the Methods do not give them.\n- claim: fig3f-alm-selectivity-abolished\n  outcome: reproduced\n  notebook: reproduce_gao_2018.ipynb\n  output: claim:fig3f-alm-selectivity-abolished\n  notes: 252 neurons (against 329); delay selectivity 2.04 spikes/s on control and 0.48 on code 6\n    trials, ratio 0.23; the remaining selectivity is above 0 (95% interval 0.21 to 0.76). Near zero\n    in two mice (0.08, -0.02), 0.71 and 0.73 in the other two. Codes 5 and 6 pooled give 0.36.\n- claim: ed9a-fn-latency\n  outcome: partially_reproduced\n  notebook: reproduce_gao_2018.ipynb\n  output: claim:ed9a-fn-latency\n  measured:\n  - 2.0\n  - 187\n  notes: Reading (a), given as measured, has the latency within tolerance and the count outside it;\n    reading (b) has 248 neurons (within) and -0.9 +/- 11.9 ms (outside). 24% of reading (a)'s\n    resampled onsets fall before the photostimulus. The sustained onset is 6.7 +/- 2.3 ms and the 2015\n    files alone, with precise event times, give 9.5 +/- 6.0 ms.\n  deviations:\n  - The modulation window (0.5 s from onset), the search window and the bin centre are choices made\n    here.\n- claim: ed9a-dn-latency\n  outcome: not_reproduced\n  notebook: reproduce_gao_2018.ipynb\n  output: claim:ed9a-dn-latency\n  measured:\n  - -9.0\n  - 183\n  notes: Onsets -9.0 +/- 5.7 ms (code 4) and -12.2 +/- 4.5 ms (codes 3 and 4); 183 and 230 neurons\n    modulated. Over 96% of resampled onsets fall before the photostimulus; the change is 0.79 spikes/s\n    10 ms before onset and 1.31 at onset. 11 of 13 dentate sessions have event times on a 10 ms grid,\n    and the 2015 files have too few modulated neurons to measure an onset, so the data cannot place\n    the onset to a few milliseconds.\n  deviations:\n  - As for ed9a-fn-latency.\n- claim: fig4f-fn-persistent\n  outcome: reproduced\n  notebook: reproduce_gao_2018.ipynb\n  output: claim:fig4f-fn-persistent\n  notes: 78 of 538 neurons (0.145) differ from control 1.0 to 1.4 s after offset, against 5 of 538\n    (0.009) before onset (Fisher p = 2.3e-19); 0.361 during photostimulation.\n- claim: fig4g-dn-recovery\n  outcome: partially_reproduced\n  notebook: reproduce_gao_2018.ipynb\n  output: claim:fig4g-dn-recovery\n  notes: Dentate 0.051 in the post-offset bin, lower than fastigial 0.145 (Fisher p = 2e-07) and down\n    from 0.328 during photostimulation, but 2.3 times its 0.022 before onset, above the factor of 2.\n  deviations:\n  - The criterion defined only the reproduced level; with one of its two parts holding, the outcome\n    is partially reproduced by the protocol's definition.\n- claim: fig4i-fn-cd-collapse\n  outcome: reproduced\n  notebook: reproduce_gao_2018.ipynb\n  output: claim:fig4i-fn-cd-collapse\n  notes: 15 sessions; ratio 0.499 (95% interval 0.204 to 0.955), just under the criterion's 0.5. The\n    median per-session ratio is 0.602 and the mean 0.854; two of six mice show no collapse (2.45 and\n    1.27). Smaller separation in 11 of 15 sessions. The fastigial and dentate sessions together are\n    28, as in the Methods.\n  deviations:\n  - The scripts' stable-trial rule is not applied here, as requiring every trial to be stable for\n    every neuron left too few trials; all pyramidal neurons and usable trials of a session are used.\n- claim: fig4i-dn-cd-minimal\n  outcome: reproduced\n  notebook: reproduce_gao_2018.ipynb\n  output: claim:fig4i-dn-cd-minimal\n  notes: 13 sessions; ratio 1.04 (95% interval 0.87 to 1.20); the fastigial ratio is lower in 98.5% of\n    paired resamples.\n  deviations:\n  - As for fig4i-fn-cd-collapse.\n- claim: ed10d-fn-no-prediction\n  outcome: not_reproduced\n  notebook: reproduce_gao_2018.ipynb\n  output: claim:ed10d-fn-no-prediction\n  measured: 386\n  notes: On code 2 trials the projection still predicts licking right (slope 0.40, p = 0.00015, 386\n    trials), less than on held-out control trials (slope 1.44, p = 3e-63).\n  deviations:\n  - The paper gives no test; the logistic regression was fixed before the analysis.\n  - As for fig4i-fn-cd-collapse.\n- claim: ed10c-alm-pi-endpoints\n  outcome: blocked\n  blocked_by: data_missing\n  notes: The ALM recordings during bilateral ALM photo-inhibition (690 trials) are not in this\n    dandiset, which holds only CN photostimulation, or in the Zenodo records. The Supplementary\n    Information refers to earlier work of the lab for them and names no deposit.\n- claim: ed10efg-alm-needed-after-fn\n  outcome: blocked\n  blocked_by: data_missing\n  notes: The behaviour of the VGAT-ChR2 mice ZD02 to ZD05 is not in the dandiset or the Zenodo\n    records.\n- claim: fig4bc-fastigial-thalamus\n  outcome: blocked\n  blocked_by: data_missing\n  notes: The anatomy images are not in the dandiset or the Zenodo records; the paper offers data on\n    request.\nfindings:\n- kind: metadata_insufficient\n  statement: The trial column photo_stim_id (codes 0 to 6) has no description in the files or the\n    dandiset metadata. The codes can be named only from the data description of the paper's Zenodo\n    records (1 and 2 fastigial, 3 and 4 dentate photo-activation in the sample and delay, 5 and 6 CN\n    photo-inhibition for 0.5 and 1.3 s), and the ALM responses agree with those names.\n- kind: metadata_error\n  statement: The descriptions of pole_in_time, pole_out_time and cue_time say they are relative to the\n    trial start; the values are session times on the clock of the spike times (pole in follows\n    start_time by 0.57 s).\n- kind: metadata_error\n  statement: For three of the four L7-cre mice the sides disagree with Supplemental Table 1 (BAYLORCD12\n    and CD13 have a left fastigial site where the table has right CN; BAYLORCD14 has left ALM where\n    the table has right ALM), and in all three the files put ALM and the stimulation site on the same\n    side, against the Methods' statement that ALM recordings were always contralateral.\n- kind: metadata_error\n  statement: The L7-cre files describe the photostimulation site as the fastigial nucleus at 2.4 mm\n    depth, while the Methods photostimulate Purkinje cells through a cranial window at the surface of\n    the cerebellar cortex.\n- kind: selection_undocumented\n  statement: The dandiset holds more units than the paper analysed (1112 pyramidal neurons in the 9\n    photo-activation mice against 912, 737 units in the 4 L7-cre mice against 490) and 20 L7-cre\n    sessions against 19, with no mark of which units or sessions the paper used. The paper's\n    selection is not described; with the scripts' rule of 30 correct trials of each type the\n    selectivity fractions come close to the paper's.\n- kind: format_error\n  statement: In the 40 sessions of the 2017 and 2018 mice (BAYLOR ids) the pole and cue times lie on a\n    10 ms grid, while the 2015 files give them to a microsecond. The photostimulus times are known\n    only through these, so the millisecond latencies of the paper cannot be measured in those files.\n- kind: data_missing\n  statement: The dandiset holds only the ALM recordings. The CN recordings are on Zenodo\n    (doi:10.5281/zenodo.6647629), with 185 sessions and 1212 units against the paper's 169 and 878.\n    The lick times are not in the dandiset (for the ALM sessions they are on CRCNS alm-4, behind a\n    login), and the lesion and behaviour-only sessions and the anatomy are not deposited anywhere\n    found. Nine claims cannot be tested.\n- kind: metadata_insufficient\n  statement: The trial table has no column marking periods when the mouse was not performing (the\n    GoodTrials of the paper's scripts), so that selection cannot be repeated.\n- kind: identifier_missing\n  statement: The 2015 mice are named anm00314746 to anm00314760, while Supplemental Table 1 names them\n    AN105 to AN109; only two (the one with a left fastigial site, and the one dentate mouse) can be\n    matched.\n- kind: metadata_insufficient\n  statement: The genotype of the 9 wild-type mice is given as unknown (the Methods say C57Bl/6), and\n    the electrode table has no positions (NaN) or impedances (-1), so unit depths are not available.\n- kind: other\n  statement: Every unit's waveform is stated as sampled at 20 kHz, including the NeuroNexus recordings\n    that the Methods say were sampled at 25 kHz; the widths agree with the cell type labels at either\n    rate, so the data do not settle which is right.\n- kind: other\n  statement: Two pairs of units in two sessions (BAYLORCD6 2017-06-11 units 48 and 57, anm00314760\n    2015-10-21 units 5 and 37) share 96% and 83% of the smaller unit's spikes within 0.5 ms, likely one\n    neuron sorted twice.\n- kind: paper_inconsistency\n  statement: The Methods say ALM was recorded on the left in 10 mice and on the right in 2, while\n    Supplemental Table 1 lists 13 ALM-recording mice (11 left, 2 right), besides the excluded mouse.\n"
}
```

```
File created successfully at: attempts/000007-gao-2018-01.yaml (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd  python3 - <<'E'
import yaml,json,jsonschema
d=yaml.safe_load(open('attempts/000007-gao-2018-01.yaml'))
jsonschema.validate(d,json.load(open('schemas/attempt.schema.json')))
import collections; print(collections.Counter(o['outcome'] for o in d['outcomes']), len(d['outcomes']))
def walk(x,path=''):
    if isinstance(x,dict):
        for k,v in x.items(): walk(v,path+'/'+str(k))
    elif isinstance(x,list):
        for i,v in enumerate(x): walk(v,path+f'[{i}]')
    elif isinstance(x,str) and ': ' in x: print('COLON',path)
walk(d)
E
grep -n "—\|rather" attempts/000007-gao-2018-01.yaml claims/000007/*.yaml
```

```
Traceback (most recent call last):
  File "<stdin>", line 3, in <module>
  File "/opt/hostedtoolcache/Python/3.13.16/x64/lib/python3.13/site-packages/jsonschema/validators.py", line 1332, in validate
    raise error
jsonschema.exceptions.ValidationError: datetime.date(2026, 10, 19) is not of type 'string'

Failed validating 'type' in schema['properties']['date']:
    {'type': 'string', 'format': 'date'}

On instance['date']:
    datetime.date(2026, 10, 19)
```

**Agent calls Bash**

```bash
cd  python3 - <<'E'
import yaml,collections
d=yaml.safe_load(open('attempts/000007-gao-2018-01.yaml'))
print(collections.Counter(o['outcome'] for o in d['outcomes']), len(d['outcomes']))
def walk(x,path=''):
    if isinstance(x,dict):
        for k,v in x.items(): walk(v,path+'/'+str(k))
    elif isinstance(x,list):
        for i,v in enumerate(x): walk(v,path+f'[{i}]')
    elif isinstance(x,str) and ': ' in x: print('COLON',path)
walk(d)
E
python3 tools/entry.py check entries/000007-gao-2018
```
